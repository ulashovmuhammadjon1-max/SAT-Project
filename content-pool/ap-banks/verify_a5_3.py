"""Key audit for AP U.S. HISTORY 5.3 The Mexican-American War.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The shared gate is
``wh_check.run``; ``a56_scope.kc_scope`` pins every ``why`` to the two
Historical Developments this topic's own page prints, or to its Learning
Objective.

WHAT THE KEYS REST ON
---------------------
  Unit 5 Learning Objective C, causes and
    effects of the Mexican-American War       items 1, 13, 28
  KC-5.1.I.C, large territories added through
    victory AND diplomatic negotiations,
    raising questions about the status of
    slavery, American Indians and Mexicans    2, 3, 4, 5, 6, 7, 12, 14, 15, 16, 18,
                                              20, 22, 23, 24, 27, 28, 29, 30
  KC-5.1.II.C, increased interaction and
    conflict in regions newly taken,
    altering economic self-sufficiency and
    cultures                                  8, 9, 10, 11, 14, 17, 19, 21, 25, 26, 29, 30

NO ``attributed`` CHECK HERE, and that is deliberate rather than an omission.
Both of this topic's sentences are the framework's own assertions; neither
reports somebody else's argument the way KC-5.1.I.B does in topic 5.2. A gate
with nothing in scope to check would pass without being able to fail, which is
the shape of check this repository has already been burned by, so it is left
off rather than run empty.

SENSITIVE MATERIAL, and the one item that exists because of it. KC-5.1.II.C
says the increase in interaction and conflict ALTERED these groups' economic
self-sufficiency and cultures. It states that a change happened; it does not
state a direction. Item 19 therefore keys the neutral reading and offers "became
more self-sufficient" as a distractor, because a key in either direction would
be the bank asserting something about real people that the framework does not.

THE SWAP ITEMS. Item 17 offers the two alterations exchanged between the two
sources, item 21 offers KC-5.1.II.C's cause and effect exchanged, and item 7
offers the acquisition and the questions in reverse order; each anchor carries
both clauses.

DATA ITEMS: 22, 23, 24 and 25. Item 23 keys what the table CANNOT support, so
its guard is on the table's COLUMNS -- nothing records what the convention did
with a petition, and corrupting a cell cannot make an absent column present.

THE ORDER OF ASSERTIONS INSIDE A TABLE CHECK IS DELIBERATE: semantic assertions
first, the literal row comparison last. The row comparison makes every cell
load-bearing against the shared corrupter, which appends text to a categorical
cell; but if it ran first, each targeted control below would fire on it rather
than on the claim it names, and would prove nothing about the guard it is
attached to.

NEGATIVE CONTROLS: ``python3 verify_a5_3.py --selftest``.
"""
import sys

import a56_scope as a56
import cg_check as cg
import wh_check
import a5_3

PETITION = "Hypothetical petition to a territorial convention, its author unnamed"
RAISES = "Question it raises"
SOURCE = "Hypothetical unattributed source"
IDEA = "Main idea it advances"
COMMUNITY = "Hypothetical description recorded for a community in a region newly taken"
REPORTS = "What the description reports"

ALLOWED = ["KC-5.1.I.C", "KC-5.1.II.C"]
OBJECTIVE = "Unit 5 Learning Objective C"


# ------------------------------------------------------------------ table checks

def _col(table, header):
    idx = table["headers"].index(header)
    return [str(row[idx]) for row in table["rows"]]


_EXPECTED_PETITIONS = [
    ["Petition 1", "Whether persons may be held as slaves in the newly acquired lands"],
    ["Petition 2",
     "Whether American Indians in the newly acquired lands are to keep their lands"],
    ["Petition 3", "Whether Mexicans living in the newly acquired lands are to be citizens"],
    ["Petition 4", "Whether the duty charged on imported wool is to be raised"],
]


def _petitions(table):
    labels = _col(table, PETITION)
    assert labels == [r[0] for r in _EXPECTED_PETITIONS], (
        f"the petitions table no longer carries the four labels this check reads by; "
        f"got {labels}")
    return dict(zip(labels, _col(table, RAISES)))


def _status_petitions(asked):
    """The rows raising one of the three questions KC-5.1.I.C names, by subject."""
    slavery = [lab for lab, q in asked.items() if "held as slaves" in q.lower()]
    indians = [lab for lab, q in asked.items() if "american indians" in q.lower()]
    mexicans = [lab for lab, q in asked.items() if "mexicans" in q.lower()]
    duty = [lab for lab, q in asked.items() if "duty" in q.lower()]
    assert slavery == ["Petition 1"], (
        f"exactly the first petition must ask about persons held as slaves; got {slavery}")
    assert indians == ["Petition 2"], (
        f"exactly the second petition must ask about American Indians; got {indians}")
    assert mexicans == ["Petition 3"], (
        f"exactly the third petition must ask about Mexicans; got {mexicans}")
    assert duty == ["Petition 4"], (
        f"exactly the fourth petition must ask about a duty; got {duty}")
    return slavery + indians + mexicans, duty


