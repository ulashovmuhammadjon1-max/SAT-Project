"""Key audit for AP WORLD HISTORY: MODERN 6.3 Indigenous Responses to State Expansion.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is ``cg_check.check``; the notation gate and the negative
control are ``es_check``, reused unchanged, because World History is a prose
subject that ``export_units.py`` does not typeset, exactly as ENV_SCI is.

WHAT THE KEYS REST ON
---------------------
Items 1, 23, 24 rest on KC-5.2.II.C: anti-imperial resistance took various
forms, including direct resistance within empires and the creation of new states
on the peripheries. Items 6, 22, 26 rest on KC-5.3.III.D: increasing questions
about political authority and growing nationalism contributed to anticolonial
movements. Items 5, 7, 14, 25 rest on KC-5.3.III.E: increasing discontent with
imperial rule led to rebellions, SOME of which were influenced by religious
ideas -- the word "some" is what items 19 and 25 turn on. Item 28 pairs
KC-5.3.III.D with KC-5.3.III.E and asserts only that both can appear in one
episode, which is what a source containing both appeals shows.

Items 2, 3, 4, 8, 9 rest on the CED's own three headings for its illustrative
examples of this topic and on nothing else about those episodes. The CED names
them and describes none of them, so no item here asks what an episode did, when
it happened, who led it or how it ended. Two of the CED's examples name leaders
whose names carry accented characters; the notation gate refuses non-ASCII and
respelling a person's name to satisfy a checker is not acceptable, so those two
examples are absent from the module. That is a deliberate omission, recorded in
the module header, not an oversight.

Items 10 to 15, and 21, rest on suggested skill 2.C, explaining the significance
of a source's point of view, purpose, historical situation and audience,
including how these might limit the use of a source. Their keys rest on the
logic of evidence rather than on a claim about what happened, and each claim
below says so rather than citing a key concept it does not follow from.

Item 27 states what this topic can and cannot settle, and item 29 rests on the
CED's own labelling of these episodes as illustrative examples. Item 30 rests on
learning objective C, that internal and external factors influenced the process
of state building.

DATA ITEMS: 16 to 21 carry tables whose values are hypothetical and labelled so
in the stem. Each keyed conclusion is recomputed below from that table alone, and
each check also falsifies the distractors. The two categorical columns are
checked against an exact vocabulary rather than by substring, so a corrupted cell
fails the check instead of still reading as its original category.

NEGATIVE CONTROL: ``python3 verify_w6_3.py --selftest`` rotates every key off its
anchor, corrupts every table cell in turn, injects each banned notation form (and
one legal string that must pass), duplicates a choice, thins a why and makes a
why name an option by letter, and requires every one of those to raise.
"""
import sys

import cg_check as cg  # noqa: F401  (imported for parity with the other verifiers)
import es_check as es
import w6_3

EPISODE = "Episode (hypothetical)"
FORM = "Form the episode took"
RELIGION = "Religious ideas invoked by participants"

DECADE = "Decade of the record (hypothetical)"
PETITIONS = "Petitions against the administration received"
ARMED = "Armed episodes recorded by officials"

DIRECT = "Armed resistance inside an existing empire"
NEW_STATE = "Creation of a new state on the periphery of an empire"


def _rows(table):
    idx = {h: j for j, h in enumerate(table["headers"])}
    return [{h: str(r[j]) for h, j in idx.items()} for r in table["rows"]]


def _episodes(table):
    """Rows of the episode register, with both categorical columns validated.

    Exact membership, not a substring test: `es_check._corrupt` appends text to a
    cell, and a substring test would still read "Yes CORRUPTED" as a yes and
    "Creation of a new state ... CORRUPTED" as a new state. The control would then
    pass while proving nothing, which is the failure this project keeps paying
    for.
    """
    rows = _rows(table)
    for r in rows:
        assert r[FORM] in (DIRECT, NEW_STATE), f"unknown form {r[FORM]!r}"
        assert r[RELIGION] in ("Yes", "No"), f"religion column reads {r[RELIGION]!r}"
    return rows


def q16(table, item):
    rows = _episodes(table)
    assert len(rows) == 5, f"the stem says five episodes; the register holds {len(rows)}"
    named = [r for r in rows if r[FORM] in (DIRECT, NEW_STATE)]
    assert len(named) == 5, f"only {len(named)} rows take a form the framework names"
    return ("all five rows record either armed resistance inside an existing empire or the "
            "creation of a new state on a periphery, the two forms KC-5.2.II.C names")


def q17(table, item):
    rows = _episodes(table)
    hits = [r[EPISODE] for r in rows if r[FORM] == NEW_STATE and r[RELIGION] == "Yes"]
    assert hits == ["Episode 5"], f"new state with religious ideas is {hits}"
    return "Episode 5 is the only row combining the creation of a new state with religious ideas"


def q18(table, item):
    rows = _episodes(table)
    yes = [r[EPISODE] for r in rows if r[RELIGION] == "Yes"]
    assert len(yes) == 3, f"religious ideas are recorded in {yes}"
    return f"the religion column reads Yes in exactly three rows: {', '.join(yes)}"


