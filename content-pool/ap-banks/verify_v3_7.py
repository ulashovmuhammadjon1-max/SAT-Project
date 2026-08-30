"""Structural gate for AP U.S. Government 3.7 Selective Incorporation.

gov345_check plus the four usgov_anchor helpers.

ONE SENTENCE WITH FOUR PARTS, AND A STUDENT NEEDS ALL FOUR
------------------------------------------------------------
EK 3.7.A.1 says the doctrine "has imposed limitations on state regulation of
civil liberties by extending SELECT protections of the Bill of Rights to the
states through the DUE PROCESS CLAUSE of the Fourteenth Amendment." What, which,
to whom, how. Two of the four are guarded here because each is dropped in a
predictable way:

  _select    The adjective is in the doctrine's NAME and is the first thing a
             paraphrase loses. "The Bill of Rights applies to the states" is the
             standard formulation and it is wrong -- selective incorporation is
             precisely the doctrine under which some guarantees do and some do
             not. Item 7 makes the correction the question and this check
             asserts no key states the totalizing version.
  _due_process
             The route is the Fourteenth Amendment's due process clause. The
             Supremacy Clause is the plausible wrong answer, because it is the
             provision students associate with federal law binding states, and
             it is a distractor in item 2 for that reason. No key may name it,
             or the Tenth Amendment, or the Commerce Clause as the vehicle.

WHAT THE MODULE DELIBERATELY DOES NOT CONTAIN
-----------------------------------------------
A roster of which guarantees have been incorporated and which have not. The
framework says SELECT and names none, so a list assembled from outside the CED
would be examinable nowhere. Every specific guarantee that appears here arrives
through a required case holding the CED itself states -- Engel's Establishment
Clause, Gideon's Sixth Amendment counsel, Yoder's Free Exercise, McDonald's
Second Amendment. The timeline table is deliberately abstract for the same
reason: it counts guarantees in a hypothetical system rather than naming real
ones, which lets item 25 make the GAP the lesson without asserting a roster.
"""
import gov345_check as gc
import usgov_anchor as ua
import v3_7

ANCHORS = {
 1: "extending select protections of the Bill of Rights to the states",
 2: "The due process clause of the Fourteenth Amendment",
 3: "It restrains the states by name and protects liberty",
 4: "so it supplied no federal constitutional remedy",
 5: "Some protections of the Bill of Rights have been extended to the states and others have not",
 6: "extends guarantees one at a time",
 7: "the claim is true of many guarantees and not of all of them",
 8: "A guarantee extended to the states is a restriction on what a state may do",
 9: "because local governments are created by and exercise the authority of the states",
 10: "was extended to state proceedings through due process",
 11: "A public school district is a state instrumentality",
 12: "since compulsory attendance laws are state laws",
 13: "Applicable to the states",
 14: "a guarantee from the Bill of Rights was applied against a state",
 15: "no authority over how a state treated its own residents",
 16: "possible only because guarantees run against the states",
 17: "incorporation sets a minimum rather than a maximum",
 18: "State governments lost the power to legislate on subjects the Bill of Rights mentions",
 19: "so the doctrine grew as cases arose",
 20: "regardless of the original text's wording",
 21: "and each applied a different guarantee",
 22: "McDonald v. Chicago, in which the action challenged was a city's",
 23: "have been extended separately",
 24: "while the number binding the national government did not change",
 25: "without binding subnational ones",
 26: "since each requires a case raising it",
 27: "the institutional form of the idea that injustice in one place is a national concern",
 28: "Has the Supreme Court held that this guarantee applies to state or local government",
 29: "through the Fourteenth Amendment's due process clause, limiting state regulation",
 30: "reach every civil liberties question involving a state or local government",
}

