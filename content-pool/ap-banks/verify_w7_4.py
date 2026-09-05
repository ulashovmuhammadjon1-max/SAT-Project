"""Key audit for AP WORLD HISTORY: MODERN 7.4 Economy in the Interwar Period.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor; ``claim``
states what the key rests on, for a human to audit. The gate is
``wh_check.run``, shared by the World History banks.

WHAT THE KEYS REST ON
---------------------
KC-6.3.I.B: following World War I and the onset of the Great Depression,
governments began to take a more active role in economic life -- items 1, 2, 5,
7, 13, 14, 19, 21, 24, 26, 29, 30. Items 2 and 19 turn on the DIRECTION of that
sentence (a beginning, and an increase rather than a withdrawal), so their
anchors carry both halves.

KC-6.3.I.A.i: in the Soviet Union, the government controlled the national
economy through the Five Year Plans, often implementing repressive policies,
with negative repercussions for the population -- items 3, 8, 11, 12, 15, 20,
22, 27, 28, 30.

The CED's illustrative examples for government intervention in the economy --
the New Deal, the fascist corporatist economy, and governments with strong
popular support in Brazil and Mexico -- carry items 4, 9, 10, 16, 23, 24 and
29. Nothing is asserted about what any of those contained: an illustrative
example is printed as an instance, and the CED prints no detail about it.

Item 17 holds the boundary with topic 7.6: the same Great Depression appears in
KC-6.3.I.B as the crisis governments responded to and in KC-6.2.IV.B.ii among
the causes of the second war. The anchor carries both halves because the
swapped reading is the plausible error.

Items 6, 15, 20, 25 and 27 rest on suggested skill 2.C, the significance of a
source's point of view, purpose, historical situation and audience, including
how these limit the use of a source. Item 18 rests on Unit 7 Learning Objective
D and item 26 on this topic's reasoning process, comparison.

WHAT IS NOT KEYED, deliberately: no date, agency, statute, plan number, output
total or leader's name, and no verdict on whether any intervention succeeded.
KC-6.3.I.B records that governments became more active without evaluating the
result, and KC-6.3.I.A.i states repression and negative repercussions without
quantifying them.

DATA ITEMS: 7 and 8 carry tables of explicitly illustrative data, recomputed
below from the table alone, with every distractor falsified against the same
numbers.

NEGATIVE CONTROLS: ``python3 verify_w7_4.py --selftest`` rotates every key,
breaks every anchor, corrupts every cell of both tables, injects each banned
notation and figure-language form, strips the citation from a ``why`` and a
``claim``, and duplicates a choice; each must raise for its own reason, and
positive controls run alongside.
"""
import sys

import cg_check as cg
import wh_check
import w7_4

EARLY = "Government share of total investment, 1925 (percent)"
LATER = "Government share of total investment, 1938 (percent)"
START = "Index at the start of the plan period"
END = "Index at the end of the plan period"


def q7(table, item):
    early = dict(zip(cg.labels(table), cg.col(table, EARLY)))
    later = dict(zip(cg.labels(table), cg.col(table, LATER)))
    fell = [lab for lab in early if later[lab] <= early[lab]]
    assert not fell, f"every share must rise; {fell} did not"
    rise = {lab: later[lab] - early[lab] for lab in early}
    order = sorted(rise, key=rise.get, reverse=True)
    assert rise[order[0]] > rise[order[1]], "the largest rise must be unique"
    assert order[0] == "Country R", f"largest rise belongs to {order[0]}, not Country R"
    assert order[0] != "Country T", "'Country T rose by the most' must be false"
    assert len(set(later.values())) > 1, "'equal shares at the later date' must be false"
    return (f"every later share exceeds its earlier one and the rises are {rise}, "
            f"so the largest belongs to {order[0]}")


