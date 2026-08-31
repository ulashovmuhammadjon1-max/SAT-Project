"""Key audit for AP HUMAN GEOGRAPHY 5.3 Agricultural Origins and Diffusions.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Two learning objectives, one statement each:

    SPS-5.A   Identify major centers of domestication of plants and animals.
    SPS-5.A.1 Early hearths of domestication of plants and animals arose in the
              Fertile Crescent and several other regions of the world, including
              the Indus River Valley, Southeast Asia, and Central America.
    SPS-5.B   Explain how plants and animals diffused globally.
    SPS-5.B.1 Patterns of diffusion, such as the Columbian Exchange and the
              agricultural revolutions, resulted in the global spread of various
              plants and animals.

WHAT THIS MODULE DELIBERATELY DOES NOT ASSERT, and why it matters more here than
in most topics: the CED names four hearths and two patterns of diffusion, and it
attaches NO crop to any hearth and NO date to any of them. Everything beyond
those two sentences is content this module is adding, so the additions are held
to a strict line:

  - Crop-to-hearth attributions appear only where they are not in scholarly
    dispute -- wheat and barley with the Fertile Crescent (items 3, 10), maize,
    beans and squash with Central America (item 4), rice with Southeast Asia
    (item 5). NOTHING is attributed to the Indus River Valley beyond the CED's
    own sentence naming it as a hearth. The Indus appears only as a name in the
    list and as a distractor, never as a key resting on a crop. That is a
    deliberate cut: the attributions available for it are contested, and
    SOCIAL_BRIEF.md's rule is that an uncertain key is cut rather than guessed.
  - NO DATE is attached to a NAMED hearth anywhere in the module. Item 27 uses
    four unlabelled hearths so that reasoning about sequence and independence can
    be tested without asserting an archaeological date the CED never supplies.
  - Columbian Exchange directions are used only for organisms whose hemisphere
    of origin is settled: maize, potatoes, tomatoes and cacao from the Americas;
    wheat, rice, sugarcane, coffee, cattle, pigs and horses from the Old World.

THE WORD "SEVERAL" IN SPS-5.A.1 carries the topic's main idea and items 6 and 29
key on it. The statement says hearths arose in the Fertile Crescent AND SEVERAL
OTHER REGIONS, which asserts multiple INDEPENDENT origins rather than one origin
followed by diffusion everywhere. That is also what makes the topic's two
learning objectives distinct: SPS-5.A asks where farming began, in the plural,
and SPS-5.B asks how its products then travelled.

THE DIRECTION OF THE COLUMBIAN EXCHANGE is the most reversible fact in the
topic, because the crops that became Old World staples came FROM the Americas
while the livestock that reshaped American landscapes came FROM the Old World.
Items 10, 11, 12, 13, 26 and 28 are built on that crossing, and each of them
offers the reversed list as a distractor.

The three table items (26, 27, 28) are the computational gate:

  26  counts species by hemisphere of domestication and checks that every one
      became important in both -- the key is a claim about the exchange being
      two-way, so a count in only one direction would not support it
  27  the span between earliest and latest evidence and the minimum distance
      between hearths, since the key rests on the hearths being far apart AND
      spread over millennia
  28  both share columns are checked to sum to 100 in every period, which is
      what makes the item a claim about composition rather than about the size
      of the food supply

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import re

import geo_check
import g5_3


def q26_two_way_exchange(table):
    """Four species each way, and every one important in both hemispheres after."""
    origin = {}
    for species, domesticated, after in table["rows"]:
        origin.setdefault(domesticated, []).append(species)
        # The claim is a two-way spread, so every row must end up in both.
        assert after == "Both", (species, after)
    assert set(origin) == {"Americas", "Old World"}, origin
    assert len(origin["Americas"]) == len(origin["Old World"]) == 4, origin
    words = {4: "Four"}
    return f"{words[len(origin['Americas'])]} species moved in each direction"


def q27_independent_origins(table):
    """Span between earliest and latest evidence, and the minimum separation."""
    dates = {r[0]: float(r[1].replace(",", "")) for r in table["rows"]}
    gaps = {r[0]: float(r[2].replace(",", "")) for r in table["rows"]}
    span = max(dates.values()) - min(dates.values())
    assert span == 5500, (dates, span)
    assert min(gaps.values()) == 3400, gaps
    # The key rests on BOTH conditions: far apart in space and spread in time.
    assert min(gaps.values()) > 1000, gaps
    assert max(dates, key=dates.get) == "Hearth 1", dates
    return f"within {span:,.0f} years of one another"


def q28_share_rises(table):
    """Composition only: the two shares must sum to 100 in every period."""
    american, old = [], []
    for _, a, o in table["rows"]:
        assert float(a) + float(o) == 100, (a, o)
        american.append(float(a))
        old.append(float(o))
    assert american[0] == 0, american
    assert american[-1] == 31, american
    assert all(b >= a for a, b in zip(american, american[1:])), american
    assert old[-1] > 0, old        # Old World crops do not disappear
    return f"to {american[-1]:.0f} percent"


CLAIMS = [
 ("the Indus River Valley, Southeast Asia, and Central America",
  "EK SPS-5.A.1 names the Fertile Crescent and several other regions including the Indus River Valley, Southeast Asia and Central America. The plural is substantive: the statement describes several separate places where domestication arose rather than one source for all of it."),

 ("first brought under human control and bred for human use",
  "EK SPS-5.A.1 speaks of early hearths of domestication, which is a claim about origin and not about present-day output. A crop's largest producer today is very often a place the crop reached long after it had been domesticated somewhere else entirely."),

 ("The Fertile Crescent",
  "EK SPS-5.A.1 names the Fertile Crescent first among its hearths, and the wild ancestors of wheat and barley are native to that region's hills. Domestication has to begin where the wild ancestor lives, which is why hearths are particular places rather than an even distribution."),

 ("Central America",
  "EK SPS-5.A.1 names Central America among its hearths, and maize, beans and squash originated there. The three are grown together because the beans return nitrogen the maize uses and the squash shades the ground, so what diffused was a system and not three separate plants."),

 ("Southeast Asia",
  "EK SPS-5.A.1 names Southeast Asia among the hearths, and rice is the crop most closely associated with it. A crop's hearth is fixed by where its wild ancestor grew rather than by where the largest harvest is taken now."),

 ("so it did not spread from a single source",
  "EK SPS-5.A.1 names several regions rather than one, which is a claim of multiple independent origins. That plural is also what makes SPS-5.A and SPS-5.B two different objectives: one asks where farming began, the other asks how its products later travelled."),

 ("those ancestors were not distributed evenly",
  "EK SPS-5.A.1 identifies hearths as places where domestication of plants and animals arose. A region with excellent soil but no domesticable wild grass or herd animal has nothing to start from, so the map of hearths is a map of biological opportunity rather than of soil quality."),

 ("until they differ from their wild ancestors",
  "EK SPS-5.A.1 refers to hearths of domestication of plants and animals. Domesticated wheat holds its seed on the stalk instead of scattering it and domesticated animals tolerate handling, and each of those is the accumulated result of selection rather than a single discovery."),

 ("between the Americas and the rest of the world after sustained contact",
  "EK SPS-5.B.1 names the Columbian Exchange among the patterns of diffusion that spread plants and animals globally. It is a biological transfer running in both directions rather than a trade in manufactured goods, which is what places it in agricultural geography."),

 ("Maize, potatoes, tomatoes, and cacao",
  "EK SPS-5.B.1 names the Columbian Exchange among the patterns of diffusion, and its most consequential feature is that American crops entered Old World diets. Wheat, rice, sugarcane and coffee travelled the other way, which is the reversal this item is built to catch."),

 ("Cattle, pigs, sheep, and horses",
  "EK SPS-5.B.1 names the Columbian Exchange as a pattern of diffusion that spread plants AND animals. The large domesticated herd animals were Old World species, and their arrival changed American transport, warfare, diet and land use within a few generations."),

 ("where existing staples did poorly",
  "EK SPS-5.B.1 says patterns of diffusion resulted in the global spread of various plants and animals. A new staple that yields well on land where the old ones struggle is an addition to the food supply rather than a substitution for it, which is the mechanism behind the population effects."),

 ("made herding and mounted travel possible",
  "EK SPS-5.B.1 names the Columbian Exchange as a pattern of diffusion spreading animals as well as plants. Grassland is a resource only if something can convert grass into food or transport, and the large herd animals that do so arrived from the Old World."),

 ("including disease pathogens",
  "EK SPS-5.B.1 describes the Columbian Exchange as a pattern of diffusion resulting in a global spread of organisms rather than of crops alone. Where a population collapses or a landscape empties, land use changes with it, which is why a biological transfer belongs in a human geography course."),

 ("changing what could be farmed where",
  "EK SPS-5.B.1 names both the Columbian Exchange and the agricultural revolutions as patterns of diffusion resulting in a global spread of plants and animals. What the two share is reach: something grown or learned in one place became available in places that had not had it."),

 ("since the crop travels with people who have moved",
  "EK SPS-5.B.1 asks how plants and animals diffused globally, and a seed is a physical object that has to be carried rather than an idea that can be copied. Movement of the thing itself with a migrating population is relocation diffusion, which is why ocean crossings dominate this topic."),

 ("share day length and growing season",
  "EK SPS-5.B.1 concerns how plants diffused globally, and a plant is adapted to a particular combination of day length, temperature and season. A crop moved along a line of latitude meets conditions it already suits, while the same distance north or south can put it outside its range."),

 ("One hearth of domestication followed by diffusion",
  "EK SPS-5.A.1 locates domestication in hearths and EK SPS-5.B.1 accounts for the later global spread, so the two statements together predict exactly this signature. A narrow wild range beside a wide cultivated range is what that pair of processes leaves behind, since wild ancestors stay where the plant evolved."),

 ("Northern Europe",
  "EK SPS-5.A.1 names the Fertile Crescent, the Indus River Valley, Southeast Asia and Central America. The phrase 'several other regions' leaves the full list open, but the four the statement actually names are the four a student is responsible for."),

 ("changed field by field",
  "EK SPS-5.B.1 describes a GLOBAL spread of plants and animals, while the adoption of any one crop is a decision taken on a particular holding. One process observed at two scales yields two different pictures, which is a recurring move throughout this course."),

 ("what a place eats and when it works are organized around what it grows",
  "EK SPS-5.B.1 sits under an enduring understanding that agriculture changes through cultural diffusion. A staple crop sets the planting and harvest calendar and the contents of an ordinary meal, so replacing one reorganizes both the working year and the table."),

 ("accumulate over many generations of selection",
  "EK SPS-5.A.1 speaks of hearths where domestication AROSE, which describes an emergence rather than an invention with a date. Seeds that stay on the stalk and animals that tolerate confinement are the outcome of repeated selection, so the change is gradual and has no single beginning."),

 ("most large wild animals cannot be bred into manageable livestock",
  "EK SPS-5.A.1 names hearths of domestication of plants AND animals, and the two need not coincide. A region's stock of candidate species is a fact of biogeography rather than of choice, which is why animal domestication is far more unevenly distributed than plant domestication."),

 ("its foreign origin stops being visible in everyday life",
  "EK SPS-5.B.1 says patterns of diffusion resulted in the global spread of various plants and animals, and says nothing about the receiving culture keeping a record of it. Complete absorption is the ordinary endpoint of a successful diffusion, so a crop's origin usually has to be traced rather than remembered."),

 ("Physical suitability is necessary but not sufficient",
  "EK SPS-5.B.1 sits under an enduring understanding about agriculture changing through CULTURAL diffusion, which makes the receiving society part of the process. Both the potato and the tomato took generations to be accepted in places where they had grown perfectly well from the start."),

 ("Four species moved in each direction",
  "Recomputed from the record: four species were domesticated in the Americas and four in the Old World, and all eight are recorded as important in both hemispheres after 1500. EK SPS-5.B.1 names the Columbian Exchange among the patterns of diffusion that spread plants and animals globally, and a balanced two-way count is what the record shows.",
  ),

 ("within 5,500 years of one another",
  "Recomputed from the figures: the earliest and latest secure evidence differ by 5,500 years, and no hearth lies within 3,400 kilometres of another. EK SPS-5.A.1 says hearths arose in the Fertile Crescent and several other regions, and separation in both space and time is what makes independent origins the reading the record supports.",
  ),

 ("rose from none of the region's food energy to 31 percent",
  "Recomputed from the figures: the two columns sum to 100 in every period, so the record is a claim about composition, and the American share rises from zero before 1500 to 31 percent by the end while Old World crops remain the majority. EK SPS-5.B.1 names the Columbian Exchange among the patterns of diffusion, and a share rising from nothing to nearly a third is what a successful one looks like.",
  ),

 ("multiple independent beginnings",
  "EK SPS-5.A.1's plural is a substantive claim and not a hedge. If domestication arose separately in several regions, the explanation has to be something several distant regions shared, which is a different and harder question than tracing the spread of a single invention."),

 ("later patterns of diffusion including the Columbian Exchange",
  "EK SPS-5.A.1 supplies the several hearths and EK SPS-5.B.1 supplies the global spread through named patterns of diffusion. A single-origin summary contradicts the word 'several' and a one-directional summary contradicts what the Columbian Exchange was."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"5.3 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"5.3 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_two_way_exchange,
    27: q27_independent_origins,
    28: q28_share_rises,
}

geo_check.check(g5_3, ANCHORS, TABLE_NOTES)
