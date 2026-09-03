r"""Key audit for AP CHEMISTRY 1.6 Photoelectron Spectroscopy.

One (anchor, claim) per item, in module order. ``anchor`` must appear in the
KEYED choice and in no distractor, since the exporter reshuffles choices.

THE GATE THAT MATTERS HERE. Every item that keys a configuration is checked by
DERIVING that configuration from the item's own tabulated spectrum: the peaks
are sorted from the highest binding energy downward, assigned to subshells in
the Aufbau order EK 1.5.A.3 names, and given the electron counts EK 1.6.A.1
reads off the peak heights. ``chem_config.from_peak_heights`` refuses any
height that exceeds a subshell's capacity, so a spectrum describing no possible
atom fails before a key can be built on it. Nothing here is compared against a
remembered configuration.

The remaining table checks recompute the electron totals, the height ratios and
the orderings of binding energy each key asserts, from the item's own table
alone. SCIENCE_BRIEF.md requires that of quantitative Chemistry, and a
"spectrum" that is really a table is quantitative all the way down.

WHAT THE KEYS REST ON
---------------------
Every key in this module rests on EK 1.6.A.1: the position of each peak in the
PES spectrum is related to the energy required to remove an electron from the
corresponding subshell, and the relative height of each peak is (ideally)
proportional to the number of electrons in that subshell. The two halves of
that sentence are independent readings of the same picture, and a large share
of the items exist to keep them apart -- items 5, 16, 23 and 25 in particular,
where confusing height with position is the whole of the distractor.

Where an item reaches past that statement it chains:
  * EK 1.5.A.3 for the Aufbau order and subshell capacities (items 3, 7, 10,
    11, 14, 17, 19, 29);
  * EK 1.5.A.4 and EK 1.5.A.2 for why a shorter distance and a larger effective
    nuclear charge mean a larger removal energy (items 5, 8, 12, 20, 30) --
    this is LO 1.6.A's second clause, the interactions between the electrons
    and the nucleus;
  * EK 1.5.A.1 for a neutral atom having as many electrons as protons (items
    15, 22).
Items 14 and 29 are the suggested skill 4.B items: is the model consistent with
the data.

NO ITEM RECALLS A MEASURED VALUE. Spectra belong to unnamed elements and every
key follows from the ORDER of the tabulated energies and the RATIOS of the
tabulated heights.

DATA ITEMS: 3, 4, 5, 6, 8, 9, 11, 12, 14, 15, 16, 17, 21, 25 and 27 carry
tables; all fifteen are recomputed below.

NEGATIVE CONTROL: ``python3 verify_h1_6.py --selftest``.
"""
import sys

import cg_check as cg
import chem_config as cc
import chem_notation

E = "Binding energy (megajoules per mole)"
H = "Relative height"


def _peaks(table):
    """(binding energy, height) pairs, ordered from the HIGHEST energy down."""
    pairs = sorted(zip(cg.col(table, E), cg.col(table, H)), reverse=True)
    energies = [e for e, _ in pairs]
    assert len(set(energies)) == len(energies), f"two peaks share a binding energy: {energies}"
    return pairs


def _derived(table, where):
    return cc.from_peak_heights([h for _, h in _peaks(table)], where)


def _keyed_config(item):
    return cc.parse(item["choices"][item["ans"]])


def _config_item(table, item, where):
    """The key must be exactly the configuration the spectrum implies."""
    want = _derived(table, where)
    got = _keyed_config(item)
    assert got == want, f"{where}: the spectrum implies {want}, but the key says {got}"
    # ...and no distractor may also match, or the item has two answers.
    for i, ch in enumerate(item["choices"]):
        if i != item["ans"] and cc.parse(ch) == want:
            raise AssertionError(f"{where}: distractor {i} also matches the spectrum")
    return (f"peaks ordered by descending binding energy give heights "
            f"{[h for _, h in _peaks(table)]}, which in Aufbau order is {want}")


def q3(table, item):
    return _config_item(table, item, "q3 element X")


