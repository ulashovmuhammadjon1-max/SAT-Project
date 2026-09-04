"""Key audit for AP CHEMISTRY 9.11 Electrolysis and Faraday's Law.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  9.11.A.1     Faraday's laws determine the stoichiometry of the cell reaction
               with respect to the electrons transferred, the mass deposited on
               or removed from an electrode, the current, the time elapsed and
               the charge of the ionic species; EQN \\( I = \\frac{q}{t} \\)
                        1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                        18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30
  constant sheet  Faraday's constant is 96,485 coulombs per one mole of
               electrons                4, 8, 9, 10, 11, 12, 15, 16, 23, 27, 30
  9.8.A.3      oxidation at the anode and reduction at the cathode, which
               decides which electrode gains mass and which loses it   17, 18
  9.9.A.1      an unfavored reaction gives a negative voltage and needs an
               externally applied potential                            29

EVERY NUMBER IS RECOMPUTED FROM THE STEM, NOT FROM A COPY OF IT. Each check
parses its own current, time, charge, half-reaction and molar mass out of the
question it is checking, the convention verify_h9_5.py established, and then
rebuilds the keyed value to three significant figures. A check holding its own
copy of a stem's numbers goes on passing after the stem has been edited, which
is the quiet failure this project has paid for elsewhere.

THE SIGN, WHERE THE SIGN IS THE ANSWER. EK 9.11.A.1.ii names mass DEPOSITED ON
or REMOVED FROM an electrode, so the two electrodes carry opposite signs and
writing them the wrong way round is the defect this topic can ship. Two guards:

  ``electrode_sign_guard``  the signed item's key must put the PLUS at the
      cathode and the MINUS at the anode, and the worded item's key must say the
      cathode gains and the anode loses. Both are checked for the presence of the
      right pairing AND the absence of the reversed one, because a key naming
      both would satisfy a presence test alone.
  ``driven_sign_guard``     the one item linking to EK 9.9.A.1 reads the
      magnitude out of its own stem, builds the NEGATIVE token from it, and
      requires the key to carry that token and the unfavored verdict, with the
      sign-flipped value offered as a distractor. The comparison is raw, because
      ``cg_check.normalize`` drops a leading plus and would let ``+1.23`` match
      inside ``-1.23``.

SCOPE. 9.8 owns the physical components, 9.9 the standard cell potential and its
arithmetic, 9.10 nonstandard conditions. ``no_stray_voltage`` asserts that no
item except the one that owns the link states a potential in volts.

THE FIGURE PROBLEM. This bank carries no images, so nothing points at one.

NEGATIVE CONTROL: ``python3 verify_h9_11.py --selftest``.
"""
import math
import re
import sys

import cg_check as cg
import h_check as h
import h9_check as h9

import h9_11

ICOL = "Current (A)"
TCOL = "Time (s)"
HALF = "Half-reaction at the cathode"
MCOL = "Molar mass (g/mol)"

# Explicit lookarounds, never \b: a digit and a letter are both word characters.
_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"shown here|the graph|graph above|graph below|the cell shown|illustrated)"
    r"(?![a-z])", re.I)

_VOLTAGE = re.compile(r"(?<![A-Za-z])[+-]?\d+(?:\.\d+)?\s*(?:\\\)\s*)?(?:V|volts?)(?![A-Za-z])")
# The single item that owns the link to EK 9.9.A.1 and may therefore state a
# potential. Every other item is scope-checked against it.
VOLTAGE_ITEM = 29


def sig(x, digits=3):
    """``x`` written to ``digits`` significant figures, as the choices write it.

    Trailing zeros are KEPT -- "5.00 A" and "0.200 mol" are how a three-figure
    answer is written, and ``:g`` would strip them and stop matching the key.
    """
    assert x > 0, f"this helper is for magnitudes; got {x}"
    places = digits - 1 - math.floor(math.log10(abs(x)))
    value = round(x, places)
    return f"{value:.0f}" if places <= 0 else f"{value:.{places}f}"


# ------------------------------------------------------------- stem arithmetic

_CURRENT = re.compile(r"(\d+(?:\.\d+)?) A(?![A-Za-z])")
_TIME = re.compile(r"(\d+(?:\.\d+)?) s(?![A-Za-z])")
_CHARGE = re.compile(r"(\d+(?:\.\d+)?) C(?![A-Za-z])")
_MOL_E = re.compile(r"(\d+(?:\.\d+)?) mol of electrons(?![A-Za-z])")
_MOL_METAL = re.compile(
    r"(\d+(?:\.\d+)?) mol of (?:copper|silver|aluminium|zinc|nickel)(?![A-Za-z])")
