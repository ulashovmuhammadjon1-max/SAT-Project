"""Key audit for AP U.S. HISTORY 4.1 Contextualizing Period 4.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The shared gate is
``wh_check.run`` -- thirty questions, five distinct choices, an anchored key, a
``why`` that names no option by letter, a KC code or Learning Objective in every
``why`` and every ``claim``, no figure language, no typeset markup, and the
marked-stimulus rule.

WHAT THE KEYS REST ON
---------------------
  Unit 4 Learning Objective A, 1800 to 1848      items 1, 17, 18, 20, 21
  KC-4.1, modern democracy and a new national
    culture, ideals matched by institutions      2, 3, 22, 25, 30
  KC-4.1.I, suffrage and political parties       4, 5, 22, 24, 26, 27, 30
  KC-4.1.II, distinctive group cultures          6, 22, 30
  KC-4.1.III, work outside government
    institutions                                 7, 8, 22, 29
  KC-4.2, innovation accelerating the economy    9, 10, 22, 24, 28, 30
  KC-4.2.I, transportation expanding production  11, 23
  KC-4.2.II, effects on society and families     12, 23
  KC-4.2.III, unity alongside regional growth    13, 23, 28, 30
  KC-4.3, trade, borders, government and
    private initiative                           14, 23, 30
  KC-4.3.I, territory and foreign trade          15
  KC-4.3.II, contests over slavery in new
    territory                                    16, 30
  skill 4.A, the Continuity and Change reasoning
    process, and the periodisation note          18, 19, 20

THE BOUNDARY THIS MODULE HAS TO HOLD. 4.1 is a CONTEXTUALIZING topic whose
Required Course Content is printed under the heading PREVIEW: UNIT 4 KEY
CONCEPTS. The lettered sub-points -- KC-4.1.I.A through KC-4.3.II.C -- are
printed on the pages of topics 4.2 through 4.13, which six sibling topics of
this unit own. So no key here names a party, a leader, a court decision, a
compromise, a purchase, a machine, a route or a convention.
``no_period_detail`` asserts that, and item 21 keys the boundary itself.

BARE YEARS ARE DELIBERATELY ABSENT from the detail pattern, for the reason
recorded in ``verify_a1_1.py``: the framework's own periodisation is years, so
a year cannot distinguish a preview from a detail, and a first draft of that
list fired on a wrong ANSWER SPAN in an item about which span the Learning
Objective gives. A proper noun can.

THE SWAP ITEMS. Several distractors here are the key with one clause reversed
rather than an unrelated claim -- item 4 exchanges the two ends of the suffrage
change, item 11 keeps manufacturing and reverses agriculture, item 15 keeps
territory and denies trade, item 29 exchanges which column grows faster. Those
anchors carry BOTH clauses, which is the defect ``verify_e2_1.py`` shipped and
``HISTORY_BRIEF.md`` records.

DATA ITEMS: 27, 28 and 29 carry tables of explicitly hypothetical figures. Each
check recomputes the keyed claim and falsifies every distractor from the same
rows FIRST, and only then compares the rows against the literal list stated
here. The order is deliberate. Semantics alone caught only 6 of q27's 12 cells,
because the shared corrupter can scale a figure in the direction the claim
already runs; the literal list closes that and makes every cell load-bearing.
Running it LAST is what keeps each semantic control firing on the guard it
names rather than on row equality.

NEGATIVE CONTROLS: ``python3 verify_a4_1.py --selftest``.
"""
import re
import sys

import cg_check as cg
import wh_check
import wh_stimulus
import a4_1

_EXPECTED_SUFFRAGE = [
    ["State 1", "3,100", "8,400"],
    ["State 2", "2,700", "9,100"],
    ["State 3", "4,500", "7,900"],
    ["State 4", "1,800", "6,200"],
]

