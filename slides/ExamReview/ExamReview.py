import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/ExamReview.slides.json",
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

    ### Exam Review

    Questions, solutions, and tips

    📖 Work through each problem yourself using the practice sets, then
    use this deck to check your answer and pick up a few extra tips.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Three Parts
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    For every problem: **try it yourself** first, using the question
    as shown, then **advance** to see the answer and the reasoning
    behind it.

    - **Part One: Practice Exam 2** — general syntax, same style as
      Exam 1.
    - **Part Two: Additional Review** — a few skills neither
      practice set fully drills on its own.
    - **Part Three: Project Practice** — a battery-rig scenario
      built around the project skills: contracts, stubs, tracing,
      debugging.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part One: Practice Exam 2
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
    mo.md("""
    ### ✅ True

    Two different keys can map to the same value — only the keys
    themselves have to be distinct.
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

    No `.py` in the module name, and import the function itself,
    not the whole module, since you'll call it unqualified.
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

    `days_met` is 3 (the contract says "at or above" target, and
    5.0 counts). `best_day` is 3, not 5 — days 3 and 5 tie at 6.1,
    and ties go to the *earliest* day. `average` is `25.2 / 5`.
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

    Watch the quote style: single quotes inside an f-string that's
    itself in double quotes.
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

    1. `"Days_Met"` should be `"days_met"` — keys are case
       sensitive, so this is a `KeyError` waiting to happen.
    2. `best_day` is `4.0` (a float); the contract says `int`.
    3. `average` is `"5.25"` (a string); the contract says `float`
       — arithmetic on it would crash.
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
    ## Part Two: Additional Review
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    A few skills the practice sets above don't fully drill on their
    own. Same idea as before: work the example yourself, then check
    it.
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
    ### Takeaway

    `goal = 30` inside the function creates a brand-new **local**
    variable — it doesn't touch the global `goal` at all. The
    function compares against 30 (so `28 >= 30` is `False`), and
    the global `goal` printed afterward is still 25.
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
    ### Takeaway

    `total` only exists inside `summarize` — once the function
    returns, it's gone. The last line raises `NameError`, since
    the main program never defined its own `total`.
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
    ### Takeaway

    `shelf.append(...)` changes the *same* list the caller passed
    in — `books` becomes `["Dune", "Emma"]`. But `title = ...`
    rebinds the local name only; the caller's own string is never
    touched. Lists are mutable; strings (and numbers) are not.
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 16](https://BU-EK125.github.io/EK125/class/Class16.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part Three: Project Practice
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    A fresh scenario — a lab cycling rechargeable battery cells —
    built to drill the project skills: reading a contract, writing
    a stub, tracing against a contract, and debugging.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 1: Bugs Live at the Seams (a)

    ```python
    def summarize_loads(loads):
        """Returns: "peak_kn" and "mean_kn"."""
        # ... (correct code, not shown) ...

    def print_summary(summary):
        print(f"Peak: {summary['peak']} kN")

    print_summary(summarize_loads([9.0, 12.5, 8.0]))
    ```

    What error does the last line produce?
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `KeyError: 'peak'`

    `print_summary` asks for `"peak"`, but the contract promises
    `"peak_kn"`.
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
    ## Problem 1 (b)

    Which function is off-contract — and how do you know?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ `print_summary` is off-contract

    The contract for `summarize_loads` promises `"peak_kn"`;
    `print_summary` reads `"peak"` instead. Fix the reader, not
    the function that's following its own contract:

    ```python
    print(f"Peak: {summary['peak_kn']} kN")
    ```
    ''')
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
    ## Problem 1 (c)

    Suppose `summarize_loads` instead received loads in **newtons**
    (`[9000.0, 12500.0, 8000.0]`). After the key fix, what prints?
    Syntax, runtime, or logic error — and how would the team catch
    it?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `Peak: 12500.0 kN` — a logic error

    No crash, just a wrong unit. Catch it with a reasonableness
    check: 12,500 kN on a bridge sensor isn't physically
    believable.
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
    mo.md('''
    ## Problem 2: Write a Precise Contract (a)

    ```python
    def load_cycles(filename):
        """Reads the battery data and returns it."""
    ```

    List three questions a teammate couldn't answer from this.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Any three of

    Is the return a dict or a list? What are the exact keys? Are
    values `int` or `float`? What happens to blank or `-999`
    rows? What units? Does it print anything?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 15](https://BU-EK125.github.io/EK125/class/Class15.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 2 (b)

    Rewrite the *Returns* section so no question is left. Rule:
    rows with a blank or `-999` capacity are skipped; result is a
    dict of lists.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    """Returns: dict of lists, keys "cycle" (int),
    "voltage" (float), "capacity_mah" (float). All
    three lists are the same length, in file order.
    Rows with any blank, or capacity -999, are
    skipped entirely.
    Example: {"cycle": [1, 4], "voltage": [3.71,
    3.68], "capacity_mah": [2950.0, 2880.0]}
    """
    ```

    💡 Double-check your own example against the sample file —
    it's easy to accidentally keep a row the contract says to
    skip.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 15](https://BU-EK125.github.io/EK125/class/Class15.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 3: Faithful Stubs (a)

    Contract: `assess_cell` returns `{"cell_id", "fade_pct",
    "passed"}`. Which stub bodies are faithful?

    ```python
    A: return {"cell_id": cell_id, "fade_pct": 12.5,
               "passed": True}
    B: print({"cell_id": cell_id, "fade_pct": 12.5,
              "passed": True})
    C: return {"cell": cell_id, "fade_pct": 12.5,
               "passed": True}
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ A: Yes. B: No. C: No.

    A returns the example, using the real parameter. B prints
    instead of returning — the function gives back `None`. C
    misspells the key (`"cell"` instead of `"cell_id"`) — a
    `KeyError` waiting to happen.
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
    ## Problem 3 (a), continued

    ```python
    # D: fade_pct is a string
    return {
        "cell_id": cell_id,
        "fade_pct": "12.5",
        "passed": True,
    }
    ```
    ```python
    # E: passed is a string
    return {
        "cell_id": cell_id,
        "fade_pct": 12.5,
        "passed": "True",
    }
    ```
    ```python
    # F: a list, not a dict
    return [cell_id, 12.5, True]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ D: No. E: No. F: No.

    D's `fade_pct` is a string, not a float. E's `passed` is the
    *string* `"True"`, not the boolean `True` — `if result["passed"]`
    would be true even for `"False"`! F returns a list with no
    keys at all.
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
    ## Problem 3 (b)

    A stub hard-codes `cell_id: "B7"`. The program calls it for
    "B1", "B2", "B3". What does the report show, and why pass
    `cell_id` through instead?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Every line says "B7"

    It runs, but you can't tell whether `main.py` passed the right
    IDs. Passing `cell_id` through lets the skeleton prove each
    argument arrived where it should.
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
    ## Problem 4: Importing Your Own Files (a)

    ```python
    # cellmath.py
    def to_percent(fraction):
        return fraction * 100

    print("cellmath loaded")

    def test_to_percent():
        print("test:", to_percent(0.25))

    if __name__ == "__main__":
        test_to_percent()
    ```
    ```python
    # main.py
    from cellmath import to_percent
    print("main starts")
    print(to_percent(0.5))
    ```

    Output when you run `main.py`?
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer

    ```
    cellmath loaded
    main starts
    50.0
    ```

    Importing runs every top-level line in `cellmath.py` first —
    that's the `print("cellmath loaded")` line.
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
    ## Problem 4 (b)

    Output when you run `cellmath.py` directly instead?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer

    ```
    cellmath loaded
    test: 25.0
    ```

    `test_to_percent()` only runs here, because `__name__` equals
    `"__main__"` only when the file itself is run directly.
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
    ## Problem 4 (c)

    Which line in `cellmath.py` causes trouble for teammates, and
    where should it go instead?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `print("cellmath loaded")`

    It runs every time anyone imports the file. Delete it, or move
    it inside `test_to_percent()`, under the `__name__` guard.
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
    ## Problem 4 (d)

    What error does each import line cause, in `main.py`?

    1. `from cellmath.py import to_percent`
    2. `from cellmath import to_pct`
    3. `from cellMath import to_percent`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answers

    1. `ModuleNotFoundError` — no `.py` in an import.
    2. `ImportError: cannot import name 'to_pct'` — file found,
       function name wrong.
    3. `ModuleNotFoundError` — capitalization must match exactly.
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
    ## Problem 5: Read a Traceback Across Files (a)

    ```
    Traceback (most recent call last):
      File "main.py", line 9, in <module>
        line = format_cell(result)
      File "formatter.py", line 6, in format_cell
        return f"{result['cell_id']}..."
    TypeError: 'NoneType' not subscriptable
    ```

    Line 8 of `main.py` is `result = assess_cell(...)`. In which
    file, function, and line did the program crash?
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `formatter.py`, in `format_cell`, line 6

    Read bottom-up: the last frame shown is where the crash
    actually happened.
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
    ## Problem 5 (b)

    Which variable is `None`? Which function created that value?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `result` is `None`

    It was created by `assess_cell` in `analyzer.py` (main.py line
    8), then handed to `format_cell`.
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
    ## Problem 5 (c)

    What's the most likely mistake inside `assess_cell`? Whose job
    is it to fix?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ It prints instead of returning

    (Or a `return` sits inside an `if` that never runs.) The owner
    of `analyzer.py` fixes it in their own file — the crash site
    (`formatter.py`) is not the bug site.
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
    ## Problem 5 (d)

    Write one temporary line, added between lines 8 and 9 of
    `main.py`, that would confirm your answer to (b).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    print("SEAM type:", type(result))
    ```

    It would show `<class 'NoneType'>` instead of the expected
    `<class 'dict'>`.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 18](https://BU-EK125.github.io/EK125/class/Class18.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 6: Name the Bug, Fix It (a)

    ```python
    readings = ["3.7", "", "3.9"]
    volts = []
    for text in readings:
        volts.append(float(text))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ RUNTIME

    `ValueError: could not convert string to float: ''`. Fix: only
    convert non-blank text.

    ```python
    if text != "":
        volts.append(float(text))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 19](https://BU-EK125.github.io/EK125/class/Class19.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 6 (b)

    ```python
    if voltage > 4.2
        print("Overcharged!")
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ SYNTAX

    Missing colon. Fix: `if voltage > 4.2:`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 19](https://BU-EK125.github.io/EK125/class/Class19.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 6 (c)

    ```python
    def total_all(values):
        """Return the sum of ALL values."""
        total = 0
        for i in range(1, len(values)):
            total = total + values[i]
        return total
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ LOGIC

    Skips index 0 — `total_all([5, 1, 2])` returns 3, not 8. Fix:

    ```python
    for i in range(len(values)):
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 19](https://BU-EK125.github.io/EK125/class/Class19.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 6 (d)

    ```python
    def count_drops(values):
        drops = 0
        for i in range(len(values)):
            if values[i + 1] < values[i]:
                drops = drops + 1
        return drops
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ RUNTIME

    `IndexError` on the last pass, when `i + 1` runs past the end.
    Fix:

    ```python
    for i in range(len(values) - 1):
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 19](https://BU-EK125.github.io/EK125/class/Class19.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 6 (e)

    ```python
    def sum_list(values):
        total = 0
        for v in values:
            total = total + v

    sum_list([1, 2])
    print(total)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ RUNTIME

    `NameError: name 'total' is not defined` — `total` is local to
    the function, which never returns it. Fix both ends:

    ```python
    return total       # last line of the function
    result = sum_list([1, 2])
    print(result)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 19](https://BU-EK125.github.io/EK125/class/Class19.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 6 (f)

    ```python
    result = {"cell_id": "B7", "fade_pct": 12.5}
    print(result["fade"])
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ RUNTIME

    `KeyError: 'fade'`. Fix:

    ```python
    print(result["fade_pct"])
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 19](https://BU-EK125.github.io/EK125/class/Class19.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 7: Debug Against the Contract (a)

    ```python
    def worst_cycle(data, limit):
        """worst_cycle (int): EARLIEST on a tie.
        below_limit (int): STRICTLY below limit."""
        caps = data["capacity_mah"]
        worst_pos = 0
        below = 0
        for i in range(len(caps)):
            if caps[i] <= caps[worst_pos]:
                worst_pos = i
            if caps[i] <= limit:
                below = below + 1
        ...
    ```

    Trace it for `caps = [2950, 2800, 2900, 2800, 2850]`,
    `limit = 2850.0`: what's `worst_pos` and `below` after each
    pass?
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Trace

    | i | caps[i] | worst_pos | below |
    |---|---|---|---|
    | 0 | 2950 | 0 | 0 |
    | 1 | 2800 | 1 | 1 |
    | 2 | 2900 | 1 | 1 |
    | 3 | 2800 | 3 | 2 |
    | 4 | 2850 | 3 | 3 |

    At i=0, `2950 <= 2950` is True, so `worst_pos` is set to 0
    again (no real change).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 19](https://BU-EK125.github.io/EK125/class/Class19.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 7 (b)

    What does the function return as written? What *should* it
    return?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ As written: cycle 400, below 3. Correct: cycle 200, below 2.

    Two bugs are hiding in those two numbers — find them in the
    next part.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 19](https://BU-EK125.github.io/EK125/class/Class19.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 7 (c)

    Find and fix the two bugs.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Two bugs

    `<=` should be `<` on the tie check — with `<=`, a tie moves
    to the *later* cycle, but the contract wants the earliest:

    ```python
    if caps[i] < caps[worst_pos]:
    ```

    `<=` should be `<` on the limit check — the contract says
    *strictly* below:

    ```python
    if caps[i] < limit:
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 19](https://BU-EK125.github.io/EK125/class/Class19.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 7 (d)

    Write two `check()` calls that FAIL on the buggy code and
    PASS on the fixed code: one for the tie, one for the boundary.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    tied = {"cycle": [1, 2],
            "capacity_mah": [2800.0, 2800.0]}
    check("tie picks earliest", 1,
          worst_cycle(tied, 2000.0)["worst_cycle"])
    ```
    ```python
    at_limit = {"cycle": [1],
                "capacity_mah": [2850.0]}
    result = worst_cycle(at_limit, 2850.0)
    check("at limit, not below", 0,
          result["below_limit"])
    ```

    A test with no tie and no boundary value would PASS on both
    the buggy and fixed code — it wouldn't catch either bug.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    📖 [Review: Class 17](https://BU-EK125.github.io/EK125/class/Class17.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 8: Write the Tests First (a)

    ```python
    def percent_in_range(values, low, high):
        """AT OR ABOVE low, AT OR BELOW high,
        rounded to 1 decimal. Empty: returns 0.0."""
    ```

    Write four `check()` calls from the contract alone, before the
    function exists: a normal case, a boundary case, an empty
    list, and a rounding case.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Four tests

    ```python
    vals = [3.0, 3.5, 4.5, 2.5]
    ends = [3.0, 4.2]
    rounder = [3.5, 5.0, 5.0]
    check("normal", 50.0,
          percent_in_range(vals, 3.0, 4.2))
    check("both ends count", 100.0,
          percent_in_range(ends, 3.0, 4.2))
    check("empty list", 0.0,
          percent_in_range([], 3.0, 4.2))
    check("rounds", 33.3,
          percent_in_range(rounder, 3.0, 4.2))
    ```
    ''')
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
    ## Problem 8 (b)

    Now write `percent_in_range` so all four tests pass.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    def percent_in_range(values, low, high):
        if len(values) == 0:
            return 0.0
        count = 0
        for v in values:
            if v >= low and v <= high:
                count = count + 1
        return round(count / len(values) * 100, 1)
    ```

    💡 Without the empty-list check, that test crashes with
    `ZeroDivisionError` — exactly the bug the smallest-input test
    exists to catch.
    ''')
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
    ## Problem 9: Write the Loader

    Write `load_cycles(filename)`: a dict of lists with keys
    `"cycle"` (int), `"voltage"` (float), `"capacity_mah"`
    (float) — skip any row with a blank value or a capacity of
    `-999`. No `break`, `continue`, or `while True`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    def load_cycles(filename):
        d = {"cycle": [], "voltage": [],
             "capacity_mah": []}
        with open(filename) as f:
            lines = f.readlines()
        for line in lines[1:]:
            p = line.strip().split(",")
            ok = "" not in p and p[2] != "-999"
            if ok:
                d["cycle"].append(int(p[0]))
                d["voltage"].append(float(p[1]))
                mah = float(p[2])
                d["capacity_mah"].append(mah)
        return d
    ```

    💡 Check the whole row *before* converting anything —
    `float("")` crashes, and converting one column at a time risks
    leaving the three lists out of alignment.
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
    ## Problem 10: Write the Main Program

    Three functions, three files: `load_cycles`, `assess_metric`,
    `write_report`. Write a complete `main.py` that loads the
    data, assesses `"voltage"` (limit 3.60) and `"capacity_mah"`
    (limit 2500.0), collects both results, and writes the report
    once. No global variables.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    from loader import load_cycles
    from analyzer import assess_metric
    from reporter import write_report

    def main():
        """Load, assess, and report battery data."""
        data = load_cycles("cells.csv")
        limits = {"voltage": 3.60,
                  "capacity_mah": 2500.0}
        results = []
        for metric, limit in limits.items():
            results.append(
                assess_metric(data, metric, limit))
        write_report(results, "battery_report.txt")

    if __name__ == "__main__":
        main()
    ```

    💡 Keeping `data` and `results` *inside* `main()` is what
    makes "no globals" automatic — call `write_report` once,
    after the loop, not inside it.
    ''')
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
    ## That's Both Practice Sets

    A few cross-cutting habits that showed up again and again:

    - **Read the contract before the code** — it tells you what
      "correct" means, especially for debugging problems.
    - **Trace loops on paper**, one line at a time.
    - Know **position vs. label**: a list index is not the same
      thing as the value it points to.
    - **Boundary and tie cases** are where `<` vs `<=` bugs hide —
      and where a test needs to specifically target them.
    - **Follow the data**: the file that crashes isn't always the
      file with the bug.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Good Luck!

    That's everything — both practice sets and the extra review.
    """)
    return


if __name__ == "__main__":
    app.run()
