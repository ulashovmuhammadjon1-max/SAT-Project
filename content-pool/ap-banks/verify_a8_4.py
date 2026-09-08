"""Key audit for AP U.S. HISTORY 8.4 Economy after 1945.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states the CED sentence the key rests on, with its Key Concept code. ``wh_check``
refuses a ``why`` or a ``claim`` citing neither a KC code nor a Learning
Objective.

WHAT THE KEYS REST ON. This topic prints TWO Learning Objectives beneath two
thematic focuses, with one historical development under each:

  Unit 8 Learning Objective D, causes of growth      items 1, 14, 19, 26
  KC-8.3.I.A, a burgeoning private sector, federal
    spending, the baby boom, technological
    developments                                     3, 4, 9, 14, 17, 18, 19, 26, 27, 30
  Unit 8 Learning Objective E, causes and effects
    of migration                                     2, 10, 24, 28
  KC-8.3.I.B, education and technology expanding,
    social mobility, the suburbs, the South and
    West, the Sun Belt                               5, 6, 7, 8, 12, 13, 15, 16, 21, 22,
                                                     23, 24, 25, 28, 29, 30
  KC-8.3.I, their shared parent, cited only where an
    item needs the frame they sit inside             20, 30
  skill 2.C                                          10, 11, 17, 21, 29

WHAT IS DELIBERATELY NOT KEYED. KC-8.3.I.A names four contributors and says they
"helped spur" growth. It does not rank them, quantify any of them, or claim they
were the only ones, so no key here ranks the four. The single item that asks
about relative size (14) asks it of a hypothetical table and is recomputed from
that table alone. No key names a statute, agency, company, highway programme or
mortgage scheme; the framework names none, and this topic's OPTIONAL SOURCES
page is explicitly not required content.

THE SWAP ITEMS, where a distractor exchanges the halves of the key and the
anchor therefore carries both clauses:
  q6   the middle class to the SUBURBS and many Americans to the South and West
  q7   the Sun Belt significant politically AND economically
  q11  strong evidence of the offer, weak evidence of the conditions
  q15  the South and West gaining by the larger share of THEIR OWN start
  q21  an insider's reason, not a measure of how common it was
  q29  a sequence seen whole, but through later knowledge

DATA ITEMS: 14, 15 and 16. Every table check runs its DERIVED assertions -- the
ones carrying the keyed claim -- before the literal guard on the rows it was
written against. ``_T_MOVE`` is categorical: appending text to a destination
cell leaves "suburb", "South" and "West" all still present as substrings, so
without the literal guard those cells would be undefended, which is the failure
a1_1's verifier records and the harness refuses.

NEGATIVE CONTROLS: ``python3 verify_a8_4.py --selftest``. Three targeted
controls check WHICH assertion raised, not merely that something did.
"""
import sys

import wh_check
import wh_stimulus as ws
import a8_4

MEASURE = "Measure in a hypothetical record"
BASE = "Index in 1948 (1948 equals 100)"
LATER = "Index in 1968"
GROUPING = "Grouping of regions in a hypothetical record"
POP50 = "Population in 1950 (millions)"
POP70 = "Population in 1970 (millions)"
HOUSEHOLD = "Household in a hypothetical survey"
REASON = "Reason the survey records for moving"
DESTINATION = "Destination the survey records"


def _col(table, header):
    idx = table["headers"].index(header)
    return [row[idx] for row in table["rows"]]


def _nums(table, header):
    return [float(v.replace(",", "")) for v in _col(table, header)]


_EXPECTED_MEASURES = [
    ["Private sector output", "100", "196"],
    ["Federal spending", "100", "172"],
    ["Patents granted", "100", "158"],
    ["Births per year", "100", "134"],
]


