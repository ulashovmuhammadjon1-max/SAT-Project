"""Key audit for AP WORLD HISTORY: MODERN 4.4 Maritime Empires Established.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code, for a human
to audit. `wh_check` refuses any claim or `why` citing neither a KC code nor a
Learning Objective.

EVERYTHING SHARED IS SHARED. `wh_check.run` supplies the structural gate
(`cg_check.check`), the notation gate (`es_check.style`), the citation rule, the
figure-language ban, and a self-test that rotates all thirty keys, breaks all
thirty anchors, corrupts every cell of every table and asserts WHICH message came
back each time. `wh_stimulus` supplies the marked-stimulus gate.

THIS IS THE LARGEST TOPIC IN THE UNIT -- three learning objectives, three
thematic focuses and seven key concepts -- and its content risk is that two
different states can respond to the SAME development in opposite ways and the
framework records both. KC-4.3.II.A.i has some Asian states adopting restrictive
or isolationist policies to limit European-dominated long-distance trade;
KC-4.3.II.A.ii has African states whose participation in the very same expanding
networks increased their influence. Ming China and Tokugawa Japan belong to the
first, the Asante and the Kingdom of the Kongo to the second, and every one of
those four names is a plausible answer to the other question. q20 is built out of
that exchange and its anchor carries both halves.

THE OTHER RISK IS THE WORD "FLOURISH". KC-4.3.II.A.iii says that DESPITE some
disruption and restructuring due to the arrival of Portuguese, Spanish, and Dutch
merchants, the existing Indian Ocean networks continued to flourish and included
intra-Asian trade and Asian merchants. Both halves are asserted in one sentence.
A key that made the arrival destroy the networks, or that made it change nothing,
each drops a half; q10, q21 and q24 are built to hold the two together, and q21's
anchor names the ENDING as against the disruption, because the true statement is
itself one of its distractors.

WHAT NO ITEM ASSERTS. The framework gives no date for any policy, post or
empire, names no ruler, and does not rank the maritime empires by size or by
date -- q29 keys exactly that ranking as the claim needing an outside source. It
does not say enslavement in Africa ended or was replaced: KC-4.2.II.B says it
CONTINUED in its traditional forms, and q17 and q18 key the continuity and its
named destinations rather than a substitution.

NEGATIVE CONTROL: `python3 verify_w4_4.py --selftest`.
"""
import sys

import cg_check as cg
import wh_check as wh
import wh_stimulus as ws

import w4_4

EARLY = "Voyages recorded in an early year"
LATER = "Voyages recorded in a later year"
RECORD = "What the account records about it"
LAND = "Land under plantation crops (units)"
LABORERS = "Enslaved laborers recorded on the estates"


def q24(table, item):
    """Every Asian group sails more in the later year; the Europeans are new to it."""
    groups = cg.labels(table)
    early = dict(zip(groups, cg.col(table, EARLY)))
    later = dict(zip(groups, cg.col(table, LATER)))
    asian = [g for g in groups if "European" not in g]
    european = [g for g in groups if "European" in g]
    assert len(asian) == 3 and len(european) == 1, \
        f"the register must hold three Asian groups and one European; got {groups}"
    for g in asian:
        assert later[g] > early[g], (
            f"the key needs every Asian group to record more voyages later; {g} went "
            f"from {early[g]} to {later[g]}")
    for g in european:
        assert early[g] == 0 and later[g] > 0, (
            f"the European group must be absent early and present later; got "
            f"{early[g]} then {later[g]}")
    # and every distractor false on the same figures
    assert not any(later[g] < early[g] for g in asian), \
        "'the Asian groups recorded fewer voyages later' must be false"
    assert len([g for g in asian if g in later]) == 3, \
        "'only one Asian group appears in the later year' must be false"
    assert len(set(later[g] for g in groups)) > 1, \
        "'the four groups recorded the same number as one another' must be false"
    return (f"the three Asian groups rise from {[early[g] for g in asian]} to "
            f"{[later[g] for g in asian]} while the European group enters the register at "
            f"{later[european[0]]:.0f} from nothing")


