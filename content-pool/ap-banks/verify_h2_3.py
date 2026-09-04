"""Key audit for AP CHEMISTRY 2.3 Structure of Ionic Solids.

One ``(anchor, claim)`` per item, in module order; the anchor must appear in the
KEYED choice and in no distractor. All fourteen table items and the one
stem-numeric item are recomputed from their own stimulus.

WHAT THE KEYS REST ON
---------------------
EK 2.3.A.1  The cations and anions in an ionic crystal are arranged in a
            systematic, periodic 3-D array that maximizes the attractive forces
            among cations and anions while minimizing the repulsive forces.
            (items 1, 2, 3, 7, 9, 11, 15, 21, 23, 27, 29)
LO 2.3.A    Represent an ionic solid with a particulate model that is
            consistent with Coulomb's law AND the properties of the constituent
            ions.  (items 5, 19, 27)
EK 2.2.A.3  Coulomb's law between cations and anions: (i) strength is
            proportional to the charge on each ion, (ii) strength increases as
            the distance between the ion centers decreases.
            (items 4, 6, 8, 10, 12, 13, 14, 16, 17, 18, 20, 22, 24, 25, 26,
            28, 30)

WHY SO MANY DATA ITEMS. This topic has ONE essential-knowledge sentence.
Restating it thirty ways would produce thirty questions with one answer between
them, so the arithmetic that LO 2.3.A itself calls for -- Coulomb's law over the
charges and sizes of the constituent ions -- carries fourteen of the items, and
each asks a different question of the numbers. Every one is recomputed here from
the table alone, and each Coulombic ranking is checked under BOTH an
inverse-square and an inverse-distance law, so no key depends on which power a
student uses.

THE EXCLUSION STATEMENT IS GATED. ``excluded_material_only_as_a_distractor``
asserts that no stem and no KEYED choice mentions a unit cell, a coordination
number, a packing fraction or a named crystal structure. Item 23 deliberately
puts four such tasks in its rejected options -- that is how an exclusion
statement gets taught -- so the gate permits them there and nowhere else.

SCOPE. ``no_macroscopic_property`` keeps EK 3.2.A.3's melting points, vapor
pressures, brittleness and conduction inside topic 3.2, where they belong.

NEGATIVE CONTROL: ``python3 verify_h2_3.py --selftest``.
"""
import re
import sys

import h_chem_notation as hn
import h2_3 as M

QCAT = "Charge on the cation"
QAN = "Charge on the anion"
SEP = "Distance between neighboring ion centers (picometers)"
RCAT = "Radius of the cation (picometers)"
RAN = "Radius of the anion (picometers)"
NCAT = "Nearest neighbors of each cation"
NAN = "Nearest neighbors of each anion"

cg = hn.cg


# ----------------------------------------------------------------- helpers

def ion_rows(table):
    """(label, charge product magnitude, separation) for every tabulated compound."""
    return [(lab, abs(qc * qa), r) for lab, qc, qa, r in
            zip(cg.labels(table), cg.col(table, QCAT), cg.col(table, QAN),
                cg.col(table, SEP))]


def radius_rows(table):
    """(label, charge product of 1, sum of the two radii) -- the same shape as ion_rows."""
    return [(lab, 1.0, rc + ra) for lab, rc, ra in
            zip(cg.labels(table), cg.col(table, RCAT), cg.col(table, RAN))]


def ordered(rows, power=2):
    """Labels strongest first under Coulomb's law at the given power of distance."""
    return [lab for lab, _ in
            sorted(((lab, q / r ** power) for lab, q, r in rows),
                   key=lambda p: p[1], reverse=True)]


def ranking(rows):
    """The strongest-first ranking, refused unless it is the same at both powers."""
    square, linear = ordered(rows, 2), ordered(rows, 1)
    assert square == linear, (
        f"the ranking depends on the power of the distance: {square} against {linear}"
    )
    scores = sorted(q / r ** 2 for _, q, r in rows)
    for a, b in zip(scores, scores[1:]):
        assert a != b, "two tabulated compounds tie, so no single ordering exists"
    return square


# ------------------------------------------------------------ table questions

