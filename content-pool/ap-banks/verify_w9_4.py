"""Key audit for AP WORLD HISTORY: MODERN 9.4 Economics in the Global Age.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code or Learning
Objective, for a human to audit. `wh_check` refuses any claim or `why` that
cites neither.

THREE PIECES OF WORDING CARRY THIS TOPIC, and each is where a bank goes wrong:

  * "In a trend ACCELERATED BY the end of the Cold War" (KC-6.3.I.D). The end of
    the Cold War sped up something already running; it did not begin it. q6 and
    q18 key that distinction, q6 against a distractor that has the trend
    beginning in 1989.
  * "knowledge economies IN SOME REGIONS" (KC-6.3.I.E). Not everywhere. q4 keys
    the qualifier, q13's survey makes it countable, and q16's NOT-supported item
    is built on flattening it into uniform growth.
  * "REFLECTED the spread of principles and practices" (KC-6.3.II.B).
    Institutions, corporations and trade agreements are described as reflecting
    the spread, not as causing it. q9 and q24 hold that verb where the framework
    put it.

CONTESTED GROUND. Whether free-market policies were good for the countries that
adopted them is a live political argument, and the CED's own illustrative list
names four governments about which people disagree sharply. NO claim below says
those policies succeeded or failed, helped or harmed, or that any of the four
governments was right or wrong. q10 asks only which list the CED prints, and
says so. The objections to global integration have their own place in the course
-- KC-6.3.II.C in Topic 9.5 and KC-6.3.IV.iv in Topic 9.7 -- so they are neither
smuggled in here nor argued away.

DEDUPE, WHICH IS SHARPER HERE THAN ANYWHERE ELSE IN THIS TERRITORY. Topic 8.4 is
also an ECN topic and also carries suggested skill 2.C, so two banks written the
same way would be the same bank with the nouns changed. 8.4 has the state
DIRECTING an economy and leans on 2.C in its narrow form -- what a source cannot
show, what limits its use. 9.4 has the state WITHDRAWING, its reasoning process
is continuity and change, and where it uses 2.C it uses the other half, the
SIGNIFICANCE of a point of view: q5, q15, q20 and q22 ask what a position let a
source see, not merely what it prevents it from seeing.

WHERE A DISTRACTOR IS THE SWAP OF THE KEY, THE ANCHOR CARRIES BOTH CLAUSES.
Seven items are built on a reversal a prepared student could believe:

  q6   a trend accelerated swapped for a trend begun
  q8   knowledge economies and manufacturing exchanged between regions
  q9   reflected swapped for caused
  q12  Asia and Latin America swapped for Europe and North America
  q16  the NOT-supported item, where the key is deliberately the false claim
  q24  reflected swapped for caused again, as a correction
  q26  what changed and what continued exchanged

For each the anchor spans the whole relation, so an anchor that matched the
swapped distractor would fail the gate rather than pass it. That defect is on
record in `verify_e2_1.py`.

WHAT THIS CANNOT DO: it cannot tell whether the history is right. It gates
structure, key/anchor agreement, notation, the absence of figure language, the
presence of a citation, and the arithmetic of the three data questions.

NEGATIVE CONTROL: `python3 verify_w9_4.py --selftest`. It rotates all thirty
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
import w9_4

T_MANUFACTURING = w9_4._T_MANUFACTURING
T_AGREEMENTS = w9_4._T_AGREEMENTS
T_SECTORS = w9_4._T_SECTORS

OUTPUT = "Total output"
ALAC = "Of that, produced in Asia and Latin America"
ELSEWHERE = "Of that, produced elsewhere"
IN_FORCE = "Agreements in force"
CROSS_REGION = "Of those, joining states of more than one region"
ONE_REGION = "Of those, joining states of a single region"
WORKERS = "Workers recorded"
ICT = "Of those, in information and communications services"
OTHER_SECTORS = "Of those, in other sectors"


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
    """Output rises and the Asia-and-Latin-America SHARE rises with it."""
    periods = cg.labels(table)
    assert periods == ["1970", "1985", "2000"], \
        f"the key speaks of each period recorded; the rows are {periods}"
    _parts_sum_to_whole(table, OUTPUT, [ALAC, ELSEWHERE], "world manufacturing output")
    total = cg.col(table, OUTPUT)
    here = cg.col(table, ALAC)
    there = cg.col(table, ELSEWHERE)
    assert all(b > a for a, b in zip(total, total[1:])), \
        f"the key says total output rose in each period; it runs {total}"
    shares = [h / t for h, t in zip(here, total)]
    assert all(b > a for a, b in zip(shares, shares[1:])), (
        f"the key says the Asia and Latin America portion rose AS A SHARE; the shares run "
        f"{[round(s, 3) for s in shares]}")
    # every distractor false on the same numbers
    assert total[-1] > total[0], \
        "'total output fell in each period after the first' must be false"
    assert shares[-1] > shares[0], \
        "'the Asia and Latin America share fell across the record' must be false"
    assert all(b > a for a, b in zip(there, there[1:])), \
        "'output produced elsewhere fell in each period' must be false"
    assert not all(s > 0.5 for s in shares), (
        "'Asia and Latin America produced more than half in every period' must be false; "
        f"the shares are {[round(s, 3) for s in shares]}")
    return (f"output runs {total} and the Asia and Latin America share "
            f"{[round(s, 3) for s in shares]}, both rising, against {there} produced "
            f"elsewhere; the parts sum to the stated wholes and all four distractors "
            f"recompute false")


def q7(table, item):
    """Agreements in force rise; single-region ones predominate throughout."""
    decades = cg.labels(table)
    assert decades == ["1960s", "1980s", "2000s"], \
        f"the key speaks of each decade recorded; the rows are {decades}"
    _parts_sum_to_whole(table, IN_FORCE, [CROSS_REGION, ONE_REGION], "agreements in force")
    total = cg.col(table, IN_FORCE)
    cross = cg.col(table, CROSS_REGION)
    single = cg.col(table, ONE_REGION)
    assert all(b > a for a, b in zip(total, total[1:])), \
        f"the key says the number in force rose in each decade; it runs {total}"
    for d, s, c in zip(decades, single, cross):
        assert s > c, (
            f"the key needs single-region agreements to outnumber the rest in {d}; the row "
            f"reads {s} single-region against {c} spanning more than one")
    # every distractor false on the same numbers
    assert total[-1] > total[0], \
        "'the number in force fell in each decade after the first' must be false"
    assert not all(c > s for c, s in zip(cross, single)), \
        "'cross-region agreements outnumbered single-region ones in every decade' must be false"
    assert cross[0] > 0, \
        "'no 1960s agreement joined states of more than one region' must be false"
    assert len(set(total)) > 1, \
        "'the three decades recorded the same number in force' must be false"
    return (f"agreements in force run {total}, rising throughout, with single-region "
            f"{single} outnumbering cross-region {cross} in every decade; the parts sum to "
            f"the stated wholes and all four distractors recompute false")


def q13(table, item):
    """Nowhere a majority, and the three shares markedly different."""
    labs = cg.labels(table)
    total = dict(zip(labs, cg.col(table, WORKERS)))
    ict = dict(zip(labs, cg.col(table, ICT)))
    _parts_sum_to_whole(table, WORKERS, [ICT, OTHER_SECTORS], "workers recorded")
    shares = {lab: ict[lab] / total[lab] for lab in labs}
    for lab in labs:
        assert shares[lab] < 0.5, (
            f"the key needs no economy to reach a majority in these services; {lab} reads "
            f"{ict[lab]} of {total[lab]}, a share of {shares[lab]:.3f}")
    assert len(set(round(v, 6) for v in shares.values())) == len(labs), (
        f"the key says the share differs between the three; the shares are "
        f"{ {k: round(v, 3) for k, v in shares.items()} }")
    # every distractor false on the same numbers
    assert not all(v > 0.5 for v in shares.values()), \
        "'these services employ a majority in every economy' must be false"
    assert ict["Economy three"] > 0, \
        "'no worker in economy three is recorded in these services' must be false"
    assert total["Economy three"] <= total["Economy two"], \
        "'economy three records more workers than economy two' must be false"
    assert len(set(round(v, 6) for v in shares.values())) > 1, \
        "'the share is the same in all three economies' must be false"
    return (f"the information and communications share runs "
            f"{ {k: round(v, 3) for k, v in shares.items()} } of totals {total}, below a "
            f"majority everywhere and different in each; the parts sum to the stated "
            f"wholes and all four distractors recompute false")


TABLE_CHECKS = {3: q3, 7: q7, 13: q13}

CLAIMS = [
 ("encouraging free-market economic policies and promoting economic liberalization in the late twentieth century",
  "KC-6.3.I.D states that in a trend accelerated by the end of the Cold War, many governments encouraged free-market economic policies and promoted economic liberalization in the late twentieth century. Selling state firms, ending price controls and cutting tariffs are that encouragement in a budget document, and each distractor describes the state doing more rather than less. The key says nothing about whether the policies worked."),

 ("multinational corporations that reflected the spread of principles and practices associated with free-market economics",
  "KC-6.3.II.B states that changing economic institutions, multinational corporations, and regional trade agreements reflected the spread of principles and practices associated with free-market economics throughout the world. A firm designing in one country, assembling in a second and selling in forty is that corporation as the framework describes it."),

 ("share produced in Asia and Latin America rose with it",
  "KC-6.3.I.E states that in the late twentieth century industrial production and manufacturing were increasingly situated in Asia and Latin America, and a rising share of a rising total is what increasingly situated means when it is counted. The index is hypothetical and is recomputed from the table alone in q3 above."),

 ("growth of knowledge economies in some regions",
  "KC-6.3.I.E states that revolutions in information and communications technology led to the growth of knowledge economies IN SOME REGIONS. The qualifier is the framework's own and a distractor removes it, so the anchor carries it; the same sentence pairs that growth with manufacturing moving to Asia and Latin America rather than with its disappearance."),

 ("selects the aspects of the agreement that matter to the audience in front of it",
  "Skill 2.C asks for the significance of a source's point of view, purpose, historical situation and audience. KC-6.3.II.B places regional trade agreements among the developments reflecting the spread of free-market principles, and a minister arguing for one before two audiences is selecting from a single case rather than holding two views, which is what the pair lets a historian see."),

 ("accelerated a trend that was already under way",
  "KC-6.3.I.D states that IN A TREND ACCELERATED BY the end of the Cold War, many governments encouraged free-market economic policies. Accelerated presupposes something already moving, so the framework describes a change of pace rather than a beginning, and a distractor has the trend starting in 1989; the anchor therefore carries both the acceleration and the prior existence."),

 ("agreements joining states of a single region outnumbered the rest in every decade",
  "KC-6.3.II.B states that regional trade agreements reflected the spread of principles and practices associated with free-market economics throughout the world, and a rising count in which regional agreements predominate is that spread counted. The record is hypothetical and is recomputed from the table alone in q7 above."),

 ("manufacturing was increasingly situated in Asia and Latin America while knowledge economies grew in some regions",
  "KC-6.3.I.E puts both movements in one sentence and in that pairing: knowledge economies growing in some regions WHILE industrial production and manufacturing were increasingly situated in Asia and Latin America. A distractor exchanges the two, so the anchor carries both halves in the framework's own arrangement."),

 ("reflected that spread rather than being named as its cause",
  "KC-6.3.II.B states that changing economic institutions, multinational corporations, and regional trade agreements REFLECTED the spread of principles and practices associated with free-market economics. Reflected is the framework's own verb and it is weaker than caused, so the anchor carries the verb together with what it excludes."),

 ("United States under Ronald Reagan, Britain under Margaret Thatcher, China under Deng Xiaoping",
  "The CED prints these four beside KC-6.3.I.D as illustrative examples of governments' increased encouragement of free-market policies. The second option is printed beside KC-6.3.I.C in Topic 8.6 for governments guiding economic life; the rest are this page's own separate lists. The item asks which list the course prints and says nothing about whether the policies succeeded, which is a live political argument the framework does not settle."),

 ("acceleration of the trend toward economic liberalization that followed the end of the Cold War",
  "KC-6.3.I.D states that in a trend accelerated by the end of the Cold War, many governments encouraged free-market economic policies and promoted economic liberalization in the late twentieth century. An editorial dating its argument to the political changes of the preceding two years is that acceleration argued from inside the moment."),

 ("industrial production and manufacturing were increasingly situated in Asia and Latin America",
  "KC-6.3.I.E states exactly that of the late twentieth century, and the CED prints Vietnam and Bangladesh, and Mexico and Honduras, as its illustrative examples. Factories opening in those regions to supply buyers elsewhere is that relocation described by the firm making it, and a distractor reverses the two ends of it."),

 ("In no economy surveyed do information and communications services employ a majority, and the share differs between the three",
  "KC-6.3.I.E states that revolutions in information and communications technology led to the growth of knowledge economies IN SOME REGIONS, which is a claim about unevenness rather than universality. A survey in which the share differs markedly and nowhere reaches a majority is that word made countable, and it is recomputed from the table alone in q13 above."),

 ("Manufacturing continued to be central to the world economy, while the places where it was carried on changed",
  "KC-6.3.I.E states that industrial production and manufacturing were increasingly situated in Asia and Latin America, which is a change of location within a continuing activity. Unit 9 Learning Objective D asks for the continuities AND changes in the global economy, and the anchor carries one of each because a distractor exchanges them."),

 ("speak from different positions within the same economy, and each shows what that position made visible",
  "Skill 2.C asks for the SIGNIFICANCE of a source's point of view and situation, which means asking what a position lets a source see rather than ranking positions for reliability. KC-6.3.II.B places regional trade agreements among the developments reflecting the spread of free-market principles, and both pamphlets are evidence about how that spread was experienced from different places inside it."),

 ("Knowledge economies grew at the same rate in every region of the world",
  "KC-6.3.I.E states that knowledge economies grew IN SOME REGIONS, so uniform growth everywhere is the claim the framework does not support. The item asks which statement is NOT supported, so the anchor is pinned to the false one deliberately; the other four restate KC-6.3.I.D, KC-6.3.I.E and KC-6.3.II.B."),

 ("World Trade Organization, NAFTA, and ASEAN",
  "The CED prints these three beside KC-6.3.II.B as illustrative examples of economic institutions and regional trade agreements. The other lists are this page's separate examples of multinational corporations, of knowledge economies and of Asian and Latin American production economies, or belong to Topic 9.5."),

 ("trend accelerated by the end of the Cold War",
  "KC-6.3.I.D states that in a trend ACCELERATED BY the end of the Cold War, many governments encouraged free-market economic policies and promoted economic liberalization. Acceleration is a change of pace in something already moving, which is exactly the historian's reading, and the reasoning process the CED prints beside this topic is continuity and change."),

 ("growth of knowledge economies that followed revolutions in information and communications technology",
  "KC-6.3.I.E states that in the late twentieth century, revolutions in information and communications technology led to the growth of knowledge economies in some regions. Advice to move from heavy industry into software and research is that growth recommended as policy, and it is the other half of the sentence from the relocation of manufacturing."),

 ("written to attract buyers and the minute to record a decision, so each supports different kinds of claim",
  "Skill 2.C asks for the significance of a source's purpose and audience, including how these might limit its uses. KC-6.3.I.D places privatization among the free-market policies many governments encouraged, and a prospectus and an internal minute about the same sale are produced for different ends, so each can establish something the other cannot."),

 ("In Asia and Latin America",
  "KC-6.3.I.E states that in the late twentieth century industrial production and manufacturing were increasingly situated in Asia and Latin America. The framework names those two regions in that sentence, and the CED prints Vietnam and Bangladesh, and Mexico and Honduras, as its illustrative examples of them."),

 ("programme's author reporting on its own work, which bears on what the account can establish",
  "Skill 2.C asks for the significance of a source's point of view and purpose, including how these might limit its uses. KC-6.3.I.D places such programmes among the free-market policies many governments encouraged, and a government reporting on its own programme in its first year has both an interest and a very short run of evidence."),

 ("Changing economic institutions, multinational corporations, and regional trade agreements",
  "KC-6.3.II.B names exactly those three as reflecting the spread of principles and practices associated with free-market economics throughout the world. Each distractor lists developments the framework states in other sentences of this course, which is the cross-sentence error a list item is built to catch."),

 ("reflected the spread of free-market principles rather than naming them as its cause",
  "KC-6.3.II.B uses the verb REFLECTED, which is weaker than caused. The correction has to restore the framework's own relation rather than substituting a different one, so the anchor carries the verb together with the relation it displaces."),

 ("first as a strong state role after independence and the second as the later encouragement of free-market policies",
  "KC-6.3.I.C in Topic 8.6 records that governments of newly independent states after World War II often took a strong role in guiding economic life, and KC-6.3.I.D here records that in a trend accelerated by the end of the Cold War many governments encouraged free-market policies in the late twentieth century. Unit 9 Learning Objective D asks for continuities and changes, and the pair is the framework's own sequence."),

 ("change in where manufacturing was carried on alongside a continuity in where its products were sold",
  "KC-6.3.I.E states that industrial production and manufacturing were increasingly situated in Asia and Latin America in the late twentieth century, which is a change in the origin of goods rather than in their destination. The reasoning process the CED prints beside this topic is continuity and change, and a distractor exchanges the two, so the anchor carries one of each in the right order."),

 ("share of the country's workers and output in information and communications activities",
  "KC-6.3.I.E states that revolutions in information and communications technology led to the growth of knowledge economies in some regions, so the share of workers and output in those activities is the direct measure. The other records bear on developments the framework treats in other topics."),

 ("manufacturing shifted toward Asia and Latin America, and that free-market principles and practices spread throughout the world",
  "KC-6.3.I.E states that industrial production and manufacturing were increasingly situated in Asia and Latin America, and KC-6.3.II.B that changing economic institutions, multinational corporations, and regional trade agreements reflected the spread of free-market principles and practices throughout the world. Both are movements rather than cessations, which is the reading the historian proposes."),

 ("direction of economic policy in many governments changed and manufacturing moved, while production, trade and the search for markets carried on",
  "KC-6.3.I.D supplies the change in the direction of policy, KC-6.3.I.E the movement of manufacturing and the growth of knowledge economies in some regions, and KC-6.3.II.B the spread of free-market principles through institutions, corporations and trade agreements, all of which presuppose production and trade continuing. Unit 9 Learning Objective D asks for continuities and changes together, so the anchor carries both sides."),

 ("knowledge economies grew in some regions while manufacturing moved toward Asia and Latin America, and institutions, firms and trade agreements reflected free-market principles spreading",
  "KC-6.3.I.D supplies the turn toward free-market policies and the acceleration by the end of the Cold War, KC-6.3.I.E the knowledge economies in some regions and the relocation of manufacturing, and KC-6.3.II.B the institutions, corporations and trade agreements reflecting the spread. The key is the conjunction of the three with every qualifier intact, and each distractor contradicts at least one."),
]

wh.run(w9_4, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
