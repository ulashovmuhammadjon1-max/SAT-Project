"""Key audit for AP HUMAN GEOGRAPHY 5.1 Introduction to Agriculture.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. One learning objective, three essential knowledge statements:

    PSO-5.A   Explain the connection between physical geography and
              agricultural practices.
    PSO-5.A.1 Agricultural practices are influenced by the physical environment
              and climatic conditions, such as the Mediterranean climate and
              tropical climates.
    PSO-5.A.2 Intensive farming practices include market gardening, plantation
              agriculture, and mixed crop-livestock systems.
    PSO-5.A.3 Extensive farming practices include shifting cultivation, nomadic
              herding, and ranching.

WHAT THE CED DOES NOT SUPPLY, and the reason this file states it explicitly: no
definition of intensive or extensive. PSO-5.A.2 and PSO-5.A.3 are bare lists. The
criterion used in every claim below is the standard one -- inputs of labour and
capital PER UNIT OF LAND. It is a ratio to AREA, not to output and not to the
worker.

That distinction is the whole difficulty of the topic. It is why plantation
agriculture, which occupies very large estates, sits on the INTENSIVE list: what
is measured is how much labour and capital each hectare receives, not how many
hectares there are. Items 4, 5, 13, 14, 21, 26, 28 and 29 all rest on it; item 13
asks for the plantation case directly and item 21 keys against the other half of
the confusion, since a mechanized extensive farm can have very high output per
WORKER while remaining extensive.

THE SECOND TRAP is reading PSO-5.A.1 as environmental determinism. The CED's verb
is INFLUENCED BY, and the statement's own examples defeat the stronger reading:
tropical climates carry plantation agriculture from the intensive list and
shifting cultivation from the extensive one, which are about as unlike as two
entries in this topic can be. Items 2, 15, 17, 18, 23, 24 and 30 are built on
that, and item 18 supplies the mechanism -- irrigation does not change the
climate, it changes the cost of working around it.

WHAT IS ASSERTED ABOUT CLIMATE, and nothing beyond it: a Mediterranean climate
has hot dry summers and mild wet winters, so warmth and water arrive in different
seasons; a wet tropical climate is warm year-round with heavy rainfall and
heavily leached soils, so fertility is held in the vegetation rather than the
ground; arid and semi-arid land grows grass unreliably. Each of those is a
physical fact from which the agricultural consequence follows directly. No claim
is made anywhere in this module about which country grows which crop.

SYNONYM CARE. `geo_check` treats {"shifting cultivation", "swidden agriculture",
"slash-and-burn agriculture"} as one construct and {"pastoral nomadism",
"nomadic herding"} as another. No choice list here offers two names for one
practice, which would make the item unanswerable in a way a duplicate-string
check would never see.

The three table items (26, 27, 28) are the computational gate:

  26  labour divided by area for all four systems, so the ranking is derived
      rather than asserted -- and the recompute checks that the most intensive
      system is NOT the one with the largest labour force, since that is the
      confusion the distractors are built on
  27  the warmest quarter is confirmed to be the driest, which is the entire
      agricultural content of a Mediterranean climate
  28  hectares per worker and capital per hectare, both checked to be two orders
      of magnitude below the rest of the table

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written. One distractor was rewritten during the pass: item 26 originally
offered "System 2 is the most intensive because it uses 900 worker-days" when
System 1 uses 1,800, so the distractor's own premise made it self-defeating. It
now reads that System 2 applies more labour than every holding larger than it,
which is true from the table and still the wrong conclusion.
"""
import re

import geo_check
import g5_1


def q26_labour_per_hectare(table):
    """Intensity is labour divided by AREA, not total labour."""
    per_ha = {}
    labour = {}
    for name, area, work in table["rows"]:
        a = float(area.replace(",", ""))
        w = float(work.replace(",", ""))
        labour[name] = w
        per_ha[name] = w / a
    assert abs(per_ha["System 1"] - 300) < 0.01, per_ha
    assert abs(per_ha["System 2"] - 7.5) < 0.01, per_ha
    assert abs(per_ha["System 3"] - 0.2) < 0.001, per_ha
    assert abs(per_ha["System 4"] - 15) < 0.01, per_ha
    assert max(per_ha, key=per_ha.get) == "System 1", per_ha
    assert min(per_ha, key=per_ha.get) == "System 3", per_ha
    # The largest holding must not also be the largest labour force, or the
    # item would not separate intensity from total inputs.
    assert max(labour, key=labour.get) == "System 1", labour
    assert labour["System 2"] > labour["System 3"], labour
    return "300 worker-days per hectare"


def q27_warmest_is_driest(table):
    """Mediterranean seasonality: the hot quarter is the dry one."""
    temps = {r[0]: float(r[1]) for r in table["rows"]}
    rain = {r[0]: float(r[2]) for r in table["rows"]}
    warmest = max(temps, key=temps.get)
    driest = min(rain, key=rain.get)
    coolest = min(temps, key=temps.get)
    wettest = max(rain, key=rain.get)
    assert warmest == driest, (temps, rain)
    assert coolest == wettest, (temps, rain)
    assert rain[driest] == 15, rain
    assert rain[wettest] > 20 * rain[driest], rain
    return f"only {rain[driest]:.0f} millimetres"


