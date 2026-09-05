"""Key audit for AP WORLD HISTORY: MODERN 8.8 End of the Cold War.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code or Learning
Objective, for a human to audit. `wh_check` refuses any claim or `why` that
cites neither, because a key traceable only to an author's knowledge of the
twentieth century cannot be checked by anyone reading this bank later.

THE WHOLE TOPIC RESTS ON ONE SENTENCE. KC-6.2.IV.E: advances in U.S. military
and technological development, the Soviet Union's costly and ultimately failed
invasion of Afghanistan, and public discontent and economic weakness in
communist countries led to the end of the Cold War and the collapse of the
Soviet Union. Three causes, two outcomes. Every claim below is an appeal to some
part of that sentence and to nothing else; the CED prints no illustrative
examples on this page, so none is used and none is invented.

CONTESTED GROUND, AND WHAT NO CLAIM BELOW ASSERTS. Why the Cold War ended is a
live political argument and the tempting keys are the ones the framework does
not license:

  * no claim says any one of the three causes was decisive or outweighed the
    others -- the sentence conjoins them and ranks nothing (q6, q12, q24, q29);
  * no claim names a head of government or credits a person -- the CED names no
    individual on this page;
  * no claim says either side won, that either system was proved superior, or
    that the outcome was inevitable (q16, q21, q27 mark those as claims the
    framework does not make);
  * no claim asserts a year -- the CED gives none on this page.

WHERE A DISTRACTOR IS THE SWAP OF THE KEY, THE ANCHOR CARRIES BOTH CLAUSES.
Six items are built on a reversal a prepared student could believe:

  q3   costly and failed swapped for inexpensive and successful
  q9   the NOT-named item, where the key is deliberately the cause the CED omits
  q14  cause and effect reversed, the end of the Cold War producing its causes
  q20  an outcome offered where the item asks for the cause side
  q27  the second NOT-supported item, on a war between the superpowers
  q30  the summary, where a distractor supplies a decisive victor

For each of those the anchor spans the whole relation and not just one noun, so
an anchor that matched the swapped distractor would fail the gate rather than
pass it. That defect is on record in `verify_e2_1.py`.

WHAT THIS CANNOT DO: it cannot tell whether the history is right. It gates
structure, key/anchor agreement, notation, the absence of figure language, the
presence of a citation, and the arithmetic of the three data questions. The
history is gated by the claims below and by the rule in HISTORY_BRIEF.md that a
key must trace to a sentence in the CED.

NEGATIVE CONTROL: `python3 verify_w8_8.py --selftest`. It rotates all thirty
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
import w8_8

T_BUDGET = w8_8._T_BUDGET
T_INTERVENTION = w8_8._T_INTERVENTION
T_SHORTAGES = w8_8._T_SHORTAGES

BUDGET = "Military budget (first decade = 100)"
RESEARCH = "Of that, spent on research and new technologies"
FORCES = "Of that, spent on existing forces"
COST = "Annual cost (first year = 100)"
FIELD = "Of that, maintaining forces in the field"
ALLIED = "Of that, supplying allied local forces"
HOUSEHOLDS = "Households surveyed"
SHORTAGE = "Of those, reporting shortages of basic goods in the past year"
NO_SHORTAGE = "Of those, reporting no such shortage"


def _parts_sum_to_whole(table, whole, parts, what):
    """Every row's parts must total its whole.

    This is what makes the negative control mean anything on these tables. The
    corruption in `es_check` only ever makes a number LARGER, so a check of the
    form "this count is above zero" is monotone and can never fail: it reads the
    table without being able to object to anything in it. Sibling module 8.5
    shipped a first draft whose table check caught 1 of 12 corrupted cells for
    exactly that reason. Each row here states a whole and the two parts it was
    divided into, and every stem says so, making the sum a property of the data
    as the question describes it rather than a contrivance.
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
    """A rising budget whose research SHARE also rises."""
    decades = cg.labels(table)
    assert decades == ["1960s", "1970s", "1980s"], \
        f"the key speaks of each decade recorded; the rows are {decades}"
    _parts_sum_to_whole(table, BUDGET, [RESEARCH, FORCES], "military budget")
    total = cg.col(table, BUDGET)
    rnd = cg.col(table, RESEARCH)
    forces = cg.col(table, FORCES)
    assert all(b > a for a, b in zip(total, total[1:])), \
        f"the key says the budget rose in each decade; it runs {total}"
    shares = [r / t for r, t in zip(rnd, total)]
    assert all(b > a for a, b in zip(shares, shares[1:])), (
        f"the key says the research portion rose AS A SHARE of the budget; the shares run "
        f"{[round(s, 3) for s in shares]}")
    # every distractor false on the same numbers
    assert total[-1] > total[0], \
        "'the budget fell in each decade after the first' must be false"
    assert shares[-1] > shares[0], \
        "'the research share fell across the record' must be false"
    assert all(b > a for a, b in zip(forces, forces[1:])), \
        "'spending on existing forces fell after the first decade' must be false"
    assert all(r < f for r, f in zip(rnd, forces)), \
        "'research spending exceeded spending on existing forces in every decade' must be false"
    return (f"the budget runs {total}, rising throughout, with the research share running "
            f"{[round(s, 3) for s in shares]} and also rising, the parts summing to the "
            f"stated wholes; all four distractors recompute false")


