"""Key audit for AP CHEMISTRY 9.9 Cell Potential and Free Energy.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  9.9.A.1  a cell reaction is either thermodynamically favored, giving a positive
           voltage, or unfavored, giving a negative voltage and needing an
           externally applied potential      1, 2, 11, 14, 17, 22, 25, 26
  9.9.A.2  the standard cell potential is calculated by identifying the oxidation
           and reduction half-reactions and their respective standard reduction
           potentials                        3, 7, 8, 9, 10, 11, 29
  9.9.A.3  the standard free energy change is proportional to the NEGATIVE of the
           cell potential, so a positive standard potential means a favored
           reaction; EQN \\( \\Delta G^\\circ = -nFE^\\circ \\)
                                             4, 5, 6, 12, 13, 14, 15, 16, 17, 18,
                                             19, 20, 21, 23, 24, 25, 27, 29, 30
  the equation and constant sheet  n is the moles of electrons and Faraday's
           constant is 96,485 coulombs per mole of electrons     18, 27, 28

THE SIGN IS THE ANSWER, AND THE SHARED MACHINERY CANNOT SEE IT. ``cg_check``
compares through ``normalize``, which drops a leading ``+``; ``h9_check`` exists
because of that, and every signed value below goes through
``h9.shows_signed`` (a RAW substring, so ``+212`` and ``-212`` are different
tokens) and ``h9.opposite_sign_offered`` (some distractor must state the
sign-flipped value, or the item does not test the sign at all).

THE CONVENTION GUARD, which is the reason this verifier is longer than the topic
warrants. EK 9.9.A.3 ties three things together -- the sign of the potential, the
sign of the free energy change, and the verdict -- and getting any one of them
backwards is the defect this topic is most likely to ship. Three separate checks,
each with its own negative control:

  ``convention_guard``  for every item whose key states a signed quantity AND a
      verdict, the sign is read from the key, the verdict is read from the key,
      and they must agree with EK 9.9.A.3. The quantity (a potential or a free
      energy change) is DECLARED per item rather than guessed, because the two
      run opposite ways and a guess would be right half the time.
  ``choice_consistency``  for the items whose choices differ only in the pairing,
      the rule is applied to ALL FIVE choices and exactly the keyed one must
      survive. This derives the key from the framework instead of believing it.
  ``two_case_guard``  the summary item states both of EK 9.9.A.1's cases at once,
      so ``favorability_verdict`` cannot read it; its two clauses are checked
      directly, and the swapped version is the negative control.

THE FIGURE PROBLEM. A cell is normally taught from a drawing and this bank has no
images, so every cell is described in words or carried as a table of standard
reduction potentials. ``no_figure_language`` asserts nothing points at a picture.

SCOPE. 9.8 owns the naming of the electrodes, 9.10 owns nonstandard conditions
and the Nernst equation, and 9.11 owns Faraday's law as a stoichiometry. So no
item here mentions a reaction quotient, the Nernst equation, a current or a
charge in coulombs other than the constant in the framework's own equation.

NEGATIVE CONTROL: ``python3 verify_h9_9.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h9_check as h9

import h9_9

SRP = "Standard reduction potential (V)"
NCOL = "Moles of electrons transferred"
ECOL = "Standard cell potential (V)"

# The tabulated half-reactions, by the metal a stem names.
ROW = {
    "silver": "Ag+ + e- gives Ag(s)",
    "copper": "Cu2+ + 2 e- gives Cu(s)",
    "hydrogen": "2 H+ + 2 e- gives H2(g)",
    "nickel": "Ni2+ + 2 e- gives Ni(s)",
    "zinc": "Zn2+ + 2 e- gives Zn(s)",
    "magnesium": "Mg2+ + 2 e- gives Mg(s)",
}

# Explicit lookarounds, never \b: a digit and a letter are both word characters.
_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"shown here|the graph|graph above|graph below|the cell shown|illustrated)"
    r"(?![a-z])", re.I)

# 9.10 and 9.11's material. "coulombs" is allowed because the framework's own
# constant is quoted in coulombs; a coulomb of CHARGE PASSED is 9.11's, and that
# arrives with a current or a time, which are what is banned here.
#
# "seconds" is NOT in this list, and that is deliberate: the first draft banned
# it and the ban fired on "the first less the second" in a why -- the ordinal,
# not the unit. Same family as this project's \bpi and LETTER_REF own-goals. A
# time in seconds is caught by _ELAPSED_TIME below, which requires a number.
_OUT_OF_SCOPE = re.compile(
    r"(?<![A-Za-z])(nernst|reaction quotient|nonstandard|amperes?|electroplating|"
    r"current)(?![A-Za-z])", re.I)
_ELAPSED_TIME = re.compile(r"(?<![A-Za-z])\d+(?:\.\d+)?\s*seconds?(?![A-Za-z])", re.I)

# EK 9.9.A.3's two signed quantities, each read by the ADJECTIVE in front of it.
_E_SIGN_WORD = re.compile(
    r"(?<![a-z])(positive|negative)\s+(?:standard\s+)?(?:cell potential|voltage)"
    r"(?![a-z])", re.I)
_G_SIGN_WORD = re.compile(
    r"(?<![a-z])(positive|negative)\s+standard free energy change(?![a-z])", re.I)
# The same signs read off a numeric value instead, allowing for the closing
# delimiter of a hand-written math span between the number and its unit.
_E_SIGN_NUM = re.compile(r"([+-])\s*\d+(?:\.\d+)?\s*(?:\\\))?\s*V(?![A-Za-z])")
_G_SIGN_NUM = re.compile(r"([+-])\s*\d+(?:\.\d+)?\s*(?:\\\))?\s*kJ/mol(?![A-Za-z])")

_SIGN_NAME = {"+": "positive", "-": "negative"}


def _one(pattern, text, mapper=lambda s: s.lower()):
    """The single value ``pattern`` finds in ``text``, or None if 0 or 2+.

    None rather than a guess. A reader that silently picks one of two signs is
    right half the time and says so with confidence, which is the failure this
    whole verifier exists to prevent.
    """
    found = {mapper(m.group(1)) for m in pattern.finditer(text)}
    return found.pop() if len(found) == 1 else None


def sign_stated(text, kind):
    """"positive", "negative" or None, for a potential (``E``) or a free energy (``G``)."""
    assert kind in ("E", "G"), f"unknown quantity {kind!r}"
    word_pat = _E_SIGN_WORD if kind == "E" else _G_SIGN_WORD
    num_pat = _E_SIGN_NUM if kind == "E" else _G_SIGN_NUM
    by_word = _one(word_pat, text)
    by_num = _one(num_pat, text, mapper=lambda s: _SIGN_NAME[s])
    if by_word and by_num and by_word != by_num:
        return None
    return by_word or by_num


def favored_expected(sign, kind):
    """EK 9.9.A.3, written once: positive potential favored, negative free energy favored."""
    assert sign in ("positive", "negative"), f"unknown sign {sign!r}"
    is_potential = kind == "E"
    sign_is_positive = sign == "positive"
    # Named booleans rather than two parallel tuples compared by index -- the
    # shape that made a verifier in this repo reject a correct key.
    return sign_is_positive if is_potential else not sign_is_positive


# Which quantity each key states alongside its verdict. Declared, never guessed:
# a potential and a free energy change run opposite ways.
CONVENTION_ITEMS = {5: "G", 6: "G", 11: "E", 12: "G", 13: "G", 14: "G", 15: "G",
                    16: "E", 17: "E", 24: "G"}

# Items whose five choices differ only in the pairing EK 9.9.A.3 fixes, with the
# sign of the cell potential their STEM supplies.
PAIR_ITEMS = {5: "positive", 6: "negative"}

# Every signed value recomputed below, so the list of what is gated is visible.
SIGNED_ITEMS = (7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 24)


def convention_guard(module, claims, items=None):
    items = CONVENTION_ITEMS if items is None else items
    for i, kind in sorted(items.items()):
        item = module.QUESTIONS[i - 1]
        key = h.keyed(item)
        anchor = claims[i - 1][0]

        sign = sign_stated(key, kind)
        assert sign, (
            f"{module.TOPIC[0]} q{i}: the keyed choice states no single sign for its "
            f"{'potential' if kind == 'E' else 'free energy change'}: {key!r}"
        )
        verdict = h9.favorability_verdict(key)
        assert verdict is not None, (
            f"{module.TOPIC[0]} q{i}: the keyed choice states no single favorability "
            f"verdict: {key!r}"
        )
        want = favored_expected(sign, kind)
        assert verdict == want, (
            f"{module.TOPIC[0]} q{i}: the key pairs a {sign} "
            f"{'cell potential' if kind == 'E' else 'standard free energy change'} with a "
            f"{'favored' if verdict else 'unfavored'} verdict, which is EK 9.9.A.3 "
            f"backwards -- {key!r}"
        )
        # The anchor has to carry the sign too. An anchor of "212 kJ/mol,
        # thermodynamically favored" would match the sign-flipped distractor,
        # because normalize() drops a leading plus.
        anchor_sign = sign_stated(anchor, kind)
        assert anchor_sign == sign, (
            f"{module.TOPIC[0]} q{i}: the anchor states the sign {anchor_sign!r} where the "
            f"key states {sign!r}, so it does not pin it -- {anchor!r}"
        )
        assert h9.favorability_verdict(anchor) == verdict, (
            f"{module.TOPIC[0]} q{i}: the anchor does not carry the key's verdict -- "
            f"{anchor!r}"
        )
    print(f"OK  {module.TOPIC[0]} convention guard: {len(items)} keys pairing a signed "
          "quantity with a verdict, each agreeing with EK 9.9.A.3, each anchor carrying "
          "both.")


def choice_consistency(module, items=None):
    """Derive the key from EK 9.9.A.3 rather than believing it.

    For an item whose choices differ only in the pairing, the framework's rule is
    applied to all five choices and exactly the keyed one must survive.
    """
    items = PAIR_ITEMS if items is None else items
    for i, stem_sign in sorted(items.items()):
        item = module.QUESTIONS[i - 1]
        want_favored = favored_expected(stem_sign, "E")
        want_g_sign = "negative" if want_favored else "positive"
        survivors = []
        for k, choice in enumerate(item["choices"]):
            g_sign = sign_stated(choice, "G")
            verdict = h9.favorability_verdict(choice)
            if g_sign is None or verdict is None:
                continue
            if g_sign == want_g_sign and verdict == want_favored:
                survivors.append(k)
        assert survivors == [item["ans"]], (
            f"{module.TOPIC[0]} q{i}: a {stem_sign} standard cell potential admits choices "
            f"{survivors} under EK 9.9.A.3, but the key is {item['ans']}"
        )
    print(f"OK  {module.TOPIC[0]} choice consistency: {len(items)} item(s) whose key is "
          "derived from EK 9.9.A.3 and is the only surviving choice.")


# EK 9.9.A.1 states BOTH cases in one sentence, so favorability_verdict cannot
# read it. The two clauses are checked directly instead. "favored" sits inside
# "unfavored", so the lookbehind is what keeps them apart.
_CASE_FAVORED = re.compile(r"(?<!un)favored, giving a positive voltage", re.I)
_CASE_UNFAVORED = re.compile(r"(?<![a-z])unfavored, giving a negative voltage", re.I)
TWO_CASE_ITEM = 1


def two_case_guard(module, item_no=TWO_CASE_ITEM):
    key = h.keyed(module.QUESTIONS[item_no - 1])
    assert _CASE_FAVORED.search(key), (
        f"{module.TOPIC[0]} q{item_no}: the key does not pair favored with a POSITIVE "
        f"voltage, which is EK 9.9.A.1's first case -- {key!r}"
    )
    assert _CASE_UNFAVORED.search(key), (
        f"{module.TOPIC[0]} q{item_no}: the key does not pair unfavored with a NEGATIVE "
        f"voltage, which is EK 9.9.A.1's second case -- {key!r}"
    )
    print(f"OK  {module.TOPIC[0]} two-case guard: q{item_no}'s key states both halves of EK "
          "9.9.A.1 the way round the framework does.")


def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in h9.facing(item):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, which this bank "
                f"cannot show -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: no item points at a picture.")


def no_out_of_scope(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in h9.facing(item):
            hit = _OUT_OF_SCOPE.search(text) or _ELAPSED_TIME.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: mentions {hit.group(0)!r}, which belongs to 9.10 "
                f"or 9.11 -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: nothing nonstandard, no Nernst equation and no "
          "Faraday's-law current or time; the topic stays on standard potentials.")


# ------------------------------------------------------------------ arithmetic

def volts(x):
    return f"{x:+.2f}"


def kj(joules, places=0):
    return f"{joules / 1000.0:+.{places}f}"


def _ecell(table, reduced, oxidized):
    """EK 9.9.A.2: the tabulated reduction potential of the cathode less the anode's."""
    return h9.cell_potential(cg.cell(table, ROW[reduced], SRP),
                             cg.cell(table, ROW[oxidized], SRP))


