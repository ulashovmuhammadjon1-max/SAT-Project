"""Key audit for AP U.S. HISTORY 1.1 Contextualizing Period 1.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The shared gate is
``wh_check.run``, which the World History banks already use -- its checks are
about history rather than about world history: a KC code or Learning Objective
in every ``why`` and every ``claim``, no figure language, no typeset markup, and
the marked-stimulus rule.

WHAT THE KEYS REST ON
---------------------
  Unit 1 Learning Objective A, 1491 to 1607      items 1, 12, 14, 24, 30
  KC-1.1, migration and settlement over time     2, 4, 12, 18, 19, 21, 22, 27, 29, 30
  KC-1.1.I, agriculture, resource use, social
    structure                                    3, 4, 15, 19, 22, 27
  KC-1.2, three groups, both sides of the
    Atlantic                                     5, 6, 19, 20, 23, 26, 27, 29, 30
  KC-1.2.I, competition WITHIN European
    societies                                    7, 12, 20, 24, 30
  KC-1.2.II, Exchange plus Spanish Empire        8, 9, 26, 28
  KC-1.2.III, divergent worldviews               10, 11, 25, 27
  skill 4.A and the topic page's definition of
    context                                      12, 13, 14, 17, 24, 28

THE BOUNDARY THIS MODULE HAS TO HOLD, and why several items exist only to
test it: 1.1 is a CONTEXTUALIZING topic whose Required Course Content is
printed under the heading PREVIEW. The lettered sub-points -- KC-1.1.I.A
through KC-1.2.III.C -- belong to topics 1.2 through 1.7, which have their own
pages. So no key here names a people, place, crop, disease, date, explorer or
colony. ``no_period_detail`` asserts that, and items 13, 24 and 28 key the
boundary itself.

THE SWAP ITEMS. KC-1.2's list of changes (social, cultural, political) and
KC-1.2.II's list (demographic, economic, social) overlap in one word and are
the likeliest pair to be confused, so item 9 offers the other list as its
distractor and the anchor carries the whole triple. Item 27 does the same for
KC-1.1 against KC-1.2, and item 19 asks which of five sentences is the one
from KC-1.2 rather than KC-1.1.

DATA ITEMS: 15, 16 and 17 carry tables of explicitly illustrative data,
recomputed below from the table alone with each distractor falsified against
the same rows. The catch rate for item 16 is deliberately partial and the
reason is stated at that check: it keys what the table CANNOT support, and a
corruption that changes a value leaves an absent column just as absent.

NEGATIVE CONTROLS: ``python3 verify_a1_1.py --selftest``.
"""
import re
import sys

import wh_check
import a1_1

REGION = "Region of North America (illustrative)"
FOOD = "Principal food source described"
FORM = "Form of settlement described"
STATEMENT = "Statement a student proposes as context (illustrative)"
WHEN = "Does it look before the period, or beside it?"

# Explicit lookarounds, never \b beside a letter run. Period-1 detail that
# belongs to topics 1.2 through 1.7 and must not appear in a PREVIEW topic.
# BARE YEARS ARE DELIBERATELY ABSENT from this list. The first draft included
# 1492 and it fired on q1's distractor "1492 to 1600" -- a wrong ANSWER SPAN in
# an item about which span Learning Objective A gives, not a reach into topic
# 1.4's material. The framework's own periodisation is years, so a year cannot
# distinguish preview from detail; a proper noun can.
_PERIOD_DETAIL = re.compile(
    r"(?<![A-Za-z])(Aztec|Inca|Maya|Iroquois|Algonquian|Pueblo|Cahokia|Columbus|Cortes|"
    r"Jamestown|Roanoke|encomienda|conquistador|smallpox|Chesapeake|"
    r"Powhatan|Hispaniola|Mexico|Peru)(?![A-Za-z])")


def no_period_detail(module):
    """A PREVIEW topic may not key the detail its later topics own."""
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"], item["why"]] + list(item["choices"]):
            hit = _PERIOD_DETAIL.search(text)
            assert not hit, (
                f"{code} q{i}: names {hit.group(0)!r}, which belongs to topics 1.2 through "
                f"1.7 rather than to this contextualizing topic -- {text[:70]!r}"
            )
    print(f"OK  {code} scope: no item reaches into the lettered sub-points that topics "
          f"1.2 through 1.7 own.")


# ------------------------------------------------------------------ table checks

def _col(table, header):
    idx = table["headers"].index(header)
    return [row[idx] for row in table["rows"]]


