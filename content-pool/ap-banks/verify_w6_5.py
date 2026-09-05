"""Key audit for AP WORLD HISTORY: MODERN 6.5 Economic Imperialism from 1750 to 1900.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is ``cg_check.check``; the notation gate and the negative
control are ``es_check``, reused unchanged, exactly as verify_w6_4.py does,
because World History is a prose subject that ``export_units.py`` does not
typeset.

WHY THIS FILE EXISTS LATE
-------------------------
w6_5.py was authored by an agent that was stopped before writing its verifier,
so thirty questions sat in the tree with NO gate on them. Reading them found one
real defect, in the shipment-record items: item 15 asked which SINGLE shipment
was arranged by a firm based in the region of production, and two rows of the
record satisfy that (Record 5, Latin America to Latin America, and Record 4,
Western Europe to Western Europe). The item had two defensible answers. The
repair is recorded in w6_5.py's header. The check that would have caught it is
the one this file now makes on every one of those items: not "is the keyed row
consistent with the stem" but "is the keyed row the ONLY row consistent with the
stem", asserted against the table itself.

WHAT THE KEYS REST ON
---------------------
This topic prints two historical developments:

    KC-5.2.I.E   Industrialized states and businesses within those states
                 practiced economic imperialism primarily in Asia and Latin
                 America.
    KC-5.1.II.C  Trade in some commodities was organized in a way that gave
                 merchants and companies based in Europe and the U.S. a distinct
                 economic advantage.

Items 1, 2, 8, 9, 22, 28 rest on KC-5.2.I.E: who practiced it, and where.
Items 3, 11, 20, 23, 25, 27 rest on KC-5.1.II.C: that the ORGANIZATION of a
trade, not the goods, is where the framework locates the advantage.
Items 4, 5, 6, 7 rest on the CED's printed commodity list. Every one of those
examples carries a DIRECTION -- produced in one place, exported to another -- so
each anchor carries both clauses and the reversal is offered as a distractor.

Item 12 and item 24 turn on holding the two statements apart: the regional claim
("primarily in Asia and Latin America") belongs to KC-5.2.I.E alone, while the
commodity list under KC-5.1.II.C includes a sub-Saharan African product. Merging
them is the easiest wrong key in this topic and both items refuse to.

Items 10, 19, 26 rest on the logic of evidence rather than on a claim about what
happened, and the claims below say so rather than citing a key concept the key
does not follow from. Item 21 rests on KC-5.2, printed in the unit 6 review for
topic 6.8, that as states industrialized they expanded existing overseas empires
and established new colonies and transoceanic relationships. Items 29 and 30 are
reasoning items about what these two statements do and do not settle.

No item asks what happened in the Opium Wars, when they happened, who signed
what, or what anything cost: the CED names those examples and describes none of
them. Every source is unattributed and labelled illustrative.

DATA ITEMS: 13 to 18 carry tables whose values are hypothetical and labelled so
in the stem. Both categorical columns of the shipment record are validated by
EXACT vocabulary rather than by substring, because ``es_check._corrupt`` appends
text to a cell and a substring test would still read "Latin America CORRUPTED"
as Latin America -- the control would pass while proving nothing. The share
column is bounded to 0 to 100, which is what catches a corrupted number: the
control multiplies a cell by three and adds eleven, so 88 becomes 275 and a bare
"is it still a majority" test would not notice.

NEGATIVE CONTROL: ``python3 verify_w6_5.py --selftest`` rotates every key off its
anchor, corrupts every table cell in turn, injects each banned notation form (and
one legal string that must pass), duplicates a choice, thins a why and makes a
why name an option by letter, and requires every one of those to raise.
"""
import sys

import cg_check as cg
import es_check as es
import w6_5

LABEL = "Shipment record (hypothetical)"
MADE = "Region where the good was produced"
SENT = "Region to which it was shipped"
FIRM = "Home base of the firm arranging the shipment"

REGIONS = {"South Asia", "Latin America", "Sub-Saharan Africa", "Western Europe",
           "North America"}
