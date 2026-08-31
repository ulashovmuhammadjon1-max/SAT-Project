"""Structural gate for AP U.S. Government 4.5 Measuring Public Opinion.

gov345_check plus the four usgov_anchor helpers, plus three content gates.

  _poll_types  EK 4.5.A.1 names four types and gives each a parenthesis, and the
               four are distinguished BY PURPOSE, not by timing:
                   opinion    public opinion on various issues
                   benchmark  BASELINE views of a candidate
                   tracking   how views of a candidate CHANGE DURING a campaign
                   exit       WHY PEOPLE VOTED THE WAY THEY DID
               Sorting them by when they happen -- before, during, after -- gets
               benchmark and tracking right by accident and exit polls wrong on
               the only point that matters. An exit poll is not "the poll taken
               on election day" and it is not a projection of the winner; the
               framework defines it by the reasons behind a vote. The gate
               refuses any key that gives one type another's parenthesis,
               attributing a parenthesis to the type NEAREST BEFORE IT so that
               items 7 and 23, whose keys correctly contrast two types in one
               sentence, are not reported.

  _methodology EK 4.5.A.2's three elements each carry a parenthesis too, and two
               of them are routinely lost. The margin of error belongs INSIDE
               accurate sampling, not beside it -- it is a property of how the
               sample was drawn. And accurate reporting is not "publish the
               numbers"; it is "conclusions that CAN BE SUPPORTED BY THE DATA",
               which is a limit on what may be claimed from data already
               collected. The gate pins both, and pins the framework's
               comparative MORE PRECISE: EK 4.5.A.2 does not sort polls into
               valid and invalid, so no key may.

  _margin      The margin of error is the hinge of this topic and the only one
               of the seven named items that changes what a reader may CONCLUDE
               rather than how a number was produced. The suggested skill here
               is 3.C -- explain patterns and trends in data TO DRAW CONCLUSIONS
               -- so three items turn on a lead sitting inside a margin. Two
               wrong readings are equally available and the gate refuses both:
               that the higher number wins anyway, and that a difference inside
               the margin is a finding of an exact tie. It also refuses treating
               such a poll as worthless, which is the overcorrection.

The CED attaches no foundational document and no required case to 4.5.A, so
nothing in this module is quoted and all three tables are labelled hypothetical.
"""
import gov345_check as gc
import usgov_anchor as ua
import v4_5

ANCHORS = {
 1: "Elections and policy debates",
 2: "examples rather than a complete catalogue",
 3: "Public opinion on various issues",
 4: "Creates baseline views of a candidate",
 5: "Follows how views of a candidate change during a campaign",
 6: "Data on why people voted the way they did",
 7: "because the framework defines them by the reasons behind a vote rather than by their",
 8: "since it creates baseline views of a candidate",
 9: "since it collects data on why people voted the way they did",
 10: "Polling methodology",
 11: "Accurate sampling methods, neutral framing of questions, and accurate reporting",
 12: "Calculating a margin of error",
 13: "Specific and unbiased wording of questions",
 14: "Clear reporting, and conclusions that can be supported by the data",
 15: "improve methodology by degree rather than dividing polls into valid and invalid",
 16: "since the framework requires conclusions that can be supported by the data",
 17: "expressing the uncertainty that sampling a subset rather than everyone creates",
 18: "can produce different data from the same electorate",
 19: "The sampling method used, including the margin of error calculated from it",
 20: "and reporting one as leading would exceed what the data support",
 21: "Which of the four types of poll produces the most reliable data",
 22: "while the undecided share fell, and the gap between the two candidates narrowed",
 23: "since it follows how views of a candidate change during a campaign",
 24: "since the difference between them is smaller than the reported margin of error",
 25: "moved reported support by 37 percentage points",
 26: "which the framework glosses as specific and unbiased wording",
 27: "without describing it further",
 28: "the reported margin of error falls or stays the same",
 29: "Polls 3 and 4 only",
 30: "so the lead is inside the margin and the poll does not establish one",
}

