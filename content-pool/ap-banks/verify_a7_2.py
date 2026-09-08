"""Key audit for AP U.S. HISTORY 7.2 Imperialism: Debates.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The gate is
``wh_check.run``, shared with the World History banks: a KC code or Learning
Objective in every ``why`` and every ``claim``, no figure language, no typeset
markup, the marked-stimulus rule, and the structural checks of ``cg_check``.

WHAT THE KEYS REST ON
---------------------
KC-7.3.I.A: "Imperialists cited economic opportunities, racial theories,
competition with European empires, and the perception in the 1890s that the
western frontier was 'closed' to argue that Americans were destined to expand
their culture and institutions to peoples around the globe."

KC-7.3.I.B: "Anti-imperialists cited principles of self-determination and
invoked both racial theories and the U.S. foreign policy tradition of
isolationism to argue that the United States should not extend its territory
overseas."

KC-7.3.I: "In the late 19th century and early 20th century, new U.S.
territorial ambitions and acquisitions in the Western Hemisphere and the
Pacific accompanied heightened public debates over America's role in
the world."

  the four things imperialists cited     items 2, 8, 10, 13, 28, 29
  what imperialists argued from them     3, 25, 29
  self-determination                     4, 9, 14, 22
  BOTH racial theories AND isolationism  5, 22, 23
  what anti-imperialists argued          6, 26
  the SHARED element, racial theories    7, 15, 18, 21, 30
  heightened public debates              12, 20
  the framework takes no side            11
  Unit 7 Learning Objective B            1, 21, 30
  suggested skill 2.C and its limits     16, 17, 19, 28
  the thematic focus printed on the page 24
  the boundary with topic 7.3            27

THE SWAP ITEMS, and why their anchors carry two clauses each: the whole
difficulty of this topic is that RACIAL THEORIES SIT ON BOTH SIDES, so an
anchor naming one argument without naming the side it is being contrasted with
would match the distractor built from the other sentence. Items 5, 9, 21 and 29
each pair one element from KC-7.3.I.A with one from KC-7.3.I.B, or reverse the
order of a correct pair, and each anchor therefore carries both halves.

WHAT IS NOT KEYED: nothing about the war with Spain or its outcome, which is
KC-7.3.I.C on the next topic's page -- item 27 keys that boundary rather than
crossing it -- and no named imperialist or anti-imperialist, because the CED
prints those names only under OPTIONAL SOURCES, which its own page says are not
required course content.

DATA ITEMS: 18, 19 and 20 carry explicitly illustrative tables recomputed below
from the table alone. The pamphlet table is CATEGORICAL, so its label and
position columns are compared literally and its Yes/No columns are format
checked, which makes every cell load-bearing for a reason of its own; the
semantic assertions that follow are what tie the rows to the key, and the
targeted control flips one flag so that it is those assertions, not a blanket
row equality, that fires.

NEGATIVE CONTROLS: ``python3 verify_a7_2.py --selftest``.
"""
import re
import sys

import wh_check
import wh_stimulus
import a7_2

PAMPHLET = "Hypothetical pamphlet (illustrative)"
POSITION = "Position it argues"
ECONOMIC = "Cites economic opportunity"
RACIAL = "Invokes racial theories"
ISOLATION = "Cites the tradition of isolationism"
STRETCH = "Stretch of years (illustrative)"
FOR = "Public meetings recorded arguing for extending U.S. territory overseas"
AGAINST = "Public meetings recorded arguing against extending U.S. territory overseas"

FOR_POS = "For extending U.S. territory overseas"
AGAINST_POS = "Against extending U.S. territory overseas"

_PAMPHLET_LABELS = ["Pamphlet 1", "Pamphlet 2", "Pamphlet 3", "Pamphlet 4"]
_POSITIONS = [FOR_POS, FOR_POS, AGAINST_POS, AGAINST_POS]
_STRETCH_LABELS = ["Stretch 1", "Stretch 2", "Stretch 3"]


def _col(table, header):
    idx = table["headers"].index(header)
    return [row[idx] for row in table["rows"]]


def _flags(table, header):
    """One Yes/No column, checked for form before it is read.

    The shared corrupter APPENDS to a cell, so 'Yes' becomes 'Yes CORRUPTED'.
    A check written as ``cell == "Yes"`` would then silently read it as a No and
    the corruption would change the answer without the check objecting. Refusing
    anything that is not exactly Yes or No is what makes each flag cell
    load-bearing.
    """
    vals = _col(table, header)
    for v in vals:
        assert v in ("Yes", "No"), f"{header!r} holds {v!r}, which is neither Yes nor No"
    return [v == "Yes" for v in vals]


