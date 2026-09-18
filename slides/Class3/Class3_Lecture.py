import marimo

__generated_with = "0.24.0"
app = marimo.App(
    width="full",
    layout_file="layouts/Class3_Lecture.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Boolean Logic

    ### Naming, Operators, and Truth Tables

    *Class 3*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Why Booleans?
    """)
    return


@app.cell
def _():
    # From the reading's "Introduction to Booleans" (Class3.html)
    flagA = True
    flagB = False
    print(type(flagA))  # <class 'bool'>
    print(isinstance(flagA, bool))  # True
    print(int(flagA))  # 1
    print(int(flagB))  # 0
    (flagA, flagB)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    A `bool` is its own type, not just 0/1 — but Python quietly treats
    `True` as `1` and `False` as `0` whenever you do arithmetic with them.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Naming Booleans Like Questions

    The reading's five go-to prefixes:

    - `is` → `isAdult`, `isActive`
    - `has` → `hasInsurance`, `hasPermission`
    - `can` → `canEdit`, `canWithdraw`
    - `should` → `shouldRetry`, `shouldExit`
    - `will` → `willExpire`, `willOverwrite`

    A good Boolean name reads like a yes/no question.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Poor Naming vs. Good Naming
    """)
    return


@app.cell
def _():
    # From the reading's "Before/After" naming example (Class3.html)
    personAge = 25
    dayOfWeek = "saturday"
    weatherData = {"precipitation": 0.2}

    # Poor names
    adult = (personAge >= 18)
    weekend = dayOfWeek in ["saturday", "sunday"]
    rain = weatherData["precipitation"] > 0

    # Better names — each one reads as a question
    isAdult = (personAge >= 18)
    isWeekend = dayOfWeek in ["saturday", "sunday"]
    isRaining = weatherData["precipitation"] > 0

    (isAdult, isWeekend, isRaining)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Same values, same logic — `isAdult`/`isWeekend`/`isRaining` just tell you
    **what they mean** without reading the code that computed them.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Your Turn

    Adapted from this week's practice notebook — each line computes a
    perfectly good Boolean, but the variable name hides what it means.
    Rename each one so it reads as a question:

    ```python
    weather = (precipitation > 0)
    user = (currentUser is not None)
    data = (len(searchResults) > 0)
    ```

    *What should each variable actually be called?*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Comparison Operators

    Straight from the reading's operator reference:

    | Operator | Meaning | Example |
    |----------|---------|---------|
    | `==` | Equal to | `(5 == 5)` → `True` |
    | `!=` | Not equal to | `(5 != 3)` → `True` |
    | `>` | Greater than | `(7 > 3)` → `True` |
    | `<` | Less than | `(2 < 8)` → `True` |
    | `>=` | Greater than or equal | `(5 >= 5)` → `True` |
    | `<=` | Less than or equal | `(3 <= 7)` → `True` |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Comparing Values
    """)
    return


@app.cell
def _():
    # From the reading's "Comparing Numbers" / "Chaining Comparisons" (Class3.html)
    age = 20
    print(age >= 18)  # True

    name1, name2 = "Alice", "Bob"
    print(name1 < name2)  # True — alphabetical

    score = 85
    print(80 <= score < 90)  # True — a chained comparison

    (age, score)
    return age, score


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `80 <= score < 90` is really `(80 <= score) and (score < 90)` — Python
    just lets you chain it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## `and` — Everything Must Be True
    """)
    return


@app.cell
def _():
    # From the reading's "AND Operator" (Class3.html)
    hasLicense = True
    hasInsurance = True
    hasRegistration = True
    canDrive = hasLicense and hasInsurance and hasRegistration
    canDrive
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `and` is only `True` when **every** part is `True`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## `or` — Any One Will Do
    """)
    return


@app.cell
def _():
    # From the reading's "OR Operator" (Class3.html)
    isDayOff = False
    isHoliday = True
    isSick = False
    canSleepIn = isDayOff or isHoliday or isSick
    canSleepIn
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `or` is `True` as soon as **any** part is `True`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## `not` — Flips It
    """)
    return


