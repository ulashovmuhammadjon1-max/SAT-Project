"""Key audit for AP U.S. HISTORY 5.1 Contextualizing Period 5.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The shared gate is
``wh_check.run`` -- its checks are about history rather than about world
history: a KC code or Learning Objective in every ``why`` and every ``claim``,
no figure language, no typeset markup, and the marked-stimulus rule.

WHAT THE KEYS REST ON
---------------------
  Unit 5 Learning Objective A, 1844 to 1877     items 1, 2, 20, 21, 23, 24, 25, 26, 27
  KC-5.1, connection, expansionist policy,
    destination for migrants                    3, 28, 29, 30
  KC-5.1.I, territories, migration westward,
    overseas initiatives                        4, 5, 27, 28, 30
  KC-5.1.II, continued debate over rights and
    citizenship in the 1840s and 1850s          6, 7, 11
  KC-5.2, intensified by expansion and
    deepening regional divisions                8, 9, 27, 29, 30
  KC-5.2.I, an array of diverging responses     10
  KC-5.2.II, the 1850s, the election of 1860
    and secession                               11, 12, 29
  KC-5.3, settled slavery and secession, left
    federal power and citizenship unresolved    13, 14, 22, 28, 29
  KC-5.3.I, manpower and industrial resources,
    Lincoln and others, emancipation            15, 16, 17
  KC-5.3.II.i, ended slavery, altered state
    and federal relations, citizenship debates  18, 19, 22, 30
  the topic page's own definition of context
    and its suggested skill 4.B                 7, 20, 21, 22, 26

THE BOUNDARY THIS MODULE HAS TO HOLD, and why three items exist only to test
it: 5.1 is a CONTEXTUALIZING topic whose Required Course Content is printed
under the heading PREVIEW. The lettered sub-points -- KC-5.1.I.A through
KC-5.3.II.E -- belong to topics 5.2 through 5.11, which have their own pages.
So no key here names a campaign, a statute, a court decision, a treaty or a
party. ``no_period_detail`` asserts that, and items 20, 22 and 23 key the
boundary itself.

WHAT IS DELIBERATELY NOT ON THE BANNED LIST. Abraham Lincoln, the Confederacy,
the Civil War and Reconstruction all appear in this module, because the
framework names them in the PREVIEWED sentences themselves -- KC-5.3.I names
"the leadership of Abraham Lincoln and others" and "the Union military victory
over the Confederacy", and KC-5.3.II.i names Reconstruction. Banning a proper
noun the preview itself prints would make the guard fire on the framework's own
words, which is the over-matching own-goal this repository keeps paying for.
BARE YEARS ARE ALSO ABSENT from the list, for the reason recorded in
``verify_a1_1.py``: the framework's periodisation IS years, so a year cannot
distinguish preview from detail.

THE SWAP ITEMS. Item 13 offers KC-5.3's two halves exchanged -- what was
settled traded with what was left unresolved -- so its anchor carries both
clauses. Item 3 reverses the direction of migration (destination against
source), item 15 inverts the decision to emancipate into a refusal, item 27
reverses the comparison the tally supports, and item 19 swaps citizenship for
sovereignty; each anchor carries whatever clause distinguishes the key from its
swap.

DATA ITEMS: 24, 25, 26 and 27 carry tables of explicitly illustrative data,
recomputed below from the table alone with each distractor falsified against
the same rows. Item 25 keys what the table CANNOT support, so its guard is on
the table's COLUMNS: no column ranks the periods, and corrupting a cell cannot
make an absent column present.

CATEGORICAL TABLES AND THE SHARED CORRUPTER. ``es_check._corrupt`` appends text
to a non-numeric cell and scales a number. Against a purely categorical table a
check written only on derived properties catches nothing, which the harness
rightly refuses, so the expected rows are stated HERE, independently of the
module. Two columns are deliberately left OUT of that literal comparison and
guarded semantically instead, so the targeted controls below fire on the claim
the item actually makes rather than on a row-equality assertion that would say
nothing about it: the periods table's SPAN column (guarded by a strict
``YYYY to YYYY`` format check plus the overlap arithmetic) and the approach
table's APPROACH column (guarded by the two-and-two count plus the
before-1844 test).

NEGATIVE CONTROLS: ``python3 verify_a5_1.py --selftest``.
"""
import re
import sys

import cg_check as cg
import wh_check
import a5_1

PERIOD = "Period of the course framework"
SPAN = "Span given in the course outline"
EMPHASIS = "Emphasis the framework states for the period"
STATEMENT = "Statement a student offers as context (illustrative)"
APPROACH = "Which of the topic page's two approaches it uses"
DEVELOPMENT = "Broad development proposed as context (illustrative tally)"
GROUPS = "Number of groups proposing it"

