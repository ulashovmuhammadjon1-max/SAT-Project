"""Atom and charge arithmetic for chemical equations written in the ``h*`` banks.

EK 4.2.A.2 is a *countable* claim: "any representation of a chemical change must
contain equal numbers of atoms of every element before and after the change
occurred. Equations thus demonstrate that mass and charge are conserved." So a
verifier for unit 4 does not have to take an author's word that an equation
balances -- it can count. This module is the counter.

THE WRITING CONVENTION THESE BANKS USE, and which this parser is built for:

    coefficient   a whole number, then ONE space:      ``2 H2O(l)``
    separator     a plus with a space on each side:    ``A + B gives C``
    arrow         the word ``gives``, never a glyph -- ``export_units.py`` does
                  not typeset Chemistry, so an arrow character reaches the
                  student raw
    phase         ``(s) (l) (g) (aq)``, stripped before parsing
    charge        written last, in the ordinary plain-text way: ``Ag+``,
                  ``Cl-``, ``Ca2+``, ``SO42-``. The trailing digits belong to
                  the CHARGE, not to the last element, so ``SO42-`` is one
                  sulfur, four oxygens and a charge of minus two.

Because a charge plus is never preceded by a space and a separator plus always
is, splitting a side on ``" + "`` cannot cut an ion in half.

``selftest()`` is the negative control for the parser itself: it runs equations
known to balance AND equations corrupted on purpose, and fails if the corrupted
ones are not rejected. A counter that says yes to everything is worse than no
counter, so nothing here is trusted until that has run.
"""
import re

_PHASE = re.compile(r"\((?:s|l|g|aq)\)")
# The charge magnitude is a SINGLE digit, never a run of them. Greedy digits
# read ``SO42-`` as a charge of minus forty-two instead of four oxygens and a
# charge of minus two, and the parser then reports a real equation unbalanced.
_CHARGE = re.compile(r"(\d?)([+-])$")
_COEFF = re.compile(r"^(\d+)\s+(\S.*)$")
_ELEMENT = re.compile(r"([A-Z][a-z]?)(\d*)")


def _merge(into, other, factor=1):
    for el, n in other.items():
        into[el] = into.get(el, 0) + n * factor
    return into


def _atoms(formula):
    """Element counts for a charge-free, phase-free formula, groups included."""
    counts, stack, i = {}, [], 0
    while i < len(formula):
        ch = formula[i]
        if ch == "(":
            stack.append(counts)
            counts, i = {}, i + 1
            continue
        if ch == ")":
            i += 1
            m = re.match(r"\d*", formula[i:])
            mult = int(m.group(0)) if m.group(0) else 1
            i += m.end()
            assert stack, f"unmatched closing parenthesis in {formula!r}"
            counts = _merge(stack.pop(), counts, mult)
            continue
        m = _ELEMENT.match(formula, i)
        assert m and m.start() == i, f"cannot read {formula[i:]!r} in {formula!r}"
        counts[m.group(1)] = counts.get(m.group(1), 0) + (int(m.group(2)) if m.group(2) else 1)
        i = m.end()
    assert not stack, f"unmatched opening parenthesis in {formula!r}"
    return counts


def species(text):
    """``('2 Ca(OH)2(aq)')`` to ``(coefficient, {element: count}, charge)``."""
    term = _PHASE.sub("", str(text)).strip()
    assert term, "an empty species term"
    m = _COEFF.match(term)
    coeff, term = (int(m.group(1)), m.group(2).strip()) if m else (1, term)
    c = _CHARGE.search(term)
    charge = 0
    if c:
        size = int(c.group(1)) if c.group(1) else 1
        charge = size if c.group(2) == "+" else -size
        term = term[:c.start()]
    assert term, f"a charge with no formula in {text!r}"
    return coeff, _atoms(term), charge


def side(text):
    """``('2 H2 + O2')`` to ``({element: total}, total charge)``."""
    totals, charge = {}, 0
    for part in str(text).split(" + "):
        coeff, atoms, q = species(part)
        _merge(totals, atoms, coeff)
        charge += coeff * q
    return totals, charge


def equation(text):
    """Split on the word ``gives`` and return both sides' totals."""
    halves = re.split(r"\s+gives\s+", str(text))
    assert len(halves) == 2, f"an equation must have exactly one 'gives': {text!r}"
    return side(halves[0]), side(halves[1])


def balanced(text):
    """True when every element and the total charge agree across ``gives``."""
    (la, lq), (ra, rq) = equation(text)
    return la == ra and lq == rq


def atom_balanced(text):
    (la, _), (ra, _) = equation(text)
    return la == ra


def charge_balanced(text):
    (_, lq), (_, rq) = equation(text)
    return lq == rq


def report(text):
    """A sentence naming what the counts are, for a check's return value."""
    (la, lq), (ra, rq) = equation(text)
    return (f"left {dict(sorted(la.items()))} charge {lq:+d}, "
            f"right {dict(sorted(ra.items()))} charge {rq:+d}")


# --------------------------------------------------------------- mechanisms

def step_species(text):
    """One elementary step as ``({species: count} left, {species: count} right)``.

    Species are kept as WRITTEN -- ``NO3``, ``ClO``, ``I-`` -- because what makes
    something an intermediate under EK 5.7.A.3 is the same species appearing on
    the product side of one step and the reactant side of another, which is a
    question about species, not about atoms.
    """
    halves = re.split(r"\s+gives\s+", str(text))
    assert len(halves) == 2, f"an elementary step must have one 'gives': {text!r}"
    out = []
    for half in halves:
        counts = {}
        for part in half.split(" + "):
            coeff, _, _ = species(part)
            name = _PHASE.sub("", part).strip()
            m = _COEFF.match(name)
            if m:
                name = m.group(2).strip()
            counts[name] = counts.get(name, 0) + coeff
        out.append(counts)
    return out[0], out[1]


