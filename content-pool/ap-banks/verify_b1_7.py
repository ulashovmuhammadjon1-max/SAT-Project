"""Key audit for AP BIOLOGY 1.7 Proteins.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here instead of reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is the shared one in ``cg_check.py``. It cannot tell whether
the biology is right; that is gated by the CLAIMS text and by the
SCIENCE_BRIEF.md rule that every key must trace to a sentence in the CED.

WHAT THE KEYS REST ON
---------------------
EK 1.7.A.1 (linear chains of amino acids connected by covalent, peptide bonds
between a carboxyl group of one amino acid and an amine group of the next)
carries items 1 and 2.

EK 1.7.A.2 (a central carbon with a hydrogen atom, a carboxyl group, an amine
group and a variable R group; three R group categories -- hydrophobic or
nonpolar, hydrophilic or polar, ionic; the interactions of these R groups
determine the structure and function of that region) carries items 3, 4, 5, 14
to 22, 28 and 29.

EK 1.7.A.3 (the specific sequence determines the primary structure and the
overall shape) carries item 6, and its exclusion statement carries item 11.

EK 1.7.A.4 (secondary structure from local folding through interactions between
atoms of the polypeptide backbone; hydrogen bonding forms alpha helices and beta
pleated sheets) carries items 7 and 24 and half of 13 and 27.

EK 1.7.A.5 (tertiary shape from hydrogen bonds, hydrophobic interactions, ionic
interactions or disulfide bridges) carries items 8 and 23 and the other half of
13 and 27.

EK 1.7.A.6 (quaternary structure from interactions between multiple
polypeptides; all four levels determine function) carries items 9, 10, 12, 25
and 30.

Item 26 chains to EK 1.2.A.1 i, which assigns sulfur to the building of
proteins, as the element assignment consistent with EK 1.7.A.5's disulfide
bridge.

DATA ITEMS: 14 to 21 carry tables. Every keyed conclusion is recomputed below
from the table alone. The R group category columns are text rather than numbers,
so those checks read the cells directly instead of through the numeric helpers.

NEGATIVE CONTROL: ``python3 verify_b1_7.py --selftest`` corrupts a key, an
anchor, two table cells and the notation on purpose and confirms each fails.
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


PROP = "Chemical property of the R group at that position"
HPHOB = "Amino acids with hydrophobic R groups"
HPHIL = "Amino acids with hydrophilic R groups"
IONIC = "Amino acids with ionic R groups"
TOTAL = "Total amino acids in the chain"
VPROP = "Chemical property of the R group at position 40"
ACT = "Enzyme activity (percentage of the unaltered protein)"

# EK 1.7.A.2's three categories. Any cell outside this set is a typo the checks catch.
CATEGORIES = {"hydrophobic, that is nonpolar", "hydrophilic, that is polar", "ionic"}


def _text_col(table, header):
    j = table["headers"].index(header)
    return {r[0]: r[j] for r in table["rows"]}


def _by_category(table, header):
    cells = _text_col(table, header)
    unknown = set(cells.values()) - CATEGORIES
    assert not unknown, f"category cells outside EK 1.7.A.2's three: {unknown}"
    out = {}
    for lab, prop in cells.items():
        out.setdefault(prop, []).append(lab)
    return out


def q14(table, item):
    groups = _by_category(table, PROP)
    ionic = sorted(groups.get("ionic", []))
    assert ionic == ["Position 27", "Position 63"], f"ionic positions: {ionic}"
    return f"exactly two positions carry ionic R groups, {ionic}, so they are the only possible ionic pair"


def q15(table, item):
    groups = _by_category(table, PROP)
    n = len(groups.get("hydrophobic, that is nonpolar", []))
    assert n == 2, f"hydrophobic positions recount to {n}"
    assert len(table["rows"]) - n == 3, "the other two categories must account for the remaining three"
    return f"{n} of the {len(table['rows'])} positions are hydrophobic; the other three fall in the other two categories"


def q16(table, item):
    groups = _by_category(table, PROP)
    nonpolar = sorted(groups.get("hydrophobic, that is nonpolar", []))
    assert nonpolar == ["Position 12", "Position 58"], f"nonpolar positions: {nonpolar}"
    assert len(nonpolar) == 2, "the stem says two positions, so exactly two must be nonpolar"
    return f"exactly two positions are hydrophobic, {nonpolar}, which is what a hydrophobic interaction needs"


def q17(table, item):
    totals = {lab: cg.cell(table, lab, TOTAL) for lab in cg.labels(table)}
    assert len(set(totals.values())) == 1, f"the chains must be equal in length; got {totals}"
    frac = {lab: cg.cell(table, lab, HPHOB) / totals[lab] for lab in cg.labels(table)}
    top = max(frac, key=frac.get)
    assert top == "Protein C", f"the largest hydrophobic proportion is {top}"
    assert list(frac.values()).count(frac[top]) == 1, "'all three the same' must be false"
    return f"hydrophobic proportions are {frac}; the unique maximum is {top}"


def q18(table, item):
    hits = [lab for lab in cg.labels(table) if cg.cell(table, lab, HPHIL) == 110]
    assert len(hits) == 1, f"the stem's 110 hydrophilic protein matched {hits}"
    lab = hits[0]
    tot = cg.cell(table, lab, TOTAL)
    parts = [cg.cell(table, lab, h) for h in (HPHOB, HPHIL, IONIC)]
    assert sum(parts) == tot, f"{lab} categories sum to {sum(parts)}, not the stated total {tot}"
    not_hydrophobic = 100 * (parts[1] + parts[2]) / tot
    assert not_hydrophobic == 80, f"recomputed {not_hydrophobic} percent, not 80"
    assert 100 * parts[1] / tot == 55, "the 55 distractor must be the hydrophilic share alone"
    return f"{lab}: hydrophilic plus ionic over the total is {not_hydrophobic:.0f} percent; 55 is hydrophilic alone"


def q19(table, item):
    totals = {lab: cg.cell(table, lab, TOTAL) for lab in cg.labels(table)}
    assert len(set(totals.values())) == 1, "the comparison needs equal chain lengths"
    counts = {lab: cg.cell(table, lab, HPHOB) for lab in cg.labels(table)}
    top = max(counts, key=counts.get)
    assert top == "Protein C", f"the most hydrophobic R groups belong to {top}"
    assert len(set(counts.values())) > 1, "'all three equally' must be false"
    return f"hydrophobic counts over an equal total are {counts}; the maximum is {top}"


def _variant_split(table):
    prop = _text_col(table, VPROP)
    unknown = set(prop.values()) - CATEGORIES
    assert not unknown, f"category cells outside EK 1.7.A.2's three: {unknown}"
    base = prop["Unaltered protein"]
    same = [lab for lab, p in prop.items() if p == base and lab != "Unaltered protein"]
    changed = [lab for lab, p in prop.items() if p != base]
    return base, same, changed


def q20(table, item):
    base, same, changed = _variant_split(table)
    act = {lab: cg.cell(table, lab, ACT) for lab in cg.labels(table)}
    assert same and changed, f"the design needs both kinds of variant; got same={same} changed={changed}"
    assert min(act[l] for l in same) > 90, f"same-category variants must retain activity: {[act[l] for l in same]}"
    assert max(act[l] for l in changed) < 25, f"changed-category variants must lose it: {[act[l] for l in changed]}"
    return (f"the variant keeping the {base} category holds {min(act[l] for l in same):.0f} percent "
            f"while the changed ones fall to {[act[l] for l in changed]}")


def q21(table, item):
    base, same, changed = _variant_split(table)
    act = {lab: cg.cell(table, lab, ACT) for lab in cg.labels(table)}
    assert len(same) == 1, f"exactly one variant should keep the original category; got {same}"
    assert act[same[0]] >= 90, f"{same[0]} retains only {act[same[0]]} percent"
    assert all(act[l] < act[same[0]] for l in changed), "the retained variant must be the highest of the altered set"
    return f"{same[0]} alone keeps the {base} category and alone retains {act[same[0]]:.0f} percent of activity"


CLAIMS = [
 ("covalent bond, also called a peptide bond",
  "EK 1.7.A.1 states that proteins comprise linear chains of amino acids connected by the formation of covalent (peptide) bonds. Hydrogen bonds, ionic and hydrophobic interactions and disulfide bridges appear in EK 1.7.A.4 and EK 1.7.A.5 as forces folding an already connected chain."),
 ("carboxyl group of one amino acid and the amine group of the next",
  "EK 1.7.A.1 places the peptide bond between a carboxyl group of one amino acid and an amine group of the next amino acid. EK 1.7.A.2 assigns the R groups to folding interactions, not to the bond that builds the chain."),
 ("central carbon atom bound to a hydrogen atom, a carboxyl group, an amine",
  "EK 1.7.A.2 states that amino acids are composed of a central carbon atom with a hydrogen atom, a carboxyl group, an amine group, and a variable R group covalently bound to it. The rejected sugar-phosphate-base option is EK 1.6.A.1's nucleotide."),
 ("Three: hydrophobic or nonpolar",
  "EK 1.7.A.2 states that the R group can be categorized by three possible chemical properties: hydrophobic/nonpolar, hydrophilic/polar, or ionic. Saturated and unsaturated are EK 1.5.A.1's fatty acid categories."),
 ("structure and function of that region of the protein",
  "EK 1.7.A.2 ends by stating that the interactions of these R groups determine the structure and function of that region of the protein. The order of the amino acids is EK 1.7.A.3's primary structure, which the R groups follow from rather than produce."),
 ("primary structure of the polypeptide and the overall shape",
  "EK 1.7.A.3 states that the specific sequence of amino acids determines the primary structure of a polypeptide as well as the overall shape of the protein. Both halves are in one sentence, so separating them misreads it."),
 ("interactions between atoms of the polypeptide backbone, with hydrogen bonding",
  "EK 1.7.A.4 states that secondary structures are made through local folding formed by interactions between atoms of the polypeptide backbone, and that hydrogen bonding forms shapes such as alpha helices and beta pleated sheets. R group interactions belong to EK 1.7.A.5 and multiple polypeptides to EK 1.7.A.6."),
 ("Hydrogen bonds, hydrophobic interactions, ionic interactions, or disulfide bridges",
  "EK 1.7.A.5, near verbatim: the three-dimensional shape of the tertiary structure results from the formation of hydrogen bonds, hydrophobic interactions, ionic interactions, or disulfide bridges."),
 ("Interactions between multiple polypeptides",
  "EK 1.7.A.6 states that the quaternary structure arises from interactions between multiple polypeptides. Local folding within one chain is EK 1.7.A.4's secondary level and the order of amino acids is EK 1.7.A.3's primary level."),
 ("All four of them",
  "EK 1.7.A.6 ends by stating that all four levels of a protein structure determine the function of a protein, so singling out one or two levels contradicts the sentence."),
 ("molecular structure of amino acids",
  "The exclusion statement printed under EK 1.7.A.3 puts the molecular structure of amino acids beyond the scope of the AP Exam. The rejected options restate content EK 1.7.A.1, EK 1.7.A.2, EK 1.7.A.3 and EK 1.7.A.6 do require."),
 ("Quaternary structure",
  "EK 1.7.A.6 states that the quaternary structure arises from interactions between multiple polypeptides, which is what two associated chains are. The other three levels are described in EK 1.7.A.3 to EK 1.7.A.5 as properties of a single chain."),
 ("tertiary level also draws on hydrophobic, ionic and disulfide",
  "EK 1.7.A.4 confines the secondary level to local folding from interactions between atoms of the polypeptide backbone with hydrogen bonding, while EK 1.7.A.5 gives the tertiary level hydrogen bonds, hydrophobic interactions, ionic interactions and disulfide bridges."),
 ("Position 27 and Position 63",
  "Recomputed in q14 above: exactly two positions carry R groups in EK 1.7.A.2's ionic category, and EK 1.7.A.5 names ionic interactions among the tertiary forces. No other pair in the table can form one."),
 ("Two",
  "Recomputed in q15 above by counting the rows assigned to EK 1.7.A.2's hydrophobic, that is nonpolar, category; the other two categories account for the remaining three positions."),
 ("hydrophobic interaction between the two nonpolar R groups",
  "Recomputed in q16 above: exactly two positions fall in the hydrophobic category, which EK 1.7.A.2 equates with nonpolar, and EK 1.7.A.5 names hydrophobic interactions among the tertiary forces. A peptide bond is reserved by EK 1.7.A.1 for neighbouring amino acids."),
 ("Protein C",
  "Recomputed in q17 above: all three chains hold the same total, so the largest hydrophobic count is also the largest proportion, and the maximum is unique."),
 ("80 percent",
  "Recomputed in q18 above. EK 1.7.A.2's three categories account for every amino acid, so the not-hydrophobic share is the hydrophilic and ionic counts over the total; the check confirms the columns really do sum to the stated total and that 55 is the hydrophilic share alone."),
 ("Protein C",
  "Recomputed in q19 above: over an equal chain length the largest hydrophobic count gives the most opportunities for the hydrophobic interactions EK 1.7.A.5 names among the tertiary forces."),
 ("only when the chemical category of the R group at that position changed",
  "Recomputed in q20 above: the variant that kept the original category retained more than ninety percent of activity while both variants that changed category fell below twenty five. EK 1.7.A.2 makes the interactions of the R groups the determinant of the structure and function of that region, and the chain length was not varied."),
 ("same chemical category, so the interactions available",
  "Recomputed in q21 above: exactly one variant keeps the original category and it alone retains the activity. EK 1.7.A.2's three categories are what a substitution can move between, and EK 1.7.A.3 makes sequence determine overall shape, which is why the sequence-does-not-matter option is false."),
 ("interactions available in that region change, which can alter the shape",
  "EK 1.7.A.2 makes the interactions of the R groups determine the structure and function of that region, and EK 1.7.A.3 makes the specific sequence determine the primary structure and the overall shape. A changed position is a changed sequence and can propagate to shape and function."),
 ("Tertiary structure",
  "EK 1.7.A.5 names disulfide bridges among the forces from which the three-dimensional tertiary shape results. EK 1.7.A.4 confines the secondary level to backbone hydrogen bonding and EK 1.7.A.6 confines the quaternary level to interactions between multiple polypeptides."),
 ("Secondary structure",
  "EK 1.7.A.4 states that hydrogen bonding forms shapes such as alpha helices and beta pleated sheets in the local folding that makes a protein's secondary structure. The framework names those two shapes at no other level."),
 ("Quaternary structure",
  "EK 1.7.A.6 states that the quaternary structure arises from interactions between multiple polypeptides, so a protein consisting of one chain has no such interaction. The other three levels are features of a single chain in EK 1.7.A.3, EK 1.7.A.4 and EK 1.7.A.5."),
 ("sulfur is used in the building of proteins",
  "EK 1.7.A.5 names disulfide bridges among the tertiary forces and EK 1.2.A.1 i assigns sulfur specifically to the building of proteins. The rejected options name assignments the framework makes to other classes or to biological molecules generally, none of which supplies a sulfur bridge."),
 ("between backbone atoms at the secondary level and is also one of several forces",
  "EK 1.7.A.4 attributes the local folding of the secondary level to hydrogen bonding between atoms of the polypeptide backbone, and EK 1.7.A.5 lists hydrogen bonds among the forces producing the tertiary shape. The bond joining neighbouring amino acids is covalent under EK 1.7.A.1."),
 ("bound to the central carbon of an amino acid",
  "EK 1.7.A.2 places the variable R group on the central carbon alongside a hydrogen atom, a carboxyl group and an amine group, and EK 1.7.A.4 describes the secondary level in terms of the polypeptide backbone. Calling the R group variable is itself the denial of the option that says every R group is identical."),
 ("interactions of that region with the surrounding water change",
  "EK 1.7.A.2 sorts R groups into hydrophobic, hydrophilic and ionic categories and states that their interactions determine the structure and function of that region of the protein, so a change of category changes the interactions available. EK 1.7.A.3 makes any changed position a change of sequence."),
 ("Primary from the amino acid sequence, secondary from backbone interactions",
  "The four statements line up one to one: EK 1.7.A.3 gives primary structure to the specific sequence, EK 1.7.A.4 gives secondary structure to interactions between atoms of the backbone, EK 1.7.A.5 gives tertiary shape to hydrogen bonds, hydrophobic and ionic interactions and disulfide bridges, and EK 1.7.A.6 gives quaternary structure to interactions between multiple polypeptides."),
]

TABLE_CHECKS = {14: q14, 15: q15, 16: q16, 17: q17, 18: q18, 19: q19, 20: q20, 21: q21}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("b1_7_mutant")
        mod.TOPIC = b1_7.TOPIC
        mod.QUESTIONS = copy.deepcopy(b1_7.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            style(mod)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def third_ionic(mod, claims):
        mod.QUESTIONS[13]["table"] = dict(
            headers=b1_7._T_RESIDUES["headers"],
            rows=[[lab, ("ionic" if lab == "Position 41" else p)]
                  for lab, p in b1_7._T_RESIDUES["rows"]])

    def category_typo(mod, claims):
        mod.QUESTIONS[14]["table"] = dict(
            headers=b1_7._T_RESIDUES["headers"],
            rows=[[lab, ("nonpolar-ish" if lab == "Position 12" else p)]
                  for lab, p in b1_7._T_RESIDUES["rows"]])

    def counts_do_not_sum(mod, claims):
        mod.QUESTIONS[17]["table"] = dict(
            headers=b1_7._T_COMPOSITION["headers"],
            rows=[[lab, hb, ("100" if lab == "Protein B" else hl), io, tot]
                  for lab, hb, hl, io, tot in b1_7._T_COMPOSITION["rows"]])

    def variant_effect_erased(mod, claims):
        mod.QUESTIONS[19]["table"] = dict(
            headers=b1_7._T_VARIANTS["headers"],
            rows=[[lab, p, ("98" if lab == "Variant 2" else a)]
                  for lab, p, a in b1_7._T_VARIANTS["rows"]])

    print("negative controls:")
    must_fail("key moved off its anchor", lambda m, c: m.QUESTIONS[8].__setitem__("ans", 1))
    must_fail("anchor no longer in the keyed choice",
              lambda m, c: c.__setitem__(23, ("no such phrase", c[23][1])))
    must_fail("a third position given an ionic R group", third_ionic)
    must_fail("an R group category cell outside the framework's three", category_typo)
    must_fail("category counts no longer summing to the stated total", counts_do_not_sum)
    must_fail("a changed-category variant given full activity", variant_effect_erased)
    must_fail("a backslash macro in a choice",
              lambda m, c: m.QUESTIONS[3]["choices"].__setitem__(1, "Two: \\alpha and \\beta only"))
    print("all negative controls raised as required.")


import b1_7  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(b1_7)
cg.check(b1_7, CLAIMS, table_checks=TABLE_CHECKS)
