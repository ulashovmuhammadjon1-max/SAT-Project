"""Unit 9 helpers: signed values, gas-mole bookkeeping, and the unit's equations.

The structural gate lives in ``cg_check.py`` and the Chemistry notation gate in
``h_check.py``. Neither is reimplemented here. What Unit 9 needs on top of them
is one thing those two cannot do: **a SIGN is the answer throughout this unit**,
and the shared machinery cannot tell one sign from the other.

WHY ``h_check.shows`` IS NOT ENOUGH FOR A SIGNED VALUE
------------------------------------------------------
``shows`` matches through ``cg_check.normalize``, which strips ``+`` and drops
punctuation. So ``normalize("+212 kJ/mol")`` and ``normalize("212 kJ/mol")``
are the same string, and ``"212 kJ/mol"`` matches INSIDE ``"-212 kJ/mol"``
because the hyphen in front is not an alphanumeric and so does not block the
lookbehind. A verifier asked to confirm that a key says ``+212`` would
therefore also accept ``-212`` -- precisely the defect this unit is most likely
to ship, since a thermodynamically favored process has a NEGATIVE
\\( \\Delta G^\\circ \\) and a POSITIVE cell potential and the two are easy to
write backwards.

``shows_signed`` compares RAW substrings instead, so ``+212`` and ``-212`` are
different tokens and neither contains the other. Its negative control is in
``selftest`` below: it asserts that a sign flip is caught, which is the whole
reason the function exists.

GAS-MOLE BOOKKEEPING
--------------------
EK 9.1.A.1's rule about moles of gas is countable, so a verifier does not have
to take the author's word for the sign of an entropy change -- it parses the
equation out of the stem and counts. The writing convention is the one
``h_equation.py`` already established for these banks:

    coefficient   a whole number then ONE space:     ``2 SO2(g)``
    separator     a plus with a space each side
    arrow         the word ``gives`` -- ``export_units.py`` does not typeset
                  Chemistry, so an arrow glyph would reach the student raw
    phase         ``(s) (l) (g) (aq)``, required on every species

NO ``\\b`` ANYWHERE, per the standing rule: a digit and a letter are both word
characters, so ``\\b`` is silently not a boundary exactly where it looks like
one.
"""
import re

# Faraday's constant, from the CED's own equation and constant sheet:
# "Faraday's constant, F = 96,485 coulombs / 1 mol e-".
FARADAY = 96485.0
# The gas constant, from the same sheet.
R_GAS = 8.314


# ------------------------------------------------------------------- signed keys

def shows_signed(item, token):
    """The keyed choice carries this exact signed token and no distractor does.

    RAW substring, deliberately. ``cg_check.normalize`` strips ``+`` and lets
    ``212`` match inside ``-212``, so a normalized check cannot tell a
    favorable answer from an unfavorable one. Every value in this unit whose
    SIGN is the point goes through here instead.
    """
    key = item["choices"][item["ans"]]
    assert token in key, (
        f"the signed token {token!r} is not in the keyed choice {key!r}"
    )
    also = [k for k, c in enumerate(item["choices"])
            if k != item["ans"] and token in c]
    assert not also, (
        f"the signed token {token!r} also appears in choice(s) {also}"
    )
    return token


def opposite_sign_offered(item, token):
    """Some distractor states the SIGN-FLIPPED value, so the item tests the sign.

    A sign question whose only wrong answers are different magnitudes does not
    actually ask the student which way round the convention runs.
    """
    assert token[0] in "+-", f"{token!r} does not begin with a sign"
    flipped = ("-" if token[0] == "+" else "+") + token[1:]
    also = [k for k, c in enumerate(item["choices"])
            if k != item["ans"] and flipped in c]
    assert also, (
        f"no distractor offers the sign-flipped {flipped!r}, so the item does not "
        f"test the sign of {token!r}"
    )
    return flipped


# ------------------------------------------------------- the sign convention

# "favored" sits inside "unfavored", so the lookbehind is what keeps the two
# apart: at the 'f' of "unfavored" the previous character is 'n', a letter, and
# the match is refused. A pattern written with \b would match both and the
# verdict would silently always read "favored".
_FAVORED = re.compile(r"(?<![A-Za-z])(un)?favou?red(?![A-Za-z])", re.I)


def favorability_verdict(text):
    """True if the text says favored, False if unfavored, None if unclear.

    A text saying both, or neither, returns None rather than guessing, so a
    caller has to handle that case deliberately instead of inheriting a
    default that happens to be right half the time.
    """
    found = {(m.group(1) or "").lower() for m in _FAVORED.finditer(text)}
    if found == {""}:
        return True
    if found == {"un"}:
        return False
    return None


# -------------------------------------------------------- gas-mole bookkeeping

