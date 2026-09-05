"""Key audit for AP WORLD HISTORY: MODERN 6.6 Causes of Migration in an Interconnected World.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The gate is ``wh_check.run``, the shared World History gate: ``cg_check.check``
for structure and anchors, ``es_check.style`` for notation (World History is a
prose subject that ``export_units.py`` does not typeset), plus the two rules
history adds -- a CED citation in every ``why`` and every ``claim``, and no
figure language, since the bank cannot display an image.

WHAT THE KEYS REST ON
---------------------
This topic prints four historical developments:

    KC-5.4.I     Migration in many cases was influenced by changes in demographics
                 in both industrialized and unindustrialized societies that
                 presented challenges to existing patterns of living.
    KC-5.4.I.B   Because of the nature of new modes of transportation, both
                 internal and external migrants increasingly relocated to cities.
                 This pattern contributed to the significant global urbanization
                 of the 19th century. The new methods of transportation also
                 allowed for many migrants to return, periodically or
                 permanently, to their home societies.
    KC-5.4.II.A  Many individuals chose freely to relocate, often in search of work.
    KC-5.4.II.B  The new global capitalist economy continued to rely on coerced and
                 semicoerced labor migration, including enslavement Chinese and
                 Indian indentured servitude, and convict labor.

Items 1, 2, 17 rest on KC-5.4.I. Items 3, 4, 5, 16, 27 rest on the three clauses
of KC-5.4.I.B. Items 6, 14 rest on KC-5.4.II.A; items 7, 8, 15, 18 on
KC-5.4.II.B. Items 9 to 13 ask only which HEADING the CED prints an illustrative
group under, never what any group did, because the CED names these groups and
describes none of them. Item 28 rests on KC-5.4, printed in this unit's review
for topic 6.8. Item 26 rests on the CED printing TWO learning objectives for this
topic, F on environmental and G on economic factors. Items 29 and 30 are
reasoning items about what these statements do and do not settle.

THE MISSING COMMA IN KC-5.4.II.B. The CED text as extracted reads "including
enslavement Chinese and Indian indentured servitude, and convict labor", which is
plainly enslavement, Chinese and Indian indentured servitude, and convict labor
with a comma dropped in the source PDF. Item 8 is the only item that touches the
list, and it asks which form is NOT named -- a question the punctuation cannot
change, since conscription for overseas garrisons appears nowhere in the sentence
under either reading. No item keys on how many forms the list contains.

DIRECTION AND SWAP. KC-5.4.I.B runs transportation to cities to urbanization,
and the illustrative examples run from a named origin to a named destination.
Items 3, 12 and 25 each carry the exact reversal as a distractor, so their anchors
carry BOTH clauses; item 29's anchor does the same for the reversal of what the
framework can and cannot answer.

DATA ITEMS: 19 to 25 carry tables labelled hypothetical in the stem, and every
keyed conclusion is recomputed below from that table alone. Every row label is
matched EXACTLY rather than by substring, because ``es_check._corrupt`` appends
" CORRUPTED" to a cell and a substring test would still read the corrupted label
as its original -- the control would pass while proving nothing. The numeric
guards are ratio guards rather than threshold guards for the same reason: the
control multiplies a cell by three and adds eleven, so a bare "is this still the
largest" test frequently survives it while a share does not.

NEGATIVE CONTROL: ``python3 verify_w6_6.py --selftest`` rotates every key off its
anchor, corrupts every table cell in turn, injects each banned notation form (and
one legal string that must pass), duplicates a choice, thins a why and makes a
why name an option by letter, and requires every one of those to raise. It then
runs legal-value controls on the ratio guards, which the cell corruption cannot
reach because it trips the label vocabulary first.
"""
import sys

import cg_check as cg
import es_check as es
import wh_check as wh
import w6_6

LEFT = "People leaving in one decade (thousands)"
BACK = "People returning to the home society in the same decade (thousands)"
STREAMS = ["Stream 1", "Stream 2", "Stream 3", "Stream 4"]

SETTLE_N = "Migrants settling there (thousands)"
CITIES = "Cities of more than one hundred thousand people"
TOWNS = "Towns smaller than that"
RURAL = "Rural districts"

DEPARTURES = "Departures recorded in one year (thousands)"
FREE = "People travelling at their own expense in search of work"
INDENTURE = "People travelling under contracts of indenture"
CONVICT = "People transported under sentence of a court"
ENSLAVED = "People moved under conditions of enslavement"
COERCED = (INDENTURE, CONVICT, ENSLAVED)

