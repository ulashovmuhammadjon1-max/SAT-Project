"""Key audit for AP ENVIRONMENTAL SCIENCE 3.2 K-Selected r-Selected Species.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
ERT-3.B.1  the K-selected profile and the usually high competition in its
           habitats            -- items 1, 3, 5, 6, 7, 8, 9, 10, 17, 20, 30
ERT-3.B.2  the r-selected profile and the typically low competition in its
           habitats            -- items 2, 4, 5, 6, 7, 8, 9, 18, 20, 21, 30
ERT-3.B.3  biotic potential is the maximum reproductive rate of a population in
           ideal conditions     -- items 11, 12, 26, 27, 30
ERT-3.B.4  many species are not uniquely r-selected or K-selected, or their
           strategies change in different conditions at different times
                                -- items 13, 14, 28, 29, 30
ERT-3.B.5  K-selected species are typically more adversely affected by invasive
           species than r-selected species, which are minimally affected; most
           invasive species are r-selected
                                -- items 15, 16, 22, 23, 24, 25, 30

THE TWO PROFILES ARE MIRROR IMAGES, WHICH MAKES THE SWAP THE STANDING HAZARD.
Every distractor set naming both kinds contains the reversed statement, so the
anchors for items 5, 6, 7, 8, 9, 15, 20 and 22 carry BOTH clauses -- which kind
and which trait. Half an anchor matches the swap as readily as the key; that
defect was found once already in verify_e2_1.py.

ERT-3.B.4 IS KEYED TWICE AND CONSTRAINS EVERYTHING ELSE: no key here says a
species must be one kind or the other. Items 13, 14, 28 and 29 turn on that,
and the two-species tables behind 28 and 29 are built so that neither row is a
clean member of either category.

WHAT IS DELIBERATELY NOT ASKED. The framework gives no formula for biotic
potential, no survivorship curve (ERT-3.C, topic 3.3) and no carrying capacity
(ERT-3.D, topic 3.4). ERT-3.B.5 is written with TYPICALLY and MOST and no key
hardens either into a rule.

DATA ITEMS: 17 to 29 carry tables, recomputed below by column header. Two of
those tables carry a text column, read cell by cell rather than through
``cg.col``.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and EVERY data table in turn, and requires each
corruption to raise BEFORE the real gate runs. Several checks read a ratio, a
total or a relationship that a column reversal preserves; e_check flattens
those tables next and each check fails because a flat column has no ratio, no
distinct total and no relationship left. ``python3 verify_e3_2.py --selftest``
is the same run; the controls are not behind the flag.
"""
import sys

import cg_check as cg
import e_check
import e3_2

MASS = "Adult mass (kilograms)"
OFFSPRING = "Offspring per reproduction event"
MATURITY = "Age at maturity (years)"
LIFESPAN = "Typical life span (years)"
COMPET = "Competition for resources (index)"
KPROF = "Species with the K-selected profile present"
RPROF = "Species with the r-selected profile present"
STRATEGY = "Reproductive strategy recorded for it"
DECLINE = "Percent decline in its numbers after the invasive species arrived"
NR = "Number classified as r-selected"
NK = "Number classified as K-selected"
IDEAL = "Maximum offspring per female per year under ideal conditions"
FIELD = "Offspring per female per year recorded in the field"
ENERGY = "Energy invested per offspring (relative units)"


def _rises(v):
    return all(v[i + 1] > v[i] for i in range(len(v) - 1))


def _falls(v):
    return all(v[i + 1] < v[i] for i in range(len(v) - 1))


def _by(table, key_header, *headers):
    keys = cg.col(table, key_header)
    order = sorted(range(len(table["rows"])), key=lambda i: keys[i])
    return [[cg.col(table, h)[i] for i in order] for h in headers]


def _textcol(table, header):
    """A non-numeric column, read by header name."""
    j = [cg.normalize(h) for h in table["headers"]].index(cg.normalize(header))
    return [str(r[j]) for r in table["rows"]]


def q17(table, item):
    labs = cg.labels(table)
    rows = dict(zip(labs, zip(cg.col(table, MASS), cg.col(table, OFFSPRING),
                              cg.col(table, MATURITY), cg.col(table, LIFESPAN))))
    kish = [lab for lab, (m, o, a, l) in rows.items()
            if m > 100 and o <= 2 and a >= 4 and l >= 20]
    assert kish == ["Species 1", "Species 3"], \
        f"exactly the first and third species must carry the K profile; got {kish}"
    return (f"exactly two rows are heavy, produce at most two offspring, mature after four "
            f"years or more and live twenty years or more: {kish}; the measurements are {rows}")


