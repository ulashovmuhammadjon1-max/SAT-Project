"""Key audit for AP HUMAN GEOGRAPHY 7.1 The Industrial Revolution.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective SPS-7.A and three statements:

    SPS-7.A.1 Industrialization began as a result of new technologies and was
              facilitated by the availability of natural resources.
    SPS-7.A.2 As industrialization spread it caused food supplies to increase and
              populations to grow; it allowed workers to seek new industrial jobs
              in the cities and changed class structures.
    SPS-7.A.3 Investors in industry sought out more raw materials and new markets,
              a factor that contributed to the rise of colonialism and
              imperialism.

SPS-7.A.1 USES TWO DIFFERENT VERBS AND THEY ARE NOT INTERCHANGEABLE. Technology
is what industrialization BEGAN AS A RESULT OF; natural resources FACILITATED it.
Item 1 offers the swap as its first distractor and item 2 asks for the reason
behind the asymmetry: coal and iron lay under the ground throughout human
history, so their availability explains WHERE industry could develop rather than
WHY it developed when it did. Reversing the two verbs is the single most
available error in this topic and both items are built on it.

SPS-7.A.2 IS A FOUR-PART CONSEQUENCE and each part has an item: food supplies
rise (6), populations grow (10), workers take industrial jobs in cities (7, 11)
and class structures change (8, 21). Items 9 and 10 connect the middle two
explicitly to EK SPS-5.C.1's second agricultural revolution and to the second
stage of the demographic transition model, so that a student meeting the same
causal chain for the third time in this course recognizes it as the same chain.

SPS-7.A.3'S HEDGE IS THE MOST IMPORTANT WORDING IN THE TOPIC and three items key
on it. The CED says the search for raw materials and new markets was A FACTOR
THAT CONTRIBUTED TO the rise of colonialism and imperialism -- not the cause, not
the reason. Item 14 makes the exact phrase the key with "the sole cause" as its
first distractor, item 20 asks for the correction directly, and item 29 makes the
same point about evidence: a mirrored trade table records the shape of a
relationship and not how it came about. A key asserting a single cause for
colonialism would assert what the framework specifically declines to.

NO REAL COUNTRY IS NAMED ANYWHERE IN THIS MODULE and no date is attached to any
named place. Which regions industrialized when is real political history the CED
does not set out here, the mechanisms can be taught without it, and a claim about
a named place is one no verifier could check. All three data items use unnamed
economies.

The three table items (26, 27, 28) are the computational gate:

  26  the two output growth FACTORS are computed separately and checked to
      differ, since one distractor asserts they rose by the same proportion
  27  the three sector shares checked to sum to 100 in each year, and industry
      AND services both checked to rise -- one distractor says services fell
  28  all four rows checked to mirror between the two economies, which is what
      the key claims; a table where only one row reversed would not support it

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting. One item was again written with a malformed
token in place of `ans=0` -- the third occurrence this session -- and was caught
by the same import-and-assert check, which now runs at the top of this file.
"""
import re

import geo_check
import g7_1

for _n, _item in enumerate(g7_1.QUESTIONS, 1):
    assert isinstance(_item.get("ans"), int), f"7.1 q{_n}: `ans` is {_item.get('ans')!r}"
    assert 0 <= _item["ans"] < len(_item["choices"]), f"7.1 q{_n}: ans out of range"


def q26_output_and_urbanization(table):
    """Growth factors computed separately; they must NOT be equal."""
    coal = [float(r[1].replace(",", "")) for r in table["rows"]]
    iron = [float(r[2]) for r in table["rows"]]
    urban = [float(r[3]) for r in table["rows"]]
    for series in (coal, iron, urban):
        assert all(b > a for a, b in zip(series, series[1:])), series
    coal_factor = coal[-1] / coal[0]
    iron_factor = iron[-1] / iron[0]
    assert 22 < coal_factor < 23, coal_factor
    assert 44 < iron_factor < 46, iron_factor
    # A distractor asserts the two rose by the same proportion; they must not.
    assert iron_factor > 1.5 * coal_factor, (coal_factor, iron_factor)
    assert urban[0] == 20 and urban[-1] == 68, urban
    return f"urban share rose from {urban[0]:.0f} to {urban[-1]:.0f} percent"


def q27_sector_shift(table):
    """Shares sum to 100 each year; industry AND services both rise."""
    agri = [float(r[1]) for r in table["rows"]]
    industry = [float(r[2]) for r in table["rows"]]
    services = [float(r[3]) for r in table["rows"]]
    for a, i, s in zip(agri, industry, services):
        assert a + i + s == 100, (a, i, s)
    assert all(b < a for a, b in zip(agri, agri[1:])), agri
    assert all(b > a for a, b in zip(industry, industry[1:])), industry
    # One distractor says services fell; they must rise throughout.
    assert all(b > a for a, b in zip(services, services[1:])), services
    assert agri[0] == 62 and agri[-1] == 15, agri
    return f"from {agri[0]:.0f} to {agri[-1]:.0f} percent of employment"


