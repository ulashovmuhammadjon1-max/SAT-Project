"""Key audit for AP U.S. HISTORY 1.4 Columbian Exchange, Spanish Exploration, and Conquest.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The shared gate is
``wh_check.run``, whose checks are about history rather than about world history.

WHAT THE KEYS REST ON
---------------------
  Unit 1 Learning Objective D, causes of the
    Exchange and its effect on Europe AND the
    Americas after 1492                            items 1, 7, 17, 19, 25, 26
  KC-1.2.I.B, new crops to Europe stimulating
    population growth, and new sources of mineral
    wealth facilitating the shift from feudalism
    to capitalism                                  2, 3, 4, 10, 14, 15, 20, 21, 24, 27, 28, 29, 30
  KC-1.2.I.C, maritime technology and organized
    trade methods helping drive economic change
    in Europe and the Americas                     5, 6, 7, 11, 22, 26, 30
  KC-1.2.II.A, epidemics and introduced crops and
    animals accompanying AND furthering Spanish
    exploration and conquest                       8, 9, 12, 13, 16, 23, 29, 30
  KC-1.2, the Exchange among the RESULTS of
    contact among three groups                     25
  the GEO thematic focus and skill 3.A             17, 18
  Reasoning Process 2, Causation, 2.ii             24

THE THREE HEDGED VERBS, which items 9, 21, 22 and 23 exist to hold. The
framework says mineral wealth FACILITATED the shift to capitalism, that
technology and trade methods HELPED DRIVE economic change, and that exploration
and conquest were ACCOMPANIED AND FURTHERED by epidemics. Each is weaker or
differently timed than the verb a student is likely to substitute -- caused,
produced, followed -- and a distractor that swaps the verb while keeping every
noun is the "right process, wrong strength of claim" near-miss HISTORY_BRIEF.md
warns about. Those anchors therefore carry the verb, not just the nouns.

THE SWAP ITEMS. This topic has TWO directions of movement in it, so the
characteristic wrong answer is a true statement pointed the wrong way. Items 4,
16, 27, 28 and 29 each carry a distractor that is the exact exchange of the
key's two halves -- crops to Europe against crops into the Americas, population
growth against the shift to capitalism, one KC code's clause against another's.
Every one of those anchors carries BOTH clauses, which is the defect
``verify_e2_1.py`` shipped.

DATA ITEMS: 14, 15 and 16.
  * Items 14 and 15 share ``_T_EUROPE``, whose cells are index numbers. Both
    columns are checked for direction at every step, so a corrupted cell breaks
    monotonicity and is caught; the period labels are compared literally so a
    corrupted label is caught too. Eight of the nine cells are caught, and the
    ninth was read rather than assumed: enlarging the LAST land figure keeps
    both columns rising at every step and keeps the land rising by more index
    points than the population, so neither key becomes false. A corruption that
    does not falsify the key is not something a check should invent an objection
    to.
  * Item 15 keys what the table CANNOT support -- that the crop caused the
    population rise -- which the framework DOES assert in KC-1.2.I.B while the
    two columns alone cannot. Its first guard is therefore on the HEADERS: no
    column reports a cause, and corrupting a cell cannot make an absent column
    present. The header guard runs BEFORE anything about the rows, for the
    reason a1_1 records: the control for this item adds a column, and a row
    assertion running first would raise for a reason that says nothing about the
    guard it names.
  * Item 16's table is CATEGORICAL, and the shared corrupter appends text, which
    ``startswith`` and substring tests survive -- the failure a1_1 records. So
    the ITEM column is compared literally here, independently of the module, and
    the DIRECTION column is left to the semantic guard, so the control that
    exchanges the two directions raises on the claim the item actually makes. A
    corrupted direction cell is still caught, through the two-and-two count.

NEGATIVE CONTROLS: ``python3 verify_a1_4.py --selftest``.
"""
import sys

import cg_check as cg
import wh_check
import a1_4

PERIOD = "Period (illustrative, after 1492)"
LAND = "Land under the new crop (index)"
POP = "Population (index)"
ITEM = "Item the framework names (illustrative arrangement)"
DIRECTION = "Which way does the framework describe it moving?"

_EXPECTED_PERIODS = ["First period", "Second period", "Third period"]


def _europe_columns(table):
    assert cg.labels(table) == _EXPECTED_PERIODS, (
        f"the period labels are not the ones this check was written against; "
        f"got {cg.labels(table)}")
    land, pop = cg.col(table, LAND), cg.col(table, POP)
    assert all(b > a for a, b in zip(land, land[1:])), \
        f"the land under the new crop must rise at every step; got {land}"
    assert all(b > a for a, b in zip(pop, pop[1:])), \
        f"the population must rise at every step; got {pop}"
    return land, pop


