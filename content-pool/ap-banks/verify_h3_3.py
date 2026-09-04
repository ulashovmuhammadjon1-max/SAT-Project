"""Key audit for AP CHEMISTRY 3.3 Solids, Liquids, and Gases.

One (anchor, claim) per item, in module order.

WHY THIS FILE EXISTS. h3_3.py was left behind by a stopped agent with no
verifier at all, so nothing gated it. Every key below was read against the CED
before this file was written, and every phase attribution is now recomputed
rather than trusted.

WHAT THE KEYS REST ON.

  3.3.A.1  crystalline against amorphous; in BOTH cases the motion of the
           individual particles is limited and they do not undergo overall
           translation; the structure is influenced by interparticle
           interactions and the ability to pack together
                    1, 2, 3, 4, 14, 15, 16, 20, 24, 30
  3.3.A.2  a liquid's particles are in close contact and continually moving and
           colliding; the arrangement and movement are influenced by the nature
           and strength of the forces, e.g. polarity, hydrogen bonding and
           temperature
                    5, 6, 7, 17, 25, 28
  3.3.A.3  the solid and liquid phases of a particular substance TYPICALLY have
           similar molar volume, because in both the particles are in close
           contact at all times
                    8, 9, 19, 22, 26, 29
  3.3.A.4  gas particles are in constant motion; collision frequency and average
           spacing depend on temperature, pressure and volume; the constant
           motion together with MINIMAL effects of forces leaves a gas with
           neither a definite volume nor a definite shape
                    10, 11, 12, 18, 21, 23, 27
  the exclusion statement attached to 3.3.A.4                      13

THE PHASE TRANSCRIPTION IS THE REAL GATE. ``FRAMEWORK`` below transcribes which
phase the CED attaches each property to, and every tabulated item is recomputed
from that transcription together with the item's own table: the check looks up
which phases own the property, finds the tabulated sample rows carrying those
phases, and asserts the KEYED choice names exactly them. An item asking "which
phase" therefore cannot be keyed to a phase the framework does not say it of,
and permuting the table's phase labels makes the item fail.

TWO HEDGES. EK 3.3.A.3 says the molar volumes are TYPICALLY similar and EK
3.3.A.4 says the effects of forces between gas particles are MINIMAL, not
absent. ``hedges_preserved`` asserts that no key states either claim stripped of
its qualifier -- an unhedged "gases have no intermolecular forces" is the
single most common false thing a student is taught here, and topic 3.6 depends
on it being false.

THE EXCLUSION STATEMENT. ``no_phase_diagram_asked`` asserts that no STEM puts a
phase diagram in front of a student, which is what the exclusion statement rules
out. Item 13 names phase diagrams in its keyed choice, which is content ABOUT
the exclusion rather than an application of it, so the check reads stems only.

FIGURES. LO 3.3.A is about particulate models and this bank cannot show one, so
``no_figure_language`` asserts no item points at a picture.

NEGATIVE CONTROL: ``python3 verify_h3_3.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h3_3

PHASE = "Phase"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below|drawn above|drawn below)(?![a-z])", re.I)

# Material owned by neighbouring topics. 3.4 owns the ideal gas law, 3.5 the
# Maxwell-Boltzmann distribution, 3.7 molarity, 3.13 Beer-Lambert. 3.3 is a
# qualitative particulate-model topic and none of them belong in it.
_OTHER_TOPIC = re.compile(
    r"(?<![A-Za-z])(ideal gas law|nRT|Maxwell-Boltzmann|Beer-Lambert|molarity|"
    r"molar absorptivity)(?![A-Za-z])", re.I)

_PHASE_DIAGRAM = re.compile(r"(?<![A-Za-z])phase diagrams?(?![A-Za-z])", re.I)

# The molar-volume hedge. A key that says the two are similar must keep the
# framework's "typically"; the framework does not assert it without exception.
_MOLAR_SIMILAR = re.compile(r"(?<![a-z])similar molar volume(?![a-z])", re.I)
_TYPICALLY = re.compile(r"(?<![a-z])typical(?:ly)?(?![a-z])", re.I)

# The forces hedge. "There are no forces between gas particles" is false and the
# framework never says it -- it says the EFFECTS are minimal. A key may only
# carry that sentence where the stem frames it as what the wording AVOIDS.
_NO_FORCES = re.compile(
    r"(?<![a-z])no forces between (?:the )?gas particles(?![a-z])", re.I)
_AVOIDANCE_FRAME = re.compile(
    r"(?<![a-z])(avoid|does not claim|not claim|rule out|rules out|"
    r"stop short)(?![a-z])", re.I)

# A gas's particles are never in close contact. The swapped distractor in the
# liquid/gas comparison says exactly that, so no key may.
_GAS_CLOSE_CONTACT = re.compile(
    r"(?<![a-z])the gas[^.]{0,60}close contact(?![a-z])", re.I)


def _facing(item):
    """Every student-facing string on one question, including its table."""
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
    print(f"OK  {module.TOPIC[0]} figures: no item points at a particulate model it "
          "cannot show; the comparisons are carried as tables.")


def no_other_topic(module):
    """3.3 is qualitative. The equations belong to 3.4, 3.7 and 3.13."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _OTHER_TOPIC.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: uses {hit.group(0)!r}, which is a neighbouring "
                f"topic's material -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no ideal gas law, no distribution and no "
          "solution arithmetic; the topic stays on the particulate model.")


