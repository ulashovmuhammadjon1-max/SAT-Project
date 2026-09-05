"""Key audit for AP WORLD HISTORY: MODERN 7.6 Causes of World War II.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor; ``claim``
states what the key rests on, for a human to audit. The gate is
``wh_check.run``, shared by the World History banks.

WHAT THE KEYS REST ON
---------------------
KC-6.2.IV.B.ii is the whole of this topic's required content: "The causes of
World War II included the unsustainable peace settlement after World War I, the
global economic crisis engendered by the Great Depression, continued imperialist
aspirations, and especially the rise to power of fascist and totalitarian
regimes that resulted in the aggressive militarism of Nazi Germany under Adolf
Hitler."

  the unsustainable peace settlement   items 1, 12, 14, 16, 19, 20, 23, 27
  the global economic crisis           items 4, 7, 9, 17, 25, 28
  continued imperialist aspirations    items 5, 11, 14
  the rise to power of the regimes     items 2, 3, 8, 15, 21, 26, 29, 30
  the word "included"                  items 6, 29
  the word "especially"                items 2, 15, 21, 29, 30

Item 3 is the SWAP item: the framework says the rise to power of those regimes
RESULTED IN the aggressive militarism of Nazi Germany under Adolf Hitler, and
the distractor reverses it, so that anchor carries both clauses. Items 12 and 20
are the other two where a reversal is the plausible error, and their anchors
carry the direction as well.

Items 10, 16, 17, 18 and 27 rest on suggested skill 2.C, the significance of a
source's point of view, purpose, historical situation and audience, including
how these limit its uses. Item 22 rests on Unit 7 Learning Objective F, and item
24 on KC-6.1.III.C.ii, which is the only consequence keyed anywhere in this
module.

Items 11, 12 and 13 compare the framework's TWO lists of causes: KC-6.2.IV.B.i
for the first war (imperialist expansion, competition for resources, territorial
and regional conflicts, a flawed alliance system, intense nationalism) and
KC-6.2.IV.B.ii for the second. Nothing else in this module reaches into topic
7.2's material.

WHAT IS NOT KEYED, deliberately: no date, treaty article, territorial claim,
battle, election, party name or casualty total. Adolf Hitler is named only
because KC-6.2.IV.B.ii names him, and nothing is asserted about him beyond that
sentence's own words. The relative significance of the causes of global conflict
belongs to Unit 7 Learning Objective I in topic 7.9; the only ranking used here
is the one the framework writes into this sentence with "especially".

DATA ITEMS: 7 and 8 carry tables of explicitly illustrative data, recomputed
below from the table alone, with each distractor falsified against the same
numbers.

NEGATIVE CONTROLS: ``python3 verify_w7_6.py --selftest`` rotates every key,
breaks every anchor, corrupts every cell of both tables, injects each banned
notation and figure-language form, strips the citation from a ``why`` and a
``claim``, and duplicates a choice; each must raise for its own reason, and
positive controls run alongside.
"""
import sys

import cg_check as cg
import wh_check
import w7_6

BASE = "Index of industrial output at the onset of the crisis"
LATER = "Index of industrial output three years later"
EARLY = "Share of government spending devoted to armed forces, earlier year (percent)"
LATE = "Share of government spending devoted to armed forces, later year (percent)"


def q7(table, item):
    base = dict(zip(cg.labels(table), cg.col(table, BASE)))
    later = dict(zip(cg.labels(table), cg.col(table, LATER)))
    # The keyed choice names Country D and a distractor names Country F, so the
    # rows the choices refer to must be the rows the table actually has.
    assert set(base) == {"Country D", "Country E", "Country F"}, \
        f"the choices refer to Countries D, E and F; the table holds {sorted(base)}"
    # The stem says the onset is SET AT one hundred in each country, so a table
    # whose bases differ no longer says what the stem says it says.
    assert set(base.values()) == {100.0}, \
        f"the onset index must be one hundred in every country; got {base}"
    risen = [k for k in base if later[k] >= base[k]]
    assert not risen, f"every country's later figure must be below its base; {risen} are not"
    fall = {k: base[k] - later[k] for k in base}
    order = sorted(fall, key=fall.get, reverse=True)
    assert fall[order[0]] > fall[order[1]], "the steepest fall must be unique"
    assert order[0] == "Country D", f"the steepest fall belongs to {order[0]}, not Country D"
    assert order[0] != "Country F", "'the steepest fall is in Country F' must be false"
    assert len([k for k in fall if fall[k] > 0]) == 3, \
        "'output falls in only one of the three countries' must be false"
    assert len(set(later.values())) > 1, \
        "'the three countries end at the same index' must be false"
    return (f"every country is based at one hundred, every later figure is lower, the falls "
            f"are {fall}, and the steepest belongs to {order[0]}")


