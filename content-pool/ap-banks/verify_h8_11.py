"""Key audit for AP CHEMISTRY 8.11 pH and Solubility.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  8.11.A.1  a solubility is pH sensitive when a constituent ion is a weak acid,
            a weak base, or the hydroxide ion, and the effect is understood
            qualitatively with Le Chatelier's principle
                    1, 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 19, 20, 21,
                    22, 23, 24, 25, 26, 27, 28, 29, 30
  the exclusion attached to 8.11.A.1  computations of solubility as a function
            of pH are outside the exam                   3
  7.9.A.1   Le Chatelier's principle predicts the response to the addition or
            removal of a species -- the shift itself      4, 5, 9, 12, 28, 30
  7.10.A.2  a concentration change moves Q, a temperature change moves K, so a
            pH change cannot move Ksp                     14, 21
  7.11.A.1  dissolution is a reversible process whose extent Ksp describes  5, 14
  7.12.A.1  the common-ion effect, which is why a hydroxide salt is LESS soluble
            at high pH                                    7, 19, 21, 29
  8.2.A.1   the six strong acids, which is how a student decides whether an
            anion is the conjugate base of a WEAK acid    4, 8, 10, 11, 12, 26, 28
  8.6.A.1   i. strong acids have very weak conjugate bases; iv. carboxylate ions
            are common weak bases                         8, 11, 13, 22, 23, 27

THE EXCLUSION IS THE SHAPE OF THIS TOPIC, so it is gated rather than trusted.
``no_solubility_computation`` asserts that no stem asks for a calculation and
that no choice states a molarity -- a computed solubility would have to appear
as one. The exclusion statement item itself NAMES the excluded computation, so
the ban is on stems and choices asking for one, not on the phrase.

THE SWAP GUARD, which is the reason this verifier is longer than the topic
warrants. The whole content of 8.11 is a DIRECTION, and a direction is one
character away from its opposite. ``direction_guard`` does not read the key and
believe it. It carries, per item, the two facts the STEM supplies -- what was
added and what kind of ion the salt carries -- predicts the direction from EK
8.11.A.1 and EK 7.9.A.1 in a single function written once, and then requires:

  * the key to state that direction and no other. A key stating both, or
    neither, is rejected rather than read as one of them.
  * the anchor to state it too, and to be long enough to carry the key's REASON
    as well. An anchor of "More of the solid dissolves" alone would match a key
    that gave the right verdict for the wrong reason, and three of the
    distractors in this module are exactly that.

The prediction function refuses any combination it was not written for, so a
case nobody thought about fails loudly instead of inheriting a default.

NEGATIVE CONTROL: ``python3 verify_h8_11.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h8_11

ACID_COL = "Molar solubility at pH 2.0 (M)"
NEUTRAL_COL = "Molar solubility at pH 7.0 (M)"
PH_COL = "pH of the solution"
SOL_COL = "Measured molar solubility of the hydroxide salt (M)"
ANION_COL = "Anion released when the salt dissolves"

# Explicit lookarounds, never \b: a digit and a letter are both word characters.
_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below|illustrated)(?![a-z])", re.I)

# The exclusion statement attached to EK 8.11.A.1. A stem asking for a
# calculation is the thing barred; the item that NAMES the exclusion is a choice
# and a why, so those are not searched for the verb.
_ASKS_TO_COMPUTE = re.compile(
    r"(?<![A-Za-z])(calculate|compute|computing|computation)(?![A-Za-z])", re.I)
# A computed solubility would reach the student as a molarity. Table cells carry
# MEASURED data, which suggested skill 2.D asks students to read, so only stems
# and choices are searched.
_BARE_MOLARITY = re.compile(r"(?<![A-Za-z0-9.])\d+(?:\.\d+)?\s*M(?![A-Za-z])")

# ---------------------------------------------------------------- the direction

_MORE = [
    re.compile(r"(?<![a-z])more of the solid dissolves(?![a-z])", re.I),
    re.compile(r"(?<![a-z])more of the solid can dissolve(?![a-z])", re.I),
    re.compile(r"(?<![a-z])it rises(?![a-z])", re.I),
    re.compile(r"(?<![a-z])the solubility rises(?![a-z])", re.I),
    re.compile(r"(?<![a-z])shifts toward dissolving(?![a-z])", re.I),
]
_LESS = [
    re.compile(r"(?<![a-z])less of the solid dissolves(?![a-z])", re.I),
    re.compile(r"(?<![a-z])less of the solid can dissolve(?![a-z])", re.I),
    re.compile(r"(?<![a-z])it falls(?![a-z])", re.I),
    re.compile(r"(?<![a-z])the solubility falls(?![a-z])", re.I),
]
_UNCHANGED = [
    re.compile(r"(?<![a-z])no appreciable change(?![a-z])", re.I),
    re.compile(r"(?<![a-z])nothing changes(?![a-z])", re.I),
    re.compile(r"(?<![a-z])no change at all(?![a-z])", re.I),
    re.compile(r"(?<![a-z])is unchanged(?![a-z])", re.I),
]


def direction_of(text):
    """"more", "less", "unchanged", or None where the text says more than one.

    None rather than a guess, for the reason h9_check.favorability_verdict
    gives: a reader that silently picks one of two verdicts is a reader that is
    right half the time and says so with confidence.
    """
    found = set()
    for name, pats in (("more", _MORE), ("less", _LESS), ("unchanged", _UNCHANGED)):
        if any(p.search(text) for p in pats):
            found.add(name)
    return found.pop() if len(found) == 1 else None


def predicted_direction(added, ion_kind):
    """EK 8.11.A.1 with EK 7.9.A.1, written once.

    ``added`` is the species whose concentration the pH change raises;
    ``ion_kind`` is what the salt's own ion is. Every combination this module
    actually uses is listed, and anything else raises rather than defaulting --
    a case nobody thought about must fail loudly.
    """
    if ion_kind == "negligible":
        # EK 8.6.A.1: the conjugate bases of the strong acids are very weak, so
        # none of EK 8.11.A.1's three cases applies and the pH does nothing.
        return "unchanged"
    if added == "acid" and ion_kind in ("weak_base_anion", "hydroxide"):
        # Hydronium removes the anion, so EK 7.9.A.1 drives dissolution.
        return "more"
    if added == "base" and ion_kind == "hydroxide":
        # EK 7.12.A.1: the addition is an ion the salt itself releases.
        return "less"
    if added == "base" and ion_kind == "weak_acid_cation":
        # Hydroxide deprotonates the cation, removing it from solution.
        return "more"
    raise AssertionError(
        f"predicted_direction has no rule for adding {added!r} to a salt whose ion is "
        f"{ion_kind!r}; the module must not ask a case the framework does not settle"
    )


# What the STEM of each direction item supplies. Listed explicitly so the guard
# cannot quietly stop covering an item that was edited. Item 19 and item 21 read
# a table whose pH RISES, which is the same stress as adding base.
DIRECTION_ITEMS = {
    4: ("acid", "weak_base_anion"),
    6: ("acid", "hydroxide"),
    7: ("base", "hydroxide"),
    8: ("acid", "negligible"),
    9: ("base", "weak_acid_cation"),
    19: ("base", "hydroxide"),
    21: ("base", "hydroxide"),
    28: ("acid", "weak_base_anion"),
}


def _words(text):
    return cg.normalize(text).split()


def direction_guard(module, claims, items=None):
    """Predict each direction, then require the key AND the anchor to state it."""
    items = DIRECTION_ITEMS if items is None else items
    for i, (added, ion_kind) in sorted(items.items()):
        item = module.QUESTIONS[i - 1]
        key = h.keyed(item)
        anchor = claims[i - 1][0]
        want = predicted_direction(added, ion_kind)

        got_key = direction_of(key)
        assert got_key is not None, (
            f"{module.TOPIC[0]} q{i}: the keyed choice states no single direction, or "
            f"states more than one: {key!r}"
        )
        assert got_key == want, (
            f"{module.TOPIC[0]} q{i}: adding {added} to a salt whose ion is {ion_kind} makes "
            f"{want} of it dissolve under EK 8.11.A.1, but the key says {got_key} -- {key!r}"
        )

        got_anchor = direction_of(anchor)
        assert got_anchor == want, (
            f"{module.TOPIC[0]} q{i}: the anchor states {got_anchor!r} where the key states "
            f"{want!r}, so it does not pin the direction -- {anchor!r}"
        )

        # The anchor must carry the key's REASON as well as its verdict. Three
        # distractors in this module give the right verdict for a wrong reason,
        # and a verdict-only anchor would match them if the key were moved.
        n_anchor, n_key = len(_words(anchor)), len(_words(key))
        assert n_anchor >= 7 and n_anchor >= 0.6 * n_key, (
            f"{module.TOPIC[0]} q{i}: the anchor is {n_anchor} words against a {n_key}-word "
            f"key, too short to carry the reason as well as the direction -- {anchor!r}"
        )
    print(f"OK  {module.TOPIC[0]} direction guard: {len(items)} directions predicted from "
          "the stress and the ion kind, each matched by its key and pinned by its anchor.")


def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in h._strings(item):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, which this bank "
                f"cannot show -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: no item points at a picture.")


def no_solubility_computation(module):
    """The exclusion statement attached to EK 8.11.A.1, gated rather than trusted."""
    for i, item in enumerate(module.QUESTIONS, 1):
        hit = _ASKS_TO_COMPUTE.search(item["q"])
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: the stem asks the student to {hit.group(0)!r}, and the "
            f"exclusion attached to EK 8.11.A.1 bars computing a solubility from a pH"
        )
        for text in [item["q"]] + list(item["choices"]):
            hit = _BARE_MOLARITY.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: states the molarity {hit.group(0)!r} outside the "
                f"measured data in the table -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} exclusion: no stem asks for a calculation and no choice "
          "states a computed solubility; the topic stays qualitative.")


# ------------------------------------------------------------------ table items

def _sensitive_rows(table):
    """Tabulated salts whose two measured solubilities differ."""
    acid = cg.col(table, ACID_COL)
    neutral = cg.col(table, NEUTRAL_COL)
    labs = cg.labels(table)
    return [lab for lab, a, n in zip(labs, acid, neutral) if a != n]


def q15(table, item):
    sens = _sensitive_rows(table)
    assert sens == ["Salt Q", "Salt S"], f"the tabulated pH-sensitive salts are {sens}"
    h.shows(item, "Salts Q and S")
    return (f"comparing the two tabulated columns row by row, exactly {sens} read "
            f"differently in the acidic and the neutral solution")


def q16(table, item):
    labs = cg.labels(table)
    factors = dict(zip(labs, (a / n for a, n in
                              zip(cg.col(table, ACID_COL), cg.col(table, NEUTRAL_COL)))))
    biggest = max(factors, key=factors.get)
    assert biggest == "Salt Q", f"the largest tabulated factor is at {biggest}: {factors}"
    ties = [lab for lab, f in factors.items() if abs(f - factors[biggest]) < 1e-9]
    assert ties == [biggest], f"the largest tabulated factor is not unique: {ties}"
    h.shows(item, "Salt Q")
    return (f"dividing each tabulated acidic solubility by its neutral one gives {factors}, "
            f"whose unique maximum is at {biggest}")


def q17(table, item):
    factor = cg.cell(table, "Salt S", ACID_COL) / cg.cell(table, "Salt S", NEUTRAL_COL)
    assert abs(factor - 20.0) < 0.5, f"the tabulated factor for salt S is {factor}"
    h.shows(item, "About 20 times")
    return (f"the two tabulated readings for salt S stand in the ratio {factor:g}, read "
            f"straight off the table")


def q18(table, item):
    sens = _sensitive_rows(table)
    assert "Salt R" not in sens, f"salt R is among the tabulated pH-sensitive salts: {sens}"
    assert cg.cell(table, "Salt R", ACID_COL) == cg.cell(table, "Salt R", NEUTRAL_COL), \
        "salt R's two tabulated readings must be equal for the key to hold"
    h.shows(item, "Neither ion is a weak acid, a weak base, or the hydroxide ion")
    return ("salt R's two tabulated readings are identical, so lowering the pH removed "
            "neither of its ions")


def _hydroxide_pairs(table):
    return sorted(zip(cg.col(table, PH_COL), cg.col(table, SOL_COL)))


def q19(table, item):
    pairs = _hydroxide_pairs(table)
    sols = [s for _, s in pairs]
    assert all(b < a for a, b in zip(sols, sols[1:])), (
        f"the tabulated solubilities do not fall as the pH rises: {pairs}"
    )
    h.shows(item, "The solubility falls as the pH rises")
    return (f"sorting the tabulated rows by pH gives solubilities {sols}, each smaller than "
            f"the one before it")


def q20(table, item):
    pairs = _hydroxide_pairs(table)
    best = max(pairs, key=lambda p: p[1])
    assert best[0] == min(p[0] for p in pairs), (
        f"the largest tabulated solubility is not at the lowest tabulated pH: {pairs}"
    )
    h.shows(item, "The least basic of the three solutions")
    return (f"the largest tabulated solubility {best[1]:g} sits beside the lowest tabulated "
            f"pH {best[0]:g}")


def q21(table, item):
    pairs = _hydroxide_pairs(table)
    sols = [s for _, s in pairs]
    assert all(b < a for a, b in zip(sols, sols[1:])), (
        f"the tabulated solubilities do not fall as the pH rises: {pairs}"
    )
    h.shows(item, "so less of the solid can dissolve")
    return (f"the tabulated data fall monotonically with rising pH: {pairs}, which is the "
            f"direction EK 7.12.A.1 gives for an added common ion")


def _anion_kind(table, label):
    """Whether a tabulated anion puts the salt inside EK 8.11.A.1's three cases."""
    text = str(dict(zip(cg.labels(table), table["rows"]))[label][1]).lower()
    weak_base = "conjugate base of a weak acid" in text
    hydroxide = "hydroxide ion" in text
    negligible = "conjugate base of a strong acid" in text
    assert sum([weak_base, hydroxide, negligible]) == 1, (
        f"the tabulated description of {label} settles more than one case, or none: {text!r}"
    )
    return "sensitive" if (weak_base or hydroxide) else "insensitive"