def _signed(item, token):
    h9.shows_signed(item, token)
    h9.opposite_sign_offered(item, token)
    return token


def q7(table, item):
    e = _ecell(table, "copper", "zinc")
    assert abs(e - 1.10) < 1e-9, f"the tabulated Cu/Zn cell potential is {e}"
    _signed(item, volts(e))
    return (f"the tabulated reduction potentials give {cg.cell(table, ROW['copper'], SRP)} "
            f"less {cg.cell(table, ROW['zinc'], SRP)}, which is {volts(e)} V")


def q8(table, item):
    e = _ecell(table, "silver", "copper")
    assert abs(e - 0.46) < 1e-9, f"the tabulated Ag/Cu cell potential is {e}"
    _signed(item, volts(e))
    return (f"the tabulated silver potential less the tabulated copper potential is "
            f"{volts(e)} V, with no division by the moles of electrons")


def q9(table, item):
    e = _ecell(table, "nickel", "magnesium")
    assert abs(e - 2.12) < 1e-9, f"the tabulated Ni/Mg cell potential is {e}"
    _signed(item, volts(e))
    return (f"the tabulated nickel potential less the tabulated magnesium potential is "
            f"{volts(e)} V, a subtraction of signed values rather than a sum")


def q10(table, item):
    best, best_e = None, None
    for reduced in ROW:
        for oxidized in ROW:
            if reduced == oxidized:
                continue
            e = _ecell(table, reduced, oxidized)
            if best_e is None or e > best_e:
                best, best_e = (reduced, oxidized), e
    assert best == ("silver", "magnesium"), f"the largest tabulated pairing is {best}"
    ties = [(r, o) for r in ROW for o in ROW
            if r != o and abs(_ecell(table, r, o) - best_e) < 1e-12]
    assert ties == [best], f"the largest tabulated pairing is not unique: {ties}"
    h.shows(item, "Magnesium is oxidized and silver ion is reduced")
    return (f"searching every ordered pair of tabulated half-reactions maximises the "
            f"potential at {best_e:+.2f} V for {best}")