def q4(table, item):
    n = sum(h for _, h in _peaks(table))
    assert abs(n - 11) < 1e-9, f"the tabulated heights total {n}, not eleven"
    assert len(table["rows"]) == 4, "the peak count should differ from the electron total"
    return f"the four tabulated heights sum to {n:.0f} electrons, while there are only 4 peaks"


def q5(table, item):
    pairs = _peaks(table)
    top_energy = pairs[0]
    tallest = max(pairs, key=lambda p: p[1])
    assert top_energy != tallest, (
        "the highest-energy peak and the tallest peak must be different peaks, or the "
        "'tallest peak, whichever one that is' distractor would be correct too")
    labs = cg.labels(table)
    order = [lab for _, lab in sorted(zip(cg.col(table, E), labs), reverse=True)]
    assert order[0] == "Peak 1", f"the highest-energy peak is {order[0]}"
    return (f"binding energies rank the peaks {order}; the highest-energy peak has height "
            f"{top_energy[1]:.0f} while the tallest has height {tallest[1]:.0f}")


def q6(table, item):
    pairs = _peaks(table)
    outermost = pairs[-1]
    assert abs(outermost[1] - 4) < 1e-9, f"the lowest-energy peak has height {outermost[1]}"
    assert abs(pairs[0][1] - 2) < 1e-9, "the highest-energy peak's height must be a distractor"
    assert outermost[1] != pairs[0][1], "reading the wrong end of the table must give a different number"
    return (f"the lowest binding energy in the table is {outermost[0]} with height "
            f"{outermost[1]:.0f}, against {pairs[0][1]:.0f} at the highest energy")


def q8(table, item):
    en = cg.col(table, "Binding energy of the highest-energy peak (megajoules per mole)")
    ht = cg.col(table, "Height of that peak")
    assert all(en[i] < en[i + 1] for i in range(len(en) - 1)), \
        f"the binding energies are not increasing down the table: {en}"
    assert len(set(ht)) == 1, (
        "every height must be equal, or the 'more innermost electrons' explanation could "
        "not be ruled out from the data")
    return (f"the innermost binding energies rise {en} while every height stays at "
            f"{ht[0]:.0f}, so the change cannot be a change in electron count")


def q9(table, item):
    pairs = _peaks(table)
    s2, p2 = pairs[1][1], pairs[2][1]
    assert abs(p2 / s2 - 3.0) < 1e-9, f"the p-to-s height ratio recomputes to {p2 / s2}"
    return f"the two second-shell heights are {s2:.0f} and {p2:.0f}, a ratio of {p2 / s2:.0f} to 1"


def q11(table, item):
    return _config_item(table, item, "q11 element W")


def q12(table, item):
    pairs = _peaks(table)
    other = [(84.0, 2.0), (4.68, 2.0), (2.08, 6.0)]  # the first spectrum, quoted in the stem
    assert [h for _, h in pairs] == [h for _, h in other], \
        f"the two height patterns differ: {[h for _, h in pairs]} against {[h for _, h in other]}"
    assert all(a[0] > b[0] for a, b in zip(pairs, other)), \
        f"not every binding energy is larger: {pairs} against {other}"
    assert len(pairs) == len(other), "'an additional subshell' must be false"
    return (f"both spectra carry heights {[int(h) for _, h in pairs]}, so the electron count is "
            f"unchanged, while every binding energy rises: {[e for e, _ in pairs]} against "
            f"{[e for e, _ in other]}")


def q14(table, item):
    derived = _derived(table, "q14 the tabulated spectrum")
    claimed = [("1s", 2), ("2s", 2), ("2p", 6)]
    assert derived != claimed, "the spectrum matches the student's configuration after all"
    assert len(derived) == len(claimed), (
        "the peak count must MATCH the claimed configuration, or the 'only two subshells' "
        "distractor would be the right objection instead")
    mismatch = [i for i, (a, b) in enumerate(zip(derived, claimed)) if a != b]
    assert mismatch == [2], f"the disagreement is at subshell(s) {mismatch}, not only the third"
    assert derived[2][1] == 3, f"the lowest-energy peak has height {derived[2][1]}, not three"
    return (f"the spectrum implies {derived} against the claimed {claimed}: the same three "
            "subshells, disagreeing only in the electron count of the outermost")


