"""Key audit for AP CHEMISTRY 2.4 Structure of Metals and Alloys.

One ``(anchor, claim)`` per item, in module order; the anchor must appear in the
KEYED choice and in no distractor. All twelve table items and both stem-numeric
items are recomputed from their own stimulus.

WHAT THE KEYS REST ON
---------------------
EK 2.4.A.1  Metallic bonding can be represented as an array of positive metal
            ions surrounded by delocalized valence electrons (a "sea of
            electrons").                          (items 1, 2, 3, 12, 19, 26)
EK 2.4.A.2  Interstitial alloys form between atoms of significantly different
            radii, where the smaller atoms fill the interstitial spaces between
            the larger atoms (steel: carbon in the interstices of iron).
                       (items 4, 6, 8, 10, 13, 15, 20, 21, 23, 24, 25, 28, 30)
EK 2.4.A.3  Substitutional alloys form between atoms of comparable radius,
            where one atom substitutes for the other in the lattice (brass:
            zinc substituting for copper).
                              (items 5, 7, 9, 11, 14, 16, 17, 18, 22, 27, 29)
EK 2.1.A.5  In a metallic solid the valence electrons are delocalized and not
            associated with any individual atom.       (items 2, 3, 12, 19)

HOW THE CLASSIFICATIONS ARE CHECKED. "Comparable" and "significantly different"
are comparisons, so every classification here is recomputed from the RATIO of
the two radii the item itself tabulates -- never from a remembered radius. Two
items name the framework's own examples, and ``q13``/``q14`` additionally assert
that the tabulated rows really do pair iron with carbon and copper with zinc,
so an edited radius could not quietly turn the CED's steel into a
substitutional alloy.

THE FRAMEWORK STATES NO NUMERICAL CUTOFF for "comparable", and
``no_numerical_threshold_in_a_key`` asserts that no KEYED choice invents one.
Two items put a fabricated cutoff in their rejected options, which is the point:
a student who thinks the framework supplies a number should be able to be shown
that it does not. The ten percent used in the two counting items is stated in
their own stems as the item's test, not offered as the framework's rule.

SCOPE. ``no_macroscopic_property`` keeps EK 3.2.A.6's conduction, malleability
and ductility inside topic 3.2, which owns them.

NEGATIVE CONTROL: ``python3 verify_h2_4.py --selftest``.
"""
import re
import sys

import h_chem_notation as hn
import h2_4 as M

HOSTR = "Radius of the host atom (picometers)"
ADDR = "Radius of the added atom (picometers)"
RAD = "Atomic radius (picometers)"
MAJ = "Majority element and its atomic radius (picometers)"
ADD = "Added element and its atomic radius (picometers)"

COUNTWORD = {0: "None of them", 1: "Exactly one", 2: "Exactly two",
             3: "Exactly three", 4: "All four"}

cg = hn.cg


# ----------------------------------------------------------------- helpers

def pair_rows(table):
    """(label, host radius, added radius, added/host) for the candidate-alloy table."""
    return [(lab, h, a, a / h) for lab, h, a in
            zip(cg.labels(table), cg.col(table, HOSTR), cg.col(table, ADDR))]


def element_rows(table):
    """(host label, host radius, [(candidate label, radius), ...])."""
    labs = cg.labels(table)
    radii = cg.col(table, RAD)
    return labs[0], radii[0], list(zip(labs[1:], radii[1:]))


def named_rows(table):
    """(alloy, majority name, majority radius, added name, added radius, ratio)."""
    out = []
    for lab, maj, add in zip(cg.labels(table),
                             [str(r[1]) for r in table["rows"]],
                             [str(r[2]) for r in table["rows"]]):
        mr = cg.num(maj)
        ar = cg.num(add)
        out.append((lab, maj.split(",")[0].strip(), mr,
                    add.split(",")[0].strip(), ar, ar / mr))
    return out


def unique_min(values, key):
    """The single argmin, refused if two entries tie for it."""
    scored = sorted(values, key=key)
    assert key(scored[0]) < key(scored[1]), (
        f"two entries tie for the extreme value: {scored[0]} and {scored[1]}"
    )
    return scored[0]


# ------------------------------------------------------------ table questions

