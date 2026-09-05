"""Key audit for AP WORLD HISTORY: MODERN 5.10 Continuity and Change in the Industrial Age.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim cites the Key Concept or Learning
Objective the key traces to.

THIS IS THE UNIT'S REASONING TOPIC
----------------------------------
The CED says so on the topic page: the final topic focuses on the skill of
argumentation and gives students an opportunity to draw on the key concepts of
the unit, using evidence relevant to them. So the module is a question SET about
evidence and argument, not a recall bank -- recall of these statements belongs to
topics 5.1 through 5.9. Every key here is one of two kinds, and each kind is
checkable:

  1. WHAT THE FRAMEWORK'S OWN WORDING ALLOWS. "For some", "at times", "often
     preceded" and "accompanied" are limits on an inference, and an argument that
     drops one is wrong against the CED rather than merely against taste. Items
     2, 4, 5, 9, 13, 20, 26 and 29 turn on a qualification the framework prints.
  2. WHETHER THE CLAIM MATCHES THE SCOPE OF THE EVIDENCE. A record of one
     district reaches that district; a memoir reaches the family that wrote it;
     two columns rising together are two columns rising together. Items 7, 18,
     24, 25 and 26 turn on that, which is skill 6.C stated plainly.

REVIEW: UNIT 5 KEY CONCEPTS, the heading the CED prints on this page in place of
"Historical Developments":

  KC-5.1       industrial capitalism -> increased standards of living FOR SOME,
               and continued improvement in manufacturing methods that increased
               the availability, affordability, and variety of consumer goods.
  KC-5.1.IV    railroads, steamships and the telegraph made exploration,
               development and communication possible in interior regions
               globally, WHICH LED TO increased trade and migration.
  KC-5.3       the 18th century marked the beginning of an intense period of
               revolution and rebellion against existing governments, leading to
               the establishment of new nation-states around the world.
  KC-5.3.I.A   Enlightenment philosophies ... philosophers developed new political
               ideas about the individual, natural rights, and the social contract.
  KC-5.3.I     the rise and diffusion of Enlightenment thought OFTEN PRECEDED
               revolutions and rebellions against existing governments.
  KC-5.3.II.i  nationalism also became a major force shaping the historical
               development of states and empires.

Because the CED instructs students to draw on everything studied in the unit,
several items reason from KC-5.1.II.B, KC-5.1.VI.A and KC-5.1.VI.C as well. All
are unit 5 statements; nothing is taken from unit 6.

NO DATE IS KEYED, AND ITEM 22 IS WHY
------------------------------------
The CED states that its developments are not constrained by the given dates and
may begin before or continue after the period. Item 22 keys that statement
itself, so the rule appears in the bank as content rather than only as a
convention; no other item rests on a boundary year.

WHY THE TABLE CONTROL DOES NOT CATCH EVERY CELL
-----------------------------------------------
The selftest prints a per-table catch rate rather than requiring one hundred
percent. Raising a value that is already the largest in an already-ordered column
can leave the keyed conclusion TRUE of the corrupted table, and a check that
fired on that would be reporting a defect that is not there. The local controls
at the foot of this file inject the three defects the APPEND-and-scale style of
corruption cannot express -- a spread flattened so the regions no longer differ,
a district set that has become uniform, and a column that no longer rises -- and
require each to raise for its own reason.

FIVE choices per item (A-E); see HISTORY_BRIEF.md.
"""
import copy
import re
import sys

import cg_check as cg
import wh_check as wh
import w5_10

START = "Index of manufacturing output, start of the period"
END = "Index of manufacturing output, end of the period"
FACTORY = "Share of cloth made in factories (percent)"
HOUSEHOLD = "Share of cloth made in households (percent)"
TONNAGE = "Tonnage of goods carried inland (thousands)"
PERSONS = "Persons recorded migrating into the interior (thousands)"


