"""Key audit for AP WORLD HISTORY: MODERN 3.3 Empires: Belief Systems.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. `claim` states what the key rests on, for a human to audit.

The structural gate is `cg_check.check`; the notation gate and the generic
negative control -- every key rotated, every table cell corrupted -- are in
`es_check`, reused unchanged. The two history gates defined here, a required
CED citation in every `why` and a ban on figure language the bank cannot
display, carry their own negative AND positive controls.

WHAT THE KEYS REST ON
---------------------
Items 1, 2, 6, 11, 17, 20, 22, 28 and 30 rest on KC-4.1.VI.i: the Protestant
Reformation marked a break with existing Christian traditions and both the
Protestant and Catholic reformations contributed to the growth of Christianity.
Items 3, 4, 19, 26, 27 and 30 rest on KC-4.1.VI.ii: political rivalries between
the Ottoman and Safavid empires intensified the split within Islam between
Sunni and Shi'a.
Items 5, 18, 22, 25 and 30 rest on KC-4.1.VI.iii: Sikhism developed in South
Asia in a context of interactions between Hinduism and Islam.
Items 12, 13 and 21 rest on the parent statement KC-4.1.VI, on expanded reach,
religious conflicts, and syncretic belief systems and practices.
Items 7 to 10, 15, 16, 23, 24 and 29 rest on suggested skill 2.B, which names
point of view, purpose, historical situation and audience as the elements to be
explained about a source; item 14 and item 28 rest on Learning Objective C's
own framing of continuity and change.

WHAT NO ITEM ASSERTS. KC-4.1.VI.ii does not say which of the two empires stood
on which side of the Sunni and Shi'a split, so nothing here keys that. The
framework names no founder or date for Sikhism, no reformer, and no council or
doctrine of the Catholic reformation, so nothing here keys those. Every source
in a stem is explicitly hypothetical and unattributed: the topic's own sample
activity uses Martin Luther's 95 Theses, and inventing a quotation for a real
document is the one thing HISTORY_BRIEF.md forbids outright.

NEGATIVE CONTROL: `python3 verify_w3_3.py --selftest`.
"""
import re
import sys

import cg_check as cg
import es_check as es

import w3_3

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

OLDER = "Houses of worship of the older tradition"
NEWER = "Houses of worship of the newer tradition"


def _rows(table):
    return {r[0]: cg.normalize(r[1]) for r in table["rows"]}


def q15(table, item):
    m = _rows(table)
    pov = [k for k, v in m.items() if "where the writer stood" in v]
    assert pov == ["Question 1"], f"exactly one row must ask about position; got {pov}"
    assert "expected to read" in m["Question 3"], "one row must ask about readership"
    assert "trying to accomplish" in m["Question 2"], "one row must ask about aim"
    assert "happening at the time" in m["Question 4"], "one row must ask about circumstances"
    return ("exactly one of the four rows asks who the writer was and where the writer stood, "
            "while the others ask about aim, readership and circumstances")


def q16(table, item):
    m = _rows(table)
    audience = [k for k, v in m.items() if "expected to read" in v]
    assert audience == ["Question 3"], f"exactly one row must ask about audience; got {audience}"
    assert "expected to read" not in m["Question 2"], \
        "the aim row must not also be the audience row"
    assert len(m) == 4, "the audience row must be one of four, so 'all four' is false"
    return ("exactly one of the four rows asks who the writer expected to read the document, "
            "which is the audience and not the purpose")


def q17(table, item):
    old, new = cg.col(table, OLDER), cg.col(table, NEWER)
    assert all(old[i + 1] > old[i] for i in range(len(old) - 1)), \
        f"the older tradition must gain in every decade; got {old}"
    assert all(new[i + 1] > new[i] for i in range(len(new) - 1)), \
        f"the newer tradition must gain in every decade; got {new}"
    assert new[-1] > new[1], "'the newer tradition gained nothing after appearing' must be false"
    assert all(a != b for a, b in zip(old, new)), \
        "'the two are equal in every decade' must be false"
    return (f"the older tradition reads {old} and the newer {new}, both strictly rising and "
            "never equal to each other")


def q18(table, item):
    m = _rows(table)
    south = [k for k, v in m.items() if "south asia" in v]
    assert south == ["Development 3"], f"exactly one row must name South Asia; got {south}"
    assert "hinduism" in m["Development 3"], "the South Asian row must name Hinduism and Islam"
    assert "christian" in m["Development 1"], "the first row must concern Christian traditions"
    assert "south asia" not in m["Development 2"], "the second row must not name South Asia"
    return ("exactly one of the three rows locates its development in South Asia amid Hinduism "
            "and Islam, while the first concerns Christian traditions and the second a split "
            "within Islam")


