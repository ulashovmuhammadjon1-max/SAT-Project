"""Key audit for AP WORLD HISTORY: MODERN 9.7 Resistance to Globalization After
1900.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that MUST appear in the keyed choice and in NO distractor; the claim
states the CED sentence the key rests on, with its Key Concept code or Learning
Objective, for a human to audit. `wh_check` refuses any claim or `why` that
cites neither.

THIS TOPIC PRINTS THE SHORTEST KEY CONCEPT IN THE UNIT, and thirty questions had
to come out of it without anything being added. KC-6.3.IV.iv: responses to
rising cultural and economic globalization took a variety of forms. That
sentence licenses exactly three things, and every claim below is one of them, or
is skill 2.C applied to a source produced by someone responding:

  (a) that there WERE responses, and that what they answered was globalization
      that was RISING (q10, q15, q20);
  (b) that the globalization responded to was of TWO kinds, cultural AND
      economic (q2, q7, q11, q27);
  (c) that the responses took A VARIETY OF FORMS (q1, q3, q6, q9, q16, q24,
      q26, q29).

Where an item needs to name what globalization consisted of, its claim cites the
sentence in another topic that says so -- KC-6.3.IV.i to iii for the cultural
side, KC-6.3.I.D, KC-6.3.I.E and KC-6.3.II.B for the economic -- rather than
inventing content for this page. Nothing is keyed to a fact this page does not
state.

THE WORD IS "RESPONSES", NOT "REJECTIONS". The topic title says Resistance but
the framework's sentence says RESPONSES and says they varied, and the CED's own
second illustrative example -- the advent of locally developed social media --
is a locally built alternative rather than a refusal. q5, q19 and q24 key that
distinction, and q19 keys it directly. A bank that read every response as a
rejection would narrow the framework's own word, which is the specific failure
this topic invites.

WHAT NO CLAIM BELOW ASSERTS. Whether globalization should have been resisted,
whether any response was justified, and whether any succeeded are live political
arguments the framework settles none of. No claim says a response was right or
wrong, effective or futile, reasonable or unreasonable; none attributes a motive
to anyone who responded; none says any institution deserved or did not deserve
the opposition it met. q23 keys the framework's silence on the merits directly,
and the illustrative-example item at q13 says in its own why that it takes no
position on either example.

DEDUPE. Topic 8.7 borders this one and is in the same territory, so the line is
drawn explicitly: 8.7 is reactions to CONFLICT and to power structures in the
Cold War era -- nonviolence, militarized states, violence against civilians --
and none of that vocabulary appears in this module. Topic 9.5's KC-6.3.II.C is a
narrower sentence about protesting the INEQUALITY of consequences and is cited
here only where an item needs one form a response took.

WHERE A DISTRACTOR IS THE SWAP OF THE KEY, THE ANCHOR CARRIES BOTH CLAUSES.
Five items are built on a reversal a prepared student could believe:

  q3   variety of forms swapped for a single form, and a falling share for a
       rising one
  q6   "a variety of forms" swapped for "no identifiable form"
  q15  responses answering globalization swapped for responses causing it
  q17  the NOT-supported item, where the key is deliberately the false claim
  q28  cultural and economic sides exchanged between two sources

For each the anchor spans the whole relation, so an anchor that matched the
swapped distractor would fail the gate rather than pass it. That defect is on
record in `verify_e2_1.py`.

WHAT THIS CANNOT DO: it cannot tell whether the history is right. It gates
structure, key/anchor agreement, notation, the absence of figure language, the
presence of a citation, and the arithmetic of the three data questions.

NEGATIVE CONTROL: `python3 verify_w9_7.py --selftest`. It rotates all thirty
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
import w9_7

T_FORMS = w9_7._T_FORMS
T_TARGET = w9_7._T_TARGET
T_SERVICES = w9_7._T_SERVICES

RESPONSES = "Responses recorded"
PROTEST = "Of those, taking the form of public protest"
OTHER_FORM = "Of those, taking some other form"
ECONOMIC = "Of those, addressed chiefly to economic globalization"
CULTURAL = "Of those, addressed chiefly to cultural globalization"
USERS = "Users recorded"
LOCAL = "Of those, using a locally developed service most often"
FOREIGN = "Of those, using a service developed abroad most often"


def _parts_sum_to_whole(table, whole, parts, what):
    """Every row's parts must total its whole.

    This is what makes the negative control mean anything on these tables. The
    corruption in `es_check` only ever makes a number LARGER, so a check of the
    form "this count is above zero" is monotone and can never fail: it reads the
    table without being able to object to anything in it. Sibling module 8.5
    shipped a first draft whose table check caught 1 of 12 corrupted cells for
    exactly that reason. Each row here states a whole and the two parts it was
    divided into, and every stem says so.
    """
    labs = cg.labels(table)
    totals = cg.col(table, whole)
    cols = [cg.col(table, p) for p in parts]
    for i, lab in enumerate(labs):
        got = sum(c[i] for c in cols)
        assert got == totals[i], (
            f"{lab}: the {what} split into {[c[i] for c in cols]} totals {got}, but the "
            f"row states {totals[i]} in all -- the parts do not sum to the whole")


def q3(table, item):
    """Both forms in every decade, and the protest SHARE falling."""
    decades = cg.labels(table)
    assert decades == ["1970s", "1990s", "2010s"], \
        f"the key speaks of every decade recorded; the rows are {decades}"
    _parts_sum_to_whole(table, RESPONSES, [PROTEST, OTHER_FORM], "responses recorded")
    total = cg.col(table, RESPONSES)
    prot = cg.col(table, PROTEST)
    other = cg.col(table, OTHER_FORM)
    for d, p, o in zip(decades, prot, other):
        assert p > 0 and o > 0, (
            f"the key needs responses of both kinds in {d}; the row reads {p} protests "
            f"and {o} of other forms")
    shares = [p / t for p, t in zip(prot, total)]
    assert all(b < a for a, b in zip(shares, shares[1:])), (
        f"the key says the protest portion falls AS A SHARE; the shares run "
        f"{[round(s, 3) for s in shares]} against counts {prot}, which rise")
    # every distractor false on the same numbers
    assert any(o > 0 for o in other), \
        "'every response recorded took the form of public protest' must be false"
    assert prot[0] > 0, \
        "'no 1970s response took the form of public protest' must be false"
    assert all(b > a for a, b in zip(total, total[1:])), \
        "'the number of responses fell in each decade after the first' must be false"
    assert shares[-1] < shares[0], \
        "'the protest share rose across the record' must be false"
    return (f"responses run {total} with {prot} protests and {other} of other forms, both "
            f"present throughout, and the protest share {[round(s, 3) for s in shares]} "
            f"falling even as the protest count rises; the parts sum to the stated wholes "
            f"and all four distractors recompute false")


def q7(table, item):
    """Both targets in every decade, economic the larger throughout."""
    decades = cg.labels(table)
    assert decades == ["1980s", "1990s", "2000s"], \
        f"the key speaks of every decade recorded; the rows are {decades}"
    _parts_sum_to_whole(table, RESPONSES, [ECONOMIC, CULTURAL], "responses recorded")
    total = cg.col(table, RESPONSES)
    eco = cg.col(table, ECONOMIC)
    cul = cg.col(table, CULTURAL)
    for d, e, c in zip(decades, eco, cul):
        assert e > 0 and c > 0, (
            f"the key needs responses of both kinds in {d}; the row reads {e} economic "
            f"and {c} cultural")
        assert e > c, (
            f"the key needs the chiefly economic to outnumber the chiefly cultural in {d}; "
            f"the row reads {e} against {c}")
    # every distractor false on the same numbers
    assert any(c > 0 for c in cul), \
        "'only chiefly economic responses are recorded' must be false"
    assert any(e > 0 for e in eco), \
        "'only chiefly cultural responses are recorded' must be false"
    assert not all(c > e for c, e in zip(cul, eco)), \
        "'chiefly cultural responses outnumber the others in every decade' must be false"
    assert all(b > a for a, b in zip(total, total[1:])), \
        "'the number of responses fell in each decade after the first' must be false"
    return (f"responses run {total} with {eco} chiefly economic and {cul} chiefly "
            f"cultural, both present in every decade and the economic the larger "
            f"throughout; the parts sum to the stated wholes and all four distractors "
            f"recompute false")


def q12(table, item):
    """Locally developed services used somewhere in every country, prevailing in one."""
    labs = cg.labels(table)
    total = dict(zip(labs, cg.col(table, USERS)))
    local = dict(zip(labs, cg.col(table, LOCAL)))
    _parts_sum_to_whole(table, USERS, [LOCAL, FOREIGN], "users recorded")
    for lab in labs:
        assert local[lab] > 0, (
            f"the key needs some users of a locally developed service in {lab}; the row "
            f"reads {local[lab]}")
    prevail = [lab for lab in labs if local[lab] > 0.5 * total[lab]]
    assert len(prevail) == 1, (
        f"the key says locally developed services are the more common choice in only one "
        f"of the three; they prevail in {prevail}")
    # every distractor false on the same numbers
    assert any(local[l] > 0 for l in labs), \
        "'no user in any country most often uses a locally developed service' must be false"
    assert len(prevail) < len(labs), \
        "'locally developed services are the more common choice in every country' must be false"
    assert total["Country three"] <= total["Country two"], \
        "'country three records more users than country two' must be false"
    assert len(set(total.values())) > 1, \
        "'the three countries record the same number of users' must be false"
    return (f"users preferring a locally developed service {local} of totals {total}: some "
            f"in every country and a majority only in {prevail}; the parts sum to the "
            f"stated wholes and all four distractors recompute false")


TABLE_CHECKS = {3: q3, 7: q7, 12: q12}

CLAIMS = [
 ("They took a variety of forms",
  "KC-6.3.IV.iv states that responses to rising cultural and economic globalization took A VARIETY OF FORMS. Variety is the framework's own word and the whole of what the sentence says about form, which Unit 9 Learning Objective G repeats in asking for the VARIOUS responses to increasing globalization."),

 ("Cultural globalization and economic globalization",
  "KC-6.3.IV.iv states that responses were to rising CULTURAL AND ECONOMIC globalization. Both adjectives are in the sentence, so a key naming one would report half of it, and two distractors offer exactly that half."),

 ("share taking the form of public protest falls across the record",
  "KC-6.3.IV.iv states that responses took A VARIETY of forms, and a record in which protest is one form among others and a shrinking share of the whole is that variety counted. The record is hypothetical and is recomputed from the table alone in q3 above, which also separates the falling share from the rising count."),

 ("forms taken by responses to rising economic globalization",
  "KC-6.3.IV.iv states that responses to rising cultural and economic globalization took a variety of forms, and the CED prints anti-IMF and anti-World Bank activism among its illustrative examples of responses to economic globalization. The key identifies which development the circular belongs to and says nothing about whether the meeting was justified."),

 ("varied forms a response to globalization could take, alongside protest",
  "KC-6.3.IV.iv states that responses took A VARIETY OF FORMS, and the CED prints the advent of locally developed social media among its illustrative examples of responses to economic globalization. A locally built alternative is one of the varied forms the sentence covers, which is why the framework's noun is responses rather than rejections."),

 ("took a variety of forms, so protest was one form among others",
  "KC-6.3.IV.iv's word is VARIETY, which rules out a single form without denying that protest was among them. The correction must keep protest inside the range rather than removing it, so the anchor carries the variety and protest's place within it."),

 ("those addressed chiefly to economic globalization outnumber the others throughout",
  "KC-6.3.IV.iv names both cultural and economic globalization as what responses answered, and a record containing both in every decade is that pairing counted. The record is hypothetical and is recomputed from the table alone in q7 above; the framework asserts no real frequency for either kind."),

 ("members stand to gain from the outcome it argues for, which bears on how the argument can be used",
  "Skill 2.C asks for the significance of a source's point of view, purpose, historical situation and audience, including how these might limit its uses. Unit 9 Learning Objective G asks for the various responses to increasing globalization, and an association arguing for the outcome its members profit from is a response whose interest a historian weighs before using it as evidence of anything else."),

 ("responses to rising globalization took a variety of forms",
  "KC-6.3.IV.iv states exactly that. A demonstration and a magazine answering the same agreement are two forms of one response, which is the variety the sentence asserts made visible in a single case."),

 ("As rising during the period in which the responses were made",
  "KC-6.3.IV.iv states that responses were to RISING cultural and economic globalization, and Unit 9 Learning Objective G repeats it in asking for responses to INCREASING globalization. The framework's adjective makes the globalization something that was growing while the responses were made."),

 ("response to rising cultural globalization, taking one of the varied forms",
  "KC-6.3.IV.iv states that responses to rising CULTURAL and economic globalization took a variety of forms. An association recording local songs because so much heard locally now comes from elsewhere answers the cultural side, and collecting and publishing is one of the varied forms rather than the only one, so the anchor carries both."),

 ("such services are the more common choice in only one of the three",
  "KC-6.3.IV.iv states that responses took a variety of forms, and the CED prints the advent of locally developed social media among its illustrative examples. A survey in which locally developed services prevail in one place and not in others is that variety measured, and it is recomputed from the table alone in q12 above."),

 ("Anti-IMF and anti-World Bank activism, and the advent of locally developed social media",
  "The CED prints these two beside KC-6.3.IV.iv as its illustrative examples of responses to economic globalization. The other lists are printed beside statements in Topics 9.5, 9.4, 9.6 and 8.7. The item asks which pair the course prints and takes no position on whether either response was justified."),

 ("issued by a government that was a party to the conference the protests were directed at",
  "Skill 2.C asks how a source's point of view, purpose and situation might limit its uses. KC-6.3.IV.iv establishes that responses to rising globalization occurred and varied, and a government party to the meeting being protested has an interest in how numerous the protesters are said to be, which is the claim at issue."),

 ("made to globalization as it rose, so globalization is what they answered",
  "KC-6.3.IV.iv states that RESPONSES TO rising cultural and economic globalization took a variety of forms, which makes globalization the thing responded to and the responses what followed. A distractor reverses that direction, so the anchor carries it; the reasoning process the CED prints beside this topic is causation."),

 ("varied in their grounds as well as in their forms",
  "KC-6.3.IV.iv states that responses took A VARIETY OF FORMS and Unit 9 Learning Objective G asks for the VARIOUS responses. Two organizations opposing one agreement on different grounds is that variety, and nothing in the framework requires objections to share a reason."),

 ("Every response to globalization in this period took the same form as every other",
  "KC-6.3.IV.iv states that responses took A VARIETY of forms, so a claim that every response took the same form reverses the framework's sentence. The item asks which statement is NOT supported, so the anchor is pinned to the false one deliberately; the other four restate the parts of that single sentence."),

 ("act on globalization through the decisions of ordinary consumers rather than through government",
  "Skill 2.C asks for the significance of a source's audience, and a leaflet addressed to shoppers at the shelf is aimed at the point where a consumer decides. KC-6.3.IV.iv states that responses took a variety of forms, and acting through consumers rather than through governments is one of them."),

 ("took a variety of forms, and building a local alternative is a different form from refusing",
  "KC-6.3.IV.iv's own noun is RESPONSES and its own claim is that they took A VARIETY of forms, and the CED's second illustrative example, the advent of locally developed social media, is a locally made alternative rather than a refusal. A bank reading every response as a rejection would narrow the framework's word, which is what this item exists to prevent."),

 ("When cultural and economic globalization began to rise in that country",
  "KC-6.3.IV.iv states that the responses were to RISING cultural and economic globalization, which makes the timing of that rise the framework's own explanation for when responses appear. The reasoning process the CED prints beside this topic is causation."),

 ("Read each for the position it was written from",
  "Skill 2.C asks for the significance of a source's point of view, purpose and audience, which is a question to put to both accounts rather than a rule for ranking them. KC-6.3.IV.iv places responses to rising globalization inside a period in which the parties disagreed, so accounts from the two sides are expected to differ and the difference is itself evidence."),

 ("responses to rising cultural globalization, of which this is one of the varied forms",
  "KC-6.3.IV.iv states that responses to rising CULTURAL and economic globalization took a variety of forms, and KC-6.3.IV.ii records that arts, entertainment and popular culture increasingly reflected a globalized society. A quota for home-made programmes answers that cultural side, and a regulatory measure is one of the varied forms rather than the only one."),

 ("states that responses occurred and varied without judging any of them",
  "KC-6.3.IV.iv states only that responses to rising cultural and economic globalization took a variety of forms. It records their occurrence and their variety and passes no judgement on any of them, and Unit 9 Learning Objective G asks a student to explain the various responses rather than to rank them. This is the item that keys the framework's silence on the merits directly."),

 ("public demonstration, a locally built alternative service, and a regulation restricting imports",
  "KC-6.3.IV.iv states that responses took A VARIETY OF FORMS, so what shows the variety is a set of responses different in kind rather than several instances of one kind. The CED's own two illustrative examples, activism and the advent of locally developed social media, are themselves two different kinds, which is the pattern the key follows."),

 ("industrial production and manufacturing were increasingly situated in Asia and Latin America",
  "KC-6.3.I.E states that in the late twentieth century industrial production and manufacturing were increasingly situated in Asia and Latin America, which is the economic development the bulletin objects to, and KC-6.3.IV.iv establishes that responses to rising economic globalization took a variety of forms. The key names what is being responded to, not whether the objection was sound."),

 ("responses to rising cultural and economic globalization took a variety of forms",
  "KC-6.3.IV.iv is precisely the claim that studying one form cannot exhaust the subject. Unit 9 Learning Objective G's word is VARIOUS, and the CED's second illustrative example is not a protest at all, so the historian's argument is the framework's own sentence restated."),

 ("responses to rising globalization, though they answer different sides of it and take different forms",
  "KC-6.3.IV.iv states that responses to rising CULTURAL AND ECONOMIC globalization took A VARIETY of forms. Support for local film answers the cultural side and a demand to close markets the economic, and a subsidy and a manifesto are different forms, so the pair shows both halves of the sentence at once and the anchor carries both."),

 ("produced to persuade someone, which shapes what it can be used to establish",
  "Skill 2.C asks for the significance of a source's purpose, including how it might limit the source's uses. KC-6.3.IV.iv establishes that responses to rising globalization took a variety of forms, and sources produced in the course of responding are made to persuade, which is a property to reckon with rather than a disqualification."),

 ("what they answered was rising cultural and economic globalization, and that they took a variety of forms",
  "KC-6.3.IV.iv is one sentence containing exactly three assertions: that there were responses, that they answered rising cultural and economic globalization, and that they took a variety of forms. The key states all three and each distractor removes or narrows one."),

 ("people answered it in many different ways, from organized activism to building local alternatives of their own",
  "KC-6.3.IV.iv states that responses to rising cultural and economic globalization took a variety of forms, and the CED prints activism and the advent of locally developed social media as its two illustrative examples of exactly that variety. The key states the rise, the variety and the framework's silence on the merits, and each distractor contradicts one of those."),
]

wh.run(w9_7, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
