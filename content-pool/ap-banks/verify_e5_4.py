"""Key audit for AP ENVIRONMENTAL SCIENCE 5.4 Impacts of Agricultural Practices.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
EIN-2.D.1 is the whole topic: agricultural practices that CAN CAUSE
environmental damage include tilling, slash-and-burn farming, and the use of
fertilizers. It names the practices and stops. Every item that attaches a
specific harm to a specific practice therefore CHAINS to a framework statement
that supplies that harm, and the chain is written out in the claim:

  tilling            -> STB-1.E.1: the goal of soil conservation is to prevent
                        soil erosion, and no-till agriculture is one of its
                        methods. Tilling is what no-till agriculture omits.
  slash-and-burn     -> EIN-2.B.2: the cutting and burning of trees releases
                        carbon dioxide and contributes to climate change.
  use of fertilizers -> STB-3.F.5: agricultural runoff is an anthropogenic
                        cause of eutrophication; STB-3.F.1: eutrophication is a
                        body of water becoming enriched in nutrients.

Items keyed on the bare list, its scope, or the framework's word CAN: 1, 2, 15,
17, 21, 23, 28, 30. Items keyed through the tilling chain: 3, 4, 5, 13, 14, 16,
19, 26, 27. Through the burning chain: 10, 11, 12, 20, 25. Through the
fertilizer chain: 6, 7, 8, 9, 18, 22, 29. Item 24 uses two chains at once.

DATA ITEMS: 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 22, 25, 27 and 29 carry
tables. Each keyed conclusion is recomputed below from that table alone and
anchored to a named row. Where a check divides, it first asserts the divisor is
non-zero, so a corrupted table fails the gate rather than raising an unrelated
exception that the negative control would not recognise.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs.
"""
import e_check
import cg_check as cg
import e5_4

SOIL_LOST = "Soil lost in one year (tonnes per hectare)"
ORGANIC = "Soil organic matter after ten seasons (percent by mass)"
APPLIED = "Fertilizer applied (kilograms per hectare)"
RUNOFF = "Nitrate carried off the plot in runoff (kilograms per hectare)"
NITRATE = "Nitrate concentration in the water (milligrams per litre)"
HARVEST = "Grain harvested from the plot (tonnes per hectare)"
RELEASED = "Carbon released to the atmosphere in the first year (tonnes per hectare)"
PLOUGHINGS = "Times the field was ploughed in the year"
SEDIMENT = "Sediment reaching the stream (tonnes per hectare)"

PLOUGHED = "Ploughed before every planting"
UNTILLED = "Left untilled and sown through the residue"
NONE_F = "No fertilizer applied"
LIGHT = "Light application"
HEAVY = "Heavy application"
UP = "Upstream of the farmland"
BESIDE = "Beside the farmland"
DOWN = "Downstream of the farmland"
BURNED = "Cut and burned on the plot"
TIMBER = "Cut and removed as timber"
STANDING = "Left standing"


def q3(table, item):
    assert cg.cell(table, PLOUGHED, SOIL_LOST) > cg.cell(table, UNTILLED, SOIL_LOST), \
        "the ploughed plot must lose the greater mass of soil"
    assert cg.cell(table, PLOUGHED, ORGANIC) < cg.cell(table, UNTILLED, ORGANIC), \
        "the ploughed plot must hold the smaller organic matter fraction"
    return (f"the ploughed plot reads {cg.cell(table, PLOUGHED, SOIL_LOST):.0f} tonnes per "
            f"hectare lost against {cg.cell(table, UNTILLED, SOIL_LOST):.0f}, and "
            f"{cg.cell(table, PLOUGHED, ORGANIC)} percent organic matter against "
            f"{cg.cell(table, UNTILLED, ORGANIC)}")


