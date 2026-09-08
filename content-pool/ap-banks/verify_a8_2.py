"""Key audit for AP U.S. HISTORY 8.2 The Cold War from 1945 to 1980.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states the CED sentence the key rests on, with its Key Concept code, for a human
to audit. ``wh_check`` refuses any ``why`` or ``claim`` citing neither a KC code
nor a Learning Objective, because a key traceable only to an author's knowledge
of the twentieth century cannot be checked by anyone reading this bank later.

WHAT THE KEYS REST ON -- four sentences and one Learning Objective, and nothing
else. This topic's page also carries a long OPTIONAL SOURCES list naming real
telegrams, speeches and interviews; the CED says of it that those sources "are
not required AP course content" and that no exam question requires them. So no
key here names a document, a policymaker or a programme.

  Unit 8 Learning Objective B, continuities and
    changes from 1945 to 1980                        items 1, 8, 14, 24, 30
  KC-8.1.I, the aims and the authoritarian Soviet
    Union                                            2, 8, 13, 23, 25, 30
  KC-8.1.I.A, alliance dissolved; collective
    security, aid, economic institutions             3, 4, 11, 12, 18, 20, 27, 28
  KC-8.1.I.B.i, the two concerns, a variety of
    measures, Korea                                  5, 6, 19, 21, 25, 30
  KC-8.1.I.C, fluctuation between confrontation
    and mutual coexistence                           7, 8, 9, 15, 17, 26, 29
  skill 2.C, and how a source's features limit its
    use                                              10, 12, 13, 14, 15, 19, 24

THE SWAP ITEMS, where a distractor exchanges the halves of the key, so the
anchor has to carry BOTH clauses or it would match the distractor too:
  q3   the alliance dissolved by tension, not by a formal act
  q4   institutions bolstering non-Communist nations, not every nation equally
  q13  strong evidence of intentions AND weak evidence of conditions
  q18  more nations receiving aid than bound by security agreements
  q21  the concern is the reason and containment the method, not the reverse

DATA ITEMS: 16, 17 and 18. Each table check runs its DERIVED assertions first --
the ones that carry the keyed claim -- and only then a literal guard on the rows
the check was written against. The order is deliberate: a corruption that breaks
the key raises on the assertion that names it, and the literal guard exists only
so that a corruption which does NOT break the key is still caught rather than
leaving a cell silently undefended. ``_T_PHASES`` is categorical, so without the
literal guard the shared corrupter (which appends text) would catch 0 of its 8
cells, which the harness rightly refuses.

NEGATIVE CONTROLS: ``python3 verify_a8_2.py --selftest``. Besides the shared
battery it runs three targeted controls that must raise on the DERIVED guard and
not on the literal one: the falling aid category made to rise, the alternation of
phases broken, and the two counts of nations crossed over.
"""
import sys

import wh_check
import wh_stimulus as ws
import a8_2

CATEGORY = "Category of assistance (hypothetical record)"
Y1948 = "Amount recorded in 1948 (units)"
Y1958 = "Amount recorded in 1958 (units)"
STRETCH = "Stretch of years (hypothetical record)"
CHARACTER = "Character the record assigns to it"
YEAR = "Year (hypothetical record)"
SECURITY = "Nations bound by recorded collective security agreements"
AID = "Nations receiving recorded international aid"


def _col(table, header):
    idx = table["headers"].index(header)
    return [row[idx] for row in table["rows"]]


def _nums(table, header):
    return [float(v.replace(",", "")) for v in _col(table, header)]


_EXPECTED_AID = [
    ["Collective security commitments", "120", "260"],
    ["International aid", "300", "180"],
    ["Support for economic institutions", "90", "210"],
]


