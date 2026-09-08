"""Key audit for AP U.S. HISTORY 7.4 The Progressives.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The gate is
``wh_check.run``: a KC code or Learning Objective in every ``why`` and every
``claim``, no figure language, no typeset markup, the marked-stimulus rule, and
the structural checks of ``cg_check``.

WHAT THE KEYS REST ON
---------------------
  Unit 7 Learning Objective D, goals and
    effects of the Progressive movement      items 1, 14, 16, 22, 23, 30
  Unit 7 Learning Objective E, attitudes to
    natural resources from 1890 to 1945      2, 19, 20, 23
  KC-7.1.II, the era's general statement     3
  KC-7.1.II.A, journalists and reformers     4, 5, 6, 7, 14, 21, 25, 26, 30
  KC-7.1.II.B, the national level            13, 14, 15, 16, 21, 29, 30
  KC-7.1.II.C, preservationists and
    conservationists                         17, 18, 19, 24, 30
  KC-7.1.II.D, divided over many issues      8, 9, 10, 11, 12, 27, 28, 30
  the two thematic focuses on the pages      24
  the boundary with KC-7.1.III               29

TWO PLACES WHERE A NEAR MISS WOULD BE A WRONG KEY, and where the anchors
therefore carry both clauses:

1. KC-7.1.II.D says some Progressives SUPPORTED Southern segregation "while
   others IGNORED its presence". It does not record any Progressive opposing
   it. Item 9's first distractor is the plausible, wrong version -- supported
   against campaigned against -- so its anchor carries the ignoring clause too,
   and item 12 keys the absence directly. Nothing in this module asserts an
   opposition the framework does not state.

2. KC-7.1.II.B says Progressives sought legislation "that THEY BELIEVED WOULD
   effectively regulate the economy". That is a report of an expectation, not a
   finding about an outcome, and item 16 keys the difference. Unit 7 Learning
   Objective D asks for goals AND effects precisely because they are not the
   same thing.

The other swap items are 10 (participation against experts), 21 (the two
scales, KC-7.1.II.A against KC-7.1.II.B) and 24 (the two thematic focuses),
each with an anchor carrying both halves.

WHAT IS NOT KEYED: no named Progressive, journalist, reformer, statute,
amendment number, park, agency or court case. The CED names none of those on
this page, and what it prints under OPTIONAL SOURCES is, in its own words, not
required course content.

DATA ITEMS: 27 and 28. The group table is CATEGORICAL, so its labels are
compared literally and every position cell is refused unless it holds exactly
Favours or Opposes -- the shared corrupter APPENDS, and a check written as
``cell == "Favours"`` would read "Favours CORRUPTED" as an Opposes without
objecting. The convention table carries an invariant instead: every row's two
figures sum to the same total, so no single number in it can be altered without
the row ceasing to add up.

NEGATIVE CONTROLS: ``python3 verify_a7_4.py --selftest``.
"""
import re
import sys

import wh_check
import wh_stimulus
import a7_4

GROUP = "Hypothetical group of Progressives (illustrative)"
PARTICIPATION = "Position on expanding popular participation in government"
EXPERTS = "Position on greater reliance on professional and technical experts"
RESTRICTION = "Position on restricting immigration"
PROPOSAL = "Proposal put to a hypothetical reform convention"
FOR = "Delegates recorded in favour"
AGAINST = "Delegates recorded against"

_GROUP_LABELS = ["Group 1", "Group 2", "Group 3", "Group 4"]
_PROPOSAL_LABELS = ["Proposal 1", "Proposal 2", "Proposal 3"]
_ISSUES = [PARTICIPATION, EXPERTS, RESTRICTION]


def _col(table, header):
    idx = table["headers"].index(header)
    return [row[idx] for row in table["rows"]]


def _positions(table, header):
    """One Favours/Opposes column, checked for form before it is read.

    ``cell == "Favours"`` would silently read the corrupter's "Favours
    CORRUPTED" as an Opposes, so a corrupted cell could change the answer
    without the check objecting. Refusing anything that is not exactly Favours
    or Opposes is what makes each of these cells load-bearing.
    """
    vals = _col(table, header)
    for v in vals:
        assert v in ("Favours", "Opposes"), (
            f"{header!r} holds {v!r}, which is neither Favours nor Opposes"
        )
    return vals


def q27(table, item):
    assert _col(table, GROUP) == _GROUP_LABELS, (
        f"the group table must be labelled {_GROUP_LABELS}; got {_col(table, GROUP)}"
    )
    split = []
    for issue in _ISSUES:
        vals = _positions(table, issue)
        if len(set(vals)) > 1:
            split.append(issue)
    assert len(split) == len(_ISSUES), (
        f"every issue recorded must find the groups on both sides for the key to hold; only "
        f"{len(split)} of {len(_ISSUES)} do"
    )
    # The four distractors, falsified against the same rows.
    assert len(split) > 1, "'the groups differ on one issue only' must be false"
    assert "Opposes" in _positions(table, PARTICIPATION), \
        "'every group favours expanding popular participation' must be false"
    assert "Favours" in _positions(table, RESTRICTION), \
        "'no group favours restricting immigration' must be false"
    return (f"all {len(_ISSUES)} issue columns carry both a Favours and an Opposes across the "
            f"{len(_GROUP_LABELS)} groups, so no issue finds them united")


