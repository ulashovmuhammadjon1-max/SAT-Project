"""Key audit for AP CHEMISTRY 9.3 Gibbs Free Energy and Thermodynamic Favorability.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  9.3.A.1  the standard state: pure substances, 1.0 M solutions, gases at 1.0
           atm or 1.0 bar                              2, 21
  9.3.A.2  a standard free energy change below zero is thermodynamically
           favored, and "spontaneous" is deprecated because it invites
           "suddenly" or "without cause"      1, 3, 4, 5, 16-22, 26
  9.3.A.3  the change from the standard free energies of formation of products
           less reactants                              16, 17, 18, 19, 20, 21, 22, 30
  9.3.A.4  some cases need both enthalpy and entropy weighed; the freezing of
           water and the dissolution of sodium nitrate are the examples
                                                       23, 24, 25, 30
  9.3.A.5  the change equals the enthalpy change less the temperature times the
           entropy change                              3, 4, 5, 6, 26, 27, 28, 29, 30
  9.3.A.6  the four-way sign table, and the two cases needing no calculation
                                                       7, 8, 9, 10, 11, 12, 13, 14, 15,
                                                       24, 25

THE SWAP GUARD. EK 9.3.A.2 pairs a NEGATIVE free energy change with a FAVORED
process, and that pairing is the single easiest thing in this unit to ship
backwards -- a key naming the right number with the wrong verdict passes every
structural check there is, because the anchor, the choice count and the
containment test all see a perfectly well-formed choice.
``sign_matches_favorability`` therefore reads the signed value and the verdict
out of each such key as two SEPARATE NAMED FACTS and requires them to agree.
Named booleans, not two tuples compared by index: a guard of this shape is
exactly where this project once built one tuple ordered (acid, base) and
another ordered (base, acid) and rejected a correct key.

It also requires a distractor carrying the sign-flipped value, so an item
cannot look like a sign question while offering only wrong magnitudes.

SCOPE. 9.4 owns kinetic control, 9.5 owns the equilibrium constant and 9.8 to
9.11 own the electrochemistry. ``no_neighbouring_topics`` asserts none appears.

ARITHMETIC. Every value is recomputed from the numbers in the stem or the
table, including the joules-to-kilojoules conversion that q29 is built around.

NEGATIVE CONTROL: ``python3 verify_h9_3.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h9_check as h9

import h9_3

GFCOL = "Standard free energy of formation, kJ/mol"

# Explicit lookarounds everywhere, never \b.
_OUT_OF_SCOPE = re.compile(
    r"(?<![A-Za-z])(equilibrium|reaction quotient|cell potential|electrolytic|galvanic|"
    r"kinetic|activation energy|catalyst|rate)(?![A-Za-z])", re.I)

_DH = re.compile(r"\\\(\s*\\Delta H\^\\circ\s*=\s*([+-]?\d+(?:\.\d+)?)\s*\\\)")
_DS = re.compile(r"\\\(\s*\\Delta S\^\\circ\s*=\s*([+-]?\d+(?:\.\d+)?)\s*\\\)")
_AT_T = re.compile(r"(?<![A-Za-z0-9])at (\d+) K(?![A-Za-z])")
_OBTAINS = re.compile(r"obtains \\\(\s*([+-]?\d+(?:\.\d+)?)\s*\\\)")
_VALUE_KJ = re.compile(r"\\\(\s*([+-]\d+(?:\.\d+)?)\s*\\\)\s*kJ/mol")
_LIMIT_K = re.compile(r"(?<![A-Za-z])(Above|Below) (\d+) K(?![A-Za-z])")

# EK 9.3.A.6's table, transcribed as data so a key is compared against the
# framework's own rule rather than against the author's memory of it.
QUADRANT = {("negative", "positive"): "all",
            ("positive", "negative"): "none",
            ("positive", "positive"): "high",
            ("negative", "negative"): "low"}

PHRASE = {"all": "At all temperatures",
          "none": "At no temperature",
          "high": "Only at high temperatures",
          "low": "Only at low temperatures"}

_STEM_SIGNS = re.compile(
    r"(negative|positive) enthalpy change and a (negative|positive) entropy change",
    re.I)

# Items whose key states BOTH a signed value in kJ/mol and a favorability
# verdict. Listed explicitly so the guard cannot quietly stop covering an item
# that was edited. q28 is deliberately absent: its key is exactly zero, which
# EK 9.3.A.2 places on neither side of the boundary, and it says so.
FAVORABILITY_ITEMS = (3, 4, 5, 16, 17, 18, 19, 20, 21, 22, 26)


def no_neighbouring_topics(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in h9.facing(item):
            hit = _OUT_OF_SCOPE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: mentions {hit.group(0)!r}, which belongs to 9.4, "
                f"9.5 or the electrochemistry topics -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no item reaches into kinetic control, the "
          "equilibrium constant or the electrochemical cells.")


def sign_matches_favorability(module):
    """EK 9.3.A.2: below zero is favored, above zero is unfavored.

    Two separately named facts, compared as booleans. The value's sign is read
    from the number; the verdict is read from the words; neither is inferred
    from the other, which is the only way this check can catch a key that has
    them the wrong way round.
    """
    for i in FAVORABILITY_ITEMS:
        item = module.QUESTIONS[i - 1]
        key = h.keyed(item)
        m = _VALUE_KJ.search(key)
        assert m, f"{module.TOPIC[0]} q{i}: the key states no signed kJ/mol value: {key!r}"
        value_is_negative = float(m.group(1)) < 0
        verdict = h9.favorability_verdict(key)
        assert verdict is not None, (
            f"{module.TOPIC[0]} q{i}: the key states no single favorability verdict: {key!r}"
        )
        key_says_favored = verdict
        assert value_is_negative == key_says_favored, (
            f"{module.TOPIC[0]} q{i}: the key pairs {m.group(1)} kJ/mol with "
            f"{'favored' if key_says_favored else 'unfavored'}, which is EK 9.3.A.2 "
            f"backwards -- {key!r}"
        )
        h9.opposite_sign_offered(item, m.group(1))
    print(f"OK  {module.TOPIC[0]} swap guard: {len(FAVORABILITY_ITEMS)} keys pair a "
          "negative value with favored and a positive value with unfavored, each against "
          "a sign-flipped distractor.")


# ---------------------------------------------------------------- stem numerics

def _stem_numbers(stem):
    dh = _DH.search(stem)
    ds = _DS.search(stem)
    assert dh and ds, f"the stem does not state both changes: {stem[:70]!r}"
    return float(dh.group(1)), float(ds.group(1))


def _temperature(stem):
    m = _AT_T.search(stem)
    assert m, f"the stem does not state a temperature: {stem[:70]!r}"
    return float(m.group(1))


def gibbs_item(item):
    """EK 9.3.A.5 recomputed from the three numbers in the stem alone."""
    dh, ds = _stem_numbers(item["q"])
    t = _temperature(item["q"])
    value = h9.gibbs(dh, ds, t)
    token = f"{value:+.1f}"
    h9.shows_signed(item, token)
    flipped = h9.opposite_sign_offered(item, token)
    return (f"the enthalpy change {dh:+.1f} kJ/mol less {t:g} K times the entropy change "
            f"{ds:+.1f} J/(mol K) recomputes to {token} kJ/mol, against {flipped} offered "
            f"as the sign-flipped distractor")


def _crossover(item, favored_above):
    """EK 9.3.A.5 solved for the temperature at which the sign changes.

    ``favored_above`` is checked against EK 9.3.A.6 rather than taken on trust:
    two positive changes are favored at HIGH temperature and two negative ones
    at LOW temperature, so the direction word in the key is a claim the sign
    pair has to support.
    """
    dh, ds = _stem_numbers(item["q"])
    t = h9.crossover_temperature(dh, ds)
    m = _LIMIT_K.search(h.keyed(item))
    assert m, f"the key states no temperature limit: {h.keyed(item)!r}"
    keyed_direction, keyed_t = m.group(1).lower(), float(m.group(2))
    assert abs(keyed_t - t) < 1e-9, (
        f"the stem's numbers put the crossover at {t:g} K, not the {keyed_t:g} K the key "
        f"states"
    )
    both_positive = dh > 0 and ds > 0
    both_negative = dh < 0 and ds < 0
    assert both_positive or both_negative, (
        "a crossover item needs the two changes to share a sign, or EK 9.3.A.6 puts the "
        "process in a row no temperature can move"
    )
    expected_direction = "above" if both_positive else "below"
    assert keyed_direction == expected_direction, (
        f"the key says the process is favored {keyed_direction} the crossover, but EK "
        f"9.3.A.6 puts a process with these signs on the {expected_direction} side"
    )
    assert keyed_direction == ("above" if favored_above else "below"), (
        "the item's own expectation and the key disagree about which side is favored"
    )
    return (f"the stem's numbers put the crossover at {t:g} K and EK 9.3.A.6 puts the "
            f"favored side {expected_direction} it")


def q6(item):
    return _crossover(item, favored_above=True)


def q27(item):
    return _crossover(item, favored_above=False)


def q28(item):
    dh, ds = _stem_numbers(item["q"])
    t = _temperature(item["q"])
    value = h9.gibbs(dh, ds, t)
    assert abs(value) < 1e-9, (
        f"the stem's numbers give {value:+.1f} kJ/mol, so the key claiming exactly zero "
        f"is wrong"
    )
    assert abs(h9.crossover_temperature(dh, ds) - t) < 1e-9, (
        "the stated temperature must be the crossover itself, which is what makes the "
        "result zero"
    )
    assert h9.favorability_verdict(h.keyed(item)) is None, (
        "a free energy change of exactly zero puts the process on neither side of EK "
        "9.3.A.2's boundary, so the key must not call it favored or unfavored"
    )
    h.shows(item, "0.0 kJ/mol, which is the temperature at which the sign changes over")
    return (f"the stem's numbers recompute to {value:+.1f} kJ/mol, the stated {t:g} K "
            f"being exactly the crossover temperature")


def q29(item):
    """Exactly one named mistake reproduces the value the student reports."""
    dh, ds = _stem_numbers(item["q"])
    t = _temperature(item["q"])
    m = _OBTAINS.search(item["q"])
    assert m, f"the stem reports no value: {item['q'][:70]!r}"
    reported = float(m.group(1))
    candidates = dict(
        correct=h9.gibbs(dh, ds, t),
        entropy_left_in_joules=dh - t * ds,
        temperature_in_celsius=h9.gibbs(dh, ds, t - 273.0),
        entropy_term_added=dh + t * ds / 1000.0,
        enthalpy_left_in_joules=dh / 1000.0 - t * ds / 1000.0,
    )
    assert abs(candidates["correct"] - reported) > 1e-9, (
        "the value the student reports is the correct one, so no mistake was made"
    )
    assert abs(candidates["entropy_left_in_joules"] - reported) < 1e-6, (
        f"leaving the entropy change in joules gives "
        f"{candidates['entropy_left_in_joules']:+.1f}, not the {reported:+.1f} reported"
    )
    clashing = [k for k, v in candidates.items()
                if k != "entropy_left_in_joules" and abs(v - reported) < 1e-6]
    assert not clashing, f"the reported value is also produced by {clashing}"
    h.shows(item, "entropy change was left in joules instead of being converted")
    return (f"leaving the entropy change in joules reproduces the reported {reported:+.1f} "
            f"kJ/mol, where the correct value is {candidates['correct']:+.1f} and every "
            f"other named mistake gives something else")


def stated_quadrant(item):
    """EK 9.3.A.6's rule applied to the two signs the stem states in words."""
    m = _STEM_SIGNS.search(item["q"])
    assert m, f"the stem does not state both signs: {item['q'][:70]!r}"
    pair = (m.group(1).lower(), m.group(2).lower())
    want = QUADRANT[pair]
    h.shows(item, PHRASE[want])
    return (f"an enthalpy change that is {pair[0]} with a {pair[1]} entropy change sits in "
            f"the framework's {want}-temperature row")


