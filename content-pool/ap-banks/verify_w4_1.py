"""Key audit for AP WORLD HISTORY: MODERN 4.1 Technological Innovations from 1450 to 1750.

WHY THIS FILE EXISTS AT ALL. `w4_1.py` was authored by an agent that was stopped
before it wrote a verifier, so thirty questions sat in the tree with NO gate on
them -- not a weak gate, none. Every item below was re-read against the CED
before this file was written, and two stems were tightened where the trace from
stimulus to key ran through my own knowledge rather than through the framework:
q18's keyed context named the Mediterranean and the Indian Ocean, which the CED
does not say, and is now KC-4.1.II's own list of worlds; q19's inventory listed
"charts of distant coasts", which is not KC-4.1.II.A's "regional wind and
currents patterns", and now records the winds and currents of a route. Nothing
else was changed and no key moved.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. `claim` states what the key rests on, for a human to audit.

EVERYTHING SHARED IS SHARED. `wh_check.run` is the World History gate the rest
of this subject already uses: `cg_check.check` for structure and anchors,
`es_check.style` for notation, a required KC code or Learning Objective in every
`why` AND every `claim`, and a ban on figure language the bank cannot display --
which matters more in this unit than in any other, because a topic about ocean
routes invites a map on every second question. Its self-test rotates all thirty
keys, breaks all thirty anchors, corrupts every table cell and asserts WHICH
message came back each time. None of that is reimplemented here.

ONE GATE IS ADDED, because it is what this module needs and the shared gate does
not have. MARKED STIMULUS. Section I is stimulus-based and this module carries seven
invented sources. HISTORY_BRIEF.md forbids putting words in a real person's
mouth, so every stem that introduces a source document must say in the stem that
it is hypothetical, unattributed or illustrative. What the check can and cannot
do, stated plainly: it proves the LABEL is present, not that the label is
honest. A stem reading "a hypothetical letter of Zheng He" would pass it. That
one is left to the reading, and no stem here names any person at all.

WHAT THE KEYS REST ON
---------------------
Items 1, 3, 9, 14, 16, 18, 23 and 28 rest on KC-4.1.II: knowledge, scientific
learning, and technology from the Classical, Islamic, and Asian worlds spread,
facilitating European technological developments and innovation. Several of them
turn on the DIRECTION of that spread, and each such item's anchor carries both
clauses because the distractor is the exact reversal.

Items 2, 6, 7, 8, 10, 12, 13, 17, 19, 22, 24, 25, 27 and 30 rest on KC-4.1.II.A:
the developments included the production of new tools, innovations in ship
designs, and an improved understanding of regional wind and currents patterns,
all of which made transoceanic travel and trade possible.

Items 4, 5 and 11 rest on the illustrative examples printed beside Unit 4:
Learning Objective A, under their two headings -- caravel, carrack and fluyt
under innovations in ship design; lateen sail, compass and astronomical charts
under European technological developments influenced by cross-cultural
interactions with the Classical, Islamic, and Asian worlds.

Items 15 and 29 rest on Unit 4: Learning Objective A itself, and items 9 and 18
additionally on suggested skill 4.A. Items 20 and 21 rest on the Technology and
Innovation thematic focus. Item 26 reaches to KC-4.1.III and KC-4.1.IV.C, both
studied in this unit, and item 27 compares with KC-4.3.II from unit 3.

WHAT NO ITEM ASSERTS. The framework dates none of these devices, names no
inventor, explains how none of them worked, and ranks none above another -- item
22 is built out of exactly that last distinction. It nowhere says Europeans were
the only people navigating oceans, and no item implies it.

NEGATIVE CONTROL: `python3 verify_w4_1.py --selftest`.
"""
import sys

import cg_check as cg
import wh_check as wh
import wh_stimulus as ws

import w4_1

# The MARKED STIMULUS gate now lives in `wh_stimulus`, so the seven modules of
# this unit share one copy of it and one set of controls. It was written here
# first; the docstring above records why the indefinite article is in it.


# ------------------------------------------------------------ table recomputes

ITEM = "Item named in the framework"
HEADING = "Heading it is printed under"
ATTEMPTED = "Crossings attempted"
COMPLETED = "Crossings completed"

# The framework's own illustrative examples for this topic, under the two
# headings it prints them beneath. Nothing else may appear in q11's table.
SHIP_DESIGN = {"caravel", "carrack", "fluyt"}
INFLUENCED = {"lateen sail", "compass", "astronomical charts"}


