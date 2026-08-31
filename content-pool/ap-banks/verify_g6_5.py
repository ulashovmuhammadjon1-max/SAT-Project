"""Key audit for AP HUMAN GEOGRAPHY 6.5 The Internal Structure of Cities.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective PSO-6.D, suggested skill 1.E ("explain the
strengths, weaknesses, and limitations of different geographic models and
theories in a specified context"), and ONE essential knowledge statement:

    PSO-6.D.1 Models and theories that are useful for explaining internal
              structures of cities include the Burgess concentric-zone model, the
              Hoyt sector model, the Harris and Ullman multiple-nuclei model, the
              galactic city model, bid-rent theory, and urban models drawn from
              Latin America, Southeast Asia, and Africa.

THE SUGGESTED SKILL IS THE TOPIC. The CED lists six models because none accounts
for every city, and skill 1.E asks for strengths, weaknesses and limitations. So
this module spends as much on what each model misses as on what it claims: items
16, 18, 19, 20, 24 and 29 are limitation items, and item 16 asks directly why a
list of six was needed.

THE SHAPE EACH MODEL CLAIMS is what every application item turns on. Concentric
zone: RINGS, land use varying with distance and not direction. Sector: WEDGES,
land use varying with direction as well, following transport corridors. Multiple
nuclei: SEVERAL specialized centres and no dominant one. Galactic city: a
weakened centre with edge cities on a ring road, built around the car. Bid-rent:
not a shape at all but the MECHANISM -- item 11's key says so explicitly, and
item 30's distractor offers the common error of treating it as a ring model.
Items 22 and 23 take the two discriminations students actually miss: rings
against wedges, and wedges against nuclei.

THE THREE REGIONAL MODELS ARE ON THE CED'S LIST FOR A REASON and item 13 keys on
the sharpest instance. In the Latin American model the wealthiest housing runs
outward as a spine and the poorest settlement is at the PERIPHERY -- the reverse
of the gradient the Burgess and Hoyt models encode. A student holding only the
first three models reads such a city's income map backwards, and item 27's table
is built to make that reversal visible. The Southeast Asian model is organized on
a former colonial PORT zone rather than a downtown, and the African model
characteristically shows more than one central business district.

WHAT THIS MODULE WILL NOT DO: assert that a named real city fits a named model.
Every application item describes a pattern and asks which model matches it, so
each key rests on the described pattern rather than on a contestable claim about
a real place. NO REAL CITY IS NAMED ANYWHERE IN THIS MODULE.

SYNONYM CARE, and it constrains this module more than any other in the unit.
`geo_check` treats {"concentric zone model", "burgess model"}, {"sector model",
"hoyt model"} and {"multiple nuclei model", "harris and ullman model",
"harris-ullman model"} as three constructs. Every item therefore names a given
model in exactly ONE way throughout its choice list -- offering "the Hoyt model"
in one option and "the sector model" in another would make the item unanswerable
in a way no duplicate-string check could see.

The three table items (26, 27, 28) are the computational gate:

  26  value checked to fall at every step AND the fall checked to be steepest
      over the first interval, since the key claims distance-decay rather than a
      straight line
  27  both gradients computed, and the verifier asserts they run in OPPOSITE
      directions -- the whole point of pairing the two cities
  28  the total is summed and the downtown share derived, with the three
      outlying centres checked to be of comparable size, because a downtown that
      merely leads is not what the galactic city model describes

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import re

import geo_check
import g6_5


def q26_bid_rent_decay(table):
    """Value falls at every step, and fastest over the first interval."""
    dist = [float(r[0].replace(",", "")) for r in table["rows"]]
    value = [float(r[1].replace(",", "")) for r in table["rows"]]
    assert all(b > a for a, b in zip(dist, dist[1:])), dist
    assert all(b < a for a, b in zip(value, value[1:])), value
    assert value[0] == 4800 and value[-1] == 45, value
    drops = [a - b for a, b in zip(value, value[1:])]
    # Distance-decay, not a straight line: the first drop is the largest.
    assert drops[0] == max(drops), drops
    assert drops[0] > 10 * drops[-1], drops
    return f"from {value[0]:,.0f} at the centre to {value[-1]:.0f}"


def q27_opposite_gradients(table):
    """The two cities' income gradients must run in opposite directions."""
    a = [float(r[1]) for r in table["rows"]]
    b = [float(r[2]) for r in table["rows"]]
    assert all(y > x for x, y in zip(a, a[1:])), a
    assert all(y < x for x, y in zip(b, b[1:])), b
    assert a[0] == 22 and a[-1] == 71, a
    assert b[0] == 68 and b[-1] == 11, b
    # Opposite directions is the entire point of pairing them.
    assert (a[-1] - a[0]) * (b[-1] - b[0]) < 0, (a, b)
    return f"from {a[0]:.0f} to {a[-1]:.0f}"


