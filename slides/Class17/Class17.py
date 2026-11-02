import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class17.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Writing Real Functions

    ### Fitness Tracker Project — Part 3

    *Class 17*

    📖 [Full reading: Class 17](https://BU-EK125.github.io/EK125/class/Class17.html)
    📋 [Today's Team Activity](https://BU-EK125.github.io/EK125/gpps/Class17_TeamActivity.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Last Week: The Frame. Today: The Interior.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Last week your team built the house's **frame** — every stub in
    place, the whole skeleton standing and running, even though
    nothing inside was real yet.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Today you do the **interior work** — wiring, plumbing, finishes —
    inside walls that don't move. Your contract is the frame; your
    real code is everything behind the walls.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    If your real function keeps every promise your stub kept, the
    rest of the house doesn't even notice the walls went up for real.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part D: The Two Trickiest Functions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **20 minutes, together.** Follow along in your own file only if
    it's your function — everyone else takes notes. You'll need to
    read and understand this logic in Classes 18–19, and on Exam 2.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Trick 1: Checking a Whole Row at Once
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    After `.strip().split(",")`, what does a row with a missing value
    turn into? How could you check the *whole row* for a blank, in
    one line, instead of checking each value separately?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    line = "7,,42"
    values = line.strip().split(",")
    print(values)
    ```

    ```
    ['7', '', '42']
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    print("" in values)
    ```

    ```
    True
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Why this is the trick, not just a shortcut:** your Loader
    doesn't know in advance *which* column will be missing on a bad
    row — it could be steps one day, resting heart rate the next.
    Checking value by value means writing a separate check for every
    column, and keeping all of them in sync as the contract changes.
    `"" in values` asks one question — "is anything in this row
    blank?" — and it's correct no matter which column, or how many
    columns, the file has.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `in` checks the whole list in one line — the same membership test
    from Class 3, now applied to a list instead of a single string.
    No `continue` needed: an `if` just decides whether the row counts.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Trick 2: Tracking the Best So Far
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    How do you find the best value in a list in one pass, without
    sorting the whole thing first?
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
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `best_index` is a **position** in the list — the moment any rows
    get skipped, position and day number drift apart. Your contract
    needs the real identifier, not just the position.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## What Flips for "Lower Is Better"?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    If a **lower** number is the one you want, what has to change in
    the loop above — and what doesn't?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    best_index = 0
    for i in range(len(temps)):
        if temps[i] < temps[best_index]:
            best_index = i
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Only the comparison operator flips. The loop, the starting point,
    and converting a position into an identifier all stay exactly the
    same.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Report Writer: Formatting Numbers
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    f-strings control exactly how a number prints. Use whatever
    format your contract's example value actually shows.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    value = 8327.8
    print(f"{value:.1f}")
    print(f"{8000:,}")
    ```

    ```
    8327.8
    8,000
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part E: Finish, Test, and Explain
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - Finish your real function until **every test passes**
    - Add **one more test** — the one most likely to catch a bug in
      your function
    - **Explain it to a teammate:** line by line, under 3 minutes
      each. They ask at least one "why" question. (TAs will too.)
    - Upload your final file to Drive and run `main.py` one more time
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Explaining your code out loud is often the fastest way to notice
    what's actually wrong with it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Clues for Building the Real Thing
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Each card below is a small, self-contained example of one place
    real teams get tripped up today — grouped by which function it
    hits. None of these are your project's actual code; each one is a
    generic stand-in so you can see the pattern and apply it to your
    own function.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **Loader — the last line of a file can be blank too:**
    ```python
    line = ""            # a blank line
    values = line.strip().split(",")
    print(values)        # ['']
    print("" in values)  # True
    ```
    An empty trailing line still becomes a row with one blank value —
    it gets skipped the same way, no special-case code needed.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **Analyst — position vs. identifier:**
    ```python
    best_index = 2                 # a position
    day_number = days[best_index]  # what you need
    ```
    `best_index` only tells you *where* in the list the best value
    sits. If your contract's `best_day` key means an actual day
    number, you must look that day up with `days[best_index]` — the
    index itself is almost never the answer your report needs.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **Analyst — tracking the best *and* the goal count, together:**
    ```python
    best = values[0]
    count = 0
    for value in values:
        if higher_is_better:
            if value > best:   # earlier tie wins
                best = value
            if value >= goal:  # a tie counts
                count += 1
        else:
            if value < best:
                best = value
            if value <= goal:
                count += 1
    ```
    Both comparisons flip together when `higher_is_better` is
    `False`. Using `>`/`<` instead of `>=`/`<=` for the goal count
    would silently miss a value that lands exactly on the goal.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **Report Writer — format what the contract promises:**
    ```python
    print(f"{8327.8:.1f}")   # 8327.8
    print(f"{8000:,}")       # 8,000
    ```
    `:.1f` rounds to one decimal place; `:,` adds thousands commas.
    Your contract's example output already shows the exact format
    expected — match it, rather than printing Python's raw default.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **Report Writer — every write needs its own line break:**
    ```python
    file.write("Average: 8327.8")
    file.write("Range: 4569.0 to 12192.0")
    ```
    Without an explicit trailing newline character at the end of each
    write, those two lines land on the same line in the file.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    **Everyone — floats don't compare exactly:**
    ```python
    print(0.1 + 0.2)
    print(0.1 + 0.2 == 0.3)
    print(round(0.1 + 0.2, 1) == 0.3)
    ```

    ```
    0.30000000000000004
    False
    True
    ```
    Computers store decimals with tiny rounding error, so a calculated
    total can be *off by a hair* from the number you expect. If your
    test checks an average or a sum with `==`, a correct function can
    still "fail" — round both sides to the same number of decimals
    before comparing.
    ''')
    return


if __name__ == "__main__":
    app.run()
