"""Key audit for AP ENVIRONMENTAL SCIENCE 3.6 Age Structure Diagrams.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
  EIN-1.A.1  population growth rates can be interpreted from age structure
             diagrams by the shape of the structure
                 -- items 1, 5, 7, 11, 12, 14, 15, 16, 22, 25, 28, 30
  EIN-1.A.2  a rapidly growing population will, as a rule, have a higher
             proportion of younger people compared to stable or declining
             populations
                 -- items 2, 3, 4, 6, 7, 8, 9, 10, 13, 17, 18, 19, 20, 21,
                    23, 24, 26, 27, 29, 30

NO FIGURE IS REFERENCED, and that is the whole design problem of this topic.
The framework's object is a picture and the bank cannot carry one, so the word
"diagram" appears in no stem; every structure a student is asked to read is
supplied as a table of population by age band, by sex where both columns are
needed. ``e_check.no_figure_reference`` enforces this on every run and its
negative control injects a stem that points at a picture.

THE SWAP IS THE DANGER HERE. Broad based versus narrow based -- an expanding
against a contracting structure -- is the distractor a prepared student is most
likely to fall for, so items 11, 14, 16, 21, 23 and 30 each carry the swap as a
distractor and each anchor names BOTH clauses (the direction AND the shape it
implies), never just one. An anchor of "narrow based shape" alone would have
matched the swap in item 11 as well as the key.

BOUNDARIES. Total fertility rate is EIN-1.B (topic 3.7), the crude rates and
the rule of 70 are EIN-1.C (topic 3.8), and the four stage model is EIN-1.D
(topic 3.9). No key here uses any of them, and items 7 and 30 refuse the
reading that a doubling time can be read off a structure.

DATA ITEMS: 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24
and 29 carry tables. Each keyed conclusion is recomputed below from that table
alone.

NEGATIVE CONTROLS run on every invocation through ``e_check.run``: a key is
moved, an anchor broken, a choice duplicated, a ``why`` thinned, an option
named by letter, a backslash and a year range injected, a stem pointed at a
figure, and every table in turn reversed and then flattened. ``--selftest``
adds ``es_check.selftest``, which rotates all thirty keys one at a time and
corrupts every cell of every table individually.
"""
import sys

import cg_check as cg
import e_check
import es_check as es

import e3_6

P1 = "Population 1 (percent of its total)"
P2 = "Population 2 (percent of its total)"
P3 = "Population 3 (percent of its total)"
MALES = "Males (thousands)"
FEMALES = "Females (thousands)"
COUNT = "Population (thousands)"
UNDER15 = "Percent of population under 15"
OVER65 = "Percent of population 65 and over"
GROWTH = "Annual population growth rate (percent)"
POPA = "Population A (thousands)"
POPB = "Population B (thousands)"


def _three(table):
    """The three share columns, keyed by their column name."""
    return {name: cg.col(table, name) for name in (P1, P2, P3)}


def _band_totals(table):
    """Males plus females, band by band, youngest first."""
    m = cg.col(table, MALES)
    f = cg.col(table, FEMALES)
    return [a + b for a, b in zip(m, f)]


def q8(table, item):
    cols = _three(table)
    for name, vals in cols.items():
        assert abs(sum(vals) - 100) < 0.5, f"{name} must total 100 percent; got {sum(vals)}"
    youngest = {name: vals[0] for name, vals in cols.items()}
    top = max(youngest, key=youngest.get)
    assert top == P1, f"the largest youngest band share must belong to Population 1; got {top}"
    assert len([v for v in youngest.values() if v == youngest[top]]) == 1, \
        "the largest youngest band share must be unique, so 'all three grow equally' is false"
    p1 = cols[P1]
    assert all(p1[i + 1] < p1[i] for i in range(len(p1) - 1)), \
        f"Population 1's shares must fall with age, giving a broad based shape; got {p1}"
    p3 = cols[P3]
    assert p3[0] == min(youngest.values()), \
        "Population 3 must hold the smallest youngest band share, so it is not the growing case"
    return (f"the youngest band shares are {youngest[P1]:.0f}, {youngest[P2]:.0f} and "
            f"{youngest[P3]:.0f} percent, and only the first column falls monotonically "
            "with age")


