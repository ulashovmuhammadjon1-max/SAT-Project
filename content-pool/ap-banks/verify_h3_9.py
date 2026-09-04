"""Key audit for AP CHEMISTRY 3.9 Separation of Solutions and Mixtures.

One (anchor, claim) per item, in module order.

THE HOLE IN THE SOURCE IS THE MAIN THING THIS FILE GUARDS. EK 3.9.A.1 has a
second sub-point whose text is absent from the CED PDF's text layer -- the page
ends at a bare "ii." and the next page opens topic 3.10. The Biology CED has one
such gap too, and SCIENCE_RESUME.md records how it was handled: key only what
the surviving text supports and do not complete it from memory.
``no_unsourced_method`` enforces that here. No key may name distillation,
evaporation, crystallisation or centrifugation as a method the framework offers.
Those words appear only in distractors, where each is wrong for a reason that
does not depend on the missing sub-point, and the check asserts they appear so
it cannot pass over an empty set.

THE DIRECTION OF TRAVEL. EK 3.9.A.1 says chromatography exploits the
DIFFERENTIAL STRENGTH of intermolecular interactions and that the chromatogram
can be used to infer relative polarities. It does not say that a species held
harder by the stationary phase travels a shorter distance. So
``retention_convention_stated`` asserts that every item whose key depends on
that convention states it in its own stem.

WHAT THE KEYS REST ON.

  the opening sentence -- filtration cannot separate a liquid solution's
  components, and processes exploiting differences in intermolecular
  interactions can                             1, 2, 8, 19, 20, 22, 25, 28, 30
  sub-point i -- the three named forms, the differential strength, the mobile
  and stationary phases, and the polarity inference
                                     3, 4, 5, 6, 7, 9, 18, 21, 26, 27, 29
  sub-point i applied to a tabulated chromatogram   10, 11, 12, 13, 14, 15, 16, 17
  sub-point i with EK 3.1.A.2 for the polarity items        12, 17, 24

ARITHMETIC. Eight tabulated items are recomputed from the distances alone, and
two of them assert the answer is NOT readable from a single column.

NEGATIVE CONTROL: ``python3 verify_h3_9.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h3_9

DIST = "Distance travelled by the component (cm)"
FRONT = "Distance travelled by the solvent front (cm)"
POLARD = "Distance on the polar stationary phase (cm)"
NONPOLARD = "Distance on the nonpolar stationary phase (cm)"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below|the chromatogram above|"
    r"the chromatogram below)(?![a-z])", re.I)

# Methods this source does not attribute to the framework. The missing
# sub-point ii very probably names one of them; a probable guess is still a
# guess, so none of them may be keyed.
_UNSOURCED = re.compile(
    r"(?<![A-Za-z])(distillation|distilling|evaporation|crystallisation|"
    r"crystallization|centrifugation)(?![A-Za-z])", re.I)

# The convention the CED does not supply, which each dependent stem must.
RETENTION_ITEMS = (10, 11, 12, 14, 15, 16, 17, 24)
_CONVENTION = re.compile(
    r"(?<![a-z])interacts more strongly with the stationary phase travels a shorter "
    r"distance(?![a-z])", re.I)


def _facing(item):
    out = [item["q"], item["why"]] + list(item["choices"])
    t = item.get("table")
    if t:
        out += [str(x) for x in t["headers"]]
        out += [str(c) for r in t["rows"] for c in r]
    return out


def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, which this bank "
                f"cannot show -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: every chromatogram is carried as a table of "
          "distances.")


def no_unsourced_method(module):
    """Nothing may be keyed to the sub-point this source does not carry."""
    offered = []
    for i, item in enumerate(module.QUESTIONS, 1):
        for k, choice in enumerate(item["choices"]):
            hit = _UNSOURCED.search(choice)
            if not hit:
                continue
            assert k != item["ans"], (
                f"{module.TOPIC[0]} q{i}: the key names {hit.group(0)!r} as a method the "
                "framework offers, but EK 3.9.A.1's second sub-point is missing from this "
                "source and nothing may be keyed to a guess about it"
            )
            offered.append((i, k))
        hit = _UNSOURCED.search(item["why"])
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: the rationale asserts something about {hit.group(0)!r}, "
            "which this source does not attribute to the framework"
        )
    assert len(offered) >= 2, (
        f"the unsourced methods appear only {len(offered)} time(s) as distractors, so this "
        "check has almost nothing to distinguish and proves little"
    )
    print(f"OK  {module.TOPIC[0]} source gap: the methods this source does not carry appear "
          f"only as distractors, at {offered}, and never in a key or a rationale.")


def retention_convention_stated(module):
    """The CED does not say a stronger hold means a shorter run. Each stem must."""
    for i in RETENTION_ITEMS:
        stem = module.QUESTIONS[i - 1]["q"]
        assert _CONVENTION.search(stem), (
            f"{module.TOPIC[0]} q{i}: the key depends on a stronger interaction meaning a "
            f"shorter distance travelled, and the stem never states it; EK 3.9.A.1 does not "
            f"supply that direction -- {stem[:110]!r}"
        )
    print(f"OK  {module.TOPIC[0]} convention: all {len(RETENTION_ITEMS)} items whose keys turn "
          "on retention state the direction in their own stems rather than borrowing it from "
          "the framework, which does not give it.")


# ----------------------------------------------------------------- table items

def _unique_extreme(mapping, want_max, what):
    pick = (max if want_max else min)(mapping, key=mapping.get)
    tied = [k for k, v in mapping.items() if abs(v - mapping[pick]) < 1e-12]
    assert tied == [pick], f"the {what} is not unique: {tied} in {mapping}"
    return pick


def _plate(table):
    return dict(zip(cg.labels(table), cg.col(table, DIST)))


def q10(table, item):
    ds = _plate(table)
    held = _unique_extreme(ds, False, "shortest tabulated distance")
    assert held == "Component 1", f"the shortest tabulated distance is {held}: {ds}"
    h.shows(item, held)
    return (f"the tabulated distances are {ds}, whose unique minimum is at {held}, which the "
            "stem's convention makes the most strongly held")


def q11(table, item):
    ds = _plate(table)
    free = _unique_extreme(ds, True, "longest tabulated distance")
    assert free == "Component 2", f"the longest tabulated distance is {free}: {ds}"
    h.shows(item, free)
    return (f"the tabulated distances are {ds}, whose unique maximum is at {free}, which the "
            "stem's convention makes the least strongly held")


def q12(table, item):
    ds = _plate(table)
    least_polar = _unique_extreme(ds, True, "longest tabulated distance")
    assert least_polar == "Component 2", f"the longest tabulated distance is {least_polar}: {ds}"
    fronts = cg.col(table, FRONT)
    assert len(set(fronts)) == 1, f"one plate must have one solvent front: {fronts}"
    h.shows(item, least_polar)
    return (f"on the single tabulated plate, with one solvent front of {fronts[0]:g} cm, the "
            f"furthest travelled is {least_polar} among {ds}, so a polar surface holds it "
            "least")


def q13(table, item):
    ratios = {lab: cg.cell(table, lab, DIST) / cg.cell(table, lab, FRONT)
              for lab in cg.labels(table)}
    above = sorted(lab for lab, v in ratios.items() if v > 0.5 + 1e-12)
    assert above == ["Component 2"], f"the components past half the front are {above}: {ratios}"
    word = {0: "None of them", 1: "Exactly one", 2: "Exactly two", 3: "All three"}[len(above)]
    h.shows(item, word)
    return (f"the tabulated ratios of component distance to solvent front recompute as "
            f"{ratios}, of which {len(above)} exceed one half: {above}")


def _two_plates(table):
    polar = dict(zip(cg.labels(table), cg.col(table, POLARD)))
    nonpolar = dict(zip(cg.labels(table), cg.col(table, NONPOLARD)))
    return polar, nonpolar


def q14(table, item):
    polar, _non = _two_plates(table)
    held = _unique_extreme(polar, False, "shortest distance on the polar plate")
    assert held == "Component X", f"the shortest polar-plate distance is {held}: {polar}"
    h.shows(item, held)
    return (f"the tabulated polar-plate distances are {polar}, whose unique minimum is at "
            f"{held}")


def q15(table, item):
    polar, nonpolar = _two_plates(table)
    gaps = {lab: abs(polar[lab] - nonpolar[lab]) for lab in polar}
    same = sorted(lab for lab, g in gaps.items() if g < 1e-12)
    assert same == ["Component Z"], f"the components alike on both plates are {same}: {gaps}"
    h.shows(item, same[0])
    return (f"the tabulated differences between the two plates are {gaps}, and exactly one "
            f"component reads the same on both: {same[0]}")


def q16(table, item):
    polar, nonpolar = _two_plates(table)
    labs = list(polar)
    pairs = [(a, b) for i, a in enumerate(labs) for b in labs[i + 1:]
             if abs(polar[a] - nonpolar[b]) < 1e-12 and abs(polar[b] - nonpolar[a]) < 1e-12
             and abs(polar[a] - polar[b]) > 1e-12]
    assert len(pairs) == 1, (
        f"exactly one tabulated pair must be each other's mirror image across the plates; "
        f"{pairs} are, from {polar} and {nonpolar}"
    )
    a, b = pairs[0]
    nums = sorted([str(a).split()[-1], str(b).split()[-1]])
    h.shows(item, f"Components {nums[0]} and {nums[1]}")
    return (f"the tabulated readings {polar} and {nonpolar} contain exactly one pair whose "
            f"two plates are exchanged: {a} and {b}")


def q17(table, item):
    polar, nonpolar = _two_plates(table)
    least = _unique_extreme(polar, True, "longest distance on the polar plate")
    assert least == "Component Y", f"the longest polar-plate distance is {least}: {polar}"
    assert nonpolar[least] < polar[least], (
        "the least polar component must also be held harder by the nonpolar surface, or the "
        f"two plates disagree: {polar} against {nonpolar}"
    )
    h.shows(item, least)
    return (f"the tabulated polar-plate distances are {polar}, whose unique maximum is at "
            f"{least}, and the same component runs only {nonpolar[least]:g} cm on the "
            "nonpolar plate, which agrees")


TABLE_CHECKS = {10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16, 17: q17}

NUMERIC = {}


CLAIMS = [
 ("They cannot be separated by filtration",
  "EK 3.9.A.1's opening sentence, unqualified: the components of a liquid solution cannot be separated by filtration."),
 ("differences in the intermolecular interactions of the components",
  "EK 3.9.A.1: they can be separated using processes that take advantage of differences in the intermolecular interactions of the components."),
 ("Paper, thin-layer, and column",
  "EK 3.9.A.1's first sub-point gives exactly that list in a parenthesis, and the same statement's opening sentence rules filtration out."),
 ("differential strength of intermolecular interactions",
  "EK 3.9.A.1's first sub-point: chromatography separates chemical species by taking advantage of the differential strength of intermolecular interactions."),
 ("The components of the solution",
  "EK 3.9.A.1's first sub-point names the components of the solution as the mobile phase, in a parenthesis, against the surface components of the stationary phase."),
 ("The surface components of the stationary phase",
  "EK 3.9.A.1's first sub-point specifies interactions with the SURFACE components of the stationary phase."),
 ("The relative polarities of components in a mixture",
  "EK 3.9.A.1's first sub-point ends with exactly that inference, and it is a comparison among the components rather than a value for any one of them."),
 ("It will not separate them, because the components of a liquid solution cannot be separated by filtration",
  "EK 3.9.A.1's opening sentence rules the method out for this kind of sample, which is the alignment judgement suggested skill 2.C asks for."),
 ("Paper chromatography, since the resulting chromatogram can be used to infer relative polarities",
  "EK 3.9.A.1's first sub-point sanctions that inference, so a chromatographic run is the procedure aligned to a question about relative polarity."),
 ("Component 1",
  "EK 3.9.A.1's differential-strength account with the convention the stem supplies. q10 recomputes the tabulated distances and checks the minimum is unique."),
 ("Component 2",
  "The same convention read the other way. q11 recomputes the tabulated distances and checks the maximum is unique."),
 ("Component 2",
  "EK 3.9.A.1 sanctions inferring relative polarities and EK 3.1.A.2 makes a polar surface hold a polar species harder. q12 recomputes the distances and checks the plate has a single solvent front."),
 ("Exactly one",
  "Each tabulated component distance compared with the tabulated solvent front. Recomputed in q13."),
 ("Component X",
  "EK 3.9.A.1 makes interaction with the surface components of the stationary phase the basis of the separation. q14 recomputes the polar-plate distances."),
 ("Component Z",
  "A component the two surfaces hold about equally shows no difference between the plates. q15 recomputes both columns and checks exactly one component matches."),
 ("Components X and Y",
  "EK 3.9.A.1's differential strength allows one surface to hold what another barely holds. q16 recomputes both columns and checks exactly one pair is each other's mirror image."),
 ("Component Y",
  "EK 3.9.A.1's polarity inference with EK 3.1.A.2. q17 recomputes the polar-plate maximum and checks the nonpolar plate agrees, so the two runs do not contradict each other."),
 ("Those between and among the components of the solution, and those with the surface components of the stationary phase",
  "EK 3.9.A.1's first sub-point names both sets of interactions, and dropping either half loses part of what the sentence attributes the separation to."),
 ("the components differ from one another in how strongly they interact",
  "EK 3.9.A.1's first sub-point attributes the separation to the DIFFERENTIAL strength of the interactions, which is a comparison between species."),
 ("They will not be separated from each other",
  "EK 3.9.A.1's first sub-point makes the differential strength the thing the method exploits, so where there is no difference there is nothing to exploit."),
 ("Gas chromatography",
  "EK 3.9.A.1's first sub-point gives the list as paper, thin-layer, and column, which has three entries and does not include this one."),
 ("Its surface components, which interact with the species being separated",
  "EK 3.9.A.1's first sub-point names interactions with the surface components of the stationary phase; separating by size is what the opening sentence rules out."),
 ("Running a chromatogram with a polar stationary phase and comparing how far each dye travels",
  "EK 3.9.A.1's first sub-point makes interaction with the stationary phase the basis of the separation and the chromatogram its record, which is the procedure alignment suggested skill 2.C asks for."),
 ("The nonpolar substance, since a polar surface holds a polar substance more strongly",
  "EK 3.1.A.2 makes interactions between polar molecules typically greater than those between nonpolar molecules of comparable size, EK 3.9.A.1 makes that difference the basis of the separation, and the stem's convention turns a stronger hold into a shorter distance. The anchor carries verdict and reason together because a distractor keeps one and swaps the other."),
 ("Filtration",
  "EK 3.9.A.1's opening sentence names filtration specifically as what cannot separate the components of a liquid solution."),
 ("ranks the components against one another rather than giving an absolute polarity",
  "EK 3.9.A.1's first sub-point speaks of the RELATIVE polarities of components in a mixture, which orders them without fixing a value for any one."),
 ("Differences in the strength of their intermolecular interactions with the mobile and stationary phases",
  "EK 3.9.A.1's first sub-point attributes the separation to the differential strength of intermolecular interactions among the solution's components and with the stationary phase's surface."),
 ("A liquid solution",
  "EK 3.9.A.1 begins with the components of a LIQUID SOLUTION, and EK 3.7.A.1 makes a solution a homogeneous mixture; a pure substance has no components to separate."),
 ("Which component of a mixture is the more polar",
  "EK 3.9.A.1's first sub-point sanctions inferring relative polarities from the chromatogram and no other inference; amounts and molar masses need other measurements."),
 ("cannot be separated by filtration, but they can be separated by processes that exploit differences in their intermolecular interactions",
  "EK 3.9.A.1's two halves in one statement: the method ruled out and the general description of what works."),
]


SWAP_ITEMS = {
    24: ("nonpolar substance", "polar surface holds a polar substance more strongly"),
}


def swap_anchors_carry_both_clauses(module, claims):
    for i, (clause_a, clause_b) in sorted(SWAP_ITEMS.items()):
        anchor = claims[i - 1][0]
        item = module.QUESTIONS[i - 1]
        has_a = cg.contains_phrase(anchor, clause_a)
        has_b = cg.contains_phrase(anchor, clause_b)
        assert has_a and has_b, (
            f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} must name both the verdict "
            f"{clause_a!r} and the reason {clause_b!r}; it carries "
            f"{'only the verdict' if has_a else 'only the reason' if has_b else 'neither'}"
        )
        half = [k for k, c in enumerate(item["choices"])
                if k != item["ans"]
                and cg.contains_phrase(c, clause_a) != cg.contains_phrase(c, clause_b)]
        assert half, (
            f"{module.TOPIC[0]} q{i}: no distractor carries exactly one of the two clauses, "
            "so this item is not the half-swap case the check is for"
        )
    print(f"OK  {module.TOPIC[0]} swap guard: {len(SWAP_ITEMS)} anchor(s) carry the verdict "
          "and the reason together, with a half-swapped distractor present.")


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[9]["q"] = "In the chromatogram above, which component moved least?"
        no_figure_language(mod)

    def unsourced_method_keyed(mod, cl):
        mod.QUESTIONS[2]["ans"] = 1
        cl[2] = ("Paper, distillation, and evaporation", cl[2][1])
        no_unsourced_method(mod)

    def unsourced_method_in_a_rationale(mod, cl):
        mod.QUESTIONS[1]["why"] = (mod.QUESTIONS[1]["why"]
                                   + " The framework's second sub-point names distillation.")
        no_unsourced_method(mod)

    def unsourced_methods_removed(mod, cl):
        # A control on the CONTROL: with the words gone everywhere, the guard
        # would pass over an empty set.
        for item in mod.QUESTIONS:
            item["choices"] = [_UNSOURCED.sub("sedimentation", c) for c in item["choices"]]
        no_unsourced_method(mod)

    def convention_dropped(mod, cl):
        mod.QUESTIONS[9]["q"] = ("The table reports how far each component of a mixture "
                                 "travelled on one plate. Which component interacts most "
                                 "strongly with the stationary phase?")
        retention_convention_stated(mod)

    def polarity_anchor_halved(mod, cl):
        cl[23] = ("The nonpolar substance", cl[23][1])
        swap_anchors_carry_both_clauses(mod, cl)

    def plate_distances_tied(mod, cl):
        mod.QUESTIONS[9]["table"] = dict(
            headers=h3_9._T_CHROM["headers"],
            rows=[["Component 1", "2.0", "8.0"], ["Component 2", "6.0", "8.0"],
                  ["Component 3", "2.0", "8.0"]])

    def plate_distances_reversed(mod, cl):
        mod.QUESTIONS[10]["table"] = dict(
            headers=h3_9._T_CHROM["headers"],
            rows=[["Component 1", "6.0", "8.0"], ["Component 2", "2.0", "8.0"],
                  ["Component 3", "4.0", "8.0"]])

    def two_solvent_fronts_on_one_plate(mod, cl):
        mod.QUESTIONS[11]["table"] = dict(
            headers=h3_9._T_CHROM["headers"],
            rows=[["Component 1", "2.0", "8.0"], ["Component 2", "6.0", "9.0"],
                  ["Component 3", "4.0", "8.0"]])

    def ratio_count_changes(mod, cl):
        mod.QUESTIONS[12]["table"] = dict(
            headers=h3_9._T_CHROM["headers"],
            rows=[["Component 1", "2.0", "8.0"], ["Component 2", "6.0", "8.0"],
                  ["Component 3", "5.0", "8.0"]])

    def mirror_pair_broken(mod, cl):
        mod.QUESTIONS[15]["table"] = dict(
            headers=h3_9._T_TWO["headers"],
            rows=[["Component X", "1.0", "7.0"], ["Component Y", "6.0", "1.0"],
                  ["Component Z", "4.0", "4.0"]])

    def second_component_alike_on_both(mod, cl):
        mod.QUESTIONS[14]["table"] = dict(
            headers=h3_9._T_TWO["headers"],
            rows=[["Component X", "1.0", "1.0"], ["Component Y", "7.0", "1.0"],
                  ["Component Z", "4.0", "4.0"]])

    def two_plates_disagree(mod, cl):
        # The component furthest along the polar plate made ALSO the furthest
        # along the nonpolar one: the two runs then contradict each other and
        # the polarity inference has no ground.
        mod.QUESTIONS[16]["table"] = dict(
            headers=h3_9._T_TWO["headers"],
            rows=[["Component X", "1.0", "7.0"], ["Component Y", "7.0", "8.0"],
                  ["Component Z", "4.0", "4.0"]])

    return [
        ("a stem referring to a chromatogram the bank cannot show", figure_language),
        ("an unsourced separation method promoted to a key", unsourced_method_keyed),
        ("a rationale asserting what the missing sub-point says",
         unsourced_method_in_a_rationale),
        ("every unsourced method removed, so that guard would run over an empty set",
         unsourced_methods_removed),
        ("a retention item stripped of the convention its stem must supply", convention_dropped),
        ("the polarity anchor cut to the verdict only", polarity_anchor_halved),
        ("two tabulated components tied for the shortest run", plate_distances_tied),
        ("the tabulated distances reversed under the key", plate_distances_reversed),
        ("two different solvent fronts on what the stem calls one plate",
         two_solvent_fronts_on_one_plate),
        ("a tabulated distance moved so the count past half the front changes",
         ratio_count_changes),
        ("the mirror-image pair broken", mirror_pair_broken),
        ("a second component made to read alike on both plates", second_component_alike_on_both),
        ("the two plates made to disagree about which component is held least",
         two_plates_disagree),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h3_9, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h3_9)
no_unsourced_method(h3_9)
retention_convention_stated(h3_9)
swap_anchors_carry_both_clauses(h3_9, CLAIMS)
h.run(h3_9, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
