"""Key audit for AP U.S. HISTORY 1.5 Labor, Slavery, and Caste in the Spanish Colonial System.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The shared gate is
``wh_check.run``, whose checks are about history rather than about world history.

WHAT THE KEYS REST ON
---------------------
  Unit 1 Learning Objective E, the empire's growth
    shaping SOCIAL AND ECONOMIC structures OVER TIME  items 1, 12, 19, 20, 27, 28
  KC-1.2.II.B, the encomienda system marshaling
    NATIVE AMERICAN labor for plantation-based
    agriculture and the extraction of precious
    metals AND OTHER RESOURCES                        2, 3, 9, 13, 16, 17, 21, 22, 29, 30
  KC-1.2.II.C, European traders partnering with
    SOME West African groups who practiced slavery
    to FORCIBLY extract enslaved laborers, and the
    Spanish importing enslaved Africans to labor in
    plantation agriculture and mining                 4, 5, 6, 9, 14, 16, 17, 21, 22, 25, 26, 30
  KC-1.2.II.D, a caste system that INCORPORATED and
    CAREFULLY DEFINED THE STATUS OF Europeans,
    Africans, and Native Americans                    7, 8, 10, 15, 24, 27, 30
  KC-1.2.II, extensive demographic, economic, and
    social changes                                    23
  the SOC thematic focus and skill 5.A               11, 12, 27

THE SWAP RISK THIS MODULE IS BUILT AROUND. KC-1.2.II.B and KC-1.2.II.C describe
two different peoples doing overlapping work: plantation agriculture appears in
both, and metals or mining in both. So the characteristic wrong answer keeps the
PURPOSE and exchanges the PEOPLE, and it reads perfectly well. Items 9, 16, 21
and 22 each carry that exchange as a distractor, and each of those anchors names
the labor source together with the arrangement, never one alone -- the defect
``verify_e2_1.py`` shipped.

THE QUALIFIERS IN KC-1.2.II.C. The sentence says SOME West African groups WHO
PRACTICED SLAVERY, and that the extraction was FORCIBLE. Items 5, 25 and 26 key
those words, and item 25 exists because the likeliest misreading in this topic
is one the framework's own sentence settles: it describes partnership with
groups that already practiced slavery, which is neither a claim that the
practice was introduced nor a claim about West Africa as a whole.

DATA ITEMS: 16, 17 and 18.
  * Item 16's ``_T_LABOR`` is CATEGORICAL, and the shared corrupter appends
    text, which ``startswith`` and substring tests survive -- the failure a1_1
    records. So the ARRANGEMENT column is compared literally here, independently
    of the module, while the LABOR SOURCE column is left to the semantic guard,
    so the control that exchanges the two sources raises on the claim the item
    actually makes. A corrupted source cell is still caught, through the
    two-and-two count.
  * Items 17 and 18 share ``_T_ACTIVITY``, whose cells are counts. Every
    distractor is falsified against the same numbers, and the zero in the last
    row is not decoration: it mirrors the framework's own lists, since
    KC-1.2.II.B names other resources besides metals while KC-1.2.II.C names
    only plantation agriculture and mining. Seven of the nine cells are caught,
    and the two that are not were read rather than assumed: enlarging an
    encomienda count in the first or third row keeps that column above the other
    everywhere, keeps plantation agriculture ahead of mining, and leaves the
    third row's single-column pattern intact, so neither key becomes false.
  * Item 18 keys what the table CANNOT support, so its first guard is on the
    HEADERS: no column reports returns, and corrupting a cell cannot make an
    absent column present. The header guard runs BEFORE anything about the rows,
    for the reason a1_1 records -- the control adds a column, and a row
    assertion running first would raise for a reason that says nothing about the
    guard it names.

NEGATIVE CONTROLS: ``python3 verify_a1_5.py --selftest``.
"""
import sys

import cg_check as cg
import wh_check
import a1_5

ARRANGEMENT = "Arrangement the framework describes (illustrative arrangement)"
SOURCE = "Whose labor does the framework describe it drawing on?"
ACTIVITY = "Activity described (illustrative)"
ENCOMIENDA = "Workers recorded under the encomienda system"
AFRICAN = "Enslaved African workers recorded"

_EXPECTED_ARRANGEMENTS = [
    "The encomienda system supporting plantation-based agriculture",
    "The encomienda system extracting precious metals and other resources",
    "Importation by the Spanish to labor in plantation agriculture",
    "Importation by the Spanish to labor in mining",
]
_EXPECTED_ACTIVITIES = [
    "Plantation agriculture",
    "Mining of precious metals",
    "Other resource extraction",
]


