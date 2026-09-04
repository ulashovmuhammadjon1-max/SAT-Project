"""Key audit for AP CHEMISTRY 2.2 Intramolecular Force and Potential Energy.

One ``(anchor, claim)`` per item, in module order; the anchor must appear in the
KEYED choice and in no distractor. All nineteen table items and the one
stem-numeric item are recomputed from their own stimulus.

WHAT THE KEYS REST ON
---------------------
EK 2.2.A.1  A graph of potential energy versus internuclear distance is a useful
            representation for describing the interactions between atoms; such
            graphs illustrate both the equilibrium bond length (the separation
            at which the potential energy is lowest) and the bond energy (the
            energy required to separate the atoms).
            (items 1, 2, 3, 4, 5, 6, 14, 15, 16, 17, 22, 24, 26, 30)
EK 2.2.A.2  In a covalent bond, the bond length is influenced by both the size
            of the atom's core and the bond order; bonds with a higher order are
            shorter and have larger bond energies.
            (items 7, 8, 9, 18, 19, 20, 25, 28)
EK 2.2.A.3  Coulomb's law can be used to understand the strength of interactions
            between cations and anions; (i) strength is proportional to the
            charge on each ion, (ii) strength increases as the distance between
            the ion centers decreases.
            (items 10, 11, 12, 13, 21, 23, 27, 29)

Item 23 chains outward and says so: EK 2.2.A.3.ii gives only the DIRECTION of
the distance effect, so the size of the effect comes from EK 1.5.A.2, which
prints Coulomb's law with the separation squared in the denominator
(``EQN: F_coulombic proportional to q1q2/r^2``, CED line 1868). Both codes are
cited in that item's rationale, because keying "more than a factor of two" to
2.2.A.3 alone would be keying a magnitude to a sentence that states none.

WHY THIS MODULE HAD NO GATE, AND WHAT THE GATE FOUND. 2.2 was left with 30
questions and no verifier when its author stopped. Writing the gate found five
real defects, all now fixed in ``h2_2.py``: four items where one choice was
wholly contained in another (a student accepting the shorter option had no
ground to reject the longer, so the item had two defensible answers), and two
stems that opened identically. It also found one key that rested on an
attraction/repulsion balance the 2.2 essential knowledge never states -- that
item's key was rewritten onto EK 2.2.A.1's own definition.

THE FIGURE PROBLEM, WHICH THIS TOPIC OWNS MORE THAN ANY OTHER. EK 2.2.A.1 is a
statement about a GRAPH and this bank cannot show one. Every potential energy
curve here is therefore a table of internuclear distance against potential
energy. ``no_figure_language`` asserts that no stem or choice points at a
picture, and ``table_words_carry_a_table`` asserts the converse defect cannot
ship either -- a stem that says "the table" while carrying none.

SCOPE. ``coulomb_stays_between_ions`` keeps EK 1.5.A.2's and 1.5.A.4's
electron-and-nucleus application of Coulomb's law inside unit 1: EK 2.2.A.3 is
about CATIONS AND ANIONS, and h1_5.py owns the other case.

NEGATIVE CONTROL: ``python3 verify_h2_2.py --selftest``.
"""
import re
import sys

import h_chem_notation as hn
import h2_2 as M

DIST = "Internuclear distance (picometers)"
PE = "Potential energy (kilojoules per mole)"
ORDER = "Bond order"
BLEN = "Bond length (picometers)"
BEN = "Bond energy (kilojoules per mole)"
QCAT = "Charge on the cation"
QAN = "Charge on the anion"
SEP = "Distance between the ion centers (picometers)"
MDIST = "Distance at the lowest potential energy (picometers)"
MPE = "Lowest potential energy reached (kilojoules per mole)"

cg = hn.cg


# ----------------------------------------------------------------- helpers

def curve(table):
    """(distance, potential energy) pairs, in increasing distance order."""
    pairs = sorted(zip(cg.col(table, DIST), cg.col(table, PE)))
    assert len(pairs) >= 4, "a curve needs enough points to read a minimum from"
    ds = [d for d, _ in pairs]
    assert len(set(ds)) == len(ds), f"a distance is tabulated twice: {ds}"
    return pairs


