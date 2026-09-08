"""Key audit for AP U.S. HISTORY 8.1 Contextualizing Period 8.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The shared gate is
``wh_check.run``, which the World History and US History banks both use: a KC
code or Learning Objective in every ``why`` and every ``claim``, no figure
language, no typeset markup, no non-ASCII, and the marked-stimulus rule.

WHAT THE KEYS REST ON
---------------------
  Unit 8 Learning Objective A, 1945 to 1980   items 1, 19, 20
  KC-8.1, an uncertain and unstable postwar
    world and the response to it              2, 3, 21, 23, 29, 30
  KC-8.1.I, the four aims and the
    authoritarian Soviet Union                4, 5
  KC-8.1.II, public debates and civil
    liberties                                 6, 7, 24, 28, 30
  KC-8.2, two developments, a range of
    responses                                 8, 9, 22, 29
  KC-8.2.I, Reconstruction-era promises and
    slow progress                             10, 11, 22
  KC-8.2.II, identity, social justice, the
    environment                               12, 22, 26, 28
  KC-8.2.III, attack from the left AND from
    a resurgent conservative movement         13, 21, 22, 26, 28
  KC-8.3, economic and demographic change     14, 21, 22, 29
  KC-8.3.I, a sense of optimism               15, 17, 21, 25, 27, 28
  KC-8.3.II, anxieties over the Cold War and
    debates that divided the nation           16, 17, 22, 27, 30
  skill 4.B and the topic page's own account
    of context                                11, 18, 19, 20

THE BOUNDARY THIS MODULE HAS TO HOLD. 8.1 is a CONTEXTUALIZING topic and its
Required Course Content is printed under the heading PREVIEW: UNIT 8 KEY
CONCEPTS. The lettered sub-points -- KC-8.1.I.A through KC-8.3.II.C -- are
printed on the pages of topics 8.2 through 8.14, so no key here names a
president, a war, a statute, a court case, a region or a named movement of the
period. ``no_period_detail`` asserts that, and items 20 and 29 key the boundary
itself.

THE SWAP ITEMS, where a distractor exchanges the halves of the key and the
anchor therefore has to carry BOTH clauses:
  q2   the world settled rather than unstable, or the response withdrawal
  q10  the Reconstruction tie cut, or the outcome made complete or nil
  q13  opposition to liberalism reduced to one side
  q16  the compound cause cut in half, or the divisive outcome reversed
  q19  the two approaches to context put in the wrong order

DATA ITEMS: 25, 26 and 27. ``_T_MOVEMENTS`` is CATEGORICAL, so its expected
rows are stated below independently of the module -- the shared corrupter
appends text to a cell, which leaves "identity" still present as a substring
and would otherwise catch 0 of 8 cells. ``_T_GROWTH`` and ``_T_MOOD`` are
numeric and every cell of each is load-bearing through a bound the corrupter
must break (a base year fixed at 100, a share that cannot exceed 100, a decade
step of exactly ten years).

NEGATIVE CONTROLS: ``python3 verify_a8_1.py --selftest``.
"""
import re
import sys

import wh_check
import wh_stimulus as ws
import a8_1

YEAR_G = "Year (hypothetical record)"
INDEX = "Index of real output per person (1945 equals 100)"
GOOD = "Households holding a given durable good (percent)"
MOVEMENT = "Movement recorded in a hypothetical survey"
ISSUE = "Issue the survey records it as focusing on"
YEAR_M = "Year (hypothetical poll)"
OPTIMISM = "Respondents expressing optimism about their own future (percent)"
ANXIETY = "Respondents expressing anxiety about international dangers (percent)"

