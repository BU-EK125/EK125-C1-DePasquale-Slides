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

    ```
    Rectangle Area Calculator
    Area: 20
    ```
    ''')
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

    # Function definitions
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

    ```
    ['72\\n', '68\\n', '75\\n', '71\\n']
    Average temperature: 71.5
    ```
    ''')
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

    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        print(f"Columns: {header}")
        for row in reader:
            name, grade, age = row
            print(f"{name} scored {grade}")
    ```

    ```
    Columns: ['Name', 'Grade', 'Age']
    Alice scored 95
    Bob scored 87
    ```
    ''')
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

    # Fixed:
    with open('students2.txt', 'r') as file:
        for line in file:
            values = line.strip().split(',')
            print(repr(values[2]))
    ```

    ```
    '20\\n'
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

    ```
    'new data\\n'
    ```
    ''')
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

    📝 [Today's GPP](https://BU-EK125.github.io/EK125/gpps/Class14_GPP.html)
    """)
    return


if __name__ == "__main__":
    app.run()