EURO_NA = {"Western Europe", "North America"}
RECORDS = ["Record 1", "Record 2", "Record 3", "Record 4", "Record 5"]

SERVICE = "Service required to move one hypothetical commodity to market"
SHARE = "Share provided by firms based in Europe or North America (hypothetical, percent)"
SHIPPING = "Ocean shipping"
INSURANCE = "Marine insurance"
FINANCE = "Trade finance and credit"
WAREHOUSE = "Warehousing at the port of shipment"
GROWING = "Growing and harvesting the crop"
MOVING = (SHIPPING, INSURANCE, FINANCE)


def _rows(table):
    idx = {h: j for j, h in enumerate(table["headers"])}
    return [{h: str(r[j]) for h, j in idx.items()} for r in table["rows"]]


def _ships(table):
    """Rows of the shipment record, with every cell validated by exact match.

    Exact membership, never a substring test: the negative control corrupts a
    cell by appending " CORRUPTED", and a substring test would still read
    "Western Europe CORRUPTED" as Western Europe. The control would then pass
    without exercising anything.
    """
    rows = _rows(table)
    assert [r[LABEL] for r in rows] == RECORDS, \
        f"the record's rows must be {RECORDS}, not {[r[LABEL] for r in rows]}"
    for r in rows:
        for column in (MADE, SENT, FIRM):
            assert r[column] in REGIONS, f"{r[LABEL]}: unexpected {column} {r[column]!r}"
    return rows


def q13(table, item):
    rows = _ships(table)
    n = sum(1 for r in rows if r[FIRM] in EURO_NA)
    assert len(rows) == 5, f"the stem says five shipments; the record holds {len(rows)}"
    assert n == 4, f"firms based in Europe or North America arrange {n} shipments, not four"
    # every rejected count must be false, so no second choice is defensible
    for wrong in (1, 2, 3, 5):
        assert n != wrong, f"the count is also {wrong}"
    return ("four of the five arranging firms are based in Western Europe or North "
            "America, and only one is based elsewhere")


def q14(table, item):
    rows = _ships(table)
    made_in_we = [r[LABEL] for r in rows if r[MADE] == "Western Europe"]
    assert made_in_we == ["Record 4"], \
        f"exactly one row must be produced in Western Europe; got {made_in_we}"
    sent_to_we = [r[LABEL] for r in rows if r[SENT] == "Western Europe"]
    assert len(sent_to_we) > 1, \
        "the stem contrasts producing with receiving, so Western Europe must also receive"
    assert "Record 4" not in sent_to_we, "Record 4 must not also be a destination row"
    return (f"Record 4 alone is produced in Western Europe, while {sent_to_we} receive "
            "goods there, so the keyed row is unique under the stem")


def q15(table, item):
    rows = _ships(table)
    home = [r[LABEL] for r in rows if r[FIRM] == r[MADE]]
    # THE CHECK WHOSE ABSENCE SHIPPED THE DEFECT. Two rows have the arranging firm
    # based in the region of production, so "the single shipment arranged by a firm
    # based in the region of production" had two answers. The stem's second
    # condition -- produced outside Europe and North America -- is what makes the
    # keyed row unique, and that uniqueness is asserted here rather than assumed.
    assert sorted(home) == ["Record 4", "Record 5"], \
        f"expected both self-arranged rows; got {home}"
    keyed = [r[LABEL] for r in rows if r[FIRM] == r[MADE] and r[MADE] not in EURO_NA]
    assert keyed == ["Record 5"], \
        f"exactly one row may satisfy BOTH conditions in the stem; got {keyed}"
    others = [r[LABEL] for r in rows if r[FIRM] != r[MADE]]
    assert sorted(others) == ["Record 1", "Record 2", "Record 3"], \
        f"the remaining rows must have the firm outside the producing region; got {others}"
    return ("Record 5 alone is both produced outside Europe and North America and "
            "arranged by a firm based in its own region of production")


