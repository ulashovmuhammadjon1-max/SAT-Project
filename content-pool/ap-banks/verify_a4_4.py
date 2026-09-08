"""Key audit for AP U.S. HISTORY 4.4 America on the World Stage.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The shared gate is
``wh_check.run``.

WHAT THE KEYS REST ON
---------------------
  Unit 4 Learning Objective D, how and why
    American foreign policy developed and
    expanded over time                            items 1, 12, 13, 14, 18, 19, 20, 21, 26
  KC-4.3.I, struggling for an independent global
    presence while claiming territory and
    promoting trade                               2, 3, 9, 16, 22, 23, 24, 26, 30
  KC-4.3.I.A.ii, influence and control over the
    Western Hemisphere by military action,
    American Indian removal and diplomacy         4, 5, 6, 7, 8, 9, 15, 23, 24, 25, 26,
                                                  27, 30
  KC-4.3.I.A.i, the neighbouring sub-point on
    topic 4.2's page, used only for the CONTRAST
    the framework itself draws                    7, 8, 9, 21, 23, 24
  KC-4.3, trade, borders, government and private
    initiative                                    10, 11, 17, 28, 29, 30
  the America in the World thematic focus         12, 13
  skill 2.B and the Causation reasoning process   14, 15, 16, 17, 18, 19, 20

SENSITIVE MATERIAL. KC-4.3.I.A.ii names American Indian removal among the means
by which the U.S. government sought influence and control over the Western
Hemisphere, and every item that touches it states it in exactly those terms: a
government instrument, listed beside military actions and diplomatic efforts.
Nothing is added. KC-4.3.I.B, on American Indian resistance and the wars and
relocations that followed, is printed on topic 4.8's page and belongs to that
topic.

WHAT IS NOT ASSERTED. The CED names the Monroe Doctrine as an EXAMPLE of a
diplomatic effort and gives no text, date or author. Items 6 and 25 therefore
ask only which category the framework puts it in, which is a fact about the
framework; no key anywhere turns on what the Doctrine said.

THE SWAP ITEMS. Items 7 and 8 exchange the region and the means between
KC-4.3.I.A.i and KC-4.3.I.A.ii, item 10 reverses both halves of KC-4.3, item 26
exchanges a concept with the sub-point beneath it, and item 29's leading
distractor exchanges which column of ventures is the larger. Those anchors carry
BOTH clauses.

DATA ITEMS: 27, 28 and 29 carry tables of explicitly hypothetical figures. Each
check recomputes the keyed claim and falsifies every distractor from the same
rows FIRST, and compares the rows against the literal list LAST -- the ordering
verify_a4_1.py records, so a control exchanging a category fires on the guard it
names rather than on row equality.

NEGATIVE CONTROLS: ``python3 verify_a4_4.py --selftest``.
"""
import sys

import cg_check as cg
import wh_check
import wh_stimulus
import a4_4

KIND = "Kind of means the record assigns it"
WHERE = "Where the action was directed"
TRADED = "Value of goods traded with other nations"
CLAIMED = "Area of territory newly claimed, in thousands of square miles"
BY_GOVERNMENT = "Ventures abroad fitted out by the government"
BY_PRIVATE = "Ventures abroad fitted out by private parties"

_EXPECTED_MEANS = [
    ["Action 1", "Military action", "The Western Hemisphere"],
    ["Action 2", "American Indian removal", "The Western Hemisphere"],
    ["Action 3", "Diplomatic effort", "The Western Hemisphere"],
    ["Action 4", "Diplomatic effort", "The Western Hemisphere"],
    ["Action 5", "Military action", "The Western Hemisphere"],
]

_EXPECTED_TRADE = [
    ["1800 to 1810", "55", "12"],
    ["1810 to 1820", "78", "19"],
    ["1820 to 1830", "104", "26"],
    ["1830 to 1840", "141", "38"],
]

_EXPECTED_INITIATIVE = [
    ["1800 to 1810", "7", "18"],
    ["1810 to 1820", "11", "27"],
    ["1820 to 1830", "16", "41"],
    ["1830 to 1840", "23", "60"],
]


def _rows_are(table, expected, what):
    assert [list(r) for r in table["rows"]] == expected, (
        f"the {what} table does not hold the rows this check was written against; "
        f"got {table['rows']}"
    )


