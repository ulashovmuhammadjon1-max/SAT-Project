"""Key audit for AP BIOLOGY 8.4 Effect of Density on Populations.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor, so an off-by-one key stops matching; the
claim states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
The conceptual items are keyed to EK 8.4.A.1 (carrying capacity is the
sustainable abundance supported by the ecosystem's total available resources)
and EK 8.4.A.2 (as limits attributable to density-dependent and
density-independent factors are imposed, a logistic growth model TYPICALLY
ensues), together with the equation the CED prints for this topic and its own
definitions of dN, dt, N, rmax and K.

THE CED NAMES THE TWO KINDS OF FACTOR AND DEFINES NEITHER. So no key here
asserts on the framework's authority that a particular factor is
density-dependent. The classification items state, in the stimulus, whether the
strength of a limit changes with crowding, and the check below reads that
property out of the table rather than out of a list this file would have had to
invent.

THE ARITHMETIC IS THE PART A MACHINE CAN SETTLE, and all of it is settled here:

  * ``STEM_MATH`` recomputes items 14 to 19 by PARSING THE NUMBERS OUT OF THE
    STEM. Each stem gives its quantities in the same order -- carrying capacity,
    then maximum per capita growth rate, then current size -- and the check
    asserts that the middle value really is a per capita rate below one, so a
    stem rewritten in a different order fails rather than being misread.
  * ``TABLE_CHECKS`` recomputes items 20 to 28 from the table plus the numbers
    the stem of the first of them states, and it VERIFIES THE TABLE ITSELF
    against the printed equation before any key is accepted.

NO GROWTH CURVE IS REFERRED TO ANYWHERE; the style pass below bars the phrases
that would promise one.

NEGATIVE CONTROL. Moving any key, changing any table cell the keys depend on,
or changing the first number in any stem the checks read makes this file raise;
confirmed by running exactly that.
"""
import re

import cg_check as cg
import b8_4

QS = b8_4.QUESTIONS
T_LOG = b8_4._T_LOG
T_FACTORS = b8_4._T_FACTORS

N_COL = "Population size N"
RATE_COL = "Change in population size per unit time"
DENSITY_COL = "Does the strength of this limit change as the population becomes more crowded?"

NUMBER_WORDS = ["Zero", "One", "Two", "Three", "Four", "Five"]

# No \b anywhere: a digit and a letter are both word characters, so \b is
# silently not a boundary next to either. Explicit lookarounds instead.
_NUM_IN_STEM = re.compile(r"(?<![A-Za-z0-9.])(\d+(?:\.\d+)?)(?![0-9]|\.\d)")


def stem_nums(item):
    return [float(x) for x in _NUM_IN_STEM.findall(item["q"])]


def keyed(item):
    return item["choices"][item["ans"]]


def raw(table, row_label, header):
    j = [cg.normalize(h) for h in table["headers"]].index(cg.normalize(header))
    i = [cg.normalize(lab) for lab in cg.labels(table)].index(cg.normalize(row_label))
    return str(table["rows"][i][j])


def _whole(x):
    assert abs(x - round(x)) < 1e-9, f"{x} must be whole for a calculator-free item"
    return int(round(x))


def logistic(rmax, n, k):
    return rmax * n * (k - n) / k


def _k_r_n(item):
    """Carrying capacity, maximum per capita growth rate, current size."""
    k, r, n = stem_nums(item)
    assert 0 < r < 1, f"the middle quantity {r} is not a per capita rate; the stem order is wrong"
    assert k >= 1 and n >= 1, f"carrying capacity {k} and size {n} must be counts of individuals"
    return k, r, n


# --------------------------------------------------------- stem arithmetic

def _rate_item(item, label):
    k, r, n = _k_r_n(item)
    value = logistic(r, n, k)
    expected = "Zero individuals per year" if value == 0 else f"{_whole(value)} individuals per year"
    assert keyed(item) == expected, \
        f"{label} key {keyed(item)!r} but the logistic equation gives {value}"
    return (f"K {int(k)}, rmax {r}, N {int(n)} give rmax times N times the unused share "
            f"{(k - n) / k:.2f}, which is {value:g}")


def m14(item):
    return _rate_item(item, "q14")


def m15(item):
    return _rate_item(item, "q15")


def m16(item):
    k, r, n = _k_r_n(item)
    assert n == k, f"this item requires a population at its carrying capacity; N is {n} and K is {k}"
    return _rate_item(item, "q16")


