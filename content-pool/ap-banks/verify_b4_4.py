"""Key audit for AP BIOLOGY 4.4 Feedback.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the keyed choice and in no distractor, so the key
survives the shuffle ``export_units.py`` applies on export.

WHAT THE KEYS REST ON
---------------------
The topic has ONE essential knowledge statement with two sub-statements, and
every key here is one of them:

  4.4.A.1     organisms use feedback mechanisms to maintain their internal
              environments in response to INTERNAL AND EXTERNAL changes
  4.4.A.1.i   NEGATIVE feedback maintains homeostasis by REDUCING THE INITIAL
              STIMULUS; a perturbed system is RETURNED TO ITS TARGET SET POINT;
              these processes operate at the MOLECULAR, CELLULAR AND ORGANISMAL
              levels
  4.4.A.1.ii  POSITIVE feedback AMPLIFIES responses; the initiating variable is
              MOVED FURTHER AWAY FROM THE INITIAL SET POINT; amplification
              occurs when the stimulus is FURTHER INTENSIFIED, initiating an
              ADDITIONAL RESPONSE

Four items classify one of the CED's own illustrative examples: blood sugar
regulation by insulin and glucagon under EK 4.4.A.1.i, and lactation in
mammals, the onset of labor in childbirth and the ripening of fruit under EK
4.4.A.1.ii. Each key is that classification and nothing more.

TWO EXAMPLES ARE SHARED WITH OTHER TOPICS AND ARE ASKED DIFFERENTLY. Insulin is
listed under EK 4.1.B.2 as a long-distance signal and module b4_1 asks it as a
question about range; item 8 here asks which feedback category blood sugar
regulation falls under. Fruit ripening is listed under EK 4.3.B.1 as a change
in gene expression altering phenotype and module b4_3 asks it that way; item 11
here asks its feedback category. Neither key would answer the other question.

NOTHING IS ASSERTED ABOUT HOW A POSITIVE FEEDBACK PROCESS ENDS. The framework
does not say, so no item asks. Items 6, 7, 18 and 21 are keyed only to
amplification and to movement away from the initial set point.

Items 13, 14, 15 and 16 carry tables. Every number is HYPOTHETICAL and the stem
says so; each keyed conclusion is recomputed below from the table alone, and
the distractors are shown false against the same numbers. No stem refers to a
figure.

FIVE choices per item (A-E), per SCIENCE_BRIEF.md.
"""
import cg_check as cg
import b4_4

RETURN = b4_4._T_RETURN
AMPLIFY = b4_4._T_AMPLIFY
GLUCOSE = b4_4._T_GLUCOSE
LEVELS = b4_4._T_LEVELS

H_T1 = "Time after the disturbance (minutes)"
H_V1 = "Measured value of the variable (hypothetical units)"
H_T2 = "Time after the stimulus (minutes)"
H_RESP = "Strength of the response produced (hypothetical units)"
H_T3 = "Time after a meal (minutes)"
H_GLU = "Blood glucose (hypothetical, milligrams per deciliter)"
H_INS = "Insulin in the blood (hypothetical, arbitrary units)"
H_D0 = "Deviation from the set point at the start (hypothetical units)"
H_D1 = "Deviation from the set point one hour later (hypothetical units)"


def q13(table, item):
    t = cg.col(table, H_T1)
    v = cg.col(table, H_V1)
    assert all(b > a for a, b in zip(t, t[1:])), f"time must increase down the table: {t}"
    assert v[-1] == v[0], f"the variable must come back to where it started: {v[0]} against {v[-1]}"
    peak = max(v)
    assert peak > v[0], "the disturbance must actually move the variable"
    i = v.index(peak)
    assert 0 < i < len(v) - 1, "the peak must lie inside the series, not at either end"
    assert all(b < a for a, b in zip(v[i:], v[i + 1:])), f"the variable must fall back steadily: {v[i:]}"
    assert len(set(v)) > 1, "'the variable never changed' must be false"
    return (f"the variable runs {v} over times {t}, rising to {peak:.0f} and returning exactly to its "
            f"starting value of {v[0]:.0f}")


def q14(table, item):
    t = cg.col(table, H_T2)
    v = cg.col(table, H_V1)
    r = cg.col(table, H_RESP)
    assert all(b > a for a, b in zip(t, t[1:])), f"time must increase down the table: {t}"
    assert all(b > a for a, b in zip(v, v[1:])), f"the variable must move steadily away: {v}"
    assert all(b > a for a, b in zip(r, r[1:])), f"the response must grow at every step: {r}"
    assert v[-1] > 2 * v[0] - v[0], "the variable must end clearly away from its starting value"
    assert v[-1] != v[0], "'the variable returns to its starting value' must be false"
    assert len(set(r)) == len(r), "'the response never changes' must be false"
    return (f"the variable runs {v} away from its starting value of {v[0]:.0f} while the response "
            f"grows {r}, both rising at every one of the {len(t)} times sampled")


