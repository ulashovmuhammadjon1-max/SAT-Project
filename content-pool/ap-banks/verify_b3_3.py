"""Key audit for AP BIOLOGY 3.3 Cellular Energy.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the keyed choice and in no distractor, so the key
survives the shuffle ``export_units.py`` applies on export.

WHAT THE KEYS REST ON
---------------------
  3.3.A.1     all living systems require an INPUT of energy
  3.3.A.2     life requires a highly ordered system and DOES NOT VIOLATE the
              first and second laws of thermodynamics
  3.3.A.2.i   ENERGY INPUT MUST EXCEED ENERGY LOSS to maintain order and power
              cellular processes
  3.3.A.2.ii  energy-RELEASING processes may be COUPLED with energy-REQUIRING
              ones
  3.3.A.2.iii SIGNIFICANT LOSS of order or energy flow RESULTS IN DEATH
  3.3.A.3     pathways are SEQUENTIAL for a more CONTROLLED transfer of energy;
              a PRODUCT of one reaction is typically the REACTANT of the next
  3.3.B.1     core metabolic pathways (glycolysis, oxidative phosphorylation)
              are CONSERVED ACROSS Archaea, Bacteria, and Eukarya

Items 10 and 28 also cite EK 2.1.A.1, which reads the presence of ribosomes in
cells in all forms of life as reflecting common ancestry -- the same inference
LO 3.3.B draws from conserved pathways, and the reason the two are compared.

THE EXCLUSION STATEMENT IS OBSERVED. The CED puts the equation for Gibbs free
energy beyond the scope of the exam. No item here asks for it, names it, or
turns on a sign convention only that equation supplies; the energy comparisons
are all input against loss, or supplied against required, which is the language
EK 3.3.A.2.i and EK 3.3.A.2.ii themselves use.

NOTHING HERE ASKS HOW GLYCOLYSIS OR OXIDATIVE PHOSPHORYLATION WORK. They enter
only as the two examples EK 3.3.B.1 names for a conserved core pathway; their
mechanisms are topics 3.4 and 3.5.

Items 12, 13, 14, 15, 16 and 27 carry tables. Every number is HYPOTHETICAL and
the stem says so; each keyed conclusion is recomputed below from the table
alone and the distractors are shown false against the same numbers.

FIVE choices per item (A-E), per SCIENCE_BRIEF.md.
"""
import cg_check as cg
import b3_3

PATHWAY = b3_3._T_PATHWAY
BALANCE = b3_3._T_BALANCE
DOMAINS = b3_3._T_DOMAINS
COUPLE = b3_3._T_COUPLE

H_UNTREATED = "Concentration in untreated cells (micromolar)"
H_TREATED = "Concentration in treated cells (micromolar)"
H_IN = "Energy taken in per day (kilojoules)"
H_LOST = "Energy lost per day (kilojoules)"
H_EXAM = "Species examined"
H_GLY = "Species carrying out glycolysis"
H_Z = "Species carrying out pathway Z"
H_REL = "Energy released by the first process (kilojoules per mole)"
H_REQ = "Energy required by the second process (kilojoules per mole)"


def _block_index(table):
    """Index of the last compound that RISES under treatment.

    The block sits immediately after it. Raises unless the table splits cleanly
    into a rising prefix and a falling suffix, which is the only shape the keyed
    reading is entitled to.
    """
    un = cg.col(table, H_UNTREATED)
    tr = cg.col(table, H_TREATED)
    rises = [i for i in range(len(un)) if tr[i] >= un[i]]
    falls = [i for i in range(len(un)) if tr[i] < un[i]]
    assert rises and falls, "the treatment must raise some compounds and lower others"
    assert max(rises) + 1 == min(falls), \
        f"the rising and falling compounds must not interleave: rises {rises}, falls {falls}"
    assert set(rises) | set(falls) == set(range(len(un))), "every compound must be classified"
    return max(rises), un, tr


