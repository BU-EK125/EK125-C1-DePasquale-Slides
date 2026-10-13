import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class11.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Digging into Arrays with NumPy

    ### Creating, Indexing, and Testing NumPy Arrays

    *Class 11*

    📖 [Full reading: Class 11](https://BU-EK125.github.io/EK125/class/Class11.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## What is NumPy?

    NumPy arrays store elements that are all the **same type** — usually
    numbers — and come with fast, built-in math operations. By convention,
    it's always imported as `np`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Array Basics: Dimensions and Axes

    A 1D array is a single row of values — one axis. A 2D array has rows
    **and** columns — two axes. NumPy calls dimensions **axes**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    import numpy as np

    arr1d = np.array([31, 42, 11])
    print(arr1d)

    arr2d = np.array([[-2, 18, 9, 32], [44, -7, 4, 99]])
    print(arr2d)
    ```

    ```
    [31 42 11]
    [[-2 18  9 32]
     [44 -7  4 99]]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Creating Arrays: Attributes

    `np.array()` turns a list into an array. `.dtype`, `.ndim`, `.shape`,
    and `.size` describe it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    arr1d = np.array([31, 42, 11])
    print(arr1d.dtype)
    print(arr1d.ndim)
    print(arr1d.shape)
    print(arr1d.size)
    ```

    ```
    int64
    1
    (3,)
    3
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `.shape` is always a **tuple** — even for a 1D array, like `(3,)` here.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Creating 2D Arrays

    Pass a **list of lists** to `np.array()` — each inner list becomes one
    row.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    arr2d = np.array([[1, 3, 8], [-2, 5, 33]])
    print(arr2d)
    print(arr2d.shape)
    ```

    ```
    [[ 1  3  8]
     [-2  5 33]]
    (2, 3)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Array Creation Functions

    `arange` works like `range()` but returns an array. `linspace` picks
    evenly spaced points. `zeros` (and similarly `ones`/`full`) fills an
    array with one repeated value.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    print(np.arange(3, 9, 2))
    print(np.linspace(1, 9, 3))
    print(np.zeros((2, 4), dtype=int))
    ```

    ```
    [3 5 7]
    [1. 5. 9.]
    [[0 0 0 0]
     [0 0 0 0]]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Indexing and Slicing Arrays

    Arrays index and slice **exactly like lists** — 0-based, with negative
    indices counting from the end.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    arr1d = np.array([31, 42, 11])
    print(arr1d[1])
    print(arr1d[-1])
    print(arr1d[:])
    ```

    ```
    42
    11
    [31 42 11]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 2D Indexing: Row, Column

    For a 2D array, give **two indices** separated by a comma: row first,
    then column.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    arr2d = np.array([[1, 3, 8], [-2, 5, 33]])
    print(arr2d[1, 2])
    print(arr2d[0, 1:])
    ```

    ```
    33
    [3 8]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `arr2d[row, col]` — the first index is always the row, the second is
    always the column.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Logical Indexing

    A comparison like `arr > 20` produces an array of `True`/`False`
    values — use it directly to filter the array.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    arr1d = np.array([31, 42, 11])
    logarr = arr1d > 20
    print(logarr)
    print(arr1d[logarr])
    ```

    ```
    [ True  True False]
    [31 42]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    On a 2D array, logical indexing always returns a **flat 1D result** —
    row structure doesn't survive the filter.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Slicing Rows and Columns

    Use `:` alone on one side of the comma to grab an **entire** row or
    column.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    arr2d = np.array([[-2, 18, 9, 32], [44, -7, 4, 99]])
    print(arr2d[0, :])
    print(arr2d[:, 1])
    ```

    ```
    [-2 18  9 32]
    [18 -7]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Subarrays and Steps

    Slice **both** axes at once to pull out a rectangular block, or add a
    step to skip elements along an axis.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    print(arr2d[0:2, 1:3])
    print(arr2d[:, ::2])
    ```

    ```
    [[18  9]
     [-7  4]]
    [[-2  9]
     [44  4]]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Same slice syntax as 1D, just one slice per axis separated by commas —
    this extends the same way to 3D and beyond.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Reshape and Transpose

    `.reshape()` rearranges an array's elements into a new shape; `.T`
    swaps rows and columns.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    arr = np.arange(4)
    print(arr.reshape(2, 2))
    print(arr.reshape(2, 2).T)
    ```

    ```
    [[0 1]
     [2 3]]
    [[0 2]
     [1 3]]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Neither `.reshape()` nor `.T` modifies the original array — both hand
    back a **new** one.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Why Test Your Code?

    A test is a small check that your code produces the output you
    expect — catching bugs now, and catching anything you break later.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## `assert`: Python's Testing Tool

    `assert` checks a condition — if it's `True`, nothing happens; if
    it's `False`, Python raises an `AssertionError` and stops.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    x = 5
    assert x > 0
    assert x > 10
    ```

    ```
    AssertionError
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The Array `assert` Gotcha

    `a == b` on two arrays returns an **array** of booleans, not one
    `True`/`False` — so `assert a == b` doesn't work the way it does for
    a single value.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    a = np.array([1, 2, 3])
    b = np.array([1, 2, 3])
    assert a == b
    ```

    ```
    ValueError: The truth value of an array is ambiguous
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Fix: use `.all()` — `assert (a == b).all()` checks that **every**
    element matches.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Floating Point Error

    Decimal numbers like `0.1` can't be stored **exactly** in binary, so
    tiny rounding errors creep into floating-point arithmetic.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    x = 0.1 + 0.2
    y = 0.3
    print(x)
    print(x == y)
    print(np.allclose(x, y))
    ```

    ```
    0.30000000000000004
    False
    True
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `np.allclose()` (or `np.testing.assert_allclose()` for a full array
    test) compares with a tolerance — never compare floats with `==`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Summary

    - Arrays have **axes** — 1D is a single axis, 2D needs `arr[row, col]`.
    - `.dtype`, `.ndim`, `.shape`, and `.size` describe an array; `.shape`
      is always a tuple.
    - `arange`, `linspace`, `zeros`, and `full` create arrays without
      typing out every element.
    - Indexing and slicing work like lists, plus logical indexing
      (`arr[arr > 0]`) and reshape/transpose for rearranging shape.
    - Never compare floats with `==` — use `np.allclose()` instead.

    📝 [Today's GPP](https://BU-EK125.github.io/EK125/gpps/Class11_GPP.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## HW6 Section 1: NumPy and Testing

    Section 1 of this week's homework (Problems 1–6) covers today's
    material. Let's walk through one of them — Problem 2 — since it's
    the one most directly about floating-point error.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 2: Testing Floating Point Array Equality

    ```python
    a = np.array([[2.0, 4.0, 6.0],
                  [8.0, 10.0, 12.0]])
    ```

    Build two arrays that *should* be identical: one as `a / np.sqrt(2)`,
    the other as `np.sqrt(0.5) * a`. Sum each one, then compare the sums.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Setting up the full logic:**

    - **Two equivalent expressions:** `a / np.sqrt(2)` and
      `np.sqrt(0.5) * a` are the same math, but floating-point arithmetic
      can round each one differently in the last few bits.
    - **Sum and compare:** compute `np.sum()` of each array, then compare
      the two sums with `==` and with `np.isclose()`.
    - **The asserts:** `assert sum1 == sum2` can fail even though the
      math is "the same" — `assert np.isclose(sum1, sum2)` is the one
      that should pass.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Mathematically-equivalent floating-point computations don't always
    produce bit-identical results — that's exactly why tolerance-based
    comparison exists.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Now It's Your Turn

    We only walked through Problem 2 — Problems 1 and 3–6 use the same
    NumPy and testing tools from today's lecture. Work through all six in
    PyCharm, run each part as you write it, and check your output
    against the expected results in the assignment.

    📝 [Today's GPP](https://BU-EK125.github.io/EK125/gpps/Class11_GPP.html)
    """)
    return


if __name__ == "__main__":
    app.run()
