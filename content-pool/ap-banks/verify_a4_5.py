"""Key audit for AP U.S. HISTORY 4.5 Market Revolution: Industrialization.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The shared gate is
``wh_check.run``.

WHAT THE KEYS REST ON
---------------------
  Unit 4 Learning Objective E, causes and
    effects of the innovations in technology,
    agriculture, and commerce over time           items 1, 7, 16, 18, 19, 23, 24
  KC-4.2.I.A, entrepreneurs, market
    relationships, manufacture more organized     2, 3, 4, 25, 26, 30
  KC-4.2.I.B, five kinds of innovation raising
    the efficiency of production methods          5, 6, 7, 20, 26, 27, 30
  KC-4.2.I.C, legislation and courts behind
    roads, canals and railroads, and the UNEVEN
    linkage of the regions                        8, 9, 10, 11, 21, 25, 26, 28, 30
  KC-4.2.III.B, Southern cotton and the related
    growth of Northern industry                   12, 13, 14, 22, 26, 29, 30
  KC-4.2.I, the parent concept                    15, 26
  the Work, Exchange, and Technology focus        16, 17, 25
  skill 6.B and its two sub-points                18, 19, 20, 21, 22

WHAT IS NOT ASSERTED. KC-4.2.I.B names five kinds of innovation without naming
an inventor, a firm, a place or a date, and KC-4.2.I.C names three kinds of
route without naming one. Neither does this module. The market revolution's
effects on workers, households and social structure are KC-4.2.II's material and
belong to topic 4.6.

THE SWAP ITEMS. Item 10 is the one this module exists to get right: KC-4.2.I.C's
second sentence is a COMPARISON between regions, and two of its distractors keep
the sentence's form while exchanging which regions were most closely tied. Item
9 keeps enlarged markets and reverses interdependence, item 12 exchanges the two
regions' activities, and item 28's leading distractor exchanges which column of
freight grows faster. Those anchors carry BOTH clauses.

DATA ITEMS: 27, 28 and 29 carry tables of explicitly hypothetical figures. Each
check recomputes the keyed claim and falsifies every distractor from the same
rows FIRST, and compares the rows against the literal list LAST -- the ordering
verify_a4_1.py records.

NEGATIVE CONTROLS: ``python3 verify_a4_5.py --selftest``.
"""
import sys

import cg_check as cg
import wh_check
import wh_stimulus
import a4_5

BEFORE = "Pieces finished per worker in a week before the new machinery"
AFTER = "Pieces finished per worker in a week after the new machinery"
MIDWEST = "Tons of freight carried between the North and the Midwest"
SOUTH = "Tons of freight carried between the North and the South"
COTTON = "Southern cotton production"
NORTHERN = "Northern manufacturing, banking, and shipping"

_EXPECTED_EFFICIENCY = [
    ["Workshop 1", "18", "44"],
    ["Workshop 2", "22", "51"],
    ["Workshop 3", "15", "39"],
    ["Workshop 4", "26", "58"],
]

_EXPECTED_LINKS = [
    ["1810 to 1820", "40", "31"],
    ["1820 to 1830", "95", "38"],
    ["1830 to 1840", "180", "44"],
    ["1840 to 1848", "310", "49"],
]

_EXPECTED_TIES = [
    ["1810 to 1820", "20", "25"],
    ["1820 to 1830", "46", "48"],
    ["1830 to 1840", "88", "83"],
    ["1840 to 1848", "150", "141"],
]


def _rows_are(table, expected, what):
    assert [list(r) for r in table["rows"]] == expected, (
        f"the {what} table does not hold the rows this check was written against; "
        f"got {table['rows']}"
    )


