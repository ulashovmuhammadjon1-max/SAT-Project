"""Key audit for AP U.S. HISTORY 5.2 Manifest Destiny.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The shared gate is
``wh_check.run``; ``a56_scope`` adds the citation-scope and attribution checks
this unit needs.

WHAT THE KEYS REST ON
---------------------
  Unit 5 Learning Objective B, causes and
    effects of westward expansion            items 1, 19, 20
  KC-5.1.I.A, resources, opportunity,
    refuge, and increased migration          2, 3, 4, 5, 6, 18, 21, 22, 25, 26, 30
  KC-5.1.I.B, what advocates of annexing
    western lands ARGUED, and the conflict
    it frequently provoked                   7, 8, 9, 10, 11, 27, 29, 30
  KC-5.1.I.D, legislation promoting western
    transportation and economic development  12, 13, 14, 15, 23, 30
  KC-5.1.I.E, initiatives creating more ties
    with Asia                                16, 17, 24, 28, 30
  the Geography and the Environment thematic
    focus printed on this page               21

WHAT IS DELIBERATELY NOT KEYED. The page also carries an OPTIONAL SOURCES list,
of which the CED says "The following optional sources and activity are not
required AP course content... None of the AP Exam questions require students to
have studied these specific sources." Nothing here asks who coined a phrase,
who signed a treaty or who wrote a pamphlet. ``kc_scope`` pins every ``why`` to
the four Historical Developments this topic's own page prints, or to its
Learning Objective, so a citation that wandered into a neighbouring topic fails.

ATTRIBUTION. KC-5.1.I.B does not assert that American institutions were
superior; it reports that ADVOCATES OF ANNEXING WESTERN LANDS ARGUED so. A
question that dropped the reporting verb would teach the argument as the
framework's finding, which is the one way this topic can do real damage.
``a56_scope.attributed`` refuses any stem, choice or ``why`` naming the
superiority of American institutions without an attribution word in reach, and
item 9 keys the distinction itself.

THE SWAP ITEMS. Item 22 offers KC-5.1.I.A's cause and effect exchanged and item
25 reverses the comparison the tally supports, so both anchors carry BOTH
clauses. Item 7 reverses the direction of expansion and item 3 the direction of
migration; each anchor carries the clause that separates the key from its swap.

DATA ITEMS: 25, 26, 27 and 28. Item 26 keys what the table CANNOT support, so
its guard is on the table's COLUMNS -- no column reports what became of the
households, and corrupting a cell cannot make an absent column present.

THE ORDER OF ASSERTIONS INSIDE A TABLE CHECK IS DELIBERATE. Each check runs its
semantic assertions FIRST and its literal row comparison LAST. The row
comparison is what makes every cell load-bearing against the shared corrupter,
which appends text to a categorical cell and scales a number -- necessary,
because scaling the leading count of the tally leaves it still the leading
count, so the comparison the key rests on would survive a corruption that
changed the data. But if the row comparison ran first, every targeted control
below would fire on it instead of on the claim it names, and would prove
nothing about the guard it is attached to.

NEGATIVE CONTROLS: ``python3 verify_a5_2.py --selftest``.
"""
import re
import sys

import a56_scope as a56
import cg_check as cg
import wh_check
import a5_2

MOTIVE = "Reason a hypothetical group of migrating households recorded"
HOUSEHOLDS = "Number of households recording it"
PAMPHLET = "Hypothetical annexation pamphlet, its author unnamed"
ARGUMENT = "Argument the pamphlet advances"

ALLOWED = ["KC-5.1.I.A", "KC-5.1.I.B", "KC-5.1.I.D", "KC-5.1.I.E"]
OBJECTIVE = "Unit 5 Learning Objective B"

# KC-5.1.I.B REPORTS this claim as the advocates' argument. Anything in the
# module that states it must say whose claim it is.
REPORTED = [(re.compile(r"superiority of American institutions", re.I),
             "the superiority of American institutions")]


# ------------------------------------------------------------------ table checks

def _col(table, header):
    idx = table["headers"].index(header)
    return [str(row[idx]) for row in table["rows"]]


_EXPECTED_MOTIVES = [
    ["Access to natural and mineral resources", "48"],
    ["Hope of economic opportunity", "61"],
    ["Hope of religious refuge", "22"],
    ["Other reasons recorded", "9"],
]
_MOTIVE_LABELS = [r[0] for r in _EXPECTED_MOTIVES]


def _motive_labels(table):
    labels = _col(table, MOTIVE)
    for want in _MOTIVE_LABELS:
        assert want in labels, (
            f"the reasons table no longer records {want!r}, so the lookups below would "
            f"read the wrong row; got {labels}")
    return labels


