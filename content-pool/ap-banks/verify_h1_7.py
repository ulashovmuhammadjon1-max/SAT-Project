r"""Key audit for AP CHEMISTRY 1.7 Periodic Trends.

One (anchor, claim) per item, in module order. ``anchor`` must appear in the
KEYED choice and in no distractor, since the exporter reshuffles choices.

WHAT IS RECOMPUTED, AND THE ONE PLACE IT MATTERS MOST. Every trend a key
asserts is recomputed from the item's own table: monotonic decrease across the
second row for radius, monotonic increase down the first column, monotonic
decrease down the halogen column for electronegativity, and so on.

The item that earns the machinery is the period 3 ionization energy table. It
is printed COMPLETE, dips and all, so two separate things have to be checked
rather than assumed:

  * item 7 keys "rises overall, though not at every step" -- so the check
    confirms BOTH that the last value exceeds the first by a wide margin AND
    that at least one step really does go down. Either half alone would let a
    wrong key through.
  * item 8 keys the subshell-boundary explanation of those dips -- so the check
    locates the falling steps and confirms they are interior to the row, since
    the rejected "a new shell begins" account would require them at a row
    boundary.

Every table used for an EXTRAPOLATION item (9, 21, 27) is separately checked to
be strictly monotonic before an estimate is keyed against it. Estimating across
a non-monotonic trend is exactly the error the complete period 3 table exists
to warn about, and a checker that let it through would be teaching it.

WHAT THE KEYS REST ON
---------------------
Items 1, 8, 19, 29 and 30 rest on EK 1.7.A.1: the organization of the table is
based on patterns of recurring properties, explained by patterns of
ground-state electron configurations and the presence of completely or
partially filled shells and subshells.

Items 2 to 7 and 10 to 26 and 28 rest on EK 1.7.A.2: trends in ionization
energy, atomic and ionic radii, electron affinity and electronegativity are
predicted by position in the table and understood qualitatively using Coulomb's
law, the shell model, and shielding and effective nuclear charge. Where the
Coulombic step is doing the work the claim also cites EK 1.5.A.2, and where a
key turns on neutrons being uncharged it cites EK 1.5.A.1.

Items 9, 21 and 27 rest on EK 1.7.A.3: periodicity is useful to predict or
estimate values of properties in the absence of data.

THE EXCLUSION IS KEPT. No item writes the configuration of an element that is
an exception to the Aufbau principle; no configuration is written out at all in
this module.

DATA ITEMS: 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 20, 21, 27 and 28 carry
tables; all sixteen are recomputed below.

NEGATIVE CONTROL: ``python3 verify_h1_7.py --selftest``.
"""
import sys

import cg_check as cg
import chem_notation


def _monotonic(vals, direction):
    if direction == "down":
        return all(vals[i] > vals[i + 1] for i in range(len(vals) - 1))
    return all(vals[i] < vals[i + 1] for i in range(len(vals) - 1))


def _trend(table, header, direction, where):
    vals = cg.col(table, header)
    assert _monotonic(vals, direction), \
        f"{where}: {vals} is not strictly {direction} in table order"
    return vals


RAD = "Atomic radius (picometers)"
IE = "First ionization energy (kilojoules per mole)"
EN = "Electronegativity"


def q3(table, item):
    vals = _trend(table, RAD, "down", "q3 second-row radii")
    return f"the tabulated radii {vals} fall at every step from left to right"


def q5(table, item):
    vals = _trend(table, RAD, "up", "q5 first-column radii")
    return f"the tabulated radii {vals} rise at every step from top to bottom"


def q6(table, item):
    vals = _trend(table, IE, "down", "q6 first-column ionization energies")
    return f"the tabulated ionization energies {vals} fall at every step down the column"