def _col(table, header):
    idx = table["headers"].index(header)
    return [row[idx] for row in table["rows"]]


def q16(table, item):
    # Only the ARRANGEMENT column is compared literally. The LABOR SOURCE column
    # is left to the semantic guard, so the control that exchanges the two
    # sources raises there -- on the claim the item makes -- rather than on a
    # row-equality assertion that would say nothing about it. A corrupted source
    # cell still fails, through the two-and-two count.
    assert _col(table, ARRANGEMENT) == _EXPECTED_ARRANGEMENTS, (
        f"the arrangements are not the ones this check was written against; "
        f"got {_col(table, ARRANGEMENT)}")
    arrangements, sources = _col(table, ARRANGEMENT), _col(table, SOURCE)
    native = [a for a, s in zip(arrangements, sources)
              if s.strip().lower() == "native american labor"]
    african = [a for a, s in zip(arrangements, sources)
               if s.strip().lower() == "enslaved african labor"]
    assert len(native) == 2 and len(african) == 2, (
        f"the key names exactly two rows drawing on Native American labor against two "
        f"drawing on enslaved African labor; got {len(native)} and {len(african)}")
    # The two Native American rows must be the encomienda ones and the two
    # enslaved African rows the importation ones, or the keyed pairing is not
    # what the table says.
    assert all("encomienda" in a.lower() for a in native), (
        f"both rows marked as Native American labor must be the encomienda ones, which is "
        f"what KC-1.2.II.B describes; got {native}")
    assert not any("encomienda" in a.lower() for a in african), (
        f"no encomienda row may be marked as drawing on enslaved African labor; "
        f"got {african}")
    return (f"exactly two rows draw on Native American labor and both name the encomienda "
            f"system ({native}), against two drawing on enslaved African labor that name "
            f"importation instead")


def _activity_columns(table):
    assert cg.labels(table) == _EXPECTED_ACTIVITIES, (
        f"the activities are not the ones this check was written against; "
        f"got {cg.labels(table)}")
    return cg.col(table, ENCOMIENDA), cg.col(table, AFRICAN)


def q17(table, item):
    enc, afr = _activity_columns(table)
    assert all(n > 0 for n in enc), (
        f"'the encomienda column records no workers in one activity' must be false; "
        f"got {enc}")
    assert afr[0] > 0 and afr[1] > 0 and afr[2] == 0, (
        f"the key requires enslaved African workers in the first two activities and none "
        f"in the third; got {afr}")
    assert not all(b > a for a, b in zip(enc, afr)), \
        "'more enslaved African workers than encomienda workers in every activity' must be false"
    assert sum(1 for a, b in zip(enc, afr) if a + b > 0) > 1, \
        "'only one activity records any workers' must be false"
    return (f"encomienda workers {enc} appear in all three activities while enslaved "
            f"African workers {afr} appear in the first two only, so exactly one activity "
            f"records one column alone")


def q18(table, item):
    # HEADER GUARD FIRST, then the rows -- see the module docstring.
    joined = " ".join(str(h) for h in table["headers"]).lower()
    for word in ("profit", "cost", "value", "price", "earnings", "yield", "return"):
        assert word not in joined, (
            f"the table must report nothing about returns for the key to hold, but a "
            f"header mentions {word!r}: {table['headers']}")
    enc, afr = _activity_columns(table)
    assert all(a > b for a, b in zip(enc, afr)), (
        f"'the encomienda column records more workers in every activity' must be true; "
        f"got {enc} against {afr}")
    assert enc[0] > enc[1] and afr[0] > afr[1], (
        f"'plantation agriculture records more workers in both columns than mining' must "
        f"be true; got {enc} and {afr}")
    assert sum(1 for a, b in zip(enc, afr) if (a > 0) != (b > 0)) == 1, (
        f"'one activity records workers in one column only' must be true; got {enc} "
        f"against {afr}")
    assert all(n >= 1 for n in enc), \
        "'every activity records at least one worker in the encomienda column' must be true"
    return ("no column of the table reports returns, while the four remaining options are "
            "counts read directly off the rows")


TABLE_CHECKS = {16: q16, 17: q17, 18: q18}

