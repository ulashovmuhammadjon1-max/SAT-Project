"""Key audit for AP WORLD HISTORY: MODERN 3.1 Empires Expand.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. `claim` states what the key rests on, for a human to audit.

The structural gate is `cg_check.check`; the notation gate (no backslash, no
caret, no digit-hyphen-digit range, no dollar sign, no non-ASCII) and the
generic negative control -- every key rotated, every table cell corrupted --
are in `es_check`, reused unchanged. Two further gates are defined here because
they are what this subject adds:

CITATION. Every `why` must carry a CED reference: a `KC-` code, a named
Learning Objective, or a suggested skill. HISTORY_BRIEF.md's whole gate is that
a key traces to a sentence in the framework, and an uncited `why` is exactly
the question nobody can check later.

FIGURE LANGUAGE. The bank cannot show images, so a stem may never send a
student to look at a map or a picture. The patterns are deliberately narrow:
they require a display word FOLLOWED by shows/depicts/above/below, so the
phrase "the fullest picture of" and a distractor naming a diagram as a concept
do not trip them -- both were real false findings elsewhere in this repo. "The
table below" is legal and stays legal, because a `table=` really is there.

WHAT THE KEYS REST ON
---------------------
Items 1, 5, 6, 10 to 16 and 19 to 30 rest on KC-4.3.II: imperial expansion
relied on the increased use of gunpowder, cannons, and armed trade to establish
large empires in both hemispheres.
Items 2, 3, 4, 21 and 25 rest on KC-4.3.II.B, the four land empires and the
regions the framework assigns to each.
Items 7, 17, 18, 22, 27 and 30 rest on KC-4.3.III.i: political and religious
disputes led to rivalries and conflict between states.
Items 8 and 9 rest on the illustrative examples printed beside Unit 3:
Learning Objective A, the Safavid-Mughal conflict and the Songhai Empire's
conflict with Morocco.

WHAT NO ITEM ASSERTS. The framework does not say which of the Ottoman and
Safavid empires held which side of the Sunni and Shi'a split, so nothing here
keys it. It supplies no dates, rulers or battles for these empires, so nothing
here keys those either. Every stimulus is labelled hypothetical and no
quotation is attributed to a real person.

NEGATIVE CONTROL: `python3 verify_w3_1.py --selftest`.
"""
import re
import sys

import cg_check as cg
import es_check as es

import w3_1

# ------------------------------------------------------- the two history gates