# Explicit lookarounds, never \b beside a letter run. Period-8 detail that the
# lettered sub-points own and that a PREVIEW topic may not key.
#
# BARE YEARS ARE DELIBERATELY ABSENT. The framework's own periodisation is
# years, and Learning Objective A itself gives 1945 to 1980, so a year cannot
# distinguish preview from detail; a proper noun can. This repeats the finding
# recorded in verify_a1_1.py, where a year in the list fired on a distractor
# that was a wrong ANSWER SPAN rather than a reach into a later topic.
_PERIOD_DETAIL = re.compile(
    r"(?<![A-Za-z])(Korea|Vietnam|McCarthy|Truman|Eisenhower|Kennedy|Johnson|Nixon|Reagan|"
    r"Marshall|NATO|Brown|Great Society|Sun Belt|baby boom|suburb|detente|Watergate|"
    r"counterculture|evangelical|Medicare|feminist|Latino|Middle East|nuclear)(?![A-Za-z])",
    re.IGNORECASE)


def no_period_detail(module):
    """A PREVIEW topic may not key the detail its later topics own."""
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"], item["why"]] + list(item["choices"]):
            hit = _PERIOD_DETAIL.search(text)
            assert not hit, (
                f"{code} q{i}: names {hit.group(0)!r}, which belongs to topics 8.2 through "
                f"8.14 rather than to this contextualizing topic -- {text[:70]!r}"
            )
    print(f"OK  {code} scope: no item reaches into the lettered sub-points that topics "
          f"8.2 through 8.14 own.")


# ------------------------------------------------------------------ table checks

def _col(table, header):
    idx = table["headers"].index(header)
    return [row[idx] for row in table["rows"]]


def _nums(table, header):
    return [float(v.replace(",", "")) for v in _col(table, header)]


def q25(table, item):
    years = _nums(table, YEAR_G)
    index = _nums(table, INDEX)
    good = _nums(table, GOOD)
    # The base year is fixed by the column's own header, so corrupting it is
    # caught here rather than left to a monotonicity check that would not see it.
    assert index[0] == 100, (
        f"the column says 1945 equals 100, so the first index value must be 100; got {index[0]}"
    )
    steps = [b - a for a, b in zip(years, years[1:])]
    assert steps == [10, 10, 10], f"the record must run in decades; the year steps are {steps}"
    assert all(b > a for a, b in zip(index, index[1:])), (
        f"'the index falls in one of the decades' must be false; the index runs {index}"
    )
    assert all(b > a for a, b in zip(good, good[1:])), (
        f"'the two measures move in opposite directions' must be false; the good runs {good}"
    )
    assert all(0 <= v <= 100 for v in good), (
        f"a share of households cannot lie outside 0 to 100; got {good}"
    )
    assert good[0] < 20, (
        f"the key says fewer than one household in five at the start, and 'already more than "
        f"half' must be false; the first value is {good[0]}"
    )
    assert good[-1] >= 90, f"the key says nearly all households at the end; got {good[-1]}"
    assert index[-1] < 2 * index[0], (
        f"'the index more than doubles' must be false; it runs from {index[0]} to {index[-1]}"
    )
    return (f"the index rises {index} from a base of 100 without doubling, while the durable "
            f"good rises {good} from under a fifth to at least nine tenths, in decade steps")


# CATEGORICAL. The shared corrupter appends " CORRUPTED" to a cell, which leaves
# "identity" and "social justice" still present as substrings, so a check written
# only on membership reads the table without being able to object to anything in
# it -- 0 of 8 cells caught, which the harness refuses. Stating the expected rows
# here, independently of the module, makes every cell load-bearing; the derived
# assertions below are what tie the data to the key.
_EXPECTED_MOVEMENTS = [
    ["Movement 1", "Identity"],
    ["Movement 2", "Social justice"],
    ["Movement 3", "The environment"],
    ["Movement 4", "Reducing the power of the federal government"],
]

# KC-8.2.II's own three issues, written out here so the check does not read them
# back out of the table it is checking.
_KC_8_2_II_ISSUES = {"identity", "social justice", "the environment"}


