import marimo

__generated_with = "0.24.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class4_Lecture.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Selection Statements

    ### if, if-else, and elif

    *Class 4*

    📖 [Full reading: Class 4](https://BU-EK125.github.io/EK125/class/Class4.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 1. Strings — Escape Characters

    Strings look simple, but a few characters can't just be typed
    directly into one — a newline, a tab, a literal quote mark. Escape
    sequences are how you tell Python "this backslash isn't a backslash,
    it's an instruction."
    """)
    return


@app.cell
def _():
    # From the reading's "Escape Characters" section (Class4.html)
    print("Hello\nWorld")
    print("Column1\tColumn2")
    print("A backslash looks like this: \\")
    "Column1\tColumn2"
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Newline and tab characters are exactly what GPP's Problem 1.2 (the
    resistor report) asks you to use for new lines and column alignment.
    A single backslash by itself would be read as the start of another
    escape sequence, which is why printing an actual backslash character
    takes writing two of them in the source code.

    Also notice the last line's *displayed* output still shows the tab
    as literal escape-sequence text instead of a real gap. `print()`
    writes the tab character straight to the terminal, which renders it
    as spacing — but a bare value (with no `print()`) is shown with
    Python's `repr()`, which re-escapes special characters so you can
    see exactly what's in the string. Same string in memory, two
    different ways of showing it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Indexing

    Every character in a string sits at a numbered position, and Python
    lets you grab any one of them with square brackets. Counting starts
    at `0`, not `1` — and counting can also run backward from the end.
    """)
    return


@app.cell
def _():
    # From the reading's "Indexing" section (Class4.html)
    word2 = "Python"
    print(word2[0])  # 'P'
    print(word2[-1])  # 'n'
    word2[-1]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Positive indices count from the front, negative ones from the back —
    `word2[-1]` is always the last character no matter how long the
    string is, which is much safer than writing `word2[len(word2) - 1]`
    by hand.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Slicing

    Indexing gets you one character. Slicing gets you a whole chunk at
    once, by giving a start position and a stop position separated by a
    colon. Either side can be left off to mean "from the beginning" or
    "to the end."
    """)
    return


@app.cell
def _():
    # From the reading's "Slicing" section (Class4.html)
    word = "Python"
    print(word[0:2])  # 'Py'
    print(word[:3])  # 'Pyt'
    print(word[3:])  # 'hon'
    word[0:2]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    A slice **excludes the end index** — `word[0:2]` stops *before*
    position `2`, so you get `'Py'` (positions 0 and 1), not `'Pyt'`.
    This trips people up constantly, so it's worth saying twice: the
    number after the colon is where the slice stops, not the last
    character it includes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## REMEMBER: Strings Are Immutable!

    This is one of the reading's own all-caps warnings, and for good
    reason. Once a string is created, none of its individual characters
    can be changed — you can only build a brand-new string out of pieces
    of the old one.
    """)
    return


@app.cell
def _():
    # From the reading — "Strings Are Immutable" (Class4.html)
    s = "cat"
    # s[0] = "b"  # ERROR: strings don't support assignment
    s = "b" + s[1:]
    s
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    You can't change a string in place — `s[0] = "b"` raises an error,
    full stop. The workaround is always the same shape: slice out the
    part you want to keep, and glue it back together with `+` into a
    *new* string. Reassigning `s` doesn't mutate the old string; it
    just points the name `s` at a different one.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Common Mistakes with Strings

    The reading pairs almost every topic with a "here's how it actually
    breaks" example. For strings, the classic mistake is trying to
    assign directly into a character position — exactly the thing the
    slide before just warned you not to do.

    ```python
    s = "dog"
    s[0] = "c"   # trying to mutate a string in place
    ```
    ```
    TypeError: 'str' object does not support item assignment
    ```

    Seeing the real error message matters: `TypeError` and "does not
    support item assignment" are the exact words you'll see in your own
    terminal when this happens, so it's worth recognizing on sight.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 2. Objects and Methods

    Strings and lists aren't just raw data — they're objects, which
    means they come with built-in **methods**: functions that belong to
    the value and act on it directly, called with a dot.
    """)
    return


@app.cell
def _():
    # From the reading's "Methods for Strings" (Class4.html)
    word3 = "python"
    print(word3.upper())  # 'PYTHON'
    print(word3.capitalize())  # 'Python'
    print(word3.replace("py", "java"))  # 'javathon'
    word3.find("th")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `.upper()` is exactly what GPP's Problem 1.1 needs to format the
    material name for the report header — `"steel".upper()` becomes
    `"STEEL"`. Like slicing, none of these methods change `word3`
    itself; each one hands back a new string, which is just another
    consequence of strings being immutable.
    """)
    return


