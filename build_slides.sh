#!/usr/bin/env bash
# Exports every marimo deck under slides/ClassN/*.py to a self-contained
# WASM HTML bundle at _slides_build/<DeckName>/index.html. Run this before
# `jb build .` -- _config.yml's html_extra_path copies _slides_build/* to
# the site root, and _toc.yml links directly to each deck's index.html.
set -euo pipefail

rm -rf _slides_build
mkdir -p _slides_build

for py_file in slides/*/*.py; do
  deck_name="$(basename "$py_file" .py)"
  deck_dir="$(dirname "$py_file")"
  echo "Exporting $py_file -> _slides_build/$deck_name"
  (cd "$deck_dir" && marimo export html-wasm "$(basename "$py_file")" \
    --mode run \
    --show-code \
    -o "$OLDPWD/_slides_build/$deck_name" \
    -f)
done
