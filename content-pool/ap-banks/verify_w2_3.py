"""Key audit for AP WORLD HISTORY: MODERN 2.3 (Unit 2, the Indian Ocean).

One (anchor, claim) per question, in module order. The anchor is a distinctive
substring of that question's OWN keyed choice and of no distractor; the claim
states the CED sentence the key rests on, with its Key Concept or Learning
Objective code.

WHAT THE KEYS REST ON
---------------------
  LO 2.E / 2.F / 2.G  the causes of the growth of networks of exchange after
                  1200, its effects, and the role of environmental factors
  skill 5.A       identify PATTERNS AMONG OR CONNECTIONS BETWEEN developments
  KC-3.1.I.A.ii   improved TRANSPORTATION TECHNOLOGIES and commercial practices
                  led to an increased volume of trade and expanded the
                  geographical range of existing trade routes, including the
                  Indian Ocean, promoting the growth of powerful new trading
                  cities
  KC-3.1.I.C.ii   innovations in PREVIOUSLY EXISTING transportation and
                  commercial technologies, including the compass, the astrolabe
                  and larger ship designs
  KC-3.1.I.A.iii  the Indian Ocean trading network FOSTERED THE GROWTH OF STATES
  KC-3.1.III.B    merchants set up diasporic communities where they introduced
                  their own traditions into the indigenous cultures AND, IN
                  TURN, indigenous cultures influenced merchant cultures
  KC-3.2.II.A.iii interregional contacts and conflicts encouraged significant
                  technological and cultural transfers, including during Chinese
                  maritime activity led by Ming Admiral Zheng He
  KC-3.1.II.A.i   the expansion and intensification of long-distance trade
                  routes often DEPENDED ON environmental knowledge, including
                  advanced knowledge of the monsoon winds
  the ECN, CDI and ENV thematic focus paragraphs

HOW THIS MODULE WAS KEPT OFF 2.1's GROUND
-------------------------------------------
KC-3.1.I.A.ii is very nearly KC-3.1.I.A.i, which topic 2.1 rests on, and
writing both modules from the shared sentence would have produced two
interchangeable banks. Only q2 and q19 touch it, and q2 is built on the one
real difference: the Indian Ocean sentence names improved TRANSPORTATION
TECHNOLOGIES beside the commercial practices the Silk Roads sentence names
alone. The weight of the module is on the three things 2.1 does not have -- the
network fostering the growth of states, the two-way influence of diasporic
communities, and the dependence on environmental knowledge.

WHERE THE ANCHOR CARRIES TWO CLAUSES, AND WHY
---------------------------------------------
KC-3.1.III.B is a two-directional sentence and KC-3.1.I.A.iii fixes a
direction, so the swapped distractor is the natural one here and it appears
five times:

  q5   network fostering state, against state fostering network
  q6   merchants influencing hosts / hosts influencing merchants, exchanged
  q16  settled community against passing party, the descriptions exchanged
  q17  the direction in which practices moved, reversed
  q25  the environment shaping societies / societies shaping environments

Those anchors carry both clauses in order, which is the defect verify_e2_1.py
shipped and HISTORY_BRIEF.md records.

ONE KEY DELIBERATELY SAYS "CONSISTENT WITH" AND NOT "SHOWS"
------------------------------------------------------------
q9's table ranks three settlements alike by shipping and by offices. That is
consistent with KC-3.1.I.A.iii's claim that the network fostered the growth of
states, and it is not evidence of the direction, which a ranking cannot supply.
The keyed choice says so in its own words rather than leaving a student to
infer causation from a correlation.

DATA QUESTIONS
--------------
Items 4, 7 and 9 carry tables of HYPOTHETICAL figures and each stem says so.
Each keyed conclusion is recomputed below from the table alone AND every
distractor is shown false on the same numbers. The control's per-table catch
rate is never nine of nine: the label column cannot be corrupted into a
contradiction, and a corruption leaving the keyed conclusion TRUE must not be
caught. A zero would mean the check had stopped reading its table.

NEGATIVE CONTROL: `python3 verify_w2_3.py --selftest`.
"""
import sys

import cg_check as cg
import w2_3
import wh_check

WIND_A = "Departures recorded in the season of one wind"
WIND_B = "Departures recorded in the season of the opposing wind"
BROUGHT = "Practices recorded as introduced by resident merchants"
TAKEN = "Practices recorded as taken up by resident merchants from the host society"
SHIPS = "Ships calling in a year"
OFFICES = "Offices recorded in its administration"


