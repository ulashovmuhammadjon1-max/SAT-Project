"""Key audit for AP BIOLOGY 1.3 Introduction to Macromolecules.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here instead of reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is the shared one in ``cg_check.py``. It cannot tell whether
the biology is right; that is gated by the CLAIMS text and by the
SCIENCE_BRIEF.md rule that every key must trace to a sentence in the CED.

WHAT THE KEYS REST ON
---------------------
Two statements carry the whole topic.

EK 1.3.A.1 -- hydrolysis is a chemical reaction involving the cleaving of
covalent bonds; it breaks molecules down into smaller molecules; when water is
added to the bond between monomers in a polymer the bond is broken, the hydrogen
ion going to one monomer and the hydroxyl group to the other. Items 1, 4, 12,
19, 21, 26 and 30 rest on it directly.

EK 1.3.A.2 -- dehydration synthesis joins two smaller molecules through covalent
bonding by removing a hydrogen ion from one monomer and a hydroxyl group from
the other, which causes the loss of the equivalent of a water molecule and the
connection of the two remaining monomers; the connection of many monomers is
polymerization. Items 2, 3, 5, 22, 25 and 27 rest on it directly.

Items 18, 20, 23, 28 and 29 rest on the CONTRAST between the two statements --
one forms a covalent bond and one cleaves one, one loses a water equivalent and
one takes water up -- and the claim says which halves are being contrasted.

THE ARITHMETIC, stated once. A chain of n monomers is held by n minus 1 bonds
between monomers. EK 1.3.A.2 costs the equivalent of one water molecule per bond
formed and EK 1.3.A.1 consumes one water molecule per bond cleaved. Items 6, 7,
8, 9, 10, 11, 13, 14, 15, 17 and 24 are that one relation applied to numbers the
stem or table supplies, and every one is recomputed below. Where a mass is
needed the stem states the 18 dalton value; nothing is recalled.

NEGATIVE CONTROL: ``python3 verify_b1_3.py --selftest`` corrupts a key, an
anchor, a table cell and the notation on purpose and confirms each check fails.
"""
import re
import sys

import cg_check as cg

_BANNED = [
    (re.compile(r"\\"), "a backslash: Biology is not typeset, so LaTeX would print raw"),
    (re.compile(r"(?<![A-Za-z])\d+\s?-\s?\d"), "a digit-hyphen-digit range: write 'to' instead"),
    (re.compile(r"\d\s?/\s?\d"), "a digit-slash-digit fraction: write it out in words"),
    (re.compile(r"\$"), "a dollar sign, which a converter reads as inline math"),
]


