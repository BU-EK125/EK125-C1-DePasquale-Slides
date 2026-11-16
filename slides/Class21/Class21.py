import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class21.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Visualizing Data and Plotting in Python

    ### Class 21

    📖 [Full reading: Class 21](https://BU-EK125.github.io/EK125/class/Class21.html)
    📋 [Group Practice: Class 21](https://BU-EK125.github.io/EK125/gpps/Class21_GPP.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Why Visualize Data?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Raw numbers only tell part of the story. These two datasets have
    the exact same average, 28:

    - Dataset A: `[23, 25, 27, 29, 31, 33]`
    - Dataset B: `[23, 23, 23, 33, 33, 33]`
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import numpy as np

    return np, plt


@app.cell(hide_code=True)
def _(plt):
    _dataset_a = [23, 25, 27, 29, 31, 33]
    _dataset_b = [23, 23, 23, 33, 33, 33]
    _x = list(range(1, 7))

    _fig, (_ax1, _ax2) = plt.subplots(1, 2, figsize=(8, 3.2))
    _ax1.plot(_x, _dataset_a, "o-", color="steelblue")
    _ax1.set_title("Dataset A")
    _ax1.set_ylim(20, 36)
    _ax1.grid(True)

    _ax2.plot(_x, _dataset_b, "o-", color="darkorange")
    _ax2.set_title("Dataset B")
    _ax2.set_ylim(20, 36)
    _ax2.grid(True)

    _fig.suptitle("Same average (28) -- very different stories")
    _fig.tight_layout()
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Visualization makes patterns, trends, and outliers obvious in a
    way a table of numbers never does -- especially when you have too
    much data to read by eye, or want to compare several scenarios
    at once.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Introduction to matplotlib
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `matplotlib` is Python's most widely-used plotting library. The
    convention -- everywhere, not just this course -- is to import its
    `pyplot` module as `plt`:

    ```python
    import matplotlib.pyplot as plt
    ```

    In PyCharm, `matplotlib` must be installed in your project once
    before you can import it (Python Packages tool window, or
    `pip install matplotlib` in the Terminal) -- unlike Colab, where
    it's already there. Same steps as installing NumPy back in
    [Class 11](https://BU-EK125.github.io/EK125/class/Class11.html),
    just a different package name.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Your First Plot
    """)
    return


@app.cell
def _(plt):
    _x_values = [1, 2, 3, 4, 5]
    _y_values = [2, 4, 6, 8, 10]

    _fig, _ax = plt.subplots()
    _ax.plot(_x_values, _y_values)
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Reading this code

    - `plt.subplots()` with no arguments hands back two things at
      once: a **Figure** (`fig`) -- the whole blank page -- and one
      **Axes** (`ax`) -- one actual plotting area drawn on that page
    - Everything about the plot itself -- `.plot()`, and later
      `.set_xlabel()`, `.legend()`, `.grid()` -- is called on `ax`,
      not `fig`
    - The bare `fig` on its own last line is what displays the
      figure **on this slide** -- notebooks (this deck, and Colab)
      auto-display whatever a cell's last bare expression evaluates
      to, the same way a lone `2 + 2` would just print `4`
    - **In a PyCharm script, that trick does nothing.** There's no
      notebook display hook, so a bare `fig` silently does nothing at
      all. That's why every GPP and the reading itself always end
      with `plt.show()` -- call that explicitly to display every
      currently open figure
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `plt.plot()` connects the points `(1,2)`, `(2,4)`, ... `(5,10)` with
    straight lines. It works -- but a reader has no idea what either
    axis even means.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Labels, Units, and a Title
    """)
    return


@app.cell
def _(plt):
    _x_values = [1, 2, 3, 4, 5]
    _y_values = [2, 4, 6, 8, 10]

    _fig, _ax = plt.subplots()
    _ax.plot(_x_values, _y_values)
    _ax.set_xlabel("Time (seconds)")
    _ax.set_ylabel("Distance (meters)")
    _ax.set_title("Object Position Over Time")
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Critical principle

    Every axis needs a label **with units**. Every plot needs a title
    that describes what is being shown. A figure without units is
    incomplete the same way a number without units is incomplete.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Customizing Appearance
    """)
    return


@app.cell
def _(plt):
    _time = [0, 1, 2, 3, 4]
    _temperature = [20, 22, 21, 23, 25]

    _fig, _ax = plt.subplots()
    _ax.plot(_time, _temperature, color="red", linestyle="--",
             linewidth=2, marker="o")
    _ax.set_xlabel("Time (hours)")
    _ax.set_ylabel("Temperature (°C)")
    _ax.set_title("Temperature Variation")
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - **Colors**: `'red'`, `'blue'`, `'green'`, `'black'`, or a hex
      code like `'#FF5733'`
    - **Line styles**: `'-'` solid, `'--'` dashed, `':'` dotted,
      `'-.'` dash-dot
    - **Markers**: `'o'` circle, `'s'` square, `'^'` triangle,
      `'*'` star
    """)
    return


@app.cell
def _(plt):
    _time = [0, 1, 2, 3, 4]
    _temperature = [20, 22, 21, 23, 25]

    _fig, _ax = plt.subplots()
    _ax.plot(_time, _temperature, color="red", linestyle="--",
             linewidth=2, marker="o")
    _ax.set_xlabel("Time (hours)")
    _ax.set_ylabel("Temperature (°C)")
    _ax.set_title("Temperature Variation")
    _ax.grid(True)
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `plt.grid(True)` helps a reader extract quantitative values by eye,
    not just the overall shape.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Scatter Plots
    """)
    return


@app.cell
def _(plt):
    _heights = [160, 165, 170, 175, 180, 185]
    _weights = [60, 65, 70, 75, 80, 85]

    _fig, _ax = plt.subplots()
    _ax.scatter(_heights, _weights, color="blue", s=100)
    _ax.set_xlabel("Height (cm)")
    _ax.set_ylabel("Weight (kg)")
    _ax.set_title("Height vs. Weight")
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `s` controls marker size -- it can carry information too, not just
    looks. Here it stands in for a third variable, shoe size:
    """)
    return


