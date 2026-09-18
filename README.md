## For instructors: How this site works, and how to modify it

This site is a public, permanent companion to the main [EK125 site](https://github.com/BU-EK125/EK125). It publishes interactive [marimo](https://marimo.io) slide decks -- lecture slides, GPPs, and homework help sessions -- as live, runnable apps that execute in the browser via WebAssembly (Pyodide). No server, no sign-in, nothing for a student to install.

This repo works differently from the other EK125 sites, which are jupyter-book notebooks that execute directly. Here, jupyter-book only builds the *wrapper* pages (the sidebar, the intro, the page around each deck); the actual interactive content is a separately-exported marimo bundle, embedded via an `<iframe>`.

**The pieces:**
- `slides/ClassN/*.py` -- the actual marimo notebook source (plus its `layouts/*.slides.json` and `custom.css`, which marimo needs alongside the `.py` file to render the slides layout and styling correctly). Edit these with `marimo edit slides/ClassN/DeckName.py`.
- `build_slides.sh` -- exports every deck in `slides/` to a self-contained WASM HTML bundle under `_slides_build/<DeckName>/`. This runs automatically in CI (both `pr-check` and the deploy workflow); you don't need to run it yourself, and `_slides_build/` is never committed (it's regenerated every build, and each bundle is tens of MB, so keeping it out of git history matters).
- `pages/<DeckName>.md` -- a one-line wrapper page that iframes `../<DeckName>/index.html`. `_config.yml`'s `html_extra_path` is what makes `_slides_build/<DeckName>/index.html` show up at that path on the built site.
- `_toc.yml` -- one entry per wrapper page, organized into a part per class.

**To add a new deck:**

1. Author it with marimo (`marimo edit`), using the slides layout, and save it under a new `slides/ClassN/` folder alongside its `layouts/` and `custom.css`.
2. Add a wrapper page at `pages/DeckName.md`:
   ```markdown
   # Your Deck Title

   <iframe src="../DeckName/index.html" width="100%" height="800px" style="border:none;"></iframe>
   ```
3. Add `- file: pages/DeckName` to `_toc.yml` under the right class's `chapters:` (or add a new `caption:` part for a new class).
4. Open a pull request rather than pushing directly to `main`. A GitHub Actions check (`pr-check`) runs automatically: it exports every deck and builds the whole book, so a marimo file that fails to export will block the merge. Fix anything it flags before merging.
5. Once the PR is merged, GitHub Actions rebuilds and republishes the live site automatically -- no manual steps needed.

## https://BU-EK125.github.io/EK125-slides/intro.html
