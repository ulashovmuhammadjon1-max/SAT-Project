"""Structural gate for AP U.S. Government 3.8 Amendments: Due Process and the
Rights of the Accused.

gov345_check plus the four usgov_anchor helpers, plus two module-specific
checks. Both of those exist because this topic's essential knowledge is written
as RULE-THEN-EXCEPTION twice over, and both halves are droppable in a way
nothing structural would notice.

  _pairing   EK 3.8.A.1: "The due process clause in the Fifth Amendment applies
             to the national government and the due process clause in the
             Fourteenth Amendment applies to states." Items 1 to 5 turn on it
             and it is reversed constantly, including by people who know it.
             The check reads every key and every rationale and refuses any that
             pairs Fifth with the states or Fourteenth with the national
             government. A reversal here is a clean falsehood a student would
             carry into an FRQ, and it is invisible to an anchor, because a
             reversed key still matches its own anchor perfectly.
  _not_absolute
             EK 3.8.A.2 states the Miranda rule, then says "these procedural
             protections are NOT ABSOLUTE," then names the public safety
             exception. EK 3.8.A.4 states the exclusionary rule with two
             qualifiers inside its own sentence -- the evidence is barred
             AGAINST THAT SUSPECT and in CRIMINAL prosecution. Every one of
             those hedges makes a key narrower, so an edit that drops one makes
             the key MORE emphatic and reads as an improvement. The check
             asserts no key anywhere in the module states a procedural
             protection as absolute or the exclusionary rule as a general bar.

WHY THE TABLES ARE LABELLED HYPOTHETICAL
----------------------------------------
The CED states no exclusion rates, so real ones would be content the exam
cannot ask about wearing the authority of content it can. Both tables say
"hypothetical" in the stem and both teach a framework claim rather than a fact
about the world: the evidence table shows EK 3.8.A.2's NOT ABSOLUTE as the gap
between two warrantless rows, and the protections table shows it as a column.
"""
import gov345_check as gc
import usgov_anchor as ua
import v3_8

ANCHORS = {
 1: "The national government",
 2: "The states",
 3: "restrain different governments",
 4: "since the actor is a state government",
 5: "since the actor is the national government",
 6: "some government interests may justify restriction",
 7: "shown to present a danger to public safety",
 8: "depend on a demonstration rather than on an assertion",
 9: "methods that are not arbitrary",
 10: "still satisfy due process, provided the procedures used were not arbitrary",
 11: "key legal doctrines established by the Supreme Court",
 12: "prior to interrogation",
 13: "not absolute",
 14: "stand as direct evidence in court",
 15: "public safety exception permitting unwarned interrogation",
 16: "a bounded circumstance in which it does not apply",
 17: "not eclipsed by the need for social order and security",
 18: "a speedy and public trial, and an impartial jury",
 19: "warrantless searches of cell phone data",
 20: "Patriot and USA Freedom Acts",
 21: "against that suspect in criminal prosecution",
 22: "against THAT SUSPECT, and in CRIMINAL prosecution",
 23: "reinforces procedural due process",
 24: "without any exception claimed was excluded far more often",
 25: "a claimed public safety exception was admitted",
 26: "reflects lawful collection rather than a weak rule",
 27: "None of the four protections",
 28: "informs accused persons of protections found in the Fifth and Sixth Amendments",
 29: "substantial but not unlimited extent",
 30: "applying rules evenly rather than arbitrarily",
}

