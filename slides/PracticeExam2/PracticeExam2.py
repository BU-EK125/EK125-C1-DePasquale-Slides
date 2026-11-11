import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/PracticeExam2.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # EK125 Exam 2

    ### Practice Exam Walkthrough

    Questions, solutions, and tips

    📖 Work through each problem yourself using the practice exam, then
    use this deck to check your answer and pick up a few extra tips.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 1: True/False (a)

    `list(range(3, 8, 2))` produces `[3, 5, 7]`.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ True

    Starting at 3, stepping by 2, stopping before 8: 3, 5, 7.
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
    mo.md('''
    ## Problem 1: True/False (b)

    ```python
    fruits = ["apple", "banana", "cherry"]
    for i, fruit in enumerate(fruits):
        print(i, fruit)
    ```

    This prints `0 apple`, `1 banana`, `2 cherry` — all on the
    same line.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ False

    Each `print()` call ends with a newline by default, so each
    pair lands on its *own* line, not all together.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 7](https://BU-EK125.github.io/EK125/class/Class7.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 1: True/False (c)

    In a dictionary, keys must be unique, but values do not need
    to be unique.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ True

    Two different keys can map to the same value — only the keys
    themselves have to be distinct.

    ```python
    grades = {"Alice": 90, "Bob": 90, "Charlie": 75}
    ```
    `"Alice"`, `"Bob"`, and `"Charlie"` are all distinct keys —
    that's required. But `"Alice"` and `"Bob"` both map to `90`,
    the same value, and that's completely fine. Trying to write
    a second `"Alice"` key, on the other hand, would just
    overwrite the first one instead of creating a duplicate.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 12](https://BU-EK125.github.io/EK125/class/Class12.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 1: True/False (d)

    ```python
    grades = {"Alice": 90, "Bob": 85}
    grades.get("Charlie")
    ```

    This causes an error.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ False

    `.get()` returns `None` for a missing key instead of raising
    `KeyError`. Only square brackets (`grades["Charlie"]`) would
    error.
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
    ## Problem 1: True/False (e)

    NumPy arrays can contain elements of different data types
    (e.g., integers and strings in the same array).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ False

    NumPy arrays are homogeneous — every element shares one dtype.
    A Python list is what lets you mix types freely.
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
    ## Problem 1: True/False (f)

    Even without `return`, variables defined inside a function are
    accessible outside that function after the function has been
    called.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ False

    A variable created inside a function is **local** — it's gone
    the moment the function returns. Only `return` can hand a
    value back out.
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
    ## Problem 1: True/False (g)

    The slice `word[2:5]` includes the character at index 5.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ False

    The end index in a slice is always **exclusive** — `word[2:5]`
    stops right before index 5.
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
    ## Problem 1: True/False (h)

    List comprehensions can include conditional statements (`if`
    conditions) to filter which elements are included.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ True

    `[x for x in items if condition]` — the trailing `if` filters
    which values make it into the new list.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 7](https://BU-EK125.github.io/EK125/class/Class7.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 2: Multiple Choice (a)

    ```python
    numbers = [10, 20, 30, 40]
    print(numbers[1:3])
    ```

    A. `[10, 20]`  B. `[20, 30]`
    C. `[20, 30, 40]`  D. `[10, 20, 30]`
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ B — `[20, 30]`

    Index 1 up to (not including) index 3: elements at positions
    1 and 2.
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
    mo.md('''
    ## Problem 2: Multiple Choice (b)

    ```python
    myDict = {"a": 1, "b": 2, "c": 3}
    myDict["d"] = 4
    myDict["a"] = 0
    print(len(myDict))
    ```

    A. 3  B. 4  C. 5  D. An error occurs
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ B — 4

    `myDict["d"] = 4` adds a new key (now 4 keys). Reassigning
    `"a"` changes a value in place — it doesn't add a key.
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
    mo.md('''
    ## Problem 2: Multiple Choice (c)

    ```python
    def mystery(x, y):
        return x + y * 2

    result = mystery(5, 3)
    ```

    A. 11  B. 16  C. 13  D. 8
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ A — 11

    `*` binds tighter than `+`: `y * 2` is `3 * 2 = 6` first, then
    `x + 6` is `5 + 6 = 11`. Operator precedence always beats
    doing it purely in your head — trace it one step at a time.
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
    ## Problem 2: Multiple Choice (d)

    Which statement is true about NumPy arrays?

    A. Can change size (not shape) after creation
    B. Support element-wise operations on entire arrays
    C. Are the same as Python lists
    D. Can only store integers
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ B

    `arr * 2`, `arr + arr`, `arr > 5` all apply to every element
    at once — no loop needed. That's the core reason to reach for
    NumPy over a plain list.
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
    ## Problem 3: Expression Evaluation (a)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    students = {"name": "Alice", "age": 20}
    students["major"] = "Engineering"
    students.pop("name")
    len(students)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `2`

    Start with 2 keys, add `"major"` (3 keys), then `.pop("name")`
    removes one, back down to 2.
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
    mo.md('''
    ## Problem 3: Expression Evaluation (b)

    ```python
    scores = {"quiz1": 85, "quiz2": 90}
    scores.keys()
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `dict_keys(['quiz1', 'quiz2'])`

    `.keys()` returns a *view* of the keys, in insertion order —
    not a plain list, though it behaves like one in a loop.
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
    mo.md('''
    ## Problem 3: Expression Evaluation (c)

    ```python
    nums = [0, 1, 2, 3, 4]
    nums[4:1:-1]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `[4, 3, 2]`

    Starting at index 4, stepping by -1, stopping *after* index 2
    (index 1 is excluded).
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
    mo.md('''
    ## Problem 3: Expression Evaluation (d)

    ```python
    word = "Python"
    word[-3:]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `'hon'`

    A negative start counts from the end; an empty `end` means
    "through the last character" — the last three letters.
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
    mo.md('''
    ## Problem 3: Expression Evaluation (e)

    ```python
    [x**2 for x in range(4)]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `[0, 1, 4, 9]`

    Squares of 0, 1, 2, 3 — `range(4)` stops before 4.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 7](https://BU-EK125.github.io/EK125/class/Class7.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 3: Expression Evaluation (f)

    ```python
    import numpy as np
    arr = np.array([2, 4, 6])
    arr * 2
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `array([4, 8, 12])`

    Element-wise multiplication — every entry doubles. A plain
    list would instead repeat: `[2, 4, 6, 2, 4, 6]`.
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
    mo.md('''
    ## Problem 3: Expression Evaluation (g)

    ```python
    grades = {"Alice": 90, "Bob": 85}
    grades.get("Charlie", -1)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `-1`

    The second argument to `.get()` is the default to return when
    the key is missing — no error either way.
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
    mo.md('''
    ## Problem 3: Expression Evaluation (h)

    ```python
    list(range(2, 10, 3))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `[2, 5, 8]`

    2, then 2+3=5, then 5+3=8; the next value (11) would be past
    10, so the sequence stops.
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
    mo.md('''
    ## Problem 4: Nested Lists and Indexing

    ```python
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    coordinates = [(0, 0), (1, 2), (3, 4)]
    ```

    Eight expressions below use this setup, sequentially.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Keep this setup in mind

    Each part (a)–(h) on the next slides reuses `matrix` and
    `coordinates` exactly as defined here.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 7](https://BU-EK125.github.io/EK125/class/Class7.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 4 (a): `matrix[1][2]`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `6`

    Row index 1 is `[4, 5, 6]`; position 2 in that row is `6`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 7](https://BU-EK125.github.io/EK125/class/Class7.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 4 (b): `matrix[0]`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `[1, 2, 3]`

    The whole first row, as a list.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 7](https://BU-EK125.github.io/EK125/class/Class7.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 4 (c): `len(matrix)`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `3`

    `len()` of a list of lists counts the outer rows, not the
    inner elements.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 7](https://BU-EK125.github.io/EK125/class/Class7.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 4 (d): `matrix[-1][0]`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `7`

    `-1` is the last row (`[7, 8, 9]`); position 0 is `7`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 7](https://BU-EK125.github.io/EK125/class/Class7.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 4 (e)

    ```python
    for x, y in coordinates:
        print(x + y, end=" ")
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `0 3 7 `

    Each tuple unpacks into `x, y`: 0+0, 1+2, 3+4 — all on one
    line because of `end=" "`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 7](https://BU-EK125.github.io/EK125/class/Class7.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 4 (f)

    ```python
    [row[0] for row in matrix]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `[1, 4, 7]`

    The first element of each row — a classic "grab one column"
    comprehension.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 7](https://BU-EK125.github.io/EK125/class/Class7.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 4 (g): `matrix[2][2]`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `9`

    Last row, last column.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 7](https://BU-EK125.github.io/EK125/class/Class7.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 4 (h): `coordinates[1][1]`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `2`

    `coordinates[1]` is the tuple `(1, 2)`; its position 1 is `2`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 7](https://BU-EK125.github.io/EK125/class/Class7.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 5: Code Tracing

    ```python
    def process(numbers):
        result = []
        for num in numbers:
            if num % 2 == 0:
                result.append(num * 2)
        return result

    data = [1, 2, 3, 4, 5]
    output = process(data)
    print(output)

    inventory = {"apples": 10, "bananas": 5}
    for item, count in inventory.items():
        print(f"{item}: {count}")
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Output

    ```
    [4, 8]
    apples: 10
    bananas: 5
    ```

    `process` keeps only even numbers, doubling each one. Then
    `.items()` unpacks every key-value pair for the print loop.
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
    mo.md('''
    ## Problem 6: Write a Function

    Write `calculate_average(numbers)`: returns the average of a
    list of numbers, or `0` if the list is empty.

    ```python
    calculate_average([10, 20, 30])  # 20.0
    calculate_average([])            # 0
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    def calculate_average(numbers):
        if len(numbers) == 0:
            return 0
        return sum(numbers) / len(numbers)
    ```

    💡 Check the empty-list case *first* — dividing by `len([])`
    would crash with `ZeroDivisionError` otherwise.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 13](https://BU-EK125.github.io/EK125/class/Class13.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 7: Contract → Stub (a)

    ```python
    def summarize_output(data, target):
        """Summarize daily solar panel output.

        Returns: dict with "days_met" (int),
        "best_day" (int), "average" (float).
        Example: {"days_met": 2, "best_day": 4,
                  "average": 5.25}
        """
    ```

    Write a faithful stub body.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    return {"days_met": 2, "best_day": 4,
            "average": 5.25}
    ```

    Same three keys, spelled exactly, with the example's own
    values and types — `return`, never `print`.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 16](https://BU-EK125.github.io/EK125/class/Class16.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 7 (b)

    Write the import line for `summarize_output`, which lives in
    `solar_tools.py`, into a `main.py` in the same folder.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer

    ```python
    from solar_tools import summarize_output
    ```

    `main.py` needs to *call* `summarize_output` without
    redefining it, so it imports the already-written function
    from the file it actually lives in. Two details matter: the
    module name is the filename with no `.py`, and importing the
    function itself (not the whole module) means you can write
    `summarize_output(...)` directly, instead of
    `solar_tools.summarize_output(...)`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 16](https://BU-EK125.github.io/EK125/class/Class16.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 7 (c)

    ```python
    log = {"day": [1, 2, 3, 4, 5],
           "kwh": [4.2, 5.0, 6.1, 3.8, 6.1]}
    summary = summarize_output(log, 5.0)
    ```

    Work out the real function's result by hand.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ `{"days_met": 3, "best_day": 3, "average": 5.04}`

    Walk the five days against `target = 5.0`:

    | day | kwh | met? |
    |-----|-----|------|
    | 1   | 4.2 | no   |
    | 2   | 5.0 | yes — equals target, counts as "at or above" |
    | 3   | 6.1 | yes  |
    | 4   | 3.8 | no   |
    | 5   | 6.1 | yes  |

    `days_met` is 3 (days 2, 3, 5). `best_day` is 3, not 5 — days
    3 and 5 tie for the highest output at 6.1, and ties go to the
    *earliest* day. `average` is the total output over all five
    days, met or not: `(4.2+5.0+6.1+3.8+6.1) / 5 = 25.2 / 5 = 5.04`.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 16](https://BU-EK125.github.io/EK125/class/Class16.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 7 (d)

    Using `summary` from part (c), print exactly:

    ```
    Best day: 3
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    print(f"Best day: {summary['best_day']}")
    ```

    `summary` is the dict from part (c), where `"best_day"` is
    `3` — so the f-string drops that value in and the line prints
    exactly `Best day: 3`. Watch the quote style: single quotes
    around the dictionary key inside an f-string that's itself in
    double quotes; mixing those up is a `SyntaxError`.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 16](https://BU-EK125.github.io/EK125/class/Class16.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 7 (e)

    A teammate's stub body runs with no error, but breaks the
    contract in three separate ways:

    ```python
    return {"Days_Met": 2, "best_day": 4.0,
            "average": "5.25"}
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Three violations

    The contract from part (a) promises exactly three keys —
    `"days_met"` (int), `"best_day"` (int), `"average"` (float).
    This stub runs without error because Python never checks
    keys or types against a docstring, but it breaks the
    contract three separate ways:

    1. `"Days_Met"` should be `"days_met"` — keys are case
       sensitive, so any caller that writes `summary["days_met"]`
       hits a `KeyError`, even though a key named "the same thing"
       is sitting right there.
    2. `best_day` is `4.0`, a float; the contract promises `int`.
       Code that assumes an index (`pages[best_day]`) could behave
       oddly with a float instead.
    3. `average` is `"5.25"`, a string; the contract promises
       `float`. Any arithmetic on it — `summary["average"] * 2` —
       crashes instead of computing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 16](https://BU-EK125.github.io/EK125/class/Class16.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 8: List Comprehensions (a)

    Create a list of squares of 1 through 10 (inclusive):
    `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    [x**2 for x in range(1, 11)]
    ```

    `range(1, 11)` is the "inclusive of 10" trick: stop one past
    the value you want to include.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 7](https://BU-EK125.github.io/EK125/class/Class7.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 8 (b)

    `words = ["apple", "banana", "cherry"]` — create a list of
    each word's length: `[5, 6, 6]`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    [len(word) for word in words]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 7](https://BU-EK125.github.io/EK125/class/Class7.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 8 (c)

    `numbers = [1, 2, ..., 10]` — keep only the even numbers:
    `[2, 4, 6, 8, 10]`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    [n for n in numbers if n % 2 == 0]
    ```

    💡 If you can write the `for` loop version first, the
    comprehension is just that loop flattened onto one line.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 7](https://BU-EK125.github.io/EK125/class/Class7.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 9: File I/O

    Write `temperatures.txt` with three readings (72, 75, 68, one
    per line), read them back as integers, then print:

    ```
    Average temperature: 71.66666666666667
    ```

    Must use `with` for both the read and the write.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    with open('temperatures.txt', 'w') as file:
        file.write('72\\\\n')
        file.write('75\\\\n')
        file.write('68\\\\n')
    ```
    ```python
    with open('temperatures.txt', 'r') as file:
        temperatures = []
        for line in file:
            temperatures.append(int(line))

    average = sum(temperatures) / len(temperatures)
    print(f"Average temperature: {average}")
    ```

    💡 `int(line)` works even with the trailing newline still
    attached — Python's `int()` ignores surrounding whitespace.
    ''')
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
    ## Problem 10: NumPy Array Operations

    Create an array `[10, 20, 30, 40, 50]`, multiply it by 3, and
    print both:

    ```
    Original: [10 20 30 40 50]
    Multiplied: [ 30 60 90 120 150]
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    import numpy as np
    arr = np.array([10, 20, 30, 40, 50])
    multiplied = arr * 3
    print(f"Original: {arr}")
    print(f"Multiplied: {multiplied}")
    ```

    💡 `arr * 3` makes a *new* array — it never changes `arr`
    itself unless you reassign it back.
    ''')
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
    ## Nice Work

    A few cross-cutting habits that showed up again and again:

    - **Trace loops on paper**, one line at a time.
    - Know which built-ins are **mutable** (lists) vs **immutable**
      (strings, tuples) — cold.
    - For programming problems, **match the output format exactly** —
      extra or missing punctuation costs points even with correct
      logic.

    Good luck!
    """)
    return


if __name__ == "__main__":
    app.run()
