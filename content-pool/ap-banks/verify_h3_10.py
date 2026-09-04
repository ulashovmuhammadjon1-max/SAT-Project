"""Key audit for AP CHEMISTRY 3.10 Solubility.

One (anchor, claim) per item, in module order.

THE TOPIC IS ONE SENTENCE: EK 3.10.A.1, substances with similar intermolecular
interactions tend to be miscible or soluble in one another. Two words in it do
all the work and both are easy to lose, so both are guarded.

``similarity_not_strength`` refuses any key that makes a substance dissolve
because its own intermolecular forces are STRONG. EK 3.10.A.1 names similarity
between the two substances, not strength in either; two substances held together
tightly but differently are exactly what it does not predict will mix. The
misconception is offered as a distractor so a student meets it, and the check
asserts it is offered.

``tendency_not_guarantee`` refuses any key promising that similar interactions
ALWAYS dissolve. The sentence's verb is tend to. Again the over-claim is offered
and the check asserts it is.

WHAT THE KEYS REST ON.

  3.10.A.1 alone      1, 2, 3, 14, 15, 20, 21, 22, 26, 27, 28, 30
  3.10.A.1 with 3.1.A.1 (London dispersion where nothing else is available)
                      4, 13, 18, 25
  3.10.A.1 with 3.1.A.2 (polar interactions; ion-dipole between ions and polar
  molecules, stronger than dipole-dipole)      5, 6, 7, 8, 9, 23, 29
  3.10.A.1 with 3.1.A.4 (hydrogen bonding needs H on N, O or F)
                      10, 12, 24, 25
  suggested skill 4.D, the particulate-to-macroscopic connection      11, 26
  the learning objective's own scope                                  19

THE TABLES ARE RECOMPUTED BY MATCHING, NOT BY MEMORY. The interaction tables
carry text rather than numbers, so the checks read each substance's tabulated
interaction and compare it against the interaction the STEM attributes to the
solvent. A key survives only if that match picks out its row and no other. The
solubility table is compared numerically.

NEGATIVE CONTROL: ``python3 verify_h3_10.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h3_10

INTERACTION = "Strongest intermolecular interaction its molecules can form"
FIRST = "Interaction available to the first substance"
SECOND = "Interaction available to the second substance"
WATERSOL = "Solubility in water (g per 100 g of water)"
HEXSOL = "Solubility in hexane (g per 100 g of hexane)"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below)(?![a-z])", re.I)

# Units 4 and 7 own the solubility rules and the solubility product.
_OTHER_TOPIC = re.compile(
    r"(?<![A-Za-z])(solubility product|Ksp|solubility rules|net ionic|"
    r"common-ion effect|precipitate)(?![A-Za-z])", re.I)

# The misconception EK 3.10.A.1's word "similar" exists to head off.
#
# THE NEGATED-PHRASE TRAP, caught by this module's own run. The first version of
# the second pattern listed "how strong they are on their own", which is a
# fragment of item 22's CORRECT key: "what matters is whether its interactions
# are similar to the solvent's, NOT how strong they are on their own". The check
# rejected a right answer for containing the phrase it was written to reject
# asserting. That is the same family as this project's `\bpi` and LETTER_REF
# bugs, and the fix is the same: an explicit lookbehind, so a phrase introduced
# by "not" is a denial of the misconception rather than an instance of it.
_STRENGTH_ALONE = re.compile(
    r"(?<![a-z])(?:because|since)\s+"
    r"(?:its|their|the\s+[a-z]+(?:\s+[a-z]+)?'s)\s+(?:own\s+)?"
    r"(?:intermolecular\s+)?forces?\s+(?:are|is)\s+(?:too\s+)?"
    r"(?:strong|stronger|the strongest)(?![a-z])", re.I)
_STRENGTH_ALONE_ALT = re.compile(
    r"(?<!not )(?<![a-z])(?:both sets of forces are strong|"
    r"strong forces always attract|how strong its interactions are)(?![a-z])", re.I)

# The over-claim EK 3.10.A.1's verb "tend to" heads off.
_GUARANTEE = re.compile(
    r"(?<![a-z])(?:always\s+(?:dissolves?|soluble|dissolve in one another)|"
    r"dissolves? completely|allows no exceptions|"
    r"always\s+soluble in one another)(?![a-z])", re.I)


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
    print(f"OK  {module.TOPIC[0]} figures: every set of solubility data is carried as a "
          "table.")


def no_other_topic(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _OTHER_TOPIC.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: uses {hit.group(0)!r}, which is unit 4's or unit "
                f"7's material -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no solubility rules, no solubility product and no "
          "precipitation; the topic stays on intermolecular interactions.")


def similarity_not_strength(module):
    """EK 3.10.A.1 names SIMILAR interactions, never strong ones."""
    offered = []
    for i, item in enumerate(module.QUESTIONS, 1):
        for k, choice in enumerate(item["choices"]):
            hit = _STRENGTH_ALONE.search(choice) or _STRENGTH_ALONE_ALT.search(choice)
            if not hit:
                continue
            assert k != item["ans"], (
                f"{module.TOPIC[0]} q{i}: the key attributes dissolving to the absolute "
                f"strength of a substance's own forces ({hit.group(0)!r}); EK 3.10.A.1 names "
                "the SIMILARITY of the two substances' interactions"
            )
            offered.append((i, k))
    assert len(offered) >= 3, (
        f"the strength-alone misconception is offered only {len(offered)} time(s), so this "
        "check has almost nothing to distinguish and proves little"
    )
    print(f"OK  {module.TOPIC[0]} similarity guard: the strength-alone misconception is "
          f"offered at {offered} and keyed nowhere.")


def tendency_not_guarantee(module):
    """EK 3.10.A.1's verb is TEND TO. No key may promise an outcome."""
    offered = []
    for i, item in enumerate(module.QUESTIONS, 1):
        for k, choice in enumerate(item["choices"]):
            hit = _GUARANTEE.search(choice)
            if not hit:
                continue
            assert k != item["ans"], (
                f"{module.TOPIC[0]} q{i}: the key promises an outcome ({hit.group(0)!r}), but "
                "EK 3.10.A.1 says substances with similar interactions TEND TO be miscible "
                "or soluble"
            )
            offered.append((i, k))
    assert len(offered) >= 2, (
        f"the guarantee over-claim is offered only {len(offered)} time(s), so this check has "
        "almost nothing to distinguish and proves little"
    )
    print(f"OK  {module.TOPIC[0]} hedge: the guarantee over-claim is offered at {offered} and "
          "keyed nowhere.")


