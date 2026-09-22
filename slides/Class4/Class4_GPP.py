import marimo

__generated_with = "0.24.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class4_GPP.slides.json",
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
        # Class 4 GPP: Coding Basics Wrap-up and Selection Statements

        **Group Exercise (Teams of 3)**

        Work together to complete the following tasks!

        📖 [Full reading: Class 4](https://BU-EK125.github.io/EK125/class/Class4.html)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Part 1: f-strings, escape characters, the `input()` function and type casting

        We'll do a few exercises to make sure that this critical coding
        principles, that we *have* seen over the last two weeks, are fresh
        in your mind!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("### Problem 1.1: Table of average of material length")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        '''
        Write a program that:

        - Uses `input()` to ask for a material name (string).
        - Uses `input()` to ask for three beam lengths in meters (floats).
        - Formats the material name in uppercase.
        - Prints a table of beam lengths, each:
          - Width of 10 characters (using a `f-string`)
          - 3 decimal places (using a `f-string`)
          - Right-aligned with units m (using a `f-string`)
        - Also prints the average length, formatted to 2 decimal places. (using a `f-string`)

        An example run looks like this

        ```
        Enter material: steel
        Enter beam length 1 (m): 3.2
        Enter beam length 2 (m): 3.1
        Enter beam length 3 (m): 4.5

        Beam Fabrication Report
        -----------------------
        Material: STEEL

        Beam Lengths:
        Beam 1:     3.200 m
        Beam 2:     3.100 m
        Beam 3:     4.500 m
        -----------------------
        Average:      3.60 m
        ```

        Note that you might need to type cast your inputs to make sure
        everything comptues!
        '''
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("### Problem 1.2: Series Resistor Voltage Report")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        '''
        Write a Python program that:

        1. Prompts the user to enter **two resistors**, including:
           - The **name** of each resistor (string)
           - The **resistance in ohms** (integer)

        2. Prompts the user to enter the **current in amps** (float), which is the same through both resistors in series.

        3. Calculates:
           - The **voltage across each resistor** using Ohm's Law:
             ```
             V = I * R
             ```
           - The **total voltage** across both resistors:
             ```
             V_total = V1 + V2
             ```

        4. Prints a **formatted report** including:
           - Each resistor's name in **uppercase**
           - Resistance using the word `"ohms"`
           - Current with **3 decimal places**
           - Voltage with **2 decimal places**
           - Columns aligned using **`\\t`**
           - A title and separator lines using **`\\n`**

        **Example run:**
        ```
        Enter name of resistor 1: R1
        Enter resistance of R1 (ohms): 220
        Enter name of resistor 2: R2
        Enter resistance of R2 (ohms): 330
        Enter current (amps): 0.125

        SERIES RESISTOR REPORT
        -----------------------------
        Name        Resistance    Current    Voltage
        R1          220 ohms      0.125 A   27.50 V
        R2          330 ohms      0.125 A   41.25 V
        -----------------------------
        Total Resistance: 550 ohms
        Total Voltage:    68.75 V
        ```

        **Notes:**
        - Use `int()` to convert resistances to integers.
        - Use `float()` to convert current to a floating-point number.
        - Use f-strings for all formatted output.
        - Use escape characters `\\n` for new lines and `\\t` for column alignment.
        '''
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("## Part 2: Basic selection statements")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Sometimes, we want to be able to decide whether or not to run a line
        or a block of code. Statements that accomplish this are called
        **selection** statements. We are going to focus on `if` and
        `if-else` statements here, but python includes additional selection
        statements, too.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        '''
        The `if` statement chooses whether statement(s) are executed or not.
        The syntax of an `if` statement is as follows:

        ```python
          if condition:
            action
          rest of code
        ```

        "condition" is an expression that must evaluate to `True` or
        `False`. "action" must be intented. It is only executed if the
        condition is true. Otherwise, it is skipped.
        '''
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("Here's an example. Try it with several different ages.")
    return


@app.cell
def _():
    age_s = 27  # originally: int(input('What is your age? \t'))
    print(int(age_s))
    if age_s < 30:
        print('Never trust anyone over 30')
    print('And the code moves on')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Indentation is very important in Python. If you want more than one
        line of code included as part of your action in an `if` statement,
        those lines must all be indented to the same level. Try running
        these two short programs.
        """
    )
    return


@app.cell
def _():
    num = 12  # originally: int(input('Please enter an integer: '))
    if num > 10:
        print(num)
        print('Thanks!')
    print('Done!')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        '''
        **Now try this one** — same idea, but look closely at the indentation:

        ```python
        num = int(input('Please enter an integer: '))
        if num > 10:
            print(num)
         print('Thanks!')
        print('Done!')
        ```

        ```
        IndentationError: unindent does not match any outer indentation level
        ```

        *`print('Thanks!')` is indented by only one space — Python can't
        match it to any enclosing block, so the whole file fails to parse.*
        '''
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        '''
        We can also choose between conditions using `if-else` statements.
        The general form is

        ```python
          if condition:
            ifaction
          else:
            elseaction
        # rest of code
        ```

        This code will choose between two actions, "ifaction" and
        "elseaction" depending on whether or not the condition is `True`.

        Here's an example. Try it out.
        '''
    )
    return


@app.cell
def _():
    name = "Christine"  # originally: input('Please enter your name: ')
    if name.lower() == 'arthur':
        print('You are the king of the Britons!')
    else:
        print('You are a brave knight on a quest for the Holy Grail!')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "So far, we've been comparing the values of numbers to one another "
        "for our condition, but the condition can be any statement that "
        "would evaluate to `True` or `False`."
    )
    return


@app.cell
def _():
    # note: the original notebook is missing the colon after `else` here
    # (its own saved output is stale from before that typo) — restored below
    string = "G"  # originally: input('Please enter a single character: ')
    if string.isalpha():
        print('This character is a letter.')
    else:
        print('This character is not a letter.')
    print('Done.')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("### Problem 2.1: Code fix!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "Fix the code above (starting with "
        "`num=int(input('Please enter an integer: '))`) so that it will "
        "run. The line that prints \"Thanks!\" should not be part of the "
        "`if` statement this time."
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("### Problem 2.2: Prize Number Generator")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        '''
        Instead of soliciting user input, we could also use a random number
        as an input to test. Very soon we will talk about better ways to
        generate *real* random numbers, but for now, we'll stick with a more
        brute force approach.

        Write a Python program that generates a "random-ish" number between
        1 and 100 **without using any imports**. (We will cover imports in
        Week3B).

        Your program should:

        1. Ask the user to type something unpredictable (letters, numbers, or a mix).
        2. Convert the user input into a number between 1 and 100 using a simple calculation (for example, using the length of the input).
        3. Print the generated number.
        4. Check if the number is smaller than 5.
           - If it is, print a message telling the user they have won a prize.
           - Otherwise, print a message saying there is no prize.

        **Example run:**
        ```
        Type something random: hello
        The generated number is: 5
        Sorry, no prize this time.
        ```
        ```
        Type something random: a
        The generated number is: 1
        Congratulations! You won a prize!
        ```

        **Hints:**
        - Use `len()` to get the length of the input.
        - Use arithmetic (`%`, `+`) to keep the number in the 1–100 range.
        - Use an `if/else` statement to check if the number is smaller than 5.
        - Use `print()` to display messages.
        '''
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("### Problem 2.3: Number Sign Checker")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        '''
        Write a Python program that asks the user to enter a number.

        The program should then determine whether the number is
        **positive**, **negative**, or **zero**, and print an appropriate
        message.

        **Example run:**
        ```
        Enter a number: 7
        The number is positive.
        ```
        ```
        Enter a number: -3
        The number is negative.
        ```
        ```
        Enter a number: 0
        The number is zero.
        ```

        **Hints:**
        - Use `int()` to convert the user input to an integer.
        - Use an `if/elif/else` statement to check the conditions.
        - Use `print()` to display the result.
        '''
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("## Part 3: Nested selection statements")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "Note that we can also nest selection statements. If you want to "
        "check a second condition after a first condition is met, you can "
        "do that. Just add another `if` statement as part of the action of "
        "the first `if`."
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("### Problem 3.1")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        "Try modifying the above code "
        "(`string=input('Please enter a single character: ')`) to check if "
        "the letter entered is uppercase. If it is, change it to lowercase "
        "and print it."
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ### More on nested selection statements

        It is also possible to nest `if/else` statements so you can check
        multiple conditions.

        For example, let's say we wanted to check to see if a given year
        was a leap year. Leap years must be divisible by 4, unless they are
        century years, then they must also be divisible by 400. The code to
        check a user input year would look like this. Try it out.
        """
    )
    return


