"""Fix up a marimo->ipynb export so it actually runs standalone on Colab.

marimo's ipynb exporter flattens every mo.md() call into a real Jupyter
markdown cell, so nothing in the exported notebook actually calls `mo`
anymore -- except two places this script cleans up:

1. The untouched first cell, which still imports marimo. Since marimo
   isn't installed on Colab (and Colab is exactly where this notebook is
   meant to run via the rocket-button link), that leftover import
   throws ModuleNotFoundError as soon as a student runs it, even though
   nothing downstream needs it. Handles two shapes: a cell that is
   *only* `import marimo as mo` gets dropped entirely; a cell that
   imports marimo alongside other, genuinely-needed stdlib imports has
   just the `import marimo as mo` statement removed, keeping the rest --
   found by parsing the cell's AST and filtering out exactly that one
   import statement, not by guessing at cell layout.

2. Any `mo.Html(...)` call left over as a code cell. Unlike mo.md(),
   the exporter does NOT flatten these into markdown -- they're kept as
   a literal `mo.Html(...)` code cell, which fails the same way (`mo`
   is undefined without marimo installed). Used in decks to embed raw
   HTML that marimo's own markdown sanitizer would otherwise strip (e.g.
   a plain <iframe src="...">, no script needed -- see mo.Html's own
   docs: it does NOT execute <script> tags, unlike mo.iframe below).
   Since a plain Jupyter/Colab markdown cell renders raw HTML natively,
   the fix is to pull out the literal string argument and turn the cell
   into a markdown cell containing exactly that HTML -- only for cells
   whose sole content is a `mo.Html("...")` call with a literal string
   argument; anything more dynamic is left alone rather than guessing.

3. Any `mo.iframe(...)` call left over as a code cell -- this is always
   a quick-check widget (the only thing this deck uses `mo.iframe()`
   for): the question text, the GPP-quoted example, the A/B/C/D
   choices, and the actual clickable buttons all live in *one* cell
   now (merged so the buttons render immediately alongside the
   question on the slide, instead of needing an extra advance to
   reveal a separate fragment -- reveal.js/marimo's layout format has
   no "same slide, already visible" option for a second cell, only
   "starts a new slide" or "hidden fragment," confirmed by testing
   both). Only the *interactive* half belongs on Colab's chopping
   block -- the buttons POST to a live Google Form tied to a specific
   lecture's polling, meaningful for a student watching the slide
   during class, not for someone opening this notebook later,
   disconnected from that lecture. The question text is still real
   content worth keeping.

   So the html is split on a literal `<!-- colab-split -->` marker
   placed in the source right before the button row: everything
   *before* it becomes a markdown cell (question, GPP quote, choices --
   the same informational content a plain `mo.md()` cell would have
   flattened to, just extracted from inside the iframe's html string
   instead); everything from the marker onward (the buttons and their
   submit script) is dropped. An `mo.iframe(...)` cell with no marker
   in its html -- i.e. one that's *only* the interactive part, the
   shape this deck used before the merge -- is dropped in full, same
   as always. (Two earlier versions tried keeping the button alive on
   Colab too -- first as a markdown `<iframe srcdoc="...">`, which
   silently rendered blank there since Colab's markdown sanitizer
   strips `<iframe>`/`<script>` tags; then as a code cell calling
   `IPython.display.HTML(...)`, which worked, but was machinery for a
   widget that doesn't actually belong in an async notebook.)

4. A markdown cell whose *entire* content is a hand-typed ```python
   fence immediately followed by a hand-typed plain ``` output fence
   (optionally with a short trailing caption after it) -- the
   slides-side convention for a demo cell that shouldn't visibly
   execute on the slide (see CONVENTIONS.md). On Colab there's no
   reason to leave this as inert text: Colab runs `print()`/`input()`
   cells completely normally (no slides-layout bug to dodge), so this
   splits the cell back into a real, runnable code cell (the extracted
   ```python body, unindented) followed by a markdown cell for any
   trailing caption -- the hand-typed *output* fence is dropped
   entirely, since running the cell for real produces its own output.
"""

import ast
import hashlib
import json
import re
import sys

path = sys.argv[1]

with open(path) as f:
    nb = json.load(f)


def _parse_call(source: str):
    """Return the parsed ast.Call if source is exactly one call expression."""
    try:
        tree = ast.parse(source.strip())
    except SyntaxError:
        return None
    if len(tree.body) != 1 or not isinstance(tree.body[0], ast.Expr):
        return None
    call = tree.body[0].value
    return call if isinstance(call, ast.Call) else None


def _is_mo_attr(func, name: str) -> bool:
    return (
        isinstance(func, ast.Attribute)
        and func.attr == name
        and isinstance(func.value, ast.Name)
        and func.value.id == "mo"
    )


