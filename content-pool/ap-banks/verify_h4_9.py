"""Key audit for AP CHEMISTRY 4.9 Oxidation-Reduction (Redox) Reactions.

One ``(anchor, claim)`` per item, in module order; the anchor must appear in the
KEYED choice and in no distractor. Four table items and nine stem-data items are
recomputed from their own stimulus and asserted against the keyed choice.

WHAT THE KEYS REST ON
---------------------
Topic 4.9 has ONE essential knowledge statement:

    EK 4.9.A.1  Balanced chemical equations for redox reactions can be
                constructed from half-reactions.

and one learning objective, 4.9.A, which is a skill: represent a balanced redox
reaction equation using half-reactions. Every key here is either that skill
carried out on a printed pair of half-reactions, or one of the three facts the
construction rests on:

  electrons take the side that names the change  -- items 1, 2, 19, 22, 27
  a half-reaction balances atoms AND charge      -- items 7, 8, 9, 15, 19, 20, 25
  the electrons must be matched before adding    -- items 3, 4, 5, 6, 10, 11, 12,
                                                    13, 14, 16, 17, 18, 21, 23,
                                                    24, 26, 28, 29, 30

Item 12 chains to EK 4.7.A.4, which allows oxidation numbers to be assigned:
the six electrons in the dichromate half are accounted for by the change each
chromium atom undergoes. That is a different ask from anything in h4_7.py, which
never uses an oxidation number to explain an electron COUNT in a half-reaction.

NOTHING HERE REQUIRES RECALL. Every half-reaction a student must use is printed
in its own stem, including the H+ and H2O of the acidic-solution cases, so no key
depends on a standard potential, a memorised half-reaction, or a balancing
convention the CED does not state.

THE COURSE-WIDE EXCLUSION IS CHECKED: "the meaning of the terms 'reducing agent'
and 'oxidizing agent' will not be assessed on the AP Exam", so neither phrase may
appear in this module either.

NEGATIVE CONTROL: ``python3 verify_h4_9.py --selftest``.
"""
import math
import re
import sys

import h_chem_notation as hn
import h4_9 as M

LEFT = "Total charge on the reactant side"
RIGHT = "Total charge on the product side"
OXE = "Electrons in the oxidation half"
REDE = "Electrons in the reduction half"
OL = "Oxygen atoms on the reactant side"
OR_ = "Oxygen atoms on the product side"
NE = "Electrons appearing in it"
SIDE = "Side on which the electrons appear"

_BANNED_TERMS = [
    re.compile(r"(?<![a-z])reducing\s+agent", re.I),
    re.compile(r"(?<![a-z])oxidi[sz]ing\s+agent", re.I),
]


def excluded_terms(module, claims):
    texts = []
    for item in module.QUESTIONS:
        texts += hn.texts(item)
    texts += [c for pair in claims for c in pair]
    for text in texts:
        for pat in _BANNED_TERMS:
            hit = pat.search(text)
            assert not hit, (
                f"{module.TOPIC[0]}: {hit.group(0)!r} appears in {text[:70]!r}, but the "
                "CED's exclusion statement says that term will not be assessed"
            )
    print(f"OK  {module.TOPIC[0]} exclusions: neither excluded term appears in "
          f"{len(texts)} strings.")


# ------------------------------------------------------------ table questions

def q7(t, item):
    labs = hn.cg.labels(t)
    left = dict(zip(labs, hn.cg.col(t, LEFT)))
    right = dict(zip(labs, hn.cg.col(t, RIGHT)))
    ok = [l for l in labs if left[l] == right[l]]
    assert len(ok) == 2, f"balanced candidates: {ok}"
    assert ok[0].startswith("I:") and ok[1].startswith("III:"), \
        f"the balanced candidates should be the first and third, not {ok}"
    bad = [l for l in labs if l not in ok]
    assert all(left[l] > right[l] for l in bad), \
        "the two unbalanced rows should both carry the larger charge on the left"
    hn.keyed(item, "I and III only")
    return (f"two of the {len(labs)} candidates match across the two charge columns and "
            "the other two do not, which is the whole check")