def m17(item):
    k, n = stem_nums(item)
    share = (k - n) / k
    assert keyed(item) == f"{share:.2f}", \
        f"q17 key {keyed(item)!r} but the unused share of {int(k)} at size {int(n)} is {share}"
    return f"K {int(k)} minus N {int(n)}, over K, is {share:.2f}"


def m18(item):
    return _rate_item(item, "q18")


def m19(item):
    k, n = stem_nums(item)
    pct = n / k * 100
    assert abs(pct - round(pct)) < 1e-9, "the percentage must be whole for a calculator-free item"
    assert keyed(item) == f"{int(round(pct))} percent", \
        f"q19 key {keyed(item)!r} but {int(n)} of {int(k)} is {pct} percent"
    return f"N {int(n)} over K {int(k)} is {int(round(pct))} percent of carrying capacity"


STEM_MATH = {14: m14, 15: m15, 16: m16, 17: m17, 18: m18, 19: m19}


# -------------------------------------------------------- table arithmetic

def _log_table(table, item):
    """Recompute the whole table from the equation and the numbers in q20's stem.

    q20 is the only item that states the carrying capacity and the per capita
    rate, so its stem is the source for every check on this table. Reading the
    parameters back out of the stem means that editing the stem without editing
    the table fails here.
    """
    k, r, _n = stem_nums(QS[19])[0], stem_nums(QS[19])[1], None
    assert 0 < r < 1, f"the per capita rate parsed from q20's stem is {r}"
    sizes = cg.col(table, N_COL)
    rates = cg.col(table, RATE_COL)
    for n, printed in zip(sizes, rates):
        computed = logistic(r, n, k)
        assert abs(computed - printed) < 1e-9, (
            f"the table prints {printed} at size {int(n)} but the equation with K {int(k)} "
            f"and rmax {r} gives {computed}"
        )
    return k, r, sizes, rates


def q20(table, item):
    k, r, sizes, rates = _log_table(table, item)
    best = max(range(len(rates)), key=lambda i: rates[i])
    assert sorted(rates)[-2] < rates[best], f"the greatest rate must be unique; the column is {rates}"
    assert cg.contains_phrase(keyed(item), f"{int(sizes[best])} individuals"), \
        f"q20 key {keyed(item)!r} but the greatest rate is at size {int(sizes[best])}"
    return f"the equation reproduces every printed rate {rates}; the maximum is at N {int(sizes[best])}"


def q21(table, item):
    k, r, sizes, rates = _log_table(table, item)
    at_k = [i for i, n in enumerate(sizes) if n == k]
    assert len(at_k) == 1, f"exactly one listed size must equal the carrying capacity {k}"
    assert rates[at_k[0]] == 0, "the size equal to the carrying capacity must print a rate of zero"
    assert max(sizes) == k, "the size equal to the carrying capacity must be the largest listed"
    return f"the largest listed size {int(k)} equals the carrying capacity, and its printed rate is zero"


def q22(table, item):
    k, r, sizes, rates = _log_table(table, item)
    pairs = [(sizes[i], sizes[j]) for i in range(len(sizes)) for j in range(i + 1, len(sizes))
             if abs(rates[i] - rates[j]) < 1e-9 and rates[i] != 0]
    assert len(pairs) == 1, f"exactly one pair of nonzero equal rates is required; found {pairs}"
    a, b = pairs[0]
    for n in (a, b):
        assert cg.contains_phrase(keyed(item), f"{int(n)} individuals"), \
            f"q22 key {keyed(item)!r} does not name size {int(n)}"
    assert abs((a + b) - k) < 1e-9, \
        f"the equal-rate pair should sit symmetrically about half the carrying capacity; {a} and {b} against K {k}"
    return f"sizes {int(a)} and {int(b)} print the same rate and sum to the carrying capacity {int(k)}"


def q23(table, item):
    k, r, sizes, rates = _log_table(table, item)
    named = [n for n in sizes if cg.contains_phrase(item["q"], f"{int(n)} individuals")]
    assert len(named) == 1, f"the stem must name exactly one listed size; it names {named}"
    value = rates[list(sizes).index(named[0])]
    assert keyed(item) == f"{_whole(value)} individuals per year", \
        f"q23 key {keyed(item)!r} but the table prints {value} at size {int(named[0])}"
    return f"the table prints {_whole(value)} at size {int(named[0])}, which the equation reproduces"


