"""Key audit for AP CHEMISTRY 4.2 Net Ionic Equations.

One ``(anchor, claim)`` per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
EK 4.2.A.1  All physical and chemical processes can be represented symbolically
            by balanced equations.                       (items 4, 14, 24)
EK 4.2.A.2  A chemical change is a rearrangement of atoms into new
            combinations, so any representation of one must contain equal
            numbers of atoms of every element before and after; equations thus
            demonstrate that mass and charge are conserved.
            (items 1, 2, 3, 7, 8, 12, 13, 15, 16, 17, 19, 20, 21, 22, 23, 25,
            26, 28, 29, 30)
EK 4.2.A.3  Balanced molecular, complete ionic and net ionic equations are
            differing symbolic forms; which is used depends on the context.
            (items 5, 6, 9, 10, 11, 12, 17, 18, 19, 26, 27)

THE ARITHMETIC IS THE POINT HERE. EK 4.2.A.2 is a countable claim, so no keyed
equation in this module is trusted: ``h_equation.py`` parses every choice that
contains the word ``gives``, adds the atoms of each element and the charges on
both sides, and the checks below assert that the KEYED equation is the one that
balances and that the distractors do not. Twenty of the thirty items are
recomputed that way. ``h_equation.selftest()`` is the control for the counter
itself and runs inside ``--selftest`` before anything else, because a parser
that returns True for everything would make every check below vacuous.

q27 CLASSIFIES THE THREE FORMS rather than trusting the row labels: a row with
no charged species is the molecular form, a row with charged species and a
species standing unaltered on both sides is the complete ionic form, and a row
with charged species and none repeated is the net ionic form. EK 4.2.A.3's three
forms therefore have to come out one each, or the check fails.

NO FIGURE LANGUAGE. The bank cannot carry images; ``no_figure_language``
asserts no stem or choice points at one.

NEGATIVE CONTROL: ``python3 verify_h4_2.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h_equation as heq

import h4_2

EQCOL = "Equation as the student wrote it"
FORMCOL = "Equation"
PROPCOL = "Proposed net ionic equation"

_FIGURE = re.compile(
    r"(?<![a-z])(as shown|shown below|shown above|figure|image|picture|depicted|"
    r"pictured|illustrated|(?:diagram|graph|profile|curve|plot|chart)s?\s+"
    r"(?:above|below))(?![a-z])", re.I)


def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, but this bank "
                f"carries no images -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: no stem or choice points at a picture.")


# --------------------------------------------------------------- shared helpers

def _try(fn, text):
    """``fn(text)`` where a choice that is not a readable equation counts False."""
    try:
        return fn(text)
    except AssertionError:
        return False


def equation_choices(item):
    """The indices of the choices that are written as equations."""
    return [i for i, c in enumerate(item["choices"]) if " gives " in c]


def only_key_balances(item, what=heq.balanced, name="balances"):
    """Exactly one choice satisfies ``what``, and it is the keyed one."""
    idx = equation_choices(item)
    assert len(idx) >= 2, f"only {len(idx)} choices are equations; nothing to compare"
    good = [i for i in idx if _try(what, item["choices"][i])]
    assert good == [item["ans"]], (
        f"choices that {name}: {good}, but the key is {item['ans']} -- "
        + "; ".join(f"{i}: {item['choices'][i]}" for i in idx)
    )
    return (f"of the {len(idx)} equations offered, only the keyed one {name}: "
            f"{heq.report(item['choices'][item['ans']])}")


def only_key_fails(item, what=heq.charge_balanced, name="conserves charge"):
    """Exactly one choice FAILS ``what``, and it is the keyed one."""
    idx = equation_choices(item)
    bad = [i for i in idx if not _try(what, item["choices"][i])]
    assert bad == [item["ans"]], (
        f"choices that fail to {name}: {bad}, but the key is {item['ans']}"
    )
    return (f"of the {len(idx)} equations offered, only the keyed one fails to {name}: "
            f"{heq.report(item['choices'][item['ans']])}")


def _species(side_text):
    return [s.strip() for s in str(side_text).split(" + ") if s.strip()]


def form_of(eq):
    """``molecular``, ``complete ionic`` or ``net ionic`` for one equation."""
    left, right = re.split(r"\s+gives\s+", eq)
    ls, rs = _species(left), _species(right)
    charged = any(heq.species(s)[2] != 0 for s in ls + rs)
    if not charged:
        return "molecular"
    return "complete ionic" if set(ls) & set(rs) else "net ionic"


# ---------------------------------------------------------------- table items

def q16(table, item):
    eqs = dict(zip(cg.labels(table),
                   [r[table["headers"].index(EQCOL)] for r in table["rows"]]))
    ok = sorted(lab for lab, eq in eqs.items() if heq.atom_balanced(eq))
    assert ok == ["E1", "E3"], f"the tabulated equations with equal atom counts are {ok}"
    h.shows(item, "E1 and E3")
    return (f"counting each element on both sides of the {len(eqs)} tabulated equations "
            f"leaves {ok} with equal numbers of atoms of every element")


def q27(table, item):
    forms = {lab: form_of(eq) for lab, eq in
             zip(cg.labels(table), [r[table["headers"].index(FORMCOL)] for r in table["rows"]])}
    assert sorted(forms.values()) == ["complete ionic", "molecular", "net ionic"], (
        f"the tabulated rows classify as {forms}, not one of each of EK 4.2.A.3's forms"
    )
    net = [lab for lab, f in forms.items() if f == "net ionic"]
    assert net == ["R3"], f"the net ionic row is {net}"
    for eq in [r[table["headers"].index(FORMCOL)] for r in table["rows"]]:
        assert heq.balanced(eq), f"a tabulated equation does not balance: {eq}"
    h.shows(item, "R3")
    return (f"classifying each tabulated row by whether it carries ions and whether a "
            f"species stands unaltered on both sides gives {forms}")


def q29(table, item):
    eqs = dict(zip(cg.labels(table),
                   [r[table["headers"].index(PROPCOL)] for r in table["rows"]]))
    bad = sorted(lab for lab, eq in eqs.items() if not heq.charge_balanced(eq))
    assert bad == ["N3"], f"the tabulated equations failing to conserve charge are {bad}"
    for lab, eq in eqs.items():
        assert heq.atom_balanced(eq), f"{lab} also fails on atoms, so charge is not the issue"
    h.shows(item, "N3")
    return (f"summing the charges on each side of the {len(eqs)} tabulated equations leaves "
            f"{bad} unbalanced while every row balances on atoms")


TABLE_CHECKS = {16: q16, 27: q27, 29: q29}


# --------------------------------------------------------------- stem numerics

def n7(item):
    return only_key_balances(item)


def n8(item):
    fits = [n for n in range(1, 11) if heq.balanced(f"4 Fe + {n} O2 gives 2 Fe2O3")]
    assert fits == [3], f"coefficients of O2 that balance the equation: {fits}"
    h.shows(item, str(fits[0]))
    return f"trying every whole coefficient from one to ten leaves {fits} as the only balance"


def net_ionic_key(item, anchor, molecular=None, complete=None, unbalanced=()):
    """The key balances AND is the net ionic form; the named siblings are what they claim.

    A "which is the net ionic equation" item cannot be settled by balance alone,
    because the molecular and complete ionic forms of the same reaction balance
    too -- that is EK 4.2.A.3's whole point. So this recomputes the CLASSIFICATION
    as well: the key must carry ions with no species standing unaltered on both
    sides, the molecular sibling must carry no ions at all, the complete ionic
    sibling must repeat at least one species across the arrow, and each choice
    named in ``unbalanced`` must actually fail EK 4.2.A.2's counts.
    """
    key = item["choices"][item["ans"]]
    assert heq.balanced(key), f"the keyed equation does not balance: {heq.report(key)}"
    assert form_of(key) == "net ionic", f"the keyed equation is the {form_of(key)} form"
    if molecular is not None:
        got = form_of(item["choices"][molecular])
        assert got == "molecular", f"choice {molecular} is the {got} form, not molecular"
    if complete is not None:
        got = form_of(item["choices"][complete])
        assert got == "complete ionic", f"choice {complete} is the {got} form"
    for j in unbalanced:
        assert not _try(heq.balanced, item["choices"][j]), (
            f"choice {j} was expected to fail EK 4.2.A.2's counts but balances"
        )
    h.shows(item, anchor)
    return (f"the keyed equation balances ({heq.report(key)}) and classifies as the net ionic "
            f"form, while the sibling forms and the {len(unbalanced)} miscounted choice(s) "
            "classify as stated")


def n9(item):
    return net_ionic_key(item, "Ag+(aq) + Cl-(aq) gives AgCl(s)",
                         molecular=1, complete=2, unbalanced=(4,))


def n12(item):
    """The molecular form: balanced, and the only balanced choice carrying no ions."""
    key = item["choices"][item["ans"]]
    assert heq.balanced(key), f"the keyed equation does not balance: {heq.report(key)}"
    mol = [i for i, c in enumerate(item["choices"])
           if " gives " in c and _try(heq.balanced, c) and form_of(c) == "molecular"]
    assert mol == [item["ans"]], f"balanced choices in the molecular form: {mol}"
    h.shows(item, "BaSO4(s) + 2 NaCl(aq)")
    return (f"the keyed equation balances ({heq.report(key)}) and is the only balanced choice "
            "written without ions, which is EK 4.2.A.3's molecular form")


def n13(item):
    return only_key_balances(item)


def n14(item):
    key = item["choices"][item["ans"]]
    left, right = re.split(r"\s+gives\s+", key)
    assert heq.species(left)[1] == heq.species(right)[1], \
        f"the keyed equation changes composition: {heq.report(key)}"
    assert "(l)" in left and "(g)" in right, f"the keyed equation is not a vaporization: {key}"
    h.shows(item, "H2O(l) gives H2O(g)")
    return ("the keyed equation carries the same element counts on both sides and takes the "
            "liquid to the gas, which is a phase change rather than a chemical one")


def n15(item):
    (_, lq), (_, rq) = heq.equation("NaCl(s) gives Na+(aq) + Cl-(aq)")
    assert lq == 0 and rq == 0, f"the charge sums are {lq} and {rq}"
    h.shows(item, "total charge is zero on each side")
    return f"summing the charges gives {lq} on the left and {rq} on the right"


def n17(item):
    return net_ionic_key(item, "H3O+(aq) + OH-(aq) gives 2 H2O(l)",
                         molecular=1, complete=4, unbalanced=(3,))


def n19(item):
    return net_ionic_key(item, "2 H3O+(aq) gives Mg2+(aq)",
                         molecular=1, unbalanced=(2, 3))


def n20(item):
    (_, lq), (_, rq) = heq.equation("Zn(s) + Cu2+(aq) gives Zn2+(aq) + Cu(s)")
    assert lq == rq == 2, f"the charge sums are {lq} and {rq}"
    h.shows(item, "total is plus two on each side")
    return f"summing the charges of the stated equation gives {lq:+d} and {rq:+d}"


def n21(item):
    return only_key_fails(item)


def n22(item):
    key = "Al(s) + O2(g) gives Al2O3(s)"
    assert not heq.atom_balanced(key), "the student's equation balances on atoms after all"
    assert heq.charge_balanced(key), "the student's equation also fails on charge"
    h.shows(item, "numbers of aluminum and of oxygen atoms differ")
    return f"counting the elements of the student's equation gives {heq.report(key)}"


def n23(item):
    return only_key_balances(item)


def n24(item):
    key = "I2(s) gives I2(g)"
    left, right = re.split(r"\s+gives\s+", key)
    assert heq.species(left)[1] == heq.species(right)[1] == {"I": 2}, heq.report(key)
    h.shows(item, "I2(s) gives I2(g)")
    return "two iodine atoms stand on each side, so the representation balances as EK 4.2.A.2 asks"


def n26(item):
    return net_ionic_key(item, "Ca2+(aq) + CO32-(aq) gives CaCO3(s)",
                         molecular=1, complete=2, unbalanced=(4,))


def n28(item):
    return only_key_balances(item)


NUMERIC = {7: n7, 8: n8, 9: n9, 12: n12, 13: n13, 14: n14, 15: n15, 17: n17,
           19: n19, 20: n20, 21: n21, 22: n22, 23: n23, 24: n24, 26: n26, 28: n28}


CLAIMS = [
 ("Equal numbers of atoms of every element before and after the change",
  "EK 4.2.A.2, near verbatim: any representation of a chemical change must contain equal numbers of atoms of every element before and after the change occurred."),
 ("rearrangement of atoms into new combinations",
  "EK 4.2.A.2 gives this as the reason for the equal counts: the changes are the result of a rearrangement of atoms into new combinations."),
 ("That mass and charge are conserved",
  "EK 4.2.A.2 ends by stating that equations thus demonstrate that mass and charge are conserved in chemical reactions."),
 ("All physical and chemical processes",
  "EK 4.2.A.1, verbatim in substance: all physical and chemical processes can be represented symbolically by balanced equations."),
 ("Balanced molecular, complete ionic, and net ionic equations",
  "EK 4.2.A.3, near verbatim: these are the differing symbolic forms used to represent a chemical reaction."),
 ("The context in which the equation is to be used",
  "EK 4.2.A.3 states that the form used to represent the reaction depends on the context in which it is to be used."),
 ("5 O2 gives 3 CO2 + 4 H2O",
  "EK 4.2.A.2's equal atom counts, recomputed in n7: every choice is parsed and only the keyed equation balances."),
 ("3",
  "EK 4.2.A.2's equal atom counts, recomputed in n8 by trying every whole coefficient from one to ten."),
 ("Ag+(aq) + Cl-(aq) gives AgCl(s)",
  "EK 4.2.A.3 names the net ionic equation as one of three forms. Recomputed in n9, which checks the key balances in atoms and charge and is the only balanced choice with ions and no species repeated across the arrow."),
 ("Sodium ion and nitrate ion",
  "EK 4.2.A.3 distinguishes the complete ionic form, in which every dissolved species is written out, from the net ionic form; the two ions still in solution afterwards are the ones the net ionic form omits."),
 ("The complete ionic equation",
  "EK 4.2.A.3 names the complete ionic equation as the form in which dissolved substances are written as separate ions, including those that stand unaltered on both sides."),
 ("BaSO4(s) + 2 NaCl(aq)",
  "EK 4.2.A.3's molecular form together with EK 4.2.A.2's equal atom counts. Recomputed in n12, which also checks the keyed choice carries no charged species."),
 ("Zn(s) + Cu2+(aq) gives Zn2+(aq) + Cu(s)",
  "EK 4.2.A.2 requires both mass and charge to be conserved. Recomputed in n13, which parses all five equations and finds only the keyed one balanced on both."),
 ("H2O(l) gives H2O(g)",
  "EK 4.2.A.1 permits a physical process to be written as a balanced equation. Recomputed in n14, which checks the element counts match and that the equation runs from liquid to gas."),
 ("total charge is zero on each side",
  "EK 4.2.A.2's conservation of charge, recomputed in n15 by summing the charges of the dissolution equation."),
 ("E1 and E3",
  "EK 4.2.A.2's equal atom counts, recomputed in q16 for every tabulated equation."),
 ("H3O+(aq) + OH-(aq) gives 2 H2O(l)",
  "EK 4.2.A.3's net ionic form with EK 4.2.A.2's atom counts. Recomputed in n17: only the keyed equation balances, and the singular-water version does not."),
 ("carries only the species whose combination differs",
  "EK 4.2.A.3 states that the form used depends on the context in which it is to be used, so the net ionic form is chosen for a purpose rather than being the only correct or the only balanced equation."),
 ("2 H3O+(aq) gives Mg2+(aq)",
  "EK 4.2.A.3's net ionic form with EK 4.2.A.2's conservation of atoms and charge. Recomputed in n19."),
 ("total is plus two on each side",
  "EK 4.2.A.2's conservation of charge, recomputed in n20 from the equation stated in the stem."),
 ("Zn(s) + Ag+(aq) gives Zn2+(aq) + Ag(s)",
  "EK 4.2.A.2 requires charge to be conserved. Recomputed in n21, which finds the keyed equation is the only one of the five whose charge sums disagree."),
 ("numbers of aluminum and of oxygen atoms differ",
  "EK 4.2.A.2's equal atom counts. Recomputed in n22, which also confirms the student's equation does conserve charge, so atoms are the defect."),
 ("C2H5OH + 3 O2 gives 2 CO2 + 3 H2O",
  "EK 4.2.A.2's equal atom counts, recomputed in n23 across all five offered equations."),
 ("I2(s) gives I2(g)",
  "EK 4.2.A.1 allows all physical processes to be represented symbolically by balanced equations. Recomputed in n24."),
 ("changes the composition, and so the identity of the substance",
  "EK 4.2.A.2 requires the equation to represent the change that occurred, and EK 4.1.A.1 makes composition the identity of a substance, so rewriting a formula would represent a different substance."),
 ("Ca2+(aq) + CO32-(aq) gives CaCO3(s)",
  "EK 4.2.A.3's net ionic form with EK 4.2.A.2's conservation of atoms and charge, recomputed in n26."),
 ("R3",
  "EK 4.2.A.3's three forms, recomputed in q27 by classifying each tabulated row on whether it carries ions and whether any species stands unaltered on both sides."),
 ("2 Al(s) + 3 Cl2(g) gives 2 AlCl3(s)",
  "EK 4.2.A.2's equal atom counts applied to the stated identity of the product, recomputed in n28."),
 ("N3",
  "EK 4.2.A.2's conservation of charge, recomputed in q29 for every tabulated equation, with each row also checked to balance on atoms."),
 ("framework says equations demonstrate that mass and charge are conserved",
  "EK 4.2.A.2 makes that statement about chemical reactions generally rather than about any one of EK 4.2.A.3's three symbolic forms."),
]


def _extra_mutations():
    def unbalance_the_key(mod, cl):
        """The keyed propane equation retyped so it no longer balances."""
        mod.QUESTIONS[6]["choices"][0] = "C3H8 + 5 O2 gives 3 CO2 + 5 H2O"
        cl[6] = ("5 O2 gives 3 CO2 + 5 H2O", cl[6][1])

    def balance_a_distractor(mod, cl):
        """A distractor made balanced too, so the key is no longer the only one."""
        mod.QUESTIONS[22]["choices"][1] = "3 O2 + C2H5OH gives 3 H2O + 2 CO2"

    def corrupt_table_equation(mod, cl):
        """A tabulated equation retyped so the recomputed answer changes."""
        t = mod.QUESTIONS[15]["table"]
        mod.QUESTIONS[15]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], "N2(g) + 3 H2(g) gives 2 NH3(g)"] if r[0] == "E2" else list(r)
                  for r in t["rows"]])

    def corrupt_form_row(mod, cl):
        """The net ionic row retyped with a spectator, so no row is net ionic."""
        t = mod.QUESTIONS[26]["table"]
        mod.QUESTIONS[26]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], "Ca2+(aq) + CO32-(aq) + Na+(aq) gives CaCO3(s) + Na+(aq)"]
                  if r[0] == "R3" else list(r) for r in t["rows"]])

    def fix_the_charge_row(mod, cl):
        """The one charge-failing row repaired, so the keyed answer is false."""
        t = mod.QUESTIONS[28]["table"]
        mod.QUESTIONS[28]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], "Zn(s) + Cu2+(aq) gives Zn2+(aq) + Cu(s)"] if r[0] == "N3"
                  else list(r) for r in t["rows"]])

    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "Which equation is shown above?"
        no_figure_language(mod)

    return [("the keyed equation retyped so it does not balance", unbalance_the_key),
            ("a distractor made to balance as well as the key", balance_a_distractor),
            ("a tabulated equation retyped so the recomputed set changes", corrupt_table_equation),
            ("the net ionic row given a spectator ion", corrupt_form_row),
            ("the charge-failing row repaired so the key is false", fix_the_charge_row),
            ("a stem pointing at a picture the bank cannot show", figure_language)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    heq.selftest()
    h.selftest(h4_2, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

heq.selftest()
no_figure_language(h4_2)
h.run(h4_2, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
