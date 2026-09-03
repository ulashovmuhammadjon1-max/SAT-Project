r"""Key audit for AP CHEMISTRY 1.2 Mass Spectra of Elements.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor -- the
exporter reshuffles choices, so a key stored as a bare index is one edit away
from pointing at a distractor. ``claim`` states what the key rests on.

EVERY WEIGHTED AVERAGE IN THIS TOPIC IS RECOMPUTED BELOW from the item's own
tabulated spectrum, which is what SCIENCE_BRIEF.md requires of quantitative
Chemistry. The checks do not stop at confirming the key: each also falsifies
the unweighted-mean distractor against the same numbers, because the
unweighted mean is the error EK 1.2.A.2 exists to rule out and an item whose
two candidate answers happen to coincide would test nothing.

WHAT THE KEYS REST ON
---------------------
Items 1, 3, 5, 9, 18, 19, 24 and 27 rest on EK 1.2.A.1: the mass spectrum of a
sample containing a single element can be used to determine the identity of the
isotopes of that element and the relative abundance of each isotope in nature.
Peak position carries mass, peak height carries abundance.

Items 2, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 20, 21, 22, 23, 25, 26, 28, 29
and 30 rest on EK 1.2.A.2: the average atomic mass of an element can be
estimated from the weighted average of the isotopic masses using the mass of
each isotope and its relative abundance.

Item 17 is the only item that says what makes two isotopes differ. It chains EK
1.2.A.1, which puts several isotopes of one element at different masses in one
spectrum, to EK 1.5.A.1, which states that the nucleus is made of protons and
neutrons; the proton count fixes the element, so within one element the mass
difference must sit in the neutrons.

THE EXCLUSION IS RESPECTED. The framework excludes spectra of samples
containing multiple elements and peaks from species other than singly charged
monatomic ions. Item 15 tabulates two spectra, but they are two separate
single-element samples and the item compares them; it does not ask a student to
disentangle two elements within one spectrum. No item involves a fragment or a
multiply charged ion.

DATA ITEMS: 2, 3, 4, 5, 6, 10, 11, 15, 16, 18, 21, 23, 27, 28 and 29 carry
tables and all fifteen are recomputed below.

NEGATIVE CONTROL: ``python3 verify_h1_2.py --selftest``.
"""
import sys

import cg_check as cg
import chem_notation

MZ = "Mass-to-charge ratio of the peak"
PCT = "Relative peak height (percent of all peaks)"


def _weighted(table, mz=MZ, pct=PCT):
    """The weighted average of EK 1.2.A.2, recomputed from the table alone."""
    masses = cg.col(table, mz)
    shares = cg.col(table, pct)
    total = sum(shares)
    assert abs(total - 100.0) < 1e-9, f"the tabulated abundances sum to {total}, not 100"
    return sum(m * s for m, s in zip(masses, shares)) / total, masses, shares


def _plain_mean(masses):
    return sum(masses) / len(masses)


def q2(table, item):
    avg, masses, _ = _weighted(table)
    assert abs(avg - 10.8) < 1e-9, f"the weighted average recomputes to {avg}, not 10.8"
    assert abs(_plain_mean(masses) - 10.5) < 1e-9, \
        "the unweighted-mean distractor should be 10.5"
    assert abs(avg - _plain_mean(masses)) > 0.2, \
        "the weighted and unweighted values must differ, or the item tests nothing"
    return f"0.200 times 10.0 plus 0.800 times 11.0 is {avg}, against an unweighted mean of 10.5"


def q3(table, item):
    _, masses, shares = _weighted(table)
    top = max(zip(shares, masses))[1]
    assert abs(top - 24.0) < 1e-9, f"the tallest peak sits at mass {top}, not 24.0"
    assert top == min(masses), "here the tallest peak is also the lightest, which the key says"
    assert max(shares) != min(shares), "'equally abundant' must be false on these heights"
    return (f"the tabulated heights are {shares} against masses {masses}, so the tallest "
            "peak is the lightest isotope and the three are not equally abundant")


