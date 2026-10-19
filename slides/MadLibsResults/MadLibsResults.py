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
    ## Entry: Table 1
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

    CHOICES = {"adj": 1, "noun": 2, "verb": 2, "place": 2}
    print(mad_libs(TEMPLATE, WORD_BANK, CHOICES))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    The gigantic professor loves to teleport in the cafeteria.
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Entry: Table 2
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

    CHOICES = {"adj": 0, "noun": 0, "verb": 0, "place": 0}
    print(mad_libs(TEMPLATE, WORD_BANK, CHOICES))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    The sneaky toaster loves to tango in the library.
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Entry: Table 3
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def mad_libs(template, word_bank, choices):
        story = template
        for category, index in choices.items():
            word = word_bank[category][index]
            story = story.replace('{' + category + '}', word)
        return story

    CHOICES = {"adj": 2, "noun": 2, "verb": 1, "place": 2}
    print(mad_libs(TEMPLATE, WORD_BANK, CHOICES))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    The soggy professor loves to sneeze in the cafeteria.
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Entry: Table 4
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

    CHOICES = {"adj": 2, "noun": 2, "verb": 0, "place": 1}
    print(mad_libs(TEMPLATE, WORD_BANK, CHOICES))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    The soggy professor loves to tango in the volcano.
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Entry: Table 6
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def mad_libs(template, word_bank, choices):
        story = template
        story_withadj = story.replace(
            "{adj}", word_bank["adj"][choices["adj"]])
        story_withnoun = story_withadj.replace(
            "{noun}", word_bank["noun"][choices["noun"]])
        story_withverb = story_withnoun.replace(
            "{verb}", word_bank["verb"][choices["verb"]])
        story_withplace = story_withverb.replace(
            "{place}", word_bank["place"][choices["place"]])
        return story_withplace

    CHOICES = {"adj": 1, "noun": 2, "verb": 0, "place": 2}
    print(mad_libs(TEMPLATE, WORD_BANK, CHOICES))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    The gigantic professor loves to tango in the cafeteria.
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Entry: Table 7
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def mad_libs(choices=None, template=None, w_bank=None):
        story = template
        for blank, index in choices.items():
            story = story.replace(
                "{" + blank + "}", w_bank[blank][index])
        return story

    CHOICES = {"adj": 0, "noun": 1, "verb": 1, "place": 0}
    print(mad_libs(choices=CHOICES, template=TEMPLATE,
                    w_bank=WORD_BANK))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    The sneaky llama loves to sneeze in the library.
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Entry: Table 8
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    import random

    def mad_libs(template, word_bank, choices):
        story = template
        for blank, index in choices.items():
            word = word_bank[blank][index]
            story = story.replace(f"{{{blank}}}", word)
        return story

    # chooses randomly each run -- this run picked:
    CHOICES = {"adj": 2, "noun": 1, "verb": 1, "place": 1}
    print(mad_libs(TEMPLATE, WORD_BANK, CHOICES))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    The soggy llama loves to sneeze in the volcano.
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Entry: Table 10
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def mad_libs(template, word_bank, choices):
        story = template
        for blank, index in choices.items():
            word_list = word_bank[blank]
            word = word_list[index]
            placeholder = "{" + blank + "}"
            story = story.replace(placeholder, word)
        return story

    CHOICES = {"adj": 2, "noun": 2, "verb": 1, "place": 1}
    print(mad_libs(TEMPLATE, WORD_BANK, CHOICES))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    The soggy professor loves to sneeze in the volcano.
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Entry: Table (unnumbered)

    This table wrote its own version of `TEMPLATE` without the `{}`
    markers — still works, just a different style.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    TEMPLATE = "The adj noun loves to verb in the place."

    def mad_libs(TEMPLATE, WORD_BANK, CHOICES):
        story = TEMPLATE
        for blank, index in CHOICES.items():
            word = WORD_BANK[blank][index]
            story = story.replace(blank, word)
        return story

    CHOICES = {"adj": 2, "noun": 0, "verb": 0, "place": 2}
    print(mad_libs(TEMPLATE, WORD_BANK, CHOICES))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    The soggy toaster loves to tango in the cafeteria.
    ```
    """)
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
