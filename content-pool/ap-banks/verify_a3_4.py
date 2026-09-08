"""Key audit for AP U.S. HISTORY 3.4 Philosophical Foundations of the American Revolution.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The shared gate is
``wh_check.run``: a KC code or Learning Objective in every ``why`` and every
``claim``, no figure language, no typeset markup, the marked-stimulus rule, and
``cg_check``'s structural and anchor checks underneath.

WHAT THE KEYS REST ON
---------------------
  Unit 3 Learning Objective D, attitudes about
    government AND the individual CHANGING       items 1, 2, 3, 4, 20, 27
  the NAT thematic focus, both sentences         5, 6, 28
  KC-3.2.I.A, Enlightenment against hereditary
    privilege WHILE religion strengthened a
    sense of liberty                             7, 8, 9, 10, 11, 21, 22, 26, 27, 28, 29, 30
  KC-3.2.I.B, republican government on natural
    rights, expressed in two named documents,
    resonating throughout American history       12, 13, 14, 15, 16, 22, 23, 25, 29, 30
  KC-3.2.I, new beliefs DEVELOPING over the
    18th century                                 17, 20, 30
  skill 2.B, EXPLAIN rather than identify        2, 3, 18, 19

THE RULE THAT BITES HARDEST HERE. KC-3.2.I.B names Thomas Paine's Common Sense
and the Declaration of Independence, so this module may name them -- and a
fabricated line of either would be read by a student as fact, which is exactly
what HISTORY_BRIEF.md forbids. ``no_invented_quotation`` asserts that no stem,
choice or why in this module contains a quoted passage at all: there is no
quotation mark in the student-facing text, so there is nothing for a student to
take for a line of a real document. That is a blunter rule than the brief's,
and deliberately so, because a checker cannot tell an honest quotation from an
invented one. The framework's own emphasis is carried by capitals instead.

THE SCOPE THIS MODULE HAS TO HOLD. The topic page's OPTIONAL SOURCES (a Sarah
Osborn memoir, a Phillis Wheatley poem) are, in the CED's own words, "not
required AP course content", and no exam question requires a student to have
studied them. ``no_optional_source_key`` asserts no key rests on either.

THE SWAP ITEMS, where a distractor is the key with two clauses exchanged and
the anchor therefore carries BOTH: item 3 (identify against explain), item 7
(talent over privilege), item 9 (which strand did which), item 14 (both
documents), item 29 (the whole sentence, exchanged).

DATA ITEMS: 21, 22 and 23, all HYPOTHETICAL, because the CED prints no data for
this topic. Items 22 and 23 state their expected rows here, independently of
the module, so every cell is load-bearing. Item 21 is categorical and compares
only its TEXT column literally, so the named control below, which removes the
overlap between the two strands, raises on the count the key depends on rather
than on a row-equality assertion that would prove nothing about it.

NEGATIVE CONTROLS: ``python3 verify_a3_4.py --selftest``.
"""
import re
import sys

import wh_check
import a3_4

TEXT = "Text in a hypothetical collection"
ENLIGHT = "Draws on Enlightenment philosophy"
RELIGION = "Draws on religious language"
ARGUMENT = "Argument made in a hypothetical set of essays"
ESSAYS = "Essays in which it appears"
LATER = "Later period in a hypothetical survey"
ADDRESSES = "Public addresses invoking the ideals of the founding documents"

_OPTIONAL_SOURCE = re.compile(
    r"(?<![A-Za-z])(Sarah Osborn|Phillis Wheatley|Whitefield|Samuel Hopkins)(?![A-Za-z])",
    re.IGNORECASE)

# Any quotation mark at all, straight or typographic. es_check already refuses
# non-ASCII, so in practice this catches the straight ones; both are listed so
# the rule does not depend on the order the two gates run in.
_QUOTED = re.compile(r"[\"“”]")


