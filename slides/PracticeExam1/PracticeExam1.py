import marimo

__generated_with = "0.24.0"
app = marimo.App(
    html_head_file="../../colab_button.html",
    width="full",
    layout_file="layouts/PracticeExam1.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
# EK125 Exam 1

### Practice Exam Walkthrough

Questions, solutions, and tips

📖 Work through each problem yourself using the practice exam, then use
this deck to check your answer and pick up a few extra tips.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
## How to Use This Deck

For every problem:

1. **Try it yourself** first, using the question as shown.
2. **Advance** to see the answer and the reasoning behind it.
3. **Advance again** for a 💡 tip — a related gotcha worth knowing for
   the real exam.

Problems follow the same order and numbering as the practice exam.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
## Problem 1: True/False (a–d)

**a)** In the block of code below, the print statement will be invoked
five times:
```python
for i in range(5):
    print(i)
```

**b)** The expression `10 // 3` evaluates to `3.33`.

**c)** After executing `mylist = [1, 2, 3]` and then `mylist[1] = 99`,
the list becomes `[1, 99, 3]`.

**d)** After executing `mystring = "Python"` and then
`mystring[3] = "t"`, the string becomes `"Pytton"`.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
### ✅ Answers

**a) True** — `range(5)` produces 5 values (0–4), so the loop body
runs 5 times.

**b) False** — `//` is *integer* (floor) division: `10 // 3` is `3`,
not `3.33`. (`3.33...` is what `10 / 3` gives.)

**c) True** — lists are mutable; index assignment replaces that one
element in place.

**d) False** — strings are *immutable*. `mystring[3] = "t"` doesn't
silently change the string — it raises
`TypeError: 'str' object does not support item assignment`.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
💡 **Tip:** b) and d) are testing the same instinct from opposite
directions — two separate rules that are easy to blur together:
`/` vs `//` (division), and mutable vs immutable (list vs string).
When a True/False question changes just one word or one operator from
something you know, stop and identify exactly which rule it's probing
before answering.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
## Problem 1: True/False (e–h)

**e)** A `while` loop will always execute its action at least once.

**f)** The `random.seed()` function ensures that the same sequence of
"random" numbers is generated each time the program runs.

**g)** The expression `5 % 2 == 0` evaluates to `True`.

**h)** Tuples in Python are mutable, meaning members may be added and
removed after the tuple is created.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
### ✅ Answers

**e) False** — a `while` loop checks its condition *first*; if it's
false immediately, the action never runs at all. Python has no
built-in do-while.

**f) True** — that's exactly what `random.seed()` is for: same seed
in, same sequence of "random" values out, every run.

**g) False** — `5 % 2` is `1` (the remainder), and `1 == 0` is
`False`.

**h) False** — tuples are immutable, the opposite of lists. Once
created, you cannot add, remove, or reassign any element.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
💡 **Tip:** if a True/False question names a specific built-in
(`random.seed()`, `%`, tuples), it's almost always testing whether you
know that thing's *one defining property* — reproducibility,
remainder, immutability. Answer from the definition, not a guess.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
## Problem 2: Multiple Choice (a–b)

**a)** What is the value of `result` after this code executes?
```python
input = [1, 2, 3, 4]
result = 0
for i in input:
    result = result + 1
```
A. `0`&nbsp;&nbsp;&nbsp; B. `4`&nbsp;&nbsp;&nbsp; C. `10`&nbsp;&nbsp;&nbsp; D. program fails to run

**b)** Which best describes what happens when a `for` loop iterates
through a string?

A. once per word &nbsp; B. once per character &nbsp; C. until the string is empty &nbsp; D. forever
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
### ✅ Answers

**a) B (`4`)** — the loop adds `1` once per element, and there are 4
elements. (`input` here is just a variable name, shadowing the
built-in `input()` function — it's a plain list, no actual
input-reading involved.)

**b) B** — a `for` loop over a string iterates character by character,
same as over a list of single characters.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
💡 **Tip:** part a) is a classic "read the variable name, not just the
type" trap — `input` looks like the built-in function, but it's been
reassigned to a list. Whenever a name matches a built-in, check what
it was actually assigned before assuming what it does.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
## Problem 2: Multiple Choice (c–d)