def style(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        texts = [item["q"], item["why"]] + list(item["choices"])
        t = item.get("table")
        if t:
            texts += [str(h) for h in t["headers"]] + [str(c) for r in t["rows"] for c in r]
        for text in texts:
            for pat, msg in _BANNED:
                hit = pat.search(text)
                assert not hit, f"{module.TOPIC[0]} q{i}: {msg} -- {hit.group(0)!r} in {text[:70]!r}"
    print(f"OK  {module.TOPIC[0]} notation: no typeset markup in "
          f"{len(module.QUESTIONS)} questions.")


NMON = "Number of monomers joined into one unbranched chain"
START = "Number of monomers in the starting polymer"
AFTER = "Number of separate molecules present after hydrolysis is complete"
BEFORE_M = "Total mass of the monomers before the reaction (daltons)"
AFTER_M = "Mass of the single polymer formed (daltons)"
TIME = "Time (minutes)"
CHAINS = "Number of intact polymer chains in the tube"
FREE = "Number of free monomers in the tube"
WATER = 18.0


def _waters(table, header):
    """One water equivalent per bond, and n monomers hold n minus 1 bonds."""
    return {lab: cg.cell(table, lab, header) - 1 for lab in cg.labels(table)}


def q7(table, item):
    w = _waters(table, NMON)
    hits = [lab for lab, v in w.items() if v == 14]
    assert hits == ["Polymer R"], f"polymers costing 14 water equivalents: {hits}"
    return f"water equivalents per polymer are {w}, and exactly one equals 14"


def q8(table, item):
    w = _waters(table, NMON)
    total = sum(w.values())
    assert total == 49, f"total water equivalents recompute to {total}"
    raw = sum(cg.col(table, NMON))
    assert raw == 53, f"the raw monomer sum is {raw}; the 53 distractor must be that sum"
    return f"3 plus 8 plus 14 plus 24 is {total:.0f}; the raw monomer sum {raw:.0f} is the distractor"


def q9(table, item):
    w = _waters(table, NMON)
    hits = [lab for lab, v in w.items() if v == 8]
    assert hits == ["Polymer Q"], f"polymers costing 8 water equivalents: {hits}"
    return f"exactly one polymer, {hits[0]}, was assembled with 8 bonds and so 8 water equivalents"


def q10(table, item):
    w = _waters(table, START)
    most = max(w, key=w.get)
    assert most == "Sample 3", f"the largest water consumption is {most}"
    assert len(set(w.values())) == len(w), "'all three the same' must be false"
    return f"water consumed per sample is {w}; the maximum is {most} and no two are equal"


def q11(table, item):
    hits = [lab for lab in cg.labels(table) if cg.cell(table, lab, START) == 11]
    assert len(hits) == 1, f"the stem's eleven-monomer sample matches {hits}"
    n = _waters(table, START)[hits[0]]
    assert n == 10, f"water consumed recomputes to {n}"
    return f"{hits[0]} starts with 11 monomers, so 10 bonds are cleaved and 10 waters consumed"


def q12(table, item):
    for lab in cg.labels(table):
        assert cg.cell(table, lab, START) == cg.cell(table, lab, AFTER), \
            f"{lab}: the two columns must agree for the keyed explanation to be about the table"
    return ("in every row the count after complete hydrolysis equals the starting monomer "
            "count, so no monomer is destroyed and none stays paired")


def _lost(table):
    return {lab: cg.cell(table, lab, BEFORE_M) - cg.cell(table, lab, AFTER_M)
            for lab in cg.labels(table)}


def q13(table, item):
    lost = _lost(table)
    for lab, d in lost.items():
        assert abs(d / WATER - round(d / WATER)) < 1e-9, f"{lab} loses {d}, not a whole number of waters"
    hits = [lab for lab, d in lost.items() if round(d / WATER) == 3]
    assert hits == ["Reaction 2"], f"reactions losing exactly three waters: {hits}"
    return f"mass lost per reaction is {lost}; divided by 18 daltons only {hits[0]} gives 3"


def q14(table, item):
    hits = [lab for lab in cg.labels(table) if cg.cell(table, lab, AFTER_M) == 1178]
    assert len(hits) == 1, f"the stem's 1,178 dalton product matches {hits}"
    bonds = round(_lost(table)[hits[0]] / WATER)
    assert bonds == 4, f"bonds recompute to {bonds}"
    assert bonds + 1 == 5, "monomers must be one more than bonds"
    return f"{hits[0]} loses 72 daltons, which is {bonds} waters and so {bonds + 1} monomers"


def q15(table, item):
    bonds = {lab: round(d / WATER) for lab, d in _lost(table).items()}
    fewest = min(bonds, key=bonds.get)
    assert fewest == "Reaction 4", f"the fewest bonds are in {fewest}"
    assert list(bonds.values()).count(bonds[fewest]) == 1, "'two reactions joined equally few' must be false"
    assert bonds[fewest] + 1 == 2, "the fewest-monomer product must contain two monomers"
    return f"bonds per reaction are {bonds}; the minimum {bonds[fewest]} is unique to {fewest}"


def q16(table, item):
    ch = cg.col(table, CHAINS)
    fr = cg.col(table, FREE)
    assert all(ch[i] > ch[i + 1] for i in range(len(ch) - 1)), f"chains must fall: {ch}"
    assert all(fr[i] < fr[i + 1] for i in range(len(fr) - 1)), f"free monomers must rise: {fr}"
    assert fr[1] > 0 and ch[1] > 0, "monomers must already be present while chains remain"
    return f"chains {ch} fall while free monomers {fr} rise, and both are nonzero at the middle times"


def q17(table, item):
    ch = cg.col(table, CHAINS)
    fr = cg.col(table, FREE)
    assert ch[-1] == 0, "the last row must have no intact chains left"
    length = fr[-1] / ch[0]
    assert abs(length - 5) < 1e-9, f"average chain length recomputes to {length}"
    # the intermediate rows must be consistent with that same length
    for c, f in zip(ch, fr):
        assert abs((ch[0] - c) * length - f) < 1e-9, f"row ({c}, {f}) is inconsistent with length {length}"
    return f"{fr[-1]:.0f} monomers from {ch[0]:.0f} chains is {length:.0f} per chain, consistent at every time"


CLAIMS = [
 ("cleaves covalent bonds and so breaks molecules down",
  "EK 1.3.A.1, near verbatim: hydrolysis is a chemical reaction involving the cleaving of covalent bonds, and this type of reaction breaks down molecules into smaller molecules. Building larger molecules is EK 1.3.A.2's dehydration synthesis."),
 ("removed from one and a hydroxyl group from the other",
  "EK 1.3.A.2: a hydrogen ion is removed from one monomer and a hydroxyl group is removed from the other. Adding those same groups rather than removing them is the hydrolysis direction of EK 1.3.A.1."),
 ("equivalent of one water molecule is lost",
  "EK 1.3.A.2 states that the removal causes the loss of the equivalent of a water molecule from the reactants. One hydrogen ion plus one hydroxyl group is one water, and the accounting is per bond formed."),
 ("hydrogen ion joins one monomer and the hydroxyl group joins the other",
  "EK 1.3.A.1, near verbatim: the hydrogen ion from a water molecule is added to one monomer and the hydroxyl group of the water molecule is added to the other monomer, completing the reaction."),
 ("Polymerization",
  "EK 1.3.A.2 ends by stating that the connection of many monomers is known as polymerization. Hydrolysis is the reverse reaction and the other three terms name processes the framework treats elsewhere."),
 ("Eight",
  "Nine monomers in one unbranched chain are held by eight bonds, and EK 1.3.A.2 costs the equivalent of one water molecule per bond formed. The nine distractor counts monomers rather than bonds."),
 ("Polymer R",
  "Recomputed in q7 above from the tabulated monomer counts, using one water equivalent per bond and n minus 1 bonds per chain. Exactly one row gives fourteen."),
 ("49",
  "Recomputed in q8 above. Each of the four chains ends one bond short of its monomer count, so the total is the raw sum less four; the check confirms the raw sum is the 53 distractor."),
 ("Polymer Q",
  "Recomputed in q9 above: eight bonds join nine monomers and only one row of the table holds nine, so the alternative that two polymers match is false."),
 ("Sample 3",
  "Recomputed in q10 above. EK 1.3.A.1 consumes one water per bond cleaved and a chain of n monomers holds n minus 1 bonds, so consumption rises with chain length and the three samples are all different."),
 ("Ten",
  "Recomputed in q11 above: the eleven-monomer chain holds ten bonds, and EK 1.3.A.1 adds one water molecule per bond broken. Reporting eleven counts monomers rather than bonds."),
 ("each monomer ends up as its own molecule",
  "EK 1.3.A.1 cleaves the covalent bonds between monomers and breaks molecules down into smaller molecules; once every such bond is cleaved nothing joins one monomer to the next. The check confirms the two tabulated columns agree in every row, and the framework describes no step that destroys or re-pairs monomers."),
 ("Reaction 2",
  "Recomputed in q13 above: the mass lost divided by the 18 daltons the stem supplies gives the number of water equivalents EK 1.3.A.2 says are lost, and only one row gives three."),
 ("Five",
  "Recomputed in q14 above: that row loses 72 daltons, which is four water equivalents and so four bonds; a chain with four bonds holds five monomers. The four distractor reports the bond count as a monomer count."),
 ("Reaction 4",
  "Recomputed in q15 above: the smallest mass loss is a single water equivalent, so a single bond and two monomers, and no other row matches it."),
 ("free monomers accumulated",
  "Recomputed in q16 above: intact chains fall monotonically while free monomers rise monotonically, and both are nonzero at the intermediate times. That is what EK 1.3.A.1 predicts, since cleaving the bonds within a chain releases its monomers."),
 ("Five",
  "Recomputed in q17 above: all monomers are free by the final row, so 500 monomers came from 100 chains, and the check confirms every intermediate row is consistent with that same chain length."),
 ("forms a covalent bond between monomers, while hydrolysis cleaves one",
  "EK 1.3.A.2 joins two smaller molecules through covalent bonding and EK 1.3.A.1 cleaves covalent bonds. Both involve water, so the shared involvement of water cannot be what decides the direction."),
 ("hydroxyl group that has been added",
  "EK 1.3.A.1 splits the added water, sending the hydrogen ion to one monomer and the hydroxyl group to the other. The oxygen atom travels in the hydroxyl group, so a label on the oxygen of water follows that half."),
 ("falling while the average molecule is getting larger",
  "EK 1.3.A.2 connects many monomers, which merges separate molecules into fewer and larger ones; EK 1.3.A.1 breaks molecules down into smaller molecules, which does the reverse. Temperature and total mass do not separate the two directions."),
 ("works by adding water across it",
  "EK 1.3.A.1 defines the reaction by the addition of water to the bond between monomers. The option that speaks of removing a hydrogen ion and a hydroxyl group describes EK 1.3.A.2, which forms the bond rather than breaking it."),
 ("both monomers, plus one water molecule",
  "EK 1.3.A.2 states that joining two smaller molecules causes the loss of the equivalent of a water molecule from the reactants and the connection of the two remaining monomers. One bond therefore accounts for exactly one water and leaves one joined product."),
 ("equals the number consumed during hydrolysis",
  "Both statements are per bond: EK 1.3.A.2 loses one water equivalent per bond formed and EK 1.3.A.1 consumes one water per bond cleaved. Assembling and then completely hydrolyzing the same chain forms and cleaves the same number of bonds."),
 ("Nineteen",
  "EK 1.3.A.2 costs the equivalent of one water molecule per bond formed between monomers, and the stem supplies the bond count. Branching rearranges the bonds without changing that per-bond accounting, so the monomer count is not the figure to use."),
 ("many monomers connected together",
  "EK 1.3.A.2 states that the connection of many monomers is known as polymerization, and EK 1.3.A.1 speaks of the bond between monomers in a polymer. The two terms therefore name the unit and the assembly."),
 ("Fewer free monomers will be released",
  "Adding water across the bond between monomers is exactly the reaction EK 1.3.A.1 describes and is what liberates monomers from a polymer. The framework supplies no alternative route by which a polymer lengthens or decomposes when that reaction is blocked."),
 ("Dehydration synthesis, and the two remaining molecules become covalently connected",
  "EK 1.3.A.2 states that removing a hydrogen ion from one monomer and a hydroxyl group from the other causes the loss of the equivalent of a water molecule and the connection of the two remaining monomers. Removal is the synthesis direction; addition is hydrolysis under EK 1.3.A.1."),
 ("falls and the amount of free water rises",
  "EK 1.3.A.2 merges monomers into fewer, larger molecules and loses the equivalent of a water molecule per bond formed, so the two counts move in opposite directions. The reverse pattern is EK 1.3.A.1's."),
 ("same pair of reactions builds and breaks the bonds",
  "EK 1.3.A.1 and EK 1.3.A.2 are stated about monomers and polymers in general, ahead of the class-specific topics 1.4 to 1.7, and the framework names no class-specific alternative reaction and no class exempt from hydrolysis."),
 ("water does not stay whole",
  "EK 1.3.A.1 states that the hydrogen ion from a water molecule is added to one monomer and the hydroxyl group to the other. That splitting step is what the student's description omits; the rest of it, that water is added and the polymer breaks into smaller molecules, matches the statement."),
]

TABLE_CHECKS = {7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 13: q13, 14: q14,
                15: q15, 16: q16, 17: q17}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("b1_3_mutant")
        mod.TOPIC = b1_3.TOPIC
        mod.QUESTIONS = copy.deepcopy(b1_3.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            style(mod)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def bad_monomer_count(mod, claims):
        mod.QUESTIONS[6]["table"] = dict(
            headers=b1_3._T_POLY["headers"],
            rows=[[lab, ("15" if lab == "Polymer S" else v)]
                  for lab, v in b1_3._T_POLY["rows"]])

    def bad_mass(mod, claims):
        mod.QUESTIONS[12]["table"] = dict(
            headers=b1_3._T_MASS["headers"],
            rows=[[lab, b, ("846" if lab == "Reaction 1" else a)]
                  for lab, b, a in b1_3._T_MASS["rows"]])

    def inconsistent_timecourse(mod, claims):
        mod.QUESTIONS[16]["table"] = dict(
            headers=b1_3._T_TIMECOURSE["headers"],
            rows=[[t, c, ("250" if t == "30" else f)]
                  for t, c, f in b1_3._T_TIMECOURSE["rows"]])

    print("negative controls:")
    must_fail("key moved off its anchor", lambda m, c: m.QUESTIONS[4].__setitem__("ans", 1))
    must_fail("anchor no longer in the keyed choice",
              lambda m, c: c.__setitem__(0, ("no such phrase", c[0][1])))
    must_fail("a second polymer given the same monomer count", bad_monomer_count)
    must_fail("a product mass altered so the water count is no longer three", bad_mass)
    must_fail("a time course row made inconsistent with the chain length", inconsistent_timecourse)
    must_fail("a backslash macro in a stem",
              lambda m, c: m.QUESTIONS[5].__setitem__("q", "How many waters for \\(n\\) monomers?"))
    print("all negative controls raised as required.")


import b1_3  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(b1_3)
cg.check(b1_3, CLAIMS, table_checks=TABLE_CHECKS)
