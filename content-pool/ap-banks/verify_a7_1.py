"""Key audit for AP U.S. HISTORY 7.1 Contextualizing Period 7.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in NO distractor; ``claim``
states what the key rests on, for a human to audit. The shared gate is
``wh_check.run``, written for the World History banks and unchanged here: a KC
code or Learning Objective in every ``why`` and every ``claim``, no figure
language, no typeset markup, the marked-stimulus rule, and the structural
checks of ``cg_check``.

WHAT THE KEYS REST ON
---------------------
  Unit 7 Learning Objective A, America grew
    into its role as a world power           items 1, 2, 25, 28
  KC-7.1, growth, instability, reform        3, 24, 30
  KC-7.1.I, the continued transition to an
    urban, industrial economy                4, 5, 21, 22, 24, 27, 30
  KC-7.1.II, the Progressive response        6, 7, 8, 9
  KC-7.1.III, a limited welfare state        10, 11, 24, 26
  KC-7.2, mass culture and migration         12, 16, 30
  KC-7.2.I, popular culture and debate       13, 14, 24
  KC-7.2.II, sharp variations for both
    international and internal migrants      15, 16, 23
  KC-7.3, international power and renewed
    domestic debate                          17, 28, 30
  KC-7.3.I, ambitions in the Western
    Hemisphere and the Pacific               18, 19, 24, 27
  KC-7.3.II, ongoing debates intensified     19
  KC-7.3.III, society transformed, the
    victory over the Axis powers             20, 29, 30
  skill 4.B and the topic page's own
    definition of context                    25, 26, 27, 29

THE BOUNDARY THIS MODULE HAS TO HOLD. 7.1 is a CONTEXTUALIZING topic whose
Required Course Content is printed under the heading PREVIEW: UNIT 7 KEY
CONCEPTS. The lettered sub-points -- KC-7.1.I.A through KC-7.3.III.E -- belong
to topics 7.2 through 7.14, which have their own pages. So no key here names a
president, a statute, a treaty, a programme, a movement, a court case, or a
place beyond the two regions KC-7.3.I itself states. ``no_period_detail``
asserts that, and items 26, 28 and 29 key the boundary itself.

THE SWAP ITEMS. Item 4's first distractor reverses KC-7.1.I's direction of
travel, item 16's reverse KC-7.2.II by keeping only one kind of migrant, item
20's keep one half of KC-7.3.III and reverse the other, and item 27's second
option is the topic page's two approaches in the wrong order. Each of those
anchors carries BOTH clauses, because half an anchor would match the swap.

DATA ITEMS: 21, 22, 23 and 24 carry tables of explicitly illustrative figures,
recomputed below from the table alone with every distractor falsified against
the same rows. The two numeric tables are guarded by a label check plus the
numeric assertions, so each of their cells is load-bearing for its own reason;
the categorical table compares its STATEMENT column literally and leaves the
code column to a format check and to the pairing assertion the key rests on,
so a corrupted code fails on the code and a mis-stated pairing fails on the
pairing.

NEGATIVE CONTROLS: ``python3 verify_a7_1.py --selftest``.
"""
import re
import sys

import wh_check
import wh_stimulus
import a7_1

DECADE = "Decade of the period (illustrative)"
URBAN = "Share of the population living in urban places (percent)"
FARM = "Share of the workforce employed in agriculture (percent)"
STRETCH = "Stretch of the period (illustrative)"
INTL = "International migrants recorded (thousands)"
INTERNAL = "Internal migrants recorded (thousands)"
STATEMENT = "Statement offered as context (illustrative)"
SOURCE_KC = "Preview key concept it is drawn from"

# Explicit lookarounds, never \b beside a letter run. Period-7 detail that the
# lettered sub-points own and that topics 7.2 through 7.14 carry on their own
# pages. BARE YEARS ARE DELIBERATELY ABSENT: the framework's own periodisation
# is years, item 2 keys the span 1890 to 1945 and KC-7.1.III itself names the
# 1930s, so a year cannot distinguish preview from detail. A proper noun can.
_PERIOD_DETAIL = re.compile(
    r"(?<![A-Za-z])(Wilson|Roosevelt|New Deal|Versailles|League of Nations|Pearl Harbor|"
    r"Philippines|Hawaii|Harlem|Holocaust|Nazi|internment|Red Scare|prohibition|suffrage|"
    r"radio|cinema|isolationism|nativist|quotas?|Klan|Spanish|atomic)(?![A-Za-z])",
    re.IGNORECASE)


