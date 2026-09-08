"""Key audit for AP U.S. HISTORY 8.3 The Red Scare.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states the CED sentence the key rests on, with its Key Concept code, for a human
to audit. ``wh_check`` refuses a ``why`` or a ``claim`` that cites neither a KC
code nor a Learning Objective.

THE UNUSUAL THING ABOUT THIS TOPIC: it prints exactly ONE sentence of historical
development, KC-8.1.II.A, and thirty questions have to come out of it without
inventing content. Two further framework sentences are therefore used, and the
module header says exactly where they come from and why:

  KC-8.1.II.A  Americans debated policies and methods designed to expose
               suspected communists within the United States even as both
               parties supported the broader strategy of containing communism.
  KC-8.1.II    the PARENT of that sentence, printed in the Unit 8 preview at
               topic 8.1. It is what makes this a topic about CAUSES: Cold War
               policies led to public debates over the power of the federal
               government and acceptable means for pursuing international and
               domestic goals while protecting civil liberties.
  KC-8.1.I     cited only where an item needs the contrast KC-8.1.II.A itself
               draws between measures at home and the broader strategy abroad.

  The THEMATIC FOCUS statement for American and National Identity is also
  printed inside this topic's Required Course Content, and item 10 keys it.

WHAT IS DELIBERATELY NOT KEYED, and this is the point of the topic. The Red
Scare invites both strong general knowledge and live political disagreement. The
framework's sentence is careful -- it records that Americans DEBATED the methods
and that BOTH parties supported containment -- so no key here rules on whether
any method was justified, names a senator, a committee, a hearing or a case, or
assigns a position to a party. Keying one side of a disagreement the CED reports
as a disagreement is exactly the guess HISTORY_BRIEF.md forbids.

THE SWAP ITEMS, where a distractor exchanges the halves of the key and the
anchor therefore carries both clauses:
  q8   disagreement first, agreement second -- the reverse is a distractor
  q13  the audience is the department's own employees, NOT the public
  q17  one share steady while the other rises -- the distractor moves both
  q27  a later account reports the later understanding, not a better one

DATA ITEMS: 15, 16 and 17. Every table check runs its DERIVED assertions -- the
ones carrying the keyed claim -- before the literal guard on the rows it was
written against, so a corruption that breaks the key raises on the assertion
naming it. ``_T_POSITIONS`` is categorical, and without the literal guard the
shared corrupter (which appends text) would catch none of its cells.

NEGATIVE CONTROLS: ``python3 verify_a8_3.py --selftest``, which besides the
shared battery runs three targeted controls and checks WHICH assertion raised.
"""
import sys

import wh_check
import wh_stimulus as ws
import a8_3

SPEAKER = "Speaker in a hypothetical set of statements"
ABROAD = "Position recorded on containing communism abroad"
HOME = "Position recorded on a proposed method of exposing suspected communists at home"
YEAR_C = "Year (hypothetical record)"
REVIEWED = "Cases reviewed"
CLOSED = "Cases closed with no finding against the person reviewed"
SUPPORT = "Recorded statements supporting containment abroad (percent)"
CRITICISM = "Recorded statements criticising a domestic exposure method (percent)"


def _col(table, header):
    idx = table["headers"].index(header)
    return [row[idx] for row in table["rows"]]


def _nums(table, header):
    return [float(v.replace(",", "")) for v in _col(table, header)]


_EXPECTED_POSITIONS = [
    ["Speaker 1", "Supports", "Supports"],
    ["Speaker 2", "Supports", "Opposes"],
    ["Speaker 3", "Supports", "Supports only with limits"],
    ["Speaker 4", "Supports", "Opposes"],
]