def as_html_cell(source: str):
    """mo.Html(<literal>) -> the literal HTML string, or None if it doesn't match."""
    call = _parse_call(source)
    if call is None or not _is_mo_attr(call.func, "Html"):
        return None
    if len(call.args) != 1 or call.keywords:
        return None
    try:
        value = ast.literal_eval(call.args[0])
    except ValueError:
        return None
    return value if isinstance(value, str) else None


_COLAB_SPLIT_MARKER = "<!-- colab-split -->"


def as_iframe_colab_cell(source: str):
    """mo.iframe(<literal>, ...) -> see docstring case 3. Returns None if
    `source` isn't an mo.iframe() call at all (caller should leave it
    alone); otherwise ("markdown", html) with the informational html
    before the colab-split marker, or ("drop", None) if there's no
    marker (the whole cell is purely the interactive button widget)."""
    call = _parse_call(source)
    if call is None or not _is_mo_attr(call.func, "iframe"):
        return None
    if len(call.args) != 1:
        return None
    try:
        html = ast.literal_eval(call.args[0])
    except ValueError:
        return None
    if not isinstance(html, str):
        return None
    if _COLAB_SPLIT_MARKER in html:
        before, _, _ = html.partition(_COLAB_SPLIT_MARKER)
        return ("markdown", before.strip())
    return ("drop", None)


_HANDTYPED_CODE_OUTPUT_RE = re.compile(
    r"\A```python\n(?P<code>.*?)\n```\n\n```\n(?:.*?)\n```\n?(?P<trailing>.*)\Z",
    re.DOTALL,
)


def split_handtyped_code_cell(source: str):
    """A markdown cell that is *only* a ```python fence followed by a
    plain ``` output fence (see docstring case 4) -> (code, trailing)
    where `trailing` is any caption text after the output fence (or ""
    if none), or None if the cell doesn't match this exact shape."""
    match = _HANDTYPED_CODE_OUTPUT_RE.match(source.strip())
    if match is None:
        return None
    return match.group("code"), match.group("trailing").strip()


def _is_import_marimo_as_mo(stmt) -> bool:
    return (
        isinstance(stmt, ast.Import)
        and len(stmt.names) == 1
        and stmt.names[0].name == "marimo"
        and stmt.names[0].asname == "mo"
    )


def without_marimo_import(source: str):
    """Drop an `import marimo as mo` statement from a cell's top level,
    keeping any other statements as-is. Returns None when the cell has
    no such import at all (caller should leave the cell untouched);
    otherwise returns the reconstructed source with that one import
    removed, or "" when nothing else was left in the cell (caller
    should drop the whole cell)."""
    try:
        tree = ast.parse(source.strip())
    except SyntaxError:
        return None
    if not any(_is_import_marimo_as_mo(stmt) for stmt in tree.body):
        return None
    remaining = [stmt for stmt in tree.body if not _is_import_marimo_as_mo(stmt)]
    if not remaining:
        return ""
    return "\n".join(ast.unparse(stmt) for stmt in remaining)


new_cells = []
for cell in nb["cells"]:
    source = "".join(cell["source"])
    if cell["cell_type"] == "code":
        without_mo = without_marimo_import(source)
        if without_mo is not None:
            if without_mo == "":
                continue
            cell = {**cell, "source": without_mo}
            new_cells.append(cell)
            continue
        iframe_result = as_iframe_colab_cell(source)
        if iframe_result is not None:
            kind, content = iframe_result
            if kind == "markdown":
                cell = {**cell, "cell_type": "markdown", "source": content}
                cell.pop("outputs", None)
                cell.pop("execution_count", None)
                new_cells.append(cell)
            continue
        html = as_html_cell(source)
        if html is not None:
            cell = {**cell, "cell_type": "markdown", "source": html}
            cell.pop("outputs", None)
            cell.pop("execution_count", None)
    elif cell["cell_type"] == "markdown":
        split = split_handtyped_code_cell(source)
        if split is not None:
            code, trailing = split
            new_cells.append(
                {**cell, "cell_type": "code", "source": code, "outputs": [], "execution_count": None}
            )
            if trailing:
                # Derived deterministically from the original cell's id (not
                # random) -- build_slides.sh's CI check re-runs this script
                # and diffs the result against what's committed, so a fresh
                # id on every run would never match.
                caption_id = hashlib.sha1(f"{cell['id']}-caption".encode()).hexdigest()[:8]
                new_cells.append(
                    {**cell, "cell_type": "markdown", "source": trailing, "id": caption_id}
                )
            continue
    new_cells.append(cell)

nb["cells"] = new_cells

with open(path, "w") as f:
    json.dump(nb, f, indent=1)
    f.write("\n")
