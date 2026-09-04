"""Key audit for AP CHEMISTRY 5.5 Collision Model.

One ``(anchor, claim)`` per item, in module order; the anchor must appear in the
KEYED choice and in no distractor. Six table items are recomputed from their own
stimulus.

WHAT THE KEYS REST ON
---------------------
EK 5.5.A.1  For an elementary reaction to successfully produce products,
            reactants must successfully collide to initiate bond-breaking and
            bond-making events.  (items 1, 8, 14, 18, 24, 27, 29, 30)
EK 5.5.A.2  In most reactions only a small fraction of collisions leads to a
            reaction; successful collisions have BOTH sufficient energy to
            overcome the activation energy requirements AND orientations that
            allow the bonds to rearrange.  (items 2, 3, 6, 7, 9, 10, 12, 16, 19,
            21, 22, 24, 27, 28, 30)
EK 5.5.A.3  The Maxwell-Boltzmann distribution curve describes the distribution
            of particle energies and gives a qualitative estimate of the
            fraction of collisions with sufficient energy and of how that
            fraction depends on temperature.  (items 4, 5, 11, 12, 13, 15, 20,
            23, 25, 26, 28)

Item 17 keys on learning objective 5.5.A itself, which names the frequency,
energy and orientation of particle collisions and nothing else.

NO CURVE ANYWHERE, AND NO NUMBER TAKEN FROM ONE. 5.5.A.3 calls its own estimate
QUALITATIVE, so the two items using the fraction table (5 and 20) ask only for a
DIRECTION and an order of magnitude, both of which the check below recomputes
from the tabulated fractions. No item computes a fraction from a temperature,
which would be an Arrhenius calculation and is excluded by the CED at 5.6.

THE ORIENTATION CLAIM IS NEVER ASSERTED ALONE. Where an item turns on
orientation (7, 21) the stem states that the energy condition was met, so the
key rests on 5.5.A.2's conjunction rather than on any claim about how often a
given orientation occurs, which the framework does not quantify.

NEGATIVE CONTROL: ``python3 verify_h5_5.py --selftest``.
"""
import sys

import h_chem_notation as hn
import h5_5 as M

TEMP = "Temperature (kelvins)"
FRAC = "Fraction of collisions with energy above the requirement"
NCOLL = "Collisions per second in the vessel"
SUCC = "Fraction of those collisions that lead to products"
LOW = "At 300 kelvins"
HIGH = "At 400 kelvins"


# ------------------------------------------------------------ table questions

def q5(t, item):
    temp = hn.cg.col(t, TEMP)
    frac = hn.cg.col(t, FRAC)
    assert temp == sorted(temp), "the temperatures should be listed in increasing order"
    assert frac == sorted(frac) and frac[0] < frac[-1], \
        f"the fraction does not grow with temperature: {frac}"
    assert max(frac) < 1, "no tabulated fraction may reach one"
    hn.keyed(item, "grows as the temperature rises")
    return (f"over {temp[0]:.0f} to {temp[-1]:.0f} kelvins the tabulated fraction rises "
            f"from {frac[0]} to {frac[-1]}, staying below one throughout")


def q6(t, item):
    rows = {r[0]: (r[1].strip().lower(), r[2].strip().lower(), r[3].strip().lower())
            for r in t["rows"]}
    for lab, (energy, orient, formed) in rows.items():
        both = energy.startswith("above") and orient.startswith("allows")
        assert formed == ("yes" if both else "no"), (
            f"{lab}: energy {energy!r} and orientation {orient!r} but outcome {formed!r}"
        )
    winners = [l for l, v in rows.items() if v[2] == "yes"]
    assert len(winners) == 1, f"collisions producing products: {winners}"
    hn.keyed(item, "energy requirement and the orientation requirement at the same time")
    return ("across all four tabulated collisions the outcome is exactly the conjunction "
            "of the two conditions, and only one collision meets both")


def q9(t, item):
    labs = hn.cg.labels(t)
    n = dict(zip(labs, hn.cg.col(t, NCOLL)))
    f = dict(zip(labs, hn.cg.col(t, SUCC)))
    pairs = [(a, b) for i, a in enumerate(labs) for b in labs[i + 1:]
             if f[a] == f[b] and n[a] != n[b]]
    assert pairs == [("Sample 1", "Sample 2")], f"pairs isolating collision frequency: {pairs}"
    hn.keyed(item, "same successful fraction but differ in collisions per second")
    return ("exactly one pair of samples holds the successful fraction fixed while the "
            "collision count differs, which is the only comparison that isolates frequency")


def q10(t, item):
    labs = hn.cg.labels(t)
    n = dict(zip(labs, hn.cg.col(t, NCOLL)))
    f = dict(zip(labs, hn.cg.col(t, SUCC)))
    pairs = [(a, b) for i, a in enumerate(labs) for b in labs[i + 1:]
             if n[a] == n[b] and f[a] != f[b]]
    assert pairs == [("Sample 1", "Sample 3")], f"pairs isolating the successful fraction: {pairs}"
    assert len(set(f.values())) > 1, "'the fraction is the same in all three' must be false"
    hn.keyed(item, "first and third samples")
    return ("exactly one pair holds the collision count fixed while the successful "
            "fraction differs, and the three fractions are not all equal")


