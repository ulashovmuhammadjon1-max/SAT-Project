"""Key audit for AP CHEMISTRY 9.2 Absolute Entropy and Entropy Change.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  9.2.A.1  the entropy change for a process is the sum of the standard
           entropies of the products less the sum for the reactants, computed
           from the absolute entropies of the species
                   every item; the arithmetic ones are 2-5, 7, 10-17, 19-25,
                   27, 29, 30
  9.1.A.1  borrowed only where an item checks a COMPUTED sign against the
           qualitative rule                     9, 19, 23, 28, 30

HOW THE ARITHMETIC IS CHECKED. ``rxn`` is one function used by fifteen items.
It parses the equation out of the stem, looks each species up in the table by
its row label INCLUDING the phase, applies the coefficients, and requires the
recomputed value -- sign and all -- to be the keyed choice. The verifier is
never told the expected answer, so a wrong key cannot be waved through by a
matching constant.

THE SIGN IS CHECKED SEPARATELY FROM THE MAGNITUDE, through
``h9_check.shows_signed``, because cg_check's normalized matching strips a
leading plus and lets "198.1" match inside "-198.1". Every arithmetic item must
also OFFER the sign-flipped value as a distractor, or it does not really ask
the student which way the subtraction runs.

SCOPE. 9.3 owns enthalpy, free energy and thermodynamic favorability.
``no_free_energy`` asserts that none of them appears here.

NEGATIVE CONTROL: ``python3 verify_h9_2.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h9_check as h9

import h9_2

SCOL = "Standard molar entropy, J/(mol K)"
VCOL = "Standard entropy change, J/(mol K)"

# Explicit lookarounds, never \b.
_OUT_OF_SCOPE = re.compile(
    r"(?<![A-Za-z])(gibbs|free energy|enthalpy|favou?red|favou?rability|kJ)(?![A-Za-z])",
    re.I)

_REPORTED = re.compile(r"\\\(\s*([+-]\d+(?:\.\d+)?)\s*\\\)")


def no_free_energy(module):
    """9.3 owns enthalpy, free energy and favorability; this topic is one equation."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in h9.facing(item):
            hit = _OUT_OF_SCOPE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: mentions {hit.group(0)!r}, which is 9.3's "
                f"material -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no item reaches into enthalpy, free energy or "
          "thermodynamic favorability.")


# --------------------------------------------------------------- the arithmetic

def entropy_of(table):
    """One species' tabulated absolute entropy, looked up by row label."""
    return lambda species: cg.cell(table, species, SCOL)


def delta_s(table, equation):
    """EK 9.2.A.1, computed from the table and the equation and nothing else."""
    reactants, products = h9.species_terms(equation)
    value = entropy_of(table)
    return h9.summed(products, value) - h9.summed(reactants, value)


def _coefficient_dropped(terms, species, value):
    """The sum a student gets by forgetting one species' coefficient."""
    return sum((1 if sp == species else c) * value(sp) for c, sp in terms)


def rxn(table, item):
    """Recompute the keyed entropy change; the verifier is never told the answer."""
    got = delta_s(table, h9.equation_from(item["q"]))
    token = f"{got:+.1f}"
    h9.shows_signed(item, token)
    flipped = h9.opposite_sign_offered(item, token)
    return (f"summing the tabulated absolute entropies over the equation in the stem "
            f"gives {token} J/(mol K), against {flipped} offered as the sign-flipped "
            f"distractor")


