"""Key audit for AP U.S. HISTORY 3.2 The Seven Years' War (The French and Indian War).

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The shared gate is
``wh_check.run``: a KC code or Learning Objective in every ``why`` and every
``claim``, no figure language, no typeset markup, the marked-stimulus rule, and
``cg_check``'s structural and anchor checks underneath.

WHAT THE KEYS REST ON
---------------------
  Unit 3 Learning Objective B, causes AND effects   items 1, 12, 18, 25, 29
  KC-3.1.I.A, rivalry, population, interior,
    French-Indian networks, American Indian
    autonomy                                       2, 3, 4, 14, 15, 18, 23, 24, 29, 30
  KC-3.1.I.B, expansion BUT at tremendous
    expense, setting the stage for revenue         5, 6, 16, 19, 20, 26, 27, 29, 30
  KC-3.1.I.C, colonial opposition AND native
    groups doing both things at once               7, 8, 17, 21, 22, 26, 27, 28, 30
  KC-3.1.I, three competitors, Britain defeated
    France and allied American Indians             9, 10, 26, 30
  the WOR thematic focus, skill 1.B, and the
    reasoning process printed on the page          11, 12, 13, 18

THE SCOPE THIS MODULE HAS TO HOLD. The topic page carries an OPTIONAL SOURCES
list, and the CED's own paragraph above it says those sources "are not required
AP course content" and that "None of the AP Exam questions require students to
have studied these specific sources." A key resting on one of them would be a
key resting on something the framework has explicitly told the student they need
not have read. ``no_optional_source_key`` asserts that no keyed choice names
one, and item 25 keys the caveat itself.

THE SWAP ITEMS, where a distractor is the key with two clauses exchanged rather
than an unrelated claim, and where the anchor therefore carries BOTH clauses:
item 3 (which networks, whose autonomy), item 5 (the gain and the cost), item 8
(trading and resisting), item 10 (victor and loser), item 22 (who objected to
what), item 23, item 27 (settled and unsettled), item 29 (cause and effect).

DATA ITEMS: 15, 16 and 17. All three carry HYPOTHETICAL figures, and the stems
say so, because the CED prints no data for this topic. Items 15 and 16 state
their expected rows here, independently of the module, so that every cell is
load-bearing -- the shared corrupter appends text to a categorical cell and
scales a number, and a check written only on derived ratios can read a
corrupted cell without being able to object to it. Item 17 is different on
purpose: only its LABEL column is compared literally, so that the named control
below, which flips one group's trading mark, raises on the count the key
actually depends on rather than on a row-equality assertion that would prove
nothing about it.

NEGATIVE CONTROLS: ``python3 verify_a3_2.py --selftest``.
"""
import re
import sys

import wh_check
import a3_2

DECADE = "Decade (hypothetical figures)"
TOTAL = "People in the British mainland colonies (thousands)"
INTERIOR = "People living in the interior districts (thousands)"
ACCOUNT = "Head of account (hypothetical index)"
BEFORE = "Before the war"
AFTER = "After the war"
GROUP = "Group in a hypothetical set of records"
TRADED = "Continued trading with Europeans"
CONTESTED = "Contested colonists' settlement on tribal land"

# The OPTIONAL SOURCES the CED prints for this topic and then tells the student
# they need not have studied. Explicit lookarounds, never \b beside a letter
# run. "Ohio" is matched only inside "Ohio Company", because the framework's own
# sentences are free to mention a river or a valley.
_OPTIONAL_SOURCE = re.compile(
    r"(?<![A-Za-z])(Jumonville|Ohio Company|Galloway|Proclamation Line|Pontiac|"
    r"Christopher Gist|Mount Vernon)(?![A-Za-z])", re.IGNORECASE)


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


# ------------------------------------------------------------------ table checks

def _col(table, header):
    idx = table["headers"].index(header)
    return [row[idx] for row in table["rows"]]


def _nums(table, header):
    return [float(str(v).replace(",", "")) for v in _col(table, header)]


# STATED HERE, not read off the module: these two tables mix a categorical
# label column with numeric columns, and the shared corrupter appends text to
# the one and scales the other. Without the expected rows, a corruption of the
# last figure in either table leaves every derived ratio still pointing the
# right way -- measured, not assumed -- and the cell is then not load-bearing.
_EXPECTED_POP = [["First", "900", "40"],
                 ["Second", "1,300", "110"],
                 ["Third", "1,800", "260"]]