SWAP_ITEMS = {
    6: ("Poor solubility", "interactions are not similar"),
    25: ("tend not to mix", "only London dispersion forces while the other hydrogen bonds"),
}


def swap_anchors_carry_both_clauses(module, claims):
    """Where a distractor keeps the verdict and swaps the reason, pin both."""
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
          "and the reason together, each with a half-swapped distractor present.")


# ----------------------------------------------------------------- table items

def _interactions(table, header):
    return {str(r[0]): cg.normalize(
        r[[cg.normalize(x) for x in table["headers"]].index(cg.normalize(header))])
        for r in table["rows"]}


def _solvent_interaction(stem):
    """What the STEM says the solvent's molecules do. Read, never remembered."""
    text = cg.normalize(stem)
    if "hydrogen bonds" in text or "hydrogen bonding" in text:
        return "hydrogen bonding"
    if "only london dispersion forces" in text:
        return "london dispersion forces only"
    raise AssertionError(
        f"the stem names no solvent interaction, so the match cannot be recomputed: "
        f"{stem[:100]!r}"
    )


def _match(table, item, header=INTERACTION):
    want = _solvent_interaction(item["q"])
    have = _interactions(table, header)
    hits = sorted(lab for lab, v in have.items() if v == want)
    assert len(hits) == 1, (
        f"exactly one tabulated solute must share the solvent's interaction {want!r}; "
        f"{hits} do, from {have}"
    )
    return hits[0], have, want