# The two settlement tables are CATEGORICAL, and the shared corrupter appends
# text to a cell or scales a number. Appending leaves `startswith("Permanent")`
# and `"maize" in ...` both true, so a check written only on those properties
# reads the table without being able to object to anything in it -- 0 of 12
# cells caught, which the harness rightly refuses. The fix is to state the
# expected rows HERE, independently of the module, so every cell is
# load-bearing; the derived assertions that follow are what tie the data to the
# key. Editing the table now means editing this list too, which is the point.
_EXPECTED_SETTLEMENT = [
    ["Region 1", "Maize raised on irrigated fields", "Permanent towns"],
    ["Region 2", "Fish and shellfish taken from rivers and the coast", "Permanent villages"],
    ["Region 3", "Bison hunted on foot across grassland", "Camps moved with the herds"],
    ["Region 4", "Nuts, game and berries gathered in woodland", "Villages moved every few years"],
]


def _settlement_rows(table):
    assert [list(r) for r in table["rows"]] == _EXPECTED_SETTLEMENT, (
        f"the settlement table does not hold the rows this check was written against; "
        f"got {table['rows']}"
    )


def q15(table, item):
    _settlement_rows(table)
    foods, forms = _col(table, FOOD), _col(table, FORM)
    assert len(set(foods)) == len(foods), f"the food sources must all differ; got {foods}"
    assert len(set(forms)) > 1, f"the settlement forms must not be uniform; got {forms}"
    permanent = [f for f in forms if f.lower().startswith("permanent")]
    assert len(permanent) == 2, (
        f"'only one region is recorded as permanent' must be false and countable; "
        f"{len(permanent)} rows say permanent"
    )
    farmed = [f for f in foods if "maize" in f.lower()]
    assert len(farmed) == 1, (
        f"'the record shows agriculture in every region' must be false; {len(farmed)} of "
        f"{len(foods)} rows record a cultivated crop"
    )
    return (f"{len(foods)} regions carry {len(set(foods))} distinct food sources and "
            f"{len(set(forms))} distinct settlement forms, {len(permanent)} of them permanent, "
            f"with {len(farmed)} cultivated crop")


def q16(table, item):
    # This item keys what the table CANNOT support, so its guard is a check on
    # the table's COLUMNS rather than on any value in them: contact between
    # regions is unsupported because no column reports it, and corrupting a
    # cell cannot make an absent column present. Stated here so the partial
    # cell-catch rate is not later mistaken for a weak check.
    # HEADER GUARD FIRST, then the rows. Ordered this way deliberately: the
    # control for this item adds a "Contact with other regions" column, and if
    # row equality ran first it would raise on the row length instead, passing
    # the control for a reason that says nothing about the guard it names.
    joined = " ".join(table["headers"]).lower()
    for word in ("contact", "trade", "relation", "exchange", "neighbour", "neighbor"):
        assert word not in joined, (
            f"the table must report nothing about relations between regions for the key to "
            f"hold, but a header mentions {word!r}: {table['headers']}"
        )
    _settlement_rows(table)
    foods, forms = _col(table, FOOD), _col(table, FORM)
    assert len(set(foods)) > 1, "'the recorded food sources differ' must be true"
    assert sum(1 for f in forms if f.lower().startswith("permanent")) == 2, \
        "'two of the four regions are recorded with permanent settlement' must be true"
    assert any("maize" in f.lower() for f in foods), \
        "'one recorded food source is a cultivated crop' must be true"
    assert len(set(forms)) > 1, "'the forms of settlement are not all the same' must be true"
    return ("no column reports relations between regions, while all four distractors are "
            "read directly off the rows")


_EXPECTED_CONTEXT = [
    ["Native societies had been migrating and settling across North America over time", "Before"],
    ["European societies were competing with one another over religion and trade", "Beside"],
    ["Native societies had developed distinct and increasingly complex societies", "Before"],
    ["West African societies were in contact with Europeans across the Atlantic", "Beside"],
]


