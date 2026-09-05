"""Key audit for AP WORLD HISTORY: MODERN 4.1 Technological Innovations from 1450 to 1750.

WHY THIS FILE EXISTS AT ALL. `w4_1.py` was authored by an agent that was stopped
before it wrote a verifier, so thirty questions sat in the tree with NO gate on
them -- not a weak gate, none. Every item below was re-read against the CED
before this file was written, and two stems were tightened where the trace from
stimulus to key ran through my own knowledge rather than through the framework:
q18's keyed context named the Mediterranean and the Indian Ocean, which the CED
does not say, and is now KC-4.1.II's own list of worlds; q19's inventory listed
"charts of distant coasts", which is not KC-4.1.II.A's "regional wind and
currents patterns", and now records the winds and currents of a route. Nothing
else was changed and no key moved.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. `claim` states what the key rests on, for a human to audit.

The structural gate is `cg_check.check`; the notation gate (no backslash, no
caret, no digit-hyphen-digit range, no dollar sign, no non-ASCII) and the
generic negative control -- every key rotated, every table cell corrupted -- are
in `es_check`, reused unchanged. Three further gates are defined here.

CITATION. Every `why` must carry a CED reference: a `KC-` code, a named Learning
Objective, a suggested skill, or the thematic focus (two items rest on the
Technology and Innovation focus printed with this topic, which is framework text
carrying no KC code of its own). HISTORY_BRIEF.md's whole gate is that a key
traces to a sentence in the framework, and an uncited `why` is exactly the
question nobody can check later.

FIGURE LANGUAGE. The bank cannot show images, so a stem may never send a student
to look at a map or a picture. This unit invites maps more than any other, which
is why the gate matters here. The patterns are deliberately narrow: they require
a display word FOLLOWED by shows/depicts/above/below, so "the fullest picture
of" and a distractor naming a diagram as a concept do not trip them -- both were
real false findings elsewhere in this repo. "The table below" is legal and stays
legal, because a `table=` really is there.

MARKED STIMULUS. Section I is stimulus-based and this module carries seven
invented sources. HISTORY_BRIEF.md forbids putting words in a real person's
mouth, so every stem that introduces a source document must say in the stem that
it is hypothetical, unattributed or illustrative. What the check can and cannot
do, stated plainly: it proves the LABEL is present, not that the label is
honest. A stem reading "a hypothetical letter of Zheng He" would pass it. That
one is left to the reading, and no stem here names any person at all.

WHAT THE KEYS REST ON
---------------------
Items 1, 3, 9, 14, 16, 18, 23 and 28 rest on KC-4.1.II: knowledge, scientific
learning, and technology from the Classical, Islamic, and Asian worlds spread,
facilitating European technological developments and innovation. Several of them
turn on the DIRECTION of that spread, and each such item's anchor carries both
clauses because the distractor is the exact reversal.

Items 2, 6, 7, 8, 10, 12, 13, 17, 19, 22, 24, 25, 27 and 30 rest on KC-4.1.II.A:
the developments included the production of new tools, innovations in ship
designs, and an improved understanding of regional wind and currents patterns,
all of which made transoceanic travel and trade possible.

Items 4, 5 and 11 rest on the illustrative examples printed beside Unit 4:
Learning Objective A, under their two headings -- caravel, carrack and fluyt
under innovations in ship design; lateen sail, compass and astronomical charts
under European technological developments influenced by cross-cultural
interactions with the Classical, Islamic, and Asian worlds.

Items 15 and 29 rest on Unit 4: Learning Objective A itself, and items 9 and 18
additionally on suggested skill 4.A. Items 20 and 21 rest on the Technology and
Innovation thematic focus. Item 26 reaches to KC-4.1.III and KC-4.1.IV.C, both
studied in this unit, and item 27 compares with KC-4.3.II from unit 3.

WHAT NO ITEM ASSERTS. The framework dates none of these devices, names no
inventor, explains how none of them worked, and ranks none above another -- item
22 is built out of exactly that last distinction. It nowhere says Europeans were
the only people navigating oceans, and no item implies it.

NEGATIVE CONTROL: `python3 verify_w4_1.py --selftest`.
"""
import re
import sys

import cg_check as cg
import es_check as es

import w4_1

# ----------------------------------------------------- the three history gates

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

