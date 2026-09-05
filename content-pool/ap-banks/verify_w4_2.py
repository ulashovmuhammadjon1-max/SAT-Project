"""Key audit for AP WORLD HISTORY: MODERN 4.2 Exploration: Causes and Events from 1450 to 1750.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code, for a human
to audit. `wh_check` refuses any claim or `why` citing neither a KC code nor a
Learning Objective.

EVERYTHING SHARED IS SHARED. `wh_check.run` supplies the structural gate
(`cg_check.check`), the notation gate (`es_check.style`), the citation rule, the
figure-language ban, and a self-test that rotates all thirty keys, breaks all
thirty anchors, corrupts every cell of every table and asserts WHICH message came
back each time. `wh_stimulus` supplies the marked-stimulus gate. Nothing here is
reimplemented.

THIS TOPIC'S CONTENT RISK IS THE MIS-ATTRIBUTION, and it is the reason six of
the anchors below carry two clauses. The framework hands three different things
to three different sponsors in three consecutive sentences:

  KC-4.1.III.A  Portuguese maritime technology  -> trade with Africa and Asia,
                and the construction of a global trading-post empire
  KC-4.1.III.B  Spanish sponsorship of the voyages of Columbus, across the
                Atlantic and Pacific -> a dramatic rise in European interest in
                transoceanic travel and trade
  KC-4.1.III.C  English, French, and Dutch sponsorship -> northern Atlantic
                crossings, often seeking alternative sailing routes to Asia

Every one of those attributions reads perfectly well attached to the wrong
sponsor, which is HISTORY_BRIEF.md's "right process, wrong region" defect in its
purest form. So wherever a distractor is the SWAP -- q9 exchanges the Portuguese
and Spanish outcomes, q10 moves the northern crossings to the Portuguese and
Spanish, q30 does both -- the anchor spans the whole relation and not one noun
of it, and the self-test's anchor-breaking pass confirms each one is doing work.

WHAT NO ITEM ASSERTS. The framework prints no illustrative examples beside this
topic at all, which is recorded in the module comment because it means every
concrete detail had to come from the four statements above or from an explicitly
hypothetical stimulus. It gives no date for any voyage, names no ruler, no
captain and no ship beyond the phrase "the voyages of Columbus", ranks no state's
exploration above another's, and says nothing about what any expedition found.
KC-4.1.III.C's "often with the goal of" is a statement about AIMS, and q22 is
built out of exactly that: nothing here keys whether the northern crossings
succeeded, because the framework does not say.

NEGATIVE CONTROL: `python3 verify_w4_2.py --selftest`.
"""
import sys

import cg_check as cg
import wh_check as wh
import wh_stimulus as ws

import w4_2

PAYER = "Who paid for the voyage"
WHERE = "Where the voyage was sent"
ROYAL = "Voyages beyond European waters with royal backing"
PRIVATE = "Voyages beyond European waters without royal backing"
PURPOSE = "Stated purpose recorded for it"


def q13(table, item):
    """Every ocean crossing in the register is royally paid for; the one that is not, is not."""
    labs = cg.labels(table)
    assert labs == ["Voyage 1", "Voyage 2", "Voyage 3", "Voyage 4"], \
        f"the four voyages the key speaks of are not the rows: {labs}"
    payers = [cg.normalize(r[1]) for r in table["rows"]]
    wheres = [cg.normalize(r[2]) for r in table["rows"]]
    # The item turns on a two-way split, so each cell must be one of the two
    # categories it distinguishes. This is also what defends the table cell by
    # cell: a corrupted payer or destination is no longer either category.
    for p in payers:
        assert p in ("a royal treasury", "a single merchant house"), \
            f"the payer {p!r} is neither of the two categories this item distinguishes"
    ocean = [("atlantic" in w) or ("africa" in w) or ("asia" in w) for w in wheres]
    inside = ["inside europe" in w for w in wheres]
    for w, o, i in zip(wheres, ocean, inside):
        assert o != i, f"the destination {w!r} is neither clearly an ocean crossing nor clearly not"
    royal = [p == "a royal treasury" for p in payers]
    assert sum(ocean) == 3 and sum(inside) == 1, \
        f"the register must hold three ocean crossings and one coastal run; got {ocean}"
    assert all(r for r, o in zip(royal, ocean) if o), \
        "the key needs every ocean crossing in the register to be royally paid for"
    assert not any(r for r, i in zip(royal, inside) if i), \
        "'the only royal voyage stayed within European waters' must be false"
    assert not all(royal), "'every voyage was paid for by a merchant house' must be false"
    assert len(set(wheres)) == len(wheres), \
        "'every voyage was sent in the same direction' must be false"
    return (f"three of the four rows cross an ocean and all three are paid from a royal "
            f"treasury, while the one coastal run inside Europe is paid by a merchant house")


