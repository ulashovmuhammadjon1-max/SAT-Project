"""Key audit for AP WORLD HISTORY: MODERN 8.4 Spread of Communism After 1900.

WHY THIS FILE EXISTS AT ALL. `w8_4.py` was written by an agent that was stopped
before it wrote a verifier, so thirty questions sat in the bank with no gate on
them. Every item below has now been read against the CED page for topic 8.4 and
the three sentences that page prints; the module comment lists them and they
match the CED text word for word.

ONE DEFECT WAS FOUND AND FIXED, and it is recorded here rather than quietly
repaired. q9's keyed choice read "in the two years when output fell furthest,
the quantity taken by the state stood above its first-year level". The output
column runs 100, 85, 71, 78, so the two years in which output stood FURTHEST
BELOW the first year are years three and four -- and the state's take in year
four is 96, which is not above 100. The claim was true only on the second
reading, "the two sharpest year-on-year drops". A key that is true on one
reading of its own words and false on another is a wrong key, so the choice was
replaced with an unambiguous claim on the same figures: the year of lowest
output was also the year of the largest state take (year three, 71 and 124).
`q9` below recomputes exactly that, and also recomputes the falsity of all four
distractors, so the table is defended cell by cell rather than at one point.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code, for a human
to audit. `wh_check` refuses any claim or `why` that cites neither a KC code nor
a Learning Objective.

WHERE A DISTRACTOR IS THE SWAP OF THE KEY, THE ANCHOR CARRIES BOTH CLAUSES.
Seven items here are built on a reversal a prepared student could believe:

  q5   "sometimes" advocating communism swapped for "always"
  q7   largest holder before swapped between smallest and largest after
  q11  "fewer than half" swapped for "more than half"
  q12  "sometimes" swapped for "never"
  q14  the NOT-supported item, where the key is the false statement
  q17  cause and effect reversed, the seizure of power causing the aggression
  q20  a redistribution that did NOT advocate communism, against one that did

For each, the anchor spans the whole relation and not just one noun, so an
anchor that matched the swapped distractor would fail the gate rather than pass
it. That defect is on record in `verify_e2_1.py`.

THE WORD "SOMETIMES" IS THE CONTENT RISK IN THIS TOPIC and three claims below
say so. KC-6.2.II.D.i says redistribution movements SOMETIMES advocated
communism or socialism. In a topic titled Spread of Communism the tempting
error is to key every land reform as communist, which would teach the opposite
of the framework's own sentence.

WHAT THIS CANNOT DO: it cannot tell whether the history is right. It gates
structure, key/anchor agreement, notation, the absence of figure language, the
presence of a citation, and the arithmetic of the three data questions. The
history is gated by the claims below and by the rule in HISTORY_BRIEF.md that a
key must trace to a sentence in the CED.

NEGATIVE CONTROL: `python3 verify_w8_4.py --selftest`, which rotates all thirty
keys, breaks all thirty anchors, corrupts every cell of every table, injects
each banned notation form, injects figure language, strips the citation from a
why and from a claim, duplicates a choice, thins a why and makes a why name an
option by letter -- asserting in each case WHICH message came back, not merely
that something raised. Positive controls run alongside, so a gate that rejected
everything would fail here rather than look thorough.
"""
import sys

import cg_check as cg
import wh_check as wh
import w8_4

T_LAND = w8_4._T_LAND
T_CAMPAIGN = w8_4._T_CAMPAIGN
T_REGION = w8_4._T_REGION

BEFORE = "Share of farmland held before the reform (percent)"
AFTER = "Share of farmland held after the reform (percent)"
OUTPUT = "Grain output (index, first year = 100)"
TAKEN = "Grain taken by the state (index, first year = 100)"
PROGRAMS = "States adopting a national land redistribution program"
DECLARED = "Of those, states whose program declared a communist or socialist aim"
NOLAND = "Households holding no land before the reform"


