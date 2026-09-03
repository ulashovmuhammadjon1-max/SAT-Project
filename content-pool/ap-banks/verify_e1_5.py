"""Key audit for AP ENVIRONMENTAL SCIENCE 1.5 The Nitrogen Cycle.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Items 1, 9, 18 and 24 rest on ERT-1.E.1: the nitrogen cycle involves several
steps, including nitrogen fixation, assimilation, ammonification, nitrification
and denitrification, and microorganisms in the soil play an important role in
many of these steps.

Items 2, 3, 4, 13, 15, 16, 19, 23 and 27 rest on ERT-1.E.2: in nitrogen
fixation, atmospheric nitrogen is converted by certain types of soil bacteria
into ammonia, and in the soil ammonia quickly converts to ammonium, which is
available for biological uptake.

Items 5, 6, 12, 14, 17, 20, 21, 22, 25 and 30 rest on ERT-1.E.3: the
availability of nitrogen compounds in the soil is limited by the rate of
nitrogen fixation, and in many ecosystems the availability of nitrogen compounds
limits primary production by plants and other producers.

Items 7, 8, 10, 11, 22, 26, 28 and 29 rest on ERT-1.E.4: the largest reservoir
of nitrogen is the atmosphere, and MOST of the reservoirs in which nitrogen
compounds occur hold those compounds for relatively short periods of time. The
word "most" is part of that claim, so no item keys a statement about every
reservoir.

WHAT IS DELIBERATELY NOT ASKED. Assimilation, ammonification, nitrification and
denitrification are NAMED by the framework and defined nowhere in it, so no key
here rests on what any of the four does, and no item asks for an order of the
steps -- ERT-1.E.1 writes "several steps, including", which is a list.

DATA ITEMS: 10 to 17 carry tables. Each keyed conclusion is recomputed below
from that table alone, and each check also falsifies the distractors against the
same numbers.

NEGATIVE CONTROL: ``python3 verify_e1_5.py --selftest`` corrupts a key, an
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


HELD = "Nitrogen held (billions of tonnes)"
STAY = "Average time nitrogen stays in the reservoir (years)"
ADDED = "Nitrogen added each year (kilograms per hectare)"
MASS = "Plant mass grown each year (kilograms per hectare)"
FIXED30 = "Nitrogen fixed in thirty days (milligrams per kilogram of soil)"
FIXYR = "Nitrogen fixed each year (kilograms per hectare)"
AVAIL = "Nitrogen available in the soil (kilograms per hectare)"
NH3 = "Ammonia remaining (milligrams per kilogram)"
NH4 = "Ammonium present (milligrams per kilogram)"
START = "Nitrogen in the soil at the start (kilograms per hectare)"
END = "Nitrogen in the soil after three seasons (kilograms per hectare)"
GROWN = "Plant mass grown (kilograms per hectare)"


def q10(table, item):
    r = dict(zip(cg.labels(table), cg.col(table, HELD)))
    atm = r["Atmosphere"]
    others = sum(v for k, v in r.items() if k != "Atmosphere")
    assert atm > 100 * others, f"the atmosphere must dwarf the rest; got {atm} against {others}"
    assert r["Ocean water"] < atm, "'ocean water holds more than the atmosphere' must be false"
    assert max(r, key=r.get) == "Atmosphere", "the atmosphere must be the largest reservoir"
    assert r["Rivers and lakes"] < r["Soil organic matter"], \
        "'rivers and lakes hold more than soil organic matter' must be false"
    return (f"the atmosphere holds {atm:.0f} billion tonnes against {others:.0f} for the "
            "other four reservoirs combined")


def q11(table, item):
    t = dict(zip(cg.labels(table), cg.col(table, STAY)))
    short = [k for k, v in t.items() if v <= 10]
    assert len(short) == len(t) - 1, f"all but one reservoir must hold nitrogen briefly; got {t}"
    assert "Atmosphere" not in short, "the atmosphere must be the long-lived exception"
    assert t["Soil ammonium"] < t["Atmosphere"], \
        "'soil ammonium outlasts the atmosphere' must be false"
    assert min(t, key=t.get) != "Ocean surface water", \
        "'ocean surface water is the shortest of the five' must be false"
    return (f"{len(short)} of the {len(t)} tabulated reservoirs hold nitrogen for ten years "
            f"or less; only the atmosphere, at {t['Atmosphere']:.0f} years, does not")


def q12(table, item):
    pairs = sorted(zip(cg.col(table, ADDED), cg.col(table, MASS)))
    assert all(pairs[i + 1][1] > pairs[i][1] for i in range(len(pairs) - 1)), \
        f"plant mass must rise with nitrogen added; got {pairs}"
    assert pairs[0][1] == min(m for _, m in pairs), "'the unfertilized plot grew the most' must be false"
    assert pairs[-1][1] > 2 * pairs[0][1], "the response must be substantial, not marginal"
    return (f"sorted by nitrogen added the plant mass reads {[m for _, m in pairs]}, "
            "strictly increasing and more than doubling across the range")


def q13(table, item):
    f = dict(zip(cg.labels(table), cg.col(table, FIXED30)))
    live, dead = "Untreated soil", "Soil heated to kill microorganisms"
    back = "Heated soil with microorganisms added back"
    assert f[dead] < 0.1 * f[live], f"heating must nearly stop fixation; got {f}"
    assert f[back] > 0.8 * f[live], "restoring the microorganisms must restore fixation"
    assert f[dead] != max(f.values()), "'heating increased fixation' must be false"
    assert f[back] > f[dead], "'adding microorganisms back reduced fixation further' must be false"
    assert len(set(f.values())) > 1, "'all three treatments fixed the same amount' must be false"
    return (f"fixation falls from {f[live]:.0f} to {f[dead]:.0f} milligrams per kilogram "
            f"when the soil is heated and returns to {f[back]:.0f} when microorganisms are "
            "added back")


def q14(table, item):
    pairs = sorted(zip(cg.col(table, FIXYR), cg.col(table, AVAIL)))
    assert all(pairs[i + 1][1] > pairs[i][1] for i in range(len(pairs) - 1)), \
        f"available nitrogen must rise with fixation; got {pairs}"
    assert pairs[0][1] != max(a for _, a in pairs), \
        "'the site fixing least holds the most available nitrogen' must be false"
    assert len(set(f for f, _ in pairs)) == len(pairs), "'fixation is the same at all sites' must be false"
    return (f"sorted by nitrogen fixed the available soil nitrogen reads "
            f"{[a for _, a in pairs]}, strictly increasing across the four sites")


def q15(table, item):
    hours = [cg.num(r[0]) for r in table["rows"]]
    nh3 = cg.col(table, NH3)
    nh4 = cg.col(table, NH4)
    assert all(hours[i + 1] > hours[i] for i in range(len(hours) - 1)), "rows must run forward in time"
    assert all(nh3[i + 1] < nh3[i] for i in range(len(nh3) - 1)), f"ammonia must fall; got {nh3}"
    assert all(nh4[i + 1] > nh4[i] for i in range(len(nh4) - 1)), f"ammonium must rise; got {nh4}"
    six = hours.index(6)
    assert (nh3[0] - nh3[six]) > 0.8 * (nh3[0] - nh3[-1]), \
        "most of the conversion must happen within the first six hours"
    assert max(hours) <= 24, "the record must not extend beyond a day, so 'many years' is false"
    return (f"ammonia falls {nh3} while ammonium rises {nh4}, with most of the change "
            "complete within six hours")


def q16(table, item):
    s = dict(zip(cg.labels(table), cg.col(table, START)))
    e = dict(zip(cg.labels(table), cg.col(table, END)))
    fixer = "Planted with a nitrogen-fixing crop"
    other = "Planted with a crop that fixes no nitrogen"
    assert s[fixer] == s[other], "'the two plots started differently' must be false"
    assert e[fixer] > s[fixer], "the fixing crop's plot must gain nitrogen"
    assert e[other] < s[other], "the other plot must lose nitrogen"
    return (f"both plots start at {s[fixer]:.0f} kilograms per hectare; the fixing crop's "
            f"plot rises to {e[fixer]:.0f} and the other falls to {e[other]:.0f}")


def q17(table, item):
    g = dict(zip(cg.labels(table), cg.col(table, GROWN)))
    base = g["Nothing added"]
    assert g["Nitrogen only"] > 2 * base, f"nitrogen must produce a large increase; got {g}"
    for other in ("Phosphorus only", "Potassium only"):
        assert abs(g[other] - base) < 0.2 * base, f"{other} must change little from the control"
        assert g[other] < g["Nitrogen only"], f"{other} must not match the nitrogen response"
    return (f"nitrogen raises plant mass from {base:.0f} to {g['Nitrogen only']:.0f} while "
            f"phosphorus and potassium give {g['Phosphorus only']:.0f} and "
            f"{g['Potassium only']:.0f}")


CLAIMS = [
 ("assimilation, ammonification",
  "ERT-1.E.1, near verbatim: the nitrogen cycle involves several steps, including nitrogen fixation, assimilation, ammonification, nitrification, and denitrification. The rejected lists belong to the water cycle, the carbon cycle, soil formation and plate tectonics."),
 ("soil bacteria into ammonia",
  "ERT-1.E.2, near verbatim: in nitrogen fixation, atmospheric nitrogen is converted by certain types of soil bacteria into ammonia. The direction of the conversion and the identity of the agent are both in that sentence."),
 ("converts to ammonium, which is available",
  "ERT-1.E.2, near verbatim: in the soil, ammonia quickly converts to ammonium, which is available for biological uptake. Both the speed and the availability of the product are stated."),
 ("Ammonium",
  "ERT-1.E.2 identifies ammonium as the form available for biological uptake and attaches that description to no other form of nitrogen."),
 ("rate of nitrogen fixation",
  "ERT-1.E.3, near verbatim: the availability of nitrogen compounds in the soil is limited by the rate of nitrogen fixation, so it is that rate rather than the size of any store that sets availability."),
 ("Primary production by plants and other producers",
  "ERT-1.E.3, near verbatim: in many ecosystems, the availability of nitrogen compounds limits primary production by plants and other producers."),
 ("The atmosphere",
  "ERT-1.E.4 states plainly that the largest reservoir of nitrogen is the atmosphere, and assigns that rank to none of the rejected reservoirs."),
 ("relatively short periods of time",
  "ERT-1.E.4 states that most of the reservoirs in which nitrogen compounds occur hold those compounds for relatively short periods of time. The word most is part of the claim, so it is not a statement about every reservoir."),
 ("important role in many of the steps",
  "ERT-1.E.1 states that microorganisms in the soil play an important role in many of the steps of the nitrogen cycle, and ERT-1.E.2 names certain types of soil bacteria as the agents of fixation."),
 ("all the other reservoirs listed",
  "Recomputed in q10 above: the atmospheric figure exceeds the sum of the other four by more than two orders of magnitude. That is the quantitative form of ERT-1.E.4's claim that the largest reservoir of nitrogen is the atmosphere."),
 ("the atmosphere the exception",
  "Recomputed in q11 above: four of the five tabulated holding times are ten years or less and only the atmosphere is long. ERT-1.E.4 states that MOST nitrogen reservoirs hold their compounds for relatively short periods."),
 ("rises as nitrogen is added",
  "Recomputed in q12 above: plant mass increases at every step up the nitrogen addition column and more than doubles across it. ERT-1.E.3 states that the availability of nitrogen compounds limits primary production in many ecosystems."),
 ("killing them almost stopped it",
  "Recomputed in q13 above: fixation collapsed when the soil was heated and recovered when microorganisms were returned. ERT-1.E.2 names certain types of soil bacteria as the agents of nitrogen fixation."),
 ("also hold more available nitrogen",
  "Recomputed in q14 above: sorting the sites by nitrogen fixed leaves available soil nitrogen strictly increasing. ERT-1.E.3 states that soil nitrogen availability is limited by the rate of nitrogen fixation."),
 ("Ammonia was converted to ammonium within hours",
  "Recomputed in q15 above: ammonia falls and ammonium rises, with most of the change complete within six hours. ERT-1.E.2 states that in the soil ammonia quickly converts to ammonium."),
 ("while the other plot lost it",
  "Recomputed in q16 above: the two plots begin at the same value and move in opposite directions, with the fixing crop's plot rising. ERT-1.E.2 makes fixation the route by which atmospheric nitrogen becomes available in the soil."),
 ("Nitrogen was the nutrient limiting",
  "Recomputed in q17 above: only the nitrogen treatment raised plant mass substantially above the untreated value. ERT-1.E.3 states that in many ecosystems the availability of nitrogen compounds limits primary production."),
 ("Transpiration",
  "ERT-1.E.1 lists nitrogen fixation, assimilation, ammonification, nitrification and denitrification. The keyed term belongs to the movement of water and appears on no nitrogen list in the framework."),
 ("makes ammonium, not atmospheric nitrogen",
  "ERT-1.E.2 identifies ammonium as the form available for biological uptake and makes fixation the step that produces it from atmospheric nitrogen, while ERT-1.E.4 makes the atmosphere the largest reservoir, so scarcity of supply is not the obstacle."),
 ("primary production could fall with it",
  "ERT-1.E.3 makes the rate of nitrogen fixation the limit on soil nitrogen availability and makes that availability a limit on primary production in many ecosystems, so removing the fixing bacteria removes the supply at its source."),
 ("Add nitrogen to some plots",
  "ERT-1.E.3 states that the availability of nitrogen compounds limits primary production in many ecosystems, and a limiting factor is tested by relieving the limit in some plots and comparing them against untreated ones."),
 ("not by the size of the atmospheric store",
  "ERT-1.E.4 grants that the atmosphere is the largest nitrogen reservoir, but ERT-1.E.3 states that soil availability is limited by the rate of nitrogen fixation, so a large store can sit behind a slow gateway."),
 ("and the ammonia converts to ammonium",
  "ERT-1.E.2 gives the order directly: atmospheric nitrogen is converted by soil bacteria into ammonia, and in the soil ammonia quickly converts to ammonium, which is available for biological uptake."),
 ("resume when they are restored",
  "ERT-1.E.1 states that microorganisms in the soil play an important role in many of the steps of the nitrogen cycle, and the way to show a living agent is responsible is to remove it and restore it while watching the process."),
 ("cannot exceed what the available nitrogen supports",
  "ERT-1.E.3 says that in many ecosystems the availability of nitrogen compounds LIMITS primary production, which is a ceiling on what producers can achieve rather than a claim that nitrogen alone determines the outcome."),
 ("most other reservoirs hold nitrogen",
  "ERT-1.E.4 makes two claims at once: the largest reservoir of nitrogen is the atmosphere, and most of the reservoirs in which nitrogen compounds occur hold them for relatively short periods of time."),
 ("into a form that becomes available",
  "ERT-1.E.2 states that nitrogen fixation converts atmospheric nitrogen into ammonia, which quickly becomes ammonium available for biological uptake, and that is the only route the framework gives from the air into the soil."),
 ("hold those compounds for relatively short periods",
  "ERT-1.E.4 states that most nitrogen reservoirs hold their compounds for relatively short periods of time, so a soil pool that empties within weeks is an instance of that general claim rather than an anomaly."),
 ("fixation is what makes some of it available",
  "ERT-1.E.4 makes the atmosphere the largest reservoir and ERT-1.E.2 makes fixation the conversion of atmospheric nitrogen into ammonia and then ammonium, so one is a place and the other is a process."),
 ("rather than water, was limiting",
  "Production did not respond to extra water but did respond once a source of fixed nitrogen appeared, and ERT-1.E.3 states that in many ecosystems the availability of nitrogen compounds limits primary production by plants and other producers."),
]

TABLE_CHECKS = {10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16, 17: q17}


def _selftest():
    """Negative control: every gate below must FAIL when its input is corrupted."""
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("e1_5_mutant")
        mod.TOPIC = e1_5.TOPIC
        mod.QUESTIONS = copy.deepcopy(e1_5.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[6]["ans"] = 3

    def break_anchor(mod, claims):
        claims[4] = ("no such phrase anywhere in the module", claims[4][1])

    def corrupt_table(mod, claims):
        # let the heated soil out-fix the untreated soil
        mod.QUESTIONS[12]["table"] = dict(
            headers=e1_5._T_STERILE["headers"],
            rows=[[t, ("99" if t.startswith("Soil heated") else v)]
                  for t, v in e1_5._T_STERILE["rows"]])

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[1]["choices"][3] = mod.QUESTIONS[1]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[20]["why"] = "It just is."

    def letter_reference(mod, claims):
        mod.QUESTIONS[25]["why"] = ("Option A is wrong because the framework says so and "
                                    "the rest of the reasoning follows from that.")

    def latex_slips_in(mod, claims):
        mod.QUESTIONS[3]["choices"][4] = "Nitrogen dissolved as \\mathrm{N_2} gas"
        style(mod)

    def range_slips_in(mod, claims):
        mod.QUESTIONS[8]["q"] = "Across 1970-1990 what role did microorganisms play in the soil?"
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


import e1_5  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(e1_5)
cg.check(e1_5, CLAIMS, table_checks=TABLE_CHECKS)
