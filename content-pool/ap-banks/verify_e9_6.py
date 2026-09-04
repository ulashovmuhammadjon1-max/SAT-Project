"""Key audit for AP ENVIRONMENTAL SCIENCE 9.6 Ocean Warming.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
  STB-4.G.1  ocean warming is caused by the increase in greenhouse gases in the
             atmosphere -- items 1, 10, 12, 13, 17, 18, 30
  STB-4.G.2  ocean warming can affect marine species in a variety of ways,
             including loss of habitat, and metabolic and reproductive changes
                 -- items 2, 3, 7, 10, 14, 15, 16, 26, 27, 28, 29, 30
  STB-4.G.3  ocean warming is causing coral bleaching, which occurs when the
             loss of algae within corals cause the corals to bleach white; some
             corals recover and some die
                 -- items 4, 5, 6, 8, 9, 10, 11, 19, 20, 21, 22, 23, 24, 25, 30

WARMING AND ACIDIFICATION ARE DIFFERENT MECHANISMS, AND THAT IS THE DEFECT THIS
MODULE IS BUILT TO AVOID. STB-4.G.3 makes bleaching the LOSS OF ALGAE within the
coral under warming; STB-4.H.4, which belongs to topic 9.7, makes acidification
damage coral by the LOSS OF CALCIUM CARBONATE that leaves it difficult to form
shells. Items 5, 9, 11 and 30 each put the two accounts in front of the student
with one distractor swapping them, and every anchor on those items carries BOTH
the process AND its mechanism. An anchor naming only "bleaching" or only "the
loss of algae" would match the swapped distractor exactly as well as the key --
that is the failure already found once in this subject's banks.

WHAT IS DELIBERATELY NOT KEYED. STB-4.G.1 gives one cause and no chain of steps
from the atmosphere to the water, so no item asks how the heat arrives.
STB-4.G.2 says "in a variety of ways, INCLUDING", so no key treats its three
effects as exhaustive; item 7 keys that hedge. STB-4.G.3 gives no proportion
for recovery or death, so no key states one -- item 8 refuses a share and the
data item 23 reads its shares from the record rather than from the framework.

NO FIGURE IS REFERENCED; ``e_check.no_figure_reference`` enforces that on every
run.

DATA ITEMS: 17 to 29 carry tables, each recomputed below from that table alone.

NEGATIVE CONTROLS run on every invocation through ``e_check.run``; ``--selftest``
adds ``es_check.selftest``, which rotates all thirty keys one at a time and
corrupts every cell of every table individually.
"""
import sys

import cg_check as cg
import e_check
import es_check as es

import e9_6

GHG = "Atmospheric greenhouse gases (carbon dioxide equivalent, parts per million)"
OCEAN = "Mean temperature of the upper ocean (degrees Celsius)"
SST = "Mean summer sea surface temperature (degrees Celsius)"
BLEACHED = "Percent of coral colonies bleached white"
RECOVERED = "Percent of the bleached colonies that recovered"
DIED = "Percent of the bleached colonies that died"
ALGAE = "Algae remaining within the coral tissue (percent of the original)"
WHITE = "Percent of the colony that appears white"
OXYGEN = "Oxygen consumed by one fish (milligrams per hour)"
EGGS = "Eggs produced by one female in the season"
TOLERANCE = "Warmest water it can occupy (degrees Celsius)"
RANGE = "Percent of its former range still cool enough for it"


def _rising(values):
    return all(values[i + 1] > values[i] for i in range(len(values) - 1))


def _falling(values):
    return all(values[i + 1] < values[i] for i in range(len(values) - 1))


def q17(table, item):
    ghg = cg.col(table, GHG)
    ocean = cg.col(table, OCEAN)
    assert _rising(ghg), f"the greenhouse gases must rise at every decade; got {ghg}"
    assert _rising(ocean), f"the ocean temperature must rise at every decade; got {ocean}"
    return (f"in decade order the greenhouse gases read {ghg} parts per million and the "
            f"upper ocean {ocean} degrees, both rising at every step")


def q18(table, item):
    ocean = cg.col(table, OCEAN)
    rise = ocean[-1] - ocean[0]
    assert abs(rise - 0.62) < 1e-9, f"the ocean must warm by 0.62 degrees; got {rise}"
    assert rise > 0, "the movement must be a warming rather than a cooling"
    return (f"the upper ocean runs from {ocean[0]} to {ocean[-1]} degrees, a rise of "
            f"{rise:.2f}")


def q19(table, item):
    pairs = sorted(zip(cg.col(table, SST), cg.col(table, BLEACHED)))
    shares = [b for _, b in pairs]
    assert _rising(shares), \
        f"the bleached share must rise with the sea surface temperature; got {pairs}"
    assert len(set(shares)) == len(shares), "'every reef shows the same share' must be false"
    return (f"sorted by summer sea surface temperature the bleached shares read {shares} "
            "percent, strictly rising")