def q7(table, item):
    """The largest holder before the reform is the smallest holder after it."""
    labs = cg.labels(table)
    before = dict(zip(labs, cg.col(table, BEFORE)))
    after = dict(zip(labs, cg.col(table, AFTER)))
    # Both columns are SHARES of the district's farmland, so each must total 100.
    # This is a real property of the data rather than a contrivance to make the
    # control look busy, and it is what defends the interior cells: the extreme
    # cell of a column cannot be caught by a max/min test alone, because the
    # corruption in es_check only ever makes a number larger.
    for header in (BEFORE, AFTER):
        total = sum(cg.col(table, header))
        assert abs(total - 100) < 1e-9, \
            f"the column {header!r} is a set of shares and totals {total}, not 100"
    assert sorted(labs) == sorted(
        ["Largest landholders", "Middling holders", NOLAND,
         "Village and collective holdings"]), \
        f"the four holding groups the key and its distractors name are not the rows: {labs}"
    top_before = cg.ranked(table, BEFORE)[0]
    low_after = cg.ranked(table, AFTER)[-1]
    assert top_before == low_after, (
        f"the key needs the largest holder before the reform ({top_before}) to be the "
        f"smallest after it ({low_after})")
    # and every distractor false on the same numbers
    top_after = cg.ranked(table, AFTER)[0]
    assert top_before != top_after, \
        "'largest before was also largest after' must be false"
    assert any(after[l] > before[l] for l in labs), \
        "'every group's share fell' must be false"
    assert sum(after.values()) >= 0.5 * sum(before.values()), \
        "'the after column totals less than half the before column' must be false"
    assert after[NOLAND] > 0, \
        "'households holding no land before still held none afterward' must be false"
    return (f"before the reform {top_before} held the largest share and after it the "
            f"smallest; the after column runs {after} against {before} before, and all "
            f"four distractors recompute false")


def q9(table, item):
    """The year of lowest output is the year of the largest state take."""
    years = cg.labels(table)
    out = dict(zip(years, cg.col(table, OUTPUT)))
    took = dict(zip(years, cg.col(table, TAKEN)))
    low_out = cg.ranked(table, OUTPUT)[-1]
    top_took = cg.ranked(table, TAKEN)[0]
    assert low_out == top_took, (
        f"the key needs the year of lowest output ({low_out}) to be the year of the "
        f"largest state take ({top_took})")
    # The ranking alone would be satisfied by ties, which would make the keyed
    # "the year in which" false because there would be more than one such year.
    outs = cg.col(table, OUTPUT)
    takes = cg.col(table, TAKEN)
    assert outs.count(min(outs)) == 1 and takes.count(max(takes)) == 1, (
        f"the key names a single year; output {outs} and take {takes} must each have a "
        f"unique extreme")
    # every distractor false on the same numbers
    steps_out = [b - a for a, b in zip(outs, outs[1:])]
    steps_took = [b - a for a, b in zip(takes, takes[1:])]
    assert any((a > 0) != (b > 0) for a, b in zip(steps_out, steps_took)), \
        "'output and the state take moved together in every year' must be false"
    assert any(s > 0 for s in steps_took), \
        "'the state take fell in every year after the first' must be false"
    assert outs[-1] < outs[0], \
        "'output stood higher in the last year than in the first' must be false"
    assert min(outs) < 0.9 * outs[0], \
        "'output never fell by more than a tenth' must be false"
    return (f"output runs {outs} and the state take {takes}; the single lowest output "
            f"year {low_out} is the single largest take year, and all four distractors "
            f"recompute false")


def q11(table, item):
    """In every region the declared-aim programs are a minority."""
    labs = cg.labels(table)
    progs = dict(zip(labs, cg.col(table, PROGRAMS)))
    decl = dict(zip(labs, cg.col(table, DECLARED)))
    for lab in labs:
        assert 0 < decl[lab] < 0.5 * progs[lab], (
            f"{lab} declared {decl[lab]} of {progs[lab]}, which is not a nonzero "
            f"minority as the key requires")
    # every distractor false on the same numbers
    assert not all(decl[l] > 0.5 * progs[l] for l in labs), \
        "'more than half in every region' must be false"
    assert decl["Latin America"] > 0, \
        "'no Latin American program declared such an aim' must be false"
    assert cg.ranked(table, PROGRAMS)[0] != "Asia", \
        "'Asia recorded more programs than any other region' must be false"
    assert len(set(progs.values())) > 1, \
        "'the three regions recorded the same number' must be false"
    return (f"declared aims {decl} against programs {progs}, a nonzero minority in every "
            f"region, and all four distractors recompute false")


TABLE_CHECKS = {7: q7, 9: q9, 11: q11}

