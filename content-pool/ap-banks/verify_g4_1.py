"""Structural audit for AP HUMAN GEOGRAPHY 4.1 Introduction to Political Geography.

It cannot check the geography. What it checks is everything a machine can:
30 questions, five distinct choices apiece, a key index in range, a `why` that is
a sentence rather than a stub, no repeated stem, no choice whose whole token run
sits inside another choice's, and -- for the three data items -- the arithmetic
recomputed from the table that ships with the question.

ANCHORS pins each key to its TEXT. export_units.py reshuffles the choices on the
way out, so a key stored as an index alone is one careless edit away from
pointing at a distractor; if the anchor stops appearing in the keyed choice, or
starts appearing in a second one, this file fails.

Grounding for the keys, stated once so a human can audit it:
  PSO-4.A.1 makes independent states the primary building blocks of the world
  political map (items 1, 20, 22).
  PSO-4.A.2 gives the closed six-item list of entity types -- nations,
  nation-states, stateless nations, multinational states, multistate nations,
  and autonomous and semiautonomous regions such as Native American reservations
  -- and every classification item here keys to a member of that list.

The four statehood criteria used throughout (defined territory, permanent
population, effective government, recognized sovereignty) are the content of the
word "independent" in PSO-4.A.1; the framework names independent states without
unpacking the adjective, so items 1, 10, 11, 14, 17 and 25 are keyed to the
criteria as ordinarily stated in the course, not to a sentence quoted from the
CED. That distinction is recorded here rather than glossed over: an EK citation
on those items would be inventing one.

The recurring distractor in this module is cultural evidence offered where
political evidence is required (items 8, 13, 17). It is the error the topic
actually produces, because "nation" in ordinary English means "country".
"""
import geo_check
import g4_1


ANCHORS = [
 "an independent state",                     # 1  four criteria satisfied
 "a stateless nation",                       # 2  Kurds
 "a nation-state",                           # 3  Iceland
 "a multinational state",                    # 4  Russia
 "a multistate nation",                      # 5  Koreans
 "national government controls its foreign policy",   # 6  autonomy test
 "an autonomous or semiautonomous region",   # 7  reservations, PSO-4.A.2
 "no government recognized as sovereign",    # 8  nation not state
 "one sovereign government ruling several distinct peoples",  # 9  pairing
 "sovereignty does not depend on area",      # 10 Vatican City
 "lacks a permanent population",             # 11 Antarctica
 "45 percent",                               # 12 18.0 of 40.0
 "no bearing on statehood",                  # 13 diversity is not the test
 "without another state's permission",       # 14 effective control
 "devolved power to its regions",            # 15 Belgium
 "Japan approaches a nation-state",          # 16 Japan vs Nigeria
 "shared culture and history",               # 17 weakest evidence
 "lack a fully sovereign state",             # 18 Palestinians, Basques
 "regional autonomy within a single sovereign state",  # 19 devolved powers
 "Colonies in Africa and Asia gained independence",    # 20 decolonization
 "no group is close to a majority",          # 21 29% share
 "The independent state",                    # 22 PSO-4.A.1 verbatim
 "a semiautonomous region of a sovereign state",       # 23 Hong Kong
 "need not have the same territory",         # 24 nation vs state
 "Recognized sovereignty over a defined territory",    # 25 contested claim
 "an autonomous region rather than an independent state",  # 26 Greenland
 "joined",                                   # 27 irredentist pressure
 "conducts its own foreign policy",          # 28 Entity P
 "Achieving recognized sovereignty",         # 29 stateless -> nation-state
 "The global scale",                         # 30 scale of analysis
]


def q12_largest_share(table):
    """18.0 of the four listed groups' 40.0 million total = 45 percent."""
    pops = [float(row[1]) for row in table["rows"]]
    return f"{round(100 * max(pops) / sum(pops))} percent"


TABLE_NOTES = {
    12: q12_largest_share,
    # Item 21 keys to a pattern reading -- which state's largest group leaves the
    # most population to other groups -- not to a computed quantity. The shares
    # are given directly and nothing is summed.
    21: "no arithmetic claim",
    # Item 28 reads a yes/no matrix of powers; there is no number in it.
    28: "no arithmetic claim",
}

geo_check.check(g4_1, ANCHORS, TABLE_NOTES)
