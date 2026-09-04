"""Key audit for AP ENVIRONMENTAL SCIENCE 5.14 Integrated Pest Management.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
  STB-1.C.1  IPM is a combination of methods used to effectively control pest
             species while minimizing the disruption to the environment. These
             methods include biological, physical, and limited chemical methods
             such as biocontrol, intercropping, crop rotation, and natural
             predators of the pests.
                        -- items 1, 2, 3, 4, 5, 10, 11, 17, 18, 19, 20, 21, 22, 26
  STB-1.D.1  The use of IPM reduces the risk that pesticides pose to wildlife,
             water supplies, and human health.
                        -- items 6, 7, 13, 14, 15, 16, 24
  STB-1.D.2  IPM minimizes disruptions to the environment and threats to human
             health but can be complex and expensive.
                        -- items 8, 9, 12, 23
Items 25 (research design), 27 (boundary with 5.6), 28 (the two hedges), 29 and
30 read across all three.

THE TWO HEDGES, gated rather than merely obeyed. STB-1.C.1 says EFFECTIVELY
CONTROL, not eliminate; STB-1.D.2 says CAN BE complex and expensive, not always
is. Item 28 keys both, and no other key anywhere in the module strengthens
either.

THE WORD LIMITED. STB-1.C.1 lists LIMITED CHEMICAL methods among the approach's
own methods, so IPM restricts chemical control rather than forbidding it. Items
3 and 22 key that, and the rejected options are the ban and the free hand.

BOUNDARY WITH 5.6, gated by item 27: resistance through artificial selection is
EIN-2.G.1 and belongs to that topic, and loss of a crop's genetic diversity is
EIN-2.G.2. Neither is keyed here; both appear only as rejected options.

DATA ITEMS: 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 and 21, recomputed below
from those tables alone and addressed by row label.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
"""
import e_check
import cg_check as cg
import e5_14

CONV = "Field under conventional spraying"
IPM = "Field under integrated pest management"
PEST_KG = "Pesticide applied (kilograms per hectare)"
LOST = "Crop lost to the pest (percent)"
COST = "Cost of pest control (currency units per hectare)"
HOURS = "Hours of monitoring and planning (per hectare)"

SPRAYED_STREAM = ("Pesticide in the stream draining the sprayed fields "
                  "(micrograms per litre)")
MANAGED_STREAM = ("Pesticide in the stream draining the managed fields "
                  "(micrograms per litre)")

WCONV = "Fields under conventional spraying"
WIPM = "Fields under integrated pest management"
BEETLES = "Predatory beetles (per square meter)"
BEES = "Wild bee species recorded"
BIRDS = "Farmland bird pairs per hundred hectares"

SEASONS = "Seasons the same crop is grown in succession"
LARVAE = "Pest larvae in the soil (per square meter)"
SAME = "The same crop every season"
BREAK = "The same crop for three seasons, then a break"
DIFFERENT = "A different crop every season"

DAMAGED = "Crop rows damaged by the pest (percent)"
ONECROP = "A single crop across the whole field"
TWOCROP = "Two crops in alternating strips"
THREECROP = "Three crops intercropped in the same beds"

RELEASED = "Predatory mites released (thousands per hectare)"
PESTMITES = "Pest mites on the leaves (per leaf)"


def q10(table, item):
    assert cg.cell(table, PEST_KG, IPM) < cg.cell(table, PEST_KG, CONV), \
        "the managed field must apply less pesticide"
    assert cg.cell(table, PEST_KG, CONV) > 3 * cg.cell(table, PEST_KG, IPM), \
        "the difference in pesticide must be large, not marginal"
    assert abs(cg.cell(table, LOST, IPM) - cg.cell(table, LOST, CONV)) <= 2, \
        "the crop lost must be about the same under the two regimes"
    assert cg.cell(table, COST, IPM) > cg.cell(table, COST, CONV), \
        "the managed field must cost more"
    assert cg.cell(table, HOURS, IPM) > cg.cell(table, HOURS, CONV), \
        "the managed field must take more planning"
    return (f"the managed field applies {cg.cell(table, PEST_KG, IPM):.0f} kilograms per hectare "
            f"against {cg.cell(table, PEST_KG, CONV):.0f}, loses {cg.cell(table, LOST, IPM):.0f} "
            f"percent against {cg.cell(table, LOST, CONV):.0f}, costs "
            f"{cg.cell(table, COST, IPM):.0f} against {cg.cell(table, COST, CONV):.0f} and takes "
            f"{cg.cell(table, HOURS, IPM):.0f} hours against {cg.cell(table, HOURS, CONV):.0f}")


