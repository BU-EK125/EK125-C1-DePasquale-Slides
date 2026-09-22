import marimo

__generated_with = "0.24.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class6_GPP.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # Class 6 GPP: Nested `for` Loops

        **Group Exercise (Teams of 3)**

        Work together to complete the following tasks!

        📖 [Full reading: Class 6](https://BU-EK125.github.io/EK125/class/Class6.html)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("### Problem 1: Worked example with nested `for` loops")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("Let's start with nested `for` loops using the `range()` function. Execute the following code.")
    return


@app.cell
def _():
    for i in range(1, 4):
        for j in range(4):
            print(i, j)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("### Problem 2: Formatted output with nested loops")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Your task is to practice nested loops by writing a Python program
        that generates a simple pattern.

        - Loop over the numbers 0 through 4.
        - On each line, first print the number, followed by a colon (`:`).
        - After the colon, print as many asterisks (`*`) as the number itself.

        **Example Output:**
        ```
        0:
        1:*
        2:**
        3:***
        4:****
        ```

        Hint: you'll need a loop inside a loop — the outer loop handles
        the numbers, and the inner loop handles printing the stars.

        This is the same shape as the number/star examples in the
        reading's
        [Nested loops](https://BU-EK125.github.io/EK125/class/Class6.html#nested-loops)
        section.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## 🎯 Quick Check: Predict Before You Code

        For row `num = 3` (which should print `3:***`), which inner loop
        is correct?

        **A.** `for i in range(num):`

        **B.** `for i in range(num + 1):`

        **C.** `for i in range(num - 1):`

        **D.** `for i in range(1, num):`

        📝 **Submit your answer below:**
        """
    )
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
    mo.md("### Problem 3: Looping Through a List to Print Element Types")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Write a Python program that prints the type of each element in a
        list.

        - Use a `for` loop together with the `range()` function to go
          through the list.
        - Do not assume you know how many items are in the list — your
          code should work for lists of any length.
        - Inside the loop, use the loop variable as an index to access
          each element of the list, and print out its type.

        ```python
        mylist = [43, 'happy', 3 < 5, 11.11]
        ```

        Need a refresher? Class 5's reading covers index-based iteration
        in
        [Looping with Indices](https://BU-EK125.github.io/EK125/class/Class5.html#looping-with-indices),
        and uses `type()` in the
        [Looping through sequences](https://BU-EK125.github.io/EK125/class/Class5.html#looping-through-sequences)
        example.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("### Problem 4: Printing Exclamation Point Patterns")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Write a Python program that uses *nested* `for` loops to print
        rows of exclamation points (`!`) based on a list of positive
        integers.

        - For each number in the list, print a row of exclamation points
          equal to that number (e.g. `3` → `!!!`).
        - Each row should have no spaces between the exclamation points.
        - Write your solution in two ways:
          - **Approach 1:** loop through the elements of the list directly.
          - **Approach 2:** loop through the *indices* of the list, and
            access elements by indexing.

        ```python
        intlist = [3, 7, 2, 1, 5]
        ```

        Approach 2 needs the same index-based iteration as Class 5's
        [Looping with Indices](https://BU-EK125.github.io/EK125/class/Class5.html#looping-with-indices)
        section.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("### Problem 5: Printing Characters from Strings with Separators")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Use the following list of strings. Write code to print all of
        the characters from all of the strings on one line, with a dash
        (`-`) after each.

        ```python
        strlist = ['I', 'love', 'coding!']
        ```

        The reading's
        [Nested loops](https://BU-EK125.github.io/EK125/class/Class6.html#nested-loops)
        section opens with a similar nested loop over a list of words,
        printing each word's characters.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("### Problem 6: Nested `while` and `for` loops")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Write a script that will prompt the user for positive numbers.
        As long as the user is entering positive numbers, print `Ni!`
        that many times on a single line for each. For example, if the
        user enters `3`, `Ni!Ni!Ni!` would be printed.

        This combines two ideas from the reading's
        [Nested loops](https://BU-EK125.github.io/EK125/class/Class6.html#nested-loops)
        section: an outer loop that keeps going as long as valid input
        keeps coming (see
        [Nesting a `while` Loop Inside Another `while` Loop](https://BU-EK125.github.io/EK125/class/Class6.html#nesting-a-while-loop-inside-another-while-loop)),
        and an inner loop that repeats a fixed number of times based on
        a value, like the number/star examples earlier in the same
        section.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("### Problem 7: Triangle of stars")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Prompt the user for a positive integer `n`. Then print a
        triangle of stars, starting with 0 in the first row and
        incrementing to `n-1` stars in the `n-1`st row.

        **Example output for `n=4`:**
        ```
        *
        **
        ***
        ```

        Same loop shape as the reading's
        [Nested loops](https://BU-EK125.github.io/EK125/class/Class6.html#nested-loops)
        section — just combined with `input()` to get `n` instead of a
        hardcoded range.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("### Problem 8: Simulating Multiple Trials with Random Numbers")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Engineers often need to test systems multiple times with random
        inputs to find bugs or verify performance.

        Write a program that:
        - Uses `random.seed(42)` for reproducibility
        - Simulates **3 trials**
        - In each trial, generates **4 random integers** between -5 and
          5 (inclusive)
        - Prints all 4 numbers on one line for each trial
        - Uses nested loops (outer loop for trials, inner loop for
          random numbers)

        **Expected Output** (with seed=42):
        ```
        Trial 1: 5 -4 -5 -1
        Trial 2: -2 -2 -3 -4
        Trial 3: 5 3 -4 4
        ```

        **Hint:** import the `random` module and use
        `random.randint(-5, 5)` to generate each number.

        See Class 6's own
        [Combining Loops with Random Numbers](https://BU-EK125.github.io/EK125/class/Class6.html#combining-loops-with-random-numbers)
        section, and Class 5's
        [Tracking Multiple Trials in One Loop](https://BU-EK125.github.io/EK125/class/Class5.html#tracking-multiple-trials-in-one-loop)
        section for a related (though non-nested) version of this
        pattern.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## 🎯 Quick Check: Predict Before You Code

        You need `random.seed(42)` to produce the exact 3 trials shown
        above. Where should the seed call go?

        **A.** Once, before the trials loop

        **B.** Inside the trials loop, at the top of every trial

        **C.** Inside the inner loop, before every single random number

        **D.** Anywhere -- it doesn't affect the output

        📝 **Submit your answer below:**
        """
    )
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


if __name__ == "__main__":
    app.run()