def q6(t, item):
    rows = pair_rows(t)
    smallest = unique_min(rows, key=lambda r: r[3])
    bigger = [r[0] for r in rows if r[3] > 1]
    assert bigger, "no tabulated pair has an added atom larger than its host, so the "\
                   "rejected option about a larger added atom describes nothing"
    hn.keyed(item, smallest[0])
    return (f"{smallest[0]} has the smallest ratio of added to host radius at "
            f"{smallest[3]:.2f}, the most significantly different pair of radii tabulated")


def q7(t, item):
    rows = pair_rows(t)
    closest = unique_min(rows, key=lambda r: abs(r[3] - 1))
    hn.keyed(item, closest[0])
    return (f"{closest[0]}'s two radii are the most nearly equal, a ratio of "
            f"{closest[3]:.3f}, which is what comparable radius means")


def q10(t, item):
    host, hr, cands = element_rows(t)
    smallest = unique_min(cands, key=lambda c: c[1] / hr)
    assert smallest[1] / hr < 0.6, (
        f"the smallest candidate is {smallest[1] / hr:.2f} of the host radius, which is "
        "not significantly different enough to key an interstitial answer"
    )
    hn.keyed(item, smallest[0])
    return (f"{smallest[0]} is {smallest[1]:g} picometers against the host's {hr:g}, a "
            f"ratio of {smallest[1] / hr:.2f}, far the most different of the candidates")


def q11(t, item):
    host, hr, cands = element_rows(t)
    closest = unique_min(cands, key=lambda c: abs(c[1] - hr))
    hn.keyed(item, closest[0])
    return (f"{closest[0]} at {closest[1]:g} picometers is nearest the host's {hr:g}, "
            f"differing by {abs(closest[1] - hr):g}, which is comparable radius")


def q13(t, item):
    rows = named_rows(t)
    far = [r for r in rows if r[5] < 0.8]
    assert len(far) == 1, f"{len(far)} tabulated alloys pair significantly different radii"
    alloy = far[0]
    assert alloy[1] == "iron" and alloy[3] == "carbon", (
        f"the interstitial row pairs {alloy[1]} with {alloy[3]}, not the iron and carbon "
        "EK 2.4.A.2 names as its own example"
    )
    hn.keyed(item, alloy[0])
    return (f"{alloy[0]} pairs {alloy[3]} at {alloy[4]:g} picometers with {alloy[1]} at "
            f"{alloy[2]:g}, a ratio of {alloy[5]:.2f}, and is the framework's own steel")


def q14(t, item):
    rows = named_rows(t)
    near = [r for r in rows if abs(r[5] - 1) <= 0.10]
    assert len(near) == 1, f"{len(near)} tabulated alloys pair comparable radii"
    alloy = near[0]
    assert alloy[1] == "copper" and alloy[3] == "zinc", (
        f"the substitutional row pairs {alloy[1]} with {alloy[3]}, not the copper and zinc "
        "EK 2.4.A.3 names as its own example"
    )
    hn.keyed(item, alloy[0])
    return (f"{alloy[0]} pairs {alloy[3]} at {alloy[4]:g} picometers with {alloy[1]} at "
            f"{alloy[2]:g}, a ratio of {alloy[5]:.3f}, and is the framework's own brass")


def q17(t, item):
    rows = pair_rows(t)
    close = [r[0] for r in rows if abs(r[3] - 1) <= 0.10]
    hn.keyed(item, COUNTWORD[len(close)])
    return (f"{len(close)} of the {len(rows)} tabulated pairs sit within ten percent, "
            f"namely {', '.join(close) or 'none'}")


def q18(t, item):
    host, hr, cands = element_rows(t)
    close = [c[0] for c in cands if abs(c[1] - hr) / hr <= 0.10]
    hn.keyed(item, COUNTWORD[len(close)])
    return (f"{len(close)} of the {len(cands)} candidates lie within ten percent of the "
            f"host's {hr:g} picometers, namely {', '.join(close) or 'none'}")


def q20(t, item):
    host, hr, cands = element_rows(t)
    furthest = unique_min(cands, key=lambda c: -abs(c[1] - hr))
    hn.keyed(item, furthest[0])
    return (f"{furthest[0]} differs from the host by {abs(furthest[1] - hr):g} picometers, "
            "the largest gap among the candidates")