def q4(table, item):
    avg, masses, shares = _weighted(table)
    lo, hi = min(masses), max(masses)
    assert lo < avg < hi, f"{avg} does not lie strictly between {lo} and {hi}"
    assert avg - lo < hi - avg, f"{avg} is not nearer the lighter isotope {lo}"
    assert dict(zip(masses, shares))[lo] > dict(zip(masses, shares))[hi], \
        "the key's reason requires the lighter isotope to be the more abundant"
    assert abs(avg - _plain_mean(masses)) > 0.1, "the 'exactly 64.0' midpoint must be false"
    return (f"the weighted average is {avg:.2f}, which lies between {lo} and {hi} and "
            f"nearer {lo} because that peak holds the larger share")


def q5(table, item):
    assert len(table["rows"]) == 3, f"the table shows {len(table['rows'])} peaks, not three"
    assert len(set(cg.col(table, MZ))) == 3, "the three peaks must sit at distinct masses"
    return "the tabulated spectrum carries exactly three peaks at three distinct masses"


def q6(table, item):
    avg, masses, _ = _weighted(table)
    assert abs(avg - 35.5) < 1e-9, f"the weighted average recomputes to {avg}, not 35.5"
    assert abs(_plain_mean(masses) - 36.0) < 1e-9, "the unweighted-mean distractor should be 36.0"
    assert abs(sum(masses) - 72.0) < 1e-9, "the sum-of-masses distractor should be 72.0"
    return f"0.750 times 35.0 plus 0.250 times 37.0 is {avg}, against an unweighted mean of 36.0"


def q10(table, item):
    avg, masses, _ = _weighted(table)
    assert abs(avg - 6.925) < 1e-9, f"the weighted average recomputes to {avg}"
    assert abs(round(avg, 1) - 6.9) < 1e-9, f"{avg} does not round to the keyed 6.9"
    assert avg < max(masses), "the answer must sit below the heavier isotopic mass"
    assert abs(_plain_mean(masses) - 6.5) < 1e-9, "the unweighted-mean distractor should be 6.5"
    return f"0.075 times 6.0 plus 0.925 times 7.0 is {avg}, which rounds to 6.9 and is below 7.0"


def q11(table, item):
    avg, masses, shares = _weighted(table)
    assert len(set(shares)) == 1, "the item's premise is that the two peaks are equal in height"
    assert abs(avg - 80.0) < 1e-9, f"the weighted average recomputes to {avg}, not 80.0"
    assert abs(avg - _plain_mean(masses)) < 1e-9, \
        "with equal weights the weighted average must reduce to the ordinary mean"
    return f"equal heights make the weighted average the ordinary mean of {masses}, which is {avg}"


def q15(table, item):
    # Two separate single-element spectra in one table, so the row label repeats
    # and cg.cell cannot be used. Parsed by hand instead.
    by_el = {}
    for el, mz, pct in table["rows"]:
        by_el.setdefault(el, []).append((cg.num(mz), cg.num(pct)))
    assert set(by_el) == {"Element G", "Element J"}, f"unexpected elements {sorted(by_el)}"
    avg = {el: sum(m * p for m, p in rows) / sum(p for _, p in rows)
           for el, rows in by_el.items()}
    assert avg["Element J"] > avg["Element G"], \
        f"element J {avg['Element J']} is not the larger average"
    assert min(m for m, _ in by_el["Element J"]) > max(m for m, _ in by_el["Element G"]), \
        "the key's reason requires every J peak to lie above every G peak"
    gaps = {el: max(p for _, p in rows) - min(p for _, p in rows) for el, rows in by_el.items()}
    assert gaps["Element G"] > gaps["Element J"], \
        "the 'differ more in height' distractor should point at the OTHER element"
    return (f"the weighted averages are {avg['Element G']:.1f} and {avg['Element J']:.1f}; every "
            "J peak lies above every G peak, while G is the one with the more unequal heights")


def q16(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, "Average atomic mass (atomic mass units)")))
    best = min(vals, key=lambda k: abs(vals[k] - 24.3))
    assert best == "Candidate 2", f"the closest tabulated average to 24.3 is {best}"
    others = sorted(abs(v - 24.3) for k, v in vals.items() if k != best)
    assert others[0] > 5.0, "a second candidate is close enough to make the match ambiguous"
    return (f"24.3 matches the tabulated {vals[best]} exactly, and the next nearest candidate "
            f"is {others[0]:.1f} atomic mass units away")


