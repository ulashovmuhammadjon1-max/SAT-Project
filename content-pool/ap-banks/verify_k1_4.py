"""Key audit for AP COMPARATIVE GOVERNMENT 1.4 Democratization.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
Learning objective PAU-1.C supplies almost everything:

  PAU-1.C.1  democratization is a transition FROM an authoritarian regime TO a
             democratic one; it can start or temporarily change direction; its
             aims over time are .a more competition, fairness and transparency in
             elections, .b increased citizen participation in policy-making
             processes, .c universal suffrage for adult citizens, .d greater
             governmental transparency, .e protected civil rights and liberties,
             .f equal treatment of citizens, .g establishment of the rule of law
  PAU-1.C.2  quotas, proportional representation, and changes in vote thresholds
             and district boundaries as the named rule adjustments
  PAU-1.C.3  corruption inhibits democratization; independent judiciaries reduce
             it while protecting individual liberties and civil rights
  PAU-1.C.4  democratization can stall or be reversed; election-rule and
             civil-liberties policy can SUPPORT OR IMPEDE it
  PAU-1.C.5  consolidation is maturing in election rules, separation of powers and
             protection of civil liberties, making reversion unlikely WITHOUT AN
             EXTERNAL SHOCK
  PAU-1.C.6  consensus among competing cultural and political groups makes the
             process sustainable

Country items are held to PAU-1.D.1.c (Nigeria out of military rule, Mexico out
of single-party dominance -- the framework's own 'respectively'), PAU-4.A.4 (the
rules facilitating Mexico's transition), PAU-4.A.3 (the rules ensuring one-party
dominance in Russia), DEM-2.A.1.c (gender quotas in Mexico's list system),
DEM-2.B.1 and DEM-2.B.4.b.

A QUESTION CUT AND REPLACED WHILE WRITING THIS FILE
---------------------------------------------------
A draft item asked what the elimination of EL DEDAZO ended. The framework names
the practice once, in PAU-4.A.4's list, and NEVER DEFINES IT -- so the key would
have rested on outside knowledge, which SOCIAL_BRIEF.md forbids for exactly this
subject. It was replaced by an item on privatizing state-owned corporations,
where the framework states the purpose in the same clause ('to decrease
patronage') and the key is therefore quoted rather than supplied.

Two further constraints observed throughout: no item asks how far along any real
country's democratization currently is, because that is a current-events fact
that dates; and item 15 keys the two-sided reading of PAU-1.C.4, since the
framework insists rule changes can impede as well as support.

DATA ITEMS
----------
Items 20-22 share a franchise-and-competitiveness table and items 23-24 a
quota-and-electoral-rule table. Both are HYPOTHETICAL and labelled so. Items 23
and 24 are a controlled comparison: one pair holds the electoral rule constant
and varies the quota, the other holds the quota constant and varies the rule,
which is checked below rather than asserted.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k1_4

V2000 = "Share of adult citizens eligible to vote, 2000"
V2020 = "Share of adult citizens eligible to vote, 2020"
COMP = "Elections judged competitive by observers, 2000-2020 (out of 5 held)"
WOMEN = "Women as a share of members"


def _delta(table):
    return {lab: cg.cell(table, lab, V2020) - cg.cell(table, lab, V2000)
            for lab in cg.labels(table)}


def q20(table, item):
    d = _delta(table)
    comp = {lab: cg.cell(table, lab, COMP) for lab in cg.labels(table)}
    assert d["Country A"] == 36, f"the keyed 36-point widening recomputes to {d['Country A']}"
    assert comp["Country A"] == 4, f"the keyed four competitive contests read as {comp['Country A']}"
    assert d["Country A"] == max(d.values()), "the keyed country must show the largest widening"
    assert d["Country B"] == 1 and d["Country C"] == -16, \
        f"the other two rows must be a 1-point rise and a 16-point fall; got {d}"
    assert cg.cell(table, "Country A", V2000) == min(cg.col(table, V2000)), \
        "the keyed country must start lowest, since democratization is a transition out of a restricted franchise"
    return "one row widens the franchise 36 points to 98 percent with 4 of 5 contests competitive, against a 1-point rise and a 16-point fall elsewhere"


def q21(table, item):
    d = _delta(table)
    comp = {lab: cg.cell(table, lab, COMP) for lab in cg.labels(table)}
    assert d["Country C"] == -16, f"the keyed narrowing recomputes to {d['Country C']}"
    assert comp["Country C"] == 1, f"the keyed single competitive contest reads as {comp['Country C']}"
    assert d["Country C"] == min(d.values()) and d["Country C"] < 0, \
        "only the keyed row may move backwards on the franchise"
    assert comp["Country C"] == min(comp.values()), "the keyed row must also be last on competitiveness"
    return "one row alone narrows the franchise, by 16 points, and is judged competitive in only 1 of 5 contests"


def q22(table, item):
    d = _delta(table)
    comp = {lab: cg.cell(table, lab, COMP) for lab in cg.labels(table)}
    assert abs(d["Country B"]) == min(abs(v) for v in d.values()), \
        "the student's premise requires this row to have changed least"
    assert cg.cell(table, "Country B", V2000) == max(cg.col(table, V2000)), \
        "the objection requires this row to start highest, leaving nothing for a transition to change"
    assert comp["Country B"] == max(comp.values()) == 5, \
        "the objection requires this row's contests to be competitive throughout"
    return "the least-changed row starts with the widest franchise and 5 of 5 competitive contests, so it has no authoritarian starting point"


def _qrow(table, label):
    i = cg.labels(table).index(label)
    return table["rows"][i]


def q23(table, item):
    r1, r2, r3 = (_qrow(table, f"Legislature {i}") for i in (1, 2, 3))
    assert r1[1] == r2[1], f"the keyed pair must share an electoral rule: {r1[1]!r} vs {r2[1]!r}"
    assert r1[2] != r2[2], "the keyed pair must differ on the quota"
    assert r1[1] != r3[1], "the rejected pair must differ on the electoral rule as well as on the quota"
    w1, w2 = cg.cell(table, "Legislature 1", WOMEN), cg.cell(table, "Legislature 2", WOMEN)
    assert w1 > w2, f"the quota row must hold the higher share; got {w1} and {w2}"
    return f"the keyed pair share the electoral rule and differ only in the quota, {w1:.0f} percent against {w2:.0f}"


def q24(table, item):
    r2, r3 = _qrow(table, "Legislature 2"), _qrow(table, "Legislature 3")
    assert r2[2] == r3[2] == "no", "the keyed pair must agree in having no quota"
    assert r2[1] != r3[1], "the keyed pair must differ in electoral rule"
    w2, w3 = cg.cell(table, "Legislature 2", WOMEN), cg.cell(table, "Legislature 3", WOMEN)
    assert w2 > w3, f"the proportional row must hold the higher share; got {w2} and {w3}"
    assert "proportional" in r2[1] and "single-member" in r3[1], \
        "the direction claimed matches EK DEM-2.B.1 only if the higher row is the proportional one"
    return f"the keyed pair agree in having no quota and differ in rule, {w2:.0f} percent under lists against {w3:.0f} under districts"


CLAIMS = [
 ("authoritarian regime to a democratic regime",
  "EK PAU-1.C.1 defines democratization as a transition from an authoritarian regime to a democratic regime. The maturing of a regime already democratic is democratic consolidation under EK PAU-1.C.5, and a change of governing party is a change of government under EK PAU-1.A.2."),
 ("temporarily change direction",
  "EK PAU-1.C.1 states that the process can start or temporarily change direction while aiming at its listed results over time, and EK PAU-1.C.4 adds that it can stall or be reversed. Both deny that the path is continuous or guaranteed."),
 ("universal suffrage",
  "EK PAU-1.C.1.c names universal suffrage for adult citizens among the outcomes democratization aims at, and extending the vote to every adult citizen is that outcome directly. The other aims listed concern information, law, consultation and liberties rather than eligibility to vote."),
 ("equal treatment of citizens",
  "EK PAU-1.C.1.f names equal treatment of citizens among democratization's aims, and legal disabilities attached to membership of a religious group are the plainest denial of it. Repealing them changes neither the franchise, the conduct of elections, nor the flow of information about policy making."),
 ("establishment of the rule of law",
  "EK PAU-1.C.1.g names establishment of the rule of law among democratization's aims and EK PAU-1.B.1.a describes it as governance by law rather than by arbitrary decisions of individual officials. Published criteria, written reasons and judicial review replace precisely that discretion."),
 ("increased citizen participation",
  "EK PAU-1.C.1.b names increased citizen participation in policy-making processes, which a consultation requirement creates between elections rather than at them. Voting eligibility, treatment before the courts and candidate competition are separate aims on the same list."),
 ("constituency by constituency",
  "EK PAU-1.C.1.a names more competition, fairness and transparency in elections, and both halves of the keyed pair change how an election is contested and how its result is reported. The rejected pairings serve suffrage and equal treatment, participation in policy making, the rule of law, and territorial administration."),
 ("greater governmental transparency",
  "EK PAU-1.C.1.d names greater governmental transparency among the aims and EK DEM-1.C.4 defines a transparent government as one letting information about government and policy making circulate openly. Publishing the reasoning behind decisions is that and alters no rule about voting, liberties, law or equal treatment."),
 ("replacing its federal structure",
  "EK PAU-1.C.1's list of seven aims does not include territorial structure, and EK PAU-2.A.1 treats federal and unitary organization as a separate classification whose unitary group holds both a clear democracy and a one-party state. The four rejected options are items .e, .c, .d and .g of the aims list."),
 ("vote thresholds and district boundaries",
  "EK PAU-1.C.2 names gender or cultural quotas, proportional representation, and changes in vote thresholds and district boundaries as the adjustments by which a democratic electoral system can accommodate ethnic diversity and increase multiparty competition."),
 ("Mexico",
  "EK DEM-2.A.1.c states that gender quotas in the party list system have helped increase female representation in Mexico's legislature. The framework attributes no comparable quota effect to any other course country, so no other name is supportable."),
 ("too small to win any district",
  "EK PAU-1.C.2 names proportional representation among the adjustments accommodating ethnic diversity, and EK DEM-2.B.1 supplies the mechanism, an increase in the number of parties represented and in the election of minority and women candidates. A minority dispersed across districts wins none of them yet can clear a list threshold."),
 ("inhibits democratization",
  "EK PAU-1.C.3 states that political corruption inhibits democratization and that independent judiciaries can reduce such corruption while protecting individual liberties and civil rights, making judicial independence do both jobs at once."),
 ("lacks the judicial independence",
  "EK PAU-1.C.3 assigns the corruption-reducing role specifically to INDEPENDENT judiciaries, and EK PAU-1.B.2 treats independence among branches as what stops one branch controlling all governmental power. Investigators and judges removable by the official they might investigate supply neither."),
 ("support or impede",
  "EK PAU-1.C.4 states that democratization can stall or be reversed and that policy changes regarding election rules and civil liberties can support or impede it. The framework is deliberately two-sided, so a claim that rule changes only ever help contradicts it."),
 ("separation of powers",
  "EK PAU-1.C.5 names election rules, separation of powers and protection of civil liberties as the three dimensions along which a democratic regime matures. The rejected lists describe statehood, economic performance, party arithmetic and terms of office."),
 ("transition out of an authoritarian regime",
  "EK PAU-1.C.1 defines democratization as the transition out of authoritarianism and EK PAU-1.C.5 defines consolidation as the maturing of a regime that is already democratic. The second presupposes the first has succeeded, so the two cannot be swapped."),
 ("improbable rather than impossible",
  "EK PAU-1.C.5 states that consolidation makes reversion to authoritarianism unlikely WITHOUT an external shock, which is a probability claim with a named exception rather than a guarantee. EK PAU-1.C.4's warning that democratization can be reversed is why the framework hedges."),
 ("consensus among competing cultural",
  "EK PAU-1.C.6 states that consensus among competing cultural and political groups about governmental policies associated with democratization and economic development can advance the process and make it sustainable. The agreement runs across rival groups, which is the opposite of excluding them."),
 ("widened by 36 percentage points",
  "EK PAU-1.C.1 makes democratization a transition out of an authoritarian regime aiming at universal suffrage and at more competition in elections. Recomputed in q20 above: one row alone starts lowest, widens most, and is judged competitive in four of five contests."),
 ("only one competitive election out of five",
  "EK PAU-1.C.4 states that democratization can stall or be reversed and that election-rule and civil-liberties policy can impede it. Recomputed in q21 above: one row alone moves backwards on the franchise and is also last on competitiveness."),
 ("no authoritarian starting point",
  "EK PAU-1.C.1 makes democratization a transition FROM an authoritarian regime, so a country already at the top of both measures has no such transition under way; EK PAU-1.C.5 would call its situation consolidation. Recomputed in q22 above from the least-changed row's starting values."),
 ("differ only in whether a quota applies",
  "EK PAU-1.C.2 lists quotas and proportional representation as two separate adjustments, so an inference about the quota must hold the electoral rule fixed. Recomputed in q23 above, and EK MPA-1.A.3's warning that numerous variables influence an outcome is the reason for the control."),
 ("neither of those two legislatures applies a quota",
  "Recomputed in q24 above: the pair agrees on having no quota and differs on the electoral rule, so the rule is what is left varying. EK DEM-2.B.1 predicts the direction, associating proportional representation with more women and minority candidates elected."),
 ("Nigeria transitioned away from military rule",
  "EK PAU-1.D.1.c states the transition of power in Nigeria and Mexico to multiparty republics following military rule and single-party dominance respectively. The framework's own 'respectively' fixes which country goes with which, and reversing them contradicts the sentence."),
 ("el dedazo",
  "EK PAU-4.A.4 names exactly these rules as facilitating Mexico's transition away from one-party dominance. The rejected options are the framework's descriptions of Russian and Iranian measures, which EK PAU-4.A.3 and EK DEM-2.B.4.a present as narrowing competition rather than widening it."),
 ("decreases patronage",
  "EK PAU-4.A.4 states the purpose inside the same clause, listing privatizing state-owned corporations to decrease patronage among the rules facilitating the transition. The key is therefore quoted from the framework rather than inferred, which is why this item replaced a drafted one about a term the framework names but never defines."),
 ("voter fraud",
  "EK DEM-2.B.4.b states that Mexico and Nigeria created independent election commissions as part of their democratic transitions to reduce voter fraud and manipulation and enhance electoral competition, which is EK PAU-1.C.1.a's electoral aim expressed as an institution."),
 ("raising party registration requirements",
  "EK PAU-4.A.3 lists increasing party registration requirements, restricting candidacy to legally registered parties and increasing threshold rules to limit ballot access among the rules ensuring one-party dominance in Russia, and EK PAU-1.C.4 says election-rule changes can impede democratization. The four rejected options are the framework's own aims and instruments."),
 ("ruled against the government",
  "EK PAU-1.C.5 defines consolidation by maturity in election rules, separation of powers and protection of civil liberties, and the keyed finding reports all three at once. Uninterrupted victory by one party bears on EK PAU-4.A.1's dominant party systems, while growth, treaty membership and popularity touch none of the three."),
]

cg.check(k1_4, CLAIMS, table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24})