def q17(t, item):
    labs = hn.cg.labels(t)
    ox = dict(zip(labs, hn.cg.col(t, OXE)))
    red = dict(zip(labs, hn.cg.col(t, REDE)))
    equal = [l for l in labs if ox[l] == red[l]]
    assert equal == ["Zinc with copper(II)"], f"pairs needing no scaling: {equal}"
    for l in labs:
        if l not in equal:
            assert math.lcm(int(ox[l]), int(red[l])) > max(ox[l], red[l]) or ox[l] != red[l], \
                f"{l} should need a multiplier on at least one half"
    hn.keyed(item, "zinc with copper(II) pair")
    return (f"exactly one of the {len(labs)} tabulated pairs already has equal electron "
            "counts in its two halves, so only that one needs no multiplier")


def q20(t, item):
    labs = hn.cg.labels(t)
    left = dict(zip(labs, hn.cg.col(t, OL)))
    right = dict(zip(labs, hn.cg.col(t, OR_)))
    excess = {l: left[l] - right[l] for l in labs}
    assert all(v > 0 for v in excess.values()), \
        f"every row must hold more oxygen on the reactant side; got {excess}"
    hn.keyed(item, "Water molecules on the product side")
    return (f"the reactant side carries {sorted(excess.values())} more oxygen atoms than "
            "the product side in the three rows, so oxygen must be added on the right")


def q24(t, item):
    labs = hn.cg.labels(t)
    n = dict(zip(labs, hn.cg.col(t, NE)))
    side = {r[0]: r[2] for r in t["rows"]}
    pairs = [(a, b) for i, a in enumerate(labs) for b in labs[i + 1:]
             if side[a] != side[b]]
    assert pairs, "no two rows put their electrons on opposite sides"
    best = min(pairs, key=lambda p: math.lcm(int(n[p[0]]), int(n[p[1]])))
    assert set(best) == {"Zn gives Zn2+ + 2 e-", "Cu2+ + 2 e- gives Cu"}, \
        f"the smallest-coefficient combinable pair is {best}"
    assert math.lcm(int(n[best[0]]), int(n[best[1]])) == 2, \
        "that pair should combine at two electrons"
    same_side = [(a, b) for i, a in enumerate(labs) for b in labs[i + 1:]
                 if side[a] == side[b]]
    assert same_side, "the 'both on the product side' distractor must name a real pair"
    hn.keyed(item, "zinc half with the copper(II) half")
    return ("among the pairs whose electrons sit on opposite sides, the smallest common "
            "electron count is two, and it belongs to the zinc and copper rows")


TABLE_CHECKS = {7: q7, 17: q17, 20: q20, 24: q24}


# --------------------------------------------------------- stem-data questions

def a4(item):
    common = math.lcm(3, 2)
    hn.keyed(item, f"aluminum half by {common // 3} and the copper half by {common // 2}")
    return f"the smallest common multiple of 3 and 2 is {common}, so the factors are 2 and 3"


def a6(item):
    hn.keyed(item, str(math.lcm(3, 2)))
    return f"the electrons lost and gained must both equal {math.lcm(3, 2)}"


def a9(item):
    left = (-1) + 8 * (+1) + 5 * (-1)
    right = +2
    assert left == right, f"the permanganate half does not balance: {left} against {right}"
    hn.keyed(item, "gives positive two")
    return (f"the reactant side sums to {left:+d} once the five electrons are counted, "
            f"matching the {right:+d} on the manganese ion")


def a10(item):
    n = math.lcm(5, 1) // 1
    hn.keyed(item, str(n))
    return f"five electrons in the permanganate half against one per iron gives {n} iron ions"


def a12(item):
    # Cr2O7 2-: seven oxygens at -2 in an ion of charge -2.
    total_cr = -2 - 7 * (-2)
    per_cr = total_cr // 2
    assert per_cr == 6, f"each chromium computes to {per_cr}, not positive six"
    drop = per_cr - 3
    assert 2 * drop == 6, f"two chromium atoms falling by {drop} do not give six electrons"
    hn.keyed(item, "falls from positive six to positive three")
    return (f"seven oxygens at negative two in a minus two ion leave {total_cr} for two "
            f"chromium atoms, so each is plus {per_cr} and each falls {drop} to plus three")


def a13(item):
    hn.keyed(item, str(math.lcm(6, 1)))
    return f"six electrons per dichromate against one per iron gives {math.lcm(6, 1)} iron ions"


def a23(item):
    n = 3 * 2      # three copper atoms, each going from 0 to +2
    hn.keyed(item, str(n))
    return f"three copper atoms each releasing two electrons transfer {n} in total"


def a26(item):
    n = math.lcm(2, 1) // 1
    hn.keyed(item, str(n))
    return f"two electrons from the zinc against one per silver ion needs {n} silver ions"


