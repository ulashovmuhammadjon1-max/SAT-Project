"""Key audit for AP ENVIRONMENTAL SCIENCE 5.1 The Tragedy of the Commons.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor, so an off-by-one key or a reordered choice
list fails here rather than reaching a student.

WHAT THE KEYS REST ON
---------------------
The whole topic is EIN-2.A.1: the tragedy of the commons suggests that
individuals will use SHARED resources in their own SELF-INTEREST rather than in
keeping with the common good, THEREBY DEPLETING the resources. Every key turns
on one of those three parts or on their combination:

  the resource must be shared      -- items 2, 9, 17, 20, 24, 28
  use follows private benefit      -- items 6, 7, 8, 13, 16, 18, 23, 26
  the consequence is depletion     -- items 3, 4, 5, 10, 11, 12, 14, 15, 19,
                                      21, 22, 25, 27, 29, 30
  the framework's own hedge, that the concept SUGGESTS rather than guarantees
  the pattern                      -- item 21

No key here proposes a remedy, names an author or a historical case, or claims
the outcome is inevitable, because the framework does none of those in 5.1.

DATA ITEMS: 4, 5, 7, 8, 10, 11, 12, 14, 15, 27 and 29 carry tables. Each keyed
conclusion is recomputed below from that table alone, and each check anchors at
least one assertion to a named row, because reversing two columns together
preserves the pairing between them.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs.
"""
import e_check
import cg_check as cg
import e5_1

HH_WOOD = "Number of households cutting firewood from the shared woodlot"
TIMBER = "Standing timber remaining in the woodlot (tonnes)"
WELLS = "Number of wells drawing on the shared aquifer"
DEPTH = "Depth to the water table (meters)"
INCOME = "Extra income to that herder over the season (units)"
FORAGE = "Loss of forage spread across all forty herders (units)"
YIELD = "Oysters harvested per hectare in the tenth year (kilograms)"
FRUIT = "Fruit taken by the village in total (kilograms)"
HH_FRUIT = "Number of households taking fruit"

OPEN_BEDS = ["Bed 1", "Bed 2"]
LIMITED_BEDS = ["Bed 3", "Bed 4"]


def q4(table, item):
    hh = cg.col(table, HH_WOOD)
    tim = cg.col(table, TIMBER)
    assert cg.cell(table, "Year 1", HH_WOOD) == min(hh), "Year 1 must have the fewest households"
    assert all(hh[i] < hh[i + 1] for i in range(len(hh) - 1)), f"households must rise; got {hh}"
    assert all(tim[i] > tim[i + 1] for i in range(len(tim) - 1)), f"timber must fall; got {tim}"
    assert tim[0] > 0, "'already zero when the record began' must be false"
    return (f"households run {hh} while standing timber runs {tim} tonnes, rising and falling "
            "respectively with no reversal in either column")


def q5(table, item):
    d = cg.cell(table, "Year 1", TIMBER) - cg.cell(table, "Year 10", TIMBER)
    assert d == 820, f"the loss recomputes to {d}, not 820"
    for wrong in (980, 530, 160, 1140):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"980 minus 160 is {d:.0f} tonnes of standing timber lost over the record"


def q7(table, item):
    assert cg.cell(table, "Add no extra animal", INCOME) == 0, \
        "the do-nothing row must carry no extra income"
    for lab in ("Add one extra animal", "Add four extra animals"):
        gain = cg.cell(table, lab, INCOME)
        loss = cg.cell(table, lab, FORAGE)
        assert gain == loss, f"{lab}: the group loss {loss} should match the private gain {gain}"
        assert gain / 40.0 < gain, "the herder's share of the loss must be smaller than the gain"
    return ("for each row the private gain equals the group loss, so the herder's own share of "
            "that loss is one fortieth of what the herder keeps")


