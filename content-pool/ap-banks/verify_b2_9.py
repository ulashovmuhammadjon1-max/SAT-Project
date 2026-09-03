"""Key audit for AP BIOLOGY 2.9 Cell Compartmentalization.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the keyed choice and in no distractor; the claim
states what the key rests on. ``export_units.py`` reshuffles the choices, so a
key held as a bare index is one edit away from pointing at a distractor -- the
anchor is what makes the key survive that.

WHAT THIS CAN AND CANNOT DO
---------------------------
There is no sympy in Biology. This file gates structure, key/anchor agreement
and the arithmetic of the four data items. It cannot tell whether the biology
is right; that is gated by the rule in SCIENCE_BRIEF.md that every key traces
to an essential knowledge statement, and by the CLAIMS text below, which names
the statement for every one of the thirty items.

WHAT THE KEYS REST ON
---------------------
Topic 2.9 has exactly two essential knowledge statements and every key here is
one of them:

  2.9.A.1  membranes and membrane-bound organelles compartmentalize
           intracellular metabolic processes and specific enzymatic reactions
  2.9.B.1  internal membranes facilitate cellular processes by minimizing
           competing interactions and by increasing the surface area where
           reactions can occur

Two items reach outside the topic for a supporting fact and say so: item 26
uses EK 3.2.A.1 (pH outside an enzyme's optimal range alters its efficiency)
and item 7 uses EK 3.1.A.1 (enzymes lower activation energy). Both are cited
in the claim rather than assumed.

Items 6, 16, 17 and 23 carry tables. Every number is HYPOTHETICAL and the stem
says so; each keyed conclusion is recomputed below from the table alone and
each distractor is shown false against the same numbers.

FIVE choices per item (A-E), per SCIENCE_BRIEF.md.
"""
import cg_check as cg
import b2_9

FRACTION = b2_9._T_FRACTION
AREA = b2_9._T_AREA
LEAK = b2_9._T_LEAK
SA = b2_9._T_SA

H_ACID = "Acid hydrolase activity (hypothetical, units per mg protein)"
H_CAT = "Catalase activity (hypothetical, units per mg protein)"
H_AREA = "Surface area (hypothetical, square micrometers)"
H_IN = "Acid hydrolase activity inside the vesicles (hypothetical, units)"
H_OUT = "Acid hydrolase activity in the surrounding solution (hypothetical, units)"
H_CRISTAE = "Number of cristae"
H_IMS = "Inner membrane surface area (square micrometers)"
H_ATP = "ATP produced per minute (arbitrary units)"


def q6(table, item):
    labs = cg.labels(table)
    acid = dict(zip(labs, cg.col(table, H_ACID)))
    cat = dict(zip(labs, cg.col(table, H_CAT)))
    top_acid = max(acid, key=acid.get)
    top_cat = max(cat, key=cat.get)
    assert top_acid != top_cat, "the key requires the two peaks in different fractions"
    # each peak must be a real peak, not a rounding difference
    assert acid[top_acid] >= 10 * max(v for k, v in acid.items() if k != top_acid), \
        "acid hydrolase peak is not sharp enough to call it concentrated"
    assert cat[top_cat] >= 10 * max(v for k, v in cat.items() if k != top_cat), \
        "catalase peak is not sharp enough to call it concentrated"
    # and every distractor false on the same numbers
    assert top_acid != "Cytosol", "'highest in the cytosol' must be false"
    assert cat[top_acid] < cat[top_cat], "'catalase highest where acid hydrolase is highest' must be false"
    return (f"acid hydrolase peaks in {top_acid} at {acid[top_acid]:.0f} and catalase in "
            f"{top_cat} at {cat[top_cat]:.0f}; each peak is at least tenfold above every other fraction")


def q16(table, item):
    labs = cg.labels(table)
    areas = dict(zip(labs, cg.col(table, H_AREA)))
    plasma = areas["Plasma membrane"]
    internal = {k: v for k, v in areas.items() if k != "Plasma membrane"}
    total_internal = sum(internal.values())
    assert total_internal > 10 * plasma, \
        f"internal total {total_internal} is not far more than plasma {plasma}"
    biggest = max(internal, key=internal.get)
    assert biggest != "Golgi apparatus", "'Golgi is the largest surface' must be false"
    assert areas["Rough endoplasmic reticulum"] != areas["Smooth endoplasmic reticulum"], \
        "'rough and smooth are equal' must be false"
    assert internal["Inner mitochondrial membrane"] > plasma, \
        "'inner mitochondrial membrane is less than plasma' must be false"
    return (f"the four internal membranes total {total_internal:.0f} against a plasma membrane of "
            f"{plasma:.0f}, and the largest single surface is the {biggest}")


