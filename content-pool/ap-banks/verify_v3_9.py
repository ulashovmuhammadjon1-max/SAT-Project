"""Structural gate for AP U.S. Government 3.9 Amendments: Due Process and the
Right to Privacy.

gov345_check plus the four usgov_anchor helpers, plus two content gates.

WHY THESE TWO GATES AND NOT OTHERS
----------------------------------
3.8 and 3.9 have nearly the same title and adjacent numbers, and the whole
reason they are separate topics is one word. Everything that can go wrong here
goes wrong in one of two ways.

  _substantive  EK 3.9.A.1 aims substantive due process at whether "government
                laws and ACTIONS are arbitrary infringements of individual
                rights"; EK 3.8.A.2 aims procedural due process at whether the
                METHODS officials used were arbitrary. Collapsing the two is the
                error this topic exists to prevent, and it is not visible to an
                anchor, because a key that describes the wrong doctrine still
                sits in its own choice and still matches its own substring. The
                check reads every key that claims to define one of the two and
                refuses any that gives it the other's object.

  _holdings     EK 3.9.A.2 states three holdings, and each has a shape that a
                paraphrase flattens in a predictable direction:
                  Griswold  INTERPRETED the due process clause to protect
                            privacy -- it did not find privacy written down.
                  Roe       EXTENDED the privacy right to abortion -- a
                            continuation, not a new doctrine.
                  Dobbs     held the Constitution DOES NOT CONFER a right to
                            abortion and left regulation TO LEGISLATURES. The
                            two flattenings are turning "does not confer" into
                            "forbids" or "requires", and sending the question
                            anywhere but a legislature.
                The check pins each of the three to the framework's own verb and
                refuses any key that states a stronger holding than the CED
                does. This matters more here than anywhere else in the unit,
                because these three are the questions a student is most likely
                to already have an opinion about, and a bank that quietly
                overstates one is teaching that opinion as law.

WHAT THE MODULE DELIBERATELY DOES NOT ASSERT
--------------------------------------------
Three gaps in the framework are left as gaps. It does not say what Dobbs did to
Griswold; it names no test for which unenumerated rights survive; and it does
not choose between the two arguments for unenumerated rights, since its own
verbs are "some argue" and "others argue". Item 18 makes the first gap the
question and item 4 makes the third one the question, which is the only honest
way to examine a place where the framework records a debate instead of an
answer. No key fills any of the three.
"""
import gov345_check as gc
import usgov_anchor as ua
import v3_9

ANCHORS = {
 1: "beyond those listed in the first eight amendments",
 2: "not explicitly listed in the Bill of Rights",
 3: "The right to privacy",
 4: "implied by certain amendments which assume it exists",
 5: "written as though the right already exists",
 6: "recognized constitutionally protected rights",
 7: "arbitrary infringements of individual rights",
 8: "while procedural due process asks whether the methods officials used were arbitrary",
 9: "the objection is to what the law does rather than to how it was made",
 10: "the objection is to the methods used rather than to the agency's power",
 11: "is not rescued by being applied through fair procedures",
 12: "continue to be debated",
 13: "Interpreted the due process clause to protect the right of privacy",
 14: "locate it by interpretation rather than by reading a clause aloud",
 15: "further extended the privacy right to abortion",
 16: "does not confer a right to abortion, leaving decisions about the regulation",
 17: "Legislatures",
 18: "and it separately says the protected actions continue to be debated",
 19: "actions protected by the right to privacy and substantive due process",
 20: "asks whether a protected private choice is invaded",
 21: "arbitrarily invades a protected private sphere under the due process clause",
 22: "attaches it to a range of cases rather than to abortion alone",
 23: "Which actions the right to privacy and substantive due process protect",
 24: "brought more than twice as often as challenges argued on substantive grounds",
 25: "whether a government law or action is an arbitrary infringement",
 26: "so they are a minority of the total",
 27: "differ most is also the decision with the least support among all adults",
 28: "close to an even split and divides the two age groups more sharply",
 29: "a spread of 36 percentage points",
 30: "with the list of protected actions still contested",
}