def q11(table, item):
    names = [cg.normalize(r[0]) for r in table["rows"]]
    headings = [cg.normalize(r[1]) for r in table["rows"]]
    for name in names:
        assert name in SHIP_DESIGN | INFLUENCED, (
            f"{name!r} is not one of the framework's illustrative examples for this topic"
        )
    ships = [n for n, h in zip(names, headings) if "ship design" in h]
    cross = [n for n, h in zip(names, headings) if "cross-cultural" in h]
    assert len(ships) == 2 and len(cross) == 2, (
        f"the key says two of each; the table gives {len(ships)} ship designs and "
        f"{len(cross)} cross-cultural developments"
    )
    assert len(ships) + len(cross) == len(names), \
        "every row must sit under one of the two headings the framework prints"
    assert set(ships) <= SHIP_DESIGN, \
        f"{sorted(set(ships) - SHIP_DESIGN)} is not printed under innovations in ship design"
    assert set(cross) <= INFLUENCED, \
        f"{sorted(set(cross) - INFLUENCED)} is not printed under the cross-cultural heading"
    assert len(set(headings)) == 2, \
        "'the four items are printed under four different headings' must be false"
    return (f"the four rows are {names}, splitting two under innovations in ship design and "
            f"two under European developments influenced by cross-cultural interactions")


def q12(table, item):
    attempted = cg.col(table, ATTEMPTED)
    completed = cg.col(table, COMPLETED)
    assert all(a > 0 for a in attempted), "a period with no attempts has no share to compute"
    shares = [c / a for c, a in zip(completed, attempted)]
    assert all(attempted[i + 1] > attempted[i] for i in range(len(attempted) - 1)), \
        f"crossings attempted must rise at every step; got {attempted}"
    assert all(shares[i + 1] > shares[i] for i in range(len(shares) - 1)), \
        f"the completed share must rise at every step; got {shares}"
    assert all(c < a for c, a in zip(completed, attempted)), \
        "'every crossing attempted was completed' must be false in every period"
    return (f"crossings attempted read {attempted} and the completed shares "
            f"{[round(s, 2) for s in shares]}, both strictly rising, and no period completed "
            "every crossing it attempted")


def q13(table, item):
    text = {r[0]: cg.normalize(r[1]) for r in table["rows"]}
    assert len(text) == len(table["rows"]), "each development must have its own row label"
    first, second = text["Development 1"], text["Development 2"]
    third, fourth = text["Development 3"], text["Development 4"]
    # One row for each of KC-4.1.II.A's three named developments, and one that is
    # none of them. 'winds and currents' rather than 'wind', because the second
    # row legitimately says 'closer to the wind' and a bare substring would call
    # it the third development too -- the under/over-matching own-goal.
    assert "tool" in first, "the first row must describe the production of a new tool"
    assert "winds and currents" not in first and "hull" not in first, \
        "the first row must be a tool and nothing else"
    assert "hull" in second and "rig" in second, \
        "the second row must describe an innovation in ship design"
    assert "tool" not in second and "winds and currents" not in second, \
        "the second row must be a ship design and nothing else"
    assert "winds and currents" in third, \
        "the third row must describe an understanding of regional winds and currents"
    assert "tool" not in third and "hull" not in third, \
        "the third row must be the wind and currents understanding and nothing else"
    for word in ("tool", "hull", "rig", "wind", "current", "ship", "sail"):
        assert word not in fourth, (
            f"the fourth row must fall outside the framework's three developments, "
            f"but it mentions {word!r}"
        )
    return ("the first three rows are a new tool, a ship design and an understanding of a "
            "region's winds and currents, one for each development KC-4.1.II.A names, while "
            "the fourth is a roofing tile and is none of them")


