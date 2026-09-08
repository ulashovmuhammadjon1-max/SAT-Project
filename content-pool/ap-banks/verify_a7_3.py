"""Key audit for AP U.S. HISTORY 7.3 The Spanish-American War.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The gate is
``wh_check.run``: a KC code or Learning Objective in every ``why`` and every
``claim``, no figure language, no typeset markup, the marked-stimulus rule, and
the structural checks of ``cg_check``.

WHAT THE KEYS REST ON -- ONE SENTENCE, AND WHAT IT DOES NOT SAY
---------------------------------------------------------------
KC-7.3.I.C: "The American victory in the Spanish-American War led to the U.S.
acquisition of island territories in the Caribbean and the Pacific, an increase
in involvement in Asia, and the suppression of a nationalist movement in
the Philippines."

KC-7.3.I: "In the late 19th century and early 20th century, new U.S.
territorial ambitions and acquisitions in the Western Hemisphere and the
Pacific accompanied heightened public debates over America's role in the world."

  the three effects, as a set              items 2, 11, 29, 30
  the two regions of the acquisitions      3, 14, 19, 23, 29
  the increase in involvement in Asia      4, 10, 18, 21, 28
  the suppression in the Philippines       5, 22, 29
  the direction of the causation           6, 7, 26
  Unit 7 Learning Objective C              1, 25
  suggested skill 2.B                      8, 15, 16, 17, 18
  the placement under KC-7.3.I             12, 19
  the boundary with topic 7.2              13, 24
  the thematic focus printed on the page   27
  what the sentence does NOT state         9, 10, 22, 23, 25

BECAUSE THE WHOLE TOPIC IS ONE SENTENCE, a third of these items key an ABSENCE:
no battle, no date, no commander, no casualty figure, no term of years for the
holding, no description of how the suppression was carried out, and no account
of the war's causes. Each of those keys is checkable by reading KC-7.3.I.C and
finding the claim missing, which is the only honest way to write a bank on a
sentence this short. Padding it with material from outside the CED is the
failure this module is written to avoid.

SENSITIVE MATERIAL. KC-7.3.I.C states the suppression of a nationalist movement
in the Philippines and states nothing further. Item 22 keys exactly that -- the
framework asserts the suppression without describing it -- and no item in this
module adds a method, a figure or an episode the CED does not carry.

THE SWAP ITEMS: 3 (one region kept of two), 24 (arguments and effects
exchanged) and 29 (each effect moved to another effect's place). Their anchors
carry both clauses, because half an anchor would match the swap.

DATA ITEMS: 19, 20 and 21. The territory table is CATEGORICAL, so its labels
and regions are compared literally and its acquisition column is refused unless
it holds exactly Yes or No -- the shared corrupter APPENDS to a cell, and a
check written as ``cell == "Yes"`` would read "Yes CORRUPTED" as a No without
objecting. Item 20 keys what the table CANNOT support, so its guard is on the
COLUMNS and it runs before the frame check, or the control that adds an opinion
column would raise on the frame and prove nothing about the guard it names.

NEGATIVE CONTROLS: ``python3 verify_a7_3.py --selftest``.
"""
import re
import sys

import wh_check
import wh_stimulus
import a7_3

TERRITORY = "Territory in the illustrative record"
REGION = "Region recorded"
ACQUIRED = "Recorded as acquired by the United States after the American victory"
STRETCH = "Stretch of years (illustrative)"
VESSELS = "U.S. merchant vessels recorded calling at Asian ports"
OFFICIALS = "U.S. officials recorded posted to Asian ports"

_TERRITORY_LABELS = ["Territory Q", "Territory R", "Territory S", "Territory T"]
_REGIONS = ["Caribbean", "Pacific", "Mediterranean", "Pacific"]
_STRETCH_LABELS = ["Stretch 1", "Stretch 2", "Stretch 3"]
_NAMED_REGIONS = {"Caribbean", "Pacific"}


def _col(table, header):
    idx = table["headers"].index(header)
    return [row[idx] for row in table["rows"]]


def _acquired_flags(table):
    """The Yes/No column, checked for form before it is read.

    ``cell == "Yes"`` would silently read the corrupter's "Yes CORRUPTED" as a
    No, so a corrupted cell could change the answer without the check
    objecting. Refusing anything that is not exactly Yes or No is what makes
    each of those cells load-bearing.
    """
    vals = _col(table, ACQUIRED)
    for v in vals:
        assert v in ("Yes", "No"), f"the acquisition column holds {v!r}, neither Yes nor No"
    return [v == "Yes" for v in vals]


