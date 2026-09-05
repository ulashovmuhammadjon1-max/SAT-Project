"""Key audit for AP WORLD HISTORY: MODERN 2.2 (Unit 2, the Mongol Empire).

One (anchor, claim) per question, in module order. The anchor is a distinctive
substring of that question's OWN keyed choice and of no distractor; the claim
states the CED sentence the key rests on, with its Key Concept or Learning
Objective code, so a later reader can check the history rather than take it on
trust.

WHAT THE KEYS REST ON
---------------------
  LO 2.B          the process of state building and decline in Eurasia over time
  LO 2.C          how the expansion of empires influenced trade and
                  communication over time
  LO 2.D          the significance of the Mongol Empire in larger patterns of
                  continuity and change
  skill 5.A       identify PATTERNS AMONG OR CONNECTIONS BETWEEN historical
                  developments and processes
  KC-3.2.I.B.iii  empires collapsed in different regions of the world and IN
                  SOME AREAS were replaced by new imperial states, including the
                  Mongol khanates
  KC-3.1.I.E.i    the expansion of empires -- including the Mongols --
                  facilitated Afro-Eurasian trade and communication as new
                  people were drawn into THEIR CONQUERORS' economies and trade
                  networks
  KC-3.2.II.A.ii  interregional contacts AND CONFLICTS between states and
                  empires, including the Mongols, encouraged significant
                  technological and cultural transfers
  the GOV, ECN and CDI thematic focus paragraphs

WHY THIS TOPIC NEEDED THE MOST RESTRAINT OF ANY SO FAR
-------------------------------------------------------
More is popularly asserted about the Mongols than about any other subject in
this unit, and almost none of it is in the CED. The framework's three sentences
carry three qualifiers and every one of them is load-bearing:

  "in some areas"        -- replacement is NOT claimed everywhere        (q2, q8)
  "their conquerors'"    -- the direction of incorporation is fixed     (q14)
  "contacts and conflicts" -- conquest and exchange are not opposed      (q5)

No key here asserts a casualty figure, a policy of religious toleration, a
postal relay system by name, or the destruction of a named city, because the
CED asserts none of them. The illustrative examples on the page -- Greco-Islamic
medical knowledge moving west, numbering systems moving to Europe, the adoption
of Uyghur script -- are used as instances of KC-3.2.II.A.ii and never as facts a
key turns on, which is what the CED's own note about illustrative examples
requires.

WHERE THE ANCHOR CARRIES TWO CLAUSES, AND WHY
---------------------------------------------
Four distractors here are the SWAP of the key rather than an unrelated claim:

  q14  conquerors and conquered, exchanged as the owners of the networks
  q21  continuity in production / change in the network, exchanged
  q25  which sentence attributes its effect to expansion and which to contact
  q3   the largest MULTIPLE at the busiest route against the thinnest

Those anchors carry both clauses in order, which is the defect verify_e2_1.py
shipped and HISTORY_BRIEF.md records.

DATA QUESTIONS
--------------
Items 3, 6 and 8 carry tables of HYPOTHETICAL figures and each stem says so.
Each keyed conclusion is recomputed below from the table alone AND every
distractor is shown false on the same numbers. The control prints a catch rate
per table; it is never nine of nine, because the label column cannot be
corrupted into a contradiction and because a corruption that leaves the keyed
conclusion TRUE must not be caught -- a checker that complained there would be
testing the numbers rather than the claim. A zero would mean the check had
stopped reading its table.

NEGATIVE CONTROL: `python3 verify_w2_2.py --selftest`.
"""
import sys

import cg_check as cg
import w2_2
import wh_check

BEFORE_M = "Messages recorded before the empire's expansion"
AFTER_M = "Messages recorded after the empire's expansion"
BEFORE_R = "Regions in which it is recorded before the contact"
AFTER_R = "Regions in which it is recorded after the contact"
COLLAPSED = "Imperial states recorded as having collapsed"
ESTABLISHED = "New imperial states recorded as established"