def q20(table, item):
    labels = cg.labels(table)
    sst = cg.col(table, SST)
    bleached = cg.col(table, BLEACHED)
    top = max(range(len(sst)), key=lambda i: sst[i])
    assert top == max(range(len(bleached)), key=lambda i: bleached[i]), \
        "the warmest reef must also be the most bleached"
    assert labels[top] == "Reef 4", f"that reef must be Reef 4; got {labels[top]}"
    return (f"{labels[top]} records the warmest summer water, {sst[top]} degrees, and the "
            f"largest bleached share, {bleached[top]:.0f} percent")


def q21(table, item):
    sst = cg.col(table, SST)
    bleached = cg.col(table, BLEACHED)
    most = max(range(len(bleached)), key=lambda i: bleached[i])
    least = min(range(len(bleached)), key=lambda i: bleached[i])
    gap = sst[most] - sst[least]
    assert abs(gap - 3.9) < 1e-9, f"the temperature gap must be 3.9 degrees; got {gap}"
    assert gap > 0, "the most bleached reef must be the warmer of the two"
    return (f"the most bleached reef sits at {sst[most]} degrees and the least bleached at "
            f"{sst[least]}, a gap of {gap:.1f}")


def q22(table, item):
    labels = cg.labels(table)
    recovered = cg.col(table, RECOVERED)
    died = cg.col(table, DIED)
    for lab, r, d in zip(labels, recovered, died):
        assert r > 0, f"{lab} must record some recovery; got {r}"
        assert d > 0, f"{lab} must record some death; got {d}"
        assert abs(r + d - 100) < 1e-9, \
            f"{lab}'s two shares must account for all the bleached colonies; got {r} and {d}"
    return (f"at every reef the recovered share {recovered} and the dead share {died} are "
            "both above zero and together account for the whole of the bleached colonies")


def q23(table, item):
    labels = cg.labels(table)
    died = cg.col(table, DIED)
    worst = max(range(len(died)), key=lambda i: died[i])
    assert labels[worst] == "Reef D", f"the largest loss must be Reef D's; got {labels[worst]}"
    assert len([d for d in died if d == died[worst]]) == 1, "that largest loss must be unique"
    assert len(set(died)) == len(died), "'all four lost the same share' must be false"
    return (f"the shares dying read {died} percent, whose single largest belongs to "
            f"{labels[worst]}")


def q24(table, item):
    pairs = sorted(zip(cg.col(table, ALGAE), cg.col(table, WHITE)))
    whites = [w for _, w in pairs]
    assert _falling(whites), \
        f"the white share must fall as the algae remaining rises; got {pairs}"
    algae = cg.col(table, ALGAE)
    assert len(set(algae)) == len(algae), "'every colony retains the same share' must be false"
    return (f"sorted by the algae remaining, the share appearing white reads {whites} "
            "percent, strictly falling")


def q25(table, item):
    labels = cg.labels(table)
    algae = cg.col(table, ALGAE)
    white = cg.col(table, WHITE)
    most_algae = max(range(len(algae)), key=lambda i: algae[i])
    least_white = min(range(len(white)), key=lambda i: white[i])
    assert most_algae == least_white, \
        "the colony keeping most algae must be the one appearing least white"
    assert labels[most_algae] == "Colony 1", \
        f"that colony must be Colony 1; got {labels[most_algae]}"
    return (f"{labels[most_algae]} retains {algae[most_algae]:.0f} percent of its algae, "
            f"the most in the record, and appears {white[most_algae]:.0f} percent white, "
            "the least")


def q26(table, item):
    temps = [float(lab) for lab in cg.labels(table)]
    assert _rising(temps), f"the rows must run from cool to warm; got {temps}"
    oxygen = cg.col(table, OXYGEN)
    eggs = cg.col(table, EGGS)
    assert _rising(oxygen), f"the oxygen used must rise with temperature; got {oxygen}"
    assert _falling(eggs), f"the eggs produced must fall with temperature; got {eggs}"
    return (f"from {temps[0]:.0f} to {temps[-1]:.0f} degrees the oxygen used reads "
            f"{oxygen} milligrams an hour, rising, while the eggs read {eggs}, falling")


def q27(table, item):
    temps = [float(lab) for lab in cg.labels(table)]
    assert _rising(temps), f"the rows must run from cool to warm; got {temps}"
    eggs = cg.col(table, EGGS)
    drop = eggs[0] - eggs[-1]
    assert abs(drop - 1390) < 1e-9, f"the fall must be 1,390 eggs; got {drop}"
    assert drop > 0, "the movement must be a fall rather than a rise"
    return (f"the eggs produced run from {eggs[0]:.0f} at the coolest temperature to "
            f"{eggs[-1]:.0f} at the warmest, a fall of {drop:.0f}")