def a29(item):
    net = 4 - 1
    hn.keyed(item, f"{'Three' if net == 3 else net} water molecules on the reactant side")
    return f"four on the left against one on the right cancels to {net} on the left and none on the right"


ARITH = {4: a4, 6: a6, 9: a9, 10: a10, 12: a12, 13: a13, 23: a23, 26: a26, 29: a29}

CLAIMS = [
 ("On the product side",
  "EK 4.9.A.1 builds balanced equations from half-reactions, and a half-reaction records what one species does with electrons. Oxidation is loss, so the electrons are written among the products."),
 ("Cu2+ + 2 e- gives Cu",
  "Reduction is the gain of electrons, so they appear among the reactants of the half-reaction. Only one of the five candidates writes them on that side."),
 ("Zn + Cu2+ gives Zn2+ + Cu",
  "EK 4.9.A.1 constructs the balanced equation from the half-reactions. Both halves already involve two electrons, so they add directly, the electrons cancel, and neither species needs a coefficient."),
 ("aluminum half by 2 and the copper half by 3",
  "Recomputed in a4. EK 4.9.A.1's construction requires the electrons lost to equal the electrons gained, and the smallest number both three and two divide is six."),
 ("2 Al + 3 Cu2+ gives 2 Al3+ + 3 Cu",
  "Recomputed in a4's factors. Scaling each half to six electrons puts two aluminum atoms with three copper(II) ions, and no electrons survive the addition."),
 ("6",
  "Recomputed in a6. EK 4.9.A.1 requires the two halves to be scaled until the electrons lost equal the electrons gained, which is the smallest common multiple of the two counts."),
 ("I and III only",
  "Recomputed in q7 above from the table's two charge columns. EK 4.9.A.1 makes half-reactions the building blocks, and a half-reaction is not usable until its charge balances as well as its atoms."),
 ("charge does not balance",
  "EK 4.9.A.1 makes a balanced half-reaction the building block. One electron leaves a doubly charged ion one unit short of neutral, so the equation as written is not usable."),
 ("gives positive two",
  "Recomputed in a9. EK 4.9.A.1 requires atoms and charge to balance in a half-reaction, and the electrons carry negative charge into that sum."),
 ("5",
  "Recomputed in a10. EK 4.9.A.1 constructs the balanced equation by scaling the halves to a common electron count; the permanganate half takes five and each iron(II) releases one."),
 ("MnO4- + 5 Fe2+ + 8 H+ gives Mn2+ + 5 Fe3+ + 4 H2O",
  "The iron half multiplied by five matches the permanganate half's five electrons, so the electrons cancel on adding, and the hydrogen and oxygen counts come from the printed half-reaction."),
 ("falls from positive six to positive three",
  "Recomputed in a12 from the convention stated in the stem, chaining EK 4.7.A.4's oxidation numbers to EK 4.9.A.1's electron count: two chromium atoms each falling three units account for the six electrons written into the half-reaction."),
 ("6",
  "Recomputed in a13. EK 4.9.A.1 requires the electrons released by the oxidation half to equal those taken in by the reduction half; the dichromate half takes six and each iron(II) releases one."),
 ("every electron released by one species is taken up by the other",
  "EK 4.9.A.1 constructs the balanced equation from half-reactions, which are two accounts of a single transfer. Once scaled to the same count, the electrons on opposite sides are the same electrons."),
 ("no electrons appear",
  "EK 4.9.A.1 builds the overall equation from half-reactions each balanced for atoms and charge; adding two balanced expressions preserves both, and the matched electrons cancel out of the result."),
 ("Cu gives Cu2+ + 2 e-, and 2 Ag+ + 2 e- gives 2 Ag",
  "EK 4.9.A.1 relates a balanced equation and its half-reactions by construction. Copper releases two electrons and the two silver ions take one each, and the two halves add back to the given equation."),
 ("zinc with copper(II) pair",
  "Recomputed in q17 above. EK 4.9.A.1 requires the electrons lost to equal the electrons gained before the halves are added, so only a pair whose tabulated counts already match needs no multiplier."),
 ("Sn2+ + 2 Fe3+ gives Sn4+ + 2 Fe2+",
  "EK 4.9.A.1 scales the halves to a common electron count before adding. The tin half releases two and each iron(III) ion takes one, so doubling the iron half makes the electrons cancel."),
 ("negative two on each side once the electrons are counted",
  "EK 4.9.A.1 makes a usable half-reaction one balanced for both atoms and charge; two iodine atoms appear on each side and the two electrons carry the charge the two iodide ions brought."),
 ("Water molecules on the product side",
  "Recomputed in q20 above. EK 4.9.A.1 requires the atoms of every element to balance in the half-reaction, and every tabulated row holds more oxygen on the reactant side."),
 ("added before being scaled to a common electron count",
  "EK 4.9.A.1's construction requires the electrons lost to equal the electrons gained. Unequal counts surviving into the sum are exactly what is left when that scaling step has been skipped."),
 ("H2 gives 2 H+ + 2 e-",
  "Oxidation writes the electrons among the products, and EK 4.9.A.1 requires atoms and charge to balance: two hydrogen atoms on each side, and two positive charges offset by two electrons."),
 ("6",
  "Recomputed in a23. EK 4.9.A.1 relates the balanced equation to the half-reactions behind it, and three copper atoms each losing two electrons is the count the reduction half must have taken in."),
 ("zinc half with the copper(II) half",
  "Recomputed in q24 above. EK 4.9.A.1 requires one half to release what the other takes in, so the electrons must sit on opposite sides, and equal counts avoid any multiplier."),
 ("written with the electrons it loses or gains",
  "EK 4.9.A.1 has balanced redox equations constructed from half-reactions, which is possible only if each half-reaction is a complete balanced account of what one species does with electrons."),
 ("2",
  "Recomputed in a26. EK 4.9.A.1 requires the electrons gained to equal the electrons lost, and zinc releases two while each silver ion takes one."),
 ("move to the other side of the equation, keeping the same coefficient",
  "A reversed half-reaction describes the same species doing the opposite thing with the same electrons, so only the side changes. EK 4.9.A.1's construction relies on being able to write either direction."),
 ("Cu gives Cu2+ + 2 e-",
  "EK 4.9.A.1 builds the overall equation by matching electrons released against electrons taken in. Two halves that both write their electrons as products leave those electrons in the sum."),
 ("Three water molecules on the reactant side",
  "Recomputed in a29. EK 4.9.A.1 yields one balanced equation from the sum of the halves, and a species present on both sides is in excess on one of them by the difference."),
 ("electron count and the charge to be accounted for explicitly",
  "EK 4.9.A.1 states that balanced chemical equations for redox reactions can be constructed from half-reactions. Writing each half separately makes the electron count an explicit quantity that has to match."),
]


