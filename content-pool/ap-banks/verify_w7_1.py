"""Key audit for AP WORLD HISTORY: MODERN 7.1 Shifting Power After 1900.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The gate itself is shared, not reinvented: ``wh_check.run`` is the World
History gate, which layers the CED-citation rule and the figure-language rule
on top of ``cg_check.check`` (thirty questions, five distinct choices, a key
pinned to its anchor, no choice contained in another, no option named by
letter, no two stems opening alike, every table question recomputed from its
own table) and ``es_check.style`` (World History is a prose subject and
``export_units.py`` does not typeset it, so a backslash, a bare caret, a
digit-slash-digit fraction or a digit-hyphen-digit span would reach a student
as literal characters -- which is why HISTORY_BRIEF.md requires "1900 to 1945"
rather than a hyphen).

WHAT THE KEYS REST ON
---------------------
Items 1, 6, 10, 15, 16, 17, 21 and 27 rest on KC-6.2.I.A: the older, land-based
Ottoman, Russian, and Qing empires collapsed due to a COMBINATION of internal
and external factors. Items 2, 19, 28 and 29 rest on the same sentence for the
identity of the three empires, for its restriction of communist revolution to
the Russian case, and for the description "older, land-based".

Items 3, 9, 11, 12, 18, 22, 25 and 26 rest on KC-6.2.I: the West dominated the
global political order at the beginning of the 20th century, but BOTH
land-based and maritime empires gave way to new states by the century's end.
The order of those two clauses is the content of items 3 and 18, so their
anchors carry both.

Items 4, 8, 13, 14, 20, 23 and 24 rest on KC-6.2.II.D: states around the world
challenged the existing political and social order, including the Mexican
Revolution that arose as a result of political crisis.

Items 5 and 28 rest on the direction of KC-6.2.I.A's final clause -- the
changes in Russia led EVENTUALLY to communist revolution, so the revolution
follows the collapse and does not cause it. The anchors carry both clauses
because the swapped distractor is the plausible error.

Item 30 rests on Unit 7 Learning Objective A, and item 8 on suggested skill 4.B.

WHAT IS NOT KEYED, deliberately: no year, no decade, no ordering of the three
collapses against one another, and no cause of the Mexican Revolution beyond
the framework's own words "political crisis". The CED states that events are
not constrained by the dates given for a period, so a key resting on a boundary
it loosens would not be checkable.

DATA ITEMS: 7 and 14 carry tables of explicitly illustrative data. Each keyed
conclusion is recomputed below from that table alone.

NEGATIVE CONTROLS: ``python3 verify_w7_1.py --selftest`` rotates every key in
turn, breaks every anchor in turn, corrupts every cell of both tables, injects
each banned notation form and each figure-language form, strips the citation
from a ``why`` and from a ``claim``, and duplicates a choice -- and requires
each to raise FOR ITS OWN REASON, since a control that fires for the wrong
reason proves nothing about the guard it names. It also runs positive controls,
so a gate that rejected everything would fail rather than look thorough.
"""
import sys

import cg_check as cg
import wh_check
import w7_1

EXT = "Share of state revenue owed to foreign creditors (percent)"
INT = "Provinces reporting failed tax collection"
EARLY = "Recorded strikes and uprisings, first decade"
LATE = "Recorded strikes and uprisings, third decade"


def q7(table, item):
    by_ext = cg.ranked(table, EXT)
    by_int = cg.ranked(table, INT)
    ext_vals = sorted(cg.col(table, EXT), reverse=True)
    int_vals = sorted(cg.col(table, INT), reverse=True)
    assert ext_vals[0] > ext_vals[1], "the largest external-pressure value must be unique"
    assert int_vals[0] > int_vals[1], "the largest internal-breakdown value must be unique"
    assert by_ext[0] == "Empire X", f"greatest external pressure is {by_ext[0]}, not Empire X"
    assert by_int[0] == "Empire Z", f"most widespread internal breakdown is {by_int[0]}, not Empire Z"
    assert by_ext[0] != by_int[0], "the two maxima must fall on different empires"
    assert "Empire Y" not in (by_ext[0], by_int[0]), "'Empire Y greatest of both' must be false"
    assert by_ext != by_int, "'the two rise together' must be false: the orderings must differ"
    assert min(cg.col(table, INT)) > 0, "'no internal difficulty at all' must be false"
    return (f"ranking by external pressure gives {by_ext} and by failed tax collection {by_int}; "
            "the two maxima are different empires and every distractor is false on these numbers")


