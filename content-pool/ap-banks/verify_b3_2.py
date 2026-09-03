"""Key audit for AP BIOLOGY 3.2 Environmental Impacts on Enzyme Function.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the keyed choice and in no distractor, so the key
survives the shuffle ``export_units.py`` applies on export.

WHAT THE KEYS REST ON
---------------------
  3.2.A.1     a change to the molecular structure of a COMPONENT in an
              enzymatic system may change its function or efficiency
  3.2.A.1.i   denaturation is disruption of protein structure by TEMPERATURE,
              pH or CHEMICAL ENVIRONMENT, ELIMINATING catalysis
  3.2.A.1.ii  temperature and pH outside the optimal range FOR A GIVEN ENZYME
              change its structure BY DISRUPTING THE HYDROGEN BONDS, altering
              catalytic efficiency
  3.2.A.2     denaturation is REVERSIBLE IN SOME CASES
  3.2.B.1     the RELATIVE concentrations of substrates and products determine
              how efficiently the reaction proceeds
  3.2.B.2     higher temperature raises molecular speed and therefore COLLISION
              FREQUENCY, raising the rate UNTIL THE OPTIMAL TEMPERATURE
  3.2.B.3     COMPETITIVE inhibitors bind REVERSIBLY to the ACTIVE SITE;
              NONCOMPETITIVE inhibitors bind ALLOSTERIC SITES, changing enzyme
              activity

THE ONE CHAINED INFERENCE, DECLARED. The CED does not print "excess substrate
overcomes competitive inhibition". Items 10, 16 and 28 reach it by chaining EK
3.2.B.3 (the competitive inhibitor binds REVERSIBLY to the ACTIVE SITE, the
site the substrate must occupy) with EK 3.2.B.1 (RELATIVE concentrations decide
how efficiently the reaction proceeds). Both keys are worded as occupancy of
the active site, which is what those two sentences jointly say, and item 24
states the complementary case for an allosteric site.

NOTHING HERE RESTS ON TOPIC 3.1. Activation energy, the protein identity of
enzymes, the shape-and-charge rule and the experimental-design skill 3.C carry
no key in this module.

Items 13, 14, 15, 16, 19 and 27 carry tables. Every number is HYPOTHETICAL and
the stem says so; each keyed conclusion is recomputed below from the table
alone and the distractors are shown false against the same numbers.

FIVE choices per item (A-E), per SCIENCE_BRIEF.md.
"""
import cg_check as cg
import b3_2

TEMP = b3_2._T_TEMP
PH = b3_2._T_PH
INHIB = b3_2._T_INHIB
RECOVER = b3_2._T_RECOVER

H_TEMP = "Temperature (degrees Celsius)"
H_TRATE = "Reaction rate (hypothetical, micromoles of product per minute)"
H_PH = "pH of the reaction mixture"
H_J = "Rate for enzyme J (hypothetical, micromoles per minute)"
H_K = "Rate for enzyme K (hypothetical, micromoles per minute)"
H_SUB = "Substrate concentration (millimolar)"
H_NONE = "Rate with no inhibitor (hypothetical, micromoles per minute)"
H_L = "Rate with inhibitor L (hypothetical, micromoles per minute)"
H_M = "Rate with inhibitor M (hypothetical, micromoles per minute)"
H_DURING = "Rate during the treatment (hypothetical, micromoles per minute)"
H_AFTER = "Rate after return to the starting conditions (hypothetical, micromoles per minute)"


def _temp_series(table):
    return list(zip(cg.col(table, H_TEMP), cg.col(table, H_TRATE)))


def q13(table, item):
    pts = _temp_series(table)
    peak = max(pts, key=lambda p: p[1])
    assert [p[1] for p in pts].count(peak[1]) == 1, "the maximum rate must be unique"
    assert peak[0] != min(t for t, _ in pts), "'the lowest temperature tested' must be false"
    assert peak[0] != max(t for t, _ in pts), "'the highest temperature tested' must be false"
    assert pts[-1][1] == 0, "the highest temperature must give a zero rate, so 'rate has fallen to zero' names a different point"
    assert peak[1] > 0, "the peak rate must be nonzero"
    return (f"the rate reaches a single maximum of {peak[1]:.0f} at {peak[0]:.0f} degrees, which is "
            f"neither the lowest nor the highest temperature tested")


