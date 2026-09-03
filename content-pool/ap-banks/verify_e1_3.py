"""Key audit for AP ENVIRONMENTAL SCIENCE 1.3 Aquatic Biomes.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Items 1, 3, 15, 22, 26 and 30 rest on ERT-1.C.1: freshwater biomes include
streams, rivers, ponds and lakes, and these freshwater biomes are a vital
resource for drinking water.

Items 2, 4, 11, 12, 16, 17, 22, 25, 26 and 29 rest on ERT-1.C.2: marine biomes
include oceans, coral reefs, marshland and estuaries, and algae in marine biomes
supply a large portion of the Earth's oxygen and also take in carbon dioxide
from the atmosphere.

Items 5, 6, 7, 8, 9, 10, 13, 14, 18, 19, 20, 21, 23, 24, 27 and 28 rest on
ERT-1.C.3: the global distribution of nonmineral marine natural resources, such
as different types of fish, varies because of some combination of salinity,
depth, turbidity, nutrient availability, and temperature. The phrase "some
combination" is what makes each single-sufficient-factor option false, and item
20 marks that soil, which belongs to the terrestrial list of ERT-1.B.3, is not
on this one.

NO BIOME IS DEFINED. The framework names the aquatic biomes and defines none of
them, so no key here rests on what an estuary or a coral reef is. Item 13 gives
the salinity numbers rather than asking a student to infer them from the setting.

DATA ITEMS: 6, 7, 8, 9, 10, 11, 12, 15, 23 and 27 carry tables. Each keyed
conclusion is recomputed below from that table alone, and each check also
falsifies the distractors against the same numbers.

NEGATIVE CONTROL: ``python3 verify_e1_3.py --selftest`` corrupts a key, an
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


SAL = "Salinity (grams of salt per kilogram of water)"
NSPP = "Number of fish species recorded"
UNIQ = "Percent of the recorded species found only in this band"
TURB = "Turbidity (nephelometric turbidity units)"
COVER = "Algal cover on the seabed (percent)"
NITRATE = "Surface nitrate concentration (micromoles per liter)"
CATCH = "Mean annual fish catch (thousands of tonnes)"
SST = "Mean sea surface temperature (degrees Celsius)"
COLD = "Percent of catch made up of cold-water species"
WARM = "Percent of catch made up of warm-water species"
DO = "Change in dissolved oxygen after six hours (milligrams per liter)"
CO2 = "Dissolved carbon dioxide (milligrams per liter)"
SHARE = "Share of the annual supply (percent)"
MTURB = "Mean turbidity (nephelometric turbidity units)"
ALGMASS = "Mass of algae per square meter of lake bed (grams)"


def q6(table, item):
    sal = cg.col(table, SAL)
    spp = cg.col(table, NSPP)
    assert max(sal) > 10 * min(sal), f"salinity must span a wide range; got {sal}"
    assert len(set(spp)) == len(spp), f"no two stations may share a species count; got {spp}"
    assert spp[sal.index(min(sal))] != max(spp), \
        "'the least saline station has the most species' must be false"
    assert spp != sorted(spp), "'species count rises steadily' must be false"
    return (f"salinity runs from {min(sal):.0f} to {max(sal):.0f} grams per kilogram and the "
            f"four species counts {spp} are all different and not in ascending order")


def q7(table, item):
    spp = cg.col(table, NSPP)
    uniq = cg.col(table, UNIQ)
    assert all(spp[i + 1] < spp[i] for i in range(len(spp) - 1)), \
        f"species count must fall with depth; got {spp}"
    assert uniq[-1] == max(uniq), "the deepest band must hold the largest unique share"
    assert uniq[0] != max(uniq), "'the shallowest band is the most distinctive' must be false"
    assert uniq[-1] > 0, "'every deep species also occurs shallower' must be false"
    return (f"species counts fall {spp} from the shallowest band to the deepest while the "
            f"share unique to a band peaks at {uniq[-1]:.0f} percent in the deepest")


def q8(table, item):
    pairs = sorted(zip(cg.col(table, TURB), cg.col(table, COVER)))
    assert all(pairs[i + 1][1] < pairs[i][1] for i in range(len(pairs) - 1)), \
        f"cover must fall as turbidity rises; got {pairs}"
    assert len(set(t for t, _ in pairs)) == len(pairs), "'turbidity is the same at all sites' must be false"
    assert pairs[-1][1] != max(c for _, c in pairs), \
        "'the murkiest site has the most cover' must be false"
    return (f"sorted by turbidity the algal cover reads {[c for _, c in pairs]}, strictly "
            "decreasing across the four sites")


def q9(table, item):
    pairs = sorted(zip(cg.col(table, NITRATE), cg.col(table, CATCH)))
    assert all(pairs[i + 1][1] > pairs[i][1] for i in range(len(pairs) - 1)), \
        f"catch must rise with nitrate; got {pairs}"
    assert pairs[0][1] != max(c for _, c in pairs), \
        "'the poorest ground yields the largest catch' must be false"
    catches = [c for _, c in pairs]
    assert max(catches) - min(catches) > 10, "'all catches within ten thousand tonnes' must be false"
    return (f"sorted by nitrate the catches read {catches}, strictly increasing and "
            f"spanning {max(catches) - min(catches):.0f} thousand tonnes")


def q10(table, item):
    trio = sorted(zip(cg.col(table, SST), cg.col(table, COLD), cg.col(table, WARM)))
    cold = [c for _, c, _ in trio]
    warm = [w for _, _, w in trio]
    assert all(cold[i + 1] < cold[i] for i in range(len(cold) - 1)), f"cold share must fall; got {cold}"
    assert all(warm[i + 1] > warm[i] for i in range(len(warm) - 1)), f"warm share must rise; got {warm}"
    assert cold[-1] != max(cold), "'the warmest block has the largest cold-water share' must be false"
    return (f"sorted by sea surface temperature the cold-water share falls {cold} while the "
            f"warm-water share rises {warm}")


def q11(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, DO)))
    lit = {lab: v for lab, v in vals.items() if lab != "Bottle 3"}
    assert all(v > 0 for v in lit.values()), f"both lit bottles must gain oxygen; got {lit}"
    assert vals["Bottle 3"] < 0, "the dark bottle must lose oxygen"
    assert vals["Bottle 1"] > vals["Bottle 2"], "the fully lit bottle must gain the most"
    assert vals["Bottle 3"] != max(vals.values()), "'the dark bottle gained the most' must be false"
    return (f"oxygen change is {vals['Bottle 1']} and {vals['Bottle 2']} milligrams per liter "
            f"in the lit bottles and {vals['Bottle 3']} in the dark one")


def q12(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, CO2)))
    night = "Middle of the night"
    day = {lab: v for lab, v in vals.items() if lab != night}
    assert all(v < vals[night] for v in day.values()), \
        f"every daylight reading must be below the night reading; got {vals}"
    assert min(vals, key=vals.get) != night, "'the lowest reading was at night' must be false"
    assert max(vals, key=vals.get) != "Midday", "'the highest reading was at midday' must be false"
    assert len(set(vals.values())) > 1, "'the readings are all equal' must be false"
    return (f"the night reading {vals[night]} milligrams per liter exceeds every daylight "
            f"reading {sorted(day.values())}, so carbon dioxide is drawn down in the light")


def q15(table, item):
    sh = dict(zip(cg.labels(table), cg.col(table, SHARE)))
    fresh = sh["Reservoir on a river"] + sh["Lake"]
    assert abs(sum(sh.values()) - 100) < 1e-6, f"the shares must total 100; got {sum(sh.values())}"
    assert fresh > 75, f"the two freshwater-biome sources must exceed three quarters; got {fresh}"
    assert max(sh, key=sh.get) != "Groundwater well", "'the well is the largest source' must be false"
    assert sh["Lake"] + sh["Groundwater well"] < sh["Reservoir on a river"], \
        "'the lake and the well together exceed the river reservoir' must be false"
    return (f"the river reservoir and the lake supply {fresh:.0f} percent between them, more "
            "than three quarters of the total")


def q23(table, item):
    turb = dict(zip(cg.labels(table), cg.col(table, MTURB)))
    mass = dict(zip(cg.labels(table), cg.col(table, ALGMASS)))
    clear = min(turb, key=turb.get)
    assert mass[clear] == max(mass.values()), "the clearer lake must hold the most algae"
    assert mass[clear] > 5 * min(mass.values()), "the difference must be large, not marginal"
    assert len(set(turb.values())) == 2, "'turbidity is the same in the two lakes' must be false"
    assert min(mass.values()) > 0, "'neither lake contains algae' must be false"
    return (f"the clearer lake reads {turb[clear]:.0f} turbidity units and carries "
            f"{mass[clear]:.0f} grams of algae per square meter against "
            f"{min(mass.values()):.0f} in the murkier one")


def q27(table, item):
    uniq = cg.col(table, UNIQ)
    spp = cg.col(table, NSPP)
    assert uniq[-1] == max(uniq), "the deepest band must hold the largest unique share"
    assert uniq[-1] != min(uniq), "'the deepest band has the smallest unique share' must be false"
    assert len(set(uniq)) > 1, "'every band has the same unique share' must be false"
    assert spp[-1] != max(spp), "'the deepest band has the most species' must be false"
    assert spp[-1] != spp[0], "'the deepest and shallowest bands are equal' must be false"
    return (f"the unique-species share {uniq} reaches its maximum in the deepest band even "
            f"though that band holds the fewest species, {spp[-1]:.0f}")


CLAIMS = [
 ("A pond",
  "ERT-1.C.1 lists streams, rivers, ponds and lakes as freshwater biomes. Every rejected option appears instead in the marine list of ERT-1.C.2, so the two framework lists between them settle the item."),
 ("An estuary",
  "ERT-1.C.2 lists oceans, coral reefs, marshland and estuaries as marine biomes, and every rejected option belongs to the freshwater list of ERT-1.C.1."),
 ("vital resource for drinking water",
  "ERT-1.C.1, near verbatim: these freshwater biomes are a vital resource for drinking water. The oxygen claim belongs to algae in marine biomes under ERT-1.C.2, and the framework makes no fish-catch or ore claim about fresh water."),
 ("oxygen and take in carbon dioxide",
  "ERT-1.C.2, near verbatim: algae in marine biomes supply a large portion of the Earth's oxygen, and also take in carbon dioxide from the atmosphere. The rejected options reverse the two gases or attach claims the statement does not make."),
 ("salinity, depth, turbidity",
  "ERT-1.C.3, near verbatim: the global distribution of nonmineral marine natural resources, such as different types of fish, varies because of some combination of salinity, depth, turbidity, nutrient availability, and temperature."),
 ("any two salinities",
  "Recomputed in q6 above: salinity spans a thirtyfold range and no two stations share a species count. ERT-1.C.3 names salinity among the conditions behind where marine species occur, and this transect is a gradient rather than a uniform stretch."),
 ("Fewer species were recorded in the deeper bands",
  "Recomputed in q7 above: the species count falls with depth while the share of species unique to a band peaks in the deepest. ERT-1.C.3 names depth among the conditions behind the distribution of marine species."),
 ("Algal cover falls as turbidity rises",
  "Recomputed in q8 above: sorting the sites by turbidity leaves the algal cover strictly decreasing. ERT-1.C.3 names turbidity among the conditions behind the distribution of marine resources."),
 ("yielded the larger catches",
  "Recomputed in q9 above: sorting the grounds by nitrate concentration leaves the catch strictly increasing. ERT-1.C.3 names nutrient availability among the conditions behind the distribution of fish."),
 ("falls as temperature rises",
  "Recomputed in q10 above: as sea surface temperature increases the cold-water share of the catch falls and the warm-water share rises. ERT-1.C.3 names temperature among the conditions behind the distribution of marine species."),
 ("did not do so in darkness",
  "Recomputed in q11 above: dissolved oxygen rose in both lit bottles, by more in the brighter one, and fell in the dark bottle. ERT-1.C.2 states that algae in marine biomes supply a large portion of the Earth's oxygen."),
 ("lower during daylight",
  "Recomputed in q12 above: every daylight reading lies below the night reading. ERT-1.C.2 states that algae in marine biomes take in carbon dioxide from the atmosphere, which is what a daytime drawdown reflects."),
 ("one of the conditions it names",
  "ERT-1.C.3 lists salinity first among the conditions whose combination accounts for the varying distribution of nonmineral marine resources such as different types of fish. It is one contributing condition, not the only one."),
 ("Different types of fish",
  "ERT-1.C.3 gives different types of fish as its own example of a nonmineral marine natural resource. Every rejected option is a mineral or fossil deposit, which the word nonmineral excludes."),
 ("More than three quarters",
  "Recomputed in q15 above: the river reservoir and the lake together supply more than three quarters of the tabulated total. ERT-1.C.1 names rivers and lakes among the freshwater biomes and calls them a vital resource for drinking water."),
 ("all three as marine biomes",
  "ERT-1.C.2 lists oceans, coral reefs, marshland and estuaries together as marine biomes, so that grouping is the framework's own rather than the student's invention."),
 ("Less oxygen supplied to the Earth and less carbon dioxide",
  "ERT-1.C.2 assigns algae in marine biomes two roles at once, supplying a large portion of the Earth's oxygen and taking in carbon dioxide from the atmosphere, so reducing the algae reduces both at the same time."),
 ("are held similar",
  "ERT-1.C.3 names five conditions whose combination accounts for distribution, so isolating one of them requires holding the other four similar. A comparison in which every condition varies cannot attribute a difference to any single one."),
 ("Depth",
  "ERT-1.C.3 lists salinity, depth, turbidity, nutrient availability and temperature. The stem holds four of those five equal between the two areas, so the one it does not mention is the only listed candidate remaining."),
 ("Soil type",
  "ERT-1.C.3 lists salinity, depth, turbidity, nutrient availability and temperature. Soil appears in the terrestrial list of ERT-1.B.3 and on no marine list, which is what makes it the exception here."),
 ("the conditions fish depend on",
  "ERT-1.C.3 names different types of fish as its example of a nonmineral marine natural resource and attributes their uneven distribution to some combination of the five conditions it lists, not to fishing effort or to ore deposits."),
 ("separates freshwater biomes",
  "ERT-1.C.1 and ERT-1.C.2 give two separate lists, one of freshwater biomes and one of marine biomes, so the framework itself draws the division the student denies."),
 ("clearer lake",
  "Recomputed in q23 above: the lake with the lower turbidity reading carries about nine times the algal mass of the murkier lake. Turbidity is one of the conditions named in ERT-1.C.3."),
 ("measured nutrient concentration",
  "ERT-1.C.3 names nutrient availability as one condition behind the distribution of fish, so the evidence that bears on it is a measured association between nutrient concentration and catch. Port distance and fleet size are properties of the fishing effort rather than of the water."),
 ("A reduction in the amount",
  "ERT-1.C.2 states that algae in marine biomes take in carbon dioxide from the atmosphere, so removing the algae removes that uptake at the place where they lived."),
 ("lakes are the freshwater list",
  "ERT-1.C.1 gives streams, rivers, ponds and lakes as the freshwater biomes and ERT-1.C.2 gives oceans, coral reefs, marshland and estuaries as the marine biomes, which is exactly the pairing the keyed option states."),
 ("the largest share of species recorded in no other band",
  "Recomputed in q27 above: the share of species found in no other band reaches its maximum in the deepest band even though that band holds the fewest species, so the data point the opposite way from the student's argument."),
 ("the larger fish resource",
  "ERT-1.C.3 names nutrient availability among the conditions whose combination accounts for the distribution of nonmineral marine resources such as fish, and the stem holds the other named conditions equal between the two grounds."),
 ("algae living in marine biomes",
  "ERT-1.C.2 attributes the supply of a large portion of the Earth's oxygen specifically to algae in marine biomes. The framework makes no such claim about dissolution from the air, about fish respiration, or about reef minerals."),
 ("which include lakes",
  "ERT-1.C.1 names lakes among the freshwater biomes and states that those biomes are a vital resource for drinking water, which is precisely the use the town proposes."),
]

TABLE_CHECKS = {6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 12: q12,
                15: q15, 23: q23, 27: q27}


def _selftest():
    """Negative control: every gate below must FAIL when its input is corrupted."""
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("e1_3_mutant")
        mod.TOPIC = e1_3.TOPIC
        mod.QUESTIONS = copy.deepcopy(e1_3.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[0]["ans"] = 4

    def break_anchor(mod, claims):
        claims[4] = ("no such phrase anywhere in the module", claims[4][1])

    def corrupt_table(mod, claims):
        # give the dark bottle the largest oxygen gain of the three
        mod.QUESTIONS[10]["table"] = dict(
            headers=e1_3._T_BOTTLE["headers"],
            rows=[[b, li, ("9.9" if b == "Bottle 3" else v)]
                  for b, li, v in e1_3._T_BOTTLE["rows"]])

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[1]["choices"][2] = mod.QUESTIONS[1]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[19]["why"] = "It just is."

    def letter_reference(mod, claims):
        mod.QUESTIONS[21]["why"] = ("Answer E is wrong because the framework says so and "
                                    "the rest of the reasoning follows from that.")

    def latex_slips_in(mod, claims):
        mod.QUESTIONS[3]["choices"][3] = "They affect \\frac{1}{4} of the atmosphere"
        style(mod)

    def range_slips_in(mod, claims):
        mod.QUESTIONS[2]["q"] = "Over 1990-2010 why did the framework single out freshwater biomes?"
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


import e1_3  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(e1_3)
cg.check(e1_3, CLAIMS, table_checks=TABLE_CHECKS)
