"""Key audit for AP COMPARATIVE GOVERNMENT 1.6 Change in Power and Authority.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
  PAU-1.D.2  how a regime uses power in support of sovereignty is determined in
             large part by its democratic or authoritarian characteristics, and
             DEMOCRATIC REGIMES CAN MAINTAIN SOVEREIGNTY USING LESS POWER
  PAU-1.D.3  regimes change when rules and institutions are replaced INCREMENTALLY
             OR SUDDENLY, by elections, coups, or revolutions in which a large
             portion of the population supports a change in the political system
  PAU-1.D.4  governments change more frequently and easily than regimes, through
             elections, appointments and lines of succession, but also by more
             violent means such as revolutions or coups, represented by such
             violent transitions in IRAN AND NIGERIA

The regime/government boundary every scenario item turns on is PAU-1.A.2: the
regime is the fundamental rules controlling access to and exercise of political
power, and regimes typically endure from government to government. Country items
are held to PAU-1.D.1.b, PAU-1.D.1.c, PAU-1.D.1.e, PAU-4.A.3 and PAU-4.A.4, and
the legitimacy item to LEG-1.B.2 and LEG-1.A.1.

THE READING PAU-1.D.2 INVITES AND THE FRAMEWORK DENIES
------------------------------------------------------
'Democratic regimes can maintain sovereignty using less power' is easy to hear as
'democracies are weaker' or as a value judgement the author is hedging. It is
neither: it is a positive claim about the POWER REQUIRED, not about the
sovereignty held, and AP_COMP_GOV_CED.md note 11 records that the framework
states it flatly. Item 3 keys that reading and item 27 applies it to a scenario.

A second trap is keyed at item 11: PAU-1.D.4 says governments change by violent
means too, so the use of force does NOT by itself make a change a regime change.
The two scenarios there differ only in whether the constitution survives.

DATA ITEMS
----------
Items 19-21 share a turnover table and items 22-23 a means-of-change table. Both
are HYPOTHETICAL and labelled so in the stems, since the framework prints no
counts of this kind and any real count would date. Each key is recomputed below.

A DEFECT FIXED WHILE WRITING THIS FILE: item 23's distractor list originally
offered '8', which is a substring of the '48' also on the list, so a normalized
containment check would flag it -- and a student scanning for '8' would find it
inside another option. It is now '31'.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k1_6

HOG = "Changes of head of government, 1990-2020"
ORDER = "Changes of constitutional order, 1990-2020"
PEACE = "Changes of head of government occurring by election or succession"
GOVCH = "Changes of government (hypothetical)"
REGCH = "Of those, changes that also replaced the regime"


def _turn(table):
    return {lab: (cg.cell(table, lab, HOG), cg.cell(table, lab, ORDER), cg.cell(table, lab, PEACE))
            for lab in cg.labels(table)}


def q19(table, item):
    t = _turn(table)
    hog, order, peace = t["Country D"]
    assert (hog, order, peace) == (9, 0, 9), f"the keyed row reads {t['Country D']}"
    assert hog == max(v[0] for v in t.values()), "the keyed row must show the most changes of head of government"
    assert peace == hog, "the key says every one of them came by election or succession"
    assert order == 0, "the key says the constitutional order never changed"
    others = {lab: v for lab, v in t.items() if lab != "Country D"}
    assert not any(v[0] == v[2] and v[1] == 0 and v[0] >= hog for v in others.values()), \
        "no other row may show the same combination as strongly"
    return "one row shows nine changes of head of government, all peaceful, with no change of constitutional order"


def q20(table, item):
    t = _turn(table)
    other_means = {lab: (v[0] - v[2], v[0]) for lab, v in t.items()}
    shares = {lab: (n / tot if tot else 0) for lab, (n, tot) in other_means.items()}
    assert other_means["Country F"] == (3, 4), f"the keyed three of four reads {other_means['Country F']}"
    assert other_means["Country E"] == (3, 7), f"the rejected three of seven reads {other_means['Country E']}"
    assert max(shares, key=shares.get) == "Country F", f"the largest share belongs to {max(shares, key=shares.get)}"
    assert shares["Country F"] > shares["Country E"], "the two rows with equal counts must be separated by their shares"
    return "three of four changes came by other means in the keyed row against three of seven in the nearest rival, so the counts tie and the shares do not"


def q21(table, item):
    total_hog = sum(cg.col(table, HOG))
    total_order = sum(cg.col(table, ORDER))
    assert (total_hog, total_order) == (22, 3), f"the column totals recompute to {total_hog} and {total_order}"
    ratio = total_hog / total_order
    assert 6.5 < ratio < 8.0, f"the ratio {ratio:.2f} is not closest to seven to one"
    for wrong in (1 / 7, 3.0, 22.0, 1.0):
        assert abs(ratio - wrong) > abs(ratio - 7.0), f"distractor {wrong} is at least as close as the key"
    return f"the columns total 22 and 3, a ratio of {ratio:.2f} to 1, closer to seven than to any value offered against it"


def q22(table, item):
    rows = {str(r[0]): (cg.cell(table, r[0], GOVCH), cg.cell(table, r[0], REGCH)) for r in table["rows"]}
    ordered = sorted(rows, key=lambda k: rows[k][0], reverse=True)
    common, rare = ordered[:2], ordered[2:]
    for lab in common:
        n, k = rows[lab]
        assert k / n < 0.10, f"{lab} replaced the regime in {k} of {n}, which is not 'almost never'"
    for lab in rare:
        n, k = rows[lab]
        assert k / n >= 0.60, f"{lab} replaced the regime in {k} of {n}, which is not 'almost always'"
    assert rows["Election"][0] > rows["Coup"][0], "'coups changed governments more often than elections' must be false"
    assert sum(k for _, k in rows.values()) > 0, "'no change replaced the regime' must be false"
    assert any(k < n for n, k in rows.values()), "'every change replaced the regime' must be false"
    return "the two largest rows replace the regime in under a tenth of cases and the two smallest in at least two thirds"


def q23(table, item):
    total = sum(cg.col(table, GOVCH))
    assert total == 79, f"the keyed total recomputes to {total}"
    for wrong in (71, 77, 31, 48):
        assert wrong != total, f"distractor {wrong} equals the correct total"
    assert sum(cg.col(table, REGCH)) == 8, "the second column totals 8, which is why a wrong-column reading is plausible"
    return f"the changes-of-government column sums to {total:.0f}, matched by no distractor"


CLAIMS = [
 ("Democratic regimes can maintain sovereignty using less power",
  "EK PAU-1.D.2 states that democratic regimes can maintain sovereignty using less power than authoritarian regimes, and that how a regime chooses to use power in support of sovereignty is determined in large part by its democratic or authoritarian characteristics. The framework offers it as a positive claim rather than a preference."),
 ("democratic or authoritarian characteristics",
  "EK PAU-1.D.2 names exactly this as what determines in large part how a regime uses power in support of sovereignty. Territory, treaty membership, party counts and constitutional age are not offered anywhere in the framework as determinants of it."),
 ("about the power required",
  "EK PAU-1.D.2 compares the POWER required to maintain sovereignty, not the sovereignty held; EK PAU-1.A.4 defines sovereignty as a state's independent legal authority over a population and territory, which the statement does not say democracies have less of."),
 ("elections, coups, or revolutions",
  "EK PAU-1.D.3 names elections, coups and revolutions in which a large portion of the population supports a change in the political system, and says the replacement of rules and institutions may be incremental or sudden. Restricting the list to a single route contradicts the sentence."),
 ("replaced step by step",
  "EK PAU-1.D.3 expressly recognizes an incremental route, stating that changes in regimes occur when rules and institutions are replaced either incrementally or suddenly. EK PAU-1.A.2 makes those fundamental rules the regime, and every amendment described alters them."),
 ("suddenly, by revolution",
  "EK PAU-1.D.3 names revolutions in which a large portion of the population supports a change in the political system among the routes by which rules and institutions are replaced, and allows the replacement to be sudden. Annulling a constitution replaces the rules rather than the officeholders."),
 ("more frequently and easily",
  "EK PAU-1.D.4 states that governments, including political officeholders, can be changed more frequently and easily than regimes, and EK PAU-1.A.2 explains why: regimes endure from government to government because they are the rules by which officeholders are replaced."),
 ("appointments, and lines of succession",
  "EK PAU-1.D.4 names elections, appointments and lines of succession as the relatively peaceful process by which governments change, contrasting them with the violent means listed in the same statement."),
 ("in Iran and Nigeria",
  "EK PAU-1.D.4 states that governments also change by more violent means such as revolutions or coups, represented by such violent transitions in Iran and Nigeria. The framework names those two countries and no others in this connection."),
 ("became a multiparty republic following military rule",
  "EK PAU-1.D.4 names Iran and Nigeria as the sites of violent transitions, EK PAU-1.D.1.b describes Iran moving from dictatorial rule to a theocracy based on Islamic Sharia law after 1979, and EK PAU-1.D.1.c describes Nigeria's transition to a multiparty republic following military rule. Same kind of route, different destinations."),
 ("a change of government and the second a change of regime",
  "EK PAU-1.A.2 makes the regime the fundamental rules controlling access to and exercise of power, so what separates the two scenarios is whether those rules were replaced. EK PAU-1.D.4 notes that governments change by violent as well as peaceful means, so force alone does not make a change a regime change."),
 ("themselves replaced as a result",
  "EK PAU-1.D.3 lists elections among the routes by which rules and institutions are replaced, so an election can produce a regime change; EK PAU-1.A.2 requires that the fundamental rules themselves change. A new majority under unchanged rules is a change of government."),
 ("large portion of the population",
  "EK PAU-1.D.3 describes revolutions in which a large portion of the population supports a change in the political system, which is what distinguishes a revolution in the framework's usage from a palace coup or a constitutional crisis."),
 ("Both the government and the regime changed",
  "EK PAU-1.D.1.b describes a transition of power from dictatorial rule to a theocracy based on Islamic Sharia law, which under EK PAU-1.A.2 is a replacement of the fundamental rules and therefore a regime change, with the rulers changing alongside them. EK PAU-1.A.2 also has the state persisting through such a change."),
 ("can arrive at a multiparty republic",
  "EK PAU-1.D.1.c records the transition to a multiparty republic following military rule, EK PAU-1.D.3 supplies the mechanism of rules and institutions being replaced, and EK PAU-1.D.4 names Nigeria among the countries with violent transitions. The three statements are consistent with one another."),
 ("incremental replacement of the rules",
  "EK PAU-4.A.3 lists higher registration requirements, higher threshold rules and the elimination of gubernatorial elections among the rules ensuring one-party dominance in Russia, and EK PAU-1.D.3 allows the replacement of rules and institutions to occur incrementally. Each measure narrows access to power by rule change rather than by a single event."),
 ("by constitutional means",
  "EK PAU-1.D.1.e states that constitutional reforms in the United Kingdom devolved power to multiple parliaments, allowing the regime to maintain stability, and EK PAU-2.A.1 continues to list the United Kingdom among the unitary states. The change was to institutions, by constitutional means, and it preserved the regime."),
 ("peaceful and largely incremental change",
  "EK PAU-4.A.4 lists the measures as facilitating Mexico's transition away from one-party dominance and EK PAU-1.D.1.c records the destination as a multiparty republic. EK PAU-1.D.3's incremental route fits a sequence of rule changes, and EK PAU-1.D.4 names Iran and Nigeria rather than Mexico for violent transitions."),
 ("all by election or succession",
  "EK PAU-1.D.4 pairs frequency with peacefulness, describing governments changing often through elections, appointments and lines of succession while regimes endure. Recomputed in q19 above: one row shows the most officeholder changes, every one of them peaceful, with no change of constitutional order."),
 ("three of four",
  "EK PAU-1.D.4 treats revolutions and coups as the more violent means by which governments change. Recomputed in q20 above: two rows tie on the count of changes by other means and the shares separate them, so the largest share marks the least peaceful record."),
 ("7 to 1",
  "Recomputed in q21 above: the columns total twenty-two changes of head of government against three changes of constitutional order. EK PAU-1.D.4's claim that governments change more frequently than regimes is what a ratio of this shape expresses."),
 ("almost never replaced the regime",
  "Recomputed in q22 above: the two largest rows are followed by regime replacement in under a tenth of cases and the two smallest in at least two thirds. That is EK PAU-1.D.4's contrast between the frequent peaceful routes and the rare violent ones, stated as proportions."),
 ("79",
  "Recomputed in q23 above by summing the changes-of-government column. The alternatives arise from dropping one of the smaller rows, adding the wrong column, or reading only the largest single row."),
 ("under the same constitutional rules",
  "EK PAU-1.A.2 makes the regime the fundamental rules controlling access to and exercise of power and EK PAU-1.D.4 names lines of succession among the peaceful routes by which governments change. A succession under unchanged rules leaves the regime intact, while each rejected option replaces the rules themselves."),
 ("council of officers assumes the power to legislate",
  "EK PAU-1.D.3 describes regime change as the replacement of rules and institutions, including by coup, and EK PAU-1.A.2 identifies those rules as the regime. The rejected events all occur inside rules that continue to operate."),
 ("designed to replace them periodically",
  "EK PAU-1.A.2 states that regimes typically endure from government to government and EK PAU-1.D.4 that governments change more frequently and easily through elections, appointments and lines of succession. Those routes are supplied by the regime, so using them leaves the regime standing."),
 ("smaller expenditure of power because of its democratic characteristics",
  "EK PAU-1.D.2 states that democratic regimes can maintain sovereignty using less power than authoritarian regimes, and that the choice of how to use power is determined in large part by democratic or authoritarian characteristics. The prediction therefore follows from the regime type, not from the protest."),
 ("peaceful transfer of power tends to reinforce legitimacy",
  "EK LEG-1.B.2 names peaceful resolution of conflicts and peaceful transfer of power among the things that reinforce legitimacy, and EK LEG-1.A.1 defines legitimacy as whether a government's constituents believe it has the right to use power as it does. Recognition by other states is a separate matter under EK PAU-1.A.2."),
 ("previous rules no longer govern anything",
  "EK PAU-1.A.2 identifies the regime with the fundamental rules controlling access to and exercise of political power, so evidence of regime change must be evidence about those rules. A new party in office, a reorganization, a new capital and a swing in vote share are all compatible with unchanged rules."),
 ("routes the regime itself provides",
  "EK PAU-1.D.3 supplies the routes and the incremental or sudden pace of regime change and EK PAU-1.D.4 the greater frequency and ease of government change, while noting that violent routes exist for governments too. The summary keeps both halves rather than collapsing them into one."),
]

cg.check(k1_6, CLAIMS, table_checks={19: q19, 20: q20, 21: q21, 22: q22, 23: q23})
