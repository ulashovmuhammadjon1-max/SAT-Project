"""Key audit for AP ENVIRONMENTAL SCIENCE 8.3 Endocrine Disruptors.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
The topic has two essential knowledge statements:

  STB-3.C.1  endocrine disruptors are chemicals that can interfere with the
             endocrine system of animals;
  STB-3.D.1  endocrine disruptors can lead to birth defects, developmental
             disorders, and gender imbalances in fish and other species.

Items 1, 4, 15, 20, 28 and 30 rest on STB-3.C.1. Items 2, 3, 5, 7, 8, 9, 10,
11, 12, 13, 16, 19, 21, 22, 23, 25, 26, 27 and 29 rest on STB-3.D.1, alone or
with the definition. Items 6, 14, 17, 18 and 24 are design and description
items under suggested skill 1.A whose keys turn on what a comparison can show,
together with the two statements above.

THE ONE PRESUPPOSITION, stated so it can be audited: the framework uses the
term endocrine system without defining it and describes NO mechanism of
interference. So the only content assumed here is that the endocrine system is
an animal's hormone system and that interference is a disturbance of its normal
working. No key states a receptor, a mimicry, or a named hormone.

NOT KEYED: no chemical is named as an endocrine disruptor, because the
framework names none in this topic -- DDT and PCBs appear in STB-3.H.1 as
persistent organic pollutants instead. No concentration or threshold is keyed;
every number belongs to the study in its own table and is recomputed below.

DATA ITEMS: 3, 5, 7, 9, 10 and 11 carry tables and every keyed reading is
recomputed from the table alone.

NEGATIVE CONTROL: `python3 verify_e8_3.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e8_3

MALE = "Male fish in the sample (percent)"
MIXED = "Fish with both male and female characteristics (percent)"
CONC = "Concentration of the test chemical in the tank (micrograms per liter)"
NORMAL = "Embryos developing normally (percent)"
DEFECT = "Embryos with visible developmental defects (percent)"
EXAMINED = "Individuals examined"
ABNORM = "Individuals with developmental abnormalities (percent)"
REPRO = "Adults showing reproductive abnormalities (percent)"
CHEM = "Chemical measured in the water (micrograms per liter)"
HATCH = "Eggs hatching successfully (percent)"
LIMB = "Hatchlings with limb or spine defects (percent)"
RIVER = "Chemical in the river (micrograms per liter)"
MALE_R = "Male fish in the sample (percent)"


def q3(table, item):
    reaches = cg.labels(table)
    pos = {r[0]: r[1] for r in table["rows"]}
    male = dict(zip(reaches, cg.col(table, MALE)))
    mixed = dict(zip(reaches, cg.col(table, MIXED)))
    near = [r for r in reaches if pos[r] == "just downstream"][0]
    up = [r for r in reaches if pos[r] == "upstream"][0]
    far = [r for r in reaches if pos[r] == "far downstream"][0]
    assert male[near] == min(male.values()), "the reach below the outfall is not lowest in males"
    assert mixed[near] == max(mixed.values()), "the reach below the outfall is not highest in mixed fish"
    assert mixed[up] == 0, "the upstream reach must show none of the mixed condition"
    assert 45 <= male[up] <= 55, "the upstream reach should sit near an even split"
    assert mixed[far] < mixed[near], "'far downstream is highest in mixed fish' must be false"
    return (f"just downstream reads {male[near]:.0f} percent male and {mixed[near]:.0f} percent "
            f"mixed against {male[up]:.0f} and {mixed[up]:.0f} upstream")


def q5(table, item):
    conc = cg.col(table, CONC)
    normal = cg.col(table, NORMAL)
    defect = cg.col(table, DEFECT)
    assert conc == sorted(conc), "the treatments must be listed in increasing order"
    assert all(defect[i] < defect[i + 1] for i in range(len(defect) - 1)), \
        f"the defect share does not rise with concentration: {defect}"
    assert all(normal[i] > normal[i + 1] for i in range(len(normal) - 1)), \
        f"the normal share does not fall with concentration: {normal}"
    for n, d in zip(normal, defect):
        assert abs(n + d - 100) < 1e-6, f"the two shares must total one hundred, got {n} and {d}"
    assert defect[0] == min(defect), "'defects only in the untreated tank' must be false"
    return (f"defects run {defect} percent as the concentration runs {conc}, rising throughout, "
            "and each pair of shares totals one hundred")


def q7(table, item):
    rows = cg.labels(table)
    rate = dict(zip(rows, cg.col(table, ABNORM)))
    ref = [r for r in rows if "reference" in r.lower()][0]
    exposed = [r for r in rows if r != ref]
    assert len(exposed) == 3, "three exposed groups are required"
    assert min(rate[r] for r in exposed) > 4 * rate[ref], \
        f"not every exposed group is far above the reference: {rate}"
    assert rate[ref] == min(rate.values()), "'the reference site is highest' must be false"
    assert len(set(rate.values())) == len(rate), "'identical in all four rows' must be false"
    turtle = [r for r in rows if r.startswith("Turtle")][0]
    assert rate[turtle] != max(rate.values()), "'the turtle is highest' must be false"
    return (f"the contaminated wetland gives {[rate[r] for r in exposed]} percent against "
            f"{rate[ref]:.0f} percent at the reference site, more than four times in every case")


def q9(table, item):
    groups = cg.labels(table)
    rate = dict(zip(groups, cg.col(table, REPRO)))
    embryo = [g for g in groups if "embryos" in g][0]
    adult = [g for g in groups if "adults" in g][0]
    never = [g for g in groups if "Never" in g][0]
    assert rate[embryo] > 3 * rate[adult], \
        f"embryonic exposure is not far above adult exposure: {rate}"
    assert rate[embryo] > 10 * rate[never], "embryonic exposure is not far above the unexposed rate"
    assert rate[never] == min(rate.values()), "'the never-exposed group is highest' must be false"
    assert len(set(rate.values())) == 3, "'the same in all three groups' must be false"
    return (f"embryonic exposure gives {rate[embryo]:.0f} percent against {rate[adult]:.0f} for "
            f"adult exposure and {rate[never]:.0f} for the never-exposed group")


def q10(table, item):
    chem = cg.col(table, CHEM)
    hatch = cg.col(table, HATCH)
    limb = cg.col(table, LIMB)
    assert chem == sorted(chem), "the ponds must be listed in increasing order of the chemical"
    assert all(hatch[i] > hatch[i + 1] for i in range(len(hatch) - 1)), \
        f"hatching success does not fall as the chemical rises: {hatch}"
    assert all(limb[i] < limb[i + 1] for i in range(len(limb) - 1)), \
        f"the defect share does not rise as the chemical rises: {limb}"
    assert limb[chem.index(max(chem))] == max(limb), \
        "'the most contaminated pond has the fewest defects' must be false"
    return (f"as the chemical runs {chem} the hatching success runs {hatch} percent and the defect "
            f"share {limb} percent, one falling and the other rising at every step")


def q11(table, item):
    years = cg.labels(table)
    chem = dict(zip(years, cg.col(table, RIVER)))
    male = dict(zip(years, cg.col(table, MALE_R)))
    seq = list(years)
    assert all(chem[seq[i]] > chem[seq[i + 1]] for i in range(len(seq) - 1)), \
        f"the chemical does not fall across the record: {chem}"
    assert all(male[seq[i]] < male[seq[i + 1]] for i in range(len(seq) - 1)), \
        f"the male share does not rise across the record: {male}"
    assert male[seq[-1]] > male[seq[0]], "the male share must end above where it began"
    assert abs(male[seq[-1]] - 50) < abs(male[seq[0]] - 50), \
        "the male share must end nearer an even split than it began"
    return (f"the chemical falls {[chem[y] for y in seq]} while the male share rises "
            f"{[male[y] for y in seq]} percent, ending nearer an even split")


CLAIMS = [
 ("interfere with the endocrine system of animals",
  "STB-3.C.1 verbatim: endocrine disruptors are chemicals that can interfere with the endocrine system of animals. Dissolving shells, removing oxygen, causing infection and altering a physical condition belong to other agents described in STB-4.H.4, STB-3.F.2, EIN-3.D and STB-3.G.1."),
 ("Birth defects, developmental disorders, and gender imbalances in fish and other species",
  "STB-3.D.1 verbatim. Suffocation, corrosion and hearing loss are effects of other pollutants elsewhere in the course, and the framework describes no benefit of exposure."),
 ("smallest share of males and the largest share of fish with mixed characteristics",
  "Recomputed in q3 above: the reach just below the outfall carries both extremes while the upstream reach sits near an even split with none of the mixed condition. Gender imbalance in fish is one of the effects in STB-3.D.1."),
 ("disturbs the normal working of the animal's hormone system",
  "STB-3.C.1 uses the term endocrine system without defining it; the endocrine system is an animal's hormone system, so interference with it is a disturbance of that system's normal working. No mechanism beyond that is claimed, because the framework states none. The rejected options describe asphyxiation, oxygen depletion, thermal pollution and acidification."),
 ("developmental defects rises with the concentration",
  "Recomputed in q5 above: the defect share rises at every step, the normal share falls in step, and the two always total one hundred. Developmental disorders are one of the effects named in STB-3.D.1."),
 ("altered sex ratios in animals exposed to it than in comparable animals that are not",
  "STB-3.D.1's effects are birth defects, developmental disorders and gender imbalances, so evidence of disruption is a difference in those outcomes between exposed and comparable unexposed animals. Presence of the chemical, production figures and opinion measure no effect."),
 ("higher rate of abnormalities than the same fish species does at the reference wetland",
  "Recomputed in q7 above: all three species in the contaminated wetland exceed four times the reference rate for the same fish species. STB-3.D.1 applies its effects to fish and other species alike."),
 ("attributed to fish and other species together",
  "STB-3.D.1's own wording is birth defects, developmental disorders, and gender imbalances in fish and other species, so the effects are not confined to fish. Nothing in the framework makes the endocrine system unique to fish or restricts the term to laboratory animals."),
 ("Exposure during embryonic development produced far more reproductive abnormalities",
  "Recomputed in q9 above: the embryo-exposed group exceeds three times the adult-exposed rate and ten times the never-exposed rate. Birth defects and developmental disorders in STB-3.D.1 are outcomes of exposure during development."),
 ("hatching success falls and the share of hatchlings with defects rises",
  "Recomputed in q10 above: ordering the ponds by the measured chemical puts hatching success in decreasing order and the defect share in increasing order. Birth defects are one of the effects in STB-3.D.1."),
 ("share of male fish rose toward an even split",
  "Recomputed in q11 above: the measured chemical falls at every step after closure while the male share rises at every step and ends nearer half the sample than it began. Gender imbalance in fish is one of the effects in STB-3.D.1."),
 ("concern development and reproduction rather than immediate survival",
  "STB-3.D.1 lists birth defects, developmental disorders and gender imbalances, all of which concern the production and development of young rather than the survival of exposed adults. That is why a population can be affected without adult deaths."),
 ("Gender imbalance in a species exposed to an endocrine disruptor",
  "A skewed proportion of males is a gender imbalance, which STB-3.D.1 lists among the effects of endocrine disruptors in fish and other species. The rejected options belong to STB-3.B.8, STB-2.I.2, STB-3.B.9 and STB-3.B.5."),
 ("same species from a similar reach with no exposure, examined in the same way",
  "Suggested skill 1.A applied to STB-3.D.1's effects: attributing them to the exposure requires a comparison group alike in species and setting but unexposed, examined identically. A different species, a repeated examination of one group, an old description and a bare count cannot supply that."),
 ("rather than immediate lethality",
  "STB-3.C.1 gives interference with a body system and STB-3.D.1 gives three developmental and reproductive outcomes, which is a different claim from immediate lethality. The framework states no dose threshold and confines the effects to no life stage."),
 ("decline in the total number of animals following an unusually cold winter",
  "A decline in numbers after cold weather is not among the three effects of STB-3.D.1 and has an evident alternative cause. Skewed sex ratios, mixed characteristics and developmental or birth defects are exactly what that statement names."),
 ("describe the effects it can have on organisms in ecosystems",
  "The topic's two learning objectives are STB-3.C, describe endocrine disruptors, and STB-3.D, describe their effects on ecosystems. The framework supplies no harmful concentration, no chemical structures, no reaction sequence and no ranking of disruptors."),
 ("comparison with an unexposed reach would test that",
  "Mixed sexual characteristics are an instance of the gender imbalance in STB-3.D.1, so the observation is consistent with endocrine disruption; but a single downstream observation identifies no particular chemical and says nothing about mortality."),
 ("outcomes of exposure during development",
  "STB-3.D.1 names birth defects and developmental disorders, which are effects on development itself and therefore appear in animals exposed while developing. The framework neither confines the endocrine system to the young nor makes adults unexposed."),
 ("interference with a body system leading to developmental and reproductive outcomes",
  "STB-3.C.1 and STB-3.D.1 together describe a chemical interfering with the endocrine system and producing birth defects, developmental disorders and gender imbalances, none of which requires the death of the exposed animal."),
 ("outcome the framework attributes to interference with the endocrine system",
  "STB-3.D.1 lists gender imbalances alongside birth defects and developmental disorders as effects in fish and other species. It is an outcome in the animals rather than a measurement of the water, and it is not attributed to oxygen or sediment."),
 ("survey of the river population for the same defects",
  "Suggested skill 1.A with STB-3.D.1. Linking a laboratory result to a wild population requires looking for the same effects in that population against a comparable unexposed one; repeating the laboratory work or measuring the channel tests nothing about the population."),
 ("gender imbalance among the animals in an exposed population",
  "STB-3.D.1 lists birth defects, developmental disorders and gender imbalances; the first two are observed in individuals while an imbalance is a property of the population's composition. All are the framework's effects, and only the imbalance is inherently about the group."),
 ("what rate of defects and what sex ratio occur without the exposure",
  "Suggested skill 1.A. The effects in STB-3.D.1 are rates and ratios that take some value without exposure as well, so a comparison site is what makes an elevated rate meaningful. It does not supply animals or replace the exposed site's measurements."),
 ("none of which requires the death of the exposed animal",
  "STB-3.C.1 defines endocrine disruptors by interference with the endocrine system and STB-3.D.1 gives three developmental and reproductive effects, so survival is not the test of whether a chemical is one."),
 ("mixed sexual characteristics at several distances downstream",
  "Mixed characteristics are an instance of STB-3.D.1's gender imbalance, and a gradient with distance compared against upstream ties the effect to the outfall. Channel width, traffic, effluent temperature and license sales measure no effect on the animals."),
 ("Hatchlings born with malformed limbs, birth defects",
  "STB-3.D.1 lists birth defects, developmental disorders and gender imbalances, and malformed limbs present at hatching are birth defects. Each rejected pairing attaches an observation to the wrong category or to organisms the statement does not concern."),
 ("chemicals released into ecosystems whose interference with animals is the harm",
  "STB-3.C.1 defines them as chemicals that can interfere with the endocrine system of animals, which makes them pollutants acting on organisms. The framework gives them no role in setting carrying capacity and does not make them a natural feature of every ecosystem."),
 ("fish and other species, so more than one kind of animal can be affected",
  "STB-3.D.1's wording, in fish and other species, is what leaves the question open, since it confines the effects to no single kind of animal, no habitat and no life stage."),
 ("interfere with the endocrine system of animals can lead to birth defects",
  "The keyed summary states STB-3.C.1 and STB-3.D.1 together. The rejected summaries belong to thermal pollution under STB-3.G, persistent organic pollutants and biomagnification under STB-3.H and STB-3.I, eutrophication under STB-3.F, and litter under STB-3.B.8."),
]

TABLE_CHECKS = {3: q3, 5: q5, 7: q7, 9: q9, 10: q10, 11: q11}

es.run(e8_3, CLAIMS, TABLE_CHECKS, sys.argv)