def q3(t, item):
    labs = cg.labels(t)
    cats = dict(zip(labs, [str(r[1]) for r in t["rows"]]))
    ans = dict(zip(labs, [str(r[2]) for r in t["rows"]]))
    assert [h for h in t["headers"]][1:] == [NCAT, NAN], f"unexpected headers {t['headers']}"
    good = [l for l in labs
            if cats[l] == "anions only" and ans[l] == "cations only"]
    assert len(good) == 1, (
        f"{len(good)} tabulated models surround every cation with anions and every anion "
        f"with cations: {good}; the item needs exactly one"
    )
    hn.keyed(item, good[0])
    return (f"of the {len(labs)} tabulated models only {good[0]} puts anions around every "
            "cation and cations around every anion, which is what alternation requires")


def q4(t, item):
    order = ranking(ion_rows(t))
    hn.keyed(item, order[0])
    return (f"{order[0]} has the largest charge product over separation, and it leads under "
            "an inverse-distance law as well as an inverse-square one")


def q6(t, item):
    rows = ion_rows(t)
    prods = {q for _, q, _ in rows}
    assert len(prods) == 1, f"the tabulated charge products are not all equal: {prods}"
    strongest = min(rows, key=lambda r: r[2])
    hn.keyed(item, strongest[0])
    return (f"every charge product equals {prods.pop():g}, so the smallest separation, "
            f"{strongest[2]:g} picometers in {strongest[0]}, gives the strongest interaction")


def q8(t, item):
    rows = ion_rows(t)
    seps = {r for _, _, r in rows}
    assert len(seps) == 1, f"the tabulated separations are not all equal: {seps}"
    strongest = max(rows, key=lambda r: r[1])
    prods = sorted(q for _, q, _ in rows)
    assert prods[-1] > prods[-2], "two compounds tie for the largest charge product"
    hn.keyed(item, strongest[0])
    return (f"every separation equals {seps.pop():g} picometers, so the largest charge "
            f"product, {strongest[1]:g} in {strongest[0]}, gives the strongest interaction")


def q10(t, item):
    rows = radius_rows(t)
    order = ranking(rows)
    closest = min(rows, key=lambda r: r[2])
    assert order[0] == closest[0], "the strongest interaction is not the smallest sum of radii"
    hn.keyed(item, closest[0])
    return (f"summing the two tabulated radii gives {closest[0]} the smallest interionic "
            f"distance at {closest[2]:g} picometers and so the strongest interaction")


def q12(t, item):
    order = ranking(ion_rows(t))
    widest = max(ion_rows(t), key=lambda r: r[2])[0]
    assert order[-1] != widest, (
        "the weakest interaction belongs to the compound with the largest separation, so "
        "the distractor reasoning from separation alone would reach the keyed answer"
    )
    hn.keyed(item, order[-1])
    return (f"{order[-1]} is last in the combined ranking, while ranking on separation "
            f"alone would wrongly point at {widest}")


def q14(t, item):
    rows = ion_rows(t)
    prods = {q for _, q, _ in rows}
    assert len(prods) == 1, f"the tabulated charge products are not all equal: {prods}"
    weakest = max(rows, key=lambda r: r[2])
    hn.keyed(item, weakest[0])
    return (f"with every charge product equal, the largest separation, {weakest[2]:g} "
            f"picometers in {weakest[0]}, gives the weakest interaction")


def q16(t, item):
    rows = ion_rows(t)
    seps = {r for _, _, r in rows}
    assert len(seps) == 1, f"the tabulated separations are not all equal: {seps}"
    weakest = min(rows, key=lambda r: r[1])
    hn.keyed(item, weakest[0])
    return (f"with every separation equal, the smallest charge product, {weakest[1]:g} in "
            f"{weakest[0]}, gives the weakest interaction")


def q18(t, item):
    rows = radius_rows(t)
    order = ranking(rows)
    widest = max(rows, key=lambda r: r[2])
    assert order[-1] == widest[0], "the weakest interaction is not the largest sum of radii"
    hn.keyed(item, widest[0])
    return (f"summing the two tabulated radii gives {widest[0]} the largest interionic "
            f"distance at {widest[2]:g} picometers and so the weakest interaction")


def q20(t, item):
    order = ranking(ion_rows(t))
    hn.keyed(item, order[1])
    return (f"the combined ranking runs {', '.join(order)}, so {order[1]} is second and the "
            "order does not depend on the power of the distance")


