"""Key audit for AP CHEMISTRY 3.11 Spectroscopy and the Electromagnetic Spectrum.

One (anchor, claim) per item, in module order.

THE TOPIC IS THREE PAIRINGS AND A LEAD SENTENCE, which is exactly why the
pairings get swapped. ``PAIRING`` below transcribes EK 3.11.A.1's three
sub-points once:

  microwave            -> molecular rotational levels
  infrared             -> molecular vibrational levels
  ultraviolet/visible  -> electronic energy levels

``pairings_never_swapped`` then reads EVERY key that names a region together
with a transition and checks it against that transcription. The region and the
transition are read into named variables out of the key's own text and compared;
nothing is indexed into parallel lists, which is the mistake that made an
earlier verifier in this bank reject a correct key. One item asks which claim
CONTRADICTS the framework, and its key is necessarily a wrong pairing, so the
check permits a mismatch only where the stem disowns it -- and asserts such an
item exists, so the exemption cannot quietly become the rule.

BOTH DIRECTIONS COME FROM ONE DICTIONARY. Items ask region-to-transition and
transition-to-region, and the checks consult the same mapping either way, so the
two directions cannot drift apart.

SCOPE. 3.12 owns the photon equations and 3.13 owns Beer-Lambert, so
``no_other_topic`` asserts no item computes a photon energy, a frequency or a
wavelength. ``no_energy_ordering`` asserts further that no key ranks the three
regions by energy or wavelength: EK 3.11.A.1 states the associations and does
NOT order the regions, and an ordering claim here would be true and unsourced.

ARITHMETIC. There is none. The six tabulated items are recomputed by looking
each tabulated region up in the transcription, which is this topic's analogue.

NEGATIVE CONTROL: ``python3 verify_h3_11.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h3_11

REGIONCOL = "Region of the spectrum"
CLAIMEDCOL = "Transition claimed for it"
OBSERVED = "Region in which absorption was observed"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below|the spectrum above|the spectrum below)(?![a-z])",
    re.I)

# 3.12 owns the photon equations; 3.13 owns Beer-Lambert.
_OTHER_TOPIC = re.compile(
    r"(?<![A-Za-z])(Planck|Beer-Lambert|molar absorptivity|path length|"
    r"nanometres|nanometers|nanometre|nanometer|hertz|joules per photon)(?![A-Za-z])",
    re.I)

# EK 3.11.A.1 states three associations and orders nothing. A claim about which
# region carries the more energetic photon would be true and unsourced here.
_ORDERING = re.compile(
    r"(?<![a-z])(higher energy than|lower energy than|more energetic than|"
    r"less energetic than|shorter wavelength than|longer wavelength than|"
    r"highest energy|lowest energy)(?![a-z])", re.I)

# ------------------------------------------------------------ the transcription

PAIRING = {
    "microwave": "rotational",
    "infrared": "vibrational",
    "ultraviolet/visible": "electronic",
}

_REGION_WORDS = [
    ("ultraviolet/visible", re.compile(
        r"(?<![a-z])(?:ultraviolet\s*/\s*visible|ultraviolet and visible|"
        r"ultraviolet|visible)(?![a-z])", re.I)),
    ("microwave", re.compile(r"(?<![a-z])microwave(?![a-z])", re.I)),
    ("infrared", re.compile(r"(?<![a-z])infrared(?![a-z])", re.I)),
]
_TRANSITION_WORDS = [
    ("rotational", re.compile(r"(?<![a-z])rotational(?![a-z])", re.I)),
    ("vibrational", re.compile(r"(?<![a-z])vibrational(?![a-z])", re.I)),
    ("electronic", re.compile(r"(?<![a-z])electronic(?![a-z])", re.I)),
]

_DISOWNED = re.compile(
    r"(?<![a-z])(contradicts|inconsistent with|does not make|the framework does not|"
    r"NOT associate|not associate)(?![a-z])", re.I)


def _named(text, table):
    """Every distinct name from ``table`` that appears in ``text``."""
    return sorted({name for name, pat in table if pat.search(text)})


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
    print(f"OK  {module.TOPIC[0]} figures: every spectrum is carried as a table naming the "
          "region in which absorption was observed.")


def no_other_topic(module):
    """Stems, choices and tables only.

    A RATIONALE is allowed to name a neighbouring topic, and should: several
    here say that concentration belongs to 3.13's Beer-Lambert law rather than
    to this statement, which is the distinction the item is teaching. What must
    not happen is a STUDENT-FACING QUESTION asking for one of those quantities,
    and that is what this checks.
    """
    for i, item in enumerate(module.QUESTIONS, 1):
        texts = [item["q"]] + list(item["choices"])
        t = item.get("table")
        if t:
            texts += [str(x) for x in t["headers"]]
            texts += [str(c) for r in t["rows"] for c in r]
        for text in texts:
            hit = _OTHER_TOPIC.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: uses {hit.group(0)!r}, which is 3.12's or 3.13's "
                f"material -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no photon arithmetic and no Beer-Lambert; the topic "
          "stays on the associations themselves.")


def no_energy_ordering(module):
    """EK 3.11.A.1 states three associations and does not rank the regions."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"], item["why"]] + list(item["choices"]):
            hit = _ORDERING.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: ranks the spectral regions ({hit.group(0)!r}), "
                "which EK 3.11.A.1 does not do; the ordering is true and unsourced here"
            )
    print(f"OK  {module.TOPIC[0]} sourcing: no item ranks the three regions by energy or "
          "wavelength, which the framework's statement does not do.")