def q14(table, item):
    base, later = _nums(table, BASE), _nums(table, LATER)
    labels = _col(table, MEASURE)
    assert all(v == 100 for v in base), (
        f"the column says 1948 equals 100, so every base value must be 100; got {base}"
    )
    assert all(l > b for b, l in zip(base, later)), (
        f"'one of the four measures stands lower in the later year' must be false; got {later}"
    )
    assert all(l < 2 * b for b, l in zip(base, later)), (
        f"the key says none of them doubles, so 'every measure more than doubles' is false; "
        f"got {later} against a base of {base}"
    )
    top = labels[later.index(max(later))]
    assert top == "Private sector output", (
        f"the key says private sector output rises by the most, so 'federal spending rises by "
        f"the most' must be false; the largest later index belongs to {top!r}"
    )
    assert len(set(later)) == len(later), (
        f"'the four stand at the same level as each other in the later year' must be false; "
        f"got {later}"
    )
    assert [list(r) for r in table["rows"]] == _EXPECTED_MEASURES, (
        f"the measures table does not hold the rows this check was written against; "
        f"got {table['rows']}"
    )
    return (f"all four later indices {later} exceed a base of 100 without reaching 200, they "
            f"are all different, and the largest belongs to {top!r}")


_EXPECTED_REGION = [
    ["South and West together", "58", "89"],
    ["Northeast and Midwest together", "93", "111"],
]


def q15(table, item):
    early, late = _nums(table, POP50), _nums(table, POP70)
    labels = _col(table, GROUPING)
    assert len(labels) == 2, f"the key compares two groupings; the table holds {len(labels)}"
    assert all(l > e for e, l in zip(early, late)), (
        f"'the South and West lose population' must be false and both groupings must gain; "
        f"got {early} then {late}"
    )
    rates = [l / e for e, l in zip(early, late)]
    sw, ne = labels.index("South and West together"), labels.index("Northeast and Midwest together")
    # BOTH clauses of the key: each gains, AND the southern and western rate is the larger.
    assert rates[sw] > rates[ne], (
        f"the key says the South and West gain by a larger share of their own starting "
        f"population, so the reversed reading must be false; the rates are "
        f"{[round(x, 3) for x in rates]}"
    )
    assert late[ne] > late[sw], (
        f"'the South and West hold a larger population in the later year' must be false; "
        f"got {late[sw]} against {late[ne]}"
    )
    assert late[ne] != late[sw], "'the two are recorded at the same population' must be false"
    assert [list(r) for r in table["rows"]] == _EXPECTED_REGION, (
        f"the region table does not hold the rows this check was written against; "
        f"got {table['rows']}"
    )
    return (f"both groupings gain, at rates {[round(x, 3) for x in rates]}, the larger belonging "
            f"to the South and West, which still hold the smaller population in the later year")


_EXPECTED_MOVE = [
    ["Household 1", "A new job in a growing industry", "A suburb of the same metropolitan area"],
    ["Household 2", "Completion of a course of higher education", "A city in the South"],
    ["Household 3", "A new job in a growing industry", "A city in the West"],
    ["Household 4", "Completion of a course of higher education",
     "A suburb of the same metropolitan area"],
]

# KC-8.3.I.B's own two directions of movement, written out here rather than read
# back out of the table this check is checking.
_DIRECTIONS = ("suburb", "south", "west")


def q16(table, item):
    dests = [d.strip().lower() for d in _col(table, DESTINATION)]
    reasons = [r.strip() for r in _col(table, REASON)]
    assert all(any(d in dest for d in _DIRECTIONS) for dest in dests), (
        f"the key says every destination falls under one of the directions KC-8.3.I.B names; "
        f"got {dests}"
    )
    suburban = [d for d in dests if "suburb" in d]
    regional = [d for d in dests if "south" in d or "west" in d]
    assert suburban and regional, (
        f"'every household moved to a suburb' and 'no household moved to the South or West' must "
        f"both be false, so both kinds of destination must appear; got {dests}"
    )
    assert not any("northeast" in d or "midwest" in d for d in dests), (
        f"'one household moved to the Northeast' must be false; got {dests}"
    )
    assert len(set(reasons)) == 2, (
        f"'every household records the same reason' must be false, and the record this check was "
        f"written against holds exactly two distinct reasons; got {sorted(set(reasons))}"
    )
    assert [list(r) for r in table["rows"]] == _EXPECTED_MOVE, (
        f"the household table does not hold the rows this check was written against; "
        f"got {table['rows']}"
    )
    return (f"{len(suburban)} destinations are suburban and {len(regional)} lie in the South or "
            f"West, none elsewhere, against {len(set(reasons))} distinct recorded reasons")


TABLE_CHECKS = {14: q14, 15: q15, 16: q16}