GROUNDING = {
 1: "U.S. Constitution, Fifth Amendment, quoted verbatim, read through EK 3.8.A.1: 'The due "
    "process clause in the Fifth Amendment applies to the national government.'",
 2: "EK 3.8.A.1's second half: 'the due process clause in the Fourteenth Amendment applies to "
    "states.' The same clause is the vehicle for selective incorporation in EK 3.7.A.1.",
 3: "EK 3.8.A.1's two assignments read together: a guarantee written against one government "
    "does not by itself reach another, which is why the Constitution needs both clauses.",
 4: "EK 3.8.A.1 applied to a state actor. The assignment turns on WHOSE action is challenged, "
    "not on the subject matter, so criminal procedure does not move the case to the Fifth.",
 5: "EK 3.8.A.1 applied to the national government acting through an agency. Property is named "
    "in both clauses and so cannot be what distinguishes them.",
 6: "EK 3.8.A.1's own hedge: 'Some government interests may justify the restriction of "
    "individual rights.' It is the reason LO 3.8.A asks about THE EXTENT of the limitation.",
 7: "EK 3.8.A.1's own example, verbatim: 'speech can be limited when it is shown to present a "
    "danger to public safety.' It connects this topic to the speech categories of 3.3.",
 8: "EK 3.8.A.1's word SHOWN, read for what it does: it places a burden of demonstration on the "
    "government, which is the difference between a bounded exception and a general licence.",
 9: "EK 3.8.A.2, verbatim: procedural due process 'requires that government officials use "
    "methods that are not arbitrary when making and carrying out decisions affecting "
    "constitutionally protected rights.'",
 10: "EK 3.8.A.2 read for its object: the requirement runs to METHODS, so an adverse outcome "
     "reached by non-arbitrary methods satisfies it. Reading it as a guarantee of results is "
     "the standard misunderstanding of the phrase PROCEDURAL due process.",
 11: "EK 3.8.A.2, verbatim: the protections 'are reinforced by key protections enshrined in "
     "other provisions of the Bill of Rights and key legal doctrines established by the "
     "Supreme Court.' The Miranda and exclusionary rules are its examples of the second.",
 12: "EK 3.8.A.2, verbatim: the Miranda rule 'requires accused persons to be informed of some "
     "procedural protections found in the Fifth and Sixth Amendments prior to interrogation.'",
 13: "EK 3.8.A.2's next sentence, verbatim: 'However, these procedural protections are not "
     "absolute.' A module that stopped at the rule would teach half the framework's statement.",
 14: "EK 3.8.A.2, verbatim: 'A public safety exception has been sanctioned by the Court that "
     "allows unwarned interrogation to stand as direct evidence in court.'",
 15: "EK 3.8.A.2's exception applied to the situation it is written about. The framework's word "
     "SANCTIONED BY THE COURT makes it a recognized exception, not a lapse in enforcement.",
 16: "EK 3.8.A.2's three-sentence structure -- rule, then 'not absolute,' then the named "
     "exception -- which is the shape of a requirement with a bounded carve-out.",
 17: "EK 3.8.A.3, verbatim: procedural rights and the prohibition of unreasonable searches are "
     "'intended to ensure that individual liberties are not eclipsed by the need for social "
     "order and security.' The verb ECLIPSED is the framework's own.",
 18: "EK 3.8.A.3.i, verbatim: 'The right to legal counsel, speedy and public trial, and an "
     "impartial jury.' The other options name entitlements the framework does not list.",
 19: "EK 3.8.A.3.ii, verbatim: 'Protection against warrantless searches of cell phone data "
     "under the Fourth Amendment.' Excessive bail is the Eighth Amendment and topic 3.6.",
 20: "EK 3.8.A.3.iii's own parenthesis: '(Patriot and USA Freedom Acts).' Naming them in the "
     "framework makes them course content rather than illustration.",
 21: "EK 3.8.A.4, verbatim: the exclusionary rule 'stipulates that evidence illegally seized by "
     "law enforcement officers in violation of the suspect's Fourth Amendment rights... cannot "
     "be used against that suspect in criminal prosecution.'",
 22: "EK 3.8.A.4's two qualifiers, both inside the framework's own sentence: AGAINST THAT "
     "SUSPECT and in CRIMINAL prosecution. Reading the rule as a general bar overstates it.",
 23: "Gideon v. Wainwright (1963), required case, which the CED attaches to 3.8.A. CED holding: "
     "the Sixth Amendment right to an attorney 'extends procedural due process protections to "
     "felony defendants in state courts' -- EK 3.8.A.2's reinforcement relationship exactly.",
 24: "Data item, CED skill 5.C. Every rate is recomputed from the table below.",
 25: "Data item illustrating EK 3.8.A.2's NOT ABSOLUTE: the two warrantless rows differ only in "
     "whether the exception was claimed. Both rows' rates are recomputed below.",
 26: "Data item, CED skill 5.C: an aggregate rate driven by its denominator. Recomputed below.",
 27: "Data item on EK 3.8.A.2's sentence that the procedural protections are not absolute; the "
     "column is recomputed below.",
 28: "EK 3.8.A.2's own pairing for the Miranda rule -- 'the Fifth and Sixth Amendments' -- "
     "located in the table as the only row naming two. Recomputed below.",
 29: "LO 3.8.A's phrase THE EXTENT TO WHICH, read against a column of four No answers. EK "
     "3.8.A.3's verb is that liberties are not ECLIPSED, which concedes they may be weighed.",
 30: "'Letter from a Birmingham Jail' (required document), quoted verbatim; the CED attaches "
     "the Letter to 3.8.A. Its test for an unjust law is uneven application, and EK 3.8.A.2's "
     "requirement is methods that are NOT ARBITRARY -- the same idea at two levels.",
}

