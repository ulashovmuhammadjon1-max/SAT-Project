"""Key audit for AP CHEMISTRY 8.8 Properties of Buffers.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON. EK 8.8.A.1 is the topic's only statement, so the audit is
organised by which of its three clauses each key uses:

  a large concentration of BOTH members of a conjugate pair
                    1, 5, 6, 13, 14, 15, 21, 22, 26, 28, 30
  the conjugate acid reacts with added base
                    2, 12, 16, 18, 20, 25
  the conjugate base reacts with added acid
                    3, 8, 9, 11, 17, 19, 24
  those reactions are responsible for stabilizing pH
                    4, 10, 27, 29
  EK 8.6.A.1.i, that a strong acid's conjugate base is very weak, is what makes
  a strong acid and its salt fail the requirement          7, 23

THE FOUR-WAY BUFFER SPLIT is recorded in h8_4.py's header, and this module is
the MECHANISM entry: net ionic equations, no arithmetic. ``no_arithmetic``
asserts that nothing here takes a logarithm, computes a pH, counts moles or
compares two buffers' capacity -- the work of 8.9, 8.4 and 8.10 respectively.

THE DATA IS RECOMPUTED STRUCTURALLY. ``q5`` does not take the module's word for
which tabulated solutions are buffers: it re-derives them from the tabulated
descriptions against a declared list of conjugate pairs and a declared list of
strong acids and bases. The equation items likewise parse each tabulated
equation into reactants and products and re-derive which one consumes hydronium
and which consumes hydroxide.

NEGATIVE CONTROL: ``python3 verify_h8_8.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h8_8

WHAT = "What was dissolved in the water"
EQN = "Net ionic equation a student wrote"
ADDED = "What was added to an acetic acid buffer"

# The chemistry the structural check is allowed to know, declared once and in
# the open rather than buried in a regex.
PAIRS = [("CH3COOH", "CH3COONa"), ("NH3", "NH4Cl")]
STRONG = ("HCl", "HBr", "HI", "HClO4", "HNO3", "NaOH", "KOH")

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below|titration curve)(?![a-z])", re.I)

# 8.9 owns the logarithm and the pH arithmetic, 8.4 the mole counting, 8.10 the
# capacity comparison. Explicit phrases, never a bare word that has an innocent
# use: "concentration" is everywhere in this topic and is not banned.
_OTHER_TOPICS = re.compile(
    r"\\log|(?<![a-z])logarithm(?![a-z])|(?<![a-z])henderson(?![a-z])"
    r"|(?<![a-z])millimoles?(?![a-z])|(?<![a-z])moles?(?![a-z])"
    r"|(?<![a-z])buffer capacity(?![a-z])|(?<![a-z])capacity(?![a-z])", re.I)

# A key that states a pH VALUE would be 8.9's work.
_PH_VALUE = re.compile(r"(?<![A-Za-z])pH\s*(?:=|of)\s*\d", re.I)


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
    print(f"OK  {module.TOPIC[0]} figures: no item points at a picture.")


def no_arithmetic(module):
    """The mechanism topic. 8.9, 8.4 and 8.10 own the sums."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _OTHER_TOPICS.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: says {hit.group(0)!r}, which belongs to 8.4, 8.9 "
                f"or 8.10 -- {text[:70]!r}"
            )
        for text in item["choices"]:
            hit = _PH_VALUE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: a choice states a pH value ({hit.group(0)!r}), "
                "which is 8.9's arithmetic"
            )
    print(f"OK  {module.TOPIC[0]} scope: no logarithm, no pH value, no mole counting and "
          "no capacity comparison; the topic stays on the mechanism.")


# ------------------------------------------------------------------ helpers

def is_buffer(description):
    """Re-derive from a tabulated description whether the solution is a buffer.

    EK 8.8.A.1 needs both members of one conjugate pair present in quantity, and
    EK 8.6.A.1.i rules out a strong acid's conjugate base, which will not react
    with added acid. Both conditions are applied here rather than assumed.
    """
    text = str(description)
    if any(re.search(r"(?<![A-Za-z0-9])" + re.escape(s) + r"(?![A-Za-z0-9])", text)
           for s in STRONG):
        return False
    for acid, salt in PAIRS:
        both = all(re.search(r"(?<![A-Za-z0-9])" + re.escape(part) + r"(?![A-Za-z0-9])",
                             text) for part in (acid, salt))
        if both:
            return True
    return False


