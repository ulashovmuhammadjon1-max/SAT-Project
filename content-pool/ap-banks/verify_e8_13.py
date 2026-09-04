"""Key audit for AP ENVIRONMENTAL SCIENCE 8.13 Dose Response Curve.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
EIN-3.B.1 is the whole of the framework's content for this topic: a dose
response curve describes the effect on an organism or mortality rate in a
population based on the dose of a particular toxin or drug. Each item keys one
of the three things that sentence contains, or reads its own table:

  the response may be an EFFECT or a MORTALITY RATE -- items 1, 2, 5, 8, 9, 16,
      18, 22, 29;
  the controlling variable is the DOSE -- items 4, 7, 11, 15, 19, 24, 28;
  the agent may be a TOXIN OR A DRUG -- items 6, 10, 13;
  read from the item's own table -- items 3, 5, 8, 10, 14, 17, 20, 24;
  the limit that a study describes only the doses given -- items 12, 25, 30.
Item 22 relates EIN-3.A.1's LD50 to this statement; items 21, 26 and 27 apply
the relationship to an environmental question, which is suggested skill 5.E.

NOT KEYED, because the framework states none of them: any named shape of the
relationship, any threshold model, any safe dose, any real chemical, any
exposure duration, and any extrapolation past the highest dose tested. Items 12
and 25 exist to refuse the last of those.

NO FIGURE ANYWHERE. The topic is named after a graph and the bank cannot show
one, so every relationship is a table and no stem refers to a curve, a plot or
an axis. Where an item asks for the dose at which a stated share responds, a
row carries that share exactly; this is checked below rather than assumed.

DATA ITEMS: 3, 5, 8, 10, 14, 17, 20 and 24 carry tables and every keyed reading
is recomputed here from the table alone.

NEGATIVE CONTROL: `python3 verify_e8_13.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e8_13

DOSE_UG = "Dose given to each group (micrograms per liter)"
GROWTH = "Percent of the group whose growth was reduced"
DIED = "Percent of the group that died"
REPRO = "Percent of the survivors with impaired reproduction"
DOSE_MG = "Dose given to each group (milligrams per kilogram of body mass)"
ENZ = "Average activity of the enzyme in the exposed animals (units)"
DRUG_DOSE = "Dose of the drug given to each group (milligrams)"
IMPROVED = "Percent of the group whose symptom improved"
SP_R = "Percent of species R showing the effect"
SP_S = "Percent of species S showing the effect"
RIVER_CONC = "Concentration measured at the site (micrograms per liter)"
RIVER_PCT = ("Percent of test animals showing the effect at that concentration in the "
             "laboratory")
PLATEAU = "Percent of the group showing the response"
CTRL_DOSE = "Dose received (milligrams per liter)"
CTRL_PCT = "Percent of the group showing the effect"


def _half_dose(dose, pct, label):
    hits = [d for d, p in zip(dose, pct) if p == 50]
    assert len(hits) == 1, (
        f"{label}: {len(hits)} rows record exactly 50 percent responding, so the dose the "
        f"item asks for is not readable from the rows given: {list(zip(dose, pct))}")
    return hits[0]


def q3(table, item):
    dose = cg.col(table, DOSE_UG)
    pct = cg.col(table, GROWTH)
    pairs = sorted(zip(dose, pct))
    assert all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"the share affected does not rise at every higher dose: {pairs}"
    assert pct[dose.index(0.0)] == 0, "the group receiving no dose is not unaffected"
    assert pct[dose.index(max(dose))] == max(pct), \
        "'the largest dose gave the smallest share' must be false"
    return (f"sorted by dose the shares run {[p for _, p in pairs]} percent, rising at "
            "every step from none in the untreated group")


def q5(table, item):
    dose = cg.col(table, DOSE_UG)
    died = cg.col(table, DIED)
    repro = cg.col(table, REPRO)
    low = [i for i in range(len(dose)) if died[i] <= 1]
    assert low, f"no dose killed one percent or fewer: {died}"
    assert max(repro[i] for i in low) >= 10, \
        f"no low mortality dose shows a substantial nonlethal effect: {repro}"
    pairs = sorted(zip(dose, repro))
    assert all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"the nonlethal effect does not rise with dose: {pairs}"
    assert died != repro, "'deaths and the effect appear at exactly the same doses' must be false"
    return (f"at doses killing at most one percent the impaired reproduction already "
            f"reaches {max(repro[i] for i in low):.0f} percent, and both columns rise with "
            "dose")


def q8(table, item):
    dose = cg.col(table, DOSE_MG)
    enz = cg.col(table, ENZ)
    pairs = sorted(zip(dose, enz))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"the measured activity does not fall at every higher dose: {pairs}"
    assert enz[dose.index(max(dose))] == min(enz), \
        "'the largest dose gave the highest activity' must be false"
    assert len(table["headers"]) == 2 and "died" not in " ".join(table["headers"]).lower(), \
        "the table records deaths after all, which would change the key"
    return (f"sorted by dose the activity values run {[e for _, e in pairs]} units, "
            "falling at every step, and no column records deaths")


def q10(table, item):
    dose = cg.col(table, DRUG_DOSE)
    imp = cg.col(table, IMPROVED)
    pairs = sorted(zip(dose, imp))
    assert all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"the share improved does not rise with dose: {pairs}"
    assert imp[dose.index(0.0)] == min(imp), \
        "'the group given no drug improved most' must be false"
    return (f"sorted by dose the shares improved run {[p for _, p in pairs]} percent, "
            "rising from the smallest value in the group given none")


def q14(table, item):
    dose = cg.col(table, DOSE_UG)
    r = cg.col(table, SP_R)
    s = cg.col(table, SP_S)
    dr = _half_dose(dose, r, "species R")
    ds = _half_dose(dose, s, "species S")
    assert dr < ds, f"species R does not reach half first: {dr} against {ds}"
    assert ds > 5 * dr, f"the two doses are not many times apart: {dr} and {ds}"
    assert max(r) > 0, "'the first species never shows the effect' must be false"
    return (f"species R reaches exactly half showing the effect at {dr} and species S at "
            f"{ds} micrograms per liter, a factor of {ds / dr:.0f}")


def q17(table, item):
    sites = cg.labels(table)
    conc = cg.col(table, RIVER_CONC)
    pct = cg.col(table, RIVER_PCT)
    order = [s for _, s in sorted(zip(conc, sites))]
    assert order == [s for _, s in sorted(zip(pct, sites))], \
        f"the order by concentration does not match the order by share affected: {conc} {pct}"
    assert pct[conc.index(max(conc))] == max(pct), \
        "the highest concentration does not carry the largest share affected"
    assert len(set(pct)) == len(pct), "'the same share at every site' must be false"
    return (f"ranking the sites by measured concentration gives {order}, the same order as "
            "ranking them by the share of test animals affected")


def q20(table, item):
    dose = cg.col(table, DOSE_MG)
    pct = cg.col(table, PLATEAU)
    pairs = sorted(zip(dose, pct))
    assert all(pairs[i][1] <= pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"the share responding falls somewhere as the dose rises: {pairs}"
    top = [p for _, p in pairs[-2:]]
    assert top == [100.0, 100.0], f"the two highest doses do not both reach 100: {top}"
    assert min(pct) == 0, "the untreated group is not free of the response"
    assert len(set(pct)) > 1, "'the same at every dose' must be false"
    return (f"sorted by dose the shares run {[p for _, p in pairs]} percent, reaching the "
            "whole group at the two highest doses so that no further rise is possible")


def q24(table, item):
    groups = cg.labels(table)
    dose = cg.col(table, CTRL_DOSE)
    pct = cg.col(table, CTRL_PCT)
    ctrl = [i for i, g in enumerate(groups) if g.strip().lower().startswith("control")]
    assert len(ctrl) == 1 and dose[ctrl[0]] == 0, \
        f"there is not exactly one group at zero dose: {groups} {dose}"
    c = ctrl[0]
    assert 0 < pct[c] < 10, f"the control does not show a small nonzero share: {pct[c]}"
    dosed = [i for i in range(len(groups)) if i != c]
    assert all(pct[i] > pct[c] for i in dosed), \
        f"some dosed group is not above the control: {pct}"
    pairs = sorted((dose[i], pct[i]) for i in dosed)
    assert all(pairs[k][1] < pairs[k + 1][1] for k in range(len(pairs) - 1)), \
        f"the dosed groups do not rise with dose: {pairs}"
    return (f"the control at zero dose shows {pct[c]:.0f} percent while the dosed groups "
            f"run {[p for _, p in pairs]} percent, rising with dose")


CLAIMS = [
 ("effect on an organism, or the mortality rate in a population, based on the dose",
  "EIN-3.B.1 verbatim in substance: a dose response curve describes the effect on an organism or mortality rate in a population based on the dose of a particular toxin or drug. Persistence, transport, fat solubility and species counts belong to other statements."),
 ("An effect on an organism, or a mortality rate in a population",
  "EIN-3.B.1 names both an effect on an organism and a mortality rate in a population, so death is one possible response rather than the only one."),
 ("rises at every higher dose, and no reduction occurred in the group that received none",
  "Recomputed in q3 above: sorted by dose the shares rise at every step and the untreated row is zero. EIN-3.B.1 makes such a dependence of an effect on the dose what the relationship describes."),
 ("dose of the toxin or drug that was given",
  "EIN-3.B.1 states that the relationship describes the effect or mortality rate based on the dose of a particular toxin or drug, so the dose is the controlling quantity."),
 ("at doses that killed few or none of the group",
  "Recomputed in q5 above: at doses killing one percent or fewer the impaired reproduction already reaches double figures, and both columns rise with dose. EIN-3.B.1 allows an effect on an organism as well as a mortality rate."),
 ("it refers to the dose of a particular toxin or drug, so a drug is covered as well",
  "EIN-3.B.1 refers to the dose of a particular toxin or drug, so both are within the statement, and it does not extend to measurements with no administered substance."),
 ("a relationship cannot be described from a single value of the dose",
  "EIN-3.B.1 describes the response as based on the dose, which is a relationship between two quantities, so the dose must be varied for it to be observed."),
 ("graded effect rather than a count of deaths",
  "Recomputed in q8 above: the measured activity falls at every higher dose and no column of the table records deaths. EIN-3.B.1 allows the response to be an effect on an organism, which a measured activity is."),
 ("Any measurable effect the dose produces in the organism",
  "EIN-3.B.1 names the effect on an organism alongside the mortality rate in a population, so a response short of death is within the statement. Abundance, price and persistence are not responses of an organism to a dose."),
 ("share of the group whose symptom improved rises with the dose given",
  "Recomputed in q10 above: sorted by dose the shares improved rise at every step from the smallest value in the group given none. EIN-3.B.1 covers a drug as well as a toxin."),
 ("each given a different dose, with the same response measured in every group",
  "EIN-3.B.1 makes the relationship one between the dose and the response, so the dose must vary across groups while the response measured stays the same. Each rejected design holds the dose fixed, changes the response, or leaves the dose unrecorded."),
 ("because the relationship describes the responses at the doses that were actually given",
  "EIN-3.B.1 describes the response based on the dose, and a study describes the doses it administered. The framework supplies no rule for projecting the relationship beyond the range tested."),
 ("so a relationship measured for one substance describes that substance",
  "EIN-3.B.1 refers to the dose of a particular toxin or drug, which ties the relationship to the substance administered as well as to the organisms tested."),
 ("Half of the first species shows the effect at a dose many times smaller",
  "Recomputed in q14 above: each species has exactly one row at half showing the effect and the dose for the first is more than five times smaller. EIN-3.B.1 makes the response depend on the dose, so the species needing less is the more sensitive."),
 ("with larger doses producing larger responses over the range tested",
  "EIN-3.B.1 states that the relationship describes the response based on the dose, so a response rising with dose is the dose controlling the response rather than the reverse."),
 ("percentage of exposed animals whose reproduction was impaired",
  "EIN-3.B.1 makes the dose the administered quantity and the effect or mortality rate the response. The four rejected options all describe how much substance the organisms received."),
 ("highest measured concentration corresponds to the largest share of test animals affected",
  "Recomputed in q17 above: ranking the sites by measured concentration gives the same order as ranking them by the share affected. EIN-3.B.1 makes the response depend on the dose, which is what lets a field concentration be read against laboratory data."),
 ("expresses what share of a group is affected, which one organism cannot show",
  "EIN-3.B.1 pairs the mortality rate with a population while pairing an effect with an organism, so the rate is a property of the group. The framework does allow an effect to be measured in an organism."),
 ("does not describe how the response depends on the dose",
  "EIN-3.B.1 describes a response based on the dose, which requires the dose to vary, so a single dose yields one point rather than the dependence the statement names."),
 ("Above a certain dose every individual in the group responded",
  "Recomputed in q20 above: the two highest rows both record the whole group responding and no row falls as dose rises, so a percentage has no room to rise further. EIN-3.B.1 makes the response depend on the dose."),
 ("connects a concentration organisms are exposed to with the response expected",
  "EIN-3.B.1 describes the effect or mortality rate based on the dose, so it links an exposure to an expected response. Production, persistence, transport and species counts are described by other statements."),
 ("single dose at which the mortality response reaches half of the population",
  "EIN-3.A.1 defines the LD50 as the dose lethal to 50 percent of the population of a particular species and EIN-3.B.1 makes the mortality rate a response based on dose, so the LD50 is one point of that relationship rather than the whole of it."),
 ("what share of a group responds without the substance",
  "EIN-3.B.1 makes the response depend on the dose, so a group at zero dose establishes the response attributable to something other than the substance. It is not itself the largest response nor a calculating device."),
 ("small share of the group receiving no dose showed the effect",
  "Recomputed in q24 above: exactly one group is at zero dose, it carries a small nonzero share, and every dosed group is above it and rises with dose. EIN-3.B.1 makes the response depend on the dose."),
 ("doses used in the study are the doses organisms receive in the wild",
  "EIN-3.B.1 describes the response based on the dose administered, which says nothing about field exposure, so this is the conclusion a dose response study alone cannot support. The four rejected conclusions are readings of the study's own doses and responses."),
 ("population needing the larger dose is less sensitive",
  "EIN-3.B.1 makes the response depend on the dose of a particular substance, so needing more of the same substance for the same response is lower sensitivity. Persistence and transport are properties of the substance in the environment."),
 ("sites whose measured concentrations fall where the data show a large share of organisms responding",
  "EIN-3.B.1 links a dose to an expected response, so matching measured concentrations against the doses at which responses are large is what the two sets of data support together. Persistence and transport are not part of this statement."),
 ("depends on how much of the substance is received, not merely on whether any is present",
  "EIN-3.B.1 makes the effect or mortality rate depend on the dose of a particular toxin or drug, which distinguishes how much is received from whether any is present."),
 ("paired with a mortality rate described on the basis of dose",
  "EIN-3.B.1 pairs the dose with an effect on an organism or a mortality rate in a population. Persistence, transport and price belong to other statements and are not responses based on dose."),
 ("it describes only the doses that were actually given",
  "The keyed summary states EIN-3.B.1 together with the limit that follows from it, since a study describes the doses it administered. Every rejected summary drops the nonlethal effect, excludes drugs, invents a safety threshold, or replaces the response with persistence."),
]

TABLE_CHECKS = {3: q3, 5: q5, 8: q8, 10: q10, 14: q14, 17: q17, 20: q20, 24: q24}

es.run(e8_13, CLAIMS, TABLE_CHECKS, sys.argv)
