"""Key audit for AP HUMAN GEOGRAPHY 7.3 Measures of Development.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective SPS-7.C, suggested skill 3.F, and three
statements:

    SPS-7.C.1 measures of social and economic development: GDP, GNP, GNI per
              capita, sectoral structure both formal and informal, income
              distribution, fertility rates, infant mortality rates, access to
              health care, use of fossil fuels and renewable energy, literacy
    SPS-7.C.2 measures of gender inequality, such as the Gender Inequality Index,
              include reproductive health, indices of empowerment, and
              labor-market participation
    SPS-7.C.3 the Human Development Index is a composite measure used to show
              spatial variation among states in levels of development

THE SUGGESTED SKILL IS THE TOPIC. Skill 3.F is "explain possible LIMITATIONS of
the data provided" -- the only suggested skill in this course that is about what
evidence cannot do. So six items (20 to 24 and 29) are limitation items and they
are not an appendix: a student who can recite ten measures and cannot say what
any of them misses has not met what SPS-7.C asks. Item 24 goes furthest, keying
on what the whole list omits -- unpaid household work and resource depletion,
neither of which enters an output figure.

THE THREE DISTINCTIONS THAT DO THE WORK, each with its own item and each with the
confusion as a distractor: GDP counts production INSIDE a border while GNP counts
production by RESIDENTS wherever they are (items 2, 3); a total measures the size
of an economy while a per-capita figure measures what it amounts to per person
(item 4); and a mean says nothing about spread, which is why SPS-7.C.1 lists
income distribution as a measure of its own (items 8, 21, 27). Item 27's table
gives two countries the SAME income per person and completely different
distributions, and its recompute asserts the incomes are identical -- the item
does not work unless they are.

WHAT IS SAFE TO ASSERT ABOUT THE TWO INDICES, and the line is drawn deliberately.
The CED gives the Gender Inequality Index's three components in its own words, so
item 15 keys on the CED's list. For the Human Development Index the CED says only
that it is a COMPOSITE measure showing spatial variation among states, so item 17
keys on that word and item 18 states the three conventional dimensions AS the
conventional composition rather than as the framework's words. No numerical
threshold is attached to either index anywhere in this module, because neither
statement supplies one and a threshold would be a claim the CED does not make.

NO REAL COUNTRY IS NAMED ANYWHERE IN THIS MODULE, the three data items included.
Development indicators are revised and rebased, so a figure true when written can
be wrong when a student reads it, and a lettered country carries the reasoning
just as well.

SYNONYM CARE. `geo_check` treats {"human development index", "hdi"}, {"gender
inequality index", "gii"} and {"gross national income per capita", "gni per
capita"} as three constructs, so no choice list names any of them in two ways.

The three table items (26, 27, 28) are the computational gate:

  26  all four measures checked to rank the countries identically, with infant
      mortality running the OPPOSITE way -- the key's claim is agreement, and a
      single disagreement would defeat it
  27  the two incomes checked to be equal and both share ratios computed, since
      the item exists only because the averages match
  28  all three components and the index checked to fall together, because the
      key states this is the easy case and item 29 is the hard one

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting. One item was again written with a malformed
token in place of `ans=0` -- the fourth this session -- and caught by the
import-and-assert check that now opens every one of these files.
"""
import re

import geo_check
import g7_3

for _n, _item in enumerate(g7_3.QUESTIONS, 1):
    assert isinstance(_item.get("ans"), int), f"7.3 q{_n}: `ans` is {_item.get('ans')!r}"
    assert 0 <= _item["ans"] < len(_item["choices"]), f"7.3 q{_n}: ans out of range"


def q26_measures_agree(table):
    """Four measures must rank the countries identically, mortality inverted."""
    income = [float(r[1].replace(",", "")) for r in table["rows"]]
    mortality = [float(r[2]) for r in table["rows"]]
    literacy = [float(r[3]) for r in table["rows"]]
    index = [float(r[4]) for r in table["rows"]]
    for series in (income, literacy, index):
        assert all(b < a for a, b in zip(series, series[1:])), series
    # Infant mortality is the one that runs the other way, by construction.
    assert all(b > a for a, b in zip(mortality, mortality[1:])), mortality
    assert mortality[0] == 4 and mortality[-1] == 68, mortality
    assert index[0] == 0.92 and index[-1] == 0.42, index
    return f"infant mortality rises from {mortality[0]:.0f} to {mortality[-1]:.0f}"