def q6(table, item):
    """The two reactions the stem names in words, both recomputed from the table."""
    value = entropy_of(table)
    to_gas = delta_s(table, "2 H2(g) + O2(g) gives 2 H2O(g)")
    to_liquid = delta_s(table, "2 H2(g) + O2(g) gives 2 H2O(l)")
    assert to_gas > to_liquid, (
        f"forming the vapour gives {to_gas:+.1f} against {to_liquid:+.1f} for the liquid, "
        "so the stem's premise that it is the less negative is false"
    )
    assert value("H2O(g)") > value("H2O(l)"), (
        "the tabulated vapour entropy must exceed the liquid's, or the keyed explanation "
        "is false"
    )
    assert value("O2(g)") > value("H2(g)"), (
        "the tabulated oxygen entropy must exceed hydrogen's, or the distractor claiming "
        "the reverse would be true"
    )
    column = cg.col(table, SCOL)
    assert value("H2(g)") > min(column), (
        "hydrogen must not hold the smallest tabulated entropy, or that distractor would "
        "be true"
    )
    h.shows(item, "absolute entropy of gaseous water is larger than that of liquid water")
    return (f"the two reactions recompute to {to_gas:+.1f} and {to_liquid:+.1f} J/(mol K), "
            f"and the tabulated water entries differ by "
            f"{value('H2O(g)') - value('H2O(l)'):+.1f} in the direction the key names")


def q8(table, item):
    pairs = dict(zip(cg.labels(table), cg.col(table, SCOL)))
    biggest = max(pairs, key=pairs.get)
    assert biggest == "O2(g)", f"the largest tabulated entropy belongs to {biggest}: {pairs}"
    assert len([v for v in pairs.values() if abs(v - pairs[biggest]) < 1e-12]) == 1, (
        f"the largest tabulated entropy must be unique: {pairs}"
    )
    h.shows(item, "O2(g)")
    return f"the tabulated absolute entropies are {pairs}, whose unique maximum is {biggest}"


def q9(table, item):
    pairs = dict(zip(cg.labels(table), cg.col(table, SCOL)))
    smallest = min(pairs, key=pairs.get)
    assert smallest == "H2O(l)", (
        f"the smallest tabulated entropy belongs to {smallest}: {pairs}"
    )
    assert len([v for v in pairs.values() if abs(v - pairs[smallest]) < 1e-12]) == 1, (
        f"the smallest tabulated entropy must be unique: {pairs}"
    )
    liquids = [lab for lab in pairs if lab.endswith("(l)")]
    assert liquids == ["H2O(l)"], (
        f"the keyed explanation calls it the only liquid in the table, and the liquids "
        f"are {liquids}"
    )
    h.shows(item, "H2O(l), which agrees with a liquid holding its matter less dispersed")
    return (f"the tabulated absolute entropies are {pairs}, whose unique minimum is the "
            f"only liquid row, {smallest}")


def _reported(stem):
    hits = _REPORTED.findall(stem)
    assert len(hits) == 1, f"expected one reported value in the stem, found {hits}"
    return float(hits[0])


def _mistake_values(table, equation):
    """What each named mistake would produce, computed from the table alone."""
    reactants, products = h9.species_terms(equation)
    value = entropy_of(table)
    correct = h9.summed(products, value) - h9.summed(reactants, value)
    return dict(
        correct=correct,
        reactant_coefficient_dropped=(h9.summed(products, value)
                                      - _coefficient_dropped(reactants, "H2(g)", value)),
        product_coefficient_dropped=(_coefficient_dropped(products, "NH3(g)", value)
                                     - h9.summed(reactants, value)),
        subtracted_backwards=-correct,
        sums_added=h9.summed(products, value) + h9.summed(reactants, value),
    )


def _one_mistake_explains(table, item, name):
    """Exactly the named mistake reproduces the value the stem reports."""
    stated = _reported(item["q"])
    values = _mistake_values(table, h9.equation_from(item["q"]))
    # Asked FIRST, so that a stem reporting the right answer fails for the
    # reason it is actually wrong rather than tripping the next assertion and
    # leaving this one never exercised.
    assert abs(values["correct"] - stated) > 1e-9, (
        f"the value the stem reports, {stated:+.1f} J/(mol K), is the correct one, so no "
        f"mistake was made and the item has no answer"
    )
    assert abs(values[name] - stated) < 1e-9, (
        f"the named mistake gives {values[name]:+.1f}, not the {stated:+.1f} the stem "
        f"reports"
    )
    others = {k: v for k, v in values.items() if k != name}
    clashing = [k for k, v in others.items() if abs(v - stated) < 1e-9]
    assert not clashing, (
        f"the reported value is also produced by {clashing}, so the item has more than "
        f"one defensible answer"
    )
    return values, stated


