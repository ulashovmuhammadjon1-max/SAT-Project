"""Key audit for AP WORLD HISTORY: MODERN 5.6 Industrialization: Government's Role.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim cites the Key Concept or Learning
Objective the key traces to.

WHAT THE KEYS REST ON
---------------------
Two statements, and every key traces to one of them or to Unit 5 Learning
Objective G:

  KC-5.1.V.C   As the influence of the Industrial Revolution GREW, a SMALL
               NUMBER of states and governments promoted THEIR OWN
               state-sponsored visions of industrialization.
  KC-5.2.II.A  The expansion of U.S. and European influence in Asia LED TO
               internal reform in Japan THAT SUPPORTED industrialization and LED
               TO the growing REGIONAL power of Japan in the Meiji Era.

The CED prints one illustrative example on this topic's page, under
"State-sponsored visions of industrialization": Muhammad Ali's development of a
cotton textile industry in Egypt. Items 4, 5 and 23 key that example and nothing
else about Egypt, because the framework says nothing else about it.

NO DATE IS KEYED
----------------
The framework gives no date for any reform, any program or any mill in this
topic, and it states that its periods are approximate and may begin before or
continue after the years given. Item 10 keys the Meiji Era because KC-5.2.II.A
prints that name, not because of any year attached to it.

SWAP ANCHORS
------------
KC-5.2.II.A is a chain of three links and each is easy to state backwards, so
items 9, 19, 24 and 27 carry the reversed link as a distractor; item 21 does the
same for KC-5.1.V.C's opening clause. Every one of those anchors carries BOTH
clauses, which is the defect found in verify_e2_1.py. The key-rotation control in
wh_check requires all thirty keys to fail when moved one place.

WHY THE TABLE CONTROL DOES NOT CATCH EVERY CELL
-----------------------------------------------
The selftest prints a per-table catch rate rather than demanding one hundred
percent, and that is deliberate. Raising the output index of a state that already
has the highest index, or raising the last decade's mill count in an already
rising column, leaves the keyed conclusion TRUE of the corrupted table. A check
that fired on those would be over-matching -- it would be reporting a defect that
is not there. What the control does require is that no table sits undefended:
q15, q16 and q17 must each catch at least one corrupted cell, and the printed
count is what makes a check that has stopped reading its table show up as a zero.

FIVE choices per item (A-E); see HISTORY_BRIEF.md.
"""
import sys

import cg_check as cg
import wh_check as wh
import w5_6

PROGRAM = "Government program of industrialization recorded"
OUTPUT = "Index of manufacturing output in the later decade"
MILLS = "Mechanized mills operating under the government program"
IMPORTED = "Share of cloth that was imported (percent)"


def _column(table, header):
    """A column read as raw strings, for a column that holds words not numbers."""
    heads = [cg.normalize(h) for h in table["headers"]]
    j = heads.index(cg.normalize(header))
    return [str(row[j]) for row in table["rows"]]


def q15(table, item):
    """A minority of the states carry a program, and those states lead on output."""
    labels = cg.labels(table)
    assert labels == ["State 1", "State 2", "State 3", "State 4", "State 5"], \
        f"the five rows must be the five illustrative states in order; got {labels}"
    flags = _column(table, PROGRAM)
    assert set(flags) <= {"Yes", "No"}, \
        f"the program column must hold only Yes or No; got {flags}"
    with_prog = [lab for lab, f in zip(labels, flags) if f == "Yes"]
    without = [lab for lab, f in zip(labels, flags) if f == "No"]
    assert len(with_prog) * 2 < len(labels), (
        f"the states with a program must be a MINORITY of the sample, which is what "
        f"KC-5.1.V.C's 'a small number' looks like in figures; got {with_prog} of {labels}"
    )
    assert len(with_prog) == 2, f"exactly two states must carry a program; got {with_prog}"
    out = dict(zip(labels, cg.col(table, OUTPUT)))
    lowest_with = min(out[lab] for lab in with_prog)
    highest_without = max(out[lab] for lab in without)
    assert lowest_with > highest_without, (
        f"every state with a program must out-rank every state without one, or the keyed "
        f"conclusion is false; lowest with a program {lowest_with}, highest without "
        f"{highest_without}"
    )
    return (f"recomputed from the table: {len(with_prog)} of {len(labels)} states record a "
            f"program, a minority, and the lowest index among them ({lowest_with}) exceeds the "
            f"highest index among the rest ({highest_without})")


def q16(table, item):
    """Mills rise at every step, the imported share falls at every step, and never to zero."""
    labels = cg.labels(table)
    assert labels == ["First decade", "Second decade", "Third decade", "Fourth decade"], \
        f"the four rows must be the four decades in order; got {labels}"
    mills = cg.col(table, MILLS)
    imported = cg.col(table, IMPORTED)
    assert all(b > a for a, b in zip(mills, mills[1:])), \
        f"the mill count must rise at every step; got {mills}"
    assert all(b < a for a, b in zip(imported, imported[1:])), \
        f"the imported share must fall at every step; got {imported}"
    assert imported[-1] > 0, (
        f"the imported share must still be above zero in the last decade, or the distractor "
        f"claiming it reaches zero would be true; got {imported[-1]}"
    )
    assert len(set(mills)) > 1 and len(set(imported)) > 1, \
        "'neither figure changes' must be false"
    return (f"recomputed from the table: mills {mills} rise at every step while the imported "
            f"share {imported} falls at every step and ends above zero")