def q14(table, item):
    pts = _temp_series(table)
    peak_i = max(range(len(pts)), key=lambda i: pts[i][1])
    rising = [p[1] for p in pts[:peak_i + 1]]
    falling = [p[1] for p in pts[peak_i:]]
    assert all(b > a for a, b in zip(rising, rising[1:])), f"the limb below the peak must rise: {rising}"
    assert all(b < a for a, b in zip(falling, falling[1:])), f"the limb above the peak must fall: {falling}"
    assert len(rising) >= 2 and len(falling) >= 2, "both limbs must contain more than one point"
    return (f"the series rises {rising} up to the peak and falls {falling} beyond it, so the two "
            f"sides of the curve run in opposite directions and cannot share one cause")


def q15(table, item):
    ph = cg.col(table, H_PH)
    j = cg.col(table, H_J)
    k = cg.col(table, H_K)
    opt_j = ph[j.index(max(j))]
    opt_k = ph[k.index(max(k))]
    assert opt_j != opt_k, f"the two optima coincide at pH {opt_j}"
    assert j.count(max(j)) == 1 and k.count(max(k)) == 1, "each optimum must be unique"
    assert opt_j != max(ph) and opt_k != max(ph), "'both work best at the highest pH' must be false"
    assert opt_j != min(ph) or opt_k != min(ph), "'both work best at the lowest pH' must be false"
    assert max(j) > min(j) and max(k) > min(k), "'neither enzyme is affected by pH' must be false"
    return f"enzyme J peaks at pH {opt_j:.0f} and enzyme K at pH {opt_k:.0f}, two different optima"


def q27(table, item):
    ph = cg.col(table, H_PH)
    j = cg.col(table, H_J)
    k = cg.col(table, H_K)
    peak_i = k.index(max(k))
    assert k.count(max(k)) == 1, "enzyme K's maximum must be unique"
    assert 0 < peak_i < len(k) - 1, "K's maximum must lie inside the range, not at an end"
    assert all(b > a for a, b in zip(k[:peak_i + 1], k[1:peak_i + 1])), \
        f"K must rise up to its peak: {k[:peak_i + 1]}"
    assert all(b < a for a, b in zip(k[peak_i:], k[peak_i + 1:])), \
        f"K must fall beyond its peak: {k[peak_i:]}"
    assert ph[peak_i] != min(ph), "'highest at the lowest pH tested' must be false"
    assert len(set(k)) > 1, "'unchanged across the range' must be false"
    assert any(a != b for a, b in zip(j, k)), "'identical to enzyme J at every pH' must be false"
    return (f"enzyme K runs {k}, rising to a single maximum at pH {ph[peak_i]:.0f} and falling "
            f"afterward, and differs from enzyme J somewhere in the range")


def q16(table, item):
    sub = cg.col(table, H_SUB)
    none = cg.col(table, H_NONE)
    lo = cg.col(table, H_L)
    mi = cg.col(table, H_M)
    assert all(b > a for a, b in zip(sub, sub[1:])), "substrate concentration must increase down the table"
    rl = [x / n for x, n in zip(lo, none)]
    rm = [x / n for x, n in zip(mi, none)]
    assert all(b > a for a, b in zip(rl, rl[1:])), f"inhibitor L must be progressively overcome: {rl}"
    assert rl[0] < 0.5 and rl[-1] >= 0.9, \
        f"L must start well below and finish near the uninhibited rate: {rl[0]:.2f} to {rl[-1]:.2f}"
    assert max(rm) - min(rm) < 0.05, f"inhibitor M's fractional effect must be flat: {rm}"
    assert rm[-1] <= 0.7, "M must still be inhibiting at the highest substrate concentration"
    drops_l = [n - x for x, n in zip(lo, none)]
    assert len(set(drops_l)) > 1, "'L reduces the rate by a constant amount' must be false"
    assert any(a != b for a, b in zip(lo, mi)), "'the two produce the same rate everywhere' must be false"
    return (f"L recovers from {rl[0]:.2f} to {rl[-1]:.2f} of the uninhibited rate as substrate rises, "
            f"while M stays flat near {sum(rm) / len(rm):.2f}, so only L is overcome by substrate")