@app.cell
def _():
    # From the reading's "Methods for Lists" (Class4.html)
    numbers_list = [3, 1, 4]
    numbers_list.append(2)
    numbers_list.sort()
    numbers_list.reverse()
    numbers_list
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `.append()`, `.sort()`, and `.reverse()` all mutate `numbers_list`
    **in place** — no reassignment needed, because lists (unlike
    strings) are mutable. These are the same list methods from Class 2;
    they're just showing up again here as part of the reading's full
    review.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Common Errors with Methods

    A method is a function — and like any function, it has to actually
    be *called* with parentheses to do anything. Leaving them off is an
    easy typo with a confusing result.

    ```python
    word = "python"
    print(word.upper)   # forgot the parentheses!
    ```
    ```
    <built-in method upper of str object at 0x...>
    ```

    Without `()`, Python doesn't run `.upper()` — it just hands you a
    *reference* to the method itself, which is why the output looks
    like a strange memory address instead of `"PYTHON"`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 3. User Input

    Everything so far has used data we typed directly into the code.
    `input()` is how a program instead asks the person running it a
    question and waits for an answer.
    """)
    return


@app.cell
def _():
    # From the reading's "User Input" section (Class4.html)
    typed_name = "Christine"  # originally: input("What is your name? ")
    f"Hello, {typed_name}"
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Every problem in today's GPP starts here — `input()` is how the beam
    lengths, resistor values, and prize-generator text all get into your
    program in the first place. The message inside the parentheses is
    just a prompt shown to the user; the value they type back is what
    gets stored in the variable.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Common Errors with Input

    `input()` has one property that catches almost everyone off guard
    at least once: whatever the user types, Python hands it back as a
    **string** — always, even if it looks like a number.

    ```python
    age = input("How old are you? ")
    print(age + 1)   # age is a string, 1 is an int
    ```
    ```
    TypeError: can only concatenate str (not "int") to str
    ```

    Python won't silently guess that you meant to add numbers — mixing
    a string and an int with `+` is a hard error, not a warning.

    This is exactly why GPP's Problem 1.1 warns: "you might need to type
    cast your inputs to make sure everything computes!"
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 4. Type Casting (Converting Between Types)

    Since `input()` always hands back a string, converting — "casting"
    — that string into a number is one of the most common first steps
    in almost any program that reads user input.
    """)
    return


@app.cell
def _():
    # From the reading's "Type Casting" section (Class4.html)
    numeric_age = float("21.0")
    type(numeric_age)
    #numeric_age + 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `input()` always returns a **string** — cast it with `int()` or
    `float()` *before* doing any math on it, not after. `int()` converts
    to a whole number; `float()` keeps decimal places, which matters for
    things like the beam lengths and current values in this week's GPP.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Common Errors with Casting

    Casting isn't magic — it can only convert text that actually looks
    like the type you're asking for, and even when it succeeds, the
    result can be surprising.

    ```python
    int("hello")   # not a valid integer
    ```
    ```
    ValueError: invalid literal for int() with base 10: 'hello'
    ```

    Notice the error type is different from before — `ValueError`, not
    `TypeError` — because this time the *type* was right (it's a
    string), but the *content* wasn't a number.

    Casting can surprise you in the other direction too: `bool("0")` is
    actually `True`, because any non-empty string counts as truthy in
    Python — even the string `"0"`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 5. Output Formatting

    Getting the right *numbers* is only half of most GPP problems — the
    other half is presenting them the way the example run shows: neatly
    labeled, aligned, and rounded. That's what this whole section is
    about.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## f-Strings

    An f-string lets you drop a variable's value directly into the
    middle of a sentence, just by wrapping it in curly braces inside a
    string that starts with `f`.
    """)
    return


@app.cell
def _():
    # From the reading's "f-Strings" section (Class4.html)
    name = "Alice"
    age = 21
    f"My name is {name} and I am {age} years old."
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    f-strings drop values straight into text — no more `+` and `str()`
    chains to stitch a message together piece by piece. This is exactly
    what GPP's beam and resistor reports are built from: one f-string
    per line, with the numbers plugged straight into the sentence.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Field Width and Alignment

    Beyond just inserting a value, f-strings can control exactly how
    much space it takes up and which way it's aligned — which is how
    you get numbers to line up into neat columns.
    """)
    return


