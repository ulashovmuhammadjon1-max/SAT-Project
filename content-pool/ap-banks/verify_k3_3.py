"""Key audit for AP COMPARATIVE GOVERNMENT 3.3 Political Ideologies.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
EK IEF-1.C.6 defines a political ideology as a set of values and beliefs about the
GOALS OF GOVERNMENT, PUBLIC POLICY, OR POLITICS, and then defines six of them
outright. Because the framework supplies the definitions verbatim, every key in
this module is a quotation rather than an interpretation:
  .a individualism -- individual CIVIL LIBERTIES AND FREEDOM OVER GOVERNMENTAL
     RESTRICTIONS
  .b neoliberalism -- LIMITED GOVERNMENTAL INTERVENTION in the economy and society;
     PRIVATIZATION, FREE TRADE, DEREGULATION, ELIMINATION OF STATE SUBSIDIES
  .c communism -- ABOLITION OF PRIVATE PROPERTY with NEAR TOTAL governmental
     control of the economy
  .d socialism -- REDUCTION OF INCOME DISPARITIES and NATIONALIZATION OF MAJOR
     PRIVATE INDUSTRIES
  .e fascism -- EXTREME NATIONALIST, favoring AUTHORITARIAN RULE and the rights of
     the ETHNIC MAJORITY over ETHNIC MINORITIES AND THE POLITICAL OPPOSITION
  .f populism -- the INTERESTS AND RIGHTS OF THE COMMON PEOPLE OVER THOSE OF THE
     ELITES

THE PAIR MOST OFTEN COLLAPSED
-----------------------------
Communism and socialism. The framework separates them precisely: .c ABOLISHES
private property and takes NEAR TOTAL control; .d nationalizes MAJOR PRIVATE
INDUSTRIES and reduces income disparities, which leaves private property standing.
Items 4, 5, 14, 20 and 21 all depend on holding that line, and each of them offers
the other definition as its leading distractor rather than as filler.

WHAT NO ITEM DOES
-----------------
Assign one of the six to a course country. IEF-1.C.6 defines them and attaches
none to any of the six countries, so 'which ideology does country X hold' would
have no defensible key. Item 30 keys that absence as part of its summary.

DATA ITEMS
----------
Items 20-22 use three hypothetical platforms written from IEF-1.C.6.b, .c and .d,
so telling them apart IS the framework's distinction. Items 23-25 use a survey
whose four rows quote IEF-1.C.6.a, .b, .d and .f, both columns summing to 100;
item 23 turns on a SIGNED change, since the largest absolute movement in the table
belongs to a row that falls rather than rises.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k3_3

OWN = "Position on ownership of major industry"
DIST = "Position on the distribution of income"
CF = "Share of respondents in Country F (percent)"
CG = "Share of respondents in Country G (percent)"

LIB = "Individual civil liberties and freedom over governmental restrictions"
LIM = "Limited governmental intervention in the economy and society"
NAT = "Reduction of income disparities and nationalization of major industries"
POP = "The interests and rights of the common people over those of the elites"


def _plat(table):
    return {str(r[0]): (str(r[1]), str(r[2])) for r in table["rows"]}


def q20(table, item):
    v = _plat(table)
    own, dist = v["Platform 1"]
    assert "abolish private property" in own and "near total government control" in own, \
        f"the keyed row reads {own!r}"
    for lab in ("Platform 2", "Platform 3"):
        assert "abolish private property" not in v[lab][0], f"{lab} must not also abolish private property"
    assert "private hands" in v["Platform 2"][0], \
        "the nearest rival must expressly leave some property private, which is what separates the two definitions"
    return "one row alone abolishes private property and takes near total control, while its nearest rival leaves smaller firms private"


def q21(table, item):
    v = _plat(table)
    own, dist = v["Platform 2"]
    assert "nationalize major private industries" in own and "private hands" in own, f"the keyed row reads {own!r}"
    assert "reduce income disparities" in dist, f"the keyed row's distribution position reads {dist!r}"
    assert "abolish private property" in v["Platform 1"][0], \
        "the rejected row must be the communism platform, so the two definitions are genuinely in play"
    return "one row nationalizes major industries and reduces income disparities while leaving smaller firms private"


def q22(table, item):
    v = _plat(table)
    own, dist = v["Platform 3"]
    for phrase in ("privatize", "subsidies", "deregulate"):
        assert phrase in own, f"the keyed row must include {phrase!r}; it reads {own!r}"
    for lab in ("Platform 1", "Platform 2"):
        assert "privatize" not in v[lab][0], f"{lab} must not also privatize"
    return "one row alone privatizes, ends subsidies and deregulates -- three of the four policies the framework names"


def _supp(table):
    return {str(r[0]): (cg.cell(table, r[0], CF), cg.cell(table, r[0], CG)) for r in table["rows"]}


def q23(table, item):
    v = _supp(table)
    change = {lab: g - f for lab, (f, g) in v.items()}
    assert max(change, key=change.get) == POP, f"the largest rise belongs to {max(change, key=change.get)}"
    assert change[POP] == 16 and change[NAT] == 11, f"the two rises recompute to {change[POP]} and {change[NAT]}"
    assert change[LIB] == -19 and change[LIM] == -8, f"the two falls recompute to {change[LIB]} and {change[LIM]}"
    biggest_abs = max(change, key=lambda k: abs(change[k]))
    assert biggest_abs != POP and change[biggest_abs] < 0, \
        "the largest ABSOLUTE movement must belong to a falling row, which is what makes the signed reading necessary"
    return f"the four signed changes are {[change[l] for l in v]}, and the largest absolute movement is a fall rather than a rise"


def q24(table, item):
    v = _supp(table)
    f_total = v[LIB][0] + v[LIM][0]
    g_total = v[LIB][1] + v[LIM][1]
    assert (f_total, g_total) == (60, 33), f"the two totals recompute to {f_total} and {g_total}"
    assert f_total > g_total, "the keyed country must hold the larger combined share"
    assert max(x[1] for x in v.values()) > max(x[0] for x in v.values()), \
        "the rejected 'largest single share' option must state something true, so only its relevance fails"
    return f"the two limiting-government rows total {f_total:.0f} in one column and {g_total:.0f} in the other"


def q25(table, item):
    v = _supp(table)
    top = max(v, key=lambda k: v[k][1])
    assert top == POP, f"the leading row in that column is {top}"
    assert "common people" in top and "elites" in top, \
        "the leading row must quote the framework's populism definition, which is what the key identifies"
    labels = list(v)
    assert not any("abolition of private property" in lab for lab in labels), \
        "no row may state the communism definition, so that distractor is unavailable from the table"
    return "the leading row in the second column quotes the common-people-against-elites definition word for word"


CLAIMS = [
 ("goals of government, public policy, or politics",
  "EK IEF-1.C.6 defines a political ideology as a set of values and beliefs about the goals of government, public policy, or politics. The rejected options are EK IEF-1.C.1's political culture, EK PAU-1.A.2's regime, EK IEF-1.C.3's socialization and EK IEF-1.A.1's civil society."),
 ("individual civil liberties and freedom over governmental restrictions",
  "EK IEF-1.C.6.a defines individualism in exactly these words. The rejected options are the framework's own definitions of neoliberalism, communism, socialism and populism."),
 ("privatization, free trade, deregulation",
  "EK IEF-1.C.6.b defines neoliberalism as belief in limited governmental intervention in the economy and society and names privatization, free trade, deregulation and the elimination of state subsidies as the policies it supports."),
 ("abolition of private property with near total governmental control",
  "EK IEF-1.C.6.c defines communism in exactly these words. The leading distractor is EK IEF-1.C.6.d's socialism, which nationalizes major industries without abolishing private property."),
 ("reduction of income disparities and the nationalization",
  "EK IEF-1.C.6.d defines socialism as belief in the reduction of income disparities and the nationalization of major private industries. The leading distractor is EK IEF-1.C.6.c's communism, which goes further by abolishing private property."),
 ("ethnic minorities and the political opposition",
  "EK IEF-1.C.6.e defines fascism as an extreme nationalist ideology favoring authoritarian rule and the rights of the ethnic majority over that of ethnic minorities and the political opposition. Both clauses are the framework's."),
 ("interests and rights of the common people over those of the elites",
  "EK IEF-1.C.6.f defines populism as a political philosophy supporting the interests and rights of the common people over that of the elites, and says nothing about the ownership of industry."),
 ("individualism",
  "EK IEF-1.C.6.a defines individualism as belief in individual civil liberties and freedom over governmental restrictions, which is what the campaign asserts. The other five are defined by ownership, distribution, nationhood or the common people."),
 ("neoliberalism",
  "EK IEF-1.C.6.b names privatization, free trade, deregulation and the elimination of state subsidies as neoliberalism's policies, and the programme is all four. EK IEF-1.C.6.a's individualism concerns civil liberties rather than economic policy."),
 ("communism",
  "EK IEF-1.C.6.c defines communism as belief in the abolition of private property with near total governmental control of the economy. EK IEF-1.C.6.d's socialism nationalizes major private industries without abolishing private property."),
 ("socialism",
  "EK IEF-1.C.6.d defines socialism as belief in the reduction of income disparities and the nationalization of major private industries, and the platform does both while leaving most property private. That is what separates it from EK IEF-1.C.6.c's communism."),
 ("fascism",
  "EK IEF-1.C.6.e defines fascism as an extreme nationalist ideology favoring authoritarian rule and the rights of the ethnic majority over those of ethnic minorities and the political opposition. All three elements of the scenario appear in that definition."),
 ("populism",
  "EK IEF-1.C.6.f defines populism as supporting the interests and rights of the common people over those of the elites, which is the contrast the movement draws. The definition requires no position on ethnicity or ownership."),
 ("whereas socialism nationalizes major private industries",
  "EK IEF-1.C.6.c and EK IEF-1.C.6.d are written to separate the two: abolition of private property and near total control on one side, nationalization of major private industries and reduced income disparities on the other. Reversing them contradicts both."),
 ("whereas neoliberalism is defined by limited governmental intervention",
  "EK IEF-1.C.6.a defines individualism by civil liberties and freedom against governmental restrictions and EK IEF-1.C.6.b defines neoliberalism by limited governmental intervention in the economy and society with a named policy list. Both limit government, in different domains."),
 ("whereas populism is defined by support for the common people",
  "EK IEF-1.C.6.e defines fascism as extreme nationalism favoring authoritarian rule and the ethnic majority over minorities and the opposition, while EK IEF-1.C.6.f defines populism by the common people against the elites. Neither definition mentions ownership of industry."),
 ("fascism",
  "EK IEF-1.C.6.e is the only one of the six whose definition names ethnic minorities and the political opposition. The other five concern liberties, economic intervention, property, distribution and the common people."),
 ("populism, defined by the common people against the elites",
  "EK IEF-1.C.6.f defines populism by whose interests should prevail rather than by ownership or liberty, and each rejected option quotes the framework's definition of a different ideology accurately."),
 ("whereas neoliberalism calls for privatization",
  "EK IEF-1.C.6.d and EK IEF-1.C.6.b put the two at opposite ends of one question: nationalization of major private industries against privatization, free trade, deregulation and the elimination of state subsidies."),
 ("near total government control",
  "EK IEF-1.C.6.c defines communism as the abolition of private property with near total governmental control of the economy. Recomputed in q20 above: only one platform states both, and its nearest rival expressly leaves smaller firms private."),
 ("leaving smaller firms in private hands",
  "EK IEF-1.C.6.d defines socialism by the reduction of income disparities and the nationalization of major private industries, which leaves private property standing. Recomputed in q21 above, with the communism platform present so the two definitions are genuinely in play."),
 ("privatize state-owned firms, end subsidies and deregulate",
  "EK IEF-1.C.6.b names privatization, free trade, deregulation and the elimination of state subsidies as neoliberalism's policies. Recomputed in q22 above: one platform states three of the four and no other privatizes."),
 ("by 16 percentage points",
  "Every row of the table quotes one of EK IEF-1.C.6's definitions, so the comparison stays inside the framework's list. Recomputed in q23 above: two rows rise and two fall, and the largest ABSOLUTE movement belongs to a falling row, which is why the signed change is what the question asks for."),
 ("Country F, whose two relevant",
  "EK IEF-1.C.6.a defines individualism by freedom over governmental restrictions and EK IEF-1.C.6.b defines neoliberalism by limited governmental intervention, so those two rows are the ones limiting government. Recomputed in q24 above: 60 against 33."),
 ("populism",
  "The leading row in that column quotes EK IEF-1.C.6.f's definition of populism word for word. Recomputed in q25 above, including that no row of the table states EK IEF-1.C.6.c's abolition of private property, so that option is unavailable from the data."),
 ("does not include authoritarian rule",
  "EK IEF-1.C.6.e's fascism is defined by extreme nationalism, authoritarian rule and the rights of the ethnic majority over minorities and the opposition, while EK IEF-1.C.6.f's populism is defined only by the common people against the elites. Outlawing rival parties and ranking ethnic groups belong to the first definition alone."),
 ("individualism",
  "EK IEF-1.C.6.a defines individualism as belief in individual civil liberties and freedom over governmental restrictions and takes no position on the economy, whereas EK IEF-1.C.6.b's neoliberalism is defined by limited governmental intervention in the economy and society."),
 ("neoliberalism and socialism",
  "EK IEF-1.C.6.b defines neoliberalism by privatization and EK IEF-1.C.6.d defines socialism by the nationalization of major private industries, opposite answers to one question. EK IEF-1.C.6.a, .e and .f are defined by liberties, nationhood and the common people instead."),
 ("only by support for the interests and rights of the common people",
  "EK IEF-1.C.6.f defines populism solely by the common people against the elites and says nothing about ownership, distribution or regulation, which are the content of EK IEF-1.C.6.b, .c and .d."),
 ("defined variously by liberties",
  "EK IEF-1.C.6 supplies the definition and its six representations, which are defined on different axes: liberties in .a, economic intervention in .b, .c and .d, nationhood and authoritarian rule in .e, and the common people against the elites in .f. The framework assigns none of them to a course country."),
]

cg.check(k3_3, CLAIMS, table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25})