def _pamphlet_frame(table):
    assert _col(table, PAMPHLET) == _PAMPHLET_LABELS, (
        f"the pamphlet table must be labelled {_PAMPHLET_LABELS}; got {_col(table, PAMPHLET)}"
    )
    assert _col(table, POSITION) == _POSITIONS, (
        f"the pamphlet table's positions are not the ones this check was written against; "
        f"got {_col(table, POSITION)}"
    )


def q18(table, item):
    _pamphlet_frame(table)
    pos = _col(table, POSITION)
    econ, racial, isol = (_flags(table, ECONOMIC), _flags(table, RACIAL),
                          _flags(table, ISOLATION))
    for_rows = [i for i, p in enumerate(pos) if p == FOR_POS]
    against_rows = [i for i, p in enumerate(pos) if p == AGAINST_POS]
    assert for_rows and against_rows, f"both positions must be represented; got {pos}"
    # THE KEY: racial theories are marked on at least one pamphlet of each side.
    assert any(racial[i] for i in for_rows) and any(racial[i] for i in against_rows), (
        f"racial theories must be invoked on both sides for the key to hold; the column reads "
        f"{racial} against positions {pos}"
    )
    # 'every pamphlet invokes racial theories' must be false.
    assert not all(racial), "'every pamphlet invokes racial theories' must be false"
    # The two distractors that offer the other columns as shared must be false.
    assert not any(econ[i] for i in against_rows), \
        "'economic opportunity is cited on both sides' must be false"
    assert not any(isol[i] for i in for_rows), \
        "'the tradition of isolationism is cited on both sides' must be false"
    return (f"racial theories are marked on {sum(racial)} of {len(racial)} pamphlets, at least "
            f"one on each side, while economic opportunity falls only on the rows arguing for "
            f"extension and isolationism only on those arguing against")


def q19(table, item):
    # This item keys what the table CANNOT support, so the guard is on the
    # table's COLUMNS rather than on any value in them: relative readership is
    # unreachable because no column reports it, and corrupting a cell cannot
    # make an absent column present. HEADER GUARD FIRST, then the frame: the
    # control for this item adds a "Copies printed" column, and if the frame ran
    # first it would raise on the position column instead, which would say
    # nothing about the guard this item names.
    joined = " ".join(table["headers"]).lower()
    for word in ("copies", "circulation", "readership", "readers", "printed", "sold",
                 "distributed"):
        assert word not in joined, (
            f"the table must report nothing about how widely a pamphlet was read for the key "
            f"to hold, but a header mentions {word!r}: {table['headers']}"
        )
    _pamphlet_frame(table)
    pos = _col(table, POSITION)
    econ, racial, isol = (_flags(table, ECONOMIC), _flags(table, RACIAL),
                          _flags(table, ISOLATION))
    assert pos.count(FOR_POS) == 2, "'two of the four pamphlets argue for extension' must be true"
    for_rows = [i for i, p in enumerate(pos) if p == FOR_POS]
    against_rows = [i for i, p in enumerate(pos) if p == AGAINST_POS]
    assert all(econ[i] for i in for_rows) and not any(econ[i] for i in against_rows), \
        "'economic opportunity is cited only by pamphlets arguing for extension' must be true"
    assert all(isol[i] for i in against_rows) and not any(isol[i] for i in for_rows), \
        "'isolationism is cited only by pamphlets arguing against extension' must be true"
    assert sum(racial[i] for i in for_rows) == 1 and sum(racial[i] for i in against_rows) == 1, \
        "'one pamphlet on each side invokes racial theories' must be true"
    return ("no column reports how widely any pamphlet was read, while the other four claims "
            "are read directly off the rows")


def q20(table, item):
    # ONE CELL OF NINE SURVIVES CORRUPTION, and the reason is the key rather
    # than the check: the item keys that both columns GROW, and the shared
    # corrupter multiplies the last figure of the leading column, which leaves
    # it growing and still leading. Every corruption that could make the keyed
    # reading false -- a fall, a flattening, a zero, a relabelled row, the two
    # columns crossing -- is caught below.
    assert _col(table, STRETCH) == _STRETCH_LABELS, (
        f"the meetings table must be labelled {_STRETCH_LABELS}; got {_col(table, STRETCH)}"
    )
    pro = [float(v) for v in _col(table, FOR)]
    con = [float(v) for v in _col(table, AGAINST)]
    assert min(pro + con) > 0, "'only meetings arguing for extension are recorded' must be false"
    assert all(b > a for a, b in zip(pro, pro[1:])), (
        f"the meetings arguing for extension must grow more numerous at every step; got {pro}"
    )
    assert all(b > a for a, b in zip(con, con[1:])), (
        f"the meetings arguing against extension must grow more numerous at every step, or "
        f"'both sides grow' is not what the record shows; got {con}"
    )
    assert all(a > b for a, b in zip(pro, con)), (
        f"'meetings against extension outnumber those for it in every stretch' must be false; "
        f"got {pro} against {con}"
    )
    return (f"both columns rise at every step, {pro} and {con}, both are recorded in every "
            f"stretch, and the column for extension leads throughout")