ARRIVALS_N = "Arrivals in one decade (thousands)"
RURAL_SAME = "Rural districts of the same country"
OTHER_SAME = "Other regions of the same country"
OVERSEAS = "Countries overseas"


def _rows(table):
    idx = {h: j for j, h in enumerate(table["headers"])}
    return [{h: str(r[j]) for h, j in idx.items()} for r in table["rows"]]


def _by_label(table, expected):
    """Rows keyed by an EXACT first-column label drawn from `expected`.

    Exact membership, never a substring test. The negative control corrupts a
    cell by appending " CORRUPTED"; a substring test would still read
    "Rural districts CORRUPTED" as the rural row, and the control would pass
    without exercising anything.
    """
    rows = _rows(table)
    label_col = table["headers"][0]
    got = [r[label_col] for r in rows]
    assert got == list(expected), f"row labels must be {list(expected)}, not {got}"
    return {r[label_col]: r for r in rows}


def _streams(table):
    by = _by_label(table, STREAMS)
    out = {}
    for name in STREAMS:
        left, back = cg.num(by[name][LEFT]), cg.num(by[name][BACK])
        assert left > 0, f"{name} records no departures"
        assert 0 < back < left, \
            f"{name} returns {back:g} against {left:g} leaving, which is not a share of those who left"
        out[name] = (left, back, back / left)
    return out


def q19(table, item):
    s = _streams(table)
    shares = {k: v[2] for k, v in s.items()}
    top = max(shares, key=shares.get)
    assert top == "Stream 4", f"the largest returning share is {top}, not Stream 4"
    assert len(set(round(v, 6) for v in shares.values())) == len(shares), \
        "two streams share a returning proportion, so the keyed stream is not unique"
    assert shares["Stream 4"] > 0.4, \
        "the why calls Stream 4's share above two in five; it is not"
    # The whys for items 19 and 20 QUOTE these pairs to the student ("86 of the
    # 200", "9 of 60"). A why that misquotes its own table is a defect of the same
    # family as a wrong key, so the quoted figures are checked against the record
    # rather than trusted. This check runs last so that a mutation which breaks a
    # proportion is reported by the proportion guard, not by this one.
    quoted = {"Stream 1": (120, 44), "Stream 2": (90, 31),
              "Stream 3": (60, 9), "Stream 4": (200, 86)}
    for name, pair in quoted.items():
        got = (s[name][0], s[name][1])
        assert got == pair, \
            f"the whys quote {name} as {pair[1]} of {pair[0]}; the record gives {got[1]:g} of {got[0]:g}"
    return ("Stream 4 returns 86 of 200, the largest of the four proportions, no two "
            "streams tie, and every figure the whys quote matches the record")


def q20(table, item):
    s = _streams(table)
    assert all(v[1] > 0 for v in s.values()), "'no stream recorded any return' must be false"
    assert not any(v[1] > v[0] for v in s.values()), \
        "'every stream returned more than it sent' must be false"
    assert len(set(round(v[2], 6) for v in s.values())) > 1, \
        "'the share was the same in every stream' must be false"
    biggest = max(s, key=lambda k: s[k][0])
    smallest_share = min(s, key=lambda k: s[k][2])
    assert biggest != smallest_share, \
        "'the stream sending the most returned the smallest share' must be false"
    return ("all four streams show returns, the shares differ, none exceeds its outward "
            "flow, and the largest sender is not the smallest returner")


def _settle(table):
    by = _by_label(table, [CITIES, TOWNS, RURAL])
    v = {k: cg.num(by[k][SETTLE_N]) for k in (CITIES, TOWNS, RURAL)}
    total = sum(v.values())
    assert total > 0, "the settlement record is empty"
    return v, total


def q21(table, item):
    v, total = _settle(table)
    share = v[CITIES] / total
    # A ratio guard, not a threshold guard. The control turns 148 into 455, which
    # would still be "more than half" but is not "close to seven in ten".
    assert 0.6 <= share <= 0.75, \
        f"cities take {share * 100:.1f} percent, which is not close to seven in ten"
    assert v[RURAL] / total < 0.6, "'seven in ten settled in rural districts' must be false"
    assert len(set(v.values())) == 3, "'divided evenly among the three' must be false"
    assert share > 0.5, "'fewer than half settled in the largest cities' must be false"
    assert v[TOWNS] + v[RURAL] > 0, "'no migrant settled outside a city' must be false"
    return (f"{v[CITIES]:g} of {total:g} thousand settled in the largest cities, "
            f"{share * 100:.1f} percent, close to seven in ten")