def q25(table, item):
    """One listed labor system pre-dates the colonial economy and three do not."""
    systems = cg.labels(table)
    assert len(systems) == 4 and len(set(systems)) == 4, \
        f"the account must list four distinct labor systems; got {systems}"
    # Each cell is PARSED to one of the two classes rather than searched for a
    # substring, so a corrupted cell no longer falls into either and the check
    # fails instead of quietly passing. That is the lesson q19 of 4.3 taught.
    existing, introduced = [], []
    for row in table["rows"]:
        note = cg.normalize(row[1])
        if note == "in use in the region before the colonial economy was built":
            existing.append(row[0])
        elif note == "introduced with the colonial economy":
            introduced.append(row[0])
        else:
            raise AssertionError(
                f"the note {note!r} classes {row[0]!r} as neither existing nor introduced")
    assert len(existing) == 1, f"the key needs exactly one existing system; got {existing}"
    assert len(introduced) == 3, f"the key needs exactly three introduced; got {introduced}"
    assert "mit'a" in cg.normalize(existing[0]), (
        f"KC-4.2.II.D names the Incan mit'a as the existing system, and the account's "
        f"existing row is {existing[0]!r}")
    return (f"one row, {existing[0]}, is recorded as already in use in the region, and the "
            f"other three, {introduced}, as introduced with the colonial economy")


def q26(table, item):
    """Land under plantation crops and enslaved laborers rise together, every decade."""
    land, laborers = cg.col(table, LAND), cg.col(table, LABORERS)
    assert all(land[i + 1] > land[i] for i in range(len(land) - 1)), \
        f"the land under plantation crops must rise at every step; got {land}"
    assert all(laborers[i + 1] > laborers[i] for i in range(len(laborers) - 1)), \
        f"the number of enslaved laborers must rise at every step; got {laborers}"
    # and every distractor false on the same numbers
    assert not any(laborers[i + 1] < laborers[i] for i in range(len(laborers) - 1)), \
        "'the number of enslaved laborers falls' must be false"
    assert not any(land[i + 1] < land[i] for i in range(len(land) - 1)), \
        "'the land under plantation crops falls' must be false"
    assert len(set(land)) > 1 and len(set(laborers)) > 1, \
        "'neither figure changes' must be false"
    return (f"the land under plantation crops reads {land} and the enslaved laborers "
            f"{laborers}, both strictly increasing across the four decades")


