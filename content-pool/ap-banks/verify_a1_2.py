"""Key audit for AP U.S. HISTORY 1.2 Native American Societies Before European Contact.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The shared gate is
``wh_check.run`` -- its checks are about history rather than about world
history: a KC code or Learning Objective in every ``why`` and every ``claim``,
no figure language, no typeset markup, the marked-stimulus rule, and the
structural gate from ``cg_check``.

WHAT THE KEYS REST ON
---------------------
  Unit 1 Learning Objective B, native populations
    and the natural environment                    items 1, 16, 19, 20, 26, 29
  KC-1.1, adapting to AND transforming diverse
    environments                                   9, 17, 20, 30
  KC-1.1.I, four kinds of innovation               12, 17, 20, 26, 30
  KC-1.1.I.A, maize northward, irrigation,
    social diversification                         2, 3, 10, 17, 18, 22, 28
  KC-1.1.I.B, aridity and grassland, largely
    mobile lifestyles                              4, 9, 11, 21, 25
  KC-1.1.I.C, mixed economies, permanent
    villages                                       5, 6, 12, 23, 25, 28
  KC-1.1.I.D, hunting and gathering, settled
    coastal communities                            7, 8, 13, 21, 24, 27
  the GEO thematic focus and skill 1.A             16, 19
  Reasoning Process 1, Comparison                  29

THE SWAP ITEMS, and why their anchors carry two clauses. This topic's four
sub-points are four AREA-plus-WAY-OF-LIFE pairs, so the natural wrong answer is
not a false claim but a TRUE claim attached to the wrong area. Items 2, 4, 7, 8
and 28 each carry a distractor that is the exact exchange of the key's two
halves, and each anchor therefore names the area and the way of life together
(or the KC code and the clause together). An anchor naming only one half would
match its own swap, which is the defect ``verify_e2_1.py`` shipped.

DATA ITEMS: 14, 15 and 25 carry tables of explicitly illustrative data,
recomputed below from the table alone, with each distractor falsified against
the same rows.

  * Items 14 and 15 share ``_T_REGIONS``, which is CATEGORICAL. The shared
    corrupter appends text to a cell, and ``startswith`` or a substring test
    survives an appended suffix -- the failure a1_1 records, where a check could
    not object to anything in its own table. So the expected AREA and CONDITION
    columns are stated here, independently of the module, and item 15 states the
    whole expected row set. The WAY OF LIFE column is deliberately left to the
    semantic guards in ``q14`` instead, so the control that exchanges two ways of
    life raises on the claim the item actually makes rather than on a row-equality
    assertion that would say nothing about it.
  * Item 15 keys what the table CANNOT support, so its first guard is on the
    table's HEADERS: no column reports relations between areas, and corrupting a
    cell cannot make an absent column present. The header guard runs BEFORE the
    row comparison for the reason a1_1 gives -- the control for this item adds a
    trade column, and a row-equality assertion running first would raise on the
    row width instead, passing the control for a reason that says nothing about
    the guard it names.
  * Item 25's table is numeric, and it caught 10 of its 12 corrupted cells only
    after a real hole was found by reading the two it missed. The corrupter
    turned a four-month occupation into twenty-three, and "occupied for the whole
    year" then became true of a third site while every derived assertion still
    passed, because they counted cells equal to twelve. The bound on the column
    is what closes it. The two still uncaught are honest: the key names WHICH
    sites carry permanent dwellings, so enlarging a count at a site that already
    has them leaves the keyed claim true, and a check has no business inventing
    an objection to that. The site labels are compared literally so that a
    corrupted label is caught.

NEGATIVE CONTROLS: ``python3 verify_a1_2.py --selftest``.
"""
import sys

import cg_check as cg
import wh_check
import a1_2

AREA = "Area of North America (illustrative)"
CONDITION = "Environmental condition described"
WAY = "Way of life described"
SITE = "Site (illustrative)"
MONTHS = "Months of the year the site was occupied"
DWELLINGS = "Permanent dwellings recorded at the site"