**c)**
```python
x = 10
while x > 5:
    x = x - 2
print(x)
```
What prints? A. nothing (infinite loop) &nbsp; B. `6` &nbsp; C. `4` &nbsp; D. `10`

**d)** What is the purpose of `end=''` in a `print()` statement?

A. ends the program &nbsp; B. adds extra characters &nbsp; C. prevents moving to a new line &nbsp; D. causes an error
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
### ✅ Answers

**c) C (`4`)** — trace it: `10 → 8 → 6 → 4`, and the loop stops as
soon as `x > 5` is false (at `x = 4`), *before* subtracting again.
`print(x)` then shows `4`.

**d) C** — `end=''` replaces the default trailing `'\n'` with
nothing, so the next `print()` continues on the same line.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
💡 **Tip:** for c), trace the loop **one line at a time on scratch
paper** instead of doing it in your head — `x: 10, 8, 6, 4`, then
check the *condition* before assuming one more subtraction happens.
Off-by-one errors in while-loop tracing are the single most common way
students lose points on this problem type.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
## Problem 3: Expression Evaluation (a–c)

Show the result of each (typed sequentially):

**a)** `15 % 4 + 2`

**b)** `3 ** 2 > 10 or 4 < 5`

**c)** `"hello".upper() == "HELLO"`
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
### ✅ Answers

**a) `5`** — `15 % 4` is `3`, then `3 + 2` is `5`.

**b) `True`** — `3 ** 2` is `9`; `9 > 10` is `False`; but `4 < 5` is
`True`; `False or True` is `True`.

**c) `True`** — `.upper()` returns `"HELLO"`, which equals `"HELLO"`.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
💡 **Tip:** for b), evaluate strictly in precedence order —
exponent first (`**`), then comparisons (`>`, `<`), then `or` last.
Writing out each intermediate value on its own line (like the answer
above) catches mistakes that doing it all in one mental leap won't.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
## Problem 3: Expression Evaluation (d–f)

Show the result of each (typed sequentially):

**d)**
```python
x = [10, 20, 30]
x.append(40)
len(x)
```

**e)** `not (True and False)`

**f)** `"abc" * 2 + "d"`
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
### ✅ Answers

**d) `4`** — the assignment and `.append()` produce no displayed value
on their own; only the final `len(x)` does, and the list has grown to
4 elements.

**e) `True`** — `True and False` is `False`; `not False` is `True`.

**f) `"abcabcd"`** — `"abc" * 2` repeats the string first
(`"abcabc"`), *then* `+ "d"` appends once.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
💡 **Tip:** for d), remember that **assignment (`=`) and most list
methods (`.append()`, `.sort()`, etc.) don't produce a displayed
value** — they return `None` or nothing at all. Only the *last*
expression that actually evaluates to something shows a result.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
## Problem 4: Sequences (a–c)

```python
colors = ["red", "green", "blue"]
phrase = "Introduction"
scores = [85, 92, 78, 95, 88]
nested = [42, "hello", [1, 2]]
mixed = ("hello", [1, 2])
```

**a)** `colors[0]`

**b)** `phrase[3:6]`

**c)** `scores[-2]`
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
### ✅ Answers

**a) `'red'`** — index `0` is the first element.

**b) `'rod'`** — `phrase[3:6]` takes indices 3, 4, 5. Spelling out
`"Introduction"`: `I(0) n(1) t(2) r(3) o(4) d(5) ...` — that's `r`,
`o`, `d`.

**c) `95`** — negative indices count from the end; `-2` is the
second-to-last element.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
💡 **Tip:** for slicing (b) and negative indices (c), **count on your
fingers or write the indices above the string** rather than eyeballing
it — this is a very easy off-by-one to get wrong under time pressure,
and there's no partial credit for "close."
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
## Problem 4: Sequences (d–e)

(same `colors` / `phrase` as before)

**d)**
```python
colors.append("yellow")
len(colors)
```

**e)** `print(phrase.replace("tion", ""))`
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
### ✅ Answers

**d) `4`** — `colors` grows to `["red", "green", "blue", "yellow"]`,
so `len()` is `4`.