CLAIMS = [
 ("break with existing Christian traditions",
  "KC-4.1.VI.i states that the Protestant Reformation marked a break with existing Christian traditions. The same sentence has both reformations contributing to the growth of Christianity, so an end to growth contradicts it; the Sunni and Shi'a split is KC-4.1.VI.ii and Sikhism KC-4.1.VI.iii."),
 ("contributed to the growth of Christianity",
  "KC-4.1.VI.i states that both the Protestant and Catholic reformations contributed to the growth of Christianity. The rejected options reverse that claim, relocate it to South Asia, or assert a unification the framework never describes."),
 ("Ottoman and Safavid empires",
  "KC-4.1.VI.ii states that political rivalries between the Ottoman and Safavid empires intensified the split within Islam between Sunni and Shi'a. The other pairs join empires KC-4.3.II.B names without connecting them to this development."),
 ("Political rivalry",
  "KC-4.1.VI.ii names political rivalries as what intensified the Sunni and Shi'a split. Atlantic shipping, American colonies and the silver trade belong to KC-4.1.III and KC-4.1.IV and are not offered as causes here."),
 # Both clauses: every distractor keeps one half of the framework's sentence
 # and changes the other, so half the anchor would match one of them.
 ("Sikhism, amid interactions between Hinduism and Islam",
  "KC-4.1.VI.iii states that Sikhism developed in South Asia in a context of interactions between Hinduism and Islam. Each rejected option preserves one half of that statement and alters the other, which is the near-miss this subject invites."),
 ("break with existing Christian traditions",
  "KC-4.1.VI.i describes the Protestant Reformation as marking a break with existing Christian traditions, and a congregation separating from the church it had belonged to is that break. The rejected options are KC-4.1.VI.ii, KC-4.1.VI.iii, KC-4.3.II.A.i and KC-4.3.I.C."),
 ("who the writer was and where the writer stood",
  "Suggested skill 2.B asks students to explain the point of view, purpose, historical situation, and/or audience of a source, and point of view is the writer's own position in relation to the subject. Word counts, paper prices, bibliographies and translation answer other questions."),
 ("persuade readers to act",
  "Suggested skill 2.B names purpose among the elements to be explained, and a pamphlet urging readers to petition their ruler is written to move them to act. The rejected options describe purposes such a pamphlet would not have."),
 ("assembled villagers to whom the sermon was preached",
  "Suggested skill 2.B names audience as an element distinct from purpose, and the audience of a sermon is those to whom it was preached. Treating audience and purpose as identical collapses a distinction the skill draws."),
 ("circumstances in the writer's world at the time",
  "Suggested skill 2.B names historical situation among the elements to be explained, and a situation is the set of circumstances surrounding a source's production. Survival rates, a modern opinion, a script and a binding are facts about the object or the reader."),
 ("compatible with that religion's overall growth",
  "KC-4.1.VI.i has the Protestant Reformation marking a break with existing Christian traditions and both reformations contributing to the growth of Christianity, so division and growth occurred together. KC-4.1.VI adds religious conflicts, so political consequences are asserted rather than denied."),
 ("syncretic belief systems and practices",
  "KC-4.1.VI states that intensified interactions expanded the reach and furthered development of existing religions and contributed to religious conflicts and the development of syncretic belief systems and practices. Each rejected option asserts the opposite of one clause of that sentence."),
 ("A syncretic belief system",
  "KC-4.1.VI names the development of syncretic belief systems and practices among the results of intensified interaction, and a community combining practices from two traditions is that development. The rejected terms belong to KC-4.3.II.A.i, KC-4.3.I.D, KC-4.3.II and KC-4.3.I.C."),
 ("continued and grew even as breaks and splits occurred",
  "Learning Objective C asks for continuity and change within the various belief systems; KC-4.1.VI.i has Christianity growing through division, KC-4.1.VI has existing religions expanding their reach, and KC-4.1.VI.ii and KC-4.1.VI.iii describe change within long-standing traditions."),
 ("Question 1",
  "Suggested skill 2.B distinguishes point of view from purpose, historical situation and audience. Recomputed in q15 above: exactly one row asks who the writer was and where the writer stood, which is point of view."),
 ("Question 3",
  "Suggested skill 2.B names audience as a separate element from purpose and situation. Recomputed in q16 above: exactly one of the four rows asks who the writer expected to read the document."),
 ("Both traditions gained houses of worship",
  "KC-4.1.VI.i states that both the Protestant and Catholic reformations contributed to the growth of Christianity, so growth on both sides of a division is what the framework leads a student to expect. Recomputed in q17 above: both columns rise in every decade and the two are never equal."),
 ("Development 3",
  "KC-4.1.VI.iii states that Sikhism developed in South Asia in a context of interactions between Hinduism and Islam. Recomputed in q18 above: exactly one row names South Asia and those two traditions, while the others describe KC-4.1.VI.i and KC-4.1.VI.ii."),
 ("intensified a split, not that it created one",
  "KC-4.1.VI.ii says the rivalry intensified the split within Islam between Sunni and Shi'a, and to intensify is to deepen what already exists. Each rejected correction denies something that same sentence states."),
 ("rising on both sides of the division",
  "KC-4.1.VI.i attaches growth in Christianity to both the Protestant and the Catholic reformations, so evidence bearing on it must count Christian communities on both sides. Shipping, garrisons, rainfall and wages document other things entirely."),
 ("contributed to religious conflicts",
  "KC-4.1.VI says intensified interaction contributed to religious conflicts and KC-4.3.III.i adds that religious disputes led to rivalries and conflict between states, so a ruler taking a side is that process. KC-4.3.I.A has rulers continuing to use religious ideas and KC-4.3.I.B records accommodation as well as suppression."),
 # Both clauses: the first distractor is the SWAP, putting the division in
 # South Asia and the new tradition in Europe.
 ("division within one religion in Europe, alongside a tradition developing amid two religions in South Asia",
  "KC-4.1.VI.i places the break with existing Christian traditions in the reformations while KC-4.1.VI.iii places Sikhism's development in South Asia amid interactions between Hinduism and Islam. The rejected options swap those regions or contradict both statements."),
 # Both clauses: a distractor opens with the same first clause.
 ("writer's position, and the readers the writer addressed",
  "Suggested skill 2.B lists point of view and audience among the elements to be explained, and a court theologian writing for the ruler's council supplies exactly those two. Survival counts, modern opinions, bindings and translations are not elements of that skill."),
 ("shapes what the source reports",
  "Suggested skill 2.B makes point of view an element to be explained precisely because the writer's position bears on how a source presents its subject. Nothing in the skill makes a partisan source unusable or restricts students to anonymous documents."),
 ("interactions between two existing traditions",
  "KC-4.1.VI.iii states that Sikhism developed in South Asia in a context of interactions between Hinduism and Islam, which is a claim about context and place. Nothing in the framework supports a European origin, an absence of contact, a Christian derivation or a later date."),
 ("Political rivalries between two empires intensified a split",
  "KC-4.1.VI.ii ties a religious development directly to the political rivalry of two empires, which is what the argument claims. The rejected statements are KC-4.2.II.D, KC-4.1.V.D, KC-4.3.II.A.iii and KC-4.1.II.A, none of which concerns religion."),
 ("political rivalry intensifying a split within a religion",
  "KC-4.1.VI.ii states that political rivalries between the Ottoman and Safavid empires intensified the split within Islam, and preaching that follows a war between two empires is that intensification. The rejected options are KC-4.1.VI.i, KC-4.1.VI.iii, KC-4.3.II.A.ii and KC-4.1.V.A."),
 ("kept growing and kept its established observances",
  "Learning Objective C asks for continuity and change within the various belief systems, and continuity is a tradition persisting. KC-4.1.VI.i's break, KC-4.1.VI.iii's new development and KC-4.1.VI.ii's intensified split are all instances of change."),
 ("audiences differ, and a source is shaped by whom it addresses",
  "Suggested skill 2.B names audience among the elements to be explained, and a public congregation and a fellow official are different audiences. Nothing in the skill ranks private sources above public ones, and two sources from one dispute may share a historical situation."),
 ("imperial rivalry deepened a split within Islam",
  "The keyed sentence joins KC-4.1.VI.i on the break and the growth of Christianity, KC-4.1.VI.ii on the intensified Sunni and Shi'a split, and KC-4.1.VI.iii on Sikhism's development in South Asia. Each rejected version contradicts at least one of the three."),
]

TABLE_CHECKS = {15: q15, 16: q16, 17: q17, 18: q18}

if __name__ == "__main__" and "--selftest" in sys.argv:
    extra_controls(w3_3)

extras(w3_3)
es.run(w3_3, CLAIMS, TABLE_CHECKS, sys.argv)