def q27(table, item):
    """All three of the framework's kinds of means appear, all in one region."""
    labs = cg.labels(table)
    assert labs == [f"Action {n}" for n in range(1, 6)], \
        f"the five actions the choices speak of are not the rows: {labs}"
    kinds = [cg.normalize(r[table["headers"].index(KIND)]) for r in table["rows"]]
    expected_kinds = {"military action", "american indian removal", "diplomatic effort"}
    assert set(kinds) == expected_kinds, (
        f"the key needs all three of the kinds KC-4.3.I.A.ii lists and no others; "
        f"got {sorted(set(kinds))}"
    )
    assert len(set(kinds)) > 1, "'only one kind of means appears' must be false"
    repeated = {k for k in set(kinds) if kinds.count(k) > 1}
    assert len(repeated) > 1, (
        f"'diplomatic effort is the only kind recorded more than once' must be false; "
        f"{sorted(repeated)} each appear more than once"
    )
    assert "military action" in kinds, "'no military action appears' must be false"
    wheres = [cg.normalize(r[table["headers"].index(WHERE)]) for r in table["rows"]]
    assert len(set(wheres)) == 1, (
        f"'the recorded actions were directed at more than one region' must be false; "
        f"got {sorted(set(wheres))}"
    )
    _rows_are(table, _EXPECTED_MEANS, "means")
    return (f"the five rows carry {len(set(kinds))} distinct kinds of means, "
            f"{len(repeated)} of them more than once, all directed at one region")


def q28(table, item):
    """Trade and new territorial claims rise together across the four decades."""
    labs = cg.labels(table)
    assert labs == ["1800 to 1810", "1810 to 1820", "1820 to 1830", "1830 to 1840"], \
        f"the four decades the item speaks of are not the rows: {labs}"
    traded, claimed = cg.col(table, TRADED), cg.col(table, CLAIMED)
    assert all(traded[i + 1] > traded[i] for i in range(len(traded) - 1)), \
        f"the traded value must rise at every step; got {traded}"
    assert all(claimed[i + 1] > claimed[i] for i in range(len(claimed) - 1)), \
        f"newly claimed territory must rise at every step; got {claimed}"
    assert not any(claimed[i + 1] < claimed[i] for i in range(len(claimed) - 1)), \
        "'new territorial claims fall away' must be false"
    assert not any(traded[i + 1] < traded[i] for i in range(len(traded) - 1)), \
        "'trade falls away' must be false"
    assert len(set(traded)) > 1 and len(set(claimed)) > 1, \
        "'neither column changes' must be false"
    assert all(t > c for t, c in zip(traded, claimed)), (
        f"'new claims exceed the traded value in every decade' must be false; got "
        f"{traded} against {claimed}"
    )
    _rows_are(table, _EXPECTED_TRADE, "trade")
    return (f"traded value runs {traded} and newly claimed area {claimed}, both rising at "
            f"every step with the traded value always the larger")


def q29(table, item):
    """Both kinds of venture rise, and the private column is the larger throughout."""
    labs = cg.labels(table)
    assert labs == ["1800 to 1810", "1810 to 1820", "1820 to 1830", "1830 to 1840"], \
        f"the four decades the item speaks of are not the rows: {labs}"
    state, private = cg.col(table, BY_GOVERNMENT), cg.col(table, BY_PRIVATE)
    assert all(state[i + 1] > state[i] for i in range(len(state) - 1)), \
        f"government ventures must rise at every step; got {state}"
    assert all(private[i + 1] > private[i] for i in range(len(private) - 1)), \
        f"private ventures must rise at every step; got {private}"
    assert all(p > s for s, p in zip(state, private)), (
        f"the key needs the private column to be the larger in EVERY row; got {state} "
        f"against {private}"
    )
    assert not any(s > p for s, p in zip(state, private)), \
        "'government ventures are the more numerous throughout' must be false"
    assert not any(private[i + 1] < private[i] for i in range(len(private) - 1)), \
        "'private ventures decline' must be false"
    present = [i for i, p in enumerate(private) if p > 0]
    assert len(present) == len(labs), (
        f"'private ventures appear in only one decade' must be false; they appear in "
        f"{len(present)} of {len(labs)}"
    )
    assert all(s != p for s, p in zip(state, private)), \
        "'the two columns hold the same figure in every decade' must be false"
    _rows_are(table, _EXPECTED_INITIATIVE, "initiative")
    return (f"government ventures run {state} and private ventures {private}, both rising "
            f"with the private column the larger in all {len(labs)} rows")


