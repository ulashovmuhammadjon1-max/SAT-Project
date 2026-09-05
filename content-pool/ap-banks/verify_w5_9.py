"""Key audit for AP WORLD HISTORY: MODERN 5.9 Society and the Industrial Age.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim cites the Key Concept or Learning
Objective the key traces to.

WHAT THE KEYS REST ON
---------------------
Three statements, and every key traces to one of them or to Unit 5 Learning
Objective J:

  KC-5.1.VI.A  New social classes, INCLUDING the middle class and the industrial
               working class, developed.
  KC-5.1.VI.B  While women and OFTEN children in working class families TYPICALLY
               held wage-earning jobs to supplement their families' income,
               middle-class women WHO DID NOT HAVE THE SAME ECONOMIC DEMANDS TO
               SATISFY were INCREASINGLY LIMITED to roles in the household or
               roles focused on child development.
  KC-5.1.VI.C  The rapid urbanization that ACCOMPANIED global capitalism AT TIMES
               led to a variety of challenges, INCLUDING pollution, poverty,
               increased crime, public health crises, housing shortages, and
               insufficient infrastructure to accommodate urban growth.

The CED prints NO illustrative example on this topic's page and no date anywhere
in it, so no key here names a city, a survey, a reformer or a year.

THE HEDGES ARE THE CONTENT
--------------------------
KC-5.1.VI.B is a single sentence carrying four qualifications, and stripping any
one of them yields a claim that reads perfectly well and is not the framework's.
Items 3, 9, 10, 11, 16 and 17 each key one of the six hedges above, and items 25
and 26 make two of them into goes-beyond items, so the qualification is keyed
rather than merely noted in a comment.

THE SWAP
--------
KC-5.1.VI.B contrasts two groups of women in one sentence and exchanging them is
the easiest wrong key in this topic. Item 8 carries the exchange as a distractor
and its anchor carries BOTH clauses, which is the defect found in
verify_e2_1.py. Item 18 does the same for KC-5.1.VI.C's causal direction.

TWO DIFFERENT RELATIONS IN ONE SENTENCE
---------------------------------------
KC-5.1.VI.C says the urbanization ACCOMPANIED global capitalism and that it AT
TIMES LED TO the challenges. Item 20 keys the first relation and item 18 the
second; nothing here makes global capitalism the cause of the urbanization or the
urbanization the cause of global capitalism, because the framework's verb is
accompanied and it commits to neither direction.

WHY THE TABLE CONTROL DOES NOT CATCH EVERY CELL
-----------------------------------------------
The selftest prints a per-table catch rate rather than requiring one hundred
percent. Raising a value that is already the largest in an already-ordered
column, or appending words to a prose cell that is still recognisably about the
same thing, can leave the keyed conclusion TRUE of the corrupted table; a check
that fired on those would be reporting a defect that is not there. What the
control requires is that no table sits undefended, and the printed count is what
makes a check that has stopped reading its table show up as a zero. The local
controls at the foot of this file inject the two defects the APPEND-style
corruption cannot express -- a row order reversed, and a fifth report quietly
made to match a named challenge -- and require each to raise for its own reason.

FIVE choices per item (A-E); see HISTORY_BRIEF.md.
"""
import copy
import re
import sys

import cg_check as cg
import wh_check as wh
import w5_9

MIDDLE = "Households counted as middle class (percent)"
WORKING = "Households counted as industrial working class (percent)"
RURAL = "Households in older rural occupations (percent)"
SHARE = "Share holding wage-earning jobs (percent)"

# The six challenges KC-5.1.VI.C prints, and the wording in the table that answers
# to each. Written out rather than guessed at by keyword, so a corrupted cell falls
# out of the mapping instead of quietly matching something it should not.
CHALLENGES = {
    "Smoke and fouled water": "pollution",
    "Families crowded for want of houses": "housing shortages",
    "Deaths from fever spreading through a district": "public health crises",
    "A rise in the number of thefts": "increased crime",
}