def q27_same_mean_different_spread(table):
    """The two incomes must be EQUAL, or the item has no point."""
    rows = {r[0]: (float(r[1].replace(",", "")), float(r[2].replace(",", "")))
            for r in table["rows"]}
    inc_x, inc_y = rows["Gross National Income per person"]
    assert inc_x == inc_y == 14000, (inc_x, inc_y)
    poor_x, poor_y = rows["Share of national income received by the poorest fifth (%)"]
    rich_x, rich_y = rows["Share of national income received by the richest fifth (%)"]
    ratio_x = rich_x / poor_x
    ratio_y = rich_y / poor_y
    assert 20 < ratio_x < 21.5, ratio_x
    assert 4 < ratio_y < 4.5, ratio_y
    assert ratio_x > 4 * ratio_y, (ratio_x, ratio_y)
    return f"about {ratio_x:.0f} times the poorest fifth's share in one country"


def q28_components_agree(table):
    """All three components and the index fall together -- the easy case."""
    life = [float(r[1]) for r in table["rows"]]
    school = [float(r[2]) for r in table["rows"]]
    income = [float(r[3].replace(",", "")) for r in table["rows"]]
    index = [float(r[4]) for r in table["rows"]]
    for series in (life, school, income, index):
        assert all(b < a for a, b in zip(series, series[1:])), series
    assert life[0] == 82 and life[-1] == 62, life
    assert school[0] == 17.5 and school[-1] == 9.8, school
    assert index[0] == 0.93 and index[-1] == 0.53, index
    return "All three components fall together"