def q17(table, item):
    # Only the STATEMENT column is compared literally. The WHEN column is left
    # to the semantic guard below, so the control that exchanges Before and
    # Beside raises there -- on the claim the item actually makes -- rather
    # than on a row-equality assertion that would say nothing about it.
    # Corrupting a WHEN cell still fails, through the 2-and-2 count.
    assert _col(table, STATEMENT) == [r[0] for r in _EXPECTED_CONTEXT], (
        f"the context table's statements are not the ones this check was written "
        f"against; got {_col(table, STATEMENT)}"
    )
    when = _col(table, WHEN)
    statements = _col(table, STATEMENT)
    before = [s for s, w in zip(statements, when) if w.strip().lower() == "before"]
    beside = [s for s, w in zip(statements, when) if w.strip().lower() == "beside"]
    assert len(before) == 2 and len(beside) == 2, (
        f"the key names exactly two 'Before' rows against two 'Beside'; got "
        f"{len(before)} and {len(beside)}"
    )
    # The two Before rows must be the NATIVE ones and the two Beside rows the
    # others, or the keyed pairing is not what the table says.
    assert all("native" in s.lower() for s in before), \
        f"both 'Before' rows must describe native societies; got {before}"
    assert not any("native" in s.lower() for s in beside), \
        f"neither 'Beside' row may describe native societies; got {beside}"
    return (f"exactly two rows are marked Before and both describe native societies "
            f"({before}), against two marked Beside that do not")


TABLE_CHECKS = {15: q15, 16: q16, 17: q17}

CLAIMS = [
 ("1491 to 1607",
  "Unit 1 Learning Objective A gives the span verbatim: explain the context for European encounters in the Americas from 1491 to 1607."),
 ("migrated and settled across the vast expanse of North America over time",
  "KC-1.1, near verbatim, including the phrase 'over time' that makes it a development rather than a single arrival."),
 ("Agriculture, resource use, and social structure",
  "KC-1.1.I names exactly these three as the innovations through which different native societies adapted to and transformed their environments."),
 ("TRANSFORMED their environments as well as adapting",
  "KC-1.1.I says native societies 'adapted to and transformed' their environments; a summary keeping only the adaptation drops half the framework's claim."),
 ("Europeans, Native Americans, and Africans",
  "KC-1.2 names exactly these three groups whose contact resulted in the Columbian Exchange and change on both sides of the Atlantic."),
 ("consequences of contact were confined to the Americas",
  "KC-1.2's phrase 'on both sides of the Atlantic Ocean' is what excludes this reading; the other options are things KC-1.2 and KC-1.2.I assert."),
 ("competition and changes within European societies",
  "KC-1.2.I states that European expansion generated intense social, religious, political, and economic competition and changes within European societies."),
 ("Columbian Exchange and the development of the Spanish Empire",
  "KC-1.2.II names this pair together as resulting in extensive demographic, economic, and social changes."),
 ("Demographic, economic, and social",
  "KC-1.2.II's triple, offered against KC-1.2's 'social, cultural, and political' as the distractor, since the two lists share one word and are the likeliest confusion in the unit."),
 ("Religion, gender roles, family, land use, and power",
  "KC-1.2.III names exactly these issues as the ones over which Europeans and Native Americans asserted divergent worldviews."),
 ("two sides held differing views and each maintained its own",
  "KC-1.2.III's 'asserted', applied to both parties, together with 'divergent', describes two sides each maintaining differing views rather than convergence or a one-sided worldview."),
 ("before 1491; European societies were competing with one another at the same time",
  "The topic page names preceding developments and contemporaneous developments in different regions, in that order; KC-1.1 supplies the first and KC-1.2.I the second."),
 ("consequence of the encounters, so it cannot be the context",
  "The topic page defines context as preceding or contemporaneous developments, and KC-1.2 places the Columbian Exchange among the RESULTS of contact."),
 ("Identify and describe a historical context",
  "Skill 4.A as printed on this topic page, and the skill Unit 1 Learning Objective A asks students to apply; the distractors are skills 5.B, 5.A, 6.B and 2.B from other pages of this course."),
 ("different food sources are recorded alongside different forms of settlement",
  "Recomputed in q15 from the table alone, and KC-1.1 attributes distinctness to societies adapting to diverse environments while KC-1.1.I names agriculture and resource use."),
 ("had no contact with one another",
  "Recomputed in q16: no column of the table reports relations between regions, so this is the one claim of the five the record cannot reach. KC-1.1.I concerns agriculture, resource use and social structure, not intergroup contact."),
 ("native migration and settlement, and about increasingly complex native societies",
  "Recomputed in q17 from the table alone: exactly two rows are marked Before and both describe native societies, which is KC-1.1's content; the two Beside rows match the topic page's contemporaneous-elsewhere approach."),
 ("first key concept describes native societies developing over time before",
  "KC-1.1 is the unit's first key concept and precedes KC-1.2, in which contact appears; Learning Objective A asks for the context FOR the encounters."),
 ("Significant social, cultural, and political changes occurred on both sides",
  "KC-1.2, against four sentences drawn from KC-1.1 and KC-1.1.I, which describe what the framework places before the encounters."),
 ("KC-1.2.I, which says expansion generated competition and changes WITHIN European societies",
  "KC-1.2.I locates the change inside European societies, which is what a claim that Europe was unchanged denies; KC-1.2 makes the same point with 'both sides of the Atlantic Ocean'."),
 ("adapted to and transformed environments that were not alike",
  "KC-1.1 ties distinct and increasingly complex societies to DIVERSE environments, so the diversity is the reason the framework offers for the difference."),
 ("developing over time and becoming increasingly complex before contact",
  "KC-1.1's 'over time' and 'increasingly complex', with KC-1.1.I's three kinds of innovation, are a description of change rather than stasis."),
 ("Technological",
  "KC-1.2 names the Columbian Exchange and significant social, cultural, and political changes; technological change is absent from that sentence, which is why it is the one that is NOT named."),
 ("occurred in the Americas in the 1660s",
  "The topic page defines context as preceding or contemporaneous developments, and Learning Objective A gives the span as 1491 to 1607, so a later event is neither."),
 ("extended to political relations as well as to belief and daily life",
  "KC-1.2.III's list runs from religion and family through land use to power, spanning belief, daily life and political relations, and the sentence ranks none of them above the others."),
 ("wide-reaching",
  "KC-1.2.II calls the demographic, economic, and social changes EXTENSIVE; confining them to Spanish territory or to one hemisphere contradicts KC-1.2's 'both sides of the Atlantic Ocean'."),
 ("KC-1.1 with native societies before contact, and KC-1.2 with the consequences",
  "KC-1.1 concerns native migration, settlement and increasing complexity; KC-1.2 concerns what contact among the three groups resulted in. Both halves are carried because the swap is the defect this item exists to catch."),
 ("PREVIEW of the unit's key concepts, and the detail belongs to the later topics",
  "The topic page prints the key concepts under the heading PREVIEW and directs the teacher to select one or two for context; KC-1.2.II names the Spanish Empire, so Unit 1 does cover it."),
 ("adapting to and transforming diverse environments, and then contact among Europeans",
  "Collects KC-1.1, KC-1.1.I and KC-1.2 in the framework's own order and adds nothing to them."),
 ("Each already had developed societies of its own, and each was changed",
  "KC-1.1 gives native societies their own development, KC-1.2.I gives European societies competition and change of their own, and KC-1.2 places significant change on both sides of the Atlantic."),
]