def minimum(table):
    """The tabulated (distance, energy) at the lowest potential energy."""
    pairs = curve(table)
    d, e = min(pairs, key=lambda p: p[1])
    lows = [p for p in pairs if p[1] == e]
    assert len(lows) == 1, f"the lowest energy {e} is tabulated at {len(lows)} distances"
    return d, e


def far_value(table):
    """The energy at the largest tabulated separation: the separated-atom reference."""
    pairs = curve(table)
    return pairs[-1][1]


def strength(q_cat, q_an, r, power=2):
    """Coulombic interaction strength, EK 1.5.A.2's form. Magnitude only."""
    return abs(q_cat * q_an) / r ** power


def ion_rows(table):
    """(label, cation charge, anion charge, separation) for every tabulated pair."""
    return list(zip(cg.labels(table), cg.col(table, QCAT), cg.col(table, QAN),
                    cg.col(table, SEP)))


def ranked_pairs(table, power=2):
    """Ion-pair labels ordered strongest first under Coulomb's law."""
    scored = [(lab, strength(qc, qa, r, power)) for lab, qc, qa, r in ion_rows(table)]
    return [lab for lab, _ in sorted(scored, key=lambda p: p[1], reverse=True)]


def orders(table):
    """(bond label, bond order) rows, ordered by increasing bond order."""
    return sorted(zip(cg.labels(table), cg.col(table, ORDER)), key=lambda p: p[1])


# ------------------------------------------------------------ table questions

def q2(t, item):
    d, e = minimum(t)
    hn.keyed(item, f"{d:g} picometers")
    return (f"the lowest tabulated potential energy, {e:g}, sits at {d:g} picometers, "
            "which EK 2.2.A.1 calls the equilibrium bond length")


def q3(t, item):
    d, e = minimum(t)
    far = far_value(t)
    depth = far - e
    hn.keyed(item, f"{depth:g} kilojoules per mole")
    return (f"the minimum lies {depth:g} kilojoules per mole below the separated-atom "
            f"value of {far:g}, which is the energy required to separate the atoms")


def q4(t, item):
    d_eq, e_eq = minimum(t)
    inner = [(d, e) for d, e in curve(t) if d < d_eq]
    assert len(inner) >= 2, "the curve must tabulate at least two points inside the minimum"
    for (d1, e1), (d2, e2) in zip(inner, inner[1:]):
        assert e1 > e2, (
            f"the energy at {d1:g} pm is not above the energy at {d2:g} pm, so the curve "
            "does not rise as the atoms are pushed together"
        )
    assert inner[0][1] > 0, (
        f"the innermost tabulated energy is {inner[0][1]:g}, so the curve never turns positive"
    )
    hn.keyed(item, "rises steeply")
    return (f"reading inward from the minimum at {d_eq:g} pm the tabulated energy rises at "
            f"every step and reaches {inner[0][1]:g}, which is positive")


def q5(t, item):
    d_eq, e_eq = minimum(t)
    outer = [(d, e) for d, e in curve(t) if d > d_eq]
    assert len(outer) >= 2, "the curve must tabulate at least two points outside the minimum"
    for (d1, e1), (d2, e2) in zip(outer, outer[1:]):
        assert e1 < e2, (
            f"the energy at {d1:g} pm is not below the energy at {d2:g} pm, so the curve "
            "does not rise as the atoms are pulled apart"
        )
    assert outer[-1][1] == 0, f"the largest separation is tabulated at {outer[-1][1]:g}, not zero"
    hn.keyed(item, "rises toward zero")
    return (f"outward from the minimum at {d_eq:g} pm the tabulated energy rises at every "
            "step and reaches exactly zero at the largest separation")


