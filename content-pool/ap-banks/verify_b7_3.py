"""Key audit for AP BIOLOGY 7.3 Artificial Selection.

One (anchor, claim) per item, in module order. ``cg_check.check`` is the
structural gate; it is described in ``verify_b5_3.py``.

WHY SIXTEEN OF THE THIRTY ITEMS CARRY A TABLE. This topic has one essential
knowledge statement and its suggested skill is 4.B, describing data from a
table. SOCIAL_DEDUPE.md records what a one-statement topic does to an author
given thirty slots -- US Government 4.7 reached into two neighbouring topics and
shipped a byte-identical repeat -- and the data are what make thirty different
questions possible here without inventing content the CED does not state.
Sixteen recomputations is therefore the design, not an accident, and every one
of them is below.

WHAT IS RECOMPUTED. Specific values are located by row rather than accepted;
trends are checked step by step rather than end to end, because a series that
dips in the middle is not a trend; the range item computes largest minus
smallest; the per-generation rate divides by the generation span rather than by
the number of rows, which is the mistake its own distractor makes; the
percentage increase divides the change by the starting value, which is the
mistake ITS distractor makes; and the two-variable items confirm the two series
move in opposite directions or together as the key says.

Two structural facts the keys depend on are asserted separately: that the two
diverging lines start at the SAME mean, without which nothing follows from their
later difference, and that the control line barely moves, without which the
selected line's change is not attributable to the selection.

NEGATIVE CONTROL: ``negcontrol_b5_7.py``.
"""
import re

import cg_check as cg
import b7_3

T_SEED = b7_3._T_SEED
T_DIVERGE = b7_3._T_DIVERGE
T_RANGE = b7_3._T_RANGE
T_YIELD = b7_3._T_YIELD
T_TRADEOFF = b7_3._T_TRADEOFF
T_RESPONSE = b7_3._T_RESPONSE
T_CONTROL = b7_3._T_CONTROL
T_VARIETIES = b7_3._T_VARIETIES


def _rows(table):
    heads = [cg.normalize(h) for h in table["headers"]]
    return [dict(zip(heads, r)) for r in table["rows"]]


def _rising(vals):
    return vals == sorted(vals) and len(set(vals)) == len(vals)


# ---------------------------------------------------------------- seed mass

SEED_GEN = "generation of selective breeding"
SEED_VAL = "mean seed mass of the population milligrams"


def _seed(table):
    s = [(cg.num(r[SEED_GEN]), cg.num(r[SEED_VAL])) for r in _rows(table)]
    gens = [g for g, _ in s]
    assert _rising(gens), f"the generations must be listed in increasing order; got {gens}"
    return s


def q4(table, item):
    s = _seed(table)
    at4 = [v for g, v in s if g == 4]
    assert len(at4) == 1 and at4[0] == 161, f"generation 4 records {at4}, not 161"
    assert len({v for _, v in s}) == len(s), "no two generations may record the same mean"
    return f"the row for generation 4 records {at4[0]:.0f} milligrams, and no other row shares that value"


def q5(table, item):
    s = _seed(table)
    vals = [v for _, v in s]
    assert _rising(vals), f"the trend must rise at every step, not merely overall; got {vals}"
    assert (vals[0], vals[-1]) == (120, 195), f"the endpoints recompute to {vals[0]} and {vals[-1]}"
    return f"the five means {vals} rise at every step from {vals[0]:.0f} to {vals[-1]:.0f}"


def q6(table, item):
    s = _seed(table)
    total = s[-1][1] - s[0][1]
    span = s[-1][0] - s[0][0]
    assert total == 75, f"the total change recomputes to {total}, not 75"
    assert span == 8, f"the programme spans {span} generations, not 8"
    per = total / span
    assert 9 <= per < 10, f"the per-generation rate recomputes to {per:.2f}"
    assert abs(total / len(s) - per) > 1, (
        "dividing by the number of ROWS must give a different answer from dividing by the number "
        "of generations, or the item cannot test which denominator is right"
    )
    return (f"{s[-1][1]:.0f} less {s[0][1]:.0f} is {total:.0f} milligrams over {span:.0f} "
            f"generations, which is {per:.1f} per generation")


# ------------------------------------------------------------ diverging lines

UP = "mean bristle number in the line bred for more bristles"
DOWN = "mean bristle number in the line bred for fewer bristles"


