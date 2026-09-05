"""Key audit for AP WORLD HISTORY: MODERN 8.3 Effects of the Cold War.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in NO distractor; the claim states the CED sentence the key
rests on, with its Key Concept code. `wh_check` refuses a `why` or a claim that
cites neither a KC code nor a Learning Objective.

WHERE A DISTRACTOR IS THE SWAP OF THE KEY, THE ANCHOR CARRIES BOTH CLAUSES:

  q6   one alliance gaining and the other losing, against both moving alike
  q8   proliferation rising, against a count that stalls or falls
  q12  conflicts within a state outnumbering those between states, and the reverse
  q13  proliferation as growth, against the confrontation reducing the number
  q19  the Cold War producing the alliances, against the alliances producing it
  q24  fighting falling outside the superpowers, against falling on their own soil

WHAT IS DELIBERATELY NOT KEYED, and this is the substantive judgement in this
module. KC-6.2.IV.D says the Cold War led to nuclear proliferation AND to proxy
wars. It does NOT say that proliferation is why the superpowers fought through
clients rather than each other, and it does not say the two never met in
battle. Both are familiar and both would read well; neither is in the CED, so
neither is keyed anywhere here. Nor does any key assign responsibility for a
proxy war to one superpower: the framework describes the pattern and not the
culprit, and that is live political ground on which this bank takes no side.
Item 28 exists to make the same point to the student, by asking what the
framework's silence about differing methods actually permits them to claim.

Item 7 is the one item resting on the CED's ILLUSTRATIVE EXAMPLES rather than
on a Key Concept, and its stem says so.

NEGATIVE CONTROL: `python3 verify_w8_3.py --selftest`.
"""
import sys

import cg_check as cg
import wh_check as wh
import w8_3

T_ALLIANCE = w8_3._T_ALLIANCE
T_NUCLEAR = w8_3._T_NUCLEAR
T_PROXY = w8_3._T_PROXY

M55 = "Member states, 1955"
M75 = "Member states, 1975"
HOLDERS = "States possessing nuclear weapons"
DECADE = "Decade (hypothetical record)"
BETWEEN = "Armed conflicts between states"
WITHIN = "Armed conflicts within a single state"


def q6(table, item):
    labs = cg.labels(table)
    assert len(labs) == 2, f"the key speaks of two alliances; the table holds {len(labs)}"
    before = {lab: cg.cell(table, lab, M55) for lab in labs}
    after = {lab: cg.cell(table, lab, M75) for lab in labs}
    gained = [lab for lab in labs if after[lab] > before[lab]]
    lost = [lab for lab in labs if after[lab] < before[lab]]
    assert len(gained) == 1 and len(lost) == 1, (
        f"the key needs exactly one alliance gaining and one losing; got {gained} and {lost}")
    assert after[labs[0]] != after[labs[1]], "'the same membership in 1975' must be false"
    smaller55 = min(labs, key=lambda lab: before[lab])
    larger75 = max(labs, key=lambda lab: after[lab])
    assert smaller55 != larger75, \
        "'the smaller in 1955 was the larger in 1975' must be false"
    return (f"membership goes {before} to {after}: {gained[0]} gains and {lost[0]} loses, "
            f"so 'both gained' and 'both lost' are false as well")


def q8(table, item):
    vals = cg.col(table, HOLDERS)
    assert all(b > a for a, b in zip(vals, vals[1:])), f"the count does not rise throughout: {vals}"
    assert vals[-1] > 5 * vals[0], \
        f"'more than five times its starting value' recomputes to {vals[-1] / vals[0]:.1f}"
    steps = [b - a for a, b in zip(vals, vals[1:])]
    assert steps[-1] < max(steps), \
        "'the largest single increase came in the last decade' must be false"
    assert vals[-1] != 2 * vals[0], "'the number doubled over the period' must be false"
    assert len(set(vals[1:])) > 1, "'unchanged from the 1950s onward' must be false"
    return (f"holders run {vals}, rising at every step, ending at "
            f"{vals[-1] / vals[0]:.1f} times the first value, with steps {steps}")


def q12(table, item):
    labs = cg.labels(table)
    btw = {lab: cg.cell(table, lab, BETWEEN) for lab in labs}
    wit = {lab: cg.cell(table, lab, WITHIN) for lab in labs}
    for lab in labs:
        assert wit[lab] > btw[lab], (
            f"{lab}: {wit[lab]} within against {btw[lab]} between, so the key fails there")
    assert not any(btw[lab] > wit[lab] for lab in labs), \
        "'between outnumbered within in every region' must be false"
    fewest_btw = cg.ranked(table, BETWEEN)[-1]
    fewest_wit = cg.ranked(table, WITHIN)[-1]
    assert not (fewest_btw == "Asia" and fewest_wit == "Asia"), \
        "'Asia recorded the fewest of both kinds' must be false"
    assert len(set(wit.values())) > 1, \
        "'the same number within a single state in all three regions' must be false"
    assert min(btw.values()) > 0, "'Africa recorded none between states' must be false"
    return (f"between-state counts {btw} against within-state counts {wit}: the second "
            f"exceeds the first in every region, and each distractor recomputes false")