def q16(table, item):
    values, stated = _one_mistake_explains(table, item, "reactant_coefficient_dropped")
    h.shows(item, "coefficient of three on hydrogen was not applied")
    return (f"leaving hydrogen's coefficient out reproduces the reported {stated:+.1f} "
            f"J/(mol K), where the correct value is {values['correct']:+.1f} and every "
            f"other named mistake gives something else")


def q17(table, item):
    values, stated = _one_mistake_explains(table, item, "subtracted_backwards")
    h.shows(item, "subtracted in the wrong order")
    return (f"exchanging the two sums reproduces the reported {stated:+.1f} J/(mol K), "
            f"the correct value being {values['correct']:+.1f}")


def _sign_agrees(table, item):
    """The computed sign and EK 9.1.A.1's gas-mole count, as two named facts.

    Named booleans rather than two tuples compared by position. A guard of this
    shape is exactly where this project once built one tuple ordered one way and
    another ordered the other and compared index against index.
    """
    equation = h9.equation_from(item["q"])
    computed = delta_s(table, equation)
    gas_change = h9.delta_n_gas(equation)
    calculation_says_increase = computed > 0
    gas_rule_says_increase = gas_change > 0
    assert calculation_says_increase == gas_rule_says_increase, (
        f"the tabulated entropies give {computed:+.1f} J/(mol K) while the moles of gas "
        f"change by {gas_change:+d}: the two routes disagree, so the item's premise fails"
    )
    return computed, gas_change, calculation_says_increase


def q19(table, item):
    computed, gas_change, increase = _sign_agrees(table, item)
    assert increase, f"the tabulated entropies give {computed:+.1f}, not an increase"
    h.shows(item, "positive and the reaction produces gas where there was none")
    return (f"the tabulated entropies give {computed:+.1f} J/(mol K) and the moles of gas "
            f"change by {gas_change:+d}, so both routes give an increase")


def q30(table, item):
    computed, gas_change, increase = _sign_agrees(table, item)
    assert not increase, f"the tabulated entropies give {computed:+.1f}, not a decrease"
    h.shows(item, "negative and a mole of gas is consumed with none produced")
    return (f"the tabulated entropies give {computed:+.1f} J/(mol K) and the moles of gas "
            f"change by {gas_change:+d}, so both routes give a decrease")


_TWO_EQUATIONS = re.compile(r",\s*(.+?), or (.+?)\?\s*$")


def q20(table, item):
    m = _TWO_EQUATIONS.search(item["q"])
    assert m, f"the stem does not offer two equations to compare: {item['q'][:70]!r}"
    first, second = delta_s(table, m.group(1)), delta_s(table, m.group(2))
    assert second > first, (
        f"the second equation gives {second:+.1f} against the first's {first:+.1f}, so it "
        "is not the larger increase the key claims"
    )
    assert second > 0, f"the keyed reaction must actually increase the entropy: {second:+.1f}"
    h.shows(item, "gives 2 CO(g)")
    return (f"the two equations in the stem recompute to {first:+.1f} and {second:+.1f} "
            f"J/(mol K), so the keyed one has the larger increase")


def q21(table, item):
    pairs = dict(zip(cg.labels(table), cg.col(table, VCOL)))
    biggest = max(pairs, key=pairs.get)
    assert biggest == "4", f"the largest tabulated increase is at {biggest}: {pairs}"
    assert len([v for v in pairs.values() if abs(v - pairs[biggest]) < 1e-12]) == 1, (
        f"the largest tabulated increase must be unique: {pairs}"
    )
    h.shows(item, "Process 4")
    return f"the tabulated entropy changes are {pairs}, whose unique maximum is at {biggest}"


def q22(table, item):
    pairs = dict(zip(cg.labels(table), cg.col(table, VCOL)))
    smallest = min(pairs, key=pairs.get)
    assert smallest == "1", f"the largest tabulated decrease is at {smallest}: {pairs}"
    assert len([v for v in pairs.values() if abs(v - pairs[smallest]) < 1e-12]) == 1, (
        f"the largest tabulated decrease must be unique: {pairs}"
    )
    h.shows(item, "Process 1")
    return f"the tabulated entropy changes are {pairs}, whose unique minimum is at {smallest}"