def no_phase_diagram_asked(module):
    """The exclusion statement attached to EK 3.3.A.4, enforced on stems."""
    for i, item in enumerate(module.QUESTIONS, 1):
        hit = _PHASE_DIAGRAM.search(item["q"])
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: the stem puts a phase diagram in front of the "
            f"student, which EK 3.3.A.4's exclusion statement rules out -- {item['q'][:70]!r}"
        )
    named = [i for i, item in enumerate(module.QUESTIONS, 1)
             if any(_PHASE_DIAGRAM.search(c) for c in item["choices"])]
    print(f"OK  {module.TOPIC[0]} exclusion: no stem asks a phase diagram to be read; "
          f"item(s) {named} name them only as the excluded content.")


def hedges_preserved(module):
    """EK 3.3.A.3's 'typically' and EK 3.3.A.4's 'minimal' must survive in the keys."""
    hedged, framed = [], []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = h.keyed(item)

        if _MOLAR_SIMILAR.search(key):
            assert _TYPICALLY.search(key), (
                f"{module.TOPIC[0]} q{i}: the key asserts similar molar volume without EK "
                f"3.3.A.3's 'typically' -- {key!r}"
            )
            hedged.append(i)

        if _NO_FORCES.search(key):
            # EK 3.3.A.4 says the EFFECTS of those forces are minimal, never
            # that the forces are absent. A key may carry the sentence only
            # where the stem asks what the framework's wording AVOIDS claiming.
            assert _AVOIDANCE_FRAME.search(item["q"]), (
                f"{module.TOPIC[0]} q{i}: the key states that there are no forces between "
                f"gas particles, but the stem does not frame it as what EK 3.3.A.4's "
                f"'minimal' wording avoids claiming -- stem {item['q'][:80]!r}"
            )
            framed.append(i)

    assert hedged, "no item keys EK 3.3.A.3's molar-volume comparison; the hedge check is idle"
    assert framed, "no item keys EK 3.3.A.4's 'minimal' hedge; the framing check is idle"
    print(f"OK  {module.TOPIC[0]} hedges: item(s) {hedged} keep EK 3.3.A.3's 'typically' "
          f"and item(s) {framed} carry EK 3.3.A.4's absence-of-forces sentence only under "
          "a stem that asks what the framework avoids claiming.")


def gas_never_in_close_contact(module):
    """EK 3.3.A.3 puts the SOLID and LIQUID particles in close contact, not a gas's."""
    for i, item in enumerate(module.QUESTIONS, 1):
        hit = _GAS_CLOSE_CONTACT.search(h.keyed(item))
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: the key places a gas's particles in close contact "
            f"({hit.group(0)!r}), which EK 3.3.A.3 says of the condensed phases instead"
        )
    print(f"OK  {module.TOPIC[0]} swap guard: no key places a gas's particles in close "
          "contact, which is the swap the liquid/gas comparison invites.")


# ------------------------------------------------------- the phase transcription

# Which phase the CED attaches each property to, transcribed from the framework
# and cited. The tabulated items are recomputed against THIS, so an item asking
# "which phase" cannot be keyed to a phase the framework does not say it of.
FRAMEWORK = {
    "no overall translation": (("solid",), "3.3.A.1"),
    "limited motion": (("solid",), "3.3.A.1"),
    "crystalline or amorphous": (("solid",), "3.3.A.1"),
    "close contact and continually colliding": (("liquid",), "3.3.A.2"),
    "polarity and hydrogen bonding named": (("liquid",), "3.3.A.2"),
    "in close contact": (("solid", "liquid"), "3.3.A.2 with 3.3.A.3"),
    "similar molar volume": (("solid", "liquid"), "3.3.A.3"),
    "constant motion": (("gas",), "3.3.A.4"),
    "spacing depends on temperature pressure and volume": (("gas",), "3.3.A.4"),
    "no definite volume nor definite shape": (("gas",), "3.3.A.4"),
}