GROUNDING = {
 1: "EK 4.5.A.1 and EK 4.5.A.2 both open with 'public opinion data that can affect elections "
    "and policy debates', which is what makes polling a subject of this course.",
 2: "EK 4.5.A.1's phrase 'different types of scientific polls SUCH AS', which marks the four "
    "as illustrative rather than exhaustive.",
 3: "EK 4.5.A.1.i's parenthesis, verbatim: 'measuring public opinion on various issues'.",
 4: "EK 4.5.A.1.ii's parenthesis, verbatim: 'creating baseline views of a candidate'.",
 5: "EK 4.5.A.1.iii's parenthesis, verbatim: 'following how views of a candidate change during "
    "a campaign'. Repetition over time is what makes change observable.",
 6: "EK 4.5.A.1.iv's parenthesis, verbatim: 'collecting data on why people voted the way they "
    "did'. Defined by subject, not by the day it is taken.",
 7: "EK 4.5.A.1's four parentheses tested against a timing-based sort. Three mention a "
    "candidate or campaign, so timing roughly works for those; the exit poll is defined by "
    "what it collects, so a poll taken after voting that asked something else would not be one.",
 8: "EK 4.5.A.1.ii applied. That later polls are compared against a baseline is what a "
    "baseline is for, and does not make the baseline a tracking poll.",
 9: "EK 4.5.A.1.iv applied. Asking which issues affected a choice already made is data on why "
    "people voted as they did, not an opinion poll about issues.",
 10: "EK 4.5.A.2, verbatim: public opinion data 'is influenced by polling methodology'.",
 11: "EK 4.5.A.2's three elements: accurate sampling methods, neutral framing of questions, "
     "and accurate reporting.",
 12: "EK 4.5.A.2.i, verbatim: 'accurate sampling methods, including calculating a margin of "
     "error'. The framework places the margin inside sampling.",
 13: "EK 4.5.A.2.ii's parenthesis, verbatim: 'specific and unbiased wording of questions'. Both "
     "adjectives are the framework's own.",
 14: "EK 4.5.A.2.iii's parenthesis, verbatim: 'clear reporting and conclusions that can be "
     "supported by the data'. The second half limits what may be claimed.",
 15: "EK 4.5.A.2's comparative MORE PRECISE, which describes a scale rather than a threshold.",
 16: "EK 4.5.A.2.iii applied to a poll whose collection was sound and whose summary was not. "
     "The framework lists reporting separately for exactly this case.",
 17: "EK 4.5.A.2.i's placement of the margin of error inside sampling: the margin exists "
     "because a poll measures some of the population rather than all of it.",
 18: "EK 4.5.A.2's central claim, that public opinion data is influenced by polling "
     "methodology. Divergent results from one electorate are what that claim predicts.",
 19: "LO 4.5.A's word ELEMENTS against EK 4.5.A.2's three, with the margin of error inside the "
     "first. The distractors are facts about a poll the framework never makes elements.",
 20: "EK 4.5.A.2.i and EK 4.5.A.2.iii together: a difference inside the margin is not "
     "distinguishable from no difference, so reporting a lead exceeds what the data support.",
 21: "EK 4.5.A.1 read for what it omits: four types listed with no ranking, and EK 4.5.A.2's "
     "three elements apply to any of them.",
 22: "Data item, CED skill 3.C. Both candidate series, the undecided series and the closing "
     "gap are recomputed below.",
 23: "EK 4.5.A.1.iii located in a repeated series. A benchmark poll is a single baseline "
     "measurement rather than a series, which is what the second option gets wrong.",
 24: "EK 4.5.A.2.i and iii applied to the final row: a 1 point gap against a stated margin of "
     "3. Recomputed below.",
 25: "Data item, CED skill 3.C. The spread across the four wordings is recomputed below.",
 26: "EK 4.5.A.2.ii located in a table that holds the sample, the proposal and the week "
     "constant and varies only the wording.",
 27: "EK 4.5.A.2.ii's gloss applied to four candidate wordings, three of which characterize "
     "the proposal before asking about it.",
 28: "Data item, CED skill 3.C. The relationship between sample size and margin is recomputed "
     "below, including the tie between the last two polls.",
 29: "Data item: comparing each poll's lead with its own margin. Recomputed below, including "
     "the poll whose lead exactly equals its margin.",
 30: "EK 4.5.A.2.iii applied to a lead inside a margin. Recomputed below.",
}