def q7(table, item):
    labs, vals = cg.labels(table), cg.col(table, IE)
    top = max(zip(vals, labs))[1]
    assert top == "Argon", f"the largest tabulated ionization energy belongs to {top}"
    assert vals[-1] > vals[0] * 2, \
        f"the row does not rise decisively overall: {vals[0]} to {vals[-1]}"
    falls = [(labs[i], labs[i + 1]) for i in range(len(vals) - 1) if vals[i + 1] < vals[i]]
    assert falls, (
        "no step falls, so the 'rises at every single step' option would be correct too "
        "and the item would have two answers")
    return (f"the largest value is {top}'s and the row rises from {vals[0]} to {vals[-1]} "
            f"overall, but the steps {falls} go down, so 'every single step' is false")


def q8(table, item):
    labs, vals = cg.labels(table), cg.col(table, IE)
    falls = [i for i in range(len(vals) - 1) if vals[i + 1] < vals[i]]
    assert falls, "there are no departures for the item to explain"
    # The rejected "a new shell begins" account needs a break at a row boundary.
    assert all(0 < i < len(vals) - 2 for i in falls), \
        f"a falling step sits at the edge of the row ({[labs[i] for i in falls]})"
    assert len(falls) == 2, f"the stem says two steps fall; the data show {len(falls)}"
    return (f"the two falling steps are at {[labs[i] + ' to ' + labs[i + 1] for i in falls]}, "
            "both interior to the row, so a new shell beginning cannot account for them")


def q9(table, item):
    vals = _trend(table, IE, "down", "q9 the gapped column")
    labs = cg.labels(table)
    assert "Potassium" not in labs, "potassium must be MISSING for the item to be an estimate"
    na, rb = cg.cell(table, "Sodium", IE), cg.cell(table, "Rubidium", IE)
    assert rb < 420 < na, f"the keyed estimate 420 does not lie between {rb} and {na}"
    for wrong in (560, 350, 900):
        assert not (rb < wrong < na), f"the rejected estimate {wrong} also lies in the interval"
    return (f"the column falls {vals}, so a member between sodium ({na}) and rubidium "
            f"({rb}) must lie between them; only the keyed estimate does")


def q10(table, item):
    r = dict(zip(cg.labels(table), cg.col(table, "Radius (picometers)")))
    e = dict(zip(cg.labels(table), cg.col(table, "Electrons")))
    assert e["Sodium ion"] < e["Sodium atom"] and r["Sodium ion"] < r["Sodium atom"], \
        "the species with fewer electrons is not the smaller one"
    assert e["Chloride ion"] > e["Chlorine atom"] and r["Chloride ion"] > r["Chlorine atom"], \
        "the species with more electrons is not the larger one"
    return (f"losing an electron takes sodium from {r['Sodium atom']} to {r['Sodium ion']} "
            f"picometers while gaining one takes chlorine from {r['Chlorine atom']} to "
            f"{r['Chloride ion']}, so the shrinking species is the one that LOST an electron")


def q11(table, item):
    r = dict(zip(cg.labels(table), cg.col(table, "Radius (picometers)")))
    assert r["Chloride ion"] > r["Chlorine atom"], "the chloride ion is not the larger"
    assert r["Chloride ion"] / r["Chlorine atom"] > 1.5, \
        "the increase is not large enough for the stem's 'so much larger'"
    return (f"the chloride ion at {r['Chloride ion']} picometers is "
            f"{r['Chloride ion'] / r['Chlorine atom']:.1f} times the atom's {r['Chlorine atom']}")


def q12(table, item):
    e = cg.col(table, "Electrons")
    p = cg.col(table, "Protons in the nucleus")
    r = cg.col(table, "Radius (picometers)")
    assert len(set(e)) == 1, f"the four species do not share an electron count: {e}"
    pairs = sorted(zip(p, r))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"the radius does not fall as the proton count rises: {pairs}"
    return (f"all four species carry {e[0]:.0f} electrons, and sorted by proton count the "
            f"radii are {[y for _, y in pairs]}, strictly falling")


def q14(table, item):
    labs = cg.labels(table)
    p = dict(zip(labs, cg.col(table, "Protons in the nucleus")))
    core = dict(zip(labs, cg.col(table, "Core electrons")))
    assert len(set(core.values())) == 1, (
        f"the core electron counts {core} are not all equal, so the item's reasoning "
        "about comparable shielding does not hold")
    top = max(p, key=p.get)
    assert top == "Fluorine", f"the largest proton count belongs to {top}"
    return (f"every row has {list(core.values())[0]:.0f} core electrons, so shielding is "
            f"comparable, and the proton counts {p} put fluorine highest")