def _territory_frame(table):
    assert _col(table, TERRITORY) == _TERRITORY_LABELS, (
        f"the territory table must be labelled {_TERRITORY_LABELS}; got "
        f"{_col(table, TERRITORY)}"
    )
    assert _col(table, REGION) == _REGIONS, (
        f"the territory table's regions are not the ones this check was written against; "
        f"got {_col(table, REGION)}"
    )


def q19(table, item):
    _territory_frame(table)
    regions, acquired = _col(table, REGION), _acquired_flags(table)
    taken = [r for r, a in zip(regions, acquired) if a]
    assert taken, "at least one territory must be recorded as acquired for the key to hold"
    # THE KEY: every acquired territory lies in one of the two regions KC-7.3.I.C names.
    stray = [r for r in taken if r not in _NAMED_REGIONS]
    assert not stray, (
        f"every territory recorded as acquired must lie in the Caribbean or the Pacific for "
        f"the key to hold; {stray} does not"
    )
    assert set(taken) == _NAMED_REGIONS, (
        f"'the territories recorded as acquired all lie in one region' must be false; the "
        f"acquired rows lie in {sorted(set(taken))}"
    )
    assert not all(acquired), "'every territory in the record was acquired' must be false"
    assert "Pacific" in taken, "'no territory in the Pacific is recorded as acquired' must be false"
    return (f"{len(taken)} of {len(acquired)} territories are marked as acquired and their "
            f"recorded regions are {taken}, both of them named by the framework, while the "
            f"row outside those regions is marked as not acquired")


def q20(table, item):
    # This item keys what the table CANNOT support, so the guard is on the
    # table's COLUMNS rather than on any value in them: no corruption of a cell
    # can make an absent column present. HEADER GUARD FIRST, then the frame:
    # the control for this item adds an opinion column, and if the frame ran
    # first it would raise on the region column instead, which would say nothing
    # about the guard this item names.
    joined = " ".join(table["headers"]).lower()
    for word in ("inhabitant", "inhabitants", "population", "resident", "residents",
                 "opinion", "consent", "welcomed", "vote"):
        assert word not in joined, (
            f"the table must report nothing about the people of the territories for the key "
            f"to hold, but a header mentions {word!r}: {table['headers']}"
        )
    _territory_frame(table)
    regions, acquired = _col(table, REGION), _acquired_flags(table)
    assert sum(acquired) == 3, "'three of the four territories are recorded as acquired' must be true"
    assert regions.count("Pacific") == 2, "'two of the recorded territories lie in the Pacific' must be true"
    caribbean = [a for r, a in zip(regions, acquired) if r == "Caribbean"]
    assert len(caribbean) == 1 and caribbean[0], (
        "'one recorded territory lies in the Caribbean and is recorded as acquired' must be true"
    )
    outside = [a for r, a in zip(regions, acquired) if r not in _NAMED_REGIONS]
    assert len(outside) == 1 and not outside[0], (
        "'the territory outside the Caribbean and the Pacific is not recorded as acquired' "
        "must be true"
    )
    return ("no column reports anything about the people of the territories, while the other "
            "four claims are read directly off the rows")


def q21(table, item):
    # TWO CELLS OF NINE SURVIVE CORRUPTION, and the reason is the key rather
    # than the check: the item keys that both measures RISE, and the shared
    # corrupter multiplies a figure, which on the last row of a rising column
    # leaves it rising. Every corruption that could make the keyed reading false
    # -- a fall, a flattening, a zero, a relabelled row -- is caught below.
    assert _col(table, STRETCH) == _STRETCH_LABELS, (
        f"the Asian port table must be labelled {_STRETCH_LABELS}; got {_col(table, STRETCH)}"
    )
    vessels = [float(v) for v in _col(table, VESSELS)]
    officials = [float(v) for v in _col(table, OFFICIALS)]
    assert min(vessels + officials) > 0, \
        "'only vessels are recorded, and nothing about officials' must be false"
    for name, vals in (("vessels", vessels), ("officials", officials)):
        assert all(b > a for a, b in zip(vals, vals[1:])), (
            f"the recorded {name} must rise at every step, or the keyed increase is not what "
            f"the record shows; got {vals}"
        )
    return (f"both columns rise at every step, {vessels} and {officials}, and both are "
            f"recorded in every stretch")


TABLE_CHECKS = {19: q19, 20: q20, 21: q21}