def q3(table, item):
    """Every route rises, and the thinnest route multiplies by the most."""
    before, after = cg.col(table, BEFORE_M), cg.col(table, AFTER_M)
    assert all(a > b for b, a in zip(before, after)), \
        f"every route must carry more after: {before} to {after}"
    ratios = [a / b for b, a in zip(before, after)]
    thinnest = before.index(min(before))
    assert ratios[thinnest] == max(ratios), \
        f"the thinnest route before must have the largest multiple: {ratios}"
    # every distractor false on the same numbers
    assert not all(a < b for b, a in zip(before, after)), "'every route fell' must be false"
    busiest = before.index(max(before))
    assert ratios[busiest] != max(ratios), \
        "'the busiest route before had the largest multiple' must be false"
    assert not any(a == b for b, a in zip(before, after)), "'one route unchanged' must be false"
    assert ratios[thinnest] != min(ratios), \
        "'the thinnest route had the smallest multiple' must be false"
    return (f"before {before} to after {after}: all rise, and the thinnest route "
            f"multiplies by {round(ratios[thinnest], 2)}, the largest of "
            f"{[round(r, 2) for r in ratios]}")


def q6(table, item):
    """All spread further, and the narrowest beforehand is NOT the widest after."""
    before, after = cg.col(table, BEFORE_R), cg.col(table, AFTER_R)
    assert all(a > b for b, a in zip(before, after)), \
        f"every kind must reach more regions after: {before} to {after}"
    narrowest = before.index(min(before))
    assert after[narrowest] != max(after), \
        f"the narrowest beforehand must NOT be the widest after: {before} / {after}"
    # every distractor false on the same numbers
    assert not any(a < b for b, a in zip(before, after)), \
        "'one kind reaches fewer regions after' must be false"
    assert not any(a == b for b, a in zip(before, after)), \
        "'one kind unchanged' must be false"
    widest = before.index(max(before))
    assert after[widest] != max(after), \
        "'the widest beforehand is also the widest after' must be false"
    return (f"before {before} to after {after}: every kind spreads, and the kind starting "
            f"in {min(before)} region(s) ends in {after[narrowest]}, not the maximum "
            f"{max(after)}")


def q8(table, item):
    """A collapse without replacement, and a replacement without collapse."""
    fell, made = cg.col(table, COLLAPSED), cg.col(table, ESTABLISHED)
    lonely_collapse = [i for i in range(len(fell)) if fell[i] > 0 and made[i] == 0]
    lonely_new = [i for i in range(len(fell)) if made[i] > 0 and fell[i] == 0]
    assert lonely_collapse, f"a collapse with no new state must appear: {fell} / {made}"
    assert lonely_new, f"a new state with no collapse must appear: {fell} / {made}"
    # every distractor false on the same numbers
    assert not all(made[i] > 0 for i in range(len(fell)) if fell[i] > 0), \
        "'every collapse is accompanied by a new state' must be false"
    assert any(m > 0 for m in made), "'no new imperial state anywhere' must be false"
    assert not all(f > 0 and m > 0 for f, m in zip(fell, made)), \
        "'every region records both' must be false"
    assert any(f > 0 for f in fell), "'no collapse anywhere' must be false"
    return (f"collapsed {fell} against established {made}: region "
            f"{lonely_collapse[0] + 1} records a collapse alone and region "
            f"{lonely_new[0] + 1} a new state alone")


TABLE_CHECKS = {3: q3, 6: q6, 8: q8}