def q11(table, item):
    e = _ecell(table, "zinc", "copper")
    assert abs(e + 1.10) < 1e-9, f"the tabulated reversed cell potential is {e}"
    assert e < 0, "the reversed cell must have a NEGATIVE standard potential"
    _signed(item, volts(e))
    assert h9.favorability_verdict(h.keyed(item)) is False, (
        "a negative standard cell potential is EK 9.9.A.3's unfavored case"
    )
    return (f"exchanging which tabulated potential is subtracted gives {volts(e)} V, the "
            f"same magnitude with the opposite sign")


def q21(table, item):
    favored = [lab for lab, e in zip(cg.labels(table), cg.col(table, ECOL)) if e > 0]
    assert favored == ["Cell 1", "Cell 3"], f"the tabulated favored cells are {favored}"
    h.shows(item, "Cells 1 and 3")
    return (f"exactly the tabulated rows whose potential is above zero are {favored}, which "
            f"EK 9.9.A.3 makes the thermodynamically favored ones")


def q22(table, item):
    unfavored = [lab for lab, e in zip(cg.labels(table), cg.col(table, ECOL)) if e < 0]
    assert unfavored == ["Cell 2", "Cell 4"], f"the tabulated unfavored cells are {unfavored}"
    h.shows(item, "Cells 2 and 4")
    return (f"the tabulated rows whose potential is below zero are {unfavored}, the cells EK "
            f"9.9.A.1 says need an externally applied potential")