def q8(t, item):
    rows = sorted(zip(cg.col(t, ORDER), cg.col(t, BLEN), cg.col(t, BEN)))
    for (o1, l1, e1), (o2, l2, e2) in zip(rows, rows[1:]):
        assert l1 > l2, f"bond order {o1:g} is not longer than order {o2:g}: {l1:g} against {l2:g}"
        assert e1 < e2, f"bond order {o1:g} is not weaker than order {o2:g}: {e1:g} against {e2:g}"
    hn.keyed(item, "shorter and its energy gets larger")
    return (f"across the {len(rows)} tabulated rows the length falls and the energy rises at "
            "every step of increasing bond order")


def q9(t, item):
    ords = cg.col(t, ORDER)
    assert len(set(ords)) == 1, f"the tabulated bond orders are not all equal: {ords}"
    lens = cg.col(t, BLEN)
    assert len(set(lens)) == len(lens), f"the tabulated lengths are not all different: {lens}"
    hn.keyed(item, "size of the partner atom's core")
    return (f"every tabulated bond order is {ords[0]:g} while all {len(lens)} lengths differ, "
            "so bond order cannot be what varies")


def q12(t, item):
    by_square = ranked_pairs(t, power=2)
    by_inverse = ranked_pairs(t, power=1)
    assert by_square[0] == by_inverse[0], (
        f"the strongest pair depends on the power used: {by_square[0]} against {by_inverse[0]}"
    )
    scores = sorted(strength(qc, qa, r) for _, qc, qa, r in ion_rows(t))
    assert scores[-1] > scores[-2], "two pairs tie for strongest"
    hn.keyed(item, by_square[0])
    return (f"{by_square[0]} has the largest charge product over separation squared, and it "
            "leads under an inverse-distance law too, so the ranking does not turn on the power")


def q13(t, item):
    rows = ion_rows(t)
    prods = {abs(qc * qa) for _, qc, qa, _ in rows}
    assert len(prods) == 1, f"the charge products are not all equal: {prods}"
    weakest = min(rows, key=lambda r: strength(r[1], r[2], r[3]))
    seps = sorted(r[3] for r in rows)
    assert seps[-1] > seps[-2], "two pairs tie for the largest separation"
    hn.keyed(item, weakest[0])
    return (f"with every charge product equal to {prods.pop():g}, {weakest[0]} carries the "
            f"largest separation at {weakest[3]:g} picometers and so the weakest interaction")


def q14(t, item):
    labs = cg.labels(t)
    depths = dict(zip(labs, cg.col(t, MPE)))
    dists = dict(zip(labs, cg.col(t, MDIST)))
    deepest = min(labs, key=lambda l: depths[l])
    shortest = min(labs, key=lambda l: dists[l])
    assert deepest != shortest, (
        "the deepest minimum and the shortest bond belong to the same molecule, so the "
        "distractor reasoning from distance would reach the keyed answer as well"
    )
    hn.keyed(item, deepest)
    return (f"{deepest} reaches {depths[deepest]:g} kilojoules per mole, the deepest of the "
            f"{len(labs)} tabulated minima, while the shortest bond belongs to {shortest}")


def q15(t, item):
    labs = cg.labels(t)
    depths = dict(zip(labs, cg.col(t, MPE)))
    dists = dict(zip(labs, cg.col(t, MDIST)))
    shortest = min(labs, key=lambda l: dists[l])
    deepest = min(labs, key=lambda l: depths[l])
    assert deepest != shortest, (
        "the deepest minimum and the shortest bond belong to the same molecule, so depth "
        "would serve as a proxy and the item would have two defensible answers"
    )
    hn.keyed(item, shortest)
    return (f"{shortest} has the smallest tabulated distance at {dists[shortest]:g} picometers, "
            f"while the deepest minimum belongs to {deepest} instead")


def q17(t, item):
    d_b, e_b = minimum(t)
    first = M.QUESTIONS[1]["table"]
    d_a, e_a = minimum(first)
    assert d_b > d_a, f"the second minimum at {d_b:g} pm is not further out than {d_a:g} pm"
    assert e_b > e_a, f"the second minimum at {e_b:g} is not shallower than {e_a:g}"
    assert far_value(t) == far_value(first) == 0, "the two curves do not share a reference value"
    gap = (e_b - e_a) / abs(e_a)
    assert gap < 0.05, f"the depths differ by {gap:.1%}, which is not 'very slightly'"
    hn.keyed(item, "Longer and very slightly weaker")
    return (f"the second minimum sits at {d_b:g} pm against {d_a:g} pm and is {gap:.1%} "
            "shallower, both curves sharing the same zero at large separation")


