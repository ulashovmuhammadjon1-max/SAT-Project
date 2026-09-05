"""Key audit for AP WORLD HISTORY: MODERN 8.9 Causation in the Age of the Cold
War and Decolonization -- Unit 8's REASONING topic.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code or Learning
Objective, for a human to audit. `wh_check` refuses any claim or `why` that
cites neither.

WHAT IS BEING KEYED HERE IS A REASONING MOVE, NOT A FACT. The CED says of this
topic that it "focuses on the skill of argumentation" and that students should
use evidence relevant to the unit's key concepts to practise skill 6.D --
corroborate, qualify, or modify an argument using diverse and alternative
evidence in order to develop a complex argument. So the claims below justify
keys of the form "this evidence corroborates that claim", "this consideration
qualifies it", "this argument is the better made and here is why". The unit's
key concepts supply the material; the skill supplies the question.

THE VERDICT THIS MODULE REFUSES TO KEY. Unit 8 Learning Objective K asks the
EXTENT to which the effects of the Cold War were similar in the Eastern and
Western Hemispheres. The CED supplies no answer to that, because it is what
students are meant to argue. NOT ONE KEY BELOW ANSWERS IT. q4, q8, q20, q25 and
q28 come nearest and each keys the reasoning rather than the verdict: what a
record can support, what a scope mismatch shows, what an inference does not
license. A bank that keyed "the effects were largely similar" or "largely
different" would mark one side of an open question wrong, which is the specific
failure this topic invites. The same refusal applies to the unit's other live
disputes: no claim below assigns blame for a proxy war, declares a victor in the
Cold War, credits a person with its end, or ranks the two economic systems --
see q26 in particular, which keys the framework's REFUSAL to name a single
decisive cause.

WHERE A DISTRACTOR IS THE SWAP OF THE KEY, THE ANCHOR CARRIES BOTH CLAUSES.
Six items are built on a reversal a prepared student could believe:

  q3   the argument resting on many cases swapped for the one resting on one
  q9   a qualifying exception swapped for a further confirming case
  q16  keeping the discordant case swapped for removing it
  q18  scope of thesis and scope of evidence exchanged
  q24  modification of a claim swapped for its confirmation
  q25  thesis broader than evidence swapped for evidence broader than thesis

For each the anchor spans the whole relation, so an anchor that matched the
swapped distractor would fail the gate rather than pass it. That defect is on
record in `verify_e2_1.py`.

THE TABLES ARE EVIDENCE, NOT ANSWERS. Each is labelled hypothetical in its stem
and each keyed conclusion is a statement about what the record shows, never
about how similar the effects actually were. q8's table is deliberately built so
that it gives a student material for BOTH halves of the Learning Objective K
argument -- a majority in both hemispheres, but not the same majority -- rather
than settling it.

WHAT THIS CANNOT DO: it cannot tell whether the history is right. It gates
structure, key/anchor agreement, notation, the absence of figure language, the
presence of a citation, and the arithmetic of the three data questions.

NEGATIVE CONTROL: `python3 verify_w8_9.py --selftest`. It rotates all thirty
keys, breaks all thirty anchors, corrupts every cell of every table, injects
each banned notation form, injects figure language into a stem and a choice,
strips the citation from a why and from a claim, duplicates a choice, thins a
why and makes a why name an option by letter -- and asserts not merely that
something raised but WHICH message came back. It also runs positive controls,
so a gate that rejected everything would fail here rather than look thorough.
"""
import sys

import cg_check as cg
import wh_check as wh
import w8_9

T_ALLIANCES = w8_9._T_ALLIANCES
T_DOCUMENTS = w8_9._T_DOCUMENTS
T_RESPONSES = w8_9._T_RESPONSES

STATES = "States recorded"
JOINED = "Of those, joined to a formal alliance with an outside great power"
NOT_JOINED = "Of those, not so joined"
DOCS = "Documents surveyed"
REFERRING = "Of those, referring to the global ideological confrontation"
NOT_REFERRING = "Of those, not referring to it"
SURVEYED = "States surveyed"
EXPAND = "Of those, whose principal response was to expand state direction of the economy"
REDUCE = "Of those, whose principal response was to reduce it"


