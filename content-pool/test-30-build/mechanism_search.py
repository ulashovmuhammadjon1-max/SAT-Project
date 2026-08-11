#!/usr/bin/env python3
"""Search the banked Math stems by MECHANISM, not by vocabulary.

Why this exists
---------------
Token-signature Jaccard measures the words a stem uses. A template repeat that
keeps the mathematics and changes the setting therefore scores LOW *because* it
changed the words. Test 25 replaced 34 of its 66 Math questions and **19 were
never flagged by the score at all** — six of those scored below 0.30. It found
them by asking what the question *does*: "capacity minus tare over unit mass",
"dilute a percentage with pure solvent", "mean of n then add one".

So this tool asks, for each of Test 30's 66 questions, a question of the form
"how many banked stems perform this same operation?" — expressed as a regex over
the bank's plain text plus, where the mechanism is visible only in the algebra,
over the LaTeX.

    python3 mechanism_search.py            # every mechanism, hit counts
    python3 mechanism_search.py H2E-16     # one mechanism, hits printed in full
    python3 mechanism_search.py --free 'regex'   # ad-hoc probe before writing

Reads ../prod_math_stems.json READ ONLY.

Boundary discipline: every keyword here uses an explicit lookaround or an
explicit word boundary on BOTH sides. `\bfen` matched "fence" and `<u` matched
`<ul` in earlier builds — a boundary-free substring match in a checker is worse
than no check, because it trains you to ignore the output.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROD = os.path.join(HERE, "..", "prod_math_stems.json")


def plain(stem):
    """Strip markup but KEEP the LaTeX — several mechanisms are only visible in it."""
    tt = re.sub(r"<img[^>]*>", " ", stem)
    tt = re.sub(r"<[^>]+>", " ", tt)
    tt = tt.replace("&deg;", " degrees ").replace("&gt;", ">").replace("&lt;", "<")
    return " ".join(tt.split())


# Each entry: tag -> (one-line description of the OPERATION, regex).
# The regex is deliberately written against what the question DOES, so that a
# banked stem in an unrelated setting still matches.
MECHANISMS = {
 # ---- Module 1 -------------------------------------------------------------
 "H1-01": ("split a whole by percent, the two parts differ by a given amount",
           r"(?i)percent of the .{0,60}\b(?:and the rest|rest)\b.{0,120}\b(?:more|fewer|less)\b"),
 "H1-02": ("same number per group; one grouping leaves a surplus, another a shortfall",
           r"(?i)\b(?:left over|leave|leaves|over|short|need)\b.{0,80}\b(?:rows?|groups?|boxes|crates?|shelves)\b"),
 "H1-03": ("two quantities sum to a total, one is k times the other minus d",
           r"(?i)\btogether\b.{0,120}\btwice\b|\btwice the\b.{0,40}\b(?:less|minus|more)\b"),
 "H1-04": ("constant rate of change plus one known point, extrapolate",
           r"(?i)\b(?:rises|increases|falls|decreases)\b by \d[^.]{0,60}\bfor (?:every|each)\b"),
 "H1-05": ("linear model: find t where the value is k times the value at t=0",
           r"(?i)\b(?:times as (?:much|many)|double|triple|quadruple)\b.{0,80}\b(?:began|start|initially|at the (?:start|beginning))"),
 "H1-06": ("compare two constant rates, one as an equation and one as a table",
           r"(?i)\brate of change\b|\bhow (?:many )?more\b.{0,80}\b(?:each|per) (?:week|day|hour|month)\b"),
 "H1-07": ("fixed cost plus per-unit beats a flat per-unit: least n",
           r"(?i)\bleast (?:whole )?number\b.{0,160}\b(?:costs? less|cheaper|less than)\b"),
 "H1-08": ("simplify a radical with an odd power inside",
           r"(?i)\\sqrt\{\d*\w|\bequivalent to\b.{0,60}\\sqrt"),
 "H1-09": ("quotient of two monomials: subtract the exponents",
           r"\\frac\{\d*\w\^\{?\d+\}?[^}]*\}\{\d*\w\^"),
 "H1-10": ("quadratic inequality: the length of the interval where it holds",
           r"(?i)\b(?:at least|at most)\b.{0,140}\^\{?2\}?|\^\{?2\}?.{0,140}\b(?:at least|at most)\b"),
 "H1-11": ("apply a horizontal shift and a vertical shift to a known point",
           r"(?i)f\(x\s*[-+]\s*\d\)\s*[-+]\s*\d|\bwhich point (?:must )?lies? on the graph\b"),
 "H1-12": ("quadratic whose roots are in a fixed ratio; recover a coefficient",
           r"(?i)one (?:solution|root|zero) (?:of|is)\b.{0,60}\btimes the other\b"),
 "H1-13": ("cross-multiply two single-term rational expressions",
           r"\\frac\{\d+\}\{[^{}]*\}\s*=\s*\\frac\{\d+\}\{[^{}]*\}"),
 "H1-14": ("two quantities in a given ratio differ by a stated amount",
           r"(?i)\bratio (?:of )?\d+ to \d+\b.{0,160}\b(?:more|less|fewer) than\b"),
 "H1-15": ("compare two package sizes by unit price, report the difference",
           r"(?i)\b(?:how much|how many cents|how many dollars) (?:less|more|cheaper)\b.{0,120}\b(?:per|a) (?:kilogram|pound|litre|liter|gallon|ounce|metre|meter)\b"),
 "H1-16": ("add one value to a list so that the median becomes a stated number",
           r"(?i)\bmedian\b.{0,160}\b(?:could be|sixth|additional|another|one more)\b"),
 "H1-17": ("compare the spread of two same-mean lists",
           r"(?i)\bstandard deviation\b.{0,200}\b(?:greater|less|same|equal)\b"),
 "H1-18": ("table total fixes a common rate, then apply it to one row",
           r"(?i)\b(?:every|each) \w+ yielded the same\b|\bat the same rate\b.{0,160}\btable\b|"
           r"\btable\b.{0,300}\bthe same \w+ for each\b"),
 "H1-19": ("similar solids: volume scales as the cube of the length factor",
           r"(?i)\bsame shape\b|\bsimilar\b.{0,200}\bvolume\b|\bevery length\b"),
 "H1-20": ("area of a sector as a fraction of a whole circle",
           r"(?i)\b(?:arc|sector)\b"),
 "H1-21": ("isosceles apex angle -> base angle -> bisected base angle",
           r"(?i)\bbisects?\b.{0,120}\bangle\b|\bangle bisector\b"),
 "H1-22": ("Pythagorean identity: square a given ratio and subtract from 1",
           r"(?i)\\(?:sin|cos|tan)\^|\bidentity\b"),

 # ---- Module 2 (Easy) ------------------------------------------------------
 "H2E-01": ("subtract a remainder then divide equally",
            r"(?i)\b(?:left over|remain(?:ing|s|der)?)\b.{0,120}\b(?:equally|each)\b"),
 "H2E-02": ("multiply a per-container count by the number of containers",
            r"(?i)\beach\b.{0,60}\bholds?\b.{0,80}\bhow many\b.{0,80}\baltogether\b"),
 "H2E-03": ("total divided by a constant daily draw",
            r"(?i)\bafter how many days\b.{0,120}\bempty\b|\bempty\b.{0,80}\bafter how many days\b"),
 "H2E-04": ("evaluate a linear model at a given input",
            r"(?i)\bis given by\b.{0,120}=.{0,60}\bwhat is\b.{0,80}\bafter \d+\b"),
 "H2E-05": ("substitute one known value into a two-variable linear equation",
            r"(?i)\bif \w\s*=\s*\d+\b.{0,80}\bwhat is the value of \w\b"),
 "H2E-06": ("start minus rate times time",
            r"(?i)\bhow many\b.{0,60}\b(?:are )?left\b.{0,140}\bafter \d+ (?:weeks?|days?|months?|hours?)\b"),
 "H2E-07": ("which listed value satisfies a one-step linear inequality",
            r"(?i)\bwhich of the following could be\b.{0,200}(?:>|<|\\le|\\ge|greater than|less than)"),
 "H2E-08": ("add two quadratic polynomials and collect like terms",
            r"(?i)\bsum of the (?:two )?(?:polynomials|expressions)\b|"
            r"\(\s*\d*\w\^\{?2\}?[^)]{0,30}\)\s*\+\s*\(\s*\d*\w\^\{?2\}?"),
 "H2E-09": ("expand a product of two linear binomials",
            r"\(\s*\w\s*[-+]\s*\d+\s*\)\s*\(\s*\w\s*[-+]\s*\d+\s*\)"),
 "H2E-10": ("raise a monomial to a power",
            r"(?:\\left\()?\s*\d+\w\^\{?\d+\}?\s*(?:\\right)?\)\^\{?2\}?"),
 "H2E-11": ("evaluate a square-root function at a stated input",
            r"(?i)\\sqrt\{\w\s*[-+]\s*\d+\}.{0,140}\bvalue of\b"),
 "H2E-12": ("solve |x-a|=b and pick the root a stated inequality allows",
            r"(?i)\|\s*[-a-zA-Z0-9 +]{1,12}\s*\||\\left\|"),
 "H2E-13": ("take a cube root",
            r"(?i)\w\^\{?3\}?\s*=\s*\d+|\bcube root\b"),
 "H2E-14": ("multiply by a stated unit-conversion factor",
            r"(?i)\b1 \w+ (?:is|equals|=) \d+ \w+\b.{0,120}\bhow many\b"),
 "H2E-15": ("divide a total equally into a stated number of parts",
            r"(?i)\bdivided equally\b|\bshared equally\b|\bdivided among\b"),
 "H2E-16": ("mode of a list",
            r"(?i)\bmode\b"),
 "H2E-17": ("range of a list",
            r"(?i)\brange of (?:the|these)\b"),
 "H2E-18": ("greatest minus least in a 4-row table",
            r"(?i)\bdifference between the (?:greatest|largest|highest) and the (?:least|smallest|lowest)\b"),
 "H2E-19": ("area of a trapezium from the two parallel sides and the height",
            r"(?i)\btrapez"),
 "H2E-20": ("how many identical cubes fill a rectangular box",
            r"(?i)\bhow many\b.{0,80}\bcubes?\b|\bpacked into\b"),
 "H2E-21": ("exterior angle equals the sum of the two non-adjacent interiors",
            r"(?i)\bexterior angle\b"),
 "H2E-22": ("convert an angle from radians to degrees",
            r"(?i)\bradian"),

 # ---- Module 2 (Hard) ------------------------------------------------------
 "H2H-01": ("clear two unlike denominators in a one-variable equation",
            r"(?i)\\frac\{\w\s*[-+]\s*\d+\}\{\d+\}\s*\+\s*\\frac\{\w"),
 "H2H-02": ("solve a 2x2 system and report a product rather than a variable",
            r"(?i)\bvalue of (?:the )?(?:product )?\\?\(?xy\\?\)?\b"),
 "H2H-03": ("two subgroups at different percentages meeting a combined count",
            r"(?i)\d+ percent of the \w+ .{0,120}\d+ percent of the \w+"),
 "H2H-04": ("two stocks drawn down at rates in a fixed ratio; equal-time in terms of r",
            r"(?i)\bin terms of \w\b.{0,200}\bhow many (?:weeks|days|months|hours|minutes)\b"),
 "H2H-05": ("a linear function given only by how far f(a) sits above f(b)",
            r"(?i)f\(-?\d+\)\s*(?:is|as)\s*\d+\s*(?:greater|less|more)"),
 "H2H-06": ("clear two fractions in an inequality and report the solution set",
            r"(?i)\\frac\{[^{}]*\}\{\d\}\s*\\(?:le|ge)\s*\\frac"),
 "H2H-07": ("choose a constant so an inequality's solution set is a stated ray",
            r"(?i)\bwhere \w is a constant\b.{0,200}(?:>|<|\\le|\\ge).{0,80}\bvalue of \w\b"),
 "H2H-08": ("combine 1/a - 1/b over a common denominator",
            r"\\frac\{1\}\{\w\}\s*[-+]\s*\\frac\{1\}\{\w\}"),
 "H2H-09": ("compose a linear function with a shift and simplify",
            r"(?i)g\(x\)\s*=\s*f\(x\s*[-+]\s*\d+\)"),
 "H2H-10": ("count the distinct x-intercepts of a factorable cubic",
            r"(?i)\bhow many (?:distinct )?x-intercepts\b|\bnumber of x-intercepts\b"),
 "H2H-11": ("equal outputs fix the axis of symmetry; the minimum then fixes c",
            r"(?i)f\(-?\d+\)\s*=\s*f\(-?\d+\)"),
 "H2H-12": ("x + k/x = n, then the gap between the two roots",
            r"(?i)\w\s*\+\s*\\frac\{\d+\}\{\w\}"),
 "H2H-13": ("biquadratic in x^2, sum the positive roots",
            r"\w\^\{?4\}?\s*[-+]\s*\d+\s*\w\^\{?2\}?"),
 "H2H-14": ("two successive percentage changes with an addition in between",
            r"(?i)\b(?:first|second) year\b.{0,240}\bpercent\b"),
 "H2H-15": ("scale a group rate to a new output in a new time",
            r"(?i)\bhow many (?:clerks|workers|hands|men|machines|people|labourers|laborers)\b.{0,200}\bminutes\b"),
 "H2H-16": ("weighted mean of two percentages over two unequal groups",
            r"(?i)\bwhat percent of all\b"),
 "H2H-17": ("two-way table: difference of two row rates in percentage points",
            r"(?i)\bpercentage points\b"),
 "H2H-18": ("pick the table row with the greatest part-to-whole ratio",
            r"(?i)\bgreatest percentage\b|\bgreatest (?:proportion|fraction|ratio)\b"),
 "H2H-19": ("largest circle cut from a square, then the leftover area",
            r"(?i)\binscribed\b|\bfits exactly\b|\bshaded\b|\blargest (?:possible )?circle\b|\bleft over\b.{0,80}\barea\b"),
 "H2H-20": ("rectangle with sides in a ratio and a given perimeter, find the area",
            r"(?i)\btwice as long as it is wide\b|\blength is twice (?:its|the) width\b"),
 "H2H-21": ("radius as the distance between two points, then the circle's area",
            r"(?i)\bcent(?:re|er)\b.{0,120}\bpasses through\b"),
 "H2H-22": ("the two acute angles of a right triangle have reciprocal tangents",
            r"(?i)\\tan\s*[A-Z].{0,160}\\tan\s*[A-Z]"),
}


def main():
    prod = json.load(open(PROD))
    rows = [(p["label"], plain(p["stem"])) for p in prod]

    if len(sys.argv) > 2 and sys.argv[1] == "--free":
        pat = re.compile(sys.argv[2])
        hits = [(lab, tx) for lab, tx in rows if pat.search(tx)]
        for lab, tx in hits:
            print(f"--- {lab}\n{tx[:420]}\n")
        print(f"{len(hits)} hit(s) of {len(rows)}")
        return

    want = [a for a in sys.argv[1:] if not a.startswith("-")]
    verbose = bool(want)
    total_flag = 0
    for tag, (desc, pat) in MECHANISMS.items():
        if want and tag not in want:
            continue
        rx = re.compile(pat)
        hits = [(lab, tx) for lab, tx in rows if rx.search(tx)]
        mark = "  " if len(hits) <= 2 else ("!!" if len(hits) >= 6 else "? ")
        if len(hits) >= 3:
            total_flag += 1
        print(f"{mark} {tag}  {len(hits):3d} hit(s)   {desc}")
        if verbose or len(hits) >= 3:
            for lab, tx in hits[: (40 if verbose else 6)]:
                print(f"      {lab}: {tx[:300]}")
            if not verbose and len(hits) > 6:
                print(f"      ... {len(hits)-6} more")
        if verbose:
            print()
    if not want:
        print(f"\n{total_flag} mechanism(s) with 3 or more banked matches — read each.")


if __name__ == "__main__":
    main()