def q27(table, item):
    """Output per worker is higher after the machinery in every workshop."""
    labs = cg.labels(table)
    assert labs == [f"Workshop {n}" for n in range(1, 5)], \
        f"the four workshops the choices speak of are not the rows: {labs}"
    before, after = cg.col(table, BEFORE), cg.col(table, AFTER)
    assert all(a > b for b, a in zip(before, after)), (
        f"the key needs output per worker to be higher after the machinery in EVERY row; "
        f"got {before} against {after}"
    )
    assert not any(a < b for b, a in zip(before, after)), \
        "'output per worker is lower after the new machinery' must be false"
    unchanged = [i for i, (b, a) in enumerate(zip(before, after)) if a == b]
    assert not unchanged, (
        f"'output per worker is unchanged in two workshops' must be false; rows "
        f"{unchanged} are unchanged"
    )
    risen = [i for i, (b, a) in enumerate(zip(before, after)) if a > b]
    assert len(risen) == len(labs), \
        f"'output rises in only one workshop' must be false; it rises in {len(risen)}"
    lowest_before = before.index(min(before))
    highest_after = after.index(max(after))
    assert lowest_before != highest_after, (
        f"'the workshop lowest before has the highest output after' must be false; row "
        f"{lowest_before} is lowest before and row {highest_after} highest after"
    )
    _rows_are(table, _EXPECTED_EFFICIENCY, "efficiency")
    return (f"all {len(labs)} rows record a higher figure after the machinery, {before} "
            f"rising to {after}, and the row lowest before is not the highest after")


def q28(table, item):
    """North to Midwest traffic outgrows North to South traffic by a wide margin."""
    labs = cg.labels(table)
    assert labs == ["1810 to 1820", "1820 to 1830", "1830 to 1840", "1840 to 1848"], \
        f"the four decades the item speaks of are not the rows: {labs}"
    midwest, south = cg.col(table, MIDWEST), cg.col(table, SOUTH)
    grow_mw = midwest[-1] / midwest[0]
    grow_s = south[-1] / south[0]
    assert grow_mw > 3 * grow_s, (
        f"the key needs the North to Midwest column to grow far faster; the multiples are "
        f"{round(grow_mw, 2)} against {round(grow_s, 2)}"
    )
    assert not grow_s > grow_mw, \
        "'traffic between the North and the South grows much faster' must be false"
    assert all(south[i + 1] > south[i] for i in range(len(south) - 1)), \
        f"'traffic between the North and the South declines' must be false; got {south}"
    assert abs(grow_mw - grow_s) > 1, \
        f"'the two columns grow at the same rate' must be false; got {grow_mw} and {grow_s}"
    assert all(m > s for m, s in zip(midwest, south)), (
        f"'the North to Midwest figure is the smaller in every decade' must be false; got "
        f"{midwest} against {south}"
    )
    _rows_are(table, _EXPECTED_LINKS, "freight")
    return (f"North to Midwest freight runs {midwest}, a multiple of {round(grow_mw, 1)}, "
            f"against {south} to the South, a multiple of {round(grow_s, 1)}")


def q29(table, item):
    """Southern cotton and the Northern index rise together, neither always ahead."""
    labs = cg.labels(table)
    assert labs == ["1810 to 1820", "1820 to 1830", "1830 to 1840", "1840 to 1848"], \
        f"the four decades the item speaks of are not the rows: {labs}"
    cotton, north = cg.col(table, COTTON), cg.col(table, NORTHERN)
    assert all(cotton[i + 1] > cotton[i] for i in range(len(cotton) - 1)), \
        f"Southern cotton production must rise at every step; got {cotton}"
    assert all(north[i + 1] > north[i] for i in range(len(north) - 1)), \
        f"the Northern index must rise at every step; got {north}"
    assert not any(north[i + 1] < north[i] for i in range(len(north) - 1)), \
        "'the Northern index falls' must be false"
    assert not any(cotton[i + 1] < cotton[i] for i in range(len(cotton) - 1)), \
        "'Southern cotton production falls' must be false"
    assert len(set(cotton)) > 1 and len(set(north)) > 1, \
        "'neither index changes' must be false"
    north_ahead = [n > c for c, n in zip(cotton, north)]
    assert not all(north_ahead), (
        f"'the Northern index is the larger in every decade' must be false; it leads in "
        f"{sum(north_ahead)} of {len(labs)} rows"
    )
    _rows_are(table, _EXPECTED_TIES, "commercial ties")
    return (f"Southern cotton runs {cotton} and the Northern index {north}, both rising at "
            f"every step with the Northern index ahead in only {sum(north_ahead)} rows")


