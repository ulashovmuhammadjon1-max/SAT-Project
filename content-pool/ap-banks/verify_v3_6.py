"""Structural gate for AP U.S. Government 3.6 Amendments: Balancing Individual Freedom
with Public Order and Safety.

gov345_check plus the four usgov_anchor helpers.

THE OBJECTIVE CARRIES THE TOPIC, NOT THE ESSENTIAL KNOWLEDGE
--------------------------------------------------------------
EK 3.6.A.1 and EK 3.6.A.2 name three amendments and three subjects and settle
nothing. What makes this a topic rather than a list is LO 3.6.A's verb: the
Court has ATTEMPTED TO BALANCE claims of individual freedom against laws and
procedures promoting public order and safety. Both sides of that scale are
legitimate in the framework's terms, which means an answer naming only one is
incomplete even when the fact it names is true. _both_sides below asserts no key
declares either consideration illegitimate.

EK 3.6.A.2 IS A GRID, NOT A TRADE-OFF
---------------------------------------
Its question is whether a measure "promotes OR INTERFERES WITH public safety AND
individual rights". Two independent questions, four combinations. A student who
frames the debate as a trade-off has no place for the combination that matters
most to an argument: a measure that burdens rights AND does not deliver safety.
Items 15 to 17 are built on the full grid and the grid table has four rows for
that reason -- q22 asserts all four combinations are present, so a later edit
cannot collapse it back into two.

WHERE THE FRAMEWORK SAYS "DEBATE", THIS BANK TAKES NO SIDE
------------------------------------------------------------
EK 3.6.A.2 identifies firearms regulation and metadata collection as subjects of
debate and resolves neither; EK 3.6.A.1 describes interpretation of an open
standard rather than a settled rule. So every item asks what the debate
consists of, what would count as evidence in it, or what a required case
actually held. _no_position fails the module if a key asserts that any of the
three contested measures is or is not justified. SOCIAL_BRIEF.md's rule against
guessing binds hardest exactly where the framework itself says the question is
open.
"""
import gov345_check as gc
import usgov_anchor as ua
import v3_6

ANCHORS = {
 1: "Balance claims of individual freedom with laws and enforcement procedures",
 2: "struck case by case and remains contested",
 3: "the disagreement is about how they were weighed",
 4: "the Eighth Amendment and its application to death penalty statutes",
 5: "are standards rather than rules",
 6: "Bail and fines",
 7: "Death penalty statutes",
 8: "given that the text supplies no list",
 9: "involve interpretation of the Eighth Amendment and its application to statutes",
 10: "the constraint on how far it may go is the individual freedom side",
 11: "whether regulation of firearms or collection of digital metadata promotes or interferes",
 12: "Government regulation of firearms and collection of digital metadata",
 13: "Unreasonable, since whether a particular collection is unreasonable",
 14: "information held by third parties about a person's activity fits none of those categories",
 15: "Four, since a measure may promote or fail to promote safety",
 16: "burdens rights and does NOT in fact promote safety",
 17: "Does the collection actually improve safety, and does it burden individual rights?",
 18: "produced no better outcomes than comparable investigations",
 19: "experienced a measurable decline relative to those that did not",
 20: "the debate now takes place within a constitutional constraint",
 21: "burdens the majority would not accept for itself",
 22: "more than the six that promoted safety without burdening rights",
 23: "because a measure's effect on safety and its effect on rights are separate questions",
 24: "depends on how heavily each effect weighs",
 25: "so contents are not the only thing that matters",
 26: "quantity and duration of collection can matter",
 27: "one required a warrant and the other did not",
 28: "interpreted open-ended standards case by case",
 29: "how far a government may go in the name of order and safety",
 30: "supply evidence that bears on whether the measure promotes safety",
}

