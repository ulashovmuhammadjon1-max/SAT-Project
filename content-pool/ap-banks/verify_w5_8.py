"""Key audit for AP WORLD HISTORY: MODERN 5.8 Reactions to the Industrial Economy.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim cites the Key Concept or Learning
Objective the key traces to.

WHAT THE KEYS REST ON
---------------------
Four statements, and every key traces to one of them or to Unit 5 Learning
Objective I:

  KC-5.1.V.D      IN RESPONSE TO the social and economic changes brought about by
                  industrial capitalism, SOME governments, organizations, and
                  individuals promoted various types of political, social,
                  educational, and urban reforms.
  KC-5.1.V.A      In industrialized states, MANY workers organized themselves,
                  OFTEN in labor unions, to improve working conditions, limit
                  hours, and gain higher wages. Workers' movements and political
                  parties emerged IN DIFFERENT AREAS, promoting alternative
                  visions of society.
  KC-5.3.IV.A.ii  Discontent with established power structures ENCOURAGED the
                  development of various ideologies, INCLUDING those espoused by
                  Karl Marx, and the ideas of socialism and communism.
  KC-5.1.V.B      IN RESPONSE TO the expansion of industrializing states, SOME
                  governments in Asia and Africa, INCLUDING the Ottoman Empire and
                  Qing China, sought to reform and modernize their economies and
                  militaries. Reform efforts were OFTEN resisted by SOME members
                  of government or established elite groups.

The CED prints NO illustrative example on this topic's page, so no key here names
a reform act, a union, a party or a strike. Nothing is dated: the framework gives
no year for anything in this topic, and it states separately that its periods are
approximate.

THE HEDGES ARE THE CONTENT
--------------------------
Every one of those four sentences is qualified, and dropping a qualification is
exactly how a plausible wrong key ships in this topic. Items 2, 5, 6, 7, 9, 15,
20, 21 and 26 each hold one: some governments; many workers; often in unions; in
different areas, with no area named; including Marx; often resisted by some
members of government; including the Ottoman Empire and Qing China. Item 21 makes
the last of those into a goes-beyond item, so the hedge is keyed rather than
merely observed.

THE NEAR MISS AT ITEM 18
------------------------
KC-5.1.V.B names the Ottoman Empire and Qing China. Japan's internal reform is
KC-5.2.II.A and is printed on topic 5.6's page, not this one, so "Japan and
Russia" is offered as the distractor a prepared student could believe. The item
asks which states the framework NAMES in that statement, which is what makes the
distinction checkable rather than a matter of judgement.

SWAP ANCHORS
------------
Three of the four statements are responses to something and each reads plausibly
backwards, so items 4, 16 and 25 carry the reversal as a distractor: the reforms
and the changes industrial capitalism brought exchanged, the ideologies and the
discontent exchanged, and the reform efforts in Asia and Africa exchanged with
the expansion of industrializing states. Each of those anchors carries BOTH
clauses, which is the defect found in verify_e2_1.py.

WHY THE TABLE CONTROL DOES NOT CATCH EVERY CELL
-----------------------------------------------
q11's control catches most but not all corrupted cells, and that is correct
rather than a gap. Raising the last decade's union membership, or raising the
first decade's hours, leaves the keyed conclusion TRUE of the corrupted table --
both columns still move as the key says. A check that fired on those would be
reporting a defect that is not there. What the control requires is that no table
sits undefended, and the printed count is what makes a check that has stopped
reading its table show up as a zero.

The same holds for the prose cells of q28 and q29. The control corrupts a cell by
APPENDING to it, and a measure that still says "army" after the append is still a
measure about the army, so q29 rightly does not fire. What q29 does check is the
thing an item of this shape actually invites going wrong: it holds every one of
the five type labels against a keyword its own description must contain, so a
label swapped between two rows fails even though the SET of types is unchanged.
Reading the type column alone would have missed that.

FIVE choices per item (A-E); see HISTORY_BRIEF.md.
"""
import re
import sys

import cg_check as cg
import wh_check as wh
import w5_8

MEMBERS = "Members of labor unions (thousands)"
HOURS = "Average hours worked in a week"

# The three aims KC-5.1.V.A prints, and the wording in the table that answers to
# each. The mapping is written out rather than guessed at by keyword, so a
# corrupted cell falls out of the mapping instead of quietly matching something.
AIMS = {
    "That the working day be shortened": "limit hours",
    "That wages be raised": "gain higher wages",
    "That the workrooms be made safer and better ventilated": "improve working conditions",
}

# The four types of reform KC-5.1.V.D names. Military is NOT among them; it
# belongs to KC-5.1.V.B, and that is what item 29 turns on.
VD_TYPES = {"Political", "Social", "Educational", "Urban"}