def q19(table, item):
    labs = cg.labels(table)
    during = dict(zip(labs, cg.col(table, H_DURING)))
    after = dict(zip(labs, cg.col(table, H_AFTER)))
    recovered = [k for k in labs if during[k] < after[k]]
    assert len(recovered) == 1, f"exactly one sample may show recovery; got {recovered}"
    r = recovered[0]
    best = max(after.values())
    assert after[r] >= 0.9 * best, "the recovering sample must return to near the untreated rate"
    unchanged = [k for k in labs if during[k] == after[k] and during[k] > 0]
    assert unchanged, "'the sample whose rate was unchanged throughout' must name a real row"
    dead = [k for k in labs if during[k] == 0 and after[k] == 0]
    assert dead, "'fell to zero and stayed at zero' must name a real row, so 'always reversible' is false"
    return (f"one sample falls from {after[r]:.0f} to {during[r]:.0f} and returns to {after[r]:.0f}, "
            f"while another never changes and another stays at zero, so recovery is neither universal nor absent")


CLAIMS = [
 ("loses the ability to catalyze reactions",
  "EK 3.2.A.1.i states that denaturation occurs when the protein structure is disrupted, eliminating the ability to catalyze reactions. Loss of structure and loss of catalysis are the two halves of that one sentence."),
 ("in pH, or in the chemical environment",
  "EK 3.2.A.1.i names exactly three causes of denaturation: a change in temperature, pH, or chemical environment. Substrate abundance affects efficiency under EK 3.2.B.1 but is not among the causes of denaturation."),
 ("Hydrogen bonds",
  "EK 3.2.A.1.ii states parenthetically that the structural change caused by temperature and pH outside the optimal range works by disrupting the hydrogen bonds. The peptide backbone is not what the statement names."),
 ("collide more frequently",
  "EK 3.2.B.2 states that higher environmental temperatures increase the average speed of movement of molecules in a solution, increasing the frequency of collisions between enzymes and substrates and therefore increasing the rate of reaction."),
 ("changes the enzyme's structure, so it catalyzes less efficiently",
  "EK 3.2.B.2 makes collision frequency raise the rate only UNTIL the optimal temperature is achieved, and EK 3.2.A.1.ii says temperature outside the optimal range changes the enzyme's structure and alters its catalytic efficiency."),
 ("reversible in some cases",
  "EK 3.2.A.2 states that in some cases enzyme denaturation is reversible, allowing the enzyme to regain activity. The qualifier is part of the statement, so neither an always nor a never reading is supported."),
 ("active site, and reversibly",
  "EK 3.2.B.3 states that competitive inhibitor molecules can bind reversibly to the active site of the enzyme. Binding to an allosteric site is what the same statement assigns to noncompetitive inhibitors."),
 ("allosteric site, changing the activity of the enzyme",
  "EK 3.2.B.3 states that noncompetitive inhibitors can bind to allosteric sites, changing the activity of the enzyme. Occupying the active site is what the same statement assigns to competitive inhibitors."),
 ("occupies the site the substrate must use",
  "EK 3.2.B.3 separates the two kinds of inhibitor by where they bind, the active site against an allosteric site. Both bind the enzyme, so the location is the distinction the statement draws."),
 ("compete for the same reversibly occupied site",
  "EK 3.2.B.3 places a competitive inhibitor reversibly at the active site, and EK 3.2.B.1 makes the relative concentrations of substrates determine how efficiently the reaction proceeds. Two molecules reversibly contesting one site is settled by their relative amounts."),
 ("relative concentrations of the substrates and the products",
  "EK 3.2.B.1 states that the relative concentrations of substrates and products determine how efficiently an enzymatic reaction proceeds. Cell mass, total enzyme inventory and organelle order are no part of that statement."),
 ("relative concentrations of substrate and product have shifted",
  "EK 3.2.B.1 makes the RELATIVE concentrations of substrates AND products the determinant of efficiency, so a shift in the balance between them changes the efficiency with no structural change to the enzyme."),
 ("at which the measured rate is highest",
  "Recomputed in q13 above. EK 3.2.B.2 makes the rate rise with temperature only until the optimal temperature is achieved, so the optimum is the unique peak of the series."),
 ("faster movement means more collisions",
  "Recomputed in q14 above. EK 3.2.B.2 supplies the rising limb through collision frequency and EK 3.2.A.1.ii supplies the falling limb through structural change outside the optimal range: two mechanisms, one curve."),
 ("different optimal pH values",
  "Recomputed in q15 above. EK 3.2.A.1.ii speaks of pH outside the optimal range FOR A GIVEN ENZYME, so the optimum is a property of the individual enzyme and two enzymes may differ."),
 ("Inhibitor L, because raising the substrate concentration nearly restores",
  "Recomputed in q16 above. EK 3.2.B.3 puts the competitive inhibitor reversibly at the active site and EK 3.2.B.1 makes relative concentrations decide occupancy, so only the competitive inhibitor's curve converges on the uninhibited one."),
 ("catalyzes its reaction less efficiently than before",
  "EK 3.2.A.1.ii states that pH outside the optimal range for a given enzyme changes its structure by disrupting the hydrogen bonds and alters the efficiency with which it catalyzes reactions. Five pH units from the optimum is such a change."),
 ("chemical environment disrupted the enzyme's structure",
  "EK 3.2.A.1.i names the chemical environment alongside temperature and pH as a cause of denaturation, in which protein structure is disrupted and the ability to catalyze reactions is eliminated."),
 ("returned to nearly its starting value afterward",
  "Recomputed in q19 above. EK 3.2.A.2 states that denaturation is reversible in some cases, allowing the enzyme to regain activity, and the signature is a fall during treatment followed by recovery after it."),
 ("collide less often",
  "EK 3.2.B.2 attributes a low rate at low temperature to reduced collision frequency between enzymes and substrates, while EK 3.2.A.1.i reserves denaturation for a structural disruption that eliminates catalysis. Slow is not denatured."),
 ("activity returns when the sample is brought back",
  "EK 3.2.A.1.i makes denaturation the elimination of catalytic ability through structural disruption and EK 3.2.A.2 allows recovery only in some cases. Restoring optimal conditions and re-assaying is the observation that separates a slowed enzyme from a destroyed one."),
 ("structure of the substrate the enzyme acts on",
  "EK 3.2.A.1 speaks of a change to the molecular structure of a COMPONENT in an enzymatic system rather than of the enzyme alone, and the substrate is such a component. Temperature, volume, duration and stirring are conditions, not molecular structures."),
 ("specified for a given enzyme",
  "EK 3.2.A.1.ii is worded as temperatures outside the optimal range FOR A GIVEN ENZYME, which makes the optimal range a property of the individual enzyme rather than a single universal value."),
 ("not occupying the site the substrate uses",
  "EK 3.2.B.3 places noncompetitive inhibitors at allosteric sites rather than at the active site, so raising the substrate concentration does not contest the inhibitor's binding and the change in activity persists."),
 ("catalyze its reaction more efficiently",
  "EK 3.2.A.1.ii says conditions outside the optimal range alter efficiency by disrupting the enzyme's structure and EK 3.2.A.1.i says severe disruption eliminates catalysis; neither supports an increase. The other four restate EK 3.2.A.1.i, EK 3.2.B.2, EK 3.2.B.3 and EK 3.2.B.1."),
 ("without the molecule ever entering the active site",
  "EK 3.2.B.3 states that noncompetitive inhibitors can bind to allosteric sites, changing the activity of the enzyme. A change in activity brought about through a site other than the active site is exactly what the statement describes."),
 ("rises to a maximum and then falls",
  "Recomputed in q27 above. Skill 4.B asks students to describe trends in data, and enzyme K's column rises to a single interior maximum and then declines, the shape EK 3.2.A.1.ii predicts either side of an optimal range."),
 ("fails to restore the uninhibited reaction rate",
  "Skill 6.C asks for reasoning that connects evidence to a claim. EK 3.2.B.3 separates the inhibitor types by binding site, and only the substrate-competition test distinguishes them, since lowering the rate at one concentration is common to both."),
 ("structural disruption was reversible",
  "EK 3.2.A.2 states that in some cases enzyme denaturation is reversible, allowing the enzyme to regain activity, and EK 3.2.A.1.ii supplies the disruption of hydrogen bonds that a raised temperature produces."),
 ("Temperature and pH act on the structure",
  "EK 3.2.A.1.i and EK 3.2.A.1.ii attribute structural change to temperature, pH and the chemical environment, while EK 3.2.B.1 makes the relative concentrations of substrate and product a matter of how efficiently the reaction proceeds rather than of the enzyme's structure."),
]

cg.check(b3_2, CLAIMS,
         table_checks={13: q13, 14: q14, 15: q15, 16: q16, 19: q19, 27: q27})
