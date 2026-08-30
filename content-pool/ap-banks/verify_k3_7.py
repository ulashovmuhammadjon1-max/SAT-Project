"""Key audit for AP COMPARATIVE GOVERNMENT 3.7 Civil Rights and Civil Liberties.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
  DEM-1.C.1  protection of key civil liberties DIFFERS ACROSS THE SIX
  DEM-1.C.2  BOTH regime types constrain media TO PROTECT CITIZENS AND MAINTAIN
             ORDER; democratic regimes generally tolerate a HIGH DEGREE OF MEDIA
             FREEDOM
  DEM-1.C.3  stronger authoritarian regimes MONITOR AND RESTRICT MEDIA ACCESS
             further TO MAINTAIN POLITICAL CONTROL: .a the GREAT FIREWALL limiting
             POLITICAL CRITICISM ON SOCIAL MEDIA, .b IRANIAN COURTS suspending or
             revoking LICENSES after a JURY finds owners guilty of publishing
             ANTI-RELIGIOUS MATERIAL or MATERIAL DETRIMENTAL TO THE NATIONAL
             INTEREST, .c RUSSIA's NATIONALIZATION of most broadcast media with
             RIGID CONTROLS ON OPPOSITION NEWS SEGMENTS
  DEM-1.C.4  TRANSPARENCY is the OPEN CIRCULATION of information about government
             and policy making; authoritarian regimes TEND TO PREFER SECRET OR
             CLOSED PROCEEDINGS TO MAXIMIZE ORDER
  DEM-1.C.5  Russia is a COMPETITIVE AUTHORITARIAN REGIME OR ILLIBERAL DEMOCRACY,
             with MINIMAL CIVIL LIBERTY PROTECTIONS
  DEM-1.C.6  civil liberties data OVER TIME can place a regime on the
             AUTHORITARIAN/DEMOCRATIC SCALE

Supporting: PAU-1.C.1.e, IEF-1.B.3, PAU-3.G.1.i, LEG-1.C.3, DEM-2.B.4.a.

SHARING SENTENCES WITH TOPIC 1.3, WITHOUT SHARING QUESTIONS
-----------------------------------------------------------
Topic 1.3 draws on DEM-1.C.2 through DEM-1.C.6 for the democratic-authoritarian
scale, so this module deliberately keys the OTHER halves of the same sentences:
the stated PURPOSE of media constraint in both regime types (item 2), the internal
detail of each of the three country mechanisms (items 3-6, 19, 23-25), transparency
APPLIED rather than defined (items 8-9), the second label 'illiberal democracy'
(item 10), and the OVER-TIME method rather than the conclusion it supports (items
12-13, 20). The exporter's near-duplicate scan is what confirms this worked.

DATA ITEMS
----------
Three sets, eight items. The mechanism table carries a fourth row -- an independent
regulator enforcing a published accuracy code -- that matches NOTHING in
DEM-1.C.3, so items 23-25 cannot be answered by elimination alone. The transparency
table's three columns are three different ways information can circulate openly,
which is DEM-1.C.4's definition applied rather than restated.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k3_7

S2010 = "Civil liberties protection score, 2010 (0 to 100)"
S2020 = "Civil liberties protection score, 2020 (0 to 100)"
OUTLETS = "Independent news outlets operating in 2020"
MECH = "Mechanism used"
CAB = "Cabinet decisions published within a month (percent)"
FOI = "Freedom-of-information requests granted (percent)"
COMM = "Legislative committee sessions held in public (percent)"


def _lib(table):
    return {lab: (cg.cell(table, lab, S2010), cg.cell(table, lab, S2020), cg.cell(table, lab, OUTLETS))
            for lab in cg.labels(table)}


def q20(table, item):
    v = _lib(table)
    change = {lab: b - a for lab, (a, b, _) in v.items()}
    assert change["Country B"] == -22, f"the keyed fall recomputes to {change['Country B']}"
    assert abs(change["Country B"]) == max(abs(x) for x in change.values()), \
        "the keyed row must show the largest movement over the decade"
    assert v["Country B"][2] == min(x[2] for x in v.values()), "the keyed row must have the fewest independent outlets"
    assert change["Country A"] == 3 and change["Country C"] == -3, f"the other changes recompute to {change}"
    return "one row falls 22 points against changes of 3 and -3 elsewhere, and also has the fewest independent outlets"


def q21(table, item):
    v = _lib(table)
    a10, a20, outl = v["Country A"]
    assert a10 == max(x[0] for x in v.values()) and a20 == max(x[1] for x in v.values()), \
        "the keyed row must be highest in both years"
    assert a20 > a10 and a20 - a10 <= 5, "the keyed row must rise, and only slightly, for 'stable' to be fair"
    assert outl == max(x[2] for x in v.values()), "the keyed row must have the most independent outlets"
    return "one row is highest in both years, moves only 3 points, and has the most independent outlets"


def q22(table, item):
    v = _lib(table)
    change = {lab: b - a for lab, (a, b, _) in v.items()}
    biggest = max(abs(x) for x in change.values())
    assert biggest == 22, f"the largest change recomputes to {biggest}"
    assert 3 in [abs(x) for x in change.values()], "the 3 distractor must be another row's change"
    assert biggest - 3 == 19, "the 19 distractor must be the difference between two changes"
    assert v["Country A"][0] - v["Country B"][0] == 34, "the 34 distractor must be a same-year gap between two rows"
    assert max(x[1] for x in v.values()) == 81, "the 81 distractor must be the largest single score"
    return f"the three changes are {[change[l] for l in v]}, the largest being {biggest:.0f}, and every distractor is a real figure read differently"


def _mech(table):
    return {str(r[0]): str(r[1]) for r in table["rows"]}


def q23(table, item):
    v = _mech(table)
    assert "filtering" in v["Case 1"] and "political criticism on social media" in v["Case 1"], \
        f"the keyed row reads {v['Case 1']!r}"
    for lab in ("Case 2", "Case 3", "Case 4"):
        assert "filtering" not in v[lab], f"{lab} must not also describe filtering"
    assert "accuracy code" in v["Case 4"], \
        "the table must carry a row matching nothing in EK DEM-1.C.3, so elimination alone cannot answer these items"
    return "one row alone describes a filtering system limiting political criticism on social media, and a fourth row matches no framework example"


def q24(table, item):
    v = _mech(table)
    assert "courts" in v["Case 2"] and "jury" in v["Case 2"] and "licences" in v["Case 2"], \
        f"the keyed row reads {v['Case 2']!r}"
    for lab in ("Case 1", "Case 3", "Case 4"):
        assert "jury" not in v[lab], f"{lab} must not also involve a jury"
    return "one row alone involves courts, a jury finding and the suspension or revocation of licences"


def q25(table, item):
    v = _mech(table)
    assert "state ownership" in v["Case 3"] and "opposition news segments" in v["Case 3"], \
        f"the keyed row reads {v['Case 3']!r}"
    for lab in ("Case 1", "Case 2", "Case 4"):
        assert "state ownership" not in v[lab], f"{lab} must not also rest on state ownership"
    return "one row alone pairs state ownership of most broadcast outlets with control of opposition news segments"


def _trans(table):
    return {lab: (cg.cell(table, lab, CAB), cg.cell(table, lab, FOI), cg.cell(table, lab, COMM))
            for lab in cg.labels(table)}


def q26(table, item):
    v = _trans(table)
    d, e = v["Government D"], v["Government E"]
    for i in range(3):
        assert d[i] > e[i], f"the keyed row must lead on column {i + 1}"
        assert d[i] >= 70 and e[i] <= 15, "the contrast must be wide enough for 'most' and 'fewer than one in ten' to hold"
    return "one row is above 70 percent on all three measures of open circulation and the other below 15 on all three"


def q27(table, item):
    v = _trans(table)
    e = v["Government E"]
    mean = sum(e) / 3
    assert mean == 9, f"the keyed average recomputes to {mean}"
    assert sum(e) == 27, "the 27 distractor must be the sum rather than the average"
    assert 12 in e and 6 in e, "the 12 and 6 distractors must be individual figures from the same row"
    d = v["Government D"]
    assert round(sum(d) / 3) == 84, "the 84 distractor must be the other row's average, rounded"
    return f"the three figures {list(e)} average {mean:.0f}, and every distractor is the sum, a single figure, or the other row's average"


CLAIMS = [
 ("it differs across the six",
  "EK DEM-1.C.1 states that protection of key civil liberties differs across the six course countries, which is why the learning objective proceeds country by country rather than by a single rule."),
 ("to protect citizens and maintain order",
  "EK DEM-1.C.2 states that both democratic and authoritarian regimes impose constraints on the media to protect citizens and maintain order. The purpose clause applies to both types, which is why the presence of a constraint identifies neither."),
 ("limit political criticism on social media",
  "EK DEM-1.C.3.a describes the Chinese Communist Party's use of the Great Firewall to limit political criticism on social media. The rejected mechanisms are the framework's descriptions of Iran and Russia, plus two that appear nowhere in it."),
 ("jury finds owners guilty",
  "EK DEM-1.C.3.b describes the Iranian court's suspension or revocation of media licenses when a jury finds owners guilty of publishing anti-religious material or information detrimental to the national interest. The jury step and both grounds are the framework's."),
 ("nationalization of most broadcast media",
  "EK DEM-1.C.3.c describes the Russian government's nationalization of most broadcast media and rigid controls on opposition news segments. The rejected mechanisms belong to China and Iran or appear nowhere in the framework."),
 ("one through court-ordered licensing decisions",
  "EK DEM-1.C.3.a, .b and .c describe three different instruments: a firewall limiting political criticism on social media, courts suspending or revoking licences after a jury verdict, and nationalization of most broadcast media with control of opposition news segments."),
 ("monitor and restrict citizens' media access to a greater degree",
  "EK DEM-1.C.3 introduces its three examples with exactly this statement, adding that the purpose is to maintain political control. The comparison is one of degree, since EK DEM-1.C.2 has both regime types constraining media."),
 ("allows information about government and policy making to circulate openly",
  "EK DEM-1.C.4 defines a transparent government in these words. The rejected terms are EK LEG-1.A.1's legitimacy, EK PAU-1.A.4's sovereignty, EK PAU-2.A.1's federalism and EK PAU-1.C.5's consolidation."),
 ("authoritarian regimes tend to prefer secret or closed proceedings",
  "EK DEM-1.C.4 states that authoritarian regimes tend to prefer secret or closed proceedings to maximize order, having defined transparency as the open circulation of information. The word 'tend' keeps it a tendency rather than a rule."),
 ("illiberal democracy",
  "EK DEM-1.C.5 states that Russia is characterized as a competitive authoritarian regime or illiberal democracy, offering two labels for the same case. The rejected terms are separate types on EK PAU-1.B.3's list."),
 ("minimal civil liberty protections",
  "EK DEM-1.C.5 states that such a regime holds contested elections with limited degrees of competitiveness while providing minimal civil liberty protections and governmental transparency. The civil liberties clause is what ties the classification to this learning objective."),
 ("protect or restrict civil liberties over time",
  "EK DEM-1.C.6 states that comparing data showing the extent to which governments protect or restrict civil liberties over time can determine regime placement on an authoritarian/democratic scale. Party counts, chamber sizes and growth rates are not offered for this."),
 ("a single reading shows a level without showing direction",
  "EK DEM-1.C.6 specifies comparing data OVER TIME, EK PAU-1.B.1 treats the classification as a matter of degree along several indicators, and EK PAU-1.C.4 warns that democratization can stall or be reversed. Direction therefore matters as well as level."),
 ("protected civil rights and liberties",
  "EK PAU-1.C.1.e names protected civil rights and liberties among the outcomes democratization aims at over time, alongside universal suffrage, greater transparency, equal treatment and the establishment of the rule of law."),
 ("highlight violations of civil liberties protected under foundational documents",
  "EK IEF-1.B.3 states that across course countries, restrictions on NGOs and civil society tend to highlight violations of civil liberties protected under foundational documents. The restriction draws attention to the protection it cuts against."),
 ("protecting human and civil rights and liberties",
  "EK PAU-3.G.1.i names serving as the final court of appeals, protecting human and civil rights and liberties, and ruling on devolution disputes among the major functions of the United Kingdom's Supreme Court. The rejected functions belong to other bodies in the framework."),
 ("internal reform pressure from citizen protest groups and civil society",
  "EK LEG-1.C.3 states that such pressure can lead to the creation of new political institutions or policies to protect civil liberties, improve transparency, address election fairness and media bias, limit corruption and ensure equality under law."),
 ("reduces electoral competition and representation",
  "EK DEM-2.B.4.a states that Iran's Guardian Council excludes reform-minded candidates or those who do not support Islamic values, which limits the number of candidates and reduces electoral competition and representation."),
 ("court decisions about licences and the other through state ownership",
  "EK DEM-1.C.3.b describes Iranian courts suspending or revoking media licences after a jury verdict and EK DEM-1.C.3.c the Russian government's nationalization of most broadcast media with rigid controls on opposition news segments. The instruments differ in kind."),
 ("fell 22 points over the decade",
  "EK DEM-1.C.6 makes protection or restriction of civil liberties OVER TIME the measure that places a regime on the scale. Recomputed in q20 above: one row moves 22 points against 3 and -3 elsewhere and also has the fewest independent outlets, which EK DEM-1.C.3 connects to media restriction."),
 ("highest in both years, rose slightly",
  "EK DEM-1.C.6 makes protection over time the measure, so a claim of stable strong protection needs a high level in both years and little movement. Recomputed in q21 above, and EK DEM-1.C.2 connects a large independent press to the media freedom democratic regimes generally tolerate."),
 ("22 points",
  "Recomputed in q22 above from the three over-time changes. The alternatives are a smaller change, the difference between two changes, a same-year gap between two rows, and the largest single score."),
 ("national filtering system that limits political criticism on social media",
  "EK DEM-1.C.3.a describes the Great Firewall limiting political criticism on social media. Recomputed in q23 above, including that the table carries a fourth row matching nothing in EK DEM-1.C.3, so elimination alone cannot answer these items."),
 ("jury finds owners guilty of publishing certain material",
  "EK DEM-1.C.3.b describes the Iranian court's suspension or revocation of media licenses when a jury finds owners guilty of publishing anti-religious material or information detrimental to the national interest. Recomputed in q24 above: one row alone involves a jury."),
 ("state ownership of most broadcast outlets with rigid control of opposition news segments",
  "EK DEM-1.C.3.c describes nationalization of most broadcast media with rigid controls on opposition news segments. Recomputed in q25 above: one row alone rests on ownership together with control of opposition coverage."),
 ("publishes most cabinet decisions, grants most information requests",
  "EK DEM-1.C.4 defines a transparent government as one allowing information about government and policy making to circulate openly, and all three columns measure that circulation. Recomputed in q26 above. That closed proceedings may maximize order is the framework's account of a preference, not a form of transparency."),
 ("9 percent",
  "Recomputed in q27 above by averaging that row's three figures. The alternatives offer the sum instead of the average, two of the individual figures, and the other row's average."),
 ("prosecutions for criticism fell to near zero",
  "EK DEM-1.C.6 makes protection or restriction of civil liberties over time the relevant measure and EK DEM-1.C.2 connects media freedom to citizen control of the political agenda. Statute counts, turnout, ministries and speeches measure none of that."),
 ("brought into state ownership, online criticism was filtered",
  "EK DEM-1.C.3 makes monitoring and restricting media access the mark of stronger authoritarian regimes, EK DEM-1.C.3.a and .c give filtering and nationalization as its instances, and EK DEM-1.C.4 makes closed proceedings the authoritarian preference. The keyed finding combines all three."),
 ("stronger authoritarian regimes restrict media access further by named means",
  "EK DEM-1.C.1 supplies the variation across the six, EK DEM-1.C.2 the shared constraint and its purpose alongside democratic media freedom, EK DEM-1.C.3 the further restriction with three named instruments, EK DEM-1.C.4 transparency, and EK DEM-1.C.6 the over-time method."),
]

cg.check(k3_7, CLAIMS,
         table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27})