**e) `Introduc`** — `"Introduction"` ends in `...duction`, and
`"tion"` (the last 4 characters) gets replaced with nothing, leaving
`"Introduc"`.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
💡 **Tip:** `.replace(old, new)` replaces *every* occurrence of `old`,
not just the first — here there's only one `"tion"` in the string, but
don't assume that's always the case on a different string.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
## Problem 4: Sequences (f–g)

(`nested = [42, "hello", [1, 2]]`, `phrase = "Introduction"` —
still SEQUENTIAL, continuing from the earlier parts)

**f)** `nested[2][0]`

**g)** `"e" in phrase`
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
### ✅ Answers

**f) `1`** — `nested[2]` is the list `[1, 2]`; its `[0]` is `1`.

**g) `False`** — spell out `"Introduction"`:
`I-n-t-r-o-d-u-c-t-i-o-n` — there's no letter `e` anywhere in it.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
💡 **Tip:** `nested[2][0]` is two indexing operations back to back —
resolve the *outer* one first (`nested[2]` → `[1, 2]`), then index
*that* result. Don't try to do both steps in one mental jump.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
## Problem 4: Sequences (h–i)

(`nested` and `mixed = ("hello", [1, 2])` — still SEQUENTIAL)

**h)**
```python
nested.pop()
len(nested)
```

**i)**
```python
mixed[1].append(3)
len(mixed) + len(mixed[1])
```
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
### ✅ Answers

**h) `2`** — `.pop()` removes and returns the *last* element
(`[1, 2]`); `nested` is left with `[42, "hello"]`, so `len()` is `2`.

**i) `5`** — even though `mixed` is a tuple, `mixed[1]` is a *list*,
and lists are always mutable regardless of what holds a reference to
them. `.append(3)` grows it to `[1, 2, 3]` in place. `len(mixed)` is
still `2` (the tuple itself has 2 elements); `len(mixed[1])` is now
`3`; `2 + 3 = 5`.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
💡 **Tip:** part i) is the single most important idea in this whole
problem: **a tuple being "immutable" only means you can't reassign
what's *in* each tuple slot — it says nothing about whether that
slot's own object can change itself.** A list stored inside a tuple is
exactly as mutable as any other list. This trips up far more students
than any slicing question does.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
## Problem 5: Code Tracing

```python
print("Starting the simulation!")
print()
value = 12.8765
label = "Score"
print(f"{label}: {value:.1f}")
word = "Python"
if word.lower() == "python":
    print("Match found!")
for num in range(3):
    print(num * 2, end="-")
print()
count = 3
while count > 0:
    print("*" * count)
    count = count - 1
print("Complete!")
```
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
### ✅ Answer
```
Starting the simulation!

Score: 12.9
Match found!
0-2-4-
***
**
*
Complete!
```
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
💡 **Tip:** two easy points to lose here: (1) the **blank line** from
the bare `print()` on line 2 — don't skip it; (2) `{value:.1f}`
**rounds** `12.8765` to `12.9`, it doesn't truncate to `12.8`.
Whenever you see an f-string format spec like `:.1f`, work out the
rounded value by hand before writing your answer — don't guess.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
## Problem 6: Conditional Logic

Rewrite using only `if`/`elif`/`else`, no nesting — same logic:

```python
if grade >= 90:
    result = "A"
else:
    if grade >= 80:
        result = "B"
    else:
        if grade >= 70:
            result = "C"
        else:
            if grade >= 60:
                result = "D"
            else:
                result = "F"
```
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
### ✅ Answer
```python
if grade >= 90:
    result = "A"
elif grade >= 80:
    result = "B"
elif grade >= 70:
    result = "C"
elif grade >= 60:
    result = "D"
else:
    result = "F"
```
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
💡 **Tip:** each `elif` implicitly carries "and the previous
conditions were all false" — that's *why* it's safe to drop the
nesting. By the time Python checks `grade >= 80`, it already knows
`grade < 90`, so you never need to write that bound explicitly. This
is the whole trick behind every nested-if-to-elif rewrite.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
## Problem 7: Truth Table

Complete the table for `(not A)`, `(B and C)`, and
`(not A) or (B and C)`:

| A | B | C | not A | B and C | (not A) or (B and C) |
|---|---|---|---|---|---|
| T | T | T | ? | ? | ? |
| T | T | F | ? | ? | ? |
| T | F | T | ? | ? | ? |
| F | T | T | ? | ? | ? |
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
### ✅ Answer

