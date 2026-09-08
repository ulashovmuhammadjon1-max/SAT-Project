"""Key audit for AP U.S. HISTORY 3.3 Taxation Without Representation.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The shared gate is
``wh_check.run``: a KC code or Learning Objective in every ``why`` and every
``claim``, no figure language, no typeset markup, the marked-stimulus rule, and
``cg_check``'s structural and anchor checks underneath.

WHAT THE KEYS REST ON
---------------------
  Unit 3 Learning Objective C, policy leading
    to war                                       items 1, 2, 3, 7, 24, 25
  KC-3.1.II.A, three causes, no representation
    or consent, perceived AND real constraints   4, 5, 6, 7, 20, 25, 28, 29, 30
  KC-3.1.II.B, four grounds for resistance       8, 9, 10, 11, 18, 22, 26, 30
  KC-3.1.II.C, leaders AND popular movements     12, 13, 14, 23, 26, 27, 30
  KC-3.1.II.D, shortages and occupation, men
    and women, financial AND material support    15, 16, 17, 23, 27, 30
  skill 2.A's four sourcing questions, and the
    WOR thematic focus                           2, 19, 20, 21, 24

THE SCOPE THIS MODULE HAS TO HOLD. This topic page carries a long OPTIONAL
SOURCES list, and the CED's own paragraph above it says those sources "are not
required AP course content" and that "None of the AP Exam questions require
students to have studied these specific sources." A key resting on one of them
would rest on something the framework has told the student they need not have
read. ``no_optional_source_key`` asserts that no keyed choice names one.

BENJAMIN FRANKLIN AND THE PATRIOT MOVEMENT ARE DELIBERATELY ABSENT from that
banned list, and this is the distinction the check exists to hold: KC-3.1.II.C
names Franklin and KC-3.1.II.D names the Patriot movement in the REQUIRED
content, while Adams, Dickinson, Hancock, Henry, Warren, Attucks, the Daughters
of Liberty and the Sons of Liberty appear only in the optional list. A checker
that banned every proper noun would ban the framework's own words, which is the
over-matching own-goal this repository keeps paying for.

THE SWAP ITEMS, where a distractor is the key with two clauses exchanged and
the anchor therefore carries BOTH: item 9 (subjects' rights against the
individual's), item 17 (kind of support and its recipient), item 27 (which
sentence describes which).

DATA ITEMS: 21, 22 and 23, all carrying HYPOTHETICAL figures, because the CED
prints no data for this topic. Items 22 and 23 state their expected rows here,
independently of the module, so every cell is load-bearing. Item 21 is
categorical and compares only its OBSERVATION column literally, so the named
control below, which marks a second row as answering the audience question,
raises on the count the key depends on rather than on a row-equality assertion
that would prove nothing about it.

NEGATIVE CONTROLS: ``python3 verify_a3_3.py --selftest``.
"""
import re
import sys

import wh_check
import a3_3

OBSERVATION = "Observation about a hypothetical pamphlet"
SOURCING = "Sourcing question the observation answers"
GROUND = "Ground appealed to (hypothetical tally)"
TALLY = "Pamphlets in which it appears"
GROUPCOL = "Group in a hypothetical district return"
MONEY = "Households contributing money"
GOODS = "Households contributing goods"

# The OPTIONAL SOURCES this topic page lists and the CED then says no exam
# question requires. Explicit lookarounds, never \b beside a letter run.
# "Adams" is matched only with a given name, so that a sentence about the
# framework's own content cannot be caught by an initial.
_OPTIONAL_SOURCE = re.compile(
    r"(?<![A-Za-z])(John Adams|Abigail Adams|Dickinson|Hancock|Patrick Henry|"
    r"Mercy Otis Warren|Crispus Attucks|Daughters of Liberty|Sons of Liberty|"
    r"Edenton|Green Mountain Boys|Paul Revere|Declaratory Act|Coercive Acts|"
    r"Stamp Act Congress|Committees of Correspondence|"
    r"Declaration of Rights and Grievances|Declaration and Resolves)(?![A-Za-z])",
    re.IGNORECASE)


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
    print(f"OK  {code} scope: no key rests on a source the framework marks optional; "
          f"Benjamin Franklin and the Patriot movement, which the required content itself "
          f"names, remain available.")


# ------------------------------------------------------------------ table checks

def _col(table, header):
    idx = table["headers"].index(header)
    return [row[idx] for row in table["rows"]]


def _nums(table, header):
    return [float(str(v).replace(",", "")) for v in _col(table, header)]


