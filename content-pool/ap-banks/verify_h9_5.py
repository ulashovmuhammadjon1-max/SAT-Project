"""Key audit for AP CHEMISTRY 9.5 Free Energy and Equilibrium.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  9.5.A.1  thermodynamically favored means the products are favored at
           equilibrium, K above 1, under standard conditions   1, 17, 23
  9.5.A.2  the two equations relating K and the standard free energy change
                   2, 3, 8, 9, 10, 11, 12, 13, 16, 18, 19, 26, 27, 28
  9.5.A.3  the connection can be made qualitatively by estimation: near zero
           gives K near 1, and a change many times RT deviates strongly
                   6, 7, 21, 22, 24, 25, 29
  9.5.A.4  a change below zero favors products, one above zero favors reactants
                   4, 5, 14, 15, 20, 30

THE SWAP GUARD. EK 9.5.A.4 pairs a free energy change BELOW zero with K ABOVE
1. A key pairing them the other way round is well formed, contradicts nothing
structural, and is wrong. ``sign_matches_k`` reads the sign of the value and the
direction of the K clause out of each such key as two separately named facts and
requires them to agree; ``sign_to_k`` does the same where the sign is stated in
the stem in words instead. Both are negative-controlled in both directions.

Because the anchor mechanism matches through ``cg_check.normalize``, which
strips a leading plus, a mutation that flips a K clause makes the anchor
ambiguous and would trip the structural gate first. The controls below therefore
call the guard directly, so each one fails on the check it exists to exercise.

HOW THIS TOPIC IS KEPT DISTINCT FROM 9.3 AND 9.9. All three relate the free
energy change to something else. Everything here asks about the POSITION OF
EQUILIBRIUM; ``no_neighbouring_topics`` asserts that no item computes a free
energy change from an enthalpy and an entropy, or reaches into the cells.

ARITHMETIC. RT is given in the stem wherever it is needed, so every value is
recomputed from the stem alone in one multiplication or division.

NEGATIVE CONTROL: ``python3 verify_h9_5.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h9_check as h9

import h9_5

KCOL = "Equilibrium constant at 300 K"
GCOL = "Standard free energy change, kJ/mol"

# Explicit lookarounds, never \b. "equilibrium" is of course allowed here.
_OUT_OF_SCOPE = re.compile(
    r"(?<![A-Za-z])(enthalpy|entropy|cell potential|electrode|galvanic|electrolytic|"
    r"kinetic control|catalys[et]|nernst)(?![A-Za-z])", re.I)

_RT = re.compile(r"\\\(\s*RT\s*=\s*([\d.]+)\s*\\\)")
_LNK = re.compile(r"\\\(\s*\\ln K\s*=\s*([+-]?[\d.]+)\s*\\\)")
_DG = re.compile(r"\\\(\s*([+-]\d+(?:\.\d+)?)\s*\\\)\s*kJ/mol")
_STEM_SIGN = re.compile(r"standard free energy change (below|above) zero", re.I)
# The lookahead stops "greater than 1" matching inside "greater than 100".
_K_CLAUSE = re.compile(r"equilibrium constant is (greater|less) than 1(?![0-9])", re.I)

# Keys stating BOTH a signed value and a direction for K. Listed explicitly so
# the guard cannot quietly stop covering an item that was edited. q10 is absent
# on purpose: its value is exactly zero and its key says the constant is exactly
# 1, which is the boundary rather than either side of it.
KEY_VALUE_K_ITEMS = (8, 9, 11)


def no_neighbouring_topics(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in h9.facing(item):
            hit = _OUT_OF_SCOPE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: mentions {hit.group(0)!r}, which belongs to 9.3, "
                f"9.4 or the electrochemistry topics -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no item computes a free energy change from an "
          "enthalpy and an entropy or reaches into the cells.")


def _k_direction(text):
    """Whether the text puts K above 1, below it, or says neither."""
    hits = {m.group(1).lower() for m in _K_CLAUSE.finditer(text)}
    if hits == {"greater"}:
        return True
    if hits == {"less"}:
        return False
    return None


def _clause_agrees(item, value, where):
    """EK 9.5.A.4: below zero goes with K above 1, and above zero with K below it."""
    key_says_k_above_one = _k_direction(h.keyed(item))
    assert key_says_k_above_one is not None, (
        f"{where}: the key states no single direction for the equilibrium constant: "
        f"{h.keyed(item)!r}"
    )
    value_is_negative = value < 0
    assert value_is_negative == key_says_k_above_one, (
        f"{where}: the key pairs a free energy change of {value:+.1f} kJ/mol with an "
        f"equilibrium constant {'above' if key_says_k_above_one else 'below'} 1, which is "
        f"EK 9.5.A.4 backwards -- {h.keyed(item)!r}"
    )
    return key_says_k_above_one


def sign_matches_k(module, claims=None):
    for i in KEY_VALUE_K_ITEMS:
        item = module.QUESTIONS[i - 1]
        m = _DG.search(h.keyed(item))
        assert m, (
            f"{module.TOPIC[0]} q{i}: the key states no signed kJ/mol value: "
            f"{h.keyed(item)!r}"
        )
        _clause_agrees(item, float(m.group(1)), f"{module.TOPIC[0]} q{i}")
        h9.opposite_sign_offered(item, m.group(1))
    print(f"OK  {module.TOPIC[0]} swap guard: {len(KEY_VALUE_K_ITEMS)} keys pair a "
          "negative free energy change with an equilibrium constant above 1 and a "
          "positive one with a constant below 1, each against a sign-flipped distractor.")


# ---------------------------------------------------------------- stem numerics

def _one(pattern, text, what):
    hits = pattern.findall(text)
    assert len(hits) == 1, f"expected one {what} in the stem, found {hits}"
    return float(hits[0])


def sign_to_k(item):
    """The sign stated in the stem in words, checked against the key's K clause."""
    m = _STEM_SIGN.search(item["q"])
    assert m, f"the stem states no direction for the free energy change: {item['q'][:70]!r}"
    stem_says_below_zero = m.group(1).lower() == "below"
    key_says_k_above_one = _k_direction(h.keyed(item))
    assert key_says_k_above_one is not None, (
        f"the key states no single direction for the equilibrium constant: "
        f"{h.keyed(item)!r}"
    )
    assert stem_says_below_zero == key_says_k_above_one, (
        f"the stem puts the free energy change {'below' if stem_says_below_zero else 'above'} "
        f"zero and the key puts the equilibrium constant "
        f"{'above' if key_says_k_above_one else 'below'} 1, which is EK 9.5.A.4 backwards"
    )
    return (f"a free energy change {'below' if stem_says_below_zero else 'above'} zero goes "
            f"with an equilibrium constant "
            f"{'above' if key_says_k_above_one else 'below'} 1, as EK 9.5.A.4 states")


