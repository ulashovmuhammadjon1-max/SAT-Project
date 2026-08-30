"""Key audit for AP HUMAN GEOGRAPHY 1.5 Human-Environmental Interaction.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. PSO-1.B prints exactly two essential-knowledge statements:

    PSO-1.B.1  Concepts of nature and society include sustainability, natural
               resources, and land use.
    PSO-1.B.2  Theories regarding the interaction of the natural environment
               with human societies have evolved from environmental determinism
               to possibilism.

PSO-1.B.2 is the sentence that carries content rather than just a list, and the
content is a DIRECTION: determinism first, possibilism after. Items 1, 2, 4, 9,
13, 15, 19, 23 and 25 are keyed to that pair and cite it. PSO-1.B.1 is three
names with no definitions attached, so items 5, 6, 7, 8, 12, 14, 16, 17, 21 and
22 cite it only where the key is list membership, and the rest -- what a
sustainable yield is, why a substance becomes a resource, what a trade-off
requires -- cite nothing at all, because the CED does not define those terms and
a manufactured code would be worse than an honest uncited claim.

The definitions the module holds itself to, stated once so a reader can audit
every key against them:
  environmental determinism  the physical environment CAUSES cultural and
                             economic outcomes
  possibilism                the physical environment LIMITS the options; the
                             society chooses among what remains
  renewable / nonrenewable   a property of the resource: is the stock replaced
                             as fast as it is drawn?
  sustainable / unsustainable  a property of the USE: does this rate of use
                             outrun replacement? A renewable resource can be
                             used unsustainably, which items 6 and 27 turn on.

The five table items (26-30) are the computational gate. Each function
recomputes the renewable share, the proportional overharvest, the food-land
loss, the recharge balance and the rainfall-versus-income ranges from the
printed cells, and each also asserts that the trap is genuinely present: that
the largest tonnage overshoot is NOT the largest proportional one, that the
basin with the biggest recharge and the basin with the smallest deficit are
both still in deficit, that the wettest country is not the richest.

REVIEW NOTE, written while building the tables. Item 29's first draft gave the
smallest absolute deficit and the smallest withdrawal to two different
distractors, one of which was the keyed basin itself -- a distractor that was
accidentally true. The withdrawal figures were changed so that every distractor
names a real but irrelevant maximum. Nothing else needed correction; all 30 keys
were derived from the questions before this file was written.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g1_5

RENEWABLE = {"Hydroelectric", "Wind", "Solar"}


def q26_renewable_share(table):
    """Share of electricity from continuously replenished flows."""
    shares = {rowdict(table, r)["Source"]:
              num(rowdict(table, r)["Share of electricity (%)"])
              for r in table["rows"]}
    assert abs(sum(shares.values()) - 100) < 1e-9, f"shares do not sum to 100: {shares}"
    renew = sum(v for k, v in shares.items() if k in RENEWABLE)
    fossil = sum(v for k, v in shares.items() if k not in RENEWABLE)
    assert renew == 40 and fossil == 60, (renew, fossil)
    # The distractor pairs must be distinguishable from the answer.
    assert shares["Hydroelectric"] == 19, shares
    assert shares["Wind"] + shares["Solar"] == 21, shares
    return "40 percent"


def q27_overharvest(table):
    """Overharvest as a SHARE of regeneration, which reorders the fisheries."""
    excess_abs, excess_rel = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        regen = num(d["Annual regeneration (tonnes)"])
        catch = num(d["Annual catch (tonnes)"])
        excess_abs[d["Fishery"]] = catch - regen
        excess_rel[d["Fishery"]] = (catch - regen) / regen
    worst_rel = max(excess_rel, key=excess_rel.get)
    worst_abs = max(excess_abs, key=excess_abs.get)
    assert worst_rel == "Fishery B", f"worst proportional overshoot: {excess_rel}"
    assert abs(excess_rel["Fishery B"] - 0.5) < 1e-9, excess_rel
    # The whole point of the item is that these two rankings disagree.
    assert worst_abs != worst_rel, (excess_abs, excess_rel)
    assert excess_abs["Fishery D"] == 0, excess_abs
    assert excess_abs["Fishery A"] < 0, excess_abs
    return "Fishery B"


def q28_food_land(table):
    """Cropland plus pasture, then and now, against the rise in built-up land."""
    by_use = {rowdict(table, r)["Land use"]: rowdict(table, r) for r in table["rows"]}
    food_90 = sum(num(by_use[u]["1990 (hectares)"]) for u in ("Cropland", "Pasture"))
    food_20 = sum(num(by_use[u]["2020 (hectares)"]) for u in ("Cropland", "Pasture"))
    built_90 = num(by_use["Built-up"]["1990 (hectares)"])
    built_20 = num(by_use["Built-up"]["2020 (hectares)"])
    total_90 = sum(num(rowdict(table, r)["1990 (hectares)"]) for r in table["rows"])
    total_20 = sum(num(rowdict(table, r)["2020 (hectares)"]) for r in table["rows"])
    assert food_90 == 36000 and food_20 == 28000, (food_90, food_20)
    assert total_90 == total_20 == 50000, (total_90, total_20)
    growth = built_20 / built_90
    assert 2.5 <= growth < 3.0, f"built-up growth is {growth}x, not nearly triple"
    return "28,000 hectares in 2020"


def q29_recharge(table):
    """The only basin drawing less than its recharge, plus the three false maxima."""
    recharge, withdrawal, deficit = {}, {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        r = num(d["Annual recharge (million m3)"])
        w = num(d["Annual withdrawal (million m3)"])
        recharge[d["Basin"]] = r
        withdrawal[d["Basin"]] = w
        deficit[d["Basin"]] = w - r
    ok = [b for b in deficit if deficit[b] < 0]
    assert ok == ["Basin 2"], f"basins within recharge: {ok}"
    # Each distractor names a real maximum or minimum belonging to a basin in
    # deficit. If any of them coincided with the answer the item would be broken.
    biggest_recharge = max(recharge, key=recharge.get)
    smallest_recharge = min(recharge, key=recharge.get)
    in_deficit = {b: d for b, d in deficit.items() if d > 0}
    smallest_deficit = min(in_deficit, key=in_deficit.get)
    assert biggest_recharge == "Basin 3" and biggest_recharge not in ok, recharge
    assert smallest_recharge == "Basin 4" and smallest_recharge not in ok, recharge
    assert smallest_deficit == "Basin 1", in_deficit
    return "Basin 2"


def q30_determinism_evidence(table):
    """Rainfall barely varies; income varies by more than eighteenfold."""
    rain, gdp, agri = {}, {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        rain[d["Country"]] = num(d["Mean annual rainfall (mm)"])
        gdp[d["Country"]] = num(d["GDP per capita (US$)"])
        agri[d["Country"]] = num(d["Share of workforce in agriculture (%)"])
    rain_spread = (max(rain.values()) - min(rain.values())) / min(rain.values())
    gdp_ratio = max(gdp.values()) / min(gdp.values())
    assert rain_spread < 0.10, f"rainfall varies by {rain_spread:.3f}"
    assert gdp_ratio > 18, f"income ratio is only {gdp_ratio:.1f}"
    # The distractor claiming wetter means richer must be false.
    assert max(rain, key=rain.get) != max(gdp, key=gdp.get), (rain, gdp)
    # And rainfall must not order the agricultural workforce share either.
    by_rain = [c for c in sorted(rain, key=rain.get)]
    by_agri = [c for c in sorted(agri, key=agri.get)]
    assert by_rain != by_agri, (by_rain, by_agri)
    return "more than eighteen"


CLAIMS = [
 ("physical environment is treated as the cause",
  "EK PSO-1.B.2 names environmental determinism as the earlier of the two theories, and its signature move is making physical conditions explain human character and achievement. That its conclusions ranked peoples by climate is the reason the theory was discarded rather than refined."),

 ("sets limits within which a society chooses",
  "EK PSO-1.B.2 describes the evolution from determinism to possibilism, and the possibilist reading is that physical conditions bound the menu without picking the dish. Crediting dikes, pumps and polders as a chosen response is exactly what a determinist account denies."),

 ("very different societies developing in similar environments",
  "Determinism fails empirically because similar climates host radically different cultures and economies, so the environment cannot be doing the causal work claimed for it. It also failed morally, since its explanations were turned into justifications for hierarchy among peoples."),

 ("narrows the options while the society selects",
  "Possibilism is not the claim that environment is irrelevant but the claim that it constrains rather than determines. Naming several viable land uses for one valley and leaving the choice to the community is precisely that structure, which EK PSO-1.B.2 identifies as the later theory."),

 ("forms over geological time",
  "EK PSO-1.B.1 names natural resources without defining the categories, and the operative distinction is the rate of replacement against the rate of use. A stock laid down over millions of years is nonrenewable on any human timescale, whatever the size of the remaining reserve."),

 ("harvested beyond its sustainable yield",
  "Renewability is a property of the resource while sustainability is a property of the use made of it, so a renewable stock can be destroyed by a harvest that outruns its regeneration. Twenty thousand tonnes replaced against thirty-four thousand removed is a deficit repeated every year."),

 ("without compromising the ability of future generations",
  "EK PSO-1.B.1 lists sustainability among the concepts of nature and society, and the standard formulation of it is intergenerational. Use is sustainable if it can continue without foreclosing the options of those who come after, which is neither untouched preservation nor short-run maximization."),

 ("Land use, one of the concepts of nature and society",
  "EK PSO-1.B.1 names land use alongside sustainability and natural resources. A classification recording how each parcel of the surface is occupied and worked is exactly what the term denotes, and several of the listed categories exist only because of human activity."),

 ("physical environment determines a society's economic development",
  "A comparison holding environment constant while outcomes differ is the evidence determinism cannot absorb, since a constant cannot explain a variable. It leaves the possibilist claim untouched, because limits are entirely compatible with different choices being made inside them."),

 ("water table falls year after year",
  "A withdrawal exceeding recharge is a stock being drawn down, and the physical consequences follow from the falling water table rather than from the label attached to the resource. Recharge is fixed by rainfall and geology and does not rise to meet demand."),

 ("Terracing steep hillsides",
  "Terracing is the possibilist case at its clearest: the slope forecloses flat-field cultivation and the society answers with an engineered alternative rather than either abandoning the site or being defeated by the constraint. Abandonment and inundation are the determinist endings the item contrasts it with."),

 ("a policy changed what the land is used for",
  "EK PSO-1.B.1 names both land use and sustainability, and this case joins them: the cropping pattern is a land-use decision and its water demand exceeds what the river can supply indefinitely. That a subsidy caused it does not put it outside the framework's concepts."),

 ("costly or impossible, and the societies there developed",
  "Possibilism keeps the environmental constraint while denying environmental causation, so a correct statement names what is foreclosed and credits the society with the response. Absolute impossibility and no influence at all are the two errors the theory sits between."),

 ("partly recoverable through recycling",
  "An ore body does not regenerate on a human timescale, so extraction is drawdown, while recycling returns already-extracted metal to use and slows how fast the remaining ore must be mined. Collection and reprocessing are never perfectly efficient, so the stock is extended rather than made renewable."),

 ("same environmental condition did not produce the same outcome",
  "When a condition is offered as the cause of an outcome, cases carrying the condition without the outcome are decisive counterexamples. That is the standard empirical case against determinism and the reason EK PSO-1.B.2 records possibilism as its successor."),

 ("recharge is negligible on a human timescale",
  "The renewable classification turns on whether a stock is replaced as fast as it is used. A fossil aquifer receiving almost no recharge is drawn down exactly like an ore body, while discovery, replanting a different forest, the day-night cycle and moving soil change none of the relevant rates."),

 ("removes food-producing land from the urban fringe",
  "EK PSO-1.B.1 names land use, and conversion is one category becoming another. Low-density housing is among the least reversible conversions, since the buildings, the services beneath them and the property boundaries all outlast any later decision to change course."),

 ("occupies grazing land and requires mined materials",
  "A trade-off requires a cost to be incurred somewhere while the benefit is obtained, and the emissions benefit here is bought with land taken from grazing and with extraction elsewhere. The other options improve one thing with no stated cost, which is why none of them is a trade-off."),

 ("grants environmental influence while reserving the decision",
  "The sentence is built to separate two verbs: shaping is constraint and dictating is causation, and possibilism accepts the first while rejecting the second. That is exactly the distinction EK PSO-1.B.2's shift from determinism is about."),

 ("one country with abundant oil is wealthy and another with equal reserves",
  "Four of the questions listed have physical answers determined by physical facts, whereas the distribution of wealth from an identical endowment depends on institutions, ownership and history. Treating that last one as environmentally caused is the determinist error the course asks students to spot."),

 ("land-use rule adopted to make settlement of the coast more sustainable",
  "EK PSO-1.B.1 names land use and sustainability, and a construction setback is a land-use instrument aimed at making occupation of a hazardous zone endurable over time. Choosing such a rule in response to a hazard is a possibilist response rather than a rejection of possibilism."),

 ("uranium was not a resource before the twentieth century",
  "What lies in the ground does not change when a use for it is discovered; what changes is whether it counts as a resource at all. That dependence on available technology and on demand is what makes the category social as well as physical."),

 ("treated with the suspicion the course attaches",
  "Attributing a collective personality to a landform is the determinist move in its most recognizable form, and EK PSO-1.B.2's account of the evolution away from it is why the course expects the argument to be named rather than accepted."),

 ("soil that took centuries to form",
  "A sustainability question asks what a decision forecloses for the future, and soil formed over centuries plus permanently altered runoff are effects that outlast any tenancy. Rent, first-year employment, motorway access and owner preference are all present-period accounting."),

 ("sets real limits and that societies choose",
  "EK PSO-1.B.2 presents possibilism as the successor to determinism, not as a denial that the environment matters. Collapsing it into technological optimism removes the constraint the theory is built around and leaves nothing that could be false."),

 ("40 percent",
  "Recomputed from the table: hydroelectric, wind and solar draw on continuously replenished flows and total 19 plus 12 plus 9, while coal and gas are stocks formed over geological time and total 60. The verifier confirms the shares sum to 100 and that the distractor pairings are genuinely different numbers.",
  q26_renewable_share),

 ("Fishery B",
  "Recomputed from the table: overshoot measured against what each stock can replace is minus 8, plus 50, plus 15 and zero percent, so the fishery losing the most tonnes and the fishery losing the largest share of its stock are different fisheries. A small stock is destroyed by a smaller absolute overshoot.",
  q27_overharvest),

 ("down from 36,000 in 1990",
  "Recomputed from the table: cropland plus pasture falls from 36,000 to 28,000 hectares while built-up land rises from 5,000 to 14,000, and the district's total is a constant 50,000. The built-up gain therefore comes almost entirely out of land that had been producing food.",
  q28_food_land),

 ("the only basin whose withdrawal is below its recharge",
  "Recomputed from the table: exactly one basin draws less than it receives, and that comparison is the whole test of whether a stock is being depleted. The verifier confirms separately that the largest recharge, the smallest recharge and the smallest deficit all belong to basins that are in deficit.",
  q29_recharge),

 ("more than eighteen",
  "Recomputed from the table: rainfall spans 1,750 to 1,900 millimetres, a spread under nine percent, while income runs from 1,200 to 22,100 dollars, a ratio above eighteen. A near-constant environmental variable cannot explain an outcome that varies that widely, and the wettest country is not the richest one.",
  q30_determinism_evidence),
]

hg_check.check(g1_5, CLAIMS, per_topic=30, n_choices=5)