def _diverge(table):
    s = [(cg.num(r["generation"]), cg.num(r[UP]), cg.num(r[DOWN])) for r in _rows(table)]
    assert _rising([g for g, _, _ in s]), "the generations must be listed in increasing order"
    return s


def q7(table, item):
    s = _diverge(table)
    assert s[0][1] == s[0][2], \
        f"the two lines must start at the same mean; they start at {s[0][1]} and {s[0][2]}"
    assert _rising([u for _, u, _ in s]), "the line bred upward must rise at every step"
    assert _rising([-d for _, _, d in s]), "the line bred downward must fall at every step"
    return (f"both lines start at {s[0][1]:.0f} and end at {s[-1][1]:.0f} and {s[-1][2]:.0f}, "
            f"having moved in opposite directions at every step")


def q8(table, item):
    s = _diverge(table)
    assert s[0][1] == s[0][2], "the common starting mean is what the key rests on"
    gap = abs(s[-1][1] - s[-1][2])
    assert gap > 30, f"the final gap of {gap} is too small for the point to be clear"
    return (f"the lines are identical at generation {s[0][0]:.0f} and differ by {gap:.0f} bristles "
            f"at generation {s[-1][0]:.0f}, so the difference arose during the programme")


# -------------------------------------------------------------- range and mean

SMALL = "smallest value observed grams"
LARGE = "largest value observed grams"
MEAN = "mean value grams"


def _range_table(table):
    out = []
    for r in _rows(table):
        lo, hi, mu = cg.num(r[SMALL]), cg.num(r[LARGE]), cg.num(r[MEAN])
        assert lo < mu < hi, f"the mean {mu} must lie inside the range {lo} to {hi}"
        out.append((cg.normalize(r["population"]), lo, hi, mu))
    assert len(out) == 2, "a before and after comparison needs exactly two rows"
    return out


def q9(table, item):
    (b, blo, bhi, _), (a, alo, ahi, _) = _range_table(table)
    before, after = bhi - blo, ahi - alo
    assert (before, after) == (98, 38), f"the ranges recompute to {before} and {after}"
    assert after < before, "the spread must narrow for the key to hold"
    assert after > 0, "the spread must not reach zero, which a distractor asserts"
    return f"the range falls from {bhi:.0f} less {blo:.0f}, or {before:.0f}, to {after:.0f} grams"


def q10(table, item):
    (b, blo, bhi, bmu), (a, alo, ahi, amu) = _range_table(table)
    assert (bmu, amu) == (88, 117), f"the means recompute to {bmu} and {amu}"
    assert amu > bmu, "the mean must rise for the key to hold"
    assert (ahi - alo) < (bhi - blo), "the spread must narrow at the same time"
    return (f"the mean rises {bmu:.0f} to {amu:.0f} grams while the range falls "
            f"{bhi - blo:.0f} to {ahi - alo:.0f}")


# ---------------------------------------------------------------------- yield

def _yield_table(table):
    return [(cg.normalize(r["stock"]), cg.num(r["mean yield per animal kilograms per year"]))
            for r in _rows(table)]


def q11(table, item):
    s = _yield_table(table)
    start, end = s[0][1], s[-1][1]
    pct = 100 * (end - start) / start
    assert 62 <= pct <= 64, f"the percentage increase recomputes to {pct:.1f}"
    ratio = 100 * end / start
    assert abs(ratio - pct) > 50, (
        "the final figure as a percentage of the first must differ clearly from the increase, "
        "or the item cannot test which one is asked for"
    )
    return (f"{end:.0f} less {start:.0f} is {end - start:.0f}, and {end - start:.0f} over "
            f"{start:.0f} is {pct:.0f} percent; the ratio itself is {ratio:.0f} percent")


def q12(table, item):
    s = _yield_table(table)
    vals = [v for _, v in s]
    assert _rising(vals), f"the trend must rise at every recorded point; got {vals}"
    return f"the three recorded means {vals} rise at each step"


# ------------------------------------------------------------------- trade-off

MASS = "mean mass of one fruit grams"
COUNT = "mean number of fruits per plant"


def _tradeoff(table):
    s = [(cg.num(r["generation of selection for larger fruit"]), cg.num(r[MASS]), cg.num(r[COUNT]))
         for r in _rows(table)]
    assert _rising([g for g, _, _ in s]), "the generations must be listed in increasing order"
    return s


