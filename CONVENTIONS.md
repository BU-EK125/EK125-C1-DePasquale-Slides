# Conventions for building decks in this repo

This documents the non-obvious patterns behind how decks in this repo are
built, established across Classes 2-4 (the older per-topic split) and
Class 6 (the current format). If you're just editing existing slide text,
see [README.md](README.md) for the basic mechanics instead. This file is
for building a new deck, or anything involving the quick-check widgets.

## Deck format: one deck per class

**Starting with Class 6, each class gets exactly one deck**, not a
separate Lecture deck and GPP deck. That deck is:

- A lecture that walks through the class's reading, in the reading's own
  order, compressing its prose into slide-sized bullets/takeaways the way
  the earlier Lecture decks already did.
- Live code examples pulled from either the reading or the class's GPP --
  whichever best illustrates the point at that spot in the lecture. There's
  no need to separately enumerate every GPP problem; the GPP notebook
  itself (linked from the deck) is where students work through all of them
  asynchronously.
- **Three multiple-choice quick-check widgets**, each based on a real GPP
  problem, placed right after the lecture section that problem depends on
  (not clustered at the end) -- see "Quick-check widgets" below.

Classes 2-4 predate this format. Their old GPP and homework-help decks
are archived (`archive/ClassN/`, excluded from the build) rather than
retrofitted into the one-deck-with-quick-checks format -- each of
those classes now has just its original Lecture deck, still under its
own topic (not a full walk through that class's reading the way Class
6 is), and **without quick-checks** -- that mechanism hadn't started
yet for these classes, and there's no GPP deck alongside them anymore
to source questions from. What *did* get retrofitted onto them: the
code-example convention below (hand-typed code+output, no live
execution) -- Classes 2-4 had the exact same bare-`print()`-vanishes
bug as Class 6 did before that convention existed, just never
noticed/fixed until it was. Don't take Classes 2-4 as the structural
pattern for a new deck -- follow Class 6 (`slides/Class6/Class6.py`)
for that -- but their code-example cells now follow the same
convention as Class 6's.

## marimo output calls: which one actually runs your content

Three different marimo calls can render HTML in a cell, and they behave
very differently -- picking the wrong one fails silently, with no error:

| Call | Sanitizes HTML? | Executes `<script>`? | Use for |
|---|---|---|---|
| `mo.md("...")` | Yes (strips `<iframe>`, `<script>`, etc.) | No | Normal prose/markdown |
| `mo.Html("...")` | No (raw HTML passes through) | **No** | Static HTML with no JS (a plain `<img>` or `<iframe src="...">` pointing at a URL) |
| `mo.iframe(html, width=, height=)` | No -- renders `html` as a real document via `<iframe srcdoc="...">` | **Yes** | Anything that needs JS to run (the quick-check buttons) |

Confirmed by direct test, not assumption: a `<script>` tag inside
`mo.Html()` silently never runs (no error, the DOM just never updates).
The same script inside `mo.iframe()` runs immediately, because it's
executing inside a genuine sandboxed document, not being innerHTML-injected
into the live page. **If a widget needs to react to a click, it must be
`mo.iframe()`, never `mo.Html()`.**

`mo.iframe()`'s first argument is an **HTML string to render**, not a URL
-- passing a URL there just dumps that text as invalid `srcdoc` content
and renders nothing. For a plain external embed (a URL), use
`mo.Html('<iframe src="...">...</iframe>')` instead.

## A bare `print()` cell silently vanishes from the slides layout

This is the single most important gotcha in this file, because it fails
**completely silently**: a code cell whose only effect is `print()` (no
`mo.md()`/`mo.Html()`/`mo.iframe()` return value) executes correctly --
its stdout shows up in the browser console, no error anywhere -- but is
**entirely absent from the rendered slide**. Not hidden, not empty:
absent. The cell's neighbors in the same slide's fragment sequence just
close the gap and renumber, so nothing even looks obviously wrong
without checking carefully.

Root cause: the marimo slides layout renders a cell's **output** (its
return value), not its **console output** (stdout/stderr). A cell that
only prints has no return value, so the slides renderer has nothing to
show for it. This is specific to the slides layout -- the exact same
cell shows its printed output fine in marimo's normal (non-slides) `run`
export, which is why this was easy to miss until a class that actually
uses several live print()-based demos (Class 6) surfaced it.