def q14(table, item):
    land, pop = _europe_columns(table)
    # and every distractor false on the same numbers
    assert not any(b < a for a, b in zip(pop, pop[1:])), "'the population falls' must be false"
    assert land[1] != land[0] and land[2] != land[1], (
        f"'the land under the new crop is unchanged after the first period' must be false; "
        f"got {land}")
    assert pop[-1] <= 2 * pop[0], (
        f"'the population more than doubles' must be false; {pop[-1]} against twice "
        f"{pop[0]}")
    assert land[-1] > land[-2], "'the land under the new crop falls at the last step' must be false"
    return (f"land {land} and population {pop} both rise at every step, and the final "
            f"population {pop[-1]} does not reach twice the opening {pop[0]}")


def q15(table, item):
    # HEADER GUARD FIRST, then the rows -- see the module docstring. The key is
    # that the table cannot establish causation, so what matters is that no
    # column reports one.
    joined = " ".join(str(h) for h in table["headers"]).lower()
    for word in ("cause", "caused", "because", "effect", "due to", "result"):
        assert word not in joined, (
            f"the table must report no cause for the key to hold, but a header mentions "
            f"{word!r}: {table['headers']}")
    land, pop = _europe_columns(table)
    assert pop[-1] > pop[0], "'the population is higher in the third period' must be true"
    assert (land[-1] - land[0]) > (pop[-1] - pop[0]), (
        f"'the land rises by more index points than the population' must be true; "
        f"{land[-1] - land[0]} against {pop[-1] - pop[0]}")
    falls = [a for a, b in zip(land, land[1:]) if b < a] + \
            [a for a, b in zip(pop, pop[1:]) if b < a]
    assert not falls, f"'neither column falls at any step' must be true; got {falls}"
    return ("no column of the table reports a cause, while the four remaining options "
            "are read directly off the two index columns")


_EXPECTED_ITEMS = [
    "New crops that stimulated European population growth",
    "New sources of mineral wealth",
    "Crops not found in the Americas",
    "Animals not found in the Americas",
]


def _col(table, header):
    idx = table["headers"].index(header)
    return [row[idx] for row in table["rows"]]


def q16(table, item):
    # Only the ITEM column is compared literally. The DIRECTION column is left to
    # the semantic guard, so the control that exchanges the two directions raises
    # there -- on the claim the item makes -- rather than on a row-equality
    # assertion that would say nothing about it. A corrupted direction cell still
    # fails, through the two-and-two count.
    assert _col(table, ITEM) == _EXPECTED_ITEMS, (
        f"the items are not the ones this check was written against; "
        f"got {_col(table, ITEM)}")
    items, directions = _col(table, ITEM), _col(table, DIRECTION)
    to_europe = [s for s, d in zip(items, directions)
                 if d.strip().lower() == "brought to europe from the americas"]
    into_americas = [s for s, d in zip(items, directions)
                     if d.strip().lower() == "introduced into the americas"]
    assert len(to_europe) == 2 and len(into_americas) == 2, (
        f"the key names exactly two items brought to Europe against two introduced into "
        f"the Americas; got {len(to_europe)} and {len(into_americas)}")
    # The two brought to Europe must be KC-1.2.I.B's pair and the two introduced
    # into the Americas must be KC-1.2.II.A's, or the keyed pairing is not what
    # the table says.
    assert not any("not found in the americas" in s.lower() for s in to_europe), (
        f"nothing described as not found in the Americas may be marked as brought to "
        f"Europe from there; got {to_europe}")
    assert all("not found in the americas" in s.lower() for s in into_americas), (
        f"both items marked as introduced into the Americas must be the ones the framework "
        f"describes as not found there; got {into_americas}")
    return (f"exactly two rows are marked as brought to Europe and neither is described as "
            f"not found in the Americas ({to_europe}), against two marked as introduced "
            f"into the Americas that both are")


TABLE_CHECKS = {14: q14, 15: q15, 16: q16}

