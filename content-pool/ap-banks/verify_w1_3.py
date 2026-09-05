"""Key audit for AP WORLD HISTORY: MODERN 1.3 (South and Southeast Asia, c. 1200 to c. 1450).

One (anchor, claim) per question, in module order. The anchor is a distinctive
substring of that question's own keyed choice and of no distractor; the claim
names the CED sentence the key rests on.

WHAT THE KEYS REST ON
---------------------
  KC-3.1.III.D.iv  Hinduism, Islam, and Buddhism, and their core beliefs and
                   practices, CONTINUED to shape societies in South and
                   Southeast Asia
  KC-3.2.I.B.i     state formation and development demonstrated continuity,
                   innovation, and diversity, INCLUDING the new Hindu and
                   Buddhist states that emerged in these regions
  LO 1.G           how the belief systems and practices of these regions
                   affected society over time
  LO 1.H           how and why states of these regions developed and maintained
                   power over time
  suggested skill 3.A, and the CDI and GOV thematic-focus paragraphs

WHY SO MANY ITEMS ARE SOURCE ITEMS
----------------------------------
The suggested skill on this topic's CED page is 3.A, identify and describe a
claim and or argument in a source, so a third of the bank gives a source and
asks what it claims. Every such source is written for the item and explicitly
unattributed. Its key is recoverable from the words printed in the stem, and
the framework statement supplies the content the item sits in -- which is the
only honest way to write a source item when no real text may be quoted and no
invented one may be signed with a real name.

THE SWAP ITEM
-------------
q28 offers continuity in legitimacy with innovation in administration, and its
strongest distractor is the same two terms exchanged. An anchor naming one term
would sit inside the swap, so the anchor carries both clauses in order. This is
the defect `HISTORY_BRIEF.md` records against `verify_e2_1.py`.

DATA QUESTIONS
--------------
Items 11, 12 and 13 carry HYPOTHETICAL tables, labelled as such in the stem
because the CED prints no such counts and a key must never rest on a remembered
figure. Each keyed conclusion is recomputed below from its own table, and every
distractor is shown false against the same numbers.

NEGATIVE CONTROL: `python3 verify_w1_3.py --selftest`.
"""
import sys

import cg_check as cg
import w1_3
import wh_check

G_EARLY = "Land grants recorded in an earlier reign"
G_LATE = "Land grants recorded in a later reign"
SHIPS = "Ships recorded in one season"
LANGS = "Languages recorded among resident traders"
H_EARLY = "Monastic communities in an earlier survey"
H_LATE = "Monastic communities in a later survey"


def q11(table, item):
    early, late = cg.col(table, G_EARLY), cg.col(table, G_LATE)
    rose = [i for i, (a, b) in enumerate(zip(early, late)) if b > a]
    same = [i for i, (a, b) in enumerate(zip(early, late)) if b == a]
    fell = [i for i, (a, b) in enumerate(zip(early, late)) if b < a]
    assert len(early) == 3 and len(rose) == 2 and len(same) == 1 and not fell, \
        f"key requires two rising, one unchanged, none falling: {rose} {same} {fell}"
    mult = {lab: cg.cell(table, lab, G_LATE) / cg.cell(table, lab, G_EARLY)
            for lab in cg.labels(table)}
    biggest = cg.ranked(table, G_EARLY)[0]
    assert mult[biggest] != max(mult.values()), \
        "'the largest earlier total grew by the largest multiple' must be false"
    return (f"grants {early} to {late}: two sites rise, one is unchanged, none falls, and "
            f"the multiples {mult} do not peak at the largest earlier total")


def q12(table, item):
    by_ships = cg.ranked(table, SHIPS)
    by_langs = cg.ranked(table, LANGS)
    assert by_ships[0] == by_langs[0], f"the top port must agree: {by_ships} {by_langs}"
    assert by_ships != by_langs, f"the two orders must differ below the top: {by_ships} {by_langs}"
    fewest_ships = by_ships[-1]
    assert cg.cell(table, fewest_ships, LANGS) != min(cg.col(table, LANGS)), \
        "'the port with fewest ships also had fewest languages' must be false"
    assert not all(v > 5 for v in cg.col(table, LANGS)), \
        "'every port recorded more than five languages' must be false"
    assert len(set(cg.col(table, LANGS))) > 1, "'the same number of languages everywhere' is false"
    return (f"by ships the order is {by_ships} and by languages {by_langs}: the same port "
            f"leads both and the lower two exchange places")