def q12(table, item):
    i, un, tr = _block_index(table)
    assert i != len(un) - 1, "'at the final step' must be false"
    assert i != 0 or tr[0] > 2 * un[0], "'at the step producing the starting material' must be false"
    assert any(a != b for a, b in zip(un, tr)), "'the treatment changed nothing' must be false"
    assert not all(t > u for u, t in zip(un, tr)), "'every compound builds up' must be false"
    return (f"compounds 1 to {i + 1} hold or rise under treatment and compounds {i + 2} onward fall, "
            f"so the block lies between position {i + 1} and position {i + 2}")


def q27(table, item):
    i, un, tr = _block_index(table)
    assert tr[i] >= 2 * un[i], f"the upstream compound must rise clearly: {un[i]} to {tr[i]}"
    assert tr[i] == max(tr), "the accumulating compound must be the largest treated value"
    assert tr[i] != min(tr), "'falls below every other compound' must be false"
    assert tr[i] != un[i], "'unchanged by the treatment' must be false"
    return (f"the compound immediately upstream of the block goes from {un[i]:.0f} to {tr[i]:.0f} "
            f"micromolar, the highest treated value in the table")


def q13(table, item):
    labs = cg.labels(table)
    inn = dict(zip(labs, cg.col(table, H_IN)))
    out = dict(zip(labs, cg.col(table, H_LOST)))
    deficit = [k for k in labs if out[k] > inn[k]]
    assert len(deficit) == 1, f"exactly one organism may run a deficit; got {deficit}"
    d = deficit[0]
    assert max(inn, key=inn.get) != d, "'the largest intake' must not be the deficit organism"
    surplus = {k: inn[k] - out[k] for k in labs}
    assert max(surplus, key=surplus.get) != d, "'the largest surplus' must not be the deficit organism"
    assert [k for k in labs if inn[k] == out[k]] and \
        [k for k in labs if inn[k] == out[k]][0] != d, \
        "the break-even organism must exist and must not be the deficit organism"
    return (f"{d} takes in {inn[d]:.0f} and loses {out[d]:.0f} kilojoules a day, the only row in the "
            f"table where loss exceeds intake")


def q14(table, item):
    labs = cg.labels(table)
    inn = dict(zip(labs, cg.col(table, H_IN)))
    out = dict(zip(labs, cg.col(table, H_LOST)))
    surplus = {k: inn[k] - out[k] for k in labs}
    best = max(surplus, key=surplus.get)
    assert list(surplus.values()).count(surplus[best]) == 1, "the largest surplus must be unique"
    assert min(out, key=out.get) != best, "'the smallest daily loss' must be false"
    assert min(inn, key=inn.get) != best, "'the smallest daily intake' must be false"
    assert inn[best] != out[best], "'intake equals loss' must be false for the keyed organism"
    return (f"the surpluses are {sorted(surplus.values())} and the largest, {surplus[best]:.0f} "
            f"kilojoules, belongs to {best}, which holds neither the smallest intake nor the smallest loss")


def q15(table, item):
    labs = cg.labels(table)
    exam = dict(zip(labs, cg.col(table, H_EXAM)))
    gly = dict(zip(labs, cg.col(table, H_GLY)))
    z = dict(zip(labs, cg.col(table, H_Z)))
    assert len(labs) == 3, "the survey must cover the three domains"
    assert all(gly[k] == exam[k] and exam[k] > 0 for k in labs), \
        "the universal pathway must be present in every species of every domain"
    carriers = [k for k in labs if z[k] > 0]
    assert len(carriers) == 1, f"the confined pathway must appear in exactly one domain; got {carriers}"
    assert z[carriers[0]] == exam[carriers[0]], "within its own domain the confined pathway must be complete"
    assert sum(z.values()) < sum(gly.values()), \
        "'the confined pathway is in more species than the universal one' must be false"
    return (f"glycolysis appears in {sum(gly.values()):.0f} of {sum(exam.values()):.0f} species across "
            f"all three domains while pathway Z appears in {sum(z.values()):.0f}, all in {carriers[0]}")


