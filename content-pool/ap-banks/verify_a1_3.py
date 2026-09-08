"""Key audit for AP U.S. HISTORY 1.3 European Exploration in the Americas.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The shared gate is
``wh_check.run``, which the World History banks already use -- its checks are
about history rather than about world history.

WHAT THE KEYS REST ON
---------------------
This topic's Required Course Content is ONE sentence. That is the fact the whole
module is built around, and it is why so many items here are about the boundary
between a cause and a consequence rather than about further content:

  KC-1.2.I.A, the three causes: a search for new
    sources of wealth, economic and military
    competition, a desire to spread Christianity   items 2, 3, 4, 5, 6, 7, 10, 11,
                                                   12, 16, 22, 23, 24, 25, 27, 29, 30
  Unit 1 Learning Objective C, causes of
    exploration AND conquest by VARIOUS nations    1, 8, 9, 20, 26
  KC-1.2.I, competition and changes WITHIN
    European societies                             14, 15, 28
  KC-1.2, the Columbian Exchange among the
    RESULTS of contact                             17, 18
  the America in the World thematic focus          19
  Reasoning Process 2, Causation                   20, 21, 22
  the framework's note that the dates are
    approximate and not constraining               26

THE BOUNDARY THIS MODULE HAS TO HOLD. KC-1.2.I.B, KC-1.2.I.C and KC-1.2.II.A --
new crops and mineral wealth, maritime technology and joint-stock companies,
epidemics and introduced animals -- are printed on topics 1.4 and 1.5, not here.
They are true sentences of the framework, and a student who has read the unit
will recognise them, which is exactly what makes them good DISTRACTORS for a
question about causes: each names something the framework places on the other
side of the causal relation Learning Objective C asks about. Items 2, 16, 17 and
30 exist to test that boundary and key it explicitly.

THE SWAP ITEM. Item 15 asks how the word "competition" differs between
KC-1.2.I.A, where it is a cause, and KC-1.2.I, where it is a consequence inside
Europe. Its leading distractor keeps the first clause and exchanges the second,
so the anchor carries BOTH clauses.

DATA ITEMS: 12, 13 and 18.
  * Items 12 and 13 share ``_T_MOTIVES``, whose cells are counts. Every count is
    tied to the key by a derived assertion, including the bound that no motive
    can be mentioned in more documents than the set contains -- which is what
    catches an inflated cell rather than merely noticing it changed.
  * Item 13 keys what the table CANNOT support, so its first guard is on the
    HEADERS: no column reports what anyone judged more important, and corrupting
    a cell cannot make an absent column present. The header guard runs BEFORE
    anything about the rows, for the reason a1_1 records: the control for this
    item adds a column, and a row assertion running first would raise for a
    reason that says nothing about the guard it names.
  * Item 18's table is CATEGORICAL, and the shared corrupter appends text. A
    check written on ``startswith`` or on a substring survives an appended
    suffix and can therefore object to nothing, which is the failure a1_1
    records. So the STATEMENT column is compared literally here, independently
    of the module. The CAUSE-or-RESULT column is deliberately left to the
    semantic guard below, so the control that exchanges the two marks raises on
    the claim the item actually makes; a corrupted mark is still caught, through
    the two-and-two count.

NEGATIVE CONTROLS: ``python3 verify_a1_3.py --selftest``.
"""
import sys

import cg_check as cg
import wh_check
import a1_3

DOCS = "Documents in the set"
WEALTH = "Mentioning a search for new wealth"
RIVALRY = "Mentioning rivalry with another European crown"
CHRIST = "Mentioning spreading Christianity"
STATEMENT = "Statement a student proposes (illustrative)"
PLACE = ("Does the framework place it among the CAUSES of the efforts, or among the "
         "RESULTS of contact?")

_EXPECTED_SETS = ["Set 1", "Set 2", "Set 3"]


def _motive_columns(table):
    return (cg.col(table, DOCS), cg.col(table, WEALTH),
            cg.col(table, RIVALRY), cg.col(table, CHRIST))


def _motive_invariants(table):
    """Everything both motive items rely on, recomputed from the table alone."""
    assert cg.labels(table) == _EXPECTED_SETS, (
        f"the set labels are not the ones this check was written against; "
        f"got {cg.labels(table)}")
    docs, wealth, rivalry, christ = _motive_columns(table)
    # A motive cannot be mentioned in more documents than the set holds. This is
    # what makes an inflated cell a FAILURE rather than merely a change, which is
    # the difference between a check that reads its table and one that only
    # appears to.
    for name, column in (("wealth", wealth), ("rivalry", rivalry), ("Christianity", christ)):
        for i, (n, d) in enumerate(zip(column, docs)):
            assert 0 <= n <= d, (
                f"set {i + 1} records {n} documents mentioning {name} out of {d} in the "
                f"set, which no count of mentions can be")
    return docs, wealth, rivalry, christ