def q22(table, item):
    v, total = _settle(table)
    assert v[RURAL] < v[CITIES], \
        "the keyed statement must be FALSE on the record: rural must not exceed cities"
    assert v[CITIES] > total / 2, "'cities received more than half' must be true"
    assert v[RURAL] == min(v.values()), "'rural districts the smallest' must be true"
    assert len(v) == 3, "'three kinds of place' must be true"
    assert v[TOWNS] > v[RURAL], "'towns received more than rural districts' must be true"
    return ("rural districts take 26 against 148 thousand in the largest cities, so the "
            "keyed claim is the unsupported one while the four rejected ones read off the column")


def _register(table):
    by = _by_label(table, [FREE, INDENTURE, CONVICT, ENSLAVED])
    v = {k: cg.num(by[k][DEPARTURES]) for k in (FREE, INDENTURE, CONVICT, ENSLAVED)}
    for k, n in v.items():
        assert n > 0, f"{k} records no departures"
    return v


def q23(table, item):
    v = _register(table)
    coerced = sum(v[k] for k in COERCED)
    assert v[FREE] == max(v.values()), "the freely travelling group must be the largest entry"
    assert coerced > 0, "'only free relocation' must be false"
    assert v[FREE] > 0, "'only coerced arrangements' must be false"
    # A ratio guard: the control turns 121 into 374, which is still the largest
    # entry but is no longer an entry the coerced total is comparable to.
    assert coerced > v[FREE] / 2, \
        f"the coerced total {coerced:g} is not comparable to the free entry {v[FREE]:g}"
    assert coerced < v[FREE], "the free entry must remain the largest single category"
    assert len(set(v.values())) > 1, "'the same number in each category' must be false"
    return (f"the free entry stands at {v[FREE]:g} thousand, the largest single category, "
            f"against {coerced:g} thousand across the three coerced categories")


def q24(table, item):
    v = _register(table)
    coerced = sum(v[k] for k in COERCED)
    assert len(COERCED) == 3, "three of the four categories must be coerced or semicoerced"
    assert coerced == 84, \
        f"the keyed choice names 84 thousand; the register gives {coerced:g}"
    assert v[FREE] == max(v.values()), \
        "'the largest category is people travelling at their own expense' must be true"
    assert len(v) == 4, "'four categories in all' must be true"
    return (f"indenture, court sentence and enslavement come to {coerced:g} thousand "
            "departures, which is what refutes a claim that they had disappeared")


def _arrivals(table):
    by = _by_label(table, [RURAL_SAME, OTHER_SAME, OVERSEAS])
    v = {k: cg.num(by[k][ARRIVALS_N]) for k in (RURAL_SAME, OTHER_SAME, OVERSEAS)}
    internal = v[RURAL_SAME] + v[OTHER_SAME]
    return v, internal, v[OVERSEAS], internal + v[OVERSEAS]


def q25(table, item):
    v, internal, external, total = _arrivals(table)
    assert internal > 0, "'only from countries overseas' must be false"
    assert external > 0, "'only from within its own country' must be false"
    assert total > 0, "'no arrivals from any origin' must be false"
    share = external / total
    # The swap distractor puts the one-in-three on the INTERNAL side, so the guard
    # has to fix which side the third belongs to, not merely that a third exists.
    assert 0.30 <= share <= 0.40, \
        f"overseas arrivals are {share * 100:.1f} percent, which is not roughly one in three"
    assert internal / total > 0.5, \
        "the reversed reading must be false: arrivals from within the country are the majority"
    return (f"{external:g} of {total:g} thousand arrivals come from overseas, "
            f"{share * 100:.1f} percent, against {internal:g} thousand from within the country")


TABLE_CHECKS = {19: q19, 20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25}

