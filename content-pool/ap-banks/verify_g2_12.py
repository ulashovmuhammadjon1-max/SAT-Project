"""Key audit for AP HUMAN GEOGRAPHY 2.12 Effects of Migration.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. This topic has exactly one essential-knowledge statement, and
it is the shortest in Unit 2:

    IMP-2.E.1  Migration has political, economic, and cultural effects.

Three domains, no examples and no definitions. So the citable content is the
CLASSIFICATION and nothing else: which of the three an effect belongs to. Items
1, 2, 3, 4, 6, 7, 11, 12, 14, 18, 19, 22 and 25 are keyed to that and cite it.
Everything else in the module -- what brain drain is, why remittances are
countercyclical, why an enclave is not just a dense district -- is argued in the
claim, because attaching "EK IMP-2.E.1" to a definition the CED never printed
would be a fabricated citation.

THE SECOND AXIS, which the CED does not name and the exam always uses: an effect
falls on the ORIGIN, on the DESTINATION, or on both, and the same migration
routinely produces OPPOSITE effects at the two ends. A departing nurse is a
shortage in one country and a filled vacancy in another; remittances are income
where they are spent and a wage bill where they are earned. Items 3, 5, 8, 13,
17, 21, 24, 26 and 30 are built on that, and item 30's table makes it
undeniable by pairing a losing district with a gaining one inside one country.

THE EVALUATION TRAP, and how the module avoids it. Migration's effects are
politically contested, so an item that asks whether an effect is GOOD is asking
students to guess a preference rather than to reason. Item 15 therefore keys to
"the effect differs by occupation, skill level, and time period" rather than to
a sign, and item 24 keys to an answer that records an improvement and a loss
together. That is the honest reading and it is also the defensible one.

The five table items (26-30) are the computational gate, and three of them
separate a RATE from a COUNT:

  26  the country receiving the most remittance dollars is the LEAST dependent
  27  the country losing the most physicians has the LOWEST loss rate
  28  the sector employing the most foreign-born workers is not the most exposed
  29  each row sums to 100, so only composition can be read, and the largest
      change is the rise in bilingual households rather than replacement
  30  one district's loss and another's gain are the same flow seen twice

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g2_12


def q26_remittance_dependence(table):
    """Dependence is a share of national income, not a dollar total."""
    share, amount = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        rem = num(d["Remittances received (US$ billions)"])
        gdp = num(d["GDP (US$ billions)"])
        amount[d["Country"]] = rem
        share[d["Country"]] = 100 * rem / gdp
    most = max(share, key=share.get)
    assert most == "Country B", share
    assert share == {"Country A": 5.0, "Country B": 30.0,
                     "Country C": 2.5, "Country D": 10.0}, share
    # The largest dollar total must belong to the LEAST dependent country.
    biggest = max(amount, key=amount.get)
    assert biggest != most, amount
    assert share[biggest] == min(share.values()), (amount, share)
    return "30 percent of national income"


def q27_brain_drain_rate(table):
    """Loss as a share of each trained cohort, against the absolute loss."""
    rate, lost = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        trained = num(d["Physicians trained (per year)"])
        gone = num(d["Physicians emigrating within five years"])
        lost[d["Country"]] = gone
        rate[d["Country"]] = 100 * gone / trained
    worst = max(rate, key=rate.get)
    assert worst == "Country Q", rate
    assert rate == {"Country P": 20.0, "Country Q": 70.0,
                    "Country R": 10.0, "Country S": 30.0}, rate
    # The country losing the most doctors must have the LOWEST rate.
    most_lost = max(lost, key=lost.get)
    assert most_lost != worst, lost
    assert rate[most_lost] == min(rate.values()), (lost, rate)
    return "70 percent of each cohort"


def q28_sector_exposure(table):
    """Exposure is the foreign-born share of a sector, not the headcount."""
    share, count = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        total = num(d["Total workers (thousands)"])
        fb = num(d["Foreign-born workers (thousands)"])
        count[d["Sector"]] = fb
        share[d["Sector"]] = 100 * fb / total
    most_exposed = max(share, key=share.get)
    assert most_exposed == "Agriculture and food processing", share
    assert share == {"Agriculture and food processing": 65.0,
                     "Construction": 35.0,
                     "Health and social care": 30.0,
                     "Public administration": 10.0}, share
    # The sector with the most foreign-born workers must not be the answer.
    assert max(count, key=count.get) != most_exposed, count
    return "65 percent of workers are foreign-born"


def q29_language_composition(table):
    """Rows sum to 100, and the bilingual category makes the largest move."""
    only_nat = numcol(table, "National language only (%)")
    both = numcol(table, "National language and another (%)")
    only_other = numcol(table, "Another language only (%)")
    for i in range(len(only_nat)):
        assert only_nat[i] + both[i] + only_other[i] == 100, i
    assert only_nat[0] - only_nat[-1] == 44, only_nat
    assert both[-1] - both[0] == 33, both
    assert only_other[-1] - only_other[0] == 11, only_other
    # Bilingual growth must exceed other-language-only growth, or the key's
    # reading (bilingualism, not replacement) is wrong.
    assert (both[-1] - both[0]) > (only_other[-1] - only_other[0]), (both, only_other)
    # And other-language-only must never become the largest category.
    for i in range(len(only_nat)):
        assert only_other[i] < max(only_nat[i], both[i]), i
    return "from 9 to 42 percent"


def q30_two_ends_one_flow(table):
    """One district loses young adults and ages; the other gains them and does not."""
    d = {}
    for row in table["rows"]:
        r = rowdict(table, row)
        d[r["District"]] = (num(r["Net migration rate (per 1,000)"]),
                            num(r["Share aged 20-39 (%)"]),
                            num(r["Share aged 65+ (%)"]))
    losing = [k for k in d if d[k][0] < 0]
    gaining = [k for k in d if d[k][0] > 0]
    assert len(losing) == 1 and len(gaining) == 1, d
    lo, gi = d[losing[0]], d[gaining[0]]
    # The losing district must be the older one on both age measures.
    assert lo[1] < gi[1], d
    assert lo[2] > gi[2], d
    # The two rates must be of comparable size, since it is one internal flow.
    assert abs(abs(lo[0]) - gi[0]) < 10, d
    return "aged one district and rejuvenated the other"


CLAIMS = [
 ("Political, economic, and cultural",
  "EK IMP-2.E.1 states that migration has political, economic and cultural effects, and the list is exactly three. Environmental, demographic and technological consequences do follow from migration, but they are not the three this statement names."),

 ("economic effect at the origin",
  "EK IMP-2.E.1 names economic effects and remittances are the clearest of them. The wages are earned at the destination and spent at the origin, so the effect on household income falls on the country the migrants left."),

 ("known as brain drain",
  "EK IMP-2.E.1 names economic effects, and this is the standard case in which the effect at the origin and the effect at the destination run opposite. The public training investment is made in one country and the return on it collected in another; the term itself is not the CED's and is defined in the module header."),

 ("cultural effect at the destination, visible in the district's landscape",
  "EK IMP-2.E.1 names cultural effects, and the visible institutions of a community are how those effects appear on the ground. That the shops are also businesses does not make the effect economic, since the item asks what the change principally is."),

 ("shortage of trained nurses at the origin and a filled vacancy at the destination",
  "A migrant is subtracted from one labour market and added to another, so a single move produces a deficit in one place and a surplus in the other. EK IMP-2.E.1's economic effects are frequently of this kind, which is why origin and destination must be considered separately."),

 ("political effect of migration at the destination",
  "EK IMP-2.E.1 names political effects, and the arrival of a population that can organize and eventually vote changes what a destination's politics is about. That the activity itself is ordinary is what makes the effect political rather than exceptional."),

 ("political effect at the origin, produced by people who are no longer resident",
  "EK IMP-2.E.1 names political effects without confining them to the receiving country. A diaspora retains an interest in the politics of the place it left and often commands resources the residents do not, so its influence there can be considerable."),

 ("labour force shrinks and a cultural effect as institutions and traditions lose",
  "EK IMP-2.E.1 names three kinds of effect and nothing prevents one migration from producing more than one. A school, a festival and a football club each require people of particular ages, so a selective loss reaches the culture as directly as the labour market."),

 ("concentrated in the young working ages",
  "Migration is strongly selective by age, so a receiving country imports a slice of the pyramid rather than a cross-section of it. The effect on age structure follows from who moves rather than from anything happening to the resident population."),

 ("dependent on labour markets and immigration policies it does not control",
  "EK IMP-2.E.1's economic effects include the structure of an economy as well as the flow of money through it. A recession or a rule change abroad transmits directly into household income at home, which is a dependence rather than a benefit or a cost."),

 ("receiving society itself is changed by the people it receives",
  "EK IMP-2.E.1 names cultural effects, and this is the reciprocal case: the receiving society is not a fixed container that migrants enter. That cultures change anyway does not make a specific change caused by specific arrivals uncaused."),

 ("Sectors that depend on migrant labour can expand",
  "EK IMP-2.E.1 separates economic from political and cultural effects, and this option concerns labour supply and wages. Language and worship are cultural, an electoral constituency is political, and a country's land area does not change at all."),

 ("influence flows along the same route in both directions",
  "EK IMP-2.E.1's three kinds of effect are not confined to one end of a migration, and a migration route is a channel rather than a one-way pipe. Remittances, return visits and changed expectations about schooling or marriage all travel back along it."),

 ("state acquires interests and obligations outside its own territory",
  "EK IMP-2.E.1 names political effects, and one of the least obvious is that a state with a large emigrant population must conduct a foreign policy about it. That obligation exists whether or not the migrants ever return."),

 ("differs by occupation, skill level, and time period",
  "EK IMP-2.E.1 names economic effects without assigning them a sign, and the evidence supports a disaggregated answer rather than a single one. Workers who compete directly with arrivals and workers whose services arrivals buy are affected in opposite directions."),

 ("returning to found firms and train others at home",
  "Brain gain is the return of skills and capital to an origin country, including through people who left and came back with more than they took. The other four options are all movements of trained people away from the country that paid to train them."),

 ("go directly to the household that needs them",
  "EK IMP-2.E.1's economic effects include the channel through which money reaches people, and remittances bypass the institutions aid must pass through. The countercyclical behaviour is what distinguishes them: a family sends more, not less, after a bad harvest."),

 ("language of a public institution changes, and an economic effect",
  "EK IMP-2.E.1 names three domains and one consequence can fall into more than one of them. The change in what language a public institution operates in is cultural, and the budget line it creates is economic."),

 ("central issue in national elections",
  "EK IMP-2.E.1 separates political from economic and cultural effects. Cuisine and worship are cultural, remittances and labour shortages are economic, and what an election is fought about is political by definition."),

 ("services need a threshold population",
  "EK IMP-2.E.1 names economic and cultural effects among its three, and both are present here: services close because too few people remain to sustain them, and their closure removes the places where the community met. Naming both is what makes the description complete."),

 ("one market tightens as the other loosens",
  "EK IMP-2.E.1's economic effects operate on two labour markets rather than one, and a migrant leaves a gap behind exactly as surely as they fill one ahead. Whether either market notices depends on how large the flow is relative to each."),

 ("identity is renegotiated across generations",
  "EK IMP-2.E.1 names cultural effects without limiting them to the migrants themselves. The consequences of a migration are worked out over generations, which is why a community's cultural geography keeps changing long after the arrivals stop."),

 ("frequently opposite in sign at the two ends",
  "EK IMP-2.E.1 names three domains without assigning a sign or a location to any of them. A general claim that survives is therefore structural -- where the effects fall and how they differ -- rather than an evaluation of whether they are good."),

 ("hollowed out the local workforce",
  "EK IMP-2.E.1's economic effects can run in both directions at the same place, and this is the standard case. The money and the missing people arrive from the same decision, so an honest account records the improvement and the loss together rather than choosing one."),

 ("worship, and signage in the district serve that community",
  "An enclave is defined by the concentration of one origin group together with the institutions that concentration supports, which is EK IMP-2.E.1's cultural effect made visible on the landscape. Density, income, location and growth rate are true of many districts that are not enclaves."),

 ("30 percent of national income",
  "Recomputed from the table: remittances are 5, 30, 2.5 and 10 percent of national income. The verifier confirms the country receiving the largest dollar amount is the LEAST dependent of the four, which is why dependence has to be read as a ratio rather than a total.",
  q26_remittance_dependence),

 ("70 percent of each cohort",
  "Recomputed from the table: emigration takes 20, 70, 10 and 30 percent of each trained cohort. The verifier confirms the country losing the most physicians in absolute terms has the lowest loss rate of the four, so a small programme losing seven in ten graduates is the severe case.",
  q27_brain_drain_rate),

 ("65 percent of workers are foreign-born",
  "Recomputed from the table: foreign-born shares are 65, 35, 30 and 10 percent of each sector's workforce. The verifier confirms the sector employing the most foreign-born workers in absolute terms is not the most exposed, since exposure is the share that would be missing.",
  q28_sector_exposure),

 ("from 9 to 42 percent",
  "Recomputed from the table: every row sums to 100, the national-language-only share falls 44 points, bilingual households rise 33 points and other-language-only rises 11. The verifier confirms bilingualism grows faster than replacement and that other-language-only never becomes the largest category.",
  q29_language_composition),

 ("aged one district and rejuvenated the other",
  "Recomputed from the table: one district loses 18 per 1,000 and holds 17 percent aged 20 to 39 against 29 percent over 65, while the other gains 21 per 1,000 with 34 percent young adults and 12 percent elderly. The verifier confirms the losing district is older on both age measures and that the two rates are of comparable size, since this is one internal flow seen from both ends.",
  q30_two_ends_one_flow),
]

hg_check.check(g2_12, CLAIMS, per_topic=30, n_choices=5)