def pairings_never_swapped(module):
    """Every key naming a region and a transition must pair them the framework's way."""
    checked, disowned = [], []
    for i, item in enumerate(module.QUESTIONS, 1):
        key, stem = h.keyed(item), item["q"]
        # A pairing is normally split between the two: the stem names the region
        # and the key names the transition, or the reverse. So each half is read
        # from the KEY where the key states it and from the stem otherwise --
        # precedence to the key, since the key is what is being asserted.
        regions = _named(key, _REGION_WORDS) or _named(stem, _REGION_WORDS)
        transitions = _named(key, _TRANSITION_WORDS) or _named(stem, _TRANSITION_WORDS)
        if len(regions) != 1 or len(transitions) != 1:
            # Zero or several of either: no single pairing is being asserted,
            # so there is nothing here for this check to read.
            continue

        region, transition = regions[0], transitions[0]
        expected = PAIRING[region]
        pairing_is_the_frameworks = transition == expected

        if pairing_is_the_frameworks:
            checked.append(i)
            continue

        # A mismatched pairing may be keyed only where the stem asks which claim
        # the framework does NOT make.
        assert _DISOWNED.search(item["q"]), (
            f"{module.TOPIC[0]} q{i}: the key pairs {region!r} with {transition!r}, but "
            f"EK 3.11.A.1 pairs it with {expected!r}, and the stem does not frame the claim "
            f"as one the framework rejects -- stem {item['q'][:80]!r}"
        )
        disowned.append(i)

    assert len(checked) >= 8, (
        f"only {len(checked)} key(s) state one pairing, so this check has almost nothing to "
        "read and proves little"
    )
    assert disowned, (
        "no item asks which claim contradicts the framework, so the disowning exemption is "
        "untested and could be masking a swapped key"
    )
    print(f"OK  {module.TOPIC[0]} pairing: {len(checked)} key(s) state one region-transition "
          f"pairing and every one matches EK 3.11.A.1; item(s) {disowned} state a mismatch "
          "under a stem that asks what the framework rejects.")


# ----------------------------------------------------------------- table items

def _row_value(table, row_label, header):
    heads = [cg.normalize(x) for x in table["headers"]]
    j = heads.index(cg.normalize(header))
    rows = [r for r in table["rows"] if cg.normalize(r[0]) == cg.normalize(row_label)]
    assert len(rows) == 1, f"row {row_label!r} appears {len(rows)} times"
    return str(rows[0][j])


def _region_of(text):
    names = _named(text, _REGION_WORDS)
    assert len(names) == 1, f"{text!r} names {names} regions, not exactly one"
    return names[0]


def _transition_of(text):
    names = _named(text, _TRANSITION_WORDS)
    assert len(names) == 1, f"{text!r} names {names} transitions, not exactly one"
    return names[0]


def _consistency(table):
    """Which tabulated rows state a pairing EK 3.11.A.1 makes."""
    out = {}
    for row in table["rows"]:
        lab = str(row[0])
        region = _region_of(_row_value(table, lab, REGIONCOL))
        claimed = _transition_of(_row_value(table, lab, CLAIMEDCOL))
        out[lab] = (region, claimed, PAIRING[region] == claimed)
    return out