def sides(equation):
    """Reactants and products of a tabulated equation written with 'to'."""
    left, _, right = str(equation).partition(" to ")
    assert right, f"equation {equation!r} has no 'to' arrow"
    # Split on " + " with its spaces, never on the bare character: an ion is
    # written H3O+ and NH4+, so a bare split would tear the charge off the
    # formula and the check would silently find nothing.
    split = lambda s: [p.strip() for p in s.split(" + ") if p.strip()]
    return split(left), split(right)


# ------------------------------------------------------------------ table items

def q5(table, item):
    flags = {lab: is_buffer(row[1])
             for lab, row in zip(cg.labels(table), table["rows"])}
    buffers = sorted(lab for lab, ok in flags.items() if ok)
    assert buffers == ["1", "3"], f"the tabulated buffers re-derive as {buffers}: {flags}"
    h.shows(item, "Solutions 1 and 3")
    return (f"re-deriving each tabulated description against the declared conjugate pairs "
            f"and strong solutes gives buffers {buffers}")


def q6(table, item):
    lone = [row[1] for lab, row in zip(cg.labels(table), table["rows"]) if lab == "4"][0]
    assert "nothing else" in str(lone), f"row 4 reads {lone!r}"
    assert not is_buffer(lone), "row 4 must not re-derive as a buffer"
    h.shows(item, "Only one member of the conjugate pair")
    return f"the tabulated row for that solution reads {lone!r}, supplying one member only"


def q7(table, item):
    row = [r[1] for lab, r in zip(cg.labels(table), table["rows"]) if lab == "2"][0]
    assert "HCl" in str(row), f"row 2 reads {row!r}"
    assert not is_buffer(row), "row 2 must not re-derive as a buffer"
    assert any(s in str(row) for s in STRONG), \
        "the row must contain a solute the framework lists as strong"
    h.shows(item, "very weak conjugate base of a strong acid")
    return (f"the tabulated row {row!r} names a strong acid, whose conjugate base EK "
            "8.6.A.1.i calls very weak")


def q8(table, item):
    hits = []
    for lab, row in zip(cg.labels(table), table["rows"]):
        left, right = sides(row[1])
        if "H3O+" in left and "CH3COO-" in left and "CH3COOH" in right:
            hits.append(lab)
    assert hits == ["P"], f"the equations consuming hydronium with acetate are {hits}"
    h.shows(item, "Equation P")
    return (f"exactly one tabulated equation has acetate and hydronium as reactants and "
            f"the un-ionized acid as a product: {hits[0]}")


def q9(table, item):
    hits = []
    for lab, row in zip(cg.labels(table), table["rows"]):
        left, right = sides(row[1])
        if "OH-" in left and "CH3COOH" in left and "CH3COO-" in right:
            hits.append(lab)
    assert hits == ["Q"], f"the equations consuming hydroxide with the acid are {hits}"
    h.shows(item, "Equation Q")
    return (f"exactly one tabulated equation has the un-ionized acid and hydroxide as "
            f"reactants and acetate as a product: {hits[0]}")


def q10(table, item):
    pair_species = {"CH3COOH", "CH3COO-"}
    hits = []
    for lab, row in zip(cg.labels(table), table["rows"]):
        left, right = sides(row[1])
        if not (pair_species & set(left)) and not (pair_species & set(right)):
            hits.append(lab)
    assert hits == ["S"], f"the equations involving neither member of the pair are {hits}"
    h.shows(item, "Equation S")
    return (f"exactly one tabulated equation contains neither member of the conjugate "
            f"pair on either side: {hits[0]}")


def q19(table, item):
    acid_trials = [lab for lab, row in zip(cg.labels(table), table["rows"])
                   if "strong acid" in str(row[1])]
    assert acid_trials == ["1"], f"the trials adding acid are {acid_trials}"
    h.shows(item, "Trial 1")
    return f"exactly one tabulated trial adds strong acid: trial {acid_trials[0]}"


def q20(table, item):
    base_trials = [lab for lab, row in zip(cg.labels(table), table["rows"])
                   if "strong base" in str(row[1])]
    assert base_trials == ["2"], f"the trials adding base are {base_trials}"
    h.shows(item, "Trial 2")
    return f"exactly one tabulated trial adds strong base: trial {base_trials[0]}"


TABLE_CHECKS = {5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 19: q19, 20: q20}

NUMERIC = {}