def q22(table, item):
    asked = _petitions(table)
    status, duty = _status_petitions(asked)
    assert len(set(status)) == 3, (
        f"exactly three petitions must raise one of KC-5.1.I.C's three questions of status; "
        f"got {status}")
    assert duty[0] not in status, (
        f"the petition about a duty must not also raise a question of status; got {duty}")
    assert [list(r) for r in table["rows"]] == _EXPECTED_PETITIONS, (
        f"the petitions table does not hold the rows this check was written against; "
        f"got {table['rows']}")
    return ("read from the table alone: three of the four petitions raise one of the three "
            "questions of status the framework names, and the fourth raises none of them")


def q23(table, item):
    # This item keys what the table CANNOT support, so its guard is a check on
    # the table's COLUMNS: nothing records what became of a petition, and a
    # corrupted cell cannot make an absent column present. HEADER GUARD FIRST,
    # because the control adds an answer column and any check on the rows would
    # raise on the row width instead -- a control firing for a reason that says
    # nothing about the guard it names.
    joined = " ".join(table["headers"]).lower()
    for word in ("answer", "outcome", "decision", "resolved", "ruling", "result", "vote"):
        assert word not in joined, (
            f"the table must record nothing about what became of a petition for the key to "
            f"hold, but a header mentions {word!r}: {table['headers']}")
    asked = _petitions(table)
    status, duty = _status_petitions(asked)
    assert len(set(status)) == 3, "'three of the four raise a question of status' must be true"
    assert len(duty) == 1, "'one petition concerns a duty' must be true"
    assert sum(1 for q in asked.values() if "held as slaves" in q.lower()) == 1, \
        "'one petition asks whether persons may be held as slaves' must be true"
    assert not any("european" in q.lower() for q in asked.values()), \
        "'no petition concerns the status of a European power' must be true"
    assert [list(r) for r in table["rows"]] == _EXPECTED_PETITIONS, (
        f"the petitions table does not hold the rows this check was written against; "
        f"got {table['rows']}")
    return ("no column of the table records what became of a petition, while all four "
            "rejected claims are read directly off the rows")


_EXPECTED_SOURCES = [
    ["Source 1",
     "The territory gained by the war settled every question about who would live there "
     "and under what status"],
    ["Source 2",
     "The territory gained by the war left open the question of who would live there "
     "and under what status"],
]


def q24(table, item):
    labels = _col(table, SOURCE)
    assert labels == [r[0] for r in _EXPECTED_SOURCES], (
        f"the sources table no longer carries the two labels this check reads by; got {labels}")
    ideas = dict(zip(labels, _col(table, IDEA)))
    settled = [lab for lab, d in ideas.items() if "settled every question" in d.lower()]
    left_open = [lab for lab, d in ideas.items() if "left open the question" in d.lower()]
    assert settled == ["Source 1"], (
        f"the source denying that questions remained must be the first; got {settled}")
    assert left_open == ["Source 2"], (
        f"the source matching KC-5.1.I.C, which says questions were RAISED, must be the "
        f"second; got {left_open}")
    assert all("status" in d.lower() for d in ideas.values()), (
        f"'neither source addresses status' must be false, so both must mention it; "
        f"got {list(ideas.values())}")
    assert all("territory gained" in d.lower() for d in ideas.values()), (
        f"neither source may deny that territory was gained; got {list(ideas.values())}")
    assert not any(("extent" in d.lower() or "size" in d.lower()) for d in ideas.values()), (
        f"'the two differ only about the extent of the territory' must be false, so neither "
        f"may mention extent at all; got {list(ideas.values())}")
    assert [list(r) for r in table["rows"]] == _EXPECTED_SOURCES, (
        f"the sources table does not hold the rows this check was written against; "
        f"got {table['rows']}")
    return ("read from the table alone: one source leaves the question of status open and "
            "the other says it was settled, and both record that territory was gained")


_EXPECTED_COMMUNITIES = [
    ["Community A", "Its customary way of making a living was disrupted"],
    ["Community B", "Its observances and its language came under pressure"],
    ["Community C", "Both its way of making a living and its observances were affected"],
    ["Community D", "A new road was surveyed some miles away"],
]


