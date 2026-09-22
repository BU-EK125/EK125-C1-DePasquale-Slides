"""Fix up a marimo->ipynb export so it actually runs standalone on Colab.

marimo's ipynb exporter flattens every mo.md() call into a real Jupyter
markdown cell, so nothing in the exported notebook actually calls `mo`
anymore -- except three places this script cleans up:

1. The untouched first cell, which still imports marimo. Since marimo
   isn't installed on Colab (and Colab is exactly where this notebook is
   meant to run via the rocket-button link), that leftover import
   throws ModuleNotFoundError as soon as a student runs it, even though
   nothing downstream needs it. Handles two shapes: a cell that is
   *only* `import marimo as mo` gets dropped entirely; a cell that
   imports marimo alongside other, genuinely-needed stdlib imports
   (e.g. `import contextlib` / `import io`, needed by #4 below on the
   slides side but not referenced at all once #4 is reverted for Colab)
   has just the `import marimo as mo` statement removed, keeping the
   rest -- found by parsing the cell's AST and filtering out exactly
   that one import statement, not by guessing at cell layout.

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
   same fix in spirit, but mo.iframe's `html` argument is content
   rendered inside a real sandboxed <iframe srcdoc="...">, not raw page
   HTML, specifically because scripts DO execute inside an iframe's own
   document (used for interactive widgets, e.g. a quick-check with a
   button that POSTs a response). Converting this to a plain markdown
   cell containing the raw HTML+<script> wouldn't work the same way --
   Jupyter/Colab's markdown renderer doesn't execute inline <script>
   tags either. So instead this reconstructs the same <iframe
   srcdoc="..."> wrapper explicitly (srcdoc-escaping the HTML), which
   already renders fine in Colab's markdown (confirmed: a plain iframe
   embed already works there) and, because it's a genuine iframe
   document, still executes its own script the same way it does on the
   live slide.

4. `<buf> = io.StringIO()` followed by
   `with contextlib.redirect_stdout(<buf>): <body>` followed by
   `mo.md(f"​```\n{<buf>.getvalue()}\n​```")`. This pattern exists purely
   to work around a marimo *slides*-layout bug: a code cell whose only
   effect is print() (no returned value) is silently dropped from the
   rendered slide entirely -- the code runs, but nothing shows, not even
   an empty space. Capturing stdout and re-returning it via mo.md() is
   the fix on the slides side. `contextlib.redirect_stdout` (not
   `mo.capture_stdout`) is used deliberately so the visible, live code
   on the slide is standard-library Python, not marimo-specific -- but
   redirecting stdout into a buffer and never printing that buffer back
   out would show *no* output at all on Colab (a real
   `contextlib.redirect_stdout` silences the terminal, same as it does
   anywhere else), and the trailing `mo.md()` call fails outright
   without marimo installed regardless. So, same as the fix below, this
   cell type gets *reverted* for Colab: pull the original body back out
   from inside the `with` block, drop the `io.StringIO()` assignment,
   the `with` wrapper, and the trailing `mo.md()` call entirely, leaving
   plain executable print() code, unindented, as its own code cell --
   exactly what it looked like before this workaround existed.
"""

import ast
import html as html_module
import json
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
    """mo.iframe(<literal>, width=..., height=...) -> a reconstructed
    <iframe srcdoc="..."> tag, or None if it doesn't match."""
    call = _parse_call(source)
    if call is None or not _is_mo_attr(call.func, "iframe"):
        return None
    if len(call.args) != 1:
        return None
    try:
        inner_html = ast.literal_eval(call.args[0])
        kwargs = {}
        for kw in call.keywords:
            if kw.arg not in ("width", "height"):
                return None
            kwargs[kw.arg] = ast.literal_eval(kw.value)
    except ValueError:
        return None
    if not isinstance(inner_html, str):
        return None
    width = kwargs.get("width", "100%")
    height = kwargs.get("height", "400px")
    escaped = html_module.escape(inner_html, quote=True)
    return (
        f'<iframe srcdoc="{escaped}" width="{width}" height="{height}" '
        'frameborder="0"></iframe>'
    )


def _is_call_to(node, module: str, attr: str) -> bool:
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == attr
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == module
    )


def as_unwrapped_print_cell(source: str):
    """`<buf> = io.StringIO()` + `with contextlib.redirect_stdout(<buf>): <body>`
    + `mo.md(f"```\n{<buf>.getvalue()}\n```")`, optionally preceded by other
    top-level statements (an import, a random.seed() call, ...) -- ->
    those leading statements plus the unindented with-body as plain code,
    or None if it doesn't match."""
    try:
        tree = ast.parse(source.strip())
    except SyntaxError:
        return None
    if len(tree.body) < 3:
        return None
    *leading_stmts, assign_stmt, with_stmt, md_stmt = tree.body
    if not (
        isinstance(assign_stmt, ast.Assign)
        and len(assign_stmt.targets) == 1
        and isinstance(assign_stmt.targets[0], ast.Name)
        and _is_call_to(assign_stmt.value, "io", "StringIO")
    ):
        return None
    buf_name = assign_stmt.targets[0].id
    if not isinstance(with_stmt, ast.With) or len(with_stmt.items) != 1:
        return None
    item = with_stmt.items[0]
    if not (
        _is_call_to(item.context_expr, "contextlib", "redirect_stdout")
        and len(item.context_expr.args) == 1
        and isinstance(item.context_expr.args[0], ast.Name)
        and item.context_expr.args[0].id == buf_name
        and item.optional_vars is None
    ):
        return None
    if not isinstance(md_stmt, ast.Expr) or not isinstance(md_stmt.value, ast.Call):
        return None
    md_call = md_stmt.value
    if not _is_mo_attr(md_call.func, "md") or len(md_call.args) != 1:
        return None
    fstring = md_call.args[0]
    if not isinstance(fstring, ast.JoinedStr):
        return None
    # Confirm the f-string is exactly the capture-and-fence pattern this
    # script generates (```\n{buf.getvalue()}\n```) -- not some other,
    # more dynamic use of mo.md() this script shouldn't touch.
    uses_expected_buf = any(
        isinstance(v, ast.FormattedValue)
        and isinstance(v.value, ast.Call)
        and isinstance(v.value.func, ast.Attribute)
        and v.value.func.attr == "getvalue"
        and isinstance(v.value.func.value, ast.Name)
        and v.value.func.value.id == buf_name
        for v in fstring.values
    )
    if not uses_expected_buf:
        return None
    return "\n".join(
        ast.unparse(stmt) for stmt in [*leading_stmts, *with_stmt.body]
    )


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
        unwrapped = as_unwrapped_print_cell(source)
        if unwrapped is not None:
            cell = {**cell, "source": unwrapped}
            new_cells.append(cell)
            continue
        html = as_html_cell(source)
        if html is None:
            html = as_iframe_cell(source)
        if html is not None:
            cell = {**cell, "cell_type": "markdown", "source": html}
            cell.pop("outputs", None)
            cell.pop("execution_count", None)
    new_cells.append(cell)

nb["cells"] = new_cells

with open(path, "w") as f:
    json.dump(nb, f, indent=1)
    f.write("\n")
