"""Key audit for AP WORLD HISTORY: MODERN 8.6 Newly Independent States.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code or Learning
Objective, for a human to audit. `wh_check` refuses any claim or `why` that
cites neither, because a key traceable only to an author's knowledge of the
twentieth century cannot be checked by anyone reading this bank later.

WHERE A DISTRACTOR IS THE SWAP OF THE KEY, THE ANCHOR CARRIES BOTH CLAUSES.
Seven items here are built on a reversal a prepared student could believe:

  q5   migration maintaining ties swapped for migration severing them
  q8   "in some cases" swapped for "never"
  q17  the NOT-supported item, where the key is deliberately the false claim
  q18  ties maintained read as an imperial relationship ended
  q19  "in some cases" swapped for "always" and for "never"
  q21  new states from redrawn boundaries swapped for consolidation
  q24  colonies and metropoles exchanged as the direction of settlement

For each of those the anchor spans the whole relation and not just one noun, so
an anchor that matched the swapped distractor would fail the gate rather than
pass it. That defect is on record in `verify_e2_1.py`.

TWO QUALIFIERS CARRY THIS TOPIC and five claims below say so. KC-6.2.III.A.ii
says redrawn boundaries led to conflict and displacement IN SOME CASES;
KC-6.3.I.C says newly independent governments OFTEN took a strong role in
guiding economic life. Flattening either into "always" would teach the opposite
of the framework's own sentence, and it is the easiest error to make in a topic
whose two most famous illustrative cases are cases of conflict. The three data
questions exist to make those quantifiers countable, not to assert real
frequencies: each table is labelled hypothetical in its stem.

CONTESTED GROUND. KC-6.2.III.A.ii names the Partition of India and the creation
of the state of Israel. The claims for the two items that mention them assert
only what that sentence asserts -- that redrawn boundaries led to conflict as
well as population displacement and/or resettlements. No key assigns
responsibility, endorses a territorial claim or states a number of people
displaced. Those are live disputes, and a bank that settled one would be
teaching a position rather than the course.

WHAT THIS CANNOT DO: it cannot tell whether the history is right. It gates
structure, key/anchor agreement, notation, the absence of figure language, the
presence of a citation, and the arithmetic of the three data questions. The
history is gated by the claims below and by the rule in HISTORY_BRIEF.md that a
key must trace to a sentence in the CED.

NEGATIVE CONTROL: `python3 verify_w8_6.py --selftest`. It rotates all thirty
keys, breaks all thirty anchors, corrupts every cell of every table, injects
each banned notation form, injects figure language into a stem and a choice,
strips the citation from a why and from a claim, duplicates a choice, thins a
why and makes a why name an option by letter -- and asserts not merely that
something raised but WHICH message came back. It also runs positive controls,
so a gate that rejected everything would fail here rather than look thorough.
"""
import sys

import cg_check as cg
import wh_check as wh
import w8_6

T_NEWSTATES = w8_6._T_NEWSTATES
T_STATEROLE = w8_6._T_STATEROLE
T_MIGRATION = w8_6._T_MIGRATION

CREATED = "New states created after a colonial withdrawal"
WITH_CONFLICT = "Of those, accompanied by conflict or population displacement"
WITHOUT_CONFLICT = "Of those, not so accompanied"
SURVEYED = "States surveyed"
STRONG = "Of those, governments taking a strong role in guiding economic life"
LIMITED = "Of those, governments taking a limited role"
RESIDENTS = "Residents born in a former colony of that metropole"
CITIES = "Of those, living in its largest cities"
ELSEWHERE = "Of those, living elsewhere in the metropole"