def q18(table, item):
    labs = cg.labels(table)
    mass = dict(zip(labs, cg.col(table, MASS)))
    off = dict(zip(labs, cg.col(table, OFFSPRING)))
    mat = dict(zip(labs, cg.col(table, MATURITY)))
    life = dict(zip(labs, cg.col(table, LIFESPAN)))
    picks = {min(mass, key=mass.get), max(off, key=off.get),
             min(mat, key=mat.get), min(life, key=life.get)}
    assert picks == {"Species 2"}, \
        f"one species must be lightest, most fecund, earliest to mature and shortest lived; got {picks}"
    return ("the same row is the lightest, the most fecund, the earliest to mature and the "
            "shortest lived of the four")


def q19(table, item):
    off = cg.col(table, OFFSPRING)
    ratio = max(off) / min(off)
    assert ratio == 3000, f"the ratio must be 3,000; got {ratio}"
    assert ratio != max(off) - min(off), \
        "the ratio must not coincide with the difference between the two counts"
    return (f"the offspring counts are {off} and the largest divided by the smallest is "
            f"{ratio:.0f}")


def q20(table, item):
    k, r = _by(table, COMPET, KPROF, RPROF)
    assert _rises(k), f"the K profile count must rise with competition; got {k}"
    assert _falls(r), f"the r profile count must fall as competition rises; got {r}"
    return (f"sorted by the competition index the K profile counts read {k} and the r "
            f"profile counts {r}, one strictly rising and the other strictly falling")


def q21(table, item):
    labs = cg.labels(table)
    r = dict(zip(labs, cg.col(table, RPROF)))
    comp = dict(zip(labs, cg.col(table, COMPET)))
    top = max(r, key=r.get)
    assert top == "Habitat 4", f"Habitat 4 must hold the most r profile species; got {top}"
    assert comp[top] == min(comp.values()), \
        "the habitat with the most r profile species must have the lowest competition index"
    assert len(set(r.values())) == len(r), "'all four hold the same number' must be false"
    return (f"the r profile counts are {r} and the largest belongs to {top}, whose "
            f"competition index {comp[top]:.0f} is the lowest")


def q22(table, item):
    strat = _textcol(table, STRATEGY)
    dec = cg.col(table, DECLINE)
    kd = [d for s, d in zip(strat, dec) if s == "K-selected"]
    rd = [d for s, d in zip(strat, dec) if s == "r-selected"]
    assert len(kd) == 2 and len(rd) == 2, \
        f"two natives of each strategy must be tabulated; got {kd} and {rd}"
    assert min(kd) > max(rd), \
        f"every K-selected decline must exceed every r-selected one; got {kd} against {rd}"
    assert min(kd) > 5 * max(rd), \
        "'the two strategies declined by about the same amount' must be false"
    assert min(rd) > 0, "'only the r-selected natives declined' must be false in reverse"
    return (f"the K-selected natives fell {kd} percent and the r-selected natives {rd}, "
            "with no overlap between the two sets")


def q23(table, item):
    dec = cg.col(table, DECLINE)
    spread = max(dec) - min(dec)
    assert spread == 59, f"the spread must be 59 percentage points; got {spread}"
    assert spread != max(dec) and spread != min(dec), \
        "the spread must not coincide with either endpoint"
    return (f"the declines run {max(dec):.0f} percent to {min(dec):.0f} percent, a spread of "
            f"{spread:.0f} points")


def q24(table, item):
    labs = cg.labels(table)
    for lab, r, k in zip(labs, cg.col(table, NR), cg.col(table, NK)):
        assert r > k, f"{lab}: the r-selected count {r} must exceed the K-selected count {k}"
        assert r > 0, f"{lab}: some invasive species must be classified r-selected"
    return ("in every one of the three surveys the r-selected classification outnumbers the "
            f"K-selected one: {list(zip(labs, cg.col(table, NR), cg.col(table, NK)))}")


def q25(table, item):
    tr = sum(cg.col(table, NR))
    tk = sum(cg.col(table, NK))
    assert tr == 101 and tk == 13, f"the totals must be 101 and 13; got {tr} and {tk}"
    assert tr != tk, "'equally represented' must be false"
    return f"the two columns total {tr:.0f} r-selected against {tk:.0f} K-selected"


def q26(table, item):
    labs = cg.labels(table)
    for lab, ideal, field in zip(labs, cg.col(table, IDEAL), cg.col(table, FIELD)):
        assert field < ideal, \
            f"{lab}: the field rate {field} must fall short of the ideal maximum {ideal}"
    return ("every population's field rate falls short of its ideal maximum: "
            f"{list(zip(labs, cg.col(table, IDEAL), cg.col(table, FIELD)))}")