def q23(table, item):
    dg = {lab: h9.delta_g_from_cell(n, e)
          for lab, n, e in zip(cg.labels(table), cg.col(table, NCOL), cg.col(table, ECOL))}
    lowest = min(dg, key=dg.get)
    assert lowest == "Cell 1", f"the most negative tabulated free energy change is at {lowest}"
    ties = [lab for lab, v in dg.items() if abs(v - dg[lowest]) < 1e-9]
    assert ties == [lowest], f"the minimum is not unique: {ties}"
    h.shows(item, "Cell 1")
    return (f"applying EK 9.9.A.3's equation to both tabulated columns gives {dg}, whose "
            f"unique minimum is at {lowest}")


def q24(table, item):
    n = cg.cell(table, "Cell 3", NCOL)
    e = cg.cell(table, "Cell 3", ECOL)
    dg = h9.delta_g_from_cell(n, e)
    assert dg < 0, "a positive tabulated potential must give a NEGATIVE free energy change"
    _signed(item, kj(dg, 1))
    return (f"the tabulated {n:g} moles of electrons at {e:+.2f} V give {kj(dg, 1)} kJ/mol "
            f"by EK 9.9.A.3's equation")


TABLE_CHECKS = {7: q7, 8: q8, 9: q9, 10: q10, 11: q11,
                21: q21, 22: q22, 23: q23, 24: q24}


# Every stem-numeric check reads its numbers OUT OF THE STEM rather than
# carrying a copy of them, the convention verify_h9_5.py established. A hardcoded
# copy passes for ever after the stem it describes has been edited.
_POTENTIAL = re.compile(
    r"standard cell potential (?:of|is) ([+-]?\d+(?:\.\d+)?) V(?![A-Za-z])")
_FREE_ENERGY = re.compile(
    r"standard free energy change of ([+-]\d+(?:\.\d+)?) kJ/mol(?![A-Za-z])")
_MOLES_E = re.compile(r"transfers (\d+) moles? of electrons(?![A-Za-z])")


def _only(pattern, text, what):
    hits = pattern.findall(text)
    assert len(hits) == 1, f"expected exactly one {what} in the stem, found {hits}"
    return float(hits[0])


def _all(pattern, text, what, count):
    hits = pattern.findall(text)
    assert len(hits) == count, f"expected {count} of the {what} in the stem, found {hits}"
    return [float(x) for x in hits]


def _dg_from_stem(item, places):
    """EK 9.9.A.3's equation applied to the moles of electrons and potential in the stem."""
    n = _only(_MOLES_E, item["q"], "number of moles of electrons")
    e = _only(_POTENTIAL, item["q"], "standard cell potential")
    dg = h9.delta_g_from_cell(n, e)
    # The SIGN, asserted explicitly and not merely implied by the magnitude.
    potential_is_positive = e > 0
    change_is_negative = dg < 0
    assert potential_is_positive == change_is_negative, (
        f"a {'positive' if potential_is_positive else 'negative'} potential must give a "
        f"{'negative' if potential_is_positive else 'positive'} free energy change, but the "
        f"equation returned {dg:+g} J/mol"
    )
    token = _signed(item, kj(dg, places))
    return n, e, dg, token


def n12(item):
    n, e, dg, token = _dg_from_stem(item, 0)
    return (f"the stem's {n:g} moles of electrons at {e:+g} V give {token} kJ/mol under EK "
            f"9.9.A.3's equation")