_COUNT_WORD = {0: "None", 1: "Exactly one", 2: "Exactly two", 3: "All three"}


def phase_map(table):
    """Row label to phase, read by header name so a new column cannot repoint it."""
    heads = [cg.normalize(x) for x in table["headers"]]
    assert cg.normalize(PHASE) in heads, f"no {PHASE!r} column; headers are {table['headers']}"
    j = heads.index(cg.normalize(PHASE))
    out = {}
    for row in table["rows"]:
        lab = str(row[0])
        assert lab not in out, f"row label {lab!r} appears twice"
        out[lab] = cg.normalize(row[j])
    assert sorted(out.values()) == ["gas", "liquid", "solid"], (
        f"the table must name each of the three phases exactly once; it names {out}"
    )
    return out


def owners(table, prop):
    """The tabulated sample labels whose phase the framework gives ``prop`` to."""
    phases, _cite = FRAMEWORK[prop]
    pm = phase_map(table)
    labs = sorted(lab for lab, ph in pm.items() if ph in phases)
    assert len(labs) == len(phases), (
        f"property {prop!r} belongs to {phases} but the table supplies {labs}"
    )
    return labs, pm


def _single(prop):
    """A table check for an item keyed to the one sample carrying ``prop``."""
    def check(table, item):
        labs, pm = owners(table, prop)
        assert len(labs) == 1, f"{prop!r} is not a single-phase property: {labs}"
        h.shows(item, labs[0])
        phases, cite = FRAMEWORK[prop]
        return (f"EK {cite} gives {prop!r} to the {phases[0]} phase, which the table "
                f"places at {labs[0]} among {pm}")
    return check


def _pair(prop):
    """A table check for an item keyed to the two samples carrying ``prop``."""
    def check(table, item):
        labs, pm = owners(table, prop)
        assert len(labs) == 2, f"{prop!r} is not a two-phase property: {labs}"
        h.shows(item, f"{labs[0]} and {labs[1]}")
        phases, cite = FRAMEWORK[prop]
        return (f"EK {cite} gives {prop!r} to the {' and '.join(phases)} phases, which the "
                f"table places at {labs} among {pm}")
    return check


def _count(prop):
    """A table check for an item keyed to HOW MANY samples carry ``prop``."""
    def check(table, item):
        labs, pm = owners(table, prop)
        word = _COUNT_WORD[len(labs)]
        h.shows(item, word)
        phases, cite = FRAMEWORK[prop]
        return (f"EK {cite} gives {prop!r} to {len(phases)} of the three phases, so the "
                f"table's matching rows are {labs} out of {pm}")
    return check


TABLE_CHECKS = {
    16: _single("no overall translation"),
    17: _single("close contact and continually colliding"),
    18: _single("no definite volume nor definite shape"),
    19: _pair("similar molar volume"),
    20: _single("limited motion"),
    21: _single("constant motion"),
    22: _count("in close contact"),
    23: _single("spacing depends on temperature pressure and volume"),
    24: _single("crystalline or amorphous"),
    25: _single("polarity and hydrogen bonding named"),
}

NUMERIC = {}


