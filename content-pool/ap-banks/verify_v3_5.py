"""Structural gate for AP U.S. Government 3.5 Second Amendment: Right to Bear Arms.

gov345_check plus the four usgov_anchor helpers.

THE THINNEST STATEMENT IN THE COURSE, AND WHY THAT MAKES THIS FILE STRICTER
-----------------------------------------------------------------------------
EK 3.5.A.1 says only that "the Supreme Court's decisions on the Second Amendment
rest upon its constitutional interpretation of the right to bear arms." It names
no doctrine, no test and no outcome. A sentence that thin does not free an
author; it fences them in, because everything a bank might want to say beyond it
would be either off-syllabus or a policy position.

So the two guards here are about RESTRAINT rather than about accuracy:

  _no_test          The framework supplies a holding about APPLICABILITY (the
                    right applies to the states) and PURPOSE (self-defense). It
                    supplies no standard for evaluating any regulation. No key
                    in this module may state one, in either direction -- neither
                    "no regulation is permissible" nor "all regulation is
                    permissible". Item 27 makes the absence of a standard the
                    answer, and item 28 makes recognising that absence the skill.
  _lopez_is_commerce
                    United States v. Lopez is attached to 3.5.A and holds
                    NOTHING about the right to bear arms. The CED's own
                    statement of it names the Commerce Clause. A student who
                    files it as a Second Amendment case has a false holding
                    ready to write into an FRQ, and this check fails the module
                    if any key or rationale supplies one.

THE TABLE OF WHAT THE TEXT DOES NOT SAY
-----------------------------------------
The clauses table has four rows and only two of them quote the Amendment. The
other two are propositions people attribute to it -- a right to a particular
weapon, a ban on all regulation -- with "No" in the last column. That is the
honest way to teach a contested text: show what it says beside what it is said
to say. q21 asserts the Yes/No split, and q23 asserts that neither absent
proposition appears in the quoted clauses, so a later edit cannot quietly
promote one of them into the text.
"""
import gov345_check as gc
import usgov_anchor as ua
import v3_5

ANCHORS = {
 1: "The Court's constitutional interpretation of the right to bear arms",
 2: "the relationship between the two is not spelled out",
 3: "Self-defense",
 4: "connected to service in an organized militia",
 5: "held by individuals, since the text says the right of the people",
 6: "does not resolve the relationship between its two clauses",
 7: "was made enforceable against state and local governments as well",
 8: "For self-defense",
 9: "the textual route by which a guarantee originally aimed at the national government",
 10: "one instance of the general process",
 11: "restrained the national government and not the states",
 12: "so both came from interpretation",
 13: "What the Second Amendment's two clauses mean when read together",
 14: "directs attention to the reasoning behind a holding",
 15: "Nothing; the holding rests on the limits of the Commerce Clause",
 16: "answered before any question about individual rights",
 17: "which leaves states free to regulate the same conduct",
 18: "McDonald decides a question about individual rights and which governments they bind",
 19: "questions of both governmental power and individual rights",
 20: "McDonald, since it makes the Second Amendment right applicable to the states",
 21: "describe readings the text does not state",
 22: "support different readings of the same sentence",
 23: "Neither a right to a particular weapon nor a ban on all regulation appears",
 24: "Three of the four guarantees came to restrain the states",
 25: "The right to keep and bear arms for self-defense, which restrained the national government",
 26: "one at a time rather than all together",
 27: "the extent is established on reach and open on limits",
 28: "which the course framework does not supply",
 29: "and that the right to keep and bear arms for self-defense applies to the states",
 30: "wrong even if it matches a common opinion",
}

