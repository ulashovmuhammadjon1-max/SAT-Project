"""Key audit for AP WORLD HISTORY: MODERN 7.7 Conducting World War II.

One ``(anchor, claim)`` per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor; ``claim``
states what the key rests on, for a human to audit. The gate is
``wh_check.run``, shared by the World History banks.

WHAT THE KEYS REST ON
---------------------
KC-6.2.IV.A.ii: "World War II was a total war. Governments used a variety of
strategies, including political propaganda, art, media, and intensified forms of
nationalism, to mobilize populations (both in the home countries and the
colonies or former colonies) for the purpose of waging war. Governments used
ideologies, including fascism and communism to mobilize all of their state's
resources for war and, in the case of totalitarian states, to repress basic
freedoms and dominate many aspects of daily life during the course of the
conflicts and beyond."

KC-6.1.III.C.ii: "New military technology and new tactics, including the atomic
bomb, fire-bombing, and the waging of 'total war', led to increased levels of
wartime casualties."

  a total war                          items 1, 17, 30
  the four mobilizing strategies       items 2, 21, 25, 26, 30
  home countries AND colonies or
    former colonies                    items 3, 4, 22, 29, 30
  for the purpose of waging war        items 5, 21
  ideologies, fascism and communism    items 6, 7, 26, 29
  all of the state's resources         items 7, 17, 30
  repression IN THE CASE OF
    totalitarian states                items 8, 14, 18, 23, 28, 29, 30
  during the conflicts AND BEYOND      items 9, 24
  technology AND tactics, casualties   items 10, 11, 20, 26, 29, 30

Items 3, 8, 10 and 14 are the SWAP items: dropping half of "home countries and
the colonies or former colonies", generalising the repression clause off
totalitarian states, dropping "new tactics" so the second war's casualty
sentence becomes the first war's, and confusing what the CED's two headings
share with what separates them. Each of those anchors carries both clauses.

Items 12, 13 and 14 rest on the CED's printed illustrative examples: Western
democracies mobilizing for war (Great Britain under Winston Churchill, United
States under Franklin Roosevelt) and totalitarian states mobilizing for war
(Germany under Adolf Hitler, USSR under Joseph Stalin). Nothing is asserted
about any of the four beyond the heading it is printed under, and no quotation
is attributed to any of them.

Items 16, 17 and 18 rest on suggested skill 3.D and take its three verbs in
turn: evidence that REFUTES an argument, evidence that SUPPORTS one, and
evidence that MODIFIES one without refuting it. Item 27 rests on Unit 7 Learning
Objective G and item 28 on this topic's reasoning process, comparison.

BOUNDARY WITH 7.3: KC-6.2.IV.A.i and KC-6.1.III.C.i cover the first war. Items
1, 4 and 26 are the only ones that reach across, and each asks how the two
sentences differ rather than restating the earlier one.

WHAT IS NOT KEYED, deliberately: no date, battle, campaign, production total,
weapon performance or casualty figure, and nothing any named leader is supposed
to have said.

DATA ITEMS: 19 and 20 carry tables of explicitly illustrative data, recomputed
below from the table alone, with each distractor falsified against the same
numbers. The casualty table carries a combined column, and the check requires it
to agree with the two figures it sums, so no cell of it can be altered silently.

NEGATIVE CONTROLS: ``python3 verify_w7_7.py --selftest`` rotates every key,
breaks every anchor, corrupts every cell of both tables, injects each banned
notation and figure-language form, strips the citation from a ``why`` and a
``claim``, and duplicates a choice; each must raise for its own reason, and
positive controls run alongside.
"""
import sys

import cg_check as cg
import wh_check
import w7_7

FIRST = "Share of the adult population in the armed forces or war production, first year (percent)"
FOURTH = "Share of the adult population in the armed forces or war production, fourth year (percent)"
EARLIER = "Recorded wartime casualties in the earlier global conflict (thousands)"
LATER = "Recorded wartime casualties in the later global conflict (thousands)"
COMBINED = "Combined casualties across the two conflicts (thousands)"