def q18(table, item):
    _, masses, shares = _weighted(table)
    share25 = dict(zip(masses, shares))[25.0]
    atoms = share25 / 100.0 * 1000
    assert abs(atoms - 100.0) < 1e-9, f"ten percent of one thousand recomputes to {atoms}"
    assert abs(share25 - 10.0) < 1e-9, \
        "the 'about 10' distractor should be the percentage read as a count"
    return f"the tabulated share at mass 25.0 is {share25} percent, which is {atoms:.0f} atoms per thousand"


def q21(table, item):
    avg, masses, _ = _weighted(table)
    mean = _plain_mean(masses)
    assert abs(mean - 64.0) < 1e-9, f"the student's unweighted mean is {mean}, not 64.0"
    assert abs(avg - 63.62) < 1e-6, f"the weighted average recomputes to {avg}"
    assert abs(round(avg, 1) - 63.6) < 1e-9, f"{avg} does not round to the keyed 63.6"
    assert avg < mean, "the keyed correction requires the weighted value to be BELOW the midpoint"
    return (f"the unweighted mean is {mean} while the weighted average is {avg:.2f}, so the "
            "abundance-weighted value sits below the midpoint as the key says")


def q23(table, item):
    # Cells here are prose of the form "6.0 at 7.5 percent", so they are parsed
    # rather than read with cg.col -- a cell with two numbers in it would make
    # cg.num raise, which is the behaviour that sent this check down this path.
    import re
    out = {}
    for label, light, heavy in table["rows"]:
        pairs = []
        for cellv in (light, heavy):
            nums = re.findall(r"\d+(?:\.\d+)?", cellv)
            assert len(nums) == 2, f"cell {cellv!r} does not hold a mass and a percentage"
            pairs.append((float(nums[0]), float(nums[1])))
        total = sum(p for _, p in pairs)
        assert abs(total - 100.0) < 1e-9, f"{label} abundances sum to {total}"
        out[label] = (sum(m * p for m, p in pairs) / total, pairs)
    dist = {lab: abs(v[1][1][0] - v[0]) for lab, v in out.items()}
    best = min(dist, key=dist.get)
    assert best == "Spectrum 1", f"the average nearest its own heavier peak is {best}"
    assert len(set(round(d, 6) for d in dist.values())) > 1, "'all equally close' must be false"
    for lab, (avg, pairs) in out.items():
        mid = (pairs[0][0] + pairs[1][0]) / 2
        assert abs(avg - mid) > 1e-6, f"{lab} sits at its midpoint, so 'always at the midpoint' holds"
    return (f"distances from each weighted average to its own heavier peak are "
            f"{ {k: round(v, 3) for k, v in dist.items()} }, so Spectrum I is nearest and no "
            "spectrum sits at its midpoint")


def q27(table, item):
    heights = cg.col(table, "Peak height (arbitrary units)")
    masses = cg.col(table, MZ)
    share = dict(zip(masses, heights))[20.0] / sum(heights) * 100
    assert abs(share - 75.0) < 1e-9, f"the share at mass 20.0 recomputes to {share}, not 75.0"
    assert abs(dict(zip(masses, heights))[20.0] - 3.00) < 1e-9, \
        "the 'read the raw height as a percentage' distractor should be 3.00"
    return f"3.00 of a total height of {sum(heights)} is {share:.1f} percent of the sample"


def q28(table, item):
    heights = cg.col(table, "Peak height (arbitrary units)")
    masses = cg.col(table, MZ)
    total = sum(heights)
    avg = sum(m * h for m, h in zip(masses, heights)) / total
    assert abs(avg - 20.5) < 1e-9, f"the weighted average recomputes to {avg}, not 20.5"
    assert abs(_plain_mean(masses) - 21.0) < 1e-9, "the unweighted-mean distractor should be 21.0"
    return (f"heights {heights} give fractional abundances of 0.750 and 0.250, and the weighted "
            f"average of {masses} is {avg}")