CLAIMS = [
 ("large concentration of both members",
  "EK 8.8.A.1's opening clause: a buffer solution contains a large concentration of both members in a conjugate acid-base pair, because each member has its own job."),
 ("The conjugate acid",
  "EK 8.8.A.1: the conjugate acid reacts with added base. A base needs a proton to take, and the acid member is what has one."),
 ("The conjugate base",
  "EK 8.8.A.1: the conjugate base reacts with added acid, the mirror of the same sentence's other clause."),
 ("ability of the buffer to stabilize pH",
  "EK 8.8.A.1's closing clause: these reactions are responsible for the ability of a buffer to stabilize pH."),
 ("Solutions 1 and 3",
  "EK 8.8.A.1 with EK 8.6.A.1.i. q5 re-derives which tabulated descriptions supply both members of a conjugate pair and contain no strong solute."),
 ("Only one member of the conjugate pair",
  "EK 8.8.A.1 requires both members in large concentration; a weak acid alone supplies its conjugate base only in the trace its own ionization gives."),
 ("very weak conjugate base of a strong acid",
  "EK 8.8.A.1 requires the conjugate base to REACT with added acid, and EK 8.6.A.1.i makes a strong acid's conjugate base very weak, so half the mechanism is unavailable."),
 ("Equation P",
  "EK 8.8.A.1's added-acid clause. q8 parses every tabulated equation and checks exactly one consumes hydronium with the conjugate base."),
 ("Equation Q",
  "EK 8.8.A.1's added-base clause. q9 parses every tabulated equation and checks exactly one consumes hydroxide with the conjugate acid."),
 ("Equation S",
  "EK 8.8.A.1 assigns both reactions to members of the pair. q10 checks exactly one tabulated equation contains neither member on either side."),
 ("consumed by the conjugate base already present",
  "EK 8.8.A.1 has the conjugate base react with added acid, and makes those reactions responsible for the stabilization; pure water holds no such species."),
 ("consumed by the conjugate acid already present",
  "EK 8.8.A.1 has the conjugate acid react with added base. Swapping the two members inverts the statement."),
 ("only one member of the pair is present in large concentration",
  "EK 8.8.A.1 requires both. A weak acid does react with added base, which is half the mechanism; the other half is missing."),
 ("conjugate acid is not present in large concentration",
  "EK 8.8.A.1 requires both members; a salt supplies the conjugate base alone, so nothing is present in quantity to consume added base."),
 ("weak acid and a salt containing its conjugate base",
  "EK 8.8.A.1 requires both members of ONE pair, and EK 8.6.A.1.i rules out a strong acid's conjugate base, which will not react with added acid."),
 ("NH4+",
  "The conjugate acid is the species holding the extra proton, and EK 8.6.A.1.iv names ammonia among the common weak BASES, making the ammonium ion the acid member."),
 ("NH3, which accepts the added proton",
  "EK 8.8.A.1 assigns added acid to the conjugate base of the pair, which here is ammonia."),
 ("NH4+, which gives up a proton",
  "EK 8.8.A.1 assigns added base to the conjugate acid of the pair, which here is the ammonium ion."),
 ("Trial 1",
  "EK 8.8.A.1's added-acid clause applied to the tabulated trials. q19 re-derives which trial adds acid and checks it is unique."),
 ("Trial 2",
  "EK 8.8.A.1's added-base clause applied to the tabulated trials. q20 re-derives which trial adds base and checks it is unique."),
 ("plentiful enough to consume the acid or base that is added",
  "EK 8.8.A.1 pairs the requirement of a LARGE concentration with the reactions that consume the addition; a trace can consume only a trace."),
 ("HF and F-",
  "EK 8.8.A.1 requires both members of one conjugate pair, and EK 8.6.A.1.i makes a strong acid's conjugate base too weak to react with added acid."),
 ("conjugate base of a strong acid is very weak and will not react",
  "EK 8.8.A.1 with EK 8.6.A.1.i: the pair is a conjugate pair, but one member cannot perform the reaction the statement assigns it."),
 ("conjugate base is converted into the conjugate acid",
  "EK 8.8.A.1 has the conjugate base react with added acid, and a base that accepts a proton becomes its own conjugate acid."),
 ("conjugate acid is converted into the conjugate base",
  "EK 8.8.A.1 has the conjugate acid react with added base, and an acid that gives up its proton becomes its own conjugate base."),
 ("fail to stabilize the pH against added acid",
  "EK 8.8.A.1 assigns added acid to the conjugate base, so a solution short of that member has nothing to consume added hydronium, while still handling added base."),
 ("pH of the first changes far less",
  "EK 8.8.A.1 makes the conjugate base's reaction with added acid responsible for the stabilization, and only one of the two solutions holds that species in quantity."),
 ("a different member handles each",
  "EK 8.8.A.1 assigns added base to the conjugate acid and added acid to the conjugate base, two distinct jobs done by two distinct species."),
 ("resisting large changes rather than preventing any change",
  "EK 8.8.A.1's own word is STABILIZE, and its mechanism converts a large pH change into a small one rather than into none at all."),
 ("each consumes one kind of addition",
  "EK 8.8.A.1 states all three parts in one sentence: both members present in quantity, each reacting with one kind of addition, and those reactions responsible for the stabilization."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the diagram above, what does a buffer contain?"
        no_figure_language(mod)

    def arithmetic_creeps_in(mod, cl):
        mod.QUESTIONS[1]["q"] = mod.QUESTIONS[1]["q"] + " Use \\( \\log \\) to decide."
        no_arithmetic(mod)

    def capacity_creeps_in(mod, cl):
        mod.QUESTIONS[1]["q"] = "Which buffer has the greater buffer capacity for base?"
        no_arithmetic(mod)

    def ph_value_key(mod, cl):
        ch = list(mod.QUESTIONS[3]["choices"])
        ch[0] = "The ability of the buffer to hold a pH of 4.75"
        mod.QUESTIONS[3]["choices"] = ch
        cl[3] = ("hold a pH of 4", cl[3][1])
        no_arithmetic(mod)

    def third_buffer(mod, cl):
        mod.QUESTIONS[4]["table"] = dict(
            headers=h8_8._T_MIXTURES["headers"],
            rows=[["1", "equal amounts of CH3COOH and CH3COONa"],
                  ["2", "equal amounts of HCl and NaCl"],
                  ["3", "equal amounts of NH3 and NH4Cl"],
                  ["4", "equal amounts of CH3COOH and CH3COONa"],
                  ["5", "equal amounts of NaOH and NaCl"]])

    def strong_pair_counted_as_buffer(mod, cl):
        # The strong acid removed from the description, so the structural rule
        # would wrongly admit row 2 -- the check must notice the count changed.
        mod.QUESTIONS[4]["table"] = dict(
            headers=h8_8._T_MIXTURES["headers"],
            rows=[["1", "equal amounts of CH3COOH and CH3COONa"],
                  ["2", "equal amounts of NH3 and NH4Cl"],
                  ["3", "equal amounts of NH3 and NH4Cl"],
                  ["4", "CH3COOH and nothing else"],
                  ["5", "equal amounts of NaOH and NaCl"]])

    def equations_swapped(mod, cl):
        mod.QUESTIONS[7]["table"] = dict(
            headers=h8_8._T_EQUATIONS["headers"],
            rows=[["P", "CH3COOH + OH- to CH3COO- + H2O"],
                  ["Q", "CH3COO- + H3O+ to CH3COOH + H2O"],
                  ["R", "CH3COOH + H3O+ to CH3COOH2+ + H2O"],
                  ["S", "Na+ + OH- to NaOH"]])

    def spectator_equation_removed(mod, cl):
        mod.QUESTIONS[9]["table"] = dict(
            headers=h8_8._T_EQUATIONS["headers"],
            rows=[["P", "CH3COO- + H3O+ to CH3COOH + H2O"],
                  ["Q", "CH3COOH + OH- to CH3COO- + H2O"],
                  ["R", "CH3COOH + H3O+ to CH3COOH2+ + H2O"],
                  ["S", "CH3COOH + H2O to CH3COO- + H3O+"]])

    def both_trials_add_acid(mod, cl):
        mod.QUESTIONS[19]["table"] = dict(
            headers=h8_8._T_ADDITIONS["headers"],
            rows=[["1", "a small amount of strong acid"],
                  ["2", "a small amount of strong acid"]])

    return [("a stem referring to a diagram the bank cannot show", figure_language),
            ("a logarithm, which is 8.9's material", arithmetic_creeps_in),
            ("a capacity comparison, which is 8.10's material", capacity_creeps_in),
            ("a keyed choice stating a pH value, which is 8.9's arithmetic", ph_value_key),
            ("a third tabulated solution made into a buffer", third_buffer),
            ("the strong-acid row replaced, so the keyed pair of buffers is wrong",
             strong_pair_counted_as_buffer),
            ("the two buffering equations exchanged in the table", equations_swapped),
            ("the spectator equation replaced, so no tabulated equation is a non-buffer one",
             spectator_equation_removed),
            ("both tabulated trials made to add acid", both_trials_add_acid)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h8_8, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h8_8)
no_arithmetic(h8_8)
h.run(h8_8, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
