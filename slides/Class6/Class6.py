import marimo

__generated_with = "0.24.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class6.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Nested Loops

    ### One Loop Inside Another

    *Class 6*

    📖 [Full reading: Class 6](https://BU-EK125.github.io/EK125/class/Class6.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Nested `for` Loops

    A **nested loop** is one loop inside another — the *action* of the
    outer loop contains a whole other loop.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    A list of words, printed character by character. The outer loop picks
    each word; the inner loop picks each character in that word.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    wordlist = ['hello', "hi", 'ciao']
    for myword in wordlist:
        for c in myword:
            print(c, end=' ')
        print()
    print("That's it!")
    ```

    ```
    h e l l o
    h i
    c i a o
    That's it!
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    The **outer loop** iterates over the *words*. For each word, the
    **inner loop** iterates over its *characters*. The `print()` that
    starts a new line belongs to the outer loop's action, not the inner
    loop's — it runs once per word, not once per character.

    🚩 **Common mistake:** misplacing that newline `print()`. If it's
    indented one level too far — inside the inner loop instead of after
    it — you get a newline after *every character* instead of after
    every *word*. When a nested loop's output looks "off by one
    indentation level," check exactly which loop each statement belongs
    to.

    You'll practice this exact pattern in today's GPP — see
    [Problem 5](https://BU-EK125.github.io/EK125/gpps/Class6_GPP.html#problem-5-printing-characters-from-strings-with-separators).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Building Up: Numbers and Stars

    Same shape, different content. The outer loop repeats 3 times,
    printing a number and a colon; the inner loop prints stars.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    for num in range(3):
        print(f'{num}:', end=' ')
        for n in range(5):
            print('*', end='')
        print()
    ```

    ```
    0: *****
    1: *****
    2: *****
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Fixed 5 stars every time. To make the star *count* track the outer
    loop's number, the inner loop needs to depend on `num` too.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    for num in range(3):
        print(f'{num}:', end=' ')
        for n in range(num + 1):
            print('*', end='')
        print()
    ```

    ```
    0: *
    1: **
    2: ***
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("What if we want the *labels* to start at 1 instead of 0?")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    for num in range(3):
        print(f'{num + 1}:', end=' ')
        for n in range(num + 1):
            print('*', end='')
        print()
    ```

    ```
    1: *
    2: **
    3: ***
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    🚩 **Common mistake:** updating what gets *displayed* without
    updating what gets *counted*, or vice versa. Both `{num+1}` (the
    printed label) and `range(num+1)` (the star count) had to change
    *together* to stay in sync — if you only update one, your displayed
    row number and its star count won't match.

    This is Problem 2 in today's GPP — see
    [Problem 2](https://BU-EK125.github.io/EK125/gpps/Class6_GPP.html#problem-2-formatted-output-with-nested-loops)
    and
    [Problem 7](https://BU-EK125.github.io/EK125/gpps/Class6_GPP.html#problem-7-triangle-of-stars).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 🎯 Quick Check: Predict Before You Code

    For row `num = 3` (which should print `3:***`), which inner loop
    is correct?

    **A.** `for i in range(num):`

    **B.** `for i in range(num + 1):`

    **C.** `for i in range(num - 1):`

    **D.** `for i in range(1, num):`

    📝 **Submit your answer below:**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.iframe(
        """
        <style>
          body { margin:0; padding:12px; background:#1a1a1a; font-family:-apple-system,sans-serif; }
          .qc-row { display:flex; gap:12px; }
          .qc-btn { flex:1; padding:14px; font-size:1.1em; font-family:monospace;
                    border-radius:8px; border:1px solid #555; background:#2a2a2a;
                    color:#eee; cursor:pointer; }
          .qc-status { margin-top:10px; font-size:0.95em; color:#9c9; min-height:1.2em; }
        </style>
        <div class="qc-row">
          <button class="qc-btn" data-choice="A">A</button>
          <button class="qc-btn" data-choice="B">B</button>
          <button class="qc-btn" data-choice="C">C</button>
          <button class="qc-btn" data-choice="D">D</button>
        </div>
        <div class="qc-status"></div>
        <script>
        (function () {
          var buttons = document.querySelectorAll('.qc-btn');
          var status = document.querySelector('.qc-status');
          var submitted = false;
          buttons.forEach(function (btn) {
            btn.addEventListener('click', function () {
              if (submitted) return;
              submitted = true;
              var choice = btn.getAttribute('data-choice');
              buttons.forEach(function (b) { b.disabled = true; b.style.opacity = '0.5'; });
              btn.style.opacity = '1';
              btn.style.background = '#2d6a4f';
              fetch('https://docs.google.com/forms/d/e/1FAIpQLSeuAoyLtubfSinMFax9ZNpYQROztkgnQ0dr17WnwAyfb69-Cg/formResponse', {
                method: 'POST',
                mode: 'no-cors',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: 'entry.1109327713=' + encodeURIComponent(choice),
              });
              status.textContent = 'Submitted: ' + choice;
            });
          });
        })();
        </script>
        """,
        width="100%",
        height="140px",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Nesting a `while` Loop Inside a `for` Loop

    Say we want the user to enter **3 positive numbers**. A `for` loop
    repeats the action 3 times; each time, a `while` loop error-checks
    until a positive number actually comes through.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    for i in range(3):
        number = input('Enter a positive number: ')
        number = float(number)
        while number <= 0:
            print('Please follow directions!')
            number = input('Enter a positive number: ')
            number = float(number)
        print('Thanks for entering', number)
        print()
    ```

    ```
    Enter a positive number: 4
    Thanks for entering 4.0

    Enter a positive number: -3.3
    Please follow directions!
    Enter a positive number: 5.1
    Thanks for entering 5.1

    Enter a positive number: -6
    Please follow directions!
    Enter a positive number: 11
    Thanks for entering 11.0
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    🚩 **Common mistake #1:** forgetting to re-read `number` inside the
    `while` loop's body. Leave out that second `number = input(...)` and
    `number` never changes — the condition `number <= 0` stays true
    forever, and the program hangs in an infinite loop.

    🚩 **Common mistake #2:** confusing "loop 3 times" with "3 total
    attempts." The outer `for` loop only counts *successful* entries — a
    user who enters `-5, -3, 7` has used 3 attempts but only filled 1 of
    the 3 required slots. Rejected entries don't count toward the 3.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 🎯 Quick Check: Predict Before You Code

    In Problem 6, you'll write a script that prompts for positive
    numbers and validates each one with a `while` loop, same pattern as
    above. If you forget to re-read the input inside that validation
    loop, what happens when the user enters a negative number?

    **A.** The program crashes immediately

    **B.** The loop runs forever (infinite loop)

    **C.** The program skips to the next line

    **D.** Python automatically fixes it

    📝 **Submit your answer below:**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.iframe(
        """
        <style>
          body { margin:0; padding:12px; background:#1a1a1a; font-family:-apple-system,sans-serif; }
          .qc-row { display:flex; gap:12px; }
          .qc-btn { flex:1; padding:14px; font-size:1.1em; font-family:monospace;
                    border-radius:8px; border:1px solid #555; background:#2a2a2a;
                    color:#eee; cursor:pointer; }
          .qc-status { margin-top:10px; font-size:0.95em; color:#9c9; min-height:1.2em; }
        </style>
        <div class="qc-row">
          <button class="qc-btn" data-choice="A">A</button>
          <button class="qc-btn" data-choice="B">B</button>
          <button class="qc-btn" data-choice="C">C</button>
          <button class="qc-btn" data-choice="D">D</button>
        </div>
        <div class="qc-status"></div>
        <script>
        (function () {
          var buttons = document.querySelectorAll('.qc-btn');
          var status = document.querySelector('.qc-status');
          var submitted = false;
          buttons.forEach(function (btn) {
            btn.addEventListener('click', function () {
              if (submitted) return;
              submitted = true;
              var choice = btn.getAttribute('data-choice');
              buttons.forEach(function (b) { b.disabled = true; b.style.opacity = '0.5'; });
              btn.style.opacity = '1';
              btn.style.background = '#2d6a4f';
              fetch('https://docs.google.com/forms/d/e/1FAIpQLSeuAoyLtubfSinMFax9ZNpYQROztkgnQ0dr17WnwAyfb69-Cg/formResponse', {
                method: 'POST',
                mode: 'no-cors',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: 'entry.776396347=' + encodeURIComponent(choice),
              });
              status.textContent = 'Submitted: ' + choice;
            });
          });
        })();
        </script>
        """,
        width="100%",
        height="140px",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Nesting a `while` Loop Inside Another `while` Loop

    What if you don't know in advance how many times you'll need to
    repeat something? Say you want to keep collecting positive numbers
    *until their total reaches at least 20* — that calls for a `while`
    loop as the **outer** loop too.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    total = 0

    while total < 20:
        number = input('Enter a positive number: ')
        number = float(number)
        while number <= 0:
            print('Please follow directions!')
            number = input('Enter a positive number: ')
            number = float(number)
        print('Thanks for entering', number)
        total = total + number
        print('Running total:', total)
        print()

    print('Reached the target! Final total:', total)
    ```

    ```
    Enter a positive number: 8
    Thanks for entering 8.0
    Running total: 8.0

    Enter a positive number: -3
    Please follow directions!
    Enter a positive number: 9
    Thanks for entering 9.0
    Running total: 17.0

    Enter a positive number: 5
    Thanks for entering 5.0
    Running total: 22.0

    Reached the target! Final total: 22.0
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    The **inner** `while` is the same validation logic as before. What's
    new is the **outer** `while`: instead of a fixed count, it keeps
    going as long as `total` hasn't reached 20 — the same accumulator
    pattern from Class 5's
    [Calculating Running Sums](https://BU-EK125.github.io/EK125/class/Class5.html#calculating-running-sums).

    🚩 **Common mistake:** putting a statement that belongs to the
    *outer* loop inside the *inner* loop by mistake (or vice versa) —
    e.g. updating `total` inside the inner validation `while` instead of
    after it finishes.

    Today's GPP
    [Problem 6](https://BU-EK125.github.io/EK125/gpps/Class6_GPP.html#problem-6-nested-while-and-for-loops)
    builds on this "keep going while valid input keeps coming" idea.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Using `if` Inside a Loop

    So far every loop has repeated the *same* action every time. An
    `if` statement inside a loop lets the action change depending on
    the current value of the loop variable.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Example: Even and Odd Numbers

    The **modulus operator `%`** gives the remainder after division. If
    `n % 2 == 0`, `n` is even; otherwise it's odd.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    for n in range(10):
        if n % 2 == 0:
            print(n, "is even")
        else:
            print(n, "is odd")
    ```

    ```
    0 is even
    1 is odd
    2 is even
    3 is odd
    4 is even
    5 is odd
    6 is even
    7 is odd
    8 is even
    9 is odd
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    🚩 **Common mistake:** writing `if n = 0:` instead of
    `if n % 2 == 0:` — a single `=` *assigns* a value, `==` *compares*
    two values. Python raises a `SyntaxError` if you try this in an
    `if` statement, so it's easy to catch, but it's still the single
    most common typo when writing conditionals.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Randomness and Reproducibility

    Engineering results must be **repeatable** — but Python's `random`
    module is exactly how you get simulation, testing, and sampling. How
    do you make "random" reproducible?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Python's `random` module gives you **pseudo-random** numbers: they
    look random but are generated by a formula, stepping forward in a
    fixed sequence from a starting point called a **seed**. Run this a
    few times — the result changes each time, since no seed is set.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    import random

    print(random.randint(1, 6))  # simulates a die roll
    ```

    ```
    5
    ```
    (unseeded -- yours will be different, and so will the next run of this exact code)
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Set a **seed**, and the sequence becomes reproducible — same seed,
    same numbers, every run.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    random.seed(42)
    print(random.randint(1, 6))
    print(random.randint(1, 6))
    print(random.randint(1, 6))
    ```

    ```
    6
    1
    1
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    🚩 **Common mistake:** putting `random.seed()` *inside* a loop
    instead of before it. Watch what happens:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    print("Wrong -- seed inside the loop:")
    for i in range(3):
        random.seed(99)
        print(random.randint(1, 6))
    ```

    ```
    Wrong -- seed inside the loop:
    4
    4
    4
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    random.seed(5)
    print("Right -- seed once, before the loop:")
    for j in range(3):
        print(random.randint(1, 6))
    ```

    ```
    Right -- seed once, before the loop:
    5
    3
    6
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Seeding inside the loop resets the sequence back to the same
    starting point on *every single iteration* — same number, three
    times in a row — instead of three different ones. Seed once, at the
    very top of your program, before any of the random calls you
    actually want to vary.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Combining Loops with Random Numbers

    Now put loops and randomness together — simulate rolling a die 5
    times.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    random.seed(10)
    print("Rolling a die 5 times:")
    for k in range(5):
        roll = random.randint(1, 6)
        print(f"Roll {k + 1}: {roll}")
    ```

    ```
    Rolling a die 5 times:
    Roll 1: 5
    Roll 2: 1
    Roll 3: 4
    Roll 4: 4
    Roll 5: 5
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    - **Use a seed** when testing, debugging, building examples, or
      submitting homework that needs a specific output.
    - **Don't use a seed** for games or real applications where you
      actually want different outcomes every time.

    You'll extend this into a nested loop in today's GPP — see
    [Problem 8](https://BU-EK125.github.io/EK125/gpps/Class6_GPP.html#problem-8-simulating-multiple-trials-with-random-numbers).
    This is also exactly the bug behind Homework 4's *Seed Reset Bug*
    problem — now you've seen it happen live.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 🎯 Quick Check: Predict Before You Code

    You need `random.seed(42)` to produce the exact 3 trials shown
    above. Where should the seed call go?

    **A.** Once, before the trials loop

    **B.** Inside the trials loop, at the top of every trial

    **C.** Inside the inner loop, before every single random number

    **D.** Anywhere -- it doesn't affect the output

    📝 **Submit your answer below:**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.iframe(
        """
        <style>
          body { margin:0; padding:12px; background:#1a1a1a; font-family:-apple-system,sans-serif; }
          .qc-row { display:flex; gap:12px; }
          .qc-btn { flex:1; padding:14px; font-size:1.1em; font-family:monospace;
                    border-radius:8px; border:1px solid #555; background:#2a2a2a;
                    color:#eee; cursor:pointer; }
          .qc-status { margin-top:10px; font-size:0.95em; color:#9c9; min-height:1.2em; }
        </style>
        <div class="qc-row">
          <button class="qc-btn" data-choice="A">A</button>
          <button class="qc-btn" data-choice="B">B</button>
          <button class="qc-btn" data-choice="C">C</button>
          <button class="qc-btn" data-choice="D">D</button>
        </div>
        <div class="qc-status"></div>
        <script>
        (function () {
          var buttons = document.querySelectorAll('.qc-btn');
          var status = document.querySelector('.qc-status');
          var submitted = false;
          buttons.forEach(function (btn) {
            btn.addEventListener('click', function () {
              if (submitted) return;
              submitted = true;
              var choice = btn.getAttribute('data-choice');
              buttons.forEach(function (b) { b.disabled = true; b.style.opacity = '0.5'; });
              btn.style.opacity = '1';
              btn.style.background = '#2d6a4f';
              fetch('https://docs.google.com/forms/d/e/1FAIpQLSeuAoyLtubfSinMFax9ZNpYQROztkgnQ0dr17WnwAyfb69-Cg/formResponse', {
                method: 'POST',
                mode: 'no-cors',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: 'entry.1464395584=' + encodeURIComponent(choice),
              });
              status.textContent = 'Submitted: ' + choice;
            });
          });
        })();
        </script>
        """,
        width="100%",
        height="140px",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Summary

    - A **nested loop** is one loop inside another's action — `for`
      inside `for`, `while` inside `for`, `while` inside `while`, any
      combination.
    - The habit that matters most: **check which loop each line belongs
      to.** Indentation is the only thing telling you.
    - An `if` inside a loop lets the action *change* based on the loop
      variable, instead of repeating identically every time.
    - Python's randomness is **pseudo-random**: reproducible with a
      seed, genuinely varying without one. Use a seed for testing and
      debugging; skip it for real applications.

    📝 [Today's GPP](https://BU-EK125.github.io/EK125/gpps/Class6_GPP.html)
    """)
    return


if __name__ == "__main__":
    app.run()