def q15(table, item):
    abroad = [v.strip() for v in _col(table, ABROAD)]
    home = [v.strip() for v in _col(table, HOME)]
    assert len(set(abroad)) == 1 and abroad[0] == "Supports", (
        f"the key needs every speaker recorded as supporting containment abroad, so "
        f"'the speakers divide over containment abroad' is false; got {abroad}"
    )
    assert len(set(home)) > 1, (
        f"'all four take the same recorded position on the method at home' must be false; "
        f"got {home}"
    )
    opposed = [i for i, v in enumerate(home) if v.lower().startswith("opposes")]
    assert opposed, "the record must contain at least one speaker opposing the method at home"
    assert all(abroad[i] == "Supports" for i in opposed), (
        f"'every speaker opposing the method at home also opposes containment' must be false; "
        f"rows {opposed} oppose the method and support containment"
    )
    assert any(v.lower().startswith("supports") for v in home), (
        f"'no speaker supports the method at home' must be false; got {home}"
    )
    assert [list(r) for r in table["rows"]] == _EXPECTED_POSITIONS, (
        f"the speaker table does not hold the rows this check was written against; "
        f"got {table['rows']}"
    )
    return (f"all four speakers record {abroad[0]!r} on containment abroad while recording "
            f"{len(set(home))} distinct positions on the method at home: {home}")


_EXPECTED_CASES = [
    ["1947", "120", "96"],
    ["1950", "260", "205"],
    ["1953", "310", "250"],
    ["1956", "180", "150"],
]


def q16(table, item):
    years = _nums(table, YEAR_C)
    reviewed = _nums(table, REVIEWED)
    closed = _nums(table, CLOSED)
    steps = [b - a for a, b in zip(years, years[1:])]
    assert steps == [3, 3, 3], f"the record must run at three-year steps; the steps are {steps}"
    assert all(c <= r for r, c in zip(reviewed, closed)), (
        f"'the number closed with no finding exceeds the number reviewed' must be false; "
        f"reviewed {reviewed} against closed {closed}"
    )
    peak = reviewed.index(max(reviewed))
    assert 0 < peak < len(reviewed) - 1, (
        f"the key says the series rises to a peak and then falls, so the largest value cannot "
        f"be at either end; the peak is at position {peak} of {reviewed}"
    )
    assert all(b > a for a, b in zip(reviewed[:peak + 1], reviewed[1:peak + 1])), (
        f"the series must rise up to its peak; got {reviewed}"
    )
    assert all(b < a for a, b in zip(reviewed[peak:], reviewed[peak + 1:])), (
        f"the series must fall after its peak, so 'reviewed rise in every year' is false; "
        f"got {reviewed}"
    )
    ratios = [c / r for r, c in zip(reviewed, closed)]
    assert all(x > 0.75 for x in ratios), (
        f"the key says more than three quarters closed with no finding in every year, and "
        f"'fewer than half' must be false; the ratios are {[round(x, 3) for x in ratios]}"
    )
    assert [list(r) for r in table["rows"]] == _EXPECTED_CASES, (
        f"the case table does not hold the rows this check was written against; "
        f"got {table['rows']}"
    )
    return (f"cases reviewed run {reviewed}, peaking in the third year recorded, with "
            f"{[round(x, 3) for x in ratios]} of each year's cases closing without a finding")


_EXPECTED_STATEMENTS = [
    ["1947", "91", "12"],
    ["1950", "93", "28"],
    ["1953", "90", "41"],
    ["1956", "92", "55"],
]


def q17(table, item):
    support = _nums(table, SUPPORT)
    criticism = _nums(table, CRITICISM)
    assert all(0 <= v <= 100 for v in support + criticism), (
        f"a percentage cannot lie outside 0 to 100; got {support} and {criticism}"
    )
    # BOTH clauses of the key, because a distractor moves the first column too.
    assert max(support) - min(support) <= 5, (
        f"the key says support holds near the same level; its spread is "
        f"{max(support) - min(support)}"
    )
    assert min(support) > 50, (
        f"'support is recorded below half in at least one year' must be false; got {support}"
    )
    assert all(b > a for a, b in zip(criticism, criticism[1:])), (
        f"the key says criticism rises in every year, so 'criticism falls at least once' is "
        f"false; got {criticism}"
    )
    assert criticism[-1] > 4 * criticism[0], (
        f"the key contrasts a steady column with a moving one, so the rise must be substantial; "
        f"criticism runs from {criticism[0]} to {criticism[-1]}"
    )
    assert [list(r) for r in table["rows"]] == _EXPECTED_STATEMENTS, (
        f"the statement table does not hold the rows this check was written against; "
        f"got {table['rows']}"
    )
    return (f"support runs {support}, a spread of {max(support) - min(support)} points, while "
            f"criticism runs {criticism}, rising at every step to more than four times its start")


TABLE_CHECKS = {15: q15, 16: q16, 17: q17}

