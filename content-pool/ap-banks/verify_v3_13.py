"""Structural gate for AP U.S. Government 3.13 Affirmative Action.

gov345_check plus the four usgov_anchor helpers, plus three content gates.

This is the shortest essential knowledge statement in Unit 3 -- two sentences --
and it is also the topic where a wrong key would do the most damage, because the
subject is one a student is likely to arrive with a position on. Everything
below exists to keep thirty questions honest against two sentences.

  _definition   EK 3.13.A.1 names FIVE characteristics (race, ethnic origin,
                gender, DISABILITY and AGE) and TWO domains (workplace AND
                educational). Disability and age are what a summary drops, and
                dropping them turns the framework's definition into a narrower
                policy about race that the framework never states. The gate
                pins the full list and the full pair of domains, and refuses any
                key that says the definition covers only one of either.

  _unresolved   LO 3.13.A's verb is DESCRIBE and its object is DEBATES. EK
                3.13.A.1 says the Court's debate HAS FOCUSED ON whether
                affirmative action is protected by the equal protection clause,
                and it stops. No key may state an outcome. This is the gate that
                matters most: an answer supplied from outside the framework
                would reach a student with exactly the authority of the
                framework's own sentence, and nothing in the item would mark it
                as the author's view rather than the College Board's. The gate
                also pins the framework's phrase PROTECTED BY, because the
                framing a student arrives with is "whether it violates the
                clause" and that is a different question with the burden on the
                other side.

  _case_names   The CED lists four cases for this topic and marks every one of
                them an ILLUSTRATIVE EXAMPLE, NOT REQUIRED. None may be named,
                for the same reason 3.12 does not name the separate but equal
                case: an illustrative example printed beside required content is
                indistinguishable from it. Item 24 makes the required/
                illustrative distinction the question instead, which is the one
                honest way to use the fact that those cases exist.

WHY BOTH TABLES END THE SAME WAY
--------------------------------
Items 27 and 30 are the same lesson approached from opposite directions: a
hiring table cannot show that a remedial policy would be unconstitutional, and
an admissions table cannot show that one is protected. Data measure a disparity
or an effect; EK 3.13.A.1's question is neither. Building both stimulus sets so
that the data CANNOT reach the constitutional question is deliberate, and the
two arithmetic checks below assert exactly that -- that each table reports what
the key says it reports, and nothing that would settle the debate.
"""
import re

import gov345_check as gc
import usgov_anchor as ua
import v3_13

ANCHORS = {
 1: "Policies intended to address workplace and educational disparities",
 2: "Race, ethnic origin, gender, disability, and age",
 3: "Disability and age",
 4: "age is one of the five characteristics",
 5: "disability is among the named characteristics and education is among the named domains",
 6: "The workplace and education",
 7: "Whether affirmative action is protected by the equal protection clause",
 8: "place the burden of argument on different sides",
 9: "The equal protection clause of the Fourteenth Amendment",
 10: "records what the argument is about rather than how it came out",
 11: "states what the debate is about and does not state an answer",
 12: "a government policy that distinguishes among them must be measured against it",
 13: "A State",
 14: "which is the question the framework says the Court's debate has focused on",
 15: "so the constitutional question the framework describes does not arise in the same way",
 16: "The educational domain, one of the two the framework names",
 17: "names five characteristics, of which race is one",
 18: "since the framework names workplace and educational disparities together",
 19: "measured against the equal protection clause",
 20: "while here it is the standard against which a policy adopted for a group is measured",
 21: "which is where the unit's argument arrives",
 22: "so a claim that it is settled goes beyond what the framework states",
 23: "the five characteristics and two domains it covers",
 24: "the exam will not require knowledge of them the way it requires the holdings",
 25: "and every other group's share of hires falls below its share of applicants",
 26: "A workplace disparity of the kind affirmative action policies are intended to address",
 27: "The table measures a disparity, and whether such a policy is protected",
 28: "narrowed in each successive year shown",
 29: "The educational domain, one of the two the framework's definition names",
 30: "reports what a policy achieved, which is a different question from the constitutional one",
}

