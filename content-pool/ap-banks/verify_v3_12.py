"""Structural gate for AP U.S. Government 3.12 Balancing Minority and Majority
Rights.

gov345_check plus the four usgov_anchor helpers, plus three content gates.

  _oscillation  LO 3.12.A is written AT TIMES ALLOWED THE RESTRICTION... AT
                OTHER TIMES HAS PROTECTED, and EK 3.12.A.1's four items
                alternate direction: the Thirteenth Amendment's shift, then the
                separate but equal doctrine, then the school desegregation
                decisions, then decisions upholding the rights of the majority.
                The objective is a claim about oscillation, and the single most
                natural way to get this topic wrong is to narrate it as a
                staircase. That error is invisible to every structural check --
                a progress narrative is well formed, internally consistent and
                confidently wrong -- so the gate reads every key for the
                monotone claims and refuses them.

  _case_names   EK 3.12.A.1.ii describes "state laws and Supreme Court holdings
                based on the 'separate but equal' doctrine" and NAMES NO CASE.
                The case a well-read author would supply is not on the CED's
                required list and the framework withholds it here. Putting it in
                would sit content the exam cannot ask about beside content it
                can, with nothing to tell a student which is which. So the gate
                enumerates the fourteen required cases and refuses any other
                "X v. Y" anywhere in the module. It is the cheapest way to make
                a refusal stick across later edits, since the pressure to add
                the obvious case will recur every time someone reads item 8.

  _scotus_terms The CED fixes six words on p. 29 -- facts, issue, holding,
                reasoning, decision, majority opinion -- and skill 2.C is
                defined in terms of them. Holding and reasoning are the pair
                that gets reversed, and decision is routinely used as a synonym
                for holding when the CED makes it the broadest of the six. The
                gate pins each definition to its item.

WHAT THE MODULE ASSUMES ABOUT THE READER, PER THE CED
-----------------------------------------------------
Students are not expected to know dissenting or concurring opinions of required
cases (CED p. 29), so none is asked about. And any non-required case on the exam
arrives with a summary containing everything needed to compare it -- so items
19 and 20 print the unfamiliar case's facts in the stem rather than assuming
recognition, and item 17 makes that rule itself the question.
"""
import re

import gov345_check as gc
import usgov_anchor as ua
import v3_12

ANCHORS = {
 1: "restricted at some times and protected at others",
 2: "moves in both directions rather than in one",
 3: "based on the separate but equal doctrine",
 4: "a decision limiting a measure adopted for a minority is part of that record",
 5: "rather than only states in rebellion",
 6: "A shift toward the establishment of civil rights for the formerly enslaved",
 7: "the same list goes on to describe restrictions that came afterward",
 8: "restaurants, hotels, schools, and similar facilities",
 9: "State laws and Supreme Court holdings",
 10: "The name asserted equality while the framework describes the doctrine as restricting",
 11: "court decisions declaring that race-based school segregation",
 12: "The relevant events that occurred before the courts became involved",
 13: "The legal or constitutional question the Court considered",
 14: "while the reasoning is the explanation of that response",
 15: "The outcome including the facts, the issue, the holding, and the reasoning",
 16: "the written analysis agreed to by more than half the justices",
 17: "a summary containing all the information necessary to compare it",
 18: "upholding the rights of the majority in cases that limit and prohibit",
 19: "race was one factor among several",
 20: "whether a government may separate people by race consistently with the Fourteenth",
 21: "the amendment is what the framework calls the permanent abolition",
 22: "a standard for identifying when a majority has restricted a minority's rights",
 23: "a limitation that came after a protection, so it is not a single direction",
 24: "a decision protecting one may limit a measure adopted for the other",
 25: "at least five times the number provided for the minority group",
 26: "restricted minority access to the same facilities as the majority population",
 27: "the counts differ by a factor of six in the smallest gap",
 28: "but restricting rulings led in the first period",
 29: "restricted at some times and protected at other times",
 30: "their share of the period's rulings fell",
}

