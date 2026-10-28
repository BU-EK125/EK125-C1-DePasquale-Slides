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
    def summarize_temperatures(temps):
        """Calculate the average, high, and low of a list
        of temperatures.

        Returns: dict with keys "average", "high", "low"
            (floats, degrees F).
            Example: {"average": 71.6, "high": 72.5,
                      "low": 70.8}
        """
        # STUB: return the example value from the contract
        summary = {"average": 71.6, "high": 72.5,
                   "low": 70.8}
        return summary
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    A stub never does the real work — it just promises the right
    type, structure, and keys so every other function can be built
    and tested against it today.
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