@app.cell
def _(mo):
    size_scale_slider = mo.ui.slider(5, 60, value=20, step=5,
                                      label="Size scale (points per shoe size)")
    size_scale_slider
    return (size_scale_slider,)


@app.cell
def _(plt, size_scale_slider):
    _heights = [160, 165, 170, 175, 180, 185]
    _weights = [60, 65, 70, 75, 80, 85]
    _shoe_size = [7, 8, 8, 9, 10, 11]
    _scale = size_scale_slider.value
    _sizes = [s * _scale / 8 for s in _shoe_size]

    _fig, _ax = plt.subplots(figsize=(6, 3.8))
    _ax.scatter(_heights, _weights, color="blue", s=_sizes, alpha=0.6)
    _ax.set_xlabel("Height (cm)")
    _ax.set_ylabel("Weight (kg)")
    _ax.set_title("Height vs. Weight (marker size = shoe size)")
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Use a scatter plot for the relationship between two variables when
    each point is a separate, independent measurement -- connecting
    them with a line would imply an order that isn't really there.
    Marker size (`s=`) can encode a third variable directly on the
    same plot, the way it did for "hours of sleep" in the reading's
    own bubble-size example.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Bar Charts
    """)
    return


@app.cell
def _(plt):
    _metals = ["Aluminum", "Titanium", "Steel", "Copper", "Lead"]
    _density_g_per_cm3 = [2.70, 4.51, 7.85, 8.96, 11.34]

    _fig, _ax = plt.subplots()
    _ax.bar(_metals, _density_g_per_cm3, color="gray")
    _ax.axhline(y=5.0, color="red", linestyle="--",
                label="Light/heavy metal cutoff")
    _ax.set_xlabel("Metal")
    _ax.set_ylabel("Density (g/cm$^3$)")
    _ax.set_title("Density of Common Engineering Metals")
    _ax.legend()
    _ax.grid(axis="y")
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Drag the cutoff itself and watch which metals cross the line:
    """)
    return


@app.cell
def _(mo):
    cutoff_slider = mo.ui.slider(1.0, 12.0, value=5.0, step=0.5,
                                  label="Light/heavy cutoff (g/cm3)")
    cutoff_slider
    return (cutoff_slider,)