def q28(table, item):
    pairs = sorted(zip(cg.col(table, TOLERANCE), cg.col(table, RANGE)))
    kept = [r for _, r in pairs]
    assert _rising(kept), \
        f"the range kept must rise with the warmth a species can bear; got {pairs}"
    assert len(set(kept)) == len(kept), "'every species kept the same share' must be false"
    assert all(r < 100 for r in kept), "'every species kept all its range' must be false"
    return (f"sorted by the warmest water each species can occupy, the share of former "
            f"range still cool enough reads {kept} percent, strictly rising")


def q29(table, item):
    labels = cg.labels(table)
    tolerance = cg.col(table, TOLERANCE)
    kept = cg.col(table, RANGE)
    worst = min(range(len(kept)), key=lambda i: kept[i])
    assert worst == min(range(len(tolerance)), key=lambda i: tolerance[i]), \
        "the species keeping least range must be the one bearing least warmth"
    assert labels[worst] == "Species 1", \
        f"that species must be Species 1; got {labels[worst]}"
    assert len(set(kept)) == len(kept), "'all four kept the same share' must be false"
    return (f"{labels[worst]} bears the least warmth, {tolerance[worst]:.0f} degrees, and "
            f"keeps the smallest share of its former range, {kept[worst]:.0f} percent")