def q28(table, item):
    assert _col(table, PROPOSAL) == _PROPOSAL_LABELS, (
        f"the convention table must be labelled {_PROPOSAL_LABELS}; got "
        f"{_col(table, PROPOSAL)}"
    )
    pro = [float(v) for v in _col(table, FOR)]
    con = [float(v) for v in _col(table, AGAINST)]
    # THE INVARIANT. Every proposal goes to the same body, so every row's two
    # figures must sum to the same total; no single number can then be altered
    # without the row ceasing to add up.
    totals = [a + b for a, b in zip(pro, con)]
    assert len(set(totals)) == 1, (
        f"every proposal is put to the same convention, so the rows must share a total; got "
        f"{totals}"
    )
    assert totals[0] > 0, "the convention must have delegates in it"
    assert min(pro + con) > 0, "'no proposal drew any recorded opposition' must be false"
    divided = [i for i, (a, b) in enumerate(zip(pro, con), 1) if a > 0 and b > 0]
    assert len(divided) == len(pro), "'the delegates divided on one proposal only' must be false"
    failed = [i for i, (a, b) in enumerate(zip(pro, con), 1) if b > a]
    assert failed, "'every proposal was carried by the delegates' must be false"
    assert len(set(pro)) == len(pro), \
        f"'every proposal drew exactly the same division' must be false; got {pro}"
    return (f"every row sums to {totals[0]:g}, all {len(divided)} proposals draw delegates on "
            f"both sides in different proportions, and proposal(s) {failed} draw more against "
            f"than for")


TABLE_CHECKS = {27: q27, 28: q28}

