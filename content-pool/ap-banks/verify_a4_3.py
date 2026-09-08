"""Key audit for AP U.S. HISTORY 4.3 Politics and Regional Interests.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The shared gate is
``wh_check.run``.

WHAT THE KEYS REST ON
---------------------
  Unit 4 Learning Objective C, how different
    regional interests affected debates about
    the role of the federal government            items 1, 5, 8, 16, 21, 22, 23, 24
  KC-4.1.I.D, regional interests trumping
    national concerns on slavery and economic
    policy                                        2, 3, 4, 5, 20, 25, 29, 30
  KC-4.2.III.D, plans to unify the economy
    debated as agriculture against industry and
    potentially favouring different sections      6, 7, 8, 9, 15, 18, 20, 25, 27, 30
  KC-4.3.II.C, congressional compromise stemming
    growing tensions only temporarily             10, 11, 12, 13, 14, 19, 26, 28, 30
  KC-4.2.III and KC-4.3.II, the parent concepts   14, 15, 25
  the Politics and Power thematic focus           16
  skill 2.B against 2.A, and the Comparison
    reasoning process                             17, 18, 19, 20, 21, 22, 23, 24

WHAT IS NOT ASSERTED. The CED names the American System and the Missouri
Compromise as EXAMPLES -- its own words are "such as" -- and gives neither
terms, dates nor authors. Items 7 and 12 therefore ask only which sentence names
which example, which is a fact about the framework rather than about the
legislation, and nothing anywhere in the module states what either measure
contained.

SENSITIVE MATERIAL. Two of this topic's three sentences concern slavery. Every
key states it in the framework's own terms -- growing tensions between opponents
and defenders of slavery, stemmed only temporarily by congressional compromise
-- and adds nothing to them.

THE SWAP ITEMS. Item 2 exchanges regional interests with national concerns, item
14 exchanges a key concept with the sub-point beneath it, item 24 exchanges the
definitions of Comparison and Causation, and item 29's leading distractor
exchanges agreement within a region for disagreement. Those anchors carry BOTH
clauses.

DATA ITEMS: 27, 28 and 29 carry tables of explicitly hypothetical figures. Each
check recomputes the keyed claim and falsifies every distractor from the same
rows FIRST, and compares the rows against the literal list LAST -- the ordering
verify_a4_1.py records, so that a control exchanging a category fires on the
guard it names rather than on row equality, while every cell still stays
load-bearing.

NEGATIVE CONTROLS: ``python3 verify_a4_3.py --selftest``.
"""
import sys

import cg_check as cg
import wh_check
import wh_stimulus
import a4_3

FOR_PLAN = "Votes cast for a plan to further unify the economy"
AGAINST_PLAN = "Votes cast against that plan"
YEARS = "Years until tension over slavery rose again"
RESOLVED = "Was the underlying disagreement recorded as resolved?"
REGION = "Region represented"
POSITION = "Position taken on a proposed economic measure"

_EXPECTED_SECTIONS = [
    ["Section 1", "34", "6"],
    ["Section 2", "29", "9"],
    ["Section 3", "5", "31"],
]

_EXPECTED_COMPROMISE = [
    ["Compromise 1", "8", "No"],
    ["Compromise 2", "6", "No"],
    ["Compromise 3", "4", "No"],
    ["Compromise 4", "3", "No"],
]

_EXPECTED_LEADERS = [
    ["Leader 1", "Region A", "In favour"],
    ["Leader 2", "Region A", "In favour"],
    ["Leader 3", "Region B", "Opposed"],
    ["Leader 4", "Region B", "Opposed"],
    ["Leader 5", "Region C", "Opposed"],
]


def _rows_are(table, expected, what):
    assert [list(r) for r in table["rows"]] == expected, (
        f"the {what} table does not hold the rows this check was written against; "
        f"got {table['rows']}"
    )


