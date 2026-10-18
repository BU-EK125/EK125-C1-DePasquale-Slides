import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/MadLibsResults.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Mad Libs Contest Results

    ### Class 13 — read, run, and vote

    *Filled in live after every table submits.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## How to Use This Deck

    Each entry shows one table's `mad_libs` function and its story —
    vote for the funniest once you've seen them all.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Shared Data

    Every table worked from this same word bank and template.

    ```python
    WORD_BANK = {
        "adj":   ["sneaky", "gigantic", "soggy"],
        "noun":  ["toaster", "llama", "professor"],
        "verb":  ["tango", "sneeze", "teleport"],
        "place": ["library", "volcano", "cafeteria"],
    }

    TEMPLATE = ("The {adj} {noun} loves to {verb} "
                "in the {place}.")
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Entry: Test Submission

    From the test file submitted through the form — real tables will
    each get their own slide in this same format.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def mad_libs(template, word_bank, choices):
        story = template
        for blank, index in choices.items():
            word = word_bank[blank][index]
            story = story.replace("{" + blank + "}", word)
        return story
    CHOICES = {"adj": 1, "noun": 0, "verb": 2, "place": 1}
    print(mad_libs(TEMPLATE, WORD_BANK, CHOICES))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    The gigantic toaster loves to teleport in the volcano.
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Vote Now

    Once every table has been shown, vote for the funniest story
    through the same form you submitted with.

    📝 [Submit and vote here](https://forms.gle/JpDvFxKsoRbSEf3Z8)
    """)
    return


if __name__ == "__main__":
    app.run()
