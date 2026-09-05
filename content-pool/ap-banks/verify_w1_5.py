"""Key audit for AP WORLD HISTORY: MODERN 1.5 (Unit 1, State Building in Africa).

WHY THIS FILE EXISTS AT ALL, WRITTEN AFTER THE FACT
---------------------------------------------------
`w1_5.py` was committed with thirty questions and NO verifier: the agent
authoring it was stopped mid-topic, so the module shipped with no gate of any
kind -- no anchor pinning any key to its own text, no notation check, no
citation check, no table arithmetic. `HISTORY_BRIEF.md` records that "a stopped
agent leaves damage, not just absence", and an ungated module is precisely that
damage. Every question below was therefore re-read against the CED before this
file was written, and the CED sentence each key rests on is stated here in the
claim so a later reader can check the history rather than take it on trust.

WHAT THE KEYS REST ON -- THIS TOPIC'S CED PAGE IS UNUSUALLY THIN
-----------------------------------------------------------------
The topic page for 1.5 carries exactly one learning objective, one historical
development and one thematic focus block:

  Unit 1 Learning Objective J  Explain how and why states in Africa developed
                   and changed over time.
  KC-3.2.I.D.ii    In Africa, as in Eurasia and the Americas, state systems
                   demonstrated continuity, innovation, and diversity and
                   expanded in scope and reach.
  Thematic focus GOV  A variety of internal and external factors contribute to
                   state formation, expansion, and decline. Governments
                   maintain order through a variety of administrative
                   institutions, policies, and procedures, and governments
                   obtain, retain, and exercise power in different ways and for
                   different purposes.
  Illustrative examples  Great Zimbabwe, Ethiopia, the Hausa kingdoms.

Two further CED sentences are cited where they bear on Africa, and both were
checked in the framework text rather than recalled:

  KC-3.1.III.D.iii (Unit 1 LO D)  Islam, Judaism, Christianity, and the core
                   beliefs and practices of these religions continued to shape
                   societies in Africa and Asia.
  KC-3.1.I.E.ii (Unit 2 LO I)     The expansion of empires, including Mali in
                   West Africa, facilitated Afro-Eurasian trade and
                   communication as new people were drawn into the economies
                   and trade networks.

Because the page is that thin, NO key here asserts a fact about Great Zimbabwe,
Ethiopia or the Hausa kingdoms: the framework names them as illustrative and
asserts nothing further about them, so a key resting on one would rest on the
author's memory instead of on the CED. That is the rule the brief states and it
is the reason this module reads as reasoning rather than as recall.

WHERE THE ANCHOR CARRIES TWO CLAUSES, AND WHY
---------------------------------------------
Several distractors here are the SWAP of the key rather than an unrelated
claim, and an anchor naming one clause would match the swap as well:

  q4   scope (new functions) against reach (new territory)
  q7   innovation in administration against continuity in administration
  q12  the doubling kingdom smallest against largest at the earlier date
  q23  extent covered / what it could do, exchanged
  q26  regulating more within existing territory / adding new territory
  q27  a crisis at the center interrupting tribute, against the reverse

Those anchors carry both clauses in order, which is the defect `verify_e2_1.py`
shipped and `HISTORY_BRIEF.md` records.

DATA QUESTIONS
--------------
Items 11, 12 and 13 carry tables. Every number is HYPOTHETICAL and each stem
says so, because the CED prints no figures for African states and inventing one
and presenting it as a record would be a fabrication a student would read as
fact. Each keyed conclusion is recomputed below from the table alone AND every
distractor is shown false against the same numbers, so the key is reachable
from the data without prior knowledge -- which is how the exam's stimulus sets
work.

The control prints a per-question catch rate for the corrupted cells and q11's
is deliberately the lowest of the three. That is not a weak check: q11's keyed
conclusion is that two rankings DIFFER, and tripling one wall length usually
leaves them differing, so the conclusion is still true and a check that
complained would be testing the numbers rather than the claim. The corruptions
that DO flip the conclusion -- the ones that make the two rankings agree -- are
caught. A zero would mean the check had stopped reading the table; a number
below the total means only that some corruptions leave the key sound.

NEGATIVE CONTROL: `python3 verify_w1_5.py --selftest`.
"""
import sys

import cg_check as cg
import w1_5
import wh_check

WALL = "Enclosure wall length in paces"
PENS = "Cattle pens recorded"
EARLY_D = "Districts governed at an earlier date"
LATE_D = "Districts governed at a later date"
EARLY_H = "Holders recorded in an earlier reign"
LATE_H = "Holders recorded in a later reign"


