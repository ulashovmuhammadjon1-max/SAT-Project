"""Key audit for AP WORLD HISTORY: MODERN 5.1 The Enlightenment.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on and
cites the Key Concept or Learning Objective it traces to.

WHAT THE KEYS REST ON
---------------------
Every key here traces to a sentence the CED prints on this topic's page:
KC-5.3.I.A (empiricist approaches applied to the natural world AND to human
relationships; the reexamination of religion's role in public life; the emphasis
on reason; the new political ideas about the individual, natural rights and the
social contract), KC-5.3.I (the rise and diffusion of that thought questioned
established traditions in all areas of life and OFTEN PRECEDED revolutions and
rebellions), KC-5.3.II.i (nationalism as a major force shaping states and
empires), KC-5.3.I.C (Enlightenment ideas AND religious ideals influenced reform
movements, which contributed to expanded suffrage, the abolition of slavery and
the end of serfdom) and KC-5.3.IV.B (demands for women's suffrage and an emergent
feminism challenged political and gender hierarchies). Items 7, 8 and 9 key to
the illustrative examples printed on the same page.

WHAT THEY DELIBERATELY DO NOT REST ON
-------------------------------------
Nothing here keys to a fact about the Enlightenment that the CED does not print.
No item asks for the date of a revolution, the nationality of a philosopher, or
the argument of a named book beyond the fact that the framework names it -- those
would rest on general knowledge, which is exactly what HISTORY_BRIEF.md forbids
because a later reader cannot check it. The only date keyed anywhere is 1848,
which the framework itself prints beside the Seneca Falls Conference.

SWAP ANCHORS
------------
Items 3, 18, 20 and 21 carry a distractor that is the key with its two clauses
exchanged -- cause and effect reversed, a comparison reversed, two sources of
argument exchanged. Their anchors carry BOTH clauses, because an anchor naming
only one of them matches the swap as well. That is the defect found in
verify_e2_1.py and it is checked here by the key-rotation control below, which
requires all thirty keys to fail when moved one place.

FIVE choices per item (A-E); see HISTORY_BRIEF.md.
"""
import sys

import cg_check as cg
import wh_check as wh
import w5_1

CLAIM_COL = "Central claim advanced"
COUNT_COL = "Number of pamphlets"


def q13(table, item):
    """The natural-rights pamphlet is the one placing rights before government."""
    labels = cg.labels(table)
    claims = {lab: str(row[1]) for lab, row in zip(labels, table["rows"])}
    prior = [lab for lab, c in claims.items() if "before any government" in c.lower()]
    assert prior == ["Pamphlet 2"], (
        f"exactly one row must place rights before government, and it must be Pamphlet 2; got {prior}"
    )
    contract = [lab for lab, c in claims.items() if "agreement with the governed" in c.lower()]
    assert contract == ["Pamphlet 1"], (
        f"the social-contract claim must sit on Pamphlet 1 alone; got {contract}"
    )
    assert "ancestors" in claims["Pamphlet 3"].lower(), "Pamphlet 3 must argue from inherited custom"
    assert "treasury" in claims["Pamphlet 4"].lower(), "Pamphlet 4 must argue from the treasury"
    assert cg.contains_phrase(item["choices"][item["ans"]], "Pamphlet 2")
    return ("read from the table alone: only Pamphlet 2 asserts rights existing before any "
            "government, while Pamphlet 1 states the social contract and the other two state neither")


def q20(table, item):
    """The keyed comparison and every distractor recomputed from the counts."""
    counts = dict(zip(cg.labels(table), cg.col(table, COUNT_COL)))
    total = sum(counts.values())
    assert total == 200, f"the stem says two hundred pamphlets; the column sums to {total}"
    rights = counts["Natural rights and the social contract"]
    religion = counts["The role of religion in public life"]
    farming = counts["Improvement of agriculture"]
    court = counts["Ceremony and etiquette at court"]
    other = counts["Other subjects"]
    assert rights > religion, "the key requires more on natural rights than on religion"
    assert not rights < farming, "'fewer than agriculture' must be false on these numbers"
    assert court < max(counts.values()), "'most treat court etiquette' must be false"
    assert court != max(counts.values()), "court etiquette must not be the largest category"
    assert other > 0, "'every pamphlet treats a political subject' must be false: other subjects is nonempty"
    return (f"recomputed from the table: {rights:.0f} on natural rights against "
            f"{religion:.0f} on religion, {farming:.0f} on agriculture, {court:.0f} on court "
            f"ceremony and {other:.0f} on other subjects, summing to {total:.0f}")