A_COL, B_COL, UND = "Candidate A (%)", "Candidate B (%)", "Undecided (%)"
SUPPORT = "Expressed support (%)"
SIZE, MOE, LEAD = ("Sample size", "Reported margin of error (percentage points)",
                   "Reported lead for Candidate A (percentage points)")


def _col(t, header):
    j = t["headers"].index(header)
    return [gc.num(r[j]) for r in t["rows"]]


def q22(t):
    """Both candidates rise, undecided falls, and the gap narrows."""
    a, b, u = _col(t, A_COL), _col(t, B_COL), _col(t, UND)
    for name, series in (("A", a), ("B", b)):
        assert series == sorted(series) and series[-1] > series[0], \
            f"candidate {name} does not gain: {series}"
    assert u == sorted(u, reverse=True) and u[-1] < u[0], f"the undecided share is {u}"
    gaps = [x - y for x, y in zip(a, b)]
    assert gaps[-1] < gaps[0], f"the gap widened: {gaps}"
    for row in t["rows"]:
        assert sum(gc.num(c) for c in row[1:]) == 100, f"row {row[0]!r} does not total 100"
    return (f"A {a[0]:.0f} to {a[-1]:.0f}, B {b[0]:.0f} to {b[-1]:.0f}, undecided "
            f"{u[0]:.0f} to {u[-1]:.0f}; gap {gaps[0]:.0f} to {gaps[-1]:.0f}; rows total 100")


def q23(t):
    """A repeated series of four, which is what a tracking poll produces."""
    assert len(t["rows"]) == 4, f"{len(t['rows'])} observations, not four"
    labels = [r[0] for r in t["rows"]]
    assert len(set(labels)) == 4 and all("Week" in l for l in labels), f"labels are {labels}"
    return f"one question repeated at {len(labels)} points in a campaign: {', '.join(labels)}"


def q24(t):
    """The final gap is 1 point, inside the stated margin of 3."""
    a, b = _col(t, A_COL), _col(t, B_COL)
    gap = a[-1] - b[-1]
    assert gap == 1, f"the final gap is {gap:.0f}, not the 1 the item relies on"
    assert 0 < gap < 3, f"the final gap {gap:.0f} is not strictly inside a margin of 3"
    assert a[-1] != b[-1], "the final figures are equal, which would make it a reported tie"
    return (f"final week {a[-1]:.0f} against {b[-1]:.0f}, a gap of {gap:.0f} point inside the "
            "stated margin of 3 -- and not an exact tie")


def q25(t):
    """Support spreads 37 points across four wordings."""
    s = _col(t, SUPPORT)
    spread = max(s) - min(s)
    assert spread == 37, f"the spread is {spread:.0f} points, not the 37 the key states"
    assert max(s) == 71 and min(s) == 34, f"the extremes are {max(s):.0f} and {min(s):.0f}"
    assert len(set(s)) == len(s), "two wordings produced identical support"
    return (f"support {', '.join(f'{x:.0f}' for x in s)} -- spread {spread:.0f} points from "
            f"{min(s):.0f} to {max(s):.0f}")


def q26(t):
    """Four distinct wordings, one variable."""
    wordings = [r[0] for r in t["rows"]]
    assert len(set(wordings)) == 4, f"a wording is repeated: {wordings}"
    assert len(t["headers"]) == 2, "the table varies more than the wording"
    return f"{len(wordings)} distinct wordings against a single support column"


def q27(t):
    """Exactly one wording attaches no characterization to the proposal."""
    loaded = ("experts say", "costly", "finally fix", "would help")
    plain = [r[0] for r in t["rows"] if not any(w in r[0].lower() for w in loaded)]
    assert len(plain) == 1, f"{len(plain)} wordings carry no characterization: {plain}"
    assert "favor or oppose" in plain[0].lower(), \
        f"the plain wording does not offer both alternatives: {plain[0]!r}"
    return f"one unloaded wording of four, offering both alternatives: {plain[0]!r}"


