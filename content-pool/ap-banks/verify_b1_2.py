"""Key audit for AP BIOLOGY 1.2 Elements of Life.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here instead of reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is the shared one in ``cg_check.py``; nothing in it is
specific to another subject. It cannot tell whether the biology is right. That
is gated by the CLAIMS text and by the SCIENCE_BRIEF.md rule that every key must
trace to a sentence in the CED.

WHAT THE KEYS REST ON
---------------------
The whole topic has ONE essential knowledge statement, EK 1.2.A.1, with three
sub-points. Items 1, 2, 17 and 29 rest on its opening sentences: atoms and
molecules from the environment are necessary to build new molecules, and carbon,
hydrogen and oxygen are the most prevalent elements used to build carbohydrates,
proteins, lipids and nucleic acids. Items 3, 7, 15 and 18 rest on i (sulfur in
proteins); items 4, 12, 19, 23, 27 and 30 on ii (phosphorus in phospholipids, a
type of lipid, and in nucleic acids); items 5 and 24 on iii (nitrogen in nucleic
acids). Items 20, 22 and 25 turn on the CONTRAST between the general sentence
and the sub-points and are keyed to that contrast rather than to a single line.

Two items reach beyond this topic and say so. Item 26 chains to EK 1.6.A.1,
which lists a phosphate and a nitrogenous base among a nucleotide's components,
and item 28 chains to EK 1.7.A.1 and EK 1.7.A.2, which put an amine group on
every amino acid. EK 1.2.A.1 iii names nitrogen only for nucleic acids, so
nitrogen in protein is NOT asserted from this topic alone.

Item 21 is an experimental-design item; its key rests on the logic of isolating
one variable, not on a content sentence.

DATA ITEMS: 6 to 16 carry tables. Every keyed conclusion is recomputed below
from the table alone and the distractors are falsified against the same numbers.

NEGATIVE CONTROL: ``python3 verify_b1_2.py --selftest`` corrupts a key, an
anchor, a table cell and the notation on purpose and confirms each check fails.
"""
import re
import sys

import cg_check as cg

# SCIENCE_BRIEF.md: Biology is exported as prose, so a backslash macro would print
# raw and a digit-hyphen-digit or digit-slash-digit is what the converter mangled
# on the prose subjects. Explicit lookarounds, never \b beside a digit.
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


C = "Carbon (percent by mass)"
H = "Hydrogen (percent by mass)"
O = "Oxygen (percent by mass)"
N = "Nitrogen (percent by mass)"
P = "Phosphorus (percent by mass)"
S = "Sulfur (percent by mass)"
SS = "Sulfur supplied (millimolar)"
PS = "Phosphorus supplied (millimolar)"
NS = "Nitrogen supplied (millimolar)"
DENS = "Cell density after 24 hours (millions of cells per milliliter)"
PCT = "Percentage of the dry mass of one bacterial species"
PROT = "Radioactivity recovered in the purified protein fraction (counts per minute)"
NUC = "Radioactivity recovered in the purified nucleic acid fraction (counts per minute)"


def _only_cho(table):
    return [lab for lab in cg.labels(table)
            if cg.cell(table, lab, N) == 0 and cg.cell(table, lab, P) == 0
            and cg.cell(table, lab, S) == 0]


def q6(table, item):
    hits = _only_cho(table)
    assert hits == ["Sample W"], f"samples with no N, P or S: {hits}"
    for lab in cg.labels(table):
        assert cg.cell(table, lab, C) > 0 and cg.cell(table, lab, H) > 0 \
            and cg.cell(table, lab, O) > 0, f"{lab} is missing one of the three prevalent elements"
    return ("exactly one row is zero in the nitrogen, phosphorus and sulfur columns while "
            "carbon, hydrogen and oxygen are nonzero in every row")


def q7(table, item):
    hits = [lab for lab in cg.labels(table) if cg.cell(table, lab, S) > 0]
    assert hits == ["Sample X"], f"samples containing sulfur: {hits}"
    return f"the sulfur column is nonzero for exactly one row, {hits[0]}, so 'every sample' is false"


def q8(table, item):
    both = [lab for lab in cg.labels(table)
            if cg.cell(table, lab, N) > 0 and cg.cell(table, lab, P) > 0]
    assert both == ["Sample Y"], f"samples with both nitrogen and phosphorus: {both}"
    n_only = [lab for lab in cg.labels(table)
              if cg.cell(table, lab, N) > 0 and cg.cell(table, lab, P) == 0]
    p_only = [lab for lab in cg.labels(table)
              if cg.cell(table, lab, P) > 0 and cg.cell(table, lab, N) == 0]
    assert n_only and p_only, "the near-miss distractors need one N-only and one P-only row"
    return (f"exactly one row carries both, with {n_only[0]} nitrogen-only and "
            f"{p_only[0]} phosphorus-only, so 'two of the samples' is false")


