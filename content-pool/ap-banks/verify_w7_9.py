"""Key audit for AP WORLD HISTORY: MODERN 7.9 Causation in Global Conflict.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor; ``claim``
states what the key rests on, for a human to audit. The gate is
``wh_check.run``, shared by the World History banks.

THIS IS THE UNIT'S REASONING TOPIC
----------------------------------
The CED says of it: "The final topic in this unit focuses on the skill of
argumentation and so provides an opportunity for your students to draw upon the
key concepts and historical developments they have studied in this unit. Using
evidence relevant to this unit's key concepts, students should practice the
suggested skill for this topic." So the module is written as an argumentation
set. Items 12, 13 and 14 are the only recall items, and they restate the review
key concepts the CED prints in this topic's own box; everything else presents an
argument and asks what evidence does to it, or asks what a stated argument can
and cannot establish.

Unit 7 Learning Objective I: explain the relative significance of the causes of
global conflict in the period 1900 to the present. Suggested skill 6.D:
corroborate, qualify, or modify an argument using diverse and alternative
evidence in order to develop a complex argument, which the CED says might
explain nuance by analyzing multiple variables, explain connections within and
across periods, explain the relative significance of a source's credibility and
limitations, or explain how or why a claim or argument is or is not effective.

  skill 6.D, its three verbs and four bullets   items 1, 5, 7, 8, 9, 15, 20,
                                                21, 22, 24, 25, 26, 30
  Learning Objective I                          items 2, 4, 10, 23, 27, 28, 30
  the review key concepts printed for 7.9       items 12, 13, 14, 16, 17
  the unit's cause statements                   items 3, 4, 5, 6, 11, 29, 30

THE HONEST ANSWER ABOUT "RELATIVE SIGNIFICANCE", and the reason no key here
rests on an author's own ranking: the framework ranks a cause exactly ONCE,
where KC-6.2.IV.B.ii writes "and especially" before the rise to power of fascist
and totalitarian regimes. KC-6.2.IV.B.i lists the causes of the first war
without ranking any of them. Items 3, 4, 23 and 30 turn on precisely that
asymmetry, and every other item about weighing causes keys to a REASONING move
that is checkable without a ranking:

  a cause cannot follow its effect                       item 10
  a factor present where no war came does not by itself
    account for where war came                           item 11
  two measures that rank three states differently do not
    both point to one state                              item 18
  an argument selected for agreement has not used
    diverse and alternative evidence                     item 24
  an assertion with no connecting evidence cannot
    support a judgement of weight                        item 9

Items 3, 12 and 30 are the SWAP items -- the ranking attached to the wrong war,
the direction of KC-6.2's "leading to", and a method that drops either half --
so those anchors carry both clauses.

WHAT IS NOT KEYED, deliberately: no date, battle, treaty clause or casualty
total, and no item asks a student to rank the causes of the First World War
against one another, because the framework prints no ranking to check such an
answer against.

DATA ITEMS: 18 and 19 carry tables of explicitly illustrative data, recomputed
below from the table alone, with each distractor falsified against the same
numbers. The second table carries an excess column that must equal the
difference of the two indices it compares, so no figure in it can be altered
silently.

NEGATIVE CONTROLS: ``python3 verify_w7_9.py --selftest`` rotates every key,
breaks every anchor, corrupts every cell of both tables, injects each banned
notation and figure-language form, strips the citation from a ``why`` and a
``claim``, and duplicates a choice; each must raise for its own reason, and
positive controls run alongside.
"""
import sys

import cg_check as cg
import wh_check
import w7_9

CLAIMS_COL = "Colonial territories claimed in the decade before the conflict, of the twelve then in dispute"
YEARS_COL = "Years since its most recent territorial dispute with a neighbour, within the preceding decade"
WEAPONS = "Index of new weapons in service"
CASUALTIES = "Index of casualties per month"
EXCESS = "Excess of the casualty index over the weapons index"


