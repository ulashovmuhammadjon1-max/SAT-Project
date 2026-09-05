"""Key audit for AP WORLD HISTORY: MODERN 7.5 Unresolved Tensions After World War I.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor; ``claim``
states what the key rests on, for a human to audit. The gate is
``wh_check.run``, shared by the World History banks.

WHAT THE KEYS REST ON
---------------------
KC-6.2.I.B is the whole of this topic's required content: "Between the two
world wars, Western and Japanese imperial states predominantly maintained
control over colonial holdings; in some cases, they gained additional
territories through conquest or treaty settlement and in other cases faced
anti-imperial resistance."

  control predominantly maintained   items 1, 7, 10, 19, 20, 25, 29, 30
  gain by conquest OR treaty         items 2, 3, 14, 15, 22, 27, 30
  anti-imperial resistance faced     items 5, 8, 11, 13, 18, 21, 24, 26, 30
  Western AND Japanese states        items 6, 17

Items 1, 10 and 19 turn on the DIRECTION of the first clause and item 7 on the
difference between two counts and one, so those anchors carry both halves; the
swapped reading is the plausible error in each.

The CED's illustrative examples carry items 3, 4, 5, 13, 15, 17 and 27:
territorial gains are illustrated by the transfer of former German colonies to
Great Britain and France under the system of League of Nations mandates and by
Manchukuo and the Greater East Asia Co-Prosperity Sphere; anti-imperial
resistance by the Indian National Congress and by West African resistance
(strikes and congresses) to French rule. Nothing is asserted about what any of
them contained beyond the heading it is printed under.

Items 9, 16, 21 and 28 rest on suggested skill 2.C, the significance of a
source's point of view, purpose, historical situation and audience, including
how these limit its uses. Item 12 rests on this topic's reasoning process,
continuity and change, and item 23 on Unit 7 Learning Objective E.

WHAT IS NOT KEYED, deliberately: no date, treaty article, territory's area,
leader's name, or outcome of any resistance movement. KC-6.2.I.B records that
resistance was faced and does not say here that it succeeded; decolonisation is
unit 8's material and belongs to another author.

DATA ITEMS: 7 and 8 carry tables of explicitly illustrative data, recomputed
below from the table alone, with each distractor falsified against the same
numbers.

NEGATIVE CONTROLS: ``python3 verify_w7_5.py --selftest`` rotates every key,
breaks every anchor, corrupts every cell of both tables, injects each banned
notation and figure-language form, strips the citation from a ``why`` and a
``claim``, and duplicates a choice; each must raise for its own reason, and
positive controls run alongside.
"""
import sys

import cg_check as cg
import wh_check
import w7_5

START = "Colonial territories administered at the start of the interwar period"
END = "Colonial territories administered at the end of the interwar period"
FIRST = "Recorded strikes and congresses against colonial rule, first decade"
SECOND = "Recorded strikes and congresses against colonial rule, second decade"


def q7(table, item):
    start = dict(zip(cg.labels(table), cg.col(table, START)))
    end = dict(zip(cg.labels(table), cg.col(table, END)))
    lost = [k for k in start if end[k] < start[k]]
    assert not lost, f"no state may hold fewer territories at the end; {lost} do"
    same = sorted(k for k in start if end[k] == start[k])
    gained = sorted(k for k in start if end[k] > start[k])
    assert len(same) == 2 and len(gained) == 1, \
        f"the key requires two unchanged and one gaining; got same={same}, gained={gained}"
    assert len(gained) != 2, "'two gained and one unchanged' must be false"
    assert len(set(end.values())) > 1, "'all three equal at the end' must be false"
    return (f"no later count falls below its earlier one; {same} are unchanged and "
            f"{gained} gains, so control is predominantly maintained with one addition")