def q15(table, item):
    """Every region rises, and the rises differ by several times over."""
    labels = cg.labels(table)
    assert labels == ["Region 1", "Region 2", "Region 3", "Region 4"], \
        f"the four rows must be the four regions in order; got {labels}"
    start = cg.col(table, START)
    end = cg.col(table, END)
    assert all(s > 0 for s in start), f"every starting index must be positive; got {start}"
    assert all(e > s for s, e in zip(start, end)), (
        f"every region must end higher than it started, or 'rose in every region' is false; "
        f"got start {start} and end {end}"
    )
    growth = [e / s for s, e in zip(start, end)]
    assert max(growth) >= 3 * min(growth), (
        f"the largest rise must be several times the smallest, or 'by amounts so different' is "
        f"not supported; got growth factors {growth}"
    )
    return (f"recomputed from the table: every region's index rises (start {start}, end {end}) "
            f"and the growth factors {[round(g, 2) for g in growth]} differ by more than "
            f"threefold across the sample")


def q16(table, item):
    """Some districts are mostly factory made, others mostly household made; rows total 100."""
    labels = cg.labels(table)
    assert labels == ["District 1", "District 2", "District 3", "District 4"], \
        f"the four rows must be the four districts in order; got {labels}"
    factory = cg.col(table, FACTORY)
    household = cg.col(table, HOUSEHOLD)
    for lab, f, h in zip(labels, factory, household):
        assert f + h == 100, (
            f"the two shares in {lab} must account for all of that district's cloth; "
            f"got {f} + {h} = {f + h}"
        )
    mostly_factory = [lab for lab, f in zip(labels, factory) if f > 50]
    mostly_household = [lab for lab, h in zip(labels, household) if h > 50]
    # These two assertions carry the whole item, and between them they falsify all
    # four distractors, because every row already totals 100. If no district were
    # mostly household made the first would fire; if none were mostly factory made
    # the second would; if the two shares were equal everywhere BOTH lists would be
    # empty and the first would fire. Separate assertions worded for "predominates
    # in every district", "the shares are equal in every district" and "household
    # production has disappeared" were written here first and then removed: with
    # the row totals fixed at 100 none of them could ever be reached, and an
    # assertion that cannot fail is worse than none because it reads like cover.
    assert mostly_factory, (
        f"at least one district must be mostly factory made, or the first half of the keyed "
        f"conclusion is false; got factory shares {factory}"
    )
    assert mostly_household, (
        f"at least one district must be mostly household made, or the second half of the keyed "
        f"conclusion is false; got household shares {household}"
    )
    return (f"recomputed from the table: {mostly_factory} are mostly factory made and "
            f"{mostly_household} mostly household made, and every row totals 100, which "
            f"falsifies every 'in every district' reading at once")


def q17(table, item):
    """Both columns rise at every step, so neither reversal nor a flat reading survives."""
    labels = cg.labels(table)
    assert labels == ["First decade", "Second decade", "Third decade", "Fourth decade"], \
        f"the four rows must be the four decades in order; got {labels}"
    tonnage = cg.col(table, TONNAGE)
    persons = cg.col(table, PERSONS)
    for series, name in ((tonnage, "tonnage carried inland"),
                         (persons, "persons migrating inland")):
        assert all(b > a for a, b in zip(series, series[1:])), \
            f"the {name} column must rise at every step; got {series}"
    assert len(set(tonnage)) > 1 and len(set(persons)) > 1, \
        "'neither figure changes' must be false"
    return (f"recomputed from the table: tonnage {tonnage} and persons {persons} each rise at "
            f"every step, so no reading in which one falls or neither moves survives")


