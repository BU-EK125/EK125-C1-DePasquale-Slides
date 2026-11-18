import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class22.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # From Python to MATLAB: Syntax and Plotting

    ### Class 22

    📖 [Full reading: Class 22](https://BU-EK125.github.io/EK125/class/Class22.html)
    📋 [Group Practice: Class 22](https://BU-EK125.github.io/EK125/gpps/Class22_GPP.html)

    *Curious how these slides work? They're built with
    [marimo](https://marimo.io), a Python notebook that runs live,
    right in your browser.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## What Will Feel Familiar: PyCharm and MATLAB
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Both are full IDEs with the same basic layout:

    | | PyCharm | MATLAB |
    |---|---|---|
    | Editor | yes | yes |
    | File browser | project panel | Current Folder |
    | Output / run | run panel | Command Window |
    | Run button | green ▶ | ▶ Run |
    | Running code | New Python File → run panel | New Script → Command Window |

    Same workflow end to end: new file, write code, run it, see the
    output, organize files in the browser panel.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Key Differences to Note

    - `.py` becomes `.m`
    - MATLAB adds a **Workspace** panel -- every current variable,
      its size, and its value, always visible, no `print()` needed
    - The Command Window is more prominent and interactive -- closer
      to a Colab cell than PyCharm's run panel
    - Huge numbers of built-in functions (`sin`, `cos`, `mean`,
      `plot`, ...) -- no imports required

    **The bottom line:** if you can navigate PyCharm, you can
    navigate MATLAB.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Installing MATLAB at Boston University
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    BU's site license covers MATLAB, Simulink, and 49 add-on
    toolboxes -- free to install on your own machine.

    1. Create a MathWorks account using your **BU email**
    2. Download via the MathWorks BU Portal, choosing the
       **"Individual Academic -- Total Headcount"** license
    3. Run the installer and install the toolboxes you need
    4. Activate automatically over the Internet, signed in with
       your MathWorks account

    The license renews annually (typically every July). Installation
    issues go to BU IT Help (ithelp@bu.edu), same as any other
    campus software problem.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Key Syntax Differences
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Most of what you already know about *how to think* carries over
    directly -- variables, loops, conditionals, functions all work
    the same way. What changes is the syntax. Six differences you'll
    hit right away:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Semicolons and Output

    Python only displays something when you call `print()`. MATLAB
    displays the result of **any** statement that doesn't end in a
    semicolon -- handy for quickly checking a value, but it floods
    the Command Window if you forget the `;` inside a loop. Use
    `disp()` to print explicitly, with or without a semicolon.

    ```python
    x = 5
    print(x)      # 5
    ```

    ```matlab
    x = 5          % displays: x = 5
    x = 5;         % silent
    disp(x)        % 5, either way
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Comments

    ```python
    # this is a comment
    ```

    ```matlab
    % this is a comment
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Indexing

    Python is **0-based** with square brackets; `-1` is the last
    element. MATLAB is **1-based** with parentheses; `end` is the
    last element.

    ```python
    arr = [10, 20, 30]
    arr[0]      # 10
    arr[-1]     # 30
    ```

    ```matlab
    arr = [10, 20, 30];
    arr(1)      % 10
    arr(end)    % 30
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Arrays vs. Vectors and Matrices

    MATLAB reuses the same square-bracket syntax for row vectors,
    column vectors, *and* matrices -- a comma separates values
    within a row, a semicolon starts a new row.

    ```python
    import numpy as np
    row = np.array([1, 2, 3, 4])
    ```

    ```matlab
    row = [1, 2, 3, 4];         % 1x4 row vector
    col = [1; 2; 3; 4];         % 4x1 column vector
    mat = [1, 2, 3; 4, 5, 6];   % 2x3 matrix
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Ranges

    ```python
    list(range(0, 10))      # 0..9
    list(range(0, 10, 2))   # 0, 2, 4, 6, 8
    np.linspace(0, 10, 5)   # 5 evenly spaced points
    ```

    ```matlab
    0:9          % 0..9
    0:2:9        % 0, 2, 4, 6, 8 (start:step:end)
    linspace(0, 10, 5)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Logical Operators

    Scalar comparisons use short-circuit operators; array/elementwise
    comparisons use single-character operators -- NumPy draws the
    exact same line between Python's `and`/`or` and `&`/`|`.

    ```python
    True and False     # scalar
    arr1 & arr2        # elementwise (NumPy arrays)
    ```

    ```matlab
    true && false       % scalar, short-circuit
    arr1 & arr2         % elementwise
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Plotting in MATLAB
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Good news: `matplotlib` was explicitly modeled on MATLAB's own
    plotting commands. Almost every plot you built last class has a
    near-identical MATLAB counterpart -- often with *less* code,
    since MATLAB needs no import and no `plt.show()`.
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import numpy as np

    return np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### A Basic Line Plot

    ```python
    import matplotlib.pyplot as plt
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plt.plot(x, y)
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title('My Plot')
    plt.show()
    ```

    ```matlab
    x = [1, 2, 3, 4, 5];
    y = [1, 4, 9, 16, 25];
    plot(x, y)
    xlabel('X values')
    ylabel('Y values')
    title('My Plot')
    ```

    No import, no `show()` -- MATLAB displays the Figure window the
    moment `plot()` runs.
    """)
    return


@app.cell(hide_code=True)
def _(plt):
    _x = [1, 2, 3, 4, 5]
    _y = [1, 4, 9, 16, 25]

    _fig, _ax = plt.subplots()
    _ax.plot(_x, _y)
    _ax.set_xlabel("X values")
    _ax.set_ylabel("Y values")
    _ax.set_title("My Plot")
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Customizing the Line

    ```matlab
    plot(x, y, 'r--', 'LineWidth', 2);
    grid on;
    ```

    `'r--'` combines a **color** (`r`) and a **line style** (`--`)
    in one short string; `'LineWidth'` is a name-value pair, the
    same idea as matplotlib's `color=`/`linewidth=` keywords.
    """)
    return


@app.cell(hide_code=True)
def _(np, plt):
    _x = np.linspace(0, 2 * np.pi, 100)
    _y = np.sin(_x)

    _fig, _ax = plt.subplots()
    _ax.plot(_x, _y, "r--", linewidth=2)
    _ax.grid(True)
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Multiple Lines and a Legend

    ```python
    plt.plot(x, y1, label='Line 1')
    plt.plot(x, y2, label='Line 2')
    plt.legend()
    ```

    ```matlab
    plot(x, y1, x, y2);
    legend('sin(x)', 'cos(x)');
    ```

    (Equivalently: `hold on; plot(x, y1); plot(x, y2); hold off;` --
    the same idea as `ax.plot()` called twice on one Axes.)
    """)
    return


@app.cell(hide_code=True)
def _(np, plt):
    _x = np.linspace(0, 2 * np.pi, 100)
    _y1 = np.sin(_x)
    _y2 = np.cos(_x)

    _fig, _ax = plt.subplots()
    _ax.plot(_x, _y1, label="sin(x)")
    _ax.plot(_x, _y2, label="cos(x)")
    _ax.legend()
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Subplots

    ```python
    plt.subplot(2, 1, 1)   # 2 rows, 1 column, plot 1
    plt.plot(x, y1)

    plt.subplot(2, 1, 2)   # 2 rows, 1 column, plot 2
    plt.plot(x, y2)
    ```

    ```matlab
    subplot(2, 1, 1);
    plot(x, y1);
    title('Top');

    subplot(2, 1, 2);
    plot(x, y2);
    title('Bottom');
    ```

    Watch the naming: MATLAB's `subplot(rows, cols, index)` picks one
    panel at a time by index, closer to Python's older `plt.subplot()`
    than to the `fig, ax = plt.subplots()` pattern from last class.
    """)
    return


@app.cell(hide_code=True)
def _(np, plt):
    _x = np.linspace(0, 2 * np.pi, 100)
    _y1 = np.sin(_x)
    _y2 = np.cos(_x)

    _fig, (_ax1, _ax2) = plt.subplots(2, 1)
    _ax1.plot(_x, _y1)
    _ax1.set_title("Top")
    _ax2.plot(_x, _y2)
    _ax2.set_title("Bottom")
    _fig.tight_layout()
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Scatter, Bar, and Histogram

    ```matlab
    % x, y = randn(100,1)
    scatter(x, y);

    categories = 1:5;
    values = [23, 45, 31, 52, 38];
    bar(categories, values);

    histogram(data, 30);   % 30 bins
    ```
    """)
    return


@app.cell(hide_code=True)
def _(np, plt):
    np.random.seed(42)
    _scatter_x = np.random.randn(100)
    _scatter_y = np.random.randn(100)
    _categories = [1, 2, 3, 4, 5]
    _values = [23, 45, 31, 52, 38]
    _hist_data = np.random.randn(1000)

    _fig, (_ax1, _ax2, _ax3) = plt.subplots(1, 3, figsize=(10, 3.2))
    _ax1.scatter(_scatter_x, _scatter_y)
    _ax1.set_title("scatter")
    _ax2.bar(_categories, _values)
    _ax2.set_title("bar")
    _ax3.hist(_hist_data, bins=30)
    _ax3.set_title("histogram")
    _fig.tight_layout()
    _fig
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
    Nobody memorizes every option. The habit that matters is knowing
    *where to look* -- each MATLAB function's documentation page
    (`mathworks.com/help/matlab/ref/...`) lists every variant:

    - **Plot types**: `plot`, `scatter` (marker size/color, `'filled'`),
      `bar` (`barh`, grouped/stacked, `'FaceColor'`), `histogram`
      (bin count, bin edges, `'Normalization'`)
    - **Colors and colormaps**: short codes, RGB triplets, hex
      (`'#FF5733'`) -- MATLAB only *names* eight colors, so use RGB
      or hex for anything else; `colormap('parula')`, `'jet'`, `'hot'`
    - **Axes and labels**: `xlim`, `ylim`, `grid on/off`,
      `axis equal`, `xticks`, `xticklabels` (for categorical data),
      `xtickangle(45)` (rotate long labels), `legend('Location', 'best')`
    - **Saving**: `saveas(gcf, 'myplot.png')` -- `gcf` means
      *get current figure*; also supports `.pdf`, `.fig`, `.eps`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Try It Yourself
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```matlab
    x = linspace(0, 4*pi, 100);
    y1 = sin(x);
    y2 = sin(x) .* exp(-x/10);

    figure;
    subplot(2,1,1);
    plot(x, y1, 'b-', 'LineWidth', 1.5);
    title('Simple Sine Wave');
    xlabel('x'); ylabel('sin(x)');
    grid on;

    subplot(2,1,2);
    plot(x, y2, 'r-', 'LineWidth', 1.5);
    title('Damped Sine Wave');
    xlabel('x');
    ylabel('sin(x) * exp(-x/10)');
    grid on;
    ```

    `.*` is MATLAB's elementwise multiply -- the direct counterpart
    to NumPy's `*` on two arrays (plain `*` in MATLAB means matrix
    multiplication instead, which is why the dot matters).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    decay_slider = mo.ui.slider(
        3, 30, value=10, step=1, label="Decay constant"
    )
    decay_slider
    return (decay_slider,)


@app.cell(hide_code=True)
def _(decay_slider, np, plt):
    _decay = decay_slider.value
    _x = np.linspace(0, 4 * np.pi, 100)
    _y1 = np.sin(_x)
    _y2 = np.sin(_x) * np.exp(-_x / _decay)

    _fig, (_ax1, _ax2) = plt.subplots(2, 1)
    _ax1.plot(_x, _y1, "b-", linewidth=1.5)
    _ax1.set_title("Simple Sine Wave")
    _ax1.set_xlabel("x")
    _ax1.set_ylabel("sin(x)")
    _ax1.grid(True)

    _ax2.plot(_x, _y2, "r-", linewidth=1.5)
    _ax2.set_title(f"Damped Sine Wave (decay constant = {_decay})")
    _ax2.set_xlabel("x")
    _ax2.set_ylabel("sin(x) * exp(-x/decay)")
    _ax2.grid(True)

    _fig.tight_layout()
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Drag the slider -- a smaller decay constant damps the wave out
    faster, exactly the same relationship `exp(-x/decay)` has in
    Python. MATLAB has no live slider on a script, but the plot
    itself is pixel-for-pixel the same call.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Quick Reference Table
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    | | Python | MATLAB |
    |---|---|---|
    | Suppress output | automatic | add `;` |
    | Comment | `#` | `%` |
    | First index | `0` | `1` |
    | Last index | `-1` | `end` |
    | Indexing | `arr[i]` | `arr(i)` |
    | Range | `range(0, 10)` | `0:9` |
    | Plot | `plt.plot(x, y)` | `plot(x, y)` |
    | Show plot | `plt.show()` | automatic |
    | Elementwise multiply | `arr1 * arr2` (NumPy) | `arr1 .* arr2` |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Install MATLAB Today
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - Install MATLAB today -- before this lecture or after, whichever
      fits your schedule, as long as it's done
    - Once it's installed, open it and create `x = 1:10` in the
      Command Window
    - Plot it: `plot(x, x.^2)`
    - Keep the 1-based vs. 0-based indexing difference fresh --
      it's the single easiest Python habit to bring into MATLAB by
      mistake
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
    due **Tuesday, November 24**, covering Classes 21, 22, *and* 23
    together. Two halves, 50 points each: a Python half (Problems
    1-3, from last class) and a MATLAB half (Problems 4-6, starting
    with today's material).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Problem 4 picks up right where today left off

    It asks you to recreate Problem 1's Python stress-strain plot --
    same two metals, same look -- in MATLAB, using `hold on` to put
    both lines on one set of axes (see "Multiple Lines and a Legend"
    above). Then it asks you to list three Python/MATLAB differences
    you noticed along the way -- today's slides are full of them.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### A few tips, not answers

    - End every line with `;` unless the problem tells you to
      display a result -- the same rule as "Semicolons and Output"
    - Two separate `plot()` calls bracketed by `hold on` / `hold off`
      is simpler than trying to pass both lines to one `plot()` call
    - Your MATLAB elastic-modulus numbers must match your Python
      numbers from Problem 1 -- a built-in self-check
    - Save each figure with `saveas(gcf, 'filename.png')` -- see
      "Saving Figures" under "MATLAB Documentation" above
    - Problems 5 and 6 lean into matrices and logical indexing --
      that's genuinely Class 23 material, not this lecture, so don't
      worry if those feel like a step up

    📋 Full assignment: [HW8](https://BU-EK125.github.io/EK125/homework/HW8.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Looking Ahead to Class 23
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Next class moves past plotting syntax into MATLAB's real
    strength: building and manipulating vectors and matrices
    directly, the data structures everything in MATLAB -- including
    every plot on these slides -- is built from.
    """)
    return


if __name__ == "__main__":
    app.run()
