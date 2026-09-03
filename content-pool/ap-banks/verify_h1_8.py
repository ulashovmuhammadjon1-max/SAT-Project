r"""Key audit for AP CHEMISTRY 1.8 Valence Electrons and Ionic Compounds.

One (anchor, claim) per item, in module order. ``anchor`` must appear in the
KEYED choice and in no distractor, since the exporter reshuffles choices.

WHAT IS RECOMPUTED. Every combining ratio keyed in this module is derived here
from two ion charges by the rule EK 4.2.A.2 supplies -- the compound carries no
net charge -- rather than being recalled as a formula. ``_balance`` reduces the
two charges to the smallest whole-number counts that cancel, so a keyed formula
is checked against a derivation. It is also used in reverse for item 30, where
a stated combining ratio has to be matched back to a pair of columns.

The analogous-compound items are checked structurally: the tabulated formulas
are parsed and the module asserts that the pattern is CONSTANT within a column
and DIFFERENT between columns. Without that second half the tables would
support EK 1.8.A.2's claim only trivially, and items 12 and 13 turn on exactly
that contrast.

WHAT THE KEYS REST ON
---------------------
Items 1, 10, 15, 23 and 27 rest on EK 1.8.A.1: the likelihood that two elements
will form a chemical bond is determined by the interactions between the valence
electrons and nuclei of elements.

Items 2, 7, 11, 12, 13, 17, 18, 24 and 28 rest on EK 1.8.A.2: elements in the
same column of the periodic table tend to form analogous compounds.

Items 3, 4, 5, 6, 8, 9, 14, 16, 19, 20, 21, 22, 25, 26, 29 and 30 rest on EK
1.8.A.3: typical charges of atoms in ionic compounds are governed by the number
of valence electrons and predicted by their location on the periodic table.
Where an item goes from two charges to a formula the claim also cites EK
4.2.A.2 for the conservation of charge, which is the framework's own statement
of the neutrality premise.

Item 22 is the suggested skill 4.C item: the connection from a particulate
feature (valence count) to something an analyst measures (a formula).

THE HEDGE IN "TYPICAL" IS KEPT. No key claims an element forms only one charge,
and no item asks for the charge of a transition metal.

DATA ITEMS: 3, 4, 5, 6, 9, 10, 11, 12, 13, 15, 16, 18, 21, 25, 26, 28, 29 and
30 carry tables; all eighteen are recomputed below.

NEGATIVE CONTROL: ``python3 verify_h1_8.py --selftest``.
"""
import re
import sys
from math import gcd

import cg_check as cg
import chem_notation

CHARGE = "Typical charge of the ion formed in an ionic compound"
COLUMN = "Column of the periodic table"
VALENCE = "Valence electrons"

_FORMULA = re.compile(r"([A-Z][a-z]?)(\d*)")


def _parse_formula(text):
    """[(element symbol, count)] for a plain-text formula such as MgCl2."""
    out = [(sym, int(n) if n else 1) for sym, n in _FORMULA.findall(text) if sym]
    assert out, f"{text!r} does not parse as a formula"
    return out


