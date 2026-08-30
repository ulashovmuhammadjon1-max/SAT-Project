"""Key audit for AP COMPARATIVE GOVERNMENT 3.8 Political and Social Cleavages.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
  LEG-2.A.1  cleavages are INTERNAL DIVISIONS THAT STRUCTURE SOCIETIES, based on
             CLASS, ETHNICITY, RELIGION or TERRITORY, with a country-by-country
             account at .a to .f
  LEG-2.B.1  they DIFFER ACROSS COURSE COUNTRIES and affect VOTING BEHAVIOR, PARTY
             SYSTEMS and INFORMAL POLITICAL NETWORKS
  LEG-2.B.2  countries have RESPONDED DIFFERENTLY; .a EVEN STABLE REGIMES face
             radical or terrorist religious elements sprung from long-standing
             cleavages; .b responses range from BRUTE REPRESSION to RECOGNITION,
             AUTONOMOUS REGIONS and REPRESENTATION IN GOVERNMENTAL INSTITUTIONS
  LEG-2.B.3  the use of cleavages TO STRENGTHEN LEGITIMACY AND HOLD ONTO POWER is
             found IN ALL COURSE COUNTRIES, and cleavages MAY ALSO undermine
             legitimacy
  LEG-2.B.4  .a separatist movements in CHINA, IRAN, NIGERIA, RUSSIA, the UNITED
             KINGDOM; .b autonomy-not-independence groups in MEXICO and the UNITED
             KINGDOM; .c ethnicity more significant in NIGERIA than MEXICO because
             of DIFFERENT COLONIAL HISTORIES and greater diversity and politicization

HOW THIS DIFFERS FROM TOPIC 1.10
--------------------------------
Topic 1.10 keys LEG-2.B.2.b's range and LEG-2.B.4's two country lists as prose
items. This module keys the LEG-2.A.1 country detail those lists rest on, converts
the two lists into a MATRIX so the reasoning is a lookup rather than a recall
(items 26-27), and keys LEG-2.B.1 and LEG-2.B.3, which 1.10 does not use at all.

THE THREE NUMBERS THE FRAMEWORK PRINTS
--------------------------------------
AT LEAST 55 recognized ethnic minorities in China, MORE THAN 250 ethnic groups in
Nigeria, ethnic Russians at MORE THAN 80 PERCENT. Items 3, 8 and 9 key them and
nothing else numerical is asserted about any country -- the tables are lettered
cases with hypothetical figures for that reason.

Item 16 exists because the comparative claim at LEG-2.B.4.c is easy to over-read:
the framework says ethnicity has mattered MORE in Nigeria than in Mexico, and
LEG-2.A.1.c describes Mexico's ethnic divisions in its own right. Neither statement
says Mexico has none.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k3_8

POPSH = "Share of the region's population belonging to one national group (percent)"
VOTESH = "Share of the region's vote for the party associated with that group (percent)"
DESC = "Description"
SEP = "Separatist movements reported"
AUT = "Groups demanding autonomy but not independence reported"


def _vote(table):
    return {lab: (cg.cell(table, lab, POPSH), cg.cell(table, lab, VOTESH)) for lab in cg.labels(table)}


def q20(table, item):
    v = _vote(table)
    pops = [p for p, _ in v.values()]
    votes = [x for _, x in v.values()]
    assert pops == sorted(pops, reverse=True) and votes == sorted(votes, reverse=True), \
        f"the two columns must fall together across the rows; got {pops} and {votes}"
    assert all(x < p for p, x in v.values()), \
        "the vote share must be below the population share in every row, so the reversed reading is false"
    assert len(set(votes)) == len(votes), "'the same in every region' must be false"
    return f"population shares {pops} and vote shares {votes} fall together, with the vote below the population share in every row"


def q21(table, item):
    v = _vote(table)
    gaps = {lab: p - x for lab, (p, x) in v.items()}
    assert max(gaps, key=gaps.get) == "Region 1", f"the largest gap belongs to {max(gaps, key=gaps.get)}"
    assert gaps == {"Region 1": 9, "Region 2": 5, "Region 3": 3}, f"the three gaps recompute to {gaps}"
    assert len(set(gaps.values())) == 3, "'the gaps are equal' must be false"
    return f"the three gaps are {gaps}, so each option states a true gap for a different region"


def q22(table, item):
    v = _vote(table)
    p, x = v["Region 2"]
    pct = x / p * 100
    assert abs(pct - 88) < 1.0, f"the keyed ratio recomputes to {pct:.1f} percent"
    assert x == 36 and p == 41, "the 36 and 41 distractors must be the two raw figures from the same row"
    assert v["Region 3"][0] == 12, "the 12 distractor must be a figure from another row"
    assert abs(p / x * 100 - 114) < 1.0, "the 114 distractor must be the same division performed the wrong way round"
    return f"{x:.0f} over {p:.0f} is {pct:.1f} percent, and every distractor is a raw figure, another row, or the inverted ratio"


def _resp(table):
    return {str(r[0]): str(r[1]) for r in table["rows"]}


def q23(table, item):
    v = _resp(table)
    r = v["Response 1"]
    assert "detention" in r and "ban" in r, f"the keyed row reads {r!r}"
    for lab in ("Response 2", "Response 3", "Response 4"):
        assert "detention" not in v[lab], f"{lab} must not also use detention"
    return "one row alone uses mass detention and prohibition against the group itself"


def q24(table, item):
    v = _resp(table)
    assert "autonomous region" in v["Response 2"], f"the second keyed row reads {v['Response 2']!r}"
    assert "reserved" in v["Response 3"] and "legislature" in v["Response 3"], \
        f"the third keyed row reads {v['Response 3']!r}"
    for lab in ("Response 1", "Response 4"):
        assert "autonomous region" not in v[lab] and "reserved" not in v[lab], \
            f"{lab} must not state either accommodating measure"
    return "two rows state the framework's two accommodating measures, an autonomous region and reserved legislative seats"


def q25(table, item):
    v = _resp(table)
    r = v["Response 4"]
    assert "blaming" in r, f"the keyed row reads {r!r}"
    for lab in ("Response 1", "Response 2", "Response 3"):
        assert "blaming" not in v[lab], f"{lab} must not also blame the minority"
    assert "detention" in v["Response 1"], \
        "the repressive row must remain distinct, since using a cleavage is not the same as repressing a group"
    return "one row alone directs blame at a minority rather than repressing or accommodating it"


def _sep(table):
    return {str(r[0]): (str(r[1]), str(r[2])) for r in table["rows"]}


def q26(table, item):
    v = _sep(table)
    both = [lab for lab, (s, a) in v.items() if s == "yes" and a == "yes"]
    assert both == ["Country J"], f"exactly one row may record both; got {both}"
    return "one row alone records separatist movements and autonomy-without-independence groups together"


def q27(table, item):
    v = _sep(table)
    only_aut = [lab for lab, (s, a) in v.items() if s == "no" and a == "yes"]
    assert only_aut == ["Country K"], f"exactly one row may record autonomy without separatism; got {only_aut}"
    assert v["Country J"] == ("yes", "yes"), \
        "the row for the country on BOTH framework lists must remain available as a distractor"
    return "one row alone records autonomy-without-independence groups and no separatist movement"


CLAIMS = [
 ("internal divisions that structure societies",
  "EK LEG-2.A.1 describes social and political cleavages as internal divisions that structure societies and names class, ethnicity, religion and territory as their bases. The rejected options are external actors, EK PAU-1.A.2's regime, EK IEF-1.C.1's political culture and EK IEF-1.A.1's civil society."),
 ("majority Han group",
  "EK LEG-2.A.1.a describes ethnic and regional divisions between the majority Han ethnic group and its recognized ethnic minorities, and between areas that have developed at different rates. The rejected descriptions are the framework's accounts of Iran, Mexico, Nigeria and the United Kingdom."),
 ("at least 55",
  "EK LEG-2.A.1.a states at least 55 recognized ethnic minorities, such as the Uighurs in the northwest and the Tibetans in the southwest. The 250-group figure belongs to Nigeria at EK LEG-2.A.1.d and the Chechens to Russia at EK LEG-2.A.1.e."),
 ("threatening atmosphere despite official recognition",
  "EK LEG-2.A.1.b states that religious divisions between the Shi'a Muslim majority and members of other religions have resulted in a threatening atmosphere DESPITE OFFICIAL RECOGNITION, so recognition and threat coexist in the framework's account. EK DEM-2.A.1.b adds that a small number of Majles seats are reserved for non-Muslim minorities."),
 ("Shi'a majority and those who are Sunni",
  "EK LEG-2.A.1.b states that within practitioners of Islam there are divisions between the Shi'a majority and those who are Sunni. The Persian-Azerbaijani division in the same statement is an ETHNIC cleavage rather than a religious one."),
 ("majority Persians",
  "EK LEG-2.A.1.b names ethnic cleavages between the majority Persians and several ethnic minorities including Azerbaijanis and Kurds, alongside the religious divisions described in the same statement."),
 ("Amerindian population and whites and mestizos",
  "EK LEG-2.A.1.c describes ethnic divisions between the Amerindian, that is indigenous, population and whites and mestizos, together with regional divisions between north and south."),
 ("more than 250 groups",
  "EK LEG-2.A.1.d states ethnic divisions among more than 250 ethnic groups, including the Hausa-Fulani, Yoruba and Igbo, and religious and regional cleavages between the predominantly Muslim north and the south where Christians and animists are concentrated."),
 ("tending to be Russian Orthodox",
  "EK LEG-2.A.1.e describes cleavages between ethnic Russians, more than 80 percent of the population and tending to be Russian Orthodox, and minority non-Russian populations including the predominantly Muslim Chechens in the Caucasus region."),
 ("Protestants and Catholics in Northern Ireland",
  "EK LEG-2.A.1.f names ethnic and regional differences among the Scottish, English, Welsh and Irish; religious differences between Protestants and Catholics in Northern Ireland; and racial tensions between whites and non-European minorities whose heritage relates to the country's colonial history."),
 ("informal political networks",
  "EK LEG-2.B.1 states that major social and political cleavages differ across course countries and affect voting behavior and party systems as well as informal political networks. All three consequences are in the same sentence."),
 ("even stable regimes are increasingly dealing",
  "EK LEG-2.B.2.a states that even stable regimes are increasingly dealing with radical or terrorist religious elements that have sprung from long-standing cleavages. The word 'even' rules out confining the problem to unstable cases."),
 ("brute repression end",
  "EK LEG-2.B.2.b states that state responses range from brute repression to recognition of ethnic and religious minorities and the creation of autonomous regions and/or representation in governmental institutions. Mass detention and a language ban sit at the first endpoint."),
 ("in all course countries",
  "EK LEG-2.B.3 states that examples of the use of social and political cleavages to strengthen legitimacy and hold onto power can be found in all course countries, and that such cleavages may also lead to conflict and undermine legitimacy."),
 ("both emerged there",
  "EK LEG-2.B.4.a names the United Kingdom among the five countries with separatist movements and EK LEG-2.B.4.b names it, with Mexico, among those with groups demanding autonomy but not independence. Appearing on both lists means both kinds of movement are present."),
 ("only that ethnicity has played a more significant role in Nigeria",
  "EK LEG-2.A.1.c describes ethnic divisions in Mexico between the Amerindian population and whites and mestizos, and EK LEG-2.B.4.c says only that ethnicity has played a MORE SIGNIFICANT role in Nigeria. The claim is comparative rather than a denial."),
 ("different colonial histories",
  "EK LEG-2.B.4.c gives different colonial histories and a greater diversity and politicization of ethnic and religious identities in Nigeria as the explanation. EK PAU-2.A.1 lists BOTH countries among the federal states, so territorial structure cannot be the difference."),
 ("predominantly Muslim north",
  "EK LEG-2.A.1.d describes religious and regional cleavages between the predominantly Muslim north and the south where Christians and animists are concentrated, so a single line divides the country on both dimensions at once. The rejected descriptions are ethnic or ethnic-and-regional."),
 ("dominant group and recognized or identified minority populations",
  "EK LEG-2.A.1.a pairs a Han majority with at least 55 recognized minorities and divisions between areas developing at different rates, and EK LEG-2.A.1.e pairs ethnic Russians at more than 80 percent with minority non-Russian populations including the Chechens in the Caucasus. Both pair a dominant group with minorities located regionally."),
 ("tracks that group's share",
  "EK LEG-2.B.1 states that cleavages affect voting behavior and party systems. Recomputed in q20 above: the two columns fall together across the three rows and the party's share is below the group's share in every one, which is why the reversed reading fails."),
 ("gap is 9 percentage points",
  "Recomputed in q21 above by subtracting each region's vote share from its population share. Each alternative states the true gap for a different region, so the item turns on comparing them."),
 ("88 percent",
  "Recomputed in q22 above by dividing the region's party vote share by its group population share. The alternatives are the two raw figures, a figure from another row, and the same division inverted."),
 ("mass detention of members of a minority",
  "EK LEG-2.B.2.b puts brute repression at one end of the range of state responses. Recomputed in q23 above: only one row uses force and prohibition against the group itself."),
 ("Responses 2 and 3",
  "EK LEG-2.B.2.b names recognition of ethnic and religious minorities, the creation of autonomous regions, and representation of minorities in governmental institutions as the accommodating endpoint. Recomputed in q24 above: two rows state the last two of those exactly."),
 ("official campaign blaming a minority",
  "EK LEG-2.B.3 states that the use of cleavages to strengthen legitimacy and hold onto power is found in all course countries. Recomputed in q25 above: one row directs blame at a minority rather than repressing or accommodating it, and the repressive row remains distinct."),
 ("both separatist movements and groups demanding autonomy",
  "EK LEG-2.B.4.a names the United Kingdom among the five with separatist movements and EK LEG-2.B.4.b among the two with autonomy-without-independence groups. Recomputed in q26 above: only one row records both."),
 ("but separatist movements are not",
  "EK LEG-2.B.4.b names Mexico and the United Kingdom for groups demanding autonomy but not independence, while EK LEG-2.B.4.a's separatist list omits Mexico. Recomputed in q27 above: only one row records the second without the first, and the both-lists row remains available as a distractor."),
 ("rightful core",
  "EK LEG-2.B.3 states that examples of using cleavages to strengthen legitimacy and hold onto power are found in all course countries. Autonomy and reserved seats are EK LEG-2.B.2.b's accommodating responses, and publishing statistics or signing a treaty is neither."),
 ("creation of autonomous regions and the representation of minorities",
  "EK LEG-2.B.2.b names recognition of ethnic and religious minorities and the creation of autonomous regions and/or representation of minorities in governmental institutions as the accommodating endpoint, with brute repression at the other."),
 ("used to hold onto power as well as to divide",
  "EK LEG-2.A.1 supplies the definition, the four bases and the country-by-country account, EK LEG-2.B.1 the effects on voting, party systems and informal networks, EK LEG-2.B.2 the differing responses and their range, and EK LEG-2.B.3 the use of cleavages to hold onto power in all course countries alongside their capacity to undermine legitimacy."),
]

cg.check(k3_8, CLAIMS,
         table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27})