def q4(table, item):
    lo = cg.cell(table, UNTILLED, SOIL_LOST)
    assert lo > 0, "the untilled loss must be non-zero for a ratio to exist"
    r = cg.cell(table, PLOUGHED, SOIL_LOST) / lo
    assert r == 6, f"the ratio recomputes to {r}, not 6"
    for wrong in (3, 18, 2, 1):
        assert r != wrong, f"the {wrong} distractor equals the key"
    return f"18 divided by 3 is {r:.0f} times as much soil lost from the ploughed plot"


def q6(table, item):
    assert cg.cell(table, NONE_F, APPLIED) == 0, "the control row must receive no fertilizer"
    pairs = sorted(zip(cg.col(table, APPLIED), cg.col(table, RUNOFF)))
    assert all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"runoff must rise with the application rate; got {pairs}"
    assert pairs[-1][1] == max(r for _, r in pairs), \
        "'the most fertilized plot lost the least' must be false"
    return (f"sorted by application rate the runoff figures are {[r for _, r in pairs]} "
            "kilograms per hectare, rising without exception")


def q7(table, item):
    d = cg.cell(table, HEAVY, RUNOFF) - cg.cell(table, NONE_F, RUNOFF)
    assert d == 30, f"the difference recomputes to {d}, not 30"
    for wrong in (31, 25, 17, 32):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"31 minus 1 is {d:.0f} kilograms per hectare of extra nitrate in runoff"


def q8(table, item):
    vals = [cg.cell(table, lab, NITRATE) for lab in (UP, BESIDE, DOWN)]
    assert vals[0] < vals[1] < vals[2], f"nitrate must rise downstream; got {vals}"
    assert len(set(vals)) == 3, "'the same at all three points' must be false"
    return (f"the three sampling points read {vals} milligrams per litre moving downstream, "
            "so the water gains nitrate as it passes the farmland")