CLAIMS = [
 ("weigh how much changed against what stayed the same",
  "Unit 5 Learning Objective K asks for the EXTENT to which industrialization brought change, and the reasoning process assigned to this topic is continuity and change. A question about extent is answered by weighing, not by asserting either extreme."),
 ("increased standards of living for some",
  "KC-5.1 is printed among this topic's review statements and it says FOR SOME. The student's claim is that statement with the qualification removed, so the framework's own wording is what limits it."),
 ("more cargo and more travellers moving through places newly reached by rail and telegraph",
  "KC-5.1.IV says these technologies made exploration, development and communication possible in interior regions globally, which led to increased trade and migration. Evidence of traffic through newly reached places is evidence about that claim."),
 ("whose earnings bought no more at the end of the period than at the start",
  "KC-5.1 says industrial capitalism raised living standards FOR SOME, so a claim about EVERY household is one a single counterexample defeats. Unit 5 Learning Objective K makes the extent of the change the question at issue."),
 ("the gain did not reach every household",
  "KC-5.1 pairs cheaper and more plentiful consumer goods with a rise in living standards FOR SOME. Two sources of this kind do not conflict; together they state the framework's qualified sentence in evidence."),
 ("continued to produce manufactured goods by older methods throughout the period",
  "KC-5.1.II.B says regions whose share of global manufacturing declined CONTINUED to produce manufactured goods, and Unit 5 Learning Objective K asks for the extent of change, which includes what persisted. Every rejected option is evidence of change rather than continuity."),
 ("cloth output rose in that district over those decades",
  "This topic's skill is reasoning about what evidence establishes, and a record of one district reaches as far as that district. KC-5.1 attaches living standards to a separate and separately qualified claim, so output figures alone do not settle it."),
 ("Enlightenment thought often preceded revolutions and rebellions",
  "KC-5.3.I, printed among this topic's review statements, connects the diffusion of Enlightenment thought with revolutions and rebellions against existing governments. The rejected statements are KC-5.1.IV, KC-5.1, KC-5.1.VI.A and KC-5.1.VI.C."),
 ("the sequence was common, not that the thought caused the rebellion in any given case",
  "KC-5.3.I says OFTEN PRECEDED, which reports an order and how frequently it held rather than a mechanism. A statement about what commonly came first cannot by itself settle causation in one instance."),
 ("revolution and rebellion led to the establishment of new nation-states",
  "KC-5.3 is printed among this topic's review statements and is the one ending in new nation-states around the world. The rejected options are KC-5.1, KC-5.1.IV and KC-5.1.VI.B, which bear on production, transport and social roles."),
 ("nationalism became a major force shaping the historical development of states and empires",
  "KC-5.3.II.i is printed among this topic's review statements and names nationalism as that force. Every rejected option comes from KC-5.1 or KC-5.1.IV, which are about production, goods and technology."),
 ("new political ideas about the individual, natural rights and the social contract",
  "KC-5.3.I.A names those ideas and emphasizes the importance of reason. The source is illustrative and unattributed, and the key rests on what it argues rather than on who wrote it."),
 ("may be accurate of different parts of the same town",
  "KC-5.1 says living standards rose FOR SOME and KC-5.1.VI.C says rapid urbanization AT TIMES brought pollution and housing shortages. Both qualifications allow the two reports to stand together, and Unit 5 Learning Objective K makes the extent of improvement the question."),
 ("how two records of the same development bear on one another",
  "The CED assigns skill 6.C to this topic, describing it as using historical reasoning to explain relationships among pieces of historical evidence, in service of Unit 5 Learning Objective K. Listing, counting and summarizing leave the relationship unexplained."),
 ("rose in every region, but by amounts so different that a claim of uniform transformation is not supported",
  "Unit 5 Learning Objective K asks for the extent of change, and q15 above recomputes both halves of the keyed conclusion from the table: every region ends higher than it started, and the growth factors differ by more than threefold."),
 ("predominates in some districts while household production still predominates in others",
  "KC-5.1.II.B describes regions that CONTINUED to produce manufactured goods as the new methods spread, and q16 above sorts the table district by district, checking that the two shares in each row account for all of that district's cloth."),
 ("tonnage carried inland and the number of people migrating inland both rise in every decade",
  "KC-5.1.IV says the new transport and communication led to increased trade and migration, and q17 above recomputes both columns as rising at every step. The keyed conclusion is about the figures themselves, which is all a table of this kind can establish."),
 ("were the cause of the two increases",
  "KC-5.1.IV supplies the causal claim; a table of two rising columns supplies only the two rising columns. Skill 6.C asks students to reason about what evidence does and does not establish, and this is the distinction it turns on most often."),
 ("belong to one connected development",
  "KC-5.1.IV is a single sentence in which the technologies make exploration, development and communication possible in interior regions globally, WHICH LED TO increased trade and migration. Explaining that relationship is skill 6.C; the rejected options break the sentence or reverse it."),
 ("living standards rose for some and that urbanization at times brought difficulties",
  "KC-5.1 says FOR SOME and KC-5.1.VI.C says AT TIMES. Those qualifications are printed in the framework, so an objection built on them argues from the course content rather than from an author's opinion."),
 ("factory production grew alongside older methods that persisted",
  "The evidence contains both halves, so the claim matching it contains both halves too. KC-5.1.II.B describes exactly that combination, and Unit 5 Learning Objective K asks how far the change went."),
 ("not rest on a development having started or stopped exactly at a boundary year",
  "Unit 5 Learning Objective K asks about change from 1750 to 1900, and the CED itself states that its developments may begin before or continue after the period. An argument keyed to a boundary year would contradict that statement."),
 ("where and how goods were produced across three generations",
  "KC-5.1 describes continued improvement in manufacturing methods and KC-5.1.VI.A the growth of an industrial working class. A household that spun at home giving way to children in a mill is that shift within one family."),
 ("the same change occurred at the same time everywhere else",
  "Skill 6.C asks students to reason about what evidence establishes, and one family's memoir reaches as far as that family. KC-5.1.II.B shows why the wider claim needs separate support, since regions differed and some continued producing by older methods."),
 ("independent of the first, of goods moving through the town before and after the line opened",
  "KC-5.1.IV connects the arrival of such transport with increased trade, but the student's single record shows only the arrival. Skill 6.C concerns the relationship between pieces of evidence, and an independent record of the traffic supplies the missing half."),
 ("which is not by itself evidence that one produced the other",
  "The framework distinguishes the two relations itself: KC-5.1.VI.C says rapid urbanization ACCOMPANIED global capitalism while KC-5.1.IV says the new transport LED TO increased trade and migration. Skill 6.C asks students to tell those apart rather than assume the stronger one."),
 ("rising steeply in some regions and barely at all in others",
  "KC-5.1.II.B describes a period in which some regions' share of global manufacturing grew while others' declined even as they continued to produce, and Unit 5 Learning Objective K asks for the extent of change. A comparison across regions is what a claim about unevenness requires."),
 ("went on producing manufactured goods by the methods they had long used",
  "KC-5.1.II.B says those regions CONTINUED to produce manufactured goods, which is the framework's own statement of persistence. The rejected options come from KC-5.1.VI.A, KC-5.1.IV, KC-5.3 and KC-5.1.I.E, and each asserts something new."),
 ("the framework's own qualifications keep it from being uniform or universal",
  "KC-5.1, KC-5.1.IV and KC-5.3 each assert a substantial change, while for some, at times and continued to produce qualify how far those changes reached. Unit 5 Learning Objective K asks precisely for that judgement of extent."),
 ("reason about how the pieces of that evidence bear on a claim about the extent of change",
  "The CED introduces this topic by saying it focuses on argumentation and lets students draw on the unit's key concepts, using evidence relevant to them. Unit 5 Learning Objective K supplies the claim at issue and skill 6.C the reasoning about how the evidence relates."),
]