@app.cell
def _():
    # From the reading's "NOT Operator" (Class3.html)
    isOvercast = False
    isSunny = not isOvercast
    isSunny
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `not` just flips `True` to `False` and back.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Truth Tables

    | A | B | `A and B` | `A or B` |
    |---|---|-----------|----------|
    | T | T | T | T |
    | T | F | F | T |
    | F | T | F | T |
    | F | F | F | F |

    *This week's GPP asks you to build one of these by hand for the login
    validator before you touch any code.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Operator Precedence
    """)
    return


@app.cell
def _():
    # From the reading's "Operator Precedence" (Class3.html)
    result1 = not True or False and True
    result2 = (not True) or (False and True)  # same thing, spelled out
    (result1, result2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `not` binds tighter than `and`, which binds tighter than `or` — but
    parenthesize anyway. Nobody wants to re-derive this at 1am.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Short-Circuit Evaluation
    """)
    return


@app.cell
def _():
    # From the reading's "Short-Circuiting" (Class3.html)
    def expensiveFunction():
        print("This is expensive to compute!")
        return True

    hasPermission = False
    result = hasPermission and expensiveFunction()
    result
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `expensiveFunction()` never even runs — once `hasPermission` is
    `False`, `and` already knows the answer.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Truthy and Falsy — Why We Compare Explicitly
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Straight from the reading's list:

    **Falsy values:** `False`, `0`, `0.0`, `0j`, `"\"`, `''`, `[]`, `()`, `{}`, `None`

    **Truthy values:** everything else.
    """)
    return


@app.cell
def _(score):
    # From the reading's "Truthy and Falsy Values" (Class3.html)
    items = []
    print(items == [])  # explicit — always correct

    name = ""
    print(not name)  # True — an empty string is falsy

    bool(score)  # True — but why leave it implicit?
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Every one of these *works* without an explicit comparison — but each one
    is silently leaning on truthiness instead of saying what you actually
    mean. This is exactly why the GPP insists on `== True` and `== False`
    everywhere.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Bonus: The Ternary Operator
    """)
    return


@app.cell
def _(age):
    # From the reading's "Ternary Operator" (Class3.html)
    status = "adult" if (age >= 18) else "minor"
    status
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    A one-line `if`/`else` for when you just need a value, not an action.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Recap

    - **Name things so they explain themselves** — a reader shouldn't have to
      trace through logic to figure out what a variable means
    - **Be explicit, not implicit** — say exactly what you mean instead of
      leaning on hidden or default behavior
    - **Reason through logic on paper before you code it** — pseudocode and
      truth tables let you verify your thinking first
    - **Build complex logic from small, well-named pieces** — a handful of
      clear Booleans combine more safely than one tangled expression
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## How This Shows Up in Today's GPP

    - **Weather Decision System** → `and`/`or` combining multiple conditions
    - **Grade Calculator** → compound `and`/`or` conditions, explicit `== True` checks
    - **Login Validator** → building a truth table by hand for `canLogin`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Preview: Simple if/else Decisions

    *From this week's Homework Help Session*

    ---
    # Technique 1: Simple if/else Decisions

    ## Problem: Compare Two Scores

    **Given:**
    ```python
    aliceScore = 85
    bobScore = 78
    ```

    **Task:** Determine if Alice has the higher score.

    ---

    ### 🤔 Let's Think Through This:

    **Question 1:** What comparison do we need to make?

    **Question 2:** What are the two possible outcomes?

    **Question 3:** How do we handle each outcome differently?

    ---

    ### ✍️ Pseudocode:

    ```
    COMPARING SCORES:
    1. Create Boolean: aliceWon = (Alice's score > Bob's score)
    2. IF aliceWon == True THEN
         winner = "Alice"
    3. ELSE
         winner = "Bob"
    4. Print winner
    ```

    ---

    ### 💻 Now Let's Code It:
    """)
    return


@app.cell
def _():
    # From this week's Homework Help Session — Technique 1
    aliceScore = 85
    bobScore = 78

    aliceWon = (aliceScore > bobScore)
    print(f"Alice wins?: {aliceWon}")

    if aliceWon == True:
        winner = "Alice"
    else:
        winner = "Bob"

    print(f"Winner: {winner}")

    (aliceWon, winner)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `if`/`else` uses the Boolean you just built to actually **do** "
        "something — that's next class.
    """)
    return


if __name__ == "__main__":
    app.run()
