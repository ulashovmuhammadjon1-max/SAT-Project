"""Key audit for AP HUMAN GEOGRAPHY 7.4 Women and Economic Development.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective SPS-7.D, suggested skill 3.D, and three
statements:

    SPS-7.D.1 The roles of women change as countries develop economically.
    SPS-7.D.2 Although there are more women in the workforce, they do not have
              equity in wages or employment opportunities.
    SPS-7.D.3 Microloans have provided opportunities for women to create small
              local businesses, which have improved standards of living.

THE OBJECTIVE'S PHRASE IS "AND TO WHAT EXTENT" and it is the most important
wording in the topic. SPS-7.D does not ask whether development produces gender
parity but HOW and HOW FAR, and SPS-7.D.2 supplies the answer in its own sentence
structure: ALTHOUGH there are more women in the workforce, they do not have
equity in wages or employment opportunities. Items 2, 3, 14, 22 and 24 are built
on that concession. Item 3 asks for the function of the word "although"
directly, because a student who remembers only the first clause has learned the
opposite of what the statement says, and item 22's key states both halves
together as the framework's own answer to its own objective.

SPS-7.D.2 NAMES TWO KINDS OF INEQUITY, not one. Wages concern what is paid;
employment opportunity concerns which occupations and which promotions are
reachable. Items 4, 5, 16, 18 and 28 keep them apart, and item 28's table is
built so that near-equal representation in one occupation group sits beside 24
percent in senior management and 12 percent in craft work -- an uneven
distribution ACROSS occupations is exactly what the second phrase names, and no
participation rate would reveal it.

SPS-7.D.3 IS A POSITIVE CLAIM AND THIS MODULE REPORTS IT AS ONE. The CED says
microloans HAVE PROVIDED opportunities and the businesses HAVE IMPROVED standards
of living, and no item here contradicts that. Items 13 and 29 do what the
objective licenses instead: they ask how FAR the instrument reaches, since a loan
answers the absence of capital and not the wage gap or the occupational access
the same topic names separately. That is a question about extent rather than a
denial, and the distinction is the whole reason item 13's key is worded as it is.

WHAT THIS MODULE DOES NOT ASSERT: that development produces parity automatically
(item 22 keys against it), or that participation rises steadily with income --
item 26's record deliberately does NOT, and its recompute asserts the
non-monotonicity, because a table where everything rose together would let a
student reach the key while believing something the record does not support.

NO REAL COUNTRY IS NAMED ANYWHERE IN THIS MODULE, the three data items included.

SYNONYM CARE. `geo_check` treats {"gender inequality index", "gii"} as one
construct, so item 9 names it in exactly one way.

The three table items (26, 27, 28) are the computational gate:

  26  the earnings ratio checked to rise at every step AND to stop short of
      parity, and participation checked NOT to move monotonically with income --
      both halves of the key, and the second is the harder one
  27  the number of women borrowers derived from the share and the total, with
      the survival rate checked to be a majority, since a distractor asserts the
      opposite
  28  every row checked to sum to 100 and women's share checked to span a wide
      range across the four groups, which is what makes the distribution uneven
      rather than merely unequal in total

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting. One item again carried a malformed token in
place of `ans=0`, caught by the import-and-assert check at the top of this file.
"""
import re

import geo_check
import g7_4

for _n, _item in enumerate(g7_4.QUESTIONS, 1):
    assert isinstance(_item.get("ans"), int), f"7.4 q{_n}: `ans` is {_item.get('ans')!r}"
    assert 0 <= _item["ans"] < len(_item["choices"]), f"7.4 q{_n}: ans out of range"