@app.cell
def _():
    # From the reading's "Field Width and Alignment" section (Class4.html)
    width_num = 1234
    print(f"{width_num:8d}")  # right-aligned (default)
    print(f"{width_num:<8d}")  # left-aligned
    print(f"{width_num:^8d}")  # centered
    f"{width_num:^8d}"
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    The format spec after the colon controls the layout: `:8d` reserves
    8 characters of width for an integer (right-aligned by default),
    `<8d` pushes it to the left, and `^8d` centers it. This is exactly
    the beam-length table format GPP's Problem 1.1 asks for — width 10,
    right-aligned, with the unit `m` tacked on the end.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Common Errors with Output

    Formatted output has two classic failure modes, and both are worth
    seeing once so you recognize them instantly in your own code.

    ```python
    name = "Alice"
    print("Hello {name}")   # forgot the f — literally prints {name}
    ```
    ```
    Hello {name}
    ```

    Without the `f` prefix, Python treats `{name}` as nothing special —
    just four literal characters in the string. No error, which is what
    makes this mistake sneaky: your code runs fine, it just silently
    prints the wrong thing.

    ```python
    pi = 3.14
    print(f"{pi:d}")   # 'd' is for integers, not floats
    ```
    ```
    ValueError: Unknown format code 'd' for object of type 'float'
    ```

    This one *does* error, because `:d` specifically means "format this
    as an integer," and `pi` is a float. Forgetting the `f` or using the
    wrong format code are the two easiest ways to break a GPP report
    table, so double-check both whenever a table looks off.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Key Takeaways

    This is the reading's own summary of everything above, condensed
    into the rules you'll actually lean on while writing tonight's GPP:

    - "Strings are immutable" — once created, they cannot be modified in place; you always build a new string instead
    - Slicing "excludes the end index" — `word[a:b]` stops right before position `b`
    - Methods need `()` to run — without it, you're printing a reference to the method, not its result
    - "input() always returns a string" — cast it with `int()` or `float()` before doing math
    - Casting can surprise you: `bool("0")` is `True`, because any non-empty string is truthy
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Selection Statements

    Everything up to this point has been about *computing* values.
    Selection statements are how a program starts *deciding* what to do
    with them — running some lines and skipping others based on a
    condition.

    ```python
    if condition:
        action
    rest of code
    ```

    - `condition` must evaluate to `True` or `False` — the same Booleans from Class 3
    - `action` runs only if `condition` is `True`; otherwise it's skipped entirely
    - Indentation is what defines the block — 4 spaces, by convention — and everything indented under the `if` belongs to it
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## If Statements

    The simplest selection statement has no "else" — it just says
    "run this if the condition is true, and otherwise do nothing extra."
    """)
    return


@app.cell
def _():
    # From the reading's "If Statements" section (Class4.html)
    num = 33
    if num < 50:
        print('It is smaller')
    print('And that is it')
    num
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    If the condition is `False`, the indented block just never runs —
    there's no error, no skipped line printed twice, nothing dramatic.
    The rest of the code, at the original indentation level, moves on
    exactly as if the `if` block weren't there at all.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## If-else Statements

    Adding an `else` gives you a second path: one branch runs when the
    condition is `True`, the other when it's `False` — never both, never
    neither.
    """)
    return


