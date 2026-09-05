"""Key audit for AP WORLD HISTORY: MODERN 2.6 (Unit 2, environmental consequences).

One (anchor, claim) per question, in module order. The anchor is a distinctive
substring of that question's OWN keyed choice and of no distractor; the claim
states the CED sentence the key rests on, with its Key Concept or Learning
Objective code.

WHAT THE KEYS REST ON -- ONE SENTENCE, AND THE WHOLE MODULE IS BUILT ON ITS CLAUSES
------------------------------------------------------------------------------------
This is among the thinnest pages in the course:

  LO 2.K       explain the ENVIRONMENTAL effects of the various networks of
               exchange in Afro-Eurasia from c. 1200 to c. 1450
  skill 5.A    identify patterns among or connections between developments
  KC-3.1.IV    there was CONTINUED diffusion of CROPS AND PATHOGENS, with
               epidemic diseases, INCLUDING the bubonic plague, ALONG TRADE
               ROUTES
  the ENV thematic focus paragraph

Four clauses of that one sentence carry thirty questions, and each is keyed
somewhere:

  "continued"          q2, q5, q22   -- the process predates the period
  "crops and pathogens" q12, q26     -- one movement, two kinds of cargo
  "including"          q8            -- the plague is an instance, not the class
  "along trade routes" q3, q4, q13   -- the path is what makes this connectivity

WHAT IS NOT KEYED, AND WHY THAT MATTERS MOST HERE
---------------------------------------------------
No key asserts a mortality figure, a date for any outbreak, a mechanism of
transmission, a climatic episode, or a demographic consequence. All of those
are things a well-prepared reader knows about the fourteenth century and none
of them is on this CED page, so a key resting on one could not be checked
against the framework by anyone reading this bank later. That is the rule in
HISTORY_BRIEF.md, and this is the topic where it costs the most to keep.

WHERE THE ANCHOR CARRIES TWO CLAUSES, AND WHY
---------------------------------------------
Four distractors here are the SWAP of the key rather than an unrelated claim:

  q5   the crops recorded somewhere BEFORE the period, against nowhere before
  q7   the most crops and the most outbreaks, asserted to coincide
  q9   the environment shaping societies / societies shaping environments
  q20  presence in a region against arrival from elsewhere, exchanged

Those anchors carry both clauses in order, which is the defect verify_e2_1.py
shipped and HISTORY_BRIEF.md records.

DATA QUESTIONS
--------------
Items 3, 5 and 7 carry tables of HYPOTHETICAL figures and each stem says so.
Each keyed conclusion is recomputed below from the table alone AND every
distractor is shown false on the same numbers. q3's keyed choice says
"consistent with" rather than "shows", because a delay growing with distance is
compatible with movement along the route and does not by itself establish it --
the same restraint verify_w2_3.py's q9 records. The control's per-table catch
rate is never nine of nine: the label column cannot be corrupted into a
contradiction, and a corruption leaving the keyed conclusion TRUE must not be
caught. A zero would mean the check had stopped reading its table.

NEGATIVE CONTROL: `python3 verify_w2_6.py --selftest`.
"""
import sys

import cg_check as cg
import w2_6
import wh_check

DISTANCE = "Days of travel from the nearest trade route"
DELAY = "Years after the first record elsewhere that the outbreak is recorded here"
BEFORE_R = "Regions in which it is recorded before this period"
DURING_R = "Regions in which it is recorded during this period"
CROPS = "Crops recorded as newly present along it"
OUTBREAKS = "Epidemic outbreaks recorded along it"