# Explicit lookarounds, never \b beside a letter run. Period-5 detail that
# belongs to topics 5.2 through 5.11 and must not appear in a PREVIEW topic.
# Every entry here is absent from the previewed sentences and present only in a
# lettered sub-point; see the module docstring for what is deliberately NOT
# banned.
_PERIOD_DETAIL = re.compile(
    r"(?<![A-Za-z])(Manifest Destiny|Mexican|Cession|Polk|Wilmot|Kansas|Nebraska|Dred|"
    r"Emancipation Proclamation|Gettysburg|Sumter|sharecropping|Plessy|Ferguson|"
    r"nativists?|nativism|abolitionists?|Homestead|amendments?|Whig|Republican|"
    r"Democratic|free-soil|Fugitive)(?![A-Za-z])", re.IGNORECASE)


def no_period_detail(module):
    """A PREVIEW topic may not key the detail its later topics own."""
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"], item["why"]] + list(item["choices"]):
            hit = _PERIOD_DETAIL.search(text)
            assert not hit, (
                f"{code} q{i}: names {hit.group(0)!r}, which belongs to topics 5.2 through "
                f"5.11 rather than to this contextualizing topic -- {text[:70]!r}"
            )
    print(f"OK  {code} scope: no item reaches into the lettered sub-points that topics "
          f"5.2 through 5.11 own.")


# ------------------------------------------------------------------ table checks

def _col(table, header):
    idx = table["headers"].index(header)
    return [str(row[idx]) for row in table["rows"]]


_EXPECTED_PERIODS = [
    ["Period 4", "1800 to 1848", "Antebellum reform and social change"],
    ["Period 5", "1844 to 1877", "How expansion led to debates over slavery"],
    ["Period 6", "1865 to 1898", "Economic development"],
    ["Period 7", "1890 to 1945", "America's rise to global power"],
]

# A span cell must be exactly "YYYY to YYYY". The format check is what makes the
# shared corrupter's appended text visible here: the two years survive a suffix,
# so a check that only pulled the digits out would read a corrupted cell as
# unchanged and report a catch rate it had not earned.
_SPAN = re.compile(r"(\d{4}) to (\d{4})")


def _period_labels(table):
    """Literal equality on the two columns the semantic guards do not cover."""
    assert _col(table, PERIOD) == [r[0] for r in _EXPECTED_PERIODS], (
        f"the periods table does not carry the period labels this check was written "
        f"against; got {_col(table, PERIOD)}")
    assert _col(table, EMPHASIS) == [r[2] for r in _EXPECTED_PERIODS], (
        f"the periods table does not carry the emphases this check was written against; "
        f"got {_col(table, EMPHASIS)}")


def _spans(table):
    out = []
    for cell in _col(table, SPAN):
        m = _SPAN.fullmatch(cell.strip())
        assert m, f"span cell {cell!r} is not written as four digits, 'to', four digits"
        start, end = int(m.group(1)), int(m.group(2))
        assert start < end, f"span cell {cell!r} does not run forwards"
        out.append((start, end))
    return out


def q24(table, item):
    _period_labels(table)
    spans = _spans(table)
    pairs = range(len(spans) - 1)
    overlap = [i for i in pairs if spans[i + 1][0] < spans[i][1]]
    gap = [i for i in pairs if spans[i + 1][0] > spans[i][1]]
    exact = [i for i in pairs if spans[i + 1][0] == spans[i][1]]
    assert len(overlap) == len(spans) - 1, (
        f"every consecutive pair must overlap for the key to hold; {len(overlap)} of "
        f"{len(spans) - 1} do, with gaps at {gap} and exact meetings at {exact}")
    assert not gap, f"'separated by a gap' must be false; gaps at {gap}"
    assert not exact, f"'meet exactly' must be false; exact meetings at {exact}"
    lengths = [b - a for a, b in spans]
    assert any(lengths[i + 1] >= lengths[i] for i in pairs), (
        f"'each successive span is shorter than the one before' must be false; "
        f"lengths are {lengths}")
    return (f"{len(spans)} spans with all {len(overlap)} consecutive pairs overlapping, "
            f"no gap and no exact meeting, and lengths {lengths} that do not decrease "
            f"throughout")


