"""Key audit for AP U.S. HISTORY 4.2 The Rise of Political Parties and the Era of Jefferson.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The shared gate is
``wh_check.run``.

WHAT THE KEYS REST ON
---------------------
  Unit 4 Learning Objective B, causes and effects
    of policy debates in the early republic       items 1, 13, 14, 20, 21, 22, 23
  KC-4.1.I.A, national parties continued to
    debate the tariff, federal power and
    relations with European powers                2, 3, 4, 17, 25, 26, 27, 30
  KC-4.1.I.B, judicial primacy in determining
    the Constitution's meaning, and federal law
    taking precedence over state law              5, 6, 7, 18, 26, 28, 30
  KC-4.3.I.A.i, influence and control over North
    America by exploration and diplomacy after
    the Louisiana Purchase                        8, 9, 10, 11, 25, 29, 30
  KC-4.1.I, parties growing beside an expanded
    suffrage                                      4, 24
  KC-4.3.I, territory and foreign trade           11, 25
  the Politics and Power thematic focus           12
  skill 2.A against 2.B, and the Causation
    reasoning process                             13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23

WHAT IS NOT ASSERTED. The CED names the Louisiana Purchase and Supreme Court
decisions without naming a seller, a price, a year or a case. Neither does this
module, and no key rests on the author's knowledge of the early republic.

THE SWAP ITEMS. Several distractors are the key with one clause reversed rather
than an unrelated claim: item 6 exchanges federal and state law, item 8
exchanges the region and the ordering against the acquisition, item 11 exchanges
the general concept with the sub-point beneath it, item 14 exchanges the verbs
of skills 2.A and 2.B, and item 29's alternatives exchange which column rises.
Those anchors carry BOTH clauses, the defect ``verify_e2_1.py`` shipped.

DATA ITEMS: 27, 28 and 29 carry tables of explicitly hypothetical figures. Each
check recomputes the keyed claim and falsifies every distractor from the same
rows FIRST, and only then compares the rows against the literal list stated
here. The order is deliberate and is the point a1_1's verifier makes about
categorical tables: the shared corrupter appends text, which a semantic guard on
a category cannot always see, so the literal list is what makes every cell
load-bearing -- but if it ran first, a control that exchanges a category would
raise on row equality and prove nothing about the guard it names.

NEGATIVE CONTROLS: ``python3 verify_a4_2.py --selftest``.
"""
import sys

import cg_check as cg
import wh_check
import wh_stimulus
import a4_2

PARTY_ONE = "Essays published by one national party"
PARTY_TWO = "Essays published by the other national party"
SUBJECT = "What the dispute was about"
PREVAILED = "Which law the decision held to prevail"
EXPLORE = "Missions sent to explore the interior"
NEGOTIATE = "Missions sent to negotiate with other governments"

_EXPECTED_DEBATE = [
    ["The tariff", "41", "37"],
    ["Powers of the federal government", "58", "52"],
    ["Relations with European powers", "33", "44"],
]

_EXPECTED_COURT = [
    ["Decision 1", "A federal duty and a conflicting state duty", "The federal law"],
    ["Decision 2", "A federal licence and a conflicting state licence", "The federal law"],
    ["Decision 3", "The meaning of a clause of the Constitution", "The federal law"],
    ["Decision 4", "A federal rule and a conflicting state rule", "The federal law"],
]

_EXPECTED_MEANS = [
    ["1790 to 1800", "1", "2"],
    ["1800 to 1810", "6", "7"],
    ["1810 to 1820", "9", "11"],
    ["1820 to 1830", "14", "16"],
]


def _rows_are(table, expected, what):
    assert [list(r) for r in table["rows"]] == expected, (
        f"the {what} table does not hold the rows this check was written against; "
        f"got {table['rows']}"
    )