_EXPECTED_MARKET = [
    ["1800 to 1810", "40", "160"],
    ["1810 to 1820", "70", "150"],
    ["1820 to 1830", "120", "130"],
    ["1830 to 1840", "210", "110"],
]

_EXPECTED_ASSOC = [
    ["1800 to 1810", "12", "9"],
    ["1810 to 1820", "31", "10"],
    ["1820 to 1830", "68", "11"],
    ["1830 to 1840", "140", "12"],
]


def _rows_are(table, expected, what):
    """Every remaining cell made load-bearing, AFTER the semantic guards above.

    The order matters and is the point a1_1's verifier makes: a direction check
    catches the corruptions that reverse a claim, but the shared corrupter can
    also scale a figure in the direction the claim already runs -- q27 caught
    only 6 of 12 cells before this was added. Comparing the rows literally
    closes that, and running it LAST keeps every semantic control firing on the
    guard it names rather than on row equality.
    """
    assert [list(r) for r in table["rows"]] == expected, (
        f"the {what} table does not hold the rows this check was written against; "
        f"got {table['rows']}"
    )


VOTE_BEFORE = "Adult white men able to vote while a property test applied"
VOTE_AFTER = "Adult white men able to vote after the property test was dropped"
SENT_AWAY = "Value of goods sent beyond the district where they were made"
KEPT_HOME = "Value of goods consumed in the district where they were made"
OUTSIDE = "Associations founded outside government institutions"
INSIDE = "Bodies founded by state or federal government"

# Explicit lookarounds, never \b beside a letter run. Period-4 detail that the
# CED prints on the pages of topics 4.2 through 4.13 and that a PREVIEW topic
# must not key. Case-insensitive, and every entry is a proper noun or a term of
# art from a LETTERED sub-point: "Democrats?" cannot match "democratic" because
# the trailing lookahead refuses a letter, which is the whole reason the
# lookaround is written out rather than left as \b.
_PERIOD_DETAIL = re.compile(
    r"(?<![A-Za-z])("
    r"Jackson|Henry Clay|Whigs?|Democrats?|Monroe Doctrine|Missouri Compromise|"
    r"Louisiana Purchase|Tallmadge|Hartford Convention|Seneca Falls|American System|"
    r"Appalachians?|Mississippi|Erie|telegraph|steam engines?|interchangeable parts|"
    r"textile machinery|canals?|railroads?|tariffs?|national bank|Supreme Court|"
    r"Second Great Awakening|temperance|abolitionist|American Indian|Protestants?"
    r")(?![A-Za-z])",
    re.IGNORECASE)


def no_period_detail(module):
    """A PREVIEW topic may not key the detail its later topics own."""
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"], item["why"]] + list(item["choices"]):
            hit = _PERIOD_DETAIL.search(text)
            assert not hit, (
                f"{code} q{i}: names {hit.group(0)!r}, which the CED prints on the page of "
                f"a later topic of this unit rather than in this topic's preview -- "
                f"{text[:70]!r}"
            )
    print(f"OK  {code} scope: no item reaches into the lettered sub-points that topics "
          f"4.2 through 4.13 own.")


# ------------------------------------------------------------------ table checks

def q27(table, item):
    """The count of eligible voters is higher after the property test in every row."""
    labs = cg.labels(table)
    assert labs == ["State 1", "State 2", "State 3", "State 4"], \
        f"the four states the key speaks of are not the rows: {labs}"
    before, after = cg.col(table, VOTE_BEFORE), cg.col(table, VOTE_AFTER)
    assert all(a > b for b, a in zip(before, after)), (
        f"the key needs the later figure to exceed the earlier one in EVERY row; "
        f"got {before} against {after}"
    )
    assert not any(a < b for b, a in zip(before, after)), \
        "'the number able to vote is lower in every state' must be false"
    unchanged = [i for i, (b, a) in enumerate(zip(before, after)) if a == b]
    assert not unchanged, (
        f"'the number is unchanged in two of the states' must be false; rows {unchanged} "
        f"are unchanged"
    )
    risen = [i for i, (b, a) in enumerate(zip(before, after)) if a > b]
    assert len(risen) == len(before), (
        f"'the number rises in only one state' must be false; it rises in {len(risen)} of "
        f"{len(before)} rows"
    )
    _rows_are(table, _EXPECTED_SUFFRAGE, "suffrage")
    return (f"all {len(before)} rows record a higher figure after the property test was "
            f"dropped, {before} rising to {after}")