def q24(table, item):
    k, r, sizes, rates = _log_table(table, item)
    peak = max(range(len(rates)), key=lambda i: rates[i])
    upper = rates[peak:]
    assert all(y < x for x, y in zip(upper, upper[1:])), \
        f"the key says the rate falls above the peak; the upper entries are {upper}"
    return f"above the peak at N {int(sizes[peak])} the printed rates run {upper}, falling at every step"


def q25(table, item):
    k, r, sizes, rates = _log_table(table, item)
    assert rates[list(sizes).index(max(sizes))] == 0, \
        "the key says the rate falls toward zero near the carrying capacity"
    assert max(sizes) == k, "the largest listed size must be the carrying capacity"
    assert min(rates) == 0, "no printed rate may be negative for this key"
    return f"the printed rates {rates} reach zero exactly at the carrying capacity {int(k)}"


def _density(table):
    out = {}
    for lab in cg.labels(table):
        v = cg.normalize(raw(table, lab, DENSITY_COL))
        assert v in ("yes", "no"), f"{lab}: the density column reads {v!r}, not yes or no"
        out[lab] = v == "yes"
    return out


def q26(table, item):
    marks = _density(table)
    n = sum(1 for v in marks.values() if v)
    assert keyed(item) == NUMBER_WORDS[n], \
        f"q26 key {keyed(item)!r} but {n} rows record a strength that changes with crowding"
    assert n < len(marks), "at least one row must be density-independent for the count to mean anything"
    return f"{n} of the {len(marks)} listed limits change in strength as the population becomes more crowded"


def q27(table, item):
    marks = _density(table)
    independent = [lab for lab, v in marks.items() if not v]
    assert len(independent) == 1, f"exactly one row must be density-independent; {independent} are"
    words = cg.normalize(independent[0]).split()
    grams = [" ".join(words[i:i + 4]) for i in range(len(words) - 3)]
    assert any(cg.contains_phrase(keyed(item), g) for g in grams), \
        f"q27 key {keyed(item)!r} quotes no four-word run of the density-independent row"
    for lab, v in marks.items():
        if v:
            w = cg.normalize(lab).split()
            gs = [" ".join(w[i:i + 4]) for i in range(len(w) - 3)]
            assert not any(cg.contains_phrase(keyed(item), g) for g in gs), \
                f"q27 key {keyed(item)!r} also quotes {lab!r}, which is density-dependent"
    return f"only {independent[0]!r} records a strength that does not change with crowding"


def q28(table, item):
    marks = _density(table)
    assert any(marks.values()) and not all(marks.values()), \
        "the column must separate the rows for the key's claim about it to hold"
    assert cg.contains_phrase(item["table"]["headers"][1], "more crowded"), \
        "the second column must be the one reporting how strength changes with crowding"
    return "the second column reports whether each limit's strength changes with crowding, and it separates the rows"


TABLE_CHECKS = {20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25,
                26: q26, 27: q27, 28: q28}