GROUNDING = {
 1: "EK 3.12.A.1's own introduction: 'Decisions demonstrating that minority rights have been "
    "restricted at times and protected at other times include...'",
 2: "LO 3.12.A's construction, AT TIMES ALLOWED THE RESTRICTION and AT OTHER TIMES HAS "
    "PROTECTED. The objective could have been written as progress and was not.",
 3: "EK 3.12.A.1.ii, the restricting item in a list that otherwise protects: the doctrine "
    "restricted access to the same facilities as the majority white population.",
 4: "EK 3.12.A.1.iv, read against the sentence that introduces the list. The item is what "
    "keeps the framework's record from reading as a one-way trend.",
 5: "U.S. Constitution, Thirteenth Amendment Section 1, quoted verbatim, against EK "
    "3.12.A.1.i's description of the Proclamation as reaching the states in rebellion. The "
    "amendment's own reach is the United States and any place subject to its jurisdiction.",
 6: "EK 3.12.A.1.i, verbatim: ratification 'marked a shift toward the establishment of civil "
    "rights for the formerly enslaved.'",
 7: "EK 3.12.A.1's word SHIFT read against items ii and iv, which describe restrictions and "
    "limitations that follow it in the same list. A list whose later items restrict cannot "
    "have been completed by its first.",
 8: "EK 3.12.A.1.ii, verbatim: restricting 'African American access to the same restaurants, "
    "hotels, schools, etc., as the majority white population.'",
 9: "EK 3.12.A.1.ii's two sources: 'State laws AND Supreme Court holdings based on the "
    "separate but equal doctrine.' Naming both shows courts carried the restriction too.",
 10: "EK 3.12.A.1.ii's verb RESTRICTING against the doctrine's own name. The framework "
     "describes unequal access under a label that asserted equality.",
 11: "Brown v. Board of Education (1954), required case, which the CED attaches to 3.12.A. "
     "CED holding: race-based school segregation violates the equal protection clause of the "
     "Fourteenth Amendment -- EK 3.12.A.1.iii's class of decision exactly.",
 12: "CED p. 29's definition of FACTS: 'relevant events before courts became involved.' Skill "
     "2.C is stated in terms of these six words, so the distinctions are course content.",
 13: "CED p. 29's definition of ISSUE: 'the legal or constitutional question considered.'",
 14: "CED p. 29's definitions of HOLDING ('the court's response to the issue') and REASONING "
     "('the explanation of a holding'). Reversing the two is the standard confusion.",
 15: "CED p. 29's definition of DECISION: 'the outcome including facts, issue, holding, and "
     "reasoning' -- the broadest of the six terms, not a synonym for the holding.",
 16: "CED p. 29's definition of the MAJORITY OPINION: the justices' written analysis 'agreed "
     "to by more than half.' Students are not expected to know dissents or concurrences.",
 17: "CED p. 29: any non-required case on the exam 'will be accompanied by a summary "
     "containing all information necessary to compare' it with a required case.",
 18: "Shaw v. Reno (1993), required case. CED holding: majority-minority districts created "
     "under the Voting Rights Act of 1965 'may be constitutionally challenged by voters if "
     "race is the only factor used in creating the district' -- EK 3.12.A.1.iv's class.",
 19: "CED skill 2.C, comparing FACTS. The Shaw holding turns on race being THE ONLY FACTOR, "
     "so a record showing several operative criteria differs on the fact that matters.",
 20: "CED skill 2.C, comparing the ISSUE, which the CED defines as the legal or "
     "constitutional question considered. Brown's equal protection question about racial "
     "separation by a government is the same question whatever the facility.",
 21: "Emancipation Proclamation (required document), quoted verbatim; the CED attaches it to "
     "3.12.A. EK 3.12.A.1.i pairs it with the Thirteenth Amendment because the Proclamation "
     "reached only the places its own text names.",
 22: "'Letter from a Birmingham Jail' (required document), quoted verbatim; the CED attaches "
     "the Letter to 3.12.A. Its test names the pattern LO 3.12.A's first half describes.",
 23: "EK 3.12.A.1's four items in order, against LO 3.12.A's AT TIMES and AT OTHER TIMES.",
 24: "EK 3.12.A.1.iv placed inside a list about minority rights, and the topic's own title, "
     "Balancing Minority and Majority Rights.",
 25: "Data item, CED skill 2.C. Every ratio is recomputed below.",
 26: "EK 3.12.A.1.ii located in the table: every row is a facility of the kind the framework "
     "names as restricted under the separate but equal doctrine.",
 27: "Data item: an argument that equality means mere presence. The narrowest and widest "
     "ratios are recomputed below.",
 28: "Data item, CED skill 2.C. Both columns and which leads in each period are recomputed.",
 29: "EK 3.12.A.1's introducing sentence shown as data: the leading column changes across "
     "periods, which is the framework's claim in observable form.",
 30: "Data item: extrapolating a direction from one period. Both shares are recomputed below, "
     "and the fall is why LO 3.12.A is written as an oscillation rather than a trend.",
}