def q26_partial_progress(table):
    """Earnings ratio rises but never reaches parity; participation does not track."""
    income = [float(r[1].replace(",", "")) for r in table["rows"]]
    participation = [float(r[2]) for r in table["rows"]]
    ratio = [float(r[3]) for r in table["rows"]]
    assert all(b > a for a, b in zip(income, income[1:])), income
    assert all(b > a for a, b in zip(ratio, ratio[1:])), ratio
    # Rises, and stops short: the "to what extent" of the objective.
    assert max(ratio) < 1.0, ratio
    assert ratio[0] == 0.58 and ratio[-1] == 0.84, ratio
    # Participation must NOT move monotonically, or the key's second half fails.
    rising = all(b > a for a, b in zip(participation, participation[1:]))
    falling = all(b < a for a, b in zip(participation, participation[1:]))
    assert not rising and not falling, participation
    assert participation[1] < participation[0], participation
    return f"rises at every step from {ratio[0]} to {ratio[-1]} without reaching parity"


def q27_microloan_outcomes(table):
    """Women borrowers derived; survival rate must be a majority."""
    vals = {r[0]: float(r[1].replace(",", "")) for r in table["rows"]}
    borrowers = vals["Borrowers"]
    share = vals["Share of borrowers who are women (%)"]
    women = borrowers * share / 100
    assert borrowers == 4200 and share == 88, (borrowers, share)
    assert 3690 < women < 3710, women
    survival = vals["Businesses still operating after three years (%)"]
    # A distractor asserts most had closed; the record must contradict it.
    assert survival > 50, survival
    assert vals["Median change in borrower household income (%)"] == 34, vals
    assert vals["Average loan (currency units)"] < 1000, vals
    # The choice says "about 3,700", which is 3,696 rounded to the nearest
    # hundred -- the way a person states a derived headcount. Returning the
    # exact figure made the containment check demand digits no correct choice
    # would print, so it failed a question whose arithmetic is right. Round to
    # the hundred HERE and keep the exact value gated by the bound above, so
    # the check still fails if the table or the share is edited.
    rounded = round(women / 100) * 100
    assert abs(women - rounded) <= 50, (women, rounded)
    return f"About {rounded:,.0f} of the {borrowers:,.0f} borrowers are women"


def q28_occupational_distribution(table):
    """Rows sum to 100, and women's share spans a wide range across groups."""
    share = {}
    for group, w, m in table["rows"]:
        assert float(w) + float(m) == 100, (group, w, m)
        share[group] = float(w)
    assert share["Senior management"] == 24, share
    assert share["Craft and machine operation"] == 12, share
    assert 49 <= share["Professional and technical"] <= 52, share
    # Uneven rather than merely unequal: the spread across groups is the point.
    assert max(share.values()) - min(share.values()) > 50, share
    return "only 24 percent of senior management and 12 percent of craft"