GROUNDING = {
 1: "EK 3.5.A.1, verbatim: the decisions 'rest upon its constitutional interpretation of the "
    "right to bear arms.'",
 2: "U.S. Constitution, Second Amendment, quoted verbatim. A prefatory clause and an "
    "operative clause with the relationship unstated is what makes interpretation necessary.",
 3: "The Second Amendment's text against the CED's statement of the McDonald holding: "
    "'self-defense' is in the second and not in the first.",
 4: "The Second Amendment's prefatory clause read as controlling.",
 5: "The Second Amendment's operative clause read as controlling: 'the right of the people', "
    "the phrase the First and Fourth Amendments use for individual rights.",
 6: "EK 3.5.A.1's word INTERPRETATION, and the textual feature that makes it unavoidable.",
 7: "McDonald v. Chicago (2010), required case, which the CED attaches to 3.5.A. CED holding: "
    "'The Second Amendment right to keep and bear arms for self-defense is applicable to the "
    "states.' A question about reach, not about existence.",
 8: "The CED's statement of McDonald names the purpose -- FOR SELF-DEFENSE -- which the "
    "constitutional text does not, and which is therefore interpretive content.",
 9: "U.S. Constitution, Fourteenth Amendment Section 1, quoted verbatim: it restrains STATES "
    "and protects liberty, which is the route for applying a guarantee against them.",
 10: "McDonald as an instance of selective incorporation, which topic 3.7 covers as a process.",
 11: "The CED's McDonald holding read backwards: applicability to the states was an open "
     "question until the decision settled it.",
 12: "EK 3.5.A.1 demonstrated: neither 'self-defense' nor 'applicable to the states' is in the "
     "Second Amendment, so both are interpretation.",
 13: "EK 3.5.A.1's interpretive question is prior to any application; the distractors are "
     "policy and political questions rather than legal ones.",
 14: "LO 3.5.A's 'extent to which... reflects a commitment to individual liberty' is a question "
     "about reasoning, which is what EK 3.5.A.1's phrasing directs attention to.",
 15: "United States v. Lopez (1995), required case, which the CED attaches to 3.5.A. CED "
     "holding: 'Congress exceeded its power under the Commerce Clause.' It holds NOTHING about "
     "the right to bear arms, and treating it as a Second Amendment case teaches a false "
     "holding.",
 16: "EK 1.8.A's ordering: whether a government has power to act is answered before whether "
     "the action burdens a right.",
 17: "Lopez's holding as the CED states it, with the half students miss: a limit on CONGRESS "
     "says nothing about what a state may do.",
 18: "McDonald against Lopez -- two required cases attached to one topic that answer different "
     "constitutional questions and share only a subject matter.",
 19: "Why the CED pairs them: a regulation must be within some government's power AND "
     "consistent with individual rights.",
 20: "McDonald applies to a STATE regulation; Lopez limits congressional power and is silent "
     "on state authority.",
 21: "Data item; the Yes/No split between quoted text and attributed propositions is "
     "recomputed below.",
 22: "EK 3.5.A.1 shown in the table's first two rows: one sentence, two clauses, two "
     "defensible emphases.",
 23: "The table's last two rows are propositions the text does not contain, which is how a "
     "contested text is taught honestly.",
 24: "Data item; the incorporation pattern across four guarantees is recomputed below.",
 25: "The CED's McDonald holding located as a row: national government first, then the states.",
 26: "The grand jury row makes the process SELECTIVE, which is topic 3.7's subject and the "
     "reason McDonald had to be decided at all.",
 27: "LO 3.5.A's 'extent to which' answered within the framework's limits: reach and purpose "
     "settled, permissible regulation unaddressed.",
 28: "SOCIAL_BRIEF.md's rule applied to a student's own reasoning: recognising what the course "
     "does NOT establish is part of answering the objective.",
 29: "EK 3.5.A.1 plus the CED's statement of McDonald, which together are everything the "
     "framework establishes for this topic.",
 30: "LO 3.5.A asks about the Court's interpretation; EK 3.6.A.2 separately identifies firearms "
     "policy as contested. What has been decided and what is debated are different questions.",
}

IN_TEXT = "Is the clause in the text?"
READING = "What a reader emphasizing it takes the Amendment to protect"
NAT = "Restrained the national government"
BEFORE = "Restrained the states before the decision"
AFTER = "Restrains the states after the decision"
ARMS = "Right to keep and bear arms for self-defense"
GRAND = "Requirement of a grand jury indictment"


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def _cell(t, label, header):
    j = t["headers"].index(header)
    for r in t["rows"]:
        if r[0] == label:
            return r[j]
    raise KeyError(label)


def q21(t):
    """Exactly two rows quote the Amendment; two are propositions it does not contain."""
    col = _col(t, IN_TEXT)
    assert col == ["Yes", "Yes", "No", "No"], f"the in-text column reads {col}"
    quoted = [r[0] for r, c in zip(t["rows"], col) if c == "Yes"]
    assert "well regulated Militia" in quoted[0] and "right of the people" in quoted[1], \
        f"the quoted rows are {quoted}"
    return "two rows quote the Amendment, two state propositions it does not contain"


def q22(t):
    """The two quoted clauses support DIFFERENT readings, which is the whole point."""
    col = _col(t, IN_TEXT)
    readings = [r for r, c in zip(_col(t, READING), col) if c == "Yes"]
    assert len(set(readings)) == 2, "the two quoted clauses no longer support different readings"
    assert "militia" in readings[0].lower() and "individuals" in readings[1].lower(), \
        f"the two readings are {readings}"
    return "the two quoted clauses support a militia-linked and an individual reading"


