"""Key audit for AP WORLD HISTORY: MODERN 3.4 Comparison in Land-Based Empires.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. `claim` states what the key rests on, for a human to audit.

The structural gate is `cg_check.check`; the notation gate and the generic
negative control -- every key rotated, every table cell corrupted -- are in
`es_check`, reused unchanged. The two history gates defined here, a required
CED citation in every `why` and a ban on figure language the bank cannot
display, carry their own negative AND positive controls.

THIS IS THE UNIT'S REASONING TOPIC, so most keys rest on a skill statement
rather than on a fact. The CED's own words: the final topic in this unit
focuses on the skill of argumentation. Items 2, 5, 9, 13, 17, 22 and 28 rest on
suggested skill 6.B, which has two parts -- describe specific examples of
historically relevant evidence, and explain how specific examples of
historically relevant evidence support an argument -- and several of those
items turn on the SECOND part being a separate requirement. Items 1, 10, 20 and
22 rest on Unit 3: Learning Objective D, compare the methods by which various
empires increased their influence from 1450 to 1750, and on the comparison
reasoning process printed with the topic.

The fact content is the unit's own REVIEW list and nothing beyond it: KC-4.1,
KC-4.1.VI, KC-4.3, KC-4.3.II, KC-4.3.II.B and KC-4.3.III.i. Items 3, 4, 6, 8,
15, 19, 21, 23, 26 and 30 additionally reach back to the unit's earlier topics
at KC-4.3.I.A, KC-4.3.I.C and KC-4.3.I.D, and items 14 and 29 to KC-4.1.VI.i
and KC-4.1.VI.ii, all of which the student has studied in this unit.

WHAT NO ITEM ASSERTS. No item ranks one empire against another on anything the
framework does not itself record -- item 24 is built out of exactly that
distinction. Every stimulus is hypothetical and unattributed.

NEGATIVE CONTROL: `python3 verify_w3_4.py --selftest`.
"""
import re
import sys

import cg_check as cg
import es_check as es

import w3_4

# ------------------------------------------------------- the two history gates

# Explicit lookarounds throughout. `\b` is silently not a boundary between a
# digit and a letter, and this project has paid for that four separate times.
_CITE = re.compile(
    r"(?<![A-Za-z0-9])(?:KC-\d\.\d"
    r"|Learning Objective [A-N](?![A-Za-z])"
    r"|[Ss]uggested skill \d\.[A-E](?![A-Za-z])"
    r"|thematic focus(?![A-Za-z]))"
)

_FIGURE = [
    re.compile(r"(?<![A-Za-z])the (?:map|image|picture|photograph|painting|cartoon|graph|"
               r"chart|diagram)s? (?:above|below|shown|shows|depicts|indicates)(?![A-Za-z])",
               re.IGNORECASE),
    re.compile(r"(?<![A-Za-z])in the (?:image|map|photograph|painting|cartoon)(?![A-Za-z])",
               re.IGNORECASE),
    re.compile(r"(?<![A-Za-z])(?:pictured|illustrated|depicted) (?:above|below)(?![A-Za-z])",
               re.IGNORECASE),
]


def cited(module):
    """Every `why` names the CED statement its key rests on."""
    for i, item in enumerate(module.QUESTIONS, 1):
        assert _CITE.search(item["why"]), (
            f"{module.TOPIC[0]} q{i}: why cites no CED statement -- {item['why'][:80]!r}"
        )
    print(f"OK  {module.TOPIC[0]} citations: all {len(module.QUESTIONS)} whys name a "
          "CED statement.")