TABLE_CHECKS = {27: q27, 28: q28, 29: q29}

CLAIMS = [
 ("developed and expanded over time",
  "Unit 4 Learning Objective D reads 'Explain how and why American foreign policy developed and expanded over time'; a policy fixed at the founding is the negation of that objective."),
 ("standing among other nations that it did not yet have",
  "KC-4.3.I's participle STRUGGLING describes an effort still under way to create an independent global presence, so the standing is sought rather than held."),
 ("North American continent and to promote foreign trade",
  "KC-4.3.I names both aims together. The anchor carries both because two distractors keep one half and reverse the other, and KC-4.3 confirms the interest in increasing foreign trade."),
 ("The Western Hemisphere",
  "KC-4.3.I.A.ii names the Western Hemisphere as the region over which the U.S. government sought influence and control; North America is the region of the neighbouring KC-4.3.I.A.i on topic 4.2's page."),
 ("Military actions, American Indian removal, and diplomatic efforts",
  "KC-4.3.I.A.ii names exactly these three among the variety of means; exploration belongs to KC-4.3.I.A.i instead."),
 ("Among the diplomatic efforts",
  "KC-4.3.I.A.ii reads 'diplomatic efforts such as the Monroe Doctrine', so the framework classes the Doctrine as an example of a diplomatic effort. The item asks only which category the framework uses, not what the Doctrine said."),
 ("first names North America and the second names the Western Hemisphere",
  "KC-4.3.I.A.i names North America and KC-4.3.I.A.ii the Western Hemisphere, which is the widening of scope Unit 4 Learning Objective D asks students to explain. The anchor carries both because the leading distractor exchanges them."),
 ("exploration and diplomatic efforts, while the second adds military actions",
  "KC-4.3.I.A.i lists exploration and diplomatic efforts and KC-4.3.I.A.ii adds military actions and American Indian removal, with diplomacy common to both. The anchor carries both halves because the leading distractor exchanges the sentences."),
 ("sought influence and control through a variety of means",
  "Both KC-4.3.I.A.i and KC-4.3.I.A.ii use the same construction, a variety of means, which is what a single-instrument account excludes."),
 ("increasing foreign trade and expanding its national borders",
  "KC-4.3 states that this interest shaped the nation's foreign policy; the leading distractor reverses both halves at once, so the anchor carries both."),
 ("not carried on by the state alone",
  "KC-4.3 names government AND private initiatives, so restricting the effort to either alone drops half the sentence, while KC-4.3.I.A.ii separately describes the government's own means."),
 ("Diplomatic, economic, cultural, and military",
  "The America in the World thematic focus printed on this topic's page names exactly these four kinds of interaction, in service of Unit 4 Learning Objective D."),
 ("increasingly important role in the world",
  "The same thematic focus says those interactions shape the development of America AND America's increasingly important role in the world, which is the widening Unit 4 Learning Objective D asks about."),
 ("Explain the point of view, purpose, historical situation",
  "Skill 2.B as printed beside this topic's title, in service of Unit 4 Learning Objective D; skill 2.A is the same list under IDENTIFY and the remaining options are 3.D, 6.B and 1.B."),
 ("communicated to another government",
  "Skill 2.B asks students to explain a purpose rather than name it. KC-4.3.I.A.ii places diplomatic efforts among the means by which the government sought influence and control over the Western Hemisphere."),
 ("reads security and commerce as a single interest",
  "Skill 2.B asks for an explanation of a point of view. KC-4.3.I joins claiming territory to promoting foreign trade in one sentence and KC-4.3.I.A.ii names military actions among the means, which is what makes the position intelligible."),
 ("only the government commands the means of protection",
  "Skill 2.B asks students to explain an audience rather than name it. KC-4.3 has the interest in increasing foreign trade spurring government and private initiatives together, so a request to the state is a request for its own instrument."),
 ("depends on what the nation was then seeking abroad",
  "Skill 2.B asks for an explanation of historical situation and skill 2.C for how such features limit a source's uses. KC-4.3.I supplies the circumstance and Unit 4 Learning Objective D asks how and why policy developed."),
 ("Causation",
  "The unit's table prints Causation as this topic's reasoning process, matching Unit 4 Learning Objective D's demand for HOW AND WHY policy developed and expanded; the rejected options are the other two reasoning processes and two historical thinking skills."),
 ("relationship between causes and effects",
  "Aspect 2.ii of the Causation reasoning process asks students to explain the relationship between causes and effects rather than to list them, and Unit 4 Learning Objective D is what it is applied to here."),
 ("reach and instruments of policy across the period",
  "Unit 4 Learning Objective D's phrase OVER TIME directs attention to change across the period, which the framework's own pair KC-4.3.I.A.i and KC-4.3.I.A.ii exhibits by widening both the region and the list of means."),
 ("not yet established and was hard to obtain",
  "KC-4.3.I's word STRUGGLING concedes difficulty and an outcome not yet reached, without saying the effort was abandoned or immediately successful."),
 ("Creating an independent global presence",
  "KC-4.3.I makes this the aim the United States was struggling towards, while KC-4.3.I.A.ii and KC-4.3.I.A.i list military actions, American Indian removal, diplomatic efforts and exploration as MEANS."),
 ("military actions and American Indian removal among the means used",
  "KC-4.3.I.A.ii is what a purely commercial account of the period leaves out; the rejected sentences all name commercial or exploratory activity and so do not contradict it."),
 ("example of a diplomatic effort, a separate item in the same list",
  "KC-4.3.I.A.ii lists military actions, American Indian removal and diplomatic efforts as separate items and places the Monroe Doctrine under the third with the words 'such as'."),
 ("KC-4.3.I states the aim of territory and trade",
  "KC-4.3.I is the broader concept and KC-4.3.I.A.ii the sub-point beneath it naming the means. The anchor carries both halves because the leading distractor exchanges the two levels, and Unit 4 Learning Objective D follows the same ordering."),
 ("three of the kinds of means the framework lists appear",
  "Recomputed in q27 from the table alone: the middle column holds three distinct kinds, two of them more than once, all directed at one region. KC-4.3.I.A.ii describes a variety of means including military actions, American Indian removal, and diplomatic efforts."),
 ("Trade and new territorial claims both grow",
  "Recomputed in q28 from the table alone: both columns rise at every step. KC-4.3 names an interest in increasing foreign trade AND expanding national borders as what shaped foreign policy."),
 ("with private ventures the more numerous throughout",
  "Recomputed in q29 from the table alone: both columns rise and the private column is the larger in every row. KC-4.3 names government and private initiatives together. The anchor carries both clauses because the leading distractor exchanges which column leads."),
 ("military action, American Indian removal and diplomacy",
  "The keyed sentence collects KC-4.3.I and KC-4.3.I.A.ii in the order the topic page prints them, with KC-4.3's government and private initiatives behind them, and adds nothing to any of the three."),
]


