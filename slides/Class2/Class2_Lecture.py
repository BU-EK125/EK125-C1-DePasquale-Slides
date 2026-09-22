import marimo

__generated_with = "0.24.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class2_Lecture.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Sequences in Python

    ### Strings, Lists, and Tuples

    *Class 2*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Why Do We Need Sequences?
    """)
    return


@app.cell
def _():
    # From the reading — "Why Do We Need Sequences?" (Class2.html)
    student1 = "Alice"
    student2 = "Tushar"
    student3 = "Charlie"

    students = ["Alice", "Tushar", "Charlie"]
    students
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Three separate variables don't scale — one sequence does. That's the whole
    point of today.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## What Is a Sequence?

    - An **ordered** collection of items
    - Every item has a **position** (an index)
    - You can measure its **length**
    - You can **iterate** over it, one item at a time

    *Same definition as the pre-read.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Three Flavors of Sequences

    | Type | Written with | Can you change it? |
    |------|--------------|---------------------|
    | `str`   | `"..."` | No |
    | `list`  | `[...]` | Yes |
    | `tuple` | `(...)` | No |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Indexing Basics

    - `seq[0]` → the first item
    - `seq[-1]` → the last item
    - `len(seq)` → how many items

    *Works exactly the same way for strings, lists, **and** tuples.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Common String Operations
    """)
    return


@app.cell
def _():
    # From the reading's "Common String Operations" (Class2.html)
    text = "Hello World"
    print(text.upper())  # "HELLO WORLD"
    print(text.replace("o", "0"))  # "Hell0 W0rld"
    print(text.split())  # ["Hello", "World"]
    "World" in text  # True
    text.upper()
    text
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Each method returns a **new** value — `text` itself never changes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Lists in Action
    """)
    return


@app.cell
def _():
    # From Class-2.pdf, "Lists" slides
    semester_list = ["Spring2025", "Fall2025"]
    semester_list.append("Spring2026")
    semester_list.pop(0)
    semester_list
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `.append()` grows a list, `.pop()` shrinks it — lists resize themselves.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Practice: Modifying a List
    """)
    return


@app.cell
def _():
    # From Class_2_GPP.ipynb, Task 2.2 (bug `numbers(3) = 35` fixed below)
    numbers = [10, 20, 30, 40, 50]
    numbers[2] = 35
    numbers.append(60)
    numbers.insert(0, 5)
    numbers.remove(40)
    numbers.pop()

    numbers  # [5, 10, 20, 35, 50]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Five list methods, each mutating `numbers` **in place**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Lists Are Mutable

    - Size can grow or shrink
    - Elements can be added, removed, or replaced
    - `[ ]` — think of it as a container you're allowed to reshape
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Your Turn

    ```python
    fruits = ["apple", "banana", "cherry"]
    fruits.append("date")
    fruits[1] = "blueberry"
    fruits.pop(0)
    ```

    *What does `fruits` look like after these three lines run?*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Common Tuple Operations
    """)
    return


@app.cell
def _():
    # From the reading's "Common Tuple Operations" (Class2.html)
    colors = ("red", "green", "blue")
    print(colors[1])  # "green"
    print("red" in colors)  # True
    colors2 = colors + ("yellow",)  # a *new* tuple
    colors2
    colors
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Indexing, `in`, and `+` all work — none of them modify `colors` itself.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Trying to Mutate a Tuple
    """)
    return


@app.cell
def _():
    # From Class-2.pdf, "Tuples" slide (raises an error on purpose)
    semester_tuple = ("Spring2025", "Fall2025")
    print(semester_tuple)
    semester_tuple.append("Spring2027")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Tuples have no `.append()` — that's exactly what raises the error above.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Tuples Are Immutable

    - Fixed size, fixed membership
    - No `.append()`, `.insert()`, `.pop()`, or `.remove()`
    - Once it's built, it stays built
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Your Turn

    ```python
    point = (3, 7)
    point[0] = 10
    ```

    *Will this run? If not, what error will Python raise — and why?*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The Tuple-of-Lists Twist
    """)
    return


@app.cell
def _():
    # From Class-2.pdf, "Tuple of Lists" slides
    classes_tuple = (["Spring2025-EK125"], ["Fall2025-EC311"])
    classes_tuple[1].append("Fall2025-EC427")
    classes_tuple
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    The tuple can't resize — but element `1` is a *list*, so `.append()` works.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Mutability Recap

    - **Container** mutability and **element** mutability are separate questions
    - A tuple can't gain or lose items — but if one of its items is a *list*, that list can still change
    - Ask two questions: *Can the container change size? Can its contents change?*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## When to Use Each

    - **String** → text you treat as a whole (a title, a name)
    - **List** → a collection that grows or shrinks (a queue, a cart, a playlist)
    - **Tuple** → a fixed bundle you want to protect (coordinates, an RGB color, a fixed-size record)

    *Rule of thumb: if it's not supposed to change, make it a tuple.*
    """)
    return


if __name__ == "__main__":
    app.run()