def q27(table, item):
    labs = cg.labels(table)
    ideal = dict(zip(labs, cg.col(table, IDEAL)))
    top = max(ideal, key=ideal.get)
    assert top == "Population 1", \
        f"Population 1 must hold the largest ideal maximum; got {top}"
    assert len(set(ideal.values())) == len(ideal), \
        "'all three have the same biotic potential' must be false"
    return (f"the ideal maxima are {ideal} offspring per female per year, and the largest "
            f"belongs to {top}")


def q28(table, item):
    labs = cg.labels(table)
    off = dict(zip(labs, cg.col(table, OFFSPRING)))
    en = dict(zip(labs, cg.col(table, ENERGY)))
    mat = dict(zip(labs, cg.col(table, MATURITY)))
    assert off["Species X"] > 100 and en["Species X"] < 10, \
        f"the first species must be fecund and cheap per offspring; got {off['Species X']}, {en['Species X']}"
    assert mat["Species X"] >= 4, \
        f"the first species must nonetheless mature late; got {mat['Species X']}"
    assert off["Species Y"] < 10 and en["Species Y"] > 50, \
        f"the second species must be sparing and costly per offspring; got {off['Species Y']}, {en['Species Y']}"
    assert mat["Species Y"] < 2, \
        f"the second species must nonetheless mature early; got {mat['Species Y']}"
    return ("one species pairs many cheap offspring with late maturity and the other pairs "
            "few costly offspring with early maturity, so neither set of traits is wholly "
            "of one kind")


def q29(table, item):
    labs = cg.labels(table)
    off = dict(zip(labs, cg.col(table, OFFSPRING)))
    en = dict(zip(labs, cg.col(table, ENERGY)))
    crowded = "Crowded, with resources scarce"
    easy = "Uncrowded, with resources abundant"
    assert off[crowded] < off[easy], \
        f"the crowded condition must yield fewer offspring; got {off}"
    assert en[crowded] > en[easy], \
        f"the crowded condition must yield more energy invested in each; got {en}"
    return (f"the same species produces {off[crowded]:.0f} offspring at {en[crowded]:.0f} "
            f"units each when crowded and {off[easy]:.0f} at {en[easy]:.0f} units each when "
            "not")


