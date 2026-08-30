"""Key audit for AP COMPARATIVE GOVERNMENT 2.5 Removal of Executives.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
This topic has exactly ONE essential knowledge statement:

  PAU-3.D.1  across the course countries, executive leaders can be removed by the
             LEGISLATIVE BRANCH through DIFFERENT PROCEDURES that CONTROL THE
             ABUSE OF POWER

One sentence cannot carry thirty items, so the procedures come from the
statements that describe them -- PAU-3.A.1 (a parliamentary legislature selects
and removes), PAU-3.A.2 (a presidential legislature reaches cabinet members only
by impeachment), PAU-3.A.3 (dual accountability), PAU-3.B.2 (censure, a check
that is NOT a removal), PAU-3.C.2.a (China's leadership changes behind closed
doors), PAU-3.E.1.d (Nigeria's Senate's unique impeachment and confirmation
powers), PAU-1.D.4 (violent transitions in Iran and Nigeria) and LEG-1.B.2
(peaceful transfer reinforces legitimacy).

THE SCORING GUIDELINES AS A SOURCE
----------------------------------
Four country facts here come from the CED's OWN SCORING GUIDELINES for its sample
comparative-analysis question on legislative independence, and the claims say so
by name so a reader can check them:
  * Iran's Majles has power over the budget, CONFIRMS AND IMPEACHES MINISTERS, and
    may issue formal questions the government must answer
  * Nigeria's constitution gives the legislature the power to IMPEACH THE
    PRESIDENT, alongside oversight
  * Mexico's constitution gives the legislature the power to IMPEACH THE PRESIDENT
  * in the United Kingdom, Question Time is used to hold the prime minister
    accountable and open debate
These are printed in the same document as the framework, which is why they are
allowed here at all; nothing is keyed to outside knowledge.

WHAT IS NOT ASKED
-----------------
Neither the framework nor its scoring guidelines describes any procedure for
removing Iran's Supreme Leader. No item asserts that none exists, and no item
asks about it, because a key resting on the framework's silence would not be
defensible. Item 15 keys only the contrast the guidelines DO state: ministers in
one country, the president in the other.

DATA ITEMS
----------
Items 20-22 use a hypothetical route matrix and 23-25 a hypothetical impeachment
record. Item 23 asks for a SHARE where the distractors offer counts, and item 25
is the interpretive brake: PAU-3.D.1 presents these procedures as controlling the
abuse of power, so their USE is the mechanism working rather than evidence of
collapse.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k2_5

HOGROUTE = "Route by which the chamber may remove the head of government"
MINROUTE = "Route by which the chamber may reach an individual minister"
USED = "Times either route was used, 1990-2020"
ATT = "Impeachment attempts initiated, 1990-2020"
SUCC = "Attempts that removed the officeholder"
SCHED = "Executives leaving office at a scheduled date (percent)"


def _routes(table):
    return {str(r[0]): (str(r[1]), str(r[2])) for r in table["rows"]}


def q20(table, item):
    v = _routes(table)
    hog, minr = v["Case G"]
    assert "ordinary vote" in hog and "selected the officeholder" in hog, \
        f"the keyed row's head-of-government route reads {hog!r}"
    assert "same ordinary vote" in minr, f"the keyed row must reach ministers by the same route; it reads {minr!r}"
    for lab in ("Case H", "Case J"):
        assert "ordinary vote" not in v[lab][0], f"{lab} must not offer an ordinary-vote route"
    return "one row alone lets an ordinary vote of the selecting chamber remove the head of government and reach ministers by the same route"


def q21(table, item):
    v = _routes(table)
    hog, minr = v["Case H"]
    assert hog.strip() == "impeachment only", f"the keyed row's head-of-government route reads {hog!r}"
    assert minr.strip() == "impeachment only", f"the keyed row's minister route reads {minr!r}"
    assert v["Case J"][1] != "impeachment only", "the third row must offer a second route to ministers"
    assert "impeachment" in v["Case J"][1], \
        "impeachment must still be available there, so the 'no route to a minister' option is false"
    return "one row alone makes impeachment the sole route to both the head of government and individual ministers"


def q22(table, item):
    vals = cg.col(table, USED)
    total = sum(vals)
    assert total == 10, f"the keyed total recomputes to {total}"
    for wrong in (9, 7, 6, 4):
        assert wrong != total, f"distractor {wrong} equals the correct total"
    assert total - min(vals) == 9 and max(vals) == 6 and total - max(vals) == 4, \
        "each distractor should be a recognizable partial reading of the same column"
    return f"the usage column reads {vals} and sums to {total:.0f}, with every distractor a partial sum or a single row"


def _imp(table):
    return {lab: (cg.cell(table, lab, ATT), cg.cell(table, lab, SUCC), cg.cell(table, lab, SCHED))
            for lab in cg.labels(table)}


def q23(table, item):
    v = _imp(table)
    share = {lab: (s / a if a else 0) for lab, (a, s, _) in v.items()}
    assert max(share, key=share.get) == "Group 3", f"the largest share belongs to {max(share, key=share.get)}"
    assert v["Group 3"][0] == 14 and v["Group 3"][1] == 6, f"the keyed six of fourteen reads {v['Group 3'][:2]}"
    assert v["Group 1"][0] == 9 and v["Group 1"][1] == 2, "the rejected count options must quote the other group's real figures"
    assert share["Group 1"] < share["Group 3"], "the group with more attempts than successes must not lead on share"
    return f"the three shares are {[round(share[l], 2) for l in v]}, so the largest count and the largest share are not the same reading"


def q24(table, item):
    vals = cg.col(table, ATT)
    total = sum(vals)
    assert total == 25, f"the keyed total recomputes to {total}"
    assert total - min(vals) == 23, "the 23 distractor must be the total less the smallest group"
    assert sum(cg.col(table, SUCC)) == 8, "the 8 distractor must be the successful-removal column"
    assert max(vals) == 14, "the 14 distractor must be the largest single group"
    assert vals[0] + vals[1] == 11, "the 11 distractor must be a two-group partial sum"
    return f"the attempts column reads {vals} and sums to {total:.0f}, with each distractor a wrong column or partial sum"


def q25(table, item):
    v = _imp(table)
    most = max(v, key=lambda k: v[k][0])
    assert most == "Group 3", f"the group with the most attempts is {most}"
    assert v[most][2] > 50, "the objection requires that group still to show most executives leaving on schedule"
    assert v[most][2] == min(x[2] for x in v.values()), \
        "it should still be lowest on scheduled departures, or the student's premise would not arise"
    assert v[most][2] != 0, "'the fewest scheduled departures, at zero' must be false"
    return f"the group with the most attempts still records {v[most][2]:.0f} percent of executives leaving at a scheduled date"


CLAIMS = [
 ("the legislative branch",
  "EK PAU-3.D.1 states that across the course countries, executive leaders can be removed by the legislative branch through different procedures that control the abuse of power. Courts, armies, commissions and international bodies are treated elsewhere in the framework."),
 ("differ from country to country",
  "EK PAU-3.D.1 says the procedures are DIFFERENT across the course countries. That word is why the topic requires knowing which route belongs to which system rather than one general rule."),
 ("control the abuse of power",
  "EK PAU-3.D.1 attaches this purpose to the removal procedures, which places them alongside EK PAU-1.B.2's independence among branches as a device preventing one branch from controlling all governmental power."),
 ("the parliamentary type",
  "EK PAU-3.A.1 states that parliamentary systems combine the lawmaking and executive functions, allowing the national legislature to select and remove the head of government and cabinet. Selection and removal by the same chamber is the parliamentary route."),
 ("impeachment",
  "EK PAU-3.A.2 states that in presidential systems the legislature can only remove cabinet members through impeachment, which is what makes the cabinet mostly responsible to the elected executive rather than to the legislature."),
 ("both the president and the legislature",
  "EK PAU-3.A.3 states that in semi-presidential systems cabinet members are held accountable by both the president and the legislature, which distinguishes the type from EK PAU-3.A.2's presidential cabinet."),
 ("impeachment and confirmation powers",
  "EK PAU-3.E.1.d states that both chambers of Nigeria's National Assembly approve legislation and that the Senate possesses unique impeachment and confirmation powers. The rejected options describe Russia's Federation Council, a parliamentary legislature, the House of Lords and Iran's judiciary."),
 ("impeach the president, alongside oversight",
  "The CED's scoring guidelines for its sample comparative-analysis question accept that in Nigeria the constitution gives the legislature the power to impeach the president as well as oversight, used to remain independent and check the executive. EK PAU-3.E.1.d places that impeachment power in the Senate."),
 ("the power to impeach the president",
  "The CED's scoring guidelines accept that in Mexico the constitution gives the legislature the power to impeach the president and that it uses this power to check the executive branch. EK PAU-3.A.2 makes impeachment the presidential system's route and places Mexico in that type."),
 ("confirms and impeaches them",
  "The CED's scoring guidelines accept that Iran's Majles has power over the budget, confirms and impeaches ministers, and may issue formal questions the government must answer. EK PAU-3.E.1.b adds that the Majles confirms presidential nominees to the Cabinet."),
 ("formal questions that the government must answer",
  "The CED's scoring guidelines list this alongside the Majles's budget power and its confirmation and impeachment of ministers. EK PAU-3.C.2.b assigns the appointment of the head of the judiciary to the Supreme Leader, so that option is not available."),
 ("hold the prime minister accountable and open debate",
  "The CED's scoring guidelines accept that during Question Time members of the United Kingdom legislature question the prime minister and use that power to hold the prime minister accountable and open debate. EK PAU-3.B.2 lists questioning the executive among the parliamentary checks, and it is a check short of removal."),
 ("whereas removal ends the officeholder's tenure",
  "EK PAU-3.B.2 lists censuring cabinet ministers among the parliamentary checks, alongside refusal of legislation, questioning and election deadlines, while EK PAU-3.D.1 concerns procedures that remove executive leaders. A condemnation and a removal are different outcomes."),
 ("The constitution of each",
  "The CED's scoring guidelines accept the impeachment power for both countries' legislatures, and EK PAU-3.A.2 makes impeachment the presidential route while placing both countries in that type. Neither is described as removing a president by ordinary vote."),
 ("impeaching ministers and the other as impeaching the president",
  "The CED's scoring guidelines accept that Iran's Majles confirms and impeaches MINISTERS and that Nigeria's legislature may impeach the PRESIDENT. Nothing here rests on the framework's silence about removing Iran's Supreme Leader, which no statement addresses."),
 ("the chamber that selected the head of government may also remove",
  "EK PAU-3.A.1 gives a parliamentary legislature the power to select and remove the head of government, and EK PAU-3.A.2 restricts a presidential legislature to impeachment, with the CED's scoring guidelines confirming that power over Mexico's president. EK PAU-3.A.1 and EK PAU-3.A.2 place the two countries in those types."),
 ("behind closed doors",
  "EK PAU-3.C.2.a states that changes in China's top leadership are accomplished behind closed doors, EK PAU-1.D.1.a locates that regime's stability in the Communist Party's control, and EK PAU-3.F.1.a identifies the Politburo Standing Committee, not a legislature, as the actual center of power."),
 ("Iran and Nigeria",
  "EK PAU-1.D.4 states that governments also change by more violent means such as revolutions or coups, represented by such violent transitions in Iran and Nigeria, contrasting those with elections, appointments and lines of succession."),
 ("peaceful transfer of power is named",
  "EK LEG-1.B.2 names peaceful resolution of conflicts and peaceful transfer of power among the things that reinforce legitimacy, and EK LEG-1.A.1 defines legitimacy as whether constituents believe the government has the right to use power as it does. A removal conducted by the stated procedure shows the rules holding."),
 ("reach ministers by the same route",
  "EK PAU-3.A.1 states that a parliamentary legislature selects and removes the head of government AND cabinet. Recomputed in q20 above: only one row lets an ordinary vote of the selecting chamber do both."),
 ("impeachment is the only route to the head of government",
  "EK PAU-3.A.2 states that a presidential legislature can only remove cabinet members through impeachment. Recomputed in q21 above: only one row makes impeachment the sole route, and impeachment remains available in the third row, so the option denying any route is false."),
 ("10",
  "Recomputed in q22 above by summing the usage column. Every distractor is a partial sum of the same column or its largest single row."),
 ("six of fourteen attempts",
  "The question asks for a SHARE, so successful removals must be divided by attempts rather than compared as counts. Recomputed in q23 above, and EK PAU-3.D.1 presents removal procedures as controlling the abuse of power, so a procedure that reaches its object is that control operating."),
 ("25",
  "Recomputed in q24 above by summing the attempts column. The distractors are the total less the smallest group, the successful-removal column, the largest single group, and a two-group partial sum."),
 ("constitutional mechanism working",
  "EK PAU-3.D.1 states that executive leaders can be removed by the legislative branch through procedures that CONTROL THE ABUSE OF POWER, so using the procedure is the framework's picture of a check operating. Recomputed in q25 above: that group still records most executives leaving at a scheduled date."),
 ("have on occasion resulted in removal",
  "EK PAU-3.D.1 concerns procedures by which executive leaders CAN BE REMOVED, and the CED's scoring guidelines accept that Nigeria's and Mexico's legislatures USE their impeachment powers to check the executive. A written article never applied does not show the same thing."),
 ("depends continuously on the chamber's support",
  "EK PAU-3.A.1 states that combining the lawmaking and executive functions allows the national legislature to select and remove the head of government and cabinet. If withdrawal of support suffices and no separate proceeding is needed, tenure depends on that support continuously."),
 ("the presidential type",
  "EK PAU-3.A.2 gives presidential systems separate fixed-term popular elections and restricts the legislature to impeachment as its route to members of the executive. A formal proceeding on stated grounds against a separately elected officeholder is that arrangement."),
 ("constrains an officeholder while still in office",
  "EK PAU-3.D.1 attaches the phrase 'control the abuse of power' to these procedures and EK PAU-1.B.2 assigns the same function to independence among branches. EK PAU-1.D.4 makes clear that elections, appointments and succession are separate routes of change."),
 ("an ordinary vote where lawmaking and executive functions are combined",
  "EK PAU-3.D.1 supplies the general claim and the word 'different', EK PAU-3.A.1 the parliamentary route and EK PAU-3.A.2 the impeachment route, with EK PAU-3.A.3 adding dual accountability in the hybrid case. The summary keeps both the general claim and the variation it insists on."),
]

cg.check(k2_5, CLAIMS, table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25})
