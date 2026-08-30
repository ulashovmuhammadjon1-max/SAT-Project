"""Key audit for AP HUMAN GEOGRAPHY 2.3 Population Composition.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. PSO-2.E and PSO-2.F print two essential-knowledge statements
between them:

    PSO-2.E.1  Patterns of age structure and sex ratio vary across different
               regions and may be mapped and analyzed at different scales.
    PSO-2.F.1  Population pyramids are used to assess population growth and
               decline and to predict markets for goods and services.

PSO-2.F.1 authorizes TWO uses, and the second -- predicting markets for goods
and services -- is stated as plainly as the first. Items 9, 10, 17, 18, 22, 27
and 28 rest on it and cite it, which is legitimate precisely because the CED
says it rather than because it sounds sensible.

Items citing PSO-2.E.1 (composition varies regionally and by scale): 4, 5, 7, 8,
13, 19, 20, 21, 23, 26, 30.
Items citing PSO-2.F.1 (pyramid as an instrument): 1, 2, 9, 10, 16, 17, 18, 22,
27, 28.
Items citing neither: 3, 6, 11, 12, 14, 15, 24, 25, 29. Their keys rest on
arithmetic the CED does not state -- that a base narrower than the cohorts above
it guarantees eventual decline, that a small male surplus at birth is erased by
higher male mortality, that a defect confined to one cohort in both sexes dates
a short event, that a large parent cohort produces an echo at unchanged
fertility. Each is argued in the claim rather than dressed in a code.

WHY THERE ARE NO PYRAMID IMAGES. This bank carries tables and nothing else, so
no stem here says "the pyramid shown". Every item that needs a pyramid is given
one as a real cohort table, which holds the same two variables in the same
structure. That is a deliberate design choice, not a gap: CLAUDE.md's standing
rule is that a stem may never describe a figure in prose in place of supplying
it, and a cohort table supplies it.

The five table items (26-30) are the computational gate:

  26  the sex ratio is computed from the totals, and the recompute asserts the
      imbalance is CONCENTRATED in the working ages rather than spread evenly,
      which is what separates the key from its nearest distractor
  27  the largest cohort is identified and advanced ten years, and the recompute
      confirms the band it moves into is currently smaller
  28  both percentage columns must sum to 100, which is why nothing about total
      population can be read from the table
  29  the deficient cohort is less than half of BOTH its neighbours while every
      other step in the series is small
  30  the first band below 100 is found by scanning in order, and the sequence
      is asserted to be monotonic so that no jump could be read as an edge

REVIEW NOTE, written while building the tables. Item 26's keyed choice first
said the sex ratio was "about 190"; recomputing from the cells gives 185.3, and
both the key and its paired distractor were corrected to 185 before this file
was written. Item 27 carried a distractor asserting the 10-19 cohort was the
largest in the table, which it is not; it was rewritten so its premise is true
and only its inference is wrong. No key was changed.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g2_3


def q26_sex_ratio(table):
    """Overall sex ratio, and the concentration of the imbalance by age."""
    males, females, by_band = 0.0, 0.0, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        m, f = num(d["Males"]), num(d["Females"])
        males += m
        females += f
        by_band[d["Age group"]] = 100 * m / f
    overall = 100 * males / females
    assert males == 10100 and females == 5450, (males, females)
    assert 184 < overall < 187, overall
    assert round(overall) == 185, overall
    # The imbalance must be CONCENTRATED, not spread: one band far above the
    # rest, and the youngest and oldest bands near balance or female-majority.
    assert by_band["25-44"] > 300, by_band
    assert 100 <= by_band["0-14"] < 110, by_band
    assert by_band["65+"] < 100, by_band
    return "about 185"


def q27_largest_cohort(table):
    """The biggest cohort, and the band it will occupy in ten years."""
    sizes = {rowdict(table, r)["Age group"]: num(rowdict(table, r)["Population (millions)"])
             for r in table["rows"]}
    biggest = max(sizes, key=sizes.get)
    assert biggest == "50-59", sizes
    assert sizes["50-59"] == 7.9, sizes
    # Ten years on, that cohort occupies 60-69, which is currently smaller.
    assert sizes["60-69"] < sizes["50-59"], sizes
    assert sizes["60-69"] == 5.0, sizes
    # The distractors name cohorts that are genuinely not the largest.
    for band in ("0-9", "10-19", "20-29"):
        assert sizes[band] < sizes[biggest], sizes
    return "7.9 million now aged 50-59"


def q28_percentage_columns(table):
    """Two percentage columns, both summing to 100, so totals are unreadable."""
    a = numcol(table, "Country A (% of population)")
    b = numcol(table, "Country B (% of population)")
    assert sum(a) == 100 and sum(b) == 100, (sum(a), sum(b))
    bands = column(table, "Age group")
    ia, io = bands.index("0-14"), bands.index("65+")
    assert a[ia] > 2 * b[ia], (a[ia], b[ia])
    assert b[io] > 5 * a[io], (a[io], b[io])
    return "rising demand for schooling"


def q29_crisis_cohort(table):
    """One cohort under half of both neighbours; every other step is small."""
    sizes = [(rowdict(table, r)["Years of birth"],
              num(rowdict(table, r)["Cohort size (thousands)"]))
             for r in table["rows"]]
    vals = [v for _, v in sizes]
    i = min(range(len(vals)), key=lambda k: vals[k])
    assert sizes[i][0] == "1940-1944", sizes
    assert 0 < i < len(vals) - 1, "the deficient cohort must have neighbours"
    assert vals[i] * 2 < vals[i - 1] and vals[i] * 2 < vals[i + 1], vals
    # Every other adjacent step must be small, so only one cohort stands out.
    others = [abs(vals[k] - vals[k + 1]) for k in range(len(vals) - 1)
              if k not in (i - 1, i)]
    assert max(others) < 100, others
    return "less than half the size"


def q30_ratio_crossover(table):
    """The first age band whose sex ratio falls below 100, found by scanning."""
    bands = [(rowdict(table, r)["Age band"], num(rowdict(table, r)["Males per 100 females"]))
             for r in table["rows"]]
    vals = [v for _, v in bands]
    assert all(vals[i] > vals[i + 1] for i in range(len(vals) - 1)), f"not monotonic: {vals}"
    first_below = next(name for name, v in bands if v < 100)
    assert first_below == "45-59", bands
    assert vals[0] > 100, vals
    return "At 45-59"


CLAIMS = [
 ("size of each age cohort, divided by sex",
  "EK PSO-2.F.1 makes the pyramid the standard instrument for assessing growth and decline, and it does that by displaying composition: how many people fall in each age band and how each band divides between the sexes at one moment."),

 ("High fertility together with high mortality",
  "EK PSO-2.F.1 makes the pyramid a tool for assessing growth and decline. Each cohort being larger than the one above it means births are rising, and that momentum carries growth forward even if fertility later falls."),

 ("below the level needed to replace the parent generation",
  "A base smaller than the cohorts above it means each generation is being replaced by a smaller one. Growth may continue while the large middle cohorts survive, but the structure guarantees decline once they age out, which the CED does not state and so is argued here."),

 ("number of males per 100 females",
  "EK PSO-2.E.1 names sex ratio as an element of population composition without defining it, and the standard convention is males per 100 females. A value above 100 marks a male-majority population and one below 100 a female-majority one."),

 ("in-migration of working-age men",
  "EK PSO-2.E.1 says sex ratio patterns vary across regions, and labour migration is the mechanism producing the most extreme national values. Births and deaths cannot generate a two-to-one imbalance, so only selective movement can move a whole country's ratio that far."),

 ("more boys are born than girls, and women live longer",
  "The pattern comes from two independent facts pulling in opposite directions across the life course: a small male surplus at birth and a female advantage in survival. The crossover is the age at which accumulated mortality has erased the initial excess."),

 ("Out-migration of young adults",
  "EK PSO-2.E.1 allows age structure to be analyzed below the national scale, and at county scale migration reshapes composition faster than fertility or mortality can. A notch confined to the working ages while children remain is what adults leaving looks like."),

 ("a large university",
  "EK PSO-2.E.1 states that age structure may be mapped and analyzed at different scales, and at district scale a single institution can dominate the profile. A cohort confined to a narrow band with almost nothing above or below it is a student population."),

 ("Primary schools, pediatric care",
  "EK PSO-2.F.1 states that population pyramids are used to predict markets for goods and services. A wide base is a large cohort of children, and the services a child needs arrive on a schedule the pyramid makes visible years in advance."),

 ("Geriatric health care",
  "EK PSO-2.F.1 names market prediction as a use of the pyramid. Advancing the largest cohorts fifteen years puts them in the ages where health, care and pension needs peak, which is a demand forecast made from composition alone."),

 ("war, famine, or epidemic",
  "A defect confined to one cohort and affecting both sexes equally points to a short dated event rather than a trend, since a trend would deform every cohort after it began. Both sexes being affected rules out any cause specific to one of them."),

 ("An echo effect",
  "Births are the fertility rate multiplied by the number of women of childbearing age, so an unusually large parent cohort produces many births without any rise in the rate. The echo is smaller than the original boom because fertility itself is lower."),

 ("a national profile is an average of very different local ones",
  "EK PSO-2.E.1 states that age structure and sex ratio may be mapped and analyzed at different scales. Internal migration moves young adults between parts of a country without changing the national total, so the national picture conceals two opposite local ones."),

 ("bulge in the 25-44 cohorts combined with a narrow base",
  "Fertility change reshapes a pyramid from the bottom upward over decades, while migration inserts people directly into the ages at which they move. Working-age adults arriving without children produce exactly this combination, which no fertility change could."),

 ("past events remain visible in the structure for decades",
  "A cohort is a group born together that thereafter only shrinks or gains by migration, so whatever happened to it stays legible as a notch or a bulge. Reading a pyramid upward is reading backward through the events each cohort lived through."),

 ("known years before it reaches school or working age",
  "EK PSO-2.F.1 names assessing growth or decline and predicting markets as the pyramid's two uses, and both work because cohorts age predictably. A child counted today needs a secondary place in a decade, which a headline total does not tell a planner."),

 ("one weighted toward education and the other toward health and pensions",
  "EK PSO-2.F.1 makes the pyramid a tool for predicting demand for goods and services, and these two compositions place their people in different service-consuming stages of life. Equal totals therefore imply nothing whatever about equal budgets."),

 ("Predicting markets for goods and services",
  "This restates the second use EK PSO-2.F.1 assigns to population pyramids. Cohort size is the number of potential buyers in the ages at which a product is used, which is precisely what a market forecast rests on."),

 ("only selective movement can shift a local ratio sharply",
  "EK PSO-2.E.1 places sex ratio among the compositional patterns analyzable at different scales. Because the sexes are born and die in roughly similar numbers, a mining camp, a garrison or a garment town can reach an extreme ratio only by attracting one sex."),

 ("a single metropolitan pyramid would average away the differences",
  "EK PSO-2.E.1 states that composition may be mapped and analyzed at different scales, and the CED's own sample activity for this topic builds pyramids for subnational units. Averaging a student district with a retirement town describes neither of them."),

 ("share of the population living in cities",
  "EK PSO-2.E.1 names age structure and sex ratio as the elements of composition, and a pyramid is built from exactly those two variables. Urban residence is a separate attribute that would need its own cross-tabulation to appear anywhere on the chart."),

 ("treatments used mainly in later life",
  "EK PSO-2.F.1 authorizes the pyramid as a tool for predicting markets, and the prediction is made by advancing a known cohort through the ages at which a product is consumed. Nothing else in the structure is needed for that inference."),

 ("Composition describes what a population is made of by age and sex",
  "EK PSO-2.E.1 defines composition through age structure and sex ratio, which are properties of the people themselves, while distribution is their arrangement across territory. Two places with identical compositions can have entirely different distributions, and the reverse holds too."),

 ("Fertility close to replacement and low mortality until old age",
  "Cohorts of similar size mean each generation is replaced by one about as large, and a taper beginning only in old age means few people are lost before then. That combination is stability rather than growth or decline."),

 ("high fertility with high mortality or from low fertility with low mortality",
  "A rate of natural increase is a difference between two other rates, so the same value can be reached from many combinations of them. High births with high deaths concentrates a population in the young ages while low births with low deaths spreads it toward the old."),

 ("imbalance concentrated in the 25-44 group",
  "Recomputed from the table: 10,100 males against 5,450 females is 185 per 100, and the 25-44 band alone runs above 300 while the youngest band is near balance and the oldest is female-majority. The verifier asserts that concentration separately, since it is what distinguishes the key from the evenly-spread distractor.",
  q26_sex_ratio),

 ("7.9 million now aged 50-59",
  "Recomputed from the table: the largest cohort is the 50-59 group at 7.9 million, and in ten years it occupies the 60-69 band, replacing a group of 5.0 million. Advancing a known cohort by a known number of years is exactly the market prediction EK PSO-2.F.1 authorizes.",
  q27_largest_cohort),

 ("rising demand for schooling",
  "Recomputed from the table: both columns sum to 100 percent, so the comparison is about shape rather than size, with 42 percent under 15 against 16 and 3 percent over 65 against 21. Percentages carry no information about totals, which is why nothing about which country has more people can be read here.",
  q28_percentage_columns),

 ("less than half the size",
  "Recomputed from the table: one cohort at 410 thousand sits between neighbours of 845 and 870, while every other adjacent step in the series is under 100 thousand. A defect confined to a single span with normal cohorts on both sides dates a brief event rather than a trend.",
  q29_crisis_cohort),

 ("At 45-59",
  "Recomputed from the table: the sequence runs 105, 104, 102, 99, 91 and 72, so the first value under 100 appears in the 45-59 band and the decline continues from there. The verifier confirms the series is monotonic, so no jump anywhere could be mistaken for a sharp crossover.",
  q30_ratio_crossover),
]

hg_check.check(g2_3, CLAIMS, per_topic=30, n_choices=5)
