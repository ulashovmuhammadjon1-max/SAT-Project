"""Key audit for AP ENVIRONMENTAL SCIENCE 3.4 Carrying Capacity.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
ERT-3.D.1  when a population exceeds its carrying capacity (which can be
           denoted K), overshoot occurs; there are environmental impacts of
           overshoot, including resource depletion
                   -- items 1, 2, 3, 10, 11, 13, 14, 16, 17, 22, 23, 24, 25,
                      26, 27, 28, 29, 30
ERT-3.E.1  a major ecological effect of population overshoot is dieback of the
           population (often severe to catastrophic) because the lack of
           available resources leads to famine, disease, and conflict
                   -- items 4, 5, 6, 7, 8, 9, 12, 15, 18, 19, 20, 21, 22, 27,
                      28, 29, 30

WHAT ERT-3.D.1 DOES NOT DO IS DEFINE CARRYING CAPACITY. It supplies the symbol,
the condition for overshoot, and one named impact. So no key here states a
definition of carrying capacity, and item 11 keys only the two things the
statement does supply. Every distractor in that item is a claim the framework
contradicts or never makes -- never a true definition dressed as an error,
because a student who learns to reject a true statement has been taught
something false.

ERT-3.E.1's hedge, OFTEN severe to catastrophic, and its list of three
consequences as things the lack of resources LEADS TO, are keyed in items 5 and
9. Nothing here promises a total dieback, a fixed order among the three, or a
particular size for the surviving population -- item 29 keys that last absence.

DATA ITEMS: 13 to 26 carry tables, recomputed below by column header.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and EVERY data table in turn, and requires each
corruption to raise BEFORE the real gate runs. Three of these checks read a
difference or a co-varying gradient that a column reversal preserves; e_check
flattens those tables next and each check fails, because a flat column has no
difference and no gradient. ``python3 verify_e3_4.py --selftest`` is the same
run; the controls are not behind the flag.
"""
import sys

import cg_check as cg
import e_check
import e3_4

HERD = "Herd size"
K = "Carrying capacity of the range (K)"
FORAGE = "Forage available per animal (kilograms per year)"
DEATHS = "Number of animals"
K2 = "Carrying capacity (K)"
PEAK = "Peak herd size reached"
LATER = "Herd size ten years after the peak"
PCTK = "Herd size as a percent of the carrying capacity"
COVER = "Percent of the range's plant cover remaining after five years"


def _falls(v):
    return all(v[i + 1] < v[i] for i in range(len(v) - 1))


def _by(table, key_header, *headers):
    keys = cg.col(table, key_header)
    order = sorted(range(len(table["rows"])), key=lambda i: keys[i])
    return [[cg.col(table, h)[i] for i in order] for h in headers]


def q13(table, item):
    labs = cg.labels(table)
    herd = cg.col(table, HERD)
    cap = cg.col(table, K)
    assert len(set(cap)) == 1, f"one carrying capacity must apply throughout; got {cap}"
    over = [lab for lab, h in zip(labs, herd) if h > cap[0]]
    assert over == ["Year 7", "Year 10"], \
        f"exactly the seventh and tenth years must be in overshoot; got {over}"
    assert len(over) < len(labs), "'in every year of the record' must be false"
    return (f"the herd reads {herd} against a carrying capacity of {cap[0]:.0f}, exceeding "
            f"it in exactly {len(over)} of the {len(labs)} years: {over}")


def q14(table, item):
    herd = cg.col(table, HERD)
    cap = cg.col(table, K)[0]
    excess = max(herd) - cap
    assert excess == 580, f"the largest excess must be 580; got {excess}"
    assert excess != max(herd) and excess != cap, \
        "the excess must not coincide with the peak herd or the capacity"
    return (f"the largest herd is {max(herd):.0f} against a capacity of {cap:.0f}, an excess "
            f"of {excess:.0f}")


def q15(table, item):
    herd = cg.col(table, HERD)
    cap = cg.col(table, K)[0]
    assert max(herd) > cap, "the herd must exceed the carrying capacity at some point"
    assert herd[-1] < cap, f"the herd must end below the carrying capacity; got {herd[-1]}"
    assert herd[-1] < herd[0], \
        f"the herd must end below where it started; got {herd[0]} then {herd[-1]}"
    return (f"the herd peaks at {max(herd):.0f} against a capacity of {cap:.0f} and ends at "
            f"{herd[-1]:.0f}, below both the capacity and its own starting {herd[0]:.0f}")