def q16(table, item):
    early, late = _nums(table, Y1948), _nums(table, Y1958)
    risers = [i for i in range(len(early)) if late[i] > early[i]]
    fallers = [i for i in range(len(early)) if late[i] < early[i]]
    assert len(risers) == 2 and len(fallers) == 1, (
        f"the key needs two categories rising and one falling; got {len(risers)} rising and "
        f"{len(fallers)} falling, from {early} to {late}"
    )
    assert sum(late) > sum(early), (
        f"the key says the recorded total is larger in the later year; got {sum(early)} then "
        f"{sum(late)}"
    )
    assert all(v > 0 for v in late), (
        f"'one recorded category falls to nothing' must be false; the later year holds {late}"
    )
    assert len(set(early)) > 1 or len(set(late)) > 1, \
        "'the three categories are recorded at equal amounts' must be false"
    # Literal guard LAST, so a corruption that breaks the key above raises there.
    assert [list(r) for r in table["rows"]] == _EXPECTED_AID, (
        f"the assistance table does not hold the rows this check was written against; "
        f"got {table['rows']}"
    )
    return (f"amounts move from {early} to {late}: {len(risers)} categories rise, "
            f"{len(fallers)} falls, none to nothing, and the total rises from {sum(early)} "
            f"to {sum(late)}")


_EXPECTED_PHASES = [
    ["1948 to 1953", "Direct or indirect military confrontation"],
    ["1954 to 1958", "Mutual coexistence"],
    ["1959 to 1963", "Direct or indirect military confrontation"],
    ["1964 to 1968", "Mutual coexistence"],
]


def q17(table, item):
    chars = [c.strip() for c in _col(table, CHARACTER)]
    assert len(set(chars)) == 2, (
        f"'three or more distinct characters' and 'the same character throughout' must both be "
        f"false, so exactly two distinct characters must appear; got {sorted(set(chars))}"
    )
    assert all(a != b for a, b in zip(chars, chars[1:])), (
        f"the key says the character ALTERNATES from one stretch to the next; got {chars}"
    )
    assert all(c for c in chars), f"every stretch must carry a character; got {chars}"
    # A single change and then a hold would give two distinct characters with no
    # repetition of the first, so the return to it is what distinguishes
    # fluctuation from one transition.
    assert chars[0] == chars[2] and chars[1] == chars[3], (
        f"'the record moves once and then holds' must be false, so the first character must "
        f"recur later in the record; got {chars}"
    )
    assert [list(r) for r in table["rows"]] == _EXPECTED_PHASES, (
        f"the phase table does not hold the rows this check was written against; "
        f"got {table['rows']}"
    )
    return (f"the four stretches carry {chars}, exactly two distinct characters alternating "
            f"and each recurring, which is fluctuation rather than a single change")


_EXPECTED_ENGAGE = [
    ["1947", "5", "8"],
    ["1952", "14", "21"],
    ["1957", "22", "29"],
    ["1962", "27", "34"],
]


def q18(table, item):
    years, sec, aid = _nums(table, YEAR), _nums(table, SECURITY), _nums(table, AID)
    steps = [b - a for a, b in zip(years, years[1:])]
    assert steps == [5, 5, 5], f"the record must run at five-year steps; the steps are {steps}"
    assert all(b > a for a, b in zip(sec, sec[1:])), (
        f"'the count bound by security agreements falls at least once' must be false; got {sec}"
    )
    assert all(b > a for a, b in zip(aid, aid[1:])), (
        f"'the count receiving aid falls at least once' must be false; got {aid}"
    )
    # BOTH clauses of the key, because the swapped distractor keeps the first.
    assert all(a > s for s, a in zip(sec, aid)), (
        f"the key says more nations receive aid than are bound by security agreements in every "
        f"year; got security {sec} against aid {aid}"
    )
    assert all(a != s for s, a in zip(sec, aid)), \
        "'the two counts are equal in every year' must be false"
    assert [list(r) for r in table["rows"]] == _EXPECTED_ENGAGE, (
        f"the engagement table does not hold the rows this check was written against; "
        f"got {table['rows']}"
    )
    return (f"security counts run {sec} and aid counts run {aid}, both rising at every "
            f"five-year step, with aid above security in all four years")


TABLE_CHECKS = {16: q16, 17: q17, 18: q18}

