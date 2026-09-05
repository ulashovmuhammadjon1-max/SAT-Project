"""Key audit for AP WORLD HISTORY: MODERN 1.4 State Building in the Americas.

One (anchor, claim) per question, in module order. The anchor is a distinctive
substring of that question's own keyed choice and of no distractor; the claim
names the CED sentence the key rests on.

WHAT THE KEYS REST ON, AND WHAT THEY DELIBERATELY DO NOT
--------------------------------------------------------
This topic's CED page carries one learning objective and one key concept
sentence:

  LO 1.I         how and why states in the Americas developed and changed over
                 time
  KC-3.2.I.D.i   in the Americas, AS IN AFRO-EURASIA, state systems demonstrated
                 continuity, innovation, and diversity, and expanded in scope and
                 reach
  the Governance thematic focus: internal AND external factors contribute to
                 state formation, expansion, and decline; governments maintain
                 order through administrative institutions, policies and
                 procedures; they obtain, retain and exercise power in different
                 ways and for different purposes

No key here asserts a fact about the Mexica, the Inca, Cahokia or the Maya
city-states beyond their being named as illustrative examples, because the
framework asserts none. The alternative to that restraint would have been to
fill the topic from memory, which is the failure `HISTORY_BRIEF.md` and
`MISSION.md` both forbid: a key that traces to the author's knowledge cannot be
checked by anyone reading the bank later.

What carries the bank instead is the suggested skill, 3.B, identify the
evidence used in a source to support an argument. Two thirds of these items
print an unattributed account, state an argument, and ask which observation
does the supporting work -- a question whose answer is recoverable from the
stem. The CED's own sample activity for this topic asks students to do exactly
that with a description of Tenochtitlan; that text is not quoted or paraphrased
here, because inventing a stimulus and signing a real author's name to it is
fabrication.

THE TWO SWAP ITEMS
------------------
q3 and q27 turn on scope against reach -- what a state undertakes to do against
how far its authority extends. Each has a distractor that is the same pair with
the terms exchanged, so the anchors carry both clauses in order rather than
naming one term.

DATA QUESTIONS
--------------
Items 11, 12 and 13 carry HYPOTHETICAL tables and say so in the stem. q11 also
carries a reasoning trap that the verifier checks explicitly: three observations
of an association do not license the causal claim one distractor makes, which is
the same limit the CED's own reasoning skills impose.

NEGATIVE CONTROL: `python3 verify_w1_4.py --selftest`.
"""
import sys

import cg_check as cg
import w1_4
import wh_check

CLOTH = "Loads of cloth rendered"
DIST = "Distance from the capital in days of travel"
H_EARLY = "Households in an earlier survey"
H_LATE = "Households in a later survey"
CAP = "Capacity in units"
TOWN = "Days of travel from the nearest town"


def q11(table, item):
    pairs = sorted(zip(cg.col(table, DIST), cg.col(table, CLOTH)))
    assert all(b[1] < a[1] for a, b in zip(pairs, pairs[1:])), \
        f"cloth must fall as distance rises: {pairs}"
    far = cg.ranked(table, DIST)[0]
    assert cg.cell(table, far, CLOTH) != max(cg.col(table, CLOTH)), \
        "'the most distant province rendered the most' must be false"
    assert len(set(cg.col(table, CLOTH))) > 1, "'equal quantities' must be false"
    near = cg.ranked(table, DIST, reverse=False)[0]
    assert cg.cell(table, near, CLOTH) != min(cg.col(table, CLOTH)), \
        "'the nearest province rendered the least' must be false"
    # the causal distractor is not refuted by arithmetic and must not be: three
    # observations of an association cannot establish which way, or whether,
    # anything produced anything. The keyed choice says so in its own words.
    assert "cannot say why" in item["choices"][item["ans"]], \
        "the key must itself decline the causal reading the fourth option asserts"
    return (f"sorted by distance the cloth column reads {[p[1] for p in pairs]}, falling at "
            f"every step, and the key declines the causal reading")


def q12(table, item):
    early, late = cg.col(table, H_EARLY), cg.col(table, H_LATE)
    mult = {lab: cg.cell(table, lab, H_LATE) / cg.cell(table, lab, H_EARLY)
            for lab in cg.labels(table)}
    smallest = cg.ranked(table, H_EARLY, reverse=False)[0]
    assert mult[smallest] == max(mult.values()), \
        f"the smallest earlier settlement must have the largest multiple: {mult}"
    fell = [lab for lab in cg.labels(table)
            if cg.cell(table, lab, H_LATE) < cg.cell(table, lab, H_EARLY)]
    assert len(fell) == 1, f"exactly one settlement must decline: {fell}"
    largest = cg.ranked(table, H_EARLY)[0]
    assert mult[largest] != max(mult.values()), \
        "'the largest earlier settlement grew by the largest multiple' must be false"
    assert fell[0] != smallest, "'the settlement that declined was the smallest' must be false"
    return (f"households {early} to {late}: multiples {mult}, the smallest earlier settlement "
            f"grows most and {fell[0]} is the one that declines")