def no_optional_source_key(module):
    """No key may rest on a source the CED says the exam never requires."""
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for label, text in (("keyed choice", item["choices"][item["ans"]]),
                            ("why", item["why"])):
            hit = _OPTIONAL_SOURCE.search(text)
            assert not hit, (
                f"{code} q{i}: the {label} rests on {hit.group(0)!r}, which the topic page "
                f"lists under OPTIONAL SOURCES and the CED says no exam question requires a "
                f"student to have studied -- {text[:70]!r}"
            )
    print(f"OK  {code} scope: no key rests on a source the framework marks optional.")


def no_invented_quotation(module):
    """Nothing in this module may READ as a quotation from a real document.

    KC-3.2.I.B names Common Sense and the Declaration of Independence, so this
    is the module in the unit where a fabricated line would do the most damage.
    A checker cannot tell an invented quotation from an honest one, so the rule
    enforced here is the blunt one: no quotation marks in student-facing text.
    """
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"], item["why"]] + list(item["choices"]):
            hit = _QUOTED.search(text)
            assert not hit, (
                f"{code} q{i}: a quotation mark appears in student-facing text. This module "
                f"names Common Sense and the Declaration of Independence, and a student would "
                f"read any quoted line as a line of one of them -- {text[:70]!r}"
            )
    print(f"OK  {code} sources: no quoted passage anywhere, so nothing can be mistaken for a "
          f"line of a document the framework names.")


# ------------------------------------------------------------------ table checks

def _col(table, header):
    idx = table["headers"].index(header)
    return [row[idx] for row in table["rows"]]


def _nums(table, header):
    return [float(str(v).replace(",", "")) for v in _col(table, header)]


_EXPECTED_TEXTS = ["Text 1", "Text 2", "Text 3", "Text 4"]
_MARKS = {"Yes", "No"}


def q21(table, item):
    # ONLY THE TEXT COLUMN IS COMPARED LITERALLY, so the named control that
    # removes the overlap between the two strands raises on the overlap count
    # below rather than on a row-equality assertion, which would fire for the
    # wrong reason. A corrupted mark still fails, through the membership check:
    # the shared corrupter appends text, and 'Yes CORRUPTED' is neither Yes nor
    # No.
    assert _col(table, TEXT) == _EXPECTED_TEXTS, (
        f"the strands table does not carry the rows this check was written against; "
        f"got {_col(table, TEXT)}")
    enl, rel = _col(table, ENLIGHT), _col(table, RELIGION)
    for m in enl + rel:
        assert m in _MARKS, f"every mark must be Yes or No; got {m!r}"
    both = [i for i, (e, r) in enumerate(zip(enl, rel)) if e == "Yes" and r == "Yes"]
    assert len(both) > 1, (
        f"the key says SOME texts draw on both at once, so more than one row must carry "
        f"both marks; {len(both)} does")
    assert enl.count("Yes") and rel.count("Yes"), \
        f"both strands must appear somewhere; got {enl} and {rel}"
    assert enl.count("No"), "'every text draws on Enlightenment philosophy' must be false"
    assert rel.count("No"), "'every text draws on religious language' must be false"
    marked = [i for i, (e, r) in enumerate(zip(enl, rel)) if e == "Yes" or r == "Yes"]
    assert len(marked) > 1, "'only one text draws on either strand' must be false"
    return (f"{len(both)} of {len(enl)} rows carry both marks, and each strand is absent from "
            f"at least one row, so neither is universal and the two are not alternatives")


_EXPECTED_ARGUMENTS = [["Office should follow individual talent", "28"],
                       ["Office should follow hereditary rank", "5"],
                       ["Government rests on the natural rights of the people", "22"],
                       ["Government rests on a ruler's inherited claim", "4"]]