**The fix, after three rejected attempts**: don't execute these demos
live at all. Hand-type the code and its output as two separate fenced
blocks inside a single `hide_code=True` `mo.md()` cell -- the same
static-text convention already used elsewhere in this deck for the
`input()`-based examples, which can't execute live in a browser either:
```python
@app.cell(hide_code=True)
def _(mo):
    mo.md('''
    ```python
    for num in range(3):
        print(f'{num}:', end=' ')
        for n in range(5):
            print('*', end='')
        print()
    ```

    ```
    0: *****
    1: *****
    2: *****
    ```
    ''')
    return
```
No `mo`-specific call sits inside the code fence, no stdlib wrapper, no
duplicate hidden cell -- the block just *is* what the code and its
output look like, exactly matching the reading's own style.

This took three iterations to land on, each rejected for a concrete
reason -- don't re-litigate these without a new reason to revisit them:
- **A hidden real cell behind a "clean-looking" duplicate** -- more
  polished-looking, but the visible "example" wasn't the code actually
  running, and there was a second, invisible cell a reader couldn't
  inspect. Also turned out to be broken in practice: `hide_code=True`
  (the Python decorator) does **not** control code visibility in the
  exported slides HTML at all -- only the layout file's own `showCode`
  field does, and omitting it falls back to the global `--show-code`
  CLI default (`true`), not to `hide_code`. So a cell relying on
  `hide_code=True` alone to stay hidden showed its wrapper code anyway.
- **One single visible cell, wrapped in `contextlib.redirect_stdout` +
  `io.StringIO()`** (stdlib, not marimo-specific) -- real, visible,
  honest, and technically correct, but still didn't look like "code from
  the reading": a `with contextlib.redirect_stdout(...):` block and a
  trailing `mo.md(f"```\n{buf.getvalue()}\n```")` call are exactly the
  kind of "crazy callouts" a plain example shouldn't need.
- **`mo.capture_stdout()`** -- same shape as the above, marimo-specific
  instead of stdlib, same objection.
- **`mo.redirect_stdout()`** -- also considered early on; renders each
  individual `print()` call as its own separate paragraph, ignoring
  `end=''`/`end=' '` entirely, so a `0: *****` demo becomes an
  unreadable vertical list of single characters. Wrong regardless of the
  hiding question.

**The tradeoff, made explicit**: these cells no longer execute at all,
so nothing catches a hand-typed output block that's actually wrong.
Verify the output by actually running the equivalent code once (a
scratch REPL, a `python3 -c "..."` one-liner) before typing it into the
slide -- **especially** for anything involving `random` with a seed,
where a wrong-by-construction guess at the output is easy to make and
easy to miss on a read-through.

This is not optional polish -- audit every new deck for bare-print demo
cells and hand-type all of them this way, or their content will just be
missing with no error to catch it.

## The reactive redefinition rule (and how it fails)

marimo requires every variable to be defined in exactly one cell across
the whole deck -- reusing a name like a bare `for n in ...` loop variable,
or a `capture_stdout` buffer, in two different cells throws "This cell
redefines variables from other cells" and (worse) silently falls back
from topological to file-order cell execution, which can itself change
what actually renders (this is what caused the print-output bug above to
surface differently before vs. after an unrelated variable-naming fix in
the same deck -- fixing one bug changed the execution order, which
exposed the other).

Before trusting a new or edited deck, run marimo's own linter, and
separately scan for accidental name reuse it might not catch (tuple
unpacking, `with ... as x`, comprehension targets):
```bash
marimo check slides/ClassN/DeckN.py
```
```bash
python3 -c "
import ast
from collections import defaultdict
src = open('slides/ClassN/DeckN.py').read()
tree = ast.parse(src)
defsites = defaultdict(list)
def collect(node, names):
    if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
        names.add(node.id)
    elif isinstance(node, (ast.Tuple, ast.List)):
        for e in node.elts: collect(e, names)
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef) and node.name == '_':
        names = set()
        for n in ast.walk(node):
            if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store):
                names.add(n.id)
            elif isinstance(n, (ast.For, ast.comprehension)):
                collect(n.target, names)
            elif isinstance(n, ast.withitem) and n.optional_vars:
                collect(n.optional_vars, names)
        for name in names:
            if not name.startswith('_'):
                defsites[name].append(node.lineno)
for name, lines in defsites.items():
    if len(lines) > 1:
        print(name, lines)
"
```
An empty result from both means it's genuinely clean.

## The Colab-export trap, and how it's handled

marimo's `marimo export ipynb` flattens every `mo.md()` call into a real
Jupyter markdown cell, so nothing in the exported notebook still calls
`mo` -- except:

