"""Key audit for AP COMPARATIVE GOVERNMENT 3.4 Political Values and Beliefs.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
  IEF-1.D.1  contrasting ideologies, INCLUDING RULE BY LAW AS OPPOSED TO RULE OF
             LAW, affect how a state treats its citizens and handles specific
             problems SUCH AS POLITICAL CORRUPTION
    .a  RULE BY LAW: the state USES THE LAW TO REINFORCE THE AUTHORITY OF THE
        STATE, associated with authoritarian regimes
    .b  RULE OF LAW: the state is LIMITED TO THE SAME RULES AS ITS CITIZENS,
        associated with democratic regimes
  IEF-1.D.2  beliefs about social and economic equality CAN BE HELD IN BOTH regime
             types, contrasted by the ENFORCEMENT RESPONSIBILITY TRANSFERRED TO
             GOVERNMENT and the CHOICE AFFORDED TO CITIZENS, ranging from LIMITED
             GOVERNMENTAL SOCIAL PROTECTIONS to a WELFARE STATE
  IEF-1.D.3  POST-MATERIALISM is social valuing of SELF-EXPRESSION AND QUALITY OF
             LIFE that presses governments on ENVIRONMENTAL ISSUES and SOCIAL AND
             ECONOMIC EQUALITY

Country instances are held to PAU-3.G.1.a (rule by law, a judiciary subservient to
a governing party) and PAU-3.G.1.i (common law enforcing the rule of law), with
PAU-1.B.1.a and PAU-1.C.3 in support.

THE DIFFERENCE-OF-DEGREE CLAIM
------------------------------
IEF-1.D.2 says beliefs about equality exist in BOTH regime types and differ in the
ARRANGEMENTS they produce. Items 8 and 19 key that; the intuitive reading, that
only one kind of regime's citizens hold such beliefs, is not the framework's. The
equality table is built so one pair of rows agrees on the belief and diverges
sharply on the provision, which is the claim in data.

DATA ITEMS
----------
Suggested skill 3.C for this topic is Data Analysis, so the module carries three
quantitative sets (8 items) rather than one: a corruption-prosecution record that
distinguishes rule by law from rule of law by WHO gets prosecuted, an equality
table separating belief from provision, and a thirty-year priority survey for
post-materialism. Item 27 adds only the two rows IEF-1.D.3 names as the objects of
post-materialist pressure, not the row naming the value itself.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k3_4

PROS = "Senior officials prosecuted for corruption, 2010-2020"
GOVP = "Of those, the share who were officials of the governing party (percent)"
OVER = "Share of prosecutions of opposition figures later overturned on appeal (percent)"
AGREE = "Share agreeing the government should guarantee everyone's basic needs (percent)"
SPEND = "Public social spending as a share of gross domestic product (percent)"
CHOICE = "Share saying individuals should choose and pay for their own health cover (percent)"
Y1990 = "Share in 1990 (percent)"
Y2020 = "Share in 2020 (percent)"

GROWTH = "Economic growth and material security"
SELFEX = "Self-expression and quality of life"
ENV = "Environmental protection"
EQUAL = "Social and economic equality"


def _rule(table):
    return {lab: (cg.cell(table, lab, PROS), cg.cell(table, lab, GOVP), cg.cell(table, lab, OVER))
            for lab in cg.labels(table)}


def q20(table, item):
    v = _rule(table)
    n, gov, over = v["Country J"]
    assert gov == min(x[1] for x in v.values()), "the keyed row must prosecute the fewest of its own party, proportionally"
    assert over == max(x[2] for x in v.values()), "the keyed row must have the most opposition prosecutions overturned"
    assert gov < 10 and over > 30, "the key calls the first 'almost never' and the second 'most', which the figures must bear"
    return "one row prosecutes governing-party officials in 4 percent of cases while 40 percent of its opposition prosecutions are overturned"


def q21(table, item):
    v = _rule(table)
    n, gov, over = v["Country H"]
    assert gov == max(x[1] for x in v.values()), "the keyed row must prosecute its own party at the highest rate"
    assert over == min(x[2] for x in v.values()), "the keyed row must have the fewest prosecutions overturned"
    mid = v["Country K"]
    assert min(x[1] for x in v.values()) < mid[1] < gov, \
        "the rejected middle row must genuinely fall between the others on the governing-party share"
    return "one row prosecutes governing-party officials at 45 percent and has only 4 percent of opposition prosecutions overturned"


def q22(table, item):
    v = _rule(table)
    n, gov, _ = v["Country H"]
    count = n * gov / 100
    assert count == 27, f"the keyed count recomputes to {count}"
    assert gov == 45 and n == 60 and n - count == 33, \
        "the 45, 60 and 33 distractors must be the percentage, the total, and the non-governing-party remainder"
    k_n, k_gov, _ = v["Country K"]
    assert k_n * k_gov / 100 == 9, "the 9 distractor must be the corresponding count for another row"
    return f"{gov:.0f} percent of {n:.0f} prosecutions is {count:.0f}, and every distractor is a real figure read from the wrong place"


def _eq(table):
    return {lab: (cg.cell(table, lab, AGREE), cg.cell(table, lab, SPEND), cg.cell(table, lab, CHOICE))
            for lab in cg.labels(table)}


def q23(table, item):
    v = _eq(table)
    pairs = [("Country L", "Country M"), ("Country L", "Country N"), ("Country M", "Country N")]
    gaps = {p: abs(v[p[0]][0] - v[p[1]][0]) for p in pairs}
    closest = min(gaps, key=gaps.get)
    assert closest == ("Country L", "Country M"), f"the closest pair on belief is {closest}"
    assert gaps[closest] == 4, f"the keyed pair's belief gap is {gaps[closest]}, not 'within a few points'"
    spend_gap = abs(v["Country L"][1] - v["Country M"][1])
    assert spend_gap == 18, f"the keyed pair's spending gap recomputes to {spend_gap}"
    assert gaps[("Country L", "Country N")] == 37, "the rejected pair's stated 37-point belief gap must be true"
    assert abs(v["Country M"][1] - v["Country N"][1]) == 3, "the other rejected pair's stated 3-point spending gap must be true"
    return f"the closest pair on belief differs by {gaps[closest]:.0f} points and by {spend_gap:.0f} points of social spending"


def q24(table, item):
    v = _eq(table)
    gap = abs(v["Country L"][1] - v["Country M"][1])
    assert gap == 18, f"the keyed gap recomputes to {gap}"
    assert abs(v["Country L"][1] - v["Country N"][1]) == 15 and abs(v["Country M"][1] - v["Country N"][1]) == 3, \
        "the 15 and 3 distractors must be the other pairs' spending gaps"
    assert abs(v["Country L"][0] - v["Country M"][0]) == 4, \
        "the 4 distractor must be the same pair's gap in the BELIEF column"
    assert max(x[1] for x in v.values()) == 29, "the 29 distractor must be the largest single spending figure"
    return f"the two rows closest on belief differ by {gap:.0f} points of social spending, and every distractor is a real figure from elsewhere"


def q25(table, item):
    v = _eq(table)
    assert v["Country M"][1] == min(x[1] for x in v.values()), "the keyed row must have the lowest social spending"
    assert v["Country M"][2] == max(x[2] for x in v.values()), "the keyed row must leave the most to individual choice"
    assert v["Country N"][0] == min(x[0] for x in v.values()), \
        "the rejected 'lowest agreement' option must name a different row, since belief is not the arrangement"
    return "one row is lowest on transferred responsibility and highest on individual choice, the two dimensions the framework names"


def _pm(table):
    return {str(r[0]): (cg.cell(table, r[0], Y1990), cg.cell(table, r[0], Y2020)) for r in table["rows"]}


def q26(table, item):
    v = _pm(table)
    assert sum(a for a, _ in v.values()) == 100 and sum(b for _, b in v.values()) == 100, "each column must sum to 100"
    assert v[SELFEX][1] > v[SELFEX][0], "the post-materialist value itself must rise"
    assert v[ENV][1] > v[ENV][0], "one object of post-materialist pressure must rise"
    assert v[GROWTH][1] < v[GROWTH][0], "the material priority must fall"
    assert v[EQUAL][1] < v[EQUAL][0], \
        "the other object must FALL, so the key cannot be read as 'everything the framework names rose'"
    return "self-expression rises 21 points and environmental protection 10 while material security falls 27 and equality falls 4"


def q27(table, item):
    v = _pm(table)
    total = v[ENV][1] + v[EQUAL][1]
    assert total == 27, f"the keyed total recomputes to {total}"
    assert v[ENV][1] + v[SELFEX][1] == 58, "the 58 distractor must add the value itself instead of the second object"
    assert v[SELFEX][1] == 39 and v[ENV][1] == 19, "the 39 and 19 distractors must be single 2020 rows"
    assert v[ENV][0] + v[EQUAL][0] == 21, "the 21 distractor must be the same two rows in the wrong year"
    return f"the two objects of post-materialist pressure total {total:.0f} in 2020, with each distractor a wrong row or a wrong year"


CLAIMS = [
 ("specific problems such as political corruption",
  "EK IEF-1.D.1 states that contrasting political ideologies, including rule by law as opposed to rule of law, affect how the state treats its citizens and deals with specific problems, such as political corruption."),
 ("uses the law to reinforce the authority of the state",
  "EK IEF-1.D.1.a defines rule by law as an arrangement in which the state uses the law to reinforce the authority of the state, and EK PAU-3.G.1.a applies the same phrase to a judicial system subservient to a governing party."),
 ("limited to the same rules as its citizens",
  "EK IEF-1.D.1.b defines rule of law as an arrangement in which the state is limited to the same rules as its citizens, and EK PAU-1.B.1.a adds that it means governance by law rather than by arbitrary decisions of individual officials."),
 ("authoritarian regimes tend to rely on rule by law",
  "EK IEF-1.D.1.a and EK IEF-1.D.1.b make exactly this pairing, each hedged with 'tend to'. Reversing it contradicts both statements."),
 ("using the law to reinforce its own authority",
  "EK IEF-1.D.1.a defines rule by law as the state using the law to reinforce its own authority, which a statute applied only against critics does. EK IEF-1.D.1.b's rule of law requires the state to be bound by the same rules, which the immunity of officials denies."),
 ("limited to the same rules as its citizens",
  "EK IEF-1.D.1.b defines rule of law as the state being limited to the same rules as its citizens, and applying one procurement statute identically to a minister and a contractor is that. A prosecution's effect on public confidence does not change which arrangement it illustrates."),
 ("one exempts the state from the rules it enforces",
  "EK IEF-1.D.1 names political corruption among the problems contrasting ideologies affect the handling of, and EK IEF-1.D.1.a and .b differ precisely on whether the state is bound by the rules it applies. EK PAU-1.C.3 adds that corruption inhibits democratization in either case."),
 ("both democratic and authoritarian regimes",
  "EK IEF-1.D.2 states that beliefs about social and economic equality can be held by citizens in both democratic and authoritarian regimes, then contrasts them by degree. This follows the pattern of EK DEM-1.C.2 and EK DEM-1.B.3."),
 ("enforcement responsibility transferred to the government",
  "EK IEF-1.D.2 names the amount of enforcement responsibility transferred to the government and the amount of choice afforded to citizens to protect their health and material well-being as its two dimensions of contrast."),
 ("from limited governmental social protections to a welfare state",
  "EK IEF-1.D.2 gives this as the range such beliefs can produce, which is a range of how much enforcement responsibility has been transferred. Rule by law and rule of law are EK IEF-1.D.1's range for a different question."),
 ("welfare state end",
  "EK IEF-1.D.2 makes the amount of enforcement responsibility transferred to government one of its two dimensions and names the welfare state as the upper end of the range. Universal provision funded from taxation transfers that responsibility."),
 ("limited governmental social protections end",
  "EK IEF-1.D.2 pairs the enforcement responsibility transferred to government with the choice afforded to citizens to protect their health and material well-being, and names limited governmental social protections as the lower end. The arrangement described transfers little and leaves much to choice."),
 ("social valuing of self-expression and quality of life",
  "EK IEF-1.D.3 defines post-materialism as social valuing of self-expression and quality of life. The rejected options are EK IEF-1.C.6.c's communism, EK IEF-1.C.6.b's neoliberalism, EK IEF-1.C.3's socialization and EK IEF-1.C.1's political culture."),
 ("environmental issues and social and economic equality",
  "EK IEF-1.D.3 states that post-materialism leads to applying pressure on governments to address environmental issues and social and economic equality, naming both objects in the same sentence."),
 ("post-materialism",
  "EK IEF-1.D.3 defines post-materialism as social valuing of self-expression and quality of life leading to pressure on governments over environmental issues and social and economic equality, which is exactly the combination the scenario describes."),
 ("whereas an ideology is a set of values and beliefs about the goals of government",
  "EK IEF-1.D.3 introduces post-materialism as a social valuing that generates pressure on governments, while EK IEF-1.C.6 defines a political ideology and names six, none of which is post-materialism. The two sit under different learning objectives."),
 ("subservient to the decisions of a governing party",
  "EK PAU-3.G.1.a states that rule by law, instead of rule of law, means the judicial system is subservient to the decisions of the Chinese Communist Party, which controls most judicial appointments. EK IEF-1.D.1.a is the general definition that description instantiates."),
 ("uses common law to enforce the rule of law",
  "EK PAU-3.G.1.i states that the United Kingdom's judicial system uses common law to enforce the rule of law, and EK IEF-1.D.1.b defines rule of law as the state being limited to the same rules as its citizens. The rejected descriptions are the framework's own accounts of China, Iran and Russia."),
 ("how much enforcement is transferred to government",
  "EK IEF-1.D.2 states that beliefs about social and economic equality can be held in both regime types and contrasts them by the enforcement responsibility transferred to government and the choice afforded to citizens. The difference is one of arrangement, not of who holds the belief."),
 ("almost never among those prosecuted",
  "EK IEF-1.D.1.a defines rule by law as the state using the law to reinforce its own authority, so the pattern is enforcement that spares the governing party and falls on opponents without surviving review. Recomputed in q20 above: one row shows both."),
 ("largest share of those prosecuted",
  "EK IEF-1.D.1.b defines rule of law as the state being limited to the same rules as its citizens, and EK PAU-1.B.1.a adds governance by law rather than by arbitrary decision. Recomputed in q21 above: one row prosecutes its own party at the highest rate with the fewest reversals."),
 ("27",
  "Recomputed in q22 above by applying the governing-party share to the row's total. Every distractor is a real figure read from the wrong place: the percentage itself, the remainder, the total, and another row's count."),
 ("within a few points of each other",
  "EK IEF-1.D.2 states that beliefs about equality can be held in both regime types but contrasted by the enforcement transferred to government. Recomputed in q23 above: the pair closest on belief, four points apart, differs by eighteen points of social spending."),
 ("18 percentage points",
  "Recomputed in q24 above from the two rows closest together on the belief column. The distractors are the other pairs' spending gaps, the same pair's gap in the belief column, and the largest single spending figure."),
 ("lowest social spending and the highest share saying individuals should choose",
  "EK IEF-1.D.2 pairs the enforcement responsibility transferred to government with the choice afforded to citizens, so the limited-protections end is lowest on the first and highest on the second. Recomputed in q25 above, including that the lowest agreement share belongs to a different row, since belief is not arrangement."),
 ("alongside a rise in environmental protection and a fall in economic growth",
  "EK IEF-1.D.3 defines post-materialism as social valuing of self-expression and quality of life that presses governments on environmental issues and social and economic equality. Recomputed in q26 above: the value rises, one object of the pressure rises, the material priority falls, and the other object falls, so the key cannot be read as 'everything named rose'."),
 ("27 percent",
  "EK IEF-1.D.3 names environmental issues and social and economic equality as the objects of post-materialist pressure, so those two rows are the ones to add. Recomputed in q27 above: one distractor adds the value itself instead of the second object, and another uses the wrong year."),
 ("prosecuted under the same statutes as private citizens",
  "EK IEF-1.D.1.b defines rule of law as the state being limited to the same rules as its citizens, so the evidence must show the state being bound. A larger statute book, an agency answering to the executive, more prosecutions of opponents, and a longer judicial term under unchanged appointment show nothing of the kind."),
 ("name self-expression and quality of life as their leading priority",
  "EK IEF-1.D.3 defines post-materialism as social valuing of self-expression and quality of life leading to pressure on governments over environmental issues and social and economic equality, so the evidence must include both the valuing and the pressure."),
 ("beliefs about equality exist in both regime types",
  "EK IEF-1.D.1 with its two sub-points supplies the rule-by-law and rule-of-law contrast and the corruption application, EK IEF-1.D.2 the cross-regime availability of equality beliefs and its two dimensions of contrast, and EK IEF-1.D.3 post-materialism and the pressure it produces."),
]

cg.check(k3_4, CLAIMS,
         table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27})