def q22(table, item):
    assert [list(r) for r in table["rows"]] == _EXPECTED_ARGUMENTS, (
        f"the arguments table does not hold the rows this check was written against; "
        f"got {table['rows']}")
    tallies = _nums(table, ESSAYS)
    talent, rank, rights, claim = tallies
    assert talent > 2 * rank, (
        f"the talent argument must far outrun the hereditary-rank one; got {talent} and {rank}")
    assert rights > 2 * claim, (
        f"the natural-rights argument must far outrun the inherited-claim one; got {rights} "
        f"and {claim}")
    assert rank < talent, "'hereditary rank appears more often than individual talent' must be false"
    assert len(set(tallies)) == len(tallies) and max(tallies) > 2 * min(tallies), \
        f"'the four appear about equally often' must be false; got {tallies}"
    assert claim != max(tallies), \
        "'a ruler's inherited claim is the most common of the four' must be false"
    labels = _col(table, ARGUMENT)
    assert any("office" in l.lower() for l in labels) and \
        any("government rests" in l.lower() for l in labels), \
        "'only arguments about officeholding appear' must be false"
    return (f"the tallies are {tallies}: talent {talent} against rank {rank}, and natural "
            f"rights {rights} against an inherited claim {claim}")


_EXPECTED_RESONANCE = [["First later period", "40"],
                       ["Second later period", "55"],
                       ["Third later period", "72"]]


def q23(table, item):
    assert [list(r) for r in table["rows"]] == _EXPECTED_RESONANCE, (
        f"the resonance table does not hold the rows this check was written against; "
        f"got {table['rows']}")
    counts = _nums(table, ADDRESSES)
    assert all(c > 0 for c in counts), (
        f"'they cease to be invoked after the first later period' and 'invoked in only one "
        f"period' must both be false; got {counts}")
    assert all(b > a for a, b in zip(counts, counts[1:])), (
        f"'invoked less often in each later period than in the one before' must be false, and "
        f"the key's word INCREASINGLY must hold; got {counts}")
    assert len(counts) > 1, "'invoked only in the period in which they were written' must be false"
    return (f"every later period records invocations, {counts}, and the counts rise at each "
            f"step")


TABLE_CHECKS = {21: q21, 22: q22, 23: q23}