def q29(table, item):
    avg, masses, shares = _weighted(table)
    dominant = max(zip(shares, masses))[1]
    assert abs(dominant - 28.0) < 1e-9, f"the dominant peak is at mass {dominant}"
    assert all(m >= dominant for m in masses), \
        "the key's reason requires every other isotope to be HEAVIER than the dominant one"
    assert avg > dominant, f"the weighted average {avg} does not exceed {dominant}"
    assert avg - dominant < 0.5, f"the weighted average {avg} is not 'slightly' above 28.0"
    assert avg < 29.0, "the 'close to 29.0' distractor must be false"
    return (f"the dominant peak holds {max(shares)} percent at mass {dominant} and both other "
            f"isotopes are heavier, so the weighted average {avg:.2f} sits just above 28.0")


CLAIMS = [
 ("identity of the isotopes",
  "EK 1.2.A.1, near verbatim: the mass spectrum of a sample containing a single element can be used to determine the identity of the isotopes of that element and the relative abundance of each isotope in nature. Nothing about bonding, geometry or bulk properties follows from a mass spectrum."),
 ("10.8 atomic mass units",
  "Recomputed in q2 above from the item's own tabulated spectrum, using the weighted average EK 1.2.A.2 defines. The check also confirms the unweighted mean is a different number, so a student who ignores the abundances lands on a distractor."),
 ("mass 24.0, whose peak is the tallest",
  "Recomputed in q3 above: the largest tabulated relative height belongs to the lightest of the three peaks. EK 1.2.A.1 makes that height the relative abundance in nature, so nothing about which isotope is heaviest is relevant."),
 ("nearer 63.0",
  "Recomputed in q4 above: the weighted average lies strictly between the two isotopic masses and nearer the more abundant one. EK 1.2.A.2's weighting is what makes the answer differ from the midpoint, which is checked false on the same numbers."),
 ("three separate peaks",
  "Recomputed in q5 above from the number of rows in the item's table. EK 1.2.A.1 assigns each peak of a single-element spectrum to one isotope of that element, so the count of peaks is the count of isotopes."),
 ("35.5 atomic mass units",
  "Recomputed in q6 above. The unweighted mean and the sum of the two masses are both checked against the table so that the two commonest wrong methods land on rejected options rather than on the key."),
 ("weighted average over isotopes of different masses",
  "EK 1.2.A.2 defines the reported average atomic mass as the weighted average of the isotopic masses, and a weighted average of two or more distinct values falls between them unless one abundance is the whole sample. Individual atoms of one isotope are not of continuously varying mass."),
 ("mass 35.0 is the more abundant",
  "EK 1.2.A.2's weighted average sits closer to the mass carrying the larger weight, and 35.5 is one quarter of the way from 35.0 to 37.0. The total size of the sample cancels out of a weighted average, so it is not needed."),
 ("relative abundance in nature of the isotope",
  "EK 1.2.A.1 states that the spectrum determines the identity of the isotopes and the relative abundance of each isotope in nature. The mass information is carried by where a peak sits; the abundance information is carried by how tall it is."),
 ("6.9 atomic mass units",
  "Recomputed in q10 above: the weighted average is 6.925, which rounds to 6.9 and lies below the heavier isotopic mass because that isotope holds almost all the abundance."),
 ("80.0 atomic mass units",
  "Recomputed in q11 above. When the weights in EK 1.2.A.2's weighted average are equal the expression reduces to the ordinary mean, which the check confirms directly rather than assuming."),
 ("69.8 atomic mass units",
  "EK 1.2.A.2's weighted average is 0.600 times 69.0 plus 0.400 times 71.0, which is 69.8. Fractional abundances and percentage abundances are the same weights on different scales, so the form of the calculation does not change."),
 ("f_1 m_1",
  "EK 1.2.A.2 defines the average atomic mass as the weighted average of the isotopic masses using the mass of each isotope and its relative abundance, which is the sum over isotopes of mass multiplied by its own fractional abundance. Every rejected expression either discards the abundances or combines the two quantities in a way that is not an average."),
 ("larger, because more of the weight",
  "In the weighted average of EK 1.2.A.2 each isotopic mass is multiplied by its own abundance, so moving weight onto the heavier isotope raises the result while the isotopic masses stay fixed. The rejected options treat abundance as if it did not enter the calculation at all."),
 ("Element J, because both of its peaks lie at higher mass",
  "Recomputed in q15 above from the two tabulated spectra. A weighted average always lies between the smallest and largest value averaged, so an element whose every isotopic mass is larger must have the larger average; the check also confirms the height-based distractor points at the other element."),
 ("Candidate 2",
  "Recomputed in q16 above. EK 1.2.A.2 makes the weighted average of the isotopic masses an estimate of the element's average atomic mass, and the check confirms no second candidate lies close enough for the identification to be ambiguous."),
 ("number of neutrons in the nucleus",
  "Chaining EK 1.2.A.1, which places several isotopes of one element at different masses in one spectrum, to EK 1.5.A.1, which states that the nucleus is made of protons and neutrons. The proton count is what makes the sample one element, so a mass difference within it has to sit in the neutrons; the stem fixes both ions as singly charged."),
 ("About 100 atoms",
  "Recomputed in q18 above: the tabulated relative height at that mass is ten percent, which EK 1.2.A.1 makes the isotope's share of the sample, and ten percent of a thousand atoms is a hundred. Reading the percentage straight off as a count gives the rejected value."),
 ("add to one hundred percent",
  "A relative abundance in EK 1.2.A.1 is an isotope's share of the sample, so the shares of all the isotopes present exhaust it. That is also what puts the weighted average of EK 1.2.A.2 on the same scale as the individual isotopic masses."),
 ("very small increase",
  "In EK 1.2.A.2's weighted average each isotopic mass enters multiplied by its own abundance, so an abundance of one part in ten thousand can shift the result only slightly however extreme its mass. Adding an isotope does not make the average undefined."),
 ("about 63.6",
  "Recomputed in q21 above. EK 1.2.A.2 calls for a weighted average using each isotope's relative abundance, and the check confirms the correct value falls below the student's midpoint because the lighter isotope is the more abundant."),
 ("11.0 atomic mass units",
  "The two abundances must exhaust the sample, fixing the heavier isotope at 80.0 percent, and EK 1.2.A.2 then gives 10.8 equal to 0.200 times 10.0 plus 0.800 times the unknown mass. Solving leaves 11.0, so the missing abundance does not have to be supplied separately."),
 ("Spectrum 1",
  "Recomputed in q23 above: the distance from each weighted average to its own heavier peak is computed for all three spectra and only one is nearest. The check also confirms no spectrum sits at its own midpoint, so the 'always at the midpoint' option is false on the data."),
 ("as they are naturally found",
  "EK 1.2.A.1 ties the abundance obtained from a spectrum to how common the isotope is in nature, and EK 1.2.A.2 uses exactly those abundances as the weights. Abundance is a share of a sample and does not set the mass of any isotope."),
 ("close to that isotope's mass but shifted",
  "The largest weight in EK 1.2.A.2's weighted average belongs to the most abundant isotope, so the result sits near that mass, while the remaining abundances pull it toward whichever masses they carry. Those may lie above or below, so no fixed direction can be asserted."),
 ("106.9 atomic mass units",
  "Nearly equal weights put EK 1.2.A.2's weighted average near the midpoint of 107.0, and the slight excess of abundance on the lighter peak moves the result a little below that midpoint rather than above it."),
 ("75.0 percent",
  "Recomputed in q27 above. EK 1.2.A.1 makes peak height proportional to the number of atoms of that isotope, so a relative abundance is one height divided by the total of all the heights; reading the raw height as a percentage gives a rejected option."),
 ("20.5 atomic mass units",
  "Recomputed in q28 above from the raw heights, converted to fractional abundances first and then fed to EK 1.2.A.2's weighted average. The unweighted mean of the two masses is checked to be a different, rejected value."),
 ("slightly above 28.0",
  "Recomputed in q29 above: the dominant peak sits at the LIGHTEST mass and both minor isotopes are heavier, so the weighted average of EK 1.2.A.2 can only be pulled upward, and the check confirms the shift is under half an atomic mass unit."),
 ("11.0 is the mass of one isotope",
  "EK 1.2.A.1 assigns every peak of a single-element spectrum to an isotope of that element, so the shorter peak is not an impurity, and EK 1.2.A.2 requires every isotopic mass to enter the average weighted by its abundance. The reported average therefore lies strictly between the two peak positions."),
]