def q17(table, item):
    # the key says the enzyme leaves the vesicles OVER TIME, so the time column
    # has to be read and shown to be ordered, not merely printed beside the data
    times = cg.col(table, "Treatment time (minutes)")
    assert all(b > a for a, b in zip(times, times[1:])), f"the sampling times must increase: {times}"
    inside = cg.col(table, H_IN)
    outside = cg.col(table, H_OUT)
    assert all(b < a for a, b in zip(inside, inside[1:])), "inside must fall at every step"
    assert all(b > a for a, b in zip(outside, outside[1:])), "outside must rise at every step"
    totals = [i + o for i, o in zip(inside, outside)]
    assert len(set(totals)) == 1, f"total activity is not conserved: {totals}"
    assert outside[0] == 0, "the experiment must start with no activity outside"
    return (f"inside falls {inside} while outside rises {outside} and the total stays at "
            f"{totals[0]:.0f}, so activity is relocating rather than being made or destroyed")


def q23(table, item):
    labs = cg.labels(table)
    area = dict(zip(labs, cg.col(table, H_IMS)))
    atp = dict(zip(labs, cg.col(table, H_ATP)))
    cristae = dict(zip(labs, cg.col(table, H_CRISTAE)))
    order = sorted(labs, key=lambda k: area[k])
    assert [atp[k] for k in order] == sorted(atp[k] for k in order), \
        "ATP must rise with surface area"
    ratios = {k: atp[k] / area[k] for k in labs}
    assert len(set(round(r, 6) for r in ratios.values())) == 1, \
        f"ATP per unit area is not constant: {ratios}"
    fewest = min(labs, key=lambda k: cristae[k])
    assert atp[fewest] == min(atp.values()), \
        "'fewest cristae gives the highest ATP' must be false"
    assert len(set(atp.values())) == len(labs), "'every mitochondrion is equal' must be false"
    return (f"ordering by inner membrane area gives {order} and ATP rises in the same order, "
            f"at a constant {list(ratios.values())[0]:.2f} units of ATP per square micrometer")