CLAIMS = [
 ("continuities and changes in Cold War policies",
  "Unit 8 Learning Objective B reads 'Explain the continuities and changes in Cold War policies from 1945 to 1980'; the distractors are Learning Objectives C, H, I and A of the same unit."),
 ("Communist military power and ideological influence",
  "KC-8.1.I names both forms of growth policymakers sought to limit: Communist military power and ideological influence."),
 ("Soviet Union, dissolved by postwar tensions",
  "KC-8.1.I.A opens 'As postwar tensions dissolved the wartime alliance between Western democracies and the Soviet Union'. The anchor carries the alliance and its dissolving agent together, because a distractor keeps the alliance and substitutes a formal act."),
 ("economic institutions that bolstered non-Communist nations",
  "KC-8.1.I.A names collective security, international aid, and economic institutions that bolstered non-Communist nations. The anchor carries the qualification because a distractor keeps all three headings and makes the institutions serve every nation equally."),
 ("Expansionist Communist ideology and Soviet repression",
  "KC-8.1.I.B.i opens 'Concerned by expansionist Communist ideology and Soviet repression', giving a doctrine and a practice together as the reason for containment."),
 ("one kind of measure among several",
  "KC-8.1.I.B.i says containment was sought through a variety of measures, INCLUDING major military engagements in Korea, so the engagements are an instance rather than the whole."),
 ("fluctuated between periods of direct and indirect military confrontation",
  "KC-8.1.I.C states that the Cold War fluctuated between periods of direct and indirect military confrontation and periods of mutual coexistence."),
 ("aim of limiting Communist power persisted, while the level of confrontation rose and fell",
  "KC-8.1.I states the aims and reports no abandonment of them, and KC-8.1.I.C makes the confrontation fluctuate; a persisting purpose against a varying intensity is the continuity and change Unit 8 Learning Objective B asks for. The anchor carries both halves because a distractor exchanges them."),
 ("conducted at a remove as well as those between the two powers themselves",
  "KC-8.1.I.C groups direct AND indirect military confrontation on one side of its contrast and mutual coexistence on the other, so indirect confrontation counts as confrontation."),
 ("including how these might limit the use or uses of a source",
  "Skill 2.C as printed beside this topic and practised in meeting Unit 8 Learning Objective B; skill 2.B, offered as the near-neighbour distractor, stops at explaining a source's features and does not reach their limiting effect."),
 ("postwar tensions dissolving the wartime alliance",
  "KC-8.1.I.A is the sentence joining the dissolution of the wartime alliance to a foreign policy based on collective security, international aid and economic institutions, which is the pair of claims the hypothetical dispatch makes."),
 ("interest in the aid programme appearing successful",
  "KC-8.1.I.A makes international aid a basis of United States foreign policy, and skill 2.C asks how a source's point of view might limit its use; an author reporting on a programme his own government funds has a stake in the finding."),
 ("wished such audiences to believe and weak evidence of conditions themselves",
  "KC-8.1.I names limiting Communist ideological influence among the aims of policy, and skill 2.C ties purpose to use. The anchor carries both halves because a distractor keeps the purpose and reverses what the source is good evidence of."),
 ("weighed against each other rather than either taken as the whole policy",
  "Skill 2.C makes audience one of the features whose significance a student must explain, and Unit 8 Learning Objective B asks about policy across a span that no single document covers."),
 ("phase of the Cold War in which confrontation had eased",
  "KC-8.1.I.C states that the Cold War fluctuated between confrontation and periods of mutual coexistence, so a source made in one phase is evidence for that phase; coexistence in the framework's sense is a phase of the Cold War, not its end."),
 ("rise while the third falls, and the recorded total is larger in the later year",
  "Recomputed in q16 from the table alone, with every rejected reading falsified against the same rows. KC-8.1.I.A names collective security, international aid and economic institutions together, so a shifting mix among them is a change of method rather than of purpose."),
 ("alternates from one stretch to the next rather than changing once",
  "Recomputed in q17 from the table alone. KC-8.1.I.C states that the Cold War fluctuated between periods of confrontation and periods of mutual coexistence, and alternation is what fluctuation looks like set out stretch by stretch."),
 ("more nations receive aid than are bound by security agreements",
  "Recomputed in q18. KC-8.1.I.A names collective security and international aid as two bases of one foreign policy; the anchor carries the direction of the comparison because a distractor reverses it while keeping the rest."),
 ("recorded long after the events, so memory and later knowledge",
  "KC-8.1.I.B.i names major military engagements in Korea among the containment measures, so the subject is inside the topic; skill 2.C locates the limitation in the source's historical situation rather than in its being testimony."),
 ("annexation of territory from defeated states",
  "KC-8.1.I.A names collective security, international aid and economic institutions bolstering non-Communist nations, and opens with the postwar tensions that dissolved the wartime alliance; annexation appears nowhere in it."),
 ("was the reason, and containment through a variety of measures was the method",
  "KC-8.1.I.B.i puts concern at expansionist Communist ideology and Soviet repression in the causal position and containment in the instrumental one. The anchor spans the whole relation because a distractor exchanges the two roles."),
 ("develops part of the engagement in a cold war that KC-8.1.I states in general terms",
  "KC-8.1.I states the engagement and its aims generally; KC-8.1.I.A, KC-8.1.I.B.i and KC-8.1.I.C each add detail beneath it, which is what a lettered sub-point does in this framework."),
 ("creating a free-market global economy",
  "KC-8.1.I lists creating a free-market global economy among the aims policymakers pursued, which is what a request to help rebuild foreign markets bears on; exposing suspected communists at home is KC-8.1.II.A and belongs to topic 8.3."),
 ("cannot by itself show what held across the whole span",
  "Unit 8 Learning Objective B asks for continuities and changes across 1945 to 1980, a claim about a span; skill 2.C makes a source's historical situation a limit on its use, and the limit here is reach rather than kind."),
 ("solely through military engagement",
  "KC-8.1.I.B.i says containment was sought through a variety of measures INCLUDING major military engagements, which makes fighting one measure among several; the four rejected statements restate KC-8.1.I.A, KC-8.1.I.C and KC-8.1.I."),
 ("fluctuation between confrontation and periods of mutual coexistence",
  "KC-8.1.I.C asserts a shape -- movement back and forth -- that a steady increase in hostility does not have, which is why it and not the topic's other sentences corrects the summary."),
 ("directed by the terms of the Cold War division",
  "KC-8.1.I.A specifies that the economic institutions bolstered NON-COMMUNIST nations, naming the recipients by their side of the division KC-8.1.I describes."),
 ("Collective security",
  "KC-8.1.I.A names collective security first among the bases of the foreign policy the United States developed, and an undertaking to treat an attack on one as an attack on all is what the phrase describes."),
 ("fluctuation KC-8.1.I.C describes between confrontation",
  "KC-8.1.I.C states that the Cold War fluctuated between periods of direct and indirect military confrontation and periods of mutual coexistence, which is what two sources eighteen years apart urging opposite courses illustrate."),
 ("steady set of aims pursued by several kinds of measure",
  "KC-8.1.I supplies the aims, KC-8.1.I.A and KC-8.1.I.B.i the several kinds of measure, and KC-8.1.I.C the varying intensity; the conjunction is what Unit 8 Learning Objective B asks students to explain."),
]