MAJ_COL, MIN_COL = "Provided for the majority group", "Provided for the minority group"
RESTRICT, PROTECT = ("Rulings restricting the claimed right", "Rulings protecting the claimed right")


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def _ratios(t):
    maj, mn = t["headers"].index(MAJ_COL), t["headers"].index(MIN_COL)
    return {r[0]: gc.num(r[maj]) / gc.num(r[mn]) for r in t["rows"]}


def q25(t):
    """Every row's majority count is at least five times the minority count."""
    ratios = _ratios(t)
    assert min(ratios.values()) >= 5, \
        f"the smallest ratio is {min(ratios.values()):.2f}, below five"
    maj = [gc.num(c) for c in _col(t, MAJ_COL)]
    mn = [gc.num(c) for c in _col(t, MIN_COL)]
    assert all(a > b for a, b in zip(maj, mn)), "a row does not favour the majority group"
    assert all(b > 0 for b in mn), "a row reports zero for the minority group"
    return ("ratios " + ", ".join(f"{k.split()[1]} {v:.0f} to 1" for k, v in ratios.items())
            + f" -- smallest {min(ratios.values()):.0f} to 1")


def q26(t):
    """Every row is a facility of the kind EK 3.12.A.1.ii names."""
    names = [n.lower() for n in _col(t, "Facility")]
    assert all(n.startswith("public") for n in names), f"a row is not a public facility: {names}"
    assert any("school" in n for n in names), \
        "no row is a school, which is one of the facilities EK 3.12.A.1.ii names"
    assert len(set(names)) == len(names), f"a facility is listed twice: {names}"
    return f"{len(names)} distinct public facilities, including a school: " + ", ".join(names)


def q27(t):
    """The narrowest gap is six to one and the widest is eleven to one."""
    ratios = _ratios(t)
    lo, hi = min(ratios.values()), max(ratios.values())
    assert round(lo) == 6, f"the narrowest ratio is {lo:.2f}, not six to one"
    assert round(hi) == 11, f"the widest ratio is {hi:.2f}, not eleven to one"
    schools = [r for r in t["rows"] if "school" in r[0].lower()][0]
    assert gc.num(schools[1]) == 24 and gc.num(schools[2]) == 4, \
        f"the schools row is {schools[1]} against {schools[2]}, not 24 against 4"
    return (f"narrowest gap {lo:.0f} to 1, widest {hi:.0f} to 1; schools row "
            f"{schools[1]} against {schools[2]}")


def q28(t):
    """Neither column leads throughout; restricting leads first, protecting leads third."""
    res = [gc.num(c) for c in _col(t, RESTRICT)]
    pro = [gc.num(c) for c in _col(t, PROTECT)]
    leaders = ["restricting" if r > p else "protecting" for r, p in zip(res, pro)]
    assert leaders[0] == "restricting", f"the first period leads {leaders[0]}"
    assert leaders[2] == "protecting", f"the third period leads {leaders[2]}"
    assert len(set(leaders)) == 2, f"one column leads in every period: {leaders}"
    return (f"restricting {', '.join(f'{r:.0f}' for r in res)} against protecting "
            f"{', '.join(f'{p:.0f}' for p in pro)}; leaders {', '.join(leaders)}")