def q19(table, item):
    rows = _episodes(table)
    no = [r[EPISODE] for r in rows if r[RELIGION] == "No"]
    assert len(no) == 2, f"rows without religious ideas are {no}"
    return (f"{' and '.join(no)} record no religious ideas, so a claim that religion caused "
            "every episode fails on the register itself")


def q20(table, item):
    rows = _rows(table)
    pet = [cg.num(r[PETITIONS]) for r in rows]
    arm = [cg.num(r[ARMED]) for r in rows]
    assert len(rows) == 4, f"the stem says four decades; the record holds {len(rows)}"
    assert all(b > a for a, b in zip(pet, pet[1:])), f"petitions do not rise throughout: {pet}"
    assert all(b > a for a, b in zip(arm, arm[1:])), f"armed episodes do not rise throughout: {arm}"
    assert pet[-1] > pet[0], "'the final decade records fewer petitions' must be false"
    return f"petitions run {pet} and armed episodes run {arm}, so both columns rise at every step"


def q21(table, item):
    rows = _rows(table)
    pet = [cg.num(r[PETITIONS]) for r in rows]
    arm = [cg.num(r[ARMED]) for r in rows]
    assert all(b > a for a, b in zip(pet, pet[1:])) and all(b > a for a, b in zip(arm, arm[1:])), \
        "the objection is about a rising record, so both columns must rise"
    assert "received" in PETITIONS and "recorded by officials" in ARMED, \
        "both columns must be administrative counts for the keyed objection to hold"
    assert len(rows) == 4, "'the record covers four decades rather than five' must be false as an objection"
    return ("both columns are counts made by the administration itself and both rise, which is "
            "what makes a change in recording practice an alternative reading of the rise")


TABLE_CHECKS = {16: q16, 17: q17, 18: q18, 19: q19, 20: q20, 21: q21}

