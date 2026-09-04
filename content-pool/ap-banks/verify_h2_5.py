"""Key audit for AP CHEMISTRY 2.5 Lewis Diagrams.

One ``(anchor, claim)`` per item, in module order; the anchor must appear in the
KEYED choice and in no distractor. Twenty-two of the thirty items are recomputed
here -- eighteen from the formula, charge and bonding written in their own stem,
and four from the species table.

WHAT THE KEYS REST ON
---------------------
EK 2.5.A.1  Lewis diagrams can be constructed according to an established set of
            principles.                                             (item 1)
CED p. 41   Unit 2's Preparing for the AP Exam page: "students must be able to
            construct Lewis structures ... Mistakes include: using the
            incorrect number of valence electrons, violating the octet rule, or
            confusing molecular geometry with bond angles."
                                                       (items 9, 15, 26, 30)
EK 1.5.A.3  Inner electrons are core electrons and outer electrons are valence
            electrons, as described by the ground-state electron configuration.
                                        (every counting item, and items 2, 26)
EK 1.5.A.1  The atom is composed of negatively charged electrons and a
            positively charged nucleus.               (items 6, 7, 8, 14, 29)
EK 2.1.A.2  Valence electrons SHARED between atoms constitute a covalent bond.
                                    (items 4, 11, 12, 17, 20, 23, 26)
EK 2.7.A.2  Both Lewis diagrams and VSEPR theory must be used for predicting
            electronic and structural properties.                   (item 21)

WHY THE ARITHMETIC IS THE GATE HERE. EK 2.5.A.1 is one sentence and it names
none of the principles it refers to. Filling that gap from a textbook is what
SOCIAL_BRIEF.md forbids, so this module keys only what the CED itself supplies:
the count of available valence electrons, which unit 2's own page names as the
first thing students get wrong, and the octet rule, which the same page and EK
2.6.A.2 both name. Everything else in the module is arithmetic over that count,
and ``valence_total`` below recomputes it from the formula and charge in the
item's own stem using nothing but the group of each element.

THE LONE-PAIR ITEMS CHECK THEIR OWN SKELETON. ``lone_pairs`` does not take the
number of bonds on trust: it reads the terminal element out of the stem's own
phrase and asserts that the number of links claimed matches the number of those
atoms in the stem's own formula. A stem that said "each of the two hydrogen
atoms" about NH3 would fail here rather than teach a wrong count.

SCOPE. ``no_resonance_or_formal_charge`` keeps EK 2.6.A.1 and 2.6.A.2's material
in topic 2.6 and ``no_hybridization`` keeps EK 2.7.A.3's in topic 2.7.
``geometry_only_as_the_boundary_item`` allows exactly one item to mention
molecular geometry -- the one whose key is that a Lewis diagram does NOT settle
it, which is EK 2.7.A.2's own claim.

NEGATIVE CONTROL: ``python3 verify_h2_5.py --selftest``.
"""
import re
import sys

import h_chem_notation as hn
import h2_5 as M

FORMULA = "Formula"
CHARGE = "Overall charge"

# Group valence-electron counts for the main-group elements this module uses.
# These are read off the periodic table, which the AP Chemistry exam supplies to
# every student; EK 1.5.A.3 is what makes them the electrons a Lewis diagram
# displays. Nothing here is a remembered STRUCTURE -- only a column number.
VALENCE = {"H": 1, "C": 4, "N": 5, "O": 6, "F": 7, "Si": 4, "P": 5, "S": 6,
           "Cl": 7, "Se": 6, "Br": 7, "I": 7}

ELEMENT_NAME = {"hydrogen": "H", "carbon": "C", "nitrogen": "N", "oxygen": "O",
                "fluorine": "F", "phosphorus": "P", "sulfur": "S",
                "chlorine": "Cl", "bromine": "Br", "iodine": "I"}

NUMWORD = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6}
ORDER = {"single": 1, "double": 2, "triple": 3}
COUNTWORD = {0: "None of them", 1: "Exactly one", 2: "Exactly two",
             3: "Exactly three", 4: "All four"}

