"""Key audit for AP COMPARATIVE GOVERNMENT 4.6 Pluralist and Corporatist
Interests.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
Learning objective IEF-2.B, four essential knowledge statements:

  IEF-2.B.1  pluralism and corporatism are SYSTEMS OF INTEREST GROUP
             REPRESENTATION
  IEF-2.B.2  PLURALIST systems promote COMPETITION AMONG AUTONOMOUS GROUPS NOT
             LINKED TO THE STATE; in a CORPORATIST system the GOVERNMENT CONTROLS
             ACCESS TO POLICY MAKING by relying on STATE-SANCTIONED GROUPS OR
             SINGLE PEAK ASSOCIATIONS to represent LABOR, BUSINESS and
             AGRICULTURAL sectors
  IEF-2.B.3  the state retains MORE CONTROL OVER CITIZEN INPUT in a corporatist
             system than in a pluralist one
  IEF-2.B.4  interest group systems CAN CHANGE OVER TIME, as represented by
             MEXICO moving FROM corporatist TOWARD pluralist

FOUR SENTENCES CARRY THIRTY ITEMS, so almost everything here is application, and
the items are built around the two errors the topic exists to correct.

  THE FIRST ERROR is reading corporatism as the absence of interest groups.
  IEF-2.B.1 forecloses it in one line: BOTH are systems OF interest group
  representation. The groups are present in either case and the difference is who
  decides which of them reach policy making. Items 1, 20 and 29 key that
  directly, and every application item (10, 11, 12, 17, 18, 21, 28) is written so
  that the mere existence of associations, of consultation, or of sector-wide
  bargaining settles nothing -- each of those appears in BOTH arrangements in the
  third table, which is why item 28 asks for the single distinguishing feature
  and the check confirms the other candidate features are common to both rows.

  THE SECOND ERROR is reversing IEF-2.B.4's direction. The framework's example
  runs FROM corporatist TOWARD pluralist, the same direction as PAU-4.A.4's
  transition away from one-party dominance, and enduring understanding IEF-2 ties
  varied citizen organizations to democratization. Items 7, 8, 16, 19 and the
  second table all key the direction, and item 24's check requires all three
  columns to move consistently with it.

The suggested skill for this topic is Source Analysis, so items 14-16 supply an
author's position and ask what system it describes or implies. Those positions
are PARAPHRASED ARGUMENTS, not quotations: nothing in the module is presented as
the words of a real writer.

Table figures are HYPOTHETICAL and every table is labelled so.

DATA ITEMS
----------
Items 21-23 read the recognition table, 24-26 the change-over-time table, 27-28
the access table. Every arithmetic distractor is verified below to be a wrong
operation on the same table. Item 24's key asserts THREE simultaneous movements,
so the check tests each column separately -- a table in which only one column
moved would leave the key partly false.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k4_6

M = "Organizations the government recognizes for consultation in Country M"
N = "Organizations the government recognizes for consultation in Country N"

SOLE = "Sectors in which one association holds sole recognition"
INDEP = "Independent associations consulted on policy"
SHARE = "Share of consultations including an association the state has not sanctioned (percent)"

SUBMIT = "Who may submit views on a draft law"
SANCTION = "Whose formation requires the state's sanction"
NEGOTIATE = "Who negotiates sector-wide agreements with the ministry"


def q21(table, item):
    m, n = cg.col(table, M), cg.col(table, N)
    sectors = [s.lower() for s in cg.labels(table)]
    assert sectors == ["labor", "business", "agriculture"], \
        f"the rows must be the framework's three sectors; they read {sectors}"
    assert set(m) == {1}, f"the keyed country must recognize exactly one body per sector; its column reads {m}"
    assert min(n) > 1, f"the rejected country must recognize many per sector; its column reads {n}"
    assert len(m) == 3, "there must be one row for each of the framework's three sectors"
    return f"one column reads {m} across labor, business and agriculture while the other reads {n}"


def q22(table, item):
    m, n = cg.col(table, M), cg.col(table, N)
    total = sum(n)
    assert total == 101, f"the keyed total recomputes to {total}"
    assert total + sum(m) == 104, "the 104 distractor must be both columns added together"
    assert total - min(n) == 84, "the 84 distractor must be the total with the smallest sector left out"
    assert max(n) == 46, "the 46 distractor must be the largest single sector"
    assert sum(m) == 3, "the 3 distractor must be the other country's total"
    return f"the second country's column reads {n} and sums to {total:.0f}, with every distractor a wrong sum of the same table"


def q23(table, item):
    m, n = cg.col(table, M), cg.col(table, N)
    diff = sum(n) - sum(m)
    assert diff == 98, f"the keyed difference recomputes to {diff}"
    gaps = [b - a for a, b in zip(m, n)]
    assert gaps == [45, 37, 16], f"the 45, 37 and 16 distractors must be the sector-by-sector gaps; they are {gaps}"
    assert sum(n) == 101, "the 101 distractor must be the larger total read as though it were the difference"
    return f"the totals are {sum(m):.0f} and {sum(n):.0f}, so they differ by {diff:.0f}"


def q24(table, item):
    sole, ind, share = cg.col(table, SOLE), cg.col(table, INDEP), cg.col(table, SHARE)
    assert sole == sorted(sole, reverse=True), f"sole recognition must fall across the surveys; it reads {sole}"
    assert sole[-1] == 0, f"sole recognition must reach zero, or it has not disappeared; it ends at {sole[-1]}"
    assert ind == sorted(ind), f"independent associations must rise; the column reads {ind}"
    assert share == sorted(share), f"unsanctioned participation must rise; the column reads {share}"
    assert len(set(ind)) == 3 and len(set(share)) == 3, "'nothing changed' must be false in both rising columns"
    assert ind[-1] > 0 and share[-1] > 0, "'consultation ceased' must be false"
    return (f"sole recognition goes {sole}, independent associations {ind} and unsanctioned participation "
            f"{share}, so all three columns move with a shift away from corporatism")


def q25(table, item):
    ind, share = cg.col(table, INDEP), cg.col(table, SHARE)
    rise = ind[2] - ind[0]
    assert rise == 62, f"the keyed increase recomputes to {rise}"
    assert ind[2] - ind[1] == 45, "the 45 distractor must be the increase between the second and third surveys"
    assert ind[1] - ind[0] == 17, "the 17 distractor must be the increase between the first and second surveys"
    assert ind[2] == 64, "the 64 distractor must be the third survey's own figure"
    assert share[2] - share[0] == 66, "the 66 distractor must be the rise in the other column"
    return f"the independent-association column reads {ind}, so the rise from the first survey to the third is {rise:.0f}"


def q26(table, item):
    share, ind = cg.col(table, SHARE), cg.col(table, INDEP)
    rise = share[2] - share[0]
    assert rise == 66, f"the keyed rise recomputes to {rise}"
    assert share[2] - share[1] == 37, "the 37 distractor must be the rise between the second and third surveys"
    assert share[1] - share[0] == 29, "the 29 distractor must be the rise between the first and second surveys"
    assert share[2] == 71, "the 71 distractor must be the final share read as a rise"
    assert ind[2] - ind[0] == 62, "the 62 distractor must be the change in the count column"
    return f"the unsanctioned-participation column reads {share}, so it rises {rise:.0f} percentage points overall"


def _acc(table):
    return {lab: (str(table["rows"][i][1]), str(table["rows"][i][2]), str(table["rows"][i][3]))
            for i, lab in enumerate(cg.labels(table))}


def q27(table, item):
    v = _acc(table)
    s1, s2 = v["System 1"], v["System 2"]
    assert s2[0].lower().startswith("only"), f"the keyed row must restrict who may submit views; it reads {s2[0]!r}"
    assert "any" in s1[0].lower(), f"the rejected row must be the open one; it reads {s1[0]!r}"
    assert s2[1].lower().startswith("every"), f"the keyed row must require sanction to form; it reads {s2[1]!r}"
    assert s1[1].lower().startswith("no"), f"the rejected row must require no sanction; it reads {s1[1]!r}"
    return "one row restricts submissions to a recognized association per sector and requires state sanction to form; the other does neither"


def q28(table, item):
    v = _acc(table)
    s1, s2 = v["System 1"], v["System 2"]
    assert "one recognized association for each sector" in s2[2].lower(), \
        f"the keyed feature must appear in the corporatist row; it reads {s2[2]!r}"
    assert "one recognized association for each sector" not in s1[2].lower(), \
        f"the keyed feature must NOT appear in the other row; it reads {s1[2]!r}"
    neg_header = [h for h in table["headers"] if "negotiates sector-wide" in h.lower()]
    assert neg_header, "the table must carry one sector-wide negotiation column, common to both rows"
    for text in (s1[2], s2[2]):
        assert "association" in text.lower(), \
            "associations must negotiate the sector-wide agreements in BOTH rows, or the rejected features would not be common ground"
    assert "association" in s1[0].lower() and "association" in s2[0].lower(), \
        "both rows must involve associations submitting views, so the existence of associations cannot be the marker"
    return "sole recognition for negotiation appears in one row only, while associations, consultation and sector-wide bargaining appear in both"


CLAIMS = [
 ("two systems of interest group representation",
  "EK IEF-2.B.1 states that pluralism and corporatism are systems of interest group representation, which is why interest groups exist under both and the systems differ over how those groups reach policy making."),
 ("autonomous groups not linked to the state",
  "EK IEF-2.B.2 states that pluralist systems promote competition among autonomous groups not linked to the state, so the competition and the independence from the state are both parts of the description."),
 ("access to policy making",
  "EK IEF-2.B.2 states that in a corporatist system the government controls access to policy making, so what the government controls is entry to the process rather than the existence of organizations or the outcome of elections."),
 ("state-sanctioned groups or single peak associations",
  "EK IEF-2.B.2 states that a corporatist government relies on state-sanctioned groups or single peak associations to represent economic sectors, which is the instrument through which access is controlled."),
 ("labor, business, and agricultural sectors",
  "EK IEF-2.B.2 names labor, business, and agricultural sectors as the sectors single peak associations represent, so the list is economic and sectoral rather than communal or institutional."),
 ("in a corporatist system",
  "EK IEF-2.B.3 states that the state retains more control over citizen input in a corporatist system than in a pluralist one, which follows from EK IEF-2.B.2's account of the government controlling access to policy making."),
 ("can change over time",
  "EK IEF-2.B.4 states that interest group systems can change over time and supplies a course country as its example, so neither system is a permanent property of a country or a consequence of its constitution."),
 ("from a corporatist system toward a pluralist system",
  "EK IEF-2.B.4 represents its claim with Mexico's moving from a corporatist system toward a pluralist system, and EK PAU-4.A.4 records rule changes in that country running in the same direction."),
 ("not linked to the state",
  "EK IEF-2.B.2 describes pluralist groups as autonomous and not linked to the state, so autonomy in the framework's sense is independence from the state rather than exclusion from contact with it."),
 ("the state has sanctioned a single association",
  "EK IEF-2.B.2 defines corporatism by the government's relying on state-sanctioned groups or single peak associations to represent labor, business and agricultural sectors, and sole legal recognition of one federation for a sector is that arrangement."),
 ("none is linked to the state",
  "EK IEF-2.B.2 states that pluralist systems promote competition among autonomous groups not linked to the state, and the absence of any legal standing one group holds and the others lack is what makes them autonomous in that sense."),
 ("single peak associations represent the labor, business, and agricultural sectors",
  "EK IEF-2.B.2 names exactly those three sectors as the ones single peak associations represent in a corporatist system, so one recognized association for each of them is the framework's arrangement rather than an accidental resemblance."),
 ("it decides which groups reach policy making",
  "EK IEF-2.B.3 states that the state retains more control over citizen input under corporatism, and EK IEF-2.B.2 gives the reason, since the government controls access to policy making through the groups it has sanctioned."),
 ("single peak association for each sector",
  "EK IEF-2.B.2 describes corporatism as relying on state-sanctioned groups or single peak associations to represent labor, business and agricultural sectors, which is the one-authoritative-voice-per-sector arrangement the argument prefers."),
 ("autonomous groups not linked to the state compete",
  "EK IEF-2.B.2 states that pluralist systems promote competition among autonomous groups not linked to the state, and the argument's two conditions, contention among many associations and standing that does not come from government, are the two halves of that description."),
 ("a movement toward a pluralist system",
  "EK IEF-2.B.4 states that interest group systems can change over time and gives Mexico's move from corporatism toward pluralism as its example, and ending sole recognition removes the state-sanctioned representation EK IEF-2.B.2 makes definitive of a corporatist system."),
 ("hold no special legal standing now take part in consultations",
  "EK IEF-2.B.2 distinguishes the two systems by whether the groups reaching policy making owe their standing to the state, so evidence of pluralization has to show unsanctioned groups gaining access, which is the direction EK IEF-2.B.4 records."),
 ("the one association the state recognizes for each sector",
  "EK IEF-2.B.2 defines corporatism by the government's controlling access to policy making through state-sanctioned groups or single peak associations, so consultation confined to the recognized association for each sector is that control in evidence."),
 ("widens the range of organizations that reach policy making",
  "Enduring understanding IEF-2 states that strong and varied citizen organizations and movements foster and are reinforced by democratization, and EK IEF-2.B.4's shift from corporatism toward pluralism increases the variety of organizations with access."),
 ("the groups exist and the government determines which of them reach policy making",
  "EK IEF-2.B.1 states that pluralism and corporatism are both systems of interest group representation, and EK IEF-2.B.2 describes corporatism as relying on state-sanctioned groups, so the groups are present by definition and the difference lies in who controls access."),
 ("exactly one organization is recognized in each of the three sectors",
  "EK IEF-2.B.2 describes a corporatist system as relying on single peak associations to represent the labor, business and agricultural sectors. Recomputed in q21 above, which also checks that the table's rows are the framework's own three sectors."),
 ("101",
  "Recomputed in q22 above by summing that country's column across the three sectors. The distractors are both columns added together, the total with the smallest sector omitted, the largest single sector, and the other country's total."),
 ("98",
  "Recomputed in q23 above by subtracting the smaller country total from the larger. The distractors are the three sector-by-sector gaps and the larger total read as though it were the difference."),
 ("Sole recognition disappeared while independent associations",
  "EK IEF-2.B.4 states that interest group systems can change over time, with Mexico moving from a corporatist system toward a pluralist one. Recomputed in q24 above, where each of the three columns is tested separately, since the key asserts three simultaneous movements."),
 ("62",
  "Recomputed in q25 above by subtracting the first survey's figure from the third. The distractors are the increases across the other pairs of surveys, the third survey's own figure, and the rise in the other column."),
 ("66 percentage points",
  "Recomputed in q26 above by subtracting the first survey's share from the third. The distractors are the rises across the other pairs of surveys, the final share read as a rise, and the change in the count column."),
 ("only the recognized association for each sector may submit views",
  "EK IEF-2.B.3 states that the state retains more control over citizen input in a corporatist system and EK IEF-2.B.2 identifies the mechanism as the government controlling access through state-sanctioned groups. Recomputed in q27 above from both restrictions in the keyed row."),
 ("one recognized association for each sector negotiates the sector-wide agreements",
  "EK IEF-2.B.2 makes the single peak association representing a sector the defining instrument of corporatism. Recomputed in q28 above, which confirms that associations, consultation on draft laws and sector-wide bargaining all appear in both rows, so only sole recognition can be the marker."),
 ("lacking state sanction is what makes them independent rather than powerless",
  "EK IEF-2.B.1 calls pluralism a system of interest group representation and EK IEF-2.B.2 describes it as promoting competition among autonomous groups not linked to the state, so the absence of state sanction is the condition of that competition rather than a bar to influence."),
 ("a country can move between them",
  "EK IEF-2.B.1 makes both systems modes of interest group representation, EK IEF-2.B.2 supplies the contrast between autonomous competition and state-sanctioned access, EK IEF-2.B.3 the greater state control under corporatism, and EK IEF-2.B.4 the possibility of change over time."),
]

cg.check(k4_6, CLAIMS,
         table_checks={21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27, 28: q28})
