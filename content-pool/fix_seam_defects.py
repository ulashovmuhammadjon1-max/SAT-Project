#!/usr/bin/env python3
"""
Repair "seam" defects: a word duplicated between an answer choice and the
passage text immediately after the blank.

## The defect

A Boundaries item is written so the choices carry the first word of the
following clause:

    passage:  "…a set of membranes is carried on each _____ two sources of sound…"
    choices:  "branch; two" / "branch, and two" / "branch two" / "branch: two"

Substituting any choice yields "each branch: **two two** sources of sound".
The intended sentence is "each branch: two sources of sound", so the passage
carries one copy too many.

It is invisible to every check the pipeline had, because each choice is
perfectly well formed **in isolation** — the defect only exists at the seam
where the choice meets the text after it. Reading the option list never shows
it; only substituting each choice and reading the whole sentence does.

## The repair

Delete the duplicated word from the **passage**, not the choices. The choices
are what the item is testing (which punctuation is legal), and all four carry
the word consistently, so the passage is the odd one out.

    python3 fix_seam_defects.py            # report only
    python3 fix_seam_defects.py --apply    # rewrite the affected testN.json
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RW = ("RW_M1", "RW_M2E", "RW_M2H")
APPLY = "--apply" in sys.argv


def text(html: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html or "")).strip()


def _doubles(s: str) -> set[str]:
    return {m.group(1).lower() for m in re.finditer(r"\b(\w+)\s+\1\b", s, re.I)}


def duplicated_word(passage_html: str, choice_html: str) -> str | None:
    """The word repeated across the seam, or None.

    Doublings already present in the passage are excluded. English has real
    ones — "Bora Bora", "had had", "that that" — and Test 7 was flagged purely
    because its passage names an island twice. A checker that cannot tell a
    genuine repetition from a defect produces findings nobody trusts.
    """
    already = _doubles(text(passage_html))
    filled = text(passage_html.replace("_____", text(choice_html), 1))
    for m in re.finditer(r"\b(\w+)\s+\1\b", filled, re.I):
        if m.group(1).lower() not in already:
            return m.group(1)
    return None


def repair_passage(passage_html: str, word: str) -> str | None:
    """Drop the passage's copy of `word` at the seam.

    The defect comes in two shapes, because a Boundaries choice spans the whole
    junction — the word before the punctuation and the word after it:

        after  "…on each _____ two sources…"      + "branch: two"
        before "…is watching _____ jackdaw…"      + "watching, a"

    In the first the passage repeats what the choice's tail supplies; in the
    second it repeats what the choice's head supplies. Both are the passage
    carrying a word the choice already has, so both are fixed by deleting the
    passage's copy — the choices are what the item tests and all four agree.

    Anchored to the blank in either direction, so the same word occurring
    elsewhere in the passage is left alone; several of these passages
    legitimately reuse it.
    """
    after = re.compile(r"(_____\s*)" + re.escape(word) + r"\b[ \t]*", re.I)
    if after.search(passage_html):
        return after.sub(r"\1", passage_html, count=1)

    before = re.compile(r"\b" + re.escape(word) + r"\b[ \t]*(?=_____)", re.I)
    if before.search(passage_html):
        return before.sub("", passage_html, count=1)

    return None


def main() -> int:
    findings, repaired, failed = [], 0, 0

    for n in range(1, 40):
        path = os.path.join(HERE, f"test-{n}-build", f"test{n}.json")
        if not os.path.exists(path):
            continue
        test = json.load(open(path))
        changed = False

        for key in RW:
            for i, q in enumerate(test.get(key, []), 1):
                passage = q.get("passage") or ""
                if "_____" not in passage:
                    continue

                words = {
                    w
                    for c in (q.get("choices") or [])
                    if (w := duplicated_word(passage, c.get("content", "")))
                }
                if not words:
                    continue

                hits = sum(
                    1
                    for c in (q.get("choices") or [])
                    if duplicated_word(passage, c.get("content", ""))
                )
                word = sorted(words)[0]
                findings.append((n, key, i, word, hits, len(q.get("choices") or [])))

                # A choice spans the whole junction, so a passage can repeat
                # the word on BOTH sides at once — "in Cairo _____ argued"
                # against "Cairo, argued". Repair repeatedly until clean.
                fixed, guard = passage, 0
                while guard < 4:
                    remaining = {
                        w
                        for c in (q.get("choices") or [])
                        if (w := duplicated_word(fixed, c.get("content", "")))
                    }
                    if not remaining:
                        break
                    nxt = repair_passage(fixed, sorted(remaining)[0])
                    if nxt is None or nxt == fixed:
                        fixed = None
                        break
                    fixed = nxt
                    guard += 1

                if fixed is None:
                    failed += 1
                    print(f"  ! Test {n} {key} Q{i}: could not repair {word!r} at the seam")
                    continue

                # Never trust the repair — re-check every choice against it.
                still = [
                    c["label"]
                    for c in (q.get("choices") or [])
                    if duplicated_word(fixed, c.get("content", ""))
                ]
                if still:
                    failed += 1
                    print(f"  ! Test {n} {key} Q{i}: still doubled for {still} after repair")
                    continue

                if APPLY:
                    q["passage"] = fixed
                    changed = True
                repaired += 1

        if changed and APPLY:
            json.dump(test, open(path, "w"), ensure_ascii=False, indent=1)

    print(f"\n{len(findings)} affected item(s):")
    for n, key, i, word, hits, total in findings:
        print(f"  Test {n:<3} {key:<7} Q{i:<3} duplicated {word!r:<14} ({hits}/{total} choices)")

    print(f"\n{'repaired' if APPLY else 'repairable'}: {repaired}   failed: {failed}")
    if not APPLY:
        print("Report only. Re-run with --apply to rewrite the affected testN.json files.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
