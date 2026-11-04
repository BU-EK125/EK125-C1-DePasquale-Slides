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
    ## Quiz 9 Review
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Quiz 9 covers Classes 17–18. Each card below is a generic
    stand-in for one skill it tests.
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
    check("hr", 0.9, round(0.6 + 0.3, 1))  # PASS
    check("hr", 0.9, 0.6 + 0.3)            # FAIL
    check("laps", 6, "6")                  # FAIL
    ```
    The second FAILs on float rounding error, not a real bug. The
    third FAILs because `6` and `"6"` are different types.
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

    Hand-calculate the true answer from the input. If it disagrees
    with `actual`, the function's wrong. If your own `expected` was
    wrong, fix the test instead.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **Reading a multi-file traceback:**
    ```
    Traceback (most recent call last):
      File "main.py", line 18, in main
        write_report(results, "report.txt")
      File "reporter.py", line 12, in write_report
        f"Best day: {results['best_day']}"
    KeyError: 'best_day'
    ```
    ```python
    # Last line of summarize_week:
    return {"best": days[i], "goal_count": n}
    ```
    The crash is in `reporter.py`, but the Analyst's own return line
    never produces the key `'best_day'` — it returns `'best'`
    instead. The Report Writer is reading the contract correctly;
    the Analyst is off-contract.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Choosing the integration order:**

    Swap in the Loader, then the Analyst, then the Report Writer —
    one at a time, rerunning on a small known-answer file after each
    swap. If it broke right after you added the Analyst, check the
    Analyst first: it's the only thing that changed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Counting complete days:**

    A file has 20 rows; 3 contain at least one blank value, and the
    contract skips any row with a blank entirely. Expected "days
    analyzed": 20 − 3 = **17**. If the report says 18 instead,
    something is under-skipping — check whether the Loader's blank
    check looks at every column or just one.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Cross-checking a reported "best day":**

    The report says the best step count was 14,200 on Day 9. The
    raw CSV shows Day 9 logged 11,400 — but Day 11 logged 14,200.
    The *value* is right, attached to the *wrong* day — a classic
    sign that skipping a blank row dropped one list's entry but not
    the other's, shifting everything after it by one.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Code or contract?**

    1. Contract promises key `avg_steps`; the Analyst's code returns
       `average`. → The Analyst's own bug, fixed in their own file.
    2. Report Writer wants to print percent-of-goal, but the
       contract never promised that value. → A gap — the team
       decides and logs it before any code changes.
    3. Two days tie for best resting heart rate; the contract is
       silent on which wins. → Also a gap — the team decides, not
       whoever noticed it first.
    """)
    return


if __name__ == "__main__":
    app.run()