def q13(table, item):
    s = _tradeoff(table)
    assert _rising([m for _, m, _ in s]), "fruit mass must rise at every step"
    assert _rising([-c for _, _, c in s]), "fruit number must fall at every step"
    return (f"mass rises {s[0][1]:.0f} to {s[-1][1]:.0f} grams while number falls {s[0][2]:.0f} to "
            f"{s[-1][2]:.0f}, at every step, so the two move oppositely")


def q14(table, item):
    s = _tradeoff(table)
    doubled = s[-1][1] / s[0][1]
    halved = s[-1][2] / s[0][2]
    assert abs(doubled - 2) < 0.05, f"mass changes by a factor of {doubled:.2f}, not a doubling"
    assert halved < 0.5, f"number falls to {halved:.2f} of its start, which is not more than half"
    return (f"mass goes from {s[0][1]:.0f} to {s[-1][1]:.0f}, a factor of {doubled:.2f}, and number "
            f"from {s[0][2]:.0f} to {s[-1][2]:.0f}, a factor of {halved:.2f}")


# ------------------------------------------------------------------- response

RANGE0 = "range of the trait in the starting population units"
CHANGE = "change in the mean after ten generations of selection units"


def _response(table):
    return {cg.normalize(r["starting population"]): (cg.num(r[RANGE0]), cg.num(r[CHANGE]))
            for r in _rows(table)}


def q15(table, item):
    d = _response(table)
    pairs = sorted(d.values())
    assert _rising([c for _, c in pairs]), \
        f"the change must rise with the starting range for the key to hold; got {pairs}"
    assert all(c <= r for r, c in pairs), "a change cannot exceed the range it was drawn from"
    return f"ordering by starting range gives changes {[c for _, c in pairs]}, which rise with it"


def q16(table, item):
    d = _response(table)
    narrowest = min(d, key=lambda k: d[k][0])
    assert d[narrowest][1] == min(v[1] for v in d.values()), \
        "the narrowest starting range must give the smallest change"
    assert d[narrowest][1] > 0, "the change must not be zero, which a distractor asserts"
    assert d[narrowest][1] == 1, f"the smallest change recomputes to {d[narrowest][1]}"
    return (f"{narrowest} has the narrowest starting range at {d[narrowest][0]:.0f} units and the "
            f"smallest change at {d[narrowest][1]:.0f}, which is not zero")


# -------------------------------------------------------------------- control

def q17(table, item):
    start = "mean trait value at generation 0"
    end = "mean trait value at generation 10"
    d = {cg.normalize(r["selective breeding applied"]): (cg.num(r[start]), cg.num(r[end]))
         for r in _rows(table)}
    assert set(d) == {"yes", "no"}, f"the two lines are marked {set(d)}"
    assert d["yes"][0] == d["no"][0], \
        f"the two lines must start at the same mean; they start at {d['yes'][0]} and {d['no'][0]}"
    moved = d["yes"][1] - d["yes"][0]
    drift = d["no"][1] - d["no"][0]
    assert moved > 10 * abs(drift), \
        f"the selected line moved {moved} and the unselected {drift}; the key needs the control to barely move"
    return (f"both lines start at {d['yes'][0]:.0f}; the bred line moves {moved:.0f} and the "
            f"unselected line {drift:.0f}, more than ten times less")


# ------------------------------------------------------------------ varieties

# This table is fixed stimulus and its cells carry units, so the negative
# control's numeric corruption cannot reach them: "4.2 times" is not a bare
# number. Without a format assertion the check caught one corruption in twelve.
# The factor is matched against the RAW cell, not the normalized one, because
# normalize() strips the decimal point and "1.0 times" becomes "1 0 times".
_VARIETY_LABEL = re.compile(r"(?:variety [0-9]+|wild form)")
_FACTOR = re.compile(r"[0-9]+\.[0-9] times")
_TRAIT = re.compile(r"(?:none|[a-z]+(?: [a-z]+){0,2})")


def _varieties(table):
    out = {}
    for r in _rows(table):
        label = cg.normalize(r["variety"])
        trait = cg.normalize(r["trait emphasized by the breeders"])
        factor = str(r["value of that trait relative to the wild form"]).strip()
        assert _VARIETY_LABEL.fullmatch(label), f"row label {label!r} is not a variety or the wild form"
        assert _TRAIT.fullmatch(trait), f"trait {trait!r} is not a short trait name"
        assert _FACTOR.fullmatch(factor), f"factor {factor!r} is not of the form '4.2 times'"
        out[label] = (trait, cg.num(factor))
    return out


