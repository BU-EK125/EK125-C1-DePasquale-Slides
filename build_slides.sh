#!/usr/bin/env bash
# Exports every marimo deck under slides/ClassN/*.py to a self-contained
# WASM HTML bundle at _slides_build/<DeckName>/index.html. Run this before
# `jb build .` -- the book's wrapper pages iframe-embed these bundles, and
# _config.yml's html_extra_path copies _slides_build/* to the site root.
set -euo pipefail

rm -rf _slides_build
mkdir -p _slides_build

for py_file in slides/*/*.py; do
  deck_name="$(basename "$py_file" .py)"
  deck_dir="$(dirname "$py_file")"
  echo "Exporting $py_file -> _slides_build/$deck_name"
  (cd "$deck_dir" && marimo export html-wasm "$(basename "$py_file")" \
    --mode run \
    -o "$OLDPWD/_slides_build/$deck_name" \
    -f)
done