CLAIMS = [
 ("causes and effects of the Red Scare after World War II",
  "Unit 8 Learning Objective C reads 'Explain the causes and effects of the Red Scare after World War II'; the distractors are Learning Objectives B, Q and D and a restatement of the suggested skill."),
 ("Policies and methods designed to expose suspected communists within the United States",
  "KC-8.1.II.A states exactly what was debated: policies and methods designed to expose suspected communists within the United States."),
 ("broader strategy of containing communism",
  "KC-8.1.II.A ends 'even as both parties supported the broader strategy of containing communism', which is the point of agreement rather than the point of dispute."),
 ("ran at the same time as agreement on the broader strategy",
  "KC-8.1.II.A joins its halves with 'even as', which marks simultaneity together with contrast rather than a sequence in either direction."),
 ("matter of suspicion rather than of established fact",
  "KC-8.1.II.A describes measures designed to expose SUSPECTED communists, which names whom the measures targeted without asserting what was found about them."),
 ("Within the United States",
  "KC-8.1.II.A places the exposure measures 'within the United States', which is the contrast it then draws with the broader strategy of containing communism abroad."),
 ("arose from Cold War policies rather than independently of them",
  "KC-8.1.II states that Cold War policies LED TO public debates over the power of the federal government and acceptable means for pursuing international and domestic goals; KC-8.1.II.A is the domestic case of those debates, and the direction runs from policy to debate."),
 ("first half records a disagreement among Americans, and the second records a point on which both parties agreed",
  "KC-8.1.II.A opens with Americans debating domestic exposure measures and closes with both parties supporting containment, in that order. The anchor carries both halves because a distractor exchanges them."),
 ("differed with each other over whether communism should be contained",
  "KC-8.1.II.A says the opposite: both parties supported the broader strategy of containing communism, so containment is not what divided them. The four rejected statements restate parts of the same sentence."),
 ("democracy, freedom, citizenship, diversity, and individualism",
  "The thematic focus statement for American and National Identity, printed inside this topic's Required Course Content, names these as what shapes American national identity and cultural values; KC-8.1.II.A's debate over acceptable means at home is a debate of that kind."),
 ("Explain the point of view, purpose, historical situation, or audience of a source",
  "Skill 2.B as printed beside this topic and practised in meeting Unit 8 Learning Objective C; skill 2.C, the near-neighbour distractor, adds the further step of explaining how those features limit a source's use."),
 ("interested party arguing from the position of employers who would apply the checks",
  "KC-8.1.II.A records Americans debating the policies and methods of domestic exposure, and skill 2.B asks a student to name the position a source argues from; the authors here are one side of that debate."),
 ("department's own employees, so it shows what the government was asking of people it employed",
  "Skill 2.B asks for a source's audience, and KC-8.1.II.A places the debated policies and methods within the United States. The anchor carries the audience AND what follows from it, because a distractor keeps the second half and changes the audience to the public."),
 ("persuade lawmakers to change a procedure",
  "KC-8.1.II.A records that Americans debated the policies and methods designed to expose suspected communists, and skill 2.B asks for purpose; a petition to a legislature is an argument for a position rather than a record or an announcement."),
 ("supporting containment abroad while dividing over the method proposed at home",
  "Recomputed in q15 from the table alone, with every rejected reading falsified against the same rows. KC-8.1.II.A pairs agreement on the broader strategy with debate over the methods used at home."),
 ("rise to a peak and then fall, and in every year recorded more than three quarters",
  "Recomputed in q16 from the table alone. KC-8.1.II.A's word SUSPECTED names whom the measures targeted without asserting what was found, so a record in which most reviews close without a finding is consistent with the sentence."),
 ("holds near the same high level in every year recorded, while criticism of the domestic method rises",
  "Recomputed in q17. KC-8.1.II.A pairs continuing support for containment with debate over domestic methods; the anchor carries both columns because a distractor moves the first one as well."),
 ("relation KC-8.1.II draws between Cold War policies and public debates over acceptable means",
  "KC-8.1.II states that Cold War policies led to public debates over the power of the federal government and acceptable means for pursuing international and domestic goals while protecting civil liberties, which is the step from danger abroad to measures at home."),
 ("inside the procedure while it was being applied",
  "Skill 2.B asks for a source's historical situation, and KC-8.1.II.A records that Americans debated the methods designed to expose suspected communists; a private record kept by someone administering such a method is one trace of that debate."),
 ("several different kinds of organisation across the country",
  "KC-8.1.II.A attributes the debate to Americans generally rather than to one body, so evidence that it reached beyond a single institution has to be drawn from more than one place."),
 ("Cold War policies led to public debates over acceptable means",
  "KC-8.1.II supplies a cause lying outside the motives of individuals, which is what an argument from personal ambition alone omits, and Unit 8 Learning Objective C asks for causes."),
 ("power of the federal government and over acceptable means for pursuing domestic goals",
  "KC-8.1.II names these debates as what Cold War policies led to, and KC-8.1.II.A is their domestic instance; containment was supported by both parties rather than abandoned."),
 ("general reading public, whom it asks to act",
  "Skill 2.B asks for audience, and an advertisement placed in a newspaper addresses its readers; KC-8.1.II.A places the debated methods within the United States, and an appeal for ordinary people to take part is one such method."),
 ("agreement on the broader strategy that KC-8.1.II.A says accompanied the domestic disagreement",
  "KC-8.1.II.A records Americans debating domestic exposure measures even as both parties supported the broader strategy of containing communism, so a shared premise beneath opposed conclusions is exactly the sentence's shape."),
 ("rules out party disagreement over containment as the source of the dispute",
  "KC-8.1.II.A says both parties supported the broader strategy of containing communism, which removes the partisan explanation and leaves the domestic policies and methods as what was contested; Unit 8 Learning Objective C asks for causes."),
 ("method designed to expose suspected communists within the United States",
  "KC-8.1.II.A describes exactly such policies and methods; the rejected options belong to KC-8.1.I's account of aims pursued abroad, which is the contrast KC-8.1.II.A draws."),
 ("reports how the period was understood later rather than how it appeared at the time",
  "Skill 2.B asks for historical situation, and a retrospective account is situated at its moment of writing; KC-8.1.II.A records a debate that was live at the time, so a later verdict of settlement is evidence about the later moment. The anchor carries both halves because a distractor keeps the date and claims superior accuracy."),
 ("arose alongside a strategy of containing communism abroad that both parties supported",
  "KC-8.1.II.A places the domestic measures alongside both parties' support for the broader strategy, and KC-8.1.II makes Cold War policies the source of such debates; neither sentence has one development displacing the other."),
 ("attributes the debate to Americans generally",
  "KC-8.1.II.A says AMERICANS debated the policies and methods, and names both parties only for the point on which they agreed, so a study confined to national politicians samples a fraction of the subject."),
 ("domestic argument about acceptable means, arising from Cold War policy and coexisting with agreement on containment",
  "KC-8.1.II.A supplies the domestic argument and the agreement, KC-8.1.II supplies the cause, and Unit 8 Learning Objective C asks for both causes and effects; each rejected option contradicts one of the two sentences."),
]


