"""Key audit for AP BIOLOGY 2.1 Cell Structure and Function.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here instead of reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is the shared one in ``cg_check.py``. It cannot tell whether
the biology is right; that is gated by the CLAIMS text and by the
SCIENCE_BRIEF.md rule that every key must trace to a sentence in the CED.

WHAT THE KEYS REST ON, statement by statement
---------------------------------------------
EK 2.1.A.1 ribosomes: items 1, 2, 3 and 21.
EK 2.1.A.2 endomembrane system: items 4, 5 and 30.
EK 2.1.A.3 endoplasmic reticulum: item 6; sub-point i, items 7 and 29;
sub-point ii, items 8 and 28.
EK 2.1.A.4 Golgi complex: items 9, 10, 30, and its illustrative example item 11.
EK 2.1.A.5 mitochondria: items 12, 13, 20, 22, 23 and 24.
EK 2.1.A.6 lysosomes: items 14, 15, 26 and 27.
EK 2.1.A.7 vacuoles: item 16; sub-point i, item 17; sub-point ii, items 18 and 25.
EK 2.1.A.8 chloroplasts: items 19 and 20.

Items 6 to 8 and 28 to 29 all turn on the SAME split the CED draws between rough
and smooth endoplasmic reticulum, and each claim names which of the two
sub-points the key comes from, because that split is where a wrong key would be
easiest to write and hardest to see.

OUT OF SCOPE ON PURPOSE. Compartmentalization as a general principle is topic
2.9 and the endosymbiotic origin of mitochondria and chloroplasts is topic 2.10.
Neither is keyed here, even though item 2 does quote EK 2.1.A.1's own common
ancestry clause, which belongs to this topic.

DATA ITEMS: 22 to 26 carry tables. Every keyed conclusion is recomputed below
from the table alone, and each table is labelled hypothetical because the CED
prints no organelle counts or rates.

NEGATIVE CONTROL: ``python3 verify_b2_1.py --selftest`` corrupts a key, an
anchor, two table columns and the notation on purpose and confirms each fails.
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


NMITO = "Mean number of mitochondria per cell"
RESP = "Rate of aerobic cellular respiration (arbitrary units)"
AREA = "Inner membrane surface area per mitochondrion (square micrometers)"
ATP = "ATP synthesized per minute (arbitrary units)"
NVAC = "Mean number of vacuoles per cell"
VVAC = "Mean volume of the largest vacuole (cubic micrometers)"
ENZ = "Hydrolytic enzyme activity inside lysosomes (units)"
UNDIG = "Undigested material accumulated per cell (arbitrary units)"


def _monotone(pairs, rising):
    """pairs sorted by the first column; True if the second moves one way throughout."""
    pairs = sorted(pairs)
    if rising:
        return all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1))
    return all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1))


def q22(table, item):
    pairs = list(zip(cg.col(table, NMITO), cg.col(table, RESP)))
    assert _monotone(pairs, rising=True), f"respiration must rise with mitochondrial number: {sorted(pairs)}"
    fewest = min(pairs)[0]
    assert min(pairs)[1] == min(r for _, r in pairs), \
        f"the row with fewest mitochondria ({fewest}) must not hold the highest rate"
    assert len(set(r for _, r in pairs)) > 1, "'every cell type the same rate' must be false"
    return f"sorted by mitochondrial number the rates are {[r for _, r in sorted(pairs)]}, strictly rising"


def q23(table, item):
    pairs = list(zip(cg.col(table, AREA), cg.col(table, ATP)))
    assert _monotone(pairs, rising=True), f"ATP must rise with inner membrane area: {sorted(pairs)}"
    assert min(pairs)[1] == min(a for _, a in pairs), \
        "the least-area preparation must not hold the most ATP"
    return f"sorted by inner membrane area the ATP rates are {[a for _, a in sorted(pairs)]}, strictly rising"


def q24(table, item):
    ratios = [a / s for s, a in zip(cg.col(table, AREA), cg.col(table, ATP))]
    assert max(ratios) - min(ratios) < 0.5, f"ATP per square micrometer is not near constant: {ratios}"
    assert 4.5 < sum(ratios) / len(ratios) < 5.5, f"the mean ratio is {sum(ratios) / len(ratios)}, not about five"
    # the doubling and halving distractors must be false on the same numbers
    assert not all(ratios[i] * 1.8 < ratios[i + 1] for i in range(len(ratios) - 1)), \
        "'roughly doubles' must be false"
    assert not all(ratios[i] > 1.8 * ratios[i + 1] for i in range(len(ratios) - 1)), \
        "'falls to roughly half' must be false"
    return (f"ATP per square micrometer is {[round(r, 2) for r in ratios]}, all near five, "
            "so the total rises in proportion to the area")


def q25(table, item):
    plant_n, animal_n = cg.cell(table, "Plant cell", NVAC), cg.cell(table, "Animal cell", NVAC)
    plant_v, animal_v = cg.cell(table, "Plant cell", VVAC), cg.cell(table, "Animal cell", VVAC)
    assert animal_n > plant_n, f"the animal cell must hold more vacuoles: {animal_n} against {plant_n}"
    assert animal_v < plant_v, f"the animal cell's largest vacuole must be smaller: {animal_v} against {plant_v}"
    assert animal_n != plant_n, "'the same number' must be false"
    return (f"animal {animal_n:.0f} vacuoles against plant {plant_n:.0f}, and largest volumes "
            f"{animal_v:.0f} against {plant_v:.0f}")


def q26(table, item):
    pairs = list(zip(cg.col(table, ENZ), cg.col(table, UNDIG)))
    assert _monotone(pairs, rising=False), f"accumulation must fall as enzyme activity rises: {sorted(pairs)}"
    top_enzyme = max(pairs)
    assert top_enzyme[1] == min(u for _, u in pairs), \
        "the line with the greatest enzyme activity must hold the least undigested material"
    assert len(set(u for _, u in pairs)) > 1, "'every line the same' must be false"
    return (f"sorted by enzyme activity the accumulations are "
            f"{[u for _, u in sorted(pairs)]}, strictly falling")


CLAIMS = [
 ("Ribosomal RNA and protein",
  "EK 2.1.A.1 states that ribosomes are comprised of ribosomal RNA and protein. Messenger RNA is what a ribosome reads, and hydrolytic enzymes belong to lysosomes under EK 2.1.A.6."),
 ("found in cells in all forms of life, which reflects the common ancestry",
  "EK 2.1.A.1 states that these non-membrane subcellular structures are found in cells in all forms of life and reflect the common ancestry in all known life. Restricting them to one group of organisms contradicts the first half of that sentence."),
 ("synthesize proteins according to messenger RNA sequences",
  "EK 2.1.A.1, near verbatim. Digestion belongs to lysosomes under EK 2.1.A.6, packaging to the Golgi under EK 2.1.A.4, and lipid synthesis and detoxification to smooth ER under EK 2.1.A.3 ii."),
 ("The Golgi complex",
  "EK 2.1.A.2 lists endoplasmic reticulum, Golgi complex, lysosomes, vacuoles and transport vesicles, the nuclear envelope, and the plasma membrane as the endomembrane system. Ribosomes are non-membrane structures under EK 2.1.A.1, and mitochondria and chloroplasts are treated separately in EK 2.1.A.5 and EK 2.1.A.8."),
 ("modify, package, and transport polysaccharides",
  "EK 2.1.A.2 states that the group works together to modify, package, and transport polysaccharides, lipids, and proteins intercellularly. Aerobic respiration is EK 2.1.A.5's and photosynthesis is EK 2.1.A.8's."),
 ("Mechanical support that helps the cell maintain shape",
  "EK 2.1.A.3 states that endoplasmic reticulum provides mechanical support by helping cells maintain shape and plays a role in intracellular transport. The rejected options give functions EK 2.1.A.6, EK 2.1.A.7 i and EK 2.1.A.8 assign elsewhere."),
 ("membrane-bound ribosomes and helps carry out protein synthesis",
  "EK 2.1.A.3 i: rough ER is associated with membrane-bound ribosomes, allows for the compartmentalization of cells, and helps carry out protein synthesis. Detoxification and lipid synthesis are the SMOOTH ER functions of EK 2.1.A.3 ii, which is the split this item turns on."),
 ("Detoxification of cells and lipid synthesis",
  "EK 2.1.A.3 ii: smooth ER functions include the detoxification of cells and lipid synthesis. Protein synthesis and membrane-bound ribosomes belong to ROUGH ER in EK 2.1.A.3 i, the other half of the same split."),
 ("series of flattened membrane sacs",
  "EK 2.1.A.4 states that the Golgi complex is a membrane-bound structure consisting of a series of flattened membrane sacs. The convoluted inner membrane is the mitochondrion's under EK 2.1.A.5 and the enzyme-filled sac the lysosome's under EK 2.1.A.6."),
 ("Correctly folding and chemically modifying newly synthesized products",
  "EK 2.1.A.4 lists correctly folding and chemically modifying newly synthesized cellular products and packaging proteins for trafficking as the Golgi's functions. Protein synthesis from messenger RNA is the ribosome's under EK 2.1.A.1."),
 ("chemical modification of proteins that takes place within the Golgi",
  "The illustrative example printed with EK 2.1.A.4 is glycosylation and other chemical modifications of proteins that take place within the Golgi and determine protein function or targeting. It is attached to that statement and to no other."),
 ("Compartments for different metabolic reactions",
  "EK 2.1.A.5 states that mitochondria have a double membrane that provides compartments for different metabolic reactions involved in aerobic cellular respiration. Photosynthesis is EK 2.1.A.8's and mechanical support EK 2.1.A.3's."),
 ("outer membrane is smooth and the inner is highly convoluted, forming folds",
  "EK 2.1.A.5 states that the outer membrane is smooth while the inner membrane is highly convoluted, forming folds that enable ATP to be synthesized more efficiently. The rejected options reverse the two membranes or attach the wrong process to the folds."),
 ("Hydrolytic enzymes that digest material",
  "EK 2.1.A.6 states that lysosomes are membrane-enclosed sacs containing hydrolytic enzymes that digest material. Each rejected option names contents the framework assigns to a different organelle."),
 ("A role in programmed cell death",
  "EK 2.1.A.6 states that lysosomes also play a role in programmed cell death, which it names apoptosis. Lipid synthesis is smooth ER's under EK 2.1.A.3 ii and maintaining cell shape is ER's under EK 2.1.A.3."),
 ("Membrane-bound sacs that play many different roles",
  "EK 2.1.A.7 states that vacuoles are membrane-bound sacs that play many different roles, so confining them to one role contradicts it. The non-membrane description belongs to ribosomes under EK 2.1.A.1."),
 ("maintains turgor pressure through nutrient and water storage",
  "EK 2.1.A.7 i states that in plant cells a specialized large vacuole maintains turgor pressure through nutrient and water storage. Photosynthesis is EK 2.1.A.8's and digestion EK 2.1.A.6's."),
 ("smaller in size and more plentiful, and they store cellular materials",
  "EK 2.1.A.7 ii states that in animal cells vacuoles are smaller in size, are more plentiful than in plant cells, and store cellular materials. Turgor pressure is what EK 2.1.A.7 i assigns to the plant cell's large vacuole."),
 ("In plants and photosynthetic algae",
  "EK 2.1.A.8 states that chloroplasts are specialized organelles found in plants and photosynthetic algae and serve as the location for photosynthesis. Being found in all forms of life is EK 2.1.A.1's claim about ribosomes."),
 ("Mitochondria and chloroplasts",
  "EK 2.1.A.5 gives mitochondria a double membrane and EK 2.1.A.8 gives chloroplasts a double membrane. Ribosomes are non-membrane structures under EK 2.1.A.1 and the framework gives no second membrane to the Golgi, vacuoles or vesicles."),
 ("The ribosome",
  "EK 2.1.A.1 calls ribosomes non-membrane subcellular structures. Lysosomes are membrane-enclosed under EK 2.1.A.6, vacuoles membrane-bound under EK 2.1.A.7, the Golgi membrane-bound under EK 2.1.A.4, and chloroplasts double-membraned under EK 2.1.A.8."),
 ("more mitochondria carried out aerobic cellular respiration at higher rates",
  "Recomputed in q22 above: ranking the rows by mitochondrial number gives the same order as ranking them by respiration rate. EK 2.1.A.5 assigns the reactions of aerobic cellular respiration to the mitochondrion's compartments."),
 ("more inner membrane area synthesized more ATP",
  "Recomputed in q23 above: ATP synthesis rises at every step as inner membrane area rises. EK 2.1.A.5 states that the folds of the highly convoluted inner membrane enable ATP to be synthesized more efficiently, and calls the outer membrane smooth."),
 ("stays roughly constant",
  "Recomputed in q24 above: dividing ATP by area gives values clustered near five across all four preparations, and the doubling and halving readings are each checked false on the same numbers."),
 ("animal cell contained more vacuoles, and its largest vacuole was smaller",
  "Recomputed in q25 above from the four tabulated values. It is exactly the comparison EK 2.1.A.7 ii draws when it says animal vacuoles are smaller in size and more plentiful than in plant cells."),
 ("less hydrolytic enzyme activity accumulated more undigested material",
  "Recomputed in q26 above: accumulation rises at every step as enzyme activity falls. EK 2.1.A.6 states that lysosomes contain hydrolytic enzymes that digest material, so less activity leaves more undigested."),
 ("Material the cell would normally digest will accumulate",
  "EK 2.1.A.6 makes the hydrolytic enzymes of the lysosome what digests material, so disabling them removes the digestion. Protein synthesis is EK 2.1.A.1's and photosynthesis EK 2.1.A.8's, and neither depends on lysosomal enzymes."),
 ("Smooth endoplasmic reticulum, because the framework assigns",
  "EK 2.1.A.3 ii names the detoxification of cells among the functions of SMOOTH endoplasmic reticulum, while EK 2.1.A.3 i gives ROUGH ER membrane-bound ribosomes and protein synthesis. The rejected option attaches the correct function to the wrong sub-point."),
 ("Rough endoplasmic reticulum, because it is associated with membrane-bound",
  "EK 2.1.A.3 i states that rough ER is associated with membrane-bound ribosomes and helps carry out protein synthesis, and EK 2.1.A.1 makes ribosomes the structures that synthesize proteins. Lipid synthesis is the SMOOTH ER's role in EK 2.1.A.3 ii."),
 ("The Golgi complex",
  "EK 2.1.A.4 gives the Golgi both of the steps described: correctly folding and chemically modifying newly synthesized cellular products, and packaging proteins for trafficking. EK 2.1.A.2 places it inside the endomembrane system, which the stem specifies."),
]

TABLE_CHECKS = {22: q22, 23: q23, 24: q24, 25: q25, 26: q26}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("b2_1_mutant")
        mod.TOPIC = b2_1.TOPIC
        mod.QUESTIONS = copy.deepcopy(b2_1.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            style(mod)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def mito_trend_broken(mod, claims):
        mod.QUESTIONS[21]["table"] = dict(
            headers=b2_1._T_MITO["headers"],
            rows=[[lab, n, ("99" if lab == "Cell type 4" else r)]
                  for lab, n, r in b2_1._T_MITO["rows"]])

    def cristae_not_proportional(mod, claims):
        mod.QUESTIONS[23]["table"] = dict(
            headers=b2_1._T_CRISTAE["headers"],
            rows=[[lab, a, ("300" if lab == "Preparation 4" else t)]
                  for lab, a, t in b2_1._T_CRISTAE["rows"]])

    def vacuole_reversed(mod, claims):
        mod.QUESTIONS[24]["table"] = dict(
            headers=b2_1._T_VACUOLE["headers"],
            rows=[["Plant cell", "20", "900"], ["Animal cell", "14", "3"]])

    print("negative controls:")
    must_fail("key moved off its anchor", lambda m, c: m.QUESTIONS[7].__setitem__("ans", 1))
    must_fail("anchor no longer in the keyed choice",
              lambda m, c: c.__setitem__(18, ("no such phrase", c[18][1])))
    must_fail("a respiration rate altered so the trend is no longer monotone", mito_trend_broken)
    must_fail("an ATP value altered so the per-area ratio is no longer constant",
              cristae_not_proportional)
    must_fail("the plant cell given more vacuoles than the animal cell", vacuole_reversed)
    must_fail("a backslash macro in a stem",
              lambda m, c: m.QUESTIONS[11].__setitem__("q", "What does the \\emph{double} membrane provide?"))
    print("all negative controls raised as required.")


import b2_1  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(b2_1)
cg.check(b2_1, CLAIMS, table_checks=TABLE_CHECKS)