def q8(table, item):
    start = dict(zip(cg.labels(table), cg.col(table, START)))
    end = dict(zip(cg.labels(table), cg.col(table, END)))
    assert all(end[k] > start[k] for k in start), f"every category must rise; {start} to {end}"
    growth = {k: end[k] - start[k] for k in start}
    order = sorted(growth, key=growth.get)
    assert growth[order[0]] < growth[order[1]], "the smallest increase must be unique"
    assert order[0] == "Consumer goods for households", \
        f"smallest increase belongs to {order[0]}, not household goods"
    assert order[-1] == "Heavy industry", f"largest increase belongs to {order[-1]}"
    assert growth[order[-1]] > 2 * growth[order[0]], \
        "'by far the least' requires the household increase to be a small fraction of the largest"
    assert len(set(growth.values())) > 1, "'grew by the same amount' must be false"
    return (f"every category ends above its start, the increases are {growth}, and the "
            f"smallest by a wide margin is {order[0]}'s")


TABLE_CHECKS = {7: q7, 8: q8}

CLAIMS = [
 ("began to take a more active role in economic life",
  "KC-6.3.I.B states that following World War I and the onset of the Great Depression, governments began to take a more active role in economic life. That is the change the framework names."),
 ("increase in the economic role governments took, not a decrease",
  "KC-6.3.I.B gives an increase in government activity following the war and the onset of the depression. The anchor carries both halves because the reversed reading is the plausible error."),
 ("often with repressive policies and negative consequences for the population",
  "KC-6.3.I.A.i: the Soviet government controlled the national economy through the Five Year Plans, often implementing repressive policies, with negative repercussions for the population. The repression and the consequences are part of that sentence."),
 ("New Deal, the fascist corporatist economy, and governments with strong popular support",
  "These are the illustrative examples the CED prints beside KC-6.3.I.B under the heading government intervention in the economy. The competing lists are the illustrative examples or developments of topics 7.5, 7.2, 7.3 and 7.8."),
 ("both took a more active role in economic life, and they differed in how far",
  "KC-6.3.I.B states the shared direction and KC-6.3.I.A.i marks the Soviet case as control of the whole national economy, so the comparison this topic's reasoning process asks for is a shared direction with differing extents."),
 ("purpose is to win support, so it cannot be taken as a neutral report",
  "Suggested skill 2.C asks how a source's purpose and audience limit its uses. A pamphlet soliciting electoral support evidences the government's own account of the intervention KC-6.3.I.B describes, not the intervention's results."),
 ("rose by the most percentage points in Country R",
  "KC-6.3.I.B's more active role read out of data rather than recalled. Recomputed in q7 above from the illustrative table alone, including the swapped distractor naming a different country."),
 ("by far the least in goods produced for households",
  "KC-6.3.I.A.i records negative repercussions for the population from control of the national economy through the Five Year Plans; a plan raising industrial output far faster than household supply is what that looks like in data. Recomputed in q8 above from the table alone."),
 ("examples of government intervention in the economy",
  "The CED prints the New Deal and the fascist corporatist economy under that heading beside KC-6.3.I.B. The heading is what the placement asserts, and the framework says nothing here about the contents of either."),
 ("Governments with strong popular support",
  "The CED's illustrative examples for KC-6.3.I.B name governments with strong popular support in Brazil and Mexico as instances of government intervention in the economy. That phrase is the framework's own."),
 ("records negative repercussions for the population",
  "KC-6.3.I.A.i states the direction of the effect on the population without quantifying it, so the framework asserts harm rather than improvement or indifference."),
 ("Often implementing repressive policies",
  "KC-6.3.I.A.i describes the Soviet government as controlling the national economy through the Five Year Plans, often implementing repressive policies. The phrase belongs to the framework's own description of the method."),
 ("governments of very different political character",
  "KC-6.3.I.B states the development generally, and the CED's illustrative examples span the New Deal, the fascist corporatist economy and governments with strong popular support in Brazil and Mexico, so the intervention crosses political types."),
 ("more active role in economic life after the onset of the Great Depression",
  "KC-6.3.I.B places that move after World War I and the onset of the Great Depression, so an argument that the state must employ people when private enterprise cannot is the move stated as a principle."),
 ("weight the source can carry as independent evidence",
  "Suggested skill 2.C asks how point of view and purpose limit a source's uses, and KC-6.3.I.A.i records that Soviet economic control was often carried out through repressive policies, which is the circumstance a state-controlled press reports from."),
 ("system of League of Nations mandates",
  "The illustrative examples for KC-6.3.I.B are the New Deal, the fascist corporatist economy, and governments with strong popular support in Brazil and Mexico. The mandates are printed for KC-6.2.I.B in topic 7.5 under territorial gains and concern colonies, not economic intervention."),
 ("Here it is the crisis governments responded to, and there it is one of the causes of the later war",
  "KC-6.3.I.B places the onset of the Great Depression among the conditions after which governments became more active, and KC-6.2.IV.B.ii names the global economic crisis engendered by the Great Depression among the causes of World War II. The anchor carries both halves because the swap is the plausible error."),
 ("different governments respond to economic crisis after 1900",
  "Unit 7 Learning Objective D asks students to explain how different governments responded to economic crisis after 1900, and the word different is what makes the topic a comparison."),
 ("beginning to take a role more active than the one they had held before",
  "KC-6.3.I.B says governments began to take a more active role, and a beginning marks a departure from what came before, which is what makes the development a change rather than a continuity."),
 ("evidence of how the plan was presented to workers, rather than of how much was produced",
  "Suggested skill 2.C asks what a source's purpose and audience allow it to show, and KC-6.3.I.A.i notes that control of the economy was often accompanied by repressive policies, which is the setting a workplace publication reports from."),
 ("more active economic role governments took after the onset of the depression",
  "KC-6.3.I.B states that governments began to take a more active role in economic life following the war and the onset of the depression; setting prices, directing credit and employing workers are that role in practice."),
 ("controlling the national economy as a whole",
  "KC-6.3.I.A.i describes control of the national economy through the Five Year Plans, while KC-6.3.I.B says only that governments generally became more active. The difference between the two statements is one of extent."),
 ("Comparable records of intervention from states with different political systems",
  "Unit 7 Learning Objective D asks how different governments responded, and the CED's illustrative examples span systems as unlike as the New Deal and the fascist corporatist economy, so an argument about difference needs material from more than one system."),
 ("states a general development and offers particular cases as illustrations",
  "KC-6.3.I.B states the general development and the CED prints three illustrative examples beside it without rating any of them, which is the structure of the framework's treatment."),
 ("evidence of the controls' existence and of one contemporary reaction",
  "Suggested skill 2.C asks students to weigh a source's point of view rather than accept or discard it. The complaint confirms that the more active government role of KC-6.3.I.B was under way and reports a reaction whose author has an interest in the verdict."),
 ("several governments faced the same crisis and the framework records different responses",
  "KC-6.3.I.B states a development common to governments generally, KC-6.3.I.A.i marks out the Soviet case, and the CED prints further illustrative examples; a shared crisis with differing responses is what a comparison is made of."),
 ("totals may rise while household supply does not",
  "KC-6.3.I.A.i states that control of the national economy through the Five Year Plans carried negative repercussions for the population, so rising aggregate output and household shortage are not in contradiction. Suggested skill 2.C asks what each source's situation allows it to show."),
 ("Five Year Plans, made about the Soviet Union",
  "KC-6.3.I.A.i attaches the Five Year Plans and their repercussions to the Soviet Union specifically, while KC-6.3.I.B states the more active role as a general development. The distractors misattach the scope of one statement or the other."),
 ("illustrative cases include programmes of very different kinds",
  "The CED prints the New Deal, the fascist corporatist economy, and governments with strong popular support in Brazil and Mexico as illustrations of KC-6.3.I.B. A shared direction is asserted; a shared programme is not."),
 ("with the Soviet case marked out as control of the whole economy",
  "KC-6.3.I.B gives the general movement towards a more active role and KC-6.3.I.A.i gives the Soviet case as control of the national economy through the Five Year Plans, so an accurate summary has to carry both, which is what the anchor does."),
]

wh_check.run(w7_4, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