TABLE_CHECKS = {27: q27, 28: q28, 29: q29}

CLAIMS = [
 ("causes and effects of the innovations in technology, agriculture, and commerce",
  "Unit 4 Learning Objective E, verbatim, which is why Causation is the reasoning process printed beside this topic."),
 ("Entrepreneurs",
  "KC-4.2.I.A states that entrepreneurs helped to create a market revolution in production and commerce; legislation and judicial systems appear in KC-4.2.I.C supporting transport rather than creating the revolution."),
 ("Market relationships between producers and consumers",
  "KC-4.2.I.A names exactly this as what came to prevail in the market revolution."),
 ("became more organized",
  "KC-4.2.I.A joins the prevailing of market relationships to the manufacture of goods becoming more organized in a single sentence."),
 ("Textile machinery, steam engines, interchangeable parts, the telegraph, and agricultural inventions",
  "KC-4.2.I.B names exactly these five kinds of innovation, and no inventor, firm, place or date anywhere."),
 ("The efficiency of production methods",
  "KC-4.2.I.B states that those innovations increased the efficiency of production methods; regional interdependence belongs to KC-4.2.I.C instead."),
 ("reached farming as well as manufacturing",
  "KC-4.2.I.B's list runs from textile machinery through the telegraph to agricultural inventions, so it spans manufacture, communication and farming, which is why Unit 4 Learning Objective E names technology, agriculture and commerce together."),
 ("Legislation and judicial systems",
  "KC-4.2.I.C states that legislation and judicial systems supported the development of roads, canals, and railroads."),
 ("extended and enlarged markets and helped foster regional interdependence",
  "KC-4.2.I.C's first sentence asserts both results together. The anchor carries both because the leading distractor keeps the enlargement and reverses the interdependence."),
 ("North and Midwest more closely than they linked regions in the South",
  "KC-4.2.I.C's second sentence, verbatim. It is a COMPARISON, so the anchor carries both sides of it; two distractors keep the form and exchange which regions were most closely tied."),
 ("interdependence the routes fostered was uneven between the regions",
  "KC-4.2.I.C's two sentences read together: the first has the routes fostering regional interdependence, the second says the networks linked the North and Midwest more closely than regions in the South."),
 ("Increasing Southern cotton production and the growth of Northern manufacturing",
  "KC-4.2.III.B names increasing Southern cotton production and the related growth of Northern manufacturing, banking, and shipping industries. The anchor carries both halves because the leading distractor exchanges the two regions' activities."),
 ("national and international commercial ties",
  "KC-4.2.III.B says the two developments promoted the development of national AND international commercial ties, so restricting the outcome to either scale drops half the sentence."),
 ("connected rather than independent",
  "KC-4.2.III.B calls the Northern growth RELATED to increasing Southern cotton production and has the two together promoting commercial ties, which asserts connection rather than coincidence."),
 ("Manufacturing and agricultural production",
  "KC-4.2.I states that new transportation systems and technologies dramatically expanded manufacturing and agricultural production, the general claim beneath which this topic's sub-points sit."),
 ("Markets, private enterprise, labor, technology, and government policy",
  "The Work, Exchange, and Technology thematic focus printed on this topic's page names exactly these five, whose interplay Unit 4 Learning Objective E asks students to trace."),
 ("shapes society and government policy and drives technological innovation",
  "The same thematic focus's second sentence, which runs the influence back the other way with the words IN TURN and reaches all three of society, government policy and technology. Unit 4 Learning Objective E asks for causes as well as effects for the same reason."),
 ("Support an argument using specific and relevant evidence",
  "Skill 6.B as printed beside this topic's title, in service of Unit 4 Learning Objective E; the rejected options are skills 3.B, 3.D, 6.A and 6.C."),
 ("explain how specific examples support an argument",
  "Skill 6.B carries two sub-points in the framework, describing specific examples of historically relevant evidence and explaining how they support an argument. Unit 4 Learning Objective E is what the skill is applied to here."),
 ("output per worker in the same workshops before and after new machinery",
  "Skill 6.B requires evidence that is relevant as well as specific, and KC-4.2.I.B's claim about the efficiency of production methods is settled by figures for output per worker."),
 ("freight carried between the North and the Midwest with the freight carried between the North and the South",
  "KC-4.2.I.C's second sentence makes a comparative claim, so under skill 6.B the evidence that supports it must itself compare two links; a national total is specific without being relevant."),
 ("voluntary associations founded in Northern towns",
  "KC-4.2.III.B's claim concerns increasing Southern cotton production and the related growth of Northern industry, and a count of voluntary associations belongs to KC-4.1.III.A instead. Skill 6.B requires relevance as well as specificity."),
 ("Causation",
  "The unit's table prints Causation as this topic's reasoning process, matching Unit 4 Learning Objective E's demand for the causes and effects of the innovations; the rejected options are the other two reasoning processes and two skills."),
 ("primary and secondary causes and between short-term and long-term effects",
  "Aspect 2.iii of the Causation reasoning process, which is the distinction Unit 4 Learning Objective E requires when innovations are traced OVER TIME."),
 ("Legislation and judicial systems supported the development of roads",
  "KC-4.2.I.C gives government its role in these sentences, and the Work, Exchange, and Technology thematic focus names government policy among the five things whose interplay shapes the economy, which is why standing outside the economy is excluded."),
 ("KC-4.2.I.C, which says the networks linked the North and Midwest more closely",
  "KC-4.2.I.C's second sentence is the direct denial of even integration; the rejected sentences concern market relationships, efficiency, commercial ties and expanded production and do not speak to how evenly the routes tied the regions."),
 ("higher after the new machinery in every workshop",
  "Recomputed in q27 from the table alone: the later figure exceeds the earlier one in all four rows. KC-4.2.I.B states that the innovations it names increased the efficiency of production methods."),
 ("North and the Midwest grows much faster than traffic between the North and the South",
  "Recomputed in q28 from the table alone: the first column rises more than sevenfold and the second by about half. KC-4.2.I.C states that transportation networks linked the North and Midwest more closely than they linked regions in the South. The anchor carries both links because the leading distractor exchanges them."),
 ("Both indexes rise together",
  "Recomputed in q29 from the table alone: both columns rise at every step, and neither leads throughout. KC-4.2.III.B calls the growth of Northern manufacturing, banking, and shipping industries RELATED to increasing Southern cotton production."),
 ("legislation and courts supported routes that enlarged markets unevenly",
  "The keyed sentence collects KC-4.2.I.A, KC-4.2.I.B, KC-4.2.I.C and KC-4.2.III.B in the order the topic page prints them and adds nothing; each rejected version contradicts one of the four."),
]


