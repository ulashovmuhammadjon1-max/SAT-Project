#!/usr/bin/env bash
# Rebuild and re-apply every passage fix for Tests 6-15, IN ORDER.
#
# The order is not optional. fix_passage_html.py regenerates a passage from the
# source PDF, so it necessarily discards anything layered on top of it — the
# rebuilt tables, the rebuilt charts and the recovered <u> spans all live only
# in the database. Running it alone silently reverted 64 fixed questions once.
#
# This is the trap CLAUDE.md already records for Math ("do NOT regenerate stems
# from the original source JSON/pool ... regenerating silently destroys those
# fixes"). The same applies here, so the regeneration and the re-application
# are one script rather than four things to remember.
#
#   DATABASE_URL=… bash rebuild_passages.sh
set -euo pipefail
cd "$(dirname "$0")/../.."
: "${DATABASE_URL:?Set DATABASE_URL}"
D=content-pool/cb-question-bank
TMP=$(mktemp -d)

echo "1/4  regenerate passage HTML from source"
python3 $D/fix_passage_html.py "$TMP/passages.json" $D/rw_tests_6_10.json $D/rw_tests_11_15.json

echo "2/4  apply base passages"
node $D/apply_passage_fixes.mjs "$TMP/passages.json" --apply | tail -1

echo "3/4  re-apply rebuilt figures (tables, then charts)"
node $D/apply_passage_fixes.mjs $D/tables.json  --apply | tail -1
node $D/apply_passage_fixes.mjs $D/charts9.json --apply | tail -1

echo "4/4  re-apply recovered underlines (last: they edit whatever text is current)"
node $D/apply_underlines.mjs $D/underlines.json --apply | tail -1

echo
echo "audit:"
node $D/audit_rw.mjs 6 15
rm -rf "$TMP"
