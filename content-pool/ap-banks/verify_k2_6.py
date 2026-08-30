"""Key audit for AP COMPARATIVE GOVERNMENT 2.6 Legislative Systems.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
  PAU-3.E.1.a  China: PARTY-CONTROLLED, UNICAMERAL; the constitution RECOGNIZES the
               National People's Congress as the government's most powerful
               institution, electing the president, approving the premier and
               legitimizing executive policies
  PAU-3.E.1.b  Iran: UNICAMERAL; the elected Majles approves legislation, oversees
               the budget and confirms Cabinet nominees, UNDER THE SUPERVISION of
               the Guardian Council for compatibility with Islam and Sharia law
  PAU-3.E.1.c  Mexico: BICAMERAL; the Chamber of Deputies approves legislation,
               levies taxes and VERIFIES OUTCOMES OF ELECTIONS; the elected Senate
               holds UNIQUE powers over Supreme Court appointments, treaties and
               federal intervention in state matters
  PAU-3.E.1.d  Nigeria: BICAMERAL, both chambers elected; BOTH approve legislation
               and the Senate holds UNIQUE impeachment and confirmation powers
  PAU-3.E.1.e  Russia: BICAMERAL; the elected Duma passes legislation and CONFIRMS
               THE PRIME MINISTER; an APPOINTED Federation Council approves budget
               legislation, treaties, judicial nominees and troop deployment
  PAU-3.E.1.f  United Kingdom: BICAMERAL; the elected Commons approves legislation
               and an APPOINTED House of Lords reviews and amends its bills,
               effectively delaying implementation as a power check

Composition is DEM-2.A.1.a-f, cited in each claim that uses it: indirect selection
in China; districts with a possible second round, no formal party structures and a
small number of 290 seats reserved for non-Muslim minorities in Iran; 300 district
plus 200 list deputies and 96 three-seat plus 32 list senators in Mexico;
population-weighted districts plus three senators from each of 36 states in
Nigeria; half districts and half proportional with a threshold in Russia;
first-past-the-post in the United Kingdom.

THE CHINA ITEM THAT COULD HAVE HAD TWO ANSWERS
----------------------------------------------
PAU-3.E.1.a says what China's CONSTITUTION RECOGNIZES; PAU-3.F.1.a says the
Politburo Standing Committee is the ACTUAL center of power. Item 2 asks the first
and item 28 asks the second, each saying which sense is meant. No item asks which
body is 'more powerful' without specifying, because the framework supports two
different answers to that question (AP_COMP_GOV_CED.md note 5).

DATA ITEMS
----------
Items 20-22 use a hypothetical seat table -- the framework gives real seat splits,
so a composition item can be answered from arithmetic plus one statement. Item 22
turns entirely on using the right denominator: two of its distractors divide the
correct numerator by another row's total. Items 23-25 use a hypothetical upper
chamber matrix in which two rows share 'appointed', so the powers column has to
do the work.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k2_6

SMD = "Seats filled in single-member districts"
PR = "Seats filled by proportional representation"
TOT = "Total seats"
HOW = "How members reach the chamber"
POWERS = "Powers the chamber holds"


def _seats(table):
    return {lab: (cg.cell(table, lab, SMD), cg.cell(table, lab, PR), cg.cell(table, lab, TOT))
            for lab in cg.labels(table)}


def q20(table, item):
    v = _seats(table)
    for lab, (d, p, t) in v.items():
        assert d + p == t, f"{lab}: {d} plus {p} should total {t}"
    assert v["Chamber 1"][:2] == (300, 200), f"the keyed row reads {v['Chamber 1'][:2]}"
    matches = [lab for lab, x in v.items() if x[:2] == (300, 200)]
    assert matches == ["Chamber 1"], f"exactly one row may carry both figures; got {matches}"
    return "one row alone carries 300 district seats and 200 proportional seats, and every row's two parts sum to its total"


def q21(table, item):
    v = _seats(table)
    halves = [lab for lab, (d, p, _) in v.items() if d == p]
    assert halves == ["Chamber 2"], f"exactly one row may split its seats evenly; got {halves}"
    assert v["Chamber 2"][0] * 2 == v["Chamber 2"][2], "the even split must account for the whole chamber"
    assert v["Chamber 1"][0] > v["Chamber 1"][1], "the rejected row must not be an even split"
    assert v["Chamber 3"][1] == 0, "the third row must fill no seats proportionally"
    return "one row alone divides its seats exactly in half between districts and proportional representation"


def q22(table, item):
    v = _seats(table)
    d, p, t = v["Chamber 1"]
    pct = p / t * 100
    assert pct == 40, f"the keyed share recomputes to {pct}"
    assert d / t * 100 == 60, "the 60 distractor must be the complementary district share"
    assert v["Chamber 2"][1] / v["Chamber 2"][2] * 100 == 50, "the 50 distractor must be another row's proportional share"
    assert abs(p / v["Chamber 2"][2] * 100 - 44) < 0.5, \
        "the 44 distractor must be the same numerator over the second row's total"
    assert abs(p / v["Chamber 3"][2] * 100 - 31) < 0.5, \
        "the 31 distractor must be the same numerator over the third row's total"
    return f"{p:.0f} of {t:.0f} is {pct:.0f} percent, and two distractors divide that numerator by the other rows' totals"


def _up(table):
    return {str(r[0]): (str(r[1]), str(r[2])) for r in table["rows"]}


def q23(table, item):
    v = _up(table)
    how, powers = v["Upper chamber X"]
    assert how == "elected", f"the keyed row must be elected; it reads {how!r}"
    for phrase in ("highest court", "treaties", "constituent unit"):
        assert phrase in powers, f"the keyed row's powers must include {phrase!r}; they read {powers!r}"
    elected = [lab for lab, (h, _) in v.items() if h == "elected"]
    assert elected == ["Upper chamber X"], f"exactly one row may be elected; got {elected}"
    return "one row alone is elected, and it carries all three of the powers the framework calls unique to that chamber"


def q24(table, item):
    v = _up(table)
    how, powers = v["Upper chamber Y"]
    assert how == "appointed", f"the keyed row must be appointed; it reads {how!r}"
    for phrase in ("budget legislation", "treaties", "judicial nominees", "troop deployment"):
        assert phrase in powers, f"the keyed row's powers must include {phrase!r}"
    appointed = [lab for lab, (h, _) in v.items() if h == "appointed"]
    assert len(appointed) == 2, "two rows must share 'appointed', so the powers column has to separate them"
    assert "troop deployment" not in v["Upper chamber Z"][1], "the other appointed row must not carry the same powers"
    return "two rows are appointed and only one of them carries the budget, treaty, judicial and troop powers"


def q25(table, item):
    v = _up(table)
    how, powers = v["Upper chamber Z"]
    assert how == "appointed", f"the keyed row must be appointed; it reads {how!r}"
    assert "reviewing and amending" in powers and "delaying" in powers, \
        f"the keyed row must review, amend and delay; it reads {powers!r}"
    for lab in ("Upper chamber X", "Upper chamber Y"):
        assert "delaying" not in v[lab][1], f"{lab} must not carry the delaying power"
    return "one row alone pairs appointment with reviewing, amending and delaying bills from the lower chamber"


CLAIMS = [
 ("China and Iran",
  "EK PAU-3.E.1.a calls China's system unicameral and EK PAU-3.E.1.b calls Iran's theocracy unicameral, while EK PAU-3.E.1.c through .f describe the remaining four course countries as bicameral."),
 ("legitimizes policies of the executive",
  "EK PAU-3.E.1.a states that China's constitution recognizes the National People's Congress as the government's most powerful institution that elects the president, approves the premier and legitimizes policies of the executive. EK PAU-3.F.1.a separately names the Politburo Standing Committee as the ACTUAL center of power, which is a different claim about a different thing."),
 ("indirectly, through a series of local and regional elections",
  "EK DEM-2.A.1.a states that the National People's Congress of China selects members indirectly through a series of local and regional elections. The rejected methods belong to the United Kingdom's Commons, Russia's Federation Council and Russia's Duma."),
 ("overseeing the budget, and confirming presidential nominees",
  "EK PAU-3.E.1.b states that Iran's elected Majles holds the power to approve legislation, oversee the budget and confirm presidential nominees to the Cabinet. The rejected lists describe China's National People's Congress, Russia's Federation Council, Mexico's Senate and the House of Lords."),
 ("Guardian Council, to ensure that laws are compatible",
  "EK PAU-3.E.1.b states that the Majles acts under the supervision of the Guardian Council to ensure compatibility with Islam and Sharia law, and EK PAU-3.F.1.d adds that the Guardian Council vets candidates and oversees the Majles to that end. EK PAU-3.F.1.c gives the Expediency Council a different role, resolving disputes between the two."),
 ("290 seats are reserved for non-Muslim minorities",
  "EK DEM-2.A.1.b states that Iran's Majles members are directly elected in single-member and multimember districts, that the body lacks formal political party structures, and that a small number of the 290 seats are reserved for non-Muslim minorities such as Christians, Jews and Zoroastrians."),
 ("levying taxes, and verifying outcomes of elections",
  "EK PAU-3.E.1.c states that Mexico's elected Chamber of Deputies approves legislation, levies taxes and verifies outcomes of elections. The rejected options are powers the same statement assigns to the Senate, or powers of Russia's Duma and the House of Lords."),
 ("appointments to the Supreme Court, approving treaties",
  "EK PAU-3.E.1.c gives Mexico's elected Senate the UNIQUE power to confirm presidential appointments to the Supreme Court, approve treaties and approve federal intervention in state matters. The rejected lists belong to the Chamber of Deputies, Nigeria's Senate, Russia's Federation Council and the House of Lords."),
 ("96 senators elected in three-seat constituencies",
  "EK DEM-2.A.1.c gives Mexico 300 deputies in single-member districts by plurality plus 200 by party list, and 96 senators in three-seat constituencies plus 32 by proportional representation. The half-and-half arrangement offered against it is Russia's Duma and the three-per-state arrangement is Nigeria's Senate."),
 ("unique impeachment and confirmation powers",
  "EK PAU-3.E.1.d states that both chambers of Nigeria's bicameral system approve legislation and that the Senate possesses unique impeachment and confirmation powers. The rejected descriptions belong to the United Kingdom, Mexico, Iran and Russia."),
 ("three members directly elected from each of the country's 36 states",
  "EK DEM-2.A.1.d states that Nigerian House members are directly elected in single-member districts with each state's number based on population size, and that the Senate has three members directly elected from each of Nigeria's 36 states. Both chambers are elected."),
 ("passing legislation and confirming the prime minister",
  "EK PAU-3.E.1.e states that Russia's elected state Duma passes legislation and confirms the prime minister, which is the approval step EK PAU-3.A.3's semi-presidential definition requires. The rejected lists belong to the Federation Council, China's National People's Congress, Mexico's Chamber of Deputies and the House of Lords."),
 ("appointed, and it approves budget legislation",
  "EK PAU-3.E.1.e describes an appointed Federation Council approving budget legislation, treaties, judicial nominees and troop deployment, and EK DEM-2.B.5.c adds that its appointments are made by regional governors and the regional legislature. Confirming the prime minister belongs to the elected Duma."),
 ("half through proportional representation with a threshold",
  "EK DEM-2.A.1.e states that changes to state Duma elections returned it to a system in which half the representatives are directly elected from single-member districts and the other half chosen through proportional representation with a threshold."),
 ("first-past-the-post rules",
  "EK PAU-3.E.1.f states that the United Kingdom's bicameral parliamentary system has an elected House of Commons that approves legislation, and EK DEM-2.A.1.f states that Commons members are directly elected under single-member district, first-past-the-post rules."),
 ("delaying implementation as a power check",
  "EK PAU-3.E.1.f states that the appointed House of Lords reviews and amends bills from the Commons, effectively delaying implementation as a power check. The rejected powers belong to Russia's two chambers and to Mexico's Chamber of Deputies."),
 ("Russia and the United Kingdom",
  "EK PAU-3.E.1.e calls Russia's Federation Council appointed and EK PAU-3.E.1.f calls the House of Lords appointed, while EK PAU-3.E.1.c and EK PAU-3.E.1.d describe Mexico's and Nigeria's Senates as elected. China and Iran have no upper chamber at all."),
 ("unique powers over Supreme Court appointments",
  "EK PAU-3.E.1.c gives Mexico's elected Senate unique power over Supreme Court appointments, treaties and federal intervention in state matters, and EK PAU-3.E.1.d gives Nigeria's elected Senate unique impeachment and confirmation powers. Troop deployment and bill delay belong to the two appointed chambers."),
 ("Mexico's Senate and Russia's Federation Council",
  "EK PAU-3.E.1.c gives Mexico's Senate the power to approve treaties and EK PAU-3.E.1.e gives Russia's Federation Council the same power alongside budget legislation, judicial nominees and troop deployment. No other chamber in the framework holds it."),
 ("300 district seats and 200 proportional seats",
  "EK DEM-2.A.1.c states that Mexico's Chamber of Deputies has 300 members elected in single-member districts by plurality and 200 more by a proportional representation party list system. Recomputed in q20 above: one row carries both figures and every row's parts sum to its total."),
 ("exactly half its seats in districts and half proportionally",
  "EK DEM-2.A.1.e states that half of Russia's state Duma is directly elected from single-member districts and the other half through proportional representation with a threshold. Recomputed in q21 above: only one row divides evenly, and the Duma is elected rather than appointed."),
 ("40 percent",
  "Recomputed in q22 above: that chamber's proportional seats over its OWN total. The distractors are the complementary district share, another row's proportional share, and the same numerator divided by each of the other two rows' totals, so the item turns on the denominator."),
 ("elected, with powers over appointments to the highest court",
  "EK PAU-3.E.1.c describes Mexico's ELECTED Senate as holding the unique power to confirm presidential appointments to the Supreme Court, approve treaties and approve federal intervention in state matters. Recomputed in q23 above: only one row is elected and carries all three."),
 ("appointed, with powers over budget legislation",
  "EK PAU-3.E.1.e describes an APPOINTED Federation Council approving budget legislation, treaties, judicial nominees and troop deployment. Recomputed in q24 above: two rows are appointed, so the powers column is what separates them."),
 ("reviewing and amending bills from the lower chamber and delaying their implementation",
  "EK PAU-3.E.1.f describes the APPOINTED House of Lords as reviewing and amending bills from the Commons, effectively delaying implementation as a power check. Recomputed in q25 above: only one row pairs appointment with that role."),
 ("approving the premier, while the other is described as confirming the prime minister",
  "EK PAU-3.E.1.a states that China's constitution recognizes the National People's Congress as electing the president and approving the premier, and EK PAU-3.E.1.e that Russia's elected Duma confirms the prime minister. Both chambers are elected, directly in Russia and indirectly in China under EK DEM-2.A.1.a."),
 ("Mexico's Chamber of Deputies",
  "EK PAU-3.E.1.c states that Mexico's elected Chamber of Deputies approves legislation, levies taxes and verifies outcomes of elections. No other legislative chamber in the framework is given that function."),
 ("the Politburo Standing Committee",
  "EK PAU-3.F.1.a states that China's Politburo Standing Committee is the actual center of power in the Chinese state, while EK PAU-3.E.1.a states only what the constitution RECOGNIZES about the National People's Congress. Both sentences are the framework's and they answer different questions."),
 ("several different routes",
  "EK DEM-2.A.1.a through .f describe indirect selection, districts with a possible second round, a mixed system, population-weighted districts, a half-and-half system and first-past-the-post, while EK PAU-3.E.1.e and .f identify two appointed upper chambers. No single route covers the six."),
 ("two of the four upper chambers are appointed",
  "EK PAU-3.E.1.a and .b describe unicameral systems, .c through .f bicameral ones, and .e and .f name the two appointed upper chambers. The powers listed differ chamber by chamber throughout the statement."),
]

cg.check(k2_6, CLAIMS, table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25})
