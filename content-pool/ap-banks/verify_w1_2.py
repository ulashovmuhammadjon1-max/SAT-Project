"""Key audit for AP WORLD HISTORY: MODERN 1.2 (Unit 1, Dar al-Islam c. 1200 to c. 1450).

One (anchor, claim) per question, in module order. The anchor is a distinctive
substring of that question's own keyed choice and of no distractor; the claim
names the CED sentence the key rests on.

WHAT THE KEYS REST ON
---------------------
  KC-3.2.I         as the Abbasid Caliphate fragmented, new Islamic political
                   entities emerged, MOST of which were dominated by Turkic
                   peoples; these states demonstrated continuity, innovation,
                   and diversity
  KC-3.1.III.A     Muslim rule continued to expand due to military expansion,
                   and Islam SUBSEQUENTLY expanded through the activities of
                   merchants, missionaries, and Sufis
  KC-3.1.III.D.iii Islam, Judaism, Christianity and their core beliefs and
                   practices continued to shape societies in Africa and Asia
  KC-3.2.II.A.i    Muslim states and empires encouraged significant intellectual
                   innovations and transfers
  LO 1.D / 1.E / 1.F  the three learning objectives printed on this topic's pages
  the CDI, GOV and TEC thematic-focus paragraphs

THE TWO PLACES THE ANCHOR HAD TO CARRY BOTH CLAUSES
---------------------------------------------------
q2 and q24 turn on the ORDER inside KC-3.1.III.A: rule expanded by military
means, and the faith spread afterwards through merchants, missionaries and
Sufis. Each has a distractor that keeps both processes and reverses their
relation -- right about the history, wrong about the sequence, which is the
hardest distractor in this subject to catch. An anchor naming only one process
would sit inside that reversal, so both anchors carry the relation itself
("successive rather than rival", "distinct processes working on different
timescales"). This is the defect recorded against `verify_e2_1.py`.

q16 is the quantifier item. KC-3.2.I says MOST of the new entities were
dominated by Turkic peoples, and the whole question is the difference between
"most" and "all", so the anchor is "without being universal" rather than
anything naming Turkic peoples, which every choice does.

DATA QUESTIONS
--------------
Items 11, 12 and 13 carry HYPOTHETICAL tables, labelled as such in the stem: a
real inventory or arrival count for this period is not something the CED
prints, and a key resting on a remembered figure could not be checked. Each
keyed conclusion is recomputed below from its table alone, and each distractor
is shown false against the same numbers.

NEGATIVE CONTROL: `python3 verify_w1_2.py --selftest`.
"""
import sys

import cg_check as cg
import w1_2
import wh_check

EARLIER = "Works in an earlier inventory"
LATER = "Works in a later inventory"
M_EARLY = "Merchants recorded in an earlier year"
M_LATE = "Merchants recorded in a later year"
YEARS = "Years of rule recorded in one chronicle"
SHARE = "Officials of Turkic military background, per hundred named"


def q11(table, item):
    early, late = cg.col(table, EARLIER), cg.col(table, LATER)
    assert all(b > a for a, b in zip(early, late)), f"every field must rise: {early} {late}"
    for field in ("Mathematics", "Medicine"):
        e, l = cg.cell(table, field, EARLIER), cg.cell(table, field, LATER)
        assert l > 2 * e, f"{field} must more than double: {e} to {l}"
    pe, pl = cg.cell(table, "Poetry", EARLIER), cg.cell(table, "Poetry", LATER)
    assert pl < 2 * pe, f"poetry must not double: {pe} to {pl}"
    assert pl > pe, "'poetry fell' must be false"
    biggest_early = cg.ranked(table, EARLIER)[0]
    mult = {lab: cg.cell(table, lab, LATER) / cg.cell(table, lab, EARLIER)
            for lab in cg.labels(table)}
    assert mult[biggest_early] != max(mult.values()), \
        "'the largest earlier holding grew by the largest multiple' must be false"
    assert not (cg.cell(table, "Medicine", EARLIER) > cg.cell(table, "Mathematics", EARLIER)
                and cg.cell(table, "Medicine", LATER) > cg.cell(table, "Mathematics", LATER)), \
        "'medicine larger than mathematics at both' must be false"
    return (f"holdings rise in all three fields; multiples recompute to {mult}, so only "
            f"mathematics and medicine pass two and poetry does not")


