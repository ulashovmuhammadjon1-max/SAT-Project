"""Key audit for AP HUMAN GEOGRAPHY 5.5 The Green Revolution.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. One learning objective and two essential knowledge
statements:

    SPS-5.D   Explain the consequences of the Green Revolution on food supply
              and the environment in the developing world.
    SPS-5.D.1 The Green Revolution was characterized in agriculture by the use
              of high-yield seeds, increased use of chemicals, and mechanized
              farming.
    SPS-5.D.2 The Green Revolution had positive and negative consequences for
              both human populations and the environment.

SPS-5.D.2 IS A TWO-BY-TWO AND THE MODULE IS BUILT ON IT. The sentence crosses
positive against negative and human against environmental, and it asserts that
all four cells are occupied. Items 6 and 7 key the two positive cells, items 9
to 11 the negative human cell and items 12 to 15 the negative environmental one,
so a student who works the module cannot come away holding only one side. Items
16, 23 and 30 key directly against one-sided readings in EITHER direction, which
matters because both are common: "it fed the world" and "it wrecked the soil"
are equally partial accounts of a sentence that says both.

WHY THE THREE CHARACTERISTICS ARE ONE PACKAGE is the mechanism SPS-5.D.1 does
not spell out, and item 5 asks for it directly. A high-yield variety is bred to
put nutrients and water into grain rather than into stem and leaf. It therefore
out-yields a traditional variety ONLY where those nutrients and that water are
supplied, which is what the chemicals, the irrigation and the machinery are for.
That is also why adoption tracked the ability to BUY inputs rather than the
willingness to try them, which is the link between SPS-5.D.1 and the negative
human consequences of SPS-5.D.2 -- items 9, 17, 22 and 28.

"IN THE DEVELOPING WORLD" sits in the learning objective rather than in either
essential knowledge statement, but it fixes where the topic applies and item 21
keys on it. Item 18 uses it as one of the differences from the second
agricultural revolution of EK SPS-5.C.1.

WHAT IS KEPT OUT. Genetically modified organisms belong to Topic 5.11's EK
IMP-5.B.1, not here: the CED characterizes this revolution by high-yield SEEDS
from conventional breeding, and conflating the two would key an item to the
wrong statement. `geo_check` also treats {"monocropping", "monoculture"} and
{"genetically modified organisms", "gmos"} as single constructs, so no choice
list offers two names for either.

The three table items (26, 27, 28) are the computational gate:

  26  both yields checked to more than double and fertilizer to rise more than
      elevenfold, plus the assertion that the cereal AREA is unchanged -- the
      item's claim is that the gain came from the same land, and a growing area
      would let a student reach the key for the wrong reason
  27  the damaged SHARE of irrigated land at both dates, not just the two raw
      areas, since the point is that the cost grew faster than the practice
  28  adoption checked to rise at every step while the farm COUNT falls in the
      same direction, which is what makes the majority of farms the least-
      adopting group

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import re

import geo_check
import g5_5


def q26_yields_and_fertilizer(table):
    """Both yields more than double, fertilizer up elevenfold, area flat."""
    rows = {r[0]: (float(r[1].replace(",", "")), float(r[2].replace(",", "")))
            for r in table["rows"]}
    rice = rows["Rice yield (tonnes per hectare)"]
    wheat = rows["Wheat yield (tonnes per hectare)"]
    fert = rows["Fertilizer applied (kilograms per hectare)"]
    area = rows["Area under cereals (million hectares)"]
    assert rice[1] > 2 * rice[0], rice
    assert wheat[1] > 2 * wheat[0], wheat
    ratio = fert[1] / fert[0]
    assert 11 < ratio < 12, ratio
    # Unchanged area is what makes the gain attributable to yield, not to land.
    assert area[0] == area[1], area
    return "more than elevenfold"


def q27_salinized_share(table):
    """The damaged SHARE of irrigated land, not just the two raw areas."""
    rows = {r[0]: (float(r[1].replace(",", "")), float(r[2].replace(",", "")))
            for r in table["rows"]}
    irr_e, dam_e = rows["Earlier"]
    irr_l, dam_l = rows["Later"]
    assert irr_l == 4 * irr_e, (irr_e, irr_l)
    assert dam_l == 18 * dam_e, (dam_e, dam_l)
    share_e = 100 * dam_e / irr_e
    share_l = 100 * dam_l / irr_l
    assert 4 <= share_e < 4.5, share_e
    assert 18.5 <= share_l < 19.5, share_l
    # The cost must grow faster than the practice, or the key's point fails.
    assert share_l > share_e, (share_e, share_l)
    return f"from about {share_e:.0f} percent to about {share_l:.0f} percent"


def q28_adoption_by_size(table):
    """Adoption rises at every step while the number of farms falls."""
    shares = [float(r[2]) for r in table["rows"]]
    counts = [float(r[1].replace(",", "")) for r in table["rows"]]
    assert all(b > a for a, b in zip(shares, shares[1:])), shares
    assert all(b < a for a, b in zip(counts, counts[1:])), counts
    assert shares[0] == 22 and shares[-1] == 94, shares
    # The least-adopting band must hold the most farms, or the inequality
    # reading in the key would not follow from the record.
    assert counts[0] == max(counts), counts
    return (f"from {shares[0]:.0f} percent on the smallest farms "
            f"to {shares[-1]:.0f} percent on the largest")


CLAIMS = [
 ("increased use of chemicals",
  "EK SPS-5.D.1 names high-yield seeds, increased use of chemicals and mechanized farming as the Green Revolution's three characteristics. Crop rotation and the seed drill belong to the second agricultural revolution, and organic farming and fair trade to EK IMP-5.B.2, so each rejected set names a different part of the course."),

 ("into grain rather than into stem and leaf",
  "EK SPS-5.D.1 names high-yield seeds among the three characteristics, and the gain comes from how the plant allocates what it takes up. That is also why such a variety rewards heavy inputs and is unremarkable without them, which links the first characteristic to the other two."),

 ("and fertilizer is what supplies them",
  "EK SPS-5.D.1 names high-yield seeds and increased chemical use in the same sentence, and they are complements rather than alternatives. A variety able to use more nitrogen yields more grain only where more nitrogen is actually applied to the field."),

 ("on a tighter schedule",
  "EK SPS-5.D.1 names mechanized farming as the third characteristic. A system carrying more inputs, tighter timing and often more than one crop a year cannot be run at the pace hand tools allow, so the three characteristics support one another rather than substituting."),

 ("adopting one part without the others gives little benefit",
  "EK SPS-5.D.1 lists the three together as the characterization of one thing. The seed is what makes the other inputs worth buying and the inputs are what make the seed worth planting, which is why the package spread or failed to spread as a whole rather than piecemeal."),

 ("Cereal output rose faster than population",
  "EK SPS-5.D.2 states that the Green Revolution had positive and negative consequences for both human populations and the environment. Feeding a growing population from a land area that did not grow is the clearest positive human consequence, and every rejected option here names a cost."),

 ("reduced the pressure to clear additional forest",
  "EK SPS-5.D.2 says the consequences were positive and negative for the environment as well as for people, and this is the positive environmental cell. Raising output per hectare means a given food requirement is met from a smaller area, which is a gain set against the four costs offered alongside it."),

 ("lowered the real price of staple grain",
  "EK SPS-5.D.2 names positive consequences for human populations, and cheaper staple food is among the largest. A price fall is a gain to buyers and a squeeze on sellers, so the people who buy their food benefit most directly while producers face lower returns per tonne."),

 ("had to be bought each season",
  "EK SPS-5.D.2 names negative as well as positive consequences for human populations, and EK SPS-5.D.1's three characteristics are all purchased inputs. Adoption therefore tracked the ability to pay, and a technology that raises the income of those who can buy it widens the distance to those who cannot."),

 ("Indebtedness, since the inputs must be paid for",
  "EK SPS-5.D.2 records negative consequences for human populations. A system built on purchased inputs converts a bad season from a lean year into a debt, because the costs were incurred months before the harvest failed to arrive."),

 ("replaced tasks that had employed hired labour",
  "EK SPS-5.D.1 names mechanized farming among the characteristics and EK SPS-5.D.2 names negative consequences for human populations. Ploughing, threshing and harvesting by machine displaces precisely the seasonal wage work that landless rural households live on."),

 ("feed algal growth, whose decay strips oxygen",
  "EK SPS-5.D.2 names negative environmental consequences, and fertilizer runoff is the standard case. What is a nutrient in a field is a nutrient in water too, so the damage is an over-feeding whose consequence is oxygen depletion rather than a direct poisoning."),

 ("kill organisms beyond the target pest",
  "EK SPS-5.D.1 names increased use of chemicals among the characteristics and EK SPS-5.D.2 names negative environmental consequences. A compound designed to kill one organism rarely distinguishes perfectly between species, which is why the effects travel beyond the field it was applied to."),

 ("where evaporation exceeds drainage",
  "EK SPS-5.D.2 names negative environmental consequences, and salinization is among the most serious for irrigated land. The salt was always dissolved in the water; what changes is that repeated evaporation concentrates it at the surface until the ground will no longer carry a crop."),

 ("damaged by a single pest or disease that all of them share a vulnerability to",
  "EK SPS-5.D.2 names negative environmental consequences of the Green Revolution, and narrowed crop diversity is one of them. Diversity across a landscape acts as insurance, since a pathogen that defeats one variety meets a different defence in the next field."),

 ("positive and negative, for human populations and for the environment alike",
  "EK SPS-5.D.2 says in a single sentence that the Green Revolution had positive AND negative consequences for both human populations and the environment. A one-sided account is not a stronger version of the framework's claim but a different and weaker one."),

 ("regions without them could not run the package",
  "EK SPS-5.D.1's three characteristics all have to be delivered and paid for, and EK SPS-5.D.2 records that consequences differed. Where water could not be controlled or inputs could not be bought and moved, the seed by itself produced no revolution at all."),

 ("largely twentieth-century change centred on the developing world",
  "EK SPS-5.C.1 describes the second agricultural revolution's technology and social impacts while EK SPS-5.D.1 characterizes this one by high-yield seeds, chemicals and mechanization. Learning objective SPS-5.D further locates its consequences in the developing world, which is a second difference between them."),

 ("Producing food and being able to obtain it are different things",
  "EK SPS-5.D.2 names both positive and negative consequences for human populations, and the two can hold in one country at once. Output is measured nationally while eating happens in a household, so purchasing power and distribution decide who actually gains from an aggregate rise."),

 ("a triumph, an unevenness and a debt at those three scales",
  "EK SPS-5.D.2 names consequences that are positive and negative simultaneously, which is possible because they fall on different people in different places. Choosing one scale and stopping there is exactly how a student ends up holding half the statement."),

 ("The developing world",
  "Learning objective SPS-5.D asks students to explain the consequences of the Green Revolution on food supply and the environment IN THE DEVELOPING WORLD. That location is part of what distinguishes this topic from the earlier agricultural revolutions in the same unit."),

 ("available in principle but not in practice",
  "EK SPS-5.D.1's three characteristics are all purchased, and EK SPS-5.D.2 records negative as well as positive consequences for human populations. Availability and affordability are different conditions, and it is the second that decides who adopts and therefore who gains."),

 ("the distribution of the gains to be weighed alongside the yield figure",
  "EK SPS-5.D.2 names consequences for human populations AND the environment, positive and negative alike. A yield figure speaks to one cell of that account, and the structure of the sentence is what makes the other three part of the question."),

 ("in the amounts and at the times the crop can actually use",
  "EK SPS-5.D.2 names both positive and negative consequences, which frames the problem as keeping the first while reducing the second. Runoff, salinization and falling water tables all follow from applying more than the crop takes up, so matching application to uptake attacks the cost without surrendering the gain."),

 ("which is what Malthus's argument said could not be sustained",
  "EK SPS-5.D.2 names positive consequences for human populations, the largest being that more people were fed than the earlier trend implied could be. Whether that gain can be repeated indefinitely is the open question, which is where the statement's environmental costs re-enter the argument."),

 ("more than elevenfold on an unchanged area",
  "Recomputed from the figures: rice rises from 1.9 to 4.6 and wheat from 1.1 to 3.2 tonnes per hectare, both more than doubling, while fertilizer rises from 8 to 92 kilograms per hectare and the cereal area is identical in both columns. EK SPS-5.D.1 names high-yield seeds and increased chemical use together, and the record shows them moving together on land already in cultivation.",
  ),

 ("from about 4 percent to about 19 percent",
  "Recomputed from the figures: irrigated area rises fourfold while salt-damaged area rises eighteenfold, so the damaged share of irrigated land rises from about 4 to about 19 percent. EK SPS-5.D.2 names negative environmental consequences, and a cost growing faster than the practice producing it is what the record establishes.",
  ),

 ("from 22 percent on the smallest farms to 94 percent on the largest",
  "Recomputed from the record: adoption rises at every step from 22 to 48 to 79 to 94 percent as holdings get larger, while the number of farms falls in the same direction, so the majority of farms sit in the least-adopting band. EK SPS-5.D.2 names negative consequences for human populations, and a technology taken up in proportion to holding size is how a yield gain becomes a widening gap.",
  ),

 ("but not whether capital, irrigation access or something else",
  "EK SPS-5.D.2 names negative consequences for human populations without specifying a mechanism, so the mechanism has to be argued rather than read off a table. Holding size correlates with credit, irrigation and market access at once, which is why a size-banded record narrows the explanation without settling it."),

 ("both benefits and costs to people and to the environment",
  "EK SPS-5.D.1 supplies the three characteristics and EK SPS-5.D.2 supplies the two-sided account across both people and the environment. Every rejected summary drops one of the four cells the second statement asserts to be occupied."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"5.5 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"5.5 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_yields_and_fertilizer,
    27: q27_salinized_share,
    28: q28_adoption_by_size,
}

geo_check.check(g5_5, ANCHORS, TABLE_NOTES)
