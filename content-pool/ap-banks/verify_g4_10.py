"""Key audit for AP HUMAN GEOGRAPHY 4.10 Consequences of Centrifugal and
Centripetal Forces.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. One learning objective and two essential knowledge
statements, and both statements are lists of CONSEQUENCES:

    SPS-4.C   Explain how the concepts of centrifugal and centripetal forces
              apply at the state scale.
    SPS-4.C.1 Centrifugal forces may lead to failed states, uneven development,
              stateless nations, and ethnic nationalist movements.
    SPS-4.C.2 Centripetal forces can lead to ethnonationalism, more equitable
              infrastructure development, and increased cultural cohesion.

Because both statements name outcomes, every item asks about an outcome. An item
that only asked whether a given force is centrifugal or centripetal would be
testing the vocabulary this topic assumes rather than the statements it sets.

THE ASYMMETRY THAT DECIDES THIS MODULE, and the thing most likely to be read as
an error in the CED: ETHNIC NATIONALIST MOVEMENTS sits on the centrifugal list
and ETHNONATIONALISM sits on the centripetal one. Both statements are quoted
above and both readings are the CED's own. The resolution is whether the
identity being mobilized is coextensive with the state or contained inside it: an
identity that the whole state is said to belong to binds people to the state,
while a minority nation's movement inside a larger state pulls against it. Items
5, 12, 18, 22 and 30 turn on this, item 12 asks for it directly, and items 11 and
22 record what the CED does not state -- that a single identity policy can act
centripetally on the majority and centrifugally on a minority at the same time.

THE SECOND PAIRING is uneven development (centrifugal) against more equitable
infrastructure development (centripetal). The two statements name these as
opposites, and infrastructure is where the abstraction becomes visible: roads,
power, water and schools are either spread across a state's regions or
concentrated in some of them. Items 8, 9, 15, 18, 21, 25, 26 and 28 read the
forces off that distribution, which is what makes the topic geographic.

"MAY LEAD TO" AND "CAN LEAD TO". Neither statement asserts the outcome follows.
Items 10, 19, 23 and 30 are keyed against the stronger reading, and item 10
supplies the standing reason a state showing centrifugal forces may not fragment:
the two lists describe a balance, not a classification.

SCALE. Learning objective SPS-4.C says "at the state scale", and the suggested
skill for this topic is comparing processes at various scales. The same identity
is centripetal for a region and centrifugal for the state containing it, so the
scale has to be stated before the question has an answer. Items 6, 16, 22 and 29
are the scale items.

NO REAL COUNTRY IS NAMED. Neither statement names one, failed states and
stateless nations are politically live categories, and a described situation
tests the same understanding without asserting a contested claim.

The three table items (26, 27, 28) are the computational gate:

  26  the spread between best- and worst-served regions, recomputed both times,
      plus the assertion that the TOTAL is unchanged -- without that the
      narrowing could be an expansion of the budget rather than a redistribution,
      and one distractor's premise depends on the total being flat
  27  four separate thresholds, so the keyed state is failing on every measure
      rather than merely worst on one
  28  the richest-to-poorest ratio at both dates, plus the assertion that EVERY
      region's output rose -- the item's point is that growth everywhere is
      compatible with divergence, and a falling region would let a student reach
      the key for the wrong reason

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written. One correction was made during the pass: item 26's table originally
gave post-policy figures summing to 2,600 against a pre-policy 2,000, which
contradicted the item's own `why` ("the total is unchanged") and would have made
a distractor's premise false. The figures now sum to 2,000 both times and the
recompute below asserts it.
"""
import re

import geo_check
import g4_10


def q26_spread_narrows(table):
    """Spread between best- and worst-served regions, and a flat total."""
    before = [float(r[1]) for r in table["rows"]]
    after = [float(r[2]) for r in table["rows"]]
    assert sum(before) == sum(after) == 2000, (sum(before), sum(after))
    spread_before = max(before) - min(before)
    spread_after = max(after) - min(after)
    assert spread_before == 700, spread_before
    assert spread_after == 100, spread_after
    # The capital region must fall, so the distractor built on that premise is
    # true-but-irrelevant rather than false.
    cap = {r[0]: (float(r[1]), float(r[2])) for r in table["rows"]}["Capital region"]
    assert cap[1] < cap[0], cap
    return f"narrowed from {spread_before:.0f} to {spread_after:.0f} currency units"


def q27_failed_state(table):
    """The failing state must fail on every measure, not merely be worst on one."""
    rows = {r[0]: r for r in table["rows"]}
    worst = min(table["rows"], key=lambda r: float(r[1]))
    assert worst[0] == "State 1", worst
    control = float(worst[1])
    revenue = float(worst[2])
    assert control < 50 and revenue < 10 and worst[3] == "No", worst
    # Every other state keeps courts and holds more than three quarters of its
    # territory, so no second candidate is available.
    for name, r in rows.items():
        if name != "State 1":
            assert r[3] == "Yes" and float(r[1]) > 75 and float(r[2]) > 50, r
    return f"controls {control:.0f} percent of its territory"


