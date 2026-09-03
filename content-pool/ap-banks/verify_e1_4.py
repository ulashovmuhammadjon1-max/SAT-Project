"""Key audit for AP ENVIRONMENTAL SCIENCE 1.4 The Carbon Cycle.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Items 1, 2, 19, 22, 26, 27 and 29 rest on ERT-1.D.1: the carbon cycle is the
movement of atoms and molecules containing the element carbon between sources
and sinks. Movement rather than creation or destruction is the whole content of
that sentence, and it is what every "carbon is destroyed" distractor violates.

Items 3, 4, 5, 13, 14, 21, 25 and 29 rest on ERT-1.D.2: some of the reservoirs
in which carbon compounds occur hold those compounds for long periods of time
while some hold them for relatively short periods.

Items 6, 7, 8, 20, 23 and 30 rest on ERT-1.D.3: carbon cycles between
photosynthesis and cellular respiration in living things. Which of the two is
the uptake step is settled by ENG-1.A.1, which defines primary productivity as
the conversion of solar energy into organic compounds via photosynthesis.

Items 9, 10, 12, 15, 17, 18, 24, 27 and 28 rest on ERT-1.D.4: plant and animal
decomposition have led to the storage of carbon over millions of years, and the
burning of fossil fuels quickly moves that stored carbon into atmospheric
carbon, in the form of carbon dioxide.

DISTINCTNESS FROM 1.5, 1.6 AND 1.7. Only item 1 asks the sources-and-sinks
definition, and it asks it of carbon. No item here asks which reservoir is
LARGEST; that is a nitrogen fact (ERT-1.E.4), a phosphorus fact (ERT-1.F.2) and
a water fact (ERT-1.G.2), asked in those topics.

DATA ITEMS: 4, 5, 11, 12, 13, 14, 15, 16 and 17 carry tables. Each keyed
conclusion is recomputed below from that table alone, and each check also
falsifies the distractors against the same numbers.

NEGATIVE CONTROL: ``python3 verify_e1_4.py --selftest`` corrupts a key, an
anchor, a table cell and the notation on purpose and confirms each check fires.
"""
import re
import sys

import cg_check as cg

_BANNED = [
    (re.compile(r"\\"), "a backslash: this subject is not typeset, so LaTeX prints raw"),
    (re.compile(r"(?<![A-Za-z])\d+\s?-\s?\d"), "a digit-hyphen-digit range: write 'to' instead"),
    (re.compile(r"\d\s?/\s?\d"), "a digit-slash-digit fraction: write it out in words"),
    (re.compile(r"\^"), "a bare caret, which prints raw outside a math span"),
    (re.compile(r"\$"), "a dollar sign, which the converter reads as inline math"),
]


def style(module):
    """No typeset notation anywhere in the module's student-facing text."""
    for i, item in enumerate(module.QUESTIONS, 1):
        texts = [item["q"], item["why"]] + list(item["choices"])
        t = item.get("table")
        if t:
            texts += [str(h) for h in t["headers"]] + [str(c) for r in t["rows"] for c in r]
        for text in texts:
            for pat, msg in _BANNED:
                hit = pat.search(text)
                assert not hit, f"{module.TOPIC[0]} q{i}: {msg} -- {hit.group(0)!r} in {text[:70]!r}"
    print(f"OK  {module.TOPIC[0]} notation: no typeset markup in "
          f"{len(module.QUESTIONS)} questions.")


STAY = "Average time a carbon atom stays in the reservoir (years)"
MOVED = "Carbon moved each year (billions of tonnes)"
PPM = "Mean atmospheric carbon dioxide (parts per million)"
EMIT = "Carbon released by fossil fuel burning each year (billions of tonnes)"
STORED = "Carbon stored (tonnes per hectare)"
LEFT = "Percent of the original carbon still present after two years"
BURIED = "Carbon buried in sediment each year (grams per square meter)"
KEPT = "Percent of buried carbon still present after one hundred years"
WOOD = "Carbon in living wood (tonnes per hectare)"
RELEASED = "Carbon released to the air in the year measured (tonnes per hectare)"
AGE = "Age of the carbon it contains (years)"
BURNTIME = "Time taken to release that carbon once combustion begins (years)"