CLAIMS = [
 ("significant energy expended for each offspring, and long life spans",
  "ERT-3.B.1 states that K-selected species tend to be large, have few offspring per reproduction event, expend significant energy for each offspring, and have long life spans. Each rejected set exchanges at least one of those for its opposite."),
 ("minimal energy invested for each offspring, and short life spans",
  "ERT-3.B.2 states that r-selected species tend to be small, have many offspring, expend or invest minimal energy for each offspring, and have short life spans. Each rejected set exchanges at least one for its opposite."),
 ("usually relatively high",
  "ERT-3.B.1 closes by stating that competition for resources in K-selected species' habitats is usually relatively high, which the word usually makes a prevailing level rather than a rule."),
 ("typically relatively low",
  "ERT-3.B.2 closes by stating that competition for resources in r-selected species' habitats is typically relatively low, the opposite of the level ERT-3.B.1 gives for K-selected habitats."),
 # Both clauses in each of the next five, because every distractor set holds the swap.
 ("K-selected species tend to have few offspring and r-selected species many",
  "ERT-3.B.1 gives K-selected species few offspring per reproduction event and ERT-3.B.2 gives r-selected species many. The rejected options exchange the two, collapse them, or deny the claim."),
 ("expend significant energy for each offspring and r-selected species minimal energy",
  "ERT-3.B.1 has K-selected species expend significant energy for each offspring and ERT-3.B.2 has r-selected species expend or invest minimal energy for each."),
 ("mature after many years of extended youth and parental care, while r-selected species mature early",
  "ERT-3.B.1 has K-selected species mature after many years of extended youth and parental care and ERT-3.B.2 has r-selected species mature early."),
 ("tend to have long life spans and r-selected species short ones",
  "ERT-3.B.1 gives K-selected species long life spans and life expectancy and ERT-3.B.2 gives r-selected species short life spans."),
 ("reproduce more than once, while r-selected species may reproduce only once",
  "ERT-3.B.1 states that K-selected species reproduce more than once in their lifetime and ERT-3.B.2 that r-selected species may reproduce only once."),
 ("Stable environments",
  "ERT-3.B.1 states outright that K-selected species live in stable environments, and separately gives their habitats a usually high level of competition for resources."),
 ("maximum reproductive rate of a population in ideal conditions",
  "ERT-3.B.3, near verbatim: biotic potential refers to the maximum reproductive rate of a population in ideal conditions. It is a maximum under ideal conditions, not an observed rate or an environmental limit."),
 ("reproduce at less than its biotic potential",
  "ERT-3.B.3 makes biotic potential a MAXIMUM reached under IDEAL conditions, so a population in conditions less than ideal cannot exceed it and will in general fall short."),
 ("not uniquely r-selected or K-selected",
  "ERT-3.B.4 states that many species have reproductive strategies that are not uniquely r-selected or K-selected, so the two categories are not a partition of all species and the exception is not confined to any one group."),
 ("Change in different conditions at different times",
  "ERT-3.B.4's second clause states that reproductive strategies may change in different conditions at different times, which allows one species' strategy to differ between occasions."),
 # Both clauses, because the distractor is the SWAP.
 ("K-selected species, while r-selected species are minimally affected",
  "ERT-3.B.5 states that K-selected species are typically more adversely affected by invasive species than r-selected species, which are minimally affected. The rejected options exchange the kinds, level them, or deny the difference."),
 ("Most invasive species are r-selected",
  "ERT-3.B.5 states that most invasive species are r-selected species, and the word most makes it a majority rather than a rule without exceptions."),
 ("The first and the third species",
  "Recomputed in q17 above: exactly two of the four rows are heavy, produce at most two offspring, mature after four years or more and live twenty years or more. ERT-3.B.1 gives K-selected species that combination."),
 ("Species 2",
  "Recomputed in q18 above: one row is simultaneously the lightest, the most fecund, the earliest to mature and the shortest lived. ERT-3.B.2 gives r-selected species exactly that combination."),
 ("Three thousand times",
  "Recomputed in q19 above: 3,000 offspring divided by 1 is 3,000, and that is not the difference between the two counts. The rejected values are other entries in the same column."),
 # Both clauses: the distractor swaps which kind is commoner where.
 ("K-selected profile are commoner where competition is higher",
  "Recomputed in q20 above: sorted by the competition index the K profile counts strictly rise and the r profile counts strictly fall. ERT-3.B.1 gives K-selected habitats a usually high level of competition and ERT-3.B.2 gives r-selected habitats a typically low one."),
 ("Habitat 4",
  "Recomputed in q21 above: the largest r profile count belongs to the habitat with the lowest competition index. ERT-3.B.2 states that competition in r-selected species' habitats is typically relatively low."),
 # Both clauses: the distractor swaps which strategy declined.
 ("K-selected natives declined far more than the r-selected natives",
  "Recomputed in q22 above: every K-selected decline exceeds every r-selected one, and by more than a factor of five. ERT-3.B.5 states that K-selected species are typically more adversely affected by invasive species than r-selected species, which are minimally affected."),
 ("59 points",
  "Recomputed in q23 above: 62 percent less 3 percent is 59 points. The rejected values are the endpoints or differences between other pairs of rows."),
 ("most of the invasive species were r-selected",
  "Recomputed in q24 above: in each of the three surveys the r-selected count exceeds the K-selected one. ERT-3.B.5 states that most invasive species are r-selected species."),
 ("101 r-selected against 13 K-selected",
  "Recomputed in q25 above: the columns total 101 and 13. The rejected options reverse the totals, level them, or give one survey's figures instead."),
 ("more slowly in the field than its ideal maximum",
  "Recomputed in q26 above: every field rate falls short of its own ideal maximum. ERT-3.B.3 makes biotic potential the MAXIMUM reproductive rate under IDEAL conditions, which field conditions do not meet."),
 ("Population 1",
  "Recomputed in q27 above: the largest ideal maximum is 900 offspring per female per year. ERT-3.B.3 defines biotic potential as that ideal-conditions maximum, so the field column is a different quantity."),
 ("Neither species carries a wholly r-selected or a wholly K-selected",
  "Recomputed in q28 above: one row pairs many cheap offspring with late maturity and the other pairs few costly offspring with early maturity, so neither set of traits is wholly of one kind. ERT-3.B.4 states that many species have strategies that are not uniquely r-selected or K-selected."),
 ("few, heavily provisioned offspring under one set of conditions and many",
  "Recomputed in q29 above: the same species produces few costly offspring when crowded and many cheap ones when not. ERT-3.B.4 states that reproductive strategies may change in different conditions at different times."),
 ("invasive species, mostly r-selected, affect K-selected natives more",
  "ERT-3.B.1 and ERT-3.B.2 supply the two mirrored profiles and their competition levels, ERT-3.B.3 the ideal-conditions maximum, ERT-3.B.4 the species that fit neither, and ERT-3.B.5 both the greater harm to K-selected natives and the r-selected majority among invaders. Each rejected summary swaps a profile, redefines biotic potential, makes the categories exhaustive, or reverses one half of the invasive-species claim."),
]

TABLE_CHECKS = {17: q17, 18: q18, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23,
                24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29}

if "--selftest" in sys.argv:
    print("note: e_check.run negative-controls every gate on every run; "
          "--selftest is the same run, not a separate one.")

e_check.run(e3_2, CLAIMS, TABLE_CHECKS)
