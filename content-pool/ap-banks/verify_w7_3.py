"""Key audit for AP WORLD HISTORY: MODERN 7.3 Conducting World War I.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The gate is ``wh_check.run``, shared by the World History banks: the
CED-citation rule and the figure-language rule on top of ``cg_check.check`` and
``es_check.style``. Nothing is reinvented here.

WHAT THE KEYS REST ON
---------------------
KC-6.2.IV.A.i: World War I was the first total war. Governments used a variety
of strategies, including political propaganda, art, media, and intensified
forms of nationalism, to mobilize populations (both in the home countries and
the colonies) for the purpose of waging war.

  the phrase "first total war"        items 2, 11, 22, 25
  the named strategies                items 3, 10, 12, 19, 26, 28
  the purpose clause                  items 1, 9, 23
  home countries AND colonies         items 4, 8, 16, 18, 27
  nationalism in its second role      item 17
  government rather than army         item 14

KC-6.1.III.C.i: new military technology led to increased levels of wartime
casualties -- items 5, 7, 13, 20, 21, 29. Items 5 and 13 turn on the DIRECTION
of that sentence, so their anchors carry both clauses; the reversed reading is
the plausible error and would otherwise match a bare mention of technology.

Items 6 and 24 rest on suggested skill 3.B, identify the evidence used in a
source to support an argument; item 30 on Unit 7 Learning Objective C; item 15
on the limit a propaganda source places on its own use.

BOUNDARY WITH 7.7, held by item 11: KC-6.2.IV.A.ii and KC-6.1.III.C.ii add
ideologies used to mobilize a state's resources, the repression of basic
freedoms in totalitarian states, and the atomic bomb and fire-bombing. None of
that is keyed in this module; it belongs to the second war's conduct.

WHAT IS NOT KEYED, deliberately: no battle, no date, no weapon by name, no
casualty total, and no real poster, painting or newspaper. The framework names
none of them, and KC-6.1.III.C.i asserts a direction without a number, so no
item asks a student to quantify it.

DATA ITEMS: 7 and 8 carry tables of explicitly illustrative data; each keyed
conclusion is recomputed below from that table alone and each distractor is
falsified against the same numbers.

NEGATIVE CONTROLS: ``python3 verify_w7_3.py --selftest`` rotates every key,
breaks every anchor, corrupts every cell of both tables, injects each banned
notation and figure-language form, strips the citation from a ``why`` and a
``claim``, and duplicates a choice -- each must raise for its own reason, and
positive controls run alongside so a gate that rejected everything would fail.
"""
import sys

import cg_check as cg
import wh_check
import w7_3

ROUNDS = "Rounds of rapid-fire artillery per day"
RATE = "Casualties per thousand troops per month"
HOME = "Troops raised in the home country (thousands)"
COLONIAL = "Troops raised in its colonies (thousands)"


def q7(table, item):
    by_rounds = cg.ranked(table, ROUNDS)
    by_rate = cg.ranked(table, RATE)
    assert len(set(cg.col(table, ROUNDS))) == len(by_rounds), "artillery values must be distinct"
    assert len(set(cg.col(table, RATE))) == len(by_rate), "casualty rates must be distinct"
    assert by_rounds == by_rate, f"orders differ: {by_rounds} against {by_rate}"
    assert by_rounds[-1] != by_rate[0], "'the sector firing fewest rounds has the highest rate' must be false"
    assert min(cg.col(table, RATE)) > 0, "'no casualties at all' must be false"
    # The inverse reading is the swapped distractor; it must be false too.
    assert by_rounds != list(reversed(by_rate)), "'heavier fire, lower casualties' must be false"
    return (f"ranking by rounds fired gives {by_rounds} and by casualty rate {by_rate}; "
            "the two orders agree and the inverse reading is false on these numbers")


