"""Export authored AP topic banks to JSON for insertion.

Each topic module defines TOPIC = (code, title, unit) and QUESTIONS.
Choices are shuffled with a per-topic deterministic seed so the answer key
spreads across A-E; numeric ladders keep their written order.
"""
import argparse
import importlib
import json
import random
import re
import sys

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
    # Economics carries 50 questions per CED topic. Calculus carries 25: its CED
    # subdivides far more finely (the disc and washer methods are four separate
    # topics), so fifty would be padding. The count is still checked exactly --
    # the point of the gate is that a short module cannot ship by accident.
    ap.add_argument("--per-topic", type=int, default=None,
                    help="questions required per topic; defaults to 25 for Calculus, 50 otherwise")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    expected = args.per_topic
    if expected is None:
        expected = 25 if args.subject.startswith("CALC") else 50

    out, dist, seen_stems = [], {c: 0 for c in "ABCDE"}, {}
    for mod_name in args.modules:
        m = importlib.import_module(mod_name)
        code, title, unit = m.TOPIC
        qs = m.QUESTIONS
        if len(qs) != expected:
            sys.exit(f"{mod_name}: expected {expected} questions, found {len(qs)}")
        rng = random.Random(int(code.replace(".", "")) * 7919)
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
                order = list(range(len(choices)))
                rng.shuffle(order)
                choices = [choices[k] for k in order]
                ans = order.index(ans)
            dist["ABCDE"[ans]] += 1
            out.append(
                dict(
                    subject=args.subject, unit=unit, topic=code, topicTitle=title, order=i,
                    stem=item["q"], table=item.get("table"), choices=choices,
                    correctIndex=ans, explanation=item["why"],
                )
            )
    json.dump(out, open(args.out, "w"))
    print(f"{len(out)} questions -> {args.out}; answer spread: {dist}")


if __name__ == "__main__":
    main()
