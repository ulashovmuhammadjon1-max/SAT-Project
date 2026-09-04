"""Key audit for AP ENVIRONMENTAL SCIENCE 8.14 Pollution and Human Health.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

THE OZONE SWAP. EIN-3.C.4 is about ELEVATED ozone in the TROPOSPHERE; STB-4.A.3
in topic 9.1 is about DEPLETED ozone in the STRATOSPHERE and attaches skin
cancer and cataracts to it. Items 5, 14 and 24 carry that swap as a distractor,
and each of those anchors below names BOTH the layer and the direction of the
change, so an anchor pinned to "ozone" or to "respiratory problems" alone
cannot pass. That is the error this course sees most often.

WHAT THE KEYS REST ON
---------------------
  EIN-3.C.1  establishing cause and effect between pollutants and human health
             issues is difficult because humans are exposed to a variety of
             chemicals and pollutants -- items 1, 7, 11, 12, 17, 18, 21, 25, 27;
  EIN-3.C.2  dysentery is caused by untreated sewage in streams and rivers --
             items 2, 3, 13, 20, 23, 26;
  EIN-3.C.3  mesothelioma is a type of cancer caused mainly by exposure to
             asbestos -- items 4, 6, 8, 15, 19, 21;
  EIN-3.C.4  respiratory problems and overall lung function can be impacted by
             elevated levels of tropospheric ozone -- items 5, 9, 10, 14, 16,
             22, 24, 28.
Items 29 and 30 join all four.

SCOPE. Pathogens and the diseases EIN-3.D.1 to EIN-3.D.12 names are keyed in
8.15; dysentery is not on that list and is keyed here. The stages of sewage
treatment are keyed in 8.11 and the formation of photochemical smog in 7.2; no
key here restates either.

NOT KEYED: no exposure limit, no incidence figure for a real place, no latency
period and no disease the framework does not attach to these pollutants.

DATA ITEMS: 3, 6, 9, 12, 16 and 20 carry tables and every keyed reading is
recomputed here from the table alone.

NEGATIVE CONTROL: `python3 verify_e8_14.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e8_14

DYS = "Dysentery cases per thousand people each year"
YEARS = "Years spent working with asbestos"
MESO = "Mesothelioma cases per hundred thousand people"
O3_DAY = "Ozone measured near the ground (parts per billion)"
VISITS = "Hospital visits for breathing problems"
NPOLL = "Number of different pollutants above background in their air and water"
ILL = "Respiratory illnesses reported per hundred people"
O3_TEST = "Ozone near the ground on the days of testing (parts per billion)"
LUNG = "Average lung function score"
SEWAGE = "Untreated sewage entering the river (millions of liters per day)"
DYS_TIME = "Dysentery cases reported per thousand people"


def q3(table, item):
    villages = cg.labels(table)
    treated = [str(r[1]).strip().lower() for r in table["rows"]]
    cases = cg.col(table, DYS)
    yes = [i for i, t in enumerate(treated) if t == "yes"]
    no = [i for i, t in enumerate(treated) if t == "no"]
    assert len(yes) == 2 and len(no) == 2, \
        f"the two treated and two untreated villages are not both present: {treated}"
    assert min(cases[i] for i in no) > 5 * max(cases[i] for i in yes), \
        f"the untreated villages are not many times higher: {cases}"
    assert min(cases) > 0, "'only one village reports any dysentery' must be false"
    return (f"the untreated villages {[villages[i] for i in no]} report "
            f"{[cases[i] for i in no]} against {[cases[i] for i in yes]} in the treated "
            "villages")


def q6(table, item):
    groups = cg.labels(table)
    years = cg.col(table, YEARS)
    rate = cg.col(table, MESO)
    order = [g for _, g in sorted(zip(years, groups))]
    assert order == [g for _, g in sorted(zip(rate, groups))], \
        f"the order by years worked does not match the order by case rate: {years} {rate}"
    assert rate[years.index(min(years))] == min(rate), \
        "'the group with no asbestos work has the highest rate' must be false"
    assert len(set(rate)) == len(rate), "'the same rate in all three' must be false"
    return (f"ranking the groups by years worked with asbestos gives {order}, the same "
            "order as ranking them by the case rate")


def q9(table, item):
    days = cg.labels(table)
    o3 = cg.col(table, O3_DAY)
    vis = cg.col(table, VISITS)
    order = [d for _, d in sorted(zip(o3, days))]
    assert order == [d for _, d in sorted(zip(vis, days))], \
        f"the order by ozone does not match the order by visits: {o3} {vis}"
    assert vis[o3.index(min(o3))] == min(vis), \
        "'the lowest ozone day carried the most visits' must be false"
    assert len(set(vis)) == len(vis), "'the same number of visits every day' must be false"
    return (f"ranking the days by ozone near the ground gives {order}, the same order as "
            "ranking them by hospital visits for breathing problems")


def q12(table, item):
    groups = cg.labels(table)
    n = cg.col(table, NPOLL)
    ill = cg.col(table, ILL)
    order = [g for _, g in sorted(zip(n, groups))]
    assert order == [g for _, g in sorted(zip(ill, groups))], \
        f"illness does not rise with the number of pollutants: {n} {ill}"
    assert all("pollutant" not in h.lower() or "number" in h.lower()
               for h in table["headers"][1:]), \
        "a column names a specific pollutant, which would let one be identified"
    assert min(n) >= 1, "some group is exposed to no pollutant at all"
    assert ill[n.index(max(n))] == max(ill), \
        "'the most exposed group reports the least illness' must be false"
    return (f"the table records only how many pollutants are elevated, {n}, and the "
            f"illness rates {ill} rise with that count, naming no individual pollutant")


def q16(table, item):
    groups = cg.labels(table)
    o3 = cg.col(table, O3_TEST)
    lung = cg.col(table, LUNG)
    order = [g for _, g in sorted(zip(o3, groups))]
    assert order == [g for _, g in sorted(zip(lung, groups), reverse=True)], \
        f"lung function does not run opposite to ozone: {o3} {lung}"
    assert lung[o3.index(max(o3))] == min(lung), \
        "the group tested on the highest ozone days is not the lowest scoring"
    assert lung[o3.index(min(o3))] == max(lung), \
        "'the cleanest days gave the lowest score' must be false"
    return (f"ranking the groups by ozone near the ground gives {order}, the reverse of "
            "the order by average lung function score")


def q20(table, item):
    periods = cg.labels(table)
    sew = cg.col(table, SEWAGE)
    dys = cg.col(table, DYS_TIME)
    before = [i for i, p in enumerate(periods) if p.strip().lower().endswith("before")]
    after = [i for i, p in enumerate(periods) if p.strip().lower().endswith("after")]
    assert len(before) == 2 and len(after) == 2, \
        f"there are not two rows before and two after: {periods}"
    assert min(sew[i] for i in before) > 3 * max(sew[i] for i in after), \
        f"the sewage entering the river did not fall sharply: {sew}"
    assert min(dys[i] for i in before) > 3 * max(dys[i] for i in after), \
        f"the dysentery cases did not fall sharply: {dys}"
    return (f"sewage runs {[sew[i] for i in before]} before and {[sew[i] for i in after]} "
            f"after, while dysentery runs {[dys[i] for i in before]} before and "
            f"{[dys[i] for i in after]} after")


CLAIMS = [
 ("exposure to a variety of chemicals and pollutants at the same time",
  "EIN-3.C.1 verbatim in substance: it can be difficult to establish a cause and effect between pollutants and human health issues because humans experience exposure to a variety of chemicals and pollutants. Each rejected option denies that difficulty or its stated reason."),
 ("Untreated sewage in streams and rivers",
  "EIN-3.C.2 verbatim: dysentery is caused by untreated sewage in streams and rivers. Asbestos is EIN-3.C.3, tropospheric ozone EIN-3.C.4, and metals and nutrients belong to other topics of this unit."),
 ("untreated report many times the dysentery of the villages whose sewage is treated",
  "Recomputed in q3 above: both untreated rows exceed five times either treated row, and no village reports zero. EIN-3.C.2 names untreated sewage in streams and rivers as the cause of dysentery."),
 ("Exposure to asbestos",
  "EIN-3.C.3 verbatim in substance: mesothelioma is a type of cancer caused mainly by exposure to asbestos. Sewage is EIN-3.C.2 and tropospheric ozone EIN-3.C.4."),
 ("from elevated levels of ozone in the troposphere near the ground",
  "EIN-3.C.4 states that respiratory problems and overall lung function can be impacted by elevated levels of tropospheric ozone. The swapped distractor moves the effect to depleted stratospheric ozone, which STB-4.A.3 links instead to skin cancer and cataracts, so the anchor carries both the layer and the direction."),
 ("longer a group worked with asbestos, the higher its rate",
  "Recomputed in q6 above: ranking the groups by years worked gives the same order as ranking them by case rate, and the group with none is lowest. EIN-3.C.3 attributes mesothelioma mainly to asbestos exposure."),
 ("difficult because humans are exposed to a variety of chemicals and pollutants",
  "EIN-3.C.1 gives simultaneous exposure to a variety of chemicals and pollutants as the reason cause and effect is hard to establish, which is the study's difficulty. The other statements each name one specific link."),
 ("Mesothelioma",
  "EIN-3.C.3 attributes mesothelioma mainly to exposure to asbestos, a mineral fiber, while EIN-3.C.2 attributes dysentery to a waterborne cause and EIN-3.C.4 attributes respiratory effects to an airborne one."),
 ("highest ozone near the ground carried the most hospital visits",
  "Recomputed in q9 above: ranking the days by ozone measured near the ground gives the same order as ranking them by hospital visits. EIN-3.C.4 links respiratory problems to elevated tropospheric ozone."),
 ("test of how well the lungs of exposed people are working",
  "EIN-3.C.4 names respiratory problems and overall lung function as what elevated tropospheric ozone can affect, so a lung function measure is the aligned measure. Vehicle counts, awareness, river depth and rainfall are not health measures."),
 ("less likely to belong to some other exposure",
  "EIN-3.C.1 states that establishing cause and effect is difficult because humans experience exposure to a variety of chemicals and pollutants, so reducing the competing exposures is what makes an attribution more secure."),
 ("no single pollutant in the table can be identified as the cause",
  "Recomputed in q12 above: the table records only how many pollutants are elevated, never which, and illness rises with that count. EIN-3.C.1 makes the variety of exposures the reason attribution is hard."),
 ("Dysentery",
  "EIN-3.C.2 states that dysentery is caused by untreated sewage in streams and rivers, which is the village's situation. Mesothelioma is EIN-3.C.3, lung function EIN-3.C.4 and skin cancer STB-4.A.3."),
 ("Tropospheric ozone near the ground, when its levels are elevated",
  "EIN-3.C.4 concerns elevated levels of tropospheric ozone, while STB-4.A.3 concerns a decrease in stratospheric ozone and attaches skin cancer and cataracts to it. The anchor carries the layer and the direction together because the distractors vary each independently."),
 ("Mesothelioma, paired with exposure to asbestos",
  "EIN-3.C.3 attributes mesothelioma mainly to asbestos, EIN-3.C.2 attributes dysentery to untreated sewage, and EIN-3.C.4 attributes respiratory effects to elevated tropospheric ozone. Each rejected pairing crosses two of those."),
 ("most ozone near the ground had the lowest average lung function score",
  "Recomputed in q16 above: ranking the groups by ozone near the ground gives the reverse of the order by lung function score. EIN-3.C.4 states that overall lung function can be impacted by elevated tropospheric ozone."),
 ("Recording every other pollutant the participants are exposed to",
  "EIN-3.C.1 names simultaneous exposure to a variety of chemicals and pollutants as the source of the difficulty, so measuring the other exposures is what a design can do about it. Report length, convenience sampling and readership do not."),
 ("single pollutant can always be identified as the cause",
  "EIN-3.C.1 states the opposite, that the variety of simultaneous exposures makes cause and effect difficult to establish, so this is the option the framework denies. The four rejected options restate EIN-3.C.1 through EIN-3.C.4 correctly."),
 ("Mesothelioma is a type of cancer caused mainly by exposure to asbestos",
  "EIN-3.C.3 attributes mesothelioma mainly to asbestos exposure, which is the worker's history. The rejected statements concern sewage, ozone near the ground, the general difficulty of attribution, and the stratosphere."),
 ("Both the untreated sewage entering the river and the dysentery cases fell sharply",
  "Recomputed in q20 above: both columns are more than three times smaller in the rows after the plant opened than in the rows before it. EIN-3.C.2 names untreated sewage in streams and rivers as the cause of dysentery."),
 ("leaves room for the difficulty it also states",
  "EIN-3.C.3 uses the word mainly and EIN-3.C.1 states that attribution is difficult because humans experience exposure to a variety of chemicals and pollutants, so the qualifier matches the framework's own caution."),
 ("in the same people across days with different ozone levels",
  "EIN-3.C.4 links elevated tropospheric ozone to respiratory problems and lung function, so both the ground level ozone and the lung measure must vary and be recorded together. Measuring the stratosphere tests STB-4.A.3 instead."),
 ("after the sewage entering the river is treated, with other conditions unchanged",
  "EIN-3.C.2 names untreated sewage in streams and rivers as the cause of dysentery and EIN-3.C.1 warns that many exposures compete, so a change in the sewage with other conditions steady is what isolates it."),
 ("higher than usual amounts of ozone near the ground",
  "EIN-3.C.4 attaches respiratory problems and lung function to elevated levels of tropospheric ozone, so the word describes how much ozone is present near the ground. STB-4.A.3 concerns a decrease in a different layer, so the anchor names both."),
 ("while urban air carries the variety of chemicals and pollutants",
  "EIN-3.C.3 names asbestos as the main cause of mesothelioma while EIN-3.C.1 states that exposure to a variety of chemicals and pollutants is what makes cause and effect difficult, and urban air is the many-exposure case."),
 ("Treating sewage before it is allowed to enter streams and rivers",
  "EIN-3.C.2 states that dysentery is caused by untreated sewage in streams and rivers, so treating the sewage addresses the stated cause. The rejected actions address asbestos, ozone in either layer, and landfill gas."),
 ("cannot be assigned to one source from this result alone",
  "EIN-3.C.1 states that it can be difficult to establish a cause and effect between pollutants and human health issues because humans experience exposure to a variety of chemicals and pollutants, which is this neighborhood's situation."),
 ("reporting breathing difficulty together with a measured index of lung performance",
  "EIN-3.C.4 names respiratory problems and overall lung function, so a respiratory report combined with a lung measurement is the aligned measure. Stomach illness is EIN-3.C.2 and the chest lining cancer EIN-3.C.3."),
 ("while recognizing why such links are hard to establish in general",
  "Learning objective EIN-3.C is to identify sources of human health issues linked to pollution and EIN-3.C.1 supplies the caution about attribution. The rejected options belong to topics 8.12, 8.11, unit 7 and 8.9."),
 ("attributing illness to one pollutant is difficult because people are exposed to many at once",
  "Each clause of the keyed summary is one of EIN-3.C.1 through EIN-3.C.4. Every rejected summary denies the stated difficulty, swaps two causes, moves the ozone effect to the wrong layer, or denies the links altogether."),
]

TABLE_CHECKS = {3: q3, 6: q6, 9: q9, 12: q12, 16: q16, 20: q20}

es.run(e8_14, CLAIMS, TABLE_CHECKS, sys.argv)