def dg_from_lnk(item):
    rt = _one(_RT, item["q"], "value of RT")
    lnk = _one(_LNK, item["q"], "logarithm of K")
    value = -rt * lnk
    token = f"{value:+.1f}"
    h9.shows_signed(item, token)
    flipped = h9.opposite_sign_offered(item, token)
    _clause_agrees(item, value, "the keyed choice")
    return (f"minus {rt:g} kJ/mol times a logarithm of {lnk:+g} recomputes the free energy "
            f"change as {token} kJ/mol, against {flipped} offered as the sign-flipped "
            f"distractor")


def lnk_from_dg(item):
    rt = _one(_RT, item["q"], "value of RT")
    dg = _one(_DG, item["q"], "free energy change")
    lnk = -dg / rt
    token = f"{lnk:+.1f}"
    h9.shows_signed(item, token)
    flipped = h9.opposite_sign_offered(item, token)
    return (f"minus {dg:+g} kJ/mol divided by {rt:g} kJ/mol recomputes the logarithm as "
            f"{token}, against {flipped} offered as the sign-flipped distractor")


def q10(item):
    rt = _one(_RT, item["q"], "value of RT")
    lnk = _one(_LNK, item["q"], "logarithm of K")
    value = -rt * lnk
    assert abs(lnk) < 1e-12, f"the stem's logarithm is {lnk}, not zero"
    assert abs(value) < 1e-12, f"the free energy change recomputes to {value}, not zero"
    assert _k_direction(h.keyed(item)) is None, (
        "a logarithm of zero puts the constant exactly at 1, so the key must not place it "
        "above or below"
    )
    h.shows(item, "0.0 kJ/mol, and the equilibrium constant is exactly 1")
    return (f"a logarithm of zero makes the free energy change {value:+.1f} kJ/mol whatever "
            f"RT is, and RT here is {rt:g} kJ/mol")


