"""Key audit for AP WORLD HISTORY: MODERN 5.5 Technology of the Industrial Age.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim cites the Key Concept or Learning
Objective the key traces to.

WHAT THE KEYS REST ON
---------------------
Three statements, and every key traces to one of them:

  KC-5.1.I.B  the development of machines, INCLUDING steam engines and the
              internal combustion engine, made it possible to take advantage of
              both existing and vast newly discovered resources of energy stored
              in fossil fuels, SPECIFICALLY coal and oil; the fossil fuels
              revolution greatly increased the energy available to human
              societies.
  KC-5.1.I.E  the second industrial revolution led to new methods in the
              production of steel, chemicals, electricity, and precision
              machinery during the second half of the 19th century.
  KC-5.1.IV   railroads, steamships, and the telegraph made exploration,
              development, and communication possible in interior regions
              globally, WHICH LED TO increased trade and migration.

THE ONE DATE
------------
Item 5 keys "the second half of the 19th century" because KC-5.1.I.E prints
those words. No other item turns on a date: the CED states that its periods are
approximate and may begin before or continue after the years given, and
HISTORY_BRIEF.md forbids keying a boundary the framework itself loosens.

WHAT THEY DELIBERATELY DO NOT REST ON
-------------------------------------
The framework names no inventor, no country of origin for any machine and no
date for the telegraph, the railroad or the steamship, so nothing here asserts
one -- item 29 keys that silence directly, by making the invented inventor the
claim that goes beyond the CED. The consequences of these technologies for
empire and for migration patterns belong to KC-5.2 and KC-5.4, which are unit 6.

SWAP ANCHORS
------------
Items 11, 19, 22 and 24 carry a distractor that is the key reversed: the
machines and the fuels exchanged as cause and effect, the technologies and the
traffic exchanged, the contents of the two industrial phases exchanged, and the
order of the second industrial revolution and the fossil fuel machines
exchanged. Each of those anchors carries BOTH clauses, which is the defect found
in verify_e2_1.py. The key-rotation control below requires all thirty keys to
fail when moved one place.

FIVE choices per item (A-E); see HISTORY_BRIEF.md.
"""
import sys

import cg_check as cg
import wh_check as wh
import w5_5

COAL = "Coal consumed (millions of tons)"
ENERGY = "Energy available per person (index)"
SECOND = "second industrial revolution"


def q9(table, item):
    """Both columns rise at every step; no mixed or flat reading survives."""
    labels = cg.labels(table)
    assert labels == ["First decade", "Second decade", "Third decade", "Fourth decade"], \
        f"the four rows must be the four decades in order; got {labels}"
    coal = cg.col(table, COAL)
    energy = cg.col(table, ENERGY)
    for series, name in ((coal, "coal consumed"), (energy, "energy available per person")):
        assert all(b > a for a, b in zip(series, series[1:])), \
            f"the {name} column must rise at every step; got {series}"
    assert not (coal[-1] < coal[0]), "'coal consumption falls' must be false"
    assert not (energy[-1] < energy[0]), "'energy available falls' must be false"
    assert len(set(coal)) > 1 and len(set(energy)) > 1, "'neither figure changes' must be false"
    assert energy[-1] > 2 * energy[0], \
        "the energy index must more than double, so 'greatly increased' is visible in the table"
    return (f"recomputed from the table: coal {coal} and energy per person {energy} each rise at "
            f"every step, with the energy index more than doubling across the four decades")


def q10(table, item):
    """Four rows are the framework's second-revolution methods; one is not."""
    where = {str(row[0]): str(row[1]) for row in table["rows"]}
    second = {name for name, place in where.items() if SECOND in place.lower()}
    assert second == {"Steel", "Chemicals", "Electricity", "Precision machinery"}, (
        f"the second industrial revolution rows must be exactly the framework's four; got {second}"
    )
    outside = [name for name in where if name not in second]
    assert outside == ["The steam engine"], (
        f"exactly one row must sit outside that list, and it must be the steam engine; got {outside}"
    )
    assert "fossil fuel" in where["The steam engine"].lower(), \
        "the steam engine row must place it among the machines that made fossil fuel energy usable"
    return ("read from the table alone: four rows carry the second industrial revolution and the "
            "steam engine row carries the fossil fuel machines instead")


