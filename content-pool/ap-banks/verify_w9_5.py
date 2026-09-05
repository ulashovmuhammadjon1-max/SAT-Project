"""Key audit for AP WORLD HISTORY: MODERN 9.5 Calls for Reform and Responses
After 1900.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code or Learning
Objective, for a human to audit. `wh_check` refuses any claim or `why` that
cites neither.

TITLE. Taken verbatim from WORLD_HISTORY_topics.json, which the authoring brief
records as the authority for four titles in this territory that had to be
reassembled by hand from CED pages whose columns interleave. This is one of the
four. It matches the CED page read in full.

"IN MUCH OF THE WORLD" IS THE LOAD-BEARING PHRASE. KC-6.3.III.ii does not say
everywhere. In a topic about reform the temptation is to write a story of
uniform progress, and that story is not the framework's. q9, q17, q19 and q26
hold the qualifier open, q19 being the NOT-supported item built precisely on
flattening it. Unit 9 Learning Objective E does the same work at the level of
the whole topic by asking how categories were MAINTAINED AND CHALLENGED -- both
verbs -- and q5, q14, q22 and q29 turn on that pairing.

ONE DATE IN THE CED IS NOT KEYED, DELIBERATELY. The CED's second illustrative
list prints "The U.S. Civil Rights Act of 1965". The Civil Rights Act is of 1964
and the Voting Rights Act is of 1965, so the year does not match the statute the
CED's own words name. This bank does not resolve that: no item keys that date or
any date from that list, and neither illustrative-example item uses that list.
Keying a year that may be an error in the source would teach the error, and the
rule in HISTORY_BRIEF.md is that an uncertain question is cut rather than
guessed. This paragraph exists so the omission reads as a decision rather than
an oversight.

CONTESTED GROUND, AND THE CARE THIS TOPIC NEEDS MOST. This page is about race,
class, gender and religion, and about apartheid and caste. Every claim below is
limited to what the framework's three sentences state. No claim evaluates any
group, belief or religion; no claim says a reform was sufficient, insufficient,
too fast or too slow; no claim assigns a motive to any group of people; no claim
describes a social category as natural or as deserved. q21 and q30 both involve
sources speaking from inside a tradition or a movement, and both key what the
source argues, not whether it is right.

WHERE A DISTRACTOR IS THE SWAP OF THE KEY, THE ANCHOR CARRIES BOTH CLAUSES.
Six items are built on a reversal a prepared student could believe:

  q9   "much of the world" swapped for "everywhere" and for "nowhere"
  q11  challenged swapped for confirmed
  q19  the NOT-supported item, where the key is deliberately the false claim
  q22  a mixture of change and persistence swapped for one or the other alone
  q24  the two things that became more inclusive, offered singly
  q27  the framework asserting both developments, against it denying one

For each the anchor spans the whole relation, so an anchor that matched the
swapped distractor would fail the gate rather than pass it. That defect is on
record in `verify_e2_1.py`.

WHAT THIS CANNOT DO: it cannot tell whether the history is right. It gates
structure, key/anchor agreement, notation, the absence of figure language, the
presence of a citation, and the arithmetic of the three data questions.

NEGATIVE CONTROL: `python3 verify_w9_5.py --selftest`. It rotates all thirty
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
import w9_5

T_UNIVERSITY = w9_5._T_UNIVERSITY
T_LEGISLATURE = w9_5._T_LEGISLATURE
T_PROTESTS = w9_5._T_PROTESTS

ENTRANTS = "Entrants recorded"
WOMEN_ENT = "Of those, women"
MEN_ENT = "Of those, men"
SEATS = "Seats in the legislature"
WOMEN_SEATS = "Of those, held by women"
MEN_SEATS = "Of those, held by men"
PROTESTS = "Protests recorded"
ENVIRONMENTAL = "Of those, whose stated grievance was chiefly environmental"
ECONOMIC = "Of those, whose stated grievance was chiefly economic"


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
    """Entrants rise and the women's SHARE rises with them."""
    periods = cg.labels(table)
    assert periods == ["1950", "1970", "1990"], \
        f"the key speaks of each period recorded; the rows are {periods}"
    _parts_sum_to_whole(table, ENTRANTS, [WOMEN_ENT, MEN_ENT], "university entrants")
    total = cg.col(table, ENTRANTS)
    women = cg.col(table, WOMEN_ENT)
    men = cg.col(table, MEN_ENT)
    assert all(b > a for a, b in zip(total, total[1:])), \
        f"the key says entrants rose in each period; they run {total}"
    shares = [w / t for w, t in zip(women, total)]
    assert all(b > a for a, b in zip(shares, shares[1:])), (
        f"the key says the women's portion rose AS A SHARE; the shares run "
        f"{[round(s, 3) for s in shares]}")
    # every distractor false on the same numbers
    assert total[-1] > total[0], \
        "'entrants fell in each period after the first' must be false"
    assert shares[-1] > shares[0], \
        "'the women's share fell across the record' must be false"
    assert not all(s > 0.5 for s in shares), (
        "'women were a majority of entrants in every period' must be false; the shares "
        f"are {[round(s, 3) for s in shares]}")
    assert all(b > a for a, b in zip(men, men[1:])), \
        "'the number of men entering fell in each period' must be false"
    return (f"entrants run {total} and the women's share {[round(s, 3) for s in shares]}, "
            f"both rising, against {men} men; the parts sum to the stated wholes and all "
            f"four distractors recompute false")