CLAIMS = [
 ("Compare the goals and effects of the Progressive reform movement",
  "Unit 7 Learning Objective D reads, verbatim, compare the goals and effects of the Progressive reform movement, and KC-7.1.II.A, KC-7.1.II.B and KC-7.1.II.D are printed under it."),
 ("attitudes toward the use of natural resources from 1890 to 1945",
  "Unit 7 Learning Objective E reads, verbatim, compare attitudes toward the use of natural resources from 1890 to 1945, with KC-7.1.II.C printed under it on this topic's second page."),
 ("calling for greater government action",
  "KC-7.1.II states that Progressives responded to political corruption, economic instability, and social concerns by calling for greater government action and other political and social measures."),
 ("political corruption, social injustice, and economic inequality",
  "KC-7.1.II.A states that some Progressive Era journalists attacked what they saw as political corruption, social injustice, and economic inequality."),
 ("middle and upper classes, and as including many women",
  "KC-7.1.II.A describes reformers as often from the middle and upper classes and including many women."),
 ("In cities and among immigrant populations",
  "KC-7.1.II.A states that reformers worked to effect social changes in cities and among immigrant populations, which KC-7.1.II.B's national level is set against."),
 ("reformers working to effect social changes",
  "KC-7.1.II.A pairs journalists attacking what they saw as wrongs with reformers working to effect social changes in cities and among immigrant populations, in a single sentence."),
 ("divided over many issues",
  "KC-7.1.II.D opens with the words the Progressives were divided over many issues, and then names three of them."),
 ("supported it, while others ignored its presence",
  "KC-7.1.II.D states that some Progressives supported Southern segregation, while others ignored its presence. The anchor carries both clauses because the plausible wrong version substitutes campaigning against it for ignoring it, and the framework records no such campaign."),
 ("expanding popular participation and relying more on professional and technical experts",
  "KC-7.1.II.D states that some Progressives advocated expanding popular participation in government while others called for greater reliance on professional and technical experts to make government more efficient; the anchor carries both sides of that division."),
 ("Immigration restriction",
  "KC-7.1.II.D ends by stating that Progressives also disagreed about immigration restriction, whereas KC-7.1.II.C has both resource groups supporting the establishment of national parks."),
 ("supporting segregation and ignoring its presence",
  "KC-7.1.II.D records exactly two Progressive positions on Southern segregation, supporting it and ignoring its presence, so working against it is not a claim the framework makes."),
 ("Effectively regulate the economy, expand democracy, and generate moral reform",
  "KC-7.1.II.B states that on the national level Progressives sought federal legislation that they believed would effectively regulate the economy, expand democracy, and generate moral reform."),
 ("places in cities and among immigrant populations",
  "KC-7.1.II.B opens 'On the national level' while KC-7.1.II.A puts reformers to work in cities and among immigrant populations, so the two sentences describe two scales; the anchor names the sentence the phrase is being contrasted with."),
 ("prohibition and women's suffrage",
  "KC-7.1.II.B states that Progressive amendments to the Constitution dealt with issues such as prohibition and women's suffrage."),
 ("What the Progressives expected of the legislation",
  "KC-7.1.II.B attributes the expectation to the Progressives with the words 'that they believed would', so the sentence reports an aim rather than grading an outcome, which is why Unit 7 Learning Objective D asks for goals AND effects."),
 ("Both supported the establishment of national parks",
  "KC-7.1.II.C states that preservationists and conservationists both supported the establishment of national parks while advocating different government responses to the overuse of natural resources."),
 ("On the government response to the overuse of natural resources",
  "KC-7.1.II.C locates the difference between preservationists and conservationists in the government response to the overuse of natural resources, not in the parks, which is what they agreed on."),
 ("preferred government response actually was",
  "KC-7.1.II.C says the two groups advocated DIFFERENT government responses without stating what either response was, so that is the question the sentence leaves open for Unit 7 Learning Objective E's comparison."),
 ("1890 to 1945",
  "Unit 7 Learning Objective E gives the span for the attitudes it asks students to compare as 1890 to 1945, the whole of Period 7, even though KC-7.1.II.C sits inside KC-7.1.II's Progressive Era."),
 ("cities and among immigrant populations with KC-7.1.II.A, and federal legislation with KC-7.1.II.B",
  "KC-7.1.II.A places reformers' work in cities and among immigrant populations and KC-7.1.II.B opens on the national level; the anchor carries both pairings because the reversed pairing is the distractor."),
 ("how these might limit the uses of a source",
  "Suggested skill 2.C as printed on this topic page, against skill 2.B's shorter statement on topics 7.3 and 7.14; it is the skill Unit 7 Learning Objective D's comparison is practised with here."),
 ("compare goals with effects",
  "Comparison is the reasoning process printed on this topic page, and both objectives are comparative: Unit 7 Learning Objective D compares goals and effects, Unit 7 Learning Objective E compares attitudes to natural resources."),
 ("Politics and Power, and Geography and the Environment",
  "The CED prints Politics and Power beside Unit 7 Learning Objective D with KC-7.1.II.A, KC-7.1.II.B and KC-7.1.II.D, and Geography and the Environment beside Unit 7 Learning Objective E with KC-7.1.II.C; the anchor carries both because every distractor keeps one and changes the other."),
 ("reformers working to effect social changes in cities",
  "KC-7.1.II.A states that reformers worked to effect social changes in cities and among immigrant populations, which is what classes organised for newly arrived families in a crowded district illustrate."),
 ("journalists attacking what they saw as political corruption",
  "KC-7.1.II.A states that some Progressive Era journalists attacked what they saw as political corruption, social injustice, and economic inequality."),
 ("groups are found on both sides of the question",
  "Recomputed in q27 from the illustrative table alone, and division on issue after issue is what KC-7.1.II.D means by stating that the Progressives were divided over many issues."),
 ("drew both support and opposition",
  "Recomputed in q28 from the illustrative table alone, including the invariant that every row sums to the same total; a body divided in that way is what KC-7.1.II.D describes."),
 ("transforming the nation into a limited welfare state",
  "The response to mass unemployment and the transformation into a limited welfare state is KC-7.1.III, printed on the later topics of this unit, while the other four statements are KC-7.1.II.A through KC-7.1.II.D on this topic's pages."),
 ("worked at more than one scale, sought several different ends",
  "KC-7.1.II.A works in cities, KC-7.1.II.B on the national level, KC-7.1.II.B names three ends at once, and KC-7.1.II.D opens by stating that the Progressives were divided over many issues; the anchor carries the scale and the ends together because a single-scale reading is the distractor."),
]


def _extra_mutations():
    def groups_agree_on_participation(mod, cl):
        # q27 keys that EVERY issue finds the groups on both sides. Bring the
        # two dissenting groups round on one issue and that stops being true --
        # while every cell stays a legal Favours or Opposes, so the format check
        # cannot answer this control in the semantics' place.
        t = dict(mod.QUESTIONS[26]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][1][1] = "Favours"
        t["rows"][3][1] = "Favours"
        mod.QUESTIONS[26]["table"] = t

    def every_proposal_carries(mod, cl):
        # q28 keys that the delegates did NOT carry them all. Reverse the one
        # proposal that fails, keeping the row's total intact so the invariant
        # cannot answer this control in the key's place.
        t = dict(mod.QUESTIONS[27]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][2][1], t["rows"][2][2] = "59", "41"
        mod.QUESTIONS[27]["table"] = t

    return [
        ("one issue made unanimous, so the groups are no longer split on every issue",
         groups_agree_on_participation, r"must find the groups on both sides"),
        ("the failing proposal reversed, so every proposal carries",
         every_proposal_carries, r"every proposal was carried"),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    import cg_check as cg
    for label, mutate, expect in _extra_mutations():
        mod = wh_check._mutant(a7_4)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            wh_check.history_style(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as e:
            assert re.search(expect, str(e), re.I), (
                f"CONTROL FIRED FOR THE WRONG REASON: {label} -- {e}")
            print(f"  control OK  {label}: {str(e)[:110]}")
        else:
            raise SystemExit(f"CONTROL FAILED: {label} did not raise")
    wh_stimulus.controls(a7_4)

wh_check.run(a7_4, CLAIMS, TABLE_CHECKS, sys.argv)