def q23(t, item):
    rows = pair_rows(t)
    closest = unique_min(rows, key=lambda r: abs(r[1] - r[2]))
    hn.keyed(item, closest[0])
    return (f"{closest[0]}'s radii differ by {abs(closest[1] - closest[2]):g} picometers, "
            "the smallest difference in the table")


def q25(t, item):
    rows = named_rows(t)
    largest = unique_min(rows, key=lambda r: -r[5])
    assert largest[5] > 1, (
        f"the largest ratio is {largest[5]:.3f}, so no tabulated alloy has an added atom "
        "larger than its majority atom and the item's premise fails"
    )
    hn.keyed(item, largest[0])
    return (f"{largest[0]} has the larger ratio of added to majority radius at "
            f"{largest[5]:.3f}, its added atom being the larger of the two")


def q27(t, item):
    host, hr, cands = element_rows(t)
    pairs = [(a, b, abs(a[1] - b[1])) for i, a in enumerate(cands) for b in cands[i + 1:]]
    best = unique_min(pairs, key=lambda p: p[2])
    hn.keyed(item, f"{best[0][0]} and {best[1][0]}")
    return (f"{best[0][0]} and {best[1][0]} differ by {best[2]:g} picometers, the closest "
            f"of the {len(pairs)} candidate pairs, with the host set aside")


TABLE_CHECKS = {6: q6, 7: q7, 10: q10, 11: q11, 13: q13, 14: q14, 17: q17,
                18: q18, 20: q20, 23: q23, 25: q25, 27: q27}


# ------------------------------------------------------- stem-numeric questions

_PM = re.compile(r"(?<![0-9])(\d+)\s+picometers(?![a-z])")


def _stem_ratio(item):
    """The ratio of the two radii the stem states, smaller over larger.

    Order-independent on purpose: one stem names the host first and the other names
    the added element first, and a check that assumed an order would silently invert
    one of them.
    """
    radii = [int(x) for x in _PM.findall(item["q"])]
    assert len(radii) == 2, f"the stem states {len(radii)} radii, expected two: {radii}"
    return min(radii) / max(radii), radii


def a29(item):
    ratio, radii = _stem_ratio(item)
    assert ratio >= 0.90, (
        f"the stem's radii {radii} give a ratio of {ratio:.3f}, which is not comparable "
        "enough to key a substitutional answer"
    )
    hn.keyed(item, "substitutional alloy, with the added atoms taking lattice positions")
    return (f"the stem's own radii {radii[0]} and {radii[1]} differ by "
            f"{(1 - ratio) * 100:.1f} percent, which is EK 2.4.A.3's comparable radius")


def a30(item):
    ratio, radii = _stem_ratio(item)
    assert ratio <= 0.60, (
        f"the stem's radii {radii} give a ratio of {ratio:.3f}, which is not significantly "
        "different enough to key an interstitial answer"
    )
    hn.keyed(item, "interstitial alloy, with the added atoms filling the spaces")
    return (f"the stem's own radii {radii[0]} and {radii[1]} give a ratio of {ratio:.2f}, "
            "which is EK 2.4.A.2's significantly different radii")


ARITH = {29: a29, 30: a30}


# ------------------------------------------------------- module-specific gates

# EK 3.2.A.6's macroscopic properties of metallic solids belong to topic 3.2.
_MACRO = re.compile(
    r"(?<![a-z])(?:malleable|malleability|ductile|ductility|conducts? (?:electricity|heat)|"
    r"electrical conductivity|melting point|boiling point)(?![a-z])", re.I)

# The framework sets no numerical cutoff for "comparable" or "significantly
# different". A rejected option may invent one; a key may not.
_THRESHOLD = re.compile(
    r"(?<![a-z])(?:factor of (?:two|three|four|five|ten|\d+)|"
    r"within (?:one|two|three|\d+) picometers?|exactly equal|equal to within)(?![a-z])",
    re.I)

_FIGURE = re.compile(
    r"(?<![a-z])(?:diagram|figure|image|picture|sketch|shown above|shown below|"
    r"pictured|the drawing below)(?![a-z])", re.I)