def q13(table, item):
    early, late = cg.col(table, H_EARLY), cg.col(table, H_LATE)
    rose = [i for i, (a, b) in enumerate(zip(early, late)) if b > a]
    fell = [i for i, (a, b) in enumerate(zip(early, late)) if b < a]
    same = [i for i, (a, b) in enumerate(zip(early, late)) if b == a]
    assert len(rose) == 1 and len(fell) == 1 and len(same) == 1, \
        f"key requires one of each direction: rose {rose}, fell {fell}, same {same}"
    biggest = cg.ranked(table, H_EARLY)[0]
    drop = {lab: cg.cell(table, lab, H_EARLY) - cg.cell(table, lab, H_LATE)
            for lab in cg.labels(table)}
    assert drop[biggest] != max(drop.values()), \
        "'the largest earlier count showed the largest decline' must be false"
    return (f"communities {early} to {late}: one district rises, one falls and one is "
            f"unchanged, and the declines {drop} do not peak at the largest earlier count")


TABLE_CHECKS = {11: q11, 12: q12, 13: q13}

CLAIMS = [
 ("rank at birth or scholarly training",
  "Suggested skill 3.A asks students to identify the claim a source makes, and this source states its claim in its own words. KC-3.1.III.D.iv supplies the context, that Hinduism and its core beliefs and practices continued to shape these societies; the Bhakti movement is the topic's illustrative example."),
 ("together with the core beliefs and practices of each",
  "KC-3.1.III.D.iv names Hinduism, Islam, and Buddhism together and says their core beliefs and practices continued to shape societies in South and Southeast Asia. Three named traditions defeat the single-tradition option and the word continued defeats the first-arrival option."),
 ("including new Hindu and Buddhist states that emerged in these regions",
  "KC-3.2.I.B.i states that state formation and development demonstrated continuity, innovation, and diversity, including the new Hindu and Buddhist states that emerged in South and Southeast Asia. All three terms are asserted in one sentence."),
 ("a ruler who honors the gods is upheld by them",
  "Suggested skill 3.A asks students to identify a claim in a source and so to separate it from what the source reports. Learning Objective H is the content: how states developed and maintained power, of which a justification of rule is a part."),
 ("carry out social functions",
  "Learning Objective G asks how the belief systems AND PRACTICES of these regions affected society over time, and KC-3.1.III.D.iv names practices beside core beliefs. Buddhist monasticism is the topic's own illustrative practice."),
 ("outside formal institutions as well as through them",
  "KC-3.1.III.D.iv says the core beliefs and practices of these traditions continued to shape these societies, and the topic's illustrative list names the Bhakti movement and Sufism, both practices rather than organs of a state."),
 ("more than one religious character emerged there",
  "KC-3.2.I.B.i asserts diversity in state formation in these regions and in the same clause names new HINDU AND BUDDHIST states. Two religious characters inside one claim of diversity is the sentence's own structure."),
 ("rather than remaining confined to particular communities",
  "KC-3.1.III.D.iv says these traditions continued to SHAPE SOCIETIES in South and Southeast Asia. A tradition that shapes a society is not one that has remained foreign to it, which is what the claim under test asserts."),
 ("converted into religious patronage and armed followers",
  "Learning Objective H asks how states of these regions developed and MAINTAINED power over time, and the Governance thematic focus states that governments obtain, retain, and exercise power in different ways and for different purposes."),
 ("inherited practice, new arrangements and regional difference",
  "KC-3.2.I.B.i uses the phrase of South and Southeast Asian state formation, KC-3.2.I.A of states in Afro-Eurasia and the Americas, and KC-3.2.I of the new Islamic entities. A shared description of a pattern is not a claim that the cases are alike in detail."),
 ("patronage did not move in one direction everywhere",
  "Recomputed in q11 above from the table alone, distractors included. Learning Objective G concerns how belief systems affected society, and KC-3.2.I.B.i's word diversity is what uneven patronage across sites illustrates."),
 ("gives different orders",
  "Recomputed in q12 above: the two rankings agree at the top and disagree below it. KC-3.1.III.D.iv concerns societies shaped by more than one tradition, and a port where traders of several languages reside is where such contact happens."),
 ("rose in one district, fell in another and was unchanged in the third",
  "Recomputed in q13 above from the two survey columns. KC-3.2.I.B.i's word diversity and Learning Objective G's phrase over time both point at variation between places rather than at one uniform trend."),
 ("three temples stand on the city's main street",
  "Suggested skill 3.A requires separating what a source reports from what it argues; a count of buildings is observable and the remaining statements apply a standard of value. KC-3.1.III.D.iv is the content context for temples in such a city."),
 ("rulers dealt with the several traditions among their subjects",
  "KC-3.1.III.D.iv names three traditions shaping the societies of these regions in the same period, and the Cultural Developments thematic focus states that the interactions of societies and their beliefs often have political implications."),
 ("which presupposes that they were already present",
  "KC-3.1.III.D.iv uses the word CONTINUED of Hinduism, Islam, and Buddhism in these regions, and the CED separately states that developments are not constrained by the given dates and may begin before the period."),
 ("that its predecessors had not employed",
  "KC-3.2.I.B.i joins innovation to continuity in one sentence about state formation in these regions, so evidence of an arrangement the predecessors lacked is evidence of the innovation half. Every rejected option evidences continuity only."),
 ("displayed and renewed their subordination",
  "Learning Objective H asks how states of these regions developed and maintained power over time, and the Governance thematic focus states that governments maintain order through a variety of administrative institutions, policies, and procedures."),
 ("through a variety of practices rather than through one uniform observance",
  "KC-3.1.III.D.iv names the core beliefs and PRACTICES of these traditions as what continued to shape these societies, and the topic's illustrative list prints three different practices under one heading."),
 ("cultivators who are driven away take the kingdom's strength with them",
  "Suggested skill 3.A asks students to identify the argument a source makes; this source states a claim and supplies a reason and an example for it. Learning Objective H supplies the content, how states developed and maintained power."),
 ("made grants of land to religious institutions",
  "KC-3.2.I.B.i and KC-3.1.III.D.iv assert matters of fact about state formation and about traditions shaping societies, and evidence can settle whether a grant was made. The rejected questions ask what should have been done, what is better, what is fair and what is deserved."),
 ("while the region's religious traditions continued to shape its societies",
  "KC-3.2.I.B.i records new Hindu and Buddhist states emerging in these regions and KC-3.1.III.D.iv records their traditions continuing to shape the societies, in the same period. Political change and cultural continuity are asserted together."),
 ("all continued to shape the societies of South and Southeast Asia",
  "KC-3.1.III.D.iv names Hinduism, Islam, and Buddhism together as continuing to shape societies in South and Southeast Asia. Three buildings of three traditions in one town is that sentence in miniature, and nothing in it implies a merger."),
 ("what the source offers in support of it",
  "Suggested skill 3.A for this topic is to identify and describe a claim and or argument in a source, and the next skill in the same sequence is to identify the evidence a source uses to support an argument. Learning Objective H is the content practiced on."),
 ("supported the ruler's standing among his subjects",
  "Learning Objective H asks how states developed and maintained power, KC-3.2.I.B.i names the new Hindu and Buddhist states of these regions, and the Cultural Developments thematic focus states that beliefs often carry political implications."),
 ("an organized body with procedures of its own",
  "Learning Objective G asks how belief systems and their practices affected society over time; KC-3.1.III.D.iv names practices beside core beliefs, and Buddhist monasticism is the topic's own illustrative practice."),
 ("arising within the region",
  "KC-3.2.I.B.i says state formation and development demonstrated continuity, innovation, and diversity, INCLUDING the new Hindu and Buddhist states that EMERGED in South and Southeast Asia. Emergence joined to continuity is the framework's own wording."),
 ("continuity in the claim to legitimacy joined to innovation in the machinery",
  "KC-3.2.I.B.i asserts continuity and innovation together in state formation in these regions. The anchor names both halves in order because the strongest distractor is the same two terms exchanged, the shape this subject makes easiest to miss."),
 ("affect people beyond its own adherents",
  "KC-3.1.III.D.iv says the core beliefs and PRACTICES of these traditions continued to shape societies, and Learning Objective G asks how belief systems and their practices affected society. Shaping a society is a wider claim than counting believers."),
 ("went on shaping the societies those states governed",
  "KC-3.2.I.B.i records new Hindu and Buddhist states emerging in these regions and KC-3.1.III.D.iv records Hinduism, Islam and Buddhism continuing to shape their societies. The two sentences describe the same regions in the same period."),
]

wh_check.run(w1_3, CLAIMS, TABLE_CHECKS, sys.argv)
