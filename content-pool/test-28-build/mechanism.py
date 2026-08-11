#!/usr/bin/env python3
"""Mechanism search over the production Math stem bank.

Token-signature Jaccard measures VOCABULARY overlap. A template repeat that
keeps the mathematics and changes the setting words scores *low* precisely
because it changed the words — Test 25 replaced 34 of 66 questions and 19 of
them were never flagged by the ordinary score, six scoring below 0.30. This
module searches the other way round: it throws the setting vocabulary away and
keeps only what the question DOES.

Three independent signals, all of them deliberately blind to the setting:

  skeleton   every word not in a curated mathematical lexicon is deleted, and
             the LaTeX is reduced to structural markers (fraction, radical,
             square, function-notation, inequality, absolute value, table,
             percent, ratio...). Jaccard over what is left.
  numbers    the multiset of numeric literals in the stem, HTML stripped first
             so a table's "0.35rem" and "#D9DEE5" cannot contribute. Sharing
             three or more literals with a banked stem is the single clearest
             tell there is: the recorded cases (2x^2-12x+23, x^2+bx+45) were
             found by their coefficients, not their words.
  ask        the interrogative shape — "least possible value", "which
             expression is equivalent", "in terms of", "what is the
             probability", "greatest", "how many" — paired with the skill.

Usage:
    python3 mechanism.py sweep              # all 66, worst first, all signals
    python3 mechanism.py near "<text>" [k]  # pre-screen a candidate BEFORE writing it
    python3 mechanism.py show "<label>"     # print one banked stem in full

Reads ../prod_math_stems.json (READ ONLY).
"""
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(HERE, "..", "prod_math_stems.json")

# A curated mathematical lexicon. A word survives normalisation only if it is
# in here, so "coachbuilder", "farrier", "turnpike", "telescope" and every
# other setting noun vanishes and two questions that DO the same thing look
# alike however differently they are dressed.
LEXICON = set("""
add added addition sum total together difference subtract less more than twice
thrice double triple half quarter product multiply times divided divide quotient
per each every rate ratio proportion proportional percent percentage increase
decrease decreased increased reduced grew fell rise rises falls change constant
constants variable value values equal equals equivalent expression expressions
equation equations inequality inequalities system solution solutions solve
satisfies satisfy root roots zero zeros distinct real integer integers whole
positive negative least greatest maximum minimum most fewest smallest largest
possible exactly at how many what which following gives given defined function
functions linear quadratic exponential graph graphs slope intercept line lines
parallel perpendicular point points table shows records gives coordinate plane
vertex form factor factored factors factoring square squared cube cubed root
radical exponent power base term terms coefficient numerator denominator
fraction simplify simplified expand expanded mean median mode average range
probability random randomly selected chance likely data set sample survey
population estimate predict model modelled models approximately
angle angles degree degrees triangle triangles right isosceles equilateral
similar congruent hypotenuse leg legs side sides length lengths width height
depth perimeter area volume surface circle circles radius diameter circumference
arc sector cylinder cone sphere prism rectangle rectangular square trapezium
trapezoid parallelogram polygon quadrilateral diagonal altitude median bisect
midpoint sine cosine tangent opposite adjacent measure measures
in terms of interms substitute substituting absolute
""".split())

STRUCT = [
    (r"\\frac", "S:frac"),
    (r"\\sqrt", "S:sqrt"),
    (r"\^\{?2\}?", "S:square"),
    (r"\^\{?3\}?", "S:cube"),
    (r"\^\{?\\?frac", "S:fracexp"),
    (r"\^\{?[a-z]\}?", "S:varexp"),
    (r"\\pi", "S:pi"),
    (r"\\(sin|cos|tan)", "S:trig"),
    (r"\|[^|]+\|", "S:abs"),
    (r"[a-z]\s*\(\s*[a-z0-9]", "S:funcnot"),
    (r"(\\le|\\ge|<|>)", "S:ineq"),
    (r"\\circ", "S:deg"),
    (r"_\{?0\}?", "S:subzero"),
]