def q16(table, item):
    (forage,) = _by(table, HERD, FORAGE)
    assert _falls(forage), f"forage per animal must fall as the herd grows; got {forage}"
    assert len(set(forage)) == len(forage), "'unchanged as the herd grew' must be false"
    return (f"sorted by herd size the forage per animal reads {forage} kilograms a year, "
            "strictly decreasing")


def q17(table, item):
    forage = cg.col(table, FORAGE)
    gap = max(forage) - min(forage)
    assert gap == 840, f"the difference must be 840 kilograms a year; got {gap}"
    assert gap != max(forage) and gap != min(forage) and gap != max(forage) + min(forage), \
        "the difference must not coincide with an endpoint or with their sum"
    return (f"forage per animal runs {max(forage):.0f} to {min(forage):.0f} kilograms a "
            f"year, a difference of {gap:.0f}")


def q18(table, item):
    labs = cg.labels(table)
    n = dict(zip(labs, cg.col(table, DEATHS)))
    assert len(n) == 3, f"three causes must be tabulated; got {len(n)}"
    assert all(v > 0 for v in n.values()), f"every cause must account for some deaths; got {n}"
    assert len(set(n.values())) == 3, \
        f"'the three causes were equal' must be false; got {n}"
    return f"all three causes account for deaths, in three different numbers: {n}"


def q19(table, item):
    labs = cg.labels(table)
    n = dict(zip(labs, cg.col(table, DEATHS)))
    worst = max(n, key=n.get)
    assert worst == "Starvation for want of forage", \
        f"starvation must account for the most deaths; got {worst}"
    assert list(n.values()).count(n[worst]) == 1, "'the three causes were equal' must be false"
    return f"the three counts are {n}, and the largest belongs to {worst}"


def q20(table, item):
    herd = cg.col(table, HERD)
    share = (herd[0] - herd[1]) / herd[0]
    assert abs(share - 0.8) < 0.05, f"the fall must be about four fifths; got {share}"
    for wrong in (0.2, 0.5, 0.1):
        assert abs(share - wrong) > 0.1, f"a fall of {wrong} must be false"
    return (f"the herd falls {herd[0]:.0f} to {herd[1]:.0f}, a loss of "
            f"{herd[0] - herd[1]:.0f}, which is {share:.2f} of the peak")


def q21(table, item):
    herd = cg.col(table, HERD)
    left = herd[1] / herd[0]
    assert left < 0.2, f"the survivors must be under a fifth of the peak; got {left}"
    assert left > 0, "the herd must not have vanished entirely"
    return (f"{herd[1]:.0f} of a peak {herd[0]:.0f} is {left:.2f} of it, under one fifth")


def q22(table, item):
    labs = cg.labels(table)
    cap = dict(zip(labs, cg.col(table, K2)))
    peak = dict(zip(labs, cg.col(table, PEAK)))
    later = dict(zip(labs, cg.col(table, LATER)))
    assert len(set(cap.values())) == 1, f"both ranges must share one capacity; got {cap}"
    over = [lab for lab in labs if peak[lab] > cap[lab]]
    assert over == ["Range 2"], f"exactly the second herd must exceed the capacity; got {over}"
    for lab in labs:
        collapsed = later[lab] < 0.5 * peak[lab]
        assert collapsed == (lab in over), \
            f"{lab}: collapse and overshoot must go together; peak {peak[lab]}, later {later[lab]}"
    return (f"the peaks are {peak} against a capacity of {cap[labs[0]]:.0f}, and the herd "
            f"standing at {later} ten years later collapsed in exactly the overshooting case")


def q23(table, item):
    labs = cg.labels(table)
    cap = dict(zip(labs, cg.col(table, K2)))
    peak = dict(zip(labs, cg.col(table, PEAK)))
    safe = [lab for lab in labs if peak[lab] <= cap[lab]]
    assert safe == ["Range 1"], \
        f"exactly the first herd must have stayed within the capacity; got {safe}"
    return (f"the peaks are {peak} against a capacity of {cap[labs[0]]:.0f}, so exactly one "
            f"herd stayed within it: {safe[0]}")


