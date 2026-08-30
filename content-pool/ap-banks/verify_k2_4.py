"""Key audit for AP COMPARATIVE GOVERNMENT 2.4 Executive Term Limits.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
  PAU-3.C.3    executive term limits have ADVANTAGES AND DISADVANTAGES with regard
               to promoting stability and effective policies
    .a  three advantages: they check executive power and inhibit the emergence of
        dictators and personality rule; help focus the officeholder on GOVERNING
        RATHER THAN WINNING ELECTIONS; provide opportunities for NEW LEADERS with
        new ideas, policies or goals
    .b  seven disadvantages: force good executives to leave office; allow
        insufficient time to achieve goals; impede policy continuity; weaken
        accountability; create a LAME-DUCK PERIOD; prevent the officeholder from
        building experience; can cause poorly designed policy

Sorting an item into the right half of that list is most of the topic, so items 2
to 13 work through the ten one at a time and then twice as a sorting exercise.
Suggested skill 5.A is Argumentation, which is why items 18, 19 and 28 ask what
evidence would support or weaken a claim rather than what the framework says.

THE ONLY TWO TERM-LIMIT FACTS THE FRAMEWORK PRINTS
--------------------------------------------------
PAU-3.C.2.b: Iran's president, up to two 4-year terms. PAU-3.C.2.c: Mexico's
president, restricted to one term. NOTHING for China, Nigeria, Russia or the
United Kingdom. Item 16 keys that absence.

China's 2018 removal of presidential term limits is the obvious thing to reach
for here and it is NOT course content: it appears only in an optional sample
instructional activity in Unit 2, never in an essential knowledge statement. No
item keys it; item 17 keys the fact about the framework instead
(AP_COMP_GOV_CED.md note 7).

'Weaken accountability' is listed with no explanation, so item 26 glosses it only
as far as DEM-2.B.2 licenses, where accountability rests on voters knowing whose
record is on the ballot at the next election. The rejected options there are
consequences the framework never attaches to a term limit.

DATA ITEMS
----------
Items 20-22 group hypothetical cases by term-limit RULE rather than by country,
because the framework attaches no such data to any country; the columns point in
opposite directions, so item 22 can make the data reproduce PAU-3.C.3's
two-sidedness. Items 23-25 track a single term year by year, where the lame-duck
disadvantage shows up as a monotone fall in passage and rise in defeat.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k2_4

YEARS = "Mean years the chief executive held office"
SCHED = "Share of executives who left office at a scheduled date (percent)"
REV = "Major reversals of existing policy per decade"
PASSED = "Executive-proposed bills passed"
DEFEATED = "Executive-proposed bills defeated"

TWO, ONE, NONE = ("Cases with a two-term limit", "Cases with a one-term limit",
                  "Cases with no term limit")


def _tl(table):
    return {lab: (cg.cell(table, lab, YEARS), cg.cell(table, lab, SCHED), cg.cell(table, lab, REV))
            for lab in cg.labels(table)}


def q20(table, item):
    v = _tl(table)
    assert v[NONE][0] == max(x[0] for x in v.values()), "the unlimited row must show the longest mean tenure"
    assert v[NONE][0] > 2 * max(v[TWO][0], v[ONE][0]), \
        "the key says 'more than twice as long', which must be true of both limited rows"
    assert v[NONE][1] == min(x[1] for x in v.values()), \
        "the unlimited row must least often leave at a scheduled date"
    assert v[ONE][0] == min(x[0] for x in v.values()), "the rejected shortest-tenure row must be the one-term row"
    assert v[ONE][1] == max(x[1] for x in v.values()), \
        "the rejected 'most often scheduled' option must name a row that is true of, but is the wrong row for this claim"
    return "the unlimited row runs 14.6 years against 7.2 and 5.0 and leaves at a scheduled date least often, at 61 percent"


def q21(table, item):
    v = _tl(table)
    assert v[ONE][2] == max(x[2] for x in v.values()), "the one-term row must record the most policy reversals"
    assert v[NONE][2] == min(x[2] for x in v.values()), "the unlimited row must record the fewest"
    assert v[ONE][0] == min(x[0] for x in v.values()), \
        "the row with the most reversals should also be the one whose executives turn over fastest"
    return "the one-term row records 4.4 reversals per decade against 1.8 where no limit applies, and also the shortest tenures"


def q22(table, item):
    v = _tl(table)
    limited = [TWO, ONE]
    assert all(v[lab][1] > v[NONE][1] for lab in limited), \
        "the limited rows must lead on scheduled departures, which is the advantage half"
    assert all(v[lab][2] > v[NONE][2] for lab in limited), \
        "the limited rows must also record more policy reversals, which is the disadvantage half"
    assert not all(v[NONE][i] >= max(x[i] for x in v.values()) for i in (0, 1, 2)), \
        "'the unlimited group leads on every measure' must be false"
    return "the limited rows lead on scheduled departures and also on policy reversals, so the table carries both halves of the framework's claim"


def _lame(table):
    return [(cg.cell(table, lab, PASSED), cg.cell(table, lab, DEFEATED)) for lab in cg.labels(table)]


def q23(table, item):
    rows = _lame(table)
    passed = [p for p, _ in rows]
    defeated = [d for _, d in rows]
    assert passed == sorted(passed, reverse=True) and len(set(passed)) == len(passed), \
        f"passage must fall at every step; got {passed}"
    assert defeated == sorted(defeated) and len(set(defeated)) == len(defeated), \
        f"defeat must rise at every step; got {defeated}"
    assert passed[0] > defeated[0] and passed[-1] < defeated[-1], \
        "the two series must cross, so the final year looks nothing like the first"
    return f"passage runs {passed} and defeat runs {defeated}, falling and rising at every step and crossing before the end"


def q24(table, item):
    rows = _lame(table)
    total = sum(p + d for p, d in rows)
    assert total == 95, f"the keyed total recomputes to {total}"
    assert sum(p for p, _ in rows) == 61 and sum(d for _, d in rows) == 34, \
        "the 61 and 34 distractors must be the two single-column totals"
    assert rows[-1][0] + rows[-1][1] == 23, "the 23 distractor must be a single year's total"
    assert (rows[0][0] + rows[0][1]) + (rows[-1][0] + rows[-1][1]) == 48, \
        "the 48 distractor must be the first and last years' totals only"
    return f"the two columns total {total:.0f} bills proposed, and each distractor is a partial or single-column sum"


def q25(table, item):
    rows = _lame(table)
    p, d = rows[-1]
    pct = p / (p + d) * 100
    assert abs(pct - 26) < 1.0, f"the final year's passage share is {pct:.1f} percent"
    assert abs(d / (p + d) * 100 - 74) < 1.0, "the 74 distractor must be the complementary defeat share"
    p0, d0 = rows[0]
    assert abs(p0 / (p0 + d0) * 100 - 88) < 1.0, "the 88 distractor must be the first year's passage share"
    p2, d2 = rows[2]
    assert abs(p2 / (p2 + d2) * 100 - 61) < 1.0 and abs(d2 / (p2 + d2) * 100 - 39) < 1.0, \
        "the 61 and 39 distractors must be the third year's passage and defeat shares"
    return f"the final year passes {p:.0f} of {p + d:.0f}, or {pct:.1f} percent, and every distractor is a real share from the wrong cell"


CLAIMS = [
 ("advantages and disadvantages",
  "EK PAU-3.C.3 states that executive term limits have advantages and disadvantages with regard to promoting stability and effective policies in a country, and then lists three of the first and seven of the second. A one-sided reading contradicts the statement in either direction."),
 ("inhibit the emergence of dictators",
  "EK PAU-3.C.3.a lists checking executive power and inhibiting the emergence of dictators and personality rule among the advantages. Every rejected option is drawn from EK PAU-3.C.3.b, the disadvantages half of the same statement."),
 ("governing rather than winning elections",
  "EK PAU-3.C.3.a states that term limits help to focus the officeholder on governing rather than winning elections. An executive who cannot stand again has no re-election campaign to run, which is the framework's reason for counting this an advantage."),
 ("opportunities for new leaders",
  "EK PAU-3.C.3.a lists providing opportunities for new leaders with new ideas, policies or goals among the advantages. The framework says nothing under this heading about the successor's party, prior office or method of selection."),
 ("force good executives to leave office",
  "EK PAU-3.C.3.b lists forcing good executives to leave office among the disadvantages. Every rejected option is drawn from EK PAU-3.C.3.a, the advantages half of the same statement."),
 ("insufficient time",
  "EK PAU-3.C.3.b lists allowing insufficient time for an officeholder to achieve goals among the disadvantages. The complaint concerns the length of the available tenure, not the parliamentary or electoral calendar."),
 ("impede policy continuity",
  "EK PAU-3.C.3.b lists impeding policy continuity among the disadvantages. A guaranteed change of officeholder means a guaranteed opportunity for a change of direction, which EK PAU-3.C.3.a counts as an advantage when it speaks of new leaders with new ideas."),
 ("weaken accountability",
  "EK PAU-3.C.3.b lists weakening accountability among the disadvantages, and EK DEM-2.B.2 grounds accountability in voters knowing whose record is on the ballot at the next election. An officeholder who cannot stand again is not on that ballot."),
 ("a successor is already certain",
  "EK PAU-3.C.3.b lists creating a lame-duck period for the officeholder among the disadvantages. The period arises because the departure is scheduled rather than contingent, which none of the rejected events is."),
 ("building experience as chief executive",
  "EK PAU-3.C.3.b lists preventing the officeholder from building experience as chief executive among the disadvantages. The framework attaches no restriction on appointments, diplomacy, budgets or addresses to a term limit."),
 ("poorly designed policy",
  "EK PAU-3.C.3.b lists causing poorly designed policy among the disadvantages, alongside insufficient time to achieve goals and the loss of accumulated experience. The rejected options concern institutions the framework never connects to term limits."),
 ("checking executive power and inhibiting personality rule",
  "EK PAU-3.C.3.a lists checking executive power and inhibiting the emergence of dictators and personality rule among the advantages, while EK PAU-3.C.3.b lists forcing good executives out and impeding policy continuity among the disadvantages. The four offered items come two from each half."),
 ("lame-duck period and weakening accountability",
  "EK PAU-3.C.3.b lists creating a lame-duck period and weakening accountability among the disadvantages, while EK PAU-3.C.3.a lists opportunities for new leaders and the focus on governing rather than winning elections among the advantages."),
 ("Mexico",
  "EK PAU-3.C.2.c states that Mexico's president is restricted to one term, in the same sentence describing the office as head of state and head of government, commander in chief and leader of the bureaucracy. It is one of only two term-limit figures the framework prints."),
 ("up to two four-year terms",
  "EK PAU-3.C.2.b states that Iran's president is elected for up to two 4-year terms, oversees the civil service and conducts foreign policy. This and Mexico's one-term restriction are the framework's only term-limit figures."),
 ("China, Nigeria, Russia and the United Kingdom",
  "EK PAU-3.C.2.b and EK PAU-3.C.2.c give figures for Iran and Mexico, and no essential knowledge statement gives one for the remaining four. Asserting a limit for any of those four would go beyond the framework."),
 ("optional sample instructional activity",
  "The 2018 removal of presidential term limits appears in the Unit 2 sample instructional activities and in no essential knowledge statement, and EK PAU-3.C.2.a describes that country's executive without stating any term limit. The essential knowledge statements are what the course content is."),
 ("leave office at scheduled dates",
  "EK PAU-3.C.3 frames the question in terms of promoting stability and effective policies, and EK PAU-3.C.3.a attributes to term limits a check on executive power and the inhibition of dictators and personality rule. A scheduled, predictable departure is what those advantages amount to in observable terms."),
 ("Long-term programmes are abandoned",
  "EK PAU-3.C.3.b lists impeding policy continuity, insufficient time to achieve goals and poorly designed policy among the disadvantages, and repeated abandonment and reversal of programmes is the observable form those take. The rejected findings bear on none of the seven."),
 ("more than twice as long",
  "EK PAU-3.C.3.a attributes to term limits a check on executive power and the inhibition of personality rule, so the supporting evidence is the contrast case. Recomputed in q20 above: where no limit applies, tenures run more than twice as long and scheduled departures are least common."),
 ("most reversals of existing policy",
  "EK PAU-3.C.3.b lists impeding policy continuity among the disadvantages. Recomputed in q21 above: the row whose executives turn over fastest records the most reversals, and the row with no limit records the fewest."),
 ("while also recording more policy reversals",
  "EK PAU-3.C.3 states that term limits have advantages AND disadvantages for stability and effective policies. Recomputed in q22 above: the limited rows lead on scheduled departures and also on policy reversals, so the data reproduce the two-sidedness rather than settling it."),
 ("illustrates the lame-duck period",
  "EK PAU-3.C.3.b lists creating a lame-duck period for the officeholder among the disadvantages. Recomputed in q23 above: passage falls at every step and defeat rises at every step, and the two series cross before the term ends."),
 ("95",
  "Recomputed in q24 above: every proposed bill was either passed or defeated, so the total is the sum of both columns across all four years. Each distractor is a single-column total, one year's total, or the first and last years only."),
 ("26 percent",
  "Recomputed in q25 above by dividing the final year's passed bills by that year's total. Each alternative is a real share taken from the wrong cell or the wrong year, which is why the item cannot be answered by recognizing a familiar number."),
 ("no further election at which to judge that record",
  "EK PAU-3.C.3.b lists weakening accountability without explaining the mechanism, and EK DEM-2.B.2 grounds accountability in voters knowing whose record is on the ballot at the next election. Immunity from law, loss of legislative initiative, forced impeachment and freedom from the courts are consequences the framework never attaches to a term limit."),
 ("also interrupts policy and denies an officeholder time and experience",
  "EK PAU-3.C.3.a and EK PAU-3.C.3.b describe the same institutional feature -- a scheduled, unavoidable change of officeholder -- from opposite sides. The framework presents the trade-off rather than recommending a rule, and attaches term-limit figures to only two of the six course countries."),
 ("continued to direct policy from outside the office",
  "EK PAU-3.C.3.a claims that term limits check executive power and inhibit the emergence of dictators and personality rule, so the weakening finding is one showing personal rule surviving the departure from office. Scheduled departures, legislative success, turnout and reshuffles are all consistent with the claim."),
 ("lame-duck period created for the officeholder",
  "EK PAU-3.C.3.b lists creating a lame-duck period among the disadvantages, and the scenario describes the loss of leverage that arises when a departure is scheduled. The other listed disadvantages concern who leaves, what the officeholder accumulates, the quality of policy and the time available."),
 ("three named advantages and seven named disadvantages",
  "EK PAU-3.C.3 opens with advantages and disadvantages regarding stability and effective policies, EK PAU-3.C.3.a lists three of the first and EK PAU-3.C.3.b seven of the second, and EK PAU-3.C.2.b and EK PAU-3.C.2.c are the only statements attaching a figure to a country."),
]

cg.check(k2_4, CLAIMS, table_checks={20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25})