def _parts_sum_to_whole(table, whole, parts, what):
    """Every row's parts must total its whole.

    This is what makes the negative control mean anything on these tables. The
    corruption in `es_check` only ever makes a number LARGER, so a check of the
    form "this count is above zero" is monotone and can never fail: it reads the
    table without being able to object to anything in it. Sibling module 8.5
    shipped a first draft whose table check caught 1 of 12 corrupted cells for
    exactly that reason. Each row here states a whole and the two parts it was
    divided into, and every stem says so.
    """
    labs = cg.labels(table)
    totals = cg.col(table, whole)
    cols = [cg.col(table, p) for p in parts]
    for i, lab in enumerate(labs):
        got = sum(c[i] for c in cols)
        assert got == totals[i], (
            f"{lab}: the {what} split into {[c[i] for c in cols]} totals {got}, but the "
            f"row states {totals[i]} in all -- the parts do not sum to the whole")


def q4(table, item):
    """Alliance membership present everywhere, universal nowhere."""
    labs = cg.labels(table)
    total = dict(zip(labs, cg.col(table, STATES)))
    joined = dict(zip(labs, cg.col(table, JOINED)))
    assert sorted(labs) == ["Africa", "Asia", "Europe", "Latin America"], \
        f"the key speaks of every region listed; the rows are {labs}"
    _parts_sum_to_whole(table, STATES, [JOINED, NOT_JOINED], "states recorded")
    for lab in labs:
        assert 0 < joined[lab] < total[lab], (
            f"the key needs some but not all of {lab}'s states joined to an outside "
            f"alliance; the row reads {joined[lab]} of {total[lab]}")
    # every distractor false on the same numbers
    assert not any(joined[l] == total[l] for l in labs), \
        "'in at least one region every state is joined to an alliance' must be false"
    assert joined["Africa"] > 0, \
        "'no state in Africa is joined to an outside alliance' must be false"
    assert cg.ranked(table, STATES)[0] != "Latin America", \
        "'Latin America records more states than any other region' must be false"
    assert len(set(total.values())) > 1, \
        "'the four regions record the same number of states' must be false"
    return (f"states joined to an outside alliance {joined} against totals {total}, a "
            f"nonempty proper subset in every region, the parts summing to the stated "
            f"wholes; all four distractors recompute false")


def q8(table, item):
    """A majority in both hemispheres, and the larger majority in the East.

    The item deliberately gives a student material for BOTH halves of the
    Learning Objective K argument. The key is a statement about the record, not
    a verdict on how similar the effects were, so BOTH conditions are asserted:
    a majority in each hemisphere (which corroborates a similarity claim) and a
    difference between the two majorities (which qualifies it).
    """
    labs = cg.labels(table)
    total = dict(zip(labs, cg.col(table, DOCS)))
    ref = dict(zip(labs, cg.col(table, REFERRING)))
    assert sorted(labs) == ["Eastern Hemisphere", "Western Hemisphere"], \
        f"Learning Objective K names the two hemispheres; the rows are {labs}"
    _parts_sum_to_whole(table, DOCS, [REFERRING, NOT_REFERRING], "documents surveyed")
    shares = {lab: ref[lab] / total[lab] for lab in labs}
    for lab in labs:
        assert shares[lab] > 0.5, (
            f"the key needs a majority referring to the confrontation in {lab}; the row "
            f"reads {ref[lab]} of {total[lab]}, a share of {shares[lab]:.3f}")
    assert shares["Eastern Hemisphere"] > shares["Western Hemisphere"], (
        f"the key names the Eastern Hemisphere's majority as the larger; the shares are "
        f"{ {k: round(v, 3) for k, v in shares.items()} }")
    # every distractor false on the same numbers
    assert not all(shares[l] < 0.5 for l in labs), \
        "'in neither hemisphere does a majority refer to the confrontation' must be false"
    assert ref["Western Hemisphere"] > 0, \
        "'no Western Hemisphere document refers to the confrontation' must be false"
    assert total["Western Hemisphere"] <= total["Eastern Hemisphere"], \
        "'the Western Hemisphere surveyed more documents' must be false"
    assert shares["Eastern Hemisphere"] != shares["Western Hemisphere"], \
        "'the share is identical in the two hemispheres' must be false"
    return (f"documents referring to the confrontation {ref} of {total}, shares "
            f"{ {k: round(v, 3) for k, v in shares.items()} }: a majority in both and the "
            f"larger in the East, the parts summing to the stated wholes; all four "
            f"distractors recompute false")


