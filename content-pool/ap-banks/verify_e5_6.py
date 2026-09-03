"""Key audit for AP ENVIRONMENTAL SCIENCE 5.6 Pest Control Methods.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
EIN-2.G.1  common pest-control methods are pesticides, herbicides, fungicides,
           rodenticides and insecticides; one consequence of using them is that
           ORGANISMS can become resistant to them THROUGH ARTIFICIAL SELECTION;
           pest control decreases crop damage by pest and increases crop yields
             -- items 1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 16, 17, 21, 23, 24, 25,
                28, 29
EIN-2.G.2  crops can be genetically engineered to increase THEIR resistance to
           pests and diseases; however, using engineered crops can lead to loss
           of genetic diversity OF THAT PARTICULAR CROP
             -- items 10, 11, 12, 13, 14, 19, 20, 22, 27
both together                                    -- items 18, 26, 30

THE TWO RESISTANCES. EIN-2.G.1's resistance belongs to the PEST and is directed
at the control method; EIN-2.G.2's resistance is engineered into the CROP and
is directed at pests and diseases. Items 18 and 29 test the distinction and
several distractors elsewhere are built by swapping them, which is the error a
prepared student actually makes.

Integrated pest management (STB-1.C, STB-1.D, topic 5.14) appears only as a
rejected option, never as a key.

DATA ITEMS: 4, 5, 7, 8, 9, 12, 13, 14, 16, 17, 19, 20 and 28 carry tables,
recomputed below from those tables alone and anchored to named rows.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs.
"""
import e_check
import cg_check as cg
import e5_6

SURV = "Share of the population surviving the standard dose (percent)"
DAMAGE = "Share of the crop damaged by the pest (percent)"
HARVEST = "Crop harvested (tonnes per hectare)"
DOSE = ("Dose needed to kill nine tenths of the pest population "
        "(grams per hectare)")
VARIETIES = "Number of distinct varieties of the crop planted in the district"
LEADING = "Share of the planted area sown to the single leading variety (percent)"
GE_DAMAGE = "Share of plants showing pest damage at harvest (percent)"
GROWN = "Number of distinct varieties of the crop grown"
LOST = "Share of the district's crop lost to a single new disease (percent)"

UNTREATED = "No pest control applied"
TREATED = "Pest control applied"
CONV = ["Field 1", "Field 2"]
ENG = ["Field 3", "Field 4"]


def q4(table, item):
    v = cg.col(table, SURV)
    assert cg.cell(table, "First", SURV) == min(v), "the first generation must survive least"
    assert all(v[i] < v[i + 1] for i in range(len(v) - 1)), f"survival must rise; got {v}"
    assert v[-1] > v[0], "the final generation must survive more than the first"
    return f"the tabulated survival shares are {v} percent, rising with no reversal"


def q5(table, item):
    d = cg.cell(table, "Fifteenth", SURV) - cg.cell(table, "First", SURV)
    assert d == 78, f"the rise recomputes to {d}, not 78"
    for wrong in (82, 65, 34, 86):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"82 minus 4 is {d:.0f} percentage points of extra survival"


def q7(table, item):
    assert cg.cell(table, TREATED, DAMAGE) < cg.cell(table, UNTREATED, DAMAGE), \
        "the treated plot must suffer the smaller share of damage"
    assert cg.cell(table, TREATED, HARVEST) > cg.cell(table, UNTREATED, HARVEST), \
        "the treated plot must produce the larger harvest"
    return (f"the treated plot reads {cg.cell(table, TREATED, DAMAGE):.0f} percent damage "
            f"against {cg.cell(table, UNTREATED, DAMAGE):.0f}, and "
            f"{cg.cell(table, TREATED, HARVEST)} tonnes per hectare against "
            f"{cg.cell(table, UNTREATED, HARVEST)}")


def q8(table, item):
    base = cg.cell(table, UNTREATED, HARVEST)
    assert base > 0, "the untreated yield must be non-zero for a ratio to exist"
    r = cg.cell(table, TREATED, HARVEST) / base
    assert r == 2, f"the yield ratio recomputes to {r}, not 2"
    for wrong in (4, 9, 0.5, 1):
        assert r != wrong, f"the {wrong} distractor equals the key"
    return f"4.8 divided by 2.4 is {r:.0f} times the untreated yield"