# A stem that INTRODUCES one of these has introduced a SOURCE, and a source in
# this bank is invented. Explicit lookarounds so "recording" does not count as
# "record" and "instructions" does count as "instruction".
#
# The indefinite article is load-bearing and was not in the first draft of this
# gate. Without it the pattern fired on q16's "the direction of technological
# diffusion in the framework's ACCOUNT of this period" -- a reference to the CED
# itself, not an invented document, and a textbook false finding of exactly the
# kind this repo keeps paying for. A stimulus is introduced ("A hypothetical
# shipwright's notebook describes..."), never referred back to with "the". The
# false finding is kept below as a positive control so nobody widens this again.
_SOURCE_NOUN = re.compile(
    r"(?<![A-Za-z])[Aa]n? (?:[A-Za-z']+ ){0,3}"
    r"(?:account|notebook|letter|book|treatise|inventory|instruction|chronicle|record|"
    r"manual|logbook|memoir|report|petition|decree|dispatch|ledger|testimony)s?(?![A-Za-z])")
_MARKED = re.compile(r"(?<![A-Za-z])(?:hypothetical|unattributed|illustrative)(?![A-Za-z])",
                     re.IGNORECASE)


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


def marked_stimulus(module):
    """A stem that introduces a source must say the source is invented."""
    n = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        hit = _SOURCE_NOUN.search(item["q"])
        if not hit:
            continue
        n += 1
        assert _MARKED.search(item["q"]), (
            f"{module.TOPIC[0]} q{i}: the stem introduces a {hit.group(0)!r} without "
            f"marking it hypothetical, unattributed or illustrative -- {item['q'][:90]!r}"
        )
    print(f"OK  {module.TOPIC[0]} stimuli: all {n} source-bearing stems are marked invented.")


def extras(module):
    cited(module)
    no_figure_language(module)
    marked_stimulus(module)


def extra_controls(module):
    """Negative AND positive controls for the three gates defined above."""
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
            print(f"  control OK  {label}: {str(exc)[:90]}")
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
        mod.QUESTIONS[3]["why"] = ("The framework says so plainly and the other options are "
                                   "simply not what it says anywhere at all.")

    def map_language(mod):
        mod.QUESTIONS[0]["q"] = ("The map below shows the routes sailed in the period. Which "
                                 "worlds did the learning spread from?")

    def image_language(mod):
        mod.QUESTIONS[1]["q"] = ("In the image, a caravel is drawn beside an older vessel. "
                                 "Which list does the framework give?")

    def unmarked_source(mod):
        # q6's stem, with the one word that marks it invented removed. The
        # source noun 'notebook' stays, so it is the MARK that is missing and
        # the mark is what this gate is about.
        mod.QUESTIONS[5]["q"] = mod.QUESTIONS[5]["q"].replace("A hypothetical shipwright's",
                                                              "A shipwright's")

    def legal_picture_word(mod):
        mod.QUESTIONS[2]["why"] = ("KC-4.1.II gives the fullest picture of the diffusion, and "
                                   "the table below is not an image at all.")

    def stem_without_a_source(mod):
        # No source noun at all: the stimulus gate must stay silent rather than
        # demanding the word 'hypothetical' of every stem in the module.
        mod.QUESTIONS[7]["q"] = ("The framework says the developments of this topic made "
                                 "something possible. What, according to that sentence?")

    def framework_account(mod):
        # THE REAL FALSE FINDING. The first draft of the stimulus gate rejected
        # q16 for the phrase "the framework's account", which introduces no
        # document at all. It must stay legal.
        mod.QUESTIONS[8]["q"] = ("Which statement best describes the direction of diffusion in "
                                 "the framework's account, and in the report of the unit "
                                 "overview, of this period?")

    print("history-specific controls:")
    must_raise("a why stripped of its CED citation", strip_citation, cited)
    must_raise("a stem sending the student to a map", map_language, no_figure_language)
    must_raise("a stem sending the student to an image", image_language, no_figure_language)
    must_raise("a source-bearing stem with its 'hypothetical' removed",
               unmarked_source, marked_stimulus)
    # POSITIVE controls. A gate that rejects everything catches nothing, and the
    # phrases below are exactly the false findings this repo has already shipped
    # from an over-matching figure check and from an over-broad word list.
    must_pass("legal prose containing 'picture of' and 'the table below'",
              legal_picture_word, no_figure_language)
    must_pass("legal prose containing 'picture of' still counts as cited",
              legal_picture_word, cited)
    must_pass("a stem that introduces no source at all", stem_without_a_source,
              marked_stimulus)
    must_pass("a stem naming the framework's own account and report",
              framework_account, marked_stimulus)


# ------------------------------------------------------------ table recomputes

ITEM = "Item named in the framework"
HEADING = "Heading it is printed under"
ATTEMPTED = "Crossings attempted"
COMPLETED = "Crossings completed"