def q12(table, item):
    lab, have, want = _match(table, item)
    assert lab == "Solute 2", f"the hydrogen-bonding tabulated solute is {lab}: {have}"
    h.shows(item, lab)
    return (f"the stem gives the solvent {want!r} and the tabulated interactions {have} match "
            f"it at exactly one row, {lab}")


def q13(table, item):
    lab, have, want = _match(table, item)
    assert lab == "Solute 1", f"the dispersion-only tabulated solute is {lab}: {have}"
    h.shows(item, lab)
    return (f"the stem gives the solvent {want!r} and the tabulated interactions {have} match "
            f"it at exactly one row, {lab}")


def _pair_matches(table):
    firsts = _interactions(table, FIRST)
    seconds = _interactions(table, SECOND)
    return {lab: firsts[lab] == seconds[lab] for lab in firsts}, firsts, seconds


def q14(table, item):
    alike, firsts, seconds = _pair_matches(table)
    unlike = sorted(lab for lab, same in alike.items() if not same)
    assert unlike == ["Pair 2"], f"the tabulated pairs with unlike interactions are {unlike}"
    h.shows(item, unlike[0])
    return (f"comparing the two tabulated interactions row by row, {firsts} against {seconds}, "
            f"exactly one pair differs: {unlike[0]}")


def q15(table, item):
    alike, firsts, seconds = _pair_matches(table)
    same = sorted(lab for lab, ok in alike.items() if ok)
    assert len(same) == 3, f"the tabulated pairs with matching interactions are {same}"
    word = {0: "None of them", 1: "Exactly one", 2: "Exactly two", 3: "Exactly three",
            4: "All four of them"}[len(same)]
    h.shows(item, word)
    return (f"comparing {firsts} against {seconds} row by row, {len(same)} tabulated pairs "
            f"match: {same}")


def _sols(table):
    w = dict(zip(cg.labels(table), cg.col(table, WATERSOL)))
    x = dict(zip(cg.labels(table), cg.col(table, HEXSOL)))
    return w, x


def q16(table, item):
    w, x = _sols(table)
    ratios = {lab: w[lab] / x[lab] for lab in w}
    top = max(ratios, key=ratios.get)
    assert top == "Solute P", f"the most water-preferring tabulated solute is {top}: {ratios}"
    assert ratios[top] > 100.0, (
        f"the preference must be decisive rather than marginal: {ratios[top]}"
    )
    others = [v for lab, v in ratios.items() if lab != top]
    assert all(v < ratios[top] for v in others), f"the maximum is not unique: {ratios}"
    h.shows(item, top)
    return (f"the tabulated water-to-hexane solubility ratios recompute as {ratios}, whose "
            f"decisive maximum is at {top}")


def q17(table, item):
    w, x = _sols(table)
    ratios = {lab: w[lab] / x[lab] for lab in w}
    balanced = sorted(lab for lab, v in ratios.items() if 0.5 < v < 2.0)
    assert balanced == ["Solute R"], f"the tabulated solutes alike in both solvents are {balanced}"
    h.shows(item, balanced[0])
    return (f"the tabulated water-to-hexane ratios recompute as {ratios}, and exactly one sits "
            f"near unity: {balanced[0]}")


def q18(table, item):
    w, x = _sols(table)
    ratios = {lab: x[lab] / w[lab] for lab in w}
    top = max(ratios, key=ratios.get)
    assert top == "Solute Q", f"the most hexane-preferring tabulated solute is {top}: {ratios}"
    assert ratios[top] > 100.0, f"the preference must be decisive: {ratios[top]}"
    others = [v for lab, v in ratios.items() if lab != top]
    assert all(v < ratios[top] for v in others), f"the maximum is not unique: {ratios}"
    h.shows(item, top)
    return (f"the tabulated hexane-to-water solubility ratios recompute as {ratios}, whose "
            f"decisive maximum is at {top}")


TABLE_CHECKS = {12: q12, 13: q13, 14: q14, 15: q15, 16: q16, 17: q17, 18: q18}

NUMERIC = {}


