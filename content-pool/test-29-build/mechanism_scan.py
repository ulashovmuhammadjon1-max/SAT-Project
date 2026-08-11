#!/usr/bin/env python3
"""Mechanism search over the READ-ONLY production Math bank.

The Test 25 finding: 19 of its 34 genuine template repeats were never flagged by
Jaccard, six of them scoring below 0.30, because a repeat that changes the
setting words scores LOW precisely because it changed the words. Jaccard measures
vocabulary; this searches for the MECHANISM.

Each entry below names one Test 29 question and the regexes that describe what it
actually asks a student to do, independent of the brickworks setting. Every
pattern must match for a bank stem to be printed.

    python3 mechanism_scan.py             # every question
    python3 mechanism_scan.py H1-14       # one question, full stems
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROD = os.path.join(HERE, "..", "prod_math_stems.json")

# (tag, description, [regexes that must all match])
MECHANISMS = [
 ("H1-01", "ratio of two priced components, total count -> total cost",
  [r"ratio|proportion of|for every", r"cost|price|\$", r"total cost|cost, in dollars|total, in dollars"]),
 ("H1-02", "linear decreasing model, first whole step below a bound",
  [r"first .{0,30}(fewer|less|below)|fewer than", r"\d,?\d*\s*-\s*\d|\-\s*\d+d\b"]),
 ("H1-03", "linear function through two data points, evaluated at a third",
  [r"linear function|linear model|constant rate", r"after \d+ .{0,20}and .{0,25}after \d+|was .{0,40} and .{0,40} was"]),
 ("H1-04", "two vehicle/container types, total count and total capacity",
  [r"(carries|holds|seats|carr)", r"how many .{0,40}(were|are) "]),
 ("H1-05", "linear price from two runs, price at a third",
  [r"price|charge|cost", r"linear function", r"what is the (price|cost|charge)"]),
 ("H1-06", "count whole multiples of k inside a range",
  [r"how many .{0,40}(whole|integer)", r"at least .{0,60}(no more|cannot|at most)|between"]),
 ("H1-07", "subtract two quadratics, squared terms cancel -> profit",
  [r"profit", r"\^\{?2\}?"]),
 ("H1-08", "vertex-form parabola, zeros -> width at the base",
  [r"how wide|width", r"\\frac\{1\}\{\d+\}|\(x-\d+\)\^\{2\}|-\\frac"]),
 ("H1-09", "geometric decay, third term given, find the first",
  [r"same (fraction|percent|proportion)|each (day|hour|year) .{0,30}same", r"end of the (first|third)|after (one|three)"]),
 ("H1-10", "g(x)=a(x-p)(x+q), one value given, find another",
  [r"a\(x\s*[-+]\s*\d+\)\(x\s*[-+]\s*\d+\)|=a\(x"]),
 ("H1-11", "rearrange a three-variable formula for one variable",
  [r"in terms of the other|which (expression|equation) gives .{0,40} in terms of"]),
 ("H1-12", "minimise a quadratic -> vertex x",
  [r"(least|minimum|smallest).{0,60}(value|cost|bill)|least\b", r"\^\{?2\}?"]),
 ("H1-13", "worker-hours: n workers h hours -> m workers k hours",
  [r"(workers?|men|hands|moulders?|pickers?|weavers?).{0,80}(hour|day)", r"same rate", r"how many"]),
 ("H1-14", "table of count x percentage, which row is greatest",
  [r"table", r"per\s?cent|percentage|%", r"greatest|largest|most"]),
 ("H1-15", "percent removed, then a fraction of the remainder",
  [r"per\s?cent", r"remain|those that|the rest|left"]),
 ("H1-16", "median of a list before and after one more value",
  [r"median"]),
 ("H1-17", "right triangle legs -> hypotenuse, plus an allowance",
  [r"(longer|extra|allowance|overlap).{0,40}(each end|both ends)|cut \d+ centimetres longer"]),
 ("H1-18", "tangent ratio given, base width -> sloping side",
  [r"tangent|\\tan", r"\\frac\{7\}\{24\}|\\frac\{\d+\}\{\d+\}"]),
 ("H1-19", "box plus a half-cylinder on top",
  [r"half.{0,12}cylinder|semicircular", r"volume"]),
 ("H1-20", "steady burn rate from two readings, run to a reserve",
  [r"steady rate|constant rate", r"how (many|long)", r"left|remain|reserve"]),
 ("H1-21", "weighted mean of two groups of different sizes",
  [r"mean", r"over all|altogether|combined|both"]),
 ("H1-22", "hollow square prism: outer minus inner, times length",
  [r"hollow|inside .{0,30}square|running up the middle", r"volume|cubic"]),

 ("H2E-01", "total minus remainder, divided into equal parts",
  [r"equal .{0,20}(loads|groups|piles|boxes|bundles)|equal parts", r"how many .{0,30}(each|in each)"]),
 ("H2E-02", "container tare plus n unit masses = total",
  [r"(empty|mass of the) .{0,30}(crate|box|carton|barrel|tin|jar)|tare", r"mass"]),
 ("H2E-03", "interpret the constant term of a linear model",
  [r"best interpretation|most reasonable interpretation", r"\d+n\s*\+\s*\d+|\+\s*\d+\b"]),
 ("H2E-04", "constant speed from two (time, position) readings",
  [r"constant (speed|rate)", r"how (many|far).{0,40}each second|per second|each (minute|second|hour)"]),
 ("H2E-05", "least whole number so that a rate exceeds a target",
  [r"least (whole|integer) number|smallest (whole|integer)", r"more than"]),
 ("H2E-06", "scale drawing: cm to metres",
  [r"(scale|drawing|map|plan).{0,60}represents|represents an actual"]),
 ("H2E-07", "capacity minus a fixed tare -> an inequality",
  [r"which inequality", r"at most|no more than|maximum"]),
 ("H2E-08", "expand and collect a linear expression",
  [r"equivalent", r"\d\(\d?x\s*\+\s*\d+\)"]),
 ("H2E-09", "match coefficients: expression equals ax + b for all x",
  [r"for (every|all) value", r"value of a|constant"]),
 ("H2E-10", "evaluate a linear function at a given input",
  [r"m\(x\)|f\(x\)=\d|\(x\)=\d+\.?\d*x", r"what is the (mass|value|cost|number)"]),
 ("H2E-11", "solve a(2)^x = N for x",
  [r"\(2\)\^\{?x|2\^\{?x"]),
 ("H2E-12", "interpret f(a)=b in context",
  [r"best interpretation|most reasonable interpretation", r"\(\d+\)\s*=\s*\d"]),
 ("H2E-13", "evaluate x/k at a given x",
  [r"\\frac\{x\}\{\d+\}"]),
 ("H2E-14", "fraction of a batch",
  [r"of every|out of every|of each \d", r"how many"]),
 ("H2E-15", "sum a column of a four-row table",
  [r"table", r"altogether|in total|total number"]),
 ("H2E-16", "part-to-part ratio, one part given, find the other",
  [r"ratio of", r"how many"]),
 ("H2E-17", "percent of a total",
  [r"per\s?cent .{0,30}(were|was|are)", r"how many"]),
 ("H2E-18", "circumference of a drum/wheel per turn",
  [r"(one|each) (complete )?(turn|revolution|rotation)"]),
 ("H2E-19", "tangent of an angle in a right triangle from two legs",
  [r"tangent of the angle|\\tan"]),
 ("H2E-20", "mean of five given values",
  [r"mean", r"\d+, \d+, \d+, \d+ and \d+|five"]),
 ("H2E-21", "box volume in m3 converted to litres",
  [r"litres?|liters?", r"cubic met"]),
 ("H2E-22", "3-4-5 right triangle: two legs -> hypotenuse",
  [r"(square|right angle|perpendicular)", r"60|80", r"how (many|far).{0,40}apart|distance"]),

 ("H2H-01", "x+y and x^2-y^2 given, find x-y",
  [r"x\^\{2\}\s*-\s*y\^\{2\}|difference of (their|two) squares"]),
 ("H2H-02", "one rate for the first n, half that rate after",
  [r"(half|twice) that rate|for each of the first"]),
 ("H2H-03", "slope through two points with a parameter a",
  [r"slope", r"\(a,|\(3a|,\s*2a\)"]),
 ("H2H-04", "count integers satisfying a compound inequality",
  [r"how many integers"]),
 ("H2H-05", "x-intercept of px+qy=r symbolically",
  [r"px\+qy|ax\+by", r"x-?(coordinate|intercept)|crosses the x"]),
 ("H2H-06", "total m, one part k times the other, express one part",
  [r"times as (heavy|many|much|long)", r"in terms of m|in terms of"]),
 ("H2H-07", "g(x)=f(x-h) horizontal shift of a linear f",
  [r"g\(x\)=f\(x", r"which expression defines"]),
 ("H2H-08", "inverse variation with the square",
  [r"varies inversely|inversely as"]),
 ("H2H-09", "two rates working together, symbolic uv/(u+v)",
  [r"working (together|alone)", r"how many (minutes|hours|days)"]),
 ("H2H-10", "x^2-6x+c, least value given, find c",
  [r"least value|minimum value", r"constant"]),
 ("H2H-11", "3^{2s}=k, find 3^{6s}",
  [r"\^\{2[a-z]\}|\^\{6[a-z]\}|\^\{3[a-z]\}"]),
 ("H2H-12", "factor out a common binomial, find a+b",
  [r"value of a\+b|a\s*\+\s*b", r"\(x-\d\)\("]),
 ("H2H-13", "scale a work rate by both workers and days",
  [r"\bw\b.{0,30}(masons|workers)|gang of", r"in terms of|how many .{0,20}(blocks|units|items)"]),
 ("H2H-14", "mean of n, one more added, new mean -> the added value",
  [r"mean", r"one more|added|(\d+) (more|additional)"]),
 ("H2H-15", "table of counts and rejects, greatest percentage",
  [r"table", r"(greatest|highest) percent"]),
 ("H2H-16", "successive percent change down then up, recover the start",
  [r"(fell|decreased|dropped).{0,60}(rose|increased)|per\s?cent.{0,80}per\s?cent"]),
 ("H2H-17", "cube plus a pyramid on its top face",
  [r"pyramid", r"volume"]),
 ("H2H-18", "equilateral triangle from two equal arcs, find the height",
  [r"equilateral|two (circular )?arcs", r"height"]),
 ("H2H-19", "cosine given, adjacent side given, find the hypotenuse",
  [r"cosine|\\cos"]),
 ("H2H-20", "mean under add-then-double transformation",
  [r"mean", r"(increased|added).{0,40}(doubled|multiplied)|each .{0,20}doubled"]),
 ("H2H-21", "proportion a/(x-p) = b/(x+q), solve for x",
  [r"\\frac\{\d\}\{x"]),
 ("H2H-22", "block minus a rectangular notch, volume",
  [r"(notch|groove|channel|slot|hole) .{0,60}cut|cut out of", r"volume"]),
]


def flat(s):
    s = re.sub(r"<img[^>]*>", " ", s)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()


def main():
    want = set(a.upper() for a in sys.argv[1:])
    rows = [(r["label"], flat(r["stem"]), r["stem"]) for r in json.load(open(PROD))]
    for tag, desc, pats in MECHANISMS:
        if want and tag not in want:
            continue
        ps = [re.compile(p, re.I) for p in pats]
        hits = [(lab, txt) for lab, txt, raw in rows if all(p.search(txt) for p in ps)]
        print(f"\n### {tag}  [{desc}]  -> {len(hits)} hit(s)")
        n = len(hits) if want else 8
        for lab, txt in hits[:n]:
            print(f"   {lab:>16}  {txt[:(400 if want else 210)]}")


if __name__ == "__main__":
    main()
