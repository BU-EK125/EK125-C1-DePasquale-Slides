import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class9.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Moving to PyCharm

    ### From Colab Notebooks to Running Python Locally

    *Class 9*

    📖 [Full reading: Class 9](https://BU-EK125.github.io/EK125/class/Class9.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Why Make the Shift?

    Colab gave everyone the same environment from day one — no install,
    no setup, just a browser. That was perfect for learning the
    fundamentals. But it has a real limitation as programs grow.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - Colab code lives in **separate cells** — their relationships
      depend on the order you happen to run them.
    - Restart the notebook and run cells out of order, and things break
      in confusing ways.
    - Real Python programs are **single `.py` files** that run top to
      bottom in one shot, every time — no ambiguity about what's run.
    - Starting this week: **PyCharm**, an IDE (Integrated Development
      Environment) — an editor, a runner, and a debugger bundled into
      one application.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## What's an IDE, Generally?

    "Integrated" is the key word — PyCharm bundles several tools that
    you'd otherwise juggle separately into one application:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - **A file browser for your whole project** — not just one
      notebook. See every `.py` file you've created, organized into
      folders, and jump between them instantly.
    - **A smarter editor** — syntax highlighting and autocomplete that
      knows your variable and function names, not just keywords.
    - **One-click running** — no cell-by-cell execution. Run the whole
      file and watch the output appear in a console panel.
    - **A debugger** — step through your code one line at a time and
      watch your variables change, instead of guessing from `print()`
      statements alone. (More on this in a later class.)
    - **Error underlining as you type** — a misspelled variable or
      missing colon gets flagged immediately, before you even run the
      file.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## What's Actually Different

    A few concrete differences between a Colab notebook and a local
    `.py` file in PyCharm:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - **Execution order**: Colab — you choose which cells run and when.
      PyCharm — the file always runs top to bottom.
    - **Output**: Colab — appears below each cell. PyCharm — appears in
      a console/terminal panel at the bottom.
    - **Saving**: Colab — auto-saved to Drive. PyCharm — a real file on
      your computer.
    - **Internet**: Colab — required. PyCharm — not required.
    - **`input()`**: works in both, but feels much more natural in
      PyCharm's console — the prompt and your typed answer sit on the
      same line, like a real program.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### The One Thing That Will Trip You Up

    In Colab, a bare expression on the last line of a cell
    automatically displays its value. In a `.py` file, **nothing is
    displayed unless you explicitly `print()` it.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    x = 10
    x + 5          # Colab: shows 15 below the cell. PyCharm: shows nothing.
    print(x + 5)   # Shows 15 in both.
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    🚩 **Common mistake:** writing a `.py` file the way you wrote Colab
    cells — a bare expression like `x + 5` or `total` on its own line,
    expecting to see the value. This does **nothing** and produces no
    error, so it's easy to miss. If your program "runs" but shows no
    output at all, check for a missing `print()` first.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Quick Review: List Comprehensions

    Before we start today's GPP help, a quick refresher on the Class 7
    tools you'll need. A list comprehension builds a list in one line:
    `[expression for i in iterable]`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    cubelist = [i**3 for i in range(5)]
    print(cubelist)
    ```

    ```
    [0, 1, 8, 27, 64]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Quick Review: Adding a Condition

    An `if` at the end filters which values make it into the list:
    `[expression for i in iterable if condition]`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    cubelisteven = [i**3 for i in range(7) if i % 2 == 0]
    print(cubelisteven)
    ```

    ```
    [0, 8, 64, 216]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Quick Review: Nested Structures

    Nesting one comprehension inside another builds a table — the
    inner comprehension builds one row, the outer repeats it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    products = [[r * c for c in range(1, 5)] for r in range(1, 4)]
    for row in products:
        print(row)
    ```

    ```
    [1, 2, 3, 4]
    [2, 4, 6, 8]
    [3, 6, 9, 12]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Why This Matters Today

    `enumerate()`, list comprehensions, and conditional comprehensions
    are exactly the tools Problem 1 of today's homework needs — now in
    a `.py` file instead of a notebook cell.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## HW5 Problem 1: Water Quality Lab

    A water quality lab records turbidity measurements (in NTU) from 5
    river monitoring stations:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    station_names = ["Upstream", "Bridge A", "Mill Pond",
                      "Bridge B", "Downstream"]
    turbidity = [2.1, 3.8, 12.4, 8.7, 5.2]
    ```

    Four parts, each asking for a different way to process this data.
    Let's think through the *logic* of each one — not the final code.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### General Strategy: Breaking the Problem Into Parts

    Before writing any code, figure out the shape of the whole problem.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    This problem has **4 parts (A–D)**, and all 4 start from the same
    two lists above. None of them depend on each other — you can do
    them in any order, though working top to bottom matches how the
    file is already laid out.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    What each part actually asks for:

    - **Part A** — *print* a numbered report. Needs a position and a
      value together, on every line.
    - **Part B** — *build a new list*, converting every reading to a
      different unit.
    - **Part C** — *build another new list*, keeping only the names
      that pass a test.
    - **Part D** — *print* a subset, visiting every other station.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Notice the split: A and D just **print**; B and C **build a new
    list**. That distinction — am I displaying something, or creating
    something to use later? — is the first question worth asking for
    any part of any problem.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Part A: Numbered Report

    Print a numbered report of each station and its reading, using
    `enumerate()` — not `range(len(...))`.

    ```
    Station 1 - Upstream: 2.1 NTU
    Station 2 - Bridge A: 3.8 NTU
    ...
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - `enumerate()` is the tool here precisely because you need **two**
      things on every line: a position *and* a value.
    - It hands you both — but it counts from 0, and the report needs
      to count from 1. What's the one-line fix that turns a 0-based
      index into the label "Station 1"?
    - The index you get from `enumerate(station_names)` is the *same*
      index that lines up with `turbidity` — that's how you pull the
      matching reading from the other list.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Part B: Unit Conversion

    Use a **list comprehension** to convert every reading to FTU
    (1 NTU = 1.05 FTU), rounded to 2 decimal places, into a new list
    `ftu_readings`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - Say the loop version out loud first: for each reading, multiply
      by the conversion factor, round it, and collect it. The
      comprehension is that exact sentence, compressed.
    - In `[expression for item in iterable]`, what's your `item`
      here, and what's the `expression`?
    - `round(...)` goes around *each* converted value — not around the
      whole list after the fact. Where in your expression does it go?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Part C: Flagging High Readings

    Use a **list comprehension with a condition** to build
    `high_stations` — the *names* of stations whose turbidity is
    **above** 5.0 NTU.

    ```
    ['Mill Pond', 'Bridge B', 'Downstream']
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - You're testing one list (`turbidity`) but collecting from the
      *other* one (`station_names`). What do you need — the index, or
      just the value — to pull the matching name out of a different
      list?
    - Where does the `if` go in a comprehension: before the `for`, or
      after it?
    - "Above" means strictly greater than — `>`, not `>=`. A station
      reading exactly 5.0 would *not* belong in the result. Double
      check which comparison you reach for by habit.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Part D: Scheduled Sampling

    Using `range()` **with a step** (not `enumerate()`, not direct
    iteration), print every other station name starting from index 0.

    ```
    Scheduled sampling stations:
    Upstream
    Mill Pond
    Downstream
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - `range()` takes up to three arguments: start, stop, step. Which
      three values give you exactly the indices 0, 2, 4?
    - Should your stop value be a hard-coded `5`, or something that
      still works if the lab adds a sixth station?
    - `range()` hands you *numbers*, not station names — you still
      need to index into `station_names` with each number to get the
      actual string to print.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Now It's Your Turn

    Same tools, your own data — work through Problem 1 in PyCharm, run
    it often, and check your output against the expected results in
    the assignment.

    📝 [Today's GPP](https://BU-EK125.github.io/EK125/gpps/Class9_GPP.html)
    """)
    return


if __name__ == "__main__":
    app.run()