def q8(table, item):
    """A cost rising every year, with the field component rising alongside it."""
    years = cg.labels(table)
    assert years == ["Year one", "Year two", "Year three", "Year four"], \
        f"the key speaks of every year recorded; the rows are {years}"
    _parts_sum_to_whole(table, COST, [FIELD, ALLIED], "annual cost")
    total = cg.col(table, COST)
    field = cg.col(table, FIELD)
    allied = cg.col(table, ALLIED)
    assert all(b > a for a, b in zip(total, total[1:])), \
        f"the key says the annual cost rose in every year; it runs {total}"
    assert all(b > a for a, b in zip(field, field[1:])), \
        f"the key says the field component rose alongside it; it runs {field}"
    # every distractor false on the same numbers
    assert all(b > a for a, b in zip(total, total[1:])), \
        "'the annual cost fell in at least one year' must be false"
    assert field[-1] > field[0], \
        "'the cost of maintaining forces in the field fell over the record' must be false"
    assert all(a < f for a, f in zip(allied, field)), \
        "'supplying allied local forces exceeded maintaining forces in the field' must be false"
    assert total[-1] > total[0], \
        "'the last year's cost stood below its first-year level' must be false"
    return (f"the annual cost runs {total} and the field component {field}, both rising at "
            f"every step against {allied} for allied forces, the parts summing to the "
            f"stated wholes; all four distractors recompute false")


def q13(table, item):
    """A majority reporting shortages in every country surveyed."""
    labs = cg.labels(table)
    total = dict(zip(labs, cg.col(table, HOUSEHOLDS)))
    short = dict(zip(labs, cg.col(table, SHORTAGE)))
    none = dict(zip(labs, cg.col(table, NO_SHORTAGE)))
    _parts_sum_to_whole(table, HOUSEHOLDS, [SHORTAGE, NO_SHORTAGE], "households surveyed")
    for lab in labs:
        assert short[lab] > 0.5 * total[lab], (
            f"the key needs a majority reporting shortages in {lab}; the row reads "
            f"{short[lab]} of {total[lab]}")
    # every distractor false on the same numbers
    assert not all(short[l] < 0.5 * total[l] for l in labs), \
        "'fewer than half reported shortages in every country' must be false"
    assert short["Country three"] > 0, \
        "'no household surveyed in country three reported a shortage' must be false"
    assert total["Country three"] <= total["Country two"], \
        "'country three surveyed more households than country two' must be false"
    assert len(set(total.values())) > 1, \
        "'the three countries surveyed the same number of households' must be false"
    return (f"households reporting shortages {short} against totals {total}, a majority "
            f"everywhere, with {none} reporting none and the parts summing to the stated "
            f"wholes; all four distractors recompute false")


TABLE_CHECKS = {4: q4, 8: q8, 13: q13}