CLAIMS = [
 ("In Africa and Asia",
  "KC-4.3.II.A.i states that Europeans established new trading posts in Africa and Asia, which proved profitable for the rulers and merchants involved in new global trade networks. The framework places these posts in no other region."),
 ("rulers and merchants involved in new global trade networks",
  "KC-4.3.II.A.i says the new trading posts proved profitable for the rulers and merchants involved in new global trade networks, and attributes that profit to no other group. Enslaved laborers, peasants, soldiers and pilgrims appear in other statements of the unit."),
 ("disruptive economic and cultural effects of European-dominated long-distance trade",
  "KC-4.3.II.A.i says some Asian states sought to limit the disruptive economic and cultural effects of European-dominated long-distance trade. Gunpowder, pilgrimage, agriculture and tribute belong to KC-4.3.II, KC-4.1.VI, KC-4.2.II.A and KC-4.3.I.D."),
 ("Restrictive or isolationist trade policies",
  "KC-4.3.II.A.i names restrictive or isolationist trade policies as what some Asian states adopted in response to European-dominated long-distance trade. Joint-stock companies belong to European rulers and merchants at KC-4.1.IV.C, and the framework records no free trade treaty or transferred port in this topic."),
 ("Ming China and Tokugawa Japan",
  "The illustrative examples beside Unit 4: Learning Objective E print Ming China and Tokugawa Japan under the heading of Asian states that adopted restrictive or isolationist trade policies, which is KC-4.3.II.A.i's second half. The Asante and the Kongo are KC-4.3.II.A.ii's African states."),
 ("Political, religious, and economic rivalries",
  "KC-4.3.II.C says that, driven largely by political, religious, and economic rivalries, European states established new maritime empires. Rivalry is the framework's own word, so an agreement or a common mission among those states contradicts the sentence rather than supplementing it."),
 ("Portuguese, Spanish, Dutch, French, and British",
  "KC-4.3.II.C names the Portuguese, Spanish, Dutch, French, and British maritime empires. The four land empires of KC-4.3.II.B and the African states of KC-4.3.II.A.ii are named elsewhere and are not among them."),
 ("Asante and the Kingdom of the Kongo, in Africa",
  "KC-4.3.II.A.ii states that the expansion of maritime trading networks fostered the growth of states in Africa, including the Asante and the Kingdom of the Kongo. Ming China and Tokugawa Japan are KC-4.3.II.A.i's restricting states, which is the opposite response to the same networks."),
 ("increase in their influence",
  "KC-4.3.II.A.ii says the participation of these African states in trading networks led to an increase in their influence. The framework records no loss of independence, closure of ports or absorption for either state."),
 # Both clauses: the sentence asserts the disruption AND the flourishing, and an
 # anchor naming only one of them matches a distractor that drops the other.
 ("continued to flourish, despite some disruption and restructuring",
  "KC-4.3.II.A.iii says that despite some disruption and restructuring due to the arrival of Portuguese, Spanish, and Dutch merchants, existing trade networks in the Indian Ocean continued to flourish. The collapse reading and the no-effect reading each drop one half of that one sentence."),
 ("Portuguese, Spanish, and Dutch merchants",
  "KC-4.3.II.A.iii names the arrival of Portuguese, Spanish, and Dutch merchants as the source of some disruption and restructuring in the Indian Ocean. The English and French appear among KC-4.3.II.C's maritime empires but not in this sentence."),
 ("Intra-Asian trade and Asian merchants",
  "KC-4.3.II.A.iii says the surviving Indian Ocean networks continued to flourish and included intra-Asian trade and Asian merchants. Each rejected option removes the Asian participation the sentence exists to assert."),
 ("Swahili Arabs, Omanis, Gujaratis, and Javanese",
  "The illustrative examples for this topic print Swahili Arabs, Omanis, Gujaratis and Javanese under the heading of Indian Ocean Asian merchants, which is what KC-4.3.II.A.iii means by intra-Asian trade and Asian merchants."),
 ("Agriculture",
  "KC-4.2.II.D states that newly developed colonial economies in the Americas largely depended on agriculture. Silver appears at KC-4.1.IV as part of the global circulation of goods rather than as the base of those economies."),
 ("Incan mit'a",
  "KC-4.2.II.D says the colonial economies utilized existing labor systems, including the Incan mit'a, and introduced new labor systems including chattel slavery, indentured servitude, and encomienda and hacienda systems. The four rejected options are all on the introduced side of that sentence."),
 ("Chattel slavery, indentured servitude, and encomienda and hacienda systems",
  "KC-4.2.II.D names chattel slavery, indentured servitude, and encomienda and hacienda systems as introduced, against the Incan mit'a as an existing system utilized. Tribute and tax farming are KC-4.3.I.D, peasant and artisan labor KC-4.2.II.A, and household enslavement in Africa KC-4.2.II.B."),
 ("continued in its traditional forms",
  "KC-4.2.II.B states that enslavement in Africa continued in its traditional forms, including incorporation of enslaved persons into households and the export of enslaved persons to the Mediterranean and the Indian Ocean regions. Continuity is what the sentence asserts, so an ending, a beginning or a replacement each contradict it."),
 ("Mediterranean and the Indian Ocean regions",
  "KC-4.2.II.B names the Mediterranean and the Indian Ocean regions as where enslaved persons continued to be exported from Africa in the traditional forms of enslavement there. The Americas belong to KC-4.2.II.C's separate account of the plantation economy."),
 ("increased demand for enslaved labor in the Americas",
  "KC-4.2.II.C says the growth of the plantation economy increased the demand for enslaved labor in the Americas, leading to significant demographic, social, and cultural changes. Each rejected option contradicts that sentence or one of KC-4.2.II.D, KC-4.3.II.A.i and KC-4.3.II.A.iii."),
 # Both clauses: the distractor exchanges the Asian and the African responses,
 # and each half of the key names states that appear in the other option too.
 ("Ming China and Tokugawa Japan adopted restrictive policies, while the Asante and the Kingdom of the Kongo grew in influence",
  "KC-4.3.II.A.i's illustrative examples print Ming China and Tokugawa Japan as Asian states adopting restrictive or isolationist trade policies, while KC-4.3.II.A.ii names the Asante and the Kingdom of the Kongo as African states whose participation increased their influence. The rejected sortings exchange those responses or flatten them into one."),
 # Both clauses: the true statement 'caused some disruption and restructuring'
 # is itself a distractor, so the anchor must carry the ENDING as against it.
 ("ended the existing trade networks rather than disrupting and restructuring them",
  "KC-4.3.II.A.iii holds both halves in one sentence: despite some disruption and restructuring due to the arrival of Portuguese, Spanish, and Dutch merchants, the existing networks continued to flourish and included intra-Asian trade and Asian merchants. Replacing the disruption with an ending drops the flourishing; the other four options are that sentence in pieces."),
 ("proved profitable for the rulers and merchants involved",
  "KC-4.3.II.A.i says Europeans established new trading posts in Africa and Asia which proved profitable for the rulers and merchants involved in new global trade networks, and a post returning a profit shared with a local ruler is that statement in a document. The rejected options are KC-4.3.II.A.i's second half, KC-4.2.II.D, KC-4.2.II.B and KC-4.3.II.A.iii."),
 ("restrictive or isolationist trade policy adopted to limit the effects",
  "KC-4.3.II.A.i says some Asian states sought to limit the disruptive economic and cultural effects of European-dominated long-distance trade by adopting restrictive or isolationist trade policies, and capping foreign shipping at one port is such a policy. The rejected options are KC-4.3.II.A.i's first half, KC-4.3.II.A.ii, KC-4.2.II.D and KC-4.1.IV.C."),
 # Both clauses: the distractor keeps the European arrival and reverses the
 # Asian trend, which is the whole content of KC-4.3.II.A.iii.
 ("more voyages in the later year even as European merchants entered",
  "KC-4.3.II.A.iii says existing Indian Ocean trade networks continued to flourish and included intra-Asian trade and Asian merchants despite the arrival of European merchants. Recomputed in q24 above: all three Asian groups rise between the two years while the European group enters the register from nothing."),
 ("One of the listed systems was already in use in the region and three were introduced",
  "KC-4.2.II.D says the colonial economies utilized existing labor systems, including the Incan mit'a, and introduced new labor systems including chattel slavery, indentured servitude, and encomienda and hacienda systems. Recomputed in q25 above: exactly one row is classed as existing and it is the mit'a, and the other three are classed as introduced."),
 ("Both the land under plantation crops and the number of enslaved laborers rise",
  "KC-4.2.II.C says the growth of the plantation economy increased the demand for enslaved labor in the Americas. Recomputed in q26 above: both columns rise at every step across the four decades, so neither swapped reading and neither no-change reading holds."),
 ("written to justify the company's costs to those who financed it",
  "Suggested skill 2.A distinguishes a source's point of view, purpose, historical situation and audience, and the reason a document was produced is its purpose; KC-4.3.II.A.i supplies the situation, the profitability of the new trading posts in Africa and Asia. Length, material, surviving copies and the presence of figures are features of the object rather than statements of why it was made."),
 # Both clauses: the item is a continuity paired with a change, and each half
 # alone appears inside a rejected pairing.
 ("Indian Ocean trade networks continued to flourish, while European states established new maritime empires",
  "KC-4.3.II.A.iii supplies the continuity, existing Indian Ocean networks flourishing with intra-Asian trade and Asian merchants in them, and KC-4.3.II.C the change, European states establishing new maritime empires driven largely by political, religious, and economic rivalries. Each rejected pairing contradicts a statement of the framework."),
 ("larger than the others",
  "The four rejected statements are KC-4.3.II.C, KC-4.3.II.A.i, KC-4.3.II.A.ii and KC-4.2.II.D almost verbatim. KC-4.3.II.C lists the maritime empires without ranking them by size, date or importance, so a comparison of that kind would need a source outside the framework."),
 ("some Asian states answered with restrictive policies while African states such as the Asante gained influence",
  "The keyed sentence joins KC-4.3.II.C, KC-4.3.II.A.i, KC-4.3.II.A.ii, KC-4.3.II.A.iii and KC-4.2.II.D in turn. Each rejected version denies the empires, denies the profit, denies the restrictive policies, exchanges the African and Asian responses, or contradicts the agricultural base and the existing labor systems."),
]

TABLE_CHECKS = {24: q24, 25: q25, 26: q26}

if __name__ == "__main__" and "--selftest" in sys.argv:
    ws.controls(w4_4)

ws.marked_stimulus(w4_4)
wh.run(w4_4, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
