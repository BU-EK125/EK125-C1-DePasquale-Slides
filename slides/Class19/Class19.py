import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class19.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Debugging and Reflection

    ### Fitness Tracker Project — Part 5

    *Class 19*

    📖 [Full reading: Class 19](https://BU-EK125.github.io/EK125/class/Class19.html)
    📋 [Today's Team Activity](https://BU-EK125.github.io/EK125/gpps/Class19_TeamActivity.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## This Morning: The Bug Hunt
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    You'll get another team's Fitness Tracker code — same contract,
    different code. Five bugs are hiding inside: one syntax, two
    runtime, two logic. Debug it until your report matches theirs
    exactly.

    **Note:** today's material is not on Exam 2. Exam 2 (Friday
    11/13) covers Classes 9–18 — see the review near the end of this
    deck.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Same method every time: classify the bug, read the traceback
    bottom-up, and debug code you didn't write by starting from its
    contract.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The Debugging Method
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    | Step | In code |
    |---|---|
    | **Reproduce** | Run it and get the error (or wrong answer) every time |
    | **Locate** | Read the traceback bottom-up, or print at the seams |
    | **Hypothesize** | "I think `best_day` is a position, not a day number" |
    | **Change ONE thing** | Make one fix. Run again. |
    | **Confirm** | Did the error go away *and* is the answer right? |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    One change, one run, every time. Change five things at once and
    you won't know which one fixed it — or what else you broke.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Three Kinds of Bugs
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    | Kind | What you see | How you catch it |
    |---|---|---|
    | **Syntax** | Program doesn't start at all | Read the line shown, and the one before it |
    | **Runtime** | Program starts, then crashes with a traceback | Read bottom-up; match the error to its cause |
    | **Logic** | Program runs fine, answer is wrong | Tests, reasonableness checks, known-good answers |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **Syntax — the program never starts:**
    ```python
    for day in days
        print(day)
    ```
    ```python
    if steps = 10000:
        print("Goal met")
    ```
    Missing colon; and `=` where `==` belongs. Both stop Python
    before a single line runs — these are grammar mistakes, not bugs
    in your logic.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **Runtime — the program starts, then crashes:**
    ```python
    print("Steps: " + steps)
    ```
    ```python
    best = get_best_day(data)  # prints only
    print(best + 1)
    ```
    The first crashes on the spot: `str` plus `int`. The second
    crashes far from its real cause — `get_best_day` is the problem,
    not the `+ 1` line.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **Logic — no crash, just a wrong answer:**
    ```python
    total = 0
    for v in values:
        total = 0  # resets every pass!
        total = total + v
    ```
    ```python
    if resting_hr < goal:  # should be <=
        count += 1
    ```
    The first returns the last value, not a sum — `total = 0` belongs
    once, before the loop. The second silently drops any value that
    exactly equals the goal.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **A "logic" bug that crashes anyway:**
    ```python
    for i in range(len(days)):
        if values[i + 1] < values[i]:
            drops += 1
    ```
    The intent is a logic mistake — comparing the wrong pair of
    values. But on the last pass, `i + 1` runs off the end of the
    list: `IndexError`. Not every off-by-one stays silent.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **Scope — a variable that doesn't exist where you think:**
    ```python
    def analyze(data):
        total_steps = sum(data["steps"])
        return total_steps

    analyze(data)
    print(total_steps)  # NameError
    ```
    `total_steps` only exists inside `analyze`. Once the function
    returns, it's gone — use the return value, not the variable's
    name.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Syntax errors stop the program before it starts. Runtime errors
    stop it partway through. Logic errors don't stop it at all — so
    you have to go looking for them.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Reading a Multi-File Traceback
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Read every traceback from the **bottom up**: last line is what
    went wrong, the block above is where, the blocks above that are
    how you got there. The crash site and the bug site are often two
    different places.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **Same file, different line:**
    ```python
    values = line.strip().split(",")
    if values != "":          # always True
        steps = int(values[0])  # crashes here
    ```
    ```
    ValueError: invalid literal for int()
    ```
    The crash is on the `int(...)` line, but the real mistake is the
    `if` two lines above — comparing a list to a string is always
    `True`, so blank rows are never skipped.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **Crossing files — a contract mismatch:**
    ```
    Traceback (most recent call last):
      File "main.py", line 15, in main
        write_report(results, "report.txt")
      File "reporter.py", line 9, in write_report
        f"Goal met: {r['days_meeting_goal']}"
    KeyError: 'days_meeting_goal'
    ```
    ```python
    # Last line of analyze_metric in analyzer.py:
    return {"metric": metric, "met_goal": count}
    ```
    The crash is in `reporter.py`, but the dictionary was built in
    `analyzer.py` — it returns `met_goal`, not the contract's
    `days_meeting_goal`. Whoever owns `analyzer.py` fixes it.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    The error appears where a bad value is **used**. The bug is
    usually where that value was **created**. Follow it back across
    the seam, and let the contract decide who's off-contract.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Debugging Code You Didn't Write
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    1. **Read the contract** — what should it do?
    2. **Read `main.py`** — how is it called, what happens to the result?
    3. **Run it** — get the error or the wrong output
    4. **Follow the data** — print at the seams, find the first value that's wrong
    5. **Only now, read that function's code closely**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    The contract tells you what "right" means. Without it, you're
    just guessing what the author intended.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Writing Tests That Catch the Bug
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    A good test is aimed at a specific way the code could be wrong —
    not just any input.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **The tie-breaking case:**
    ```python
    tied = {
        "day": [1, 2, 3],
        "steps": [900, 950, 950],
    }
    check("earliest tie wins", 2, best_day(tied))
    ```
    Two days tie for the lead. If `>` quietly became `>=`, this test
    catches it — a list with no tie wouldn't.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **The boundary case:**
    ```python
    check("goal met exactly", 1,
          count_meeting_goal([8000], 8000))
    ```
    A value clearly above or below the goal passes whether the code
    uses `>` or `>=`. Only a value exactly *at* the goal tells them
    apart.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **The smallest possible input:**
    ```python
    check("empty list", 0, average_steps([]))
    ```
    A function that divides by `len(values)` crashes here with
    `ZeroDivisionError` unless it's handled — and an empty list is a
    completely legal input to hand it.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **The rounding case:**
    ```python
    check("rounds to one place", 66.7,
          round(200.15 / 3, 1))
    ```
    Pick a value where the *unrounded* result would fail an exact
    match — so the test is actually checking the rounding, not just
    getting lucky.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Four questions worth asking about any function: what about a
    tie? What about the exact boundary? What about empty input? What
    about rounding?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Fix It So It Stays Fixed
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    When you find a bug, ask: **"Why didn't my tests catch this?"**
    Then add a **regression test** — one that would have caught it —
    so if the bug ever comes back, the test fails immediately.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # Regression test: exact goal must count
    check("at goal", True, meets_goal(62, 62))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    You'll add exactly this kind of test to your own file this
    afternoon, naming the bug it guards against.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Wrapping Up Part 5
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Not actually required for submission** — no Gradescope
    deadline tomorrow. Still finish this work; you'll want it done:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - **Team:** Bug Log (all five bugs) and the fixed files; the
      team retrospective
    - **Individual:** your file with its new regression test; your
      ~300-word reflection, answering all five prompts with specific
      examples
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exam 2 Review: Classes 9–18
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Exam 2 (Friday 11/13) covers Classes 9 through 18 — not today's
    material. One worked reminder from each class, with a link back
    to the full reading.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Review: Class 9 — Moving to PyCharm
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    x = 10
    x + 5         # Colab: shows 15 below the cell
    print(x + 5)  # .py file: shows 15 either way
    ```
    In a `.py` file, nothing is displayed unless you explicitly
    `print()` it — a bare expression on its own line does nothing
    and causes no error, so a "working" program can still show zero
    output.

    📖 [Full reading: Class 9](https://BU-EK125.github.io/EK125/class/Class9.html)
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Review: Class 10 — Mastering Slicing
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums[::-1]     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    nums[9:4:-1]   # [9, 8, 7, 6, 5]
    ```
    A negative step walks backward; `[::-1]` is the standard idiom
    for reversing. With a negative step, `start` must be *greater
    than* `end` or you silently get nothing back — no error.

    📖 [Full reading: Class 10](https://BU-EK125.github.io/EK125/class/Class10.html)
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Review: Class 11 — NumPy Arrays
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    arr2d = np.array([[1, 3, 8], [-2, 5, 33]])
    arr2d[1, 2]    # 33
    arr2d[0, 1:]   # [3 8]
    ```
    `arr2d[row, col]` — the first index is always the row, the
    second always the column. A plain list repeats under `*`; an
    array multiplies element-wise.

    📖 [Full reading: Class 11](https://BU-EK125.github.io/EK125/class/Class11.html)
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Review: Class 12 — Dictionaries
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    print(bigone.get("size"))
    print(bigone.get("size", -999))
    ```
    ```
    None
    -999
    ```
    `get()` is safer than `bigone["size"]` whenever a key might be
    missing — it never raises a `KeyError`.

    📖 [Full reading: Class 12](https://BU-EK125.github.io/EK125/class/Class12.html)
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Review: Class 13 — User-Defined Functions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def printstrs(instr, n):
        for i in range(n):
            print(instr, end="")
        print()

    printstrs("Hi", 5)
    print(printstrs("a", 2))
    ```
    ```
    HiHiHiHiHi
    aa
    None
    ```
    A function with no `return` still hands back a value by
    default: `None`. A default parameter can be left out entirely.

    📖 [Full reading: Class 13](https://BU-EK125.github.io/EK125/class/Class13.html)
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Review: Class 14 — File I/O
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    with open("log.txt") as f:
        for line in f:
            values = line.split(",")
            print(repr(values[2]))
    ```
    ```python
    # Fixed:
            values = line.strip().split(",")
            print(repr(values[2]))
    ```
    Splitting a raw line keeps the trailing newline stuck to its
    last field — easy to miss until something downstream compares
    strings and silently fails.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def sqrarea(sidelen):
        sqar = sidelen**2
        return sqar

    area = sqrarea(4)
    print(sqar)
    ```
    ```
    NameError: name 'sqar' is not defined
    ```
    Every function gets its own scope. Once a function finishes, its
    local variables are gone — only the returned value survives.

    📖 [Full reading: Class 14](https://BU-EK125.github.io/EK125/class/Class14.html)
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Review: Class 15 — Project Kickoff
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Where "contract" comes from: parameters, returns, and side
    effects, agreed on and written down before any code — the
    vocabulary every later class builds on.

    📖 [Full reading: Class 15](https://BU-EK125.github.io/EK125/class/Class15.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Review: Class 16 — Stub Building
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def read_temperatures(filename):
        """Read temperatures (deg F) from a file.

        Returns: list of float.
            Example: [71.2, 70.8, 72.5, 71.9]
        """
        return [71.2, 70.8, 72.5, 71.9]
    ```
    A faithful stub: same header and docstring, returns (never
    prints) the contract's own example values, with the correct
    types — even before the real logic exists.

    📖 [Full reading: Class 16](https://BU-EK125.github.io/EK125/class/Class16.html)
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Review: Class 17 — Writing Real Functions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    temps = [71.2, 74.5, 73.8, 76.1]
    days  = [1, 2, 4, 5]   # day 3 had no reading

    best_index = 0
    for i in range(len(temps)):
        if temps[i] > temps[best_index]:
            best_index = i

    print(best_index)        # 3 -- a position
    print(days[best_index])  # 5 -- the actual day
    ```
    `best_index` is a position in the list — the moment any rows get
    skipped, position and day number drift apart.

    📖 [Full reading: Class 17](https://BU-EK125.github.io/EK125/class/Class17.html)
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Review: Class 18 — Integrating It All Together
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Swap in one real function at a time, rerunning after each
    change. A traceback's crash site and its bug's actual source are
    often in two different files.

    📖 [Full reading: Class 18](https://BU-EK125.github.io/EK125/class/Class18.html)
    """)
    return


if __name__ == "__main__":
    app.run()
