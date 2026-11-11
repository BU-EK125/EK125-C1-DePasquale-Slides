import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class20.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Exam 2 Practice

    ### Additional Review

    A few skills the practice exams don't fully drill on their own.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Additional Review
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    A few skills the practice exams don't fully drill on their own.
    Same idea as before: work the example yourself, then check it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## What's Covered
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - **Default parameters** — positional vs. keyword calls, and
      what happens when you skip one
    - **Functions with no return** — a function always hands back
      something, even if it's `None`
    - **Scope: local vs. global** — a name assigned inside a
      function never touches the outer one
    - **Mutable vs. immutable arguments** — a list change inside a
      function is visible outside; a reassignment isn't
    - **Dictionary gotchas** — `in` checks keys; `.get()` never
      raises `KeyError`
    - **Dict of lists / list of dicts** — know which `len()` you're
      actually asking for
    - **Writing a combined function** — a default parameter, a
      manual counter, no `sum()`/`len()` shortcuts
    - **2D NumPy** — `.shape` and `arr[row, col]` indexing
    - **Slicing and repetition** — negative steps, and list `*` vs.
      array `*`
    - **Tracing** — follow the exact order of execution, including
      what gets printed vs. returned
    - **Testing: floats, boundaries, ties** — round before comparing
      floats, and target the exact edge case
    - **Debugging: contract first** — read the docstring before the
      code, and watch for sentinel values
    - **Quick review** — stub rules, import errors, and the course's
      style rules
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Default Parameters
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def apply_late_fee(balance, fee=0.25):
        return balance + fee

    apply_late_fee(2.00)          # ?
    apply_late_fee(2.00, 1.00)    # ?
    apply_late_fee(balance=2.00, fee=1.00)  # ?
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer: `2.25`, `3.00`, `3.00`

    - First call: only `balance` is given, so `fee` falls back
      to its default, `0.25` → `2.00 + 0.25 = 2.25`
    - Second call: `1.00` fills `fee` positionally (it's the
      second parameter) → `2.00 + 1.00 = 3.00`
    - Third call: the same two values, passed by name instead
      of position — same result, `3.00`
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    total = 2.00
    apply_late_fee(total)  # result discarded
    print(total)            # ?
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer: `2.0` — unchanged

    - `apply_late_fee(total)` runs, computes `2.00 + 0.25 = 2.25`,
      and `return`s it — but nothing on that line catches it
    - Without writing `total = apply_late_fee(total)`, that
      `2.25` is thrown away the moment the call finishes
    - `total` itself was never reassigned, so it's still `2.00`
      when printed
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    A parameter with a default can always be left out. In a function
    header, every parameter *after* the first default must also have
    one.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 13](https://BU-EK125.github.io/EK125/class/Class13.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Functions With No Return
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def show_title(title):
        print(f"Now reading: {title}")

    show_title("Dune")        # ?
    x = show_title("Dune")    # ?
    print(x)                   # ?
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer: `x` is `None`

    - `show_title("Dune")` prints the line and nothing is stored,
      so there's nothing to look at afterward
    - `x = show_title("Dune")` prints that same line — printing
      happens either way, whether or not you capture the result
    - There's no `return` in the function, so Python fills one in
      automatically: `None`. That's what ends up in `x`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Printing and returning are separate actions — one produces
    visible output, the other hands data back to the caller. A
    function with no `return` statement always hands back `None`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 13](https://BU-EK125.github.io/EK125/class/Class13.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Scope: Local vs. Global
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    goal = 25

    def meets_goal(pages):
        goal = 30
        return pages >= goal

    print(meets_goal(28), goal)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer: `False 25`

    `goal = 30` inside the function creates a brand-new **local**
    variable — it doesn't touch the global `goal` at all. The
    function compares against its own local `30` (so `28 >= 30`
    is `False`), and the global `goal` printed afterward is still
    `25`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Assigning to a name inside a function always creates a local
    variable, even if a global one with the same name exists — it
    never reaches out and modifies the global by that assignment.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def summarize(word):
        total = 0
        for ch in word:
            total = total + 1
        print(total)

    summarize("dune")
    print(total)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer: `NameError`

    `summarize("dune")` runs fine and prints `4`. But `total` only
    exists inside `summarize` — once the function returns, it's
    gone. The last line raises `NameError`, since the main program
    never defined its own `total`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    A variable created inside a function only lives for as long as
    that function is running — nothing outside the function can see
    it, before or after the call.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 14](https://BU-EK125.github.io/EK125/class/Class14.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mutable vs. Immutable Arguments
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def add_book(shelf, title):
        shelf.append(title)
        title = title.upper()
        return title

    books = ["Dune"]
    result = add_book(books, "Emma")
    print(books)
    print(result)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer: `['Dune', 'Emma']` and `EMMA`

    - `shelf.append(title)` changes the *same* list object the
      caller passed in — so `books` becomes `["Dune", "Emma"]`,
      visible outside the function too
    - `title = title.upper()` makes `title` point at a brand-new
      string, `"EMMA"` — it never touches the caller's original
      string, it just rebinds the local name
    - `return title` hands back that new string, so
      `print(books)` shows `['Dune', 'Emma']` and `print(result)`
      shows `EMMA`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Lists are mutable, so an in-place change (`.append`, `.sort`,
    `[i] = ...`) is visible outside the function. Strings and
    numbers are not — any "change" to one is really a brand-new
    value, and reassigning a parameter name never reaches back to
    the caller's variable.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 13](https://BU-EK125.github.io/EK125/class/Class13.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Dictionary Gotchas
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Dictionaries are everywhere once you're building anything real —
    a single wrong choice between `in`, `.get()`, and `[]` is one of
    the most common ways a function that "looks right" quietly
    breaks on a value it wasn't expecting.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    book = {"title": "Dune", "copies": 3}
    "copies" in book         # ?
    3 in book                 # ?
    book.get("author")         # ?
    book.get("author", "?")    # ?
    book["author"]              # ?
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    for key, value in book.items():
        print(key, value)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer: `True`, `False`, `None`, `"?"`, `KeyError`

    - `"copies" in book` → `True`: `in` only ever looks at keys
    - `3 in book` → `False`: `3` is a *value* here, not a key, so
      `in` never finds it
    - `book.get("author")` → `None`: a missing key with no
      default quietly returns `None`
    - `book.get("author", "?")` → `"?"`: a missing key with a
      default returns that default instead
    - `book["author"]` → `KeyError`: square brackets are the only
      one of these that raises on a missing key
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `in` on a dictionary always checks keys, never values.
    `.get()` is the safe way to handle a key that might be
    missing; square brackets are the only one of the three that
    raises.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 12](https://BU-EK125.github.io/EK125/class/Class12.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Dict of Lists, List of Dicts
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    library = {
        "title": ["Dune", "Emma", "Kim"],
        "copies": [3, 1, 2],
    }
    library["title"][1]    # ?
    len(library)             # ?
    len(library["title"])    # ?
    library["title"][0:2]    # ?
    library.get("author", [])  # ?
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer: `"Emma"`, `2`, `3`, `["Dune", "Emma"]`, `[]`

    - `library["title"][1]` → `"Emma"`: index into the list
      stored under the `"title"` key
    - `len(library)` → `2`: the dictionary has two keys,
      `"title"` and `"copies"` — `len()` counts *keys*
    - `len(library["title"])` → `3`: that one list has three
      books in it — a completely different number from the one
      above, easy to mix up
    - `library["title"][0:2]` → `["Dune", "Emma"]`: ordinary list
      slicing, once you're inside the right key
    - `library.get("author", [])` → `[]`: a missing key with an
      empty-list default, safe to loop over immediately
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `len()` of the whole dictionary counts its keys; `len()` of
    one of its lists counts that list's entries — two very
    different numbers that are easy to mix up.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 12](https://BU-EK125.github.io/EK125/class/Class12.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Writing a Combined Function
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Real functions rarely exercise just one skill at a time — here's
    what it looks like when several show up together in a single,
    realistic function, the way they do in your own project code.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Loop over a dictionary whose values are lists (some empty), and
    return a new dictionary of counts — no `sum()` or `len()` for the
    counting itself.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    pages_read = {
        "Mia": [32, 0, 45, 50],
        "Noah": [],
        "Ava": [20, 20, 20],
    }

    def count_weeks_met(pages_read, goal=25):
        """Count weeks each reader met the goal."""
        weeks_met = {}
        for name in pages_read:
            count = 0
            for pages in pages_read[name]:
                if pages >= goal:
                    count = count + 1
            weeks_met[name] = count
        return weeks_met
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    results = count_weeks_met(pages_read)
    for name, count in results.items():
        print(f"{name}: {count}")
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer

    ```
    Mia: 3
    Noah: 0
    Ava: 0
    ```

    Mia's 4 weeks: `32, 0, 45, 50` — three are `>= 25`. Noah never
    logged a page, so his empty list just never enters the inner
    loop; `count` stays `0` with no special-case code required.
    Ava's `20, 20, 20` never reaches the `25` goal, so she's `0`
    too.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `goal=25` is a default parameter; the manual `count` accumulator
    handles Noah's empty list for free, with no special case. Swap
    `>=` for `>` and it's now strict instead of inclusive — same
    structure, one symbol different.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 13](https://BU-EK125.github.io/EK125/class/Class13.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 2D NumPy
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    grid = np.array([[5, 10], [3, 8], [7, 2]])
    grid.shape    # ?
    grid[1, 0]    # ?
    grid[:, 1]    # ?
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer: `(3, 2)`, `3`, `[10  8  2]`

    - `grid.shape` → `(3, 2)`: 3 rows, 2 columns
    - `grid[1, 0]` → `3`: row index 1, column index 0 — the
      second row, `[3, 8]`, first entry
    - `grid[:, 1]` → `[10  8  2]`: every row (`:`), column index
      1 only — the second column, read top to bottom
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `.shape` reports `(rows, columns)`. `arr[row, col]` indexes
    directly — a colon in either spot grabs a whole row or column
    instead of a single entry.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 11](https://BU-EK125.github.io/EK125/class/Class11.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Slicing and Repetition
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    books = ["Dune", "Emma", "Kim", "1984"]
    books[::-1]              # ?
    books[::2]                # ?
    list(range(10, 0, -2))    # ?
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    - `books[::-1]` reads the whole list backward:
      `["1984", "Kim", "Emma", "Dune"]`
    - `books[::2]` starts at the beginning and takes every
      second entry: `["Dune", "Kim"]`
    - `range(10, 0, -2)` counts down from 10, stopping before 0,
      in steps of 2: `[10, 8, 6, 4, 2]`
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    A negative step walks backward instead of forward; any other
    step size just changes how many entries get skipped each
    time. `range(start, stop, step)` follows the exact same rule
    with plain numbers instead of a sequence.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    tags = ["new"]
    tags * 2            # ?
    np.array([1, 2]) * 2   # ?
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer: `["new", "new"]` and `[2 4]`

    - `tags * 2` repeats the list: `["new", "new"]` — the same
      element written out twice
    - `np.array([1, 2]) * 2` instead multiplies **each entry**
      by 2: `[2 4]`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    The same `*` operator means something completely different
    depending on the type it's applied to — repetition for a
    plain list, element-wise multiplication for a NumPy array.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 10](https://BU-EK125.github.io/EK125/class/Class10.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Tracing
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Tracing — predicting exactly what a program does, one line at a
    time — is the most reliable way to catch a bug before it ships,
    and the only real way to understand code someone else wrote.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Mix a default parameter, `enumerate`, a dictionary that
    accumulates as it goes, and a `None` result — trace it line by
    line before checking the answer.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def letter_count(word, start_at=0):
        counts = {}
        for i, ch in enumerate(word):
            if i >= start_at:
                counts[ch] = counts.get(ch, 0) + 1
        print(counts)

    outcome = letter_count("libris")
    print(outcome)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer

    ```
    {'l': 1, 'i': 2, 'b': 1, 'r': 1, 's': 1}
    None
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    The dictionary print fires *inside* the call. `letter_count` has
    no `return`, so `outcome` — and the second `print` — is `None`,
    even though the function clearly did real work.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 13](https://BU-EK125.github.io/EK125/class/Class13.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Testing: Floats, Boundaries, Ties
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    A test is only useful if it's aimed at a specific way the code
    could be wrong — not just any input. These are three of the
    most common blind spots: places a careless test quietly passes
    even when the function doesn't actually work.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def average_rating(ratings):
        return sum(ratings) / len(ratings)

    r = [4.0, 4.1, 4.5]
    check("avg", 4.2, average_rating(r))
    check("avg", 4.2, round(average_rating(r), 1))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer: first check FAILS, second check PASSES

    `average_rating` is correct — `(4.0+4.1+4.5)/3` is
    mathematically `4.2`. But floating-point arithmetic can store
    that as something like `4.199999999999999` instead of exactly
    `4.2`, so comparing with `==` fails even though the function
    did its job. Rounding inside the *test* (not the function)
    clears up that noise, so the second `check()` passes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Round inside the test, not the function, unless the contract
    itself promises rounding — a correct function can still FAIL a
    `check()` that compares floats with `==`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    check("at quota", True, reaches_quota(45, 45))
    tied = {"Mia": 50, "Ava": 50}
    check("earliest tie", "Mia", top_reader(tied))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer: both checks PASS

    The first assumes `reaches_quota` treats `>=` as inclusive, so
    a page count exactly equal to the quota still counts as
    reaching it. The second assumes `top_reader` breaks a tie by
    picking whichever name it saw *first* — here, `"Mia"`, since
    she comes first in `tied`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    A boundary test uses a value exactly at the edge of a
    condition (not safely inside or outside it). A tie test uses
    two equal values to check which one a function picks when
    there's no single "correct" one.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 17](https://BU-EK125.github.io/EK125/class/Class17.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Debugging: Contract First
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Most debugging mistakes don't come from not knowing Python —
    they come from starting in the wrong place. Before touching any
    code, the contract tells you exactly what "right" is supposed
    to look like.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def worst_week(pages):
        """Return the lowest-page week."""
        worst = 0
        for i in range(len(pages)):
            if pages[i] < pages[worst]:
                worst = i
        return worst
    ```
    Does this function match its own contract?
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer: no — it returns an index, not a week

    The docstring says "the lowest-page week" — but the code
    returns a list **position** (an `int` index into `pages`), not
    a week number. If weeks are labeled starting at 1, or logged
    out of order, that index doesn't actually identify the week at
    all.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Read the contract before the code: does "week" mean an index,
    or a label? A function can run without error and still not do
    what its own docstring promises.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    pages = [32, -999, 45, 50]  # -999 = not logged
    average = sum(pages) / len(pages)
    ```
    What does `average` actually come out to?
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer: `-218.0`

    `sum([32, -999, 45, 50])` is `-872`, divided by 4 entries is
    `-218.0` — a wildly wrong "average" that the code never
    complains about, because `-999` is just a number to Python,
    not a flag meaning "missing."
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    A sentinel meant to signal "missing" corrupts the statistic if
    nothing filters it out first — check the loader before
    trusting the analyst's math.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```
    Traceback (most recent call last):
      File "main.py", line 6, in main
        for s in scores:
    TypeError: 'int' object is not iterable
    ```
    ```python
    # Last line of compute_scores in scorer.py:
    """Returns: a list of scores."""
    return total
    ```
    Which file actually has the bug?
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer: `scorer.py`, not `main.py`

    `main.py` tries to loop over `scores`, and crashes there
    because that's where the mismatch first gets used. But the
    actual contract violation is in `scorer.py`: the docstring
    promises a list of scores, and the code hands back a single
    `int` — the running `total` — instead.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    The file that crashes and the file with the bug are often not
    the same file — the traceback tells you where the program gave
    up, not where the mistake was made. Here the wrong *type* broke
    the contract, not a wrong key name — the same "check upstream
    first" instinct still finds it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 18](https://BU-EK125.github.io/EK125/class/Class18.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Quick Review
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - **A contract describes what a function does, never how** — a
      header, parameters, and a return value, not the code inside it
    - **A faithful stub:** same header and docstring, `return`
      (never `print`) the contract's own example values, with the
      correct types
    - `ModuleNotFoundError` — can't find the **file**.
      `ImportError` — file found, the **name** doesn't match
    - Importing a file runs every top-level line in it, including a
      stray `print()` outside a function
    - `if __name__ == "__main__":` — code below it runs only when
      *this* file is run directly, not when another file imports it
    - Style rules: no global variables, no `break`, no `continue`,
      no `while True`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def test_apply_late_fee():
        print(apply_late_fee(2.00))

    if __name__ == "__main__":
        test_apply_late_fee()
    ```
    What happens when a teammate's `main.py` imports
    `apply_late_fee` from this file?
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer: nothing prints

    `test_apply_late_fee()` only runs inside the
    `if __name__ == "__main__":` block, and that block only
    executes when *this* file is the one being run directly — not
    when another file imports a function out of it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    A test function guarded by `if __name__ == "__main__":` runs
    when you execute this file directly, but stays silent on
    import — exactly the behavior you want from a file's own
    self-test.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 16](https://BU-EK125.github.io/EK125/class/Class16.html)
    """)
    return


if __name__ == "__main__":
    app.run()