CLAIMS = [
 ("tend to be miscible or soluble in one another",
  "EK 3.10.A.1 in full: substances with similar intermolecular interactions tend to be miscible or soluble in one another."),
 ("A general expectation rather than a guarantee",
  "EK 3.10.A.1's verb is tend to, which states a pattern without promising it holds in every case."),
 ("Their intermolecular interactions being similar to each other",
  "EK 3.10.A.1 names SIMILAR intermolecular interactions, not strong ones, and says nothing about masses or melting points."),
 ("soluble in one another, because their interactions are similar",
  "EK 3.1.A.1 leaves both substances with London dispersion forces, so the two are alike, and EK 3.10.A.1 makes similarity the ground of the expectation."),
 ("because both rely on interactions between polar molecules",
  "EK 3.1.A.2 makes dipole-dipole interactions those present between polar molecules, so both substances bring the same kind, which is EK 3.10.A.1's condition."),
 ("Poor solubility, because the two substances' intermolecular interactions are not similar",
  "EK 3.1.A.1 and EK 3.1.A.2 leave the two substances with unlike interactions, and EK 3.10.A.1 attaches its expectation of mixing to similarity. The anchor carries verdict and reason together because a distractor keeps the verdict and swaps the reason."),
 ("since the two substances' interactions are unlike each other",
  "EK 3.10.A.1 turns on similarity, and here one substance relies on dipole-dipole interactions under EK 3.1.A.2 while the other has only London dispersion forces under EK 3.1.A.1."),
 ("Ion-dipole forces of attraction",
  "EK 3.1.A.2 states that ion-dipole forces of attraction are present between ions and polar molecules and tend to be stronger than dipole-dipole forces."),
 ("since no ion-dipole interaction is available",
  "EK 3.1.A.2 places ion-dipole forces between ions and POLAR molecules, so a solvent with no dipole offers nothing comparable and EK 3.10.A.1's expectation does not apply."),
 ("because both substances can take part in hydrogen bonding",
  "EK 3.1.A.4 defines hydrogen bonding for hydrogen covalently bonded to nitrogen, oxygen or fluorine, which describes both substances, and EK 3.10.A.1 expects such a pair to dissolve."),
 ("A particulate-level property, the intermolecular interactions, to a macroscopic property, solubility",
  "EK 3.10.A.1 predicts a bulk observation from interactions between particles, which is the connection suggested skill 4.D asks a student to explain."),
 ("Solute 2",
  "EK 3.10.A.1 with EK 3.1.A.4. q12 reads the solvent's interaction out of the stem and checks exactly one tabulated solute matches it."),
 ("Solute 1",
  "EK 3.10.A.1 with EK 3.1.A.1. q13 reads the solvent's interaction out of the stem and checks exactly one tabulated solute matches it."),
 ("Pair 2",
  "EK 3.10.A.1 attaches its expectation to SIMILAR interactions. q14 compares the two tabulated entries row by row and checks exactly one pair differs."),
 ("Exactly three",
  "The same comparison counted across the whole table. Recomputed in q15."),
 ("Solute P",
  "EK 3.10.A.1 makes similarity the reason substances dissolve, so a decisive preference for the hydrogen-bonding solvent indicates which interactions the solute's own resemble. q16 recomputes every tabulated ratio and requires the preference to exceed a hundredfold."),
 ("Solute R",
  "A solute whose two tabulated figures are close resembles both solvents, which EK 3.10.A.1's TEND TO leaves room for. q17 recomputes the ratios and checks exactly one sits near unity."),
 ("Solute Q",
  "The mirrored reading of the same table, with EK 3.1.A.1 naming the nonpolar solvent's London dispersion forces. Recomputed in q18."),
 ("Ionic and molecular compounds, in aqueous and nonaqueous solvents",
  "Learning objective 3.10.A names both kinds of compound and both kinds of solvent, and ties all of it to the intermolecular interactions between particles."),
 ("because the framework says such substances TEND TO be miscible or soluble",
  "EK 3.10.A.1's verb states a general pattern rather than an exceptionless rule, so one pair that does not follow it leaves the sentence standing."),
 ("not expected to mix, since their interactions are not similar",
  "EK 3.10.A.1 names similarity and not absolute strength, so two substances each held together tightly but differently do not meet its condition."),
 ("whether its interactions are similar to the solvent's",
  "EK 3.10.A.1 states the condition as similar intermolecular interactions between the two substances; strength on its own says nothing about whether the solvent can offer comparable interactions."),
 ("Ion-dipole forces tend to be the stronger of the two",
  "EK 3.1.A.2 says ion-dipole forces are present between ions and polar molecules and tend to be stronger than dipole-dipole forces."),
 ("miscible, because their intermolecular interactions are similar",
  "EK 3.1.A.4 makes hydrogen bonding a single named kind of interaction, so two liquids that both take part in it meet EK 3.10.A.1's condition."),
 ("tend not to mix, since one has only London dispersion forces while the other hydrogen bonds",
  "EK 3.1.A.4 requires hydrogen bonded to nitrogen, oxygen or fluorine, which carbon and hydrogen alone cannot supply, leaving EK 3.1.A.1's London dispersion forces. The anchor carries verdict and reason together because a distractor keeps the verdict and swaps the reason."),
 ("as a tendency rather than as a rule",
  "EK 3.10.A.1 reasons from particle interactions to whether bulk samples mix, and its verb marks the limit of how far the model reaches -- both halves of what suggested skill 4.D asks about."),
 ("The molar mass of each substance",
  "EK 3.10.A.1 mentions intermolecular interactions, their similarity, and the miscibility or solubility that follows, and nothing else."),
 ("tend not to be soluble in one another",
  "EK 3.10.A.1 attaches the expectation of mixing to similar interactions, so a pair failing that condition carries the opposite expectation; the sentence is about dissolving rather than reacting."),
 ("since a polar solvent can offer ion-dipole interactions to the ions",
  "EK 3.1.A.2 places ion-dipole forces between ions and polar molecules without restricting them to water, and learning objective 3.10.A explicitly covers nonaqueous solvents."),
 ("Substances with similar intermolecular interactions tend to be miscible or soluble in one another",
  "EK 3.10.A.1 verbatim, with each part carrying weight: similarity rather than strength, a tendency rather than a certainty, and mixing rather than reacting."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[15]["q"] = "In the graph above, which solute prefers water?"
        no_figure_language(mod)

    def other_topic(mod, cl):
        mod.QUESTIONS[0]["q"] = (mod.QUESTIONS[0]["q"]
                                 + " Use the solubility rules to decide.")
        no_other_topic(mod)

    def strength_alone_keyed(mod, cl):
        mod.QUESTIONS[21]["ans"] = 1
        cl[21] = ("What matters is how strong its interactions are", cl[21][1])
        similarity_not_strength(mod)

    def strength_distractors_removed(mod, cl):
        for item in mod.QUESTIONS:
            item["choices"] = [
                _STRENGTH_ALONE_ALT.sub("whether the two substances are alike",
                                        _STRENGTH_ALONE.sub("because it is a liquid", c))
                for c in item["choices"]]
        similarity_not_strength(mod)

    def guarantee_keyed(mod, cl):
        mod.QUESTIONS[1]["ans"] = 1
        cl[1] = ("every pair with similar interactions dissolves completely", cl[1][1])
        tendency_not_guarantee(mod)

    def guarantee_distractors_removed(mod, cl):
        for item in mod.QUESTIONS:
            item["choices"] = [_GUARANTEE.sub("often mix", c) for c in item["choices"]]
        tendency_not_guarantee(mod)

    def swap_anchor_halved(mod, cl):
        cl[5] = ("Poor solubility", cl[5][1])
        swap_anchors_carry_both_clauses(mod, cl)

    def hydrocarbon_anchor_halved(mod, cl):
        cl[24] = ("tend not to mix", cl[24][1])
        swap_anchors_carry_both_clauses(mod, cl)

    def two_solutes_match_the_solvent(mod, cl):
        mod.QUESTIONS[11]["table"] = dict(
            headers=h3_10._T_SOLUTES["headers"],
            rows=[["Solute 1", "London dispersion forces only"],
                  ["Solute 2", "Hydrogen bonding"],
                  ["Solute 3", "Hydrogen bonding"]])

    def solvent_interaction_dropped_from_the_stem(mod, cl):
        mod.QUESTIONS[12]["q"] = ("The tabulated solutes are each added instead to a "
                                  "different solvent. Which is expected to be the most "
                                  "soluble?")

    def a_second_pair_made_unlike(mod, cl):
        mod.QUESTIONS[13]["table"] = dict(
            headers=h3_10._T_PAIRS["headers"],
            rows=[["Pair 1", "Hydrogen bonding", "Dipole-dipole interactions"],
                  ["Pair 2", "London dispersion forces only", "Hydrogen bonding"],
                  ["Pair 3", "Dipole-dipole interactions", "Dipole-dipole interactions"],
                  ["Pair 4", "London dispersion forces only",
                   "London dispersion forces only"]])

    def pair_count_changes(mod, cl):
        mod.QUESTIONS[14]["table"] = dict(
            headers=h3_10._T_PAIRS["headers"],
            rows=[["Pair 1", "Hydrogen bonding", "Hydrogen bonding"],
                  ["Pair 2", "London dispersion forces only", "Hydrogen bonding"],
                  ["Pair 3", "Dipole-dipole interactions", "Hydrogen bonding"],
                  ["Pair 4", "London dispersion forces only",
                   "London dispersion forces only"]])

    def preference_made_marginal(mod, cl):
        # A solute that dissolves only twice as well in water as in hexane does
        # not indicate anything decisive about which interactions its own
        # resemble, even though it is still the maximum.
        mod.QUESTIONS[15]["table"] = dict(
            headers=h3_10._T_SOLB["headers"],
            rows=[["Solute P", "36.0", "18.0"], ["Solute Q", "0.02", "28.0"],
                  ["Solute R", "15.0", "14.0"]])

    def balanced_solute_unbalanced(mod, cl):
        mod.QUESTIONS[16]["table"] = dict(
            headers=h3_10._T_SOLB["headers"],
            rows=[["Solute P", "36.0", "0.01"], ["Solute Q", "0.02", "28.0"],
                  ["Solute R", "15.0", "0.5"]])

    def hexane_preference_moved(mod, cl):
        mod.QUESTIONS[17]["table"] = dict(
            headers=h3_10._T_SOLB["headers"],
            rows=[["Solute P", "36.0", "0.01"], ["Solute Q", "28.0", "0.02"],
                  ["Solute R", "15.0", "14.0"]])

    return [
        ("a stem referring to a graph the bank cannot show", figure_language),
        ("unit 4's solubility rules creeping in", other_topic),
        ("the strength-alone misconception promoted to a key", strength_alone_keyed),
        ("every strength-alone distractor removed, so that guard would run over an empty set",
         strength_distractors_removed),
        ("the guarantee over-claim promoted to a key", guarantee_keyed),
        ("every guarantee distractor removed, so the hedge check would be idle",
         guarantee_distractors_removed),
        ("the nonpolar-in-polar anchor cut to the verdict only", swap_anchor_halved),
        ("the hydrocarbon anchor cut to the verdict only", hydrocarbon_anchor_halved),
        ("two tabulated solutes made to share the solvent's interaction",
         two_solutes_match_the_solvent),
        ("the solvent's interaction dropped from a stem the table check reads it from",
         solvent_interaction_dropped_from_the_stem),
        ("a second tabulated pair made unlike", a_second_pair_made_unlike),
        ("a tabulated pair changed so the miscible count moves", pair_count_changes),
        ("the water preference cut to a factor of two, which indicates nothing decisive",
         preference_made_marginal),
        ("the balanced tabulated solute made lopsided", balanced_solute_unbalanced),
        ("the tabulated hexane preference reversed", hexane_preference_moved),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h3_10, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h3_10)
no_other_topic(h3_10)
similarity_not_strength(h3_10)
tendency_not_guarantee(h3_10)
swap_anchors_carry_both_clauses(h3_10, CLAIMS)
h.run(h3_10, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
