"""Key audit for AP COMPARATIVE GOVERNMENT 3.6 Forces that Impact Political
Participation.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
  DEM-1.B.1  both regime types SUPPORT SIMILAR FORMS of participation, including
             voting, and differ in citizens' IMPACT based on HOW OPEN AND
             COMPETITIVE ELECTIONS ARE; many authoritarian elections have FEW IF ANY
             OPPOSITION CANDIDATES -- defined as those ADVOCATING DIFFERING VIEWS
             FROM THE CONTROLLING PARTY/ELITE -- and the government OFTEN INTERVENES
             to ensure its preferred candidates win
  DEM-1.B.2  INFORMAL participation (PROTESTS, POLITICAL CRITICISM THROUGH SOCIAL
             MEDIA) is treated differently; authoritarian systems show LESS
             TOLERANCE OF CRITICAL VIEWPOINTS
  DEM-1.B.3  BOTH types REGULATE formal participation by RESTRICTING VOTING ACCESS
             and DISALLOWING DISRUPTIVE AND VIOLENT PROTESTS, but authoritarian
             regimes limit participation TO A MUCH GREATER EXTENT
  DEM-1.B.4  authoritarian regimes TOLERATE MASS PROTESTS LESS, VALUING PUBLIC ORDER
             MORE THAN INDIVIDUAL LIBERTIES AND CIVIL RIGHTS

THE FRAMEWORK'S OWN TRAP
------------------------
DEM-1.B.3 is the statement the CED builds a sample multiple-choice question on:
three of that item's four distractors are 'only authoritarian regimes...'
statements, and the key is the one recognizing that BOTH types regulate formal
participation and differ in degree (AP_COMP_GOV_CED.md note 13). Items 7, 10, 16
and 23 key that reading, and nothing here treats the existence of a restriction as
evidence of regime type on its own -- item 16's scenario is a disruptive march
dispersed in an acknowledged democracy.

Suggested skill 5.B is Argumentation, so items 17, 18, 28 and 29 ask which
evidence would support or weaken a claim.

DATA ITEMS
----------
Three sets, eight items. The election table separates ballot crowding from the
presence of DIFFERING-VIEW candidates, which is DEM-1.B.1's actual criterion. The
regulation table is built so the two rows DEM-1.B.3 names as common carry
double-figure counts in BOTH columns while the two rows DEM-1.B.2 and DEM-1.B.4
concern diverge sharply -- the framework's difference of degree and its difference
of tolerance, side by side. The protest table then puts DEM-1.B.4 alone.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k3_6

PERSEAT = "Candidates on the ballot per seat"
DIFF = "Share of candidates advocating views differing from the governing party (percent)"
WON = "Share of contests won by the governing party (percent)"
DEMC = "Number of democratic cases applying it"
AUTHC = "Number of authoritarian cases applying it"
PERM = "Mass demonstrations permitted to proceed, 2015-2020"
DISP = "Mass demonstrations dispersed by force, 2015-2020"
PROSEC = "Share of demonstrators prosecuted (percent)"

COMMON = ("Restrictions on voting access", "Disallowing disruptive and violent protests")
DIVERGENT = ("Banning peaceful mass demonstrations", "Prosecuting online criticism of officials")


def _opp(table):
    return {lab: (cg.cell(table, lab, PERSEAT), cg.cell(table, lab, DIFF), cg.cell(table, lab, WON))
            for lab in cg.labels(table)}


def q20(table, item):
    v = _opp(table)
    per, diff, won = v["Country S"]
    assert per == min(x[0] for x in v.values()) and per < 1.5, "the keyed row must have barely more than one candidate per seat"
    assert diff == min(x[1] for x in v.values()) and diff < 10, "the keyed row must have almost no differing-view candidates"
    assert won == max(x[2] for x in v.values()) and won > 90, "the keyed row must have the governing party winning nearly everything"
    return "one row shows 1.2 candidates per seat, 6 percent advocating differing views, and 97 percent of contests won"


def q21(table, item):
    v = _opp(table)
    per, diff, won = v["Country T"]
    assert per == max(x[0] for x in v.values()), "the keyed row must have the most candidates per seat"
    assert diff == max(x[1] for x in v.values()), "the keyed row must have the largest differing-view share"
    assert won == min(x[2] for x in v.values()) and won < 50, \
        "the keyed row's governing party must win fewer than half the contests"
    assert v["Country U"][2] > 50, "the rejected middle row's governing party must win a majority, as its option says"
    return "one row leads on candidates per seat and on differing-view candidates while its governing party wins under half the contests"


def q22(table, item):
    col = cg.col(table, WON)
    gap = max(col) - min(col)
    assert gap == 53, f"the keyed gap recomputes to {gap}"
    assert max(col) - sorted(col)[1] == 39 and sorted(col)[1] - min(col) == 14, \
        "the 39 and 14 distractors must be the other pairwise gaps in the same column"
    diff = cg.col(table, DIFF)
    assert max(diff) - min(diff) == 65, "the 65 distractor must be the corresponding gap in the differing-views column"
    assert max(col) == 97, "the 97 distractor must be the largest single value read as a difference"
    return f"the governing-party column spans {min(col):.0f} to {max(col):.0f}, a gap of {gap:.0f}"


def _reg(table):
    return {str(r[0]): (cg.cell(table, r[0], DEMC), cg.cell(table, r[0], AUTHC)) for r in table["rows"]}


def q23(table, item):
    v = _reg(table)
    for lab in COMMON:
        d, a = v[lab]
        assert d >= 10 and a >= 10, f"{lab} must carry double figures in BOTH columns; it reads {d}, {a}"
    for lab in DIVERGENT:
        d, a = v[lab]
        assert d <= 2 and a >= 15, f"{lab} must be near-absent from the democratic column; it reads {d}, {a}"
    assert all(d > 0 for d, _ in v.values()), "'no regulation appears among democratic cases' must be false"
    return "the two rows the framework calls common carry double figures in both columns; the other two are near-absent from one"


def q24(table, item):
    v = _reg(table)
    spread = {lab: abs(a - d) for lab, (d, a) in v.items()}
    top2 = sorted(spread, key=spread.get, reverse=True)[:2]
    assert set(top2) == set(DIVERGENT), f"the two most divergent rows are {top2}"
    for lab in COMMON:
        assert spread[lab] < min(spread[x] for x in DIVERGENT), \
            f"{lab} must diverge less than either of the two keyed rows"
    return f"the four spreads are {[spread[l] for l in v]}, and the two largest are the protest ban and the prosecution of online criticism"


def q25(table, item):
    col = cg.col(table, AUTHC)
    total = sum(col)
    assert total == 74, f"the keyed total recomputes to {total}"
    assert sum(cg.col(table, DEMC)) == 37, "the 37 distractor must be the other column's total"
    assert total - 17 == 57, "the 57 distractor must be the total less one row"
    assert col[0] + col[1] == 39, "the 39 distractor must be a two-row partial sum"
    assert 20 in col, "the 20 distractor must be a single row of the same column"
    return f"the authoritarian column reads {col} and sums to {total:.0f}, with each distractor a wrong column or partial sum"


def _prot(table):
    return {lab: (cg.cell(table, lab, PERM), cg.cell(table, lab, DISP), cg.cell(table, lab, PROSEC))
            for lab in cg.labels(table)}


def q26(table, item):
    v = _prot(table)
    perm, disp, pros = v["Country W"]
    assert disp > perm, "the keyed row must disperse more demonstrations than it permits"
    assert pros > 33, "the key says more than a third of demonstrators were prosecuted"
    other = v["Country V"]
    assert other[0] > other[1] and other[2] < pros, \
        "the rejected row must permit more than it disperses and prosecute far less"
    assert other[0] + other[1] > perm + disp, \
        "the rejected row must record more demonstrations in total, so 'more in total' is a true but irrelevant option"
    return "one row disperses 96 demonstrations against 24 permitted and prosecutes 37 percent of demonstrators"


def q27(table, item):
    v = _prot(table)
    perm, disp, pros = v["Country W"]
    pct = disp / (perm + disp) * 100
    assert abs(pct - 80) < 1.0, f"the keyed share recomputes to {pct:.1f} percent"
    assert abs(100 - pct - 20) < 1.0, "the 20 distractor must be the complementary share"
    assert pros == 37, "the 37 distractor must be the prosecution figure from the same row"
    vperm, vdisp, _ = v["Country V"]
    assert abs(vdisp / (vperm + vdisp) * 100 - 4) < 1.0, "the 4 distractor must be the other row's dispersal share"
    assert disp == 96, "the 96 distractor must be the raw count read as a percentage"
    return f"{disp:.0f} of {perm + disp:.0f} demonstrations is {pct:.1f} percent, and every distractor is a real figure read wrongly"


CLAIMS = [
 ("both support similar forms of participation",
  "EK DEM-1.B.1 states that authoritarian and democratic regimes support similar forms of participation to influence policy making, including casting votes in public elections. The difference it draws is about citizens' impact rather than about which forms exist."),
 ("how open and competitive elections are",
  "EK DEM-1.B.1 states that the two regime types differ in how much impact citizens have on policies and policy making based on how open and competitive elections are. Eligibility, territorial structure and institutional design are treated under other statements."),
 ("advocating differing views from that of the controlling party",
  "EK DEM-1.B.1 defines opposition candidates parenthetically as those advocating differing views from that of the controlling party or elite, so the definition turns on the views advanced rather than on a candidate's history or affiliation."),
 ("intervene in those elections",
  "EK DEM-1.B.1 states that the government often intervenes in these elections to ensure that its preferred candidates and parties win, in the same statement that notes few if any opposition candidates are allowed to run. The elections still take place."),
 ("political criticism expressed through social media",
  "EK DEM-1.B.2 gives protests and political criticism expressed through social media as its examples of informal participation. Casting ballots belongs to the formal participation of EK DEM-1.A.4 and EK DEM-1.B.3."),
 ("less tolerance of critical viewpoints",
  "EK DEM-1.B.2 states that informal participation is treated differently across regime types and that authoritarian systems show less tolerance of critical viewpoints that may challenge them. EK DEM-1.C.3 supplies the framework's instances of media restriction."),
 ("both authoritarian and democratic regimes regulate it",
  "EK DEM-1.B.3 states that both regime types regulate formal political participation and that authoritarian regimes manage and limit it to a much greater extent. The CED's own sample question is built on rejecting the exclusive reading."),
 ("restrictions on voting access and disallowing disruptive and violent protests",
  "EK DEM-1.B.3 names these two as regulations both regime types apply. The rejected options describe measures the framework attributes to particular regimes rather than to both."),
 ("to a much greater extent",
  "EK DEM-1.B.3 uses exactly this phrase, fixing both the direction and the size of the difference while keeping the practice common to both types."),
 ("does not by itself identify the regime type",
  "EK DEM-1.B.3 states that both regime types place restrictions on voting access, differing in degree rather than in kind, and the CED's own sample multiple-choice question is built on rejecting the exclusive reading."),
 ("tolerate them less than democratic regimes do",
  "EK DEM-1.B.4 states that authoritarian regimes tolerate mass political protests and movements less than democratic regimes do. EK DEM-1.B.3 has already established that both types disallow disruptive and violent protests, so this is a further difference of degree."),
 ("value public order more than individual liberties",
  "EK DEM-1.B.4 gives this as the reason for the difference in tolerance. What a regime values is the axis EK IEF-1.C.1 makes political culture set expectations along."),
 ("both find authoritarian regimes less tolerant",
  "EK DEM-1.B.2 concerns informal participation including criticism through social media and EK DEM-1.B.4 concerns mass political protests and movements, and both state that authoritarian regimes are less tolerant. They are separate statements pointing the same way."),
 ("few if any opposition candidates",
  "EK DEM-1.B.1 describes many elections in authoritarian regimes as having few if any opposition candidates, those advocating differing views from the controlling party or elite, with the government often intervening to secure its preferred results. Both features appear in the scenario."),
 ("less tolerance of critical viewpoints, including political criticism expressed through social media",
  "EK DEM-1.B.2 names political criticism expressed through social media among the forms of informal participation and states that authoritarian systems show less tolerance of critical viewpoints. The asymmetry between critical and supportive posts is that intolerance made visible."),
 ("both regime types regulate formal participation by disallowing disruptive and violent protests",
  "EK DEM-1.B.3 states that both authoritarian and democratic regimes regulate formal participation by restricting voting access and disallowing disruptive and violent protests. A disruptive march dispersed in a democracy is that statement's democratic half."),
 ("Almost no candidates advocating views differing from the governing party",
  "EK DEM-1.B.1 makes citizens' impact depend on how open and competitive elections are and describes many authoritarian elections as having few if any opposition candidates with the government intervening. Turnout, timing, sitting dates and prompt publication bear on none of that."),
 ("dispersed by force and a substantial share of participants were prosecuted",
  "EK DEM-1.B.4 states that authoritarian regimes tolerate mass protests less, valuing public order more than individual liberties and civil rights. Dispersal and prosecution measure tolerance, whereas a notice requirement is the ordinary regulation EK DEM-1.B.3 attributes to both types."),
 ("difference lies in how open and competitive those elections are",
  "EK DEM-1.B.1 states that both regime types support similar forms of participation, including voting, and differ in citizens' impact according to how open and competitive elections are. EK LEG-1.A.2 adds that popular elections can be a source of legitimacy for both."),
 ("barely more than one candidate per seat",
  "EK DEM-1.B.1 describes many authoritarian elections as having few if any opposition candidates with the government intervening to ensure its preferred candidates win. Recomputed in q20 above: one row shows a crowded-out ballot, almost no differing-view candidates and near-total victory together."),
 ("the governing party winning fewer than half the contests",
  "EK DEM-1.B.1 makes citizens' impact depend on how open and competitive elections are. Recomputed in q21 above: one row leads on candidates per seat and on differing-view candidates while its governing party can and does lose."),
 ("53 percentage points",
  "Recomputed in q22 above from the governing-party column. Every distractor is a real figure from another pair of rows, another column, or a single value read as a difference."),
 ("appear in substantial numbers of both",
  "EK DEM-1.B.3 names restrictions on voting access and the disallowing of disruptive and violent protests as regulations BOTH regime types apply. Recomputed in q23 above: those two rows carry double figures in both columns while the other two are near-absent from the democratic column."),
 ("banning peaceful mass demonstrations and prosecuting online criticism",
  "EK DEM-1.B.4 states that authoritarian regimes tolerate mass political protests less and EK DEM-1.B.2 that they show less tolerance of critical viewpoints including criticism through social media. Recomputed in q24 above: those two rows have the largest spreads between the columns."),
 ("74",
  "Recomputed in q25 above by summing the authoritarian column. Each distractor is the other column's total, the total less a row, a two-row partial sum, or a single row."),
 ("far more demonstrations were dispersed by force than were permitted",
  "EK DEM-1.B.4 states that authoritarian regimes tolerate mass political protests and movements less, valuing public order more than individual liberties and civil rights. Recomputed in q26 above, including that the rejected row records more demonstrations in total, which makes that option true but irrelevant."),
 ("80 percent",
  "Recomputed in q27 above by dividing the demonstrations dispersed by force by the total permitted plus dispersed. Every distractor is a real figure read wrongly: the complement, the prosecution share, the other row's dispersal share, and a raw count."),
 ("Prosecutions for online criticism of officials have risen sharply",
  "EK DEM-1.B.2 names political criticism expressed through social media among the forms of informal participation and states that authoritarian systems show less tolerance of critical viewpoints. A rise in prosecutions specific to criticism against a flat background is evidence about tolerance rather than about usage."),
 ("removed from the ballot before voting began",
  "EK DEM-1.B.1 defines opposition candidates as those advocating differing views from the controlling party or elite and makes their presence part of what open and competitive means. Turnout, polling error, voluntary abstention and a slow count are all compatible with a free contest."),
 ("limit participation to a much greater extent",
  "EK DEM-1.B.1 supplies the similar forms and the difference in impact, EK DEM-1.B.2 the treatment of informal criticism, EK DEM-1.B.3 the regulation both types apply and the much greater extent in one, and EK DEM-1.B.4 the lower tolerance of mass protest and its reason."),
]

cg.check(k3_6, CLAIMS,
         table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27})