CLAIMS = [
 ("empiricist approach already applied to the natural world",
  "KC-5.3.I.A states that Enlightenment philosophies applied new ways of understanding and empiricist approaches to BOTH the natural world AND human relationships. The source carries a method used for bodies over to people, which is that sentence enacted; the rejected options either deny observation altogether or make inherited belief the evidence."),
 ("the social contract",
  "KC-5.3.I.A ends by naming the three new political ideas: the individual, natural rights, and the social contract. The four rejected groupings name arrangements the framework describes such thought as questioning, not ideas it produced."),
 ("established traditions often came before rebellions",
  "KC-5.3.I, near verbatim: the rise and diffusion of Enlightenment thought that questioned established traditions often PRECEDED revolutions and rebellions against existing governments. The anchor carries both clauses because one distractor is the same sentence with cause and effect exchanged."),
 ("the end of serfdom",
  "KC-5.3.I.C names the three expansions of rights together: expanded suffrage, the abolition of slavery, and the end of serfdom. No other listed set is attached by the framework to reform movements of this period."),
 ("both Enlightenment ideas and religious ideals",
  "KC-5.3.I.C opens by naming two influences at once: Enlightenment ideas AND religious ideals influenced various reform movements. Two appeals for one reform, one from natural rights and one from religious duty, is that sentence in miniature."),
 ("political and gender hierarchies",
  "KC-5.3.IV.B, near verbatim: demands for women's suffrage and an emergent feminism challenged political and gender hierarchies. The rejected options name coal and iron, banking, national boundaries and factory organization, which the framework treats in topics 5.3 through 5.7."),
 ("A Vindication of the Rights of Woman",
  "The illustrative examples printed beside KC-5.3.IV.B on this topic's page, under Demands, name Mary Wollstonecraft's A Vindication of the Rights of Woman. The rejected titles belong to the framework's economic, industrial and revolutionary-document material rather than to this list."),
 ("Rights of Woman and of the Female Citizen",
  "The same illustrative list, printed beside KC-5.3.IV.B, names Olympe de Gouges's Declaration of the Rights of Woman and of the Female Citizen. The document it echoes, the Declaration of the Rights of Man and of the Citizen, is named separately in KC-5.3.I.B as a French revolutionary document, so the anchor carries the distinguishing words rather than the shared opening."),
 ("Elizabeth Cady Stanton and Lucretia Mott",
  "The illustrative list printed beside KC-5.3.IV.B names the Seneca Falls Conference (1848) organized by Elizabeth Cady Stanton and Lucretia Mott. This is the only date keyed in the module and it is the framework's own."),
 ("role that religion played in public life",
  "KC-5.3.I.A states that Enlightenment philosophies reexamined the role that religion played in public life. The framework describes a reexamination of religion's public role, which is what a source about confession, law and office is doing, and not a rejection of belief."),
 ("the importance of reason",
  "KC-5.3.I.A states that Enlightenment philosophies emphasized the importance of reason. A line ranking reason above the mere age of a custom states that emphasis as a rule of decision; the rejected options name capital, language and specialization, which belong to KC-5.1."),
 ("Nationalism",
  "KC-5.3.II.i, printed on this topic's page: nationalism ALSO became a major force shaping the historical development of states and empires. The word also places it beside Enlightenment thought, which is why the framework prints it here rather than only in topic 5.2."),
 ("Pamphlet 2",
  "KC-5.3.I.A distinguishes natural rights from the social contract, and the table is recomputed in q13 above: only the second pamphlet asserts rights existing before any government, while the first states the social contract instead."),
 ("The social contract",
  "KC-5.3.I.A names the social contract among the new political ideas. A compact entered into by the governed, whose breach releases the other party, is that idea; the rejected options name trade, labor, serfdom and unification, all treated elsewhere in the unit."),
 ("questioned in all areas of life",
  "KC-5.3.I says the thought questioned established traditions IN ALL AREAS OF LIFE. Religion is one area within that scope rather than its boundary, which is why the same sentence stands behind political, social and economic criticism in this unit."),
 ("spread beyond the settings in which it first appeared",
  "KC-5.3.I pairs the RISE with the DIFFUSION of Enlightenment thought. Diffusion is what lets one body of thought be connected to revolutions and rebellions in several places; rise alone would report origin without reach."),
 ("The abolition of slavery",
  "KC-5.3.I.C names the abolition of slavery among the expansions of rights reform movements contributed to, and the same sentence names religious ideals alongside Enlightenment ideas as influences, which is the pair of premises the source argues from."),
 ("named alongside expanded suffrage and the abolition of slavery",
  "KC-5.3.I.C places the end of serfdom on the RESULT side of the sentence, listed with expanded suffrage and the abolition of slavery. The anchor carries both the placement and the companions because a distractor moves it to the cause side."),
 ("intellectual and ideological context",
  "Unit 5 Learning Objective A asks students to explain the intellectual and ideological context in which revolutions swept the Atlantic world from 1750 to 1900. The rejected options are verbatim the learning objectives of topics 5.5, 5.3, 5.6 and 5.9."),
 ("More pamphlets in the sample treat natural rights and the social contract than treat the role of religion",
  "Recomputed in q20 above from the table alone: seventy two against fifty four, with the reversed comparison, the court-ceremony claim and the all-political claim each checked false on the same counts. The two leading subjects are those KC-5.3.I.A names, natural rights and the social contract on one side and the role of religion in public life on the other. The anchor carries both sides of the comparison because a distractor reverses it."),
 ("The second argues from reason and evidence while the first argues from the age of a custom",
  "KC-5.3.I.A makes reason and empiricist approaches the mark of Enlightenment argument and KC-5.3.I describes established traditions being questioned; suggested skill 3.A is identifying the claim a source advances. The anchor is the full two-clause sentence because one distractor exchanges the two sources."),
 ("before and outside the grant",
  "KC-5.3.I.A names natural rights among the new political ideas. A right held by a person as a person is not conferred by the authority it is asserted against, which is what separates it from a privilege granted by a crown and what makes it usable against existing political authority."),
 ("supplies a standard the ruler can fail",
  "KC-5.3.I.A names the social contract and KC-5.3.I describes such thought questioning established traditions and often preceding rebellion. Authority resting on agreement can be measured against that agreement, which is the property that makes the idea available to critics."),
 ("continued to be defended even as new ways of understanding questioned them",
  "KC-5.3.I describes traditions being QUESTIONED, not abolished at a stroke, while KC-5.3.I.A describes new approaches being applied. The reasoning process assigned to this topic is continuity and change, so the answer has to hold both together."),
 ("demands for women's suffrage and an emergent feminism",
  "KC-5.3.IV.B presents women's suffrage as demanded against standing hierarchies, which is language of contest. KC-5.3.I.C's expanded suffrage says nothing about whom the expansion reached, so it is KC-5.3.IV.B that complicates an assumption of automatic extension."),
 ("the reform movements that expanded suffrage",
  "The petition argues FROM the ideas of KC-5.3.I.A and FOR the expanded suffrage of KC-5.3.I.C, so it sits at the join between them. The rejected pairs are industrial and economic statements from KC-5.1 and KC-5.2 and do not touch the franchise."),
 ("across several decades and drawing on the same body of ideas",
  "Unit 5 Learning Objective B concerns how the Enlightenment affected societies OVER TIME, and KC-5.3.I.C attributes reform movements and their expansions of rights to those ideas. A run of movements across decades exhibits that duration; a single document at one moment cannot."),
 ("religious ideals as well as Enlightenment ideas",
  "KC-5.3.I.C names religious ideals alongside Enlightenment ideas as influences on reform movements, so a religious argument feeding an abolition campaign is that statement in operation. Nothing in the framework makes the two kinds of argument exclusive."),
 ("often preceded rebellions rather than that it always caused them",
  "KC-5.3.I's own hedges are the point: the thought OFTEN PRECEDED revolutions and rebellions. Precedence in time plus the word often falls short of universal causation, and reading the framework's qualifications is part of reasoning honestly from it."),
 ("questioned traditions and shaped later reform and revolt",
  "The summary joins KC-5.3.I.A's new ways of understanding and new political ideas, KC-5.3.I's questioning of traditions and precedence over revolt, and KC-5.3.I.C's later reform movements. The rejected options relocate the Enlightenment into the arts, industry, church settlement or trade policy."),
]

TABLE_CHECKS = {13: q13, 20: q20}

wh.run(w5_1, CLAIMS, TABLE_CHECKS, sys.argv)