def q27(table, item):
    """Both new classes rise at every step, the older rural share falls, rows total 100."""
    labels = cg.labels(table)
    assert labels == ["First decade", "Second decade", "Third decade", "Fourth decade"], \
        f"the four rows must be the four decades in order; got {labels}"
    middle = cg.col(table, MIDDLE)
    working = cg.col(table, WORKING)
    rural = cg.col(table, RURAL)
    for series, name in ((middle, "middle class"), (working, "industrial working class")):
        assert all(b > a for a, b in zip(series, series[1:])), \
            f"the {name} share must rise at every step; got {series}"
    assert all(b < a for a, b in zip(rural, rural[1:])), \
        f"the older rural share must fall at every step; got {rural}"
    for lab, m, w, r in zip(labels, middle, working, rural):
        assert m + w + r == 100, (
            f"the three shares in {lab} must account for the whole society, or a share is not a "
            f"share; got {m} + {w} + {r} = {m + w + r}"
        )
    assert rural[-1] > 0, (
        f"the older rural share must still be above zero in the last decade, or the distractor "
        f"claiming it reaches zero would be true; got {rural[-1]}"
    )
    return (f"recomputed from the table: the middle class share {middle} and the industrial "
            f"working class share {working} each rise at every step while the older rural share "
            f"{rural} falls at every step, and every row totals 100")


def q28(table, item):
    """Four reports answer to a named challenge; exactly one answers to none."""
    reports = {str(row[0]): str(row[1]) for row in table["rows"]}
    assert sorted(reports) == ["Report 1", "Report 2", "Report 3", "Report 4", "Report 5"], \
        f"the five rows must be the five reports; got {sorted(reports)}"
    matched = {lab: CHALLENGES[text] for lab, text in reports.items() if text in CHALLENGES}
    unmatched = sorted(lab for lab in reports if lab not in matched)
    assert unmatched == ["Report 5"], (
        f"exactly one report must fall outside KC-5.1.VI.C's named challenges, and it must be "
        f"the keyed one; got {unmatched}"
    )
    assert len(set(matched.values())) == 4, (
        f"the other four must answer to four DIFFERENT named challenges, or the item has two "
        f"defensible answers; got {matched}"
    )
    assert "countryside" in reports["Report 5"].lower(), (
        f"the unmatched report must be the one about the countryside, so the sorting is legible "
        f"from the table; got {reports['Report 5']!r}"
    )
    return ("read from the table alone: four reports answer to four different challenges "
            "KC-5.1.VI.C names, and the fifth answers to none of them")


def q29(table, item):
    """Working class women rank highest, middle class women lowest, all three distinct."""
    labels = cg.labels(table)
    assert labels == ["Women in working class families", "Children in working class families",
                      "Women in middle class families"], \
        f"the three rows must be the three groups of the survey; got {labels}"
    shares = cg.col(table, SHARE)
    assert len(set(shares)) == 3, (
        f"the three shares must differ, or 'equal shares' would be defensible; got {shares}"
    )
    order = cg.ranked(table, SHARE)
    assert order[0] == "Women in working class families", (
        f"working class women must hold the highest share, or the first half of the key is "
        f"false; the ranking is {order}"
    )
    assert order[-1] == "Women in middle class families", (
        f"middle class women must hold the lowest share, or the second half of the key is false; "
        f"the ranking is {order}"
    )
    assert min(shares) > 0, "'no group holds a wage-earning job' must be false"
    return (f"recomputed from the table: ranked by share the order is {order}, so working class "
            f"women stand highest and middle class women lowest")


