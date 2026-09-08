"""Key audit for AP U.S. HISTORY 3.1 Contextualizing Period 3.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The shared gate is
``wh_check.run``, which the World History banks already use -- its checks are
about history rather than about world history: a KC code or Learning Objective
in every ``why`` and every ``claim``, no figure language, no typeset markup, and
the marked-stimulus rule.

WHAT THE KEYS REST ON
---------------------
  Unit 3 Learning Objective A, and the topic
    page's own instruction on context          items 1, 2, 14, 15, 16, 17, 18, 19, 20, 21,
                                               22, 23
  KC-3.1, tighter control against colonial
    resolve                                    3, 29, 30
  KC-3.1.I, the three competitors and the
    outcome of the war                         4, 5, 28
  KC-3.1.II, colonists asserting
    self-government                            6, 24
  KC-3.2, ideals inspiring experiments          7, 24, 29, 30
  KC-3.2.I, beliefs developing over the 18th
    century                                    8, 24
  KC-3.2.II, both limits at once               9, 23, 24, 25
  KC-3.2.III.i, national forms ALONGSIDE
    regional variation                         10, 27, 30
  KC-3.3, migration and competition            11, 24, 29, 30
  KC-3.3.I, three results, after independence  12, 26
  KC-3.3.II, borders, neutral trade, economic
    interests                                  13, 30

THE BOUNDARY THIS MODULE HAS TO HOLD, and why several items exist only to test
it: 3.1 is a CONTEXTUALIZING topic whose Required Course Content is printed
under the heading PREVIEW: UNIT 3 KEY CONCEPTS. The lettered sub-points --
KC-3.1.I.A through KC-3.3.II.C -- are printed on the pages of topics 3.2
through 3.12, which own them. So no key here names a tax, an act, a battle, a
convention, a party, a founder or a treaty. ``no_period_detail`` asserts that,
and items 17, 23 and 24 key the boundary itself.

WHAT IS DELIBERATELY ABSENT FROM THAT BANNED LIST, and why. The Seven Years'
War, the French and Indian War, Britain, France, American Indians and the
Revolutionary War are all printed in KC-3.1 and KC-3.1.I, which ARE the
preview, so banning them would ban the framework's own words. Bare years are
absent for the reason ``verify_a1_1.py`` records: the framework's periodisation
is years, so a year cannot distinguish preview from detail, and a list holding
one fires on a wrong-span distractor in an item about spans. A proper noun that
appears only under a later topic's lettered sub-points can.

THE SWAP ITEMS. Item 5 offers the reversed victor of KC-3.1.I and item 29 the
exchanged subjects of KC-3.1 and KC-3.3, so both anchors carry both clauses.
Item 9's distractors each keep one of KC-3.2.II's two limits and drop the
other, so its anchor carries the pair.

DATA ITEMS: 20, 21 and 22. Each table's expected rows are stated HERE,
independently of the module, because two of the three are CATEGORICAL and the
shared corrupter appends text -- a check written only on derived properties
would read a corrupted cell without being able to object to it, which is the
zero-catch failure ``verify_a1_1.py`` records. Stating the rows makes every
cell load-bearing; the derived assertions that follow are what tie the data to
the key.

NEGATIVE CONTROLS: ``python3 verify_a3_1.py --selftest``.
"""
import re
import sys

import wh_check
import a3_1

CONCEPT = "Previewed key concept"
SUBPOINTS = "Roman-numeral sub-points printed beneath it in the preview"
STATEMENT = "Statement offered as context for this unit (illustrative)"
STANDING = "Where it stands in relation to Period 3"
PERIOD = "Period as the framework numbers it"
FIRST = "First year of the span"
LAST = "Last year of the span"

# Explicit lookarounds, never \b beside a letter run. Period-3 detail that is
# printed only under the lettered sub-points owned by topics 3.2 through 3.12
# and must not appear in a PREVIEW topic.
_PERIOD_DETAIL = re.compile(
    r"(?<![A-Za-z])(Stamp Act|Townshend|Coercive|Declaratory|Intolerable|"
    r"Common Sense|Paine|Declaration of Independence|Articles of Confederation|"
    r"Northwest Ordinance|Constitutional Convention|Federalist|Hamilton|Jefferson|"
    r"Madison|Washington|Franklin|republican motherhood|Bill of Rights|Haiti|"
    r"Appalachian|Mississippi|Farewell Address|Whiskey|Loyalist|Patriot|"
    r"Continental Army|Yorktown|Lexington|Saratoga|California)(?![A-Za-z])",
    re.IGNORECASE)


