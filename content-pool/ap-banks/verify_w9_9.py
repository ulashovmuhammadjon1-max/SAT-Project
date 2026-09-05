"""Key audit for AP WORLD HISTORY: MODERN 9.9 Continuity and Change in a
Globalized World -- Unit 9's REASONING topic.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code or Learning
Objective, for a human to audit. `wh_check` refuses any claim or `why` that
cites neither.

WHAT IS BEING KEYED HERE IS A REASONING MOVE, NOT A FACT. The CED says this
topic "focuses on the skill of argumentation" and that students should use
evidence relevant to the unit's key concepts to practise skill 6.D. So the claims
below justify keys of the form "this evidence qualifies that claim", "this
argument is the better made and here is why", "this source's limitation matters
here". The unit's key concepts supply the material; the skill supplies the
question.

THE CED'S OWN SENTENCE FRAME IS THE SHAPE OF THE TOPIC. Its sample activity for
9.9 gives students this to complete: "Science and technology led to profound
changes like ______; however, this change did have limits, for example ______
remained constant." A claim of change qualified by a continuity. That is what an
argument about EXTENT is, and it is why q1, q2, q6, q13, q18, q19 and q23 all
key what would limit or qualify a change claim rather than what would prove it.

THE VERDICT THIS MODULE REFUSES TO KEY. Unit 9 Learning Objective I asks the
EXTENT to which science and technology brought change from 1900 to the present.
The CED supplies no answer, because that is what students are meant to argue.
NOT ONE KEY BELOW ANSWERS IT. q3, q10, q16 and q28 come nearest and each keys
the reasoning rather than the verdict: what a record can support, which question
the framework leaves open, what a scope mismatch shows. q16 is the sharpest,
keying the extent question as the open one against four the framework settles. A
bank that keyed "the change was profound" or "the change was limited" would mark
one side of an open question wrong. The same refusal covers the unit's live
disputes: no claim says whether modified agriculture, birth control, free-market
policy or the globalization of culture was good or bad, and none states a cause
of climate change.

HOW THIS DIFFERS FROM 8.9, the other reasoning topic in this territory. Both
carry skill 6.D, so what separates them is the reasoning process. 8.9's is
CAUSATION and its items turn on corroborating and refuting causal claims about
the Cold War. 9.9's is CONTINUITY AND CHANGE and its items turn on qualifying a
change with a continuity, telling a difference of degree from a difference of
kind, and matching the scope of a claim to the scope of its evidence. q29 keys
that distinction between the two topics directly. Neither module reuses the
other's stems or evidence.

WHERE A DISTRACTOR IS THE SWAP OF THE KEY, THE ANCHOR CARRIES BOTH CLAUSES.
Six items are built on a reversal a prepared student could believe:

  q1   a qualifying case swapped for a further confirming case
  q4   the argument showing limits swapped for the argument asserting totality
  q13  what would still be recognized swapped for more of what would not
  q14  using the discordant case swapped for discarding it
  q16  the open question swapped for four the framework settles
  q28  scope of claim and scope of evidence exchanged

For each the anchor spans the whole relation, so an anchor that matched the
swapped distractor would fail the gate rather than pass it. That defect is on
record in `verify_e2_1.py`.

THE TABLES ARE EVIDENCE, NOT ANSWERS. Each is labelled hypothetical in its stem
and each keyed conclusion is a statement about what the record shows, never about
how much science and technology actually changed. q3's table is deliberately
built so that a technology is present in every region but at very different
levels, giving a student material for both halves of an argument about extent
rather than settling it.

WHAT THIS CANNOT DO: it cannot tell whether the history is right. It gates
structure, key/anchor agreement, notation, the absence of figure language, the
presence of a citation, and the arithmetic of the three data questions.

NEGATIVE CONTROL: `python3 verify_w9_9.py --selftest`. It rotates all thirty
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
import w9_9

T_ELECTRICITY = w9_9._T_ELECTRICITY
T_DEATHS = w9_9._T_DEATHS
T_TELEPHONES = w9_9._T_TELEPHONES

HOUSEHOLDS = "Households surveyed"
CONNECTED = "Of those, connected to an electricity supply"
UNCONNECTED = "Of those, not connected"
DEATHS = "Deaths recorded"
UNDER5 = "Of those, of persons under 5 years of age"
OVER5 = "Of those, of persons 5 years of age and over"
HOMES = "Households recorded"
WITH_PHONE = "Of those, with a telephone of any kind"
WITHOUT_PHONE = "Of those, with none"


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


def q3(table, item):
    """Present everywhere, at markedly different levels.

    The item deliberately gives a student material for BOTH halves of the
    Learning Objective I argument, so BOTH conditions are asserted: connected
    households in every region (which corroborates a claim of change) and shares
    that differ greatly (which qualifies it).
    """
    labs = cg.labels(table)
    total = dict(zip(labs, cg.col(table, HOUSEHOLDS)))
    on = dict(zip(labs, cg.col(table, CONNECTED)))
    _parts_sum_to_whole(table, HOUSEHOLDS, [CONNECTED, UNCONNECTED], "households surveyed")
    shares = {lab: on[lab] / total[lab] for lab in labs}
    for lab in labs:
        assert on[lab] > 0, \
            f"the key needs connected households in {lab}; the row reads {on[lab]}"
    spread = max(shares.values()) - min(shares.values())
    assert spread > 0.25, (
        f"the key says the share differs GREATLY between the regions; the shares are "
        f"{ {k: round(v, 3) for k, v in shares.items()} }, a spread of {spread:.3f}")
    # every distractor false on the same numbers
    assert on["Region three"] > 0, \
        "'no household in the third region is connected' must be false"
    assert any(v < 1.0 for v in shares.values()), \
        "'every household in every region is connected' must be false"
    assert len(set(round(v, 6) for v in shares.values())) > 1, \
        "'the share connected is the same in all three regions' must be false"
    assert total["Region three"] <= total["Region two"], \
        "'the third region surveyed more households than the second' must be false"
    return (f"connected households {on} of {total}, shares "
            f"{ {k: round(v, 3) for k, v in shares.items()} }: present everywhere and "
            f"spread by {spread:.3f}; the parts sum to the stated wholes and all four "
            f"distractors recompute false")


def q7(table, item):
    """Deaths fall, and the under-five SHARE falls at every step too."""
    periods = cg.labels(table)
    assert periods == ["1920", "1960", "2000"], \
        f"the key speaks of each period recorded; the rows are {periods}"
    _parts_sum_to_whole(table, DEATHS, [UNDER5, OVER5], "deaths recorded")
    total = cg.col(table, DEATHS)
    young = cg.col(table, UNDER5)
    older = cg.col(table, OVER5)
    assert all(b < a for a, b in zip(total, total[1:])), \
        f"the key says deaths recorded fell in each period; they run {total}"
    shares = [y / t for y, t in zip(young, total)]
    assert all(b < a for a, b in zip(shares, shares[1:])), (
        f"the key says the under-five portion fell AS A SHARE in each period; the shares "
        f"run {[round(s, 3) for s in shares]}")
    # every distractor false on the same numbers
    assert total[-1] < total[0], \
        "'deaths recorded rose in each period after the first' must be false"
    assert shares[-1] < shares[0], \
        "'the under-five share rose across the record' must be false"
    assert young[-1] > 0, \
        "'no death of a person under 5 is recorded in the last period' must be false"
    assert not all(b < a for a, b in zip(older, older[1:])), \
        "'deaths of persons 5 and over fell in each period' must be false"
    return (f"deaths run {total} and the under-five share {[round(s, 3) for s in shares]}, "
            f"both falling at every step, against {older} of persons 5 and over, which do "
            f"not; the parts sum to the stated wholes and all four distractors recompute "
            f"false")


def q10(table, item):
    """Telephone ownership rises to a large majority."""
    periods = cg.labels(table)
    assert periods == ["1960", "1980", "2000"], \
        f"the key speaks of each period recorded; the rows are {periods}"
    _parts_sum_to_whole(table, HOMES, [WITH_PHONE, WITHOUT_PHONE], "households recorded")
    total = cg.col(table, HOMES)
    have = cg.col(table, WITH_PHONE)
    shares = [h / t for h, t in zip(have, total)]
    assert all(b > a for a, b in zip(shares, shares[1:])), (
        f"the key says the share rose in each period; the shares run "
        f"{[round(s, 3) for s in shares]}")
    assert shares[-1] > 0.75, (
        f"the key says a large majority by the last period; the share is "
        f"{shares[-1]:.3f}")
    # every distractor false on the same numbers
    assert shares[-1] > shares[0], \
        "'the share fell across the record' must be false"
    assert have[0] > 0, \
        "'no household is recorded with a telephone in the first period' must be false"
    assert not all(s > 0.5 for s in shares), (
        "'a majority had one in every period' must be false; the shares are "
        f"{[round(s, 3) for s in shares]}")
    assert total[-1] > total[0], \
        "'the number of households recorded fell across the record' must be false"
    return (f"households with a telephone run {have} of {total}, a share of "
            f"{[round(s, 3) for s in shares]} rising to a large majority only at the end; "
            f"the parts sum to the stated wholes and all four distractors recompute false")


TABLE_CHECKS = {3: q3, 7: q7, 10: q10}

CLAIMS = [
 ("region in which one of the century's technologies had still not arrived",
  "Unit 9 Learning Objective I asks for the EXTENT to which science and technology brought change, and skill 6.D asks a student to qualify or modify an argument using alternative evidence. KC-6.1 records advances in communication, transportation, industry, agriculture and medicine without asserting that they reached everywhere, so a region a technology had not reached limits the claim's scope; a distractor offers a further confirming case instead, so the anchor carries the direction of the evidence."),

 ("claim of change qualified by a continuity, which is what a claim about extent requires",
  "Unit 9 Learning Objective I asks for the extent to which science and technology brought change, and skill 6.D asks for an argument that qualifies and complicates. The frame the CED prints in its sample activity for this topic pairs a profound change with something that remained constant, which is a claim about extent rather than about occurrence."),

 ("Connected households are recorded in every region, but the share connected differs greatly between the three",
  "KC-6.1.I.D records that energy technologies raised productivity and increased the production of material goods, and Unit 9 Learning Objective I asks for the EXTENT of the change technology brought. A survey in which a technology is present everywhere but unevenly gives a student material for both halves of an argument about extent rather than settling it, so the anchor carries both the presence and the unevenness. Recomputed in q3 above."),

 ("claim about extent requires the limits of the change to be shown as well as the change",
  "Unit 9 Learning Objective I asks for the EXTENT to which science and technology brought change, and skill 6.D names explaining how or why an argument is or is not effective. An argument showing where a change reached and where it did not is an argument about extent; a distractor prefers the stronger unqualified claim, so the anchor carries both requirements."),

 ("same technology's spread in several regions, showing markedly different levels",
  "KC-6.1 records that rapid advances in science and technology led to advances in communication, transportation, industry, agriculture, and medicine, and skill 6.D asks a student to corroborate an argument with diverse evidence. A claim about unevenness is comparative and needs measurements from more than one place, which a single region or a list of inventions cannot supply."),

 ("how far and where that lengthening reached, which is what a claim about extent requires",
  "KC-6.1.I.C states that medical innovations, including vaccines and antibiotics, increased the ability of humans to survive and live longer lives, which the chapter reports correctly. Unit 9 Learning Objective I asks for the EXTENT of such change, so what is missing is the reach and the limits rather than the fact."),

 ("share of them of persons under 5 fell in each period as well",
  "KC-6.1.I.C states that medical innovations increased the ability of humans to survive and live longer lives, and a falling share of deaths among the youngest is one measure a student could use in an argument about how far that reached. The record is hypothetical and is recomputed from the table alone in q7 above; the framework supplies no verdict on the extent of the change."),

 ("existence of a technology does not establish that it had reached or been adopted everywhere",
  "KC-6.1 records that advances in science and technology led to advances across several fields without asserting that any reached everywhere at once. Unit 9 Learning Objective I asks for the EXTENT of the change, so the gap between a technology existing and its being in use is the question the argument assumes away."),

 ("Explaining nuance by analyzing multiple variables",
  "Skill 6.D names explaining nuance of an issue by analyzing multiple variables as one of its four moves, and KC-6.1 names communication, transportation, industry, agriculture, and medicine as the fields in which advances occurred. Assembling four of those fields under one claim is that move rather than any of the other three the skill lists."),

 ("rose in each period and was a large majority by the last",
  "KC-6.1.I.A states that new modes of communication reduced the problem of geographic distance, and the spread of a household technology is one measure of how far that reached. The record is hypothetical and both halves of the key are recomputed from the table alone in q10 above; how much change this represents is what a student is asked to argue."),

 ("same sentence states the yields and the spread of modified methods",
  "KC-6.1.I.B states that the Green Revolution and commercial agriculture increased productivity and sustained the earth's growing population AS IT SPREAD chemically and genetically modified forms of agriculture. Both claims are halves of that one sentence, and the framework asserts them together without judging whether the methods were good."),

 ("also records changes in social categories and in culture that were not technological",
  "KC-6.1 records the technological advances, but KC-6.3.III.i and KC-6.3.III.ii record rights-based challenges to old assumptions and a widening of access, and KC-6.3.IV.i to iii record changes in the arts and in culture. Skill 6.D asks a student to qualify an argument using alternative evidence, and the non-technological changes the unit also records are that evidence."),

 ("what a person born in 1900 would still recognize, and saying why",
  "Unit 9 Learning Objective I asks for the EXTENT of the change science and technology brought, and the CED's own sentence frame for this topic pairs a profound change with something that remained constant. Skill 6.D asks a student to qualify an argument using alternative evidence; a distractor offers more instances of the same change, which would only restate the claim, so the anchor names the continuity."),

 ("difference to say something about how far and how evenly the change reached",
  "Unit 9 Learning Objective I asks for the extent to which science and technology brought change, and skill 6.D asks a student to develop a complex argument using diverse and ALTERNATIVE evidence. A difference between two neighbours is evidence about evenness, and discarding the inconvenient case is the failure the skill is written against."),

 ("manufacturer's own assessment of what its product has done",
  "Skill 6.D names explaining the relative historical significance of a source's credibility and limitations. KC-6.1 records that advances in science and technology led to advances across several fields, and a manufacturer assessing its own product's effect has an interest in the answer, which is what limits the use of the source."),

 ("How far science and technology changed the world between 1900 and the present",
  "KC-6.1.I.A, KC-6.1.I.C, KC-6.1.I.D and KC-6.3.IV.iii each state a development as course content, while Unit 9 Learning Objective I asks students to explain THE EXTENT TO WHICH science and technology brought change. The framework supplies the developments and leaves the measure of their reach to be argued; this item keys the open question against four the framework settles, and is the sharpest statement in this module of what the bank will not decide."),

 ("more inclusive in much of the world, which is a change of degree rather than a disappearance",
  "KC-6.3.III.ii states that IN MUCH OF THE WORLD access to education and participation in new political and professional roles became more inclusive in terms of race, class, gender, and religion. Unit 9 Learning Objective I asks for the extent of change, and the framework's qualifier makes this a change of degree, which is what the student's inference oversteps."),

 ("what the two accounts show to have stayed the same, and build a claim about extent from both",
  "The reasoning process the CED prints beside this topic is continuity and change, and Unit 9 Learning Objective I asks for the extent of the change science and technology brought. The CED's own sentence frame for this topic requires both a change and something that remained constant, so the continuities are the missing half."),

 ("changed a great deal in some places and little in others, with evidence for both",
  "Unit 9 Learning Objective I asks for THE EXTENT TO WHICH science and technology brought change, which is a question of how much and how widely rather than whether at all. KC-6.1 already settles the occurrence by recording the advances, so an argument that adds anything must be about their reach."),

 ("Qualifying a claim using alternative evidence, so that the argument states its own limits",
  "KC-6.1.III.B states that more effective forms of birth control gave women greater control over fertility and contributed to declining rates of fertility IN MUCH OF THE WORLD, a claim with a qualifier already in it. Skill 6.D names qualifying an argument using diverse and alternative evidence, and a historian who states both the pattern and its limit is making that move rather than any of the other three."),

 ("states responded in a variety of ways to the economic challenges of the century",
  "KC-6.3.I states that states responded IN A VARIETY OF WAYS to the economic challenges of the twentieth century, which is difference persisting alongside a common set of technologies. Skill 6.D asks a student to complicate an argument with alternative evidence, and the framework's own word variety is that evidence."),

 ("states how far a change reached, supports that with evidence from more than one field or place, and explains what it did not reach",
  "Skill 6.D asks a student to corroborate, qualify, or modify an argument using diverse and alternative evidence IN ORDER TO DEVELOP A COMPLEX ARGUMENT, and Unit 9 Learning Objective I asks specifically for extent. Reach, breadth of evidence and an explained limit are the three parts of that, and each distractor drops at least one."),

 ("became more global, which is not the same as saying it became uniform",
  "KC-6.3.IV.i states that in the second half of the century popular and consumer culture became MORE GLOBAL, and KC-6.3.IV.ii that arts, entertainment, and popular culture increasingly reflected the influence of a globalized society. More global is a comparative, and Unit 9 Learning Objective I's question about extent is what the student's leap to uniformity skips."),

 ("series for the scale of the change and the recollections for what it meant to those it reached",
  "Skill 6.D asks for diverse and alternative evidence and for an explanation of the relative significance of a source's credibility and limitations. KC-6.1 records advances across several fields whose scale a series can measure and whose meaning it cannot, so the two sources answer different parts of one question about extent."),

 ("medical advance reached, tested against records of who received it and where",
  "KC-6.1.I.C states that medical innovations increased the ability of humans to survive and live longer lives, and a claim about how widely that reached is a claim about coverage, which records of recipients test directly. Skill 6.D asks for evidence relevant to the argument, and each distractor pairs a claim with material bearing on nothing in it."),

 ("earlier centuries as well, since the claim is comparative",
  "Skill 6.D asks a student to explain how or why an argument is or is not effective, and Unit 9 Learning Objective I asks for the extent of change, which invites comparison. A claim that one century's change exceeded another's cannot be supported from one side alone, however much evidence is added to that side."),

 ("claim is far wider than the evidence gathered to support it",
  "Unit 9 Learning Objective I asks for the extent to which science and technology brought change from 1900 to the present, which makes the scope of a claim and the scope of its evidence the thing at issue. Skill 6.D asks why an argument is or is not effective, and a distractor exchanges the two scopes, so the anchor names which is wider than which."),

 ("continuity and change, where the preceding unit's final topic is causation",
  "The CED prints continuity and change as the reasoning process beside this topic, under Unit 9 Learning Objective I, and causation beside Topic 8.9 under Unit 8 Learning Objective K. Both share skill 6.D, so the process is what distinguishes the arguments they ask for, and the anchor names both halves of the contrast."),

 ("carry qualifiers, recording change in much of the world, in some regions, and in a variety of ways",
  "KC-6.3.III.ii says in much of the world, KC-6.3.I says in a variety of ways, KC-6.1.III.B says in much of the world again, and KC-6.3.I.E in Topic 9.4 says in some regions. Qualifiers of that kind make the reach of a change a question rather than a given, and Unit 9 Learning Objective I asks a student to argue it."),

 ("support that with evidence from more than one field, and say what the change did not reach",
  "Unit 9 Learning Objective I asks a student to explain the extent to which science and technology brought change from 1900 to the present, and skill 6.D asks for an argument corroborated, qualified or modified with diverse and alternative evidence. Extent, breadth of evidence and an explained limit are the three parts of that; a chronology, a verdict on benefit and a single cause are none of them."),
]

wh.run(w9_9, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
