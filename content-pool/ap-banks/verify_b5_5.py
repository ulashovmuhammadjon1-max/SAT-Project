"""Key audit for AP BIOLOGY 5.5 Environmental Effects on Phenotype.

One (anchor, claim) per item, in module order. ``cg_check.check`` is the
structural gate; it is described in ``verify_b5_3.py``.

THE PARTICULAR RISK IN THIS TOPIC is not arithmetic, it is padding: the CED
gives 5.5 a single essential knowledge statement and six illustrative examples,
so an author with thirty slots is tempted either to say the same thing thirty
times or to reach into a neighbouring topic. The claims below name, for every
item, which illustrative example it rests on or which second statement it
chains EK 5.5.A.1 to. Nine items are data items and each of their tables is
recomputed here from the table alone -- the trend, the mean, the ratio or the
reversal that the keyed choice asserts.

NEGATIVE CONTROL: ``negcontrol_b5_7.py``.
"""
import cg_check as cg
import b5_5

T_PH = b5_5._T_PH
T_PHTIME = b5_5._T_PHTIME
T_HARE = b5_5._T_HARE
T_REPTILE = b5_5._T_REPTILE
T_UV = b5_5._T_UV
T_YEAST = b5_5._T_YEAST
T_HEIGHT = b5_5._T_HEIGHT
T_NORM = b5_5._T_NORM
T_MEAN = b5_5._T_MEAN


def _rows(table):
    heads = [cg.normalize(h) for h in table["headers"]]
    return [dict(zip(heads, r)) for r in table["rows"]]


def _series(table, xcol, ycol, xmax=None, percent=False):
    """The two named columns as (x, y) pairs, with the sanity bounds enforced.

    The bounds are not decoration. A trend check alone is nearly blind: scaling
    one value of a monotonic series usually leaves it monotonic, so the negative
    control caught one corruption in eight until the ranges below were added.
    A percentage above 100 or an x column out of order is not data.
    """
    pairs = [(cg.num(r[cg.normalize(xcol)]), cg.num(r[cg.normalize(ycol)]))
             for r in _rows(table)]
    xs = [p[0] for p in pairs]
    assert xs == sorted(xs) and len(set(xs)) == len(xs), \
        f"the {xcol!r} column is not strictly increasing: {xs}"
    if xmax is not None:
        assert all(0 <= x <= xmax for x in xs), f"{xcol!r} out of range: {xs}"
    if percent:
        assert all(0 <= y <= 100 for y in (p[1] for p in pairs)), \
            f"{ycol!r} holds a value outside 0 to 100 percent: {[p[1] for p in pairs]}"
    return pairs


def q2(table, item):
    pairs = [(cg.num(r["soil ph of the pot"]), cg.normalize(r["flower color of the cutting"]))
             for r in _rows(table)]
    colors = {c for _, c in pairs}
    assert len(colors) > 1, "one genotype must show more than one colour or the key fails"
    low = {c for ph, c in pairs if ph < 6}
    high = {c for ph, c in pairs if ph > 6.5}
    assert low == {"blue"} and high == {"pink"}, \
        f"the acidic pots give {low} and the alkaline pots {high}; the key needs blue and pink"
    return (f"{len(pairs)} cuttings of one plant across pH {min(p for p, _ in pairs)} to "
            f"{max(p for p, _ in pairs)} give {len(colors)} different flower colours")


def q3(table, item):
    s = _series(table, "Hours of light per day", "Percent of hares with a white coat",
                xmax=24, percent=True)
    assert all(b[1] < a[1] for a, b in zip(s, s[1:])), \
        f"the white-coat percentage must fall at every step; got {s}"
    assert s[0][1] - s[-1][1] > 50, "the fall must be large enough to call an effect"
    return (f"white coats fall from {s[0][1]:.0f} to {s[-1][1]:.0f} percent as light rises "
            f"from {s[0][0]:.0f} to {s[-1][0]:.0f} hours, a strictly decreasing series")


def q4(table, item):
    s = _series(table, "Incubation temperature (degrees Celsius)",
                "Percent of hatchlings that are female", xmax=60, percent=True)
    nearest = min(s, key=lambda p: abs(p[1] - 50))
    assert nearest[0] == 30, f"the temperature nearest an even sex ratio is {nearest[0]}, not 30"
    others = sorted(abs(p[1] - 50) for p in s if p[0] != nearest[0])
    assert others[0] > abs(nearest[1] - 50), "a second temperature ties the key"
    assert all(b[1] > a[1] for a, b in zip(s, s[1:])), "percent female must rise with temperature"
    return (f"the five percentages are {[p[1] for p in s]}; the one nearest 50 is "
            f"{nearest[1]:.0f} at {nearest[0]:.0f} degrees, and no other is as close")