CLAIMS = [
 ("The development of social and economic structures over time",
  "Unit 1 Learning Objective E gives the phrase verbatim: explain how the growth of the Spanish Empire in North America shaped the development of social and economic structures over time."),
 ("Native American labor",
  "KC-1.2.II.B states that in the encomienda system, Spanish colonial economies marshaled Native American labor; enslaved Africans appear in KC-1.2.II.C under a different arrangement."),
 ("plantation-based agriculture and to extract precious metals and other resources",
  "KC-1.2.II.B gives both purposes together, to support plantation-based agriculture and extract precious metals and other resources, and the framework adds none of the purposes the distractors name."),
 ("partnered with some West African groups who practiced slavery, to forcibly extract enslaved laborers",
  "KC-1.2.II.C's first sentence, near verbatim, including the qualifier SOME and the adverb FORCIBLY, both of which a distractor here drops or widens."),
 ("limits the claim to particular groups rather than extending it to all of West Africa",
  "KC-1.2.II.C writes SOME West African groups who practiced slavery, so the sentence describes particular partners rather than the region as a whole, in the way KC-1.1.I.C's 'some societies' limits a claim to part of a named area."),
 ("Plantation agriculture and mining",
  "KC-1.2.II.C's second sentence states that the Spanish imported enslaved Africans to labor in plantation agriculture and mining, and names no other kind of work."),
 ("incorporated, and carefully defined the status of, the diverse population",
  "KC-1.2.II.D, near verbatim; incorporation is the opposite of the exclusion one distractor offers and careful definition the opposite of leaving status open."),
 ("Europeans, Africans, and Native Americans",
  "KC-1.2.II.D names exactly these three as the diverse population the caste system incorporated and defined, which is the same trio KC-1.2 names as the groups whose contact produced the Columbian Exchange."),
 ("encomienda system with Native American labor, and Spanish importation with enslaved African labor",
  "KC-1.2.II.B places Native American labor in the encomienda system and KC-1.2.II.C has the Spanish import enslaved Africans; the leading distractor exchanges the two peoples while keeping both arrangements, so the anchor carries both pairings."),
 ("brought the empire's whole population within it and assigned each part of that population a stated position",
  "KC-1.2.II.D uses INCORPORATED and CAREFULLY DEFINED THE STATUS OF together, so dropping either verb leaves half the sentence; the Social Structures thematic focus treats such categories as created and maintained rather than merely observed."),
 ("created, maintained, challenged, and transformed",
  "The Social Structures thematic focus printed on this topic page states that social categories, roles, and practices are created, maintained, challenged, and transformed throughout American history, shaping government policy, economic systems, culture, and the lives of citizens, and KC-1.2.II.D's caste system is such a category being made."),
 ("Identify patterns among or connections between historical developments and processes",
  "Skill 5.A as printed on this topic page, and what Unit 1 Learning Objective E asks of a student connecting the encomienda system, the importation of enslaved Africans and the caste system; the distractors are skills 5.B, 3.A, 1.A and 6.B from other pages."),
 ("KC-1.2.II.B, on the encomienda system marshaling Native American labor for agriculture and extraction",
  "KC-1.2.II.B describes Spanish colonial economies marshaling Native American labor to support plantation-based agriculture and extract precious metals and other resources, which is what a grant of a district's labor for fields and mine would be; KC-1.2.II.C's arrangement rests on importation instead."),
 ("KC-1.2.II.C, on European traders partnering with some West African groups to forcibly extract enslaved laborers",
  "KC-1.2.II.C's first sentence describes exactly that transaction and destination; the encomienda system of KC-1.2.II.B draws on labor already in the Americas. The anchor carries the clause as well as the code because the same key concept's second sentence is a different arrangement."),
 ("KC-1.2.II.D, on the caste system that incorporated and carefully defined the status",
  "KC-1.2.II.D describes a caste system that incorporated, and carefully defined the status of, the empire's diverse population, which is what a register sorting inhabitants by descent and fixing obligations records."),
 ("two encomienda rows draw on Native American labor, and the two importation rows on enslaved African labor",
  "Recomputed in q16 from the table alone. KC-1.2.II.B assigns the encomienda system Native American labor and KC-1.2.II.C has the Spanish import enslaved Africans, and the anchor carries both halves because the leading distractor exchanges the sources while keeping every arrangement."),
 ("only the encomienda column records workers in other resource extraction",
  "Recomputed in q17 from the table alone, with every distractor falsified on the same counts. The pattern mirrors the framework's own lists: KC-1.2.II.B names precious metals AND OTHER RESOURCES while KC-1.2.II.C names only plantation agriculture and mining."),
 ("more profitable to the Spanish than the other",
  "Recomputed in q18: no column of the table reports returns, so relative profit is the one claim of the five it cannot reach. KC-1.2.II.B and KC-1.2.II.C describe what labor was used for and where it came from and weigh neither arrangement's yield against the other's."),
 ("developed across the period rather than at a single moment",
  "Unit 1 Learning Objective E asks how the empire's growth shaped the development of social and economic structures OVER TIME, and the Social Structures thematic focus calls such categories created, maintained, challenged, and transformed rather than settled once."),
 ("reach the arrangement of society as well as the organization of production",
  "Unit 1 Learning Objective E names social AND economic structures, and this topic supplies both: KC-1.2.II.B and KC-1.2.II.C describe how production was organized and by whose labor, KC-1.2.II.D how status was assigned."),
 ("labor directed to plantation agriculture and to the working of metals",
  "KC-1.2.II.B has Native American labor supporting plantation-based agriculture and extracting precious metals, and KC-1.2.II.C has enslaved Africans laboring in plantation agriculture and mining, so the two sentences share purposes while differing in whose labor they describe -- which is the connection skill 5.A asks students to identify."),
 ("marshals the labor of people already in the Americas, while the other rests on people the Spanish imported",
  "KC-1.2.II.B describes labor marshaled within the Americas and KC-1.2.II.C describes importation across the Atlantic; their purposes overlap rather than divide, so the anchor carries both halves of the contrast."),
 ("Demographic, economic, and social",
  "KC-1.2.II names extensive demographic, economic, and social changes; 'social, cultural, and political' is KC-1.2's list, and mistaking one for the other is the likeliest confusion in this unit."),
 ("incorporating and defining the status of the population, while labor is the subject of the two sentences before it",
  "KC-1.2.II.D is a statement about position rather than about work, and KC-1.2.II.B and KC-1.2.II.C are the sentences that describe labor. The anchor carries both clauses because the item turns on the boundary between them."),
 ("partnered with some West African groups who practiced slavery",
  "KC-1.2.II.C describes partnership with groups that already practiced slavery, which is neither a claim that the practice was introduced nor a claim about West Africa as a whole; reading either into the sentence adds something the framework does not say."),
 ("the people taken did not go by their own choice",
  "KC-1.2.II.C's adverb FORCIBLY attaches to the extraction of enslaved laborers for the Americas and settles that the people taken did not consent; the same sentence names West African partners and the Americas as the destination."),
 ("made and maintained by people rather than as simply given",
  "The Social Structures thematic focus calls social categories created, maintained, challenged, and transformed, and KC-1.2.II.D's verb DEVELOPED says the Spanish made the caste system rather than found it; Unit 1 Learning Objective E joins those social structures to the economic ones."),
 ("Mutual misunderstandings between Europeans and Native Americans",
  "That is KC-1.2.III.A, printed on the topic about cultural interactions rather than here; the other four options are KC-1.2.II.B, KC-1.2.II.C in both its sentences and KC-1.2.II.D, which are the whole of this topic's Required Course Content."),
 ("carries the extraction past precious metals to resources the sentence does not list one by one",
  "KC-1.2.II.B says the encomienda system extracted precious metals AND OTHER RESOURCES, widening what was taken without enumerating it, and it is the one purpose here that KC-1.2.II.C's plantation agriculture and mining do not match."),
 ("obtained through partnerships with some West African groups who practiced slavery",
  "Collects KC-1.2.II.B, KC-1.2.II.C and KC-1.2.II.D in the framework's own terms and adds nothing; each rejected option either invents European indentured servants, narrows the caste system to Europeans, or drops one of the three sentences Unit 1 Learning Objective E rests on."),
]


