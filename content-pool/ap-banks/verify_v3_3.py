"""Structural gate for AP U.S. Government 3.3 First Amendment: Freedom of Speech.

Units 3 to 5 use gov345_check rather than usgov_check -- that is the convention
verify_v3_1.py and verify_v3_2.py established, and it is the right one here
because gov345_check enforces the digit-hyphen rule and the LETTER_REF rule that
this half of the course needs. On top of it this file runs the three helpers
from usgov_anchor that the Unit 1 and 2 modules use: shape, anchors and
grounding, plus the notation check, which is stricter than gov345_check's
(it catches a slash between digits as well as a hyphen).

FOUR CED PARENTHETICALS, AND ONE PAIR STUDENTS REVERSE
--------------------------------------------------------
EK 3.3.A.1 and EK 3.3.A.2 supply four definitions in their own parentheses:
symbolic speech ("nonverbal action that communicates an idea or belief"),
defamation ("language that harms the reputation of another"), LIBEL (written)
and SLANDER (oral). The libel/slander pair is reversed by students more
reliably than almost anything else in this course, and _definitions below
asserts the keyed choices still carry the framework's own assignment. Item 13
tests the pair directly and item 14 tests it in a scenario, because a student
who has the definition can still misapply it to a broadcast.

THE TAIL OF EK 3.3.A.2.iv
--------------------------
The framework does not present Schenck's clear-and-present-danger formula as
the current test. It says "restrictions on speech that create a clear and
present danger AND SUBSEQUENT INTERPRETATIONS WHICH HAVE REFINED THOSE
RESTRICTIONS." A bank that stops at 1919 teaches a standard that has since been
narrowed, and a student who recites it will overstate how easily speech may be
restricted -- which is precisely the question LO 3.3.A asks. Items 18 and 19
carry the refinement clause and _refinement asserts it survives in the module.

THE COLUMN-DIRECTION TRAP IN THE CLAIMS TABLE
-----------------------------------------------
The second column of the claims table is "claims upheld FOR THE SPEAKER". The
defamation row reads 26 of 94, which a hurried reader takes as the court being
hostile to defamation plaintiffs when it means the opposite: the person alleging
harm won most of the time. Item 26 is built on that misreading, and the check
below confirms the column header still says "for the speaker" -- because if
someone shortened it to "claims upheld", the item would become unanswerable and
nothing else would notice.
"""
import re as _re

import gov345_check as gc
import usgov_anchor as ua
import v3_3

ANCHORS = {
 1: "nonverbal action that communicates an idea or belief",
 2: "It is protected by the First Amendment",
 3: "states the protection in absolute terms",
 4: "That symbolic speech, nonverbal action communicating an idea or belief, is protected",
 5: "Tinker v. Des Moines (1969), in which a ban on students wearing black armbands",
 6: "Silently displaying a banner with no words",
 7: "covering nonverbal action required an interpretation of what counts as speech",
 8: "Efforts to balance social order and individual freedom",
 9: "limits on the time of day an event can be held, on where it can be held, and on noise levels",
 10: "restricts the circumstances of expression rather than the message expressed",
 11: "since it governs circumstances and applies without regard to the message",
 12: "language that harms the reputation of another",
 13: "Libel is written communication and slander is oral communication",
 14: "slander, since the communication was oral",
 15: "recover for reputational harm necessarily restricts what a speaker may say",
 16: "Some obscene and offensive communication, rather than all of it",
 17: "Restrictions on speech that create a clear and present danger",
 18: "Subsequent interpretations which have refined those restrictions",
 19: "will overstate how easily speech may be restricted",
 20: "A rule barring amplified sound after ten at night, with time, place and manner",
 21: "reaches beyond the immediate community",
 22: "the rights to speak and assemble are the means by which it is demanded",
 23: "a large majority of political and symbolic expression claims and a small minority",
 24: "while recognizing categories in which speech may be limited",
 25: "so a low figure in the defamation row means plaintiffs often won",
 26: "Three of the four ordinances restrict circumstances without regard to the message",
 27: "since it turns on the message",
 28: "All three: a limit on the time of day",
 29: "substantial but not unlimited",
 30: "Each category is narrow and defined",
}