GROUNDING = {
 1: "EK 3.13.A.1, verbatim: 'Affirmative action refers to policies intended to address "
    "workplace and educational disparities...' The definition runs to the disparities "
    "addressed rather than to any method of addressing them.",
 2: "EK 3.13.A.1's five characteristics: 'race, ethnic origin, gender, disability, and age.'",
 3: "EK 3.13.A.1's list read for what a summary loses. Disability and age extend the concept "
    "well beyond the categories it is usually discussed in.",
 4: "EK 3.13.A.1 applied: age is among the five characteristics and the workplace among the "
    "two domains, so both halves of the definition are satisfied.",
 5: "EK 3.13.A.1 applied: disability is among the five characteristics and education among the "
    "two domains. Whether the institution is public is a question the definition does not "
    "turn on -- though EK 3.10.A.1's point about state action bears on what follows.",
 6: "EK 3.13.A.1's two domains, 'workplace and educational disparities'. Voting, housing and "
    "public accommodations belong to the statutes of EK 3.11.A.1, not to this definition.",
 7: "EK 3.13.A.1, verbatim: 'Supreme Court debate has focused on whether affirmative action is "
    "protected by the equal protection clause of the Fourteenth Amendment.'",
 8: "EK 3.13.A.1's phrase PROTECTED BY against the framing a student usually arrives with. "
    "Asking whether a clause shelters a policy and whether a policy offends it are different "
    "questions, and the framework's own wording is the first.",
 9: "EK 3.13.A.1's named clause. EK 3.10.A.1 names the same clause, with the due process "
    "clause and acts of Congress, as a source of civil rights generally.",
 10: "LO 3.13.A's verb DESCRIBE and object DEBATES, against EK 3.13.A.1's 'has focused on'. "
     "Every other topic in this unit states a holding where there is one to state.",
 11: "EK 3.13.A.1's second sentence, read for where it ends. An answer supplied from outside "
     "the framework would reach a student with the framework's own authority.",
 12: "U.S. Constitution, Fourteenth Amendment Section 1, quoted verbatim. The clause runs to "
     "any person within a state's jurisdiction and constrains state action, which is why EK "
     "3.13.A.1 locates the Court's debate there.",
 13: "Fourteenth Amendment Section 1's grammatical subject, 'any State' -- the same point EK "
     "3.10.A.1 relies on when it names acts of Congress as a separate source of civil rights.",
 14: "EK 3.13.A.1 applied, CED skill 1.E. Ethnic origin is among the five characteristics and "
     "the workplace among the two domains, so the framework's constitutional question is the "
     "one the program raises.",
 15: "EK 3.13.A.1's definition (which turns on the disparity addressed, not on who addresses "
     "it) against EK 3.10.A.1's point that the Fourteenth Amendment's clauses run to a State.",
 16: "EK 3.13.A.1's educational domain. The framework's word is EDUCATIONAL rather than higher "
     "education, so a school district is inside it.",
 17: "EK 3.13.A.1's five characteristics against a description that keeps only the first.",
 18: "EK 3.13.A.1 names both domains in one sentence without ranking them.",
 19: "EK 3.12.A.1.iv (the Court upholding the rights of the majority in cases limiting "
     "majority-minority districting) against EK 3.13.A.1, both located in the equal protection "
     "clause: a measure adopted for one group tested against a guarantee running to all.",
 20: "EK 3.10.A.2 (the clause can support and motivate movements) against EK 3.13.A.1 (the "
     "clause as the provision the debate is conducted under). One mobilizing role, one "
     "testing role, one clause.",
 21: "The unit's four civil rights topics read in order: EK 3.10.A.2 movements invoke the "
     "clause, EK 3.11.A.1 the government responds, EK 3.12.A.1 records both directions, EK "
     "3.13.A.1 asks what the clause does about a remedy.",
 22: "LO 3.13.A's DESCRIBE and DEBATES against EK 3.13.A.1's 'has focused on', which records "
     "no answer. Reporting the framework accurately means reporting that.",
 23: "EK 3.13.A.1 in full: a definition, five characteristics, two domains, and the focus of a "
     "debate. The CED marks this topic's four cases as illustrative examples, NOT REQUIRED.",
 24: "The CED's own distinction between required cases, whose holdings are course content, and "
     "ILLUSTRATIVE EXAMPLES marked NOT REQUIRED, of which this topic lists four.",
 25: "Data item, CED skill 1.E. Every share and every change is recomputed below.",
 26: "EK 3.13.A.1's workplace domain located in the table: a gap between a group's share of "
     "applicants and its share of hires is the condition a policy would address.",
 27: "EK 3.13.A.1's unanswered question against data that cannot answer it. The table's "
     "content is recomputed below to confirm it reports a disparity and nothing more.",
 28: "Data item, CED skill 1.E. All four gaps are recomputed below.",
 29: "EK 3.13.A.1's educational domain located in the table.",
 30: "EK 3.13.A.1's unanswered question again, from the other side: effectiveness and "
     "constitutionality are different questions, and the framework answers neither here.",
}