def _extra_mutations():
    def profit_column_appears(mod, cl):
        # q18 keys what the table cannot support; a column reporting returns
        # would make the keyed claim reachable and the item wrong.
        t = dict(mod.QUESTIONS[16]["table"])
        t["headers"] = list(t["headers"]) + ["Profit recorded to the Spanish"]
        t["rows"] = [list(r) + ["High"] for r in t["rows"]]
        mod.QUESTIONS[16]["table"] = t
        mod.QUESTIONS[17]["table"] = t

    def labor_sources_exchanged(mod, cl):
        # Flip which arrangements draw on which labor, so the keyed pairing stops
        # being the framework's. Every column still holds the same multiset of
        # values, so no single-cell corruption can express this.
        t = dict(mod.QUESTIONS[15]["table"])
        flip = {"Native American labor": "Enslaved African labor",
                "Enslaved African labor": "Native American labor"}
        t["rows"] = [[a, flip[s]] for a, s in t["rows"]]
        mod.QUESTIONS[15]["table"] = t

    return [
        ("a profit column added, making q18's unsupportable claim supportable",
         profit_column_appears, "must report nothing about returns"),
        ("the two labor sources exchanged, so the keyed pairing is no longer the "
         "framework's",
         labor_sources_exchanged, "must be the encomienda ones"),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    import contextlib
    import io
    for label, mutate, expect in _extra_mutations():
        mod = wh_check._mutant(a1_5)
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

wh_check.run(a1_5, CLAIMS, TABLE_CHECKS, sys.argv)