GROUNDING = {
 1: "U.S. Constitution, Ninth Amendment, quoted verbatim, read through EK 3.9.A.1's own gloss: "
    "it 'states that individuals have protected rights beyond those listed in the first eight "
    "amendments' and supports the existence of unenumerated rights.",
 2: "EK 3.9.A.1, verbatim: the Court 'has recognized constitutionally protected rights that are "
    "not explicitly listed in the Bill of Rights. These unenumerated rights...' The definition "
    "turns on absence from the text, not on the strength of the protection.",
 3: "EK 3.9.A.1, verbatim: 'These unenumerated rights include the right to privacy.' The four "
    "distractors are each written into the text of an amendment, so each is enumerated.",
 4: "EK 3.9.A.1's two recorded arguments: implication from 'certain amendments that assume the "
    "existence of such rights', and the Ninth Amendment. The framework's verbs are 'some argue' "
    "and 'others argue', so it records the debate without settling it.",
 5: "EK 3.9.A.1's word ASSUME: the argument is about what the text presupposes, which is why it "
    "does not require the right to be written anywhere.",
 6: "EK 3.9.A.1's opening sentence, which is the premise of the whole topic. The four "
    "distractors are all EK statements from topic 3.8 and concern procedure.",
 7: "EK 3.9.A.1, verbatim: 'the Supreme Court has used substantive due process to examine "
    "whether government laws and actions are arbitrary infringements of individual rights.'",
 8: "EK 3.9.A.1 against EK 3.8.A.2: the substantive examination runs to the law or action, the "
    "procedural one to the methods. Both due process clauses bind both governments (EK "
    "3.8.A.1), so which government acts cannot be the distinction.",
 9: "EK 3.9.A.1 applied to a challenge that concedes the procedure and attacks the content, "
    "which is the substantive examination by definition.",
 10: "EK 3.8.A.2 applied to a challenge that concedes the power and attacks the absence of "
     "notice and a hearing, which is a complaint about method.",
 11: "EK 3.9.A.1 and EK 3.8.A.2 read as independent tests. Passing one says nothing about the "
     "other, which is why the framework gives them separate topics with nearly identical names.",
 12: "LO 3.9.A's phrase THE EXTENT TO WHICH, read against EK 3.9.A.2's closing sentence: 'The "
     "actions that are protected by the right to privacy and substantive due process continue "
     "to be debated.' A contested boundary is measured by extent, not by whether.",
 13: "EK 3.9.A.2, verbatim: in Griswold v. Connecticut (1965) the Court 'interpreted the due "
     "process clause to protect the right of privacy from government infringement.'",
 14: "EK 3.9.A.2's own preface, 'while a right to privacy is not explicitly named in the "
     "Constitution', read against EK 3.9.A.1's definition of an unenumerated right.",
 15: "EK 3.9.A.2, verbatim: in Roe v. Wade (1973) 'the application of substantive due process "
     "further extended the privacy right to abortion.' The verb EXTENDED places Roe as a "
     "continuation of Griswold rather than a fresh doctrine.",
 16: "EK 3.9.A.2, verbatim: Dobbs (2022) 'overturned Roe v. Wade, holding that the Constitution "
     "does not confer a right to abortion, leaving decisions about the regulation of abortion "
     "to legislatures.' Not conferring a right is not forbidding or requiring the practice.",
 17: "EK 3.9.A.2's own destination for the question after Dobbs: legislatures. Where a "
     "constitutional right is held not to exist, the matter returns to ordinary lawmaking.",
 18: "EK 3.9.A.2 read for what it does NOT say. Its Dobbs sentence names Roe and the abortion "
     "right and stops, and its closing sentence keeps the scope of privacy open.",
 19: "EK 3.9.A.2's three decisions in sequence, closing with 'continue to be debated' -- the "
     "framework's own illustration of an unsettled boundary.",
 20: "Brown v. Board of Education (1954), required case, which the CED attaches to 3.9.A (p. "
     "31). CED holding: race-based school segregation violates the EQUAL PROTECTION clause. "
     "Griswold rests on the DUE PROCESS clause; both clauses sit in Fourteenth Amendment "
     "Section 1, so naming the amendment does not distinguish them.",
 21: "CED skill 2.C, comparing a non-required case to a framework-named one on its THEORY. The "
     "stem's challenge attacks a law's substance under due process, which is EK 3.9.A.1's "
     "examination and the Griswold theory. McDonald concerns the Second Amendment, enumerated.",
 22: "EK 3.9.A.1's scope: substantive due process is described as used 'in a range of cases', "
     "in the present tense, and is not confined to any one right.",
 23: "EK 3.9.A.2's final sentence, which is the one thing in this topic the framework marks as "
     "open. The four distractors are each stated flatly somewhere in the framework.",
 24: "Data item, CED skill 1.A. Both counts and the ratio are recomputed below.",
 25: "EK 3.9.A.1's definition of the substantive examination, located as a row of the table. "
     "The distractors describe method, which EK 3.8.A.2 assigns to procedural due process.",
 26: "Data item: a share of a denominator the student did not add up. Recomputed below.",
 27: "Data item, CED skill 1.A. Every gap and every column extreme is recomputed below.",
 28: "Data item carrying EK 3.9.A.2's closing sentence: a debate appears in survey data as a "
     "divided public, not as a consensus. Recomputed below.",
 29: "Data item: the spread of the all-adults column, recomputed below, against a claim that "
     "the four decisions are treated alike.",
 30: "EK 3.9.A.1 and EK 3.9.A.2 read together, including the closing sentence. Reading the "
     "topic as settled in either direction contradicts it.",
}

