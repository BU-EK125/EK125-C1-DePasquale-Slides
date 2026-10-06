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
    you need `word[2:4]`. A slice's length is always `end - start`.
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
    you get nothing back — no error, just a silent empty result. Going
    backward means starting from a *bigger* index.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Common Slicing Patterns

    A handful of patterns cover most real uses — worth having
    memorized rather than re-deriving every time:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - **First `n` items:** `sequence[:n]`
    - **Last `n` items:** `sequence[-n:]`
    - **Drop the first item:** `sequence[1:]`
    - **Drop the last item:** `sequence[:-1]`
    - **Drop first *and* last:** `sequence[1:-1]`
    - **Every other item:** `sequence[::2]`
    - **Reversed:** `sequence[::-1]`
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

    🚩 **Common mistakes** with slice assignment:
    - The right-hand side must be an **iterable**, even for one value —
      `numbers[1:3] = 5` raises a `TypeError`; use `numbers[1:3] = [5]`.
    - Assigning into a **zero-width slice** (like `data[3:3] = [...]`)
      *inserts* new elements instead of replacing anything — there's
      nothing between index 3 and itself to remove.
    - With a **stepped** slice, the number of replacement values must
      exactly match the number being replaced, or Python raises a
      `ValueError`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Gotcha: `nums[-1]` vs. `nums[:-1]`

    These look nearly identical but do very different things.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    numbers = [10, 20, 30, 40, 50]
    print(numbers[-1])    # just the last element
    print(numbers[:-1])   # everything EXCEPT the last element
    ```

    ```
    50
    [10, 20, 30, 40]
    ```
    ''')
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
    - `nums[-1]` (one value) and `nums[:-1]` (everything but the last)
      are easy to mix up — they're not the same thing.

    📝 [Today's GPP](https://BU-EK125.github.io/EK125/gpps/Class10_GPP.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## HW5 Section 2: Slicing Practice

    Section 2 of this week's homework (Problems 3–7) is all slicing —
    same tools as today's reading, applied to five new datasets. Let's
    think through each one's *logic*, not the final code.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 3: Slice Warm-Up

    ```python
    stress_readings = [12.4, 15.1, 18.7, 14.3, 22.6,
                        19.8, 16.2, 21.0, 13.5, 17.9]
    ```

    Six asks, each a single slice expression — no loops needed:
    (a) first 3 · (b) last 4 · (c) positions 3–6 inclusive ·
    (d) all except first and last · (e) reversed · (f) every other,
    starting from the first.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **The Slice Recipe:** for every part, write out *which indices you
    want* in plain English first, then translate:

    - "First `n`" → `[:n]`. "Last `n`" → `[-n:]`.
    - "`a` through `b` **inclusive**" → `[a:b+1]` — the `+1` is the
      whole trick, since slicing's own end is exclusive.
    - "All except first and last" → `[1:-1]`.
    - "Reversed" → `[::-1]`. "Every other, from the first" → `[::2]`.

    Match each of the six asks above to one of these patterns before
    you type anything.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 4: Negative Indices and Steps

    ```python
    aqi_data = [42, 45, 48, 51, 55, 60,
                72, 85, 93, 88, 80, 75,
                68, 64, 70, 78, 85, 90,
                88, 80, 70, 60, 52, 47]
    ```

    Five asks:
    - (a) final 6 hours
    - (b) 5th-to-last through 2nd-to-last, inclusive — **negative
      indices only**
    - (c) every 3rd reading
    - (d) hours 7–18, reversed, as a *single* slice
    - (e) predict, then check: `aqi_data[-1]` vs. `aqi_data[-1:]`
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - (a) and (b) are both the Slice Recipe from Problem 3 — just with
      negative numbers. Write the indices out first: what are the
      5th-to-last and 2nd-to-last positions, as negative numbers?
    - (d) needs a **negative step**, which means `start` must come
      *after* `end` in the list, not before — the opposite order you'd
      use going forward.
    - (e) is conceptual, not computational: one of these gives back a
      single value, the other gives back a **list containing** that
      value. Indexing and slicing never return the same type, even
      when they grab "the same" element.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 5: Slice Assignment

    ```python
    force_data = [0.0, 0.0, 0.0, 45.2, 67.8, 89.1,
                  112.4, 98.3, 76.5, 0.0, 0.0]
    ```

    The first 3 and last 2 readings are instrument artifacts, not real
    data. Clean the dataset: extract the valid middle, compute its
    average, then overwrite the bad readings with that average.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Steps:**

    1. Slice out just the valid middle (indices 3 through 8) into its
       own variable.
    2. Compute the average of *that* variable — not the original list
       — using `sum()` and `len()`, rounded.
    3. Build two small replacement lists using `[value] * n`: one of
       length 3, one of length 2.
    4. Use slice assignment to drop each replacement list into the
       first 3 and last 2 positions of the *original* list.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    🚩 **Order matters here.** You must compute the average from the
    valid data *before* you overwrite anything — the extracted
    variable from step 1 protects that data, but only if you actually
    read from it before step 4 changes the original list.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 6: Building Sequences from Slices

    ```python
    line_A = [101, 102, 103, 104, 105]
    line_B = [201, 202, 203, 204, 205]
    ```

    Three unrelated parts, each its own slicing trick:
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - **Part A — Rotate `line_A` left by 2:** split it into two
      pieces with two slices, then glue them back together in the
      opposite order with `+`. Which piece comes first after the swap?
    - **Part B — Interleave `line_A` and `line_B`:** start from a
      placeholder list of 10 zeros (`[0] * 10`), then use **two**
      stepped slice assignments — one starting at index 0, one at
      index 1 — to drop each list into every other position.
    - **Part C — Parts after a defective ID:** use `.index()` to find
      *where* the defective ID lives — don't hard-code the position —
      then slice from one past that point to the end.
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
    **Steps:**

    1. Work out *how many* 5-day windows fit in the data —
       `len(daily_temps) - window_size + 1`. Why the `+ 1`?
    2. Write that as a `range()`, where each number is the **starting
       index** of one window.
    3. Inside the loop, slice out that one window: `window_size`
       values starting at the current index.
    4. Compute that window's average, round it, and collect it into a
       results list.
    5. After the loop, print each result with a label showing which
       days it covers.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    This is the exact same "extract a window, process it, collect the
    result" shape as the reading's own windowing example — just with
    an average instead of a min/max. Write the pseudocode for step 1
    through 4 in plain English *before* writing any Python; the loop
    itself is short once the formula for "how many windows" is right.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Now It's Your Turn

    Same patterns, your own data — work through Problems 3–7 in
    PyCharm, run each part as you write it, and check your output
    against the expected results in the assignment.

    📝 [Today's GPP](https://BU-EK125.github.io/EK125/gpps/Class10_GPP.html)
    """)
    return


if __name__ == "__main__":
    app.run()
