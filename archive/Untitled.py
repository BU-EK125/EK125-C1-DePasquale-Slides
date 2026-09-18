import marimo

__generated_with = "0.24.0"
app = marimo.App(
    width="full",
    layout_file="layouts/Untitled.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Testing
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Testing again
    """)
    return


@app.cell
def _():
    x = 2
    x**3
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