# Explicit lookarounds throughout. `\b` is silently not a boundary between a
# digit and a letter, and this project has paid for that four separate times.
_CITE = re.compile(
    r"(?<![A-Za-z0-9])(?:KC-\d\.\d"
    r"|Learning Objective [A-N](?![A-Za-z])"
    r"|[Ss]uggested skill \d\.[A-E](?![A-Za-z]))"
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
        mod.QUESTIONS[3]["why"] = ("The framework says so plainly and the other options are "
                                   "simply not what it says anywhere at all.")

    def map_language(mod):
        mod.QUESTIONS[0]["q"] = ("The map below shows four empires. Which of them expanded "
                                 "using gunpowder weapons?")

    def image_language(mod):
        mod.QUESTIONS[1]["q"] = ("In the image, a besieging army is drawn beside its guns. "
                                 "What does this best illustrate?")

    def legal_picture_word(mod):
        mod.QUESTIONS[2]["why"] = ("KC-4.3.II.B gives the fullest picture of the four land "
                                   "empires and the regions each occupied, and the table below "
                                   "is not an image at all.")

    print("history-specific controls:")
    must_raise("a why stripped of its CED citation", strip_citation, cited)
    must_raise("a stem sending the student to a map", map_language, no_figure_language)
    must_raise("a stem sending the student to an image", image_language, no_figure_language)
    # POSITIVE control. A gate that rejects everything catches nothing, and the
    # two phrases below are exactly the false findings this repo has already
    # shipped from an over-matching figure check.
    must_pass("legal prose containing 'picture of' and 'the table below'",
              legal_picture_word, no_figure_language)
    must_pass("legal prose containing 'picture of' still counts as cited",
              legal_picture_word, cited)


# ------------------------------------------------------------ table recomputes

GP = "Soldiers carrying gunpowder weapons"
OTHER = "Soldiers carrying other weapons"
HEAVY = "Heavy cannon cast"
LIGHT = "Light field guns cast"


def q15(table, item):
    gp, other = cg.col(table, GP), cg.col(table, OTHER)
    shares = [g / (g + o) for g, o in zip(gp, other)]
    assert all(shares[i + 1] > shares[i] for i in range(len(shares) - 1)), \
        f"the gunpowder share must rise at every step; got {shares}"
    majorities = [g > o for g, o in zip(gp, other)]
    assert sum(majorities) == 1, \
        f"'every force carried a gunpowder majority' must be false; majorities {majorities}"
    totals = [g + o for g, o in zip(gp, other)]
    assert len(set(totals)) == 1, \
        f"the forces must be equal in size so 'the largest force' is false; got {totals}"
    assert all(g > 0 for g in gp), "'no force carried gunpowder weapons' must be false"
    assert len(set(zip(gp, other))) == len(gp), "'the four forces are identical' must be false"
    return (f"the gunpowder shares read {[round(s, 2) for s in shares]}, strictly rising; "
            f"all four totals are {totals[0]:.0f} and only one force reaches a majority")


def q16(table, item):
    heavy, light = cg.col(table, HEAVY), cg.col(table, LIGHT)
    assert all(heavy[i + 1] > heavy[i] for i in range(len(heavy) - 1)), \
        f"heavy cannon output must rise at every step; got {heavy}"
    assert all(light[i + 1] > light[i] for i in range(len(light) - 1)), \
        f"light gun output must rise at every step; got {light}"
    assert all(h != l for h, l in zip(heavy, light)), \
        "'the two kinds are equal in every decade' must be false"
    return (f"heavy cannon read {heavy} and light field guns {light}, both strictly "
            "increasing across the four decades")


def q17(table, item):
    text = {r[0]: cg.normalize(r[1]) for r in table["rows"]}
    assert "throne" in text["Dispute 1"], "the first dispute must be over a contested throne"
    assert "religion" in text["Dispute 2"], "the second dispute must be over a shared religion"
    third = text["Dispute 3"]
    assert "throne" not in third and "religion" not in third, \
        "the third dispute must be neither political nor religious"
    assert "market" in third, "the third dispute must be a market matter inside one town"
    return ("the first row describes a contested throne and the second a disagreement over a "
            "shared religion, while the third is a grain price inside one town")


CLAIMS = [
 ("increased use of gunpowder and cannons",
  "KC-4.3.II states that imperial expansion relied on the increased use of gunpowder, cannons, and armed trade to establish large empires in both hemispheres. A siege carried by artillery and followed by annexation is that process, and each rejected option belongs to a different statement of the framework."),
 # Both clauses, because the distractor is the SWAP: it gives each empire the
 # other's region. Either clause alone matches both choices.
 ("Manchu in Central and East Asia, and the Mughal in South and Central Asia",
  "KC-4.3.II.B lists the Manchu in Central and East Asia and the Mughal in South and Central Asia. The distractors exchange those regions or move an empire into the region the same sentence assigns to the Ottomans or the Safavids."),
 ("Southern Europe, the Middle East, and North Africa",
  "KC-4.3.II.B places the Ottoman Empire in Southern Europe, the Middle East, and North Africa, and assigns the other listed regions to the Manchu and the Mughal. It names no land empire of this period in West Africa or Northern Europe."),
 ("situated in the Middle East",
  "KC-4.3.II.B names the Safavids in the Middle East. Every rejected region is one the same sentence assigns to another of the four empires, or a region for which the sentence names no land empire at all."),
 ("Armed trade",
  "KC-4.3.II names gunpowder, cannons, and armed trade as the three means on which imperial expansion relied. Armed trade is the framework's own term; free trade agreements, abolished armies, a shared currency and renounced claims are nowhere attributed to these empires."),
 ("In both hemispheres",
  "KC-4.3.II closes by saying these means established large empires in both hemispheres, so the process is not confined to one side of the Atlantic, to Europe, or to a single ocean basin."),
 ("Political and religious disputes led to rivalries",
  "KC-4.3.III.i states that political and religious disputes led to rivalries and conflict between states, and the scenario supplies one dispute of each kind. KC-4.3.III.ii adds economic disputes, so 'economic disputes alone' misreports the framework."),
 ("Safavid and Mughal empires",
  "The illustrative examples printed beside Unit 3: Learning Objective A name the Safavid-Mughal conflict as a state rivalry of the period, illustrating KC-4.3.III.i. The rejected pairs combine empires the framework names without ever pairing them."),
 ("Morocco",
  "The same illustrative examples name the Songhai Empire's conflict with Morocco. The Kingdom of the Kongo belongs to KC-4.3.II.A.ii and Tokugawa Japan to the restrictive-policy examples at KC-4.3.II.A.i; neither is paired with Songhai."),
 ("Armed trade",
  "KC-4.3.II names armed trade alongside gunpowder and cannons as a means of imperial expansion, which is commerce conducted under force. Tax farming and tribute collection are KC-4.3.I.D, indentured servitude is KC-4.2.II.D, and syncretism is KC-4.1.VI."),
 ("equipped with cannon and gunpowder weapons",
  "KC-4.3.II ties imperial expansion to gunpowder and cannons, so evidence for that causal claim must connect territorial growth to those weapons. Library, granary, pilgrimage and wage records document other things and leave the claim untested."),
 ("accompanied the empire's territorial expansion",
  "KC-4.3.II makes gunpowder and cannon central to expansion in this period, and the account pairs rising outlay on both with new territory. A treasury record speaks to neither population, nor the whole of revenue, nor a turn from land warfare."),
 ("gunpowder weaponry and armed trade",
  "KC-4.3.II supplies the shared means and KC-4.3.II.B the four empires and their widely separated regions, which is why the framework treats them together. A shared capital, a shared revenue source, renounced expansion and a merchant founding are claims it never makes."),
 ("names armed trade among the means of imperial expansion",
  "KC-4.3.II puts gunpowder, cannons, and armed trade in a single sentence, so force and commerce are not separable there. Each rejected correction denies something that same sentence asserts."),
 ("rises steadily from the first force to the fourth",
  "Recomputed in q15 above: the gunpowder share rises strictly across the four forces, only one force reaches a majority, all four totals are equal, and every force carries some gunpowder weapons. KC-4.3.II makes that increasing use the process at issue."),
 ("both kinds of gun rises in every decade",
  "Recomputed in q16 above: both columns increase at every step, so neither swapped option holds and the two columns are never equal. KC-4.3.II describes exactly this increased use of gunpowder and cannons."),
 ("Dispute 1 and Dispute 2 only",
  "KC-4.3.III.i names political and religious disputes as leading to rivalries and conflict between states. Recomputed in q17 above: the first row is a contested throne and the second a quarrel over a shared religion, while the third is a grain price inside one town and sets no two states against each other."),
 ("different understanding of a faith",
  "KC-4.3.III.i pairs political with religious disputes as causes of rivalry between states, so the religious dimension must be a disagreement about belief that the states themselves take up. Coinage, calendars, recruitment and building stone differ between neighbours without any such dispute."),
 ("increased use of gunpowder, cannons, and armed trade",
  "KC-4.3.II gives this reason and no other in this topic. The printing press is not named in the unit, silver appears at KC-4.1.IV as a stimulus to trade rather than as exhausted, and KC-4.3.I.D has rulers using tribute collection rather than abandoning it."),
 ("central to the way expanding empires fought",
  "KC-4.3.II ties expansion to the increased use of gunpowder and cannons, and an order of march built around the guns shows that centrality. The account bears on neither cavalry, recruitment, fortification nor finance."),
 ("not confined to a single region",
  "KC-4.3.II.B lists regions from East Asia to North Africa and KC-4.3.II says the same means built large empires in both hemispheres, so the spread evidences a pattern wider than one region. A shared dynasty, an alliance and equal territory are not asserted anywhere."),
 ("sustained rivalry and conflict between states",
  "KC-4.3.III.i says the disputes led to rivalries and conflict between states, so rivalry is the framework's own term for the resulting relationship. Short campaigns, single encounters, naval theatres and a general treaty are assertions it does not make."),
 ("Armed Commerce",
  "KC-4.3.II names gunpowder, cannons, and armed trade as what expansion relied on, which is what the keyed title states. Peaceful federation and retreat contradict it, naval power belongs to the maritime empires of unit 4, and KC-4.3.I.B records accommodation of religious diversity."),
 ("names armed trade alongside gunpowder and cannons",
  "KC-4.3.II lists three means in one sentence, so commerce backed by force is part of the framework's own explanation of expansion. Each rejected correction denies something that sentence asserts."),
 # Both clauses: the swap is the point of the item, and the true pairing
 # "the Safavids in the Middle East" is itself one of the distractors.
 ("Safavids in Central and East Asia rather than in the Middle East",
  "KC-4.3.II.B assigns Central and East Asia to the Manchu and the Middle East to the Safavids, so moving the Safavids eastward is the error. The other four pairings are the framework's own, which is what makes the mistaken one hard to see: every word in it appears in the source and only the combination does not."),
 ("use of armed force to control trade",
  "KC-4.3.II joins expansion to gunpowder, cannons, and armed trade, and the report has annexation followed by an armed post levying duties on commerce. The rejected pairs are unit 4 developments at KC-4.1.IV.C, KC-4.1.VI, KC-4.1.V and KC-4.2.II.C."),
 ("political claim and a religious disagreement",
  "KC-4.3.III.i names political and religious disputes as what led to rivalries and conflict between states, so a quarrel resting on both explains a durable rivalry. Weights, hemispheres, an absence of guns and an absence of revenue are not offered there as causes."),
 ("established large empires in both hemispheres",
  "KC-4.3.II's closing phrase is what makes a comparison across hemispheres available. The rejected readings add restrictions the sentence does not carry, about who possessed gunpowder, where empires existed, how cannon were used, and who traded under arms."),
 ("duties levied on trade under guard",
  "KC-4.3.II names the weaponry and the armed trade together, so an argument covering both halves needs evidence of each. Every rejected pair leaves one half unevidenced or bears on neither."),
 ("gunpowder weaponry and armed trade, and political and religious disputes",
  "The keyed sentence joins KC-4.3.II on the means of expansion to KC-4.3.III.i on the disputes that set the empires against one another. Each rejected version contradicts one of those statements or contradicts the closing phrase about both hemispheres."),
]

TABLE_CHECKS = {15: q15, 16: q16, 17: q17}

if __name__ == "__main__" and "--selftest" in sys.argv:
    extra_controls(w3_1)

extras(w3_1)
es.run(w3_1, CLAIMS, TABLE_CHECKS, sys.argv)