BROUGHT, STRUCK = "Challenges brought", "Government action struck down"
GROUND = "Ground of the challenge"
ALL_ADULTS, YOUNGER, OLDER = "All adults (%)", "Under 40 (%)", "40 and older (%)"
DECISION = "Decision at issue"


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def _row(t, needle):
    hits = [r for r in t["rows"] if needle in r[0]]
    assert len(hits) == 1, f"{needle!r} matches {len(hits)} rows, not one"
    return hits[0]


def q24(t):
    """Procedural alone is more than double substantive alone, and 'both' is smallest."""
    sub = gc.num(_row(t, "Substantive")[1])
    proc = gc.num(_row(t, "Procedural")[1])
    both = gc.num(_row(t, "Both grounds")[1])
    assert proc > 2 * sub, f"procedural {proc:.0f} is not more than twice substantive {sub:.0f}"
    assert both < sub and both < proc, f"the 'both grounds' row {both:.0f} is not the smallest"
    return (f"procedural {proc:.0f} against substantive {sub:.0f}, a ratio of "
            f"{proc / sub:.2f}; 'both grounds' smallest at {both:.0f}")


def q25(t):
    """The substantive row's label states the framework's own object of examination."""
    label = _row(t, "Substantive")[0].lower()
    assert "the law itself" in label and "arbitrary infringement" in label, \
        f"the substantive row no longer states EK 3.9.A.1's object: {label!r}"
    proc = _row(t, "Procedural")[0].lower()
    assert "methods" in proc, f"the procedural row no longer states EK 3.8.A.2's object: {proc!r}"
    assert len(t["rows"]) == 3, f"{len(t['rows'])} rows, not three"
    return f"the two grounds are labelled by their objects: {label!r} against {proc!r}"


def q26(t):
    """Substantive alone is a minority of the total the three rows add to."""
    brought = [gc.num(c) for c in _col(t, BROUGHT)]
    total = sum(brought)
    sub = gc.num(_row(t, "Substantive")[1])
    assert total == 425, f"the three rows total {total:.0f}, not 425"
    assert sub < total / 2, f"substantive {sub:.0f} is not a minority of {total:.0f}"
    return (f"{sub:.0f} substantive of {total:.0f} total, "
            f"{gc.pct(sub, total)} percent -- a minority")


def _gaps(t):
    """Age gap per row, keyed by the decision."""
    y, o = t["headers"].index(YOUNGER), t["headers"].index(OLDER)
    return {r[0]: gc.num(r[y]) - gc.num(r[o]) for r in t["rows"]}


