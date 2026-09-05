"""Key audit for AP WORLD HISTORY: MODERN 8.2 The Cold War.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in NO distractor; the claim states the CED sentence the key
rests on, with its Key Concept code. `wh_check` refuses any `why` or claim that
cites neither a KC code nor a Learning Objective.

WHERE A DISTRACTOR IS THE SWAP OF THE KEY, THE ANCHOR CARRIES BOTH CLAUSES:

  q6   'fewer than half' against 'more than half' of the same states
  q12  the second bloc overtaking the first, against the first leading throughout
  q16  the shift producing the Cold War, against the Cold War producing the shift
  q18  bloc one's growth multiple against bloc two's
  q25  the movement opposing both orders, against it being allied to one

For each of those the anchor spans the whole relation and not a single noun, so
an anchor that also matched the swapped distractor would fail rather than pass.
That defect is on record in `verify_e2_1.py`.

WHAT IS DELIBERATELY NOT KEYED. This topic invites live political disagreement
about which superpower was responsible for the confrontation. No item here keys
a side. Every key restates KC-6.2.IV.C.ii (a postwar shift in the balance of
power, two superpowers organized on rival principles, a struggle carried across
the globe) or KC-6.2.V.B (groups, including the Non-Aligned Movement, that
opposed the existing orders and promoted alternatives), and goes no further.

Item 8 is the one item resting on the CED's ILLUSTRATIVE EXAMPLES rather than on
a Key Concept, and its stem says so. Illustrative examples are optional in the
course, which is why there is exactly one.

NEGATIVE CONTROL: `python3 verify_w8_2.py --selftest`.
"""
import sys

import cg_check as cg
import wh_check as wh
import w8_2

T_ALIGN = w8_2._T_ALIGN
T_BROADCAST = w8_2._T_BROADCAST
T_STUDENTS = w8_2._T_STUDENTS

REPRESENTED = "States represented"
ALLIED = "States declaring a formal alliance with a superpower"
BLOC1 = "Weekly hours of foreign-language broadcasting, bloc one"
BLOC2 = "Weekly hours of foreign-language broadcasting, bloc two"
Y55 = "Students from newly independent states, 1955"
Y70 = "Students from newly independent states, 1970"


def q6(table, item):
    labs = cg.labels(table)
    rep = {lab: cg.cell(table, lab, REPRESENTED) for lab in labs}
    allied = {lab: cg.cell(table, lab, ALLIED) for lab in labs}
    for lab in labs:
        assert allied[lab] * 2 < rep[lab], (
            f"{lab}: {allied[lab]} of {rep[lab]} is not fewer than half, so the key fails")
    # every distractor false on the same numbers
    assert not any(allied[lab] * 2 > rep[lab] for lab in labs), \
        "'more than half in every region' must be false"
    fewest_sent = cg.ranked(table, REPRESENTED)[-1]
    most_allied = cg.ranked(table, ALLIED)[0]
    assert fewest_sent != most_allied, \
        "'the region sending fewest states had the most alliances' must be false"
    assert len(set(allied.values())) > 1, \
        "'the same number of alliances in all three regions' must be false"
    assert min(allied.values()) > 0, \
        "'one region had no state declaring an alliance' must be false"
    return (f"represented {rep} against alliances {allied}: every region is below half, "
            f"and all four distractors recompute false")


def q12(table, item):
    one = cg.col(table, BLOC1)
    two = cg.col(table, BLOC2)
    assert all(b > a for a, b in zip(one, one[1:])), f"bloc one does not rise throughout: {one}"
    assert all(b > a for a, b in zip(two, two[1:])), f"bloc two does not rise throughout: {two}"
    assert one[0] > two[0], \
        f"bloc two must start behind for 'overtook' to hold; got {one[0]} against {two[0]}"
    assert two[-1] > one[-1], \
        f"bloc two must end ahead for 'overtook' to hold; got {two[-1]} against {one[-1]}"
    # and the distractors
    assert not (one[-1] < one[0] and two[-1] < two[0]), "'both fell over the period' must be false"
    assert any(a != b for a, b in zip(one, two)), "'identical in every decade' must be false"
    assert not all(a > b for a, b in zip(one, two)), \
        "'bloc one ahead in every decade' must be false"
    return (f"bloc one runs {one} and bloc two {two}: both rise at every step, and the "
            f"second passes the first only in the final decade")