def n13(item):
    n, e, dg, token = _dg_from_stem(item, 1)
    assert n == 1, f"the stem states {n:g} moles of electrons, not one"
    return (f"the stem's single mole of electrons at {e:+g} V gives {token} kJ/mol, half "
            f"what two moles would give")


def n14(item):
    n, e, dg, token = _dg_from_stem(item, 1)
    assert e < 0 and dg > 0, f"the stem's potential {e:+g} V must give a positive change"
    return (f"the stem's {n:g} moles of electrons at {e:+g} V give {token} kJ/mol, the "
            f"thermodynamically unfavored case of EK 9.9.A.1")


def n15(item):
    n, e, dg, token = _dg_from_stem(item, 0)
    assert n == 4, f"the stem states {n:g} moles of electrons, not four"
    return (f"the stem's {n:g} moles of electrons at {e:+g} V give {token} kJ/mol; the "
            f"moles of electrons multiply rather than divide")


def _e_from_stem(item):
    n = _only(_MOLES_E, item["q"], "number of moles of electrons")
    dg = _only(_FREE_ENERGY, item["q"], "standard free energy change") * 1000.0
    e = -dg / (n * h9.FARADAY)
    change_is_negative = dg < 0
    potential_is_positive = e > 0
    assert change_is_negative == potential_is_positive, (
        f"a {'negative' if change_is_negative else 'positive'} free energy change must give "
        f"a {'positive' if change_is_negative else 'negative'} potential, but the "
        f"rearrangement returned {e:+g} V"
    )
    token = _signed(item, volts(e))
    return n, dg, e, token


def n16(item):
    n, dg, e, token = _e_from_stem(item)
    assert dg < 0 and e > 0, f"the stem's change {dg:+g} J/mol must give a positive potential"
    return (f"the stem's {dg / 1000:+g} kJ/mol over {n:g} moles of electrons and Faraday's "
            f"constant recomputes the potential as {token} V")


def n17(item):
    n, dg, e, token = _e_from_stem(item)
    assert dg > 0 and e < 0, f"the stem's change {dg:+g} J/mol must give a negative potential"
    return (f"the stem's {dg / 1000:+g} kJ/mol over {n:g} mole of electrons recomputes the "
            f"potential as {token} V, which EK 9.9.A.1 says needs an external supply")


def n18(item):
    e = _only(_POTENTIAL, item["q"], "standard cell potential")
    dg = _only(_FREE_ENERGY, item["q"], "standard free energy change") * 1000.0
    n = -dg / (h9.FARADAY * e)
    assert abs(n - round(n)) < 0.05, f"the recomputed moles of electrons are {n}, not whole"
    assert round(n) == 2, f"the recomputed moles of electrons are {round(n)}"
    h.shows(item, "2 moles of electrons")
    return (f"the stem's {dg / 1000:+g} kJ/mol divided by Faraday's constant times {e:+g} V "
            f"returns {n:.2f} moles of electrons")


def n19(item):
    e = _only(_POTENTIAL, item["q"], "standard cell potential")
    ns = _all(_MOLES_E, item["q"], "numbers of moles of electrons", 2)
    first, second = (h9.delta_g_from_cell(n, e) for n in ns)
    assert abs(second / first - ns[1] / ns[0]) < 1e-9, (
        f"the two changes {first}, {second} are not in the ratio of the stem's {ns}"
    )
    assert first < 0 and second < 0, "a positive potential must give negative changes"
    token = _signed(item, kj(second, 0))
    return (f"the stem's {ns[1]:g} moles of electrons at {e:+g} V give {token} kJ/mol "
            f"against {kj(first, 1)} kJ/mol for {ns[0]:g}, exactly twice the magnitude")


NUMERIC = {12: n12, 13: n13, 14: n14, 15: n15, 16: n16, 17: n17, 18: n18, 19: n19}


