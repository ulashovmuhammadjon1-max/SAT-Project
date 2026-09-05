"""Key audit for AP WORLD HISTORY: MODERN 8.7 Global Resistance to Established
Power Structures After 1900.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code or Learning
Objective, for a human to audit. `wh_check` refuses any claim or `why` that
cites neither, because a key traceable only to an author's knowledge of the
twentieth century cannot be checked by anyone reading this bank later.

WHERE A DISTRACTOR IS THE SWAP OF THE KEY, THE ANCHOR CARRIES BOTH CLAUSES.
Six items here are built on a reversal a prepared student could believe:

  q3   intensifying conflict swapped for reducing it
  q6   opposition and intensification exchanged between the two clauses
  q9   "some promoted nonviolence" swapped for "none did"
  q18  a movement's turn to force read as the promotion of nonviolence
  q21  the framework's concession about conflict swapped for its denial
  q26  the contrasting pair of reactions swapped for a pair from other topics

For each of those the anchor spans the whole relation and not just one noun, so
an anchor that matched the swapped distractor would fail the gate rather than
pass it. That defect is on record in `verify_e2_1.py`.

THE QUANTIFIERS ARE THE CONTENT RISK and five claims below say so. KC-6.2.V says
MANY opposed the trend toward conflict and SOME intensified it; KC-6.2.V.A says
SOME of those who challenged the wars promoted nonviolence; KC-6.2.V.C says
militarized states OFTEN responded in ways that intensified conflict;
KC-6.2.V.D says SOME movements used violence. None is a universal. In a topic
whose title is about resistance, the tempting error is to key every challenge to
power as nonviolent, or every state as intensifying conflict, and either would
teach the opposite of the framework's own sentence. The three data questions
exist to make those quantifiers countable; each table is labelled hypothetical
in its stem and asserts no real frequency.

CONTESTED GROUND, AND WHAT NO CLAIM BELOW ASSERTS. This topic covers political
violence and the CED names particular regimes and particular movements. Every
claim here is limited to what the framework's descriptive sentences state.
None justifies, condemns, ranks or excuses any actor; none assigns
responsibility for a particular episode; none takes a side in a dispute that
remains live. Where an item involves a source produced by a party to a
conflict, it asks what the source's purpose and audience were -- skill 2.B --
and not who was in the right.

NO INVENTED QUOTATION. Gandhi, King and Mandela are named inside KC-6.2.V.A
itself, so q2's key may say what the framework says about them. No item in this
module puts words in their mouths or in any other real person's; every stimulus
is an unattributed illustrative text. This is the topic where that temptation is
strongest, which is why it is stated here as well as in the module header.

WHAT THIS CANNOT DO: it cannot tell whether the history is right. It gates
structure, key/anchor agreement, notation, the absence of figure language, the
presence of a citation, and the arithmetic of the three data questions. The
history is gated by the claims below and by the rule in HISTORY_BRIEF.md that a
key must trace to a sentence in the CED.

NEGATIVE CONTROL: `python3 verify_w8_7.py --selftest`. It rotates all thirty
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
import w8_7

T_REACTIONS = w8_7._T_REACTIONS
T_METHODS = w8_7._T_METHODS
T_TRANSFERS = w8_7._T_TRANSFERS

ORGS = "Organizations recorded"
OPPOSING = "Of those, opposing the trend toward conflict"
INTENSIFYING = "Of those, acting in ways that intensified conflict"
MOVEMENTS = "Movements recorded"
NONVIOLENT = "Of those, whose campaigns were conducted without violence"
VIOLENT = "Of those, whose campaigns used violence"
TRANSFERS = "Transfers recorded"
TO_CONFLICT = "Of those, to a state already engaged in an armed conflict"
NOT_CONFLICT = "Of those, to a state not so engaged"


def _parts_sum_to_whole(table, whole, parts, what):
    """Every row's parts must total its whole.

    This is what makes the negative control mean anything on these tables. The
    corruption in `es_check` only ever makes a number LARGER, so a check of the
    form "this count is above zero" is monotone and can never fail: it reads the
    table without being able to object to anything in it. Sibling module 8.5
    shipped a first draft whose table check caught 1 of 12 corrupted cells for
    exactly that reason. Each row here states a whole and the two parts it was
    divided into, and every stem says the record placed each case under exactly
    one of the two headings, so the sum is a property of the data as the
    question describes it rather than a contrivance.
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
    """Both kinds in every decade, with the opposing kind the larger."""
    decades = cg.labels(table)
    total = dict(zip(decades, cg.col(table, ORGS)))
    opp = dict(zip(decades, cg.col(table, OPPOSING)))
    inten = dict(zip(decades, cg.col(table, INTENSIFYING)))
    assert decades == ["1950s", "1960s", "1970s", "1980s"], \
        f"the key speaks of every decade recorded and a distractor names two; rows {decades}"
    _parts_sum_to_whole(table, ORGS, [OPPOSING, INTENSIFYING], "organizations recorded")
    for d in decades:
        assert inten[d] > 0, (
            f"the key needs organizations of both kinds in {d}; the row records "
            f"{inten[d]} intensifying")
        assert opp[d] > inten[d], (
            f"the key needs the opposing kind to outnumber the intensifying kind in {d}; "
            f"the row reads {opp[d]} against {inten[d]}")
    # every distractor false on the same numbers
    assert any(inten[d] > 0 for d in decades), \
        "'only organizations opposing the trend are recorded' must be false"
    assert not all(inten[d] > opp[d] for d in decades), \
        "'intensifying organizations outnumber opposing ones in every decade' must be false"
    assert total["1980s"] > 0, \
        "'no organization of either kind is recorded in the 1980s' must be false"
    assert cg.ranked(table, ORGS)[0] != "1950s", \
        "'the decade recording the most organizations is the 1950s' must be false"
    return (f"opposing {opp} outnumbers intensifying {inten} in every decade with both "
            f"present, the two summing to the stated totals {total}, and all four "
            f"distractors recompute false")


