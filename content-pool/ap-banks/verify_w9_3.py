"""Key audit for AP WORLD HISTORY: MODERN 9.3 Technological Advances: Debates
About the Environment After 1900.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code or Learning
Objective, for a human to audit. `wh_check` refuses any claim or `why` that
cites neither.

THIS TOPIC CONTAINS THE MOST CONTESTED SENTENCE IN THE COURSE, and the first job
of this file is to record what the keys do NOT say. KC-6.1.II.B states that the
release of greenhouse gases and pollutants into the atmosphere CONTRIBUTED TO
DEBATES ABOUT the nature and causes of climate change. The framework asserts the
releases and it asserts the debates. It does not settle what the nature or the
causes of climate change are.

  * No claim below states what causes climate change, or that it has no cause,
    or that any particular account of it is correct or incorrect.
  * No claim assigns responsibility for emissions to any country, industry,
    government or group. The releases table names no real state; its two parts
    are "one group of states" and "all other states", and q12's item asks nothing
    about responsibility.
  * No claim endorses or rejects any environmental policy. q25 puts two opposed
    policy papers side by side and keys the existence of the debate, not a
    winner.
  * q4, q9, q17, q23, q25 and q27 mark the boundary explicitly: each keys the
    fact that the framework describes a DEBATE rather than a verdict. q27 is the
    sharpest, keying which question the framework leaves open against four it
    settles.

That is HISTORY_BRIEF.md and MISSION.md applied at their hardest point: recent
history invites both strong general knowledge and live political disagreement,
so stay on what the framework states and let contested questions stay contested.
A bank that keyed a position here would be teaching that position under cover of
an exam.

KC-6.1.II.A IS FOUR CHANGES AND ONE CONSEQUENCE: deforestation, desertification,
a decline in air quality, and increased consumption of the world's supply of
fresh water, followed by humans competing over these and other resources MORE
INTENSELY THAN EVER BEFORE. The framework says human activity CONTRIBUTED TO the
four, not that it was their sole cause, and q6, q14 and q21 keep that verb
exactly where the framework put it -- q6 against "sole cause", q14 against "no
part at all", q21 against a reading that supplies a culprit the sentence does
not name.

WHERE A DISTRACTOR IS THE SWAP OF THE KEY, THE ANCHOR CARRIES BOTH CLAUSES.
Six items are built on a reversal a prepared student could believe:

  q4   contributing to debates swapped for settling the question
  q6   "contributed to" swapped for "sole cause" and for "no part"
  q7   a rising quantity swapped for a rising share (true of one, false of the
       other, and the verifier separates them)
  q16  the NOT-supported item, where the key is deliberately the false claim
  q22  release and debate reversed in order
  q29  competition intensifying swapped for competition ending

For each the anchor spans the whole relation, so an anchor that matched the
swapped distractor would fail the gate rather than pass it. That defect is on
record in `verify_e2_1.py`.

WHAT THIS CANNOT DO: it cannot tell whether the history is right. It gates
structure, key/anchor agreement, notation, the absence of figure language, the
presence of a citation, and the arithmetic of the three data questions.

NEGATIVE CONTROL: `python3 verify_w9_3.py --selftest`. It rotates all thirty
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
import w9_3

T_FOREST = w9_3._T_FOREST
T_WATER = w9_3._T_WATER
T_RELEASES = w9_3._T_RELEASES

LAND = "Land surveyed"
FOREST = "Of that, under forest"
NOT_FOREST = "Of that, not under forest"
WITHDRAWN = "Fresh water withdrawn"
AGRI = "Of that, withdrawn for agriculture"
OTHER_USE = "Of that, withdrawn for other uses"
RELEASES = "Total recorded releases"
GROUP_ONE = "Of that, from one group of states"
ALL_OTHERS = "Of that, from all other states"


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
    """Forest falls in every period; the rest of the region rises to match."""
    periods = cg.labels(table)
    assert periods == ["1950", "1970", "1990"], \
        f"the key speaks of each period recorded; the rows are {periods}"
    _parts_sum_to_whole(table, LAND, [FOREST, NOT_FOREST], "land surveyed")
    forest = cg.col(table, FOREST)
    other = cg.col(table, NOT_FOREST)
    total = cg.col(table, LAND)
    assert all(b < a for a, b in zip(forest, forest[1:])), \
        f"the key says the forested area fell in each period; it runs {forest}"
    assert all(b > a for a, b in zip(other, other[1:])), \
        f"the key says the unforested area rose correspondingly; it runs {other}"
    # every distractor false on the same numbers
    assert forest[-1] < forest[0], \
        "'the area under forest rose in each period' must be false"
    assert other[-1] > other[0], \
        "'the area not under forest fell in each period' must be false"
    assert not all(f > 0.5 * t for f, t in zip(forest, total)), (
        "'forest covered more than half the region in every period' must be false; the "
        f"shares are {[round(f / t, 3) for f, t in zip(forest, total)]}")
    assert forest[-1] > 0, \
        "'no forest remained by the last period' must be false"
    return (f"forest runs {forest}, falling at every step, against {other} unforested, "
            f"rising at every step, within surveyed totals {total}; the parts sum to the "
            f"stated wholes and all four distractors recompute false")


def q7(table, item):
    """Withdrawals rise; agriculture is the largest part every period.

    The last distractor is true of the agricultural QUANTITY and false of the
    agricultural SHARE, which is exactly the confusion the item is built on, so
    both are computed here rather than only the one the key needs.
    """
    periods = cg.labels(table)
    assert periods == ["1950", "1970", "1990"], \
        f"the key speaks of each period recorded; the rows are {periods}"
    _parts_sum_to_whole(table, WITHDRAWN, [AGRI, OTHER_USE], "fresh water withdrawn")
    total = cg.col(table, WITHDRAWN)
    agri = cg.col(table, AGRI)
    other = cg.col(table, OTHER_USE)
    assert all(b > a for a, b in zip(total, total[1:])), \
        f"the key says total withdrawals rose in each period; they run {total}"
    for p, a, o in zip(periods, agri, other):
        assert a > o, (
            f"the key needs agriculture to be the largest part in {p}; the row reads "
            f"{a} for agriculture against {o} for other uses")
    shares = [a / t for a, t in zip(agri, total)]
    # every distractor false on the same numbers
    assert total[-1] > total[0], \
        "'total withdrawals fell in each period after the first' must be false"
    assert other[-1] > other[0], \
        "'withdrawals for other uses fell across the record' must be false"
    assert not all(s < 0.5 for s in shares), \
        "'agriculture accounted for less than half in every period' must be false"
    assert not all(b > a for a, b in zip(shares, shares[1:])), (
        "'agriculture's SHARE rose across the record' must be false, even though its "
        f"quantity rose; the shares run {[round(s, 3) for s in shares]} against "
        f"quantities {agri}")
    return (f"withdrawals run {total}, rising throughout, with agriculture {agri} the "
            f"larger part in every period but its share {[round(s, 3) for s in shares]} "
            f"falling; the parts sum to the stated wholes and all four distractors "
            f"recompute false")


def q12(table, item):
    """Releases rise while the first group's share falls.

    The item asks nothing about responsibility and this check asserts nothing
    about it: the table's two parts are "one group of states" and "all other
    states", neither of which names a real country.
    """
    periods = cg.labels(table)
    assert periods == ["1950", "1970", "1990"], \
        f"the key speaks of each period recorded; the rows are {periods}"
    _parts_sum_to_whole(table, RELEASES, [GROUP_ONE, ALL_OTHERS], "recorded releases")
    total = cg.col(table, RELEASES)
    one = cg.col(table, GROUP_ONE)
    rest = cg.col(table, ALL_OTHERS)
    assert all(b > a for a, b in zip(total, total[1:])), \
        f"the key says total recorded releases rose in each period; they run {total}"
    shares = [o / t for o, t in zip(one, total)]
    assert all(b < a for a, b in zip(shares, shares[1:])), (
        f"the key says the first group's SHARE fell; the shares run "
        f"{[round(s, 3) for s in shares]} against quantities {one}")
    # every distractor false on the same numbers
    assert total[-1] > total[0], \
        "'total recorded releases fell in each period after the first' must be false"
    assert shares[-1] < shares[0], \
        "'the first group's share rose across the record' must be false"
    assert rest[-1] > rest[0], \
        "'releases from all other states fell across the record' must be false"
    assert not all(s < 0.5 for s in shares), \
        "'the first group accounted for less than half in every period' must be false"
    return (f"recorded releases run {total}, rising throughout, with the first group's "
            f"share {[round(s, 3) for s in shares]} falling against {rest} from all "
            f"others; the parts sum to the stated wholes and all four distractors "
            f"recompute false")


TABLE_CHECKS = {3: q3, 7: q7, 12: q12}

CLAIMS = [
 ("Human activity contributing to deforestation",
  "KC-6.1.II.A states that human activity contributed to deforestation, desertification, a decline in air quality, and increased consumption of the world's supply of fresh water. A district record of woodland cleared for cultivation and timber is the first of those four observed locally, and skill 4.B asks a student to situate a specific development inside its broader process."),

 ("Compete over these and other resources more intensely than ever before",
  "KC-6.1.II.A states that as human activity contributed to the four changes it names, humans competed over these and other resources MORE INTENSELY THAN EVER BEFORE. Intensified competition is the consequence the framework's own sentence gives."),

 ("area under forest fell in each period recorded, and the area not under forest rose",
  "KC-6.1.II.A names deforestation among the changes to which human activity contributed. The survey is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in q3 above; the table records a change in land cover and attributes it to no one in particular."),

 ("contributed to debates about the nature and causes of climate change",
  "KC-6.1.II.B states that the release of greenhouse gases and pollutants into the atmosphere CONTRIBUTED TO DEBATES ABOUT the nature and causes of climate change. The framework records the releases and the debates; it does not settle what the nature or the causes are, and a distractor has it settling the question, so the anchor carries the debate rather than a verdict."),

 ("desertification, one of the changes to which human activity contributed",
  "KC-6.1.II.A names desertification among the four changes to which human activity contributed. Land at a dry margin worked without rest until it will no longer hold a crop is that change described in the field, and the framework distinguishes it from the other three named in the same sentence."),

 ("having contributed to them, rather than as their only cause",
  "KC-6.1.II.A states that human activity CONTRIBUTED TO deforestation, desertification, a decline in air quality, and increased consumption of the world's supply of fresh water. Contributed is the framework's own verb, weaker than sole causation and stronger than no part at all, and distractors take it in both directions, so the anchor carries the verb together with what it excludes."),

 ("agriculture accounted for the largest part in every period",
  "KC-6.1.II.A names increased consumption of the world's supply of fresh water among the changes to which human activity contributed. The record is hypothetical and is recomputed from the table alone in q7 above; the last distractor is true of the agricultural quantity and false of the agricultural share, and the verifier computes both so the two cannot be confused."),

 ("decline in air quality, to which human activity contributed",
  "KC-6.1.II.A names a decline in air quality among the four changes to which human activity contributed. Smoke from domestic fires and factories producing a persistent haze is that decline observed in one city, and skill 4.B asks a student to place a specific finding inside the broader process."),

 ("contributed to debates about the nature and causes of climate change, and leaves those debates open",
  "KC-6.1.II.B states that the releases contributed to DEBATES ABOUT the nature and causes of climate change. The framework's subject is the existence of the debates, not a verdict within them. This claim, and this item, exist to mark that boundary, and the anchor carries the framework's own reticence as well as its assertion."),

 ("Deforestation, desertification, a decline in air quality, and increased consumption of fresh water",
  "KC-6.1.II.A names exactly these four. Each distractor mixes in developments the framework states in other sentences of this course, which is the cross-sentence error a list item is built to catch."),

 ("more intense competition over resources that followed the environmental changes",
  "KC-6.1.II.A states that as human activity contributed to the four changes it names, humans competed over these and other resources more intensely than ever before. Two states disputing the flow of a shared river is that competition in its plainest form, and the framework counts increased consumption of fresh water among the changes driving it."),

 ("rose in each period, while the share coming from the first group of states fell",
  "KC-6.1.II.B states that the release of greenhouse gases and pollutants into the atmosphere contributed to debates about the nature and causes of climate change, so the quantity and distribution of releases is course content. The index is hypothetical and names no real state; it is recomputed from the table alone in q12 above, and neither the item nor this claim says anything about responsibility for the releases."),

 ("humans competed over resources more intensely than ever before",
  "KC-6.1.II.A ends with that statement, which is a claim about unprecedented intensity. The pamphlet's claim is the framework's own comparison, and each distractor denies some part of the sentence."),

 ("contradicts the claim, stating that human activity contributed to the changes it names",
  "KC-6.1.II.A states that human activity CONTRIBUTED TO the four changes. Contributed contradicts no involvement without asserting sole causation, and a distractor overshoots to sole causation, so the anchor carries the verdict together with the framework's own verb."),

 ("Increased consumption of the world's supply of fresh water",
  "KC-6.1.II.A names increased consumption of the world's supply of fresh water among the four changes to which human activity contributed. Wells needing to be sunk deeper each year is that consumption recorded by the authority that manages it, and skill 4.B asks a student to place the local record inside the broader process."),

 ("became less intense than it had been before 1900",
  "KC-6.1.II.A states that humans competed over these and other resources MORE INTENSELY THAN EVER BEFORE, so reduced intensity reverses the framework's sentence. The item asks which statement is NOT supported, so the anchor is pinned to the false one deliberately; the other four restate the four changes the same sentence names."),

 ("since releases into the atmosphere contributed to debates about the nature and causes of climate change",
  "KC-6.1.II.B states exactly that. The disagreement between two articles is one instance of the debates the framework names, and the framework endorses neither side, which is what this key says and all it says."),

 ("contributing to deforestation, one of the environmental changes of the period",
  "KC-6.1.II.A names deforestation first among the changes to which human activity contributed. A plan to clear woodland for farms is a decision contributing to that change, and skill 4.B asks a student to situate the specific proposal within the broader process rather than to judge the proposal."),

 ("contributed to environmental changes and that humans then competed over those resources more intensely",
  "KC-6.1.II.A joins the two in one sentence: as human activity contributed to deforestation, desertification, a decline in air quality, and increased consumption of the world's supply of fresh water, humans competed over these and other resources more intensely than ever before. The reasoning process the CED prints beside this topic is causation, and that sentence is the causal chain, so the anchor carries both links."),

 ("decline in air quality and about releases into the atmosphere during this period",
  "KC-6.1.II.A names a decline in air quality among the changes to which human activity contributed, and KC-6.1.II.B names the release of pollutants into the atmosphere and the debates it contributed to. A city beginning to measure its air daily belongs inside those two, which skill 4.B asks a student to identify as the broader context."),

 ("says human activity contributed to the changes and names no particular actor as responsible",
  "KC-6.1.II.A makes HUMAN ACTIVITY the subject of its sentence and names no country, industry or generation. A reading that supplied one would go beyond the framework, which is precisely why no key in this module assigns responsibility for any environmental change."),

 ("release of greenhouse gases and pollutants into the atmosphere, and debates about the nature and causes of climate change",
  "KC-6.1.II.B fixes the release as prior and the debates as what it contributed to. A distractor reverses the order, so the anchor names both terms in the framework's own direction."),

 ("increased consumption of fresh water and the sharper competition over resources that followed",
  "KC-6.1.II.A names increased consumption of the world's supply of fresh water among the changes to which human activity contributed and states that humans competed over such resources more intensely than ever before. Skill 4.B, the suggested skill for this topic, asks a student to situate a specific development inside a broader process, which page counts and prose judgements do not do."),

 ("contributed to debates of exactly this kind, without the framework favouring either proposal",
  "KC-6.1.II.B states that the release of greenhouse gases and pollutants into the atmosphere contributed to debates about the nature and causes of climate change. Two opposed policy papers responding to the same measurements are an instance of those debates, and the framework describes them without taking a side, so the anchor carries the debate and the framework's neutrality together."),

 ("resources affected by the period's environmental changes, and other resources besides",
  "KC-6.1.II.A states that humans competed over THESE AND OTHER RESOURCES more intensely than ever before, where these are the resources implicated in the four named changes. The framework's phrase reaches past the four, so a key confined to one of them would understate the sentence."),

 ("intensified competition over resources that accompanied the period's environmental changes",
  "KC-6.1.II.A states that as human activity contributed to the four named changes, humans competed over these and other resources more intensely than ever before. Buyers bidding against one another for what had been freely available is that intensified competition recorded commercially."),

 ("What the nature and causes of climate change are",
  "KC-6.1.II.A asserts the four environmental changes and human activity's contribution to them as course content, while KC-6.1.II.B asserts only that releases contributed to DEBATES ABOUT the nature and causes of climate change. The framework therefore states the four and leaves the content of the debates open; this item keys which question the framework leaves open against four it settles, and is the sharpest statement in this module of what the bank will not decide."),

 ("sharper competition over resources that followed the environmental changes of the period",
  "KC-6.1.II.A states that as human activity contributed to deforestation and the other changes it names, humans competed over these and other resources more intensely than ever before. A council forced to choose between two uses of the same land is that competition inside one jurisdiction, and skill 4.B asks for the broader process a specific decision belongs to."),

 ("Sharper competition over resources, and debates about the nature and causes of climate change",
  "KC-6.1.II.A ends in competition more intense than ever before and KC-6.1.II.B ends in debates about the nature and causes of climate change. Those are the two outcomes the topic's two sentences name, and the framework supplies a debate rather than a verdict, which the key preserves and a distractor removes."),

 ("releases into the atmosphere fed debates about the climate that the course does not settle",
  "KC-6.1.II.A supplies the four changes, human activity's contribution to them, and the competition more intense than ever before; KC-6.1.II.B supplies the releases and the debates about the nature and causes of climate change. The key is the conjunction of the two sentences, keeping contributed rather than caused and a debate rather than a verdict, and each distractor breaks at least one of those."),
]

wh.run(w9_3, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