def no_macroscopic_property(module):
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _MACRO.search(text)
            assert not hit, (
                f"{code} q{i}: rests on {hit.group(0)!r}, which is EK 3.2.A.6 and belongs "
                f"to topic 3.2 -- {text[:70]!r}"
            )
    print(f"OK  {code} scope: no item rests on conduction, malleability or ductility, "
          "which are EK 3.2.A.6's material.")


def no_numerical_threshold_in_a_key(module):
    code = module.TOPIC[0]
    in_distractors = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]]
        hit = _THRESHOLD.search(key)
        assert not hit, (
            f"{code} q{i}: the keyed choice states {hit.group(0)!r} as a cutoff, but the "
            f"framework gives no numerical threshold for comparable radius -- {key[:70]!r}"
        )
        for j, ch in enumerate(item["choices"]):
            if j != item["ans"] and _THRESHOLD.search(ch):
                in_distractors += 1
    assert in_distractors >= 2, (
        "no rejected option invents a cutoff, so nothing in the module teaches that the "
        "framework does not supply one"
    )
    print(f"OK  {code} hedge: no keyed choice invents a numerical cutoff for comparable "
          f"radius; {in_distractors} rejected option(s) do, which is what makes the point.")


def no_figure_language(module):
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{code} q{i}: refers to {hit.group(0)!r}, which the bank cannot show -- "
                f"{text[:70]!r}"
            )
    print(f"OK  {code} figures: no stem or choice points at a picture; every model is "
          "described in words or by tabulated radii.")


