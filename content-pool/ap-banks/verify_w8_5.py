"""Key audit for AP WORLD HISTORY: MODERN 8.5 Decolonization After 1900.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code or Learning
Objective, for a human to audit. `wh_check` refuses any claim or `why` that
cites neither, because a key traceable only to an author's knowledge of the
twentieth century cannot be checked by anyone reading this bank later.

WHERE A DISTRACTOR IS THE SWAP OF THE KEY, THE ANCHOR CARRIES BOTH CLAUSES.
Eight items here are built on a reversal a prepared student could believe:

  q2   negotiated and armed struggle exchanged between the two clauses
  q6   India and Algeria exchanged between the two illustrative lists
  q8   the direction of travel reversed, independence back toward autonomy
  q10  a negotiated transfer read as an armed struggle
  q15  an armed struggle read as a negotiated transfer
  q17  the NOT-supported item, where the key is deliberately the false claim
  q21  outcome and process exchanged between "same" and "differed"
  q24  the second NOT-supported item, on the half of KC-6.2.II.B that a
       distractor strikes out

For each of those the anchor spans the whole relation and not just one noun, so
an anchor that matched the swapped distractor would fail the gate rather than
pass it. That defect is on record in `verify_e2_1.py`.

THE CONTENT RISK IN THIS TOPIC IS THE WORD "VARYING", and five claims below say
so. KC-6.2.II.A says nationalist leaders and parties sought VARYING DEGREES of
autonomy within OR independence from imperial rule. In a topic titled
Decolonization the tempting error is to key every nationalist party as
demanding outright independence, which would teach the opposite of the
framework's own sentence. KC-6.2.I.C's "some ... while others" and KC-6.2.II.B's
"some of these movements" carry the same load for the other two statements, and
the three data questions exist to make those quantifiers countable rather than
to assert how common either route actually was.

WHAT THIS CANNOT DO: it cannot tell whether the history is right. It gates
structure, key/anchor agreement, notation, the absence of figure language, the
presence of a citation, and the arithmetic of the three data questions. The
history is gated by the claims below and by the rule in HISTORY_BRIEF.md that a
key must trace to a sentence in the CED.

NEGATIVE CONTROL: `python3 verify_w8_5.py --selftest`. It rotates all thirty
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
import w8_5

T_DEGREES = w8_5._T_DEGREES
T_PATHS = w8_5._T_PATHS
T_MOVEMENTS = w8_5._T_MOVEMENTS

SURVEYED = "Programmes surveyed"
WITHIN = "Of those, seeking greater autonomy within imperial rule"
FROM = "Of those, seeking full independence from imperial rule"
BECOMING = "Colonies becoming independent"
NEGOTIATED = "Of those, independence negotiated"
ARMED = "Of those, independence following armed struggle"
RECORDED = "Movements recorded"
AUTONOMY = "Of those, stated aim was autonomy"
SEPARATE = "Of those, stated aim was a separate state"


def _parts_sum_to_whole(table, whole, parts, what):
    """Every row's parts must total its whole.

    This is the assertion that makes the negative control mean anything. The
    corruption in `es_check` only ever makes a number LARGER, so a check of the
    form "this count is above zero" is monotone and can never fail -- it reads
    the table without being able to object to anything in it. Each row here
    states a whole and the two parts it was divided into, so corrupting any one
    of the three breaks the sum and is caught. Every stem says the survey placed
    each case under exactly one of the two headings, so this is a property of
    the data as the question describes it, not a contrivance.
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
    """Both aims appear in both regions -- the framework's 'varying degrees'."""
    labs = cg.labels(table)
    within = dict(zip(labs, cg.col(table, WITHIN)))
    indep = dict(zip(labs, cg.col(table, FROM)))
    surveyed = dict(zip(labs, cg.col(table, SURVEYED)))
    assert sorted(labs) == ["Africa", "Asia"], \
        f"KC-6.2.II.A names Asia and Africa; the table's rows are {labs}"
    _parts_sum_to_whole(table, SURVEYED, [WITHIN, FROM], "programmes surveyed")
    for lab in labs:
        assert within[lab] > 0 and indep[lab] > 0, (
            f"the key needs both aims present in {lab}; the row reads "
            f"{within[lab]} within and {indep[lab]} independence")
    # every distractor false on the same numbers
    assert within["Asia"] > 0, \
        "'every programme surveyed in Asia sought full independence' must be false"
    assert within["Africa"] > 0, \
        "'no programme recorded in Africa sought greater autonomy' must be false"
    assert indep["Africa"] <= indep["Asia"], \
        "'Africa recorded more programmes seeking full independence than Asia' must be false"
    assert len(set(surveyed.values())) > 1, \
        "'the two regions surveyed the same number of programmes' must be false"
    return (f"both aims are present in both regions, {within} within against {indep} "
            f"independence, the two parts summing to the stated totals {surveyed}, and "
            f"all four distractors recompute false")


