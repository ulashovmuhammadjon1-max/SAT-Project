"""Key audit for AP BIOLOGY 2.5 Membrane Transport.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here instead of reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is the shared one in ``cg_check.py``. It cannot tell whether
the biology is right; that is gated by the CLAIMS text and by the
SCIENCE_BRIEF.md rule that every key must trace to a sentence in the CED.

WHAT THE KEYS REST ON
---------------------
EK 2.5.A.1 (selective permeability allows the formation of concentration
gradients of solutes across the membrane) carries items 1, 21 and 27.

EK 2.5.A.2 (passive transport is net movement from high to low concentration
without the direct input of metabolic energy) carries items 2, 10, 12, 14, 16,
18, 22, 26 and 29.

EK 2.5.A.3 (active transport requires the direct input of energy; in some cases
it moves molecules from low concentration to high) carries items 3, 4, 11, 13,
17 and 25. Items 9, 15, 28 and 30 rest on the CONTRAST between EK 2.5.A.2 and EK
2.5.A.3, and each claim names both halves.

EK 2.5.B.1 (endocytosis and exocytosis require energy to move large substances
or large amounts of substances into and out of cells) and its sub-point i (the
cell folds the plasma membrane in on itself, forming new small vesicles that
engulf material from the external environment) carry items 5, 6, 7, 8, 19, 23
and 24.

HONEST NOTE, REPEATED FROM THE MODULE. EK 2.5.B.1 has a second sub-point on
exocytosis whose text is not recoverable from the pdftotext dump of the CED used
for this bank. NO item keys a mechanism for exocytosis. Item 8 is the only item
that says anything about its direction, and it derives that from two readable
sentences: the lead sentence puts the pair's traffic "into and out of cells",
and sub-point i identifies endocytosis as the inward one. Nothing further about
exocytosis is asserted anywhere in this module.

Item 20 is the CED's suggested skill for this topic, 3.D, propose a new
investigation; its key rests on what separates a proposed cause from
alternatives, not on a content sentence.

DATA ITEMS: 13 to 20 carry tables. Every keyed conclusion is recomputed below
from the table alone. The direction column is checked against the framework's
own two directions, so a cell outside that vocabulary fails rather than ships.

NEGATIVE CONTROL: ``python3 verify_b2_5.py --selftest`` corrupts a key, an
anchor, two table cells and the notation on purpose and confirms each fails.
"""
import re
import sys

import cg_check as cg

