"""Key audit for AP WORLD HISTORY: MODERN 1.7 (Unit 1's reasoning topic).

One (anchor, claim) per question, in module order. The anchor is a distinctive
substring of that question's OWN keyed choice and of no distractor; the claim
states the CED sentence the key rests on, with its Key Concept or Learning
Objective code.

WHAT THE KEYS REST ON
---------------------
This is the unit's final topic, and the CED says of every such page that it
"includes key concepts, which summarize the historical developments in the
unit". The page reprints six of them, and those six plus the suggested skill
are what every key here traces to:

  LO 1.N          the similarities AND differences in the processes of state
                  formation from c. 1200 to c. 1450
  skill 6.A       make a historically defensible claim
  KC-3.2          state formation and development demonstrated continuity,
                  innovation, and diversity in various regions
  KC-3.2.I        as the Abbasid Caliphate fragmented, new Islamic political
                  entities emerged, MOST OF WHICH were dominated by Turkic
                  peoples; these states showed continuity, innovation, diversity
  KC-3.2.I.A      the Song used traditional methods of Confucianism and an
                  imperial bureaucracy to maintain AND JUSTIFY its rule
  KC-3.2.I.B.i    the new Hindu and Buddhist states of South and Southeast Asia
  KC-3.2.I.D.i    the Americas, as in Afro-Eurasia: continuity, innovation,
                  diversity, and expansion in scope and reach
  KC-3.2.I.D.ii   Africa, as in Eurasia and the Americas: the same four

KC-3.2.I.B.ii, the Europe sentence, is cited in q24 and is printed on TOPIC 1.6,
not on this page. That is stated in the module header and again in the claim, so
nobody later mistakes it for one of the six this page reprints.

A REASONING TOPIC IS NOT A LICENCE TO KEY REASONING ALONE
----------------------------------------------------------
The temptation in an argumentation topic is to key what makes an argument good
in general, which no CED sentence supports and no reader could check. Every key
below is therefore anchored to something the framework says about THIS unit's
content: q20 turns on the word "most" in KC-3.2.I, q27 on the fact that
KC-3.2.I.D.i and KC-3.2.I.D.ii never compare the two regions' extents, q17 on
the CED's own statement that its dates are approximate.

WHERE THE ANCHOR CARRIES TWO CLAUSES, AND WHY
---------------------------------------------
Three distractors here are the SWAP of the key, so an anchor naming one clause
would match the swap as well:

  q3   which draft asserts the similarity and which the difference, exchanged
  q24  fragmentation "said only of Europe" against "only of the Abbasid case"
  q30  the similarity and the difference, exchanged between the two halves

Those anchors carry both clauses in order.

DATA QUESTIONS
--------------
Items 5, 7 and 11 carry tables of HYPOTHETICAL figures and each stem says so.
Each keyed conclusion is recomputed below from the table alone AND every
distractor is shown false on the same numbers. The control prints a per-question
catch rate for corrupted cells; it is not nine of nine anywhere, because the
label column cannot be corrupted into a contradiction and because a corruption
that leaves the keyed conclusion TRUE must not be caught -- a checker that
complained there would be testing the numbers rather than the claim. A zero
would mean the check had stopped reading its table.

q7's rate is the lowest in this module, at one of nine, and the reason is worth
stating rather than papering over. Its key is a claim of DIFFERENCE between
three states, and the control's corruption multiplies a cell -- which almost
always makes the three states differ MORE, leaving the key true. The single
catch is the one corruption that pulls the balances together. Raising the rate
here would mean adding assertions the key does not depend on, which is how a
check stops being about the question it guards.

NEGATIVE CONTROL: `python3 verify_w1_7.py --selftest`.
"""
import sys

import cg_check as cg
import w1_7
import wh_check

EARLY_P = "Separate polities recorded at an earlier date"
LATE_P = "Separate polities recorded at a later date"
EXAM = "Officials recorded as recruited by examination"
INHERIT = "Officials recorded as inheriting their posts"
CARRIED = "Institutions carried forward from an earlier state"
NEW = "Institutions first recorded in this period"