def q12(table, item):
    docs, wealth, rivalry, christ = _motive_invariants(table)
    rows = list(zip(wealth, rivalry, christ))
    assert all(min(r) > 0 for r in rows), (
        f"all three motives must appear in every set for the key to hold; got {rows}")
    leaders = {r.index(max(r)) for r in rows}
    assert len(leaders) > 1, (
        f"'no single motive leads in all three sets' requires the leader to change; "
        f"the leading column is {leaders} in every row")
    assert not all(w == max(r) and r.count(max(r)) == 1 for w, r in zip(wealth, rows)), \
        "'the search for new wealth leads in every set' must be false"
    assert not any(n == d for r, d in zip(rows, docs) for n in r), (
        f"'every document mentions all three motives' must be false, so no motive column "
        f"may equal the documents column; got {rows} against {docs}")
    return (f"across {len(rows)} sets of {docs[0]} documents the three motive counts are "
            f"{rows}, every one above zero, with the leading motive changing from set to "
            f"set and no count reaching the size of the set")


def q13(table, item):
    # HEADER GUARD FIRST, then the rows -- see the module docstring.
    joined = " ".join(str(h) for h in table["headers"]).lower()
    for word in ("important", "importance", "priority", "rank", "judged", "weight"):
        assert word not in joined, (
            f"the table must report nothing about what anyone judged more important for "
            f"the key to hold, but a header mentions {word!r}: {table['headers']}")
    docs, wealth, rivalry, christ = _motive_invariants(table)
    assert len(set(docs)) == 1, (
        f"'every set contains the same number of documents' must be true; got {docs}")
    assert rivalry[1] > rivalry[2], (
        f"'rivalry is mentioned in more documents in the second set than in the third' "
        f"must be true; got {rivalry}")
    assert christ[0] < wealth[0], (
        f"'Christianity is mentioned in fewer documents than wealth in the first set' "
        f"must be true; got {christ[0]} against {wealth[0]}")
    return ("no column reports what anyone judged more important, while the four "
            "remaining options are counts read directly off the rows")


_EXPECTED_STATEMENTS = [
    "A search for new sources of wealth",
    "Economic and military competition among European nations",
    "The Columbian Exchange",
    "Extensive demographic, economic, and social changes",
]


def _col(table, header):
    idx = table["headers"].index(header)
    return [row[idx] for row in table["rows"]]


def q18(table, item):
    # Only the STATEMENT column is compared literally. The CAUSE-or-RESULT column
    # is left to the semantic guard, so the control that exchanges the two marks
    # raises there -- on the claim the item makes -- rather than on a row-equality
    # assertion that would say nothing about it. A corrupted mark still fails,
    # through the two-and-two count below.
    assert _col(table, STATEMENT) == _EXPECTED_STATEMENTS, (
        f"the proposed statements are not the ones this check was written against; "
        f"got {_col(table, STATEMENT)}")
    statements, marks = _col(table, STATEMENT), _col(table, PLACE)
    causes = [s for s, m in zip(statements, marks) if m.strip().lower() == "cause"]
    results = [s for s, m in zip(statements, marks) if m.strip().lower() == "result"]
    assert len(causes) == 2 and len(results) == 2, (
        f"the key names exactly two causes against two results; got {len(causes)} and "
        f"{len(results)}")
    # The two marked as causes must be the two naming things KC-1.2.I.A gives as
    # causes, and neither of the two marked as results may be one of them.
    assert all("wealth" in s.lower() or "competition" in s.lower() for s in causes), \
        f"both rows marked as causes must name wealth or competition; got {causes}"
    assert not any("wealth" in s.lower() or "competition" in s.lower() for s in results), \
        f"neither row marked as a result may name wealth or competition; got {results}"
    return (f"exactly two rows are marked as causes and both name what KC-1.2.I.A gives "
            f"as causes ({causes}), against two marked as results that name neither")


TABLE_CHECKS = {12: q12, 13: q13, 18: q18}