def q8(table, item):
    early = dict(zip(cg.labels(table), cg.col(table, EARLY)))
    late = dict(zip(cg.labels(table), cg.col(table, LATE)))
    # The keyed choice names State P and a distractor names State R, so the rows
    # the choices refer to must be the rows the table actually has.
    assert set(early) == {"State P", "State Q", "State R"}, \
        f"the choices refer to States P, Q and R; the table holds {sorted(early)}"
    # A share of government spending cannot exceed the whole of it.
    for name, share in list(early.items()) + list(late.items()):
        assert 0 <= share <= 100, f"{name} reports a share of {share} percent, which is not a share"
    fallen = [k for k in early if late[k] <= early[k]]
    assert not fallen, f"every state's later share must exceed its earlier one; {fallen} do not"
    assert min(list(early.values()) + list(late.values())) > 0, \
        "'only one state devotes any spending to armed forces' must be false"
    rise = {k: late[k] - early[k] for k in early}
    order = sorted(rise, key=rise.get, reverse=True)
    assert rise[order[0]] > rise[order[1]], "the largest increase must be unique"
    assert order[0] == "State P", f"the largest increase belongs to {order[0]}, not State P"
    assert order[0] != "State R", "'the largest increase is in State R' must be false"
    top_early = max(early, key=early.get)
    assert rise[top_early] != max(rise.values()), \
        "'the state highest in the earlier year records the largest increase' must be false"
    return (f"every later share exceeds its earlier share, the increases in percentage points "
            f"are {rise}, the largest belongs to {order[0]}, and the state that began highest "
            f"was {top_early}")


TABLE_CHECKS = {7: q7, 8: q8}