def q24(table, item):
    (cover,) = _by(table, PCTK, COVER)
    assert _falls(cover), f"plant cover must fall as the herd share rises; got {cover}"
    assert cover[-1] == min(cover), \
        "'the largest herd relative to capacity kept the most cover' must be false"
    assert len(set(cover)) == len(cover), "'the same cover on all four ranges' must be false"
    return (f"sorted by herd size as a share of the carrying capacity the plant cover reads "
            f"{cover} percent, strictly decreasing")


def q25(table, item):
    labs = cg.labels(table)
    pct = dict(zip(labs, cg.col(table, PCTK)))
    over = [lab for lab in labs if pct[lab] > 100]
    assert over == ["Range C", "Range D"], \
        f"exactly the third and fourth ranges must be in overshoot; got {over}"
    assert len(over) < len(labs), "'all four ranges' must be false"
    return (f"the herd shares are {pct} percent of capacity, above 100 in exactly "
            f"{len(over)} of them: {over}")


def q26(table, item):
    labs = cg.labels(table)
    cover = dict(zip(labs, cg.col(table, COVER)))
    worst = min(cover, key=cover.get)
    assert worst == "Range D", f"Range D must retain the least plant cover; got {worst}"
    assert list(cover.values()).count(cover[worst]) == 1, \
        "'the four ranges lost the same amount' must be false"
    pct = dict(zip(labs, cg.col(table, PCTK)))
    assert pct[worst] == max(pct.values()), \
        "the range retaining least cover must also carry the largest herd relative to capacity"
    return (f"the plant cover remaining is {cover} percent, and the least belongs to {worst}, "
            f"whose herd stands at {pct[worst]:.0f} percent of the capacity")


