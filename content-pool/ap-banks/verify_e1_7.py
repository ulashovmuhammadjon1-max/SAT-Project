"""Key audit for AP ENVIRONMENTAL SCIENCE 1.7 The Hydrologic (Water) Cycle.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
This topic has only TWO essential knowledge statements, so every key traces to
one or both of them and to nothing else.

ERT-1.G.1 -- the hydrologic cycle, which is powered by the sun, is the movement
of water in its various solid, liquid, and gaseous phases between sources and
sinks -- carries items 1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 22, 23,
24, 27, 28, 29 and 30.

ERT-1.G.2 -- the oceans are the primary reservoir of water at the Earth's
surface, with ice caps and groundwater acting as much smaller reservoirs --
carries items 3, 4, 5, 6, 15, 17, 19, 21, 25, 26 and 29.

THE PHASE ITEMS. Items 9, 11, 12, 16, 19 and 28 turn on which phase a named body
of water is in. The framework names the three phases and identifies none of them
with a substance, so the presupposed content is only the minimum that naming
three phases requires: ice is the solid phase, liquid water the liquid phase,
water vapor the gaseous phase. Nothing beyond that is keyed, and the framework
does NOT name evaporation, condensation, precipitation, runoff, infiltration or
transpiration in this topic, so no item asks for those terms.

DATA ITEMS: 5, 6, 7, 8, 9, 10, 17, 18 and 19 carry tables. Each keyed conclusion
is recomputed below from that table alone, and each check also falsifies the
distractors against the same numbers.

NEGATIVE CONTROL: ``python3 verify_e1_7.py --selftest`` corrupts a key, an
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


WHELD = "Water held (thousands of cubic kilometers)"
SUN = "Sunlight received each day (megajoules per square meter)"
EVAP = "Water evaporated each day (millimeters)"
TANK = "Water evaporated from an open tank (millimeters)"
SNOWPACK = "Water held as snow on the ground (millimeters)"
STREAM = "Water leaving the basin in the stream (millimeters)"
CAPACITY = "Greatest mass of water vapor the air can hold (grams per cubic meter)"
SHARE = "Share of all the water on Earth (percent)"
FALL = "Rain and snow falling on the basin (millimeters)"
VAPOUT = "Water leaving as vapor (millimeters)"
RIVEROUT = "Water leaving in the river (millimeters)"
ICE = "Water stored in one region's ice caps (cubic kilometers)"
SUMMER = "Mean summer air temperature (degrees Celsius)"


def q5(table, item):
    r = dict(zip(cg.labels(table), cg.col(table, WHELD)))
    ocean = r["Oceans"]
    others = sum(v for k, v in r.items() if k != "Oceans")
    assert ocean > 10 * others, f"the oceans must dwarf the rest; got {ocean} against {others}"
    assert max(r, key=r.get) == "Oceans", "the oceans must be the largest reservoir"
    assert r["Atmosphere"] < r["Lakes and rivers"], \
        "'the atmosphere holds more than lakes and rivers' must be false"
    return (f"the oceans hold {ocean:.0f} thousand cubic kilometers against {others:.0f} "
            "for the other four reservoirs combined")


def q6(table, item):
    r = dict(zip(cg.labels(table), cg.col(table, WHELD)))
    ocean, lakes = r["Oceans"], r["Lakes and rivers"]
    for mid in ("Ice caps and glaciers", "Groundwater"):
        assert r[mid] < 0.05 * ocean, f"{mid} must be far below the oceans"
        assert r[mid] > 20 * lakes, f"{mid} must be far above lakes and rivers"
    assert r["Ice caps and glaciers"] + r["Groundwater"] < ocean, \
        "'ice caps and groundwater together exceed the oceans' must be false"
    return (f"ice caps hold {r['Ice caps and glaciers']:.0f} and groundwater "
            f"{r['Groundwater']:.0f} thousand cubic kilometers, between the oceans at "
            f"{ocean:.0f} and lakes and rivers at {lakes:.0f}")


def q7(table, item):
    pairs = sorted(zip(cg.col(table, SUN), cg.col(table, EVAP)))
    assert all(pairs[i + 1][1] > pairs[i][1] for i in range(len(pairs) - 1)), \
        f"evaporation must rise with sunlight; got {pairs}"
    assert pairs[0][1] != max(e for _, e in pairs), \
        "'the least sunlit site evaporated the most' must be false"
    assert len(set(s for s, _ in pairs)) == len(pairs), "'all sites received the same sunlight' must be false"
    return (f"sorted by sunlight the daily evaporation reads {[e for _, e in pairs]} "
            "millimeters, strictly increasing across the four sites")


def q8(table, item):
    v = dict(zip(cg.labels(table), cg.col(table, TANK)))
    day = [v["Sunrise to midday"], v["Midday to sunset"]]
    night = [v["Sunset to midnight"], v["Midnight to sunrise"]]
    assert min(day) > 3 * max(night), f"daylight loss must far exceed night loss; got {v}"
    assert min(day) > 0, "'no water left during daylight' must be false"
    assert max(v, key=v.get) not in ("Sunset to midnight", "Midnight to sunrise"), \
        "'a dark period lost the most' must be false"
    assert len(set(v.values())) > 1, "'the same amount left in each period' must be false"
    return (f"the daylight periods lost {day} millimeters against {night} in the dark, "
            "more than three times as much in the smaller daylight period alone")


def q9(table, item):
    snow = cg.col(table, SNOWPACK)
    flow = cg.col(table, STREAM)
    assert all(snow[i + 1] < snow[i] for i in range(len(snow) - 1)), f"snow must decline; got {snow}"
    assert snow[-1] == 0, "the snow store must empty by the end of the record"
    peak = flow.index(max(flow))
    assert peak != snow.index(max(snow)), \
        "'the stream peaks in the month with the most snow' must be false"
    assert max(flow) > 0, "'no water left in the stream' must be false"
    assert flow != sorted(flow), "'both snow and stream flow rose' must be false"
    return (f"snow on the ground falls {snow} to nothing while stream flow {flow} peaks as "
            "it does so")


def q10(table, item):
    temps = [cg.num(r[0]) for r in table["rows"]]
    cap = cg.col(table, CAPACITY)
    assert all(temps[i + 1] > temps[i] for i in range(len(temps) - 1)), "rows must ascend in temperature"
    assert all(cap[i + 1] > cap[i] for i in range(len(cap) - 1)), f"capacity must rise; got {cap}"
    assert cap[0] == min(cap), "'the coldest air holds the most vapor' must be false"
    return (f"as temperature rises {temps} degrees the capacity rises {cap} grams per cubic "
            "meter at every step")


def q17(table, item):
    s = dict(zip(cg.labels(table), cg.col(table, SHARE)))
    ocean = s["Salt water in the oceans"]
    assert ocean > 90, f"the oceanic share must be the great majority; got {ocean}"
    for k, v in s.items():
        if k != "Salt water in the oceans":
            assert v < 2, f"{k} must be a small share; got {v}"
    assert max(s, key=s.get) == "Salt water in the oceans", "the oceans must hold the largest share"
    return (f"the oceans hold {ocean} percent of the Earth's water while every freshwater "
            f"category is below {max(v for k, v in s.items() if k != 'Salt water in the oceans')} "
            "percent")


def q18(table, item):
    vap = cg.col(table, VAPOUT)
    riv = cg.col(table, RIVEROUT)
    fall = cg.col(table, FALL)
    assert all(v > 0 for v in vap), f"vapor loss must be positive every year; got {vap}"
    assert all(r > 0 for r in riv), f"river loss must be positive every year; got {riv}"
    assert any(v > r for v, r in zip(vap, riv)), \
        "'the river carried more than vapor in every year' must be false"
    assert all(f > 0 for f in fall), "'the basin received no water in the driest year' must be false"
    return (f"vapor losses {vap} and river losses {riv} are both positive in all three "
            "years, so the basin loses water in two phases at once")


def q19(table, item):
    ice = cg.col(table, ICE)
    warm = cg.col(table, SUMMER)
    assert all(ice[i + 1] < ice[i] for i in range(len(ice) - 1)), f"the ice store must shrink; got {ice}"
    assert all(warm[i + 1] > warm[i] for i in range(len(warm) - 1)), f"summer temperature must rise; got {warm}"
    return (f"stored ice falls {ice[0]:.0f} to {ice[-1]:.0f} cubic kilometers while mean "
            f"summer temperature rises {warm[0]} to {warm[-1]} degrees")


CLAIMS = [
 ("The sun",
  "ERT-1.G.1 states that the hydrologic cycle is powered by the sun, and the framework assigns the cycle no other energy source."),
 ("Solid, liquid and gaseous",
  "ERT-1.G.1, near verbatim: the movement of water in its various solid, liquid, and gaseous phases between sources and sinks. All three phases are inside the cycle."),
 ("The oceans",
  "ERT-1.G.2, near verbatim: the oceans are the primary reservoir of water at the Earth's surface, with ice caps and groundwater acting as much smaller reservoirs."),
 ("much smaller reservoirs than the oceans",
  "ERT-1.G.2 names ice caps and groundwater as acting as much smaller reservoirs than the oceans, which it calls the primary reservoir of water at the Earth's surface."),
 ("far more water than the other four reservoirs combined",
  "Recomputed in q5 above: the oceanic figure exceeds the sum of the other four by more than an order of magnitude, which is the quantitative form of ERT-1.G.2's claim about the primary reservoir."),
 ("far larger than lakes and rivers",
  "Recomputed in q6 above: both intermediate reservoirs sit far below the oceans and far above lakes and rivers, which is what ERT-1.G.2 describes in calling them much smaller reservoirs than the primary one."),
 ("more sunlight evaporated more water",
  "Recomputed in q7 above: sorting the sites by sunlight received leaves daily evaporation strictly increasing. ERT-1.G.1 states that the hydrologic cycle is powered by the sun."),
 ("Far more water left the tank during the daylight",
  "Recomputed in q8 above: each daylight figure is several times larger than either dark figure. ERT-1.G.1 states that the hydrologic cycle is powered by the sun, and a daylight-dark contrast of this size is what a sun-driven process shows."),
 ("solid phase later left the basin in the liquid",
  "Recomputed in q9 above: snow on the ground falls to nothing while stream flow peaks as it does. ERT-1.G.1 names solid, liquid and gaseous as the phases of the cycle; snow is the solid phase and stream water the liquid phase."),
 ("Warmer air can hold more water",
  "Recomputed in q10 above: the tabulated capacity rises at every step up the temperature column. ERT-1.G.1 places the gaseous phase within the hydrologic cycle."),
 ("An ice cap",
  "ERT-1.G.1 names solid, liquid and gaseous as the phases in which water moves through the cycle, and ERT-1.G.2 names ice caps as a reservoir. Ice is the solid phase; every rejected option is liquid or gaseous."),
 ("Water vapor in the atmosphere",
  "ERT-1.G.1 names solid, liquid and gaseous as the phases of the cycle. Water vapor is the gaseous phase; the rejected options are ice in the solid phase or liquid water in a reservoir."),
 ("the cycle is powered by the sun",
  "ERT-1.G.1 names the sun as what powers the hydrologic cycle, and the framework offers no alternative energy source anywhere for it."),
 ("Less water would be moved",
  "ERT-1.G.1 states that the hydrologic cycle is powered by the sun, so reducing the energy supplied reduces the work the cycle can do in moving water between sources and sinks."),
 ("From the oceans to the ice caps",
  "ERT-1.G.2 names the oceans, ice caps and groundwater as reservoirs, and ERT-1.G.1 makes the cycle a movement between sources and sinks. The sequence described begins at the ocean surface and ends on an ice cap."),
 ("Liquid, then gaseous, then solid",
  "ERT-1.G.1 names solid, liquid and gaseous as the phases in which water moves. Ocean water is liquid, vapor is gaseous and snow is solid, so the order follows the order of events in the stem."),
 ("great majority of the Earth's water, with each freshwater category far smaller",
  "Recomputed in q17 above: the oceanic share exceeds ninety percent while every other tabulated share is below two percent. ERT-1.G.2 makes the oceans the primary reservoir and the others much smaller."),
 ("both as vapor and in its river",
  "Recomputed in q18 above: both loss columns are positive in all three years. ERT-1.G.1 makes the cycle a movement of water in its various phases between sources and sinks."),
 ("water left the solid phase",
  "Recomputed in q19 above: stored ice falls while summer temperature rises across the surveys. ERT-1.G.2 names ice caps as a reservoir and ERT-1.G.1 puts movement between phases inside the cycle."),
 ("can return to a reservoir it has already left",
  "ERT-1.G.1 defines the hydrologic cycle as the movement of water between sources and sinks, which permits the same water to return rather than being consumed at either end."),
 ("ice caps and groundwater act as reservoirs",
  "ERT-1.G.2 names ice caps and groundwater as reservoirs of water in their own right, so lakes and rivers cannot hold essentially all the fresh water, even though both are much smaller than the oceans."),
 ("far faster on bright days",
  "ERT-1.G.1 states that the hydrologic cycle is powered by the sun, and the way to test that at one site is to vary the sunlight while holding other conditions similar and watch what the water does."),
 ("powered by the sun",
  "ERT-1.G.1 carries all three elements in one sentence: the cycle is powered by the sun, it involves the various solid, liquid and gaseous phases, and it is a movement between sources and sinks."),
 ("will return more of that water to the air",
  "ERT-1.G.1 states that the hydrologic cycle is powered by the sun, so the region receiving more solar energy has more of the energy the cycle uses to move water from a liquid store into the gaseous phase."),
 ("much smaller than the oceans",
  "ERT-1.G.2 names groundwater, alongside ice caps, as acting as a much smaller reservoir than the oceans, which it calls the primary reservoir of water at the Earth's surface."),
 ("primary surface reservoir",
  "ERT-1.G.2 carries exactly those two claims in one sentence: the oceans are the primary reservoir of water at the Earth's surface, with ice caps and groundwater acting as much smaller reservoirs."),
 ("Into other reservoirs of the cycle",
  "ERT-1.G.1 defines the hydrologic cycle as the movement of water between sources and sinks, so water leaving one reservoir arrives at another rather than ceasing to exist."),
 ("All three phases take part",
  "ERT-1.G.1 describes the cycle as the movement of water in its various solid, liquid and gaseous phases between sources and sinks, so all three are inside the cycle and the movement is among them."),
 ("moved between reservoirs rather than lost",
  "ERT-1.G.1 makes the cycle a movement of water between sources and sinks and ERT-1.G.2 makes the oceans the primary reservoir of water at the Earth's surface, so a transfer out of a much smaller reservoir lands in the large one."),
 ("permanently consumed",
  "ERT-1.G.1 describes movement between sources and sinks, which no more consumes water than it creates it, while ERT-1.G.1 and ERT-1.G.2 between them supply the solar energy, the atmospheric movement, the ice cap and the groundwater that the rejected options describe."),
]

TABLE_CHECKS = {5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 17: q17, 18: q18, 19: q19}


def _selftest():
    """Negative control: every gate below must FAIL when its input is corrupted."""
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("e1_7_mutant")
        mod.TOPIC = e1_7.TOPIC
        mod.QUESTIONS = copy.deepcopy(e1_7.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[0]["ans"] = 1

    def break_anchor(mod, claims):
        claims[3] = ("no such phrase anywhere in the module", claims[3][1])

    def corrupt_table(mod, claims):
        # give the night periods the larger evaporation
        mod.QUESTIONS[7]["table"] = dict(
            headers=e1_7._T_DAYNIGHT["headers"],
            rows=[[p, ("9.9" if p.startswith("Midnight") else v)]
                  for p, v in e1_7._T_DAYNIGHT["rows"]])

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[2]["choices"][3] = mod.QUESTIONS[2]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[11]["why"] = "It just is."

    def letter_reference(mod, claims):
        mod.QUESTIONS[19]["why"] = ("Option D is wrong because the framework says so and "
                                    "the rest of the reasoning follows from that.")

    def latex_slips_in(mod, claims):
        mod.QUESTIONS[1]["choices"][4] = "Only \\frac{1}{3} of the phases take part"
        style(mod)

    def range_slips_in(mod, claims):
        mod.QUESTIONS[2]["q"] = "Across 1900-2000 which was the primary reservoir of water?"
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


import e1_7  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(e1_7)
cg.check(e1_7, CLAIMS, table_checks=TABLE_CHECKS)