def q11(table, item):
    """Ranking by wall length and by pens must give DIFFERENT orders."""
    wall, pens = cg.col(table, WALL), cg.col(table, PENS)
    by_wall = cg.ranked(table, WALL)
    by_pens = cg.ranked(table, PENS)
    assert by_wall != by_pens, f"the two rankings must differ: {by_wall} vs {by_pens}"
    longest = by_wall[0]
    assert cg.cell(table, longest, PENS) != max(pens), \
        f"the longest wall must NOT hold the most pens; {longest} does"
    # every distractor false on the same numbers
    shortest = by_wall[-1]
    assert cg.cell(table, shortest, PENS) != min(pens), \
        "'the shortest wall has the fewest pens' must be false"
    longest_pens = cg.cell(table, longest, PENS)
    assert not all(p > longest_pens for p in pens), \
        "'every settlement has more pens than the longest-walled one' must be false"
    assert any(w != p for w, p in zip(wall, pens)), \
        "'wall length equals pens everywhere' must be false"
    return (f"wall order {by_wall} differs from pen order {by_pens}; the longest wall "
            f"holds {longest_pens} pens against a maximum of {max(pens)}")


def q12(table, item):
    """Two kingdoms grow, one is level, and the doubler is the SMALLEST early."""
    early, late = cg.col(table, EARLY_D), cg.col(table, LATE_D)
    names = cg.labels(table)
    grew = [i for i in range(len(early)) if late[i] > early[i]]
    level = [i for i in range(len(early)) if late[i] == early[i]]
    fell = [i for i in range(len(early)) if late[i] < early[i]]
    assert len(early) == 3 and len(grew) == 2 and len(level) == 1, \
        f"key needs two growing and one level of three; grew={grew} level={level}"
    assert not fell, "'at least one kingdom governed fewer' must be false"
    doubled = [i for i in range(len(early)) if late[i] == 2 * early[i]]
    assert len(doubled) == 1, f"exactly one kingdom must exactly double; got {doubled}"
    d = doubled[0]
    assert early[d] == min(early), \
        f"the doubling kingdom must be SMALLEST at the earlier date: {names[d]} has {early[d]}"
    assert early[d] != max(early), "'the doubler was the largest earlier' must be false"
    biggest_early = early.index(max(early))
    ratios = [late[i] / early[i] for i in range(len(early))]
    assert ratios[biggest_early] != max(ratios), \
        "'the largest kingdom earlier grew by the largest multiple' must be false"
    assert not all(late[i] > early[i] for i in range(len(early))), \
        "'all three grew' must be false"
    return (f"earlier {early} and later {late}: {len(grew)} grew, {len(level)} level, "
            f"and the doubler {names[d]} starts at {early[d]}, the smallest")


def q13(table, item):
    """Two of three offices grow; the treasury triples and no other office does."""
    early, late = cg.col(table, EARLY_H), cg.col(table, LATE_H)
    treasury_e = cg.cell(table, "Office of the treasury", EARLY_H)
    treasury_l = cg.cell(table, "Office of the treasury", LATE_H)
    rose = [i for i in range(len(early)) if late[i] > early[i]]
    assert len(early) == 3 and len(rose) == 2, f"exactly two of three must rise; got {rose}"
    assert treasury_l == 3 * treasury_e, \
        f"the treasury must triple: {treasury_e} to {treasury_l}"
    tripled = [i for i in range(len(early)) if late[i] == 3 * early[i]]
    assert len(tripled) == 1, f"only the treasury may triple; tripling offices {tripled}"
    # every distractor false on the same numbers
    assert not all(late[i] > early[i] for i in range(len(early))), \
        "'every office rose' must be false"
    frontier_e = cg.cell(table, "Office of the frontier", EARLY_H)
    frontier_l = cg.cell(table, "Office of the frontier", LATE_H)
    assert not frontier_l > frontier_e, "'the frontier office rose' must be false"
    court_e = cg.cell(table, "Office of the court", EARLY_H)
    court_l = cg.cell(table, "Office of the court", LATE_H)
    assert not court_l > 2 * court_e, "'the court office more than doubled' must be false"
    assert not any(late[i] < early[i] for i in range(len(early))), \
        "'every office recorded fewer' must be false"
    return (f"earlier {early} and later {late}: two offices rise, the treasury goes "
            f"{treasury_e} to {treasury_l} and is the only one to triple")


TABLE_CHECKS = {11: q11, 12: q12, 13: q13}

