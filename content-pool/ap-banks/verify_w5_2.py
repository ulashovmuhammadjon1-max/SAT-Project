"""Key audit for AP WORLD HISTORY: MODERN 5.2 Nationalism and Revolutions in the
Period from 1750 to 1900.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim cites the Key Concept or Learning
Objective the key traces to.

WHAT THE KEYS REST ON
---------------------
KC-5.3 (the 18th century began an intense period of revolution and rebellion
leading to new nation-states around the world), KC-5.3.II.ii (a new sense of
commonality based on language, religion, social customs, and territory,
SOMETIMES harnessed by governments), KC-5.3.II.iii (newly imagined national
communities linked identity with the borders of the state; nationalists
challenged boundaries or sought unification of fragmented regions),
KC-5.3.III.B (rebellions by colonial subjects in the Americas inspired by
democratic ideals; the American Revolution as a model for a number of those that
followed; three movements facilitating independent states in the Americas),
KC-5.3.I.B (three named revolutionary documents, each paired by the framework
with its revolution) and KC-5.3.IV.A.i (discontent with monarchist and imperial
rule encouraged democracy and 19th-century liberalism). Items 15 to 19 key to
the illustrative examples printed beside KC-5.3.II.iii.

WHAT THEY DELIBERATELY DO NOT REST ON
-------------------------------------
This is the topic where writing from general knowledge would be easiest, so the
line is drawn hard. NO item quotes any of the three named documents -- inventing
a quotation and attributing it to a real document is fabrication, and every
quoted stimulus in the module is explicitly illustrative and unattributed. No
item asks for the date of a revolution, the name of a leader the CED does not
print, or the content of a document beyond the pairing the framework itself
supplies. The only centuries named are the framework's own.

SWAP ANCHORS
------------
Items 6, 22 and 23 carry a distractor that is the key with its two clauses
exchanged: the model and its imitators reversed, cause and effect reversed, and
a comparison of two counts reversed. Each of those anchors carries BOTH clauses,
because an anchor naming one clause alone matches the swap too -- the defect
found in verify_e2_1.py. The key-rotation control below requires all thirty keys
to fail when moved one place, which is what tests it.

FIVE choices per item (A-E); see HISTORY_BRIEF.md.
"""
import sys

import cg_check as cg
import wh_check as wh
import w5_2

BASIS_COL = "Basis of its appeal to commonality"
COUNT_COL = "Number of societies in the sample"


def q21(table, item):
    """Each row appeals to a different one of the four bases KC-5.3.II.ii names."""
    labels = cg.labels(table)
    assert labels == ["Movement 1", "Movement 2", "Movement 3", "Movement 4"], (
        f"the four rows must be the four illustrative movements; got {labels}"
    )
    bases = {"language": "language", "religion": "religion",
             "territory": "territory", "customs": "social customs"}
    found = {}
    for lab, row in zip(labels, table["rows"]):
        text = str(row[1]).lower()
        hits = [name for key, name in bases.items() if key in text]
        assert len(hits) == 1, f"{lab} must appeal to exactly one named basis; got {hits}"
        found[lab] = hits[0]
    assert len(set(found.values())) == 4, (
        f"the four rows must take four DIFFERENT bases, so 'all four appeal to the same "
        f"basis' is false; got {found}"
    )
    assert "territory" in found.values(), "'none appeals to territory' must be false"
    religion_rows = [lab for lab, b in found.items() if b == "religion"]
    assert len(religion_rows) == 1, "'every appeal rests on a shared religion' must be false"
    return (f"read from the table alone: the four rows appeal to {sorted(found.values())}, "
            f"which are four different bases and not one repeated")


def q23(table, item):
    """The keyed comparison and every distractor recomputed from the counts."""
    counts = dict(zip(cg.labels(table), cg.col(table, COUNT_COL)))
    total = sum(counts.values())
    assert total == 60, f"the stem says sixty societies; the column sums to {total}"
    indep = counts["Independence from an imperial ruler"]
    unify = counts["Unification of fragmented regions into one state"]
    redraw = counts["Redrawing of an existing boundary"]
    none = counts["No change to existing arrangements"]
    assert indep > unify, "the key requires more demanding independence than unification"
    assert none < max(counts.values()), "'most demand no change' must be false"
    assert none != max(counts.values()), "the no-change row must not be the largest"
    assert redraw > 0, "'no society makes any demand about a boundary' must be false"
    assert redraw < total, "'every society sought a redrawn boundary' must be false"
    return (f"recomputed from the table: {indep:.0f} demand independence against "
            f"{unify:.0f} demanding unification, {redraw:.0f} a redrawn boundary and "
            f"{none:.0f} no change, summing to {total:.0f}")


