import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class13.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # User-Defined Functions

    ### Writing, Calling, and Passing Data to Your Own Functions

    *Class 13*

    📖 [Full reading: Class 13](https://BU-EK125.github.io/EK125/class/Class13.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Defining and Calling a Function

    Two reasons to write your own: reusing code, and building modular
    programs. `def` starts a function header with parameters in
    parentheses; `return` sends a value back out.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def sqrarea(sidelen):
        """This function calculates the area of a square."""
        return sidelen**2

    print(sqrarea(3))
    ```

    ```
    9
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Functions with No Return

    Not every function calculates something — some just perform a
    task. Even then, Python hands back a value by default: `None`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def printstrs(instr, n):
        for i in range(n):
            print(instr, end='')
        print()
    printstrs("Hi", 5)
    print(printstrs('a', 2))
    ```

    ```
    HiHiHiHiHi
    aa
    None
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Default and Keyword Arguments

    A parameter can have a default value, used only if the caller
    doesn't provide one. Naming an argument lets you skip defaults and
    pass arguments in **any order**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def greet(name, greeting="Hello"):
        print(f"{greeting}, {name}!")

    greet("Alice")
    greet(name="Bob", greeting="Hi")
    ```

    ```
    Hello, Alice!
    Hi, Bob!
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mutable vs. Immutable Arguments

    **Immutable** (numbers, strings, tuples) are always safe — any
    "change" makes a new object. **Mutable** ones (lists, dicts) can
    really be changed in place by a function.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def modifyList(lst):
        lst.append(999)
        lst[0] = "changed"
        print(f"Inside: {lst}")
    myData = [1, 2, 3]
    modifyList(myData)
    print(f"Outside: {myData}")
    ```

    ```
    Inside: ['changed', 2, 3, 999]
    Outside: ['changed', 2, 3, 999]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## In-Class Activity: Mad Libs Function Contest

    Time to write a real function from scratch. Work in groups of
    **three**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The Task

    Write one function, `mad_libs`, that fills in a story template.
    You're given a word bank (a dictionary of lists), a template
    string, and a `CHOICES` dictionary — your function returns the
    finished story.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    WORD_BANK = {
        "adj":   ["sneaky", "gigantic", "soggy"],
        "noun":  ["toaster", "llama", "professor"],
        "verb":  ["tango", "sneeze", "teleport"],
        "place": ["library", "volcano", "cafeteria"],
    }

    TEMPLATE = "The {adj} {noun} loves to {verb} in the {place}."
    CHOICES  = {"adj": 1, "noun": 0, "verb": 2, "place": 1}
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Write the Function

    Fill in `mad_libs` so it builds the story from `template`,
    `word_bank`, and `choices`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def mad_libs(template, word_bank, choices):
        story = template
        # your code here
        return story

    print(mad_libs(TEMPLATE, WORD_BANK, CHOICES))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ## Expected Output

    With the `CHOICES` above, your output should be:

    ```
    The gigantic toaster loves to teleport in the volcano.
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Requirements

    Your function must use all of the following:

    - A `for` loop over `choices.items()`, unpacking each pair as
      `(blank, index)`
    - A dictionary lookup into `word_bank`
    - A list index to select the word
    - The string method `.replace()`

    Don't hard-code any words from the word bank or template — your
    function must work for **any** valid `CHOICES`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Creative Round

    Choose your own `CHOICES` to produce the funniest story you can.
    Submit your `CHOICES` dictionary along with your function — the
    class will vote on the funniest result.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## How You'll Be Rated (100 points)

    - **Correctness (60)** — an autograder runs your function on
      hidden inputs, including a repeated blank and a template with no
      blanks.
    - **Required constructs (20)** — 5 points each for the `.items()`
      loop, the dictionary lookup, the list index, and `.replace()`.
    - **Readability (10)** — clear variable names and at least one
      comment explaining your approach.
    - **Creative submission (10)** — full credit for a valid `CHOICES`
      dictionary that runs without errors.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Bonus (up to 5 points)

    - Funniest story, by class vote
    - Most test cases passed on the first submission
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Submission

    Submit **one Colab notebook per group of three**, containing your
    function and your `CHOICES`, to the shared Google Drive folder —
    📁 *(link — add before class)*. ⏰ *(due date — add before class)*

    Your code must run without errors: a submission that crashes on
    the hidden tests receives no correctness credit, so test with
    several different `CHOICES` before submitting.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Appendix: Functions and Arguments, in Full

    ### The complete walkthrough behind today's 4 condensed slides

    Useful for review and for working through the GPP and homework —
    not covered live due to time.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Why Write Your Own Functions?

    Two big reasons: **reusing code** you'd otherwise repeat, and
    building **modular programs** — breaking a problem into pieces,
    each handled by its own function.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Defining a Function

    `def` starts a function header, followed by its name and
    parameters in parentheses. The docstring, a triple-quoted string,
    describes what it does; `return` sends a value back out.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def sqrarea(sidelen):
        """This function calculates the area of a square."""
        return sidelen**2

    print(sqrarea(3))
    ```

    ```
    9
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Returning Multiple Values

    `return` can only hand back **one** object — but that object can
    be a tuple, bundling several values together.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def sqrarea_perim(sidelen):
        """Calculates the area and perimeter of a square."""
        sqar = sidelen**2
        sqperim = 4 * sidelen
        return sqar, sqperim

    area, perim = sqrarea_perim(11)
    print(area, perim)
    ```

    ```
    121 44
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Functions with No Return

    Not every function calculates something — some just perform a
    task, like printing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def printstrs(instr, n):
        """This function prints instr n times."""
        for i in range(n):
            print(instr, end='')
        print()

    printstrs("Hi", 5)
    ```

    ```
    HiHiHiHiHi
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Every Function Returns *Something*

    Even with no `return` statement, a function still hands back a
    value by default.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    print(printstrs('a', 2))
    ```

    ```
    aa
    None
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    That default return value is `None` — Python doesn't leave a
    function truly empty-handed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Lambda Functions

    A `lambda` is a short, anonymous function — one expression, no
    `def`, no `return` statement needed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    times3 = lambda num: num * 3
    print(times3(11))
    ```

    ```
    33
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    A lambda's body is limited to a single expression — anything more
    complex needs a regular `def` function.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## How Arguments Get Into Functions

    When you call a function, Python doesn't copy your data — the
    parameter is just a **new name** for the same object, like a
    nickname. If "Liz" gets a haircut, "Elizabeth" does too, because
    they're the same person.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Default Parameter Values

    A parameter can have a default value, used only when the caller
    doesn't provide one — and parameters with defaults must come
    **after** ones without.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def greet(name, greeting="Hello"):
        print(f"{greeting}, {name}!")

    greet("Alice")
    greet("Bob", "Hi")
    ```

    ```
    Hello, Alice!
    Hi, Bob!
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Keyword Arguments

    Naming an argument when you call a function lets you skip defaults
    you want to keep, and give arguments in **any order**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def createAccount(username, email, role="user", active=True):
        return f"{username} ({email}): {role}, active={active}"

    print(createAccount("alice", "alice@x.com", "admin", False))
    print(createAccount(
        username="bob", role="admin", email="bob@x.com"
    ))
    ```

    ```
    alice (alice@x.com): admin, active=False
    bob (bob@x.com): admin, active=True
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Two Types of Data: Mutable and Immutable

    **Immutable** (can't change): numbers, strings, tuples.
    **Mutable** (can change): lists, dictionaries, sets.

    This distinction determines what a function can do to the data you
    pass it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Immutable Arguments Are Always Safe

    Any "change" to an immutable object inside a function creates a new
    object — the original is never touched.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def tryToModify(x, s, t):
        x = x + 1
        s = s.upper()
        t = t + (4,)
        print(f"Inside: x={x}, s={s}, t={t}")
    num, string, tup = 10, "hello", (1, 2, 3)
    tryToModify(num, string, tup)
    print(f"Outside: num={num}, string={string}, tup={tup}")
    ```

    ```
    Inside: x=11, s=HELLO, t=(1, 2, 3, 4)
    Outside: num=10, string=hello, tup=(1, 2, 3)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mutable Arguments Can Be Changed

    Mutable objects can be changed in place — `.append()` and index
    assignment both modify the original.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def modifyList(lst):
        lst.append(999)
        lst[0] = "changed"
        print(f"Inside: {lst}")
    myData = [1, 2, 3]
    modifyList(myData)
    print(f"Outside: {myData}")
    ```

    ```
    Inside: ['changed', 2, 3, 999]
    Outside: ['changed', 2, 3, 999]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Reassignment Doesn't Count

    Assigning a brand-new value to the parameter, `lst = []`, just
    creates a new local variable — in-place methods change the
    original, but reassignment never does.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def resetList(lst):
        lst = []
        print(f"Inside: {lst}")
    myData = [1, 2, 3]
    resetList(myData)
    print(f"Outside: {myData}")
    ```

    ```
    Inside: []
    Outside: [1, 2, 3]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Same Name, Different Variable

    A parameter can share a name with the variable you pass in — same
    object, two separate names.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def processGrades(grades):
        grades.append(100)
        print(f"Inside: {grades}")

    grades = [85, 90, 78]
    processGrades(grades)
    print(f"Outside: {grades}")
    ```

    ```
    Inside: [85, 90, 78, 100]
    Outside: [85, 90, 78, 100]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Summary

    - `def` starts a function; `return` sends one value back out —
      bundle several values in a tuple if you need more.
    - A function with no `return` still returns something: `None`.
    - `lambda` makes a quick, one-expression anonymous function.
    - Default and keyword arguments let callers skip values and pass
      arguments in any order.
    - Immutable arguments (numbers, strings, tuples) are always safe
      inside a function; mutable ones (lists, dicts) can be changed in
      place — but reassigning the parameter itself never escapes.

    Today's reading also covers variable scope, modular programs, and
    copying lists — worth reading on your own.

    📝 [Today's GPP](https://BU-EK125.github.io/EK125/gpps/Class13_GPP.html)
    """)
    return


if __name__ == "__main__":
    app.run()