def q12(table, item):
    early, late = cg.col(table, M_EARLY), cg.col(table, M_LATE)
    assert all(b > a for a, b in zip(early, late)), f"both routes must rise: {early} {late}"
    sea_e, sea_l = cg.cell(table, "Sea route", M_EARLY), cg.cell(table, "Sea route", M_LATE)
    ov_e, ov_l = cg.cell(table, "Overland route", M_EARLY), cg.cell(table, "Overland route", M_LATE)
    assert sea_l == 3 * sea_e, f"the sea route must triple: {sea_e} to {sea_l}"
    assert ov_l == 1.25 * ov_e, f"the overland route must rise by a quarter: {ov_e} to {ov_l}"
    assert ov_l < sea_l, "'overland carried more in the later year' must be false"
    assert sea_l / sea_e != ov_l / ov_e, "'both grew by the same multiple' must be false"
    assert not (sea_e > ov_e), "'the sea route was higher in both years' must be false"
    return (f"sea {sea_e} to {sea_l} is exactly threefold and overland {ov_e} to {ov_l} is "
            f"exactly a quarter more; the sea route starts below the overland route")


def q13(table, item):
    shares = cg.col(table, SHARE)
    assert all(s > 50 for s in shares), f"every share must be a majority: {shares}"
    assert len(set(shares)) == len(shares), f"the shares must differ from one another: {shares}"
    assert not any(s < 50 for s in shares), "'a minority in at least one state' must be false"
    longest = cg.ranked(table, YEARS)[0]
    assert cg.cell(table, longest, SHARE) != max(shares), \
        "'the longest recorded rule had the largest share' must be false"
    pairs = sorted(zip(cg.col(table, YEARS), shares))
    assert not all(b[1] > a[1] for a, b in zip(pairs, pairs[1:])), \
        "'share rises with recorded length of rule' must be false"
    return (f"the three shares {shares} are each above fifty per hundred and all differ, and "
            f"they do not rise with the recorded years of rule")


TABLE_CHECKS = {11: q11, 12: q12, 13: q13}