CLAIMS = [
 ("Overshoot occurs",
  "ERT-3.D.1 states that when a population exceeds its carrying capacity, overshoot occurs. The statement treats exceeding K as something that does happen, which is what the rejected options deny or replace."),
 ("The letter K",
  "ERT-3.D.1 states in its own parenthesis that carrying capacity can be denoted as K, and offers no other letter."),
 ("Resource depletion",
  "ERT-3.D.1 states that there are environmental impacts of population overshoot, INCLUDING resource depletion. That is the one impact the statement names, and including leaves room for others it does not name."),
 ("Dieback of the population",
  "ERT-3.E.1 states that a major ecological effect of population overshoot is dieback of the population. Dieback is the framework's own term for what follows overshoot."),
 ("Often severe to catastrophic",
  "ERT-3.E.1 describes the dieback, in its own parenthesis, as often severe to catastrophic. OFTEN makes that the usual range rather than a guarantee, and the statement does comment on severity."),
 ("The lack of available resources",
  "ERT-3.E.1 states that the dieback follows BECAUSE the lack of available resources leads to famine, disease, and conflict, so the shortage of resources is the cause it gives."),
 ("Famine, disease and conflict",
  "ERT-3.E.1 states that the lack of available resources leads to famine, disease, and conflict. Each rejected set replaces at least one of the three."),
 ("A rise in the birth rate",
  "ERT-3.E.1 names famine, disease, and conflict. A rise in the birth rate is not among them."),
 ("Any one of the three, or more than one, may be at work",
  "ERT-3.E.1 lists the three as what the lack of resources leads to without requiring all of them at once, restricting a case to one, or fixing an order among them."),
 ("The population's carrying capacity",
  "ERT-3.D.1 states that overshoot occurs when a population EXCEEDS ITS CARRYING CAPACITY, so carrying capacity is the quantity the population is measured against. The other quantities belong to other statements."),
 ("denoted K, and that a population exceeding it is in overshoot",
  "ERT-3.D.1 supplies the symbol K in a parenthesis and the condition under which overshoot occurs. Each rejected option asserts something the statement contradicts -- by saying a population cannot exceed K -- or never mentions at all."),
 ("dieback, often severe to catastrophic",
  "ERT-3.E.1 attaches a dieback, often severe to catastrophic, to overshoot, and ERT-3.D.1 attaches resource depletion to it, so a simple return to an earlier size is neither. The rejected options are true statements that do not bear on severity."),
 ("In the seventh and tenth years",
  "Recomputed in q13 above: the herd exceeds the constant carrying capacity of 900 in exactly two of the five years recorded. ERT-3.D.1 makes exceeding carrying capacity the overshoot condition."),
 ("By 580 animals",
  "Recomputed in q14 above: 1,480 less 900 is 580, and 580 is neither the peak nor the capacity. The rejected values are those quantities or a difference between other rows."),
 ("below the carrying capacity and below its own starting size",
  "Recomputed in q15 above: the herd peaks above the capacity and is then recorded below both the capacity and its own starting count. ERT-3.E.1 makes dieback the major ecological effect of overshoot."),
 ("fell as the herd grew",
  "Recomputed in q16 above: sorted by herd size the forage per animal is strictly decreasing. ERT-3.D.1 names resource depletion among the environmental impacts of overshoot."),
 ("840 kilograms a year",
  "Recomputed in q17 above: 910 less 70 is 840, which is neither endpoint nor their sum. The rejected values are those other quantities."),
 ("All three of the consequences the framework names appear",
  "Recomputed in q18 above: all three causes account for deaths, in three different numbers. ERT-3.E.1 states that the lack of available resources leads to famine, disease, and conflict."),
 ("Starvation for want of forage",
  "Recomputed in q19 above: the three counts are 620, 410 and 190 and the largest is unique. The comparison is a direct reading of one column."),
 ("By about four fifths",
  "Recomputed in q20 above: the herd falls from 1,480 to 260, which is about 82 percent of the peak, and no other listed fraction is within reach of that. ERT-3.E.1 describes the dieback after overshoot as often severe to catastrophic."),
 ("under a fifth of the peak size",
  "Recomputed in q21 above: 260 out of a peak of 1,480 is under one fifth, and the herd has not vanished. ERT-3.E.1's phrase for a dieback of this kind is often severe to catastrophic."),
 ("Only the herd that rose above the carrying capacity",
  "Recomputed in q22 above: exactly one of the two herds exceeds the shared capacity, and the collapse to under half the peak occurs in exactly that case. ERT-3.D.1 supplies the overshoot condition and ERT-3.E.1 the dieback that follows it."),
 ("The herd on Range 1",
  "Recomputed in q23 above: exactly one herd's peak lies at or below the shared carrying capacity. ERT-3.D.1 defines the overshoot condition as the population exceeding its carrying capacity."),
 ("Less plant cover remained on the ranges whose herds stood higher",
  "Recomputed in q24 above: sorted by herd size as a share of carrying capacity the plant cover remaining is strictly decreasing. ERT-3.D.1 names resource depletion among the environmental impacts of overshoot."),
 ("Range C and Range D",
  "Recomputed in q25 above: exactly two of the four herds stand above 100 percent of the carrying capacity. ERT-3.D.1 makes exceeding carrying capacity the overshoot condition."),
 ("Range D",
  "Recomputed in q26 above: the least plant cover remaining is unique and belongs to the range whose herd stands furthest above the carrying capacity."),
 ("Resource depletion, followed by a dieback",
  "ERT-3.D.1 names resource depletion among the environmental impacts of overshoot and ERT-3.E.1 names dieback as its major ecological effect. Neither statement offers a rising capacity, a steady herd or an improvement in resources."),
 ("forage per animal falling, and deaths from starvation",
  "ERT-3.D.1 supplies the overshoot condition and resource depletion and ERT-3.E.1 supplies the dieback and the famine, disease and conflict behind it. The keyed records are exactly those three elements; each rejected option measures something the statements do not connect to overshoot."),
 ("always returns to exactly its carrying capacity afterwards",
  "ERT-3.D.1 and ERT-3.E.1 together supply the condition, the depletion, the dieback and the three consequences, and neither states where the population settles afterwards. A promise of an exact return is therefore an addition to the framework."),
 ("dieback, often severe to catastrophic, because the lack of resources",
  "ERT-3.D.1 supplies the symbol, the overshoot condition and resource depletion, and ERT-3.E.1 supplies the dieback, its hedged severity and the famine, disease and conflict behind it. Each rejected summary denies that K can be exceeded, softens the dieback, swaps its cause, or adds a promise about where the population settles."),
]

TABLE_CHECKS = {13: q13, 14: q14, 15: q15, 16: q16, 17: q17, 18: q18, 19: q19,
                20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26}

if "--selftest" in sys.argv:
    print("note: e_check.run negative-controls every gate on every run; "
          "--selftest is the same run, not a separate one.")

e_check.run(e3_4, CLAIMS, TABLE_CHECKS)