def _parts_sum_to_whole(table, whole, parts, what):
    """Every row's parts must total its whole.

    This is what makes the negative control mean anything on these tables. The
    corruption in `es_check` only ever makes a number LARGER, so a check of the
    form "this count is above zero" is monotone and can never fail: it reads the
    table without being able to object to anything in it. Sibling module 8.5
    shipped a first draft whose table check caught 1 of 12 corrupted cells for
    exactly that reason. Each row here states a whole and the two parts it was
    divided into, and every stem says the record placed each case under exactly
    one of the two headings, so the sum is a property of the data as the
    question describes it rather than a contrivance.
    """
    labs = cg.labels(table)
    totals = cg.col(table, whole)
    cols = [cg.col(table, p) for p in parts]
    for i, lab in enumerate(labs):
        got = sum(c[i] for c in cols)
        assert got == totals[i], (
            f"{lab}: the {what} split into {[c[i] for c in cols]} totals {got}, but the "
            f"row states {totals[i]} in all -- the parts do not sum to the whole")


def q4(table, item):
    """New states in every decade, and only some accompanied by conflict."""
    decades = cg.labels(table)
    made = dict(zip(decades, cg.col(table, CREATED)))
    with_c = dict(zip(decades, cg.col(table, WITH_CONFLICT)))
    without = dict(zip(decades, cg.col(table, WITHOUT_CONFLICT)))
    assert decades == ["1940s", "1950s", "1960s", "1970s"], \
        f"the key speaks of every decade recorded; the rows are {decades}"
    _parts_sum_to_whole(table, CREATED, [WITH_CONFLICT, WITHOUT_CONFLICT], "new states")
    for d in decades:
        assert made[d] > 0, f"the key needs new states in {d}; the row reads {made[d]}"
        assert with_c[d] > 0 and without[d] > 0, (
            f"the key needs some but not all of {d}'s new states accompanied by conflict; "
            f"the row reads {with_c[d]} with and {without[d]} without")
    # every distractor false on the same numbers
    assert any(without[d] > 0 for d in decades), \
        "'every new state was accompanied by conflict or displacement' must be false"
    assert any(with_c[d] > 0 for d in decades), \
        "'no new state was accompanied by conflict or displacement' must be false"
    most_made = cg.ranked(table, CREATED)[0]
    most_conflict = cg.ranked(table, WITH_CONFLICT)[0]
    assert most_made != most_conflict, (
        f"'the decade creating the most new states also recorded the most accompanied by "
        f"conflict' must be false, but both are {most_made}")
    assert cg.ranked(table, CREATED, reverse=False)[0] != "1960s", \
        "'fewer new states were created in the 1960s than in any other decade' must be false"
    return (f"new states {made} split into {with_c} accompanied and {without} not, summing "
            f"to the stated totals; the decade of most states ({most_made}) is not the "
            f"decade of most conflict ({most_conflict}), and all four distractors "
            f"recompute false")


def q10(table, item):
    """The strong role is the more common of the two in every region."""
    labs = cg.labels(table)
    surveyed = dict(zip(labs, cg.col(table, SURVEYED)))
    strong = dict(zip(labs, cg.col(table, STRONG)))
    limited = dict(zip(labs, cg.col(table, LIMITED)))
    _parts_sum_to_whole(table, SURVEYED, [STRONG, LIMITED], "states surveyed")
    for lab in labs:
        assert strong[lab] > limited[lab], (
            f"the key needs the strong role to outnumber the limited role in {lab}; the "
            f"row reads {strong[lab]} strong against {limited[lab]} limited")
    # every distractor false on the same numbers
    assert not all(limited[l] > strong[l] for l in labs), \
        "'more governments took a limited role in every region' must be false"
    assert strong["Caribbean"] > 0, \
        "'no government surveyed in the Caribbean took a strong role' must be false"
    assert cg.ranked(table, SURVEYED)[0] != "Asia", \
        "'Asia surveyed more states than any other region' must be false"
    assert len(set(surveyed.values())) > 1, \
        "'the three regions surveyed the same number of states' must be false"
    return (f"the strong role {strong} outnumbers the limited role {limited} in every "
            f"region, the two summing to the stated totals {surveyed}, and all four "
            f"distractors recompute false")