CLAIMS = [
 ("holding real authority under a caliph who retained the older titles",
  "KC-3.2.I states that as the Abbasid Caliphate fragmented, new Islamic political entities emerged. A caliph named in prayer and on coin while another power holds the revenue, the appointments and the army is that fragmentation described from inside; the CED asserts none of the four alternatives."),
 ("successive rather than rival",
  "KC-3.1.III.A states that Muslim rule continued to expand due to military expansion and that Islam SUBSEQUENTLY expanded through the activities of merchants, missionaries, and Sufis. The anchor carries the relation, not one process, because the strongest distractor reverses the order and keeps both."),
 ("shared inheritance and local difference are both part of their description",
  "KC-3.2.I says the new Islamic political entities demonstrated continuity, innovation, and diversity. Diversity sits in the same sentence as continuity, so each uniformity option contradicts the framework rather than merely oversimplifying it."),
 ("together with the core beliefs and practices of each",
  "KC-3.1.III.D.iii names Islam, Judaism, and Christianity together and says the core beliefs and practices of these religions continued to shape societies in Africa and Asia. Three traditions are named, which is what the single-tradition option denies."),
 ("effect of state support",
  "KC-3.2.II.A.i states that Muslim states and empires encouraged significant intellectual innovations and transfers, and Learning Objective F asks for the effects of intellectual innovation in Dar al-Islam. Endowment, salaries and a library are that encouragement made concrete."),
 ("preserved, interpreted and carried into new settings",
  "KC-3.2.II.A.i pairs innovations WITH transfers, and this topic's illustrative list names preservation and commentaries on Greek moral and natural philosophy as a transfer. A commentary is interpretation, so the copying-only option misdescribes the same activity."),
 ("sustained contact",
  "KC-3.2.II.A.i credits Muslim states and empires with encouraging significant intellectual innovations and transfers, and the topic's illustrative list names scholarly and cultural transfers in Muslim and Christian Spain. Proximity between communities is the condition that example points to."),
 ("of the kind Muslim states and empires are said to have encouraged",
  "KC-3.2.II.A.i is the sentence that groups them: Muslim states and empires encouraged significant intellectual innovations and transfers. The illustrative list files advances in mathematics, literature and medicine under that heading and not under trade, war or administration."),
 ("teaching and personal devotion carried by travelers",
  "KC-3.1.III.A names merchants, missionaries, and Sufis as the activities through which Islam subsequently expanded, and distinguishes them in the same sentence from the military expansion of Muslim rule. Devotion carried by travelers is the second half of that sentence."),
 ("added innovations of their own",
  "KC-3.2.I credits the entities emerging from the Abbasid fragmentation with continuity, innovation, and diversity, and KC-3.2.II.A.i credits Muslim states with encouraging intellectual innovations and transfers. A smaller territory or more rulers describes the division itself, not its cultural consequence."),
 ("mathematics and medicine each more than doubled while poetry did not",
  "Recomputed in q11 above from the table alone, distractors included. KC-3.2.II.A.i is the process such a pattern would illustrate; the data is labelled hypothetical because the CED prints no inventory and a key must not rest on a remembered figure."),
 ("the sea route tripled while the overland route grew by a quarter",
  "Recomputed in q12 above from the table alone. KC-3.1.III.A names merchants among the agents by which Islam expanded after the expansion of Muslim rule, which is why movement along routes is evidence for this topic."),
 ("the share differed from state to state",
  "Recomputed in q13 above: each share is above fifty per hundred and no two are equal. KC-3.2.I says the new entities were MOST of them dominated by Turkic peoples and demonstrated diversity, so predominance with variation is the shape the framework describes."),
 ("across many regions and generations",
  "Suggested skill 1.A for this topic asks students to identify and describe a historical concept, development, or process, and KC-3.1.III.A describes the expansion of Islam as an extended development. Each rejected option is a single datable act."),
 ("themselves demonstrated continuity, innovation and diversity",
  "KC-3.2.I puts the fragmentation of the Abbasid Caliphate and the emergence of new entities in one sentence and then credits those entities with continuity, innovation, and diversity. The decline of one state is therefore not the decline of its political world."),
 ("without being universal",
  "KC-3.2.I says MOST of which were dominated by Turkic peoples. The quantifier is the whole question: it asserts a prevailing pattern and stops short of a universal claim, and the CED's approximate dates rule out the threshold-year option."),
 ("places that no army had brought under Muslim rule",
  "KC-3.1.III.A separates the expansion of Muslim RULE by military means from the subsequent expansion of ISLAM through merchants, missionaries and Sufis. A trading community observing its faith beyond any Muslim state is the second process without the first."),
 ("rather than as either static or wholly new",
  "KC-3.2.I.A applies the phrase continuity, innovation, and diversity to states of Afro-Eurasia and the Americas including the Song, and KC-3.2.I applies the same phrase to the new Islamic entities. The examination system is asserted of the Song alone."),
 ("endowed institutions of learning and paid the scholars",
  "KC-3.2.II.A.i asserts that Muslim states and empires encouraged intellectual innovations and transfers, which is a claim about what was done and can be checked against evidence. The four rejected questions ask what was right, better or deserved."),
 ("supported innovation and the transfer of learning from elsewhere",
  "KC-3.2.II.A.i names Muslim states and empires as the agent that encouraged significant intellectual innovations and transfers, and Learning Objective F asks for the effects of that innovation. Each alternative denies the support the framework credits."),
 ("not only the conduct of individuals within them",
  "KC-3.1.III.D.iii says these religions continued to SHAPE SOCIETIES in Africa and Asia, and the Cultural Developments thematic focus says beliefs often carry political, social and cultural implications. The society, not the individual, is the unit of that sentence."),
 ("adopting arrangements their predecessors had not used",
  "KC-3.2.I lists continuity, innovation, and diversity together rather than in alternation, so the new entities are all three at once. Each rejected option keeps one term of the three and drops the others."),
 ("both intended and unintended consequences",
  "The Technology and Innovation thematic focus states that technological advances have shaped human development and interactions with both intended and unintended consequences, and KC-3.2.II.A.i places significant innovation inside this period rather than after it."),
 ("distinct processes working on different timescales",
  "KC-3.1.III.A separates military expansion of Muslim rule from the subsequent expansion of Islam through merchants, missionaries and Sufis. The anchor carries the relation because one distractor is the same pair of processes with the order reversed."),
 ("rather than bystanders to it",
  "KC-3.2.II.A.i states that Muslim states and empires ENCOURAGED significant intellectual innovations and transfers. Encouragement of production as well as of transfer is what the sentence asserts, and the collection-only option keeps only half of it."),
 ("new Islamic political entities that emerged as the Abbasid Caliphate fragmented",
  "KC-3.2.I describes exactly that emergence, and this topic's illustrative list names the Seljuk Empire, the Mamluk sultanate of Egypt and the Delhi sultanates as instances of the category. Maritime empires belong to a later unit of the course."),
 ("alongside the transfers received from elsewhere",
  "KC-3.2.II.A.i names innovations AND transfers as two things Muslim states encouraged, and the illustrative list separates advances in mathematics, literature and medicine from the transfers printed beside them. Every rejected option is itself an instance of transfer."),
 ("since the given dates are approximate",
  "The CED states that events, processes, and developments are not constrained by the given dates and may begin before, or continue after, the period. KC-3.1.III.D.iii's word CONTINUED, used of three religions, is an instance of a process older than the period."),
 ("followed by the emergence of new political entities",
  "Learning Objective E asks for the causes and effects of the rise of Islamic states, and KC-3.2.I supplies the pair in one clause: as the Abbasid Caliphate fragmented, new Islamic political entities emerged. The rejected pairing reverses that order."),
 ("occurred together, since states that emerged from a fragmenting caliphate",
  "KC-3.2.I, KC-3.2.II.A.i and KC-3.1.III.D.iii assert respectively that new entities emerged from fragmentation, that Muslim states encouraged intellectual innovation and transfers, and that three religions continued to shape societies in Africa and Asia, all in the same period."),
]

wh_check.run(w1_2, CLAIMS, TABLE_CHECKS, sys.argv)
