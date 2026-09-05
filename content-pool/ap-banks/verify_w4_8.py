"""Key audit for AP WORLD HISTORY: MODERN 4.8 Continuity and Change from 1450 to 1750.

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

THIS IS THE UNIT'S REASONING TOPIC AND THE MODULE IS BUILT AS ONE. The CED page
prints no new key concept: it prints a REVIEW list, suggested skill 6.C, and a
paragraph saying the final topic in this unit focuses on the skill of
argumentation. So most keys here rest on a RELATIONSHIP rather than on a fact --
what a piece of evidence shows, which of two series the framework makes the
cause, what would strengthen or weaken a stated argument, and where an argument
outruns what its evidence can carry. Items 9 to 15 and 23 to 29 are of that
kind; items 1 to 8 establish the review list the reasoning runs on, and 16 to 22
apply it to a table or a stimulus.

THE ONE ERROR THIS TOPIC INVITES ABOVE ALL OTHERS is keying the change and
dropping the continuity. KC-4.2 is a single sentence with a subordinate
continuity and a main-clause set of changes: ALTHOUGH the world's productive
systems continued to be heavily centered on agriculture, major changes occurred
in agricultural labor, the systems and locations of manufacturing, gender and
social structures, and environmental processes. In a topic called Continuity and
Change it is very easy to write thirty items about the change. q4, q11, q12, q17,
q20, q27, q29 and q30 all turn on holding the two halves together, and q17's
table is built so that agriculture keeps the larger share in every period while
manufacturing rises -- a table where manufacturing overtook agriculture would
have made a distractor true.

KC-4.3 RUNS BOTH WAYS for the same reason: empires shaping AND being shaped by
the diverse populations they incorporated. q8 and q21 keep both directions and
q8's anchor carries both clauses, because three of its distractors are the
sentence with one direction removed.

WHAT NO ITEM ASSERTS. The framework weighs no period against another, which q28
keys as precisely the claim needing an outside source. And q15 turns on the CED's
own wording: KC-4.2.II says the Atlantic slave trade DEVELOPED AND INTENSIFIED,
which is growth and not a beginning -- reinforced by the CED's note that events
and processes are not constrained by the given dates.

NEGATIVE CONTROL: `python3 verify_w4_8.py --selftest`.
"""
import sys

import cg_check as cg
import wh_check as wh
import wh_stimulus as ws

import w4_8

RECORDS = "What it records"
AGRI = "Share of the recorded workforce in agriculture (percent)"
MANU = "Share of the recorded workforce in manufacturing crafts (percent)"
OFFERED = "Evidence the essay offers for it"


def q16(table, item):
    """Three pieces of evidence bear on the demand for labor; one does not."""
    labs = cg.labels(table)
    assert labs == ["Evidence %d" % n for n in range(1, 5)], \
        f"the four pieces the key counts are not the rows: {labs}"
    # A closed vocabulary, parsed rather than searched, so a corrupted cell falls
    # outside it and the check fails instead of quietly passing.
    bears = {
        "rising exports of a raw material from one region": True,
        "more laborers recorded on the plantations of that region": True,
        "more enslaved persons landed at that region's ports": True,
        "the rebuilding of a cathedral tower in a distant city": False,
    }
    got = []
    for row in table["rows"]:
        note = cg.normalize(row[1])
        assert note in bears, f"the evidence {note!r} is outside this item's vocabulary"
        got.append(bears[note])
    assert sum(got) == 3, f"the key needs three qualifying pieces; got {sum(got)} from {got}"
    # KC-4.2.II reaches demand for goods, plantations AND the Atlantic slave
    # trade, so the three qualifying rows must not all be of one kind.
    assert not all(got), "'all four' must be false"
    assert any(got), "'none of the four' must be false"
    assert sum(got) not in (1, 2), "the one-piece and two-piece readings must both be false"
    return ("three rows record exports of a raw material, plantation laborers and arrivals of "
            "enslaved persons, all inside KC-4.2.II's account, and the fourth records a cathedral "
            "tower, which is outside it")


