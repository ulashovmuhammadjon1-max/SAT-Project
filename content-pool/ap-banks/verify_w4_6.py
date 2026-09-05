"""Key audit for AP WORLD HISTORY: MODERN 4.6 Internal and External Challenges to State Power from 1450 to 1750.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code, for a human
to audit. `wh_check` refuses any claim or `why` citing neither a KC code nor a
Learning Objective.

EVERYTHING SHARED IS SHARED. `wh_check.run` supplies the structural gate
(`cg_check.check`), the notation gate (`es_check.style`), the citation rule, the
figure-language ban, and a self-test that rotates all thirty keys, breaks all
thirty anchors, corrupts every cell of every table and asserts WHICH message came
back each time. `wh_stimulus` supplies the marked-stimulus gate.

THIS TOPIC PRINTS ONLY TWO SENTENCES, and that is the constraint the module is
built around rather than a gap in it:

  KC-4.3.III.iii  State expansion and centralization led to resistance from an
                  array of social, political, and economic groups on a LOCAL
                  level.
  KC-5.3.III.C    Enslaved persons challenged existing authorities in the
                  AMERICAS through organized resistance.

Everything else beside the topic is the two headings of illustrative examples
and suggested skill 4.B. So the items lean on those examples, on the causal
direction, and on the contextualization skill, rather than inventing detail the
framework does not carry. KC-5.3.III.C genuinely bears a unit 5 code while being
printed in unit 4; that is the CED's own cross-reference and the code is cited
as printed.

THE THREE WORDS THAT CARRY THE KEYS. "Local" (q2), "the Americas" (q4, q13) and
"an array of social, political, and economic groups" (q3, q24) are each a single
word or phrase whose replacement leaves a fluent and false sentence. q13's
anchor carries both the wrong continent AND the right one, because the true
statement is itself one of its distractors.

WHAT NO ITEM ASSERTS. The framework dates none of these episodes, names no ruler
they faced, gives no size or duration for any of them, and -- this is what q25 is
built on -- says NOTHING about whether any resistance succeeded. Both a claim of
success and a claim of failure would need a source outside the CED, so the key
there is that the claim goes beyond the framework rather than that it is refuted
by it. q26 keys the comparison of two episodes' size as the same kind of
overreach.

NEGATIVE CONTROL: `python3 verify_w4_6.py --selftest`.
"""
import sys

import cg_check as cg
import wh_check as wh
import wh_stimulus as ws

import w4_6

WHO = "Who is recorded as resisting"
WHAT = "What they are recorded as resisting"
OFFICES = "New offices of the central government in the province"
DISTURB = "Local disturbances recorded in the province"
HEADING = "Heading it is printed under"


def q19(table, item):
    """Three of the four episodes are local groups resisting the state's reach."""
    labs = cg.labels(table)
    assert labs == ["Episode %d" % n for n in range(1, 5)], \
        f"the four episodes the key counts are not the rows: {labs}"
    # An episode qualifies only if BOTH halves hold: a social, political or
    # economic group AND a grievance directed at the central state. Each cell is
    # parsed against a closed vocabulary rather than searched for a substring,
    # so a corrupted cell no longer parses and the check fails rather than
    # quietly passing -- the lesson 4.3's q19 taught.
    group_kind = {
        "a local farming community": "economic and social",
        "a group of provincial nobles": "political",
        "the merchants of a market town": "economic",
        "a troupe of travelling musicians": None,
    }
    against_state = {
        "the extension of the central government's tax demands": True,
        "the gathering of authority into the capital": True,
        "new controls imposed by the central treasury": True,
        "a change in the date of a village festival": False,
    }
    qualifies = []
    for row in table["rows"]:
        who, what = cg.normalize(row[1]), cg.normalize(row[2])
        assert who in group_kind, f"the group {who!r} is outside this item's vocabulary"
        assert what in against_state, f"the grievance {what!r} is outside this item's vocabulary"
        qualifies.append(bool(group_kind[who]) and against_state[what])
    assert sum(qualifies) == 3, \
        f"the key needs three qualifying episodes; got {sum(qualifies)} from {qualifies}"
    kinds = {group_kind[cg.normalize(r[1])] for r in table["rows"] if group_kind[cg.normalize(r[1])]}
    assert len(kinds) >= 2, (
        "KC-4.3.III.iii names an ARRAY of kinds of group, so the qualifying rows must not all "
        f"be of one kind; got {kinds}")
    # and every distractor false on the same rows
    assert not all(qualifies), "'all four episodes' must be false"
    assert any(qualifies), "'none of the episodes' must be false"
    assert sum(qualifies) not in (1, 2), "the one- and two-episode readings must both be false"
    return (f"three of the four rows pair a social, political or economic group with a grievance "
            f"against the central state, drawn from {sorted(kinds)}, and the fourth is a festival "
            "date that is neither")