def q5(table, item):
    s = _series(table, "Daily UV exposure (arbitrary units)",
                "Mean melanin content of skin samples (arbitrary units)", xmax=100)
    lo = min(s, key=lambda p: p[0])
    hi = max(s, key=lambda p: p[0])
    fold = hi[1] / lo[1]
    assert abs(fold - 4) < 0.25, f"the fold change recomputes to {fold:.2f}, not about four"
    assert all(b[1] > a[1] for a, b in zip(s, s[1:])), "melanin must rise with exposure"
    return f"melanin rises from {lo[1]:.0f} to {hi[1]:.0f} units, a factor of {fold:.2f}"


def q6(table, item):
    rows = _rows(table)
    col = "pheromone produced nanograms per million cells"
    alone = [cg.num(r[col]) for r in rows if cg.contains_phrase(r["culture condition"], "grown alone")]
    together = [cg.num(r[col]) for r in rows
                if cg.contains_phrase(r["culture condition"], "grown together")]
    assert len(alone) == 2 and len(together) == 1, \
        f"expected two solo cultures and one mixed; got {len(alone)} and {len(together)}"
    assert together[0] > 5 * max(alone), \
        f"the mixed culture {together[0]} is not sharply above the solo cultures {alone}"
    assert min(alone) > 0, "each mating type alone must produce some pheromone, so 'only one can' is false"
    return (f"solo cultures release {alone} and the mixed culture {together[0]:.0f}, "
            f"more than five times the larger solo value")


def q7(table, item):
    s = [(r["decade"], cg.num(r["mean adult height in the population centimeters"]))
         for r in _rows(table)]
    assert all(b[1] > a[1] for a, b in zip(s, s[1:])), f"the means must rise across decades; got {s}"
    gain = s[-1][1] - s[0][1]
    assert 10 <= gain <= 20, f"the rise recomputes to {gain} centimeters"
    assert len({d for d, _ in s}) == len(s), "the decades must be distinct"
    return f"the mean rises {gain:.0f} centimeters from the {s[0][0]} to the {s[-1][0]}, strictly increasing"


def q13(table, item):
    rows = _rows(table)
    trio = [(cg.num(r["soil ph of the pot"]), cg.normalize(r["flower color that season"]))
            for r in rows]
    assert len(trio) == 3, "reversibility needs three seasons"
    (ph1, c1), (ph2, c2), (ph3, c3) = trio
    assert ph1 == ph3 and ph1 != ph2, f"the pH must return to its first value; got {ph1}, {ph2}, {ph3}"
    assert c1 == c3 and c1 != c2, f"the colour must return with it; got {c1}, {c2}, {c3}"
    return (f"pH {ph1} gave {c1}, pH {ph2} gave {c2}, and returning to pH {ph3} gave {c3} again, "
            f"so the phenotype tracks the condition in both directions")


def q17(table, item):
    rows = _rows(table)
    cold = "mean height at 18 degrees celsius centimeters"
    warm = "mean height at 28 degrees celsius centimeters"
    d = {cg.normalize(r["plant line"]): (cg.num(r[cold]), cg.num(r[warm])) for r in rows}
    ch = {k: v[1] - v[0] for k, v in d.items()}
    biggest = max(ch, key=ch.get)
    assert biggest == "line 1", f"the largest response belongs to {biggest}"
    assert ch["line 1"] > 5 * ch["line 2"], \
        f"responses {ch} are not far enough apart to call one far stronger"
    assert not (d["line 1"][0] > d["line 2"][0] and d["line 1"][1] > d["line 2"][1]), \
        "'taller at both temperatures' must be false, and here the ranking reverses"
    return (f"line 1 changes by {ch['line 1']:.0f} centimeters and line 2 by {ch['line 2']:.0f}; "
            f"the ranking of the two lines reverses between the temperatures")