def q15(table, item):
    t = cg.col(table, H_T3)
    g = cg.col(table, H_GLU)
    i = cg.col(table, H_INS)
    assert all(b > a for a, b in zip(t, t[1:])), f"time must increase down the table: {t}"
    assert g[-1] == g[0], f"glucose must return to its starting value: {g[0]} against {g[-1]}"
    assert i[-1] == i[0], f"insulin must return to its starting value: {i[0]} against {i[-1]}"
    gpeak, ipeak = g.index(max(g)), i.index(max(i))
    assert gpeak == ipeak and gpeak > 0, "glucose and insulin must peak together, after the meal"
    assert max(g) > g[0] and max(i) > i[0], "both must rise above their starting values"
    assert all(b < a for a, b in zip(g[gpeak:], g[gpeak + 1:])), f"glucose must then fall back: {g[gpeak:]}"
    assert all(b < a for a, b in zip(i[ipeak:], i[ipeak + 1:])), f"insulin must then fall back: {i[ipeak:]}"
    return (f"glucose runs {g} and insulin {i}: both rise after the meal, peak at {t[gpeak]:.0f} "
            f"minutes, and return exactly to their starting values of {g[0]:.0f} and {i[0]:.0f}")


def q16(table, item):
    labs = cg.labels(table)
    start = dict(zip(labs, cg.col(table, H_D0)))
    later = dict(zip(labs, cg.col(table, H_D1)))
    assert all(later[k] < start[k] for k in labs), \
        f"every system must move back toward its set point: {start} then {later}"
    assert all(start[k] > 0 for k in labs), "every system must begin away from its set point"
    for level in ("molecular", "cellular", "organismal"):
        hits = [k for k in labs if level in k.lower()]
        assert len(hits) == 1, f"exactly one row must be the {level} level; got {hits}"
    assert len(labs) == 3, f"the three named levels and no others: {labs}"
    return (f"deviation falls from {list(start.values())} to {list(later.values())} in all three rows, "
            f"one each at the molecular, cellular and organismal levels")


