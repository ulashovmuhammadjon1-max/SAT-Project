"""Key audit for AP COMPARATIVE GOVERNMENT 1.7 Federal and Unitary Systems.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
  PAU-2.A.1  federal states like MEXICO, NIGERIA and RUSSIA divide power among
             levels of government to confer local autonomy in supplying SOCIAL AND
             EDUCATIONAL SERVICES while reserving powers for the national
             government; unitary states like CHINA, IRAN and the UNITED KINGDOM
             concentrate power nationally with more uniform policies and
             POTENTIALLY more efficient policy making
  PAU-2.A.2  the degree of centralization can change over time in BOTH federal and
             unitary states, often reflecting a response to internal and external
             actors including ETHNIC CLEAVAGES and the operations of SUPRANATIONAL
             ORGANIZATIONS AND OTHER COUNTRIES

Country items are held to PAU-1.D.1.e (United Kingdom devolution), DEM-2.B.5.c
(Russia's federal districts and president-approved gubernatorial lists),
DEM-2.B.3.b (Nigeria's federal distribution requirement), PAU-3.E.1.c (Mexico's
Senate approving federal intervention in state matters), PAU-3.G.1.e (Sharia
Courts in northern Nigeria under its system of federalism), PAU-3.G.1.i (the UK
Supreme Court ruling on devolution disputes) and LEG-1.B.4 (devolution's benefits
and costs in one statement).

THE TRAP THE TOPIC EXISTS TO SET
--------------------------------
The generalization a student arrives with -- authoritarian states centralize,
democracies federalize -- is refuted by the framework's own two lists: the
unitary group holds China and the United Kingdom, the federal group holds two
multiparty republics and the regime DEM-1.C.5 calls competitive authoritarian.
Items 4, 25 and 26 key that directly rather than leaving it implicit, and item 7
keys the related point that devolution did NOT reclassify the United Kingdom.

Item 14 keys the framework's hedge: unitary concentration brings 'POTENTIALLY
more efficient' policy making. Dropping 'potentially' turns a conditional into a
guarantee the statement does not make, and item 15 pairs it with LEG-1.B.4's
two-sided account of devolution.

DATA ITEMS
----------
Items 20-22 share a subnational-spending table and 23-24 a policy-area table,
both HYPOTHETICAL and labelled so. Item 22 is a check on what the data can
support: a spending ratio is not the framework's criterion for federal or
unitary, and the key says so.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k1_7

STRUCT = "Constitutional structure"
S00 = "Share of public spending decided by subnational governments, 2000"
S20 = "Share of public spending decided by subnational governments, 2020"
NAT = "Share of a hypothetical sample of states in which the area is decided nationally"
SUB = "Share in which it is decided subnationally"


def _struct(table):
    return {str(r[0]): str(r[1]) for r in table["rows"]}


def _delta(table):
    return {lab: cg.cell(table, lab, S20) - cg.cell(table, lab, S00) for lab in cg.labels(table)}


def q20(table, item):
    s, d = _struct(table), _delta(table)
    assert s["Country H"] == "federal" and s["Country J"] == "unitary", \
        f"the keyed pair must be one federal and one unitary; got {s}"
    assert d["Country H"] < 0, "the federal member of the pair must have centralized"
    assert d["Country J"] > 0, "the unitary member of the pair must have decentralized"
    assert s["Country K"] == "federal", "the rejected pair must be two states of the same structure"
    assert len({v for v in s.values()}) == 2, "the table must contain both structures for the claim to be illustrated"
    return "one federal row falls 12 points and one unitary row rises 13, so the pair shows the claim holding in both structures"


def q21(table, item):
    d = _delta(table)
    smallest = min(d, key=lambda k: abs(d[k]))
    assert smallest == "Country K", f"the smallest change belongs to {smallest}"
    assert abs(d["Country K"]) == 2, f"the keyed 2 points recomputes to {abs(d['Country K'])}"
    assert abs(d["Country H"]) == 12 and abs(d["Country J"]) == 13, \
        f"the rejected changes must read 12 and 13; got {d}"
    assert cg.cell(table, "Country K", S20) == 43, \
        "the 43 distractor must be that country's final share, so the trap is level against change"
    return "the three changes are 12, 13 and 2 percentage points, and the smallest is the key while 43 is that row's final level"


def q22(table, item):
    s, d = _struct(table), _delta(table)
    assert d["Country J"] > 0 and s["Country J"] == "unitary", \
        "the student's premise requires the unitary row's subnational share to have risen"
    assert STRUCT in table["headers"], \
        "the objection depends on the table naming the constitutional structure separately from the spending shares"
    assert s["Country J"] == "unitary", "the table still labels that row unitary after the rise, which is the point"
    return "the unitary row's subnational share does rise, by 13 points, while the table continues to label its structure unitary"


def _serv(table):
    return {str(r[0]): (cg.cell(table, r[0], NAT), cg.cell(table, r[0], SUB)) for r in table["rows"]}


def q23(table, item):
    v = _serv(table)
    for lab, (n, sub) in v.items():
        assert n + sub == 100, f"{lab} sums to {n + sub}, not 100"
    for lab in ("Defense", "Foreign affairs"):
        assert v[lab][0] == 100, f"{lab} must be national throughout the sample"
    for lab in ("School curriculum", "Local social services"):
        assert v[lab][1] > 50, f"{lab} must be majority subnational; it reads {v[lab][1]}"
    assert v["Defense"][1] < v["School curriculum"][1], \
        "'defense subnational more often than curriculum' must be false"
    return "the two service areas are majority subnational at 55 and 80 percent while defense and foreign affairs are national in the whole sample"


def q24(table, item):
    v = _serv(table)
    eligible = {lab: abs(n - sub) for lab, (n, sub) in v.items() if n < 100}
    assert set(eligible) == {"School curriculum", "Local social services"}, \
        f"the exclusion should leave exactly two rows; it left {sorted(eligible)}"
    assert eligible["Local social services"] == 60 and eligible["School curriculum"] == 10, \
        f"the two gaps recompute to {eligible}"
    assert max(eligible, key=eligible.get) == "Local social services", "the key must name the larger gap"
    assert v["Local social services"][1] == 80 and v["School curriculum"][1] == 55, \
        "the 80 and 55 distractors must be single column values rather than differences"
    return "excluding the rows that are national throughout leaves gaps of 60 and 10 points, and the distractors offer column values instead"


CLAIMS = [
 ("Federal: Mexico, Nigeria, Russia",
  "EK PAU-2.A.1 names Mexico, Nigeria and Russia as federal and China, Iran and the United Kingdom as unitary. The United Kingdom stays on the unitary list even though EK PAU-1.D.1.e records constitutional reforms devolving power to multiple parliaments."),
 ("confer a degree of local autonomy",
  "EK PAU-2.A.1 states that federal states divide power among different levels of government to confer a degree of local autonomy in supplying social and educational services, while also reserving powers for the national government. Uniformity is what the same sentence attributes to unitary states."),
 ("potentially more efficient policy making",
  "EK PAU-2.A.1 attributes more uniform policies and potentially more efficient policy making to unitary states. Local autonomy in social and educational services belongs to the federal half of the same statement, and national concentration does not abolish subnational administration."),
 ("one-party state and a long-established democracy",
  "EK PAU-2.A.1's unitary list holds China and the United Kingdom and its federal list holds Mexico, Nigeria and Russia, while EK DEM-1.C.5 calls Russia a competitive authoritarian regime or illiberal democracy. The two classifications cut across each other, so neither can be read off the other."),
 ("in both federal and unitary states",
  "EK PAU-2.A.2 states that the degree to which power is centralized or decentralized can change over time in both federal and unitary states. The framework's own instances are a unitary state devolving power and a federal state reasserting central control."),
 ("ethnic cleavages",
  "EK PAU-2.A.2 names ethnic cleavages and the operations of supranational organizations and other countries as the internal and external actors whose pressure such changes often reflect. The statement deliberately pairs one internal with two external sources."),
 ("without ceasing to be unitary",
  "EK PAU-2.A.1 still lists the United Kingdom among the unitary states and EK PAU-1.D.1.e records that the reforms devolved power to multiple parliaments and let the regime maintain stability. EK PAU-2.A.2 is what makes a change of degree possible inside an unchanged structure."),
 ("centralizing power under the national executive",
  "EK DEM-2.B.5.c presents the federal districts with presidential envoys and the president-approved gubernatorial lists as reasserting federal power under the Russian president, and EK PAU-2.A.1 lists Russia among the federal states. EK PAU-2.A.2 allows the degree of centralization to move within a federal structure."),
 ("system of federalism",
  "EK PAU-3.G.1.e states that under Nigeria's system of federalism, Islamic Sharia Courts have been established in the north, and EK PAU-2.A.1 lists Nigeria as federal. A legal order that differs by region is what dividing power among levels of government makes possible."),
 ("federal characteristic of the regime",
  "EK DEM-2.B.3.b states that the 25 percent in two-thirds of the states requirement reflects the federal characteristic of the Nigerian regime, and EK PAU-2.A.1 lists Nigeria among the federal states. The rule makes the constituent units part of how the presidency is won."),
 ("approving federal intervention in state matters",
  "EK PAU-3.E.1.c gives Mexico's Senate the unique power to confirm Supreme Court appointments, approve treaties, and approve federal intervention in state matters. The last is the point at which the national and state levels meet, which is what makes it a federal power."),
 ("ruling on devolution disputes",
  "EK PAU-3.G.1.i names serving as the final court of appeals, protecting human and civil rights and liberties, and ruling on devolution disputes among the United Kingdom Supreme Court's major functions. A unitary state that has devolved power still needs an authority to settle which level may act."),
 ("A unitary state has devolved power to regional parliaments while a federal state",
  "EK PAU-2.A.1 classifies the United Kingdom as unitary and Russia as federal, EK PAU-1.D.1.e records devolution in the first and EK DEM-2.B.5.c the reassertion of central power in the second. EK PAU-2.A.2 permits both movements inside unchanged structures, which is why the pairing runs in opposite directions."),
 ("makes more uniform policies and potentially more efficient policy making possible",
  "EK PAU-2.A.1 says unitary states concentrate power nationally with more uniform policies and POTENTIALLY more efficient policy making. The hedge is the framework's own, and removing it converts a conditional claim into a guarantee the statement does not make."),
 ("both opportunities for and obstacles",
  "EK LEG-1.B.4 lists policy innovation, local fit, competition, participation, a check on central power and better minority representation alongside contradictory policies, complicated implementation, interregional inequality, competition for resources and exacerbated tensions, in one statement. EK PAU-2.A.1's efficiency claim is hedged for the same reason."),
 ("matching policies to local needs",
  "EK LEG-1.B.4.a lists promoting policy innovation, matching policies to local needs, improving policies through competition, increasing political participation, checking central power and allowing better representation of religious, ethnic and minority groups. Uniformity belongs to EK PAU-2.A.1's unitary half instead."),
 ("contradictory policies across regions",
  "EK LEG-1.B.4.b lists creating contradictory policies, making implementation more complicated and inefficient, allowing inequality between regions, increasing competition for resources and exacerbating ethnic and local tensions. The framework states these alongside the benefits, so devolution is two-sided in its account."),
 ("concentrating power at the national level",
  "EK PAU-2.A.1 attributes to unitary states the concentration of power at the national level with more uniform policies. Identical curricula, structures and local powers set centrally are that uniformity, and the opposite of the local autonomy the same statement gives federal states."),
 ("dividing power among levels of government",
  "EK PAU-2.A.1 describes federal states dividing power among different levels of government to confer local autonomy in supplying social and educational services while reserving powers for the national government. Both halves of that description appear in the scenario."),
 ("federal state's subnational share fell while the unitary state's rose",
  "EK PAU-2.A.2 says the degree of centralization can change in BOTH federal and unitary states, so illustrating it needs one of each moving. Recomputed in q20 above: the federal row falls and the unitary row rises."),
 ("by 2 percentage points",
  "Recomputed in q21 above: the three changes are 12, 13 and 2 percentage points. The larger figure offered for the same country is its final share rather than its change, which is the trap the item sets."),
 ("how power is divided constitutionally",
  "EK PAU-2.A.1 defines the two structures by how power is divided among levels of government rather than by a spending ratio, and EK PAU-2.A.2 allows the degree of centralization to change within both. Recomputed in q22 above: the row's share does rise while the table still labels its structure unitary, which is the framework's own United Kingdom case."),
 ("the framework associates with local autonomy",
  "EK PAU-2.A.1 names social and educational services as what federal division of power confers local autonomy over, while reserving powers for the national government. Recomputed in q23 above: those two rows are majority subnational and the two classic national functions are unanimously national."),
 ("gap of 60 percentage points",
  "Recomputed in q24 above: excluding the rows decided nationally throughout leaves two, whose gaps are 60 and 10 percentage points. The larger figures offered against it are single column values rather than differences."),
 ("no implication about a state's place on the democratic-authoritarian scale",
  "EK PAU-2.A.1 places China, Iran and the United Kingdom in one unitary group while EK PAU-1.B.1 supplies a separate set of indicators for regime type. Two states can share the first classification and diverge on the second, which these two do."),
 ("compatible with more than one regime type",
  "EK PAU-2.A.1 groups Mexico, Nigeria and Russia as federal, EK PAU-1.D.1.c describes Nigeria and Mexico as multiparty republics, and EK DEM-1.C.5 characterizes Russia as competitive authoritarian. EK DEM-2.B.5.c shows a federal structure accommodating the reassertion of central power as well."),
 ("response to internal actors including ethnic cleavages",
  "EK PAU-2.A.2 states that changes in centralization in many cases reflect a state response to internal and external actors including ethnic cleavages, and EK LEG-1.B.4.a lists better representation of religious, ethnic and minority groups among devolution's benefits. A regional assembly for a concentrated minority is that response."),
 ("operations of a supranational organization",
  "EK PAU-2.A.2 names the operations of supranational organizations and other countries among the external actors whose influence such changes reflect, alongside internal ethnic cleavages. EK PAU-1.A.2's rules of access to power are untouched by a reallocation of regulatory authority, so no regime change is involved."),
 ("power to shape who holds regional office",
  "EK PAU-2.A.2 makes the degree of centralization the thing that moves, and EK DEM-2.B.5.c gives the framework's own instance of it, a national executive shaping who holds regional office. Counting units, relocating a legislature, a regional election result and treaty membership move no authority between levels."),
 ("shift over time in response to internal and external pressures",
  "EK PAU-2.A.1 supplies the classification and the purpose of each structure, and EK PAU-2.A.2 supplies the movement within it and the actors driving that movement. Holding both means treating the structure as the fixed thing and the degree of centralization as the moving one."),
]

cg.check(k1_7, CLAIMS, table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24})
