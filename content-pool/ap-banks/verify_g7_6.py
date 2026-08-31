"""Key audit for AP HUMAN GEOGRAPHY 7.6 Trade and the World Economy.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective PSO-7.A, suggested skill 5.B, and the
FIRST FOUR of that objective's essential knowledge statements. The CED splits
PSO-7.A across two topics; PSO-7.A.5 to PSO-7.A.7 belong to 7.7 and nothing here
touches them.

    PSO-7.A.1 Complementarity and comparative advantage establish the basis
              for trade.
    PSO-7.A.2 Neoliberal policies, including free trade agreements, have created
              new organizations, spatial connections, and trade relationships,
              such as the EU, World Trade Organization (WTO), Mercosur, and
              OPEC, that foster greater globalization.
    PSO-7.A.3 Government initiatives at all scales may affect economic
              development, including tariffs.
    PSO-7.A.4 Global financial crises (e.g., debt crises), international lending
              agencies (e.g., the International Monetary Fund), and strategies
              of development (e.g., microlending) demonstrate how different
              economies have become more closely connected, even interdependent.

SIX TERMS ARE NAMED BY THE CED AND DEFINED BY NOBODY -- complementarity,
comparative advantage, neoliberal policies, free trade agreements, tariffs, debt
crises. PSO-7.A requires them to be explained, so the module supplies the
discipline's standard sense and its header says so, exactly as g7_2 did for
least cost theory and g7_5 for Rostow's stages. Each such item's `why` is worded
as an explanation of a term the CED names, never as a quotation of a sentence
the CED does not contain.

NOTHING IS ASSERTED ABOUT THE FOUR NAMED ORGANIZATIONS. The CED names the EU,
the World Trade Organization, Mercosur and OPEC and says nothing further about
any of them. Item 9 asks which four are named and item 10 asks what the
framework says they do -- foster greater globalization. No item anywhere states
a membership, a rule, a founding date or a policy, because the CED states none
and this bank has no other source. This is the constraint that most shaped the
module: a whole family of obvious items about what the WTO or OPEC does had to
be left unwritten.

TWO HEDGES ARE KEYED ON DIRECTLY, because losing either turns a defensible CED
sentence into a false one:
    PSO-7.A.3 says initiatives MAY AFFECT development, not that they do -- item
        17, whose distractors are the four ways of over-reading it.
    PSO-7.A.4 says connected, EVEN INTERDEPENDENT -- item 26, which asks what
        the second word adds, since a student who reads them as synonyms has
        lost the statement's escalation.

COMPLEMENTARITY AND COMPARATIVE ADVANTAGE ARE TWO THINGS. One is a fact about
what two places have and want; the other is a fact about relative cost. Items 5
and 6 are a matched pair built so that each case supplies exactly one of the two
conditions and states nothing that would supply the other -- item 5's case names
a surplus and a demand and says nothing about what is forgone, item 6's names
what is forgone and states no surplus. Item 7 asks why the CED names two.

THE MICROLENDING TRAP, AVOIDED DELIBERATELY. g7_4 already carries six items on
microloans under SPS-7.D.3 -- what they are, the chain from loan to living
standard, how far the instrument reaches, and the limits of a programme's own
figures. PSO-7.A.4 names microlending as well, and writing another "what does a
microloan do" item here would have been the tenth cross-topic duplicate of the
kind COMP_GOV_DEDUPE.md records. Item 25 asks instead why the CED puts a
household-scale instrument in the same list as a world-scale crisis, which is a
question about the list and exists only in this topic.

NO REAL COUNTRY IS NAMED ANYWHERE IN THIS MODULE. The three data items carry
hypothetical records attached to two unnamed regions, one unnamed country and
four unnamed economies.

The three table items (27, 28, 29) are the computational gate:

  27  the opportunity costs are DERIVED from the two output columns and appear
      nowhere in the table, so a student has to divide. The record is built so
      that one region out-produces the other in BOTH goods -- checked
      explicitly -- because that is the only arrangement in which comparative
      advantage and absolute advantage give different answers, and a table where
      they agreed would let a student reach the key while believing the wrong
      thing.
  28  three changes recomputed from the two rows, and the total quantity of
      steel available checked to FALL, since a distractor claims domestic output
      made up the whole of the lost imports. Every other distractor is checked
      against directly too: imports down not up, domestic output up not down,
      price up not unchanged.
  29  each economy's loss recomputed as its own exposure times a shock that is
      checked to be identical across all four, which is what makes the key's
      claim about exposure rather than about the size of the shock.

ROUNDING. Every returned string is built from the recomputed values and rounded
to the figure a person would print, with the exact value held by a bound beside
it. verify_g7_4.py had to be repaired for the opposite mistake: it recomputed
3,696 and demanded those digits appear in a choice that correctly said "about
3,700", so it failed a question whose arithmetic was right.

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written. One drafted item was cut: a scenario in which a trade agreement lowered
tariffs on a good and exports of it doubled, which is g5_9 q11 asked again with
a different good. Its slot went to item 13, which asks what a supranational
agreement changes BELOW its own scale -- suggested skill 5.B's question, and one
no other module in this bank asks.
"""
import re