def _targeted_controls():
    """Each must raise on the DERIVED guard it names, not on the literal backstop."""
    def falling_category_rises(mod, cl):
        t = dict(mod.QUESTIONS[15]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][1][2] = "460"          # international aid now rises too
        mod.QUESTIONS[15]["table"] = t

    def alternation_broken(mod, cl):
        t = dict(mod.QUESTIONS[16]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][2][1] = "Mutual coexistence"   # one change, then a hold
        mod.QUESTIONS[16]["table"] = t

    def counts_cross_over(mod, cl):
        t = dict(mod.QUESTIONS[17]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][3][1] = "40"           # security overtakes aid in the last year
        mod.QUESTIONS[17]["table"] = t

    return [
        ("the falling assistance category made to rise, so q16's keyed two-and-one fails",
         falling_category_rises, "two categories rising and one falling"),
        ("the phase record made to change once and hold, so q17's keyed alternation fails",
         alternation_broken, "ALTERNATES from one stretch to the next"),
        ("security agreements made to overtake aid, so q18's keyed comparison fails",
         counts_cross_over, "more nations receive aid than are bound"),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    ws.controls(a8_2)
    import cg_check as cg
    for label, mutate, expect in _targeted_controls():
        mod = wh_check._mutant(a8_2)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            wh_check.history_style(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as e:
            # A control that fires for the wrong reason proves nothing about the
            # guard it names, so the message is checked and not merely the fact.
            assert expect in str(e), (
                f"CONTROL FIRED FOR THE WRONG REASON: {label} -- {e}")
            print(f"  control OK  {label}: {str(e)[:110]}")
        else:
            raise SystemExit(f"CONTROL FAILED: {label} did not raise")

wh_check.run(a8_2, CLAIMS, TABLE_CHECKS, sys.argv)
