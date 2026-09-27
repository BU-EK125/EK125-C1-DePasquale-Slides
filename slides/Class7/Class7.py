import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class7.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Advanced Iteration and Nested Structures

    ### Range, Enumerate, Comprehensions, Indexing & Slicing

    *Class 7*

    📖 [Full reading: Class 7](https://BU-EK125.github.io/EK125/class/Class7.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## `range()`: More Than Just `range(n)`

    You've used `range(n)` to count from 0. Two more forms give you real
    control over where iteration starts, stops, and steps.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - `range(start, stop)` — begins at `start` instead of 0
    - `range(start, stop, step)` — also sets the increment between values
    - `stop` is always **exclusive**, same as before
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    print(list(range(3, 7)))        # start, stop
    print(list(range(3, 10, 2)))    # start, stop, step
    ```

    ```
    [3, 4, 5, 6]
    [3, 5, 7, 9]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Counting Backwards Needs a Negative Step

    What happens if you try to count *down* without telling `range()`
    to step backwards?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    print(list(range(10, 2)))      # no step -- silently empty!
    print(list(range(10, 2, -2)))  # explicit negative step
    ```

    ```
    []
    [10, 8, 6, 4]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    🚩 **Common mistake:** forgetting the negative step when counting
    backwards. `range()`'s default step is `+1`, so a start greater than
    the stop with no explicit step never raises an error — it just
    silently produces an **empty** sequence. Counting down always needs
    an explicit negative third argument.

    You'll use all three `range()` arguments together in today's GPP —
    see [Problem 1.1: Counting Backwards](https://BU-EK125.github.io/EK125/gpps/Class7_GPP.html#problem-1-1-counting-backwards).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 🎯 Quick Check: Predict Before You Code

    **GPP Problem 1.1: Counting Backwards**

    > Use `range()` to print the numbers from 10 down to 1 (inclusive),
    > each on a new line.

    **Expected output:**
    ```
    10
    9
    8
    ...
    2
    1
    ```

    Which `range()` call produces this?

    **A.** `range(10, 1)`

    **B.** `range(10, 0, -1)`

    **C.** `range(1, 11)`

    **D.** `range(10, -1)`

    📝 **Submit your answer below:**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.iframe(
        """
        <style>
          body { margin:0; padding:12px; background:#1a1a1a; font-family:-apple-system,sans-serif; }
          .qc-row { display:flex; gap:12px; }
          .qc-btn { flex:1; padding:14px; font-size:1.1em; font-family:monospace;
                    border-radius:8px; border:1px solid #555; background:#2a2a2a;
                    color:#eee; cursor:pointer; }
          .qc-status { margin-top:10px; font-size:0.95em; color:#9c9; min-height:1.2em; }
        </style>
        <div class="qc-row">
          <button class="qc-btn" data-choice="A">A</button>
          <button class="qc-btn" data-choice="B">B</button>
          <button class="qc-btn" data-choice="C">C</button>
          <button class="qc-btn" data-choice="D">D</button>
        </div>
        <div class="qc-status"></div>
        <script>
        (function () {
          var buttons = document.querySelectorAll('.qc-btn');
          var status = document.querySelector('.qc-status');
          var submitted = false;
          buttons.forEach(function (btn) {
            btn.addEventListener('click', function () {
              if (submitted) return;
              submitted = true;
              var choice = btn.getAttribute('data-choice');
              buttons.forEach(function (b) { b.disabled = true; b.style.opacity = '0.5'; });
              btn.style.opacity = '1';
              btn.style.background = '#2d6a4f';
              fetch('https://docs.google.com/forms/d/e/1FAIpQLSdHU67IBnwYojEj6Z_YCwHnZdh7-vK4RxDPVcPCzfFGfSOyow/formResponse', {
                method: 'POST',
                mode: 'no-cors',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: 'entry.1109327713=' + encodeURIComponent(choice),
              });
              status.textContent = 'Submitted: ' + choice;
            });
          });
        })();
        </script>
        """,
        width="100%",
        height="140px",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer: B

    `range(10, 0, -1)` — starting at 10, stepping by -1, stopping
    *before* 0 gives exactly `10, 9, ..., 1`. **A** and **D** both keep
    the default `+1` step with a start greater than the stop, so both
    are silently empty. **C** counts in the wrong direction entirely.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The `enumerate()` Function

    `range()` is great when a loop just needs a count. But what if you
    need both the **index** and the **value** from a sequence at the
    same time? `enumerate()` gives you both, in one loop.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    numlist = [4, 52, 33, 11, -3]
    for i, item in enumerate(numlist):
        print('Item', i, 'is', item)
    ```

    ```
    Item 0 is 4
    Item 1 is 52
    Item 2 is 33
    Item 3 is 11
    Item 4 is -3
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    🚩 **Common mistake:** forgetting to unpack *both* values.
    `for item in enumerate(numlist):` (a single loop variable) gives you
    a `(index, value)` **tuple** in `item`, not the value by itself.
    Always pair `enumerate()` with two loop variables, e.g.
    `for i, item in enumerate(numlist):`.

    You'll practice this exact pattern in today's GPP — see
    [Problem 1.2: Sensor Readings with Indices](https://BU-EK125.github.io/EK125/gpps/Class7_GPP.html#problem-1-2-sensor-readings-with-indices).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## List Comprehensions

    **Vectorizing code** means replacing a loop with a compact
    expression. A list comprehension builds a whole list in one line:
    `[expression for i in iterable]`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # Loop version:
    cubelist = []
    for i in range(5):
        cubelist.append(i**3)

    # Comprehension version -- same result:
    cubelist = [i**3 for i in range(5)]
    print(cubelist)
    ```

    ```
    [0, 1, 8, 27, 64]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Comprehensions don't add any power to the language — they're a
    convenient, succinct way to write the same loop.

    🚩 **Common mistake:** using a comprehension just for its *side
    effects*, e.g. `[print(x) for x in mylist]`. This builds and
    immediately throws away a list of `None`s (since `print()` returns
    `None`) just to make the printing happen. If all you want is to
    repeat an action, use a plain `for` loop instead — save
    comprehensions for building a list you're actually going to use.

    Today's GPP has you build comprehensions like this from scratch —
    see [Problem 2.1: Squares](https://BU-EK125.github.io/EK125/gpps/Class7_GPP.html#problem-2-1-squares)
    and [Problem 2.2: Temperature Conversion](https://BU-EK125.github.io/EK125/gpps/Class7_GPP.html#problem-2-2-temperature-conversion).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Adding Conditionals

    An `if` at the end of a comprehension filters which expressions
    make it into the list: `[expression for i in iterable if condition]`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # Loop version:
    cubelisteven = []
    for i in range(7):
        if i % 2 == 0:
            cubelisteven.append(i**3)

    # Comprehension version -- same result:
    cubelisteven = [i**3 for i in range(7) if i % 2 == 0]
    print(cubelisteven)
    ```

    ```
    [0, 8, 64, 216]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    The `if` filters *which* values of `i` get an expression built for
    them — it doesn't wrap the expression itself. This was your first
    glimpse of vectorization: instead of looping step by step, you build
    the whole list in one expression.

    You'll write one of these yourself in today's GPP — see
    [Problem 2.3: Filtering Even Numbers](https://BU-EK125.github.io/EK125/gpps/Class7_GPP.html#problem-2-3-filtering-even-numbers).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 🎯 Quick Check: Predict Before You Code

    **GPP Problem 2.3: Filtering Even Numbers**

    > Use a conditional list comprehension to create a new list
    > containing only the even numbers from the given list.

    ```python
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ```

    **Expected result:** `[2, 4, 6, 8, 10]`

    Which comprehension produces it?

    **A.** `[x for x in numbers if x % 2 == 0]`

    **B.** `[x % 2 == 0 for x in numbers]`

    **C.** `[x for x in numbers if x % 2 == 1]`

    **D.** `[x for x in range(len(numbers)) if x % 2 == 0]`

    📝 **Submit your answer below:**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.iframe(
        """
        <style>
          body { margin:0; padding:12px; background:#1a1a1a; font-family:-apple-system,sans-serif; }
          .qc-row { display:flex; gap:12px; }
          .qc-btn { flex:1; padding:14px; font-size:1.1em; font-family:monospace;
                    border-radius:8px; border:1px solid #555; background:#2a2a2a;
                    color:#eee; cursor:pointer; }
          .qc-status { margin-top:10px; font-size:0.95em; color:#9c9; min-height:1.2em; }
        </style>
        <div class="qc-row">
          <button class="qc-btn" data-choice="A">A</button>
          <button class="qc-btn" data-choice="B">B</button>
          <button class="qc-btn" data-choice="C">C</button>
          <button class="qc-btn" data-choice="D">D</button>
        </div>
        <div class="qc-status"></div>
        <script>
        (function () {
          var buttons = document.querySelectorAll('.qc-btn');
          var status = document.querySelector('.qc-status');
          var submitted = false;
          buttons.forEach(function (btn) {
            btn.addEventListener('click', function () {
              if (submitted) return;
              submitted = true;
              var choice = btn.getAttribute('data-choice');
              buttons.forEach(function (b) { b.disabled = true; b.style.opacity = '0.5'; });
              btn.style.opacity = '1';
              btn.style.background = '#2d6a4f';
              fetch('https://docs.google.com/forms/d/e/1FAIpQLSdHU67IBnwYojEj6Z_YCwHnZdh7-vK4RxDPVcPCzfFGfSOyow/formResponse', {
                method: 'POST',
                mode: 'no-cors',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: 'entry.1464395584=' + encodeURIComponent(choice),
              });
              status.textContent = 'Submitted: ' + choice;
            });
          });
        })();
        </script>
        """,
        width="100%",
        height="140px",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer: A

    `[x for x in numbers if x % 2 == 0]`. **B** builds a list of
    `True`/`False` values instead of filtering anything. **C** inverts
    the condition and keeps the odds. **D** filters even *indices*
    (positions 0, 2, 4, ...) rather than even *values* — a very easy mix-up.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Nested Structures: Building 2D Data

    So far, comprehensions have built flat lists. Nesting one
    comprehension inside another builds a **table or grid** — the
    inner comprehension builds one row, the outer comprehension repeats
    it. This mirrors the nested `for` loops from Class 6, one loop for
    rows and one for columns.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    grid = [[col for col in range(3)] for row in range(2)]
    print(grid)

    # Same result, built with a nested loop instead:
    nested = []
    for row in range(2):
        inner = []
        for col in range(3):
            inner.append(col)
        nested.append(inner)
    print(nested)
    ```

    ```
    [[0, 1, 2], [0, 1, 2]]
    [[0, 1, 2], [0, 1, 2]]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Example: Product Table

    Nested comprehensions **construct** the very structures that nested
    loops would otherwise only print (or build via repeated `.append()`
    calls).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    products = [[r * c for c in range(1, 5)] for r in range(1, 4)]
    for row in products:
        print(row)
    ```

    ```
    [1, 2, 3, 4]
    [2, 4, 6, 8]
    [3, 6, 9, 12]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Read a nested comprehension **outer-to-inner**: `for r in range(1, 4)`
    picks each row, and `for c in range(1, 5)` builds that row's
    columns — same order as writing the equivalent nested loop.

    You'll build a table just like this one in today's GPP — see
    [Problem 3.2: Building a Multiplication Table](https://BU-EK125.github.io/EK125/gpps/Class7_GPP.html#problem-3-2-building-a-multiplication-table).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Working with Nested Lists

    A nested list — like seats in a theater — is just a list containing
    other lists.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    seats = [['A1', 'A2'], ['B1', 'B2']]
    for row in seats:
        for seat in row:
            print(seat)
    ```

    ```
    A1
    A2
    B1
    B2
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Nesting `enumerate()` gives you **both** the row and column position
    at once:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            print(f"Row {i}, Col {j}: {seat}")
    ```

    ```
    Row 0, Col 0: A1
    Row 0, Col 1: A2
    Row 1, Col 0: B1
    Row 1, Col 1: B2
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Combine `enumerate()` with a comprehension to **tag** values with
    their positions in one step:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    indexed = [(i, j, seat)
               for i, row in enumerate(seats)
               for j, seat in enumerate(row)]
    print(indexed)
    ```

    ```
    [(0, 0, 'A1'), (0, 1, 'A2'), (1, 0, 'B1'), (1, 1, 'B2')]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Every seat is now structured data — tagged with its row index,
    column index, and value — built in one expression instead of a
    multi-line loop with manual bookkeeping.

    You'll work with a nested list just like this one in today's GPP —
    see [Problem 3.1: Understanding Nested Lists](https://BU-EK125.github.io/EK125/gpps/Class7_GPP.html#problem-3-1-understanding-nested-lists).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Multi-Level Indexing

    Once a nested structure exists, you don't need to loop over
    everything to get one value out of it — you can index straight to
    it. Think of each bracket as **peeling away a layer**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    grid = [[10, 20], [30, 40], [50, 60]]

    print(grid[0])      # First row
    print(grid[2])      # Third row
    print(grid[2][0])   # Third row, first element
    ```

    ```
    [10, 20]
    [50, 60]
    50
    ```

    `grid` → the entire structure. `grid[2]` → one row, `[50, 60]`.
    `grid[2][0]` → one number, `50`.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    🚩 **Common mistake:** writing `grid[2, 0]` (a comma inside one
    bracket) instead of `grid[2][0]` (two separate bracket pairs).
    Python lists don't support comma-indexing like that — it raises a
    `TypeError`. Each level of nesting needs its own `[...]`.

    You'll build a grid like this — with tuples inside instead of
    numbers — in today's GPP — see
    [Problem 3.3: Grid of Coordinates](https://BU-EK125.github.io/EK125/gpps/Class7_GPP.html#problem-3-3-grid-of-coordinates).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Lists (unlike tuples) are mutable, so you can modify one entry deep
    inside a nested structure:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    print(grid[1][1])   # Second row, second column

    grid[0][1] = 99
    print(grid)
    ```

    ```
    40
    [[10, 99], [30, 40], [50, 60]]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Slicing: Windows of Data

    Indexing gives you one element. **Slicing** gives you a whole
    window of elements in one step — your next taste of vectorization.
    The slice **includes** the start index and **stops right before**
    the end index.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    nums = [5, 10, 15, 20, 25]
    print(nums[1:4])   # Indices 1 through 3
    print(nums[:3])    # Start through index 2
    print(nums[2:])    # Index 2 through the end
    print(nums[-1])    # Last element
    print(nums[:-1])   # Everything but the last element
    ```

    ```
    [10, 15, 20]
    [5, 10, 15]
    [15, 20, 25]
    25
    [5, 10, 15, 20]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Loops vs. Slicing

    A loop extracts a subset **step by step**. Slicing describes the
    same block of data in one expression.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # Loop version:
    subset = []
    for i in range(1, 4):
        subset.append(nums[i])
    print(subset)

    # Slicing -- same result:
    print(nums[1:4])

    # Negative indices aren't limited to -1:
    print(nums[-1])   # Last
    print(nums[-2])   # Second to last
    ```

    ```
    [10, 15, 20]
    [10, 15, 20]
    25
    20
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    This week's slicing stays to **flat** lists only — slicing whole
    rows or columns out of a nested grid comes later. Prefer negative
    indices like `nums[-1]` over hardcoding `nums[len(nums) - 1]`; they
    stay correct even if the list's length changes.

    You'll practice extracting slices like these in today's GPP — see
    [Problem 4.1: Extracting Data Ranges](https://BU-EK125.github.io/EK125/gpps/Class7_GPP.html#problem-4-1-extracting-data-ranges).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 🎯 Quick Check: Predict Before You Code

    **GPP Problem 4.2: Reverse a List**

    > Use slicing to reverse this list without using the `.reverse()`
    > method or `reversed()` function.

    ```python
    values = [10, 20, 30, 40, 50]
    ```

    **Expected result:** `[50, 40, 30, 20, 10]`

    Which slice does it?

    **A.** `values[::-1]`

    **B.** `values[::1]`

    **C.** `values[-1:]`

    **D.** `values[0:-1]`

    📝 **Submit your answer below:**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.iframe(
        """
        <style>
          body { margin:0; padding:12px; background:#1a1a1a; font-family:-apple-system,sans-serif; }
          .qc-row { display:flex; gap:12px; }
          .qc-btn { flex:1; padding:14px; font-size:1.1em; font-family:monospace;
                    border-radius:8px; border:1px solid #555; background:#2a2a2a;
                    color:#eee; cursor:pointer; }
          .qc-status { margin-top:10px; font-size:0.95em; color:#9c9; min-height:1.2em; }
        </style>
        <div class="qc-row">
          <button class="qc-btn" data-choice="A">A</button>
          <button class="qc-btn" data-choice="B">B</button>
          <button class="qc-btn" data-choice="C">C</button>
          <button class="qc-btn" data-choice="D">D</button>
        </div>
        <div class="qc-status"></div>
        <script>
        (function () {
          var buttons = document.querySelectorAll('.qc-btn');
          var status = document.querySelector('.qc-status');
          var submitted = false;
          buttons.forEach(function (btn) {
            btn.addEventListener('click', function () {
              if (submitted) return;
              submitted = true;
              var choice = btn.getAttribute('data-choice');
              buttons.forEach(function (b) { b.disabled = true; b.style.opacity = '0.5'; });
              btn.style.opacity = '1';
              btn.style.background = '#2d6a4f';
              fetch('https://docs.google.com/forms/d/e/1FAIpQLSdHU67IBnwYojEj6Z_YCwHnZdh7-vK4RxDPVcPCzfFGfSOyow/formResponse', {
                method: 'POST',
                mode: 'no-cors',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: 'entry.305172968=' + encodeURIComponent(choice),
              });
              status.textContent = 'Submitted: ' + choice;
            });
          });
        })();
        </script>
        """,
        width="100%",
        height="140px",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer: A

    `values[::-1]` — an empty start and stop with step `-1` walks the
    whole list backwards. **B** is an unchanged copy (step `+1`). **C**
    keeps only the last element. **D** drops the last element but
    doesn't reverse anything.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Summary

    - **`range()`** and **`enumerate()`** give you more control over
      iteration — start/stop/step, and index-plus-value together.
    - **List comprehensions** build lists compactly in one line;
      adding `if` filters which values make it in.
    - **Nested comprehensions and loops** build 2D data — the inner
      comprehension builds a row, the outer repeats it.
    - **Multi-level indexing** (`grid[row][col]`) reaches exactly the
      element you need from a nested structure.
    - **Slicing** extracts a whole window of a flat list at once — your
      next step into vectorization, after comprehensions.

    📝 [Today's GPP](https://BU-EK125.github.io/EK125/gpps/Class7_GPP.html)
    """)
    return


if __name__ == "__main__":
    app.run()