CLAIMS = [
 ("Europe and the Americas, during the period after 1492",
  "Unit 1 Learning Objective D gives both halves verbatim: explain causes of the Columbian Exchange and its effect on Europe and the Americas during the period after 1492."),
 ("New crops, which stimulated European population growth",
  "KC-1.2.I.B states that the Columbian Exchange brought new crops to Europe from the Americas, stimulating European population growth. The anchor carries the item and its consequence together because the same sentence gives mineral wealth a different consequence."),
 ("The European shift from feudalism to capitalism",
  "KC-1.2.I.B states that the new sources of mineral wealth facilitated the European shift from feudalism to capitalism; the reversal of that direction is the distractor the anchor has to exclude."),
 ("Both the new crops and the new sources of mineral wealth are described as coming to Europe from the Americas",
  "KC-1.2.I.B brings both items to Europe from the Americas; movement into the Americas is KC-1.2.II.A's subject and concerns crops and animals not found there. The anchor carries both items and the direction because every distractor is a different assignment of the same directions."),
 ("Improvements in maritime technology, and more organized methods for conducting international trade",
  "KC-1.2.I.C names exactly this pair as helping drive changes to economies in Europe and the Americas; introduced animals and epidemics belong to KC-1.2.II.A and mineral wealth and population growth to KC-1.2.I.B."),
 ("Joint-stock companies",
  "KC-1.2.I.C names joint-stock companies as its own example of more organized methods for conducting international trade; the encomienda system of KC-1.2.II.B is a labor arrangement rather than a method of trade."),
 ("In Europe and the Americas alike",
  "KC-1.2.I.C locates the changes to economies in Europe and the Americas together, which matches KC-1.2's placement of change on both sides of the Atlantic Ocean and Unit 1 Learning Objective D's request for the effect on both."),
 ("Widespread deadly epidemics that devastated native populations, and the introduction of crops and animals not found in the Americas",
  "KC-1.2.II.A names both, in those words, as what accompanied and furthered Spanish exploration and conquest of the Americas. The anchor carries both clauses because the leading distractor moves the epidemics to Europe while keeping the structure."),
 ("did not merely coincide with the conquest but helped it along",
  "KC-1.2.II.A joins ACCOMPANIED to FURTHERED, so the sentence claims both that these things ran alongside the conquest and that they advanced it, which is stronger than coincidence and different from a consequence arriving afterwards."),
 ("KC-1.2.I.B, on new crops brought to Europe stimulating European population growth",
  "KC-1.2.I.B attributes European population growth to the new crops the Exchange brought to Europe, and a treatise arguing that a newly arrived plant feeds more people from the same ground states that link as an argument, which suggested skill 3.A asks students to identify."),
 ("KC-1.2.I.C, on more organized methods for conducting international trade, such as joint-stock companies",
  "KC-1.2.I.C names joint-stock companies as the example of the organized trade methods that helped drive economic change, and dividing a voyage's costs and returns among many investors is what such a company does. The anchor carries the clause as well as the code because the other half of the same sentence, maritime technology, is a distractor."),
 ("KC-1.2.II.A, on widespread deadly epidemics that devastated native populations",
  "KC-1.2.II.A states that Spanish exploration and conquest were accompanied and furthered by widespread deadly epidemics that devastated native populations, which is the collapse the record describes. The anchor carries the clause because the other half of the same sentence is also an option."),
 ("KC-1.2.II.A, on the introduction of crops and animals not found in the Americas",
  "KC-1.2.II.A names the introduction of crops and animals not found in the Americas among the things that accompanied and furthered Spanish exploration and conquest; KC-1.2.I.B describes movement in the opposite direction and concerns crops and mineral wealth."),
 ("Both the land under the new crop and the population rise at every step",
  "Recomputed in q14 from the table alone, with each rejected option falsified on the same numbers. KC-1.2.I.B is the sentence such a pattern would illustrate: new crops brought to Europe stimulating European population growth."),
 ("That the new crop was the cause of the rise in population",
  "Recomputed in q15: no column of the table reports a cause, so two quantities rising together is all it shows, even though KC-1.2.I.B does assert the causal link. Distinguishing what a source establishes from what it merely accompanies is suggested skill 3.A's own business."),
 ("brought to Europe, and the crops and animals not found in the Americas are the two introduced into the Americas",
  "Recomputed in q16 from the table alone: the two rows marked as brought to Europe are KC-1.2.I.B's pair and the two marked as introduced into the Americas are KC-1.2.II.A's. The anchor carries both halves because the leading distractor exchanges the directions while keeping every item."),
 ("Identify and describe a claim and/or argument in a text-based or non-text-based source",
  "Skill 3.A as printed on this topic page, and the skill Unit 1 Learning Objective D asks students to apply to sources about the Columbian Exchange; the distractors are skills 3.B, 3.C, 2.A and 5.A from other pages of this course."),
 ("the development of America impacts the environment and reshapes geography",
  "The Geography and the Environment thematic focus states this in its own words, and KC-1.2.II.A's introduced crops and animals together with KC-1.2.I.B's new crops reaching Europe are that reshaping running in both directions."),
 ("point from which the Columbian Exchange's effects on Europe and the Americas are traced",
  "Unit 1 Learning Objective D asks for the effect on Europe and the Americas during the period after 1492, so the date opens the span in which the effects are followed; the unit itself runs to 1607."),
 ("marshalling of Native American labor to extract precious metals",
  "KC-1.2.I.B names new crops, European population growth, new sources of mineral wealth and the shift from feudalism to capitalism. Marshalling Native American labor to extract precious metals is KC-1.2.II.B's description of the encomienda system, which belongs to a later topic of this unit."),
 ("helped a shift along without being its sole cause",
  "KC-1.2.I.B's verb is FACILITATED rather than caused, which credits the new sources of mineral wealth with helping the European shift from feudalism to capitalism without making them its whole explanation."),
 ("names contributing causes rather than a single sufficient one",
  "KC-1.2.I.C says maritime technology and organized trade methods HELPED DRIVE changes to economies in Europe and the Americas, crediting them with a share in the change in the same hedged way KC-1.2.I.B says mineral wealth facilitated the shift to capitalism."),
 ("accompanying and furthering the conquest, so they run alongside it and advance it",
  "KC-1.2.II.A places the epidemics beside Spanish exploration and conquest and gives them a part in it, rather than after it as a consequence; the same sentence calls them widespread and deadly and locates them among native populations."),
 ("New crops brought to Europe, and the stimulation of European population growth",
  "KC-1.2.I.B joins the two in one clause, which is the cause-and-effect relationship Reasoning Process 2 asks students to explain; the other pairings join terms the framework keeps in separate sentences."),
 ("one of the things that contact among those three groups resulted in",
  "KC-1.2 states that contact among Europeans, Native Americans, and Africans RESULTED IN the Columbian Exchange, so the Exchange follows the contact, while Unit 1 Learning Objective D still asks for the Exchange's own causes."),
 ("KC-1.2.I.B on new crops and mineral wealth reaching Europe, and KC-1.2.I.C on changes to economies in Europe and the Americas",
  "Those two sentences are the ones that place consequences of the Exchange in Europe, which is what a claim confining its effects to the Americas denies, and Unit 1 Learning Objective D asks about both sides."),
 ("New crops with European population growth, and new sources of mineral wealth with the shift from feudalism to capitalism",
  "KC-1.2.I.B attaches each consequence to its own item within one sentence, and the leading distractor exchanges the two consequences while keeping every term, so the anchor carries both pairings."),
 ("KC-1.2.I.B has new crops arriving in Europe from the Americas, while KC-1.2.II.A has crops not found in the Americas introduced there",
  "KC-1.2.I.B and KC-1.2.II.A mention crops moving in opposite directions, so exchanging the two codes misstates both sentences; the anchor carries the code and its direction together for that reason."),
 ("KC-1.2.II.A, on crops and animals not found in the Americas, and KC-1.2.I.B, on new sources of mineral wealth reaching Europe",
  "KC-1.2.II.A names the introduction of crops and animals not found in the Americas and KC-1.2.I.B the new sources of mineral wealth brought to Europe, which is what an outbound cargo of seed and stock against a return cargo of bullion would be. The anchor pins each code to its own clause because the distractor exchanges them."),
 ("crops and animals not found there into the Americas, and epidemics that devastated native populations accompanied and furthered the Spanish conquest",
  "Collects KC-1.2.I.B, KC-1.2.I.C and KC-1.2.II.A in the framework's own terms and adds nothing; the rejected options replace facilitated with caused, drop mineral wealth or animals, deny KC-1.2.I.B's European consequences, or contradict KC-1.2.II.A's accompanied and furthered."),
]


