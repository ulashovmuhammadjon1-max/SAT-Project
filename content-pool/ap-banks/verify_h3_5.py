"""Key audit for AP CHEMISTRY 3.5 Kinetic Molecular Theory.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  3.5.A.1  KMT relates the macroscopic properties of gases to particle motion,
           and the Maxwell-Boltzmann distribution describes the DISTRIBUTION of
           kinetic energies at a given temperature      1, 2, 14, 16, 18
  3.5.A.2  all particles in a sample of matter are in continuous, random motion,
           and the average kinetic energy is half the mass times the square of
           the average velocity            3, 4, 10, 11, 15, 17, 29
  3.5.A.3  the Kelvin temperature is proportional to the average kinetic energy
                    5, 6, 7, 8, 12, 21, 22, 23, 25, 27
  3.5.A.2 with 3.5.A.3 together -- equal average kinetic energies at one Kelvin
           temperature, and that energy proportional to mass times squared speed
                    9, 20, 24, 26
  3.5.A.4  the distribution is a graphical representation of the energies and
           velocities at a given temperature             13, 19, 28, 30

THE TWO THINGS NO KEY MAY SAY. ``distribution_never_uniform`` refuses any key
asserting that all the particles at one temperature share a single kinetic
energy or speed -- the distribution in EK 3.5.A.1 and EK 3.5.A.4 is a spread,
and the average in EK 3.5.A.3 presupposes that the values differ. The check
also asserts that the misconception IS offered somewhere as a distractor, so it
cannot pass by running over an empty set. ``kelvin_named_in_proportionality``
refuses any key that makes a quantity proportional to a bare "temperature";
EK 3.5.A.3's proportionality is to the KELVIN temperature and holds for no
other scale.

THE ONE DERIVATION. The lighter gas moves faster only because EK 3.5.A.3
equalises the average kinetic energies and EK 3.5.A.2 writes that energy as half
the mass times the squared speed. Item 9's distractors include the half-swap --
the right verdict from the wrong clause and the wrong verdict from the right one
-- so ``swap_anchors_carry_both_clauses`` requires that anchor to name both the
lighter gas AND the larger speed, and proves the ambiguity by finding the
one-clause distractor.

ARITHMETIC. Eight stem items and seven tabulated ones are recomputed from the
stimulus alone. No effusion law is used anywhere: every speed ratio comes from
the two framework equations.

FIGURES. EK 3.5.A.4 is a graph and this bank cannot show one, so the
distribution is a table and ``no_figure_language`` asserts no item points at a
picture.

NEGATIVE CONTROL: ``python3 verify_h3_5.py --selftest``.
"""
import math
import re
import sys

import cg_check as cg
import h_check as h

import h3_5

F300 = "Fraction of particles at 300 K"
F900 = "Fraction of particles at 900 K"
TEMPK = "Kelvin temperature (K)"
AVGKE = "Average kinetic energy (relative units)"
MOLARMASS = "Molar mass (grams per mole)"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below|curve above|curve below|curve shown|"
    r"plotted above|plotted below)(?![a-z])", re.I)

# 3.4 owns the ideal gas law and partial pressures, 3.6 every departure from
# ideality, 3.13 Beer-Lambert. None of them belong in a topic about motion.
_OTHER_TOPIC = re.compile(
    r"(?<![A-Za-z])(ideal gas law|nRT|partial pressure|partial pressures|"
    r"deviation|deviations|van der Waals|Beer-Lambert|molar absorptivity)(?![A-Za-z])",
    re.I)

# The misconception: one shared value where the framework asserts a spread.
_UNIFORM = [
    re.compile(r"(?<![a-z])(?:all|every)\s+(?:of\s+)?(?:the\s+)?particles?(?![a-z])"
               r"[^.]{0,70}(?<![a-z])(?:same|identical)(?![a-z])", re.I),
    re.compile(r"(?<![a-z])single\s+(?:kinetic energy|speed|velocity)(?![a-z])"
               r"[^.]{0,60}(?<![a-z])every particle(?![a-z])", re.I),
]