def q13(table, item):
    state = _consistency(table)
    wrong = sorted(lab for lab, (_r, _c, ok) in state.items() if not ok)
    assert wrong == ["Row 3"], f"the tabulated rows the framework does not make are {wrong}"
    h.shows(item, wrong[0])
    return (f"each tabulated region was looked up in the framework's three associations, "
            f"giving {state}, with exactly one row inconsistent: {wrong[0]}")


def q14(table, item):
    state = _consistency(table)
    right = sorted(lab for lab, (_r, _c, ok) in state.items() if ok)
    assert len(right) == 2, f"the consistent tabulated rows are {right}"
    word = {0: "None of them", 1: "Exactly one", 2: "Exactly two", 3: "All three"}[len(right)]
    h.shows(item, word)
    return (f"looking each tabulated region up in the framework's associations gives {state}, "
            f"of which {len(right)} rows agree: {right}")


def _sample_regions(table):
    return {str(r[0]): _region_of(_row_value(table, str(r[0]), OBSERVED))
            for r in table["rows"]}


def _sample_for(table, transition):
    regions = _sample_regions(table)
    hits = sorted(lab for lab, reg in regions.items() if PAIRING[reg] == transition)
    assert len(hits) == 1, (
        f"exactly one tabulated sample must sit in the region the framework pairs with "
        f"{transition!r}; {hits} do, from {regions}"
    )
    return hits[0], regions


def q15(table, item):
    lab, regions = _sample_for(table, "electronic")
    assert lab == "Sample G", f"the electronic-transition sample is {lab}: {regions}"
    h.shows(item, lab)
    return (f"the tabulated regions are {regions}, and the framework pairs electronic energy "
            f"levels with exactly one of them, at {lab}")


def q16(table, item):
    lab, regions = _sample_for(table, "vibrational")
    assert lab == "Sample F", f"the vibrational-transition sample is {lab}: {regions}"
    h.shows(item, lab)
    return (f"the tabulated regions are {regions}, and the framework pairs molecular "
            f"vibrational levels with exactly one of them, at {lab}")


def q17(table, item):
    lab, regions = _sample_for(table, "rotational")
    assert lab == "Sample E", f"the rotational-transition sample is {lab}: {regions}"
    h.shows(item, lab)
    return (f"the tabulated regions are {regions}, and the framework pairs molecular "
            f"rotational levels with exactly one of them, at {lab}")


def q18(table, item):
    regions = _sample_regions(table)
    molecular = sorted(lab for lab, reg in regions.items()
                       if PAIRING[reg] in ("rotational", "vibrational"))
    assert len(molecular) == 2, f"the samples showing a molecular motion are {molecular}"
    word = {0: "None of them", 1: "Exactly one", 2: "Exactly two", 3: "All three"}[
        len(molecular)]
    h.shows(item, word)
    return (f"the tabulated regions are {regions}; the framework pairs two of them with a "
            f"motion of the molecule and one with an electronic transition, giving "
            f"{molecular}")


TABLE_CHECKS = {13: q13, 14: q14, 15: q15, 16: q16, 17: q17, 18: q18}

NUMERIC = {}