def q15(table, item):
    vals = _trend(table, EN, "up", "q15 third-row electronegativities")
    return f"the tabulated electronegativities {vals} rise at every step from left to right"


def q16(table, item):
    vals = _trend(table, EN, "down", "q16 seventeenth-column electronegativities")
    return f"the tabulated electronegativities {vals} fall at every step down the column"


def q20(table, item):
    vals = _trend(table, RAD, "up", "q20 first-column radii")
    assert vals[-1] == max(vals), "the last tabulated element must be the largest"
    return (f"the column rises {vals}, so an element placed below the last should exceed "
            f"{vals[-1]}, which no other option allows")


def q21(table, item):
    vals = _trend(table, RAD, "down", "q21 second-row radii")
    assert vals[0] > vals[-1], "the student's claimed direction must be refuted by the data"
    return f"the tabulated radii {vals} fall across the row, refuting the claim that they grow"


def q27(table, item):
    vals = _trend(table, EN, "down", "q27 seventeenth-column electronegativities")
    lowest = vals[-1]
    assert lowest == min(vals), "the last tabulated value must be the smallest"
    for wrong in (4.5, 2.9):
        assert wrong > lowest, f"the rejected estimate {wrong} is not above the trend's last value"
    return (f"the column falls {vals}, so a member below the last must sit below {lowest}; "
            "every rejected estimate sits at or above it")


def q28(table, item):
    labs = cg.labels(table)
    p = dict(zip(labs, cg.col(table, "Protons in the nucleus")))
    e = dict(zip(labs, cg.col(table, "Electrons")))
    r = dict(zip(labs, cg.col(table, "Radius (picometers)")))
    assert e["Sodium ion"] == e["Magnesium ion"], "the two ions do not share an electron count"
    assert p["Magnesium ion"] == p["Sodium ion"] + 1, "the proton counts do not differ by one"
    assert r["Magnesium ion"] < r["Sodium ion"], "the magnesium ion is not the smaller"
    return (f"both ions carry {e['Sodium ion']:.0f} electrons and the proton counts are "
            f"{p['Sodium ion']:.0f} against {p['Magnesium ion']:.0f}, with radii "
            f"{r['Sodium ion']} and {r['Magnesium ion']} picometers")