CLAIMS = [
 ("within empires, and the creation of new states",
  "KC-5.2.II.C, near verbatim: anti-imperial resistance took various forms, including direct resistance within empires and the creation of new states on the peripheries. Purchase of colonies, emigration of officials, petitions to European parliaments, company founding, trade refusal and the abolition of monarchies are not named there."),
 ("Sokoto Caliphate",
  "The CED lists the Sokoto Caliphate in modern-day Nigeria under new states, and lists the Ghost Dance, the Xhosa Cattle-Killing Movement and the Mahdist wars under rebellions and the 1857 rebellion in India under direct resistance. KC-5.2.II.C is the statement the new-state heading illustrates."),
 ("establishment of independent states on the periphery",
  "The CED lists the establishment of independent states in the Balkans under new states, the heading answering to KC-5.2.II.C's creation of new states on the peripheries. The rejected options belong to other statements in this unit."),
 ("Direct resistance within an empire",
  "The CED lists the 1857 rebellion in India among its examples of direct resistance, the first of the two forms KC-5.2.II.C names. Settler colonies, company transfers and economic imperialism are the subject of other topics in this unit."),
 ("some of which were influenced by religious ideas",
  "KC-5.3.III.E, near verbatim, is the statement the CED's rebellions heading illustrates, and the Ghost Dance, the Xhosa Cattle-Killing Movement and the Mahdist wars are the three examples printed under it. The rejected statements are printed in this unit under other topics."),
 ("political authority, and growing nationalism",
  "KC-5.3.III.D, near verbatim: increasing questions about political authority and growing nationalism contributed to anticolonial movements. Population decline, garrison withdrawal, settler colonies, company abolition, commodity prices and mission schools are not named there."),
 ("Increasing discontent with imperial rule",
  "KC-5.3.III.E names increasing discontent with imperial rule as what led to rebellions, and adds that some of those rebellions were influenced by religious ideas, so an absence of religious ideas is the opposite of what the framework says."),
 ("Cherokee Nation and the Zulu Kingdom",
  "The CED lists the Cherokee Nation and the Zulu Kingdom under new states alongside the Balkans and the Sokoto Caliphate, while the 1857 rebellion in India and the Yaa Asantewaa War are listed under direct resistance and the Ghost Dance, the Xhosa Cattle-Killing Movement and the Mahdist wars under rebellions."),
 ("Yaa Asantewaa War",
  "The CED lists the Yaa Asantewaa War in West Africa among its examples of direct resistance, the first form named in KC-5.2.II.C. The other four options are listed under rebellions or under new states."),
 ("interest in how his own conduct was judged",
  "Suggested skill 2.C asks how a source's point of view and purpose may limit its use. A commander reporting on the operation he led has a stake in how it is judged and renders the rebels' aims at second hand. Presence at the events, the language of composition and a later date of writing are not by themselves disqualifications."),
 ("grievances its authors expected would persuade others",
  "Suggested skill 2.C makes purpose central to a source's use. A recruiting proclamation is written to persuade, so its contents are what its authors judged persuasive; it records neither their private reasoning nor the response, nor official policy, nor officials' beliefs."),
 ("each stresses whatever its own audience was most likely to accept",
  "Suggested skill 2.C names audience among the features whose significance must be explained. Two documents from one movement aimed at different audiences emphasize different things, which is a reason to read them together rather than to rank one as honest or discard both."),
 ("shaped by what had happened in the years between",
  "Suggested skill 2.C names a source's historical situation. A memoir written decades later is composed in a later situation with later knowledge and purposes, which shapes the account without making participation disqualifying or the events less important."),
 ("increasing discontent with imperial rule was present among the governed",
  "KC-5.3.III.E names increasing discontent with imperial rule as what led to rebellions, and a petition complaining of new taxes and of a removed local authority expresses exactly that discontent. It mentions no religion, no new state, no company transfer and no migration."),
 ("reports what that official saw and chose to report",
  "Suggested skill 2.C asks how point of view and purpose limit a source's use. One dispatch is one vantage point with its own purposes, and a claim about a whole population's views requires evidence about that population; the framework bans no category of source."),
 ("All five episodes",
  "Recomputed in q16 above: every row of the register records either armed resistance inside an existing empire or the creation of a new state on a periphery, which are the two forms KC-5.2.II.C names."),
 ("Episode 5",
  "Recomputed in q17 above: Episode 5 is the only row whose form is the creation of a new state and whose religion column reads Yes."),
 ("Three of the five episodes",
  "Recomputed in q18 above: the religion column reads Yes in three of the five rows. KC-5.3.III.E's own wording, that SOME rebellions were influenced by religious ideas, is what leads a student to expect a mixed column rather than a uniform one."),
 ("two of the five episodes record no religious ideas",
  "Recomputed in q19 above: two rows read No, so the register refutes a claim that religious ideas caused every episode. The rejected objections are true of the register but leave the claim standing."),
 ("Both the petitions and the armed episodes rise",
  "Recomputed in q20 above: petitions run 14, 31, 58, 96 and armed episodes run 1, 2, 4, 9, so both columns rise at every step and each rejected statement contradicts one or both sequences."),
 ("which may itself have changed over the four decades",
  "Suggested skill 2.C asks how a source's purpose and situation limit its use, and q21 above confirms both columns are counts made by the administration itself. A rise in what officials recorded may reflect a change in recording as well as a change in events; the record's length, its missing name, its units and its column order do not bear on that."),
 ("and rule imposed on it by an outside empire",
  "Learning objective C asks how internal and external factors influenced state building, and KC-5.3.III.D places growing nationalism and questions about political authority inside the society concerned while imperial rule comes from outside it. Each rejected option puts both of its items on the same side of that line."),
 ("establishing a state outside imperial control is itself a refusal",
  "KC-5.2.II.C names the creation of new states on the peripheries as one of the forms anti-imperial resistance took, so the classification is the framework's own. It does not make such states imperial foundations, prior to empire or tributary, and it does not turn every change of government into resistance."),
 ("direct resistance within an empire",
  "KC-5.2.II.C names direct resistance within empires as one of the two forms of anti-imperial resistance, and a movement that fights the administration without leaving the empire's borders is that form. Ethnic enclaves, settler colonies and economic imperialism belong to other statements in this unit."),
 ("some of the rebellions were influenced by religious ideas, not all of them",
  "KC-5.3.III.E says that increasing discontent with imperial rule led to rebellions, SOME of which were influenced by religious ideas. The quantifier is the correction, and KC-5.3.III.D separately names questions about political authority and growing nationalism."),
 ("one in political questions and nationalism and the other in discontent",
  "KC-5.3.III.D attributes anticolonial movements to increasing questions about political authority and growing nationalism; KC-5.3.III.E attributes rebellions to increasing discontent with imperial rule. Both locate the cause in how imperial rule was experienced, and both are printed under this unit's span of c. 1750 to c. 1900."),
 ("Whether the framework attributes rebellions to discontent with imperial rule can be answered; how many people took part in any particular rebellion cannot",
  "KC-5.3.III.E states the cause the framework attributes and KC-5.2.II.C names the forms resistance took. Participant numbers, casualties and dates for particular episodes appear nowhere in this topic, whose examples are listed without description. The anchor carries both clauses because the exact reversal is a distractor."),
 ("could operate together in one movement",
  "KC-5.3.III.E names religious ideas as an influence on some rebellions and KC-5.3.III.D names increasing questions about political authority as a contributor to anticolonial movements. A source carrying both appeals shows them in one episode, which is consistent with two separate framework statements rather than a contradiction of either."),
 ("general claims about forms and causes, not a complete inventory",
  "The CED prints these episodes under the heading of illustrative examples beside KC-5.2.II.C and KC-5.3.III.E, which are general claims about the forms resistance took and the discontent that produced rebellions. An example illustrates such a claim and does not exhaust the cases falling under it."),
 ("acted in ways that shaped what followed",
  "KC-5.2.II.C, KC-5.3.III.D and KC-5.3.III.E describe resistance, anticolonial movements and rebellions arising among the governed, and learning objective C asks how internal and external factors influenced state building. The preceding topic's KC-5.2.I.C already has European states using warfare, so a claim that no force was used is false there as well."),
]

es.run(w6_3, CLAIMS, TABLE_CHECKS, sys.argv)