def q19(table, item):
    d = _varieties(table)
    wild = [k for k in d if cg.contains_phrase(k, "wild form")]
    assert len(wild) == 1, "exactly one row must be the wild form"
    base = d[wild[0]]
    assert base[1] == 1.0, f"the wild form must be the baseline at 1.0 times; it reads {base[1]}"
    bred = {k: v for k, v in d.items() if k not in wild}
    traits = [v[0] for v in bred.values()]
    assert len(set(traits)) == len(traits), f"each variety must emphasize a different trait; got {traits}"
    assert all(v[1] > base[1] for v in bred.values()), "every variety must exceed the wild form"
    return (f"{len(bred)} varieties, each emphasizing a different trait ({traits}), all above the "
            f"wild form's baseline of {base[1]}")


def q20(table, item):
    d = _varieties(table)
    bred = {k: v for k, v in d.items() if not cg.contains_phrase(k, "wild form")}
    best = max(bred, key=lambda k: bred[k][1])
    assert bred[best][0] == "flower cluster size", \
        f"the largest factor belongs to the variety bred for {bred[best][0]}"
    assert len({v[1] for v in bred.values()}) == len(bred), "no two varieties may tie"
    return (f"the recorded factors are {sorted(v[1] for v in bred.values())} and the largest, "
            f"{bred[best][1]}, belongs to the variety bred for {bred[best][0]}")