def q5(table, item):
    """The leading region changes hands, and the total falls."""
    early, late = cg.col(table, EARLY_P), cg.col(table, LATE_P)
    assert early.index(max(early)) != late.index(max(late)), \
        f"the leading region must change: {early} then {late}"
    assert sum(late) < sum(early), \
        f"the total must fall: {sum(early)} to {sum(late)}"
    # every distractor false on the same numbers
    assert not (early.index(max(early)) == late.index(max(late)) and sum(late) > sum(early)), \
        "'the same leader and a rising total' must be false"
    assert not all(late[i] < early[i] for i in range(len(early))), \
        "'every region holds fewer later' must be false"
    assert any(late[i] > early[i] for i in range(len(early))), \
        "'no region holds more later' must be false"
    assert sum(late) != sum(early), "'the same total at both dates' must be false"
    return (f"earlier {early} totalling {sum(early)} against later {late} totalling "
            f"{sum(late)}: the lead passes from region {early.index(max(early)) + 1} to "
            f"region {late.index(max(late)) + 1} while the total falls")


def q7(table, item):
    """The three states differ sharply in the mix, so 'similar ways' fails."""
    exam, inherit = cg.col(table, EXAM), cg.col(table, INHERIT)
    shares = [e / (e + i) for e, i in zip(exam, inherit)]
    assert max(shares) - min(shares) > 0.5, \
        f"the examination share must differ sharply across the states: {shares}"
    assert len(set(shares)) == len(shares), f"no two states may share a balance: {shares}"
    # every distractor false on the same numbers
    assert not all(e > i for e, i in zip(exam, inherit)), \
        "'examination outnumbers inheritance everywhere' must be false"
    assert not all(i > e for e, i in zip(exam, inherit)), \
        "'inheritance outnumbers examination everywhere' must be false"
    assert len(set(shares)) > 1, "'the same balance in all three' must be false"
    assert sum(1 for e in exam if e > 0) > 1, \
        "'only one state records examination recruits' must be false"
    return (f"examination {exam} against inheritance {inherit}: the examination shares "
            f"{[round(x, 2) for x in shares]} span more than half the range")


def q11(table, item):
    """Both kinds everywhere, and the balance differing between regions."""
    carried, new = cg.col(table, CARRIED), cg.col(table, NEW)
    assert all(c > 0 for c in carried) and all(n > 0 for n in new), \
        f"every region must record both kinds: carried {carried}, new {new}"
    shares = [c / (c + n) for c, n in zip(carried, new)]
    assert len(set(shares)) == len(shares), f"the balance must differ everywhere: {shares}"
    # every distractor false on the same numbers
    assert not any(n == 0 for n in new), "'one region records none first recorded' must be false"
    assert len(set(shares)) > 1, "'the same balance in all three' must be false"
    assert not all(n == 0 for n in new), "'no region records any first recorded' must be false"
    assert carried.index(max(carried)) != new.index(max(new)), \
        "'the region with the most carried forward also has the most first recorded' must be false"
    return (f"carried forward {carried} against first recorded {new}: both present in every "
            f"region and the carried-forward shares {[round(x, 2) for x in shares]} all differ")


TABLE_CHECKS = {5: q5, 7: q7, 11: q11}

