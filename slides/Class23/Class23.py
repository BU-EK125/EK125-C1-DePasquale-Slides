import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class23.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Creating Vectors and Matrices in MATLAB

    ### Class 23

    📖 [Full reading: Class 23](https://BU-EK125.github.io/EK125/class/Class23.html)
    📋 [Group Practice: Class 23](https://BU-EK125.github.io/EK125/gpps/Class23_GPP.html)

    *Curious how these slides work? They're built with
    [marimo](https://marimo.io), a Python notebook that runs live,
    right in your browser.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Everything in MATLAB Is a Matrix
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    MATLAB® is short for **Matrix Laboratory** -- every piece of data
    is written to work as a matrix of dimensions r × c ("r by c"), r
    rows and c columns. A vector is just a matrix with one of those
    dimensions equal to 1, and a scalar is a matrix with both equal
    to 1.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Scalar, Vector, Matrix at a Glance

    | | Dimensions | Example |
    |---|---|---|
    | Scalar | 1 × 1 | `7` |
    | Column vector | 3 × 1 | `[2; 5; 9]` |
    | Row vector | 1 × 4 | `[1 4 2 8]` |
    | Matrix | 2 × 2 | `[2 9; 4 1]` |

    Vectors and scalars aren't a separate type in MATLAB -- they're
    just matrices that happen to be thin in one or both directions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Creating Row Vectors
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Direct Entry Method

    ```matlab
    v = [1 2 3 4]
    v = [1,2,3,4]
    ```

    ```python
    import numpy as np
    v = np.array([1, 2, 3, 4])
    ```

    Values separated by spaces or commas -- MATLAB accepts either.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Colon Operator Method

    ```matlab
    vec = 2:6       % 2 3 4 5 6
    nv = 1:2:9      % 1 3 5 7 9  (first:step:last)
    ```

    ```python
    list(range(2, 7))        # 2..6
    list(range(1, 10, 2))    # 1, 3, 5, 7, 9
    ```

    Same inclusive-endpoint rule as the Ranges slide last class:
    MATLAB's `2:6` includes the 6, Python's `range(2, 7)` needs the
    7 to reach the same values.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### linspace Function

    ```matlab
    ls = linspace(3, 15, 5)   % 3  6  9  12  15
    ```

    ```python
    np.linspace(3, 15, 5)   # [3, 6, 9, 12, 15]
    ```

    One of the rare places Python and MATLAB agree exactly --
    `linspace` treats its endpoint as inclusive in both languages.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Accessing Vector Elements
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Each element's position is its **index** (or **subscript**).
    MATLAB indices start at **1**, not 0 -- `newvec(5)` is read aloud
    as "newvec sub 5".

    ```matlab
    newvec = [1 3 5 7 9 3 6 9 12 15];
    newvec(5)    % 9
    ```

    ```python
    newvec = [1, 3, 5, 7, 9, 3, 6, 9, 12, 15]
    newvec[4]    # 9
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Extracting Subsets

    ```matlab
    b = newvec(4:6)   % 7  9  3
    ```

    ```python
    b = newvec[3:6]   # [7, 9, 3]
    ```

    **Watch both ends at once:** porting a MATLAB range isn't just
    `start - 1` -- the *stop* doesn't shift at all, because Python's
    slice stop is already exclusive. `4:6` (index 6 included) becomes
    `3:6` (index 6 excluded, but index 5 -- the same element -- is
    still the last one included), not `3:5`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Creating Column Vectors
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Direct Entry Method

    Values in square brackets separated by **semicolons** (instead of
    commas or spaces) create a column vector:

    ```matlab
    c = [1; 2; 3; 4]
    ```

    ```python
    c = np.array([[1], [2], [3], [4]])
    # or: np.array([1, 2, 3, 4]).reshape(-1, 1)
    ```

    NumPy's plain `np.array([1, 2, 3, 4])` is 1-D -- neither a row nor
    a column. Getting a genuine column takes nested brackets or a
    reshape; MATLAB bakes the row/column distinction into every
    vector from the moment it's created.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Transpose Method

    Any row vector can be transposed into a column vector with the
    **apostrophe**, MATLAB's built-in transpose operator:

    ```matlab
    r = 1:3;
    c = r'
    ```

    ```python
    r = np.arange(1, 4)
    c = r.reshape(-1, 1)
    ```

    NumPy's `.T` does nothing on a 1-D array -- there's no row/column
    to swap yet. It only does something once the array is genuinely
    2-D.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Creating Matrices
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Creating a matrix is just a generalization of creating a vector:
    spaces or commas separate values within a row, semicolons start a
    new row.

    ```matlab
    mat = [4 3 1; 2 5 6]
    ```

    ```python
    mat = np.array([[4, 3, 1], [2, 5, 6]])
    ```

    MATLAB folds this straight into one literal; NumPy nests a
    separate list for each row.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Accessing Matrix Elements

    ```matlab
    mat = [2:4; 3:5];
    mat(2,3)    % 5
    ```

    ```python
    mat = np.array([[2, 3, 4], [3, 4, 5]])
    mat[1, 2]    # 5
    ```

    **Row first, then column -- same order in both languages.** Only
    the starting index shifts.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Accessing Matrix Subsets

    ```matlab
    mat(1:2, 2:3)
    ```

    ```python
    mat[0:2, 1:3]
    ```

    The same both-ends shift from "Extracting Subsets" applies to
    each dimension independently.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Modifying Vector and Matrix Elements
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Modifying Individual Elements

    ```matlab
    v = [10 20 30 40 50];
    v(3) = 99;

    mat = [1 2 3; 4 5 6; 7 8 9];
    mat(2,3) = 100;
    ```

    ```python
    v = np.array([10, 20, 30, 40, 50])
    v[2] = 99

    mat = np.array(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    )
    mat[1, 2] = 100
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Modifying Entire Rows or Columns

    A single colon by itself means "every element along this
    dimension" -- in both languages:

    ```matlab
    mat(2,:) = [40 50 60];
    mat(:,1) = [10; 20; 30];
    ```

    ```python
    mat[1, :] = [40, 50, 60]
    mat[:, 0] = [10, 20, 30]
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Modifying Submatrices

    ```matlab
    mat(2:3, 2:4) = [0 0 0; 0 0 0];
    mat(1:2, 2:3) = 0;    % scalar broadcasts
    ```

    ```python
    mat[1:3, 1:4] = [[0, 0, 0], [0, 0, 0]]
    mat[0:2, 1:3] = 0    # broadcasts here too
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Modifying with Vector Subscripts

    ```matlab
    v([1 3 5]) = [100 300 500];
    mat([1 3], [1 3]) = [10 30; 70 90];  % corners
    ```

    ```python
    v[[0, 2, 4]] = [100, 300, 500]
    mat[np.ix_([0, 2], [0, 2])] = [
        [10, 30], [70, 90]
    ]
    ```

    Selecting a row list *and* a column list at once needs `np.ix_`
    in NumPy -- plain `mat[[0,2], [0,2]]` picks just two single
    elements, `(0,0)` and `(2,2)`, not a 2×2 block.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Modifying Using Logical Indexing

    ```matlab
    v = [5 12 8 3 15 9];
    v(v > 10) = 10;

    mat(mat < 0) = 0;
    mat(mat >= 50 & mat <= 70) = 60;
    ```

    ```python
    v = np.array([5, 12, 8, 3, 15, 9])
    v[v > 10] = 10

    mat[mat < 0] = 0
    mat[(mat >= 50) & (mat <= 70)] = 60
    ```

    One of the rare places the syntax lines up almost exactly --
    `>`, `<`, `&`, `|` all mean the same thing, element by element, in
    both languages. The one catch: Python needs parentheses around
    each comparison before `&`/`|`, since `&` binds *tighter* than
    `>=`/`<=` there. MATLAB has no such precedence trap.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Special Matrix-Creating Functions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    | MATLAB | NumPy | Produces |
    |---|---|---|
    | `zeros(n)` / `zeros(m,n)` | `np.zeros((n,n))` / `np.zeros((m,n))` | all zeros |
    | `ones(n)` / `ones(m,n)` | `np.ones((n,n))` / `np.ones((m,n))` | all ones |
    | `eye(n)` | `np.eye(n)` | identity matrix |
    | `rand(m,n)` | `np.random.rand(m,n)` | uniform on (0, 1) |
    | `randn(m,n)` | `np.random.randn(m,n)` | standard normal |
    | `randi(imax,m,n)` | `np.random.randint(1, imax+1, size=(m,n))` | random integers 1..imax |

    **Watch `randi`:** same inclusive-endpoint rule as `range`/`:`
    from earlier -- MATLAB's `imax` is included, NumPy's `randint`
    high bound is excluded, so the NumPy call needs `imax + 1`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Concatenating Matrices
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Horizontal Concatenation

    ```matlab
    A = [1 2; 3 4];
    B = [5 6; 7 8];
    C = [A, B];        % or: horzcat(A, B)
    ```

    ```python
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    C = np.hstack([A, B])
    ```

    (`np.concatenate([A, B], axis=1)` is the equivalent of `horzcat`.)
    Both languages require the same number of rows in `A` and `B` --
    MATLAB errors on a dimension mismatch, NumPy raises a
    `ValueError`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Vertical Concatenation

    ```matlab
    C = [A; B];        % or: vertcat(A, B)
    ```

    ```python
    C = np.vstack([A, B])
    ```

    (`np.concatenate([A, B], axis=0)` is the equivalent of `vertcat`.)
    Same idea, rotated -- this time the column counts must match. A
    third dimension works the same way again: MATLAB's `cat(3,A,B)`
    is NumPy's `np.stack([A, B], axis=2)`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Expanding Matrices
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Assigning past a MATLAB matrix's current size **expands it
    automatically**, filling every new position with 0:

    ```matlab
    A = [1 2; 3 4];
    A(3,4) = 10;
    A =
        1  2  0   0
        3  4  0   0
        0  0  0  10
    ```

    NumPy does **not** do this -- `A[2,3] = 10` on a 2×4 array raises
    `IndexError`. A NumPy array's shape is fixed once created; growing
    it means building a new, bigger array and copying the old values
    into it, not assigning past the edge.

    For loops that repeatedly grow a matrix, **preallocate** instead,
    in both languages:

    ```matlab
    results = zeros(1, 1000);
    for k = 1:1000
        results(k) = k^2;
    end
    ```

    ```python
    results = np.zeros(1000)
    for k in range(1000):
        results[k] = (k + 1) ** 2
    ```

    (In NumPy the loop is usually skippable entirely --
    `np.arange(1, 1001) ** 2` vectorizes it -- but the preallocate
    habit still matters anywhere you can't avoid the loop.)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Reshaping Arrays
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Basic Syntax

    ```matlab
    A = 1:12;
    B = reshape(A, [3, 4])
    B =
        1  4  7  10
        2  5  8  11
        3  6  9  12
    ```

    ```python
    A = np.arange(1, 13)
    B = A.reshape(3, 4, order='F')
    # array([[ 1,  4,  7, 10],
    #        [ 2,  5,  8, 11],
    #        [ 3,  6,  9, 12]])
    ```

    **Watch the fill order:** MATLAB's `reshape` always fills
    column-by-column -- its only order. NumPy's `.reshape()` defaults
    to filling row-by-row instead:

    ```python
    A.reshape(3, 4)   # order='C' default
    # array([[ 1,  2,  3,  4],
    #        [ 5,  6,  7,  8],
    #        [ 9, 10, 11, 12]])
    ```

    Same call, different layout -- unless you explicitly pass
    `order='F'` to match MATLAB.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Automatic Dimension Calculation

    ```matlab
    B = reshape(A, 2, [])   % 6 columns
    ```

    ```python
    B = A.reshape(2, -1, order='F')   # 6 columns
    ```

    `[]` in MATLAB and `-1` in NumPy mean the same thing: "figure out
    this dimension from the others."
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Key Takeaways
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - MATLAB stores everything as a matrix -- scalars and vectors are
      just special cases
    - Indices start at **1**, not 0
    - `:` creates sequences and slices -- always inclusive on both ends
    - `;` separates rows; `,` or a space separates columns
    - `'` transposes
    - `[]` both creates matrices and concatenates them
    - `zeros`, `ones`, `eye`, `rand`, `randn`, `randi` build special
      matrices
    - Logical indexing (`mat(mat > x) = y`) modifies conditionally --
      and looks almost identical to NumPy
    - `reshape` preserves elements but fills **column-wise** by
      default, the opposite of NumPy's default
    - Preallocate before a loop that grows a matrix
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## MATLAB Documentation: Your Best Resource
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - **Creating matrices**: `zeros`, `ones`, `eye`, `rand`, `randn`,
      `randi`, `linspace`
    - **Reshaping & concatenation**: `reshape`, `horzcat`, `vertcat`,
      `cat`
    - **Indexing**: logical indexing, the `end` keyword, and the
      colon operator all live under "Array Indexing" in the docs
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## This Week's Homework: HW8
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **HW8: Plotting in Python and MATLAB, Vectors and Matrices** --
    due **Tuesday, November 24**. Problems 5 and 6 -- 30 of the
    MATLAB half's 50 points -- are today's material.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Problem 5 picks up directly from today

    It gives you a flat row of sensor readings and asks you to
    `reshape` it into a 3×4 grid (watch the column-wise fill order
    from "Reshaping Arrays" above), then predict four indexing
    expressions before you run them, fix one bad reading, pull out a
    2×2 block, cap values with logical indexing *without* touching
    the original, and concatenate on a new column.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### A few tips, not answers

    - Predict each indexing expression on paper before running it --
      that's the point of "predict-then-verify," not a step to skip
    - "Without modifying the original" means logical indexing on a
      **copy** -- `capped = sensors; capped(capped > 28) = 28;`, not
      `sensors(sensors > 28) = 28;`
    - `end` still works inside a 2-D subscript, same as it does for a
      plain vector
    - Problem 6 is logical indexing applied to a time signal -- no
      loop needed, same `signal(signal < 0) = 0` pattern as today's
      "Logical Indexing" slide

    📋 Full assignment: [HW8](https://BU-EK125.github.io/EK125/homework/HW8.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Looking Ahead to Class 24
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Next class builds on today's vectors and matrices with the actual
    math MATLAB does with them -- vector and matrix operations,
    arithmetic, and multiplication -- the next layer up from just
    creating and indexing the data structures.
    """)
    return


if __name__ == "__main__":
    app.run()