def q25(table, item):
    # This item keys what the table CANNOT support, so its guard is a check on
    # the table's COLUMNS rather than on any value in them: no column ranks the
    # periods against one another, and corrupting a cell cannot make an absent
    # column present. HEADER GUARD FIRST, then the labels, then the spans --
    # ordered this way deliberately, because the control for this item adds an
    # importance column and a row-shape assertion running first would raise for
    # a reason that says nothing about the guard it names.
    joined = " ".join(table["headers"]).lower()
    for word in ("important", "importance", "rank", "priority", "weight"):
        assert word not in joined, (
            f"the table must rank nothing for the key to hold, but a header mentions "
            f"{word!r}: {table['headers']}")
    _period_labels(table)
    spans = _spans(table)
    assert spans[1][0] < spans[0][1], (
        f"'Period 5 begins before Period 4 ends' must be true; got {spans[0]} and {spans[1]}")
    assert spans[2][0] < spans[1][1], (
        f"'Period 6 begins before Period 5 ends' must be true; got {spans[1]} and {spans[2]}")
    emphases = _col(table, EMPHASIS)
    assert len(set(emphases)) == len(emphases), (
        f"'a different emphasis for each period' must be true; got {emphases}")
    lengths = [b - a for a, b in spans]
    assert lengths[-1] == max(lengths) and lengths.count(max(lengths)) == 1, (
        f"'Period 7's span is the longest' must be true and unshared; lengths are {lengths}")
    return ("no header of the table ranks one period against another, while all four "
            "rejected claims are read directly off the rows")


_EXPECTED_APPROACH_STATEMENTS = [
    "A development already under way before 1844 that continued into the period",
    "A development in a different region of the world during the same years",
    "A development that had run its course before 1844",
    "A development in a different geographical area at the same time",
]


def q26(table, item):
    # Only the STATEMENT column is compared literally. The APPROACH column is
    # left to the semantic guard below, so the control that exchanges the two
    # labels raises on the claim the item actually makes rather than on a
    # row-equality assertion. Corrupting an APPROACH cell still fails, through
    # the two-and-two count, because a corrupted label matches neither category.
    assert _col(table, STATEMENT) == _EXPECTED_APPROACH_STATEMENTS, (
        f"the approach table's statements are not the ones this check was written "
        f"against; got {_col(table, STATEMENT)}")
    statements, labels = _col(table, STATEMENT), _col(table, APPROACH)
    preceding = [s for s, lab in zip(statements, labels)
                 if lab.strip().lower() == "preceding developments"]
    contemporaneous = [s for s, lab in zip(statements, labels)
                       if lab.strip().lower() == "contemporaneous developments elsewhere"]
    assert len(preceding) == 2 and len(contemporaneous) == 2, (
        f"the key names exactly two preceding rows against two contemporaneous ones; got "
        f"{len(preceding)} and {len(contemporaneous)}")
    assert all("before 1844" in s.lower() for s in preceding), (
        f"both preceding rows must sit before 1844; got {preceding}")
    assert not any("before 1844" in s.lower() for s in contemporaneous), (
        f"no contemporaneous row may sit before 1844; got {contemporaneous}")
    return (f"exactly two rows are marked as preceding developments and both sit before "
            f"1844 ({preceding}), against two marked contemporaneous that do not")


# The tally table is CATEGORICAL in its first column and numeric in its second,
# and neither half is fully pinned by the arithmetic alone: scaling the leading
# count leaves it still the largest, so the comparison the key rests on survives
# a corruption that changed the data. The expected rows are therefore stated
# here in full, which makes every one of the eight cells load-bearing; the
# derived assertions that follow are what tie the data to the key.
_EXPECTED_TALLY = [
    ["Westward expansion", "9"],
    ["Regional differences", "7"],
    ["Political controversies and compromises", "5"],
    ["Other proposals", "3"],
]


def q27(table, item):
    assert [list(r) for r in table["rows"]] == _EXPECTED_TALLY, (
        f"the tally table does not hold the rows this check was written against; "
        f"got {table['rows']}")
    counts = cg.col(table, GROUPS)
    named = dict(zip(_col(table, DEVELOPMENT), counts))
    assert named["Westward expansion"] > named["Regional differences"], (
        f"the keyed comparison must hold: {named['Westward expansion']} against "
        f"{named['Regional differences']}")
    assert len(set(counts)) == len(counts), (
        f"'every group proposed the same development' must be false; got {counts}")
    assert named["Political controversies and compromises"] < max(counts), (
        f"'political controversies and compromises was the most proposed' must be false; "
        f"got {named['Political controversies and compromises']} against {max(counts)}")
    assert sum(counts[:3]) > counts[3], (
        f"'the three named developments together were fewer than the other proposals' must "
        f"be false; got {sum(counts[:3])} against {counts[3]}")
    return (f"read from the table alone: {named['Westward expansion']:.0f} against "
            f"{named['Regional differences']:.0f}, four distinct counts, and the three "
            f"named developments outnumbering the remainder")