def _col(table, header):
    idx = table["headers"].index(header)
    return [row[idx] for row in table["rows"]]


_EXPECTED_AREAS = ["Area W", "Area X", "Area Y", "Area Z"]
_EXPECTED_CONDITIONS = [
    "Arid basin and open grassland",
    "River valley with fertile floodplain",
    "Dry uplands watered by canals dug for the purpose",
    "Ocean coast rich in fish and sea mammals",
]
_EXPECTED_WAYS = [
    "Largely mobile, moving with the seasons",
    "Permanent villages, farming with hunting and fishing",
    "Permanent towns supported by maize",
    "Settled communities that do not farm",
]


def q14(table, item):
    # Only the AREA and CONDITION columns are compared literally. The WAY column
    # is left to the semantic guards below, so the control that exchanges two
    # ways of life raises HERE, on the covariation the key asserts, rather than
    # on a row-equality assertion that would prove nothing about it.
    assert _col(table, AREA) == _EXPECTED_AREAS, (
        f"the areas are not the ones this check was written against; got {_col(table, AREA)}")
    assert _col(table, CONDITION) == _EXPECTED_CONDITIONS, (
        f"the environmental conditions are not the ones this check was written against; "
        f"got {_col(table, CONDITION)}")
    conditions, ways = _col(table, CONDITION), _col(table, WAY)
    assert len(set(ways)) == len(ways), f"the ways of life must all differ; got {ways}"
    assert len(set(conditions)) == len(conditions), \
        f"the environmental conditions must all differ; got {conditions}"
    settled = [w for w in ways if "permanent" in w.lower() or "settled" in w.lower()]
    assert len(settled) == 3, (
        f"'only one area is recorded with a settled or permanent way of life' must be "
        f"false and countable; {len(settled)} rows are settled or permanent")
    farmed = [w for w in ways if "maize" in w.lower()]
    assert len(farmed) == 1, (
        f"'every area is recorded as growing maize' must be false; {len(farmed)} of "
        f"{len(ways)} rows record maize")
    mobile = [(c, w) for c, w in zip(conditions, ways) if "mobile" in w.lower()]
    assert len(mobile) == 1, f"exactly one row must record a mobile way of life; got {mobile}"
    assert "ocean" not in mobile[0][0].lower(), (
        f"'the mobile way of life is recorded alongside the ocean coast' must be false, "
        f"but the mobile row's condition is {mobile[0][0]!r}")
    return (f"{len(ways)} areas carry {len(set(conditions))} distinct conditions and "
            f"{len(set(ways))} distinct ways of life, {len(settled)} of them settled, "
            f"{len(farmed)} recording maize, and the one mobile row sits against "
            f"{mobile[0][0]!r} rather than the ocean coast")


def q15(table, item):
    # HEADER GUARD FIRST, then the rows. This item keys what the table CANNOT
    # support, so its guard is on the COLUMNS rather than on any value in them:
    # exchange between areas is unsupported because no column reports it, and
    # corrupting a cell cannot make an absent column present. The control for
    # this item adds a trade column; if row equality ran first it would raise on
    # the row width instead, which would say nothing about this guard.
    joined = " ".join(str(h) for h in table["headers"]).lower()
    for word in ("trade", "contact", "exchange", "relation", "neighbour", "neighbor"):
        assert word not in joined, (
            f"the table must report nothing about relations between areas for the key to "
            f"hold, but a header mentions {word!r}: {table['headers']}")
    expected = [list(r) for r in zip(_EXPECTED_AREAS, _EXPECTED_CONDITIONS, _EXPECTED_WAYS)]
    assert [list(r) for r in table["rows"]] == expected, (
        f"the areas table does not hold the rows this check was written against; "
        f"got {table['rows']}")
    conditions, ways = _col(table, CONDITION), _col(table, WAY)
    assert len(set(conditions)) > 1, "'the recorded conditions differ from area to area' must be true"
    assert sum(1 for w in ways if "permanent" in w.lower() or "settled" in w.lower()) == 3, \
        "'three of the four areas are settled or permanent' must be true"
    assert any("maize" in w.lower() for w in ways), \
        "'one recorded way of life rests on maize' must be true"
    assert any("mobile" in w.lower() for w in ways), \
        "'one recorded way of life is largely mobile' must be true"
    return ("no column reports exchange between the areas, while all four remaining "
            "options are read directly off the rows")