def q9(table, item):
    """Both routes are recorded in every decade -- KC-6.2.I.C's 'some ... others'."""
    decades = cg.labels(table)
    neg = dict(zip(decades, cg.col(table, NEGOTIATED)))
    arm = dict(zip(decades, cg.col(table, ARMED)))
    assert decades == ["1940s", "1950s", "1960s", "1970s"], (
        f"the key speaks of every decade the table covers and a distractor of the decades "
        f"after the 1950s, so the four decades must be these in order; they are {decades}")
    _parts_sum_to_whole(table, BECOMING, [NEGOTIATED, ARMED], "colonies becoming independent")
    for d in decades:
        assert neg[d] > 0 and arm[d] > 0, (
            f"the key needs both routes recorded in {d}; the row reads {neg[d]} "
            f"negotiated and {arm[d]} following armed struggle")
    # every distractor false on the same numbers
    for d in decades:
        assert arm[d] <= neg[d], (
            f"'in at least one decade more independences followed armed struggle than "
            f"were negotiated' must be false, but {d} reads {arm[d]} against {neg[d]}")
    assert neg["1960s"] > 0 and neg["1970s"] > 0, \
        "'negotiated independence ceased after the 1950s' must be false"
    most_neg = cg.ranked(table, NEGOTIATED)[0]
    fewest_arm = cg.ranked(table, ARMED)[-1]
    assert most_neg != fewest_arm, (
        "'the decade with the most negotiated independences also recorded the fewest "
        "following armed struggle' must be false")
    assert sum(arm.values()) < sum(neg.values()), \
        "'more independences followed armed struggle than were negotiated' must be false"
    return (f"every decade records both routes, negotiated {neg} against armed {arm}, the "
            f"two summing to the stated totals; the decade of most negotiated ({most_neg}) "
            f"is not the decade of fewest armed ({fewest_arm}), and all four distractors "
            f"recompute false")


def q12(table, item):
    """Autonomy is one aim among others in every movement type."""
    labs = cg.labels(table)
    total = dict(zip(labs, cg.col(table, RECORDED)))
    auto = dict(zip(labs, cg.col(table, AUTONOMY)))
    sep = dict(zip(labs, cg.col(table, SEPARATE)))
    assert sorted(labs) == ["Ethnic", "Regional", "Religious"], (
        f"KC-6.2.II.B names regional, religious and ethnic movements; the rows are {labs}")
    _parts_sum_to_whole(table, RECORDED, [AUTONOMY, SEPARATE], "movements recorded")
    for lab in labs:
        assert auto[lab] > 0 and sep[lab] > 0, (
            f"the key needs both aims present among the {lab} movements; the row reads "
            f"{auto[lab]} for autonomy and {sep[lab]} for a separate state")
    # every distractor false on the same numbers
    assert auto["Religious"] > 0, \
        "'no religious movement stated autonomy as its aim' must be false"
    majorities = [lab for lab in labs if auto[lab] > 0.5 * total[lab]]
    assert majorities != ["Regional"], (
        "'regional movements are the only type in which a majority stated autonomy' must "
        f"be false; the types with a majority are {majorities}")
    assert len(set(total.values())) > 1, \
        "'the three types recorded the same number' must be false"
    return (f"autonomy is stated by {auto} and a separate state by {sep}, the two summing "
            f"to the recorded totals {total}, with majorities for autonomy in "
            f"{majorities}, and all four distractors recompute false")


TABLE_CHECKS = {4: q4, 9: q9, 12: q12}

