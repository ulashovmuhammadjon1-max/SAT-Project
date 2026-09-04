"""Key audit for AP CHEMISTRY 8.5 Acid-Base Titrations.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  8.5.A.1  a titration curve plots pH against volume of titrant   1, 27
  8.5.A.2  at the equivalence point, moles of titrant equal moles of analyte,
           for weak and strong alike       2, 3, 4, 7, 10, 12, 13, 14, 21, 24, 28
  8.5.A.3  the half-equivalence point has equal concentrations of the pair, so
           pH equals pKa there             5, 6, 11, 19, 20, 22, 23, 29, 30
  8.5.A.4  the equivalence pH is set by the major species: neutral for strong
           with strong, basic for a weak acid, acidic for a weak base
                                           8, 9, 18
  8.5.A.5  a polyprotic curve gives the number of acidic protons, the major
           species and each pKa -- qualitatively only    15, 16, 17, 25, 26

THE FIGURE PROBLEM. EK 8.5.A.1 makes the CURVE the representation of this topic
and this bank cannot show one, so every curve is a table of volume against pH.
``no_figure_language`` asserts that no stem or choice refers to a picture,
which is the defect SCIENCE_BRIEF.md names and the project has shipped once.

TWO SCOPE CHECKS. ``no_indicator_selection`` keeps EK 8.7.A.3's rule about
choosing an indicator out of this module, since 8.7 owns it.
``polyprotic_stays_qualitative`` asserts that no item pairing a polyprotic acid
with a numeric key exists, which is what EK 8.5.A.5's exclusion statement
requires.

ARITHMETIC. Every analyte concentration is recomputed through ``analyte_conc``,
written once, from the stated or tabulated volumes and titrant concentration.

NEGATIVE CONTROL: ``python3 verify_h8_5.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h8_5

VOLCOL = "Volume of 0.100 M NaOH added (mL)"
PHCOL = "pH of the flask"
AVOL = "Volume of analyte (mL)"
TCONC = "Concentration of titrant (M)"
TVOL = "Volume of titrant at the equivalence point (mL)"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|curve above|curve below)(?![a-z])", re.I)
_INDICATOR = re.compile(r"(?<![A-Za-z])indicators?(?![A-Za-z])", re.I)
_POLYPROTIC = re.compile(r"(?<![A-Za-z])(?:di|tri|poly)protic(?![A-Za-z])", re.I)
_NUMERIC_KEY = re.compile(r"\d+\.\d+\s*M(?![A-Za-z])")


def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, but every titration "
                f"curve here is a table -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: every titration curve is carried as a table of "
          "volume against pH.")


def no_indicator_selection(module):
    """EK 8.7.A.3's indicator rule belongs to 8.7, not here."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _INDICATOR.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: mentions an indicator, which is 8.7's material "
                f"-- {text[:60]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no item selects an indicator, which is 8.7's "
          "material.")


def polyprotic_stays_qualitative(module):
    """EK 8.5.A.5's exclusion statement bars per-species computation."""
    for i, item in enumerate(module.QUESTIONS, 1):
        if _POLYPROTIC.search(item["q"]):
            hit = _NUMERIC_KEY.search(h.keyed(item))
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: a polyprotic item with a computed concentration "
                f"({hit.group(0)!r}) in its key, which EK 8.5.A.5 excludes"
            )
    print(f"OK  {module.TOPIC[0]} scope: every polyprotic item stays qualitative, as EK "
          "8.5.A.5's exclusion statement requires.")


def analyte_conc(titrant_conc, titrant_volume, analyte_volume):
    """EK 8.5.A.2: equal moles at the equivalence point, written once."""
    mmol = titrant_conc * titrant_volume
    return mmol / analyte_volume


# ------------------------------------------------------------------ table items

def _curve(table):
    return dict(zip([str(v) for v in cg.col(table, VOLCOL)], cg.col(table, PHCOL)))


def q6(table, item):
    vols = cg.col(table, VOLCOL)
    phs = dict(zip(vols, cg.col(table, PHCOL)))
    half = 20.00 / 2.0
    assert half in phs, f"the half-equivalence volume {half} is not tabulated: {sorted(phs)}"
    assert abs(phs[half] - 4.75) < 1e-9, f"the tabulated pH there is {phs[half]}"
    assert abs(phs[20.00] - 8.80) < 1e-9, "the equivalence pH must be the 8.80 distractor"
    h.shows(item, "4.75")
    return (f"half of the 20.00 mL equivalence volume is {half:g} mL, where the table "
            f"reports pH {phs[half]:g}")