_BANNED = [
    (re.compile(r"\\"), "a backslash: Biology is not typeset, so LaTeX would print raw"),
    (re.compile(r"(?<![A-Za-z])\d+\s?-\s?\d"), "a digit-hyphen-digit range: write 'to' instead"),
    (re.compile(r"\d\s?/\s?\d"), "a digit-slash-digit fraction: write it out in words"),
    (re.compile(r"\^"), "a caret exponent: Biology is not typeset, so write it in words"),
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


DIRN = "Direction of net movement relative to the concentration gradient"
BLOCKED = "Rate when ATP production is blocked (percentage of the untreated rate)"
INSIDE = "Concentration inside the cell (millimolar)"
OUTSIDE = "Concentration outside the cell (millimolar)"
VES = "Vesicles formed at the plasma membrane per cell in ten minutes"
PART = "Large particulate matter taken into the cell (arbitrary units)"

# The framework's own two directions. EK 2.5.A.2 gives the first to passive transport
# and EK 2.5.A.3 gives the second to the active case it describes.
DOWN = "from high concentration to low concentration"
UP = "from low concentration to high concentration"


def _directions(table):
    j = table["headers"].index(DIRN)
    cells = {r[0]: r[j] for r in table["rows"]}
    unknown = set(cells.values()) - {DOWN, UP}
    assert not unknown, f"direction cells outside the framework's two: {unknown}"
    return cells


def _energy_split(table):
    """Rows that nearly stop without ATP, and rows that keep almost all of their rate."""
    rates = {lab: cg.cell(table, lab, BLOCKED) for lab in cg.labels(table)}
    needs = sorted(lab for lab, v in rates.items() if v < 20)
    keeps = sorted(lab for lab, v in rates.items() if v > 80)
    assert set(needs) | set(keeps) == set(rates), \
        f"every row must fall clearly on one side or the other: {rates}"
    return rates, needs, keeps


def q13(table, item):
    dirs = _directions(table)
    rates, needs, keeps = _energy_split(table)
    assert needs == ["Process 2", "Process 4"], f"energy-requiring rows: {needs}"
    for lab in needs:
        assert dirs[lab] == UP, f"{lab} requires energy but runs {dirs[lab]!r}"
    return f"{needs} both run {UP} and fall to {[rates[l] for l in needs]} percent without ATP"


def q14(table, item):
    dirs = _directions(table)
    rates, needs, keeps = _energy_split(table)
    assert keeps == ["Process 1", "Process 3"], f"energy-independent rows: {keeps}"
    for lab in keeps:
        assert dirs[lab] == DOWN, f"{lab} keeps its rate but runs {dirs[lab]!r}"
    return f"{keeps} both run {DOWN} and keep {[rates[l] for l in keeps]} percent without ATP"


def q15(table, item):
    dirs = _directions(table)
    rates, needs, keeps = _energy_split(table)
    assert len(needs) == 2 and len(keeps) == 2, f"the split must be two and two: {rates}"
    assert all(dirs[l] == DOWN for l in keeps), "the rows that keep their rate must be the down-gradient ones"
    return (f"two rows fall to {[rates[l] for l in needs]} percent and two keep "
            f"{[rates[l] for l in keeps]} percent, and the ones that keep their rate run down the gradient")


def _gradient(table):
    return {lab: (cg.cell(table, lab, INSIDE), cg.cell(table, lab, OUTSIDE))
            for lab in cg.labels(table)}


def q16(table, item):
    g = _gradient(table)
    inward = sorted(lab for lab, (i, o) in g.items() if o > i)
    assert inward == ["Solute W"], f"rows with more outside than inside: {inward}"
    return f"exactly one row is more concentrated outside than inside, {inward[0]}: {g[inward[0]]}"


def q17(table, item):
    g = _gradient(table)
    outward = sorted(lab for lab, (i, o) in g.items() if i > o)
    assert outward == ["Solute X"], f"rows with more inside than outside: {outward}"
    return f"exactly one row is more concentrated inside than outside, {outward[0]}: {g[outward[0]]}"


def q18(table, item):
    g = _gradient(table)
    level = sorted(lab for lab, (i, o) in g.items() if i == o)
    assert level == ["Solute Y"], f"rows with equal concentrations: {level}"
    return f"exactly one row records equal concentrations on the two sides, {level[0]}: {g[level[0]]}"


def q19(table, item):
    ves = {lab: cg.cell(table, lab, VES) for lab in cg.labels(table)}
    part = {lab: cg.cell(table, lab, PART) for lab in cg.labels(table)}
    up, treated = "Untreated cells", "Cells with ATP synthesis blocked"
    assert ves[treated] < ves[up] / 5, f"vesicle formation must fall sharply: {ves}"
    assert part[treated] < part[up] / 5, f"particle uptake must fall sharply: {part}"
    return (f"vesicles fall from {ves[up]:.0f} to {ves[treated]:.0f} and uptake from "
            f"{part[up]:.0f} to {part[treated]:.0f} when ATP synthesis is blocked")


def q20(table, item):
    labs = cg.labels(table)
    assert len(labs) == 2, f"the design as it stands has {len(labs)} groups, not two"
    assert not any("restor" in lab.lower() for lab in labs), \
        "no recovery group is present yet, which is what makes the proposal an addition"
    return ("the table holds one treated and one untreated group and no recovery group, so "
            "restoring the energy supply is a comparison the design does not yet contain")


CLAIMS = [
 ("formation of concentration gradients of solutes",
  "EK 2.5.A.1 states that the selective permeability of membranes allows for the formation of concentration gradients of solutes across the membrane. A membrane letting everything through equally could hold no gradient."),
 ("high concentration to regions of low concentration without the direct input",
  "EK 2.5.A.2, near verbatim: passive transport is the net movement of molecules from regions of high concentration to regions of low concentration without the direct input of metabolic energy. Both the direction and the absence of an energy input are part of the definition."),
 ("direct input of energy to move molecules",
  "EK 2.5.A.3 states that active transport requires the direct input of energy to move molecules, which is exactly what EK 2.5.A.2 denies of passive transport."),
 ("low concentration to regions of high concentration",
  "EK 2.5.A.3 states that in some cases active transport is utilized to move molecules from regions of low concentration to regions of high concentration. The opposite direction is EK 2.5.A.2's passive case."),
 ("into and out of cells",
  "EK 2.5.B.1 states that the processes of endocytosis and exocytosis require energy to move large substances or large amounts of substances into and out of cells. Small nonpolar molecules cross with no process at all under EK 2.4.A.2."),
 ("folds the plasma membrane in on itself",
  "EK 2.5.B.1 i states that in endocytosis the cell takes in large molecules and particulate matter by folding the plasma membrane in on itself and forming new small vesicles that engulf material from the external environment. No gap, channel or diffusion step appears in that description."),
 ("Large molecules and particulate matter",
  "EK 2.5.B.1 i names exactly this as what endocytosis takes in. Small nonpolar molecules cross freely under EK 2.4.A.2 and need no vesicle."),
 ("Endocytosis brings material into the cell",
  "Derived from two readable sentences and no more: EK 2.5.B.1 puts the pair's traffic into and out of cells, and EK 2.5.B.1 i identifies endocytosis as the process that takes material in from the external environment, leaving exocytosis as the outward half. The CED's own sub-point on exocytosis is not recoverable from this dump and nothing about its mechanism is asserted."),
 ("Whether the direct input of energy is required",
  "EK 2.5.A.2 defines passive transport as occurring without the direct input of metabolic energy and EK 2.5.A.3 defines active transport as requiring it. Selective permeability is common ground under EK 2.5.A.1, and size is what separates the bulk processes of EK 2.5.B.1."),
 ("Passive transport",
  "EK 2.5.A.2 defines passive transport as net movement from high concentration to low concentration without the direct input of metabolic energy, which is what the observation reports. EK 2.5.A.3 and EK 2.5.B.1 all require an energy input."),
 ("Active transport",
  "EK 2.5.A.3 states that active transport requires the direct input of energy and that in some cases it moves molecules from low concentration to high, and both features of the observation match. Neither matches EK 2.5.A.2's energy-free definition."),
 ("net movement of a solute down its concentration gradient",
  "EK 2.5.A.2 defines passive transport as occurring without the direct input of metabolic energy, so it is the one listed process not dependent on the drug's target. EK 2.5.A.3 and EK 2.5.B.1 make the other three energy-requiring."),
 ("Process 2 and Process 4",
  "Recomputed in q13 above: exactly two rows both run from low concentration to high and fall below twenty percent of their rate when ATP production is blocked, which are the two features EK 2.5.A.3 attaches to active transport."),
 ("Process 1 and Process 3",
  "Recomputed in q14 above: exactly two rows run from high concentration to low and keep more than eighty percent of their rate without ATP, which are the two features EK 2.5.A.2 attaches to passive transport."),
 ("Two of them depend on a direct energy input and two do not",
  "Recomputed in q15 above: the four rows split two and two on the ATP result, and the rows that keep their rate are the down-gradient ones, so the table separates EK 2.5.A.3's group from EK 2.5.A.2's."),
 ("Solute W",
  "Recomputed in q16 above: exactly one row is more concentrated outside than inside. EK 2.5.A.2 gives passive transport the direction from high concentration to low, so inward passive movement needs that arrangement."),
 ("Solute X",
  "Recomputed in q17 above: exactly one row is more concentrated inside than outside, so adding more against that difference is movement from low to high, which EK 2.5.A.3 assigns to active transport."),
 ("Solute Y",
  "Recomputed in q18 above: exactly one row records equal concentrations on the two sides. EK 2.5.A.2 makes passive transport a NET movement, which equal concentrations leave with no direction."),
 ("Both vesicle formation and the uptake of large particles depend",
  "Recomputed in q19 above: both measurements fall to under a fifth of their untreated values when ATP synthesis is blocked. EK 2.5.B.1 requires energy for endocytosis and EK 2.5.B.1 i makes vesicle formation the mechanism by which large molecules and particulate matter are taken in."),
 ("Restore an energy supply to the treated cells",
  "Recomputed in q20 above: the design holds one treated and one untreated group and no recovery group. A treatment can act by more than one route, so showing that restoring the proposed cause restores the effect is what separates it from the alternatives. This is the CED's suggested skill 3.D for this topic."),
 ("selectively permeable, so solutes are not free to equalize",
  "EK 2.5.A.1 states that the selective permeability of membranes allows for the formation of concentration gradients, and EK 2.4.A.1 traces that permeability to the hydrophobic interior. Free permeability would abolish a gradient rather than allow it."),
 ("membrane is present throughout",
  "EK 2.5.A.2 defines passive transport as net movement ACROSS the membrane from high to low concentration without the direct input of metabolic energy, so the membrane is a participant rather than an absence. Movement from low to high is EK 2.5.A.3's active case."),
 ("The plasma membrane, which folds in on itself",
  "EK 2.5.B.1 i states that the cell takes in large molecules and particulate matter by folding the plasma membrane in on itself and forming new small vesicles, so the vesicle derives from the plasma membrane."),
 ("too big to cross the membrane the way small nonpolar molecules do",
  "EK 2.5.B.1 assigns the bulk processes to large substances or large amounts of substances and EK 2.5.B.1 i names large molecules and particulate matter, while EK 2.4.A.2 lets small nonpolar molecules cross freely with no process at all. Size rather than gradient direction separates the cases."),
 ("against its concentration gradient and stops when",
  "EK 2.5.A.3 attaches both features to active transport: the direct input of energy, and in some cases movement from low concentration to high. The rejected first alternative is EK 2.5.A.2's passive case, and crossing an intact membrane is common to both."),
 ("rate is unchanged when the cell's supply",
  "EK 2.5.A.2 defines passive transport as occurring without the direct input of metabolic energy, so insensitivity to losing that energy is the diagnostic. Accumulating against a gradient and forming vesicles are EK 2.5.A.3's and EK 2.5.B.1's energy-requiring cases."),
 ("cannot be maintained, because it was the selective permeability",
  "EK 2.5.A.1 states that the selective permeability of membranes is what allows for the formation of concentration gradients of solutes across the membrane, so removing the selectivity removes the condition the gradient rests on."),
 ("Passive transport needs no direct energy input",
  "EK 2.5.A.2 places passive transport outside the energy-requiring group, EK 2.5.A.3 places active transport inside it, and EK 2.5.B.1 states that both endocytosis and exocytosis require energy, so the four split one against three."),
 ("Passive transport, since movement follows the gradient",
  "Both reported features are the halves of EK 2.5.A.2's definition: net movement set by the concentration difference, and no direct input of metabolic energy. EK 2.5.A.3 and EK 2.5.B.1 all require that input."),
 ("Passive transport moves molecules down a gradient without a direct energy input",
  "The three parts line up with three statements: EK 2.5.A.2 for passive transport, EK 2.5.A.3 for active transport including the low to high case, and EK 2.5.B.1 for the energy requirement of endocytosis and exocytosis with large substances or large amounts of substances."),
]

TABLE_CHECKS = {13: q13, 14: q14, 15: q15, 16: q16, 17: q17, 18: q18, 19: q19, 20: q20}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("b2_5_mutant")
        mod.TOPIC = b2_5.TOPIC
        mod.QUESTIONS = copy.deepcopy(b2_5.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            style(mod)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def energy_split_confused(mod, claims):
        mod.QUESTIONS[12]["table"] = dict(
            headers=b2_5._T_ENERGY["headers"],
            rows=[[lab, d, ("96" if lab == "Process 2" else r)]
                  for lab, d, r in b2_5._T_ENERGY["rows"]])

    def direction_typo(mod, claims):
        mod.QUESTIONS[13]["table"] = dict(
            headers=b2_5._T_ENERGY["headers"],
            rows=[[lab, ("downhill" if lab == "Process 1" else d), r]
                  for lab, d, r in b2_5._T_ENERGY["rows"]])

    def second_inward_solute(mod, claims):
        mod.QUESTIONS[15]["table"] = dict(
            headers=b2_5._T_GRADIENT["headers"],
            rows=[["Solute W", "12", "140"], ["Solute X", "150", "5"], ["Solute Y", "30", "90"]])

    def vesicles_unaffected(mod, claims):
        mod.QUESTIONS[18]["table"] = dict(
            headers=b2_5._T_VESICLE["headers"],
            rows=[["Untreated cells", "46", "88"],
                  ["Cells with ATP synthesis blocked", "44", "6"]])

    print("negative controls:")
    must_fail("key moved off its anchor", lambda m, c: m.QUESTIONS[3].__setitem__("ans", 1))
    must_fail("anchor no longer in the keyed choice",
              lambda m, c: c.__setitem__(5, ("no such phrase", c[5][1])))
    must_fail("an up-gradient process made insensitive to blocking ATP", energy_split_confused)
    must_fail("a direction cell outside the framework's two", direction_typo)
    must_fail("a second solute made more concentrated outside", second_inward_solute)
    must_fail("vesicle formation made unaffected by blocking ATP", vesicles_unaffected)
    must_fail("a backslash macro in a choice",
              lambda m, c: m.QUESTIONS[1]["choices"].__setitem__(4, "Movement only where \\Delta c is zero"))
    print("all negative controls raised as required.")


import b2_5  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(b2_5)
cg.check(b2_5, CLAIMS, table_checks=TABLE_CHECKS)