_MOLAR_MASS = re.compile(r"molar mass of [a-z]+ (?:is|as) (\d+(?:\.\d+)?) g/mol")
# "Ag+(aq) + e- gives" has no coefficient, which means one electron. The group is
# optional rather than absent so both spellings parse through one pattern.
_ELECTRONS = re.compile(r"\+ (\d*) ?e- gives")
_MAGNITUDE_V = re.compile(r"magnitude of the standard cell potential[^.]*? is "
                          r"(\d+(?:\.\d+)?) V(?![A-Za-z])")


def _only(pattern, text, what):
    hits = pattern.findall(text)
    assert len(hits) == 1, f"expected exactly one {what} in the stem, found {hits}"
    return hits[0]


def _num(pattern, text, what):
    return float(_only(pattern, text, what))


def _electrons(text, what="half-reaction"):
    raw = _only(_ELECTRONS, text, what)
    n = int(raw) if raw else 1
    assert 1 <= n <= 4, f"an implausible {n} electrons per ion in {text[:60]!r}"
    return n


def charge_from_current(item):
    i = _num(_CURRENT, item["q"], "current")
    t = _num(_TIME, item["q"], "time elapsed")
    q = h9.charge(i, t)
    h.shows(item, f"{sig(q)} C")
    return (f"the stem's {i:g} A for {t:g} s gives {sig(q)} C by the framework's own "
            f"equation for the current")


def time_from_charge(item):
    q = _num(_CHARGE, item["q"], "charge")
    i = _num(_CURRENT, item["q"], "current")
    t = q / i
    h.shows(item, f"{sig(t)} s")
    return (f"the stem's {q:g} C at {i:g} A gives {sig(t)} s, the framework's equation "
            f"rearranged for the time elapsed")


def current_from_charge(item):
    q = _num(_CHARGE, item["q"], "charge")
    t = _num(_TIME, item["q"], "time elapsed")
    i = q / t
    h.shows(item, f"{sig(i)} A")
    return (f"the stem's {q:g} C in {t:g} s gives {sig(i)} A, which is the framework's "
            f"equation applied directly")


def moles_from_charge(item):
    q = _num(_CHARGE, item["q"], "charge")
    n = h9.moles_of_electrons(q)
    h.shows(item, f"{sig(n)} mol")
    return (f"the stem's {q:g} C divided by Faraday's constant gives {sig(n)} mol of "
            f"electrons")


def charge_from_moles(item):
    n = _num(_MOL_E, item["q"], "number of moles of electrons")
    q = n * h9.FARADAY
    h.shows(item, f"{sig(q)} C")
    return (f"the stem's {n:g} mol of electrons times Faraday's constant gives {sig(q)} C")


def _mass_from_charge(item):
    q = _num(_CHARGE, item["q"], "charge")
    z = _electrons(item["q"])
    mm = _num(_MOLAR_MASS, item["q"], "molar mass")
    moles_e = h9.moles_of_electrons(q)
    return q, z, mm, moles_e, moles_e / z * mm


def mass_deposited(item):
    q, z, mm, moles_e, mass = _mass_from_charge(item)
    h.shows(item, f"{sig(mass)} g")
    return (f"the stem's {q:g} C gives {moles_e:.4g} mol of electrons, which the stem's "
            f"{z} electron(s) per ion and {mm:g} g/mol turn into {sig(mass)} g")


def moles_of_metal(item):
    moles_e = _num(_MOL_E, item["q"], "number of moles of electrons")
    z = _electrons(item["q"])
    moles = moles_e / z
    h.shows(item, f"{sig(moles)} mol")
    return (f"the stem's {moles_e:g} mol of electrons over the {z} electrons per ion in its "
            f"half-reaction gives {sig(moles)} mol of metal")


def time_for_amount(item):
    moles = _num(_MOL_METAL, item["q"], "amount of metal")
    z = _electrons(item["q"])
    i = _num(_CURRENT, item["q"], "current")
    t = moles * z * h9.FARADAY / i
    h.shows(item, f"{sig(t)} s")
    return (f"the stem's {moles:g} mol at {z} electrons per ion is {moles * z:g} mol of "
            f"electrons, or {moles * z * h9.FARADAY:.0f} C, which at {i:g} A takes "
            f"{sig(t)} s")