GROUNDING = {
 1: "EK 3.7.A.1, verbatim, including the adjective SELECT that the doctrine is named for.",
 2: "EK 3.7.A.1's named route: 'through the due process clause of the Fourteenth Amendment.'",
 3: "U.S. Constitution, Fourteenth Amendment Section 1, quoted verbatim. Its subject is 'No "
    "State' and its object is liberty, which is what makes it the vehicle.",
 4: "EK 3.7.A.1's verb EXTENDING, read backwards: a protection extended to the states did not "
    "reach them before. LO 3.7.A's implication.",
 5: "EK 3.7.A.1's word SELECT: the selection is among GUARANTEES, not among states or years.",
 6: "EK 3.7.A.1's selective doctrine against the totalizing alternative it is named against.",
 7: "EK 3.7.A.1 read precisely: dropping the adjective is the standard error, and the standard "
    "formulation 'the Bill of Rights applies to the states' contains it.",
 8: "EK 3.7.A.1's phrase 'imposed limitations on state regulation of civil liberties' -- a "
    "guarantee is a limit on government, and incorporation adds a government it limits.",
 9: "McDonald v. Chicago (2010), required case, which the CED attaches to 3.7.A: the challenged "
    "action was a CITY's, which is how the framework's own holdings answer this.",
 10: "Gideon v. Wainwright (1963), required case, which the CED attaches to 3.7.A. CED holding: "
     "the Sixth Amendment right to an attorney 'extends procedural due process protections to "
     "felony defendants in state courts' -- EK 3.7.A.1's mechanism inside the holding.",
 11: "Engel v. Vitale (1962), required case, which the CED attaches to 3.7.A. The First "
     "Amendment's text restrains Congress, so reaching a school district requires extension.",
 12: "Wisconsin v. Yoder (1972), required case, which the CED attaches to 3.7.A. Compulsory "
     "attendance is STATE law, which is why the case needs incorporation.",
 13: "McDonald v. Chicago (2010): 'applicable to the states' is the phrase that answers the "
     "incorporation question; 'for self-defense' names the purpose instead.",
 14: "The four required cases the CED attaches to 3.7.A, involving a school district, a state "
     "court, a state and a city, and four different guarantees.",
 15: "Articles of Confederation (required document), Article II, quoted verbatim; the CED "
     "attaches the Articles to 3.7.A. The union reached nothing a state did internally, which "
     "is the condition the Fourteenth Amendment reversed. EK 1.4.A.1 adds the missing courts.",
 16: "LO 3.7.A's IMPLICATIONS: state and local governments make most of the decisions touching "
     "individuals, so which governments a guarantee binds determines how much it does.",
 17: "EK 3.7.A.1's 'limitations on state regulation' read as a floor: a state may protect more, "
     "and nothing in the doctrine stops it.",
 18: "EK 3.7.A.1 tested by exclusion: a limit on HOW a state may regulate is not a removal of "
     "the power to regulate. The other four options follow directly from the statement.",
 19: "EK 3.7.A.1's SELECTIVE character explained: courts decide the cases before them, so a "
     "doctrine built through litigation extends only what a case puts in issue.",
 20: "EK 3.7.A.1's mechanism: the original text's audience does not settle the question once a "
     "guarantee has been extended. The conditional matters, because incorporation is selective.",
 21: "Data item on the four required cases; the columns are recomputed below.",
 22: "McDonald located in the table as the row naming a city.",
 23: "EK 3.7.A.1's SELECT shown as data: four cases, four guarantees, four decades.",
 24: "Data item on a labelled hypothetical; both columns' behaviour is recomputed below.",
 25: "EK 3.7.A.1's selective half shown as a gap: seventeen against twenty-four.",
 26: "Data item, CED skill 3.E: extrapolating a doctrinal series assumes the remaining "
     "guarantees are like the extended ones, which nothing in the table supports.",
 27: "'Letter from a Birmingham Jail' (required document), quoted verbatim; the CED attaches "
     "the Letter to 3.7.A. A guarantee binding only the national government leaves a state's "
     "treatment of a person a purely local matter.",
 28: "EK 3.7.A.1 operationalized: incorporation is extension BY THE COURT through due process, "
     "so the test is whether a holding has done it.",
 29: "EK 3.7.A.1's four parts restated in order: which protections, to whom, by what route, "
     "with what effect.",
 30: "LO 3.7.A's word IMPLICATIONS, and the reason it is the right word: scope.",
}

WHOSE, GUARANTEE = "Whose action was challenged", "Guarantee applied"
NAT_COL = "Guarantees enforceable against the national government"
SUB_COL = "Guarantees enforceable against subnational governments"


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def q21(t):
    """No row challenges national action, and every row applies a different guarantee."""
    whose = _col(t, WHOSE)
    assert not any("national" in w.lower() or "congress" in w.lower() for w in whose), \
        f"a row challenges national action: {whose}"
    assert len(set(_col(t, GUARANTEE))) == 4, "two rows apply the same guarantee"
    assert len(t["rows"]) == 4, f"{len(t['rows'])} rows, not four"
    return f"four cases, four different guarantees, none challenging national action: {whose}"


def q22(t):
    """Exactly one row names a city, which is the local-government row."""
    whose = _col(t, WHOSE)
    cities = [r[0] for r, w in zip(t["rows"], whose) if "city" in w.lower()]
    assert cities == ["McDonald v. Chicago (2010)"], f"the city rows are {cities}"
    return "one row names a city, and it is McDonald"


def q23(t):
    """Guarantees come from different amendments, which is what SELECT means."""
    guarantees = _col(t, GUARANTEE)
    amendments = {g.split("Amendment")[0].strip().split()[-1] for g in guarantees}
    assert len(amendments) >= 3, f"the guarantees come from too few amendments: {amendments}"
    return f"guarantees drawn from {len(amendments)} different amendments across four decades"