def q22(table, item):
    kinds = {lab: _anion_kind(table, lab) for lab in cg.labels(table)}
    sens = sorted(lab for lab, k in kinds.items() if k == "sensitive")
    assert sens == ["Salt W", "Salt Y"], f"the tabulated pH-sensitive salts are {sens}"
    h.shows(item, "Salts W and Y")
    return (f"reading each tabulated anion against EK 8.11.A.1's three cases classifies the "
            f"salts as {kinds}")


def q23(table, item):
    kinds = {lab: _anion_kind(table, lab) for lab in cg.labels(table)}
    insens = sorted(lab for lab, k in kinds.items() if k == "insensitive")
    assert insens == ["Salt X", "Salt Z"], f"the tabulated insensitive salts are {insens}"
    h.shows(item, "Salts X and Z")
    return (f"the tabulated anions described as very weak conjugate bases of strong acids "
            f"are {insens}, which EK 8.11.A.1's cases do not reach")


def q24(table, item):
    rows = dict(zip(cg.labels(table), table["rows"]))
    # EK 8.11.A.1's FIRST case is a constituent ion that is itself a weak acid;
    # only such an ion is removed by added base. "conjugate base of a weak acid"
    # names a weak BASE, so the search is for the ion described as an acid in
    # its own right, which is what the lookbehind for "of a " excludes.
    acidic_ions = [lab for lab, r in rows.items()
                   if re.search(r"(?<!of a )weak acid(?![a-z])", str(r[1]), re.I)]
    assert not acidic_ions, (
        f"a tabulated anion is described as a weak ACID, which added base would remove: "
        f"{acidic_ions}"
    )
    h.shows(item, "None of them, since none releases an ion that added base could remove")
    return ("no tabulated anion is described as a weak acid, so added hydroxide removes "
            "none of them and EK 8.11.A.1's first case reaches no row")


