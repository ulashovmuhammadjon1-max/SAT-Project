"""Key audit for AP WORLD HISTORY: MODERN 2.4 (Unit 2, trans-Saharan trade).

One (anchor, claim) per question, in module order. The anchor is a distinctive
substring of that question's OWN keyed choice and of no distractor; the claim
states the CED sentence the key rests on, with its Key Concept or Learning
Objective code.

WHAT THE KEYS REST ON
---------------------
  LO 2.H          the causes and effects of the growth of trans-Saharan trade
  LO 2.I          how the expansion of empires influenced trade and
                  communication over time
  skill 1.B       explain a historical concept, development, or process
  KC-3.1.II.A.ii  the growth of interregional trade was encouraged by
                  innovations in EXISTING transportation technologies
  KC-3.1.I.A.iv   improved transportation technologies and commercial practices
                  led to an increased volume of trade and expanded the
                  geographical range of EXISTING trade routes, including the
                  trans-Saharan trade network
  KC-3.1.I.E.ii   the expansion of empires -- including Mali in West Africa --
                  facilitated Afro-Eurasian trade and communication as new
                  people were drawn into THE economies and trade networks
  the TEC and GOV thematic focus paragraphs

THE ONE COMPARISON WITH ANOTHER TOPIC, AND WHY IT IS SAFE
-----------------------------------------------------------
q13 turns on a difference between KC-3.1.I.E.i (topic 2.2) and KC-3.1.I.E.ii
(this topic). The first says new people were drawn into THEIR CONQUERORS'
economies and trade networks; the second says they were drawn into THE
economies and trade networks. That is a difference in the CED's own text, read
off the framework rather than recalled, and it is the only cross-topic
comparison keyed here.

WHAT IS NOT KEYED. Nothing about gold, salt as a commodity, Mansa Musa, Timbuktu
or Islamic learning in West Africa appears in any key, because the CED asserts
none of them on this page. Mali is named once, where KC-3.1.I.E.ii names it,
and no key asserts anything further about it. The camel saddle and caravans are
illustrative examples, which the CED says "do not in any way constitute
additional, preferred, or required information".

WHERE THE ANCHOR CARRIES TWO CLAUSES, AND WHY
---------------------------------------------
Five distractors here are the SWAP of the key rather than an unrelated claim:

  q5   districts and trading communities, exchanged as the faster-rising column
  q13  which of the two sentences assigns the networks an owner
  q18  efficiency and volume of trade, their definitions exchanged
  q20  which key concept asserts the encouragement and which the volume
  q27  volume and range, their definitions exchanged

Those anchors carry both clauses in order, which is the defect verify_e2_1.py
shipped and HISTORY_BRIEF.md records.

DATA QUESTIONS
--------------
Items 3, 5 and 7 carry tables of HYPOTHETICAL figures and each stem says so.
Each keyed conclusion is recomputed below from the table alone AND every
distractor is shown false on the same numbers. q7's key deliberately separates a
TOTAL from a RATE, because a table of this shape invites a student to treat them
as the same measure. The control's per-table catch rate is never nine of nine:
the label column cannot be corrupted into a contradiction, and a corruption
leaving the keyed conclusion TRUE must not be caught. A zero would mean the
check had stopped reading its table.

NEGATIVE CONTROL: `python3 verify_w2_4.py --selftest`.
"""
import sys

import cg_check as cg
import w2_4
import wh_check

LOAD = "Load carried per animal in units"
DAYS = "Days the animal can travel between waterings"
DISTRICTS = "Districts within the empire"
COMMUNITIES = "Communities recorded trading into the network"
ANIMALS = "Animals travelling in the caravan"
GUARDS = "Guards recorded travelling with it"


def q3(table, item):
    """Load and endurance rise together -- no trade-off between the two."""
    load, days = cg.col(table, LOAD), cg.col(table, DAYS)
    assert cg.ranked(table, LOAD) == cg.ranked(table, DAYS), \
        f"the two rankings must agree: {cg.ranked(table, LOAD)} vs {cg.ranked(table, DAYS)}"
    # every distractor false on the same numbers
    assert cg.ranked(table, LOAD) != list(reversed(cg.ranked(table, DAYS))), \
        "'the two move in opposite directions' must be false"
    assert cg.cell(table, cg.ranked(table, LOAD)[0], DAYS) != min(days), \
        "'the heaviest load travels fewest days' must be false"
    assert len(set(days)) > 1, "'every arrangement allows the same days' must be false"
    assert cg.cell(table, cg.ranked(table, LOAD)[-1], DAYS) != max(days), \
        "'the lightest load travels the most days' must be false"
    return (f"loads {load} and days {days} rank the arrangements in the same order, so "
            f"neither measure is bought at the other's expense")


