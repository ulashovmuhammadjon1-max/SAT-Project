"""Key audit for AP WORLD HISTORY: MODERN 3.2 Empires: Administration.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. `claim` states what the key rests on, for a human to audit.

The structural gate is `cg_check.check`; the notation gate and the generic
negative control -- every key rotated, every table cell corrupted -- are in
`es_check`, reused unchanged. The two history gates defined here, a required
CED citation in every `why` and a ban on figure language the bank cannot
display, carry their own negative AND positive controls; the positive ones
exist because an over-matching checker is worse than none, and this repo has
already shipped a figure check that fired on the phrase "the fullest picture
of".

WHAT THE KEYS REST ON
---------------------
Items 1, 2, 12, 18, 22, 25 and 30 rest on KC-4.3.I.C: recruitment and use of
bureaucratic elites, as well as the development of military professionals,
became more common among rulers who wanted to maintain centralized control over
their populations and resources.
Items 3, 7, 8, 11, 13, 16, 20, 24, 26, 28 and 30 rest on KC-4.3.I.A: rulers
continued to use religious ideas, art, and monumental architecture to legitimize
their rule.
Items 4, 5, 9, 10, 15, 17, 19, 23 and 30 rest on KC-4.3.I.D: rulers used tribute
collection, tax farming, and innovative tax-collection systems to generate
revenue in order to forward state power and expansion.
Items 6 to 9, 23, 26 and 28 additionally use the HEADINGS under which the
framework prints its illustrative examples -- bureaucratic elites or military
professionals; religious ideas; art and monumental architecture; tax-collection
systems -- which are themselves framework content.
Items 21, 27 and 29 rest on the relationship between two of those statements,
and item 29 on the governance thematic focus printed with the topic.

WHAT NO ITEM ASSERTS. The framework names these practices without describing
how any of them worked, so nothing here keys the mechanics of the devshirme, a
zamindar's share, or the date of any building. Every stimulus is labelled
hypothetical and no quotation is attributed to a real person or document.

NEGATIVE CONTROL: `python3 verify_w3_2.py --selftest`.
"""
import re
import sys

import cg_check as cg
import es_check as es

import w3_2

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

FARMED = "Revenue raised by tax farmers"
SALARIED = "Revenue raised by salaried officials"
INKIND = "Share of taxes received in grain and cloth"
COIN = "Share of taxes received in hard currency"


def q14(table, item):
    farmed, salaried = cg.col(table, FARMED), cg.col(table, SALARIED)
    shares = [f / (f + s) for f, s in zip(farmed, salaried)]
    assert all(shares[i + 1] < shares[i] for i in range(len(shares) - 1)), \
        f"the tax-farming share must fall at every step; got {shares}"
    farmer_leads = [f > s for f, s in zip(farmed, salaried)]
    assert 0 < sum(farmer_leads) < len(farmed), (
        "neither method may lead in every province, or two distractors become true; "
        f"got {farmer_leads}")
    assert all(f > 0 for f in farmed), "'no province used tax farmers' must be false"
    assert len(set(zip(farmed, salaried))) == len(farmed), \
        "'the four provinces raised identical amounts' must be false"
    return (f"the tax-farming shares read {[round(s, 2) for s in shares]}, strictly falling, "
            f"and tax farmers lead in {sum(farmer_leads)} of the four provinces")


def _register(table):
    return {r[0]: cg.normalize(r[1]) for r in table["rows"]}


def q15(table, item):
    m = _register(table)
    revenue = [k for k, v in m.items() if "taxes" in v]
    assert revenue == ["Measure 3"], \
        f"exactly one measure must concern the collection of taxes; got {revenue}"
    assert "sold" in m["Measure 3"], "the tax measure must be a sale of the collecting right"
    assert "officials" in m["Measure 1"], "the first measure must concern recruited officials"
    assert "mosque" in m["Measure 2"], "the second measure must be a building programme"
    return ("only the third row concerns taxes, and it sells the right to collect them, while "
            "the first recruits officials and the second raises buildings")


def q16(table, item):
    m = _register(table)
    building = [k for k, v in m.items() if "mosque" in v or "tomb" in v]
    assert building == ["Measure 2"], \
        f"exactly one measure must be a building programme; got {building}"
    assert "taxes" not in m["Measure 2"], "the building measure must not also be a tax measure"
    assert "officials" not in m["Measure 2"], \
        "the building measure must not also be a recruitment measure"
    return ("exactly one of the three rows raises a mosque and a dynastic tomb, and it is "
            "neither a tax measure nor a recruitment measure")