NUMERIC = {3: gibbs_item, 4: gibbs_item, 5: gibbs_item, 6: q6,
           7: stated_quadrant, 8: stated_quadrant, 9: stated_quadrant,
           10: stated_quadrant, 24: stated_quadrant, 25: stated_quadrant,
           26: gibbs_item, 27: q27, 28: q28, 29: q29}


# ------------------------------------------------------------------ table items

def _quadrant_rows(table):
    out = {}
    for row in table["rows"]:
        pair = (str(row[1]).strip().lower(), str(row[2]).strip().lower())
        assert pair in QUADRANT, f"row {row} states a pair of signs the rule does not cover"
        out[str(row[0])] = QUADRANT[pair]
    return out


def quadrant_item(want, label, anchor):
    def check(table, item):
        rows = _quadrant_rows(table)
        matching = sorted(k for k, v in rows.items() if v == want)
        assert matching == [label], (
            f"the tabulated signs put {matching} in the {want}-temperature row, not the "
            f"single process {label!r} the key names"
        )
        h.shows(item, anchor)
        return (f"reading the tabulated signs through the framework's rule gives {rows}, "
                f"whose only {want}-temperature entry is {label}")
    return check


def formation_of(table):
    return lambda species: cg.cell(table, species, GFCOL)


def gf_item(table, item):
    """EK 9.3.A.3 recomputed from the table and the equation in the stem."""
    reactants, products = h9.species_terms(h9.equation_from(item["q"]))
    value = formation_of(table)
    got = h9.summed(products, value) - h9.summed(reactants, value)
    token = f"{got:+.1f}"
    h9.shows_signed(item, token)
    flipped = h9.opposite_sign_offered(item, token)
    return (f"summing the tabulated formation free energies over the equation in the stem "
            f"gives {token} kJ/mol, against {flipped} offered as the sign-flipped "
            f"distractor")