_EXPECTED_OBSERVATIONS = [
    "Its writer sat in a colonial assembly and had spoken there against the new duties",
    "It was printed in order to persuade readers to refuse the new duties",
    "It appeared in the months just after the new duties were announced",
    "It was sold cheaply in a port town where sailors and dockworkers gathered",
]
# The four sourcing questions skill 2.A names, and no others.
_SOURCING_CATEGORIES = {"Point of view", "Purpose", "Historical situation", "Audience"}


def q21(table, item):
    # ONLY THE OBSERVATION COLUMN IS COMPARED LITERALLY, so the named control
    # that marks a SECOND row 'Audience' raises on the count below rather than
    # on a row-equality assertion, which would fire for the wrong reason. A
    # corrupted category cell still fails, through the membership check: the
    # shared corrupter appends text, and 'Audience CORRUPTED' is not one of
    # skill 2.A's four questions.
    assert _col(table, OBSERVATION) == _EXPECTED_OBSERVATIONS, (
        f"the sourcing table's observations are not the ones this check was written "
        f"against; got {_col(table, OBSERVATION)}")
    marks = [m.strip() for m in _col(table, SOURCING)]
    for m in marks:
        assert m in _SOURCING_CATEGORIES, (
            f"every row must be marked with one of skill 2.A's four questions; got {m!r}")
    audience = [i for i, m in enumerate(marks) if m == "Audience"]
    assert len(audience) == 1, (
        f"the key names THE one observation about audience, so exactly one row may carry "
        f"that mark; {len(audience)} do")
    assert set(marks) == _SOURCING_CATEGORIES, (
        f"all four of skill 2.A's questions must be represented, or the rejected options "
        f"are not all false; got {marks}")
    row = audience[0]
    assert "sold" in _col(table, OBSERVATION)[row].lower(), (
        f"the audience row must be the one about where and how the pamphlet was sold; "
        f"got {_col(table, OBSERVATION)[row]!r}")
    return (f"exactly {len(audience)} of {len(marks)} rows is marked Audience, and all four "
            f"of skill 2.A's questions appear once each")


_EXPECTED_GROUNDS = [["Rights of British subjects", "31"],
                     ["Local traditions of self-rule", "24"],
                     ["Rights of the individual", "19"],
                     ["Ideas of the Enlightenment", "12"]]


def q22(table, item):
    assert [list(r) for r in table["rows"]] == _EXPECTED_GROUNDS, (
        f"the grounds table does not hold the rows this check was written against; "
        f"got {table['rows']}")
    tallies = _nums(table, TALLY)
    grounds = _col(table, GROUND)
    assert len(tallies) == 4, f"KC-3.1.II.B names four grounds; the table tallies {len(tallies)}"
    assert all(t > 0 for t in tallies), \
        f"'only one of the four grounds appears at all' must be false; got {tallies}"
    assert len(set(tallies)) == len(tallies), \
        f"'the four grounds appear in equal numbers' must be false; got {tallies}"
    least = grounds[tallies.index(min(tallies))]
    assert "self-rule" not in least.lower(), \
        f"'the ground appealed to least often is local traditions of self-rule' must be false"
    assert "enlightenment" in least.lower(), (
        f"the smallest tally must belong to Enlightenment ideas, or the last option is not "
        f"falsified; it belongs to {least!r}")
    most = grounds[tallies.index(max(tallies))]
    assert "enlightenment" not in most.lower(), \
        "'Enlightenment ideas appear more often than any other ground' must be false"
    return (f"the four tallies are {tallies}, all above zero and all different, with the "
            f"smallest against {least!r} and the largest against {most!r}")


_EXPECTED_SUPPORT = [["Laborers", "120", "150"],
                     ["Artisans", "90", "70"],
                     ["Households headed by women", "60", "110"],
                     ["Merchants", "30", "25"]]


def q23(table, item):
    assert [list(r) for r in table["rows"]] == _EXPECTED_SUPPORT, (
        f"the district return table does not hold the rows this check was written against; "
        f"got {table['rows']}")
    money, goods = _nums(table, MONEY), _nums(table, GOODS)
    groups = _col(table, GROUPCOL)
    assert all(m > 0 for m in money) and all(g > 0 for g in goods), (
        f"every group must contribute in both forms for the key to hold; got {money} and "
        f"{goods}")
    assert sum(1 for m in money if m > 0) > 1, "'only one group contributed anything' must be false"
    assert any(g > 0 for g in goods), "'none contributed goods' must be false"
    merchants = groups.index("Merchants")
    assert money[merchants] != max(money) and goods[merchants] != max(goods), (
        f"'merchants contributed more than any other group in both forms' must be false; "
        f"got {money[merchants]} and {goods[merchants]}")
    assert any(m > g for m, g in zip(money, goods)), (
        "'contributions of goods exceeded contributions of money in every group' must be "
        "false")
    return (f"all {len(groups)} groups contribute under both headings, money {money} against "
            f"goods {goods}, and the merchants lead neither column")


