"""Key audit for AP WORLD HISTORY: MODERN 7.2 Causes of World War I.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The gate is ``wh_check.run``, shared by the World History banks: it layers the
CED-citation rule (every ``why`` and every ``claim`` must name a Key Concept
code or a Learning Objective) and the figure-language rule on top of
``cg_check.check`` and ``es_check.style``. Nothing here is reinvented.

WHAT THE KEYS REST ON
---------------------
Every item rests on KC-6.2.IV.B.i, which is the whole of this topic's required
content: "The causes of World War I included imperialist expansion and
competition for resources. In addition, territorial and regional conflicts
combined with a flawed alliance system and intense nationalism to escalate the
tensions into global conflict."

  imperialist expansion            items 1, 7, 15, 23, 25, 27
  competition for resources        items 1, 8, 10, 24, 27
  territorial and regional conflict items 5, 18, 28
  the flawed alliance system       items 4, 6, 16, 22
  intense nationalism              items 5, 12, 14
  the combination and its scale    items 3, 13, 17, 19, 26, 29

Item 2 is the exclusion test: the global economic crisis engendered by the
Great Depression belongs to KC-6.2.IV.B.ii, the causes of the SECOND war, and
is the most attractive wrong answer available. Items 9 and 30 rest on that same
sentence for the unsustainable peace settlement after World War I. Item 20
rests on KC-6.1.III.C.i, new military technology leading to increased levels of
wartime casualties. Item 11 rests on Unit 7 Learning Objective B, item 29 on
suggested skill 1.B, and item 21 on the limits a source's purpose places on its
use.

WHAT IS NOT KEYED, deliberately: no date, no assassination, no mobilisation
order, no battle, no named alliance bloc and no treaty clause. The framework
states none of them. No item asks which cause mattered most, because
KC-6.2.IV.B.i lists the causes without ranking them; relative significance is
Unit 7 Learning Objective I, in topic 7.9.

DATA ITEMS: 7 and 8 carry tables of explicitly illustrative data. Each keyed
conclusion is recomputed below from that table alone, and each check also
falsifies the four distractors against the same numbers.

NEGATIVE CONTROLS: ``python3 verify_w7_2.py --selftest`` rotates every key in
turn, breaks every anchor in turn, corrupts every cell of both tables, injects
each banned notation form and each figure-language form, strips the citation
from a ``why`` and from a ``claim``, and duplicates a choice -- each of which
must raise FOR ITS OWN REASON. Positive controls run too, so a gate that
rejected everything would fail rather than look thorough.
"""
import sys

import cg_check as cg
import wh_check
import w7_2

EARLY = "Overseas territory held in 1880 (thousands of square kilometers)"
LATE = "Overseas territory held in 1910 (thousands of square kilometers)"
RUBBER = "Share of its rubber consumed that is imported (percent)"
IRON = "Share of its iron ore consumed that is imported (percent)"


def q7(table, item):
    early = dict(zip(cg.labels(table), cg.col(table, EARLY)))
    late = dict(zip(cg.labels(table), cg.col(table, LATE)))
    grew = [lab for lab in early if late[lab] > early[lab]]
    assert len(grew) == len(early), f"every power must expand; only {grew} did"
    ratios = {lab: late[lab] / early[lab] for lab in early}
    # Pin the values, not just their order: with only the ordering asserted, a
    # corrupted cell in the earlier column often leaves the ranking intact and
    # the check sleeps through it. Every power at least doubles here.
    assert all(r > 2 for r in ratios.values()), f"every holding must at least double; got {ratios}"
    assert ratios["Power C"] > 10 and ratios["Power A"] < 5, \
        f"the spread of growth multiples has changed: {ratios}"
    order = sorted(ratios, key=ratios.get, reverse=True)
    top, second = ratios[order[0]], ratios[order[1]]
    assert top > second, "the largest growth multiple must be unique"
    assert order[0] == "Power C", f"largest multiple belongs to {order[0]}, not Power C"
    assert order[0] != "Power A", "'Power A grew by the largest factor' must be false"
    assert len(set(late.values())) > 1, "'equal holdings at the later date' must be false"
    return (f"every holding is larger at the later date and the growth multiples are "
            f"{ {k: round(v, 2) for k, v in ratios.items()} }, so the largest belongs to {order[0]}")