CLAIMS = [
 ("sustainable abundance of a species that can be supported",
  "EK 8.4.A.1 defines carrying capacity as the sustainable abundance of a species that can be supported by the ecosystem's total available resources. It is not a record of past abundance and not a growth rate."),
 ("The ecosystem's total available resources",
  "EK 8.4.A.1 names the ecosystem's total available resources as what supports the sustainable abundance. The current population size is what carrying capacity is compared against, not what sets it."),
 ("can go on supporting rather than one reached briefly",
  "EK 8.4.A.1 uses the word SUSTAINABLE, which points to what the available resources can go on supporting. A momentary peak is a different quantity, which is why the definition is not about a maximum ever reached."),
 ("A logistic growth model",
  "EK 8.4.A.2 states that as limits to growth attributable to density-dependent and density-independent factors are imposed, a logistic growth model typically ensues. Exponential growth is what EK 8.3.A.2 assigns to reproduction without constraints."),
 ("not an outcome guaranteed in every case",
  "EK 8.4.A.2 writes TYPICALLY rather than always. A stated tendency describes the usual outcome and leaves room for departures, so an absolute reading overstates the sentence."),
 ("The carrying capacity",
  "The CED defines K as the carrying capacity in the logistic growth equation for this topic. N is the current population size, rmax the maximum per capita growth rate and dN the change in population size."),
 ("unused share of the carrying capacity is smaller",
  "The CED prints dN/dt equal to rmax times N times the quantity K minus N all divided by K. Holding rmax and N fixed while lowering K shrinks the last factor, so the whole product shrinks, and the factor stays positive because the stem keeps N below K. Recomputed numerically in ``falling_k`` below rather than argued. This item replaced a straight definition of rmax, which b8_3 already asks of the exponential equation; a cross-topic scan scored the pair at 0.75 and SOCIAL_DEDUPE.md says to change the ask, not the wording."),
 ("approaches one, so the growth term is close to what unconstrained growth would give",
  "With N small compared with K the numerator K minus N is nearly K, so the quotient is nearly one and the whole expression is nearly rmax times N, which is the product EK 8.3.A.2's exponential equation gives."),
 ("Zero, so the change in population size per unit time is zero",
  "If N equals K then K minus N is zero, so the quotient and therefore the whole product are zero whatever rmax and N are. That is how the printed equation represents a population at its carrying capacity."),
 ("negative value, so the model predicts a decline",
  "If N exceeds K then K minus N is negative, so the quotient is negative and the product is negative. This is what the printed equation yields; the framework does not discuss the case separately, and the claim rests on the equation rather than on a further sentence."),
 ("Whether the strength of the limit changes as the population becomes more crowded",
  "EK 8.4.A.2 names density-dependent and density-independent factors and defines neither, so the only division the framework itself supplies is the one carried in the two words: whether the effect depends on the density of the population it acts on."),
 ("density-dependent",
  "EK 8.4.A.2 names density-dependent factors without listing any, so the classification rests on the division the term makes. The scenario itself states that the strength of the limit rises as the population becomes more crowded."),
 ("density-independent",
  "EK 8.4.A.2 names density-independent factors without listing any, so the classification rests on the division the term makes. The scenario itself states that the proportion removed does not change with density."),
 ("16 individuals per year",
  "The CED prints dN/dt equal to rmax times N times the quantity K minus N all divided by K. Recomputed in the stem-math check above from the three numbers the stem states; omitting the last factor gives one of the distractors."),
 ("40 individuals per year",
  "The same printed equation, recomputed above. This population sits at half its carrying capacity, so the last factor is one half and the product is half of rmax times N."),
 ("Zero individuals per year",
  "If N equals K the last factor of the printed equation is zero, so the product is zero however large rmax and N may be. The check above confirms from the stem that the population is at its carrying capacity."),
 ("0.75",
  "The last factor of the printed equation is the share of the carrying capacity still unused. Recomputed above from the two numbers the stem states."),
 ("45 individuals per year",
  "The same printed equation, recomputed above from the three numbers the stem states: the per capita rate times the population size, multiplied by the unused share of the carrying capacity."),
 ("25 percent",
  "Skill 5.A includes percentages. Recomputed above as the current size divided by the carrying capacity; the complement of that figure is the unused share the equation uses."),
 ("500 individuals",
  "The printed equation multiplies a term rising with N by a term falling as N approaches K, so the product peaks between the extremes. The table check above reproduces EVERY printed rate from the equation and the stem's parameters before locating the unique maximum."),
 ("population size equals the carrying capacity",
  "The stem states the carrying capacity and the largest listed size equals it, so the printed equation's last factor is zero. The table check confirms both facts; a rate of zero is not the same as no births and no deaths occurring."),
 ("100 individuals and 900 individuals",
  "The equation multiplies a rising factor by a falling one, so sizes placed symmetrically about half the carrying capacity give the same product. The table check above confirms exactly one such pair exists and that the two sizes sum to the carrying capacity."),
 ("9 individuals per year",
  "Skill 4.B, identifying a specific data point, checked against skill 5.A. The table check above confirms the printed value at the named size is what the equation gives for the stated carrying capacity and per capita rate."),
 ("It falls",
  "The last factor of the printed equation shrinks toward zero as N approaches K, and beyond the peak that shrinking outweighs the rising factor. The table check above confirms the printed rates fall at every step above the peak."),
 ("falls toward zero, so its size levels off",
  "EK 8.4.A.2 states that a logistic growth model typically ensues once limits are imposed, and the printed equation drives the change in population size to zero as N approaches K. The table check confirms the printed rate reaches zero exactly at the carrying capacity."),
 ("Three",
  "EK 8.4.A.2 names density-dependent factors without listing any, so the count must come from the stimulus. The table check above counts the rows whose strength the table records as changing with crowding, and confirms at least one row is not of that kind."),
 ("frost that kills the same proportion of individuals",
  "EK 8.4.A.2 names density-independent factors and defines none, so the classification rests on the division the term makes. The table check confirms exactly one row records a strength that does not change with crowding, and that the key quotes that row and no other."),
 ("changes with crowding, which is exactly what the two terms divide on",
  "EK 8.4.A.2 names the two kinds of factor and defines neither, so the only division the framework supplies is dependence or independence with respect to population density. That is the property the table's second column reports."),
 ("multiplies the same product of per capita rate and population size by the unused share",
  "The CED prints dN/dt equal to rmax times N for reproduction without constraints in EK 8.3.A.2, and dN/dt equal to rmax times N times the quantity K minus N all divided by K here. The second is the first multiplied by one additional factor."),
 ("once limits attributable to density-dependent and density-independent factors are imposed a logistic growth model typically ensues",
  "EK 8.4.A.1 defines carrying capacity as the sustainable abundance supported by the ecosystem's total available resources, and EK 8.4.A.2 supplies the second half. Each distractor contradicts one of those two sentences."),
]