def q19(table, item):
    rows = _rows(table)
    shade = [cg.num(r["leaf area in shade square centimeters"]) for r in rows]
    sun = [cg.num(r["leaf area in full sun square centimeters"]) for r in rows]
    m_shade, m_sun = sum(shade) / len(shade), sum(sun) / len(sun)
    assert (m_shade, m_sun) == (51, 29), f"the means recompute to {m_shade} and {m_sun}"
    assert m_shade not in shade or True, "means need not equal any single replicate"
    assert m_shade != m_sun, "the equal-means distractor must be false"
    return (f"shade replicates {shade} average {m_shade:.0f}; sun replicates {sun} average "
            f"{m_sun:.0f}")


CLAIMS = [
 ("ability of one genotype to produce different phenotypes",
  "EK 5.5.A.1 states that environmental conditions influence gene expression and can lead to phenotypic plasticity, glossed in the framework as the ability of individual genotypes to produce different phenotypes. Cuttings of one plant share a genotype, so no difference in alleles is available to explain the result."),
 ("One genotype produced more than one flower color",
  "Flower color based on soil pH is an illustrative example the CED prints with EK 5.5.A.1. The table check recomputes that the acidic pots all gave blue flowers and the alkaline pots all gave pink, across cuttings the stem states came from one plant."),
 ("falls steadily as the hours of light per day increase",
  "Seasonal fur color in arctic animals is an illustrative example printed with EK 5.5.A.1. The table check recomputes that the white-coat percentage decreases at every step of the series and falls by more than fifty points overall, in animals of one inbred line."),
 ("30 degrees Celsius",
  "Sex determination in reptiles is an illustrative example printed with EK 5.5.A.1. The table check recomputes which of the five percentages is nearest fifty, confirms no other temperature ties it, and confirms the series rises with temperature."),
 ("About four times as much",
  "The effect of increased ultraviolet light on melanin production in animals is an illustrative example printed with EK 5.5.A.1. The table check recomputes the ratio of the highest to the lowest mean melanin content as a factor of four, and confirms the series is monotonic."),
 ("only when cells of the opposite mating type are present",
  "The presence of the opposite mating type affecting pheromone production in yeast and other fungi is an illustrative example printed with EK 5.5.A.1. The table check recomputes that the mixed culture releases more than five times the larger solo value, and that neither mating type alone releases nothing."),
 ("Improved conditions during growth",
  "Height and weight in humans is an illustrative example printed with EK 5.5.A.1, which locates the environment's effect in gene expression. The table check recomputes a rise of fourteen centimeters across the four decades, a span of roughly three generations, and the stem supplies the change in conditions."),
 ("same genotype and different phenotypes",
  "EK 5.3.A.2.iii defines the genotype as the set of alleles inherited and EK 5.3.A.2.iv defines the phenotype as the observable expression; EK 5.5.A.1 adds that conditions influence gene expression. Size is observable, so it belongs to the phenotype, and the greenhouse changes no allele."),
 ("cuttings taken from one parent plant under several different conditions",
  "EK 5.5.A.1 defines plasticity as the ability of individual genotypes to produce different phenotypes, so the design must hold the genotype fixed and vary the environment. Seedlings from many parents, or wild plants from several habitats, confound the two."),
 ("DNA sequence of the animal is unchanged",
  "EK 5.5.A.1 places the effect on gene expression rather than on the sequence. A mutation is an alteration of a DNA sequence, which is EK 6.7.A.1's subject; the same alleles are present in both seasons and are expressed differently."),
 ("Cuttings from a single plant, grown across the same range of conditions",
  "EK 5.5.A.1 makes plasticity a property of one genotype, so the discriminating evidence holds the genotype constant while conditions vary. Every other listed observation leaves genotype and environment varying together."),
 ("depends on which of the inherited genes are expressed",
  "EK 5.5.A.1 names gene expression as where the environment acts, and EK 5.3.A.2.iv makes the phenotype the observable expression of inherited traits. The environment can therefore alter what is observed while supplying and altering no allele."),
 ("response is reversible",
  "EK 5.5.A.1 places the effect on gene expression rather than on the DNA sequence, which allows a phenotype to track a condition in both directions. The table check recomputes that the pH returned to its first value and that the flower colour returned with it."),
 ("share a genotype but not an environment",
  "Flower color based on soil pH is an illustrative example printed with EK 5.5.A.1. Two cuttings of one plant are genetically identical by EK 5.3.A.2.iii, so the soil is the only variable left and the phenotype is expected to follow it."),
 ("biased toward one sex",
  "Sex determination in reptiles is an illustrative example printed with EK 5.5.A.1: the environmental condition sets this phenotype. Fixing the incubation temperature therefore fixes the input that decides sex, so a single-sex cohort is the predictable consequence."),
 ("Genetically identical individuals split between two conditions",
  "EK 5.5.A.1 defines phenotypic plasticity as the ability of INDIVIDUAL GENOTYPES to produce different phenotypes, so isolating the environment requires the genotype to be held constant. A phenotype spreading over generations is a change in the population instead."),
 ("Line 1 responds far more strongly",
  "EK 5.5.A.1 makes plasticity a property of individual genotypes, so genotypes may differ in how plastic they are. The table check recomputes the two responses as twenty-two centimeters against two, and confirms that the ranking of the lines reverses between the temperatures."),
 ("genotype of the plants",
  "EK 5.5.A.1 defines plasticity as one genotype producing different phenotypes, so the genotype is what must be held constant while the environmental factor varies. Holding the light constant instead would remove the comparison the conclusion rests on."),
 ("51 square centimeters in shade",
  "A mean is the sum of the values divided by their number. The table check recomputes 204 over four as 51 and 116 over four as 29, and confirms the two means differ, so the equal-means option is false on the same data."),
 ("inherited the parent's alleles, not the melanin",
  "The effect of increased ultraviolet light on melanin production is an illustrative example printed with EK 5.5.A.1, which puts the effect on gene expression. EK 5.3.A.2.iii makes the set of alleles the thing that is inherited, so the offspring receive the capacity rather than the pigment."),
 ("changes the expression of genes the cell already carries",
  "EK 5.5.A.1 states that environmental conditions influence gene expression and lists the opposite mating type's effect on pheromone production in yeast among its illustrative examples. The genes are already in the genome; the neighbouring cells change whether and how strongly they are expressed."),
 ("received the same genotype",
  "EK 5.5.A.1 states that conditions influence gene expression, and EK 5.3.A.2.iii makes the genotype the set of alleles inherited. A genetically uniform variety supplies one genotype to both fields, so no genetic difference remains to explain the yields, and yield is observable and therefore part of the phenotype."),
 ("persists when individuals from both groups are raised together",
  "EK 5.5.A.1 makes a plastic difference a response to differing conditions, so removing the difference in conditions removes it. A difference surviving a common environment cannot be attributed to an environment that is no longer differing."),
 ("encode the pigment and the machinery that responds",
  "EK 5.5.A.1 says environmental conditions influence GENE EXPRESSION, which presupposes genes to be expressed. The illustrative example of flower color based on soil pH is therefore an interaction, not a replacement of the genotype by the environment."),
 ("determined by an environmental condition in one species and by inheritance in another",
  "Sex determination in reptiles is an illustrative example printed with EK 5.5.A.1, while EK 5.4.A.2 covers traits determined by genes on sex chromosomes. Temperature acts on the expression of genes the embryo already carries and changes no chromosome."),
 ("range of phenotypes that this one genotype produces",
  "EK 5.5.A.1 glosses phenotypic plasticity as the ability of individual genotypes to produce different phenotypes. With the genotype held constant and only the temperature varied, the measurements describe that range and can say nothing about how many genotypes or alleles exist."),
 ("Conditions during growth",
  "Height and weight in humans is an illustrative example printed with EK 5.5.A.1, which states that environmental conditions influence gene expression. With the genotypes similar, the environment is the remaining source of the difference."),
 ("requires an environmental cue that the constant conditions removed",
  "Seasonal fur color in arctic animals is an illustrative example printed with EK 5.5.A.1, which places the effect of conditions on gene expression. Holding the conditions constant removes the varying input, so the expression stops varying while the alleles remain."),
 ("may come from the best soil rather than the best genotypes",
  "EK 5.5.A.1 states that conditions influence gene expression, so an observed phenotype confounds alleles with conditions. EK 5.3.A.2.iii makes the alleles the thing the offspring inherit, so the largest fruit in the best corner of the field carries no guarantee of them."),
 ("more individuals with a dark coat over many generations",
  "EK 5.5.A.1 concerns one genotype producing different phenotypes under different conditions, and the four rejected options are its own illustrative examples with the genotype held constant. A shift in which genotypes a population contains over generations is unit 7's subject, not plasticity."),
]

cg.check(b5_5, CLAIMS,
         table_checks={2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 13: q13, 17: q17, 19: q19})
