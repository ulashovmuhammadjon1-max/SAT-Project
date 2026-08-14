"""
Combine parsed question-bank parts into one deduped file, and flag anything
already present in the live bank.

    python3 combine_parts.py <out.json> <part1.json> <part2.json> …

Two separate dedupe passes, because they catch different things:

1. **Within the supplied parts.** The parts are page ranges of one export and
   their boundaries overlap by a page, so the same question legitimately
   appears in two files. One part has also arrived twice as a straight re-send.
   Keyed on the official `Question ID`, which is exact and stable — no
   heuristic needed.

2. **Against the questions already banked.** Keyed on normalised stem text,
   not on id, because a question transcribed into an earlier test from this
   same College Board source carries no official id in our database. Matching
   is on the first 120 normalised characters: enough to identify the passage,
   short enough to survive the punctuation and markup differences between a
   hand-transcribed copy and this export.

Flags rather than drops. A question already in the bank is left in the file
with `already_in_bank: true` so the import step can decide — dropping it here
would hide a real overlap from review.
"""
import json
import os
import re
import subprocess
import sys
from collections import Counter


def norm(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = s.replace("&nbsp;", " ").replace("’", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"\s+", " ", s).strip().lower()
    return re.sub(r"[^a-z0-9 ]", " ", s).strip()


def load_bank_keys():
    """Normalised passage+stem for every question already in the database."""
    url = os.environ.get("DATABASE_URL")
    if not url:
        print("DATABASE_URL not set — skipping the already-in-bank check")
        return set()
    url = re.sub(r"\?schema=public$", "", url.strip().strip('"'))
    rows = subprocess.run(
        ["psql", url, "-t", "-A", "-F", "\t", "-c",
         'SELECT COALESCE(p.content, \'\'), q.stem FROM "Question" q '
         'LEFT JOIN "Passage" p ON p.id = q."passageId"'],
        capture_output=True, text=True,
    ).stdout.strip().split("\n")
    keys = set()
    for r in rows:
        parts = r.split("\t")
        if len(parts) >= 2:
            keys.add(norm(parts[0] + " " + parts[1])[:120])
    return keys


def main():
    out, parts = sys.argv[1], sys.argv[2:]
    seen, dupes, repaired = {}, 0, 0

    def better(a, b):
        """Pick the more complete of two records for the same question id.

        A question that straddles a split boundary appears truncated in the
        earlier part — its `Correct Answer` and `Rationale` live in the next
        file — and complete in the later one. Keeping whichever arrived first
        would silently prefer the broken copy, so completeness decides:
        a clean parse beats an error, then a longer rationale wins.
        """
        if ("error" in a) != ("error" in b):
            return b if "error" in a else a
        return max(a, b, key=lambda q: len(q.get("rationale", "")))

    for p in parts:
        qs = json.load(open(p))
        new = 0
        for q in qs:
            prev = seen.get(q["id"])
            if prev is None:
                seen[q["id"]] = q
                new += 1
            else:
                dupes += 1
                pick = better(prev, q)
                if pick is not prev:
                    seen[q["id"]] = pick
                    repaired += 1
        print(f"{os.path.basename(p):48} {len(qs):>4} parsed  {new:>4} new")
    if repaired:
        print(f"\n{repaired} truncated record(s) replaced by a complete copy from a later part")

    all_q = list(seen.values())
    bank = load_bank_keys()
    for q in all_q:
        q["already_in_bank"] = bool(bank) and norm(q.get("question", ""))[:120] in bank

    fresh = [q for q in all_q if not q["already_in_bank"]]
    print(f"\nunique          {len(all_q)}  (duplicates across parts: {dupes})")
    print(f"already in bank {sum(1 for q in all_q if q['already_in_bank'])}")
    print(f"new to import   {len(fresh)}")
    print(f"need a figure   {sum(1 for q in fresh if q.get('needs_figure'))}")
    print(f"\nskills:      {dict(Counter(q['skill'] for q in fresh))}")
    print(f"difficulty:  {dict(Counter(q['difficulty'] for q in fresh))}")
    print(f"answer keys: {dict(Counter(q['correct'] for q in fresh))}")

    json.dump(all_q, open(out, "w"), indent=1)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