def q19(t, item):
    rows = sorted(zip(cg.col(t, ORDER), cg.col(t, BEN)))
    lo, hi = rows[0][1], rows[-1][1]
    ratio = hi / lo
    assert 2.25 <= ratio <= 2.75, f"the energy ratio is {ratio:.2f}, not about two and a half"
    hn.keyed(item, "two and a half times")
    return (f"{hi:g} over {lo:g} is {ratio:.2f}, which rounds to about two and a half times")


def q20(t, item):
    rows = sorted(zip(cg.col(t, ORDER), cg.col(t, BLEN)))
    drop = rows[0][1] - rows[-1][1]
    assert drop > 0, f"the bond does not shorten: the length changes by {drop:g} picometers"
    hn.keyed(item, f"{drop:g} picometers")
    return (f"{rows[0][1]:g} minus {rows[-1][1]:g} is {drop:g} picometers, the shortening from "
            "the single bond to the triple bond")


def q21(t, item):
    rows = ion_rows(t)
    same = [(a, b) for i, a in enumerate(rows) for b in rows[i + 1:]
            if a[3] == b[3] and abs(a[1] * a[2]) != abs(b[1] * b[2])]
    assert same, "no two tabulated pairs share a separation while differing in charge"
    a, b = same[0]
    bigger = a if abs(a[1] * a[2]) > abs(b[1] * b[2]) else b
    assert strength(*bigger[1:]) > strength(*(a if bigger is b else b)[1:]), \
        "the larger charge product does not give the larger strength at equal separation"
    hn.keyed(item, "doubly charged ions, because interaction strength is proportional")
    return (f"{a[0]} and {b[0]} share a separation of {a[3]:g} picometers, so the larger "
            f"charge product of {bigger[0]} is the only thing that can raise its strength")


def q22(t, item):
    pairs = curve(t)
    far = pairs[-1][1]
    assert far == max(e for _, e in pairs[1:]), (
        "the largest separation does not hold the highest energy of the outer branch"
    )
    assert far == 0, f"the separated-atom value is {far:g} rather than zero"
    hn.keyed(item, "no longer interacting")
    return ("the largest tabulated separation holds exactly zero, the top of the outer branch "
            "and the state the atoms reach once separated")


def q24(t, item):
    d, e = minimum(t)
    far = far_value(t)
    assert far == 0, f"the separated-atom value is {far:g}, so reading the minimum would not work"
    assert abs(e) == far - e, (
        "the magnitude of the minimum does not equal its depth below the reference, so the "
        "coincidence the item turns on does not hold"
    )
    hn.keyed(item, "depth of the minimum below that value")
    return (f"the reference is zero here, so the magnitude {abs(e):g} happens to equal the "
            f"depth {far - e:g}, which is the coincidence the claim depends on")


def q25(t, item):
    ords = cg.col(t, ORDER)
    assert len(set(ords)) == 1, f"the tabulated bond orders are not all equal: {ords}"
    lens = cg.col(t, BLEN)
    assert lens == sorted(lens), (
        f"the tabulated lengths do not increase down the list of larger partner atoms: {lens}"
    )
    hn.keyed(item, "larger atomic core will be the longer")
    return (f"bond order is {ords[0]:g} throughout while the lengths rise from {lens[0]:g} to "
            f"{lens[-1]:g} picometers as the partner atom grows")


def q27(t, item):
    rows = ion_rows(t)
    isolating = [(a[0], b[0]) for i, a in enumerate(rows) for b in rows[i + 1:]
                 if a[3] == b[3] and abs(a[1] * a[2]) != abs(b[1] * b[2])]
    assert len(isolating) == 1, (
        f"{len(isolating)} tabulated comparisons hold separation fixed while charge varies: "
        f"{isolating}; the item needs exactly one"
    )
    first, second = isolating[0]
    hn.keyed(item, f"{first} against {second}")
    return (f"exactly one tabulated comparison, {first} against {second}, holds the separation "
            "fixed while the charges differ, which is what isolating charge requires")