TABLE_CHECKS = {
    11: quadrant_item("all", "P", "Process P"),
    12: quadrant_item("none", "Q", "Process Q"),
    13: quadrant_item("high", "R", "Process R"),
    14: quadrant_item("low", "S", "Process S"),
    16: gf_item, 17: gf_item, 18: gf_item, 19: gf_item, 20: gf_item,
    21: gf_item, 22: gf_item,
}


CLAIMS = [
 ("misunderstandings that a process happens suddenly or without cause",
  "EK 9.3.A.2 says the phrase thermodynamically favored is preferred so that common misunderstandings, equating spontaneous with suddenly or without cause, can be avoided."),
 ("Pure substances, solutions at 1.0 M, and gases at a pressure of 1.0 atm or 1.0 bar",
  "EK 9.3.A.1 names exactly these as the standard state in which all reactants and products are present when the standard free energy change is defined."),
 ("-40.0 kJ/mol, thermodynamically favored",
  "EK 9.3.A.5's equation with the entropy change converted to kilojoules, and EK 9.3.A.2's rule that below zero is favored. Recomputed in gibbs_item from the three numbers in the stem."),
 ("+20.0 kJ/mol, thermodynamically unfavored",
  "EK 9.3.A.5 at a temperature too low for the entropy term to overcome the enthalpy term, with EK 9.3.A.2 reading the positive result as unfavored. Recomputed in gibbs_item."),
 ("-10.0 kJ/mol, thermodynamically favored",
  "EK 9.3.A.5 at twice the temperature, which doubles the entropy term and turns the result negative -- EK 9.3.A.6's high-temperature row. Recomputed in gibbs_item."),
 ("Above 500 K",
  "EK 9.3.A.5's expression changes sign at the quotient of the two changes once the units agree, and EK 9.3.A.6 puts two positive changes on the high-temperature side. Recomputed in q6."),
 ("At all temperatures",
  "EK 9.3.A.6's table assigns a negative enthalpy change with a positive entropy change to the row favored at all temperatures. Checked against the rule in stated_quadrant."),
 ("At no temperature",
  "EK 9.3.A.6's table assigns a positive enthalpy change with a negative entropy change to the row favored at no temperature. Checked in stated_quadrant."),
 ("Only at high temperatures",
  "EK 9.3.A.6's table assigns two positive changes to the high-temperature row, because the entropy term of EK 9.3.A.5 grows with temperature. Checked in stated_quadrant."),
 ("Only at low temperatures",
  "EK 9.3.A.6's table assigns two negative changes to the low-temperature row, because raising the temperature enlarges a term that here opposes favorability. Checked in stated_quadrant."),
 ("Process P",
  "EK 9.3.A.6's table applied to four tabulated pairs of signs. q11 reads every row through the framework's rule and checks exactly one lands in the row the key names."),
 ("Process Q",
  "The same rule applied to the favored-at-no-temperature row. q12 recomputes every tabulated row and checks the match is unique."),
 ("Process R",
  "The same rule applied to the high-temperature row, which EK 9.3.A.6 assigns to two positive changes. q13 recomputes every tabulated row."),
 ("Process S",
  "The same rule applied to the low-temperature row, which EK 9.3.A.6 assigns to two negative changes. q14 recomputes every tabulated row."),
 ("negative with a positive entropy change, and when it is positive with a negative entropy change",
  "EK 9.3.A.6 says no calculation is necessary in exactly those two cases -- favored in the first, unfavored in the second -- because they are the rows no temperature can move."),
 ("-32.8 kJ/mol, thermodynamically favored",
  "EK 9.3.A.3's sum of formation free energies, products less reactants, with EK 9.3.A.2 reading the negative result as favored. Recomputed in gf_item from the table and the stem."),
 ("-818.1 kJ/mol, thermodynamically favored",
  "EK 9.3.A.3 with the water entry doubled and the methane entry subtracted rather than dropped. Recomputed in gf_item."),
 ("+130.4 kJ/mol, thermodynamically unfavored",
  "EK 9.3.A.3 summing both products before subtracting the single reactant, with EK 9.3.A.2 reading the positive result as unfavored under standard conditions. Recomputed in gf_item."),
 ("+173.2 kJ/mol, thermodynamically unfavored",
  "EK 9.3.A.3 with the tabulated value for nitrogen monoxide doubled and both elemental reactants contributing nothing. Recomputed in gf_item."),
 ("-70.6 kJ/mol, thermodynamically favored",
  "EK 9.3.A.3 with both nitrogen oxides doubled; dropping either coefficient changes the size and, in one case, the sign. Recomputed in gf_item."),
 ("+8.5 kJ/mol, thermodynamically unfavored",
  "EK 9.3.A.3 applied to a physical process, with EK 9.3.A.1's standard state fixing the vapour at 1.0 atm, which is why the small positive result means not favored. Recomputed in gf_item."),
 ("+32.8 kJ/mol, thermodynamically unfavored",
  "EK 9.3.A.3's subtraction runs products less reactants, so the reverse reaction has the same magnitude with the opposite sign. Recomputed in gf_item."),
 ("The freezing of water and the dissolution of sodium nitrate",
  "EK 9.3.A.4 names exactly these two as examples of processes for which both enthalpy and entropy must be considered before favorability can be decided."),
 ("Only at low temperatures",
  "EK 9.3.A.4 names freezing as such a case and EK 9.3.A.6's table puts two negative changes in the low-temperature row. Checked against the rule in stated_quadrant."),
 ("Only at high temperatures",
  "EK 9.3.A.4 names this dissolution as such a case and EK 9.3.A.6's table puts two positive changes in the high-temperature row. Checked in stated_quadrant."),
 ("+20.0 kJ/mol, thermodynamically unfavored",
  "EK 9.3.A.5 with a negative entropy term subtracted, which adds to the enthalpy change and here outweighs it, putting 500 K past the crossover of EK 9.3.A.6's low-temperature row. Recomputed in gibbs_item."),
 ("Below 400 K",
  "EK 9.3.A.5's expression changes sign at the quotient of the two changes, and EK 9.3.A.6 puts two negative changes on the low-temperature side. Recomputed in q27."),
 ("0.0 kJ/mol, which is the temperature at which the sign changes over",
  "EK 9.3.A.5's two terms are equal in size at the stated temperature, so the difference is zero and the process sits on EK 9.3.A.2's boundary rather than on either side of it. Recomputed in q28."),
 ("entropy change was left in joules instead of being converted",
  "EK 9.3.A.5 multiplies the entropy change by a few hundred kelvin, so an unconverted entropy change inflates that term about a thousandfold. q29 recomputes every named mistake and checks only this one reproduces the reported value."),
 ("standard free energies of formation, or from the enthalpy and entropy changes",
  "EK 9.3.A.3 gives the first route and EK 9.3.A.5 the second, and EK 9.3.A.4 explains why neither the enthalpy nor the entropy change settles the matter alone."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the diagram above, why is the older word avoided?"
        h9.no_figure_language(mod)

    def equilibrium_creeps_in(mod, cl):
        mod.QUESTIONS[1]["why"] = (
            mod.QUESTIONS[1]["why"] + " The equilibrium constant follows from it.")
        no_neighbouring_topics(mod)

    def verdict_flipped_on_a_key(mod, cl):
        # The defect the structural gate cannot see. The number is untouched and
        # the anchor is moved with the wording, so cg_check passes; only the
        # swap guard can refuse a negative value called unfavored.
        ch = list(mod.QUESTIONS[2]["choices"])
        ch[0] = "\\( -40.0 \\) kJ/mol, thermodynamically unfavored"
        mod.QUESTIONS[2]["choices"] = ch
        cl[2] = ("40.0 kJ/mol, thermodynamically unfavored", cl[2][1])
        sign_matches_favorability(mod)

    def verdict_flipped_on_a_formation_key(mod, cl):
        ch = list(mod.QUESTIONS[17]["choices"])
        ch[0] = "\\( +130.4 \\) kJ/mol, thermodynamically favored"
        mod.QUESTIONS[17]["choices"] = ch
        cl[17] = ("130.4 kJ/mol, thermodynamically favored", cl[17][1])
        sign_matches_favorability(mod)

    def sign_flipped_distractor_removed(mod, cl):
        ch = list(mod.QUESTIONS[2]["choices"])
        ch[1] = "\\( +45.0 \\) kJ/mol, thermodynamically unfavored"
        mod.QUESTIONS[2]["choices"] = ch
        sign_matches_favorability(mod)

    def entropy_units_ignored(mod, cl):
        # The stem's entropy change written as though it were already in kJ,
        # so the recomputed value is no longer the keyed one.
        mod.QUESTIONS[2]["q"] = mod.QUESTIONS[2]["q"].replace("-200.0", "-0.2")

    def temperature_changed(mod, cl):
        mod.QUESTIONS[3]["q"] = mod.QUESTIONS[3]["q"].replace("at 300 K", "at 900 K")

    def crossover_direction_reversed(mod, cl):
        ch = list(mod.QUESTIONS[5]["choices"])
        ch[0] = "Below 500 K"
        mod.QUESTIONS[5]["choices"] = ch
        cl[5] = ("Below 500 K", cl[5][1])

    def stated_signs_exchanged(mod, cl):
        # The stem now describes the favored-at-no-temperature case while the
        # key still says all temperatures.
        mod.QUESTIONS[6]["q"] = (
            "A process here has a positive enthalpy change and a negative entropy change. "
            "At which temperatures is it thermodynamically favored?")

    def quadrant_table_corrupted(mod, cl):
        mod.QUESTIONS[10]["table"] = dict(
            headers=h9_3._T_QUAD["headers"],
            rows=[["P", "positive", "positive"], ["Q", "positive", "negative"],
                  ["R", "positive", "positive"], ["S", "negative", "negative"]])

    def quadrant_table_gains_a_second_match(mod, cl):
        mod.QUESTIONS[10]["table"] = dict(
            headers=h9_3._T_QUAD["headers"],
            rows=[["P", "negative", "positive"], ["Q", "negative", "positive"],
                  ["R", "positive", "positive"], ["S", "negative", "negative"]])

    def formation_value_corrupted(mod, cl):
        mod.QUESTIONS[15]["table"] = dict(
            headers=h9_3._T_GF["headers"],
            rows=[[sp, ("-40.0" if sp == "NH3(g)" else v)]
                  for sp, v in h9_3._T_GF["rows"]])

    def reported_mistake_value_changed(mod, cl):
        mod.QUESTIONS[28]["q"] = mod.QUESTIONS[28]["q"].replace("+59900.0", "+59000.0")

    def zero_item_given_a_verdict(mod, cl):
        ch = list(mod.QUESTIONS[27]["choices"])
        ch[0] = "\\( 0.0 \\) kJ/mol, so the process is thermodynamically favored"
        mod.QUESTIONS[27]["choices"] = ch
        cl[27] = ("0.0 kJ/mol, so the process is thermodynamically favored", cl[27][1])

    return [
        ("a stem pointing at a figure the bank cannot show", figure_language),
        ("a why reaching into the equilibrium constant, which is 9.5's material",
         equilibrium_creeps_in),
        ("a negative free energy change keyed as unfavored", verdict_flipped_on_a_key),
        ("a positive free energy change keyed as favored",
         verdict_flipped_on_a_formation_key),
        ("a favorability item left with no sign-flipped distractor",
         sign_flipped_distractor_removed),
        ("the stem's entropy change rewritten so the keyed value no longer follows",
         entropy_units_ignored),
        ("the temperature in a stem changed while the key stands", temperature_changed),
        ("a crossover key claiming the favored side is below rather than above",
         crossover_direction_reversed),
        ("the two signs in a stem exchanged while the key stands",
         stated_signs_exchanged),
        ("the sign table corrupted so the keyed process is in the wrong row",
         quadrant_table_corrupted),
        ("a second tabulated process put in the same row as the keyed one",
         quadrant_table_gains_a_second_match),
        ("a tabulated formation free energy corrupted", formation_value_corrupted),
        ("a reported wrong answer that no named mistake reproduces",
         reported_mistake_value_changed),
        ("the exactly-zero item given a favorability verdict it cannot support",
         zero_item_given_a_verdict),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h9_3, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

h9.no_figure_language(h9_3)
no_neighbouring_topics(h9_3)
sign_matches_favorability(h9_3)
h.run(h9_3, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