def q25(table, item):
    labels = _motive_labels(table)
    counts = cg.col(table, HOUSEHOLDS)
    named = dict(zip(labels, counts))
    assert named["Hope of economic opportunity"] > named["Access to natural and mineral resources"], (
        f"the keyed comparison must hold: {named['Hope of economic opportunity']} recording "
        f"economic opportunity against {named['Access to natural and mineral resources']} "
        f"recording resources")
    assert named["Hope of religious refuge"] < max(counts), (
        f"'religious refuge was the most frequently recorded reason' must be false; got "
        f"{named['Hope of religious refuge']} against {max(counts)}")
    assert len(set(counts)) == len(counts), (
        f"'every household recorded the same reason' must be false; got {counts}")
    assert sum(counts[:3]) > counts[3], (
        f"'the three named reasons were recorded by fewer households than the remainder' "
        f"must be false; got {sum(counts[:3])} against {counts[3]}")
    assert [list(r) for r in table["rows"]] == _EXPECTED_MOTIVES, (
        f"the reasons table does not hold the rows this check was written against; "
        f"got {table['rows']}")
    return (f"read from the table alone: {named['Hope of economic opportunity']:.0f} against "
            f"{named['Access to natural and mineral resources']:.0f}, four distinct counts, "
            f"and the three named reasons outnumbering the remainder")


def q26(table, item):
    # This item keys what the table CANNOT support, so its guard is a check on
    # the table's COLUMNS: nothing records what became of the households, and a
    # corrupted cell cannot make an absent column present. HEADER GUARD FIRST,
    # because the control for this item adds an outcome column and any check on
    # the rows would raise on the row width instead, passing the control for a
    # reason that says nothing about the guard it names.
    joined = " ".join(table["headers"]).lower()
    for word in ("outcome", "result", "found", "achiev", "succeed", "settled", "arriv"):
        assert word not in joined, (
            f"the table must report nothing about what became of the households for the key "
            f"to hold, but a header mentions {word!r}: {table['headers']}")
    labels = _motive_labels(table)
    counts = cg.col(table, HOUSEHOLDS)
    named = dict(zip(labels, counts))
    assert named["Hope of economic opportunity"] > named["Hope of religious refuge"], \
        "'economic opportunity recorded more often than religious refuge' must be true"
    assert named["Access to natural and mineral resources"] > 40, \
        "'resources recorded by more than forty households' must be true"
    assert named["Other reasons recorded"] < min(
        named["Access to natural and mineral resources"],
        named["Hope of economic opportunity"],
        named["Hope of religious refuge"]), \
        "'fewer households recorded a reason outside the three than recorded any one' must be true"
    assert [list(r) for r in table["rows"]] == _EXPECTED_MOTIVES, (
        f"the reasons table does not hold the rows this check was written against; "
        f"got {table['rows']}")
    return ("no column of the table reports what became of the households, while all four "
            "rejected claims are read directly off the rows")


_EXPECTED_PAMPHLETS = [
    ["Pamphlet 1",
     "Manifest Destiny compels the nation to extend its borders westward to the "
     "Pacific Ocean"],
    ["Pamphlet 2",
     "American institutions are superior to those of their neighbours and ought to "
     "be carried west"],
    ["Pamphlet 3",
     "The duties charged on imported cloth should be lowered at the next session"],
    ["Pamphlet 4",
     "Trade should be enlarged by treaty and by a regular steamship service across "
     "the Pacific"],
]


def _pamphlet_arguments(table):
    labels, arguments = _col(table, PAMPHLET), _col(table, ARGUMENT)
    assert labels == [r[0] for r in _EXPECTED_PAMPHLETS], (
        f"the pamphlet table no longer carries the four labels this check reads by; "
        f"got {labels}")
    return dict(zip(labels, arguments))


def q27(table, item):
    args = _pamphlet_arguments(table)
    annexation = [lab for lab, a in args.items()
                  if "manifest destiny" in a.lower() or "superior" in a.lower()]
    assert annexation == ["Pamphlet 1", "Pamphlet 2"], (
        f"exactly the first two pamphlets must advance the two claims KC-5.1.I.B reports, "
        f"Manifest Destiny and the superiority of American institutions; got {annexation}")
    trade = [lab for lab, a in args.items() if "trade" in a.lower()]
    assert trade == ["Pamphlet 4"], (
        f"the trade argument must sit on the fourth pamphlet alone; got {trade}")
    assert [list(r) for r in table["rows"]] == _EXPECTED_PAMPHLETS, (
        f"the pamphlet table does not hold the rows this check was written against; "
        f"got {table['rows']}")
    return ("read from the table alone: exactly two pamphlets advance the pair of claims "
            "the framework attributes to advocates of annexation, and neither of the other "
            "two does")


