"""Structural audit for AP HUMAN GEOGRAPHY 4.2 Political Processes.

Same gate as every other module in this bank: 30 questions, five distinct
choices, a key index in range, a `why` that is a reason rather than a stub, no
repeated stem, no choice contained token-for-token inside another, and the
arithmetic in each data item recomputed from its own table.

Grounding for the keys:
  PSO-4.B.1 -- sovereignty, nation-states, and self-determination shape the
  contemporary world. Items 1-3, 12, 21, 23 and 28 key to those three concepts
  and to nothing outside them.
  PSO-4.B.2 -- colonialism, imperialism, independence movements, and devolution
  along national lines have influenced contemporary political boundaries. Items
  4, 5, 7-10, 14-17, 20, 22, 25, 29 key to that list.

Neocolonialism (items 10, 22) is named in the CED at PSO-4.C.1 as an expression
of political power, not in this topic's own EK bullets; it is used here because
it is the process that connects PSO-4.B.2's colonialism to the present, and the
citation is recorded rather than implied.

Supranationalism (items 18, 19, 27, 30) belongs to SPS-4.B in Topic 4.9. It
appears here only as the counter-direction to devolution, because the pair is
what makes the scale argument legible; no item asks for a fact about a
particular supranational organization, which is 4.9's business.

Three items carry data tables. Two of them make an arithmetic claim -- a
difference of counts and a ratio of counts -- and both are recomputed below
from the table's own numbers, so a mistyped cell fails the module rather than
teaching a wrong figure.
"""
import geo_check
import g4_2


ANCHORS = [
 "sovereignty",                                   # 1  supreme internal authority
 "self-determination",                            # 2  right to choose status
 "vote to become an independent state",           # 3  referendum plus recognition
 "independence movements ending colonial rule",   # 4  decolonization
 "devolution along national lines",               # 5  Czechoslovakia, PSO-4.B.2
 "93 states",                                     # 6  144 - 51
 "devolution",                                    # 7  powers moved downward
 "leaving its government in place",               # 8  imperialism without settlement
 "cut across ethnic homelands",                   # 9  Berlin Conference legacy
 "neocolonialism",                                # 10 economic control after independence
 "armed groups the central government cannot dislodge",  # 11 nominal sovereignty
 "matched national homelands",                    # 12 nation-state ideal
 "short of secession",                            # 13 devolutionary demand
 "Imperialism is the broader process",            # 14 genus and species
 "invite competing claims",                       # 15 why borders are kept
 "devolution within a unitary state",             # 16 Scotland
 "ending administration by an outside power",     # 17 four transfers
 "limits the state's exercise of sovereignty",    # 18 supranational constraint
 "tends to increase it",                          # 19 opposite directions
 "expressed through a vote",                      # 20 South Sudan
 "leaving minorities on the wrong side",          # 21 intermixed settlement
 "inherited from the colonial period",            # 22 export dependence
 "claim part of it",                              # 23 sovereignty vs self-determination
 "foreign policy, defense, and international recognition",  # 24 secessionist test
 "empires were dismantled",                       # 25 1914 vs 2014
 "twelvefold",                                    # 26 48 / 4
 "to a supranational scale",                      # 27 customs union
 "who is sovereign",                              # 28 PSO-4.B.1 in practice
 "preserving the state's territorial integrity",  # 29 devolution as a response
 "cross freely",                                  # 30 borders unchanged, less salient
]


def q6_growth(table):
    """UN members in 1975 minus members in 1945: 144 - 51 = 93."""
    by_year = {row[0]: int(row[1]) for row in table["rows"]}
    return f"{by_year['1975'] - by_year['1945']} states"


def q26_largest_multiple(table):
    """Region with the biggest 2014-to-1914 ratio, named as a multiple word."""
    words = {1: "onefold", 2: "twofold", 3: "threefold", 4: "fourfold",
             12: "twelvefold"}
    best = max(table["rows"], key=lambda r: int(r[2]) / int(r[1]))
    ratio = int(best[2]) // int(best[1])
    assert int(best[2]) % int(best[1]) == 0, "ratio is not a whole multiple"
    return words[ratio]


TABLE_NOTES = {
    6: q6_growth,
    # Item 17 is a records table with no quantity in it: the key reads the shared
    # PROCESS off four rows of dates and administering powers.
    17: "no arithmetic claim",
    26: q26_largest_multiple,
}

geo_check.check(g4_2, ANCHORS, TABLE_NOTES)