def q4(table, item):
    t = dict(zip(cg.labels(table), cg.col(table, STAY)))
    assert t["Fossil fuel deposits"] > 1e6 * t["Living plant tissue"], \
        "the fuel deposit must outlast living tissue by orders of magnitude"
    assert t["Sedimentary rock"] > t["Soil organic matter"], \
        "'soil holds carbon longer than sedimentary rock' must be false"
    assert min(t, key=t.get) != "Deep ocean water", \
        "'deep ocean water is the shortest of the five' must be false"
    assert len(set(t.values())) == len(t), "'all five hold carbon for the same time' must be false"
    return (f"the residence times run from {min(t.values()):.0f} to {max(t.values()):.0f} "
            "years, with fossil fuel deposits at the top and living plant tissue at the bottom")


def q5(table, item):
    t = dict(zip(cg.labels(table), cg.col(table, STAY)))
    two_shortest = sorted(t, key=t.get)[:2]
    assert set(two_shortest) == {"Soil organic matter", "Living plant tissue"}, \
        f"the two shortest reservoirs must be soil and living tissue; got {two_shortest}"
    assert all(t[k] < 100 for k in two_shortest), "both must return carbon within decades"
    assert t["Soil organic matter"] < t["Sedimentary rock"], \
        "'soil outlasts sedimentary rock' must be false"
    assert t["Living plant tissue"] < t["Deep ocean water"], \
        "'living tissue outlasts deep ocean water' must be false"
    assert t["Fossil fuel deposits"] > t["Living plant tissue"], \
        "'fossil fuel carbon returns faster than living tissue carbon' must be false"
    return (f"the two shortest residence times are {t['Soil organic matter']:.0f} and "
            f"{t['Living plant tissue']:.0f} years, both within decades")


def q11(table, item):
    f = dict(zip(cg.labels(table), cg.col(table, MOVED)))
    photo = f["Photosynthesis on land and in the sea"]
    resp = f["Cellular respiration and decomposition"]
    fossil = f["Burning of fossil fuels"]
    assert abs(photo - resp) < 0.1 * min(photo, resp), \
        f"photosynthesis and return must be close in size; got {photo} and {resp}"
    assert fossil < 0.2 * min(photo, resp), "combustion must be far smaller than either"
    assert fossil != max(f.values()), "'combustion is the largest transfer' must be false"
    assert resp > 0, "'respiration and decomposition move no carbon' must be false"
    assert len(set(f.values())) == len(f), "'all three are equal' must be false"
    return (f"photosynthesis {photo:.0f} and return {resp:.0f} billion tonnes differ by "
            f"{abs(photo - resp):.0f}, while combustion moves {fossil:.0f}")


def q12(table, item):
    co2 = cg.col(table, PPM)
    emit = cg.col(table, EMIT)
    assert all(co2[i + 1] > co2[i] for i in range(len(co2) - 1)), f"carbon dioxide must rise; got {co2}"
    assert all(emit[i + 1] > emit[i] for i in range(len(emit) - 1)), f"emissions must rise; got {emit}"
    return (f"carbon dioxide rises {co2[0]:.0f} to {co2[-1]:.0f} parts per million while "
            f"emissions rise {emit[0]} to {emit[-1]} billion tonnes a year")


def q13(table, item):
    p = dict(zip(cg.labels(table), cg.col(table, STORED)))
    total = sum(p.values())
    top2 = p["Living trees"] + p["Soil organic matter"]
    assert top2 / total > 0.8, f"the two largest pools must exceed four fifths; got {top2 / total:.2f}"
    assert p["Leaf litter"] < p["Living trees"], "'litter holds more than trees' must be false"
    assert max(p, key=p.get) != "Dead wood on the ground", "'dead wood is the largest pool' must be false"
    assert max(p.values()) > 2 * (total / 4), "'each pool is about a quarter' must be false"
    assert p["Soil organic matter"] > 0, "'soil holds no carbon' must be false"
    return (f"living trees and soil hold {top2:.0f} of the {total:.0f} tonnes per hectare "
            f"tabulated, which is {100 * top2 / total:.0f} percent")


