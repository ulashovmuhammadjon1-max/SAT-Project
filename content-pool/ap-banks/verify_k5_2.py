"""Key audit for AP COMPARATIVE GOVERNMENT 5.2 Political Responses to Global
Market Forces.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
Learning objective IEF-3.B, three essential knowledge statements:

  IEF-3.B.1  course countries CONTINUE TO EXPERIMENT with policies on PRIVATE
             OWNERSHIP OF INDUSTRY AND CAPITAL: .a coastal SPECIAL ECONOMIC ZONES
             in China, .b PRIVATIZATION AND INCREASED COMPETITION in Mexico's oil
             industry, .c Nigeria's STATE-OWNED petroleum corporation in JOINT
             VENTURES with foreign companies, .d RE-NATIONALIZATION of oil and
             gas plus FOREIGN INVESTMENT LIMITATIONS in Russia
  IEF-3.B.2  VARYING DEGREES of private control of natural resources, the UNITED
             KINGDOM the MOST and CHINA the LEAST
  IEF-3.B.3  governments respond in order to .a improve domestic economic
             conditions, .b respond to domestic demands, .c CONTROL OR INFLUENCE
             DOMESTIC POLITICAL DEBATES TO MAINTAIN OR INCREASE THEIR OWN POWER,
             .d extend national influence regionally and internationally

THE FOUR EXAMPLES DO NOT POINT THE SAME WAY, and that is the whole topic. Two
open (coastal zones, privatization with competition), one is a hybrid (state
ownership retained, foreign partners admitted), one closes (re-nationalization
plus investment limits). A student carrying the assumption that globalization
means liberalization cannot place the fourth. IEF-3.B.1's own verb is EXPERIMENT.
Items 11, 12, 13, 14 and 27 all key that divergence, and item 27's table check
confirms that exactly one of the four episodes withdraws participation while the
other three admit it -- if two did, the item would have two answers.

IEF-3.B.2 IS A SPECTRUM WITH TWO NAMED ENDS, not a ranking. The framework fixes
the United Kingdom at the most-private end and China at the least, and says the
rest vary. Item 19 keys that reading and the module never places a third course
country on the scale, because the framework does not. The spectrum table's rows
are unnamed hypotheticals for the same reason.

IEF-3.B.3.c IS THE PURPOSE STUDENTS DROP. Three of the four reasons concern the
economy, the public or the country's standing; the third concerns the
government's own hold on power, and it is the one that explains why two
governments of different regime types can adopt the same measure for different
reasons. Items 9, 15 and 28 key it, and item 28's check confirms only one row of
the motive table names both the debate and the government's own position.

NOTHING HERE TURNS ON CURRENT EVENTS -- no price, output figure, exchange rate,
election or date beyond what the framework itself states. Every table figure is
HYPOTHETICAL and labelled so.

DATA ITEMS
----------
Items 21-23 read the spectrum table, 24-27 the episode table, 28-29 the motive
table. The episode and motive checks are structural: they confirm the keyed row
carries the framework's distinguishing feature and that NO other row carries it,
which is what makes a single-answer item single-answered. Item 23's arithmetic
distractors are each verified to be a real gap elsewhere in the same column.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k5_2

PRIV = "Natural resource output produced by privately owned firms (percent)"
LIMITS = "Limits on foreign investment in the resource sector"
DID = "What the government did"
REASON = "Reason given for the policy"


def _spec(table):
    return {lab: (cg.cell(table, lab, PRIV), str(table["rows"][i][2]))
            for i, lab in enumerate(cg.labels(table))}


def q21(table, item):
    v = _spec(table)
    top = max(v, key=lambda k: v[k][0])
    assert top == "Country A", f"the largest private share belongs to {top}"
    assert v["Country A"][0] == 91, f"the keyed 91 percent reads {v['Country A'][0]}"
    assert v["Country A"][1].lower() == "none", \
        f"the keyed row must also place no limits on foreign investment; it reads {v['Country A'][1]!r}"
    others = [lab for lab in v if lab != "Country A" and v[lab][1].lower() == "none"]
    assert not others, f"no other row may be unrestricted, or the key would not be unique; also {others}"
    assert v["Country B"][0] == 62 and v["Country C"][1].lower() == "extensive" and v["Country D"][0] == 4, \
        "each rejected option must state its own row truly"
    return f"the private-share column reads {[v[k][0] for k in v]} against limits {[v[k][1] for k in v]}"


def q22(table, item):
    v = _spec(table)
    bottom = min(v, key=lambda k: v[k][0])
    assert bottom == "Country D", f"the smallest private share belongs to {bottom}"
    assert v["Country D"] == (4, "Extensive"), f"the keyed row reads {v['Country D']}"
    assert v["Country C"][0] == 28 and v["Country B"][1].lower() == "some" and v["Country A"][1].lower() == "none", \
        "each rejected option must state its own row truly"
    assert min(v[k][0] for k in v) > 0, "'no private production anywhere' must be false, so the rejected final option is testable"
    return f"the smallest private share is {v['Country D'][0]:.0f} percent, paired with extensive limits on foreign investment"


def q23(table, item):
    p = cg.col(table, PRIV)
    gap = max(p) - min(p)
    assert gap == 87, f"the keyed gap recomputes to {gap}"
    pairs = {abs(a - b) for a in p for b in p if a != b}
    for d in (63, 34, 24):
        assert d in pairs, f"the {d} distractor must be another gap in the same column; gaps are {sorted(pairs)}"
    assert max(p) == 91, "the 91 distractor must be the largest single figure read as a gap"
    return f"the private-share column reads {p}, so the largest minus the smallest is {gap:.0f} percentage points"


def _ep(table):
    return {str(r[0]): str(r[1]).lower() for r in table["rows"]}


def _only(v, key, needle, label):
    assert needle in v[key], f"the keyed episode must contain {needle!r}; it reads {v[key]!r}"
    others = [k for k in v if k != key and needle in v[k]]
    assert not others, f"{label}: {needle!r} must appear in one episode only; also {others}"


def q24(table, item):
    v = _ep(table)
    _only(v, "Episode 1", "coastal", "coastal zones")
    assert "special terms" in v["Episode 1"], "the keyed episode must offer terms unavailable elsewhere"
    return "one episode alone opens designated coastal areas to foreign investment on special terms"


def q25(table, item):
    v = _ep(table)
    _only(v, "Episode 2", "competitors", "competition")
    assert "private investment" in v["Episode 2"], "the keyed episode must admit private investment as well as competitors"
    return "one episode alone admits both private investment into the national oil company and competitors into the industry"


def q26(table, item):
    v = _ep(table)
    _only(v, "Episode 3", "joint ventures", "joint ventures")
    assert "state hands" in v["Episode 3"], "the keyed episode must keep the corporation in state hands"
    assert "state ownership" in v["Episode 4"], \
        "the re-nationalization episode must be the other one mentioning state ownership, so the two are distinguishable"
    return "one episode alone keeps the petroleum corporation in state hands while entering joint ventures with foreign firms"


def q27(table, item):
    v = _ep(table)
    _only(v, "Episode 4", "returned", "re-nationalization")
    assert "limits on foreign investment" in v["Episode 4"], \
        "the keyed episode must impose investment limits as well as restoring state ownership"
    opening = [k for k in v if k != "Episode 4"
               and ("foreign investment" in v[k] or "private investment" in v[k] or "foreign firms" in v[k])]
    assert len(opening) == 3, \
        f"the other three episodes must each admit private or foreign participation, or the key is not unique; they are {opening}"
    for k in opening:
        assert "limits on foreign investment" not in v[k], f"{k} must not also restrict foreign investment"
    return "three episodes admit private or foreign participation and one withdraws it, so exactly one runs the other way"


def _mot(table):
    return {str(r[0]): str(r[1]).lower() for r in table["rows"]}


def q28(table, item):
    v = _mot(table)
    assert "government's own position" in v["Statement 3"], f"the keyed row reads {v['Statement 3']!r}"
    assert "argued about" in v["Statement 3"], "the keyed row must name the domestic debate as well as the government's position"
    others = [k for k in v if k != "Statement 3" and "own position" in v[k]]
    assert not others, f"no other statement may name the government's own position; also {others}"
    return "one statement alone joins shaping the domestic argument to securing the government's own position"


def q29(table, item):
    v = _mot(table)
    assert "petitions" in v["Statement 2"], f"the keyed row reads {v['Statement 2']!r}"
    others = [k for k in v if k != "Statement 2" and "petitions" in v[k]]
    assert not others, f"no other statement may name petitions; also {others}"
    assert "output and employment" in v["Statement 1"] and "region" in v["Statement 4"], \
        "the rejected statements must be the economic purpose and the outward-looking one, so all four purposes are present"
    return "one statement alone reports a demand arriving from citizens and associations rather than an economic or external aim"


CLAIMS = [
 ("policies regarding private ownership of industry and capital",
  "EK IEF-3.B.1 states that in response to market forces course countries continue to experiment with policies regarding private ownership of industry and capital, and its verb experiment marks those policies as unsettled rather than fixed."),
 ("special economic zones",
  "EK IEF-3.B.1.a names special economic zones along the coast of China among the experiments with private ownership of industry and capital. Each rejected policy is one of the framework's other three country examples."),
 ("privatization and increased competition",
  "EK IEF-3.B.1.b names privatization and increased competition in Mexico's oil industry, and EK LEG-5.A.3.a records the same government's decision to allow private investment in that company."),
 ("state-owned corporation collaborating with foreign companies",
  "EK IEF-3.B.1.c states that Nigeria's state-owned Nigerian National Petroleum Corporation collaborates with foreign companies in joint ventures to extract and produce oil, so ownership stays with the state while foreign firms take part in production."),
 ("re-nationalization of oil and natural gas industries together with the imposition",
  "EK IEF-3.B.1.d names the re-nationalization of oil and natural gas industries and the imposition of foreign investment limitations together, so both halves reduce private and foreign control rather than pulling against each other."),
 ("the United Kingdom",
  "EK IEF-3.B.2 states that course countries allow varying degrees of private control of natural resources, with the United Kingdom allowing the most private control."),
 ("China",
  "EK IEF-3.B.2 states that course countries allow varying degrees of private control of natural resources, with China allowing the least private control."),
 ("controlling or influencing domestic political debates to maintain or increase their own power",
  "EK IEF-3.B.3 names improving domestic economic conditions, responding to domestic demands, controlling or influencing domestic political debates to maintain or increase their own power, and extending national influence regionally and internationally as the four purposes."),
 ("to maintain or increase their own power",
  "EK IEF-3.B.3.c is the only one of the four purposes stated in terms of the government's own position, since it names controlling or influencing domestic political debates to maintain or increase their own power."),
 ("extending national influence regionally and internationally",
  "EK IEF-3.B.3.d is the only one of the four purposes directed outside the country, naming the extension of national influence regionally and internationally."),
 ("returned oil and gas firms to state ownership and restricted foreign investment",
  "EK IEF-3.B.1.b names privatization and increased competition in Mexico's oil industry while EK IEF-3.B.1.d names re-nationalization and the imposition of foreign investment limitations in Russia, so the two experiments run in opposite directions."),
 ("created zones on its coast where foreign investment is admitted",
  "EK IEF-3.B.1.a names special economic zones along the coast of China and EK IEF-3.B.1.d names the imposition of foreign investment limitations in Russia, so one example widens the opening to foreign capital and the other narrows it."),
 ("remains state-owned while working with foreign firms",
  "EK IEF-3.B.1.c keeps Nigeria's petroleum corporation state-owned while it enters joint ventures with foreign companies, and EK IEF-3.B.1.b records privatization and increased competition in Mexico's oil industry, so foreign participation without a transfer of ownership differs from opening the industry to private owners."),
 ("there is no single direction",
  "EK IEF-3.B.1 introduces its examples with the verb experiment, and the four it gives include coastal zones open to foreign investment and privatization on one side against re-nationalization with foreign investment limitations on the other."),
 ("controlling or influencing domestic political debates",
  "EK IEF-3.B.3.c states that governments respond to global market forces in order to control or influence domestic political debates to maintain or increase their own power, and an argument pitched at quieting criticism and keeping the government secure is that purpose stated openly."),
 ("special economic zones along a coast",
  "EK IEF-3.B.1.a names special economic zones along the coast of China among the experiments with private ownership of industry and capital, and a coastal district offering investment terms available nowhere else is what such a zone is."),
 ("together with foreign investment limitations",
  "EK IEF-3.B.1.d names the re-nationalization of oil and natural gas industries and the imposition of foreign investment limitations as a single example, and the scenario contains both halves of it."),
 ("collaborating with foreign companies in joint ventures",
  "EK IEF-3.B.1.c describes a state-owned petroleum corporation collaborating with foreign companies in joint ventures to extract and produce oil, which admits foreign participation while ownership stays with the state."),
 ("a spectrum whose two ends the framework names",
  "EK IEF-3.B.2 states that course countries allow varying degrees of private control of natural resources and names only the two extremes, so it fixes endpoints rather than dividing the countries into groups or ordering all six."),
 ("a larger role in a regional organization",
  "EK IEF-3.B.3.d states that governments respond to global market forces in order to extend national influence regionally and internationally, so supporting evidence must point outside the country, while the rejected findings point instead to EK IEF-3.B.3.b, EK IEF-3.B.3.a and EK IEF-3.B.3.c."),
 ("91 percent of resource output",
  "EK IEF-3.B.2 places one end of its spectrum where the most private control of natural resources is allowed. Recomputed in q21 above, where one row alone combines the largest private share with no limit on foreign investment."),
 ("only 4 percent of resource output",
  "EK IEF-3.B.2 places the other end of its spectrum where the least private control is allowed. Recomputed in q22 above, where one row alone combines the smallest private share with extensive limits on foreign investment."),
 ("87 percentage points",
  "Recomputed in q23 above by subtracting the smallest private share from the largest. The distractors are three other gaps in the same column and the largest single figure read as though it were a gap."),
 ("designated coastal areas",
  "EK IEF-3.B.1.a names special economic zones along the coast of China. Recomputed in q24 above, where only one episode opens designated coastal areas to foreign investment on terms unavailable elsewhere."),
 ("competitors were admitted to the industry",
  "EK IEF-3.B.1.b names privatization and increased competition in Mexico's oil industry, so the matching episode has to show both private investment entering the national company and competitors entering the industry. Recomputed in q25 above."),
 ("stayed in state hands while entering joint ventures",
  "EK IEF-3.B.1.c states that Nigeria's state-owned petroleum corporation collaborates with foreign companies in joint ventures to extract and produce oil. Recomputed in q26 above, which also checks that the re-nationalization episode is distinguishable from this one."),
 ("returned to state ownership and limits were imposed on foreign investment",
  "EK IEF-3.B.1's other three examples each admit private or foreign participation while EK IEF-3.B.1.d withdraws it. Recomputed in q27 above, which confirms that exactly one episode withdraws participation, so the item has a single answer."),
 ("securing the government's own position",
  "EK IEF-3.B.3.c states that governments respond to global market forces in order to control or influence domestic political debates to maintain or increase their own power. Recomputed in q28 above, where one row alone names both the domestic argument and the government's own position."),
 ("answering petitions submitted by citizens and associations",
  "EK IEF-3.B.3.b states that governments respond to global market forces in order to respond to domestic demands, and a petition from citizens and associations is a demand arriving from the public rather than an economic aim or a matter of standing abroad. Recomputed in q29 above."),
 ("some opening and at least one closing",
  "EK IEF-3.B.1 supplies four experiments running in different directions, EK IEF-3.B.2 the spectrum of private control over natural resources with its two named ends, and EK IEF-3.B.3 the four purposes, two of them economic or public and two about power and standing."),
]

cg.check(k5_2, CLAIMS,
         table_checks={21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29})