GROUNDING = {
 1: "EK 3.3.A.1's own parenthesis: symbolic speech is 'nonverbal action that communicates an "
    "idea or belief.'",
 2: "EK 3.3.A.1: speech 'including symbolic speech... is protected by the First Amendment.'",
 3: "U.S. Constitution, First Amendment, quoted verbatim. The text admits no exception; "
    "EK 3.3.A.2's four limits come from interpretation.",
 4: "Tinker v. Des Moines (1969), required case, which the CED attaches to 3.3.A. CED holding: "
    "a ban on black armbands protesting the war violated the students' freedom of speech -- "
    "EK 3.3.A.1's symbolic speech.",
 5: "Tinker v. Des Moines (1969) as a SCOTUS comparison; the non-required facts are printed "
    "in the stem per CED p. 29.",
 6: "EK 3.3.A.1's definition applied: NONVERBAL is the operative word, so the four verbal and "
    "written distractors are ordinary speech rather than symbolic speech.",
 7: "EK 3.3.A.1 read against the First Amendment's text, which names speech and the press and "
    "not nonverbal expression.",
 8: "EK 3.3.A.2's opening clause: the limiting interpretations reflect 'efforts to balance "
    "social order and individual freedom.'",
 9: "EK 3.3.A.2.i's own three illustrations: time of day, where an event can be held, and "
    "noise levels.",
 10: "EK 3.3.A.2.i read for what unites its three examples -- all are circumstances rather "
     "than content.",
 11: "EK 3.3.A.2.i applied to a content-neutral permit rule.",
 12: "EK 3.3.A.2.iii's own parenthesis: defamation is 'language that harms the reputation of "
     "another.'",
 13: "EK 3.3.A.2.iii's own parentheses: libel is written communication and slander is oral. "
     "The pair students reverse.",
 14: "EK 3.3.A.2.iii applied to a broadcast: reputational harm makes it defamation, and the "
     "spoken medium makes it slander rather than libel.",
 15: "EK 3.3.A.2 lists defamation protections among interpretations 'that limit speech,' "
     "because the protection runs to the person harmed and the limit falls on the speaker.",
 16: "EK 3.3.A.2.ii's own qualifier: 'limitations on SOME obscene and offensive "
     "communication.' Dropping 'some' would make any offensive speech restrictable.",
 17: "Schenck v. United States (1919), required case, which the CED attaches to 3.3.A. CED "
     "holding: speech creating a 'clear and present danger' was not protected and could be "
     "limited -- the source of EK 3.3.A.2.iv.",
 18: "EK 3.3.A.2.iv's tail, verbatim: 'and subsequent interpretations which have refined those "
     "restrictions.' The framework treats Schenck's formula as a starting point.",
 19: "EK 3.3.A.2.iv's refinement clause read for its consequence, against LO 3.3.A's question "
     "about the EXTENT of the commitment to free speech.",
 20: "EK 3.3.A.2's four categories, each distractor misassigned: content restriction, libel, "
     "protected symbolic speech, slander.",
 21: "'Letter from a Birmingham Jail' (required document), 'Injustice anywhere is a threat to "
     "justice everywhere,' quoted verbatim; the CED attaches the Letter to 3.3.A.",
 22: "'Letter from a Birmingham Jail' (required document), 'Freedom is never voluntarily given "
     "by the oppressor,' quoted verbatim, read against the First Amendment's speech, assembly "
     "and petition clauses.",
 23: "Data item on a labelled hypothetical; all four success rates are recomputed below.",
 24: "EK 3.3.A.1 and EK 3.3.A.2 seen together as data: two high-success categories and two low "
     "ones, which neither an absolutist nor a no-protection reading would produce.",
 25: "Data item, CED skill 3.E, and specifically a column-direction trap: the second column "
     "counts outcomes FOR THE SPEAKER, so a low defamation figure means plaintiffs won.",
 26: "Data item on a labelled hypothetical; the content-neutrality column is read below.",
 27: "EK 3.3.A.2.i located in the table: the only ordinance whose application depends on what "
     "is being said falls outside the time, place and manner category.",
 28: "EK 3.3.A.2.i's three named examples located in the table's first two rows.",
 29: "LO 3.3.A's phrase 'the extent to which', answered by holding EK 3.3.A.1 and EK 3.3.A.2 "
     "together rather than choosing one.",
 30: "EK 3.3.A.2's categories are bounded, and EK 3.3.A.2.iv's refinement clause records that "
     "one has been narrowed -- which is why the extent is a matter of degree.",
}