TABLE_CHECKS = {18: q18, 19: q19, 20: q20}

CLAIMS = [
 ("similarities and differences in attitudes about the nation's proper role",
  "Unit 7 Learning Objective B reads, verbatim, explain the similarities and differences in attitudes about the nation's proper role in the world."),
 ("competition with European empires, and the perception that the western frontier was closed",
  "KC-7.3.I.A names economic opportunities, racial theories, competition with European empires, and the perception in the 1890s that the western frontier was closed as what imperialists cited."),
 ("destined to expand their culture and institutions",
  "KC-7.3.I.A gives the imperialist conclusion as the claim that Americans were destined to expand their culture and institutions to peoples around the globe."),
 ("Principles of self-determination",
  "KC-7.3.I.B states that anti-imperialists cited principles of self-determination; free trade, toleration, federal supremacy and scientific management appear in neither KC-7.3.I.A nor KC-7.3.I.B."),
 ("Racial theories and the U.S. foreign policy tradition of isolationism",
  "KC-7.3.I.B says anti-imperialists invoked BOTH racial theories and the U.S. foreign policy tradition of isolationism, so the anchor carries both because every distractor pairs one of them with material from KC-7.3.I.A."),
 ("should not extend its territory overseas",
  "KC-7.3.I.B gives the anti-imperialist conclusion as the argument that the United States should not extend its territory overseas, with no regional exception and no claim about commerce."),
 ("cited by imperialists and invoked by anti-imperialists alike",
  "Racial theories are named in KC-7.3.I.A's list of what imperialists cited and in KC-7.3.I.B's statement that anti-imperialists invoked both racial theories and isolationism, so it is the one element the two sentences share."),
 ("Competition with European empires",
  "KC-7.3.I.A names competition with European empires and KC-7.3.I.B does not, whereas racial theories appear in both and self-determination and isolationism only in KC-7.3.I.B."),
 ("self-determination, and the perception that the western frontier was closed",
  "KC-7.3.I.B names principles of self-determination and KC-7.3.I.A names the perception in the 1890s that the western frontier was closed, in that order; the anchor carries both clauses because the reversed pair is the distractor."),
 ("a perception that imperialists cited in argument",
  "KC-7.3.I.A reports 'the perception in the 1890s that the western frontier was closed' among the things imperialists cited, so the framework reports it as a perception used in argument rather than asserting it."),
 ("report what each side cited and argued",
  "KC-7.3.I.A and KC-7.3.I.B each state what a side cited and what it argued, and neither endorses a side; Unit 7 Learning Objective B asks for a comparison of attitudes rather than a verdict."),
 ("Heightened public debates over America's role in the world",
  "KC-7.3.I states that new U.S. territorial ambitions and acquisitions in the Western Hemisphere and the Pacific accompanied heightened public debates over America's role in the world."),
 ("joins economic opportunity to competition with European empires",
  "KC-7.3.I.A names economic opportunities and competition with European empires among the things imperialists cited, and neither appears in KC-7.3.I.B."),
 ("principles of self-determination",
  "KC-7.3.I.B states that anti-imperialists cited principles of self-determination to argue against extending territory overseas, which is the argument that no people should be governed without its own consent."),
 ("invoked by anti-imperialists as well",
  "KC-7.3.I.A lists racial theories among what imperialists cited and KC-7.3.I.B says anti-imperialists invoked them too, so that argument alone cannot place a source on either side."),
 ("how these might limit the uses of a source",
  "Suggested skill 2.C as printed on this topic page, explain the significance of a source's point of view, purpose, historical situation, and audience, including how these might limit the uses of a source. It is the skill Unit 7 Learning Objective B's comparison of attitudes calls for; the distractors are skills 4.B, 5.B, 1.B and 6.D from other pages of this unit."),
 ("but not how widely that argument was held",
  "Suggested skill 2.C asks how purpose and audience limit a source's uses, and KC-7.3.I.A names economic opportunities as one of four things imperialists cited rather than as the whole of the case or as a measure of its support."),
 ("invoked by pamphlets arguing on both sides",
  "Recomputed in q18 from the illustrative table alone, and it is the pattern KC-7.3.I.A and KC-7.3.I.B state together, since racial theories are the one element both sentences carry."),
 ("more widely read",
  "Recomputed in q19: no column of the table reports readership, so this is the one claim of the five the record cannot reach. KC-7.3.I.A and KC-7.3.I.B likewise state what each side cited without asserting how widely either case was received."),
 ("grow more numerous",
  "Recomputed in q20 from the illustrative table alone, and rising argument on both sides is what KC-7.3.I calls heightened public debates over America's role in the world."),
 ("Both sides drew on racial theories, while only one side appealed to self-determination",
  "KC-7.3.I.A and KC-7.3.I.B share racial theories and differ over self-determination and isolationism, which answers both halves of Unit 7 Learning Objective B; the anchor carries both clauses because the reversed claim is the distractor."),
 ("cite principles of self-determination and the tradition of isolationism",
  "KC-7.3.I.B has anti-imperialists cite principles of self-determination and invoke the U.S. foreign policy tradition of isolationism to argue against extending territory overseas."),
 ("invoked racial theories alongside the tradition of isolationism",
  "KC-7.3.I.B says anti-imperialists invoked BOTH racial theories and the U.S. foreign policy tradition of isolationism, so the sentence has them using the racial argument rather than rejecting it."),
 ("America in the World, concerning interactions between empires",
  "The thematic focus printed on this topic page is America in the World, the diplomatic, economic, cultural, and military interactions between empires, nations, and peoples, which is the theme KC-7.3.I's debates belong to."),
 ("reports the claim imperialists made about expansion",
  "KC-7.3.I.A says imperialists cited four things TO ARGUE that Americans were destined to expand their culture and institutions, so the destiny sits inside the argument being reported."),
 ("says nothing about trade",
  "KC-7.3.I.B's argument is that the United States should not extend its TERRITORY overseas; commerce is absent from the sentence, and economic opportunities belong to KC-7.3.I.A."),
 ("led to the acquisition of island territories",
  "The acquisition of island territories following the American victory is KC-7.3.I.C, printed on the next topic's page, while this topic's Required Course Content is KC-7.3.I.A and KC-7.3.I.B."),
 ("was one of the things imperialists cited",
  "KC-7.3.I.A names the perception in the 1890s that the western frontier was closed among the things imperialists cited, which is a historical situation shaping an argument in the sense suggested skill 2.C asks about."),
 ("economic opportunities cited, and the argument that Americans were destined to expand",
  "KC-7.3.I.A names economic opportunities among what imperialists cited and gives their conclusion as the claim that Americans were destined to expand their culture and institutions, so the anchor carries both halves of the pair."),
 ("overlapping stock of arguments",
  "KC-7.3.I.A and KC-7.3.I.B share racial theories, differ over the rest, and end in opposite conclusions about extending territory, inside the heightened public debates KC-7.3.I describes."),
]


