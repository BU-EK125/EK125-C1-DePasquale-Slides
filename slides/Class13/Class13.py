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
    skips it. Naming an argument lets you pass arguments in any order.
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

    **Immutable** values are always safe; **mutable** ones (lists,
    dicts) can really be changed in place by a function.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def modifyList(lst):
        lst.append(999)
        print(f"Inside: {lst}")
    myData = [1, 2, 3]
    modifyList(myData)
    print(f"Outside: {myData}")
    ```

    ```
    Inside: [1, 2, 3, 999]
    Outside: [1, 2, 3, 999]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## In-Class Creative Round: Mad Libs

    Work **by table**. Write one function, `mad_libs`, that fills a
    story template with your own funny words — the class votes on the
    funniest result.
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

    TEMPLATE = ("The {adj} {noun} loves to {verb} "
                "in the {place}.")
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
    ```

    Then build your own `CHOICES` dictionary (same shape as
    `WORD_BANK`'s keys, with an index into each list) and call
    `mad_libs(TEMPLATE, WORD_BANK, CHOICES)` with it.
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## How It's Judged

    Choose your own `CHOICES` to make the funniest story you can.
    That's the whole grade today: funniest story, by class vote.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Submission

    Submit **one notebook per table** — your function and CHOICES —
    through this form. We'll reuse the **same form** to vote on the
    funniest story.

    📝 [Submit and vote here](https://forms.gle/JpDvFxKsoRbSEf3Z8)
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

    `def` starts a header with name and parameters; `return` sends a value back.
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

    Python doesn't copy your data into a function — the parameter is
    just a new name for the same object, like a nickname.
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
    def createAccount(user, email, role="user"):
        return f"{user} ({email}): {role}"

    print(createAccount("alice", "a@x.com", "admin"))
    print(createAccount(user="bob", email="b@x.com"))
    ```

    ```
    alice (a@x.com): admin
    bob (b@x.com): user
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mutable vs. Immutable Data

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
    def tryToModify(x, s):
        x, s = x + 1, s.upper()
        print(f"Inside: x={x}, s={s}")
    num, string = 10, "hello"
    tryToModify(num, string)
    print(f"Outside: num={num}, string={string}")
    ```

    ```
    Inside: x=11, s=HELLO
    Outside: num=10, string=hello
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
        print(f"Inside: {lst}")
    myData = [1, 2, 3]
    modifyList(myData)
    print(f"Outside: {myData}")
    ```

    ```
    Inside: [1, 2, 3, 999]
    Outside: [1, 2, 3, 999]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Reassignment Doesn't Count

    Reassigning the parameter (`lst = []`) never touches the original —
    only in-place methods do.
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
    - Immutable arguments (numbers, strings, tuples) are always safe;
      mutable ones (lists, dicts) can be changed in place — but
      reassigning the parameter itself never escapes.

    Today's reading also covers variable scope, modular programs, and
    copying lists — worth reading on your own.

    📝 [Today's GPP](https://BU-EK125.github.io/EK125/gpps/Class13_GPP.html)
    """)
    return


if __name__ == "__main__":
    app.run()