def q28_ratio_widens(table):
    """Richest-to-poorest ratio at both dates, with every region growing."""
    early = {r[0]: float(r[1].replace(",", "")) for r in table["rows"]}
    late = {r[0]: float(r[2].replace(",", "")) for r in table["rows"]}
    # Growth everywhere is the premise the item rests on.
    assert all(late[k] > early[k] for k in early), (early, late)
    r_early = max(early.values()) / min(early.values())
    r_late = max(late.values()) / min(late.values())
    assert abs(r_early - 2.4) < 0.05, r_early
    assert abs(r_late - 4.43) < 0.05, r_late
    assert r_late > r_early, (r_early, r_late)
    return f"widened from {r_early:.1f} to about {r_late:.1f}"


CLAIMS = [
 ("Failed states, uneven development, stateless nations",
  "EK SPS-4.C.1 names exactly failed states, uneven development, stateless nations and ethnic nationalist movements. Every rejected list either imports an outcome from the centripetal statement or borrows from a neighbouring topic, and keeping the two lists apart is what this topic asks for."),

 ("more equitable infrastructure development, and increased cultural cohesion",
  "EK SPS-4.C.2 names exactly ethnonationalism, more equitable infrastructure development and increased cultural cohesion. Ethnic nationalist movements and uneven development sit on the centrifugal list, so any set combining them with cultural cohesion is drawn from both statements at once."),

 ("the most complete of the centrifugal outcomes",
  "EK SPS-4.C.1 names failed states among the outcomes centrifugal forces may lead to. The defining feature is a government unable to perform the basic functions of a state across its own territory, which is the furthest point the centrifugal list reaches."),

 ("A stateless nation",
  "EK SPS-4.C.1 names stateless nations among the centrifugal outcomes. A nation is a people with a shared identity and a homeland, and it is stateless when no sovereign state corresponds to it, which puts standing pressure on every state its homeland crosses."),

 ("pulls a region away from the state",
  "EK SPS-4.C.1 names ethnic nationalist movements among the centrifugal outcomes. The identity mobilized here is contained inside the state rather than coextensive with it, so organizing around it works against the state's unity -- which is why the CED places it opposite ethnonationalism."),

 ("Centripetally at the regional scale and centrifugally at the state scale",
  "Learning objective SPS-4.C applies these concepts at the state scale, which implies the answer depends on the scale chosen, and the suggested skill for the topic is comparing processes at various scales. A shared identity draws a region's people toward one another and marks them off from the rest of the state in the same movement."),

 ("one set draws its people and regions toward the centre",
  "Enduring understanding SPS-4 concerns challenges to state sovereignty and learning objective SPS-4.C applies these forces at the state scale. Both essential knowledge statements list consequences for a state's cohesion, which identifies cohesion as the quantity the two kinds of force act on."),

 ("a centripetal outcome",
  "EK SPS-4.C.2 names more equitable infrastructure development among the outcomes centripetal forces can lead to. Provision that reaches every region gives each of them a material stake in the state, which is how a government converts revenue into cohesion."),

 ("which the framework lists among the outcomes of centrifugal forces",
  "EK SPS-4.C.1 names uneven development among the centrifugal outcomes. A region that can see it is served far worse than another has a standing grievance against the arrangement producing the difference, which is what makes the pattern divisive rather than merely unequal."),

 ("may follow rather than must",
  "EK SPS-4.C.1 says centrifugal forces MAY LEAD TO those outcomes and EK SPS-4.C.2 says centripetal forces CAN LEAD TO theirs, so neither list is asserted to follow. A state's condition at any moment reflects the balance of the two rather than the presence of either."),

 ("and centrifugal for the linguistic minority",
  "EK SPS-4.C.2 names increased cultural cohesion as a centripetal outcome while EK SPS-4.C.1 names ethnic nationalist movements as a centrifugal one, and one language policy can produce both. Whether a unifying measure unifies depends on who is inside the group it unifies."),

 ("identifies the whole state with one nation",
  "EK SPS-4.C.1 and EK SPS-4.C.2 place ethnic nationalist movements and ethnonationalism on opposite lists, and the difference is whether the identity mobilized is coextensive with the state or contained within it. The same material unifies in the first case and divides in the second."),

 ("Increased cultural cohesion",
  "EK SPS-4.C.2 names increased cultural cohesion among the outcomes centripetal forces can lead to. Public symbols and a common curriculum are the standard instruments for producing a sense of one people out of a population that is not otherwise obviously one thing."),

 ("grievance supports an ethnic nationalist movement",
  "EK SPS-4.C.1 lists its four outcomes without ordering them, but they differ in severity and commonly reinforce one another. Material grievance supplies a reason, identity supplies a claim, and prolonged conflict is what erodes a government's capacity to govern its own territory."),

 ("a visible record of who the state treats as belonging to it",
  "EK SPS-4.C.2 names more equitable infrastructure development among the centripetal outcomes and EK SPS-4.C.1 names uneven development among the centrifugal ones. Investment leaves a physical pattern on the map, which is readable evidence rather than an assertion about attitudes."),

 ("The state scale",
  "Learning objective SPS-4.C says explicitly that these concepts are to be applied at the state scale. They can be used at other scales, but the outcomes both essential knowledge statements list are outcomes for states rather than for households or continents."),

 ("the balance of forces rather than as a function of diversity",
  "EK SPS-4.C.1 and EK SPS-4.C.2 each name outcomes without treating either set as automatic. Diversity supplies possible centrifugal material, but a state investing across its regions and building a shared civic identity is applying the countervailing force the second statement names."),

 ("matched to more equitable infrastructure development",
  "EK SPS-4.C.1 and EK SPS-4.C.2 name seven outcomes between them, and only one pairing here matches a case to the outcome whose description it satisfies. Each rejected pairing substitutes an outcome from one list for an outcome on the other."),

 ("gave the region a stake in remaining",
  "EK SPS-4.C.1 says centrifugal forces MAY LEAD TO their outcomes, which leaves room for a state's response to change the result. Granting a region authority over its own affairs addresses the grievance without conceding the territory, which is the standard countervailing move."),

 ("no state corresponds to the nation",
  "EK SPS-4.C.1 names stateless nations among the centrifugal outcomes, and the condition is structural rather than administrative. A stateless nation may be prosperous and well governed by the states it lives in, because statelessness is a fact about the fit between nations and borders."),

 ("an efficient allocation may still weaken the state's cohesion",
  "EK SPS-4.C.1 names uneven development among the centrifugal outcomes and nothing in the statement requires the pattern to be accidental. A policy chosen for its returns can widen regional differences, which is why cohesion and efficiency can pull a government in opposite directions."),

 ("Centripetal for those the identity includes and centrifugal for those it excludes",
  "EK SPS-4.C.2 names ethnonationalism and increased cultural cohesion as centripetal outcomes while EK SPS-4.C.1 names ethnic nationalist movements as a centrifugal one. The CED's asymmetric placement of the two ethnic terms is precisely what makes a single identity policy readable as both at once."),

 ("reflects the balance between the two kinds of force",
  "EK SPS-4.C.1 uses 'may lead to' and EK SPS-4.C.2 uses 'can lead to', so neither list is asserted to follow from the force it belongs to. Real states show items from both lists at the same time, which is why the pair is more useful as a balance than as a classification."),

 ("the centre has stopped holding the country together",
  "EK SPS-4.C.1 names failed states among the centrifugal outcomes. Centrifugal and centripetal describe forces on a state's cohesion rather than on the line drawn around it, so a government that no longer reaches most of its territory has already lost what the terms measure."),

 ("identity-based outcomes that money alone does not settle",
  "EK SPS-4.C.1 names four outcomes, of which only uneven development is directly material; stateless nations and ethnic nationalist movements rest on identity and on the fit between nations and borders. EK SPS-4.C.2's remedy of equitable infrastructure therefore reaches part of the centrifugal list and not all of it."),

 ("narrowed from 700 to 100 currency units",
  "Recomputed from the figures: the spread between the best- and worst-served regions falls from 700 to 100 currency units while the total is unchanged at 2,000, so this is a redistribution rather than an expansion of the budget. EK SPS-4.C.2 names more equitable infrastructure development among the centripetal outcomes, and a narrowing spread is what that phrase describes.",
  ),

 ("controls 31 percent of its territory",
  "Recomputed from the record: one state holds 31 percent of its territory, collects 8 percent of its revenue outside the capital and has no functioning nationwide courts, while each of the other three exceeds 75 percent on territory, 50 percent on revenue and keeps its courts. EK SPS-4.C.1 names failed states among the centrifugal outcomes, and inability to perform basic functions across the territory is the definition.",
  ),

 ("widened from 2.4 to about 4.4",
  "Recomputed from the figures: every region's output per person rose, yet the richest-to-poorest ratio widens from 2.4 to about 4.4 because the core grew far faster than the rest. EK SPS-4.C.1 names uneven development among the centrifugal outcomes, and growth everywhere is fully compatible with divergence between regions.",
  ),

 ("an identity that binds a region together is the same identity that marks it off",
  "Learning objective SPS-4.C specifies the state scale, which implies the answer changes when a different scale is chosen, and the topic's suggested skill is comparing processes at various scales. This pair of readings is the clearest instance of why the scale has to be stated before the question has an answer."),

 ("may lead to failed states",
  "EK SPS-4.C.1 and EK SPS-4.C.2 state exactly these two lists and use 'may lead to' and 'can lead to' rather than asserting the outcomes follow. Ethnic identity appears on both lists in different forms, which is why a summary calling it always divisive misstates the framework."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"4.10 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"4.10 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_spread_narrows,
    27: q27_failed_state,
    28: q28_ratio_widens,
}

geo_check.check(g4_10, ANCHORS, TABLE_NOTES)