def _extra_mutations():
    def racial_only_on_one_side(mod, cl):
        # q18 keys that racial theories appear on BOTH sides. Clear the flag on
        # the one pamphlet arguing against extension that carries it, and the
        # keyed reading is gone -- while the cell stays a legal Yes/No, so the
        # format check cannot answer this control in the semantics' place.
        t = dict(mod.QUESTIONS[17]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][2][3] = "No"
        mod.QUESTIONS[17]["table"] = t

    def readership_column_appears(mod, cl):
        # q19 keys what the table cannot support; a column reporting readership
        # would make the keyed claim reachable and the item wrong. The column is
        # added to the HEADERS AND THE ROWS together, or cg_check's row-width
        # assertion would raise first and prove nothing about this guard.
        t = dict(mod.QUESTIONS[18]["table"])
        t["headers"] = list(t["headers"]) + ["Copies printed"]
        t["rows"] = [list(r) + ["2,000"] for r in t["rows"]]
        mod.QUESTIONS[18]["table"] = t

    def one_side_falls_away(mod, cl):
        # q20 keys that BOTH columns grow. Make the column arguing against
        # extension fall in the last stretch and the key stops holding.
        t = dict(mod.QUESTIONS[19]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][2][2] = "5"
        mod.QUESTIONS[19]["table"] = t

    return [
        ("racial theories cleared from the side arguing against extension",
         racial_only_on_one_side, r"racial theories must be invoked on both sides"),
        ("a readership column added, making q19's unsupportable claim supportable",
         readership_column_appears, r"nothing about how widely a pamphlet was read"),
        ("the meetings against extension made to fall away in the last stretch",
         one_side_falls_away, r"grow more numerous at every step"),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    import cg_check as cg
    for label, mutate, expect in _extra_mutations():
        mod = wh_check._mutant(a7_2)
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
    wh_stimulus.controls(a7_2)

wh_check.run(a7_2, CLAIMS, TABLE_CHECKS, sys.argv)