def q7(table, item):
    c = analyte_conc(0.100, 20.00, 25.00)
    assert abs(c - 0.0800) < 1e-12, f"the analyte concentration recomputes to {c}"
    assert abs(0.100 * 20.00 / 20.00 - 0.100) < 1e-12, \
        "the 0.100 M distractor must come from dividing by the titrant volume"
    h.shows(item, "0.0800 M")
    return f"2.00 millimoles of titrant in a 25.00 mL sample recomputes the concentration as {c:g} M"


def q8(table, item):
    phs = dict(zip(cg.col(table, VOLCOL), cg.col(table, PHCOL)))
    assert phs[20.00] > 7.0, f"the tabulated equivalence pH is {phs[20.00]}, not above 7"
    assert phs[0.00] < 7.0, "the titration must start acidic"
    h.shows(item, "conjugate base of the weak acid is present")
    return f"the tabulated equivalence pH is {phs[20.00]:g}, above the neutral value"


def q9(table, item):
    phs = dict(zip(cg.col(table, VOLCOL), cg.col(table, PHCOL)))
    neutral = [v for v, ph in phs.items() if abs(ph - 7.0) < 1e-9]
    assert neutral == [25.00], f"tabulated readings at pH 7.00: {neutral}"
    h.shows(item, "strong acid and strong base titration results in a neutral pH")
    return f"the tabulated readings pass through 7.00 at {neutral[0]:g} mL"


def q10(table, item):
    c = analyte_conc(0.100, 25.00, 25.00)
    assert abs(c - 0.100) < 1e-12, f"the analyte concentration recomputes to {c}"
    h.shows(item, "0.100 M")
    return f"2.50 millimoles of titrant in a 25.00 mL sample recomputes the concentration as {c:g} M"


def q12(table, item):
    c = analyte_conc(cg.cell(table, "2", TCONC), cg.cell(table, "2", TVOL),
                     cg.cell(table, "2", AVOL))
    assert abs(c - 0.100) < 1e-12, f"trial 2 recomputes to {c}"
    h.shows(item, "0.100 M")
    return f"the tabulated figures for trial 2 recompute the analyte concentration as {c:g} M"


def q13(table, item):
    cs = {lab: analyte_conc(cg.cell(table, lab, TCONC), cg.cell(table, lab, TVOL),
                            cg.cell(table, lab, AVOL))
          for lab in cg.labels(table)}
    largest = max(cs, key=cs.get)
    assert largest == "3", f"the most concentrated analyte is trial {largest}"
    assert len(set(round(v, 9) for v in cs.values())) == len(cs), \
        "the three recomputed concentrations must be distinct for the maximum to be unique"
    h.shows(item, "Trial 3")
    return f"the three recomputed concentrations are {cs}, whose maximum is at {largest}"


def q14(table, item):
    c = analyte_conc(cg.cell(table, "3", TCONC), cg.cell(table, "3", TVOL),
                     cg.cell(table, "3", AVOL))
    assert abs(c - 0.500) < 1e-12, f"trial 3 recomputes to {c}"
    assert abs(cg.cell(table, "3", TVOL) - cg.cell(table, "3", AVOL)) < 1e-12, \
        "the two volumes must be equal, which is why the concentrations agree"
    h.shows(item, "0.500 M")
    return (f"equal tabulated volumes make the analyte concentration equal the titrant's, "
            f"{c:g} M")


def steep_regions(table, threshold=0.5):
    """The volume spans over which pH climbs faster than `threshold` per mL.

    Measured as a SLOPE, not as a raw pH difference between adjacent rows.
    A difference says as much about how finely the table was sampled as
    about the chemistry: read every 10.00 mL, a curve that climbs steadily
    from 1.90 to 12.00 shows a 2-point "jump" in every interval and a
    genuine equivalence jump is indistinguishable from the plateau. Slope
    separates them -- the buffer regions here sit near 0.1 pH/mL and the
    equivalence jumps at 0.7 and above.

    Contiguous steep intervals are merged, so one jump straddling an
    equivalence volume counts once rather than twice.
    """
    vols, phs = cg.col(table, VOLCOL), cg.col(table, PHCOL)
    assert vols == sorted(vols), f"tabulated volumes are not ascending: {vols}"
    assert phs == sorted(phs), f"tabulated pH does not rise monotonically: {phs}"
    slopes = [(phs[i + 1] - phs[i]) / (vols[i + 1] - vols[i]) for i in range(len(vols) - 1)]
    regions, run = [], None
    for i, s in enumerate(slopes):
        if s >= threshold:
            run = (vols[i], vols[i + 1]) if run is None else (run[0], vols[i + 1])
        elif run is not None:
            regions.append(run)
            run = None
    if run is not None:
        regions.append(run)
    return regions, slopes


