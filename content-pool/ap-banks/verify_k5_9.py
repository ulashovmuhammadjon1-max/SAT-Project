"""Key audit for AP COMPARATIVE GOVERNMENT 5.9 Impact of Natural Resources.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
Learning objective LEG-5.A, four essential knowledge statements:

  LEG-5.A.1  RENTIER STATES (Iran, Nigeria, Russia) draw a SIZABLE PERCENTAGE OF
             TOTAL GOVERNMENT REVENUE from EXPORTING OIL AND GAS or LEASING THE
             RESOURCE, and have RAISED STANDARDS OF LIVING AND FUNDED GOVERNMENTAL
             PROGRAMS
  LEG-5.A.2  the RESOURCE CURSE, nine outcomes .a-.i, of which .h is A LACK OF
             GOVERNMENTAL ACCOUNTABILITY TO CITIZENS WHEN NOT RELYING ON CITIZENS
             FOR TAXES
  LEG-5.A.3  resources are NATIONALIZED IN CHINA, IRAN, MEXICO, NIGERIA AND RUSSIA
             to provide revenue, consolidate control and reduce foreign influence,
             all of which CAN REINFORCE POLITICAL LEGITIMACY; the DEGREE OF CENTRAL
             CONTROL DIFFERS (.a private investment in Pemex, .b foreign MNCs
             exercising political control in Nigeria, .c high centralization and
             WEALTH CONCENTRATION in Russia)
  LEG-5.A.4  PRIVATIZED OWNERSHIP decreases government control, increases wealth
             inequality, and results in the POTENTIAL LOSS OF SOVEREIGNTY

LEG-5.A.2.h IS THE SHARPEST CLAIM IN THE UNIT and the module is built around it.
A government funded by selling a resource is not funded by its citizens, and the
framework states the consequence directly. It is a claim about the DIRECTION OF
DEPENDENCE, not about how rich a country is, which is why item 10's distractors
are all about wealth, dispersion or law rather than about who pays, and why the
first table's key rests on the SHARE of revenue coming from taxes rather than on
any revenue total.

THE FRAMEWORK SAYS BOTH GOOD AND BAD. LEG-5.A.1 credits rentier states with
raising standards of living and funding governmental programs; LEG-5.A.2 then
lists nine adverse outcomes; and enduring understanding LEG-5 says resource
endowments have POSITIVE AND NEGATIVE effects. An answer that keeps one half
contradicts the framework's own heading, which is what item 18 tests and why both
one-sided readings appear among its distractors.

THE THREE INSTANCES IN LEG-5.A.3 ARE A SCALE, NOT A LIST. All five named
countries nationalize; what differs is the DEGREE of central control -- private
investors admitted at one end, foreign corporations exercising political control
in the middle, high centralization with wealth concentration at the other. Items
14, 15, 16 and 27-29 key positions on that scale, and item 29 pairs the position
with the outcome the framework attaches to it, so the arrangement alone does not
settle it.

NOTHING HERE TURNS ON CURRENT EVENTS: no oil price, production figure, revenue
share, contract, sanction or dispute of any real country is asserted anywhere.
Every table figure is HYPOTHETICAL, labelled so, and attached to unnamed
countries or years.

DATA ITEMS
----------
Items 21-23 read the revenue table, 24-26 the price table, 27-29 the control
table. Item 21's key asserts a joint movement across THREE columns, so its check
orders the rows by the resource share and requires the other two to move
consistently; item 24's key asserts that revenue and spending follow the price
BOTH up and down, so its check tests both directions. Every arithmetic distractor
is verified to be a wrong operation on the same table.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k5_9

OIL = "Government revenue from oil and gas exports (percent of the total)"
TAX = "Government revenue from taxes on citizens and domestic firms (percent of the total)"
RESP = "Index of government responsiveness to citizen complaints"
PRICE = "World price index for the country's main export"
REV = "Government revenue index"
SPEND = "Spending on state programmes (index)"
HOW = "How the resource sector is controlled"


def _rent(table):
    return {lab: (cg.cell(table, lab, OIL), cg.cell(table, lab, TAX), cg.cell(table, lab, RESP))
            for lab in cg.labels(table)}


def q21(table, item):
    v = _rent(table)
    order = sorted(v, key=lambda k: v[k][0], reverse=True)
    taxes = [v[k][1] for k in order]
    resp = [v[k][2] for k in order]
    assert taxes == sorted(taxes), f"the tax share must rise as the resource share falls; ordered it reads {taxes}"
    assert resp == sorted(resp), f"responsiveness must rise as the resource share falls; ordered it reads {resp}"
    assert len(set(resp)) == 3, "'all three record the same responsiveness' must be false"
    assert min(taxes) > 0, "'no country draws revenue from taxes on citizens' must be false"
    return (f"ordering the rows by resource share {[v[k][0] for k in order]} gives tax shares {taxes} and "
            f"responsiveness {resp}, both rising as the resource share falls")


def q22(table, item):
    r = cg.col(table, RESP)
    diff = max(r) - min(r)
    assert diff == 53, f"the keyed difference recomputes to {diff}"
    pairs = {abs(a - b) for a in r for b in r if a != b}
    assert 26 in pairs and 27 in pairs, f"the 26 and 27 distractors must be the other gaps; gaps are {sorted(pairs)}"
    assert max(r) == 84 and min(r) == 31, f"the 84 and 31 distractors must be the column's extremes; it reads {r}"
    return f"the responsiveness column reads {r}, so the largest minus the smallest is {diff:.0f} points"


def q23(table, item):
    o = cg.col(table, OIL)
    diff = max(o) - min(o)
    assert diff == 72, f"the keyed difference recomputes to {diff}"
    pairs = {abs(a - b) for a in o for b in o if a != b}
    assert 37 in pairs and 35 in pairs, f"the 37 and 35 distractors must be the other gaps; gaps are {sorted(pairs)}"
    assert max(o) == 78 and min(o) == 6, f"the 78 and 6 distractors must be the column's extremes; it reads {o}"
    return f"the resource-share column reads {o}, so the largest minus the smallest is {diff:.0f} percentage points"


def q24(table, item):
    p, r, s = cg.col(table, PRICE), cg.col(table, REV), cg.col(table, SPEND)
    assert p[0] == r[0] == s[0] == 100, f"all three columns must be based at 100 in the first year; they read {p[0]}, {r[0]}, {s[0]}"
    assert p[1] > p[0] and r[1] > r[0] and s[1] > s[0], \
        f"all three must rise in the second year; they read {p[1]}, {r[1]}, {s[1]}"
    assert p[2] < p[0] and r[2] < r[0] and s[2] < s[0], \
        f"all three must end below the starting level; they read {p[2]}, {r[2]}, {s[2]}"
    assert len(set(r)) == 3, "'government revenue was steady' must be false"
    assert p[1] > p[0], "'the world price fell in every year' must be false"
    return f"the price goes {p}, revenue {r} and spending {s}, all three rising then falling below the base"


def q25(table, item):
    p, r = cg.col(table, PRICE), cg.col(table, REV)
    rng = max(p) - min(p)
    assert rng == 91, f"the keyed range recomputes to {rng}"
    assert max(p) - 100 == 52, "the 52 distractor must be the gap above the starting year"
    assert 100 - min(p) == 39, "the 39 distractor must be the gap below the starting year"
    assert max(p) == 152, "the 152 distractor must be the largest single figure read as a range"
    assert max(r) - min(r) == 69, "the 69 distractor must be the revenue column's range"
    return f"the price column reads {p}, so its range is {rng:.0f} points"


def q26(table, item):
    p, r = cg.col(table, PRICE), cg.col(table, REV)
    rng = max(r) - min(r)
    assert rng == 69, f"the keyed range recomputes to {rng}"
    assert max(r) - 100 == 41, "the 41 distractor must be the gap above the starting year"
    assert 100 - min(r) == 28, "the 28 distractor must be the gap below the starting year"
    assert max(r) == 141, "the 141 distractor must be the largest single figure read as a range"
    assert max(p) - min(p) == 91, "the 91 distractor must be the price column's range"
    return f"the revenue column reads {r}, so its range is {rng:.0f} points"


def _ctrl(table):
    return {str(r[0]): str(r[1]).lower() for r in table["rows"]}


def q27(table, item):
    v = _ctrl(table)
    assert "private investors have been admitted" in v["Arrangement 1"], f"the keyed row reads {v['Arrangement 1']!r}"
    others = [k for k in v if k != "Arrangement 1" and "private investors" in v[k]]
    assert not others, f"no other arrangement may admit private investors; also {others}"
    assert "state company remains" in v["Arrangement 1"], \
        "the keyed row must keep the state company in place, since the framework's instance is a nationalized sector"
    return "one arrangement alone keeps the state company while admitting private investors to it"


def q28(table, item):
    v = _ctrl(table)
    a2 = v["Arrangement 2"]
    assert "foreign multinational corporations" in a2 and "political influence" in a2, f"the keyed row reads {a2!r}"
    others = [k for k in v if k != "Arrangement 2" and "foreign multinational" in v[k]]
    assert not others, f"no other arrangement may involve foreign multinational corporations; also {others}"
    assert "underwrite production" in a2, "the keyed row must have the foreign firms underwriting production, as the framework does"
    return "one arrangement alone has foreign multinational corporations both underwriting production and exercising political influence"


def q29(table, item):
    v = _ctrl(table)
    a3 = v["Arrangement 3"]
    assert "high degree of centralized control" in a3, f"the keyed row reads {a3!r}"
    assert "wealth has become concentrated" in a3, \
        "the keyed row must pair the centralization with wealth concentration, since the key asserts both"
    for k in ("Arrangement 1", "Arrangement 2"):
        assert "centralized control" not in v[k], f"{k} must not also claim centralized control"
        assert "wealth" not in v[k], f"{k} must not also mention wealth, so the rejected pairings are false"
    return "one arrangement alone holds the sector under high centralization and records wealth concentration with it"


CLAIMS = [
 ("from leasing the resource to foreign countries",
  "EK LEG-5.A.1 defines rentier states as those obtaining a sizable percentage of total government revenue from the export of oil and gas or from leasing the resource to foreign countries, so the definition turns on where the revenue comes from."),
 ("Iran, Nigeria, and Russia",
  "EK LEG-5.A.1 names Iran, Nigeria, and Russia among rentier states, which are the course countries whose governments draw a sizable share of total revenue from oil and gas."),
 ("raise standards of living and fund governmental programs",
  "EK LEG-5.A.1 states that rentier states have been able to raise standards of living and fund governmental programs based on their huge reserves, which is the favorable half of the framework's account."),
 ("the resource curse",
  "EK LEG-5.A.2 states that the political and economic outcomes related to rentier state status are often referred to as the resource curse when petroleum is involved."),
 ("a lack of economic diversification",
  "EK LEG-5.A.2.a names a lack of economic diversification and EK LEG-5.A.2.b the concentration of governmental resources on developing the one profitable export industry to the exclusion of other types of industries."),
 ("world market pricing",
  "EK LEG-5.A.2.c names severe revenue fluctuations based on world market pricing, so the instability originates in a price set outside the country rather than in any domestic decision."),
 ("the overvaluation of currency and trade imbalances",
  "EK LEG-5.A.2.d names the overvaluation of currency and trade imbalances among the political and economic outcomes related to rentier state status."),
 ("the disparity between rich and poor increases",
  "EK LEG-5.A.2.e names the increasing disparity between rich and poor among the outcomes related to rentier state status."),
 ("cooperate with international judicial bodies",
  "EK LEG-5.A.2.f names a lack of incentive to modernize the economy or cooperate with international judicial bodies among the outcomes related to rentier state status."),
 ("not relying on citizens for taxes",
  "EK LEG-5.A.2.h names a lack of governmental accountability to citizens when not relying on citizens for taxes, which makes the framework's claim one about the direction of dependence rather than about a country's wealth."),
 ("increased governmental corruption, and the absence of democracy",
  "EK LEG-5.A.2.g names increased governmental corruption and EK LEG-5.A.2.i the absence of democracy among the outcomes related to rentier state status."),
 ("China, Iran, Mexico, Nigeria, and Russia",
  "EK LEG-5.A.3 states that resources are nationalized in China, Iran, Mexico, Nigeria, and Russia, which is five of the six course countries, and EK IEF-3.B.2 places the sixth at the end of the spectrum allowing the most private control of natural resources."),
 ("consolidate government control, and reduce the political influence of foreign governments",
  "EK LEG-5.A.3 names providing government revenue, consolidating government control, and reducing the political influence of foreign governments and multinational corporations as the purposes of nationalization, adding that all of them can reinforce political legitimacy."),
 ("allow private investment in its national oil company",
  "EK LEG-5.A.3.a gives the Mexican government's decision to allow private investment in Pemex as one of the ways the degree of central government control differs among the states that nationalize their resources."),
 ("that they exercise political control",
  "EK LEG-5.A.3.b names the political control exercised by foreign multinational corporations that underwrite Nigeria's oil production as one of the ways the degree of central government control differs."),
 ("wealth concentration",
  "EK LEG-5.A.3.c states that the high degree of centralized control over natural resource companies in Russia has resulted in wealth concentration."),
 ("decreased government control, increased wealth inequality, and the potential loss of sovereignty",
  "EK LEG-5.A.4 states that privatized ownership of natural resources decreases government control, increases wealth inequality, and results in the potential loss of sovereignty."),
 ("then lists nine adverse political and economic outcomes",
  "EK LEG-5.A.1 states the benefits and EK LEG-5.A.2 lists the outcomes often called the resource curse, while enduring understanding LEG-5 states that natural resource endowments can have positive and negative effects on political stability and economic development."),
 ("a lack of governmental accountability to citizens when not relying on citizens for taxes",
  "EK LEG-5.A.2.h states exactly the link the argument makes between the source of a government's revenue and its obligation to answer to the people it governs."),
 ("results in the potential loss of sovereignty",
  "EK LEG-5.A.4 states that privatized ownership of natural resources decreases government control, increases wealth inequality, and results in the potential loss of sovereignty, which is what the warning describes."),
 ("the smaller the share drawn from taxes on citizens",
  "EK LEG-5.A.2.h names a lack of governmental accountability to citizens when not relying on citizens for taxes. Recomputed in q21 above, which orders the rows by resource share and requires both other columns to move consistently, since the key asserts a joint movement across three columns."),
 ("53 points",
  "Recomputed in q22 above by subtracting the smallest responsiveness figure from the largest. The distractors are the other two gaps in that column and its two extreme values read as differences."),
 ("72 percentage points",
  "Recomputed in q23 above by subtracting the smallest resource share from the largest. The distractors are the other two gaps in that column and its two extreme values read as differences."),
 ("swinging far below the starting level in the last year",
  "EK LEG-5.A.2.c names severe revenue fluctuations based on world market pricing. Recomputed in q24 above, which tests the rise and the fall separately, since the key asserts that revenue and spending follow the price in both directions."),
 ("91 points",
  "Recomputed in q25 above by subtracting the smallest world price figure from the largest. The distractors are the two gaps against the starting year, the largest single figure read as a range, and the revenue column's range."),
 ("69 points",
  "Recomputed in q26 above by subtracting the smallest revenue figure from the largest. The distractors are the two gaps against the starting year, the largest single figure read as a range, and the price column's range."),
 ("private investors have been admitted to it",
  "EK LEG-5.A.3.a gives the decision to allow private investment in a national oil company as an instance of a lower degree of central control over a nationalized resource. Recomputed in q27 above, where one arrangement alone admits private investors while the state company remains."),
 ("foreign multinational corporations underwrite production and exercise political influence",
  "EK LEG-5.A.3.b names the political control exercised by foreign multinational corporations that underwrite Nigeria's oil production. Recomputed in q28 above, where one arrangement alone gives foreign corporations both roles."),
 ("high degree of centralized control, which the framework associates with wealth concentration",
  "EK LEG-5.A.3.c states that the high degree of centralized control over natural resource companies in Russia has resulted in wealth concentration, and EK LEG-5.A.3 introduces its three instances as showing that the degree of central government control differs. Recomputed in q29 above, which also confirms no other arrangement mentions wealth."),
 ("loosening its need to answer to taxpayers",
  "EK LEG-5.A.1 supplies the benefits, EK LEG-5.A.2 the nine adverse outcomes including the accountability claim, EK LEG-5.A.3 the purposes of nationalization and the differing degrees of control, and EK LEG-5.A.4 the effects of privatized ownership."),
]

cg.check(k5_9, CLAIMS,
         table_checks={21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29})