def q18(table, item):
    labs = cg.labels(table)
    before = {lab: cg.cell(table, lab, Y55) for lab in labs}
    after = {lab: cg.cell(table, lab, Y70) for lab in labs}
    blocs = [lab for lab in labs if lab.lower().startswith("bloc")]
    assert len(blocs) == 2, f"expected two bloc rows, found {blocs}"
    neither = [lab for lab in labs if lab not in blocs]
    assert len(neither) == 1, f"expected one unaligned row, found {neither}"
    nb = neither[0]
    growth = sum(after[b] for b in blocs) / sum(before[b] for b in blocs)
    assert growth > 3, f"'more than tripled' recomputes to a factor of {growth:.2f}"
    third = (after[nb] - before[nb]) / before[nb]
    assert abs(third - 1 / 3) < 0.005, f"'rose by a third' recomputes to {third:.3f}"
    # every distractor false on the same numbers
    assert not (after[blocs[1]] > after[blocs[0]] and before[blocs[1]] > before[blocs[0]]), \
        "'bloc two hosted more in both years' must be false"
    assert after[nb] > before[nb], "'the unaligned count fell' must be false"
    assert (after[blocs[0]] / before[blocs[0]]) < (after[blocs[1]] / before[blocs[1]]), \
        "'bloc one grew by the larger multiple' must be false"
    assert len(set(after.values())) > 1, "'all three equal in 1970' must be false"
    return (f"the two blocs together go from {sum(before[b] for b in blocs)} to "
            f"{sum(after[b] for b in blocs)}, a factor of {growth:.2f}, while {nb} rises "
            f"by {third:.3f} of itself")


TABLE_CHECKS = {6: q6, 12: q12, 18: q18}