def _extra_mutations():
    def cause_column_appears(mod, cl):
        # q15 keys what the table cannot support; a column reporting the cause of
        # the rise would make the keyed claim reachable and the item wrong.
        t = dict(mod.QUESTIONS[13]["table"])
        t["headers"] = list(t["headers"]) + ["Cause of the rise recorded"]
        t["rows"] = [list(r) + ["The new crop"] for r in t["rows"]]
        mod.QUESTIONS[13]["table"] = t
        mod.QUESTIONS[14]["table"] = t

    def directions_exchanged(mod, cl):
        # Flip which items are brought to Europe, so the keyed pairing stops
        # being the framework's. Every column still holds the same multiset of
        # values, so no single-cell corruption can express this.
        t = dict(mod.QUESTIONS[15]["table"])
        flip = {"Brought to Europe from the Americas": "Introduced into the Americas",
                "Introduced into the Americas": "Brought to Europe from the Americas"}
        t["rows"] = [[s, flip[d]] for s, d in t["rows"]]
        mod.QUESTIONS[15]["table"] = t

    return [
        ("a cause column added, making q15's unsupportable claim supportable",
         cause_column_appears, "must report no cause"),
        ("the two directions exchanged, so the keyed pairing is no longer the framework's",
         directions_exchanged, "not found in the Americas may be marked as brought to Europe"),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    import contextlib
    import io
    for label, mutate, expect in _extra_mutations():
        mod = wh_check._mutant(a1_4)
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

wh_check.run(a1_4, CLAIMS, TABLE_CHECKS, sys.argv)