CLAIMS = [
 ("thermodynamically favored, giving a positive voltage, or thermodynamically unfavored, giving a negative voltage",
  "EK 9.9.A.1 verbatim in substance: the reactions are either thermodynamically favored, resulting in a positive voltage, or unfavored, resulting in a negative voltage."),
 ("An externally applied potential",
  "EK 9.9.A.1 attaches to the unfavored case the words requiring an externally applied potential for the reaction to proceed, which EK 9.8.A.2 makes the electrolytic cell."),
 ("identifying the oxidation and reduction half-reactions and their respective standard reduction potentials",
  "EK 9.9.A.2 verbatim: the standard cell potential can be calculated by identifying the half-reactions and their respective standard reduction potentials."),
 ("\\Delta G^\\circ = -nFE^\\circ",
  "EK 9.9.A.3's EQN, with the negative sign that makes the free energy change proportional to the NEGATIVE of the cell potential."),
 ("thermodynamically favored, with a negative standard free energy change",
  "EK 9.9.A.3: a cell with a positive standard potential involves a favored reaction, and the negative sign in its equation puts the free energy change below zero."),
 ("thermodynamically unfavored, with a positive standard free energy change",
  "EK 9.9.A.3's other case: a negative standard potential means an unfavored reaction, and the equation turns it into a free energy change above zero."),
 ("+1.10",
  "EK 9.9.A.2's subtraction applied to the tabulated copper and zinc potentials. q7 recomputes it and h9.shows_signed compares the token raw, so the sign cannot slip."),
 ("+0.46",
  "EK 9.9.A.2 again, for the tabulated silver and copper potentials; a half-reaction potential is not divided by its number of electrons. q8 recomputes it."),
 ("+2.12",
  "EK 9.9.A.2 for the tabulated nickel and magnesium potentials, subtracting signed values rather than adding magnitudes. q9 recomputes it."),
 ("Magnesium is oxidized and silver ion is reduced",
  "EK 9.9.A.2 makes the potential the cathode's less the anode's, so it is largest for the highest tabulated potential over the lowest. q10 searches every ordered pair."),
 ("-1.10 \\) V, so the reaction is thermodynamically unfavored",
  "Reversing the cell exchanges the subtraction under EK 9.9.A.2, and EK 9.9.A.3 makes a negative standard potential the unfavored case. q11 recomputes both."),
 ("-212 \\) kJ/mol, thermodynamically favored",
  "EK 9.9.A.3's equation for two moles of electrons at +1.10 V, with the negative sign in front. n12 recomputes it and checks the sign explicitly."),
 ("-77.2 \\) kJ/mol, thermodynamically favored",
  "EK 9.9.A.3's equation for one mole of electrons at +0.80 V; using two moles is what doubles the magnitude. n13 recomputes it."),
 ("+96.5 \\) kJ/mol, thermodynamically unfavored",
  "EK 9.9.A.3's negative sign turns a negative standard potential into a positive free energy change, which EK 9.9.A.1 calls the unfavored case. n14 recomputes it."),
 ("-154 \\) kJ/mol, thermodynamically favored",
  "EK 9.9.A.3's equation scales with the moles of electrons, so four of them at +0.40 V still give a large negative change. n15 recomputes it."),
 ("+1.00 \\) V, so the cell is thermodynamically favored",
  "EK 9.9.A.3's equation rearranged: the free energy change over the moles of electrons and Faraday's constant, with the sign reversed. n16 recomputes it."),
 ("-1.00 \\) V, so the cell is thermodynamically unfavored",
  "The same rearrangement carrying the sign the other way, and EK 9.9.A.1's requirement of an externally applied potential. n17 recomputes it."),
 ("2 moles of electrons",
  "EK 9.9.A.3's equation contains only n, Faraday's constant and the potential, so two of them fix the third. n18 recomputes n and checks it is a whole number."),
 ("-193 \\) kJ/mol, twice as large in magnitude",
  "EK 9.9.A.3's proportionality to the moles of electrons: doubling n at a fixed potential doubles the magnitude and leaves the sign alone. n19 recomputes both cells."),
 ("always carry opposite signs, and the size of one fixes the size of the other",
  "EK 9.9.A.3 puts a negative sign in front of a product of positive quantities, so the free energy change and the potential can never share a sign."),
 ("Cells 1 and 3",
  "EK 9.9.A.3 makes a positive standard potential the favored case. q21 reads the tabulated potentials and checks exactly those two are above zero."),
 ("Cells 2 and 4",
  "EK 9.9.A.1 attaches the externally applied potential to the unfavored case. q22 checks exactly those two tabulated potentials are below zero."),
 ("Cell 1",
  "EK 9.9.A.3's equation uses both tabulated columns, so the comparison is a product and not the potential alone. q23 recomputes every row and checks the minimum is unique."),
 ("-88.8 \\) kJ/mol, thermodynamically favored",
  "EK 9.9.A.3's equation applied to that row's tabulated moles of electrons and potential. q24 recomputes it from the table alone."),
 ("Zero, since the equation multiplies the potential by the other factors",
  "EK 9.9.A.3's equation is a product with the potential as one factor, so a potential of zero gives zero whatever n is, and neither of the framework's two cases applies."),
 ("Both are thermodynamically favored, and the second has the more negative free energy change",
  "EK 9.9.A.3 attaches no threshold to a positive potential, and its equation makes the free energy change more negative as the potential grows at fixed n."),
 ("the number of moles of electrons transferred in the reaction",
  "The framework's equation and constant sheet defines n as the number of moles of electrons, which EK 9.9.A.3's equation multiplies by Faraday's constant and the potential."),
 ("The charge on one mole of electrons, 96,485 coulombs",
  "The equation and constant sheet gives Faraday's constant as 96,485 coulombs per one mole of electrons, which turns moles of electrons into a charge."),
 ("the standard cell potential follows from them and its sign settles the question",
  "EK 9.9.A.2 calculates the potential from the half-reactions and EK 9.9.A.3 makes its sign decide the favorability; n scales the free energy change but not its sign."),
 ("A positive standard cell potential, a negative standard free energy change, and a thermodynamically favored reaction",
  "EK 9.9.A.3 ties all three in one sentence, so any set giving the two quantities the same sign, or the wrong verdict, contradicts it."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the cell shown, which of the two cases applies?"
        no_figure_language(mod)

    def nernst_creeps_in(mod, cl):
        mod.QUESTIONS[0]["why"] = (mod.QUESTIONS[0]["why"]
                                   + " Use the Nernst equation to see it.")
        no_out_of_scope(mod)

    def current_creeps_in(mod, cl):
        mod.QUESTIONS[1]["q"] = mod.QUESTIONS[1]["q"] + " A current of 2 amperes flows."
        no_out_of_scope(mod)

    def verdict_flipped_on_a_signed_key(mod, cl):
        # q12's key states -212 kJ/mol, which EK 9.9.A.3 makes the FAVORED case.
        # The value and every structural property are untouched; only the
        # verdict is turned round, so nothing but the convention guard can see it.
        ch = list(mod.QUESTIONS[11]["choices"])
        ch[0] = "\\( -212 \\) kJ/mol, thermodynamically unfavored"
        ch[1] = "\\( +212 \\) kJ/mol, thermodynamically favored"
        mod.QUESTIONS[11]["choices"] = ch
        cl[11] = ("-212 \\) kJ/mol, thermodynamically unfavored", cl[11][1])
        convention_guard(mod, cl)

    def sign_flipped_on_a_potential_key(mod, cl):
        # q16's key states +1.00 V with a favored verdict. Flipping the sign
        # alone makes the pairing contradict EK 9.9.A.3.
        ch = list(mod.QUESTIONS[15]["choices"])
        ch[0] = "\\( -1.00 \\) V, so the cell is thermodynamically favored"
        ch[1] = "\\( +1.00 \\) V, so the cell is thermodynamically unfavored"
        mod.QUESTIONS[15]["choices"] = ch
        cl[15] = ("-1.00 \\) V, so the cell is thermodynamically favored", cl[15][1])
        convention_guard(mod, cl)

    def quantity_declared_wrongly(mod, cl):
        # The module is untouched; the guard is told q12's key states a
        # POTENTIAL. A -212 with a favored verdict is right for a free energy
        # change and wrong for a potential, so the declaration is what fails.
        items = dict(CONVENTION_ITEMS)
        items[12] = "E"
        convention_guard(mod, cl, items=items)

    def anchor_drops_the_sign(mod, cl):
        cl[11] = ("212 \\) kJ/mol, thermodynamically favored", cl[11][1])
        convention_guard(mod, cl)

    def anchor_drops_the_verdict(mod, cl):
        cl[11] = ("-212 \\) kJ/mol", cl[11][1])
        convention_guard(mod, cl)

    def pairing_key_moved(mod, cl):
        # q5's stem gives a POSITIVE potential. Moving the key onto the choice
        # pairing favored with a POSITIVE free energy change leaves the item
        # structurally sound and contradicts EK 9.9.A.3.
        mod.QUESTIONS[4]["ans"] = 2
        choice_consistency(mod)

    def stem_sign_changed_under_a_correct_key(mod, cl):
        items = dict(PAIR_ITEMS)
        items[5] = "negative"
        choice_consistency(mod, items=items)

    def two_cases_swapped(mod, cl):
        ch = list(mod.QUESTIONS[0]["choices"])
        ch[0] = ("It is thermodynamically favored, giving a negative voltage, or "
                 "thermodynamically unfavored, giving a positive voltage")
        ch[1] = "It is thermodynamically favored, giving a positive voltage, and no other case"
        mod.QUESTIONS[0]["choices"] = ch
        two_case_guard(mod)

    def tabulated_potential_changed(mod, cl):
        mod.QUESTIONS[6]["table"] = dict(
            headers=h9_9._T_SRP["headers"],
            rows=[["Ag+ + e- gives Ag(s)", "+0.80"],
                  ["Cu2+ + 2 e- gives Cu(s)", "+0.50"],
                  ["2 H+ + 2 e- gives H2(g)", "0.00"],
                  ["Ni2+ + 2 e- gives Ni(s)", "-0.25"],
                  ["Zn2+ + 2 e- gives Zn(s)", "-0.76"],
                  ["Mg2+ + 2 e- gives Mg(s)", "-2.37"]])

    def largest_pairing_moved(mod, cl):
        mod.QUESTIONS[9]["table"] = dict(
            headers=h9_9._T_SRP["headers"],
            rows=[["Ag+ + e- gives Ag(s)", "+0.80"],
                  ["Cu2+ + 2 e- gives Cu(s)", "+2.90"],
                  ["2 H+ + 2 e- gives H2(g)", "0.00"],
                  ["Ni2+ + 2 e- gives Ni(s)", "-0.25"],
                  ["Zn2+ + 2 e- gives Zn(s)", "-0.76"],
                  ["Mg2+ + 2 e- gives Mg(s)", "-2.37"]])

    def reversed_cell_made_favorable(mod, cl):
        mod.QUESTIONS[10]["table"] = dict(
            headers=h9_9._T_SRP["headers"],
            rows=[["Ag+ + e- gives Ag(s)", "+0.80"],
                  ["Cu2+ + 2 e- gives Cu(s)", "-1.50"],
                  ["2 H+ + 2 e- gives H2(g)", "0.00"],
                  ["Ni2+ + 2 e- gives Ni(s)", "-0.25"],
                  ["Zn2+ + 2 e- gives Zn(s)", "-0.76"],
                  ["Mg2+ + 2 e- gives Mg(s)", "-2.37"]])

    def tabulated_cell_sign_flipped(mod, cl):
        mod.QUESTIONS[20]["table"] = dict(
            headers=h9_9._T_CELLS["headers"],
            rows=[["Cell 1", "2", "+1.10"], ["Cell 2", "1", "+0.44"],
                  ["Cell 3", "2", "+0.46"], ["Cell 4", "4", "-0.20"]])

    def tabulated_electrons_changed(mod, cl):
        mod.QUESTIONS[22]["table"] = dict(
            headers=h9_9._T_CELLS["headers"],
            rows=[["Cell 1", "1", "+1.10"], ["Cell 2", "1", "-0.44"],
                  ["Cell 3", "6", "+0.46"], ["Cell 4", "4", "-0.20"]])

    def stem_potential_changed(mod, cl):
        # Proves the free energy check really READS the stem rather than
        # carrying a copy of its numbers: the key is untouched and only the
        # stated potential moves.
        mod.QUESTIONS[11]["q"] = mod.QUESTIONS[11]["q"].replace(
            "standard cell potential of +1.10 V", "standard cell potential of +1.20 V")

    def stem_electron_count_changed(mod, cl):
        mod.QUESTIONS[14]["q"] = mod.QUESTIONS[14]["q"].replace(
            "transfers 4 moles of electrons", "transfers 2 moles of electrons")

    def stem_free_energy_sign_flipped(mod, cl):
        mod.QUESTIONS[15]["q"] = mod.QUESTIONS[15]["q"].replace(
            "standard free energy change of -193 kJ/mol",
            "standard free energy change of +193 kJ/mol")

    def stem_electron_counts_made_equal(mod, cl):
        mod.QUESTIONS[18]["q"] = mod.QUESTIONS[18]["q"].replace(
            "the second transfers 4 moles of electrons",
            "the second transfers 2 moles of electrons")

    def tabulated_row_rescaled(mod, cl):
        mod.QUESTIONS[23]["table"] = dict(
            headers=h9_9._T_CELLS["headers"],
            rows=[["Cell 1", "2", "+1.10"], ["Cell 2", "1", "-0.44"],
                  ["Cell 3", "4", "+0.46"], ["Cell 4", "4", "-0.20"]])

    return [
        ("a stem pointing at a cell the bank cannot show", figure_language),
        ("the Nernst equation, which is 9.10's material", nernst_creeps_in),
        ("a current in amperes, which is 9.11's material", current_creeps_in),
        ("a signed key whose verdict was turned round against EK 9.9.A.3",
         verdict_flipped_on_a_signed_key),
        ("a potential key whose sign was flipped under an unchanged verdict",
         sign_flipped_on_a_potential_key),
        ("a free energy key declared to the guard as a potential",
         quantity_declared_wrongly),
        ("an anchor on a signed value written without its sign", anchor_drops_the_sign),
        ("an anchor that carries the value but not the verdict", anchor_drops_the_verdict),
        ("the key moved onto the choice EK 9.9.A.3 rules out", pairing_key_moved),
        ("the stem's potential sign changed under a correct key",
         stem_sign_changed_under_a_correct_key),
        ("EK 9.9.A.1's two cases stated the wrong way round", two_cases_swapped),
        ("a tabulated reduction potential changed under a keyed cell potential",
         tabulated_potential_changed),
        ("a tabulated potential raised so another pairing is the largest",
         largest_pairing_moved),
        ("the tabulated potentials changed so the reversed cell is favorable",
         reversed_cell_made_favorable),
        ("a tabulated cell potential made positive under a keyed favored pair",
         tabulated_cell_sign_flipped),
        ("the tabulated moles of electrons changed under a keyed ranking",
         tabulated_electrons_changed),
        ("a tabulated row rescaled under a keyed free energy change",
         tabulated_row_rescaled),
        ("the stem's potential changed under an unchanged keyed free energy change",
         stem_potential_changed),
        ("the stem's moles of electrons halved under an unchanged key",
         stem_electron_count_changed),
        ("the stem's free energy change sign-flipped under a keyed positive potential",
         stem_free_energy_sign_flipped),
        ("the stem's two electron counts made equal under a keyed doubling",
         stem_electron_counts_made_equal),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h9_9, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h9_9)
no_out_of_scope(h9_9)
two_case_guard(h9_9)
convention_guard(h9_9, CLAIMS)
choice_consistency(h9_9)
h.run(h9_9, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