def q16(table, item):
    """City residence is the majority in every metropole -- KC-6.2.III.B's 'usually'."""
    labs = cg.labels(table)
    total = dict(zip(labs, cg.col(table, RESIDENTS)))
    city = dict(zip(labs, cg.col(table, CITIES)))
    other = dict(zip(labs, cg.col(table, ELSEWHERE)))
    _parts_sum_to_whole(table, RESIDENTS, [CITIES, ELSEWHERE], "residents recorded")
    for lab in labs:
        assert city[lab] > 0.5 * total[lab], (
            f"the key needs a majority in the largest cities of {lab}; the row reads "
            f"{city[lab]} of {total[lab]}")
    # every distractor false on the same numbers
    assert not all(city[l] < 0.5 * total[l] for l in labs), \
        "'fewer than half lived in the largest cities in each metropole' must be false"
    assert total["Metropole three"] <= total["Metropole two"], \
        "'metropole three recorded more such residents than metropole two' must be false"
    assert any(other[l] > 0 for l in labs), \
        "'none of the recorded residents lived outside the largest cities' must be false"
    assert len(set(total.values())) > 1, \
        "'the three metropoles recorded the same number' must be false"
    return (f"city residents {city} against totals {total}, a majority in every metropole, "
            f"with {other} living elsewhere and the parts summing to the stated wholes; "
            f"all four distractors recompute false")


TABLE_CHECKS = {4: q4, 10: q10, 16: q16}