# SCIENCE_BRIEF.md: Biology is exported untypeset, so a backslash macro or a
# dollar span would reach a student as literal characters, and a
# digit-hyphen-digit run reads as a subtraction. Explicit lookarounds, never \b.
_BANNED = [
    (re.compile(r"\\"), "a backslash: this bank carries no LaTeX"),
    (re.compile(r"\$"), "a dollar-delimited math span"),
    (re.compile(r"(?<![A-Za-z])\d+\s*-\s*\d+(?![A-Za-z])"), "a digit-hyphen-digit range"),
    (re.compile(r"\d\s*/\s*\d"), "a digit-slash-digit fraction"),
]

# The logistic curve is the classic figure for this topic and the bank cannot
# show one, which is exactly the defect SCIENCE_BRIEF.md says this project has
# already shipped. Every phrase promising a picture is barred.
_FIGURE_TALK = re.compile(
    r"(?<![A-Za-z])(the (?:graph|curve|figure|diagram|chart|plot) (?:shown|above|below)|"
    r"in the (?:graph|curve|figure|diagram|chart|plot) (?:shown|above|below)|"
    r"shown in the (?:graph|curve|figure|diagram|chart|plot))(?![A-Za-z])",
    re.IGNORECASE)


def style():
    hits = 0
    for i, item in enumerate(QS, 1):
        texts = [("stem", item["q"]), ("why", item["why"])]
        texts += [(f"choice {k}", c) for k, c in enumerate(item["choices"])]
        if item.get("table"):
            texts.append(("table", " | ".join(item["table"]["headers"])))
            texts += [("table", " | ".join(str(c) for c in r)) for r in item["table"]["rows"]]
        for where, text in texts:
            for pat, why_bad in _BANNED:
                m = pat.search(text)
                assert not m, f"q{i} {where} contains {m.group(0)!r}, {why_bad}"
                hits += 1
            m = _FIGURE_TALK.search(text)
            assert not m, (
                f"q{i} {where} says {m.group(0)!r}, promising a figure the bank cannot show"
            )
            hits += 1
    return hits


def falling_k():
    """q7's key, recomputed rather than argued.

    Lower the carrying capacity while holding the per capita rate and the
    population size fixed, keeping the population below the new capacity, and
    confirm the printed equation gives a SMALLER change in population size per
    unit time and that it stays positive.
    """
    r, n = 0.10, 200.0
    before, after = logistic(r, n, 1000.0), logistic(r, n, 600.0)
    assert 0 < after < before, (
        f"lowering the carrying capacity must shrink the rate while leaving it positive; "
        f"got {before} then {after}"
    )
    return f"with rmax {r} and N {int(n)}, lowering K from 1000 to 600 takes the rate from {before:g} to {after:g}"


def main():
    n_style = style()
    note_k = falling_k()
    notes = []
    for i, fn in sorted(STEM_MATH.items()):
        item = QS[i - 1]
        assert "table" not in item, f"q{i} has a table; it belongs in TABLE_CHECKS"
        notes.append(f"  q{i:>2}: {fn(item)}")
    cg.check(b8_4, CLAIMS, table_checks=TABLE_CHECKS)
    print(f"    {n_style} notation and figure-reference checks clean.")
    print(f"    q 7: {note_k}")
    print(f"    {len(STEM_MATH)} stem calculation(s) recomputed from the stem text:")
    print("\n".join(notes))


main()