TABLE_CHECKS = {24: q24, 25: q25, 26: q26, 27: q27}

CLAIMS = [
 ("1844 to 1877",
  "Unit 5 Learning Objective A gives the span verbatim: explain the context in which sectional conflict emerged from 1844 to 1877."),
 ("emergence of sectional conflict",
  "Unit 5 Learning Objective A names sectional conflict as the development whose context is to be explained; the rejected options are the Learning Objective A of Units 6, 1 and 7."),
 ("the destination for many migrants from other countries",
  "KC-5.1, near verbatim. The anchor carries the whole clause because one distractor reverses the direction of migration, making the country a source of emigrants rather than a destination."),
 ("substantial migration westward, and new overseas initiatives",
  "KC-5.1.I names the acquisition of new territories, substantial migration westward, and new overseas initiatives as what popular enthusiasm for expansion resulted in."),
 ("Economic and security interests",
  "KC-5.1.I says popular enthusiasm for U.S. expansion was bolstered by economic and security interests; no other pairing appears in that sentence."),
 ("Rights and citizenship for various groups",
  "KC-5.1.II states that in the 1840s and 1850s Americans continued to debate questions about rights and citizenship for various groups of U.S. inhabitants."),
 ("already under way before the period",
  "KC-5.1.II's word CONTINUED places the debate before the decades it names, which is the continuity the reasoning process printed beside this topic asks students to examine."),
 ("Expansion and deepening regional divisions",
  "KC-5.2 opens by naming both: the debates were INTENSIFIED BY expansion and deepening regional divisions. The anchor carries both because one distractor keeps only the second."),
 ("Economic, cultural, and political issues",
  "KC-5.2 names debates over slavery and other economic, cultural, and political issues; military, diplomatic, legal, scientific and technological issues are absent from that list."),
 ("not a single position held on each side",
  "KC-5.2.I says the differences produced an ARRAY OF DIVERGING RESPONSES from Americans in the North and the South, which is many responses rather than one position on each side."),
 ("1850s",
  "KC-5.2.II states that debates over slavery came to dominate political discussion in the 1850s; KC-5.1.II's 1840s and 1850s concern rights and citizenship rather than this domination."),
 ("election of 1860 and the secession of Southern states",
  "KC-5.2.II names both as what the debates of the 1850s culminated in. The ending of slavery, offered by one distractor, belongs to KC-5.3.II.i and comes later."),
 ("settled the issues of slavery and secession, but left unresolved many questions about the power of the federal government",
  "KC-5.3, near verbatim. The anchor carries BOTH clauses because one distractor exchanges them, keying what was settled as what was left unresolved and the reverse."),
 ("disputed rather than settled by agreement",
  "KC-5.3 calls the reconstruction of the South CONTESTED and says the war and that reconstruction left many questions unresolved, which is what a dispute leaves behind."),
 ("industrial resources, the leadership of Abraham Lincoln and others, and the decision to emancipate",
  "KC-5.3.I names the three together. The anchor runs through all three because one distractor keeps the first two and inverts the third into a refusal to emancipate."),
 ("decline to attribute the leadership to one person alone",
  "KC-5.3.I writes 'the leadership of Abraham Lincoln and others', which widens the credit beyond one person while naming no one else."),
 ("did not follow at once",
  "KC-5.3.I says the advantages EVENTUALLY led to the Union military victory, so the word qualifies the timing; the same sentence states that the victory was won."),
 ("African Americans, women, and other minorities",
  "KC-5.3.II.i names exactly these three as the groups whose rights the debates over new definitions of citizenship particularly concerned."),
 ("altered relationships between the states and the federal government, and led to debates over new definitions of citizenship",
  "KC-5.3.II.i, near verbatim. The anchor carries the words NEW DEFINITIONS because one distractor keeps the same clause without them and another substitutes sovereignty for citizenship."),
 ("situated within a broader historical context",
  "Skill 4.B as printed on this topic page, and what Unit 5 Learning Objective A asks students to do; the rejected options are skills 4.A, 1.B, 3.C and 6.C from other pages of this unit."),
 ("at the same time in a different region or geographical area",
  "The topic page's second bullet names similarities and differences with contemporaneous historical developments in different regions or geographical areas, which Unit 5 Learning Objective A is served by."),
 ("printed as a PREVIEW of the unit's key concepts",
  "The topic page prints the key concepts under the heading PREVIEW and directs the teacher to select one or two for context; KC-5.3 names the Civil War and KC-5.3.II.i names Reconstruction, so Unit 5 does cover both."),
 ("Continuity and change",
  "The Unit 5 outline prints Continuity and Change beside this topic, Causation beside topics 5.2, 5.3, 5.6 and 5.7, and Comparison beside 5.4, 5.5, 5.8 and 5.12; Unit 5 Learning Objective A is what the reasoning process serves."),
 ("each later span begins before the one before it ends",
  "Recomputed in q24 from the table alone, and the framework's note about periodisation states that several of the periods show some degree of overlap; Unit 5 Learning Objective A asks for a context that a single boundary year could not supply."),
 ("regards the earlier of two overlapping periods as the more important",
  "Recomputed in q25: no column of the table ranks the periods, so this is the one claim of the five the record cannot reach. Unit 5 Learning Objective A asks for context, not for a ranking of periods."),
 ("already under way before 1844 and the row about a development that had run its course",
  "Recomputed in q26 from the table alone: exactly two rows are marked as preceding developments and both sit before 1844, which is the topic page's first approach to context under Unit 5 Learning Objective A."),
 ("Westward expansion was proposed by more groups than regional differences",
  "Recomputed in q27 from the table alone: nine against seven, with the reversed comparison false on the same counts. KC-5.1.I's substantial migration westward and KC-5.2's deepening regional divisions are both previewed for this unit, so either could be offered as context."),
 ("questions about the power of the federal government and citizenship rights remained open",
  "KC-5.3, against four sentences drawn from KC-5.1 and KC-5.1.I describing the nation's connection with the world and what expansion produced."),
 ("settled slavery and secession while leaving questions of federal power and citizenship open",
  "Collects KC-5.1, KC-5.2 and KC-5.3 in the framework's own order and adds nothing to them; KC-5.3's own words are that the questions were LEFT UNRESOLVED."),
 ("one of the things that intensified the debates",
  "KC-5.2 says the debates were intensified by expansion AND deepening regional divisions, which makes expansion one intensifying cause among others rather than all of them or none."),
]