def _targeted_controls():
    """Each must raise on the DERIVED guard it names, not on the literal backstop."""
    def speaker_splits_on_containment(mod, cl):
        t = dict(mod.QUESTIONS[14]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][1][1] = "Opposes"
        mod.QUESTIONS[14]["table"] = t

    def peak_moves_to_the_end(mod, cl):
        t = dict(mod.QUESTIONS[15]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][3][1] = "400"
        mod.QUESTIONS[15]["table"] = t

    def support_stops_holding(mod, cl):
        t = dict(mod.QUESTIONS[16]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][3][1] = "62"
        mod.QUESTIONS[16]["table"] = t

    return [
        ("one speaker made to oppose containment abroad, so q15's keyed agreement fails",
         speaker_splits_on_containment, "supporting containment abroad"),
        ("the case series made to peak at its last reading, so q16's rise-and-fall fails",
         peak_moves_to_the_end, "cannot be at either end"),
        ("support for containment made to slide, so q17's keyed steadiness fails",
         support_stops_holding, "holds near the same level"),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    ws.controls(a8_3)
    import cg_check as cg
    for label, mutate, expect in _targeted_controls():
        mod = wh_check._mutant(a8_3)
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

wh_check.run(a8_3, CLAIMS, TABLE_CHECKS, sys.argv)