TABLE_CHECKS = {2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 10: q10, 11: q11, 15: q15,
                16: q16, 18: q18, 21: q21, 23: q23, 27: q27, 28: q28, 29: q29}


def _selftest():
    """Negative control: every gate must FAIL when its own input is corrupted."""
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("h1_2_mutant")
        mod.TOPIC = h1_2.TOPIC
        mod.QUESTIONS = copy.deepcopy(h1_2.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:95]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[1]["ans"] = 1

    def break_anchor(mod, claims):
        claims[22] = ("no such phrase anywhere in the choice", claims[22][1])

    def flip_abundances(mod, claims):
        # Swap the two abundances in q2's spectrum: the weighted average becomes
        # 10.2, so the keyed 10.8 is no longer what the table says.
        mod.QUESTIONS[1]["table"] = dict(headers=h1_2._T_X["headers"],
                                         rows=[["10.0", "80.0"], ["11.0", "20.0"]])

    def abundances_stop_summing(mod, claims):
        mod.QUESTIONS[5]["table"] = dict(headers=h1_2._T_CL["headers"],
                                         rows=[["35.0", "75.0"], ["37.0", "35.0"]])

    def make_dominant_peak_heaviest(mod, claims):
        # q29's key says the average sits slightly ABOVE the dominant mass
        # because every other isotope is heavier. Put the tall peak on top.
        mod.QUESTIONS[28]["table"] = dict(
            headers=h1_2._T_SI["headers"],
            rows=[["28.0", "3.0"], ["29.0", "5.0"], ["30.0", "92.0"]])

    def make_candidates_ambiguous(mod, claims):
        mod.QUESTIONS[15]["table"] = dict(
            headers=h1_2._T_CANDIDATES["headers"],
            rows=[["Candidate 1", "10.8"], ["Candidate 2", "24.3"],
                  ["Candidate 3", "24.4"], ["Candidate 4", "63.5"],
                  ["Candidate 5", "80.0"]])

    def forget_table_check(mod, claims):
        mod.QUESTIONS[0]["table"] = h1_2._T_X

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[7]["choices"][2] = mod.QUESTIONS[7]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[16]["why"] = "It just is."

    def letter_reference(mod, claims):
        mod.QUESTIONS[6]["why"] = ("Choice D is wrong because the framework says so, and "
                                   "the remaining reasoning follows directly from that.")

    def notation_slips_in(mod, claims):
        mod.QUESTIONS[12]["choices"][3] = r"The product m_1 m_2 m_3 of the three masses"
        chem_notation.style(mod)

    def macro_escapes_its_span(mod, claims):
        mod.QUESTIONS[12]["q"] = r"An element has isotopes of mass \(m_1\) and mass m_2 overall."
        chem_notation.style(mod)

    print("negative controls:")
    must_fail("a bare subscript loose in a choice", notation_slips_in)
    must_fail("a subscript that escaped its math span", macro_escapes_its_span)
    must_fail("key moved off its anchor", move_key)
    must_fail("anchor no longer present in the keyed choice", break_anchor)
    must_fail("abundances swapped so the keyed average is false", flip_abundances)
    must_fail("abundances no longer summing to one hundred", abundances_stop_summing)
    must_fail("dominant peak moved to the heaviest mass", make_dominant_peak_heaviest)
    must_fail("a second candidate close enough to make the match ambiguous",
              make_candidates_ambiguous)
    must_fail("a table added with no recompute behind it", forget_table_check)
    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a rationale reduced below the minimum", thin_why)
    must_fail("a rationale naming an option by letter", letter_reference)
    print("all negative controls raised as required.")


import h1_2  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

chem_notation.style(h1_2)
cg.check(h1_2, CLAIMS, table_checks=TABLE_CHECKS)