# The framework's own illustrative examples for this topic, under the two
# headings it prints them beneath. Nothing else may appear in q11's table.
SHIP_DESIGN = {"caravel", "carrack", "fluyt"}
INFLUENCED = {"lateen sail", "compass", "astronomical charts"}


def q11(table, item):
    names = [cg.normalize(r[0]) for r in table["rows"]]
    headings = [cg.normalize(r[1]) for r in table["rows"]]
    for name in names:
        assert name in SHIP_DESIGN | INFLUENCED, (
            f"{name!r} is not one of the framework's illustrative examples for this topic"
        )
    ships = [n for n, h in zip(names, headings) if "ship design" in h]
    cross = [n for n, h in zip(names, headings) if "cross-cultural" in h]
    assert len(ships) == 2 and len(cross) == 2, (
        f"the key says two of each; the table gives {len(ships)} ship designs and "
        f"{len(cross)} cross-cultural developments"
    )
    assert len(ships) + len(cross) == len(names), \
        "every row must sit under one of the two headings the framework prints"
    assert set(ships) <= SHIP_DESIGN, \
        f"{sorted(set(ships) - SHIP_DESIGN)} is not printed under innovations in ship design"
    assert set(cross) <= INFLUENCED, \
        f"{sorted(set(cross) - INFLUENCED)} is not printed under the cross-cultural heading"
    assert len(set(headings)) == 2, \
        "'the four items are printed under four different headings' must be false"
    return (f"the four rows are {names}, splitting two under innovations in ship design and "
            f"two under European developments influenced by cross-cultural interactions")


def q12(table, item):
    attempted = cg.col(table, ATTEMPTED)
    completed = cg.col(table, COMPLETED)
    assert all(a > 0 for a in attempted), "a period with no attempts has no share to compute"
    shares = [c / a for c, a in zip(completed, attempted)]
    assert all(attempted[i + 1] > attempted[i] for i in range(len(attempted) - 1)), \
        f"crossings attempted must rise at every step; got {attempted}"
    assert all(shares[i + 1] > shares[i] for i in range(len(shares) - 1)), \
        f"the completed share must rise at every step; got {shares}"
    assert all(c < a for c, a in zip(completed, attempted)), \
        "'every crossing attempted was completed' must be false in every period"
    return (f"crossings attempted read {attempted} and the completed shares "
            f"{[round(s, 2) for s in shares]}, both strictly rising, and no period completed "
            "every crossing it attempted")


def q13(table, item):
    text = {r[0]: cg.normalize(r[1]) for r in table["rows"]}
    assert len(text) == len(table["rows"]), "each development must have its own row label"
    first, second = text["Development 1"], text["Development 2"]
    third, fourth = text["Development 3"], text["Development 4"]
    # One row for each of KC-4.1.II.A's three named developments, and one that is
    # none of them. 'winds and currents' rather than 'wind', because the second
    # row legitimately says 'closer to the wind' and a bare substring would call
    # it the third development too -- the under/over-matching own-goal.
    assert "tool" in first, "the first row must describe the production of a new tool"
    assert "winds and currents" not in first and "hull" not in first, \
        "the first row must be a tool and nothing else"
    assert "hull" in second and "rig" in second, \
        "the second row must describe an innovation in ship design"
    assert "tool" not in second and "winds and currents" not in second, \
        "the second row must be a ship design and nothing else"
    assert "winds and currents" in third, \
        "the third row must describe an understanding of regional winds and currents"
    assert "tool" not in third and "hull" not in third, \
        "the third row must be the wind and currents understanding and nothing else"
    for word in ("tool", "hull", "rig", "wind", "current", "ship", "sail"):
        assert word not in fourth, (
            f"the fourth row must fall outside the framework's three developments, "
            f"but it mentions {word!r}"
        )
    return ("the first three rows are a new tool, a ship design and an understanding of a "
            "region's winds and currents, one for each development KC-4.1.II.A names, while "
            "the fourth is a roofing tile and is none of them")