def q14(table, item):
    early = dict(zip(cg.labels(table), cg.col(table, EARLY)))
    late = dict(zip(cg.labels(table), cg.col(table, LATE)))
    assert min(list(early.values()) + list(late.values())) > 0, \
        "'only one region records any challenges' must be false"
    order = cg.ranked(table, LATE)
    late_vals = sorted(late.values(), reverse=True)
    assert late_vals[0] > late_vals[1], "the largest later total must be unique"
    assert order[0] == "Region I", f"largest later total belongs to {order[0]}, not Region I"
    fell = [lab for lab in early if late[lab] < early[lab]]
    assert fell == ["Region III"], f"the only decline must be Region III; got {fell}"
    assert len(fell) < len(early), "'every region falls' must be false"
    assert fell, "'no region falls' must be false"
    return (f"every cell is above zero, the largest later total is {order[0]}'s, "
            f"and exactly one region declines, namely {fell[0]}")


TABLE_CHECKS = {7: q7, 14: q14}

CLAIMS = [
 ("combination of internal and external factors",
  "KC-6.2.I.A attributes the collapse of the older land-based empires to a combination of internal and external factors. Failed provincial tax collection is internal and foreign control of borrowing terms is external, so the pamphlet supplies one of each and neither alone."),
 ("Russian, and Qing",
  "KC-6.2.I.A names the older, land-based empires that collapsed as the Ottoman, Russian, and Qing. The distractors substitute maritime empires, which KC-6.2.I treats as the other kind."),
 ("gave way by the century's end to new states formed",
  "KC-6.2.I: the West dominated the global political order at the beginning of the 20th century, but both land-based and maritime empires gave way to new states by the century's end. The anchor carries both clauses in order, because the reversed reading is the plausible error."),
 ("political crisis inside the state producing a challenge",
  "KC-6.2.II.D states that the Mexican Revolution arose as a result of political crisis and groups it with states around the world challenging the existing political and social order. A demand for a new government together with a demand about landholding touches both orders."),
 ("collapse came first, and the framework describes it as leading eventually to communist revolution",
  "KC-6.2.I.A's final clause: these changes in Russia EVENTUALLY led to communist revolution. The revolution follows the collapse and does not produce it, so the anchor carries both clauses to exclude the swapped distractor."),
 ("pairs external factors with internal ones",
  "KC-6.2.I.A gives a combination of internal and external factors. Defeat by a foreign power is external, so a single-cause account of that kind omits the internal half of the framework's explanation."),
 ("Empire X is under the greatest external financial pressure and Empire Z",
  "KC-6.2.I.A pairs internal with external factors, and this item asks a student to tell one from the other in data rather than to recall a case. Recomputed in q7 above from the illustrative table alone: the two maxima fall on different empires, and the swapped distractor is excluded because the anchor names both empires in their roles."),
 ("several regions were challenging the existing political and social order",
  "Suggested skill 4.B asks how a specific development is situated within a broader context, and KC-6.2.II.D supplies that context by placing challenges to the existing order in states around the world."),
 ("replacement of both land-based and maritime empires by new states",
  "KC-6.2.I names this as the century's change. The alternatives describe conditions the framework does not present as beginning or ending within the period."),
 ("external dependence and an internal administrative weakness",
  "KC-6.2.I.A's pairing applied to a source: buying weapons abroad on credit is a dependence on outside states, and appointing ministers for loyalty rather than competence is a weakness of the empire's own administration."),
 ("new states were formed where the empires",
  "KC-6.2.I states that both kinds of empire gave way to new states by the century's end, which is a replacement of imperial government by new states rather than any of the alternative outcomes."),
 ("both land-based and maritime empires as giving way to new states",
  "KC-6.2.I applies the same outcome to both kinds of empire, so a comparison across the two is available and neither kind can be described as surviving intact."),
 ("political crisis within the state",
  "KC-6.2.II.D locates the origin of the Mexican Revolution in political crisis. An account beginning with an invasion replaces the stated cause with one the framework does not give."),
 ("later decade is Region I",
  "KC-6.2.II.D places challenges to the existing political and social order in states around the world, which is the pattern this item asks a student to read out of data. Recomputed in q14 above from the illustrative table alone: no cell is zero, the largest later total is unique, and exactly one region's total falls, so the four distractors are each false on these numbers."),
 ("reason to leave the empire's internal administration out",
  "A minister belonged to the administration whose failures KC-6.2.I.A counts among the internal factors, so an account naming only external causes is the account his position would favour. That is a limit on the source's use, which is what suggested skill 2.C asks students to explain."),
 ("broken down before foreign pressure increased",
  "A cause cannot follow its effect. If the internal breakdown KC-6.2.I.A names is already under way before external pressure rises, the internal side has the earlier claim on the outcome; the other findings leave the sequence untouched."),
 ("functioned normally until foreign creditors imposed new terms",
  "The same sequencing rule read the other way. Three of the alternatives are themselves evidence of the internal weakness KC-6.2.I.A names and would strengthen rather than weaken the claim."),
 ("West dominated the global political order at the beginning",
  "KC-6.2.I opens with exactly this condition, and the rest of the statement describes movement away from it, so it is the starting point a unit on shifting power states first."),
 ("Russia",
  "KC-6.2.I.A links the eventual communist revolution to the changes in Russia specifically, and to none of the other cases named in this topic."),
 ("formation of new states out of territory that empires had governed",
  "KC-6.2.I describes empires giving way to new states. A congress declaring that former imperial provinces will govern themselves is that process rather than an expansion, a continuation or a transfer between empires."),
 ("combination of the two rather than by either kind alone",
  "KC-6.2.I.A says the collapses were due to a combination of internal and external factors. The sentence neither ranks the two kinds nor excludes either, so promoting one to decisive asserts more than the framework does."),
 ("process spread across the century rather than a single event",
  "KC-6.2.I says empires gave way to new states by the century's end, a span rather than a date, and the CED states that developments are not constrained by the dates given for a period."),
 ("challenges to an existing order that begin with a crisis inside the state",
  "KC-6.2.II.D attributes the Mexican Revolution to political crisis, and KC-6.2.I.A counts internal factors among the causes of imperial collapse. The shared element is a crisis inside the state rather than an external agent."),
 ("social order as well as the political order",
  "KC-6.2.II.D pairs the political and the social order as the things challenged. A revolutionary government redistributing land acts on the arrangement of society as well as on who governs."),
 ("consistent with Western predominance at the beginning of the century",
  "KC-6.2.I begins from Western domination of the global political order at the beginning of the 20th century, so a source reporting that domination reports the framework's starting condition."),
 ("Maritime empires survived the century intact",
  "KC-6.2.I says BOTH land-based and maritime empires gave way to new states. Exempting maritime empires contradicts the word both, while the other four statements restate KC-6.2.I, KC-6.2.I.A and KC-6.2.II.D."),
 ("Provincial administrative records of tax collection",
  "KC-6.2.I.A distinguishes internal from external factors. Records of how the empire taxed and staffed its own provinces document the empire's own machinery, whereas loans, treaties, ambassadors and foreign tariffs document its relations with others."),
 ("links communist revolution to only one of the collapsed land-based empires",
  "KC-6.2.I.A attaches the eventual communist revolution to the Russian case after naming three collapsed empires, so generalising the outcome to every collapse asserts more than the sentence does."),
 ("older and land-based rather than maritime",
  "KC-6.2.I.A calls them the older, land-based Ottoman, Russian, and Qing empires, and KC-6.2.I sets land-based empires beside maritime ones. The anchor carries both halves because the reversed description is the plausible error."),
 ("internal and which external factors contributed to change",
  "Unit 7 Learning Objective A asks students to explain how internal and external factors contributed to change in various states after 1900, so an inquiry framed in those two categories restates the objective."),
]


wh_check.run(w7_1, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
