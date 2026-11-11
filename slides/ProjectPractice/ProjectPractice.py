import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/ProjectPractice.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # EK125 Exam 2

    ### Project Practice

    A battery-rig scenario built around the project skills: reading
    a contract, writing a stub, tracing, and debugging.

    📖 Work through each problem yourself, then use this deck to
    check your answer and pick up a few extra tips.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 1: Bugs Live at the Seams (a)

    ```python
    def summarize_loads(loads):
        """Returns: "peak_kn" and "mean_kn"."""
        # ... (correct code, not shown) ...

    def print_summary(summary):
        print(f"Peak: {summary['peak']} kN")

    print_summary(summarize_loads([9.0, 12.5, 8.0]))
    ```

    What error does the last line produce?
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `KeyError: 'peak'`

    `print_summary` asks for `"peak"`, but the contract promises
    `"peak_kn"`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 18](https://BU-EK125.github.io/EK125/class/Class18.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 1 (b)

    Which function is off-contract — and how do you know?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ `print_summary` is off-contract

    The contract for `summarize_loads` promises `"peak_kn"`;
    `print_summary` reads `"peak"` instead. Fix the reader, not
    the function that's following its own contract:

    ```python
    print(f"Peak: {summary['peak_kn']} kN")
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 18](https://BU-EK125.github.io/EK125/class/Class18.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 1 (c)

    Suppose `summarize_loads` instead received loads in **newtons**
    (`[9000.0, 12500.0, 8000.0]`). After the key fix, what prints?
    Syntax, runtime, or logic error — and how would the team catch
    it?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `Peak: 12500.0 kN` — a logic error

    No crash, just a wrong unit. Catch it with a reasonableness
    check: 12,500 kN on a bridge sensor isn't physically
    believable.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 18](https://BU-EK125.github.io/EK125/class/Class18.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 2: Write a Precise Contract (a)

    ```python
    def load_cycles(filename):
        """Reads the battery data and returns it."""
    ```

    List three questions a teammate couldn't answer from this.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Any three of

    Is the return a dict or a list? What are the exact keys? Are
    values `int` or `float`? What happens to blank or `-999`
    rows? What units? Does it print anything?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 15](https://BU-EK125.github.io/EK125/class/Class15.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 2 (b)

    Rewrite the *Returns* section so no question is left. Rule:
    rows with a blank or `-999` capacity are skipped; result is a
    dict of lists.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    """Returns: dict of lists, keys "cycle" (int),
    "voltage" (float), "capacity_mah" (float). All
    three lists are the same length, in file order.
    Rows with any blank, or capacity -999, are
    skipped entirely.
    Example: {"cycle": [1, 4], "voltage": [3.71,
    3.68], "capacity_mah": [2950.0, 2880.0]}
    """
    ```

    💡 Double-check your own example against the sample file —
    it's easy to accidentally keep a row the contract says to
    skip.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 15](https://BU-EK125.github.io/EK125/class/Class15.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 3: Faithful Stubs (a)

    Contract: `assess_cell` returns `{"cell_id", "fade_pct",
    "passed"}`. Which stub bodies are faithful?

    ```python
    A: return {"cell_id": cell_id, "fade_pct": 12.5,
               "passed": True}
    B: print({"cell_id": cell_id, "fade_pct": 12.5,
              "passed": True})
    C: return {"cell": cell_id, "fade_pct": 12.5,
               "passed": True}
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ A: Yes. B: No. C: No.

    A returns the example, using the real parameter. B prints
    instead of returning — the function gives back `None`. C
    misspells the key (`"cell"` instead of `"cell_id"`) — a
    `KeyError` waiting to happen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 16](https://BU-EK125.github.io/EK125/class/Class16.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 3 (a), continued

    ```python
    # D: fade_pct is a string
    return {
        "cell_id": cell_id,
        "fade_pct": "12.5",
        "passed": True,
    }
    ```
    ```python
    # E: passed is a string
    return {
        "cell_id": cell_id,
        "fade_pct": 12.5,
        "passed": "True",
    }
    ```
    ```python
    # F: a list, not a dict
    return [cell_id, 12.5, True]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ D: No. E: No. F: No.

    D's `fade_pct` is a string, not a float. E's `passed` is the
    *string* `"True"`, not the boolean `True` — `if result["passed"]`
    would be true even for `"False"`! F returns a list with no
    keys at all.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 16](https://BU-EK125.github.io/EK125/class/Class16.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 3 (b)

    A stub hard-codes `cell_id: "B7"`. The program calls it for
    "B1", "B2", "B3". What does the report show, and why pass
    `cell_id` through instead?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Every line says "B7"

    It runs, but you can't tell whether `main.py` passed the right
    IDs. Passing `cell_id` through lets the skeleton prove each
    argument arrived where it should.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 16](https://BU-EK125.github.io/EK125/class/Class16.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 4: Importing Your Own Files (a)

    ```python
    # cellmath.py
    def to_percent(fraction):
        return fraction * 100

    print("cellmath loaded")

    def test_to_percent():
        print("test:", to_percent(0.25))

    if __name__ == "__main__":
        test_to_percent()
    ```
    ```python
    # main.py
    from cellmath import to_percent
    print("main starts")
    print(to_percent(0.5))
    ```

    Output when you run `main.py`?
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer

    ```
    cellmath loaded
    main starts
    50.0
    ```

    Importing runs every top-level line in `cellmath.py` first —
    that's the `print("cellmath loaded")` line.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 16](https://BU-EK125.github.io/EK125/class/Class16.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 4 (b)

    Output when you run `cellmath.py` directly instead?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer

    ```
    cellmath loaded
    test: 25.0
    ```

    `test_to_percent()` only runs here, because `__name__` equals
    `"__main__"` only when the file itself is run directly.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 16](https://BU-EK125.github.io/EK125/class/Class16.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 4 (c)

    Which line in `cellmath.py` causes trouble for teammates, and
    where should it go instead?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `print("cellmath loaded")`

    It runs every time anyone imports the file. Delete it, or move
    it inside `test_to_percent()`, under the `__name__` guard.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 16](https://BU-EK125.github.io/EK125/class/Class16.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 4 (d)

    What error does each import line cause, in `main.py`?

    1. `from cellmath.py import to_percent`
    2. `from cellmath import to_pct`
    3. `from cellMath import to_percent`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answers

    1. `ModuleNotFoundError` — no `.py` in an import.
    2. `ImportError: cannot import name 'to_pct'` — file found,
       function name wrong.
    3. `ModuleNotFoundError` — capitalization must match exactly.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 16](https://BU-EK125.github.io/EK125/class/Class16.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 5: Read a Traceback Across Files (a)

    ```
    Traceback (most recent call last):
      File "main.py", line 9, in <module>
        line = format_cell(result)
      File "formatter.py", line 6, in format_cell
        return f"{result['cell_id']}..."
    TypeError: 'NoneType' not subscriptable
    ```

    Line 8 of `main.py` is `result = assess_cell(...)`. In which
    file, function, and line did the program crash?
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `formatter.py`, in `format_cell`, line 6

    Read bottom-up: the last frame shown is where the crash
    actually happened.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 18](https://BU-EK125.github.io/EK125/class/Class18.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 5 (b)

    Which variable is `None`? Which function created that value?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `result` is `None`

    It was created by `assess_cell` in `analyzer.py` (main.py line
    8), then handed to `format_cell`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 18](https://BU-EK125.github.io/EK125/class/Class18.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 5 (c)

    What's the most likely mistake inside `assess_cell`? Whose job
    is it to fix?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ It prints instead of returning

    (Or a `return` sits inside an `if` that never runs.) The owner
    of `analyzer.py` fixes it in their own file — the crash site
    (`formatter.py`) is not the bug site.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 18](https://BU-EK125.github.io/EK125/class/Class18.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 5 (d)

    Write one temporary line, added between lines 8 and 9 of
    `main.py`, that would confirm your answer to (b).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    print("SEAM type:", type(result))
    ```

    It would show `<class 'NoneType'>` instead of the expected
    `<class 'dict'>`.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 18](https://BU-EK125.github.io/EK125/class/Class18.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 6: Name the Bug, Fix It (a)

    ```python
    readings = ["3.7", "", "3.9"]
    volts = []
    for text in readings:
        volts.append(float(text))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ RUNTIME

    `ValueError: could not convert string to float: ''`. Fix: only
    convert non-blank text.

    ```python
    if text != "":
        volts.append(float(text))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 19](https://BU-EK125.github.io/EK125/class/Class19.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 6 (b)

    ```python
    if voltage > 4.2
        print("Overcharged!")
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ SYNTAX

    Missing colon. Fix: `if voltage > 4.2:`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 19](https://BU-EK125.github.io/EK125/class/Class19.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 6 (c)

    ```python
    def total_all(values):
        """Return the sum of ALL values."""
        total = 0
        for i in range(1, len(values)):
            total = total + values[i]
        return total
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ LOGIC

    Skips index 0 — `total_all([5, 1, 2])` returns 3, not 8. Fix:

    ```python
    for i in range(len(values)):
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 19](https://BU-EK125.github.io/EK125/class/Class19.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 6 (d)

    ```python
    def count_drops(values):
        drops = 0
        for i in range(len(values)):
            if values[i + 1] < values[i]:
                drops = drops + 1
        return drops
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ RUNTIME

    `IndexError` on the last pass, when `i + 1` runs past the end.
    Fix:

    ```python
    for i in range(len(values) - 1):
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 19](https://BU-EK125.github.io/EK125/class/Class19.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 6 (e)

    ```python
    def sum_list(values):
        total = 0
        for v in values:
            total = total + v

    sum_list([1, 2])
    print(total)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ RUNTIME

    `NameError: name 'total' is not defined` — `total` is local to
    the function, which never returns it. Fix both ends:

    ```python
    return total       # last line of the function
    result = sum_list([1, 2])
    print(result)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 19](https://BU-EK125.github.io/EK125/class/Class19.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 6 (f)

    ```python
    result = {"cell_id": "B7", "fade_pct": 12.5}
    print(result["fade"])
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ RUNTIME

    `KeyError: 'fade'`. Fix:

    ```python
    print(result["fade_pct"])
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 19](https://BU-EK125.github.io/EK125/class/Class19.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 7: Debug Against the Contract (a)

    ```python
    def worst_cycle(data, limit):
        """worst_cycle (int): EARLIEST on a tie.
        below_limit (int): STRICTLY below limit."""
        caps = data["capacity_mah"]
        worst_pos = 0
        below = 0
        for i in range(len(caps)):
            if caps[i] <= caps[worst_pos]:
                worst_pos = i
            if caps[i] <= limit:
                below = below + 1
        ...
    ```

    Trace it for `caps = [2950, 2800, 2900, 2800, 2850]`,
    `limit = 2850.0`: what's `worst_pos` and `below` after each
    pass?
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Trace

    | i | caps[i] | worst_pos | below |
    |---|---|---|---|
    | 0 | 2950 | 0 | 0 |
    | 1 | 2800 | 1 | 1 |
    | 2 | 2900 | 1 | 1 |
    | 3 | 2800 | 3 | 2 |
    | 4 | 2850 | 3 | 3 |

    At i=0, `2950 <= 2950` is True, so `worst_pos` is set to 0
    again (no real change).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 19](https://BU-EK125.github.io/EK125/class/Class19.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 7 (b)

    What does the function return as written? What *should* it
    return?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ As written: cycle 400, below 3. Correct: cycle 200, below 2.

    Two bugs are hiding in those two numbers — find them in the
    next part.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 19](https://BU-EK125.github.io/EK125/class/Class19.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 7 (c)

    Find and fix the two bugs.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Two bugs

    `<=` should be `<` on the tie check — with `<=`, a tie moves
    to the *later* cycle, but the contract wants the earliest:

    ```python
    if caps[i] < caps[worst_pos]:
    ```

    `<=` should be `<` on the limit check — the contract says
    *strictly* below:

    ```python
    if caps[i] < limit:
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 19](https://BU-EK125.github.io/EK125/class/Class19.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 7 (d)

    Write two `check()` calls that FAIL on the buggy code and
    PASS on the fixed code: one for the tie, one for the boundary.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    tied = {"cycle": [1, 2],
            "capacity_mah": [2800.0, 2800.0]}
    check("tie picks earliest", 1,
          worst_cycle(tied, 2000.0)["worst_cycle"])
    ```
    ```python
    at_limit = {"cycle": [1],
                "capacity_mah": [2850.0]}
    result = worst_cycle(at_limit, 2850.0)
    check("at limit, not below", 0,
          result["below_limit"])
    ```

    A test with no tie and no boundary value would PASS on both
    the buggy and fixed code — it wouldn't catch either bug.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 17](https://BU-EK125.github.io/EK125/class/Class17.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 8: Write the Tests First (a)

    ```python
    def percent_in_range(values, low, high):
        """AT OR ABOVE low, AT OR BELOW high,
        rounded to 1 decimal. Empty: returns 0.0."""
    ```

    Write four `check()` calls from the contract alone, before the
    function exists: a normal case, a boundary case, an empty
    list, and a rounding case.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Four tests

    ```python
    vals = [3.0, 3.5, 4.5, 2.5]
    ends = [3.0, 4.2]
    rounder = [3.5, 5.0, 5.0]
    check("normal", 50.0,
          percent_in_range(vals, 3.0, 4.2))
    check("both ends count", 100.0,
          percent_in_range(ends, 3.0, 4.2))
    check("empty list", 0.0,
          percent_in_range([], 3.0, 4.2))
    check("rounds", 33.3,
          percent_in_range(rounder, 3.0, 4.2))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 17](https://BU-EK125.github.io/EK125/class/Class17.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 8 (b)

    Now write `percent_in_range` so all four tests pass.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    def percent_in_range(values, low, high):
        if len(values) == 0:
            return 0.0
        count = 0
        for v in values:
            if v >= low and v <= high:
                count = count + 1
        return round(count / len(values) * 100, 1)
    ```

    💡 Without the empty-list check, that test crashes with
    `ZeroDivisionError` — exactly the bug the smallest-input test
    exists to catch.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 17](https://BU-EK125.github.io/EK125/class/Class17.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 9: Write the Loader

    Write `load_cycles(filename)`: a dict of lists with keys
    `"cycle"` (int), `"voltage"` (float), `"capacity_mah"`
    (float) — skip any row with a blank value or a capacity of
    `-999`. No `break`, `continue`, or `while True`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    def load_cycles(filename):
        d = {"cycle": [], "voltage": [],
             "capacity_mah": []}
        with open(filename) as f:
            lines = f.readlines()
        for line in lines[1:]:
            p = line.strip().split(",")
            ok = "" not in p and p[2] != "-999"
            if ok:
                d["cycle"].append(int(p[0]))
                d["voltage"].append(float(p[1]))
                mah = float(p[2])
                d["capacity_mah"].append(mah)
        return d
    ```

    💡 Check the whole row *before* converting anything —
    `float("")` crashes, and converting one column at a time risks
    leaving the three lists out of alignment.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 14](https://BU-EK125.github.io/EK125/class/Class14.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 10: Write the Main Program

    Three functions, three files: `load_cycles`, `assess_metric`,
    `write_report`. Write a complete `main.py` that loads the
    data, assesses `"voltage"` (limit 3.60) and `"capacity_mah"`
    (limit 2500.0), collects both results, and writes the report
    once. No global variables.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    from loader import load_cycles
    from analyzer import assess_metric
    from reporter import write_report

    def main():
        """Load, assess, and report battery data."""
        data = load_cycles("cells.csv")
        limits = {"voltage": 3.60,
                  "capacity_mah": 2500.0}
        results = []
        for metric, limit in limits.items():
            results.append(
                assess_metric(data, metric, limit))
        write_report(results, "battery_report.txt")

    if __name__ == "__main__":
        main()
    ```

    💡 Keeping `data` and `results` *inside* `main()` is what
    makes "no globals" automatic — call `write_report` once,
    after the loop, not inside it.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 18](https://BU-EK125.github.io/EK125/class/Class18.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Nice Work

    A few cross-cutting habits that showed up again and again:

    - **Read the contract before the code** — it tells you what
      "correct" means, especially for debugging problems.
    - **Trace loops on paper**, one line at a time.
    - Know **position vs. label**: a list index is not the same
      thing as the value it points to.
    - **Boundary and tie cases** are where `<` vs `<=` bugs hide —
      and where a test needs to specifically target them.
    - **Follow the data**: the file that crashes isn't always the
      file with the bug.

    Good luck!
    """)
    return


if __name__ == "__main__":
    app.run()