def q14(table, item):
    """Royally backed voyages start as the smaller share and end as the larger one."""
    royal, private = cg.col(table, ROYAL), cg.col(table, PRIVATE)
    shares = [r / (r + p) for r, p in zip(royal, private)]
    assert all(shares[i + 1] > shares[i] for i in range(len(shares) - 1)), \
        f"the royally backed share must rise at every step; got {shares}"
    assert shares[0] < 0.5, f"the first decade must be a minority; got {shares[0]}"
    assert shares[-1] > 0.5, f"the last decade must be a majority; got {shares[-1]}"
    # and every distractor false on the same numbers
    assert not all(royal[i + 1] < royal[i] for i in range(len(royal) - 1)), \
        "'royally backed voyages fall in every decade' must be false"
    assert len(set(royal)) > 1 and len(set(private)) > 1, \
        "'neither column changes' must be false"
    assert all(r != p for r, p in zip(royal, private)), \
        "'the two columns are equal in every decade' must be false"
    return (f"royally backed voyages read {royal} against {private} without backing, so the "
            f"royal share runs {[round(s, 2) for s in shares]}, from a minority to a majority")


def q15(table, item):
    """Exactly one recorded purpose is the northern search for another route to Asia."""
    labs = cg.labels(table)
    assert labs == ["Expedition %d" % n for n in range(1, 5)], \
        f"the four expeditions the choices name are not the rows: {labs}"
    text = {r[0]: cg.normalize(r[1]) for r in table["rows"]}
    asia = [k for k, v in text.items() if "asia" in v]
    north = [k for k, v in text.items() if "northern" in v]
    assert len(asia) == 3, f"three of the four purposes must name Asia; got {asia}"
    assert north == ["Expedition 3"], \
        f"exactly one purpose must be the northern one, and it must be the third; got {north}"
    assert "asia" in text["Expedition 3"], \
        "the northern purpose must also be a search for a route to Asia"
    assert "africa" in text["Expedition 1"] and "west" in text["Expedition 2"], \
        "the two non-northern Asia purposes must be the routes already in use"
    assert "asia" not in text["Expedition 4"] and "northern" not in text["Expedition 4"], \
        ("the fourth purpose must concern neither Asia nor northern waters, so that the "
         "expedition it names is a real non-answer rather than a second candidate")
    return ("three of the four recorded purposes name Asia, and exactly one of those three "
            "seeks it through northern waters, while the fourth stays inside the sponsor's "
            "own kingdom")