_EXPECTED_EXPENSE = [["Cost of maintaining forces in North America", "20", "100"],
                     ["Revenue raised in the colonies", "6", "7"],
                     ["Mainland territory administered", "30", "95"]]


def q15(table, item):
    assert [list(r) for r in table["rows"]] == _EXPECTED_POP, (
        f"the population table does not hold the rows this check was written against; "
        f"got {table['rows']}")
    total, interior = _nums(table, TOTAL), _nums(table, INTERIOR)
    assert all(b > a for a, b in zip(total, total[1:])), \
        f"the colonial total must rise at every step; got {total}"
    assert all(b > a for a, b in zip(interior, interior[1:])), \
        f"the interior figure must rise at every step; got {interior}"
    shares = [i / t for i, t in zip(interior, total)]
    assert all(b > a for a, b in zip(shares, shares[1:])), \
        f"the interior share of the whole must rise; got {shares}"
    assert not any(b < a for a, b in zip(total, total[1:])), \
        "'the colonial total rises while the interior falls' must be false"
    assert len(set(total)) > 1, "'both figures are unchanged' must be false"
    assert interior[-1] < total[-1] - interior[-1], (
        f"'the interior holds more people than the rest of the colonies' must be false; "
        f"got {interior[-1]} against {total[-1] - interior[-1]}")
    return (f"the colonial totals {total} and interior figures {interior} both rise, and "
            f"the interior share moves {[round(s, 3) for s in shares]}")


def q16(table, item):
    assert [list(r) for r in table["rows"]] == _EXPECTED_EXPENSE, (
        f"the accounts table does not hold the rows this check was written against; "
        f"got {table['rows']}")
    before, after = _nums(table, BEFORE), _nums(table, AFTER)
    accounts = _col(table, ACCOUNT)
    cost, revenue, territory = 0, 1, 2
    assert "cost" in accounts[cost].lower() and "revenue" in accounts[revenue].lower() \
        and "territory" in accounts[territory].lower(), (
            f"the three heads of account are not in the order this check reads them: "
            f"{accounts}")
    ratios = [a / b for b, a in zip(before, after)]
    assert ratios[cost] >= 3 and ratios[territory] >= 3, (
        f"cost and territory must both rise sharply for the key to hold; got {ratios}")
    assert ratios[revenue] < 1.5, (
        f"revenue must barely move for the key to hold; got {ratios[revenue]}")
    assert ratios[revenue] < ratios[cost], \
        "'revenue rises faster than the cost of maintaining forces' must be false"
    assert after[territory] > before[territory], "'the territory administered falls' must be false"
    assert max(ratios) - min(ratios) > 1, \
        "'all three rise by about the same proportion' must be false"
    assert all(a > b for b, a in zip(before, after)), \
        "'costs and revenue both fall after the war' must be false"
    return (f"the before and after figures {list(zip(before, after))} give ratios "
            f"{[round(r, 2) for r in ratios]}: two multiply several times over while the "
            f"third barely moves")


_EXPECTED_GROUPS = ["Group 1", "Group 2", "Group 3", "Group 4"]
_MARKS = {"Yes", "No"}


def q17(table, item):
    # ONLY THE LABEL COLUMN IS COMPARED LITERALLY, so the named control that
    # flips one group's trading mark raises on the count below rather than on a
    # row-equality assertion. A corrupted mark still fails, through the
    # membership check: the shared corrupter appends text, and 'Yes CORRUPTED'
    # is neither Yes nor No.
    assert _col(table, GROUP) == _EXPECTED_GROUPS, (
        f"the groups table does not carry the rows this check was written against; "
        f"got {_col(table, GROUP)}")
    traded, contested = _col(table, TRADED), _col(table, CONTESTED)
    for mark in traded + contested:
        assert mark in _MARKS, f"every mark must be Yes or No; got {mark!r}"
    both = [i for i, (t, c) in enumerate(zip(traded, contested)) if t == "Yes" and c == "Yes"]
    assert len(both) * 2 > len(traded), (
        f"the key says MOST groups are recorded as doing both; only {len(both)} of "
        f"{len(traded)} are")
    assert both, "'no group is recorded as doing both at once' must be false"
    assert traded.count("Yes") < len(traded), \
        "'every group is recorded as continuing to trade' must be false"
    assert contested.count("No") == 0, \
        "'every group is recorded as accepting colonists' settlement' must be false"
    crossed = [i for i, (t, c) in enumerate(zip(traded, contested))
               if t == "Yes" and c == "No"]
    assert not crossed, (
        f"'the groups that continued trading are the ones that did not contest settlement' "
        f"must be false; rows {crossed} would make it true")
    return (f"{len(both)} of {len(traded)} rows record both continued trade and contested "
            f"settlement, and no row records trade without contest")