def q9(table, item):
    hits = [lab for lab in cg.labels(table)
            if cg.cell(table, lab, P) > 0 and cg.cell(table, lab, N) == 0
            and cg.cell(table, lab, S) == 0]
    assert hits == ["Sample Z"], f"phosphorus without nitrogen or sulfur: {hits}"
    return ("exactly one row has phosphorus with neither nitrogen nor sulfur, which "
            "excludes the nucleic acid and the protein readings")


def q10(table, item):
    lab = [l for l in cg.labels(table) if cg.cell(table, l, C) == 37]
    assert len(lab) == 1, f"the stem's 37 percent carbon matches {lab}"
    total = sum(cg.cell(table, lab[0], h) for h in (C, H, O))
    assert total == 73, f"carbon plus hydrogen plus oxygen recomputes to {total}"
    rest = sum(cg.cell(table, lab[0], h) for h in (N, P, S))
    assert total + rest == 100, "the row must sum to 100 for the complement to hold"
    assert rest == 27, f"the complement recomputes to {rest}, not 27"
    return f"37 plus 4 plus 32 is {total:.0f}; the remaining {rest:.0f} is nitrogen and phosphorus"


def q11(table, item):
    hits = [lab for lab in cg.labels(table) if cg.cell(table, lab, SS) == 0]
    assert hits == ["Culture 2"], f"cultures with no sulfur: {hits}"
    full = [lab for lab in cg.labels(table)
            if all(cg.cell(table, lab, h) > 0 for h in (SS, PS, NS))]
    assert len(full) == 1, f"exactly one fully supplied culture expected, got {full}"
    assert cg.cell(table, hits[0], DENS) < cg.cell(table, full[0], DENS), \
        "the sulfur-free culture must grow less than the complete one"
    return (f"exactly one culture was given no sulfur and it reached "
            f"{cg.cell(table, hits[0], DENS)} against {cg.cell(table, full[0], DENS)} for the complete medium")


def q12(table, item):
    hits = [lab for lab in cg.labels(table) if cg.cell(table, lab, PS) == 0]
    assert hits == ["Culture 3"], f"cultures with no phosphorus: {hits}"
    return (f"exactly one row records zero phosphorus supplied, {hits[0]}, and phosphorus "
            "is the only element the framework assigns to two classes")


def q13(table, item):
    full = cg.cell(table, "Culture 1", DENS)
    nos = [lab for lab in cg.labels(table) if cg.cell(table, lab, SS) == 0]
    ratio = full / cg.cell(table, nos[0], DENS)
    assert abs(ratio - 8) < 0.05, f"the ratio recomputes to {ratio}"
    return f"9.6 divided by 1.2 is {ratio:.0f}, so the eightfold reading is the only one that fits"


def q14(table, item):
    three = sum(cg.cell(table, e, PCT) for e in ("Carbon", "Hydrogen", "Oxygen"))
    assert three == 78, f"carbon plus hydrogen plus oxygen recomputes to {three}"
    top3 = sum(sorted(cg.col(table, PCT), reverse=True)[:3])
    assert top3 == 84, f"the three largest entries sum to {top3}, so the 84 distractor is not the trap it should be"
    assert sum(cg.col(table, PCT)) == 100, "the column must sum to 100"
    return (f"50 plus 8 plus 20 is {three:.0f}; the three LARGEST entries sum to "
            f"{top3:.0f}, which is the distractor")


def q15(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, PCT)))
    smallest = min(vals, key=vals.get)
    assert smallest == "Sulfur", f"the smallest entry is {smallest}"
    return f"sulfur's {vals['Sulfur']:.0f} percent is the minimum of {sorted(vals.values())}"


def q16(table, item):
    j = table["headers"].index("Radioactive element added to the medium")
    elem = {r[0]: r[j] for r in table["rows"]}
    prot = {lab: cg.cell(table, lab, PROT) for lab in cg.labels(table)}
    nuc = {lab: cg.cell(table, lab, NUC) for lab in cg.labels(table)}
    s_lab = [k for k, v in elem.items() if v == "Sulfur"][0]
    p_lab = [k for k, v in elem.items() if v == "Phosphorus"][0]
    assert prot[s_lab] > 10 * nuc[s_lab], "the sulfur culture must label protein far more"
    assert nuc[p_lab] > 10 * prot[p_lab], "the phosphorus culture must label nucleic acid far more"
    return (f"{s_lab} (sulfur) gives {prot[s_lab]:.0f} counts in protein against "
            f"{nuc[s_lab]:.0f} in nucleic acid, and {p_lab} (phosphorus) the reverse")