def q23(table, item):
    pairs = dict(zip(cg.labels(table), cg.col(table, VCOL)))
    rising = sorted(lab for lab, v in pairs.items() if v > 0)
    assert rising == ["2", "4"], f"the tabulated increases are at {rising}: {pairs}"
    h.shows(item, "Processes 2 and 4")
    return (f"the tabulated entropy changes are {pairs}, and exactly the rows {rising} "
            f"are positive")


def q28(table, item):
    value = entropy_of(table)
    assert value("H2O(g)") > value("H2O(l)"), "the keyed comparison must hold in the table"
    assert value("H2(g)") < value("O2(g)"), "the hydrogen-oxygen distractor must be false"
    assert value("NH3(g)") > value("H2O(l)"), "the ammonia distractor must be false"
    assert value("N2(g)") < value("O2(g)"), "the nitrogen-oxygen distractor must be false"
    h.shows(item, "Gaseous water has a larger absolute entropy than liquid water")
    return ("the tabulated entries make the keyed comparison true and each of the other "
            "four comparisons false")


TABLE_CHECKS = {2: rxn, 3: rxn, 4: rxn, 5: rxn, 6: q6, 7: rxn, 8: q8, 9: q9,
                10: rxn, 11: rxn, 12: rxn, 13: rxn, 14: rxn, 15: rxn,
                16: q16, 17: q17, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23,
                24: rxn, 25: rxn, 27: rxn, 28: q28, 29: rxn, 30: q30}

NUMERIC = {}


