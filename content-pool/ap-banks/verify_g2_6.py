"""Key audit for AP HUMAN GEOGRAPHY 2.6 Malthusian Theory.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. This topic has exactly one essential-knowledge statement:

    IMP-2.B.3  Malthusian theory and its critiques are used to analyze
               population change and its consequences.

Note the four words that decide the shape of the module: AND ITS CRITIQUES. The
CED puts them inside the required content, so a module teaching only the theory
would be teaching half the topic. Items 1-5, 11, 12, 18, 19 and 23 are on the
argument; items 6-10, 13, 15, 16, 17, 20, 21, 22, 24 and every table item from
27 on are on the critiques. That balance is the citation being obeyed rather
than a stylistic choice.

WHAT THE CITATION CANNOT SUPPORT. The statement names the theory and does not
describe it, so no key here can rest on "the CED says Malthus said". Every
description is set out in the module header and repeated in the claims below:
geometric against arithmetic growth, positive checks acting on mortality,
preventive checks acting on fertility, and the four standard critiques
(Boserup's induced intensification, the empirical record of yields, the
fertility decline, and famine as a distribution failure). Neo-Malthusianism is
handled as a RESTATEMENT of the argument for non-food resources, not as a
refutation, which is the distinction item 17 tests.

THE TERMINOLOGY TRAP. "Positive check" means acting on the death rate, not
being desirable. Items 3, 4, 5 and 19 all turn on it and item 5 asks about it
directly, because it is the single most reliable misreading in the topic.

The five table items (26-30) are the computational gate:

  26  geometric against arithmetic in bare numbers -- the recompute asserts one
      column really doubles and the other really adds a constant
  27  cereal per person RISES while population more than doubles, which is the
      empirical critique in two rows
  28  output nearly triples while cultivated area rises 10 percent, so yield
      did the work -- the recompute asserts the area contribution is small
  29  national availability moves under 2 percent while famine deaths go from
      zero to 180,000 and back, which is the distribution critique in data
  30  fertility falls monotonically as income rises, with no reversal anywhere

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting. Item 24 is a NOT question and its key is the
one option that is not a recognized critique; the claim says so explicitly,
because a negative stem is exactly where a hurried reader mis-keys.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g2_6


def q26_geometric_vs_arithmetic(table):
    """One column doubles, the other adds a constant, and the gap opens."""
    pop = numcol(table, "Population (millions)")
    food = numcol(table, "Food supply (millions fed)")
    assert pop[0] == food[0], "the two series must start equal"
    # Population multiplies by a constant factor.
    ratios = [pop[i + 1] / pop[i] for i in range(len(pop) - 1)]
    assert len(set(ratios)) == 1 and ratios[0] == 2, ratios
    # Food adds a constant increment.
    diffs = [food[i + 1] - food[i] for i in range(len(food) - 1)]
    assert len(set(diffs)) == 1 and diffs[0] == 1, diffs
    share = food[-1] / pop[-1]
    assert share < 0.2, share
    assert pop[-1] == 32 and food[-1] == 6, (pop[-1], food[-1])
    return "fewer than one person in five"


def q27_output_per_person(table):
    """Cereal per person rises even though population more than doubles."""
    rows = sorted((num(rowdict(table, r)["Year"]),
                   num(rowdict(table, r)["Population (billions)"]),
                   num(rowdict(table, r)["Cereal production (million tonnes)"]))
                  for r in table["rows"])
    # million tonnes is 1e9 kg and billions of people is 1e9 people, so the
    # two factors cancel and tonnes-per-billion is already kg per person.
    per = [t / p for _, p, t in rows]
    assert abs(per[0] - 300) < 1, per
    assert 380 < per[1] < 390, per
    assert per[1] > per[0], per
    pop_growth = rows[1][1] / rows[0][1]
    out_growth = rows[1][2] / rows[0][2]
    assert pop_growth > 2 and out_growth > pop_growth, (pop_growth, out_growth)
    return "300 to about 385 kilograms"


def q28_yield_not_area(table):
    """Output nearly triples; almost none of it comes from more land."""
    rows = sorted((num(rowdict(table, r)["Year"]),
                   num(rowdict(table, r)["Cultivated area (million hectares)"]),
                   num(rowdict(table, r)["Yield (tonnes per hectare)"]))
                  for r in table["rows"])
    output = [a * y for _, a, y in rows]
    assert abs(output[0] - 30) < 1e-9 and abs(output[-1] - 88) < 1e-9, output
    area_growth = rows[-1][1] / rows[0][1]
    yield_growth = rows[-1][2] / rows[0][2]
    assert abs(area_growth - 1.1) < 1e-9, area_growth
    assert yield_growth > 2.5, yield_growth
    # Area contributes far less than yield to the total increase.
    assert (area_growth - 1) * 5 < (yield_growth - 1), (area_growth, yield_growth)
    return "30 to 88 million tonnes"


def q29_distribution_failure(table):
    """National availability barely moves while famine deaths appear and recede."""
    rows = [(rowdict(table, r)["Year"],
             num(rowdict(table, r)["National food available (kcal per person per day)"]),
             num(rowdict(table, r)["Famine deaths in Region Q"]))
            for r in table["rows"]]
    kcal = [k for _, k, _ in rows]
    deaths = [d for _, _, d in rows]
    spread = (max(kcal) - min(kcal)) / max(kcal)
    assert spread < 0.02, spread
    assert deaths[0] == 0 and deaths[1] == 180000, deaths
    assert deaths[2] < deaths[1], deaths
    # The supply column must NOT track the deaths column, or the item collapses.
    assert kcal.index(min(kcal)) == deaths.index(max(deaths)) and spread < 0.02, \
        "the small dip coincides with the peak, so the claim must rest on its size"
    return "failure was in access within one region"


def q30_fertility_and_income(table):
    """Fertility falls monotonically as income rises; no reversal anywhere."""
    rows = sorted((num(rowdict(table, r)["GDP per capita (US$)"]),
                   num(rowdict(table, r)["Total fertility rate"]))
                  for r in table["rows"])
    tfr = [t for _, t in rows]
    assert all(tfr[i] > tfr[i + 1] for i in range(len(tfr) - 1)), tfr
    assert tfr[0] == 5.4 and tfr[-1] == 1.5, tfr
    incomes = [g for g, _ in rows]
    assert incomes[-1] / incomes[0] > 30, incomes
    return "fertility falls steadily as incomes rise"


CLAIMS = [
 ("grow by multiplication while food supply grows by addition",
  "EK IMP-2.B.3 names Malthusian theory as a theory of population change and its consequences without describing it, so this key rests on the standard account: geometric population against arithmetic subsistence. The mismatch between the two kinds of growth guarantees a crossing however large the starting surplus is."),

 ("Population is 16 million while food supports 5 million",
  "Four doublings take a million to sixteen million while four equal additions take it to five, so food per person falls to five sixteenths of its original level. That divergence after a single century is the whole force of the argument, and it follows from the shapes of the two series rather than from any particular number."),

 ("Famine, which raises the death rate",
  "Malthus divides the checks by which vital rate they act on: a positive check raises mortality and a preventive check lowers fertility. The word positive marks the direction of the effect on deaths and carries no judgement that the outcome is desirable."),

 ("Postponing marriage to a later age",
  "A preventive check operates on the birth rate before a birth occurs, and later marriage shortens the years available for childbearing. Every other option listed reduces a population by killing people, which places it among the positive checks instead."),

 ("acting on the death rate rather than to being desirable",
  "The terminology names a mechanism rather than a moral character, and Malthus regarded the preventive checks as the humane alternative to the positive ones. This is the single most reliable misreading in the topic, which is why the item asks about it directly."),

 ("population pressure drives agricultural innovation",
  "EK IMP-2.B.3 requires the critiques as well as the theory, and Boserup's reverses the causation. Malthus treats food supply as an external ceiling, while Boserup treats it as a variable responding to the number of mouths, since more people both need and supply the labour intensification requires."),

 ("Mechanization, fertilizer, irrigation, and high-yielding crop varieties",
  "EK IMP-2.B.3's critiques rest first on the empirical record: output per hectare rose in ways the arithmetic premise did not allow for. Famines have continued to occur, but not because global production failed to keep pace with global population."),

 ("since birth rates fall on their own as societies develop",
  "The argument requires population to keep multiplying unless something stops it, and a voluntary fertility decline is a brake Malthus did not foresee. Households in urbanized, educated, low-mortality societies choose fewer children with no check applied to them at all."),

 ("failure of distribution, purchasing power, and politics",
  "Malthus locates famine in a shortage of total production, but a famine inside a country holding a surplus is a failure of access. Whether people can obtain food depends on income, entitlements, transport and political will, none of which appears as a term in his model."),

 ("beyond food to water, soil, fisheries, energy, and the atmosphere",
  "EK IMP-2.B.3 makes both the theory and its critiques examinable, and the neo-Malthusian position concedes that food production outran the original prediction while restating the limits argument for other resources. The structure of the claim is unchanged and only the binding constraint has moved."),

 ("Cultivated area and yields have stopped rising while population continues to grow",
  "A Malthusian reading needs the supply side stalled while the demand side keeps rising, which is exactly the combination described. Every other option shows one of the two curves moving in the direction the argument says it cannot."),

 ("more children to survive and be born",
  "Inside his framework any improvement in subsistence translates into more surviving people rather than into a lasting rise in living standards. Whether that is true is one of the critiques the CED requires, but the question asks what follows within the theory itself."),

 ("calories available per person rose while population more than doubled",
  "The premise is that subsistence cannot keep pace with a multiplying population, so a period in which supply per person ROSE while population doubled contradicts it directly. That the increase came mostly from yield rather than from new land sharpens the point."),

 ("remains the question behind debates about water, soil, and climate",
  "EK IMP-2.B.3 pairs the theory with its critiques precisely because the pair is the analytical tool. The specific arithmetic was wrong, while the question of whether a growing population meets a resource ceiling is asked again for every resource later in the course."),

 ("population pressure has induced more intensive use of the same land",
  "EK IMP-2.B.3 requires the critiques, and Boserup's is that necessity drives intensification. Terracing, shorter fallows and double cropping each raise output per hectare at the cost of more labour, which a larger population is exactly what supplies."),

 ("Malthus treats technology as fixed and food as the limit",
  "The disagreement is precisely about whether the food-supply curve is exogenous. Holding it fixed produces an inevitable crossing, while letting it respond to the demand for food produces intensification instead of catastrophe."),

 ("binding limit named is a resource other than food",
  "Malthus's constraint is subsistence specifically, and the later restatement moves the constraint to whichever resource is scarcest. Naming water rather than food is the whole of the difference, since the reasoning is structurally identical."),

 ("rise by a roughly constant amount in each period",
  "An arithmetic series adds a fixed increment while a geometric series multiplies by a fixed factor, and the two diverge without limit however small the multiplier. That structural divergence, not any particular figure, is what makes the conclusion inevitable inside the model."),

 ("Mortality rising in a region during a prolonged drought",
  "A positive check operates through deaths, and famine following crop failure is the case Malthus named first. Every other option lowers the birth rate, which places it among the preventive checks instead."),

 ("which makes food growth geometric too",
  "If output also multiplies rather than adds, the two curves need not cross at all, so the conclusion fails rather than merely being postponed. That is a structural error in a premise, not a mistaken estimate of a coefficient."),

 ("from food to environmental sinks and services",
  "EK IMP-2.B.3 keeps the theory and its critiques together as tools for analyzing the consequences of population change. What survived the critiques is the form of the question, and the resources now argued over are ones nobody priced in 1798."),

 ("Yields per hectare rose sharply",
  "Most of the post-1950 increase came from getting more out of each hectare rather than from ploughing new ground, which is the precise sense in which technology broke the arithmetic premise. Cultivated area grew comparatively little over the same period."),

 ("fallen by about a fifth",
  "Output at 1.6 times divided by population at 2 times leaves 0.8 of the original amount per person, a fall of 20 percent. A rising total with a falling per-person figure is exactly the situation the argument is about, which is why the total alone settles nothing."),

 ("population has never grown in any period of history",
  "This is a NOT question and the key is the one option that is not a recognized critique. EK IMP-2.B.3 requires the critiques, and the four genuine ones each attack a premise or a prediction, whereas denying that population has ever grown contradicts the evidence rather than the theory."),

 ("raising output, importing food, or reducing fertility",
  "Using the theory analytically means identifying the gap it describes and acting on the terms it names, which is what EK IMP-2.B.3's pairing with the critiques makes possible. The fatalistic reading treats the positive check as a policy, which the critiques and ordinary decency both reject."),

 ("fewer than one person in five",
  "Recomputed from the table: the population column doubles at every step while the food column rises by exactly one each time, so at the last interval six million can be fed out of thirty-two million people. The verifier asserts the two growth patterns really are geometric and arithmetic rather than merely looking so.",
  q26_geometric_vs_arithmetic),

 ("300 to about 385 kilograms",
  "Recomputed from the table: 900 million tonnes among three billion people is 300 kilograms each, and 3,000 million tonnes among 7.8 billion is about 385. Population grew 2.6-fold against production's 3.3-fold, which is the empirical critique of the arithmetic premise in two rows.",
  q27_output_per_person),

 ("30 to 88 million tonnes",
  "Recomputed from the table: multiplying area by yield gives 30, 58.8 and 88 million tonnes, an increase of 193 percent, while cultivated area rose only ten percent. The verifier asserts the area contribution is a small fraction of the yield contribution, which is the mechanism the arithmetic premise excluded.",
  q28_yield_not_area),

 ("failure was in access within one region",
  "Recomputed from the table: national availability moves within 40 kilocalories across the three years, under two percent, while famine deaths run from zero to 180,000 and then fall. A national supply that never materially fell cannot be the cause of a regional catastrophe, which is the distribution critique stated in data.",
  q29_distribution_failure),

 ("fertility falls steadily as incomes rise",
  "Recomputed from the table: fertility falls from 5.4 to 1.5 as income rises from 1,100 to 42,000 dollars, with no reversal at any step. A population that limits its own growth as it develops removes the premise that only an external check can stop it.",
  q30_fertility_and_income),
]

hg_check.check(g2_6, CLAIMS, per_topic=30, n_choices=5)