ASK = [
    (r"least (possible )?(value|number|integer)", "A:least"),
    (r"greatest (possible )?(value|number|integer)", "A:greatest"),
    (r"which (expression|of the following expressions) is equivalent", "A:equivform"),
    (r"in terms of", "A:interms"),
    (r"what is the probability", "A:prob"),
    (r"how many", "A:howmany"),
    (r"which equation", "A:whicheq"),
    (r"which inequality", "A:whichineq"),
    (r"what is the value of", "A:valueof"),
    (r"describes all values", "A:allvalues"),
    (r"(mean|average)", "A:mean"),
    (r"median", "A:median"),
    (r"displays?|reveals?", "A:displays"),
    (r"no real solutions|two distinct|exactly one solution", "A:discrim"),
    (r"infinitely many solutions", "A:infmany"),
    (r"table", "A:table"),
]


def plain(text):
    """Strip HTML (tags and attribute values both) and entities."""
    t = re.sub(r"<img[^>]*>", " ", text)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"&[a-z]+;", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def skeleton(text):
    """Setting-blind fingerprint: mathematical lexicon + structural markers."""
    t = plain(text)
    marks = []
    for pat, tag in STRUCT:
        if re.search(pat, t):
            marks.append(tag)
    for pat, tag in ASK:
        if re.search(pat, t, re.I):
            marks.append(tag)
    words = re.findall(r"[a-z]+", t.lower())
    kept = [w for w in words if w in LEXICON]
    return set(kept) | set(marks)


def numbers(text):
    """Numeric literals in the stem, HTML removed first.

    A table's style attribute carries 0.35rem, 0.6rem, 1px and #D9DEE5; every
    one of them would otherwise be counted as a coefficient, and every table
    question in the bank would look alike.
    """
    t = plain(text)
    t = t.replace(",", "")
    out = []
    for mo in re.finditer(r"(?<![\w.])\d+(?:\.\d+)?(?![\w.])", t):
        v = mo.group(0)
        f = float(v)
        if f in (0.0, 1.0, 2.0):
            continue  # too common to carry information
        out.append(v.rstrip("0").rstrip(".") if "." in v else v)
    return Counter(out)


def jac(a, b):
    return len(a & b) / max(1, len(a | b))


def numshare(a, b):
    return sum((a & b).values())


def load():
    return json.load(open(BANK))


def report(text, rows, k=6, label=None):
    s0, n0 = skeleton(text), numbers(text)
    scored = []
    for r in rows:
        sk = jac(s0, skeleton(r["stem"]))
        ns = numshare(n0, numbers(r["stem"]))
        scored.append((sk, ns, r))
    by_sk = sorted(scored, key=lambda z: -z[0])[:k]
    by_ns = sorted(scored, key=lambda z: (-z[1], -z[0]))[:k]
    print(f"### {label or plain(text)[:70]}")
    print("  -- by mechanism skeleton")
    for sk, ns, r in by_sk:
        print(f"     {sk:.2f} n{ns}  {r['label']}: {plain(r['stem'])[:170]}")
    print("  -- by shared numeric literals")
    for sk, ns, r in by_ns:
        if ns < 2:
            break
        print(f"     n{ns} {sk:.2f}  {r['label']}: {plain(r['stem'])[:170]}")
    print()
    return max(z[0] for z in scored), max(z[1] for z in scored)


def main():
    rows = load()
    mode = sys.argv[1] if len(sys.argv) > 1 else "sweep"
    if mode == "near":
        report(sys.argv[2], rows, int(sys.argv[3]) if len(sys.argv) > 3 else 6)
    elif mode == "show":
        for r in rows:
            if r["label"] == sys.argv[2]:
                print(plain(r["stem"]))
    else:
        from math_test28 import ALL
        k = int(sys.argv[2]) if len(sys.argv) > 2 else 4
        for q in ALL:
            report(q["stem"], rows, k, label=f"{q['n']} [{q['skill']}] "
                                             + plain(q["stem"])[:90])


if __name__ == "__main__":
    main()