CLAIMS = [
 ("grew in what they did and in how far their authority ran",
  "KC-3.2.I.D.ii states that in Africa, as in Eurasia and the Americas, state systems demonstrated continuity, innovation, and diversity and expanded in scope and reach. Every clause of the key is that sentence in plainer words, and each rejected option denies one of them: uniformity denies diversity, derivation denies innovation, contraction denies expansion, and incomparability denies the sentence's own opening phrase."),

 ("an instance of a general process rather than as an exception",
  "KC-3.2.I.D.ii opens 'In Africa, as in Eurasia and the Americas', and KC-3.2.I.D.i and KC-3.2.I.A apply the same three terms to the Americas and to Afro-Eurasia. Shared analytic vocabulary is a claim about how the cases are to be analyzed, not a claim of contact, of descent or of identity in size and organization, which is what the four rejected options assert."),

 ("The second, because it gives an account of how a change came about",
  "The suggested skill for this topic is 1.B, explain a historical concept, development, or process, and Learning Objective J asks how and WHY states in Africa developed and changed over time. An explanation supplies the means by which a change occurred; a list of accessions in order supplies only a sequence. The anchor names the paragraph AND the reason because the strongest distractor is the same reason attached to the other paragraph."),

 ("scope of the state, since it has taken on functions",
  "KC-3.2.I.D.ii says state systems expanded in scope AND reach, which are two things, and the Governance thematic focus describes governments maintaining order through administrative institutions, policies, and procedures. In the scenario no new territory is acquired, so the reach option is false on the scenario as well as on the framework's wording; the anchor carries both scope and functions because reach and territory are the swap."),

 ("claim about variation between cases",
  "KC-3.2.I.D.ii asserts diversity among the state systems of Africa, and the Governance thematic focus says governments obtain, retain, and exercise power in different ways and for different purposes. Diversity is a relation between cases, so a single case cannot exhibit it, whatever the quality of the evidence for that case."),

 ("means to attract followers",
  "The Governance thematic focus states that governments obtain, retain, and exercise power in different ways and for different purposes, and KC-3.2.I.D.ii asserts diversity among African state systems. Wealth converted into followers is one of those ways. No key here asserts anything about Great Zimbabwe itself, which the CED names only as an illustrative example."),

 ("innovation in administration that makes the districts answerable to the ruler",
  "KC-3.2.I.D.ii names innovation alongside continuity in African state systems, and the Governance thematic focus names administrative institutions and procedures as how governments maintain order. Replacing inherited district leadership with removable appointees changes who the district answers to, which is the innovation; the anchor carries both the label and the change because the swap distractor keeps the sentence and substitutes continuity."),

 ("disorder anywhere along the route reduces what reaches its own markets",
  "The Governance thematic focus states that a variety of internal and EXTERNAL factors contribute to state formation, expansion, and decline, and KC-3.1.I.E.ii records that the expansion of empires, including Mali in West Africa, facilitated Afro-Eurasian trade and communication as new people were drawn into the economies and trade networks. A revenue that depends on traffic depends on conditions outside the state's own borders."),

 ("use a named case to illustrate it rather than to carry it",
  "The CED states of illustrative examples that they are intended as examples and do not in any way constitute additional, preferred, or required information, and that historical development statements comprise the knowledge required to demonstrate mastery of the learning objective. The required statement for this topic is KC-3.2.I.D.ii and the objective is Learning Objective J. This item replaced a near-duplicate of topic 1.4 q21, which asks for an internal factor and keys a disputed succession in almost the same words."),

 ("carries forward an existing claim to authority while the new office",
  "KC-3.2.I.D.ii lists continuity, innovation, and diversity together as properties of the same state systems rather than as stages that follow one another, and Learning Objective J asks how states developed and changed over time. The anchor carries the old title and the new office together because holding both at once is the whole point."),

 ("longest wall does not have the most pens",
  "Recomputed in q11 above from the table alone, including that each of the four alternatives is false on the same numbers. KC-3.2.I.D.ii asserts diversity among African state systems, and two measures that rank the same settlements in different orders is what variation looks like in data. The figures are hypothetical and the stem says so."),

 ("exactly doubled was the smallest at the earlier date",
  "Recomputed in q12 above from the two columns, distractors included. KC-3.2.I.D.ii says African state systems expanded in scope and reach and were diverse, so growth in some cases and not in all is what the sentence predicts. The anchor carries the doubling AND the starting size because the swap distractor changes only smallest to largest."),

 ("office of the treasury tripled",
  "Recomputed in q13 above from the two columns. The Governance thematic focus names administrative institutions as how governments maintain order, and KC-3.2.I.D.ii's expansion in scope is what a growing establishment in some offices and not others would illustrate."),

 ("may take in more than one center",
  "KC-3.2.I.D.ii uses the phrase 'state systems' of Africa and KC-3.2.I.D.i uses it of the Americas, in both cases alongside diversity, and the Governance thematic focus describes governments maintaining order through a VARIETY of institutions, policies and procedures. The framework's noun is the arrangement of authority, not a roster of named kingdoms."),

 ("an account resting on one cause is likely to be incomplete",
  "The Governance thematic focus states that a VARIETY of internal and external factors contribute to state formation, expansion, and decline, and Learning Objective J asks how and why states in Africa developed and changed over time. A single-cause account is not forbidden but is answerable to that variety."),

 ("written medium for its administration",
  "KC-3.1.III.D.iii states that Islam, Judaism, Christianity, and the core beliefs and practices of these religions continued to shape societies in Africa and Asia, and the Governance thematic focus names administrative institutions and procedures as how governments maintain order. The key claims only what those two sentences support: a tradition present across a wider region could supply learning and a script."),

 ("while leaving their own leadership in place",
  "KC-3.2.I.D.ii says state systems expanded in scope and REACH, and the Governance thematic focus says governments obtain, retain, and exercise power in different ways and for different purposes. Obligation without occupation is one of those ways, and it is why reach and administration are not the same measure."),

 ("governed more districts at the end of a reign",
  "KC-3.2.I.D.ii asserts matters of fact about state systems expanding in scope and reach, and Learning Objective J asks how and why they developed and changed. A count of districts can be checked against evidence; whether an annexation was right, whether obligations were fair, whether one arrangement was superior and whether loyalty was deserved cannot be settled by observation."),

 ("other centers may continue or expand while one declines",
  "KC-3.2.I.D.ii asserts diversity among the state systems of Africa, and the Governance thematic focus names formation, expansion AND decline as parts of one subject. A statement about one center is therefore not a statement about the region, and the framework nowhere makes decline and expansion the same process."),

 ("no earlier ruler of that state had employed",
  "KC-3.2.I.D.ii joins innovation to continuity in a single sentence about African state systems, so an arrangement without a precedent in that state is evidence of the innovation half. A repeated title, an unmoved capital, an unchanged boundary and a claim of descent from the founder each evidence continuity instead."),

 ("not constrained by the given dates",
  "The CED states that events, processes, and developments are not constrained by the given dates and may begin before, or continue after, the period, and KC-3.2.I.D.ii's word continuity presupposes arrangements older than the period's opening. No key in this module turns on a boundary year."),

 ("standing procedure with named responsibility",
  "The Governance thematic focus states that governments maintain order through a variety of administrative institutions, policies, and procedures, and KC-3.2.I.D.ii credits African state systems with expansion in scope. A fixed schedule with a named officer and a stated penalty is a procedure in exactly that sense."),

 ("the first is a claim about the extent it covered and the second about what it was able to do",
  "KC-3.2.I.D.ii names expansion in scope and expansion in reach as two things rather than one, and the Governance thematic focus separates how power is exercised from the extent over which it runs. The anchor carries both halves IN ORDER because the strongest distractor is the same pair exchanged."),

 ("more than one arrangement is consistent with an effective state",
  "The Governance thematic focus states that governments maintain order through a variety of administrative institutions, policies, and procedures, and KC-3.2.I.D.ii asserts diversity among the state systems of Africa. A council and an appointed officer are two of that variety, not one valid method and one invalid one."),

 ("each is strong where the other is weak",
  "Learning Objective J asks students to explain how and why states in Africa developed and changed, which requires weighing sources rather than ranking them by type, and the Governance thematic focus is the content, since an administrative record is the product of the institutions it names. Neither kind of source is true or false by category."),

 ("regulate more aspects of life within the territory it already held, rather than adding new territory",
  "KC-3.2.I.D.ii pairs expansion in scope with expansion in reach, and the Governance thematic focus describes governments maintaining order through institutions and procedures. Depth is the scope half. The anchor carries both halves because the strongest distractor is the same pair exchanged."),

 ("obedience in the district depended in part on the center's ability to act",
  "The Governance thematic focus names internal factors among those contributing to state expansion and decline, and KC-3.2.I.D.ii speaks of reach. The anchor carries the DIRECTION of the relation, from the center outward, because one distractor reverses cause and effect and would match an anchor naming only the two events."),

 ("rather than naming any particular institution",
  "KC-3.2.I.D.ii applies continuity, innovation and diversity to Africa as KC-3.2.I.D.i does to the Americas and KC-3.2.I.A to Afro-Eurasia. The three terms describe patterns of change and variation, which is why one vocabulary covers institutionally unlike cases without asserting that the cases are alike."),

 ("internal as well as external factors",
  "The Governance thematic focus states that a variety of INTERNAL and external factors contribute to state formation, expansion, and decline, and KC-3.2.I.D.ii asserts continuity among African state systems, which is a claim about inherited arrangements. An account admitting only outside influence contradicts both."),

 ("carried inherited arrangements forward while adopting new ones",
  "KC-3.2.I.D.ii is one sentence carrying every element of the key at once: continuity, innovation, diversity, and expansion in scope and reach, in Africa as in Eurasia and the Americas. Learning Objective J asks how and why these states developed and changed over time."),
]

wh_check.run(w1_5, CLAIMS, TABLE_CHECKS, sys.argv)