def q27(table, item):
    """Two sections back the plan and one opposes it, and none is evenly divided."""
    labs = cg.labels(table)
    assert labs == ["Section 1", "Section 2", "Section 3"], \
        f"the three sections the key speaks of are not the rows: {labs}"
    yes, no = cg.col(table, FOR_PLAN), cg.col(table, AGAINST_PLAN)
    backing = [y > n for y, n in zip(yes, no)]
    assert sum(backing) == 2 and sum(backing) == len(labs) - 1, (
        f"the key needs exactly two sections backing the plan and one opposing it; "
        f"got {yes} for against {no} against"
    )
    assert not all(backing), "'all three sections support the plan' must be false"
    assert any(backing), "'all three sections oppose the plan' must be false"
    assert all(y != n for y, n in zip(yes, no)), \
        f"'the sections divide evenly' must be false; got {yes} against {no}"
    dissent = [i for i, n in enumerate(no) if n > 0]
    assert len(dissent) == len(labs), (
        f"'only one section recorded any votes against' must be false; {len(dissent)} of "
        f"{len(labs)} rows record votes against"
    )
    _rows_are(table, _EXPECTED_SECTIONS, "division")
    return (f"votes for run {yes} against {no}, so two of the three sections back the plan "
            f"and one opposes it, with every row recording some dissent")


def q28(table, item):
    """Tension returns after every compromise and no underlying disagreement is resolved."""
    labs = cg.labels(table)
    assert labs == [f"Compromise {n}" for n in range(1, 5)], \
        f"the four compromises the choices speak of are not the rows: {labs}"
    resolved = [cg.normalize(r[table["headers"].index(RESOLVED)]) for r in table["rows"]]
    assert all(v == "no" for v in resolved), (
        f"the key needs no recorded compromise to have resolved the disagreement; "
        f"got {resolved}"
    )
    assert not any(v == "yes" for v in resolved), \
        "'every compromise resolved the underlying disagreement' must be false"
    years = cg.col(table, YEARS)
    returned = [y for y in years if y > 0]
    assert len(returned) == len(labs), (
        f"'tension rose again after only one of the four' must be false; it rose again "
        f"after {len(returned)} of {len(labs)}"
    )
    assert all(years[i + 1] < years[i] for i in range(len(years) - 1)), (
        f"'the interval lengthens with each compromise' must be false; the intervals are "
        f"{years}"
    )
    assert all(y > 1 for y in years), (
        f"'no compromise held for more than a year' must be false; the shortest interval "
        f"is {min(years)} years"
    )
    _rows_are(table, _EXPECTED_COMPROMISE, "compromise")
    return (f"all four rows record the disagreement unresolved, with tension returning "
            f"after {years} years, intervals that shorten rather than lengthen")


def q29(table, item):
    """Position tracks region: agreement inside each region, disagreement between them."""
    labs = cg.labels(table)
    assert labs == [f"Leader {n}" for n in range(1, 6)], \
        f"the five leaders the choices speak of are not the rows: {labs}"
    ri = table["headers"].index(REGION)
    pi = table["headers"].index(POSITION)
    regions = [cg.normalize(r[ri]) for r in table["rows"]]
    positions = [cg.normalize(r[pi]) for r in table["rows"]]
    by_region = {}
    for reg, pos in zip(regions, positions):
        by_region.setdefault(reg, set()).add(pos)
    split = [reg for reg, seen in by_region.items() if len(seen) > 1]
    assert not split, (
        f"the key needs every region to be of one mind; {split} hold more than one position"
    )
    assert len(set(positions)) > 1, \
        f"'all five leaders take the same position' must be false; got {set(positions)}"
    shared = [reg for reg, _ in by_region.items() if regions.count(reg) > 1]
    assert len(shared) >= 2, (
        f"'only one region is represented by more than one leader' must be false; "
        f"{len(shared)} regions carry more than one"
    )
    assert len(set(positions)) < len(positions), \
        "'no two leaders take the same position' must be false"
    _rows_are(table, _EXPECTED_LEADERS, "leaders")
    return (f"{len(by_region)} regions each hold a single position, {len(shared)} of them "
            f"with more than one leader, across {len(set(positions))} distinct positions")


TABLE_CHECKS = {27: q27, 28: q28, 29: q29}