def q8(table, item):
    gain = cg.cell(table, "Add four extra animals", INCOME)
    loss = cg.cell(table, "Add four extra animals", FORAGE)
    share = loss / 40.0
    assert gain == 160, f"the extra income recomputes to {gain}, not 160"
    assert share == 4, f"the herder's share recomputes to {share}, not 4"
    assert share != gain, "'160 units of loss to that herder' must be false"
    return f"160 units of income against {loss:.0f} units of loss spread over forty herders, or {share:.0f} each"


def q10(table, item):
    w = cg.col(table, WELLS)
    d = cg.col(table, DEPTH)
    assert cg.cell(table, "Year 1", WELLS) == min(w), "Year 1 must have the fewest wells"
    assert all(w[i] < w[i + 1] for i in range(len(w) - 1)), f"wells must rise; got {w}"
    assert all(d[i] < d[i + 1] for i in range(len(d) - 1)), f"depth to water must grow; got {d}"
    return (f"wells run {w} while the depth to water runs {d} meters, both rising without "
            "a reversal, so less water lies within reach as more users draw on it")


def q11(table, item):
    d = cg.cell(table, "Year 13", DEPTH) - cg.cell(table, "Year 1", DEPTH)
    assert d == 46, f"the increase recomputes to {d}, not 46"
    for wrong in (68, 37, 21, 90):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"68 minus 22 is {d:.0f} meters of additional depth to the water table"


def q12(table, item):
    yields = {lab: cg.cell(table, lab, YIELD) for lab in cg.labels(table)}
    opened = [yields[b] for b in OPEN_BEDS]
    limited = [yields[b] for b in LIMITED_BEDS]
    assert max(opened) < min(limited), \
        f"the open beds {opened} must all fall below the limited beds {limited}"
    assert min(limited) > 0, "'the limited beds yielded nothing' must be false"
    assert max(opened) * 2 < min(limited), "the gap must be large enough to call 'far less'"
    return (f"the open beds returned {opened} kilograms per hectare against {limited} for the "
            "beds under an enforced limit, a gap of more than a factor of two")


def q14(table, item):
    hh = dict(zip(cg.labels(table), cg.col(table, HH_FRUIT)))
    tot = dict(zip(cg.labels(table), cg.col(table, FRUIT)))
    assert max(hh, key=hh.get) == "Season 4", "the last season must have the most households"
    seasons = cg.labels(table)
    hs = [hh[s] for s in seasons]
    assert all(hs[i] < hs[i + 1] for i in range(len(hs) - 1)), f"households must keep rising; got {hs}"
    ts = [tot[s] for s in seasons]
    assert max(ts) == tot["Season 3"], "the total must peak in the third season"
    assert ts[-1] < ts[-2], "the total must fall in the final season"
    return (f"households run {hs} while the totals run {ts} kilograms, so the total peaks in "
            "the third season and falls in the fourth despite the largest number of users")


def q15(table, item):
    per = cg.cell(table, "Season 4", FRUIT) / cg.cell(table, "Season 4", HH_FRUIT)
    assert per == 20, f"the per-household share recomputes to {per}, not 20"
    for wrong in (80, 45, 120, 1600):
        assert per != wrong, f"the {wrong} distractor equals the key"
    return f"1,600 kilograms divided among 80 households is {per:.0f} kilograms each"


def q27(table, item):
    yields = {lab: cg.cell(table, lab, YIELD) for lab in cg.labels(table)}
    open_avg = sum(yields[b] for b in OPEN_BEDS) / 2.0
    lim_avg = sum(yields[b] for b in LIMITED_BEDS) / 2.0
    d = lim_avg - open_avg
    assert open_avg == 150 and lim_avg == 600, \
        f"the two averages recompute to {open_avg} and {lim_avg}"
    assert d == 450, f"the gap recomputes to {d}, not 450"
    for wrong in (150, 600, 470, 750):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"an open-access average of {open_avg:.0f} against {lim_avg:.0f} leaves a gap of {d:.0f}"