APPS, HIRED = "Share of applicants (%)", "Share of those hired (%)"
ADM = "Share of admitted students (%)"
GROUP, YEAR = "Applicant group", "Year"


def _col(t, header):
    j = t["headers"].index(header)
    return [gc.num(r[j]) for r in t["rows"]]


def _labels(t):
    return [r[0] for r in t["rows"]]


def q25(t):
    """Exactly one group rises; the other three fall; both columns total 100."""
    a, h = _col(t, APPS), _col(t, HIRED)
    assert sum(a) == 100 and sum(h) == 100, f"columns total {sum(a):.0f} and {sum(h):.0f}"
    deltas = dict(zip(_labels(t), (y - x for x, y in zip(a, h))))
    up = [k for k, v in deltas.items() if v > 0]
    assert len(up) == 1, f"{len(up)} groups rise, not one: {up}"
    assert all(v < 0 for k, v in deltas.items() if k not in up), "a group is exactly flat"
    return ("changes " + ", ".join(f"{k} {v:+.0f}" for k, v in deltas.items())
            + f" -- one riser, {up[0]}")


def q26(t):
    """The table is a workplace stimulus: applicants and hires, no year column."""
    assert APPS in t["headers"] and HIRED in t["headers"], "a share column is missing"
    assert YEAR not in t["headers"], "the hiring table carries a year column"
    a, h = _col(t, APPS), _col(t, HIRED)
    assert any(x != y for x, y in zip(a, h)), "no disparity: the two columns are identical"
    return (f"{len(t['rows'])} groups, applicant and hire shares differing in "
            f"{sum(1 for x, y in zip(a, h) if x != y)} of them")


def q27(t):
    """A disparity is present and nothing in the table bears on constitutionality."""
    a, h = _col(t, APPS), _col(t, HIRED)
    gaps = [abs(y - x) for x, y in zip(a, h)]
    assert max(gaps) > 0, "the key's premise fails: the table shows no disparity"
    legal = ("constitution", "equal protection", "unconstitutional", "court", "clause",
             "amendment", "lawful", "policy")
    cells = [c.lower() for c in t["headers"]] + [c.lower() for r in t["rows"] for c in r]
    for cell in cells:
        for w in legal:
            assert w not in cell, (
                f"the table cell {cell!r} names {w!r}; this stimulus must report a disparity "
                "only, since items 27 and 30 turn on data being unable to reach EK 3.13.A.1's "
                "constitutional question")
    return (f"largest gap {max(gaps):.0f} points; no cell in the table names a court, a clause "
            "or a policy, so nothing here bears on the constitutional question")


