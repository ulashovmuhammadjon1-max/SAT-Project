"""Key audit for AP CHEMISTRY 4.1 Introduction for Reactions.

One ``(anchor, claim)`` per item, in module order. The anchor must appear in the
KEYED choice and in no distractor, so an off-by-one key or a reordered choice
list fails here rather than reaching a student.

WHAT THE KEYS REST ON
---------------------
EK 4.1.A.1  A physical change occurs when a substance undergoes a change in
            properties but not a change in composition; changes of phase and
            the formation/separation of mixtures are common physical changes.
            (items 1, 3, 4, 6, 10, 11, 12, 13, 15, 16, 19, 22, 23, 24, 27, 30)
EK 4.1.A.2  A chemical change occurs when substances are transformed into new
            substances, typically with different compositions; production of
            heat or light, formation of a gas, formation of a precipitate and
            color change provide possible evidence that one has occurred.
            (items 2, 5, 6, 7, 8, 9, 14, 15, 17, 18, 20, 21, 25, 26, 28, 29, 30)

THE EVIDENCE LIST IS DATA, NOT PROSE. ``EVIDENCE_KINDS`` below holds EK
4.1.A.2's four observations exactly once, and both table checks classify their
own rows against that one set rather than against a hand-counted answer. So a
table row retyped into a different category is caught by the count, not by a
reader noticing.

q17 PARSES THE FORMULAS rather than trusting a label: it strips the phase
annotations from each tabulated cell and compares the SET of formulas before
with the set after, which is EK 4.1.A.2's own criterion of a change in
composition. A row whose formulas were mistyped fails there.

NO FIGURE LANGUAGE. The bank cannot carry images, so ``no_figure_language``
asserts that no stem or choice points at one.

NEGATIVE CONTROL: ``python3 verify_h4_1.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h4_1

KIND = "Kind of observation it is"
BEFORE = "Substances present before"
AFTER = "Substances present after"

# EK 4.1.A.2's list, written once and used by both table checks.
EVIDENCE_KINDS = {
    "production of heat or light",
    "formation of a gas",
    "formation of a precipitate",
    "color change",
}

_FIGURE = re.compile(
    r"(?<![a-z])(as shown|shown below|shown above|figure|image|picture|depicted|"
    r"pictured|illustrated|(?:diagram|graph|profile|curve|plot|chart)s?\s+"
    r"(?:above|below))(?![a-z])", re.I)

_PHASE = re.compile(r"\((?:s|l|g|aq)\)")


def no_figure_language(module):
    """No stem or choice may point at a picture this bank cannot show."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, but this bank "
                f"carries no images -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: no stem or choice points at a picture.")


def _kinds(table):
    """The tabulated observation kinds, lowercased, in row order."""
    return [cg.normalize(v) for v in
            [r[table["headers"].index(KIND)] for r in table["rows"]]]


def _formulas(cell):
    """The set of chemical formulas in a cell, with phase annotations dropped."""
    return {part.strip() for part in _PHASE.sub("", str(cell)).split(",")
            if part.strip()}


# ------------------------------------------------------------------ table items

def q8(table, item):
    kinds = _kinds(table)
    assert len(kinds) == len(set(kinds)), f"a repeated observation kind: {kinds}"
    listed = [k for k in kinds if k in {cg.normalize(e) for e in EVIDENCE_KINDS}]
    assert len(listed) == 3, (
        f"the tabulated kinds matching EK 4.1.A.2's list are {listed}"
    )
    h.shows(item, "Three of them")
    return (f"classifying the {len(kinds)} tabulated kinds against EK 4.1.A.2's four "
            f"named observations leaves {len(listed)} of them on the list")


def q17(table, item):
    labels = cg.labels(table)
    bi, ai = table["headers"].index(BEFORE), table["headers"].index(AFTER)
    changed = [row[0] for row in table["rows"]
               if _formulas(row[bi]) != _formulas(row[ai])]
    assert changed == ["P2", "P4"], (
        f"comparing the tabulated formulas before and after gives {changed}"
    )
    assert len(labels) == 4, f"the table lists {len(labels)} processes"
    h.shows(item, "P2 and P4")
    return (f"stripping the phase annotations and comparing each row's formulas gives a "
            f"change of composition in {changed} and in no other tabulated process")