CLAIMS = [
 ("array of positive metal ions surrounded by delocalized valence electrons",
  "EK 2.4.A.1, verbatim: metallic bonding can be represented as an array of positive metal ions surrounded by delocalized valence electrons, a sea of electrons."),
 ("valence electrons, which are delocalized rather than associated with any individual atom",
  "EK 2.4.A.1 names them delocalized VALENCE electrons and EK 2.1.A.5 adds that they are not associated with any individual atom; core electrons are not what either statement describes."),
 ("delocalized through the solid rather than held by any one core",
  "EK 2.4.A.1 draws the cores as positive ions surrounded by delocalized valence electrons, and EK 2.1.A.5 says those electrons belong to no individual atom, which is what leaves each core positive."),
 ("significantly different radii, with the smaller atoms filling the spaces",
  "EK 2.4.A.2, verbatim: interstitial alloys form between atoms of significantly different radii, where the smaller atoms fill the interstitial spaces between the larger atoms. The anchor spans both clauses because a rejected option keeps the condition and swaps the placement."),
 ("comparable radius, with one atom substituting for the other",
  "EK 2.4.A.3, verbatim: substitutional alloys form between atoms of comparable radius, where one atom substitutes for the other in the lattice. The anchor spans both clauses because a rejected option keeps one and swaps the other."),
 ("Pair 4",
  "EK 2.4.A.2 conditions an interstitial alloy on significantly different radii. Recomputed in q6 as the smallest ratio of added to host radius, with a check that some tabulated pair really does have the larger added atom the rejected option describes."),
 ("Pair 3",
  "EK 2.4.A.3 conditions a substitutional alloy on comparable radius. Recomputed in q7 as the ratio nearest one, refusing a tie."),
 ("Carbon occupies the interstices in iron",
  "EK 2.4.A.2 gives this as its own example, in these words: steel, in which carbon occupies the interstices in iron."),
 ("Zinc substitutes for copper in the lattice",
  "EK 2.4.A.3 gives this as its own example: in certain brass alloys, other elements, usually zinc, substitute for copper."),
 ("Element B",
  "EK 2.4.A.2 requires significantly different radii for an atom to fill the spaces between larger atoms. Recomputed in q10, which also asserts the winning candidate is under sixty percent of the host radius rather than merely the smallest."),
 ("Element C",
  "EK 2.4.A.3 conditions substitution on comparable radius. Recomputed in q11 as the candidate radius nearest the host's, refusing a tie."),
 ("positive ions and valence electrons delocalized over the whole array",
  "EK 2.4.A.1 gives the model as positive metal ions with delocalized valence electrons and EK 2.1.A.5 says those electrons are not associated with any individual atom, so a model of neutral atoms keeping their own electrons abandons both halves."),
 ("Alloy 1",
  "EK 2.4.A.2 conditions the interstitial case on significantly different radii. Recomputed in q13, which also asserts the tabulated row really pairs iron with carbon, the framework's own steel."),
 ("Alloy 2",
  "EK 2.4.A.3 conditions the substitutional case on comparable radius. Recomputed in q14, which also asserts the tabulated row really pairs copper with zinc, the framework's own brass."),
 ("Radii that are significantly different",
  "EK 2.4.A.2 states the condition in exactly those words. The framework sets no numerical threshold anywhere, which is why the options stating one are rejected."),
 ("Radii that are comparable",
  "EK 2.4.A.3 states the condition in exactly those words. A stated factor or a stated tolerance in picometers is more than the framework claims."),
 ("Exactly two",
  "EK 2.4.A.3 makes comparable radius the substitutional condition. Recomputed in q17 from the tabulated radii against the ten percent test the stem itself states."),
 ("Exactly three",
  "EK 2.4.A.3 makes comparable radius the substitutional condition. Recomputed in q18 from each candidate radius against the host's, on the ten percent test the stem itself states."),
 ("Each valence electron stays paired with one particular metal ion",
  "EK 2.4.A.1 supports every rejected statement here, and EK 2.1.A.5 rules this one out directly by saying the valence electrons are not associated with any individual atom."),
 ("Element B",
  "Recomputed in q20 as the candidate radius furthest from the host's. EK 2.4.A.2 is what makes that comparison the interesting one, since significantly different radii are the interstitial condition."),
 ("interstitial spaces between the larger atoms",
  "EK 2.4.A.2 places them there in its own words: the smaller atoms fill the interstitial spaces between the larger atoms."),
 ("takes the place of the other at those positions",
  "EK 2.4.A.3 states it directly: one atom substitutes for the other in the lattice, which is a lattice position taken rather than a space between positions filled."),
 ("Pair 3",
  "Recomputed in q23 as the smallest difference between the two tabulated radii. EK 2.4.A.3's comparable radius is what makes the smallest difference worth finding."),
 ("reserves for atoms of comparable radius",
  "EK 2.4.A.3 conditions substitution on comparable radius and EK 2.4.A.2 assigns significantly different radii to the interstitial case, so an atom half the host's size goes into the spaces rather than into a lattice position."),
 ("Alloy 2",
  "Recomputed in q25 as the larger ratio of added to majority radius, with a check that the winning ratio really does exceed one. EK 2.4.A.2 and EK 2.4.A.3 are what make that ratio decisive."),
 ("metallic model has positive ions in a sea of delocalized valence electrons",
  "EK 2.4.A.1 gives the metallic model and EK 2.3.A.1 gives the ionic one as cations and anions in a periodic array; the delocalized electrons are what the ionic model has no counterpart for."),
 ("Element A and Element D",
  "Recomputed in q27 as the closest pair among the candidates with the host set aside. EK 2.4.A.3 is what makes closeness in radius the property worth measuring."),
 ("must contain equal numbers of the two kinds of atom",
  "EK 2.4.A.2 and EK 2.4.A.3 support every rejected statement here and say nothing about the numbers of the two kinds of atom; the framework's own brass example describes zinc as a substituent rather than as half the solid."),
 ("substitutional alloy, with the added atoms taking lattice positions",
  "EK 2.4.A.3 conditions a substitutional alloy on comparable radius and puts the substituting atom in the lattice. Recomputed in a29 from the two radii the stem states."),
 ("interstitial alloy, with the added atoms filling the spaces",
  "EK 2.4.A.2 conditions an interstitial alloy on significantly different radii and puts the smaller atoms in the spaces between the larger ones. Recomputed in a30 from the two radii the stem states."),
]


# ------------------------------------------------------------ negative controls

def _retable(mod, i, label, **cells):
    """Replace named cells of one row of question ``i``'s table, by column header."""
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


def _tie_for_smallest_ratio(mod, cl):
    """Give a second pair the same ratio, so no single pair is the likeliest."""
    _retable(mod, 6, "Pair 1", **{HOSTR: "140", ADDR: "70"})