1. The untouched first cell (`import marimo as mo`) -- dead code after
   export, but still throws `ModuleNotFoundError` on Colab (marimo isn't
   installed there).
2. Any `mo.Html(...)` or `mo.iframe(...)` call -- these are **not**
   flattened by the exporter and stay as literal code cells, which
   `NameError` on `mo` for the same reason.

`strip_marimo_import.py` runs automatically (via `build_slides.sh`, right
after each `marimo export ipynb`) and fixes both:

- Removes the `import marimo as mo` statement. If a cell's source is
  exactly that one line, the whole cell is dropped; if marimo is
  imported alongside other, genuinely-needed stdlib imports, only the
  marimo import statement is removed (found via the cell's AST, not by
  assuming cell layout), keeping the rest of the cell as-is.
- Rewrites `mo.Html("<literal>")` into a plain markdown cell containing
  the equivalent raw HTML -- fine for static content with no `<script>`.
- **Splits `mo.iframe(...)` cells on a `<!-- colab-split -->` marker.**
  In this deck `mo.iframe()` is only ever a quick-check widget -- and
  since the question text and the A/B/C/D buttons now live in the
  *same* cell (see "Quick-check widgets" below for why), only the
  interactive half should disappear on Colab: the buttons POST to a
  live Google Form tied to that lecture's polling, meaningful for a
  student watching the slide during class and meaningless for someone
  opening this notebook later, disconnected from that lecture. The
  question text is real content worth keeping. So the html is split on
  a literal `<!-- colab-split -->` comment placed right before the
  button row: everything before it becomes a markdown cell; everything
  from the marker onward (buttons + submit script) is dropped. An
  `mo.iframe(...)` cell with no marker at all -- i.e. purely
  interactive, no question text merged in -- is dropped in full.

Two earlier versions tried to keep the button alive on Colab in some
form, both worth knowing about if you're tempted to redo this:
- Reconstructing an `<iframe srcdoc="...">` tag and turning the cell
  into markdown rendered as a **silently blank cell**, no error --
  confirmed by a real report after it shipped. Colab's markdown-cell
  sanitizer strips `<iframe>`/`<script>` tags out of markdown *source*.
- Calling `display(HTML(<literal>))` from a **code** cell instead
  actually worked -- Colab's code-cell *output* is trusted and
  unsanitized (confirmed against Colab's own official
  `advanced_outputs.ipynb` sample, which uses this exact pattern for a
  clickable button) -- but it was still machinery for a widget that,
  on reflection, doesn't belong in an async notebook at all. Dropping
  the cell (later, splitting it) turned out simpler and was what was
  actually wanted.

**If you introduce a new marimo call pattern that ends up in a code cell
after `ipynb` export** (anything other than `mo.md()`), check whether it
needs the same treatment: export the deck, open the resulting `.ipynb`,
and look for any cell still calling `mo.` after
`strip_marimo_import.py` has run. If you add handling for a new pattern,
extend that script the same way -- match the literal call via `ast`, only
convert cells that are *exactly* that one call with literal arguments, and
leave anything more dynamic alone rather than guessing.

### Hand-typed code+output cells become real code cells on Colab

The hand-typed `mo.md('''```python ... ``` \n\n ``` ... ```''')` cells
(see "A bare `print()` cell silently vanishes from the slides layout"
above) exist to dodge a **slides-layout-specific** bug -- Colab has no
such bug, and flattening one of these into an inert markdown block with
a fenced code snippet a student can't actually run would just be a
worse experience for no reason: Colab runs `print()`/`input()` cells
completely normally.