def q16(table, item):
    rows = _ships(table)
    home = [r[LABEL] for r in rows if r[FIRM] == r[MADE]]
    assert home, "the key says at least one such shipment exists; the record shows none"
    assert len(home) < len(rows), "the record must not make every firm a local one"
    # Each rejected option is TRUE of the record but leaves the student's claim
    # standing. The first draft of this check asked whether a header contained the
    # token "good" and fired on "Region where the good was produced" -- an
    # over-matching checker, the own-goal this project keeps paying for. What the
    # rejected options actually assert is that the record holds no commodity name,
    # no value and no year, and _ships above has already established that every
    # cell outside the label column is one of five region names.
    assert not any("commodit" in h.lower() or "value" in h.lower() or "year" in h.lower()
                   for h in table["headers"]), \
        f"no column may name a commodity, a value or a year; headers are {table['headers']}"
    assert len(rows) == 5, "the record covers five shipments"
    return (f"{len(home)} of the {len(rows)} rows have the arranging firm based in the "
            "producing region, so at least one does and the claim of never is refuted")


def _shares(table):
    rows = _rows(table)
    shares = {}
    for r in rows:
        shares[r[SERVICE]] = cg.num(r[SHARE])
    for lab in (SHIPPING, INSURANCE, FINANCE, WAREHOUSE, GROWING):
        assert lab in shares, f"row {lab!r} missing from the table"
    for lab, v in shares.items():
        # A share outside 0 to 100 is not a share. This is the bound that catches a
        # corrupted number: the control turns 88 into 275, which is still a
        # "majority" and would slip past a bare threshold test.
        assert 0 <= v <= 100, f"{lab} is {v:g} percent, which is not a share"
    return shares


def q17(table, item):
    s = _shares(table)
    majority = [k for k, v in s.items() if v > 50]
    assert set(majority) == set(MOVING), \
        f"the majority shares must be exactly the three moving services; got {majority}"
    assert s[GROWING] < 5, f"growing and harvesting is {s[GROWING]:g} percent, not almost none"
    assert s[WAREHOUSE] < 50, "warehousing must not be a majority share"
    assert len(set(s.values())) > 1, "'divided evenly' must be false"
    assert max(s.values()) < 100, "'supplied every service in full' must be false"
    assert majority, "'no service held a majority' must be false"
    return (f"shipping {s[SHIPPING]:g}, insurance {s[INSURANCE]:g} and finance "
            f"{s[FINANCE]:g} are majorities while growing stands at {s[GROWING]:g}")


def q18(table, item):
    s = _shares(table)
    lowest_moving = min(s[k] for k in MOVING)
    assert lowest_moving > s[WAREHOUSE] and lowest_moving > s[GROWING], \
        "the three organizing services must all outrank warehousing and growing"
    assert all(s[k] > 50 for k in MOVING), "the three organizing services must be majorities"
    assert s[WAREHOUSE] <= 50, \
        "the rejected option calls warehousing a majority, which must be false"
    assert s[GROWING] == min(s.values()), "growing must be the smallest share in the table"
    return (f"the three organizing services stand at {s[SHIPPING]:g}, {s[INSURANCE]:g} "
            f"and {s[FINANCE]:g}, all above warehousing at {s[WAREHOUSE]:g}")


TABLE_CHECKS = {13: q13, 14: q14, 15: q15, 16: q16, 17: q17, 18: q18}