def _move_the_closest_ratio(mod, cl):
    """Make a different pair the most nearly equal one."""
    _retable(mod, 7, "Pair 2", **{ADDR: "128"})


def _no_small_candidate(mod, cl):
    """Grow the interstitial candidate until nothing is significantly different."""
    _retable(mod, 10, "Element B", **{RAD: "138"})


def _steel_stops_being_interstitial(mod, cl):
    """Grow the carbon radius until the framework's own steel is not the far pair."""
    _retable(mod, 13, "Alloy 1", **{ADD: "carbon, 130"})


def _brass_stops_naming_zinc(mod, cl):
    """Rename the substituting element, so the row no longer is the CED's brass."""
    _retable(mod, 14, "Alloy 2", **{ADD: "carbon, 134"})


def _third_pair_becomes_close(mod, cl):
    """Change the count the within-ten-percent item reports."""
    _retable(mod, 17, "Pair 1", **{ADDR: "120"})


def _candidate_moves_out_of_range(mod, cl):
    """Change the count the candidate-within-ten-percent item reports."""
    _retable(mod, 18, "Element D", **{RAD: "200"})


def _closest_candidate_pair_moves(mod, cl):
    """Make a different pair of candidates the closest to each other."""
    _retable(mod, 27, "Element C", **{RAD: "134"})


def _substitution_stem_radii_diverge(mod, cl):
    before = mod.QUESTIONS[28]["q"]
    after = before.replace("141 picometers", "70 picometers")
    assert after != before, "the control's replacement did not match the stem"
    mod.QUESTIONS[28]["q"] = after


def _interstitial_stem_radii_converge(mod, cl):
    before = mod.QUESTIONS[29]["q"]
    after = before.replace("62 picometers", "138 picometers")
    assert after != before, "the control's replacement did not match the stem"
    mod.QUESTIONS[29]["q"] = after


def _threshold_in_a_key(mod, cl):
    ch = list(mod.QUESTIONS[15]["choices"])
    ch[0] = "Radii equal to within one picometer"
    mod.QUESTIONS[15]["choices"] = ch
    cl[15] = ("Radii equal to within one picometer", cl[15][1])
    no_numerical_threshold_in_a_key(mod)


def _macroscopic_property_creeps_in(mod, cl):
    mod.QUESTIONS[0]["q"] = "Why does a metallic solid conduct electricity so well?"
    no_macroscopic_property(mod)


def _figure_language(mod, cl):
    mod.QUESTIONS[1]["q"] = "In the diagram of the metallic lattice, which electrons move?"
    no_figure_language(mod)


if __name__ == "__main__" and "--selftest" in sys.argv:
    hn.selftest(M, CLAIMS, TABLE_CHECKS, arith=ARITH, extra=[
        ("two pairs tied for the smallest radius ratio", _tie_for_smallest_ratio),
        ("the most nearly equal pair moved off its key", _move_the_closest_ratio),
        ("the small interstitial candidate grown until nothing is significantly different",
         _no_small_candidate),
        ("the framework's own steel edited until it is no longer the far pair",
         _steel_stops_being_interstitial),
        ("the framework's own brass edited so it no longer names zinc",
         _brass_stops_naming_zinc),
        ("a third pair brought inside ten percent, changing the tabulated count",
         _third_pair_becomes_close),
        ("a candidate pushed outside ten percent, changing the tabulated count",
         _candidate_moves_out_of_range),
        ("a different pair of candidates made the closest to each other",
         _closest_candidate_pair_moves),
        ("the substitution stem's radii pushed apart until the key is false",
         _substitution_stem_radii_diverge),
        ("the interstitial stem's radii brought together until the key is false",
         _interstitial_stem_radii_converge),
        ("a fabricated numerical cutoff moved into a keyed choice", _threshold_in_a_key),
        ("a macroscopic property of metals, which is topic 3.2's",
         _macroscopic_property_creeps_in),
        ("a stem pointing at a diagram the bank cannot show", _figure_language),
    ])

no_macroscopic_property(M)
no_numerical_threshold_in_a_key(M)
no_figure_language(M)
hn.audit(M, CLAIMS, TABLE_CHECKS, arith=ARITH)