So `strip_marimo_import.py` treats this shape as a fifth case: a
markdown cell whose *entire* content is exactly a ```python fence
followed by a plain ``` output fence (optionally with a short trailing
caption after it, e.g. the "(unseeded -- yours will be different...)"
note) gets split back into a **real, runnable code cell** -- just the
extracted ```python body, unindented -- plus a separate trailing
markdown cell for any caption. The hand-typed *output* fence is dropped
entirely; running the cell for real produces its own output, and for
every seeded-random example in this deck that output is verified to
match what was hand-typed on the slide (run the equivalent code once
before writing the output block, same rule as writing the slide text in
the first place).

This means the two code shapes genuinely diverge on Colab vs. the
slide: the slide shows static text (because live execution isn't an
option there), Colab gets a live cell (because it is). Both show the
same code and the same output when nothing goes wrong -- verify that
stays true after editing one of these cells, by re-running the affected
Colab cell locally (or via `python3 -c "..."`) and diffing against the
slide's hand-typed output block.

## Quick-check widgets: how they work

Each quick-check is four custom buttons (A/B/C/D) that POST an answer
directly to a Google Form's backend -- not an embedded Google Forms
iframe. This was a deliberate choice: the visible Google Forms UI (its own
branding, "Question N" header, "Clear form" link) looked out of place
inside a dark-themed slide deck.

**One form per class, not one form per question.** Every quick-check
question for a given class lives as a separate question in the *same*
Google Form, so all of a class's responses land in one place with the
Summary tab's auto-generated pie chart per question already free, no
dashboard to build. Nothing about isolating one question's embed from
another requires separate forms -- since the trick is a direct POST to a
specific field (below), each question is addressable independently no
matter how many others share the form.

**How the mechanism works:**
1. Google Forms accepts a direct POST to
   `https://docs.google.com/forms/d/e/<FORM_ID>/formResponse` with
   `entry.<FIELD_ID>=<value>` in the body -- this is the same endpoint the
   visible form UI itself submits to, just called directly.
2. `mode: 'no-cors'` is required (cross-origin), which means the response
   can't be read back -- the widget shows an optimistic "Submitted: X" on
   click, not a confirmed one.
3. **Finding a question's field ID**: fetch the form's live `/viewform`
   page source and grep for `FB_PUBLIC_LOAD_DATA_` -- it's a JS array
   embedded in the raw HTML (not visible in the rendered form) that lists
   every question with its title and field ID:
   ```bash
   curl -s "https://docs.google.com/forms/d/e/<FORM_ID>/viewform" | grep -o "FB_PUBLIC_LOAD_DATA_.*"
   ```
   Each question appears as `[<question_id>, "<title>", null, 2,
   [[<FIELD_ID>, [["A",...],["B",...],...]]], ...]` -- the `<FIELD_ID>` is
   what goes after `entry.`. Do this instead of asking whoever owns the
   form to hunt for it via the "Get pre-filled link" menu.