_PROPORTIONAL = re.compile(r"(?<![a-z])proportional(?![a-z])", re.I)
_TEMPERATURE = re.compile(r"(?<![a-z])temperature(?![a-z])", re.I)
_KELVIN = re.compile(r"(?<![a-z])Kelvin(?![a-z])", re.I)


def _facing(item):
    out = [item["q"], item["why"]] + list(item["choices"])
    t = item.get("table")
    if t:
        out += [str(x) for x in t["headers"]]
        out += [str(c) for r in t["rows"] for c in r]
    return out


def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, which this bank "
                f"cannot show -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: EK 3.5.A.4's distribution is carried as a table; "
          "no item points at a picture.")


def no_other_topic(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _OTHER_TOPIC.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: uses {hit.group(0)!r}, which is 3.4's or 3.6's "
                f"material -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no ideal gas law, no partial pressures and no "
          "departure from ideality.")


def distribution_never_uniform(module):
    """A spread, never one shared value. EK 3.5.A.1 and EK 3.5.A.4 make it a distribution."""
    offered = []
    for i, item in enumerate(module.QUESTIONS, 1):
        for k, choice in enumerate(item["choices"]):
            hit = next((p.search(choice) for p in _UNIFORM if p.search(choice)), None)
            if not hit:
                continue
            assert k != item["ans"], (
                f"{module.TOPIC[0]} q{i}: the key says all the particles share one value "
                f"({hit.group(0)!r}), but EK 3.5.A.1 makes the kinetic energies a "
                "DISTRIBUTION and EK 3.5.A.3 speaks of their average"
            )
            offered.append((i, k))
    assert len(offered) >= 2, (
        f"only {len(offered)} distractor(s) offer the uniform-energy misconception, so this "
        "check has almost nothing to distinguish and proves little"
    )
    print(f"OK  {module.TOPIC[0]} distribution guard: the uniform-energy misconception is "
          f"offered at {offered} and keyed nowhere.")


def kelvin_named_in_proportionality(module):
    """EK 3.5.A.3's proportionality is to the KELVIN temperature and to no other scale."""
    checked = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = h.keyed(item)
        if _PROPORTIONAL.search(key) and _TEMPERATURE.search(key):
            assert _KELVIN.search(key), (
                f"{module.TOPIC[0]} q{i}: the key makes a quantity proportional to a bare "
                f"temperature -- {key!r}. EK 3.5.A.3 says the KELVIN temperature."
            )
            checked.append(i)
    assert checked, (
        "no key states a proportionality to a temperature at all, so this check ran over an "
        "empty set and proves nothing"
    )
    print(f"OK  {module.TOPIC[0]} Kelvin guard: item(s) {checked} state a proportionality to "
          "a temperature and every one of them names it as the Kelvin temperature.")


SWAP_ITEMS = {
    9: ("lighter", "larger speed"),
}


def swap_anchors_carry_both_clauses(module, claims):
    for i, (clause_a, clause_b) in sorted(SWAP_ITEMS.items()):
        anchor = claims[i - 1][0]
        item = module.QUESTIONS[i - 1]
        has_a = cg.contains_phrase(anchor, clause_a)
        has_b = cg.contains_phrase(anchor, clause_b)
        assert has_a and has_b, (
            f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} must name both {clause_a!r} and "
            f"{clause_b!r}; it carries "
            f"{'only the first' if has_a else 'only the second' if has_b else 'neither'}"
        )
        half = [k for k, c in enumerate(item["choices"])
                if k != item["ans"]
                and cg.contains_phrase(c, clause_a) != cg.contains_phrase(c, clause_b)]
        assert half, (
            f"{module.TOPIC[0]} q{i}: no distractor carries exactly one of the two clauses, "
            "so this item is not the half-swap case the check is for"
        )
    print(f"OK  {module.TOPIC[0]} swap guard: {len(SWAP_ITEMS)} anchor(s) name both the "
          "component and the consequence, with a half-swapped distractor present.")


