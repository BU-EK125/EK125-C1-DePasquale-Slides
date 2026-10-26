import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class15.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Collaborating with Others: Problem Definition and Initial Decisions

    ### Kicking Off the Fitness Tracker Analyzer — Project Part 1

    *Class 15*

    📖 [Full reading: Class 15](https://BU-EK125.github.io/EK125/class/Class15.html)
    📋 [Today's Team Activity](https://BU-EK125.github.io/EK125/gpps/Class15_TeamActivity.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Before You Continue

    If you haven't finished this morning (Parts A–D), stop and finish
    those first — everything below builds directly on it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## This Afternoon: Prove the Plan Works
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Part E:** work out real numbers together, as a class. **Part
    F:** stress-test another team's contract. **Part G:** fix what
    the stress test finds and submit. Keep everything you compute —
    it becomes your **test cases** in Class 17.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part E: Work Out the Expected Answers by Hand
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **About 20 minutes, together.** We'll work through this as a
    class, step by step, using only Days 1–5 of `fitness_data.csv`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Warm-Up: What Does Python Actually See?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **W1.** Line 2 of the file, as Python reads it, is the text
    `1,8478,61,8.1,50` followed by a newline character. After
    `.strip().split(",")`, what list do you get? Are the items
    numbers or strings?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    line = "1,8478,61,8.1,50\\n"
    print(line.strip().split(","))
    ```

    ```
    ['1', '8478', '61', '8.1', '50']
    ```

    All **strings** — not numbers.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **W2.** What does the line for Day 9 become after
    `.strip().split(",")`?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    line = "9,,,5.6,\\n"   # Day 9 is missing 3 readings
    print(line.strip().split(","))
    ```

    ```
    ['9', '', '', '5.6', '']
    ```

    Blanks become **empty strings**.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## From One Line to a Dictionary of Lists
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    This is the "dictionary of lists" pattern from today's reading:
    one list per column, where position *i* in every list is the same
    row. For each row: split it like you just did, convert each value
    to your team's chosen type (int for `day`, float for the rest),
    and **append it to that column's list**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # After Day 1:  day = [1],      steps = [8478.0], ...
    # After Day 2:  day = [1, 2],   steps = [8478.0, 9430.0], ...
    ```

    Keep going through Day 5, one row at a time, for every column —
    that builds the dictionary `load_tracker_data` returns.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Data Loader: The Dictionary for Days 1–5
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Write the exact dictionary `load_tracker_data` would return for a
    file containing only Days 1–5. Skip any row missing a value
    (today's reference decision — though none of Days 1–5 are blank).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    load_tracker_data("fitness_data.csv")
    ```

    ```
    {'day': [1, 2, 3, 4, 5],
     'steps': [8478.0, 9430.0, 6970.0, 4569.0, 12192.0],
     'resting_hr': [61.0, 67.0, 67.0, 59.0, 66.0],
     'sleep_hours': [8.1, 7.8, 6.4, 7.7, 7.6],
     'active_minutes': [50.0, 34.0, 52.0, 21.0, 38.0]}
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Now Write It as a Contract
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    You just computed that dictionary. Here's what it looks like
    written up as the Loader's contract — the key names and types
    come straight from the CSV's own columns, and the "Example" line
    is exactly what you just worked out.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def load_tracker_data(filename):
        """Read a fitness tracker CSV file and return its
        data as a dictionary.

        Parameters:
            filename (str): name of the CSV file, e.g.
                "fitness_data.csv"

        Returns:
            A dictionary with one key per column: "day",
            "steps", "resting_hr", "sleep_hours",
            "active_minutes". Each value is a list, one entry
            per day with no blank readings. "day" is a list of
            ints; the rest are lists of floats.

            Example (first 5 days):
            {"day": [1, 2, 3, 4, 5],
             "steps": [8478.0, 9430.0, 6970.0, 4569.0, 12192.0],
             "resting_hr": [61.0, 67.0, 67.0, 59.0, 66.0],
             "sleep_hours": [8.1, 7.8, 6.4, 7.7, 7.6],
             "active_minutes": [50.0, 34.0, 52.0, 21.0, 38.0]}

        Side effects: none. Does not print.

        Assumptions and messy cases: if any value in a row
            is blank, the whole row is skipped.
        """
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Gotcha: Skip the Row, or Skip the Value?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Skip only the **blank value** instead of the whole row, and the
    lists stop lining up — with no error to warn you.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # Day 2's steps reading was blank
    day   = [1, 2, 3, 4]         # every day kept
    steps = [7000, 9000, 8000]   # Day 2 skipped, but only here

    print(day[1], steps[1])
    ```

    ```
    2 9000
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `steps[1]` should be Day 2 but is actually **Day 3's** reading.
    Decide this once, write it in the contract, and make sure the
    Loader and Analyst agree.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Data Analyst: `steps`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Using that dictionary, write the exact dictionary
    `analyze_metric` would return for `steps` with your goal (8000).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    analyze_metric(data, "steps", 8000)
    ```

    ```
    {'metric': 'steps', 'num_days': 5, 'average': 8327.8,
     'minimum': 4569.0, 'maximum': 12192.0, 'best_day': 5,
     'goal': 8000, 'days_meeting_goal': 3}
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Data Analyst: `resting_hr` (Lower Is Better)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Now do the same for `resting_hr` with your goal (62) —
    remember: **lower** is better here.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    analyze_metric(data, "resting_hr", 62,
                   higher_is_better=False)
    ```

    ```
    {'metric': 'resting_hr', 'num_days': 5, 'average': 64.0,
     'minimum': 59.0, 'maximum': 67.0, 'best_day': 4,
     'goal': 62, 'days_meeting_goal': 2}
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Steps: Day 5's maximum (12192) wins. Resting HR: Day 4's
    **minimum** (59) wins instead — the same function, flipped by
    `higher_is_better`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Gotcha: Index vs. Day Number
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `best_day` must be the day **number** from the `day` column, not
    its position in the list — after skipping rows, those two numbers
    drift apart.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # Day 3 was skipped -- position 2 in the list is Day 4,
    # not Day 3
    day = [1, 2, 4, 5]
    print(day[2])
    ```

    ```
    4
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Report Writer: The Exact Report Text
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Write the exact report text `write_report` would produce from
    those two results.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```
    Metric: steps
      Average: 8327.8
      Range:   4569.0 to 12192.0
      Best day: Day 5
      Goal: 8000  (met on 3 of 5 days)

    Metric: resting_hr
      Average: 64.0
      Range:   59.0 to 67.0
      Best day: Day 4
      Goal: 62  (met on 2 of 5 days)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Put these into your contract as the **Example** values. Keep this
    work — in Class 17, these hand-calculated answers become your
    **test cases**: how you'll know your real function is correct.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part F: Contract Stress Test (10 min)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Swap** your Team Contract with a neighboring team.

    **Without talking to them**, using only what's written, answer on
    paper:

    1. The line of code that loads their data file.
    2. The line of code that analyzes `steps` with their goal.
    3. The line of code that prints the **average** from that result.
    4. The exact value their `load_tracker_data` would return for
       just Days 1–2.
    5. Every question you wanted to ask, because their contract
       didn't say.

    **Return the sheet.** Fix your own contract for every question
    you got back, and log each fix in the Decision Log.

    *Common gaps to watch for:* a vague Returns line, `best_day` as
    an index instead of a day number, mismatched key names, and
    unstated blank-value handling.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part G: Finish and Submit
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - Answer the four problem-definition questions: what goes in,
      what comes out, what counts as success, what's messy
    - Fix every gap the stress test turned up, and log each change
    - Fill in your working agreement and go through the submission
      checklist

    The Recorder submits the Team Contract as a **group PDF** to
    Gradescope ("Fitness Tracker Part 1: Team Contract") by
    **Tuesday 10/27, 11:59 PM**.

    📋 [Today's Team Activity](https://BU-EK125.github.io/EK125/gpps/Class15_TeamActivity.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Looking Ahead: Class 16
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Next class, you'll turn today's contracts into **stubs** — each
    function returns its contract's example value before any real
    logic exists — and get the whole pipeline running end to end. A
    good contract today means a good stub tomorrow, and a good test
    case in Class 17.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Summary
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - **Seams:** the places one person's code hands data to
      another's — most team bugs live here
    - **Function contract:** name, inputs, output (type, structure,
      and an example value), side effects, and assumptions
    - **Dictionary of lists:** every column-list must stay the same
      length and stay lined up by position
    - **Stress test:** the fastest way to find a contract's gaps
      before they become bugs

    📖 [Full reading: Class 15](https://BU-EK125.github.io/EK125/class/Class15.html)
    📋 [Today's Team Activity](https://BU-EK125.github.io/EK125/gpps/Class15_TeamActivity.html)
    """)
    return


if __name__ == "__main__":
    app.run()