CLAIMS = [
 ("patterns of recurring properties",
  "EK 1.7.A.1, near verbatim: the organization of the periodic table is based on patterns of recurring properties of the elements, which are explained by patterns of ground-state electron configurations and the presence of completely or partially filled shells and subshells of electrons in atoms."),
 ("Ionization energy, atomic and ionic radii, electron affinity",
  "EK 1.7.A.2 lists exactly these four properties. The rejected lists name real properties, but the framework does not attach their periodicity to this learning objective, so a key built on them would be inventing content."),
 ("decreases steadily from left to right",
  "Recomputed in q3 above: every tabulated radius is smaller than the one before it as the row is read left to right. EK 1.7.A.2 makes atomic radius one of the properties predicted by position."),
 ("added electrons enter the same shell",
  "EK 1.7.A.2 has the trends understood using Coulomb's law, the shell model, and shielding and effective nuclear charge. Across a row the screening core is unchanged while protons accumulate, so the effective nuclear charge on the valence shell rises and EK 1.5.A.2 makes the attraction stronger. Neutrons are uncharged under EK 1.5.A.1, which kills the neutron option outright."),
 ("shell farther from the nucleus, shielded by more core electrons",
  "Recomputed in q5 above: the tabulated radii rise down the column. EK 1.7.A.2's shell model and shielding supply the reason, and EK 1.5.A.2 makes the greater distance a weaker hold. Proton count rises rather than falls down a column, which refutes one rejected option on its own terms."),
 ("falls down the column, because the valence electron lies farther",
  "Recomputed in q6 above: every tabulated ionization energy is smaller than the one above it. EK 1.7.A.2 lists ionization energy among the periodic properties and explains it through distance and shielding; each element in the column has one valence electron, which is why that cannot be the variable."),
 ("rise overall from left to right although not at every single step",
  "Recomputed in q7 above, and this is the item the complete table exists for. The check confirms BOTH halves of the key independently: the last value is more than twice the first, and at least one step really does fall, so the 'every single step' option is false on the same numbers."),
 ("completely or partially filled",
  "Recomputed in q8 above: the two falling steps are located and confirmed to be interior to the row, which is what rules out the 'a new shell begins' account, since a new shell begins only at a row boundary. EK 1.7.A.1 attributes recurring properties to completely or partially filled shells AND SUBSHELLS, which is the framework's own basis for a break inside a row."),
 ("between the values for sodium and rubidium",
  "Recomputed in q9 above. EK 1.7.A.3 licenses an estimate in the absence of data, and the check first confirms the column is strictly monotonic -- estimating across a non-monotonic trend is the error the period 3 table warns about -- then confirms that only the keyed value falls inside the bracketing interval."),
 ("losing an electron leaves the same nuclear charge acting on fewer",
  "Recomputed in q10 above from the tabulated electron counts and radii: the species that lost an electron shrank and the one that gained an electron grew. EK 1.7.A.2 lists ionic radius among the periodic properties and EK 1.5.A.2 supplies the mechanism."),
 ("repulsion among the electrons while the nuclear charge stays the same",
  "Recomputed in q11 above: the anion's radius is more than one and a half times the atom's at unchanged nuclear charge. Adding an electron to a partly filled subshell opens no new shell, so the rejected new-shell account is not available."),
 ("radius falls as the number of protons rises, because a larger nuclear charge",
  "Recomputed in q12 above: all four species carry the same electron count, so the electron count cannot explain the ordering, and the radius falls strictly as the proton count rises. EK 1.5.A.2 makes the larger positive charge the stronger pull."),
 ("once the screening effect of the other electrons is taken into account",
  "EK 1.7.A.2 names shielding and effective nuclear charge as the concepts through which the trends are understood, and shielding is exactly what separates the effective charge from the bare proton count. Neutrons carry no charge under EK 1.5.A.1."),
 ("Fluorine",
  "Recomputed in q14 above. The check first confirms every row has the SAME core electron count, which is what makes shielding comparable and the comparison legitimate at all, and then that the keyed element has the largest proton count."),
 ("increases from left to right",
  "Recomputed in q15 above: every tabulated electronegativity exceeds the one to its left. EK 1.7.A.2 lists electronegativity among the properties predicted by position in the table."),
 ("held farther from the nucleus and are more shielded",
  "Recomputed in q16 above: the tabulated values fall at every step down the column. EK 1.7.A.2 explains that through distance and shielding, and every member of the column has the same valence count, which is why that cannot be the cause."),
 ("larger effective nuclear charge at a comparable distance",
  "EK 1.7.A.2 makes ionization energy predictable from position and understood through effective nuclear charge and the shell model: across a row the valence shell is unchanged while protons accumulate, so by EK 1.5.A.2 the valence electron is held more firmly toward the right."),
 ("same number of valence electrons",
  "EK 1.7.A.1 traces the table's organization to patterns of recurring ground-state configurations, and it is the outer part of that pattern that repeats down a column. Proton and electron totals differ between members of a column, so neither can be the shared feature."),
 ("one electron short of a filled subshell",
  "EK 1.7.A.2 lists electron affinity among the properties predicted by position and understood through effective nuclear charge, and EK 1.7.A.1 makes completely or partially filled subshells part of the explanation of recurring properties. An atom that both feels a large effective nuclear charge and can complete a subshell gains the most from an added electron; one whose subshells are already complete has nowhere to put it."),
 ("larger than that of every element listed",
  "Recomputed in q20 above. EK 1.7.A.3 permits an estimate in the absence of data, and the check confirms the column is strictly monotonic and that the last tabulated element is its largest, so an element placed below it should continue the rise."),
 ("tabulated radii shrink across the row",
  "Recomputed in q21 above: the tabulated values fall from left to right, so the student's prediction is refuted by the data rather than by an appeal to authority. EK 1.7.A.2 supplies the correct reasoning -- the added electrons enter the same shell while the effective nuclear charge grows."),
 ("core that screens them stays the same",
  "EK 1.7.A.2 has these trends understood through shielding and effective nuclear charge. Along a row the screening core is unchanged so each added proton is felt nearly in full; down a column the added protons arrive with a larger core and a valence shell that has moved outward, so the net change is much smaller."),
 ("element on the right is smaller",
  "EK 1.7.A.2 makes atomic radius predictable from position, and the radius shrinks left to right along a row because the effective nuclear charge rises on an unchanged valence shell. Ordering by INCREASING radius therefore runs from right to left, which is what the keyed option says."),
 ("lower in a column has the smaller first ionization energy",
  "EK 1.7.A.2 has ionization energy predicted by position and understood through Coulomb's law, the shell model and shielding. Down a column the valence electron sits in a shell farther out and better screened, so by EK 1.5.A.2 it is held less firmly despite the larger proton count."),
 ("estimating values of its properties in the absence of data",
  "EK 1.7.A.3, near verbatim: the periodicity is useful to predict or estimate values of properties in the absence of data. An estimate is not an exact value, and isotopic composition is what a mass spectrum supplies under EK 1.2.A.1 rather than what periodicity supplies."),
 ("smaller atomic radius and a larger first ionization energy",
  "EK 1.7.A.2 makes both properties expressions of the same attraction between the nucleus and the valence electrons, and EK 1.5.A.2 makes a larger effective charge a stronger pull. A stronger pull draws the shell in and makes an electron harder to remove, so the two properties must move in opposite directions."),
 ("Below 2.5",
  "Recomputed in q27 above. The check confirms the column is strictly monotonic before any estimate is keyed to it, confirms the last tabulated value is the smallest, and confirms every rejected estimate sits at or above that value rather than continuing the fall."),
 ("one more proton, so the same ten electrons",
  "Recomputed in q28 above: the two ions carry identical electron counts and proton counts differing by one, with the higher-proton ion the smaller. EK 1.5.A.2 makes the larger positive charge the stronger attraction, and EK 1.5.A.1 rules the uncharged neutron out of the explanation."),
 ("drops sharply at the start of the next",
  "EK 1.7.A.1 bases the table on patterns of RECURRING properties explained by the repeating pattern of ground-state configurations. A quantity that resets at the start of each row and then repeats its behaviour is what recurrence looks like; a quantity rising monotonically with atomic number exhibits no recurrence at all."),
 ("same number of valence electrons, but the lower element's are in a shell farther",
  "EK 1.7.A.1 traces the columns to repeating configurations, which fixes the valence count down a column, while each successive member occupies one more shell. EK 1.7.A.2 then uses that greater distance, with the extra shielding it brings, to explain the property trends down the column."),
]