def q22(t, item):
    rc = cg.col(t, RCAT)
    ra = cg.col(t, RAN)
    assert len(set(rc)) == 1, f"the tabulated cation radius is not constant: {rc}"
    assert len(set(ra)) == len(ra), f"the tabulated anion radii are not all different: {ra}"
    sums = [c + a for c, a in zip(rc, ra)]
    assert len(set(sums)) == len(sums), "two solids share an interionic distance"
    hn.keyed(item, "radius of the anion")
    return (f"the cation radius is {rc[0]:g} picometers in every row while the anion radius "
            f"runs from {min(ra):g} to {max(ra):g}, so only the anion moves the sum")


def q24(t, item):
    rows = ion_rows(t)
    controlled = [(a[0], b[0]) for i, a in enumerate(rows) for b in rows[i + 1:]
                  if a[1] == b[1] and a[2] != b[2]]
    assert len(controlled) == 1, (
        f"{len(controlled)} tabulated comparisons hold the charges fixed while the "
        f"separation varies: {controlled}; the item needs exactly one"
    )
    first, second = controlled[0]
    hn.keyed(item, f"{first} against {second}")
    return (f"exactly one tabulated pair, {first} against {second}, shares its charge "
            "product while differing in separation, which is what isolating distance means")


def q26(t, item):
    rows = ion_rows(t)
    seps = {r for _, _, r in rows}
    assert len(seps) == 1, f"the tabulated separations are not all equal: {seps}"
    ref = [q for lab, q, _ in rows if lab == "Compound Q"]
    assert len(ref) == 1, "the reference compound named in the stem is not tabulated once"
    twice = [lab for lab, q, _ in rows if lab != "Compound Q" and q == 2 * ref[0]]
    assert len(twice) == 1, (
        f"{len(twice)} tabulated compounds carry twice the reference charge product: "
        f"{twice}; the item needs exactly one"
    )
    hn.keyed(item, twice[0])
    return (f"at a fixed separation the ratio is the ratio of charge products, and only "
            f"{twice[0]} carries {2 * ref[0]:g} against the reference {ref[0]:g}")


def q28(t, item):
    rows = ion_rows(t)
    prods = {q for _, q, _ in rows}
    assert len(prods) == 1, f"the tabulated charge products are not all equal: {prods}"
    by_sep = sorted(rows, key=lambda r: r[2])
    for a, b in zip(by_sep, by_sep[1:]):
        assert a[1] / a[2] ** 2 > b[1] / b[2] ** 2, (
            f"the strength does not fall from {a[0]} to {b[0]}, so it is not monotonic"
        )
    hn.keyed(item, "weakens steadily")
    return (f"with the charges equal the strength falls at every one of the "
            f"{len(by_sep) - 1} steps of increasing separation, so the fall is steady")


TABLE_CHECKS = {3: q3, 4: q4, 6: q6, 8: q8, 10: q10, 12: q12, 14: q14, 16: q16,
                18: q18, 20: q20, 22: q22, 24: q24, 26: q26, 28: q28}


# -------------------------------------------------------- stem-numeric question

_CHARGE_PAIR = re.compile(r"([+-]\d+)\s+and\s+([+-]\d+)(?![0-9])")


def a30(item):
    """Read both charge pairs out of the stem, then apply EK 2.2.A.3.i."""
    pairs = _CHARGE_PAIR.findall(item["q"])
    assert len(pairs) == 2, f"the stem states {len(pairs)} charge pairs, expected two: {pairs}"
    products = [abs(int(a) * int(b)) for a, b in pairs]
    ratio = products[1] / products[0]
    assert ratio == 4, (
        f"the charge products in the stem give a ratio of {ratio:g}, not the factor of four "
        "the keyed choice states"
    )
    hn.keyed(item, "About four times")
    return (f"the stem's own charges give products of {products[0]} and {products[1]}, a "
            f"ratio of {ratio:g}, with the separation stipulated to be nearly equal")


ARITH = {30: a30}


# ------------------------------------------------------- module-specific gates

# The topic's exclusion statement. These may appear in a REJECTED option -- item
# 23 exists to mark them out of scope -- and nowhere else.
_EXCLUDED = re.compile(
    r"(?<![a-z])(?:unit cell|coordination number|packing (?:fraction|efficiency)|"
    r"face-centered|body-centered|simple cubic|rock salt|Madelung|lattice energy|"
    r"named lattice|named crystal structure)"
    r"(?![a-z])", re.I)