def q9(table, item):
    cols = _three(table)
    top_heavy = []
    for name, vals in cols.items():
        young = vals[0]
        old = vals[4] + vals[5]
        if old > young:
            top_heavy.append(name)
    assert top_heavy == [P3], \
        f"exactly Population 3 must hold more people aged sixty and over than under fifteen; got {top_heavy}"
    return (f"the two oldest bands of Population 3 total {cols[P3][4] + cols[P3][5]:.0f} "
            f"percent against {cols[P3][0]:.0f} percent under fifteen, and no other column "
            "is top heavy")


def q10(table, item):
    youngest = [cg.col(table, name)[0] for name in (P1, P2, P3)]
    gap = max(youngest) - min(youngest)
    assert abs(gap - 27) < 1e-9, f"the spread of the youngest band shares must be 27; got {gap}"
    return (f"the youngest band shares are {youngest}, so the largest less the smallest is "
            f"{gap:.0f} percentage points")


def q11(table, item):
    totals = _band_totals(table)
    assert all(totals[i] > totals[i + 1] for i in range(len(totals) - 1)), \
        f"each younger band must hold more people than the band above it; got {totals}"
    assert len(set(totals)) == len(totals), \
        "'the bands hold nearly equal numbers' must be false"
    assert totals[-1] != max(totals), "'the oldest band is the largest' must be false"
    return (f"band by band the totals read {[int(t) for t in totals]} thousand, strictly "
            "falling with age, which is a broad based structure")


def q12(table, item):
    m = cg.col(table, MALES)
    f = cg.col(table, FEMALES)
    total = m[0] + f[0]
    assert abs(total - 1920) < 1e-9, f"the youngest band must total 1,920 thousand; got {total}"
    assert m[0] != total and f[0] != total, "neither sex alone may equal the band total"
    return (f"the youngest band holds {m[0]:.0f} males and {f[0]:.0f} females, "
            f"{total:.0f} thousand together")


def q13(table, item):
    m = cg.col(table, MALES)
    f = cg.col(table, FEMALES)
    total = m[0] + f[0] + m[1] + f[1]
    assert abs(total - 3530) < 1e-9, f"the two youngest bands must total 3,530 thousand; got {total}"
    assert abs((m[0] + f[0]) - total) > 1e-9, "the youngest band alone must not equal the total"
    return (f"the two youngest bands hold {m[0] + f[0]:.0f} and {m[1] + f[1]:.0f} thousand, "
            f"{total:.0f} thousand together")


def q14(table, item):
    totals = _band_totals(table)
    youngest = totals[0]
    assert youngest == min(totals), \
        f"the youngest band must be the smallest in the record; got {[int(t) for t in totals]}"
    assert len([t for t in totals if t == youngest]) == 1, "that minimum must be unique"
    middle = max(totals[3:6])
    assert youngest < middle, \
        f"the youngest band must be smaller than the middle bands; got {youngest} against {middle}"
    assert len(set(totals)) > 1, "'every band holds the same number' must be false"
    return (f"band by band the totals read {[int(t) for t in totals]} thousand, so the "
            f"youngest band, {youngest:.0f}, is the smallest and the middle bands the "
            "largest, a narrow based structure")


def q15(table, item):
    totals = _band_totals(table)
    labels = cg.labels(table)
    top = max(range(len(totals)), key=lambda i: totals[i])
    assert labels[top] == "40 to 49", \
        f"the largest band must be 40 to 49; got {labels[top]}"
    assert len([t for t in totals if t == totals[top]]) == 1, "the largest band must be unique"
    return (f"band by band the totals read {[int(t) for t in totals]} thousand, whose single "
            f"largest entry falls in the {labels[top]} band")


def q16(table, item):
    vals = cg.col(table, COUNT)
    young = vals[:6]
    mean = sum(young) / len(young)
    spread = max(abs(v - mean) / mean for v in young)
    assert spread < 0.05, \
        f"the six youngest bands must sit within five percent of their mean; got {spread:.3f}"
    assert vals[0] < 1.5 * young[3], "'the youngest bands hold far more' must be false"
    assert vals[0] > 0.7 * max(young), "'the youngest bands hold far fewer' must be false"
    assert vals[-1] != max(vals), "'the oldest band is the largest' must be false"
    return (f"the six youngest bands read {[int(v) for v in young]} thousand, a spread of "
            f"{spread * 100:.1f} percent about their mean, so the structure is close to "
            "vertical")