def q25(table, item):
    labels = _col(table, COMMUNITY)
    assert labels == [r[0] for r in _EXPECTED_COMMUNITIES], (
        f"the communities table no longer carries the four labels this check reads by; "
        f"got {labels}")
    desc = dict(zip(labels, _col(table, REPORTS)))

    def has(text, word):
        return word in text.lower()

    both = [lab for lab, d in desc.items()
            if has(d, "making a living") and has(d, "observances")]
    living = [lab for lab, d in desc.items()
              if has(d, "making a living") and not has(d, "observances")]
    culture = [lab for lab, d in desc.items()
               if has(d, "observances") and not has(d, "making a living")]
    neither = [lab for lab, d in desc.items()
               if not has(d, "making a living") and not has(d, "observances")]
    assert both == ["Community C"], (
        f"exactly one description must report both alterations KC-5.1.II.C names, and it "
        f"must be the third; got {both}")
    assert living == ["Community A"], (
        f"exactly the first description must report a livelihood alone; got {living}")
    assert culture == ["Community B"], (
        f"exactly the second description must report observances alone; got {culture}")
    assert neither == ["Community D"], (
        f"exactly the fourth description must report neither alteration; got {neither}")
    assert [list(r) for r in table["rows"]] == _EXPECTED_COMMUNITIES, (
        f"the communities table does not hold the rows this check was written against; "
        f"got {table['rows']}")
    return ("read from the table alone: one description of the four reports both a way of "
            "making a living and observances, two report one each, and one reports neither")


TABLE_CHECKS = {22: q22, 23: q23, 24: q24, 25: q25}

CLAIMS = [
 ("causes and effects of the Mexican-American War",
  "Unit 5 Learning Objective C verbatim; one distractor keeps the wording and drops the effects, which is why the anchor carries both halves."),
 ("Large territories",
  "KC-5.1.I.C opens by stating that the United States added large territories in the West."),
 ("Mexican-American War and diplomatic negotiations",
  "KC-5.1.I.C names both means in one clause: the territories were added through victory in the war AND diplomatic negotiations."),
 ("not all of the added territory came through military victory alone",
  "KC-5.1.I.C attributes the addition to two means at once, so naming only the victory would drop half of what the sentence says."),
 ("Slavery, American Indians, and Mexicans",
  "KC-5.1.I.C names exactly these three as the subjects whose status the acquisition raised questions about, in the newly acquired lands."),
 ("The newly acquired lands",
  "KC-5.1.I.C places the questions of status in the newly acquired lands rather than anywhere the United States already held."),
 ("followed from the acquisition rather than preceding it",
  "KC-5.1.I.C makes the acquisition the thing that RAISED the questions, which fixes the order Unit 5 Learning Objective C asks students to explain."),
 ("interaction and conflict with Mexican Americans and American Indians",
  "KC-5.1.II.C, near verbatim; the same sentence says these groups' economic self-sufficiency was ALTERED rather than increased, which is what makes that distractor wrong."),
 ("newly taken from American Indians and Mexico",
  "KC-5.1.II.C names these regions, which places the increase where KC-5.1.I.C has just said territory was added."),
 ("economic self-sufficiency and their cultures",
  "KC-5.1.II.C names exactly this pair as what was altered; numbers, military strength, landholdings and trade with Europe appear nowhere in the sentence."),
 ("dealings of more than one kind, not conflict only",
  "KC-5.1.II.C names INTERACTION AND CONFLICT together, so the sentence covers dealings that were not all violent as well as those that were."),
 ("added through victory in war and through diplomatic negotiations",
  "KC-5.1.I.C is the sentence about how the territories were acquired, while the four rejected options all restate KC-5.1.II.C's account of what followed."),
 ("Compare the arguments or main ideas of two sources",
  "Skill 3.C as printed beside this topic, and the skill Unit 5 Learning Objective C is practised with here; the rejected options are skills 1.B, 4.B, 2.B and 3.D, printed beside other topics of this unit."),
 ("reports that their economic self-sufficiency and cultures were altered",
  "KC-5.1.I.C raises the question of status and KC-5.1.II.C then reports the alteration, so the two sentences run in that order and neither records an answer."),
 ("America's increasingly important role in the world",
  "The America in the World thematic focus printed at the head of this topic, which is why the page rests on KC-5.1.I.C's pairing of military victory with diplomatic negotiations."),
 ("diplomatic negotiations the sentence names alongside victory in the war",
  "KC-5.1.I.C names diplomatic negotiations as the second of two means, so a boundary fixed by agreement between governments is that means rather than the victory."),
 ("economic self-sufficiency in the first and culture in the second",
  "KC-5.1.II.C names economic self-sufficiency and cultures as the two alterations. The anchor carries BOTH clauses because one distractor exchanges them between the two accounts."),
 ("raised questions about the status of slavery",
  "KC-5.1.I.C names the status of slavery in the newly acquired lands as one of the three questions the acquisition raised."),
 ("way these groups supported themselves was changed",
  "KC-5.1.II.C says the economic self-sufficiency was ALTERED, which states that a change occurred and does not state a direction; supplying one would go beyond the sentence."),
 ("were resolved within the period",
  "KC-5.1.I.C says the questions were RAISED and records no resolution, so a resolution is the one claim of the five this topic does not make."),
 ("interaction and conflict as the cause, and the alteration of these groups' economic self-sufficiency and cultures as the effect",
  "KC-5.1.II.C's own direction of causation: the increase altered the self-sufficiency and cultures. The anchor carries BOTH clauses because one distractor exchanges them."),
 ("about slavery, about American Indians, and about Mexicans",
  "Recomputed in q22 from the table alone: three of the four petitions raise one of the three questions KC-5.1.I.C names, and the fourth raises none of them."),
 ("convention answered the questions",
  "Recomputed in q23: no column of the table records what became of a petition, so this is the one claim of the five the record cannot reach; KC-5.1.I.C likewise records no answer."),
 ("second matches the framework, which says the acquisition raised questions about status",
  "Recomputed in q24 from the table alone, against KC-5.1.I.C, which says the acquisition RAISED questions about status rather than settling them."),
 ("way of making a living and whose observances were both affected",
  "Recomputed in q25 from the table alone: exactly one description reports both of the alterations KC-5.1.II.C names, economic self-sufficiency and cultures."),
 ("names economic self-sufficiency and cultures as what was altered",
  "KC-5.1.II.C names both, and a disrupted trade with observances under pressure is one of each; KC-5.1.I.C concerns how the territories were added instead."),
 ("questions the same acquisition raised, rather than as unrelated matters",
  "KC-5.1.I.C attributes all three questions of status to one acquisition, in a single clause, without ranking them or answering any of them."),
 ("added territories and the questions of status both follow from the victory",
  "Unit 5 Learning Objective C asks for causes and effects, and KC-5.1.I.C places both the territories and the questions after the victory it names, which makes them effects."),
 ("raised questions about the status of slavery, American Indians and Mexicans there",
  "Collects KC-5.1.I.C and KC-5.1.II.C in the order this topic's page prints them and adds nothing to them."),
 ("brought their status into question and was followed by increased government interaction",
  "KC-5.1.I.C raises the questions of status and KC-5.1.II.C reports the increased interaction and conflict that followed in the regions newly taken."),
]