def q11(table, item):
    base = cg.cell(table, PEST_KG, IPM)
    assert base > 0, "the managed field's application must be non-zero for a ratio to exist"
    ratio = cg.cell(table, PEST_KG, CONV) / base
    assert ratio == 4, f"the ratio recomputes to {ratio}, not 4"
    for wrong in (base, cg.cell(table, PEST_KG, CONV) - base,
                  cg.cell(table, PEST_KG, CONV) + base, 1):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return f"12 divided by 3 is {ratio:.0f} times as much pesticide on the sprayed field"


def q12(table, item):
    d = cg.cell(table, COST, IPM) - cg.cell(table, COST, CONV)
    assert d == 35, f"the difference recomputes to {d}, not 35"
    for wrong in (cg.cell(table, COST, IPM),
                  cg.cell(table, COST, IPM) + cg.cell(table, COST, CONV),
                  cg.cell(table, COST, CONV),
                  cg.cell(table, PEST_KG, CONV) - cg.cell(table, PEST_KG, IPM)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"95 minus 60 is {d:.0f} currency units per hectare more on the managed field"


def q13(table, item):
    s, m = cg.col(table, SPRAYED_STREAM), cg.col(table, MANAGED_STREAM)
    assert cg.cell(table, "Year 1", SPRAYED_STREAM) == min(s), \
        "the sprayed stream must start at its lowest reading"
    assert all(s[i] < s[i + 1] for i in range(len(s) - 1)), f"the sprayed stream must rise; got {s}"
    assert all(m[i] > m[i + 1] for i in range(len(m) - 1)), f"the managed stream must fall; got {m}"
    return (f"the sprayed stream runs {s} micrograms per litre while the managed stream runs "
            f"{m}, the two moving in opposite directions")


def q14(table, item):
    d = cg.cell(table, "Year 8", SPRAYED_STREAM) - cg.cell(table, "Year 8", MANAGED_STREAM)
    assert d == 24, f"the difference recomputes to {d}, not 24"
    for wrong in (cg.cell(table, "Year 8", SPRAYED_STREAM),
                  cg.cell(table, "Year 8", SPRAYED_STREAM)
                  + cg.cell(table, "Year 8", MANAGED_STREAM),
                  cg.cell(table, "Year 4", SPRAYED_STREAM)
                  - cg.cell(table, "Year 4", MANAGED_STREAM),
                  cg.cell(table, "Year 8", MANAGED_STREAM)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"27 minus 3 is {d:.0f} micrograms per litre lower in the managed stream"


def q15(table, item):
    for row in (BEETLES, BEES, BIRDS):
        assert cg.cell(table, row, WIPM) > cg.cell(table, row, WCONV), \
            f"the count for {row!r} must be higher on the managed fields"
    assert cg.cell(table, BEETLES, WCONV) == min(cg.col(table, WCONV)), \
        "the beetle row must hold the smallest count on the sprayed fields"
    return (f"beetles {cg.cell(table, BEETLES, WIPM):.0f} against "
            f"{cg.cell(table, BEETLES, WCONV):.0f}, bee species "
            f"{cg.cell(table, BEES, WIPM):.0f} against {cg.cell(table, BEES, WCONV):.0f} and "
            f"bird pairs {cg.cell(table, BIRDS, WIPM):.0f} against "
            f"{cg.cell(table, BIRDS, WCONV):.0f}")


def q16(table, item):
    d = cg.cell(table, BEES, WIPM) - cg.cell(table, BEES, WCONV)
    beetle = cg.cell(table, BEETLES, WIPM) - cg.cell(table, BEETLES, WCONV)
    assert d == 16, f"the difference recomputes to {d}, not 16"
    assert beetle == 15, f"the beetle difference recomputes to {beetle}, not 15"
    for wrong in (cg.cell(table, BEES, WIPM),
                  cg.cell(table, BEES, WIPM) + cg.cell(table, BEES, WCONV),
                  beetle, cg.cell(table, BEES, WCONV)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return (f"23 minus 7 is {d:.0f} more bee species on the managed fields, against a beetle "
            f"difference of {beetle:.0f}")


def q17(table, item):
    s, l = cg.col(table, SEASONS), cg.col(table, LARVAE)
    assert cg.cell(table, SAME, SEASONS) == max(s), \
        "the unchanged field must carry the longest run of one crop"
    assert cg.cell(table, SAME, LARVAE) == max(l), "the unchanged field must hold the most larvae"
    assert cg.cell(table, DIFFERENT, LARVAE) == min(l), \
        "'the field that changes crop every season holds the most' must be false"
    assert all(s[i] > s[i + 1] for i in range(len(s) - 1)), f"the run must shorten; got {s}"
    assert all(l[i] > l[i + 1] for i in range(len(l) - 1)), f"the larvae must fall with it; got {l}"
    return (f"runs of {s} seasons carry {l} larvae per square meter, falling together as the run "
            "of one crop shortens")


def q18(table, item):
    base = cg.cell(table, DIFFERENT, LARVAE)
    assert base > 0, "the rotated field must hold some larvae for a ratio to exist"
    ratio = cg.cell(table, SAME, LARVAE) / base
    assert ratio == 8, f"the ratio recomputes to {ratio}, not 8"
    for wrong in (4, cg.cell(table, BREAK, LARVAE) / base, cg.cell(table, SAME, SEASONS) / 3, 1):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return f"320 divided by 40 is {ratio:.0f} times as many larvae under the unchanged crop"


def q19(table, item):
    d = cg.col(table, DAMAGED)
    assert cg.cell(table, ONECROP, DAMAGED) == max(d), \
        "'the single-crop field suffered the least damage' must be false"
    assert cg.cell(table, THREECROP, DAMAGED) == min(d), \
        "the most mixed planting must suffer the least damage"
    assert all(d[i] > d[i + 1] for i in range(len(d) - 1)), f"damage must fall; got {d}"
    assert len(set(d)) == len(d), "'the same share of damage' must be false"
    return (f"damage runs {d} percent from a single crop through two crops in strips to three "
            "crops intercropped, falling as the mixture increases")


def q20(table, item):
    d = cg.col(table, DAMAGED)
    diff = cg.cell(table, ONECROP, DAMAGED) - cg.cell(table, THREECROP, DAMAGED)
    assert diff == 22, f"the difference recomputes to {diff}, not 22"
    for wrong in (max(d), max(d) + min(d),
                  cg.cell(table, ONECROP, DAMAGED) - cg.cell(table, TWOCROP, DAMAGED), min(d)):
        assert diff != wrong, f"the {wrong} distractor equals the key"
    return f"31 minus 9 is {diff:.0f} percentage points less of the crop damaged"


def q21(table, item):
    p, r = cg.col(table, PESTMITES), cg.col(table, RELEASED)
    assert cg.cell(table, "Before release", PESTMITES) == max(p), \
        "the pest must be highest before the predators are released"
    assert all(p[i] > p[i + 1] for i in range(len(p) - 1)), f"the pest must fall; got {p}"
    assert cg.cell(table, "Before release", RELEASED) == 0, \
        "no predators may have been released before the release"
    assert (cg.cell(table, "One month after release", RELEASED)
            == cg.cell(table, "Three months after release", RELEASED)), \
        "'the number of predators released fell as the pest fell' must be false"
    return (f"pest mites run {p} per leaf against predators released of {r} thousand per hectare, "
            "the pest falling while the release stays put")


CLAIMS = [
 ("combination of methods used to effectively control pest species while minimizing",
  "STB-1.C.1, near verbatim: IPM is A COMBINATION OF METHODS used to EFFECTIVELY CONTROL pest species WHILE MINIMIZING THE DISRUPTION TO THE ENVIRONMENT. Each rejected option reduces it to one method, drops the environmental condition, or reverses the aim, so the anchor spans the whole clause."),
 ("Biological, physical, and limited chemical methods",
  "STB-1.C.1 states that the methods include BIOLOGICAL, PHYSICAL, AND LIMITED CHEMICAL methods. One distractor keeps the three categories and removes the limit, so the anchor carries the word limited."),
 ("remain part of the approach but are restricted rather than excluded",
  "STB-1.C.1 lists LIMITED CHEMICAL methods alongside biological and physical ones, so the chemical component is inside the approach and bounded. Reading the word as a ban, or ignoring it, both depart from the statement, and it fixes no order in which methods must be tried."),
 ("Biocontrol, intercropping, crop rotation, and natural predators",
  "STB-1.C.1 names biocontrol, intercropping, crop rotation, and natural predators of the pests. Contour plowing, terracing, windbreaks and strip cropping are STB-1.E.1's soil conservation methods and prescribed burning and reforestation are STB-1.G, both in other topics."),
 ("Blanket spraying of a broad-spectrum insecticide",
  "STB-1.C.1's four examples are biocontrol, intercropping, crop rotation, and natural predators of the pests. Spraying a whole field with a broad-spectrum chemical is neither limited nor listed, and it is the practice EIN-2.G.1 ties to resistance in topic 5.6."),
 ("risk that pesticides pose to wildlife, water supplies, and human health",
  "STB-1.D.1, near verbatim: the use of IPM reduces THE RISK THAT PESTICIDES POSE TO WILDLIFE, WATER SUPPLIES, AND HUMAN HEALTH. Loss of a crop's genetic diversity is EIN-2.G.2 in topic 5.6, and the other options name nothing the statement mentions."),
 ("Wildlife, water supplies, and human health",
  "STB-1.D.1 names those three as what pesticides put at risk. The nearest distractor swaps the third for loss of the crop's genetic diversity, which EIN-2.G.2 attaches to engineered crops in a different topic."),
 ("It can be complex and expensive",
  "STB-1.D.2 states that IPM minimizes disruptions to the environment and threats to human health BUT CAN BE COMPLEX AND EXPENSIVE. The framework does record drawbacks, and neither crop loss nor extra pesticide is among them."),
 ("minimizes disruptions to the environment and threats to human health",
  "STB-1.D.2 opens with those two benefits and only then adds the drawbacks. Two rejected options reverse one of the two, so the anchor carries both; cost and labour are the statement's drawbacks rather than benefits."),
 ("used far less pesticide and lost about as little crop, but cost more",
  "Recomputed in q10 above: 3 kilograms per hectare against 12, 8 percent of the crop lost against 9, 95 currency units against 60, and 14 hours of planning against 2. STB-1.C.1 has IPM effectively controlling the pest and STB-1.D.2 warns it can be complex and expensive. One distractor keeps the first half and reverses the second, so the anchor spans both."),
 ("Four times as much",
  "Recomputed in q11 above: 12 divided by 3 kilograms per hectare. The rejected values quote the managed field alone, take the difference rather than the ratio, add the two, or deny that they differ."),
 ("35 currency units per hectare more",
  "Recomputed in q12 above: 95 minus 60 currency units per hectare. The rejected values quote one field's cost alone, add the two, or take the difference in pesticide applied. STB-1.D.2 warns that IPM can be expensive."),
 ("managed fields fell while pesticide in the stream draining the sprayed fields rose",
  "Recomputed in q13 above: the sprayed stream 20, 24 and 27 micrograms per litre against the managed stream 18, 9 and 3. STB-1.D.1 states that IPM reduces the risk pesticides pose to water supplies. One distractor swaps the two directions, so the anchor carries both."),
 ("24 micrograms per litre lower",
  "Recomputed in q14 above: 27 minus 3 micrograms per litre in the final year. The rejected values quote the sprayed stream alone, add the two, take an earlier year, or quote the managed stream alone."),
 ("Every group counted was more numerous on the managed fields",
  "Recomputed in q15 above: beetles 19 against 4, bee species 23 against 7, bird pairs 12 against 5. STB-1.D.1 states that the use of IPM reduces the risk pesticides pose to wildlife. One distractor reverses the direction, so the anchor carries it."),
 ("16 more species",
  "Recomputed in q16 above: 23 minus 7 wild bee species. The rejected values quote the managed fields alone, add the two, give the beetle row's difference of 15, or quote the sprayed fields alone."),
 ("longer the same crop is grown in succession, the more pest larvae",
  "Recomputed in q17 above: six seasons of one crop carry 320 larvae per square meter, three seasons carry 150, and a different crop every season carries 40. STB-1.C.1 names crop rotation among the methods of integrated pest management. One distractor reverses the direction, so the anchor carries it."),
 ("Eight times as many",
  "Recomputed in q18 above: 320 divided by 40 larvae per square meter. The rejected values come from the middle field, from the column counting seasons, or from denying that the fields differ."),
 ("Mixing more crops into the same ground went with less of the crop being damaged",
  "Recomputed in q19 above: 31 percent damaged under a single crop, 17 under two crops in strips and 9 under three intercropped. STB-1.C.1 names intercropping among the methods of integrated pest management. One distractor reverses the direction, so the anchor carries it."),
 ("22 percentage points less",
  "Recomputed in q20 above: 31 minus 9 percent of the rows damaged. The rejected values quote the single crop alone, add the two, compare the wrong pair of arrangements, or quote the most mixed planting alone."),
 ("pest fell steadily after the predators were released",
  "Recomputed in q21 above: 46 pest mites per leaf before the release, 18 after a month and 5 after three months, with the release held at 20 thousand per hectare. STB-1.C.1 names biocontrol and natural predators of the pests among its methods. One distractor reverses the direction, so the anchor carries it."),
 ("includes limited chemical methods among the approach's own methods",
  "STB-1.C.1 lists biological, physical, AND LIMITED CHEMICAL methods, so a bounded chemical component is part of the approach rather than outside it. The statement attaches no sequence in which the methods must be tried and places no other condition on their use."),
 ("says it can be complex and expensive",
  "STB-1.D.2 states that IPM minimizes disruptions to the environment and threats to human health BUT CAN BE COMPLEX AND EXPENSIVE. The word can is a hedge, so the framework neither promises cheapness nor asserts that every scheme is costly."),
 ("Less pesticide in the water drawn from the stream",
  "STB-1.D.1 names water supplies among the three things pesticides put at risk, so the evidence is a fall in pesticide in the water actually used. Pest counts, yield, labour and market price measure other things, some of which the framework never mentions."),
 ("neighbouring fields of the same crop and soil, one managed each way",
  "A comparison isolates the approach only when crop, soil and season are matched and the outcome is measured on both sides. Each rejected design supplies no comparison, lets the weather or the crop vary alongside the treatment, or collects opinion in place of measurement."),
 ("Combining biological, physical and limited chemical methods",
  "STB-1.C.1 defines IPM as that combination and STB-1.D.1 states that its use reduces the risk pesticides pose to water supplies, which is the grower's concern. Nothing in the framework recommends leaving a pest uncontrolled, and crop rotation is one of its own named methods rather than growing one crop repeatedly."),
 ("resistant to a control method through artificial selection",
  "Resistance arising through ARTIFICIAL SELECTION is EIN-2.G.1 in topic 5.6, a statement about the consequence of common pest-control chemicals. Every rejected option is quoted from STB-1.C.1, STB-1.D.1 or STB-1.D.2, which are this topic's own statements."),
 ("EFFECTIVELY CONTROL pest species, and that the approach CAN BE complex",
  "STB-1.C.1 says the methods EFFECTIVELY CONTROL pest species rather than remove them, and STB-1.D.2 says the approach CAN BE complex and expensive rather than that it always is. Both are hedges, and strengthening either goes past the framework, so the anchor carries both."),
 ("first says what the approach is, the second says what its use reduces the risk to",
  "STB-1.C.1 defines the approach and lists its methods, STB-1.D.1 names wildlife, water supplies and human health as what its use protects, and STB-1.D.2 sets two benefits against complexity and cost. One distractor is the swap of the definition and the cost-benefit statement, so the anchor carries the ordering."),
 ("such as biocontrol, intercropping, crop rotation and natural predators, to control pests",
  "The keyed summary carries STB-1.C.1's definition, categories and examples, STB-1.D.1's three protected things, and STB-1.D.2's benefits and drawbacks. Each rejected summary bans the chemical component, reverses a direction, or substitutes STB-1.E.1's soil conservation methods or EIN-2.G.2's crop diversity claim."),
]

TABLE_CHECKS = {10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16,
                17: q17, 18: q18, 19: q19, 20: q20, 21: q21}

e_check.run(e5_14, CLAIMS, TABLE_CHECKS)
