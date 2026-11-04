import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class18.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Integrating It All Together

    ### Fitness Tracker Project — Part 4

    *Class 18*

    📖 [Full reading: Class 18](https://BU-EK125.github.io/EK125/class/Class18.html)
    📋 [Today's Team Activity](https://BU-EK125.github.io/EK125/gpps/Class18_TeamActivity.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Finish Your Own Integration
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - Finish any step that isn't complete — every row of your
      integration log should say "Yes" under *Matches expected?*
    - Run each teammate's tests again. Did your contract change
      today? Update your tests to match.
    - Add a reasonableness check to `check_seams.py`: confirm all
      five lists have the same length, and that the length is 25
    - Upload everything to Drive
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    A program that runs with no errors isn't done — every value in
    your report should match what you'd get by hand-checking the
    raw data.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Due Sunday: The Working Program
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Gradescope: **"Fitness Tracker Part 4: Working Program"** — group
    submission, by **Sunday 11/8, 11:59 PM**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - `loader.py`
    - `analyzer.py`
    - `reporter.py`
    - `main.py` — pointed at `fitness_data.csv`
    - `check_seams.py`, including today's reasonableness check
    - `fitness_report.txt` — the report from the full data
    - Integration log (steps 0–4) and an updated Team Contract with
      the Decision Log (PDF)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Quiz 9 Review: Four Things to Practice
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Quiz 9 covers Classes 17–18. These four cards are generic
    stand-ins for the exact skills it tests — work through each one
    before Friday.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **Tracing a best-value loop — ties:**
    ```python
    vals = [71.2, 74.5, 74.5, 73.0]
    best = 0
    for i in range(len(vals)):
        if vals[i] > vals[best]:
            best = i
    print(best)  # 1 -- the earlier tie wins
    ```
    Swap `>` for `>=` and `best` becomes `2` instead — the *later*
    tie wins. One symbol change, opposite tie-breaking behavior.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **Predicting `check()` — PASS or FAIL:**
    ```python
    check("avg", 0.3, round(0.1 + 0.2, 1))  # PASS
    check("avg", 0.3, 0.1 + 0.2)            # FAIL
    check("count", 4, "4")                  # FAIL
    ```
    The second FAILs on float rounding error, not a real bug. The
    third FAILs because `4` and `"4"` are different types. FAIL means
    "these two values disagree" — not automatically "the function is
    wrong."
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **Writing a boundary-value test:**
    ```python
    check("at goal", True, meets_goal(8000, 8000))
    ```
    A value clearly above or below the goal passes whether the
    function uses `>` or `>=`. Only a value exactly *at* the goal
    tells them apart. Never paste a function's own output in as
    `expected` — a buggy function's bug would just pass itself.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **A FAIL: function or test?**

    Hand-calculate the true answer yourself, from the input. If it
    disagrees with `actual`, the function has a bug. If your own
    `expected` value was the one that was wrong, fix the test —
    don't touch working code because of a bad test.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Quiz 9: What's Fair Game
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    No new syntax this week, but the integration skills from today
    are. Possible things we might ask you to do:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - Everything on the four review cards above
    - Read a multi-file traceback: name the file and function where
      it crashed, then say whose code is off-contract
    - Given a scenario, choose the correct integration order
    - Compute the expected number of complete days from a description
      of a file
    - Spot a wrong "best day" from a small table of raw data, using a
      cross-check
    - Code or contract? Given a short scenario, choose the right
      process
    """)
    return


if __name__ == "__main__":
    app.run()