def q28(table, item):
    """Goods sent away rise while goods kept at home fall, so the share sent away rises."""
    labs = cg.labels(table)
    assert labs == ["1800 to 1810", "1810 to 1820", "1820 to 1830", "1830 to 1840"], \
        f"the four decades the item speaks of are not the rows: {labs}"
    away, home = cg.col(table, SENT_AWAY), cg.col(table, KEPT_HOME)
    shares = [a / (a + h) for a, h in zip(away, home)]
    assert all(shares[i + 1] > shares[i] for i in range(len(shares) - 1)), \
        f"the share leaving its own district must rise at every step; got {shares}"
    assert not all(shares[i + 1] < shares[i] for i in range(len(shares) - 1)), \
        "'the share leaving its own district falls in every decade' must be false"
    rising_away = all(away[i + 1] > away[i] for i in range(len(away) - 1))
    rising_home = all(home[i + 1] > home[i] for i in range(len(home) - 1))
    falling_home = all(home[i + 1] < home[i] for i in range(len(home) - 1))
    assert rising_away and falling_home and not rising_home, (
        f"'both columns move in the same direction' must be false; got {away} against {home}"
    )
    assert not all(h > a for a, h in zip(away, home)), \
        "'the value consumed locally exceeds the value sent away in every decade' must be false"
    assert len(set(away)) > 1 and len(set(home)) > 1, \
        "'neither column changes' must be false"
    _rows_are(table, _EXPECTED_MARKET, "market")
    return (f"goods sent away run {away} against {home} kept at home, so the share leaving "
            f"its district runs {[round(s, 2) for s in shares]}")


def q29(table, item):
    """Associations outside government outgrow government-founded bodies by a wide margin."""
    labs = cg.labels(table)
    assert labs == ["1800 to 1810", "1810 to 1820", "1820 to 1830", "1830 to 1840"], \
        f"the four decades the item speaks of are not the rows: {labs}"
    outside, inside = cg.col(table, OUTSIDE), cg.col(table, INSIDE)
    grow_out = outside[-1] / outside[0]
    grow_in = inside[-1] / inside[0]
    assert grow_out > 3 * grow_in, (
        f"the key needs growth outside government to far outpace growth within it; the "
        f"multiples are {round(grow_out, 2)} against {round(grow_in, 2)}"
    )
    assert not grow_in > grow_out, \
        "'bodies founded by government grow far faster' must be false"
    assert all(outside[i + 1] > outside[i] for i in range(len(outside) - 1)), \
        "'associations founded outside government decline' must be false"
    assert all(o > i for o, i in zip(outside, inside)), (
        f"'bodies founded by government outnumber the others in every decade' must be "
        f"false; got {outside} against {inside}"
    )
    assert all(o != i for o, i in zip(outside, inside)), \
        "'the two columns hold the same figure in every decade' must be false"
    _rows_are(table, _EXPECTED_ASSOC, "association")
    return (f"associations outside government run {outside}, a multiple of "
            f"{round(grow_out, 1)}, against {inside} founded by government, a multiple of "
            f"{round(grow_in, 1)}")


TABLE_CHECKS = {27: q27, 28: q28, 29: q29}

