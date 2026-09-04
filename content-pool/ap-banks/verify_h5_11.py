"""Key audit for AP CHEMISTRY 5.11 Catalysis.

One (anchor, claim) per item, in module order.

WHY THIS FILE EXISTS AT ALL. ``h5_11.py`` was left behind by an agent that
stopped mid-topic, so it carried 30 well-formed questions and NO GATE. The
questions were read one by one against the CED before this was written, and the
one thing that had to change is recorded in the module header: the protonated
formic acid was written with its extra proton last, which every other bank here
reads as the SIZE of a charge (``SO42-`` is four oxygens and a charge of minus
two). ``mechanisms_balance`` below is what turned that up.

WHAT THE KEYS REST ON.

  5.11.A.1  a catalyst must increase the number of effective collisions AND/OR
            provide a path with a lower activation energy relative to the
            original reaction coordinate      1, 17, 18, 21, 24, 28, 29
  5.11.A.2  the net concentration of the catalyst is constant, though it is
            frequently consumed in the rate-determining step and regenerated in
            a subsequent step                 2, 3, 11, 13, 15, 19, 20, 22, 23, 27
  5.11.A.3  some catalysts bind the reactants, orienting them more favorably or
            lowering the barrier, often through a new bound intermediate; MANY
            enzymes work this way             4, 5, 6, 25
  5.11.A.4  acid-base catalysis is the covalent-bonding example, a reactant or
            intermediate gaining or losing a proton, which introduces a new
            intermediate and new elementary reactions   7, 8, 14, 26, 30
  5.11.A.5  surface catalysis binds a reactant or intermediate to the surface,
            introducing steps involving the new bound intermediates
                                              9, 10, 16
  EK 5.7.A.3 supplies the mirror definition of an intermediate      12
  EK 5.8.A.1 makes the rate law the molecularity of the rate-limiting step  23

THE MECHANISM TABLES ARE RECOMPUTED, NOT TRUSTED. Four items ask which
tabulated species is the catalyst and which is the intermediate. Nothing about
those keys is a matter of opinion, so ``h_equation`` resolves each mechanism
from the table alone -- consumed-then-regenerated is a catalyst, made-then-
consumed is an intermediate -- and the recomputed species must be the one named
in the KEYED choice and in none of the distractors. Every tabulated elementary
step is atom- and charge-balanced by the same parser, which is what forced the
notation change above.

THE TWO HEDGES THE FRAMEWORK MAKES, and which a key here could quietly drop:

  ``and/or``  EK 5.11.A.1 gives TWO routes. ``hedges_preserved`` asserts that no
              keyed choice presents a lower activation energy as the only way a
              catalyst can work.
  ``Many``    EK 5.11.A.3 says MANY enzymes function by binding, not all. The
              same check asserts that no keyed choice on an item mentioning
              enzymes makes that universal. This is not hypothetical: the very
              distractor sitting beside the key on q25 is the universal version,
              so an off-by-one key there ships the overreach.

NEGATIVE CONTROL: ``python3 verify_h5_11.py --selftest``. Every check above is
corrupted on purpose and must raise; each mutation was checked to violate the
thing its assertion states, rather than merely to differ from the original.
"""
import re
import sys

import cg_check as cg
import h_check as h
import h_equation as eq

import h5_11

STEP = "Elementary reaction"
EA = "Activation energy (kJ/mol)"
EREACT = "Energy of the reactants (kJ/mol)"
EPROD = "Energy of the products (kJ/mol)"

# A BARE "image" CANNOT GO IN HERE. The first draft banned it and immediately
# rejected q12's "the mirror image of EK 5.11.A.2's catalyst" -- a correct
# sentence with no picture in it. An over-matching checker is worse than none,
# so "image" is banned only where it is actually pointing at something.
_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below|energy profile above|energy profile below|"
    r"profile shown)(?![a-z])|"
    r"(?<![a-z])(?:the\s+)?image\s+(?:above|below|shown|shows|depicts)(?![a-z])|"
    r"(?<![a-z])(?:in|from)\s+the\s+image(?![a-z])", re.I)

