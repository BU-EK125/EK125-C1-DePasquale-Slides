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

3. Any `mo.iframe(...)` call left over as a code cell -- same failure,
   same fix in spirit, but mo.iframe's `html` argument is content that
   needs its own `<script>` to actually execute (used for interactive
   widgets, e.g. a quick-check with a button that POSTs a response).
   An earlier version of this fix reconstructed an explicit
   `<iframe srcdoc="...">` wrapper and turned the cell into markdown --
   that renders as a **blank cell on Colab**, no error: Colab's
   markdown-cell sanitizer silently strips `<iframe>` (and `<script>`)
   tags out of markdown *source*, confirmed by a live report of exactly
   this ("the marimo button cell is in the export notebook but it's
   blank") after that version shipped.

   The fix instead turns the cell into a **code cell** that calls
   `IPython.display.HTML(...)` on the widget's HTML directly (no manual
   `<iframe>` wrapper at all -- Colab already hosts every cell's
   *output* in its own sandboxed iframe with script execution enabled,
   confirmed against Colab's own official `advanced_outputs.ipynb`
   sample, which uses this exact `display(HTML('...<script>...'))`
   pattern for a clickable button). Code-cell output and markdown-cell
   source go through different rendering paths in Colab -- output
   produced by the notebook's own kernel is trusted and unsanitized,
   raw HTML pasted in markdown source is not -- so the same HTML that
   silently vanished as markdown works as a code cell's displayed
   output.

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


def as_iframe_cell(source: str):
    """mo.iframe(<literal>, width=..., height=...) -> Python source for a
    code cell that displays the same HTML via `display(HTML(...))`, or
    None if it doesn't match. `width`/`height` are dropped -- Colab
    sizes a code cell's output to its content automatically, and they
    only meant anything for the `<iframe>` wrapper this no longer uses."""
    call = _parse_call(source)
    if call is None or not _is_mo_attr(call.func, "iframe"):
        return None
    if len(call.args) != 1:
        return None
    try:
        inner_html = ast.literal_eval(call.args[0])
        for kw in call.keywords:
            if kw.arg not in ("width", "height"):
                return None
    except ValueError:
        return None
    if not isinstance(inner_html, str):
        return None
    return f"from IPython.display import HTML, display\n\ndisplay(HTML({inner_html!r}))"


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
        html = as_html_cell(source)
        if html is not None:
            cell = {**cell, "cell_type": "markdown", "source": html}
            cell.pop("outputs", None)
            cell.pop("execution_count", None)
        else:
            iframe_code = as_iframe_cell(source)
            if iframe_code is not None:
                cell = {**cell, "source": iframe_code, "outputs": [], "execution_count": None}
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