@app.cell
def _(cutoff_slider, plt):
    _metals = ["Aluminum", "Titanium", "Steel", "Copper", "Lead"]
    _density_g_per_cm3 = [2.70, 4.51, 7.85, 8.96, 11.34]
    _cutoff = cutoff_slider.value
    _light = [m for m, d in zip(_metals, _density_g_per_cm3) if d < _cutoff]

    _fig, _ax = plt.subplots(figsize=(6, 3.5))
    _ax.bar(_metals, _density_g_per_cm3, color="gray")
    _ax.axhline(y=_cutoff, color="red", linestyle="--",
                label=f"Cutoff: {_cutoff:g} g/cm3")
    _ax.set_ylabel("Density (g/cm$^3$)")
    _ax.set_title(f"Light metals: {', '.join(_light) if _light else '(none)'}")
    _ax.legend()
    _ax.grid(axis="y")
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Bar charts compare one number across categories. `plt.axhline()`
    draws a reference line across the whole plot -- useful for a
    cutoff or a target value. Drag it low enough and every metal is
    "heavy"; drag it above 11.34 and every metal is "light" -- the
    cutoff is a choice, not a fact about the data.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Histograms
    """)
    return


@app.cell
def _(plt):
    _test_scores = [78, 82, 85, 88, 90, 92, 85, 87, 83, 89,
                     91, 86, 84, 88, 90, 87, 85, 82, 79, 94]

    _fig, _ax = plt.subplots()
    _ax.hist(_test_scores, bins=5, color="purple", edgecolor="black")
    _ax.set_xlabel("Score Range")
    _ax.set_ylabel("Number of Students")
    _ax.set_title("Distribution of Test Scores")
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    A histogram shows the **distribution** of one variable -- how many
    values fall into each numeric range. That's different from a bar
    chart, which compares a number across named categories. Mixing
    these two up is a common, and testable, mistake.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## How Many Bins Is Right?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    The `bins` parameter controls how many ranges the data gets divided
    into -- and it changes what story the histogram tells. Try it on
    30 resistors, all labeled 100 ohm:
    """)
    return


@app.cell
def _(mo):
    bins_slider = mo.ui.slider(3, 20, value=6, step=1, label="Number of bins")
    bins_slider
    return (bins_slider,)


@app.cell
def _(bins_slider, plt):
    _resistance_ohm = [99.2, 100.5, 101.1, 98.7, 100.0, 99.8, 100.9,
                        101.6, 99.5, 100.2, 98.9, 100.4, 99.9, 100.7,
                        101.3, 99.1, 100.1, 100.6, 99.4, 100.3, 102.0,
                        98.4, 100.8, 99.7, 100.0, 101.0, 99.6, 100.2,
                        99.3, 100.5]
    _bins = bins_slider.value

    _fig, _ax = plt.subplots(figsize=(6, 3.5))
    _ax.hist(_resistance_ohm, bins=_bins, color="teal", edgecolor="black")
    _ax.set_xlabel("Resistance (ohm)")
    _ax.set_ylabel("Number of resistors")
    _ax.set_title(f"{_bins} Bins")
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Drag the slider from 3 up past 15. Too **few** bins lumps
    everything together and hides the shape; too **many** bins, with
    only 30 data points, leaves most bins holding 0-2 resistors and
    the plot looks jagged and noisy. Somewhere in the middle shows the
    real shape -- one peak near 100 ohm.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Multiple Lines and a Legend
    """)
    return


@app.cell
def _(plt):
    _time = [0, 1, 2, 3, 4, 5]
    _object1 = [0, 2, 4, 6, 8, 10]
    _object2 = [0, 3, 6, 9, 12, 15]

    _fig, _ax = plt.subplots()
    _ax.plot(_time, _object1, label="Object 1", color="blue", marker="o")
    _ax.plot(_time, _object2, label="Object 2", color="red", marker="s")
    _ax.set_xlabel("Time (seconds)")
    _ax.set_ylabel("Position (meters)")
    _ax.set_title("Position of Two Objects Over Time")
    _ax.legend()
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Calling `plt.plot()` twice before `plt.show()` draws both lines on
    the same axes. `legend()` only shows a line if that line's
    `plot()` call had a `label=` -- no label, no legend entry.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## A Ball Thrown Straight Up
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    A ball thrown straight up at speed `v0` has height
    `height = v0 * t - 4.9 * t**2` (height in m, `t` in s). Drag the
    launch speed and watch the whole curve change:
    """)
    return