def q16(table, item):
    labs = cg.labels(table)
    rel = dict(zip(labs, cg.col(table, H_REL)))
    req = dict(zip(labs, cg.col(table, H_REQ)))
    ok = [k for k in labs if rel[k] > req[k]]
    short = [k for k in labs if rel[k] < req[k]]
    assert ok and short, "the table must contain both sufficient and insufficient pairs"
    assert len(ok) < len(labs), "'all four pairs' must be false"
    assert len(ok) > 1, "'only the pair with the largest release' must be false"
    biggest = max(labs, key=lambda k: rel[k])
    assert set(ok) != {biggest}, "the sufficient pairs must not be exactly the largest-release pair"
    return (f"{len(ok)} of the {len(labs)} pairs release more than they require ({sorted(ok)}) and "
            f"{len(short)} fall short ({sorted(short)}), decided row by row rather than by release alone")


CLAIMS = [
 ("requires an input of energy",
  "EK 3.3.A.1 states that all living systems require an input of energy. The framework nowhere claims a system creates energy, that every system is photosynthetic, or that intake is stored without loss."),
 ("does not violate the first and second laws",
  "EK 3.3.A.2 states that life requires a highly ordered system and does not violate the first and second laws of thermodynamics. Orderliness and thermodynamic law are treated as compatible, not competing."),
 ("Energy input must exceed energy loss",
  "EK 3.3.A.2.i states that energy input must exceed energy loss to maintain order and to power cellular processes. Bare equality would leave nothing over for the ordering work the same statement requires."),
 ("Coupling, which lets the energy released",
  "EK 3.3.A.2.ii states that cellular processes which release energy may be coupled with cellular processes that require energy. Denaturation, conservation, compartmentalization and inhibition are introduced elsewhere for other purposes."),
 ("Death",
  "EK 3.3.A.2.iii states that significant loss of order or energy flow results in death. The framework gives this as the outcome, not as a setback from which recovery is expected."),
 ("more controlled transfer of energy",
  "EK 3.3.A.3 states that energy-related pathways are sequential to allow for a more controlled transfer of energy. Control rather than total yield is the reason the statement supplies."),
 ("typically the reactant for the following step",
  "EK 3.3.A.3 states that a product of a reaction in a metabolic pathway is typically the reactant for the subsequent step. That linkage is what makes a pathway a sequence rather than a set of separate reactions."),
 ("Archaea, Bacteria, and Eukarya",
  "EK 3.3.B.1 states that core metabolic pathways are conserved across all currently recognized domains and names all three of them."),
 ("Glycolysis and oxidative phosphorylation",
  "EK 3.3.B.1 gives these two parenthetically as its examples of core metabolic pathways conserved across all currently recognized domains."),
 ("most simply explained as inherited from an ancestor",
  "Skill 6.C asks for reasoning connecting evidence to a theory. EK 3.3.B.1 supplies conservation across all three domains as the evidence, and EK 2.1.A.1 applies the identical inference to ribosomes found in all forms of life."),
 ("just before the blocked step builds up",
  "EK 3.3.A.3 makes each product the reactant for the following step, so removing one step starves everything downstream and leaves the material entering that step with nowhere to go. Skill 6.E asks for this prediction."),
 ("last compound to rise into the first compound to fall",
  "Recomputed in q12 above. EK 3.3.A.3's product-to-reactant linkage means a block shows as accumulation immediately upstream and depletion downstream, and the junction between the two locates it."),
 ("energy loss is greater than its daily energy intake",
  "Recomputed in q13 above. EK 3.3.A.2.i requires input to exceed loss to maintain order, and EK 3.3.A.2.iii makes a significant loss of energy flow result in death."),
 ("exceeds its loss by the greatest amount",
  "Recomputed in q14 above. EK 3.3.A.2.i frames the requirement as input exceeding loss, so the surplus is the difference between the two columns; skill 5.A asks for that calculation."),
 ("of all three domains and the other is confined",
  "Recomputed in q15 above. EK 3.3.B.1 defines conservation across Archaea, Bacteria, and Eukarya, and the table separates a pathway with that distribution from one that lacks it."),
 ("energy released exceeds the energy required",
  "Recomputed in q16 above. EK 3.3.A.2.ii permits an energy-releasing process to be coupled to an energy-requiring one, and EK 3.3.A.2.i states the condition in the same terms, so the comparison is within each row."),
 ("order must be continually restored",
  "EK 3.3.A.2.i requires input to exceed loss on an ongoing basis to MAINTAIN order, and EK 3.3.A.2.iii makes failure of that flow fatal. Continuing loss is what makes the requirement continuous rather than one-time."),
 ("if the loss continues, it dies",
  "EK 3.3.A.2.i makes maintained order depend on input exceeding loss, and EK 3.3.A.2.iii states that a significant loss of order or energy flow results in death. Zero intake against continuing loss is that case."),
 ("taking in more energy than it loses, so no exception is needed",
  "EK 3.3.A.2 states that life requires a highly ordered system and does NOT violate the first and second laws of thermodynamics, and EK 3.3.A.2.i supplies the mechanism as an excess of input over loss."),
 ("each step supplies the material for the next",
  "EK 3.3.A.3 defines the pathway by that linkage: it is sequential, and a product of one reaction is typically the reactant for the subsequent step. Unconnected reactions in one compartment are not a pathway."),
 ("capture energy in stages",
  "EK 3.3.A.3 gives control of the energy transfer as the reason pathways are sequential. Staging does not alter the total energy involved, which EK 3.3.A.2 keeps within the first law."),
 ("Archaea, Bacteria, and Eukarya alike",
  "Skill 6.C asks for evidence connected to the claim. EK 3.3.B.1 defines the category by distribution across all currently recognized domains, so breadth within one domain, a large yield or a particular location does not establish it."),
 ("Only the cell with all five enzymes",
  "EK 3.3.A.3 makes each product the reactant for the next step, so a missing step severs the sequence and nothing downstream of it is made. Skill 6.E asks for the effect of disrupting one component of a system."),
 ("coupled to a process that releases energy",
  "EK 3.3.A.2.ii states that cellular processes releasing energy may be coupled with cellular processes that require energy, which is the framework's account of how a process that cannot proceed alone nevertheless proceeds."),
 ("maintain its order with no ongoing input of energy",
  "EK 3.3.A.1 requires an input of energy for all living systems and EK 3.3.A.2.i requires that input to exceed loss. The other four options restate EK 3.3.A.2.i, EK 3.3.A.2.ii, EK 3.3.B.1 and EK 3.3.A.3 directly."),
 ("conservation is defined across all three domains",
  "EK 3.3.B.1 sets the criterion as conservation across all currently recognized domains, Archaea, Bacteria, and Eukarya. Presence throughout a single domain does not satisfy a criterion stated across three."),
 ("rises well above the untreated value",
  "Recomputed in q27 above. EK 3.3.A.3 makes each compound the reactant for the following step, so blocking that step leaves the incoming compound with no route forward and it accumulates; skill 4.B asks for the data point that shows it."),
 ("read as evidence of descent from a common ancestor",
  "EK 2.1.A.1 says ribosomes are found in cells in all forms of life and reflect the common ancestry of all known life, and EK 3.3.B.1 places conserved core pathways under a learning objective about common ancestry. The inference is the same in both."),
 ("since all living systems do",
  "EK 3.3.A.1 states that ALL living systems require an input of energy, with no exemption for a low metabolic rate, and EK 3.3.A.2.i keeps the input-exceeds-loss requirement attached to maintaining order."),
 ("share core pathways across all three domains",
  "EK 3.3.A.1 and EK 3.3.A.2.i give the continuing surplus, EK 3.3.A.3 gives the sequential and controlled transfer, and EK 3.3.B.1 gives conservation across Archaea, Bacteria, and Eukarya."),
]

cg.check(b3_3, CLAIMS,
         table_checks={12: q12, 13: q13, 14: q14, 15: q15, 16: q16, 27: q27})