def q27(t):
    """The widest age gap sits on the row with the lowest all-adults figure."""
    gaps = _gaps(t)
    widest = max(gaps, key=lambda k: abs(gaps[k]))
    allc = {r[0]: gc.num(r[t["headers"].index(ALL_ADULTS)]) for r in t["rows"]}
    lowest = min(allc, key=lambda k: allc[k])
    assert widest == lowest, \
        f"the widest gap is on {widest!r} but the lowest support is on {lowest!r}"
    assert not all(g > 0 for g in gaps.values()), \
        "every row favours the younger group, which the key's third distractor denies"
    assert min(allc.values()) > 50, "a row falls to or below half, which the fourth option needs"
    return (f"widest age gap {abs(gaps[widest]):.0f} points on {widest!r}, which is also the "
            f"lowest all-adults figure at {allc[lowest]:.0f} percent; gaps "
            + ", ".join(f"{k.split()[0]} {v:+.0f}" for k, v in gaps.items()))


def q28(t):
    """Exactly one row is near an even split, and it is the widest-gap row."""
    allc = {r[0]: gc.num(r[t["headers"].index(ALL_ADULTS)]) for r in t["rows"]}
    divided = [k for k, v in allc.items() if abs(v - 50) <= 5]
    assert len(divided) == 1, f"{len(divided)} rows sit near an even split: {divided}"
    gaps = _gaps(t)
    widest = max(gaps, key=lambda k: abs(gaps[k]))
    assert divided[0] == widest, \
        f"the divided row {divided[0]!r} is not the widest-gap row {widest!r}"
    consensus = [k for k, v in allc.items() if v >= 85]
    assert consensus, "no row shows the near-consensus pattern the key contrasts against"
    return (f"one divided row, {divided[0]!r} at {allc[divided[0]]:.0f} percent with a "
            f"{abs(gaps[widest]):.0f} point gap, against near-consensus on "
            f"{', '.join(repr(c) for c in consensus)}")


def q29(t):
    """The all-adults column spreads 36 points, so the four are not treated alike."""
    allc = [gc.num(c) for c in _col(t, ALL_ADULTS)]
    spread = max(allc) - min(allc)
    assert spread == 36, f"the all-adults spread is {spread:.0f} points, not 36"
    assert len(set(allc)) == len(allc), "two decisions draw identical support"
    names = _col(t, DECISION)
    assert len(set(names)) == len(names), f"a decision is listed twice: {names}"
    return (f"all-adults column runs {max(allc):.0f} down to {min(allc):.0f}, "
            f"a spread of {spread:.0f} points across {len(names)} distinct decisions")


# --- module-specific content gates -------------------------------------------

_SUBSTANTIVE_OBJECT = ("the law itself", "laws and actions", "a government law or action",
                       "what the law does", "arbitrary infringement", "arbitrary infringements",
                       "arbitrarily invades", "a protected private choice is invaded",
                       "protected private sphere")
_PROCEDURAL_OBJECT = ("the methods", "methods officials used", "methods used",
                      "notice and a hearing", "how it was made", "procedures")