CLAIMS = [
 ("causes of economic growth in the years after World War II",
  "Unit 8 Learning Objective D reads 'Explain the causes of economic growth in the years after World War II'; the distractors are Learning Objectives E, B and C of the same unit."),
 ("causes and effects of the migration of various groups of Americans after 1945",
  "Unit 8 Learning Objective E, printed beneath this topic's second thematic focus; Learning Objective K, on continuities and changes in immigration patterns, belongs to a later topic of the unit."),
 ("burgeoning private sector, federal spending, the baby boom, and technological developments",
  "KC-8.3.I.A names exactly these four as having helped spur economic growth; higher education and the Sun Belt belong to KC-8.3.I.B, which is about migration."),
 ("contributed to growth without the sentence claiming any one of them produced it alone",
  "KC-8.3.I.A says the four things 'helped spur' economic growth, which attributes contribution rather than sufficiency, and it lists them without ranking or weighting."),
 ("Higher education opportunities and new technologies",
  "KC-8.3.I.B opens 'As higher education opportunities and new technologies rapidly expanded'; federal spending, the private sector and the birth rate belong to KC-8.3.I.A instead."),
 ("middle class to the suburbs and of many Americans to the South and West",
  "KC-8.3.I.B attaches each group to its own destination: the middle class to the suburbs, many Americans to the South and West. The anchor carries both pairings because a distractor exchanges them."),
 ("emerged as a significant political and economic force",
  "KC-8.3.I.B states that the Sun Belt region emerged as a significant political AND economic force; the anchor carries both kinds of significance because two distractors keep one and drop the other."),
 ("social mobility increased, and migration to the suburbs and to the South and West followed",
  "KC-8.3.I.B is a chain: as higher education opportunities and new technologies rapidly expanded, increasing social mobility encouraged the two migrations, and the Sun Belt then emerged."),
 ("reduction in the amount the federal government spent",
  "KC-8.3.I.A names federal SPENDING among the four contributors, so a reduction in what the federal government spent is the reverse of what the sentence says. The keyed choice is worded this way rather than as 'the reduction of federal spending' because that phrasing made the key a strict superset of the distractor 'Federal spending', which cg_check rightly refuses: a student who accepts the shorter option has no ground to reject the longer."),
 ("including how these might limit the use or uses of a source",
  "Skill 2.C as printed beside this topic and practised in meeting Unit 8 Learning Objective D and Learning Objective E; skill 2.B, the near-neighbour distractor, stops before the limiting step."),
 ("strong evidence of what buyers were being offered and weak evidence of what life in such a development was like",
  "KC-8.3.I.B records the migration of the middle class to the suburbs, and skill 2.C asks how purpose limits use. The anchor carries both halves because a distractor keeps the purpose and reverses what the source is good evidence of."),
 ("rapid expansion of higher education opportunities",
  "KC-8.3.I.B places the rapid expansion of higher education opportunities before increasing social mobility, and new degree programmes with rising admissions are evidence of that expansion."),
 ("Sun Belt region emerged as a significant political and economic force",
  "KC-8.3.I.B closes with this claim, and an appeal to move production toward a growing southern state is an instance of that economic weight; federal spending belongs to KC-8.3.I.A."),
 ("stand higher in the later year without any of them doubling, and private sector output rises by the most",
  "Recomputed in q14 from the table alone, with every rejected reading falsified against the same rows. KC-8.3.I.A names four contributors together and ranks none of them, so the ranking here is the hypothetical table's and not the framework's."),
 ("South and West gain by a larger share of their own starting population",
  "Recomputed in q15. KC-8.3.I.B records the migration of many Americans to the South and West and the Sun Belt's emergence; the anchor names which grouping gains faster because a distractor reverses exactly that."),
 ("either a suburb or a place in the South or West",
  "Recomputed in q16 from the table alone. KC-8.3.I.B names two directions of movement, the middle class to the suburbs and many Americans to the South and West, and every recorded destination falls under one of them."),
 ("records one household, so it cannot by itself show how widely",
  "KC-8.3.I.A names technological developments and a burgeoning private sector among the contributors to growth, so the subject is inside the topic; skill 2.C makes breadth the limit on a single household's account."),
 ("The baby boom",
  "KC-8.3.I.A names the baby boom among the things that helped spur economic growth, and an argument from a larger number of children appeals to it; higher education and the Sun Belt belong to KC-8.3.I.B."),
 ("names federal spending as one of four contributors",
  "KC-8.3.I.A places federal spending in a list with a burgeoning private sector, the baby boom and technological developments, so the framework treats government outlays as one contributor among several rather than as the whole explanation."),
 ("both sit beneath the same key concept about postwar change",
  "KC-8.3.I.A and KC-8.3.I.B are both lettered sub-points of KC-8.3.I, on rapid economic and social changes in American society fostering a sense of optimism in the postwar years."),
 ("giving one migrant's reason rather than a measure of how common that reason was",
  "KC-8.3.I.B records the migration of many Americans to the South and West, and skill 2.C asks how point of view bears on use. The anchor carries both halves because a distractor keeps the insider's position and claims it measures a pattern."),
 ("households' education or occupation to whether and where they moved",
  "KC-8.3.I.B makes increasing social mobility the link between expanding education and technology on one side and migration on the other, so evidence for it must connect a household's position to its movement."),
 ("migration of the middle class to the suburbs",
  "KC-8.3.I.B names this as one of the two movements increasing social mobility encouraged; a shift of households from a central city to the districts around it is that movement rather than the move toward the South and West."),
 ("asks about several movements of population rather than one",
  "Unit 8 Learning Objective E asks about the migration of VARIOUS groups of Americans after 1945, and KC-8.3.I.B supplies two distinct movements with different groups and destinations."),
 ("people had been moving into the South",
  "KC-8.3.I.B states that increasing social mobility encouraged the migration of many Americans to the South and West, and a population largely born in other states is evidence of arrivals."),
 ("Technological developments played no part",
  "KC-8.3.I.A names technological developments among the four things that helped spur economic growth, so denying their part contradicts the sentence; the rejected options restate it."),
 ("Technological developments",
  "KC-8.3.I.A names technological developments among the contributors to growth, and machinery raising output per worker is such a development; the baby boom and federal spending are the sentence's other contributors."),
 ("emergence of the Sun Belt region as a significant political and economic force",
  "KC-8.3.I.B records this as the outcome of the migrations it describes, which is the EFFECT Unit 8 Learning Objective E asks students to explain alongside the causes."),
 ("trace a whole sequence of moves but reports them through what the writer knew later",
  "KC-8.3.I.B names both a move to the suburbs and a move to the South and West, and skill 2.C asks what a source's historical situation contributes and what it limits. The anchor carries both halves because a distractor keeps the distance and claims contemporary accuracy."),
 ("several forces together spurred economic growth, and that the mobility accompanying it",
  "KC-8.3.I.A supplies the several contributors and KC-8.3.I.B the mobility, the two migrations and the Sun Belt's emergence; both are sub-points of KC-8.3.I, on rapid economic and social changes in American society."),
]