def q14(table, item):
    left = cg.col(table, LEFT)
    assert all(left[i + 1] > left[i] for i in range(len(left) - 1)), \
        f"retention must rise from the softest litter to the woodiest; got {left}"
    assert left[0] < left[-1], "'branches lose carbon faster than soft leaves' must be false"
    assert max(left) < 100, "'no litter lost any carbon' must be false"
    assert left[1] > left[0], "'needles retained less than soft leaves' must be false"
    return (f"the share still present after two years rises {left} from soft leaves to "
            "whole branches, so the four materials release carbon at different rates")


def q15(table, item):
    b = dict(zip(cg.labels(table), cg.col(table, BURIED)))
    k = dict(zip(cg.labels(table), cg.col(table, KEPT)))
    peat = "Waterlogged peat basin"
    assert max(b, key=b.get) == peat and max(k, key=k.get) == peat, \
        "the peat basin must lead on both columns"
    assert b[peat] != b["Well-drained upland soil"], "'the two bury the same amount' must be false"
    assert min(k.values()) > 0, "'neither retains any carbon' must be false"
    return (f"the peat basin buries {b[peat]:.0f} grams per square meter against "
            f"{b['Well-drained upland soil']:.0f} and keeps {k[peat]:.0f} percent against "
            f"{k['Well-drained upland soil']:.0f} percent")


def q16(table, item):
    w = dict(zip(cg.labels(table), cg.col(table, WOOD)))
    r = dict(zip(cg.labels(table), cg.col(table, RELEASED)))
    cut, uncut = "Stand cut and burned", "Uncut stand"
    drop = w[uncut] - w[cut]
    assert drop > 0, "the cut stand must have lost living wood carbon"
    assert r[cut] > r[uncut], "'the cut stand released less' must be false"
    assert abs(r[cut] - drop) < 0.2 * drop, \
        f"the carbon released {r[cut]} must account for most of the drop {drop}"
    assert w[cut] < w[uncut], "'the cut stand still holds more living wood' must be false"
    return (f"living wood carbon falls by {drop:.0f} tonnes per hectare while "
            f"{r[cut]:.0f} tonnes per hectare are released to the air in the same year")


def q17(table, item):
    age = dict(zip(cg.labels(table), cg.col(table, AGE)))
    burn = dict(zip(cg.labels(table), cg.col(table, BURNTIME)))
    assert len(set(burn.values())) == 1, f"the release times must be identical; got {burn}"
    coal = "Coal from a deep seam"
    assert age[coal] == max(age.values()) and age[coal] > 1e6 * min(age.values()), \
        "coal must hold by far the oldest carbon"
    assert max(burn.values()) < 1, "'none releases its carbon within a year' must be false"
    assert age["Dried grass in a field fire"] < age[coal], \
        "'burning grass returns older carbon than coal' must be false"
    return (f"every material releases its carbon in {list(burn.values())[0]} years while "
            f"the ages span {min(age.values()):.0f} to {max(age.values()):.0f} years")


