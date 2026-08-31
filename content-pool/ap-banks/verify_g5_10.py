"""Key audit for AP HUMAN GEOGRAPHY 5.10 Consequences of Agricultural Practices.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective IMP-5.A, "Explain how agricultural
practices have environmental and societal consequences", and three statements,
all of them lists:

    IMP-5.A.1 Environmental effects of agricultural land use include pollution,
              land cover change, desertification, soil salinization, and
              conservation efforts.
    IMP-5.A.2 Agricultural practices -- including slash and burn, terraces,
              irrigation, deforestation, draining wetlands, shifting
              cultivation, and pastoral nomadism -- alter the landscape.
    IMP-5.A.3 Societal effects of agricultural practices include changing diets,
              role of women in agricultural production, and economic purpose.

THE ODD ENTRY ON THE FIRST LIST IS "CONSERVATION EFFORTS" and it is the single
most instructive thing in the topic. Four of the five entries are damage and the
fifth is a response to damage. The CED puts all five under one heading because
the heading is EFFECTS of agricultural land use, and organized effort to protect
soil and water is a consequence of farming in exactly the same sense that the
erosion is. Items 8, 22 and 24 rest on this; item 24 offers "all five are kinds
of damage" as the distractor because that is the reading a student arrives with.

IMP-5.A.2'S VERB IS "ALTER THE LANDSCAPE", not raise yields and not change
incomes, so every item keyed to it asks what a practice leaves VISIBLE on the
ground: a slope cut into steps, a canal network and the field geometry serving
it, a forest edge that has moved, ditches across drained ground, a mosaic of
plots at different stages of regrowth, tracks and wells converging on water.
Items 9 to 15 walk the CED's own list of seven, and items 20 and 25 reverse the
reasoning by reading a practice off a landscape.

IMP-5.A.3'S THIRD ENTRY needs unpacking and item 18 does it: "economic purpose"
means the purpose FOR WHICH a society farms -- to feed itself or to sell -- and a
shift between those changes what is grown, who grows it and where it goes. The
second entry, the role of women, is Topic 5.12's entire subject, so item 17 keys
only on what IMP-5.A.3 itself asserts, which is that the role is a consequence
of practice rather than a fixed feature of a society, and leaves the detail to
that topic.

WHAT NO ITEM ASSERTS: that any practice is universally destructive, or that
desertification and salinization follow automatically from farming dry land. Both
are outcomes of particular practices under particular conditions, so items 6, 7
and 23 key on the MECHANISM, which puts the conditions inside the answer.

SYNONYM CARE. `geo_check` treats {"shifting cultivation", "slash-and-burn
agriculture", "swidden agriculture"} as one construct and {"pastoral nomadism",
"nomadic herding"} as another. The CED's own list names slash and burn AND
shifting cultivation separately, so where the statement is quoted they sit
together inside a SINGLE choice; no item offers two names for one practice as
competing options.

The three table items (26, 27, 28) are the computational gate:

  26  both columns checked to sum to 100, which makes the record a claim about
      composition and defeats the distractor asserting the basin shrank, plus
      the combined agricultural share recomputed at both dates
  27  the nitrate ratio and the oxygen fall are both derived, and the verifier
      confirms the maximum nitrate is NOT at the upstream point, since two
      distractors assert exactly that
  28  both columns checked to sum to 100, with the fall in the staple share and
      the combined rise of the other two groups recomputed

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import re

import geo_check
import g5_10


def q26_land_cover(table):
    """Composition only, and agriculture's combined share at both dates."""
    before = {r[0]: float(r[1]) for r in table["rows"]}
    after = {r[0]: float(r[2]) for r in table["rows"]}
    assert sum(before.values()) == sum(after.values()) == 100, (before, after)
    assert before["Forest"] == 62 and after["Forest"] == 31, (before, after)
    agri_before = before["Cropland"] + before["Pasture"]
    agri_after = after["Cropland"] + after["Pasture"]
    assert agri_before == 33 and agri_after == 65, (agri_before, agri_after)
    assert after["Forest"] < before["Forest"] / 2 + 1, (before, after)
    return f"from {before['Forest']:.0f} to {after['Forest']:.0f} percent"


def q27_water_quality(table):
    """Nitrate ratio and oxygen fall, with the upstream point confirmed cleanest."""
    nitrate = {r[0]: float(r[2]) for r in table["rows"]}
    oxygen = {r[0]: float(r[3]) for r in table["rows"]}
    position = {r[0]: r[1] for r in table["rows"]}
    upstream = [k for k, v in position.items() if v == "Above all farmland"][0]
    worst = [k for k, v in position.items()
             if v == "Below intensively farmed land"][0]
    # Two distractors claim the upstream point is the worst; neither may hold.
    assert nitrate[upstream] == min(nitrate.values()), nitrate
    assert oxygen[upstream] == max(oxygen.values()), oxygen
    ratio = nitrate[worst] / nitrate[upstream]
    assert ratio > 10, (nitrate, ratio)
    assert oxygen[worst] < oxygen[upstream] / 2, oxygen
    return "more than tenfold"


