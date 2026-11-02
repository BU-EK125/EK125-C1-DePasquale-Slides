import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class17.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Writing Real Functions

    ### Fitness Tracker Project — Part 3

    *Class 17*

    📖 [Full reading: Class 17](https://BU-EK125.github.io/EK125/class/Class17.html)
    📋 [Today's Team Activity](https://BU-EK125.github.io/EK125/gpps/Class17_TeamActivity.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Last Week: The Frame. Today: The Interior.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Last week your team built the house's **frame** — every stub in
    place, the whole skeleton standing and running, even though
    nothing inside was real yet.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Today you do the **interior work** — wiring, plumbing, finishes —
    inside walls that don't move. Your contract is the frame; your
    real code is everything behind the walls.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    If your real function keeps every promise your stub kept, the
    rest of the house doesn't even notice the walls went up for real.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## This Afternoon
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Part D (20 min, together):** walkthrough of the two trickiest
    functions — the Loader's skip-the-row logic and the Analyst's
    best-day loop — plus a quick Report Writer formatting tip. Follow
    along in your own file only if it's your function; everyone else
    takes notes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Part E (remaining time):** finish your real function until
    every test passes, add one more test of your own, **explain your
    code line by line to a teammate**, then upload and re-run
    `main.py`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Clues for Building the Real Thing
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - **Loader:** a blank value becomes an empty string after
      splitting — can you check the *whole row* at once, instead of
      one value at a time?
    - **Analyst:** tracking "best so far" gives you a **list
      position** — after skipping rows, does that position still
      match the day number?
    - **Analyst:** what changes in your comparisons when
      `higher_is_better` is `False`? (Hint: more than one line.)
    - **Report Writer:** check your contract's example value closely —
      does it want `8327.8`, or something formatted differently?
    - **Everyone:** `0.1 + 0.2 != 0.3`. If your test compares floats
      with `==`, where should the rounding happen?
    """)
    return


if __name__ == "__main__":
    app.run()