def q23(t):
    """Neither absent proposition may appear inside a quoted clause."""
    col = _col(t, IN_TEXT)
    quoted = " ".join(r[0].lower() for r, c in zip(t["rows"], col) if c == "Yes")
    for phrase in ("particular weapon", "prohibition on all", "all firearms regulation"):
        assert phrase not in quoted, \
            f"{phrase!r} now appears inside a clause marked as in the text"
    absent = [r[0] for r, c in zip(t["rows"], col) if c == "No"]
    assert len(absent) == 2, f"{len(absent)} rows are marked as absent from the text"
    return f"both absent propositions stay outside the quoted text: {absent}"


def q24(t):
    """Three guarantees came to restrain the states; one did not."""
    assert _col(t, NAT) == ["Yes"] * 4, "a guarantee does not restrain the national government"
    assert _col(t, BEFORE) == ["No"] * 4, "a guarantee already restrained the states"
    after = _col(t, AFTER)
    assert after.count("Yes") == 3 and after.count("No") == 1, f"the after column reads {after}"
    return "four guarantees bind the national government, three came to bind the states"


def q25(t):
    """The arms row follows the incorporation pattern the CED's McDonald holding states."""
    assert _cell(t, ARMS, NAT) == "Yes" and _cell(t, ARMS, BEFORE) == "No" \
        and _cell(t, ARMS, AFTER) == "Yes", "the arms row no longer shows incorporation"
    assert "self-defense" in ARMS, \
        "the arms row no longer names the purpose the CED's McDonald holding states"
    return "arms row: national yes, states no before, states yes after -- McDonald's pattern"


def q26(t):
    """One guarantee did not change, which is what makes the process selective."""
    unchanged = [r[0] for r in t["rows"]
                 if _cell(t, r[0], BEFORE) == _cell(t, r[0], AFTER)]
    assert unchanged == [GRAND], f"the unchanged rows are {unchanged}"
    return f"one guarantee unchanged ({GRAND}), so the process is selective rather than total"


def _no_test(module):
    """The framework supplies no standard for evaluating a firearms regulation."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for phrase in ("no firearms regulation is permissible",
                       "all firearms regulation is permissible",
                       "any regulation of firearms is unconstitutional",
                       "states may regulate firearms without limit"):
            if phrase in key:
                bad.append(f"q{i} key: states a standard for evaluating firearms regulation "
                           f"({phrase!r}); the framework supplies a holding about "
                           "applicability and purpose and no test")
    if bad:
        print(f"FAIL {module.__name__} no test")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} no test: no key states a standard for evaluating a firearms "
          "regulation, in either direction -- the framework supplies none")


def _lopez_is_commerce(module):
    """No key or rationale may give Lopez a Second Amendment holding."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        for label, s in (("key", item["choices"][item["ans"]]), ("why", item["why"])):
            low = s.lower()
            if "lopez" not in low:
                continue
            if "second amendment" in low and "commerce" not in low:
                if not any(n in low for n in ("nothing", "not ", "rather than", "says nothing")):
                    bad.append(f"q{i} {label}: attaches a Second Amendment holding to Lopez; "
                               "the CED states it as a Commerce Clause holding")
    if bad:
        print(f"FAIL {module.__name__} Lopez")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} Lopez: no key or rationale gives United States v. Lopez a "
          "Second Amendment holding; the CED states it as a Commerce Clause holding")


ua.shape(v3_5)
ua.check(v3_5, ANCHORS, GROUNDING)
ua.notation(v3_5)
_no_test(v3_5)
_lopez_is_commerce(v3_5)
gc.check(v3_5, arith={21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26})

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key, and one thing worth stating plainly because it looks like an
# omission and is a decision.
#
# This module says nothing about what firearms regulations survive constitutional
# review. That is not an oversight: the CED gives this topic one sentence about
# interpretation and one required holding about APPLICABILITY TO THE STATES for
# SELF-DEFENSE, and it gives no test. SOCIAL_BRIEF.md's rule is that an
# uncertain key is cut rather than guessed, and a bank that supplied a standard
# the framework does not state would be teaching content the exam cannot ask
# about while sounding authoritative about a contested question. So items 27 and
# 28 make the ABSENCE of a standard the thing being tested, and _no_test asserts
# that no key drifts in either direction.
#
# The other thing recorded here is the Lopez trap, which is the most valuable
# item in the module. The CED attaches United States v. Lopez to this topic, and
# it is a case about a gun law that decides a question of congressional power.
# A student who reads the topic heading and the case name together will file it
# as a Second Amendment holding, and then write that false holding in an FRQ.
# Items 15 to 20 attack it from five directions -- what the case held, why a gun
# case has a Commerce Clause holding, what the correction is, how the two
# required cases differ, and which one governs a STATE regulation -- and
# _lopez_is_commerce makes the boundary a checked property of the file.