def q5(table, item):
    """Both columns rise, and the trading communities rise by MORE each step."""
    districts = cg.col(table, DISTRICTS)
    communities = cg.col(table, COMMUNITIES)
    assert all(b > a for a, b in zip(districts, districts[1:])), \
        f"districts must rise at every step: {districts}"
    assert all(b > a for a, b in zip(communities, communities[1:])), \
        f"trading communities must rise at every step: {communities}"
    d_gains = [b - a for a, b in zip(districts, districts[1:])]
    c_gains = [b - a for a, b in zip(communities, communities[1:])]
    assert all(c > d for d, c in zip(d_gains, c_gains)), \
        f"communities must rise by more at every step: districts {d_gains}, communities {c_gains}"
    # every distractor false on the same numbers
    assert not all(d > c for d, c in zip(d_gains, c_gains)), \
        "'districts rise by more at every step' must be false"
    assert not any(b < a for a, b in zip(communities, communities[1:])), \
        "'trading communities fall' must be false"
    assert not any(b < a for a, b in zip(districts, districts[1:])), \
        "'districts fall' must be false"
    assert len(set(districts)) > 1, "'both counts unchanged' must be false"
    return (f"districts {districts} gain {d_gains} while trading communities "
            f"{communities} gain {c_gains}, more at each step")


def q7(table, item):
    """The largest TOTAL of guards is not the largest RATE per hundred animals."""
    animals, guards = cg.col(table, ANIMALS), cg.col(table, GUARDS)
    rates = [100 * g / a for a, g in zip(animals, guards)]
    assert guards.index(max(guards)) != rates.index(max(rates)), \
        f"the biggest total {guards} and the biggest rate {rates} must be different caravans"
    # every distractor false on the same numbers
    assert animals.index(max(animals)) != rates.index(max(rates)), \
        "'the largest caravan also has the highest rate' must be false"
    assert min(guards) > 0, "'the smallest caravan travels without guards' must be false"
    assert len(set(rates)) > 1, "'every caravan has the same rate' must be false"
    assert animals.index(min(animals)) != guards.index(max(guards)), \
        "'the smallest caravan has the most guards in total' must be false"
    return (f"animals {animals} and guards {guards} give rates per hundred "
            f"{[round(r, 2) for r in rates]}; the largest total and the largest rate "
            f"fall on different caravans")


TABLE_CHECKS = {3: q3, 5: q5, 7: q7}

