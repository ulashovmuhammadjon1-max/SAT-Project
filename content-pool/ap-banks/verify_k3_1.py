"""Key audit for AP COMPARATIVE GOVERNMENT 3.1 Civil Society.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
  IEF-1.A.1  civil society is a range of VOLUNTARY ASSOCIATIONS AUTONOMOUS FROM THE
             STATE, including local religious and neighborhood organizations, news
             media, business and professional associations, and NGOs
  IEF-1.A.2  their STRENGTH AND VARIETY differs with REGIME TYPE, and they can be
             LIMITED BY GOVERNMENT REGISTRATION AND MONITORING POLICIES
  IEF-1.B.1  though NOT NECESSARILY POLITICAL, a ROBUST civil society serves as an
             AGENT OF DEMOCRATIZATION
  IEF-1.B.2  across the course countries these organizations can, TO VARYING
             DEGREES, monitor and lobby the government, expose governmental
             malfeasance, represent the interests of members, and provide members
             with organizational experience
  IEF-1.B.3  restrictions on NGOs and civil society TEND TO HIGHLIGHT VIOLATIONS OF
             CIVIL LIBERTIES protected under foundational documents

Supporting: LEG-1.C.3 (reform pressure from civil society producing institutions),
DEM-1.C.2 and DEM-1.C.3.c (media constraints and state ownership of broadcasting),
PAU-1.C.1 (what democratization aims at), PAU-4.A.1-2 (what parties are for).

THE PROPERTY EVERY BORDERLINE ITEM TURNS ON
-------------------------------------------
Autonomy from the state is what makes an association part of civil society. A
ministry, a state-owned broadcaster and a governing party's own organization are
therefore outside it however many members they have -- items 2, 4, 19, 27 and 29
all turn on that rather than on size, registration or funding.

THE HALF OF IEF-1.B.1 STUDENTS DROP
-----------------------------------
The sentence begins 'though civil society organizations are NOT NECESSARILY
POLITICAL' and only then calls a robust civil society an agent of democratization.
Item 8 keys the first clause and item 29 applies it, because a reader who keeps
only the democratization claim will exclude every apolitical association from the
category the framework puts them in.

DATA ITEMS
----------
Items 20-22 use a hypothetical table whose three columns are exactly IEF-1.A.2's
constraint mechanisms plus the count they constrain. Items 23-25 use a sample
whose four row labels are IEF-1.A.1's four named kinds of association, so item 25
can key that all four belong to civil society while their monitoring rates differ
-- IEF-1.B.2's 'to varying degrees' in data. Item 23 asks for a SHARE where the
largest raw count belongs to a different row.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k3_1

NGO = "Registered nongovernmental organizations per 100,000 people"
MON = "Share of such organizations reporting government monitoring of their finances (percent)"
REF = "Applications for registration refused in the past year (percent)"
NORG = "Number of organizations"
PUB = "Number that published a report on government spending in the past year"


def _cs(table):
    return {lab: (cg.cell(table, lab, NGO), cg.cell(table, lab, MON), cg.cell(table, lab, REF))
            for lab in cg.labels(table)}


def q20(table, item):
    v = _cs(table)
    n, m, r = v["Country 2"]
    assert n == min(x[0] for x in v.values()), "the keyed row must have the fewest organizations"
    assert m == max(x[1] for x in v.values()), "the keyed row must report the most monitoring"
    assert r == max(x[2] for x in v.values()), "the keyed row must refuse the most registrations"
    assert all(x[2] > 0 for x in v.values()), \
        "every row refuses some registrations, which is what makes the 'all three equally' option tempting"
    return "one row is worst on all three columns at once: fewest organizations, most monitoring, most refusals"


def q21(table, item):
    v = _cs(table)
    n, m, r = v["Country 1"]
    assert n == max(x[0] for x in v.values()), "the keyed row must have the most organizations"
    assert m == min(x[1] for x in v.values()) and r == min(x[2] for x in v.values()), \
        "the keyed row must be lowest on both constraint columns"
    mid = v["Country 3"]
    assert min(x[0] for x in v.values()) < mid[0] < n, "the rejected middle row must genuinely lie between the others"
    return "one row leads on the count of organizations and is lowest on both of the framework's constraint measures"


def q22(table, item):
    col = cg.col(table, NGO)
    total = sum(col)
    assert total == 134, f"the keyed total recomputes to {total}"
    assert total - min(col) == 125 and sorted(col)[0] + sorted(col)[1] == 50, \
        "the 125 and 50 distractors must be partial sums of the same column"
    assert max(col) == 84, "the 84 distractor must be the largest single row"
    assert 84 + 9 == 93, "the 93 distractor must be another two-row partial sum"
    return f"the organization column reads {col} and sums to {total:.0f}, with every distractor a partial sum or a single row"


def _act(table):
    return {str(r[0]): (cg.cell(table, r[0], NORG), cg.cell(table, r[0], PUB)) for r in table["rows"]}


def q23(table, item):
    v = _act(table)
    share = {lab: p / n for lab, (n, p) in v.items()}
    top = max(share, key=share.get)
    assert top.startswith("News media"), f"the largest share belongs to {top}"
    assert v[top] == (95, 71), f"the keyed 71 of 95 reads as {v[top]}"
    biggest_count = max(v, key=lambda k: v[k][1])
    assert biggest_count != top, \
        "the largest raw count must belong to a DIFFERENT row, or the item would not test proportion against count"
    return f"the four shares are {[round(share[l], 2) for l in v]}, and the largest raw count belongs to another row"


def q24(table, item):
    col = [n for n, _ in _act(table).values()]
    total = sum(col)
    assert total == 945, f"the keyed total recomputes to {total}"
    pub = [p for _, p in _act(table).values()]
    assert sum(pub) == 283, "the 283 distractor must be the other column's total"
    assert total - max(col) == 535, "the 535 distractor must be the total less the largest row"
    assert max(col) == 410, "the 410 distractor must be the largest single row"
    assert 410 + 260 == 670, "the 670 distractor must be a two-row partial sum"
    return f"the organization column reads {col} and sums to {total:.0f}; each distractor is another column, a partial sum, or one row"


def q25(table, item):
    v = _act(table)
    named = ("religious and neighborhood", "business and professional", "news media", "nongovernmental")
    labels = " | ".join(v).lower()
    for phrase in named:
        assert phrase in labels, f"the table must include EK IEF-1.A.1's {phrase!r} category; rows are {list(v)}"
    assert all(p > 0 for _, p in v.values()), "'no type performed any monitoring' must be false"
    assert all(p < n for n, p in v.values()), "'every organization published a report' must be false"
    share = {lab: p / n for lab, (n, p) in v.items()}
    assert max(share.values()) > 20 * min(share.values()), \
        "the rates must differ widely enough for 'very different rates' to be the right reading"
    return "all four of the framework's named kinds of association appear, each published something, and the rates differ more than twentyfold"


CLAIMS = [
 ("voluntary associations that are autonomous from the state",
  "EK IEF-1.A.1 defines civil society as a range of voluntary associations that are autonomous from the state. The rejected options describe EK PAU-1.A.4's government, party systems, executive agencies and the electorate, none of which has that autonomy."),
 ("being autonomous from the state",
  "EK IEF-1.A.1 makes autonomy from the state definitive and EK IEF-1.B.1 adds that such organizations are not necessarily political. Registration, size and funding bear on how a civil society organization operates, not on whether it is one."),
 ("local religious and neighborhood organizations",
  "EK IEF-1.A.1 names local religious and neighborhood organizations, news media, business and professional associations, and nongovernmental organizations as its examples. Ministries, commissions, courts and foreign bodies are not voluntary associations autonomous from the state."),
 ("ministry of information",
  "EK IEF-1.A.1 requires voluntary associations AUTONOMOUS FROM THE STATE, and a ministry running a state broadcaster is part of the state. The other four options are among the kinds of association the same statement names."),
 ("differs depending on the regime type",
  "EK IEF-1.A.2 states that the strength and variety of civil society organizations differs depending on the regime type in which they operate, a difference of degree rather than of presence, matching EK DEM-1.C.2 and EK DEM-1.B.3."),
 ("registration and monitoring policies",
  "EK IEF-1.A.2 states that civil society organizations can be limited by government registration and monitoring policies. Registration decides who may exist and monitoring what they may do unobserved, which is why the framework names both."),
 ("agent of democratization",
  "EK IEF-1.B.1 states that though civil society organizations are not necessarily political, a robust civil society serves as an agent of democratization, and EK PAU-1.C.1 defines democratization as a transition from an authoritarian to a democratic regime."),
 ("not necessarily political",
  "EK IEF-1.B.1 opens with this qualification before making its democratization claim. A choir, a trade association or a neighborhood group belongs to civil society without any political programme, which is what the clause protects."),
 ("providing members with organizational experience",
  "EK IEF-1.B.2 names monitoring and lobbying the government, exposing governmental malfeasance, representing the interests of members, and providing members with organizational experience, adding that these are performed TO VARYING DEGREES. Nominating candidates and forming governments belong to parties."),
 ("monitoring and lobbying the government",
  "EK IEF-1.B.2 names monitoring and lobbying the government among the functions civil society organizations can perform. Analysis is the monitoring half and argument to ministers the lobbying half."),
 ("exposing governmental malfeasance",
  "EK IEF-1.B.2 names exposing governmental malfeasance among the functions of civil society organizations, and EK LEG-1.C.3 describes reform pressure from civil society producing institutions that limit corruption."),
 ("representing the interests of members",
  "EK IEF-1.B.2 names representing the interests of members among the functions of civil society organizations, and EK IEF-1.A.1 lists business and professional associations among the bodies that make up civil society."),
 ("providing members with organizational experience",
  "EK IEF-1.B.2 names providing members with organizational experience among the functions of civil society organizations, and EK IEF-1.B.1's democratization claim rests partly on skills of this kind spreading beyond the association."),
 ("to varying degrees",
  "EK IEF-1.B.2 states that across the course countries these functions can be performed to varying degrees, and EK IEF-1.A.2's point that strength and variety differ by regime type is why the qualification is there."),
 ("highlight violations of civil liberties",
  "EK IEF-1.B.3 states that across course countries, the placing of restrictions on NGOs and civil society tends to highlight violations of civil liberties protected under foundational documents. The restriction draws attention to the protection it cuts against."),
 ("internal reform pressure from citizen protest groups",
  "EK LEG-1.C.3 states that reform pressure from citizen protest groups and civil society can lead to new institutions or policies protecting civil liberties, improving transparency, addressing election fairness and media bias, limiting corruption and ensuring equality under law. Civil society applies the pressure; the state creates the institution."),
 ("their strength and variety differ with regime type",
  "EK IEF-1.A.2 states that the strength and variety of civil society organizations differs depending on regime type and that they can be limited by registration and monitoring policies, which is a difference of degree rather than of presence."),
 ("limited by government registration and monitoring policies",
  "EK IEF-1.A.2 names registration and monitoring policies as the means by which civil society organizations can be limited, and the scenario describes both. EK IEF-1.B.3 adds that such restrictions tend to highlight violations of civil liberties."),
 ("the independently owned newspaper",
  "EK IEF-1.A.1 names news media among the components of civil society but defines the category by autonomy from the state, which an outlet the state owns does not have. EK DEM-1.C.3.c describes nationalization of most broadcast media as a way of tightening political control."),
 ("highest share of registrations refused",
  "EK IEF-1.A.2 names registration and monitoring policies as the constraints on civil society, and the table's columns report the count of organizations, the extent of monitoring and refusals of registration. Recomputed in q20 above: one row is worst on all three."),
 ("least financial monitoring",
  "EK IEF-1.B.1 speaks of a ROBUST civil society and EK IEF-1.A.2 makes registration and monitoring the constraints on it. Recomputed in q21 above: one row leads on the count of organizations and is lowest on both constraints."),
 ("134",
  "Recomputed in q22 above by summing the organizations column. Every distractor is a partial sum of that same column or its largest single row."),
 ("71 of 95",
  "EK IEF-1.B.2 names monitoring the government among the functions of civil society organizations, and the question asks for a proportion. Recomputed in q23 above: the largest share and the largest raw count belong to different rows."),
 ("945",
  "Recomputed in q24 above by summing the organization counts across all four rows. The distractors are the other column's total, the total less a row, a two-row partial sum, and the largest single row."),
 ("at very different rates",
  "EK IEF-1.A.1 names all four of the table's row categories as components of civil society and EK IEF-1.B.2 says the functions are performed to varying degrees. Recomputed in q25 above: every row published something and the rates differ more than twentyfold."),
 ("are not necessarily political, whereas parties exist to contest elections",
  "EK IEF-1.A.1 defines civil society by voluntary association and autonomy from the state, EK IEF-1.B.1 adds that such organizations are not necessarily political, and EK PAU-4.A.1 and EK PAU-4.A.2 describe party systems in terms of controlling governing power. EK PAU-4.A.2 also shows parties existing under an authoritarian regime."),
 ("without needing the state's approval",
  "EK IEF-1.A.1 requires autonomy from the state, EK IEF-1.A.2 names registration and monitoring as the limits on it, and EK IEF-1.B.2 lists monitoring, exposure and representation among the functions. Every rejected finding describes bodies created, funded, staffed or owned by the state or the governing party."),
 ("highlight violations of civil liberties protected under foundational documents",
  "EK IEF-1.B.3 states that restrictions on NGOs and civil society tend to highlight violations of civil liberties protected under foundational documents. The other statements are true of the framework but do not explain why a restriction draws attention to itself."),
 ("rather than by political purpose",
  "EK IEF-1.A.1 names business and professional associations among the components of civil society and defines the category by voluntary association and autonomy from the state, while EK IEF-1.B.1 states that civil society organizations are not necessarily political."),
 ("four named functions to varying degrees",
  "EK IEF-1.A.1 supplies the definition and examples, EK IEF-1.A.2 the variation by regime type and the registration and monitoring limits, EK IEF-1.B.1 the not-necessarily-political qualification and the democratization claim, and EK IEF-1.B.2 the four functions performed to varying degrees."),
]

cg.check(k3_1, CLAIMS, table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25})