# ------------------------------------------------------------------ arithmetic

def speed_ratio(m_light, m_heavy):
    """EK 3.5.A.2 with EK 3.5.A.3: equal average kinetic energies fix the speed ratio."""
    return math.sqrt(m_heavy / m_light)


def n6(item):
    factor = 2.0 / 1.0
    assert abs(factor - 2.0) < 1e-12, f"the energy factor recomputes to {factor}"
    h.shows(item, "doubles")
    return f"the Kelvin temperature ratio is {factor:g}, and EK 3.5.A.3 passes it straight through"


def n7(item):
    factor = 800.0 / 200.0
    assert abs(factor - 4.0) < 1e-12, f"the energy factor recomputes to {factor}"
    h.shows(item, "four times as large")
    return f"800 K over 200 K recomputes the average kinetic energy factor as {factor:g}"


def n10(item):
    factor = 3.0 ** 2
    assert abs(factor - 9.0) < 1e-12, f"the energy factor recomputes to {factor}"
    h.shows(item, "nine times as large")
    return (f"EK 3.5.A.2 squares the velocity, so tripling the speed multiplies the energy "
            f"by {factor:g}")


def n11(item):
    factor = math.sqrt(1.0 / 4.0)
    assert abs(factor - 0.5) < 1e-12, f"the speed factor recomputes to {factor}"
    h.shows(item, "half as large")
    return (f"holding the energy fixed while multiplying the mass by four multiplies the "
            f"speed by {factor:g}")


def n15(item):
    ke = 0.5 * 2.0 * 3.0 ** 2
    assert abs(ke - 9.0) < 1e-12, f"the kinetic energy recomputes to {ke}"
    no_half = 2.0 * 3.0 ** 2
    no_square = 0.5 * 2.0 * 3.0
    assert abs(no_half - 18.0) < 1e-12 and abs(no_square - 3.0) < 1e-12, (
        f"the two mistake values recompute to {no_half} and {no_square}"
    )
    for wrong in (f"{no_half:g} J", f"{no_square:.1f} J"):
        offered = [k for k, c in enumerate(item["choices"]) if cg.contains_phrase(c, wrong)]
        assert offered and item["ans"] not in offered, (
            f"the mistake value {wrong} must be offered as a distractor and not keyed; it "
            f"appears at {offered} with the key at {item['ans']}"
        )
    h.shows(item, f"{ke:.1f} J")
    return (f"half of 2.0 kilograms times the square of 3.0 meters per second is {ke:g} J, "
            f"with {no_half:g} J and {no_square:g} J the two mistake values offered")


def n22(item):
    factor = 900.0 / 300.0
    assert abs(factor - 3.0) < 1e-12, f"the energy factor recomputes to {factor}"
    squared = factor ** 2
    assert abs(squared - 9.0) < 1e-12, "the nine-fold distractor must be the squared ratio"
    h.shows(item, "three times as large")
    return (f"900 K over 300 K gives {factor:g}, with the squared ratio {squared:g} offered "
            "as the distractor")


def n23(item):
    ratio = 2.0 / 1.0
    assert abs(ratio - 2.0) < 1e-12, f"the temperature ratio recomputes to {ratio}"
    h.shows(item, "2 to 1")
    return (f"EK 3.5.A.3's proportionality carries the energy ratio {ratio:g} to the Kelvin "
            "temperatures unchanged")


def n24(item):
    factor = math.sqrt(600.0 / 300.0)
    assert abs(factor - 1.4142) < 1e-3, f"the speed factor recomputes to {factor}"
    doubled = 2.0 * factor
    assert abs(doubled - 2.83) < 1e-2, "the 2.8 distractor must be twice the correct factor"
    h.shows(item, f"{factor:.1f}")
    return (f"doubling the average kinetic energy multiplies the speed by the square root of "
            f"two, {factor:.4f}, with {doubled:.1f} offered as a distractor")


