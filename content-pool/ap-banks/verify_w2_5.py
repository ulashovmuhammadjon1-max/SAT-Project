"""Key audit for AP WORLD HISTORY: MODERN 2.5 (Unit 2, cultural consequences).

One (anchor, claim) per question, in module order. The anchor is a distinctive
substring of that question's OWN keyed choice and of no distractor; the claim
states the CED sentence the key rests on, with its Key Concept or Learning
Objective code.

WHAT THE KEYS REST ON
---------------------
  LO 2.J          the intellectual and cultural effects of the various networks
                  of exchange in Afro-Eurasia from c. 1200 to c. 1450
  skill 2.A       identify a source's POINT OF VIEW, PURPOSE, HISTORICAL
                  SITUATION, AND/OR AUDIENCE
  KC-3.1.III.D    increased cross-cultural interactions RESULTED IN the
                  diffusion of literary, artistic, and cultural traditions, as
                  well as scientific and technological innovations
  KC-3.3.II       the fate of cities VARIED GREATLY, with periods of significant
                  decline and periods of increased urbanization, buoyed by
                  rising productivity and expanding trade networks
  KC-3.1.III.C    AS exchange networks intensified, an increasing number of
                  travelers within Afro-Eurasia wrote about their travels
  the CDI thematic focus paragraph

THE RULE THAT GOVERNED THIS MODULE MORE THAN ANY OTHER
--------------------------------------------------------
This topic page names three real travel writers -- Ibn Battuta, Margery Kempe,
Marco Polo -- as illustrative examples, and its skill is sourcing. The obvious
item to write is a quotation attributed to one of them, and it is exactly what
HISTORY_BRIEF.md forbids: the CED prints none of their texts, so an invented
passage over a real name would be a fabrication a student would read as a real
quotation and no later reader could check. Every source in this module is
therefore explicitly unattributed and written for the item, and no key asserts
anything about any named traveller.

WHAT THE SOURCING ITEMS ARE KEYED TO. A sourcing key cannot rest on a Key
Concept alone, because skill 2.A is a skill and not a content statement. Each
such key here is keyed to the skill AND to the framework sentence that supplies
the material it operates on -- normally KC-3.1.III.C, which is why travel
accounts exist to be sourced at all, and in q23 KC-3.3.II, which is what a city
register bears on. The claims below say which, in every case.

WHERE THE ANCHOR CARRIES TWO CLAUSES, AND WHY
---------------------------------------------
Five distractors here are the SWAP of the key rather than an unrelated claim:

  q7   which column multiplies by more, accounts or journeys
  q9   which practice spreads furthest, the narrowest or the widest at the start
  q11  purpose and point of view, their definitions exchanged
  q16  which of exchange and writing follows from the other
  q24  contact producing diffusion, against diffusion producing contact

Those anchors carry both clauses in order, which is the defect verify_e2_1.py
shipped and HISTORY_BRIEF.md records.

DATA QUESTIONS
--------------
Items 5, 7 and 9 carry tables of HYPOTHETICAL figures and each stem says so.
Each keyed conclusion is recomputed below from the table alone AND every
distractor is shown false on the same numbers. The household figures in q5 carry
thousands commas; cg.num strips them, which is why the check reads 9,000 as nine
thousand rather than failing. The control's per-table catch rate is never nine
of nine: the label column cannot be corrupted into a contradiction, and a
corruption leaving the keyed conclusion TRUE must not be caught. A zero would
mean the check had stopped reading its table.

NEGATIVE CONTROL: `python3 verify_w2_5.py --selftest`.
"""
import sys

import cg_check as cg
import w2_5
import wh_check

EARLY_H = "Households recorded at an earlier date"
LATE_H = "Households recorded at a later date"
ACCOUNTS = "Surviving accounts of travel"
JOURNEYS = "Recorded long-distance journeys"
EARLY_R = "Regions in which it is recorded in an earlier period"
LATE_R = "Regions in which it is recorded in a later period"