CLAIMS = [
 ("arranged in a regular three-dimensional structure",
  "EK 3.3.A.1, verbatim in substance: solids can be crystalline, where the particles are arranged in a regular three-dimensional structure."),
 ("do not have a regular, orderly arrangement",
  "EK 3.3.A.1's other half, verbatim in substance: they can be amorphous, where the particles do not have a regular, orderly arrangement."),
 ("motion of the individual particles is limited",
  "EK 3.3.A.1 says of BOTH the crystalline and the amorphous case that the motion of the individual particles is limited and they do not undergo overall translation."),
 ("ability of the particles to pack together",
  "EK 3.3.A.1: the structure of the solid is influenced by interparticle interactions and the ability of the particles to pack together."),
 ("close contact with each other, and continually moving and colliding",
  "EK 3.3.A.2 states both clauses together, so the anchor carries both; each rejected option keeps one clause and swaps the other for another phase's description."),
 ("nature and strength of the forces",
  "EK 3.3.A.2: the arrangement and movement of particles are influenced by the nature and strength of the forces between the particles."),
 ("Polarity, hydrogen bonding, and temperature",
  "EK 3.3.A.2 gives exactly those three in parentheses as its own examples of what influences a liquid's particles."),
 ("typically have similar molar volume",
  "EK 3.3.A.3: the solid and liquid phases for a particular substance typically have similar molar volume. The hedge is part of the statement and hedges_preserved requires the key to keep it."),
 ("constituent particles are in close contact at all times",
  "EK 3.3.A.3 gives this as the reason for the similarity: because, in both phases, the constituent particles are in close contact at all times."),
 ("are in constant motion",
  "EK 3.3.A.4 opens by saying that in the gas phase the particles are in constant motion."),
 ("temperature, pressure, and volume",
  "EK 3.3.A.4: their frequencies of collision and the average spacing between them are dependent on temperature, pressure, and volume."),
 ("minimal effects of forces between them",
  "EK 3.3.A.4 gives both parts of the reason in one clause -- because of this constant motion, and minimal effects of forces between particles, a gas has neither a definite volume nor a definite shape."),
 ("interpreting phase diagrams",
  "The exclusion statement attached to EK 3.3.A.4 says understanding and interpreting phase diagrams will not be assessed on the AP Exam; the four rejected statements are required content."),
 ("Solids may be crystalline or amorphous",
  "EK 3.3.A.1 draws that division within the solid phase alone, and neither EK 3.3.A.2 nor EK 3.3.A.4 divides the liquid or gas phase in any comparable way."),
 ("Limited motion of the individual particles",
  "EK 3.3.A.1 asserts limited motion in the same sentence that denies overall translation, so the denial of translation leaves individual motion standing."),
 ("Sample 1",
  "EK 3.3.A.1 denies overall translation to solids only. Recomputed in the table check, which finds the tabulated solid row and requires the key to name it."),
 ("Sample 2",
  "EK 3.3.A.2 gives close contact together with continual collision to liquids. Recomputed against the tabulated phase labels."),
 ("Sample 3",
  "EK 3.3.A.4 gives neither a definite volume nor a definite shape to the gas phase. Recomputed against the tabulated phase labels."),
 ("Sample 1 and Sample 2",
  "EK 3.3.A.3 compares the solid and liquid phases of a particular substance and no other pair. Both tabulated rows are recomputed and the key must name exactly them."),
 ("Sample 1",
  "EK 3.3.A.1 limits the motion of the individual particles in solids, in both the crystalline and the amorphous case. Recomputed against the tabulated phase labels."),
 ("Sample 3",
  "EK 3.3.A.4 puts gas particles in constant motion, a separate statement from EK 3.3.A.2's continual movement in a liquid. Recomputed against the table."),
 ("Exactly two",
  "EK 3.3.A.2 puts a liquid's particles in close contact and EK 3.3.A.3 says both the solid and liquid phases keep their particles in close contact at all times, so the count is recomputed as two of the three tabulated rows."),
 ("Sample 3",
  "EK 3.3.A.4 attaches the dependence of collision frequency and spacing on temperature, pressure and volume to the gas phase. Recomputed against the table."),
 ("Sample 1",
  "EK 3.3.A.1 allows a solid to be crystalline or amorphous and draws no such division elsewhere. Recomputed against the tabulated phase labels."),
 ("Sample 2",
  "EK 3.3.A.2 names polarity, hydrogen bonding and temperature among the influences on a liquid's particles. Recomputed against the tabulated phase labels."),
 ("holding for every substance without exception",
  "EK 3.3.A.3's word is typically, which asserts a general pattern; the four rejected statements are each part of what the sentence does assert."),
 ("no forces between gas particles at all",
  "EK 3.3.A.4 says the effects of forces between gas particles are minimal rather than absent, and topic 3.6 attributes real deviations to those same interparticle attractions."),
 ("The liquid, whose particles the framework places in close contact",
  "EK 3.3.A.2 puts a liquid's constituent particles in close contact, while EK 3.3.A.4 describes a gas by the average spacing between its particles instead."),
 ("solid and liquid phases of a particular substance",
  "EK 3.3.A.3 names the solid and liquid phases for a particular substance, and gives close contact in both as the reason; the gas phase does not enter the comparison."),
 ("completely motionless",
  "EK 3.3.A.1 says the motion of a solid's individual particles is LIMITED, which asserts motion rather than denying it, so complete motionlessness contradicts the statement."),
]