def q28(t, item):
    rows = sorted(zip(cg.col(t, ORDER), cg.col(t, BLEN), cg.col(t, BEN)))
    steps = list(zip(rows, rows[1:]))
    assert len(steps) >= 2, "a stepwise claim needs at least two steps"
    for (o1, l1, e1), (o2, l2, e2) in steps:
        assert l2 < l1, f"the length does not fall from order {o1:g} to {o2:g}"
        assert e2 > e1, f"the energy does not rise from order {o1:g} to {o2:g}"
    hn.keyed(item, "decreases at each step, and the bond energy rises")
    return (f"the length falls and the energy rises at each of the {len(steps)} tabulated "
            "steps, so neither claim holds only overall")


TABLE_CHECKS = {2: q2, 3: q3, 4: q4, 5: q5, 8: q8, 9: q9, 12: q12, 13: q13,
                14: q14, 15: q15, 17: q17, 19: q19, 20: q20, 21: q21, 22: q22,
                24: q24, 25: q25, 27: q27, 28: q28}


# -------------------------------------------------------- stem-numeric question

_PM = re.compile(r"(?<![0-9])(\d+)\s+picometers(?![a-z])")


def a23(item):
    """Read the two separations out of the stem itself, then apply EK 1.5.A.2."""
    seps = [int(x) for x in _PM.findall(item["q"])]
    assert len(seps) == 2, f"the stem states {len(seps)} separations, expected two: {seps}"
    near, far = min(seps), max(seps)
    factor = (far / near) ** 2
    linear = far / near
    assert factor > 2, (
        f"the inverse-square factor is {factor:g}, which is not more than two, so the keyed "
        "claim does not follow from the stem's own numbers"
    )
    assert abs(linear - 2) < 1e-9, (
        f"an inverse-distance law would give {linear:g}, not the factor of two the rejected "
        "option states, so that distractor no longer means what the item needs it to"
    )
    hn.keyed(item, "more than a factor of two")
    return (f"EK 1.5.A.2 squares the separation, so {far}/{near} gives {factor:g}, more than "
            f"the factor of {linear:g} an inverse-distance law would give")


ARITH = {23: a23}


# ------------------------------------------------------- module-specific gates

# Only picture words. "graph" alone is legitimate here: EK 2.2.A.1 IS a statement
# about a graph, and several stems ask what such a graph would display or how it
# would be built without ever claiming one is on the page.
_FIGURE = re.compile(
    r"(?<![a-z])(?:diagram|figure|image|picture|sketch|photograph|"
    r"shown above|shown below|graph above|graph below|curve above|curve below|"
    r"the graph shows|graph displayed|pictured)(?![a-z])", re.I)

_TABLE_WORD = re.compile(r"(?<![a-z])(?:table|tabulated)(?![a-z])", re.I)

_COULOMB = re.compile(r"(?<![A-Za-z])[Cc]oulomb", re.I)
_UNIT_ONE = re.compile(
    r"(?<![a-z])(?:electrons?|subshells?|ionization|effective nuclear charge)(?![a-z])", re.I)


def no_figure_language(module):
    """No stem or choice may point at a picture the bank cannot show."""
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{code} q{i}: refers to {hit.group(0)!r}, but every potential energy curve "
                f"here is a table -- {text[:70]!r}"
            )
    print(f"OK  {code} figures: no stem or choice points at a picture; every curve is a "
          "table of distance against potential energy.")


def table_words_carry_a_table(module):
    """The converse defect: a stem that says 'the table' while carrying none."""
    code = module.TOPIC[0]
    n = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        if _TABLE_WORD.search(item["q"]):
            n += 1
            assert item.get("table"), (
                f"{code} q{i}: the stem sends the student to a table the item does not "
                f"carry -- {item['q'][:70]!r}"
            )
    print(f"OK  {code} stimulus: all {n} stem(s) naming a table carry one.")