import geo_check
import g7_6

for _n, _item in enumerate(g7_6.QUESTIONS, 1):
    assert isinstance(_item.get("ans"), int), f"7.6 q{_n}: `ans` is {_item.get('ans')!r}"
    assert 0 <= _item["ans"] < len(_item["choices"]), f"7.6 q{_n}: ans out of range"


def _num(cell):
    return float(str(cell).replace(",", ""))


def q27_comparative_advantage(table):
    """Opportunity costs derived; one region must out-produce the other in both."""
    cloth = [_num(r[1]) for r in table["rows"]]
    grain = [_num(r[2]) for r in table["rows"]]
    assert len(table["rows"]) == 2, table["rows"]
    # Absolute advantage in BOTH goods, or the item teaches nothing: comparative
    # advantage only says something absolute advantage does not in this case.
    assert cloth[0] > cloth[1] and grain[0] > grain[1], (cloth, grain)
    # Cost of one unit of grain, measured in cloth forgone.
    grain_cost = [c / g for c, g in zip(cloth, grain)]
    # Cost of one unit of cloth, measured in grain forgone.
    cloth_cost = [g / c for c, g in zip(cloth, grain)]
    assert grain_cost[1] < grain_cost[0], grain_cost
    assert cloth_cost[0] < cloth_cost[1], cloth_cost
    # A distractor says the two costs are the same; another says the more
    # productive region holds the comparative advantage in both.
    assert abs(grain_cost[0] - grain_cost[1]) > 0.1, grain_cost
    lo, hi = round(grain_cost[1], 2), round(grain_cost[0], 2)
    assert abs(grain_cost[1] - lo) < 0.005 and abs(grain_cost[0] - hi) < 0.005
    return (f"gives up {lo} units of cloth for each unit of grain while "
            f"Region 1 gives up {hi}")


def q28_tariff_effect(table):
    """Three changes recomputed; total steel available must fall."""
    tariff = [_num(r[1]) for r in table["rows"]]
    imports = [_num(r[2]) for r in table["rows"]]
    home = [_num(r[3]) for r in table["rows"]]
    price = [_num(r[4]) for r in table["rows"]]
    assert len(table["rows"]) == 2, table["rows"]
    assert tariff[1] > tariff[0], tariff
    # Each distractor asserts one of these the other way round.
    assert imports[1] < imports[0], imports
    assert home[1] > home[0], home
    assert price[1] > price[0], price
    # A distractor claims domestic output replaced the whole of the lost
    # imports, so the total available must be checked to have fallen.
    assert imports[1] + home[1] < imports[0] + home[0], (imports, home)
    imp_fall = (imports[0] - imports[1]) / imports[0] * 100
    home_rise = (home[1] - home[0]) / home[0] * 100
    price_rise = (price[1] - price[0]) / price[0] * 100
    a, b, c = round(imp_fall), round(home_rise), round(price_rise)
    for exact, shown in ((imp_fall, a), (home_rise, b), (price_rise, c)):
        assert abs(exact - shown) <= 0.5, (exact, shown)
    assert c == 17, price_rise  # stated in the keyed choice's third clause
    return (f"Imports fell by about {a} percent while steel made inside the "
            f"country rose by about {b} percent")