CLAIMS = [
 ("between sources and sinks",
  "ERT-1.D.1, near verbatim: the carbon cycle is the movement of atoms and molecules containing the element carbon between sources and sinks. Movement, not creation or destruction, is the content of that sentence."),
 ("moved into the atmosphere as carbon dioxide",
  "ERT-1.D.1 makes the cycle a movement between reservoirs, and ERT-1.D.4 states specifically that burning fossil fuels moves stored carbon into atmospheric carbon in the form of carbon dioxide. Nothing in the framework destroys a carbon atom."),
 ("relatively short periods",
  "ERT-1.D.2, near verbatim: some of the reservoirs in which carbon compounds occur hold those compounds for long periods of time, while some hold them for relatively short periods of time."),
 ("long-term store and living plant tissue",
  "Recomputed in q4 above: the tabulated residence times span more than seven orders of magnitude, with fossil fuel deposits at the top and living plant tissue at the bottom. ERT-1.D.2 is the statement that reservoirs differ in how long they hold carbon."),
 ("within decades",
  "Recomputed in q5 above: the two shortest tabulated residence times are both measured in tens of years, which is what makes them the short-period reservoirs ERT-1.D.2 sets against the long-period ones."),
 ("Photosynthesis and cellular respiration",
  "ERT-1.D.3, near verbatim: carbon cycles between photosynthesis and cellular respiration in living things. The rejected pairs belong to the nitrogen cycle, the water cycle, and rock processes."),
 ("Photosynthesis",
  "ERT-1.D.3 places photosynthesis and cellular respiration at the two ends of the living carbon cycle, and ENG-1.A.1 defines primary productivity as the conversion of solar energy into organic compounds via photosynthesis, which identifies photosynthesis as the intake step."),
 ("Cellular respiration",
  "ERT-1.D.3 names photosynthesis and cellular respiration as the pair between which carbon cycles in living things, and ENG-1.A.1 makes photosynthesis the process that BUILDS organic compounds, leaving respiration as the return step."),
 ("Plant and animal decomposition",
  "ERT-1.D.4, near verbatim: plant and animal decomposition have led to the storage of carbon over millions of years. Combustion is the release step in the same statement, not the storage step."),
 ("quickly moves that stored carbon",
  "ERT-1.D.4, near verbatim: the burning of fossil fuels quickly moves that stored carbon into atmospheric carbon, in the form of carbon dioxide. The word quickly is the framework's own and is what sets combustion against the slow storage step."),
 ("close to each other in size",
  "Recomputed in q11 above: the photosynthesis and return figures differ by a small fraction of either while the combustion figure is far below both. ERT-1.D.3 pairs the first two as the living cycle and ERT-1.D.4 adds combustion as a separate transfer out of long-term storage."),
 ("Both quantities rose",
  "Recomputed in q12 above: both tabulated columns increase across the four decades. ERT-1.D.4 states that burning fossil fuels quickly moves stored carbon into atmospheric carbon dioxide, which is the direction the data run."),
 ("more than four fifths",
  "Recomputed in q13 above: the two largest pools sum to more than four fifths of the tabulated total. ERT-1.D.2 is the framework statement that carbon occupies reservoirs of different kinds, which is what a pool inventory records."),
 ("Softer litter loses its carbon faster",
  "Recomputed in q14 above: the share of carbon still present after two years rises from the softest material to the woodiest. ERT-1.D.2 is the statement that holding times differ between reservoirs."),
 ("retains a far larger share",
  "Recomputed in q15 above: the waterlogged basin leads both tabulated columns. ERT-1.D.4 attributes long-term carbon storage to plant and animal decomposition, and ERT-1.D.2 allows reservoirs to differ in how long they hold it."),
 ("in a single year",
  "Recomputed in q16 above: the fall in living wood carbon and the carbon released to the air in the same year are of comparable size. ERT-1.D.1 makes the cycle a movement between reservoirs rather than a loss of atoms."),
 ("whatever its age",
  "Recomputed in q17 above: the release-time column is identical across the three materials while the age column spans hundreds of millions of years. ERT-1.D.4 draws exactly this contrast between slow storage and quick combustion."),
 ("carbon taken up recently",
  "ERT-1.D.4 sets storage over millions of years against a quick return by combustion, so what distinguishes the two cases is the age of the carbon and the speed of its release, not whether carbon dioxide is produced."),
 ("into which carbon moves",
  "ERT-1.D.1 describes the carbon cycle as movement between sources and sinks, which pairs a place carbon leaves with a place carbon enters. Nothing in the framework has carbon atoms destroyed or turned into another element."),
 ("Less carbon is taken up by photosynthesis",
  "ERT-1.D.3 makes photosynthesis the uptake step of the living carbon cycle, so removing the photosynthesizers removes the uptake, and ERT-1.D.1 makes the burning a movement of that carbon into another reservoir rather than a loss."),
 ("after very long spans",
  "ERT-1.D.2 distinguishes reservoirs by how long they hold carbon compounds, so the evidence that bears on the distinction is retention measured over time. A large standing mass or a great depth says nothing about holding time."),
 ("it does not add carbon",
  "ERT-1.D.1 defines the cycle as movement of carbon-containing atoms and molecules between sources and sinks, so an increase in one reservoir is a transfer out of another rather than the appearance of new carbon."),
 ("Photosynthesis moves carbon out of the atmosphere",
  "ERT-1.D.3 makes photosynthesis the step that builds organic compounds and ERT-1.D.4 states that burning fossil fuels moves stored carbon into atmospheric carbon dioxide, so the two processes run in opposite directions."),
 ("combustion quickly returns it",
  "ERT-1.D.4 carries both halves of the sequence: plant and animal decomposition led to storage over millions of years, and burning fossil fuels quickly moves that stored carbon into atmospheric carbon dioxide."),
 ("some for relatively short periods",
  "The two soils are matched on the quantity of carbon and differ only in how long they keep it, which is exactly the distinction ERT-1.D.2 draws between long-period and short-period reservoirs."),
 ("than leaves them",
  "ERT-1.D.1 makes a sink a destination in the movement of carbon between sources and sinks, so the relevant measurement is the balance of carbon entering against carbon leaving over a period."),
 ("is a source and a growing forest is a sink",
  "ERT-1.D.4 has combustion moving stored carbon into the atmosphere, which makes a burning seam a source, and ERT-1.D.3 has photosynthesis building organic compounds in growing plants, which makes a growing forest a destination."),
 ("accumulating over those spans",
  "ERT-1.D.4 states that plant and animal decomposition have led to the storage of carbon over millions of years, so the timescale belongs to the accumulation of decomposed material rather than to any property of the atoms."),
 ("exchanges rapidly",
  "ERT-1.D.1 makes the cycle a redistribution between reservoirs and ERT-1.D.2 makes reservoirs differ in holding time, so a transfer from a slow reservoir to a fast one raises the content of the fast one without changing the total."),
 ("into a plant by photosynthesis",
  "ERT-1.D.3 states that carbon cycles between photosynthesis and cellular respiration in living things, and ENG-1.A.1 makes photosynthesis the step that builds organic compounds, leaving respiration as the return."),
]