CLAIMS = [
 ("social customs, and territory",
  "KC-5.3.II.ii, near verbatim: people around the world developed a new sense of commonality based on language, religion, social customs, and territory. The rejected sets are the industrial resources of KC-5.1.I.A, the labor demands of KC-5.1.V.A, the finance of KC-5.1.III.B and the technologies of KC-5.1.I.E."),
 ("harnessed the new sense of commonality to foster unity",
  "KC-5.3.II.ii's closing clause: this was SOMETIMES harnessed by governments to foster a sense of unity. The framework has a government using a sentiment that already exists, which is neither the sentiment destroying the state nor the state producing it from nothing."),
 ("new nation-states around the world",
  "KC-5.3, near verbatim: the 18th century marked the beginning of an intense period of revolution and rebellion against existing governments, leading to the establishment of new nation-states around the world. The phrase around the world is what makes the outcome global."),
 ("19th-century liberalism",
  "KC-5.3.IV.A.i names democracy and 19th-century liberalism as the ideologies encouraged by discontent with monarchist and imperial rule. The framework's other ideological statement, KC-5.3.IV.A.ii, names socialism and communism, which is why those are not the pair here."),
 ("Democratic ideals",
  "KC-5.3.III.B opens by stating that colonial subjects in the Americas led a series of rebellions inspired by democratic ideals. The rejected options name industrial and labor developments the framework places under KC-5.1 and does not attach to these rebellions."),
 ("a model and inspiration for a number of the revolutions that followed",
  "KC-5.3.III.B, near verbatim: the American Revolution, and its successful establishment of a republic, was a model and inspiration for a number of the revolutions that followed. The anchor carries both the model and the followers because a distractor exchanges them."),
 ("the Haitian Revolution, and the Latin American independence movements",
  "KC-5.3.III.B names exactly the American Revolution, the Haitian Revolution and the Latin American independence movements as facilitating the emergence of independent states in the Americas. The rejected sets come from the European unifications, the reform programs of KC-5.1.V.B and KC-5.2.II.A, and the reform outcomes of KC-5.3.I.C."),
 ("Declaration of the Rights of Man and of the Citizen, and the Letter from Jamaica",
  "KC-5.3.I.B names the three revolutionary documents in which the ideas of Enlightenment philosophers were reflected. The rejected sets substitute titles the framework places under economics, reform demands and later ideologies."),
 ("The American Revolution",
  "KC-5.3.I.B pairs each document with a revolution and names the American Declaration of Independence during the American Revolution. The pairing is printed, so the key does not rest on outside knowledge of who drafted the text."),
 ("The French Revolution",
  "KC-5.3.I.B names the French Declaration of the Rights of Man and of the Citizen during the French Revolution. Each of the three documents in that statement is attached by the framework to one revolution."),
 ("The Letter from Jamaica",
  "KC-5.3.I.B places Bolivar's Letter from Jamaica on the eve of the Latin American revolutions. On the eve is the framework's own placement in time, so no date has to be supplied from outside the CED."),
 ("resistance to existing political authority, often in pursuit of independence",
  "KC-5.3.I.B closes with that effect exactly: the documents influenced resistance to existing political authority, often in pursuit of independence and democratic ideals. They are instruments of resistance in the framework, not records written afterwards."),
 ("linked it with the borders of the state",
  "KC-5.3.II.iii states that newly imagined national communities often linked this new national identity with borders of the state. That link is what makes the following clause possible, in which nationalists challenge boundaries or seek unification."),
 ("unification of fragmented regions",
  "KC-5.3.II.iii states that in some cases nationalists challenged boundaries or sought unification of fragmented regions, and KC-5.3.II.ii names language among the bases of commonality. The rejected options belong to KC-5.3.II.ii's second clause, KC-5.3.III.B, KC-5.1.V.A and KC-5.1.V.C."),
 ("German and Italian unifications",
  "The illustrative examples printed beside KC-5.3.II.iii, under calls for national unification or liberation, name the German and Italian unifications. The rejected pairs come from KC-5.3.III.B, KC-5.1.V.C, KC-5.2.II.A, KC-5.3.I.C and KC-5.1.III.B."),
 ("Propaganda Movement",
  "The illustrative examples printed beside KC-5.3.II.iii name the Propaganda Movement in the Philippines. Only one of the five options appears on the framework's own list for this topic, which is what the item tests."),
 ("Maori nationalism",
  "The illustrative examples printed beside KC-5.3.II.iii name Maori nationalism and the New Zealand wars in New Zealand. The other four options are on the same list but belong to Southeast Asia, southeastern Europe, the Ottoman Empire and the Italian peninsula."),
 ("Lola Rodriguez de Tio",
  "The illustrative examples printed beside KC-5.3.II.iii name Puerto Rico and the writings of Lola Rodriguez de Tio. The rejected names are the illustrative examples for topic 5.1, printed beside KC-5.3.IV.B under demands challenging political and gender hierarchies."),
 ("Balkan nationalisms and Ottomanism",
  "The illustrative examples printed beside KC-5.3.II.iii list Balkan nationalisms and Ottomanism together among the calls for national unification or liberation. The rejected pairs come from other regions on that list or from KC-5.3.III.B and KC-5.3.I.C."),
 ("grounds nationhood in one of the bases of commonality",
  "KC-5.3.II.ii names language, religion, social customs, and territory as the bases of the new sense of commonality; the two manifestos take the first and the last. Suggested skill 3.C for this topic is comparing the main ideas of two sources, which is what the shared ground makes visible."),
 ("Each of the four appeals to one of the bases",
  "KC-5.3.II.ii's four bases, checked against the table in q21 above: the four rows take four different bases, so the claims that all four share one basis, that territory is absent, and that every appeal is religious are each false on the table itself."),
 ("Discontent with monarchist and imperial rule encouraged the development of the ideologies",
  "KC-5.3.IV.A.i puts discontent on the causal side: discontent with monarchist and imperial rule encouraged the development of systems of government and various ideologies. The reasoning process for this topic is causation, so the anchor carries both cause and effect because a distractor reverses them."),
 ("demand independence from an imperial ruler than demand unification",
  "The two courses of KC-5.3.II.iii and KC-5.3.III.B, counted in q23 above: twenty six against eighteen. The anchor carries both sides of the comparison because a distractor reverses it, and every other option is checked false against the same counts."),
 ("Enlightenment philosophers reflected in revolutionary documents",
  "KC-5.3.I.B states that the ideas of Enlightenment philosophers, as reflected in revolutionary documents, influenced resistance to existing political authority, often in pursuit of independence. The rejected options are industrial and economic statements from KC-5.1."),
 ("a model for a number of the revolutions that followed, not for all of them",
  "KC-5.3.III.B says a number of the revolutions that followed. The quantifier is the framework's own limit, and reading such limits is what keeps a key inside the CED rather than beyond it."),
 ("newly constructed rather than inherited unchanged",
  "KC-5.3.II.iii speaks of NEWLY IMAGINED national communities, and KC-5.3.II.ii describes the sense of commonality itself as newly developed. The adjective marks the construction of the identity, which the framework then ties to real borders."),
 ("nationalists taking toward the borders of the state",
  "KC-5.3.II.iii states that nationalists challenged boundaries or sought unification of fragmented regions, and KC-5.3 names new nation-states as the outcome. Separation and unification act on the same link between identity and borders, which is the comparison suggested skill 3.C asks for."),
 ("emergence of independent states in the Americas",
  "KC-5.3.III.B states that the American Revolution, the Haitian Revolution and the Latin American independence movements facilitated the emergence of independent states in the Americas. The rejected effects belong to KC-5.1.II.B, KC-5.1.III.B and KC-5.1.V.B."),
 ("causes of the rebellion and how widely they were felt",
  "Unit 5 Learning Objective C asks students to explain causes and effects of the various revolutions in the period from 1750 to 1900, so the causes and their reach are the evidence at issue. The rejected options gather facts that leave the question of cause untouched."),
 ("drove revolts that produced new nation-states",
  "The summary joins KC-5.3.II.ii's new sense of commonality, KC-5.3.IV.A.i's discontent with monarchist and imperial rule, and KC-5.3's establishment of new nation-states around the world. Each rejected option contradicts one of those three or relocates the account into industry."),
]

TABLE_CHECKS = {21: q21, 23: q23}

wh.run(w5_2, CLAIMS, TABLE_CHECKS, sys.argv)