def q26(table, item):
    # Only the LABEL column is compared literally. The ISSUE column is left to
    # the membership guard below, so the control that moves the fourth row
    # inside KC-8.2.II's three issues raises on the claim the item actually
    # makes rather than on a row-equality assertion that would say nothing about
    # it. Appending text to an ISSUE cell still fails, through the count of rows
    # falling outside the three. Ordered this way deliberately: with row
    # equality first, that control passed for the WRONG REASON, which proves
    # nothing about the guard it names.
    assert _col(table, MOVEMENT) == [r[0] for r in _EXPECTED_MOVEMENTS], (
        f"the survey table does not hold the row labels this check was written against; "
        f"got {_col(table, MOVEMENT)}"
    )
    issues = [v.strip().lower() for v in _col(table, ISSUE)]
    inside = [v for v in issues if v in _KC_8_2_II_ISSUES]
    outside = [v for v in issues if v not in _KC_8_2_II_ISSUES]
    assert len(inside) == 3 and sorted(inside) == sorted(_KC_8_2_II_ISSUES), (
        f"exactly three rows must record the three issues KC-8.2.II names; got {inside}"
    )
    assert len(outside) == 1, (
        f"exactly one row must record an issue outside KC-8.2.II's three, or the key is not "
        f"unique; got {outside}"
    )
    # Exact, not a substring test: appending text to this one cell leaves it
    # outside the three issues and still containing 'federal government', so a
    # containment test here catches 7 of 8 cells and reports the eighth as
    # defended when it is not.
    assert outside[0] == _EXPECTED_MOVEMENTS[3][1].lower(), (
        f"the keyed row must read exactly as the one about reducing the power of the federal "
        f"government; got {outside[0]!r}"
    )
    return (f"three rows record {sorted(inside)}, which are KC-8.2.II's three issues, and the "
            f"one remaining row records {outside[0]!r}")


def q27(table, item):
    years = _nums(table, YEAR_M)
    opt = _nums(table, OPTIMISM)
    anx = _nums(table, ANXIETY)
    steps = [b - a for a, b in zip(years, years[1:])]
    assert steps == [5, 5, 5], f"the poll must be recorded at five-year steps; got {steps}"
    assert all(0 <= v <= 100 for v in opt + anx), (
        f"a poll share cannot lie outside 0 to 100; got {opt} and {anx}"
    )
    assert all(v > 50 for v in opt), f"'a majority expressed optimism' must hold every year; {opt}"
    assert all(v > 50 for v in anx), f"'a majority expressed anxiety' must hold every year; {anx}"
    assert anx[-1] > 50, (
        f"'anxiety falls below half in the last year' must be false; the last value is {anx[-1]}"
    )
    assert any(b > a for a, b in zip(opt, opt[1:])), (
        f"'optimism declines at every reading' must be false; optimism runs {opt}"
    )
    assert all(o != a for o, a in zip(opt, anx)), (
        f"'the two shares are equal in every year' must be false; got {opt} against {anx}"
    )
    return (f"optimism runs {opt} and anxiety runs {anx}, both above half in all four years "
            f"recorded at five-year steps, and never equal in the same year")


TABLE_CHECKS = {25: q25, 26: q26, 27: q27}