def q5(table, item):
    """One city falls, one rises, one is level -- no single direction."""
    early, late = cg.col(table, EARLY_H), cg.col(table, LATE_H)
    fell = [i for i in range(len(early)) if late[i] < early[i]]
    rose = [i for i in range(len(early)) if late[i] > early[i]]
    level = [i for i in range(len(early)) if late[i] == early[i]]
    assert len(early) == 3 and len(fell) == 1 and len(rose) == 1 and len(level) == 1, \
        f"one of each direction is required: fell={fell} rose={rose} level={level}"
    # every distractor false on the same numbers
    assert not all(l > e for e, l in zip(early, late)), "'every city grew' must be false"
    assert not all(l < e for e, l in zip(early, late)), "'every city declined' must be false"
    assert early.index(max(early)) != late.index(max(late)), \
        "'the largest city earlier is the largest later' must be false"
    assert not all(l == e for e, l in zip(early, late)), "'all unchanged' must be false"
    return (f"earlier {early} against later {late}: one city falls, one rises and one "
            f"does not move, so the three point three ways")


def q7(table, item):
    """Both rise, and ACCOUNTS multiply by more than JOURNEYS across the span."""
    accounts, journeys = cg.col(table, ACCOUNTS), cg.col(table, JOURNEYS)
    assert all(b > a for a, b in zip(accounts, accounts[1:])), \
        f"accounts must rise at every step: {accounts}"
    assert all(b > a for a, b in zip(journeys, journeys[1:])), \
        f"journeys must rise at every step: {journeys}"
    acc_mult = accounts[-1] / accounts[0]
    jou_mult = journeys[-1] / journeys[0]
    assert acc_mult > jou_mult, \
        f"accounts must multiply by more: {acc_mult} against {jou_mult}"
    # every distractor false on the same numbers
    assert not jou_mult > acc_mult, "'journeys multiply by more' must be false"
    assert not any(b < a for a, b in zip(accounts, accounts[1:])), \
        "'accounts fall' must be false"
    assert not any(b < a for a, b in zip(journeys, journeys[1:])), \
        "'journeys fall' must be false"
    assert len(set(accounts)) > 1, "'both unchanged' must be false"
    return (f"accounts {accounts} multiply by {round(acc_mult, 2)} while journeys "
            f"{journeys} multiply by {round(jou_mult, 2)}")


def q9(table, item):
    """All spread, and the NARROWEST at the start reaches the MOST regions."""
    early, late = cg.col(table, EARLY_R), cg.col(table, LATE_R)
    assert all(l > e for e, l in zip(early, late)), \
        f"every practice must reach more regions: {early} to {late}"
    narrowest = early.index(min(early))
    assert late[narrowest] == max(late), \
        f"the narrowest practice at the start must reach the most regions: {early} / {late}"
    # every distractor false on the same numbers
    widest = early.index(max(early))
    assert late[widest] != max(late), \
        "'the widest practice at the start reaches the most later' must be false"
    assert not any(l < e for e, l in zip(early, late)), \
        "'one practice reaches fewer regions later' must be false"
    assert len(set(late)) > 1, "'all reach the same number later' must be false"
    assert late[narrowest] != min(late), \
        "'the narrowest at the start reaches the fewest later' must be false"
    return (f"earlier {early} to later {late}: all spread, and the practice starting in "
            f"{min(early)} region(s) ends in {late[narrowest]}, the widest")


TABLE_CHECKS = {5: q5, 7: q7, 9: q9}