CLAIMS = [
 ("both industrialized and unindustrialized societies",
  "KC-5.4.I states that migration in many cases was influenced by changes in demographics in BOTH industrialized and unindustrialized societies. The anchor carries the pairing because every rejected option confines the demographic change to one side of it or denies that the framework names any society."),
 ("Challenges to existing patterns of living",
  "KC-5.4.I's own wording: those changes in demographics presented challenges to existing patterns of living. The framework does not say they ended migration, improved living standards uniformly or prohibited movement, and a general return of migrants belongs to KC-5.4.I.B rather than to this clause."),
 ("New modes of transportation led both internal and external migrants increasingly to relocate to cities",
  "KC-5.4.I.B, near verbatim: because of the nature of new modes of transportation, both internal and external migrants increasingly relocated to cities. The exact reversal of cause and effect is offered as a distractor and the reversal of the direction of the move as another, so the anchor carries both clauses."),
 ("significant global urbanization of the 19th century",
  "KC-5.4.I.B states that this pattern contributed to the significant global urbanization of the 19th century. Depopulation is the opposite of that clause, and the end of travel, the abolition of coerced labour and an equalization of population between countryside and city are asserted nowhere in it."),
 ("allowed many migrants to return, periodically or permanently, to their home societies",
  "KC-5.4.I.B's closing sentence: the new methods of transportation also allowed for many migrants to return, periodically or permanently, to their home societies. Allowing a return is neither requiring one nor preventing one, and the statement puts no limit on who could travel."),
 ("Many individuals chose freely to relocate, often in search of work",
  "KC-5.4.II.A verbatim. The search for work is part of that sentence, so an option removing the work motive or substituting another contradicts it, as does an option denying that free choice was common in this period."),
 ("Coerced and semicoerced labour migration",
  "KC-5.4.II.B states that the new global capitalist economy CONTINUED to rely on coerced and semicoerced labor migration. The word continued is the framework's own, so an option asserting an end to such migration, or its confinement within one country, is the opposite of that sentence."),
 ("Conscription of soldiers for service in overseas garrisons",
  "KC-5.4.II.B names enslavement, Chinese and Indian indentured servitude, and convict labor. Conscription for overseas garrisons appears nowhere in that sentence, which is what makes it the form the framework does not name; the four rejected options are each printed in it. The item does not depend on the missing comma in the source text, because it asks only what is absent."),
 ("Return of migrants",
  "The CED prints Japanese agricultural workers in the Pacific under its heading Return of migrants for topic 6.6. The CED prints that heading beside KC-5.4.I.B, its statement about return. Migrant ethnic enclaves and the regulation of immigrants are headings in topic 6.7 and resource export economies one in topic 6.4, so each rejected option names a real heading from the wrong topic."),
 ("The Americas",
  "The CED prints Lebanese merchants in the Americas under its heading Return of migrants for topic 6.6, beside KC-5.4.I.B. The Pacific belongs to the Japanese agricultural workers in the same list, and South Asia, West Africa and Australia appear in other topics of this unit rather than in this example."),
 ("The return of migrants to their home societies",
  "The CED prints Italian industrial workers in Argentina under the heading Return of migrants for topic 6.6, and KC-5.4.I.B is the statement that new methods of transportation allowed many migrants to return periodically or permanently. Enclaves and immigration regulation are topic 6.7's headings, export economies topic 6.4's and economic imperialism topic 6.5's."),
 ("British engineers and geologists going to South Asia and Africa",
  "The CED prints British engineers and geologists to South Asia and Africa under its heading Migrants for topic 6.6, beside KC-5.4.II.A and KC-5.4.II.B. Origin and destination are the whole content of the example and the exact reversal is offered as a distractor, so the anchor carries both clauses."),
 ("Among migrants",
  "The CED prints Irish to the United States under the heading Migrants for topic 6.6, while its Return of migrants heading names the Japanese, Lebanese and Italian examples. That heading is printed beside KC-5.4.II.A. Irish in North America appear again in topic 6.7 under migrant ethnic enclaves, which is a different topic's list and a different claim."),
 ("an individual choosing freely to relocate in search of work",
  "KC-5.4.II.A states that many individuals chose freely to relocate, often in search of work, and an unattributed letter reporting higher wages and a choice of employer describes that motive. Indenture and transportation under sentence are the coerced and semicoerced forms of KC-5.4.II.B, and the source is illustrative and attributed to no one."),
 ("coerced and semicoerced labour migration the framework says the global capitalist economy relied on",
  "KC-5.4.II.B names indentured servitude among the coerced and semicoerced forms the new global capitalist economy continued to rely on, and a term bound to one employer with the passage recovered from wages is an arrangement of that kind. Free relocation, return, urbanization and demographic change are each a different statement of this topic."),
 ("new methods of transportation allowed many migrants to return to their home societies",
  "KC-5.4.I.B states that the new methods of transportation allowed for many migrants to return, periodically or permanently, to their home societies, and a cheaper and faster round passage is the practical form of that possibility. The illustrative advertisement shows no compulsion, and the framework asserts none."),
 ("a change in demographics presenting a challenge to an existing pattern of living",
  "KC-5.4.I states that migration was in many cases influenced by changes in demographics that presented challenges to existing patterns of living, and a district whose holdings will no longer support its rising generation is such a challenge. Border regulation and enclaves belong to topic 6.7, convict labour to KC-5.4.II.B and return to KC-5.4.I.B."),
 ("continued to rely on convict labour among other coerced forms",
  "KC-5.4.II.B names convict labor among the coerced and semicoerced forms of labour migration that the new global capitalist economy continued to rely on, and a sentence of transportation to labour for a term is that form. The option asserting that receiving societies always welcomed migrants is contradicted by KC-5.4.III.C in the next topic."),
 ("Stream 4",
  "Recomputed in q19 above: Stream 4 returns 86 of the 200 who left, the largest of the four proportions, and no two streams tie, so the keyed stream is unique. KC-5.4.I.B is the statement about return that the record illustrates. The record gives both columns for every stream, so the option denying that the shares can be compared is false on the table itself."),
 ("Every stream recorded some return migration, and the share returning differed from stream to stream",
  "Recomputed in q20 above: all four streams show returns, no stream returns more than it sent, the shares are not equal, and the largest sender is also the largest returner rather than the smallest. KC-5.4.I.B says the new methods allowed MANY migrants to return, which is neither all nor none."),
 ("Close to seven in every ten of these migrants settled in the largest cities",
  "Recomputed in q21 above: 148 of 216 thousand, about sixty-nine percent, settled in cities of more than one hundred thousand people, against 42 in smaller towns and 26 in rural districts. That is the pattern KC-5.4.I.B describes when it says migrants increasingly relocated to cities and that this contributed to significant global urbanization."),
 ("Rural districts received more of these migrants than the largest cities did",
  "Recomputed in q22 above: rural districts take 26 thousand against 148 in the largest cities, so the keyed statement is the one the record contradicts, while each rejected statement is checked to be TRUE of the same column. This is a NOT-supported item, so the key is the false claim by design, and KC-5.4.I.B is the statement about relocation to cities the record illustrates."),
 ("with the freely travelling group the largest single category",
  "Recomputed in q23 above: 121 thousand travel at their own expense, the largest single entry, while indenture, court sentence and enslavement are coerced or semicoerced arrangements totalling 84 thousand. KC-5.4.II.A and KC-5.4.II.B are both statements of this topic and the register shows the two side by side."),
 ("together they account for 84 thousand departures",
  "Recomputed in q24 above: indenture at 58, court sentence at 17 and enslavement at 9 come to 84 thousand, which is what refutes a claim that such arrangements had disappeared. The four rejected statements are true of the register and leave that claim standing, and KC-5.4.II.B says the economy CONTINUED to rely on these forms."),
 ("with roughly one in three arriving from overseas",
  "Recomputed in q25 above: 71 of 205 thousand arrivals come from overseas and 134 thousand from within the same country, so the third belongs on the overseas side. The swapped proportion is offered as a distractor, so the anchor carries both clauses, and KC-5.4.I.B says BOTH internal and external migrants increasingly relocated to cities."),
 ("arising from more than one kind of cause",
  "The CED prints TWO learning objectives for topic 6.6: Learning Objective F, how various environmental factors, and Learning Objective G, how various economic factors contributed to the development of varied patterns of migration from 1750 to 1900. Printing both is what shows the framework treating the causes as plural rather than as one kind, one period or none."),
 ("how a change in transportation bore on where migrants settled and on whether they could go home",
  "KC-5.4.I.B links new modes of transportation to relocation to cities, to global urbanization and to the possibility of return, and suggested skill 5.B asks how one historical development relates to another. Attending to one end of that link alone is not the relation, and the framework prints no date for any mode of transportation."),
 ("emergence of transoceanic empires and of a global capitalist economy",
  "KC-5.4, printed in this unit's review, reads that as a result of the emergence of transoceanic empires and a global capitalist economy, migration patterns changed dramatically and the numbers of migrants increased significantly. Each rejected option asserts the opposite of one clause of that sentence."),
 ("Which kinds of cause the framework identifies can be answered; how many people left any particular society cannot",
  "KC-5.4.I, KC-5.4.I.B, KC-5.4.II.A and KC-5.4.II.B between them name demographic change, transportation, the search for work and coercion as causes, so the kinds of cause are answerable; the framework prints no figure, no route and no starting date for any stream. The anchor carries both clauses because the exact reversal is offered."),
 ("new transportation shaped where they went and whether they returned, and coercion continued to move others against their will",
  "KC-5.4.I gives demographic change, KC-5.4.II.A free relocation often in search of work, KC-5.4.I.B transportation shaping destination and return, and KC-5.4.II.B the continued reliance on coerced and semicoerced labour migration. The key holds all four together and each rejected option deletes one or more of them."),
]