BROUGHT, UPHELD = "Claims brought", "Claims upheld for the speaker"
POL, SYM = "Political speech in a public forum", "Symbolic expression"
DEF, DANGER = "Speech alleged to be defamatory", "Speech alleged to create imminent danger"
DEPENDS = "Does it depend on the message?"


def _rate(t, row):
    return gc.num(_cell(t, row, UPHELD)) / gc.num(_cell(t, row, BROUGHT))


def _cell(t, label, header):
    j = t["headers"].index(header)
    for r in t["rows"]:
        if r[0] == label:
            return r[j]
    raise KeyError(label)


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def q23(t):
    """Two categories succeed for the speaker far more often than the other two."""
    rates = {r[0]: _rate(t, r[0]) for r in t["rows"]}
    high = [k for k, v in rates.items() if v > 0.7]
    low = [k for k, v in rates.items() if v < 0.35]
    assert sorted(high) == sorted([POL, SYM]), f"high-success rows are {high}"
    assert sorted(low) == sorted([DEF, DANGER]), f"low-success rows are {low}"
    assert gc.num(_cell(t, POL, BROUGHT)) == max(gc.num(c) for c in _col(t, BROUGHT)), \
        "political speech is not the largest category"
    assert rates[DEF] < rates[POL], "defamation succeeds more often than political speech"
    return (f"speaker success {rates[POL]:.0%} political, {rates[SYM]:.0%} symbolic, "
            f"{rates[DEF]:.0%} defamation, {rates[DANGER]:.0%} danger")


def q24(t):
    """Neither an absolutist nor a no-protection reading fits the spread."""
    rates = [_rate(t, r[0]) for r in t["rows"]]
    assert max(rates) < 1.0, "some category succeeds every time, which absolutism would need"
    assert min(rates) > 0.0, "some category never succeeds, which no-protection would need"
    assert max(rates) - min(rates) > 0.5, "the categories are too alike to show a pattern"
    return (f"success ranges {min(rates):.0%} to {max(rates):.0%}, so neither extreme reading "
            "fits the table")


def q25(t):
    """The column counts outcomes FOR THE SPEAKER, which is the item's whole point."""
    assert "for the speaker" in UPHELD, "the column no longer says whose claims were upheld"
    assert UPHELD in t["headers"], "the speaker column is missing"
    losses = gc.num(_cell(t, DEF, BROUGHT)) - gc.num(_cell(t, DEF, UPHELD))
    assert losses > gc.num(_cell(t, DEF, UPHELD)), \
        "speakers win most defamation claims, so the misreading the item targets is not available"
    return (f"defamation: {gc.num(_cell(t, DEF, UPHELD)):.0f} of "
            f"{gc.num(_cell(t, DEF, BROUGHT)):.0f} upheld for the SPEAKER, so the party "
            f"alleging harm prevailed {losses:.0f} times")


def q26(t):
    """Three ordinances are content neutral and one is not."""
    dep = _col(t, DEPENDS)
    assert dep.count("No") == 3 and dep.count("Yes") == 1, f"content column reads {dep}"
    yes_row = t["rows"][dep.index("Yes")][0]
    assert "criticizing" in yes_row, f"the content-based row is {yes_row!r}"
    return "three ordinances content neutral, one content based (the council-criticism rule)"


def q27(t):
    """The only content-based ordinance is the one that cannot be a time/place/manner rule."""
    dep = _col(t, DEPENDS)
    assert dep.count("Yes") == 1, "more than one ordinance depends on the message"
    for row, d in zip(t["rows"], dep):
        if d == "No":
            assert row[1] in ("Manner and time", "Place", "Manner"), \
                f"a content-neutral row restricts {row[1]!r}, which is not a circumstance"
    return "the three content-neutral rows restrict time, place or manner only"


def q28(t):
    """All three of the CED's own examples appear across the first two rows."""
    first, second = t["rows"][0][0].lower(), t["rows"][1][0].lower()
    assert "after ten at night" in first, "the time-of-day example is missing"
    assert "sound" in first, "the noise-level example is missing"
    assert "inside the courthouse" in second, "the place example is missing"
    return "time of day and noise level in row one, place in row two"


