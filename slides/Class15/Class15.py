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
    ## What a Finished Contract Looks Like
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Here's the target: a complete, filled-in contract for the Data
    Loader. No real code inside it — just a precise description a
    teammate could build against without ever seeing the real
    implementation.
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
    ## Part E: Tracing a CSV Row by Hand
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `.strip().split(",")` on a clean line gives a list of **strings**;
    the same trace on a row with blanks gives empty strings — exactly
    what the Loader checks for before converting types.
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
    ''')
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
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Building the Dictionary of Lists
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Skip any row missing a value (today's reference decision), and
    every list below ends up the same length — Day 1 is position 0 in
    all five.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # Using only Days 1-5 of the file
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
    ## Computing `analyze_metric`: Two Ways "Best" Can Mean
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    "Best" depends entirely on `higher_is_better` — watch it flip
    between these two calls on the same Days 1–5 data.
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
    **minimum** (59) wins instead — lower is better there.
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
    ## Writing the Report
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