CLAIMS = [
 ("They change",
  "EK SPS-7.D.1 states simply that the roles of women change as countries develop economically. The claim is that the roles are a function of the economy rather than a fixed feature of a society, which is the same move EK IMP-5.C.1 makes for agriculture."),

 ("they do not have equity in wages or employment opportunities",
  "EK SPS-7.D.2 states that ALTHOUGH there are more women in the workforce, they do not have equity in wages or employment opportunities. Both halves sit in one sentence, and reporting either alone misstates it."),

 ("marks the first clause as a real gain and the second as a limit on it",
  "EK SPS-7.D.2 begins with ALTHOUGH there are more women in the workforce. A concession asserts both halves while marking the second as the one qualifying the first, which is exactly the structure learning objective SPS-7.D's 'to what extent' asks students to handle."),

 ("because the occupations they predominantly hold are paid less",
  "EK SPS-7.D.2 names equity in wages as one of the two things not achieved. The gap has two components -- different pay within a job and different pay between the jobs each group predominantly holds -- and a measure capturing only the first understates it."),

 ("Unequal access to particular occupations and to advancement within them",
  "EK SPS-7.D.2 names equity in employment opportunities separately from equity in wages. Opportunity concerns which jobs are reachable and which promotions are available, which is a claim about the shape of employment rather than about its price."),

 ("Falling fertility, rising education and the growth of service and office employment",
  "EK SPS-7.D.1 says the roles of women change as countries develop economically and EK SPS-7.D.2 records that there are more women in the workforce. Fewer years of childbearing, more schooling and a shift toward sectors hiring on credentials are the changes that route runs through."),

 ("Schooling extends, fertility falls, employment shifts toward sectors hiring on qualifications",
  "EK SPS-7.D.1 states that the roles of women change as countries develop economically without specifying how, and learning objective SPS-7.D asks HOW as well as to what extent. Each of these is a change in what is possible or required rather than a change of opinion."),

 ("Both make women's economic role a function of the system they work within",
  "EK IMP-5.C.1 says the role of females in food production varies depending on the type of production involved, and EK SPS-7.D.1 says the roles of women change as countries develop economically. Both locate the explanation in the surrounding economy rather than in any fixed characteristic."),

 ("reproductive health, empowerment and labour-market participation",
  "EK SPS-7.C.2 names those three as the components of that measure, and EK SPS-7.D.2 says women lack equity in wages and employment opportunities. The measure and the claim concern the same conditions, which is why the two topics sit next to each other."),

 ("Provided opportunities for women to create small local businesses",
  "EK SPS-7.D.3 states that microloans have provided opportunities for women to create small local businesses, which have improved standards of living. The chain has three steps -- the loan, the business, the improvement -- and the framework asserts all three."),

 ("too small for a bank's costs to be worth incurring",
  "EK SPS-7.D.3 says microloans have PROVIDED OPPORTUNITIES, which implies an opportunity that did not previously exist. Assessing a loan costs roughly the same whatever its size and collateral is what a lender falls back on, so both obstacles bear hardest on the smallest borrowers."),

 ("the income the business earns is what raises the household's standard of living",
  "EK SPS-7.D.3 says microloans provided opportunities to CREATE SMALL LOCAL BUSINESSES, WHICH have improved standards of living. The relative pronoun does the work: the businesses improved living standards and the loan is what made the businesses possible."),

 ("leaves untouched the wage gap and the unequal access to occupations",
  "EK SPS-7.D.3 credits microloans with providing opportunities and improving standards of living, and EK SPS-7.D.2 names a lack of equity in wages and employment opportunities. Learning objective SPS-7.D asks TO WHAT EXTENT, and an instrument supplying capital answers one of the constraints the topic names."),

 ("how far economic development has contributed to gender parity",
  "Learning objective SPS-7.D asks students to explain how AND TO WHAT EXTENT changes in economic development have contributed to gender parity. A yes-or-no answer does not address the second half, and EK SPS-7.D.2's concession is the framework's own indication that the answer is partial."),

 ("the distribution of each group across occupations and levels of seniority",
  "EK SPS-7.D.2 names both wages and employment opportunities as areas without equity, so a measure of one does not stand in for the other. Participation says who is in the labour market, earnings say what they receive, and the occupational distribution says where in it they are."),

 ("includes the effect of women being concentrated in lower-paid occupations",
  "EK SPS-7.D.2 names inequity in wages AND in employment opportunities as two things. Comparing like with like removes the second from the measurement, which serves one purpose and understates the total difference in earnings the two together produce."),

 ("a group carrying more of it has less time available for paid work",
  "EK SPS-7.D.2 says women lack equity in employment opportunities, and time is one of the constraints on opportunity. Work that is not paid for is not counted, which does not make it absent, and the hours it takes are not available for anything else."),

 ("The concentration of each group in different occupations",
  "EK SPS-7.D.2 names inequity in wages and in employment opportunities in one clause, and occupational segregation is the mechanism joining them. If the two groups hold different jobs and those jobs pay differently, an earnings gap follows without any employer paying two people differently for identical work."),

 ("occupations hiring on schooling and credentials",
  "EK SPS-7.D.1 says the roles of women change as countries develop economically, and EK SPS-7.B.1 says the sectors are characterized by distinct development patterns. A change in which sectors are hiring is a change in what qualifications the labour market rewards."),

 ("later and fewer births, which together lengthen the period available for paid work",
  "EK SPS-7.D.1 says the roles of women change as countries develop economically, and EK SPS-7.C.1 names both fertility rates and literacy among the measures of development. The two move together with development and both bear on how much of a life is available for paid work."),

 ("the national labour market, where wages and occupational access are set",
  "EK SPS-7.D.2 concerns wages and employment opportunities, which are properties of a labour market, while EK SPS-7.D.3 concerns a household business. The two scales require different data to answer different halves of the objective."),

 ("the framework states in the same breath that equity in wages and opportunities has not followed",
  "EK SPS-7.D.1 says roles change with development and EK SPS-7.D.2 says that although there are more women in the workforce, equity in wages and employment opportunities has not been reached. The two statements together are the framework's answer to its own objective's 'to what extent'."),

 ("no legal protection, no recorded earnings and no career ladder",
  "EK SPS-7.D.2 names inequity in wages and employment opportunities, and EK SPS-7.C.1 names sectoral structure BOTH FORMAL AND INFORMAL among the measures of development. Being in the labour market and being in its protected part are different things, and only the first shows in a participation rate."),

 ("Entry into the labour market and position within it are different things",
  "EK SPS-7.D.2 states exactly this combination: ALTHOUGH there are more women in the workforce, they do not have equity in wages or employment opportunities. Counting who is in the labour market and examining where in it they are are two different questions, and the sentence answers both."),

 ("A woman borrowing a small sum to start a market stall, matched to microloans creating small local businesses",
  "EK SPS-7.D.1, EK SPS-7.D.2 and EK SPS-7.D.3 cover changing roles, the absence of equity, and microloans respectively. Only one pairing here places an observation under the statement that actually covers it."),

 ("rises at every step from 0.58 to 0.84 without reaching parity",
  "Recomputed from the record: the earnings ratio rises at every step from 0.58 to 0.84 and stops short of 1.00, while participation runs 62, 45, 58, 69 and so does not track income at all. Learning objective SPS-7.D asks TO WHAT EXTENT development has contributed to gender parity, and a measure improving without arriving is what a partial answer looks like.",
  ),

 ("About 3,700 of the 4,200 borrowers are women",
  "Recomputed from the record: 88 percent of 4,200 borrowers is about 3,700, the three-year survival rate of 71 percent is a majority, and median household income rose 34 percent. EK SPS-7.D.3 says microloans provided opportunities for women to create small local businesses which have improved standards of living.",
  ),

 ("only 24 percent of senior management and 12 percent of craft",
  "Recomputed from the record: every row sums to 100 and women's share runs from 68 percent in clerical and service work down to 24 in senior management and 12 in craft and machine operation, a spread of more than fifty points. EK SPS-7.D.2 names inequity in EMPLOYMENT OPPORTUNITIES separately from wages, and that spread is what the phrase describes.",
  ),

 ("borrowers who were selected or self-selected into the programme",
  "EK SPS-7.D.3 credits microloans with providing opportunities and improving standards of living, and learning objective SPS-7.D asks TO WHAT EXTENT. Households that sought and obtained a loan may differ from those that did not in ways that also affect their incomes, which limits the comparison rather than the programme."),

 ("equity in wages and occupational access has not followed",
  "EK SPS-7.D.1 supplies the changing roles, EK SPS-7.D.2 the gain and its limit in one sentence, and EK SPS-7.D.3 the microloan route. Each rejected summary either claims a parity the framework denies, denies a change it asserts, or drops the concession that answers the objective's 'to what extent'."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"7.4 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"7.4 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_partial_progress,
    27: q27_microloan_outcomes,
    28: q28_occupational_distribution,
}

geo_check.check(g7_4, ANCHORS, TABLE_NOTES)
