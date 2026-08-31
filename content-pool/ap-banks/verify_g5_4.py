"""Key audit for AP HUMAN GEOGRAPHY 5.4 The Second Agricultural Revolution.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. One learning objective and ONE essential knowledge statement,
and the statement is a causal chain rather than a list:

    SPS-5.C   Explain the advances and impacts of the second agricultural
              revolution.
    SPS-5.C.1 New technology and increased food production in the second
              agricultural revolution led to better diets, longer life
              expectancies, and more people available for work in factories.

Every key in this module traces to that sentence. Because it is the only one, the
module's difficulty is not coverage but reading it correctly, and there are two
ways to read it wrongly.

FIRST, THE THREE CONSEQUENCES ARE LINKED TO EACH OTHER, not merely to the cause.
Better diets are the mechanism by which life expectancy rose; rising output per
farm WORKER is the mechanism by which labour became available. Items 5, 6, 11,
18, 23 and 29 key on the links rather than the endpoints, which is what the
objective's word "impacts" asks for.

SECOND, THE DIRECTION OF THE LAST LINK. The CED says increased food production
LED TO more people being AVAILABLE for factory work. It does not say factories
drew people off the land, and it does not say farming declined. Items 5, 11, 12,
15 and 24 key against the reversed reading; item 15 states in the key itself what
the sentence does not claim, and item 24 disposes of "farming became
unimportant" -- a falling employment share is a measure of productivity, not of
irrelevance, and the same sentence says production INCREASED.

WHAT THE CED DOES NOT NAME: any technology, date, inventor or country. The
technologies this module uses -- the seed drill, four-course rotation replacing
bare fallow, selective breeding of livestock, consolidation of scattered strips
into compact enclosed farms, the mechanical reaper -- are the standard ones for
this revolution, and every item keys on the MECHANISM by which the device raises
output rather than on who introduced it or when. The mechanism is what "new
technology and increased food production" actually asserts; a date or an inventor
would be content the framework does not carry.

NEIGHBOURING TOPICS. Two items exist to separate this revolution from the ones
either side of it: item 16 against the FIRST agricultural revolution, which is
the domestication of EK SPS-5.A.1, and item 17 against the GREEN REVOLUTION,
which EK SPS-5.D.1 characterizes by high-yield seeds, increased chemical use and
mechanized farming in the developing world. Item 1's distractors are drawn from
both of those statements for the same reason.

The three table items (26, 27, 28) are the computational gate:

  26  the percentage rise in yield, plus the assertion that the AREA is
      unchanged -- without that the higher output could have come from new land
      rather than from new technique, which is the whole point of the item
  27  output, farm workers per 1,000 hectares and the agricultural employment
      share, checked to move in the pattern the CED's sentence requires: output
      up while both labour measures fall
  28  three separate indicators, with the child-mortality column checked to more
      than halve, since that is where a twelve-year rise in an average life
      expectancy actually comes from

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written. One distractor was rewritten during the pass: item 26 offered "about 43
percent", which corresponds to nothing a student would compute from the table.
It now reads 57 percent with its reasoning stated, which is the real error --
dividing the increase by the LATER yield instead of the earlier one -- so the
distractor now catches a mistake instead of being noise.
"""
import re

import geo_check
import g5_4


def q26_yield_rise(table):
    """Percentage rise in yield, with the area held constant."""
    rows = {r[0]: r for r in table["rows"]}
    before = float(rows["Before the new methods"][1])
    after = float(rows["After the new methods"][1])
    area_b = float(rows["Before the new methods"][2].replace(",", ""))
    area_a = float(rows["After the new methods"][2].replace(",", ""))
    # Unchanged area is what makes the gain attributable to technique.
    assert area_b == area_a, (area_b, area_a)
    pct = (after - before) / before * 100
    assert 132 < pct < 134, pct
    # The distractor's error -- dividing by the later yield -- must give 57.
    wrong = (after - before) / after * 100
    assert 56 < wrong < 58, wrong
    return f"about {pct:.0f} percent"


def q27_labour_and_output(table):
    """Output up while both measures of agricultural labour fall."""
    rows = {r[0]: r for r in table["rows"]}
    early, late = rows["Earlier"], rows["Later"]
    per_ha_e, per_ha_l = float(early[1]), float(late[1])
    share_e, share_l = float(early[2]), float(late[2])
    out_e = float(early[3].replace(",", ""))
    out_l = float(late[3].replace(",", ""))
    assert out_l > 2 * out_e, (out_e, out_l)
    assert per_ha_l < per_ha_e, (per_ha_e, per_ha_l)
    assert share_l < share_e, (share_e, share_l)
    assert share_e == 61 and share_l == 24, (share_e, share_l)
    return f"fell from {share_e:.0f} to {share_l:.0f} percent"