_TERM = re.compile(r"^(?:(\d+)\s+)?([A-Z][A-Za-z0-9]*)\((s|l|g|aq)\)$")
_EQ_IN_STEM = re.compile(r"reaction\s+(.+?)\s*(?:,|\?|$)")


def _side_gas_moles(side):
    total = 0
    for term in side.split(" + "):
        m = _TERM.match(term.strip())
        assert m, f"cannot parse the term {term!r} in {side!r}"
        if m.group(3) == "g":
            total += int(m.group(1) or 1)
    return total


def equation_from(stem):
    """The chemical equation written in a stem, found after the word 'reaction'."""
    m = _EQ_IN_STEM.search(stem)
    assert m, f"no equation follows the word 'reaction' in {stem[:70]!r}"
    return m.group(1)


def delta_n_gas(equation):
    """Moles of gas-phase products minus moles of gas-phase reactants."""
    left, sep, right = equation.partition(" gives ")
    assert sep, f"no 'gives' separating the two sides of {equation!r}"
    return _side_gas_moles(right) - _side_gas_moles(left)


_SPECIES_TERM = re.compile(r"^(?:(\d+)\s+)?([A-Z][A-Za-z0-9]*\((?:s|l|g|aq)\))$")


def species_terms(equation):
    """``(reactants, products)``, each a list of ``(coefficient, species)``.

    The species string keeps its phase label, because that is how the tables in
    these modules label their rows -- H2O(l) and H2O(g) are two different rows
    with two different absolute entropies, and a lookup that dropped the phase
    would silently read the wrong one.
    """
    left, sep, right = equation.partition(" gives ")
    assert sep, f"no 'gives' separating the two sides of {equation!r}"

    def side(text):
        out = []
        for term in text.split(" + "):
            m = _SPECIES_TERM.match(term.strip())
            assert m, f"cannot parse the term {term!r} in {text!r}"
            out.append((int(m.group(1) or 1), m.group(2)))
        return out

    return side(left), side(right)


def summed(terms, value_of):
    """The coefficient-weighted sum of a per-species quantity over one side."""
    return sum(coeff * value_of(species) for coeff, species in terms)


# --------------------------------------------------------------- the equations

def gibbs(delta_h_kj, delta_s_j, t_kelvin):
    """EK 9.3.A.5: \\( \\Delta G^\\circ = \\Delta H^\\circ - T \\Delta S^\\circ \\).

    Enthalpy in kJ/mol, entropy in J/(mol K), temperature in kelvin; the result
    is in kJ/mol. The unit conversion lives HERE, written once, because a
    forgotten factor of a thousand is the other way this arithmetic goes wrong.
    """
    return delta_h_kj - t_kelvin * delta_s_j / 1000.0


def crossover_temperature(delta_h_kj, delta_s_j):
    """The temperature at which EK 9.3.A.5's expression changes sign."""
    assert delta_s_j != 0, "entropy change of zero: the expression never changes sign"
    return delta_h_kj * 1000.0 / delta_s_j


def delta_g_from_cell(n, e_volts):
    """EK 9.9.A.3: \\( \\Delta G^\\circ = -nFE^\\circ \\), in joules per mole."""
    return -n * FARADAY * e_volts


def cell_potential(e_cathode, e_anode):
    """EK 9.9.A.2: the reduction potential of the cathode less that of the anode."""
    return e_cathode - e_anode


def charge(current_amps, seconds):
    """EK 9.11.A.1's EQN: \\( I = q/t \\), rearranged for the charge."""
    return current_amps * seconds


def moles_of_electrons(coulombs):
    return coulombs / FARADAY


# ---------------------------------------------------------------- figure guard

FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"shown here|the graph|graph above|graph below|the cell shown|illustrated)"
    r"(?![a-z])", re.I)


def facing(item):
    """Every student-facing string on one question, including its table."""
    out = [item["q"], item["why"]] + list(item["choices"])
    t = item.get("table")
    if t:
        out += [str(x) for x in t["headers"]]
        out += [str(c) for r in t["rows"] for c in r]
    return out


def no_figure_language(module):
    """This bank carries no images, so nothing may point at one.

    9.8 is the reason this is shared across the unit: a galvanic cell is
    normally taught entirely from a drawing, and a stem saying "the cell shown"
    would reach a student with nothing behind it.
    """
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in facing(item):
            hit = FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, which this bank "
                f"cannot show -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: no item points at a picture.")


# ------------------------------------------------------------------- selftest

def _must_raise(label, fn):
    try:
        fn()
    except AssertionError as exc:
        print(f"  control OK  {label}: {str(exc)[:90]}")
        return
    raise SystemExit(f"CONTROL FAILED: {label} did not raise")


