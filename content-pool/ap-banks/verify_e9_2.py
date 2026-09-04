"""Key audit for AP ENVIRONMENTAL SCIENCE 9.2 Reducing Ozone Depletion.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
STB-4.B.1 is this topic's whole content, in three parts: the strategy is
REPLACEMENT of ozone-depleting chemicals with substitutes that do not deplete
the layer; HFCs are one such replacement; SOME of them are strong greenhouse
gases. Items key those and reason from them:

  the replacement strategy  -- items 1, 5, 7, 8, 16, 19, 21, 25, 29;
  HFCs as the named substitute -- items 2, 10, 23;
  some are strong greenhouse gases -- items 3, 4, 9, 11, 12, 15, 18, 24, 26,
      27, 28;
  read from the item's own table -- items 3, 6, 10, 14, 18, 22.

Neighbouring statements are cited only where an item needs them, and each such
claim below says so: STB-4.A.2 (CFCs cause the depletion) in items 5, 6, 7, 19,
23; STB-4.A.3 (less stratospheric ozone means more UV, then skin cancer and
cataracts) in items 17, 20, 22; STB-4.C.1 (CFCs are among the principal
greenhouse gases) in items 13, 23, 26; STB-4.D.1 (carbon dioxide is the
reference with a potential of 1) in item 14.

NOT KEYED: no treaty, no date, no named commercial refrigerant, and above all
no claim that EVERY hydrofluorocarbon is a strong greenhouse gas -- the
framework says some are, and item 25 exists to refuse the stronger reading.

DATA ITEMS: 3, 6, 10, 14, 18 and 22 carry tables and every keyed reading is
recomputed here from the table alone; item 14 is arithmetic and its product is
recomputed rather than asserted.

NEGATIVE CONTROL: `python3 verify_e9_2.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e9_2

GWP_SUB = "Warming potential compared with the same mass of carbon dioxide"
PROD = "Production of ozone depleting chemicals (thousands of tons per year)"
OZONE_P = "Springtime ozone column over the pole (Dobson units)"
CFC_USE = "Use of chlorofluorocarbons (thousands of tons)"
HFC_USE = "Use of hydrofluorocarbons (thousands of tons)"
MASS = "Mass that would be released (tons)"
ODP = "Ozone depleting potential"
OZONE_R = "Springtime ozone column (Dobson units)"
UVI = "Ultraviolet index measured at the surface"


def q3(table, item):
    names = cg.labels(table)
    depletes = [str(r[1]).strip().lower() for r in table["rows"]]
    gwp = cg.col(table, GWP_SUB)
    yes = [i for i, d in enumerate(depletes) if d == "yes"]
    no = [i for i, d in enumerate(depletes) if d == "no"]
    assert len(yes) == 1 and len(no) == 3, \
        f"the table is not one depleting compound against three substitutes: {depletes}"
    assert "chlorofluorocarbon" in names[yes[0]].lower(), \
        f"the depleting row is not the chlorofluorocarbon: {names[yes[0]]}"
    big = [i for i in no if gwp[i] > 1000]
    assert big, f"no substitute carries a large warming potential: {gwp}"
    assert any(gwp[i] < 10 for i in no), \
        "'the substitutes all sit close to carbon dioxide' must be judged against a low one too"
    assert all(g > 0 for g in gwp), "'none carries any warming potential' must be false"
    return (f"only {names[yes[0]]} depletes the layer, yet the substitute "
            f"{names[big[0]]} still carries a warming potential of {gwp[big[0]]:.0f}")


def q6(table, item):
    periods = cg.labels(table)
    prod = cg.col(table, PROD)
    ozone = cg.col(table, OZONE_P)
    assert all(prod[i] > prod[i + 1] for i in range(len(prod) - 1)), \
        f"production does not fall across the periods in row order: {prod}"
    assert all(ozone[i] < ozone[i + 1] for i in range(len(ozone) - 1)), \
        f"the ozone column does not rise across the periods: {ozone}"
    assert ozone[prod.index(max(prod))] == min(ozone), \
        "'the largest production had the largest ozone column' must be false"
    return (f"from {periods[0]} to {periods[-1]} production runs {prod} while the "
            f"springtime ozone column runs {ozone}, falling and rising respectively")


def q10(table, item):
    decades = cg.labels(table)
    cfc = cg.col(table, CFC_USE)
    hfc = cg.col(table, HFC_USE)
    assert all(cfc[i] > cfc[i + 1] for i in range(len(cfc) - 1)), \
        f"chlorofluorocarbon use does not fall across the decades: {cfc}"
    assert all(hfc[i] < hfc[i + 1] for i in range(len(hfc) - 1)), \
        f"hydrofluorocarbon use does not rise across the decades: {hfc}"
    return (f"from {decades[0]} to {decades[-1]} chlorofluorocarbon use runs {cfc} while "
            f"hydrofluorocarbon use runs {hfc}, in opposite directions")


def q14(table, item):
    options = cg.labels(table)
    mass = cg.col(table, MASS)
    gwp = cg.col(table, GWP_SUB)
    equiv = [m * g for m, g in zip(mass, gwp)]
    top = equiv.index(max(equiv))
    assert options[top].strip().lower() == "option 1", \
        f"the largest carbon dioxide equivalent belongs to {options[top]}, not the first row"
    assert abs(equiv[top] - 14000) < 1e-6, \
        f"the largest equivalent is {equiv[top]:.0f} tons, not fourteen thousand"
    assert len(set(equiv)) == len(equiv), "two options give the same equivalent"
    return (f"{options[top]} at {mass[top]:.0f} tons times a potential of {gwp[top]:.0f} "
            f"is {equiv[top]:.0f} tons of carbon dioxide equivalent, the largest of "
            f"{[round(e) for e in equiv]}")


def q18(table, item):
    names = cg.labels(table)
    odp = cg.col(table, ODP)
    gwp = cg.col(table, GWP_SUB)
    safe_ozone = [i for i, v in enumerate(odp) if v == 0]
    assert 0 < len(safe_ozone) < len(names), \
        f"the candidates are not split between depleting and non-depleting: {odp}"
    both = [i for i in safe_ozone if gwp[i] < 100]
    assert len(both) == 1, \
        f"{len(both)} candidates pass both tests, so 'only one' would be wrong: {list(zip(odp, gwp))}"
    assert any(gwp[i] >= 100 for i in safe_ozone), \
        "'every non-depleting candidate has a small warming potential' must be false"
    worst_gwp = gwp.index(max(gwp))
    assert odp[worst_gwp] == 0, \
        "'the largest warming potential also depletes the most ozone' must be false"
    return (f"{names[both[0]]} is the only candidate with an ozone depleting potential of "
            f"zero and a warming potential below one hundred, given {list(zip(odp, gwp))}")


def q22(table, item):
    periods = cg.labels(table)
    ozone = cg.col(table, OZONE_R)
    uvi = cg.col(table, UVI)
    assert all(ozone[i] < ozone[i + 1] for i in range(len(ozone) - 1)), \
        f"the ozone column does not rise across the periods: {ozone}"
    assert all(uvi[i] > uvi[i + 1] for i in range(len(uvi) - 1)), \
        f"the ultraviolet index does not fall across the periods: {uvi}"
    return (f"from {periods[0]} to {periods[-1]} the ozone column runs {ozone} while the "
            f"ultraviolet index runs {uvi}, rising and falling respectively")


CLAIMS = [
 ("replacing ozone depleting chemicals with substitutes that do not deplete the ozone layer",
  "STB-4.B.1 verbatim in substance: ozone depletion can be mitigated by replacing ozone-depleting chemicals with substitutes that do not deplete the ozone layer. Slower release, surface manufacture and shading are not the framework's strategy."),
 ("One replacement for ozone depleting chemicals",
  "STB-4.B.1 states that hydrofluorocarbons are one such replacement. Chlorofluorocarbons are the anthropogenic cause named in STB-4.A.2, not the replacement."),
 ("yet one of those substitutes still carries a very large warming potential",
  "Recomputed in q3 above: exactly one row is marked as depleting and it is the chlorofluorocarbon, while one of the three substitutes carries a warming potential above one thousand. That is STB-4.B.1's own caveat that some replacements are strong greenhouse gases."),
 ("Some of them are strong greenhouse gases",
  "STB-4.B.1 states that hydrofluorocarbons are one such replacement, but some are strong greenhouse gases. It does not say they deplete ozone or that they convert into the chemicals they replaced."),
 ("Chlorofluorocarbons",
  "Learning objective STB-4.B concerns chemicals used to substitute for chlorofluorocarbons, and STB-4.A.2 names chlorofluorocarbons as an anthropogenic cause of stratospheric ozone depletion. The rejected options are pollutants from other units."),
 ("production of the ozone depleting chemicals fell across the periods, the springtime ozone column rose",
  "Recomputed in q6 above: production falls at every step in row order while the ozone column rises at every step. STB-4.B.1 makes replacement the mitigation and STB-4.A.2 names those chemicals as a cause."),
 ("removes from use the chemicals that cause the depletion",
  "STB-4.B.1 describes replacing ozone-depleting chemicals with substitutes that do not deplete the layer, and STB-4.A.2 names those chemicals as a cause, so the response acts on the cause rather than on the damage."),
 ("It must not deplete the ozone layer",
  "STB-4.B.1 defines the strategy as replacing ozone-depleting chemicals with substitutes that do not deplete the ozone layer. Price, natural origin and rapid breakdown are not mentioned, and the framework accepts that some substitutes are strong greenhouse gases."),
 ("while some substitutes contribute strongly to the greenhouse effect",
  "STB-4.B.1 states that hydrofluorocarbons are one such replacement, but some are strong greenhouse gases, so the ozone problem can be addressed while a climate concern remains."),
 ("chlorofluorocarbons fell across the decades while the use of hydrofluorocarbons rose",
  "Recomputed in q10 above: the chlorofluorocarbon column falls at every step while the hydrofluorocarbon column rises at every step. STB-4.B.1 names hydrofluorocarbons as one replacement."),
 ("compounds in that class differ from one another",
  "STB-4.B.1 says that hydrofluorocarbons are one such replacement, but some are strong greenhouse gases, which qualifies the claim to part of the class rather than to all or to none of it."),
 ("meets the ozone requirement but may still carry a strong greenhouse effect",
  "STB-4.B.1 makes not depleting the ozone layer the requirement for a substitute and then adds that some replacements are strong greenhouse gases, so the one criterion does not settle the other."),
 ("also includes it among the principal greenhouse gases",
  "STB-4.A.2 names chlorofluorocarbons as an anthropogenic cause of stratospheric ozone depletion and STB-4.C.1 includes chlorofluorocarbons among the principal greenhouse gases, so both statements apply to the same compounds."),
 ("first option, whose release is equivalent to 14,000 tons of carbon dioxide",
  "Recomputed in q14 above: each mass times its warming potential gives a carbon dioxide equivalent, the largest belongs to the first row, and its value is exactly the keyed figure. STB-4.D.1 makes carbon dioxide the reference and STB-4.B.1 is why a replacement's potential matters."),
 ("the one with the smaller warming potential",
  "STB-4.B.1 requires a substitute not to deplete the ozone layer and adds that some replacements are strong greenhouse gases, so between two compounds that both pass the first test the warning applies to the second property."),
 ("the depletion is reduced by acting on what causes it",
  "STB-4.B.1 states that ozone depletion can be mitigated by replacing ozone-depleting chemicals with substitutes that do not deplete the layer, so mitigation here is a reduction achieved by removing the cause."),
 ("ozone column measured over the pole recovers",
  "STB-4.B.1 makes replacement the mitigation and STB-4.A.3 makes the state of the stratospheric ozone the quantity at stake, so falling production with a recovering column is the evidence. Ground level ozone belongs to EIN-3.C.4."),
 ("Only one candidate both avoids depleting the ozone layer and carries a small warming potential",
  "Recomputed in q18 above: exactly one candidate has an ozone depleting potential of zero together with a warming potential below one hundred, and at least one non-depleting candidate fails the second test. That is STB-4.B.1's pair of concerns."),
 ("continuing to use them leaves the cause in place",
  "STB-4.B.1 describes mitigation as replacing ozone-depleting chemicals with substitutes that do not deplete the layer, and STB-4.A.2 names those chemicals as a cause of the depletion."),
 ("skin cancer and cataracts that can follow increased ultraviolet exposure",
  "STB-4.A.3 states that a decrease in stratospheric ozone increases the ultraviolet rays reaching the surface and that exposure can lead to skin cancer and cataracts, and STB-4.B.1 is the response to that depletion. The rejected options are unit 8 health effects."),
 ("demonstration that it does not deplete the ozone layer",
  "STB-4.B.1 defines the substitute by the property of not depleting the ozone layer. Cost, distribution, manufacturing speed and solubility are not part of the statement."),
 ("springtime ozone column rose across the periods while the ultraviolet index at the surface fell",
  "Recomputed in q22 above: the ozone column rises at every step while the ultraviolet index falls at every step. STB-4.A.3 supplies the inverse relation and STB-4.B.1 the mitigation that produces it."),
 ("Hydrofluorocarbons, paired with being one replacement for ozone depleting chemicals",
  "STB-4.B.1 names hydrofluorocarbons as one replacement, STB-4.A.2 names chlorofluorocarbons as an anthropogenic cause of depletion, and STB-4.C.1 includes chlorofluorocarbons among the principal greenhouse gases. Each rejected pairing crosses two of those."),
 ("substitute that is itself a strong greenhouse gas",
  "STB-4.B.1 states that hydrofluorocarbons are one such replacement, but some are strong greenhouse gases, which is a response to one problem that contributes to another."),
 ("every hydrofluorocarbon is a strong greenhouse gas",
  "STB-4.B.1 says that SOME hydrofluorocarbons are strong greenhouse gases, so the universal claim is the one the framework does not make. The four rejected options restate the sentence accurately."),
 ("act as a greenhouse gas without depleting ozone",
  "STB-4.B.1 warns that some replacements are strong greenhouse gases even though they do not deplete the ozone layer, so the two properties are separate. STB-4.C.1's list of principal greenhouse gases includes compounds unrelated to ozone depletion."),
 ("but some are strong greenhouse gases",
  "STB-4.B.1 pairs the replacement with the warning that some of the replacements are strong greenhouse gases, which is precisely the reported outcome. The rejected statements concern the causes and consequences of the depletion itself."),
 ("leave the ozone layer undepleted and also avoid acting as a strong greenhouse gas",
  "STB-4.B.1 sets the ozone requirement and then names the greenhouse concern that some replacements raise, so satisfying both concerns means passing both tests."),
 ("does not deplete the ozone layer and whose warming potential is low",
  "STB-4.B.1 requires a substitute that does not deplete the ozone layer and warns that some replacements are strong greenhouse gases, so a low warming potential answers the warning while the first property answers the strategy."),
 ("though some of them are strong greenhouse gases",
  "The keyed summary is STB-4.B.1 in full, with all three of its parts. Every rejected summary reverses the strategy, denies the caveat, misdescribes the replacement, or denies that a response exists."),
]

TABLE_CHECKS = {3: q3, 6: q6, 10: q10, 14: q14, 18: q18, 22: q22}

es.run(e9_2, CLAIMS, TABLE_CHECKS, sys.argv)