CLAIMS = [
 ("effects of the Spanish-American War",
  "Unit 7 Learning Objective C reads, verbatim, explain the effects of the Spanish-American War, and KC-7.3.I.C, the only historical development printed under it, states what the American victory led to."),
 ("increase in involvement in Asia, and the suppression of a nationalist movement",
  "KC-7.3.I.C names exactly three effects of the American victory: the acquisition of island territories in the Caribbean and the Pacific, an increase in involvement in Asia, and the suppression of a nationalist movement in the Philippines."),
 ("The Caribbean and the Pacific",
  "KC-7.3.I.C places the acquired island territories in the Caribbean AND the Pacific, and KC-7.3.I pairs the Western Hemisphere with the Pacific in the same way; the anchor carries both regions because keeping one is the plausible error."),
 ("It increased",
  "KC-7.3.I.C names an increase in involvement in Asia among the effects of the American victory, which fixes the direction against an end, a transfer or no change."),
 ("It was suppressed",
  "KC-7.3.I.C names the suppression of a nationalist movement in the Philippines among the effects of the American victory."),
 ("victory led to the three effects",
  "KC-7.3.I.C opens 'The American victory in the Spanish-American War led to' and then lists three consequences, and Unit 7 Learning Objective C asks for the effects of that war, so the causation runs from the victory outward."),
 ("Causation",
  "Causation is the reasoning process printed on this topic page, matching KC-7.3.I.C's structure of a victory that led to three named effects and Unit 7 Learning Objective C's demand for effects."),
 ("point of view, purpose, historical situation, and audience of a source",
  "Suggested skill 2.B as printed on this topic page; skill 2.C, which adds the significance of those things and the limits they place on a source, is printed on topics 7.2, 7.4 and 7.5, and Unit 7 Learning Objective C is the objective 2.B is practised on here."),
 ("names no battle at all",
  "KC-7.3.I.C states a victory and three effects and names no engagement, no commander and no date, so a battle read into it is material the framework does not supply."),
 ("change of degree rather than a beginning",
  "KC-7.3.I.C reports an INCREASE in involvement in Asia, which states that involvement grew rather than that it started, and the sentence keeps Asia distinct from the Caribbean and Pacific islands it names separately."),
 ("territory on the European continent",
  "KC-7.3.I.C names island territories in the Caribbean and the Pacific, an increase in involvement in Asia and the suppression of a nationalist movement in the Philippines; KC-7.3.I places the period's acquisitions in the Western Hemisphere and the Pacific, so European territory is in neither."),
 ("period of heightened public debate",
  "KC-7.3.I.C is a lettered sub-point of KC-7.3.I, which states that new U.S. territorial ambitions and acquisitions accompanied heightened public debates over America's role in the world."),
 ("imperialist and anti-imperialist argument",
  "KC-7.3.I.A gives the imperialist case and KC-7.3.I.B the anti-imperialist one, and the CED prints both on the preceding topic's page, while this page carries only KC-7.3.I.C and the effects Unit 7 Learning Objective C asks about."),
 ("acquisition of island territories in the Pacific",
  "KC-7.3.I.C names the acquisition of island territories in the Caribbean and the Pacific, so a station on a Pacific island falls under that effect rather than under the suppression it places in the Philippines."),
 ("point of view, purpose, historical situation, and audience",
  "Suggested skill 2.B, printed on this topic page, asks a student to explain the point of view, purpose, historical situation, and audience of a source, and KC-7.3.I.C reports the suppression without passing judgement or giving figures."),
 ("persuade a reading public",
  "Suggested skill 2.B asks for the purpose of a source, and a letter written to win readers over has persuasion as its purpose; KC-7.3.I.C supplies the acquisitions such a letter would be arguing about."),
 ("shaped for the people who would hear it",
  "Suggested skill 2.B asks a student to explain the audience of a source, which is worth explaining only because it shapes what the source says; KC-7.3.I.C gives the outcome both hypothetical sources argue about."),
 ("increase in U.S. involvement in Asia",
  "KC-7.3.I.C names an increase in involvement in Asia among the effects of the American victory, which is the historical situation a document about newly opened ports belongs to, in the sense suggested skill 2.B asks about."),
 ("recorded as acquired lies in the Caribbean or the Pacific",
  "Recomputed in q19 from the illustrative table alone, and it is the pattern KC-7.3.I.C states when it places the acquired island territories in the Caribbean and the Pacific."),
 ("inhabitants of the acquired territories welcomed",
  "Recomputed in q20: no column of the table reports anything about the people of the territories, so this is the one claim of the five the record cannot reach, and KC-7.3.I.C likewise reports the acquisitions without reporting opinion in them."),
 ("Both recorded measures rise across the stretches",
  "Recomputed in q21 from the illustrative table alone, and rising activity of both kinds is what KC-7.3.I.C means by an increase in involvement in Asia."),
 ("does not describe how it was carried out",
  "KC-7.3.I.C states the suppression of a nationalist movement in the Philippines as one of three effects and says nothing more about it: no method, no duration, no episode."),
 ("says nothing about how long the territories were held",
  "KC-7.3.I.C states the acquisition of island territories in the Caribbean and the Pacific and gives no term for that holding, so both 'temporary' and 'permanent' add to the sentence."),
 ("ARGUED, and this one states what the victory LED TO",
  "KC-7.3.I.A and KC-7.3.I.B report what each side argued and KC-7.3.I.C reports what the victory led to; the anchor carries both clauses because the reversed pairing is the distractor, and Unit 7 Learning Objective B and Unit 7 Learning Objective C ask the two different questions."),
 ("asks for the EFFECTS of the war",
  "Unit 7 Learning Objective C reads explain the effects of the Spanish-American War, and KC-7.3.I.C states only what the American victory led to, so the war's causes are outside this topic's required content."),
 ("The American victory in the Spanish-American War",
  "KC-7.3.I.C names the American victory as what led to the acquisitions, the increased involvement in Asia and the suppression; the closed frontier is KC-7.3.I.A's, the debates are KC-7.3.I's setting and the economic transition is KC-7.1.I's."),
 ("America in the World, concerning interactions between empires",
  "The thematic focus printed on this topic page is America in the World, the diplomatic, economic, cultural, and military interactions between empires, nations, and peoples, which is the theme KC-7.3.I.C's acquisitions belong to."),
 ("names an increase in involvement in Asia among the war's effects",
  "KC-7.3.I.C names an increase in involvement in Asia as one of the three things the American victory led to, which is what a claim of no change in Asia denies."),
 ("suppression of a nationalist movement with the Philippines, and the acquisition of island territories with the Caribbean",
  "KC-7.3.I.C attaches the acquisition to the Caribbean and the Pacific, the increase in involvement to Asia and the suppression to the Philippines; the anchor carries two of those pairings because every distractor moves an effect to another effect's place."),
 ("more than one kind, in more than one region",
  "KC-7.3.I.C attributes three different kinds of consequence to one victory, across the Caribbean, the Pacific, Asia and the Philippines, which is why Unit 7 Learning Objective C asks for the effects in the plural."),
]