CLAIMS = [
 ("separate internal compartment",
  "EK 2.9.A.1 states that membranes and membrane-bound organelles compartmentalize intracellular metabolic processes and specific enzymatic reactions. Physical separation is what lets hydrolysis and synthesis run in one cell at one time."),
 ("competing interactions apart",
  "EK 2.9.B.1 names exactly two contributions of internal membranes, minimizing competing interactions and increasing the surface area where reactions can occur, and the key states both. Membranes supply no activation energy and no organelle is sealed against exchange."),
 ("escape into the cytosol",
  "EK 2.9.A.1 makes the organelle membrane the barrier that confines a specific enzymatic reaction. Removing the barrier puts the hydrolases among the macromolecules they were being kept away from, which is the disruption prediction skill 6.E asks for."),
 ("hold the proteins that carry out",
  "EK 2.9.B.1 names increased surface area for reactions as a contribution of internal membranes. A reaction run by membrane-embedded proteins scales with how much membrane is available to hold them, which is why the inner membrane is folded."),
 ("membrane-embedded proteins",
  "EK 2.9.B.1 ties internal membrane area to how much reaction can be supported. Reducing thylakoid area reduces the membrane-based chemistry that can run at once while leaving the compartment boundary itself intact."),
 ("different fraction",
  "Recomputed in q6 above: the two activities peak in different fractions, which is the observable signature of the separation asserted by EK 2.9.A.1, and every alternative reading is false against the same numbers."),
 ("keeps their concentrations high",
  "Compartmentalization concentrates the participants rather than changing the chemistry. EK 2.9.A.1 places specific enzymatic reactions inside membrane-bound organelles, and EK 3.1.A.1 leaves lowering activation energy to the enzyme itself, enclosed or not."),
 ("away from molecules it would otherwise attack",
  "EK 2.9.B.1 names minimizing competing interactions as a contribution of internal membranes. Sequestering a reactive product is that same principle applied to a product rather than to an enzyme."),
 ("into distinct compartments",
  "EK 2.9.A.1 makes compartmentalization of intracellular processes the function of membranes and membrane-bound organelles. The nuclear envelope applies that to two steps of a single information pathway."),
 ("broken down inappropriately",
  "EK 2.9.A.1 makes the compartment the reason a specific enzymatic reaction stays confined. A mis-sorted hydrolase is still catalytic; what changes is which molecules it now meets, which is the effect skill 6.E asks students to predict."),
 ("surface where the reactions of protein processing",
  "EK 2.9.B.1 names increasing the surface area where reactions can occur as a contribution of internal membranes. Building more of the membrane whose surface hosts the process is that statement applied directly."),
 ("recovered almost entirely in one isolated organelle fraction",
  "Compartmentalization is a claim about location, so its evidence must be a measurement of location. Recovery of activity in one fraction is what the separation of enzymatic reactions in EK 2.9.A.1 predicts; mass and energetics say nothing about where an enzyme sits."),
 ("conditions different from the rest of the cell",
  "EK 2.9.A.1 places metabolic processes inside membrane-bound organelles, and a boundary is what allows a local condition to persist. Without it the interior would equilibrate with the cytosol and the enzymes tuned to low pH would lose efficiency, per EK 3.2.A.1."),
 ("regulate the two pathways separately",
  "EK 2.9.B.1 names minimizing competing interactions as a purpose of internal membranes. Two pools of one intermediate on opposite sides of a membrane can be drawn down independently, which a single shared pool could not be."),
 ("applied in order",
  "EK 2.9.A.1 attributes compartmentalization of specific enzymatic reactions to membrane-bound organelles. Separate sacs are separate compartments, so one set of modifying enzymes can act without the next set acting at the same time."),
 ("far more surface than the plasma membrane",
  "Recomputed in q16 above: the internal membranes listed sum to many times the plasma membrane value, which is the quantitative form of EK 2.9.B.1's claim that internal membranes increase the surface area where reactions can occur."),
 ("leaving the vesicles over time",
  "Recomputed in q17 above: activity falls inside and rises outside while the total is conserved, so it is relocating and not being synthesized or destroyed. That the membrane was what confined it is EK 2.9.A.1 shown experimentally."),
 ("still occurs in the isolated fraction",
  "Skill 3.C asks for procedures aligned to the question asked. Only separating the compartment and re-testing distinguishes an organelle location from a cytosolic one; counting organelles or sequencing the enzyme leaves both possibilities alive."),
 ("concentrated in separate organelles",
  "Skill 6.B asks for evidence connected to the claim. The claim is that incompatible chemistry can coexist, so the supporting observation must be incompatible enzymes found in separate places, which is EK 2.9.A.1 and EK 2.9.B.1 expressed as data."),
 ("cargo separated from the cytosol during the journey",
  "EK 2.9.A.1 makes the membrane the boundary that compartmentalizes cell contents. A transport vesicle is a temporary compartment, so its contents stay separated from the cytosol until fusion delivers them."),
 ("now interfere with one another",
  "EK 2.9.B.1 names minimizing competing interactions as a contribution of internal membranes, so merging every compartment restores exactly the competition the boundaries were minimizing. That is the disruption prediction skill 6.E asks for."),
 ("same level in every fraction",
  "A confinement claim predicts an uneven distribution across fractions, so the observation that weakens it is an even one. The other listed observations are compatible with confinement or say nothing at all about location."),
 ("rises in step with the inner membrane surface area",
  "Recomputed in q23 above: the two columns rise together and the ratio of ATP to area is constant across all three mitochondria. That is EK 2.9.B.1's surface area claim expressed as data, which skill 4.B asks students to describe."),
 ("targeted to that compartment",
  "EK 2.9.A.1 attributes the localization of specific enzymatic reactions to compartmentalization by membranes and membrane-bound organelles. A reaction occurs where its enzyme is, and the enzyme is where the cell delivered it."),
 ("independent of the surrounding conditions",
  "EK 2.9.A.1 and EK 2.9.B.1 support the other four statements. Nothing in the framework claims that a compartment is independent of surrounding conditions, and organelles exchange substrates and products with the cytosol continuously."),
 ("outside the pH range in which it works best",
  "Compartments hold local conditions. EK 3.2.A.1 states that pH outside the optimal range for a given enzyme changes its structure and alters the efficiency with which it catalyzes reactions, so the immediate effect of release into neutral cytosol is a fall in efficiency."),
 ("Cell A can support a greater variety",
  "Both mechanisms named in EK 2.9.B.1 favor the cell with more internal membrane: more surface for membrane-based reactions, and more boundaries keeping competing interactions apart."),
 ("controlling what reaches them",
  "EK 2.9.A.1 makes the membrane a compartment boundary rather than a catalyst. What the boundary changes is which molecules are present at the enzyme, and that is how a specific enzymatic reaction is confined to a region."),
 ("cannot share one space at all",
  "The student's claim concedes rate but not compatibility, so the objection must be about compatibility. EK 2.9.B.1 lists minimizing competing interactions separately from surface area, and a hydrolase meeting the proteins it degrades is a difference in kind, not in speed."),
 ("Keeping incompatible processes apart",
  "EK 2.9.B.1 names precisely this pair: internal membranes facilitate cellular processes by minimizing competing interactions and by increasing the surface area where reactions can occur."),
]

cg.check(b2_9, CLAIMS, table_checks={6: q6, 16: q16, 17: q17, 23: q23})
