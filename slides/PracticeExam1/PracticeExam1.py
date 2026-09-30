import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/PracticeExam1.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # EK125 Exam 1

    ### Practice Exam Walkthrough

    Questions, solutions, and tips

    📖 Work through each problem yourself using the practice exam, then
    use this deck to check your answer and pick up a few extra tips.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## How to Use This Deck

    For every problem:

    1. **Try it yourself** first, using the question as shown.
    2. **Advance** to see the answer and the reasoning behind it.
    3. **Advance again** for a 💡 tip — a related gotcha worth knowing
       for the real exam.

    Problems follow the same order and numbering as the practice exam.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 1: True/False (a)

    In the block of code below, the print statement will be invoked
    five times:
    ```python
    for i in range(5):
        print(i)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ True

    `range(5)` produces 5 values (0–4), so the loop body runs 5 times.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 1: True/False (b)

    The expression `10 // 3` evaluates to `3.33`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ False

    `//` is *integer* (floor) division: `10 // 3` is `3`, not `3.33`.
    (`3.33...` is what `10 / 3` gives.)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 1: True/False (c)

    After executing `mylist = [1, 2, 3]` and then `mylist[1] = 99`,
    the list becomes `[1, 99, 3]`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ True

    Lists are mutable; index assignment replaces that one element in
    place.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 1: True/False (d)

    After executing `mystring = "Python"` and then
    `mystring[3] = "t"`, the string becomes `"Pytton"`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ False

    Strings are *immutable*. `mystring[3] = "t"` doesn't silently
    change the string — it raises
    `TypeError: 'str' object does not support item assignment`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 1: True/False (e)

    A `while` loop will always execute its action at least once.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ False

    A `while` loop checks its condition *first*; if it's false
    immediately, the action never runs at all. Python has no built-in
    do-while.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 1: True/False (f)

    The `random.seed()` function ensures that the same sequence of
    "random" numbers is generated each time the program runs.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ True

    That's exactly what `random.seed()` is for: same seed in, same
    sequence of "random" values out, every run.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 1: True/False (g)

    The expression `5 % 2 == 0` evaluates to `True`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ False

    `5 % 2` is `1` (the remainder), and `1 == 0` is `False`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 1: True/False (h)

    Tuples in Python are mutable, meaning members may be added and
    removed after the tuple is created.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ False

    Tuples are immutable, the opposite of lists. Once created, you
    cannot add, remove, or reassign any element.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 2: Multiple Choice (a)

    What is the value of `result` after this code executes?
    ```python
    input = [1, 2, 3, 4]
    result = 0
    for i in input:
        result = result + 1
    ```
    A. `0`&nbsp;&nbsp;&nbsp; B. `4`&nbsp;&nbsp;&nbsp; C. `10`&nbsp;&nbsp;&nbsp; D. program fails to run
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ B (`4`)

    The loop adds `1` once per element, and there are 4 elements.
    (`input` here is just a variable name, shadowing the built-in
    `input()` function — it's a plain list, no actual input-reading
    involved.)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 2: Multiple Choice (b)

    Which best describes what happens when a `for` loop iterates
    through a string?

    A. once per word &nbsp; B. once per character &nbsp; C. until the string is empty &nbsp; D. forever
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ B

    A `for` loop over a string iterates character by character, same
    as over a list of single characters.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 2: Multiple Choice (c)

    ```python
    x = 10
    while x > 5:
        x = x - 2
    print(x)
    ```
    What prints? A. nothing (infinite loop) &nbsp; B. `6` &nbsp; C. `4` &nbsp; D. `10`
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ C (`4`)

    Trace it: `10 → 8 → 6 → 4`, and the loop stops as soon as
    `x > 5` is false (at `x = 4`), *before* subtracting again.
    `print(x)` then shows `4`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 2: Multiple Choice (d)

    What is the purpose of `end=''` in a `print()` statement?

    A. ends the program &nbsp; B. adds extra characters &nbsp; C. prevents moving to a new line &nbsp; D. causes an error
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ C

    `end=''` replaces the default trailing `'\\n'` with nothing, so
    the next `print()` continues on the same line.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 3: Expression Evaluation (a)

    Show the result: `15 % 4 + 2`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `5`

    `15 % 4` is `3`, then `3 + 2` is `5`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 3: Expression Evaluation (b)

    Show the result: `3 ** 2 > 10 or 4 < 5`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `True`

    `3 ** 2` is `9`; `9 > 10` is `False`; but `4 < 5` is `True`;
    `False or True` is `True`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 3: Expression Evaluation (c)

    Show the result: `"hello".upper() == "HELLO"`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `True`

    `.upper()` returns `"HELLO"`, which equals `"HELLO"`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 3: Expression Evaluation (d)

    Show the result (typed sequentially, continuing from a–c):
    ```python
    x = [10, 20, 30]
    x.append(40)
    len(x)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `4`

    The assignment and `.append()` produce no displayed value on
    their own; only the final `len(x)` does, and the list has grown
    to 4 elements.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 3: Expression Evaluation (e)

    Show the result: `not (True and False)`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `True`

    `True and False` is `False`; `not False` is `True`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 3: Expression Evaluation (f)

    Show the result: `"abc" * 2 + "d"`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `"abcabcd"`

    `"abc" * 2` repeats the string first (`"abcabc"`), *then*
    `+ "d"` appends once.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 4: Sequences (a)

    ```python
    colors = ["red", "green", "blue"]
    phrase = "Introduction"
    scores = [85, 92, 78, 95, 88]
    nested = [42, "hello", [1, 2]]
    mixed = ("hello", [1, 2])
    ```

    `colors[0]`
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `'red'`

    Index `0` is the first element.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 4: Sequences (b)

    (same `phrase` as before)

    `phrase[3:6]`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `'rod'`

    `phrase[3:6]` takes indices 3, 4, 5. Spelling out
    `"Introduction"`: `I(0) n(1) t(2) r(3) o(4) d(5) ...` — that's
    `r`, `o`, `d`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 4: Sequences (c)

    (same `scores` as before)

    `scores[-2]`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `95`

    Negative indices count from the end; `-2` is the second-to-last
    element.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 4: Sequences (d)

    (same `colors` as before)

    ```python
    colors.append("yellow")
    len(colors)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `4`

    `colors` grows to `["red", "green", "blue", "yellow"]`, so `len()`
    is `4`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 4: Sequences (e)

    (same `phrase` as before)

    `print(phrase.replace("tion", ""))`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `Introduc`

    `"Introduction"` ends in `...duction`, and `"tion"` (the last 4
    characters) gets replaced with nothing, leaving `"Introduc"`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 4: Sequences (f)

    (same `nested` as before)

    `nested[2][0]`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `1`

    `nested[2]` is the list `[1, 2]`; its `[0]` is `1`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 4: Sequences (g)

    (same `phrase` as before)

    `"e" in phrase`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `False`

    Spell out `"Introduction"`: `I-n-t-r-o-d-u-c-t-i-o-n` — there's
    no letter `e` anywhere in it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 4: Sequences (h)

    (same `nested` as before)

    ```python
    nested.pop()
    len(nested)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `2`

    `.pop()` removes and returns the *last* element (`[1, 2]`);
    `nested` is left with `[42, "hello"]`, so `len()` is `2`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 4: Sequences (i)

    (same `mixed` as before)

    ```python
    mixed[1].append(3)
    len(mixed) + len(mixed[1])
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ `5`

    Even though `mixed` is a tuple, `mixed[1]` is a *list*, and lists
    are always mutable regardless of what holds a reference to them.
    `.append(3)` grows it to `[1, 2, 3]` in place. `len(mixed)` is
    still `2` (the tuple itself has 2 elements); `len(mixed[1])` is
    now `3`; `2 + 3 = 5`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 5: Code Tracing

    ```python
    print("Starting the simulation!")
    print()
    value = 12.8765
    label = "Score"
    print(f"{label}: {value:.1f}")
    word = "Python"
    if word.lower() == "python":
        print("Match found!")
    for num in range(3):
        print(num * 2, end="-")
    print()
    count = 3
    while count > 0:
        print("*" * count)
        count = count - 1
    print("Complete!")
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer

    ```python
    print("Starting the simulation!")
    print()
    value = 12.8765
    label = "Score"
    print(f"{label}: {value:.1f}")
    word = "Python"
    if word.lower() == "python":
        print("Match found!")
    for num in range(3):
        print(num * 2, end="-")
    print()
    count = 3
    while count > 0:
        print("*" * count)
        count = count - 1
    print("Complete!")
    ```

    ```
    Starting the simulation!

    Score: 12.9
    Match found!
    0-2-4-
    ***
    **
    *
    Complete!
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 6: Conditional Logic

    Rewrite using only `if`/`elif`/`else`, no nesting — same logic:

    ```python
    if grade >= 90:
        result = "A"
    else:
        if grade >= 80:
            result = "B"
        else:
            if grade >= 70:
                result = "C"
            else:
                if grade >= 60:
                    result = "D"
                else:
                    result = "F"
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Answer
    ```python
    if grade >= 90:
        result = "A"
    elif grade >= 80:
        result = "B"
    elif grade >= 70:
        result = "C"
    elif grade >= 60:
        result = "D"
    else:
        result = "F"
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 7: Truth Table

    Complete the table for `(not A)`, `(B and C)`, and
    `(not A) or (B and C)`:

    | A | B | C | not A | B and C | (not A) or (B and C) |
    |---|---|---|---|---|---|
    | T | T | T | ? | ? | ? |
    | T | T | F | ? | ? | ? |
    | T | F | T | ? | ? | ? |
    | F | T | T | ? | ? | ? |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### ✅ Answer

    | A | B | C | not A | B and C | (not A) or (B and C) |
    |---|---|---|---|---|---|
    | T | T | T | F | T | **T** |
    | T | T | F | F | F | **F** |
    | T | F | T | F | F | **F** |
    | F | T | T | T | T | **T** |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Problem 8: While Loop with Validation

    Prompt for a password. Valid only if **at least 6 characters AND
    contains at least one digit**. Keep prompting until valid, then
    print `"Password accepted!"`.

    ```
    Enter a password: hi
    Enter a password: hello
    Enter a password: hello1
    Password accepted!
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Solution

    ```python
    have_valid_password = False
    while not have_valid_password:
        password = input("Enter a password: ")
        hasDigit = False
        for char in password:
            if char.isdigit():
                hasDigit = True
        if hasDigit and len(password) >= 6:
            have_valid_password = True
            print("Password accepted!")
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 9: Random Numbers and List Processing

    Using `random.seed(42)`:
    - Generate 6 random integers, each 1–20 (inclusive)
    - Print the list
    - Print the **sum of the even numbers** (by value, not index)
    - Print the **count of numbers greater than 10**

    Format:
    ```
    Numbers: [list of numbers here]
    Sum of even numbers: X
    Count greater than 10: Y
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Solution

    ```python
    import random

    random.seed(42)
    generated_numbers = []
    for i in range(6):
        generated_numbers.append(random.randint(1, 20))

    even_sum = 0
    greater_than_ten = 0
    for number in generated_numbers:
        if number % 2 == 0:
            even_sum = even_sum + number
        if number > 10:
            greater_than_ten = greater_than_ten + 1

    print(f"Numbers: {generated_numbers}")
    print(f"Sum of even numbers: {even_sum}")
    print(f"Count greater than 10: {greater_than_ten}")
    ```

    ```
    Numbers: [4, 1, 9, 8, 8, 5]
    Sum of even numbers: 20
    Count greater than 10: 0
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Problem 10: BlackJack Experiment

    Deal 4 random "cards," each uniformly 1–11 (inclusive, no choice
    between 1/11). Simulate **100 experiments**. Print:
    ```
    Of 100 experiments, N resulted in a value of 21 or less.
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ### ✅ Solution

    ```python
    import random

    under_twenty_one = 0
    for experiment in range(100):
        total_value = 0
        for card_number in range(4):
            total_value = total_value + random.randint(1, 11)
        if total_value <= 21:
            under_twenty_one += 1

    print(f"Of 100 experiments, {under_twenty_one} resulted in a value of 21 or less.")
    ```

    ```
    Of 100 experiments, 40 resulted in a value of 21 or less.
    ```
    (unseeded -- yours will be different, and so will the next run of
    this exact code)
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## That's the Whole Exam

    A few cross-cutting habits that showed up again and again:

    - **Trace loops on paper**, one line at a time — don't do it in
      your head.
    - Know which built-ins are **mutable** (lists) vs **immutable**
      (strings, tuples) — cold.
    - Watch for a problem explicitly ruling out a wrong approach in
      parentheses — that's a hint about a common mistake, not filler
      text.
    - For programming problems, **match the output format exactly** —
      extra or missing punctuation costs points even with correct
      logic.

    Good luck!
    """)
    return


if __name__ == "__main__":
    app.run()