CLAIMS = [
 ("Internal tension within China together with Japanese aggression",
  "KC-6.2.I.i states that as a result of internal tension and Japanese aggression, Chinese communists seized power. The framework names those two conditions and no others; it does not describe a Soviet invasion of China or a negotiated withdrawal by a European colonial power."),

 ("communist revolution",
  "KC-6.2.I.i states that these changes in China eventually led to communist revolution. The framework treats the seizure of power and the revolution as connected stages of one process, not as a restoration, a partition or a turn to free-market policy."),

 ("the government of communist China controlled the national economy",
  "KC-6.3.I.A.ii states that in communist China the government controlled the national economy through the Great Leap Forward. The framework presents the campaign as an instrument of state direction, which is the opposite of opening the economy or handing planning to an outside body."),

 ("often implemented repressive policies, with negative repercussions for the population",
  "KC-6.3.I.A.ii states that the government controlled the national economy through the Great Leap Forward, often implementing repressive policies, with negative repercussions for the population. The framework records the coercion and the harm together, so the anchor carries both and an answer reporting one without the other cannot match it."),

 ("sometimes advocated communism or socialism, rather than always doing so",
  "KC-6.2.II.D.i states that movements to redistribute land and resources developed within states in Africa, Asia, and Latin America, sometimes advocating communism or socialism. The word sometimes is the framework's own; a distractor swaps it for always, so the anchor carries the qualifier and the contrast with always."),

 ("Communist Revolution for Vietnamese independence, Mengistu Haile Mariam in Ethiopia",
  "The CED prints four ILLUSTRATIVE EXAMPLES beside KC-6.2.II.D.i on land and resource redistribution: the Communist Revolution for Vietnamese independence, Mengistu Haile Mariam in Ethiopia, land reform in Kerala and other states within India, and the White Revolution in Iran. The distractor lists are illustrative examples the framework prints beside other statements."),

 ("largest share before the reform had the smallest share after it",
  "KC-6.2.II.D.i describes movements to redistribute land and resources, and a transfer of share between holding groups is what redistribution names. The survey is hypothetical; the keyed conclusion and the falsity of every distractor are recomputed from the table alone in q7 above. A distractor exchanges smallest for largest after the reform, so the anchor carries both ends of the relation."),

 ("written for the authority that ordered the campaign",
  "KC-6.3.I.A.ii records repressive policies and negative repercussions for the population under a campaign of state economic control, which is what a subordinate reporting upward has reason not to record. Unit 8 Learning Objective D is served by skill 2.C, explaining how a source's purpose and audience limit its uses."),

 ("year in which output stood lowest was also the year in which the state took the most",
  "KC-6.3.I.A.ii states that the government controlled the national economy through the Great Leap Forward, often implementing repressive policies, with negative repercussions for the population. A state taking the most in the year production stood lowest is one route by which such repercussions reach a population. The figures are hypothetical and both halves of the claim are recomputed in q9 above."),

 ("each source reports the interest of the group that produced it",
  "KC-6.2.II.D.i places redistribution movements within states, which makes them a conflict between groups with opposed interests in the same land. Reading each source for the position it represents rather than ranking the two for truthfulness is what skill 2.C asks under Unit 8 Learning Objective E."),

 ("fewer than half of the programs declared a communist or socialist aim",
  "KC-6.2.II.D.i states that redistribution movements developed in Africa, Asia, and Latin America and sometimes advocated communism or socialism. A survey in which such declarations are a minority everywhere is that word sometimes made measurable. A distractor swaps fewer for more, so the anchor carries the direction; the figures are hypothetical and are recomputed in q11 above."),

 ("sometimes advocated communism or socialism, so many did not",
  "KC-6.2.II.D.i uses the word sometimes, which rules out both always and never. The correction has to preserve the middle position rather than replace one absolute with another, so the anchor carries the qualifier together with its consequence."),

 ("pursue independence and the redistribution of resources as a single programme",
  "KC-6.2.II.D.i places movements to redistribute land and resources within states in Africa, Asia, and Latin America, and the CED's own illustrative example of a Communist Revolution for Vietnamese independence pairs the demand for independence with redistribution. The framework therefore treats the combination as available rather than impossible."),

 ("took power after a foreign invasion by the Soviet Union",
  "KC-6.2.I.i names internal tension and Japanese aggression as the conditions from which the Chinese communists seized power and names no Soviet invasion, so this is the statement the framework does not support. The item asks which claim is NOT supported, so the anchor is pinned to the false statement deliberately; the other four restate KC-6.2.I.i and KC-6.2.II.D.i."),

 ("testimony about how the campaign was experienced by one person in one place",
  "KC-6.3.I.A.ii records negative repercussions for the population under the campaign, which is what individual testimony can attest and what a single memoir cannot quantify nationally. Judging what a source's situation permits it to support is skill 2.C, the suggested skill for this topic."),

 ("rural population the movement hoped to recruit",
  "KC-6.2.II.D.i places redistribution movements within states in Latin America among other regions, and a slogan poster carrying no figures is built to persuade the people whose support such a movement needs. Identifying the audience a source addresses is skill 2.C under Unit 8 Learning Objective E."),

 ("Japanese aggression, which led to the communists' seizure of power",
  "KC-6.2.I.i states that as a result of internal tension and Japanese aggression, Chinese communists seized power, fixing the two conditions as prior and the seizure as their result. Every distractor makes a later development the cause of an earlier one, so the anchor carries the direction of the relation and not merely its two terms."),

 ("compiled and published by the authority whose campaign they assess",
  "KC-6.3.I.A.ii records repressive policies and negative repercussions for the population under a campaign of state economic control, which gives the compiling authority an interest in the figures it publishes. Explaining how a source's producer and purpose limit its uses is skill 2.C, this topic's suggested skill."),

 ("change who held land and resources within its own state",
  "KC-6.2.II.D.i states that movements to redistribute land and resources developed WITHIN states in Africa, Asia, and Latin America. The framework asserts a common object, the internal distribution of land and resources, and does not assert common organization or a common ideology."),

 ("redistribute land and resources that did not advocate communism",
  "KC-6.2.II.D.i says such movements SOMETIMES advocated communism or socialism, which makes the advocacy a variable feature and the redistribution the defining one. The stem's second case sells estates into private smallholdings, so it redistributes without advocating communism; the distractor that calls any redistribution communist is exactly the reading the word sometimes forbids, and the anchor carries both halves."),

 ("constraints under which publication took place rather than of the campaign's results",
  "KC-6.3.I.A.ii records the government controlling the national economy and often implementing repressive policies, which bears on what could be printed. Uniform praise across every outlet is evidence about the conditions of publication, and reading popular opinion off it would mistake a source's situation for its content."),

 ("Holdings and incomes recorded for those households before and after",
  "KC-6.2.II.D.i describes movements to redistribute land and resources, so a claim about their effects is a claim about who ended up holding what. Announcements, staffing levels and foreign coverage report a programme's intentions or its profile rather than its outcome for the households in question."),

 ("seizure of power in China as leading to communist revolution there, and treats redistribution movements elsewhere as sometimes advocating communism",
  "KC-6.2.I.i traces the Chinese sequence from internal tension and Japanese aggression to the seizure of power and then to communist revolution, while KC-6.2.II.D.i separately places redistribution movements in Africa, Asia, and Latin America that sometimes advocated communism or socialism. The framework sets the two side by side and makes neither the agent of the other, so the anchor carries both halves."),

 ("Both documents state expectations, and neither records what actually followed",
  "KC-6.2.II.D.i places these movements inside states where interested parties disagreed about them, and a prediction reports its author's expectation and interest. Distinguishing what a source's situation allows it to establish from what it merely asserts is skill 2.C, the suggested skill here."),

 ("directed the national economy through campaigns it designed and enforced",
  "KC-6.3.I.A.ii states that in communist China the government controlled the national economy through the Great Leap Forward, often implementing repressive policies. Direction and enforcement by the state is the framework's own description, and each distractor describes a withdrawal of the state that the sentence contradicts."),

 ("fits the framework, which places these movements within states in three world regions",
  "KC-6.2.II.D.i states that movements to redistribute land and resources developed within states in Africa, Asia, and Latin America. Within states is the framework's own wording and it is what the student's argument needs; the framework names no single foreign sponsor."),

 ("read each against the other, asking what each was produced for",
  "KC-6.2.II.D.i and KC-6.3.I.A.ii describe programmes conducted by states with an interest in how they were recorded, alongside testimony gathered later that is free of that interest but subject to memory. Reading each source for its purpose and situation, skill 2.C, is what lets the two be used together."),

 ("took control of the national economy and its campaigns brought repression and harm",
  "KC-6.3.I.A.ii states that the government controlled the national economy through the Great Leap Forward, often implementing repressive policies, with negative repercussions for the population. The key reports the control, the repression and the harm together, which is what Unit 8 Learning Objective D asks for as the consequences of China's adoption of communism."),

 ("within states in Africa, Asia and Latin America over the holding of land and resources, sometimes under a communist or socialist banner",
  "KC-6.2.II.D.i states that movements to redistribute land and resources developed within states in Africa, Asia, and Latin America, sometimes advocating communism or socialism. Unit 8 Learning Objective E asks for the causes of such movements, and the key preserves both the internal origin and the qualifier sometimes."),

 ("directed the economy at heavy cost to the population, while movements over land and resources arose across three world regions and only sometimes took a communist form",
  "KC-6.2.I.i supplies the Chinese conditions and outcome, KC-6.3.I.A.ii the state direction of the economy with repression and negative repercussions, and KC-6.2.II.D.i the redistribution movements across three regions that sometimes advocated communism or socialism. The key is the conjunction of those three sentences and each distractor contradicts at least one."),
]

wh.run(w8_4, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