OFFERED, EXCLUDED = "Times offered", "Times excluded"
HOW = "How the evidence was obtained"
PROT, AMEND = "Protection", "Amendment it rests on"
ABSOLUTE = "Described by the framework as absolute?"


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def _rates(t):
    """Exclusion rate per row, keyed by the row label."""
    return {row[0]: gc.pct(gc.num(row[2]), gc.num(row[1]))
            for row in t["rows"]}


def _row(t, needle):
    """The one row whose label contains the needle."""
    hits = [r for r in t["rows"] if needle in r[0]]
    assert len(hits) == 1, f"{needle!r} matches {len(hits)} rows, not one"
    return hits[0]


def q24(t):
    """The no-exception row is excluded far more often; volunteered is not the top rate."""
    rates = _rates(t)
    warrant = rates["Under a warrant supported by probable cause"]
    noexc = rates["Without a warrant, no exception claimed"]
    vol = rates["Volunteered by the suspect before questioning began"]
    assert noexc > 10 * warrant, \
        f"the no-exception rate {noexc} is not far above the warrant rate {warrant}"
    assert vol < max(rates.values()), \
        "volunteered statements are the most excluded category, which the key denies"
    return (f"exclusion rates: warrant {warrant} percent, no exception {noexc} percent, "
            f"volunteered {vol} percent")


def q25(t):
    """The two warrantless rows flip the majority when the exception is claimed."""
    noexc = _row(t, "no exception claimed")
    exc = _row(t, "public safety exception claimed")
    n_off, n_ex = gc.num(noexc[1]), gc.num(noexc[2])
    e_off, e_ex = gc.num(exc[1]), gc.num(exc[2])
    assert n_ex > n_off / 2, \
        f"the no-exception row does not mostly exclude: {n_ex:.0f} of {n_off:.0f}"
    assert e_off - e_ex > e_off / 2, \
        f"the exception row does not mostly admit: {e_off - e_ex:.0f} of {e_off:.0f} admitted"
    return (f"no exception claimed: {n_ex:.0f} of {n_off:.0f} excluded "
            f"({gc.pct(n_ex, n_off)} percent); exception claimed: "
            f"{e_off - e_ex:.0f} of {e_off:.0f} admitted "
            f"({gc.pct(e_off - e_ex, e_off)} percent)")