def q17(table, item):
    pairs = sorted(zip(cg.col(table, UNDER15), cg.col(table, GROWTH)))
    assert all(pairs[i + 1][1] > pairs[i][1] for i in range(len(pairs) - 1)), \
        f"growth must rise with the share under fifteen; got {pairs}"
    assert len(set(g for _, g in pairs)) == len(pairs), \
        "'all four grow at the same rate' must be false"
    old = dict(zip(cg.labels(table), cg.col(table, OVER65)))
    growth = dict(zip(cg.labels(table), cg.col(table, GROWTH)))
    oldest = max(old, key=old.get)
    assert growth[oldest] != max(growth.values()), \
        "the country with the largest share sixty five and over must not have the highest growth"
    return (f"sorted by the share under fifteen the growth rates read "
            f"{[g for _, g in pairs]} percent, strictly increasing")


def q18(table, item):
    growth = dict(zip(cg.labels(table), cg.col(table, GROWTH)))
    shrinking = [c for c, g in growth.items() if g < 0]
    assert shrinking == ["Country 4"], \
        f"exactly Country 4 must record a growth rate below zero; got {shrinking}"
    young = dict(zip(cg.labels(table), cg.col(table, UNDER15)))
    old = dict(zip(cg.labels(table), cg.col(table, OVER65)))
    assert young["Country 4"] == min(young.values()), \
        "the shrinking country must hold the smallest share under fifteen"
    assert old["Country 4"] == max(old.values()), \
        "the shrinking country must hold the largest share sixty five and over"
    return (f"the growth rates read {list(growth.values())} percent, with a single negative "
            "entry, and it belongs to the country with the smallest young share")


def q19(table, item):
    young = dict(zip(cg.labels(table), cg.col(table, UNDER15)))
    top = max(young, key=young.get)
    assert top == "Country 1", f"Country 1 must hold the largest share under fifteen; got {top}"
    assert len([v for v in young.values() if v == young[top]]) == 1, \
        "that largest share must be unique, so the four structures can be ranked"
    return (f"the shares under fifteen read {list(young.values())} percent, whose single "
            f"largest entry belongs to {top}")


def q20(table, item):
    a = cg.col(table, POPA)
    b = cg.col(table, POPB)
    assert abs(sum(a) - sum(b)) < 1e-9, \
        f"the two populations must be the same total size; got {sum(a)} and {sum(b)}"
    assert a[0] > 2 * b[0], \
        f"Population A's youngest band must be more than twice Population B's; got {a[0]} and {b[0]}"
    assert a[0] != b[0], "'the two hold the same number under fifteen' must be false"
    return (f"both columns total {sum(a):.0f} thousand while the youngest bands hold "
            f"{a[0]:.0f} and {b[0]:.0f} thousand, a ratio above two")


def q21(table, item):
    a = cg.col(table, POPA)
    b = cg.col(table, POPB)
    assert abs(sum(a) - sum(b)) < 1e-9, "the two totals must be equal for the comparison to bite"
    share_a = a[0] / sum(a)
    share_b = b[0] / sum(b)
    assert share_a > share_b, \
        f"Population A must carry the higher young share; got {share_a:.3f} and {share_b:.3f}"
    mid_a = a[1] + a[2]
    mid_b = b[1] + b[2]
    assert mid_b > mid_a, \
        "Population B must hold more people in the middle bands, so that distractor is a true fact drawing a false conclusion"
    return (f"the young shares are {share_a * 100:.0f} and {share_b * 100:.0f} percent of "
            "equal totals, so the higher proportion of younger people belongs to the first")


def q22(table, item):
    young = cg.col(table, UNDER15)
    old = cg.col(table, OVER65)
    assert all(young[i + 1] < young[i] for i in range(len(young) - 1)), \
        f"the share under fifteen must fall at every count; got {young}"
    assert all(old[i + 1] > old[i] for i in range(len(old) - 1)), \
        f"the share sixty five and over must rise at every count; got {old}"
    return (f"the young shares read {young} percent, falling at every count, while the old "
            f"shares read {old} percent, rising at every count")


def q23(table, item):
    young = cg.col(table, UNDER15)
    old = cg.col(table, OVER65)
    assert young[-1] < young[0], "the young share must end below where it began"
    assert young[-1] < 0.5 * young[0], \
        f"the young share must fall by more than half for the structure to have moved away; got {young}"
    assert old[-1] > old[0], "the old share must end above where it began"
    assert young[-1] > 0, "'the population holds nobody under fifteen' must be false"
    return (f"the young share falls from {young[0]:.0f} to {young[-1]:.0f} percent, less "
            f"than half its starting value, while the old share rises from {old[0]:.0f} to "
            f"{old[-1]:.0f} percent")