def q25(table, item):
    # The labels are compared literally so a corrupted label is caught; the
    # numbers are left to the derived assertions. The catch rate is PARTIAL on
    # purpose: the key names WHICH sites carry permanent dwellings, so enlarging
    # a dwelling count at a site that already has them leaves the key true, and
    # a check has no business inventing an objection to it.
    assert cg.labels(table) == ["Site 1", "Site 2", "Site 3", "Site 4"], (
        f"the site labels are not the ones this check was written against; "
        f"got {cg.labels(table)}")
    months, dwellings = cg.col(table, MONTHS), cg.col(table, DWELLINGS)
    # A year has twelve months, so a column of months per year that runs past
    # twelve is not data the key can be read off at all. Without this the
    # corrupter's 4 into 23 slipped through: "occupied for the whole year"
    # would then be true of a third site while the count of cells equal to
    # twelve stayed at two, and the keyed claim would be false with every
    # derived assertion still passing.
    assert all(1 <= m <= 12 for m in months), \
        f"months of the year must lie between one and twelve; got {months}"
    full_year = [i for i, m in enumerate(months) if m == 12]
    with_dwellings = [i for i, d in enumerate(dwellings) if d > 0]
    assert len(full_year) == 2, f"exactly two sites must be occupied all year; got {months}"
    assert with_dwellings == full_year, (
        f"the sites with permanent dwellings must be exactly the sites occupied all year; "
        f"dwellings {dwellings} against months {months}")
    assert any(d == 0 for d in dwellings), \
        "'permanent dwellings are recorded at every site' must be false"
    fewest = min(range(len(months)), key=lambda i: months[i])
    assert dwellings[fewest] != max(dwellings), (
        f"'the site occupied for the fewest months records the most dwellings' must be "
        f"false; that site records {dwellings[fewest]} against a maximum of {max(dwellings)}")
    assert len(full_year) < len(months), "'every site was occupied for the whole year' must be false"
    assert len(set(dwellings)) > 1, "'the same number of dwellings at every site' must be false"
    return (f"months {months} against dwellings {dwellings}: the two sites at twelve "
            f"months are exactly the two carrying dwellings, and the other two carry none")


TABLE_CHECKS = {14: q14, 15: q15, 25: q25}