def selftest():
    """Negative controls for the helpers themselves.

    Every one of these mutations has been confirmed to violate the thing being
    asserted -- a control that cannot fail is worse than none, and this project
    has shipped one that could not.
    """
    print("h9_check helper controls:")

    key_pos = dict(choices=["A change of +212 kJ/mol", "A change of -212 kJ/mol",
                            "A change of +106 kJ/mol", "A change of -106 kJ/mol",
                            "No change at all"], ans=0)
    # Positive control first: the helper must ACCEPT the correct signed token.
    assert shows_signed(key_pos, "+212") == "+212"
    assert opposite_sign_offered(key_pos, "+212") == "-212"

    _must_raise("the sign of a keyed value flipped",
                lambda: shows_signed(key_pos, "-212"))
    _must_raise("a signed token absent from every choice",
                lambda: shows_signed(key_pos, "+999"))

    no_flip = dict(choices=["A change of +212 kJ/mol", "A change of +106 kJ/mol",
                            "A change of +53 kJ/mol", "A change of +424 kJ/mol",
                            "No change at all"], ans=0)
    _must_raise("an item offering no sign-flipped distractor",
                lambda: opposite_sign_offered(no_flip, "+212"))

    # The gas-mole parser. Positive control, then a corruption that must be seen.
    stem = ("For the reaction CaCO3(s) gives CaO(s) + CO2(g), what is the sign of the "
            "entropy change?")
    assert delta_n_gas(equation_from(stem)) == 1, "the parser miscounts a known equation"
    reverse = ("For the reaction CaO(s) + CO2(g) gives CaCO3(s), what is the sign of the "
               "entropy change?")
    assert delta_n_gas(equation_from(reverse)) == -1, "the parser miscounts the reverse"
    balanced = "For the reaction H2(g) + Cl2(g) gives 2 HCl(g), what happens?"
    assert delta_n_gas(equation_from(balanced)) == 0, "the parser miscounts equal sides"
    _must_raise("a species written without a phase label",
                lambda: delta_n_gas("CaCO3 gives CaO(s) + CO2(g)"))
    _must_raise("an equation with no 'gives'",
                lambda: delta_n_gas("CaCO3(s) + CaO(s)"))
    _must_raise("a stem with no equation after the word 'reaction'",
                lambda: equation_from("What is entropy?"))

    # The verdict reader. "favored" is a substring of "unfavored", so a reader
    # that got this wrong would report every unfavored process as favored --
    # the single most damaging error available in this unit.
    assert favorability_verdict("thermodynamically favored") is True
    assert favorability_verdict("thermodynamically unfavored") is False
    assert favorability_verdict("a process, favored under standard conditions") is True
    assert favorability_verdict("says nothing about it") is None, \
        "a text with no verdict must not be read as one"
    assert favorability_verdict("favored at low temperature and unfavored above it") is None, \
        "a text carrying both verdicts must not be read as either"

    # The species parser. The coefficient must be carried, and the phase label
    # must survive, or a lookup reads liquid water's entropy for the vapour.
    react, prod = species_terms("2 H2(g) + O2(g) gives 2 H2O(l)")
    assert react == [(2, "H2(g)"), (1, "O2(g)")], f"reactant side parsed as {react}"
    assert prod == [(2, "H2O(l)")], f"product side parsed as {prod}"
    table = {"H2(g)": 130.7, "O2(g)": 205.0, "H2O(l)": 69.9}
    assert abs(summed(react, table.__getitem__) - 466.4) < 1e-9, \
        "the coefficient-weighted sum is wrong"
    _must_raise("a coefficient written without its space",
                lambda: species_terms("2H2(g) gives H2(g) + H2(g)"))
    _must_raise("a species whose phase label is missing",
                lambda: species_terms("2 H2 + O2(g) gives 2 H2O(l)"))

    # The equations. Each positive control is a value computed by hand.
    assert abs(gibbs(-92.2, -198.8, 298) - (-92.2 + 298 * 0.1988)) < 1e-9
    assert abs(gibbs(0.0, 100.0, 1000.0) - (-100.0)) < 1e-9, \
        "the J-to-kJ conversion is wrong: 1000 K times 100 J/(mol K) is 100 kJ/mol"
    assert abs(crossover_temperature(30.0, 100.0) - 300.0) < 1e-9
    assert abs(delta_g_from_cell(2, 1.10) - (-2 * 96485.0 * 1.10)) < 1e-6
    assert delta_g_from_cell(2, 1.10) < 0, \
        "a positive cell potential must give a NEGATIVE free energy change"
    assert delta_g_from_cell(2, -0.50) > 0, \
        "a negative cell potential must give a POSITIVE free energy change"
    assert abs(cell_potential(0.34, -0.76) - 1.10) < 1e-9
    assert abs(charge(2.00, 965.0) - 1930.0) < 1e-9
    assert abs(moles_of_electrons(96485.0) - 1.0) < 1e-12
    _must_raise("a crossover temperature asked of a process with no entropy change",
                lambda: crossover_temperature(30.0, 0.0))

    print("h9_check helper controls all raised as required.")


if __name__ == "__main__":
    selftest()