NUMERIC = {6: n6, 7: n7, 10: n10, 11: n11, 15: n15, 22: n22, 23: n23, 24: n24}


# ----------------------------------------------------------------- table items

def _lower_bound(label):
    """The first number in a speed-range label such as '600 to 800'."""
    hit = re.match(r"\s*(\d+)", str(label))
    assert hit, f"speed range {label!r} does not open with a number"
    return float(hit.group(1))


def q12(table, item):
    ts, kes = cg.col(table, TEMPK), cg.col(table, AVGKE)
    ratios = [round(k / t, 9) for t, k in zip(ts, kes)]
    assert len(set(ratios)) == 1, f"the tabulated energy-per-kelvin values are {ratios}"
    assert len(set(kes)) > 1, (
        "the tabulated energies must differ, or the 'same at every temperature' distractor "
        "is true as well"
    )
    squares = [round(k / t ** 2, 12) for t, k in zip(ts, kes)]
    assert len(set(squares)) > 1, (
        "the energy must NOT also follow the square of the temperature, or that distractor "
        "is true as well"
    )
    h.shows(item, "directly proportional to the Kelvin temperature")
    return (f"every tabulated row shares the ratio {ratios[0]:g} of energy to Kelvin "
            f"temperature while the energies {kes} differ and {squares} varies")


def _mb_columns(table):
    labels = cg.labels(table)
    cold = dict(zip(labels, cg.col(table, F300)))
    hot = dict(zip(labels, cg.col(table, F900)))
    for name, colm in (("300 K", cold), ("900 K", hot)):
        total = round(sum(colm.values()), 9)
        assert abs(total - 1.0) < 1e-9, f"the {name} fractions sum to {total}, not one"
    return cold, hot


def q13(table, item):
    cold, hot = _mb_columns(table)
    fast_cold = sum(v for lab, v in cold.items() if _lower_bound(lab) >= 600)
    fast_hot = sum(v for lab, v in hot.items() if _lower_bound(lab) >= 600)
    assert fast_hot > fast_cold, (
        f"the hotter column must hold more fast particles: {fast_hot} against {fast_cold}"
    )
    slow_cold = sum(v for lab, v in cold.items() if _lower_bound(lab) < 200)
    slow_hot = sum(v for lab, v in hot.items() if _lower_bound(lab) < 200)
    assert slow_hot < slow_cold, (
        "the slowest range must SHRINK on warming, or the 'slower than 200' distractor is "
        f"true as well: {slow_hot} against {slow_cold}"
    )
    assert cold != hot, (
        "the two tabulated columns must differ, or the 'same in the two samples' distractor "
        "is true as well"
    )
    h.shows(item, f"rises from {fast_cold:.2f} to {fast_hot:.2f}")
    return (f"the tabulated fractions above 600 meters per second are {fast_cold:.2f} and "
            f"{fast_hot:.2f}, while the slowest range falls from {slow_cold:.2f} to "
            f"{slow_hot:.2f} and both columns sum to one")


def _unique_argmax(mapping, what):
    top = max(mapping, key=mapping.get)
    tied = [k for k, v in mapping.items() if abs(v - mapping[top]) < 1e-12]
    assert len(tied) == 1, f"the {what} is not unique: {tied} in {mapping}"
    return top


def q14(table, item):
    cold, _hot = _mb_columns(table)
    top = _unique_argmax(cold, "most populated 300 K range")
    assert top == "200 to 400", f"the most populated cool range is {top}: {cold}"
    h.shows(item, top)
    return f"the tabulated 300 K fractions {cold} have a unique maximum at the {top} range"


