"""Key audit for AP COMPARATIVE GOVERNMENT 2.3 Executive Systems.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
  PAU-3.C.1  executive institutions, including chief executives and cabinets,
             FORMULATE, IMPLEMENT AND ENFORCE policy
  PAU-3.C.2  titles, powers, structure and functions VARY across the six:
     .a China: president as commander in chief, chair of the Military Commission
        and party General Secretary; nominates the PREMIER, who is head of
        government over the civil service; leadership changes BEHIND CLOSED DOORS
     .b Iran: the SUPREME LEADER sets the agenda, is commander in chief, appoints
        top ministers, the Expediency Council, HALF the Guardian Council and the
        head of the judiciary; the PRESIDENT serves UP TO TWO 4-YEAR TERMS,
        oversees the civil service and conducts foreign policy
     .c Mexico: elected president as head of state AND head of government,
        commander in chief, leader of the bureaucracy, RESTRICTED TO ONE TERM
     .d Nigeria: elected president as head of state AND head of government, chief
        executive, commander in chief, head of civil service
     .e Russia: PRIME MINISTER as head of government over the civil service;
        elected PRESIDENT as head of state and commander in chief, appoints top
        ministers, conducts foreign policy, PRESIDES OVER THE DUMA under certain
        conditions
     .f United Kingdom: MONARCH ceremonially head of state, FORMALLY appointing as
        prime minister the leader of the largest Commons party or coalition; the
        PRIME MINISTER calls elections, sets the foreign policy agenda, and is DE
        FACTO commander in chief and chief executive over the civil service

WHAT IS NOT ASKED, AND WHY
--------------------------
The framework prints exactly TWO term-limit facts: Iran's president serves up to
two 4-year terms, and Mexico's president is restricted to one term. It gives no
figure for China, Nigeria, Russia or the United Kingdom, and no LENGTH for
Mexico's single term. No item asks for any of those, and the term-limit table's
rows are lettered cases rather than named countries precisely so that its term
lengths assert nothing about a real country (AP_COMP_GOV_CED.md note 7).

Half of the Guardian Council, never all of it -- PAU-3.C.2.b and PAU-3.G.1.b both
say half (AP_COMP_GOV_CED.md note 8). Item 11 keys it.

Item 28 keys the framework's own hedge, DE FACTO commander in chief, which marks
the same form-against-practice distinction PAU-3.E.1.a and PAU-3.F.1.a draw for
China's legislature.

DATA ITEMS
----------
Items 20-22 use a three-row matrix of hypothetical executive arrangements, one
row for each pattern the framework describes -- fused, ceremonial-plus-premier,
and split-with-elected-president. Items 23-25 use a hypothetical term-limit
table; item 25 is arithmetic on it rather than a fact about any country.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k2_3

HOS = "Head of state"
HOG = "Head of government"
ARMS = "Who commands the armed forces"
TERMS = "Maximum consecutive terms permitted for the chief executive"
LEN = "Length of one term, in years"
MAXY = "Maximum consecutive years in office"


def _exec(table):
    return {str(r[0]): (str(r[1]), str(r[2]), str(r[3])) for r in table["rows"]}


def q20(table, item):
    v = _exec(table)
    hos, hog, arms = v["Case A"]
    assert "elected president" in hos, f"the keyed row's head of state reads {hos!r}"
    assert "same elected president" in hog, f"the keyed row must fuse the two offices; it reads {hog!r}"
    assert "elected president" in arms, "the keyed row must give command to the same elected president"
    for lab in ("Case B", "Case C"):
        assert "same elected president" not in v[lab][1], f"{lab} must not fuse the two offices"
    return "one row alone makes a single elected president head of state, head of government and commander of the armed forces"


def q21(table, item):
    v = _exec(table)
    hos, hog, arms = v["Case B"]
    assert "monarch" in hos and "ceremonial" in hos, f"the keyed row's head of state reads {hos!r}"
    assert "largest party" in hog, f"the keyed row's head of government reads {hog!r}"
    assert "in fact rather than in form" in arms, \
        "the keyed row must carry the de facto qualification the framework uses"
    for lab in ("Case A", "Case C"):
        assert "monarch" not in v[lab][0], f"{lab} must not have a hereditary head of state"
    return "one row alone pairs a ceremonial hereditary head of state with a largest-party head of government commanding in fact rather than in form"


def q22(table, item):
    v = _exec(table)
    hos, hog, arms = v["Case C"]
    assert "elected president" in hos, f"the keyed row's head of state reads {hos!r}"
    assert "prime minister" in hog and "civil service" in hog, f"the keyed row's head of government reads {hog!r}"
    assert "elected president" in arms, "the keyed row must give command to the elected head of state"
    assert "prime minister" not in v["Case A"][1], "the fused row must not also contain a prime minister"
    return "one row alone separates an elected head of state who commands the armed forces from a prime minister running the civil service"


def q23(table, item):
    t = {lab: cg.cell(table, lab, TERMS) for lab in cg.labels(table)}
    assert t["Case D"] == 1, f"the keyed row permits {t['Case D']} terms, not one"
    assert [lab for lab, v in t.items() if v == 1] == ["Case D"], "exactly one row may permit a single term"
    assert all(v >= 1 for v in t.values()), "every row must state a maximum, so the 'no limit stated' reading fails"
    return "one row alone permits a single consecutive term, which is the arrangement the framework states for one course country"


def q24(table, item):
    t = {lab: (cg.cell(table, lab, TERMS), cg.cell(table, lab, LEN)) for lab in cg.labels(table)}
    assert t["Case E"] == (2, 4), f"the keyed row reads {t['Case E']}, not two terms of four years"
    matches = [lab for lab, v in t.items() if v == (2, 4)]
    assert matches == ["Case E"], f"exactly one row may carry both figures; got {matches}"
    assert all(v[1] > 0 for v in t.values()), "every row states a term length, so the 'no case states a length' option is false"
    return "one row alone carries both of the framework's figures for that country, two terms and four years each"


def q25(table, item):
    rows = {lab: (cg.cell(table, lab, TERMS), cg.cell(table, lab, LEN), cg.cell(table, lab, MAXY))
            for lab in cg.labels(table)}
    for lab, (n, ln, mx) in rows.items():
        assert n * ln == mx, f"{lab}: {n} terms of {ln} years should give {n * ln}, table says {mx}"
    top = max(rows, key=lambda k: rows[k][2])
    assert top == "Case F" and rows[top][2] == 15, f"the largest maximum is {top} at {rows[top][2]}"
    assert rows["Case E"][2] == 8 and rows["Case D"][2] == 6, "the rejected options must quote the other rows' products"
    return f"every row's terms times its length reproduces its final column, and the largest product is {rows[top][2]:.0f}"


CLAIMS = [
 ("formulate, implement and enforce policy",
  "EK PAU-3.C.1 states that governments have executive institutions, including chief executives and cabinets, that formulate, implement and enforce policy through different methods and agencies. Lawmaking, adjudication and electoral administration are assigned elsewhere in the framework."),
 ("chair of China's Military Commission",
  "EK PAU-3.C.2.a assigns China's president the roles of commander in chief, chair of China's Military Commission and General Secretary of the Chinese Communist party. The rejected descriptions belong to the premier, the United Kingdom's monarch, Mexico's president and Iran's Supreme Leader."),
 ("half of the Guardian Council",
  "EK PAU-3.C.2.b assigns the Supreme Leader the political agenda, command in chief, and the appointment of top ministers, the Expediency Council, HALF of the Guardian Council and the head of the judiciary. The rejected descriptions belong to Iran's elected president and to other countries' executives."),
 ("restricted to one term",
  "EK PAU-3.C.2.c describes Mexico's elected president as both head of state and head of government, commander in chief and leader of the bureaucracy, able to approve domestic legislation and lead foreign policy, and restricted to one term. That restriction is one of only two term-limit figures the framework prints."),
 ("head of the civil service",
  "EK PAU-3.C.2.d describes Nigeria's elected president as both head of state and head of government, serving as chief executive, commander in chief and head of civil service, and able to approve domestic legislation and conduct foreign policy."),
 ("prime minister is head of government and oversees the civil service",
  "EK PAU-3.C.2.e divides Russia's executive exactly this way, with the elected president as head of state and commander in chief appointing top ministers and conducting foreign policy. The split is what EK PAU-3.A.3's semi-presidential definition leads one to expect."),
 ("formally appoints as prime minister the leader of the party or coalition",
  "EK PAU-3.C.2.f states that the monarch serves ceremonially as head of state and FORMALLY appoints as prime minister the leader of the party or coalition holding the largest number of seats in the Commons. The seat count decides the outcome, which is what makes the role ceremonial."),
 ("the premier, nominated by the president",
  "EK PAU-3.C.2.a states that China's president nominates the premier, who in turn serves as head of government overseeing the civil service. The president holds a separate set of roles under the same statement."),
 ("behind closed doors",
  "EK PAU-3.C.2.a states that changes in China's top leadership are accomplished behind closed doors, and EK PAU-1.D.1.a locates that regime's stability in the Communist Party's control. A succession settled outside public institutions is settled by the party."),
 ("up to two four-year terms",
  "EK PAU-3.C.2.b states that Iran's president is elected for up to two 4-year terms, oversees the civil service and conducts foreign policy. Command of the armed forces and the political agenda belong to the Supreme Leader under the same statement."),
 ("half of it",
  "EK PAU-3.C.2.b states that the Supreme Leader appoints half of the Guardian Council, and EK PAU-3.G.1.b adds that the head of the judiciary can nominate the other half with approval by the Majles. The framework says half in both places."),
 ("presiding over it under certain conditions",
  "EK PAU-3.C.2.e states that Russia's elected president presides over the Duma under certain conditions, alongside being head of state and commander in chief. EK PAU-3.E.1.e describes the Duma as elected, so its members are not presidential appointees."),
 ("de facto commander in chief",
  "EK PAU-3.C.2.f assigns the prime minister the power to call elections, the foreign policy agenda, and the roles of de facto commander in chief and chief executive over the civil service, while the head of state remains the monarch."),
 ("serving ceremonially as head of state",
  "EK PAU-3.C.2.f states that the monarch serves ceremonially as head of state and formally appoints the prime minister. Every rejected role is assigned by the same statement to the prime minister."),
 ("Supreme Leader is commander in chief, whereas in Nigeria",
  "EK PAU-3.C.2.b makes Iran's Supreme Leader commander in chief while EK PAU-3.C.2.d makes Nigeria's elected president commander in chief as well as head of state and head of government. The contrast is between an unelected and an elected holder of the same function."),
 ("one-term restriction for only one of them",
  "EK PAU-3.C.2.c and EK PAU-3.C.2.d describe the two presidencies in almost identical terms and only the first adds the one-term restriction. The framework prints no term-limit figure for Nigeria, so asserting one would go beyond it."),
 ("separate popular elections",
  "EK PAU-3.C.2.a has China's president nominating a premier who oversees the civil service, and EK PAU-3.C.2.e has Russia's prime minister overseeing the civil service alongside an elected president who commands the armed forces. EK PAU-3.A.3 supplies Russia's separate popular elections, which China's arrangement has no counterpart to."),
 ("unelected office that is ceremonial",
  "EK PAU-3.C.2.b gives the Supreme Leader the political agenda, command in chief and a set of appointments, while EK PAU-3.C.2.f describes the monarch as ceremonial and appointing the prime minister only formally. Both offices are unelected, so the contrast has to be drawn on powers."),
 ("Mexico and Nigeria",
  "EK PAU-3.C.2.c and EK PAU-3.C.2.d both describe an elected president who is head of state AND head of government. Every rejected pair contains at least one country whose two offices are held by different people under EK PAU-3.C.2.a, .b, .e or .f."),
 ("one elected president is head of state",
  "EK PAU-3.C.2.c and EK PAU-3.C.2.d both fuse head of state, head of government and command of the armed forces in one elected officeholder. Recomputed in q20 above: only one row of the table does the same."),
 ("in fact rather than in form",
  "EK PAU-3.C.2.f pairs a ceremonial monarch as head of state with a prime minister drawn from the largest Commons party who is DE FACTO commander in chief. Recomputed in q21 above: only one row carries all three features, including the de facto qualification."),
 ("prime minister is head of government overseeing the civil service",
  "EK PAU-3.C.2.e gives Russia a prime minister as head of government over the civil service and an elected president as head of state and commander in chief. Recomputed in q22 above: only one row splits the roles that way while keeping the head of state elected."),
 ("permits one consecutive term",
  "EK PAU-3.C.2.c states that Mexico's president is restricted to one term. Recomputed in q23 above: exactly one row permits a single consecutive term, and every row states a maximum, so the option denying that the framework prints any limit is false."),
 ("two consecutive terms of four years each",
  "EK PAU-3.C.2.b states that Iran's president is elected for up to two 4-year terms, so both figures must match. Recomputed in q24 above: only one row carries both, and every row states a length."),
 ("three permitted terms multiplied",
  "Recomputed in q25 above: each row's permitted terms multiplied by its term length reproduces its final column, and the largest product is the answer. The alternatives quote a smaller row's product or a single term length."),
 ("Iran",
  "EK PAU-3.C.2.b gives Iran's unelected Supreme Leader the political agenda and command in chief while giving the elected president oversight of the civil service and the conduct of foreign policy. No other course country is described with that division."),
 ("China",
  "EK PAU-3.C.2.a describes China's president as commander in chief, chair of the Military Commission and General Secretary of the Communist party, nominating the premier who serves as head of government overseeing the civil service. The party office distinguishes this from Russia's arrangement."),
 ("formal position belongs to the head of state",
  "EK PAU-3.C.2.f describes the monarch as ceremonial head of state and the prime minister as DE FACTO commander in chief and chief executive over the civil service. The phrase separates where the form of the office sits from where the power is exercised, the same distinction EK PAU-3.E.1.a and EK PAU-3.F.1.a draw for China."),
 ("Iran's Supreme Leader",
  "EK PAU-3.C.2.b states that the Supreme Leader appoints the head of the judiciary, and EK PAU-3.G.1.b repeats it. EK PAU-3.G.1.d has Mexico's magistrates nominated by the president and approved by the Senate, and EK PAU-3.G.1.h has Russia's judges nominated by the president and approved by the Federation Council."),
 ("sometimes fused and sometimes separate",
  "EK PAU-3.C.1 supplies the common function and EK PAU-3.C.2 opens by stating that titles, powers, structure and functions vary across the six countries. EK PAU-3.C.2.c and .d fuse the two top offices while .a, .b, .e and .f separate them, so neither uniform claim survives."),
]

cg.check(k2_3, CLAIMS, table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25})