def q8(table, item):
    """Seats held by women rise; over a quarter by the last period."""
    periods = cg.labels(table)
    assert periods == ["1950", "1975", "2000"], \
        f"the key speaks of each point recorded; the rows are {periods}"
    _parts_sum_to_whole(table, SEATS, [WOMEN_SEATS, MEN_SEATS], "seats in the legislature")
    total = cg.col(table, SEATS)
    women = cg.col(table, WOMEN_SEATS)
    assert all(b > a for a, b in zip(women, women[1:])), \
        f"the key says the seats held by women rose at every point; they run {women}"
    shares = [w / t for w, t in zip(women, total)]
    assert shares[-1] > 0.25, (
        f"the key says more than a quarter of the seats by the last period; the share is "
        f"{shares[-1]:.3f}")
    # every distractor false on the same numbers
    assert women[0] > 0, \
        "'women held no seats in the earliest period' must be false"
    assert shares[-1] > shares[0], \
        "'the share of seats held by women fell across the record' must be false"
    assert shares[-1] < 0.5, \
        "'women held a majority of the seats in the last period' must be false"
    assert len(set(total)) > 1, \
        "'the legislature had the same number of seats in every period' must be false"
    return (f"seats held by women run {women} of {total}, a share of "
            f"{[round(s, 3) for s in shares]} rising past a quarter but not to a majority; "
            f"the parts sum to the stated wholes and all four distractors recompute false")


def q12(table, item):
    """Protests rise, and both kinds of grievance appear in every decade."""
    decades = cg.labels(table)
    assert decades == ["1970s", "1980s", "1990s"], \
        f"the key speaks of each decade recorded; the rows are {decades}"
    _parts_sum_to_whole(table, PROTESTS, [ENVIRONMENTAL, ECONOMIC], "protests recorded")
    total = cg.col(table, PROTESTS)
    env = cg.col(table, ENVIRONMENTAL)
    eco = cg.col(table, ECONOMIC)
    assert all(b > a for a, b in zip(total, total[1:])), \
        f"the key says the number of protests rose in each decade; it runs {total}"
    for d, e, c in zip(decades, env, eco):
        assert e > 0 and c > 0, (
            f"the key needs grievances of both kinds in {d}; the row reads {e} "
            f"environmental and {c} economic")
    # every distractor false on the same numbers
    assert any(e > 0 for e in env), \
        "'only chiefly economic grievances are recorded' must be false"
    assert any(c > 0 for c in eco), \
        "'only chiefly environmental grievances are recorded' must be false"
    assert total[-1] > total[0], \
        "'the number of protests fell in each decade after the first' must be false"
    assert not all(e > c for e, c in zip(env, eco)), \
        "'environmental grievances outnumbered economic ones in every decade' must be false"
    return (f"protests run {total}, rising throughout, with {env} chiefly environmental and "
            f"{eco} chiefly economic, both present in every decade; the parts sum to the "
            f"stated wholes and all four distractors recompute false")


TABLE_CHECKS = {3: q3, 8: q8, 12: q12}