def q4(table, item):
    """Both seasons everywhere, and neither far above half at any port."""
    a, b = cg.col(table, WIND_A), cg.col(table, WIND_B)
    assert all(x > 0 for x in a) and all(y > 0 for y in b), \
        f"every port must sail in both seasons: {a} and {b}"
    shares = [x / (x + y) for x, y in zip(a, b)]
    assert all(0.45 < s < 0.55 for s in shares), \
        f"neither season may account for much more than half anywhere: {shares}"
    # every distractor false on the same numbers
    assert not any(y == 0 for y in b), "'one season only' must be false"
    assert not any(max(x, y) > 2 * min(x, y) for x, y in zip(a, b)), \
        "'one season more than twice the other somewhere' must be false"
    assert a.index(max(a)) == b.index(max(b)), \
        ("'the port with the most departures in the first season has the fewest in the "
         "second' must be false; it must in fact have the most in both")
    return (f"season one {a} against season two {b}: both seasons used at every port and "
            f"the first-season shares {[round(s, 2) for s in shares]} all sit near half")


def q7(table, item):
    """Both directions everywhere, and the leading direction not uniform."""
    brought, taken = cg.col(table, BROUGHT), cg.col(table, TAKEN)
    assert all(x > 0 for x in brought) and all(y > 0 for y in taken), \
        f"both kinds must appear at every port: {brought} and {taken}"
    leads = [("in" if x > y else "out" if y > x else "level")
             for x, y in zip(brought, taken)]
    assert len(set(leads)) > 1, f"the leading direction must not be uniform: {leads}"
    # every distractor false on the same numbers
    assert not all(y == 0 for y in taken), "'only introduced practices recorded' must be false"
    assert not all(x == 0 for x in brought), "'only adopted practices recorded' must be false"
    assert brought.index(max(brought)) != taken.index(max(taken)), \
        "'the port with the most introduced also has the most adopted' must be false"
    return (f"introduced {brought} against taken up {taken}: both present at every port "
            f"and the leading direction runs {leads}")


def q9(table, item):
    """The two rankings agree -- consistent with, not proof of, the claim."""
    by_ships = cg.ranked(table, SHIPS)
    by_offices = cg.ranked(table, OFFICES)
    assert by_ships == by_offices, \
        f"the two rankings must agree: {by_ships} against {by_offices}"
    # every distractor false on the same numbers
    assert by_ships != list(reversed(by_offices)), "'the rankings are reversed' must be false"
    offices = cg.col(table, OFFICES)
    assert cg.cell(table, by_ships[0], OFFICES) != min(offices), \
        "'the busiest settlement has the fewest offices' must be false"
    assert len(set(offices)) > 1, "'every settlement has the same number of offices' must be false"
    assert sum(1 for o in offices if o > 0) > 1, \
        "'offices at only one settlement' must be false"
    return (f"ranking by ships {by_ships} matches ranking by offices {by_offices}, which "
            f"is a correlation and not by itself a direction of cause")


TABLE_CHECKS = {4: q4, 7: q7, 9: q9}