def q17(table, item):
    """Three aims are government action; exactly one is a government standing aside."""
    aims = {str(row[0]): str(row[1]) for row in table["rows"]}
    assert sorted(aims) == ["State 1", "State 2", "State 3", "State 4"], \
        f"the four rows must be the four illustrative states; got {sorted(aims)}"
    expected = {
        "State 1": "The government funds and directs new mills of its own",
        "State 2": "The government reforms internal institutions so that industry may grow",
        "State 3": "The government promotes an industrial program of its own design",
        "State 4": "The government takes no part and leaves all industry to private merchants",
    }
    assert aims == expected, (
        f"the stated aims must be the four the item was written against, or the sorting below "
        f"is being done on different text; got {aims}"
    )
    aside = [lab for lab, aim in aims.items() if "takes no part" in aim.lower()]
    assert aside == ["State 4"], (
        f"exactly one state must stand aside, and it must be the keyed one; got {aside}"
    )
    acting = sorted(lab for lab in aims if lab not in aside)
    assert acting == ["State 1", "State 2", "State 3"], \
        f"the other three must all describe a government acting; got {acting}"
    for lab in acting:
        assert any(verb in aims[lab].lower() for verb in ("funds and directs",
                                                          "reforms internal institutions",
                                                          "promotes an industrial program")), \
            f"{lab}'s aim names no government action: {aims[lab]!r}"
    return ("read from the table alone: three rows describe a government funding, reforming or "
            "promoting, and one row describes a government taking no part")