CLAIMS = [
 ("New social classes, including the middle class and the industrial working class",
  "KC-5.1.VI.A is one short sentence and says exactly that: new social classes, including the middle class and the industrial working class, developed. Each rejected option denies that new and distinct classes appeared."),
 ("The middle class and the industrial working class",
  "KC-5.1.VI.A names those two and no others, and describes them as NEW. That is what separates them from the older groups the rejected options name."),
 ("examples and the framework does not say they were the only new classes",
  "KC-5.1.VI.A says new social classes, INCLUDING the middle class and the industrial working class. The word leaves the list open, so treating the two as the whole of it asserts more than the framework does."),
 ("Wage-earning jobs",
  "KC-5.1.VI.B opens with it: women and often children in working class families typically held wage-earning jobs. The statement mentions no other holding for those families."),
 ("To supplement their families' income",
  "KC-5.1.VI.B gives the purpose in the same clause. Suffrage belongs to KC-5.3.I.C and labor unions to KC-5.1.V.A, and neither is offered by the framework as a reason for this work."),
 ("Roles in the household or roles focused on child development",
  "KC-5.1.VI.B closes with those two roles and names no third. Wage-earning work is what the same sentence attaches to working class families, which is the contrast the statement is built on."),
 ("did not have the same economic demands to satisfy",
  "KC-5.1.VI.B supplies the reason itself, in the relative clause describing middle-class women. The rejected options are reasons the framework nowhere gives."),
 ("Working class women typically held wage-earning jobs, while middle-class women were increasingly limited to roles in the household",
  "KC-5.1.VI.B contrasts the two groups in one sentence and exchanging them is the easiest wrong key in this topic, so the anchor carries BOTH clauses. The framework attaches wage-earning work to working class families and household roles to middle-class women."),
 ("children frequently did so, without the framework claiming all of them did",
  "KC-5.1.VI.B qualifies only the children with OFTEN and prints no figure for either group. The sentence supports neither a universal claim about children nor any comparison of how frequently the two groups worked."),
 ("the usual case rather than a universal one",
  "KC-5.1.VI.B says TYPICALLY held wage-earning jobs. The adverb describes the usual case and stops there, and the framework supplies no count anywhere in the statement."),
 ("a trend growing over time rather than a fixed condition",
  "KC-5.1.VI.B says INCREASINGLY limited, a direction of change rather than a settled state, and this topic's reasoning process is continuity and change. The same sentence attaches wage-earning work to working class families, so the limitation is not described as applying to them equally."),
 ("Global capitalism",
  "KC-5.1.VI.C opens with the phrase: the rapid urbanization that ACCOMPANIED global capitalism. The verb places the two side by side without making either the cause of the other."),
 ("A variety of challenges",
  "KC-5.1.VI.C says the rapid urbanization at times led to a variety of challenges, and then lists them. Each rejected option contradicts that outcome rather than qualifying it."),
 ("Pollution, poverty, increased crime, public health crises and housing shortages",
  "KC-5.1.VI.C prints pollution, poverty, increased crime, public health crises, housing shortages, and insufficient infrastructure to accommodate urban growth. The rejected sets name difficulties the framework does not attach to urbanization here."),
 ("Insufficient infrastructure to accommodate urban growth",
  "KC-5.1.VI.C closes its list with that phrase. It is the sixth item the framework prints, and none of the rejected options appears in the statement at all."),
 ("an outcome that sometimes followed rather than one that always did",
  "KC-5.1.VI.C says AT TIMES led to a variety of challenges. The phrase limits how often the outcome followed, and the framework supplies no dates, so neither a universal nor a dated claim is keyable."),
 ("the list gives examples and the framework does not present it as complete",
  "KC-5.1.VI.C says a VARIETY of challenges, INCLUDING the six it then names. Both words leave the list open, and the framework neither ranks the six nor attaches them to a named place."),
 ("rapid urbanization came first and at times led to those challenges",
  "KC-5.1.VI.C puts the rapid urbanization first and the challenges second, keeping the qualification at times. The anchor carries both clauses because a distractor exchanges them."),
 ("changed existing social hierarchies and standards of living",
  "Unit 5 Learning Objective J asks students to explain how industrialization caused change in existing social hierarchies and standards of living. The rejected questions belong to the objectives behind KC-5.1.I.A, KC-5.1.III.A, KC-5.3 and KC-5.1.I.B."),
 ("Global capitalism, which the framework says that urbanization accompanied",
  "KC-5.1.VI.C situates the urbanization itself: the rapid urbanization that accompanied global capitalism. The rejected options are the broader contexts of KC-5.1.III.A, KC-5.1.V.B, KC-5.3 and KC-5.3.I, none of which the framework attaches to urban growth."),
 ("new social classes, including the middle class and the industrial working class, developed",
  "KC-5.1.VI.A states it in those words. A directory recording two growing groups of townspeople beside the older trades is that development as it would appear in a record of the period."),
 ("children in working class families typically held wage-earning jobs to supplement their families' income",
  "KC-5.1.VI.B attaches wage-earning work to women and often children in working class families and gives supplementing the family's income as its purpose. A budget with three sets of earnings in one household is that arrangement written down."),
 ("middle-class women were increasingly limited to roles in the household or roles focused on child development",
  "KC-5.1.VI.B names exactly those two roles for middle-class women, and the manual's two subjects are those two roles. Its intended readers are the group the framework's clause is about."),
 ("housing shortages, pollution and insufficient infrastructure",
  "KC-5.1.VI.C names housing shortages, pollution and insufficient infrastructure to accommodate urban growth among the challenges rapid urbanization at times brought. Cellars used as dwellings, a fouled water supply and streets without drains are those three together."),
 ("every middle-class woman was barred from paid employment",
  "KC-5.1.VI.B says middle-class women were INCREASINGLY LIMITED to certain roles, which describes a trend and not a prohibition. The framework states the other four claims and supplies the reason itself."),
 ("followed in every town that grew during the period",
  "KC-5.1.VI.C says the urbanization AT TIMES led to those challenges and names no town. Turning that into a claim about every growing town drops the framework's own qualification."),
 ("rise in every decade while the share in older rural occupations falls in every decade",
  "KC-5.1.VI.A says new social classes, including the middle class and the industrial working class, developed, and q27 above recomputes the sample: both new shares rise at every step, the older rural share falls at every step, every row totals 100, and the rural share never reaches zero."),
 ("shortage of laborers in the surrounding countryside",
  "KC-5.1.VI.C lists pollution, poverty, increased crime, public health crises, housing shortages, and insufficient infrastructure. q28 above matches four of the reports to four DIFFERENT named challenges and finds the fifth matching none of them."),
 ("highest among women in working class families and lowest among women in middle class families",
  "KC-5.1.VI.B attaches wage-earning work to women and often children in working class families and household roles to middle-class women, and q29 above ranks the survey's one numeric column. The anchor carries both ends because a distractor reverses one of them."),
 ("rapid urbanization at times brought pollution, poverty, crime, disease, housing shortages and strained infrastructure",
  "The summary joins KC-5.1.VI.A, KC-5.1.VI.B and KC-5.1.VI.C, the three statements this topic prints, and keeps the qualification at times on the last. Each rejected option contradicts one of the three."),
]