CLAIMS = [
 ("redrawing of political boundaries after the withdrawal of former colonial authorities led to the creation of new states",
  "KC-6.2.III.A.i states that the redrawing of political boundaries after the withdrawal of former colonial authorities led to the creation of new states. One imperial province becoming three sovereign states between 1935 and 1965 is that process recorded in a gazetteer, and the framework places the withdrawal before the new states rather than after them."),

 ("frontiers followed lines drawn by the departing colonial authority",
  "KC-6.2.III.A.i makes the departing colonial authority's redrawn boundaries the origin of the new states, so evidence that the lines were that authority's own refutes a claim that the peoples inside settled them. Skill 3.D, the suggested skill for this topic, asks which evidence refutes a source's argument."),

 ("newly independent government taking a strong role in guiding economic life to promote development",
  "KC-6.3.I.C states that in newly independent states after World War II, governments often took on a strong role in guiding economic life to promote development. State ownership, a national investment board and sectoral output targets are that strong role in a document; each distractor has the state doing less rather than more."),

 ("some but not all were accompanied by conflict or displacement",
  "KC-6.2.III.A.i gives the creation of new states from redrawn boundaries and KC-6.2.III.A.ii adds that this led to conflict and displacement IN SOME CASES. The record is hypothetical, and the keyed conclusion with the falsity of every distractor is recomputed from the table alone in q4 above."),

 ("usually in the major cities, maintained cultural and economic ties between colony and metropole",
  "KC-6.2.III.B states that the migration of former colonial subjects to imperial metropoles, usually in the major cities, maintained cultural and economic ties between the colony and the metropole even after the dissolution of empires. A distractor has the same migration severing those ties, so the anchor carries the destination and the maintenance together."),

 ("often took a strong role in guiding economic life to promote development",
  "KC-6.3.I.C states that governments in newly independent states after World War II often took on a strong role in guiding economic life to promote development, which is a change in economic arrangements rather than only in who governed. Unit 8 Learning Objective H asks for the economic changes and continuities resulting from decolonization."),

 ("Israel, Cambodia, and Pakistan",
  "The CED prints Israel, Cambodia and Pakistan beside KC-6.2.III.A.i and KC-6.2.III.A.ii as illustrative examples of states created by the redrawing of political boundaries. The other lists are illustrative examples the framework prints beside governments guiding economic life and beside statements in other topics."),

 ("conflict and displacement in some cases, so not in every case",
  "KC-6.2.III.A.ii states that the redrawing of political boundaries IN SOME CASES led to conflict as well as population displacement and/or resettlements. The qualifier rules out the universal claim and equally rules out the opposite absolute, so the correction must preserve the middle position."),

 ("remittances and correspondence sent from the metropole to the former colony",
  "KC-6.2.III.B states that migration to imperial metropoles maintained cultural and economic ties between the colony and the metropole even after the dissolution of empires. Remittances and correspondence are those maintained ties as evidence, whereas a count of city arrivals bears on where migrants settled rather than on whether the connection continued."),

 ("more governments took a strong role in guiding economic life than took a limited role",
  "KC-6.3.I.C states that newly independent governments OFTEN took on a strong role in guiding economic life to promote development. A survey in which the strong role is the more common of the two everywhere is that word made countable; the figures are hypothetical and are recomputed from the table alone in q10 above."),

 ("presents as natural was inherited from a colonial administrative decision",
  "KC-6.2.III.A.i states that the redrawing of political boundaries after the withdrawal of former colonial authorities led to the creation of new states, which makes colonial administrative lines the origin of many later frontiers. Skill 3.D asks how one source's evidence bears on another source's argument."),

 ("strong role newly independent governments often took in guiding economic life to promote development",
  "KC-6.3.I.C is the sentence founding state industries to cut import dependence belongs to. Free-market policies, multinational corporations and regional trade agreements belong to KC-6.3.I.D and KC-6.3.II.B in Topic 9.4 and describe the state doing less rather than more, which is why they are the near-miss distractors here."),

 ("Conflict as well as population displacement and resettlements",
  "KC-6.2.III.A.ii states that the redrawing of political boundaries in some cases led to conflict as well as population displacement and/or resettlements. The framework names conflict and the movement of people as the further consequences and names no reunification, reoccupation or transfer to international administration."),

 ("governments of newly independent states often took a strong role",
  "KC-6.3.I.C states that governments in newly independent states after World War II often took on a strong role in guiding economic life, which contradicts the editorial's supporting claim about what every other such state was doing. Skill 3.D asks which evidence refutes a source's argument, as distinct from evidence bearing only on its author's credibility."),

 ("redrawing of political boundaries led to conflict as well as population displacement or resettlement",
  "KC-6.2.III.A.ii states that the redrawing of political boundaries in some cases led to conflict as well as population displacement and/or resettlements, including those related to the Partition of India and the creation of the state of Israel. That sentence is the whole of what the framework asserts about these two cases; the key assigns no responsibility to any party and states no figure."),

 ("more than half of the recorded residents lived in its largest cities",
  "KC-6.2.III.B states that the migration of former colonial subjects to imperial metropoles was USUALLY in the major cities. An estimate in which city residence is the majority in every metropole is that word made countable; the figures are hypothetical and are recomputed from the table alone in q16 above."),

 ("uniformly withdrew from economic life and left development to private firms",
  "KC-6.3.I.C states that governments in newly independent states after World War II often took on a strong role in guiding economic life to promote development, so a uniform withdrawal reverses that sentence and is the statement the framework does not support. The item asks which claim is NOT supported, so the anchor is pinned to the false statement deliberately; the other four restate KC-6.3.I.C, KC-6.2.III.A.i, KC-6.2.III.A.ii and KC-6.2.III.B."),

 ("maintaining ties between colony and metropole rather than ending them",
  "KC-6.2.III.B states that migration to imperial metropoles maintained cultural and economic ties EVEN AFTER the dissolution of empires. The official reads the same migration as evidence of a relationship ended, which the framework's own clause qualifies, so the anchor carries both the maintenance and the reading it displaces."),

 ("in some cases rather than in all",
  "KC-6.2.III.A.ii states that the redrawing of political boundaries IN SOME CASES led to conflict as well as population displacement and/or resettlements. A framework using some rather than all or none is one that both of the compared cases fit, so the anchor names the qualifier together with the alternative it excludes."),

 ("other newly independent states were taking a comparably strong role",
  "KC-6.3.I.C states that governments in newly independent states after World War II often took on a strong role in guiding economic life to promote development, so evidence that comparable states were doing the same supports the bulletin's case. Skill 3.D asks which evidence supports a source's argument; flags, former colonial status and emigration bear on other statements in this topic."),

 ("creation of new states through the redrawing of political boundaries after colonial authorities withdrew",
  "KC-6.2.III.A.i states that the redrawing of political boundaries after the withdrawal of former colonial authorities led to the creation of new states. More sovereign states in 1968 than in 1938 across the same ground, along lines that had been administrative, is that process recorded cartographically; a distractor reverses it into consolidation, so the anchor carries the direction."),

 ("Gamal Abdel Nasser in Egypt, Indira Gandhi in India, Julius Nyerere in Tanzania",
  "The CED prints these four beside KC-6.3.I.C as illustrative examples of governments guiding economic life in newly independent states. The other lists are illustrative examples the framework prints beside free-market policies, beside nonviolence, beside the Non-Aligned Movement and beside land and resource redistribution."),

 ("lay in a colony of that metropole and that its emigrants have gone there since independence",
  "KC-6.2.III.B states that the migration of former colonial subjects to imperial metropoles maintained cultural and economic ties between the colony and the metropole even after the dissolution of empires, which makes the connection a continuation of the colonial relationship rather than an accident of recent decades. Skill 3.D asks which evidence refutes a source's argument."),

 ("creation of new states from redrawn boundaries, and the movement of populations that in some cases followed",
  "KC-6.2.III.A.i gives the creation of new states through redrawn boundaries and KC-6.2.III.A.ii the conflict, population displacement and resettlements that in some cases followed. Unit 8 Learning Objective G asks how political changes led to territorial and demographic developments; a distractor exchanges colony and metropole as the direction of settlement, so the anchor carries both halves."),

 ("export patterns persisted while the new government simultaneously built state industries",
  "Unit 8 Learning Objective H asks for the economic changes AND continuities resulting from decolonization, and KC-6.3.I.C supplies the change, governments often taking a strong role in guiding economic life. A finding of continuity in exports alongside that change qualifies the historian's argument without overturning it, which is the modification skill 3.D names."),

 ("economic ties that migration to former metropoles maintained after empires dissolved",
  "KC-6.2.III.B states that the migration of former colonial subjects to imperial metropoles maintained cultural and economic ties between the colony and the metropole even after the dissolution of empires. Remittances large enough to pay for a fifth of a country's imports are that economic tie measured by the receiving state itself."),

 ("frontiers, and the administrative districts inside them, were those the colonial authority had drawn",
  "KC-6.2.III.A.i states that the redrawing of political boundaries after the withdrawal of former colonial authorities led to the creation of new states, so the territorial shape of a new state is itself an inheritance from the colonial period. Skill 3.D asks which evidence requires a source's argument to be qualified."),

 ("changed who governed and often how the economy was directed, while carrying forward colonial frontiers",
  "KC-6.3.I.C supplies the change in how economies were directed, KC-6.2.III.A.i makes the new states' frontiers the redrawn colonial ones, and KC-6.2.III.B makes migration a maintained tie with the metropole. Unit 8 Learning Objective H asks for changes and continuities together, so the anchor carries both sides."),

 ("population displacement and resettlement accompanying redrawn boundaries, and of migration to former metropoles",
  "KC-6.2.III.A.ii names population displacement and resettlements as consequences of redrawn boundaries in some cases, and KC-6.2.III.B names migration to imperial metropoles, so those are the two bodies of evidence in which demographic consequences would appear. Unit 8 Learning Objective G names territorial, demographic and nationalist developments as what political change led to."),

 ("in some cases conflict and the movement of peoples, their governments often took a strong hand in directing development",
  "KC-6.2.III.A.i supplies the new states from redrawn boundaries, KC-6.2.III.A.ii the conflict and displacement that followed in some cases, KC-6.3.I.C the strong role governments often took, and KC-6.2.III.B the ties migration maintained. The key is the conjunction of those four with both qualifiers intact, and each distractor contradicts at least one."),
]

wh.run(w8_6, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