CLAIMS = [
 ("advocacy rather than measurement",
  "KC-6.2.IV.C.ii describes a power struggle between capitalism and communism carried on across the globe, of which a broadcast beamed into a rival state is an instrument. The source is excellent evidence of its maker's purpose and weak evidence about the living standards it asserts, which is the distinction the suggested skill for this topic turns on."),
 ("opposed the existing economic and political orders and promoted alternatives",
  "KC-6.2.V.B states that groups and individuals, including the Non-Aligned Movement, opposed and promoted alternatives to the existing economic, political, and social orders. Refusing bases to both blocs while reserving independent judgement is that stance written as policy."),
 ("shift in the global balance of economic and political power during and after World War II that rapidly evolved",
  "KC-6.2.IV.C.ii states that the global balance of economic and political power shifted during and after World War II and rapidly evolved into the Cold War. The framework names that shift as the origin rather than a dynastic, colonial or environmental dispute."),
 ("contest between rival ways of organizing society",
  "KC-6.2.IV.C.ii states that the emergence of the two superpowers led to ideological conflict and a power struggle between capitalism and communism. Two pamphlets in the same argumentative form establish how the contest was framed by those waging it, which is what a pair of sources can support."),
 ("an alternative to the existing economic and political orders rather than membership in either bloc",
  "KC-6.2.V.B names the Non-Aligned Movement among groups that opposed and promoted alternatives to the existing orders. Promoting an alternative is precisely not choosing between the two on offer, so the anchor carries both halves of that contrast."),
 ("fewer than half of the states represented had declared an alliance",
  "KC-6.2.V.B describes states promoting an alternative to the existing orders, of which a conference whose participants have largely declined alliance is one measure. The survey is hypothetical; the keyed proportion and the falsity of each distractor are recomputed in q6 above, and the anchor says 'fewer' because a distractor says 'more'."),
 ("two states preeminent and the ideological struggle between them was already under way",
  "KC-6.2.IV.C.ii places the emergence of the two superpowers and the start of the ideological struggle in the years during and after World War II. A 1948 memorandum insisting only two options exist is intelligible only against that situation, which is what identifying a source's historical situation means."),
 ("Sukarno in Indonesia and Kwame Nkrumah in Ghana",
  "The CED prints these two as the ILLUSTRATIVE EXAMPLES accompanying KC-6.2.V.B and the Non-Aligned Movement. The distractor pairs are illustrative examples the framework attaches to other statements, on nonviolence, on responses that intensified conflict and on free-market policies."),
 ("how that government wished the confrontation to be understood",
  "KC-6.2.IV.C.ii describes an ideological conflict in which each side argued its case, and an official history is one instrument of that argument. A source produced by a party to the dispute is authoritative about its own framing and not about its opponent's conduct."),
 ("different audiences the two sources address and the different purposes",
  "Explaining a source by its audience and purpose is this topic's suggested skill, and KC-6.2.IV.C.ii supplies the reason a government faced both audiences at once: the struggle between capitalism and communism was carried on across the globe, before domestic publics and neutral states alike."),
 ("carried on across the globe",
  "KC-6.2.IV.C.ii states that the ideological conflict led to a power struggle between capitalism and communism across the globe, and KC-6.2.V.B adds states outside both blocs to the picture. Every narrower description of the struggle's extent contradicts one or both."),
 ("increased their broadcasting in every decade recorded, and the second overtook the first",
  "KC-6.2.IV.C.ii describes an ideological conflict waged across the globe, of which broadcasting into other countries is one form. The estimate is hypothetical; q12 above recomputes both halves of the key and the falsity of the distractor that has the first bloc leading throughout, which is why the anchor carries the overtaking as well as the rise."),
 ("opposed the existing orders and promoted alternatives to both blocs",
  "KC-6.2.V.B states that groups and individuals opposed and promoted alternatives to the existing economic, political, and social orders. Refusing arms from both sides on the ground that they carry someone else's quarrel is that position argued from the receiving end."),
 ("economic and political weight that set it apart from every other state",
  "KC-6.2.IV.C.ii ties the emergence of superpowers to the shift in the global balance of economic and political power during and after World War II. The framework rests the distinction on weight relative to other states, not on empire, population, treaty recognition or neutrality."),
 ("strong evidence of the argument its makers wanted the public to accept",
  "KC-6.2.IV.C.ii makes the case each side argued part of the object of study, so a one-sided source is the best evidence there is of its own maker's purpose. A source's point of view limits what it shows about its opponent without making it worthless, which is the distinction this topic's skill requires."),
 ("shift in the global balance of power, which rapidly evolved into the Cold War",
  "KC-6.2.IV.C.ii fixes the shift as prior and the Cold War as what it became. A distractor reverses that order, so the anchor carries both terms and the direction between them rather than either term alone."),
 ("readers for whom neither bloc's account of the world was authoritative",
  "KC-6.2.V.B places groups and states outside both existing orders, opposing them and promoting alternatives, which is the readership an editorial criticizing both assumes. Nothing in the editorial's content could establish a claim about secret financing."),
 ("more than tripled their intake, while the number hosted by neither bloc rose by a third",
  "KC-6.2.IV.C.ii describes a struggle between capitalism and communism carried across the globe, of which competition for a newly independent state's graduates is one arena. The count is hypothetical; q18 above recomputes both halves of the key and the falsity of the reversed growth-multiple distractor."),
 ("reliable description of conditions inside the rival superpower",
  "KC-6.2.IV.C.ii makes each superpower an interested party in a global ideological conflict, so a speech is authoritative about its own maker's framing and weakest exactly where it describes its opponent. Distinguishing what a source can and cannot support is the skill this topic practises."),
 ("knowledge of how the confrontation ended, which shapes what it treats as important",
  "KC-6.2.V.B places nonaligned governments under pressure from both existing orders, which both sources describe; what separates them is the situation each was composed in. Hindsight selects what a later source records, which is neither an automatic virtue nor an automatic fault."),
 ("competition between the two superpowers for overseas colonies",
  "KC-6.2.IV.C.ii traces the confrontation to the postwar shift in the balance of economic and political power and describes it as a struggle between capitalism and communism, not as a colonial competition. The keyed statement is therefore the one the framework does not support; the other four restate KC-6.2.IV.C.ii and KC-6.2.V.B."),
 ("an argument for an alternative to both of the existing orders",
  "KC-6.2.V.B states that groups and individuals opposed and promoted alternatives to the existing economic, political, and social orders. Rejecting the characteristic arrangement of each bloc in one statement is the promotion of an alternative rather than a choice between them."),
 ("organized on rival principles, a democracy and an authoritarian communist state",
  "KC-6.2.IV.C.ii states that the democracy of the United States and the authoritarian communist Soviet Union emerged as superpowers, which led to ideological conflict. The rival principles on which the two were organized are what the framework makes the ideological form of the struggle rest on."),
 ("records the experience of people whose governments' documents rarely mention them",
  "KC-6.2.IV.C.ii describes a struggle carried across the globe, so it reached populations far from either capital, and KC-6.2.V.B places whole societies outside both orders. Testimony gathered decades later is not contemporaneous and cannot report either superpower's intentions, but it reaches people the official record omits."),
 ("opposed the existing orders that the superpowers led and promoted alternatives",
  "KC-6.2.V.B names the Non-Aligned Movement among the groups that opposed and promoted alternatives to the existing economic, political, and social orders. Opposing both orders is incompatible with being an alliance of, a creation of, or a supporter of either superpower, so the anchor carries both the opposition and the alternative."),
 ("sought to shape its own population's understanding of the confrontation",
  "KC-6.2.IV.C.ii describes an ideological conflict in which each side argued its case, and a state textbook is among the most deliberate forms that argument took. The source is read for its purpose, not for the accuracy of its account of the opponent."),
 ("shaped by the need to persuade audiences abroad and at home",
  "Distinguishing a source by its intended audience is this topic's suggested skill, and KC-6.2.IV.C.ii supplies the reason a foreign ministry had audiences at home and abroad to persuade in a global ideological struggle. A document written for internal circulation faces no such requirement."),
 ("both superpowers competing for influence in states that had recently become independent",
  "KC-6.2.IV.C.ii states that the struggle between capitalism and communism was carried on across the globe. Competition inside newly independent states outside Europe tests that claim directly, whereas each distractor is drawn from Europe or from one superpower's internal affairs."),
 ("consistent with refusing alliance with either",
  "KC-6.2.V.B describes opposition to the existing orders and the promotion of alternatives, which is a stance toward alliance rather than a refusal of all contact. Treating any receipt of aid as membership would empty the framework's own category of states opposing both orders."),
 ("left two states preeminent on rival principles, and their struggle was carried across the globe",
  "KC-6.2.IV.C.ii supplies the postwar shift, the two superpowers organized on rival principles and the global reach of the struggle; KC-6.2.V.B supplies the groups that opposed both orders and promoted alternatives. The key is the conjunction of the two sentences, and each distractor contradicts at least one."),
]

wh.run(w8_2, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