TABLE_CHECKS = {4: q4, 5: q5, 11: q11, 12: q12, 13: q13, 14: q14,
                15: q15, 16: q16, 17: q17}


def _selftest():
    """Negative control: every gate below must FAIL when its input is corrupted."""
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("e1_4_mutant")
        mod.TOPIC = e1_4.TOPIC
        mod.QUESTIONS = copy.deepcopy(e1_4.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[5]["ans"] = 1

    def break_anchor(mod, claims):
        claims[9] = ("no such phrase anywhere in the module", claims[9][1])

    def corrupt_table(mod, claims):
        # make combustion the largest annual transfer
        mod.QUESTIONS[10]["table"] = dict(
            headers=e1_4._T_FLUX["headers"],
            rows=[[p, ("900" if p == "Burning of fossil fuels" else v)]
                  for p, v in e1_4._T_FLUX["rows"]])

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[8]["choices"][4] = mod.QUESTIONS[8]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[17]["why"] = "It just is."

    def letter_reference(mod, claims):
        mod.QUESTIONS[22]["why"] = ("Choice B is wrong because the framework says so and "
                                    "the rest of the reasoning follows from that.")

    def latex_slips_in(mod, claims):
        mod.QUESTIONS[0]["choices"][4] = "It moves \\frac{1}{2} of the carbon only"
        style(mod)

    def range_slips_in(mod, claims):
        mod.QUESTIONS[2]["q"] = "Over 1960-2010 what does the framework say about reservoirs?"
        style(mod)

    print("negative controls:")
    must_fail("a backslash macro in a choice", latex_slips_in)
    must_fail("a digit-hyphen-digit range in a stem", range_slips_in)
    must_fail("key moved off its anchor", move_key)
    must_fail("anchor no longer in the keyed choice", break_anchor)
    must_fail("table value corrupted so the keyed conclusion is false", corrupt_table)
    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a why reduced below the minimum", thin_why)
    must_fail("a why naming an option by letter", letter_reference)
    print("all negative controls raised as required.")


import e1_4  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(e1_4)
cg.check(e1_4, CLAIMS, table_checks=TABLE_CHECKS)