def q27(table, item):
    """Both parties publish on all three issues; neither leads on all three."""
    labs = cg.labels(table)
    assert labs == ["The tariff", "Powers of the federal government",
                    "Relations with European powers"], \
        f"the three issues KC-4.1.I.A names are not the rows: {labs}"
    one, two = cg.col(table, PARTY_ONE), cg.col(table, PARTY_TWO)
    assert all(v > 0 for v in one + two), (
        f"the key needs both parties to have published on every issue; got {one} and {two}"
    )
    both = [i for i in range(len(one)) if one[i] > 0 and two[i] > 0]
    assert len(both) == len(labs), \
        f"'only one issue drew essays from both parties' must be false; {len(both)} did"
    totals = [o + t for o, t in zip(one, two)]
    assert totals[2] < max(totals[0], totals[1]), (
        f"'relations with European powers drew more essays in total' must be false; "
        f"totals are {totals}"
    )
    leads_one = [o > t for o, t in zip(one, two)]
    assert not all(leads_one) and any(leads_one), (
        f"'the same party published more on every issue' must be false; the first column "
        f"leads on {sum(leads_one)} of {len(labs)} issues"
    )
    _rows_are(table, _EXPECTED_DEBATE, "essay count")
    return (f"all six cells are positive, the three totals run {totals}, and the first "
            f"column leads on {sum(leads_one)} of the three issues rather than all of them")


def q28(table, item):
    """Every recorded decision resolves in favour of the federal law."""
    labs = cg.labels(table)
    assert labs == [f"Decision {n}" for n in range(1, 5)], \
        f"the four decisions the choices speak of are not the rows: {labs}"
    prevailed = [cg.normalize(r[table["headers"].index(PREVAILED)]) for r in table["rows"]]
    federal = [p == "the federal law" for p in prevailed]
    assert all(federal), (
        f"the key needs every recorded decision to hold the federal law to prevail; "
        f"got {prevailed}"
    )
    assert not any(p == "the state law" for p in prevailed), \
        "'in every recorded decision the state law prevailed' must be false"
    assert len(set(prevailed)) == 1, \
        "'the decisions divide evenly between federal and state law' must be false"
    subjects = [cg.normalize(r[table["headers"].index(SUBJECT)]) for r in table["rows"]]
    conflicts = [s for s in subjects if "conflicting" in s]
    assert len(conflicts) == 3, (
        f"'only one of the disputes involved a conflict of laws' must be false; "
        f"{len(conflicts)} rows record a conflict"
    )
    assert len(set(subjects)) == len(subjects), \
        "'every dispute concerned the same subject' must be false"
    _rows_are(table, _EXPECTED_COURT, "decision")
    return (f"all four rows name the federal law as prevailing, {len(conflicts)} of them "
            f"over a conflicting state measure, across four distinct subjects")


def q29(table, item):
    """Exploring and negotiating missions both rise across the four decades."""
    labs = cg.labels(table)
    assert labs == ["1790 to 1800", "1800 to 1810", "1810 to 1820", "1820 to 1830"], \
        f"the four decades the item speaks of are not the rows: {labs}"
    explore, negotiate = cg.col(table, EXPLORE), cg.col(table, NEGOTIATE)
    rising_e = all(explore[i + 1] > explore[i] for i in range(len(explore) - 1))
    rising_n = all(negotiate[i + 1] > negotiate[i] for i in range(len(negotiate) - 1))
    assert rising_e and rising_n, (
        f"the key needs BOTH columns to rise at every step; got {explore} and {negotiate}"
    )
    assert not any(explore[i + 1] < explore[i] for i in range(len(explore) - 1)), \
        "'exploring missions decline' must be false"
    assert not any(negotiate[i + 1] < negotiate[i] for i in range(len(negotiate) - 1)), \
        "'negotiating missions decline' must be false"
    assert len(set(explore)) > 1 and len(set(negotiate)) > 1, \
        "'neither kind of mission changes' must be false"
    ahead = [e > n for e, n in zip(explore, negotiate)]
    assert not any(ahead), (
        f"'exploring missions outnumber negotiating missions in every decade' must be "
        f"false; the exploring column leads in {sum(ahead)} of {len(labs)} decades"
    )
    _rows_are(table, _EXPECTED_MEANS, "mission")
    return (f"exploring missions run {explore} and negotiating missions {negotiate}, both "
            f"rising at every step with the negotiating column always the larger")


TABLE_CHECKS = {27: q27, 28: q28, 29: q29}