CLAIMS = [
 ("Exploration and conquest of the New World by various European nations",
  "Unit 1 Learning Objective C gives the phrase verbatim: explain the causes of exploration and conquest of the New World by various European nations."),
 ("economic and military competition, and a desire to spread Christianity",
  "KC-1.2.I.A names a search for new sources of wealth, economic and military competition, and a desire to spread Christianity; the rejected sets each import maritime technology, the shift from feudalism to capitalism, new crops or epidemic disease, which belong to KC-1.2.I.B, KC-1.2.I.C and KC-1.2.II.A."),
 ("causal claim, that the three named things gave rise to the efforts",
  "KC-1.2.I.A's verb, stemmed from, places the three named things behind the efforts rather than after them, and Unit 1 Learning Objective C asks for exactly the causes of exploration and conquest."),
 ("search for new sources of wealth",
  "KC-1.2.I.A names a search for new sources of wealth as the first of its three causes, and a petition resting on reported gold and silver is that search stated plainly; maritime technology and joint-stock companies belong to KC-1.2.I.C."),
 ("Economic and military competition among European nations",
  "KC-1.2.I.A names economic and military competition as the second of its three causes, and a warning that a rival kingdom will claim the coast first is that competition; the Columbian Exchange belongs to KC-1.2 and the shift from feudalism to capitalism to KC-1.2.I.B."),
 ("desire to spread Christianity",
  "KC-1.2.I.A names a desire to spread Christianity as the third of its three causes; recording customs and founding farms appear nowhere among the causes the sentence gives."),
 ("search for new sources of wealth and the desire to spread Christianity",
  "KC-1.2.I.A's three causes are wealth, competition and Christianity, and reserving a share of precious metals with a priest aboard combines the first and third while naming no rival power. The anchor carries both halves because every distractor is a different pairing from the same list."),
 ("extends the question beyond first voyages to the taking of territory",
  "Unit 1 Learning Objective C asks for the causes of exploration AND conquest, and KC-1.2.I.A uses the same pair of words for the efforts whose causes it names."),
 ("the work of a single European power",
  "Unit 1 Learning Objective C asks about various European nations and KC-1.2.I.A likewise writes of European nations in the plural, so a one-power account is what the wording excludes."),
 ("Economic and military",
  "KC-1.2.I.A names economic and military competition; religion enters that sentence as a separate cause rather than as a kind of competition, and dynastic, cultural and legal competition appear nowhere in it."),
 ("a pursuit of something not yet held and the other is a contest with rival powers",
  "KC-1.2.I.A's list has three items and sets a search for new sources of wealth beside economic and military competition rather than inside it, so the framework distinguishes seeking a new source from contending with a rival for one."),
 ("no single motive leads in all three sets",
  "Recomputed in q12 from the table alone, including that each rejected option is false on the same counts. The three motive columns are the three causes KC-1.2.I.A names, and that sentence sets them side by side without ranking them."),
 ("judged one motive more important than the others",
  "Recomputed in q13: no column of the table reports what anyone judged more important, so this is the one claim of the five the counts cannot reach. KC-1.2.I.A ranks its three causes no more than the table does."),
 ("Within European societies",
  "KC-1.2.I states that European expansion into the Western Hemisphere generated intense social, religious, political, and economic competition and changes within European societies, and KC-1.2 places significant change on both sides of the Atlantic Ocean."),
 ("named among the causes of the efforts to explore and conquer, and in the other among the things European expansion generated",
  "KC-1.2.I.A makes competition a cause of the efforts while KC-1.2.I makes competition something expansion generated within European societies, so the same word is a cause in one sentence and a consequence in the other. The anchor carries both clauses because the leading distractor keeps the first and exchanges the second."),
 ("introduction of crops and animals not found in the Americas",
  "KC-1.2.I.A gives wealth, competition and Christianity as the causes; the introduction of crops and animals not found in the Americas belongs to KC-1.2.II.A, which describes what accompanied and furthered Spanish exploration and conquest rather than what set the efforts going."),
 ("which places the Columbian Exchange among the results of contact",
  "KC-1.2 states that contact among Europeans, Native Americans, and Africans RESULTED IN the Columbian Exchange, so the Exchange follows the voyages; the other sentences are true but silent on the ordering."),
 ("search for new sources of wealth, and economic and military competition among European nations",
  "Recomputed in q18 from the table alone: exactly two rows are marked as causes and both name what KC-1.2.I.A gives as causes, while the two marked as results are what KC-1.2 and KC-1.2.II place after contact."),
 ("shape the development of America and its increasingly important role in the world",
  "The America in the World thematic focus printed on this topic page states that diplomatic, economic, cultural, and military interactions between empires, nations, and peoples shape the development of America and America's increasingly important role in the world, and KC-1.2.I.A's economic and military competition is an interaction of that kind."),
 ("Describing causes and/or effects of a specific historical development",
  "Reasoning Process 2, Causation, opens with describing causes and effects of a specific historical development or process, and Unit 1 Learning Objective C asks for exactly that about exploration and conquest."),
 ("Weigh them against one another rather than simply list them",
  "Reasoning Process 2 includes explaining the difference between primary and secondary causes and between short-term and long-term effects, which is a task of weighing, while KC-1.2.I.A supplies three causes without weighing them."),
 ("stated together and left unranked",
  "KC-1.2.I.A names its three causes in one list and gives no order of importance among them, while Reasoning Process 2 makes explaining relative significance the student's task; reading a ranking into the sentence in either direction adds something it does not say."),
 ("names three causes and joins them in one sentence",
  "KC-1.2.I.A states that the efforts stemmed from a search for new sources of wealth, economic and military competition, and a desire to spread Christianity, which is three causes rather than one."),
 ("neither asserts nor denies it",
  "KC-1.2.I.A names wealth, competition and Christianity and says nothing whatever about population, so the framework does not speak to that explanation at all; Unit 1 Learning Objective C asks students to explain the causes the course content supplies."),
 ("why those nations undertook the voyages, not about how the voyages turned out",
  "KC-1.2.I.A's subject is the EFFORTS of European nations to explore and conquer, and it puts three motives behind them, which is what Unit 1 Learning Objective C means by causes; what was found and whom the voyagers met belong to KC-1.2.II and KC-1.2.III."),
 ("may lie before the period's opening date",
  "The framework states that events, processes, and developments are not constrained by the given dates and may begin before, or continue after, the approximate dates assigned to each unit and topic, so a cause of the efforts KC-1.2.I.A describes may predate the period."),
 ("third cause of the same standing",
  "KC-1.2.I.A joins a desire to spread Christianity to a search for new sources of wealth and to economic and military competition in one list of what the efforts stemmed from, giving no order among them."),
 ("which says expansion generated intense competition and changes within European societies",
  "KC-1.2.I locates the competition and change inside European societies, which is what a claim that Europe was unchanged denies; KC-1.2 makes the same point with changes on both sides of the Atlantic Ocean."),
 ("joins them as things the efforts stemmed from together, and asserts no order",
  "KC-1.2.I.A writes that the efforts stemmed from all three together, which is a list rather than a chronology, and nothing in it assigns a cause to a particular nation or places any of them after the voyages."),
 ("sought new sources of wealth, contended with one another economically and militarily",
  "KC-1.2.I.A in the framework's own terms and nothing more; maritime technology belongs to KC-1.2.I.C and the crops and animals to KC-1.2.II.A, neither of which the framework gives as a cause, and Unit 1 Learning Objective C speaks of various nations."),
]