CLAIMS = [
 ("promoted their own state-sponsored visions of industrialization",
  "KC-5.1.V.C states it in one sentence: as the influence of the Industrial Revolution grew, a small number of states and governments promoted their own state-sponsored visions of industrialization. Each rejected option contradicts that sentence rather than qualifying it."),
 ("only a few states and governments took this path",
  "KC-5.1.V.C says A SMALL NUMBER of states and governments, which is a limit and not a count. The framework neither universalizes the claim nor prints a figure, so both a majority reading and an exact number go beyond it."),
 ("a program of its own rather than one common program imposed on all",
  "KC-5.1.V.C says these states promoted THEIR OWN state-sponsored visions. The possessive is the framework's, and it is why no single shared or imported model can be keyed here."),
 ("Muhammad Ali's development of a cotton textile industry",
  "The CED prints exactly one illustrative example beside KC-5.1.V.C, under the heading state-sponsored visions of industrialization. The rejected options are illustrative examples printed on other topics' pages beside KC-5.2.I.E, KC-5.1.III.B and KC-5.1.II.A."),
 ("A cotton textile industry",
  "The illustrative example printed beside KC-5.1.V.C names a cotton textile industry in Egypt and no other sector. The framework says nothing about what else that state produced, so no other industry is keyable."),
 ("expansion of U.S. and European influence in Asia",
  "KC-5.2.II.A opens with that cause: the expansion of U.S. and European influence in Asia led to internal reform in Japan. The framework names no other cause for the reform anywhere in this unit."),
 ("Industrialization",
  "KC-5.2.II.A says the internal reform in Japan SUPPORTED INDUSTRIALIZATION. That is the middle link of the framework's own chain, and the rejected options substitute developments the sentence does not name."),
 ("growing regional power of Japan",
  "KC-5.2.II.A closes with the outcome: the reform supported industrialization and led to the growing regional power of Japan in the Meiji Era. Two rejected options reverse the direction of that change."),
 ("expansion of U.S. and European influence in Asia led to internal reform in Japan",
  "KC-5.2.II.A runs in one direction and this topic's reasoning process is causation, so the order of that sentence is the answer. The anchor carries BOTH clauses because a distractor exchanges them."),
 ("The Meiji Era",
  "KC-5.2.II.A names the era: the growing regional power of Japan in the Meiji Era. The rejected options are periods named in other statements of this unit, none of them attached to Japan's reform."),
 ("regional power rather than global power",
  "KC-5.2.II.A says the growing REGIONAL power of Japan and stops there. The adjective is the framework's own, so a key asserting worldwide power would supply something the CED does not print."),
 ("economic strategies they did, and what followed from them",
  "Unit 5 Learning Objective G asks students to explain the causes and effects of economic strategies of different states and empires. The rejected questions belong to the objectives behind KC-5.1.V.A, KC-5.3.I.A, KC-5.1.VI.C and KC-5.1.VI.A."),
 ("Accounts for other developments that could have produced the same growth",
  "Unit 5 Learning Objective G asks for causes and effects, and KC-5.1.V.C states only that such programs were promoted, never that they were the sole cause of any later growth. An argument that leaves rival causes unaddressed claims more than the framework supports."),
 ("government action, rather than private enterprise alone, supported industrial development",
  "KC-5.1.V.C describes governments promoting industrial visions of their own and KC-5.2.II.A describes internal reform that supported industrialization. The CED prints both on this topic's page, and identifying that pattern is the suggested skill for the topic."),
 ("minority of the states, and both states with one show a higher output index",
  "KC-5.1.V.C says a SMALL NUMBER of states and governments promoted such programs, and q15 above recomputes the sample: two states of five carry a program and the lowest index among them exceeds the highest index among the rest. The anchor carries both halves because two distractors reverse one of them."),
 ("rises in every decade while the share of cloth imported falls in every decade",
  "KC-5.1.V.C describes a government promoting an industrial vision of its own, and q16 above recomputes both columns: the mill count rises at every step, the imported share falls at every step, and it never reaches zero. Nothing here is recalled from outside the table."),
 ("State 4",
  "KC-5.1.V.C covers governments that PROMOTED industrial visions of their own and KC-5.2.II.A covers a government reforming internal institutions in a way that supported industrialization. q17 above finds exactly one row in which the government takes no part, which is the one aim neither statement covers."),
 ("promoted industrial programs of their own",
  "KC-5.1.V.C is the statement about governments promoting industrialization as a program of their own, and a treasury funding mills under a state official is that arrangement. The rejected options are KC-5.1.III.A, KC-5.1.V.A, KC-5.1.IV and KC-5.1.VI.A, none of which describes a government founding industry."),
 ("expansion of outside influence in Asia led to internal reform that supported industrialization",
  "KC-5.2.II.A states that the expansion of U.S. and European influence in Asia led to internal reform in Japan that supported industrialization. The source is unattributed and illustrative, and the anchor carries both clauses because a distractor exchanges them."),
 ("a named minister designed the industrial program",
  "KC-5.1.V.C and KC-5.2.II.A state the other four claims and name no minister, official or designer of any program. Supplying one fills a silence in the CED from outside it, which HISTORY_BRIEF.md forbids."),
 ("growing influence of the Industrial Revolution the setting in which those governments acted",
  "KC-5.1.V.C opens AS THE INFLUENCE OF THE INDUSTRIAL REVOLUTION GREW and only then describes what a small number of states did. The growing influence is the circumstance of that sentence, not its result, and the anchor carries both halves because a distractor reverses them."),
 ("state-sponsored vision of industrialization",
  "KC-5.1.V.C attaches the promotion of industrial visions to states and governments, while KC-5.1.V.A attaches organizing, shorter hours, higher wages and workers' parties to the workers themselves. Those are separate statements on separate topic pages."),
 ("Muhammad Ali's cotton textile industry in Egypt",
  "The illustrative example printed beside KC-5.1.V.C is the development of a cotton textile industry in Egypt, and cotton grown to supply state-directed spinning and weaving works is that arrangement. The rejected examples are printed beside KC-5.1.III.B, KC-5.1.II.A and KC-5.2.I.E."),
 ("Pressure from outside a state producing reform inside it",
  "KC-5.2.II.A begins with the expansion of U.S. and European influence in Asia and makes internal reform in Japan the consequence. The anchor carries both clauses because a distractor exchanges the outside pressure and the internal reform."),
 ("count of exactly how many states promoted such a program",
  "KC-5.1.V.C supplies the limit, the connection to the Industrial Revolution's growing influence and the possessive, and the CED prints the Egyptian example beside it. It prints no figure anywhere, so the count is the one item on the list the framework does not give."),
 ("consistent with it, because the framework says only a small number of states",
  "KC-5.1.V.C limits the claim to a small number of states and governments, so a state without such a program is exactly what the limit allows. The framework neither universalizes the claim nor denies that private merchants founded mills."),
 ("reform supported industrialization",
  "KC-5.2.II.A places the reform first and industrialization after it: internal reform in Japan THAT SUPPORTED industrialization. A distractor reverses that order, so the anchor carries the reform and the industrialization together."),
 ("both a government program in Egypt and internal reform in Japan",
  "KC-5.1.V.C carries the illustrative example of a cotton textile industry in Egypt and KC-5.2.II.A carries the internal reform in Japan, and the CED prints both statements on this one topic page. Each rejected option denies one half of what the page contains."),
 ("extended beyond its own region",
  "KC-5.2.II.A says regional power and stops there. Extending the claim past the region adds a reach the sentence does not give it, while the other four options restate parts of that same sentence."),
 ("outside pressure produced internal reform that supported industrialization and growing regional power",
  "The summary joins KC-5.1.V.C and KC-5.2.II.A, the two statements this topic prints, and keeps both hedges: a small number of governments, and power that is regional. Each rejected option contradicts one of those sentences."),
]

TABLE_CHECKS = {15: q15, 16: q16, 17: q17}

wh.run(w5_6, CLAIMS, TABLE_CHECKS, sys.argv)