def q10(table, item):
    """Both methods present in every region and neither accounting for all."""
    labs = cg.labels(table)
    total = dict(zip(labs, cg.col(table, MOVEMENTS)))
    nonv = dict(zip(labs, cg.col(table, NONVIOLENT)))
    viol = dict(zip(labs, cg.col(table, VIOLENT)))
    _parts_sum_to_whole(table, MOVEMENTS, [NONVIOLENT, VIOLENT], "movements recorded")
    for lab in labs:
        assert 0 < nonv[lab] < total[lab] and 0 < viol[lab] < total[lab], (
            f"the key needs both methods present and neither accounting for all in {lab}; "
            f"the row reads {nonv[lab]} without violence and {viol[lab]} with, of "
            f"{total[lab]}")
    # every distractor false on the same numbers
    assert any(nonv[l] > 0 for l in labs), \
        "'every movement surveyed used violence' must be false"
    assert nonv["Region three"] > 0, \
        "'no movement in region three campaigned without violence' must be false"
    assert cg.ranked(table, MOVEMENTS)[0] != "Region two", \
        "'region two recorded more movements than any other region' must be false"
    assert len(set(total.values())) > 1, \
        "'the three regions recorded the same number' must be false"
    return (f"both methods appear in every region, {nonv} without violence against {viol} "
            f"with, summing to the stated totals {total}, and all four distractors "
            f"recompute false")