def q20(table, item):
    """Central offices and local disturbances rise together, every decade."""
    offices, disturbances = cg.col(table, OFFICES), cg.col(table, DISTURB)
    assert all(offices[i + 1] > offices[i] for i in range(len(offices) - 1)), \
        f"new central offices must rise at every step; got {offices}"
    assert all(disturbances[i + 1] > disturbances[i] for i in range(len(disturbances) - 1)), \
        f"local disturbances must rise at every step; got {disturbances}"
    # and every distractor false on the same numbers
    assert not any(disturbances[i + 1] < disturbances[i] for i in range(len(disturbances) - 1)), \
        "'local disturbances fall' must be false"
    assert not any(offices[i + 1] < offices[i] for i in range(len(offices) - 1)), \
        "'new central offices fall' must be false"
    assert len(set(offices)) > 1 and len(set(disturbances)) > 1, \
        "'neither figure changes' must be false"
    return (f"new central offices read {offices} and local disturbances {disturbances}, both "
            "strictly increasing across the four decades")


def q21(table, item):
    """Two illustrative examples sit under each of the framework's two headings."""
    examples = cg.labels(table)
    assert len(examples) == 4 and len(set(examples)) == 4, \
        f"the table must list four distinct examples; got {examples}"
    local, enslaved = [], []
    for row in table["rows"]:
        heading = cg.normalize(row[1])
        if heading == "local resistance":
            local.append(row[0])
        elif heading == "resistance of enslaved persons":
            enslaved.append(row[0])
        else:
            raise AssertionError(
                f"{row[0]!r} is printed under {heading!r}, which is neither of the two headings "
                "the framework prints beside this topic")
    assert len(local) == 2 and len(enslaved) == 2, \
        f"the key needs two under each heading; got {len(local)} and {len(enslaved)}"
    for name in enslaved:
        assert "enslaved" in cg.normalize(name) or "maroon" in cg.normalize(name), (
            f"{name!r} is filed under the resistance of enslaved persons but names neither "
            "enslaved persons nor a Maroon society")
    assert len({cg.normalize(r[1]) for r in table["rows"]}) == 2, \
        "'the four examples are printed under four different headings' must be false"
    return (f"two rows, {local}, are printed under local resistance and two, {enslaved}, under "
            "the resistance of enslaved persons, so the four fall under exactly two headings")