def q29(t):
    """The leading column changes across the four periods."""
    res = [gc.num(c) for c in _col(t, RESTRICT)]
    pro = [gc.num(c) for c in _col(t, PROTECT)]
    assert len(t["rows"]) == 4, f"{len(t['rows'])} periods, not four"
    assert any(r > p for r, p in zip(res, pro)), "no period restricts more than it protects"
    assert any(p > r for r, p in zip(res, pro)), "no period protects more than it restricts"
    return ("both directions occur: restricting leads in "
            f"{sum(1 for r, p in zip(res, pro) if r > p)} of {len(res)} periods and "
            f"protecting in {sum(1 for r, p in zip(res, pro) if p > r)}")


def q30(t):
    """The protecting share falls between the third and fourth periods while still leading."""
    rows = t["rows"]
    r3, r4 = rows[2], rows[3]
    s3 = gc.pct(gc.num(r3[2]), gc.num(r3[1]) + gc.num(r3[2]))
    s4 = gc.pct(gc.num(r4[2]), gc.num(r4[1]) + gc.num(r4[2]))
    assert s3 > s4, f"the protecting share rose, {s3} to {s4}"
    assert gc.num(r4[2]) > gc.num(r4[1]), "protecting no longer leads in the fourth period"
    # Tolerance rather than round(): Python rounds half to EVEN, so round(54.5)
    # is 54 and this assertion failed against a key that correctly says "about
    # 55 percent". A checker that is wrong about arithmetic is the worst kind,
    # because the thing it is checking is arithmetic.
    assert abs(s3 - 83) <= 0.5 and abs(s4 - 55) <= 0.5, \
        f"the shares are {s3} and {s4}, not the about 83 and about 55 the key states"
    return (f"protecting share {s3} percent in the third period against {s4} in the fourth, "
            f"a fall of {s3 - s4:.1f} points with the lead intact")


# --- module-specific content gates -------------------------------------------

_MONOTONE = (
    "steady progress", "steadily expanded", "steadily narrowed", "without interruption",
    "continuous improvement", "continuous decline", "has always protected",
    "has never restricted", "has never protected", "only in one direction",
    "an uninterrupted expansion",
)


