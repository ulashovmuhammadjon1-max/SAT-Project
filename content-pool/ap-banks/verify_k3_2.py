"""Key audit for AP COMPARATIVE GOVERNMENT 3.2 Political Culture.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
  IEF-1.C.1  political culture is the COLLECTIVE ATTITUDES, VALUES AND BELIEFS of
             the citizenry and the NORMS OF BEHAVIOR in the political system, and
             it sets expectations about the exercise of power to establish a
             BALANCE BETWEEN SOCIAL ORDER AND INDIVIDUAL LIBERTY
  IEF-1.C.2  it is influenced by GEOGRAPHY, RELIGIOUS TRADITIONS and HISTORY, and
             forms beliefs about the ROLE OF GOVERNMENT, the RIGHTS OF THE
             INDIVIDUAL, and the EXTENT AND ROLE OF CITIZENS IN CONTROLLING
             GOVERNMENT POLICY MAKING
  IEF-1.C.3  it is transmitted through POLITICAL SOCIALIZATION, the LIFELONG process
             of acquiring one's beliefs, values and orientations
  IEF-1.C.4  FAMILY, SCHOOLS, PEERS, RELIGIOUS INSTITUTIONS, MEDIA and SOCIAL
             ENVIRONMENTS INCLUDING CIVIC ORGANIZATIONS are the agents
  IEF-1.C.5  many agents are SIMILAR ACROSS REGIME TYPES; AUTHORITARIAN REGIMES
             APPLY MORE CONCERTED GOVERNMENTAL PRESSURES around conforming beliefs

THE DIFFERENCE-OF-DEGREE CLAIM, AGAIN
-------------------------------------
IEF-1.C.5 belongs to the same family as DEM-1.C.2 on media and DEM-1.B.3 on
participation: the AGENTS are similar in both regime types and the GOVERNMENTAL
PRESSURE differs. The intuitive reading -- that socialization is something only
authoritarian regimes do -- is not the framework's, and items 13, 15 and 25 key
that. Item 25 is the sharpest: a survey of which agent people NAME does not
measure how much pressure a government APPLIES, so the data cannot settle the
question EK IEF-1.C.5 answers.

Supporting statements: LEG-1.A.2 (tradition and ideology among the sources of
legitimacy), IEF-1.C.6 (ideology, for the contrast in item 16), IEF-1.A.1 (news
media and neighborhood organizations as civil society), MPA-1.A.3.

DATA ITEMS
----------
Items 20-22 use a hypothetical table whose first two columns are the two ends of
IEF-1.C.1's balance, so the framework's own axis can be read off it. Items 23-25
use a survey whose five rows are exactly IEF-1.C.4's named agents, both columns
summing to 100, which lets item 24 key that the same agents appear in both
countries in different proportions.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k3_2

ORDER = "Share agreeing that maintaining order should take priority over individual liberty (percent)"
SAY = "Share agreeing that citizens should have a say in policy between elections (percent)"
FAM = "Share saying they learned their political views mainly from family (percent)"
CD = "Share naming it as their main influence in Country D (percent)"
CE = "Share naming it as their main influence in Country E (percent)"


def _ord(table):
    return {lab: (cg.cell(table, lab, ORDER), cg.cell(table, lab, SAY), cg.cell(table, lab, FAM))
            for lab in cg.labels(table)}


def q20(table, item):
    v = _ord(table)
    o, s, _ = v["Country A"]
    assert o == max(x[0] for x in v.values()) == 71, "the keyed row must hold the highest order share"
    assert s == min(x[1] for x in v.values()) == 28, "the keyed row must hold the lowest expectation of a say"
    assert o > 50 and s < 50, "the keyed row must sit clearly at the order end on both columns"
    return "one row pairs the highest order-over-liberty share, 71, with the lowest expectation of a say between elections, 28"


def q21(table, item):
    v = _ord(table)
    o, s, _ = v["Country B"]
    assert o == min(x[0] for x in v.values()), "the keyed row must hold the lowest order share"
    assert s == max(x[1] for x in v.values()), "the keyed row must hold the highest expectation of a say"
    mid = v["Country C"]
    assert abs(mid[0] - mid[1]) < abs(o - s), "the rejected middle row's two figures must indeed be closest together"
    return "one row is lowest on order and highest on expected influence at once, which is the opposite corner of the same axis"


def q22(table, item):
    col = cg.col(table, ORDER)
    gap = max(col) - min(col)
    assert gap == 37, f"the keyed gap recomputes to {gap}"
    assert max(col) - sorted(col)[1] == 19 and sorted(col)[1] - min(col) == 18, \
        "the 19 and 18 distractors must be the other pairwise gaps in the same column"
    say = cg.col(table, SAY)
    assert max(say) - min(say) == 41, "the 41 distractor must be the corresponding gap in the other column"
    assert max(col) == 71, "the 71 distractor must be the largest single value read as a difference"
    return f"the order column spans {min(col):.0f} to {max(col):.0f}, a gap of {gap:.0f}, with every distractor a real figure from the wrong pair or column"


def _agent(table):
    return {str(r[0]): (cg.cell(table, r[0], CD), cg.cell(table, r[0], CE)) for r in table["rows"]}


def q23(table, item):
    v = _agent(table)
    diff = {lab: abs(d - e) for lab, (d, e) in v.items()}
    assert max(diff, key=diff.get) == "Schools", f"the largest difference belongs to {max(diff, key=diff.get)}"
    stated = {"Schools": 16, "Family": 7, "Religious institutions": 8, "Peers": 4, "Media": 3}
    for lab, n in stated.items():
        assert diff[lab] == n, f"the option for {lab} states {n} but the table gives {diff[lab]}"
    return f"the five differences recompute to {sorted(diff.values(), reverse=True)}, and each option states a true difference for a different row"


def q24(table, item):
    v = _agent(table)
    assert sum(d for d, _ in v.values()) == 100 and sum(e for _, e in v.values()) == 100, \
        "both columns must sum to 100, or 'in different proportions' is not a fair reading"
    assert all(d > 0 and e > 0 for d, e in v.values()), \
        "every agent must appear in BOTH columns, which is what 'the same set of agents' asserts"
    named = ("family", "schools", "peers", "religious institutions", "media")
    labels = [lab.lower() for lab in v]
    for phrase in named:
        assert phrase in labels, f"the table must carry EK IEF-1.C.4's {phrase!r} row; rows are {list(v)}"
    assert any(d != e for d, e in v.values()), "'every respondent named the same agent' must be false"
    return "both columns sum to 100 over the same five agents, all of them on the framework's list, with different proportions in each"


def q25(table, item):
    v = _agent(table)
    d, e = v["Schools"]
    assert e > d, "the student's premise requires the second column to name schools more often"
    headers = " ".join(table["headers"]).lower()
    assert "naming it as their main influence" in headers, \
        "the objection turns on the columns measuring which agent is NAMED, not how much pressure is applied"
    assert "pressure" not in headers, "no column may measure governmental pressure, or the objection would fail"
    return "the second column does name schools more often, and no column in the table measures governmental pressure at all"


CLAIMS = [
 ("collective attitudes, values and beliefs of the citizenry",
  "EK IEF-1.C.1 defines political culture as the collective attitudes, values and beliefs of the citizenry and the norms of behavior in the political system. The rejected options describe EK PAU-1.A.4's government, EK PAU-1.A.2's regime, EK IEF-1.C.6's political ideology and a measure of behavior."),
 ("balance between social order and individual liberty",
  "EK IEF-1.C.1 states that political culture sets expectations about the exercise of power to establish a balance between social order and individual liberty, which is the tension enduring understanding IEF-1 names in its own wording."),
 ("geography, religious traditions and history",
  "EK IEF-1.C.2 names factors of geography, religious traditions and history as the influences on political culture. Institutional and economic features appear elsewhere in the framework and not under this heading."),
 ("extent and role of citizens in controlling government policy making",
  "EK IEF-1.C.2 states that these influences form a population's values and beliefs about the role of government, the rights of the individual, and the extent and role of citizens in controlling government policy making. All three are beliefs rather than institutions."),
 ("lifelong process of acquiring one's beliefs",
  "EK IEF-1.C.3 defines political socialization as the lifelong process of acquiring one's beliefs, values and orientations toward the political system, and states that political culture is transmitted through it."),
 ("lasts a lifetime rather than ending in childhood",
  "EK IEF-1.C.3 calls socialization the LIFELONG process, and EK IEF-1.C.4 names agents that operate at different stages of life. Confining it to childhood or to formal schooling contradicts both statements."),
 ("social environments including civic organizations",
  "EK IEF-1.C.4 names family, schools, peers, religious institutions, media and social environments including civic organizations as playing a crucial role in socialization. State institutions and foreign bodies are not on that list."),
 ("family",
  "EK IEF-1.C.4 names family first among the agents that play a crucial role in socialization, and EK IEF-1.C.3's lifelong framing is why the process does not end when a child leaves home."),
 ("schools",
  "EK IEF-1.C.4 names schools among the agents of socialization, and EK IEF-1.C.5 adds that authoritarian regimes apply more concerted governmental pressures around conforming beliefs, of which a mandated curriculum is one possible instrument."),
 ("peers",
  "EK IEF-1.C.4 names peers among the agents that play a crucial role in socialization, and EK IEF-1.C.3's lifelong framing is why an adult's views can still move under such influence."),
 ("religious institutions",
  "EK IEF-1.C.4 names religious institutions among the agents of socialization and EK IEF-1.C.2 names religious traditions among the influences on political culture, so the two statements reach the same source from different angles."),
 ("media and social environments including civic organizations",
  "EK IEF-1.C.4 names media and social environments including civic organizations among the agents of socialization, and EK IEF-1.A.1 places news media and neighborhood organizations within civil society, autonomous from the state."),
 ("similar across regime types",
  "EK IEF-1.C.5 states that many agents of socialization are similar across regime types before drawing its difference about governmental pressure. The difference it draws is not about which agents exist."),
 ("authoritarian regimes apply more concerted governmental pressures",
  "EK IEF-1.C.5 states that authoritarian regimes apply more concerted governmental pressures to socialize their citizens around conforming beliefs than do democratic regimes, while the agents themselves are largely similar. The difference is one of degree in the pressure applied."),
 ("how concerted the governmental pressure is",
  "EK IEF-1.C.5 states that many agents of socialization are similar across regime types before drawing its difference, and EK IEF-1.C.3 makes socialization the means by which ANY political culture is transmitted. This follows the pattern of EK DEM-1.C.2 and EK DEM-1.B.3."),
 ("whereas a political ideology is a set of values and beliefs about the goals of government",
  "EK IEF-1.C.1 defines political culture as the collective attitudes, values and beliefs of a citizenry and the norms of its political system, while EK IEF-1.C.6 defines a political ideology as a set of values and beliefs about the goals of government, public policy or politics. One describes a population, the other a programme."),
 ("broader than a view on one question",
  "EK IEF-1.C.1 defines political culture as collective attitudes, values and beliefs together with norms of behavior, and EK IEF-1.C.2 has it forming views about the role of government, individual rights and citizens' part in policy making. A single issue reaches none of that breadth."),
 ("geography",
  "EK IEF-1.C.2 names geography among the factors influencing political culture, alongside religious traditions and history. Institutional design appears elsewhere in the framework and is not among these three."),
 ("religious traditions",
  "EK IEF-1.C.2 names religious traditions among the factors influencing political culture, and EK IEF-1.C.4 separately names religious institutions among the agents through which political culture is transmitted."),
 ("only 28 percent expect a say",
  "EK IEF-1.C.1 makes the balance between social order and individual liberty what political culture sets expectations about. Recomputed in q20 above: one row pairs the highest order share with the lowest expectation of a say between elections."),
 ("lowest share giving order priority",
  "EK IEF-1.C.1 supplies the axis and EK IEF-1.C.2 includes the extent and role of citizens in controlling policy making among the beliefs political culture forms. Recomputed in q21 above: one row sits at the opposite corner of the same axis."),
 ("37 percentage points",
  "Recomputed in q22 above by subtracting the smallest figure in the order column from the largest. Every distractor is a real figure from another pair of rows, the other column, or a single value read as a difference."),
 ("schools, by 16 percentage points",
  "EK IEF-1.C.4 names all five of the table's rows among the agents of socialization, so this is a comparison inside the framework's own list. Recomputed in q23 above: each alternative states the true difference for a different row."),
 ("the same set of agents, all of which the framework lists",
  "EK IEF-1.C.5 states that many agents of socialization are similar across regime types, and every row of the table is one of EK IEF-1.C.4's agents. Recomputed in q24 above: both columns sum to 100 over the same five rows and no cell is zero."),
 ("does not establish it",
  "EK IEF-1.C.5's claim is about the CONCERTEDNESS OF GOVERNMENTAL PRESSURE, which a survey of named influences does not measure, and EK MPA-1.A.3 denies that causation can be isolated with certainty from such evidence. Recomputed in q25 above: the premise is a correct reading and no column measures pressure."),
 ("history",
  "EK IEF-1.C.2 names history among the factors influencing political culture, alongside geography and religious traditions, and says these form beliefs about the role of government, individual rights and citizens' part in policy making."),
 ("Across a generation",
  "EK IEF-1.C.1 makes political culture the collective attitudes, values and beliefs of a citizenry, EK IEF-1.C.2 makes beliefs about government and citizens' part in policy making its content, and EK IEF-1.C.3 makes transmission a lifelong process. A generational shift in those beliefs is a change of culture; a swing against one government is not."),
 ("differences in political culture",
  "EK IEF-1.C.2 states that political culture forms a population's values and beliefs about the role of government, the rights of the individual, and the extent and role of citizens in controlling government policy making. Both countries in the item hold competitive elections, so the institutional fact does not separate them."),
 ("tradition and ideology among the sources of legitimacy",
  "EK LEG-1.A.2 names nationalism, tradition, governmental effectiveness, economic growth, ideology, religious heritage and organizations, and a dominant party's endorsement among the sources of legitimacy, and EK LEG-1.A.1 makes legitimacy a belief of a government's constituents. EK IEF-1.C.1's collective attitudes and beliefs are where such beliefs live."),
 ("those agents are similar across regime types while governmental pressure on them is not",
  "EK IEF-1.C.1 supplies the definition, EK IEF-1.C.2 the influences and what they form, EK IEF-1.C.3 the lifelong transmission, EK IEF-1.C.4 the agents, and EK IEF-1.C.5 the similarity of agents alongside the difference in governmental pressure."),
]

cg.check(k3_2, CLAIMS, table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25})