# What each type's measure must actually be about, so the table's labels are
# checked against its own descriptions rather than taken on trust. A label swapped
# between two rows -- the real defect a "which type is missing" item invites --
# fails here even though the set of types is unchanged.
TYPE_MARK = {"Political": "vote", "Social": "children", "Educational": "school",
             "Urban": "sewers", "Military": "army"}


def q11(table, item):
    """Membership rises at every step, hours fall at every step, and never to zero."""
    labels = cg.labels(table)
    assert labels == ["First decade", "Second decade", "Third decade", "Fourth decade"], \
        f"the four rows must be the four decades in order; got {labels}"
    members = cg.col(table, MEMBERS)
    hours = cg.col(table, HOURS)
    assert all(b > a for a, b in zip(members, members[1:])), \
        f"union membership must rise at every step; got {members}"
    assert all(b < a for a, b in zip(hours, hours[1:])), \
        f"the average hours worked must fall at every step; got {hours}"
    assert hours[-1] > 0, (
        f"the average hours worked must still be above zero in the last decade, or the "
        f"distractor claiming they reach zero would be true; got {hours[-1]}"
    )
    assert len(set(members)) > 1 and len(set(hours)) > 1, \
        "'neither figure changes' must be false"
    return (f"recomputed from the table: union membership {members} rises at every step while "
            f"average weekly hours {hours} fall at every step and end above zero")


def q28(table, item):
    """Three demands answer to one of the framework's three aims; exactly one does not."""
    demands = {str(row[0]): str(row[1]) for row in table["rows"]}
    assert sorted(demands) == ["Petition 1", "Petition 2", "Petition 3", "Petition 4"], \
        f"the four rows must be the four petitions; got {sorted(demands)}"
    matched = {lab: AIMS[text] for lab, text in demands.items() if text in AIMS}
    unmatched = sorted(lab for lab in demands if lab not in matched)
    assert unmatched == ["Petition 4"], (
        f"exactly one petition must fall outside KC-5.1.V.A's three aims, and it must be the "
        f"keyed one; got {unmatched}"
    )
    assert set(matched.values()) == {"limit hours", "gain higher wages",
                                     "improve working conditions"}, (
        f"the other three must cover the framework's three aims, one each, or the item has two "
        f"defensible answers; got {matched}"
    )
    assert "closed" in demands["Petition 4"].lower(), \
        f"the unmatched demand must be the one to close the mill; got {demands['Petition 4']!r}"
    return ("read from the table alone: three demands answer to KC-5.1.V.A's three aims, one "
            "each, and the fourth answers to none of them")


def q29(table, item):
    """Four measures carry KC-5.1.V.D's four types; exactly one carries a fifth."""
    kinds = {str(row[0]): str(row[1]) for row in table["rows"]}
    assert len(kinds) == 5, f"the table must hold five distinct measures; got {len(kinds)}"
    types = sorted(kinds.values())
    assert len(set(types)) == 5, f"each measure must carry a different type; got {types}"
    inside = {t for t in types if t in VD_TYPES}
    outside = sorted(t for t in types if t not in VD_TYPES)
    assert inside == VD_TYPES, (
        f"the table must carry all four of KC-5.1.V.D's types; got {sorted(inside)}"
    )
    assert outside == ["Military"], (
        f"exactly one type must sit outside that list, and it must be the keyed one; got {outside}"
    )
    for measure, kind in kinds.items():
        mark = TYPE_MARK[kind]
        assert mark in measure.lower(), (
            f"the measure labelled {kind!r} must actually be about {mark!r}, or the table's "
            f"labels are not checkable against its own descriptions; got {measure!r}"
        )
    army = [m for m, t in kinds.items() if t == "Military"]
    assert len(army) == 1, f"exactly one measure may carry the outside type; got {army}"
    return ("read from the table alone: four of the five types are KC-5.1.V.D's own, each "
            "matched to a measure that is genuinely about it, and the fifth is not among them")