CLAIMS = [
 ("businesses based within those states",
  "KC-5.2.I.E names TWO practitioners in one sentence: industrialized states AND businesses within those states. Every option confining the practice to one of them, or moving it to the governments of producing territories or to abolished chartered companies, contradicts that sentence."),
 ("Asia and Latin America",
  "KC-5.2.I.E states that economic imperialism was practiced primarily in Asia and Latin America. The word primarily is the framework's own; Africa, Australia, Europe, North America and the Pacific islands are not the regions that sentence names."),
 ("distinct economic advantage for merchants and companies based in Europe and the United States",
  "KC-5.1.II.C, near verbatim: trade in some commodities was organized in a way that gave merchants and companies based in Europe and the U.S. a distinct economic advantage. The reversal, an advantage to the producing regions, is offered as a distractor, so the anchor carries both the advantage and whose it was."),
 ("produced in the Middle East or South Asia and exported to China",
  "The CED prints opium produced in the Middle East or South Asia and exported to China among the commodities that contributed to European and American economic advantage under KC-5.1.II.C. The direction is the whole content of the example and the reversal is a distractor, so the anchor carries both clauses."),
 ("grown in South Asia and Egypt and exported to Great Britain",
  "The CED prints cotton grown in South Asia and Egypt and exported to Great Britain and other European countries under the same heading. The reversed direction would describe the opposite trade and is offered as a distractor, so the anchor carries origin and destination together."),
 ("Palm oil",
  "The CED prints palm oil produced in sub-Saharan Africa and exported to European countries among the commodities that contributed to European and American economic advantage. Opium moves to China, copper is extracted in Chile, South Asian cotton leaves South Asia for Europe, and manufactured cloth is on no list in this topic."),
 ("Chile",
  "The CED prints copper extracted in Chile among the commodities that contributed to European and American economic advantage under KC-5.1.II.C. Egypt and South Asia appear in the cotton example, China as the destination of opium, and West Africa in topic 6.4's palm oil example, not in the copper one."),
 ("industrialized states practicing economic imperialism",
  "The CED prints Britain and France expanding their influence in China through the Opium Wars under its own heading for industrialized states practicing economic imperialism, which is the statement of KC-5.2.I.E. Settler colonies, new states on peripheries, religiously influenced rebellions and labour migration belong to other statements in this unit. The item asks only which heading the example sits under, never what happened in the wars."),
 ("businesses within an industrialized state practicing economic imperialism in Latin America",
  "The CED prints the construction of the Port of Buenos Aires with the support of British firms under the same heading, and KC-5.2.I.E names businesses within industrialized states alongside the states themselves and places the practice primarily in Asia and Latin America. Firms supporting a port are neither annexation, nor an enclave, nor a colonial transfer."),
 ("businesses of an industrialized state obtaining a lasting economic position",
  "This key rests on the logic of the example rather than on a sentence about a real loan: KC-5.2.I.E names businesses within industrialized states as practitioners of economic imperialism and KC-5.1.II.C describes an organization of trade giving such firms a distinct advantage. A financed, operated and revenue-sharing railway is an economic position of that kind, and the reversal, a producing country gaining the advantage, is offered as a distractor."),
 ("How the trade was arranged, and not only what was traded",
  "KC-5.1.II.C attributes the distinct advantage of European and American merchants and companies to the way trade in some commodities was ORGANIZED. That locates the advantage in the arrangements rather than in the goods, and assigns it to those merchants rather than to the producing regions or to a treaty among them."),
 ("the regional claim belongs to the statement about economic imperialism, while the palm oil example belongs to a separate statement",
  "KC-5.2.I.E places economic imperialism primarily in Asia and Latin America; KC-5.1.II.C is a different statement, and the palm oil example is printed under it. Reading one statement's region into the other is the error the item names, and the anchor carries both halves because the whole point is keeping the two statements apart."),
 ("Four of the five shipments",
  "Recomputed in q13 above: the arranging firm is based in Western Europe in Records 1, 3 and 4 and in North America in Record 2, which is four of five, and every rejected count is checked to be false. That concentration is what KC-5.1.II.C means by an advantage held by merchants and companies based in Europe and the U.S."),
 ("Record 4",
  "Recomputed in q14 above: Record 4 is the ONLY row whose region of production is Western Europe, while Records 1, 3 and 5 have Western Europe as their destination. The uniqueness is asserted against the record rather than assumed, and the item asks nothing the record does not contain."),
 ("Record 5",
  "Recomputed in q15 above, and this is the item the missing verifier let ship broken. TWO rows have the arranging firm based in the region of production, Record 4 and Record 5, so the stem carries a second condition -- produced outside Europe and North America -- and q15 asserts that exactly one row satisfies both."),
 ("at least one shipment is arranged by a firm based in the region that produced the good",
  "Recomputed in q16 above: two of the five rows have the arranging firm based in the region of production, so at least one does and the student's claim of never is refuted from the data the student is using. The four rejected statements are true of the record but leave that claim standing, and KC-5.1.II.C asserts an advantage rather than a monopoly."),
 ("supplied most of the services that moved the crop, but almost none of the labour that grew it",
  "Recomputed in q17 above: shipping 88, insurance 91 and finance 84 are the table's only majority shares, warehousing stands at 35 and growing and harvesting at 2. The exact reversal is offered as a distractor, so the anchor carries both clauses, and an even division, a complete monopoly and an absence of majorities are each false on the same numbers."),
 ("high shares held in shipping, insurance and finance",
  "Recomputed in q18 above: the three organizing services all exceed 50 percent and all outrank warehousing and growing. KC-5.1.II.C locates the advantage in the way trade was ORGANIZED, and these are the organizing services; the growing share reports production, warehousing at 35 is not a majority at all, and a row count and a unit carry no claim."),
 ("how the venture was presented to the people being asked to invest in it",
  "This key rests on the logic of evidence, not on a framework assertion about any real firm. A circular issued to shareholders is written to attract and reassure capital, so it is direct evidence of the case made to investors; profits, local opinion, wages and shipping volumes are matters it is not written to report."),
 ("the same commodity could be traded on different terms, and the terms decided who gained",
  "KC-5.1.II.C grounds the distinct economic advantage in how trade in some commodities WAS ORGANIZED, which is a claim about terms rather than about goods. The listed commodities were produced outside Europe and the United States, so no option making them European manufactures or worthless to their producers can be right."),
 ("one through control of territory and one through economic position",
  "KC-5.2.I.A to KC-5.2.I.D describe shifts in control over territory while KC-5.2.I.E describes economic imperialism practiced by industrialized states and businesses within them. Both sit under KC-5.2, that as states industrialized they expanded existing overseas empires and established new colonies and transoceanic relationships, so they are two forms of extended reach rather than one process."),
 ("The naming of businesses within industrialized states alongside the states themselves",
  "KC-5.2.I.E reads that industrialized states AND businesses within those states practiced economic imperialism, so the phrase naming businesses is what refutes a governments-only reading. The regions, the organization of trade, the commodity list and the unit's placement are all true of the framework and say nothing about who practiced it."),
 ("a firm based abroad occupying a position in the organization of a trade",
  "KC-5.1.II.C attributes the advantage of European and American merchants and companies to the way trade in some commodities was organized, and the credit on which an export trade depends is part of that organization. The account describes no annexation, no migration, no settlement and no extraction."),
 ("practiced primarily in Asia and Latin America, and the commodities that gave European and American merchants an advantage came from several regions including Africa",
  "KC-5.2.I.E places economic imperialism primarily in Asia and Latin America; the CED's commodity list under KC-5.1.II.C runs from the Middle East and South Asia to Egypt, sub-Saharan Africa and Chile. The anchor carries both clauses because the item exists to keep the regional claim and the commodity list apart."),
 ("The terms on which a commodity trade was financed and shipped",
  "Unit 6 learning objective E asks how various economic factors contributed to the development of the global economy from 1750 to 1900, and KC-5.1.II.C makes the organization of a trade the source of a distinct economic advantage. Beliefs, national rank, staffing levels and boundary dates belong to the cultural and governance statements of this unit rather than its economic ones."),
 ("how the returns from one trade were divided between those who moved it and those who produced it",
  "This key rests on the logic of evidence. Freight and insurance accounts and a growers' petition report the two ends of one trade, which is what makes reading them together informative about the division of the returns, and KC-5.1.II.C is a claim about exactly that division. Priority of composition, forgery, population and religion are not questions either document is fitted to answer."),
 ("securing favourable terms of trade for merchants of the second state",
  "KC-5.1.II.C attributes the advantage of European and American merchants and companies to the way trade was organized, and terms of admission and a capped duty are terms of trade. The clause transfers no territory, creates no colony, ends no trade and moves no workers, so no other option describes it."),
 ("it is industrialized states and their businesses that the framework names as practicing it",
  "KC-5.2.I.E names industrialized states and businesses within those states as the practitioners, which is what places the statement in a unit on the consequences of industrialization. KC-5.1.II.A in the same unit has the raw material trade growing rather than ending, and the framework nowhere makes industrialization a consequence of economic imperialism."),
 ("Which regions the framework identifies as its principal setting can be answered; how much profit any single firm made cannot",
  "KC-5.2.I.E names the practitioners and places the practice primarily in Asia and Latin America, so those are answerable from the framework; profits, treaty terms and starting dates appear nowhere in this topic, whose examples are printed as illustrations without figures. The anchor carries both clauses because the exact reversal is offered."),
 ("Industrialized states and their businesses extended their economic position abroad, and the way particular trades were organized left the gains concentrated in Europe and the United States",
  "KC-5.2.I.E gives the practitioners and the principal regions and KC-5.1.II.C gives the distinct economic advantage held by merchants and companies based in Europe and the U.S. The anchor carries both clauses because the swapped version, with producing regions in both roles, is offered as a distractor."),
]