CLAIMS = [
 ("Carbon, hydrogen and oxygen",
  "EK 1.2.A.1, near verbatim: carbon, hydrogen, and oxygen are the most prevalent elements used to build biological molecules. Sulfur, phosphorus and nitrogen appear in the statement only as additions tied to particular classes."),
 ("Carbohydrates, proteins, lipids and nucleic acids",
  "EK 1.2.A.1 names exactly these four as the biological molecules built from the prevalent elements. Minerals, salts, vitamins and water are not on that list, and enzymes are proteins rather than a fifth class."),
 ("Proteins",
  "EK 1.2.A.1 i, verbatim in substance: sulfur is used in the building of proteins. It is the only class the sulfur sub-point names."),
 ("Phospholipids and nucleic acids",
  "EK 1.2.A.1 ii: phosphorus is used in the building of phospholipids, which the statement identifies as a type of lipid, and of nucleic acids. Those are the only two users of phosphorus the statement gives."),
 ("Nitrogen",
  "EK 1.2.A.1 iii: nitrogen is used in the building of nucleic acids, and EK 1.2.A.1 ii already supplies phosphorus to the same class. Calcium, iron and sodium appear nowhere in EK 1.2.A.1."),
 ("Sample W",
  "Recomputed in q6 above: exactly one row is zero in the nitrogen, phosphorus and sulfur columns, leaving only the three elements EK 1.2.A.1 calls most prevalent, and no sub-point assigns any further element to carbohydrates."),
 ("Sample X",
  "Recomputed in q7 above: the sulfur column is nonzero for exactly one row, and EK 1.2.A.1 i is what makes sulfur the protein marker."),
 ("Sample Y",
  "Recomputed in q8 above: exactly one row is nonzero in both the nitrogen and the phosphorus column, the pair EK 1.2.A.1 ii and iii assign to nucleic acids, with a nitrogen-only and a phosphorus-only row as the near misses."),
 ("A phospholipid",
  "Recomputed in q9 above, then read against EK 1.2.A.1: phosphorus points to a phospholipid or a nucleic acid, absent nitrogen rules out the nucleic acid under EK 1.2.A.1 iii, and absent sulfur rules out the protein under EK 1.2.A.1 i."),
 ("73 percent",
  "Recomputed in q10 above by summing the carbon, hydrogen and oxygen columns of the row the stem identifies. The row sums to 100, so the 27 percent distractor is its complement."),
 ("Culture 2",
  "Recomputed in q11 above: exactly one culture was supplied no sulfur, and its final density is far below the fully supplied culture's. EK 1.2.A.1 i is what makes sulfur the element whose absence reaches proteins."),
 ("Culture 3",
  "Recomputed in q12 above: exactly one row records zero phosphorus supplied. EK 1.2.A.1 ii is the only sub-point that names two classes for one element, which is what the stem asks for."),
 ("Eight times",
  "Recomputed in q13 above from the two tabulated densities. The comparison is what licenses calling the withheld element limiting, in the sense of EK 1.2.A.1 that atoms from the environment are necessary to build new molecules."),
 ("78 percent",
  "Recomputed in q14 above: the three elements EK 1.2.A.1 names sum to 78. The 84 distractor is the sum of the three LARGEST entries, which swaps nitrogen for hydrogen, and the check confirms it really is 84."),
 ("Sulfur",
  "Recomputed in q15 above: sulfur holds the smallest tabulated share of any single element, and EK 1.2.A.1 i nonetheless names it as used in the building of proteins."),
 ("first culture is incorporated mainly into protein",
  "Recomputed in q16 above: the sulfur culture labels the protein fraction far more heavily and the phosphorus culture the nucleic acid fraction, which is the pattern EK 1.2.A.1 i and ii predict."),
 ("cannot create the elements it needs",
  "EK 1.2.A.1 opens by stating that atoms and molecules from the environment are necessary to build new molecules. Building means assembling supplied atoms, so neither creating elements nor absorbing finished polymers is what the statement describes."),
 ("Protein synthesis will be impaired before carbohydrate synthesis",
  "EK 1.2.A.1 i assigns sulfur to proteins alone, while EK 1.2.A.1 makes carbohydrates a matter of carbon, hydrogen and oxygen, none of which the scenario withholds. The two classes therefore cannot be affected equally."),
 ("Phospholipids",
  "EK 1.2.A.1 ii is the only sub-point naming phosphorus, and the scenario supplies nitrogen while withholding phosphorus, so the shortage falls on a phosphorus user. Carbohydrates require none of the three additional elements."),
 ("nitrogen is not a requirement of every class",
  "EK 1.2.A.1 makes carbon, hydrogen and oxygen the general building elements and EK 1.2.A.1 iii adds nitrogen only for nucleic acids, so a carbohydrate is a counterexample to the student's universal claim."),
 ("differ only in whether phosphorus is present",
  "Attributing a growth difference to phosphorus requires phosphorus to be the only difference between treatments, and replication is what separates a difference from noise. Withholding two elements at once confounds them, and a single culture supplies no baseline."),
 ("first is a protein and the second is a nucleic acid",
  "EK 1.2.A.1 i assigns sulfur to proteins; EK 1.2.A.1 ii and iii assign phosphorus and nitrogen together to nucleic acids. A phospholipid would carry phosphorus rather than sulfur, so the pairing is fixed by the two element sets."),
 ("used both in a type of lipid and in nucleic acids",
  "EK 1.2.A.1 ii states that phosphorus is used in the building of phospholipids, which it calls a type of lipid, and of nucleic acids. That spans two classes and no more; proteins take sulfur under EK 1.2.A.1 i."),
 ("Nucleic acids",
  "EK 1.2.A.1 iii states that nitrogen is used in the building of nucleic acids. Sugars, complex carbohydrates, steroids and fatty acids are not assigned nitrogen anywhere in EK 1.2.A.1."),
 ("measurable amount of nitrogen",
  "EK 1.2.A.1 assigns carbon, hydrogen and oxygen to biological molecules generally and adds nitrogen only for nucleic acids in EK 1.2.A.1 iii, so nitrogen is the element whose presence is inconsistent with a pure carbohydrate. Solubility is not an elemental claim at all."),
 ("phosphate supplies the phosphorus and the nitrogenous base supplies the nitrogen",
  "Chained to EK 1.6.A.1, which lists a five-carbon sugar, a phosphate and a nitrogenous base as a nucleotide's components. That places phosphorus in the phosphate and nitrogen in the base, matching the pair EK 1.2.A.1 ii and iii assign to nucleic acids."),
 ("more consistent with phospholipid remains",
  "EK 1.2.A.1 ii gives phosphorus two users. EK 1.2.A.1 iii adds nitrogen to nucleic acids and EK 1.2.A.1 i adds sulfur to proteins, so with both of those absent only the phospholipid reading survives."),
 ("obtain nitrogen as well as the sulfur",
  "Chained to EK 1.7.A.1 and EK 1.7.A.2, which place an amine group on every amino acid; an amine group contains nitrogen. EK 1.2.A.1 iii names nitrogen only for nucleic acids, so the protein statements are where this chain has to run."),
 ("supplied from outside the organism and are reassembled",
  "EK 1.2.A.1 states that atoms and molecules from the environment are necessary to build new molecules. Nothing in the framework has an organism creating atoms, transmuting elements, or storing intact polymers unchanged."),
 ("Phosphorus",
  "EK 1.2.A.1 ii is the only sub-point that names two classes for a single element: phospholipids, a type of lipid, and nucleic acids, the molecules that store hereditary information. Sulfur reaches only proteins and nitrogen only nucleic acids."),
]