def q9(table, item):
    d = cg.cell(table, UNTREATED, DAMAGE) - cg.cell(table, TREATED, DAMAGE)
    assert d == 29, f"the reduction recomputes to {d}, not 29"
    for wrong in (38, 9, 47, 24):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"38 minus 9 is {d:.0f} percentage points less of the crop damaged"


def q12(table, item):
    var = cg.col(table, VARIETIES)
    lead = cg.col(table, LEADING)
    assert cg.cell(table, "Before engineered seed was available", VARIETIES) == max(var), \
        "the earliest period must carry the most varieties"
    assert all(var[i] > var[i + 1] for i in range(len(var) - 1)), f"varieties must fall; got {var}"
    assert all(lead[i] < lead[i + 1] for i in range(len(lead) - 1)), \
        f"the leading variety's share must rise; got {lead}"
    return (f"varieties run {var} while the leading variety's share runs {lead} percent, "
            "moving in opposite directions with no reversal")


def q13(table, item):
    d = (cg.cell(table, "Before engineered seed was available", VARIETIES)
         - cg.cell(table, "Twenty years after it became available", VARIETIES))
    assert d == 30, f"the loss recomputes to {d}, not 30"
    for wrong in (34, 23, 7, 38):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"34 minus 4 is {d:.0f} distinct varieties no longer planted"


def q14(table, item):
    conv = [cg.cell(table, f, GE_DAMAGE) for f in CONV]
    eng = [cg.cell(table, f, GE_DAMAGE) for f in ENG]
    assert max(eng) < min(conv), f"the engineered fields {eng} must fall below the conventional {conv}"
    assert min(eng) > 0, "'no pest damage at all' must be false for the engineered fields"
    assert max(eng) * 2 < min(conv), "the gap must be large enough to call 'much less'"
    return (f"the engineered fields read {eng} percent damage against {conv} for the "
            "conventional fields, both engineered values below both conventional ones")


def q16(table, item):
    v = cg.col(table, DOSE)
    assert cg.cell(table, "Year 1", DOSE) == min(v), "the first year must need the smallest dose"
    assert all(v[i] < v[i + 1] for i in range(len(v) - 1)), f"the dose must rise; got {v}"
    return f"the tabulated doses are {v} grams per hectare, rising with no reversal"


def q17(table, item):
    base = cg.cell(table, "Year 1", DOSE)
    assert base > 0, "the first dose must be non-zero for a ratio to exist"
    r = cg.cell(table, "Year 12", DOSE) / base
    assert r == 14, f"the ratio recomputes to {r}, not 14"
    for wrong in (4, 20, 6, 1):
        assert r != wrong, f"the {wrong} distractor equals the key"
    return f"560 divided by 40 is {r:.0f} times the first year's dose"


def q19(table, item):
    pairs = sorted(zip(cg.col(table, GROWN), cg.col(table, LOST)))
    assert cg.cell(table, "District L", GROWN) == min(cg.col(table, GROWN)), \
        "District L must grow the fewest varieties"
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"the share lost must fall as varieties rise; got {pairs}"
    assert len(set(cg.col(table, LOST))) > 1, "'the same share in all three' must be false"
    return (f"sorted by varieties grown the shares lost are {[s for _, s in pairs]} percent, "
            "falling as the number of varieties rises")


def q20(table, item):
    g = dict(zip(cg.labels(table), cg.col(table, GROWN)))
    l = dict(zip(cg.labels(table), cg.col(table, LOST)))
    fewest, most = min(g, key=g.get), max(g, key=g.get)
    d = l[fewest] - l[most]
    assert d == 54, f"the difference recomputes to {d}, not 54"
    for wrong in (61, 37, 17, 68):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"61 minus 7 is {d:.0f} percentage points more of the crop lost"