# EK 3.2.A.3's macroscopic properties of ionic solids belong to topic 3.2.
_MACRO = re.compile(
    r"(?<![a-z])(?:melting point|boiling point|vapor pressure|brittle|brittleness|"
    r"malleable|ductile|conducts? electricity|electrical conductivity)(?![a-z])", re.I)


def excluded_material_only_as_a_distractor(module):
    code = module.TOPIC[0]
    in_distractors = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        guarded = [("stem", item["q"]),
                   ("keyed choice", item["choices"][item["ans"]])]
        for where, text in guarded:
            hit = _EXCLUDED.search(text)
            assert not hit, (
                f"{code} q{i}: the {where} invokes {hit.group(0)!r}, which the topic's "
                f"exclusion statement puts outside the exam -- {text[:70]!r}"
            )
        for j, ch in enumerate(item["choices"]):
            if j != item["ans"] and _EXCLUDED.search(ch):
                in_distractors += 1
    print(f"OK  {code} exclusion: no stem or keyed choice invokes a specific crystal "
          f"structure; {in_distractors} rejected option(s) name one, which is how the "
          "exclusion statement is taught.")


def no_macroscopic_property(module):
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _MACRO.search(text)
            assert not hit, (
                f"{code} q{i}: rests on {hit.group(0)!r}, which is EK 3.2.A.3 and belongs "
                f"to topic 3.2 -- {text[:70]!r}"
            )
    print(f"OK  {code} scope: no item rests on a macroscopic property of an ionic solid, "
          "which is EK 3.2.A.3's material.")