CLAIMS = [
 ("the balance between the two differed from region to region",
  "KC-3.2 states that state formation and development demonstrated continuity, innovation, and diversity in various regions, and Learning Objective N asks for the similarities AND differences in those processes. Skill 6.A asks for a claim that is defensible, which means arguable and supportable: uniformity contradicts diversity, two of the rejected drafts are unarguable, and one is a judgment of value rather than a historical claim."),

 ("nothing in the evidence could count against it",
  "Suggested skill 6.A for this topic asks for a historically DEFENSIBLE claim, which is a claim an argument could defend against a rival reading. KC-3.2's assertions of continuity, innovation and diversity are all contestable; that states in this period had governments is not, so there is nothing for an argument to do."),

 ("The first asserts a similarity and the second a difference",
  "Learning Objective N asks students to explain the similarities AND differences in the processes of state formation from c. 1200 to c. 1450. KC-3.2.I.A and KC-3.2.I.D.i apply the same three terms to Afro-Eurasia and to the Americas, which is the similarity, while only KC-3.2.I.A names Confucian methods, which is the difference. The anchor carries both halves in order because the strongest distractor exchanges them."),

 ("a claim that all states did one thing runs against it",
  "KC-3.2.I.A names the Song Dynasty of China in particular as utilizing traditional methods of Confucianism and an imperial bureaucracy to maintain and justify its rule, and KC-3.2 asserts diversity in state formation across various regions. A universal claim is defeated by the diversity the framework asserts repeatedly, not by a denial that any state examined its officials."),

 ("is not the region holding the most at the later date, and the three regions together hold fewer",
  "Recomputed in q5 above from the table alone, distractors included. KC-3.2 states that state formation and development demonstrated continuity, innovation, and diversity in various regions, and a falling total beneath a change in which region leads is what a defensible claim of diversity rests on: the regions do not move together. The anchor carries both clauses because the strongest distractor inverts each of them. This question replaced one whose keyed conclusion duplicated topic 2.5 q5."),

 ("as well as on arrangements that had no precedent",
  "KC-3.2 and KC-3.2.I both name continuity, innovation, and diversity together, and KC-3.2.I.D.i and KC-3.2.I.D.ii repeat the same terms of the Americas and of Africa. A thesis of pure novelty drops continuity and a thesis of pure preservation drops innovation; the framework asserts both at once, which is what the revision restores."),

 ("differ sharply in how their officials came to hold office",
  "Recomputed in q7 above from the two columns. KC-3.2 asserts diversity in state formation across various regions and KC-3.2.I.A names an imperial bureaucracy as a method of one dynasty in particular, so figures pointing in opposite directions support a claim of difference rather than one of similarity."),

 ("combined them in different measures rather than choosing one or the other",
  "KC-3.2 states that state formation and development demonstrated continuity, innovation, and diversity in various regions, and KC-3.2.I says the same of the new Islamic political entities. The framework lists the three properties together rather than as alternatives, which is why a state may show any combination of them."),

 ("most of them dominated by Turkic peoples",
  "KC-3.2.I states that as the Abbasid Caliphate fragmented, new Islamic political entities emerged, most of which were dominated by Turkic peoples, and that these states demonstrated continuity, innovation, and diversity. The key restates that sentence and each rejected option contradicts a part of it."),

 ("New Hindu and Buddhist states emerged there",
  "KC-3.2.I.B.i states that state formation and development demonstrated continuity, innovation, and diversity, including the new Hindu and Buddhist states that emerged in South and Southeast Asia. KC-3.2.I attaches Turkic domination to the entities emerging from the Abbasid fragmentation, which is a different case in a different sentence."),

 ("records institutions of both kinds, and the balance between them differs",
  "Recomputed in q11 above from the table alone. KC-3.2 names continuity, innovation, and diversity together as properties of state formation in various regions, and both kinds present everywhere in differing proportions is exactly that combination expressed in figures."),

 ("why that shared feature does not collapse the differences",
  "KC-3.2 asserts continuity, innovation, AND diversity together, so the strongest objection to a claim of difference between regions is the framework's own claim of a shared pattern, and Learning Objective N asks for similarities and differences together. Meeting that objection strengthens the claim; restating it in stronger words does not."),

 ("evidence from each region bearing on what growing in scope and in reach consisted of",
  "KC-3.2.I.D.i and KC-3.2.I.D.ii state of the Americas and of Africa that state systems demonstrated continuity, innovation, and diversity, and expanded in scope and reach. Skill 6.A asks for a defensible claim, which needs a ground and evidence rather than more cases, an evaluation, or a date the two regions happen to share."),

 ("but only the former is described as justifying its rule",
  "KC-3.2.I.A and KC-3.2.I.D.ii both apply continuity, innovation and diversity, which is the similarity, while only KC-3.2.I.A adds that the Song used Confucian methods and an imperial bureaucracy to maintain AND JUSTIFY its rule, which is the difference. Learning Objective N asks for a relation between cases rather than for two descriptions in sequence."),

 ("without singling out any one driver",
  "KC-3.2 names continuity, innovation, and diversity in state formation across various regions, and the Governance thematic focus states that a variety of internal and external factors contribute to state formation, expansion, and decline. A single-driver claim is not forbidden but is answerable to that variety, which is what a student defending it must be ready for."),

 ("continuity in state formation can survive a break in the ruling line",
  "KC-3.2 states that state formation and development demonstrated continuity, innovation, and diversity, and the Governance thematic focus names administrative institutions, policies, and procedures as how governments maintain order. The framework attaches continuity to those arrangements rather than to an unbroken line of descent."),

 ("must have begun after 1200, since the period opens there",
  "The CED states that events, processes, and developments are not constrained by the given dates and may begin before, or continue after, the period. KC-3.2's word continuity presupposes arrangements older than the period's opening, so the indefensible claim is the one that treats the opening year as a barrier."),

 ("asserts variation rather than sameness",
  "KC-3.2, KC-3.2.I, KC-3.2.I.A, KC-3.2.I.B.i, KC-3.2.I.D.i and KC-3.2.I.D.ii all name continuity, innovation, AND DIVERSITY together. A vocabulary whose third term is diversity cannot be evidence that the regions it is applied to were the same."),

 ("dues rendered from a district that had rendered none before",
  "KC-3.2.I.D.i and KC-3.2.I.D.ii name expansion in scope and expansion in reach as two different things, and KC-3.2 joins continuity to innovation. Dues arriving from a district that owed none before is authority reaching further, while each rejected pairing attaches its evidence to the wrong half of one of those two distinctions."),

 ("a draft covering all of them asserts more than the sentence it rests on",
  "KC-3.2.I states that as the Abbasid Caliphate fragmented, new Islamic political entities emerged, MOST OF WHICH were dominated by Turkic peoples. A defensible claim matches the quantifier of the sentence it rests on. One rejected option reaches the same draft by a rule of thumb about the word most, which is the right answer for a reason that is not a defence."),

 ("compared across regions in a way a list of names cannot",
  "Learning Objective N asks students to explain the similarities and differences in the PROCESSES of state formation from c. 1200 to c. 1450, and KC-3.2 describes those processes as showing continuity, innovation, and diversity. A process is the thing the objective makes comparable across regions."),

 ("assigns no reasons at all",
  "KC-3.2.I.D.i and KC-3.2.I.D.ii state in parallel words that state systems in the Americas and in Africa demonstrated continuity, innovation, and diversity, and expanded in scope and reach. Neither sentence supplies a cause, so a claim about opposite reasons has nothing in this unit's key concepts to rest on."),

 ("two arrangements answering the same need",
  "KC-3.2 names diversity as the third of the three terms it applies to state formation across various regions, and the Governance thematic focus states that governments maintain order through a variety of administrative institutions, policies, and procedures and exercise power in different ways and for different purposes."),

 ("the shared word covers different outcomes",
  "KC-3.2.I states that as the Abbasid Caliphate fragmented, new Islamic political entities emerged, most of which were dominated by Turkic peoples, while KC-3.2.I.B.ii -- printed on topic 1.6 and NOT among the concepts this page reprints -- states that Europe was politically fragmented and characterized by decentralized monarchies, feudalism, and the manorial system. One word, two different consequences in the framework's own text."),

 ("to every region of the world",
  "Skill 6.A asks for a historically DEFENSIBLE claim, and KC-3.2 confines its own assertion to various regions rather than to all of them. Stretching a claim past the evidence that covers it makes it harder to defend, while naming its scope, saying what would count against it and citing its source all make defence easier."),

 ("repeated assertion of diversity alongside continuity and innovation",
  "KC-3.2, KC-3.2.I, KC-3.2.I.A, KC-3.2.I.B.i, KC-3.2.I.D.i and KC-3.2.I.D.ii each name DIVERSITY beside continuity and innovation. That repeated word is what a claim of predominant likeness must answer; the bare use of a shared vocabulary is not, since one of the shared terms is diversity itself."),

 ("expanded further in scope and reach than those of the Americas",
  "KC-3.2.I.D.i and KC-3.2.I.D.ii assert the expansion of the Americas and of Africa in the same words and never compare the two extents with each other. A claim that one expanded FURTHER than the other adds a comparison of magnitude the framework does not make anywhere."),

 ("the general claim carrying the argument and the case supporting it",
  "KC-3.2 states that state formation and development demonstrated continuity, innovation, and diversity in various regions, which is the general claim, and skill 6.A asks for a defensible claim rather than for a narrative. One case can illustrate a general assertion without establishing it and without having to be typical in every respect."),

 ("showed continuity, innovation and diversity",
  "KC-3.2 asserts that state formation and development demonstrated continuity, innovation, and diversity in various regions, and KC-3.2.I.A, KC-3.2.I.B.i, KC-3.2.I.D.i and KC-3.2.I.D.ii repeat the three terms of Afro-Eurasia, of South and Southeast Asia, of the Americas and of Africa in turn. None of the four rejected uniformities is asserted anywhere in the framework."),

 ("alike in showing continuity, innovation and diversity everywhere, and unlike in the particular arrangements",
  "KC-3.2 states that state formation and development demonstrated continuity, innovation, and diversity in various regions, and Learning Objective N asks for the similarities AND the differences in those processes. The key names one of each, which is what the objective requires; the anchor carries both because the summary would be half an answer with either clause removed."),
]

wh_check.run(w1_7, CLAIMS, TABLE_CHECKS, sys.argv)