TABLE_CHECKS = {6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 13: q13,
                14: q14, 15: q15, 16: q16}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("b1_2_mutant")
        mod.TOPIC = b1_2.TOPIC
        mod.QUESTIONS = copy.deepcopy(b1_2.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            style(mod)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    print("negative controls:")
    must_fail("key moved off its anchor",
              lambda m, c: m.QUESTIONS[2].__setitem__("ans", 3))
    must_fail("anchor no longer in the keyed choice",
              lambda m, c: c.__setitem__(4, ("no such phrase", c[4][1])))
    must_fail("sulfur added to a second sample, breaking q7's uniqueness",
              lambda m, c: m.QUESTIONS[6].__setitem__("table", dict(
                  headers=b1_2._T_SAMPLES["headers"],
                  rows=[r[:6] + ["3"] if r[0] == "Sample Y" else list(r)
                        for r in b1_2._T_SAMPLES["rows"]])))
    must_fail("a dry mass percentage altered so the 78 total is wrong",
              lambda m, c: m.QUESTIONS[13].__setitem__("table", dict(
                  headers=b1_2._T_DRYMASS["headers"],
                  rows=[[e, ("12" if e == "Hydrogen" else v)]
                        for e, v in b1_2._T_DRYMASS["rows"]])))
    must_fail("a backslash macro in a choice",
              lambda m, c: m.QUESTIONS[0]["choices"].__setitem__(1, "\\alpha and oxygen"))
    must_fail("a why naming an option by letter",
              lambda m, c: m.QUESTIONS[1].__setitem__(
                  "why", "Choice C is wrong because the framework never lists salts among "
                         "the four classes of biological molecule."))
    print("all negative controls raised as required.")


import b1_2  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(b1_2)
cg.check(b1_2, CLAIMS, table_checks=TABLE_CHECKS)