def _substantive(module):
    """No key may give substantive due process the procedural object, or the reverse."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        if "substantive due process" in key:
            head = key[:key.index("substantive due process")]
            tail = key[key.index("substantive due process"):]
            # The clause that follows the name is what defines it here.
            seg = tail.split("while")[0]
            if any(p in seg for p in _PROCEDURAL_OBJECT) and \
               not any(s in seg for s in _SUBSTANTIVE_OBJECT):
                bad.append(f"q{i} key: gives substantive due process a procedural object; EK "
                           "3.9.A.1 aims it at whether laws and actions are arbitrary "
                           f"infringements. Clause: {seg!r}")
            del head
        if "procedural due process" in key:
            seg = key[key.index("procedural due process"):].split("while")[0]
            if any(s in seg for s in ("the law itself", "arbitrarily invades",
                                      "what the law does")):
                bad.append(f"q{i} key: gives procedural due process a substantive object; EK "
                           f"3.8.A.2 aims it at the methods officials used. Clause: {seg!r}")
    q7 = module.QUESTIONS[6]
    if "arbitrary infringements of individual rights" not in q7["choices"][q7["ans"]].lower():
        bad.append("q7: the key no longer states EK 3.9.A.1's object of the substantive "
                   "examination, 'arbitrary infringements of individual rights'")
    if bad:
        print(f"FAIL {module.__name__} substantive")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} substantive: no key gives substantive due process the "
          "procedural object or procedural due process the substantive one, and EK 3.9.A.1's "
          "own object survives in the defining key")


# Every case name this module can mention. A phrase is attributed to the case
# name NEAREST BEFORE IT, not to any case named anywhere in the sentence -- the
# first draft of this check did the latter and reported a false finding on item
# 20, whose key correctly says "Brown rests on the equal protection clause...
# while Griswold rests on the due process clause". Attributing "equal
# protection" to Griswold because both names appear in one sentence is the
# over-matching own-goal this project keeps paying for: a checker that fires on
# a correct key trains its reader to ignore it.
_CASE_NAMES = ("griswold", "roe", "dobbs", "brown", "gideon", "baker", "mcdonald",
               "marbury", "mcculloch", "shaw", "citizens united")


def _attributed_to(text, phrase_at):
    """The case name nearest before an offset, or None if no name precedes it."""
    best, best_at = None, -1
    for name in _CASE_NAMES:
        at = text.rfind(name, 0, phrase_at)
        if at > best_at:
            best, best_at = name, at
    return best


def _holdings(module):
    """The three EK 3.9.A.2 holdings keep the framework's own verbs and go no further."""
    bad = []
    overstatements = {
        "dobbs": (("requires states to permit", "requires states to prohibit",
                   "forbids abortion", "abolished the right to privacy",
                   "overturned griswold", "to the federal courts"),
                  "EK 3.9.A.2 says only that Dobbs held the Constitution DOES NOT CONFER a "
                  "right to abortion and left regulation TO LEGISLATURES"),
        "griswold": (("explicitly named in the constitution to protect",
                      "found the right written", "equal protection clause"),
                     "EK 3.9.A.2 says Griswold INTERPRETED the DUE PROCESS clause; the right "
                     "is not explicitly named"),
        "roe": (("created a new doctrine", "equal protection clause",
                 "committed to congress"),
                "EK 3.9.A.2 says Roe EXTENDED the privacy right through substantive due "
                "process"),
    }
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        stem = item["q"].lower()
        for case, (phrases, note) in overstatements.items():
            if case not in stem and case not in key:
                continue
            for p in phrases:
                at = key.find(p)
                if at < 0:
                    continue
                owner = _attributed_to(key, at)
                # No case name precedes the phrase: fall back to the stem's
                # subject, since the key is then completing the stem's sentence.
                if owner is None:
                    owner = _attributed_to(stem + " " + key, len(stem) + 1 + at)
                if owner == case:
                    bad.append(f"q{i} key: states {p!r} about {case.title()}; {note}")
    q16 = module.QUESTIONS[15]
    k16 = q16["choices"][q16["ans"]].lower()
    if "does not confer a right to abortion" not in k16 or "legislatures" not in k16:
        bad.append("q16: the Dobbs key no longer carries both halves of EK 3.9.A.2's sentence, "
                   "DOES NOT CONFER and LEAVING DECISIONS TO LEGISLATURES")
    q15 = module.QUESTIONS[14]
    if "extended the privacy right to abortion" not in q15["choices"][q15["ans"]].lower():
        bad.append("q15: the Roe key no longer carries EK 3.9.A.2's verb EXTENDED")
    q13 = module.QUESTIONS[12]
    k13 = q13["choices"][q13["ans"]].lower()
    if "interpreted the due process clause" not in k13:
        bad.append("q13: the Griswold key no longer says the Court INTERPRETED the DUE PROCESS "
                   "clause, which is EK 3.9.A.2's own verb and clause")
    if bad:
        print(f"FAIL {module.__name__} holdings")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} holdings: Griswold keeps INTERPRETED THE DUE PROCESS CLAUSE, "
          "Roe keeps EXTENDED, Dobbs keeps DOES NOT CONFER and TO LEGISLATURES, and no key "
          "states a holding stronger than the one EK 3.9.A.2 states")


ua.shape(v3_9)
ua.check(v3_9, ANCHORS, GROUNDING)
ua.notation(v3_9)
_substantive(v3_9)
_holdings(v3_9)
gc.check(v3_9, arith={24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29})
