import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class16.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Stub Building

    ### Fitness Tracker Project — Part 2: The Running Skeleton

    *Class 16*

    📖 [Full reading: Class 16](https://BU-EK125.github.io/EK125/class/Class16.html)
    📋 [Today's Team Activity](https://BU-EK125.github.io/EK125/gpps/Class16_TeamActivity.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## A Faithful Stub, with Its Docstring
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    This is the reading's own weather-station example, not your
    Fitness Tracker code — so it shows the pattern without handing
    you your own Part 2 answer. The same five rules apply to your
    Loader, Analyst, and Report Writer: copy the header and docstring
    exactly, return the contract's example value, use easy parameters
    directly, always `return` (never `print`), and touch every key a
    teammate's data will need.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def read_temperatures(filename):
        """Read temperatures in degrees F from a file.

        Returns: list of float, one per valid reading.
            Example: [71.2, 70.8, 72.5, 71.9]
        """
        # PLAN:
        # 1. Make an empty list for the temperatures
        # 2. Open the file for reading
        # 3. For each line in the file:
        #      a. strip the newline
        #      b. if the line is not blank and not "-999",
        #         convert it to float and add it to the list
        # 4. Return the list

        # STUB: return the example value from the contract
        return [71.2, 70.8, 72.5, 71.9]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    This afternoon, add this kind of pseudocode *above* your own
    stub's `return` — one comment per step, written in plain English,
    covering the messy cases your contract describes. **Leave the
    stub body in place.** The program must still run.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Checking the Seams
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    A program that runs isn't automatically correct. Print every
    value as it crosses from one function to the next, and compare it
    to the contract.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    data = load_tracker_data("fitness_data.csv")
    print("SEAM 1 type:", type(data))
    print("SEAM 1 keys:", list(data.keys()))
    print("SEAM 1 lengths:", len(data["day"]),
          len(data["steps"]))

    results = analyze_metric(data, "steps", 8000)
    print("SEAM 2 type:", type(results))
    print("SEAM 2 keys:", list(results.keys()))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Three questions answer most seam problems: Is it the right
    **type**? Does it have the right **keys**? Are the lists the
    right **length**? These prints are temporary — put them in
    `check_seams.py` (a copy of `main.py`), so the real `main.py`
    stays clean.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The Four Errors You'll Most Likely See Today
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    | Error | Usually means | Where to look |
    |---|---|---|
    | `ModuleNotFoundError: No module named 'loader'` | Can't find the **file** | Same folder? Spelled exactly right? |
    | `ImportError: cannot import name 'load_data'` | File found, **function name** doesn't match | Compare the `import` line to the `def` line |
    | `TypeError: 'NoneType' object is not subscriptable` | A function **printed instead of returning** | Does that function have a `return`? |
    | `KeyError: 'average'` | The two sides of a seam **disagree on a key name** | Compare the key in the error to the contract |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Three of these four are **seam errors** — each piece is fine on
    its own, but two pieces don't agree. When an error appears, ask
    "which seam?" before you ask "which line?"
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Due Sunday: The Running Skeleton
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Gradescope: **"Fitness Tracker Part 2: Running Skeleton"** — group
    submission, by **Sunday 11/1, 11:59 PM**. Submit more than once;
    Gradescope keeps your history.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - `loader.py`, `analyzer.py`, `reporter.py`, `main.py` — each a
      faithful stub
    - `check_seams.py`, with your final seam-check output pasted in a
      comment at the bottom
    - An updated Team Contract (PDF) — **only** if it changed today

    *Before you submit:* `main.py` runs start to finish with no
    errors, the report file is created, and `check_seams.py` checks
    both seams with every check matching the contract.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## How Should `main.py` Look?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Three import lines — file name without `.py`, then the exact
    function name — a `main()` function running your team's plan from
    Section 3 of your contract, and the `if __name__ ==
    "__main__":` guard calling `main()`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    from loader import load_tracker_data
    from analyzer import analyze_metric
    from reporter import write_report


    def main():
        data = load_tracker_data("fitness_data.csv")

        # Your team's plan from Section 3 -- at least 3
        # metrics, resting_hr required
        plan = [("steps", 8000, True),
                ("resting_hr", 62, False)]

        results_list = []
        for metric, goal, higher_is_better in plan:
            results = analyze_metric(data, metric, goal,
                                      higher_is_better)
            results_list.append(results)

        write_report(results_list, "fitness_report.txt")


    if __name__ == "__main__":
        main()
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    The `plan` list here is illustrative — use your own team's
    metrics and goals from Part C, not these exact numbers.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Quiz 8 and Exam 2: What's Fair Game
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    No new Python syntax was covered this week, but the new skills
    from Classes 15–16 are fair game. Possible things we might ask
    you to do:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - Given a contract docstring, write a correct call and store the
      result
    - Given a contract, write the expression to access one value from
      the returned dictionary
    - Identify which key or type mismatch causes an error, or a
      silent wrong answer
    - Given a few rows of CSV text, write the dictionary of lists a
      loader would return
    - Identify what is missing from a vague contract
    - Given a contract, write the call that stores the result
      (Class 15)
    - Given a contract, write a faithful stub (Class 16)
    - Pick the faithful stub from four options, or explain why one is
      unfaithful
    - Match an error message (`ModuleNotFoundError`, `ImportError`,
      `NoneType ... not subscriptable`, `KeyError`) to its most likely
      cause
    - Write the import line for a function in a named file
    - Predict the output of a short `main()` that uses a stub
    """)
    return


if __name__ == "__main__":
    app.run()