TABLE_CHECKS = {15: q15, 16: q16, 17: q17}


# --------------------------------------------------------------- local controls
# wh_check's own control corrupts a cell by APPENDING to it or by scaling a number
# upward. Neither can express the three defects these tables actually invite: a
# spread flattened so the regions no longer differ, a district set that has become
# uniform, and a column that no longer rises at every step. Each is injected here
# and each must raise FOR ITS OWN REASON -- a control that fires for the wrong
# reason proves nothing about the guard it names. The positive control runs first,
# so a check that rejected everything would fail here rather than look thorough.

def _local_controls():
    def expect(label, table, fn, pattern):
        try:
            fn(table, None)
        except (AssertionError, KeyError, ZeroDivisionError) as exc:
            if not re.search(pattern, str(exc), re.I):
                raise SystemExit(
                    f"LOCAL CONTROL FAILED for 5.10 -- {label} raised for the WRONG reason.\n"
                    f"  wanted a message matching {pattern!r}\n  got: {exc}")
            return
        raise SystemExit(f"LOCAL CONTROL FAILED for 5.10 -- {label}: nothing raised")

    for name, table, fn in (("q15", w5_10._T_REGIONS, q15),
                            ("q16", w5_10._T_DISTRICTS, q16),
                            ("q17", w5_10._T_INLAND, q17)):
        note = fn(copy.deepcopy(table), None)
        assert isinstance(note, str) and note.split(), f"{name} returned no note"
    print("  local positive control OK  all three table checks pass on the real tables")

    # 1. the spread flattened. Every region still rises, so the 'rose in every
    #    region' half is untouched and only the 'by amounts so different' half can
    #    fail -- which is exactly the half the key rests on.
    flat = copy.deepcopy(w5_10._T_REGIONS)
    for row in flat["rows"]:
        row[2] = "130"
    expect("q15 with every region rising by the same amount", flat, q15,
           r"several times the smallest")

    # 2. one region made to fall, so 'rose in every region' fails and the message
    #    must name THAT half rather than the spread.
    falling = copy.deepcopy(w5_10._T_REGIONS)
    falling["rows"][3][2] = "88"
    expect("q15 with one region falling", falling, q15, r"end higher than it started")

    # 3. every district made mostly factory made, so the keyed 'some ... others'
    #    reading is false while every row still totals 100. Both directions are
    #    injected, because the two halves of the key are guarded by two different
    #    assertions and a control that only ever exercised one would say nothing
    #    about the other.
    uniform_factory = copy.deepcopy(w5_10._T_DISTRICTS)
    for row in uniform_factory["rows"]:
        row[1], row[2] = "80", "20"
    expect("q16 with every district mostly factory made", uniform_factory, q16,
           r"at least one district must be mostly household made")

    uniform_household = copy.deepcopy(w5_10._T_DISTRICTS)
    for row in uniform_household["rows"]:
        row[1], row[2] = "20", "80"
    expect("q16 with every district mostly household made", uniform_household, q16,
           r"at least one district must be mostly factory made")

    # and the tie case, which is what a reader expects a separate assertion for:
    # with the totals fixed at 100 an even split leaves BOTH lists empty, so the
    # first of the two assertions is what fires.
    tied = copy.deepcopy(w5_10._T_DISTRICTS)
    for row in tied["rows"]:
        row[1], row[2] = "50", "50"
    expect("q16 with the two shares tied in every district", tied, q16,
           r"at least one district must be mostly factory made")

    # 4. a district's two shares no longer accounting for all its cloth. Both the
    #    'some ... others' halves still hold, so only the total can catch it.
    unbalanced = copy.deepcopy(w5_10._T_DISTRICTS)
    unbalanced["rows"][1][1] = "66"
    expect("q16 with a district's shares no longer totalling 100", unbalanced, q16,
           r"account for all of that district's cloth")

    # 5. one inland column made non-monotonic while still ending higher than it
    #    began, which a start-to-end comparison would miss.
    bumpy = copy.deepcopy(w5_10._T_INLAND)
    bumpy["rows"][2][2] = "15"
    expect("q17 with the migration column no longer rising at every step", bumpy, q17,
           r"must rise at every step")
    print("  local control OK  a flattened spread, a falling region, three uniform district sets "
          "(all factory, all household, all tied), an unbalanced district and a non-monotonic "
          "column each raise, each for its own reason")


if "--selftest" in sys.argv:
    _local_controls()

wh.run(w5_10, CLAIMS, TABLE_CHECKS, sys.argv)