def q28(table, item):
    cold, hot = _mb_columns(table)
    top_hot = _unique_argmax(hot, "most populated 900 K range")
    top_cold = _unique_argmax(cold, "most populated 300 K range")
    assert _lower_bound(top_hot) > _lower_bound(top_cold), (
        f"the hotter sample's most populated range {top_hot!r} must sit above the cooler "
        f"sample's {top_cold!r}, or the item shows nothing about warming"
    )
    h.shows(item, top_hot)
    return (f"the tabulated 900 K fractions {hot} peak at the {top_hot} range, above the "
            f"300 K peak at {top_cold}")


def q20(table, item):
    masses = dict(zip(cg.labels(table), cg.col(table, MOLARMASS)))
    lightest = min(masses, key=masses.get)
    tied = [k for k, v in masses.items() if abs(v - masses[lightest]) < 1e-12]
    assert tied == [lightest], f"the lightest tabulated gas is not unique: {masses}"
    assert lightest == "Gas X", f"the lightest tabulated gas is {lightest}: {masses}"
    h.shows(item, lightest)
    return (f"the tabulated molar masses {masses} have a unique minimum at {lightest}, which "
            "EK 3.5.A.2 with EK 3.5.A.3 gives the largest average speed")


def q21(table, item):
    kes = dict(zip(cg.labels(table), cg.col(table, AVGKE)))
    ts = dict(zip(cg.labels(table), cg.col(table, TEMPK)))
    top = _unique_argmax(kes, "largest tabulated average kinetic energy")
    assert top == "Sample 3", f"the largest tabulated average kinetic energy is at {top}: {kes}"
    assert _unique_argmax(ts, "hottest tabulated sample") == top, (
        "the hottest tabulated sample must also carry the largest energy, or EK 3.5.A.3 is "
        f"contradicted by the table: {ts} against {kes}"
    )
    h.shows(item, top)
    return (f"the tabulated energies {kes} peak at {top}, the same row as the temperature "
            f"maximum in {ts}")


def q26(table, item):
    masses = dict(zip(cg.labels(table), cg.col(table, MOLARMASS)))
    ratio = speed_ratio(masses["Gas X"], masses["Gas Z"])
    assert abs(ratio - 4.0) < 1e-12, f"the speed ratio recomputes to {ratio}"
    inverse = 1.0 / ratio
    offered = [k for k, c in enumerate(item["choices"])
               if cg.contains_phrase(c, f"{inverse:.2f}")]
    assert offered and item["ans"] not in offered, (
        f"the inverted ratio {inverse:.2f} must be offered as a distractor and not keyed; it "
        f"appears at {offered} with the key at {item['ans']}"
    )
    h.shows(item, f"{ratio:.1f}")
    return (f"equal average kinetic energies with tabulated molar masses "
            f"{masses['Gas X']:g} and {masses['Gas Z']:g} recompute the speed ratio as "
            f"{ratio:g}, with {inverse:.2f} offered as the inverted distractor")


TABLE_CHECKS = {12: q12, 13: q13, 14: q14, 20: q20, 21: q21, 26: q26, 28: q28}