def _extra_mutations():
    def period_detail_creeps_in(mod, cl):
        mod.QUESTIONS[0]["why"] = mod.QUESTIONS[0]["why"] + " Columbus sailed in 1492."
        no_period_detail(mod)

    def contact_column_appears(mod, cl):
        # q16 keys what the table cannot support; a column reporting contact
        # would make the keyed claim reachable and the item wrong.
        t = dict(mod.QUESTIONS[15]["table"])
        t["headers"] = list(t["headers"]) + ["Contact with other regions"]
        t["rows"] = [list(r) + ["Recorded"] for r in t["rows"]]
        mod.QUESTIONS[15]["table"] = t

    def before_rows_no_longer_native(mod, cl):
        # Flip which rows are marked Before, so the keyed pair stops being the
        # native one. A value corruption cannot express this.
        t = dict(mod.QUESTIONS[16]["table"])
        t["rows"] = [[s, ("Beside" if w == "Before" else "Before")] for s, w in t["rows"]]
        mod.QUESTIONS[16]["table"] = t

    return [
        ("period detail in a contextualizing topic", period_detail_creeps_in),
        ("a contact column added, making q16's unsupportable claim supportable",
         contact_column_appears),
        ("the Before and Beside marks exchanged, so the keyed pair is no longer the native one",
         before_rows_no_longer_native),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    for label, mutate in _extra_mutations():
        mod = wh_check._mutant(a1_1)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            wh_check.history_style(mod, claims)
            no_period_detail(mod)
            import cg_check as cg
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as e:
            print(f"  control OK  {label}: {str(e)[:110]}")
        else:
            raise SystemExit(f"CONTROL FAILED: {label} did not raise")

no_period_detail(a1_1)
wh_check.run(a1_1, CLAIMS, TABLE_CHECKS, sys.argv)