CLAIMS = [
 ("subtracting the sum of the reactant entropies from the sum of the product entropies",
  "EK 9.2.A.1's equation, verbatim in substance: the entropy change of a reaction is the sum of the standard entropies of the products less the sum for the reactants."),
 ("-198.1 J/(mol K), a decrease",
  "EK 9.2.A.1 applied to the tabulated absolute entropies with every coefficient carried. Recomputed in rxn from the equation in the stem and the table alone."),
 ("198.1 J/(mol K), an increase",
  "EK 9.2.A.1 with the products and reactants exchanged, which reverses the sign and leaves the magnitude. Recomputed in rxn."),
 ("-326.6 J/(mol K), a decrease",
  "EK 9.2.A.1 using the row for LIQUID water, the coefficients applied. Recomputed in rxn from the table and the equation in the stem."),
 ("-88.8 J/(mol K), a decrease",
  "EK 9.2.A.1 using the row for GASEOUS water instead, which is the only change from the reaction forming the liquid. Recomputed in rxn."),
 ("absolute entropy of gaseous water is larger than that of liquid water",
  "EK 9.2.A.1 makes the product sum the only difference between the two reactions. q6 recomputes both changes from the table and checks each rejected comparison is false in the table."),
 ("118.9 J/(mol K), an increase",
  "EK 9.2.A.1 applied to a physical process: the absolute entropy of the vapour less that of the liquid. Recomputed in rxn."),
 ("O2(g)",
  "Reading the largest absolute entropy out of the table, which is the first step of every calculation under EK 9.2.A.1. q8 recomputes the maximum and checks it is unique."),
 ("H2O(l), which agrees with a liquid holding its matter less dispersed",
  "The smallest tabulated value belongs to the only liquid row, and EK 9.1.A.1 makes matter in a liquid less dispersed than as a gas. q9 recomputes the minimum and checks the row is the only liquid."),
 ("3.1 J/(mol K), an increase",
  "EK 9.2.A.1 with the small but non-zero entropy of the solid included in the reactant sum. Recomputed in rxn."),
 ("-172.8 J/(mol K), a decrease",
  "EK 9.2.A.1 with the coefficient of two applied to both the monoxide and the dioxide. Recomputed in rxn."),
 ("-4.9 J/(mol K), a decrease",
  "EK 9.2.A.1 with coefficients of two on the oxygen and the water vapour; three moles of gas become three, so the change is small. Recomputed in rxn."),
 ("175.9 J/(mol K), an increase",
  "EK 9.2.A.1 with the monoxide doubled and the solid's entropy included. Recomputed in rxn from the table and the stem."),
 ("160.7 J/(mol K), an increase",
  "EK 9.2.A.1 with both products summed before the single reactant is subtracted. Recomputed in rxn."),
 ("-181.5 J/(mol K), a decrease",
  "EK 9.2.A.1 with both the sodium and the sodium chloride doubled. Recomputed in rxn from the table and the equation."),
 ("coefficient of three on hydrogen was not applied",
  "EK 9.2.A.1's sums are coefficient-weighted. q16 recomputes what each named mistake would give and checks that exactly one reproduces the value the stem reports."),
 ("subtracted in the wrong order",
  "EK 9.2.A.1 fixes the order as products less reactants, so exchanging the sums returns the same magnitude with the opposite sign. q17 recomputes every candidate mistake."),
 ("absolute entropy, that is, its standard molar entropy",
  "EK 9.2.A.1 says the change is calculated from the absolute entropies of the species involved, and the learning objective names those as the standard molar entropies."),
 ("positive and the reaction produces gas where there was none",
  "EK 9.2.A.1's calculation and EK 9.1.A.1's gas-mole rule are two routes to one sign. q19 recomputes both from the table and the equation and requires them to agree."),
 ("gives 2 CO(g)",
  "EK 9.2.A.1 applied to both equations named in the stem. q20 parses each out of the stem and recomputes it from the same table."),
 ("Process 4",
  "EK 9.2.A.1's quantity is signed, so the largest increase is the largest positive entry rather than the largest magnitude. q21 recomputes the maximum and checks it is unique."),
 ("Process 1",
  "A decrease is a negative value under the same signed convention, so the largest decrease is the most negative entry. q22 recomputes the minimum and checks it is unique."),
 ("Processes 2 and 4",
  "EK 9.1.A.1 ties a rise in entropy to matter becoming more dispersed and EK 9.2.A.1 supplies the signed value. q23 recomputes which tabulated rows are positive."),
 ("-237.8 J/(mol K), a decrease",
  "EK 9.2.A.1 applied to two moles condensing, so the single-mole difference between the two water rows is doubled. Recomputed in rxn."),
 ("-80.8 J/(mol K), a decrease",
  "EK 9.2.A.1 with the hydrogen doubled and the solid carbon included in the reactant sum. Recomputed in rxn."),
 ("entropy after the process less the entropy before it",
  "EK 9.2.A.1 describes the calculation as using the absolute entropies of the species before and after the process occurs, which fixes the order of the subtraction."),
 ("-321.4 J/(mol K), a decrease",
  "EK 9.2.A.1 with every entry doubled, giving twice the single-mole value of the reverse reaction. Recomputed in rxn."),
 ("Gaseous water has a larger absolute entropy than liquid water",
  "EK 9.1.A.1 makes matter in the gas state more dispersed than as a liquid, and the table bears it out. q28 checks the keyed comparison holds and every other comparison fails in the table."),
 ("181.5 J/(mol K), an increase",
  "EK 9.2.A.1 for the reverse of the formation reaction, the same magnitude with the opposite sign. Recomputed in rxn."),
 ("negative and a mole of gas is consumed with none produced",
  "EK 9.2.A.1's calculation and EK 9.1.A.1's rule again give one sign. q30 recomputes both from the table and the equation and requires them to agree."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the diagram above, how is the entropy change obtained?"
        h9.no_figure_language(mod)

    def free_energy_creeps_in(mod, cl):
        mod.QUESTIONS[0]["why"] = (
            mod.QUESTIONS[0]["why"] + " The enthalpy change is needed as well.")
        no_free_energy(mod)

    def tabulated_entropy_corrupted(mod, cl):
        mod.QUESTIONS[1]["table"] = dict(
            headers=h9_2._T_S1["headers"],
            rows=[[sp, ("200.0" if sp == "NH3(g)" else v)]
                  for sp, v in h9_2._T_S1["rows"]])

    def key_magnitude_altered(mod, cl):
        # The anchor is moved with the choice, so the structural gate passes and
        # only the recomputation can see the change. Confirmed: the table gives
        # -326.6, so a key reading -326.7 must be refused.
        ch = list(mod.QUESTIONS[3]["choices"])
        ch[0] = "\\( -326.7 \\) J/(mol K), a decrease"
        mod.QUESTIONS[3]["choices"] = ch
        cl[3] = ("326.7 J/(mol K), a decrease", cl[3][1])

    def stimulus_flips_the_sign(mod, cl):
        # The table altered so the recomputed change turns negative while the
        # key still reads +3.1. Confirmed to violate shows_signed rather than
        # any magnitude check: 200.0 - (5.7 + 205.0) is -10.7.
        mod.QUESTIONS[9]["table"] = dict(
            headers=h9_2._T_S2["headers"],
            rows=[[sp, ("200.0" if sp == "CO2(g)" else v)]
                  for sp, v in h9_2._T_S2["rows"]])

    def no_sign_flipped_distractor(mod, cl):
        ch = list(mod.QUESTIONS[1]["choices"])
        ch[1] = "\\( +199.1 \\) J/(mol K), an increase"
        mod.QUESTIONS[1]["choices"] = ch

    def reported_error_value_changed(mod, cl):
        mod.QUESTIONS[15]["q"] = mod.QUESTIONS[15]["q"].replace("+63.3", "+64.3")

    def two_mistakes_reach_the_reported_value(mod, cl):
        # Ammonia given hydrogen's tabulated entropy, so dropping either
        # coefficient lands on the same number and the item has two answers.
        mod.QUESTIONS[15]["q"] = mod.QUESTIONS[15]["q"].replace("+63.3", "-198.1")

    def ranking_table_corrupted(mod, cl):
        mod.QUESTIONS[20]["table"] = dict(
            headers=h9_2._T_RXN["headers"],
            rows=[["1", "-198.1"], ["2", "+318.9"], ["3", "-88.8"], ["4", "+160.7"]])

    def smallest_entropy_moved(mod, cl):
        mod.QUESTIONS[8]["table"] = dict(
            headers=h9_2._T_S1["headers"],
            rows=[[sp, ("300.0" if sp == "H2O(l)" else v)]
                  for sp, v in h9_2._T_S1["rows"]])

    def two_routes_made_to_disagree(mod, cl):
        mod.QUESTIONS[18]["table"] = dict(
            headers=h9_2._T_S3["headers"],
            rows=[[sp, ("20.0" if sp == "CO2(g)" else v)]
                  for sp, v in h9_2._T_S3["rows"]])

    def comparison_reversed(mod, cl):
        mod.QUESTIONS[19]["q"] = (
            "Which reaction has the larger increase in entropy on the tabulated absolute "
            "entropies, C(s) + CO2(g) gives 2 CO(g), or C(s) + O2(g) gives CO2(g)?")

    return [
        ("a stem pointing at a figure the bank cannot show", figure_language),
        ("a why reaching into enthalpy, which is 9.3's material", free_energy_creeps_in),
        ("a tabulated absolute entropy corrupted so the keyed value is wrong",
         tabulated_entropy_corrupted),
        ("a keyed magnitude altered with its anchor moved to match",
         key_magnitude_altered),
        ("the stimulus altered so the recomputed sign no longer matches the key",
         stimulus_flips_the_sign),
        ("an arithmetic item left with no sign-flipped distractor",
         no_sign_flipped_distractor),
        ("a reported wrong answer that no named mistake reproduces",
         reported_error_value_changed),
        ("a reported value that is the CORRECT one, so no mistake was made",
         two_mistakes_reach_the_reported_value),
        ("the ranking table corrupted so the keyed process is no longer the maximum",
         ranking_table_corrupted),
        ("the smallest tabulated entropy moved off the keyed species",
         smallest_entropy_moved),
        ("the table corrupted so the calculation and the gas-mole rule disagree",
         two_routes_made_to_disagree),
        ("the two equations in a comparison stem exchanged", comparison_reversed),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h9_2, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

h9.no_figure_language(h9_2)
no_free_energy(h9_2)
h.run(h9_2, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