# EK 5.11.A.1's "and/or" collapsed to one route. Matched only on the KEYED
# choice, because a distractor saying this is exactly the misconception the
# item is testing. The two orders are spelled out rather than joined by ``.*``
# so the pattern cannot span a sentence boundary and match two unrelated
# clauses.
_SOLE_ROUTE = re.compile(
    r"(?<![a-z])only\s+(?:\w+\s+){0,4}(?:lower|lowering|reduc\w+)\s+"
    r"(?:the\s+)?activation\s+energy(?![a-z])|"
    r"(?<![a-z])activation\s+energy\s+is\s+the\s+only(?![a-z])",
    re.I)

_ENZYME = re.compile(r"(?<![A-Za-z])enzymes?(?![A-Za-z])", re.I)
# A universal quantifier standing where the framework wrote "Many".
_UNIVERSAL = re.compile(r"(?<![A-Za-z])(all|every|always|without exception)(?![A-Za-z])",
                        re.I)


def _facing(item):
    """Every student-facing string on one question, its table included."""
    out = [item["q"], item["why"]] + list(item["choices"])
    t = item.get("table")
    if t:
        out += [str(x) for x in t["headers"]]
        out += [str(c) for r in t["rows"] for c in r]
    return out


def no_figure_language(module):
    """5.11 compares a catalyzed and an uncatalyzed path; the bank has no image."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, which this bank "
                f"cannot show -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: every energy comparison and every mechanism is "
          "carried as a table, and no item points at a picture.")


def hedges_preserved(module):
    """EK 5.11.A.1 says AND/OR and EK 5.11.A.3 says MANY. A key may not drop either."""
    n_enzyme = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        key = h.keyed(item)
        hit = _SOLE_ROUTE.search(key)
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: the keyed choice makes a lower activation energy the "
            f"ONLY route ({hit.group(0)!r}), but EK 5.11.A.1 pairs it with an increase in "
            "the number of effective collisions using and/or"
        )
        if any(_ENZYME.search(t) for t in [item["q"]] + list(item["choices"])):
            n_enzyme += 1
            hit = _UNIVERSAL.search(key)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: the keyed choice makes a universal claim about "
                f"enzymes ({hit.group(0)!r}); EK 5.11.A.3 says MANY enzymes function in "
                "this manner, not all"
            )
    print(f"OK  {module.TOPIC[0]} hedges: no key reduces EK 5.11.A.1's and/or to one route, "
          f"and neither of the {n_enzyme} enzyme item(s) universalises EK 5.11.A.3's 'many'.")


# ------------------------------------------------------------------ mechanisms

def steps(table):
    """The tabulated elementary reactions, in row order."""
    return [str(r[[cg.normalize(x) for x in table["headers"]].index(cg.normalize(STEP))])
            for r in table["rows"]]


def mechanisms_balance(module):
    """EK 4.2.A.2 is countable, so count it: every tabulated step balances.

    This is the check that found the one real defect in the module as
    inherited. A mechanism whose steps do not conserve atoms and charge is not
    a mechanism, and the catalyst it appears to contain is an artefact.
    """
    n = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        table = item.get("table")
        if not table or cg.normalize(STEP) not in [cg.normalize(x) for x in table["headers"]]:
            continue
        for s in steps(table):
            assert eq.atom_balanced(s), (
                f"{module.TOPIC[0]} q{i}: the tabulated step {s!r} does not conserve atoms "
                f"-- {eq.report(s)}"
            )
            assert eq.charge_balanced(s), (
                f"{module.TOPIC[0]} q{i}: the tabulated step {s!r} does not conserve charge "
                f"-- {eq.report(s)}"
            )
            n += 1
    print(f"OK  {module.TOPIC[0]} mechanisms: {n} tabulated elementary step(s) atom- and "
          "charge-balanced from the written formulas alone.")


def _sole(names, what, table):
    assert len(names) == 1, (
        f"the tabulated mechanism resolves to {len(names)} {what} ({names}), so no single "
        f"species can be keyed: {table['rows']}"
    )
    return names[0]


def _catalyst_item(table, item):
    """Recompute which tabulated species is consumed then regenerated."""
    ss = steps(table)
    cat = _sole(eq.catalysts(ss), "catalyst(s)", table)
    inter = _sole(eq.intermediates(ss), "intermediate(s)", table)
    # Named booleans, not two tuples read in parallel: a catalyst and an
    # intermediate are mirror images of one another, and comparing them by
    # position is how this project's inverted checker shipped.
    is_catalyst_first_seen_as_reactant = cat in eq.step_species(ss[0])[0]
    is_intermediate_first_seen_as_product = inter in eq.step_species(ss[0])[1]
    assert is_catalyst_first_seen_as_reactant, (
        f"the recomputed catalyst {cat!r} is not consumed by the first tabulated step, so "
        "it cannot be the species EK 5.11.A.2 describes"
    )
    assert is_intermediate_first_seen_as_product, (
        f"the recomputed intermediate {inter!r} is not produced by the first tabulated step"
    )
    assert cat != inter, "a species cannot be both the catalyst and the intermediate"
    return cat, inter


def q11(table, item):
    cat, inter = _catalyst_item(table, item)
    assert cat == "Cl", f"the recomputed catalyst is {cat!r}"
    h.shows(item, "Cl, the chlorine atom")
    return (f"the tabulated steps consume {cat} and regenerate it, leaving {inter} as the "
            "intermediate and neither in the overall equation")


def q12(table, item):
    cat, inter = _catalyst_item(table, item)
    assert inter == "ClO", f"the recomputed intermediate is {inter!r}"
    h.shows(item, "ClO, the chlorine monoxide radical")
    return (f"the tabulated steps produce {inter} and then consume it, the mirror of the "
            f"catalyst {cat}, which is consumed and then regenerated")


def q13(table, item):
    cat, inter = _catalyst_item(table, item)
    assert cat == "H3O+", f"the recomputed catalyst is {cat!r}"
    h.shows(item, "H3O+, the hydronium ion")
    return (f"the tabulated steps consume {cat} and regenerate it, leaving {inter} as the "
            "new intermediate EK 5.11.A.4 says acid-base catalysis introduces")


def q14(table, item):
    cat, inter = _catalyst_item(table, item)
    assert cat == "H3O+", f"the recomputed catalyst is {cat!r}"
    # EK 5.11.A.4's characteristic move is a PROTON gained or lost, so the
    # intermediate must differ from a reactant by exactly one hydrogen and one
    # unit of positive charge. Recomputed, not asserted.
    _, atoms_i, q_i = eq.species(inter)
    protonated = None
    for name in eq.step_species(steps(table)[0])[0]:
        _, atoms_r, q_r = eq.species(name)
        gained_one_h = (
            {el: n for el, n in atoms_i.items() if el != "H"}
            == {el: n for el, n in atoms_r.items() if el != "H"}
            and atoms_i.get("H", 0) - atoms_r.get("H", 0) == 1
            and q_i - q_r == 1
        )
        if gained_one_h:
            protonated = name
    assert protonated, (
        f"no tabulated reactant differs from the intermediate {inter!r} by exactly one "
        "proton, so the mechanism does not show the proton transfer EK 5.11.A.4 describes"
    )
    h.shows(item, "Acid-base catalysis, in which a reactant gains a proton")
    return (f"the tabulated intermediate {inter} is {protonated} plus exactly one hydrogen "
            f"and one unit of positive charge, and {cat} is consumed and regenerated")


def q15(table, item):
    cat, inter = _catalyst_item(table, item)
    assert cat == "M", f"the recomputed catalyst is {cat!r}"
    h.shows(item, "M, a site on the metal surface")
    return (f"the tabulated steps consume the surface sites {cat} and free them again, "
            f"leaving the bound species {inter} as the intermediate")


def q16(table, item):
    cat, inter = _catalyst_item(table, item)
    assert inter == "MH", f"the recomputed intermediate is {inter!r}"
    h.shows(item, "bound reaction intermediate")
    return (f"the tabulated steps produce {inter} and then consume it, which is EK "
            f"5.11.A.5's bound intermediate, while {cat} is the surface itself")


# ------------------------------------------------------------------ energies

def _paths(table):
    """The two tabulated paths, read by row label rather than by position."""
    labs = cg.labels(table)
    assert len(labs) == 2, f"the energy table must hold two paths, not {labs}"
    with_cat = [lab for lab in labs if "with the catalyst" == cg.normalize(lab)]
    without = [lab for lab in labs if "without the catalyst" == cg.normalize(lab)]
    assert len(with_cat) == 1 and len(without) == 1, (
        f"the two tabulated rows must be the catalyzed and the uncatalyzed path: {labs}"
    )
    return without[0], with_cat[0]


def q17(table, item):
    off, on = _paths(table)
    # Named booleans again, so nothing here depends on which row came first.
    barrier_fell = cg.cell(table, on, EA) < cg.cell(table, off, EA)
    reactants_unchanged = cg.cell(table, on, EREACT) == cg.cell(table, off, EREACT)
    products_unchanged = cg.cell(table, on, EPROD) == cg.cell(table, off, EPROD)
    assert barrier_fell, (
        f"the tabulated catalyzed barrier {cg.cell(table, on, EA)} is not below the "
        f"uncatalyzed {cg.cell(table, off, EA)}"
    )
    assert reactants_unchanged and products_unchanged, (
        "the tabulated endpoints move, so the key's claim that only the barrier changed "
        f"is false: reactants {cg.cell(table, off, EREACT)} to {cg.cell(table, on, EREACT)}, "
        f"products {cg.cell(table, off, EPROD)} to {cg.cell(table, on, EPROD)}"
    )
    h.shows(item, "activation energy, while leaving the reactant and product energies unchanged")
    return (f"the tabulated barrier falls from {cg.cell(table, off, EA):g} to "
            f"{cg.cell(table, on, EA):g} kJ/mol while both endpoint energies stay put")


def q18(table, item):
    off, on = _paths(table)
    drop = cg.cell(table, off, EA) - cg.cell(table, on, EA)
    assert drop > 0, f"the recomputed drop is {drop}, so nothing has been lowered"
    assert abs(drop - 60.0) < 1e-9, f"the recomputed drop is {drop} kJ/mol"
    # The distractors must be the wrong subtractions, not filler.
    span = cg.cell(table, off, EREACT) - cg.cell(table, off, EPROD)
    assert abs(span - 30.0) < 1e-9, (
        f"the reactant-minus-product distractor recomputes to {span}, not the tabulated 30"
    )
    h.shows(item, "60 kJ/mol")
    return (f"subtracting the two tabulated barriers, {cg.cell(table, off, EA):g} minus "
            f"{cg.cell(table, on, EA):g}, recomputes the drop as {drop:g} kJ/mol")


TABLE_CHECKS = {11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16,
                17: q17, 18: q18}


# ---------------------------------------------------------------- stem numerics

def n29(item):
    high, low = 150.0, 90.0
    assert low < high, "the item's premise is that one stated barrier is the lower"
    faster_is_the_lower_barrier = low < high
    assert faster_is_the_lower_barrier, (
        "EK 5.11.A.1 makes the LOWER activation energy the faster path"
    )
    assert abs(high - low - 60.0) < 1e-9, "the two stated barriers must differ by sixty"
    h.shows(item, "90 kJ/mol path")
    return (f"of the two stated barriers, {low:g} kJ/mol is the lower and so, under EK "
            f"5.6.A.4, the one a larger proportion of collisions can clear")


NUMERIC = {29: n29}


CLAIMS = [
 ("Increase the number of effective collisions and/or provide a reaction path with a lower activation energy",
  "EK 5.11.A.1, near verbatim: in order for a catalyst to increase the rate of a reaction, the addition of the catalyst must increase the number of effective collisions and/or provide a reaction path with a lower activation energy relative to the original reaction coordinate."),
 ("It is constant",
  "EK 5.11.A.2's opening sentence: in a reaction mechanism containing a catalyst, the net concentration of the catalyst is constant."),
 ("Consumed in the rate-determining step and regenerated in a subsequent step",
  "EK 5.11.A.2's second sentence, verbatim in substance: the catalyst will frequently be consumed in the rate-determining step, only to be regenerated in a subsequent step in the mechanism."),
 ("By binding to the reactants",
  "EK 5.11.A.3: some catalysts accelerate a reaction by binding to the reactants, and many enzymes function in this manner. The framework's hedge is 'many', which hedges_preserved holds the key to."),
 ("oriented more favorably or react with lower activation energy",
  "EK 5.11.A.3, near verbatim: the reactants are either oriented more favorably or react with lower activation energy."),
 ("new reaction intermediate in which the catalyst is bound to the reactants",
  "EK 5.11.A.3: there is often a new reaction intermediate in which the catalyst is bound to the reactants, which is the change to the mechanism the learning objective asks about."),
 ("A reactant or intermediate either gains or loses a proton",
  "EK 5.11.A.4 names acid-base catalysis as its example of covalent bonding between catalyst and reactant, in which a reactant or intermediate either gains or loses a proton. Adsorption onto a surface is EK 5.11.A.5's separate case."),
 ("new reaction intermediate and new elementary reactions involving that intermediate",
  "EK 5.11.A.4, verbatim in substance: this introduces a new reaction intermediate and new elementary reactions involving that intermediate."),
 ("binds to, or forms a covalent bond with, the surface",
  "EK 5.11.A.5, near verbatim: in surface catalysis, a reactant or intermediate binds to, or forms a covalent bond with, the surface."),
 ("Elementary reactions involving new bound reaction intermediates",
  "EK 5.11.A.5's second sentence: this introduces elementary reactions involving these new bound reaction intermediates, a change to the mechanism rather than to the overall equation."),
 ("Cl, the chlorine atom",
  "EK 5.11.A.2's consumed-then-regenerated species. q11 resolves the tabulated mechanism with h_equation and checks exactly one species is consumed by an earlier step and regenerated by a later one."),
 ("ClO, the chlorine monoxide radical",
  "EK 5.7.A.3's intermediate, produced by some steps and consumed by others. q12 recomputes it from the same table and checks it is the mirror of the catalyst, not the catalyst itself."),
 ("H3O+, the hydronium ion",
  "EK 5.11.A.2 with EK 5.11.A.4: the hydronium ion is consumed and regenerated, and the proton it donates is what makes this acid-base catalysis. q13 recomputes both facts from the table."),
 ("Acid-base catalysis, in which a reactant gains a proton",
  "EK 5.11.A.4's own example. q14 recomputes that the tabulated intermediate is a tabulated reactant plus exactly one hydrogen and one unit of positive charge, so the proton transfer is counted rather than asserted."),
 ("M, a site on the metal surface",
  "EK 5.11.A.5 has the reactant bind to the surface and EK 5.11.A.2 has the catalyst regenerated, so the surface sites are occupied and freed. q15 recomputes which tabulated species that is."),
 ("bound reaction intermediate",
  "EK 5.11.A.5's new bound reaction intermediate, with EK 5.7.A.3 supplying made-first-consumed-after. q16 recomputes it from the tabulated steps."),
 ("activation energy, while leaving the reactant and product energies unchanged",
  "EK 5.11.A.1 makes the catalyzed path one with a lower activation energy RELATIVE TO THE ORIGINAL REACTION COORDINATE, a different route between the same two ends. q17 recomputes that the barrier falls and both endpoints hold still."),
 ("60 kJ/mol",
  "EK 5.11.A.1's lowering of the barrier, measured. q18 subtracts the two tabulated barriers and separately recomputes the endpoint span that the thirty-unit distractor comes from."),
 ("regenerated as fast as it is consumed",
  "EK 5.11.A.2 keeps the net concentration constant by regeneration, and EK 5.7.A.2 makes the overall equation what the combined steps leave, so a species consumed and reformed cancels out of it."),
 ("present before the reaction begins and is consumed before being regenerated",
  "EK 5.11.A.2 for the catalyst and EK 5.7.A.3 for the intermediate, which is produced by some steps and consumed by others so that it is present only while the reaction is occurring."),
 ("larger proportion of collisions carries enough energy",
  "EK 5.11.A.1 offers the lower-barrier path as a route to a faster reaction, and EK 5.6.A.4 explains a rate through the proportion of particle collisions energetic enough to reach the transition state."),
 ("its net concentration is constant even though steps consume",
  "EK 5.11.A.2 states both halves at once: the net concentration is constant, and the catalyst is frequently consumed in the rate-determining step and regenerated afterwards."),
 ("frequently consumed in the rate-determining step, whose molecularity sets the rate law",
  "EK 5.11.A.2 puts the catalyst in the rate-determining step and EK 5.8.A.1 makes the rate law the molecularity of that step, so a species colliding there carries a power whatever becomes of it later."),
 ("Increasing the number of effective collisions",
  "EK 5.11.A.1's first route, the one paired with the lower barrier by and/or. The framework offers two, and this is the half that is not about the activation energy."),
 ("Many of them accelerate a reaction by binding to the reactants",
  "EK 5.11.A.3 says MANY enzymes function in this manner. The framework's own hedge is the whole point of the item, and hedges_preserved asserts no key on an enzyme item universalises it."),
 ("adds new elementary reactions and new intermediates",
  "EK 5.11.A.4 and EK 5.11.A.5 each say the catalyst introduces a new intermediate and new elementary reactions, and EK 5.11.A.1 makes the new path an alternative relative to the original reaction coordinate."),
 ("regenerated in a subsequent step, so that its net concentration is unchanged",
  "EK 5.11.A.2 states both clauses: consumed in the rate-determining step, regenerated in a subsequent step, net concentration constant."),
 ("alternative path relative to the original reaction coordinate",
  "EK 5.11.A.1 describes the catalyzed route as one relative to the ORIGINAL reaction coordinate, so it runs between the same reactants and products; EK 5.11.A.2 cancels the catalyst out of the overall equation."),
 ("90 kJ/mol path",
  "EK 5.11.A.1 makes the lower activation energy the faster route and EK 5.6.A.4 ties the rate to the proportion of collisions energetic enough to reach the transition state. Recomputed in n29."),
 ("a new bound intermediate, a proton transferred, or a surface site occupied and freed",
  "The learning objective for 5.11 asks for the relationship between a catalyst's effect and CHANGES IN THE REACTION MECHANISM, and EK 5.11.A.3, 5.11.A.4 and 5.11.A.5 each describe that effect as a new intermediate and new elementary reactions."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the energy diagram above, what has the catalyst done?"
        no_figure_language(mod)

    def sole_route_key(mod, cl):
        # EK 5.11.A.1's and/or collapsed to one route, in the KEYED choice.
        ch = list(mod.QUESTIONS[23]["choices"])
        ch[0] = "Nothing, since only lowering the activation energy can raise a rate"
        mod.QUESTIONS[23]["choices"] = ch
        cl[23] = ("only lowering the activation energy", cl[23][1])
        hedges_preserved(mod)

    def enzymes_universalised(mod, cl):
        # q25's own neighbouring distractor is this sentence, so an off-by-one
        # key ships it. The check must catch the sentence, not the index.
        ch = list(mod.QUESTIONS[24]["choices"])
        ch[0] = "All of them accelerate a reaction by binding to the reactants"
        ch[1] = "Some of them accelerate a reaction by binding to the reactants"
        mod.QUESTIONS[24]["choices"] = ch
        cl[24] = ("All of them accelerate a reaction by binding", cl[24][1])
        hedges_preserved(mod)

    def unbalanced_step(mod, cl):
        # One oxygen invented on the right of the ozone mechanism's first step.
        # Atom counts: left Cl O3, right Cl O4. It still LOOKS like a
        # mechanism, and Cl is still consumed and regenerated, so nothing but
        # the count can reject it.
        mod.QUESTIONS[10]["table"] = dict(
            headers=h5_11._M_OZONE["headers"],
            rows=[["Step 1", "Cl + O3 gives ClO + O3"],
                  ["Step 2", "ClO + O gives Cl + O2"]])
        mechanisms_balance(mod)

    def uncharged_step(mod, cl):
        # Charge left over on the right: the hydronium's plus is dropped from
        # the regeneration step, so atoms still nearly work but charge cannot.
        mod.QUESTIONS[12]["table"] = dict(
            headers=h5_11._M_ACID["headers"],
            rows=[["Step 1", "HCOOH + H3O+ gives H2COOH+ + H2O"],
                  ["Step 2", "H2COOH+ gives CO + H3O"]])
        mechanisms_balance(mod)

    def catalyst_and_intermediate_swapped(mod, cl):
        # The two tabulated steps reversed. Cl is now made first and consumed
        # after -- the INTERMEDIATE -- and ClO the catalyst, so q11's key is
        # false while every species in the table is unchanged.
        mod.QUESTIONS[10]["table"] = dict(
            headers=h5_11._M_OZONE["headers"],
            rows=[["Step 1", "ClO + O gives Cl + O2"],
                  ["Step 2", "Cl + O3 gives ClO + O2"]])

    def no_catalyst_at_all(mod, cl):
        # The hydronium is consumed and never given back, so the mechanism has
        # an intermediate and NO catalyst -- while both steps still balance for
        # atoms and charge, so nothing but the regeneration bookkeeping can
        # reject it. q13 keys a catalyst, so there must be exactly one.
        mod.QUESTIONS[12]["table"] = dict(
            headers=h5_11._M_ACID["headers"],
            rows=[["Step 1", "HCOOH + H3O+ gives H2COOH+ + H2O"],
                  ["Step 2", "H2COOH+ gives CO + H2O + H+"]])

    def proton_transfer_removed(mod, cl):
        # A mechanism that still balances, still has exactly one catalyst
        # (H3O+, consumed and regenerated) and exactly one intermediate -- but
        # the intermediate is an ADDUCT of the whole hydronium, not the
        # reactant plus one proton. EK 5.11.A.4's acid-base key is therefore
        # false, and the ONLY assertion that can fire is the proton count:
        # every other check on this item still passes.
        mod.QUESTIONS[13]["table"] = dict(
            headers=h5_11._M_ACID["headers"],
            rows=[["Step 1", "HCOOH + H3O+ gives HCOOHH3O+"],
                  ["Step 2", "HCOOHH3O+ gives CO + H2O + H3O+"]])

    def endpoints_moved(mod, cl):
        # The catalyzed path given DIFFERENT product energy. q17's key says the
        # endpoints are unchanged, which this makes false while still lowering
        # the barrier, so nothing but the endpoint comparison can reject it.
        mod.QUESTIONS[16]["table"] = dict(
            headers=h5_11._T_PATHS["headers"],
            rows=[["Without the catalyst", "150", "50", "20"],
                  ["With the catalyst", "90", "50", "5"]])

    def barrier_drop_changed(mod, cl):
        # The catalyzed barrier moved to 100, so the drop is 50 and the keyed
        # 60 kJ/mol is false. The barrier still falls, so the direction check
        # alone would not see it.
        mod.QUESTIONS[17]["table"] = dict(
            headers=h5_11._T_PATHS["headers"],
            rows=[["Without the catalyst", "150", "50", "20"],
                  ["With the catalyst", "100", "50", "20"]])

    def barrier_raised(mod, cl):
        # The catalyzed path given the HIGHER barrier. q18's drop goes negative,
        # which is the sign error a magnitude-only check would miss.
        mod.QUESTIONS[17]["table"] = dict(
            headers=h5_11._T_PATHS["headers"],
            rows=[["Without the catalyst", "90", "50", "20"],
                  ["With the catalyst", "150", "50", "20"]])

    return [("a stem referring to an energy diagram the bank cannot show", figure_language),
            ("a keyed choice reducing EK 5.11.A.1's and/or to the barrier alone",
             sole_route_key),
            ("a keyed choice universalising EK 5.11.A.3's 'many enzymes'",
             enzymes_universalised),
            ("a tabulated elementary step with an atom invented on the right",
             unbalanced_step),
            ("a tabulated elementary step that does not conserve charge", uncharged_step),
            ("the two tabulated steps reversed, which exchanges the catalyst and the "
             "intermediate", catalyst_and_intermediate_swapped),
            ("a tabulated mechanism with no species consumed and regenerated at all",
             no_catalyst_at_all),
            ("a tabulated mechanism with a catalyst but no proton transferred, behind an "
             "acid-base key", proton_transfer_removed),
            ("the tabulated product energy moved, so the key's 'endpoints unchanged' is false",
             endpoints_moved),
            ("the tabulated catalyzed barrier moved, so the keyed drop is the wrong size",
             barrier_drop_changed),
            ("the tabulated barrier RAISED by the catalyst, the sign error a magnitude "
             "check would miss", barrier_raised)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h5_11, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h5_11)
hedges_preserved(h5_11)
mechanisms_balance(h5_11)
h.run(h5_11, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