CLAIMS = [
 ("reflects what its readers did not know",
  "Suggested skill 2.A for this topic asks students to identify a source's point of view, purpose, historical situation and AUDIENCE, and KC-3.1.III.C states that as exchange networks intensified, an increasing number of travelers within Afro-Eurasia wrote about their travels. An audience that has never seen a place is what makes strangeness worth reporting and familiarity not worth mentioning."),

 ("an increasing number of travellers within Afro-Eurasia wrote about their travels",
  "KC-3.1.III.C states that as exchange networks intensified, an increasing number of travelers within Afro-Eurasia wrote about their travels. The sentence ties the quantity of writing to the intensity of exchange, which is what each rejected option denies."),

 ("a reason to present the journey as having achieved something",
  "Suggested skill 2.A asks students to identify a source's PURPOSE as well as its point of view, and KC-3.1.III.C records travellers within Afro-Eurasia writing about their travels in growing numbers. A document written to justify an expense is arguing as well as reporting, which is what a historian must weigh."),

 ("some cities passing through significant decline and others through increased urbanization",
  "KC-3.3.II states that the fate of cities varied greatly, with periods of significant decline and periods of increased urbanization, buoyed by rising productivity and expanding trade networks. Variation is the claim the sentence makes, and each rejected option asserts a uniformity instead."),

 ("one downward, one upward and one not at all",
  "Recomputed in q5 above from the two columns, distractors included. KC-3.3.II states that the fate of cities varied greatly, with periods of significant decline and periods of increased urbanization, and figures pointing three ways at once are what that variation looks like in a record."),

 ("diffusion of a cultural tradition through cross-cultural interaction",
  "KC-3.1.III.D states that increased cross-cultural interactions resulted in the diffusion of literary, artistic, and cultural traditions, as well as scientific and technological innovations. A text copied, translated and used far from where it was written is diffusion in exactly that sense."),

 ("the accounts multiply by a larger factor than the journeys do",
  "Recomputed in q7 above from the two columns. KC-3.1.III.C states that as exchange networks intensified, an INCREASING NUMBER of travelers within Afro-Eurasia wrote about their travels, so writing growing faster than travel is the pattern that sentence describes. The anchor carries both columns in order because the strongest distractor exchanges them."),

 ("a single city's record cannot be made to stand for cities in general",
  "KC-3.3.II states that the fate of cities VARIED GREATLY, with periods of significant decline and periods of increased urbanization, buoyed by rising productivity and expanding trade networks. A claim of variation is not settled by one case on either side of it."),

 ("the practice recorded in fewest regions earlier reaches the most regions later",
  "Recomputed in q9 above from the two columns. KC-3.1.III.D states that increased cross-cultural interactions resulted in the diffusion of literary, artistic, and cultural traditions, as well as scientific and technological innovations, and uneven spread is what diffusion looks like in a record. The anchor carries both clauses because the strongest distractor exchanges which practice travels furthest."),

 ("outside the learned and official worlds",
  "Suggested skill 2.A asks students to identify a source's POINT OF VIEW as well as its purpose and audience, and KC-3.1.III.C records an increasing number of travelers within Afro-Eurasia writing about their travels. Who a writer is bears on what the writing notices and what it passes over."),

 ("Purpose is what the writer meant the text to accomplish, and point of view is the position from which the writer saw",
  "Suggested skill 2.A for this topic names a source's point of view, purpose, historical situation, and audience as four separable things to identify, and KC-3.1.III.C supplies the travel accounts the skill is practised on here. The anchor carries both definitions in order because the strongest distractor exchanges them."),

 ("diffusion of a technological innovation through the contact that trade created",
  "KC-3.1.III.D states that increased cross-cultural interactions resulted in the diffusion of literary, artistic, and cultural traditions, AS WELL AS scientific and technological innovations. The framework puts both kinds of diffusion in one sentence, which is why a technique and a devotional text are instances of the same claim."),

 ("what situation the writer was in when the account was composed",
  "Suggested skill 2.A names a source's HISTORICAL SITUATION among the things a student must identify, and KC-3.1.III.C records the growing body of travel writing the skill is practised on. When and under what conditions a text was written bears on what it can be used to show."),

 ("every society receiving a tradition from outside abandoned its own",
  "KC-3.1.III.D asserts diffusion, KC-3.1.III.C the growth of travel writing, and KC-3.3.II the variation in the fate of cities. Nothing in any of the three says that a receiving society gave up its own traditions in exchange, which is what makes that the unsupported claim."),

 ("The distance in time between the events and the writing is part of the source's situation",
  "Suggested skill 2.A names a source's historical situation among the things to be identified, and KC-3.1.III.C records travellers within Afro-Eurasia writing about their travels in growing numbers as exchange networks intensified. When a text was written relative to what it describes is part of that situation."),

 ("the framework makes the growth in travel writing follow from",
  "KC-3.1.III.C states that AS exchange networks intensified, an increasing number of travelers within Afro-Eurasia wrote about their travels. The connective makes the writing follow the exchange, and the anchor carries both halves in order because the strongest distractor reverses them."),

 ("a question about reception rather than about the practice itself",
  "KC-3.1.III.D states that increased cross-cultural interactions resulted in the diffusion of literary, artistic, and cultural traditions, and the Cultural Developments thematic focus states that the development of ideas, beliefs, and religions illustrates how groups in society view themselves. Suggested skill 2.A asks what a particular source's point of view can and cannot establish."),

 ("attaches that growth to more being produced and to wider exchange",
  "KC-3.3.II states that the fate of cities varied greatly, with periods of significant decline and periods of increased urbanization, BUOYED BY rising productivity and expanding trade networks. The participle attaches a support to the growth without asserting that every city grew."),

 ("a difference of judgment may follow from a difference of situation",
  "Suggested skill 2.A asks students to identify a source's point of view, purpose, historical situation and audience, and KC-3.1.III.C supplies the growing body of travel accounts on which that skill is exercised. Two situations can produce two honest and different judgments of the same place."),

 ("without stating that any particular tradition displaced another",
  "KC-3.1.III.D states that increased cross-cultural interactions resulted in the diffusion of literary, artistic, and cultural traditions, as well as scientific and technological innovations. It asserts spread, names no displacement, and confines itself to no single category of thing spread."),

 ("prices, dangers and the customs of dealing are likely to be full",
  "Suggested skill 2.A names AUDIENCE among the things a student identifies in a source, and KC-3.1.III.C records travellers writing about their travels in growing numbers as exchange networks intensified. What readers intend to do with a text shapes what is worth putting in it."),

 ("the writing is a trace of the movement that produced it",
  "KC-3.1.III.C states that as exchange networks intensified, an increasing number of travelers within Afro-Eurasia wrote about their travels, and Learning Objective J asks for the intellectual and cultural effects of the various networks of exchange in Afro-Eurasia from c. 1200 to c. 1450."),

 ("what fell outside that concern may be absent though it existed",
  "Suggested skill 2.A asks students to identify a source's PURPOSE, and KC-3.3.II makes the fate of cities, which such a register bears on, a subject of this topic. A document made for one administrative use is complete for that use and silent about much else."),

 ("It treats increased cross-cultural interaction as producing diffusion",
  "KC-3.1.III.D states that increased cross-cultural interactions RESULTED IN the diffusion of literary, artistic, and cultural traditions, as well as scientific and technological innovations. The verb makes contact the cause, and the anchor carries both halves in order because the strongest distractor reverses them."),

 ("evidence of contact or of a route between them is what turns the observation into a claim about spread",
  "KC-3.1.III.D attributes diffusion to INCREASED CROSS-CULTURAL INTERACTIONS, so the framework's own account of spread runs through contact. Suggested skill 2.A asks what a source establishes, and a bare coincidence of presence establishes less than a route between the two places does."),

 ("the praise is evidence of the relationship between writer and host",
  "Suggested skill 2.A asks students to identify a source's point of view and historical situation, and KC-3.1.III.C records the growing body of travel writing in this period. A writer's position relative to a subject is part of what the text is evidence for."),

 ("bears on how a society understands itself and not only on what it practises",
  "The Cultural Developments thematic focus states that the development of ideas, beliefs, and religions illustrates how groups in society view themselves, and that the interactions of societies and their beliefs often have political, social, and cultural implications. KC-3.1.III.D supplies the diffusion those interactions produce."),

 ("built in the same years in which the traffic through its market multiplied",
  "KC-3.3.II states that the fate of cities varied greatly, with periods of significant decline and periods of increased urbanization, BUOYED BY rising productivity and expanding trade networks. Building and traffic growing together is the pattern that clause describes."),

 ("almost everything known about diffusion in this period reaches us through texts",
  "Suggested skill 2.A for this topic is to identify a source's point of view, purpose, historical situation, and audience, and KC-3.1.III.C states that as exchange networks intensified, an increasing number of travelers within Afro-Eurasia wrote about their travels. Those writings are the evidence for the diffusion KC-3.1.III.D asserts."),

 ("the cities along those networks rose or fell rather than following one course",
  "KC-3.1.III.D supplies the diffusion of literary, artistic, and cultural traditions as well as scientific and technological innovations, KC-3.1.III.C the increasing number of travelers who wrote about their travels as exchange networks intensified, and KC-3.3.II the varied fate of cities. Each rejected option contradicts at least one of the three."),
]

wh_check.run(w2_5, CLAIMS, TABLE_CHECKS, sys.argv)