def q8(table, item):
    first = dict(zip(cg.labels(table), cg.col(table, FIRST)))
    second = dict(zip(cg.labels(table), cg.col(table, SECOND)))
    assert all(second[k] > first[k] for k in first), f"every territory must rise; {first} to {second}"
    assert min(list(first.values()) + list(second.values())) > 0, \
        "'only one territory records any activity' must be false"
    rise = {k: second[k] - first[k] for k in first}
    order = sorted(rise, key=rise.get, reverse=True)
    assert rise[order[0]] > rise[order[1]], "the largest increase must be unique"
    assert order[0] == "Territory K", f"largest increase belongs to {order[0]}, not Territory K"
    assert order[0] != "Territory J", "'Territory J shows the largest increase' must be false"
    top_first = max(first, key=first.get)
    assert rise[top_first] == max(rise.values()), \
        "'the highest first-decade count shows the smallest increase' must be false"
    return (f"every second-decade count exceeds its first-decade count, the increases are "
            f"{rise}, and the largest belongs to {order[0]}")


TABLE_CHECKS = {7: q7, 8: q8}

CLAIMS = [
 ("predominantly maintained control over them",
  "KC-6.2.I.B states that between the two world wars, Western and Japanese imperial states predominantly maintained control over colonial holdings. Maintenance of control is the continuity the sentence opens with."),
 ("Through conquest or through treaty settlement",
  "KC-6.2.I.B states that in some cases imperial states gained additional territories through conquest or treaty settlement, so both routes are named and an answer offering only one is incomplete."),
 ("territorial gain made through a treaty settlement",
  "The CED prints the mandate transfers under territorial gains beside KC-6.2.I.B, and that sentence names conquest and treaty settlement as the two routes. A transfer arranged under the postwar settlement is the second."),
 ("Territorial gains",
  "The illustrative examples the CED prints beside KC-6.2.I.B are divided into territorial gains and anti-imperial resistance, and Manchukuo and the Greater East Asia Co-Prosperity Sphere appear under the first heading."),
 ("Indian National Congress, and West African strikes and congresses",
  "The CED prints the Indian National Congress and West African resistance, in the form of strikes and congresses, to French rule as its examples of the anti-imperial resistance KC-6.2.I.B says imperial states faced."),
 ("Western and Japanese imperial states",
  "KC-6.2.I.B names Western and Japanese imperial states together as the holders of colonial holdings between the two world wars, so restricting the sentence to either alone drops half of it."),
 ("two ended with the same number, and one gained",
  "KC-6.2.I.B pairs control predominantly maintained with additional territories gained in some cases. Recomputed in q7 above from the illustrative table alone, including the swapped distractor that reverses the two counts."),
 ("largest increase is in Territory K",
  "KC-6.2.I.B states that imperial states in other cases faced anti-imperial resistance, and this item asks a student to read that out of data. Recomputed in q8 above from the illustrative table alone, including each false distractor."),
 ("reason to present the year as untroubled",
  "Suggested skill 2.C asks how point of view and purpose limit a source's uses, and KC-6.2.I.B records anti-imperial resistance among what imperial states faced -- which an administration reporting on its own year has least reason to record."),
 ("predominantly kept their colonial holdings, and in some cases added to them",
  "KC-6.2.I.B states that these states predominantly maintained control and in some cases gained additional territories. The anchor carries both halves because the reversed reading is the plausible error."),
 ("anti-imperial resistance that imperial states faced in some of their holdings",
  "KC-6.2.I.B records anti-imperial resistance in some cases, illustrated by the Indian National Congress. An organised refusal of cooperation aimed at self-government is resistance of that kind."),
 ("holdings kept and, alongside that, territories gained and resistance encountered",
  "KC-6.2.I.B pairs a continuity with two changes in one sentence, which is why this topic's reasoning process is continuity and change."),
 ("West African strikes and congresses",
  "The CED prints West African resistance in the form of strikes and congresses to French rule among its examples of the anti-imperial resistance named in KC-6.2.I.B, so a strike joining wage demands to a demand about who governs falls under that heading."),
 ("records treaty settlement alongside conquest",
  "KC-6.2.I.B names conquest or treaty settlement as the routes to additional territory, and the CED's mandate example is a gain of the second kind, so an account resting on force alone omits half the sentence."),
 ("territory passed from one imperial power to others",
  "KC-6.2.I.B counts additional territories gained through treaty settlement among the period's changes, and the CED's example is the transfer of former German colonies to Great Britain and France under the mandate system. What changes is which power administers the territory."),
 ("addressed to people who fund and vote on colonial policy",
  "Suggested skill 2.C names audience among the things that shape a source's significance, and KC-6.2.I.B records resistance that an address to metropolitan supporters has reason to omit."),
 ("named alongside Western states as an imperial power",
  "KC-6.2.I.B names Western and Japanese imperial states together as maintaining control over colonial holdings, and the CED prints Manchukuo and the Greater East Asia Co-Prosperity Sphere among the territorial gains."),
 ("Records of strikes, congresses and other organised protest",
  "KC-6.2.I.B states that imperial states in some cases faced anti-imperial resistance, which the CED illustrates with congresses and strikes, so records of organised protest bear on contested control directly."),
 ("predominantly maintained between the wars, while over the century empires gave way to new states",
  "KC-6.2.I.B covers the interwar years and KC-6.2.I the century as a whole. The two describe different stretches of the same century, and the anchor carries both so the reading that collapses them cannot match."),
 ("allows for exceptions rather than asserting that control was maintained everywhere",
  "KC-6.2.I.B says control was PREDOMINANTLY maintained, and the same sentence names cases of gain and cases of resistance, so the qualifier states a general pattern while leaving room for the exceptions it goes on to give."),
 ("may understate resistance that the framework records",
  "KC-6.2.I.B records anti-imperial resistance faced in some cases, and suggested skill 2.C asks what a source's point of view does to its report. A paper published where colonial policy is made is positioned to minimise protest rather than to measure it."),
 ("additional territory gained through treaty settlement",
  "KC-6.2.I.B names conquest or treaty settlement as the two routes to additional territory, and a transfer arranged by the victors in a postwar agreement is the second rather than the first."),
 ("stayed the same and what changed in territorial holdings",
  "Unit 7 Learning Objective E asks students to explain the continuities and changes in territorial holdings from 1900 to the present."),
 ("faced in some cases rather than in every case",
  "KC-6.2.I.B says imperial states in OTHER cases faced anti-imperial resistance, which places resistance in some holdings rather than making it a uniform condition, and the framework supplies no rule linking protest to how a territory was acquired."),
 ("imperial control continued while resistance to it was being organised",
  "KC-6.2.I.B has control predominantly maintained at the same time as anti-imperial resistance is faced, which is a tension the period leaves standing."),
 ("political demands of an organised anti-imperial movement",
  "KC-6.2.I.B records anti-imperial resistance, illustrated by congresses as well as strikes. A petition states the movement's demands rather than the government's intentions or any figure about the territory."),
 ("Territorial gain, illustrated by the transfer of former German colonies",
  "The CED prints the mandate transfers and Manchukuo under territorial gains and the Indian National Congress and West African strikes and congresses under anti-imperial resistance, the two headings KC-6.2.I.B supplies. The anchor carries the heading and the example together."),
 ("evidence of the movement's claims and activity",
  "Suggested skill 2.C asks students to weigh purpose rather than accept or discard a source, and KC-6.2.I.B records that imperial states faced anti-imperial resistance, which such a document evidences even where its support claims cannot be measured."),
 ("gave up control of their colonial holdings during these years",
  "KC-6.2.I.B states that these states predominantly maintained control between the two world wars, so a general surrender contradicts the sentence while the other four options restate its three parts."),
 ("Control mostly held, some territories added by conquest or treaty",
  "KC-6.2.I.B combines a continuity with two changes: predominantly maintained control, additional territories gained in some cases through conquest or treaty settlement, and anti-imperial resistance faced in others. A summary has to carry all three."),
]

wh_check.run(w7_5, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