CLAIMS = [
 ("systematic, periodic three-dimensional array",
  "EK 2.3.A.1, verbatim in substance: the cations and anions in an ionic crystal are arranged in a systematic, periodic 3-D array. Each rejected option drops one of those three words."),
 ("maximizes the attractive forces among cations and anions while minimizing",
  "EK 2.3.A.1, verbatim: the array maximizes the attractive forces among cations and anions while minimizing the repulsive forces. The framework does not balance the two against each other."),
 ("Model 1",
  "EK 2.3.A.1 requires the arrangement to maximize attraction among cations and anions while minimizing repulsion. Recomputed in q3, which finds exactly one tabulated model surrounding every cation with anions and every anion with cations."),
 ("Compound X",
  "EK 2.2.A.3 makes both the charges and the separation matter, and LO 2.3.A requires the ionic model to be consistent with Coulomb's law. Recomputed in q4, under both an inverse-square and an inverse-distance law."),
 ("Coulomb's law and the properties of the constituent ions",
  "LO 2.3.A states the requirement in those words: a particulate model consistent with Coulomb's law and the properties of the constituent ions. Dropping the second half is what one rejected option does."),
 ("Compound J",
  "EK 2.2.A.3.ii makes the strength rise as the separation falls. Recomputed in q6, which first asserts every tabulated charge product is equal so that separation is the only variable."),
 ("surrounding each cation with oppositely charged ions",
  "EK 2.3.A.1 has the array maximize attraction among cations and anions while minimizing repulsion, and putting anions around a cation is what achieves both. The delocalized-electron option is EK 2.4.A.1's metallic model."),
 ("Compound T",
  "EK 2.2.A.3.i makes the strength proportional to the charge on each ion. Recomputed in q8, which first asserts every tabulated separation is equal so that charge is the only variable."),
 ("raises exactly the repulsive forces the array is described as minimizing",
  "EK 2.3.A.1 says the array minimizes the repulsive forces, and repulsion in an ionic solid is between ions of like charge, so making like charges nearest neighbors works directly against the described arrangement."),
 ("Sample 1",
  "The distance between neighboring ion centers is the sum of the two radii, and EK 2.2.A.3.ii makes the smallest such distance the strongest interaction. Recomputed in q10 from the tabulated radii."),
 ("periodic throughout the solid",
  "EK 2.3.A.1 calls the array systematic and PERIODIC, and a periodic arrangement repeats, so the same local arrangement recurs from place to place inside one crystal."),
 ("Compound W",
  "EK 2.2.A.3 requires both columns to be combined. Recomputed in q12, which also asserts that the compound with the largest separation is NOT the weakest, so the rejected distance-only reasoning cannot reach the key."),
 ("second solid are stronger, because strength is proportional to the charge on each ion",
  "EK 2.2.A.3.i, near verbatim: because the interaction strength is proportional to the charge on each ion, larger charges lead to stronger interactions. Size is stipulated equal."),
 ("Compound M",
  "EK 2.2.A.3.ii makes the largest separation the weakest interaction once the charges are held equal. Recomputed in q14."),
 ("One continuous array",
  "EK 2.3.A.1 describes a systematic, periodic three-dimensional ARRAY maximizing attraction among cations and anions, which is one extended arrangement; isolating each pair would give up most of those attractions."),
 ("Compound Q",
  "EK 2.2.A.3.i makes the smallest charge product the weakest interaction once the separations are held equal. Recomputed in q16."),
 ("smaller ions bring the ion centers closer together",
  "EK 2.2.A.3.ii, near verbatim: because the interaction strength increases as the distance between the centers of the ions decreases, smaller ions lead to stronger interactions."),
 ("Sample 4",
  "The interionic distance is the sum of the two tabulated radii, and EK 2.2.A.3.ii makes the largest such distance the weakest interaction. Recomputed in q18."),
 ("properties of the constituent ions, which include their charges and their relative sizes",
  "LO 2.3.A requires a particulate model consistent with Coulomb's law and with the properties of the constituent ions, and a drawing carrying neither charge nor relative size carries none of them."),
 ("Compound Z",
  "EK 2.2.A.3 makes a full ranking require both columns. Recomputed in q20, which produces the same order under an inverse-square and an inverse-distance law."),
 ("leaves out the oppositely charged neighbors above and below",
  "EK 2.3.A.1 specifies a THREE-DIMENSIONAL array, so a single sheet supplies neighbors in only two directions and omits attractions the framework says the arrangement maximizes."),
 ("radius of the anion",
  "The interionic distance is the sum of the two radii. Recomputed in q22, which asserts the tabulated cation radius is constant across all four rows while the anion radius varies."),
 ("surrounds each ion with oppositely charged neighbors is favored",
  "EK 2.3.A.1 states that the array maximizes attraction among cations and anions while minimizing repulsion, which answers why alternation is favored. The topic's exclusion statement puts the four rejected tasks, all about a named crystal structure, outside the exam."),
 ("Compound W against Compound Y",
  "Isolating a variable means holding the other fixed. Recomputed in q24, which asserts exactly one tabulated pair shares its charge product while differing in separation, and EK 2.2.A.3 is what makes both quantities relevant."),
 ("a larger charge and a smaller separation both",
  "EK 2.2.A.3.i and EK 2.2.A.3.ii each supply half the answer, and here the two point the same way, so no weighing of one against the other is required."),
 ("Compound R",
  "EK 2.2.A.3.i makes the strength proportional to the charge on each ion, so at a fixed separation the ratio of two interactions is the ratio of their charge products. Recomputed in q26, which asserts exactly one tabulated compound doubles the reference."),
 ("Oppositely charged ions drawn as near neighbors",
  "EK 2.2.A.3 makes attraction between unlike charges and repulsion between like charges both grow as the separation falls, so a drawing answers to Coulomb's law by placing unlike charges close and like charges apart, which is the arrangement EK 2.3.A.1 describes."),
 ("weakens steadily",
  "EK 2.2.A.3.ii makes the strength fall as the separation rises, with the charges held equal. Recomputed in q28 step by step, so a claim true only between the extremes would fail."),
 ("separate molecule",
  "EK 2.3.A.1 describes a systematic, periodic three-dimensional array and LO 2.3.A adds consistency with Coulomb's law, which support every rejected statement here. Nothing in the framework describes a separate molecular unit inside the array."),
 ("About four times",
  "EK 2.2.A.3.i makes the strength proportional to the charge on each ion, so doubling both charges multiplies their product by four while the separation, stipulated nearly equal, contributes nothing. Recomputed in a30 from the stem's own charges."),
]


# ------------------------------------------------------------ negative controls