# --------------------------------------------------------- legal-value controls
#
# es_check's cell control appends " CORRUPTED", which trips the exact label
# vocabulary in _by_label before any ratio guard runs, and multiplies a number by
# three and adds eleven, which a threshold guard often survives. So each ratio
# guard gets a control that substitutes one LEGAL value for another: the table
# stays well formed and the only thing that changes is the proportion the key
# asserts. Each control asserts on the MESSAGE, because a control that fires for
# the wrong reason proves nothing about the guard it names.

def _fires(base, mutate, check, needle, label):
    import copy
    table = copy.deepcopy(base)
    mutate(table["rows"])
    try:
        check(table, None)
    except AssertionError as exc:
        assert needle in str(exc), \
            f"CONTROL FIRED FOR THE WRONG REASON ({label}): expected {needle!r}, got {exc}"
        return
    raise SystemExit(f"CONTROL FAILED: {label} -- {check.__name__} accepted the mutation")


def ratio_control():
    st, se, rg, ar = (w6_6._T_STREAMS, w6_6._T_SETTLE, w6_6._T_REGISTER, w6_6._T_ARRIVALS)

    # Stream 3 returns 9 of 60; raise it to 40 and its share passes Stream 4's, so
    # the keyed stream is no longer the largest returner.
    _fires(st, lambda rows: rows[2].__setitem__(2, "40"), q19,
           "the largest returning share is Stream 3", "item 19 with a new largest returner")
    # Make Stream 4 send the most AND return the smallest share, which turns a
    # rejected option into a true one.
    _fires(st, lambda rows: rows[3].__setitem__(2, "10"), q20,
           "returned the smallest share", "item 20 with the largest sender returning least")
    # 100 is a legal count but drops the cities' share to about six in ten... below
    # the band the key claims, so the ratio guard must fire where a "more than
    # half" test would not.
    _fires(se, lambda rows: rows[0].__setitem__(1, "100"), q21,
           "not close to seven in ten", "item 21 with the city share thinned")
    _fires(se, lambda rows: rows[2].__setitem__(1, "200"), q22,
           "rural must not exceed cities", "item 22 with rural districts made the largest")
    # 300 is a legal count and still the largest entry, but the coerced total is no
    # longer comparable to it, which a bare "is it the largest" test would miss.
    _fires(rg, lambda rows: rows[0].__setitem__(1, "300"), q23,
           "is not comparable to the free entry", "item 23 with the free entry inflated")
    _fires(rg, lambda rows: rows[1].__setitem__(1, "40"), q24,
           "the register gives", "item 24 with the coerced total moved off 84")
    # Swap the proportion onto the internal side, which is exactly the distractor.
    _fires(ar, lambda rows: rows[0].__setitem__(1, "20"), q25,
           "not roughly one in three", "item 25 with the overseas share raised")

    # POSITIVE control: the same seven checks must ACCEPT the module's own tables,
    # so a check that rejected everything would be caught here rather than counted
    # as seven successes.
    for fn in (q19, q20):
        fn(st, None)
    for fn in (q21, q22):
        fn(se, None)
    for fn in (q23, q24):
        fn(rg, None)
    q25(ar, None)
    print("  control OK  every ratio guard fires on a legal-value mutation, for the "
          "reason it names, and passes the real tables")


if "--selftest" in sys.argv:
    ratio_control()

wh.run(w6_6, CLAIMS, table_checks=TABLE_CHECKS, argv=sys.argv)