CLAIMS = [
 ("in response to internal and external changes",
  "EK 4.4.A.1 states that organisms use feedback mechanisms to maintain their internal environments in response to internal and external changes, naming both sources."),
 ("reducing the initial stimulus",
  "EK 4.4.A.1.i states that negative feedback mechanisms maintain homeostasis by reducing the initial stimulus to regulate physiological processes."),
 ("returned back to its target set point",
  "EK 4.4.A.1.i states that if a system is perturbed or disrupted, negative feedback mechanisms return the system back to its target set point."),
 ("The molecular, the cellular, and the organismal levels",
  "EK 4.4.A.1.i states that these processes operate at the molecular, cellular, and organismal levels, naming all three together."),
 ("amplify responses and processes",
  "EK 4.4.A.1.ii states that positive feedback mechanisms amplify responses and processes in biological organisms."),
 ("moved further away from the initial set point",
  "EK 4.4.A.1.ii states that the variable initiating the response is moved further away from the initial set point, which is what separates positive from negative feedback."),
 ("further intensified, which initiates an additional response",
  "EK 4.4.A.1.ii states that amplification occurs when the stimulus is further intensified, which in turn initiates an additional response that produces system change."),
 ("Negative feedback",
  "The CED lists blood sugar regulation by insulin and glucagon as its illustrative example for EK 4.4.A.1.i, the statement about negative feedback returning a system to its target set point."),
 ("Positive feedback",
  "The CED lists lactation in mammals as an illustrative example for EK 4.4.A.1.ii, the statement that positive feedback amplifies responses and moves the initiating variable further from the initial set point."),
 ("Positive feedback, in which the stimulus is further intensified",
  "The CED lists the onset of labor in childbirth as an illustrative example for EK 4.4.A.1.ii, which describes amplification through a stimulus that is further intensified, initiating an additional response."),
 ("Positive feedback, which amplifies the response",
  "The CED lists the ripening of fruit among the illustrative examples for EK 4.4.A.1.ii, the statement that positive feedback mechanisms amplify responses and processes in biological organisms."),
 ("brought back toward the set point or driven further from it",
  "EK 4.4.A.1.i returns the system to its target set point and EK 4.4.A.1.ii moves the initiating variable further away from it, so direction relative to the set point is the distinction the framework draws."),
 ("brought back to the value it started from",
  "Recomputed in q13 above. EK 4.4.A.1.i states that negative feedback returns a perturbed system back to its target set point, and the series rises after the disturbance and then falls back exactly to its starting value."),
 ("Positive feedback, because the variable moves further",
  "Recomputed in q14 above. EK 4.4.A.1.ii states that positive feedback amplifies responses and that the initiating variable moves further away from the initial set point; both features hold at every successive time."),
 ("followed by a rise in insulin and a return of glucose",
  "Recomputed in q15 above. EK 4.4.A.1.i states that negative feedback returns a perturbed system to its target set point, and the CED gives blood sugar regulation by insulin and glucagon as its example."),
 ("moved back toward its set point, at all three levels",
  "Recomputed in q16 above. EK 4.4.A.1.i states that negative feedback processes operate at the molecular, cellular, and organismal levels, and the table holds one system from each."),
 ("stays away from its set point instead of being returned",
  "EK 4.4.A.1.i makes the return to the target set point the work of the negative feedback mechanism, so removing the mechanism removes the return. Skill 6.E asks for the effect of disrupting one component of a system."),
 ("continues to move further away from the initial set point",
  "EK 4.4.A.1.ii states that the initiating variable is moved further away from the initial set point and that amplification occurs when the stimulus is further intensified, initiating an additional response."),
 ("Negative feedback operating at the organismal level",
  "EK 4.4.A.1.i makes the return of a perturbed system to its target set point the mark of negative feedback, and names the organismal level among the three at which such processes operate."),
 ("first is negative feedback and the second is positive feedback",
  "EK 4.4.A.1.i defines negative feedback by reduction of the initial stimulus and EK 4.4.A.1.ii defines positive feedback by the stimulus being further intensified, which assigns the two mechanisms directly."),
 ("feeds back on the stimulus, intensifying it further",
  "EK 4.4.A.1.ii describes the loop explicitly: amplification occurs when the stimulus is further intensified, which in turn initiates an additional response producing system change. Output acting back on the stimulus is what makes it feedback."),
 ("direction of the effect on the stimulus, not whether the outcome is good",
  "EK 4.4.A.1.i and EK 4.4.A.1.ii define the two kinds by what happens to the stimulus and to the variable relative to the set point. The framework names both among the mechanisms organisms use and lists ordinary processes under each."),
 ("returned to the same target set point after each perturbation",
  "EK 4.4.A.1.i states that a perturbed or disrupted system is returned back to its TARGET set point, a value the mechanism regulates around rather than one set by the size of the disturbance."),
 ("returns the system to after a disturbance",
  "EK 4.4.A.1.i states that negative feedback mechanisms return the system back to its target set point, which identifies the set point as the regulated value rather than an extreme or an average."),
 ("Negative feedback at the molecular level",
  "EK 4.4.A.1.i defines negative feedback by reduction of the initial stimulus and states that these processes operate at the molecular, cellular, and organismal levels. A product slowing its own production is that mechanism at the first of them."),
 ("grows larger as the variable moves further from its starting value",
  "EK 4.4.A.1.ii pairs amplification of the response with movement of the initiating variable further away from the initial set point, so evidence for the claim must show both features together."),
 ("respond to internal and external changes alike",
  "EK 4.4.A.1 states that organisms use feedback mechanisms to maintain their internal environments in response to internal AND EXTERNAL changes, naming both sources."),
 ("first illustrates negative feedback and the second illustrates amplification",
  "EK 4.4.A.1.i assigns reduction of the initial stimulus and return to the set point to negative feedback, and EK 4.4.A.1.ii assigns amplification and movement away from the set point to positive feedback."),
 ("Negative feedback moves the initiating variable further from the target set point",
  "EK 4.4.A.1.i has negative feedback RETURN the system to its target set point; moving further away is what EK 4.4.A.1.ii assigns to positive feedback. The other four options restate EK 4.4.A.1.ii, EK 4.4.A.1.i and EK 4.4.A.1."),
 ("returns the system to its set point; the other intensifies the stimulus",
  "EK 4.4.A.1.i gives reduction of the initial stimulus and return to the target set point, and EK 4.4.A.1.ii gives amplification through a further intensified stimulus with the variable moved further from the initial set point."),
]

cg.check(b4_4, CLAIMS, table_checks={13: q13, 14: q14, 15: q15, 16: q16})