def _extra_mutations():
    def period_detail_creeps_in(mod, cl):
        mod.QUESTIONS[0]["why"] = mod.QUESTIONS[0]["why"] + " The Wilmot Proviso is the case."
        no_period_detail(mod)

    def importance_column_appears(mod, cl):
        # q25 keys what the table cannot support; a column ranking the periods
        # would make the keyed claim reachable and the item wrong.
        t = dict(mod.QUESTIONS[24]["table"])
        t["headers"] = list(t["headers"]) + ["Relative importance the framework assigns"]
        t["rows"] = [list(r) + ["High"] for r in t["rows"]]
        mod.QUESTIONS[24]["table"] = t

    def a_span_stops_overlapping(mod, cl):
        # Move Period 5's start past Period 4's end. The SPAN column is left out
        # of the literal row comparison precisely so this control fires on q24's
        # overlap arithmetic -- the claim the item actually makes -- rather than
        # on a row-equality assertion that would say nothing about it. Only
        # q24's copy of the table is replaced, so q25 still sees the original.
        t = dict(mod.QUESTIONS[23]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][1][1] = "1850 to 1877"
        mod.QUESTIONS[23]["table"] = t

    def the_two_approaches_are_exchanged(mod, cl):
        # Swap which rows are marked preceding, so the keyed pair stops being
        # the before-1844 one. A value corruption cannot express this, and the
        # literal comparison deliberately does not cover the label column.
        t = dict(mod.QUESTIONS[25]["table"])
        t["rows"] = [[s, ("Contemporaneous developments elsewhere"
                          if lab == "Preceding developments" else "Preceding developments")]
                     for s, lab in t["rows"]]
        mod.QUESTIONS[25]["table"] = t

    return [
        ("period detail in a contextualizing topic", period_detail_creeps_in),
        ("an importance column added, making q25's unsupportable claim supportable",
         importance_column_appears),
        ("a span moved so consecutive periods no longer overlap", a_span_stops_overlapping),
        ("the two context approaches exchanged, so the keyed pair is no longer the "
         "before-1844 one", the_two_approaches_are_exchanged),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    for label, mutate in _extra_mutations():
        mod = wh_check._mutant(a5_1)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            wh_check.history_style(mod, claims)
            no_period_detail(mod)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as e:
            print(f"  control OK  {label}: {str(e)[:110]}")
        else:
            raise SystemExit(f"CONTROL FAILED: {label} did not raise")

no_period_detail(a5_1)
wh_check.run(a5_1, CLAIMS, TABLE_CHECKS, sys.argv)