TABLE_CHECKS = {21: q21, 22: q22, 23: q23}

CLAIMS = [
 ("British colonial policies regarding North America led to the Revolutionary War",
  "Unit 3: Learning Objective C reads verbatim 'Explain how British colonial policies regarding North America led to the Revolutionary War', so the objective runs from policy to war rather than the other way."),
 ("point of view, purpose, historical situation, and audience",
  "Skill 2.A as printed beside this topic's title, beneath Unit 3: Learning Objective C. The distractors are skills 1.B, 3.A, 6.B and 5.A, printed on other pages of this unit, none of which is a sourcing skill."),
 ("Causation",
  "The unit's topic table assigns Causation to this topic, matching Unit 3: Learning Objective C's 'led to' and KC-3.1.II.A's account of what began to unite the colonists."),
 ("imperial struggles of the mid-18th century, new British efforts to collect taxes",
  "KC-3.1.II.A names three things together: the imperial struggles of the mid-18th century, as well as new British efforts to collect taxes without direct colonial representation or consent and to assert imperial authority in the colonies."),
 ("Without direct colonial representation or consent",
  "KC-3.1.II.A qualifies the new British efforts to collect taxes with exactly this phrase, which withholds representation AND consent together."),
 ("Perceived and real constraints on their economic activities and political rights",
  "KC-3.1.II.A ends with the colonists uniting against perceived and real constraints on their economic activities and political rights; the sentence carries two pairs at once and every distractor drops half of one."),
 ("a process getting under way in this period rather than a unity already achieved",
  "KC-3.1.II.A says the causes BEGAN TO UNITE the colonists, which marks a start rather than a completed state, and is why the sentence serves Unit 3: Learning Objective C on how policies LED TO war."),
 ("rights of British subjects, the rights of the individual, local traditions of self-rule, and the ideas of the Enlightenment",
  "KC-3.1.II.B names exactly these four grounds as the basis of colonial leaders' calls for resistance to Britain."),
 ("owed; the second is a claim about persons as such",
  "KC-3.1.II.B lists the rights of British subjects and the rights of the individual as two separate grounds, in that order. The anchor carries both halves because one distractor is the same distinction with the two terms exchanged."),
 ("Local traditions of self-rule",
  "Of KC-3.1.II.B's four grounds, this is the one appealing to established colonial practice rather than to a doctrine about what is owed."),
 ("alongside a body of thought developing outside the colonies",
  "KC-3.1.II.B names the ideas of the Enlightenment as ONE of four grounds, so the body of thought is present without being the only ground; medieval doctrine and classical antiquity are absent from the sentence."),
 ("energized by colonial leaders and also by popular movements",
  "KC-3.1.II.C states that the effort for American independence was energized by colonial leaders such as Benjamin Franklin, as well as by popular movements, so both sides are asserted together."),
 ("Laborers, artisans, and women",
  "KC-3.1.II.C names popular movements that included the political activism of laborers, artisans, and women; no other group is named in that clause."),
 ("so he stands as an example rather than as the only leader",
  "KC-3.1.II.C introduces Benjamin Franklin with the words SUCH AS, which makes him an instance of the colonial leaders who energized the effort rather than the whole of them."),
 ("Economic shortages, and the British military occupation of some regions",
  "KC-3.1.II.D opens 'In the face of economic shortages and the British military occupation of some regions', and says SOME regions rather than every region."),
 ("Men and women, mobilizing in large numbers",
  "KC-3.1.II.D states that men and women mobilized in large numbers, which names both sexes and a large scale rather than a small circle or a single sex."),
 ("Financial and material support, provided to the Patriot movement",
  "KC-3.1.II.D names both the kind of support and its recipient. The anchor carries both because each distractor keeps one and alters the other."),
 ("Local traditions of self-rule",
  "KC-3.1.II.B names local traditions of self-rule among its four grounds, and an argument resting on generations of self-government is that ground rather than a claim about individuals as such or a doctrine drawn from outside."),
 ("in order to persuade readers to stop buying certain imported goods",
  "Skill 2.A, printed on this topic page, separates a source's PURPOSE, the objective its creator pursued, from its POINT OF VIEW, which is what about the creator shaped what they said; the four rejected observations are all facts about the writer. KC-3.1.II.B supplies the content such a source would carry."),
 ("while troops were quartered in the town",
  "Skill 2.A's HISTORICAL SITUATION is what was happening at the time and place a source was created, which the rejected options do not state; KC-3.1.II.A supplies that setting in the new efforts to collect taxes and assert imperial authority, and KC-3.1.II.D in the British military occupation of some regions."),
 ("where and how cheaply the pamphlet was sold",
  "Recomputed in q21 from the table alone: exactly one row is marked Audience and it is the row about where and how cheaply the pamphlet was sold, with the other three marked as the remaining questions of skill 2.A, the skill printed beside Unit 3: Learning Objective C on this topic page."),
 ("All four of the grounds the framework names appear, though in unequal numbers",
  "Recomputed in q22 from the table alone, with each rejected option falsified against the same tallies. The four grounds tallied are exactly the four KC-3.1.II.B names."),
 ("Every group listed contributed in both forms",
  "Recomputed in q23 from the table alone. KC-3.1.II.D describes men and women mobilizing in large numbers to provide financial AND material support to the Patriot movement, and KC-3.1.II.C names laborers, artisans, and women among those active."),
 ("interactions between empires, nations, and peoples shape the development of America",
  "The America in the World thematic focus printed on this topic page; KC-3.1.II.A's imperial struggles and new British efforts are an interaction of that kind. The rejected options are the framework's thematic focuses for politics and power, social structures, migration and regional culture."),
 ("began to unite colonists against constraints, and colonial leaders and popular movements",
  "KC-3.1.II.A supplies the first link and KC-3.1.II.C the second, which together are what Unit 3: Learning Objective C means by British policies leading to the Revolutionary War."),
 ("colonial leaders confined their arguments to a single ground",
  "KC-3.1.II.B names four grounds together, so this is the one claim of the five the framework contradicts; the other four are stated in KC-3.1.II.B, KC-3.1.II.C and KC-3.1.II.D."),
 ("names who energized the effort for independence, while the second names what people did",
  "KC-3.1.II.C is about who energized the effort and KC-3.1.II.D about what men and women did under shortage and occupation. The anchor carries both clauses because the leading distractor is this distinction with the two sentences exchanged."),
 ("without deciding every case one way",
  "KC-3.1.II.A's pairing of PERCEIVED AND REAL constraints keeps the sentence from claiming that every grievance was well founded and from claiming that none was, while leaving the constraints as the thing united against."),
 ("began to unite the colonists against constraints on their economic activities",
  "KC-3.1.II.A states that new British efforts to collect taxes without direct colonial representation or consent began to unite the colonists against perceived and real constraints on their economic activities and political rights; a town agreeing with its neighbours to refuse imported goods is that uniting in action."),
 ("who argued from four distinct grounds, and both leaders and ordinary people",
  "KC-3.1.II.A gives the causes and the beginning of unity, KC-3.1.II.B four grounds rather than one, and KC-3.1.II.C and KC-3.1.II.D both leaders and ordinary men and women. Each rejected option collapses one of those sentences into a single cause, ground or participant."),
]