CLAIMS = [
 ("Societal change from 1945 to 1980",
  "Unit 8 Learning Objective A gives the object and the span verbatim: explain the context for societal change from 1945 to 1980."),
 ("uncertain and unstable postwar world, to which the United States responded by asserting",
  "KC-8.1 states that the United States responded to an uncertain and unstable postwar world by asserting and working to maintain a position of global leadership. The anchor carries the description of the world AND the response, because a distractor exchanges each half in turn."),
 ("far-reaching and were both domestic and international",
  "KC-8.1 ends 'with far-reaching domestic and international consequences', which names both spheres and calls them far-reaching."),
 ("create a free-market global economy, and build an international security system",
  "KC-8.1.I names the three aims of the cold war engagement: limit the growth of Communist military power and ideological influence, create a free-market global economy, and build an international security system."),
 ("As the authoritarian Soviet Union",
  "KC-8.1.I calls it 'the authoritarian Soviet Union', so the framework does supply a characterization and that characterization is authoritarian."),
 ("power of the federal government, and acceptable means",
  "KC-8.1.II names both subjects of the public debates Cold War policies produced: the power of the federal government, and acceptable means for pursuing international and domestic goals while protecting civil liberties."),
 ("without sacrificing civil liberties",
  "KC-8.1.II's closing clause 'while protecting civil liberties' is what makes the debate about means rather than about goals alone, and the sentence calls the debates public and domestic as well as international."),
 ("New movements for civil rights, and liberal efforts to expand the role of government",
  "KC-8.2 names exactly this pair as generating a range of political and cultural responses; the distractor that reads reduction rather than expansion reverses the framework's own verb."),
 ("responses were uniform and ran in a single direction",
  "KC-8.2 says a RANGE of political and cultural responses, so a single uniform reaction is the reading the word excludes; the rejected options are things the sentence asserts."),
 ("some legal and political successes in ending segregation, although progress toward racial equality was slow",
  "KC-8.2.I is balanced between successes achieved and progress that was slow, and the anchor carries both halves because one distractor keeps the successes and drops the qualification."),
 ("Continuity with a preceding historical development",
  "The topic page names 'change from and/or continuity with preceding historical developments' as one of its two approaches to context, and KC-8.2.I's Reconstruction-era promises are a link backward in time rather than sideways to another region."),
 ("African American civil rights movement, and focused on identity",
  "KC-8.2.II gives both causes, social conditions AND the African American civil rights movement, and the three issues of identity, social justice, and the environment; the anchor spans the join because distractors cut one cause or replace the issues."),
 ("from the left as well as from a resurgent conservative movement",
  "KC-8.2.III makes the attack on liberalism two-sided with the phrase 'as well as', and both single-sided readings are offered as distractors, so the anchor carries both directions."),
 ("Economic and demographic changes, with consequences for American society, politics, and culture",
  "KC-8.3 names postwar economic and demographic changes as the cause and American society, politics, and culture as what bore the far-reaching consequences; the anchor carries both ends because distractors alter one or the other."),
 ("sense of optimism in the postwar years",
  "KC-8.3.I states that rapid economic and social changes in American society fostered a sense of optimism in the postwar years."),
 ("anxieties over the Cold War changed U.S. culture, and led to significant political and moral debates",
  "KC-8.3.II gives a compound cause, new demographic and social developments ALONG WITH anxieties over the Cold War, and a divisive outcome; the anchor spans cause and outcome because a distractor keeps the cause and reverses the outcome."),
 ("optimism and debates that sharply divided the nation both belong to the same period",
  "KC-8.3.I and KC-8.3.II are printed side by side in the same preview for the same period, so the framework asserts optimism and sharp division together rather than in sequence."),
 ("situated within a broader historical context",
  "Skill 4.B as printed beside this topic and cited by Unit 8 Learning Objective A; the distractors are skills 4.A, 5.B, 1.B and 3.C from other pages of this course, and 4.A is the near neighbour."),
 ("pursuing promises made in an earlier era; other societies were passing through postwar economic changes",
  "The topic page names preceding developments first and contemporaneous developments in different regions second; KC-8.2.I supplies the first. The anchor spans both halves in order because a distractor reverses them."),
 ("printed as a PREVIEW of the unit's key concepts",
  "The heading over this topic's Required Course Content reads PREVIEW: UNIT 8 KEY CONCEPTS, and the lettered sub-points of KC-8.1 through KC-8.3 are printed on the later topic pages of the same unit."),
 ("responded to an unstable postwar world by asserting a position of global leadership",
  "KC-8.1 is the unit's first key concept; the four rejected statements are KC-8.2, KC-8.3, KC-8.2.III and KC-8.3.I, which belong to the preview's other two key concepts."),
 ("New demographic and social developments changed U.S. culture",
  "KC-8.3.II sits under KC-8.3, the key concept about economic and demographic change, while the four rejected statements are KC-8.2.I, KC-8.2.II, KC-8.2.III and KC-8.2."),
 ("KC-8.1, on the American response to an uncertain and unstable postwar world",
  "KC-8.1 is the previewed sentence describing an uncertain and unstable postwar world and the American assertion of global leadership, which is the argument the hypothetical memorandum makes."),
 ("public debates over acceptable means for pursuing goals while protecting civil liberties",
  "KC-8.1.II is the previewed sentence about acceptable means for pursuing international and domestic goals while protecting civil liberties, which is the complaint the hypothetical letter makes."),
 ("rise at every reading, and the durable good spreads from fewer than one household in five",
  "Recomputed in q25 from the table alone, with each rejected reading falsified against the same rows. KC-8.3.I attributes a sense of optimism to rapid economic and social changes in American society."),
 ("reducing the power of the federal government",
  "Recomputed in q26: three rows record KC-8.2.II's own three issues of identity, social justice, and the environment, and one records something outside them. Reducing the role of government belongs to KC-8.2.III's resurgent conservative movement instead."),
 ("majority expressed optimism about their own future, and in every year a majority also expressed anxiety",
  "Recomputed in q27 from the table alone. KC-8.3.I records a sense of optimism and KC-8.3.II records anxieties over the Cold War, and the preview prints both for the same period rather than in sequence."),
 ("federal government withdrew from economic life",
  "Nothing in the Unit 8 preview says this, and KC-8.2 says the opposite by describing liberal efforts to EXPAND the role of government. The four rejected statements are KC-8.1.II, KC-8.2.II, KC-8.3.I and KC-8.2.III."),
 ("asserted global leadership in an unstable postwar world, new movements",
  "Collects KC-8.1, KC-8.2 and KC-8.3 in the order the preview prints them and adds nothing to any of the three."),
 ("parts of one context rather than as separate stories",
  "KC-8.1 gives the assertion of global leadership far-reaching DOMESTIC as well as international consequences, KC-8.1.II makes Cold War policies the source of debates at home, and KC-8.3.II names anxieties over the Cold War among the causes of cultural change."),
]