def q19(table, item):
    first = dict(zip(cg.labels(table), cg.col(table, FIRST)))
    fourth = dict(zip(cg.labels(table), cg.col(table, FOURTH)))
    # The keyed choice names State G and a distractor names State H, so the rows
    # the choices refer to must be the rows the table actually has.
    assert set(first) == {"State G", "State H", "State J"}, \
        f"the choices refer to States G, H and J; the table holds {sorted(first)}"
    for name, share in list(first.items()) + list(fourth.items()):
        assert 0 <= share <= 100, f"{name} reports a share of {share} percent, which is not a share"
    fallen = [k for k in first if fourth[k] <= first[k]]
    assert not fallen, f"every state's fourth-year share must exceed its first-year share; {fallen} do not"
    assert min(list(first.values()) + list(fourth.values())) > 0, \
        "'only one state engages any of its adult population' must be false"
    # The item asks for the largest MULTIPLE, not the largest gain in percentage
    # points. It used to ask for the points, and its keyed sentence was then
    # identical to 7.6 q8's apart from the state letter -- the same analytical
    # move on a second table, which is the template repeat CLAUDE.md names.
    #
    # UNIQUENESS BEFORE IDENTITY. max() returns the FIRST row holding the
    # extremum, so a tie reads as a clean winner and a control aimed at the tie
    # guard would be answered by the identity assert instead.
    mult = {k: fourth[k] / first[k] for k in first}
    m_order = sorted(mult, key=mult.get, reverse=True)
    assert mult[m_order[0]] > mult[m_order[1]], "the largest multiple must be unique"
    assert m_order[0] == "State J", \
        f"the largest multiple belongs to {m_order[0]}, not State J"
    # THE TRAP IS THE ITEM. The state gaining most in percentage points must NOT
    # be the one growing by the largest multiple, or the two readings of the
    # table agree and the question tests nothing.
    rise = {k: fourth[k] - first[k] for k in first}
    p_order = sorted(rise, key=rise.get, reverse=True)
    assert rise[p_order[0]] > rise[p_order[1]], \
        "the largest points gain must be unique for the trap to be sharp"
    assert p_order[0] != m_order[0], (
        f"{p_order[0]} gains most in percentage points AND grows by the largest multiple, "
        f"so the distractor naming it is not a trap"
    )
    assert len(set(fourth.values())) > 1, \
        "'the three states reach the same share by the fourth year' must be false"
    return (f"every fourth-year share exceeds its first-year share; the multiples are "
            f"{ {k: round(v, 2) for k, v in mult.items()} }, largest at {m_order[0]}, while the "
            f"largest gain in percentage points is {p_order[0]}'s {rise[p_order[0]]:g} -- the two "
            f"readings disagree, which is what the item tests")


def q20(table, item):
    earlier = dict(zip(cg.labels(table), cg.col(table, EARLIER)))
    later = dict(zip(cg.labels(table), cg.col(table, LATER)))
    combined = dict(zip(cg.labels(table), cg.col(table, COMBINED)))
    assert set(earlier) == {"State S", "State T", "State U"}, \
        f"the choices refer to States S, T and U; the table holds {sorted(earlier)}"
    # The fourth column is the sum of the two before it, so no figure in this
    # table can be altered without the row ceasing to add up.
    for k in earlier:
        assert combined[k] == earlier[k] + later[k], (
            f"{k}: the combined column reports {combined[k]} but the two conflicts sum to "
            f"{earlier[k] + later[k]}"
        )
    fallen = [k for k in earlier if later[k] <= earlier[k]]
    assert not fallen, f"every state's later figure must exceed its earlier one; {fallen} do not"
    assert min(list(earlier.values()) + list(later.values())) > 0, \
        "'only one state records any casualties in the later conflict' must be false"
    rise = {k: later[k] - earlier[k] for k in earlier}
    order = sorted(rise, key=rise.get, reverse=True)
    assert rise[order[0]] > rise[order[1]], "the largest increase must be unique"
    assert order[0] == "State U", f"the largest increase belongs to {order[0]}, not State U"
    assert order[0] != "State T", "'the largest increase is in State T' must be false"
    top_earlier = max(earlier, key=earlier.get)
    assert rise[top_earlier] == max(rise.values()), \
        "'the state with the most casualties earlier records the smallest increase' must be false"
    return (f"every later figure exceeds its earlier one, each combined figure equals the two it "
            f"sums, the increases are {rise}, and the largest belongs to {order[0]}, which is also "
            f"the state highest in the earlier conflict")