def _definitions(module):
    """The CED's four parentheticals must survive in the keys that test them."""
    bad = []
    pairs = {
        1: "nonverbal action that communicates an idea or belief",
        12: "language that harms the reputation of another",
        13: "Libel is written communication and slander is oral communication",
    }
    for i, phrase in pairs.items():
        key = module.QUESTIONS[i - 1]["choices"][module.QUESTIONS[i - 1]["ans"]]
        if phrase not in key:
            bad.append(f"q{i}: the CED's own wording {phrase!r} is no longer in the key")
    # Nowhere in the module may libel be ASSERTED to be oral, or slander written.
    #
    # Narrow on purpose. The first version of this loop flagged any sentence
    # containing "libel" and "oral" without "written", and fired on item 14's
    # rationale -- "the medium being spoken makes it slander rather than libel" --
    # which states the rule CORRECTLY and mentions both words while doing it. That
    # is the over-matching checker this project keeps rebuilding. What must never
    # appear is the assertion itself, so the patterns below require the two words
    # to be joined by a copula.
    wrong = [r"libel[^.]{0,20}\bis\b[^.]{0,20}oral",
             r"oral[^.]{0,20}\bis\b[^.]{0,20}libel",
             r"slander[^.]{0,20}\bis\b[^.]{0,20}written",
             r"written[^.]{0,20}\bis\b[^.]{0,20}slander"]
    for i, item in enumerate(module.QUESTIONS, 1):
        for label, s in (("key", item["choices"][item["ans"]]), ("why", item["why"])):
            low = s.lower()
            for pat in wrong:
                m = _re.search(pat, low)
                if m:
                    bad.append(f"q{i} {label}: {m.group(0)!r} reverses EK 3.3.A.2.iii's "
                               "assignment of libel to written and slander to oral")
    if bad:
        print(f"FAIL {module.__name__} definitions")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} definitions: symbolic speech, defamation, libel and slander "
          "all keep the CED's own wording, and the libel/slander pair is never reversed")


def _refinement(module):
    """EK 3.3.A.2.iv's tail must appear; Schenck is not presented as the current test."""
    blob = " ".join(it["q"] + " " + it["why"] + " " + " ".join(it["choices"])
                    for it in module.QUESTIONS).lower()
    bad = []
    if "refined those restrictions" not in blob:
        bad.append("EK 3.3.A.2.iv's clause 'subsequent interpretations which have refined "
                   "those restrictions' appears nowhere; without it the module presents the "
                   "1919 formula as the current test")
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        if "clear and present danger" in key and "current test" in key:
            bad.append(f"q{i} key: calls the clear and present danger formula the current test")
    if bad:
        print(f"FAIL {module.__name__} refinement")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} refinement: EK 3.3.A.2.iv's refinement clause is present and "
          "no key presents the 1919 formula as the standard that governs today")


ua.shape(v3_3)
ua.check(v3_3, ANCHORS, GROUNDING)
ua.notation(v3_3)
_definitions(v3_3)
_refinement(v3_3)
gc.check(v3_3, arith={23: q23, 24: q24, 25: q25, 26: q26, 27: q27, 28: q28})

# WHAT THE REVIEW FOUND
# ---------------------
# No wrong key. Two things are recorded here because they would be invisible to
# a later reader otherwise.
#
# First, the claims table's second column is headed "Claims upheld FOR THE
# SPEAKER", and the whole of item 25 depends on those three words. The
# defamation row reads 26 of 94, which looks like a court hostile to defamation
# claims and means the reverse -- the person alleging harm won 68 times. If
# anyone shortens the header to "Claims upheld", every other item still works
# and item 25 becomes unanswerable, so q25's arithmetic asserts the header text
# itself rather than only the numbers under it.
#
# Second, this is the first Unit 3 module written in this session, and it runs
# BOTH checkers: gov345_check, which Units 3 to 5 use and which enforces the
# digit-hyphen and LETTER_REF rules, and the usgov_anchor helpers built for
# Units 1 and 2. The two are complementary rather than redundant -- gov345_check
# has the notation and letter-reference rules usgov_check lacks, and
# usgov_anchor has the shape, anchor and grounding maps gov345_check lacks.
# Later Unit 3 to 5 modules should follow this pattern rather than choosing one.