def q9(table, item):
    d = cg.cell(table, DOWN, NITRATE) - cg.cell(table, UP, NITRATE)
    assert abs(d - 3.7) < 1e-9, f"the rise recomputes to {d}, not 3.7"
    for wrong in (4.1, 2.2, 1.5, 4.5):
        assert abs(d - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return f"4.1 minus 0.4 is {d:.1f} milligrams per litre"


def q10(table, item):
    v = cg.col(table, HARVEST)
    assert cg.cell(table, "First season", HARVEST) == max(v), \
        "the first season must carry the largest harvest"
    assert all(v[i] > v[i + 1] for i in range(len(v) - 1)), f"the harvest must fall; got {v}"
    return f"the harvests run {v} tonnes per hectare, falling in every step"


def q11(table, item):
    first = cg.cell(table, "First season", HARVEST)
    assert first > 0, "the first season harvest must be non-zero for a fraction to exist"
    frac = cg.cell(table, "Fourth season", HARVEST) / first
    assert abs(frac - 1.0 / 6.0) < 1e-9, f"the fraction recomputes to {frac}, not one sixth"
    for wrong in (0.5, 1.0 / 3.0, 2.0 / 3.0, 1.0):
        assert abs(frac - wrong) > 1e-9, "a rejected fraction equals the key"
    return f"0.4 divided by 2.4 is {frac:.3f}, which is one sixth of the first season"


def q12(table, item):
    v = dict(zip(cg.labels(table), cg.col(table, RELEASED)))
    assert max(v, key=v.get) == BURNED, f"the largest release is {max(v, key=v.get)}"
    assert v[STANDING] == 0, "the untouched treatment must release nothing"
    assert v[BURNED] > v[TIMBER], "burning must exceed removal as timber"
    return (f"the three treatments release {list(v.values())} tonnes per hectare, largest "
            "where the vegetation was cut and burned")


def q13(table, item):
    assert cg.cell(table, "Field 1", PLOUGHINGS) == 0, "Field 1 must be the unploughed field"
    pairs = sorted(zip(cg.col(table, PLOUGHINGS), cg.col(table, SEDIMENT)))
    assert all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"sediment must rise with ploughings; got {pairs}"
    assert pairs[0][1] > 0, "'only the unploughed field delivered sediment' must be false"
    return (f"sorted by number of ploughings the sediment figures are {[s for _, s in pairs]} "
            "tonnes per hectare, rising without exception")


def q14(table, item):
    d = cg.cell(table, "Field 4", SEDIMENT) - cg.cell(table, "Field 1", SEDIMENT)
    assert d == 22, f"the difference recomputes to {d}, not 22"
    for wrong in (24, 17, 11, 26):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"24 minus 2 is {d:.0f} tonnes per hectare of extra sediment"


def q22(table, item):
    shares = {}
    for lab in (LIGHT, HEAVY):
        rate = cg.cell(table, lab, APPLIED)
        assert rate > 0, f"{lab} must have a non-zero application rate for a share to exist"
        shares[lab] = cg.cell(table, lab, RUNOFF) / rate
    assert shares[HEAVY] > shares[LIGHT], \
        f"the share must rise; got {shares[LIGHT]} then {shares[HEAVY]}"
    assert abs(1.0 / shares[LIGHT] - 8) < 1, \
        f"the light share is one part in {1.0 / shares[LIGHT]:.1f}, not about eight"
    assert abs(1.0 / shares[HEAVY] - 6) < 1, \
        f"the heavy share is one part in {1.0 / shares[HEAVY]:.1f}, not about six"
    return (f"6 of 50 kilograms is one part in {1.0 / shares[LIGHT]:.1f} and 31 of 200 is one "
            f"part in {1.0 / shares[HEAVY]:.1f}, so the share rises")


def q25(table, item):
    t = cg.cell(table, TIMBER, RELEASED)
    assert t > 0, "the timber-removal release must be non-zero for a ratio to exist"
    r = cg.cell(table, BURNED, RELEASED) / t
    assert r > 4, f"burning releases {r:.1f} times the removal case, which is not 'several'"
    assert cg.cell(table, STANDING, RELEASED) < t, \
        "'only leaving it standing released carbon' must be false"
    return (f"55 tonnes per hectare from burning against {t:.0f} from removal as timber, a "
            f"factor of {r:.1f}")


def q27(table, item):
    s = dict(zip(cg.labels(table), cg.col(table, SEDIMENT)))
    p = dict(zip(cg.labels(table), cg.col(table, PLOUGHINGS)))
    assert min(p, key=p.get) == "Field 1", "Field 1 must be the least ploughed field"
    assert min(s, key=s.get) == "Field 1", "the least ploughed field must lose the least sediment"
    assert max(p, key=p.get) == max(s, key=s.get), \
        "the most ploughed field must also be the one losing the most sediment"
    return (f"ploughings {list(p.values())} against sediment {list(s.values())} tonnes per "
            "hectare, with the extremes of the two columns on the same fields")


def q29(table, item):
    vals = {lab: cg.cell(table, lab, NITRATE) for lab in cg.labels(table)}
    assert min(vals, key=vals.get) == UP, \
        f"the smallest reading must be upstream, but it is at {min(vals, key=vals.get)}"
    assert vals[UP] > 0, "'the water above the farmland contains some nitrate' must be true"
    assert vals[BESIDE] > vals[UP] and vals[DOWN] > vals[BESIDE], \
        "the three readings must rise steadily downstream"
    return (f"the readings are {list(vals.values())} milligrams per litre from upstream to "
            "downstream, so an upstream source is the one reading the data rule out")


CLAIMS = [
 ("slash-and-burn farming, and the use of fertilizers",
  "EIN-2.D.1, near verbatim: agricultural practices that can cause environmental damage include tilling, slash-and-burn farming, and the use of fertilizers. The rejected groups are STB-1.E.1's conservation methods, STB-1.E.2's fertility strategies, EIN-2.H.1's meat production methods, and STB-1.G's forestry methods."),
 ("which is weaker than saying",
  "EIN-2.D.1 uses the words CAN CAUSE, which asserts a possibility rather than an invariable outcome. Tilling is named in the list, no size threshold appears, and the statement covers all three practices."),
 ("held less organic matter",
  "Recomputed in q3 above: 18 tonnes per hectare of soil lost against 3, and 1.4 percent organic matter against 3.2. EIN-2.D.1 names tilling among the damaging practices and STB-1.E.1 makes no-till agriculture a soil conservation method whose goal is to prevent soil erosion."),
 ("Six times as much",
  "Recomputed in q4 above: 18 divided by 3. The rejected values quote one loss as if it were the ratio or use the organic matter column."),
 ("listed as a soil conservation method",
  "STB-1.E.1 states that the goal of soil conservation is to prevent soil erosion and lists no-till agriculture among the methods. Tilling is what no-till agriculture omits, so soil erosion is the damage the framework's own statements attach to it."),
 ("rose with every increase in the fertilizer",
  "Recomputed in q6 above: runoff of 1, 6, 14 and 31 kilograms per hectare at rising application rates. EIN-2.D.1 names fertilizer use among the damaging practices and STB-3.F.5 names agricultural runoff as an anthropogenic cause of eutrophication."),
 ("30 kilograms per hectare more",
  "Recomputed in q7 above: 31 minus 1 kilograms per hectare. The rejected values quote the heavy plot alone, pair the wrong treatments, or add the two."),
 ("higher below the farmland than above it",
  "Recomputed in q8 above: 0.4, 2.6 and 4.1 milligrams per litre moving downstream past the farmland. STB-3.F.5 names agricultural runoff as an anthropogenic cause of eutrophication and STB-3.F.1 defines eutrophication as nutrient enrichment of a body of water."),
 ("3.7 milligrams",
  "Recomputed in q9 above: 4.1 minus 0.4 milligrams per litre. The rejected values quote the downstream reading alone, pair the wrong points, or add the readings."),
 ("fell in every season after the first",
  "Recomputed in q10 above: 2.4, 1.6, 0.9 and 0.4 tonnes per hectare. EIN-2.D.1 names slash-and-burn farming among the practices that can cause environmental damage."),
 ("One sixth of it",
  "Recomputed in q11 above: 0.4 divided by 2.4. The rejected fractions correspond to other pairs of seasons or deny that the harvest changed."),
 ("Cutting and burning released the most carbon",
  "Recomputed in q12 above: 55 tonnes per hectare against 12 and 0. EIN-2.B.2 states that the cutting and burning of trees releases carbon dioxide and contributes to climate change, which is the harm EIN-2.D.1's mention of slash-and-burn farming points to."),
 ("rose with each additional ploughing",
  "Recomputed in q13 above: 2, 7, 13 and 24 tonnes per hectare at 0, 1, 2 and 4 ploughings. EIN-2.D.1 names tilling and STB-1.E.1 puts preventing soil erosion as the goal no-till agriculture serves."),
 ("22 tonnes per hectare more",
  "Recomputed in q14 above: 24 minus 2 tonnes per hectare. The rejected values quote one field alone, pair the wrong fields, or add the two."),
 ("Contour plowing",
  "EIN-2.D.1 names tilling, slash-and-burn farming and the use of fertilizers. Contour plowing appears instead in STB-1.E.1 as a soil conservation method whose goal is to prevent soil erosion, which places it on the opposite side of the framework."),
 ("through the previous season's residue",
  "EIN-2.D.1 names tilling as the practice at issue and STB-1.E.1 lists no-till agriculture among the soil conservation methods whose goal is to prevent soil erosion. Each rejected option leaves the ploughing in place, and two add a second practice the framework also names as damaging."),
 ("alters natural systems",
  "The enduring understanding EIN-2 states that when humans use natural resources they alter natural systems, and tilling, slash-and-burn farming and fertilizer use are three ways of using farmland. None generates electricity, and the framework attaches no legal requirement to them."),
 ("much higher than in the water entering it",
  "EIN-2.D.1 names the use of fertilizers as a practice that can cause environmental damage, STB-3.F.5 makes agricultural runoff a cause of eutrophication, and STB-3.F.1 defines that as nutrient enrichment of a body of water. Crop height, fuel costs and machinery counts measure something else."),
 ("same soil, slope and crop",
  "A test of one practice must vary that practice and hold everything else fixed, so soil, slope and crop must match while the ploughing differs. Each rejected comparison changes a second variable or a different practice."),
 ("which the framework links to climate change",
  "EIN-2.D.1 names slash-and-burn farming as a practice that can cause environmental damage, and EIN-2.B.2 states that the cutting and burning of trees releases carbon dioxide and contributes to climate change. The framework never treats burning as removing carbon from the cycle."),
 ("first officer is correct",
  "EIN-2.D.1 reads that agricultural practices that CAN CAUSE environmental damage INCLUDE tilling, slash-and-burn farming, and the use of fertilizers, and stops there. The specific harms come from STB-1.E.1, EIN-2.B.2 and STB-3.F.5, which are separate statements in other topics."),
 ("rises from about one part in eight",
  "Recomputed in q22 above: 6 of 50 kilograms applied against 31 of 200, so the share carried off rises with the rate. EIN-2.D.1 names the use of fertilizers among the practices that can cause environmental damage."),
 ("depends on how and where a practice is carried out",
  "The word CAN in EIN-2.D.1 makes the statement one about what these practices are capable of producing rather than what they invariably produce. The framework does not doubt the practices exist and says nothing about damage being reversible."),
 ("fertilizers for the nitrate",
  "STB-3.F.5 makes agricultural runoff a source of nutrient enrichment, which points to the fertilizer named in EIN-2.D.1, and STB-1.E.1 attaches soil erosion to the absence of no-till practice, which points to tilling. The rejected pairings swap the two or substitute practices from topics 5.5 and 5.6."),
 ("several times as much carbon in the first year",
  "Recomputed in q25 above: 55 tonnes per hectare from burning against 12 from removal as timber. EIN-2.B.2 attributes the release of carbon dioxide to the cutting AND BURNING of trees, which is the step slash-and-burn farming adds."),
 ("mass of soil leaving the hillside",
  "STB-1.E.1 makes preventing soil erosion the goal of the conservation methods that include no-till agriculture, so the damage attached to tilling is soil leaving the field. Watering, yield, employment and price measure things the framework does not connect to tilling."),
 ("tilling is among the practices",
  "Recomputed in q27 above: sediment falls from 24 to 2 tonnes per hectare as ploughings fall from four to none, which is a result about tilling. EIN-2.D.1 is the statement that names tilling; the rejected statements are EIN-2.C.2, STB-3.F.1, EIN-2.I.5 and ENG-2.B.2."),
 ("adopted to prevent soil erosion",
  "EIN-2.D.1 introduces its three practices as ones that CAN CAUSE ENVIRONMENTAL DAMAGE, while STB-1.E.1 states that the goal of soil conservation is to prevent soil erosion and then lists its methods. The two lists share no member."),
 ("comes from a source upstream of the farmland",
  "Recomputed in q29 above: the smallest reading is the upstream one, so an upstream source is exactly what the data rule out. The other four statements each restate part of the same rising sequence correctly."),
 ("are agricultural practices that can cause",
  "EIN-2.D.1 states that agricultural practices that can cause environmental damage include tilling, slash-and-burn farming, and the use of fertilizers. The rejected summaries strengthen CAN into always, substitute practices from topics 5.5 and 5.6, shorten the list, or deny it."),
]

TABLE_CHECKS = {3: q3, 4: q4, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 12: q12,
                13: q13, 14: q14, 22: q22, 25: q25, 27: q27, 29: q29}

e_check.run(e5_4, CLAIMS, TABLE_CHECKS)