def q28(t):
    """Margin never rises as sample size grows, and it ties at the top."""
    size, moe = _col(t, SIZE), _col(t, MOE)
    assert size == sorted(size) and len(set(size)) == len(size), f"sample sizes are {size}"
    assert all(y <= x for x, y in zip(moe, moe[1:])), f"the margin rises somewhere: {moe}"
    assert moe[-1] == moe[-2], \
        "the last two margins differ, so the key's 'or stays the same' has nothing to cover"
    return (f"sample sizes {', '.join(f'{x:.0f}' for x in size)} against margins "
            f"{', '.join(f'{x:.0f}' for x in moe)} -- never rising, tied at the top")


def q29(t):
    """Exactly polls 3 and 4 report a lead strictly larger than their own margin."""
    labels = [r[0] for r in t["rows"]]
    moe, lead = _col(t, MOE), _col(t, LEAD)
    exceed = [l for l, m, d in zip(labels, moe, lead) if d > m]
    assert exceed == ["Poll 3", "Poll 4"], f"the polls exceeding their margin are {exceed}"
    equal = [l for l, m, d in zip(labels, moe, lead) if d == m]
    assert equal == ["Poll 2"], \
        f"the poll whose lead equals its margin is {equal}, which the rationale names"
    return (f"leads {', '.join(f'{x:.0f}' for x in lead)} against margins "
            f"{', '.join(f'{x:.0f}' for x in moe)} -- exceeded in {', '.join(exceed)}, "
            f"equal in {equal[0]}")


def q30(t):
    """Poll 1 reports a lead of 3 inside a margin of 5."""
    row = [r for r in t["rows"] if r[0] == "Poll 1"]
    assert len(row) == 1, "Poll 1 is missing or duplicated"
    moe, lead = gc.num(row[0][2]), gc.num(row[0][3])
    assert lead == 3 and moe == 5, f"Poll 1 reads lead {lead:.0f}, margin {moe:.0f}"
    assert lead < moe, "Poll 1's lead is not inside its margin"
    assert lead > 0, "Poll 1 reports no lead, so the key's first clause fails"
    assert moe == max(_col(t, MOE)), "Poll 1 does not carry the largest margin in the table"
    return f"Poll 1: lead {lead:.0f} inside margin {moe:.0f}, the largest margin of the four"


# --- module-specific content gates -------------------------------------------

_TYPES = ("opinion poll", "benchmark poll", "tracking poll", "exit poll")
_PARENS = {
    "opinion poll": "public opinion on various issues",
    "benchmark poll": "baseline views of a candidate",
    "tracking poll": "how views of a candidate change during a campaign",
    "exit poll": "why people voted the way they did",
}


def _nearest_type(text, at):
    """Whichever poll type name sits nearest before an offset."""
    best, best_at = None, -1
    for name in _TYPES:
        pos = text.rfind(name, 0, at)
        if pos > best_at:
            best, best_at = name, pos
    return best