CLAIMS = [
 ("Classical, Islamic, and Asian worlds",
  "KC-4.1.II names the Classical, Islamic, and Asian worlds as the worlds from which knowledge, scientific learning, and technology spread, facilitating European technological developments and innovation. The framework names no other set of sources for this diffusion anywhere in the unit."),
 ("innovations in ship designs, and an improved understanding",
  "KC-4.1.II.A names the production of new tools, innovations in ship designs, and an improved understanding of regional wind and currents patterns, and says all of them made transoceanic travel and trade possible. The rejected lists are KC-4.3.II on expansion, KC-4.3.I.D on revenue and KC-4.2.II.D on labor systems."),
 # Both clauses: the distractor reverses the direction of the spread, and either
 # half alone ('technology spread') matches the reversal just as well.
 ("from other worlds spread and facilitated those European developments",
  "KC-4.1.II has knowledge, scientific learning, and technology from the Classical, Islamic, and Asian worlds spreading and facilitating European developments, so isolation is what the framework denies and the reversed direction is what it does not say."),
 ("caravel",
  "The illustrative examples printed beside Unit 4: Learning Objective A give the caravel, the carrack and the fluyt under innovations in ship design, while the compass and astronomical charts sit under the separate cross-cultural heading. Joint-stock companies are KC-4.1.IV.C and the encomienda KC-4.2.II.D."),
 ("European developments influenced by cross-cultural interactions",
  "The heading printed above the lateen sail, the compass and astronomical charts reads: European technological developments influenced by cross-cultural interactions with the Classical, Islamic, and Asian worlds, which is KC-4.1.II in the illustrative examples' own words. The rejected descriptions belong to KC-4.2.II.D, KC-4.3.I.A, KC-4.3.II.A.i and KC-4.1.V.A."),
 ("innovation in ship design",
  "KC-4.1.II.A names innovations in ship designs among the three developments that made transoceanic travel and trade possible, and a hull and rig that hold a course closer to the wind are that. The rejected terms belong to KC-4.3.I.D, KC-4.1.VI, KC-4.3.II.A.i and KC-4.2.II.D."),
 ("improved understanding of regional wind and currents",
  "KC-4.1.II.A names an improved understanding of regional wind and currents patterns as one of the three developments, and a seasonal record of the winds and currents of one route is that understanding written down. New tools and ship designs are the other two items in the same sentence."),
 ("Transoceanic travel and trade",
  "KC-4.1.II.A ends by saying that new tools, innovations in ship designs, and an improved understanding of regional wind and currents patterns all made transoceanic travel and trade possible. KC-4.2.II.C, KC-4.1.VI, KC-4.3.III.i and KC-4.1.IV each contradict one of the rejected options."),
 ("spread of knowledge and technology from the Classical",
  "Suggested skill 4.A asks a student to identify and describe a historical context for a specific development, and KC-4.1.II supplies exactly that context for European navigation. A single year's rainfall, a headcount, a paint colour and a ship's name are details rather than contexts."),
 ("made transoceanic travel and trade possible",
  "KC-4.1.II.A states in its own words that these developments made transoceanic travel and trade possible, which is a causal link the framework asserts rather than one a student supplies. Each rejected option denies or reverses that link."),
 # Both clauses: two distractors say ALL FOUR items fall under one heading, and
 # either half of the key matches one of them.
 ("ship designs and two are developments influenced by cross-cultural interaction",
  "The framework prints the caravel, carrack and fluyt under innovations in ship design and the lateen sail, compass and astronomical charts under European developments influenced by cross-cultural interactions, which is the split KC-4.1.II and KC-4.1.II.A describe. Recomputed in q11 above: two rows fall under each heading and no row falls outside them."),
 # Both clauses: the two swap distractors move one column up and the other down.
 ("crossings attempted and the share completed rose",
  "KC-4.1.II.A ties an improved understanding of regional wind and currents patterns to making transoceanic travel and trade possible. Recomputed in q12 above: attempts rise across the three periods, the completed share rises with them, and no period completed every crossing attempted."),
 ("first three developments only",
  "KC-4.1.II.A names the production of new tools, innovations in ship designs, and an improved understanding of regional wind and currents patterns. Recomputed in q13 above: the first three rows are one of each and the roofing tile is none of them."),
 ("follows methods set out in earlier works from another world",
  "KC-4.1.II claims that knowledge, scientific learning, and technology from the Classical, Islamic, and Asian worlds spread and facilitated European developments, so evidence for it must show a European work depending on earlier learning from elsewhere. Ship counts, crew lists, timber tallies and weather reports show no such dependence."),
 ("technological developments changed patterns of trade and travel",
  "Unit 4: Learning Objective A asks how cross-cultural interactions resulted in the diffusion of technology and facilitated changes in patterns of trade and travel, and KC-4.1.II.A says the resulting developments made transoceanic travel and trade possible. KC-4.1.IV has regional markets continuing to flourish, which one rejected option denies."),
 # Both clauses: the distractor is the exact reversal of the diffusion, which is
 # the single easiest wrong key to ship in this topic.
 ("Classical, Islamic, and Asian worlds spread and facilitated European innovation",
  "KC-4.1.II gives the direction explicitly: knowledge, scientific learning, and technology FROM those worlds spread, facilitating European technological developments and innovation. The reversal reads just as well and is not what the sentence says."),
 ("beside new tools and ship designs",
  "KC-4.1.II.A places an improved understanding of regional wind and currents patterns in one list with new tools and innovations in ship designs and says all of them made ocean travel and trade possible. Each rejected option contradicts part of that same sentence."),
 ("long exchange of technical knowledge",
  "Suggested skill 4.A asks for a historical context for a specific development, and KC-4.1.II supplies one in the framework's own terms: the spread of knowledge, scientific learning, and technology from the Classical, Islamic, and Asian worlds. A launch date, a nail count, one owner's taste and a modern museum are not contexts."),
 # Both clauses: a distractor keeps the first half ('the production of new
 # tools') and swaps the second, so half the anchor would match it.
 ("new tools, and an improved understanding of regional wind",
  "KC-4.1.II.A names new tools and an improved understanding of regional wind and currents patterns among its three developments; instruments for taking bearings are tools and a chart of a route's winds and currents is that understanding. Plantations are KC-4.2.II.C, syncretism KC-4.1.VI, companies KC-4.1.IV.C and officials KC-4.3.I.C."),
 ("human adaptation and innovation",
  "The Technology and Innovation thematic focus printed with this topic says human adaptation and innovation have resulted in increased efficiency, comfort, and security and that technological advances have shaped human development. The rejected descriptions are the Governance, Social Interactions, Humans and the Environment and Cultural Developments thematic focuses."),
 ("both intended and unintended consequences",
  "The same Technology and Innovation thematic focus says technological advances have shaped human development and interactions with both intended and unintended consequences, which is what licenses treating unintended consequences as part of the subject. The rejected statements are KC-4.3.I.A, KC-4.3.II.B, KC-4.2.II.A and KC-5.3.III.C."),
 ("one list of developments the framework does not rank",
  "KC-4.1.II.A names new tools and innovations in ship designs in a single list and says all of the listed developments made transoceanic travel and trade possible, without ordering them. Asserting a rank in either direction goes beyond what the sentence says, which is the point of the item."),
 ("from other worlds facilitated European technological developments",
  "KC-4.1.II states that scientific learning from the Classical, Islamic, and Asian worlds spread, facilitating European technological developments and innovation, and adapting star tables compiled elsewhere is that facilitation. The illustrative examples name astronomical charts among the developments so influenced."),
 ("faster than every other",
  "The four rejected statements are KC-4.1.II and KC-4.1.II.A almost verbatim. The framework compares no two vessel designs for speed and dates, ranks and describes none of these devices, so a claim about speed would have to be defended from outside it."),
 ("built up from accumulated observation",
  "KC-4.1.II.A speaks of an IMPROVED understanding of regional wind and currents patterns, which is a process rather than a starting condition, and collecting pilots' observations is how such an improvement accumulates. The word regional in the same phrase tells against treating every ocean as identical."),
 ("credits state sponsorship of exploration",
  "KC-4.1.III says new state-supported transoceanic maritime exploration occurred in this period and KC-4.1.IV.C adds mercantilist policies and joint-stock companies used by rulers, so technology sits alongside state action in the framework's account. Each rejected option denies something the unit states outright."),
 ("one to expansion and one to ocean travel",
  "KC-4.3.II connects gunpowder, cannons, and armed trade to imperial expansion, while KC-4.1.II.A connects new tools, ship designs and knowledge of winds and currents to transoceanic travel and trade. Each rejected option contradicts one or both of those statements."),
 ("spread of knowledge that facilitated further developments",
  "KC-4.1.II has knowledge, scientific learning, and technology spreading and facilitating European technological developments and innovation, and KC-4.1.II.A then lists developments that followed, so the framework describes a process rather than a single event."),
 ("routes sailed before and after",
  "Unit 4: Learning Objective A asks how the diffusion of technology facilitated changes in patterns of trade and travel, so evidence for it has to compare travel before and after those developments came into use. Taverns, bread prices, spires and enrolments bear on none of that."),
 ("new tools, better ships, and a fuller grasp of winds and currents",
  "The keyed sentence joins KC-4.1.II on the spread of knowledge, scientific learning, and technology to KC-4.1.II.A on new tools, innovations in ship designs, and an improved understanding of regional wind and currents patterns making transoceanic travel and trade possible. Each rejected version contradicts one of those two statements."),
]

TABLE_CHECKS = {11: q11, 12: q12, 13: q13}

if __name__ == "__main__" and "--selftest" in sys.argv:
    extra_controls(w4_1)

extras(w4_1)
es.run(w4_1, CLAIMS, TABLE_CHECKS, sys.argv)