@app.cell
def _(mo):
    speed_slider = mo.ui.slider(5, 25, value=15, step=1,
                                 label="Launch speed (m/s)")
    speed_slider
    return (speed_slider,)


@app.cell
def _(np, plt, speed_slider):
    _v0 = speed_slider.value
    _t = np.linspace(0, 2 * _v0 / 9.8, 100)
    _height = _v0 * _t - 4.9 * _t**2

    _fig, _ax = plt.subplots(figsize=(6, 3.8))
    _ax.plot(_t, _height, color="blue", linewidth=2)
    _ax.set_xlabel("Time (s)")
    _ax.set_ylabel("Height (m)")
    _ax.set_title(f"Launch speed: {_v0} m/s  (max height: {max(_height):.1f} m)")
    _ax.grid(True)
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `np.linspace` builds the whole array of time values at once, and
    NumPy applies the height formula to every one of them in a single
    line -- no loop needed. That's the pattern behind every smooth
    curve in this reading.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Subplots: Several Plots, One Figure
    """)
    return


@app.cell
def _(plt):
    _time = [0, 1, 2, 3, 4, 5]
    _position = [0, 2, 4, 6, 8, 10]
    _velocity = [2, 2, 2, 2, 2, 2]

    _fig = plt.figure(figsize=(8, 3.2))

    _ax1 = plt.subplot(1, 2, 1)
    _ax1.plot(_time, _position, "b-o")
    _ax1.set_xlabel("Time (s)")
    _ax1.set_ylabel("Position (m)")
    _ax1.set_title("Position vs. Time")

    _ax2 = plt.subplot(1, 2, 2)
    _ax2.plot(_time, _velocity, "r-s")
    _ax2.set_xlabel("Time (s)")
    _ax2.set_ylabel("Velocity (m/s)")
    _ax2.set_title("Velocity vs. Time")

    plt.tight_layout()
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `subplot(rows, columns, plotNumber)` -- and numbering **starts at
    1**, not 0. `subplot(1, 2, 1)` is a 1-row, 2-column layout,
    selecting the first panel. Set each panel's labels right after
    selecting it; set them before the matching `subplot()` call and
    they land on the *previous* panel instead.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Saving Figures
    """)
    return


@app.cell
def _(plt):
    _x_values = [1, 2, 3, 4, 5]
    _y_values = [2, 4, 6, 8, 10]

    _fig, _ax = plt.subplots()
    _ax.plot(_x_values, _y_values)
    _ax.set_xlabel("X axis")
    _ax.set_ylabel("Y axis")
    _ax.set_title("My Plot")
    _fig.savefig("myPlot.png", dpi=300, bbox_inches="tight")
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `savefig(..., dpi=300, bbox_inches='tight')` -- `dpi=300` is a good
    resolution for a report or a submitted figure; `bbox_inches='tight'`
    trims the excess white space around it. Call `savefig()` **before**
    `plt.show()`, since `show()` can clear the figure afterward.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Smooth Curves With NumPy
    """)
    return


@app.cell
def _(np, plt):
    _x_values = np.linspace(0, 10, 100)
    _y_values = np.sin(_x_values)

    _fig, _ax = plt.subplots()
    _ax.plot(_x_values, _y_values)
    _ax.set_xlabel("x")
    _ax.set_ylabel("sin(x)")
    _ax.set_title("Sine Function")
    _ax.grid(True)
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    How few points does it take before "smooth" breaks down?
    """)
    return


@app.cell
def _(mo):
    points_slider = mo.ui.slider(3, 100, value=100, step=1,
                                  label="Number of points")
    points_slider
    return (points_slider,)