CLAIMS = [
 ("1800 to 1848",
  "Unit 4 Learning Objective A gives the span verbatim: explain the context in which the republic developed from 1800 to 1848. The rejected spans are Period 3's, Period 5's, and two that appear nowhere in the framework's periodisation."),
 ("modern democracy and celebrated a new national culture",
  "KC-4.1, near verbatim. The sentence joins the two developments, so an option keeping one and denying the other misstates it."),
 ("change their society and institutions to match them",
  "KC-4.1's second clause: Americans sought to define the nation's democratic ideals AND change their society and institutions to match them. The rejected version keeps the defining and drops the changing."),
 ("from a system based on property ownership to one based on voting by all adult white men",
  "KC-4.1.I states the direction of the change. The anchor carries BOTH ends because one distractor exchanges them and another keeps the starting point while altering the destination."),
 ("accompanied by the growth of political parties",
  "KC-4.1.I ends by saying the transition to a more participatory democracy was accompanied by the growth of political parties; every rejected option asserts a contraction the sentence does not."),
 ("national culture while various groups developed distinctive cultures of their own",
  "KC-4.1.II holds both halves at once with the word WHILE, so the anchor carries the national culture and the distinctive group cultures together."),
 ("Primarily outside of government institutions",
  "KC-4.1.III states that increasing numbers of Americans worked primarily outside of government institutions to advance their ideals; each rejected option names a government institution."),
 ("New religious and intellectual movements",
  "KC-4.1.III names new religious and intellectual movements as the inspiration for many of the Americans it describes."),
 ("Technology, agriculture, and commerce",
  "KC-4.2 names exactly these three fields of innovation as powerfully accelerating the American economy."),
 ("national and regional identities",
  "KC-4.2 says the acceleration precipitated profound changes to U.S. society and to national AND regional identities, so identity is changed rather than fixed and both scales are named."),
 ("Manufacturing and agricultural production together",
  "KC-4.2.I states that new transportation systems and technologies dramatically expanded manufacturing and agricultural production. The anchor carries both because two distractors keep one and reverse the other."),
 ("workers' lives, and gender and family relations",
  "KC-4.2.II names significant effects on U.S. society, workers' lives, and gender and family relations; the closest distractor drops the last item of that list."),
 ("unify the nation while also encouraging the growth of different regions",
  "KC-4.2.III asserts both outcomes at once, so the anchor carries the unification and the regional growth together against distractors that keep only one."),
 ("Government and private initiatives",
  "KC-4.3 states that the interest in foreign trade and expanding borders spurred government AND private initiatives, so restricting it to either alone drops half the sentence."),
 ("North American continent and promote foreign trade",
  "KC-4.3.I states that the United States sought to claim territory throughout the North American continent and promote foreign trade. The anchor carries both because one distractor keeps the territory and denies the trade."),
 ("contests over the extension of slavery into new territories",
  "KC-4.3.II states that the acquisition of lands in the West gave rise to contests over the extension of slavery into new territories, so the question was opened rather than settled."),
 ("preceding developments, and similarities or differences with contemporaneous developments",
  "The topic page for Unit 4 Learning Objective A names change from or continuity with PRECEDING developments and similarities or differences with CONTEMPORANEOUS developments in DIFFERENT regions; the closest distractor inverts both."),
 ("Identify and describe a historical context",
  "Skill 4.A as printed beside this topic's title, and the skill Unit 4 Learning Objective A asks students to apply; the rejected options are skills 4.B, 1.B, 5.B and 6.C, each printed beside another topic of this same unit."),
 ("patterns of continuity and change over time",
  "The unit's own table prints Continuity and Change as this topic's reasoning process, and the framework defines that process as describing and explaining patterns of continuity and change over time. Unit 4 Learning Objective A is the objective it serves."),
 ("may begin before, or continue after, the period",
  "The framework's periodisation note reads that events, processes, and developments are not constrained by the given dates and may begin before, or continue after, the period, while Unit 4 Learning Objective A still gives 1800 to 1848 as the span."),
 ("prints the unit's key concepts as a PREVIEW",
  "The heading over this topic's Required Course Content reads PREVIEW: UNIT 4 KEY CONCEPTS and the page directs the teacher to select one or two of them for context, so the lettered sub-points sit on later topic pages. KC-4.1.I names the growth of political parties, so the unit does cover party politics."),
 ("powerfully accelerated the American economy",
  "KC-4.2 is the economic key concept; the four rejected options are KC-4.1, KC-4.1.I, KC-4.1.II and KC-4.1.III, which concern democracy and culture."),
 ("increasing foreign trade and expanding national borders",
  "KC-4.3 is the foreign-policy key concept; the rejected options come from KC-4.2.I, KC-4.1.I, KC-4.2.II and KC-4.2.III and concern the domestic economy, the franchise or society."),
 ("parties were growing, while innovation was accelerating the economy",
  "KC-4.1.I describes suffrage expanding and parties growing and KC-4.2 describes innovation accelerating the economy, so the framework asserts change in politics and in the economy at once. The anchor carries both because two distractors freeze one of them."),
 ("a standard that existing society and institutions did not yet meet",
  "KC-4.1 has Americans define the nation's democratic ideals and then change society and institutions TO MATCH them, an order that only holds if the institutions did not already match."),
 ("still rested on a category that excluded those who were not adult white men",
  "KC-4.1.I describes the new basis for the franchise as voting by all adult white men, a stated category rather than the whole population, while still calling the change an expansion of suffrage."),
 ("higher after the property test was dropped",
  "Recomputed in q27 from the table alone: the later figure exceeds the earlier one in every row, which is the direction of change KC-4.1.I reports when suffrage moved off a property basis."),
 ("leaving its own district rises",
  "Recomputed in q28 from the table alone: goods sent away rise at every step while goods kept at home fall, so the share leaving its district rises throughout. KC-4.2.III has economic development shaping settlement and trade patterns and KC-4.2 calls the acceleration profound."),
 ("outside government grow far faster than bodies founded by government",
  "Recomputed in q29 from the table alone: the first column rises more than tenfold and the second by a third of that, so growth outside government far outpaces growth within it. KC-4.1.III places the work of increasing numbers of Americans primarily outside of government institutions. The anchor carries both columns because one distractor exchanges them."),
 ("innovation accelerated the economy and reshaped society and regional identity",
  "The keyed sentence collects KC-4.1, KC-4.1.I, KC-4.1.II, KC-4.2, KC-4.2.III, KC-4.3 and KC-4.3.II in the order the framework prints them and adds nothing; each rejected version contradicts or omits one of those key concepts."),
]