def q24(t):
    """The national column is constant; the subnational column grows."""
    nat, sub = [gc.num(c) for c in _col(t, NAT_COL)], [gc.num(c) for c in _col(t, SUB_COL)]
    assert len(set(nat)) == 1, f"the national column changes: {nat}"
    assert sub == sorted(sub) and len(set(sub)) == len(sub), f"the subnational column is {sub}"
    assert sub[0] == 0, "the subnational column does not start at zero"
    return f"national constant at {nat[0]:.0f}; subnational {', '.join(f'{s:.0f}' for s in sub)}"


def q25(t):
    """The final gap is what makes the incorporation selective rather than total."""
    nat = gc.num(_col(t, NAT_COL)[-1])
    sub = gc.num(_col(t, SUB_COL)[-1])
    assert sub < nat, "the subnational column has caught the national column, removing the gap"
    return (f"final period: {sub:.0f} of {nat:.0f} guarantees bind subnational governments, "
            f"leaving {nat - sub:.0f} that do not")


def q26(t):
    """Four periods and both columns are present; the series is a trend, not a projection."""
    assert len(t["rows"]) == 4, f"{len(t['rows'])} periods"
    assert NAT_COL in t["headers"] and SUB_COL in t["headers"], "a column is missing"
    sub = [gc.num(c) for c in _col(t, SUB_COL)]
    gains = [b - a for a, b in zip(sub, sub[1:])]
    assert len(set(gains)) > 1, \
        "the gains are uniform, which would make linear extrapolation harder to argue against"
    return f"subnational gains of {', '.join(f'{g:.0f}' for g in gains)} -- uneven, not a rate"


def _select(module):
    """The doctrine's own adjective must survive; no key may totalize it."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for phrase in ("every protection of the bill of rights",
                       "all protections of the bill of rights",
                       "the entire bill of rights applies to the states",
                       "incorporation is complete"):
            if phrase in key:
                bad.append(f"q{i} key: states the totalizing version ({phrase!r}); the "
                           "doctrine is named SELECTIVE and EK 3.7.A.1 says SELECT protections")
    q1 = module.QUESTIONS[0]
    if "select protections" not in q1["choices"][q1["ans"]].lower():
        bad.append("q1: the keyed statement of EK 3.7.A.1 no longer carries the word SELECT")
    if bad:
        print(f"FAIL {module.__name__} select")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} select: EK 3.7.A.1's adjective survives in the defining key "
          "and no key states the totalizing version")


def _due_process(module):
    """The route is the Fourteenth Amendment's due process clause and nothing else."""
    bad = []
    wrong = ("supremacy clause", "necessary and proper clause", "tenth amendment",
             "commerce clause")
    for i, item in enumerate(module.QUESTIONS, 1):
        for label, s in (("key", item["choices"][item["ans"]]), ("why", item["why"])):
            low = s.lower()
            if "incorporat" not in low and "extend" not in low:
                continue
            for w in wrong:
                if w in low and "not " not in low and "rather than" not in low:
                    bad.append(f"q{i} {label}: names the {w} in an incorporation claim; "
                               "EK 3.7.A.1's route is the due process clause of the "
                               "Fourteenth Amendment")
    q2 = module.QUESTIONS[1]
    if "due process clause of the fourteenth amendment" not in q2["choices"][q2["ans"]].lower():
        bad.append("q2: the keyed route is no longer the due process clause of the Fourteenth "
                   "Amendment")
    if bad:
        print(f"FAIL {module.__name__} due process")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} due process: no key or rationale routes incorporation through "
          "the Supremacy Clause, the Tenth Amendment or any provision but the Fourteenth "
          "Amendment's due process clause")


ua.shape(v3_7)
ua.check(v3_7, ANCHORS, GROUNDING)
ua.notation(v3_7)
_select(v3_7)
_due_process(v3_7)
gc.check(v3_7, arith={21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26})

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. Two decisions recorded because both are refusals.
#
# First, the module contains no roster of incorporated and unincorporated
# guarantees. That list is the most natural thing to want here and the framework
# supplies none -- EK 3.7.A.1 says SELECT and stops. A roster assembled from
# outside the CED would be content the exam cannot ask about, presented with the
# same authority as content it can. So every specific guarantee in this module
# arrives through a required case holding the CED itself states, and the
# timeline table counts guarantees in a hypothetical system rather than naming
# real ones. That is what lets item 25 teach the GAP -- seventeen of
# twenty-four -- which is the doctrine's selective half, without asserting which
# seven.
#
# Second, _due_process exists because the Supremacy Clause is the wrong answer a
# well-prepared student reaches for. It IS the provision that makes federal law
# bind states, and it is not the route for incorporation; EK 3.7.A.1 names the
# Fourteenth Amendment's due process clause. A distractor in item 2 offers it
# deliberately, and the check makes sure no key or rationale anywhere in the
# module quietly agrees with the distractor.