CLAIMS = [
 ("regional interests affected debates about the role of the federal government",
  "Unit 4 Learning Objective C reads 'Explain how different regional interests affected debates about the role of the federal government in the early republic', with the influence running from interests to debates; the leading distractor reverses that direction."),
 ("Regional interests often trumped national concerns",
  "KC-4.1.I.D, verbatim. The anchor carries both terms in the framework's own order because the leading distractor exchanges them."),
 ("Slavery and economic policy",
  "KC-4.1.I.D names positions on slavery and economic policy as the ones for which regional interests often trumped national concerns; foreign policy belongs to KC-4.3.I.A.ii."),
 ("frequent pattern rather than a rule without exception",
  "KC-4.1.I.D's word OFTEN describes a frequent pattern and stops short of a universal rule, which is why neither 'every case' nor 'rare' matches it."),
 ("Many political leaders",
  "KC-4.1.I.D speaks of many political leaders' positions, which is narrower than the electorate and different from judges or the voluntary associations of KC-4.1.III.A. Unit 4 Learning Objective C concerns the debates those leaders conducted."),
 ("benefit agriculture or industry",
  "KC-4.2.III.D states that plans to further unify the U.S. economy generated debates over whether such policies would benefit agriculture or industry; the closest distractor turns the framework's OR into an AND and the debate into agreement."),
 ("The American System",
  "KC-4.2.III.D names the American System as its example of a plan to further unify the U.S. economy. The framework says 'such as' and gives no terms, so the item asks only which sentence names which example."),
 ("also a debate between sections",
  "KC-4.2.III.D ends 'potentially favoring different sections of the country', which is what makes the economic question a sectional one, and Unit 4 Learning Objective C asks how regional interests affected such debates."),
 ("generated debates that set sections against one another",
  "KC-4.2.III.D calls them plans to FURTHER UNIFY the economy and then reports the sectional debate they generated, so the unifying aim and the divisive response sit in one sentence; KC-4.2.III makes the same double point."),
 ("only temporarily stemmed growing tensions",
  "KC-4.3.II.C, verbatim: congressional attempts at political compromise only temporarily stemmed growing tensions, which is neither a permanent settlement nor an absence of effect."),
 ("Opponents and defenders of slavery",
  "KC-4.3.II.C names the parties to the growing tensions; agriculture against industry is KC-4.2.III.D's division and the federal against state governments is KC-4.1.I.B's."),
 ("The Missouri Compromise",
  "KC-4.3.II.C names the Missouri Compromise as its example of a congressional attempt at political compromise, against KC-4.2.III.D's example of a plan to unify the economy."),
 ("intensifying rather than subsiding",
  "KC-4.3.II.C calls the tensions GROWING and says compromise stemmed them only temporarily, which describes intensification rather than decline or a steady state."),
 ("KC-4.3.II says western acquisition gave rise to contests",
  "KC-4.3.II is the key concept and KC-4.3.II.C the sub-point printed beneath it, reporting how Congress responded. The anchor carries both halves because the leading distractor exchanges the two levels."),
 ("plans to unify the economy generated debates potentially favoring different sections",
  "KC-4.2.III.D is the sub-point printed beneath KC-4.2.III on this page and carries the same doubleness the parent concept states, unity alongside the growth of different regions."),
 ("Debates fostered by social and political groups about the role of government",
  "The Politics and Power thematic focus printed on this topic's page names these debates as what shapes government policy, institutions, political parties and the rights of citizens, which is the shaping Unit 4 Learning Objective C traces from regional interests."),
 ("Explain the point of view, purpose, historical situation",
  "Skill 2.B as printed beside this topic's title, in service of Unit 4 Learning Objective C; skill 2.A is the same list under IDENTIFY and is printed on topic 4.2."),
 ("speaks for an agricultural interest",
  "Skill 2.B asks students to EXPLAIN a point of view rather than name it, and KC-4.2.III.D supplies the ground, a debate over whether a unifying policy would benefit agriculture or industry."),
 ("price of getting other work done",
  "Skill 2.B asks for an explanation of purpose, meaning what the source is trying to achieve and by what means; KC-4.3.II.C supplies the setting of congressional attempts at compromise over the extension of slavery."),
 ("because Congress is the body that sets the duty",
  "Skill 2.B asks students to explain an audience rather than name it. KC-4.2.III.D places the question of whom a policy benefits among the sectional debates, and KC-4.1.I.D has regional interests underlying leaders' positions on economic policy."),
 ("help account for the argument it makes",
  "Skill 2.B asks students to explain a source's historical situation and skill 2.C to explain how such features limit its uses, which treats circumstance as an explanation of the argument. KC-4.1.I.D gives the kind of circumstance Unit 4 Learning Objective C is about."),
 ("Comparison, which involves describing and explaining similarities and differences",
  "The unit's table prints Comparison as this topic's reasoning process, matching Unit 4 Learning Objective C's demand for how DIFFERENT regional interests affected debates, and the framework defines it by similarities and differences between developments."),
 ("relative historical significance of similarities and differences",
  "Aspect 1.iii of the Comparison reasoning process, which is what Unit 4 Learning Objective C requires when regional interests are weighed against national concerns as KC-4.1.I.D describes. The weighing of causes and effects is aspect 2.v of Causation instead."),
 ("Comparison sets developments beside one another, while Causation traces what produced a development",
  "The framework defines Comparison by similarities and differences and Causation by causes, effects and the relationship between them. The anchor carries both halves because the leading distractor exchanges the definitions, and both processes appear inside Unit 4 -- Comparison here under Unit 4 Learning Objective C, Causation on topics 4.2 and 4.4."),
 ("plans to unify the economy would benefit agriculture or industry",
  "KC-4.2.III.D is the economic sentence on this page; the rejected options come from KC-4.3.II.C, KC-4.3.II and KC-4.1.I.D and concern the politics of slavery."),
 ("KC-4.3.II.C, which says such compromises only temporarily stemmed",
  "KC-4.3.II.C is the direct denial that a compromise closed the dispute; the other sentences named concern economic debate, the franchise and the unifying effect of economic development."),
 ("two supporting the plan and one opposing it",
  "Recomputed in q27 from the table alone: two rows record more votes for than against and one the reverse. KC-4.2.III.D describes plans to further unify the economy generating debates that potentially favoured different sections of the country."),
 ("none resolved the underlying disagreement",
  "Recomputed in q28 from the table alone: every row records renewed tension and no resolution. KC-4.3.II.C states that congressional attempts at political compromise only temporarily stemmed growing tensions between opponents and defenders of slavery."),
 ("same region take the same position, and the positions differ between regions",
  "Recomputed in q29 from the table alone: each region holds one position and the regions differ. KC-4.1.I.D states that regional interests often trumped national concerns as the basis for many political leaders' positions. The anchor carries both clauses because the leading distractor exchanges agreement within a region for disagreement."),
 ("plans to unify the economy were argued over as sectional questions",
  "The keyed sentence collects KC-4.1.I.D, KC-4.2.III.D and KC-4.3.II.C in the order the topic page prints them and adds nothing; each rejected version reverses or denies one of the three."),
]


def _extra_mutations():
    def a_compromise_resolves_it(mod, cl):
        # The uniformity guard is written FIRST in q28 so this control fires on
        # the claim the item makes rather than on the literal row comparison.
        t = mod.QUESTIONS[27]["table"]
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][1][2] = "Yes"

    def a_region_splits(mod, cl):
        t = mod.QUESTIONS[28]["table"]
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][3][2] = "In favour"

    def every_section_backs_the_plan(mod, cl):
        t = mod.QUESTIONS[26]["table"]
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][2][1], t["rows"][2][2] = "31", "5"

    return [
        ("a compromise recorded as resolving the disagreement", a_compromise_resolves_it),
        ("one region's two leaders recorded on opposite sides", a_region_splits),
        ("the third section's votes reversed so every section backs the plan",
         every_section_backs_the_plan),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    wh_stimulus.controls(a4_3)
    for label, mutate in _extra_mutations():
        mod = wh_check._mutant(a4_3)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            wh_check.history_style(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as e:
            print(f"  control OK  {label}: {str(e)[:110]}")
        else:
            raise SystemExit(f"CONTROL FAILED: {label} did not raise")

wh_check.run(a4_3, CLAIMS, TABLE_CHECKS, sys.argv)