def estimate_small(item):
    rt = _one(_RT, item["q"], "value of RT")
    dg = _one(_DG, item["q"], "free energy change")
    assert abs(dg) < rt, (
        f"the free energy change {dg:+g} kJ/mol is not small compared with RT = {rt:g}, so "
        f"EK 9.5.A.3's near-zero estimate does not apply"
    )
    assert dg < 0, f"the free energy change {dg:+g} must be below zero for the keyed side"
    h.shows(item, "A little above 1")
    return (f"the free energy change {dg:+g} kJ/mol is smaller in size than RT = {rt:g} "
            f"kJ/mol and lies below zero, so the constant sits a little above 1")


def estimate_large(item):
    rt = _one(_RT, item["q"], "value of RT")
    dg = _one(_DG, item["q"], "free energy change")
    assert abs(dg) > 5 * rt, (
        f"the free energy change {dg:+g} kJ/mol is not many times RT = {rt:g}, so EK "
        f"9.5.A.3's strong-deviation estimate does not apply"
    )
    assert dg < 0, f"the free energy change {dg:+g} must be below zero for the keyed side"
    h.shows(item, "Very much greater than 1")
    return (f"the free energy change {dg:+g} kJ/mol is {abs(dg) / rt:g} times RT = {rt:g} "
            f"kJ/mol and lies below zero, so the constant deviates strongly upward")


def compare_two(item):
    values = [float(v) for v in _DG.findall(item["q"])]
    assert len(values) == 2, f"expected two free energy changes in the stem, found {values}"
    assert all(v < 0 for v in values), (
        f"both processes must be favored for the comparison the key makes: {values}"
    )
    assert values[0] != values[1], "the two values must differ, or neither is the larger"
    larger_k_is_more_negative = min(values) < max(values)
    assert larger_k_is_more_negative, "the more negative value is the one giving the larger K"
    h.shows(item, "more negative")
    return (f"of the two stated changes {values}, the more negative gives the larger "
            f"logarithm under the framework's equation and so the larger constant")


NUMERIC = {4: sign_to_k, 5: sign_to_k, 8: dg_from_lnk, 9: dg_from_lnk, 10: q10,
           11: dg_from_lnk, 12: lnk_from_dg, 13: lnk_from_dg, 24: estimate_small,
           25: estimate_large, 26: compare_two}


# ------------------------------------------------------------------ table items

def _ks(table):
    return dict(zip(cg.labels(table), cg.col(table, KCOL)))


def _gs(table):
    return dict(zip(cg.labels(table), cg.col(table, GCOL)))


def q14(table, item):
    ks = _ks(table)
    biggest = max(ks, key=ks.get)
    assert biggest == "1", f"the largest tabulated constant is at {biggest}: {ks}"
    assert len([v for v in ks.values() if abs(v - ks[biggest]) < 1e-12]) == 1, (
        f"the largest tabulated constant must be unique: {ks}"
    )
    h.shows(item, "Reaction 1")
    return f"the tabulated constants are {ks}, whose unique maximum is at {biggest}"