CLAIMS = [
 ("colonial attitudes about government and the individual changed",
  "Unit 3: Learning Objective D reads 'Explain how and why colonial attitudes about government and the individual changed in the years leading up to the American Revolution.' Both subjects are in it, and the direction is change."),
 ("Explain the point of view, purpose, historical situation, and audience of a source",
  "Skill 2.B as printed beside this topic's title, beneath Unit 3: Learning Objective D. Skill 2.A, printed on the taxation topic, asks only that the same four be IDENTIFIED."),
 ("EXPLAIN a source's point of view, purpose, historical situation, or audience, where the other asks only that they be IDENTIFIED",
  "Skill 2.B opens with Explain and skill 2.A with Identify, while the four sourcing questions named afterwards are the same in both. The anchor carries both halves because the leading distractor exchanges the two verbs. Unit 3: Learning Objective D is the objective this skill serves here."),
 ("Continuity and Change",
  "The unit's topic table assigns Continuity and Change to this topic, matching Unit 3: Learning Objective D's CHANGED and KC-3.2.I's beliefs that had been DEVELOPING over the course of the 18th century."),
 ("those ideas in turn shape political institutions and society",
  "The American and National Identity thematic focus printed on this topic page has the influence running both ways: debates shape national identity and cultural values, and in turn those ideas shape political institutions and society. KC-3.2.I.A is an instance of the first half."),
 ("coexisted with varying degrees of regional and group identities",
  "The second sentence of the American and National Identity thematic focus on this page says notions of national identity and culture have coexisted with varying degrees of regional and group identities throughout American history, which rules out replacement, prevention and a fixed proportion. Unit 3: Learning Objective D's years before the Revolution are one stretch inside that longer run."),
 ("Individual talent over hereditary privilege",
  "KC-3.2.I.A states that Enlightenment ideas and philosophy inspired many American political thinkers to emphasize individual talent OVER hereditary privilege. The anchor carries both terms in order because the leading distractor is the same pair reversed."),
 ("Enlightenment ideas inspired many American political thinkers to emphasize individual talent",
  "KC-3.2.I.A names this emphasis as what Enlightenment ideas and philosophy inspired; the religious strand is the other half of the same sentence and concerns how Americans viewed themselves, and KC-3.2.I.B bases republican government on natural rights rather than inheritance."),
 ("It strengthened Americans' view of themselves as a people blessed with liberty",
  "KC-3.2.I.A's second clause credits religion with exactly this. Assigning the talent emphasis to religion swaps the sentence's two halves, which is why the anchor is the religious clause in full."),
 ("Two, Enlightenment philosophy and religion, presented as working alongside each other",
  "KC-3.2.I.A joins its two clauses with WHILE, so both contributions are asserted, neither is dismissed or deferred, and the sentence sets no bar to a thinker drawing on both."),
 ("without claiming every thinker held it",
  "KC-3.2.I.A says Enlightenment ideas inspired MANY American political thinkers, which is a claim about a large number rather than about all of them or a slight few."),
 ("superiority of republican forms of government",
  "KC-3.2.I.B opens with the colonists' belief in the superiority of republican forms of government based on the natural rights of the people."),
 ("The natural rights of the people",
  "KC-3.2.I.B specifies that the republican forms the colonists believed superior were based on the natural rights of the people; an inherited claim is what KC-3.2.I.A's emphasis works against."),
 ("Thomas Paine's Common Sense and the Declaration of Independence",
  "KC-3.2.I.B names both writings together as where the belief found expression. The anchor carries both because two distractors keep one and drop the other."),
 ("resonated throughout American history",
  "KC-3.2.I.B states that the ideas in these documents resonated throughout American history, which is what rules out confinement to the Revolution, forgetting, a regional limit or a later first revival."),
 ("understanding of the ideals on which the nation was based",
  "KC-3.2.I.B ends with the ideas shaping Americans' understanding of the ideals on which the nation was based, so the sentence concerns ideals rather than boundaries or officeholding."),
 ("new beliefs that had been developing over the course of the 18th century",
  "KC-3.2.I states that the ideals inspiring the revolutionary cause reflected NEW beliefs that HAD BEEN DEVELOPING over the course of the 18th century, which is why this topic's reasoning process is Continuity and Change."),
 ("in order to persuade the congregation that their liberties were a trust",
  "Skill 2.B distinguishes a source's PURPOSE, the objective its creator pursued, from its HISTORICAL SITUATION, what was happening around it; only the keyed statement gives an objective. KC-3.2.I.A is the content such a source would carry, crediting religion with strengthening Americans' view of themselves as a people blessed with liberty."),
 ("plain language and sold at a price a labourer could afford",
  "Skill 2.B separates AUDIENCE, who a source was made for, from point of view, historical situation and purpose; price and plainness identify the readers aimed at. KC-3.2.I.A supplies the argument such a pamphlet would make, individual talent over hereditary privilege."),
 ("colonial attitudes about government and the individual changed in the years leading up",
  "Unit 3: Learning Objective D asks for exactly this change, and KC-3.2.I places the development across the 18th century rather than after independence; KC-3.2.I.A credits religion with strengthening rather than discouraging a sense of liberty."),
 ("some texts draw on both at once, so they are not alternatives",
  "Recomputed in q21 from the table alone, with each rejected option falsified against the same marks. KC-3.2.I.A joins Enlightenment philosophy and religion with WHILE, describing two contributions running together."),
 ("each appear far more often than their inherited counterparts",
  "Recomputed in q22 from the table alone. KC-3.2.I.A supplies the first pairing, individual talent over hereditary privilege, and KC-3.2.I.B the second, republican government based on the natural rights of the people."),
 ("continue to be invoked in every later period recorded, and increasingly so",
  "Recomputed in q23 from the table alone: every later period records invocations and the counts rise. KC-3.2.I.B says the ideas in these documents resonated throughout American history, shaping Americans' understanding of the ideals on which the nation was based."),
 ("FOUND EXPRESSION in them, which is a claim about where the belief was set down",
  "KC-3.2.I.B says the colonists' belief FOUND EXPRESSION in Thomas Paine's Common Sense and the Declaration of Independence; expression presupposes a belief already held, so the writings neither create it nor exhaust it, and the sentence says nothing of legal force."),
 ("religion and Enlightenment philosophy worked against one another",
  "KC-3.2.I.A places the two in one sentence joined by WHILE, describing contributions running together rather than opposed, so this is the one claim of the five the framework does not make; the other four are stated in KC-3.2.I.A and KC-3.2.I.B."),
 ("worked against hereditary privilege, so the change concerned who deserves standing",
  "KC-3.2.I.A sets individual talent OVER hereditary privilege, so privilege by birth is what the emphasis displaces, and Unit 3: Learning Objective D names attitudes about government AND THE INDIVIDUAL together."),
 ("as a people blessed with liberty",
  "KC-3.2.I.A's second clause credits religion with strengthening Americans' view of themselves as a people blessed with liberty, which a text calling liberty a trust to be proved worthy of expresses in religious language."),
 ("not contained within 1754 to 1800",
  "KC-3.2.I.B says the ideas resonated THROUGHOUT AMERICAN HISTORY, so their effect runs past the close of the unit rather than being exhausted inside it, and the framework does make a claim about their duration."),
 ("Enlightenment philosophy pressed the claim of talent against inherited rank, while religion strengthened",
  "KC-3.2.I.A assigns the talent emphasis to Enlightenment ideas and the strengthened sense of liberty to religion. The anchor carries both clauses because the leading distractor is the same sentence with the two contributions exchanged."),
 ("one philosophical and one religious, changed how colonists regarded government and the individual",
  "KC-3.2.I.A supplies the two strands, KC-3.2.I.B the belief in republican government on natural rights and the documents expressing it, and the same sentence the reach beyond the period; Unit 3: Learning Objective D asks for that change."),
]