CLAIMS = [
 ("social and economic changes brought about by industrial capitalism",
  "KC-5.1.V.D opens with the cause: in response to the social and economic changes brought about by industrial capitalism, some governments, organizations, and individuals promoted various reforms. The framework names no other occasion for them."),
 ("Some governments, organizations, and individuals",
  "KC-5.1.V.D names all three together and qualifies them with SOME. The framework neither universalizes the claim nor confines the reforms to a single kind of promoter, so no option naming one group alone can be keyed."),
 ("Political, social, educational, and urban",
  "KC-5.1.V.D lists exactly those four types of reform. Military reform appears in the framework only in KC-5.1.V.B, attached to governments in Asia and Africa rather than to this statement."),
 ("Industrial capitalism brought social and economic changes, and the reforms came in response to them",
  "KC-5.1.V.D begins IN RESPONSE TO the changes industrial capitalism brought, which puts the changes first. This topic's reasoning process is causation, and the anchor carries BOTH clauses because a distractor exchanges them."),
 ("part of them did so, and the framework does not claim all of them did",
  "KC-5.1.V.D writes SOME governments, organizations, and individuals, which limits the claim without counting anyone. The framework prints no figure, so neither a universal claim nor a proportion is keyable."),
 ("In industrialized states",
  "KC-5.1.V.A opens with the setting: in industrialized states, many workers organized themselves. The framework's account of the Ottoman Empire and Qing China is KC-5.1.V.B, a separate statement about governments rather than workers."),
 ("Often in labor unions",
  "KC-5.1.V.A says many workers organized themselves, OFTEN in labor unions. The adverb is the framework's own and stops short of always, which is the difference the two leading options turn on."),
 ("improve working conditions, limit hours, and gain higher wages",
  "KC-5.1.V.A names those three aims in that order. Suffrage, abolition and the end of serfdom belong to KC-5.3.I.C, the reform of economies and militaries to KC-5.1.V.B, and free trade to KC-5.1.III.A."),
 ("appeared in more than one place rather than in a single country",
  "KC-5.1.V.A says workers' movements and political parties emerged IN DIFFERENT AREAS and names none of those areas. The phrase asserts more than one place and nothing further, so a list of countries would come from outside the CED."),
 ("Alternative visions of society",
  "KC-5.1.V.A closes with the phrase: workers' movements and political parties emerged in different areas, promoting alternative visions of society. State-sponsored visions belong to KC-5.1.V.C and free trade to KC-5.1.III.A."),
 ("rises in every decade while the average hours worked in a week fall in every decade",
  "KC-5.1.V.A names limiting hours among the aims of workers who organized themselves, often in labor unions, and q11 above recomputes both columns from the table: membership rises at every step, hours fall at every step, and hours never reach zero. The table shows the movement and the framework supplies the aim."),
 ("Discontent with established power structures",
  "KC-5.3.IV.A.ii opens with the cause: discontent with established power structures encouraged the development of various ideologies. One distractor inverts the noun into its opposite, so the anchor carries the discontent itself."),
 ("Those espoused by Karl Marx",
  "KC-5.3.IV.A.ii names him: various ideologies, including those espoused by Karl Marx. Adam Smith is named in KC-5.1.III.A instead, in the framework's account of free trade and laissez-faire capitalism."),
 ("Socialism and communism",
  "KC-5.3.IV.A.ii names the ideas of socialism and communism. Democracy and 19th-century liberalism belong to KC-5.3.IV.A.i and laissez-faire capitalism to KC-5.1.III.A, so neither is keyable to this statement."),
 ("examples and the framework does not present them as the only ones",
  "KC-5.3.IV.A.ii says VARIOUS ideologies, INCLUDING those espoused by Karl Marx. Both words leave the list open, so a key treating the named ideas as exhaustive would claim more than the framework does."),
 ("Discontent with established power structures encouraged the development of the ideologies",
  "KC-5.3.IV.A.ii puts the discontent first and the ideologies second. The anchor carries both clauses because the distractor exchanges them, and this topic's reasoning process is causation."),
 ("The expansion of industrializing states",
  "KC-5.1.V.B opens with it: in response to the expansion of industrializing states, some governments in Asia and Africa sought to reform and modernize. The framework names no other occasion for those efforts."),
 ("The Ottoman Empire and Qing China",
  "KC-5.1.V.B names those two and no others. The framework's statement about internal reform in Japan is KC-5.2.II.A, printed on topic 5.6's page, which is what makes Japan a near miss rather than a second correct answer."),
 ("Their economies and militaries",
  "KC-5.1.V.B names both together: these governments sought to reform and modernize their economies and militaries. Religious instruction and land tenure appear nowhere in the statement."),
 ("often resisted by some members of government or established elite groups",
  "KC-5.1.V.B closes with that sentence. Both hedges are the framework's own, and the resistance it names comes from inside those states rather than from workers or from outside them."),
 ("were the only governments in Asia and Africa that sought such reform",
  "KC-5.1.V.B says SOME governments in Asia and Africa, INCLUDING the Ottoman Empire and Qing China. Both words leave the group open, so treating the two named states as the whole of it asserts what the CED does not print."),
 ("caused calls for change in industrial societies and what followed from them",
  "Unit 5 Learning Objective I asks students to explain the causes and effects of calls for changes in industrial societies from 1750 to 1900. The rejected questions belong to the objectives behind KC-5.1.I.A, KC-5.1.I.B, KC-5.1.I.D and KC-5.3.I.A."),
 ("workers organized themselves, often in labor unions, to limit hours",
  "KC-5.1.V.A names limiting hours among the aims of workers who organized themselves, often in labor unions. The handbill's audience is the workers of one mill and its purpose is to get them to combine, which is that statement and no other on the list."),
 ("A government's, illustrating the urban reforms promoted in response to industrial capitalism",
  "KC-5.1.V.D names urban reform among the four types promoted by some governments, organizations, and individuals in response to the changes industrial capitalism brought. A council writing to its own ratepayers about drains and paving is a government promoting that kind of reform."),
 ("sought to reform and modernize their economies and militaries in response to the expansion of industrializing states",
  "KC-5.1.V.B joins both halves in one sentence, and the memorial names the workshops and the army together. The anchor carries both clauses because a distractor reverses the response and the thing responded to."),
 ("often resisted by some members of government or established elite groups",
  "KC-5.1.V.B says reform efforts were often resisted by some members of government or established elite groups. Officials of a court objecting that established ranks would be unsettled are that resistance, arising inside the government rather than among workers or abroad."),
 ("discontent with established power structures encouraged the ideas of socialism and communism",
  "KC-5.3.IV.A.ii names the ideas of socialism and communism among the ideologies that discontent encouraged. A call for common ownership argues against the order itself rather than for terms within it, which separates it from the wage demands of KC-5.1.V.A."),
 ("the mill be closed and its machinery destroyed",
  "KC-5.1.V.A names three aims: improve working conditions, limit hours, and gain higher wages. q28 above matches three of the table's four demands to those aims, one each, and finds the fourth answering to none of them."),
 ("Military",
  "KC-5.1.V.D names political, social, educational, and urban reforms and no others. q29 above checks that the table carries all four of those plus exactly one further type, and that the further type is the one attached to the measure about the army."),
 ("Workers organized to change their conditions, some governments and individuals promoted reforms, discontent encouraged new ideologies",
  "The summary joins KC-5.1.V.A, KC-5.1.V.D, KC-5.3.IV.A.ii and KC-5.1.V.B, the four statements this topic prints, and keeps each hedge: some governments, many workers, and reform often resisted. Each rejected option contradicts one of the four."),
]

