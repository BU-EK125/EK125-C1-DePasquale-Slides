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
    ## This Afternoon: From Plan to Precision
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    This morning you made decisions. This afternoon you prove they
    work — by actually working the numbers by hand, the way your
    functions will have to.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Part E:** work out real answers together, as a class. **Part
    F:** stress-test another team's contract. **Part G:** fix what
    the stress test finds and finish the contract.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Keep everything you compute today. In Class 17, these same
    hand-calculated answers become the **test cases** that tell you
    whether your real code is correct.
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
    Before diving into the details, here's the target: a complete,
    filled-in contract for the Data Loader. Notice there's no real
    code inside it — just a precise description someone else could
    build against without ever seeing the real implementation.
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
    ### Takeaway

    Every placeholder in your own contract template should end up
    looking this precise by the end of today — especially the
    "Example:" line, which you'll work out by hand this afternoon.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part E: What Does Python Actually See?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Before computing anything, trace exactly what each line of the
    CSV becomes in Python. Day 1's raw line ends with a newline
    character; `.strip()` removes it, then `.split(",")` breaks it
    into a list of **strings**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    line = "1,8478,61,8.1,50\\n"
    values = line.strip().split(",")
    print(values)
    ```

    ```
    ['1', '8478', '61', '8.1', '50']
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Every item is a **string** — `'1'`, not `1`. The loader has to
    convert each column to the right type (`int` for `day`, `float`
    for everything else) before it goes in the dictionary.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Now the Blank Row
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Day 9 is missing three readings. The same
    `.strip().split(",")` trace shows how a blank reading shows up in
    Python — not as `None`, but as an **empty string**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    line = "9,,,5.6,\\n"
    values = line.strip().split(",")
    print(values)
    ```

    ```
    ['9', '', '', '5.6', '']
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    This is exactly how the Loader detects a blank reading: check
    whether `""` shows up anywhere in `values` before converting the
    row.
    """)
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
    `load_tracker_data` reads one row at a time, skips any row that's
    missing a value (today's reference decision — "skip the whole
    row"), and appends each column to its own list.
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
    ### Takeaway

    All five lists have the same length (5) and line up position by
    position — position 0 is Day 1 in every list. That alignment is
    the whole point.
    """)
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
    If a Loader skips only the **blank value** instead of the whole
    row, the lists stop lining up — and nothing tells you.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # A small example: Day 2's steps reading was blank
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
    Position 1 should be Day 2 in every list — but `steps[1]` is
    actually **Day 3's** reading. Skip the whole row instead, and
    every list stays the same length and lines up.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Decide this once, write it in the contract, and make sure the
    Loader and the Analyst agree. A length mismatch like this gives a
    wrong answer with **no error**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Computing `analyze_metric`: Steps
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Think it through in words first: start with the first day as the
    best so far; for each day, if it's better, it becomes the new
    best; count the days that meet the goal.
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
    Day 5's 12192 steps is the maximum, so `best_day` is 5. Three of
    the five days (1, 2, and 5) meet the 8000-step goal.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Computing `analyze_metric`: Resting Heart Rate
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Same function, but `higher_is_better=False` — a **lower** resting
    heart rate is the better one. "Best" always depends on this flag;
    never assume bigger is better.
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
    ### Takeaway

    Day 4's 59 bpm is the minimum, so it's the **best** day here — the
    opposite of the steps example. Only Days 1 and 4 meet the
    62-bpm-or-lower goal.
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
    `best_day` must be the actual **day number** from the `day`
    column — not its position in the list. After skipping rows, those
    two numbers drift apart.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # Day 3 was skipped -- position 2 in the list is Day 4,
    # not Day 3
    day   = [1, 2, 4, 5]
    steps = [8478.0, 9430.0, 4569.0, 12192.0]

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
    ### Takeaway

    Say explicitly in your contract: `best_day` is a day **number**,
    read from the `day` list at the winning position — never just the
    winning position itself.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Writing the Report
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `write_report` turns the Analyst's dictionaries into formatted
    text. Rounding and formatting are decisions too — your team
    already decided who rounds, and to how many places.
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
    ## Part F: The Contract Stress Test
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Swap Team Contracts with a neighboring team. Using **only their
    contract** — no talking — try to write code against it. Every
    question you'd have to ask is a gap in their contract.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    Remember the reading's weather-station example: Person B's
    function returned a key named `"avg"`; Person C's code expected
    `"average"`. Both were "right" — they just never agreed.

    ```
    KeyError: 'average'
    ```

    This is exactly the kind of gap a stress test catches before it
    becomes a bug.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## What to Flag in a Stress Test
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - A vague Returns line ("returns the data") instead of a type,
      structure, and example value
    - `best_day` described ambiguously as an index instead of a day
      number
    - Two owners using different key names for the same thing
    - Blank-value handling that's never stated — or stated
      differently by the Loader and the Analyst
    - A function that both prints **and** returns (Class 13's rule:
      pick one)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    A perfect contract gets **zero** questions in the stress test.
    Every question you receive shows a guess your own teammates might
    have made differently too.
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
    - Fix every gap the stress test turned up, and log each change in
      the Decision Log
    - Fill in your team's working agreement (communication plan,
      meeting times, file ownership)
    - Go through the submission checklist at the end of the Team
      Contract template
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
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
    logic exists — and get the whole three-function pipeline running
    end to end.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    A good contract today means a good stub tomorrow, and a good test
    case in Class 17. Precision now saves debugging later.
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
      another's — most team bugs live here, not inside any one
      function
    - **Function contract:** name, inputs, output (type, exact
      structure, and an example value), side effects, and
      assumptions — written as a docstring
    - **Dictionary of lists:** every column-list must stay the same
      length and stay lined up by position
    - **Stress test:** the fastest way to find a contract's gaps
      before they become bugs
    - **Decision Log:** a dated, written record — so no decision
      lives only in someone's memory

    📖 [Full reading: Class 15](https://BU-EK125.github.io/EK125/class/Class15.html)
    📋 [Today's Team Activity](https://BU-EK125.github.io/EK125/gpps/Class15_TeamActivity.html)
    """)
    return


if __name__ == "__main__":
    app.run()