def q12(t, item):
    rows = {r[0]: (r[1].strip().lower(), r[2].strip().lower()) for r in t["rows"]}
    differing = [k for k, (a, b) in rows.items() if a != b]
    same = [k for k, (a, b) in rows.items() if a == b]
    assert same == ["Total number of particles"], f"rows unchanged between the temperatures: {same}"
    assert len(differing) == 2, f"rows that differ: {differing}"
    high_e = [k for k in differing if "very high energy" in k.lower()]
    assert high_e, "no row reports the fraction of particles at very high energy"
    assert rows[high_e[0]] == ("smaller", "larger"), \
        f"the high-energy row reads {rows[high_e[0]]}"
    hn.keyed(item, "larger fraction of particles with very high energy")
    return ("of the three tabulated properties one is unchanged and two differ, and the "
            "one naming the high-energy fraction goes from smaller to larger")


def q20(t, item):
    frac = hn.cg.col(t, FRAC)
    ratio = max(frac) / min(frac)
    assert 100 <= ratio < 1000, f"the fraction changes by a factor of {ratio}, not a few hundred"
    assert ratio > 2 and ratio < 10000, "the two rejected magnitudes must both be wrong"
    hn.keyed(item, "grows by a factor of a few hundred")
    return (f"the largest tabulated fraction {max(frac)} over the smallest {min(frac)} is a "
            f"factor of {ratio:.0f}, which is a few hundred")


TABLE_CHECKS = {5: q5, 6: q6, 9: q9, 10: q10, 12: q12, 20: q20}

