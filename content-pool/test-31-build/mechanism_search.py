#!/usr/bin/env python3
"""
Mechanism search over the production Math bank.

Why this exists, and why the Jaccard screen in verify_math_test31.py is not
enough on its own: Test 25 replaced 34 of its 66 Math questions and **19 of
those were never flagged by the similarity screen at all**, six of them scoring
below 0.30. A token-signature Jaccard measures the *words*. A template repeat
that keeps the mathematics and changes the setting therefore scores LOW
precisely because it changed the words — the setting is most of the token mass
in an SAT stem.

So this tool asks the opposite question. For each of Test 31's 66 questions it
names the *mechanism* — the mathematical move the student has to make, stated
independently of any setting — and counts how many banked stems make the same
move. A high count is not a failure; it is a reading list. The point is to see
"9 banked items already recover a side from a tangent ratio" before shipping a
tenth, and to pick replacement mechanisms from the low-count end.

Two rules learned the hard way and enforced here:

  * **Every probe uses explicit lookarounds, never `\\b`.** The first draft of
    this file probed for arc-length with the bare substring `arc` and reported
    29 hits. Most of them were the word **March**. `\\b` would not have helped
    either where a token can abut a digit. A boundary-free substring match in a
    checker is worse than no check, because it trains you to ignore the output.
  * **Probes run on the stripped text.** `<img>` first (a base64 payload
    matches nearly anything), then all remaining tags, then entities.

Usage
    python3 mechanism_search.py              # every mechanism, with counts
    python3 mechanism_search.py --read 8     # print exemplars where count >= 8
    python3 mechanism_search.py --probe "arc length of a sector"
    python3 mechanism_search.py --free       # mechanisms the bank barely uses
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROD = os.path.join(HERE, "..", "prod_math_stems.json")


def strip(html):
    tx = re.sub(r"<img[^>]*>", " ", html)
    tx = re.sub(r"<[^>]+>", " ", tx)
    tx = tx.replace("&deg;", " degrees ").replace("&nbsp;", " ")
    tx = re.sub(r"&[a-z]+;", " ", tx)
    return re.sub(r"\s+", " ", tx)


def W(word):
    """A whole word, with an explicit lookbehind and lookahead.

    Not `\\b`: a digit and a letter are both word characters, so `\\bpi` never
    matches in "3pi", and `\\bfen` happily matches the "fen" inside "fence".
    """
    return r"(?<![A-Za-z])" + word + r"(?![A-Za-z])"


# Each entry: mechanism name -> regex over the stripped stem. The name states
# the mathematical move with no setting words in it at all, which is the whole
# point of the exercise.
MECHANISMS = {
    # ---- algebra
    "recover slope+intercept from two (input, cost) pairs":
        W("fixed") + r"[\s\S]{0,200}" + W("plus") + r"|" + W("charges")
        + r"[\s\S]{0,120}" + W("each"),
    "solve a 2x2 linear system by elimination":
        r"(?<![A-Za-z])(cost|weigh|price)[a-z]*(?![A-Za-z])[\s\S]{0,400}"
        r"(?<![A-Za-z])(and|while)(?![A-Za-z])[\s\S]{0,300}"
        r"(?<![A-Za-z])(cost|weigh|price)[a-z]*(?![A-Za-z])",
    "least/greatest integer satisfying a linear inequality":
        r"(?<![A-Za-z])(least|greatest|largest|smallest|maximum|minimum)"
        r"(?![A-Za-z])[\s\S]{0,60}" + W("integer"),
    "greatest whole count affordable within a budget":
        r"(?<![A-Za-z])(greatest|maximum)(?![A-Za-z])[\s\S]{0,120}"
        r"(?<![A-Za-z])(buy|purchase|afford)[a-z]*(?![A-Za-z])",
    "solve a compound (double) inequality":
        r"\\lt[\s\S]{0,60}\\le|\\le[\s\S]{0,60}\\lt|"
        r"&lt;[\s\S]{0,40}\\le",
    "translate words into an inequality (which inequality represents)":
        r"(?<![A-Za-z])[Ww]hich inequality(?![A-Za-z])",
    "value of k making a linear system inconsistent":
        W("no solution"),
    "value of k making a linear system have infinitely many solutions":
        W("infinitely many"),
    "recover a missing coordinate from a stated slope":
        W("slope") + r"[\s\S]{0,200}" + W("value of a") + r"|"
        + W("has slope") + r"[\s\S]{0,160}(?<![A-Za-z])y-(intercept|axis)",
    "perpendicular line through a point":
        W("perpendicular"),
    "rearrange a literal formula for a named variable":
        r"(?<![A-Za-z])in terms of(?![A-Za-z])",
    "clear denominators in a single-variable rational equation":
        r"\\frac\{[a-z]\}\{\d\}[\s\S]{0,80}\\frac\{[a-z]\}\{\d\}",
    "two speeds out and back, total time given":
        r"(?<![A-Za-z])(round trip|returns? (?:by|along|over) the same|"
        r"walks back|rows back|rides back)",

    # ---- advanced
    "evaluate a quadratic function at a given number":
        r"(?<![A-Za-z])function [a-z] is defined by(?![A-Za-z])[\s\S]{0,160}"
        r"(?<![A-Za-z])value of(?![A-Za-z])[\s\S]{0,20}\\?\(?[a-z]\(-?\d",
    "solve f(x) = k for the input x":
        r"(?<![A-Za-z])function [a-z] is defined by(?![A-Za-z])[\s\S]{0,200}"
        r"(?<![A-Za-z])(for what value of|what value of x)(?![A-Za-z])",
    "compose two functions / recover the inner function":
        r"[fgh]\([fgh]\(",
    "divide a quadratic by a linear factor":
        r"\\frac\{ *\d*x\^\{?2\}?[\s\S]{0,60}\}\{ *\d*x",
    "quotient of powers with a numeric coefficient":
        r"\\frac\{ *\d+ *x\^\{?\d\}?[\s\S]{0,20}\}\{ *\d* *x\^\{?\d",
    "combine two rational expressions over a common denominator":
        r"\\frac\{[^{}]{1,8}\}\{[^{}]{1,14}\} *[-+] *\\frac\{",
    "expand and collect a linear expression":
        r"(?<![A-Za-z])[Ww]hich expression is equivalent to(?![A-Za-z])"
        r"[\s\S]{0,60}\d *\(",
    "complete the square to vertex form":
        r"\(x *[-+] *h\)|(?<![A-Za-z])in the form(?![A-Za-z])[\s\S]{0,60}\(x",
    "match coefficients in an identity true for every x":
        r"(?<![A-Za-z])for (?:every|all) value(?:s)? of x(?![A-Za-z])",
    "discriminant zero: exactly one real solution":
        r"(?<![A-Za-z])exactly one(?![A-Za-z])[\s\S]{0,40}"
        r"(?<![A-Za-z])(real )?solution",
    "radical equation, reject the extraneous root":
        r"\\sqrt\{[^{}]*\} *=",
    "same-base exponential equation, equate exponents":
        r"\d\^\{[^{}]*\} *= *\d",
    "sum or product of the roots of a factored quadratic":
        r"(?<![A-Za-z])(sum|product) of (?:those|the) (?:two )?solutions",
    "minimum/maximum of a quadratic in vertex form":
        r"(?<![A-Za-z])(minimum|maximum) value(?![A-Za-z])",
    "quadratic word problem: area gives a side, then perimeter":
        r"(?<![A-Za-z])area(?![A-Za-z])[\s\S]{0,200}"
        r"(?<![A-Za-z])perimeter(?![A-Za-z])",
    "interval on which a quadratic exceeds a level":
        r"(?<![A-Za-z])how (?:many|long)(?![A-Za-z])[\s\S]{0,120}"
        r"(?<![A-Za-z])(above|more than|higher than)(?![A-Za-z])",

    # ---- problem solving and data
    "percent of a given total":
        r"\d+ *(?:%|percent) of",
    "scale a rate up to a longer period":
        r"(?<![A-Za-z])at (?:this|that|the same) rate(?![A-Za-z])",
    "inverse proportion (constant product)":
        r"(?<![A-Za-z])inversely proportional(?![A-Za-z])",
    "mean recovered after one value is removed":
        r"(?<![A-Za-z])mean(?![A-Za-z])[\s\S]{0,220}"
        r"(?<![A-Za-z])(removed|taken out|is taken|discarded)",
    "mean of a short explicit list":
        r"(?<![A-Za-z])mean(?![A-Za-z])[\s\S]{0,120}"
        r"(?:\d+(?:\.\d+)? *, *){3}",
    "median of a short explicit list":
        r"(?<![A-Za-z])median(?![A-Za-z])",
    "weighted mean of two groups of different sizes":
        r"(?<![A-Za-z])mean(?![A-Za-z])[\s\S]{0,200}"
        r"(?<![A-Za-z])mean(?![A-Za-z])[\s\S]{0,200}"
        r"(?<![A-Za-z])(all|combined|together|both)(?![A-Za-z])",
    "conditional probability from a two-way table":
        r"(?<![A-Za-z])selected at random(?![A-Za-z])",
    "probability of a run of draws without replacement":
        r"(?<![A-Za-z])without replacement(?![A-Za-z])|"
        r"(?<![A-Za-z])one after another(?![A-Za-z])",
    "read two cells of a table and subtract":
        r"(?<![A-Za-z])how many more(?![A-Za-z])",
    "carry a table proportion to a larger total":
        r"(?<![A-Za-z])same (?:proportion|percentage|fraction)(?![A-Za-z])",
    "compare percentage change across table rows":
        r"(?<![A-Za-z])(greatest|largest) percent",
    "combined work rate, one worker leaves partway":
        r"(?<![A-Za-z])(alone in|working alone)(?![A-Za-z])",
    "unit yield recovered, then scaled and divided":
        r"(?<![A-Za-z])(at the same (?:yield|rate) per|per) [a-z ]{3,20}"
        r"[\s\S]{0,140}(?<![A-Za-z])how many(?![A-Za-z])",

    # ---- geometry and trigonometry
    "arc length of a sector from a central angle":
        r"(?<![A-Za-z])arc(?![A-Za-z])",
    "area of a sector":
        r"(?<![A-Za-z])sector(?![A-Za-z])",
    "angle sum of a triangle with one angle a multiple of another":
        r"(?<![A-Za-z])(three|twice|four) times the measure(?![A-Za-z])",
    "exterior angle of a triangle":
        r"(?<![A-Za-z])exterior angle(?![A-Za-z])",
    "supplementary angles":
        r"(?<![A-Za-z])supplementary(?![A-Za-z])",
    "complementary angles":
        r"(?<![A-Za-z])complementary(?![A-Za-z])",
    "volume of a cylinder":
        r"(?<![A-Za-z])cylind[a-z]+(?![A-Za-z])[\s\S]{0,200}"
        r"(?<![A-Za-z])volume(?![A-Za-z])|"
        r"(?<![A-Za-z])volume(?![A-Za-z])[\s\S]{0,160}"
        r"(?<![A-Za-z])cylind[a-z]+(?![A-Za-z])",
    "volume of a cylinder plus a cone (composite solid)":
        r"(?<![A-Za-z])cone(?![A-Za-z])[\s\S]{0,200}"
        r"(?<![A-Za-z])(cylind[a-z]+|total volume)(?![A-Za-z])|"
        r"(?<![A-Za-z])cylind[a-z]+(?![A-Za-z])[\s\S]{0,200}"
        r"(?<![A-Za-z])cone(?![A-Za-z])",
    "volume ratio of similar solids (cube of the scale factor)":
        r"(?<![A-Za-z])similar(?![A-Za-z])[\s\S]{0,240}"
        r"(?<![A-Za-z])(volume|litres|liters|holds)(?![A-Za-z])",
    "side ratio from parallel segment in a triangle":
        r"(?<![A-Za-z])parallel to(?![A-Za-z])[\s\S]{0,120}"
        r"(?<![A-Za-z])(side|segment)?[\s]*[A-Z]{2}(?![A-Za-z])",
    "recover a side from a tangent ratio":
        r"\\tan",
    "recover a side or area from a cosine/sine ratio":
        r"\\cos|\\sin",
    "count identical boxes that fill a larger box":
        r"(?<![A-Za-z])(filled completely|no space left|fills? the)(?![A-Za-z])",
    "area of a rectangle from two given sides":
        r"(?<![A-Za-z])area(?![A-Za-z])[\s\S]{0,140}"
        r"(?<![A-Za-z])(rectangle|rectangular)(?![A-Za-z])|"
        r"(?<![A-Za-z])(rectangle|rectangular)(?![A-Za-z])[\s\S]{0,140}"
        r"(?<![A-Za-z])area(?![A-Za-z])",
}

# Which mechanism each Test 31 question is intended to exercise. Written by
# hand, because the point is to state what the student actually does.
OURS = {
    "M1-01": "recover slope+intercept from two (input, cost) pairs",
    "M1-02": "least/greatest integer satisfying a linear inequality",
    "M1-03": "solve a 2x2 linear system by elimination",
    "M1-04": "count identical boxes that fill a larger box",
    "M1-05": "two speeds out and back, total time given",
    "M1-06": "perpendicular line through a point",
    "M1-07": "least/greatest integer satisfying a linear inequality",
    "M1-08": "quadratic word problem: area gives a side, then perimeter",
    "M1-09": "interval on which a quadratic exceeds a level",
    "M1-10": "divide a quadratic by a linear factor",
    "M1-11": "same-base exponential equation, equate exponents",
    "M1-12": "compose two functions / recover the inner function",
    "M1-13": "complete the square to vertex form",
    "M1-14": "carry a table proportion to a larger total",
    "M1-15": "inverse proportion (constant product)",
    "M1-16": "mean recovered after one value is removed",
    "M1-17": "conditional probability from a two-way table",
    "M1-18": "scale a rate up to a longer period",
    "M1-19": "arc length of a sector from a central angle",
    "M1-20": "exterior angle of a triangle",
    "M1-21": "recover a side from a tangent ratio",
    "M1-22": "count identical boxes that fill a larger box",

    "M2E-01": "solve a one-step linear equation in context",
    "M2E-02": "evaluate a linear model at a given input",
    "M2E-03": "solve a linear equation then evaluate an expression",
    "M2E-04": "evaluate a linear model at a given input",
    "M2E-05": "least/greatest integer satisfying a linear inequality",
    "M2E-06": "solve a one-step linear equation in context",
    "M2E-07": "translate words into an inequality (which inequality represents)",
    "M2E-08": "expand and collect a linear expression",
    "M2E-09": "evaluate a quadratic function at a given number",
    "M2E-10": "sum or product of the roots of a factored quadratic",
    "M2E-11": "quotient of powers with a numeric coefficient",
    "M2E-12": "solve f(x) = k for the input x",
    "M2E-13": "radical equation, reject the extraneous root",
    "M2E-14": "percent of a given total",
    "M2E-15": "scale a rate up to a longer period",
    "M2E-16": "mean of a short explicit list",
    "M2E-17": "median of a short explicit list",
    "M2E-18": "read two cells of a table and subtract",
    "M2E-19": "area of a rectangle from two given sides",
    "M2E-20": "supplementary angles",
    "M2E-21": "volume of a cylinder",
    "M2E-22": "recover a side from a tangent ratio",

    "M2H-01": "value of k making a linear system inconsistent",
    "M2H-02": "recover a missing coordinate from a stated slope",
    "M2H-03": "solve a compound (double) inequality",
    "M2H-04": "solve a 2x2 linear system by elimination",
    "M2H-05": "rearrange a literal formula for a named variable",
    "M2H-06": "greatest whole count affordable within a budget",
    "M2H-07": "clear denominators in a single-variable rational equation",
    "M2H-08": "match coefficients in an identity true for every x",
    "M2H-09": "discriminant zero: exactly one real solution",
    "M2H-10": "radical equation, reject the extraneous root",
    "M2H-11": "compose two functions / recover the inner function",
    "M2H-12": "combine two rational expressions over a common denominator",
    "M2H-13": "minimum/maximum of a quadratic in vertex form",
    "M2H-14": "combined work rate, one worker leaves partway",
    "M2H-15": "compare percentage change across table rows",
    "M2H-16": "weighted mean of two groups of different sizes",
    "M2H-17": "probability of a run of draws without replacement",
    "M2H-18": "unit yield recovered, then scaled and divided",
    "M2H-19": "volume of a cylinder plus a cone (composite solid)",
    "M2H-20": "side ratio from parallel segment in a triangle",
    "M2H-21": "recover a side or area from a cosine/sine ratio",
    "M2H-22": "volume ratio of similar solids (cube of the scale factor)",
}


def load():
    return json.load(open(PROD))


def hits(pattern, prod):
    rx = re.compile(pattern, re.I)
    return [q for q in prod if rx.search(strip(q["stem"]))]


def main():
    prod = load()
    args = sys.argv[1:]

    if "--probe" in args:
        name = args[args.index("--probe") + 1]
        for q in hits(MECHANISMS[name], prod):
            print(f"  {q['label']}: {strip(q['stem'])[:260]}")
        return

    read_at = None
    if "--read" in args:
        read_at = int(args[args.index("--read") + 1])

    counts = {}
    for name, pat in MECHANISMS.items():
        counts[name] = hits(pat, prod)

    used = {}
    for tag, mech in OURS.items():
        used.setdefault(mech, []).append(tag)

    print(f"bank: {len(prod)} stems\n")
    print("mechanism counts for every mechanism Test 31 uses "
          "(count = banked stems making the same move)\n")
    rows = []
    for mech, tags in used.items():
        n = len(counts.get(mech, []))
        rows.append((n, mech, sorted(tags)))
    for n, mech, tags in sorted(rows, reverse=True):
        mark = "  <-- READ" if n >= 8 else ""
        print(f"  {n:4d}  {mech:<58s} {','.join(tags)}{mark}")
        if read_at is not None and n >= read_at:
            for q in counts[mech][:14]:
                print(f"          {q['label']}: {strip(q['stem'])[:190]}")

    if "--free" in args:
        print("\nmechanisms the bank barely uses (candidates for replacements):")
        for name, qs in sorted(counts.items(), key=lambda z: len(z[1])):
            if len(qs) <= 4:
                print(f"  {len(qs):4d}  {name}")


if __name__ == "__main__":
    main()