def q28(table, item):
    args = _pamphlet_arguments(table)
    trade = [lab for lab, a in args.items() if "trade" in a.lower()]
    assert trade == ["Pamphlet 4"], (
        f"exactly one pamphlet must advance the enlargement of trade; got {trade}")
    fourth = args["Pamphlet 4"].lower()
    assert "treaty" in fourth and "steamship" in fourth, (
        f"the trade pamphlet must propose both a treaty and a steamship service, which is "
        f"what makes it an economic and a diplomatic initiative at once; got {fourth!r}")
    assert [list(r) for r in table["rows"]] == _EXPECTED_PAMPHLETS, (
        f"the pamphlet table does not hold the rows this check was written against; "
        f"got {table['rows']}")
    return ("read from the table alone: one pamphlet of the four proposes enlarging trade, "
            "and it proposes both a treaty and a steamship service")


TABLE_CHECKS = {25: q25, 26: q26, 27: q27, 28: q28}

CLAIMS = [
 ("causes and effects of westward expansion from 1844 to 1877",
  "Unit 5 Learning Objective B verbatim; the anchor carries the span because one distractor keeps the wording and changes the years to Period 4's."),
 ("hope of many settlers for economic opportunities or religious refuge",
  "KC-5.1.I.A names the desire for access to natural and mineral resources AND this hope together as what led to increased migration to and settlement in the West."),
 ("increased migration to and settlement in the West",
  "KC-5.1.I.A's effect clause, verbatim. One distractor reverses the direction of the migration, which is why the anchor carries the direction as well as the noun."),
 ("without attributing it to all of them",
  "KC-5.1.I.A writes 'the hope of MANY settlers', which is a claim about a large number and not about every settler who moved west."),
 ("desire for access to natural and mineral resources",
  "KC-5.1.I.A names this first among the causes of increased migration, and ore is a mineral resource; the rejected options are KC-5.1.I.A's other motive and the subjects of KC-5.1.I.B, KC-5.1.I.D and KC-5.1.I.E."),
 ("hope of many settlers for religious refuge",
  "KC-5.1.I.A names economic opportunities OR religious refuge, and a move made in order to worship freely is the second; the anchor carries the whole phrase because the sibling motive shares its opening words."),
 ("compelled the United States to expand its borders westward to the Pacific Ocean",
  "KC-5.1.I.B, near verbatim as the argument it reports advocates of annexing western lands making. The anchor carries the direction because one distractor turns the expansion eastward."),
 ("Westward to the Pacific Ocean",
  "KC-5.1.I.B names the Pacific Ocean as the limit the advocates argued for; no other limit appears in that sentence."),
 ("not as the framework's own assertion",
  "KC-5.1.I.B opens 'Advocates of annexing western lands argued that', so the superiority of American institutions is reported as their argument rather than asserted by the framework."),
 ("frequently provoked competition and violent conflict",
  "KC-5.1.I.B's closing clause, verbatim: 'however, this frequently provoked competition and violent conflict'."),
 ("in every instance",
  "KC-5.1.I.B says FREQUENTLY, which asserts that the provocation was common while declining to claim it happened every time."),
 ("legislation promoting western transportation and economic development",
  "KC-5.1.I.D names exactly this as what boosted westward migration during and after the Civil War."),
 ("already occurring and was increased rather than begun",
  "KC-5.1.I.D says migration was BOOSTED, and KC-5.1.I.A has already described an increased migration arising from resources, opportunity and refuge, so the boost adds to a movement the framework has established."),
 ("not confined to the years following the war",
  "KC-5.1.I.D says DURING AND AFTER the Civil War, naming two stretches of time at once, so neither one alone is what the sentence claims."),
 ("Western transportation and economic development",
  "KC-5.1.I.D names both as what the new legislation promoted; the franchise, garrisons, mineral surveys and education are not in that sentence."),
 ("Economic, diplomatic, and cultural initiatives",
  "KC-5.1.I.E names exactly these three kinds of initiative as what U.S. interest in expanding trade led to."),
 ("Asia",
  "KC-5.1.I.E names Asia as the part of the world with which the initiatives were to create more ties; no other region appears in this topic's four sentences."),
 ("hope of economic opportunities drew many settlers",
  "KC-5.1.I.A is the sentence about why settlers moved, while the four rejected options restate parts of the argument KC-5.1.I.B reports advocates of annexation making."),
 ("Causation",
  "The Unit 5 outline prints causation beside this topic, matching Unit 5 Learning Objective B, which asks for the causes and effects of westward expansion from 1844 to 1877."),
 ("Explain a historical concept, development, or process",
  "Skill 1.B as printed beside this topic, and what Unit 5 Learning Objective B asks students to do with the concept of Manifest Destiny; the rejected options are skills 4.B, 3.C, 2.B and 5.A from other pages of this unit."),
 ("foster regional diversity",
  "The Geography and the Environment focus statement printed at the head of this topic, which is why the page rests on KC-5.1.I.A's desire for access to natural and mineral resources; the rejected options are the framework's Migration, Work, Social Structures and America in the World statements."),
 ("natural and mineral resources as the cause, and increased migration to and settlement in the West as the effect",
  "KC-5.1.I.A's own direction of causation. The anchor carries BOTH clauses because one distractor exchanges them, making the migration the cause and the desire its effect."),
 ("boosted by new legislation promoting western transportation",
  "KC-5.1.I.D ties a rise in westward migration to new legislation promoting western transportation and economic development, which a road and a telegraph line built under a new statute are."),
 ("create more ties with Asia",
  "KC-5.1.I.E names economic, diplomatic, and cultural initiatives creating more ties with Asia, and a steamship service with an exchange of envoys is an economic initiative and a diplomatic one together."),
 ("hope of economic opportunity than recorded access to natural and mineral resources",
  "Recomputed in q25 from the table alone: sixty one against forty eight, with the reversed comparison false on the same counts. All three named reasons are those KC-5.1.I.A gives for increased migration to and settlement in the West."),
 ("found the opportunity they had hoped for",
  "Recomputed in q26: no column of the table reports what became of the households, so this is the one claim of the five the record cannot reach. KC-5.1.I.A states the hopes settlers carried west, not what came of them."),
 ("Manifest Destiny and the pamphlet claiming the superiority of American institutions",
  "Recomputed in q27 from the table alone: exactly two of the four pamphlets advance the pair of claims KC-5.1.I.B reports advocates of annexing western lands arguing."),
 ("trade be enlarged by treaty and by a regular steamship service",
  "Recomputed in q28 from the table alone: one pamphlet of the four proposes enlarging trade, and by both a treaty and a steamship service, which is KC-5.1.I.E's economic and diplomatic initiative at once."),
 ("ended competition over natural resources",
  "KC-5.1.I.B says the expansion FREQUENTLY PROVOKED competition and violent conflict, so ending competition is the one claim of the five the framework does not make; the others restate KC-5.1.I.A, KC-5.1.I.B, KC-5.1.I.D and KC-5.1.I.E."),
 ("settlers west; advocates argued that expansion to the Pacific was compelled",
  "Collects KC-5.1.I.A, KC-5.1.I.B, KC-5.1.I.D and KC-5.1.I.E in the order this topic's page prints them and adds nothing to them."),
]