def no_period_detail(module):
    """A PREVIEW topic may not key the detail its later topics own."""
    code = module.TOPIC[0]
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"], item["why"]] + list(item["choices"]):
            hit = _PERIOD_DETAIL.search(text)
            assert not hit, (
                f"{code} q{i}: names {hit.group(0)!r}, which belongs to topics 7.2 through "
                f"7.14 rather than to this contextualizing topic -- {text[:70]!r}"
            )
    print(f"OK  {code} scope: no item reaches into the lettered sub-points that topics "
          f"7.2 through 7.14 own.")


# ------------------------------------------------------------------ table checks

def _col(table, header):
    idx = table["headers"].index(header)
    return [row[idx] for row in table["rows"]]


def _nums(table, header):
    return [float(v) for v in _col(table, header)]


_DECADE_LABELS = ["Decade 1", "Decade 2", "Decade 3", "Decade 4"]
_STRETCH_LABELS = ["Stretch 1", "Stretch 2", "Stretch 3"]


def _transition_labels(table):
    assert _col(table, DECADE) == _DECADE_LABELS, (
        f"the transition table must be labelled {_DECADE_LABELS}; got {_col(table, DECADE)}"
    )


def q21(table, item):
    _transition_labels(table)
    urban, farm = _nums(table, URBAN), _nums(table, FARM)
    for name, vals in (("urban", urban), ("agricultural", farm)):
        assert all(0 <= v <= 100 for v in vals), f"the {name} column is not a share: {vals}"
    assert all(b > a for a, b in zip(urban, urban[1:])), \
        f"the urban share must rise at every step for the key to hold; got {urban}"
    assert all(b < a for a, b in zip(farm, farm[1:])), \
        f"the agricultural share must fall at every step for the key to hold; got {farm}"
    # 'the agricultural share is the larger in every decade' must be FALSE, and
    # 'both fall' and 'the shares stay level' are already false above.
    larger = [i for i, (u, f) in enumerate(zip(urban, farm), 1) if f > u]
    assert 0 < len(larger) < len(urban), (
        f"'the agricultural share is the larger in every decade' must be false but not "
        f"vacuous; it is larger in decades {larger}"
    )
    return (f"the urban column rises {urban} while the agricultural column falls {farm}, and "
            f"the agricultural share leads in only {len(larger)} of {len(urban)} decades")


def q22(table, item):
    _transition_labels(table)
    urban, farm = _nums(table, URBAN), _nums(table, FARM)
    ahead = [i for i, (u, f) in enumerate(zip(urban, farm)) if u > f]
    assert ahead, "'the urban share never exceeds the agricultural share' must be false"
    first = ahead[0]
    # The crossing must happen ONCE and stay crossed, or 'first exceeds' is not
    # a well defined reading of the record.
    assert ahead == list(range(first, len(urban))), (
        f"the urban share must cross the agricultural share once and stay above it; it leads "
        f"in rows {ahead}"
    )
    assert _DECADE_LABELS[first] == "Decade 3", (
        f"the crossing falls in {_DECADE_LABELS[first]}, not Decade 3"
    )
    return (f"the urban column {urban} first passes the agricultural column {farm} at row "
            f"{first + 1}, which the table labels {_DECADE_LABELS[first]}")