def _beaker_groups(table):
    """Tabulated beakers grouped by the solid they hold."""
    rows = dict(zip(cg.labels(table), table["rows"]))
    groups = {}
    for lab, r in rows.items():
        contents, observation = str(r[1]).lower(), str(r[2]).lower()
        solid = "calcium fluoride" if "calcium fluoride" in contents else (
            "silver chloride" if "silver chloride" in contents else None)
        assert solid, f"the tabulated contents of {lab} name no solid this check knows"
        groups.setdefault(solid, []).append((lab, contents, observation))
    return groups


def _differing_group(table):
    groups = _beaker_groups(table)
    differing = []
    for solid, entries in groups.items():
        assert len(entries) == 2, f"{solid} appears in {len(entries)} tabulated beakers"
        (la, ca, oa), (lb, cb, ob) = sorted(entries)
        assert ca != cb, f"the two beakers holding {solid} describe the same solution"
        if oa != ob:
            differing.append((solid, la, lb))
    return groups, differing


def q25(table, item):
    _, differing = _differing_group(table)
    assert len(differing) == 1, f"exactly one tabulated pair must differ, found {differing}"
    solid, la, lb = differing[0]
    assert (la, lb) == ("Beaker 1", "Beaker 2"), f"the differing tabulated pair is {la}, {lb}"
    h.shows(item, "Beakers 1 and 2")
    return (f"the two tabulated beakers holding {solid} at different pH record different "
            f"observations, and they are {la} and {lb}")


