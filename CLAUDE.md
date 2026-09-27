# Cross-repo context for EK125-C1-DePasquale-Slides

This file exists to carry over knowledge from work done in the other EK125
repos that isn't written down anywhere in this repo's own README.md or
CONVENTIONS.md (both of which are authoritative for this repo's own
mechanics -- marimo deck format, build pipeline, quick-check mechanism, etc.
Don't duplicate those here; read them first).

## The repo map

- **EK125** (`BU-EK125/EK125`) -- the main, public, permanent jupyter-book
  site. Student-facing. This is the canonical source for reading content,
  GPP problem statements, and (as of Fall 2026) homework problem statements.
- **EK125-notebooks** (`BU-EK125/EK125-notebooks`, private) -- the
  instructor-side staging/source repo everything gets ported *from*. It is
  **not always trustworthy as-is**: files there have repeatedly turned out
  stale (old grading rubrics, missing content added later) or polluted
  (worked answers baked into what should be blank GPP scaffolds, joke
  placeholder names left over from testing). Always cross-check against
  what students are actually currently given before trusting it.
- **EK125-C1-DePasquale-Slides** (this repo) -- public marimo slide decks,
  built as a separate jupyter-book site with external links to WASM-exported
  decks. Content here (lecture walkthroughs, quick-checks) should be sourced
  from and stay consistent with the main EK125 site's readings and GPPs.
- **EK1225-IPP** (public; typo'd name, "1225" not "125", permanent -- don't
  rename without asking) -- a sibling site cloned from this repo's own
  pattern, publishing per-class Individual Practice Problem (IPP) decks.
  **Convention established there that applies here too by contrast: IPP
  decks show questions only, no answer reveal -- GPP decks in this repo
  may use a reveal-on-click fragment for quick-checks, IPP decks should
  not.** If this repo's pattern gets cloned to yet another new repo, note
  that `colab_button.html` has the source repo's org/name **hardcoded**
  and needs manual find-and-replace (confirmed while building EK1225-IPP;
  `build_slides.sh` and `strip_marimo_import.py` have no such hardcoding).
- **EK125-hw-help**, **EK125-discussions** (public) -- companion sites for
  homework-help-session and discussion-section notebooks. Not yet audited
  by any Claude session; check their own docs before assuming this file's
  conventions apply.
- **EK125-Instructors** (private) -- exists, purpose not yet documented.
- **EK125WIP** (`briandepasquale/EK125WIP`, personal, not under the
  BU-EK125 org) -- the raw-material working folder, organized by semester
  (`S26`/`F25`/`F26`/`copyOfShared`). **Marimo lecture-deck drafts for
  Classes 2-4 already exist at `F26/Class {2,3,4}/Slides/`** (full
  `ClassN_Lecture.py`/`ClassN_GPP.py`/`HWN_*_Help_Session.py` families with
  `layouts/` and `custom.css`), built but never pushed here -- **check
  there before redrafting a lecture deck for one of these classes from
  scratch.** Also note: GPP source files there can exist in both a
  solutions-bearing variant (e.g. `Class_2_GPP.ipynb`) and a clean variant
  (e.g. `Class_2_GPP_corrected.ipynb`) -- always confirm which one you're
  building a public deck from; the solutions-bearing one must never be the
  source for anything published here.

## Course structure (Acts)

- **Act 1 = "Python in Colab"**: Classes 1-7. (Class 8 does not exist --
  the numbering intentionally jumps 7 to 9; not a gap to fill.)
- **Act 2 = "Python in an IDE"**: starts around Class 9.
- **Act 3 = MATLAB**: starts at Class 16 (a Python-to-MATLAB bridge class).

## Content privacy policy (governs what can be public, anywhere)

The main EK125 site's README states the baseline rule: no solutions, no
quizzes/exams, no IPPs published anywhere public -- Blackboard or similar is
where assessment/answer content lives. As of Fall 2026 there are exactly
two deliberate, scoped exceptions, decided explicitly by the instructor and
not to be extended further without being asked:

1. **Homework problem statements** (not solutions) -- homework is now
   graded for submission only, not correctness, so the prompts themselves
   can be public.
2. **GPP solutions for Act 1 (Classes 1-7) only.** Explicitly not extended
   to Act 2/Act 3 GPP solutions or to any homework solutions.

If this repo ever surfaces GPP solution content (e.g. in a slide's
answer-reveal), the same Act-1-only boundary applies.

## The PII lesson (important, hard-won)

Raw notebook files sourced from EK125-notebooks can contain **real personal
information** embedded in Colab execution metadata -- `executionInfo.user.
displayName` / `userId` on individual cells, and `colab.provenance.file_id`
/ `timestamp` at the notebook level. This was found by inspecting raw JSON,
not visible in any rendered preview.

**Rule: never copy a cell directly from an EK125-notebooks source file into
anything public.** Always rebuild each cell from scratch, keeping only
`cell_type` and the joined `source` text, with fresh minimal metadata
(`{"id": <new-uuid>}`) -- discard everything else. This applies to any
content pulled into this repo's decks too, not just the main site's GPP
solutions.

## Sourcing/auditing pattern

When porting or referencing content from EK125-notebooks or EK125WIP,
cross-check against what students are *actually currently given* (a real
downloaded copy of the assignment/GPP, not just the internal source) before
trusting it. This has repeatedly caught real problems: dropped content,
stale grading language that predates policy changes, and stray scratch
cells left over from someone editing a file interactively.

## Main-site build conventions worth knowing

- The main EK125 site executes every notebook for real at build time
  (`execute_notebooks: force`). Tags used there: `skip-execution` (blank
  scaffold cells, or complete solution cells with `input()` -- the latter
  need a baked, execution-verified transcript in the cell's `outputs`);
  `raises-exception` (cells that intentionally error as a teaching demo).
- A subtle `_toc.yml` / sphinx-external-toc bug: a class page with **more
  than one top-level `#` (H1) heading** (instead of `##` for its major
  sections) silently drops its nested TOC children from the sidebar --
  the page still builds cleanly and is directly reachable, it's just
  invisible in navigation. Keep exactly one real H1 per page.
- PRs there never auto-merge without explicit instructor go-ahead. Stacked
  PRs (branched off another not-yet-merged PR) get auto-*closed* (not
  retargeted) by GitHub once the base PR merges and its branch is deleted
  -- recovery is to rebase (or cherry-pick, if the base commit was itself
  rebased to a new hash) onto the fresh `main` and open a replacement PR.

## Lecture-deck fidelity-audit process (reusable)

Established pattern from building the F26 drafts in EK125WIP: source a
lecture deck only from that class's GPP notebook + its lecture PDF + the
*public* reading page (`bu-ek125.github.io/EK125/ClassN.html`), then
self-audit turn-by-turn ("is everything in the lecture in the html
reading?") producing a slide-by-slide fidelity table against the reading.
Worth reusing for any future lecture-deck work in this repo -- cite the
source per slide, then verify against the live public reading URL before
considering a deck done.

## Where to look next

- This repo's own **CONVENTIONS.md** and **README.md** for how decks,
  quick-checks, and the build pipeline actually work here.
- The main **EK125** repo's **CONVENTIONS.md** and **README.md** for the
  authoritative reading/GPP/homework porting patterns, cross-reference and
  common-mistake auditing standards, and the GPP-solutions porting pattern
  (including the PII-stripping step above, described there in full).