def _extra_mutations():
    def stray_acquisition(mod, cl):
        # q19 keys that every acquired territory lies in one of the two regions
        # KC-7.3.I.C names. Mark the Mediterranean row as acquired and the key
        # is false -- while the cell stays a legal Yes/No, so the format check
        # cannot answer this control in the semantics' place.
        t = dict(mod.QUESTIONS[18]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][2][2] = "Yes"
        mod.QUESTIONS[18]["table"] = t

    def opinion_column_appears(mod, cl):
        # q20 keys what the table cannot support. Added to the HEADERS AND THE
        # ROWS together, or cg_check's row-width assertion raises first and
        # proves nothing about this guard.
        t = dict(mod.QUESTIONS[19]["table"])
        t["headers"] = list(t["headers"]) + ["Opinion of the inhabitants recorded"]
        t["rows"] = [list(r) + ["Favourable"] for r in t["rows"]]
        mod.QUESTIONS[19]["table"] = t

    def officials_fall_away(mod, cl):
        # q21 keys that BOTH measures rise. Make the officials column fall in
        # the last stretch and the keyed reading stops holding.
        t = dict(mod.QUESTIONS[20]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][2][2] = "7"
        mod.QUESTIONS[20]["table"] = t

    return [
        ("a territory outside the two named regions marked as acquired", stray_acquisition,
         r"must lie in the Caribbean or the Pacific"),
        ("an opinion column added, making q20's unsupportable claim supportable",
         opinion_column_appears, r"nothing about the people of the territories"),
        ("the officials posted to Asian ports made to fall in the last stretch",
         officials_fall_away, r"recorded officials must rise at every step"),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    import cg_check as cg
    for label, mutate, expect in _extra_mutations():
        mod = wh_check._mutant(a7_3)
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
    wh_stimulus.controls(a7_3)

wh_check.run(a7_3, CLAIMS, TABLE_CHECKS, sys.argv)