_ATOM = re.compile(r"([A-Z][a-z]?)(\d*)")
_FORM_IN_STEM = re.compile(r"formula is ([A-Z][A-Za-z0-9]*)(?![A-Za-z0-9])")
_CHARGE_IN_STEM = re.compile(r"overall charge of (\d)([+-])(?![0-9])")
_NEUTRAL = re.compile(r"(?<![a-z])neutral overall(?![a-z])")
_LINKS = re.compile(r"joined to each of the (one|two|three|four|five|six) "
                    r"([a-z]+) atoms by a (single|double|triple) bond")
_DIATOMIC = re.compile(r"the two ([a-z]+) atoms are joined by a "
                       r"(single|double|triple) bond")
_DRAWN = re.compile(r"shows (\d+) electrons(?![0-9])")

cg = hn.cg


# ----------------------------------------------------------------- helpers

def atoms(formula):
    """{symbol: count} for a plain-text formula such as CCl4."""
    parsed = _ATOM.findall(formula)
    assert parsed, f"cannot read the formula {formula!r}"
    rebuilt = "".join(sym + digits for sym, digits in parsed)
    assert rebuilt == formula, (
        f"the formula {formula!r} did not parse cleanly; it rebuilds as {rebuilt!r}"
    )
    out = {}
    for sym, digits in parsed:
        assert sym in VALENCE, f"no valence-electron count recorded for {sym!r}"
        out[sym] = out.get(sym, 0) + (int(digits) if digits else 1)
    return out


def valence_total(formula, charge):
    """Valence electrons available to the diagram. ``charge`` is signed, 0 if neutral."""
    total = sum(VALENCE[sym] * n for sym, n in atoms(formula).items())
    return total - charge


def read_species(stem):
    """(formula, signed charge) as the stem itself states them."""
    form = _FORM_IN_STEM.search(stem)
    assert form, f"the stem does not state a formula in the expected words: {stem[:80]!r}"
    chg = _CHARGE_IN_STEM.search(stem)
    if chg:
        signed = int(chg.group(1)) * (1 if chg.group(2) == "+" else -1)
    else:
        assert _NEUTRAL.search(stem), (
            f"the stem states neither a charge nor that the species is neutral: {stem[:80]!r}"
        )
        signed = 0
    return form.group(1), signed


def total_from_stem(item):
    formula, charge = read_species(item["q"])
    return formula, charge, valence_total(formula, charge)


def bonding_electrons(item, formula):
    """Electrons taken by the bonds the stem describes, with the skeleton checked.

    The number of links is NOT taken on trust: the terminal element named in the
    stem's own phrase must occur in the stem's own formula exactly as many times as
    the stem claims there are bonds to it.
    """
    counts = atoms(formula)
    hit = _LINKS.search(item["q"])
    if hit:
        links = NUMWORD[hit.group(1)]
        sym = ELEMENT_NAME.get(hit.group(2))
        assert sym, f"unrecognized element name {hit.group(2)!r} in the stem"
        assert counts.get(sym) == links, (
            f"the stem claims {links} bonds to {hit.group(2)} but the formula {formula} "
            f"contains {counts.get(sym)} of them"
        )
        return links * ORDER[hit.group(3)] * 2, f"{links} {hit.group(3)} bond(s)"
    hit = _DIATOMIC.search(item["q"])
    assert hit, f"the stem describes no bonding this check can read: {item['q'][:80]!r}"
    sym = ELEMENT_NAME.get(hit.group(1))
    assert sym, f"unrecognized element name {hit.group(1)!r} in the stem"
    assert counts == {sym: 2}, (
        f"the stem describes a two-atom molecule of {hit.group(1)} but the formula is "
        f"{formula}"
    )
    return ORDER[hit.group(2)] * 2, f"one {hit.group(2)} bond"