CLAIMS = [
 ("knowing when a wind reverses is part of what made a regular long voyage possible",
  "KC-3.1.II.A.i states that the expansion and intensification of long-distance trade routes often depended on environmental knowledge, including advanced knowledge of the monsoon winds, and the Humans and the Environments thematic focus states that the environment shapes human societies."),

 ("Improved transportation technologies, which the Indian Ocean sentence names alongside commercial practices",
  "KC-3.1.I.A.i attributes the change on the Silk Roads to improved commercial practices, while KC-3.1.I.A.ii attributes it to improved TRANSPORTATION TECHNOLOGIES AND commercial practices. Increased volume, expanded range and the growth of powerful new trading cities stand in both sentences, so the transportation clause is the only addition."),

 ("political development in the region is treated as an effect of the exchange",
  "KC-3.1.I.A.iii states in one sentence that the Indian Ocean trading network fostered the growth of states. The framework makes the network the agent and the growth of states the effect, which is what the reversed option and the null option each deny."),

 ("at none of them does either season account for much more than half",
  "Recomputed in q4 above from the two columns, distractors included. KC-3.1.II.A.i states that the expansion and intensification of long-distance trade routes often depended on environmental knowledge, including advanced knowledge of the monsoon winds, and traffic balanced between two opposing seasons is what sailing to a reversing wind looks like in a port's records."),

 ("since the traffic came first and the apparatus of government followed it",
  "KC-3.1.I.A.iii states that the Indian Ocean trading network fostered the growth of states, which fixes the direction of the relation. The anchor carries both the traffic and the government in order because the strongest distractor exchanges them."),

 ("indigenous cultures in turn influenced the merchants' own",
  "KC-3.1.III.B states that in key places along important trade routes merchants set up diasporic communities where they introduced their own cultural traditions into the indigenous cultures AND, IN TURN, indigenous cultures influenced merchant cultures. The anchor carries both directions because each of the two strongest distractors keeps one and drops the other."),

 ("the direction in which more practices moved is not the same at all three",
  "Recomputed in q7 above from the two columns. KC-3.1.III.B describes influence running in both directions between settled merchant communities and the societies around them, and figures in which neither direction predominates everywhere are what such a relation looks like in a record."),

 ("bear on how a vessel is navigated and loaded",
  "KC-3.1.I.C.ii states that the growth of interregional trade in luxury goods was encouraged by significant innovations in PREVIOUSLY EXISTING transportation and commercial technologies, including the use of the compass, the astrolabe, and larger ship designs. All three instances the sentence gives belong to the transportation half of that pair."),

 ("rank in the same order by ships calling as by offices recorded",
  "Recomputed in q9 above from the two columns. KC-3.1.I.A.iii states that the Indian Ocean trading network fostered the growth of states, and two measures ranking the same settlements alike is consistent with that claim. The keyed wording says consistent with rather than proves, because a ranking cannot establish a direction of cause on its own."),

 ("the settlers' traditions enter the host society and the host society's enter theirs",
  "KC-3.1.III.B states that merchants set up diasporic communities where they introduced their own cultural traditions into the indigenous cultures and, in turn, indigenous cultures influenced merchant cultures. The account in the stem shows both halves of that sentence at once."),

 ("treated as a condition of the growth rather than a consequence of it",
  "KC-3.1.II.A.i states that the expansion and intensification of long-distance trade routes often DEPENDED ON environmental knowledge, including advanced knowledge of the monsoon winds. Depending on something makes it a condition, and the monsoon is a maritime instance rather than an overland one."),

 ("directed by a single state that controlled the whole of it",
  "KC-3.1.I.A.ii, KC-3.1.I.A.iii, KC-3.1.III.B and KC-3.1.II.A.i between them assert increased volume, the fostering of states, diasporic merchant communities and a dependence on environmental knowledge. A single controlling state appears in none of those sentences."),

 ("Innovations in transportation technologies already in use",
  "KC-3.1.I.C.ii states that the growth of interregional trade in luxury goods was encouraged by significant innovations in previously existing transportation and commercial technologies, including the use of the compass, the astrolabe, and larger ship designs. Every feature of the inventory in the stem belongs to that clause."),

 ("an instance of the interregional contacts and conflicts",
  "KC-3.2.II.A.iii states that interregional contacts and conflicts between states and empires encouraged significant technological and cultural transfers, INCLUDING during Chinese maritime activity led by Ming Admiral Zheng He. The word including makes the voyages one case of the pattern rather than the whole of it."),

 ("which is a political effect asserted in the same set of sentences as the commercial ones",
  "KC-3.1.I.A.iii states that the Indian Ocean trading network fostered the growth of states, standing beside KC-3.1.I.A.ii's account of volume and range. The four rejected options are true of the framework but bear on the commerce or the navigation rather than on the politics."),

 ("settled in the place, which is what allows traditions to pass in both directions",
  "KC-3.1.III.B states that in key places along important trade routes MERCHANTS SET UP DIASPORIC COMMUNITIES where they introduced their own cultural traditions into the indigenous cultures and, in turn, indigenous cultures influenced merchant cultures. Settlement is what the sentence describes and what its two-way influence requires. The anchor carries the settlement and its consequence together because one distractor exchanges the two descriptions."),

 ("introduced by a settled merchant community entering the practice of the host society",
  "KC-3.1.III.B states that merchants introduced their own cultural traditions into the indigenous cultures and that indigenous cultures in turn influenced merchant cultures. The movement described in this stem runs from the merchants into the town, and the anchor names the direction because the strongest distractor reverses it."),

 ("in a rhythm no change of vessel would produce",
  "KC-3.1.II.A.i states that the expansion and intensification of long-distance trade routes often depended on environmental knowledge, INCLUDING ADVANCED KNOWLEDGE OF THE MONSOON WINDS. A seasonal rhythm in the sailings is the signature of that knowledge, while larger ships and better instruments belong to KC-3.1.I.C.ii's technological clause instead."),

 ("so the effect it describes runs in both directions",
  "KC-3.1.III.B states that merchants introduced their own cultural traditions into the indigenous cultures AND, IN TURN, indigenous cultures influenced merchant cultures. The phrase in turn is the framework's own, and it is exactly what a one-way account leaves out."),

 ("paired with an increased volume of trade and an extended range for routes already in use",
  "KC-3.1.I.A.ii states that improved transportation technologies and commercial practices led to an increased volume of trade and expanded the geographical range of existing trade routes, including the Indian Ocean. That is the pairing the sentence itself makes; each rejected option joins a cause to an effect the framework does not attach to it."),

 ("without stating which direction carried more in any particular place",
  "KC-3.1.III.B states that merchants introduced their own cultural traditions into the indigenous cultures and that indigenous cultures in turn influenced merchant cultures. It supplies no magnitude on either side and names no particular place, so a claim about which way the balance fell would go past the sentence."),

 ("The state's growth and the network's traffic reinforce one another",
  "KC-3.1.I.A.iii states that the Indian Ocean trading network fostered the growth of states, and KC-3.1.III.B records merchants settling in key places along important trade routes. A ruler protecting and taxing that traffic is the state side of the same relation."),

 ("what changed was their improvement and spread, not their first appearance",
  "KC-3.1.I.C.ii states that the growth of interregional trade in luxury goods was encouraged by significant innovations in PREVIOUSLY EXISTING transportation and commercial technologies, including the use of the compass, the astrolabe, and larger ship designs. The adjective is the framework's own."),

 ("practices of the ports among the merchants",
  "KC-3.1.III.B states that merchants introduced their own cultural traditions into the indigenous cultures and, in turn, indigenous cultures influenced merchant cultures, and the Cultural Developments thematic focus states that the interactions of societies and their beliefs often have political, social, and cultural implications."),

 ("the environment shaping the societies that trade and those populations in turn shaping their environments",
  "The Humans and the Environments thematic focus states that the environment shapes human societies, and as populations grow and change, these populations IN TURN shape their environments, while KC-3.1.II.A.i makes environmental knowledge a condition of the expansion of long-distance routes. The anchor carries both directions because two distractors keep one and drop the other."),

 ("the places where merchants settled and cultural traditions passed between communities",
  "KC-3.1.I.A.ii supplies the increased volume of trade on existing routes including the Indian Ocean, and KC-3.1.III.B supplies the diasporic communities in key places along important trade routes where traditions moved both ways. The framework asserts both of the same routes, which is why both descriptions hold."),

 ("built up in the same years as its shipping traffic multiplied",
  "KC-3.1.I.A.iii states that the Indian Ocean trading network fostered the growth of states. Government and traffic growing together is the pattern that sentence predicts, so evidence of it bears directly on a claim that the two were unconnected."),

 ("so it is part of the account of the trade itself",
  "KC-3.1.II.A.i states that the expansion and intensification of long-distance trade routes often depended on environmental knowledge, including advanced knowledge of the monsoon winds, and Learning Objective G of this unit asks for the role of environmental factors in the development of networks of exchange in the period from c. 1200 to c. 1450."),

 ("woven into the institutions of its host society while keeping observances of its own",
  "KC-3.1.III.B states that merchants set up diasporic communities where they introduced their own cultural traditions into the indigenous cultures and, in turn, indigenous cultures influenced merchant cultures. Keeping an observance while using a local court is both halves of that sentence in a single life."),

 ("the whole depended on knowing when the winds would turn",
  "KC-3.1.I.A.ii supplies the improved transportation technologies and commercial practices and the increased volume on existing routes, KC-3.1.I.A.iii the fostering of states, KC-3.1.III.B the diasporic communities and their two-way influence, and KC-3.1.II.A.i the dependence on environmental knowledge including the monsoon winds. Each rejected option contradicts at least one of the four."),
]

wh_check.run(w2_3, CLAIMS, TABLE_CHECKS, sys.argv)