def q8(table, item):
    rubber = dict(zip(cg.labels(table), cg.col(table, RUBBER)))
    iron = dict(zip(cg.labels(table), cg.col(table, IRON)))
    assert set(rubber.values()) == {100.0}, \
        f"the keyed 'entirely imported' column must be 100 for every power; got {rubber}"
    order = sorted(iron, key=iron.get, reverse=True)
    assert iron[order[0]] > iron[order[1]], "the largest second-column share must be unique"
    assert order[0] == "Power B", f"most import-dependent for the second material is {order[0]}"
    assert order[0] != "Power C", "'Power C is the most import-dependent' must be false"
    assert min(iron.values()) > 0, "'each supplies all of its own needs' must be false"
    assert len(set(iron.values())) > 1, "'depend to the same degree' must be false"
    return (f"the first column is 100 for all three powers and the second column ranks "
            f"{order}, so the maximum in the second column is {order[0]}'s")


TABLE_CHECKS = {7: q7, 8: q8}

CLAIMS = [
 ("expansion together with competition for resources",
  "KC-6.2.IV.B.i: the causes of World War I included imperialist expansion and competition for resources. Acquiring distant territory is the first and securing a rubber supply before a rival does is the second, so the source supplies one of each."),
 ("global economic depression",
  "KC-6.2.IV.B.i names imperialist expansion, competition for resources, territorial and regional conflicts, a flawed alliance system and intense nationalism. The global economic crisis engendered by the Great Depression belongs to KC-6.2.IV.B.ii, the causes of the second war."),
 ("flawed alliance system, and intense nationalism",
  "KC-6.2.IV.B.i: territorial and regional conflicts combined with a flawed alliance system and intense nationalism to escalate the tensions into global conflict. The three named terms are the framework's own."),
 ("escalate regional tensions into a conflict on a global scale",
  "KC-6.2.IV.B.i calls the alliance system flawed and places it among the things that escalated tensions into global conflict. Escalation is the function the sentence assigns it, and the same sentence names other causes beside it."),
 ("Intense nationalism joined to a territorial dispute",
  "KC-6.2.IV.B.i names territorial and regional conflicts and intense nationalism among the things that combined. A claim of national superiority is the second and a demand for a neighbouring province is the first, so the anchor carries both."),
 ("flawed alliance system, which bound states to one another",
  "KC-6.2.IV.B.i has the alliance system combining with regional conflict and nationalism to escalate tensions into global conflict. It is the cause in that list which draws additional states into a quarrel not originally theirs."),
 ("Power C multiplied its holdings by the largest factor",
  "KC-6.2.IV.B.i names imperialist expansion among the causes, and this item asks a student to read expansion out of data rather than to recall a case. Recomputed in q7 above from the illustrative table alone, including that the swapped distractor naming the other power is false."),
 ("Power B is the most import-dependent for the other",
  "KC-6.2.IV.B.i names competition for resources among the causes, and a state that must import what its industry consumes has an interest in the territory supplying it. Recomputed in q8 above from the illustrative table alone, including the swapped distractor."),
 ("named among the causes of the next war",
  "KC-6.2.IV.B.ii lists the unsustainable peace settlement after World War I first among the causes of World War II, which is the framework's own statement of a consequence of the first war."),
 ("Competition for resources",
  "KC-6.2.IV.B.i names competition for resources among the causes of World War I. Two industrial states seeking exclusive access to the same supply is that competition; the alternatives are other causes in the same sentence or belong to KC-6.2.IV.B.ii."),
 ("causes and the consequences of the First World War",
  "Unit 7 Learning Objective B asks students to explain the causes and consequences of World War I, so an inquiry framed in those terms restates the objective."),
 ("intense nationalism the framework names among the war's causes",
  "KC-6.2.IV.B.i names intense nationalism among the things that combined to escalate tensions. Teaching national unity and the hostility of neighbours cultivates exactly that, and the source mentions no resource, alliance, economic policy or treaty."),
 ("escalated until states in many parts of the world were at war",
  "KC-6.2.IV.B.i describes tensions being escalated into global conflict from territorial and regional conflicts. The global scale is the product of escalation rather than a property the original dispute had."),
 ("one of several things that combined, not as a cause acting by itself",
  "KC-6.2.IV.B.i lists two causes and then has three more combine. Nationalism appears as one term of a combination, so an account resting on it alone drops the rest of the sentence."),
 ("rival states claiming the same overseas territory",
  "KC-6.2.IV.B.i names imperialist expansion among the causes. Rival claims to the same territory bear on that cause directly, whereas schools, crops, newspapers and titles bear on it only through inferences the framework does not supply."),
 ("alliance system that the framework describes as flawed",
  "KC-6.2.IV.B.i names a flawed alliance system among the things that escalated tensions into global conflict. A written undertaking to join a partner's war is that system in operation."),
 ("lists several causes and describes three of them as combining",
  "KC-6.2.IV.B.i names imperialist expansion and competition for resources, then has territorial and regional conflicts combine with a flawed alliance system and intense nationalism. Both the list and the word combined are in the sentence."),
 ("territorial and regional conflict of the kind the framework names",
  "KC-6.2.IV.B.i names territorial and regional conflicts among the things that combined to escalate tensions. A disputed annexation objected to by a neighbouring rival is a conflict about territory in a region."),
 ("operating together rather than in isolation",
  "KC-6.2.IV.B.i uses combined for three of its causes and adds the others with included and in addition, so joint operation is asserted and no ranking is given. Relative significance is left to Unit 7 Learning Objective I."),
 ("New military technology led to increased levels of wartime casualties",
  "KC-6.1.III.C.i states exactly this, and the framework attaches it to the conduct of the First World War. The four alternatives assert outcomes that appear nowhere in the framework."),
 ("reason to omit causes that implicate its state",
  "KC-6.2.IV.B.i names causes, including imperialist expansion and competition for resources, that implicate more than one state. A belligerent government's justification has an interest in omitting them, which limits the source's use without making it worthless."),
 ("drew each into a quarrel that began elsewhere",
  "KC-6.2.IV.B.i describes a flawed alliance system combining with regional conflict and nationalism to escalate tensions into global conflict. Alliances are what place a state in a war it had no quarrel of its own to fight."),
 ("expanding into other regions and competing for their resources",
  "KC-6.2.IV.B.i places imperialist expansion and competition for resources among the causes, and both operate across regions. An essay on the war's global scale is best opened with the process that had already made the powers' interests global."),
 ("evidenced by rival claims to the same mineral-bearing territory",
  "KC-6.2.IV.B.i names competition for resources as a cause, and rival claims to a mineral-bearing territory are evidence of that competition. The other pairings attach evidence to a cause it does not bear on."),
 ("Imperialist expansion",
  "KC-6.2.IV.B.i names imperialist expansion among the causes. A source describing powers that have divided the world and can grow only at one another's expense describes that expansion, not an alliance, a settlement, a regime type or an economic policy."),
 ("more than one domain, including the economic and the political",
  "KC-6.2.IV.B.i names competition for resources and imperialist expansion alongside territorial conflict, alliances and nationalism, so the sentence spans economic and political causes rather than one kind."),
 ("Imperialist expansion and competition for resources",
  "KC-6.2.IV.B.i names these two in the same clause. Justifying expansion by the need for raw materials is the point at which they meet, and neither the alliance system nor nationalism figures in that reasoning."),
 ("territorial and regional conflicts were among the things that escalated tensions",
  "KC-6.2.IV.B.i lists territorial and regional conflicts first among the three that combined to escalate tensions, so removing them removes one term of the combination while leaving the separate claims untouched."),
 ("process in which several causes combined over time",
  "Suggested skill 1.B asks students to explain a historical development or process, and KC-6.2.IV.B.i describes causes that combined to escalate tensions, which is a process rather than an event."),
 ("own list of causes, including an unsustainable peace settlement",
  "KC-6.2.IV.B.i gives the first war's causes and KC-6.2.IV.B.ii the second war's, the latter including the unsustainable peace settlement after World War I and the global economic crisis engendered by the Great Depression. The lists overlap but differ."),
]

wh_check.run(w7_2, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