CLAIMS = [
 ("causes and effects of policy debates",
  "Unit 4 Learning Objective B reads 'Explain the causes and effects of policy debates in the early republic', which is why Causation is this topic's reasoning process."),
 ("tariff, powers of the federal government, and relations with European powers",
  "KC-4.1.I.A names exactly these three as the issues national political parties continued to debate in the early 1800s; the extension of slavery belongs to KC-4.3.II instead."),
 ("carried on from before the early 1800s",
  "KC-4.1.I.A's verb CONTINUED places the debates as ongoing rather than newly begun, which the framework's periodisation note also allows for."),
 ("National political parties",
  "KC-4.1.I.A assigns the debates to national political parties, whose growth KC-4.1.I places beside the expansion of suffrage; courts are the subject of KC-4.1.I.B."),
 ("primacy of the judiciary in determining the meaning of the Constitution",
  "KC-4.1.I.B states that Supreme Court decisions established exactly this primacy, and assigns it to no other branch."),
 ("federal laws took precedence over state laws",
  "KC-4.1.I.B's second assertion, verbatim. The anchor carries both bodies of law in the framework's own order because the leading distractor exchanges them."),
 ("interpretation rather than enforcement",
  "KC-4.1.I.B speaks of the primacy of the judiciary in DETERMINING THE MEANING of the Constitution, which is interpretation; the sentence assigns enforcement to nobody."),
 ("North America, following the Louisiana Purchase",
  "KC-4.3.I.A.i names both the region and the ordering: following the Louisiana Purchase, the U.S. government sought influence and control over North America. The anchor carries both because one distractor changes the region and another the ordering."),
 ("Exploration and diplomatic efforts",
  "KC-4.3.I.A.i names exploration and diplomatic efforts among the variety of means the government used."),
 ("rested on a single instrument of policy",
  "KC-4.3.I.A.i's phrase 'a variety of means' asserts more than one instrument, so a single-instrument account is the reading it excludes; the rejected options are things the sentence states."),
 ("KC-4.3.I states the general aim of claiming territory and promoting trade",
  "KC-4.3.I is the broader concept and KC-4.3.I.A.i sits beneath it as one way the aim was pursued. The anchor carries both halves because the leading distractor exchanges the two levels."),
 ("Government policy, institutions, political parties, and the rights of citizens",
  "The Politics and Power thematic focus printed on this topic's page names exactly these four as the things debates about the role of government shape, and Unit 4 Learning Objective B asks for the causes and effects of those debates."),
 ("Identify a source's point of view",
  "Skill 2.A as printed beside this topic's title; the rejected options are skills 2.B, 2.C, 3.B and 3.C, and Unit 4 Learning Objective B is the objective 2.A serves here."),
 ("those features and 2.B asks the student to explain them",
  "The framework prints 2.A under IDENTIFY and 2.B under EXPLAIN with the same four features, so the verb is the whole difference. The anchor carries both halves because the leading distractor exchanges the verbs, and Unit 4 Learning Objective B is served by 2.A here."),
 ("addresses itself to the voters of one state",
  "Skill 2.A separates audience from point of view, purpose and historical situation; whom a source addresses is its audience, and KC-4.1.I.A supplies the debate over federal power that the source joins."),
 ("persuade merchants to accept the restriction",
  "Under skill 2.A the purpose is what a source sets out to do. KC-4.1.I.A names relations with European powers among the issues under debate, which is the situation rather than the purpose."),
 ("while the national parties were debating the duty",
  "Under skill 2.A the historical situation is the circumstance of production, and KC-4.1.I.A places the tariff among the issues national political parties continued to debate in the early 1800s."),
 ("approves of federal law prevailing over state law",
  "Under skill 2.A the point of view is the position a source takes, and the position here is approval of the precedence KC-4.1.I.B describes."),
 ("position from which the source speaks",
  "Skill 2.A lists point of view separately from purpose, situation and audience, and skill 2.C asks how such features might limit a source's uses, which presumes the position shapes the account. Unit 4 Learning Objective B applies the skill to policy debates."),
 ("Causation, which involves describing causes and effects",
  "The unit's table prints Causation as this topic's reasoning process, matching Unit 4 Learning Objective B, and the framework defines it as describing causes and effects and explaining the relationship between them."),
 ("Primary against secondary causes",
  "Aspect 2.iii of the Causation reasoning process asks students to explain the difference between primary and secondary causes and between short and long term effects; Unit 4 Learning Objective B is what it is applied to here."),
 ("relative historical significance of different causes and effects",
  "Aspect 2.v of the Causation reasoning process asks for the relative historical significance of different causes and effects, so the framework asks for a weighing rather than treating all causes alike. Unit 4 Learning Objective B supplies the debates being weighed."),
 ("relevant context influenced a specific historical development",
  "Aspect 2.iv of the Causation reasoning process runs from context to development, and Unit 4 Learning Objective B is what it is applied to here. The anchor carries the direction because the leading distractor reverses it, and identifying a context is skill 4.A rather than a causation aspect."),
 ("transition to a more participatory democracy through an expanded suffrage",
  "KC-4.1.I places the growth of political parties alongside the transition to a more participatory democracy achieved by expanding suffrage, which is the growth KC-4.1.I.A shows at work in policy debate."),
 ("influence and control over North America after a territorial acquisition",
  "KC-4.3.I.A.i sits under KC-4.3, the foreign-policy key concept, while the rejected options come from KC-4.1.I.A, KC-4.1.I.B and KC-4.1.I and concern politics and law inside the republic."),
 ("continuing to debate those powers",
  "KC-4.1.I.A has national political parties continuing to debate the powers of the federal government while KC-4.1.I.B records the judiciary's primacy in reading the Constitution, so the framework holds both without making one end the other."),
 ("published essays on all three issues",
  "Recomputed in q27 from the table alone: every cell is positive, so both parties published on each issue, which is the pattern KC-4.1.I.A describes when it names three issues national political parties continued to debate."),
 ("every recorded decision the federal law was held to prevail",
  "Recomputed in q28 from the table alone: the final column names the federal law in all four rows. KC-4.1.I.B states that Supreme Court decisions asserted that federal laws took precedence over state laws."),
 ("Both kinds of mission increase",
  "Recomputed in q29 from the table alone: both columns rise at every step. KC-4.3.I.A.i describes a variety of means including exploration and diplomatic efforts, so the anchor carries both kinds because the distractors exchange which one rises."),
 ("court decisions gave the judiciary primacy in reading the Constitution",
  "The keyed sentence collects KC-4.1.I.A, KC-4.1.I.B and KC-4.3.I.A.i in the order the topic page prints them and adds nothing; each rejected version negates one of the three or moves it to another period."),
]


