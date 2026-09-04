"""Key audit for AP CHEMISTRY 8.6 Molecular Structure of Acids and Bases.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON. EK 8.6.A.1 and its five sub-points are the whole content
of this topic, so the audit is organised by sub-point:

  8.6.A.1 preamble  structure identifies which protons act, and their relative
                    strength                           1, 17, 23, 25
  i    strong acids have very weak conjugate bases, stabilized by
       electronegativity, inductive effects or resonance
                                                       2, 15, 18, 22, 26
  ii   carboxylic acids are a common class of weak acid      3, 14
  iii  group I and II hydroxides are strong bases, with very weak conjugate
       acids                                           4, 5, 19, 27, 28
  iv   common weak bases: nitrogenous bases such as ammonia, and carboxylate
       ions                                            6, 13, 20
  v    electronegative elements stabilize the conjugate base and so increase
       acid strength           7, 8, 9, 10, 11, 12, 16, 21, 24, 29, 30

SCOPE. h8_2.py owns pH arithmetic for strong acids and bases; h8_3.py owns Ka,
Kb and percent ionization. ``no_ph_or_constant_question`` asserts that no item
here asks for a pH or for the value of an ionization constant, so this module
argues from structure and nothing else.

THE DATA HAS TO SUPPORT THE TREND. ``pka_trend_is_monotonic`` asserts that in
each measured series the tabulated pKa moves strictly in one direction as the
structural variable changes. Without it a table could show a flat or scrambled
series behind a stem that claims a trend, and every other check would pass.

NEGATIVE CONTROL: ``python3 verify_h8_6.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h8_6

NCL = "Chlorine atoms on the carbon bearing the acidic group"
NGAP = "Carbon atoms between the chlorine and the acidic group"
PKA = "pKa measured by the student"
DESC = "How the framework describes it"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below)(?![a-z])", re.I)

# 8.2 owns pH arithmetic and 8.3 owns the ionization constants. Explicit
# question phrases only -- "pKa" appears legitimately all through this module as
# a measured quantity to be COMPARED.
_ARITHMETIC_Q = re.compile(
    r"(?<![a-z])(?:what is the ph|calculate the ph|what is the poh"
    r"|what is the value of k[ab]|calculate k[ab]"
    r"|what is the percent ionization)(?![a-z])", re.I)


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
    print(f"OK  {module.TOPIC[0]} figures: no item points at a structure the student "
          "cannot see; every structure is described in words or in a table.")


def no_ph_or_constant_question(module):
    """8.2 owns pH arithmetic and 8.3 owns Ka and Kb."""
    for i, item in enumerate(module.QUESTIONS, 1):
        hit = _ARITHMETIC_Q.search(item["q"])
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: asks for {hit.group(0)!r}, which is 8.2's or 8.3's "
            "material"
        )
    print(f"OK  {module.TOPIC[0]} scope: no item computes a pH or an ionization constant; "
          "every argument runs from structure.")


def pka_trend_is_monotonic(module):
    """A stem claiming a trend must sit on a table that shows one.

    Both measured series vary exactly one structural feature. If the tabulated
    pKa did not move strictly in one direction as that feature changed, the
    items keyed on the trend would be false while every structural check still
    passed -- so the data itself is gated.
    """
    checked = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        t = item.get("table")
        if not t:
            continue
        heads = [cg.normalize(x) for x in t["headers"]]
        for var in (NCL, NGAP):
            if cg.normalize(var) not in heads:
                continue
            xs, ys = cg.col(t, var), cg.col(t, PKA)
            assert xs == sorted(xs), f"{module.TOPIC[0]} q{i}: {var} is not in order: {xs}"
            assert len(set(xs)) == len(xs), \
                f"{module.TOPIC[0]} q{i}: the structural variable repeats: {xs}"
            falling = all(b < a for a, b in zip(ys, ys[1:]))
            rising = all(b > a for a, b in zip(ys, ys[1:]))
            assert falling or rising, (
                f"{module.TOPIC[0]} q{i}: the tabulated pKa {ys} is neither strictly "
                f"falling nor strictly rising against {xs}, so no trend can be read"
            )
            checked += 1
    assert checked >= 2, f"{module.TOPIC[0]}: only {checked} measured series checked"
    print(f"OK  {module.TOPIC[0]} data: {checked} tabulated series checked; each moves "
          "strictly in one direction as its structural variable changes.")


# ------------------------------------------------------------------ table items

def q8(table, item):
    xs, ys = cg.col(table, NCL), cg.col(table, PKA)
    assert all(b < a for a, b in zip(ys, ys[1:])), f"the tabulated pKa is {ys}"
    assert xs[0] == 0 and xs[-1] == 3, f"the tabulated chlorine counts are {xs}"
    h.shows(item, "falls as more chlorine atoms are added")
    return f"the tabulated pKa runs {ys} as the chlorine count runs {xs}, falling at every step"


def q9(table, item):
    pkas = dict(zip(cg.labels(table), cg.col(table, PKA)))
    strongest = min(pkas, key=pkas.get)
    assert strongest == "N", f"the smallest tabulated pKa belongs to {strongest}: {pkas}"
    assert len(set(pkas.values())) == len(pkas), "the tabulated pKa values must be distinct"
    counts = dict(zip(cg.labels(table), cg.col(table, NCL)))
    assert counts[strongest] == max(counts.values()), (
        "the strongest acid must also be the one with the most electronegative atoms, or "
        "the item does not illustrate EK 8.6.A.1.v"
    )
    h.shows(item, "Acid N")
    return (f"the tabulated pKa values are {pkas}, whose minimum is at {strongest}, which "
            f"also carries the most chlorine")


def q10(table, item):
    xs, ys = cg.col(table, NCL), cg.col(table, PKA)
    assert all(b < a for a, b in zip(ys, ys[1:])), f"the tabulated pKa is {ys}"
    assert len(set(xs)) == len(xs), "the series must vary the structural feature"
    h.shows(item, "stabilize the conjugate base and so increase acid strength")
    return (f"the series varies only the electronegative-atom count {xs} and the tabulated "
            f"pKa falls {ys}")


def q11(table, item):
    xs, ys = cg.col(table, NGAP), cg.col(table, PKA)
    assert all(b > a for a, b in zip(ys, ys[1:])), f"the tabulated pKa is {ys}"
    assert xs[0] == 0, f"the closest tabulated position is {xs[0]}"
    h.shows(item, "chlorine sits closer to the acidic group")
    return (f"the tabulated pKa rises {ys} as the chlorine moves from {xs[0]:g} to "
            f"{xs[-1]:g} carbons away, so the closest position is the strongest acid")


def q12(table, item):
    pkas = dict(zip(cg.labels(table), cg.col(table, PKA)))
    strongest = min(pkas, key=pkas.get)
    assert strongest == "P", f"the smallest tabulated pKa belongs to {strongest}: {pkas}"
    gaps = dict(zip(cg.labels(table), cg.col(table, NGAP)))
    assert gaps[strongest] == min(gaps.values()), (
        "the most stabilized conjugate base must belong to the nearest substituent"
    )
    h.shows(item, "Acid P")
    return (f"the tabulated pKa values are {pkas}, whose minimum is at {strongest}, the "
            "acid whose electronegative atom is nearest the acidic group")


def q19(table, item):
    labels = cg.labels(table)
    descs = {lab: str(table["rows"][i][1]) for i, lab in enumerate(labels)}
    strong = [lab for lab, d in descs.items() if "hydroxide" in cg.normalize(d)]
    assert sorted(strong) == sorted(["NaOH", "Ca(OH)2"]), \
        f"the tabulated hydroxides are {strong}"
    assert len(strong) == 2, f"exactly two rows must be hydroxides: {descs}"
    h.shows(item, "group I hydroxide and the group II hydroxide")
    return f"exactly two tabulated rows are described as hydroxides: {strong}"


def q20(table, item):
    labels = cg.labels(table)
    descs = {lab: str(table["rows"][i][1]) for i, lab in enumerate(labels)}
    weak = [lab for lab, d in descs.items()
            if "nitrogenous" in cg.normalize(d) or "carboxylate" in cg.normalize(d)]
    assert sorted(weak) == sorted(["NH3", "CH3COO-"]), f"the tabulated weak bases are {weak}"
    assert len(weak) == 2, f"exactly two rows must be weak bases: {descs}"
    h.shows(item, "nitrogenous base and the carboxylate ion")
    return (f"exactly two tabulated rows are described as a nitrogenous base or a "
            f"carboxylate ion: {weak}")


def q29(table, item):
    xs, ys = cg.col(table, NCL), cg.col(table, PKA)
    assert all(b < a for a, b in zip(ys, ys[1:])), f"the tabulated pKa is {ys}"
    assert min(ys) == ys[-1], f"the smallest tabulated pKa is not the last: {ys}"
    h.shows(item, "below the smallest tabulated value")
    return (f"the tabulated pKa falls monotonically to {ys[-1]:g}, so continuing the trend "
            "goes below it")


TABLE_CHECKS = {8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 19: q19, 20: q20, 29: q29}

NUMERIC = {}


CLAIMS = [
 ("Which protons will participate, and the relative strength",
  "EK 8.6.A.1, verbatim in substance: the protons that will participate in acid-base reactions, and their relative strength, can be inferred from the molecular structure."),
 ("Electronegativity, inductive effects, resonance, or some combination",
  "EK 8.6.A.1.i names exactly these as what stabilizes the very weak conjugate bases of the strong acids."),
 ("Carboxylic acids",
  "EK 8.6.A.1.ii states that carboxylic acids are one common class of weak acid; nitrogenous compounds appear in EK 8.6.A.1.iv as weak BASES."),
 ("Group I and group II hydroxides",
  "EK 8.6.A.1.iii names group I and II hydroxides as its examples of strong bases; ammonia and carboxylate ions are the weak bases of EK 8.6.A.1.iv."),
 ("They are very weak",
  "EK 8.6.A.1.iii states that strong bases have very weak conjugate acids. Every acid-base pair has both members, so the conjugate acid exists; it is simply feeble."),
 ("ammonia, and carboxylate ions",
  "EK 8.6.A.1.iv: common weak bases include nitrogenous bases such as ammonia as well as carboxylate ions. Group I hydroxides belong to the strong bases of EK 8.6.A.1.iii."),
 ("stabilize the conjugate base relative to the conjugate acid, increasing acid strength",
  "EK 8.6.A.1.v, verbatim in substance. The direction matters: stabilizing what is left after the proton departs is what makes the proton easier to lose."),
 ("falls as more chlorine atoms are added",
  "EK 8.6.A.1.v read off a measured series. q8 recomputes the tabulated pKa against the tabulated chlorine count and checks the fall is strict at every step."),
 ("Acid N",
  "EK 8.3.A.2 makes the smallest pKa the strongest acid. q9 recomputes the minimum, checks the values are distinct, and checks that acid also carries the most chlorine."),
 ("stabilize the conjugate base and so increase acid strength",
  "EK 8.6.A.1.v is the statement the series isolates: exactly one structural feature varies, and q10 checks that."),
 ("chlorine sits closer to the acidic group",
  "EK 8.6.A.1.i names inductive effects, which are transmitted through bonds and weaken with distance. q11 recomputes the rise in tabulated pKa with distance."),
 ("Acid P",
  "EK 8.6.A.1.v ties a more stabilized conjugate base to a stronger acid. q12 recomputes the minimum pKa and checks it belongs to the nearest substituent."),
 ("nitrogenous base, the framework's own example",
  "EK 8.6.A.1.iv names nitrogenous bases such as ammonia among the common weak bases; EK 8.6.A.1.v attaches electronegativity to increased ACID strength."),
 ("carboxylate ion",
  "EK 8.6.A.1.ii and iv pair carboxylic acids with carboxylate ions, which is an acid with what remains after its proton leaves."),
 ("spread over more than one atom",
  "EK 8.6.A.1.i names resonance among the stabilizing influences, and resonance delocalizes charge across more than one atom."),
 ("electronegative fluorine stabilizes the conjugate base",
  "EK 8.6.A.1.v: electronegative elements stabilize the conjugate base and so increase acid strength; the substituent is not itself an acidic proton."),
 ("bonded to oxygen",
  "EK 8.6.A.1 has structure identify the participating proton, and EK 8.6.A.1.ii and iv make the carboxylate ion what remains after the hydrogen on oxygen departs."),
 ("very weak conjugate base",
  "EK 8.6.A.1.i, verbatim in substance: the strong acids have very weak conjugate bases, stabilized by electronegativity, inductive effects or resonance."),
 ("group I hydroxide and the group II hydroxide",
  "EK 8.6.A.1.iii names group I and II hydroxides as strong bases. q19 recomputes from the tabulated descriptions which two rows those are."),
 ("nitrogenous base and the carboxylate ion",
  "EK 8.6.A.1.iv names both among the common weak bases. q20 recomputes from the tabulated descriptions which two rows those are."),
 ("electronegative atoms near the acidic group",
  "EK 8.6.A.1.v with EK 8.6.A.1.i's inductive effects, which weaken with distance; concentration is not strength, the distinction EK 8.3.A.1 rests on."),
 ("little tendency to take a proton back",
  "EK 8.6.A.1.i pairs the very weak conjugate bases of the strong acids with their stabilization. Such an anion is in fact present in large concentration, so concentration is not the reason."),
 ("carboxylic acids carry, rather than a basic nitrogen",
  "EK 8.6.A.1.ii and iv sort the two families: carboxylic acids are a common weak acid, nitrogenous compounds a common weak base."),
 ("The second, so the second acid is the stronger",
  "EK 8.6.A.1.v ties stabilization of the conjugate base by electronegative elements directly to increased acid strength, so both halves of the answer point the same way."),
 ("molecular structure around each proton differs",
  "EK 8.6.A.1 says the RELATIVE strength of the protons can be inferred from structure, which presupposes that protons in one molecule can differ."),
 ("molar mass of the anion",
  "EK 8.6.A.1.i lists electronegativity, inductive effects and resonance; molar mass is not among them and the framework offers no mass-based rule."),
 ("hydroxide is a strong base while ammonia is a common weak base",
  "EK 8.6.A.1.iii and iv place the two substances on opposite sides of the framework's own division."),
 ("strong base, whose conjugate acid is very weak",
  "EK 8.6.A.1.iii names group I and II hydroxides as strong bases and says in the same sentence that strong bases have very weak conjugate acids."),
 ("below the smallest tabulated value",
  "EK 8.6.A.1.v continued past the tabulated series. q29 checks the tabulated pKa falls monotonically and that its minimum is the last row."),
 ("conjugate base, the stronger the acid",
  "EK 8.6.A.1.v states the relationship directly, and EK 8.6.A.1.i makes the same connection for the strong acids by way of their very weak conjugate bases."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the structure shown above, which proton is acidic?"
        no_figure_language(mod)

    def ph_question(mod, cl):
        mod.QUESTIONS[2]["q"] = "What is the pH of a 0.10 M solution of this acid?"
        no_ph_or_constant_question(mod)

    def flat_series(mod, cl):
        # A series whose pKa does not move behind a stem that claims a trend.
        mod.QUESTIONS[7]["table"] = dict(
            headers=h8_6._T_CHLORINE["headers"],
            rows=[["J", "0", "4.8"], ["L", "1", "4.8"],
                  ["M", "2", "4.8"], ["N", "3", "4.8"]])
        pka_trend_is_monotonic(mod)

    def scrambled_series(mod, cl):
        mod.QUESTIONS[7]["table"] = dict(
            headers=h8_6._T_CHLORINE["headers"],
            rows=[["J", "0", "4.8"], ["L", "1", "1.3"],
                  ["M", "2", "2.9"], ["N", "3", "0.7"]])

    def strongest_lacks_the_substituent(mod, cl):
        # The smallest pKa moved onto the acid with the FEWEST electronegative
        # atoms, so the series would no longer illustrate EK 8.6.A.1.v.
        mod.QUESTIONS[8]["table"] = dict(
            headers=h8_6._T_CHLORINE["headers"],
            rows=[["J", "0", "0.7"], ["L", "1", "1.3"],
                  ["M", "2", "2.9"], ["N", "3", "4.8"]])

    def third_hydroxide(mod, cl):
        mod.QUESTIONS[18]["table"] = dict(
            headers=h8_6._T_SUBSTANCES["headers"],
            rows=[["NaOH", "a group I hydroxide"], ["Ca(OH)2", "a group II hydroxide"],
                  ["KOH", "a group I hydroxide"], ["CH3COO-", "a carboxylate ion"]])

    return [("a stem referring to a structure the bank cannot show", figure_language),
            ("an item computing a pH, which 8.2 owns", ph_question),
            ("a measured series whose pKa does not move at all", flat_series),
            ("a measured series whose pKa moves in both directions", scrambled_series),
            ("the strongest acid moved onto the least substituted member of the series",
             strongest_lacks_the_substituent),
            ("a third hydroxide added, so the keyed pair of strong bases is wrong",
             third_hydroxide)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h8_6, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h8_6)
no_ph_or_constant_question(h8_6)
pka_trend_is_monotonic(h8_6)
h.run(h8_6, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