def _permuted(rows):
    return dict(headers=h3_3._T_PHASES["headers"], rows=rows)


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the particulate diagram above, how is the solid drawn?"
        no_figure_language(mod)

    def neighbouring_topic(mod, cl):
        mod.QUESTIONS[9]["q"] = mod.QUESTIONS[9]["q"] + " Use the ideal gas law to decide."
        no_other_topic(mod)

    def phase_diagram_in_a_stem(mod, cl):
        mod.QUESTIONS[7]["q"] = "Reading the phase diagram, what are the molar volumes?"
        no_phase_diagram_asked(mod)

    def molar_hedge_dropped(mod, cl):
        # The key stripped of EK 3.3.A.3's qualifier. It still SAYS the two
        # molar volumes are similar, so nothing structural notices; only the
        # hedge check does.
        ch = list(mod.QUESTIONS[7]["choices"])
        ch[0] = "They have similar molar volume in every case"
        mod.QUESTIONS[7]["choices"] = ch
        cl[7] = ("similar molar volume in every case", cl[7][1])
        hedges_preserved(mod)

    def forces_asserted_not_framed(mod, cl):
        # Same keyed choice, but the stem now asks what the framework CLAIMS
        # rather than what its wording avoids claiming -- which turns a correct
        # item into the assertion that gases have no intermolecular forces.
        mod.QUESTIONS[26]["q"] = ("What does EK 3.3.A.4 establish about forces between "
                                  "gas particles?")
        hedges_preserved(mod)

    def hedge_check_made_idle(mod, cl):
        # A control on the CONTROL: if no item keyed either hedge, the two
        # assertions above would pass over an empty set and prove nothing.
        for item in mod.QUESTIONS:
            ch = list(item["choices"])
            ch[item["ans"]] = "An unrelated statement about containers"
            item["choices"] = ch
        hedges_preserved(mod)

    def gas_given_close_contact(mod, cl):
        # The swap the liquid/gas comparison invites, keyed.
        mod.QUESTIONS[27]["ans"] = 1
        cl[27] = ("The gas, whose particles the framework places in close contact",
                  cl[27][1])
        gas_never_in_close_contact(mod)

    def phase_labels_permuted(mod, cl):
        # Sample 1 is now the gas. Every "which sample" key that named the
        # solid is false, and the table check recomputes it and says so.
        rows = [["Sample 1", "gas"], ["Sample 2", "liquid"], ["Sample 3", "solid"]]
        for i in (16, 17, 18, 19, 20, 21, 22, 23, 24, 25):
            mod.QUESTIONS[i - 1]["table"] = _permuted(rows)

    def two_rows_share_a_phase(mod, cl):
        # A table naming only two phases cannot answer a three-way question,
        # and the count item's answer of two would come out wrong as well.
        rows = [["Sample 1", "solid"], ["Sample 2", "liquid"], ["Sample 3", "liquid"]]
        for i in (16, 22):
            mod.QUESTIONS[i - 1]["table"] = _permuted(rows)

    def pair_item_loses_a_row(mod, cl):
        # The molar-volume pair item keyed to the solid and liquid rows, with
        # the liquid row swapped to a gas: the recomputed pair no longer
        # matches the key.
        rows = [["Sample 1", "solid"], ["Sample 2", "gas"], ["Sample 3", "liquid"]]
        mod.QUESTIONS[18]["table"] = _permuted(rows)

    return [
        ("a stem referring to a particulate diagram the bank cannot show", figure_language),
        ("the ideal gas law creeping in from 3.4", neighbouring_topic),
        ("a stem asking a phase diagram to be read, which the exclusion statement bars",
         phase_diagram_in_a_stem),
        ("EK 3.3.A.3's 'typically' stripped out of its key", molar_hedge_dropped),
        ("the absence-of-forces sentence keyed under a stem that asserts it rather than "
         "naming it as avoided", forces_asserted_not_framed),
        ("every key replaced, so the hedge check would run over an empty set",
         hedge_check_made_idle),
        ("a gas's particles keyed as being in close contact", gas_given_close_contact),
        ("the tabulated phase labels permuted, so Sample 1 is the gas", phase_labels_permuted),
        ("two tabulated rows given the same phase", two_rows_share_a_phase),
        ("the molar-volume pair's liquid row turned into a gas", pair_item_loses_a_row),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h3_3, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h3_3)
no_other_topic(h3_3)
no_phase_diagram_asked(h3_3)
hedges_preserved(h3_3)
gas_never_in_close_contact(h3_3)
h.run(h3_3, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
