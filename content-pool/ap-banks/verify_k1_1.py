"""Key audit for AP COMPARATIVE GOVERNMENT 1.1 The Practice of Political Scientists.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON, AND WHAT THEY DELIBERATELY DO NOT
--------------------------------------------------------
Items 1-4, 10-12, 15 and 21-30 are keyed to sentences the CED prints:
MPA-1.A.1 (the two kinds of source), MPA-1.A.3 (causation cannot be determined
with certainty), MPA-1.A.4 (correlation is association), MPA-1.A.5 (empirical
against normative), MPA-1.A.6 (empirical information supports generalizations
and arguments) and MPA-1.A.7 (comparison is how conclusions are derived).

Items 5-8, 13, 14 and 29 concern the seven data collection resources of
MPA-1.A.8. The framework NAMES those seven and does not define them, so the
keys here rest on what each resource measures -- a stable definitional fact the
framework presupposes by requiring students to investigate relationships with
them, and the same fact the CED's own sample question 2 keys when it prefers the
Human Development Index to per capita GDP as a measure of living standards.
No item asks for a country's value on any index, because that would be a
current-events fact the CED does not supply.

Items 16-21 carry tables. Every number in them is HYPOTHETICAL and the stem says
so; each keyed conclusion is recomputed below from the table alone, and the
distractors are checked to be false against the same numbers. That is the point
of labelling the data: a student can reach the key without knowing anything
about the countries, which is how the exam's quantitative sets work.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k1_1

T_HDI = k1_1._T_HDI
T_FH = k1_1._T_FH
T_GINI = k1_1._T_GINI

GDPPC = "GDP per capita (hypothetical, US$)"
HDI = "Human Development Index (hypothetical, 0-1)"
GINI = "Gini index (hypothetical; 0 = perfect equality, 100 = perfect inequality)"


def q16(table, item):
    cn_gdp, cn_hdi = cg.cell(table, "China", GDPPC), cg.cell(table, "China", HDI)
    mx_gdp, mx_hdi = cg.cell(table, "Mexico", GDPPC), cg.cell(table, "Mexico", HDI)
    assert cn_gdp > mx_gdp and cn_hdi > mx_hdi, "key requires China above Mexico on both"
    # and every distractor false on the same numbers
    ng_gdp = cg.cell(table, "Nigeria", GDPPC)
    assert not (0.45 <= ng_gdp / mx_gdp <= 0.55), "'roughly half of Mexico' must be false"
    uk_hdi, ng_hdi = cg.cell(table, "United Kingdom", HDI), cg.cell(table, "Nigeria", HDI)
    assert uk_hdi <= 2 * ng_hdi, "'more than twice Nigeria' must be false"
    assert not (mx_hdi > cn_hdi), "'Mexico higher HDI than China' must be false"
    over10k = [h for g, h in zip(cg.col(table, GDPPC), cg.col(table, HDI)) if g > 10000]
    assert any(h >= 0.75 for h in over10k), "'all above 10,000 have HDI below 0.75' must be false"
    return "China 12,500 > Mexico 10,200 and China 0.768 > Mexico 0.758; all four distractors false on these numbers"


def q17(table, item):
    by_gdp = cg.ranked(table, GDPPC)
    by_hdi = cg.ranked(table, HDI)
    assert by_gdp == by_hdi, f"orders differ: {by_gdp} vs {by_hdi}"
    return f"ranking by either column gives the same order {by_gdp}, an association and nothing stronger"


def q18(table, item):
    series = {lab: [cg.cell(table, lab, h) for h in ("2010 score", "2015 score", "2020 score")]
              for lab in cg.labels(table)}
    ru = series["Russia"]
    assert ru[1] < ru[0] and ru[2] < ru[1], "Russia must fall in both periods"
    for lab in ("Mexico", "Nigeria"):
        s = series[lab]
        assert s[1] < s[0] and s[2] > s[1] and s[2] < s[0], f"{lab} must fall then partially recover"
    lowest = min(series, key=lambda k: series[k][2])
    assert lowest == "Russia", "the lowest final score is Russia's, so 'Nigeria lowest' is false"
    assert abs(series["Mexico"][2] - series["Mexico"][0]) < abs(ru[2] - ru[0]), \
        "'Mexico changes more than Russia' must be false"
    return "Russia 31-24-20 falls twice; Mexico 66-61-62 and Nigeria 48-45-47 fall then partly recover"


def q19(table, item):
    risers = [lab for lab in cg.labels(table)
              if cg.cell(table, lab, "2020 score") > cg.cell(table, lab, "2015 score")]
    assert len(cg.labels(table)) == 3 and len(risers) == 2, \
        f"key requires three countries with two rising; got {risers}"
    return f"the table holds three countries and {risers} rise between 2015 and 2020"


def q20(table, item):
    order = cg.ranked(table, GINI)
    assert order[0] == "Mexico", f"highest Gini is {order[0]}"
    assert order[-1] == "United Kingdom", f"lowest Gini is {order[-1]}"
    return f"Mexico's 45 is the largest value and the United Kingdom's 33 the smallest"


def q21(table, item):
    gap = cg.cell(table, "Mexico", GINI) - cg.cell(table, "United Kingdom", GINI)
    assert gap == 12, f"the stated 12-point gap recomputes to {gap}"
    return "Mexico 45 minus United Kingdom 33 is 12, so the first quoted statement is checkable"


CLAIMS = [
 ("correlation",
  "EK MPA-1.A.4 defines correlation as an association between two or more variables, and EK MPA-1.A.3 denies that causation can be established with certainty here. An observed co-movement is therefore a correlation and no more."),
 ("both elect a president",
  "EK MPA-1.A.5 requires empirical statements to be separated from normative ones. Only the keyed statement reports an arrangement checkable against evidence; the four distractors turn on ought, should or duty. The institutional fact itself is EK PAU-3.A.2."),
 ("joined to a normative claim",
  "EK MPA-1.A.5. The vetting clause is checkable and the injustice clause applies a value standard, so the sentence carries exactly one of each kind. The vetting fact is EK PAU-3.F.1d."),
 ("no way to isolate which one produced the change",
  "EK MPA-1.A.3, near verbatim: numerous variables potentially influence political policies and regime stability, with no way to isolate and demonstrate which is producing the change."),
 ("Human Development Index",
  "EK MPA-1.A.8 names all five options among its seven data resources; the discriminating fact is that the HDI combines income with health and education attainment, which is what a living-standards comparison needs. The CED's own sample question 2 keys this same preference over per capita GDP."),
 ("Gini index",
  "EK MPA-1.A.8 names the Gini index (coefficient) among the seven resources. It is the distribution measure of the set: per capita GDP is an average that conceals distribution, and the other three measure growth, development and political freedom."),
 ("available on average to each resident",
  "Total GDP scales with population, so equal totals over unequal populations give very different amounts per resident. This is why EK MPA-1.A.8 lists GDP and GDP per capita as separate resources rather than as one."),
 ("expanding quickly from a low starting level",
  "A growth rate reports the speed of change and a per capita figure reports the level, so the two cannot contradict each other. EK MPA-1.A.8 lists them separately for that reason."),
 ("political cartoon",
  "EK MPA-1.A.1 sorts the material explicitly: charts, tables, graphs and maps on one side, speeches, foundational documents, political cartoons and political commentaries on the other. Only the cartoon is on the qualitative side."),
 ("inferences about course countries",
  "EK MPA-1.A.1 states that analysis of this material is a way to make comparisons between and inferences about course countries. It does not license certainty about causation, which EK MPA-1.A.3 denies."),
 ("comparing different political systems",
  "EK MPA-1.A.7, near verbatim: comparative political scientists compare different political systems to derive conclusions about politics. A single case supplies no variation to compare."),
 ("support a generalization",
  "EK MPA-1.A.6 names applying concepts, supporting generalizations and making arguments as the principal uses of empirical information. Turnout figures across five countries backing a general claim is the second of those."),
 ("Freedom House",
  "EK MPA-1.A.8 names Freedom House among the seven resources; it is the set's measure of political rights and civil liberties, which is what the question asks for. The other four report income distribution, output, growth and human development."),
 ("Transparency International",
  "EK MPA-1.A.8 names Transparency International among the seven resources; it is the set's corruption measure. Corruption is the subject of the comparison, and no other listed resource reports it."),
 ("legislative powers of two countries differ",
  "EK MPA-1.A.7 makes comparison across systems the discipline's method, and EK MPA-1.A.5 places value questions outside what evidence settles. Only the keyed question can be answered by observation and comparison."),
 ("both higher than Mexico's",
  "Recomputed from the table in q16 above: China exceeds Mexico on both columns, and each distractor is checked false against the same numbers."),
 ("rise and fall together",
  "Recomputed in q17 above: ranking the four countries by either column yields the same order. EK MPA-1.A.3 is why the stronger causal reading is unavailable from four observations."),
 ("fall and then partially recover",
  "Recomputed in q18 above from the three series, including that Russia rather than Nigeria holds the lowest score and that Russia's full-period change is the largest."),
 ("two of them rose in the most recent period",
  "Recomputed in q19 above: the table holds three countries and two of the three rise between the last two years, so a claim about every country in the world fails both outside and inside the data."),
 ("Mexico",
  "Recomputed in q20 above: the header states higher means more unequal, and Mexico's 45 is the largest of the five values shown."),
 ("the first is empirical and the second is normative",
  "EK MPA-1.A.5's distinction applied to the table: the 12-point gap is recomputed in q21 above and is checkable, whereas what a country ought to tax is a value judgement no table settles."),
 ("cannot distinguish the two directions",
  "EK MPA-1.A.3. An association is symmetric, so the same data fit the reverse account and fit a third variable producing both; nothing in the observation isolates the direction the conclusion asserts."),
 ("began improving several years before",
  "A cause cannot follow its effect. If the outcome was already moving before the proposed cause appeared, the proposed cause cannot account for the start of the movement, which is a limit no other listed finding imposes."),
 ("differ in many respects besides the one named",
  "EK MPA-1.A.3 names the problem for a two-case design: numerous variables potentially influence the outcome and none can be isolated, so wealth, history or cleavage structure fits the result as well as system type."),
 ("quantitative material that supports description of a pattern",
  "EK MPA-1.A.1 names maps among the quantitative material whose analysis supports comparison and inference; reading a pattern is legitimate, attributing a cause to it is what EK MPA-1.A.3 forbids."),
 ("standard of value that observation cannot settle",
  "EK MPA-1.A.5. Both statements concern the same election and the same figure, so the only difference is that the second calls the figure disgraceful, which is a judgement about what turnout ought to be."),
 ("much larger set of countries",
  "EK MPA-1.A.2 treats quantitative analysis as the route to defensible comparisons and inferences. A pattern surviving more cases and more periods is harder to attribute to the particular six chosen; discarding the worst-fitting cases manufactures the pattern instead."),
 ("offers a reason",
  "The CED's data skills run 3.A describe the data, 3.B describe patterns and trends, 3.C explain patterns and trends to draw conclusions, 3.D explain what the data implies about political systems. Only supplying a reason crosses from description into explanation."),
 ("measures a different aspect of a country",
  "EK MPA-1.A.8's seven resources report development, output, growth, distribution, political rights, corruption and state pressure -- separate properties on which one country can rank high and low at once. Nothing about combining them overcomes EK MPA-1.A.3's causal limit."),
 ("quantitative and qualitative material used together",
  "EK MPA-1.A.1 pairs the two kinds of material and EK MPA-1.A.6 names supporting an argument as a principal use of empirical information. The election record and growth figures are quantitative and the speech is qualitative."),
]

cg.check(k1_1, CLAIMS, table_checks={16: q16, 17: q17, 18: q18, 19: q19, 20: q20, 21: q21})