@app.cell
def _():
    year = 2000  # originally: int(input("Enter a year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('Leap year!')
            else:
                print('Not a leap year.')
        else:
            print('Leap year!')
    else:
        print('Not a leap year.')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("This type of statement can be simplified using the `elif` keyword.")
    return


@app.cell
def _():
    # Prompt the user for the number of limbs lost
    limbs_lost = 3  # originally: int(input("Enter the number of limbs the Black Knight has lost: "))

    # Determine the message to print
    if limbs_lost == 0:
        message = "The Black Knight says: 'None shall pass!'"
    elif limbs_lost == 1:
        message = "The Black Knight says: 'It's just a flesh wound!'"
    elif limbs_lost == 2:
        message = "The Black Knight says: 'I've had worse!'"
    elif limbs_lost == 3:
        message = "The Black Knight says: 'Come on, you pansy!'"
    else:
        message = "The Black Knight says: 'Alright, we'll call it a draw.'"

    # Print the message
    print(message)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("### Problem 3.2: Classify ages")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Write an age group classifier using the `elif` keyword.

        - Prompt the user for an age
        - Classify the person based on age ranges:
          - 0-12 = child
          - 13-19 = teen
          - 20-64 = adult
          - 65 and over = senior.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("### Problem 3.3: Selections AND booleans")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        '''
        In **Week 2**, we learned about *booleans* and the boolean
        relational operators: `==`, `!=`, `<`, `>`, `<=`, `>=`, `not`,
        `and`, and `or`. Using those operators.

        Write a Python program that asks the user to enter:
        - The number of cats
        - The number of dogs

        Then use **booleans** and the boolean relational operators (`==`,
        `!=`, `<`, `>`, `<=`, `>=`, `not`, `and`, `or`) to compare the two
        values.

        Your program should print messages according to the following
        rules:

        1. If there is at least one cat, print `Squeee!`
        2. If there are 5 cats or more, print `Purr...`
        3. If there are 5 dogs or more, print `Arf!`
        4. If there are either more than 10 cats **or** more than 10 dogs, print `Where frends?`
        5. If there are more than 10 cats **and** more than 10 dogs, print `Frends!`
        6. If there are exactly as many cats as dogs, print `Perfection.`

        To get practice with more boolean logic, also add these extra checks:
        7. If the number of cats and dogs is **not equal**, print `Not balanced.`
        8. If there are fewer cats than dogs, print `More dogs than cats.`
        9. If there are at least twice as many cats as dogs, print `Cats rule!`
        10. If there are at least twice as many dogs as cats, print `Dogs rule!`
        11. If there are **no cats and no dogs** (zero of both), print `No pets at all!`

        **Example run:**
        ```
        Enter the number of cats: 12
        Enter the number of dogs: 12
        Squeee!
        Purr...
        Arf!
        Where frends?
        Frends!
        Perfection.
        ```

        **Requirements:**
        - Use at least **6 different boolean operators** (`==`, `!=`, `<`, `>`, `<=`, `>=`, `not`, `and`, `or`) in your solution.
        - Each rule should be checked with an `if` statement (not `elif`), because more than one condition may be true.
        '''
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("### Problem 3.4: Combining selection, f-strings and everything else!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        '''
        Write a Python program that solves a quadratic equation of the form:

        ```
        ax^2 + bx + c = 0
        ```

        Your program should:

        1. Prompt the user to enter the coefficients `a`, `b`, and `c`.
        2. Compute the **discriminant** using the formula:
           ```
           discriminant = b^2 - 4ac
           ```
        3. Handle the three possible cases for the discriminant:
           - If the discriminant is **positive**, print two different real roots.
           - If the discriminant is **zero**, print one real root (both roots are the same).
           - If the discriminant is **negative**, print two complex roots (with a real and an imaginary part).

        **Important Note:**
        - Calculate square roots using exponentiation with `**0.5`.
          For example, the square root of `x` can be computed as:
          ```
          x**0.5
          ```

        **Example run (discriminant > 0):**
        ```
        Enter coefficient a: 1
        Enter coefficient b: -3
        Enter coefficient c: 2
        The roots are real and different: 2.00 and 1.00
        ```

        **Example run (discriminant == 0):**
        ```
        Enter coefficient a: 1
        Enter coefficient b: 2
        Enter coefficient c: 1
        The root is real and the same: -1.00
        ```

        **Example run (discriminant < 0):**
        ```
        Enter coefficient a: 1
        Enter coefficient b: 2
        Enter coefficient c: 5
        The roots are complex: -1.00 ± 2.00i
        ```
        '''
    )
    return


if __name__ == "__main__":
    app.run()