def q29(table, item):
    w = cg.col(table, WELLS)
    d = cg.col(table, DEPTH)
    assert cg.cell(table, "Year 13", WELLS) == max(w), "the last year must have the most wells"
    assert w[-1] > w[0] and d[-1] > d[0], \
        f"wells must end higher and water must end deeper; got {w} and {d}"
    return (f"the wells rise from {w[0]:.0f} to {w[-1]:.0f} while the depth to water grows "
            f"from {d[0]:.0f} to {d[-1]:.0f} meters")


CLAIMS = [
 ("in their own self-interest rather than",
  "EIN-2.A.1, near verbatim: the tragedy of the commons suggests that individuals will use shared resources in their own self-interest rather than in keeping with the common good, thereby depleting the resources. The rejected options reverse the direction of the effect or add an ignorance condition the framework does not state."),
 ("It must be shared",
  "EIN-2.A.1 speaks of SHARED resources, and its conflict between self-interest and the common good has no purchase where one owner bears the whole cost of use. The framework attaches no condition about renewability, location or price."),
 ("depletion of the resource that follows",
  "EIN-2.A.1 names three things in order: shared use, self-interested behaviour, and the depletion that follows. A falling water table is the third of these, the outcome, and not the shared character of the aquifer or the motive of a user."),
 ("timber fell in every recorded",
  "Recomputed in q4 above: households rise from 12 to 44 while standing timber falls from 980 to 160 tonnes with no reversal in either column. EIN-2.A.1 describes shared use in each user's own interest thereby depleting the resource."),
 ("820",
  "Recomputed in q5 above from the first and last rows: 980 minus 160 tonnes. The rejected values quote one year alone, pair the wrong years, or add the two figures."),
 ("combined result harms everyone",
  "EIN-2.A.1 sets self-interest against the common good, which means the individually sensible choice and the collectively good choice come apart. The framework does not make the outcome depend on miscalculation, on force, or on users acting against their own interest."),
 ("bears only one fortieth",
  "Recomputed in q7 above: for each row the private gain equals the group loss, and that loss is spread over forty herders. This asymmetry between concentrated benefit and divided cost is the mechanism behind EIN-2.A.1."),
 ("160 units of income and 4 units",
  "Recomputed in q8 above: 160 units of income against 160 units of forage loss divided among forty herders, which is 4 units falling on the herder who added the animals."),
 ("only that landowner may enter",
  "EIN-2.A.1 applies to SHARED resources, so that one user's gain is drawn from something others also depend on. Where a single owner takes the whole benefit and bears the whole cost, the conflict the framework describes does not arise."),
 ("water table fell steadily",
  "Recomputed in q10 above: wells rise from 18 to 88 while the depth to water grows from 22 to 68 meters, so less water lies within reach as more users draw on it. EIN-2.A.1 describes shared resources depleted by self-interested use."),
 ("46 meters",
  "Recomputed in q11 above: 68 meters minus 22 meters. The rejected values quote the final depth alone, pair the wrong years, or add the two readings."),
 ("yielded far less in the tenth year",
  "Recomputed in q12 above: 140 and 160 kilograms per hectare on the open beds against 610 and 590 where harvest is limited and enforced. EIN-2.A.1 attributes depletion to shared resources used in each individual's own self-interest, and open access is what makes a resource shared in that sense."),
 ("without regard to what is best for all",
  "EIN-2.A.1 contrasts the individual's own self-interest with the common good, so the behaviour it names is choosing by the private benefit alone. Each rejected option describes a user who is already taking the common good into account."),
 ("stopped rising and then fell",
  "Recomputed in q14 above: households run 10, 20, 40 and 80 while the totals run 1,200, 1,600, 1,800 and 1,600 kilograms, so the total peaks in the third season and falls in the fourth. EIN-2.A.1 describes shared resources depleted by use in each user's own interest."),
 ("An average of 20 kilograms",
  "Recomputed in q15 above: 1,600 kilograms divided among 80 households. The rejected values come from another season, from the number of households, or from not dividing at all."),
 ("deliberate rather than careless",
  "EIN-2.A.1 says individuals use shared resources IN THEIR OWN SELF-INTEREST rather than in keeping with the common good, which describes purposeful choice. Carelessness, ignorance and error are different accounts and none appears in the statement."),
 ("each user choosing by their own benefit",
  "EIN-2.A.1 requires both a shared resource and self-interested use and states that the two together deplete the resource. Removing either condition removes the conflict between individual benefit and common good on which the concept rests."),
 ("bears the whole future cost",
  "EIN-2.A.1 turns on the gap between the private benefit of an extra unit taken and the shared cost of taking it, so concentrating benefit and cost in one owner closes that gap. The stem holds the profit motive constant, and the framework makes no claim about starting stocks."),
 ("falls year after year",
  "EIN-2.A.1 links many self-interested users of a shared resource to depletion, so the diagnostic sign is a falling return to each user as the number of users grows. A fenced single-user resource is not shared, and an agreed maximum is the common good being taken into account."),
 ("beneath the land of many separate owners",
  "EIN-2.A.1 applies to shared resources, and groundwater beneath many owners is drawn on by all of them so that each withdrawal reduces what remains for the rest. The rejected items are each used and paid for by one household."),
 ("suggests this pattern",
  "EIN-2.A.1 opens with the words the tragedy of the commons SUGGESTS, which is a claim about what the concept predicts rather than a guarantee about every shared resource. The framework attaches no threshold of users and no renewability condition."),
 ("because a shared resource was used",
  "The river is shared, each district chose by its own harvest, and the resource ran short, which are the three elements of EIN-2.A.1. A rain shadow is ENG-2.B.2, sustainable yield is STB-1.A.2 and describes the opposite behaviour, and salinization is EIN-2.F.6."),
 ("would not be borne out",
  "EIN-2.A.1 makes depletion follow from self-interested use of a shared resource, so removing the self-interested behaviour removes the framework's stated cause. The framework does not claim that sharing alone depletes a resource."),
 ("share of the loss that falls on that user",
  "A shared resource is drawn on by many, so a reduction caused by one user is spread across all of them, and that division of the cost is what makes self-interest point away from the common good in EIN-2.A.1."),
 ("open to all townspeople the number of animals has risen",
  "EIN-2.A.1 requires all three of a shared resource, use following each user's own interest, and depletion. Only the keyed option reports all three; each rejected option is missing the shared access, the rising use, or the falling condition of the resource."),
 ("restraint by one user costs",
  "EIN-2.A.1 sets the individual's self-interest against the common good, and the described situation is that conflict persisting even where the common good is understood. The rejected options replace the conflict with ignorance or with an assumption that dissolves it."),
 ("450 kilograms per hectare",
  "Recomputed in q27 above: an open-access average of 150 kilograms per hectare against 600 under an enforced limit. The rejected values are the two averages themselves, a wrong pairing, and the sum."),
 ("commonly shared among many users",
  "The enduring understanding EIN-2 states that when humans use natural resources they alter natural systems, and EIN-2.A.1 applies to shared resources, which pastures, forests, fisheries and groundwater commonly are. The rejected options deny that these resources can be depleted or that individuals choose about them."),
 ("water within reach of them fell",
  "Recomputed in q29 above: wells rising from 18 to 88 while the depth to water grows from 22 to 68 meters. EIN-2.A.1 attributes this joint movement to shared use in each user's own interest."),
 ("depletion is the result of the two together",
  "EIN-2.A.1 states that individuals will use SHARED resources in their own SELF-INTEREST rather than in keeping with the common good, THEREBY DEPLETING the resources, which orders the three as condition, behaviour and consequence."),
]

TABLE_CHECKS = {4: q4, 5: q5, 7: q7, 8: q8, 10: q10, 11: q11, 12: q12, 14: q14,
                15: q15, 27: q27, 29: q29}

e_check.run(e5_1, CLAIMS, TABLE_CHECKS)