def _extra_mutations():
    def a_fourth_petition_raises_a_status_question(mod, cl):
        # Give the duty petition a question of status, so four rather than three
        # raise one and the keyed set of three is wrong.
        t = dict(mod.QUESTIONS[21]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][3][1] = "Whether Mexicans in the newly acquired lands may hold office"
        mod.QUESTIONS[21]["table"] = t

    def an_answer_column_appears(mod, cl):
        # q23 keys what the table cannot support; a column recording the
        # convention's answer would make the keyed claim reachable.
        t = dict(mod.QUESTIONS[22]["table"])
        t["headers"] = list(t["headers"]) + ["Answer the convention returned"]
        t["rows"] = [list(r) + ["Granted"] for r in t["rows"]]
        mod.QUESTIONS[22]["table"] = t

    def the_two_sources_are_exchanged(mod, cl):
        # Swap the two main ideas, so the source matching KC-5.1.I.C is the
        # first rather than the second and the keyed comparison reverses.
        t = dict(mod.QUESTIONS[23]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][0][1], t["rows"][1][1] = t["rows"][1][1], t["rows"][0][1]
        mod.QUESTIONS[23]["table"] = t

    def a_second_community_reports_both(mod, cl):
        # Make the first description report observances as well, so two rows
        # report both alterations and the keyed one is no longer unique.
        t = dict(mod.QUESTIONS[24]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][0][1] = ("Its customary way of making a living was disrupted and its "
                           "observances came under pressure")
        mod.QUESTIONS[24]["table"] = t

    return [
        ("a fourth petition given a question of status, so the keyed three is wrong",
         a_fourth_petition_raises_a_status_question),
        ("an answer column added, making q23's unsupportable claim supportable",
         an_answer_column_appears),
        ("the two sources' main ideas exchanged, so the keyed comparison reverses",
         the_two_sources_are_exchanged),
        ("a second community reporting both alterations, so the keyed one is not unique",
         a_second_community_reports_both),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    a56.controls(a5_3, ALLOWED, OBJECTIVE, out_of_scope="KC-5.1.I.B")
    for label, mutate in _extra_mutations():
        mod = wh_check._mutant(a5_3)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            wh_check.history_style(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as e:
            print(f"  control OK  {label}: {str(e)[:110]}")
        else:
            raise SystemExit(f"CONTROL FAILED: {label} did not raise")

a56.kc_scope(a5_3, ALLOWED, OBJECTIVE)
wh_check.run(a5_3, CLAIMS, TABLE_CHECKS, sys.argv)
