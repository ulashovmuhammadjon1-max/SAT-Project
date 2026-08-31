"""Key audit for AP COMPARATIVE GOVERNMENT 5.1 Impact of Global Economic and
Technological Forces.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
Learning objective IEF-3.A, four essential knowledge statements:

  IEF-3.A.1  economic globalization = interconnected NETWORKS + a WORLDWIDE
             MARKET WITH ACTORS UNCONSTRAINED BY POLITICAL BORDERS + a REDUCTION
             IN STATE CONTROL OVER ECONOMIES; it has DEEPENED CROSS-NATIONAL
             CONNECTIONS AMONG WORKERS, GOODS AND CAPITAL and CAUSED CHALLENGES
             FOR REGIME AND CULTURAL STABILITY
  IEF-3.A.2  membership in the IMF, World Bank and WTO HAS PROMOTED ECONOMIC
             LIBERALIZATION POLICIES; .a China and Nigeria; .b Mexico's middle
             class has grown
  IEF-3.A.3  MNCs INCREASINGLY DOMINATE GLOBAL MARKETS and challenge domestic
             policy on LABOR, THE ENVIRONMENT, LAND RIGHTS, TAXATION and THE
             BUDGET
  IEF-3.A.4  globalization and neoliberalism PROVOKE CONFLICTS WITHIN STATES:
             .a civil society demands, .b protests, .c arrests and social media
             restrictions, .d empowerment of once-marginal, nationalist and
             populist groups

THE WORD THAT DECIDES ITEM 11 IS "WITHIN". IEF-3.A.4 locates these conflicts
inside states, and all four of its sub-items name domestic actors. A student who
reads globalization as a story about relations between governments will pick a
between-states option; the framework's own preposition rules it out.

THE FOUR SUB-ITEMS ARE A SEQUENCE, not a set: demands, then protest, then the
state's response to protest, then the rise of groups that blame the government.
Item 20 keys the sequence and the third table puts it on data -- which is why
item 27's check requires ALL FOUR columns to rise, not one.

THIS IS THE UNIT SOCIAL_BRIEF.MD WARNS ABOUT, because public policy and economic
conditions move with events and a fact true when written can be false when read.
The module therefore asserts NOTHING about a growth rate, an exchange rate, an
election result, or any current condition. The only country-specific claims in it
are the two the framework itself makes: IEF-3.A.2.a (China and Nigeria enacted
liberalization policies, and a majority of respondents in recent studies said
they expect children in their countries to be better off than their parents --
keyed at items 6 and 7 as a claim about survey EXPECTATIONS, which is what the
statement says, not about measured incomes) and IEF-3.A.2.b (Mexico's middle
class has grown, IN PART as a result of those policies -- item 8 keeps the
framework's own qualifier).

Every figure in every table is HYPOTHETICAL and labelled so. Item 21 asks which
ROWS match the framework's combination rather than naming a country, so no
survey number is attributed to any real state.

DATA ITEMS
----------
Items 21-23 read the survey table, 24-26 the dispute table, 27-29 the three-year
table. Every arithmetic distractor is verified to be a wrong operation on the
same table. Item 24's check also confirms the dispute table's five rows ARE the
framework's five policy areas, so the comparison cannot drift outside the
statement it tests.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k5_1

OPT = "Respondents expecting children to be better off than their parents (percent)"
LIB = "Economic liberalization policies enacted"

DISPUTES = "Disputes recorded between the government and multinational corporations (hypothetical)"

DEMANDS = "Demands submitted to the government by civil society groups"
PROTESTS = "Protest events led by students and other groups"
ARRESTS = "Protesters arrested"
DAYS = "Days on which social media services were restricted"


def _opt(table):
    return {lab: (cg.cell(table, lab, OPT), str(table["rows"][i][2]))
            for i, lab in enumerate(cg.labels(table))}


def q21(table, item):
    v = _opt(table)
    both = [lab for lab in v if v[lab][0] > 50 and v[lab][1].lower() == "yes"]
    assert both == ["Country 1", "Country 2"], f"the rows with a majority and a liberalization record are {both}"
    rest = [lab for lab in v if lab not in both]
    for lab in rest:
        assert v[lab][0] < 50 and v[lab][1].lower() == "no", \
            f"{lab} must fail both conditions, or 'the first two rows' would not be the only answer"
    assert len(v) == 4, "the table must have four rows, so 'all four' and 'the first and last' are testable"
    return (f"the survey column reads {[v[l][0] for l in v]} against liberalization records "
            f"{[v[l][1] for l in v]}, and exactly the first two rows meet both conditions")


def q22(table, item):
    o = cg.col(table, OPT)
    n = sum(1 for x in o if x > 50)
    assert n == 2, f"the count of rows above half recomputes to {n}"
    assert len(o) == 4, "the 4 distractor must be the number of rows in the table"
    assert sum(1 for x in o if x > 40) == 3, "the 3 distractor must come from including the row just under half"
    assert sum(1 for x in o if x > 60) == 1, "the 1 distractor must come from omitting one qualifying row"
    assert n > 0, "the 0 distractor must be false"
    return f"the survey column reads {o}, of which {n:.0f} exceed half"


def q23(table, item):
    o = cg.col(table, OPT)
    gap = max(o) - min(o)
    assert gap == 35, f"the keyed gap recomputes to {gap}"
    pairs = {abs(a - b) for a in o for b in o if a != b}
    for d in (23, 12, 6):
        assert d in pairs, f"the {d} distractor must be another gap in the same column; gaps are {sorted(pairs)}"
    assert max(o) == 64, "the 64 distractor must be the largest single figure read as a gap"
    return f"the survey column reads {o}, so the largest minus the smallest is {gap:.0f} percentage points"


def q24(table, item):
    areas = [a.lower() for a in cg.labels(table)]
    assert areas == ["labor", "the environment", "land rights", "taxation", "the budget"], \
        f"the rows must be the framework's five policy areas; they read {areas}"
    d = {lab: cg.cell(table, lab, DISPUTES) for lab in cg.labels(table)}
    top = max(d, key=d.get)
    assert top == "Taxation", f"the most disputed area is {top}"
    assert d["Taxation"] == 31, f"the keyed count reads {d['Taxation']}"
    stated = {"The environment": 22, "Labor": 14, "Land rights": 9, "The budget": 6}
    for lab, n in stated.items():
        assert d[lab] == n, f"the option for {lab} states {n} but the table gives {d[lab]}"
    return f"the five counts are {[d[l] for l in d]}, and each option states the true count for a different one of the framework's areas"


def q25(table, item):
    c = cg.col(table, DISPUTES)
    total = sum(c)
    assert total == 82, f"the keyed total recomputes to {total}"
    assert total - min(c) == 76, "the 76 distractor must be the total with the smallest row omitted"
    assert sum(sorted(c)[-3:]) == 67, "the 67 distractor must be the three largest rows added"
    assert total - max(c) == 51, "the 51 distractor must be the total with the largest row omitted"
    assert max(c) == 31, "the 31 distractor must be the largest single row"
    return f"the dispute column reads {c} and sums to {total:.0f}, with every distractor a wrong sum of the same column"


def q26(table, item):
    c = cg.col(table, DISPUTES)
    diff = max(c) - min(c)
    assert diff == 25, f"the keyed difference recomputes to {diff}"
    assert 22 in c and 9 in c, f"the 22 and 9 distractors must be rows of the same column; it reads {c}"
    assert max(c) - 14 == 17, "the 17 distractor must be another gap within the same column"
    assert max(c) + min(c) == 37, "the 37 distractor must be the two extreme rows added instead of subtracted"
    return f"the dispute column reads {c}, so the largest minus the smallest is {diff:.0f}"


def q27(table, item):
    cols = {h: cg.col(table, h) for h in (DEMANDS, PROTESTS, ARRESTS, DAYS)}
    for h, c in cols.items():
        assert c == sorted(c), f"the column {h!r} must rise across the three years; it reads {c}"
        assert len(set(c)) == 3, f"the column {h!r} must change in every year, or 'none changed' is defensible"
    assert min(cols[DAYS]) == 0, \
        "the first year must record no restricted days, so 'restrictions in every year' is false"
    return "all four columns rise across the three years: " + "; ".join(
        f"{h.split(' ')[0].lower()} {c}" for h, c in cols.items())


def q28(table, item):
    a = cg.col(table, ARRESTS)
    rise = a[2] - a[0]
    assert rise == 930, f"the keyed increase recomputes to {rise}"
    assert a[2] - a[1] == 580, "the 580 distractor must be the increase between the second and third years"
    assert a[1] - a[0] == 350, "the 350 distractor must be the increase between the first and second years"
    assert a[2] == 990, "the 990 distractor must be the third year's own figure"
    assert a[0] + a[2] == 1050, "the 1050 distractor must be the first and third years added instead of subtracted"
    return f"the arrest column reads {a}, so the rise from the first year to the third is {rise:.0f}"


def q29(table, item):
    d, p = cg.col(table, DAYS), cg.col(table, PROTESTS)
    total = sum(d)
    assert total == 27, f"the keyed total recomputes to {total}"
    assert max(d) == 21, "the 21 distractor must be the largest single year"
    assert sorted(d)[1] == 6, "the 6 distractor must be the middle year"
    assert total + max(d) == 48, "the 48 distractor must be the total with its largest year counted twice"
    assert sum(p) == 125, "the 125 distractor must be a different column's total"
    return f"the restriction column reads {d} and sums to {total:.0f} days"


CLAIMS = [
 ("a reduction in state control over economies",
  "EK IEF-3.A.1 names economic networks growing more interconnected, a worldwide market with actors unconstrained by political borders, and a reduction in state control over economies as what economic globalization includes. Each rejected set either runs the opposite way or belongs to another unit."),
 ("cross-national connections among workers, goods, and capital",
  "EK IEF-3.A.1 states that economic globalization has deepened cross-national connections among workers, goods, and capital, so what it connects is people, products and money rather than institutions."),
 ("challenges for regime and cultural stability",
  "EK IEF-3.A.1 states that economic globalization has caused challenges for regime and cultural stability, which extends the framework's concern past economic measures to whether a regime holds and how a culture changes."),
 ("the International Monetary Fund, the World Bank, and the World Trade Organization",
  "EK IEF-3.A.2 names state membership in the International Monetary Fund, the World Bank, and the World Trade Organization as having promoted economic liberalization policies. The bodies in the rejected sets are the supranational organizations of EK LEG-3.A.3 or organizations the framework does not treat here."),
 ("economic liberalization policies",
  "EK IEF-3.A.2 states that membership in those three organizations has promoted economic liberalization policies, which is a claim about the direction in which membership pushes a member's policy."),
 ("China and Nigeria",
  "EK IEF-3.A.2.a names China and Nigeria as having enacted economic liberalization policies, alongside its finding that a majority of respondents in recent studies expect children in their countries to be better off than their parents."),
 ("expect children in their countries to be better off than their parents",
  "EK IEF-3.A.2.a records what a majority of respondents in recent studies said, so the statement is about reported expectations for the next generation rather than about any measured economic outcome."),
 ("the number of people in the middle class has grown",
  "EK IEF-3.A.2.b states that in Mexico, in part as a result of these policies, the number of people in the middle class has grown, and the qualifier in part belongs to the framework rather than being added here."),
 ("they increasingly dominate global markets",
  "EK IEF-3.A.3 states that multinational corporations increasingly dominate global markets and pose challenges to, and sometimes conflict with, domestic economic policies."),
 ("labor, the environment, land rights, taxation, and the budget",
  "EK IEF-3.A.3 names domestic economic policies regarding labor, the environment, land rights, taxation, and the budget as the areas multinational corporations challenge and sometimes conflict with."),
 ("within states",
  "EK IEF-3.A.4 states that globalization and neoliberalism can provoke conflicts within states, and each of its four sub-items names a domestic actor, so the conflicts are located inside a country rather than between governments."),
 ("increased demands being placed on governments by civil society groups",
  "EK IEF-3.A.4.a names increased demands being placed on governments by civil society groups among the conflicts globalization and neoliberalism can provoke within states."),
 ("arrests of protesters and imposition of social media restrictions",
  "EK IEF-3.A.4.c pairs arrests of protesters with the imposition of social media restrictions in a single item, so the framework treats the physical response and the informational one as one kind of conflict."),
 ("once-marginal, nationalist, and populist groups",
  "EK IEF-3.A.4.d names the empowerment of once-marginal, nationalist, and populist groups that blame the government for changes in culture and economic conditions, joining a cultural grievance to an economic one in a single item."),
 ("a reduction in state control over economies",
  "EK IEF-3.A.1 lists a reduction in state control over economies among the three components of economic globalization, and it is the component stated in terms of what a government can and cannot do rather than in terms of flows or networks."),
 ("actors unconstrained by political borders",
  "EK IEF-3.A.1 names a worldwide market with actors unconstrained by political borders among the features of economic globalization, and firms answering to no single jurisdiction while moving funds faster than regulators can respond is that feature in operation."),
 ("regarding taxation and the budget",
  "EK IEF-3.A.3 names taxation and the budget among the domestic economic policy areas that multinational corporations pose challenges to and sometimes conflict with, which is exactly the dispute described."),
 ("arrests of protesters and imposition of social media restrictions",
  "EK IEF-3.A.4.c names arrests of protesters and imposition of social media restrictions as a single item, and the scenario contains both halves, which is why it matches that item rather than the protest item or the civil society item."),
 ("blaming the government for changes in culture as well as in economic conditions",
  "EK IEF-3.A.1 states that economic globalization has caused challenges for regime and cultural stability, and EK IEF-3.A.4.d gives the political form of that, since the groups it names blame the government for changes in culture and in economic conditions together."),
 ("the state responds by arresting protesters and restricting communications",
  "EK IEF-3.A.4 lists increased civil society demands, then protests by students and disenfranchised groups, then arrests of protesters together with social media restrictions, then the empowerment of groups that blame the government, in that order."),
 ("the first two rows",
  "EK IEF-3.A.2.a states that China and Nigeria have enacted economic liberalization policies and that a majority of respondents expect children in their countries to be better off than their parents, so a matching row needs both conditions. Recomputed in q21 above, which also confirms no other row meets either one."),
 ("2",
  "Recomputed in q22 above by counting the rows whose survey figure exceeds half. The distractors are the number of rows in the table, a count that admits the row just under half, a count that drops a qualifying row, and a claim that none qualifies."),
 ("35 percentage points",
  "Recomputed in q23 above by subtracting the smallest survey figure from the largest. The distractors are other gaps in the same column and the largest single figure read as though it were a gap."),
 ("taxation, with 31 disputes",
  "EK IEF-3.A.3 names labor, the environment, land rights, taxation and the budget as the policy areas multinational corporations challenge. Recomputed in q24 above, which also confirms the table's five rows are exactly those five areas and that each option states its own row's true count."),
 ("82",
  "Recomputed in q25 above by summing the dispute column across the five areas. The distractors are the total with the smallest row omitted, the three largest rows added, the total with the largest row omitted, and the largest single row."),
 ("25",
  "Recomputed in q26 above by subtracting the smallest row from the largest. The distractors are two of the rows themselves, another gap within the column, and the two extreme rows added instead of subtracted."),
 ("all rose together across the three years",
  "EK IEF-3.A.4 lists civil society demands, protests, arrests together with social media restrictions, and the empowerment of groups that blame the government as conflicts globalization can provoke within states. Recomputed in q27 above, where each of the four columns is tested separately, since the key asserts four simultaneous movements."),
 ("930",
  "Recomputed in q28 above by subtracting the first year's arrest figure from the third year's. The distractors are the increases across the other pairs of years, the third year's own figure, and the first and third years added instead of subtracted."),
 ("27",
  "Recomputed in q29 above by summing the restriction column across the three years. The distractors are the largest single year, the middle year, the total with its largest year counted twice, and a different column's total."),
 ("the resulting strains show up inside states",
  "EK IEF-3.A.1 supplies the description of globalization and its challenges to regime and cultural stability, EK IEF-3.A.2 the push toward liberalization from membership in international financial organizations, EK IEF-3.A.3 the contest between multinational corporations and domestic economic policy, and EK IEF-3.A.4 the four conflicts within states."),
]

cg.check(k5_1, CLAIMS,
         table_checks={21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29})