CLAIMS = [
 ("rights-based discourses that challenged old assumptions about race, class, gender, and religion",
  "KC-6.3.III.i states that rights-based discourses challenged old assumptions about race, class, gender, and religion, and the CED prints the U.N. Universal Declaration of Human Rights among its illustrative examples. A document asserting entitlements without distinction, taken up against arguments from custom, is that discourse in its characteristic use."),

 ("In terms of race, class, gender, and religion",
  "KC-6.3.III.ii states that in much of the world, access to education as well as participation in new political and professional roles became more inclusive IN TERMS OF RACE, CLASS, GENDER, AND RELIGION. Those four are the framework's own list and the same four KC-6.3.III.i names as the subjects of the old assumptions."),

 ("share of them who were women rose with it",
  "KC-6.3.III.ii states that in much of the world access to education became more inclusive in terms of race, class, gender, and religion, and the CED prints the increasing numbers of women in higher education among its illustrative examples. The record is hypothetical and is recomputed from the table alone in q3 above."),

 ("inequality of its environmental and economic consequences",
  "KC-6.3.II.C states that movements throughout the world protested the INEQUALITY OF THE ENVIRONMENTAL AND ECONOMIC CONSEQUENCES of global integration. The framework names the inequality of two specific kinds of consequence as the object of the protest, and the anchor carries both kinds because the sentence does."),

 ("challenged old assumptions, while access became more inclusive in much of the world rather than in all of it",
  "KC-6.3.III.i states that rights-based discourses challenged old assumptions and KC-6.3.III.ii that access became more inclusive IN MUCH OF THE WORLD. Unit 9 Learning Objective E asks how social categories, roles and practices were both MAINTAINED and CHALLENGED, and a challenge reaching much of the world rather than all of it is both at once, so the anchor carries both halves."),

 ("access to education becoming more inclusive in terms of race, class, gender, and religion",
  "KC-6.3.III.ii states that in much of the world, access to education as well as participation in new political and professional roles became more inclusive in terms of race, class, gender, and religion. A rule of eligibility replaced by open examination is that widening in one institution, and skill 4.B asks a student to situate the specific change inside the broader process."),

 ("Universal Declaration of Human Rights, global feminism movements, the Negritude movement",
  "The CED prints these four beside KC-6.3.III.i as illustrative examples of challenges to assumptions about race, class, gender, and religion. The second option is this page's separate list of environmental and economic movements, and the rest are printed beside statements in other topics. Neither illustrative-example item in this module uses the list containing the CED's disputed Civil Rights Act date."),

 ("by the last period they held more than a quarter of the seats",
  "KC-6.3.III.ii states that in much of the world participation in new political roles became more inclusive in terms of race, class, gender, and religion, and the CED prints the granting of the right to vote and to hold public office to women among its illustrative examples. The record is hypothetical and is recomputed from the table alone in q8 above."),

 ("in much of the world, which is not the same as everywhere",
  "KC-6.3.III.ii states that IN MUCH OF THE WORLD access to education and participation in new political and professional roles became more inclusive. Much of the world is the framework's own qualifier and it rules out the universal claim as well as the opposite absolute, so the anchor carries the qualifier together with what it excludes."),

 ("protested the inequality of the environmental and economic consequences of global integration",
  "KC-6.3.II.C is the sentence. A leaflet contrasting distant beneficiaries with local costs to a fishery joins the environmental and the economic grievance in the framework's own pairing."),

 ("challenged old assumptions about race, class, gender, and religion",
  "KC-6.3.III.i states that rights-based discourses CHALLENGED old assumptions about race, class, gender, and religion. Challenged is the framework's own verb and the four categories its own list, so a distractor confirming those assumptions reverses the sentence and the anchor carries the verb with its object."),

 ("grievances of both kinds are recorded in every decade",
  "KC-6.3.II.C names both the ENVIRONMENTAL and the ECONOMIC consequences as what movements protested the inequality of. A record in which both appear in every decade is that pairing counted, and the figures are hypothetical, with the key recomputed from the table alone in q12 above."),

 ("participation in new professional roles becoming more inclusive during this period",
  "KC-6.3.III.ii states that in much of the world, participation in new political and professional roles became more inclusive in terms of race, class, gender, and religion. A first admission to a professional examination followed by its becoming unremarkable is that widening across one working life, which skill 4.B asks a student to situate in the broader process."),

 ("maintained and how they have been challenged over time",
  "Unit 9 Learning Objective E, printed on this topic's page, is to explain how social categories, roles, and practices have been MAINTAINED AND CHALLENGED over time. Both verbs are in the objective, so a bank telling only a story of change would answer half of it, and the anchor carries both."),

 ("rights-based discourses the framework names as challenging old assumptions",
  "KC-6.3.III.i states that rights-based discourses challenged old assumptions about race, class, gender, and religion, and an argument from what is owed as of right is that kind of discourse by its own premise. The second pamphlet argues from output rather than entitlement, which is what distinguishes the two."),

 ("Greenpeace, the Green Belt Movement in Kenya, and the World Fair Trade Organization",
  "The CED prints Greenpeace and Professor Wangari Maathai's Green Belt Movement in Kenya as its environmental movements and the World Fair Trade Organization as its economic movement, beside KC-6.3.II.C. The other options are this page's separate list of challenges to old assumptions, or belong to other topics."),

 ("became more inclusive in much of the world, which allows for places where it did not",
  "KC-6.3.III.ii states that IN MUCH OF THE WORLD access to education and participation in new political and professional roles became more inclusive. The qualifier is what makes room for both of the study's findings at once, and a framework asserting a universal change could not accommodate the second, so the anchor carries the qualifier and its consequence."),

 ("movements protested the inequality of the environmental and economic consequences of global integration",
  "KC-6.3.II.C is the sentence. Costs falling locally while earnings leave the region is that inequality stated in both of the framework's registers at once, the environmental and the economic."),

 ("equally inclusive in every part of the world",
  "KC-6.3.III.ii says IN MUCH OF THE WORLD, so equal inclusiveness everywhere is the claim the framework does not support. The item asks which statement is NOT supported, so the anchor is pinned to the false one deliberately; the other four restate KC-6.3.III.i, KC-6.3.III.ii and KC-6.3.II.C."),

 ("who was eligible to vote and to hold office, and of who actually did so",
  "KC-6.3.III.ii states that in much of the world participation in new political roles became more inclusive in terms of race, class, gender, and religion, so eligibility and actual participation over time are the direct measures. The other records bear on developments the framework treats in other topics."),

 ("challenges to old assumptions about race that this course places among rights-based discourses",
  "KC-6.3.III.i states that rights-based discourses challenged old assumptions about race, class, gender, and religion, and the CED prints the Negritude movement among its illustrative examples. An argument that a people's art and thought be valued on their own terms is a challenge to an assumption about race in the framework's sense, and the key describes the argument without evaluating it."),

 ("objective for this topic asks about categories both maintained and challenged",
  "Unit 9 Learning Objective E asks a student to explain how social categories, roles, and practices have been MAINTAINED AND CHALLENGED over time, which is exactly the mixture the historian describes, and KC-6.3.III.ii's qualifier supplies the same mixture inside one sentence. Distractors offer uniform change and uniform stasis, so the anchor carries both verbs."),

 ("movements protesting the inequality of the economic consequences of global integration",
  "KC-6.3.II.C states that movements throughout the world protested the inequality of the environmental and economic consequences of global integration, and the CED prints the World Fair Trade Organization among its illustrative examples of economic movements. A campaign to change what growers receive is that protest expressed as a proposal."),

 ("Access to education, and participation in new political and professional roles",
  "KC-6.3.III.ii names two things together: access to education AS WELL AS participation in new political and professional roles. A key confined to one would report half the sentence, and two distractors offer exactly that half, so the anchor carries both."),

 ("rights-based discourses and to the widening of access in much of the world",
  "KC-6.3.III.i supplies the rights-based discourses that challenged old assumptions and KC-6.3.III.ii the widening of access in much of the world, which are the broader processes a 1980 admission campaign sits inside. Skill 4.B, the suggested skill for this topic, asks a student to situate a specific development within a broader context."),

 ("first as a challenge to old assumptions and the second as a widening of access in much of the world",
  "KC-6.3.III.i states that rights-based discourses challenged old assumptions about race, class, gender, and religion, and KC-6.3.III.ii that in much of the world access to education and participation in new political and professional roles became more inclusive in those same four terms. The framework asserts both, and distractors have it denying one or the other, so the anchor carries both with their own descriptions."),

 ("inequality of the environmental consequences of global integration",
  "KC-6.3.II.C states that movements throughout the world protested the INEQUALITY of the environmental and economic consequences of global integration, and the CED prints the Green Belt Movement in Kenya among its illustrative examples of environmental movements. Residents arguing that a loss fell hardest on the poorest is that inequality as the ground of the protest."),

 ("assumptions about all four were challenged, and access widened in terms of all four in much of the world",
  "KC-6.3.III.i names race, class, gender, and religion as the subjects of the old assumptions rights-based discourses challenged, and KC-6.3.III.ii names the same four as the terms in which access became more inclusive in much of the world. The framework uses one list twice, which is what the key reports, and it does not say the categories disappeared."),

 ("challenged old assumptions about class and religion",
  "KC-6.3.III.i states that rights-based discourses challenged old assumptions about race, class, gender, and religion, and the CED prints liberation theology in Latin America among its illustrative examples. A letter treating the condition of the poorest as an obligation rather than a given challenges an assumption about class from within a religious tradition, which is two of the framework's four categories at once. The key describes the argument and does not evaluate the faith it is made in."),

 ("schooling and public and professional office opened to more people across much of the world, and movements objected that the gains and costs of global integration fell unevenly",
  "KC-6.3.III.i supplies the rights-based challenge to old assumptions about the four categories, KC-6.3.III.ii the widening of access to education and to political and professional roles in much of the world, and KC-6.3.II.C the movements protesting the inequality of the environmental and economic consequences of global integration. The key is the conjunction of the three with the qualifier intact, and each distractor contradicts at least one."),
]

wh.run(w9_5, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
