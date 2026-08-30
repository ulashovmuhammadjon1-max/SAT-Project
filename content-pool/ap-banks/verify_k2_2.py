"""Key audit for AP COMPARATIVE GOVERNMENT 2.2 Comparing Parliamentary,
Presidential, and Semi-Presidential Systems.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
  PAU-3.B.1  ALTHOUGH parliamentary systems have FEWER institutional obstacles to
             enact policy than presidential systems (presidential systems have
             DIVIDED BRANCH POWERS), parliamentary systems HAVE THEIR OWN CHECKS
             ON THE EXECUTIVE BRANCH
  PAU-3.B.2  parliaments may censure cabinet ministers, refuse to pass
             executive-proposed legislation, question the executive and cabinet
             ministers, and impose time deadlines on calling new elections

Supporting: PAU-3.A.1-3 (the three definitions), PAU-3.D.1 (removal by the
legislature through DIFFERENT procedures across the course countries),
PAU-3.E.1.c (Mexico's Senate), PAU-3.E.1.d (Nigeria's Senate's unique impeachment
and confirmation powers), PAU-3.E.1.e (the Duma and the Federation Council),
PAU-3.E.1.f (the Lords delaying implementation as a power check) and PAU-3.F.2
(how legislatures reinforce legitimacy and stability).

THE HALF OF THE SENTENCE STUDENTS DROP
--------------------------------------
PAU-3.B.1 is a concession: 'ALTHOUGH parliamentary systems have fewer
institutional obstacles ... parliamentary systems have their own checks on the
executive branch.' Keep only the first clause and you conclude that a
parliamentary executive is unchecked, which the same sentence denies. Items 3, 9,
22 and 26 key the second clause, and item 22 makes the data agree with it -- the
parliamentary row's defeat share is small but NOT zero. AP_COMP_GOV_CED.md note
11 records this as one of the framework's positions most often misread.

Item 10 keys the reverse misreading, that presidential systems must be quicker
because one leader holds both executive roles. The framework says the opposite
about obstacles, and PAU-3.A.2's fusion of head of state and head of government
does not remove the separation from a separately elected legislature.

DATA ITEMS
----------
Items 20-22 use a hypothetical three-group table whose columns all point the same
way, so the framework's comparison can be checked on passage, speed and defeat at
once. Items 23-25 use a table whose four rows are exactly PAU-3.B.2's four
checks; item 24 asks for a SHARE where the distractors offer counts, and item 25
turns on frequency and effect coming apart.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k2_2

PASS = "Executive-proposed bills that became law (percent)"
MONTHS = "Median months from proposal to enactment"
DEFEAT = "Executive-proposed bills defeated by the legislature (percent)"
EPS = "Episodes recorded (hypothetical)"
CHANGED = "Episodes in which the executive afterwards changed its position"

PARL, PRES, SEMI = "Parliamentary cases", "Presidential cases", "Semi-presidential cases"


def q20(table, item):
    p = {lab: (cg.cell(table, lab, PASS), cg.cell(table, lab, MONTHS), cg.cell(table, lab, DEFEAT))
         for lab in cg.labels(table)}
    assert p[PARL][0] == max(v[0] for v in p.values()), "the parliamentary row must lead on passage"
    assert p[PARL][1] == min(v[1] for v in p.values()), "the parliamentary row must be quickest"
    assert p[PARL][2] == min(v[2] for v in p.values()), "the parliamentary row must lose the smallest share"
    assert p[SEMI][1] < p[PRES][1], "'semi-presidential takes longest' must be false"
    assert len({v[0] for v in p.values()}) == 3, "'the three groups enact the same share' must be false"
    assert all(v[2] > 0 for v in p.values()), "'no group defeats any bill' must be false"
    return "the parliamentary row leads on passage at 88, is quickest at 7 months, and loses least at 6 percent"


def q21(table, item):
    gap = cg.cell(table, PARL, PASS) - cg.cell(table, PRES, PASS)
    assert gap == 34, f"the keyed 34-point gap recomputes to {gap}"
    assert cg.cell(table, PARL, PASS) - cg.cell(table, SEMI, PASS) == 21, \
        "the 21 distractor must be the gap to the other row of the same column"
    assert cg.cell(table, SEMI, PASS) - cg.cell(table, PRES, PASS) == 13, \
        "the 13 distractor must be the remaining gap in the same column"
    assert cg.cell(table, PRES, DEFEAT) - cg.cell(table, PARL, DEFEAT) == 18, \
        "the 18 distractor must be the corresponding gap in the defeat column"
    assert cg.cell(table, PRES, MONTHS) - cg.cell(table, PARL, MONTHS) == 12, \
        "the 12 distractor must be the corresponding gap in the months column"
    return f"88 minus 54 is {gap:.0f}, and every distractor is a real gap between the wrong pair of cells or the wrong column"


def q22(table, item):
    d = cg.cell(table, PARL, DEFEAT)
    assert d > 0, "the objection requires the parliamentary row's defeat share to be non-zero"
    assert d == min(cg.col(table, DEFEAT)), "it should still be the smallest, or the student's premise would not arise"
    assert cg.cell(table, PARL, PASS) > cg.cell(table, PRES, PASS), \
        "the parliamentary row must still show fewer obstacles, since the framework says so"
    return "the parliamentary row's defeat share is the smallest in the table at 6 percent and is not zero"


def _checks(table):
    return {str(r[0]): (cg.cell(table, r[0], EPS), cg.cell(table, r[0], CHANGED)) for r in table["rows"]}


def q23(table, item):
    v = _checks(table)
    top = max(v, key=lambda k: v[k][0])
    assert top.startswith("Questioning"), f"the most frequent check is {top}"
    assert v[top][0] == 210, f"the keyed 210 episodes reads as {v[top][0]}"
    assert v[top][0] > sum(n for lab, (n, _) in v.items() if lab != top), \
        "the keyed row should exceed the other three combined, so 'most often' is unambiguous"
    assert len(v) == 4, "the table must carry all four of the framework's named checks"
    return "one row records 210 episodes, more than the other three rows combined"


def q24(table, item):
    v = _checks(table)
    share = {lab: k / n for lab, (n, k) in v.items()}
    top = max(share, key=share.get)
    assert top.startswith("Imposition"), f"the largest share belongs to {top}"
    assert v[top] == (5, 4), f"the keyed four of five reads as {v[top]}"
    bigger_counts = [lab for lab, (_, k) in v.items() if k > v[top][1]]
    assert len(bigger_counts) >= 2, \
        "at least two rejected rows must quote a LARGER raw count than the key, which is the trap"
    for lab in bigger_counts:
        assert share[lab] < share[top], f"{lab} has a bigger count but must have a smaller share"
    return f"the four shares are {[round(share[l], 2) for l in v]}, and two rejected rows quote larger counts on smaller shares"


def q25(table, item):
    v = _checks(table)
    share = {lab: k / n for lab, (n, k) in v.items()}
    most_used = max(v, key=lambda k: v[k][0])
    assert min(share, key=share.get) == most_used, \
        "the key requires the most-used check to hold the smallest share of position changes"
    least_used = min(v, key=lambda k: v[k][0])
    assert v[least_used][1] > 0, "'the least used check was never followed by a change' must be false"
    assert all(k < n for n, k in v.values()), "'every episode' must be false"
    assert any(k > 0 for _, k in v.values()), "'no episode' must be false"
    return "the most frequently recorded check holds the smallest proportion of position changes, so frequency and effect part company"


CLAIMS = [
 ("Parliamentary systems have fewer institutional obstacles",
  "EK PAU-3.B.1 states that parliamentary systems have fewer institutional obstacles to enact policy than presidential systems. Reversing the direction is the most common misreading of the sentence."),
 ("divided branch powers",
  "EK PAU-3.B.1 supplies the reason parenthetically: presidential systems have divided branch powers. EK PAU-3.A.2's separate fixed-term elections and executive-responsible cabinet are what that division consists of."),
 ("their own checks on the executive branch",
  "EK PAU-3.B.1 is a concession sentence whose second clause states that parliamentary systems have their own checks on the executive branch. Dropping that clause turns it into a claim the framework explicitly refuses to make."),
 ("imposing time deadlines",
  "EK PAU-3.B.2 lists censuring cabinet ministers, refusing to pass executive-proposed legislation, questioning the executive and ministers, and imposing time deadlines on calling new elections. These four give content to EK PAU-3.B.1's concession."),
 ("censure of a cabinet minister",
  "EK PAU-3.B.2 names censuring cabinet ministers among the parliamentary checks on the executive. A formal motion of condemnation is that check; the others concern legislation, interrogation and the election timetable."),
 ("refusal to pass executive-proposed legislation",
  "EK PAU-3.B.2 names refusing to pass executive-proposed legislation among the parliamentary checks. EK PAU-3.B.1's concession is precisely that a system with fewer institutional obstacles still contains checks of this kind."),
 ("questioning of the executive and cabinet ministers",
  "EK PAU-3.B.2 names questioning the executive and cabinet ministers among the parliamentary checks, and EK PAU-3.F.2 adds openly debating policy among the ways legislatures reinforce legitimacy and stability."),
 ("imposition of a time deadline",
  "EK PAU-3.B.2 names imposing time deadlines on calling new elections among the parliamentary checks. It matters because EK PAU-3.C.2.f gives a prime minister the power to call elections, which a deadline constrains."),
 ("names four of them",
  "EK PAU-3.B.1's second clause says parliamentary systems have their own checks on the executive branch, and EK PAU-3.B.2 lists censure, refusal of legislation, questioning and election deadlines. The student has kept the first clause and dropped the second."),
 ("attributing fewer of them",
  "EK PAU-3.B.1 assigns FEWER institutional obstacles to parliamentary systems and attributes the presidential system's obstacles to divided branch powers. EK PAU-3.A.2's fusion of head of state and head of government does not remove the separation from a separately elected legislature."),
 ("neither owes its office to the other",
  "EK PAU-3.A.2 gives presidential systems separate fixed-term popular elections for the legislature alongside a separately chosen executive, which is what EK PAU-3.B.1 means by divided branch powers. The rejected options describe EK PAU-3.A.1's parliamentary arrangement."),
 ("nominee for prime minister must be approved",
  "EK PAU-3.A.3 requires the president's nominee for prime minister to be approved by the legislature and makes cabinet members accountable to both branches, an approval step EK PAU-3.A.2's presidential type does not contain. Popular election of both branches is common to the two."),
 ("may select and remove the head of government",
  "EK PAU-3.A.1, EK PAU-3.A.2 and EK PAU-3.A.3 supply the three arrangements, and EK PAU-3.D.1 states that across the course countries executive leaders can be removed by the legislative branch through DIFFERENT procedures that control the abuse of power."),
 ("check on the executive operating inside a parliamentary system",
  "EK PAU-3.E.1.f states that the appointed House of Lords reviews and amends bills from the Commons, effectively delaying implementation as a power check, and EK PAU-3.B.1 says parliamentary systems have their own checks. Delay is not a veto, and the chamber does not remove the head of government."),
 ("checks arising from the divided branch powers",
  "EK PAU-3.E.1.c gives Mexico's elected Senate the unique power to confirm Supreme Court appointments, approve treaties and approve federal intervention in state matters, EK PAU-3.A.2 places Mexico among the presidential systems, and EK PAU-3.B.1 attributes divided branch powers to that type."),
 ("impeachment and confirmation powers",
  "EK PAU-3.E.1.d states that both chambers of Nigeria's National Assembly approve legislation and that the Senate possesses unique impeachment and confirmation powers. The rejected options describe EK PAU-3.A.1's parliamentary route, EK PAU-3.A.3's semi-presidential route, EK PAU-3.E.1.f's Lords and EK PAU-3.E.1.e's Federation Council."),
 ("appointed Federation Council that approves budget legislation",
  "EK PAU-3.E.1.e describes Russia's bicameral system in exactly these terms, and the elected chamber's confirmation of the prime minister is what EK PAU-3.A.3's semi-presidential definition requires."),
 ("facilitating compromise between factions",
  "EK PAU-3.F.2 names responding to public demand, openly debating policy, facilitating compromise between factions, extending civil liberties and restricting the power of the executive as the ways legislatures reinforce legitimacy and stability. The last is the same function EK PAU-3.B.1 describes comparatively."),
 ("removal of cabinet members through impeachment",
  "EK PAU-3.A.2 makes impeachment the route by which a presidential legislature may remove cabinet members, while EK PAU-3.B.2's parliamentary list comprises censure, refusal of legislation, questioning and election deadlines. The four rejected options are that list."),
 ("shortest median time",
  "EK PAU-3.B.1 states that parliamentary systems have fewer institutional obstacles to enacting policy. Recomputed in q20 above: one row leads on passage, is quickest, and loses the smallest share, so all three columns point the same way."),
 ("34 percentage points",
  "Recomputed in q21 above by subtracting the presidential group's passage share from the parliamentary group's. Every distractor is a real gap between a different pair of cells or in a different column."),
 ("some executive-proposed bills being defeated even in the parliamentary cases",
  "EK PAU-3.B.1's second clause says parliamentary systems have their own checks on the executive branch and EK PAU-3.B.2 names four. Recomputed in q22 above: the parliamentary row's defeat share is the smallest in the table and is not zero, so the data agree with the framework rather than with the student."),
 ("210 episodes",
  "EK PAU-3.B.2 names all four checks the table records. Recomputed in q23 above: one row exceeds the other three combined, which is what makes it unambiguously the most frequently used."),
 ("four of five episodes",
  "The question asks for a SHARE, so each row's second figure must be divided by its first. Recomputed in q24 above: at least two rejected rows quote a larger raw count while representing a much smaller share of their own totals."),
 ("smallest share of its episodes",
  "EK PAU-3.B.2 lists the four checks without ranking them, and reading the table as proportions separates frequency from effect. Recomputed in q25 above: the most frequently recorded check holds the lowest proportion of episodes followed by a change of position."),
 ("subject to checks its own legislature exercises",
  "EK PAU-3.B.1 combines both halves in one sentence: fewer institutional obstacles for parliamentary systems because presidential systems have divided branch powers, and their own checks on the executive nonetheless. Keeping only one half produces each rejected option."),
 ("divided branch powers the framework attributes to presidential systems",
  "EK PAU-3.B.1 attributes divided branch powers to presidential systems, and EK PAU-3.A.2's separately elected fixed-term legislature is what allows a rival majority to sit opposite the executive. EK PAU-3.E.1.c and EK PAU-3.E.1.d give confirmation powers to the upper chambers of the framework's two presidential cases."),
 ("gains an advantage that a deadline removes",
  "EK PAU-3.B.2 names imposing time deadlines on calling new elections among the parliamentary checks, and EK PAU-3.C.2.f gives a prime minister the power to call elections. A deadline constrains the timing of that decision without touching the head of state, the courts or the holding of elections."),
 ("question sessions have repeatedly forced changes",
  "EK PAU-3.B.2 names censure, refusal to pass executive-proposed legislation and questioning among the parliamentary checks, and the keyed finding reports all three being used. A large majority, a heavy legislative programme, sitting days and ceremonial activity say nothing about constraint."),
 ("deadlines on calling elections",
  "EK PAU-3.B.1 supplies the comparison and its concession and EK PAU-3.B.2 the four checks that give the concession content. The summary keeps both halves, which is what the framework's 'although' construction requires."),
]

cg.check(k2_2, CLAIMS, table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25})