def no_figure_language(module):
    """No student-facing text may point at a picture the bank cannot show."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in es.texts(item):
            for pat in _FIGURE:
                hit = pat.search(text)
                assert not hit, (
                    f"{module.TOPIC[0]} q{i}: refers to a figure the bank cannot display "
                    f"-- {hit.group(0)!r}"
                )
    print(f"OK  {module.TOPIC[0]} figures: no question sends a student to an image.")


def extras(module):
    cited(module)
    no_figure_language(module)


def extra_controls(module):
    """Negative AND positive controls for the two gates defined above."""
    import copy
    import types

    def mutant():
        m = types.ModuleType(module.__name__ + "_mutant")
        m.TOPIC = module.TOPIC
        m.QUESTIONS = copy.deepcopy(module.QUESTIONS)
        return m

    def must_raise(label, mutate, gate):
        mod = mutant()
        mutate(mod)
        try:
            gate(mod)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:80]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def must_pass(label, mutate, gate):
        mod = mutant()
        mutate(mod)
        try:
            gate(mod)
        except AssertionError as exc:
            raise SystemExit(f"CONTROL FAILED: {label} was rejected -- {exc}")
        print(f"  control OK  {label}: accepted, as legal text must be")

    def strip_citation(mod):
        mod.QUESTIONS[6]["why"] = ("The framework says so plainly and the other options are "
                                   "simply not what it says anywhere at all.")

    def map_language(mod):
        mod.QUESTIONS[0]["q"] = ("The map below shows four provinces. Which was governed by "
                                 "salaried officials?")

    def image_language(mod):
        mod.QUESTIONS[1]["q"] = ("In the image, a ruler is shown enthroned before his court. "
                                 "What does this best illustrate?")

    def legal_picture_word(mod):
        mod.QUESTIONS[2]["why"] = ("KC-4.3.I.A gives the fullest picture of how rulers "
                                   "legitimized their rule, and the table below is not an "
                                   "image at all.")

    print("history-specific controls:")
    must_raise("a why stripped of its CED citation", strip_citation, cited)
    must_raise("a stem sending the student to a map", map_language, no_figure_language)
    must_raise("a stem sending the student to an image", image_language, no_figure_language)
    # POSITIVE control: a gate that rejects everything catches nothing.
    must_pass("legal prose containing 'picture of' and 'the table below'",
              legal_picture_word, no_figure_language)
    must_pass("legal prose containing 'picture of' still counts as cited",
              legal_picture_word, cited)


# ------------------------------------------------------------ table recomputes

EMPA = "Empire A"
EMPB = "Empire B"
SALARIED = "Provinces governed by salaried officials of the ruler"
FARMED = "Provinces whose taxes were farmed to contractors"
BUILDINGS = "Major religious buildings raised by the ruler"


def _rows(table):
    return {r[0]: cg.normalize(r[1]) for r in table["rows"]}


def q4(table, item):
    m = _rows(table)
    assert "artillery" in m["Evidence 1"], "the first row must record artillery"
    assert "duties" in m["Evidence 3"] and "garrisoned" in m["Evidence 3"], \
        "the third row must record duties levied at a garrisoned post"
    assert "artillery" not in m["Evidence 2"] and "duties" not in m["Evidence 2"], \
        "the second row must bear on neither armed force nor armed commerce"
    assert "rainfall" in m["Evidence 4"], "the fourth row must record rainfall"
    return ("the first row records an artillery train and the third duties levied at a "
            "garrisoned post, while the second counts pages and the fourth records rainfall")


def q5(table, item):
    m = _rows(table)
    assert "two centuries later" in m["Evidence 4"], \
        "the rainfall row must be dated two centuries after the events"
    assert "two centuries later" not in m["Evidence 1"], \
        "the artillery row must not carry the same distance in time"
    return ("the rainfall row is explicitly dated two centuries after the annexation it would "
            "be used to explain")


def q6(table, item):
    salaried = {c: cg.cell(table, SALARIED, c) for c in (EMPA, EMPB)}
    farmed = {c: cg.cell(table, FARMED, c) for c in (EMPA, EMPB)}
    built = {c: cg.cell(table, BUILDINGS, c) for c in (EMPA, EMPB)}
    assert salaried[EMPA] > salaried[EMPB] and farmed[EMPB] > farmed[EMPA], (
        "the two empires must lean opposite ways on the two fiscal rows; "
        f"got salaried {salaried} and farmed {farmed}")
    assert salaried != farmed, "'identical in how revenue was collected' must be false"
    assert abs(built[EMPA] - built[EMPB]) <= 1, \
        f"religious building must be similar, so 'differed sharply' is false; got {built}"
    assert min(salaried.values()) > 0, "'neither used salaried officials' must be false"
    assert min(farmed.values()) > 0, "'neither farmed any taxes' must be false"
    return (f"salaried provinces read {salaried} and farmed provinces {farmed}, leaning "
            f"opposite ways, while religious buildings read {built}, differing by one")


def q7(table, item):
    m = _rows(table)
    assert "gunpowder" in m["Claim 1"], "the first draft must assert the use of gunpowder"
    assert "neither ever" in m["Claim 2"] and "force" in m["Claim 2"], \
        "the second draft must deny the use of force"
    assert "western hemisphere" in m["Claim 3"], \
        "the third draft must place the empires in the Western Hemisphere"
    assert "western hemisphere" not in m["Claim 1"] and "neither ever" not in m["Claim 1"], \
        "the first draft must carry neither of the two contradictions"
    return ("only the first draft asserts the gunpowder use the framework describes, while the "
            "second denies force and the third relocates the land empires to the Western "
            "Hemisphere")


CLAIMS = [
 ("differed in how they raised the revenue to pay for it",
  "Unit 3: Learning Objective D asks students to compare the methods by which various empires increased their influence, so a comparison must run along a stated axis. The keyed pair names a similarity from KC-4.3.II and a difference from KC-4.3.I.D, while the rejected pairs set two facts side by side with no axis at all."),
 ("bears on the claim the argument actually makes",
  "Suggested skill 6.B is stated in two parts, describing specific examples of historically relevant evidence and explaining how they support an argument, so relevance is a relation between evidence and claim rather than a property of a source's length, date or language."),
 # Both clauses: a distractor opens with the same first clause and changes
 # only the second.
 ("Artillery in each empire's campaigns, together with the different ways each raised revenue",
  "KC-4.3.II supplies the shared military means and KC-4.3.I.D the differing revenue methods, so a thesis asserting both halves needs one piece of evidence for each. Every rejected pair evidences one half twice, or neither."),
 ("Evidence 1 and Evidence 3",
  "KC-4.3.II names gunpowder, cannons, and armed trade as the means of imperial expansion. Recomputed in q4 above: the first row records an artillery train and the third duties levied at a garrisoned post, while the second counts pages and the fourth records rainfall."),
 ("two centuries after the events",
  "Suggested skill 6.B requires evidence to be historically relevant to the argument it supports, and q5 above confirms the rainfall row is dated two centuries after the annexation. Being written, numerical, provincial or rare has no bearing on relevance."),
 # Both clauses: one distractor asserts the second clause's opposite while
 # sharing its subject, so half the anchor would not separate them.
 ("differed in how provincial revenue was collected but were similar in the scale of their religious building",
  "KC-4.3.I.D names tax farming among the revenue methods and KC-4.3.I.A names monumental architecture among the means of legitimation. Recomputed in q6 above: the two empires lean opposite ways on the fiscal rows and differ by one on religious buildings, and both used both fiscal methods somewhere."),
 ("Claim 1",
  "KC-4.3.II states that imperial expansion relied on gunpowder, cannons, and armed trade, and KC-4.3.II.B places these land empires across Asia, the Middle East, Southern Europe and North Africa. Recomputed in q7 above: only the first draft avoids contradicting one of those two statements."),
 ("sharply different methods of raising revenue",
  "KC-4.3.II, KC-4.3.I.A and KC-4.3.I.C describe practices shared across these empires, so evidence of them supports rather than weakens a likeness argument. KC-4.3.I.D names several distinct revenue methods, which is where the framework itself locates variation."),
 ("the reason it bears on the claim is then explained",
  "Suggested skill 6.B has two parts, describing specific examples and explaining how they support an argument, so naming an example performs only half the task. Length, position and restatement do not perform the second half."),
 ("gunpowder weaponry and armed commerce",
  "KC-4.3.II makes gunpowder, cannons, and armed trade the framework's explanation of imperial expansion, so that is the axis on which a comparison of causes runs. Modern renown, modern borders, name lengths and portrait survival are facts about the record or the present."),
 ("shaping and being shaped by the diverse populations",
  "KC-4.3 states that empires achieved increased scope and influence around the world, shaping and being shaped by the diverse populations they incorporated. The rejected statements are KC-4.3.II, KC-4.3.III.i, KC-4.1.VI.i and KC-4.1.III, none of which concerns incorporated populations."),
 ("influence run in both directions",
  "KC-4.3's phrase is shaping AND being shaped, which is a two-way relation. Each rejected reading denies one half of that phrase or draws a conclusion about expansion the sentence does not support."),
 ("how the named evidence supports the argument",
  "Suggested skill 6.B requires both describing specific examples of historically relevant evidence and explaining how those examples support an argument, and a bare list of names and dates performs only the first."),
 ("political and religious disputes set states against one another",
  "KC-4.3.III.i states that political and religious disputes led to rivalries and conflict between states and KC-4.1.VI adds that intensified interactions contributed to religious conflicts. Each rejected option denies a connection both statements assert."),
 ("artillery campaign, a new revenue system, and a programme of monumental building",
  "KC-4.3.II supplies military means, KC-4.3.I.D revenue methods and KC-4.3.I.A legitimation through art and monumental architecture, so an argument about more than one kind of method needs an example drawn from more than one statement. Each rejected set repeats a single kind."),
 ("regions in which each was situated",
  "KC-4.3.II.B assigns each land empire a region: the Manchu in Central and East Asia, the Mughal in South and Central Asia, the Ottoman in Southern Europe, the Middle East, and North Africa, and the Safavids in the Middle East. The framework records nothing about heights, court poetry, robes or calendars."),
 ("claim about what the similarity shows",
  "Suggested skill 6.B asks students to support an argument using specific and relevant evidence, which presupposes a claim for the evidence to support. Repetition, an exhaustive list, a publication date and an assertion of importance supply no claim."),
 ("Both used means the framework names",
  "KC-4.3.II names gunpowder, cannons, AND armed trade in one sentence as what imperial expansion relied on, so conquest and armed commerce both fall within its account. Each rejected option drops one of the three or denies the sentence entirely."),
 ("administration, revenue and legitimation",
  "KC-4.3.I.A, KC-4.3.I.C and KC-4.3.I.D describe legitimation, recruited elites and revenue systems alongside the military means of KC-4.3.II, so military technology alone does not exhaust the unit's account. The rejected options contradict statements the unit makes outright."),
 ("methods by which empires increased their influence, which covers both",
  "Unit 3: Learning Objective D asks for a comparison of the methods by which various empires increased their influence from 1450 to 1750, and the unit supplies both expansion at KC-4.3.II and administration at KC-4.3.I.A, KC-4.3.I.C and KC-4.3.I.D as such methods."),
 ("spent on the campaigns that took the next one",
  "KC-4.3.I.D says rulers used tribute collection, tax farming, and innovative tax-collection systems to generate revenue in order to forward state power and expansion, which is exactly the connection the claim asserts. A list, the weather, a staff count and one village's tax show no such link."),
 ("similarities and differences along a stated axis",
  "The reasoning process printed with this topic is comparison and Unit 3: Learning Objective D asks students to compare methods, which requires a shared axis rather than two separate lists. Nothing there fixes the conclusion in advance, sets a minimum number of cases, or confines comparison to one region."),
 ("shared method of legitimizing rule",
  "KC-4.3.I.A states that rulers continued to use religious ideas, art, and monumental architecture to legitimize their rule, so two such buildings evidence a shared method. Alliance, shared belief, an absence of force and identical finances are conclusions the evidence does not reach."),
 ("one empire's army was better trained than another's",
  "The four rejected statements are KC-4.3.II, KC-4.3.II.B, KC-4.3.III.i and KC-4.3 almost verbatim. The framework makes no comparative judgement about the training of any army, so that claim would have to be defended from outside it."),
 ("interconnection of the Eastern and Western Hemispheres",
  "KC-4.1, printed in this topic's review list, states that the interconnection of the Eastern and Western Hemispheres, made possible by transoceanic voyaging, transformed trade and had a significant social impact on the world. The rejected statements concern the empires internally."),
 # Both clauses: a distractor opens with the same first clause.
 ("religious ideas to legitimize rule, and that religious disputes led to conflict",
  "KC-4.3.I.A has rulers using religious ideas to legitimize their rule and KC-4.3.III.i has religious disputes leading to rivalries and conflict between states, so the two together give religion a role inside and between empires. Ship design is KC-4.1.II.A and American crops KC-4.1.V.D."),
 ("without ranking them for any empire",
  "KC-4.3.II names three means together and KC-4.3.II.B names four empires in four regions, but nothing there assigns a single dominant cause to any one of them. The rejected options contradict the plain content of both statements."),
 ("second specific example and explain how it too supports",
  "Suggested skill 6.B asks for specific examples of historically relevant evidence and for an explanation of how they support the argument, so a second worked example advances both halves. Repetition, an unnamed multitude, a bare assertion and a footnote advance neither."),
 ("both saw division as well as growth",
  "KC-4.3 has empires achieving increased scope and influence and KC-4.1.VI has interactions expanding the reach of existing religions while contributing to religious conflicts, with KC-4.1.VI.i and KC-4.1.VI.ii supplying the division. KC-4.3.II locates imperial expansion in both hemispheres."),
 ("differing in how they raised revenue and legitimized rule",
  "The keyed sentence names a similarity from KC-4.3.II and differences drawn from KC-4.3.I.D and KC-4.3.I.A, which is what Unit 3: Learning Objective D asks for. Each rejected version contradicts KC-4.3.II, KC-4.3, KC-4.3.II.B or KC-4.1."),
]

TABLE_CHECKS = {4: q4, 5: q5, 6: q6, 7: q7}

if __name__ == "__main__" and "--selftest" in sys.argv:
    extra_controls(w3_4)

extras(w3_4)
es.run(w3_4, CLAIMS, TABLE_CHECKS, sys.argv)