def q17(table, item):
    """Agriculture keeps the larger share while manufacturing rises throughout."""
    labs = cg.labels(table)
    assert labs == ["First period", "Second period", "Third period", "Fourth period"], \
        f"the key speaks of every period shown, so the four periods must be the rows: {labs}"
    agri, manu = cg.col(table, AGRI), cg.col(table, MANU)
    assert all(a > m for a, m in zip(agri, manu)), (
        "KC-4.2's continuity needs agriculture to hold the larger share in EVERY period; "
        f"got {agri} against {manu}")
    assert all(manu[i + 1] > manu[i] for i in range(len(manu) - 1)), \
        f"the manufacturing share must rise at every step; got {manu}"
    # and every distractor false on the same numbers
    assert not any(m >= a for a, m in zip(agri, manu)), \
        "'manufacturing overtakes agriculture' must be false in every period"
    assert not all(agri[i + 1] > agri[i] for i in range(len(agri) - 1)), \
        "'the agricultural share rises' must be false"
    assert len(set(agri)) > 1 and len(set(manu)) > 1, \
        "'neither share changes' must be false"
    assert agri[-1] != manu[-1], "'the two shares are equal in the final period' must be false"
    return (f"agriculture reads {agri} against manufacturing {manu}, so agriculture holds the "
            "larger share in all four periods while the manufacturing share rises at every step")


def q18(table, item):
    """Three claims are matched to evidence that bears on them; one is not."""
    claims = cg.labels(table)
    assert len(claims) == 4 and len(set(claims)) == 4, \
        f"the essay must offer four distinct claims; got {claims}"
    # The pairing is what the item is about, so both halves of each row are
    # parsed against a closed vocabulary and the match is recomputed rather than
    # asserted. A corrupted cell in either column falls outside and fails.
    fits = {
        ("that the demand for labor intensified",
         "records of more laborers on plantations and more raw material exported"): True,
        ("that transoceanic voyaging transformed trade",
         "records of goods arriving by sea that had previously come overland"): True,
        ("that an empire was shaped by a population it incorporated",
         "records of a court adopting practices of a newly incorporated group"): True,
        ("that the climate of the atlantic changed",
         "records of more laborers on plantations"): False,
    }
    got = []
    for row in table["rows"]:
        pair = (cg.normalize(row[0]), cg.normalize(row[1]))
        assert pair in fits, f"the pairing {pair!r} is outside this item's vocabulary"
        got.append(fits[pair])
    assert sum(got) == 3, f"the key needs three fitting pairings; got {sum(got)} from {got}"
    # The mismatched row must reuse evidence that fits a DIFFERENT claim, which
    # is what makes it a misuse rather than simply an absence of evidence.
    misfit = [cg.normalize(r[1]) for r, ok in zip(table["rows"], got) if not ok]
    others = [cg.normalize(r[1]) for r, ok in zip(table["rows"], got) if ok]
    assert len(misfit) == 1, f"exactly one pairing must fail; got {misfit}"
    assert any(misfit[0] in o for o in others), (
        "the failing row's evidence must also appear under a claim it does fit, or the key's "
        "phrase 'bears on a different claim' is not what the table shows")
    assert all(r[1].strip() for r in table["rows"]), \
        "'the essay offers no evidence for any of its claims' must be false"
    return ("three rows pair a claim with evidence that bears on it, and the fourth offers "
            "plantation laborers for a claim about the climate, which is evidence bearing on a "
            "different claim in the same table")


