"""Fix up a marimo->ipynb export so it actually runs standalone on Colab.

marimo's ipynb exporter flattens every mo.md() call into a real Jupyter
markdown cell, so nothing in the exported notebook actually calls `mo`
anymore -- except two places this script cleans up:

1. The untouched first cell, which still imports marimo. Since marimo
   isn't installed on Colab (and Colab is exactly where this notebook is
   meant to run via the rocket-button link), that leftover import cell
   throws ModuleNotFoundError as soon as a student runs it, even though
   nothing downstream needs it. Removed only when a cell's source is
   *exactly* `import marimo as mo` (nothing else) -- if a deck's first
   cell ever grows real setup code alongside the marimo import, this
   leaves it alone rather than guessing.

2. Any `mo.Html(...)` call left over as a code cell. Unlike mo.md(),
   the exporter does NOT flatten these into markdown -- they're kept as
   a literal `mo.Html(...)` code cell, which fails the same way (`mo`
   is undefined without marimo installed). These are used in decks to
   embed raw HTML that marimo's own markdown sanitizer would otherwise
   strip (e.g. an <iframe>). Since a plain Jupyter/Colab markdown cell
   renders raw HTML natively with no sanitization, the fix is to pull
   out the literal string argument and turn the cell into a markdown
   cell containing exactly that HTML -- only for cells whose sole
   content is a `mo.Html("...")` call with a literal string argument;
   anything more dynamic is left alone rather than guessing.
"""

import ast
import json
import sys

path = sys.argv[1]

with open(path) as f:
    nb = json.load(f)


def as_html_literal(source: str):
    """Return the literal string argument if source is exactly mo.Html(<literal>), else None."""
    try:
        tree = ast.parse(source.strip())
    except SyntaxError:
        return None
    if len(tree.body) != 1 or not isinstance(tree.body[0], ast.Expr):
        return None
    call = tree.body[0].value
    if not isinstance(call, ast.Call):
        return None
    func = call.func
    is_mo_html = (
        isinstance(func, ast.Attribute)
        and func.attr == "Html"
        and isinstance(func.value, ast.Name)
        and func.value.id == "mo"
    )
    if not is_mo_html or len(call.args) != 1 or call.keywords:
        return None
    try:
        value = ast.literal_eval(call.args[0])
    except ValueError:
        return None
    return value if isinstance(value, str) else None


new_cells = []
for cell in nb["cells"]:
    source = "".join(cell["source"])
    if cell["cell_type"] == "code" and source.strip() == "import marimo as mo":
        continue
    if cell["cell_type"] == "code":
        html = as_html_literal(source)
        if html is not None:
            cell = {**cell, "cell_type": "markdown", "source": html}
            cell.pop("outputs", None)
            cell.pop("execution_count", None)
    new_cells.append(cell)

nb["cells"] = new_cells

with open(path, "w") as f:
    json.dump(nb, f, indent=1)
    f.write("\n")