def no_period_detail(module):
    """A PREVIEW topic may not key the detail its later topics own."""
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"], item["why"]] + list(item["choices"]):
            hit = _PERIOD_DETAIL.search(text)
            assert not hit, (
                f"{code} q{i}: names {hit.group(0)!r}, which is printed under a lettered "
                f"sub-point owned by topics 3.2 through 3.12 rather than in this "
                f"contextualizing topic's preview -- {text[:70]!r}"
            )
    print(f"OK  {code} scope: no item reaches into the lettered sub-points that topics "
          f"3.2 through 3.12 own.")


# ------------------------------------------------------------------ table checks

def _col(table, header):
    idx = table["headers"].index(header)
    return [row[idx] for row in table["rows"]]


_EXPECTED_PREVIEW = [["KC-3.1", "2"], ["KC-3.2", "3"], ["KC-3.3", "2"]]


def q20(table, item):
    assert [list(r) for r in table["rows"]] == _EXPECTED_PREVIEW, (
        f"the preview table does not hold the rows this check was written against; "
        f"got {table['rows']}"
    )
    counts = [int(c) for c in _col(table, SUBPOINTS)]
    top = max(counts)
    assert counts.count(top) == 1, (
        f"the key needs exactly one concept carrying the most sub-points; got {counts}")
    rest = [c for c in counts if c != top]
    assert len(set(rest)) == 1, (
        f"the two remaining concepts must carry the SAME number for the key to hold; "
        f"got {rest}")
    assert len(set(counts)) > 1, "'all three carry the same number' must be false"
    assert len(set(counts)) != len(counts), "'each carries a different number' must be false"
    assert min(counts) > 0, "'one carries no sub-points at all' must be false"
    assert sum(counts) != 9, f"'nine sub-points between them' must be false; the sum is {sum(counts)}"
    return (f"the sub-point counts are {counts}: one concept carries {top}, the other two "
            f"carry {rest[0]} each, and they total {sum(counts)}")


_EXPECTED_APPROACH = [
    ["Colonial traditions of self-government had been forming before 1754", "Preceding"],
    ["Enlightenment ideas were being argued over in Europe during these same decades",
     "Contemporaneous, in a different region"],
    ["New states were admitted west of the mountains long after 1848", "Later than the period"],
    ["British and French rivalry in North America had begun well before 1754", "Preceding"],
]


def q21(table, item):
    assert [list(r) for r in table["rows"]] == _EXPECTED_APPROACH, (
        f"the context table does not hold the rows this check was written against; "
        f"got {table['rows']}"
    )
    standing = [s.strip().lower() for s in _col(table, STANDING)]
    later = [s for s in standing if s.startswith("later")]
    assert len(later) == 1, (
        f"the key names exactly one row outside the two approaches; {len(later)} rows are "
        f"marked later than the period")
    preceding = [s for s in standing if s.startswith("preceding")]
    contemporaneous = [s for s in standing if s.startswith("contemporaneous")]
    assert preceding and contemporaneous, (
        f"both of the topic page's approaches must appear among the other rows, or the "
        f"remaining four options are not all false; got {standing}")
    assert len(preceding) + len(contemporaneous) + len(later) == len(standing), (
        f"every row must fall into one of the three categories; got {standing}")
    # 'No row falls outside the two approaches' must be false, which is the same
    # count as above, stated from the distractor's side.
    assert later, "'no row falls outside the two approaches' must be false"
    return (f"{len(preceding)} rows are marked preceding and {len(contemporaneous)} "
            f"contemporaneous elsewhere, against exactly {len(later)} marked later than "
            f"the period")


_EXPECTED_SPAN = [["Period 2", "1607", "1754"],
                  ["Period 3", "1754", "1800"],
                  ["Period 4", "1800", "1848"]]


def q22(table, item):
    assert [list(r) for r in table["rows"]] == _EXPECTED_SPAN, (
        f"the period table does not hold the rows this check was written against; "
        f"got {table['rows']}"
    )
    firsts = [int(v) for v in _col(table, FIRST)]
    lasts = [int(v) for v in _col(table, LAST)]
    assert lasts[0] == firsts[1], (
        f"the preceding period must close in the year this one opens; got {lasts[0]} "
        f"and {firsts[1]}")
    assert lasts[1] == firsts[2], (
        f"this period must close in the year the following one opens; got {lasts[1]} "
        f"and {firsts[2]}")
    assert lasts[0] >= firsts[1] and lasts[1] >= firsts[2], \
        "'separated by several years in which nothing is assigned' must be false"
    assert lasts[0] <= firsts[1], "'overlaps the preceding period' must be false"
    lengths = [b - a for a, b in zip(firsts, lasts)]
    assert lengths[1] < lengths[0] and lengths[1] < lengths[2], (
        f"'longer than the preceding period and shorter than the following one' must be "
        f"false; the spans are {lengths}")
    return (f"the spans run {list(zip(firsts, lasts))}: each closes in the year the next "
            f"opens, and their lengths are {lengths}")