def q23(table, item):
    # PARTIAL CELL-CATCH RATE, and the reason, stated here so it is not later
    # mistaken for a check that has stopped reading its table: this item keys
    # that the figures VARY SHARPLY and that both kinds of migrant appear. The
    # shared corrupter multiplies a number, which usually makes the variation
    # sharper rather than falsifying it, so a corruption that lifts the largest
    # figure in a column leaves the keyed reading true and the check rightly
    # passes. Every corruption that could make the key wrong -- a reversal, a
    # flattening, a missing figure, a relabelled row -- is caught below.
    assert _col(table, STRETCH) == _STRETCH_LABELS, (
        f"the migration table must be labelled {_STRETCH_LABELS}; got {_col(table, STRETCH)}"
    )
    intl, internal = _nums(table, INTL), _nums(table, INTERNAL)
    assert min(intl + internal) > 0, \
        f"'only internal migrants are recorded' must be false; got {intl} and {internal}"
    assert all(b < a for a, b in zip(intl, intl[1:])), \
        f"'the international figure rises across the stretches' must be false; got {intl}"
    assert all(b > a for a, b in zip(internal, internal[1:])), \
        f"'the two figures move in the same direction' must be false; got {internal}"
    # 'neither figure changes by much' must be false: each column has to span a
    # multiple of at least three between its own smallest and largest figure.
    for name, vals in (("international", intl), ("internal", internal)):
        assert max(vals) >= 3 * min(vals), (
            f"the {name} column does not vary sharply enough for the key to hold: {vals}"
        )
    return (f"the international column falls {intl} while the internal column rises "
            f"{internal}, each spanning a multiple of at least three, with both kinds of "
            f"migrant recorded in every stretch")


_EXPECTED_STATEMENTS = [
    "The United States continued its transition to an urban, industrial economy led by "
    "large companies",
    "Popular culture grew in influence even as debates over its effects increased",
    "New territorial ambitions and acquisitions accompanied heightened public debates",
    "Policymakers transformed the nation into a limited welfare state during the 1930s",
]
# A preview code as the CED prints it on this page: a top-level concept and an
# optional roman-numeral sub-point, and nothing lettered, because the lettered
# sub-points belong to topics 7.2 through 7.14. Explicit anchors, no \b.
_CODE = re.compile(r"\AKC-7\.[123](?:\.(?:I|II|III))?\Z")


def q24(table, item):
    # Only the STATEMENT column is compared literally. The code column is left
    # to the format check and then to the pairing assertion, so the control that
    # moves a statement out of KC-7.1 raises on the PAIRING -- the claim the
    # item actually makes -- rather than on a row-equality assertion that would
    # say nothing about it. A corrupted code cell still fails, on the format.
    assert _col(table, STATEMENT) == _EXPECTED_STATEMENTS, (
        f"the concept table's statements are not the ones this check was written against; "
        f"got {_col(table, STATEMENT)}"
    )
    codes = _col(table, SOURCE_KC)
    for c in codes:
        assert _CODE.match(c), (
            f"{c!r} is not a preview key concept code of the form KC-7.1, KC-7.2.I and so on"
        )
    tops = [".".join(c.split(".")[:2]) for c in codes]
    repeated = sorted({t for t in tops if tops.count(t) > 1})
    assert len(repeated) == 1, (
        f"exactly one top-level concept must appear twice for the key to be the only "
        f"defensible pair; repeated: {repeated}"
    )
    assert repeated[0] == "KC-7.1", f"the repeated top-level concept is {repeated[0]}, not KC-7.1"
    pair = [i for i, t in enumerate(tops) if t == repeated[0]]
    assert pair == [0, 3], (
        f"the two rows sharing a top-level concept must be the transition row and the "
        f"welfare-state row; got rows {[i + 1 for i in pair]}"
    )
    return (f"the codes recorded are {codes}, whose top-level concepts are {tops}, so the only "
            f"repeated one is {repeated[0]} and it pairs rows 1 and 4")


TABLE_CHECKS = {21: q21, 22: q22, 23: q23, 24: q24}