def coulomb_stays_between_ions(module):
    """EK 2.2.A.3 is about cations and anions; the electron case is 1.5's."""
    code = module.TOPIC[0]
    n = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            if not _COULOMB.search(text):
                continue
            n += 1
            hit = _UNIT_ONE.search(text)
            assert not hit, (
                f"{code} q{i}: applies Coulomb's law to {hit.group(0)!r}, which is EK "
                f"1.5.A.2 and 1.5.A.4's territory rather than 2.2.A.3's -- {text[:70]!r}"
            )
    print(f"OK  {code} scope: all {n} Coulombic string(s) stay between cations and anions, "
          "leaving the electron-and-nucleus case to unit 1.")


CLAIMS = [
 ("equilibrium bond length and the bond energy",
  "EK 2.2.A.1, near verbatim: such graphs illustrate both the equilibrium bond length, the separation at which the potential energy is lowest, and the bond energy, the energy required to separate the atoms."),
 ("74 picometers",
  "EK 2.2.A.1 defines the equilibrium bond length as the separation at which the potential energy is lowest. Recomputed in q2 from the table's own minimum."),
 ("436 kilojoules",
  "EK 2.2.A.1 defines the bond energy as the energy required to separate the atoms, which is the depth of the minimum below the separated-atom value. Recomputed in q3."),
 ("rises steeply",
  "EK 2.2.A.1 makes the equilibrium bond length the separation at which the potential energy is LOWEST, so the energy must be higher on both sides of it. Recomputed in q4, which also checks the innermost tabulated value is positive."),
 ("rises toward zero",
  "EK 2.2.A.1 makes the bond energy the energy required to separate the atoms, so the curve must climb from its minimum to the separated-atom value. Recomputed in q5 from the outer branch."),
 ("internuclear distance in picometers on the horizontal axis and potential energy",
  "Suggested skill 3.A asks for appropriate graphing with correct scale and units, and EK 2.2.A.1 names the two quantities as potential energy and the distance between atoms. The anchor spans both axes because a rejected option keeps the same vertical axis with a different horizontal one."),
 ("shorter and have larger bond energies",
  "EK 2.2.A.2, verbatim: bonds with a higher order are shorter and have larger bond energies. Each rejected option swaps one half of that sentence or both."),
 ("shorter and its energy gets larger",
  "EK 2.2.A.2 states the relationship and q8 recomputes it from the table, checking that the length falls and the energy rises at every step of increasing bond order."),
 ("size of the partner atom's core",
  "EK 2.2.A.2 names exactly two influences on the length of a covalent bond, the size of the atom's core and the bond order. Recomputed in q9, which asserts every tabulated bond order is identical while the lengths differ."),
 ("It becomes stronger",
  "EK 2.2.A.3.i: because the interaction strength is proportional to the charge on each ion, larger charges lead to stronger interactions. The proportionality is stated of EACH ion, so raising one charge suffices."),
 ("smaller distance between ion centers means a stronger interaction",
  "EK 2.2.A.3.ii: because the interaction strength increases as the distance between the centers of the ions decreases, smaller ions lead to stronger interactions. The charges are stipulated equal, leaving distance the only variable."),
 ("Pair 2",
  "EK 2.2.A.3 makes both the charges and the separation matter. Recomputed in q12, which also confirms the winner does not depend on whether the separation enters squared or linearly."),
 ("Pair D",
  "EK 2.2.A.3.ii makes the strength fall as the separation grows. Recomputed in q13, which first asserts every tabulated charge product is equal so that separation is the only variable."),
 ("Molecule M",
  "EK 2.2.A.1 makes the bond energy the energy required to separate the atoms, which is the depth of the minimum. Recomputed in q14, which also asserts the shortest bond belongs to a different molecule so depth and distance cannot both point one way."),
 ("Molecule J",
  "EK 2.2.A.1 defines the equilibrium bond length as the separation at which the potential energy is lowest, so the shortest bond is the smallest such separation. Recomputed in q15."),
 ("defined as the separation at which the potential energy is lowest",
  "EK 2.2.A.1 gives the equilibrium bond length exactly this definition, so the statement is what the term means. The framework never asserts the atoms stop moving there, nor that the nuclei touch, nor that the zero of the scale sits there."),
 ("Longer and very slightly weaker",
  "EK 2.2.A.1 makes the position of the minimum the bond length and its depth the bond energy. Recomputed in q17 against the first curve, including a check that the depth difference is under five percent."),
 ("shorter and requires more energy to break",
  "EK 2.2.A.2: bonds with a higher order are shorter and have larger bond energies, and the bond energy is EK 2.2.A.1's energy required to separate the atoms. Holding the two elements fixed leaves bond order as the variable."),
 ("two and a half times",
  "EK 2.2.A.2 fixes the direction of the change; the size of it is read off the table. Recomputed in q19 as the ratio of the tabulated triple-bond and single-bond energies."),
 ("34 picometers",
  "EK 2.2.A.2 states that higher-order bonds are shorter, and the amount is the difference between the two tabulated lengths. Recomputed in q20."),
 ("doubly charged ions, because interaction strength is proportional",
  "EK 2.2.A.3.i states the proportionality to the charge on each ion, and EK 2.2.A.3 makes Coulomb's law the right tool for a cation-anion interaction. Recomputed in q21, which finds the two tabulated pairs sharing a separation."),
 ("no longer interacting",
  "EK 2.2.A.1 makes the bond energy the energy required to SEPARATE the atoms, so the value approached at large separation is the state that separation reaches. Recomputed in q22."),
 ("more than a factor of two",
  "EK 2.2.A.3.ii gives the direction and EK 1.5.A.2 gives the magnitude, printing Coulomb's law with the separation squared in the denominator. Recomputed in a23, which reads both separations out of the stem and confirms an inverse-distance law would give the factor the rejected option states."),
 ("depth of the minimum below that value",
  "EK 2.2.A.1 defines the bond energy as the energy required to separate the atoms, which is a DIFFERENCE between the minimum and the separated-atom value. Recomputed in q24, which asserts the two coincide here only because the reference is zero."),
 ("larger atomic core will be the longer",
  "EK 2.2.A.2 names the size of the atom's core alongside bond order as an influence on bond length. Recomputed in q25, which asserts the tabulated order is constant while the lengths rise with the partner atom."),
 ("separation the atoms settle at and the energy needed to pull them apart",
  "EK 2.2.A.1 calls such a graph a useful representation because it illustrates both the equilibrium bond length and the bond energy, which is exactly the pair of readings named."),
 ("Pair 1 against Pair 2",
  "Isolating a variable means holding the other fixed. Recomputed in q27, which asserts exactly one tabulated comparison holds the separation fixed while the charges differ, and EK 2.2.A.3 is what makes both quantities relevant."),
 ("decreases at each step, and the bond energy rises",
  "EK 2.2.A.2 states that higher-order bonds are shorter with larger bond energies. Recomputed in q28 step by step, so a claim that held only between the extremes would fail."),
 ("requires weighing the larger charges against the smaller separation",
  "EK 2.2.A.3 makes the strength depend on the charge on each ion and on the distance between the ion centers, and it ranks neither factor above the other, so a comparison in which they point opposite ways is not settled by either sub-point alone."),
 ("No stable bond forms",
  "EK 2.2.A.1 makes the bond energy the energy required to separate the atoms and the equilibrium bond length the separation at which the potential energy is lowest, so a curve never falling below the separated-atom value offers neither a separation to settle at nor an energy recovered by separating."),
]


