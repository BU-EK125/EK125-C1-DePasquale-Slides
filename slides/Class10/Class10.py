import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class10.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Mastering Slicing

    ### Extracting, Reversing, and Replacing Parts of a Sequence

    *Class 10*

    📖 [Full reading: Class 10](https://BU-EK125.github.io/EK125/class/Class10.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Quick Review: Indexing

    One index gets you **one element** — positive counts from the
    front, negative counts from the back. Slicing, today's topic, gets
    you a **window** of elements instead.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    word = "Python"
    print(word[0])      # 'P'
    print(word[-1])     # 'n'
    ```

    ```
    P
    n
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Basic Slice Notation

    `sequence[start:end]` grabs a window: it **includes** `start` and
    **stops right before** `end`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    word = "Programming"
    print(word[0:4])   # "Prog"
    print(word[3:7])   # "gram"
    ```

    ```
    Prog
    gram
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    🚩 **Common mistake:** forgetting the end index is *exclusive* —
    `word[2:3]` grabs only one character. To include index 3 as well,
    you need `word[2:4]`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Omitting Start and End

    Leave either side blank to mean "all the way to that edge."
    `sequence[:]` — both sides blank — copies the whole thing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    word = "Python"
    print(word[:3])    # "Pyt"  -- start of the string through index 2
    print(word[3:])    # "hon"  -- index 3 through the end
    ```

    ```
    Pyt
    hon
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Negative Indices in Slices

    Negative indices work inside slices too — they still count
    backward from the end, one position at a time.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    word = "Programming"
    print(word[-4:])    # "ming"      -- last 4 characters
    print(word[:-3])    # "Programm"  -- everything except the last 3
    ```

    ```
    ming
    Programm
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The Step Parameter

    A third number, `sequence[start:end:step]`, sets how many
    positions to move each time — not just one.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(numbers[::2])     # every other element, starting at 0
    print(numbers[1::2])    # every other element, starting at 1
    ```

    ```
    [0, 2, 4, 6, 8]
    [1, 3, 5, 7, 9]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Negative Steps: Reversing

    A negative step walks **backward**. `[::-1]` is the standard
    Python idiom for reversing any sequence.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(numbers[::-1])     # the whole thing, reversed
    print(numbers[9:4:-1])   # indices 9 down to 5
    ```

    ```
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    [9, 8, 7, 6, 5]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    With a negative step, `start` must be **greater than** `end` or
    you get nothing back — no error, just a silent empty result.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Slice Assignment (Lists Only)

    Lists let you assign directly into a slice to replace a whole
    section at once. Strings can't — they're immutable.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    numbers = [1, 2, 3, 4, 5]
    numbers[1:4] = [20, 30, 40]
    print(numbers)
    ```

    ```
    [1, 20, 30, 40, 5]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    🚩 **Common mistake:** the right-hand side must be an **iterable**,
    even for one value — `numbers[1:3] = 5` raises a `TypeError`; use
    `numbers[1:3] = [5]`.
    """)
    return



@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Summary

    - `sequence[start:end]` includes `start`, excludes `end`.
    - Leaving either side blank means "to that edge"; `[:]` copies the
      whole sequence.
    - A third number, `step`, controls direction and spacing —
      negative steps walk backward, and `[::-1]` reverses.
    - Only **lists** support slice assignment — replacing, inserting,
      or deleting a whole section at once.

    📝 [Today's GPP](https://BU-EK125.github.io/EK125/gpps/Class10_GPP.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## HW5 Section 2: Slicing Practice

    Section 2 of this week's homework (Problems 3–7) is all slicing.
    Let's walk through one of them — Problem 7 — since it's the one
    with the most going on logically.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 7: Moving Window Analysis

    ```python
    daily_temps = [8.2, 9.1, 11.4, 10.3, 13.6,
                   15.2, 14.8, 16.1, 17.3, 15.9,
                   14.2, 12.8, 11.1, 9.7, 10.5]
    window_size = 5
    ```

    Compute a **moving average**: the average of every 5 consecutive
    days, sliding forward one day at a time.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Setting up the full logic:**

    - **How many windows fit:** `len(daily_temps) - window_size + 1` —
      this is both the answer *and* how many times the loop needs to
      run.
    - **The loop itself:** `for start in range(num_windows):` — each
      pass slices out one window, `daily_temps[start : start +
      window_size]`, computes its average, and appends it to a
      results list.
    - **After the loop:** print each result with a label showing
      which days it covers.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    This "slice a window, compute something, collect it" loop works
    for any moving-window problem — only the per-window computation
    changes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Now It's Your Turn

    We only walked through Problem 7 — Problems 3–6 use the exact
    same slicing tools from today's lecture. Work through all five in
    PyCharm, run each part as you write it, and check your output
    against the expected results in the assignment.

    📝 [Today's GPP](https://BU-EK125.github.io/EK125/gpps/Class10_GPP.html)
    """)
    return


if __name__ == "__main__":
    app.run()