CLAIMS = [
 ("role as a world power",
  "Unit 7 Learning Objective A reads, verbatim, explain the context in which America grew into its role as a world power."),
 ("1890 to 1945",
  "The unit heading gives Period 7 as 1890 to 1945, the span across which Unit 7 Learning Objective A asks for the context of America's growth into a world power; 1865 to 1898 is Period 6 and 1945 to 1980 is Period 8."),
 ("new efforts to reform",
  "KC-7.1 states that growth expanded opportunity, while economic instability led to new efforts to reform U.S. society and its economic system."),
 ("rural, agricultural economy to an urban, industrial economy",
  "KC-7.1.I names the direction of travel: from a rural, agricultural economy TO an urban, industrial economy led by large companies. The anchor carries both ends because the first distractor is the same sentence reversed."),
 ("already under way before the period opened",
  "KC-7.1.I says the United States CONTINUED its transition, which places it before 1890 as well as inside the period, matching the topic page's first approach to context, continuity with preceding developments."),
 ("Political corruption, economic instability, and social concerns",
  "KC-7.1.II names exactly these three as what Progressives responded to in the Progressive Era of the early 20th century."),
 ("calling for greater government action",
  "KC-7.1.II states that Progressives responded by calling for greater government action and other political and social measures."),
 ("early 20th century",
  "KC-7.1.II opens by placing the Progressive Era in the early 20th century, against KC-7.1.III's 1930s and against decades the framework does not put it in."),
 ("mass unemployment and social upheavals",
  "KC-7.1.III states that during the 1930s policymakers responded to the mass unemployment and social upheavals of the Great Depression."),
 ("limited welfare state and redefining the goals",
  "KC-7.1.III states that policymakers responded by transforming the U.S. into a limited welfare state, redefining the goals and ideas of modern American liberalism."),
 ("qualifies the transformation rather than claiming a complete welfare state",
  "KC-7.1.III's adjective LIMITED qualifies how far the transformation went while the sentence still calls it a transformation that redefined modern American liberalism."),
 ("growth of mass culture and significant changes in migration patterns",
  "KC-7.2 joins exactly these two: innovations in communications and technology contributed to the growth of mass culture, while significant changes occurred in internal and international migration patterns."),
 ("effects of culture on public values, morals, and American national identity",
  "KC-7.2.I states that debates increased over the effects of culture on public values, morals, and American national identity even as popular culture grew in influence."),
 ("met no argument",
  "KC-7.2.I's construction, popular culture grew in influence EVEN AS debates increased, is what excludes an uncontested growth; the other options are things the sentence asserts."),
 ("Economic pressures, global events, and political developments",
  "KC-7.2.II names exactly these three as the causes of sharp variations in the numbers, sources, and experiences of migrants."),
 ("Both international and internal migrants",
  "KC-7.2.II names the numbers, sources, and experiences of BOTH international and internal migrants, and KC-7.2 pairs internal and international migration patterns in the same way, so the anchor carries both because dropping either is the plausible error."),
 ("international power abroad, and renewed domestic debate",
  "KC-7.3 states that participation in a series of global conflicts propelled the United States into a position of international power WHILE renewing domestic debates over the nation's proper role in the world, so the anchor carries both consequences."),
 ("Western Hemisphere and the Pacific",
  "KC-7.3.I names new U.S. territorial ambitions and acquisitions in the Western Hemisphere and the Pacific, and the anchor carries both regions because one distractor keeps only the first."),
 ("already ongoing and the war and its aftermath sharpened them",
  "KC-7.3.II says World War I and its aftermath intensified ONGOING debates about the nation's role in the world, and KC-7.3.I already places heightened public debates in the late 19th century and early 20th century."),
 ("transformation of American society, and a position of global, political, and military leadership",
  "KC-7.3.III states that U.S. participation in World War II transformed American society, while the victory over the Axis powers vaulted the U.S. into a position of global, political, and military leadership; the anchor carries both halves because the distractors keep one and reverse the other."),
 ("rises in every decade recorded while the agricultural share falls",
  "Recomputed in q21 from the illustrative table alone, and KC-7.1.I states the transition from a rural, agricultural economy to an urban, industrial economy that the two columns move with."),
 ("Decade 3",
  "Recomputed in q22 from the illustrative table alone: the urban column first passes the agricultural column at the third row. KC-7.1.I asserts the transition but supplies no date for any crossing, which is why the table has to."),
 ("vary sharply from one stretch to the next",
  "Recomputed in q23 from the illustrative table alone, and KC-7.2.II states that economic pressures, global events, and political developments caused sharp variations in the numbers of both international and internal migrants."),
 ("transition to an urban, industrial economy and the statement about a limited welfare state",
  "Recomputed in q24 from the illustrative table alone: the two rows sharing a top-level concept are the KC-7.1.I row and the KC-7.1.III row, both under KC-7.1, while the other statements sit under KC-7.2 and KC-7.3."),
 ("situated within a broader historical context",
  "Suggested skill 4.B as printed on this topic page, and the skill Unit 7 Learning Objective A asks students to apply; the distractors are skills 2.B, 5.B, 1.B and 6.C from other pages of this unit."),
 ("PREVIEW of the unit's key concepts",
  "The topic page prints the key concepts under the heading PREVIEW and directs the teacher to select one or two for context, so the detail belongs to the later topics; KC-7.1.III does place the 1930s inside Unit 7."),
 ("under way before 1890, then comparing",
  "The topic page names preceding developments first and contemporaneous developments in different regions second; KC-7.1.I's 'continued' supplies the first and KC-7.3.I's public debates over America's role in the world sit beside the period. The anchor carries both clauses in order because the swap is the distractor."),
 ("grew into that role",
  "Unit 7 Learning Objective A asks for the context in which America GREW INTO its role as a world power, and KC-7.3 says global conflicts propelled the United States into a position of international power, so the standing is reached during the period."),
 ("where the period's developments arrive",
  "KC-7.3.III places the victory over the Axis powers at the end of the sequence, as what vaulted the United States into global, political, and military leadership, while the topic page defines context as preceding or contemporaneous developments."),
 ("instability brought reform",
  "Collects KC-7.1, KC-7.2 and KC-7.3 in the order the framework prints them under the heading PREVIEW: UNIT 7 KEY CONCEPTS, and adds nothing to them."),
]


