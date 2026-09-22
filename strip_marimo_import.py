"""Remove the leftover `import marimo as mo` cell from a marimo->ipynb export.

marimo's ipynb exporter flattens every mo.md() call into a real Jupyter
markdown cell, so nothing in the exported notebook actually calls `mo`
anymore -- except the untouched first cell, which still imports it. Since
marimo isn't installed on Colab (and Colab is exactly where this notebook
is meant to run via the rocket-button link), that leftover import cell
throws ModuleNotFoundError as soon as a student runs it, even though
nothing downstream needs it.

Only removes a cell if its source is *exactly* `import marimo as mo`
(nothing else) -- if a deck's first cell ever grows real setup code
alongside the marimo import, this leaves it alone rather than guessing.
"""

import json
import sys

path = sys.argv[1]

with open(path) as f:
    nb = json.load(f)

nb["cells"] = [
    cell
    for cell in nb["cells"]
    if not (
        cell["cell_type"] == "code"
        and "".join(cell["source"]).strip() == "import marimo as mo"
    )
]

with open(path, "w") as f:
    json.dump(nb, f, indent=1)
    f.write("\n")