CLAIMS = [
 ("Practising the skill of argumentation",
  "The CED page for this topic says the final topic in this unit focuses on the skill of argumentation and provides an opportunity for students to draw upon the key concepts and historical developments they have studied in the unit, using evidence relevant to those key concepts. It prints a review list of KC-4.1, KC-4.2 and KC-4.3 rather than any new concept."),
 ("Use historical reasoning to explain relationships among pieces of historical evidence",
  "Suggested skill 6.C for this topic is to use historical reasoning to explain relationships among pieces of historical evidence, with continuity and change as the reasoning process. Authorship belongs to suggested skill 2.A, and the remaining options describe handling evidence without reasoning about it, which is what KC-4.2 and its siblings are here to be reasoned about."),
 ("economic developments from 1450 to 1750 affected social structures",
  "Unit 4: Learning Objective N asks students to explain how economic developments from 1450 to 1750 affected social structures over time, which is why the review list beside it carries KC-4.1, KC-4.2 and KC-4.3. The rejected options reverse the direction of the explanation or shrink it to a single household or harvest."),
 # Both clauses: the sentence is a continuity AND a set of changes, and each
 # distractor keeps one and drops the other.
 ("heavily centered on agriculture, although major changes occurred",
  "KC-4.2 says that although the world's productive systems continued to be heavily centered on agriculture, major changes occurred in agricultural labor, the systems and locations of manufacturing, gender and social structures, and environmental processes. The continuity and the changes are one sentence."),
 ("growing global demand for raw materials and finished products",
  "KC-4.2.II says the demand for labor intensified as a result of the growing global demand for raw materials and finished products. KC-4.2 says productive systems continued to be heavily centered on agriculture rather than abandoning it, and the framework offers none of the other causes."),
 ("plantations expanded, and the Atlantic slave trade developed and intensified",
  "KC-4.2.II names traditional peasant agriculture increasing and changing in nature, plantations expanding, and the Atlantic slave trade developing and intensifying. The rejected lists reverse all three or belong to KC-4.1.II.A, KC-4.1.IV.C and KC-4.3."),
 # Both clauses: two distractors keep one consequence and drop the other.
 ("transformed trade and had a significant social impact",
  "KC-4.1 says the interconnection of the Eastern and Western Hemispheres, made possible by transoceanic voyaging, transformed trade and had a significant social impact on the world. Both consequences are asserted in the one sentence."),
 # Both clauses: three distractors are the sentence with one direction removed.
 ("shaped the diverse populations they incorporated and were shaped by them in turn",
  "KC-4.3 says empires achieved increased scope and influence around the world, shaping and being shaped by the diverse populations they incorporated. The two directions are given together, and dropping either is the error the distractors are built from."),
 ("growing demand for raw materials intensified the demand for labor",
  "KC-4.2.II states the relationship in that direction: the demand for labor intensified as a result of the growing global demand for raw materials and finished products. The reversed reading is not what the sentence says, and the framework connects neither ship design nor climate to a rising workforce."),
 ("goods that once came overland arriving by sea",
  "KC-4.1 says the interconnection of the hemispheres, made possible by transoceanic voyaging, transformed trade, so evidence for it must show a route or a pattern of trade changing. Masons, an accession, rainfall and a library leave the argument where it stood."),
 ("most of the recorded workforce still in agriculture at the end of the period",
  "KC-4.2 says the world's productive systems continued to be heavily centered on agriculture even as major changes occurred around them, so a workforce still concentrated in agriculture is the direct counter-evidence to a claim that agriculture ceased to be the centre. Ship counts, titles, one price and a correspondence bear on the claim not at all."),
 # Both clauses: the distractor exchanges which is the continuity and which the
 # change, and each half of the key appears in it.
 ("Agriculture remaining the base of production is the continuity, and the expansion of plantations is the change",
  "KC-4.2 gives the continuity, productive systems continuing to be heavily centered on agriculture, and KC-4.2.II gives the change, plantations expanding as the demand for labor intensified. Exchanging them inverts the pair and denying either denies half of KC-4.2."),
 ("rose together, and the framework puts the causation the other way",
  "Two series rising together establish that they moved together and not which moved the other, and KC-4.2.II gives the framework's direction: the demand for labor intensified as a result of the growing global demand for raw materials and finished products. The student has reversed it."),
 ("volume of trade through that port grew",
  "One port's totals support a claim about that port and no more. KC-4.1 makes the wider claim about world trade and KC-4.1.II.A the claim about ship design, but neither can be read off a single port's book, and keeping track of scale is what suggested skill 6.C asks when relating pieces of evidence."),
 ("overstates it, since the framework says the Atlantic slave trade developed and intensified",
  "KC-4.2.II says the Atlantic slave trade developed and intensified, which describes growth rather than a beginning, and the CED's own note says events, processes, and developments are not constrained by the given dates and may begin before or continue after the period."),
 ("Three of the four, since one records something unconnected",
  "KC-4.2.II ties the intensified demand for labor to the growing global demand for raw materials and finished products and names expanding plantations and the intensifying Atlantic slave trade alongside it. Recomputed in q16 above: three rows fall inside that account and the cathedral tower falls outside it."),
 # Both clauses: the continuity and the change are both needed, and a distractor
 # has manufacturing overtaking agriculture.
 ("larger share in every period while the manufacturing share rises",
  "KC-4.2 says productive systems continued to be heavily centered on agriculture although major changes occurred in the systems and locations of manufacturing. Recomputed in q17 above: agriculture holds the larger share in all four periods while the manufacturing share rises at every step."),
 ("supported by evidence that bears on them, and one is supported by evidence that bears on a different claim",
  "Suggested skill 6.C asks a student to explain relationships among pieces of evidence, and the relationship at issue is whether a piece bears on the claim it is offered for; KC-4.2.II makes plantation laborers evidence about the demand for labor and not about a climate. Recomputed in q18 above: three pairings hold and one reuses evidence that fits a different claim in the same table."),
 ("transoceanic voyaging transformed trade and had a social impact",
  "KC-4.1 says the interconnection of the Eastern and Western Hemispheres, made possible by transoceanic voyaging, transformed trade and had a significant social impact on the world, and an account joining a changed route to changed trades in the town shows both halves at once. The rejected options are KC-4.3, KC-4.3.III.ii, KC-4.2 and KC-4.1.II."),
 # Both clauses: a distractor exchanges which half is the continuity.
 ("continuity in what was produced together with a change in how labor was organised",
  "KC-4.2 says productive systems continued to be heavily centered on agriculture although major changes occurred in agricultural labor, and KC-4.2.II adds that traditional peasant agriculture increased and changed in nature. Same fields with more hands on different terms is that pairing."),
 ("empires shaped and were shaped by the diverse populations",
  "KC-4.3 says empires achieved increased scope and influence around the world, shaping and being shaped by the diverse populations they incorporated, and a court taking up provincial customs while the province takes up imperial administration is influence running both ways. The rejected options are KC-4.2.II, KC-4.1.II.A, KC-4.3.III.ii and KC-4.2."),
 ("Economic disputes led to rivalries and conflict",
  "KC-4.3.III.ii, printed in this topic's review list, says economic disputes led to rivalries and conflict between states, and a quarrel over who carries a route's trade is an economic dispute. Political and religious disputes are KC-4.3.III.i, which belongs to unit 3 and is not in this review list."),
 ("intensified the demand for labor, plantations expanded and the Atlantic slave trade intensified",
  "KC-4.2.II runs from the growing global demand for raw materials and finished products to the intensified demand for labor, expanding plantations and the developing and intensifying Atlantic slave trade, while KC-4.2 names gender and social structures among what changed and KC-4.1 records a significant social impact. The rejected chains reverse or break that order, which Unit 4: Learning Objective N asks students to get right."),
 ("social structure was unchanged across the period",
  "KC-4.2.II ties expanding plantations and an intensifying Atlantic slave trade to the intensified demand for labor, and KC-4.2 names gender and social structures among what changed in the period, so an unchanged social structure runs against the framework rather than following from the file. The other four claims are read directly off the three series."),
 ("arrangements of work and family in a region changed as its trade changed",
  "KC-4.1 says the interconnection of the hemispheres transformed trade AND had a significant social impact on the world, and KC-4.2 names gender and social structures among what changed, so the missing half of the argument is evidence about how people lived and worked. Faster voyages, a new duty, a redrawn chart and a share issue are commercial or technical."),
 ("change in how and where production was organised",
  "KC-4.2 describes major changes in agricultural labor and in the systems and locations of manufacturing, and KC-4.2.II names the expansion of plantations, so evidence at the level of how production was organised is what the claim needs. One village's harvest in one year speaks to weather rather than to a productive system."),
 ("production in the region remained centered on agriculture",
  "KC-4.2 says the world's productive systems continued to be heavily centered on agriculture although major changes occurred around them, so in a set of changes the agricultural base is the continuity the framework points to. Every rejected option names one of the changes instead."),
 ("mattered more to the world than those of the previous period",
  "The four rejected statements are KC-4.1, KC-4.2.II, KC-4.2 and KC-4.3 almost verbatim. The framework weighs no period against another for importance, so a comparison of that kind would have to be defended from another source."),
 ("pairs things that continued with things that changed",
  "KC-4.2 pairs productive systems continuing to be heavily centered on agriculture with major changes in labor, manufacturing, social structures and environmental processes, and KC-4.2.II pairs traditional peasant agriculture increasing with its changing in nature. Causation is the reasoning process printed with other topics of this unit, including 4.1 and 4.6."),
 ("production stayed centered on agriculture even as labor, manufacturing and social structures changed",
  "The keyed sentence joins KC-4.1, KC-4.2, KC-4.2.II and KC-4.3, which is the review list printed beside this topic. Each rejected version denies the transformation of trade, reverses the continuity in productive systems, drops one direction of KC-4.3's two-way relationship, or denies the continuities that make this a continuity and change topic."),
]

TABLE_CHECKS = {16: q16, 17: q17, 18: q18}

if __name__ == "__main__" and "--selftest" in sys.argv:
    ws.controls(w4_8)

ws.marked_stimulus(w4_8)
wh.run(w4_8, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