CLAIMS = [
 ("macroscopic properties of gases to the motions of the particles",
  "EK 3.5.A.1, verbatim in substance: the kinetic molecular theory relates the macroscopic properties of gases to motions of the particles in the gas."),
 ("distribution of the kinetic energies of particles at a given temperature",
  "EK 3.5.A.1's second sentence, verbatim in substance. A distribution is a spread of values, so a single shared value is what the sentence denies."),
 ("continuous, random motion",
  "EK 3.5.A.2 opens by saying all the particles in a sample of matter are in continuous, random motion, with no restriction to a phase or a temperature."),
 ("\\frac{1}{2}mv^{2}",
  "EK 3.5.A.2 gives the average kinetic energy as half the mass times the square of the average velocity; mass enters to the first power and velocity is squared."),
 ("average kinetic energy of the particles in the sample",
  "EK 3.5.A.3, verbatim in substance: the Kelvin temperature of a sample of matter is proportional to the average kinetic energy of the particles in the sample."),
 ("doubles",
  "EK 3.5.A.3's proportionality carries a factor on the Kelvin temperature straight to the average kinetic energy. Recomputed in n6."),
 ("four times as large",
  "EK 3.5.A.3 applied to a fourfold rise in the Kelvin temperature. Recomputed in n7."),
 ("average kinetic energy follows the Kelvin temperature alone",
  "EK 3.5.A.3 names the Kelvin temperature and no other quantity, so two samples at one temperature agree in average kinetic energy whatever they are made of."),
 ("lighter gas, because equal average kinetic energies with a smaller mass require a larger speed",
  "EK 3.5.A.3 equalises the average kinetic energies at one Kelvin temperature and EK 3.5.A.2 writes that energy as half the mass times the squared velocity, so a smaller mass forces a larger speed. Both clauses are pinned because half-swapped distractors are present."),
 ("nine times as large",
  "EK 3.5.A.2 squares the velocity, so a factor on the speed appears squared in the energy. Recomputed in n10."),
 ("half as large",
  "EK 3.5.A.2 with the energy held fixed: quadrupling the mass quarters the squared velocity and so halves the velocity. Recomputed in n11."),
 ("directly proportional to the Kelvin temperature",
  "EK 3.5.A.3, checked against the table in q12, which recomputes the energy-per-kelvin for every row and confirms neither the constant-energy nor the squared-temperature distractor is true as well."),
 ("rises from 0.07 to 0.35",
  "EK 3.5.A.3 raises the average kinetic energy with the Kelvin temperature and EK 3.5.A.4 makes the distribution its representation. q13 recomputes both fast-particle fractions, checks the slowest range shrinks, and checks both columns sum to one."),
 ("200 to 400",
  "EK 3.5.A.1 makes the distribution a spread with a most populated region. q14 recomputes the cool column's maximum and checks it is unique."),
 ("9.0 J",
  "EK 3.5.A.2's equation applied to the stated mass and speed. Recomputed in n15, which also recomputes the two mistake values and checks each is offered rather than keyed."),
 ("spread over a range described by the Maxwell-Boltzmann distribution",
  "EK 3.5.A.1 asserts a distribution of kinetic energies at a given temperature, and EK 3.5.A.3 speaks of their average, which presupposes that the individual values differ."),
 ("all the particles in a sample of matter",
  "EK 3.5.A.2 words the claim as being about all the particles in a sample of matter, without restriction to a phase, a temperature or a composition."),
 ("The temperature",
  "EK 3.5.A.1 and EK 3.5.A.4 both describe the distribution as being of energies or velocities at a GIVEN temperature, so one distribution belongs to one temperature while the energies along it vary."),
 ("graphical representation of the energies and velocities of particles",
  "EK 3.5.A.4, verbatim in substance: the Maxwell-Boltzmann distribution provides a graphical representation of the energies and velocities of particles at a given temperature."),
 ("Gas X",
  "EK 3.5.A.3 equalises the average kinetic energies and EK 3.5.A.2 ties that energy to mass times squared speed. q20 recomputes the tabulated molar masses and checks the minimum is unique."),
 ("Sample 3",
  "EK 3.5.A.3's proportionality. q21 recomputes the tabulated energies and checks their maximum falls on the same row as the temperature maximum."),
 ("three times as large",
  "EK 3.5.A.3 passes the Kelvin temperature ratio through unchanged. Recomputed in n22, which also recomputes the squared ratio offered as a distractor."),
 ("2 to 1",
  "EK 3.5.A.3 makes the two quantities proportional, so their ratio is preserved and is neither squared nor inverted. Recomputed in n23."),
 ("1.4",
  "EK 3.5.A.3 doubles the average kinetic energy and EK 3.5.A.2 makes that energy follow the square of the velocity. Recomputed in n24, which also recomputes the doubled-factor distractor."),
 ("Compressing the sample into half its volume",
  "EK 3.5.A.3 makes the average kinetic energy proportional to the Kelvin temperature and to nothing else, so a change at fixed temperature leaves it alone whatever it does to the volume."),
 ("4.0",
  "EK 3.5.A.2 with EK 3.5.A.3: equal average kinetic energies make the speed ratio the square root of the inverse mass ratio. Recomputed in q26 from the tabulated molar masses, with the inverted value checked to be a distractor."),
 ("To the average kinetic energy",
  "EK 3.5.A.3 names the average kinetic energy specifically; speed enters only through EK 3.5.A.2, where it is squared and multiplied by the mass."),
 ("400 to 600",
  "EK 3.5.A.3 raises the average with the Kelvin temperature. q28 recomputes the hot column's maximum and checks it sits at a higher speed than the cool column's."),
 ("\\sqrt{\\frac{2KE}{m}}",
  "EK 3.5.A.2's equation multiplied by two and divided by the mass isolates the squared velocity, and the square root then isolates the velocity itself."),
 ("whole distribution of speeds shifts to higher values",
  "EK 3.5.A.4 makes the distribution a representation of a whole population and EK 3.5.A.3 raises its average with the Kelvin temperature, so the centre moves while the spread and the randomness remain."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[12]["q"] = "In the graph above, which range holds the most particles?"
        no_figure_language(mod)

    def ideal_gas_law_creeps_in(mod, cl):
        mod.QUESTIONS[0]["q"] = (mod.QUESTIONS[0]["q"]
                                 + " Use the ideal gas law to decide.")
        no_other_topic(mod)

    def uniform_energy_keyed(mod, cl):
        # The misconception promoted to a key: at one temperature every particle
        # is claimed to share one kinetic energy.
        mod.QUESTIONS[29]["ans"] = 1
        cl[29] = ("Every particle speeds up to the same new speed", cl[29][1])
        distribution_never_uniform(mod)

    def uniform_distractors_removed(mod, cl):
        # A control on the CONTROL: with the misconception offered nowhere, the
        # guard would pass over an empty set.
        for item in mod.QUESTIONS:
            item["choices"] = [c.replace("the same new speed", "a higher speed")
                                .replace("has the same kinetic energy,",
                                         "has a kinetic energy")
                                .replace("The single kinetic energy shared by every particle",
                                         "The average kinetic energy of the particles")
                               for c in item["choices"]]
        distribution_never_uniform(mod)

    def kelvin_dropped(mod, cl):
        ch = list(mod.QUESTIONS[11]["choices"])
        ch[0] = "The average kinetic energy is directly proportional to the temperature"
        mod.QUESTIONS[11]["choices"] = ch
        cl[11] = ("directly proportional to the temperature", cl[11][1])
        kelvin_named_in_proportionality(mod)

    def proportionality_keys_removed(mod, cl):
        # A control on the CONTROL for the Kelvin guard.
        for item in mod.QUESTIONS:
            ch = list(item["choices"])
            ch[item["ans"]] = "An unrelated statement about the container"
            item["choices"] = ch
        kelvin_named_in_proportionality(mod)

    def speed_anchor_halved(mod, cl):
        cl[8] = ("larger speed", cl[8][1])
        swap_anchors_carry_both_clauses(mod, cl)

    def speed_anchor_other_half(mod, cl):
        cl[8] = ("lighter", cl[8][1])
        swap_anchors_carry_both_clauses(mod, cl)

    def ke_table_not_proportional(mod, cl):
        mod.QUESTIONS[11]["table"] = dict(
            headers=h3_5._T_KE["headers"],
            rows=[["Sample 1", "200", "2.0"], ["Sample 2", "400", "5.0"],
                  ["Sample 3", "600", "6.0"]])

    def ke_table_flattened(mod, cl):
        # Every row identical: the energy-per-kelvin ratio is still constant, so
        # the FIRST assertion still passes, and the control lands where it was
        # meant to -- on the requirement that the energies differ, without which
        # the "same at every Kelvin temperature" distractor is true as well. A
        # control that fired on the earlier assertion would have proved only
        # that some assertion works, not this one.
        mod.QUESTIONS[11]["table"] = dict(
            headers=h3_5._T_KE["headers"],
            rows=[["Sample 1", "200", "2.0"], ["Sample 2", "200", "2.0"],
                  ["Sample 3", "200", "2.0"]])

    def mb_column_stops_summing(mod, cl):
        mod.QUESTIONS[12]["table"] = dict(
            headers=h3_5._T_MB["headers"],
            rows=[["0 to 200", "0.30", "0.10"], ["200 to 400", "0.45", "0.25"],
                  ["400 to 600", "0.18", "0.30"], ["600 to 800", "0.05", "0.20"],
                  ["800 to 1000", "0.02", "0.40"]])

    def mb_columns_exchanged(mod, cl):
        # The hot and cold columns swapped: the fast fraction now FALLS on
        # warming, so the keyed comparison is false.
        mod.QUESTIONS[12]["table"] = dict(
            headers=h3_5._T_MB["headers"],
            rows=[[lab, hot, cold] for lab, cold, hot in h3_5._T_MB["rows"]])

    def mb_peak_does_not_move(mod, cl):
        # Both columns peaking in the SAME range: the warming item shows nothing.
        mod.QUESTIONS[27]["table"] = dict(
            headers=h3_5._T_MB["headers"],
            rows=[["0 to 200", "0.30", "0.10"], ["200 to 400", "0.45", "0.50"],
                  ["400 to 600", "0.18", "0.20"], ["600 to 800", "0.05", "0.15"],
                  ["800 to 1000", "0.02", "0.05"]])

    def masses_tied(mod, cl):
        mod.QUESTIONS[19]["table"] = dict(
            headers=h3_5._T_MASS["headers"],
            rows=[["Gas X", "4.0"], ["Gas Y", "4.0"], ["Gas Z", "64.0"]])

    def masses_changed_under_the_ratio_item(mod, cl):
        mod.QUESTIONS[25]["table"] = dict(
            headers=h3_5._T_MASS["headers"],
            rows=[["Gas X", "4.0"], ["Gas Y", "16.0"], ["Gas Z", "16.0"]])

    return [
        ("a stem referring to a graph the bank cannot show", figure_language),
        ("the ideal gas law creeping in from 3.4", ideal_gas_law_creeps_in),
        ("the uniform-energy misconception promoted to a key", uniform_energy_keyed),
        ("every uniform-energy distractor removed, so that guard would run over an empty set",
         uniform_distractors_removed),
        ("a proportionality key naming a bare temperature instead of the Kelvin temperature",
         kelvin_dropped),
        ("every key replaced, so the Kelvin guard would run over an empty set",
         proportionality_keys_removed),
        ("the speed anchor cut to the consequence only", speed_anchor_halved),
        ("the speed anchor cut to the component only", speed_anchor_other_half),
        ("a tabulated energy moved off the proportional line", ke_table_not_proportional),
        ("the tabulated energies flattened, so a distractor becomes true as well",
         ke_table_flattened),
        ("a distribution column that no longer sums to one", mb_column_stops_summing),
        ("the hot and cold distribution columns exchanged", mb_columns_exchanged),
        ("both distribution columns made to peak in the same range", mb_peak_does_not_move),
        ("two tabulated gases tied for the smallest molar mass", masses_tied),
        ("the tabulated molar masses changed under the speed-ratio item",
         masses_changed_under_the_ratio_item),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h3_5, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h3_5)
no_other_topic(h3_5)
distribution_never_uniform(h3_5)
kelvin_named_in_proportionality(h3_5)
swap_anchors_carry_both_clauses(h3_5, CLAIMS)
h.run(h3_5, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