def _poll_types(module):
    """No type may be given another's parenthesis."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        if not any(t in key for t in _TYPES):
            continue
        for owner, paren in _PARENS.items():
            at = key.find(paren)
            while at >= 0:
                near = _nearest_type(key, at)
                if near is not None and near != owner:
                    bad.append(f"q{i} key: attaches {paren!r} to a {near}; EK 4.5.A.1 gives "
                               f"that parenthesis to the {owner}")
                    break
                at = key.find(paren, at + 1)
    pins = {3: "opinion poll", 4: "benchmark poll", 5: "tracking poll", 6: "exit poll"}
    for n, kind in pins.items():
        key = module.QUESTIONS[n - 1]["choices"][module.QUESTIONS[n - 1]["ans"]].lower()
        if _PARENS[kind] not in key:
            bad.append(f"q{n}: the key for the {kind} no longer carries EK 4.5.A.1's own "
                       f"parenthesis, {_PARENS[kind]!r}")
    # An exit poll is not a projection of the result.
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        if "exit poll" in key:
            for wrong in ("who won", "the official result", "certified vote totals",
                          "counts the ballots"):
                if wrong in key:
                    bad.append(f"q{i} key: makes an exit poll about {wrong!r}; EK 4.5.A.1.iv "
                               "defines it as collecting data on WHY people voted as they did")
    if bad:
        print(f"FAIL {module.__name__} poll types")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} poll types: no key gives one of EK 4.5.A.1's four types "
          "another's parenthesis, all four definitions survive, and no key turns an exit poll "
          "into a projection of the result")


def _methodology(module):
    """EK 4.5.A.2's three elements keep their parentheses and its comparative."""
    bad = []
    q11 = module.QUESTIONS[10]
    k11 = q11["choices"][q11["ans"]].lower()
    for part in ("sampling", "framing", "reporting"):
        if part not in k11:
            bad.append(f"q11: the key has dropped {part!r}, one of EK 4.5.A.2's three elements")
    q12 = module.QUESTIONS[11]
    if "margin of error" not in q12["choices"][q12["ans"]].lower():
        bad.append("q12: the key no longer places the margin of error inside EK 4.5.A.2.i's "
                   "accurate sampling methods")
    q14 = module.QUESTIONS[13]
    k14 = q14["choices"][q14["ans"]].lower()
    if "supported by the data" not in k14:
        bad.append("q14: the key no longer carries EK 4.5.A.2.iii's limit, conclusions that "
                   "CAN BE SUPPORTED BY THE DATA -- without it accurate reporting collapses "
                   "into merely publishing the numbers")
    binaries = ("is not a poll at all", "guaranteed to be correct", "divides polls into valid",
                "makes a poll accurate", "makes a poll scientific")
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for b_ in binaries:
            if b_ in key and "rather than" not in key:
                bad.append(f"q{i} key: turns EK 4.5.A.2's comparative MORE PRECISE into a "
                           f"threshold ({b_!r}); the framework describes a scale")
    if bad:
        print(f"FAIL {module.__name__} methodology")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} methodology: EK 4.5.A.2's three elements keep their "
          "parentheses, the margin of error stays inside accurate sampling, and MORE PRECISE "
          "stays a comparative")


def _margin(module):
    """A lead inside the margin establishes nothing -- and is not a tie, and not worthless."""
    bad = []
    wrong = (
        ("the candidate with the higher number is leading",
         "a difference inside the margin is not distinguishable from no difference"),
        ("shows the two candidates are exactly tied",
         "a gap inside the margin is not a finding of an exact tie"),
        ("the poll should be disregarded entirely",
         "a poll whose lead is inside its margin is still evidence, just not of a lead"),
        ("recalculated until the lead exceeds",
         "the margin follows from the sampling and is not adjustable to fit a conclusion"),
    )
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for phrase, note in wrong:
            if phrase in key:
                bad.append(f"q{i} key: states {phrase!r}; {note}")
    # Stem AND key: item 20's stem states the margin and its key states the
    # consequence, which is the right division of labour for the item and would
    # have been reported as a failure by a key-only check.
    for n in (20, 24, 30):
        item = module.QUESTIONS[n - 1]
        text = (item["q"] + " " + item["choices"][item["ans"]]).lower()
        if "margin" not in text:
            bad.append(f"q{n}: the key no longer turns on the margin of error, which is the "
                       "only one of EK 4.5.A's seven named items that limits what may be "
                       "CONCLUDED rather than describing how a number was produced")
    if bad:
        print(f"FAIL {module.__name__} margin")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} margin: no key reads a lead inside the margin as a lead, as "
          "an exact tie, or as grounds for discarding the poll, and all three items that turn "
          "on the margin still do")


ua.shape(v4_5)
ua.check(v4_5, ANCHORS, GROUNDING)
ua.notation(v4_5)
_poll_types(v4_5)
_methodology(v4_5)
_margin(v4_5)
gc.check(v4_5, arith={22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27,
                      28: q28, 29: q29, 30: q30})