TABLE_CHECKS = {20: q20, 21: q21, 22: q22}

CLAIMS = [
 ("developed a sense of national identity",
  "Unit 3: Learning Objective A reads verbatim 'Explain the context in which America gained independence and developed a sense of national identity.' The four distractors are Unit 3's Learning Objectives B, I, M and N, printed on later topic pages."),
 ("1754 to 1800",
  "The unit is titled Period 3: 1754 to 1800 at the head of every page of the unit, and Unit 3: Learning Objective A asks for the context of what happens inside it. 1607 to 1754 is Period 2 and 1800 to 1848 is Period 4."),
 ("colonial resolve to pursue self-government",
  "KC-3.1 states that British attempts to assert tighter control over its North American colonies AND the colonial resolve to pursue self-government led to a colonial independence movement and the Revolutionary War. The anchor carries the colonial half because every distractor denies one side of that pair."),
 ("economic and political advantage in North America",
  "KC-3.1.I names the competition among the British, French, and American Indians for economic and political advantage in North America. Neither the parties nor the object of the competition may be substituted without leaving the sentence."),
 ("Britain defeated France and allied American Indians",
  "KC-3.1.I ends 'in which Britain defeated France and allied American Indians'. The anchor carries the whole clause because the leading distractor is the same clause with the victor and the loser exchanged."),
 ("in the face of renewed British imperial efforts",
  "KC-3.1.II states that the desire of many colonists to assert ideals of self-government in the face of renewed British imperial efforts led to a colonial independence movement and war with Britain."),
 ("new experiments with different forms of government",
  "KC-3.2 states that the American Revolution's democratic and republican ideals inspired new experiments with different forms of government; the plural and the word DIFFERENT are what defeat a single uniform outcome."),
 ("developing over the course of the 18th century",
  "KC-3.2.I states that the ideals that inspired the revolutionary cause reflected new beliefs about politics, religion, and society that had been developing over the course of the 18th century."),
 ("both centralized power and excessive popular influence",
  "KC-3.2.II says the new constitutions and declarations of rights limited BOTH centralized power AND excessive popular influence. The anchor carries both limits because each distractor keeps one and drops the other."),
 ("continued regional variations and differences over economic",
  "KC-3.2.III.i states that new forms of national culture and political institutions developed alongside continued regional variations and differences over economic, political, social, and foreign policy issues."),
 ("competition over resources, boundaries, and trade",
  "KC-3.3 states that migration WITHIN North America and competition over resources, boundaries, and trade intensified conflicts among peoples and nations."),
 ("shifting alliances, and cultural blending",
  "KC-3.3.I names competition for resources, shifting alliances, and cultural blending as the three results of interactions among different groups; cultural blending is the term a student is likeliest to drop."),
 ("maintain neutral trading rights, and promote its economic interests",
  "KC-3.3.II names safeguarding its borders, maintaining neutral trading rights, and promoting its economic interests as the three things the continued presence of European powers challenged the United States to do."),
 ("Identify and describe a historical context",
  "Skill 4.A as printed beside this topic's title, and the skill Unit 3: Learning Objective A asks students to apply. The distractors are skills 1.B, 2.A, 5.A and 6.B, each printed on another topic page of this same unit."),
 ("Continuity and Change",
  "The unit's own topic table assigns Continuity and Change to this topic as its reasoning process, in service of Unit 3: Learning Objective A; Causation and Comparison are assigned to other topics of the unit."),
 ("contemporaneous historical developments in different regions",
  "The topic page names exactly two approaches to context: change from or continuity with preceding historical developments, and similarities or differences with contemporaneous historical developments in different regions or geographical areas. Unit 3: Learning Objective A is what they serve."),
 ("Select one or two of the previewed key concepts",
  "The topic page directs the teacher to consider this unit's key concepts, previewed below, and select one or two for which students will most need context. That direction is why the lettered detail behind Unit 3: Learning Objective A belongs to the later topics."),
 ("The American Revolution and the creation of the U.S. Constitution",
  "The optional activity on this topic page tells the teacher to note that the two main historical developments covered in this unit are the American Revolution and the creation of the U.S. Constitution, which is the pair Unit 3: Learning Objective A asks students to contextualise."),
 ("a key topic in this course and in two other AP history courses",
  "The optional activity on this page has the teacher display AP European History's Unit 4 and AP World History's Unit 5 and highlight that the Enlightenment is a key topic in all three courses, which is the page's own instance of contextualising Unit 3: Learning Objective A with contemporaneous developments elsewhere."),
 ("carries more sub-points than the other two",
  "Recomputed in q20 from the table alone, with each of the four alternatives falsified against the same counts. The preview printed for Unit 3: Learning Objective A carries KC-3.1, KC-3.2 and KC-3.3, and KC-3.2 is the one with three Roman-numeral sub-points."),
 ("later than the period",
  "Recomputed in q21 from the table alone: exactly one row is marked later than the period, and the topic page's two approaches reach only preceding developments and contemporaneous developments elsewhere. Unit 3: Learning Objective A asks for the context IN WHICH the period's developments occurred."),
 ("the spans meet rather than leaving a gap",
  "Recomputed in q22 from the table alone: each period closes in the year the next opens. That is why the context Unit 3: Learning Objective A asks for reaches back into the preceding period rather than into unassigned years."),
 ("printed as a PREVIEW of the unit's key concepts",
  "This topic's Required Course Content sits under the heading PREVIEW: UNIT 3 KEY CONCEPTS, and the page tells the teacher to select one or two of them; KC-3.2.II is previewed here, so the unit does cover the new constitutions rather than deferring them to another period."),
 ("migration within North America and competition over resources",
  "KC-3.3 is the previewed concept about movement and rival claims; KC-3.2, KC-3.2.II, KC-3.2.I and KC-3.1.II are all about ideals or the forms of government they produced."),
 ("The limit on excessive popular influence",
  "KC-3.2.II limits BOTH centralized power AND excessive popular influence, so a summary keeping only the first has dropped the second; the same sentence does mention protecting individual liberties and does place all of this after declaring independence."),
 ("In the decades after American independence",
  "KC-3.3.I opens with exactly this phrase, which places the competition, shifting alliances and cultural blending it describes in the later part of the period rather than before the Seven Years' War."),
 ("simultaneous, so the first did not displace the second",
  "KC-3.2.III.i's word ALONGSIDE puts the new national forms and the continuing regional variations at the same time and denies displacement in either direction; the sentence also names political institutions, not culture alone."),
 ("competitors for advantage in their own right, and as allies defeated alongside France",
  "KC-3.1.I gives American Indians both roles in one sentence: among the parties competing for economic and political advantage, and among those defeated when Britain defeated France and allied American Indians. The anchor carries both clauses because the distractors keep one and alter the other."),
 ("KC-3.3 with migration and competition over resources",
  "KC-3.1 concerns tighter British control against colonial resolve, KC-3.3 concerns migration and competition over resources, boundaries, and trade, and KC-3.2 concerns the Revolution's ideals. Both halves are carried because the leading distractor is the same pairing with the two subjects exchanged."),
 ("produced independence and war; the Revolution's ideals inspired experiments",
  "Collects KC-3.1, KC-3.2 and KC-3.3 in the order the preview prints them and adds nothing; the alternatives each contradict KC-3.2.III.i, KC-3.2, KC-3.3 or KC-3.3.II, or drop two of the three previewed concepts."),
]