def q15(table, item):
    n = sum(h for _, h in _peaks(table))
    assert abs(n - 6) < 1e-9, f"the heights total {n}, not six"
    assert len(table["rows"]) == 3, "the peak count must differ from the electron total"
    return f"the three tabulated heights total {n:.0f} electrons, so a neutral atom has {n:.0f} protons"


def q16(table, item):
    pairs = _peaks(table)
    lowest, highest = pairs[-1], pairs[0]
    assert abs(lowest[1] - 1) < 1e-9, f"the lowest-energy peak has height {lowest[1]}"
    tallest = max(pairs, key=lambda p: p[1])
    assert tallest != lowest and tallest != highest, (
        "the tallest peak must be neither the lowest nor the highest in energy, so "
        "confusing height with position lands on a distractor")
    return (f"the smallest binding energy is {lowest[0]} with height {lowest[1]:.0f}, while the "
            f"tallest peak sits at {tallest[0]} with height {tallest[1]:.0f}")


def q17(table, item):
    return _config_item(table, item, "q17 element U")


def q21(table, item):
    pairs = _peaks(table)
    outer = pairs[1][1] + pairs[2][1]
    assert abs(outer - 8) < 1e-9, f"the outer shell recomputes to {outer} electrons"
    assert abs(sum(h for _, h in pairs) - 10) < 1e-9, "the total should be ten, a rejected value"
    assert abs(pairs[0][1] - 2) < 1e-9, "the innermost height should be another rejected value"
    return (f"the two lowest binding energies carry heights {pairs[1][1]:.0f} and "
            f"{pairs[2][1]:.0f}, so the outer shell holds {outer:.0f} of the {int(sum(h for _, h in pairs))} electrons")


def q25(table, item):
    pairs = _peaks(table)
    tallest = max(pairs, key=lambda p: p[1])
    rank = [e for e, _ in pairs].index(tallest[0]) + 1
    assert rank == 3, f"the tallest peak sits at rank {rank} by binding energy, not third"
    assert abs(pairs[0][1] - 2) < 1e-9, f"the innermost peak has height {pairs[0][1]}, not two"
    assert tallest[0] != pairs[0][0], "the claim under test would be TRUE on this spectrum"
    return (f"the tallest peak (height {tallest[1]:.0f}) sits at the third-largest binding energy, "
            f"while the innermost peak has height {pairs[0][1]:.0f}")


def q27(table, item):
    pairs = _peaks(table)
    other = [(84.0, 2.0), (4.68, 2.0), (2.08, 6.0)]  # element Z, quoted in the stem
    assert all(b[0] > a[0] for a, b in zip(pairs, other)), \
        f"element Z does not hold every subshell more tightly: {pairs} against {other}"
    assert other[-1][1] > pairs[-1][1], \
        f"element Z's outermost height {other[-1][1]} does not exceed {pairs[-1][1]}"
    return (f"element Z's binding energies {[e for e, _ in other]} exceed element Y's "
            f"{[e for e, _ in pairs]} peak for peak, and its outermost height {int(other[-1][1])} "
            f"exceeds {int(pairs[-1][1])}")


