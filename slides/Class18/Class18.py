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
    ## One Bulb at a Time
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Replace all ten burned-out holiday bulbs at once, plug in, and the
    string is still dark — which one is the problem? Replace **one**,
    plug in, check. Replace the next, plug in, check. The moment it
    goes dark, you know exactly which bulb caused it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Add one real function at a time, and run after every change. When
    something breaks, it was the last thing you added.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The Integration Plan
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Data flows Loader → Analyst → Report Writer, so integrate in that
    order:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    | Step | Real functions | Stubs |
    |---|---|---|
    | 0 | none | all three |
    | 1 | Loader | Analyst, Report Writer |
    | 2 | Loader, Analyst | Report Writer |
    | 3 | all three | none |

    After **every** step: run `main.py`, run `check_seams.py`, and
    compare the output to what you expect.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Start small:** point `main.py` at `test_days1to5.csv` first, not
    the full data file. You already hand-calculated the correct
    answer for Days 1–5 in Class 15, so you know exactly what each
    step should produce. Only switch to `fitness_data.csv` once Days
    1–5 works perfectly.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## This Morning: Four Steps
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - **Step 0:** confirm the Class 16 skeleton still runs on Days 1–5
    - **Step 1:** swap in the real Loader — check Seam 1's keys and
      lengths (5 each) against your Class 15 hand calculation
    - **Step 2:** swap in the real Analyst — check that `best_day` is
      an actual **day number**, not a position
    - **Step 3:** swap in the real Report Writer — compare the report
      line by line to your contract's example
    - **Step 4:** switch to the full data file and check every value
      against the data facts
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    The report itself won't change until the Analyst is real — that's
    expected. At Steps 0–1 you're checking the **seam**, not the
    report.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Reading a Traceback That Crosses Files
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    With three files calling each other, a traceback can look
    intimidating. Read it **from the bottom up**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```
    Traceback (most recent call last):
      File "main.py", line 30, in <module>
        main()
      File "main.py", line 25, in main
        write_report(results_list, "report.txt")
      File "reporter.py", line 31, in write_report
        f"(met on {r['days_meeting_goal']} of "
    KeyError: 'days_meeting_goal'
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    1. **Last line — what went wrong:** `KeyError:
       'days_meeting_goal'`. A dictionary doesn't have that key.
    2. **The block just above — where it happened:** `reporter.py`,
       inside `write_report`.
    3. **The blocks above that — how we got there:** `main.py` called
       `main()`, which called `write_report(...)`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    The crash happened in the **Report Writer's** file, but the
    dictionary missing that key was **made by the Analyst**. The
    contract decides who's off-contract: check the Analyst's
    *Returns* section for the exact key name it promises.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    The error appears where a bad value is **used**. The bug is often
    where that value was **created**. Follow the value back across
    the seam, and let the contract decide who's wrong.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## "It Runs" Is Not the Same as "It's Right"
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    A program can run with no errors and still give a wrong answer —
    nobody in Boston has ever recorded a resting heart rate of −999.
    A program can't tell you its own answer is ridiculous. **You**
    have to check.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    | Check | Question to ask |
    |---|---|
    | **Counts** | Is the number of items what it should be? |
    | **Lengths** | Do lists that should match have the same length? |
    | **Ranges** | Are values physically possible? |
    | **Consistency** | Do related numbers agree with each other? |
    | **Cross-check** | Does one result agree with the raw data? |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    The cross-check is the most powerful one: if the report says the
    best step day is Day 25, open the CSV and look at Day 25. If its
    step count isn't the maximum, something is wrong — even though
    the program ran perfectly.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Code or Contract?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    When two pieces disagree, ask in this order:

    1. **What does the contract say?** The side that doesn't match it
       gets fixed — by its own owner.
    2. **Is the contract unclear or silent?** The team decides, the
       Recorder dates it in the Decision Log, *then* the code changes.
    3. **Is the contract wrong?** Same process as #2.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Never quietly work around a teammate's bug in your own file. A
    workaround hides the problem, and the next person to use that
    function hits it again.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The Integration Log
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    The **Recorder** fills this in after every step — it turns "we
    fixed some stuff" into evidence of exactly what your team found
    and how. You'll use it in Class 19's reflection.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    | Step | Real functions | Matches expected? | What broke | Cause | Fix (who) |
    |---|---|---|---|---|---|
    | 1 | Loader | Yes | — | — | — |
    | 2 | Loader + Analyst | No | `best_day` was 4 for steps | Returned position, not day number | Analyst: use `days[best_index]` |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## This Afternoon: Integration Clinic
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Another team's program runs **with no errors**. Your job: decide
    whether it's actually right.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    1. Run it, open the report, and compare every value to the data
       facts below
    2. **Find the seam:** add seam prints (type, keys, **lengths**)
       after `load_tracker_data`
    3. **Find the bug:** which function is off-contract? Check the
       contract in its docstring
    4. **Explain it**, then fix it and confirm every value matches
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    | Data fact (`fitness_data.csv`) | Correct value |
    |---|---|
    | Days analyzed | **25** |
    | Steps: average | **8843.4** |
    | Steps: minimum / maximum | **4569 / 14773** |
    | Steps: best day | **Day 27** |
    | Resting HR: average | **63.0** |
    | Resting HR: best day | **Day 14** |
    | Sleep hours: best day | **Day 7** |
    | Active minutes: average | **41.4** |

    If your team analyzes different metrics or rounds differently,
    check the ones you have — small differences in the last digit are
    fine.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Some values can happen to look right even when the program is
    wrong. "A few numbers match" is not evidence the program is
    right — check every value against the data facts.
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
    - Finish any step that isn't complete — every row of your log
      should say "Yes" under *Matches expected?*
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
    - `loader.py`, `analyzer.py`, `reporter.py`, `main.py` — pointed
      at `fitness_data.csv`
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