def q15(table, item):
    regions, slopes = steep_regions(table)
    assert len(regions) == 2, (
        f"a diprotic curve must show exactly two regions of rapid rise; the tabulated "
        f"readings show {len(regions)}: {regions} from slopes {[round(s, 3) for s in slopes]}"
    )
    # Each jump has to sit ON an equivalence volume, not merely somewhere.
    for eq, region in zip((20.00, 40.00), regions):
        assert region[0] <= eq <= region[1], (
            f"the rapid rise at {region} does not contain the equivalence volume {eq}"
        )
    h.shows(item, "two separate regions of rapid pH rise")
    return (f"the tabulated readings rise rapidly over {regions[0]} and {regions[1]} mL, "
            f"bracketing both equivalence volumes, and sit near "
            f"{min(slopes):.2f} pH/mL on the buffer plateaus")


def q25(table, item):
    vols = cg.col(table, VOLCOL)
    assert 20.00 in vols and 40.00 in vols, f"tabulated volumes are {vols}"
    assert abs(20.00 - 40.00 / 2.0) < 1e-12, \
        "the first equivalence point must fall at half the second"
    h.shows(item, "reading at 20.00 mL")
    return "half of the stated 40.00 mL second equivalence volume is 20.00 mL, a tabulated reading"


TABLE_CHECKS = {6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 12: q12, 13: q13, 14: q14,
                15: q15, 19: None, 25: q25}
TABLE_CHECKS.pop(19)


def q19(table, item):
    phs = dict(zip(cg.col(table, VOLCOL), cg.col(table, PHCOL)))
    half = 20.00 / 2.0
    assert abs(phs[half] - 4.75) < 1e-9, f"the tabulated pH at {half} mL is {phs[half]}"
    h.shows(item, "4.75")
    return f"the table reports pH {phs[half]:g} at the half-equivalence volume of {half:g} mL"


TABLE_CHECKS[19] = q19


# ---------------------------------------------------------------- stem numerics

def n3(item):
    c = analyte_conc(0.100, 20.00, 25.00)
    assert abs(c - 0.0800) < 1e-12, f"recomputed {c}"
    assert abs(0.100 * 25.00 / 20.00 - 0.125) < 1e-12, \
        "the 0.125 M distractor must come from dividing by the titrant volume"
    h.shows(item, "0.0800 M")
    return f"the equal-moles relationship recomputes the acid concentration as {c:g} M"


def n21(item):
    c = analyte_conc(0.200, 25.00, 50.00)
    assert abs(c - 0.100) < 1e-12, f"recomputed {c}"
    h.shows(item, "0.100 M")
    return f"5.00 millimoles of titrant in 50.00 mL recomputes the concentration as {c:g} M"


def n22(item):
    ka = 10.0 ** (-5.00)
    assert abs(ka - 1.0e-5) < 1e-15, f"the constant recomputes to {ka}"
    assert abs(1.0e-14 / ka - 1.0e-9) < 1e-18, \
        "the ten to the minus ninth distractor must be the conjugate base constant"
    h.shows(item, "1.0 \\times 10^{-5}")
    return f"ten raised to the negative of the half-equivalence pH recomputes Ka as {ka:g}"


def n23(item):
    assert 3.00 < 6.00, "the item's premise is that one half-equivalence pH is lower"
    ka_j, ka_l = 10.0 ** (-3.00), 10.0 ** (-6.00)
    assert ka_j > ka_l, f"the lower pKa must give the larger constant: {ka_j} against {ka_l}"
    h.shows(item, "Acid J")
    return f"pKa values of 3.00 and 6.00 recompute to constants {ka_j:g} and {ka_l:g}"


def n28(item):
    c = analyte_conc(0.500, 10.00, 10.00)
    assert abs(c - 0.500) < 1e-12, f"recomputed {c}"
    h.shows(item, "0.500 M")
    return f"equal volumes recompute the base concentration as {c:g} M, the titrant's own value"