def _targeted_controls():
    """Each must raise on the DERIVED guard it names, not on the literal backstop."""
    def spending_overtakes(mod, cl):
        t = dict(mod.QUESTIONS[13]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][1][2] = "198"          # federal spending now the largest riser
        mod.QUESTIONS[13]["table"] = t

    def rates_reverse(mod, cl):
        t = dict(mod.QUESTIONS[14]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][1][2] = "150"          # the Northeast and Midwest now grow faster
        mod.QUESTIONS[14]["table"] = t

    def a_household_leaves_the_pattern(mod, cl):
        t = dict(mod.QUESTIONS[15]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][2][2] = "A city in the Northeast"
        mod.QUESTIONS[15]["table"] = t

    return [
        ("federal spending made the largest riser, so q14's keyed ranking fails",
         spending_overtakes, "private sector output rises by the most"),
        ("the Northeast and Midwest made to grow faster, so q15's keyed comparison fails",
         rates_reverse, "larger share of their own starting population"),
        ("one household moved to the Northeast, so q16's keyed coverage fails",
         a_household_leaves_the_pattern, "every destination falls under one of the directions"),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    ws.controls(a8_4)
    import cg_check as cg
    for label, mutate, expect in _targeted_controls():
        mod = wh_check._mutant(a8_4)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            wh_check.history_style(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as e:
            assert expect in str(e), (
                f"CONTROL FIRED FOR THE WRONG REASON: {label} -- {e}")
            print(f"  control OK  {label}: {str(e)[:110]}")
        else:
            raise SystemExit(f"CONTROL FAILED: {label} did not raise")

wh_check.run(a8_4, CLAIMS, TABLE_CHECKS, sys.argv)