def table_species(table):
    """(label, formula, signed charge, total) for each tabulated row."""
    heads = list(table["headers"])
    fi, ci = heads.index(FORMULA), heads.index(CHARGE)
    out = []
    for row in table["rows"]:
        label, formula, charge = str(row[0]), str(row[fi]), str(row[ci]).strip()
        if charge.lower() == "neutral":
            signed = 0
        else:
            m = re.fullmatch(r"(\d)([+-])", charge)
            assert m, f"cannot read the tabulated charge {charge!r}"
            signed = int(m.group(1)) * (1 if m.group(2) == "+" else -1)
        out.append((label, formula, signed, valence_total(formula, signed)))
    return out


# --------------------------------------------------------- stem-numeric checks

def counting(item):
    """The keyed choice states the total this stem's own formula and charge give."""
    formula, charge, total = total_from_stem(item)
    hn.keyed(item, str(total))
    return (f"{formula} with a charge of {charge:+d} brings {total} valence electrons, "
            "summed from the group of each atom present")


def lone_pairs(item):
    """The keyed choice states the pairs left once the stem's own bonds are taken."""
    formula, charge, total = total_from_stem(item)
    used, described = bonding_electrons(item, formula)
    left = total - used
    assert left >= 0, f"{described} would take {used} electrons but only {total} are available"
    assert left % 2 == 0, f"{left} electrons left over does not divide into pairs"
    hn.keyed(item, str(left // 2))
    return (f"{formula} brings {total} electrons and {described} take {used}, leaving "
            f"{left} electrons as {left // 2} lone pair(s)")


def a30(item):
    """The drawn total really does disagree with the available total, and upward."""
    formula, charge, total = total_from_stem(item)
    drawn = _DRAWN.search(item["q"])
    assert drawn, f"the stem does not state how many electrons were drawn: {item['q'][:80]!r}"
    drawn = int(drawn.group(1))
    assert drawn != total, (
        f"the stem's drawn count {drawn} equals the available count {total}, so nothing "
        "has gone wrong and the item has no answer"
    )
    assert drawn > total, (
        f"the stem draws {drawn} against {total} available, which is FEWER, so the keyed "
        "direction is wrong"
    )
    hn.keyed(item, "more valence electrons than the species actually has available")
    return (f"{formula} brings {total} valence electrons and the stem's diagram shows "
            f"{drawn}, which is {drawn - total} too many")


ARITH = {3: counting, 5: counting, 7: counting, 8: counting, 10: counting,
         11: lone_pairs, 12: lone_pairs, 14: counting, 16: counting,
         17: lone_pairs, 19: counting, 20: lone_pairs, 22: counting,
         23: lone_pairs, 25: counting, 27: counting, 29: counting, 30: a30}


# ------------------------------------------------------------ table questions

def q13(t, item):
    rows = table_species(t)
    ordered = sorted(rows, key=lambda r: -r[3])
    assert ordered[0][3] > ordered[1][3], "two tabulated species tie for the largest total"
    hn.keyed(item, ordered[0][0])
    return (f"{ordered[0][0]} totals {ordered[0][3]} valence electrons, the largest of "
            f"{', '.join(str(r[3]) for r in rows)}")


def q18(t, item):
    rows = table_species(t)
    ordered = sorted(rows, key=lambda r: r[3])
    assert ordered[0][3] < ordered[1][3], "two tabulated species tie for the smallest total"
    anion = [r for r in rows if r[2] < 0]
    assert anion, "no tabulated species carries a negative charge, so the rejected "\
                  "option about a charge removing electrons describes nothing"
    hn.keyed(item, ordered[0][0])
    return (f"{ordered[0][0]} totals {ordered[0][3]} valence electrons, the smallest of "
            f"{', '.join(str(r[3]) for r in rows)}")


def q24(t, item):
    rows = table_species(t)
    smallest = min(r[3] for r in rows)
    doubles = [r for r in rows if r[3] == 2 * smallest]
    assert len(doubles) == 1, (
        f"{len(doubles)} tabulated species have exactly twice the smallest total: "
        f"{[r[0] for r in doubles]}; the item needs exactly one"
    )
    hn.keyed(item, doubles[0][0])
    return (f"{doubles[0][0]} totals {doubles[0][3]}, exactly twice the smallest total of "
            f"{smallest}, and no other tabulated species does")


def q28(t, item):
    rows = table_species(t)
    over = [r[0] for r in rows if r[3] > 20]
    hn.keyed(item, COUNTWORD[len(over)])
    return (f"{len(over)} of the {len(rows)} tabulated species exceed twenty valence "
            f"electrons, namely {', '.join(over) or 'none'}")


TABLE_CHECKS = {13: q13, 18: q18, 24: q24, 28: q28}


# ------------------------------------------------------- module-specific gates

_TOPIC_2_6 = re.compile(r"(?<![a-z])(?:resonance|formal charges?)(?![a-z])", re.I)
_TOPIC_2_7 = re.compile(
    r"(?<![a-z])(?:hybridi[sz]ed|hybridi[sz]ation|hybrid orbitals?|"
    r"sigma bonds?|pi bonds?)(?![a-z])", re.I)
_GEOMETRY = re.compile(
    r"(?<![a-z])(?:molecular geometry|bond angles?|VSEPR)(?![a-z])", re.I)
_FIGURE = re.compile(
    r"(?<![a-z])(?:diagram shown|shown above|shown below|the figure|the picture|"
    r"pictured|as drawn above)(?![a-z])", re.I)


def no_resonance_or_formal_charge(module):
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"], item["why"]] + list(item["choices"]):
            hit = _TOPIC_2_6.search(text)
            assert not hit, (
                f"{code} q{i}: mentions {hit.group(0)!r}, which is EK 2.6.A.1 and 2.6.A.2's "
                f"material and belongs to topic 2.6 -- {text[:70]!r}"
            )
    print(f"OK  {code} scope: no item touches resonance or formal charge, which topic 2.6 "
          "owns.")


def no_hybridization(module):
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"], item["why"]] + list(item["choices"]):
            hit = _TOPIC_2_7.search(text)
            assert not hit, (
                f"{code} q{i}: mentions {hit.group(0)!r}, which is EK 2.7.A.3 and 2.7.A.4's "
                f"material and belongs to topic 2.7 -- {text[:70]!r}"
            )
    print(f"OK  {code} scope: no item touches hybridization or sigma and pi bonding, which "
          "topic 2.7 owns.")


def geometry_only_as_the_boundary_item(module):
    """Exactly one item may raise geometry, and only to deny it follows from a Lewis
    diagram alone -- which is EK 2.7.A.2's own statement that BOTH are needed."""
    code = module.TOPIC[0]
    hits = [i for i, item in enumerate(module.QUESTIONS, 1)
            if _GEOMETRY.search(item["q"]) or
            any(_GEOMETRY.search(c) for c in item["choices"])]
    assert len(hits) == 1, (
        f"{code}: {len(hits)} items raise molecular geometry ({hits}); exactly one may, "
        "the boundary item resting on EK 2.7.A.2"
    )
    item = module.QUESTIONS[hits[0] - 1]
    key = item["choices"][item["ans"]]
    assert cg.contains_phrase(key, "does not by itself settle the molecular geometry"), (
        f"{code} q{hits[0]}: raises geometry but its key does not deny that a Lewis diagram "
        f"settles it alone -- {key[:70]!r}"
    )
    print(f"OK  {code} boundary: exactly one item raises molecular geometry, q{hits[0]}, "
          "and its key is EK 2.7.A.2's own point that a Lewis diagram alone does not fix it.")


def no_figure_language(module):
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{code} q{i}: refers to {hit.group(0)!r}, but this bank cannot show a Lewis "
                f"diagram -- {text[:70]!r}"
            )
    print(f"OK  {code} figures: no stem or choice points at a drawn diagram; every item "
          "states its formula, charge and bonding in words.")


CLAIMS = [
 ("established set of principles",
  "EK 2.5.A.1, verbatim: Lewis diagrams can be constructed according to an established set of principles."),
 ("valence electrons, shown either in bonds between atoms or as lone pairs",
  "EK 1.5.A.3 separates core from valence electrons and EK 2.1.A.2 makes a covalent bond valence electrons shared between atoms, so the bonding a Lewis diagram shows is the valence electrons."),
 ("8",
  "EK 1.5.A.3 makes the total the sum of the atoms' valence electrons, four for carbon and one for each hydrogen. Recomputed in the arithmetic check from the stem's own formula."),
 ("Two",
  "EK 2.1.A.2 makes a covalent bond valence electrons SHARED between atoms and EK 2.2.A.2 treats a single bond as bond order one, so one single bond is one shared pair."),
 ("16",
  "EK 1.5.A.3 makes the total the sum over the atoms present, four for carbon and six for each oxygen. Recomputed from the stem's own formula."),
 ("added for each unit of negative charge and one removed for each unit of positive charge",
  "EK 1.5.A.1 makes an atom negatively charged electrons about a positively charged nucleus, so an overall negative charge is a surplus of electrons and a positive one a deficit. The anchor spans both clauses because a rejected option swaps them."),
 ("24",
  "EK 1.5.A.3 gives five for nitrogen and six for each oxygen, and EK 1.5.A.1 makes the single negative charge one extra electron. Recomputed from the stem's own formula and stated charge."),
 ("8",
  "EK 1.5.A.3 gives five for nitrogen and one for each hydrogen, and EK 1.5.A.1 makes the single positive charge one electron fewer. Recomputed from the stem's own formula and stated charge."),
 ("incorrect number of valence electrons",
  "Unit 2's Preparing for the AP Exam page lists the mistakes in these words: using the incorrect number of valence electrons, violating the octet rule, or confusing molecular geometry with bond angles."),
 ("18",
  "EK 1.5.A.3 gives six valence electrons for sulfur and six for each oxygen from their column of the periodic table. Recomputed from the stem's own formula."),
 ("4",
  "EK 2.1.A.2 makes each shared pair two electrons, so the two double bonds the stem states take eight of the available electrons. Recomputed, including a check that the stem's bond count matches its own formula."),
 ("1",
  "EK 2.1.A.2 makes each single bond one shared pair, so the three bonds the stem states take six of the eight available electrons. Recomputed from the stem's own formula and bonding."),
 ("Sulfate ion",
  "EK 1.5.A.3 makes each total the sum of the atoms' valence electrons and EK 1.5.A.1 adjusts for the tabulated charge. Recomputed in q13 for every row, refusing a tie."),
 ("24",
  "EK 1.5.A.3 gives four for carbon and six for each oxygen, and EK 1.5.A.1 makes the charge of two minus two extra electrons. Recomputed from the stem's own formula and stated charge."),
 ("Violating the octet rule",
  "Unit 2's Preparing for the AP Exam page names this mistake in exactly those words, and EK 2.6.A.2 confirms the octet rule as a criterion the course uses."),
 ("12",
  "EK 1.5.A.3 gives four valence electrons for each carbon and one for each hydrogen. Recomputed from the stem's own formula; this is the molecule the CED's own sample question uses."),
 ("0",
  "EK 2.1.A.2 makes each single bond one shared pair, so the four bonds the stem states take all eight available electrons and none remain. Recomputed from the stem's own formula and bonding."),
 ("Methane",
  "EK 1.5.A.3 fixes each total from the tabulated formula. Recomputed in q18, which also asserts some tabulated species really does carry a negative charge, so the rejected option about a charge removing electrons has something to be wrong about."),
 ("32",
  "EK 1.5.A.3 gives four valence electrons for carbon and seven for each chlorine from their columns of the periodic table. Recomputed from the stem's own formula."),
 ("2",
  "EK 2.1.A.2 with EK 2.2.A.2 makes a triple bond three shared pairs, taking six of the ten available electrons. Recomputed from the stem's own formula and bonding."),
 ("does not by itself settle the molecular geometry",
  "EK 2.7.A.2, near verbatim: both Lewis diagrams and VSEPR theory must be used for predicting electronic and structural properties, so neither suffices alone. The framework draws no exception there for ions or for molecules without lone pairs."),
 ("26",
  "EK 1.5.A.3 gives five valence electrons for phosphorus and seven for each chlorine from their columns of the periodic table. Recomputed from the stem's own formula."),
 ("2",
  "EK 2.1.A.2 makes each single bond one shared pair, so the two bonds the stem states take four of the eight available electrons. Recomputed from the stem's own formula and bonding."),
 ("Carbon dioxide",
  "EK 1.5.A.3 and EK 1.5.A.1 fix each tabulated total. Recomputed in q24, which asserts exactly one tabulated species is double the smallest."),
 ("10",
  "EK 1.5.A.3 gives one valence electron for hydrogen, four for carbon and five for nitrogen from their positions in the periodic table. Recomputed from the stem's own formula."),
 ("Every one of them appears in the diagram",
  "Unit 2's own list of mistakes names using the incorrect number of valence electrons, which presupposes that the finished diagram accounts for the counted electrons exactly; EK 2.1.A.2 makes the bonding ones shared pairs and the rest lone pairs."),
 ("8",
  "EK 1.5.A.3 gives five valence electrons for nitrogen and one for each hydrogen. Recomputed from the stem's own formula."),
 ("Exactly two",
  "EK 1.5.A.3 and EK 1.5.A.1 fix each tabulated total. Recomputed in q28 against the threshold the stem itself states, which is the item's test rather than a rule of the framework's."),
 ("32",
  "EK 1.5.A.3 gives six valence electrons for sulfur and six for each oxygen, and EK 1.5.A.1 makes the charge of two minus two extra electrons. Recomputed from the stem's own formula and stated charge."),
 ("more valence electrons than the species actually has available",
  "EK 1.5.A.3 and the periodic table fix what the species brings, and unit 2's own list of mistakes names an incorrect valence electron count first. Recomputed in a30, which asserts the drawn total really does exceed the available one."),
]


# ------------------------------------------------------------ negative controls

def _swap(mod, i, old, new):
    before = mod.QUESTIONS[i - 1]["q"]
    after = before.replace(old, new)
    assert after != before, f"the control's replacement {old!r} did not match q{i}'s stem"
    mod.QUESTIONS[i - 1]["q"] = after


def _wrong_formula(mod, cl):
    """Change the species under a keyed count, leaving the key behind."""
    _swap(mod, 5, "formula is CO2", "formula is CO3")


def _charge_sign_flips(mod, cl):
    """Turn the nitrate ion into a cation, so the keyed count is one electron too many."""
    _swap(mod, 7, "overall charge of 1-", "overall charge of 1+")


def _bond_order_drops(mod, cl):
    """Make the carbon dioxide bonds single, so the keyed lone-pair count is false."""
    _swap(mod, 11, "by a double bond", "by a single bond")


def _link_count_contradicts_the_formula(mod, cl):
    """Claim two bonds to hydrogen in a stem whose own formula says three."""
    _swap(mod, 12, "each of the three hydrogen", "each of the two hydrogen")


def _drawn_count_matches(mod, cl):
    """Make the drawn total equal the available total, so nothing has gone wrong."""
    _swap(mod, 30, "shows 20 electrons", "shows 18 electrons")


def _drawn_count_runs_the_other_way(mod, cl):
    """Make the drawn total too SMALL, so the keyed direction is wrong."""
    _swap(mod, 30, "shows 20 electrons", "shows 16 electrons")


def _retable(mod, i, label, **cells):
    t = mod.QUESTIONS[i - 1]["table"]
    heads = list(t["headers"])
    rows = []
    for row in t["rows"]:
        row = list(row)
        if str(row[0]) == label:
            for header, value in cells.items():
                row[heads.index(header)] = value
        rows.append(row)
    mod.QUESTIONS[i - 1]["table"] = dict(headers=heads, rows=rows)


def _sulfate_shrinks(mod, cl):
    """Shrink the largest species so the tabulated maximum moves off its key.

    Flipping its charge is NOT enough and the first draft of this control did
    exactly that: two units of charge move a total of thirty-two only to
    twenty-eight, which is still the largest in the table, so the control passed
    while proving nothing. The formula has to move.
    """
    _retable(mod, 13, "Sulfate ion", **{FORMULA: "SO2"})


def _methane_gains_a_charge(mod, cl):
    """Give the smallest species a charge, so nothing is twice it any more."""
    _retable(mod, 24, "Methane", **{CHARGE: "2-"})


def _nothing_doubles_the_smallest(mod, cl):
    """Change the tabulated formula so no species is twice the smallest."""
    _retable(mod, 24, "Carbon dioxide", **{FORMULA: "CO3"})


def _resonance_creeps_in(mod, cl):
    mod.QUESTIONS[0]["q"] = "Which structure requires resonance as a refinement?"
    no_resonance_or_formal_charge(mod)


def _hybridization_creeps_in(mod, cl):
    ch = list(mod.QUESTIONS[1]["choices"])
    ch[1] = "The electrons in the hybrid orbitals of the central atom"
    mod.QUESTIONS[1]["choices"] = ch
    no_hybridization(mod)


def _a_second_geometry_item(mod, cl):
    mod.QUESTIONS[2]["q"] = ("A Lewis diagram is drawn for methane, whose formula is CH4 "
                             "and which is neutral overall. What is its bond angle?")
    geometry_only_as_the_boundary_item(mod)


def _geometry_key_flips(mod, cl):
    """Keep one geometry item but key it to the claim EK 2.7.A.2 denies."""
    item = mod.QUESTIONS[20]
    item["ans"] = 1
    geometry_only_as_the_boundary_item(mod)


def _figure_language(mod, cl):
    mod.QUESTIONS[3]["q"] = "In the diagram shown, how many electrons does one bond hold?"
    no_figure_language(mod)


if __name__ == "__main__" and "--selftest" in sys.argv:
    hn.selftest(M, CLAIMS, TABLE_CHECKS, arith=ARITH, extra=[
        ("a keyed count left behind when the stem's formula changed", _wrong_formula),
        ("the sign of a stated ionic charge flipped under its keyed count",
         _charge_sign_flips),
        ("a stated bond order lowered under a keyed lone-pair count", _bond_order_drops),
        ("a stem claiming fewer bonds than its own formula has atoms",
         _link_count_contradicts_the_formula),
        ("the drawn electron count made equal to the available one, so nothing is wrong",
         _drawn_count_matches),
        ("the drawn electron count made too small, reversing the keyed direction",
         _drawn_count_runs_the_other_way),
        ("the largest tabulated species shrunk, moving the maximum off its key",
         _sulfate_shrinks),
        ("a tabulated charge added to the smallest species, so nothing doubles it",
         _methane_gains_a_charge),
        ("a tabulated formula changed so nothing doubles the smallest total",
         _nothing_doubles_the_smallest),
        ("resonance, which is topic 2.6's, moved into a stem", _resonance_creeps_in),
        ("hybrid orbitals, which are topic 2.7's, moved into a choice",
         _hybridization_creeps_in),
        ("a second item raising molecular geometry", _a_second_geometry_item),
        ("the geometry item keyed to the claim EK 2.7.A.2 denies", _geometry_key_flips),
        ("a stem pointing at a drawn diagram the bank cannot show", _figure_language),
    ])

no_resonance_or_formal_charge(M)
no_hybridization(M)
geometry_only_as_the_boundary_item(M)
no_figure_language(M)
hn.audit(M, CLAIMS, TABLE_CHECKS, arith=ARITH)