def _extra_mutations():
    def period_detail_creeps_in(mod, cl):
        mod.QUESTIONS[0]["why"] = (mod.QUESTIONS[0]["why"] +
                                   " The Whigs and the Democrats disagreed about it.")
        no_period_detail(mod)

    def suffrage_columns_exchanged(mod, cl):
        # Reverse the direction of the keyed change without touching any label.
        # Row equality is deliberately NOT asserted for these tables, so this
        # fires on the direction assertion -- the claim the item actually makes.
        t = mod.QUESTIONS[26]["table"]
        t["rows"] = [[lab, after, before] for lab, before, after in t["rows"]]

    def government_bodies_outgrow(mod, cl):
        # Make the government column the fast-growing one, which is the swap the
        # anchor was written to carry.
        t = mod.QUESTIONS[28]["table"]
        t["rows"] = [[lab, out, inn] for lab, inn, out in t["rows"]]

    return [
        ("period detail in a contextualizing topic", period_detail_creeps_in),
        ("the suffrage table's two columns exchanged, reversing the keyed direction",
         suffrage_columns_exchanged),
        ("the association table's two columns exchanged, so the government column grows faster",
         government_bodies_outgrow),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    wh_stimulus.controls(a4_1)
    for label, mutate in _extra_mutations():
        mod = wh_check._mutant(a4_1)
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

no_period_detail(a4_1)
wh_check.run(a4_1, CLAIMS, TABLE_CHECKS, sys.argv)
