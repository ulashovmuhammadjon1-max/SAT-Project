"""Export authored AP topic banks to JSON for insertion.

Each topic module defines TOPIC = (code, title, unit) and QUESTIONS.
Choices are shuffled with a per-topic deterministic seed so the answer key
spreads across A-E; numeric ladders keep their written order.

Math notation is typeset into KaTeX by mathfmt.convert on the way OUT, not in
the modules themselves. The modules stay in the plain-text notation the briefs
specified, which is what every verify_*.py asserts against and what a human
edits; converting here means the two cannot drift, and re-running the export is
idempotent because convert() is a pure function of the source string.
"""
import argparse
from collections import Counter
import importlib
import json
import random
import re
import sys

from mathfmt import convert as tex

NUMERICISH = re.compile(
    r"^[\s$€£%\d.,/+\-]*(tons?|utils?|bolts?|units?|steel|coal|cars?|trucks?|cakes?|pies?|"
    r"wheat|cloth|phones?|drones?|glass(es)?|movies?|slices?|Pepsis|books?|pens?|bicycles?|"
    r"computers?|guns?|butter|loaves|loaf|bread|cheese|tables?|chairs?|hamburgers?|pretzels?|"
    r"smoothies?|muffins?|fish|coconuts?|houses?|tractors?|of|per|for|and|a|an|the|"
    r"[\s$€£%\d.,/+\-])*$",
    re.IGNORECASE,
)


def numeric_ladder(choices):
    return all(NUMERICISH.match(c) and re.search(r"\d", c) for c in choices)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("modules", nargs="+", help="module names, e.g. u2_1 u2_2")
    ap.add_argument("--subject", default="MICRO")
    # Questions per CED topic, by subject. These differ because the courses
    # subdivide differently: Calculus lists the disc and washer methods as four
    # separate topics, so fifty each would be padding, while an economics topic
    # is broad enough to carry fifty honestly. The count is still checked
    # EXACTLY -- the point of the gate is that a short module cannot ship by
    # accident, so a new subject must be added here rather than defaulted.
    ap.add_argument("--per-topic", type=int, default=None,
                    help="questions required per topic; defaults to the subject's count")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    PER_TOPIC = {
        "MICRO": 50, "MACRO": 50,
        "CALC_AB": 25, "CALC_BC": 25,
        "STATISTICS": 25,
        "PSYCHOLOGY": 30,
        "HUMAN_GEO": 30, "US_GOV": 30, "COMP_GOV": 30,
    }
    expected = args.per_topic
    if expected is None:
        expected = PER_TOPIC.get(args.subject)
        if expected is None:
            sys.exit(
                f"unknown subject {args.subject!r}: add it to PER_TOPIC or pass --per-topic"
            )

    out, dist, seen_stems = [], {c: 0 for c in "ABCDE"}, {}
    for mod_name in args.modules:
        m = importlib.import_module(mod_name)
        code, title, unit = m.TOPIC
        qs = m.QUESTIONS
        if len(qs) != expected:
            sys.exit(f"{mod_name}: expected {expected} questions, found {len(qs)}")
        rng = random.Random(int(code.replace(".", "")) * 7919)

        # One balanced bag of key positions per choice-count, consumed as the
        # questions are walked.
        #
        # Numeric ladders are deliberately left in their written order, so
        # their keys sit wherever the author put them and cannot be moved. The
        # bag therefore has to COMPENSATE for them: count the ladder keys
        # first, then hand the movable questions the positions that level the
        # topic's totals. Balancing only the movable questions is not enough --
        # it left 16 topics still at 40% or more on one letter, because the
        # ladders were pulling the totals on their own.
        key_slots = {}
        for width in (4, 5):
            fixed = Counter(
                it["ans"]
                for it in qs
                if len(it["choices"]) == width and numeric_ladder(it["choices"])
            )
            movable = sum(
                1
                for it in qs
                if len(it["choices"]) == width and not numeric_ladder(it["choices"])
            )
            # Repeatedly hand the next slot to whichever position is furthest
            # behind, so the final totals differ by at most one.
            slots = []
            running = Counter(fixed)
            for _ in range(movable):
                pos = min(range(width), key=lambda k: (running[k], k))
                slots.append(pos)
                running[pos] += 1
            rng.shuffle(slots)
            key_slots[width] = slots
        for i, item in enumerate(qs, 1):
            choices, ans = list(item["choices"]), item["ans"]
            # Five choices for econ (A-E), four for calculus (A-D).
            if len(choices) not in (4, 5) or not 0 <= ans < len(choices):
                sys.exit(f"{mod_name} q{i}: needs 4-5 choices and a valid answer index")
            if len(set(choices)) != len(choices):
                sys.exit(f"{mod_name} q{i}: duplicate answer choices")
            # A stem repeated inside one subject means an accidental clone.
            key = item["q"][:90].lower()
            if key in seen_stems and seen_stems[key] != (code, i):
                print(f"  warn: near-duplicate stem {mod_name} q{i} vs {seen_stems[key]}")
            seen_stems.setdefault(key, (code, i))

            if not numeric_ladder(choices):
                # Place the key at a position drawn from a balanced sequence
                # rather than shuffling blind. A blind shuffle only RELOCATES
                # the clustering in the source: modules are written key-first,
                # so nearly every ans is 0, and a single seed over 25 questions
                # lands badly often enough to matter -- 37 of 111 Calculus
                # topics had 40% or more of their keys on one letter, the worst
                # at 52%. A student who always guessed that letter would score
                # 52% on that topic, which is a defect in the bank, not a quirk.
                target = key_slots[len(choices)].pop()
                order = [k for k in range(len(choices)) if k != ans]
                rng.shuffle(order)
                order.insert(target, ans)
                choices = [choices[k] for k in order]
                ans = target
            dist["ABCDE"[ans]] += 1
            # Typeset AFTER the shuffle, so the conversion cannot disturb
            # choice order or the answer key.
            table = item.get("table")
            if table:
                table = dict(
                    headers=[tex(h) for h in table["headers"]],
                    rows=[[tex(c) for c in row] for row in table["rows"]],
                )
            out.append(
                dict(
                    subject=args.subject, unit=unit, topic=code, topicTitle=title, order=i,
                    stem=tex(item["q"]), table=table, choices=[tex(c) for c in choices],
                    correctIndex=ans, explanation=tex(item["why"]),
                )
            )
    json.dump(out, open(args.out, "w"))
    print(f"{len(out)} questions -> {args.out}; answer spread: {dist}")


if __name__ == "__main__":
    main()