def q18(table, item):
    claims = dict(zip(cg.labels(table), cg.col(table, CLAIMS_COL)))
    years = dict(zip(cg.labels(table), cg.col(table, YEARS_COL)))
    assert set(claims) == {"State 1", "State 2", "State 3"}, \
        f"the item speaks of three states; the table holds {sorted(claims)}"
    # Both columns are bounded by their own headers: twelve territories in
    # dispute, and a decade of years to count back through.
    for name, n in claims.items():
        assert 0 <= n <= 12, f"{name} claims {n} of the twelve territories in dispute"
    for name, n in years.items():
        assert 0 <= n <= 10, f"{name} reports {n} years within the preceding decade"
    by_claims = sorted(claims, key=claims.get, reverse=True)
    # "Most recent dispute" is the SMALLEST number of years since one.
    by_recency = sorted(years, key=years.get)
    assert len(set(claims.values())) == 3, \
        "'all three states record the same number of colonial claims' must be false"
    assert len(set(years.values())) == 3, \
        "'all three last had a dispute in the same year' must be false"
    assert by_claims[0] != by_recency[0], (
        f"the keyed conclusion requires the two measures to point at different states; "
        f"most claims is {by_claims[0]} and most recent dispute is {by_recency[0]}"
    )
    assert by_claims[0] == by_recency[-1], (
        f"the state with the most claims must be the one longest without a dispute; "
        f"most claims is {by_claims[0]} and longest without a dispute is {by_recency[-1]}"
    )
    return (f"ranked by colonial claims the order is {by_claims}, ranked from most recent "
            f"dispute to least it is {by_recency}, so the two measures reverse each other "
            f"and do not point at the same state")


def q19(table, item):
    weapons = dict(zip(cg.labels(table), cg.col(table, WEAPONS)))
    casualties = dict(zip(cg.labels(table), cg.col(table, CASUALTIES)))
    excess = dict(zip(cg.labels(table), cg.col(table, EXCESS)))
    order = ["Theatre 1", "Theatre 2", "Theatre 3"]
    assert cg.labels(table) == order, \
        f"the item reads the theatres in order; the table holds {cg.labels(table)}"
    # The third column is the second minus the first, so no figure in this table
    # can be altered without the row ceasing to agree with itself.
    for k in order:
        assert excess[k] == casualties[k] - weapons[k], (
            f"{k}: the excess column reports {excess[k]} but the two indices differ by "
            f"{casualties[k] - weapons[k]}"
        )
    for name, series in (("weapons", weapons), ("casualties", casualties)):
        values = [series[k] for k in order]
        assert values == sorted(values) and len(set(values)) == 3, \
            f"the {name} index must rise across the three theatres; got {values}"
    gaps = [excess[k] for k in order]
    assert gaps == sorted(gaps) and len(set(gaps)) == 3, \
        f"'the gap between them narrows' must be false; the gaps are {gaps}"
    assert any(casualties[k] != weapons[k] for k in order), \
        "'the two indices are equal in every theatre' must be false"
    return (f"both indices rise across {order}, each excess equals the casualty index minus "
            f"the weapons index, and the gaps {gaps} themselves widen")


TABLE_CHECKS = {18: q18, 19: q19}