CLAIMS = [
 ("Resistance from an array of social, political, and economic groups",
  "KC-4.3.III.iii states that state expansion and centralization led to resistance from an array of social, political, and economic groups on a local level. Surrender of privileges, disappearance of local government, agreement to stop expanding and transfer of authority are each the opposite of that resistance."),
 ("The local level",
  "KC-4.3.III.iii places the resistance on a local level, which is the last phrase of the sentence. Relations between empires belong to KC-4.3.III.i and KC-4.3.III.ii, which concern rivalries and conflict between states rather than resistance inside one."),
 ("Social, political, and economic groups",
  "KC-4.3.III.iii describes resistance from an array of social, political, and economic groups on a local level. The word array and the three adjectives are the framework's own, so narrowing the resistance to a single kind of group misreports it."),
 ("In the Americas",
  "KC-5.3.III.C states that enslaved persons challenged existing authorities in the Americas through organized resistance. KC-4.2.II.B describes the continuation of enslavement in Africa but records no organized resistance there, so relocating the statement asserts what the framework does not."),
 ("Organized resistance",
  "KC-5.3.III.C names organized resistance as the means by which enslaved persons challenged existing authorities in the Americas. No petition, purchase, office or treaty appears in that statement."),
 ("development of state power from 1450 to 1750",
  "Unit 4: Learning Objective L asks students to explain the effects of the development of state power from 1450 to 1750, and KC-4.3.III.iii supplies one such effect. Maritime technology is Learning Objective A, the Columbian Exchange Learning Objective D, and joint-stock companies KC-4.1.IV.C."),
 ("Pueblo Revolts, the Fronde, and Cossack revolts",
  "The illustrative examples beside Unit 4: Learning Objective L print the Pueblo Revolts, the Fronde, Cossack revolts, the Maratha conflict with the Mughals, Ana Nzinga's resistance and Metacom's War under local resistance, illustrating KC-4.3.III.iii. Maroon societies sit under the separate heading for the resistance of enslaved persons."),
 ("Ndongo and Matamba",
  "The illustrative examples print Ana Nzinga's resistance, as ruler of Ndongo and Matamba, among the episodes of local resistance illustrating KC-4.3.III.iii. The Asante and the Kongo appear at KC-4.3.II.A.ii as African states whose influence grew through trade, which is a different statement about a different process."),
 ("Metacom's War, also given as King Philip's War",
  "The illustrative examples for this topic print Metacom's War with King Philip's War in brackets, among the episodes of local resistance illustrating KC-4.3.III.iii. Each rejected option pairs two separate entries from that same list as though they were one."),
 ("The Mughal Empire",
  "The illustrative examples name the Maratha conflict with the Mughals among the episodes of local resistance illustrating KC-4.3.III.iii. The other four empires appear at KC-4.3.II.B and in the state rivalries beside topic 3.1, but none is paired with the Marathas."),
 ("In the Caribbean and Brazil",
  "The illustrative examples print the establishment of Maroon societies in the Caribbean and Brazil under the heading for the resistance of enslaved persons, illustrating KC-5.3.III.C. Resistance of enslaved persons in North America is a separate entry under the same heading."),
 # Both clauses: the distractor exchanges the two examples between the two
 # headings, so an anchor naming one example alone matches it.
 ("Fronde under local resistance, and Maroon societies under the resistance of enslaved persons",
  "The illustrative examples print the Fronde among the episodes of local resistance illustrating KC-4.3.III.iii, and the establishment of Maroon societies in the Caribbean and Brazil under the separate heading illustrating KC-5.3.III.C. The rejected sortings exchange the headings or collapse them into one."),
 # Both clauses: the true statement is itself a distractor, so the anchor must
 # carry the wrong continent AND the right one it displaces.
 ("in Africa through organized resistance rather than in the Americas",
  "KC-5.3.III.C places the organized resistance of enslaved persons in the Americas, so moving it to Africa is the error. KC-4.2.II.B's account of enslavement continuing in Africa is what makes the mistaken statement read plausibly, but it records no organized resistance there."),
 ("State expansion and centralization across the period",
  "Suggested skill 4.B asks how a specific development is situated within a broader historical context, and KC-4.3.III.iii supplies the context: state expansion and centralization led to resistance from an array of social, political, and economic groups on a local level. An officer's name, the weather, a horse count and a market day are details of the episode rather than the process around it."),
 ("expansion and centralization of state power",
  "KC-4.3.III.iii makes state expansion and centralization the cause and local resistance the effect, which is the causation this topic's reasoning process asks students to trace. The rejected options are KC-4.1.V.B, KC-4.3.II, KC-4.1.IV.C and KC-4.1.II.A, none of which the framework connects to local revolt."),
 # Both clauses: the item joins two sentences, and a distractor keeps the
 # plantation half while reversing the resistance half.
 ("increased the demand for enslaved labor in the Americas, and enslaved persons there challenged existing authorities",
  "KC-4.2.II.C says the growth of the plantation economy increased the demand for enslaved labor in the Americas, and KC-5.3.III.C says enslaved persons challenged existing authorities in the Americas through organized resistance. Each rejected option reverses or denies one of those sentences."),
 ("state expansion and centralization drew resistance from local groups",
  "KC-4.3.III.iii says state expansion and centralization led to resistance from an array of social, political, and economic groups on a local level, and a farming district protesting a doubled levy under closer central control is such a group resisting. The rejected options are KC-5.3.III.C, KC-4.3.III.ii, KC-4.1.IV and KC-4.3.I.A."),
 ("enslaved persons in the Americas challenged existing authorities",
  "KC-5.3.III.C says enslaved persons challenged existing authorities in the Americas through organized resistance, and the illustrative examples print the establishment of Maroon societies in the Caribbean and Brazil under that heading. The rejected options are KC-4.2.II.B, KC-4.3.III.iii, KC-4.2.II.A and KC-4.3.II.A.i."),
 ("Three, because the framework names social, political, and economic groups",
  "KC-4.3.III.iii names an array of social, political, and economic groups resisting state expansion and centralization on a local level. Recomputed in q19 above: three rows pair such a group with a grievance against the central state, and the festival date is neither."),
 ("Both the number of new central offices and the number of local disturbances rise",
  "KC-4.3.III.iii says state expansion and centralization led to resistance from local groups. Recomputed in q20 above: both columns rise at every step across the four decades, so neither swapped reading and neither no-change reading holds."),
 ("Two of the listed examples are printed as local resistance and two as resistance of enslaved persons",
  "The framework prints six episodes under local resistance, illustrating KC-4.3.III.iii, and two entries under the resistance of enslaved persons, illustrating KC-5.3.III.C. Recomputed in q21 above: the four rows split two and two between exactly those headings."),
 ("resistance to state expansion and centralization, the other resistance by enslaved persons",
  "Local resistance illustrates KC-4.3.III.iii, on social, political, and economic groups resisting state expansion and centralization, while the resistance of enslaved persons illustrates KC-5.3.III.C, on enslaved persons challenging existing authorities in the Americas. Conflicts between states are KC-4.3.III.i and KC-4.3.III.ii, which belong to other topics."),
 ("array of social, political, and economic groups resisting on a local level",
  "KC-4.3.III.iii describes resistance from an array of social, political, and economic groups on a local level, and the illustrative examples run from the Fronde to the Pueblo Revolts to Cossack revolts. Narrowing the resistance to one group or one region contradicts both the sentence and the list printed beside it."),
 ("goes beyond the framework, which states that resistance followed expansion and centralization without saying how any episode ended",
  "KC-4.3.III.iii says state expansion and centralization led to resistance and stops there, and KC-5.3.III.C records that enslaved persons challenged existing authorities without stating an outcome. Both a claim of success and a claim of failure would need a source outside the framework, so the key is the overreach rather than a refutation."),
 ("involved more people than another",
  "The four rejected statements are KC-4.3.III.iii, KC-5.3.III.C and the illustrative examples almost verbatim. The framework gives no size, date or duration for any episode and compares none with another, so a claim about numbers involved would need an outside source."),
 ("internal and external factors contribute to state formation, expansion, and decline",
  "The Governance thematic focus printed with this topic says a variety of internal and external factors contribute to state formation, expansion, and decline, and KC-4.3.III.iii supplies an internal factor in the resistance that met expansion and centralization. The rejected statements are the other four thematic focuses of the course."),
 ("local disturbances in the years a province came under closer central administration",
  "KC-4.3.III.iii makes state expansion and centralization the cause of local resistance, so evidence for it has to put the two together in one place and time. Silver, crops, shipbuilding and company shares bear on KC-4.1.IV, KC-4.1.V, KC-4.1.II.A and KC-4.1.IV.C instead."),
 # Both clauses: the two headings are the answer, and each half alone appears
 # inside one of the rejected pairs.
 ("Local resistance to state expansion and centralization, and organized resistance by enslaved persons in the Americas",
  "KC-4.3.III.iii and KC-5.3.III.C are the two statements printed beside this topic, and the illustrative examples are grouped under exactly those two headings. The rejected pairs are KC-4.3.III.i with KC-4.3.III.ii, KC-4.3.II.A.i with KC-4.1.IV.C, KC-4.1.V, and KC-4.2.II.A with KC-4.1.IV."),
 ("state expansion and centralization led to that resistance",
  "KC-4.3.III.iii states the direction of the causation in its own words, with expansion and centralization leading to resistance, which is why Unit 4: Learning Objective L asks for the effects of the development of state power. Each rejected option reverses or denies that link."),
 ("resisted at a local level, and in the Americas enslaved persons challenged existing authorities",
  "The keyed sentence joins KC-4.3.III.iii on local resistance to state expansion and centralization with KC-5.3.III.C on the organized resistance of enslaved persons in the Americas. Each rejected version denies the resistance, narrows it to one group or region, exchanges the two continents, or asserts an outcome the framework never states."),
]

TABLE_CHECKS = {19: q19, 20: q20, 21: q21}

if __name__ == "__main__" and "--selftest" in sys.argv:
    ws.controls(w4_6)

ws.marked_stimulus(w4_6)
wh.run(w4_6, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
