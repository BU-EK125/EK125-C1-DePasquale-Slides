import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class14.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Scripts, File I/O, and the Local File Environment

    ### Running Programs Outside the Notebook

    *Class 14*

    📖 [Full reading: Class 14](https://BU-EK125.github.io/EK125/class/Class14.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Before We Start: Picking Up From Class 13

    A quick recap, a few details we skipped, and variable scope — all
    things we didn't get to in Class 13 — before moving on to today's
    topic.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Quick Recap: Functions

    `def` starts a function header with its parameters; `return` sends
    a value back out. The **docstring** — a string right after the
    header — is a one-sentence description of what the function does.
    Parameters can also have **default values**, used only when the
    caller doesn't provide one.

    📖 [GPP: Adding Docstrings](https://BU-EK125.github.io/EK125/gpps/Class14_GPP.html#problem-2-adding-docstrings-to-functions)
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
    ## Lambda Functions

    A `lambda` is a short, anonymous function — one expression, no
    `def`, no `return` statement needed.

    📖 [GPP Part 7: Lambda Functions](https://BU-EK125.github.io/EK125/gpps/Class13_GPP.html#part-7-lambda-functions)
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
    ## How Arguments Get Into Functions

    Python doesn't copy your data into a function — the parameter is
    just a new name for the same object, like a nickname. That's the
    key fact variable scope builds on next.

    📖 [GPP Part 1: Parameter Passing](https://BU-EK125.github.io/EK125/gpps/Class13_GPP.html#part-1-understanding-parameter-passing)
    📝 [HW7 Problem 6: Mutable vs. Immutable Arguments](https://BU-EK125.github.io/EK125/homework/HW7.html#problem-6-mutable-vs-immutable-arguments)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def show_identity(data):
        print("Same object as outside?", data is myList)

    myList = [1, 2, 3]
    show_identity(myList)
    ```

    ```
    Same object as outside? True
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Counter-Example: Reassigning Breaks the Nickname

    `data = []` doesn't change what `myList` points to outside — it
    just points `data` at a brand-new object instead.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def reset(data):
        data = []
        print("Same object as outside?", data is myList)

    myList = [1, 2, 3]
    reset(myList)
    print("Outside is still:", myList)
    ```

    ```
    Same object as outside? False
    Outside is still: [1, 2, 3]
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Scope Is Like *Inception*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.Html(
        '''
        <div style="display: flex; align-items: center; gap: 28px;">
          <img src="inception_poster.jpg" style="max-height: 320px;
               border-radius: 8px; flex-shrink: 0;">
          <p style="margin: 0; font-size: 30px; line-height: 1.3;
             color: #ddd;">
            A dream within a dream within a dream — each level has its
            own rules, and you can see back out to an outer level, but
            an outer level can't see into an inner one. A function
            call works the same way: each one opens its own level,
            nested functions can see out to the ones enclosing them,
            and once a level ends, everything inside it is gone for
            good.
          </p>
        </div>
        '''
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Variable Scope: What Is It?

    A variable's **scope** is where it's valid. Every function gets its
    own symbol table when it's called — once the function finishes,
    that table (and everything in it) is gone.

    📖 [GPP Part 5: Variable Scope](https://BU-EK125.github.io/EK125/gpps/Class13_GPP.html#part-5-variable-scope-legb-rule)
    📝 [HW7 Problem 5: Local Scope](https://BU-EK125.github.io/EK125/homework/HW7.html#problem-5-local-scope)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def sqrarea(sidelen):
        sqar = sidelen**2
        return sqar

    area = sqrarea(4)
    print(sqar)
    ```

    ```
    NameError: name 'sqar' is not defined
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The LEGB Rule

    Looking up a name, Python checks four scopes in order:

    1. **Local** — inside the current function
    2. **Enclosing** — in any function this one is nested inside
    3. **Global** — at the module level
    4. **Built-in** — Python's own names
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    x = "global"

    def outer():
        x = "enclosing"
        def inner():
            x = "local"
            print(x)
        inner()
        print(x)

    outer()
    print(x)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    local
    enclosing
    global
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Three separate variables, all named `x` — Python always resolves a
    name to the **closest** scope that defines it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## GPP Solution: Problem 5.2

    The GPP asks you to predict this same kind of nested-scope lookup
    before running it — same shape as the example above, different
    variable name.

    📖 [GPP Part 5](https://BU-EK125.github.io/EK125/gpps/Class13_GPP.html#part-5-variable-scope-legb-rule)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    x = 10

    def outer():
        x = 20
        def inner():
            print(f"Inner sees x = {x}")
        inner()
        print(f"Outer sees x = {x}")

    outer()
    print(f"Global sees x = {x}")
    ```

    ```
    Inner sees x = 20
    Outer sees x = 20
    Global sees x = 10
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Reading a Global Is Easy

    A function can freely **read** a variable from an outer scope — no
    special syntax needed. Notice `taxRate` below is **not** a
    parameter — `price` is passed in because it's different on every
    call, while `taxRate` is just read from global scope.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    taxRate = 0.08

    def calculateTotal(price):
        return price * (1 + taxRate)

    print(calculateTotal(100))
    ```

    ```
    108.0
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Pass It, or Read It as a Global?

    - **Pass it as an argument** when the value is different on every
      call, or you want the function reusable and testable on its
      own, independent of outside state.
    - **Read it as a global** when it's a fixed constant or shared
      setting for the whole program — a tax rate, a config value — and
      passing it to every function that needs it would just be
      repetitive.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Gotcha: Assigning Creates a New Local

    If a function **assigns** to a name anywhere in its body, Python
    treats that name as local for the *entire* function — even on a
    line that reads it before the assignment happens.

    📖 [GPP Problem 5.1: Fix the Broken Code](https://BU-EK125.github.io/EK125/gpps/Class13_GPP.html#part-5-variable-scope-legb-rule)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    count = 0

    def increment():
        count = count + 1  # reads 'count' before assigning it
        print(count)

    increment()
    ```

    ```
    UnboundLocalError: cannot access local variable 'count'
    where it is not associated with a value
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## GPP Solution: Problem 5.1

    The GPP's own broken code hits this exact `UnboundLocalError` — the
    fix below avoids `global` entirely by **returning** the updated
    count and reassigning it in the caller, the preferred style for
    this kind of state-tracking.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    studentsProcessed = 0

    def processStudent(name, count):
        print(f"Processing {name}")
        count = count + 1
        return count

    studentsProcessed = processStudent("Alice", studentsProcessed)
    studentsProcessed = processStudent("Bob", studentsProcessed)
    studentsProcessed = processStudent(
        "Charlie", studentsProcessed)
    print(f"Total processed: "
          f"{studentsProcessed}")
    ```

    ```
    Processing Alice
    Processing Bob
    Processing Charlie
    Total processed: 3
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The `global` Keyword

    To let a function **modify** a module-level variable, declare it
    `global` first — otherwise `=` always creates a new local.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # Without 'global' -- fails
    count = 0

    def increment():
        count = count + 1
        print(count)

    increment()
    ```

    ```
    UnboundLocalError: cannot access local variable 'count'
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # With 'global' -- works
    count = 0

    def increment():
        global count
        count = count + 1
        print(count)

    increment()
    increment()
    print(count)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    1
    2
    2
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The `nonlocal` Keyword

    `global` only reaches the module level. For a nested function that
    needs to modify a variable in its **enclosing** function (not the
    global scope), use `nonlocal` instead.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def outerFunction():
        count = 0
        def increment():
            nonlocal count
            count += 1
        increment()
        increment()
        print(count)

    outerFunction()
    ```

    ```
    2
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `global` reaches the module level; `nonlocal` reaches one level
    out. Prefer returning a new value over either when you can — it's
    usually easier to follow.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Gotcha: The Mutable Default Argument Trap

    A default value is created **once**, when Python first reads the
    `def` line — not fresh on every call. A mutable default (like
    `[]`) is the same object every single call shares.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def addItem(item, itemList=[]):
        itemList.append(item)
        return itemList

    result1 = addItem("apple")
    print(result1)
    result2 = addItem("banana")
    print(result2)
    print(result1 is result2)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    ['apple']
    ['apple', 'banana']
    True
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The Fix: Default to `None`

    Use `None` as the default, then create a fresh mutable object
    **inside** the function body on every call.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def addItem(item, itemList=None):
        if itemList is None:
            itemList = []
        itemList.append(item)
        return itemList

    print(addItem("apple"))
    print(addItem("banana"))
    ```

    ```
    ['apple']
    ['banana']
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    This pattern — default to `None`, build the real value inside the
    function — applies to any mutable default: lists, dicts, sets.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Scope: What to Remember

    - **LEGB order** — Local → Enclosing → Global → Built-in. Python
      always resolves a name to the *closest* scope that defines it.
    - A function's local variables are gone once it returns —
      referencing one afterward raises `NameError`.
    - **Gotcha:** assigning to a name *anywhere* in a function makes it
      local for the *entire* function, even on an earlier line that
      only reads it — that's what raises `UnboundLocalError`, not a
      missing `global`.
    - Reading an outer-scope variable needs no special syntax;
      **modifying** one does — `global` for the module level,
      `nonlocal` for an enclosing function.
    - **Gotcha:** `global` and `nonlocal` are not interchangeable —
      `global` only ever reaches the module level, never an enclosing
      function's variables.
    - **Gotcha:** scope is decided by where code is *written*
      (lexically), not by where a function happens to be *called
      from*.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## What Is a Script?

    Until now, you've written code in notebooks (Colab/Jupyter) — run one
    cell, see its result, then move to the next. A **script** is a
    complete `.py` file that runs top to bottom in one shot when you
    execute it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - **Interactive code (notebooks)** — like a conversation: say
      something, get an immediate response, continue.
    - **Scripts** — like writing a letter: write the whole thing first,
      then send it to be read start to finish.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    In a script, everything runs in sequence, output only appears if
    you `print()` it, and the file must be **saved** before you run it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Why Use Scripts?

    - **Professional** — the industry standard; easy to share and
      version control (Git/GitHub); runnable from the command line.
    - **Practical** — reusable anytime, better organized for larger
      programs, easier to debug.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The `if __name__ == "__main__":` Pattern

    When you run a file directly (`python calculator.py`), Python sets
    the special variable `__name__` to `"__main__"`. This pattern says:
    "only run this part if I'm the file being executed directly."

    📖 [GPP: Understanding `if __name__`](https://BU-EK125.github.io/EK125/gpps/Class14_GPP.html#problem-8-understanding-the-if-name-main-pattern)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    def calculate_area(length, width):
        """Calculate area of a rectangle."""
        return length * width

    def main():
        print("Rectangle Area Calculator")
        area = calculate_area(4, 5)
        print(f"Area: {area}")

    if __name__ == "__main__":
        main()
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    Rectangle Area Calculator
    Area: 20
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Two reasons to use it: it **separates** your functions from your
    main program logic, and it lets **other files import your
    functions** without accidentally running your main program too.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Script Structure Best Practices

    A well-organized script follows the same order every time:

    📖 [GPP: Script Organization](https://BU-EK125.github.io/EK125/gpps/Class14_GPP.html#problem-3-script-organization)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    """Script description at the top."""

    # Imports
    import math

    # Constants
    GRAVITY = 9.81
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # Function definitions (continued from previous slide)
    def calculate_something(param1, param2):
        """Function docstring explaining what it does."""
        return param1 + param2

    # Main program
    if __name__ == "__main__":
        result = calculate_something(5, 10)
        print(f"Result: {result}")
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Docstring → imports → constants → function definitions → main. This
    order isn't arbitrary: Python needs to know about a function (and
    any constants it uses) **before** your main code calls it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Why Work with Files?

    Until now, all your data disappeared when the program ended. Files
    let you save results, process large datasets, share data between
    programs, and keep logs — reading sensor data, saving calculation
    results, writing automated reports.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Opening Files: `open()` and `with`

    The old way (`open()` / `.close()`) works, but it's easy to forget
    the `close()` call — especially if an error happens first. The
    modern way wraps it in a **context manager**: a `with` block that
    closes the file automatically, even if something goes wrong inside.

    📝 [HW7 Problem 7: Writing and Reading Back Sensor Data](https://BU-EK125.github.io/EK125/homework/HW7.html#problem-7-writing-and-reading-back-sensor-data)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # Old way -- you have to remember to close!
    file = open('data.txt', 'r')
    content = file.read()
    file.close()

    # Modern way -- closes automatically
    with open('data.txt', 'r') as file:
        content = file.read()
    # File is already closed here
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Always use `with open(...) as file:` — never the old `open()` /
    `.close()` pair.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## File Modes

    Opening a file requires a **mode** — what you intend to do with it:

    | Mode | Meaning | If the file doesn't exist |
    |------|---------|---------------------------|
    | `'r'` | Read | Error |
    | `'w'` | Write (overwrite) | Creates a new file |
    | `'a'` | Append | Creates a new file |
    | `'r+'` | Read/Write | Error |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `'w'` mode **deletes the entire file** first if it already exists —
    use `'a'` when you want to add to a file without losing what's
    already in it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Reading Files: `.read()`

    Reads the **entire file** into one string at once — best for small
    files.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # story.txt contains:
    #   Once upon a time
    #   In a land far away
    #   There lived a dragon

    with open('story.txt', 'r') as file:
        content = file.read()
        print(content)
    ```

    ```
    Once upon a time
    In a land far away
    There lived a dragon

    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Reading Files: `.readline()`

    Reads **one line at a time** — useful when you only need the first
    few lines, like a header.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    with open('story.txt', 'r') as file:
        line = file.readline()
        print(line)
    ```

    ```
    Once upon a time

    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Reading Files: `.readlines()`

    Reads **all lines into a list** — one string per line, each still
    ending in `\\n`. Good when you need to process every line.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # temperatures.txt contains: 72, 68, 75, 71 (one per line)

    with open('temperatures.txt', 'r') as file:
        lines = file.readlines()
        print(lines)

        temps = [float(line.strip()) for line in lines]
        average = sum(temps) / len(temps)
        print(f"Average temperature: {average}")
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    ['72\\n', '68\\n', '75\\n', '71\\n']
    Average temperature: 71.5
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Each line keeps its trailing `\\n` — use `.strip()` to remove it
    before converting to a number or comparing strings.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Reading Files: Iterate Directly

    For large files, loop over the file object itself — one line is
    read into memory at a time, instead of the whole file at once.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # system.log has 4 lines, 2 starting with "ERROR"

    error_count = 0
    with open('system.log', 'r') as file:
        for line in file:
            if 'ERROR' in line:
                error_count += 1
    print(f"Found {error_count} errors")
    ```

    ```
    Found 2 errors
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Writing Files

    `'w'` mode creates the file if needed and overwrites it if it
    already exists. `.write()` does **not** add newlines for you — you
    have to include `\\n` yourself.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    with open('output.txt', 'w') as file:
        file.write('Hello, World!\\n')
        file.write('This is a new line.\\n')

    with open('output.txt', 'r') as file:
        print(file.read())
    ```

    ```
    Hello, World!
    This is a new line.

    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Appending to Files

    `'a'` mode adds to the **end** of a file instead of erasing it
    first — the basis of a logging pattern you'll use constantly.

    📝 [HW7 Problem 8: Write vs. Append](https://BU-EK125.github.io/EK125/homework/HW7.html#problem-8-write-vs-append-a-lab-activity-log)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # log.txt already contains: "First entry\\n"

    with open('log.txt', 'a') as file:
        file.write('New log entry\\n')

    with open('log.txt', 'r') as file:
        print(file.read())
    ```

    ```
    First entry
    New log entry

    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `'w'` **overwrites** everything; `'a'` **adds on** to what's
    already there. Mixing these up is one of the most common file bugs.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Working with CSV Files

    CSV (Comma-Separated Values) stores tabular data as plain text —
    one row per line, fields separated by commas. Python's `csv`
    module handles the reading and writing for you.

    📝 [HW7 Problem 9: Reading and Writing CSV Files](https://BU-EK125.github.io/EK125/homework/HW7.html#problem-9-reading-and-writing-csv-files)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    import csv

    students = [
        ['Name', 'Grade', 'Age'],
        ['Alice', 95, 20],
        ['Bob', 87, 21],
    ]
    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        print(f"Columns: {header}")
        for row in reader:
            name, grade, age = row
            print(f"{name} scored {grade}")
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    Columns: ['Name', 'Grade', 'Age']
    Alice scored 95
    Bob scored 87
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The Local File Environment

    Your computer organizes files in a tree: folders contain files and
    other folders. A **path** is the route to a file — either
    **absolute** (the full address, from the very top) or **relative**
    (from wherever your program currently is).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    Documents/
    ├── EK125/
    │   ├── Class14/
    │   │   ├── script.py
    │   │   └── data.txt
    │   └── Homework/
    │       └── hw5.py
    └── Photos/
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `.` means the current directory, `..` means one level up, and `~`
    means your home directory — all relative to wherever your script
    is currently running.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The `os` Module

    `os` lets your code ask questions about — and move around — the
    file system: where am I, what's here, does this exist.

    📝 [HW7 Problem 10: Organizing Experiment Folders with `os`](https://BU-EK125.github.io/EK125/homework/HW7.html#problem-10-organizing-experiment-folders-with-os)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    import os

    print(os.getcwd())
    print(os.listdir())
    ```

    ```
    /Users/alice/Documents/EK125
    ['script.py', 'data.txt', 'notes.md']
    ```

    *(illustrative — your own output will show your actual folder and
    its actual contents)*
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Checking Before You Open

    `os.path.exists()` tells you whether a file is there **before**
    you try to open it — avoiding a crash on a typo'd filename.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    import os

    print(os.path.exists('students.csv'))
    print(os.path.exists('nonexistent.txt'))
    ```

    ```
    True
    False
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Building Paths: `os.path.join()`

    Windows uses `\\` between folder names; Mac/Linux use `/`. Hand-
    writing either one breaks on the other operating system —
    `os.path.join()` always produces the right separator.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    import os

    path = os.path.join('Documents', 'EK125', 'data.txt')
    print(path)
    ```

    ```
    Documents/EK125/data.txt
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Always build paths with `os.path.join()` instead of concatenating
    strings with `/` or `\\` — it's the one call that works everywhere.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Creating Directories

    `os.mkdir('name')` creates **one** new folder — it fails if the
    parent folder doesn't already exist. `os.makedirs('a/b/c')` creates
    **every** folder in the path that's missing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    When in doubt, use `os.makedirs(path, exist_ok=True)` — it builds
    the whole path if needed, and doesn't error if it already exists.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Common Mistake: Forgetting `.strip()`

    Splitting a raw line keeps the trailing newline stuck to its last
    field — easy to miss until something downstream compares strings
    and silently fails.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # students2.txt contains: "Alice,95,20\\n"

    with open('students2.txt', 'r') as file:
        for line in file:
            values = line.split(',')
            print(repr(values[2]))
    ```

    ```
    '20\\n'
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    # Fixed:
    with open('students2.txt', 'r') as file:
        for line in file:
            values = line.strip().split(',')
            print(repr(values[2]))
    ```

    ```
    '20'
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Common Mistake: `'w'` Mode Overwrites

    Opening an existing file in `'w'` mode **erases it immediately** —
    even before you write anything new.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    with open('important.txt', 'w') as file:
        file.write('original data\\n')

    # Later, accidentally reopened in 'w' mode:
    with open('important.txt', 'w') as file:
        file.write('new data\\n')

    with open('important.txt', 'r') as file:
        print(repr(file.read()))
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ```
    'new data\\n'
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    If you only want to add to a file, use `'a'`. Reach for `'w'` only
    when overwriting is exactly what you want.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Summary

    - A **script** runs top to bottom from a `.py` file; organize it as
      docstring → imports → constants → functions → main, guarded by
      `if __name__ == "__main__":`.
    - Always open files with **`with`** — it closes them automatically,
      even on error.
    - Modes: `'r'` read, `'w'` write (**overwrites**), `'a'` append.
    - Read with `.read()`, `.readline()`, `.readlines()`, or by
      iterating the file directly — and `.strip()` trailing newlines.
    - The `os` module answers *where am I* (`getcwd`, `listdir`), *does
      this exist* (`path.exists`), and *build me a path*
      (`path.join`) — all portable across operating systems.
    - Scope follows the **LEGB** rule (Local, Enclosing, Global,
      Built-in); assigning to a name anywhere in a function makes it
      local for the whole function, unless declared `global`/`nonlocal`.
    - A mutable default argument (like `itemList=[]`) is created once
      and shared across every call — default to `None` instead.

    📝 [Today's GPP](https://BU-EK125.github.io/EK125/gpps/Class14_GPP.html)
    📝 [This week's homework: HW7](https://BU-EK125.github.io/EK125/homework/HW7.html)
    """)
    return


if __name__ == "__main__":
    app.run()