def q20(table, item):
    """Transfers rise each decade and mostly go to states already fighting."""
    decades = cg.labels(table)
    total = dict(zip(decades, cg.col(table, TRANSFERS)))
    to_c = dict(zip(decades, cg.col(table, TO_CONFLICT)))
    not_c = dict(zip(decades, cg.col(table, NOT_CONFLICT)))
    assert decades == ["1960s", "1970s", "1980s"], \
        f"the key speaks of each successive decade; the rows are {decades}"
    _parts_sum_to_whole(table, TRANSFERS, [TO_CONFLICT, NOT_CONFLICT], "transfers recorded")
    seq = [total[d] for d in decades]
    assert all(b > a for a, b in zip(seq, seq[1:])), \
        f"the key says the number of transfers rose in each successive decade; it runs {seq}"
    for d in decades:
        assert to_c[d] > 0.5 * total[d], (
            f"the key needs most of {d}'s transfers to go to states already engaged; the "
            f"row reads {to_c[d]} of {total[d]}")
    # every distractor false on the same numbers
    assert not all(not_c[d] > 0.5 * total[d] for d in decades), \
        "'most transfers went to states not already engaged' must be false"
    assert seq[-1] > seq[0], "'the number of transfers fell after the 1960s' must be false"
    assert any(to_c[d] > 0 for d in decades), \
        "'no transfer went to a state already engaged in a conflict' must be false"
    assert len(set(seq)) > 1, \
        "'the three decades recorded the same number of transfers' must be false"
    return (f"transfers run {seq}, rising at every step, with {to_c} going to states "
            f"already engaged against {not_c} not, the parts summing to the stated wholes; "
            f"all four distractors recompute false")


TABLE_CHECKS = {4: q4, 10: q10, 20: q20}