TABLE_CHECKS = {19: q19, 20: q20}

CLAIMS = [
 ("That it was a total war",
  "KC-6.2.IV.A.ii opens by stating that World War II was a total war, while KC-6.2.IV.A.i reserves the phrase 'the first total war' for the earlier conflict, so the two characterisations are not interchangeable."),
 ("Political propaganda, art, media, and intensified forms of nationalism",
  "KC-6.2.IV.A.ii names political propaganda, art, media, and intensified forms of nationalism among the strategies governments used to mobilize populations for the purpose of waging war."),
 ("home countries and in the colonies or former colonies alike",
  "KC-6.2.IV.A.ii states in its own parenthesis that populations were mobilized both in the home countries and the colonies or former colonies, so the anchor carries both places because dropping either is the plausible error."),
 ("The colonies or former colonies",
  "KC-6.2.IV.A.i writes 'the colonies' for the first war and KC-6.2.IV.A.ii writes 'the colonies or former colonies' for the second, so the extension to former colonies is what distinguishes the later sentence; the other phrases appear in both."),
 ("For the purpose of waging war",
  "KC-6.2.IV.A.ii states that the mobilizing strategies were used for the purpose of waging war, which is the clause separating them from cultural or economic policy in general."),
 ("Fascism and communism",
  "KC-6.2.IV.A.ii says governments used ideologies, including fascism and communism, to mobilize all of their state's resources for war; intensified nationalism appears in the same sentence as a strategy rather than as one of the named ideologies."),
 ("All of their state's resources for war",
  "KC-6.2.IV.A.ii states that governments used ideologies to mobilize ALL of their state's resources for war, and that word is what makes the claim one about total war rather than about an army or an industry."),
 ("totalitarian states in particular, rather than to every government that fought",
  "KC-6.2.IV.A.ii attaches the repression of basic freedoms and the domination of many aspects of daily life to totalitarian states in particular while leaving the mobilization claim general, so the anchor carries both halves of the contrast."),
 ("During the course of the conflicts and beyond them",
  "KC-6.2.IV.A.ii ends with 'during the course of the conflicts and beyond', which extends the repression of basic freedoms and the domination of daily life past the end of the fighting."),
 ("New military technology together with new tactics",
  "KC-6.1.III.C.ii names new military technology AND new tactics as what led to increased levels of wartime casualties, whereas KC-6.1.III.C.i names technology alone for the first war, so the anchor carries both terms."),
 ("atomic bomb, fire-bombing, and the waging of total war",
  "KC-6.1.III.C.ii names the atomic bomb, fire-bombing, and the waging of total war among the new military technology and new tactics that led to increased levels of wartime casualties."),
 ("Great Britain under Winston Churchill and the United States under Franklin Roosevelt",
  "The CED prints this pair under the heading Western democracies mobilizing for war beside KC-6.2.IV.A.ii, and nothing is asserted about either government beyond that heading."),
 ("Germany under Adolf Hitler and the USSR under Joseph Stalin",
  "The CED prints this pair under the heading totalitarian states mobilizing for war beside KC-6.2.IV.A.ii, which is also the sentence attaching the repression of basic freedoms to totalitarian states in particular."),
 ("Both name states mobilizing for war",
  "The CED's two headings beside KC-6.2.IV.A.ii both read 'mobilizing for war', and that sentence states the mobilization claim of governments generally while attaching repression to totalitarian states alone, so mobilization is the shared element and repression is not."),
 ("made of governments generally, and the CED illustrates it with Western democracies",
  "KC-6.2.IV.A.ii makes its mobilization claim of governments without restricting it to one kind of state, and the CED prints Great Britain and the United States under a heading about mobilizing for war."),
 ("governments in Western democracies also mobilized their populations for war",
  "Suggested skill 3.D asks how evidence refutes an argument, and KC-6.2.IV.A.ii plus the CED's Western democracies heading make mobilization a claim about governments generally, so such evidence contradicts an exclusive claim about single-party states."),
 ("assigned civilians to war production and directed media towards the war effort",
  "Suggested skill 3.D asks how evidence supports an argument, and KC-6.2.IV.A.ii calls the war a total war, names media among the mobilizing strategies and states that all of the state's resources were mobilized for war."),
 ("mobilized their populations without repressing basic freedoms",
  "Suggested skill 3.D distinguishes modifying an argument from refuting it, and KC-6.2.IV.A.ii attaches repression to totalitarian states in particular while leaving mobilization general, so such evidence narrows the account without overturning its mobilization claim."),
 ("it grows by the largest multiple in State J",
  "KC-6.2.IV.A.ii states that governments used ideologies to mobilize all of their state's resources for war, and this item asks a student to read a rising share of the adult population out of data. Recomputed in q19 above from the illustrative table alone, including the swapped distractor."),
 ("largest increase is in State U",
  "KC-6.1.III.C.ii states that new military technology and new tactics led to increased levels of wartime casualties, and this item asks a student to read that increase out of data. Recomputed in q20 above from the illustrative table alone, including the combined column that must agree with the two figures it sums."),
 ("political propaganda used to mobilize a home population",
  "KC-6.2.IV.A.ii names political propaganda among the strategies used to mobilize populations, in the home countries and the colonies or former colonies, for the purpose of waging war."),
 ("mobilization reaching the colonies or former colonies as well as the home countries",
  "KC-6.2.IV.A.ii states that populations were mobilized both in the home countries and the colonies or former colonies, and the second half of that parenthesis is the phrase the framework adds for the second war."),
 ("repression of basic freedoms and domination of daily life the framework attributes to totalitarian states",
  "KC-6.2.IV.A.ii says that in the case of totalitarian states governments used ideologies to repress basic freedoms and dominate many aspects of daily life, which covers control of the press, of movement and of labour."),
 ("such domination of daily life extended beyond the conflicts themselves",
  "KC-6.2.IV.A.ii says totalitarian states repressed basic freedoms and dominated many aspects of daily life during the course of the conflicts AND BEYOND, so a wartime control still in force afterwards is inside the framework's account rather than an exception to it."),
 ("That the conflict was a total war",
  "KC-6.2.IV.A.i opens 'World War I was the first total war' and KC-6.2.IV.A.ii opens 'World War II was a total war', so this is the one characterisation the framework states of both; the four distractors are clauses .ii adds that .i does not carry. Replaces an item that was topic 7.3 q12 with 'First' swapped for 'Second', identical choices and identical key."),
 ("ideologies, including fascism and communism, to mobilize all of the state's resources",
  "KC-6.2.IV.A.i and KC-6.2.IV.A.ii both name propaganda, art, media and intensified nationalism, and both casualty sentences name new military technology, but the ideologies clause appears only in KC-6.2.IV.A.ii."),
 ("alike, and in what ways did they differ",
  "Unit 7 Learning Objective G asks students to explain similarities and differences in how governments used a variety of methods to conduct war."),
 ("mobilization claim about governments generally and then marks off one clause for totalitarian states",
  "KC-6.2.IV.A.ii states a general mobilization claim and then adds a clause holding only in the case of totalitarian states, and the CED prints its examples under two headings that set the two kinds of state side by side."),
 ("left the populations of their colonies and former colonies out of the war effort",
  "KC-6.2.IV.A.ii states that populations were mobilized both in the home countries and the colonies or former colonies, so leaving those populations out contradicts the sentence while the other options restate KC-6.2.IV.A.ii and KC-6.1.III.C.ii."),
 ("with totalitarian states also repressing freedoms",
  "KC-6.2.IV.A.ii supplies the total war characterisation, the mobilization of populations at home and in the colonies or former colonies, the mobilization of all the state's resources through ideologies and the repression clause for totalitarian states, and KC-6.1.III.C.ii supplies the rise in casualties, so a summary must carry all of them."),
]

wh_check.run(w7_7, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
