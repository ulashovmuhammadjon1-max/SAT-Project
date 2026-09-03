"""Key audit for AP BIOLOGY 1.4 Carbohydrates.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here instead of reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is the shared one in ``cg_check.py``. It cannot tell whether
the biology is right; that is gated by the CLAIMS text and by the
SCIENCE_BRIEF.md rule that every key must trace to a sentence in the CED.

WHAT THE KEYS REST ON, AND WHAT THIS TOPIC REFUSES TO ASK
---------------------------------------------------------
The topic has ONE essential knowledge statement. EK 1.4.A.1: monosaccharides
(simple sugars) are the monomers for polysaccharides (complex carbohydrates);
these monomers are connected by covalent bonds to form polymers such as complex
carbohydrates, which may be linear or branched. Its exclusion statement puts the
molecular structure of specific carbohydrate polymers outside the AP Exam, and
its illustrative examples -- cellulose, starch, glycogen -- are given with NO
function and NO structure.

So item 5 keys those three names only to what EK 1.4.A.1 says of them, that they
are polymers of monosaccharide monomers. Nothing in this module keys "starch is
the plant storage polymer" or "glycogen is branched": the framework does not
print either, and the second is inside the exclusion. Item 6 keys the exclusion
statement itself.

Items 1, 2, 3, 4, 7, 8, 9, 14, 19, 23, 24, 25, 28 and 29 rest on EK 1.4.A.1
directly. Items 10, 11, 12, 13, 15, 16, 17, 22, 26, 27 and 30 CHAIN to EK
1.3.A.1 (hydrolysis cleaves the covalent bonds between monomers, breaking
molecules into smaller molecules) or EK 1.3.A.2 (dehydration synthesis forms
them, losing a water equivalent per bond); item 18 chains to EK 1.2.A.1 on the
elements; item 21 chains to EK 1.7.A.1 for the parallel with a peptide chain.
Item 20 rests on the same hydrolysis chain used as evidence.

THE BOND ARITHMETIC, stated once. A connected, ring-free molecule of n monomer
units is held by n minus 1 covalent bonds between monomers, however those bonds
are arranged. Items 10, 15 and 30 use it; item 15 is the one 1.3 cannot ask,
because branching is a carbohydrate statement.

DATA ITEMS: 7 to 15 carry tables. Every keyed conclusion is recomputed below
from the table alone.

NEGATIVE CONTROL: ``python3 verify_b1_4.py --selftest`` corrupts a key, an
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


UNITS = "Number of monosaccharide units in one molecule"
SHAPE = "Shape of the connected chain"
KINDS = "Kinds of simple sugar recovered after complete hydrolysis"
TOTAL = "Total number of simple sugar molecules recovered"
EUNITS = "Number of monosaccharide units"
ENDS = "Number of chain ends counted on one molecule"


def _shape(table, label):
    j = table["headers"].index(SHAPE)
    return [r[j] for r in table["rows"] if r[0] == label][0]


def q7(table, item):
    singles = [lab for lab in cg.labels(table) if cg.cell(table, lab, UNITS) == 1]
    assert singles == ["Sample J"], f"single-unit rows: {singles}"
    return f"exactly one row records one monomer unit, {singles[0]}, so it carries no bond between monomers"


def q8(table, item):
    branched = [lab for lab in cg.labels(table)
                if _shape(table, lab) == "branched" and cg.cell(table, lab, UNITS) > 1]
    assert branched == ["Sample L"], f"branched polymers: {branched}"
    return f"exactly one row is both a polymer and branched, {branched[0]}"


def q9(table, item):
    linear = sorted(lab for lab in cg.labels(table)
                    if _shape(table, lab) == "unbranched" and cg.cell(table, lab, UNITS) > 1)
    assert linear == ["Sample K", "Sample M"], f"unbranched polymers: {linear}"
    return f"exactly two rows are polymers recorded as unbranched: {linear}"


def q10(table, item):
    hits = [lab for lab in cg.labels(table) if cg.cell(table, lab, UNITS) == 300]
    assert len(hits) == 1, f"the stem's 300-unit sample matches {hits}"
    bonds = cg.cell(table, hits[0], UNITS) - 1
    assert bonds == 299, f"bond count recomputes to {bonds}"
    return f"{hits[0]} holds 300 units in one chain, so {bonds:.0f} bonds between monomers"


def q11(table, item):
    ones = [lab for lab in cg.labels(table) if cg.cell(table, lab, TOTAL) == 1]
    assert ones == ["Sample P"], f"rows recovering a single molecule: {ones}"
    return f"exactly one row recovers a single simple sugar molecule, {ones[0]}, so it had no bond to break"


def q12(table, item):
    hits = [lab for lab in cg.labels(table)
            if cg.cell(table, lab, KINDS) == 1 and cg.cell(table, lab, TOTAL) > 1]
    assert hits == ["Sample Q"], f"single-monomer polysaccharides: {hits}"
    return (f"exactly one row recovers many molecules of exactly one kind, {hits[0]}, "
            "which is a polymer of a single kind of monomer")


def q13(table, item):
    big = [lab for lab in cg.labels(table) if cg.cell(table, lab, TOTAL) > 500]
    assert sorted(big) == ["Sample Q", "Sample R"], f"rows above 500 molecules: {big}"
    more_mol = max(big, key=lambda l: cg.cell(table, l, TOTAL))
    more_kinds = max(big, key=lambda l: cg.cell(table, l, KINDS))
    assert more_mol != more_kinds, "the pair must run in opposite directions on the two columns"
    assert cg.cell(table, more_kinds, KINDS) > cg.cell(table, more_mol, KINDS), \
        "the fewer-molecule sample must be the one with more kinds"
    return (f"{more_mol} yields more molecules while {more_kinds} yields more kinds, so the "
            "two columns disagree across this pair")


def q14(table, item):
    branched = sorted(lab for lab in cg.labels(table) if cg.cell(table, lab, ENDS) > 2)
    assert branched == ["Polymer U", "Polymer W"], f"rows with more than two ends: {branched}"
    linear = sorted(lab for lab in cg.labels(table) if cg.cell(table, lab, ENDS) == 2)
    assert len(linear) == 2, f"exactly two rows should have two ends, got {linear}"
    return f"{branched} record more than the two ends an unbranched chain has; {linear} record exactly two"


def q15(table, item):
    counts = set(cg.col(table, EUNITS))
    assert counts == {1000.0}, f"every row must hold 1,000 units; got {counts}"
    bonds = 1000 - 1
    assert bonds == 999, "n minus 1 must give 999"
    ends = cg.col(table, ENDS)
    assert len(set(ends)) > 1, "the rows must differ in branching for the point to bite"
    return ("all four rows hold 1,000 units, so each holds 999 bonds, while the end counts "
            f"{ends} differ -- branching changes arrangement, not bond count")


CLAIMS = [
 ("A monosaccharide",
  "EK 1.4.A.1, near verbatim: monosaccharides (simple sugars) are the monomers for polysaccharides. Amino acids, nucleotides, fatty acids and phospholipids are the units the framework assigns to other classes in EK 1.5.A.1, EK 1.6.A.1 and EK 1.7.A.1."),
 ("simple sugars, and polysaccharides are complex carbohydrates",
  "EK 1.4.A.1 supplies both parenthetical synonyms in a single sentence, pairing monosaccharide with simple sugar and polysaccharide with complex carbohydrate. Every rejected option inverts that pairing or borrows a name from another class."),
 ("A covalent bond",
  "EK 1.4.A.1 states that these monomers are connected by covalent bonds to form polymers. Hydrogen bonds, ionic and hydrophobic interactions and disulfide bridges appear in EK 1.7.A.4 and EK 1.7.A.5 as forces shaping a folded protein, never as the monomer link in a polysaccharide."),
 ("may be linear or branched",
  "EK 1.4.A.1 ends by stating that the polymers formed may be linear or branched, which permits both shapes and requires neither. The helix belongs to EK 1.6.A.3 and EK 1.7.A.4."),
 ("Polymers built from monosaccharide monomers",
  "Cellulose, starch and glycogen appear in the CED as the illustrative examples attached to EK 1.4.A.1, whose subject is polymers formed by connecting monosaccharide monomers with covalent bonds. The framework states no function and no structure for any of the three, so nothing further about them is keyed anywhere in this module."),
 ("molecular structure of specific carbohydrate polymers",
  "The exclusion statement printed under EK 1.4.A.1 says that the molecular structure of specific carbohydrate polymers is beyond the scope of the AP Exam. The four rejected options restate content EK 1.4.A.1 and EK 1.2.A.1 do require."),
 ("Sample J",
  "Recomputed in q7 above: exactly one row records a single monomer unit. EK 1.4.A.1 makes a monosaccharide the monomer and a polysaccharide a polymer of many such monomers, so a one-unit molecule carries no bond between monomers at all."),
 ("Sample L",
  "Recomputed in q8 above: exactly one row is recorded as branched while holding many units. EK 1.4.A.1 allows a complex carbohydrate to be linear or branched, and a single unit is not a polymer to begin with."),
 ("Sample K and Sample M",
  "Recomputed in q9 above: exactly two rows hold more than one unit and are recorded as unbranched, which is what EK 1.4.A.1's linear option describes."),
 ("299",
  "Recomputed in q10 above. Every unit after the first is added by forming one covalent bond, so an unbranched chain of n units holds n minus 1 bonds; EK 1.4.A.1 makes those links covalent and EK 1.3.A.2 is the reaction that forms each one."),
 ("Sample P",
  "Recomputed in q11 above: exactly one row recovers a single simple sugar molecule. Under EK 1.3.A.1 complete hydrolysis releases one molecule per monomer, so a single product means the sample had no bond between monomers to cleave."),
 ("Sample Q",
  "Recomputed in q12 above: exactly one row recovers many molecules of exactly one kind, which is what a polysaccharide built from a single kind of monosaccharide monomer yields under EK 1.4.A.1 and EK 1.3.A.1."),
 ("while the sample yielding fewer molecules",
  "Recomputed in q13 above: across the two rows above five hundred molecules, the sample with the larger total has fewer kinds and the sample with more kinds has the smaller total. EK 1.4.A.1 places no limit on how many kinds of monosaccharide a polysaccharide may contain."),
 ("Polymer U and Polymer W",
  "Recomputed in q14 above: an unbranched chain has exactly two ends, and exactly two rows record more than two, so those two must divide somewhere along their length. EK 1.4.A.1 is what makes both shapes admissible."),
 ("999 such bonds",
  "Recomputed in q15 above: every row holds 1,000 units, so every row holds 999 bonds between monomers, while the end counts differ. Branching changes where the bonds sit, not how many there are, which is why EK 1.4.A.1 can allow either shape for one class of polymer."),
 ("Hydrolysis, which adds water across the bonds",
  "EK 1.3.A.1 defines hydrolysis as the cleaving of covalent bonds, effected by adding water across the bond between monomers, and EK 1.4.A.1 makes the polysaccharide link covalent. Dehydration synthesis and polymerization run in the opposite direction."),
 ("Dehydration synthesis, releasing the equivalent of one water molecule",
  "EK 1.3.A.2 joins two smaller molecules through covalent bonding with the loss of the equivalent of a water molecule from the reactants, and EK 1.4.A.1 makes the bond being formed here a covalent one between monosaccharides."),
 ("carbon, hydrogen and oxygen are the elements named as most prevalent",
  "EK 1.2.A.1 names carbon, hydrogen and oxygen as the most prevalent elements used to build biological molecules including carbohydrates, and its sub-points assign sulfur to proteins and phosphorus and nitrogen to phospholipids and nucleic acids, never to carbohydrates."),
 ("linear or branched, so an unbranched chain is one possibility",
  "EK 1.4.A.1 states that the polymers may be linear or branched. The correction is therefore to the universality of the student's claim, not to its direction, since the framework endorses neither shape exclusively."),
 ("releases a large number of simple sugar molecules",
  "EK 1.4.A.1 defines a polysaccharide as a polymer of monosaccharide monomers and EK 1.3.A.1 makes hydrolysis the reaction that releases them. Amino acids would indicate a peptide chain under EK 1.7.A.1, and elemental composition does not separate a monomer from a polymer."),
 ("many monomers are connected by covalent bonds into a polymer",
  "EK 1.4.A.1 connects monosaccharide monomers by covalent bonds into polysaccharides, and EK 1.7.A.1 connects amino acids by covalent peptide bonds into a growing peptide chain. The shared covalent monomer-to-polymer relation is what the comparison rests on."),
 ("unable to assemble monosaccharides into complex carbohydrates",
  "EK 1.4.A.1 makes the covalent bond between monomers the thing that turns monosaccharides into a polysaccharide, so losing the ability to form it blocks assembly. Breakdown is hydrolysis under EK 1.3.A.1 and is a different reaction."),
 ("held to one another by hydrogen bonds",
  "EK 1.4.A.1 states that the monomers are connected by covalent bonds, so attributing the connection to hydrogen bonds contradicts it. The four rejected options restate EK 1.4.A.1 or the hydrolysis reaction of EK 1.3.A.1 accurately."),
 ("Both are complex carbohydrates",
  "EK 1.4.A.1 says the polymers may be linear or branched, so shape does not decide membership in the class. Nitrogen belongs to nucleic acids under EK 1.2.A.1 iii, and a connected ring-free molecule of n units holds n minus 1 bonds in either shape."),
 ("no bond to another monomer to cleave",
  "EK 1.4.A.1 makes the monosaccharide the unit and the polysaccharide the assembly, and EK 1.3.A.1 confines hydrolysis to the bond between monomers in a polymer. A lone unit has no such bond, though EK 1.3.A.2 can still join it to another."),
 ("more than one kind of monosaccharide monomer",
  "EK 1.3.A.1 releases a polymer's monomers when its bonds are cleaved, so the identities of the products report the identities of the monomers. EK 1.4.A.1 places no restriction on how many kinds are used and none on shape, so branching cannot be inferred here."),
 ("Covalent bonds between its monomers are cleaved by hydrolysis",
  "EK 1.4.A.1 makes the links covalent and EK 1.3.A.1 makes hydrolysis the cleaving of covalent bonds that breaks molecules down into smaller molecules. Dehydration synthesis runs the other way and yields no monomers."),
 ("It is a polysaccharide",
  "EK 1.4.A.1 defines a polysaccharide as a polymer whose monosaccharide monomers are connected by covalent bonds, which is exactly the behaviour reported. The exclusion statement removes the need for structural detail rather than making classification impossible."),
 ("Monosaccharide and polysaccharide",
  "EK 1.4.A.1 states that monosaccharides are the monomers for polysaccharides, which is the unit to assembly relation. Two rejected pairs are synonym pairs the same sentence supplies, and two are alternatives rather than a unit and its assembly."),
 ("It has increased",
  "EK 1.3.A.1 states that hydrolysis breaks molecules down into smaller molecules, and EK 1.4.A.1 makes those smaller molecules the monosaccharides of the polymer. Water is consumed rather than lost in this direction, and the conclusion holds for either shape EK 1.4.A.1 permits."),
]

TABLE_CHECKS = {7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("b1_4_mutant")
        mod.TOPIC = b1_4.TOPIC
        mod.QUESTIONS = copy.deepcopy(b1_4.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            style(mod)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def second_branched(mod, claims):
        mod.QUESTIONS[7]["table"] = dict(
            headers=b1_4._T_CARBS["headers"],
            rows=[[lab, n, ("branched" if lab == "Sample M" else sh)]
                  for lab, n, sh in b1_4._T_CARBS["rows"]])

    def unequal_units(mod, claims):
        mod.QUESTIONS[14]["table"] = dict(
            headers=b1_4._T_ENDS["headers"],
            rows=[[lab, ("1,200" if lab == "Polymer W" else n), e]
                  for lab, n, e in b1_4._T_ENDS["rows"]])

    def bond_count_wrong(mod, claims):
        mod.QUESTIONS[9]["table"] = dict(
            headers=b1_4._T_CARBS["headers"],
            rows=[[lab, ("310" if lab == "Sample K" else n), sh]
                  for lab, n, sh in b1_4._T_CARBS["rows"]])

    print("negative controls:")
    must_fail("key moved off its anchor", lambda m, c: m.QUESTIONS[0].__setitem__("ans", 2))
    must_fail("anchor no longer in the keyed choice",
              lambda m, c: c.__setitem__(3, ("no such phrase", c[3][1])))
    must_fail("a second sample marked branched", second_branched)
    must_fail("the equal-unit premise of the branching item broken", unequal_units)
    must_fail("the 300-unit sample renumbered so 299 is wrong", bond_count_wrong)
    must_fail("a backslash macro in a why",
              lambda m, c: m.QUESTIONS[3].__setitem__(
                  "why", "EK 1.4.A.1 allows \\text{linear} or branched polymers to form."))
    print("all negative controls raised as required.")


import b1_4  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(b1_4)
cg.check(b1_4, CLAIMS, table_checks=TABLE_CHECKS)