def q28(table, item):
    kinds = _kinds(table)
    listed = {cg.normalize(e) for e in EVIDENCE_KINDS}
    outside = [row[0] for row, k in zip(table["rows"], kinds) if k not in listed]
    assert len(outside) == 1, f"tabulated observations outside EK 4.1.A.2's list: {outside}"
    assert "mass" in cg.normalize(outside[0]), (
        f"the one observation off the list should be the mass report, not {outside[0]!r}"
    )
    h.shows(item, "mass of the sealed flask was unchanged")
    return (f"exactly one of the {len(kinds)} tabulated kinds falls outside EK 4.1.A.2's "
            f"four named observations, and it is the report about {outside[0][:40]!r}")


TABLE_CHECKS = {8: q8, 17: q17, 28: q28}


CLAIMS = [
 ("change in properties but not a change in composition",
  "EK 4.1.A.1, near verbatim: a physical change occurs when a substance undergoes a change in properties but not a change in composition."),
 ("transformed into new substances, typically with different compositions",
  "EK 4.1.A.2, near verbatim. Phase change and mixing leave composition alone and are physical under EK 4.1.A.1."),
 ("phase of a substance among solid, liquid and gas",
  "EK 4.1.A.1 names changes in the phase of a substance among solid, liquid and gas as common physical changes; the other options are EK 4.1.A.2's evidence for a chemical change."),
 ("Both are physical changes",
  "EK 4.1.A.1 names formation and separation of mixtures of substances among common physical changes, and neither operation alters the composition of the sulfur or the iron."),
 ("The formation of a precipitate",
  "EK 4.1.A.2 lists production of heat or light, formation of a gas, formation of a precipitate, and color change as possible evidence of a chemical change."),
 ("change in the phase of the substance",
  "EK 4.1.A.2's list has four entries and a phase change is not among them; EK 4.1.A.1 puts phase change on the list of common PHYSICAL changes instead."),
 ("only possible evidence of a chemical change",
  "EK 4.1.A.2 introduces its observations as providing POSSIBLE evidence, and EK 4.1.A.1 makes boiling a phase change in which composition is unaltered."),
 ("Three of them",
  "Recomputed in q8 by classifying each tabulated kind against EK 4.1.A.2's four named observations."),
 ("new substance of different composition was formed and light was produced",
  "EK 4.1.A.2 makes transformation into new substances the criterion and offers production of heat or light as possible evidence; the residue does not behave as magnesium does."),
 ("same composition as a gas that it had as a liquid",
  "EK 4.1.A.1 makes a change in the phase of a substance a common physical change, since properties change while composition does not."),
 ("separating a mixture leaves the composition of each component unaltered",
  "EK 4.1.A.1 names formation and separation of mixtures of substances among common physical changes."),
 ("separates a mixture without altering the composition",
  "EK 4.1.A.1 covers this twice over: distillation is a pair of phase changes and it separates a mixture, and both are named as common physical changes."),
 ("dissolving formed a mixture without changing the composition",
  "EK 4.1.A.1 makes formation of a mixture a common physical change and defines a physical change as one without a change in composition; the recovered sugar is evidence of exactly that."),
 ("A gas will be given off and the residue will be a different color",
  "EK 4.1.A.2 offers formation of a gas and color change among the observations providing possible evidence of a chemical change, while warming and expansion accompany any heating."),
 ("dilution spreads the same dissolved substance through more water",
  "EK 4.1.A.2 offers color change as POSSIBLE evidence only, and EK 4.1.A.1 makes a change that leaves composition alone a physical change."),
 ("passed from solid to gas without any change in its composition",
  "EK 4.1.A.1 makes a change in the phase of a substance a common physical change, and EK 4.1.A.2's gas formation is evidence rather than proof."),
 ("P2 and P4",
  "Recomputed in q17 by comparing the set of formulas before and after for each tabulated process, which is EK 4.1.A.2's own criterion of a change in composition."),
 ("phase change releases energy while leaving the composition of the water alone",
  "EK 4.1.A.2 offers production of heat among its possible evidence rather than as a sufficient test, and EK 4.1.A.1 classes condensation as a phase change."),
 ("transformation into new substances of different composition",
  "EK 4.1.A.2 defines a chemical change this way and EK 4.1.A.1 makes unaltered composition the mark of a physical one, so composition settles the classification."),
 ("typically with compositions different from the original substances",
  "EK 4.1.A.2 reads that substances are transformed into new substances, typically with different compositions; the hedge is the framework's own."),
 ("possible evidence rather than as a requirement",
  "EK 4.1.A.2 says the four observations provide POSSIBLE evidence that a chemical change has occurred, which makes them indicators rather than a checklist every chemical change must satisfy."),
 ("composition was unaltered throughout",
  "EK 4.1.A.1 makes changes of phase common physical changes in which properties change but composition does not, and the recovered boiling point is evidence the substance is unchanged."),
 ("separation of a mixture leaves each dye with the composition it had in the ink",
  "EK 4.1.A.1 names separation of mixtures of substances among common physical changes; the colored bands were present in the ink from the start."),
 ("properties have changed while its composition has not",
  "EK 4.1.A.1 defines a physical change as a change in properties without a change in composition, which is what drawing a wire does."),
 ("glow and for a residue whose color differs",
  "EK 4.1.A.2 offers production of heat or light and color change among the observations that provide possible evidence, while warming under a lit burner accompanies any heating."),
 ("solid of a composition different from either gas",
  "EK 4.1.A.2 makes transformation into new substances of different composition the criterion for a chemical change, and a solid formed at the same temperature is neither gas in another phase."),
 ("exactly what a physical change is",
  "EK 4.1.A.1 defines a physical change as a change in properties but not a change in composition and names phase changes as common examples, so a large change in hardness is allowed by the definition."),
 ("mass of the sealed flask was unchanged",
  "Recomputed in q28, which finds the single tabulated observation falling outside EK 4.1.A.2's four; conservation of mass comes from EK 4.2.A.2 instead."),
 ("spectacular and leave composition alone",
  "EK 4.1.A.1 and EK 4.1.A.2 both turn on composition while EK 4.1.A.2's observations are only possible evidence, so appearance and composition can come apart in either direction."),
 ("behaves as the starting material did",
  "EK 4.1.A.1 makes unaltered composition the mark of a physical change and EK 4.1.A.2 makes new substances the mark of a chemical one, so testing the recovered material addresses the criterion itself."),
]