def q28_diet_composition(table):
    """Composition only; staple share falls and the other two groups rise."""
    before = {r[0]: float(r[1]) for r in table["rows"]}
    after = {r[0]: float(r[2]) for r in table["rows"]}
    assert sum(before.values()) == sum(after.values()) == 100, (before, after)
    assert before["Cereals and roots"] == 74 and after["Cereals and roots"] == 51
    rich_before = before["Animal products"] + before["Oils and sugars"]
    rich_after = after["Animal products"] + after["Oils and sugars"]
    assert rich_before == 21 and rich_after == 43, (rich_before, rich_after)
    return (f"fall from {before['Cereals and roots']:.0f} to "
            f"{after['Cereals and roots']:.0f} percent")


CLAIMS = [
 ("desertification, soil salinization, and conservation efforts",
  "EK IMP-5.A.1 names exactly pollution, land cover change, desertification, soil salinization and conservation efforts. Changing diets and economic purpose belong to EK IMP-5.A.3's societal list, and the other sets are drawn from settlement, the Green Revolution and survey methods."),

 ("Slash and burn, terraces, irrigation, deforestation",
  "EK IMP-5.A.2 names exactly this list of practices and says they alter the landscape. The rejected set of pollution, desertification and salinization names effects rather than practices, which is the distinction between this statement and the one before it."),

 ("the role of women in agricultural production",
  "EK IMP-5.A.3 names changing diets, the role of women in agricultural production and economic purpose as the three societal effects. The environmental effects belong to EK IMP-5.A.1 and the landscape-altering practices to EK IMP-5.A.2, so this is the only one of the three about people."),

 ("carried off them by rain and irrigation water",
  "EK IMP-5.A.1 names pollution first among the environmental effects of agricultural land use. What makes agricultural pollution distinctive is that it is diffuse -- it leaves a whole surface rather than a pipe -- which is why it is so hard to regulate or to trace to a source."),

 ("forest or grassland becomes cropland or pasture",
  "EK IMP-5.A.1 names land cover change among the environmental effects of agricultural land use. Cover is what physically occupies the surface, which is why the change is visible from satellites and why it affects water, soil and habitat at the same time."),

 ("until it can no longer support the vegetation it once did",
  "EK IMP-5.A.1 names desertification among the environmental effects of agricultural land use, attributing a role to farming without making it the sole cause. Removing vegetation faster than dry land can regrow it exposes the soil, and the soil then blows or washes away."),

 ("where it evaporates rather than draining away",
  "EK IMP-5.A.1 names soil salinization among the environmental effects of agricultural land use. The salt is already dissolved in the water applied; what farming supplies is the repeated evaporation that concentrates it in the root zone until crops will no longer grow."),

 ("organized effort to protect soil and water is as much a consequence",
  "EK IMP-5.A.1 puts all five entries under one heading, four of them damage and the fifth a response to it. Reading the statement as a list of harms makes the last entry incomprehensible; reading it as a list of consequences of agricultural land use makes it obvious."),

 ("cut a slope into a stair of level platforms",
  "EK IMP-5.A.2 names terraces among the practices that alter the landscape. A level surface holds water long enough for it to soak in rather than run off, which makes terracing both a landscape alteration and a soil-conservation practice at once."),

 ("Canals, ditches, reservoirs and the geometry of fields",
  "EK IMP-5.A.2 names irrigation among the practices that alter the landscape. Delivering water requires a built network that outlasts any single crop, and taking that water alters the river or aquifer it came from as well as the ground it reaches."),

 ("since land under forest is being converted to agricultural use",
  "EK IMP-5.A.2 names deforestation among the practices that alter the landscape and EK IMP-5.A.1 names land cover change among the environmental effects. A moving forest edge is the visible boundary between two land covers, which is why it can be measured from imagery."),

 ("capacity to store floodwater",
  "EK IMP-5.A.2 names draining wetlands among the practices that alter the landscape. A wetland performs functions besides occupying space -- holding water back, filtering it, supporting particular species -- and draining it ends all of them together."),

 ("mosaic of plots at different stages of clearing",
  "EK IMP-5.A.2 names shifting cultivation among the practices that alter the landscape. Because plots are used and rested in rotation, at any moment the district holds ground at every stage of the cycle at once, which is what makes the pattern a mosaic rather than a field."),

 ("the wells and watering points herds converge on",
  "EK IMP-5.A.2 names pastoral nomadism among the practices that alter the landscape, which is worth noticing because the practice cultivates nothing. Water is the scarce resource where it occurs, so the imprint concentrates wherever the herds must come to drink."),

 ("The ash returns nutrients to the surface",
  "EK IMP-5.A.2 names slash and burn among the practices that alter the landscape. Burning transfers nutrients held in standing vegetation onto the ground, and where rainfall leaches heavily that transfer is short-lived, which is what makes the practice a cycle rather than a settlement."),

 ("the societal effects of agricultural practices include changing diets",
  "EK IMP-5.A.3 names changing diets first among the societal effects of agricultural practices. What a society eats follows from what its agriculture produces and buys, so a change in production reaches the table as surely as it reaches the market."),

 ("so it changes as those practices change",
  "EK IMP-5.A.3 names the role of women in agricultural production among the societal effects of agricultural practices. Placing it on that list is itself the claim: the role is a consequence of how a society farms rather than a fixed feature of the society."),

 ("to feed itself or to sell",
  "EK IMP-5.A.3 names economic purpose among the societal effects of agricultural practices. A shift from growing food to eat toward growing crops to sell reorganizes a household's labour, its diet and its exposure to prices, which is why the CED counts it as a societal effect."),

 ("where a terrace or a salinized plot is visible",
  "EK IMP-5.A.1 names effects ranging from a single salinized field to land cover change across a whole region. The same practice repeated across thousands of holdings becomes a regional change, so the two scales record one process at different resolutions."),

 ("practices the framework names among those that alter the landscape",
  "EK IMP-5.A.2 names terraces and irrigation among the practices that alter the landscape, and both leave permanent constructed features. Reading a practice from what it built reverses the statement's own direction, and it is what a cultural landscape makes possible."),

 ("rebuilding soil takes far longer than removing it",
  "EK IMP-5.A.1 names desertification among the environmental effects of agricultural land use. Soil forms over centuries and can be lost in years, so a degraded dry landscape cannot be restored on anything like the timescale over which it was damaged."),

 ("Contour ploughing, cover crops, reduced tillage",
  "EK IMP-5.A.1 names conservation efforts among the environmental effects of agricultural land use. Every practice in the keyed set works by keeping soil and water where they are, which is the direct answer to the erosion, runoff and pollution the same statement lists."),

 ("bare soil is exposed to wind and rain",
  "EK IMP-5.A.1 names desertification among the environmental effects of agricultural land use. Each step in the chain follows from the one before, and the decisive feature is that the last step makes the damage permanent, since without plants there is nothing left to hold the soil."),

 ("conservation efforts, is a response to it",
  "EK IMP-5.A.1 lists pollution, land cover change, desertification, soil salinization AND conservation efforts under a single heading. That heading is environmental effects of agricultural land use, and a deliberate effort to protect soil and water is an effect of farming in exactly the same sense."),

 ("matched to a network of ditches",
  "EK IMP-5.A.2 names seven practices and says they alter the landscape, each in its own way. Only one pairing here matches a practice to the feature it actually produces, and the others swap the traces of two of the CED's own listed practices."),

 ("Forest fell from 62 to 31 percent",
  "Recomputed from the record: both columns sum to 100, so this is composition rather than area, and forest halves from 62 to 31 percent while cropland and pasture together rise from 33 to 65. EK IMP-5.A.1 names land cover change among the environmental effects of agricultural land use, and this is that effect measured directly.",
  ),

 ("Nitrate rises more than tenfold",
  "Recomputed from the record: nitrate rises from 1.2 to 14.5 milligrams per litre between the point above the farmland and the point below the intensively farmed land, while dissolved oxygen falls from 9.1 to 4.3. The verifier also confirms the upstream point is the cleanest on both measures, since two distractors assert the opposite.",
  ),

 ("cereals and roots fall from 74 to 51 percent",
  "Recomputed from the record: both columns sum to 100, so the change is compositional, and the staple share falls 23 points while animal products and oils and sugars together rise from 21 to 43 percent. EK IMP-5.A.3 names changing diets first among the societal effects of agricultural practices.",
  ),

 ("settlements and industry may also discharge along the same reach",
  "EK IMP-5.A.1 names pollution among the environmental effects of agricultural land use without claiming farming is the only source. Diffuse agricultural runoff is genuinely hard to separate from other discharges along one stretch of river, which is why the reading must be stated as consistent rather than conclusive."),

 ("including through conservation as well as damage",
  "EK IMP-5.A.1 supplies the environmental effects including conservation, EK IMP-5.A.2 the practices that alter the landscape, and EK IMP-5.A.3 the three societal effects. Each rejected summary drops one of the three statements or reads the first list as containing damage alone."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"5.10 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"5.10 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_land_cover,
    27: q27_water_quality,
    28: q28_diet_composition,
}

geo_check.check(g5_10, ANCHORS, TABLE_NOTES)