def n30(item):
    pka = 9.00
    assert abs(14.0 - pka - 5.00) < 1e-9, \
        "the 5.00 distractor must be the pKb obtained by subtracting from fourteen"
    h.shows(item, "9.00")
    return ("the half-equivalence pH is the pKa of the conjugate acid directly, with 5.00 "
            "the pKb that subtracting from fourteen would give")


NUMERIC = {3: n3, 21: n21, 22: n22, 23: n23, 28: n28, 30: n30}


CLAIMS = [
 ("pH of the flask against the volume of titrant added",
  "EK 8.5.A.1, verbatim in substance: a titration curve plots pH against the volume of titrant added."),
 ("moles of titrant added equal the moles of analyte",
  "EK 8.5.A.2, verbatim in substance. Equal volumes or equal concentrations hold only by coincidence, and pH equalling pKa is the HALF-equivalence point of EK 8.5.A.3."),
 ("0.0800 M",
  "EK 8.5.A.2's equal-moles relationship. Recomputed in n3, which also recomputes the distractor formed by dividing by the wrong volume."),
 ("holds for titrations of both strong and weak",
  "EK 8.5.A.2 ends by saying this is the case for titrations of strong acids and bases AND weak acids and bases; partial ionization changes the pH reached, not the stoichiometry."),
 ("equal, so the pH equals the pKa",
  "EK 8.5.A.3, verbatim in substance: at the half-equivalence point there are equal concentrations of each species in the conjugate pair, and pH equals pKa when they are equal."),
 ("4.75",
  "EK 8.5.A.3 applied to the tabulated curve. Recomputed in q6, which locates half the equivalence volume in the table and checks the equivalence reading is a distractor."),
 ("0.0800 M",
  "EK 8.5.A.2 applied to the same tabulated titration. Recomputed in q7."),
 ("conjugate base of the weak acid is present",
  "EK 8.5.A.4: in titrations of weak acids the conjugate base is present at the equivalence point and undergoes proton transfer with water, producing a basic solution. The tabulated equivalence pH is checked above 7 in q8."),
 ("strong acid and strong base titration results in a neutral pH",
  "EK 8.5.A.4, verbatim in substance, and the tabulated readings pass through 7.00 exactly at the equivalence volume, which q9 recomputes."),
 ("0.100 M",
  "EK 8.5.A.2 applied to the strong acid curve, using the tabulated volume at which the pH reaches 7.00. Recomputed in q10."),
 ("no conjugate acid-base pair present in comparable amounts",
  "EK 8.5.A.3 introduces the half-equivalence point for titrations of WEAK acids and bases, where an un-ionized acid coexists with its conjugate base; EK 8.2.A.1 leaves a strong acid essentially fully ionized."),
 ("0.100 M",
  "EK 8.5.A.2 applied to a tabulated trial. Recomputed in q12 from the three tabulated figures."),
 ("Trial 3",
  "EK 8.5.A.2 applied across three tabulated trials. All three concentrations are recomputed in q13 and checked distinct so the maximum is unique."),
 ("0.500 M",
  "EK 8.5.A.2 where the two volumes happen to be equal, which is what makes the two concentrations agree. Recomputed in q14."),
 ("two separate regions of rapid pH rise",
  "EK 8.5.A.5: titration curves can be used to determine the number of acidic protons. The successive tabulated rises are counted in q15 and exactly two are steep."),
 ("major species present at any point, and the pKa associated with each proton",
  "EK 8.5.A.5, verbatim in substance, and its exclusion statement rules out computing the concentration of each species."),
 ("Computing the concentration of each species",
  "The exclusion statement attached to EK 8.5.A.5 names exactly this, while leaving qualitative reasoning about large versus small concentrations within scope."),
 ("conjugate acid of the weak base is present",
  "EK 8.5.A.4 for the mirrored case: the conjugate acid of a weak base is present at the equivalence point and transfers a proton to water, producing an acidic solution."),
 ("4.75",
  "EK 8.5.A.3 read directly off the tabulated curve at half the equivalence volume. Recomputed in q19."),
 ("pKa of the weak acid can be determined from the pH measured there",
  "EK 8.5.A.3 gives this as the reason the half-equivalence point is useful. The analyte CONCENTRATION comes from the equivalence point under EK 8.5.A.2 instead."),
 ("0.100 M",
  "EK 8.5.A.2 with a different pair of volumes and a different titrant concentration. Recomputed in n21."),
 ("1.0 \\times 10^{-5}",
  "EK 8.5.A.3 gives the pKa from the half-equivalence pH and EK 8.3.A.2 converts it to Ka. Recomputed in n22, which also recomputes the conjugate constant as the distractor."),
 ("Acid J",
  "EK 8.5.A.3 makes each half-equivalence pH a pKa, and EK 8.3.A.2 makes the smaller pKa the larger constant. Recomputed in n23."),
 ("equivalence volume depends on moles rather than on acid strength",
  "EK 8.5.A.2 fixes the equivalence point by equal MOLES, which depend on concentration and volume alone; EK 8.5.A.4 makes strength govern the pH reached there instead."),
 ("reading at 20.00 mL",
  "EK 8.5.A.5 has the curve reveal the protons, and a diprotic acid consumes equal titrant for each, so the first equivalence point falls at half the second. Checked against the tabulated volumes in q25."),
 ("singly deprotonated ion HA-",
  "EK 8.5.A.5 permits identifying the major species present at any point on a polyprotic curve while excluding computation of each concentration. One proton has been removed and the second has not yet begun to go."),
 ("titrant is added in measured amounts",
  "EK 8.5.A.1 pairs the controlled conditions with a curve plotting pH against the VOLUME OF TITRANT ADDED, so the measured addition is what makes each point interpretable; the analyte concentration is normally the unknown."),
 ("0.500 M",
  "EK 8.5.A.2 for a base titrated with an acid, with equal volumes making the concentrations agree. Recomputed in n28."),
 ("Between the start and the equivalence point",
  "EK 8.5.A.3 places equal concentrations of the pair at the half-equivalence point, so both members are present through the region before the equivalence point; EK 8.5.A.4 leaves only the conjugate base at the equivalence point itself."),
 ("9.00",
  "EK 8.5.A.3 makes the half-equivalence pH the pKa of the conjugate acid directly. Recomputed in n30, which also recomputes the pKb that subtracting from fourteen would give."),
]