def q8(table, item):
    home = dict(zip(cg.labels(table), cg.col(table, HOME)))
    colonial = dict(zip(cg.labels(table), cg.col(table, COLONIAL)))
    assert min(colonial.values()) > 0, "'only one power raised colonial troops' must be false"
    order = sorted(colonial, key=colonial.get, reverse=True)
    assert colonial[order[0]] > colonial[order[1]], "the largest colonial total must be unique"
    assert order[0] == "Power B", f"most colonial troops raised by {order[0]}, not Power B"
    top_home = max(home, key=home.get)
    assert top_home == "Power A", f"largest home army belongs to {top_home}, not Power A"
    assert top_home != order[0], \
        "'the power with the largest home army also raised the most colonial troops' must be false"
    assert all(colonial[lab] < home[lab] for lab in home), \
        "'each raised more colonial than home troops' must be false"
    return (f"every colonial total is above zero, the largest belongs to {order[0]}, "
            f"and the largest home-country army belongs to {top_home}, a different power")


TABLE_CHECKS = {7: q7, 8: q8}

CLAIMS = [
 ("mobilization of a whole population for the purpose of waging war",
  "KC-6.2.IV.A.i calls World War I the first total war and describes governments mobilizing populations for the purpose of waging war. A notice telling factory and farm workers their work is part of the fighting is that mobilization addressed to civilians."),
 ("at home and in the colonies for the purpose of waging war",
  "KC-6.2.IV.A.i pairs the phrase first total war directly with mobilizing populations both in the home countries and the colonies for the purpose of waging war. The scale is the scale of mobilization inside belligerent states."),
 ("art, media, and intensified forms of nationalism",
  "KC-6.2.IV.A.i lists political propaganda, art, media, and intensified forms of nationalism as the strategies of mobilization. The competing lists belong to KC-6.3.I.A.i or appear nowhere in the framework."),
 ("in the colonies were mobilized as well as those in the home countries",
  "KC-6.2.IV.A.i's parenthesis covers both the home countries and the colonies at once, so the anchor carries both clauses and an answer exempting either side contradicts the sentence."),
 ("New military technology led to increased levels of wartime casualties",
  "KC-6.1.III.C.i, verbatim. The direction is the substance of the claim, so the anchor carries the cause and the effect together and the reversed distractor cannot match it."),
 ("evidence for the claim that the whole population is engaged",
  "Suggested skill 3.B asks students to identify the evidence a source uses to support its argument. The claim is that victory depends on the whole nation, and the statement about new factory workers supports it, which is the relation KC-6.2.IV.A.i calls total war."),
 ("heavier use of rapid-fire artillery record the higher casualty rates",
  "KC-6.1.III.C.i asserts that new military technology led to increased levels of wartime casualties, and this item asks a student to read that association out of data. Recomputed in q7 above from the illustrative table alone, including the inverse distractor."),
 ("Power B raised the most colonial troops",
  "KC-6.2.IV.A.i states that populations were mobilized in the home countries and the colonies. Recomputed in q8 above from the illustrative table alone, including that the power with the largest home army is not the one with the largest colonial contingent."),
 ("To mobilize populations for the purpose of waging war",
  "KC-6.2.IV.A.i gives exactly this purpose for the propaganda, art and media governments produced. The purpose clause is part of the sentence and none of the alternatives appears in it."),
 ("use of art among the strategies of wartime mobilization",
  "KC-6.2.IV.A.i names art explicitly among the strategies, alongside political propaganda, media and intensified forms of nationalism, used to mobilize populations for war."),
 ("It was the first total war",
  "KC-6.2.IV.A.i opens with this statement about World War I. The four alternatives are drawn from KC-6.2.IV.A.ii and KC-6.1.III.C.ii, which the framework attaches to the Second World War in topic 7.7."),
 ("five-year plans",
  "KC-6.2.IV.A.i names political propaganda, art, media and intensified forms of nationalism. Control of the national economy through the Five Year Plans is KC-6.3.I.A.i, an interwar Soviet policy rather than a wartime mobilization strategy."),
 ("new technology coming first and the higher casualties following from it",
  "KC-6.1.III.C.i makes the technology the cause and the casualties the effect. The anchor carries both clauses because the reversed account is the plausible error."),
 ("populations to be mobilized were civilian and lay outside the army",
  "KC-6.2.IV.A.i assigns the mobilizing to governments and directs it at populations in the home countries and the colonies, who are not under military command."),
 ("wanted the population to do, rather than whether the population complied",
  "KC-6.2.IV.A.i identifies propaganda and art as government strategies for mobilizing populations, so such a source documents the strategy itself. Whether it worked is a separate question the source cannot settle."),
 ("recruitment and requisitioning carried out in colonial territories",
  "KC-6.2.IV.A.i states that populations were mobilized both in the home countries and the colonies, so colonial recruitment records bear on the half of the sentence the claim denies."),
 ("method governments used to mobilize populations for war",
  "KC-6.2.IV.A.i lists intensified forms of nationalism among the strategies of mobilization, while KC-6.2.IV.B.i places intense nationalism among the war's causes. The same phenomenon carries two roles in the framework, and this topic is the mobilizing one."),
 ("mobilization extended to the colonies and not only to the home countries",
  "KC-6.2.IV.A.i includes the colonies in the mobilization. An order compelling colonial villages to supply labour and grain is that mobilization in a colonial setting."),
 ("use of media as a strategy of mobilization",
  "KC-6.2.IV.A.i names media among the strategies governments used to mobilize populations for the purpose of waging war."),
 ("rise sharply in the months after a new weapon is introduced",
  "KC-6.1.III.C.i asserts that new military technology led to increased levels of wartime casualties, so a rise following an introduction is evidence for that direction while flat totals or an unissued weapon leave it unsupported."),
 ("fall on the sectors where the newest weapons are concentrated",
  "KC-6.1.III.C.i ties higher casualties to new technology, so a fall exactly where that technology is concentrated is the observation the claim cannot absorb. The other findings bear on KC-6.2.IV.A.i instead."),
 ("conduct of a total war, in which the whole society is turned to the war effort",
  "KC-6.2.IV.A.i calls World War I the first total war and describes governments mobilizing populations for waging war; direction of industry, rationing and conscripted labour are that mobilization reaching civilian life."),
 ("manage what the population believed about the war while mobilization continued",
  "KC-6.2.IV.A.i names media and political propaganda among government strategies for mobilizing populations, which is why the framework treats the press as a channel governments managed rather than as a neutral record."),
 ("list of damaged towns, offered in support of the claim about national survival",
  "Suggested skill 3.B asks which part of a source is the evidence and which the claim. The anchor carries both halves in order, because the reversed reading is the plausible error; the speech also illustrates the intensified nationalism of KC-6.2.IV.A.i."),
 ("identifies the First World War as the first total war",
  "KC-6.2.IV.A.i states that World War I was the first total war, and KC-6.2.IV.A.ii separately states that World War II was a total war. A claim that earlier wars already met the description contradicts the first."),
 ("produced by a government as a strategy for mobilizing its population",
  "KC-6.2.IV.A.i attributes political propaganda to governments and gives its purpose as mobilizing populations for waging war, so authorship and purpose are the framework's own criteria."),
 ("extends the war effort to populations far from where most of the fighting",
  "KC-6.2.IV.A.i includes colonial populations in the mobilization, which places the war's demands on societies distant from the fronts and is part of what makes the mobilization total."),
 ("output of the government's own propaganda and information offices",
  "KC-6.2.IV.A.i names political propaganda, art and media among the strategies governments used to mobilize populations, so the offices responsible for them document the effort directly."),
 ("asserted to have raised the level of wartime casualties",
  "KC-6.1.III.C.i states that new military technology led to increased levels of wartime casualties, while KC-6.2.IV.A.i attributes propaganda and intensified nationalism to governments and includes colonial populations. Only the keyed pairing states what the framework states."),
 ("methods did governments conduct the war and mobilize their populations",
  "Unit 7 Learning Objective C asks students to explain how governments used a variety of methods to conduct war, and KC-6.2.IV.A.i supplies those methods."),
]

wh_check.run(w7_3, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