CLAIMS = [
 ("internal combustion engine",
  "KC-5.1.I.B names them explicitly: the development of machines, including steam engines and the internal combustion engine, made it possible to take advantage of energy stored in fossil fuels. The rejected pairs name machines the framework does not print in that statement."),
 ("Coal and oil",
  "KC-5.1.I.B says resources of energy stored in fossil fuels, SPECIFICALLY coal and oil. The adverb is the framework's own, which is why this pair is keyed and no other fuel on the list is."),
 ("greatly increased the energy available to human societies",
  "KC-5.1.I.B closes with that sentence verbatim: the fossil fuels revolution greatly increased the energy available to human societies. Two distractors reverse the verb, so the anchor carries the direction as well as the object."),
 ("chemicals, electricity, and precision machinery",
  "KC-5.1.I.E names exactly four: steel, chemicals, electricity, and precision machinery. The rejected sets are drawn from KC-5.1.I.A, KC-5.1.IV and KC-5.1.III.B."),
 ("second half of the 19th century",
  "KC-5.1.I.E prints the timing itself: during the second half of the 19th century. This is one of the few dates the framework fixes in this unit, which is what makes it keyable at all."),
 ("steamships, and the telegraph",
  "KC-5.1.IV groups the three: railroads, steamships, and the telegraph made exploration, development, and communication possible in interior regions globally. The rejected sets come from KC-5.1.I.E, KC-5.1.I.B and KC-5.1.III.B."),
 ("Exploration, development, and communication",
  "KC-5.1.IV states what the three made possible in interior regions globally. The rejected options name developments the framework attaches to KC-5.3.I.C, KC-5.1.V.A, KC-5.3.II.iii and KC-5.1.V.B."),
 ("Increased trade and migration",
  "KC-5.1.IV closes with the consequence: which led to increased trade and migration. The framework puts the three technologies first and the increase second, and every rejected option reverses or contradicts that outcome."),
 ("Coal consumption and the energy available per person both rise",
  "KC-5.1.I.B states that the fossil fuels revolution greatly increased the energy available to human societies, and q9 above recomputes both columns rising at every step, with the energy index more than doubling. The anchor carries both columns because two distractors reverse one of them."),
 ("steam engine",
  "KC-5.1.I.E lists steel, chemicals, electricity and precision machinery as the second industrial revolution's new methods, while KC-5.1.I.B names the steam engine among the machines that made fossil fuel energy usable. q10 above checks the table records that division."),
 ("development of machines made it possible to take advantage of the energy stored in fossil fuels",
  "KC-5.1.I.B runs in one direction: the development of machines MADE IT POSSIBLE to take advantage of resources of energy stored in fossil fuels. The reasoning process for this topic is causation, and the anchor carries both clauses because a distractor exchanges them."),
 ("already known deposits and newly found ones were both brought into use",
  "KC-5.1.I.B says BOTH existing AND vast newly discovered resources of energy stored in fossil fuels. Covering deposits of both kinds is what makes the increase the same statement then describes so large."),
 ("new machines and new methods changed the way goods were produced over time",
  "Unit 5 Learning Objective F asks students to explain how technology shaped economic production over time. The rejected questions belong to the objectives behind KC-5.3.I.C, KC-5.3.II.ii, KC-5.3.I.A and KC-5.1.VI.C."),
 ("machines made it possible to take advantage of energy stored in fossil fuels",
  "KC-5.1.I.B describes machines making it possible to take advantage of energy stored in fossil fuels, specifically coal and oil. An engine burning coal in place of a water wheel is that substitution; the rejected options are framework statements about other developments."),
 ("new methods in chemical production",
  "KC-5.1.I.E names chemicals among the four kinds of production in which the second industrial revolution led to new methods. The rejected options are KC-5.1.I.B, KC-5.1.IV, KC-5.1.I.C and KC-5.1.III.B, none of which covers chemical manufacture."),
 ("new methods in the production of electricity",
  "KC-5.1.I.E names electricity among the four kinds of production transformed by the second industrial revolution during the second half of the 19th century. No other framework statement in this unit mentions generating stations or lighting."),
 ("Precision machinery",
  "KC-5.1.I.E names precision machinery as one of the four. Steam power is named in KC-5.1.I.B instead, among the machines that made fossil fuel energy usable, which is the distinction the item turns on."),
 ("opened interior regions and led to increased trade and migration",
  "KC-5.1.IV joins both halves in one sentence: railroads, steamships, and the telegraph made exploration, development, and communication possible in interior regions globally, which led to increased trade and migration."),
 ("The railroads, steamships and telegraph came first and led to increased trade and migration",
  "KC-5.1.IV puts the three technologies first and the traffic second. The anchor is the whole two-clause sentence because the distractor exchanges the halves, and this topic's reasoning process is causation."),
 ("greatly increased the energy available to human societies, which powered production",
  "KC-5.1.I.B supplies the increase in available energy and Unit 5 Learning Objective F supplies the question about economic production. More available energy is what connects the technology to the output."),
 ("steamships helped open interior regions and increase trade and migration",
  "KC-5.1.IV names steamships alongside railroads and the telegraph. KC-5.1.I.E's four new methods are steel, chemicals, electricity and precision machinery, so a steamship belongs to the first statement and not the second."),
 ("The first turned on steam power and coal, the second on steel, chemicals, electricity and precision machinery",
  "KC-5.1.II.B names steam-powered industrial production during the first Industrial Revolution, and KC-5.1.I.E names the second industrial revolution's four methods. The anchor carries both phases because a distractor exchanges their contents."),
 ("Steel",
  "KC-5.1.I.E names steel first among the four kinds of production in which the second industrial revolution brought new methods. Internal combustion belongs to KC-5.1.I.B's machines rather than to that list."),
 ("second half of the 19th century, after the machines",
  "KC-5.1.I.E places the second industrial revolution during the second half of the 19th century, while KC-5.1.I.B's machines belong to the industrial growth this unit opens with. The anchor carries both the date and the order because a distractor reverses them."),
 ("the telegraph made communication possible in interior regions globally",
  "KC-5.1.IV names the telegraph among the three developments that made exploration, development, and communication possible in interior regions globally. Speed of message rather than movement of goods or people is the telegraph's part of that sentence."),
 ("how goods were made in the district before and after the technology arrived",
  "Unit 5 Learning Objective F asks how technology shaped economic production over time, and KC-5.1.I.B and KC-5.1.I.E both describe technologies changing how things were made. A before and after record of production is what bears on that claim."),
 ("grouped with railroads and steamships as opening interior regions",
  "KC-5.1.IV groups railroads, steamships, and the telegraph together. KC-5.1.I.E's four methods are steel, chemicals, electricity and precision machinery, and KC-5.1.I.B's machines are the steam and internal combustion engines, so the telegraph is in neither."),
 ("opening of interior regions led to increased trade",
  "KC-5.1.IV states that these technologies made exploration, development, and communication possible in interior regions globally, which led to increased trade and migration. Cargo arriving from newly named inland towns is that consequence in a port's own records."),
 ("single named inventor",
  "KC-5.1.I.B, KC-5.1.I.E and KC-5.1.IV state the other four claims and name no inventor anywhere among them. Attributing the fossil fuels revolution to one person supplies a fact the CED does not print, which HISTORY_BRIEF.md forbids."),
 ("unlocked fossil fuel energy, later methods transformed further industries",
  "The summary joins KC-5.1.I.B's machines and fossil fuels, KC-5.1.I.E's second industrial revolution and KC-5.1.IV's railroads, steamships and telegraph. Each rejected option contradicts one of those three statements."),
]

TABLE_CHECKS = {9: q9, 10: q10}

wh.run(w5_5, CLAIMS, TABLE_CHECKS, sys.argv)