CLAIMS = [
 ("state-supported transoceanic maritime exploration",
  "KC-4.1.III states that new state-supported transoceanic maritime exploration occurred in this period, so state support and ocean crossing together are what the framework identifies as new. It does not say voyaging was abandoned or that this was the first ocean crossing made by anyone."),
 ("States",
  "Unit 4: Learning Objective B asks students to describe the role of states in the expansion of maritime exploration from 1450 to 1750, and KC-4.1.III calls that exploration state-supported. The framework assigns the sponsorship of transoceanic exploration in this period to no other kind of body."),
 ("global trading-post empire",
  "KC-4.1.III.A says Portuguese development of maritime technology and navigational skills led to increased travel to and trade with Africa and Asia and resulted in the construction of a global trading-post empire. No interior settler empire, land empire, republican confederation or monastic network is attributed to it."),
 ("Africa and Asia",
  "KC-4.1.III.A names increased travel to and trade with Africa and Asia as what followed from Portuguese maritime technology and navigational skills. The transatlantic and transpacific voyaging belongs to KC-4.1.III.B, and the other regions listed appear in no statement of this topic."),
 ("dramatic increase in European interest",
  "KC-4.1.III.B says Spanish sponsorship of the voyages of Columbus and subsequent voyages across the Atlantic and Pacific dramatically increased European interest in transoceanic travel and trade. The trading-post empire distractor is KC-4.1.III.A's real outcome attached to the wrong sponsor."),
 ("Atlantic and the Pacific",
  "KC-4.1.III.B places the Spanish-sponsored voyages of Columbus and the voyages that followed across the Atlantic and Pacific. No other water is named in that sentence, and KC-4.1.III.C's northern crossings are Atlantic rather than Arctic in the framework's own wording."),
 ("English, French, and Dutch",
  "KC-4.1.III.C states that northern Atlantic crossings were undertaken under English, French, and Dutch sponsorship. Portuguese and Spanish sponsorship belong to KC-4.1.III.A and KC-4.1.III.B, and the land empires of KC-4.3.II.B are given no role in transoceanic sponsorship anywhere."),
 ("alternative sailing routes to Asia",
  "KC-4.1.III.C says the northern Atlantic crossings were undertaken often with the goal of finding alternative sailing routes to Asia. Plantations belong to KC-4.2.II.C, and the framework attaches none of the remaining purposes to any voyage in this topic."),
 # Both clauses: the distractor exchanges the two outcomes between the two
 # sponsors, and either half of the anchor would match it.
 ("Portuguese sponsorship with a global trading-post empire, and Spanish sponsorship with a sharp rise",
  "KC-4.1.III.A gives the global trading-post empire to Portuguese development of maritime technology, and KC-4.1.III.B gives the dramatic rise in European interest to Spanish sponsorship of the voyages of Columbus. The rejected pairings exchange those attributions or hand one of them to KC-4.1.III.C's English, French and Dutch sponsors."),
 # Both clauses: the true statement is itself one of the distractors, so an
 # anchor naming only the northern crossings would match both.
 ("under Portuguese and Spanish sponsorship rather than English",
  "KC-4.1.III.C assigns the northern Atlantic crossings to English, French, and Dutch sponsorship, so moving them to the Portuguese and Spanish is the error. The other four options are KC-4.1.III, KC-4.1.III.A, KC-4.1.III.B and KC-4.1.III.C almost verbatim."),
 ("State-supported transoceanic maritime exploration",
  "KC-4.1.III describes new state-supported transoceanic maritime exploration in this period, and a ruler paying from the treasury to send ships across an unfamiliar ocean is that development. The rejected options are KC-4.3.I.C, KC-4.3.II.A.i, KC-4.3.I.A and KC-4.2.II.A."),
 ("global trading-post empire",
  "KC-4.1.III.A names the construction of a global trading-post empire as the outcome of Portuguese maritime technology and navigational skills, and posts held for trade rather than settlement along distant coasts are what that phrase describes. The rejected options are KC-4.2.II.D, KC-4.3.II, KC-4.1.VI and KC-4.3.II.A.i."),
 ("crossed an ocean was paid for out of a royal treasury",
  "KC-4.1.III makes the exploration of this period state-supported. Recomputed in q13 above: the three rows that cross an ocean are all paid from a royal treasury, the one privately funded voyage stays on the European coast, and no two rows share a destination."),
 # Both clauses: the distractor swaps which column grows into the majority, and
 # 'royal backing grow from a minority' alone matches 'WITHOUT royal backing
 # grow from a minority' as a substring.
 ("with royal backing grow from a minority",
  "KC-4.1.III singles out state-supported exploration as what was new in this period. Recomputed in q14 above: the royally backed share rises at every step, opening below half and closing above it, so the reversed reading and the three no-change readings are all false."),
 ("another sailing route to Asia through northern waters",
  "KC-4.1.III.C says the northern Atlantic crossings were undertaken often with the goal of finding alternative sailing routes to Asia. Recomputed in q15 above: three recorded purposes name Asia and exactly one of those seeks it through northern waters, so the match is that one and not the routes already in use."),
 # Both clauses: the distractor keeps the first half and swaps the second.
 ("into Europe, and the state-supported ocean voyaging",
  "KC-4.1.II and KC-4.1.II.A have knowledge and technology spreading into Europe and producing the tools, ship designs and understanding of winds and currents that made transoceanic travel possible, and KC-4.1.III then reports the state-supported ocean voyaging of the period. Suggested skill 5.B asks for exactly that relation between two developments."),
 ("Increased travel to and trade with Africa and Asia",
  "KC-4.1.III.A gives increased travel to and trade with Africa and Asia as the outcome of Portuguese maritime technology, which is an economic effect in the framework's own words and is what Unit 4: Learning Objective C asks students to explain. Every rejected option asserts a contraction of trade the framework nowhere records."),
 ("governance concerns how governments exercise power",
  "The governance thematic focus printed with this topic says governments obtain, retain, and exercise power in different ways and for different purposes, and KC-4.1.III makes the exploration of the period state-supported. The rejected descriptions are the other four thematic focuses of the course."),
 ("better navigated than",
  "The four rejected statements are KC-4.1.III, KC-4.1.III.A, KC-4.1.III.B and KC-4.1.III.C almost verbatim. The framework compares no two states' expeditions for quality of navigation, so a claim of that kind would have to be defended from outside it."),
 ("depended on state support and was expected to bring commercial return",
  "KC-4.1.III describes the exploration of the period as state-supported and Unit 4: Learning Objective C asks for its economic causes and effects, which together are what the petition joins. Each rejected option removes either the state or the commercial motive those two statements supply."),
 ("treasuries paying to fit out voyages",
  "KC-4.1.III makes state support the distinguishing feature of the period's transoceanic exploration, so evidence for it has to connect a government's money to a voyage. Taverns, harvests, ferry fees and ships' names document other things and leave the claim untested."),
 ("often undertaken with the goal of finding alternative routes",
  "KC-4.1.III.C says the northern Atlantic crossings were undertaken under English, French, and Dutch sponsorship, often with the goal of finding alternative sailing routes to Asia. That is a statement about the aim of the voyages and none about the outcome, so both success and failure go beyond it."),
 ("one to trade with Africa and Asia and the other to a rise in European interest",
  "KC-4.1.III.A ties Portuguese maritime technology to increased travel to and trade with Africa and Asia, KC-4.1.III.B ties Spanish sponsorship of the voyages of Columbus to a dramatic rise in European interest in transoceanic travel and trade, and KC-4.1.III makes both state-supported. Each rejected comparison contradicts one of those sentences."),
 ("Opening of Ocean Routes",
  "KC-4.1.III makes the exploration of this period state-supported and transoceanic, which is what the keyed title states. Exploration without the state and a turn away from the sea contradict that sentence, an overland road contradicts KC-4.1.III.C's search for sailing routes, and KC-4.1.III.A to KC-4.1.III.C name several sponsors rather than one."),
 ("often made in search of another route to Asia",
  "KC-4.1.III.C says northern Atlantic crossings were undertaken often with the goal of finding alternative sailing routes to Asia, and a search for a westward passage along a cold northern coast is that search. The rejected options are KC-4.1.III.A, KC-4.1.III.B, KC-4.3.II.A.i and KC-4.2.II.D."),
 ("states then supported voyages across the oceans",
  "KC-4.1.II.A says new tools, innovations in ship designs, and an improved understanding of regional wind and currents patterns all made transoceanic travel and trade possible, and KC-4.1.III reports the new state-supported transoceanic exploration that followed. Suggested skill 5.B asks for exactly this kind of relation between two developments."),
 ("economic causes and effects of maritime exploration",
  "Unit 4: Learning Objective C asks students to explain the economic causes and effects of maritime exploration by the various European states, and KC-4.1.III.A and KC-4.1.III.B both give trade as an outcome. The rejected statements are KC-4.3.I.A, KC-4.3.II.B, KC-5.3.III.C and KC-4.2.II.A, none of which bears on the motive for a voyage."),
 ("not sea travel itself",
  "KC-4.1.III says new state-supported transoceanic maritime exploration occurred in this period, so what it calls new is the combination of state support with ocean crossing. The CED's own note that events and processes are not constrained by the given dates tells against reading the sentence as a claim that ocean travel began in 1450."),
 ("more ocean voyages fitted out year after year",
  "KC-4.1.III.B says Spanish sponsorship of the voyages of Columbus and subsequent voyages dramatically increased European interest in transoceanic travel and trade, and a claim about rising interest across Europe needs evidence spanning several states and several years. A wage, a harbour depth, a bolt of cloth and a birth date bear on none of it."),
 # Both clauses again: one rejected version exchanges the Portuguese and
 # Spanish attributions wholesale, so half the anchor would match it.
 ("Spanish sponsorship of transatlantic voyaging raised European interest sharply",
  "The keyed sentence joins KC-4.1.III, KC-4.1.III.A, KC-4.1.III.B and KC-4.1.III.C in the order the framework prints them. The rejected versions remove the state, deny the trade, exchange the Portuguese and Spanish attributions, or strip the northern crossings of the goal KC-4.1.III.C gives them."),
]

TABLE_CHECKS = {13: q13, 14: q14, 15: q15}

if __name__ == "__main__" and "--selftest" in sys.argv:
    ws.controls(w4_2)

ws.marked_stimulus(w4_2)
wh.run(w4_2, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
