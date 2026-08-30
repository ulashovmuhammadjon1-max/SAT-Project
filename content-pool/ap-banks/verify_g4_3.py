"""Structural audit for AP HUMAN GEOGRAPHY 4.3 Political Power and Territoriality.

Grounding for the keys:
  PSO-4.C.1 -- political power is expressed geographically as control over
  people, land, and resources, illustrated by neocolonialism, shatterbelts, and
  choke points. Items 1-5, 8-15, 18, 19, 21-23, 25, 27-30 key inside that
  sentence and its three named illustrations.
  PSO-4.C.2 -- territoriality is the connection of people, their culture, and
  their economic systems to the land. Items 6, 7, 16, 17, 20, 24, 26 key to that
  definition, and deliberately to the CULTURE and ECONOMIC clauses of it rather
  than to land ownership, which the framework does not mention.

Item 24 extends territoriality below the state (a garden, a street corner). The
CED's sentence is scale-neutral -- it says "people", not "states" -- so the item
is keyed to the definition as written; the note is here because a reader could
reasonably ask whether the framework licenses the local reading, and it does.

The three illustrations are different KINDS of thing: a relationship, a region,
and a site. Items 14 and 27 test exactly that, and their distractors are the
permutations a student produces from having memorized the three words as an
undifferentiated set.

Two of the three data items make an arithmetic claim; both are recomputed below
from the table's own cells. The third (item 22) is a comparison of given
percentages with nothing to compute.
"""
import geo_check
import g4_3


ANCHORS = [
 "people, land, and resources",                      # 1  PSO-4.C.1 verbatim
 "leverage over global trade",                       # 2  choke point
 "a shatterbelt",                                    # 3  region between rivals
 "small strategic site",                             # 4  local site, global effect
 "economic dependence",                              # 5  neocolonialism
 "connection of a people, their culture",            # 6  PSO-4.C.2 definition
 "customary use rather than legal title",            # 7  grazing routes
 "licenses which foreign firms",                     # 8  control over resources
 "rivalry of outside powers",                        # 9  shatterbelt vs borderland
 "supported opposing local forces",                  # 10 Cold War shatterbelts
 "very narrow and carries the largest share",        # 11 3 km, 21%
 "control of a transit route",                       # 12 landlocked state
 "permits for internal migration",                   # 13 control over people
 "narrow passage whose control confers leverage",    # 14 choke point vs shatterbelt
 "formal independence has not ended",                # 15 base, contracts, currency
 "bound to the specific place",                      # 16 resettlement refusal
 "physical assertion of territoriality",             # 17 fences and checkpoints
 "sovereignty over the islands as the means",        # 18 uninhabited chain
 "comparable wealth",                                # 19 NOT neocolonialism
 "protect a cultural meaning",                       # 20 historic landscape
 "position along the river",                         # 21 upstream dams
 "three-quarters of its export earnings",            # 22 78% share
 "convert control of a choke point",                 # 23 right of transit
 "from the local to the national scale",             # 24 garden, corner, border
 "expropriates farmland",                            # 25 control over land
 "a payment cannot replace",                         # 26 sacred mountain
 "an economic relationship; shatterbelt",            # 27 the three illustrations
 "passage or route on which many other states depend",  # 28 position multiplies power
 "exceeding the next highest by 5",                  # 29 7 - 2
 "influence over global flows of trade",             # 30 scale mismatch
]


def q11_choke_point(table):
    """Narrow AND high-traffic: the row with the largest share, checked to be
    among the two narrowest, is the choke point the key names."""
    rows = [(r[0], int(r[1]), int(r[2].rstrip("%"))) for r in table["rows"]]
    busiest = max(rows, key=lambda r: r[2])
    narrowest_two = sorted(rows, key=lambda r: r[1])[:2]
    assert busiest in narrowest_two, "the busiest passage is not among the narrowest"
    return busiest[0]


def q29_margin(table):
    """Boundary changes of the most-contested region minus the next highest."""
    rows = [(r[0], int(r[1]), int(r[2])) for r in table["rows"]]
    contested = max(rows, key=lambda r: (r[1], r[2]))
    others = sorted((r[2] for r in rows if r[0] != contested[0]), reverse=True)
    return f"exceeding the next highest by {contested[2] - others[0]}"


TABLE_NOTES = {
    11: q11_choke_point,
    # Item 22 compares four given percentages; the key names the largest and no
    # quantity is derived from the others.
    22: "no arithmetic claim",
    29: q29_margin,
}

geo_check.check(g4_3, ANCHORS, TABLE_NOTES)