@app.cell
def _():
    # From the reading's "If-else Statements" section (Class4.html)
    num2 = -4.0
    if num2 < 0:
        print(f'{num2} is a negative number')
    else:
        print(f'{num2} is a nonnegative number')
    num2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `else` catches everything the `if` didn't — exactly one branch runs,
    every time, for every possible value of `num2`. You never have to
    write out the opposite condition yourself.
    """)
    return


@app.cell
def _():
    # From the reading's "If-else Statements" section (Class4.html)
    num3 = 0.0
    if num3 < 0:
        print(f'{num3} is a negative number')
    elif num3 == 0:
        print('It is a zero')
    else:
        print(f'{num3} is a positive number')
    num3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `elif` adds more branches without nesting a new `if` inside the
    `else`. Python checks each condition top to bottom in order and
    stops at the very first one that's `True` — later `elif`/`else`
    branches are never even evaluated once a match is found.
    """)
    return


@app.cell
def _():
    # From the reading's "If-else Statements" section (Class4.html)
    num4 = 7
    if 5 <= num4 <= 10:
        print('In range')
    else:
        print('Not in range')
    num4
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `5 <= num4 <= 10` is exactly `(5 <= num4) and (num4 <= 10)` written
    more compactly — the same chained-comparison trick from Class 3's
    Boolean expressions, now living inside an `if` condition.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Nested `if` vs. `elif`

    This week's GPP has you check leap years using **three levels of
    nested if/else** — an `if` inside an `if` inside an `if`. It works,
    but it's easy to lose track of which branch you're in. Here's the
    same underlying decision, side by side, written both ways.
    """)
    return


@app.cell
def _():
    # Nested if/else — an if inside an if inside an if
    grade_score = 82

    if grade_score >= 90:
        letter_grade = "A"
    else:
        if grade_score >= 80:
            letter_grade = "B"
        else:
            if grade_score >= 70:
                letter_grade = "C"
            else:
                letter_grade = "F"

    letter_grade
    return (grade_score,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Every branch after the first is nested one level deeper inside the
    previous `else` — by the time you reach the "F" case, you're three
    indents deep just to express one decision.
    """)
    return


@app.cell
def _(grade_score):
    # The exact same decision, flattened with elif
    if grade_score >= 90:
        letter_grade2 = "A"
    elif grade_score >= 80:
        letter_grade2 = "B"
    elif grade_score >= 70:
        letter_grade2 = "C"
    else:
        letter_grade2 = "F"

    letter_grade2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Same `grade_score`, same result — `"B"` either way — but `elif`
    keeps every branch at the same indentation level. This is exactly
    the transformation the reading applies to the leap-year check: same
    logic, flattened from a staircase into a single readable chain.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Your Turn

    Straight from this week's GPP — Problem 2.3:

    Write a program that asks the user to enter a number, then
    determines whether it's **positive**, **negative**, or **zero**.

    ```
    Enter a number: 7
    The number is positive.
    ```

    *Sketch the if/elif/else you'd need — which condition should you
    check first, and does the order matter here? You'll code it for
    real in the GPP.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Recap

    - **Know your data's type before you operate on it** — `input()`
      always returns a string; cast it before doing math, and remember
      that methods return new values rather than changing the original
    - **Structure decisions the way you'd explain them out loud** —
      if/elif/else should read like your own step-by-step reasoning,
      checked in the same order you'd naturally check it
    - **Test the boundaries** — zero, negative, and exactly-equal cases
      are where logic quietly breaks, so check them deliberately instead
      of hoping they never come up
    - **Simplify once you understand the nesting** — `elif` flattens
      what nested if/else makes hard to read, but only reach for it
      once you're sure the nested version actually does what you want
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## How This Shows Up in Today's GPP

    - **Problems 1.1 / 1.2** → casting `input()` to a number, then formatting the result with f-strings, field width, and decimal places
    - **Problems 2.1–2.3** → building `if`, `if-else`, and `if/elif/else` from scratch, including fixing broken indentation
    - **Problems 3.1–3.4** → nested `if`, `elif`, Booleans, and every technique above combined into one program
    """)
    return


if __name__ == "__main__":
    app.run()