CLAIMS = [
 ("energy required to remove an electron",
  "EK 1.6.A.1, near verbatim: the position of each peak in the PES spectrum is related to the energy required to remove an electron from the corresponding subshell. The framework attaches the electron count to peak HEIGHT instead, which is the confusion every rejected option here rests on."),
 ("number of electrons in the subshell",
  "EK 1.6.A.1, near verbatim: the relative height of each peak is (ideally) proportional to the number of electrons in that subshell. Removal energy is carried by peak position, and nothing in the framework connects a peak to the nucleus's neutron count."),
 (r"1s^2\,2s^2\,2p^6\,3s^1",
  "DERIVED in q3 above from the item's own table: the peaks are ordered from the highest binding energy down, assigned to subshells in the Aufbau order of EK 1.5.A.3, and given the electron counts EK 1.6.A.1 reads off the heights. The check also confirms no distractor matches the same spectrum."),
 ("Eleven electrons",
  "Recomputed in q4 above as the sum of the tabulated heights, which EK 1.6.A.1 makes the electron counts of the individual subshells. The check confirms the number of peaks is a different number, so counting peaks instead lands on a rejected option."),
 ("Peak 1",
  "Recomputed in q5 above. EK 1.6.A.1 makes peak position the removal energy and EK 1.5.A.4 relates that energy to distance from the nucleus and effective nuclear charge, so the largest binding energy marks the closest subshell. The check confirms the tallest peak is a DIFFERENT peak, which is what makes the height-based option wrong."),
 ("Four electrons",
  "Recomputed in q6 above: the smallest tabulated binding energy is the most loosely held subshell, which is the outermost, and EK 1.6.A.1 makes its height the electron count. Reading the height at the other end of the table gives a rejected value, which the check confirms is different."),
 ("1s subshell, which is the closest to the nucleus",
  "EK 1.6.A.1 makes the largest binding energy the most tightly held electrons, EK 1.5.A.4 places those closest to the nucleus, and EK 1.5.A.3's shell model caps the 1s subshell at two electrons. A p subshell holds six, so the claim that every subshell holds two is false on the framework's own terms."),
 ("attracted more strongly as the nuclear charge increases",
  "Recomputed in q8 above: the innermost binding energy rises down the table while every tabulated height stays equal. LO 1.6.A's second clause asks what a spectrum says about electron-nucleus interaction, and EK 1.5.A.2 makes a larger nuclear charge a stronger attraction at fixed distance. The constant heights are what rule out the electron-count explanation."),
 ("Three to one",
  "Recomputed in q9 above. EK 1.6.A.1 makes relative height proportional to electron count, so the ratio of two heights is the ratio of two counts with the proportionality constant cancelling."),
 ("Five peaks",
  "EK 1.6.A.1 assigns one peak to each subshell, so the count of peaks is the count of OCCUPIED SUBSHELLS in the configuration given -- five of them. Counting the three occupied shells or the sixteen electrons gives the two nearest rejected options."),
 (r"1s^2\,2s^2\,2p^6\,3s^2",
  "DERIVED in q11 above from the item's own spectrum by the same route as item 3, and the check confirms no distractor reproduces the same four heights in the same order."),
 ("same number of electrons, but the second has more protons",
  "Recomputed in q12 above: the two spectra carry identical heights, so by EK 1.6.A.1 identical electron counts, while every binding energy is larger. EK 1.5.A.2 attributes a stronger hold on the same electrons to a larger nuclear charge, and the equal peak counts rule out an additional subshell."),
 ("2s electrons are held more tightly than 2p electrons",
  "EK 1.6.A.1 gives each SUBSHELL its own peak position, and EK 1.5.A.3 places the s and p subshells inside a single shell, so two peaks from one shell is a statement about sublevels. Protons sit in the nucleus by EK 1.5.A.1, and all electrons carry the same charge."),
 ("height of three rather than six",
  "Recomputed in q14 above: the spectrum implies the same three subshells as the student's configuration and disagrees only in the outermost electron count. That the peak COUNT matches is what rules out the other objection, and suggested skill 4.B is the skill being exercised."),
 ("Six electrons, so the atomic number is six",
  "Recomputed in q15 above as the sum of the tabulated heights, per EK 1.6.A.1, together with EK 1.5.A.1's equality of protons and electrons in a neutral atom. The check confirms the peak count differs from the electron total."),
 ("lowest binding energy, which holds one electron",
  "Recomputed in q16 above. EK 1.6.A.1 makes peak position the removal energy, so the smallest tabulated energy marks the electron removed most easily, and the check confirms the tallest peak is neither the lowest nor the highest in energy -- so a student reading height instead of position lands on a distractor."),
 (r"3s^2\,3p^1",
  "DERIVED in q17 above from the item's own five-peak spectrum, with the check confirming no distractor reproduces all five heights in Aufbau order."),
 ("an empty subshell has none to remove",
  "EK 1.6.A.1 makes the relative height proportional to the number of electrons in the subshell, and a quantity proportional to zero is zero. The framework describes no negative heights and places no limit on which subshells the technique reaches."),
 (r"1s^2\,2s^1",
  "EK 1.6.A.1 assigns one peak per occupied subshell, position giving removal energy and height giving electron count, so the higher-energy peak of height two is the innermost subshell and the lower one of height one is the next. The Aufbau order of EK 1.5.A.3 fills the second-shell s subshell before the p subshell, and the 1s capacity of two rules out the three-electron option."),
 ("innermost subshell, because those electrons feel the full increase",
  "LO 1.6.A's second clause, with EK 1.5.A.4: removal energy depends on distance from the nucleus and on the EFFECTIVE nuclear charge, which is the nuclear charge less the shielding. An innermost electron sits inside nearly all the others, so an added proton reaches it almost unshielded, while an outer electron's gain is largely offset by the electron added alongside it."),
 ("outermost shell holds eight electrons",
  "Recomputed in q21 above: the two lowest binding energies belong to the outer shell and their heights add to eight. The total of ten and the innermost height of two are both checked to be different numbers, so each appears among the rejected options."),
 ("number of electrons in the atom",
  "EK 1.6.A.1 makes each height proportional to one subshell's electron count, so the heights add to the atom's electron total, and EK 1.5.A.1 equates that with the proton count in a neutral atom. Heights being relative is precisely what allows them to be summed against one another."),
 ("three times as many electrons",
  "EK 1.6.A.1 makes relative height proportional to the number of electrons, so a ratio of heights is a ratio of electron counts. How hard an electron is to remove is carried by peak POSITION and has nothing to do with height."),
 ("four subshells are occupied",
  "EK 1.6.A.1 pairs one peak with each subshell, so the number of peaks counts occupied subshells. The electron total comes from the heights and the number of shells from which subshells those are, so neither can be read off the peak count."),
 ("tallest peak here sits at the third-largest binding energy",
  "Recomputed in q25 above against the item's own table: the tallest peak and the highest-energy peak are different peaks, and the innermost one has height two. EK 1.6.A.1 makes height and position independent readings, which is exactly what the student's claim denies."),
 ("How strongly the electrons in each subshell are held",
  "EK 1.6.A.1 states that the energies of the electrons in a given shell can be measured experimentally with PES and that peak position is the removal energy -- LO 1.6.A's interaction between the electrons and the nucleus. Isotopic composition is what a mass spectrum supplies instead, under EK 1.2.A.1."),
 ("more electrons in its outermost subshell",
  "Recomputed in q27 above: every corresponding binding energy is larger for the second element and its outermost peak is taller. By EK 1.6.A.1 the first comparison is about removal energies and the second about electron counts, so both halves of the keyed statement are read directly off the two spectra."),
 ("only their ratios carry information",
  "EK 1.6.A.1 makes height PROPORTIONAL to the number of electrons in the subshell, and a proportionality fixes ratios rather than absolute values. Rescaling every height by one factor therefore leaves every electron count unchanged."),
 ("two separate peaks for that shell rather than one",
  "Suggested skill 4.B: is the model consistent with the evidence. EK 1.6.A.1 gives one peak per SUBSHELL and EK 1.5.A.3 puts the s and p subshells inside one shell, so a filled second shell produces two peaks at different energies -- which a single shared energy per shell would forbid."),
 ("positively charged ion",
  "EK 1.6.A.1 makes the equal heights an equal electron count and the larger positions larger removal energies, and EK 1.5.A.2 attributes a firmer hold on the same number of electrons to a larger net positive charge. Adding electrons would raise the total height, so the negative-ion option is refuted by the heights themselves."),
]