def q12(table, item):
    """Both directions present everywhere, neither predominant throughout."""
    labs = cg.labels(table)
    total = dict(zip(labs, cg.col(table, SURVEYED)))
    up = dict(zip(labs, cg.col(table, EXPAND)))
    down = dict(zip(labs, cg.col(table, REDUCE)))
    _parts_sum_to_whole(table, SURVEYED, [EXPAND, REDUCE], "states surveyed")
    for lab in labs:
        assert up[lab] > 0 and down[lab] > 0, (
            f"the key needs both directions present in {lab}; the row reads {up[lab]} "
            f"expanding and {down[lab]} reducing")
    winners = {lab: ("expand" if up[lab] > down[lab] else "reduce") for lab in labs}
    assert len(set(winners.values())) > 1, (
        f"the key says the predominant direction is not the same in all three groups; the "
        f"predominant directions are {winners}")
    # every distractor false on the same numbers
    assert any(down[l] > 0 for l in labs), \
        "'every state surveyed expanded state direction' must be false"
    assert down["Group three"] > 0, \
        "'no state in group three reduced state direction' must be false"
    assert len(set(total.values())) > 1, \
        "'the three groups surveyed the same number of states' must be false"
    return (f"expanding {up} against reducing {down} of {total} surveyed, both present "
            f"everywhere with predominant directions {winners} differing between groups, "
            f"the parts summing to the stated wholes; all four distractors recompute false")


TABLE_CHECKS = {4: q4, 8: q8, 12: q12}

