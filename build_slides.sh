#!/usr/bin/env bash
# Exports every marimo deck under slides/ClassN/*.py to:
#  - a self-contained WASM HTML bundle at _slides_build/<DeckName>/
#    (gitignored, regenerated every build -- _config.yml's
#    html_extra_path copies it to the site root, and _toc.yml links
#    directly to each deck's index.html)
#  - a real .ipynb at notebooks/<DeckName>.ipynb (committed -- this is
#    what the 🚀 Colab button on each deck links to; Colab reads it
#    straight from GitHub, so it has to actually exist in the repo,
#    not just in a generated build artifact)
#
# Run this before `jb build .`. If you edited a deck locally, run this
# and commit the resulting notebooks/*.ipynb change too -- pr-check
# verifies they're in sync and fails if you forget.
set -euo pipefail

rm -rf _slides_build
mkdir -p _slides_build notebooks

for py_file in slides/*/*.py; do
  deck_name="$(basename "$py_file" .py)"
  deck_dir="$(dirname "$py_file")"
  echo "Exporting $py_file -> _slides_build/$deck_name"
  (cd "$deck_dir" && marimo export html-wasm "$(basename "$py_file")" \
    --mode run \
    --show-code \
    -o "$OLDPWD/_slides_build/$deck_name" \
    -f)
  echo "Exporting $py_file -> notebooks/$deck_name.ipynb"
  marimo export ipynb "$py_file" -o "notebooks/$deck_name.ipynb" -f
done