def _extra_mutations():
    def period_detail_creeps_in(mod, cl):
        mod.QUESTIONS[0]["why"] = mod.QUESTIONS[0]["why"] + " The war in Vietnam is one example."
        no_period_detail(mod)

    def issue_moves_inside(mod, cl):
        # q26 keys the one row OUTSIDE KC-8.2.II's three issues. Make that row
        # record one of the three and the keyed claim stops being true, which no
        # single-cell corruption of a value can express as cleanly.
        t = dict(mod.QUESTIONS[25]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][3][1] = "Identity"
        mod.QUESTIONS[25]["table"] = t

    def anxiety_falls_away(mod, cl):
        # q27 keys BOTH majorities holding in every year. Drop one anxiety
        # reading below half and the key fails while every value stays a legal
        # share, which a bounds check alone would not catch.
        t = dict(mod.QUESTIONS[26]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][3][2] = "41"
        mod.QUESTIONS[26]["table"] = t

    return [
        ("period detail in a contextualizing topic", period_detail_creeps_in),
        ("the fourth survey row moved inside KC-8.2.II's three issues, so q26 has no unique key",
         issue_moves_inside),
        ("one anxiety reading dropped below half, so q27's keyed majority fails",
         anxiety_falls_away),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    ws.controls(a8_1)
    for label, mutate in _extra_mutations():
        mod = wh_check._mutant(a8_1)
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

no_period_detail(a8_1)
wh_check.run(a8_1, CLAIMS, TABLE_CHECKS, sys.argv)
