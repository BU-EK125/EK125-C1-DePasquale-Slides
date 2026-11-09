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

    ### Getting Ready, Together

    *Class 20*

    📖 Work through the practice sets first, then use this deck to
    round out a few skills they don't fully cover.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## A Reading Challenge, for Practice
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    One scenario for everything today: a library tracks a summer
    reading challenge. Readers log pages read per week; the library
    tracks its own book inventory. None of this is from the real
    exam — it's a fresh scenario to practice the same skills on.
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

    apply_late_fee(2.00)          # 2.25
    apply_late_fee(2.00, 1.00)    # 3.00
    apply_late_fee(balance=2.00, fee=1.00)
    ```
    First call uses the default fee. Second overrides it
    positionally. Third does the same by keyword.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    total = 2.00
    apply_late_fee(total)  # result discarded
    print(total)            # 2.0 -- unchanged
    ```
    A default is only used when the caller leaves that argument out.
    Calling a function doesn't change the variable you passed in
    unless you reassign it yourself.
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
    ## Functions With No Return
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def show_title(title):
        print(f"Now reading: {title}")

    show_title("Dune")        # prints the line
    x = show_title("Dune")    # prints the line
    print(x)                   # None
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    A function with no `return` statement always hands back `None` —
    whatever it printed along the way is separate from what it
    returned.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Dictionary Basics Under Pressure
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    book = {"title": "Dune", "copies": 3}
    "copies" in book         # True
    3 in book                 # False, not a key
    book.get("author")         # None, no error
    book.get("author", "?")    # "?"
    book["author"]              # KeyError
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
    ### Takeaway

    `in` on a dictionary always checks keys, never values. `.get()`
    never raises `KeyError`; square brackets do.
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
    library["title"][1]    # "Emma"
    len(library)             # 2 -- keys
    len(library["title"])    # 3 -- books
    library["title"][0:2]    # ["Dune", "Emma"]
    library.get("author", [])  # [] -- safe
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `len()` of the whole dictionary counts its keys; `len()` of one
    of its lists counts that list's entries — two very different
    numbers that are easy to mix up.
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
    ## 2D NumPy
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    grid = np.array([[5, 10], [3, 8], [7, 2]])
    grid.shape    # (3, 2)
    grid[1, 0]    # 3
    grid[:, 1]    # [10  8  2]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `.shape` reports (rows, columns). `arr[row, col]` indexes
    directly — a colon in either spot grabs a whole row or column.
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
    books[::-1]              # reversed
    books[::2]                # every other book
    list(range(10, 0, -2))    # [10, 8, 6, 4, 2]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    tags = ["new"]
    tags * 2            # ["new", "new"]
    np.array([1, 2]) * 2   # [2 4]
    ```
    The same `*` operator, two completely different results,
    depending only on whether it's a list or a NumPy array.
    ''')
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
    ## Testing: Floats, Boundaries, Ties
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
    A correct function can still FAIL a `check()` that compares
    floats with `==` — round inside the *test*, not the function,
    unless the contract itself promises rounding.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    check("at goal", True, meets_goal(25, 25))
    tied = {"Mia": 50, "Ava": 50}
    check("earliest tie", "Mia", top_reader(tied))
    ```
    A boundary test uses a value exactly at the goal. A tie test uses
    two equal values to check which one the function picks.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Debugging: Contract First
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
    The docstring says "the lowest-page week" — but the code returns
    a list **position**, not a week number. Read the contract before
    the code: does "week" mean an index, or a label?
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    pages = [32, -999, 45, 50]  # -999 = not logged
    average = sum(pages) / len(pages)
    ```
    A sentinel meant to signal "missing" corrupts the statistic if
    nothing filters it out first — check the loader before trusting
    the analyst's math.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```
    Traceback (most recent call last):
      File "main.py", line 10, in main
        write_summary(stats, "out.txt")
      File "reporter.py", line 6, in write_summary
        f"Average: {stats['avg_pages']}"
    KeyError: 'avg_pages'
    ```
    ```python
    # Last line of summarize in analyzer.py:
    return {"pages_avg": total / count}
    ```
    The crash is in `reporter.py`, but the dictionary was built in
    `analyzer.py` — it returns `pages_avg`, not the contract's
    `avg_pages`. The file that crashes and the file with the bug are
    often not the same file.
    ''')
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
    A test function defined like this runs when you execute this
    file directly, but stays silent when a teammate's `main.py`
    imports a function from it.
    ''')
    return


if __name__ == "__main__":
    app.run()