def q28_diet_and_mortality(table):
    """Calories up, child mortality more than halved, life expectancy up."""
    rows = {r[0]: r for r in table["rows"]}
    early, late = rows["Earlier"], rows["Later"]
    kcal_e = float(early[1].replace(",", ""))
    kcal_l = float(late[1].replace(",", ""))
    le_e, le_l = float(early[2]), float(late[2])
    u5_e, u5_l = float(early[3]), float(late[3])
    gain = kcal_l - kcal_e
    assert gain == 700, gain
    assert u5_l < u5_e / 2, (u5_e, u5_l)      # "more than half"
    assert le_l - le_e == 12, (le_e, le_l)
    return f"{gain:.0f} kilocalories a day"


CLAIMS = [
 ("longer life expectancies",
  "EK SPS-5.C.1 names better diets, longer life expectancies and more people available for work in factories as the three impacts. High-yield seeds, chemicals and mechanization are the Green Revolution's characteristics in EK SPS-5.D.1, and domestication belongs to EK SPS-5.A.1, so both of those sets describe different revolutions."),

 ("New technology and increased food production",
  "EK SPS-5.C.1 identifies new technology and increased food production as the cause of the three impacts it names. The causal order runs from technology through output to the social consequences, and nothing in the sentence runs the other way."),

 ("Far less seed is wasted",
  "EK SPS-5.C.1 attributes the revolution's impacts to new technology raising food production, and this device works by improving the ratio of plants established to seed sown. The gain is in the efficiency of a scarce input rather than in the fertility of the ground itself."),

 ("Land that was formerly left idle now grows a crop",
  "EK SPS-5.C.1 attributes increased food production to new technology, and a rotation is a technology in the sense of a method. Under bare fallow a share of every farm produced nothing each year, so keeping that share in production is a direct addition to output."),

 ("so labour was released rather than pulled away",
  "EK SPS-5.C.1 says increased food production led to more people being AVAILABLE for work in factories, which describes a surplus rather than recruitment. When a smaller share of the workforce can feed everyone, the remainder is free to do something else."),

 ("resists infectious disease better and dies of it less often",
  "EK SPS-5.C.1 lists better diets and longer life expectancies consecutively, and the order reflects the mechanism between them. Nutrition changes how likely an infection is to kill rather than whether it is caught, and the largest effect falls on the youngest."),

 ("Systematic breeding is a method for raising output",
  "EK SPS-5.C.1 attributes the impacts to new technology and increased food production, and a technology is any means of getting more from given inputs. An animal bred to put more of its feed into meat or milk raises output without the farm acquiring another hectare."),

 ("A single block can be worked, drained, fenced and improved as a unit",
  "EK SPS-5.C.1 attributes increased food production to new technology, and reorganizing how land is held is among the period's changes. Drainage and controlled breeding are practicable on a block one household controls and impracticable across strips shared with neighbours."),

 ("since the harvest no longer requires the same labour force",
  "EK SPS-5.C.1 names more people available for work in factories among the impacts, and labour-saving machinery is the most direct route to it. The crop is unchanged; what has changed is the number of hands needed to gather it."),

 ("so they can exist in large numbers only where farms produce a surplus",
  "EK SPS-5.C.1 links increased food production to more people being available for work in factories. A city is a concentration of people who buy their food rather than growing it, which is possible only where a surplus exists and can be moved to them."),

 ("so total agricultural output could rise while the number of farm workers fell",
  "EK SPS-5.C.1 pairs increased food production with more people available for factory work, and both can hold at once only if each remaining worker produces more. Rising output alongside a shrinking agricultural workforce is the signature of the entire period."),

 ("which places the food first",
  "EK SPS-5.C.1's verb points in one direction: food production LED TO more people being available for factory work. The sentence would have to be written the other way round to support the claim that industry came first and agriculture responded."),

 ("death rates fall sharply while birth rates remain high",
  "EK SPS-5.C.1 names longer life expectancies among the impacts, and a rise in life expectancy is a fall in mortality. A falling death rate against a birth rate that has not yet responded is exactly the second stage of the demographic transition model."),

 ("It released labour from the land at the same time",
  "EK SPS-5.C.1 names more people available for work in factories among the impacts, and factories were built where labour, capital and transport met. The same change supplies both halves of a city -- the people who can leave the land and the food that will feed them afterwards."),

 ("it does not assert that agricultural output fell",
  "EK SPS-5.C.1 pairs INCREASED food production with the availability of workers, so both claims are made in one sentence. A reading in which farming failed and drove people away contradicts the first half of the statement it claims to be interpreting."),

 ("raised the output of species already domesticated",
  "EK SPS-5.A.1 places the domestication of plants and animals in early hearths while EK SPS-5.C.1 describes new technology raising food production. Bringing a species under cultivation and getting more from a species already cultivated are different achievements separated by thousands of years."),

 ("a later package of high-yield seeds, chemicals and mechanization",
  "EK SPS-5.D.1 characterizes the Green Revolution by high-yield seeds, increased chemical use and mechanized farming in the developing world, while EK SPS-5.C.1 describes this revolution's technology and its social impacts. They are separate topics with separate essential knowledge statements."),

 ("An average is pulled up sharply",
  "EK SPS-5.C.1 names longer life expectancies among the impacts, and that measure is an average of ages at death across a whole population. A death at one year removes far more years from the average than a death at seventy, so improvements in infant survival dominate the figure."),

 ("so transport turns higher production into a larger food supply",
  "EK SPS-5.C.1 connects increased food production to more people being available for work in factories, and that connection runs through a market. Grain that cannot reach a city does not feed the city, so movement belongs to the same causal chain rather than to a separate story."),

 ("appears at the household scale as more and more varied food",
  "EK SPS-5.C.1 names better diets among the impacts of increased food production, and production is measured for regions while diets are eaten by households. Reading one process at two scales is what turns an aggregate statistic into a statement about people's lives."),

 ("only if it outpaces the number of people it must feed",
  "EK SPS-5.C.1 links increased food production to better diets, and what a person eats depends on output divided by the population sharing it. The chain is stated as a historical outcome rather than as a law, so a case where growth absorbs the gain is a limit on the claim and not a refutation."),

 ("while the share of the workforce in agriculture fell",
  "EK SPS-5.C.1 pairs increased food production with more people available for factory work. Rising yields per hectare and per worker alongside a falling agricultural employment share is exactly that pairing, whereas expanding the farmed area would raise output without indicating any change of technique."),

 ("Better nutrition is the mechanism by which mortality fell",
  "EK SPS-5.C.1 lists better diets and longer life expectancies consecutively as impacts of increased food production, and the order reflects the causal path. A better-fed population survives infection more often, which is what a rising life expectancy records."),

 ("a smaller share of workers was feeding a larger population",
  "EK SPS-5.C.1 attributes INCREASED food production to the period, so output rose rather than fell. A falling share of employment in a sector measures that sector's productivity, and calling the sector unimportant contradicts the sentence's own first clause."),

 ("Terraced hillsides built centuries earlier for hand cultivation",
  "EK SPS-5.C.1 attributes the period's impacts to new technology raising food production, and four of these five features are physical traces of exactly that. Terraces cut long before for hand cultivation record an older adaptation to slope and say nothing about the changes this statement describes."),

 ("about 133 percent",
  "Recomputed from the figures: yield rises from 0.9 to 2.1 tonnes per hectare, an increase of 1.2 on a base of 0.9, which is about 133 percent, and the area under grain is identical in both rows. The unchanged area is what makes the gain attributable to technique rather than to bringing new land into cultivation.",
  ),

 ("fell from 61 to 24 percent",
  "Recomputed from the record: output rises from 360 to 840 thousand tonnes while farm workers per 1,000 hectares fall from 620 to 210 and the agricultural share of employment falls from 61 to 24 percent. EK SPS-5.C.1 pairs increased food production with more people available for factory work, and both halves of that pairing appear here at once.",
  ),

 ("rose by 700 kilocalories a day",
  "Recomputed from the figures: available food energy rises by 700 kilocalories a day, deaths before age five fall from 310 to 140 per thousand, which is more than a halving, and life expectancy rises by 12 years. EK SPS-5.C.1 names better diets and longer life expectancies among the impacts, and the child mortality column shows where the gain in the average came from.",
  ),

 ("the three results are linked to each other and not only to the cause",
  "EK SPS-5.C.1 puts new technology and increased food production at the head of a sentence whose three consequences depend on one another as well as on the cause. Nutrition is the mechanism behind falling mortality, and output per worker is the mechanism behind released labour."),

 ("which improved diets, lengthened life expectancy, and freed labour",
  "EK SPS-5.C.1 states exactly this chain, running from technology through production to three social consequences. The reversed version contradicts the sentence's direction, and the two remaining summaries describe the Green Revolution of EK SPS-5.D.1 and the hearths of EK SPS-5.A.1 instead."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"5.4 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"5.4 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_yield_rise,
    27: q27_labour_and_output,
    28: q28_diet_and_mortality,
}

geo_check.check(g5_4, ANCHORS, TABLE_NOTES)