def _net(steps):
    """Species left over once everything appearing on both sides has cancelled."""
    left, right = {}, {}
    for step in steps:
        ls, rs = step_species(step)
        _merge(left, ls)
        _merge(right, rs)
    net_l, net_r = {}, {}
    for name in set(left) | set(right):
        d = left.get(name, 0) - right.get(name, 0)
        if d > 0:
            net_l[name] = d
        elif d < 0:
            net_r[name] = -d
    return net_l, net_r


def mechanism_overall(steps):
    """The overall equation the steps add to, as ``(left, right)`` species counts."""
    return _net(steps)


def aligns_with(steps, overall):
    """EK 5.7.A.2: do the combined steps align with this overall equation?"""
    net_l, net_r = _net(steps)
    ls, rs = step_species(overall)
    return net_l == ls and net_r == rs


def intermediates(steps):
    """Species produced by an earlier step and consumed by a later one.

    EK 5.7.A.3: "produced by some elementary steps and consumed by others, such
    that it is present only while a reaction is occurring" -- the second clause
    is why a species surviving into the overall equation is excluded here.
    """
    net_l, net_r = _net(steps)
    parsed = [step_species(s) for s in steps]
    out = []
    for i, (_, rs) in enumerate(parsed):
        for name in rs:
            if name in net_l or name in net_r or name in out:
                continue
            if any(name in parsed[j][0] for j in range(i + 1, len(parsed))):
                out.append(name)
    return sorted(out)


def catalysts(steps):
    """Species consumed by an earlier step and regenerated by a later one.

    The mirror image of ``intermediates``: EK 5.11.A.2 has the catalyst
    frequently consumed in one step and regenerated in a subsequent one, and EK
    5.7.A.1 lists catalysts among a mechanism's components.
    """
    net_l, net_r = _net(steps)
    parsed = [step_species(s) for s in steps]
    out = []
    for i, (ls, _) in enumerate(parsed):
        for name in ls:
            if name in net_l or name in net_r or name in out:
                continue
            if any(name in parsed[j][1] for j in range(i + 1, len(parsed))):
                out.append(name)
    return sorted(out)


def selftest():
    """Positive AND negative controls for the parser itself."""
    ok = [
        "C3H8 + 5 O2 gives 3 CO2 + 4 H2O",
        "4 Fe + 3 O2 gives 2 Fe2O3",
        "AgNO3(aq) + NaCl(aq) gives AgCl(s) + NaNO3(aq)",
        "Ag+(aq) + Cl-(aq) gives AgCl(s)",
        "Ba2+(aq) + SO42-(aq) gives BaSO4(s)",
        "H3O+(aq) + OH-(aq) gives 2 H2O(l)",
        "Mg(s) + 2 H3O+(aq) gives Mg2+(aq) + H2(g) + 2 H2O(l)",
        "Zn(s) + Cu2+(aq) gives Zn2+(aq) + Cu(s)",
        "NaCl(s) gives Na+(aq) + Cl-(aq)",
        "H2O(l) gives H2O(g)",
        "Ca(OH)2(aq) + 2 HCl(aq) gives CaCl2(aq) + 2 H2O(l)",
    ]
    bad = [
        ("C3H8 + 4 O2 gives 3 CO2 + 4 H2O", "one oxygen molecule short"),
        ("4 Fe + 3 O2 gives 3 Fe2O3", "iron and oxygen both wrong on the right"),
        ("Ag+(aq) + Cl-(aq) gives AgCl2(s)", "a chlorine invented on the right"),
        ("Ag2+(aq) + Cl-(aq) gives AgCl(s)", "charge left over on the left"),
        ("Zn(s) + Cu2+(aq) gives Zn2+(aq) + Cu2+(aq)", "charge not conserved"),
    ]
    for eq in ok:
        assert balanced(eq), f"POSITIVE CONTROL FAILED: {eq!r} should balance -- {report(eq)}"
    for eq, why in bad:
        assert not balanced(eq), (
            f"NEGATIVE CONTROL FAILED: {eq!r} ({why}) was accepted -- {report(eq)}"
        )
    # Charge and atoms must be separable, or a check cannot say which failed.
    assert atom_balanced("Zn(s) + Cu2+(aq) gives Zn2+(aq) + Cu2+(aq)")
    assert not charge_balanced("Zn(s) + Cu2+(aq) gives Zn2+(aq) + Cu2+(aq)")
    assert not atom_balanced("C3H8 + 4 O2 gives 3 CO2 + 4 H2O")
    assert charge_balanced("C3H8 + 4 O2 gives 3 CO2 + 4 H2O")
    # The charge suffix must win over the last element's subscript.
    assert species("SO42-") == (1, {"S": 1, "O": 4}, -2), species("SO42-")
    assert species("2 Ca(OH)2") == (2, {"Ca": 1, "O": 2, "H": 2}, 0), species("2 Ca(OH)2")
    print(f"OK  h_equation: {len(ok)} balanced equations accepted, {len(bad)} corrupted "
          "ones rejected, atom and charge failures told apart.")


if __name__ == "__main__":
    selftest()