CLAIMS = [
 ("The different types of molecular motion or electronic transition",
  "EK 3.11.A.1's lead sentence, verbatim in substance; concentration is what topic 3.13's Beer-Lambert law relates absorbance to instead."),
 ("Transitions in molecular rotational levels",
  "EK 3.11.A.1's first sub-point: microwave radiation is associated with transitions in molecular rotational levels."),
 ("Transitions in molecular vibrational levels",
  "EK 3.11.A.1's second sub-point: infrared radiation is associated with transitions in molecular vibrational levels."),
 ("Transitions in electronic energy levels",
  "EK 3.11.A.1's third sub-point: ultraviolet and visible radiation is associated with transitions in electronic energy levels."),
 ("Microwave",
  "EK 3.11.A.1's first sub-point read from the transition back to the region; the pairing is the same in both directions."),
 ("Infrared",
  "EK 3.11.A.1's second sub-point read from the transition back to the region."),
 ("Ultraviolet and visible",
  "EK 3.11.A.1's third sub-point read from the transition back to the region."),
 ("A transition in its molecular rotational levels",
  "EK 3.11.A.1's lead sentence relates an absorption in a region to a type of transition, and its first sub-point supplies the type for the microwave region."),
 ("A transition in its molecular vibrational levels",
  "The same reading applied to the infrared region, whose type EK 3.11.A.1's second sub-point supplies."),
 ("A transition in its electronic energy levels",
  "The same reading applied to the ultraviolet region, whose type EK 3.11.A.1's third sub-point supplies."),
 ("its lead sentence names absorption or emission",
  "EK 3.11.A.1 opens with differences in absorption OR EMISSION of photons, so the associations run in both directions."),
 ("Transitions in electronic energy levels",
  "EK 3.11.A.1's third sub-point gives electronic energy levels to ultraviolet and visible radiation, and its second gives molecular vibrational levels to the infrared region."),
 ("Row 3",
  "EK 3.11.A.1's associations looked up for each tabulated region. q13 recomputes all three rows and checks exactly one is inconsistent."),
 ("Exactly two",
  "The same lookup counted across the table. Recomputed in q14."),
 ("Sample G",
  "EK 3.11.A.1's third sub-point applied to the tabulated regions. q15 checks exactly one tabulated sample sits in the region paired with electronic transitions."),
 ("Sample F",
  "EK 3.11.A.1's second sub-point applied to the tabulated regions. Recomputed in q16."),
 ("Sample E",
  "EK 3.11.A.1's first sub-point applied to the tabulated regions. Recomputed in q17."),
 ("Exactly two",
  "EK 3.11.A.1's first two sub-points name motions of the molecule and its third names electronic energy levels. q18 counts across the tabulated regions."),
 ("Infrared",
  "EK 3.11.A.1's second sub-point, used to predict which region to reach for, which is the prediction from a given model suggested skill 4.A asks for."),
 ("Microwave",
  "EK 3.11.A.1's first sub-point used the same way; the infrared region belongs to vibrational levels under the following sub-point."),
 ("Ultraviolet and visible",
  "EK 3.11.A.1's third sub-point used the same way; it is the only one of the three about electrons."),
 ("A region of the spectrum to a type of molecular motion or electronic transition",
  "EK 3.11.A.1's lead sentence and learning objective 3.11.A say this in the same words."),
 ("The one for ultraviolet and visible radiation",
  "EK 3.11.A.1's first two sub-points name molecular rotational and vibrational levels, which are motions; only the third names electronic energy levels."),
 ("Those for microwave and infrared radiation",
  "EK 3.11.A.1's first sub-point names molecular ROTATIONAL levels and its second molecular VIBRATIONAL levels, both of them motions of the molecule."),
 ("That transitions in molecular vibrational levels are taking place",
  "EK 3.11.A.1's lead sentence licenses reading an observed absorption as a transition of the associated type, and its second sub-point supplies that type for the infrared region."),
 ("That transitions in molecular rotational levels are taking place",
  "The same reading applied to the microwave region, whose type EK 3.11.A.1's first sub-point supplies."),
 ("The radio region",
  "EK 3.11.A.1's three sub-points name microwave, infrared, and ultraviolet and visible radiation, and attach an association to those three only."),
 ("Infrared radiation is associated with transitions in electronic energy levels",
  "EK 3.11.A.1 assigns electronic energy levels to ultraviolet and visible radiation and molecular vibrational levels to the infrared region, so this claim moves one sub-point's transition onto another's region. The pairing check permits this mismatch in a key only because the stem asks which claim contradicts the framework."),
 ("The ultraviolet and visible region",
  "EK 3.11.A.1's lead sentence covers emission as well as absorption and its third sub-point supplies the region for electronic energy levels."),
 ("Microwave with rotational levels, infrared with vibrational levels, and ultraviolet and visible with electronic levels",
  "EK 3.11.A.1's three sub-points in order; each rejected option keeps every region and every transition while exchanging at least one pair."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[14]["q"] = "In the spectrum above, which sample absorbed?"
        no_figure_language(mod)

    def photon_arithmetic(mod, cl):
        mod.QUESTIONS[0]["q"] = (mod.QUESTIONS[0]["q"]
                                 + " Use Planck's equation to decide.")
        no_other_topic(mod)

    def energy_ordering(mod, cl):
        ch = list(mod.QUESTIONS[1]["choices"])
        ch[0] = ("Transitions in molecular rotational levels, since microwave photons carry "
                 "lower energy than infrared photons")
        mod.QUESTIONS[1]["choices"] = ch
        no_energy_ordering(mod)

    def pairing_swapped(mod, cl):
        # The classic defect: infrared keyed to rotational levels.
        mod.QUESTIONS[2]["ans"] = 1
        cl[2] = ("Transitions in molecular rotational levels", cl[2][1])
        pairings_never_swapped(mod)

    def region_direction_swapped(mod, cl):
        mod.QUESTIONS[5]["ans"] = 1
        cl[5] = ("Microwave", cl[5][1])
        pairings_never_swapped(mod)

    def disowning_stem_rewritten(mod, cl):
        mod.QUESTIONS[27]["q"] = "Which claim does the framework make?"
        pairings_never_swapped(mod)

    def no_disowning_item_left(mod, cl):
        # A control on the exemption itself. BOTH disowning items have to be
        # neutralised for this to reach the branch it tests: a first version
        # touched only one of them, left the other in `disowned`, and fired on
        # an unrelated containment error instead -- a control that could not
        # fail the way it claimed to. Items 12 and 28 are the two that state a
        # mismatch, so both are given a correctly paired key here.
        fixed = "Microwave radiation goes with rotational levels"
        for idx in (11, 27):
            ch = list(mod.QUESTIONS[idx]["choices"])
            ch[0] = fixed
            mod.QUESTIONS[idx]["choices"] = ch
            cl[idx] = (fixed, cl[idx][1])
        pairings_never_swapped(mod)

    def table_row_made_consistent(mod, cl):
        mod.QUESTIONS[12]["table"] = dict(
            headers=h3_11._T_CHECK["headers"],
            rows=[["Row 1", "Microwave", "Molecular rotational levels"],
                  ["Row 2", "Infrared", "Molecular vibrational levels"],
                  ["Row 3", "Ultraviolet/visible", "Electronic energy levels"]])

    def second_table_row_made_wrong(mod, cl):
        mod.QUESTIONS[13]["table"] = dict(
            headers=h3_11._T_CHECK["headers"],
            rows=[["Row 1", "Microwave", "Molecular vibrational levels"],
                  ["Row 2", "Infrared", "Molecular vibrational levels"],
                  ["Row 3", "Ultraviolet/visible", "Molecular rotational levels"]])

    def two_samples_share_a_region(mod, cl):
        mod.QUESTIONS[14]["table"] = dict(
            headers=h3_11._T_SAMPLES["headers"],
            rows=[["Sample E", "Microwave"], ["Sample F", "Ultraviolet/visible"],
                  ["Sample G", "Ultraviolet/visible"]])

    def sample_regions_permuted(mod, cl):
        mod.QUESTIONS[16]["table"] = dict(
            headers=h3_11._T_SAMPLES["headers"],
            rows=[["Sample E", "Infrared"], ["Sample F", "Ultraviolet/visible"],
                  ["Sample G", "Microwave"]])

    def molecular_count_changes(mod, cl):
        mod.QUESTIONS[17]["table"] = dict(
            headers=h3_11._T_SAMPLES["headers"],
            rows=[["Sample E", "Microwave"], ["Sample F", "Ultraviolet/visible"],
                  ["Sample G", "Ultraviolet/visible"]])

    return [
        ("a stem referring to a spectrum the bank cannot show", figure_language),
        ("3.12's photon arithmetic creeping in", photon_arithmetic),
        ("a key ranking the regions by energy, which the framework does not do",
         energy_ordering),
        ("infrared keyed to rotational levels", pairing_swapped),
        ("a transition-to-region item keyed to the wrong region", region_direction_swapped),
        ("the disowning stem rewritten so the contradicting key becomes an assertion",
         disowning_stem_rewritten),
        ("the contradicting item turned into an ordinary one, so the exemption goes untested",
         no_disowning_item_left),
        ("the inconsistent tabulated row made consistent", table_row_made_consistent),
        ("a second tabulated row made inconsistent", second_table_row_made_wrong),
        ("two tabulated samples given the same region", two_samples_share_a_region),
        ("the tabulated sample regions permuted", sample_regions_permuted),
        ("a tabulated sample region changed so the molecular-motion count moves",
         molecular_count_changes),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h3_11, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h3_11)
no_other_topic(h3_11)
no_energy_ordering(h3_11)
pairings_never_swapped(h3_11)
h.run(h3_11, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
