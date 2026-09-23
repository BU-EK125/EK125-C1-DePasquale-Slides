import marimo

__generated_with = "0.24.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class2_GPP.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Week 2A Morning Assignment: Working with Sequences

    **Group Exercise (Teams of 3)**

    📖 [Full reading: Class 2](https://BU-EK125.github.io/EK125/class/Class2.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 1: String Exploration

    Work together to complete the following tasks:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Task 1.1: String Basics
    """)
    return


@app.cell
def _():
    # Given this string:
    sentence = "The quick brown fox jumps over the lazy dog"

    # Write code to:
    # 1. Print the first character
    # 2. Print the last character
    # 3. Print the length of the sentence
    # 4. Check if the word "fox" is in the sentenc
    sentence[1]
    return (sentence,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Bonus: Slicing (from the reading)
    """)
    return


@app.cell
def _(sentence):
    # Bonus from the reading — "Slicing" (Class2.html)
    sentence[0:9]  # a *range* of positions, not just one
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Slicing works on lists too — same `[start:stop]` syntax. "
        "Try `sentence[-9:]` next.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Task 1.2: String Manipulation
    """)
    return


@app.cell
def _():
    # Given this string:
    name = "john doe"

    # Write code to do each of the following (create a new variable for each, always starting from the original `name`):
    # 1. Convert it to title case (John Doe) and print the result
    # 2. Replace all spaces with underscores and print the result
    # 3. Convert to uppercase and print the result
    # 4. Count how many times the letter 'o' appears and print the count
    name.title()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 2: List Operations
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Task 2.1: List Creation and Access
    """)
    return


@app.cell
def _():
    # Create a list containing the names of your three team members
    teamNames = ["bob", "sally", "george"]  # Fill this in

    # Write code to:
    # 1. Print the first team member's name
    # 2. Print the last team member's name
    # 3. Print how many people are on your team
    # 4. Add a fourth name "TA Helper" to the list

    teamNames
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Task 2.2: List Modification Challenge
    """)
    return


@app.cell
def _():
    # Start with this list:
    numbers = [10, 20, 30, 40, 50]

    # Without retyping the entire list, use list methods to:
    # 1. Change the third number from `30` to `35`
    # 2. Add the number 60 to the end
    # 3. Insert the number 5 at the beginning (Careful, this is a little harder!)
    # 4. Remove the number 40 from the list
    # 5. Remove the last number from the list
    # Print the final list - it should be [5, 10, 20, 35, 50]

    numbers
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 3: Mixed Practice
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Task 3.1: Data Processing

    Your team has collected some survey data. Help clean and process it:
    """)
    return


@app.cell
def _():
    # Raw survey responses (some have extra spaces, inconsistent capitalization)
    responses = ["yes", "NO", "maybe", "YES", "no", "Maybe", "yes"]

    # Write code to:
    # 1. Clean each response (convert to lowercase)
    # 2. Count how many "yes", "no", and "maybe" responses there are
    # 3. Create separate lists for each type of response
    # 4. Create separate tuples for each type of response

    responses
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Task 3.2: Text Analysis
    """)
    return


@app.cell
def _():
    # Analyze this text:
    text = """Monty Python's sketch on spam https://en.wikipedia.org/wiki/Spam_(Monty_Python_sketch)
    directly led to the use of spam to describe unwanted email. As a joke, and in reference
    to the repetitive and unwanted presence of spam in the sketch, early internet users
    flooded forums with the word SPAM . This came to describe the equally unwanted marketing
    and repetetive emails which flood our inbox daily."""

    # Write code to:
    # 1. Split the text into individual words
    # 2. Count how many words there are total
    # 3. Count how many times "spam" appears, both upper and lowercase

    text
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 4: Challenge Problem

    This is a bit of a stretch. You will have to do some work on your own to
    find the additional command necessary to test if something is a string or
    a number.
    """)
    return


@app.cell
def _():
    # You have a list of mixed data types:
    mixed_data = [1, "hello", 2.5, "world", 42, "python", 3.14]

    # Write code to:
    # 1. Create two separate lists: one for numbers, one for strings
    # 2. Calculate the sum of all numbers
    # 3. Join all strings together with spaces between them

    mixed_data
    return


if __name__ == "__main__":
    app.run()