| A | B | C | not A | B and C | (not A) or (B and C) |
|---|---|---|---|---|---|
| T | T | T | F | T | **T** |
| T | T | F | F | F | **F** |
| T | F | T | F | F | **F** |
| F | T | T | T | T | **T** |
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
💡 **Tip:** fill the table **column by column, not row by row** —
compute the whole `not A` column first, then the whole `B and C`
column, then combine. Doing one full row at a time makes it easy to
slip and use the wrong row's B or C by accident.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
## Problem 8: While Loop with Validation

Prompt for a password. Valid only if **at least 6 characters AND
contains at least one digit**. Keep prompting until valid, then print
`"Password accepted!"`.

```
Enter a password: hi
Enter a password: hello
Enter a password: hello1
Password accepted!
```
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
### ✅ A working solution
```python
password = input("Enter a password: ")
while len(password) < 6 or not any(ch.isdigit() for ch in password):
    password = input("Enter a password: ")
print("Password accepted!")
```
(Verified against the exam's own example transcripts.)
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
💡 **Tip:** this is a **prime-the-pump while loop** — ask once before
the loop so there's something to check, then the loop's own action
re-asks. Watch the logic direction: the *condition* needs
`len < 6 OR no digit` (keep looping if *either* requirement is still
unmet) — even though the problem describes the requirement itself
with "AND."
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
## Problem 9: Random Numbers and List Processing

Using `random.seed(42)`:
- Generate 6 random integers, each 1–20 (inclusive)
- Print the list
- Print the **sum of the even numbers** (by value, not index)
- Print the **count of numbers greater than 10**

Format:
```
Numbers: [list of numbers here]
Sum of even numbers: X
Count greater than 10: Y
```
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
### ✅ A working solution
```python
import random
random.seed(42)
numbers = [random.randint(1, 20) for _ in range(6)]
print("Numbers:", numbers)

even_sum = sum(n for n in numbers if n % 2 == 0)
print("Sum of even numbers:", even_sum)

count_gt10 = sum(1 for n in numbers if n > 10)
print("Count greater than 10:", count_gt10)
```
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
💡 **Tip:** "sum of the even numbers (NOT numbers with even indices)"
is called out explicitly for a reason — **index-based filtering
(`numbers[::2]`) is the classic wrong answer here.** Filter on the
*value* (`n % 2 == 0`), not the *position*. When a problem explicitly
rules out a specific mistake in parentheses, assume past students have
made exactly that mistake.

With `random.seed(42)`, this actually produces:
```
Numbers: [4, 1, 9, 8, 8, 5]
Sum of even numbers: 20
Count greater than 10: 0
```
(verified by running it)
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
## Problem 10: BlackJack Experiment

Deal 4 random "cards," each uniformly 1–11 (inclusive, no choice
between 1/11). Simulate **100 experiments**. Print:
```
Of 100 experiments, N resulted in a value of 21 or less.
```
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
### ✅ A working solution
```python
import random

successes = 0
for _ in range(100):
    total = sum(random.randint(1, 11) for _ in range(4))
    if total <= 21:
        successes += 1

print(f"Of 100 experiments, {successes} resulted in a value of 21 or less.")
```
(No seed is specified for this problem, so `N` will vary run to run —
one sample run gave `45`.)
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
💡 **Tip:** this is the same **accumulator pattern** as Problem 9's
counting, just nested one level deeper — an *inner* loop builds one
experiment's total (4 cards), and an *outer* loop repeats the whole
experiment 100 times, counting successes. When a problem says
"simulate N experiments," that's almost always your outer
`for _ in range(N):` loop, with a counter initialized to `0` *before*
it starts.
''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md('''
## That's the Whole Exam

A few cross-cutting habits that showed up again and again:

- **Trace loops on paper**, one line at a time — don't do it in your
  head.
- Know which built-ins are **mutable** (lists) vs **immutable**
  (strings, tuples) — cold.
- Watch for a problem explicitly ruling out a wrong approach in
  parentheses — that's a hint about a common mistake, not filler text.
- For programming problems, **match the output format exactly** —
  extra or missing punctuation costs points even with correct logic.

Good luck!
''')
    return