def current_for_amount(item):
    moles = _num(_MOL_METAL, item["q"], "amount of metal")
    z = _electrons(item["q"])
    t = _num(_TIME, item["q"], "time elapsed")
    i = moles * z * h9.FARADAY / t
    h.shows(item, f"{sig(i)} A")
    return (f"the stem's {moles:g} mol at {z} electrons per ion is "
            f"{moles * z * h9.FARADAY:.0f} C, which in {t:g} s needs {sig(i)} A")


def signed_electrode_masses(item):
    """EK 9.11.A.1.ii: the same magnitude deposited at one electrode and removed
    from the other, so the two changes are opposite in SIGN."""
    q, z, mm, moles_e, mass = _mass_from_charge(item)
    token = f"+{sig(mass)} \\) g at the cathode"
    h9.shows_signed(item, token)
    flipped = h9.opposite_sign_offered(item, token)
    return (f"the stem's {q:g} C and {z} electrons per ion deposit {sig(mass)} g, so the "
            f"cathode gains it and the anode loses it; {flipped!r} is offered as the "
            f"reversed distractor")


NUMERIC = {5: charge_from_current, 6: time_from_charge, 7: current_from_charge,
           8: moles_from_charge, 9: charge_from_moles,
           10: mass_deposited, 11: mass_deposited, 12: mass_deposited,
           13: moles_of_metal, 15: time_for_amount, 16: current_for_amount,
           17: signed_electrode_masses}


# ------------------------------------------------------------------ table items

def _run_charges(table):
    return {lab: h9.charge(i, t) for lab, i, t in
            zip(cg.labels(table), cg.col(table, ICOL), cg.col(table, TCOL))}


def q19(table, item):
    charges = _run_charges(table)
    q = charges["Run 1"]
    h.shows(item, f"{sig(q)} C")
    return (f"the tabulated current and time for that run multiply to {sig(q)} C; the four "
            f"tabulated charges are {charges}")


def q20(table, item):
    charges = _run_charges(table)
    biggest = max(charges, key=charges.get)
    ties = [lab for lab, c in charges.items() if abs(c - charges[biggest]) < 1e-9]
    assert ties == [biggest], f"the largest tabulated charge is not unique: {ties}"
    assert biggest == "Run 4", f"the largest tabulated charge is at {biggest}"
    h.shows(item, biggest)
    return f"the tabulated charges are {charges}, whose unique maximum is at {biggest}"


def q21(table, item):
    charges = _run_charges(table)
    smallest = min(charges, key=charges.get)
    ties = [lab for lab, c in charges.items() if abs(c - charges[smallest]) < 1e-9]
    assert ties == [smallest], f"the smallest tabulated charge is not unique: {ties}"
    assert smallest == "Run 3", f"the smallest tabulated charge is at {smallest}"
    h.shows(item, smallest)
    return f"the tabulated charges are {charges}, whose unique minimum is at {smallest}"


def q22(table, item):
    charges = _run_charges(table)
    groups = {}
    for lab, c in charges.items():
        groups.setdefault(round(c, 6), []).append(lab)
    shared = sorted(g for g in groups.values() if len(g) > 1)
    assert shared == [["Run 1", "Run 2"]], f"the tabulated charges group as {groups}"
    h.shows(item, "Runs 1 and 2")
    return (f"grouping the tabulated rows by their recomputed charge gives {groups}, with "
            f"exactly one pair sharing a value")


def q23(table, item):
    charges = _run_charges(table)
    n = h9.moles_of_electrons(charges["Run 4"])
    h.shows(item, f"{sig(n)} mol")
    return (f"that run's tabulated current and time give {charges['Run 4']:g} C, which "
            f"Faraday's constant turns into {sig(n)} mol of electrons")


def _deposits(table, coulombs):
    """Moles and mass of each tabulated metal for a fixed charge."""
    moles_e = h9.moles_of_electrons(coulombs)
    out = {}
    for row, mm in zip(table["rows"], cg.col(table, MCOL)):
        half = str(row[0])
        z = _electrons(half, f"tabulated half-reaction {half!r}")
        # The element symbol only: "Al3+(aq) ..." must not become "Al3".
        symbol = re.match(r"([A-Z][a-z]?)", half)
        assert symbol, f"cannot read an element symbol from {half!r}"
        name = symbol.group(1)
        out[name] = (moles_e / z, moles_e / z * mm)
    return out