def _extra_mutations():
    def the_two_leading_counts_are_exchanged(mod, cl):
        # Swap the counts the keyed comparison rests on. The semantic assertions
        # run BEFORE the row comparison precisely so this fires on the
        # comparison rather than on row equality.
        t = dict(mod.QUESTIONS[24]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][0][1], t["rows"][1][1] = t["rows"][1][1], t["rows"][0][1]
        mod.QUESTIONS[24]["table"] = t

    def an_outcome_column_appears(mod, cl):
        # q26 keys what the table cannot support; a column reporting what became
        # of the households would make the keyed claim reachable and the item wrong.
        t = dict(mod.QUESTIONS[25]["table"])
        t["headers"] = list(t["headers"]) + ["Outcome recorded for the households"]
        t["rows"] = [list(r) + ["Prospered"] for r in t["rows"]]
        mod.QUESTIONS[25]["table"] = t

    def a_pamphlet_stops_arguing_for_annexation(mod, cl):
        # Replace the second pamphlet's argument, so only one of the four
        # advances the pair KC-5.1.I.B reports and the keyed pair is wrong.
        t = dict(mod.QUESTIONS[26]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][1][1] = "The roads of the eastern states should be repaired at public cost"
        mod.QUESTIONS[26]["table"] = t

    return [
        ("the two leading counts exchanged, so the keyed comparison reverses",
         the_two_leading_counts_are_exchanged),
        ("an outcome column added, making q26's unsupportable claim supportable",
         an_outcome_column_appears),
        ("a pamphlet no longer advancing the argument KC-5.1.I.B reports",
         a_pamphlet_stops_arguing_for_annexation),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    a56.controls(a5_2, ALLOWED, OBJECTIVE, REPORTED, out_of_scope="KC-5.1.I.C")
    for label, mutate in _extra_mutations():
        mod = wh_check._mutant(a5_2)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            wh_check.history_style(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as e:
            print(f"  control OK  {label}: {str(e)[:110]}")
        else:
            raise SystemExit(f"CONTROL FAILED: {label} did not raise")

a56.kc_scope(a5_2, ALLOWED, OBJECTIVE)
a56.attributed(a5_2, REPORTED)
wh_check.run(a5_2, CLAIMS, TABLE_CHECKS, sys.argv)