CLAIMS = [
 ("drawn into the economies and trade networks of those who had conquered them",
  "KC-3.1.I.E.i states that the expansion of empires, including the Mongols, facilitated Afro-Eurasian trade and communication as new people were drawn into their conquerors' economies and trade networks. Expansion comes first and facilitation follows, which is what the option reversing the order gets wrong."),

 ("in SOME areas they were replaced by new imperial states",
  "KC-3.2.I.B.iii states that empires collapsed in different regions of the world and IN SOME AREAS were replaced by new imperial states, including the Mongol khanates. The qualifier is the framework's own, and a claim of replacement everywhere overshoots it."),

 ("the route carrying fewest before multiplied its traffic by the largest factor",
  "Recomputed in q3 above from the table alone, distractors included. KC-3.1.I.E.i states that the expansion of empires facilitated Afro-Eurasian trade and communication, and a rise on every route with the largest multiple where traffic had been thinnest is what facilitation looks like in figures. The anchor carries both clauses because two distractors invert one clause each."),

 ("across territories that had previously been under separate authorities",
  "KC-3.1.I.E.i states that the expansion of empires, including the Mongols, facilitated Afro-Eurasian trade and communication, and the Governance thematic focus states that governments maintain order through a variety of administrative institutions, policies, and procedures. One warrant honoured the length of a route is that facilitation in operation."),

 ("Contacts AND conflicts between states and empires both encouraged",
  "KC-3.2.II.A.ii states that interregional contacts AND CONFLICTS between states and empires, including the Mongols, encouraged significant technological and cultural transfers. Both nouns stand in the sentence, which is what the two options keeping only one of them each halve."),

 ("the kind recorded in fewest regions beforehand is not the kind recorded in most regions afterwards",
  "Recomputed in q6 above from the two columns. KC-3.2.II.A.ii states that interregional contacts and conflicts between states and empires encouraged significant technological and cultural transfers, and knowledge reaching further than before is what such a transfer looks like in a record; the framework orders no race between the kinds transferred. The anchor carries both clauses because the strongest distractor changes only which kind ends up furthest spread. This table replaced one of the same shape as topic 2.3 q7."),

 ("named as an instance of the new imperial states",
  "KC-3.2.I.B.iii states that empires collapsed in different regions of the world and in some areas were replaced by new imperial states, INCLUDING THE MONGOL KHANATES. The word including makes the khanates one case of the pattern the sentence describes rather than the whole of it."),

 ("records a collapse with no new imperial state, and another records a new imperial state with no collapse",
  "Recomputed in q8 above from the two columns. KC-3.2.I.B.iii says empires collapsed in different regions and IN SOME AREAS were replaced by new imperial states, so a pattern in which collapse and replacement do not always accompany each other is exactly what that qualifier allows. The anchor carries both cases because either alone would match a weaker distractor."),

 ("carries forward the arrangements it finds and adds to them",
  "Learning Objective B of this unit asks students to explain the process of state building AND decline in Eurasia over time, KC-3.2.I.B.iii pairs collapse with replacement by new imperial states, and the Governance thematic focus names administrative institutions and procedures as how governments maintain order."),

 ("communities which had not previously traded into the network begin to appear",
  "KC-3.1.I.E.i states that the expansion of empires facilitated Afro-Eurasian trade and communication AS NEW PEOPLE WERE DRAWN INTO their conquerors' economies and trade networks. New participants appearing after incorporation is the mechanism the sentence itself names, which is why it tells against a demand-side explanation."),

 ("a place in larger patterns of continuity and change",
  "Learning Objective D asks students to explain the significance of the Mongol Empire in LARGER PATTERNS of continuity and change, and the empire is named in KC-3.2.I.B.iii among the new imperial states and in KC-3.2.II.A.ii among the parties whose contacts and conflicts encouraged technological and cultural transfers."),

 ("Interregional contact encouraging a technological or cultural transfer",
  "KC-3.2.II.A.ii states that interregional contacts and conflicts between states and empires, including the Mongols, encouraged significant technological and cultural transfers, and the topic's illustrative list names the transfer of Greco-Islamic medical knowledge to western Europe as one such case."),

 ("is also named among the contacts and conflicts that encouraged technological and cultural transfers",
  "KC-3.1.I.E.i names the expansion of empires including the Mongols as facilitating Afro-Eurasian trade and communication, while KC-3.2.II.A.ii names interregional contacts and conflicts between states and empires including the Mongols as encouraging significant technological and cultural transfers. Suggested skill 5.A asks for exactly such connections between processes."),

 ("entered networks belonging to those who had conquered them, rather than the conquerors entering theirs",
  "KC-3.1.I.E.i states that the expansion of empires facilitated Afro-Eurasian trade and communication as new people were drawn into THEIR CONQUERORS' economies and trade networks. The possessive fixes the direction, and the anchor carries both parties in order because the strongest distractor exchanges them."),

 ("records collapse in different regions and replacement by new imperial states in some areas at once",
  "KC-3.2.I.B.iii states that empires collapsed in different regions of the world and in some areas were replaced by new imperial states, including the Mongol khanates, and Learning Objective B asks for the process of state building AND decline in Eurasia over time. One sentence carries both halves."),

 ("being drawn into a wider network of exchange than the one it had belonged to before",
  "KC-3.1.I.E.i states that the expansion of empires facilitated Afro-Eurasian trade and communication as new people were drawn into their conquerors' economies and trade networks, and the Economics thematic focus says societies affect and are affected by the ways they produce, exchange, and consume goods and services."),

 ("the only new imperial states established anywhere in the period",
  "KC-3.2.I.B.iii names the Mongol khanates with the word INCLUDING, which presents them as an instance rather than as the whole class of new imperial states. The four rejected options restate KC-3.2.I.B.iii, KC-3.1.I.E.i and KC-3.2.II.A.ii as they stand."),

 ("The first creates the contact within which the second becomes possible",
  "KC-3.2.II.A.ii states that interregional contacts and conflicts between states and empires encouraged significant technological and cultural transfers, and KC-3.1.I.E.i records imperial expansion facilitating communication. Suggested skill 5.A asks for the connection between two processes, and here it runs from contact to transfer rather than the other way."),

 ("a practice belonging to one people comes into use among another",
  "KC-3.2.II.A.ii states that interregional contacts and conflicts between states and empires, including the Mongols, encouraged significant technological and cultural transfers, and the adoption of Uyghur script is the topic page's own illustrative instance. The Cultural Developments thematic focus supplies the wider point that interactions of societies carry political and cultural implications."),

 ("a pattern of imperial collapse and replacement that was older than the empire itself",
  "Learning Objective D asks students to explain the significance of the Mongol Empire in larger patterns of continuity and change, and KC-3.2.I.B.iii places the khanates among new imperial states replacing collapsed empires, a pattern the sentence describes as occurring in different regions of the world."),

 ("Continuity in what a district produced together with change in the network and the authority through which it moved",
  "KC-3.1.I.E.i states that the expansion of empires facilitated Afro-Eurasian trade and communication as new people were drawn into their conquerors' economies and trade networks, and Learning Objective D asks for the empire's place in larger patterns of CONTINUITY AND CHANGE. The anchor carries both halves in order because the strongest distractor exchanges them."),

 ("entering a trade network for the first time in the years following their incorporation",
  "KC-3.1.I.E.i states that the expansion of empires facilitated Afro-Eurasian trade and communication AS NEW PEOPLE WERE DRAWN INTO their conquerors' economies and trade networks. New entrants are the framework's own mechanism, so evidence of them bears directly on a claim that expansion made no difference."),

 ("without stating which party in any exchange gained more by it",
  "KC-3.2.II.A.ii states that interregional contacts and conflicts between states and empires, including the Mongols, encouraged significant technological AND CULTURAL transfers. It names no direction, no magnitude and no beneficiary, so a claim about who gained more would go beyond the sentence."),

 ("regions that had had little occasion to send word to one another before",
  "KC-3.1.I.E.i states that the expansion of empires, including the Mongols, facilitated Afro-Eurasian trade AND COMMUNICATION. Envoys able to travel a long road under a single authority are the communication half of that sentence rather than the trade half."),

 ("The first attributes the facilitation to the expansion of empires, and the second attributes the encouragement to the contacts and conflicts",
  "KC-3.1.I.E.i names the expansion of empires as what facilitated Afro-Eurasian trade and communication, while KC-3.2.II.A.ii names interregional contacts and conflicts between states and empires as what encouraged technological and cultural transfers. The anchor carries both attributions in order because the strongest distractor exchanges them."),

 ("developments may continue after the period in which they are studied",
  "The CED states that events, processes, and developments are not constrained by the given dates and may begin before, or continue after, the period, and KC-3.1.I.E.i asserts that imperial expansion facilitated Afro-Eurasian trade and communication. The first of those sentences is what licenses a claim reaching past the period's end."),

 ("their appearance in trade networks that had not previously reached them",
  "KC-3.1.I.E.i states that the expansion of empires facilitated Afro-Eurasian trade and communication as new people were drawn into their conquerors' economies and trade networks, which is a consequence the framework itself asserts. Suggested skill 5.A asks for connections between developments, and each rejected pairing joins a development to a circumstance that would have held anyway."),

 ("their consequence was not confined to the encounter that produced them",
  "KC-3.2.II.A.ii states that interregional contacts and conflicts between states and empires encouraged SIGNIFICANT technological and cultural transfers, and the topic's illustrative list gives instances in which a body of knowledge or a script came into use in a region other than its own. The framework makes no comparison with other periods."),

 ("lowered the cost of moving and dealing across its territory",
  "KC-3.1.I.E.i states that the expansion of empires facilitated Afro-Eurasian trade and communication, and the Governance thematic focus states that governments maintain order through a variety of administrative institutions, policies, and procedures and exercise power in different ways and for different purposes."),

 ("by the contacts and conflicts that followed encourage techniques and practices to move between regions",
  "KC-3.2.I.B.iii supplies collapse and replacement by new imperial states including the Mongol khanates, KC-3.1.I.E.i the drawing of new peoples into their conquerors' economies and trade networks, and KC-3.2.II.A.ii the transfers encouraged by interregional contacts and conflicts. The key states all three and each rejected option contradicts at least one."),
]

wh_check.run(w2_2, CLAIMS, TABLE_CHECKS, sys.argv)