CLAIMS = [
 ("interacted with the natural environment in North America",
  "Unit 1 Learning Objective B gives the phrase verbatim: explain how and why various native populations in the period before European contact interacted with the natural environment in North America."),
 ("Northward from present-day Mexico into the present-day American Southwest",
  "KC-1.1.I.A states the direction and the endpoints together, from present-day Mexico northward into the present-day American Southwest and beyond. The anchor carries both because the leading distractor is the exact reversal."),
 ("advanced irrigation, and social diversification",
  "KC-1.1.I.A names economic development, settlement, advanced irrigation, and social diversification as what the spread of maize cultivation supported, and no other list in the topic overlaps it."),
 ("Largely mobile lifestyles, in response to the aridity of the Great Basin",
  "KC-1.1.I.B joins the response to the environment in one sentence: societies responded to the aridity of the Great Basin and the grasslands of the western Great Plains by developing largely mobile lifestyles. Both halves are in the anchor because each distractor keeps one and replaces the other."),
 ("the Mississippi River Valley, and the Atlantic seaboard",
  "KC-1.1.I.C names the Northeast, the Mississippi River Valley, and along the Atlantic seaboard; every rejected set imports an area belonging to KC-1.1.I.A, KC-1.1.I.B or KC-1.1.I.D."),
 ("hunter-gatherer economies favored the development of permanent villages",
  "KC-1.1.I.C states that some societies developed mixed agricultural and hunter-gatherer economies that favored the development of permanent villages; the mobile outcome belongs to KC-1.1.I.B and irrigated maize to KC-1.1.I.A."),
 ("By hunting and gathering, with settled communities in some areas",
  "KC-1.1.I.D holds hunting and gathering together with settled communities supported by the vast resources of the ocean, so the anchor carries both clauses against a distractor that denies the second."),
 ("The Great Basin with largely mobile lifestyles",
  "KC-1.1.I.B places mobility in the Great Basin and the western Great Plains and KC-1.1.I.D places settled coastal communities in the Northwest; the leading distractor exchanges the two areas while keeping both ways of life, so the anchor names an area and its way of life together."),
 ("without asserting that no society in those areas ever stayed in one place",
  "KC-1.1.I.B's qualifier 'largely' states a predominant pattern rather than a rule without exceptions, which is what separates the general claim from the absolute one."),
 ("KC-1.1.I.A, on maize cultivation supporting settlement",
  "KC-1.1.I.A names settlement and advanced irrigation among what the spread of maize cultivation supported, and the described site combines both with the crop; the land is dry but the response described is irrigation rather than KC-1.1.I.B's mobility."),
 ("KC-1.1.I.B, on societies responding to aridity and grassland",
  "KC-1.1.I.B is the only sub-point joining aridity and grassland to largely mobile lifestyles, and the described group has both the environment and the response."),
 ("KC-1.1.I.C, on mixed agricultural and hunter-gatherer economies favoring",
  "KC-1.1.I.C describes economies mixing agriculture with hunting and gathering and says they favored the development of permanent villages, which is exactly the combination described in the stem."),
 ("KC-1.1.I.D, on hunting and gathering with settled communities",
  "KC-1.1.I.D is the only sub-point that puts settled communities and the absence of farming together, naming the vast resources of the ocean as what supported them."),
 ("each differs alongside a different environmental condition",
  "Recomputed in q14 from the table alone, including that each rejected option is false on the same rows. KC-1.1.I is the framework's statement that different native societies adapted to and transformed their environments, which is the covariation the table shows."),
 ("peoples of these areas traded with one another",
  "Recomputed in q15: no column of the table reports relations between areas, so this is the one claim of the five the record cannot reach. KC-1.1.I concerns agriculture, resource use and social structure rather than exchange between regions."),
 ("foster regional diversity",
  "The Geography and the Environment thematic focus printed on this topic page states that geographic and environmental factors shape the development of America and foster regional diversity, which is the relationship Unit 1 Learning Objective B asks students to explain."),
 ("advanced irrigation that followed the spread of maize cultivation",
  "KC-1.1 says societies adapted to AND transformed their environments, and KC-1.1.I.A's advanced irrigation is the one item among the four sub-points that alters the land rather than accommodating it."),
 ("social consequences as well as economic and settlement ones",
  "KC-1.1.I.A puts social diversification in the same list as economic development, settlement and advanced irrigation, so one agricultural change is given consequences of several kinds at once, and KC-1.1.I names social structure alongside agriculture."),
 ("Identify a historical concept, development, or process",
  "Skill 1.A as printed on this topic page, applied to the four ways of life KC-1.1.I describes under Unit 1 Learning Objective B; the distractors are skills 1.B, 4.A, 5.A and 3.B from other pages of this course."),
 ("four ways of adapting to different environments and ranks none",
  "KC-1.1.I sets four regional ways of life beside one another without ordering them, and KC-1.1 calls the resulting societies distinct rather than ranked. Agriculture appears in KC-1.1.I.A and KC-1.1.I.C but not in all four."),
 ("does not make settled life depend on agriculture",
  "KC-1.1.I.D has societies supporting themselves by hunting and gathering and nonetheless developing settled communities where ocean resources were vast, while KC-1.1.I.B has mobility follow from aridity and grassland."),
 ("does not fix the northern limit of the spread",
  "KC-1.1.I.A writes that maize cultivation spread into the present-day American Southwest 'and beyond', which leaves the far end of the movement open rather than closing it at a boundary."),
 ("every society in the Northeast, the Mississippi River Valley and along the Atlantic seaboard",
  "KC-1.1.I.C's word 'some' makes the mixed economy a pattern among societies of those areas rather than a description of all of them, so the universal claim is the one the sentence blocks."),
 ("in part of that region rather than throughout it",
  "KC-1.1.I.D says settled communities developed 'in some areas' of the Northwest and present-day California, which neither extends settlement to the whole region nor denies it."),
 ("the two at which permanent dwellings are recorded",
  "Recomputed in q25 from the months and dwellings columns alone. KC-1.1.I.C ties permanent villages to economies that kept people in one place and KC-1.1.I.B ties mobility to the dry areas, which is the contrast such a record would illustrate."),
 ("links a way of life to the environment of the area",
  "KC-1.1.I.A, KC-1.1.I.B, KC-1.1.I.C and KC-1.1.I.D each attach a way of life to the conditions of a named area, which is the general statement KC-1.1.I makes and Unit 1 Learning Objective B asks students to explain."),
 ("which says those societies supported themselves by hunting and gathering",
  "KC-1.1.I.D states that societies in the Northwest and present-day California supported themselves by hunting and gathering, which directly denies a maize-based livelihood there; KC-1.1.I.A concerns a different region and direction."),
 ("KC-1.1.I.A ties settlement to maize cultivation and advanced irrigation",
  "KC-1.1.I.A names settlement and advanced irrigation among what maize cultivation supported, while KC-1.1.I.C makes permanent villages follow from mixed agricultural and hunter-gatherer economies. The anchor carries the code with its clause because the distractor exchanges them."),
 ("similarities and/or differences between different historical developments",
  "Reasoning Process 1, Comparison, opens with describing similarities and/or differences between different historical developments or processes, and the unit outline prints Comparison beside this topic, whose content is the four regional ways of life of KC-1.1.I."),
 ("took a different form in each area the framework names",
  "KC-1.1.I in the framework's own words, with the observation that its four sub-points describe four different forms and nothing more; KC-1.1.I.A's irrigation and KC-1.1.I.D's farmless settled communities are what defeat the remaining options."),
]