GROUNDING = {
 1: "LO 3.6.A, verbatim: the Court has 'attempted to balance claims of individual freedom with "
    "laws and enforcement procedures that promote public order and safety.'",
 2: "LO 3.6.A's verb ATTEMPTED with EK 3.6.A.2's continuing debate: a balance redrawn case by "
    "case rather than fixed.",
 3: "LO 3.6.A puts both considerations on the scale, so a criticism of the weighting is inside "
    "the framework's terms and a claim that one side does not count is outside them.",
 4: "EK 3.6.A.1, verbatim: decisions defining cruel and unusual punishment 'involve "
    "interpretation of the Eighth Amendment and its application to death penalty statutes.'",
 5: "U.S. Constitution, Eighth Amendment, quoted verbatim. A clause forbidding what is 'cruel "
    "and unusual' without a list is a standard, which is why EK 3.6.A.1's word is interpretation.",
 6: "U.S. Constitution, Eighth Amendment's three clauses: excessive bail, excessive fines, "
    "cruel and unusual punishments.",
 7: "EK 3.6.A.1's named application: death penalty statutes. Firearms and metadata belong to "
    "EK 3.6.A.2, a separate statement about different amendments.",
 8: "EK 3.6.A.1's interpretive work stated as the question a court must answer.",
 9: "EK 3.6.A.1 applied to a scenario; the distractors name EK 3.6.A.2 and topics 3.3 to 3.5.",
 10: "LO 3.6.A's balance located in the Eighth Amendment: a punishment is an enforcement "
     "procedure promoting order, with a constitutional ceiling on it.",
 11: "EK 3.6.A.2, verbatim: the debate 'involves concerns about public safety and whether or "
     "not the government regulation of firearms or collection of digital metadata promotes or "
     "interferes with public safety and individual rights.'",
 12: "EK 3.6.A.2's two named subjects, one for each amendment: firearms under the Second, "
     "digital metadata under the Fourth.",
 13: "U.S. Constitution, Fourth Amendment, quoted verbatim. UNREASONABLE is the open term a "
     "court must fill in when a new form of collection appears.",
 14: "The Fourth Amendment's four nouns -- persons, houses, papers, effects -- against "
     "EK 3.6.A.2's metadata, a category the text does not obviously cover.",
 15: "EK 3.6.A.2's phrasing counted: 'promotes or interferes with public safety AND individual "
     "rights' is two independent questions and therefore four combinations.",
 16: "EK 3.6.A.2's fourth possibility, the one a trade-off framing has no place for: a burden "
     "on rights that buys no safety.",
 17: "EK 3.6.A.2's two questions stated as an analyst's checklist; popularity, cost and "
     "feasibility are real considerations the framework does not put on this scale.",
 18: "CED skill 5.B: a claim about whether a program improves outcomes needs a comparison of "
     "outcomes as evidence.",
 19: "CED skill 5.B applied to EK 3.6.A.2's firearms half: whether a measure PROMOTES safety "
     "is an empirical claim requiring a comparison.",
 20: "McDonald v. Chicago (2010), required case, which the CED attaches to 3.6.A. CED holding: "
     "the right to keep and bear arms for self-defense is applicable to the states -- which "
     "frames the debate constitutionally without resolving it.",
 21: "'Letter from a Birmingham Jail' (required document), the unjust-law test, quoted "
     "verbatim; the CED attaches the Letter to 3.6.A.",
 22: "Data item on a labelled hypothetical; the four category counts are recomputed below.",
 23: "EK 3.6.A.2's grid structure made visible: four rows because two independent questions.",
 24: "Data item, CED skill 3.E: a category count treats a small burden and a large one as "
     "identical, and LO 3.6.A's balance is about weight.",
 25: "Data item on a labelled hypothetical; the contents/warrant pattern is recomputed below.",
 26: "EK 3.6.A.2's metadata question: a category with no contents that still required a "
     "warrant shows the standard turning on something else.",
 27: "Data item; two rows agreeing in one column and differing in another is what refutes the "
     "single-column inference.",
 28: "LO 3.6.A's 'attempted', with EK 3.6.A.1's open standard and EK 3.6.A.2's continuing "
     "debate: work in progress rather than a settled rule.",
 29: "LO 3.6.A names the balance rather than any amendment, which is why the Eighth, Second "
     "and Fourth share a topic.",
 30: "CED skill 5.B with EK 3.6.A.2's two questions: the evidence must bear on safety and on "
     "rights, and the framework resolves neither debate.",
}

SAFETY, RIGHTS, COUNT = ("Effect on public safety", "Effect on individual rights",
                         "Measures in this category")
CONTENTS, WARRANT = ("Contents of communications included?", "Held to require a warrant?")
DIALED = "Numbers dialed and call durations"
LOCATION = "Location of a device over several months"
RECORDINGS = "Recordings of conversations"
ENVELOPES = "Addresses on the outside of mailed envelopes"


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def _cell(t, label, header):
    j = t["headers"].index(header)
    for r in t["rows"]:
        if r[0] == label:
            return r[j]
    raise KeyError(label)


def _n(t, safety, rights):
    for r in t["rows"]:
        if r[0] == safety and r[1] == rights:
            return gc.num(r[2])
    raise KeyError((safety, rights))


def q22(t):
    """Burden without benefit outnumbers benefit without burden."""
    burden_no_benefit = _n(t, "Does not promote", "Burdens")
    benefit_no_burden = _n(t, "Promotes", "Does not burden")
    assert burden_no_benefit > benefit_no_burden, \
        f"{burden_no_benefit} against {benefit_no_burden}"
    total = sum(gc.num(c) for c in _col(t, COUNT))
    assert total == 40, f"the counts sum to {total}, not the forty the stem states"
    promotes = _n(t, "Promotes", "Burdens") + benefit_no_burden
    assert promotes * 2 > total, "a majority of measures no longer promote safety"
    assert _n(t, "Does not promote", "Does not burden") > 0, \
        "the fourth category is empty, which would make a distractor true"
    return (f"{burden_no_benefit:.0f} burden rights without promoting safety against "
            f"{benefit_no_burden:.0f} the other way; {promotes:.0f} of {total:.0f} promote safety")