CLAIMS = [
 ("They affect variation in other species",
  "EK 7.3.A.1 states that through artificial selection humans affect variation in other species. The verb is affect and the object is variation in another species, which is narrower than creating species."),
 ("Humans, who decide which individuals breed",
  "EK 7.2.A.2 makes the environment what applies selective pressures to populations and EK 7.3.A.1 makes humans the agent of artificial selection, so substituting the human choice of parents for the environmental pressure is the difference. EK 6.7.B.1 makes mutation random and so directionless."),
 ("no variation in that trait for the breeder to select among",
  "EK 7.3.A.1 has humans affect variation, and EK 7.2.A.1 makes phenotypic variation what selection acts on. Choosing among individuals requires differences to choose between; new variation arises by mutation under EK 6.7.B.1."),
 ("161 milligrams",
  "Suggested skill 4.B's first part, identifying a specific data point. The table check locates the row for the fourth generation by its own generation number and confirms no other row records the same mean."),
 ("rose at every recorded generation",
  "Skill 4.B's second part, describing a trend. The table check confirms the means rise at EVERY step rather than merely from end to end, which is what makes the rise a trend, and confirms the two endpoint values."),
 ("75 milligrams in total, which is a little over 9 milligrams per generation",
  "The table check recomputes the total as the difference between the endpoint means and the rate by dividing that by the GENERATION SPAN, then confirms that dividing by the number of rows instead would give a clearly different answer -- which is the error the rejected value makes."),
 ("began at the same mean and moved apart in opposite directions",
  "EK 7.3.A.1 has humans affect variation in other species. The table check confirms the two lines record an identical mean at the start and that one rises and the other falls at every step thereafter."),
 ("arose during the breeding programme rather than being present at the start",
  "The table check asserts the common starting mean separately, because that is what the inference rests on: with nothing distinguishing the lines at the start, a difference of more than thirty bristles at the end arose while the breeding was applied."),
 ("narrowed, from a range of 98 grams to a range of 38 grams",
  "A range is the largest value less the smallest, and the table check computes both and confirms the spread narrows without reaching zero, which is what a rejected option asserts. EK 7.3.A.1 makes an effect on variation what artificial selection produces."),
 ("mean rose from 88 to 117 grams while the spread narrowed",
  "Skill 4.B applied to two variables at once. The table check confirms the mean rises and the range falls between the same two rows, and that each mean lies inside its own range."),
 ("about 63 percent",
  "A percentage increase is the change divided by the starting value. The table check computes it and confirms that the final figure taken as a percentage of the first differs from it by more than fifty points, which is the error the rejected value makes."),
 ("rose at each recorded point in the programme",
  "Skill 4.B's second part. The table check confirms the three recorded means rise at each step, and EK 7.3.A.1 attributes such a change to humans affecting variation in the species."),
 ("mass of one fruit rose, the mean number of fruits per plant fell",
  "Skill 4.B's third part, describing a relationship between variables. The table check confirms mass rises at every step while number falls at every step across the same generations."),
 ("doubled across the eight generations while mean fruits per plant fell by more than half",
  "Skill 4.B is describing data, which is reporting what the numbers say. The table check confirms the doubling and the fall to less than half; the rejected options supply a cause, a recommendation, a prediction about untested conditions, or a generalization the table does not settle."),
 ("wider the range of the trait in the starting population, the larger the change",
  "Skill 4.B's third part. The table check orders the three populations by starting range and confirms the changes rise with it, and that no change exceeds the range it was drawn from. EK 7.2.A.1 makes variation what selection acts on."),
 ("changed the least of the three, by one unit",
  "Skill 4.B's first part. The table check confirms the population with the narrowest starting range records the smallest change and that the change is not zero, which is what a rejected option asserts."),
 ("attributable to the selective breeding, since the unselected line barely moved",
  "The table check confirms both lines start at the same mean and that the bred line's movement is more than ten times the unselected line's, which is what allows the change to be attributed to the breeding rather than to the passage of generations."),
 ("what the trait does over the same number of generations without selection",
  "EK 7.3.A.1 attributes an effect on variation to artificial selection, and attributing an observed change to it requires knowing what would have happened without it, which is what an unselected line supplies."),
 ("Different traits were emphasized in different varieties",
  "EK 7.3.A.1 states that through artificial selection humans affect variation in other species. The table check confirms each variety is recorded against a different emphasized trait and that all of them exceed the wild form's baseline of one."),
 ("flower cluster size, at 5.1 times the wild form",
  "Skill 4.B's first part. The table check confirms which of the recorded factors is largest, that no two tie, and that the wild form is the baseline rather than a competitor."),
 ("environment applies the pressure; in artificial selection humans decide",
  "EK 7.2.A.2 makes the environment what applies selective pressures and EK 7.3.A.1 makes humans the agent of artificial selection. Both act on the variation of EK 7.2.A.1 and both work through which individuals leave offspring, so the agent is what differs."),
 ("through artificial selection humans affect variation in other species",
  "EK 7.3.A.1 states this, and choosing the parents of each generation and observing the population change is what it describes. The rejected options are framework statements about other matters."),
 ("acts on the phenotypic variation present, and a breeder can only choose among the individuals that exist",
  "EK 7.2.A.1 states that selection acts on phenotypic variations in populations, and EK 7.3.A.1 has humans affect that variation rather than supply it; new variation comes from mutation under EK 6.7.B.1."),
 ("narrowed, and the data show that a narrower starting range gives a smaller response",
  "Two tables in this module carry the reasoning: one shows a range narrowing across twenty generations of breeding and another shows narrower starting ranges giving smaller changes. EK 7.2.A.1 makes phenotypic variation what selection acts on."),
 ("claim about what will happen in the next twenty generations goes beyond them",
  "Skill 4.B is describing data from a table, which covers a value and a trend the recorded numbers show. Extending the pattern to generations that were not measured is a prediction, which the table does not settle."),
 ("How humans can affect diversity within a population",
  "Learning objective 7.3.A is stated in exactly these words, with EK 7.3.A.1 supplying the mechanism. An individual's own phenotype changing during life is EK 5.5.A.1's plasticity."),
 ("each breeder affects the variation in a different direction",
  "EK 7.3.A.1 makes the effect on variation follow from which individuals the breeder allows to reproduce, and this module's divergence data show that outcome from a common starting mean."),
 ("only select among the variation present",
  "EK 7.3.A.1 has humans affect variation and EK 7.2.A.1 makes phenotypic variation what selection acts on, so choosing parents sorts what exists. EK 6.7.B.1 makes mutation the random source of anything new."),
 ("increased at every generation that was recorded",
  "Skill 4.B's second part is describing trends and patterns in the data, which is a report of the direction the recorded numbers take rather than a cause, a recommendation, a generalization or a judgement of importance."),
 ("humans allow only some individuals to breed",
  "EK 7.3.A.1 states that through artificial selection humans affect variation in other species and EK 7.2.A.1 makes phenotypic variation what any selection acts on. Each rejected account has selection create variation, has acquired changes inherited, or alters the code EK 6.4.A.3.iv makes shared."),
]

cg.check(b7_3, CLAIMS,
         table_checks={4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 12: q12,
                       13: q13, 14: q14, 15: q15, 16: q16, 17: q17, 19: q19, 20: q20})