def q28_mirrored_trade(table):
    """Every row must reverse between the two economies, not just one."""
    rows = {r[0]: (float(r[1]), float(r[2])) for r in table["rows"]}
    raw_imp = rows["Raw materials as a share of imports"]
    man_imp = rows["Manufactured goods as a share of imports"]
    raw_exp = rows["Raw materials as a share of exports"]
    man_exp = rows["Manufactured goods as a share of exports"]
    assert raw_imp[0] > raw_imp[1], raw_imp
    assert man_imp[0] < man_imp[1], man_imp
    assert raw_exp[0] < raw_exp[1], raw_exp
    assert man_exp[0] > man_exp[1], man_exp
    assert raw_imp[0] == 71 and man_exp[0] == 83, (raw_imp, man_exp)
    assert raw_exp[1] == 88 and man_imp[1] == 76, (raw_exp, man_imp)
    return "one importing raw materials and exporting manufactures"


CLAIMS = [
 ("began as a result of new technologies and was facilitated by the availability",
  "EK SPS-7.A.1 states that industrialization began as a result of new technologies and was facilitated by the availability of natural resources. The two verbs are not interchangeable, and swapping them reverses which of the two the framework treats as the new thing."),

 ("The resources had always been there",
  "EK SPS-7.A.1 distinguishes what industrialization BEGAN AS A RESULT OF from what FACILITATED it. Coal seams and iron ore lay under the ground throughout human history, so their availability explains where industry could develop rather than why it developed when it did."),

 ("Coal, iron ore, and water power",
  "EK SPS-7.A.1 says industrialization was facilitated by the availability of natural resources. Coal supplied heat and then motive power, iron ore the material for machines and structures, and falling water the earliest mechanical power."),

 ("bulky and heavy relative to its value",
  "EK SPS-7.A.1 says the availability of natural resources facilitated industrialization, and availability at a place is what matters when transport is expensive. A fuel consumed in enormous quantity and cheap per tonne cannot bear a long journey, so the industry went to the fuel."),

 ("The steam engine, mechanized textile production",
  "EK SPS-7.A.1 attributes the beginning of industrialization to new technologies. A power source not tied to a river, a way to spin and weave by machine, and cheaper iron together made large-scale mechanized production possible."),

 ("Food supplies to increase and populations to grow",
  "EK SPS-7.A.2 states that as industrialization spread it caused food supplies to increase and populations to grow. The two are listed together because the first makes the second possible, which is the chain EK SPS-5.C.1 describes from the agricultural side."),

 ("Seek new industrial jobs in the cities",
  "EK SPS-7.A.2 says industrialization ALLOWED workers to seek new industrial jobs in the cities. The verb is permissive: the jobs existed and could be sought, which is a different claim from saying workers were compelled to move."),

 ("an industrial working class paid a wage and a commercial and professional middle class",
  "EK SPS-7.A.2 names changed class structures among industrialization's consequences. Where income had rested largely on land, a factory wage and a return from a business were new positions, and a society containing them is organized differently."),

 ("which is the same chain seen from the agricultural side",
  "EK SPS-7.A.2 says industrialization caused food supplies to increase and populations to grow, and EK SPS-5.C.1 says the second agricultural revolution led to better diets and more people available for factory work. The two describe one process from opposite ends."),

 ("lowered death rates while birth rates stayed high",
  "EK SPS-7.A.2 says industrialization caused food supplies to increase and populations to grow. A population grows rapidly when deaths fall before births do, and that gap is exactly what the second stage of the demographic transition model describes."),

 ("made it possible to feed a population that no longer grew its own food",
  "EK SPS-7.A.2 says industrialization allowed workers to seek new industrial jobs IN THE CITIES and caused food supplies to increase. Both halves are needed: a city is a place where people work without farming, which requires the jobs and the surplus together."),

 ("More raw materials and new markets",
  "EK SPS-7.A.3 states that investors in industry sought out more raw materials and new markets. The pairing matters: a factory needs inputs to consume and buyers for what it makes, and both requirements grow as output grows."),

 ("Domestic sources of raw materials and domestic buyers are finite",
  "EK SPS-7.A.3 says investors sought out MORE raw materials and NEW markets. Both adjectives point at growth: what suffices at one scale of production does not at a larger one, which is what turns an industrial economy outward."),

 ("a factor that contributed to the rise of colonialism and imperialism",
  "EK SPS-7.A.3's wording is precise: the search for raw materials and new markets was A FACTOR THAT CONTRIBUTED TO the rise of colonialism and imperialism. The framework names one contributing factor and does not claim it was the only or the decisive one."),

 ("so the same relationship met both requirements",
  "EK SPS-7.A.3 names both more raw materials and new markets as what investors sought. A trading relationship in which one side sends materials and receives manufactures satisfies both at once, which is why the two appear in a single statement."),

 ("spread of industrial production from the regions where it began",
  "Learning objective SPS-7.A asks how the Industrial Revolution facilitated the growth AND DIFFUSION of industrialization. Diffusion is the spread of a process from a hearth, the same concept EK SPS-5.B.1 applies to plants and animals in Unit 5."),

 ("regions differed in when all four were available",
  "EK SPS-7.A.1 names technology and resources as the conditions for industrialization to begin, and learning objective SPS-7.A asks about its diffusion. A process requiring several conditions at once spreads unevenly, since it can start only where the last of them arrives."),

 ("lowered the cost of moving heavy raw materials in and finished goods out",
  "EK SPS-7.A.1 makes the availability of natural resources a facilitator of industrialization, and availability is partly a question of what can be moved. Cheaper transport widens the area a factory can draw from and sell to, which is what permits scale."),

 ("where investors sought raw materials and markets on other continents",
  "EK SPS-7.A.1 ties the beginning of industry to resources available at particular places while EK SPS-7.A.3 describes investors reaching outward for materials and markets. The same process is a question of site at one scale and of empire at another."),

 ("since the framework says 'a factor that contributed to' rather than naming a cause",
  "EK SPS-7.A.3 says the search for raw materials and new markets was A FACTOR THAT CONTRIBUTED TO the rise of colonialism and imperialism. Reading a contributing factor as the cause states more than the framework does, and the difference is what the CED's phrasing preserves."),

 ("Position stops depending on what a household owns and starts depending on what it earns",
  "EK SPS-7.A.2 names changed class structures among industrialization's consequences. A wage relationship is a different kind of position from a tenancy or a freehold, and a society containing many of both is structured differently from one containing only the latter."),

 ("marks the scale of the transformation",
  "Learning objective SPS-7.A asks how the Industrial Revolution facilitated the growth and diffusion of industrialization, and EK SPS-7.A.2 lists food supply, population, work and class among what it changed. A change reaching all four is revolutionary in extent whatever its pace."),

 ("changed how goods were manufactured and where people worked",
  "EK SPS-5.A.1 places domestication in early hearths and EK SPS-5.C.1 describes the second agricultural revolution, while EK SPS-7.A.1 concerns the beginning of industrial production. The three are linked -- EK SPS-7.A.2 says industrialization increased food supplies -- without being the same event."),

 ("EK PSO-7.A.5 on outsourcing and economic restructuring",
  "EK SPS-7.A.1 to EK SPS-7.A.3 concern how industrialization began and spread, while EK PSO-7.A.5 states that outsourcing and economic restructuring have led to a decline in jobs in core regions. A region losing industry belongs to that later topic rather than counting against this one."),

 ("Investors seeking raw materials and new markets abroad, matched to a factor contributing to colonialism",
  "EK SPS-7.A.1, EK SPS-7.A.2 and EK SPS-7.A.3 cover the beginning, the consequences and the outward reach of industrialization respectively. Only one pairing here places a development under the statement that actually covers it."),

 ("urban share rose from 20 to 68 percent",
  "Recomputed from the record: coal rises from 10 to 225 million tonnes, a factor of 22.5, iron from 0.2 to 9.0, a factor of 45, and the urban share from 20 to 68 percent, each at every step. The verifier asserts the two output factors DIFFER, since one distractor claims they rose by the same proportion.",
  ),

 ("from 62 to 15 percent of employment",
  "Recomputed from the record: the three shares sum to 100 in each year, agriculture falls at every step from 62 to 15 percent, and industry and services both rise, to 49 and 36. EK SPS-7.A.2 says industrialization allowed workers to seek new industrial jobs, and labour leaving farming for both other sectors is what that looks like.",
  ),

 ("one importing raw materials and exporting manufactures",
  "Recomputed from the record: all four rows reverse between the two economies, one taking 71 percent of imports as raw materials and sending 83 percent of exports as manufactures while the other records 8 and 5. EK SPS-7.A.3 says investors sought out more raw materials and new markets, and a relationship supplying both produces exactly this mirrored pattern.",
  ),

 ("the framework itself calls the search for materials and markets only a contributing factor",
  "EK SPS-7.A.3 says the search for raw materials and new markets was A FACTOR THAT CONTRIBUTED TO the rise of colonialism and imperialism. A table records the shape of a relationship at a moment, and the framework's own hedge is a warning against reading a pattern as a complete explanation."),

 ("the search for materials and markets contributed to colonialism and imperialism",
  "EK SPS-7.A.1 supplies the beginning, EK SPS-7.A.2 the consequences and EK SPS-7.A.3 the outward reach that followed. Each rejected version reverses one of the three directions the statements set, and one of them swaps the CED's two verbs in the first statement."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"7.1 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"7.1 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_output_and_urbanization,
    27: q27_sector_shift,
    28: q28_mirrored_trade,
}

geo_check.check(g7_1, ANCHORS, TABLE_NOTES)