CLAIMS = [
 ("varying degrees of autonomy within, or independence from, imperial rule",
  "KC-6.2.II.A states that nationalist leaders and parties in Asia and Africa sought varying degrees of autonomy within or independence from imperial rule. Two programmes in one colony asking for different amounts of self-rule are that range of degrees visible in one place, which is what the word varying names."),

 ("Some colonies negotiated their independence, while others achieved independence through armed struggle",
  "KC-6.2.I.C states that after the end of World War II, some colonies negotiated their independence, while others achieved independence through armed struggle. A distractor exchanges the two halves of that sentence, so the anchor carries the whole of it rather than either route alone."),

 ("challenging the imperial boundaries a new state had inherited",
  "KC-6.2.II.B states that regional, religious, and ethnic movements challenged colonial rule and inherited imperial boundaries. A frontier drawn by a departed empire and still in force after independence is an inherited imperial boundary, and contesting it is the second of the two targets the framework names."),

 ("some programmes sought autonomy within imperial rule and others sought full independence",
  "KC-6.2.II.A records varying degrees of autonomy within or independence from imperial rule among nationalist parties in Asia and Africa. The survey is hypothetical, and the keyed conclusion together with the falsity of all four distractors is recomputed from the table alone in q4 above."),

 ("varying degrees of autonomy within, or independence from, imperial rule that nationalist parties sought",
  "KC-6.2.II.A distinguishes autonomy WITHIN imperial rule from independence FROM it, which is the distinction the memorandum reports. KC-6.2.I.C's distinction between negotiated and armed routes concerns how independence was reached rather than how much self-rule was demanded, so the anchor names the range and its subject together."),

 ("India from the British Empire illustrates negotiated independence, and Algeria from the French empire illustrates independence through armed struggle",
  "The CED prints India from the British Empire, the Gold Coast from the British Empire and French West Africa as illustrative examples of negotiated independence, and Algeria from the French empire, Angola from the Portuguese empire and Vietnam from the French empire as illustrative examples of independence through armed struggle, all beside KC-6.2.I.C. A distractor exchanges the two cases, so the anchor carries each case together with its own process."),

 ("regional movements that advocated for autonomy rather than a separate state",
  "KC-6.2.II.B states that regional, religious, and ethnic movements challenged colonial rule and inherited imperial boundaries, and that SOME of these movements advocated for autonomy. The word some makes autonomy one of the aims such movements held rather than a disqualification from the category."),

 ("from autonomy within imperial rule to independence from it",
  "KC-6.2.II.A places autonomy within imperial rule and independence from imperial rule at two ends of a range of varying degrees. A distractor reverses the direction of travel along that range, so the anchor names the starting point and the end point in order rather than the pair alone."),

 ("Both processes are recorded in every decade",
  "KC-6.2.I.C asserts that both processes occurred after the end of World War II rather than that either was the more frequent. The record is hypothetical, and the keyed conclusion with the falsity of every distractor is recomputed from the table alone in q9 above."),

 ("negotiated independence, as distinct from independence achieved through armed struggle",
  "KC-6.2.I.C names two processes after the end of World War II. A conference with a colony's elected leaders and an announced transfer date is the negotiated one, and because the reversed reading is the error the item is built to catch, the anchor names the process together with the one it is distinct from."),

 ("varying degrees of autonomy within or independence from imperial rule, so some asked for less than independence",
  "KC-6.2.II.A's phrase varying degrees rules out the claim that every party demanded the maximum and equally rules out the opposite absolute. The correction must preserve the range, so the anchor carries the framework's qualifier together with its consequence."),

 ("some movements sought autonomy and others sought a separate state",
  "KC-6.2.II.B states that SOME of the regional, religious, and ethnic movements advocated for autonomy. A survey in which autonomy is one aim among others in every type is that word made countable; the figures are hypothetical and are recomputed from the table alone in q12 above."),

 ("challenged colonial rule and also challenged the imperial boundaries that independent states inherited",
  "KC-6.2.II.B names both targets in one sentence, colonial rule and inherited imperial boundaries. A distractor keeps one target and drops the other, so the anchor carries both."),

 ("In Asia and in Africa",
  "KC-6.2.II.A states that nationalist leaders and parties in Asia and Africa sought varying degrees of autonomy within or independence from imperial rule. The framework names both regions in that sentence, and a key naming one of the two would drop half of what it asserts."),

 ("independence achieved through armed struggle, one of the two routes the course names",
  "KC-6.2.I.C states that after the end of World War II some colonies negotiated their independence while others achieved independence through armed struggle. A front reporting years of fighting until the imperial government withdraws describes the second route, and the anchor names which of the two it is so the reversed reading cannot match."),

 ("regional, religious, and ethnic movements that challenged colonial rule and inherited imperial boundaries",
  "KC-6.2.II.B names regional, religious, and ethnic movements as a category distinct from the nationalist parties of KC-6.2.II.A. A community asking for a political unit of its own inside a colony belongs to that category rather than to a party speaking for the whole colony."),

 ("Every colony that became independent after World War II reached that outcome by the same process",
  "KC-6.2.I.C asserts that the processes differed, some colonies negotiating their independence while others achieved it through armed struggle, so a single common process is the statement the framework does not support. The item asks which claim is NOT supported, so the anchor is pinned to the false statement deliberately; the other four restate KC-6.2.I.C, KC-6.2.II.A and KC-6.2.II.B."),

 ("processes by which various peoples pursued independence after 1900",
  "Unit 8 Learning Objective F is to compare the processes by which various peoples pursued independence after 1900, and the reasoning process the CED prints beside this topic is comparison. The distractors name learning objectives belonging to other topics in this course."),

 ("a degree of autonomy within imperial rule rather than for independence from it",
  "KC-6.2.II.A says nationalist leaders and parties sought varying degrees of autonomy WITHIN or independence FROM imperial rule, so a demand for internal self-government inside the empire is one of the degrees that sentence covers. A distractor reads it as a disguised demand for independence, which would erase the distinction the framework's wording draws, so the anchor carries both sides of it."),

 ("same process by which independence was pursued, and each reflects the position of the moment in which it was written",
  "Unit 8 Learning Objective F asks for a comparison of the processes by which peoples pursued independence, and KC-6.2.I.C establishes that those processes differed from case to case. Two accounts of one process written in different situations can both report it while framing it differently, which is what skill 5.B's relating of one development to another requires."),

 ("outcome was the same in both cases, while the process by which it was reached differed",
  "KC-6.2.I.C places a common outcome, independence, at the end of two different processes, negotiation and armed struggle. A distractor exchanges outcome and process between same and differed, so the anchor carries the whole comparison rather than either term."),

 ("sought varying degrees, so an elected majority might satisfy some of them and not others",
  "KC-6.2.II.A states that nationalist leaders and parties sought varying degrees of autonomy within or independence from imperial rule. Where the aims vary, one concession sits at a single point on the range and cannot by itself meet demands sitting further along it."),

 ("Indian National Congress, Ho Chi Minh in French Indochina, Kwame Nkrumah in the British Gold Coast, and Gamal Abdel Nasser",
  "The CED prints these four beside KC-6.2.II.A as illustrative examples of nationalist leaders and parties. The other lists are illustrative examples the framework prints beside the regional, religious, and ethnic movements of KC-6.2.II.B and beside statements in other topics, on redrawn boundaries, on free-market policies and on proxy wars."),

 ("but never questioned the boundaries independent states inherited",
  "KC-6.2.II.B states that regional, religious, and ethnic movements challenged colonial rule AND inherited imperial boundaries, so a statement that they never questioned inherited boundaries strikes out half of that sentence and is the one the framework does not support. The item asks which claim is NOT supported, so the anchor is pinned to the false statement deliberately."),

 ("degree of self-rule each movement demanded, and the process by which independence was eventually reached",
  "KC-6.2.II.A supplies the first feature, the varying degrees of autonomy or independence sought, and KC-6.2.I.C the second, the difference between negotiated independence and independence through armed struggle. Unit 8 Learning Objective F asks for a comparison of processes, which those two features between them describe."),

 ("pressed varying demands on imperial rule, and independence when it came was reached through negotiation in some cases and armed struggle in others",
  "KC-6.2.II.A describes the varying demands nationalist leaders and parties made of imperial rule and KC-6.2.I.C the two processes by which independence was reached after the end of World War II. Skill 5.B asks how one development relates to another, so the anchor carries both developments in the order the framework sets them."),

 ("how much self-rule to demand and how quickly, within the range the course describes",
  "KC-6.2.II.A states that nationalist leaders and parties sought varying degrees of autonomy within or independence from imperial rule, which is a range along which immediate independence and a staged transfer sit at different points. The pamphlet takes a position on that range rather than disputing whether imperial rule existed."),

 ("Regional, religious, and ethnic movements challenged colonial rule and inherited imperial boundaries",
  "KC-6.2.II.B is the sentence a petition for frontiers other than the ones an empire drew belongs to. KC-6.2.II.A concerns the degree of self-rule a nationalist party sought for a whole colony rather than where its borders should lie, which is why the two are the near-miss pair here."),

 ("degree of self-rule demanded and the process by which independence was reached",
  "KC-6.2.II.A records varying degrees of autonomy or independence sought and KC-6.2.I.C records negotiated independence alongside independence through armed struggle, so those are the framework's own two axes of variation. It describes no variation in whether the territories were under imperial rule or in whether independence produced a state."),

 ("asked for varying amounts of self-rule, independence after 1945 came by negotiation in some places and by armed struggle in others",
  "KC-6.2.II.A supplies the varying degrees sought in Asia and Africa, KC-6.2.I.C the two processes after the end of World War II, and KC-6.2.II.B the regional, religious, and ethnic movements challenging colonial rule and inherited imperial boundaries. The key is the conjunction of the three and each distractor contradicts at least one."),
]

wh.run(w8_5, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