def _extra_mutations():
    def importance_column_appears(mod, cl):
        # q13 keys what the table cannot support; a column reporting what a crown
        # judged most important would make the keyed claim reachable and the item
        # wrong.
        t = dict(mod.QUESTIONS[11]["table"])
        t["headers"] = list(t["headers"]) + ["Motive the crown judged most important"]
        t["rows"] = [list(r) + ["Wealth"] for r in t["rows"]]
        mod.QUESTIONS[11]["table"] = t
        mod.QUESTIONS[12]["table"] = t

    def cause_and_result_exchanged(mod, cl):
        # Flip which rows are marked as causes, so the keyed pair stops being the
        # one KC-1.2.I.A names. Every column still holds the same multiset of
        # values, so no single-cell corruption can express this.
        t = dict(mod.QUESTIONS[17]["table"])
        t["rows"] = [[s, ("Result" if m == "Cause" else "Cause")] for s, m in t["rows"]]
        mod.QUESTIONS[17]["table"] = t

    return [
        ("an importance column added, making q13's unsupportable claim supportable",
         importance_column_appears, "judged more important"),
        ("the Cause and Result marks exchanged, so the keyed pair is no longer the one "
         "KC-1.2.I.A names",
         cause_and_result_exchanged, "must name wealth or competition"),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    import contextlib
    import io
    for label, mutate, expect in _extra_mutations():
        mod = wh_check._mutant(a1_3)
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

wh_check.run(a1_3, CLAIMS, TABLE_CHECKS, sys.argv)