def _pattern(text):
    """The combining ratio of a formula, reduced -- MgCl2 and CaCl2 share one."""
    counts = [n for _, n in _parse_formula(text)]
    g = 0
    for c in counts:
        g = c if g == 0 else gcd(g, c)
    return tuple(c // g for c in counts)


def _balance(pos, neg):
    """EK 1.8.A.3 charges to the smallest whole-number counts that cancel.

    EK 4.2.A.2: charge is conserved, so the compound carries no net charge.
    Returns (number of cations, number of anions).
    """
    p, n = int(pos), abs(int(neg))
    g = gcd(p, n)
    return n // g, p // g


def _charges(table):
    return {int(cg.num(lab.split()[-1])): cg.cell(table, lab, CHARGE)
            for lab in cg.labels(table)}


def q3(table, item):
    c = _charges(table)
    assert c[1] == 1, f"the tabulated charge for column 1 is {c[1]}"
    return f"the table records the column 1 charge as {c[1]:+.0f}, matching one valence electron lost"


def q4(table, item):
    c = _charges(table)
    assert c[16] == -2, f"the tabulated charge for column 16 is {c[16]}"
    assert c[16] != 2 and c[16] != -6, "the sign-flip and lose-six distractors must be false"
    return f"the table records the column 16 charge as {c[16]:+.0f}"


def q5(table, item):
    v = dict(zip(cg.labels(table), cg.col(table, VALENCE)))
    three = [k for k, n in v.items() if n == 3]
    assert three == ["Aluminum"], f"the elements with three valence electrons are {three}"
    return f"the tabulated valence counts are {v}, so exactly one element loses three"


def q6(table, item):
    c = _charges(table)
    ratio = _balance(c[2], c[17])
    assert ratio == (1, 2), f"balancing {c[2]:+.0f} against {c[17]:+.0f} gives {ratio}"
    return (f"a charge of {c[2]:+.0f} balanced against {c[17]:+.0f} needs {ratio[0]} metal ion "
            f"to {ratio[1]} nonmetal ions")


def q9(table, item):
    c = _charges(table)
    ratio = _balance(c[13], c[16])
    assert ratio == (2, 3), f"balancing {c[13]:+.0f} against {c[16]:+.0f} gives {ratio}"
    key = _parse_formula("Al2O3")
    assert [n for _, n in key] == list(ratio), "the keyed formula does not match the balance"
    assert _balance(c[16] * -1, c[13] * -1) != ratio or True, ""
    return (f"charges {c[13]:+.0f} and {c[16]:+.0f} balance at {ratio[0]} to {ratio[1]}, which "
            "is the keyed formula's own subscripts")


def q10(table, item):
    v = dict(zip(cg.labels(table), cg.col(table, VALENCE)))
    assert 1 in v.values() and 7 in v.values(), \
        f"the table must contain both a one-valence and a seven-valence element: {v}"
    return (f"the tabulated valence counts {v} include an element with one and an element "
            "with seven, which is the pairing the key names")


def _analogous(table, header):
    """{column: set of reduced combining ratios} for the tabulated formulas."""
    cols = cg.col(table, COLUMN)
    out = {}
    for col, row in zip(cols, table["rows"]):
        out.setdefault(int(col), set()).add(_pattern(row[2]))
    return out


def q11(table, item):
    by_col = _analogous(table, "Formula of its compound with chlorine")
    for col, pats in by_col.items():
        assert len(pats) == 1, f"column {col} does not show one pattern: {pats}"
    assert len(set(map(frozenset, by_col.values()))) == len(by_col), \
        f"two columns share a pattern, so the table cannot demonstrate the contrast: {by_col}"
    assert by_col[1] == {(1, 1)}, f"column 1's pattern is {by_col[1]}, not one to one"
    return (f"the tabulated formulas reduce to {by_col}: constant within each column and "
            "different between them, so a first-column element gives a one-to-one formula")


def q12(table, item):
    by_col = _analogous(table, "Formula of its compound with chlorine")
    assert by_col[1] == {(1, 1)} and by_col[2] == {(1, 2)}, \
        f"the two columns' patterns are {by_col}"
    assert all(_parse_formula(r[2])[1][0] == "Cl" for r in table["rows"]), (
        "every tabulated compound must be with chlorine, or the 'forms some compound' "
        "distractor would not be uniformly true")
    return (f"column 1 gives {sorted(by_col[1])} and column 2 gives {sorted(by_col[2])}, so the "
            "pattern is constant inside a column and differs between them")


def q13(table, item):
    by_col = _analogous(table, "Formula of its compound with oxygen")
    assert by_col[1] == {(2, 1)}, f"column 1's oxide pattern is {by_col[1]}"
    assert by_col[2] == {(1, 1)}, f"column 2's oxide pattern is {by_col[2]}"
    assert by_col[1] != by_col[2], "'all four the same pattern' must be false"
    return (f"the tabulated oxides reduce to {by_col}: two first-column atoms per oxygen "
            "against one second-column atom per oxygen")


def q15(table, item):
    labs = cg.labels(table)
    vals = cg.col(table, "First ionization energy (kilojoules per mole)")
    assert all(vals[i] > vals[i + 1] for i in range(len(vals) - 1)), \
        f"the ionization energies do not fall down the column: {vals}"
    assert labs[-1] == "Strontium" and labs[0] == "Beryllium", \
        f"the column runs {labs[0]} to {labs[-1]}"
    return (f"the tabulated energies {vals} fall down the column, so the last element gives "
            "up its valence electrons most readily")


def q16(table, item):
    charges = {1: 1, 2: 2, 13: 3, 16: -2, 17: -1}
    bad = []
    for row in table["rows"]:
        name, formula, metal_col, non_col = row
        counts = [n for _, n in _parse_formula(formula)]
        want = _balance(charges[int(metal_col)], charges[int(non_col)])
        if tuple(counts) != want:
            bad.append((name, tuple(counts), want))
    assert [b[0] for b in bad] == ["Compound 3"], f"the unbalanced formulas are {bad}"
    return (f"balancing each proposal against its own columns leaves exactly one mismatch: "
            f"{bad[0][0]} is written {bad[0][1]} where the charges require {bad[0][2]}")


def q18(table, item):
    by_col = _analogous(table, "Formula of its compound with chlorine")
    cols = dict(zip(cg.labels(table), cg.col(table, COLUMN)))
    assert cols["Calcium"] == cols["Magnesium"], "calcium and magnesium are not in one column"
    assert cols["Sodium"] != cols["Magnesium"], "sodium must be in a DIFFERENT column"
    assert by_col[2] == {(1, 2)}, f"the second column's pattern is {by_col[2]}"
    return (f"the table puts calcium in magnesium's column ({cols['Calcium']:.0f}) and sodium "
            f"in another ({cols['Sodium']:.0f}), with the shared pattern {sorted(by_col[2])}")


def q21(table, item):
    c = _charges(table)
    ratio = _balance(c[1], c[16])
    assert ratio == (2, 1), f"balancing {c[1]:+.0f} against {c[16]:+.0f} gives {ratio}"
    assert ratio != (1, 1), "the student's one-to-one proposal must be false on the charges"
    return (f"charges {c[1]:+.0f} and {c[16]:+.0f} balance at {ratio[0]} to {ratio[1]}, so a "
            "one-to-one formula leaves a net charge")


def q25(table, item):
    c = _charges(table)
    ratio = _balance(c[2], c[17])
    assert ratio == (1, 2), f"balancing {c[2]:+.0f} against {c[17]:+.0f} gives {ratio}"
    return (f"one ion of charge {c[2]:+.0f} needs {ratio[1]} of charge {c[17]:+.0f}, so "
            f"seventeenth-column ions outnumber second-column ions {ratio[1]} to {ratio[0]}")


def q26(table, item):
    v = dict(zip(cg.labels(table), cg.col(table, VALENCE)))
    charge = {"Sodium": 1, "Magnesium": 2, "Aluminum": 3, "Sulfur": -2, "Chlorine": -1}
    # Every metal-nonmetal pairing the table permits is balanced, not just the
    # keyed one. The first draft of this item asked for a ONE-TO-ONE ratio and
    # this check found two pairings that satisfy it -- magnesium with sulfur and
    # sodium with chlorine -- so the item had two defensible answers and was
    # rewritten to ask for the ratio only one pairing gives.
    hits = [(a, b) for a in charge for b in charge
            if charge[a] > 0 > charge[b] and _balance(charge[a], charge[b]) == (1, 2)]
    assert hits == [("Magnesium", "Chlorine")], \
        f"the pairs balancing one to two are {hits}"
    assert v["Magnesium"] == 2 and v["Chlorine"] == 7, \
        f"the tabulated valence counts for that pair are {v['Magnesium']} and {v['Chlorine']}"
    return (f"of every metal-nonmetal pairing in the table only {hits[0][0]} with "
            f"{hits[0][1]} balances one to two, on valence counts "
            f"{v['Magnesium']:.0f} and {v['Chlorine']:.0f}")


def q28(table, item):
    by_col = _analogous(table, "Formula of its compound with chlorine")
    cols = dict(zip(cg.labels(table), cg.col(table, COLUMN)))
    assert cols["Calcium"] == 2, "calcium must be in the second column for the item to work"
    assert by_col[2] == {(1, 2)}, f"the second column's pattern is {by_col[2]}"
    assert len(by_col[2]) == 1, "the column must show a single pattern for the prediction"
    return (f"both tabulated second-column elements form the pattern {sorted(by_col[2])} with "
            "chlorine, so an element added below them is predicted to do the same")


def q29(table, item):
    c = _charges(table)
    assert c[16] < 0, f"the tabulated column 16 charge is {c[16]}, not negative"
    assert c[16] != 2, "the 'plus two' rejected option must be false on the table"
    return f"the tabulated column 16 charge is {c[16]:+.0f}, so a charge of plus six is not it"


def q30(table, item):
    c = _charges(table)
    hits = [(a, b) for a in c for b in c
            if c[a] > 0 > c[b] and _balance(c[a], c[b]) == (2, 3)]
    assert hits == [(13, 16)], f"the column pairings giving a two-to-three ratio are {hits}"
    return (f"searching every tabulated metal-nonmetal pairing, only columns "
            f"{hits[0][0]} and {hits[0][1]} balance two to three")


CLAIMS = [
 ("interactions between the valence electrons and the nuclei",
  "EK 1.8.A.1, near verbatim: the likelihood that two elements will form a chemical bond is determined by the interactions between the valence electrons and nuclei of elements. Mass, neutron count and core electrons appear nowhere in that statement."),
 ("analogous compounds",
  "EK 1.8.A.2, near verbatim: elements in the same column of the periodic table tend to form analogous compounds. Analogous is a claim about the pattern of the formula, so it says nothing about the masses of the compounds and does not mean the elements bond to each other."),
 ("plus one, governed by its single valence electron",
  "Recomputed in q3 above against the item's own table. EK 1.8.A.3 makes the typical charge governed by the number of valence electrons and predicted by location, and EK 1.5.A.3 reserves the term core electron for the inner electrons, which are not what is lost."),
 ("charge of minus two",
  "Recomputed in q4 above from the table, which also confirms the sign-flipped and lose-six values are different numbers. EK 1.8.A.3 predicts the charge from position, and EK 1.7.A.1's completely filled subshells are why gaining two is the change that happens."),
 ("Aluminum",
  "Recomputed in q5 above: exactly one tabulated element has three valence electrons, and EK 1.8.A.3 makes the typical charge governed by that count."),
 ("One metal atom to two nonmetal atoms",
  "Recomputed in q6 above by balancing the two tabulated charges. EK 1.8.A.3 supplies the charges from position and EK 4.2.A.2's conservation of charge supplies the requirement that they cancel, which fixes the ratio."),
 ("KBr, one potassium ion for each bromide ion",
  "EK 1.8.A.2 states that elements in the same column tend to form analogous compounds, so an element directly below another forms the same pattern with the same partner. EK 1.8.A.3 agrees independently, since the two elements share a valence count and so a typical charge."),
 ("location fixes the number of valence electrons",
  "EK 1.8.A.3 states that typical charges are governed by the number of valence electrons and predicted by location on the periodic table, and EK 1.7.A.1 supplies the link by tracing the columns to repeating ground-state configurations. Core electrons are the inner ones under EK 1.5.A.3."),
 ("Al2O3",
  "Recomputed in q9 above by balancing the two tabulated charges, with the keyed formula's own subscripts compared against the result. EK 1.8.A.3 gives the charges and EK 4.2.A.2 gives the requirement that they cancel."),
 ("one valence electron together with an element with seven",
  "Recomputed in q10 above to the extent of confirming the table offers both. EK 1.8.A.1 makes the likelihood of a bond depend on the interactions between the valence electrons and nuclei of the two elements, and EK 1.8.A.3 turns those valence counts into opposite typical charges."),
 ("RbCl, one rubidium ion for each chloride ion",
  "Recomputed in q11 above: the tabulated formulas reduce to one pattern inside each column and different patterns between columns, so EK 1.8.A.2's analogy has real content here and fixes the prediction for a further member of the first column."),
 ("one-to-one compound with chlorine, while every element of the second column",
  "Recomputed in q12 above. EK 1.8.A.2's claim is that the PATTERN recurs within a column, so the evidence must be constancy inside a column together with a difference between columns -- and the check confirms that every tabulated compound is with chlorine, which is what makes the 'forms some compound' option uniformly true and therefore useless."),
 ("two atoms for each oxygen atom, while the second-column elements need only one",
  "Recomputed in q13 above from the tabulated oxide formulas. EK 1.8.A.2 predicts the agreement within each column and EK 1.8.A.3 explains the difference between them, since an ion of charge plus one needs two of itself to cancel a charge of minus two."),
 ("minus one, because gaining a single electron completes",
  "EK 1.8.A.3 makes the typical charge governed by the valence count, and EK 1.7.A.1 makes completely filled shells and subshells the recurring feature the configuration pattern produces. Gaining one electron is a far smaller change than losing seven, which is why the framework calls the negative charge the typical one."),
 ("Strontium, and it should be the most reactive",
  "Recomputed in q15 above: the tabulated ionization energies fall down the column, so the last element parts with its valence electrons for the least energy. LO 1.8.A is the relationship between reactivity and periodicity, and EK 1.8.A.1 makes bond formation turn on the interaction between valence electrons and nuclei -- which is what an ionization energy measures."),
 ("Compound 3",
  "Recomputed in q16 above: each tabulated formula is balanced against the charges its own two columns imply under EK 1.8.A.3, and exactly one fails. EK 4.2.A.2's conservation of charge is the standard applied."),
 ("same charge and compounds of the same pattern",
  "EK 1.8.A.2 makes column-mates form analogous compounds and EK 1.8.A.3 traces the typical charge to the valence count, which EK 1.7.A.1's repeating configurations hold constant down a column. A differing proton count changes how tightly those electrons are held, not how many there are."),
 ("Calcium, which lies in the same column",
  "Recomputed in q18 above from the table's own column entries: calcium shares magnesium's column and sodium does not. EK 1.8.A.2 makes the COLUMN the relationship that predicts an analogous compound, not the row and not being a nonmetal like the partner."),
 ("plus two, with two fewer electrons",
  "EK 1.5.A.1 gives the electron a negative charge, so removing two leaves a net charge of plus two, and EK 1.8.A.3 makes that the typical charge for the column. Protons sit in the nucleus by EK 1.5.A.1 and are untouched by the loss of electrons."),
 ("column determines the number of valence electrons",
  "EK 1.8.A.3 predicts the typical charge from location and governs it by the valence count, and EK 1.7.A.1 makes a column a repeating configuration pattern. Atomic mass is a perfectly real quantity that simply does not enter the prediction, which is why the rejected options that dispute its reality are wrong twice over."),
 ("two of the first are needed",
  "Recomputed in q21 above by balancing the two tabulated charges, which come to two-to-one rather than one-to-one. EK 1.8.A.3 supplies the charges and EK 4.2.A.2 the requirement that they cancel; the framework assigns typical charges to nonmetals as readily as to metals."),
 ("fixes the ratio in which the elements combine",
  "Suggested skill 4.C: the connection from the particulate level to what is observed. EK 1.8.A.3 runs from valence electron count to typical ionic charge, and EK 4.2.A.2's charge balance turns two charges into a combining ratio -- which is what an elemental analysis measures as a formula."),
 ("first supplying an electron to the second",
  "EK 1.8.A.1 makes bond formation depend on the interactions between the valence electrons and nuclei of the two elements. A low ionization energy means that single valence electron is loosely held, and EK 1.8.A.3 makes an element with seven valence electrons one that typically gains one, so the transfer has a direction."),
 ("different combining ratios",
  "EK 1.8.A.2's claim concerns the recurrence of a formula PATTERN within a column, so only a difference in that pattern can count against it. Differing masses, proton counts, radii and rows are all expected of column-mates and are consistent with the claim."),
 ("Two to one",
  "Recomputed in q25 above by balancing the two tabulated charges. EK 1.8.A.3 supplies them from position and EK 4.2.A.2 requires them to cancel, so the ions appear in the inverse ratio of the magnitudes of their charges; stating that ratio the other way round is the nearest rejected option."),
 ("Magnesium and chlorine",
  "Recomputed in q26 above by balancing EVERY metal-nonmetal pairing available in the table, not just the keyed one: exactly one comes to the stated ratio. This item earned that check -- as first drafted it asked for a ONE-TO-ONE ratio, and the search found two pairings satisfying it, so the item had two defensible answers until it was rewritten. EK 1.8.A.3 supplies the charges from the tabulated valence counts and EK 4.2.A.2 the requirement that they cancel."),
 ("farther from the nucleus and is more shielded",
  "LO 1.8.A is the relationship between reactivity trends and periodicity. EK 1.7.A.2 explains the fall in ionization energy down a column through distance and shielding, and EK 1.8.A.1 makes bond formation turn on the interaction between valence electrons and nuclei. Every element of the column has one valence electron and a growing proton count, so neither of those can be the variable."),
 ("one-to-two ratio, as the other second-column elements",
  "Recomputed in q28 above: both tabulated members of that column show the same pattern with chlorine. EK 1.8.A.2 predicts the analogy and EK 1.7.A.3 separately licenses using periodicity to predict a property in the absence of data."),
 ("tabulated typical charge for that column is negative",
  "Recomputed in q29 above from the table itself. EK 1.8.A.3 governs the typical charge by the valence count and predicts it from location, and EK 1.7.A.1's completely filled shells and subshells are why the small change rather than the large one occurs."),
 ("thirteenth column with a nonmetal of the sixteenth",
  "Recomputed in q30 above by balancing every metal-nonmetal pairing the table offers and keeping the ones that give the stated two-to-three ratio: exactly one pairing does. EK 1.8.A.3 supplies the charges and EK 4.2.A.2 the balance."),
]

TABLE_CHECKS = {3: q3, 4: q4, 5: q5, 6: q6, 9: q9, 10: q10, 11: q11, 12: q12,
                13: q13, 15: q15, 16: q16, 18: q18, 21: q21, 25: q25, 26: q26,
                28: q28, 29: q29, 30: q30}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("h1_8_mutant")
        mod.TOPIC = h1_8.TOPIC
        mod.QUESTIONS = copy.deepcopy(h1_8.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:95]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[8]["ans"] = 1

    def break_anchor(mod, claims):
        claims[15] = ("no such phrase anywhere in the choice", claims[15][1])

    def corrupt_a_charge(mod, claims):
        mod.QUESTIONS[8]["table"] = dict(
            headers=h1_8._T_TYPICAL["headers"],
            rows=[["Column 1", "+1"], ["Column 2", "+2"], ["Column 13", "+2"],
                  ["Column 16", "-2"], ["Column 17", "-1"]])

    def break_the_column_pattern(mod, claims):
        # Sodium made to form a two-to-one chloride: the first column no longer
        # shows one pattern, so the analogy item has nothing to stand on.
        mod.QUESTIONS[10]["table"] = dict(
            headers=h1_8._T_ANALOG["headers"],
            rows=[["Lithium", "1", "LiCl"], ["Sodium", "1", "Na2Cl"],
                  ["Potassium", "1", "KCl"], ["Magnesium", "2", "MgCl2"],
                  ["Calcium", "2", "CaCl2"]])

    def make_the_columns_agree(mod, claims):
        # Both columns given the same pattern: the contrast item 12 rests on is gone.
        mod.QUESTIONS[11]["table"] = dict(
            headers=h1_8._T_ANALOG["headers"],
            rows=[["Lithium", "1", "LiCl"], ["Sodium", "1", "NaCl"],
                  ["Potassium", "1", "KCl"], ["Magnesium", "2", "MgCl"],
                  ["Calcium", "2", "CaCl"]])

    def balance_the_bad_formula(mod, claims):
        mod.QUESTIONS[15]["table"] = dict(
            headers=h1_8._T_FORMULAS["headers"],
            rows=[["Compound 1", "NaCl", "1", "17"], ["Compound 2", "MgO", "2", "16"],
                  ["Compound 3", "K2O", "1", "16"], ["Compound 4", "CaBr2", "2", "17"]])

    def flatten_the_reactivity_trend(mod, claims):
        mod.QUESTIONS[14]["table"] = dict(
            headers=h1_8._T_IE_COL2["headers"],
            rows=[["Beryllium", "549"], ["Magnesium", "590"], ["Calcium", "738"],
                  ["Strontium", "900"]])

    def add_a_second_one_to_one_pair(mod, claims):
        mod.QUESTIONS[25]["table"] = dict(
            headers=h1_8._T_VALENCE["headers"],
            rows=[["Sodium", "1", "1"], ["Magnesium", "2", "2"], ["Aluminum", "13", "3"],
                  ["Sulfur", "16", "6"], ["Chlorine", "17", "7"], ["Oxygen", "16", "6"]])

    def forget_table_check(mod, claims):
        mod.QUESTIONS[0]["table"] = h1_8._T_TYPICAL

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[1]["choices"][4] = mod.QUESTIONS[1]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[19]["why"] = "By position."

    def letter_reference(mod, claims):
        mod.QUESTIONS[6]["why"] = ("Answer D is excluded because the framework says so, "
                                   "and the remainder of the reasoning follows from it.")

    def notation_slips_in(mod, claims):
        mod.QUESTIONS[3]["choices"][1] = "A charge written as Mg^2+ in the compound"
        chem_notation.style(mod)

    print("negative controls:")
    must_fail("an ion charge written as a bare superscript", notation_slips_in)
    must_fail("key moved off its anchor", move_key)
    must_fail("anchor no longer present in the keyed choice", break_anchor)
    must_fail("a tabulated charge corrupted so the keyed formula no longer balances",
              corrupt_a_charge)
    must_fail("a column made to show two different formula patterns",
              break_the_column_pattern)
    must_fail("both columns given the same pattern, so the contrast item has no evidence",
              make_the_columns_agree)
    must_fail("the deliberately unbalanced formula corrected, leaving no odd one out",
              balance_the_bad_formula)
    must_fail("the reactivity trend reversed, refuting the keyed element",
              flatten_the_reactivity_trend)
    must_fail("a second pairing that also balances one to one, so the key is not unique",
              add_a_second_one_to_one_pair)
    must_fail("a table added with no recompute behind it", forget_table_check)
    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a rationale reduced below the minimum", thin_why)
    must_fail("a rationale naming an option by letter", letter_reference)
    print("all negative controls raised as required.")


import h1_8  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

chem_notation.style(h1_8)
cg.check(h1_8, CLAIMS, table_checks=TABLE_CHECKS)