def _extra_mutations():
    def period_detail_creeps_in(mod, cl):
        mod.QUESTIONS[0]["why"] = (mod.QUESTIONS[0]["why"]
                                   + " Woodrow Wilson asked Congress for war in 1917.")
        no_period_detail(mod)

    def pairing_moved_off_kc71(mod, cl):
        # q24's key names the two rows that share a top-level concept. Move the
        # welfare-state row into KC-7.2 and the keyed pair no longer exists.
        t = dict(mod.QUESTIONS[23]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][3][1] = "KC-7.2.II"
        mod.QUESTIONS[23]["table"] = t

    def crossing_moved_earlier(mod, cl):
        # q22 keys the decade in which the urban share first passes the
        # agricultural share. Lift Decade 2's urban share above it and the
        # crossing moves, which no single-cell corruption is guaranteed to do.
        t = dict(mod.QUESTIONS[21]["table"])
        t["rows"] = [list(r) for r in t["rows"]]
        t["rows"][1][1] = "40"
        mod.QUESTIONS[21]["table"] = t

    return [
        ("period detail in a contextualizing topic", period_detail_creeps_in,
         r"belongs to topics 7\.2 through 7\.14"),
        ("the shared top-level concept moved off KC-7.1, so the keyed pair is gone",
         pairing_moved_off_kc71, r"repeated top-level concept|must appear twice"),
        ("the urban share lifted in Decade 2, so the crossing moves off Decade 3",
         crossing_moved_earlier, r"crossing falls in"),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    import cg_check as cg
    for label, mutate, expect in _extra_mutations():
        mod = wh_check._mutant(a7_1)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            wh_check.history_style(mod, claims)
            no_period_detail(mod)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as e:
            # A control that fires for the wrong reason proves nothing about the
            # guard it names, so the message is checked, not just the fact of it.
            assert re.search(expect, str(e), re.I), (
                f"CONTROL FIRED FOR THE WRONG REASON: {label} -- {e}")
            print(f"  control OK  {label}: {str(e)[:110]}")
        else:
            raise SystemExit(f"CONTROL FAILED: {label} did not raise")
    wh_stimulus.controls(a7_1)

no_period_detail(a7_1)
wh_check.run(a7_1, CLAIMS, TABLE_CHECKS, sys.argv)
