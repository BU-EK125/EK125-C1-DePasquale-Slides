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

Classes 2-4 predate this format and still use the old Lecture+GPP split;
they haven't been retrofitted. Don't take them as the pattern for a new
class -- follow Class 6 (`slides/Class6/Class6.py`) instead.

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

- Removes the leftover `import marimo as mo` cell, but *only* when a
  cell's source is exactly that line -- won't touch it if a deck's first
  cell ever grows real setup code alongside the import.
- Rewrites `mo.Html("<literal>")` and `mo.iframe("<literal>", width=,
  height=)` calls into a plain markdown cell containing the equivalent raw
  HTML (an `mo.iframe` call gets reconstructed as an explicit
  `<iframe srcdoc="...">`, HTML-escaped) -- confirmed this renders and
  still executes its script when opened in Colab, the same way a plain
  `<iframe src="...">` already does there.

**If you introduce a new marimo call pattern that ends up in a code cell
after `ipynb` export** (anything other than `mo.md()`), check whether it
needs the same treatment: export the deck, open the resulting `.ipynb`,
and look for any cell still calling `mo.` after
`strip_marimo_import.py` has run. If you add handling for a new pattern,
extend that script the same way -- match the literal call via `ast`, only
convert cells that are *exactly* that one call with literal arguments, and
leave anything more dynamic alone rather than guessing.

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

**Widget markup** (the exact pattern used three times in
`slides/Class6/Class6.py` -- copy it for a new quick-check, only changing
the question text, the `entry.<FIELD_ID>`, and the answer copy):
```python
mo.iframe(
    """
    <style> ...dark-theme button styling... </style>
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
    width="100%", height="140px",
)
```

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