def q26(table, item):
    _, differing = _differing_group(table)
    assert len(differing) == 1, f"exactly one tabulated pair must differ, found {differing}"
    solid = differing[0][0]
    assert solid == "calcium fluoride", f"the tabulated pair that differs holds {solid}"
    h.shows(item, "Fluoride ion is the conjugate base of a weak acid while chloride ion is "
                  "not")
    return (f"the tabulated observations change with pH for {solid} and not for the other "
            f"solid, which is the contrast EK 8.11.A.1 explains")


TABLE_CHECKS = {15: q15, 16: q16, 17: q17, 18: q18, 19: q19, 20: q20, 21: q21,
                22: q22, 23: q23, 24: q24, 25: q25, 26: q26}

NUMERIC = {}


CLAIMS = [
 ("One of the ions the salt is made of is a weak acid, a weak base, or the hydroxide ion",
  "EK 8.11.A.1, in substance verbatim: the solubility of a salt is pH sensitive when one of the constituent ions is a weak acid, a weak base, or the hydroxide ion."),
 ("Qualitatively, using Le Chatelier's principle",
  "EK 8.11.A.1 says these effects can be understood qualitatively using Le Chatelier's principle, and EK 7.9.A.1 makes that the tool for a system's response to a stress."),
 ("Computation of the solubility of a salt as a function of pH",
  "The exclusion statement attached to EK 8.11.A.1 names exactly this, while learning objective 8.11.A asks for the qualitative effect and skill 2.D for reading measured results."),
 ("More of the solid dissolves, because hydronium ion removes carbonate ion",
  "Carbonic acid is absent from EK 8.2.A.1's list of strong acids, so carbonate is a weak base, one of EK 8.11.A.1's three cases; EK 7.9.A.1 supplies the shift once it is protonated."),
 ("Lowering the concentration of a dissolved product shifts the dissolution equilibrium",
  "EK 7.11.A.1 makes dissolution reversible and EK 7.9.A.1 makes the removal of a species a stress, which together are the qualitative argument EK 8.11.A.1 points at."),
 ("It rises, because hydronium ion consumes the hydroxide ion",
  "EK 8.11.A.1 names the hydroxide ion among the three constituent ions that make a solubility pH sensitive, and neutralizing it is the removal EK 7.9.A.1 responds to."),
 ("It falls, because the added hydroxide ion is an ion the solid itself releases",
  "EK 7.12.A.1's common-ion effect, which for a hydroxide salt is also EK 8.11.A.1's pH effect: the same added ion is both the salt's own and the one setting the pH."),
 ("No appreciable change, because chloride ion is the very weak conjugate base",
  "EK 8.2.A.1 lists HCl among the strong acids and EK 8.6.A.1 gives the strong acids very weak conjugate bases, so none of EK 8.11.A.1's three cases applies."),
 ("More of the solid dissolves, because hydroxide ion removes the cation by deprotonating it",
  "EK 8.11.A.1 says a CONSTITUENT ion that is a weak acid makes the solubility pH sensitive, and a cation counts; EK 7.9.A.1 then shifts the equilibrium once it is removed."),
 ("Calcium fluoride, since fluoride ion is the conjugate base of a weak acid",
  "EK 8.2.A.1's list of strong acids holds HCl, HBr, HI and HNO3 but not HF, so fluoride alone among these anions falls under EK 8.11.A.1's weak-base case."),
 ("Silver bromide, whose two ions are neither weak acids nor weak bases",
  "HBr is one of EK 8.2.A.1's strong acids, so bromide is a very weak conjugate base under EK 8.6.A.1 and EK 8.11.A.1's three cases reach neither of this salt's ions."),
 ("Hydronium ion, which converts fluoride ion into hydrofluoric acid",
  "Hydrofluoric acid is absent from EK 8.2.A.1's list, so fluoride is the conjugate base of a weak acid and reacts with hydronium -- the removal EK 7.9.A.1 responds to."),
 ("Yes, because a carboxylate ion is a weak base",
  "EK 8.6.A.1 names carboxylate ions among the common weak bases, and EK 8.11.A.1 makes a salt pH sensitive when a constituent ion is a weak base."),
 ("The constant is unchanged, while the amount of salt that dissolves may change",
  "EK 7.10.A.2 says a concentration change alters Q and a temperature change alters K, so under EK 7.11.A.1 the pH moves the position of the dissolution equilibrium and not its constant."),
 ("Salts Q and S",
  "EK 8.11.A.1's definition applied to measured results, as suggested skill 2.D asks. q15 compares the two tabulated columns row by row."),
 ("Salt Q",
  "EK 8.11.A.1 supplies the reason a large factor appears at all. q16 divides each tabulated acidic reading by its neutral one and checks the maximum is unique."),
 ("About 20 times",
  "Suggested skill 2.D, reading a ratio off measured results. q17 recomputes it from the two tabulated readings for that salt."),
 ("Neither ion is a weak acid, a weak base, or the hydroxide ion",
  "EK 8.11.A.1 makes a solubility pH sensitive exactly in its three cases, so a salt that does not respond has none of them. q18 checks the two tabulated readings really are equal."),
 ("The solubility falls as the pH rises",
  "EK 8.11.A.1 names hydroxide as a constituent ion and EK 7.12.A.1 gives the direction. q19 sorts the tabulated rows by pH and checks each reading is below the last."),
 ("The least basic of the three solutions",
  "The same statement read for its maximum: the solution with the least hydroxide already in it accepts the most from the solid. q20 locates the largest tabulated reading."),
 ("adds an ion the solid itself releases, so less of the solid can dissolve",
  "EK 7.12.A.1's common-ion argument in Le Chatelier's terms, with EK 7.10.A.2 ruling out any change in the constant. q21 rechecks the tabulated trend."),
 ("Salts W and Y",
  "EK 8.11.A.1's three cases applied to four tabulated anions, the conjugate base of a weak acid being itself a weak base. q22 classifies each tabulated description."),
 ("Salts X and Z",
  "EK 8.6.A.1 attaches very weak conjugate bases to the strong acids, so acid protonates neither. q23 reads the same tabulated descriptions the other way."),
 ("None of them, since none releases an ion that added base could remove",
  "Added hydroxide removes a constituent ion only where that ion is a weak ACID, EK 8.11.A.1's first case, and EK 7.12.A.1 makes added base a common ion for the hydroxide salt instead."),
 ("Beakers 1 and 2",
  "A demonstration needs the same solid at two pH values with different results. q25 groups the tabulated beakers by solid and checks exactly one pair differs."),
 ("Fluoride ion is the conjugate base of a weak acid while chloride ion is not",
  "EK 8.2.A.1 lists HCl and omits HF, so EK 8.11.A.1 reaches one solid and not the other. q26 checks the tabulated pair that differs is the fluoride one."),
 ("It holds only where a constituent ion is a weak base or the hydroxide ion",
  "EK 8.11.A.1 attaches a condition to the effect, and EK 8.6.A.1 makes the conjugate bases of the strong acids too weak to meet it, so the generalisation fails."),
 ("protonates carbonate ion, so the dissolution equilibrium shifts toward dissolving",
  "Carbonic acid is not among EK 8.2.A.1's strong acids, so EK 8.11.A.1's weak-base case applies and EK 7.9.A.1 supplies the shift once carbonate is removed."),
 ("a pH effect and a common-ion effect at once, since hydroxide is both",
  "EK 8.11.A.1 names hydroxide a constituent ion and EK 7.12.A.1 defines the common-ion effect; added hydroxide answers to both, on the same Le Chatelier argument."),
 ("A weakly basic anion with a decrease in pH, and a weakly acidic cation with an increase in pH",
  "EK 8.11.A.1's cases with EK 7.9.A.1's direction: each ion is removed, and so each salt dissolved, by the addition it reacts with, which is the opposite of itself."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the diagram, what makes a solubility pH sensitive?"
        no_figure_language(mod)

    def stem_asks_for_a_calculation(mod, cl):
        mod.QUESTIONS[0]["q"] = ("Calculate the molar solubility of the salt at pH 3.0. "
                                 + mod.QUESTIONS[0]["q"])
        no_solubility_computation(mod)

    def choice_states_a_computed_solubility(mod, cl):
        ch = list(mod.QUESTIONS[1]["choices"])
        ch[4] = "The molar solubility works out as 0.0040 M at that pH"
        mod.QUESTIONS[1]["choices"] = ch
        no_solubility_computation(mod)

    def key_direction_flipped(mod, cl):
        # q6's key reads "It rises, because ..."; turned round it says the
        # opposite of what EK 8.11.A.1 predicts for acid on a hydroxide salt,
        # while leaving every structural property of the item untouched.
        ch = list(mod.QUESTIONS[5]["choices"])
        ch[0] = "It falls, because hydronium ion consumes the hydroxide ion the solid releases"
        ch[1] = "It rises, because hydronium ion consumes the hydroxide ion the solid gains"
        mod.QUESTIONS[5]["choices"] = ch
        cl[5] = ("It falls, because hydronium ion consumes the hydroxide ion", cl[5][1])
        direction_guard(mod, cl)

    def key_states_two_directions(mod, cl):
        ch = list(mod.QUESTIONS[5]["choices"])
        ch[0] = ("It rises, because hydronium ion consumes the hydroxide ion, and then it "
                 "falls again")
        mod.QUESTIONS[5]["choices"] = ch
        cl[5] = ("It rises, because hydronium ion consumes the hydroxide ion", cl[5][1])
        direction_guard(mod, cl)

    def premise_changed_under_a_correct_key(mod, cl):
        # The item is untouched; the guard is told the stem adds ACID to the
        # hydroxide salt of q7, for which EK 8.11.A.1 predicts MORE dissolving
        # while the key says less. The prediction, not the key, is what moved.
        items = dict(DIRECTION_ITEMS)
        items[7] = ("acid", "hydroxide")
        direction_guard(mod, cl, items=items)

    def uncovered_combination(mod, cl):
        items = dict(DIRECTION_ITEMS)
        items[4] = ("acid", "weak_acid_cation")
        direction_guard(mod, cl, items=items)

    def anchor_drops_the_reason(mod, cl):
        cl[3] = ("More of the solid dissolves", cl[3][1])
        direction_guard(mod, cl)

    def anchor_drops_the_direction(mod, cl):
        cl[6] = ("the added hydroxide ion is an ion the solid itself releases", cl[6][1])
        direction_guard(mod, cl)

    def measured_readings_made_equal(mod, cl):
        mod.QUESTIONS[14]["table"] = dict(
            headers=h8_11._T_MEASURED["headers"],
            rows=[["Salt Q", "0.045", "0.045"],
                  ["Salt R", "0.000018", "0.000018"],
                  ["Salt S", "0.012", "0.00060"],
                  ["Salt T", "0.0021", "0.0021"]])

    def largest_factor_moved(mod, cl):
        mod.QUESTIONS[15]["table"] = dict(
            headers=h8_11._T_MEASURED["headers"],
            rows=[["Salt Q", "0.045", "0.0090"],
                  ["Salt R", "0.000018", "0.000018"],
                  ["Salt S", "0.012", "0.00060"],
                  ["Salt T", "0.0021", "0.0021"]])

    def salt_r_made_responsive(mod, cl):
        mod.QUESTIONS[17]["table"] = dict(
            headers=h8_11._T_MEASURED["headers"],
            rows=[["Salt Q", "0.045", "0.00030"],
                  ["Salt R", "0.000018", "0.0000020"],
                  ["Salt S", "0.012", "0.00060"],
                  ["Salt T", "0.0021", "0.0021"]])

    def hydroxide_trend_reversed(mod, cl):
        mod.QUESTIONS[18]["table"] = dict(
            headers=h8_11._T_HYDROXIDE["headers"],
            rows=[["9.0", "0.0000010"], ["10.0", "0.00010"], ["11.0", "0.010"]])

    def hydroxide_maximum_moved(mod, cl):
        mod.QUESTIONS[19]["table"] = dict(
            headers=h8_11._T_HYDROXIDE["headers"],
            rows=[["9.0", "0.00010"], ["10.0", "0.010"], ["11.0", "0.0000010"]])

    def anion_reclassified(mod, cl):
        mod.QUESTIONS[21]["table"] = dict(
            headers=h8_11._T_ANIONS["headers"],
            rows=[["Salt W", "carbonate ion, the conjugate base of a weak acid"],
                  ["Salt X", "acetate ion, the conjugate base of a weak acid"],
                  ["Salt Y", "hydroxide ion"],
                  ["Salt Z", "nitrate ion, the very weak conjugate base of a strong acid"]])

    def anion_description_settles_nothing(mod, cl):
        mod.QUESTIONS[22]["table"] = dict(
            headers=h8_11._T_ANIONS["headers"],
            rows=[["Salt W", "carbonate ion, the conjugate base of a weak acid"],
                  ["Salt X", "an ion the description does not classify"],
                  ["Salt Y", "hydroxide ion"],
                  ["Salt Z", "nitrate ion, the very weak conjugate base of a strong acid"]])

    def both_beaker_pairs_respond(mod, cl):
        mod.QUESTIONS[24]["table"] = dict(
            headers=h8_11._T_BEAKERS["headers"],
            rows=[["Beaker 1", "excess solid calcium fluoride in water at pH 7.0",
                   "a small amount of solid dissolves"],
                  ["Beaker 2", "excess solid calcium fluoride in a solution at pH 2.0",
                   "a much larger amount of solid dissolves"],
                  ["Beaker 3", "excess solid silver chloride in water at pH 7.0",
                   "a very small amount of solid dissolves"],
                  ["Beaker 4", "excess solid silver chloride in a solution at pH 2.0",
                   "a much larger amount of solid dissolves"]])

    def the_wrong_solid_responds(mod, cl):
        mod.QUESTIONS[25]["table"] = dict(
            headers=h8_11._T_BEAKERS["headers"],
            rows=[["Beaker 1", "excess solid calcium fluoride in water at pH 7.0",
                   "a small amount of solid dissolves"],
                  ["Beaker 2", "excess solid calcium fluoride in a solution at pH 2.0",
                   "a small amount of solid dissolves"],
                  ["Beaker 3", "excess solid silver chloride in water at pH 7.0",
                   "a very small amount of solid dissolves"],
                  ["Beaker 4", "excess solid silver chloride in a solution at pH 2.0",
                   "a much larger amount of solid dissolves"]])

    return [
        ("a stem pointing at a diagram the bank cannot show", figure_language),
        ("a stem asking for a solubility the exclusion statement bars",
         stem_asks_for_a_calculation),
        ("a choice stating a computed molar solubility", choice_states_a_computed_solubility),
        ("a keyed direction turned round against EK 8.11.A.1", key_direction_flipped),
        ("a key stating two directions at once", key_states_two_directions),
        ("the stress changed so the prediction no longer matches a correct key",
         premise_changed_under_a_correct_key),
        ("a combination the prediction function was never written for",
         uncovered_combination),
        ("a direction anchor cut down to the verdict alone", anchor_drops_the_reason),
        ("a direction anchor that carries the reason but not the verdict",
         anchor_drops_the_direction),
        ("the tabulated readings for a pH-sensitive salt made equal",
         measured_readings_made_equal),
        ("the largest tabulated factor moved to another salt", largest_factor_moved),
        ("the salt keyed as unresponsive given two different tabulated readings",
         salt_r_made_responsive),
        ("the tabulated hydroxide trend reversed", hydroxide_trend_reversed),
        ("the largest tabulated hydroxide solubility moved off the lowest pH",
         hydroxide_maximum_moved),
        ("a tabulated anion reclassified so the keyed pair is wrong", anion_reclassified),
        ("a tabulated anion description that settles no case",
         anion_description_settles_nothing),
        ("both tabulated beaker pairs made to respond to acid", both_beaker_pairs_respond),
        ("the tabulated response moved to the other solid", the_wrong_solid_responds),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h8_11, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h8_11)
no_solubility_computation(h8_11)
direction_guard(h8_11, CLAIMS)
h.run(h8_11, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