CLAIMS = [
 ("Advances in United States military and technological development, the Soviet Union's costly and failed invasion of Afghanistan",
  "KC-6.2.IV.E states that advances in U.S. military and technological development, the Soviet Union's costly and ultimately failed invasion of Afghanistan, and public discontent and economic weakness in communist countries led to the end of the Cold War and the collapse of the Soviet Union. Those three are the framework's causes and it names no others; the anchor spans two of them so no single-cause distractor can match."),

 ("Advances in United States military and technological development",
  "KC-6.2.IV.E names advances in U.S. military and technological development first among the three causes it gives. A sustained programme of advanced weapons research that the other superpower struggles to match is that advance in budgetary terms, and it is distinct from the two other causes in the same sentence."),

 ("That it was costly, and that it ultimately failed",
  "KC-6.2.IV.E describes the Soviet Union's COSTLY and ULTIMATELY FAILED invasion of Afghanistan. Both adjectives are the framework's own and a distractor exchanges them for their opposites, so the anchor carries both."),

 ("portion going to research and new technologies rose as a share of it",
  "KC-6.2.IV.E names advances in U.S. military and technological development among the causes of the end of the Cold War, and a rising research share of a rising budget is one form such an advance takes. The record is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in q4 above."),

 ("Public discontent and economic weakness in communist countries",
  "KC-6.2.IV.E names public discontent and economic weakness in communist countries among the three causes. A complaint of unobtainable goods joined to a loss of confidence in official promises is both halves of that clause in one document."),

 ("names three causes acting together and does not rank one above the others",
  "KC-6.2.IV.E conjoins its three developments in a single list leading to one pair of outcomes and assigns no priority among them. This is the framework's most easily distorted feature and the correction has to preserve both the number of causes and the absence of a ranking, so the anchor carries both."),

 ("The end of the Cold War and the collapse of the Soviet Union",
  "KC-6.2.IV.E states that the three causes it names led to the end of the Cold War and the collapse of the Soviet Union. Those are the sentence's two outcomes; the dissolution of empires, the founding of the United Nations and the beginning of the Cold War belong to other statements in this course."),

 ("cost of maintaining forces in the field rose alongside it",
  "KC-6.2.IV.E names the Soviet Union's COSTLY and ultimately failed invasion of Afghanistan among the causes of the end of the Cold War, and a cost rising year on year is what makes an intervention costly in that sense. The record is hypothetical and both halves of the keyed claim are recomputed from the table alone in q8 above."),

 ("A direct war fought between the two superpowers on each other's territory",
  "KC-6.2.IV.E names three causes and a direct war between the superpowers is not among them; the framework nowhere states that the two fought each other directly. The item asks which cause the course does NOT name, so the anchor is pinned to the absent one deliberately, and the other four are the causes of that sentence."),

 ("the end of the Cold War and the collapse of the Soviet Union",
  "KC-6.2.IV.E names economic weakness in communist countries among the causes that led to the end of the Cold War and the collapse of the Soviet Union. The framework places that weakness at the end of the confrontation rather than at its beginning, so the direction of the causal relation is what the key states."),

 ("consistent with the framework, which names the invasion as costly and ultimately failed",
  "KC-6.2.IV.E describes the Soviet Union's costly and ultimately failed invasion of Afghanistan, which is the pairing of expense and outcome the historian identifies. The framework does not make it the sole cause, so a distractor calling it consistent BECAUSE the invasion is the sole cause fails; the anchor therefore carries the verdict together with the reason."),

 ("lists them together as jointly leading to the same outcome, without ordering them by importance",
  "KC-6.2.IV.E joins its three developments in one list leading to one pair of outcomes. It neither ranks them, nor derives one from another, nor reverses cause and effect, so the anchor carries both the conjunction and the absence of an ordering."),

 ("more than half of the households reported shortages of basic goods",
  "KC-6.2.IV.E names public discontent and economic weakness in communist countries among the causes of the end of the Cold War, and widespread shortages of basic goods are one measurable form of that weakness. The survey is hypothetical and is recomputed from the table alone in q13 above."),

 ("three developments named came first and the end of the Cold War followed from them",
  "KC-6.2.IV.E states that the three developments LED TO the end of the Cold War and the collapse of the Soviet Union, fixing them as prior and the outcomes as their result. Every distractor reverses that order or denies the relation, so the anchor carries the order as well as the terms."),

 ("public discontent inside a communist country in the years before the Cold War ended",
  "KC-6.2.IV.E names public discontent in communist countries among the causes of the end of the Cold War and the collapse of the Soviet Union. Workers' letters of complaint printed inside such a country are that discontent recorded from within and bear on none of the other causes the sentence names."),

 ("proves one economic system to have been superior to the other",
  "KC-6.2.IV.E names three causes and two outcomes and makes no judgement about the merits of either economic system, so a verdict on systemic superiority is a claim the framework does not supply. The item asks which explanation goes beyond the framework, so the anchor is pinned to that unlicensed claim deliberately; the other four restate parts of the sentence."),

 ("three contributing developments and then the two outcomes they led to",
  "KC-6.2.IV.E has exactly that shape: three developments conjoined, leading to the end of the Cold War and the collapse of the Soviet Union. Skill 1.B asks a student to explain a historical development or process, which is what reproducing the framework's own causal structure requires."),

 ("names causes of both kinds, so neither student has the whole of the framework's account",
  "KC-6.2.IV.E names public discontent and economic weakness in communist countries, which are internal, alongside advances in U.S. military and technological development and a failed invasion of Afghanistan, which reach the communist states from outside their own societies. The sentence supplies both kinds and ranks neither, so the anchor carries the conjunction and the refusal to rank."),

 ("costly and ultimately failed invasion among the causes of the end of the Cold War",
  "KC-6.2.IV.E names the Soviet Union's costly and ultimately failed invasion of Afghanistan among the causes of the end of the Cold War. A long war consuming resources intended for domestic use while its objectives remain unmet is that pairing of cost and failure described without naming the country."),

 ("The collapse of the Soviet Union",
  "KC-6.2.IV.E places the collapse of the Soviet Union with the end of the Cold War on the outcome side of its sentence and the other four options on the cause side. Skill 1.B asks a student to explain a process, and telling which term of a causal statement is which is the first requirement of doing so."),

 ("explains the outcome by particular developments and asserts no inevitability",
  "KC-6.2.IV.E gives three specific developments that led to the end of the Cold War and the collapse of the Soviet Union. An explanation by particular causes is not a claim of inevitability, and the framework nowhere states that the outcome was fixed in advance or that actions were irrelevant."),

 ("records of production and of shortages of consumer goods",
  "KC-6.2.IV.E names economic weakness in communist countries among the causes of the end of the Cold War, and production figures and shortages are the direct measures of such weakness. Each distractor attaches one of the framework's causes to evidence bearing on a different cause or on a different topic."),

 ("two conditions the framework names together among the causes of the end of the Cold War",
  "KC-6.2.IV.E names public discontent AND economic weakness in communist countries in one clause among the causes that led to the end of the Cold War and the collapse of the Soviet Union. The framework locates both inside the communist countries and places both before the outcome rather than after it."),

 ("identifies no such single development, naming three that led to the outcome together",
  "KC-6.2.IV.E names three developments in one list leading to the end of the Cold War and the collapse of the Soviet Union and assigns no priority among them. Answering with any one of the three would supply a ranking the framework withholds, which is what each distractor here does."),

 ("Developments inside communist countries and developments outside them both contributed",
  "KC-6.2.IV.E names public discontent and economic weakness in communist countries alongside advances in U.S. military and technological development and the Soviet Union's failed invasion of Afghanistan. The list spans both the inside and the outside of the communist states, so the framework supports the conjunction and denies neither half."),

 ("outcome reached through several developments accumulating over years, not a single moment of decision",
  "KC-6.2.IV.E names a sustained programme of military and technological advance, a long and costly invasion, and accumulated public discontent and economic weakness, all of which run over years rather than moments. Skill 1.B asks for the explanation of a development or process, which is what separates the key from an account built around a single event."),

 ("ended because one superpower defeated the other in open war",
  "KC-6.2.IV.E names three causes and neither states nor implies a war fought between the superpowers, so a defeat in open war is the claim the framework does not support. The item asks which statement is NOT supported, so the anchor is pinned to the false claim deliberately; the other four restate parts of the sentence, including its second outcome."),

 ("three pressures the framework names as leading to the end of the Cold War, seen from one side",
  "KC-6.2.IV.E names advances in U.S. military and technological development, a costly and ultimately failed invasion, and public discontent and economic weakness in communist countries as the causes of the end of the Cold War and the collapse of the Soviet Union. A memorandum listing all three as simultaneous burdens is that sentence stated as a problem of policy."),

 ("names three distinct developments and attributes the outcome to them together",
  "KC-6.2.IV.E lists three developments and says they led to the end of the Cold War and the collapse of the Soviet Union. Three distinct developments joined to one pair of outcomes is what makes the explanation multi-causal, and a distractor offers three descriptions of one development instead, so the anchor carries the distinctness and the joint attribution."),

 ("costly and failed war in Afghanistan, and discontent and economic weakness inside the communist countries together brought the confrontation to an end",
  "KC-6.2.IV.E is a single sentence naming three causes and two outcomes, and the key restates it without adding a ranking among the causes, a verdict on either system, or a person to credit. Each distractor contradicts the sentence or supplies a cause the framework does not name."),
]

wh.run(w8_8, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