_SYMBOL = {"Ag": "Silver", "Cu": "Copper", "Al": "Aluminium", "Zn": "Zinc"}


def q24(table, item):
    coulombs = _num(_CHARGE, item["q"], "charge")
    dep = _deposits(table, coulombs)
    heaviest = max(dep, key=lambda k: dep[k][1])
    ties = [k for k, v in dep.items() if abs(v[1] - dep[heaviest][1]) < 1e-9]
    assert ties == [heaviest], f"the largest tabulated mass is not unique: {ties}"
    assert heaviest == "Ag", f"the largest deposited mass is {heaviest}"
    h.shows(item, _SYMBOL[heaviest])
    return (f"for the stem's {coulombs:g} C the tabulated half-reactions and molar masses "
            f"give {[(k, round(v[1], 3)) for k, v in dep.items()]}")


def q25(table, item):
    coulombs = _num(_CHARGE, item["q"], "charge")
    dep = _deposits(table, coulombs)
    lightest = min(dep, key=lambda k: dep[k][1])
    ties = [k for k, v in dep.items() if abs(v[1] - dep[lightest][1]) < 1e-9]
    assert ties == [lightest], f"the smallest tabulated mass is not unique: {ties}"
    assert lightest == "Al", f"the smallest deposited mass is {lightest}"
    h.shows(item, _SYMBOL[lightest])
    return (f"for the stem's {coulombs:g} C the recomputed masses are "
            f"{[(k, round(v[1], 3)) for k, v in dep.items()]}, whose minimum is {lightest}")


def q26(table, item):
    coulombs = _num(_CHARGE, item["q"], "charge")
    mass = _deposits(table, coulombs)["Zn"][1]
    h.shows(item, f"{sig(mass)} g")
    return (f"the stem's {coulombs:g} C with that row's tabulated two electrons per ion and "
            f"molar mass gives {sig(mass)} g")


def q27(table, item):
    coulombs = _num(_CHARGE, item["q"], "charge")
    moles = _deposits(table, coulombs)["Al"][0]
    h.shows(item, f"{sig(moles)} mol")
    return (f"the stem's {coulombs:g} C over that row's tabulated three electrons per ion "
            f"gives {sig(moles)} mol")


def q28(table, item):
    coulombs = _num(_CHARGE, item["q"], "charge")
    dep = _deposits(table, coulombs)
    groups = {}
    for name, (moles, _) in dep.items():
        groups.setdefault(round(moles, 9), []).append(name)
    shared = sorted(g for g in groups.values() if len(g) > 1)
    assert shared == [["Cu", "Zn"]], f"the tabulated amounts group as {groups}"
    h.shows(item, "Copper and zinc")
    return (f"grouping the tabulated metals by recomputed moles for {coulombs:g} C gives "
            f"{groups}, with exactly one pair sharing a value")


TABLE_CHECKS = {19: q19, 20: q20, 21: q21, 22: q22, 23: q23,
                24: q24, 25: q25, 26: q26, 27: q27, 28: q28}


# --------------------------------------------------------------- the sign guards

_PLUS_CATHODE = re.compile(r"\+\d+(?:\.\d+)?\s*\\\)\s*g at the cathode")
_MINUS_CATHODE = re.compile(r"-\d+(?:\.\d+)?\s*\\\)\s*g at the cathode")
_PLUS_ANODE = re.compile(r"\+\d+(?:\.\d+)?\s*\\\)\s*g at the anode")
_MINUS_ANODE = re.compile(r"-\d+(?:\.\d+)?\s*\\\)\s*g at the anode")

_CATHODE_GAINS = re.compile(r"cathode gains mass", re.I)
_CATHODE_LOSES = re.compile(r"cathode loses mass", re.I)
_ANODE_GAINS = re.compile(r"anode gains mass", re.I)
_ANODE_LOSES = re.compile(r"anode loses mass", re.I)

SIGNED_MASS_ITEM = 17
WORDED_MASS_ITEM = 18