def q15(table, item):
    below = sorted(lab for lab, v in _ks(table).items() if v < 1)
    assert below == ["2"], f"the tabulated constants below 1 are {below}"
    h.shows(item, "Reaction 2")
    return f"exactly one tabulated constant lies below 1: {below[0]}"


def q16(table, item):
    unity = sorted(lab for lab, v in _ks(table).items() if abs(v - 1.0) < 1e-12)
    assert unity == ["3"], f"the tabulated constants equal to 1 are {unity}"
    h.shows(item, "Reaction 3")
    return (f"exactly one tabulated constant is 1, at {unity[0]}, where the logarithm and "
            f"so the free energy change are zero")


def q17(table, item):
    above = sorted(lab for lab, v in _ks(table).items() if v > 1)
    assert above == ["1", "4"], f"the tabulated constants above 1 are {above}"
    assert any(abs(v - 1.0) < 1e-12 for v in _ks(table).values()), (
        "the table must include a constant of exactly 1, or the item does not test that "
        "the boundary is excluded"
    )
    h.shows(item, "Reactions 1 and 4, whose constants are greater than 1")
    return (f"the tabulated constants strictly above 1 are {above}, with the row at "
            f"exactly 1 excluded")


def q18(table, item):
    gs = _gs(table)
    lowest = min(gs, key=gs.get)
    assert lowest == "P", f"the most negative tabulated change is at {lowest}: {gs}"
    assert len([v for v in gs.values() if abs(v - gs[lowest]) < 1e-12]) == 1, (
        f"the most negative tabulated change must be unique: {gs}"
    )
    h.shows(item, "Process P")
    return (f"the tabulated free energy changes are {gs}, whose unique minimum is at "
            f"{lowest}, and the framework's equation makes that the largest constant")


def q19(table, item):
    zeros = sorted(lab for lab, v in _gs(table).items() if abs(v) < 1e-12)
    assert zeros == ["S"], f"the tabulated changes equal to zero are {zeros}"
    h.shows(item, "Process S")
    return f"exactly one tabulated free energy change is zero, at {zeros[0]}"


def q20(table, item):
    above = sorted(lab for lab, v in _gs(table).items() if v > 0)
    assert above == ["Q"], f"the tabulated changes above zero are {above}"
    h.shows(item, "Process Q")
    return f"exactly one tabulated free energy change lies above zero: {above[0]}"


def q21(table, item):
    favoring = {lab: v for lab, v in _gs(table).items() if v < 0}
    nearest = min(favoring, key=lambda lab: abs(favoring[lab]))
    assert nearest == "R", (
        f"among the tabulated rows below zero, the one nearest zero is {nearest}: {favoring}"
    )
    assert len([v for v in favoring.values()
                if abs(abs(v) - abs(favoring[nearest])) < 1e-12]) == 1, (
        f"that row must be unique, or the key is not the only defensible answer: {favoring}"
    )
    h.shows(item, "Process R")
    return (f"the tabulated rows favoring products are {favoring}, whose smallest size is "
            f"at {nearest}, the nearest to a constant of 1")


TABLE_CHECKS = {14: q14, 15: q15, 16: q16, 17: q17, 18: q18, 19: q19, 20: q20, 21: q21}