TABLE_CHECKS = {6: q6, 8: q8, 12: q12}

CLAIMS = [
 ("new military alliances that the Cold War produced",
  "KC-6.2.IV.D states that the Cold War produced new military alliances, including NATO and the Warsaw Pact. A mutual defense pledge with a joint command is the characteristic form of such an alliance, and is neither a disarmament measure nor a commercial or colonial instrument."),
 ("same instrument, a standing military alliance",
  "KC-6.2.IV.D pairs NATO and the Warsaw Pact in one sentence, recording the same instrument taken up on both sides. Comparing how the two superpowers sought to maintain influence is this topic's learning objective, and matching instruments is the comparison the framework itself supports."),
 ("rival superpowers backed opposing sides",
  "KC-6.2.IV.D states that the Cold War led to proxy wars between and within postcolonial states in Latin America, Africa, and Asia. The framework locates such wars in other states, and the phrase between and within covers interstate and internal conflict alike."),
 ("Latin America, Africa, and Asia",
  "KC-6.2.IV.D names exactly these three regions as the setting of the proxy wars the Cold War produced. The regions matter because they identify where the confrontation was fought with arms while neither superpower's own territory was invaded."),
 ("both wars fought between separate states and armed conflicts inside a single state",
  "KC-6.2.IV.D says proxy wars occurred between and within postcolonial states, a formulation covering both forms. Restricting the category to one of them contradicts the framework's own wording, and postcolonial is the opposite of never colonized."),
 ("gained members over the period while the other lost members",
  "KC-6.2.IV.D makes the standing military alliances a product of the Cold War, so their membership is one measure of the confrontation's shape. The record is hypothetical, and q6 above recomputes the key together with the falsity of 'both gained', 'both lost' and the reversal of the two."),
 ("Angolan Civil War",
  "The CED prints the Korean War, the Angolan Civil War and the Sandinista-Contras conflict in Nicaragua as the ILLUSTRATIVE EXAMPLES accompanying KC-6.2.IV.D's statement about proxy wars. Every distractor lists conflicts the framework places in earlier units."),
 ("rose in every decade recorded and ended more than five times its starting value",
  "KC-6.2.IV.D states that the Cold War led to nuclear proliferation, and a rising count of states holding such weapons is what proliferation names. The record is hypothetical, and q8 above recomputes both halves of the key and the falsity of each distractor."),
 ("spread of nuclear weapons to a growing number of states",
  "KC-6.2.IV.D names nuclear proliferation among the Cold War's effects, in a sentence about the confrontation's spread rather than its containment. Proliferation is growth in the number of holders, which is the opposite of the disarmament and transfer options offered."),
 ("a proxy war fought within a postcolonial state",
  "KC-6.2.IV.D states that the Cold War led to proxy wars between and within postcolonial states. Factions inside one newly independent state acquiring rival great-power sponsors is that pattern in its internal form."),
 ("became the ground on which the superpowers' proxy wars were fought",
  "KC-6.2.IV.D locates proxy wars between and within postcolonial states in Latin America, Africa, and Asia, which connects the end of empire directly to the superpower confrontation. KC-6.2.I.C places the achievement of independence in the same postwar years, so the two processes overlap rather than succeed one another."),
 ("conflicts within a single state outnumbered conflicts between states",
  "KC-6.2.IV.D says proxy wars occurred between and within postcolonial states, and the relative weight of the two kinds is what a count of this shape reports. The figures are hypothetical; q12 above recomputes the key and the falsity of the reversed comparison, which is why the anchor names both kinds in order."),
 ("reduced the number of states holding nuclear weapons",
  "KC-6.2.IV.D lists nuclear proliferation among the Cold War's effects, so a claim that the confrontation reduced the number of nuclear-armed states reverses the framework's own sentence and is the statement not supported. The other four restate the alliances, the proxy wars, the regions and the proliferation."),
 ("arms and advisers by a different superpower",
  "KC-6.2.IV.D describes proxy wars as a product of the Cold War fought within postcolonial states, so rival sponsorship is what makes a conflict one. Duration, colonial past and press coverage do not distinguish one war from another, and every postcolonial state satisfies the colonial-past test by definition."),
 ("drawn into a local contest by the local participants themselves",
  "KC-6.2.IV.D places proxy wars within postcolonial states, and an appeal of this kind shows one mechanism by which a local contest acquired superpower sponsors. A request records what its author sought, not what was delivered, what the recipient intended, or how the contest ended."),
 ("standing commitment among states, while a proxy war is armed conflict in which rival sponsors back opposing sides",
  "KC-6.2.IV.D lists new military alliances and proxy wars as two separate products of the Cold War in a single sentence. The alliances are standing mutual commitments; the proxy wars are the fighting, located between and within postcolonial states rather than in Europe."),
 ("Proxy wars fought between and within postcolonial states",
  "KC-6.2.IV.D states that the Cold War led to proxy wars between and within postcolonial states in Latin America, Africa, and Asia. A complaint that outsiders' disputes are settled locally with local casualties describes that pattern from inside one of those states."),
 ("Each built a military alliance and each backed clients in conflicts outside its own territory",
  "KC-6.2.IV.D names new military alliances, including NATO and the Warsaw Pact, together with proxy wars between and within postcolonial states, placing both instruments on both sides. The framework does not describe either superpower abstaining from alliances, from nuclear weapons or from the postcolonial world."),
 ("Cold War came first, and new military alliances, nuclear proliferation and proxy wars followed",
  "KC-6.2.IV.D makes the Cold War the subject and the three developments its products. Every distractor reverses that direction, so the anchor carries the ordering and not the list alone."),
 ("produced standing military blocs on both sides",
  "KC-6.2.IV.D states that the Cold War produced new military alliances, including NATO and the Warsaw Pact, which is the condition that makes joining one an available choice in 1955. The framework places none of the alternative arrangements the distractors describe in this period."),
 ("wars the Cold War led to, fought with rival superpower backing",
  "KC-6.2.IV.D states that the Cold War led to proxy wars between and within postcolonial states, which is a claim about their relation to the confrontation rather than about their locality. The framework does not describe them as fought at home by the superpowers, as judicial, as prewar or as commercial."),
 ("number of separate states that had acquired nuclear weapons",
  "KC-6.2.IV.D names nuclear proliferation among the Cold War's effects, and proliferation is the spread of the weapons to more holders. Civilian power generation, drills, publications and budgets measure adjacent things rather than the number of states holding the weapons."),
 ("reasoning by which a local conflict was absorbed into the superpower confrontation",
  "KC-6.2.IV.D states that the Cold War led to proxy wars between and within postcolonial states, and this document shows the step by which a distant conflict became one, the rival's involvement being offered as the reason to intervene. The report bears on none of the alliance, arsenal, domestic or decolonization questions."),
 ("fell largely on states outside the two superpowers",
  "KC-6.2.IV.D places proxy wars between and within postcolonial states in Latin America, Africa, and Asia, locating the fighting outside the superpowers and outside Europe. The reversed claim is a distractor, so the anchor carries where the fighting fell and where it did not."),
 ("local origins and acquired an additional superpower dimension",
  "KC-6.2.IV.D describes proxy wars as fought within postcolonial states, a formulation presupposing both a conflict located in such a state and a superpower rivalry running through it. Each of the two accounts reports one of those layers, and the framework's phrasing accommodates both."),
 ("census recording the population of a nonaligned state",
  "KC-6.2.IV.D identifies the alliances by their character as standing military commitments, so treaty texts, accession lists, joint exercises and accession debates all bear on them directly. A population count for a state outside both blocs speaks to none of that, which is why it is the least useful of the five."),
 ("Proxy wars fought in states far from either superpower's own territory",
  "KC-6.2.IV.D states that the Cold War led to proxy wars between and within postcolonial states in Latin America, Africa, and Asia, which is a quarrel between two powers fought out on a third party's ground. The other options name developments the framework attaches to different statements."),
 ("records the same instruments, alliances and proxy conflicts, on both sides",
  "KC-6.2.IV.D names new military alliances, nuclear proliferation and proxy wars without assigning any of them to one side only. A claim that the two superpowers used entirely different means therefore runs past what the framework supports, which is the limit a comparison in this topic has to respect."),
 ("pursued through alliances, arms and wars in other states",
  "KC-6.2.IV.C.ii describes the confrontation as an ideological conflict and a power struggle between capitalism and communism across the globe; KC-6.2.IV.D records the alliances, the proliferation and the proxy wars that struggle produced. The key joins the two sentences and each distractor denies one of them."),
 ("spread nuclear weapons to more states, and set off wars between and within postcolonial states",
  "KC-6.2.IV.D states all three effects in one sentence: new military alliances including NATO and the Warsaw Pact, nuclear proliferation, and proxy wars between and within postcolonial states in Latin America, Africa, and Asia. Each distractor drops or contradicts at least one of the three."),
]

wh.run(w8_3, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