TABLE_CHECKS = {3: q3, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 12: q12,
                14: q14, 15: q15, 16: q16, 20: q20, 21: q21, 27: q27, 28: q28}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("h1_7_mutant")
        mod.TOPIC = h1_7.TOPIC
        mod.QUESTIONS = copy.deepcopy(h1_7.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:95]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[2]["ans"] = 1

    def break_anchor(mod, claims):
        claims[13] = ("no such phrase anywhere in the choice", claims[13][1])

    def reverse_the_radius_trend(mod, claims):
        mod.QUESTIONS[2]["table"] = dict(
            headers=h1_7._T_RAD_PERIOD["headers"],
            rows=list(reversed(h1_7._T_RAD_PERIOD["rows"])))

    def smooth_the_period3_dips(mod, claims):
        # Remove the two falling steps: item 7's key then has a rival, since
        # "rises at every single step" becomes true as well.
        mod.QUESTIONS[6]["table"] = dict(
            headers=h1_7._T_IE_PERIOD3["headers"],
            rows=[["Sodium", "496"], ["Magnesium", "738"], ["Aluminum", "760"],
                  ["Silicon", "786"], ["Phosphorus", "1012"], ["Sulfur", "1100"],
                  ["Chlorine", "1251"], ["Argon", "1521"]])

    def move_a_dip_to_the_row_edge(mod, claims):
        mod.QUESTIONS[7]["table"] = dict(
            headers=h1_7._T_IE_PERIOD3["headers"],
            rows=[["Sodium", "496"], ["Magnesium", "400"], ["Aluminum", "578"],
                  ["Silicon", "786"], ["Phosphorus", "1012"], ["Sulfur", "1000"],
                  ["Chlorine", "1251"], ["Argon", "1521"]])

    def break_monotonicity_before_an_estimate(mod, claims):
        # An extrapolation item must not be keyed against a trend that wanders.
        mod.QUESTIONS[26]["table"] = dict(
            headers=h1_7._T_EN_GROUP["headers"],
            rows=[["Fluorine", "4.0"], ["Chlorine", "3.0"], ["Bromine", "3.4"],
                  ["Iodine", "2.5"]])

    def give_the_gap_away(mod, claims):
        mod.QUESTIONS[8]["table"] = dict(
            headers=h1_7._T_IE_GAP["headers"],
            rows=[["Lithium", "520"], ["Sodium", "496"], ["Potassium", "419"],
                  ["Rubidium", "403"], ["Cesium", "376"]])

    def unequal_cores_break_the_zeff_argument(mod, claims):
        mod.QUESTIONS[13]["table"] = dict(
            headers=h1_7._T_ZEFF["headers"],
            rows=[["Lithium", "3", "2", "1"], ["Carbon", "6", "2", "4"],
                  ["Oxygen", "8", "4", "4"], ["Fluorine", "9", "2", "7"]])

    def break_the_isoelectronic_premise(mod, claims):
        mod.QUESTIONS[11]["table"] = dict(
            headers=h1_7._T_ISO["headers"],
            rows=[["Oxide ion", "8", "10", "140"], ["Fluoride ion", "9", "10", "133"],
                  ["Sodium ion", "11", "9", "98"], ["Magnesium ion", "12", "10", "72"]])

    def forget_table_check(mod, claims):
        mod.QUESTIONS[0]["table"] = h1_7._T_RAD_PERIOD

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[17]["choices"][3] = mod.QUESTIONS[17]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[22]["why"] = "It is periodic."

    def letter_reference(mod, claims):
        mod.QUESTIONS[1]["why"] = ("Choice C is excluded because the framework says so, "
                                   "and the remaining reasoning follows from that.")

    def notation_slips_in(mod, claims):
        mod.QUESTIONS[9]["choices"][2] = "A positive ion such as Na^+ formed by loss"
        chem_notation.style(mod)

    print("negative controls:")
    must_fail("an ion charge written as a bare superscript", notation_slips_in)
    must_fail("key moved off its anchor", move_key)
    must_fail("anchor no longer present in the keyed choice", break_anchor)
    must_fail("the radius trend reversed, refuting the keyed direction",
              reverse_the_radius_trend)
    must_fail("the period 3 dips smoothed away, so 'every single step' becomes true too",
              smooth_the_period3_dips)
    must_fail("a dip moved to the edge of the row, where a new shell WOULD explain it",
              move_a_dip_to_the_row_edge)
    must_fail("an extrapolation keyed against a trend that is no longer monotonic",
              break_monotonicity_before_an_estimate)
    must_fail("the element to be estimated added back into its own table",
              give_the_gap_away)
    must_fail("unequal cores, so the effective-nuclear-charge comparison no longer holds",
              unequal_cores_break_the_zeff_argument)
    must_fail("the isoelectronic premise broken by an unequal electron count",
              break_the_isoelectronic_premise)
    must_fail("a table added with no recompute behind it", forget_table_check)
    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a rationale reduced below the minimum", thin_why)
    must_fail("a rationale naming an option by letter", letter_reference)
    print("all negative controls raised as required.")


import h1_7  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

chem_notation.style(h1_7)
cg.check(h1_7, CLAIMS, table_checks=TABLE_CHECKS)