def q28(t):
    """The gap narrows monotonically and the admitted share stays below the applicant share."""
    a, adm = _col(t, APPS), _col(t, ADM)
    gaps = [x - y for x, y in zip(a, adm)]
    assert all(g > 0 for g in gaps), f"the admitted share reaches the applicant share: {gaps}"
    assert gaps == sorted(gaps, reverse=True) and len(set(gaps)) == len(gaps), \
        f"the gaps do not narrow strictly: {gaps}"
    assert adm == sorted(adm) and adm[-1] > adm[0], "the admitted share does not rise"
    return (f"gaps {', '.join(f'{g:.0f}' for g in gaps)} points, narrowing each year; "
            f"admitted share {adm[0]:.0f} to {adm[-1]:.0f}, still below the applicant "
            f"share of {a[-1]:.0f}")


def q29(t):
    """The table is an education stimulus over four separate years."""
    assert YEAR in t["headers"], "the admissions table has no year column"
    years = _labels(t)
    assert len(years) == 4 and len(set(years)) == 4, f"years are {years}"
    assert ADM in t["headers"], "the admitted-share column is missing"
    return f"four distinct years of admissions data: {', '.join(years)}"


def q30(t):
    """An effect is present and nothing in the table bears on constitutionality."""
    a, adm = _col(t, APPS), _col(t, ADM)
    assert adm[-1] > adm[0], "the key's premise fails: the table shows no achievement"
    legal = ("constitution", "equal protection", "unconstitutional", "court", "clause",
             "amendment", "lawful", "protected")
    cells = [c.lower() for c in t["headers"]] + [c.lower() for r in t["rows"] for c in r]
    for cell in cells:
        for w in legal:
            assert w not in cell, (
                f"the table cell {cell!r} names {w!r}; this stimulus must report an effect "
                "only, since the item turns on data being unable to settle EK 3.13.A.1's "
                "question")
    return (f"admitted share rises {adm[-1] - adm[0]:.0f} points against an applicant share "
            f"rising {a[-1] - a[0]:.0f}; no cell names a court, a clause or a holding")


# --- module-specific content gates -------------------------------------------

_CHARACTERISTICS = ("race", "ethnic origin", "gender", "disability", "age")


def _definition(module):
    """EK 3.13.A.1's five characteristics and two domains stay five and two."""
    bad = []
    q2 = module.QUESTIONS[1]
    k2 = q2["choices"][q2["ans"]].lower()
    for c in _CHARACTERISTICS:
        if c not in k2:
            bad.append(f"q2: the key has dropped {c!r}, one of EK 3.13.A.1's five named "
                       "characteristics")
    q6 = module.QUESTIONS[5]
    k6 = q6["choices"][q6["ans"]].lower()
    if "workplace" not in k6 or "education" not in k6:
        bad.append("q6: the key no longer names both of EK 3.13.A.1's domains, workplace and "
                   "educational")
    q1 = module.QUESTIONS[0]
    k1 = q1["choices"][q1["ans"]].lower()
    if "workplace and educational disparities" not in k1:
        bad.append("q1: the key no longer carries EK 3.13.A.1's own object, 'workplace and "
                   "educational disparities'")
    # No key may narrow the definition to one characteristic or one domain.
    narrowings = ("covers only race", "is a policy about race alone", "names race alone",
                  "covers only gender", "covers only workplaces", "covers only education",
                  "covers only educational", "covers only workplace")
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for n in narrowings:
            if n in key:
                bad.append(f"q{i} key: narrows EK 3.13.A.1's definition by saying it {n!r}; "
                           "the framework names five characteristics and two domains")
    if bad:
        print(f"FAIL {module.__name__} definition")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} definition: all five of EK 3.13.A.1's characteristics and "
          "both of its domains survive in the defining keys, and no key narrows the "
          "definition to one of either")