CLAIMS = [
 ("Classical, Islamic, and Asian worlds",
  "KC-4.1.II names the Classical, Islamic, and Asian worlds as the worlds from which knowledge, scientific learning, and technology spread, facilitating European technological developments and innovation. The framework names no other set of sources for this diffusion anywhere in the unit."),
 ("innovations in ship designs, and an improved understanding",
  "KC-4.1.II.A names the production of new tools, innovations in ship designs, and an improved understanding of regional wind and currents patterns, and says all of them made transoceanic travel and trade possible. The rejected lists are KC-4.3.II on expansion, KC-4.3.I.D on revenue and KC-4.2.II.D on labor systems."),
 # Both clauses: the distractor reverses the direction of the spread, and either
 # half alone ('technology spread') matches the reversal just as well.
 ("from other worlds spread and facilitated those European developments",
  "KC-4.1.II has knowledge, scientific learning, and technology from the Classical, Islamic, and Asian worlds spreading and facilitating European developments, so isolation is what the framework denies and the reversed direction is what it does not say."),
 ("caravel",
  "The illustrative examples printed beside Unit 4: Learning Objective A give the caravel, the carrack and the fluyt under innovations in ship design, while the compass and astronomical charts sit under the separate cross-cultural heading. Joint-stock companies are KC-4.1.IV.C and the encomienda KC-4.2.II.D."),
 ("European developments influenced by cross-cultural interactions",
  "The heading printed above the lateen sail, the compass and astronomical charts reads: European technological developments influenced by cross-cultural interactions with the Classical, Islamic, and Asian worlds, which is KC-4.1.II in the illustrative examples' own words. The rejected descriptions belong to KC-4.2.II.D, KC-4.3.I.A, KC-4.3.II.A.i and KC-4.1.V.A."),
 ("innovation in ship design",
  "KC-4.1.II.A names innovations in ship designs among the three developments that made transoceanic travel and trade possible, and a hull and rig that hold a course closer to the wind are that. The rejected terms belong to KC-4.3.I.D, KC-4.1.VI, KC-4.3.II.A.i and KC-4.2.II.D."),
 ("improved understanding of regional wind and currents",
  "KC-4.1.II.A names an improved understanding of regional wind and currents patterns as one of the three developments, and a seasonal record of the winds and currents of one route is that understanding written down. New tools and ship designs are the other two items in the same sentence."),
 ("Transoceanic travel and trade",
  "KC-4.1.II.A ends by saying that new tools, innovations in ship designs, and an improved understanding of regional wind and currents patterns all made transoceanic travel and trade possible. KC-4.2.II.C, KC-4.1.VI, KC-4.3.III.i and KC-4.1.IV each contradict one of the rejected options."),
 ("spread of knowledge and technology from the Classical",
  "Suggested skill 4.A asks a student to identify and describe a historical context for a specific development, and KC-4.1.II supplies exactly that context for European navigation. A single year's rainfall, a headcount, a paint colour and a ship's name are details rather than contexts."),
 ("made transoceanic travel and trade possible",
  "KC-4.1.II.A states in its own words that these developments made transoceanic travel and trade possible, which is a causal link the framework asserts rather than one a student supplies. Each rejected option denies or reverses that link."),
 # Both clauses: two distractors say ALL FOUR items fall under one heading, and
 # either half of the key matches one of them.
 ("ship designs and two are developments influenced by cross-cultural interaction",
  "The framework prints the caravel, carrack and fluyt under innovations in ship design and the lateen sail, compass and astronomical charts under European developments influenced by cross-cultural interactions, which is the split KC-4.1.II and KC-4.1.II.A describe. Recomputed in q11 above: two rows fall under each heading and no row falls outside them."),
 # Both clauses: the two swap distractors move one column up and the other down.
 ("crossings attempted and the share completed rose",
  "KC-4.1.II.A ties an improved understanding of regional wind and currents patterns to making transoceanic travel and trade possible. Recomputed in q12 above: attempts rise across the three periods, the completed share rises with them, and no period completed every crossing attempted."),
 ("first three developments only",
  "KC-4.1.II.A names the production of new tools, innovations in ship designs, and an improved understanding of regional wind and currents patterns. Recomputed in q13 above: the first three rows are one of each and the roofing tile is none of them."),
 ("follows methods set out in earlier works from another world",
  "KC-4.1.II claims that knowledge, scientific learning, and technology from the Classical, Islamic, and Asian worlds spread and facilitated European developments, so evidence for it must show a European work depending on earlier learning from elsewhere. Ship counts, crew lists, timber tallies and weather reports show no such dependence."),
 ("technological developments changed patterns of trade and travel",
  "Unit 4: Learning Objective A asks how cross-cultural interactions resulted in the diffusion of technology and facilitated changes in patterns of trade and travel, and KC-4.1.II.A says the resulting developments made transoceanic travel and trade possible. KC-4.1.IV has regional markets continuing to flourish, which one rejected option denies."),
 # Both clauses: the distractor is the exact reversal of the diffusion, which is
 # the single easiest wrong key to ship in this topic.
 ("Classical, Islamic, and Asian worlds spread and facilitated European innovation",
  "KC-4.1.II gives the direction explicitly: knowledge, scientific learning, and technology FROM those worlds spread, facilitating European technological developments and innovation. The reversal reads just as well and is not what the sentence says."),
 ("beside new tools and ship designs",
  "KC-4.1.II.A places an improved understanding of regional wind and currents patterns in one list with new tools and innovations in ship designs and says all of them made ocean travel and trade possible. Each rejected option contradicts part of that same sentence."),
 ("long exchange of technical knowledge",
  "Suggested skill 4.A asks for a historical context for a specific development, and KC-4.1.II supplies one in the framework's own terms: the spread of knowledge, scientific learning, and technology from the Classical, Islamic, and Asian worlds. A launch date, a nail count, one owner's taste and a modern museum are not contexts."),
 # Both clauses: a distractor keeps the first half ('the production of new
 # tools') and swaps the second, so half the anchor would match it.
 ("new tools, and an improved understanding of regional wind",
  "KC-4.1.II.A names new tools and an improved understanding of regional wind and currents patterns among its three developments; instruments for taking bearings are tools and a chart of a route's winds and currents is that understanding. Plantations are KC-4.2.II.C, syncretism KC-4.1.VI, companies KC-4.1.IV.C and officials KC-4.3.I.C."),
 ("human adaptation and innovation",
  "The Technology and Innovation thematic focus printed with this topic says human adaptation and innovation have resulted in increased efficiency, comfort, and security and that technological advances have shaped human development, which is why KC-4.1.II and KC-4.1.II.A sit under it rather than under governance. The rejected descriptions are the Governance, Social Interactions, Humans and the Environment and Cultural Developments thematic focuses."),
 ("both intended and unintended consequences",
  "The same Technology and Innovation thematic focus says technological advances have shaped human development and interactions with both intended and unintended consequences, which is what licenses treating unintended consequences as part of the subject. The rejected statements are KC-4.3.I.A, KC-4.3.II.B, KC-4.2.II.A and KC-5.3.III.C."),
 ("one list of developments the framework does not rank",
  "KC-4.1.II.A names new tools and innovations in ship designs in a single list and says all of the listed developments made transoceanic travel and trade possible, without ordering them. Asserting a rank in either direction goes beyond what the sentence says, which is the point of the item."),
 ("from other worlds facilitated European technological developments",
  "KC-4.1.II states that scientific learning from the Classical, Islamic, and Asian worlds spread, facilitating European technological developments and innovation, and adapting star tables compiled elsewhere is that facilitation. The illustrative examples name astronomical charts among the developments so influenced."),
 ("faster than every other",
  "The four rejected statements are KC-4.1.II and KC-4.1.II.A almost verbatim. The framework compares no two vessel designs for speed and dates, ranks and describes none of these devices, so a claim about speed would have to be defended from outside it."),
 ("built up from accumulated observation",
  "KC-4.1.II.A speaks of an IMPROVED understanding of regional wind and currents patterns, which is a process rather than a starting condition, and collecting pilots' observations is how such an improvement accumulates. The word regional in the same phrase tells against treating every ocean as identical."),
 ("credits state sponsorship of exploration",
  "KC-4.1.III says new state-supported transoceanic maritime exploration occurred in this period and KC-4.1.IV.C adds mercantilist policies and joint-stock companies used by rulers, so technology sits alongside state action in the framework's account. Each rejected option denies something the unit states outright."),
 ("one to expansion and one to ocean travel",
  "KC-4.3.II connects gunpowder, cannons, and armed trade to imperial expansion, while KC-4.1.II.A connects new tools, ship designs and knowledge of winds and currents to transoceanic travel and trade. Each rejected option contradicts one or both of those statements."),
 ("spread of knowledge that facilitated further developments",
  "KC-4.1.II has knowledge, scientific learning, and technology spreading and facilitating European technological developments and innovation, and KC-4.1.II.A then lists developments that followed, so the framework describes a process rather than a single event."),
 ("routes sailed before and after",
  "Unit 4: Learning Objective A asks how the diffusion of technology facilitated changes in patterns of trade and travel, so evidence for it has to compare travel before and after those developments came into use. Taverns, bread prices, spires and enrolments bear on none of that."),
 ("new tools, better ships, and a fuller grasp of winds and currents",
  "The keyed sentence joins KC-4.1.II on the spread of knowledge, scientific learning, and technology to KC-4.1.II.A on new tools, innovations in ship designs, and an improved understanding of regional wind and currents patterns making transoceanic travel and trade possible. Each rejected version contradicts one of those two statements."),
]

TABLE_CHECKS = {11: q11, 12: q12, 13: q13}

if __name__ == "__main__" and "--selftest" in sys.argv:
    ws.controls(w4_1)

ws.marked_stimulus(w4_1)
wh.run(w4_1, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