# ------------------------------------------------------------ negative controls

def _flatten_minimum(mod, cl):
    """Move the tabulated minimum so the keyed equilibrium bond length is false."""
    t = mod.QUESTIONS[1]["table"]
    mod.QUESTIONS[1]["table"] = dict(
        headers=t["headers"],
        rows=[[d, ("-500" if d == "120" else e)] for d, e in t["rows"]])


def _shallower_reference(mod, cl):
    """Break the separated-atom reference so the keyed bond energy no longer follows."""
    t = mod.QUESTIONS[2]["table"]
    mod.QUESTIONS[2]["table"] = dict(
        headers=t["headers"],
        rows=[[d, ("-50" if d == "400" else e)] for d, e in t["rows"]])


def _invert_bond_energy(mod, cl):
    """Make the triple bond the WEAKEST, contradicting EK 2.2.A.2's own sentence."""
    t = mod.QUESTIONS[7]["table"]
    mod.QUESTIONS[7]["table"] = dict(
        headers=t["headers"],
        rows=[[b, o, l, ("200" if o == "3" else e)] for b, o, l, e in t["rows"]])


def _spread_the_ion_pair(mod, cl):
    """Push the doubly charged pair far enough out that it is no longer strongest."""
    t = mod.QUESTIONS[11]["table"]
    mod.QUESTIONS[11]["table"] = dict(
        headers=t["headers"],
        rows=[[p, qc, qa, ("600" if p == "Pair 2" else r)] for p, qc, qa, r in t["rows"]])


