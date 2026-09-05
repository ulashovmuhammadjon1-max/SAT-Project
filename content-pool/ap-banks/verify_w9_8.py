"""Key audit for AP WORLD HISTORY: MODERN 9.8 Institutions Developing in a
Globalized World.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code or Learning
Objective, for a human to audit. `wh_check` refuses any claim or `why` that
cites neither.

TITLE. Taken verbatim from WORLD_HISTORY_topics.json, one of four titles in this
territory the authoring brief records as reassembled by hand from interleaved
CED columns. It matches the CED page read in full.

THE SKILL IS WHAT MAKES THIS MODULE ITS OWN. Suggested skill 3.C -- compare the
arguments or main ideas of TWO sources -- is carried by no other topic in units
8 or 9. Fourteen items below set two unattributed sources side by side and key
the comparison: where they agree, where they diverge, and what each is arguing.
That is what keeps 9.8 from reading as a second copy of 9.7, whose skill is 2.C
and which asks about one source at a time.

"STATED" IS THE MOST IMPORTANT WORD ON THE PAGE. KC-6.3.II.A says new
international organizations, including the United Nations, formed with the
STATED GOAL of maintaining world peace and facilitating international
cooperation. The framework reports what these bodies declared they were for. It
does not say they achieved it, and whether they did is a live political argument
this course does not enter.

  * No claim below says any international organization succeeded or failed at
    keeping the peace, was effective or ineffective, or was worth having.
  * No claim says any state was right or wrong in its dealings with such a body.
  * q4, q12, q14, q19 and q29 turn on the word stated. q19 is the sharpest: it
    keys the difference between reporting a declared goal and endorsing a claim
    about what was accomplished. q28 keys a disagreement between two sources
    that the framework explicitly leaves open rather than resolving it.

ALSO NOT KEYED: the sentence says "new international organizations, INCLUDING
the United Nations", so the United Nations is one of a class rather than the
whole of it. q6 and q16 hold that open, because treating the sentence as being
about a single body would narrow it.

WHERE A DISTRACTOR IS THE SWAP OF THE KEY, THE ANCHOR CARRIES BOTH CLAUSES.
Six items are built on a reversal a prepared student could believe:

  q1   which of the two texts announces and which reserves judgement
  q6   "including the United Nations" swapped for "the United Nations alone"
  q8   the point of agreement and the point of difference exchanged
  q14  the NOT-supported item, where the key is deliberately the false claim
  q19  reporting a stated goal swapped for endorsing an achievement
  q21  institutions emerging swapped for institutions emerging and then stopping

For each the anchor spans the whole relation, so an anchor that matched the
swapped distractor would fail the gate rather than pass it. That defect is on
record in `verify_e2_1.py`.

NO REAL DOCUMENT IS QUOTED. No charter, resolution or treaty appears in this
module and no source is attributed to a real person or organization. Every
paired source is explicitly unattributed and illustrative, and each item turns on
comparing two arguments rather than on recognising who made them.

WHAT THIS CANNOT DO: it cannot tell whether the history is right. It gates
structure, key/anchor agreement, notation, the absence of figure language, the
presence of a citation, and the arithmetic of the three data questions.

NEGATIVE CONTROL: `python3 verify_w9_8.py --selftest`. It rotates all thirty
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
import w9_8

T_MEMBERSHIP = w9_8._T_MEMBERSHIP
T_FOUNDED = w9_8._T_FOUNDED
T_REGISTERED = w9_8._T_REGISTERED

MEMBERS = "Member states"
OLD_STATES = "Of those, states already independent in 1945"
NEW_STATES = "Of those, states that became independent later"
FOUNDED = "Organizations founded"
PEACE_PURPOSE = "Of those, whose stated purpose was maintaining peace or security"
OTHER_PURPOSE = "Of those, whose stated purpose was something else"
AGREEMENTS = "Agreements registered"
BILATERAL = "Of those, between two states only"
MULTILATERAL = "Of those, among three or more states"


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
    """Membership grows, and the growth is entirely in the later-independent column."""
    years = cg.labels(table)
    assert years == ["1945", "1965", "1985"], \
        f"the key speaks of every date recorded; the rows are {years}"
    _parts_sum_to_whole(table, MEMBERS, [OLD_STATES, NEW_STATES], "member states")
    total = cg.col(table, MEMBERS)
    old = cg.col(table, OLD_STATES)
    new = cg.col(table, NEW_STATES)
    assert all(b > a for a, b in zip(total, total[1:])), \
        f"the key says membership grew at every date; it runs {total}"
    assert len(set(old)) == 1, (
        f"the key attributes the growth to later-independent states, so the earlier-"
        f"independent column must not move; it runs {old}")
    assert all(b > a for a, b in zip(new, new[1:])), \
        f"the key needs the later-independent column to supply the growth; it runs {new}"
    # every distractor false on the same numbers
    assert total[-1] > total[0], \
        "'membership fell at each date after the first' must be false"
    assert old[-1] >= old[0], \
        "'the number already independent in 1945 fell across the record' must be false"
    assert not all(n > 0.5 * t for n, t in zip(new, total)), (
        "'later-independent states were a majority at every date' must be false; the "
        f"shares are {[round(n / t, 3) for n, t in zip(new, total)]}")
    assert total[1] != total[2], \
        "'membership was unchanged between the second and third dates' must be false"
    return (f"membership runs {total} with {old} already independent in 1945, unchanged, "
            f"and {new} independent later, rising; the parts sum to the stated wholes and "
            f"all four distractors recompute false")


def q7(table, item):
    """Foundings rise, and the non-peace purpose predominates in every decade."""
    decades = cg.labels(table)
    assert decades == ["1940s", "1960s", "1980s"], \
        f"the key speaks of each decade recorded; the rows are {decades}"
    _parts_sum_to_whole(table, FOUNDED, [PEACE_PURPOSE, OTHER_PURPOSE],
                        "organizations founded")
    total = cg.col(table, FOUNDED)
    peace = cg.col(table, PEACE_PURPOSE)
    other = cg.col(table, OTHER_PURPOSE)
    assert all(b > a for a, b in zip(total, total[1:])), \
        f"the key says the number founded rose in each decade; it runs {total}"
    for d, p, o in zip(decades, peace, other):
        assert o > p, (
            f"the key needs the other stated purposes to predominate in {d}; the row reads "
            f"{p} for peace or security against {o} for something else")
    # every distractor false on the same numbers
    assert not all(p > o for p, o in zip(peace, other)), \
        "'most were founded for peace or security in every decade' must be false"
    assert peace[0] > 0, \
        "'no organization founded in the 1940s had peace or security as its purpose' must be false"
    assert total[-1] > total[0], \
        "'the number founded fell in each decade after the first' must be false"
    assert len(set(total)) > 1, \
        "'the three decades recorded the same number founded' must be false"
    return (f"foundings run {total} with {peace} for peace or security against {other} for "
            f"other stated purposes, the latter predominating throughout; the parts sum to "
            f"the stated wholes and all four distractors recompute false")


def q10(table, item):
    """Registrations rise and the multilateral SHARE rises with them."""
    decades = cg.labels(table)
    assert decades == ["1950s", "1970s", "1990s"], \
        f"the key speaks of each decade recorded; the rows are {decades}"
    _parts_sum_to_whole(table, AGREEMENTS, [BILATERAL, MULTILATERAL],
                        "agreements registered")
    total = cg.col(table, AGREEMENTS)
    two = cg.col(table, BILATERAL)
    many = cg.col(table, MULTILATERAL)
    assert all(b > a for a, b in zip(total, total[1:])), \
        f"the key says registrations rose in each decade; they run {total}"
    shares = [m / t for m, t in zip(many, total)]
    assert all(b > a for a, b in zip(shares, shares[1:])), (
        f"the key says the three-or-more portion rose AS A SHARE; the shares run "
        f"{[round(s, 3) for s in shares]}")
    # every distractor false on the same numbers
    assert total[-1] > total[0], \
        "'registrations fell in each decade after the first' must be false"
    assert shares[-1] > shares[0], \
        "'the three-or-more share fell across the record' must be false"
    assert all(b > a for a, b in zip(two, two[1:])), \
        "'agreements between two states only fell in each decade' must be false"
    assert not all(s > 0.5 for s in shares), (
        "'most agreements were among three or more states in every decade' must be false; "
        f"the shares are {[round(s, 3) for s in shares]}")
    return (f"registrations run {total} and the three-or-more share "
            f"{[round(s, 3) for s in shares]}, both rising, against {two} bilateral, which "
            f"also rise; the parts sum to the stated wholes and all four distractors "
            f"recompute false")


TABLE_CHECKS = {3: q3, 7: q7, 10: q10}

CLAIMS = [
 ("Text 1 announces it while Text 2 reserves judgement on whether it will be met",
  "KC-6.3.II.A states that new international organizations, including the United Nations, formed with the STATED GOAL of maintaining world peace and facilitating international cooperation. The framework records what such bodies declared, and skill 3.C asks a student to compare two sources' main ideas; a distractor exchanges which text does which, so the anchor names both roles in order."),

 ("Maintaining world peace and facilitating international cooperation",
  "KC-6.3.II.A names both as the stated goal of the new international organizations. Two distractors offer one half without the other, so the anchor carries both."),

 ("growth came from states that became independent after 1945",
  "KC-6.3.II.A supplies the organizations formed with a stated goal of peace and cooperation, and KC-6.2.III.A.i in Topic 8.6 the creation of new states from redrawn boundaries after colonial withdrawals. A membership growing from later-independent states joins those two, and the record is hypothetical, with the key recomputed from the table alone in q3 above."),

 ("reports their stated goal and does not assess their results",
  "KC-6.3.II.A's word is STATED: it records the declared purpose of these organizations and returns no verdict on the outcome, which is a live political argument this course does not enter. The anchor carries both the reporting and the abstention, because distractors supply a verdict in each direction."),

 ("membership as changing how a state can act toward others, though they value the change differently",
  "Unit 9 Learning Objective H asks how and why globalization changed international interactions among states, and KC-6.3.II.A supplies the organizations through which those interactions ran. Skill 3.C asks a student to compare two sources' main ideas, and the shared premise here is that membership alters what a state can do, which the two sources then evaluate oppositely."),

 ("INCLUDING the United Nations, so it names one among several",
  "KC-6.3.II.A states that NEW INTERNATIONAL ORGANIZATIONS, INCLUDING the United Nations, formed with the stated goal of maintaining world peace and facilitating international cooperation. Including makes the United Nations an instance of a wider class, and a distractor makes it the whole of the sentence, so the anchor carries the word and its consequence."),

 ("in every decade most were founded for a stated purpose other than peace or security",
  "KC-6.3.II.A names two stated goals, maintaining world peace AND facilitating international cooperation, so cooperation covers purposes wider than peace and security alone. The record is hypothetical and is recomputed from the table alone in q7 above."),

 ("disagree about where a settlement should be sought, while agreeing that a settlement is needed",
  "Skill 3.C asks a student to compare the arguments or main ideas of two sources, which means locating the shared ground and the point of difference. KC-6.3.II.A supplies the international bodies formed with the stated goal of facilitating international cooperation, and a distractor exchanges the agreement and the disagreement, so the anchor carries both in order."),

 ("how globalization changed international interactions among states",
  "Unit 9 Learning Objective H, printed on this topic's page, is to explain how and why globalization changed international interactions among states, and KC-6.3.II.A supplies the new organizations in which those interactions came to be conducted. A shift from bilateral capitals to permanent conference halls is that change described by a participant."),

 ("share among three or more states rose with it",
  "KC-6.3.II.A states that new international organizations formed with the stated goal of facilitating international cooperation, and a rising proportion of agreements binding three or more states at once is one form such cooperation takes. The record is hypothetical and is recomputed from the table alone in q10 above."),

 ("value the organization for facilitating cooperation, but each identifies a different beneficiary",
  "KC-6.3.II.A names facilitating international cooperation among the stated goals of these organizations, and both delegations describe a form of that cooperation. Skill 3.C asks for a comparison of two sources' main ideas, and the shared object with different beneficiaries is what the comparison yields."),

 ("aims as stated, but no assessment of whether they were met",
  "KC-6.3.II.A records that these organizations formed with the STATED GOAL of maintaining world peace and facilitating international cooperation. The framework supplies the declared aim and stops; whether it was met is a matter on which people disagree and on which this course takes no position."),

 ("identify a form of international cooperation as valuable, but they identify different forms",
  "KC-6.3.II.A names facilitating international cooperation among the stated goals of the new international organizations, and technical work and a standing forum are two forms cooperation can take. Skill 3.C asks a student to compare two sources' main ideas, and here they agree on the category and differ within it."),

 ("records that these organizations achieved the goal they were founded for",
  "KC-6.3.II.A records the STATED GOAL and says nothing about achievement, so a claim that the course records their achievement is the one the framework does not support. The item asks which statement is NOT supported, so the anchor is pinned to the false one deliberately; the other four restate parts of that sentence."),

 ("membership as consequential, one for the state's position abroad and one for its conduct at home",
  "Unit 9 Learning Objective H asks how and why globalization changed international interactions among states, and KC-6.3.II.A supplies the organizations through which the change ran. Skill 3.C asks for a comparison of two sources' main ideas, and both texts treat membership as consequential while locating the consequence in different places, so the anchor carries both locations."),

 ("named as one of the new international organizations rather than as the only one",
  "KC-6.3.II.A states that new international organizations, INCLUDING the United Nations, formed with the stated goal of maintaining world peace and facilitating international cooperation. Including places the United Nations inside a wider class and gives it the same stated goal as the rest of that class."),

 ("judged by its effect on disputes but propose different measures of that effect",
  "Skill 3.C asks a student to compare the arguments or main ideas of two sources, locating shared ground and divergence. KC-6.3.II.A gives maintaining world peace as one of these bodies' stated goals, and the two texts propose different measures of the same thing; the framework supplies no verdict, so neither text is keyed as correct."),

 ("international cooperation these organizations were formed to facilitate",
  "KC-6.3.II.A states that new international organizations formed with the stated goal of maintaining world peace and FACILITATING INTERNATIONAL COOPERATION, and a hundred delegations voting on one text is that facilitation in operation. Military alliances belong to KC-6.2.IV.D and trade agreements to KC-6.3.II.B in other topics."),

 ("Reporting a goal an organization declared is not the same as endorsing a claim about what it accomplished",
  "KC-6.3.II.A's word is STATED. The framework records what these bodies declared themselves to be for, which leaves entirely open what they achieved, and a course reporting the declaration is not thereby making the further claim. This is the sharpest statement in the module of the distinction the whole topic rests on, and the anchor carries both halves of it."),

 ("different accounts of what makes such organizations effective, one resting on obligation and one on the interests of powerful states",
  "Skill 3.C asks a student to compare the arguments of two sources, and here the two propose different mechanisms for the same phenomenon. KC-6.3.II.A establishes that such organizations were formed with a stated goal, and the framework explains neither mechanism, so the key describes the disagreement rather than settling it."),

 ("emerged and continued to develop throughout the century",
  "KC-6.3, which the CED reprints as a review key concept in Topic 8.9, states that new institutions of global association EMERGED AND CONTINUED TO DEVELOP THROUGHOUT THE CENTURY. Both halves of that phrase are the framework's own and a distractor keeps only the emergence, so the anchor carries both."),

 ("authority comes from its members, and they disagree about how far that authority extends",
  "KC-6.3.II.A places these organizations among the institutions through which states dealt with one another, and their authority is what their members confer. Skill 3.C asks a student to compare two sources' main ideas, and here a shared premise about the source of authority frames a disagreement about its extent."),

 ("how many of its agreements bound it to two or more other states at once",
  "Unit 9 Learning Objective H asks how and why globalization changed international interactions among states, and KC-6.3.II.A supplies the organizations formed to facilitate international cooperation. How many states an agreement binds at once is the direct measure of whether dealings became multilateral."),

 ("explain the growth of these organizations, but they attribute it to different motives",
  "The reasoning process the CED prints beside this topic is causation, and skill 3.C asks a student to compare two sources' arguments. KC-6.3, reprinted in Topic 8.9, records that new institutions of global association emerged and continued to develop throughout the century; the framework supplies the growth and not its motive, so the key describes two accounts without endorsing either."),

 ("Maintaining world peace, and facilitating international cooperation",
  "KC-6.3.II.A names exactly those two as the stated goal of the new international organizations formed in this period. Each distractor attaches one of the framework's goals to a development stated in a different sentence of this course, which is the cross-sentence error a pairing item is built to catch."),

 ("differ over whether membership or conduct is the test",
  "Skill 3.C asks a student to compare the arguments or main ideas of two sources, naming the common ground and the disagreement. KC-6.3.II.A establishes the organizations and their stated goal, and the framework provides no test of usefulness, so the key reports the two proposed tests rather than choosing between them."),

 ("institutions of global association that emerged and continued to develop through the century",
  "KC-6.3, reprinted as a review key concept in Topic 8.9, states that new institutions of global association emerged and continued to develop throughout the century, and KC-6.3.II.A names the international organizations formed with a stated goal of peace and cooperation. Two hundred standing bodies is that development counted."),

 ("made a difference to its members' conduct, which the framework does not settle",
  "KC-6.3.II.A records the STATED GOAL of these organizations and returns no verdict on their effect, so the disagreement between the two texts is exactly the question the framework leaves open. Skill 3.C asks a student to compare two sources' main ideas, and locating an unsettled question is part of that comparison; the anchor carries both the disagreement and the framework's silence."),

 ("United Nations is among them, and that their stated goal was world peace and international cooperation",
  "KC-6.3.II.A is one sentence containing exactly three assertions: that new international organizations formed, that the United Nations is among them, and that their stated goal was maintaining world peace and facilitating international cooperation. The key states all three and each distractor either removes one or adds a verdict the framework withholds."),

 ("declaring that they existed to keep the peace and to make cooperation between states easier, and such institutions went on developing across the century",
  "KC-6.3.II.A supplies the new organizations, the United Nations among them, and their stated goal, while KC-6.3 supplies institutions of global association emerging and continuing to develop throughout the century. The key is the conjunction of those with the declaration reported and no verdict added, and each distractor either contradicts one or supplies a verdict the framework withholds."),
]

wh.run(w9_8, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