TABLE_CHECKS = {11: q11, 28: q28, 29: q29}


# --------------------------------------------------------------- local controls
# wh_check's own control corrupts a cell by APPENDING to it, which cannot express
# the two defects these three tables actually invite: a type label swapped between
# two rows, and a fourth petition that has quietly become a fourth match. Both are
# injected here, and each is required to raise FOR ITS OWN REASON -- a control
# that fires for the wrong reason proves nothing about the guard it names. The
# positive control runs first, so a check that rejected everything would fail here
# rather than look thorough.

def _local_controls():
    import copy

    def expect(label, table, fn, pattern):
        try:
            fn(table, None)
        except (AssertionError, KeyError) as exc:
            if not re.search(pattern, str(exc), re.I):
                raise SystemExit(
                    f"LOCAL CONTROL FAILED for 5.8 -- {label} raised for the WRONG reason.\n"
                    f"  wanted a message matching {pattern!r}\n  got: {exc}")
            return
        raise SystemExit(f"LOCAL CONTROL FAILED for 5.8 -- {label}: nothing raised")

    for name, table, fn in (("q11", w5_8._T_UNIONS, q11),
                            ("q28", w5_8._T_PETITIONS, q28),
                            ("q29", w5_8._T_MEASURES, q29)):
        note = fn(copy.deepcopy(table), None)
        assert isinstance(note, str) and note.split(), f"{name} returned no note"
    print("  local positive control OK  all three table checks pass on the real tables")

    # 1. two type labels exchanged. The SET of types is unchanged, so a check
    #    reading the type column alone would not notice; TYPE_MARK is what does.
    swapped = copy.deepcopy(w5_8._T_MEASURES)
    swapped["rows"][0][1], swapped["rows"][4][1] = (swapped["rows"][4][1],
                                                    swapped["rows"][0][1])
    expect("q29 with Political and Military labels exchanged", swapped, q29,
           r"must actually be about")

    # 2. the fourth petition made to match one of the framework's three aims, so
    #    NOTHING falls outside them and the keyed choice becomes false.
    matched = copy.deepcopy(w5_8._T_PETITIONS)
    matched["rows"][3][1] = "That wages be raised"
    expect("q28 with every petition matching an aim", matched, q28,
           r"must fall outside")

    # 3. one hours cell moved so the column no longer falls at every step.
    bumpy = copy.deepcopy(w5_8._T_UNIONS)
    bumpy["rows"][2][2] = "70"
    expect("q11 with the hours column no longer falling", bumpy, q11,
           r"fall at every step")
    print("  local control OK  a swapped type label, a fourth matching petition and a "
          "non-falling hours column each raise, each for its own reason")


if "--selftest" in sys.argv:
    _local_controls()

wh.run(w5_8, CLAIMS, TABLE_CHECKS, sys.argv)