TABLE_CHECKS = {27: q27, 28: q28, 29: q29}


# --------------------------------------------------------------- local controls
# wh_check's own control corrupts a cell by APPENDING to it or by scaling a
# number. Neither can express the two defects these tables actually invite: a row
# order that has been reversed while the values stay legal, and a fifth report
# that has quietly become a fourth match. Both are injected here and each must
# raise FOR ITS OWN REASON -- a control that fires for the wrong reason proves
# nothing about the guard it names. The positive control runs first, so a check
# that rejected everything would fail here rather than look thorough.

def _local_controls():
    def expect(label, table, fn, pattern):
        try:
            fn(table, None)
        except (AssertionError, KeyError) as exc:
            if not re.search(pattern, str(exc), re.I):
                raise SystemExit(
                    f"LOCAL CONTROL FAILED for 5.9 -- {label} raised for the WRONG reason.\n"
                    f"  wanted a message matching {pattern!r}\n  got: {exc}")
            return
        raise SystemExit(f"LOCAL CONTROL FAILED for 5.9 -- {label}: nothing raised")

    for name, table, fn in (("q27", w5_9._T_CLASSES, q27),
                            ("q28", w5_9._T_REPORTS, q28),
                            ("q29", w5_9._T_SURVEY, q29)):
        note = fn(copy.deepcopy(table), None)
        assert isinstance(note, str) and note.split(), f"{name} returned no note"
    print("  local positive control OK  all three table checks pass on the real tables")

    # 1. the survey's rows reordered so the middle class group is no longer last.
    #    Every value is still legal, so only the RANKING check can see it.
    reordered = copy.deepcopy(w5_9._T_SURVEY)
    reordered["rows"] = [reordered["rows"][2], reordered["rows"][1], reordered["rows"][0]]
    expect("q29 with the survey rows reversed", reordered, q29, r"three rows must be")

    # 2. the same reversal expressed as VALUES rather than row order: the shares
    #    swapped between the working class and middle class women. The row labels
    #    are untouched, so the label check cannot fire and the ranking must.
    swapped = copy.deepcopy(w5_9._T_SURVEY)
    swapped["rows"][0][1], swapped["rows"][2][1] = (swapped["rows"][2][1],
                                                    swapped["rows"][0][1])
    expect("q29 with the two women's shares exchanged", swapped, q29,
           r"must hold the highest share")

    # 3. the fifth report made to match a challenge the framework names, so
    #    NOTHING falls outside the list and the keyed choice becomes false.
    matched = copy.deepcopy(w5_9._T_REPORTS)
    matched["rows"][4][1] = "A rise in the number of thefts"
    expect("q28 with every report matching a named challenge", matched, q28,
           r"must fall outside")

    # 4. a class share moved so the three no longer account for the whole society.
    #    The columns still rise and fall correctly, so only the total can catch it.
    unbalanced = copy.deepcopy(w5_9._T_CLASSES)
    unbalanced["rows"][1][1] = "12"
    expect("q27 with a decade's shares no longer totalling 100", unbalanced, q27,
           r"must account for the whole society")
    print("  local control OK  a reordered survey, exchanged shares, a fifth matching report "
          "and an unbalanced decade each raise, each for its own reason")


if "--selftest" in sys.argv:
    _local_controls()

wh.run(w5_9, CLAIMS, TABLE_CHECKS, sys.argv)