TABLE_CHECKS = {15: q15, 16: q16, 17: q17}

CLAIMS = [
 ("causes and effects of the Seven Years' War",
  "Unit 3: Learning Objective B reads 'Explain the causes and effects of the Seven Years' War (the French and Indian War).' Both halves are in the objective, so an objective confined to causes is not it."),
 ("growing population of the British colonies expanded into the interior",
  "KC-3.1.I.A states that colonial rivalry intensified between Britain and France in the mid-18th century AS the growing population of the British colonies expanded into the interior of North America. The growth and the expansion are on the British side."),
 ("French-Indian trade networks and American Indian autonomy",
  "KC-3.1.I.A names both things the expansion threatened, in one clause. The anchor carries both because each distractor keeps one of the pair and replaces the other."),
 ("middle of the 18th century",
  "KC-3.1.I.A dates the intensifying rivalry to the mid-18th century, which is where the span of Unit 3 opens; no other century is named in that sentence."),
 ("by defeating the French, but at tremendous expense",
  "KC-3.1.I.B holds gain and cost together: a major expansion of territorial holdings achieved by defeating the French, BUT at tremendous expense. The anchor carries both clauses because the distractors keep one and drop the other."),
 ("raise revenue and consolidate control over the colonies",
  "KC-3.1.I.B ends 'setting the stage for imperial efforts to raise revenue and consolidate control over the colonies', which names exactly these two imperial aims."),
 ("generated colonial opposition",
  "KC-3.1.I.C states that after the British victory, imperial officials' attempts to prevent colonists from moving westward generated colonial opposition, so opposition rather than welcome or success is the framework's report."),
 ("both to continue trading with Europeans and to resist the encroachments",
  "KC-3.1.I.C states that native groups sought to BOTH continue trading with Europeans AND resist the encroachments of colonists on tribal lands. The anchor carries both because each distractor keeps one aim and denies the other."),
 ("The British, the French, and American Indians",
  "KC-3.1.I names the competition among the British, French, and American Indians for economic and political advantage in North America as what culminated in the war."),
 ("Britain defeated France and allied American Indians",
  "KC-3.1.I ends with this clause. The anchor carries the whole of it because the leading distractor is the same clause with the victor and the loser exchanged, and KC-3.1.I.B independently makes Britain the power that gained territory."),
 ("interactions between empires, nations, and peoples shape the development of America",
  "The America in the World thematic focus printed on this topic page states that diplomatic, economic, cultural, and military interactions between empires, nations, and peoples shape the development of America and its increasingly important role in the world; KC-3.1.I.A's imperial rivalry is why this topic sits under it."),
 ("a historical concept, development, or process",
  "Skill 1.B as printed beside this topic's title, and what Unit 3: Learning Objective B asks for when it says EXPLAIN the causes and effects. The distractors are skills 4.A, 3.B, 2.B and 6.B from other pages of this unit."),
 ("Causation",
  "The unit's topic table assigns Causation to this topic, matching Unit 3: Learning Objective B's demand for causes and effects and the shape of KC-3.1.I.A, KC-3.1.I.B and KC-3.1.I.C, each of which links a development to what produced it or followed from it."),
 ("expansion of a growing colonial population into the interior",
  "KC-3.1.I.A describes the growing population of the British colonies expanding into the interior and threatening French-Indian trade networks and American Indian autonomy; surveying ground for farms along an existing trade route is that expansion, not the revenue effort KC-3.1.I.B places after the war."),
 ("interior grows as a share of the whole",
  "Recomputed in q15 from the table alone, with each of the four alternatives falsified against the same figures. KC-3.1.I.A makes the GROWING colonial population the thing that pressed into the interior."),
 ("revenue raised in the colonies barely moves",
  "Recomputed in q16 from the table alone: two heads of account multiply several times over while the third moves by a small fraction. KC-3.1.I.B calls that gap a major expansion of territorial holdings won at tremendous expense, setting the stage for imperial efforts to raise revenue."),
 ("trading with Europeans and contesting settlement are not alternatives",
  "Recomputed in q17 from the table alone: most rows record both, and no row records trade without contest. That is KC-3.1.I.C's claim that native groups sought to BOTH continue trading with Europeans AND resist encroachments on tribal lands."),
 ("A cause of the intensifying rivalry",
  "KC-3.1.I.A supplies the causal antecedent, while the effects among the distractors belong to KC-3.1.I.C and KC-3.1.I.B. Sorting causes from effects is what Unit 3: Learning Objective B and this topic's assigned reasoning process ask for."),
 ("set the stage for efforts to raise revenue and consolidate control",
  "KC-3.1.I.B connects the fighting to the policy that followed in a single clause, so the war and later imperial policy are linked rather than separate, and consolidation is the opposite of the loosening a distractor offers."),
 ("major expansion of territorial holdings was achieved at tremendous expense",
  "KC-3.1.I.B holds the gain and the cost together, and places the expense on the victor rather than on the defeated power."),
 ("After the British victory",
  "KC-3.1.I.C opens with exactly this phrase, which places the attempts to prevent westward movement and the two aims of native groups after the fighting rather than before the rivalry of KC-3.1.I.A or after independence."),
 ("Colonists opposed imperial attempts to stop them moving westward, while native groups resisted",
  "KC-3.1.I.C names two objections with different objects: colonial opposition to imperial restriction, and native resistance to colonists' encroachments. The anchor carries both clauses because one distractor exchanges the parties and another collapses them into one grievance."),
 ("French-Indian trade networks, and American Indian autonomy",
  "KC-3.1.I.A names the threatened networks as French-Indian and the threatened autonomy as American Indian in the same clause; the anchor carries both because each distractor keeps one term and swaps the other."),
 ("colonial expansion into the interior threatened existing trade networks",
  "KC-3.1.I.A makes settlement across an established route the threat it describes. KC-3.1.I.C says native groups continued trading and that the attempts to prevent westward movement generated opposition rather than succeeded."),
 ("not required course content, and no exam question requires",
  "The optional-sources paragraph on this topic page says the listed sources are not required AP course content and that none of the AP Exam questions require students to have studied them, which is why this topic's content is carried by KC-3.1.I.A, KC-3.1.I.B, KC-3.1.I.C and Unit 3: Learning Objective B."),
 ("Britain won its territorial gains cheaply",
  "KC-3.1.I.B says the expansion came at TREMENDOUS EXPENSE, so a cheap victory is the single claim of the five the framework contradicts; the other four are stated in KC-3.1.I, KC-3.1.I.B and KC-3.1.I.C."),
 ("while leaving the question of who would settle the interior in dispute",
  "KC-3.1.I.B supplies the settled question, a major expansion of British holdings by defeating the French, and KC-3.1.I.C the unsettled one, with colonial opposition and native resistance both continuing. The anchor carries both halves because a distractor exchanges them."),
 ("attempts to prevent colonists from moving westward generated colonial opposition",
  "KC-3.1.I.C states this directly; a request to lift such an order is that opposition expressed, and the same sentence says native groups sought to continue trading rather than to end it."),
 ("Colonial population pressing into the interior helped bring on the fighting, and the cost of winning it",
  "KC-3.1.I.A supplies the cause and KC-3.1.I.B the effect. The anchor carries both clauses because the leading distractor is the same pair with cause and effect exchanged, and Unit 3: Learning Objective B asks for both together."),
 ("resolved in Britain's favour at great cost, and the settlement it produced left both colonists",
  "KC-3.1.I names three competing parties and Britain's victory, KC-3.1.I.B the tremendous expense, and KC-3.1.I.C the grievances of colonists and native groups that followed. The anchor carries the whole combination because each rejected option denies one part of it."),
]


def _extra_mutations():
    def optional_source_becomes_the_key(mod, cl):
        mod.QUESTIONS[0]["choices"][mod.QUESTIONS[0]["ans"]] += \
            " as the Proclamation Line of 1763 shows"
        no_optional_source_key(mod)

    def only_half_the_groups_do_both(mod, cl):
        # q17 keys that MOST groups did both. Flipping one group's trading mark
        # leaves two of four doing both, which is not most, and the item then has
        # no defensible key. The mark stays a legal Yes or No, so only the count
        # can object -- which is the point of comparing just the label column.
        t = dict(mod.QUESTIONS[16]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][2][1] = "No"
        mod.QUESTIONS[16]["table"] = t

    return [
        ("an optional source promoted into a keyed choice", optional_source_becomes_the_key,
         r"lists under OPTIONAL SOURCES"),
        ("one group's trading mark flipped, so only half do both",
         only_half_the_groups_do_both, r"key says MOST groups"),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    for label, mutate, expect in _extra_mutations():
        mod = wh_check._mutant(a3_2)
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

no_optional_source_key(a3_2)
wh_check.run(a3_2, CLAIMS, TABLE_CHECKS, sys.argv)