def q28(table, item):
    v = cg.col(table, SURV)
    steps = [v[i + 1] - v[i] for i in range(len(v) - 1)]
    assert steps == [13, 31, 34], f"the interval rises recompute to {steps}, not 13, 31 and 34"
    assert max(steps) == steps[-1], "the largest rise must fall in the final interval"
    assert len(set(steps)) == 3, "'the three intervals show equal growth' must be false"
    return (f"the three interval rises are {steps} percentage points, largest between the "
            "tenth and the fifteenth generation")


CLAIMS = [
 ("herbicides, fungicides, rodenticides",
  "EIN-2.G.1 names pesticides, herbicides, fungicides, rodenticides, and insecticides as common pest-control methods. The rejected groups are STB-1.E.1's soil conservation methods, EIN-2.E.2's irrigation types, EIN-2.H.1's meat production methods, and STB-1.G's forestry methods."),
 ("Artificial selection",
  "EIN-2.G.1 states that organisms can become resistant to common pest-control methods THROUGH ARTIFICIAL SELECTION. The framework names the process, so the option denying that it does is wrong on its face."),
 ("decreases crop damage by pests and increases crop yields",
  "EIN-2.G.1 ends by stating that pest control decreases crop damage by pest and increases crop yields. Each rejected option reverses one of the two effects, drops one, or substitutes benefits the framework does not claim."),
 ("A rising share of the population survives",
  "Recomputed in q4 above: survival shares of 4, 17, 48 and 82 percent under a fixed dose. EIN-2.G.1 attributes resistance to common pest-control methods to artificial selection, and this is that resistance in the field."),
 ("78 percentage points",
  "Recomputed in q5 above: 82 minus 4 percentage points. The rejected values quote the final share alone, pair the wrong generations, or add the two."),
 ("leaves those that can to reproduce",
  "EIN-2.G.1 attributes resistance to ARTIFICIAL SELECTION, which is selection by human action over which individuals survive to reproduce. The rejected options describe change within one lifetime, transfer from the crop, or no selection at all."),
 ("suffered less damage and produced more crop",
  "Recomputed in q7 above: 9 percent damage against 38, and 4.8 tonnes per hectare against 2.4. EIN-2.G.1 states that pest control decreases crop damage by pest and increases crop yields."),
 ("Twice as much",
  "Recomputed in q8 above: 4.8 divided by 2.4. The rejected values invert the ratio, use the damage column, or deny the two differ."),
 ("A reduction of 29 percentage points",
  "Recomputed in q9 above: 38 minus 9 percentage points of the crop damaged. The rejected values quote one share alone or add them."),
 ("crop's resistance to pests and diseases",
  "EIN-2.G.2 states that crops can be genetically engineered to increase THEIR resistance to pests and diseases. The rejected option about the pests' resistance describes EIN-2.G.1 instead, where the resistance belongs to the organism being controlled."),
 ("loss of genetic diversity of that particular crop",
  "EIN-2.G.2, near verbatim: using genetically engineered crops in planting or other ways can lead to loss of genetic diversity of that particular crop. That is narrower than every species in a region, and the framework does record a drawback."),
 ("number of distinct varieties fell",
  "Recomputed in q12 above: varieties of 34, 11 and 4 against a leading variety share of 12, 58 and 86 percent. EIN-2.G.2 names loss of genetic diversity of that particular crop as a consequence of using engineered crops."),
 ("30 varieties",
  "Recomputed in q13 above: 34 minus 4 distinct varieties. The rejected values quote the opening count alone, pair the wrong periods, or add the two."),
 ("engineered variety showed much less pest damage",
  "Recomputed in q14 above: 6 and 8 percent damage against 31 and 27, with neither engineered field at zero. EIN-2.G.2 states that crops can be genetically engineered to increase their resistance to pests and diseases."),
 ("become resistant to common pest-control methods",
  "EIN-2.G.1 names resistance through artificial selection as a consequence of USING the control method, so applying it more often is the pressure that produces the problem rather than a way round it. The rejected statements are real framework claims that say nothing about how long a chemical keeps working."),
 ("the same effect required more chemical",
  "Recomputed in q16 above: doses of 40, 90, 220 and 560 grams per hectare for the same kill. EIN-2.G.1 attributes resistance to common pest-control methods to artificial selection, and a rising dose is that resistance measured a second way."),
 ("Fourteen times as much",
  "Recomputed in q17 above: 560 divided by 40 grams per hectare. The rejected values come from other pairs of years or deny the dose changed."),
 ("engineered crop is made resistant to the pest",
  "EIN-2.G.1 makes the resistance a property the ORGANISM being controlled acquires to the control method, and EIN-2.G.2 makes the resistance a property engineered into the CROP against pests and diseases. They are different traits in different organisms."),
 ("fewer distinct varieties lost a larger share",
  "Recomputed in q19 above: varieties of 22, 9 and 3 against shares lost of 7, 24 and 61 percent. EIN-2.G.2 names loss of genetic diversity of a particular crop as a consequence of using engineered crops, and these data are why that loss matters."),
 ("54 percentage points larger",
  "Recomputed in q20 above: 61 minus 7 percentage points between the districts growing fewest and most varieties. The rejected values quote one share alone, pair the wrong districts, or add them."),
 ("survives the same application of the same chemical",
  "EIN-2.G.1 makes resistance a change in the organisms' ability to survive the control method, so the diagnostic comparison holds the chemical and the dose fixed and watches survival over generations. The rejected observations each vary something else."),
 ("can lead to loss of genetic diversity",
  "EIN-2.G.2 concedes the engineered resistance and then adds that planting engineered crops can lead to loss of genetic diversity of that particular crop, which is the cost of planting one variety everywhere. The rejected statements support the company's case or belong to other topics."),
 ("less crop damage and a larger harvest",
  "EIN-2.G.1 carries both sides in one statement: resistance through artificial selection as the consequence, and decreased crop damage with increased yields as the benefit. Loss of genetic diversity belongs to engineered crops in EIN-2.G.2 rather than to chemicals."),
 ("surviving the treatment over successive generations",
  "EIN-2.G.1 claims a benefit, less damage and higher yields, and a consequence, resistance through artificial selection, so testing both needs a yield comparison and a survival trend. Each rejected pair measures at most one of the two."),
 ("dose of the chemical needed to achieve the same reduction",
  "EIN-2.G.1 names resistance through artificial selection as the process at issue, and a rising dose for the same effect measures it directly. Total harvest, equipment ownership, irrigated area and permitted days each leave the resistance unmeasured."),
 ("Each pairs a benefit with a drawback",
  "EIN-2.G.1 pairs resistance through artificial selection with decreased crop damage and increased yields, and EIN-2.G.2 pairs engineered resistance with loss of genetic diversity of that crop. Both statements carry one of each, which is what the learning objective's phrase benefits and drawbacks asks for."),
 ("can lead to LOSS of genetic diversity",
  "EIN-2.G.2 states that using genetically engineered crops can lead to LOSS of genetic diversity of that particular crop, so the direction in the student's sentence is reversed. The framework does address diversity here and limits the claim to the one crop."),
 ("Between the tenth and the fifteenth generation",
  "Recomputed in q28 above: interval rises of 13, 31 and 34 percentage points, largest in the final interval. Two rejected options report a smaller interval correctly but do not answer which is largest."),
 ("weed population that survives a herbicide more often each year is showing the resistance",
  "EIN-2.G.1 names herbicides among the common pest-control methods and attributes resistance in the target organisms to artificial selection, which is the weed case exactly. The rejected applications swap the two kinds of resistance or reverse a stated effect."),
 ("but selects for resistant organisms",
  "EIN-2.G.1 supplies the resistance consequence together with decreased damage and increased yields, and EIN-2.G.2 supplies engineered resistance together with loss of genetic diversity of that particular crop. The keyed summary carries all four claims."),
]

TABLE_CHECKS = {4: q4, 5: q5, 7: q7, 8: q8, 9: q9, 12: q12, 13: q13, 14: q14, 16: q16,
                17: q17, 19: q19, 20: q20, 28: q28}

e_check.run(e5_6, CLAIMS, TABLE_CHECKS)
