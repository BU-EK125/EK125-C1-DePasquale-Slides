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
    ## Trick 1: Skipping a Bad Value
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    What does a blank line, or a missing-data code like `-999`,
    actually look like once you've read it? How do you decide whether
    to use a line or skip it?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def read_temperatures(filename):
        """Read temperatures in F from a file. Skips blank
        lines and -999."""
        # 1. Make an empty list for the temperatures
        temps = []
        # 2. Open the file for reading
        with open(filename, "r") as file:
            # 3. For each line in the file:
            for line in file:
                # a. strip the newline
                reading = line.strip()
                # b. if not blank and not "-999", convert
                #    it and add it
                if reading != "" and reading != "-999":
                    temps.append(float(reading))
        # 4. Return the list
        return temps
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    The same idea scales up: your Loader checks a whole **row** of
    several columns at once, not just one value. What check would let
    you test several values together, instead of one at a time?
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
    - **Loader:** a blank value becomes an empty string after
      splitting — can you check the *whole row* at once, instead of
      one value at a time?
    - **Analyst:** tracking "best so far" gives you a **list
      position** — after skipping rows, does that position still
      match the day number?
    - **Analyst:** what changes in your comparisons when
      `higher_is_better` is `False`? (Hint: more than one line.)
    - **Report Writer:** check your contract's example value closely —
      does it want `8327.8`, or something formatted differently?
    - **Everyone:** `0.1 + 0.2 != 0.3`. If your test compares floats
      with `==`, where should the rounding happen?
    """)
    return


if __name__ == "__main__":
    app.run()