CLAIMS = [
 ("many individuals and groups that opposed the trend toward conflict",
  "KC-6.2.V states that although conflict dominated much of the twentieth century, many individuals and groups, including states, opposed this trend, and that some individuals and groups, however, intensified the conflicts. An association formed to end the resort to war belongs to the first of those two categories, which the same sentence separates from the second."),

 ("The practice of nonviolence",
  "KC-6.2.V.A states that groups and individuals challenged the many wars of the century, and some, such as Mohandas Gandhi, Martin Luther King Jr., and Nelson Mandela, promoted the practice of nonviolence as a way to bring about political change. Nonviolence is the method the framework attaches to those three names; the item asks only what the framework says and puts no words in anyone's mouth."),

 ("further intensified conflict, which is how militarized states often responded",
  "KC-6.2.V.C states that militaries and militarized states often responded to the proliferation of conflicts in ways that further intensified conflict. A distractor reverses the effect into a reduction of conflict, so the anchor carries the effect together with the actor rather than either alone."),

 ("in each decade those opposing the trend outnumber those intensifying it",
  "KC-6.2.V states that MANY individuals and groups opposed the trend toward conflict while SOME, however, intensified the conflicts, which makes both kinds present and the opposing kind the larger. The survey is hypothetical and the keyed conclusion, with the falsity of every distractor, is recomputed from the table alone in q4 above."),

 ("challenging an existing power structure through the practice of nonviolence",
  "KC-6.2.V.A states that some who challenged the many wars of the century promoted the practice of nonviolence as a way to bring about political change. Announcing in advance that supporters will not resist arrest is that practice stated as a method, and the action is directed at a government rather than at civilians, which is what separates it from KC-6.2.V.D."),

 ("Many individuals and groups opposed the trend toward conflict, while some others intensified the conflicts",
  "KC-6.2.V puts both halves in one sentence: many individuals and groups, including states, opposed this trend, and some individuals and groups, however, intensified the conflicts. A distractor keeps one half and denies the other, so the anchor spans the whole two-sided claim."),

 ("movements that used violence against civilians in an effort to achieve political aims",
  "KC-6.2.V.D states that some movements used violence against civilians in an effort to achieve political aims. The framework's sentence is descriptive and the key states no more than it does; it assigns no responsibility for any particular episode and takes no side in any live dispute."),

 ("how the government wished its own actions to be understood by the public it addressed",
  "Skill 2.B, the suggested skill for this topic, asks for the point of view, purpose and audience of a source, and a press office statement is produced to shape public understanding rather than to measure outcomes. KC-6.2.V.C establishes the claim such a statement is placed to obscure, which is why the source cannot settle it."),

 ("some of those who challenged the wars promoted nonviolence, not all of them",
  "KC-6.2.V.A states that groups and individuals challenged the many wars of the century, and SOME, such as Mohandas Gandhi, Martin Luther King Jr., and Nelson Mandela, promoted the practice of nonviolence. The word some makes nonviolence one method among those used, so the correction must preserve it rather than replace one absolute with another."),

 ("movements of both kinds are recorded and neither kind accounts for all of them",
  "KC-6.2.V.A records that some who challenged existing power structures promoted the practice of nonviolence and KC-6.2.V.D that some movements used violence, so the framework describes both methods without making either universal. The survey is hypothetical and is recomputed from the table alone in q10 above."),

 ("Chile under Augusto Pinochet, Spain under Francisco Franco, Uganda under Idi Amin",
  "The CED prints these four beside KC-6.2.V.C as illustrative examples of responses that intensified conflict. The other lists are illustrative examples the framework prints beside the Non-Aligned Movement, beside states created by redrawn boundaries, beside proxy wars and beside regional trade agreements, all in other topics."),

 ("depends on the withdrawal of ordinary cooperation, which only the public can give or withhold",
  "KC-6.2.V.A states that some who challenged the wars of the century promoted the practice of nonviolence as a way to bring about political change, and a method that works by withholding cooperation must address those whose cooperation is at issue. Skill 2.B asks why a source addresses the audience it addresses."),

 ("militarized state responding to conflict in a way that further intensified it",
  "KC-6.2.V.C states that militaries and militarized states often responded to the proliferation of conflicts in ways that further intensified conflict, and the CED prints the buildup of the military-industrial complex and weapons trading beside that sentence. An argument that one state's purchase obliges another's is that pattern stated as a principle."),

 ("Some movements used violence against civilians in an effort to achieve political aims",
  "KC-6.2.V.D is the sentence, and its word SOME makes this one pattern among the reactions this topic covers rather than a universal. The same sentence attributes a political aim to the movements it describes, which is why the key carries both the method and the aim."),

 ("outside the country and opposed to the government it describes, which shapes what it reports and omits",
  "Skill 2.B asks for the point of view and historical situation of a source, and exile plus opposition is that situation stated. KC-6.2.V places both those who challenged existing power structures and those who upheld them inside the same period, so a source from one side is evidence about that side's account rather than a neutral record."),

 ("Ask what purpose each account served and whom each was written for",
  "Skill 2.B asks for the point of view, purpose, historical situation and audience of a source, which is a question to put to both accounts rather than a rule for ranking them. KC-6.2.V describes a century in which power structures were both upheld and challenged, so accounts from the two positions are expected to differ."),

 ("buildup of arms as a response to conflict that the framework treats as intensifying it further",
  "KC-6.2.V.C states that militaries and militarized states often responded to the proliferation of conflicts in ways that further intensified conflict, and the CED prints the buildup of the military-industrial complex and weapons trading beside it. A sustained expansion in military sales is that buildup reported commercially."),

 ("turned to violence in an effort to achieve political aims",
  "KC-6.2.V.D states that some movements used violence against civilians in an effort to achieve political aims, and a manifesto rejecting petition and election in favour of force announces that choice of method. KC-6.2.V.A describes the opposite choice inside the same topic, which is why it is the near-miss distractor and why the anchor carries the method with the aim."),

 ("produced by the government whose measures it describes and was aimed at an audience outside the country",
  "Skill 2.B asks for the purpose and audience of a source, and a state broadcast aimed abroad is made to secure a foreign reputation rather than to record domestic opinion. KC-6.2.V.C establishes that militarized states often responded to conflict in ways that intensified it, so a state's account of its own measures is the claim that needs independent support."),

 ("rose in each successive decade, and in every decade most went to states already engaged",
  "KC-6.2.V.C states that militaries and militarized states often responded to the proliferation of conflicts in ways that further intensified conflict, and the CED prints weapons trading beside it as an illustrative example. The record is hypothetical and both halves of the keyed claim, with the falsity of every distractor, are recomputed from the table alone in q20 above."),

 ("Conflict did dominate much of the century, but many individuals and groups opposed that trend",
  "KC-6.2.V states that ALTHOUGH conflict dominated much of the twentieth century, many individuals and groups, including states, opposed this trend. The framework grants the premise and adds the opposition, so the qualification keeps both halves; a distractor denies the premise instead, which is why the anchor spans both."),

 ("Shining Path and Al-Qaeda",
  "The CED prints Shining Path and Al-Qaeda beside KC-6.2.V.D as illustrative examples of movements that used violence. The other pairs are illustrative examples the framework prints beside nationalist parties, beside environmental movements, beside the Non-Aligned Movement and beside regional and ethnic movements, all in other topics."),

 ("make the campaign's method visible to the wider public whose support it sought",
  "KC-6.2.V.A states that some who challenged the wars of the century promoted the practice of nonviolence as a way to bring about political change, and a method that works through public sympathy has to be publicly known. Skill 2.B asks what purpose a source served and whom it addressed, which is what publication rather than internal circulation reveals."),

 ("Individuals, groups, and states alike",
  "KC-6.2.V states that many individuals and groups, INCLUDING STATES, opposed this trend. The inclusion of states is part of the framework's own sentence, so a key naming only individuals or only groups would drop what that sentence deliberately adds."),

 ("pressure brought by ordinary people on their own governments can affect the conduct of conflict",
  "KC-6.2.V.A states that groups and individuals challenged the many wars of the century and that some promoted the practice of nonviolence as a way to bring about political change, which rests on the belief that public pressure can move a government. Skill 2.B asks what point of view a source expresses."),

 ("challenged wars and promoted nonviolence, and movements that used violence against civilians",
  "KC-6.2.V.A describes those who challenged the many wars of the century and promoted the practice of nonviolence, and KC-6.2.V.D describes movements that used violence against civilians in an effort to achieve political aims. Unit 8 Learning Objective I asks for the VARIOUS reactions to existing power structures, and these are the contrasting pair, so the anchor carries both."),

 ("participant, long afterward, to explain and justify his own part",
  "Skill 2.B asks how a source's point of view, purpose and situation bear on its use, and a participant writing retrospectively to justify his own conduct has a purpose that shapes what the account can establish. KC-6.2.V.C states the effect such a memoir is placed to deny."),

 ("militaries and militarized states of the region responded to the conflicts already under way",
  "KC-6.2.V.C states that militaries and militarized states often responded to the proliferation of conflicts in ways that further intensified conflict, which is the framework's own explanation for conflict rising rather than falling. The reasoning process the CED prints beside this topic is causation."),

 ("ranged from opposing conflict and practising nonviolence to intensifying conflict and using violence against civilians",
  "KC-6.2.V sets opposition to the trend toward conflict beside its intensification, KC-6.2.V.A adds the promotion of nonviolence and KC-6.2.V.D the movements that used violence against civilians. Unit 8 Learning Objective I asks for the various reactions, and the range between those poles is what makes them various."),

 ("some of them through nonviolence, while militarized states often answered conflict in ways that deepened it",
  "KC-6.2.V supplies the dominance of conflict and the opposition to it including states, KC-6.2.V.A the promotion of nonviolence by some who challenged the wars, KC-6.2.V.C the militarized responses that further intensified conflict, and KC-6.2.V.D the movements that used violence against civilians. The key is the conjunction of those four with every quantifier intact."),
]

wh.run(w8_7, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