# --------------------------------------------------------- legal-value controls
#
# es_check's cell control corrupts a cell by appending " CORRUPTED", which trips
# the exact-vocabulary validation in _ships or the 0-to-100 bound in _shares
# BEFORE any uniqueness guard runs. Those twenty-of-twenty lines therefore prove
# that the tables are read; they prove nothing about the guards that make each
# keyed row the ONLY defensible answer, which is the property whose absence
# shipped item 15 with two correct choices.
#
# So each guard gets its own control that substitutes one LEGAL region or share
# for another. The record stays well formed, the vocabulary check passes, and the
# only thing that changes is whether the key is still unique. Each control also
# asserts on the MESSAGE, because a control that fires for the wrong reason
# proves nothing about the guard it names.

_MADE, _SENT, _FIRM = 1, 2, 3


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


def uniqueness_control():
    ships, adv = w6_5._T_SHIPMENTS, w6_5._T_ADVANTAGE

    # The original defect, reproduced exactly: give Record 4 a second row's worth
    # of Latin American production so TWO rows satisfy both of item 15's
    # conditions. This is the mutation the missing verifier would have had to
    # catch, and it is legal in every other respect.
    def two_answers(rows):
        rows[3][_MADE] = "Latin America"
        rows[3][_FIRM] = "Latin America"
    _fires(ships, two_answers, q15, "exactly one row may satisfy BOTH conditions",
           "item 15 with two defensible answers")

    _fires(ships, lambda rows: rows[0].__setitem__(_MADE, "Western Europe"), q14,
           "exactly one row must be produced in Western Europe",
           "item 14 with a second European producer")

    def no_local_firm(rows):
        rows[3][_FIRM] = "North America"
        rows[4][_FIRM] = "Western Europe"
    _fires(ships, no_local_firm, q16, "the key says at least one such shipment exists",
           "item 16 with no locally arranged shipment")

    _fires(ships, lambda rows: rows[4].__setitem__(_FIRM, "Western Europe"), q13,
           "not four", "item 13 with a fifth European firm")

    # Shares: 60 and 40 are legal percentages, so the 0-to-100 bound cannot fire
    # and the guard under test is the only thing that can.
    _fires(adv, lambda rows: rows[3].__setitem__(1, "60"), q17,
           "majority shares must be exactly the three moving services",
           "item 17 with warehousing raised to a majority")
    _fires(adv, lambda rows: rows[4].__setitem__(1, "40"), q18,
           "growing must be the smallest share",
           "item 18 with growing raised above warehousing")

    # POSITIVE control: the same six checks must ACCEPT the module's own tables,
    # so a check that rejected everything would be caught here rather than
    # counted as six successes.
    for fn in (q13, q14, q15, q16):
        fn(ships, None)
    for fn in (q17, q18):
        fn(adv, None)
    print("  control OK  every uniqueness guard fires on a legal-value mutation, "
          "for the reason it names, and passes the real tables")


if "--selftest" in sys.argv:
    uniqueness_control()

es.run(w6_5, CLAIMS, TABLE_CHECKS, sys.argv)
