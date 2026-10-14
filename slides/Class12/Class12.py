import marimo

__generated_with = "0.25.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/Class12.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Dictionaries

    ### Storing and Looking Up Data by Key

    *Class 12*

    📖 [Full reading: Class 12](https://BU-EK125.github.io/EK125/class/Class12.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Before We Start: Testing Your Code

    We didn't get to this in Class 11 — let's cover it now before moving
    on to today's topic.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Why Test Your Code?

    A test is a small check that your code produces the output you
    expect. Three reasons it's worth the extra code:

    - **Correctness** — catches bugs early, before they affect results
      you're relying on.
    - **Regression guard** — confirms you haven't broken something that
      used to work, if you edit the code later.
    - **Documentation** — a well-written test shows exactly how a
      function is supposed to behave.

    In this course, you'll mostly write **unit tests** — checking one
    small piece of code (a single function or calculation) in isolation.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## `assert`: Python's Testing Tool

    `assert` checks a condition — if it's `True`, nothing happens; if
    it's `False`, Python raises an `AssertionError` and stops.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    import numpy as np

    x = 5
    assert x > 0
    assert x > 10
    ```

    ```
    AssertionError
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The Array `assert` Gotcha

    `a == b` on two arrays returns an **array** of booleans, not one
    `True`/`False`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    a = np.array([1, 2, 3])
    b = np.array([1, 2, 3])
    assert a == b
    ```

    ```
    ValueError: The truth value of an array is ambiguous
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Fix: `assert (a == b).all()` checks that **every** element matches.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## What is a Dictionary?

    A dictionary stores **key-value pairs** — it's a *mapping*, not a
    sequence, so you look things up by **key** instead of by position.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## When to Use a Dictionary

    Lists and NumPy arrays are for **ordered** data you access by
    position — "the 3rd element." Reach for a dictionary when position
    doesn't mean anything, but a **label** does:

    - **A single record** — one hurricane's name, year, and category,
      instead of remembering "index 0 is the name."
    - **A lookup table** — mapping a student ID to a grade, or a word
      to how many times it appeared.
    - **Counting or grouping** — tallying votes or categories as you
      loop through data.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Use a **list** or **array** when order/position matters (especially
    for numeric math); use a **dictionary** when a meaningful name does.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Creating a Dictionary

    Use `{}` with `key: value` pairs. Access a value with its key in
    square brackets.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    bigone = {'name': 'Bertha', 'year': 1952, 'category': 4}
    print(bigone['year'])
    ```

    ```
    1952
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## A Missing Key: `KeyError`

    Indexing with a key that doesn't exist raises a `KeyError`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    bigone['size']
    ```

    ```
    KeyError: 'size'
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Modifying a Dictionary

    Assign to an existing key to **change** its value, or to a new key
    to **add** one.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    bigone['category'] = 5
    bigone['wind'] = 120
    print(bigone)
    ```

    ```
    {'name': 'Bertha', 'year': 1952, 'category': 5, 'wind': 120}
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Dictionaries are **mutable** — just like lists, you change them in
    place instead of creating a new one.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Deleting and Counting

    `del` removes a key-value pair; `len()` counts how many pairs
    remain.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    del bigone['wind']
    print(bigone)
    print(len(bigone))
    ```

    ```
    {'name': 'Bertha', 'year': 1952, 'category': 5}
    3
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Membership and Keys

    `in` / `not in` check whether a key exists; `list()` pulls out just
    the keys.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    print('year' in bigone)
    print('sqarea' not in bigone)
    print(list(bigone))
    ```

    ```
    True
    True
    ['name', 'year', 'category']
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The `get()` Method

    `get()` retrieves a value like square brackets do, but returns
    `None` — or a default you choose — instead of raising an error.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    print(bigone.get('size'))
    print(bigone.get('size', -999))
    ```

    ```
    None
    -999
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    `get()` is safer than `bigone['size']` whenever a key might be
    missing — it never raises a `KeyError`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Removing One Item: `pop()`

    `pop()` deletes a key-value pair **and returns the value** that was
    removed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    delcat = bigone.pop('category')
    print(delcat)
    ```

    ```
    5
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Takeaway

    Like `get()`, `pop()` also accepts a default, avoiding a `KeyError`
    on a missing key.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## `popitem()` and `clear()`

    `popitem()` removes the **last** key-value pair, returned as a
    tuple. `clear()` empties the dictionary completely.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    k, v = bigone.popitem()
    print(k, v)

    bigone.clear()
    print(bigone)
    ```

    ```
    year 1952
    {}
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Iterating with `keys()`

    `.keys()` loops over just the keys.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    bigone = {'name': 'Bertha', 'year': 1952, 'category': 4}
    for kname in bigone.keys():
        print('The key is', kname)
    ```

    ```
    The key is name
    The key is year
    The key is category
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Iterating with `items()`

    `.items()` gives you **both** the key and the value together.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    for k, v in bigone.items():
        print('The value of', repr(k), 'is', v)
    ```

    ```
    The value of 'name' is Bertha
    The value of 'year' is 1952
    The value of 'category' is 4
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## A List of Dictionaries

    To store more than one record, put several dictionaries in a list —
    then index or loop through it like any other list.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    hurr0 = {'name': 'Bertha', 'year': 1952, 'category': 4}
    hurr1 = {'name': 'Bob', 'year': 1990, 'category': 2}
    hurr2 = {'name': 'Camilla', 'year': 1960, 'category': 5}
    hurricanes = [hurr0, hurr1, hurr2]
    print(hurricanes[2])
    ```

    ```
    {'name': 'Camilla', 'year': 1960, 'category': 5}
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Looping Through a List of Dictionaries

    Loop through the list, and index into each dictionary by key as you
    go.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    print('The largest hurricanes were:')
    for hurr in hurricanes:
        if hurr['category'] >= 4:
            print(repr(hurr['name']))
    ```

    ```
    The largest hurricanes were:
    'Bertha'
    'Camilla'
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Nested Values: A List Inside a Dictionary

    A dictionary's value can be any type — including a list. Index into
    it the same way you'd index any list.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    icdessert = {
        'flavor': 'malted',
        'cone': True,
        'nscoops': 2,
        'addins': ['pecans', 'chocolate chips']
    }
    print(icdessert['addins'])
    ```

    ```
    ['pecans', 'chocolate chips']
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Indexing into the Nested List

    Index into the list the same way you would anywhere else.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    print(icdessert['addins'][0])
    ```

    ```
    pecans
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Dictionary Comprehension

    Like a list comprehension, but each entry produces a `key: value`
    pair.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    cubedict = {i: i**3 for i in range(5)}
    print(cubedict)
    ```

    ```
    {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
    ```
    ''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Summary

    - A dictionary stores **key-value pairs** — look things up by key,
      not position; a missing key raises a `KeyError`.
    - `get()` and `pop()` both accept a default value to avoid that
      error.
    - `del`, `len()`, `in`, and `list()` all work on dictionaries.
    - `.keys()`, `.values()`, and `.items()` iterate over a dictionary;
      `.items()` gives you both the key and the value.
    - Values can be any type — including a list or another dictionary —
      and dictionary comprehensions build one the same way list
      comprehensions do.

    📝 [Today's GPP](https://BU-EK125.github.io/EK125/gpps/Class12_GPP.html)
    """)
    return


if __name__ == "__main__":
    app.run()