def q13(table, item):
    caps = cg.col(table, CAP)
    biggest = cg.ranked(table, CAP)[0]
    nearest = cg.ranked(table, TOWN, reverse=False)[0]
    assert biggest != nearest, f"the largest capacity must not be the nearest group: {biggest}"
    pairs = sorted(zip(cg.col(table, TOWN), caps))
    assert not all(b[1] < a[1] for a, b in zip(pairs, pairs[1:])), \
        "'capacity falls as distance rises across all three' must be false"
    assert len(set(caps)) > 1, "'equal capacities' must be false"
    farthest = cg.ranked(table, TOWN)[0]
    assert cg.cell(table, farthest, CAP) != max(caps), \
        "'the most distant group has the largest capacity' must be false"
    return (f"by distance the capacities read {[p[1] for p in pairs]}, which rises then falls, "
            f"so neither the nearest nor the farthest group holds the largest")


TABLE_CHECKS = {11: q11, 12: q12, 13: q13}

CLAIMS = [
 ("expanded in scope and reach, as state systems in Afro-Eurasia did",
  "KC-3.2.I.D.i states that in the Americas, as in Afro-Eurasia, state systems demonstrated continuity, innovation, and diversity, and expanded in scope and reach. Every clause of the key comes from that sentence, and each distractor contradicts one of them."),
 ("same general pattern of state formation as the rest of the world",
  "KC-3.2.I.D.i opens with the comparative phrase as in Afro-Eurasia and then applies to the Americas the terms KC-3.2.I.A applies to Afro-Eurasia. A shared analytic pattern is not a claim of contact, of descent or of identity."),
 ("how much a state undertakes to do, while reach concerns how far its authority extends",
  "KC-3.2.I.D.i says state systems expanded in scope AND reach, naming two things. The Governance thematic focus supplies the distinction by treating what governments do, through institutions and procedures, separately from the extent over which they do it. The anchor carries both halves because one distractor exchanges them."),
 ("fixed hours, which implies a rule enforced on many people at once",
  "Suggested skill 3.B asks which observation is the EVIDENCE for an argument. A fixed opening hour is a rule obeyed by many and so bears on organized authority; the Governance thematic focus names procedures as how governments maintain order, and KC-3.2.I.D.i is the content."),
 ("rendered to the center by settlements many days of travel away",
  "KC-3.2.I.D.i says state systems in the Americas expanded in scope and REACH, and skill 3.B asks which observation supports the argument. Obligations rendered from a distance are evidence about reach; the rejected options all concern the center alone."),
 ("each requires a standing procedure rather than a single decision",
  "The Governance thematic focus states that governments maintain order through a variety of administrative institutions, policies, and procedures, and KC-3.2.I.D.i credits state systems in the Americas with continuity, innovation, and diversity."),
 ("some through a network of cities and others through a single dominant center",
  "KC-3.2.I.D.i asserts diversity among state systems in the Americas, and the Governance thematic focus says governments obtain, retain, and exercise power in different ways and for different purposes. Uniform commodity, timing or language would tell the other way."),
 ("made in districts at a considerable distance from it",
  "Suggested skill 3.B asks students to identify the evidence supporting an argument; goods from distant districts evidence connection to other places, which is what a claim about a wider system needs. KC-3.2.I.D.i's phrase scope and reach is the context."),
 ("effectiveness did not depend on one form of rule",
  "The Governance thematic focus states that governments obtain, retain, and exercise power in different ways and for different purposes, and KC-3.2.I.D.i asserts diversity among the state systems of the Americas."),
 ("carrying forward inherited arrangements while also adopting new ones",
  "Learning Objective I asks how and why states in the Americas developed and CHANGED over time, and KC-3.2.I.D.i names continuity, innovation, and diversity together with expansion in scope and reach."),
 ("cannot say why",
  "Recomputed in q11 above: cloth falls at every step as distance rises, and each factual distractor is false on the same numbers. The causal option is refused for a reason arithmetic cannot supply, so the key states the limit itself; KC-3.2.I.D.i's scope and reach is the content."),
 ("smallest at the earlier survey grew by the largest multiple",
  "Recomputed in q12 above from the two survey columns, distractors included. KC-3.2.I.D.i credits state systems in the Americas with diversity as well as expansion, and settlements moving in opposite directions at once is what such data shows."),
 ("is not the one closest to a town",
  "Recomputed in q13 above: capacity rises then falls with distance, so neither the nearest nor the farthest group holds the largest. The Governance thematic focus treats provisioning as an administrative arrangement and KC-3.2.I.D.i asserts diversity."),
 ("able to command labor from many districts at once",
  "Suggested skill 3.B asks students to identify the evidence a source uses to support an argument, which requires telling argument and evidence apart. The keyed option is the conclusion the other four would be offered to establish; Learning Objective I is the content."),
 ("rendered nothing to the center and took no direction from it",
  "The Governance thematic focus describes governments as maintaining order through institutions, policies and procedures and KC-3.2.I.D.i speaks of reach, so the absence of obligation or direction is what bears on whether authority was exercised. Size, pottery, position and age do not."),
 ("two different means to expansion",
  "KC-3.2.I.D.i asserts diversity among state systems in the Americas and says they expanded in scope and reach; the Governance thematic focus says power is obtained and exercised in different ways. Two routes to expansion is those statements applied."),
 ("more than one district over a long period",
  "The Governance thematic focus names administrative institutions, policies, and procedures as how governments maintain order, and KC-3.2.I.D.i credits state systems in the Americas with expansion in scope and reach. Skill 3.B asks which detail carries the argument."),
 ("settlements at a distance from a center rendered goods to it",
  "KC-3.2.I.D.i asserts matters of fact about state systems expanding in scope and reach, and skill 3.B concerns evidence. Whether goods were rendered can be checked; justice, betterness, desert and excess are standards of value observation does not settle."),
 ("while introducing new arrangements for recording and moving labor",
  "KC-3.2.I.D.i states that state systems in the Americas demonstrated continuity, innovation, and diversity, listing the terms together rather than in sequence, so two of them may hold in one state at one time."),
 ("count of dwellings in one quarter",
  "Suggested skill 3.B asks which observation supports the argument actually made. The argument concerns population, so a count standing in for residents supports it while visitors and stored goods do not. KC-3.2.I.D.i is the content context."),
 ("dispute over succession among the ruling families of the state itself",
  "The Governance thematic focus states that a variety of internal AND external factors contribute to state formation, expansion, and decline. A succession dispute arises inside the state; the four rejected factors originate outside it. KC-3.2.I.D.i is the content those factors operate on."),
 ("states a conclusion while the record reports observable acts",
  "Suggested skill 3.B asks students to identify the evidence a source uses to support an argument, which presupposes that a stated conclusion is not itself evidence for itself. Learning Objective I supplies the content, how states developed and changed."),
 ("functions it had not previously performed anywhere",
  "KC-3.2.I.D.i names expansion in scope AND reach as two things, and the Governance thematic focus describes what governments do through institutions and procedures. New functions are scope; greater distance and more subjects are reach."),
 ("not constrained by the given dates",
  "The CED states that events, processes, and developments are not constrained by the given dates and may begin before, or continue after, the period, and KC-3.2.I.D.i's word continuity presupposes arrangements inherited from before it."),
 ("by means an outside observer does not recognize",
  "The Governance thematic focus states that governments maintain order through a VARIETY of administrative institutions, policies, and procedures, and KC-3.2.I.D.i asserts innovation and diversity among the state systems of the Americas."),
 ("the same analytic terms apply to each",
  "KC-3.2.I.D.i says in the Americas, AS IN AFRO-EURASIA, state systems demonstrated continuity, innovation, and diversity, and KC-3.2.I.A applies those same terms to Afro-Eurasia. Shared vocabulary is what licenses the comparison, not contact."),
 ("others in the same region continued to govern their districts and to grow",
  "The Governance thematic focus names formation, expansion AND decline as parts of one subject, and KC-3.2.I.D.i asserts diversity among the state systems of the Americas. Other centers continuing is what separates one decline from a general collapse."),
 ("claim about extent and the second about what the state could do",
  "KC-3.2.I.D.i pairs expansion in scope with expansion in reach as separate terms and the Governance thematic focus separates how power is exercised from the extent over which it is exercised. The anchor names both halves in order because one distractor exchanges them."),
 ("amount and the timing are both stated in advance",
  "Suggested skill 3.B asks which detail supports the argument. A schedule fixed in advance is the mark of a procedure, which the Governance thematic focus names as a means by which governments maintain order; KC-3.2.I.D.i is the content."),
 ("extended what they did and how far they did it",
  "KC-3.2.I.D.i is one sentence carrying every element of the key: continuity, innovation, diversity, and expansion in scope and reach, in the Americas as in Afro-Eurasia. Learning Objective I asks how and why these states developed and changed."),
]

wh_check.run(w1_4, CLAIMS, TABLE_CHECKS, sys.argv)