def _extra_mutations():
    def every_action_the_same_kind(mod, cl):
        # The kinds guard is written FIRST in q27 so this fires on the claim the
        # item makes rather than on the literal row comparison at the end.
        t = mod.QUESTIONS[26]["table"]
        t["rows"] = [list(r) for r in t["rows"]]
        for row in t["rows"]:
            row[1] = "Diplomatic effort"

    def a_second_region_appears(mod, cl):
        t = mod.QUESTIONS[26]["table"]
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][3][2] = "Europe"

    def private_ventures_fall(mod, cl):
        t = mod.QUESTIONS[28]["table"]
        t["rows"] = [list(r) for r in t["rows"]]
        for row, value in zip(t["rows"], ["60", "41", "27", "18"]):
            row[2] = value

    return [
        ("every recorded action assigned to a single kind of means", every_action_the_same_kind),
        ("one action recorded as directed outside the hemisphere", a_second_region_appears),
        ("the private venture column reversed so it falls across the decades",
         private_ventures_fall),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    wh_stimulus.controls(a4_4)
    for label, mutate in _extra_mutations():
        mod = wh_check._mutant(a4_4)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            wh_check.history_style(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as e:
            print(f"  control OK  {label}: {str(e)[:110]}")
        else:
            raise SystemExit(f"CONTROL FAILED: {label} did not raise")

wh_check.run(a4_4, CLAIMS, TABLE_CHECKS, sys.argv)