def q24(table, item):
    young = cg.col(table, UNDER15)
    move = young[0] - young[-1]
    assert abs(move - 24) < 1e-9, f"the fall must be 24 percentage points; got {move}"
    assert move > 0, "the movement must be a fall rather than a rise"
    return (f"the share under fifteen runs from {young[0]:.0f} to {young[-1]:.0f} percent, "
            f"a fall of {move:.0f} percentage points")


def q29(table, item):
    young = dict(zip(cg.labels(table), cg.col(table, UNDER15)))
    old = dict(zip(cg.labels(table), cg.col(table, OVER65)))
    mid = cg.col(table, "Percent of population 15 to 64")
    for lab, y, m, o in zip(cg.labels(table), young.values(), mid, old.values()):
        assert abs(y + m + o - 100) < 0.5, f"{lab} must total 100 percent; got {y + m + o}"
    top = max(young, key=young.get)
    assert top == "Region 1", f"Region 1 must lead on the share under fifteen; got {top}"
    assert old[top] == min(old.values()), \
        "the region leading on the young share must also trail on the old share"
    assert len([v for v in young.values() if v == young[top]]) == 1, \
        "'all four carry the same structure' must be false"
    return (f"the shares under fifteen read {list(young.values())} percent and those sixty "
            f"five and over {list(old.values())} percent, and {top} leads the first and "
            "trails the second")