CLAIMS = [
 ("extended beyond its ideological origins to have profound effects on economic, political, social, and cultural aspects",
  "KC-6.2.IV.C states that the Cold War conflict extended beyond its basic ideological origins to have profound effects on economic, political, social, and cultural aspects of global events. The argument's premise about ideas is granted by the framework and its conclusion is what the same sentence denies, which is why that sentence undermines it while the other observations leave it standing."),

 ("military alliances in one hemisphere and of proxy wars fought in postcolonial states in the other",
  "KC-6.2.IV.D states that the Cold War produced new military alliances, including NATO and the Warsaw Pact, and led to nuclear proliferation and proxy wars between and within postcolonial states in Latin America, Africa, and Asia. Skill 6.D asks a student to corroborate an argument with relevant evidence, and a claim about both hemispheres requires evidence drawn from both."),

 ("rests on a range of cases and acknowledges evidence that complicates it",
  "Skill 6.D, the suggested skill for the topic whose aim is Unit 8 Learning Objective K, asks a student to corroborate, qualify, or modify an argument using diverse and alternative evidence in order to develop a complex argument, and names explaining how or why an argument is effective as one of its moves. A distractor treats the acknowledged complication as a weakness, which inverts the skill, so the anchor carries the breadth of evidence and the acknowledgement together."),

 ("Every region records some states joined to an outside alliance, and in no region are all of its states so joined",
  "KC-6.2.IV.D places the Cold War's alliances and proxy wars across Europe, Latin America, Africa and Asia, so its reach was wide without being uniform. The record is hypothetical and the keyed conclusion is a statement about what the record shows, not a verdict on how similar the effects were; it is recomputed from the table alone in q4 above."),

 ("served the government whose decisions he is explaining, which shapes what the account can establish",
  "Skill 6.D names explaining the relative historical significance of a source's credibility and limitations as one of the moves a complex argument makes. An official explaining his own government's conduct has an interest in how it is judged, and KC-6.2.IV.C establishes the profound effects such an account is placed to attribute elsewhere."),

 ("challenged the existing political and social order in varying ways rather than in a single way",
  "KC-6.2 states that peoples and states around the world challenged the existing political and social order in VARYING WAYS, leading to unprecedented worldwide conflicts. The modification the claim needs is the framework's own word, and the distractors replace one overstatement with another rather than qualifying it."),

 ("several kinds of effect together to show the nuance of a claim about how far the conflict reached",
  "Skill 6.D names explaining nuance of an issue by analyzing multiple variables, and KC-6.2.IV.C states that the Cold War had profound effects on economic, political, social, AND cultural aspects of global events. Holding the four together is what analyzing multiple variables means; discarding three abandons the nuance."),

 ("majority of documents in both hemispheres refer to the confrontation, and that majority is the larger in the Eastern Hemisphere",
  "KC-6.2.IV.C states that the Cold War had profound effects on political and other aspects of global events, of which the frequency of official reference is one trace. Unit 8 Learning Objective K asks how far the effects were similar across hemispheres, and this record gives a student material for BOTH halves of that argument rather than settling it -- which is why the anchor carries the shared majority and the difference between the two together. Recomputed in q8 above."),

 ("region in which the conflict's recorded effects differed markedly from those elsewhere",
  "Skill 6.D asks a student to qualify or modify an argument using alternative evidence, and a universal claim is qualified by a well-documented exception rather than by a further confirming case. A distractor offers the confirming case instead, so the anchor carries the direction of the evidence as well as its subject. Unit 8 Learning Objective K is the aim this skill is attached to on the CED's page for this topic."),

 ("connection across periods, by relating an earlier disappointment to a later demand",
  "KC-6.2.II states that hopes for greater self-government were largely unfulfilled following World War I and that increasing anti-imperialist sentiment after World War II contributed to the dissolution of empires. Skill 6.D names explaining relevant and insightful connections within and across periods, and joining those two moments is that move rather than any of the other three the skill lists."),

 ("supplies a narrative rather than an argument that its evidence is made to support",
  "Skill 6.D, the suggested skill for the topic whose aim is Unit 8 Learning Objective K, names explaining how or why a historical claim or argument is or is not effective. An argument is effective when its evidence is shown to bear on its claim, so a chronology that never returns to its thesis fails on the skill's own terms rather than on any rule about where a thesis sits or what it is about."),

 ("Both directions of policy appear in every group, and the direction that predominates is not the same in all three groups",
  "KC-6.3.I states that states responded in a VARIETY of ways to the economic challenges of the twentieth century, and KC-6.3 that the role of the state in the domestic economy varied. The survey is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in q12 above."),

 ("party to the conflict has an interest in how it is described, so the second account is needed to test the first",
  "Skill 6.D names explaining the relative historical significance of a source's credibility and limitations, and using diverse and alternative evidence. KC-6.2.IV.D places proxy wars between and within postcolonial states inside this unit, and a belligerent's own communique is the kind of source whose interest has to be tested against another."),

 ("proxy wars of the Cold War were fought within and between postcolonial states",
  "KC-6.2.IV.D states that the Cold War led to proxy wars between and within postcolonial states in Latin America, Africa, and Asia, which places the two processes in the same territories and the same events. Shared chronology or shared coverage in books is not a connection between the processes themselves, which is what each distractor offers instead."),

 ("contradicts the claim, stating that the role of the state in the domestic economy varied",
  "KC-6.3 states that the role of the state in the domestic economy varied, and KC-6.3.I that states responded in a variety of ways to the economic challenges of the twentieth century. The framework's word is varied, which contradicts uniformity without denying that states had an economic role, so the anchor carries the verdict together with its ground."),

 ("Keep the discordant case in the argument and explain what it shows about the thesis's limits",
  "Skill 6.D, the suggested skill for the topic whose aim is Unit 8 Learning Objective K, asks a student to corroborate, qualify, or modify an argument using diverse and ALTERNATIVE evidence in order to develop a complex argument. Evidence running against a thesis is what qualifies it into a complex one; suppressing it and abandoning the thesis outright are the two failures the skill is written against, and a distractor offers each."),

 ("government's own account of a decision for which it wishes to appear responsible",
  "Skill 6.D names explaining the relative historical significance of a source's credibility and limitations. A government asserting the freedom of its own choice is describing something it has an interest in, and KC-6.2.IV.C establishes that the conflict's effects reached deeply into political life, which is the pressure such a paper would have reason not to record."),

 ("reshaped daily life, tested against evidence of its effects on economic, social and cultural practice",
  "KC-6.2.IV.C states that the Cold War conflict had profound effects on economic, political, social, and cultural aspects of global events, so evidence of those effects is what a claim about daily life must be tested against. Skill 6.D asks for evidence relevant to the argument; each distractor pairs a claim with material bearing on nothing in it, and one pairs the same claim with irrelevant evidence, so the anchor carries the claim and the evidence together."),

 ("links two periods in a way that explains why the later demands took the form they did",
  "KC-6.2.II states that hopes for greater self-government were largely unfulfilled following World War I and that increasing anti-imperialist sentiment after World War II contributed to the dissolution of empires. Skill 6.D names explaining relevant and insightful connections within and across periods, and a connection is insightful when it explains something about the later development rather than merely noting that both occurred."),

 ("profound and widespread does not establish that they took the same form in every place",
  "KC-6.2.IV.C states that the conflict had profound effects on economic, political, social, and cultural aspects of global events, which is a claim about depth and range rather than about uniformity. Unit 8 Learning Objective K asks for the EXTENT of similarity across hemispheres, a question the framework leaves open, so the key marks the inference as unlicensed without answering the question itself."),

 ("evidence from more than one region, and an explanation of a case that fits the claim imperfectly",
  "Skill 6.D, the suggested skill for the topic whose aim is Unit 8 Learning Objective K, asks a student to corroborate, qualify, or modify an argument using diverse and alternative evidence IN ORDER TO DEVELOP A COMPLEX ARGUMENT. A claim, evidence of range and an explained exception are the three parts of that, and each distractor drops at least one of them."),

 ("Set the two against each other and explain what the difference between them shows",
  "Skill 6.D asks for the use of diverse and alternative evidence and for an explanation of the relative significance of a source's credibility and limitations. KC-6.3.I places states with varying economic roles inside this unit, and a government's own statistics are a source whose interest the skill requires a student to weigh rather than to accept or discard wholesale."),

 ("led to unprecedented worldwide conflicts",
  "KC-6.2 states that peoples and states around the world challenged the existing political and social order in varying ways, leading to unprecedented worldwide conflicts. Both the word unprecedented and the word worldwide are the framework's own, which is what makes that sentence the corroboration the argument needs."),

 ("modifies the claim, stating that such institutions emerged and continued to develop",
  "KC-6.3 states that new institutions of global association emerged AND CONTINUED TO DEVELOP throughout the century. The framework agrees that they emerged and disagrees that they then stopped, so the correct move is a modification rather than a flat confirmation or refusal, and the anchor carries the move together with its ground."),

 ("thesis is broader than the evidence assembled to support it",
  "Unit 8 Learning Objective K asks for the extent to which effects were similar in the Eastern and Western Hemispheres, which makes the scope of a claim and the scope of its evidence the thing at issue. Skill 6.D asks why an argument is or is not effective, and a distractor exchanges the two scopes, so the anchor names which is broader than which."),

 ("several developments the framework names as having led to the outcome together",
  "KC-6.2.IV.E names advances in U.S. military and technological development, the Soviet Union's costly and ultimately failed invasion of Afghanistan, and public discontent and economic weakness in communist countries as leading together to the end of the Cold War and the collapse of the Soviet Union. The framework names no individual and no single decisive cause, so the key states the refusal to rank rather than supplying a ranking."),

 ("shaped by the conditions of its publication and needs to be read alongside others",
  "Skill 6.D names explaining the relative historical significance of a source's credibility and limitations, which means locating what a source can and cannot establish rather than accepting or discarding it. KC-6.2 records that existing orders were challenged in varying ways, so an account reporting no opposition is evidence about its own conditions of publication as much as about its subject."),

 ("In what respects were the conflict's effects alike across regions, and in what respects did they differ",
  "Unit 8 Learning Objective K asks for the extent to which the effects of the Cold War were similar in the Eastern and Western Hemispheres, and skill 6.D asks for an argument that qualifies and complicates rather than one returning a verdict. A question inviting both likeness and difference is answerable from the evidence; a question of moral correctness is not settled by the framework and is not what the course asks."),

 ("varying forms, states responded to economic pressures in varying ways, and the conflict's effects reached many aspects of life at once",
  "KC-6.2 records challenges to the existing political and social order in varying ways, KC-6.3 and KC-6.3.I a varying state role and a variety of responses to economic challenges, and KC-6.2.IV.C profound effects across economic, political, social, and cultural aspects of global events. Variation on several axes at once is what a complex argument is built from."),

 ("support it with evidence from more than one region, and explain what qualifies it",
  "Unit 8 Learning Objective K asks for the extent to which the effects of the Cold War were similar in the Eastern and Western Hemispheres, and skill 6.D asks a student to corroborate, qualify, or modify an argument using diverse and alternative evidence in order to develop a complex argument. Extent, range of evidence and qualification are the three parts of that; neither chronology nor a moral verdict is among them."),
]

wh.run(w8_9, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