def q26(t):
    """The warrant row is a majority of the denominator, which is what drags the rate down."""
    offered = [gc.num(c) for c in _col(t, OFFERED)]
    excluded = [gc.num(c) for c in _col(t, EXCLUDED)]
    warrant = _row(t, "Under a warrant")
    total = sum(offered)
    assert gc.num(warrant[1]) > total / 2, \
        f"the warrant row is {gc.num(warrant[1]):.0f} of {total:.0f}, not a majority"
    overall = gc.pct(sum(excluded), total)
    noexc = _row(t, "no exception claimed")
    strong = gc.pct(gc.num(noexc[2]), gc.num(noexc[1]))
    assert strong > 4 * overall, \
        "the row where the rule bites is not far above the aggregate, so the correction fails"
    return (f"warrant row is {gc.num(warrant[1]):.0f} of {total:.0f} offered "
            f"({gc.pct(gc.num(warrant[1]), total)} percent); aggregate exclusion {overall} "
            f"percent against {strong} percent in the no-exception row")


def q27(t):
    """Every row's last column says No, and there are four rows."""
    col = [c.strip().lower() for c in _col(t, ABSOLUTE)]
    assert len(t["rows"]) == 4, f"{len(t['rows'])} rows, not four"
    assert set(col) == {"no"}, f"the absolute column is not uniformly No: {col}"
    return f"four protections, and the absolute column reads {', '.join(col)}"


def q28(t):
    """Exactly one row rests on two amendments, and it is the Miranda row."""
    two = [r[0] for r in t["rows"] if " and " in r[t["headers"].index(AMEND)]]
    assert len(two) == 1, f"{len(two)} rows name two amendments: {two}"
    assert "Miranda" in two[0], f"the two-amendment row is {two[0]!r}, not the Miranda row"
    amend = _row(t, "Miranda")[t["headers"].index(AMEND)]
    assert "Fifth" in amend and "Sixth" in amend, f"the Miranda row names {amend!r}"
    return f"one row of four names two amendments -- {two[0]!r} resting on {amend!r}"


def q29(t):
    """The column is uniform, and every protection in it is a real protection."""
    col = [c.strip().lower() for c in _col(t, ABSOLUTE)]
    assert len(set(col)) == 1, f"the column is not uniform: {col}"
    assert col[0] == "no", f"the uniform answer is {col[0]!r}, not No"
    names = _col(t, PROT)
    assert len(set(names)) == len(names), f"a protection is listed twice: {names}"
    return (f"{len(names)} distinct protections, every one answered No -- limitation that is "
            "substantial and not unlimited, which is what EXTENT asks")


# --- module-specific content gates -------------------------------------------
# Neither of these can check the politics. Each pins one sentence of the CED
# that a plausible edit would quietly reverse or soften.

def _pairing(module):
    """Fifth to the national government, Fourteenth to the states. Never reversed."""
    bad = []
    reversals = (
        ("fifth amendment", ("applies to states", "applies to the states",
                             "since the actor is a state")),
        ("fourteenth amendment", ("applies to the national government",
                                  "since the actor is the national government")),
    )
    for i, item in enumerate(module.QUESTIONS, 1):
        for label, s in (("key", item["choices"][item["ans"]]), ("why", item["why"])):
            low = s.lower()
            for amendment, wrong_tails in reversals:
                if amendment not in low:
                    continue
                for tail in wrong_tails:
                    if tail not in low:
                        continue
                    # Only a hit when the wrong tail follows the amendment name
                    # closely enough to be its predicate; the two clauses are
                    # named in one sentence all over this module.
                    gap = low.index(tail) - (low.index(amendment) + len(amendment))
                    if 0 <= gap <= 30:
                        bad.append(
                            f"q{i} {label}: pairs {amendment!r} with {tail!r}; EK 3.8.A.1 "
                            "assigns the Fifth to the national government and the "
                            "Fourteenth to the states")
    q1, q2 = module.QUESTIONS[0], module.QUESTIONS[1]
    if "national government" not in q1["choices"][q1["ans"]].lower():
        bad.append("q1: the Fifth Amendment's clause is no longer keyed to the national "
                   "government")
    if "states" not in q2["choices"][q2["ans"]].lower():
        bad.append("q2: the Fourteenth Amendment's clause is no longer keyed to the states")
    if bad:
        print(f"FAIL {module.__name__} pairing")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} pairing: no key or rationale reverses EK 3.8.A.1's "
          "assignment of the Fifth Amendment to the national government and the Fourteenth "
          "to the states")