CLAIMS = [
 ("innovations in transportation technologies already in use",
  "KC-3.1.II.A.ii states that the growth of interregional trade was encouraged by innovations in EXISTING transportation technologies, and this topic page names the camel saddle and caravans as its illustrative instances. The word existing is what defeats the option calling them inventions without precedent."),

 ("among EXISTING trade routes whose geographical range",
  "KC-3.1.I.A.iv states that improved transportation technologies and commercial practices led to an increased volume of trade and expanded the geographical range of existing trade routes, INCLUDING THE TRANS-SAHARAN TRADE NETWORK. The sentence places the network among routes already in use."),

 ("rise together across the arrangements listed",
  "Recomputed in q3 above from the two columns, distractors included. KC-3.1.II.A.ii states that the growth of interregional trade was encouraged by innovations in existing transportation technologies, and the Technology thematic focus says human adaptation and innovation have resulted in increased efficiency. Two measures improving together is what such an innovation looks like in figures."),

 ("what a party can carry between them sets the limit on the journey",
  "KC-3.1.II.A.ii states that the growth of interregional trade was encouraged by innovations in existing transportation technologies, and the Technology thematic focus states that human adaptation and innovation have resulted in increased efficiency, comfort, and security. What a party can carry between stages is the constraint such innovations relieve."),

 ("the communities trading into the network rise by more than the districts do",
  "Recomputed in q5 above from the two columns. KC-3.1.I.E.ii states that the expansion of empires, including Mali in West Africa, facilitated Afro-Eurasian trade and communication as new people were drawn into the economies and trade networks. The anchor carries both columns in order because the strongest distractor exchanges them."),

 ("spreads the cost of guidance and protection",
  "The Technology thematic focus states that human adaptation and innovation have resulted in increased efficiency, comfort, and SECURITY, and KC-3.1.II.A.ii names innovations in existing transportation technologies as an encouragement to interregional trade, with caravans as this page's own illustrative instance."),

 ("most guards in total is not the caravan carrying the most guards for each hundred animals",
  "Recomputed in q7 above from the two columns. KC-3.1.II.A.ii names innovations in existing transportation technologies as an encouragement to interregional trade, with caravans among this page's illustrative instances, and the Technology thematic focus names increased security among the results of human adaptation. A total and a rate that fall on different caravans is the distinction such figures let a student draw, and the anchor carries both measures because the strongest distractor asserts that they coincide."),

 ("peoples not previously part of a network were drawn into the economies",
  "KC-3.1.I.E.ii states that the expansion of empires, including Mali in West Africa, facilitated Afro-Eurasian trade and communication as new people were drawn into the economies and trade networks. Expansion stands first in that sentence and facilitation follows, which is what the reversed option gets wrong."),

 ("turn traffic passing through its territory into revenue",
  "The Governance thematic focus states that governments obtain, retain, and exercise power in different ways and for different purposes and maintain order through administrative institutions, policies, and procedures, and KC-3.1.I.E.ii ties imperial expansion to the facilitation of trade and communication."),

 ("in separate sentences about the same growth",
  "KC-3.1.II.A.ii names innovations in existing transportation technologies, KC-3.1.I.A.iv names improved transportation technologies and commercial practices, and KC-3.1.I.E.ii names the expansion of empires. Learning Objective H asks for the causes and effects of the growth of trans-Saharan trade, and the framework supplies more than one cause for it."),

 ("a technical and a political cause respectively",
  "KC-3.1.II.A.ii and KC-3.1.I.A.iv sit under the Technology and Innovation focus and name innovations in existing transportation technologies and improved commercial practices, while KC-3.1.I.E.ii sits under the Governance focus and names the expansion of empires. Learning Objective H asks for the causes and effects of the growth of trans-Saharan trade and Learning Objective I for the influence of imperial expansion. This item replaced one on the word EXISTING that duplicated topic 2.1 q3."),

 ("its effects are not exhausted by its purpose",
  "The Technology thematic focus states that technological advances have shaped human development and interactions WITH BOTH INTENDED AND UNINTENDED CONSEQUENCES, which is the framework's own phrase, and KC-3.1.II.A.ii supplies this topic's case, an innovation in an existing transportation technology whose effects ran well past the journeys it was adopted to ease."),

 ("The sentence naming conquerors assigns the networks an owner while the other does not",
  "KC-3.1.I.E.i states that new people were drawn into THEIR CONQUERORS' economies and trade networks, while KC-3.1.I.E.ii, this topic's sentence, states that they were drawn into THE economies and trade networks. The anchor carries both halves in order because the strongest distractor exchanges them, and the difference was read off the CED text rather than recalled."),

 ("makes passage and redress dependable lowers what a merchant must risk",
  "KC-3.1.I.E.ii states that the expansion of empires, including Mali in West Africa, facilitated Afro-Eurasian trade and communication, and the Governance thematic focus states that governments maintain order through a variety of administrative institutions, policies, and procedures."),

 ("began only after an empire had been established across the whole of the route",
  "KC-3.1.II.A.ii, KC-3.1.I.A.iv and KC-3.1.I.E.ii between them assert the encouragement given by innovations in existing technologies, the increase in volume and range, and the facilitation by imperial expansion. None makes an empire a precondition of the trade, and KC-3.1.I.A.iv calls the network an existing route."),

 ("with a reason for other powers to deal with it",
  "The Governance thematic focus states that governments obtain, retain, and exercise power in different ways and for different purposes, and KC-3.1.I.E.ii links the expansion of empires to the facilitation of Afro-Eurasian trade and communication as new people were drawn into the economies and trade networks."),

 ("It is an improved commercial practice",
  "KC-3.1.I.A.iv states that improved transportation technologies AND COMMERCIAL PRACTICES led to an increased volume of trade and expanded the geographical range of existing trade routes, including the trans-Saharan trade network. Settlement deferred to a later meeting is a commercial practice rather than a transport technology."),

 ("efficiency describes what a given effort can accomplish, while an increase in trade describes how much is actually carried",
  "The Technology thematic focus states that human adaptation and innovation have resulted in increased efficiency, comfort, and security, while KC-3.1.I.A.iv states that improved technologies and practices led to an increased VOLUME OF TRADE. The anchor carries both halves in order because the strongest distractor exchanges the definitions."),

 ("placing the West African case inside a wider network",
  "KC-3.1.I.E.ii states that the expansion of empires, including Mali in West Africa, facilitated AFRO-EURASIAN trade and communication as new people were drawn into the economies and trade networks. The adjective is the framework's own and it is what places the case in a wider frame."),

 ("The first says innovations in existing transportation technologies encouraged the growth of interregional trade, while the second adds commercial practices",
  "KC-3.1.II.A.ii states that the growth of interregional trade was encouraged by innovations in existing transportation technologies, and KC-3.1.I.A.iv states that improved transportation technologies AND COMMERCIAL PRACTICES led to an increased volume of trade and expanded the geographical range of existing trade routes. The anchor carries both halves in order because the strongest distractor exchanges them."),

 ("made the places where it halted into centres of exchange in their own right",
  "KC-3.1.I.A.iv states that improved transportation technologies and commercial practices led to an increased volume of trade and expanded the geographical range of existing trade routes, including the trans-Saharan trade network, promoting the growth of powerful new trading cities."),

 ("joining the two with the word as rather than setting them side by side",
  "KC-3.1.I.E.ii states that the expansion of empires, including Mali in West Africa, facilitated Afro-Eurasian trade and communication AS new people were drawn into the economies and trade networks. The connective is the framework's own and it makes the second clause a consequence of the first rather than a coincidence with it."),

 ("without naming which innovation mattered most",
  "KC-3.1.II.A.ii states only that the growth of interregional trade was encouraged by innovations in existing transportation technologies, and this topic's illustrative list names the camel saddle and caravans without ranking them. The CED adds that illustrative examples do not constitute required information."),

 ("a barrier to those without them and a route to those with them",
  "KC-3.1.II.A.ii states that the growth of interregional trade was encouraged by innovations in existing transportation technologies, and the Technology thematic focus states that human adaptation and innovation have resulted in increased efficiency, comfort, and security. What such adaptation relieves is exactly the difficulty of the ground."),

 ("after an expanding empire brought their territory under its authority",
  "KC-3.1.I.E.ii states that the expansion of empires, including Mali in West Africa, facilitated Afro-Eurasian trade and communication AS NEW PEOPLE WERE DRAWN INTO the economies and trade networks. New entrants following incorporation is the framework's own mechanism, and it is a political condition rather than a technical one."),

 ("without which the technologies of carriage would not by themselves have made the crossing dependable",
  "KC-3.1.II.A.ii names innovations in existing transportation technologies as an encouragement to the growth of interregional trade, and the Technology thematic focus names increased security among the results of human adaptation. Knowing where the water lies is the adaptation on which the carriage depends."),

 ("more may be carried over the same ground, or the same amount carried over more ground",
  "KC-3.1.I.A.iv states that improved transportation technologies and commercial practices led to an increased volume of trade AND expanded the geographical range of existing trade routes. Two effects are named, and the anchor carries both because the strongest distractor exchanges their definitions."),

 ("its effect is largest where that difficulty is greatest",
  "The Technology thematic focus states that human adaptation and innovation have resulted in increased efficiency, comfort, and security, and KC-3.1.II.A.ii ties innovations in existing transportation technologies to the growth of interregional trade. An adaptation answers a condition, which is why different conditions reward it differently."),

 ("reached beyond what anyone adopting it intended",
  "The Technology thematic focus states that technological advances have shaped human development and interactions WITH BOTH INTENDED AND UNINTENDED CONSEQUENCES, and KC-3.1.I.A.iv ties improved technologies and practices to an increased volume of trade on the trans-Saharan network among others."),

 ("while the expansion of empires drew further peoples into the exchange",
  "KC-3.1.II.A.ii supplies the innovations in existing transportation technologies, KC-3.1.I.A.iv the improved commercial practices with the increased volume and expanded range of existing routes including the trans-Saharan network, and KC-3.1.I.E.ii the facilitation by imperial expansion as new people were drawn into the economies and trade networks. Each rejected option contradicts at least one."),
]

wh_check.run(w2_4, CLAIMS, TABLE_CHECKS, sys.argv)