def electrode_sign_guard(module, signed=SIGNED_MASS_ITEM, worded=WORDED_MASS_ITEM):
    """EK 9.11.A.1.ii with EK 9.8.A.3: the cathode gains and the anode loses.

    Both the presence of the framework's pairing and the ABSENCE of the reversed
    one are asserted. A presence test alone would pass a key that stated both.
    """
    key = h.keyed(module.QUESTIONS[signed - 1])
    gains_at_cathode = bool(_PLUS_CATHODE.search(key))
    loses_at_anode = bool(_MINUS_ANODE.search(key))
    assert gains_at_cathode and loses_at_anode, (
        f"{module.TOPIC[0]} q{signed}: the key does not put the positive change at the "
        f"cathode and the negative one at the anode -- {key!r}"
    )
    assert not _MINUS_CATHODE.search(key) and not _PLUS_ANODE.search(key), (
        f"{module.TOPIC[0]} q{signed}: the key also states the reversed pairing -- {key!r}"
    )

    key = h.keyed(module.QUESTIONS[worded - 1])
    right_way = bool(_CATHODE_GAINS.search(key)) and bool(_ANODE_LOSES.search(key))
    wrong_way = bool(_CATHODE_LOSES.search(key)) or bool(_ANODE_GAINS.search(key))
    assert right_way, (
        f"{module.TOPIC[0]} q{worded}: the key does not say the cathode gains mass and the "
        f"anode loses it, which EK 9.8.A.3 fixes -- {key!r}"
    )
    assert not wrong_way, (
        f"{module.TOPIC[0]} q{worded}: the key states the reversed pairing as well -- {key!r}"
    )
    print(f"OK  {module.TOPIC[0]} electrode signs: the plus is at the cathode and the minus "
          "at the anode, in the numeric item and in the worded one, with neither reversal "
          "present.")


def driven_sign_guard(module, item_no=VOLTAGE_ITEM):
    """EK 9.9.A.1: a driven reaction gives a NEGATIVE voltage."""
    item = module.QUESTIONS[item_no - 1]
    magnitude = _num(_MAGNITUDE_V, item["q"], "magnitude of the standard cell potential")
    token = f"-{magnitude:g}"
    h9.shows_signed(item, token)
    flipped = h9.opposite_sign_offered(item, token)
    verdict = h9.favorability_verdict(h.keyed(item))
    assert verdict is False, (
        f"{module.TOPIC[0]} q{item_no}: a driven reaction is thermodynamically UNFAVORED "
        f"under EK 9.9.A.1, but the key reads {verdict!r} -- {h.keyed(item)!r}"
    )
    print(f"OK  {module.TOPIC[0]} driven sign: the stem's magnitude {magnitude:g} V becomes "
          f"{token} V in the key, with {flipped} offered as the sign-flipped distractor and "
          "the unfavored verdict attached.")


def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in h9.facing(item):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, which this bank "
                f"cannot show -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: no item points at a picture.")


def no_stray_voltage(module, owner=VOLTAGE_ITEM):
    """9.9 owns the cell potential; only the item making the link may state one."""
    for i, item in enumerate(module.QUESTIONS, 1):
        if i == owner:
            continue
        for text in h9.facing(item):
            hit = _VOLTAGE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: states the potential {hit.group(0)!r}, which is "
                f"9.9's material -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: only q{owner} states a potential in volts, and it "
          "is the item that makes the link to EK 9.9.A.1.")