def _extra_mutations():
    def a_state_law_prevails(mod, cl):
        # Exchange one decision's outcome. Row equality would catch it too, which
        # is why the uniformity guard is written FIRST in q28: this control must
        # fire on the claim the item makes, not on a bookkeeping assertion.
        t = mod.QUESTIONS[27]["table"]
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][2][2] = "The state law"

    def exploring_missions_fall(mod, cl):
        t = mod.QUESTIONS[28]["table"]
        t["rows"] = [list(r) for r in t["rows"]]
        for row, value in zip(t["rows"], ["14", "9", "6", "1"]):
            row[1] = value

    def one_party_silent_on_an_issue(mod, cl):
        t = mod.QUESTIONS[26]["table"]
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][2][2] = "0"

    return [
        ("a decision recorded as holding the state law to prevail", a_state_law_prevails),
        ("the exploring column reversed so it falls across the four decades",
         exploring_missions_fall),
        ("one party recorded as publishing nothing on one of the three issues",
         one_party_silent_on_an_issue),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    wh_stimulus.controls(a4_2)
    for label, mutate in _extra_mutations():
        mod = wh_check._mutant(a4_2)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            wh_check.history_style(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as e:
            print(f"  control OK  {label}: {str(e)[:110]}")
        else:
            raise SystemExit(f"CONTROL FAILED: {label} did not raise")

wh_check.run(a4_2, CLAIMS, TABLE_CHECKS, sys.argv)