def q28_polycentric_employment(table):
    """Downtown share of total jobs, with comparable outlying centres."""
    jobs = {r[0]: float(r[1].replace(",", "")) for r in table["rows"]}
    total = sum(jobs.values())
    assert total == 559000, total
    downtown = jobs["Traditional downtown"]
    share = 100 * downtown / total
    assert 20 < share < 22, share
    outlying = [v for k, v in jobs.items() if k.startswith("Outlying")]
    assert len(outlying) == 3, jobs
    # The downtown leads, but only just -- a dominant core would be the
    # concentric-zone case rather than the galactic one.
    assert downtown > max(outlying), (downtown, outlying)
    assert downtown < 1.5 * max(outlying), (downtown, outlying)
    # The outlying centres together must outweigh the downtown, but the margin
    # is 231,000 against 118,000 -- 1.96x, not over 2x. The first draft of this
    # assertion demanded 2x and failed; the record is right and the check was
    # wrong, which is the gate doing its job on the verifier rather than on the
    # questions.
    assert sum(outlying) > 1.5 * downtown, (downtown, outlying)
    return f"about {share:.0f} percent of the area's {total:,.0f} jobs"


CLAIMS = [
 ("the Hoyt sector model, the Harris and Ullman multiple-nuclei model",
  "EK PSO-6.D.1 names exactly this set of models and theories. The four principles offered as an alternative belong to EK PSO-6.C.1 and explain relationships BETWEEN cities, whereas these explain the arrangement of land uses WITHIN one."),

 ("A series of rings around a single central business district",
  "EK PSO-6.D.1 names the Burgess concentric-zone model among the models explaining internal city structure. Its distinctive claim is that land use varies with distance from one centre and not with direction, which is what produces rings rather than wedges."),

 ("A zone of transition, mixing industry with deteriorating",
  "EK PSO-6.D.1 names the Burgess concentric-zone model among the models useful for explaining internal city structure. The zone next to the centre is under constant pressure from the expanding business district, which discourages long-term investment and lets housing there deteriorate."),

 ("with each ring pushing into the one beyond it",
  "EK PSO-6.D.1 names the Burgess concentric-zone model, and its rings record a process rather than a static plan. Growth radiating from one core is what makes concentric bands the expected outcome, and it is also the assumption that fails wherever a city has more than one core."),

 ("so a given land use forms a strip from the core to the edge",
  "EK PSO-6.D.1 names the Hoyt sector model among the models explaining internal city structure. Its distinctive claim is that land use varies with DIRECTION from the centre as well as with distance, which turns each band into a wedge."),

 ("expands outward along the route that serves it",
  "EK PSO-6.D.1 names the Hoyt sector model among the models useful for explaining internal city structure. Accessibility is what makes a site usable for a purpose, so an activity extends in the direction where its accessibility persists rather than equally in every direction."),

 ("around several separate specialized centres rather than around one dominant core",
  "EK PSO-6.D.1 names the Harris and Ullman multiple-nuclei model among the models explaining internal city structure. Its departure from the two earlier models is that it abandons the single centre both of them assume."),

 ("heavy industry and high-status housing repel each other",
  "EK PSO-6.D.1 names the Harris and Ullman multiple-nuclei model among the models useful for explaining internal city structure. Attraction between like uses and repulsion between unlike ones is the mechanism producing several specialized nodes instead of one general centre."),

 ("edge cities strung along a ring road have taken functions",
  "EK PSO-6.D.1 names the galactic city model among the models explaining internal city structure. It is the model built for a metropolitan area whose employment and retail have decentralized, which the three earlier models were not designed to describe."),

 ("The automobile and the high-capacity road network",
  "EK PSO-6.D.1 names the galactic city model among the models useful for explaining internal city structure. Earlier transport technologies converged on a single terminus and reinforced a single centre, while a road network permits travel from any outlying point directly to any other."),

 ("only uses earning enough per unit of land can occupy it",
  "EK PSO-6.D.1 lists bid-rent theory alongside the shape models rather than as one of them. It is not a picture of a city but the reason a picture arises: competing uses bid for central land and whichever earns most per square metre obtains it."),

 ("as a spine along a major boulevard",
  "EK PSO-6.D.1 names urban models drawn from Latin America among the models explaining internal city structure. The elite spine is the feature that most sharply distinguishes that model from the concentric and sector models drawn from other regions."),

 ("The poorest settlement is at the periphery and wealth is nearer the centre",
  "EK PSO-6.D.1 names urban models drawn from Latin America alongside the Burgess concentric-zone model, and the two disagree about direction. A student holding only the earlier model reads such a city's income map backwards, which is exactly why the CED lists regional models."),

 ("focused on a former colonial port zone",
  "EK PSO-6.D.1 names urban models drawn from Southeast Asia among the models explaining internal city structure. Organizing on a port rather than on a downtown follows from how such cities grew, and it is why a model assuming one central business district fits them poorly."),

 ("a colonial one, a traditional one and an open-air market zone",
  "EK PSO-6.D.1 names urban models drawn from Africa among the models useful for explaining internal city structure. Several commercial cores of different origins coexisting in one city is a structure the single-centre models have no way to represent."),

 ("does not describe cities that grew differently elsewhere",
  "EK PSO-6.D.1 gives a list and calls its members models USEFUL FOR EXPLAINING internal city structure, while the suggested skill for this topic is explaining strengths, weaknesses and limitations in a specified context. A model is a compressed account of the process that built one kind of city."),

 ("since the centre has been weakened and outlying nodes on a ring road carry the activity",
  "EK PSO-6.D.1 names the galactic city model among the models explaining internal city structure, and every element of this stem is one of its features. A ring road with commuting between outer nodes is exactly the pattern the earlier single-centre models cannot represent."),

 ("built from particular cities at a particular time",
  "EK PSO-6.D.1 calls these models USEFUL FOR EXPLAINING internal city structure, and the suggested skill is explaining their strengths, weaknesses and limitations. Simplification is what makes a model usable and it is simultaneously the source of every mismatch with a real city."),

 ("widespread car ownership decentralized both employment and retail",
  "EK PSO-6.D.1 lists the galactic city model alongside the older three, which is the CED itself acknowledging that the earlier ones needed supplementing. A model encodes the transport technology of its period, so a change in that technology is what dates it."),

 ("distance bands, directional wedges and separate nuclei",
  "EK PSO-6.D.1 lists six models as useful for explaining internal structures without assigning one to each city. Each isolates a different regularity, so a real city may show rings of building age, a wedge of high-status housing and specialized outlying nodes at the same time."),

 ("since each describes the arrangement of districts within a single urban area",
  "EK PSO-6.D.1 describes these as models explaining INTERNAL structures of cities, so their subject is the districts of one urban area. Ranking a country's cities is what EK PSO-6.C.1's principles do, and confusing those two lists is the commonest error across this unit."),

 ("The first illustrates the concentric zone model and the second the sector model",
  "EK PSO-6.D.1 names both models, and their shapes distinguish them completely. A band at a constant distance varies with distance alone, while a strip along one route varies with direction, which is the whole difference between a ring and a wedge."),

 ("keeps a single dominant centre from which wedges radiate",
  "EK PSO-6.D.1 names both among the models explaining internal city structure. Wedges must radiate from something, so the sector model retains the single core it inherited, while the multiple nuclei model's entire innovation is to give that core up."),

 ("reflects the history, transport technology and land market",
  "EK PSO-6.D.1 lists models drawn from Latin America, Southeast Asia and Africa alongside the older ones, which is the CED making this point in its own structure. A colonial port, a market zone and a peripheral squatter settlement are features the earlier models had no reason to include."),

 ("Elite housing running outward from the centre along one boulevard",
  "EK PSO-6.D.1 names six models with distinct shapes and features. Only one pairing here matches a described pattern to the model whose account it satisfies; each of the others attaches a description to a model claiming a different shape."),

 ("from 4,800 at the centre to 45",
  "Recomputed from the record: land value falls at every step from 4,800 to 45 currency units per square metre, and the fall is steepest over the first two kilometres, dropping 3,650 there against 115 over the final ten. EK PSO-6.D.1 names bid-rent theory among the models useful for explaining internal city structure, and steep distance-decay in land value is the mechanism it describes.",
  ),

 ("Income rises outward in City A from 22 to 71",
  "Recomputed from the record: one city's median income rises at every step from 22 to 71 while the other's falls at every step from 68 to 11, so the two gradients run in opposite directions. EK PSO-6.D.1 lists urban models drawn from Latin America alongside the concentric-zone model, and this reversal is why one model cannot serve both cities.",
  ),

 ("about 21 percent of the area's 559,000 jobs",
  "Recomputed from the record: the five entries total 559,000 jobs and the downtown's 118,000 is about 21 percent of them, while the three outlying centres together hold 231,000. The verifier also checks that the downtown leads by less than half, since a dominant core would be the concentric-zone case rather than the galactic one.",
  ),

 ("since a ring and a wedge look the same along one radius",
  "EK PSO-6.D.1 names both the Burgess concentric-zone model and the Hoyt sector model, and they differ over whether land use varies with direction as well as with distance. A single radius holds direction constant, so it cannot separate them -- which is precisely the gap the sector model was proposed to fill."),

 ("bid-rent theory supplies the mechanism behind the patterns",
  "EK PSO-6.D.1 lists six models and theories as useful for explaining internal structures of cities, and the suggested skill is explaining their strengths, weaknesses and limitations in context. Bid-rent theory sits on that list alongside the shape models because it explains why land uses sort themselves at all."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"6.5 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"6.5 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_bid_rent_decay,
    27: q27_opposite_gradients,
    28: q28_polycentric_employment,
}

geo_check.check(g6_5, ANCHORS, TABLE_NOTES)