TABLE_CHECKS = {3: q3, 4: q4, 5: q5, 6: q6, 8: q8, 9: q9, 11: q11, 12: q12,
                14: q14, 15: q15, 16: q16, 17: q17, 21: q21, 25: q25, 27: q27}


def _selftest():
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("h1_6_mutant")
        mod.TOPIC = h1_6.TOPIC
        mod.QUESTIONS = copy.deepcopy(h1_6.QUESTIONS)
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
        claims[8] = ("no such phrase anywhere in the choice", claims[8][1])

    def corrupt_peak_height(mod, claims):
        # Element X's 2p peak drops to five electrons: the keyed configuration
        # is no longer what the spectrum says.
        mod.QUESTIONS[2]["table"] = dict(
            headers=h1_6._H,
            rows=[["Peak 1", "104", "2"], ["Peak 2", "6.84", "2"],
                  ["Peak 3", "3.67", "5"], ["Peak 4", "0.50", "1"]])

    def impossible_spectrum(mod, claims):
        mod.QUESTIONS[10]["table"] = dict(
            headers=h1_6._H,
            rows=[["Peak 1", "126", "2"], ["Peak 2", "9.07", "2"],
                  ["Peak 3", "5.31", "7"], ["Peak 4", "0.74", "2"]])

    def reorder_energies(mod, claims):
        # Put the tallest peak at the HIGHEST binding energy: item 25's key,
        # which turns on those being different peaks, becomes false.
        mod.QUESTIONS[24]["table"] = dict(
            headers=h1_6._H,
            rows=[["Peak 1", "104", "6"], ["Peak 2", "6.84", "2"],
                  ["Peak 3", "3.67", "2"], ["Peak 4", "0.50", "1"]])

    def flatten_innermost_trend(mod, claims):
        mod.QUESTIONS[7]["table"] = dict(
            headers=h1_6._T_INNERMOST["headers"],
            rows=[["Element J", "28.6", "2"], ["Element K", "28.6", "2"],
                  ["Element L", "28.6", "2"], ["Element M", "28.6", "2"]])

    def make_the_student_right(mod, claims):
        mod.QUESTIONS[13]["table"] = dict(
            headers=h1_6._H,
            rows=[["Peak 1", "39.6", "2"], ["Peak 2", "2.45", "2"],
                  ["Peak 3", "1.45", "6"]])

    def break_the_ion_comparison(mod, claims):
        mod.QUESTIONS[11]["table"] = dict(
            headers=h1_6._H,
            rows=[["Peak 1", "126", "2"], ["Peak 2", "9.07", "2"],
                  ["Peak 3", "5.31", "6"], ["Peak 4", "0.74", "2"]])

    def forget_table_check(mod, claims):
        mod.QUESTIONS[0]["table"] = h1_6._T_X

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[6]["choices"][2] = mod.QUESTIONS[6]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[18]["why"] = "From the table."

    def letter_reference(mod, claims):
        mod.QUESTIONS[1]["why"] = ("Option D is excluded because the framework says so, "
                                   "and the rest of the reasoning follows from that.")

    def notation_slips_in(mod, claims):
        mod.QUESTIONS[2]["choices"][1] = "1s2 2s2 2p6 3s^2 as written"
        chem_notation.style(mod)

    print("negative controls:")
    must_fail("a configuration written with a bare caret outside a span", notation_slips_in)
    must_fail("key moved off its anchor", move_key)
    must_fail("anchor no longer present in the keyed choice", break_anchor)
    must_fail("a peak height changed so the keyed configuration is false", corrupt_peak_height)
    must_fail("a spectrum describing no possible atom (a 2p peak of height seven)",
              impossible_spectrum)
    must_fail("the tallest peak moved to the highest binding energy, making the "
              "student's claim true", reorder_energies)
    must_fail("the innermost-peak trend flattened, refuting the keyed explanation",
              flatten_innermost_trend)
    must_fail("the spectrum made to match the configuration it is supposed to refute",
              make_the_student_right)
    must_fail("a fourth peak added, so the two compared species no longer match",
              break_the_ion_comparison)
    must_fail("a table added with no recompute behind it", forget_table_check)
    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a rationale reduced below the minimum", thin_why)
    must_fail("a rationale naming an option by letter", letter_reference)
    print("all negative controls raised as required.")


import h1_6  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

chem_notation.style(h1_6)
cg.check(h1_6, CLAIMS, table_checks=TABLE_CHECKS)