# Outcome claims. Each is a statement the framework does NOT make, phrased the
# way a confident author would phrase it. The check runs on keys only: a
# DISTRACTOR saying "the framework states that affirmative action is protected"
# is exactly what items 11 and 22 need in order to be answerable, so scanning
# every choice would make the module unwritable. That asymmetry is the point --
# the gate protects what the bank ASSERTS, not what it offers to be rejected.
_OUTCOMES = (
    "the supreme court has held that affirmative action is protected",
    "the supreme court has held that affirmative action violates",
    "affirmative action is protected by the equal protection clause, as the court has held",
    "the question has been settled",
    "the court settled the question",
    "the debate has been resolved",
    "affirmative action is unconstitutional",
    "affirmative action is constitutional",
)


def _unresolved(module):
    """No key states an outcome the framework does not state."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for phrase in _OUTCOMES:
            if phrase in key:
                bad.append(f"q{i} key: states {phrase!r}. LO 3.13.A's verb is DESCRIBE and its "
                           "object is DEBATES; EK 3.13.A.1 says the debate HAS FOCUSED ON a "
                           "question and records no answer")
    q7 = module.QUESTIONS[6]
    k7 = q7["choices"][q7["ans"]].lower()
    if "protected by the equal protection clause" not in k7:
        bad.append("q7: the key no longer carries EK 3.13.A.1's own framing, PROTECTED BY the "
                   "equal protection clause -- not whether affirmative action violates it")
    for n in (10, 11, 22):
        key = module.QUESTIONS[n - 1]["choices"][module.QUESTIONS[n - 1]["ans"]].lower()
        if not any(w in key for w in ("does not state", "rather than how it came out",
                                      "goes beyond what the framework states")):
            bad.append(f"q{n}: the key no longer records that the framework leaves the "
                       "question open, which is the one thing this topic actually settles")
    if bad:
        print(f"FAIL {module.__name__} unresolved")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} unresolved: no key states an outcome EK 3.13.A.1 does not "
          "state, the framework's PROTECTED BY framing survives, and the three items that "
          "record the question as open still record it")


_REQUIRED_PAIRS = {
    ("marbury", "madison"), ("mcculloch", "maryland"), ("schenck", "united"),
    ("brown", "board"), ("baker", "carr"), ("engel", "vitale"),
    ("gideon", "wainwright"), ("tinker", "des"), ("co", "united"), ("times", "united"),
    ("wisconsin", "yoder"), ("shaw", "reno"), ("states", "lopez"),
    ("mcdonald", "chicago"), ("united", "federal"), ("united", "fec"),
}
_VS = re.compile(r"([A-Za-z]+)\.?\s+v\.\s+([A-Za-z]+)")


def _case_names(module):
    """None of this topic's four illustrative cases may be named."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        strings = [("stem", item["q"]), ("why", item["why"])]
        strings += [(f"choice {'ABCDE'[k]}", c) for k, c in enumerate(item["choices"])]
        for label, s in strings:
            for m in _VS.finditer(s):
                if (m.group(1).lower(), m.group(2).lower()) not in _REQUIRED_PAIRS:
                    bad.append(f"q{i} {label}: names {m.group(0)!r}. The CED marks every case "
                               "it lists for 3.13 an ILLUSTRATIVE EXAMPLE, NOT REQUIRED, and "
                               "an illustrative example printed beside required content is "
                               "indistinguishable from it")
    if bad:
        print(f"FAIL {module.__name__} case names")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} case names: none of the four cases the CED lists for this "
          "topic as illustrative examples is named anywhere in the module")


ua.shape(v3_13)
ua.check(v3_13, ANCHORS, GROUNDING)
ua.notation(v3_13)
_definition(v3_13)
_unresolved(v3_13)
_case_names(v3_13)
gc.check(v3_13, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