def _oscillation(module):
    """No key may narrate EK 3.12.A.1's list as a one-way trend."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for phrase in _MONOTONE:
            if phrase in key:
                bad.append(f"q{i} key: narrates the record as {phrase!r}; LO 3.12.A is written "
                           "AT TIMES ALLOWED THE RESTRICTION and AT OTHER TIMES HAS PROTECTED, "
                           "and EK 3.12.A.1's four items alternate direction")
    q1 = module.QUESTIONS[0]
    k1 = q1["choices"][q1["ans"]].lower()
    if "restricted" not in k1 or "protected" not in k1:
        bad.append("q1: the key no longer states both halves of EK 3.12.A.1's introducing "
                   "sentence, restricted at some times and protected at others")
    q23 = module.QUESTIONS[22]
    if "not a single direction" not in q23["choices"][q23["ans"]].lower():
        bad.append("q23: the key no longer refuses the progress narrative, which is the one "
                   "reading of this topic that contradicts its own objective")
    if bad:
        print(f"FAIL {module.__name__} oscillation")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} oscillation: no key narrates EK 3.12.A.1's list as a one-way "
          "trend, and the items that make the alternation the question still state it")


# The fourteen required cases (CED p. 30). Any other "X v. Y" in this module is
# a case the framework does not put in a student's hands -- most pressingly the
# one that decided the separate but equal doctrine, which EK 3.12.A.1.ii
# describes without naming. A pattern rather than a word list is used because
# the risk is an UNKNOWN name being added later, which no allowlist of wrong
# answers could anticipate.
#
# The comparison is on the WORD EITHER SIDE of " v. ", not on a captured span.
# The first draft matched a run of capitalised words and reported a false
# finding on item 11, whose stem opens "In Brown v. Board of Education" -- the
# sentence-initial "In" was absorbed into the name and the containment test then
# failed against "brown v. board of education". A two-word signature has no
# left edge to get wrong, which is the whole reason for choosing it.
_REQUIRED_PAIRS = {
    ("marbury", "madison"), ("mcculloch", "maryland"), ("schenck", "united"),
    ("brown", "board"), ("baker", "carr"), ("engel", "vitale"),
    ("gideon", "wainwright"), ("tinker", "des"), ("co", "united"), ("times", "united"),
    ("wisconsin", "yoder"), ("shaw", "reno"), ("states", "lopez"),
    ("mcdonald", "chicago"), ("united", "federal"), ("united", "fec"),
}
_VS = re.compile(r"([A-Za-z]+)\.?\s+v\.\s+([A-Za-z]+)")


def _case_names(module):
    """Only the CED's required cases may be named anywhere in the module."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        strings = [("stem", item["q"]), ("why", item["why"])]
        strings += [(f"choice {'ABCDE'[k]}", c) for k, c in enumerate(item["choices"])]
        for label, s in strings:
            for m in _VS.finditer(s):
                pair = (m.group(1).lower(), m.group(2).lower())
                if pair not in _REQUIRED_PAIRS:
                    bad.append(f"q{i} {label}: names {m.group(0)!r}, which is not one of the "
                               "CED's fourteen required cases. EK 3.12.A.1.ii describes the "
                               "separate but equal doctrine WITHOUT naming a case, and adding "
                               "one puts content the exam cannot ask about beside content it "
                               "can")
    if bad:
        print(f"FAIL {module.__name__} case names")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} case names: every case named anywhere in the module is one "
          "of the CED's fourteen required cases, and the separate but equal doctrine is "
          "described exactly as EK 3.12.A.1.ii describes it, without a case name")


_TERMS = {
    12: ("facts", "relevant events that occurred before the courts became involved"),
    13: ("issue", "legal or constitutional question the court considered"),
    14: ("holding", "the reasoning is the explanation of that response"),
    15: ("decision", "outcome including the facts, the issue, the holding, and the reasoning"),
    16: ("majority opinion", "agreed to by more than half the justices"),
}


def _scotus_terms(module):
    """The CED's six analysis words keep the CED's own definitions."""
    bad = []
    for i, (term, definition) in _TERMS.items():
        key = module.QUESTIONS[i - 1]["choices"][module.QUESTIONS[i - 1]["ans"]].lower()
        if definition not in key:
            bad.append(f"q{i}: the key for {term.upper()} no longer carries the CED's own "
                       f"definition (p. 29), {definition!r}")
    # Nothing in the module may ask about a dissent or concurrence: CED p. 29
    # says students are not expected to know them for required cases.
    for i, item in enumerate(module.QUESTIONS, 1):
        low = (item["q"] + " " + " ".join(item["choices"])).lower()
        for word in ("dissenting opinion", "concurring opinion", "dissent in", "concurrence"):
            if word in low:
                bad.append(f"q{i}: refers to a {word!r}; CED p. 29 says students are not "
                           "expected to know dissenting or concurring opinions of required "
                           "cases")
    if bad:
        print(f"FAIL {module.__name__} scotus terms")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} scotus terms: facts, issue, holding, reasoning, decision and "
          "majority opinion all keep the CED's p. 29 definitions, and no item asks about a "
          "dissenting or concurring opinion")


ua.shape(v3_12)
ua.check(v3_12, ANCHORS, GROUNDING)
ua.notation(v3_12)
_oscillation(v3_12)
_case_names(v3_12)
_scotus_terms(v3_12)
gc.check(v3_12, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