def _extra_mutations():
    def a_quotation_appears(mod, cl):
        mod.QUESTIONS[13]["choices"][mod.QUESTIONS[13]["ans"]] = (
            'Thomas Paine\'s Common Sense, which opens "Some writers have so confounded '
            'society with government"')
        no_invented_quotation(mod)

    def optional_source_becomes_the_key(mod, cl):
        mod.QUESTIONS[8]["why"] += " Phillis Wheatley is the framework's proof of it."
        no_optional_source_key(mod)

    def the_two_strands_stop_overlapping(mod, cl):
        # q21 keys that SOME texts draw on both strands at once. Removing the
        # overlap leaves every mark a legal Yes or No and both strands still
        # present, so only the overlap count can object -- which is why this
        # check compares the text column alone.
        t = dict(mod.QUESTIONS[20]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][1][2] = "No"
        t["rows"][3][2] = "No"
        mod.QUESTIONS[20]["table"] = t

    return [
        ("a quotation put into a keyed choice", a_quotation_appears,
         r"a quotation mark appears in student-facing text"),
        ("an optional source made to carry a why", optional_source_becomes_the_key,
         r"lists under OPTIONAL SOURCES"),
        ("the overlap between the two strands removed", the_two_strands_stop_overlapping,
         r"SOME texts draw on both at once"),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    for label, mutate, expect in _extra_mutations():
        mod = wh_check._mutant(a3_4)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            wh_check.history_style(mod, claims)
            no_optional_source_key(mod)
            no_invented_quotation(mod)
            import cg_check as cg
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as e:
            assert re.search(expect, str(e)), (
                f"CONTROL FIRED FOR THE WRONG REASON: {label} -- {e}")
            print(f"  control OK  {label}: {str(e)[:110]}")
        else:
            raise SystemExit(f"CONTROL FAILED: {label} did not raise")

no_optional_source_key(a3_4)
no_invented_quotation(a3_4)
wh_check.run(a3_4, CLAIMS, TABLE_CHECKS, sys.argv)