def _deepest_also_shortest(mod, cl):
    """Give the deepest minimum the shortest bond too, so the item has two answers.

    The control has to move the DISTANCE, not the depth: shortening Molecule M's
    bond is what collapses the two readings onto one molecule. Lowering some
    other molecule's depth would leave the keyed answer intact and prove nothing.
    """
    t = mod.QUESTIONS[13]["table"]
    mod.QUESTIONS[13]["table"] = dict(
        headers=t["headers"],
        rows=[[m, ("50" if m == "Molecule M" else d), e] for m, d, e in t["rows"]])


def _shrink_the_stem_gap(mod, cl):
    """Halve the stated far separation, so the recomputed factor is no longer above two."""
    mod.QUESTIONS[22]["q"] = mod.QUESTIONS[22]["q"].replace(
        "the second 400 picometers apart", "the second 240 picometers apart")


def _equal_separations_vanish(mod, cl):
    """Remove the one controlled comparison the isolate-charge item depends on."""
    t = mod.QUESTIONS[26]["table"]
    mod.QUESTIONS[26]["table"] = dict(
        headers=t["headers"],
        rows=[[p, qc, qa, ("290" if p == "Pair 1" else r)] for p, qc, qa, r in t["rows"]])


def _figure_language(mod, cl):
    mod.QUESTIONS[0]["q"] = "In the diagram above, which two quantities are displayed?"
    no_figure_language(mod)


def _table_word_without_a_table(mod, cl):
    mod.QUESTIONS[0]["q"] = ("Using the tabulated potential energies, which two quantities "
                             "does such a representation display?")
    table_words_carry_a_table(mod)


def _coulomb_leaves_the_topic(mod, cl):
    mod.QUESTIONS[9]["q"] = ("Coulomb's law is applied to an electron in a subshell and the "
                             "nucleus of its own atom. What happens to the attraction if the "
                             "nuclear charge is doubled?")
    coulomb_stays_between_ions(mod)


if __name__ == "__main__" and "--selftest" in sys.argv:
    hn.selftest(M, CLAIMS, TABLE_CHECKS, arith=ARITH, extra=[
        ("the tabulated minimum moved off the keyed bond length", _flatten_minimum),
        ("the separated-atom reference corrupted under the keyed bond energy",
         _shallower_reference),
        ("the triple bond made the weakest, against EK 2.2.A.2", _invert_bond_energy),
        ("the doubly charged pair pushed out until it is no longer strongest",
         _spread_the_ion_pair),
        ("the deepest minimum given the shortest bond too, so the item has two answers",
         _deepest_also_shortest),
        ("the stem's far separation shrunk until the keyed factor is false",
         _shrink_the_stem_gap),
        ("the one controlled charge comparison broken", _equal_separations_vanish),
        ("a stem pointing at a diagram the bank cannot show", _figure_language),
        ("a stem naming a table the item does not carry", _table_word_without_a_table),
        ("Coulomb's law applied to an electron and a nucleus, which is unit 1's",
         _coulomb_leaves_the_topic),
    ])

no_figure_language(M)
table_words_carry_a_table(M)
coulomb_stays_between_ions(M)
hn.audit(M, CLAIMS, TABLE_CHECKS, arith=ARITH)