@app.cell
def _(np, plt, points_slider):
    _n = points_slider.value
    _x_values = np.linspace(0, 10, _n)
    _y_values = np.sin(_x_values)

    _fig, _ax = plt.subplots(figsize=(6, 3.8))
    _ax.plot(_x_values, _y_values, marker="o" if _n <= 30 else None)
    _ax.set_xlabel("x")
    _ax.set_ylabel("sin(x)")
    _ax.set_title(f"Sine Function ({_n} points)")
    _ax.grid(True)
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    100 points, not just a handful, is what makes this curve look
    smooth. Drag down toward 3-5 points and `matplotlib` still
    connects them with straight lines -- the curve doesn't get wrong,
    it just stops looking like a sine wave. `matplotlib` plots NumPy
    arrays exactly as happily as it plots plain lists.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Radar Charts
    """)
    return


@app.cell
def _(np, plt):
    _categories = ["Math", "Physics", "Programming", "Writing", "Communication"]
    _values = [85, 90, 78, 82, 88]
    _num_vars = len(_categories)
    _angles = np.linspace(0, 2 * np.pi, _num_vars, endpoint=False).tolist()

    _values_closed = _values + _values[:1]
    _angles_closed = _angles + _angles[:1]

    _fig, _ax = plt.subplots(figsize=(4.5, 4.5), subplot_kw=dict(projection="polar"))
    _ax.plot(_angles_closed, _values_closed, "o-", linewidth=2, color="blue")
    _ax.fill(_angles_closed, _values_closed, alpha=0.25, color="blue")
    _ax.set_xticks(_angles)
    _ax.set_xticklabels(_categories)
    _ax.set_ylim(0, 100)
    _ax.set_title("Student Skills Assessment", pad=20)
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Radar (spider) charts compare several variables for one subject on
    the same scale -- they work best with 3-8 variables. The GPP's
    bonus problem asks you to put *two* designs on the same radar
    chart, with a legend, to compare them directly.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Working With Pandas DataFrames
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `pandas` is Python's main library for tabular data -- the kind
    you'd see in a spreadsheet, with named columns and rows. Its core
    object is the **DataFrame**. The convention is to import it as
    `pd`:

    ```python
    import pandas as pd

    data = {"Month": ["Jan", "Feb", "Mar"],
            "Sales": [150, 200, 175]}
    df = pd.DataFrame(data)
    ```

    Each dictionary key becomes a column name, and each list becomes
    that column's values -- `df["Sales"]` pulls out a column exactly
    the way a plain list would.
    """)
    return


@app.cell
def _():
    import pandas as pd

    return (pd,)


@app.cell
def _(pd, plt):
    _data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Sales": [150, 200, 175, 220, 240, 260],
        "Expenses": [100, 120, 110, 130, 140, 150],
    }
    _df = pd.DataFrame(_data)

    _fig, _ax = plt.subplots()
    _ax.plot(_df["Month"], _df["Sales"], marker="o", label="Sales")
    _ax.plot(_df["Month"], _df["Expenses"], marker="s", label="Expenses")
    _ax.set_xlabel("Month")
    _ax.set_ylabel("Amount ($1000s)")
    _ax.set_title("Monthly Sales and Expenses")
    _ax.legend()
    _ax.grid(True)
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `df['columnName']` pulls out a column exactly like any list, so
    everything you already know about `plt.plot()` carries over
    directly -- DataFrames don't need a separate plotting vocabulary.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Beyond matplotlib
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    The reading's Appendix tours several more libraries: **folium**
    (geographic heatmaps on a real map), **Plotly** (interactive,
    zoomable plots), **Seaborn** (statistical plots with nicer
    defaults), **Altair**, and **Bokeh**. None of these are required
    for this course -- matplotlib stays the foundation because it's
    the most widely supported and gives you the most direct control
    -- but they're worth knowing exist for your own projects later.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Common Mistakes to Avoid
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - **Missing labels or units** -- the single most common deduction
    - **Too many colors and styles in one plot** -- vary one thing at
      a time (color *or* marker), not all of them at once
    - **Forgetting `plt.show()`** -- without it, nothing displays at all
    - **Subplot numbering starting at 0** -- it starts at 1
    - **Doing math on plain lists** -- `list1 - list2` raises
      `TypeError`; convert to NumPy arrays first
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Best Practices Summary
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - Always label axes with units, and always include a title
    - Use a legend whenever there's more than one series
    - Keep styling simple -- vary one thing at a time
    - Choose the plot type from the question you want answered:
      line for trends, scatter for relationships, bar for categories,
      histogram for distributions
    - Use grid lines when a reader needs to read off quantitative values
    - Save figures at 300 dpi for anything going in a report
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Looking Ahead to Class 22
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Next class, almost every command on these slides reappears in
    MATLAB nearly unchanged -- `plot()`, `xlabel()`, `title()`,
    `legend()`, `subplot()` all exist there too. `matplotlib` was
    modeled on MATLAB's own plotting commands, so the hardest part of
    today's reading is already behind you.
    """)
    return


if __name__ == "__main__":
    app.run()