def _retable(mod, i, label, **cells):
    """Replace named cells of one row of question ``i``'s table, by column header."""
    t = mod.QUESTIONS[i - 1]["table"]
    heads = list(t["headers"])
    rows = []
    for row in t["rows"]:
        row = list(row)
        if str(row[0]) == label:
            for header, value in cells.items():
                row[heads.index(header)] = value
        rows.append(row)
    mod.QUESTIONS[i - 1]["table"] = dict(headers=heads, rows=rows)


def _model_4_alternates(mod, cl):
    """Give a second tabulated model the keyed pattern, so the item has two answers."""
    _retable(mod, 3, "Model 4", **{NAN: "cations only"})


def _spread_the_strongest(mod, cl):
    """Push the doubly charged compound out until it is no longer strongest."""
    _retable(mod, 4, "Compound X", **{SEP: "700"})


def _charges_stop_matching(mod, cl):
    """Break the equal-charge premise the separation-only item depends on."""
    _retable(mod, 6, "Compound K", **{QCAT: "+2"})


def _separations_stop_matching(mod, cl):
    """Break the equal-separation premise the charge-only item depends on."""
    _retable(mod, 8, "Compound T", **{SEP: "400"})


def _cation_radius_varies(mod, cl):
    """Break the constant-cation premise the isolate-the-anion item depends on."""
    _retable(mod, 22, "Sample 2", **{RCAT: "150"})


def _second_controlled_pair(mod, cl):
    """Give a second pair the same charge product, so distance is no longer isolated.

    The charge product is what has to move, and it has to move onto a value another
    row already carries: setting Compound X to a single charge makes three rows share
    a product where one pair shared it before, which is exactly the ambiguity the
    isolate-the-variable item cannot survive. Changing a charge to some OTHER new
    value leaves the count at one and proves nothing -- the first draft of this
    control did that and passed silently.
    """
    _retable(mod, 24, "Compound X", **{QCAT: "+1", QAN: "-1"})


def _nothing_doubles_the_reference(mod, cl):
    """Remove the compound whose charge product is exactly twice the reference."""
    _retable(mod, 26, "Compound R", **{QCAT: "+3"})


def _stem_charges_shrink(mod, cl):
    """Halve the second charge pair in the stem, so the keyed factor no longer follows."""
    before = mod.QUESTIONS[29]["q"]
    after = before.replace("carrying +2 and -2", "carrying +2 and -1")
    assert after != before, "the control's replacement did not match the stem"
    mod.QUESTIONS[29]["q"] = after


def _excluded_material_in_a_key(mod, cl):
    ch = list(mod.QUESTIONS[0]["choices"])
    ch[0] = "As the face-centered arrangement adopted by every ionic compound"
    mod.QUESTIONS[0]["choices"] = ch
    cl[0] = ("face-centered arrangement", cl[0][1])
    excluded_material_only_as_a_distractor(mod)


def _macroscopic_property_creeps_in(mod, cl):
    mod.QUESTIONS[1]["q"] = ("Which macroscopic property follows: does the array give the "
                             "solid a high melting point?")
    no_macroscopic_property(mod)


if __name__ == "__main__" and "--selftest" in sys.argv:
    hn.selftest(M, CLAIMS, TABLE_CHECKS, arith=ARITH, extra=[
        ("a second tabulated model made to alternate, so the item has two answers",
         _model_4_alternates),
        ("the strongest compound's separation corrupted until the table no longer\n          supports its key", _spread_the_strongest),
        ("the equal-charge premise of the separation-only item broken",
         _charges_stop_matching),
        ("the equal-separation premise of the charge-only item broken",
         _separations_stop_matching),
        ("the constant cation radius broken under the isolate-the-anion item",
         _cation_radius_varies),
        ("a second pair given the same charge product, so distance is not isolated",
         _second_controlled_pair),
        ("the compound that doubles the reference charge product removed",
         _nothing_doubles_the_reference),
        ("the stem's own charges changed so the keyed factor of four is false",
         _stem_charges_shrink),
        ("excluded crystal-structure material moved into a keyed choice",
         _excluded_material_in_a_key),
        ("a macroscopic property of ionic solids, which is topic 3.2's",
         _macroscopic_property_creeps_in),
    ])

excluded_material_only_as_a_distractor(M)
no_macroscopic_property(M)
hn.audit(M, CLAIMS, TABLE_CHECKS, arith=ARITH)
