## For instructors: How this site works, and how to modify it

This site is a public, permanent companion to the main [EK125 site](https://github.com/BU-EK125/EK125). It publishes interactive [marimo](https://marimo.io) slide decks -- lecture slides, GPPs, and homework help sessions -- as live, runnable apps that execute in the browser via WebAssembly (Pyodide). No server, no sign-in, nothing for a student to install.

This repo works differently from the other EK125 sites, which are jupyter-book notebooks that execute directly. Here, jupyter-book only builds the intro page and the sidebar; each deck in the sidebar is a plain external link straight to its own exported marimo page -- clicking it navigates you there directly (full page, no iframe), the same as clicking any other external link.

**The pieces:**
- `slides/ClassN/*.py` -- the actual marimo notebook source (plus its `layouts/*.slides.json` and `custom.css`, which marimo needs alongside the `.py` file to render the slides layout and styling correctly). Edit these with `marimo edit slides/ClassN/DeckName.py`.
- `build_slides.sh` -- exports every deck in `slides/` to a self-contained WASM HTML bundle under `_slides_build/<DeckName>/`. This runs automatically in CI (both `pr-check` and the deploy workflow); you don't need to run it yourself, and `_slides_build/` is never committed (it's regenerated every build, and each bundle is tens of MB, so keeping it out of git history matters).
- `_config.yml`'s `html_extra_path` is what copies `_slides_build/<DeckName>/index.html` onto the built site at `<DeckName>/index.html`.
- `_toc.yml` -- one `url:` entry per deck, pointing at its full published URL (e.g. `https://bu-ek125.github.io/EK125-slides/Class2_Lecture/index.html`), organized into a part per class. **Note:** because these are absolute URLs to the live site, sidebar links always go to the live site even when you're previewing a local `jb build` -- there's no local-preview equivalent for these links, only for the intro page itself.

**To add a new deck:**

1. Author it with marimo (`marimo edit`), using the slides layout, and save it under a new `slides/ClassN/` folder alongside its `layouts/` and `custom.css`.
2. Add an entry to `_toc.yml` under the right class's `chapters:` (or add a new `caption:` part for a new class):
   ```yaml
   - url: https://bu-ek125.github.io/EK125-slides/DeckName/index.html
     title: "Your Deck Title"
   ```
3. Open a pull request rather than pushing directly to `main`. A GitHub Actions check (`pr-check`) runs automatically: it exports every deck and builds the whole book, so a marimo file that fails to export will block the merge. Fix anything it flags before merging.
4. Once the PR is merged, GitHub Actions rebuilds and republishes the live site automatically -- no manual steps needed.

## https://BU-EK125.github.io/EK125-slides/intro.html