CLAIMS = [
 ("The rank-size rule",
  "EK SPS-7.C.1 names infant mortality, literacy, income distribution and access to health care among its measures, along with the national accounts and energy use. The rank-size rule belongs to EK PSO-6.C.1 and describes the size distribution of a country's cities."),

 ("produced inside a country's borders",
  "EK SPS-7.C.1 names Gross Domestic Product among the measures of social and economic development. The word domestic marks the boundary: what counts is where production happened, not who owned the operation that carried it out."),

 ("what a country's residents produce wherever they are",
  "EK SPS-7.C.1 names both Gross Domestic Product and Gross National Product among its measures, which implies they differ. One is bounded by territory and the other by who the producer belongs to, and the gap is largest where profits and wages cross borders heavily."),

 ("dividing by population measures what it amounts to for each person",
  "EK SPS-7.C.1 names Gross National Income PER CAPITA specifically. A populous country can have an enormous total and a modest figure per person, so the total ranks economies by size and the per-capita figure by what an average resident has."),

 ("The same sum of money buys different amounts in different countries",
  "EK SPS-7.C.1 names Gross National Income per capita among the measures and suggested skill 3.F asks for the limitations of data. A figure converted at a market exchange rate measures what a resident could buy abroad rather than what they can buy at home."),

 ("shift as an economy develops, so the composition itself indicates a level",
  "EK SPS-7.C.1 names sectoral structure among the measures of development and EK SPS-7.B.1 says the sectors are characterized by distinct development patterns. The second statement is what makes the first a measure rather than a description."),

 ("Much economic activity is unregistered and untaxed",
  "EK SPS-7.C.1 names sectoral structure of an economy, BOTH FORMAL AND INFORMAL. The qualification is a warning built into the statement: where much work is unregistered, a measure that sees only registered activity describes a different economy from the one people live in."),

 ("An average says nothing about spread",
  "EK SPS-7.C.1 names income distribution alongside Gross National Income per capita, and listing both means neither substitutes for the other. A mean is a single number about a whole distribution, and a distribution is what it is a single number about."),

 ("It falls as incomes, education and access to health care rise",
  "EK SPS-7.C.1 names fertility rates among the measures of social and economic development. What makes a demographic figure a development indicator is that it responds reliably to the same changes development consists of, which is the logic of the demographic transition model."),

 ("nutrition, clean water, sanitation and health care at once",
  "EK SPS-7.C.1 names infant mortality rates among the measures of social and economic development. A measure sensitive to several conditions at once is a good summary indicator precisely because a failure in any one of them shows up in it."),

 ("Whether people can actually reach and afford care",
  "EK SPS-7.C.1 names access to health care among the measures of development, and access is a relationship rather than a stock. A country can have practitioners concentrated where a minority lives and still leave most people without reachable care."),

 ("the mix between the two sources indicates how that energy is obtained",
  "EK SPS-7.C.1 names use of fossil fuels AND renewable energy among the measures. Naming both makes it two measures in one: how much energy a population commands, and what kind, which are separate facts about a country."),

 ("the precondition for most further schooling and most skilled work",
  "EK SPS-7.C.1 names literacy rates among the measures of social and economic development. Reading is the gateway skill, conditioning access to further training, to information and to most work above the least skilled, which is why the rate summarizes more than schooling."),

 ("Reproductive health, indices of empowerment, and labour-market participation",
  "EK SPS-7.C.2 says measures of gender inequality, such as the Gender Inequality Index, include reproductive health, indices of empowerment and labor-market participation. The rejected options are drawn from EK SPS-7.C.1's general list of development measures."),

 ("a country can score well on income or literacy overall while a large gap persists",
  "EK SPS-7.C.2 names measures of gender inequality as a category of their own alongside EK SPS-7.C.1's general measures. An average conceals the composition of the population it averages, which is the same reason income distribution is listed separately from income per person."),

 ("composite measure used to show spatial variation among states",
  "EK SPS-7.C.3 states that the Human Development Index is a composite measure used to show spatial variation among states in levels of development. Both halves matter: it combines several indicators, and its purpose is comparison across places."),

 ("A long and healthy life, knowledge, and a decent standard of living",
  "EK SPS-7.C.3 calls the index a composite measure without listing its parts, and these are its conventional three dimensions. The rejected first alternative is EK SPS-7.C.2's list for the gender inequality measure, which is the composite most easily confused with this one."),

 ("conceals which of the underlying components is high or low",
  "EK SPS-7.C.3 describes the index as a COMPOSITE measure showing spatial variation among states, and suggested skill 3.F asks for the limitations of data. Two countries can reach the same composite score by entirely different routes, which a single number cannot report."),

 ("while social measures record the conditions of people's lives",
  "Learning objective SPS-7.C asks students to describe SOCIAL AND ECONOMIC measures of development, and EK SPS-7.C.1's list contains both kinds. Naming both is a claim that development is not exhausted by output, which is also why the composite index combines them."),

 ("How the income is shared",
  "EK SPS-7.C.1 lists income distribution as a measure separate from Gross National Income per capita, and suggested skill 3.F asks for the limitations of the data provided. A mean is compatible with any distribution, which is exactly why the framework lists both."),

 ("Unregistered work is not captured by the systems that produce national accounts",
  "EK SPS-7.C.1 names sectoral structure BOTH FORMAL AND INFORMAL among its measures, and suggested skill 3.F asks for the limitations of data. What is unregistered is largely uncounted, so recorded and actual output diverge by more where the informal share is larger."),

 ("an average over regions that may differ enormously",
  "EK SPS-7.C.3 says the Human Development Index shows spatial variation AMONG STATES, which is a comparison at one scale. Suggested skill 3.F asks for the limitations of the data, and a figure computed for a whole state conceals whatever variation exists inside it."),

 ("different intervals with different definitions and different reliability",
  "Suggested skill 3.F for this topic is explaining possible limitations of the data provided. A cross-country table looks uniform on the page and is assembled from national collections differing in date, method and coverage, which is a limitation of the comparison rather than of any one figure."),

 ("Unpaid work in households and the depletion of natural resources",
  "Suggested skill 3.F asks for the limitations of the data, and EK SPS-7.C.1's list is built around recorded output and recorded social outcomes. Work never paid for and resources drawn down without being priced fall outside what those systems count."),

 ("Infant mortality rate, matched to the effect of nutrition, water, sanitation and health care",
  "EK SPS-7.C.1 lists these measures for different things, and the list is useful only if the measures are kept apart. Only one pairing here matches a measure to what it actually captures; each of the others attaches a measure to the subject of a different one on the same list."),

 ("infant mortality rises from 4 to 68",
  "Recomputed from the record: income falls from 48,000 to 1,100, literacy from 99 to 51 percent and the composite index from 0.92 to 0.42, while infant mortality rises from 4 to 68 at every step. EK SPS-7.C.1 names all four kinds of measure, and their agreeing is what makes any one usable as a summary.",
  ),

 ("about 21 times the poorest fifth's share in one country",
  "Recomputed from the record: both countries record 14,000 per person, and the ratio of the richest fifth's share to the poorest fifth's is about 20.7 in one and about 4.2 in the other. The verifier asserts the two incomes are EQUAL, since the item exists only because the averages match.",
  ),

 ("All three components fall together",
  "Recomputed from the record: life expectancy falls from 82 to 62, expected schooling from 17.5 to 9.8 years, income from 46,000 to 2,900 and the composite index from 0.93 to 0.53. EK SPS-7.C.3 calls the index a composite measure of spatial variation among states, and a case where every component agrees is the easy one.",
  ),

 ("the same score by different combinations of the components",
  "EK SPS-7.C.3 describes the Human Development Index as a COMPOSITE measure, and suggested skill 3.F asks for the limitations of the data provided. Compression is what makes a composite comparable and it is the same operation that discards which component is weak."),

 ("gender inequality is measured separately by its own components",
  "EK SPS-7.C.1 supplies the general measures, EK SPS-7.C.2 the gender inequality components and EK SPS-7.C.3 the composite index, while suggested skill 3.F makes limitations part of the topic. Each rejected summary reduces the three statements to one or removes the qualification the skill supplies."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"7.3 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"7.3 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_measures_agree,
    27: q27_same_mean_different_spread,
    28: q28_components_agree,
}

geo_check.check(g7_3, ANCHORS, TABLE_NOTES)
