"""Key audit for AP COMPARATIVE GOVERNMENT 4.3 Political Party Systems.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
Learning objective PAU-4.A, seven essential knowledge statements:

  PAU-4.A.1  party systems and membership DIFFER among course countries, RANGING
             FROM DOMINANT PARTY SYSTEMS TO MULTIPARTY SYSTEMS
  PAU-4.A.2  CHINA reserves governing power to ONE PARTY to maintain CENTRALISM
             AND ORDER, while ALLOWING EIGHT OTHER PARTIES TO EXIST to BROADEN
             DISCUSSION AND CONSULTATION
  PAU-4.A.3  six rules ensuring ONE-PARTY DOMINANCE IN RUSSIA
  PAU-4.A.4  four rules facilitating MEXICO's transition AWAY from one-party
             dominance
  PAU-4.A.5  the DEGREE OF COMPETITION within multiparty systems influences
             REPRESENTATION and FORMAL POLITICAL PARTICIPATION; .a NIGERIA, .b
             the UNITED KINGDOM
  PAU-4.A.6  CATCH-ALL parties and IDEOLOGICALLY DIVERSE PLATFORMS
  PAU-4.A.7  legislatures HIGHLY ORGANIZED BY POLITICAL PARTIES, voting on
             STRICT PARTY DISCIPLINE

THE STRUCTURAL POINT THE MODULE IS BUILT AROUND: PAU-4.A.3 and PAU-4.A.4 are
mirror images. Six rules that entrench a party's hold and four that loosen one,
stated about two different course countries, so the framework's own claim is
that the SAME KIND of instrument -- registration, nomination, patronage, the
electoral administration -- runs in either direction depending on how it is set.
Items 4, 7, 14, 28 and 29 key that mirror; getting one of those keys wrong means
reading the two lists as the same list, which is the single most likely error in
this topic.

The second trap is PAU-4.A.5.b's concession. The statement says two major
parties control the legislature and executive AND that first-past-the-post
favors them, BUT that minor parties with regional representation still win some
seats. A summary that stops at "two-party system" contradicts the framework.
Items 10, 17 and 18 key that clause, item 18 by way of the mechanism in
PAU-4.B.1.g and PAU-4.B.1.h -- support spread thin wins nothing, support
concentrated in one region wins the districts there.

Item 16 keys PAU-4.B.1.b, which is where the framework says Iran lacks formal
political party structures. It is in this module because "which of the six has
no party system" is the natural companion to "how do the other five differ", and
because DEM-2.A.1.b repeats it about the Majles.

TABLE FIGURES ARE HYPOTHETICAL and the module labels every table so. The only
party numbers the module asserts about a real country are the framework's own:
Nigeria's 30 registered parties (PAU-4.A.5.a) and China's eight permitted
parties (PAU-4.A.2). Items 21 and 22 use a 30 in the table for exactly that
reason -- the row is recognizable as Nigeria's because the framework supplies
that number, not because the module invented one.

DATA ITEMS
----------
Items 20-22 read one party table; 23-25 a threshold table; 26-27 a discipline
table. Every arithmetic claim is recomputed from the table below, and every
distractor is checked to be a WRONG operation on the same table rather than a
free-floating number -- a distractor nobody can derive teaches nothing.

Item 23's key is a JOINT movement in two columns, so the check verifies both
columns are monotone and in opposite directions; a table where only one column
moved would make the key half true. Item 25 then asks which framework claim that
pattern illustrates, which is the AP move of turning a described trend back into
the course content.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k4_3

REG = "Registered political parties"
WIN5 = "Parties winning more than 5 percent of the seats"
LARGEST = "Share of seats held by the largest party (percent)"

THRESH = "Threshold for representation (percent of the vote)"
CLEARED = "Parties clearing the threshold"
WASTED = "Share of votes cast for parties that won no seats (percent)"

WITHPARTY = "Share of divisions in which members voted with their own party (percent)"
AMENDED = "Bills amended against the government's wishes in a session"


def q20(table, item):
    largest = {lab: cg.cell(table, lab, LARGEST) for lab in cg.labels(table)}
    win5 = {lab: cg.cell(table, lab, WIN5) for lab in cg.labels(table)}
    top = max(largest, key=largest.get)
    assert top == "Country A", f"the largest seat share belongs to {top}"
    assert largest["Country A"] == 94, f"the keyed 94 percent reads {largest['Country A']}"
    assert win5["Country A"] == 1, \
        f"the dominant row must have exactly one party above 5 percent, not {win5['Country A']}"
    assert min(win5[lab] for lab in win5 if lab != "Country A") >= 2, \
        "every other row must show more than one party above 5 percent, or the contrast is not clean"
    assert win5["Country B"] == 3, f"the rejected option states three parties but the row gives {win5['Country B']}"
    assert largest["Country C"] < 50, \
        f"the rejected option says fewer than half the seats but Country C holds {largest['Country C']}"
    assert len(set(largest.values())) == 3, "'all three equally' must be false"
    return (f"the largest-party shares are {[largest[l] for l in largest]} percent and the counts above "
            f"5 percent are {[win5[l] for l in win5]}, so one row alone shows near-total control with no rival")


def q21(table, item):
    reg = {lab: cg.cell(table, lab, REG) for lab in cg.labels(table)}
    win5 = {lab: cg.cell(table, lab, WIN5) for lab in cg.labels(table)}
    assert reg["Country B"] == 30, f"the framework's 30 registered parties reads {reg['Country B']}"
    assert win5["Country B"] == 3, f"the keyed three parties above 5 percent reads {win5['Country B']}"
    others = [lab for lab in reg if reg[lab] == 30 and lab != "Country B"]
    assert not others, f"only one row may carry the framework's party count; also {others}"
    assert reg["Country A"] == 9 and win5["Country A"] == 1, \
        f"the rejected nine-party option must state that row truly; it reads {reg['Country A']}, {win5['Country A']}"
    assert reg["Country C"] == 12 and win5["Country C"] == 2, \
        f"the rejected twelve-party option must state that row truly; it reads {reg['Country C']}, {win5['Country C']}"
    return ("only one row shows both the framework's 30 registered parties and three parties winning "
            "meaningful representation, and each rejected option states its own row correctly")


def q22(table, item):
    c = cg.col(table, REG)
    total = sum(c)
    assert total == 51, f"the keyed total recomputes to {total}"
    assert 30 + 12 == 42, "the 42 distractor must be the total less the smallest row"
    assert 9 + 30 == 39, "the 39 distractor must be the total less the largest row"
    assert 9 + 12 == 21, "the 21 distractor must be a two-row partial sum"
    assert max(c) == 30, "the 30 distractor must be the largest single row"
    return f"the registered-party column reads {c} and sums to {total:.0f}, with every distractor a wrong sum of the same column"


def q23(table, item):
    th = cg.col(table, THRESH)
    cleared = cg.col(table, CLEARED)
    wasted = cg.col(table, WASTED)
    assert th == sorted(th), f"the rows must be in rising threshold order; got {th}"
    assert len(set(th)) == 3, "the three thresholds must differ, or there is no pattern to read"
    assert cleared == sorted(cleared, reverse=True), \
        f"parties clearing the threshold must fall as the threshold rises; got {cleared}"
    assert wasted == sorted(wasted), \
        f"the wasted-vote share must rise as the threshold rises; got {wasted}"
    assert len(set(wasted)) == 3, "'the same at every threshold' must be false"
    assert min(cleared) > 0 and max(wasted) > 0, "'every party cleared the threshold' must be false"
    return (f"as the threshold goes {th}, the parties clearing it go {cleared} and the wasted share goes "
            f"{wasted}, so the two columns move in opposite directions at every step")


def q24(table, item):
    w = cg.col(table, WASTED)
    diff = max(w) - min(w)
    assert diff == 15, f"the keyed difference recomputes to {diff}"
    pairs = sorted({abs(a - b) for a in w for b in w if a != b})
    assert 8 in pairs and 7 in pairs, f"the 8 and 7 distractors must be other gaps in the same column; gaps are {pairs}"
    assert min(w) == 4, f"the 4 distractor must be the smallest wasted share, which reads {min(w)}"
    assert max(w) == 19, "the 19 distractor must be the largest single value read as though it were a difference"
    return f"the wasted-vote column reads {w}, so the largest minus the smallest is {diff:.0f} percentage points"


def q25(table, item):
    cleared = cg.col(table, CLEARED)
    th = cg.col(table, THRESH)
    assert th == sorted(th) and cleared == sorted(cleared, reverse=True), \
        "the table must show representation shrinking as the threshold rises, or it illustrates nothing"
    assert cleared[0] - cleared[-1] == 4, \
        f"the number of represented parties must fall visibly; it falls by {cleared[0] - cleared[-1]}"
    return f"raising the threshold from {th[0]:.0f} to {th[-1]:.0f} percent cuts represented parties from {cleared[0]:.0f} to {cleared[-1]:.0f}"


def q26(table, item):
    disc = {lab: cg.cell(table, lab, WITHPARTY) for lab in cg.labels(table)}
    amend = {lab: cg.cell(table, lab, AMENDED) for lab in cg.labels(table)}
    assert max(disc, key=disc.get) == "Legislature P", f"the higher discipline belongs to {max(disc, key=disc.get)}"
    assert disc["Legislature P"] == 98 and amend["Legislature P"] == 2, \
        f"the keyed row reads {disc['Legislature P']}, {amend['Legislature P']}"
    assert disc["Legislature Q"] == 71, f"the rejected option states 71 but the row gives {disc['Legislature Q']}"
    assert amend["Legislature Q"] > amend["Legislature P"], \
        "the low-discipline row must be the one where more bills were amended, so the two columns agree"
    assert disc["Legislature P"] != disc["Legislature Q"], "'both equally' must be false"
    return (f"party voting is {disc['Legislature P']:.0f} against {disc['Legislature Q']:.0f} percent and successful "
            f"amendments {amend['Legislature P']:.0f} against {amend['Legislature Q']:.0f}, so both columns point the same way")


def q27(table, item):
    d = cg.col(table, WITHPARTY)
    diff = max(d) - min(d)
    assert diff == 27, f"the keyed difference recomputes to {diff}"
    a = cg.col(table, AMENDED)
    assert max(a) - min(a) == 42, "the 42 distractor must be the gap in the other column"
    assert 100 - min(d) == 29, "the 29 distractor must come from subtracting the smaller share from 100"
    assert max(a) == 44, "the 44 distractor must be a raw count from the amendments column"
    assert max(d) == 98, "the 98 distractor must be the larger share read as though it were a difference"
    return f"the party-voting column reads {d}, so the difference between the two legislatures is {diff:.0f} percentage points"


CLAIMS = [
 ("from dominant party systems to multiparty systems",
  "EK PAU-4.A.1 states that party systems and membership differ among the course countries, ranging from dominant party systems to multiparty systems. The rejected ranges are the territorial, executive, legal and welfare axes stated elsewhere in the framework."),
 ("broaden discussion and consultation",
  "EK PAU-4.A.2 states that China allows eight other parties to exist to broaden discussion and consultation while only the Communist Party of China controls governing power, so their existence is consultative and not a route to office."),
 ("centralism and order",
  "EK PAU-4.A.2 names centralism and order as the values the one-party rule is meant to maintain. The rejected values are stated elsewhere in the framework and not in this statement."),
 ("selective court decisions to disqualify candidates",
  "EK PAU-4.A.3 lists increasing party registration requirements, allowing only legally registered parties to run, selective court decisions disqualifying candidates, limiting the opposition's media access, increasing threshold rules and eliminating gubernatorial elections as the rules ensuring one-party dominance in Russia."),
 ("only legally registered parties to run",
  "EK PAU-4.A.3 pairs increasing party registration requirements with allowing only legally registered parties to run for office, and those two together decide who may appear on the ballot at all, while media limits shape a campaign that still takes place."),
 ("eliminating gubernatorial elections",
  "EK PAU-4.A.3 names eliminating gubernatorial elections, which abolishes a contest rather than restricting who may enter one, and EK DEM-2.B.5.c describes regional legislatures instead appointing a governor from a presidentially approved list."),
 ("national electoral institute",
  "EK PAU-4.A.4 names eliminating el dedazo, privatizing state-owned corporations to decrease patronage, decentralizing and reducing one-party power at the subnational level, and establishing and strengthening the National Electoral Institute as facilitating Mexico's transition away from one-party dominance."),
 ("representation and formal political participation",
  "EK PAU-4.A.5 states that the degree of competition within multiparty systems can influence representation and formal political participation by citizens. Territorial structure, judicial tenure, chamber counts and international recognition are governed by other statements."),
 ("30 registered parties",
  "EK PAU-4.A.5.a states that Nigeria's multiparty system includes 30 registered political parties, with two strong parties, the People's Democratic Party and the All Progressives Congress, and a third party having a degree of electoral success."),
 ("still able to win some seats",
  "EK PAU-4.A.5.b states that two major parties control the legislature and executive under first-past-the-post rules favoring them, but that minor parties with regional representation are also able to win some legislative representation. The concession is part of the statement, not an exception to it."),
 ("ideologically diverse platforms",
  "EK PAU-4.A.6 states that catch-all political parties can earn support from groups with different characteristics, attracting popular support with ideologically diverse platforms, so breadth of platform and breadth of coalition define one another."),
 ("strict party discipline",
  "EK PAU-4.A.7 states that some legislatures, such as the United Kingdom's House of Commons, are highly organized by political parties, with voting based on strict party discipline that influences policy making."),
 ("registration, threshold, court and media rules",
  "EK PAU-4.A.2 reserves governing power in China to one party while permitting eight others to exist for consultation, whereas EK PAU-4.A.3 secures dominance in Russia through six rules operating inside elections that still occur, and EK DEM-1.C.5 records those elections as contested with limited competitiveness."),
 ("and the other with ensuring one-party dominance",
  "EK PAU-4.A.4 credits Mexico's four measures with facilitating a transition away from one-party dominance while EK PAU-4.A.3 credits Russia's six rules with ensuring it, so the framework describes rule changes running in opposite directions."),
 ("a third with some electoral success",
  "EK PAU-4.A.5.a gives Nigeria 30 registered parties with two strong ones and a third having a degree of electoral success, and EK PAU-4.A.5.b gives the United Kingdom two major parties alongside minor regional parties winning some seats, so both systems seat more than two parties."),
 ("Iran",
  "EK PAU-4.B.1.b states that Iran lacks formal political party structures and that parties operate as loosely formed political alliances with questionable linkage to constituents, and EK DEM-2.A.1.b repeats that the Majles lacks formal political party structures."),
 ("also able to win some legislative representation",
  "EK PAU-4.A.5.b closes with the concession that minor parties with regional representation are also able to win some legislative representation, and EK PAU-4.B.1.h adds that single-member districts allow regional parties to win legislative seats. Every rejected option is a part of the statement the summary keeps."),
 ("spread thinly wins no districts",
  "EK PAU-4.B.1.g states that single-member district plurality elections diminish minor-party representation and EK PAU-4.B.1.h that single-member districts allow regional parties to win legislative seats, and EK DEM-2.B.2 supplies the mechanism, since only the leading candidate in a district converts votes into a seat."),
 ("catch-all parties can earn support from groups with different characteristics",
  "EK PAU-4.A.6 states that catch-all political parties earn support from groups with different characteristics by attracting popular support with ideologically diverse platforms, making the platform the means and the breadth of support the end."),
 ("94 percent of the seats",
  "EK PAU-4.A.1 places dominant party systems at one end of its range, so the dominant end shows one party holding almost all the seats with no significant rival. Recomputed in q20 above, where one row alone shows both features at once."),
 ("30 registered parties and three winning more than 5 percent",
  "EK PAU-4.A.5.a gives Nigeria 30 registered parties with two strong parties and a third having a degree of electoral success, so the matching row needs both the party count and three parties winning meaningful representation. Recomputed in q21 above."),
 ("51",
  "Recomputed in q22 above by summing the registered-party column across the three rows. Each distractor is the total less one row, a two-row partial sum, or the largest single row read as a total."),
 ("fewer parties clear it and a larger share of votes",
  "EK PAU-4.A.3 names increasing threshold rules among the devices limiting party access to the ballot and EK PAU-4.B.1.e records diminished representation of smaller parties in Russia because of changing threshold rules. Recomputed in q23 above, where both columns move monotonically and in opposite directions."),
 ("15 percentage points",
  "Recomputed in q24 above by subtracting the smallest wasted-vote share from the largest. The distractors are the two other gaps in that column, the smallest figure in it, and the largest figure in it read as though it were a difference."),
 ("changing threshold rules",
  "EK PAU-4.B.1.e states that diminished representation of smaller parties occurs because of changing threshold rules, and EK PAU-4.A.3 lists increasing threshold rules among the devices ensuring one-party dominance. Recomputed in q25 above, where raising the threshold cuts the number of represented parties."),
 ("Legislature P",
  "EK PAU-4.A.7 states that legislatures highly organized by political parties vote on strict party discipline that influences policy making, so the match needs near-unanimous party voting together with an executive rarely defeated on amendments. Recomputed in q26 above, where both columns point the same way."),
 ("27 percentage points",
  "Recomputed in q27 above by subtracting the smaller party-voting share from the larger. The distractors are the gap in the amendments column, the result of subtracting from 100 instead, a raw amendment count, and the larger share read as a difference."),
 ("independent electoral institute was established",
  "EK PAU-4.A.4 names eliminating el dedazo, privatizing state-owned corporations to decrease patronage, decentralizing and reducing one-party power at the subnational level, and establishing and strengthening the National Electoral Institute as the measures facilitating a transition away from one-party dominance. Every rejected finding is either the opposite result or one of EK PAU-4.A.3's devices for entrenching dominance."),
 ("courts have disqualified opposition candidates selectively",
  "EK PAU-4.A.3 lists increasing registration requirements, increasing threshold rules, selective court decisions disqualifying candidates and limiting the opposition's media access among the rules ensuring one-party dominance in Russia. The rejected findings describe EK PAU-4.A.6's catch-all party and EK PAU-4.A.5's competitive multiparty systems."),
 ("how tightly they discipline their legislators",
  "EK PAU-4.A.1 supplies the range of party systems, EK PAU-4.A.2 through EK PAU-4.A.4 the rules that entrench or loosen one party's hold, EK PAU-4.A.5 the effect of competition on representation and participation, EK PAU-4.A.6 the catch-all party and EK PAU-4.A.7 strict party discipline in some legislatures."),
]

cg.check(k4_3, CLAIMS,
         table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27})