def q28_extensive_ratios(table):
    """Hectares per worker and capital per hectare, both far below the rest."""
    ha_per_worker, cap_per_ha = {}, {}
    for name, area, workers, capital in table["rows"]:
        a = float(area.replace(",", ""))
        ha_per_worker[name] = a / float(workers)
        cap_per_ha[name] = float(capital.replace(",", ""))
    assert max(ha_per_worker, key=ha_per_worker.get) == "Holding Y", ha_per_worker
    assert min(cap_per_ha, key=cap_per_ha.get) == "Holding Y", cap_per_ha
    assert ha_per_worker["Holding Y"] == 1000, ha_per_worker
    assert cap_per_ha["Holding Y"] == 12, cap_per_ha
    others = [v for k, v in ha_per_worker.items() if k != "Holding Y"]
    assert ha_per_worker["Holding Y"] > 100 * max(others), ha_per_worker
    return "12 currency units of capital per hectare"


CLAIMS = [
 ("influenced by the physical environment and climatic conditions",
  "EK PSO-5.A.1 states that agricultural practices are influenced by the physical environment and climatic conditions. The verb is the point: the environment fixes what is possible and what is costly, while what is actually farmed also answers to markets, technology and culture."),

 ("drought-tolerant through the summer",
  "EK PSO-5.A.1 names the Mediterranean climate among its examples of climatic influence, and that climate's defining feature is that warmth and rain arrive in different seasons. An unirrigated crop must therefore survive the dry warm months or finish growing before they begin."),

 ("Plantation agriculture",
  "EK PSO-5.A.2 names plantation agriculture among the intensive practices and EK PSO-5.A.1 names tropical climates among the conditions influencing practice. Year-round warmth and rainfall permit perennial export crops that a frost would kill, which is why such crops concentrate in the tropics."),

 ("applied to each unit of land, so a small area is worked hard",
  "The CED gives two lists and no criterion, so this module uses the standard one: intensity is inputs of labour and capital per unit of AREA. Total output and output per worker are different ratios and can point in the opposite direction from intensity."),

 ("so a large area is needed",
  "EK PSO-5.A.3 names shifting cultivation, nomadic herding and ranching as extensive practices, and all three spread modest inputs across a wide area. Land is substituting for labour and capital, which is why extensive systems occur where land is cheap relative to both."),

 ("Market gardening, an intensive practice",
  "EK PSO-5.A.2 names market gardening among the intensive practices. A few hectares worked continuously for perishable, high-value produce is the defining case, and perishability is what ties the holding to a market it can reach the same day."),

 ("Market gardening, plantation agriculture",
  "EK PSO-5.A.2 names exactly market gardening, plantation agriculture and mixed crop-livestock systems. The list repays memorizing because plantation agriculture occupies large estates, which makes it the entry students most often move to the extensive list."),

 ("Shifting cultivation, nomadic herding",
  "EK PSO-5.A.3 names exactly shifting cultivation, nomadic herding and ranching. All three apply modest labour and capital across a wide area, which is the property the category records and the reason the three appear together."),

 ("extensive because the household needs a large area of land over time",
  "EK PSO-5.A.3 names shifting cultivation among the extensive practices. The plot in cultivation is small, but the fallow land regenerating around it belongs to the system, so the land a household requires over one full cycle is large."),

 ("extensive practice suited to land too dry or too variable",
  "EK PSO-5.A.3 names nomadic herding as an extensive practice and EK PSO-5.A.1 ties practice to the physical environment. Where rainfall is too low and too erratic to risk a crop, moving animals to wherever grass has actually grown converts an unreliable resource into food."),

 ("Ranching, an extensive practice",
  "EK PSO-5.A.3 names ranching among the extensive practices. The land is held permanently and receives very little labour or capital per hectare, which separates it both from herding across land nobody fences and from systems that crop the same ground."),

 ("the same land supports two enterprises",
  "EK PSO-5.A.2 names mixed crop-livestock systems among the intensive practices. Linking crops and animals keeps each hectare producing through more of the year and closes the nutrient cycle on the farm, which is a high level of management per unit of land."),

 ("labour and capital per unit of land, and a plantation's processing",
  "EK PSO-5.A.2 places plantation agriculture on the intensive list, and estate size is not the criterion. A perennial export crop that must be planted, tended, harvested by hand and often processed on site absorbs a great deal of labour and capital on every hectare it occupies."),

 ("since intensity compares inputs with land area rather than with output",
  "Intensity is the ratio of labour and capital to AREA, so two farms with equal output tell a geographer nothing about it until the area is known. Five workers per hectare against one worker per 225 hectares is the comparison the two categories are built on."),

 ("Climate sets the limits and the costs",
  "EK PSO-5.A.1 says practices are INFLUENCED by the physical environment and climatic conditions rather than determined by them. Tropical climates carry plantation agriculture from the intensive list and shifting cultivation from the extensive one, which settles the matter from inside the CED's own examples."),

 ("Soil depth and fertility, slope, and the availability of water",
  "EK PSO-5.A.1 names the physical environment alongside climatic conditions. Thin soils, steep ground and absent water restrict what can be grown and how it must be grown, which is why terracing, irrigation and grazing appear where they do."),

 ("Burning returns nutrients to the surface",
  "EK PSO-5.A.1 connects practice to the physical environment and EK PSO-5.A.3 names shifting cultivation as an extensive practice. Where continuous rainfall leaches the soil, fertility is held in the standing vegetation rather than the ground, so clearing, cropping and fallow follow from the physical facts."),

 ("Technology can relax a climatic constraint",
  "EK PSO-5.A.1's verb is 'influenced', and irrigation is the clearest illustration of why that verb was chosen. The dry summer remains a physical fact; what has changed is the cost of working around it, which is exactly the kind of change that shifts a practice without shifting a climate."),

 ("Ranching with extensive",
  "EK PSO-5.A.2 lists market gardening, plantation agriculture and mixed crop-livestock systems as intensive and EK PSO-5.A.3 lists shifting cultivation, nomadic herding and ranching as extensive. Only one pairing here puts a practice on the list the framework puts it on."),

 ("so it becomes rational to substitute more land for labour and capital",
  "EK PSO-5.A.2 and EK PSO-5.A.3 divide practices by how hard each hectare is worked, and the price of a hectare is what makes working it hard worthwhile. A farmer economizes on whichever input is dear, which is land near a city and labour and capital far from one."),

 ("output per worker on a mechanized extensive farm",
  "Extensive systems yield little per hectare by construction, but that is a statement about the denominator. A grain farm worked by two operators with large machinery can produce enormous quantities per person, and confusing the two denominators is the commonest error in this part of the course."),

 ("which depends on moving animals across wide areas",
  "EK PSO-5.A.3 names nomadic herding as an extensive practice, and its extensiveness is a matter of mobility across a large area rather than of the size of any one holding. The other four practices are conducted on land held in one place, so partition does not remove their basis."),

 ("without the two regions farming identically",
  "EK PSO-5.A.1 says practice is influenced by climatic conditions and offers the Mediterranean climate as an example, which implies the influence travels with the climate. Shared climate narrows the range of sensible crops in both places while market access, landholding and technology account for the remaining differences."),

 ("without a frost that would kill it",
  "EK PSO-5.A.1 names tropical climates among the climatic conditions influencing practice and EK PSO-5.A.2 names plantation agriculture as an intensive practice. A perennial crop is years of investment standing in a field, which a frost-free climate protects and a temperate one does not."),

 ("Inputs per hectare vary continuously",
  "EK PSO-5.A.2 and EK PSO-5.A.3 give lists rather than a threshold, and no boundary value appears anywhere in the framework. Cattle on unimproved range and cattle on fertilized irrigated pasture are the same enterprise conducted at very different intensities."),

 ("300 worker-days per hectare",
  "Recomputed from the figures: labour divided by area gives 300, 7.5, 0.2 and 15 worker-days per hectare, so the smallest holding is worked hardest and the largest most lightly. The verifier also checks that the most intensive system is the one with the largest labour force here, so that the distractors built on total labour are wrong for the right reason.",
  ),

 ("The warmest season is also the driest",
  "Recomputed from the figures: the hottest quarter at 27 degrees receives 15 millimetres while the coolest at 11 degrees receives 310, so warmth and water arrive in opposite seasons. EK PSO-5.A.1 names the Mediterranean climate among its examples, and that seasonal mismatch is its whole agricultural consequence.",
  ),

 ("one worker per 1,000 hectares",
  "Recomputed from the figures: one holding records 1,000 hectares per worker and 12 currency units of capital per hectare, against three hectares for nine workers and 4,200 units per hectare at the other end of the record. EK PSO-5.A.3 groups the practices that spread modest labour and capital over a wide area, and both ratios here are two orders of magnitude below the rest.",
  ),

 ("labour and capital applied per hectare",
  "EK PSO-5.A.2 and EK PSO-5.A.3 divide their practices by how heavily each unit of land is worked. Total output, workforce size, distance to a port and the destination of the crop are each compatible with either category, so only the ratio to area decides it."),

 ("divide into intensive and extensive groups the framework lists by name",
  "EK PSO-5.A.1 supplies the influence of environment and climate while EK PSO-5.A.2 and EK PSO-5.A.3 supply the two named lists. Tropical climates carry plantation agriculture from one list and shifting cultivation from the other, which is why no climate maps onto a single category."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"5.1 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"5.1 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_labour_per_hectare,
    27: q27_warmest_is_driest,
    28: q28_extensive_ratios,
}

geo_check.check(g5_1, ANCHORS, TABLE_NOTES)