CLAIMS = [
 ("increase in greenhouse gases in the atmosphere",
  "STB-4.G.1, near verbatim: ocean warming is caused by the increase in greenhouse gases in the atmosphere. A fall in seawater pH belongs to the framework's separate statement on acidification, and the loss of algae is what bleaching is rather than what warms the water."),
 ("Loss of habitat, and metabolic and reproductive changes",
  "STB-4.G.2, near verbatim: ocean warming can affect marine species in a variety of ways, including loss of habitat, and metabolic and reproductive changes. Each rejected option drops two of the three or substitutes salinity, which the statement never names."),
 ("change in the salinity of the water they occupy",
  "STB-4.G.2 names loss of habitat and metabolic and reproductive changes, which the four rejected options restate in one wording or another. Salinity appears nowhere in this topic's statements."),
 ("Coral bleaching",
  "STB-4.G.3 states that ocean warming is causing coral bleaching, and attributes no other change in corals to warming."),
 ("loss of algae from within the corals causes the corals to bleach white",
  "STB-4.G.3, near verbatim: coral bleaching occurs when the loss of algae within corals cause the corals to bleach white. The anchor carries the mechanism as well as the outcome, because the rejected option keeps the outcome and substitutes the calcium carbonate mechanism that STB-4.H.4 gives for acidification."),
 ("Some recover and some die",
  "STB-4.G.3 ends by stating that some corals recover and some die, so the framework commits to neither outcome for all of them and gives no share for either."),
 ("examples rather than a complete list",
  "The phrase A VARIETY OF WAYS, INCLUDING in STB-4.G.2 marks the three named effects as instances rather than an exhaustive set, so the framework neither closes the list nor narrows it to one species."),
 ("some bleached corals recover and some die",
  "STB-4.G.3 states that some corals recover and some die, so a claim that all of them die closes an outcome the framework leaves open. The framework also supplies no share for either outcome."),
 ("loss of algae within the corals; the difficulty in forming shells through the loss of calcium carbonate is what the framework attributes to acidification",
  "STB-4.G.3 defines bleaching as the loss of algae within corals under warming, while STB-4.H.4 attributes the difficulty in forming shells, through the loss of calcium carbonate, to acidification. The anchor carries both halves because one rejected option is that sentence with the two mechanisms exchanged."),
 ("caused by a fall in the pH of seawater",
  "STB-4.G.1, STB-4.G.2 and STB-4.G.3 supply the four rejected statements between them. STB-4.G.1 names the increase in atmospheric greenhouse gases as the cause of warming, and a fall in pH belongs to the framework's separate account of acidification."),
 ("Warming causes bleaching through the loss of algae; acidification makes it difficult to form shells",
  "STB-4.G.3 attributes bleaching, the loss of algae within corals, to ocean warming, and STB-4.H.4 attributes the difficulty in forming shells, through the loss of calcium carbonate, to ocean acidification. The anchor names both processes with their own mechanisms, because the rejected option exchanges them."),
 ("caused by the increase in greenhouse gases in the atmosphere",
  "STB-4.G.1 is the only statement in this topic reaching from the atmosphere to the water, so a report of rising atmospheric greenhouse gases connects to the ocean through it."),
 ("atmospheric greenhouse gases and of ocean temperature over the same years",
  "STB-4.G.1 asserts a cause running from atmospheric greenhouse gases to ocean warming, so the evidence bearing on it follows both quantities over the same period rather than either alone or a single reading."),
 ("A reproductive change",
  "STB-4.G.2 names reproductive changes among the ways ocean warming can affect marine species, and a fall in the eggs produced each season is a change in reproduction rather than in habitat or in body chemistry."),
 ("A metabolic change",
  "STB-4.G.2 names metabolic changes among the ways ocean warming can affect marine species, and a change in the rate at which an animal uses oxygen and energy is a change in metabolism."),
 ("A loss of habitat",
  "STB-4.G.2 names loss of habitat among the ways ocean warming can affect marine species, and water that has become too warm to occupy is habitat lost rather than a change within the animal."),
 ("Both rise at every successive decade",
  "Recomputed in q17 above: in decade order each greenhouse gas reading and each ocean temperature exceeds the one before it. STB-4.G.1 states that ocean warming is caused by the increase in greenhouse gases in the atmosphere."),
 ("By 0.62 degrees Celsius",
  "Recomputed in q18 above: the first and last entries of the ocean temperature column differ by 0.62 degrees, upward. STB-4.G.1 makes that warming the effect the framework attributes to rising atmospheric greenhouse gases."),
 ("the larger the share of its colonies bleached white",
  "Recomputed in q19 above: sorting the reefs by summer sea surface temperature leaves the bleached share strictly rising, with no ties. STB-4.G.3 states that ocean warming is causing coral bleaching."),
 ("Reef 4",
  "Recomputed in q20 above: the warmest summer water and the largest bleached share fall in the same row. STB-4.G.3 attributes coral bleaching to ocean warming."),
 ("3.9 degrees Celsius warmer",
  "Recomputed in q21 above: the reefs with the largest and smallest bleached shares differ by 3.9 degrees in summer water temperature, the more bleached being the warmer. STB-4.G.3 ties bleaching to warming, which is what makes that the relevant comparison."),
 ("At every reef some of the bleached colonies recovered and some died",
  "Recomputed in q22 above: at each of the four reefs both shares stand above zero and together account for the whole of the bleached colonies. STB-4.G.3 states that some corals recover and some die."),
 ("Reef D",
  "Recomputed in q23 above: the largest share dying belongs to one reef alone and the four shares differ. STB-4.G.3 gives no proportion for either outcome, so the shares are read from the record."),
 ("lost the most algae are the colonies that appear whitest",
  "Recomputed in q24 above: sorting the colonies by algae remaining leaves the white share strictly falling. STB-4.G.3 states that bleaching occurs when the loss of algae within corals causes the corals to bleach white."),
 ("Colony 1",
  "Recomputed in q25 above: the largest algae figure and the smallest white figure fall in the same row, which is the pairing STB-4.G.3's account of bleaching predicts."),
 ("uses more oxygen and the females produce fewer eggs",
  "Recomputed in q26 above: as the temperature rises the oxygen used rises at every step and the eggs produced fall at every step. STB-4.G.2 names both metabolic and reproductive changes among the effects of ocean warming on marine species."),
 ("By 1,390 eggs",
  "Recomputed in q27 above: the entries at the coolest and warmest temperatures in the egg column differ by 1,390, downward. STB-4.G.2 names reproductive changes among the effects of ocean warming."),
 ("bear the least warmth have kept the least of their former range",
  "Recomputed in q28 above: sorting the species by the warmest water each can occupy leaves the share of range still cool enough strictly rising, and no species retains all of its range. STB-4.G.2 names loss of habitat among the ways ocean warming affects marine species."),
 ("Species 1, which can bear the least warmth of the four",
  "Recomputed in q29 above: the smallest range figure and the smallest temperature tolerance fall in the same row, and the four shares differ. STB-4.G.2 names loss of habitat among the effects of ocean warming."),
 ("coral bleaching, the loss of algae within corals, after which some corals recover and some die",
  "STB-4.G.1 supplies the cause, STB-4.G.2 the three named kinds of effect within a variety of ways, and STB-4.G.3 the bleaching, its mechanism in the loss of algae, and the split outcome afterwards. The rejected summaries substitute a pH cause, close the list of effects, promise one outcome for every bleached coral, or exchange the warming and acidification mechanisms."),
]

TABLE_CHECKS = {17: q17, 18: q18, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23,
                24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29}

if "--selftest" in sys.argv:
    es.selftest(e9_6, CLAIMS, TABLE_CHECKS)

e_check.run(e9_6, CLAIMS, TABLE_CHECKS)