CLAIMS = [
 ("shape of a population's age structure",
  "EIN-1.A.1, near verbatim: population growth rates can be interpreted from age structure diagrams by the shape of the structure. A total, an area, a species count and a rainfall figure are none of them that shape."),
 ("higher proportion of younger people than a stable or declining population",
  "EIN-1.A.2, near verbatim: a rapidly growing population will, as a rule, have a higher proportion of younger people compared to stable or declining populations. The anchor carries the direction and the comparison together because the swapped distractor differs only in that direction."),
 ("need not hold in every single case",
  "EIN-1.A.2 hedges with AS A RULE, which states a tendency; a single departing population would therefore not contradict it, and the framework asserts no universal law."),
 ("stable populations and with declining populations",
  "EIN-1.A.2 names the comparison classes explicitly as stable or declining populations, and names no others."),
 ("growth rate to be interpreted",
  "EIN-1.A.1 states that population growth rates can be interpreted from the shape of the structure, so a set of counts by age band carries more than the total the student credits it with."),
 ("larger share under fifteen is the more rapidly growing",
  "EIN-1.A.2 attaches the higher proportion of younger people to the rapidly growing population, and the two cases here are matched on total size and differ in exactly that proportion."),
 ("exact number of years a population will take to double",
  "EIN-1.A.1 and EIN-1.A.2 supply the four rejected statements between them and neither offers any arithmetic from a shape to a rate or to a number of years. Doubling time belongs to EIN-1.C.4 in topic 3.8."),
 ("largest share of its people in the youngest band",
  "Recomputed in q8 above: one column holds much the largest youngest band share and is the only one falling monotonically with age. EIN-1.A.2 attaches that higher proportion of younger people to rapid growth."),
 ("Population 3",
  "Recomputed in q9 above: exactly one of the three columns holds more people in its two oldest bands than in its youngest. EIN-1.A.2 sets that structure against the rapidly growing case."),
 ("27 percentage points",
  "Recomputed in q10 above: the largest and smallest youngest band shares differ by 27 points. EIN-1.A.2 makes that share the quantity a comparison of growth rests on."),
 # Both clauses. The distractor is the SWAP -- fewer people, narrow based, declining --
 # and an anchor naming only the shape would match it as readily as the key.
 ("more people than the band above it, which is the broad based shape of a rapidly growing population",
  "Recomputed in q11 above: every band holds more people than the band above it. EIN-1.A.2 attaches a higher proportion of younger people to a rapidly growing population, which is what a strictly falling profile with age reports."),
 ("1,920 thousand",
  "Recomputed in q12 above: the two entries in the youngest band sum to 1,920 thousand, and neither sex alone gives that figure. EIN-1.A.1 reads the shape off the whole structure, so both columns count into a band."),
 ("3,530 thousand",
  "Recomputed in q13 above: the four entries in the two youngest bands sum to 3,530 thousand. EIN-1.A.2 makes the size of the young part of the structure the quantity that distinguishes rapid growth."),
 # Both clauses again, for the same reason: the swap is broad based and growing.
 ("fewer people than the middle bands, which is the narrow based shape of a stable or declining population",
  "Recomputed in q14 above: the youngest band is the unique smallest in the record and the middle bands the largest. EIN-1.A.2 ties a higher proportion of younger people to rapid growth, so a structure lacking that proportion is not the growing case."),
 ("40 to 49",
  "Recomputed in q15 above: adding the two sexes band by band leaves a single largest total, and it is not in the youngest band. EIN-1.A.1 makes where the structure is widest part of its shape."),
 ("nearly equal numbers, which is the near vertical shape",
  "Recomputed in q16 above: the six youngest bands sit within five percent of their mean, so the structure is neither broad based nor narrow based. EIN-1.A.2's larger young share is absent, and so is the deficit that marks decline."),
 ("larger shares under fifteen also carry the higher growth rates",
  "Recomputed in q17 above: sorting the four countries by the share under fifteen leaves the growth rate strictly increasing, and the country with the largest old share does not lead on growth. EIN-1.A.2 is the statement connecting the two."),
 ("Country 4",
  "Recomputed in q18 above: exactly one growth rate lies below zero, and it belongs to the country with the smallest share under fifteen and the largest share sixty five and over -- the structure EIN-1.A.2 sets against rapid growth."),
 ("Country 1",
  "Recomputed in q19 above: one country holds a uniquely largest share under fifteen. EIN-1.A.2 attaches the higher proportion of younger people to the most rapidly growing case."),
 ("Population A holds more than twice as many people under fifteen as Population B",
  "Recomputed in q20 above: the two columns total the same figure while one youngest band exceeds twice the other. EIN-1.A.2 makes the proportion, not the total, the quantity bearing on growth."),
 ("Population A, because a higher proportion of its people are young",
  "Recomputed in q21 above: on equal totals the first column carries the higher young share, while the second genuinely holds more people in the middle bands. EIN-1.A.2 keys growth to the proportion of younger people."),
 ("falls at every count while the share sixty five and over rises",
  "Recomputed in q22 above: one column falls at each successive count and the other rises at each. EIN-1.A.1 makes such a change in the shape of the structure the thing a growth rate is interpreted from."),
 ("moving away from the shape of a rapidly growing population",
  "Recomputed in q23 above: the young share falls to less than half its starting value while the old share rises. EIN-1.A.2 attaches the larger young share to rapid growth, so a structure losing it moves away from that shape."),
 ("fall of 24 percentage points",
  "Recomputed in q24 above: the first and last entries in the young column differ by 24 points, and the movement is downward. EIN-1.A.2 makes that share the distinguishing quantity."),
 ("comparing the shape of the resulting structure",
  "EIN-1.A.1 makes the shape of the age structure the thing a growth rate is interpreted from, so a study has to build the structure and read its shape rather than record a bare total or an unrelated quantity."),
 ("broad based structure, of the kind a rapidly growing population has",
  "EIN-1.A.2 states that a rapidly growing population will as a rule have a higher proportion of younger people, and a population with well over a third of its people under fifteen and almost none above sixty five carries exactly that proportion."),
 ("share of the whole population that falls in the younger age bands",
  "A proportion is a part expressed against a whole, which is what lets EIN-1.A.2 compare a rapidly growing population with a stable or declining one of quite different total size."),
 ("shape of a population's age structure and the population's growth rate",
  "EIN-1.A.1 puts exactly those two quantities in one sentence: growth rates can be interpreted from age structure by the shape of the structure."),
 ("Region 1",
  "Recomputed in q29 above: one region leads on the share under fifteen and trails on the share sixty five and over, and each set of shares totals one hundred. EIN-1.A.2 attaches the larger young share to the rapidly growing case."),
 ("interpreted from the shape of a population's age structure, and a rapidly growing population as a rule holds a higher proportion of younger people",
  "EIN-1.A.1 supplies the first clause and EIN-1.A.2 the second, with its direction and its comparison against stable and declining populations. The anchor carries both clauses because the rejected summary swaps only the word higher for lower."),
]

TABLE_CHECKS = {8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 13: q13, 14: q14,
                15: q15, 16: q16, 17: q17, 18: q18, 19: q19, 20: q20, 21: q21,
                22: q22, 23: q23, 24: q24, 29: q29}

if "--selftest" in sys.argv:
    es.selftest(e3_6, CLAIMS, TABLE_CHECKS)

e_check.run(e3_6, CLAIMS, TABLE_CHECKS)