CLAIMS = [
 ("products are favored at equilibrium, so the equilibrium constant is greater than 1",
  "EK 9.5.A.1, verbatim in substance: thermodynamically favored means the products are favored at equilibrium, K above 1, under standard conditions -- a statement about position, not completion."),
 ("-RT \\ln K",
  "EK 9.5.A.2 gives this equation directly; dropping the temperature or dividing by the logarithm changes the units as well as the value."),
 ("e^{-\\Delta G^\\circ / RT}",
  "EK 9.5.A.2's exponential form, the same relationship rearranged; RT belongs in the denominator of the exponent."),
 ("greater than 1, and products are favored at equilibrium",
  "EK 9.5.A.4: a process with a standard free energy change below zero favors products. sign_to_k reads the stem's direction and the key's clause as two named facts and requires them to agree."),
 ("less than 1, and reactants are favored at equilibrium",
  "EK 9.5.A.4's mirror clause: a change above zero favors reactants. An equilibrium constant is never negative whatever the sign of the change. Checked in sign_to_k."),
 ("It will be close to 1",
  "EK 9.5.A.3 states that when the standard free energy change is near zero the equilibrium constant will be close to 1, reached by estimation rather than calculation."),
 ("It deviates strongly from 1",
  "EK 9.5.A.3 states that when the change is much larger or much smaller than RT, K deviates strongly from 1 -- RT being the scale the comparison is made against."),
 ("-10.0 kJ/mol, and the equilibrium constant is greater than 1",
  "EK 9.5.A.2's logarithmic equation with the sign reversed, and EK 9.5.A.4's pairing. Recomputed in dg_from_lnk from RT and the logarithm stated in the stem."),
 ("+20.0 kJ/mol, and the equilibrium constant is less than 1",
  "EK 9.5.A.2 turning a negative logarithm into a positive change, with EK 9.5.A.4 putting such a process on the reactant side. Recomputed in dg_from_lnk."),
 ("0.0 kJ/mol, and the equilibrium constant is exactly 1",
  "EK 9.5.A.2's equation gives zero for a logarithm of zero whatever RT is, and that is the boundary of EK 9.5.A.4 rather than either side of it. Recomputed in q10."),
 ("-20.0 kJ/mol, and the equilibrium constant is greater than 1",
  "EK 9.5.A.2 carries RT as a factor, so the same logarithm at twice the value of RT doubles the change. Recomputed in dg_from_lnk, which also checks the smaller value is offered."),
 ("\\ln K = +10.0",
  "EK 9.5.A.2 rearranged: the logarithm is the change divided by RT with the sign reversed. Recomputed in lnk_from_dg."),
 ("\\ln K = -3.0",
  "EK 9.5.A.2 rearranged for a change above zero, which gives a negative logarithm and so a constant below 1, as EK 9.5.A.4 requires. Recomputed in lnk_from_dg."),
 ("Reaction 1",
  "EK 9.5.A.4 makes a larger constant a position of equilibrium lying further toward products. q14 recomputes the maximum from the table and checks it is unique."),
 ("Reaction 2",
  "EK 9.5.A.4 makes a constant below 1 the mark of a process favoring reactants. q15 recomputes which tabulated rows are below 1."),
 ("Reaction 3",
  "EK 9.5.A.2 makes the change zero exactly when the logarithm is, which is a constant of 1. q16 recomputes which tabulated constant is 1."),
 ("Reactions 1 and 4, whose constants are greater than 1",
  "EK 9.5.A.1 ties favorability to a constant GREATER than 1, so the row at exactly 1 is excluded. q17 recomputes the rows strictly above 1 and checks the boundary row exists."),
 ("Process P",
  "EK 9.5.A.2 makes the logarithm the change divided by RT with the sign reversed, so the most negative change gives the largest constant. q18 recomputes the minimum and checks it is unique."),
 ("Process S",
  "EK 9.5.A.2 gives a logarithm of zero for a change of zero, which is a constant of exactly 1. q19 recomputes which tabulated change is zero."),
 ("Process Q",
  "EK 9.5.A.4 puts a change above zero on the reactant side. q20 recomputes which tabulated change lies above zero; a change of zero favors neither side."),
 ("Process R",
  "EK 9.5.A.3 makes a change near zero correspond to a constant near 1. q21 recomputes the sizes of the tabulated rows below zero and checks the smallest is unique."),
 ("scale against which the size of the free energy change is judged",
  "EK 9.5.A.3 compares the change with RT, so RT supplies the standard of comparison without which calling a change large or small would mean nothing."),
 ("claim that a favored process has its products favored at equilibrium",
  "EK 9.5.A.1 attaches the phrase under standard conditions to exactly that claim, since the standard free energy change is defined for EK 9.3.A.1's standard state."),
 ("A little above 1",
  "EK 9.5.A.3's near-zero estimate with EK 9.5.A.4's direction. estimate_small checks from the stem that the change really is smaller in size than RT and really lies below zero."),
 ("Very much greater than 1",
  "EK 9.5.A.3's strong-deviation estimate with EK 9.5.A.4's direction. estimate_large checks from the stem that the change is many times RT and below zero."),
 ("more negative",
  "EK 9.5.A.2 makes the logarithm proportional to the change with the sign reversed, so at one temperature the more negative change gives the larger constant. Checked in compare_two."),
 ("logarithm of the constant changes sign, so the constant becomes its reciprocal",
  "EK 9.5.A.2 makes the logarithm the change divided by RT with the sign reversed, so reversing the change reverses the logarithm, and a logarithm of opposite sign belongs to the reciprocal constant."),
 ("size would fall, because RT is larger, so the constant moves toward 1",
  "EK 9.5.A.2 divides the change by RT, so a larger RT with the same numerator gives a logarithm of smaller size, which EK 9.5.A.3 reads as a constant nearer 1."),
 ("Qualitatively, through estimation",
  "EK 9.5.A.3 opens by saying connections between K and the standard free energy change can be made qualitatively through estimation."),
 ("change below zero with a constant above 1, and a change above zero with a constant below 1",
  "EK 9.5.A.4 states both halves, and the pairing is fixed by the minus sign in EK 9.5.A.2's equation rather than by the temperature."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the diagram above, what does the phrase mean?"
        h9.no_figure_language(mod)

    def enthalpy_creeps_in(mod, cl):
        mod.QUESTIONS[0]["why"] = mod.QUESTIONS[0]["why"] + " The enthalpy change decides."
        no_neighbouring_topics(mod)

    def k_clause_flipped_on_a_key(mod, cl):
        # The number is left alone and only the direction of the K clause is
        # turned round. The guard is called directly because flipping the clause
        # makes the anchor ambiguous, and the structural gate would otherwise
        # fail first and leave this check unexercised.
        ch = list(mod.QUESTIONS[7]["choices"])
        ch[0] = "\\( -10.0 \\) kJ/mol, and the equilibrium constant is less than 1"
        mod.QUESTIONS[7]["choices"] = ch
        sign_matches_k(mod)

    def k_clause_flipped_the_other_way(mod, cl):
        ch = list(mod.QUESTIONS[8]["choices"])
        ch[0] = "\\( +20.0 \\) kJ/mol, and the equilibrium constant is greater than 1"
        mod.QUESTIONS[8]["choices"] = ch
        sign_matches_k(mod)

    def sign_flipped_distractor_removed(mod, cl):
        ch = list(mod.QUESTIONS[7]["choices"])
        ch[1] = "\\( +14.0 \\) kJ/mol, and the equilibrium constant is less than 1"
        mod.QUESTIONS[7]["choices"] = ch
        sign_matches_k(mod)

    def stem_sign_word_flipped(mod, cl):
        # Rewritten rather than patched in place: replacing the word alone would
        # make this stem open exactly like the next item's, and the
        # duplicate-opening check would fire first and leave sign_to_k
        # unexercised -- a control that passes for a reason it did not test.
        mod.QUESTIONS[3]["q"] = (
            "Take a process with a standard free energy change above zero. What follows "
            "about the equilibrium constant under standard conditions?")

    def rt_changed_in_a_stem(mod, cl):
        mod.QUESTIONS[7]["q"] = mod.QUESTIONS[7]["q"].replace("RT = 2.5", "RT = 3.5")

    def logarithm_sign_flipped_in_a_stem(mod, cl):
        mod.QUESTIONS[11]["q"] = mod.QUESTIONS[11]["q"].replace("-25.0", "+25.0")

    def zero_item_given_a_direction(mod, cl):
        mod.QUESTIONS[9]["q"] = mod.QUESTIONS[9]["q"].replace("\\ln K = 0", "\\ln K = 2.0")

    def small_change_made_large(mod, cl):
        mod.QUESTIONS[23]["q"] = mod.QUESTIONS[23]["q"].replace("-0.5", "-25.0")

    def large_change_made_small(mod, cl):
        mod.QUESTIONS[24]["q"] = mod.QUESTIONS[24]["q"].replace("-60.0", "-3.0")

    def compared_processes_made_unfavored(mod, cl):
        mod.QUESTIONS[25]["q"] = (
            mod.QUESTIONS[25]["q"].replace("-5.0", "+5.0").replace("-50.0", "+50.0"))

    def constant_table_maximum_moved(mod, cl):
        mod.QUESTIONS[13]["table"] = dict(
            headers=h9_5._T_K["headers"],
            rows=[["1", "15"], ["2", "0.004"], ["3", "1.0"], ["4", "25"]])

    def boundary_row_removed(mod, cl):
        # The row at exactly 1 replaced by another above it, so the item stops
        # testing that "greater than 1" excludes the boundary. The keyed pair
        # would then be wrong as well, and q17 must refuse it.
        mod.QUESTIONS[16]["table"] = dict(
            headers=h9_5._T_K["headers"],
            rows=[["1", "1500"], ["2", "0.004"], ["3", "3.0"], ["4", "25"]])

    def free_energy_table_corrupted(mod, cl):
        mod.QUESTIONS[17]["table"] = dict(
            headers=h9_5._T_G["headers"],
            rows=[["P", "-2.0"], ["Q", "+15.0"], ["R", "-5.0"], ["S", "0.0"]])

    def nearest_to_one_tied(mod, cl):
        mod.QUESTIONS[20]["table"] = dict(
            headers=h9_5._T_G["headers"],
            rows=[["R", "-5.0"], ["P", "-5.0"], ["Q", "+15.0"], ["S", "0.0"]])

    return [
        ("a stem pointing at a figure the bank cannot show", figure_language),
        ("a why reaching into enthalpy, which is 9.3's material", enthalpy_creeps_in),
        ("a negative free energy change keyed with a constant below 1",
         k_clause_flipped_on_a_key),
        ("a positive free energy change keyed with a constant above 1",
         k_clause_flipped_the_other_way),
        ("a favorability item left with no sign-flipped distractor",
         sign_flipped_distractor_removed),
        ("the stem's direction word flipped while the key stands", stem_sign_word_flipped),
        ("the value of RT changed in a stem while the key stands", rt_changed_in_a_stem),
        ("the sign of a free energy change flipped in a stem",
         logarithm_sign_flipped_in_a_stem),
        ("the exactly-zero item given a logarithm that is not zero",
         zero_item_given_a_direction),
        ("an estimation stem whose change is no longer small compared with RT",
         small_change_made_large),
        ("an estimation stem whose change is no longer many times RT",
         large_change_made_small),
        ("a comparison stem whose two processes are no longer favored",
         compared_processes_made_unfavored),
        ("the largest tabulated constant moved off the keyed reaction",
         constant_table_maximum_moved),
        ("the tabulated constant of exactly 1 replaced, so the boundary goes untested",
         boundary_row_removed),
        ("the most negative tabulated change moved off the keyed process",
         free_energy_table_corrupted),
        ("a second tabulated process tied for nearest to a constant of 1",
         nearest_to_one_tied),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h9_5, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

h9.no_figure_language(h9_5)
no_neighbouring_topics(h9_5)
sign_matches_k(h9_5)
h.run(h9_5, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