def _wreck_charge(mod, cl):
    """Module-specific control: make a third candidate balance."""
    t = mod.QUESTIONS[6]["table"]
    mod.QUESTIONS[6]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], r[1], "+1"] if r[0].startswith("II:") else list(r)
              for r in t["rows"]])


def _wreck_electrons(mod, cl):
    """Module-specific control: make a second pair need no scaling."""
    t = mod.QUESTIONS[16]["table"]
    mod.QUESTIONS[16]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], r[1], "3"] if r[0].startswith("Aluminum") else list(r)
              for r in t["rows"]])


def _wreck_oxygen(mod, cl):
    """Module-specific control: put the excess oxygen on the product side."""
    t = mod.QUESTIONS[19]["table"]
    mod.QUESTIONS[19]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], "0", "4"] if r[0].startswith("MnO4-") else list(r)
              for r in t["rows"]])


def _wreck_stem_number(mod, cl):
    """Module-specific control: key a scaling item to the wrong multiple."""
    mod.QUESTIONS[5]["choices"][0] = "7"


def _reintroduce_excluded_term(mod, cl):
    mod.QUESTIONS[2]["why"] += " Zinc is the reducing agent in this reaction."


def _selftest():
    hn.selftest(M, CLAIMS, TABLE_CHECKS, arith=ARITH,
                extra=[("a charge cell corrupted", _wreck_charge),
                       ("an electron-count cell corrupted", _wreck_electrons),
                       ("an oxygen-count cell corrupted", _wreck_oxygen),
                       ("a key edited away from its recomputed value", _wreck_stem_number)])
    mod = hn._mutant(M)
    _reintroduce_excluded_term(mod, CLAIMS)
    try:
        excluded_terms(mod, CLAIMS)
    except AssertionError as exc:
        print(f"  control OK  an excluded term reintroduced: {str(exc)[:88]}")
    else:
        raise SystemExit("CONTROL FAILED: an excluded term was not caught")


if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

excluded_terms(M, CLAIMS)
hn.audit(M, CLAIMS, TABLE_CHECKS, arith=ARITH)