def q3(table, item):
    """Delay grows with distance from the route, at every step."""
    distance, delay = cg.col(table, DISTANCE), cg.col(table, DELAY)
    order = sorted(range(len(distance)), key=lambda i: distance[i])
    ordered_delay = [delay[i] for i in order]
    assert all(b > a for a, b in zip(ordered_delay, ordered_delay[1:])), \
        f"delay must rise with distance: distances {distance}, delays {delay}"
    # every distractor false on the same numbers
    assert not all(b < a for a, b in zip(ordered_delay, ordered_delay[1:])), \
        "'the furthest settlement records it earliest' must be false"
    assert len(set(delay)) > 1, "'the same interval everywhere' must be false"
    nearest = distance.index(min(distance))
    assert delay[nearest] != max(delay), \
        "'the nearest settlement records it last' must be false"
    assert all(d > 0 for d in delay), "'no settlement records the outbreak' must be false"
    return (f"distances {distance} against delays {delay}: ordered by distance the delays "
            f"run {ordered_delay}, rising at every step")


def q5(table, item):
    """Present somewhere BEFORE, and in more regions DURING -- a continuation."""
    before, during = cg.col(table, BEFORE_R), cg.col(table, DURING_R)
    assert all(b > 0 for b in before), \
        f"every crop must already be recorded somewhere before the period: {before}"
    assert all(d > b for b, d in zip(before, during)), \
        f"every crop must reach more regions during the period: {before} to {during}"
    # every distractor false on the same numbers
    assert not any(b == 0 for b in before), "'recorded nowhere before' must be false"
    assert not any(d < b for b, d in zip(before, during)), \
        "'fewer regions during' must be false"
    widest_before = before.index(max(before))
    assert during[widest_before] != min(during), \
        "'the widest crop before is the narrowest during' must be false"
    assert len(set(during)) > 1, "'the same number of regions during' must be false"
    return (f"before {before} and during {during}: every crop is already somewhere and "
            f"every crop is in more places later, which is a continuation")


def q7(table, item):
    """Both present on every route, and the two maxima on different routes."""
    crops, outbreaks = cg.col(table, CROPS), cg.col(table, OUTBREAKS)
    assert all(c > 0 for c in crops) and all(o > 0 for o in outbreaks), \
        f"every route must record both: crops {crops}, outbreaks {outbreaks}"
    assert crops.index(max(crops)) != outbreaks.index(max(outbreaks)), \
        f"the two maxima must fall on different routes: {crops} and {outbreaks}"
    # every distractor false on the same numbers
    assert not any(o == 0 for o in outbreaks), "'a route with no outbreak' must be false"
    assert not all(o == 0 for o in outbreaks), "'no route records an outbreak' must be false"
    assert not all(o > c for c, o in zip(crops, outbreaks)), \
        "'outbreaks outnumber crops everywhere' must be false"
    return (f"crops {crops} and outbreaks {outbreaks}: both present on every route, and "
            f"the maxima fall on routes {crops.index(max(crops)) + 1} and "
            f"{outbreaks.index(max(outbreaks)) + 1}")


TABLE_CHECKS = {3: q3, 5: q5, 7: q7}