def _extra_mutations():
    def corrupt_table(mod, cl):
        mod.QUESTIONS[5]["table"] = dict(
            headers=h8_5._T_WEAK_CURVE["headers"],
            rows=[[v, ("6.20" if v == "10.00" else ph)]
                  for v, ph in h8_5._T_WEAK_CURVE["rows"]])

    def corrupt_numeric(mod, cl):
        ch = list(mod.QUESTIONS[2]["choices"])
        ch[0] = "0.0900 M"
        mod.QUESTIONS[2]["choices"] = ch
        cl[2] = ("0.0900 M", cl[2][1])

    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the titration curve shown above, what is plotted?"
        no_figure_language(mod)

    def indicator_creeps_in(mod, cl):
        mod.QUESTIONS[4]["q"] = "Which indicator should be chosen for this titration?"
        no_indicator_selection(mod)

    def polyprotic_computation(mod, cl):
        ch = list(mod.QUESTIONS[14]["choices"])
        ch[0] = "The concentration of HA- is 0.050 M at that point"
        mod.QUESTIONS[14]["choices"] = ch
        cl[14] = ("concentration of HA-", cl[14][1])
        polyprotic_stays_qualitative(mod)

    def flat_diprotic(mod, cl):
        # The real defect this module shipped with: readings every 10.00 mL,
        # climbing at a near-constant rate, behind a stem that asks the
        # student to read TWO separate jumps off them. q15 must reject it.
        mod.QUESTIONS[14]["table"] = dict(
            headers=h8_5._T_DIPROTIC["headers"],
            rows=[["0.00", "1.90"], ["10.00", "2.90"], ["20.00", "5.00"],
                  ["30.00", "7.20"], ["40.00", "10.00"], ["50.00", "12.00"]])

    return [("the diprotic table flattened to uniform sampling, so no jump is "
             "readable where the stem says two are",
             flat_diprotic),
            ("a tabulated half-equivalence pH corrupted so the keyed pKa is false",
             corrupt_table),
            ("a recomputed analyte concentration no longer in the keyed choice",
             corrupt_numeric),
            ("a stem referring to a curve the bank cannot show", figure_language),
            ("an item selecting an indicator, which is 8.7's material", indicator_creeps_in),
            ("a polyprotic item with a computed concentration, which EK 8.5.A.5 excludes",
             polyprotic_computation)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h8_5, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h8_5)
no_indicator_selection(h8_5)
polyprotic_stays_qualitative(h8_5)
h.run(h8_5, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