def _extra_mutations():
    def period_detail_creeps_in(mod, cl):
        mod.QUESTIONS[0]["why"] = mod.QUESTIONS[0]["why"] + " The Stamp Act is the example."
        no_period_detail(mod)

    def two_rows_marked_later(mod, cl):
        # q21 keys the one row the topic page's two approaches cannot reach. If a
        # second row were marked later, the key would name a row rather than THE
        # row and the item would have two defensible answers. A value corruption
        # that appends text cannot express this, because it leaves the marks
        # readable as their original category.
        t = dict(mod.QUESTIONS[20]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][0][1] = "Later than the period"
        mod.QUESTIONS[20]["table"] = t

    def spans_leave_a_gap(mod, cl):
        # q22 keys that the spans abut. Moving one boundary year by a decade
        # leaves every cell well formed and the table still readable, and only
        # the derived equality can object.
        t = dict(mod.QUESTIONS[21]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][0][2] = "1744"
        mod.QUESTIONS[21]["table"] = t

    return [
        ("period detail in a contextualizing topic", period_detail_creeps_in),
        ("a second row marked later than the period, so q21's key names one of two",
         two_rows_marked_later),
        ("a boundary year moved back, so the spans no longer meet", spans_leave_a_gap),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    for label, mutate in _extra_mutations():
        mod = wh_check._mutant(a3_1)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            wh_check.history_style(mod, claims)
            no_period_detail(mod)
            import cg_check as cg
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as e:
            print(f"  control OK  {label}: {str(e)[:110]}")
        else:
            raise SystemExit(f"CONTROL FAILED: {label} did not raise")

no_period_detail(a3_1)
wh_check.run(a3_1, CLAIMS, TABLE_CHECKS, sys.argv)