CLAIMS = [
 ("diffusion of crops and of pathogens continued along those routes",
  "KC-3.1.IV states that there was continued diffusion of crops and pathogens, with epidemic diseases, including the bubonic plague, along trade routes. Both kinds stand in the one clause, and the word continued rules out an origin inside the period."),

 ("calls the diffusion CONTINUED",
  "KC-3.1.IV states that there was CONTINUED diffusion of crops and pathogens along trade routes, and the CED separately states that developments are not constrained by the given dates and may begin before the period. The adjective is the framework's own, which is what the student's sentence contradicts."),

 ("the later the outbreak is recorded there",
  "Recomputed in q3 above from the two columns, distractors included. KC-3.1.IV states that there was continued diffusion of crops and pathogens, with epidemic diseases, including the bubonic plague, ALONG TRADE ROUTES, and a delay that grows with distance from a route is what movement along that route looks like in figures. The keyed wording says consistent with rather than shows, because a correlation does not by itself fix a path."),

 ("the same connections that carried goods are treated as the paths disease travelled",
  "KC-3.1.IV states that there was continued diffusion of crops and pathogens, with epidemic diseases, including the bubonic plague, ALONG TRADE ROUTES. The prepositional phrase is what makes this an environmental consequence of connectivity rather than a separate subject."),

 ("already recorded somewhere before the period and is recorded in more regions during it",
  "Recomputed in q5 above from the two columns. KC-3.1.IV states that there was CONTINUED diffusion of crops and pathogens along trade routes, and a crop already present somewhere and present in more places later is that continuation in figures. The anchor carries both clauses because the strongest distractor denies the earlier presence."),

 ("diffusion of a crop along a route of exchange",
  "KC-3.1.IV states that there was continued diffusion of crops and pathogens along trade routes, and Learning Objective K asks students to explain the environmental effects of the various networks of exchange in Afro-Eurasia from c. 1200 to c. 1450."),

 ("the route recording the most crops is not the route recording the most outbreaks",
  "Recomputed in q7 above from the two columns. KC-3.1.IV puts the diffusion of crops and of pathogens in one clause about trade routes, so both appearing along every route is what the sentence predicts, while the framework nowhere makes their quantities move together. The anchor carries both clauses because the strongest distractor asserts that the two maxima coincide."),

 ("one instance of a wider class of epidemic diseases",
  "KC-3.1.IV states that there was continued diffusion of crops and pathogens, with epidemic diseases, INCLUDING the bubonic plague, along trade routes. The word marks an instance of a class, which is the same function it performs elsewhere in the framework."),

 ("the environment shaping human societies and those societies in turn shaping their environments",
  "The Humans and the Environments thematic focus states that the environment shapes human societies, and as populations grow and change, these populations IN TURN shape their environments, while KC-3.1.IV supplies what this topic's environment carries. The anchor carries both directions because two distractors keep one and drop the other."),

 ("that population in turn changing the ground it lived on",
  "KC-3.1.IV states that there was continued diffusion of crops along trade routes, and the Humans and the Environments thematic focus states that the environment shapes human societies and that as populations grow and change these populations in turn shape their environments."),

 ("confined to a single region of Afro-Eurasia",
  "KC-3.1.IV states that there was continued diffusion of crops and pathogens, with epidemic diseases, including the bubonic plague, along trade routes, and Learning Objective K frames the topic as the environmental effects of the various networks of exchange IN AFRO-EURASIA. No confinement to one region is asserted anywhere."),

 ("in a single clause about the same trade routes",
  "KC-3.1.IV states that there was continued diffusion of CROPS AND PATHOGENS, with epidemic diseases, including the bubonic plague, along trade routes. One clause, one set of routes and two kinds of cargo is what makes the benefits and harms of connectivity inseparable in this account."),

 ("appearing first in places connected by traffic and only later in nearer places off the route",
  "KC-3.1.IV states that there was continued diffusion of crops and pathogens, with epidemic diseases, including the bubonic plague, ALONG TRADE ROUTES. An order of arrival following connection rather than distance is what movement along a route would leave in a record."),

 ("thought to travel with the traffic",
  "KC-3.1.IV states that there was continued diffusion of crops and pathogens, with epidemic diseases, including the bubonic plague, along trade routes. A measure aimed at arriving traffic is a measure aimed at the path the framework names."),

 ("changes what grows there and what the ground is used for",
  "Learning Objective K asks students to explain the ENVIRONMENTAL effects of the various networks of exchange, KC-3.1.IV places the diffusion of crops among those effects, and the Humans and the Environments thematic focus states that populations shape their environments as they grow and change."),

 ("Evidence of a route joining the two and of the crop's presence at points along it",
  "KC-3.1.IV states that there was continued DIFFUSION of crops and pathogens ALONG TRADE ROUTES, which makes the route the framework's own mechanism. Suggested skill 5.A asks for connections between developments, and a connection is exactly what simultaneity by itself does not supply."),

 ("without stating how many people they killed or in which years they arrived",
  "KC-3.1.IV states that there was continued diffusion of crops and pathogens, with epidemic diseases, including the bubonic plague, along trade routes. It supplies no mortality, no date and no mechanism, so a key resting on any of those would rest on something outside the framework."),

 ("supporting a general claim rather than establishing by itself what happened across Afro-Eurasia",
  "KC-3.1.IV asserts the diffusion of epidemic diseases along trade routes as a general development, and Learning Objective K asks for the environmental effects of the various networks of exchange in Afro-Eurasia. One town's record illustrates a general claim without establishing it and without needing to be typical."),

 ("the appearance along it of a crop that had not grown there before",
  "KC-3.1.IV states that there was continued diffusion of crops and pathogens along trade routes, which makes a crop's arrival along a route a consequence the framework itself asserts. Suggested skill 5.A asks for connections between developments, and each rejected pairing attaches a development to a circumstance that would have held anyway."),

 ("The first records a state of affairs and the second asserts that it arrived from elsewhere",
  "KC-3.1.IV states that there was continued DIFFUSION of crops and pathogens, with epidemic diseases, including the bubonic plague, ALONG TRADE ROUTES. Diffusion is the framework's word and it is a claim about movement along a path. The anchor carries both halves in order because the strongest distractor exchanges them."),

 ("the routes it names crossed the regions rather than staying within them",
  "Learning Objective K asks students to explain the environmental effects of the various networks of exchange IN AFRO-EURASIA from c. 1200 to c. 1450, and KC-3.1.IV places the diffusion of crops and pathogens along trade routes, which are what join the regions to one another."),

 ("established long enough for its arrival to have passed out of memory",
  "KC-3.1.IV states that there was CONTINUED diffusion of crops and pathogens along trade routes, and the CED states that developments are not constrained by the given dates and may begin before the period. A spread already beyond living memory is that continuation seen from inside it."),

 ("the same networks carry both subjects",
  "KC-3.1.IV places the diffusion of crops and pathogens ALONG TRADE ROUTES, and KC-3.1.I.A.i, KC-3.1.I.A.ii and KC-3.1.I.A.iv are the framework's sentences on the volume and range of those same routes. Suggested skill 5.A asks for exactly such connections between processes."),

 ("what moves along a route does not stop at the people who carry it",
  "KC-3.1.IV states that there was continued diffusion of crops and pathogens, with epidemic diseases, including the bubonic plague, along trade routes, and the Humans and the Environments thematic focus states that the environment shapes human societies. Neither sentence limits the effect to those who carried the traffic."),

 ("carried something a region could eat as well as something that made it ill",
  "KC-3.1.IV states that there was continued diffusion of CROPS AND PATHOGENS, with epidemic diseases, including the bubonic plague, along trade routes. Both are named in the one clause, which is what a wholly negative account of connectivity leaves out."),

 ("can also show a path that was not commercial",
  "KC-3.1.IV states that there was continued diffusion of crops and pathogens along trade routes, and Learning Objective K asks for the environmental effects of the various networks of exchange. A documented transfer is an instance of the diffusion the sentence asserts, and the framework does not confine such movement to a single kind of carrier."),

 ("names a movement from somewhere to somewhere along a path",
  "KC-3.1.IV states that there was continued diffusion of crops and pathogens, with epidemic diseases, including the bubonic plague, ALONG TRADE ROUTES. The framework attaches its noun to a path, which is what makes this topic a consequence of connectivity rather than a subject on its own."),

 ("land not previously cultivated was brought under the plough",
  "The Humans and the Environments thematic focus states that the environment shapes human societies and that as populations grow and change these populations IN TURN shape their environments, and KC-3.1.IV places the diffusion of crops along trade routes. New ground broken is the population reshaping its environment."),

 ("the consequence of places being joined",
  "KC-3.1.IV states that there was continued diffusion of crops and pathogens, with epidemic diseases, including the bubonic plague, ALONG TRADE ROUTES, and Learning Objective K asks for the environmental effects OF THE VARIOUS NETWORKS OF EXCHANGE. The connection between places is the subject of the topic."),

 ("the regions reached were changed by what arrived and changed their own ground in turn",
  "KC-3.1.IV supplies the continued diffusion of crops and pathogens, with epidemic diseases including the bubonic plague, along trade routes, and the Humans and the Environments thematic focus supplies the two-way relation between populations and their environments. Each rejected option contradicts one or the other."),
]

wh_check.run(w2_6, CLAIMS, TABLE_CHECKS, sys.argv)