CLAIMS = [
 ("The stoichiometry of the redox reaction occurring in an electrochemical cell",
  "EK 9.11.A.1 verbatim in substance: Faraday's laws can be used to determine the stoichiometry of the redox reaction occurring in an electrochemical cell."),
 ("Number of electrons transferred, mass deposited or removed, current, time elapsed, and charge of the ionic species",
  "EK 9.11.A.1's five listed items, in its own order; neither the temperature nor the cell potential appears among them."),
 ("I = \\frac{q}{t}",
  "EK 9.11.A.1's EQN, giving the current as the charge divided by the time elapsed; Faraday's constant enters at the next step instead."),
 ("96,485 coulombs per one mole of electrons",
  "The equation and constant sheet states Faraday's constant in exactly these terms, which is the conversion from a charge to a number of electrons."),
 ("3000 C",
  "EK 9.11.A.1's equation rearranged for the charge. charge_from_current reads the current and the time out of the stem and multiplies them."),
 ("1930 s",
  "The same equation rearranged for the time elapsed. time_from_charge reads the charge and the current out of the stem and divides."),
 ("5.00 A",
  "EK 9.11.A.1's equation applied directly. current_from_charge reads the charge and the time out of the stem."),
 ("0.500 mol",
  "Faraday's constant as the equation sheet gives it, used to turn a charge into the number of electrons transferred. moles_from_charge recomputes it."),
 ("9650 C",
  "The same conversion the other way. charge_from_moles reads the moles of electrons out of the stem and multiplies by Faraday's constant."),
 ("3.18 g",
  "Charge to electrons by Faraday's constant, electrons to moles of copper by the stem's half-reaction, moles to mass by the stem's molar mass. mass_deposited recomputes all three steps."),
 ("10.8 g",
  "The same chain with one electron per ion, which is why the same charge deposits twice the moles here -- EK 9.11.A.1's fifth item at work."),
 ("2.70 g",
  "The same chain with three electrons per ion. mass_deposited reads the electron count out of the half-reaction printed in the stem."),
 ("0.200 mol",
  "EK 9.11.A.1's fifth item, the charge of the ionic species: two electrons per nickel ion halve the moles of electrons. moles_of_metal recomputes it."),
 ("Three times as many moles are deposited from the 1+ solution",
  "EK 9.11.A.1's fifth item stated as a comparison: a 3+ ion needs three electrons where a 1+ ion needs one, so the same charge discharges three times as many of the latter."),
 ("1930 s",
  "Amount to electrons by the stem's half-reaction, electrons to charge by Faraday's constant, charge and current to time by EK 9.11.A.1's equation. time_for_amount recomputes it."),
 ("5.00 A",
  "The same chain ending at the current instead. current_for_amount reads the amount, the half-reaction and the time out of the stem."),
 ("+3.18 \\) g at the cathode",
  "EK 9.11.A.1.ii names mass deposited ON and removed FROM an electrode, and EK 9.8.A.3 puts the deposit at the cathode. signed_electrode_masses recomputes the magnitude and compares the SIGNED token raw."),
 ("cathode gains mass, because reduction deposits metal there",
  "EK 9.8.A.3 assigns reduction to the cathode and oxidation to the anode, so the deposit and the removal EK 9.11.A.1.ii names fall on those electrodes respectively."),
 ("9650 C",
  "EK 9.11.A.1's equation applied to one tabulated row. q19 multiplies that row's tabulated current by its tabulated time."),
 ("Run 4",
  "The charge is a product of both tabulated columns, so neither decides the comparison alone. q20 recomputes every row and checks the maximum is unique."),
 ("Run 3",
  "The same product read for its minimum. q21 recomputes every tabulated row and checks the smallest is unique."),
 ("Runs 1 and 2",
  "A large current for a short time passes the same charge as a small one for a long time. q22 groups the tabulated rows by recomputed charge and checks exactly one pair shares a value."),
 ("0.200 mol",
  "That row's tabulated current and time give the charge, and Faraday's constant gives the electrons transferred. q23 recomputes both steps."),
 ("Silver",
  "For a fixed charge the mass depends on the electrons per ion and the molar mass together. q24 recomputes every tabulated metal's mass and checks the maximum is unique."),
 ("Aluminium",
  "The same comparison read for its minimum: the most electrons per ion and the smallest tabulated molar mass. q25 recomputes every row."),
 ("3.27 g",
  "Charge to electrons, electrons to moles by that row's tabulated half-reaction, moles to mass by its tabulated molar mass. q26 recomputes the chain."),
 ("0.0333 mol",
  "The same chain stopped at the amount, with the tabulated three electrons per aluminium ion. q27 recomputes it."),
 ("Copper and zinc",
  "For a fixed charge the moles depend only on the electrons per ion, EK 9.11.A.1's fifth item. q28 groups the tabulated metals by recomputed moles and checks one pair shares a value."),
 ("-1.23 \\) V, because a reaction requiring an external supply is thermodynamically unfavored",
  "EK 9.9.A.1: a thermodynamically unfavored reaction results in a negative voltage and requires an externally applied potential. driven_sign_guard builds the negative token from the magnitude in the stem."),
 ("Multiply the current by the time, divide by Faraday's constant, divide by the electrons per ion, then multiply by the molar mass",
  "EK 9.11.A.1's equation, then Faraday's constant, then the charge of the ionic species, then the molar mass -- the chain through the five quantities the statement lists."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the diagram, what do Faraday's laws determine?"
        no_figure_language(mod)

    def stray_voltage(mod, cl):
        mod.QUESTIONS[4]["why"] = mod.QUESTIONS[4]["why"] + " The cell runs at 1.10 V."
        no_stray_voltage(mod)

    def stem_current_changed(mod, cl):
        mod.QUESTIONS[4]["q"] = mod.QUESTIONS[4]["q"].replace(
            "steady current of 1.50 A", "steady current of 2.50 A")

    def stem_time_changed(mod, cl):
        mod.QUESTIONS[5]["q"] = mod.QUESTIONS[5]["q"].replace(
            "current of 3.00 A", "current of 1.50 A")

    def stem_charge_changed(mod, cl):
        mod.QUESTIONS[7]["q"] = mod.QUESTIONS[7]["q"].replace("48250 C", "96500 C")

    def stem_electron_count_changed(mod, cl):
        # q10 keys 3.18 g on a two-electron half-reaction. Rewriting the stem's
        # half-reaction with one electron doubles the recomputed mass.
        mod.QUESTIONS[9]["q"] = mod.QUESTIONS[9]["q"].replace(
            "Cu2+(aq) + 2 e- gives Cu(s)", "Cu+(aq) + e- gives Cu(s)")

    def stem_molar_mass_changed(mod, cl):
        mod.QUESTIONS[10]["q"] = mod.QUESTIONS[10]["q"].replace("107.87 g/mol",
                                                                "63.55 g/mol")

    def stem_amount_changed(mod, cl):
        mod.QUESTIONS[14]["q"] = mod.QUESTIONS[14]["q"].replace("0.0500 mol of copper",
                                                                "0.1000 mol of copper")

    def signed_masses_swapped(mod, cl):
        ch = list(mod.QUESTIONS[16]["choices"])
        ch[0] = "The change is \\( -3.18 \\) g at the cathode and \\( +3.18 \\) g at the anode"
        ch[1] = "The change is \\( +3.18 \\) g at the cathode and \\( -3.18 \\) g at the anode"
        mod.QUESTIONS[16]["choices"] = ch
        cl[16] = ("-3.18 \\) g at the cathode", cl[16][1])
        electrode_sign_guard(mod)

    def signed_key_states_both_pairings(mod, cl):
        ch = list(mod.QUESTIONS[16]["choices"])
        ch[0] = ("The change is \\( +3.18 \\) g at the cathode and \\( -3.18 \\) g at the "
                 "anode, or \\( -3.18 \\) g at the cathode and \\( +3.18 \\) g at the anode")
        mod.QUESTIONS[16]["choices"] = ch
        electrode_sign_guard(mod)

    def worded_electrodes_swapped(mod, cl):
        ch = list(mod.QUESTIONS[17]["choices"])
        ch[0] = ("The anode gains mass, because reduction deposits metal there, and the "
                 "cathode loses mass, because oxidation dissolves it")
        ch[1] = ("The cathode gains mass, because reduction deposits metal there, and the "
                 "anode loses mass, because oxidation removes it")
        mod.QUESTIONS[17]["choices"] = ch
        cl[17] = ("anode gains mass, because reduction deposits metal there", cl[17][1])
        electrode_sign_guard(mod)

    def driven_potential_made_positive(mod, cl):
        ch = list(mod.QUESTIONS[28]["choices"])
        ch[0] = ("\\( +1.23 \\) V, because a reaction requiring an external supply is "
                 "thermodynamically unfavored")
        ch[1] = ("\\( -1.23 \\) V, because a reaction requiring an external supply is "
                 "thermodynamically favored")
        mod.QUESTIONS[28]["choices"] = ch
        cl[28] = ("+1.23 \\) V, because a reaction requiring an external supply is "
                  "thermodynamically unfavored", cl[28][1])
        driven_sign_guard(mod)

    def driven_verdict_flipped(mod, cl):
        ch = list(mod.QUESTIONS[28]["choices"])
        ch[0] = ("\\( -1.23 \\) V, because a reaction requiring an external supply is "
                 "thermodynamically favored")
        ch[1] = ("\\( +1.23 \\) V, because a reaction requiring an external supply is "
                 "thermodynamically unfavored")
        mod.QUESTIONS[28]["choices"] = ch
        cl[28] = ("-1.23 \\) V, because a reaction requiring an external supply is "
                  "thermodynamically favored", cl[28][1])
        driven_sign_guard(mod)

    def driven_magnitude_changed(mod, cl):
        mod.QUESTIONS[28]["q"] = mod.QUESTIONS[28]["q"].replace(
            "being driven is 1.23 V", "being driven is 2.46 V")
        driven_sign_guard(mod)

    def tabulated_largest_charge_moved(mod, cl):
        mod.QUESTIONS[19]["table"] = dict(
            headers=h9_11._T_RUNS["headers"],
            rows=[["Run 1", "5.00", "9650"], ["Run 2", "2.00", "4825"],
                  ["Run 3", "1.00", "1930"], ["Run 4", "10.0", "1930"]])

    def tabulated_smallest_charge_tied(mod, cl):
        mod.QUESTIONS[20]["table"] = dict(
            headers=h9_11._T_RUNS["headers"],
            rows=[["Run 1", "5.00", "1930"], ["Run 2", "2.00", "4825"],
                  ["Run 3", "1.00", "1930"], ["Run 4", "1.00", "1930"]])

    def tabulated_pair_broken(mod, cl):
        mod.QUESTIONS[21]["table"] = dict(
            headers=h9_11._T_RUNS["headers"],
            rows=[["Run 1", "5.00", "1930"], ["Run 2", "2.00", "2000"],
                  ["Run 3", "1.00", "1930"], ["Run 4", "10.0", "1930"]])

    def tabulated_molar_mass_changed(mod, cl):
        mod.QUESTIONS[23]["table"] = dict(
            headers=h9_11._T_METALS["headers"],
            rows=[["Ag+(aq) + e- gives Ag(s)", "10.787"],
                  ["Cu2+(aq) + 2 e- gives Cu(s)", "63.55"],
                  ["Al3+(aq) + 3 e- gives Al(s)", "26.98"],
                  ["Zn2+(aq) + 2 e- gives Zn(s)", "65.38"]])

    def tabulated_electron_count_changed(mod, cl):
        mod.QUESTIONS[25]["table"] = dict(
            headers=h9_11._T_METALS["headers"],
            rows=[["Ag+(aq) + e- gives Ag(s)", "107.87"],
                  ["Cu2+(aq) + 2 e- gives Cu(s)", "63.55"],
                  ["Al3+(aq) + 3 e- gives Al(s)", "26.98"],
                  ["Zn+(aq) + e- gives Zn(s)", "65.38"]])

    def tabulated_equal_moles_pair_broken(mod, cl):
        mod.QUESTIONS[27]["table"] = dict(
            headers=h9_11._T_METALS["headers"],
            rows=[["Ag+(aq) + e- gives Ag(s)", "107.87"],
                  ["Cu2+(aq) + 2 e- gives Cu(s)", "63.55"],
                  ["Al3+(aq) + 3 e- gives Al(s)", "26.98"],
                  ["Zn3+(aq) + 3 e- gives Zn(s)", "65.38"]])

    return [
        ("a stem pointing at a diagram the bank cannot show", figure_language),
        ("a potential in volts outside the one item that owns the link", stray_voltage),
        ("the stem's current changed under an unchanged keyed charge", stem_current_changed),
        ("the stem's current changed under an unchanged keyed time", stem_time_changed),
        ("the stem's charge changed under an unchanged keyed amount", stem_charge_changed),
        ("the stem's half-reaction rewritten with one electron per ion",
         stem_electron_count_changed),
        ("the stem's molar mass changed under an unchanged keyed mass",
         stem_molar_mass_changed),
        ("the stem's amount of metal doubled under an unchanged keyed time",
         stem_amount_changed),
        ("the two signed electrode changes exchanged", signed_masses_swapped),
        ("a signed key stating both pairings at once", signed_key_states_both_pairings),
        ("the worded electrode roles exchanged", worded_electrodes_swapped),
        ("the driven reaction's potential made positive", driven_potential_made_positive),
        ("the driven reaction called favored", driven_verdict_flipped),
        ("the stem's magnitude changed under an unchanged signed key",
         driven_magnitude_changed),
        ("the tabulated largest charge moved", tabulated_largest_charge_moved),
        ("a second tabulated row tied for the smallest charge", tabulated_smallest_charge_tied),
        ("the tabulated pair of equal charges broken", tabulated_pair_broken),
        ("a tabulated molar mass lowered under a keyed heaviest metal",
         tabulated_molar_mass_changed),
        ("the zinc half-reaction's electron count changed under a keyed zinc mass",
         tabulated_electron_count_changed),
        ("the tabulated pair of equal amounts broken", tabulated_equal_moles_pair_broken),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h9_11, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h9_11)
no_stray_voltage(h9_11)
electrode_sign_guard(h9_11)
driven_sign_guard(h9_11)
h.run(h9_11, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