def q23(t):
    """All four combinations of the two independent questions are present."""
    pairs = {(r[0], r[1]) for r in t["rows"]}
    expected = {("Promotes", "Burdens"), ("Promotes", "Does not burden"),
                ("Does not promote", "Burdens"), ("Does not promote", "Does not burden")}
    assert pairs == expected, f"the grid is not complete: {sorted(pairs)}"
    assert len(t["rows"]) == 4, f"{len(t['rows'])} rows, not the four the grid needs"
    return "all four combinations of the two independent questions present"


def q24(t):
    """The table reports counts and nothing about magnitude."""
    assert all(c.isdigit() for c in _col(t, COUNT)), "the count column is no longer counts"
    assert not any(k in h.lower() for h in t["headers"]
                   for k in ("severity", "magnitude", "how much", "weight")), \
        "a column now reports magnitude, which the item says is absent"
    return "counts only; nothing in the table reports how heavily either effect weighs"


def q25(t):
    """A warrant was required in a category with no contents."""
    assert _cell(t, LOCATION, CONTENTS) == "No" and _cell(t, LOCATION, WARRANT) == "Yes", \
        "the location row no longer breaks the contents-only rule"
    with_contents = [r[0] for r in t["rows"] if _cell(t, r[0], CONTENTS) == "Yes"]
    assert with_contents == [RECORDINGS], f"contents rows are {with_contents}"
    return "location: no contents, warrant required -- so contents is not the only trigger"


def q26(t):
    """The location row is distinguished by duration, which the label must still say."""
    assert "over several months" in LOCATION, \
        "the location row no longer states the duration the item turns on"
    assert _cell(t, DIALED, WARRANT) == "No", \
        "the dialed-numbers row now requires a warrant, removing the contrast"
    return "location over several months required a warrant; dialed numbers did not"


def q27(t):
    """Two rows agree on contents and differ on the warrant, which refutes the inference."""
    assert _cell(t, ENVELOPES, CONTENTS) == _cell(t, LOCATION, CONTENTS) == "No", \
        "the two rows no longer agree in the contents column"
    assert _cell(t, ENVELOPES, WARRANT) != _cell(t, LOCATION, WARRANT), \
        "the two rows no longer differ in the warrant column"
    return "envelopes and location agree on contents (No) and differ on warrant (No against Yes)"


def _both_sides(module):
    """LO 3.6.A puts both considerations on the scale; no key may remove one."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for phrase in ("public safety is not a legitimate",
                       "individual freedom is not a legitimate",
                       "public safety always outweighs",
                       "individual freedom always outweighs"):
            if phrase in key:
                bad.append(f"q{i} key: removes one side of LO 3.6.A's balance ({phrase!r})")
    if bad:
        print(f"FAIL {module.__name__} both sides")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} both sides: no key declares either individual freedom or "
          "public safety an illegitimate consideration")


def _no_position(module):
    """The framework calls these debates and resolves none; neither may a key."""
    bad = []
    contested = ("death penalty", "firearms regulation", "metadata collection",
                 "collection program")
    verdicts = ("is unconstitutional", "is constitutional", "is unjustified",
                "is justified", "should be abolished", "should be adopted")
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        if not any(c in key for c in contested):
            continue
        for v in verdicts:
            if v in key and "whether" not in key:
                bad.append(f"q{i} key: delivers a verdict on a contested measure ({v!r}); "
                           "EK 3.6.A.2 identifies these as debates and resolves none of them")
    if bad:
        print(f"FAIL {module.__name__} no position")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} no position: no key resolves any of the three debates the "
          "framework identifies as contested")


ua.shape(v3_6)
ua.check(v3_6, ANCHORS, GROUNDING)
ua.notation(v3_6)
_both_sides(v3_6)
_no_position(v3_6)
gc.check(v3_6, arith={22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27})

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. The design decision worth recording is the grid table, and it is
# the same kind of decision as v2_14's two-column monitoring table.
#
# EK 3.6.A.2 asks whether a measure "promotes or interferes with public safety
# AND individual rights". That is two independent questions, and a two-row table
# -- safety up, rights down -- would have illustrated the trade-off framing
# instead of the framework's own. The table therefore has four rows, one per
# combination, and the numbers are chosen so the interesting cell is populated:
# thirteen measures burdened rights WITHOUT promoting safety, against six that
# promoted safety without burdening rights.
#
# That cell is the one a trade-off framing has no place for, and item 16 asks a
# student to name it. q23 asserts all four combinations are present, so an edit
# that dropped a row would fail this file rather than quietly restoring the
# framing the topic exists to complicate.
#
# The second decision is _no_position. Three of this topic's subjects are live
# political controversies, and the framework's own word for them is DEBATE. A
# bank that resolved one would be asserting something the exam cannot ask and
# the CED does not say, while sounding authoritative. Every item here asks what
# the debate consists of, what would count as evidence in it, or what a required
# case held -- and the check makes that a property of the file rather than a
# habit of its author.