def _not_absolute(module):
    """No key may state a procedural protection as absolute, or the rule as a general bar."""
    bad = []
    absolutes = (
        "protections are absolute",
        "protections are always",
        "warnings are absolute",
        "may never be limited",
        "individual rights are absolute",
        "in any proceeding against anyone",
        "in every proceeding",
        "regardless of how it was obtained",
    )
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for phrase in absolutes:
            if phrase in key:
                bad.append(f"q{i} key: states {phrase!r}; EK 3.8.A.2 says 'these procedural "
                           "protections are not absolute' and EK 3.8.A.4 bars the evidence "
                           "only against that suspect in criminal prosecution")
    q13 = module.QUESTIONS[12]
    if "not absolute" not in q13["choices"][q13["ans"]].lower():
        bad.append("q13: the key no longer carries EK 3.8.A.2's sentence that the procedural "
                   "protections are not absolute")
    q22 = module.QUESTIONS[21]
    k22 = q22["choices"][q22["ans"]].lower()
    if "that suspect" not in k22 or "criminal" not in k22:
        bad.append("q22: the key no longer carries both of EK 3.8.A.4's qualifiers, AGAINST "
                   "THAT SUSPECT and in CRIMINAL prosecution")
    if bad:
        print(f"FAIL {module.__name__} not absolute")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} not absolute: no key states a procedural protection as "
          "absolute or the exclusionary rule as a general bar, and both of EK 3.8.A.4's "
          "qualifiers survive")


ua.shape(v3_8)
ua.check(v3_8, ANCHORS, GROUNDING)
ua.notation(v3_8)
_pairing(v3_8)
_not_absolute(v3_8)
gc.check(v3_8, arith={24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29})

# WHAT THE REVIEW FOUND
# ---------------------
# This module was left in flight by a stopped agent, was repaired to parse, and
# had never had its CONTENT read. Reading all thirty against the CED found two
# defects, both in data items, both fixed in v3_8.py:
#
#   q24, in the RATIONALE. It said volunteered statements were excluded at "the
#   lowest rate in the table." They are not: 4 of 210 is 1.9 percent, and
#   evidence taken under a warrant is 9 of 820, 1.1 percent. The keyed choice
#   was true and the distractor it was refuting was false, so nothing structural
#   would ever have caught this -- it is a wrong sentence sitting in the text a
#   student reads after answering. Rewritten to say what the numbers support.
#
#   q25, in the KEY. It said a claimed public safety exception "changed the
#   outcome in most of those cases." The exclusion rate falls from 84.3 percent
#   to 32.8 percent between the two warrantless rows, which is a gap of about 51
#   points -- so roughly half, not most, and the sentence was arguing from a
#   difference of rates as though it were a count of cases. The key now states
#   what the table actually shows: most warrantless evidence with no exception
#   claimed was excluded, and most of the evidence under a claimed exception was
#   admitted. Both halves are recomputed by q25 above, which is why the check
#   asserts the MAJORITY flips rather than asserting a rate.
#
# No wrong answer key was found. Every other item traces to a CED sentence, and
# the two quotations -- the Fifth Amendment in item 1 and the "Letter from a
# Birmingham Jail" in item 30 -- are verbatim. The CED attaches both Gideon
# (item 23) and the Letter to 3.8.A, checked against the cross-reference tables.