CLAIMS = [
 ("unsustainable peace settlement that followed the First World War",
  "KC-6.2.IV.B.ii lists the unsustainable peace settlement after World War I first among the causes of World War II, so a memorandum arguing that the imposed borders cannot be held states that grievance rather than an economic, imperial or regime-based cause."),
 ("rise to power of fascist and totalitarian regimes",
  "KC-6.2.IV.B.ii places 'and especially' before the rise to power of fascist and totalitarian regimes. That qualifier is the framework's own ranking of one cause above the other three, which appear in the same list without it."),
 ("resulted in the aggressive militarism of Nazi Germany",
  "KC-6.2.IV.B.ii says the rise to power of fascist and totalitarian regimes resulted in the aggressive militarism of Nazi Germany under Adolf Hitler. The anchor carries both clauses because the reversed reading is the plausible error."),
 ("engendered by the Great Depression",
  "KC-6.2.IV.B.ii names the global economic crisis engendered by the Great Depression among the causes of World War II, supplying both the scale of the crisis and what engendered it."),
 ("carried on from the earlier period",
  "KC-6.2.IV.B.ii names CONTINUED imperialist aspirations, and KC-6.2.I.B records imperial states predominantly maintaining and in some cases enlarging their colonial holdings between the wars, so the adjective marks a continuity rather than a new departure."),
 ("members of the list rather than as a complete enumeration",
  "KC-6.2.IV.B.ii says the causes of World War II INCLUDED the four it names, which asserts membership and not completeness; the sentence ranks only one item, with the word 'especially', and does not order the rest."),
 ("steepest fall is in Country D",
  "KC-6.2.IV.B.ii names the global economic crisis engendered by the Great Depression among the causes of the war, and this item asks a student to read a crisis out of data. Recomputed in q7 above from the illustrative table alone, including each false distractor."),
 ("largest increase in percentage points is in State P",
  "KC-6.2.IV.B.ii names the aggressive militarism that resulted from the rise to power of fascist and totalitarian regimes, and rising military shares of spending are evidence bearing on it. Recomputed in q8 above from the illustrative table alone, including the swapped distractor."),
 ("global economic crisis that the framework counts among the causes",
  "KC-6.2.IV.B.ii names the global economic crisis engendered by the Great Depression among the causes of World War II, and collapsed orders with rising unemployment across several markets at once is a report of that crisis."),
 ("purpose is to justify that action",
  "Suggested skill 2.C asks how a source's point of view and purpose limit its uses, and KC-6.2.IV.B.ii names continued imperialist aspirations and aggressive militarism among the war's causes. A government explaining its own seizure of territory is the interested party."),
 ("named as imperialist expansion for the first war and as continued imperialist aspirations",
  "KC-6.2.IV.B.i names imperialist expansion among the causes of World War I and KC-6.2.IV.B.ii names continued imperialist aspirations among those of World War II, so imperialism is the element the two lists share."),
 ("named among the causes of the second",
  "KC-6.2.IV.B.ii opens its list of the causes of World War II with the unsustainable peace settlement after World War I, while KC-6.2.IV.B.i gives the earlier war its own causes; the settlement is the framework's stated link running forward from one war to the next, and the anchor carries the direction."),
 ("flawed alliance system",
  "KC-6.2.IV.B.i names a flawed alliance system, with territorial and regional conflicts and intense nationalism, among the things that escalated tensions into World War I, and KC-6.2.IV.B.ii's list for the second war names none of them."),
 ("continued imperialist aspirations joined to a grievance about the peace settlement",
  "KC-6.2.IV.B.ii names continued imperialist aspirations and the unsustainable peace settlement after World War I as two separate causes, and an appeal demanding colonial territory while blaming the settlement for the lost claim joins them."),
 ("lists political causes as well, and singles out the rise to power",
  "KC-6.2.IV.B.ii names one economic cause among four, and marks the rise to power of fascist and totalitarian regimes as especially important, so an economic account drops the cause the framework weights most."),
 ("joining a grievance about the peace settlement to a demand for rearmament",
  "Suggested skill 2.C asks what a source's purpose does to its usefulness, and a programme states intentions rather than achievements. KC-6.2.IV.B.ii names the unsustainable peace settlement and the rise to power of such regimes among the war's causes."),
 ("later report is written during the global economic crisis",
  "Suggested skill 2.C names historical situation among the things that shape a source's significance, and KC-6.2.IV.B.ii dates the global economic crisis to the Great Depression, so two reports separated by its onset describe different situations."),
 ("shaped for the people meant to receive it",
  "Suggested skill 2.C names audience among the things that shape a source's significance and limit its uses, and KC-6.2.IV.B.ii records aggressive militarism among the war's causes, which a government has different reasons to present differently at home and abroad."),
 ("justified those demands by the terms imposed on them in the settlement",
  "KC-6.2.IV.B.ii names the unsustainable peace settlement after World War I among the causes of World War II, so evidence that the later demands were framed by reference to the settlement's own terms connects it to the outbreak."),
 ("made the same demands before the settlement existed",
  "A cause cannot follow its effect, and KC-6.2.IV.B.ii names the settlement among the war's causes, so demands predating the settlement remove it from the chain; the anchor carries the ordering because the reversed reading is the plausible error."),
 ("list of the war's causes with one of them singled out",
  "KC-6.2.IV.B.ii states what caused World War II and marks one cause as especially important with the word 'especially', which is causation reasoning; mobilization is KC-6.2.IV.A.ii's subject in topic 7.7."),
 ("What caused the Second World War, and what followed from it",
  "Unit 7 Learning Objective F asks students to explain the causes and consequences of World War II, so a question framed as causes and what followed restates the objective."),
 ("could not be maintained, which is why it stands among the causes of the next war",
  "KC-6.2.IV.B.ii calls the peace settlement after World War I unsustainable and places it among the causes of World War II, so the adjective is doing explanatory work inside a sentence about why a second war came."),
 ("increased levels of wartime casualties, produced by new military technology and new tactics",
  "KC-6.1.III.C.ii states that new military technology and new tactics, including the atomic bomb, fire-bombing and the waging of total war, led to increased levels of wartime casualties, and Unit 7 Learning Objective F covers consequences as well as causes."),
 ("without stating that the crisis produced the regimes",
  "KC-6.2.IV.B.ii lists the global economic crisis and the rise to power of fascist and totalitarian regimes as two items in one list of the war's causes; listing them together states that each contributed and not that either produced the other."),
 ("aggressive militarism that the framework names among the causes",
  "KC-6.2.IV.B.ii names the aggressive militarism of Nazi Germany that resulted from the rise to power of fascist and totalitarian regimes among the war's causes, and conscription, a doubled army and demands on neighbours are that conduct."),
 ("helped to draft the settlement, so he has reason to defend it",
  "Suggested skill 2.C asks how point of view limits a source's uses, and KC-6.2.IV.B.ii names the unsustainable peace settlement after World War I among the causes of the second war, which is exactly the charge a drafter has reason to answer."),
 ("reaching beyond any single state's economy",
  "KC-6.2.IV.B.ii calls the crisis it names a GLOBAL economic crisis engendered by the Great Depression, which places it across economies rather than inside one."),
 ("single cause, and the framework identifies that cause as the Great Depression",
  "KC-6.2.IV.B.ii names four causes and marks one of them as especially important, so reducing the war to a single cause contradicts the sentence, and the framework's weighting falls on the regimes rather than on the depression."),
 ("with the rise of fascist and totalitarian regimes singled out",
  "KC-6.2.IV.B.ii lists an unsustainable peace settlement, a global economic crisis and continued imperialist aspirations, then marks the rise to power of fascist and totalitarian regimes with 'especially', so a summary must carry both the plurality and that ranking."),
]

wh_check.run(w7_6, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