def _extra_mutations():
    def optional_source_becomes_the_key(mod, cl):
        mod.QUESTIONS[7]["choices"][mod.QUESTIONS[7]["ans"]] += \
            " as the Declaratory Act shows"
        no_optional_source_key(mod)

    def two_rows_marked_audience(mod, cl):
        # q21 keys THE row about audience. Marking a second row the same way
        # leaves every cell a legal category, so only the count can object --
        # which is why this check compares the observation column alone.
        t = dict(mod.QUESTIONS[20]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][1][1] = "Audience"
        mod.QUESTIONS[20]["table"] = t

    return [
        ("an optional source promoted into a keyed choice", optional_source_becomes_the_key,
         r"lists under OPTIONAL SOURCES"),
        ("a second row marked Audience, so q21's key names one of two",
         two_rows_marked_audience, r"exactly one row may carry"),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    for label, mutate, expect in _extra_mutations():
        mod = wh_check._mutant(a3_3)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            wh_check.history_style(mod, claims)
            no_optional_source_key(mod)
            import cg_check as cg
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as e:
            assert re.search(expect, str(e)), (
                f"CONTROL FIRED FOR THE WRONG REASON: {label} -- {e}")
            print(f"  control OK  {label}: {str(e)[:110]}")
        else:
            raise SystemExit(f"CONTROL FAILED: {label} did not raise")

no_optional_source_key(a3_3)
wh_check.run(a3_3, CLAIMS, TABLE_CHECKS, sys.argv)