def _extra_mutations():
    def trade_column_appears(mod, cl):
        # q15 keys what the table cannot support; a column reporting exchange
        # between areas would make the keyed claim reachable and the item wrong.
        t = dict(mod.QUESTIONS[14]["table"])
        t["headers"] = list(t["headers"]) + ["Trade with other areas"]
        t["rows"] = [list(r) + ["Recorded"] for r in t["rows"]]
        mod.QUESTIONS[14]["table"] = t

    def ways_of_life_exchanged(mod, cl):
        # Move the mobile way of life onto the ocean row and the coastal one onto
        # the arid row. Every column still holds the same multiset of values, so
        # a corruption of a single cell cannot express this; only q14's semantic
        # guard on which condition the mobile row sits against can see it.
        t = dict(mod.QUESTIONS[13]["table"])
        rows = [list(r) for r in t["rows"]]
        rows[0][2], rows[3][2] = rows[3][2], rows[0][2]
        t["rows"] = rows
        mod.QUESTIONS[13]["table"] = t
        mod.QUESTIONS[14]["table"] = t

    return [
        ("a trade column added, making q15's unsupportable claim supportable",
         trade_column_appears, "relations between areas"),
        ("the mobile and coastal ways of life exchanged between rows",
         ways_of_life_exchanged, "mobile row's condition"),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    import contextlib
    import io
    for label, mutate, expect in _extra_mutations():
        mod = wh_check._mutant(a1_2)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            with contextlib.redirect_stdout(io.StringIO()):
                wh_check.history_style(mod, claims)
                cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as e:
            # A control that fires for the WRONG reason proves nothing about the
            # guard it names, so the message is checked, not just the fact of it.
            assert expect in str(e), f"CONTROL FIRED FOR THE WRONG REASON: {label} -- {e}"
            print(f"  control OK  {label}: {str(e)[:110]}")
        else:
            raise SystemExit(f"CONTROL FAILED: {label} did not raise")

wh_check.run(a1_2, CLAIMS, TABLE_CHECKS, sys.argv)
