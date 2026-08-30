"""Step 2 of 3: typeset the dumped AP rows, and prove nothing else moved.

    python3 convert_db_rows.py dump.json patch.json

Reads the rows dumped from the database, runs every string through
mathfmt.convert, and writes only the rows that actually changed.

The invariants asserted here are the point of the script, not decoration.
Anything that shifts a choice's position, changes how many choices there are,
or moves the answer key would corrupt every `ApQuestionAttempt` already stored
against that question -- a student's saved index would start pointing at a
different answer. So the script refuses to emit a patch at all if any of that
happens, rather than emitting a partly-good one.
"""
import json
import re
import sys

from mathfmt import convert

SPAN = re.compile(r"\\\((.+?)\\\)", re.S)


def strip_spans(s):
    """The text with every math span replaced by its own source, which is what
    the round trip inside convert() guaranteed it still says."""
    return SPAN.sub(" ", s)


def main():
    dump, out = sys.argv[1], sys.argv[2]
    rows = json.load(open(dump))
    patch, spans, changed = [], [], 0

    for r in rows:
        choices = r["choicesJson"]
        if isinstance(choices, str):
            choices = json.loads(choices)
        table = r.get("tableJson")
        if isinstance(table, str):
            table = json.loads(table)

        new_stem = convert(r["stem"])
        new_choices = [convert(c) for c in choices]
        new_expl = convert(r["explanation"]) if r["explanation"] else r["explanation"]
        new_table = None
        if table:
            new_table = dict(
                table,
                headers=[convert(h) for h in table["headers"]],
                rows=[[convert(c) for c in row] for row in table["rows"]],
            )

        # Invariants. A conversion may only ever re-typeset a string.
        assert len(new_choices) == len(choices), f"{r['id']}: choice count changed"
        assert all(isinstance(c, str) for c in new_choices), f"{r['id']}: non-string choice"
        if new_table:
            assert len(new_table["rows"]) == len(table["rows"]), f"{r['id']}: rows changed"
            assert all(len(a) == len(b) for a, b in zip(new_table["rows"], table["rows"])), \
                f"{r['id']}: row width changed"

        dirty = (new_stem != r["stem"] or new_choices != choices
                 or new_expl != r["explanation"]
                 or (new_table is not None and new_table != table))
        if not dirty:
            continue
        changed += 1
        for s in [new_stem, new_expl or ""] + new_choices:
            for m in SPAN.finditer(s):
                spans.append([r["id"], m.group(1)])
        patch.append(dict(id=r["id"], stem=new_stem, choices=new_choices,
                          explanation=new_expl, table=new_table,
                          correctIndex=r["correctIndex"]))

    json.dump(patch, open(out, "w"))
    json.dump(spans, open(out + ".spans.json", "w"))
    print(f"{len(rows)} rows read, {changed} to update, {len(spans)} math spans")
    print(f"wrote {out} and {out}.spans.json")


if __name__ == "__main__":
    main()