def _extra_mutations():
    def machinery_lowers_output(mod, cl):
        t = mod.QUESTIONS[26]["table"]
        t["rows"] = [list(r) for r in t["rows"]]
        for row in t["rows"]:
            row[1], row[2] = row[2], row[1]

    def southern_link_outgrows_the_midwest(mod, cl):
        # The comparison this topic exists to get right, reversed. The growth
        # guard is written FIRST in q28 so this fires there rather than on the
        # literal row comparison at the end.
        t = mod.QUESTIONS[27]["table"]
        t["rows"] = [list(r) for r in t["rows"]]
        for row in t["rows"]:
            row[1], row[2] = row[2], row[1]

    def northern_index_falls(mod, cl):
        t = mod.QUESTIONS[28]["table"]
        t["rows"] = [list(r) for r in t["rows"]]
        for row, value in zip(t["rows"], ["141", "83", "48", "25"]):
            row[2] = value

    return [
        ("output per worker recorded as falling after the new machinery",
         machinery_lowers_output),
        ("the two freight columns exchanged, so the Southern link is the faster growing",
         southern_link_outgrows_the_midwest),
        ("the Northern index reversed so it falls across the decades", northern_index_falls),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    wh_stimulus.controls(a4_5)
    for label, mutate in _extra_mutations():
        mod = wh_check._mutant(a4_5)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            wh_check.history_style(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as e:
            print(f"  control OK  {label}: {str(e)[:110]}")
        else:
            raise SystemExit(f"CONTROL FAILED: {label} did not raise")

wh_check.run(a4_5, CLAIMS, TABLE_CHECKS, sys.argv)