CLAIMS = [
 ("collide successfully so that bond-breaking and bond-making can begin",
  "EK 5.5.A.1, near verbatim: for an elementary reaction to successfully produce products, reactants must successfully collide to initiate bond-breaking and bond-making events."),
 ("Sufficient energy to overcome the activation energy requirement, and an orientation",
  "EK 5.5.A.2, near verbatim: successful collisions have BOTH sufficient energy to overcome the activation energy requirements AND orientations that allow the bonds to rearrange in the required manner."),
 ("Only a small fraction of them",
  "EK 5.5.A.2, near verbatim: in most reactions, only a small fraction of the collisions leads to a reaction, because both conditions have to be met at once."),
 ("distribution of particle energies in a sample",
  "EK 5.5.A.3, near verbatim: the Maxwell-Boltzmann distribution curve describes the distribution of particle energies."),
 ("grows as the temperature rises",
  "Recomputed in q5 above from the tabulated fractions. EK 5.5.A.3 makes how that fraction depends on temperature exactly what the distribution is used to estimate."),
 ("energy requirement and the orientation requirement at the same time",
  "Recomputed in q6 above: the tabulated outcome is the conjunction of the two conditions in all four rows, which is EK 5.5.A.2's requirement of BOTH."),
 ("oriented so that the bonds could not rearrange",
  "EK 5.5.A.2 makes energy and orientation two separate conditions that must both be met, so excess energy cannot repair an orientation that does not allow the required rearrangement."),
 ("make collisions between reactants more frequent",
  "EK 5.5.A.1 makes a collision necessary before an elementary reaction can produce products, so more particles per unit volume give more chances. Neither of EK 5.5.A.2's conditions is altered by crowding."),
 ("same successful fraction but differ in collisions per second",
  "Recomputed in q9 above. EK 5.5.A.1's collision count and EK 5.5.A.2's successful fraction are separate quantities, so isolating one means holding the other fixed."),
 ("first and third samples",
  "Recomputed in q10 above: exactly one tabulated pair holds the collision count fixed while the fraction of successful collisions differs."),
 ("larger fraction of the particles carries high energy",
  "EK 5.5.A.3 makes the fraction of collisions with sufficient energy grow with temperature, which is the distribution shifting toward higher energies."),
 ("larger fraction of particles with very high energy",
  "Recomputed in q12 above. EK 5.5.A.2 requires sufficient energy to overcome the activation energy requirement, and EK 5.5.A.3 makes the fraction meeting it the quantity the distribution estimates."),
 ("energies are distributed",
  "EK 5.5.A.3 states that the Maxwell-Boltzmann curve describes the DISTRIBUTION of particle energies, and a distribution places particles on both sides of its average."),
 ("initiates the bond-breaking and bond-making events",
  "EK 5.5.A.1 states that reactants must successfully collide to initiate bond-breaking and bond-making events, which is what makes a collision successful."),
 ("compares between conditions rather than yielding a numerical rate",
  "EK 5.5.A.3 describes the estimate obtained from the distribution as QUALITATIVE, covering the fraction with sufficient energy and how it depends on temperature."),
 ("do not depend on stirring",
  "EK 5.5.A.2 makes success depend on a collision's energy relative to the requirement and on the orientation of the particles, neither of which is set by whether the vessel is stirred."),
 ("mass of the products formed",
  "Learning objective 5.5.A names the frequency, energy and orientation of particle collisions. How much product forms is an outcome of the reaction rather than a property of a collision."),
 ("frequency with which reactant particles collide",
  "EK 5.5.A.1 makes collisions necessary before products can form, and compressing a gas puts more particles in each unit of volume. EK 5.5.A.2's conditions belong to an individual collision."),
 ("Both must be satisfied in the same collision",
  "EK 5.5.A.2 states that successful collisions have both sufficient energy AND orientations that allow the bonds to rearrange in the required manner."),
 ("grows by a factor of a few hundred",
  "Recomputed in q20 above from the tabulated fractions. EK 5.5.A.3 makes the temperature dependence of that fraction something the distribution is used to estimate qualitatively."),
 ("few of those orientations allow the bonds to rearrange",
  "EK 5.5.A.2 makes a suitable orientation one of the two conditions for success, and how readily a collision meets it is a property of the particles rather than of how often they meet."),
 ("overcome the activation energy requirement of the reaction",
  "EK 5.5.A.2 states that successful collisions have sufficient energy to overcome the activation energy requirements, so that requirement is the standard the collision's energy is compared against."),
 ("more frequent and more often energetic enough",
  "EK 5.5.A.3 makes the fraction with sufficient energy grow with temperature, and faster-moving particles meet more often, so the frequency named in the learning objective moves the same way."),
 ("collide many billions of times per second",
  "EK 5.5.A.1 makes collisions necessary but EK 5.5.A.2 makes only a small fraction of them successful, so a very large collision count alongside a slow reaction points at the two success conditions."),
 ("Warming the mixture while holding the amounts and the volume fixed",
  "EK 5.5.A.3 makes the fraction of collisions with sufficient energy depend on temperature, and warming is the only listed change that alters the distribution of particle energies rather than the crowding."),
 ("energies are distributed over a range",
  "EK 5.5.A.3 states that the Maxwell-Boltzmann distribution curve describes the distribution of particle energies, which is what makes a fraction with sufficient energy meaningful."),
 ("how often collisions occur multiplied by the fraction",
  "EK 5.5.A.1 makes a collision necessary and EK 5.5.A.2 makes only a small fraction of them successful, so both quantities bear on how quickly products appear."),
 ("neither the energy distribution nor the orientation requirement has changed",
  "EK 5.5.A.2 makes success depend on energy relative to the requirement and on orientation, and EK 5.5.A.3 ties the energy distribution to temperature, so compressing at fixed temperature changes only how often particles meet."),
 ("meet with enough energy and in a suitable orientation, and bond-breaking",
  "EK 5.5.A.1 has the collision INITIATE the bond-breaking and bond-making events, and EK 5.5.A.2 gives the two conditions the collision must meet for that to happen."),
 ("fraction reflects the energy and orientation each reaction requires",
  "EK 5.5.A.2 attaches both success conditions to the reaction itself, through its activation energy requirement and the rearrangement its bonds need, while EK 5.5.A.1 makes the collision count a matter of the particles meeting at all."),
]


def _wreck_outcome(mod, cl):
    """Module-specific control: make a one-condition collision succeed."""
    t = mod.QUESTIONS[5]["table"]
    mod.QUESTIONS[5]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], r[1], r[2], "Yes"] if r[0] == "C2" else list(r) for r in t["rows"]])


def _wreck_fraction(mod, cl):
    """Module-specific control: reverse the temperature dependence."""
    t = mod.QUESTIONS[4]["table"]
    mod.QUESTIONS[4]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], "0.00001"] if r[0] == "450" else list(r) for r in t["rows"]])


def _wreck_counts(mod, cl):
    """Module-specific control: destroy the pair that isolates frequency."""
    t = mod.QUESTIONS[8]["table"]
    mod.QUESTIONS[8]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], r[1], "0.000050"] if r[0] == "Sample 2" else list(r)
              for r in t["rows"]])


def _wreck_twotemps(mod, cl):
    """Module-specific control: flip the high-energy row the key names."""
    t = mod.QUESTIONS[11]["table"]
    mod.QUESTIONS[11]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], "Larger", "Smaller"] if "very high energy" in r[0] else list(r)
              for r in t["rows"]])


if __name__ == "__main__" and "--selftest" in sys.argv:
    hn.selftest(M, CLAIMS, TABLE_CHECKS,
                extra=[("a collision outcome corrupted", _wreck_outcome),
                       ("the temperature dependence reversed", _wreck_fraction),
                       ("the frequency-isolating pair destroyed", _wreck_counts),
                       ("the high-energy row flipped", _wreck_twotemps)])

hn.audit(M, CLAIMS, TABLE_CHECKS)