4. **Naming questions in the form**: since students never see the form's
   own UI, the title only matters for whoever reviews the Summary tab
   later. Give each question a real identifying title (e.g. "Problem 2:
   range() bound"), not the default "Question N" -- otherwise the pie
   charts are meaningless out of context.

**The question and the buttons are one cell, not two.** An earlier
version had a separate `mo.md()` cell for the question (its own new
slide) followed by the `mo.iframe()` button widget marked as a
`{"type": "fragment"}` in the layout -- which meant the buttons stayed
hidden until the class advanced one more time past the question, an
extra step nobody asked for and a real report flagged directly ("make
the abcd appear w the question"). Tested directly rather than assumed:
marimo's slides layout format has exactly two states per cell --
`{}` (starts a brand new slide) or `{"type": "fragment"}` (hidden until
advanced) -- there's no third "part of the current slide, already
visible" option for a *second* cell. The only way to get the question
and the buttons to render together, immediately, is to put them in the
same cell.

**Widget markup** (the exact pattern used twice in
`slides/Class6/Class6.py` -- copy it for a new quick-check, only
changing the question text, the `entry.<FIELD_ID>`, and the answer
copy). The question/example/choices come first as hand-written HTML
(no marimo markdown rendering inside an iframe -- write the equivalent
tags directly), then a `<!-- colab-split -->` marker, then the buttons:
```python
mo.iframe(
    """
    <style> ...dark-theme styling for both the text and the buttons... </style>
    <h2>🎯 Quick Check: Predict Before You Code</h2>
    <p><strong>GPP Problem N</strong> asks for exactly this output:</p>
    <div class="gpp-output">...</div>
    <p>Which choice is correct?</p>
    <div class="choices">
      <p><strong>A.</strong> ...</p>
      ...
    </div>
    <p>📝 <strong>Submit your answer below:</strong></p>
    <!-- colab-split -->
    <div class="qc-row">
      <button class="qc-btn" data-choice="A">A</button>
      ...
    </div>
    <div class="qc-status"></div>
    <script>
    (function () {
      var buttons = document.querySelectorAll('.qc-btn');
      ...
      btn.addEventListener('click', function () {
        ...
        fetch('https://docs.google.com/forms/d/e/<FORM_ID>/formResponse', {
          method: 'POST', mode: 'no-cors',
          headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          body: 'entry.<FIELD_ID>=' + encodeURIComponent(choice),
        });
        status.textContent = 'Submitted: ' + choice;
      });
    })();
    </script>
    """,
    width="100%", height="480px",
)
```
The `<!-- colab-split -->` marker isn't decorative -- `strip_marimo_import.py`
looks for it verbatim to know where the interactive half starts (see
"The Colab-export trap" above). Forget it and the whole widget,
question text included, silently vanishes from the Colab export.

The answer reveal (`### ✅ Answer: ...`) stays a **separate**, ordinary
`mo.md()` cell marked as a fragment right after the widget -- unlike
the buttons, it's *supposed* to stay hidden until the instructor
chooses to advance past it, so the same fix doesn't apply there.

**What was ruled out, and why** (don't re-litigate these without a reason
to revisit them):
- **Embedding the Google Form directly** (`mo.Html('<iframe
  src=".../viewform?embedded=true">')`) -- worked, but showed Google's own
  UI/branding inside the slide. Replaced by the button approach above.
- **A custom widget backed by this platform's own shared-data tools**
  (Claude Artifacts' `db` capability) -- the platform's own docs state a
  `db`-declaring artifact "cannot be shared publicly... every reader and
  writer is a signed-in member of the owner's organization." Students
  aren't in that organization, so this is a hard platform limitation, not
  a config issue -- don't revisit this path for anonymous public response
  collection.
- **A separate Google Form per question** -- unnecessary once the direct-POST
  mechanism was in place, since a single form's questions are already
  independently addressable by field ID. Making many forms is real manual
  overhead for no benefit under this mechanism.

## Hand-authoring `layouts/*.slides.json`

marimo's slides layout file is a JSON array with exactly one entry per
cell in the deck's `.py` file, **in the same order**, including the first
`import marimo as mo` cell. Each entry is one of:
- `{}` -- this cell starts a **new slide**.
- `{"type": "fragment"}` -- this cell **appends to the current slide**,
  revealed as a fragment (progressive reveal via the right-arrow key).
- Either can add `"showCode": true/false` to override whether that cell's
  source is shown in presentation mode, independent of its
  `hide_code=True` setting in the `.py` file.

The established pattern: a `##`/`###` heading that starts a genuinely new
topic gets `{}`; everything that elaborates on it (an example, a
Takeaway, a code cell) gets `{"type": "fragment"}` until the next heading.
A quick-check's question markdown cell is its own new slide (`{}`); the
button-widget cell right after it is a fragment on that same slide.

There's no tooling to generate this automatically -- write the `.py` file
first, then walk its cells in order assigning directives by the rule
above. Verify the cell count matches
(`python3 -c "import ast; print(len([n for n in
ast.walk(ast.parse(open('slides/ClassN/DeckName.py').read())) if
isinstance(n, ast.FunctionDef) and n.name == '_']))"`) before trusting the
layout file.

## Testing a quick-check widget without polluting the real spreadsheet

Since the widget's `fetch()` call actually submits to the live form, a
real headless-browser click during testing would write a real (fake) row
into the class's response sheet. Intercept and abort the request instead
of letting it through, using Playwright:
```python
def handle_route(route, request):
    if "formResponse" in request.url:
        captured.append({"url": request.url, "post_data": request.post_data})
    route.abort()  # never actually reaches Google's servers
page.route("**/formResponse*", lambda route: handle_route(route, route.request))
```
Then click the button normally and assert on `captured` -- confirms the
exact field ID and value that *would* have been submitted, with zero
side effects on the real data.

**Jumping directly to a specific slide** (rather than pressing
`ArrowRight` in a loop, which is unreliable -- reveal.js keeps
off-screen slides in the DOM in a way that makes Playwright's
`is_visible()`/bounding-box checks report false positives for slides
that aren't actually on screen yet): load the page with a `#/<N>` hash,
e.g. `http://localhost:PORT/index.html#/5`. `N` is reveal.js's own
0-indexed horizontal slide count -- **not** the cell index or the count of
`{}` entries in the layout file starting from cell 0. In practice this
was off by exactly one from a naive count of `{}` entries (the `import
marimo as mo` cell doesn't appear to produce its own slide), but don't
assume that offset holds for a new deck -- confirm empirically (screenshot
after navigating) rather than trust the arithmetic.

## Archiving, never deleting

A deck or file superseded by a restructure (e.g. Class 6's old
`Class6_Lecture.py`/`Class6_GPP.py` split, replaced by the single
`Class6.py`) gets `git mv`'d into `archive/ClassN/`, not deleted --
matching the same rule the main EK125 repo follows.
`exclude_patterns` in `_config.yml` already excludes `archive/*` from
the built site.