CLAIMS = [
 ("Corroborate, qualify, or modify it using diverse and alternative evidence",
  "Suggested skill 6.D for this topic is to corroborate, qualify, or modify an argument using diverse and alternative evidence in order to develop a complex argument, and the CED directs students to practise it on evidence relevant to this unit's key concepts, KC-6.2 among them."),
 ("relative significance of the causes of global conflict in the period 1900 to the present",
  "Unit 7 Learning Objective I asks students to explain the relative significance of the causes of global conflict in the period 1900 to the present; the other options restate Unit 7 Learning Objectives G and E."),
 ("list for the Second World War, where one cause is introduced by the word 'especially'",
  "KC-6.2.IV.B.ii writes 'and especially' before the rise to power of fascist and totalitarian regimes, while KC-6.2.IV.B.i lists the first war's causes without ranking any of them, so the anchor carries the war and the ranking together because attaching it to the wrong war is the plausible error."),
 ("Argue the ranking from evidence, because the framework lists those causes without ranking them",
  "KC-6.2.IV.B.i names five things among the causes of World War I and orders none of them, and the framework's single ranking, in KC-6.2.IV.B.ii, belongs to the second war, so Unit 7 Learning Objective I leaves this ranking to be argued."),
 ("settlement of the first war appears among the causes of the second",
  "KC-6.2.IV.B.ii opens its list with the unsustainable peace settlement after World War I and includes continued imperialist aspirations, while KC-6.2.IV.B.i names imperialist expansion among the first war's causes; suggested skill 6.D asks for connections across periods."),
 ("names new technology as what raised casualty levels, and names other things among the causes",
  "KC-6.1.III.C.i and KC-6.1.III.C.ii attribute increased levels of wartime casualties to new military technology, and to new tactics in the second case, while KC-6.2.IV.B.i and KC-6.2.IV.B.ii give each war a list of causes in which technology does not appear."),
 ("political and territorial pressures acting on the same state, weighed alongside the economic ones",
  "Suggested skill 6.D asks students to explain nuance of an issue by analyzing multiple variables, and KC-6.2.IV.B.i names territorial and regional conflicts, a flawed alliance system and intense nationalism alongside competition for resources."),
 ("Corroboration from a source with a different interest in the outcome",
  "Suggested skill 6.D asks students to corroborate an argument using diverse and alternative evidence and to weigh a source's credibility and limitations, and KC-6.2.IV.B.i and KC-6.2.IV.B.ii state the causes at issue; agreement between differently interested sources strengthens a claim without settling it."),
 ("names a cause the framework lists but never shows how that cause produced the outcome",
  "KC-6.2.IV.B.i does name intense nationalism among the things that combined to escalate tensions, so the fault is not the choice of cause; suggested skill 6.D asks students to explain how or why an argument is or is not effective."),
 ("a cause cannot come after the outcome it is offered to explain",
  "KC-6.2.IV.B.i and KC-6.2.IV.B.ii present their items as causes of the wars that followed them, and Unit 7 Learning Objective I asks for the relative significance of causes, which cannot be weighed before the ordering holds."),
 ("does not on its own account for where war came, though it may still be among the causes",
  "KC-6.2.IV.B.i describes causes that combined to escalate tensions into global conflict rather than any one factor acting alone, and suggested skill 6.D asks for nuance drawn from multiple variables, so a factor present in cases with different outcomes is narrowed rather than dropped."),
 ("challenges came first, and the framework describes them as leading to unprecedented worldwide conflicts",
  "KC-6.2 states that peoples and states around the world challenged the existing political and social order in varying ways, leading to unprecedented worldwide conflicts, so the anchor carries both halves because the reversed reading is the plausible error."),
 ("That the conflicts were without precedent",
  "KC-6.2 describes the challenges to the existing political and social order as leading to UNPRECEDENTED worldwide conflicts, and the adjective is the framework's own."),
 ("advances in communication, transportation, industry, agriculture, and medicine",
  "KC-6.1 states that rapid advances in science and technology altered the understanding of the universe and the natural world and led to advances in communication, transportation, industry, agriculture, and medicine."),
 ("one broad development is presented in the framework with more than one kind of consequence",
  "KC-6.1 attributes advances in industry, agriculture and medicine to rapid advances in science and technology, while KC-6.1.III.C.i and KC-6.1.III.C.ii attribute increased wartime casualties to new military technology and new tactics; suggested skill 6.D asks for nuance drawn from multiple variables."),
 ("collapsed due to a combination of internal and external factors",
  "KC-6.2.I.A states that the older, land-based Ottoman, Russian, and Qing empires collapsed due to a combination of internal and external factors, and suggested skill 6.D asks students to modify an argument with the evidence it leaves out."),
 ("Mexican Revolution is described as arising as a result of political crisis",
  "KC-6.2.II.D states that states around the world challenged the existing political and social order, including the Mexican Revolution that arose as a result of political crisis, which is a counterexample to an argument tracing every such challenge to a world war."),
 ("longest without a territorial dispute, so the two measures do not point to the same state",
  "KC-6.2.IV.B.i names imperialist expansion and territorial conflicts as separate items among the causes of war, and suggested skill 6.D asks for nuance drawn from analysing more than one variable. Recomputed in q18 above from the illustrative table alone, including the argument's own claim, which the table falsifies."),
 ("casualty index rises faster, so the gap between them widens",
  "KC-6.1.III.C.ii states that new military technology and new tactics led to increased levels of wartime casualties, and an argument about that claim would rest on evidence of this kind. Recomputed in q19 above from the illustrative table alone, including the excess column, which must equal the difference of the two indices."),
 ("government's interest in the account be weighed, and other evidence sought",
  "Suggested skill 6.D asks students to explain the relative historical significance of a source's credibility and limitations and to use diverse and alternative evidence, and KC-6.2.IV.B.ii names the causes at issue, on which a combatant government is an interested party."),
 ("more than one of the causes the framework names, with a statement of how they bore on one another",
  "Suggested skill 6.D asks students to explain nuance of an issue by analyzing multiple variables, and KC-6.2.IV.B.i itself describes territorial and regional conflicts combining with a flawed alliance system and intense nationalism."),
 ("predominantly maintained control over colonial holdings, and the statement naming continued imperialist aspirations",
  "KC-6.2.I.B states that between the two world wars imperial states predominantly maintained control over colonial holdings, and KC-6.2.IV.B.ii names continued imperialist aspirations among the causes of World War II; suggested skill 6.D asks for connections across periods."),
 ("argument has been made for the ranking, since the framework itself ranks a cause only where it writes 'especially'",
  "Unit 7 Learning Objective I asks for the relative significance of the causes of global conflict, the only ranking the framework prints is the 'especially' of KC-6.2.IV.B.ii, and KC-6.2.IV.B.i lists its causes unranked, so elsewhere the ranking rests on evidence."),
 ("not used diverse and alternative evidence",
  "Suggested skill 6.D asks students to corroborate, qualify, or modify an argument using diverse and alternative evidence, drawing on this unit's key concepts, KC-6.2 and KC-6.2.IV.B.ii among them; evidence selected for agreement cannot qualify or modify anything."),
 ("It has corroborated the argument",
  "Suggested skill 6.D names corroborating, qualifying and modifying as three distinct operations, and KC-6.2.IV.B.i and KC-6.2.IV.B.ii supply the claims at issue; independent evidence agreeing with a claim is the first of the three."),
 ("qualified the argument, narrowing the range of cases the claim covers",
  "Suggested skill 6.D names corroborating, qualifying and modifying as three distinct operations, and KC-6.2.I.B's own qualifier 'predominantly' is the framework narrowing a claim in exactly this way rather than overturning it."),
 ("carried the most weight, and on what evidence",
  "Unit 7 Learning Objective I asks students to explain the relative significance of the causes of global conflict in the period 1900 to the present, and suggested skill 6.D requires the answer to rest on diverse and alternative evidence."),
 ("weigh the causes of conflict against one another rather than to describe the conflicts",
  "Unit 7 Learning Objective I asks for the relative significance of the causes of global conflict, which is a question about causes and their weight, and the CED states that this final topic draws on the unit's key concepts, KC-6.2 among them."),
 ("identifies a single cause that accounts for every conflict of the century",
  "KC-6.2.IV.B.i and KC-6.2.IV.B.ii each give a list of causes, KC-6.2 describes varied challenges leading to conflict and KC-6.2.I.A names a combination of factors, so no single universal cause is offered anywhere and the other options restate those statements."),
 ("weigh them against evidence of several kinds, and use the framework's own ranking where it gives one",
  "Unit 7 Learning Objective I asks for relative significance and suggested skill 6.D asks that the argument rest on diverse and alternative evidence; KC-6.2.IV.B.ii supplies the framework's one explicit ranking while KC-6.2.IV.B.i leaves its causes unranked, so the anchor carries both halves of the method."),
]

wh_check.run(w7_9, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