def q17(table, item):
    inkind, coin = cg.col(table, INKIND), cg.col(table, COIN)
    assert all(coin[i + 1] > coin[i] for i in range(len(coin) - 1)), \
        f"the hard-currency share must rise at every step; got {coin}"
    assert all(inkind[i + 1] < inkind[i] for i in range(len(inkind) - 1)), \
        f"the payment-in-kind share must fall at every step; got {inkind}"
    assert all(abs(a + b - 100) < 1e-9 for a, b in zip(inkind, coin)), \
        f"the two shares must sum to 100 in each decade; got {list(zip(inkind, coin))}"
    assert all(a != b for a, b in zip(inkind, coin)), \
        "'the two shares are equal in every decade' must be false"
    return (f"the hard-currency shares read {coin} and the payment-in-kind shares {inkind}, "
            "rising and falling respectively and summing to 100 in each decade")


CLAIMS = [
 ("bureaucratic elites to maintain centralized control",
  "KC-4.3.I.C states that recruitment and use of bureaucratic elites, as well as the development of military professionals, became more common among rulers who wanted to maintain centralized control over their populations and resources. Salaried officials posted and rotated by the ruler are that practice; the rejected options are KC-4.3.I.A, KC-4.3.I.D, KC-4.3.II.A.i and KC-4.2.II.D."),
 ("maintain centralized control over their populations and resources",
  "KC-4.3.I.C gives the purpose in its own words. Transferring administration to companies, shrinking revenue, elected assemblies and abolishing tribute each contradict what the framework says these rulers were doing."),
 ("Religious ideas, art, and monumental architecture",
  "KC-4.3.I.A states that rulers continued to use religious ideas, art, and monumental architecture to legitimize their rule. None of the rejected sets appears in that statement."),
 ("Tribute collection, tax farming, and innovative tax-collection systems",
  "KC-4.3.I.D names exactly these three revenue methods. The rejected lists name fiscal devices the framework does not attribute to the rulers of land-based empires in this period."),
 ("forward state power and expansion",
  "KC-4.3.I.D states the purpose directly: to generate revenue in order to forward state power and expansion. Redistribution, industrial policy, independent religious funding and tax relief are not the ends the framework attaches to these methods."),
 ("Bureaucratic elites or military professionals",
  "The illustrative examples beside Unit 3: Learning Objective B print the Ottoman devshirme and the salaried samurai under this heading, which is the category KC-4.3.I.C describes. Restrictive trade policies belong to KC-4.3.II.A.i in a different unit."),
 ("religious idea used to legitimize rule",
  "The Mexica practice of human sacrifice, European notions of divine right and the Songhai promotion of Islam are printed under the heading of religious ideas, and KC-4.3.I.A makes religious ideas a means by which rulers legitimized their rule."),
 ("art and monumental architecture to legitimize rule",
  "Qing imperial portraits, the Incan sun temple of Cuzco, Mughal mausolea and mosques and European palaces are printed under art and monumental architecture, which KC-4.3.I.A names alongside religious ideas as a means of legitimation."),
 ("generate revenue for state power and expansion",
  "Mughal zamindar tax collection, Ottoman tax farming, Mexica tribute lists and the Ming practice of collecting taxes in hard currency are printed under tax-collection systems, and KC-4.3.I.D states that such methods generated revenue to forward state power and expansion."),
 ("Tax farming",
  "KC-4.3.I.D names tax farming among the revenue methods and the illustrative examples print Ottoman tax farming as an instance. A contractor advancing a fixed sum and recovering it locally is that arrangement, not tribute, not a chartered company at KC-4.1.IV.C, and not the salaried service of KC-4.3.I.C."),
 ("Legitimize the ruler's rule",
  "KC-4.3.I.A attaches exactly this purpose to religious ideas, art, and monumental architecture. Revenue belongs to KC-4.3.I.D and recruitment to KC-4.3.I.C, and neither is what a tomb or a portrait accomplishes."),
 ("became more common, not that it began",
  "KC-4.3.I.C says the recruitment and use of bureaucratic elites became more common, which is a claim about frequency rather than about origin. The rejected readings add beginnings, endings and restrictions the sentence does not contain."),
 ("carried on from earlier periods",
  "KC-4.3.I.A's word is continued, which places the practice in continuity with earlier periods rather than treating it as an innovation of 1450 to 1750. Nothing in the sentence confines it to one empire, to unarmed rulers, or to new territory."),
 ("falls steadily from the first province to the fourth",
  "Recomputed in q14 above: the tax-farming share falls strictly across the four provinces, each method leads in two of them, and every province uses both. KC-4.3.I.D names tax farming as one method among others, which is why a mixed picture is what the framework leads a student to expect."),
 ("Measure 3 only",
  "KC-4.3.I.D names tax farming among the revenue methods, and recomputed in q15 above only the third row concerns taxes, selling the right to collect them. The first row is the recruitment of KC-4.3.I.C and the second the architecture of KC-4.3.I.A."),
 ("Measure 2 only",
  "KC-4.3.I.A names religious ideas, art, and monumental architecture as the means of legitimation. Recomputed in q16 above, exactly one row raises a mosque and a dynastic tomb, and that row is neither a tax measure nor a recruitment measure."),
 ("hard currency rises in every decade",
  "Recomputed in q17 above: the hard-currency share rises at every step, the payment-in-kind share falls, the two sum to 100 and are never equal. KC-4.3.I.D names innovative tax-collection systems, and the illustrative examples print the Ming practice of collecting taxes in hard currency as one."),
 ("owe their position to the ruler and are paid by the state",
  "KC-4.3.I.C ties the recruitment of bureaucratic elites to rulers who wanted to maintain centralized control over their populations and resources, which is the aim stated. Granting great families the right to farm their own districts' taxes moves control toward them instead."),
 ("Tribute collection",
  "KC-4.3.I.D names tribute collection first among the revenue methods, and the illustrative examples print Mexica tribute lists under tax-collection systems. Chartered companies belong to KC-4.1.IV.C and the remaining options are not revenue methods at all."),
 ("using religious ideas, art, and architecture to legitimize rule",
  "KC-4.3.I.A is an explicit statement that rulers continued to use religious ideas, art, and monumental architecture to legitimize their rule. The rejected corrections overstate in the other direction: KC-4.3.II makes force central to expansion, and no statement makes these rulers elected."),
 # Both clauses: the first distractor shares the opening clause and differs
 # only in its second half, so half the anchor would match it too.
 ("dynastic mosque built in the capital, together with a new system for collecting taxes",
  "KC-4.3.I.A covers legitimation through religious ideas, art, and monumental architecture and KC-4.3.I.D covers revenue through tribute, tax farming, and innovative collection systems, so a pair showing both must draw one item from each statement."),
 ("rulers seeking centralized control over populations and resources",
  "KC-4.3.I.C names the recruitment of bureaucratic elites and the development of military professionals in one sentence with a single stated motive. The rejected options add identities, pay arrangements and origins the sentence does not state."),
 ("innovative tax-collection system used to generate revenue",
  "KC-4.3.I.D names innovative tax-collection systems among the revenue methods, and the illustrative examples print the Ming practice of collecting taxes in hard currency under that heading. The rejected categories are KC-4.3.I.A, KC-4.3.II.A.i and KC-4.2.II.D."),
 ("religious ideas and monumental architecture to legitimize their rule",
  "KC-4.3.I.A joins religious ideas to art and monumental architecture as means of legitimation, and the report has a ceremony in a monumental religious building doing that work. The rejected statements are KC-4.3.II, KC-4.3.II.A.i, KC-4.2.II.D and KC-4.3.II.A.iii."),
 ("recruited and deployed officials to keep central control",
  "KC-4.3.I.C makes the recruitment and use of bureaucratic elites the framework's account of how rulers maintained centralized control over populations and resources, so that is the axis a comparison must run along. Calendars, decoration, one year's exports and geography answer other questions."),
 ("commissioned by the court and displayed in official settings",
  "KC-4.3.I.A names art alongside religious ideas and monumental architecture as a means of legitimation, and the illustrative examples print Qing imperial portraits under art and monumental architecture. Art made privately or for sale does no legitimating work for a ruler."),
 # Both clauses: the item is about a tension BETWEEN two aims, so an anchor
 # naming only one of them would not distinguish the key from a distractor
 # that names that same aim beside a different second one.
 ("Raising revenue quickly, and keeping control of the provinces",
  "KC-4.3.I.D presents revenue methods including tax farming while KC-4.3.I.C makes centralized control over populations and resources the aim behind recruiting salaried elites, so devolving collection to a landholder serves the first and complicates the second. The rejected pairs set two halves of one statement against each other or belong to unit 4."),
 ("A religious idea used to legitimize rule",
  "KC-4.3.I.A names religious ideas among the means of legitimation, and the illustrative examples print European notions of divine right under religious ideas. The rejected categories are KC-4.3.I.D, KC-4.3.I.C, KC-4.3.III.iii and KC-4.3.II.A.i."),
 ("obtained, retained, and exercised power",
  "The governance thematic focus printed with this topic states that governments maintain order through administrative institutions, policies, and procedures and obtain, retain, and exercise power in different ways and for different purposes, which is what KC-4.3.I.A, KC-4.3.I.C and KC-4.3.I.D between them describe."),
 ("staffed the state with recruited elites and military professionals",
  "The keyed sentence joins KC-4.3.I.A on legitimation, KC-4.3.I.C on recruited elites and military professionals, and KC-4.3.I.D on tribute collection, tax farming, and innovative tax-collection systems. Each rejected version contradicts at least one of those three statements."),
]

TABLE_CHECKS = {14: q14, 15: q15, 16: q16, 17: q17}

if __name__ == "__main__" and "--selftest" in sys.argv:
    extra_controls(w3_2)

extras(w3_2)
es.run(w3_2, CLAIMS, TABLE_CHECKS, sys.argv)
