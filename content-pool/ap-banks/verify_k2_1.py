"""Key audit for AP COMPARATIVE GOVERNMENT 2.1 Parliamentary, Presidential, and
Semi-Presidential Systems.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
  PAU-3.A.1  parliamentary systems, SUCH AS THE UNITED KINGDOM, combine the
             lawmaking and executive functions, letting the national legislature
             SELECT AND REMOVE the head of government and cabinet
  PAU-3.A.2  presidential systems, SUCH AS MEXICO AND NIGERIA, have a cabinet
             mostly responsible to the elected executive, legislative removal of
             cabinet members ONLY THROUGH IMPEACHMENT, separate FIXED-TERM popular
             elections for the legislature, and one leader as BOTH head of state
             and head of government
  PAU-3.A.3  semi-presidential systems, SUCH AS RUSSIA, have separate popular
             elections for president and legislature, a prime minister NOMINATED
             BY THE PRESIDENT AND APPROVED BY THE LEGISLATURE, and cabinet members
             accountable to BOTH

Country detail is held to PAU-3.C.2.c (Mexico), PAU-3.C.2.d (Nigeria),
PAU-3.C.2.e (Russia), PAU-3.C.2.f (the United Kingdom) and PAU-3.E.1.e (the Duma
confirming the prime minister).

THE ITEM THIS MODULE REFUSES TO WRITE
-------------------------------------
PAU-3.A assigns a system type to FOUR course countries. CHINA AND IRAN ARE NEVER
LABELLED parliamentary, presidential or semi-presidential anywhere in the
framework. An item asking a student to classify either would have no defensible
key, and the answer a student would reach from the existence of a presidential
office is wrong on the substance. No item here asks it; item 12 keys the absence
itself, which is the honest way to test the same knowledge. See
AP_COMP_GOV_CED.md note 2.

For the same reason no item offers 'parliamentary-hybrid' as an option for
Russia: PAU-3.E.1.e uses that phrase of Russia's LEGISLATURE while PAU-3.A.3
calls the system semi-presidential, and an item that put both on the same list
would be unanswerable (AP_COMP_GOV_CED.md note 3).

DATA ITEMS
----------
Items 20-22 use a hypothetical removals table -- the definitions are about WHO
CAN REMOVE WHOM, so counting removals is the natural way to test them from data.
Items 23-25 use a hypothetical classification matrix, one row per type. Both are
labelled hypothetical in the stems.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k2_1

BYLEG = "Cabinet ministers removed by the legislature, 2000-2020"
BYEXEC = "Cabinet ministers removed by the chief executive, 2000-2020"
HOGREM = "Heads of government removed by the legislature, 2000-2020"


def _cab(table):
    return {lab: (cg.cell(table, lab, BYLEG), cg.cell(table, lab, BYEXEC), cg.cell(table, lab, HOGREM))
            for lab in cg.labels(table)}


def q20(table, item):
    v = _cab(table)
    assert v["Case 1"][2] == 3, f"the keyed three removals recompute to {v['Case 1'][2]}"
    assert v["Case 1"][0] > 0, "the key also says some cabinet ministers were removed by the legislature"
    others = [lab for lab in v if lab != "Case 1"]
    assert all(v[lab][2] == 0 for lab in others), \
        "no other row may show the legislature removing a head of government"
    return "one row alone records the legislature removing heads of government, three of them, alongside cabinet removals"


def q21(table, item):
    v = _cab(table)
    assert v["Case 2"][0] == 0 and v["Case 2"][2] == 0, f"the keyed row must show no legislative removals; got {v['Case 2']}"
    assert v["Case 2"][1] == max(x[1] for x in v.values()), "the keyed row must show the most executive removals"
    assert any(v[lab][0] > 0 for lab in v), "the impeachment route must be visible somewhere, so 'never' is false"
    return "one row records no legislative removals at all alongside the largest number of executive removals, 24"


def q22(table, item):
    exec_total = sum(cg.col(table, BYEXEC))
    leg_total = sum(cg.col(table, BYLEG))
    assert exec_total == 53, f"the keyed total recomputes to {exec_total}"
    assert exec_total + leg_total == 60, "the 60 distractor must be the sum with the wrong column folded in"
    assert max(cg.col(table, BYEXEC)) == 24, "the 24 distractor must be the largest single row"
    vals = cg.col(table, BYEXEC)
    assert exec_total - min(vals) == 42 and vals[0] + vals[2] == 29, \
        "the 42 and 29 distractors must be partial sums of the same column"
    return f"the executive-removal column sums to {exec_total:.0f}, and every distractor is a partial or contaminated sum"


def _sel(table):
    return {str(r[0]): (str(r[1]), str(r[2]), str(r[3])) for r in table["rows"]}


def q23(table, item):
    v = _sel(table)
    hos, leg, hog = v["Case 4"]
    assert hos == "yes" and leg == "yes", "the keyed row needs separate popular elections for both"
    assert "nominated by the president" in hog and "approved by the legislature" in hog, \
        f"the keyed row's route to office is {hog!r}"
    assert not all(x == "yes" for x in (v["Case 5"][0], v["Case 5"][1])), \
        "no other row may hold both separate elections together with a nominate-and-approve route"
    assert "nominated" not in v["Case 6"][2], "the third row must use a different route to office"
    return "one row alone pairs separate popular elections for head of state and legislature with a nominate-and-approve prime minister"


def q24(table, item):
    v = _sel(table)
    hos, leg, hog = v["Case 5"]
    assert hos == "no", "the keyed row must not hold a separate popular election for the head of state"
    assert leg == "yes", "its legislature must still be popularly elected"
    assert "selected by the legislature" in hog and "remove" in hog, \
        f"the keyed row must place BOTH selection and removal in the legislature; it reads {hog!r}"
    for lab in ("Case 4", "Case 6"):
        assert "selected by the legislature" not in v[lab][2], f"{lab} must use a different route to office"
    return "one row alone puts both selection and removal of the head of government in the legislature and elects no head of state"


def q25(table, item):
    v = _sel(table)
    hos, leg, hog = v["Case 6"]
    assert hos == "yes" and leg == "yes", "the keyed row needs separate popular elections, which the type requires"
    assert "same person" in hog and "head of state and head of government" in hog, \
        f"the keyed row must fuse the two offices; it reads {hog!r}"
    for lab in ("Case 4", "Case 5"):
        assert "same person" not in v[lab][2], f"{lab} must not fuse the two offices"
    return "one row alone elects a single person as both head of state and head of government while still electing a legislature"


CLAIMS = [
 ("combines the lawmaking and executive functions",
  "EK PAU-3.A.1 states that parliamentary systems combine the lawmaking and executive functions, which allows the national legislature to select and remove the head of government and cabinet. Selection and removal by one body is what that combination makes possible."),
 ("the United Kingdom",
  "EK PAU-3.A.1 names the United Kingdom as its parliamentary example, EK PAU-3.A.2 names Mexico and Nigeria as presidential, and EK PAU-3.A.3 names Russia as semi-presidential. The remaining course countries are given no such label anywhere in the framework."),
 ("mostly responsible to the elected executive",
  "EK PAU-3.A.2 states that presidential systems feature a cabinet mostly responsible to the elected executive, with a legislature that can only remove cabinet members through impeachment. The rejected options describe EK PAU-3.A.1's and EK PAU-3.A.3's arrangements."),
 ("Mexico and Nigeria",
  "EK PAU-3.A.2 names Mexico and Nigeria as its presidential examples, and EK PAU-3.C.2.c and EK PAU-3.C.2.d confirm that each has an elected president serving as both head of state and head of government."),
 ("only through impeachment",
  "EK PAU-3.A.2 states that in presidential systems the legislature can only remove cabinet members through impeachment. That restriction is what makes the cabinet mostly responsible to the elected executive rather than to the legislature."),
 ("separate fixed-term popular elections",
  "EK PAU-3.A.2 specifies separate fixed-term popular elections for the national legislature. The fixed term is part of the definition, since it prevents the executive from timing a legislative election to suit itself."),
 ("both head of state and head of government",
  "EK PAU-3.A.2 specifies a top executive leader serving as both head of state and head of government, and EK PAU-3.C.2.c and EK PAU-3.C.2.d repeat that formula for Mexico and Nigeria. Splitting the two roles belongs to the other two types."),
 ("must be approved by the legislature",
  "EK PAU-3.A.3 states that semi-presidential systems hold separate popular elections for the president and the legislature and allow the president to nominate a prime minister who must be approved by the legislature. Both halves are needed to separate this type from the other two."),
 ("Russia",
  "EK PAU-3.A.3 names Russia as its semi-presidential example, and EK PAU-3.C.2.e matches the description with an elected president as head of state and commander in chief alongside a prime minister who is head of government."),
 ("nominates the prime minister, who must then be approved",
  "EK PAU-3.A.3 requires presidential nomination followed by legislative approval, and EK PAU-3.E.1.e adds that Russia's elected state Duma confirms the prime minister. Requiring both steps is what makes the arrangement a hybrid."),
 ("to both the president and the legislature",
  "EK PAU-3.A.3 states that cabinet members are held accountable by both the president and the legislature, which is the difference from EK PAU-3.A.2's cabinet, mostly responsible to the elected executive alone."),
 ("gives China and Iran no such label",
  "EK PAU-3.A.1 names the United Kingdom, EK PAU-3.A.2 Mexico and Nigeria, and EK PAU-3.A.3 Russia, and no essential knowledge statement assigns either remaining course country a type. Inferring a label from the existence of a presidential office is exactly what the framework's silence forbids."),
 ("a parliamentary system",
  "EK PAU-3.A.1 defines parliamentary systems by the combination of lawmaking and executive functions, which allows the national legislature to select and remove the head of government and cabinet. Selection and removal together are the distinguishing pair."),
 ("a presidential system",
  "EK PAU-3.A.2 defines presidential systems by a cabinet mostly responsible to the elected executive, legislative removal of cabinet members only by impeachment, separate fixed-term popular elections for the legislature, and one leader as head of state and head of government. All four appear in the scenario."),
 ("a semi-presidential system",
  "EK PAU-3.A.3 defines semi-presidential systems by separate popular elections for president and legislature, presidential nomination of a prime minister subject to legislative approval, and cabinet accountability to both. All three appear in the scenario."),
 ("formally appointed by a ceremonial head of state",
  "EK PAU-3.C.2.f describes the monarch formally appointing as prime minister the leader of the party or coalition holding the largest number of seats in the Commons, while EK PAU-3.C.2.c describes Mexico's elected president as both head of state and head of government. EK PAU-3.A.1 and EK PAU-3.A.2 make these the defining routes."),
 ("held accountable by both the president and the legislature",
  "EK PAU-3.A.2 makes a presidential cabinet mostly responsible to the elected executive with legislative removal only by impeachment, while EK PAU-3.A.3 makes a semi-presidential cabinet accountable to both branches. That is the main institutional consequence of the hybrid form."),
 ("confirmed by the elected chamber",
  "EK PAU-3.C.2.f has the monarch formally appointing the leader of the largest Commons party, while EK PAU-3.A.3 and EK PAU-3.E.1.e have the president nominating a prime minister whom the elected Duma confirms. The elected chamber matters in both, through different mechanisms."),
 ("one leader holds both roles",
  "EK PAU-3.A.2 specifies a top executive leader serving as both head of state and head of government, while EK PAU-3.C.2.f gives the United Kingdom a ceremonial head of state distinct from the prime minister. The two arrangements differ exactly on whether the roles are fused."),
 ("three heads of government as well as",
  "EK PAU-3.A.1 defines a parliamentary system by the legislature's power to select and remove the head of government and cabinet, so a record of the legislature actually removing heads of government is the distinguishing evidence. Recomputed in q20 above: only one row shows it."),
 ("no minister and no head of government while the chief executive",
  "EK PAU-3.A.2 makes the cabinet mostly responsible to the elected executive and allows legislative removal only through impeachment, a rare route. Recomputed in q21 above: one row shows the executive doing nearly all the removing and the legislature none, while another row shows impeachment does happen, so the 'never' option overstates the rule."),
 ("53",
  "Recomputed in q22 above by summing the executive-removal column. The distractors are the same column with a row omitted, the sum contaminated by the legislative column, the largest single row, and a two-row partial sum."),
 ("nominated by the president and approved by the legislature",
  "EK PAU-3.A.3 requires separate popular elections for president and legislature together with presidential nomination of a prime minister approved by the legislature. Recomputed in q23 above: only one row carries all three features."),
 ("selected and removable by the legislature",
  "EK PAU-3.A.1 defines a parliamentary system by the legislature selecting AND removing the head of government, and EK PAU-3.C.2.f shows that such a system still has a head of state, a ceremonial one. Recomputed in q24 above: only one row places both powers in the legislature."),
 ("the same elected person serves as head of state and head of government",
  "EK PAU-3.A.2 specifies a top executive leader serving as both head of state and head of government alongside separate popular elections for the legislature. Recomputed in q25 above: one row fuses the two offices while still electing a legislature, which is why the option denying legislative elections in this type is false."),
 ("answers to the elected executive alone or to both",
  "EK PAU-3.A.2 and EK PAU-3.A.3 both provide separate popular elections and both use the title president, so neither of those separates the types. The framework's difference is the cabinet's line of accountability."),
 ("owes office to the legislature alone or to a nomination",
  "EK PAU-3.A.1 gives the legislature the power to select and remove the head of government, while EK PAU-3.A.3 inserts a separately elected president who nominates and a legislature that approves. The route to office is where the two definitions part."),
 ("head of the civil service",
  "EK PAU-3.C.2.d describes Nigeria's elected president as both head of state and head of government, serving as chief executive, commander in chief and head of civil service, and able to approve domestic legislation and conduct foreign policy. EK PAU-3.A.2 names Nigeria presidential on exactly this basis."),
 ("leader of the bureaucracy",
  "EK PAU-3.C.2.c describes Mexico's elected president as head of state and head of government, commander in chief and leader of the bureaucracy, able to approve domestic legislation and lead foreign policy. EK PAU-3.A.2 names Mexico presidential, and the fusion of the two offices is what that definition turns on."),
 ("only four of the six course countries",
  "EK PAU-3.A.1, EK PAU-3.A.2 and EK PAU-3.A.3 differ on the route to the head of government's office and on the cabinet's lines of accountability, and each names its examples. No statement assigns a type to the remaining two course countries."),
]

cg.check(k2_1, CLAIMS, table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25})