def q29_exposure_to_one_partner(table):
    """Loss recomputed as exposure times a shock identical across all four."""
    share = [_num(r[1]) for r in table["rows"]]
    shock = [_num(r[2]) for r in table["rows"]]
    loss = [_num(r[3]) for r in table["rows"]]
    # The key's claim is about exposure, so the shock must be the same for all.
    assert len(set(shock)) == 1, shock
    assert len(set(share)) == len(share), share
    for s, k, l in zip(share, shock, loss):
        assert abs(l - s * k / 100) <= 0.5, (s, k, l)
    # Distractors: identical losses, the smallest share taking the largest hit,
    # equal shares, and no loss at all.
    assert len(set(loss)) > 1, loss
    assert share.index(min(share)) != loss.index(max(loss)), (share, loss)
    assert min(loss) > 0, loss
    hi, lo = round(max(loss)), round(min(loss))
    assert abs(max(loss) - hi) <= 0.5 and abs(min(loss) - lo) <= 0.5, loss
    return f"runs from about {hi} percent down to about {lo} percent"


CLAIMS = [
 ("Complementarity and comparative advantage",
  "EK PSO-7.A.1 states that complementarity and comparative advantage establish the basis for trade. Two conditions are named rather than one, and each answers a different question about why a flow between two places exists at all."),

 ("One place holds a surplus of something the other place demands",
  "EK PSO-7.A.1 names complementarity as one of the two bases for trade and the CED does not define it. It matches a surplus on one side to a demand on the other, which is a fact about what each place has and wants rather than about how cheaply either can produce."),

 ("gives up less of its other output to produce a given good than its partner does",
  "EK PSO-7.A.1 names comparative advantage as the second basis for trade and the CED does not define it. The comparison is between what a place forgoes to make one thing rather than another, which makes it a statement about relative cost rather than about total output."),

 ("each can specialize where its own sacrifice is smaller",
  "EK PSO-7.A.1 names comparative advantage rather than absolute output as a basis for trade. Producing one thing means not producing another with the same workers and land, and that forgone alternative can be smaller in the less productive place, which is the case the concept exists to handle."),

 ("Complementarity, since a surplus in one place meets a demand in the other",
  "EK PSO-7.A.1 names complementarity and comparative advantage as two separate bases. The case states what each region has and needs and says nothing about what either gives up to produce timber, so it supplies the first condition and not the second."),

 ("Comparative advantage, since the amount of other output forgone differs between them",
  "EK PSO-7.A.1 names both bases and this case is stated entirely in terms of what is forgone. No surplus or unmet demand appears in it anywhere, so the condition supplied is the one about relative cost rather than the one about matching a surplus to a want."),

 ("one about what each place has and wants and one about what each place gives up to produce it",
  "EK PSO-7.A.1 puts complementarity and comparative advantage in one sentence as joint conditions. Two places can hold matching surpluses and wants while neither has a cost advantage, and two places can differ in relative cost while neither produces a surplus of anything the other lacks."),

 ("reduce government restriction on markets and on trade across borders",
  "EK PSO-7.A.2 names neoliberal policies, INCLUDING FREE TRADE AGREEMENTS, as what created the organizations and relationships it lists, and the CED does not define the term. A free trade agreement is one instance of the wider policy of lowering the barriers a state maintains, which is what makes the CED's word 'including' accurate."),

 ("The EU, the World Trade Organization, Mercosur, and OPEC",
  "EK PSO-7.A.2 names exactly these four as examples of the new organizations, spatial connections and trade relationships neoliberal policies created. The rejected lists are real, but they are bodies with other purposes, categories of employment, instruments of trade policy, and positions in the world economy."),

 ("foster greater globalization",
  "EK PSO-7.A.2 says these organizations, connections and relationships FOSTER GREATER GLOBALIZATION. The verb credits them with encouraging a process already under way, which is a weaker and more defensible claim than that they equalize development or supersede governments."),

 ("lower or remove the barriers each applies to the others' goods",
  "EK PSO-7.A.2 names free trade agreements as an instance of neoliberal policies and the CED does not define them. Reciprocal reduction of barriers is the defining feature, and it is what makes such an agreement a neoliberal instrument rather than any commercial treaty."),

 ("a spatial connection is a route or flow that now exists between places",
  "EK PSO-7.A.2 lists organizations, spatial connections and trade relationships as three separate products of the same policies. Only the first has members, the second is a fact about geography since a flow runs between places, and the third can persist with no treaty behind it."),

 ("which places specialize in which goods can shift within every member as well as between them",
  "Suggested skill 5.B asks students to explain spatial relationships across various geographic scales. EK PSO-7.A.2 says such agreements create new spatial connections, and a connection made at the supranational scale reaches the local one by changing which producers a local firm competes against."),

 ("makes distant suppliers and customers viable where they were not",
  "EK PSO-7.A.2 says neoliberal policies including free trade agreements foster greater globalization. A barrier at a border is a cost falling on distance-crossing exchange specifically, so lifting it changes which of those exchanges are worth making without changing any physical distance."),

 ("A tax a government levies on goods imported into its territory",
  "EK PSO-7.A.3 names tariffs as an example of a government initiative that may affect economic development, and the CED does not define the term. A tariff is a tax on imports specifically, which separates it from a subsidy paid to producers and from a quota, which limits quantity rather than adding cost."),

 ("At all scales",
  "EK PSO-7.A.3 states that government initiatives AT ALL SCALES may affect economic development, including tariffs. That phrase is why suggested skill 5.B, on explaining spatial relationships across various geographic scales, is the skill the CED attaches to this topic."),

 ("capable of affecting development without claiming that every initiative does",
  "EK PSO-7.A.3 says government initiatives at all scales MAY affect economic development. A modal claim asserts possibility rather than regularity, which is the honest form for a statement covering everything from a municipal incentive to a national tariff."),

 ("A municipal authority servicing land for an industrial park",
  "EK PSO-7.A.3 says government initiatives at ALL SCALES may affect economic development, and suggested skill 5.B asks for spatial relationships explained across scales. Only one of these sets varies the scale at which the decision is taken rather than the number of decisions of one kind."),

 ("Buyers of steel pay more, whether they import it or buy it at home",
  "EK PSO-7.A.3 names tariffs among the government initiatives that may affect economic development. A tax on the imported version raises what buyers pay for the import and lets the domestic version sell at a higher price than before, so the effect falls inside the country as well as outside it."),

 ("an initiative taken at one scale produces effects at the others",
  "EK PSO-7.A.3 says government initiatives at all scales may affect economic development, and suggested skill 5.B asks students to explain spatial relationships across various geographic scales. A national tariff changes what a local factory pays for its materials, so the decision and its consequences sit at different levels."),

 ("Global financial crises, international lending agencies, and strategies of development",
  "EK PSO-7.A.4 names those three and offers debt crises, the International Monetary Fund and microlending as its examples of each. The rejected lists are drawn from other statements of this same unit, which is what makes them plausible."),

 ("a borrower cannot meet obligations it has already incurred",
  "EK PSO-7.A.4 offers debt crises as its example of a global financial crisis and does not define them. The reason such a crisis can be called GLOBAL is that a debt is a relationship: a borrower who cannot pay is also a lender's unpaid asset, which is how the difficulty travels."),

 ("often attaches conditions to what it lends",
  "EK PSO-7.A.4 names international lending agencies and gives the International Monetary Fund as its example. The statement's point is what such a body demonstrates rather than what it decides, and lending across borders is itself one of the connections the statement is about."),

 ("a loss in one place is a loss to holders and suppliers in many others",
  "EK PSO-7.A.4 says global financial crises demonstrate how different economies have become more closely connected, even interdependent. The connection is the mechanism as well as the lesson: an unpaid debt or a cancelled order is somebody else's missing income, and the chain does not stop at a border."),

 ("putting a household-scale instrument beside a world-scale crisis",
  "EK PSO-7.A.4 puts all three cases in one sentence and says they DEMONSTRATE how closely connected economies have become. The list is deliberately mixed in scale, which is the same point suggested skill 5.B makes about spatial relationships across various geographic scales."),

 ("each now relies on the others in a way it cannot easily undo",
  "EK PSO-7.A.4 says the three cases demonstrate that economies have become more closely connected, EVEN INTERDEPENDENT. The escalation is the point: influence running between two economies is a weaker claim than reliance running both ways, and only the second makes withdrawal costly."),

 ("gives up 0.75 units of cloth for each unit of grain while Region 1 gives up 1.33",
  "Recomputed from the record: Region 1 out-produces Region 2 in both goods, yet a unit of grain costs Region 1 eight sixths of a unit of cloth and costs Region 2 three quarters of one. EK PSO-7.A.1 names comparative advantage rather than absolute output as a basis for trade, and this is the arrangement in which the two answers differ.",
  ),

 ("Imports fell by about 44 percent while steel made inside the country rose by about 27 percent",
  "Recomputed from the record: imports fall from 900 to 500 thousand tonnes, domestic output rises from 600 to 760, and the average price rises from 480 to 560 currency units, so the quantity replaced at home is smaller than the quantity of imports lost. EK PSO-7.A.3 says government initiatives at all scales MAY affect economic development, and a record showing a gain and a cost together is what that hedge looks like.",
  ),

 ("runs from about 12 percent down to about 2 percent",
  "Recomputed from the record: the partner's imports fall by 20 percent in every case, and each economy's loss is that same fall applied to its own exposure, giving about 12, 7, 3 and 2 percent. EK PSO-7.A.4 says economies have become more closely connected, EVEN INTERDEPENDENT, and exposure rather than the size of the shock decides how far the connection carries.",
  ),

 ("government initiatives at every scale may affect development",
  "EK PSO-7.A.1 supplies the basis for trade, EK PSO-7.A.2 the organizations and what they foster, EK PSO-7.A.3 the government initiatives with their hedge, and EK PSO-7.A.4 the interdependence. Each rejected summary either drops one of the four statements or strengthens a hedged claim into one the framework does not make."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"7.6 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"7.6 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

# The exporter does not typeset this subject, so hand-written LaTeX would ship
# as literal backslashes, and a range written with a hyphen between two digits
# reads as a minus sign to any converter ever pointed at the bank. Explicit
# lookarounds, never \b -- a digit and a letter are both word characters.
DIGIT_RANGE = re.compile(r"[0-9]\s*[-/]\s*[0-9]")
for n, item in enumerate(g7_6.QUESTIONS, 1):
    strings = [item["q"], item["why"], *item["choices"]]
    tbl = item.get("table")
    if tbl:
        strings += list(tbl["headers"]) + [c for row in tbl["rows"] for c in row]
    for s in strings:
        assert "\\(" not in s and "\\[" not in s and "$" not in s, (
            f"7.6 q{n}: math delimiter in a prose subject: {s!r}")
        m = DIGIT_RANGE.search(s)
        assert not m, f"7.6 q{n}: digit range {m.group(0)!r} in {s!r}"

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    27: q27_comparative_advantage,
    28: q28_tariff_effect,
    29: q29_exposure_to_one_partner,
}

geo_check.check(g7_6, ANCHORS, TABLE_NOTES)