def _extra_mutations():
    def miscategorized_row(mod, cl):
        """A table row retyped into a category EK 4.1.A.2 does not list."""
        t = mod.QUESTIONS[7]["table"]
        mod.QUESTIONS[7]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], "Change in volume"] if "deep blue" in r[0] else list(r)
                  for r in t["rows"]])

    def formula_corrupted(mod, cl):
        """A composition row retyped so the before and after formulas agree."""
        t = mod.QUESTIONS[16]["table"]
        mod.QUESTIONS[16]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], r[1], "CaCO3(s)"] if r[0] == "P4" else list(r)
                  for r in t["rows"]])

    def off_list_row_added(mod, cl):
        """A second observation moved off EK 4.1.A.2's list, so the key is no longer unique."""
        t = mod.QUESTIONS[27]["table"]
        mod.QUESTIONS[27]["table"] = dict(
            headers=t["headers"],
            rows=[[r[0], "Change in volume"] if "bright orange" in r[0] else list(r)
                  for r in t["rows"]])

    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the diagram above, which change is physical?"
        no_figure_language(mod)

    return [("a tabulated observation retyped into an unlisted category", miscategorized_row),
            ("a composition row retyped so no change of composition remains", formula_corrupted),
            ("a second observation moved off the evidence list", off_list_row_added),
            ("a stem pointing at a picture the bank cannot show", figure_language)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h4_1, CLAIMS, table_checks=TABLE_CHECKS, mutations=_extra_mutations())

no_figure_language(h4_1)
h.run(h4_1, CLAIMS, table_checks=TABLE_CHECKS)
