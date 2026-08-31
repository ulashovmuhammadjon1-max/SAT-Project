"""Key audit for AP HUMAN GEOGRAPHY 7.7 Changes as a Result of the World Economy.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective PSO-7.A, suggested skill 4.F, and the LAST
THREE of that objective's essential knowledge statements. The CED splits PSO-7.A
across two topics; PSO-7.A.1 to PSO-7.A.4 belong to 7.6 and nothing here touches
them.

    PSO-7.A.5 Outsourcing and economic restructuring have led to a decline in
              jobs in core regions and an increase in jobs in newly
              industrialized countries.
    PSO-7.A.6 In countries outside the core, the growth of industry has resulted
              in the creation of new manufacturing zones -- including special
              economic zones, free-trade zones, and export-processing zones --
              and the emergence of an international division of labor in which
              developing countries have lower-paying jobs.
    PSO-7.A.7 The contemporary economic landscape has been transformed by
              post-Fordist methods of production, multiplier effects, economies
              of scale, agglomeration, just-in-time delivery, the emergence of
              service sectors, high technology industries, and growth poles.

TEN TERMS ARE NAMED BY THE CED AND DEFINED BY NOBODY. PSO-7.A.7 is a list of
eight things with no definitions attached, PSO-7.A.6 names three zone types the
same way, and outsourcing and economic restructuring are named without being
explained. PSO-7.A requires these changes to be explained, so the module
supplies the discipline's standard sense for each and its header lists every one
of them. Each such item's `why` is worded as an explanation of a term the CED
names, never as a quotation of a sentence the CED does not carry.

TWO CLAUSES ARE KEYED ON DIRECTLY, because dropping either leaves a true-sounding
sentence that is not the framework's:
    PSO-7.A.5 asserts BOTH a decline in core regions and an increase in newly
        industrialized countries -- item 1's distractors are the four ways of
        keeping one half and losing the other, and item 4 asks why the two
        halves are one phenomenon.
    PSO-7.A.6 says an international division of labor IN WHICH DEVELOPING
        COUNTRIES HAVE LOWER-PAYING JOBS -- item 12 keys on the arrangement and
        the wage clause together, since an account of the division alone has
        dropped what the statement actually asserts about it.

TWO COLLISIONS WERE AVAILABLE IN THIS BANK AND BOTH WERE STEERED AROUND:

    ECONOMIES OF SCALE is already defined outright at g5_7 q10 under EK
    PSO-5.C.5, with five further items on the mechanism. A second definition
    item here would have been the tenth cross-topic duplicate of the kind
    COMP_GOV_DEDUPE.md records. Item 20 asks instead what economies of scale do
    to the MAP of production -- fewer and larger plants each serving a wider
    area -- which is the geographic consequence PSO-7.A.7 lists them for, and
    which g5_7 never asks.

    AGGLOMERATION means something else in unit 6. g6_2 uses "urban
    agglomeration" for a continuous built-up area and its population; PSO-7.A.7
    means the clustering of related firms. Item 17 states the industrial sense
    in full and the module never uses the phrase "urban agglomeration", so
    nothing here can be read against the unit 6 definition.

SUGGESTED SKILL 4.F IS ABOUT VISUAL SOURCES, AND THIS BANK CANNOT CARRY ONE.
`geo_check` rejects outright any stem promising a map, a photograph or a
diagram, because CLAUDE.md's rule 3 forbids a prose description standing in for
a figure. Items 25 and 26 therefore ask what a photograph CANNOT show rather
than presenting one, which is the honest form of the skill here: a wage, a
contract and a position in a production chain are not visible properties of a
building, and a picture of a closed plant records an absence without recording
what replaced it. Both items' distractors are checked against the opposite
error -- treating a limitation as a reason to reject visual evidence entirely.

NO REAL COUNTRY, REGION OR FIRM IS NAMED ANYWHERE IN THIS MODULE. The three data
items carry hypothetical records attached to an unnamed core region, an unnamed
newly industrialized country, an unnamed semiperipheral country and an unnamed
plant.

The three table items (27, 28, 29) are the computational gate:

  27  the two job changes are DERIVED from four columns and appear nowhere in
      the table. The core region's TOTAL employment is checked to RISE while its
      manufacturing falls, because that is the whole point of the item and a
      distractor asserts the opposite; a record in which the total also fell
      would let a student reach the key while believing manufacturing decline
      and employment decline are the same thing.
  28  the four shares are checked to add to 100, the two core stages are
      identified from the record's own second column rather than by position,
      and final assembly is checked to hold BOTH the smallest share and the
      lowest pay -- the coincidence the key rests on. The highest-paying stage
      is checked NOT to hold the smallest share, since a distractor says it does.
  29  the three job counts are summed and checked against the region's own
      recorded loss, which must be at least as large. Every other distractor is
      checked directly: the total exceeds the direct count, the region has fewer
      jobs afterwards, and suppliers do not outnumber local services.

ROUNDING. Every returned string is built from the recomputed values and printed
the way a person would state them, with the exact value held by a bound beside
it. verify_g7_4.py had to be repaired for the opposite mistake: it recomputed
3,696 and demanded those digits appear in a choice that correctly said "about
3,700", so it failed a question whose arithmetic was right.

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written. One drafted item was cut: "What are economies of scale?", which is
g5_7 q10 word for word. Its slot became item 20.
"""
import re

import geo_check
import g7_7

for _n, _item in enumerate(g7_7.QUESTIONS, 1):
    assert isinstance(_item.get("ans"), int), f"7.7 q{_n}: `ans` is {_item.get('ans')!r}"
    assert 0 <= _item["ans"] < len(_item["choices"]), f"7.7 q{_n}: ans out of range"


def _num(cell):
    return float(str(cell).replace(",", ""))


def q27_employment_shift(table):
    """Job changes derived; the core region's TOTAL must rise as manufacturing falls."""
    rows = table["rows"]
    assert len(rows) == 2, rows
    assert "core" in rows[0][0].lower(), rows[0][0]
    assert "newly industrialized" in rows[1][0].lower(), rows[1][0]
    mfg = [(_num(r[1]), _num(r[2])) for r in rows]
    svc = [(_num(r[3]), _num(r[4])) for r in rows]
    fall = mfg[0][0] - mfg[0][1]
    rise = mfg[1][1] - mfg[1][0]
    assert fall > 0, mfg[0]
    assert rise > 0, mfg[1]
    # A distractor claims the two are equal; another claims manufacturing fell
    # in both places.
    assert fall != rise, (fall, rise)
    # Distractors on services and on the core region's total.
    assert svc[0][1] > svc[0][0], svc[0]
    assert svc[1][1] > svc[1][0], svc[1]
    core_before = mfg[0][0] + svc[0][0]
    core_after = mfg[0][1] + svc[0][1]
    assert core_after > core_before, (core_before, core_after)
    for exact in (fall, rise):
        assert abs(exact - round(exact)) < 0.5, exact
    return (f"fell by {fall:.0f} thousand in the core region and rose by "
            f"{rise:.0f} thousand")


def q28_value_chain(table):
    """Shares add to 100; the core stages are found from the record's own column."""
    rows = table["rows"]
    stage = [r[0] for r in rows]
    where = [r[1].lower() for r in rows]
    share = [_num(r[2]) for r in rows]
    pay = [_num(r[3]) for r in rows]
    assert sum(share) == 100, share
    core = [i for i, w in enumerate(where) if "core" in w]
    assert len(core) == 2, where
    core_share = sum(share[i] for i in core)
    assembly = [i for i, s in enumerate(stage) if "assembly" in s.lower()]
    assert len(assembly) == 1, stage
    a = assembly[0]
    # The key rests on the smallest share and the lowest pay being the same row.
    assert share[a] == min(share), (share, a)
    assert pay[a] == min(pay), (pay, a)
    # A distractor says the best-paid stage takes the smallest share.
    assert share[pay.index(max(pay))] != min(share), (share, pay)
    # A distractor says the non-core stages take more of the price.
    assert core_share > 100 - core_share, core_share
    # A distractor says the four shares are about a quarter each.
    assert any(abs(s - 25) > 5 for s in share), share
    return (f"capture {core_share:.0f} percent of the final price between them, "
            f"while final assembly captures {share[a]:.0f} percent")


def q29_multiplier(table):
    """Three job counts summed and checked against the region's own loss."""
    vals = {r[0]: _num(r[1]) for r in table["rows"]}
    direct = vals["Jobs directly employed at the plant"]
    suppliers = vals["Jobs at suppliers serving the plant"]
    services = vals[
        "Jobs in local services supported by the wages of the first two groups"]
    before = vals["Jobs in the region before the plant closed"]
    after = vals["Jobs in the region two years after it closed"]
    total = direct + suppliers + services
    # A distractor says the closure cost only the plant's own jobs.
    assert total > direct, (total, direct)
    # A distractor says the region held more jobs afterwards.
    assert after < before, (before, after)
    # A distractor says suppliers outnumber the local services supported.
    assert suppliers < services, (suppliers, services)
    # A distractor says the effect misses local services entirely.
    assert services > 0, services
    # The region's own recorded loss must be at least the associated total, or
    # the key's second clause is not supported by the record.
    assert before - after >= total, (before - after, total)
    return f"{direct:,.0f} direct jobs stand behind {total:,.0f} in total"


CLAIMS = [
 ("A decline in jobs in core regions and an increase in jobs in newly industrialized countries",
  "EK PSO-7.A.5 states that outsourcing and economic restructuring have led to a decline in jobs in core regions and an increase in jobs in newly industrialized countries. Two directions are asserted in one sentence, and reporting either alone turns a redistribution into a disappearance or a windfall."),

 ("Contracting work out to another firm",
  "EK PSO-7.A.5 names outsourcing as one of the two processes behind the shift, and the CED does not define it. What moves is the performance of the work rather than the ownership of the product, which is how the practice shifts employment across a border without moving a sale."),

 ("so employment can rise overall while manufacturing falls",
  "EK PSO-7.A.5 names economic restructuring alongside outsourcing, and EK SPS-7.B.1 says the different economic sectors are characterized by distinct development patterns. Restructuring is a change in the composition of employment, which is why a region can lose manufacturing jobs and still add jobs in total."),

 ("relocated rather than abolished",
  "EK PSO-7.A.5 puts the decline in core regions and the increase in newly industrialized countries in one sentence with one cause. A relocated task is subtracted at one end of the move and added at the other, which is what makes the two halves a single phenomenon."),

 ("grown rapidly and recently, so it now holds work that was previously done in core regions",
  "EK PSO-7.A.5 says jobs have increased in newly industrialized countries, and EK PSO-7.A.6 says the growth of industry outside the core created new manufacturing zones there. The category turns on recent and rapid growth of industry rather than on any absolute level of output."),

 ("outsourcing and economic restructuring have produced a decline in jobs in core regions",
  "EK PSO-7.A.5 names outsourcing specifically, and contracting work to an independent supplier abroad is what the word describes. The rejected claims are real statements of this unit and each concerns a different process, so matching the case to the right statement is the work of the item."),

 ("New manufacturing zones and an international division of labor",
  "EK PSO-7.A.6 states that in countries outside the core the growth of industry has resulted in the creation of new manufacturing zones and the emergence of an international division of labor. Both a place and an arrangement are asserted, and the arrangement is the more consequential of the two."),

 ("Special economic zones, free-trade zones, and export-processing zones",
  "EK PSO-7.A.6 names exactly these three as the new manufacturing zones created by the growth of industry outside the core. The rejected sets mix terms from other statements of this unit and from urban planning, none of which this statement lists."),

 ("where the rules on trade, tax and investment differ",
  "EK PSO-7.A.6 names it among the new manufacturing zones and the CED does not define it. The rules change at a boundary drawn inside one country, which is what makes such a zone a geographic object rather than a policy applying everywhere."),

 ("landed, held, handled and sent onward without the customs charges",
  "EK PSO-7.A.6 names free-trade zones among the manufacturing zones created outside the core, and the CED does not define them. The concession is territorial and attaches to goods passing through rather than entering, which is what separates such a zone from a free trade agreement between states."),

 ("conditional on the output being sent abroad rather than sold in the domestic market",
  "EK PSO-7.A.6 names export-processing zones alongside the other two and the CED does not define them. The condition attached to the concession is what the name records, and it is why such a zone can raise a country's exports without changing what its own buyers can obtain."),

 ("the framework says developing countries have the lower-paying jobs",
  "EK PSO-7.A.6 names the emergence of an international division of labor IN WHICH DEVELOPING COUNTRIES HAVE LOWER-PAYING JOBS. The arrangement and the wage claim sit in one clause, so an account describing the division without the pay difference has dropped what the framework asserts about it."),

 ("a firm gains them by locating there and loses them by locating anywhere else",
  "EK PSO-7.A.6 says the growth of industry outside the core created new manufacturing zones, and a zone is defined by its boundary. A rule that changes at a line makes location itself valuable, which is why such a policy produces a cluster rather than a general increase spread across a country."),

 ("Post-Fordist methods of production, multiplier effects, economies of scale, agglomeration",
  "EK PSO-7.A.7 names exactly these eight as what has transformed the contemporary economic landscape. Each rejected list is a real statement of this unit, drawn from the topics on trade, on theories of development, on sustainability and on economic sectors."),

 ("smaller batches that can be changed",
  "EK PSO-7.A.7 names post-Fordist methods of production first among the eight and the CED does not define them. Flexibility is the defining property, and it is what allows a firm to distribute stages of one product across several places rather than concentrating a long run in one."),

 ("through the suppliers it buys from and the wages its workers spend",
  "EK PSO-7.A.7 names multiplier effects among the eight and the CED does not define them. The effect works through two channels -- purchases from suppliers and wages spent locally -- which is why the employment associated with a plant is always larger than the plant's own payroll."),

 ("shared suppliers, a common pool of skilled labour and the rapid movement of ideas",
  "EK PSO-7.A.7 names agglomeration among the eight, and EK SPS-7.B.2 names the factors influencing where manufacturing locates. The advantage is external to any one firm and belongs to the cluster, which is why the process is self-reinforcing: each arrival makes the place more attractive to the next."),

 ("Components arrive as they are needed for production rather than being held in stock",
  "EK PSO-7.A.7 names just-in-time delivery among the eight and the CED does not define it. The practice replaces a stock of components with a flow of them, removing the cost of holding inventory and putting the reliability of transport in its place."),

 ("draws further activity toward it, so growth spreads outward from that point",
  "EK PSO-7.A.7 names growth poles among the eight and the CED does not define them. The concept is spatial: growth is treated as something that begins somewhere and propagates, which is why a state wanting development in a lagging region may try to establish one there."),

 ("fewer and larger plants, each serving a wider area",
  "EK PSO-7.A.7 names economies of scale among the things that transformed the contemporary economic LANDSCAPE, which is a claim about geography rather than about accounting. If unit cost falls as a plant grows, the cheapest arrangement concentrates output and accepts a longer haul to the customer."),

 ("a delay of hours cannot stop the line",
  "EK PSO-7.A.7 names just-in-time delivery among the eight things transforming the economic landscape, and its spatial consequence is why it belongs on that list. Removing the stock removes the cushion, so the plant's tolerance for a transport failure falls to nearly nothing and proximity becomes worth paying for."),

 ("its wages supported employment in local services",
  "EK PSO-7.A.7 names multiplier effects among the eight, and a multiplier runs in both directions. The two channels that add employment when a plant opens are the same two that subtract it when the plant closes, which is why the regional loss exceeds the payroll."),

 ("the work which grew as manufacturing employment fell was of a different kind",
  "EK PSO-7.A.7 names the emergence of service sectors and high technology industries among the eight, and EK PSO-7.A.5 records the decline of jobs in core regions. Read together they describe a change of composition, which is the economic restructuring the earlier statement names."),

 ("allows the stages of one product to be separated and placed wherever each stage is cheapest",
  "EK PSO-7.A.7 names post-Fordist methods of production and EK PSO-7.A.6 names the emergence of an international division of labor. A production method that can be broken into changeable segments is what makes the geographic separation of those segments practical, so the two statements describe one change from two sides."),

 ("not the wages paid, the terms of employment, or where this stage sits in a chain",
  "Suggested skill 4.F asks students to explain possible limitations of visual sources provided. EK PSO-7.A.6 makes a claim about pay and about position in a division of labour, and neither is a visible property of a building, so the source cannot reach the claim."),

 ("record an absence and not what replaced it",
  "Suggested skill 4.F asks for the possible limitations of visual sources, and EK PSO-7.A.5 names outsourcing AND economic restructuring together. A photographic record is selected from what is visible, and the offices and service employment that grew are neither ruined nor photogenic, so the set can be accurate and still one-sided."),

 ("fell by 280 thousand in the core region and rose by 450 thousand",
  "Recomputed from the record: manufacturing falls from 820 to 540 thousand in one place and rises from 310 to 760 thousand in the other, while services rise in both, so the core region's total moves from 2,720 to 3,020 thousand. EK PSO-7.A.5 names a decline in core regions and an increase in newly industrialized countries, and EK PSO-7.A.7 names the emergence of service sectors, which is why the total can rise while manufacturing falls.",
  ),

 ("capture 69 percent of the final price between them, while final assembly captures 9 percent",
  "Recomputed from the record: the four shares add to 100, the two stages carried out in the core hold 31 and 38 of them, and final assembly holds the smallest share at the lowest hourly pay in the chain. EK PSO-7.A.6 names an international division of labor IN WHICH DEVELOPING COUNTRIES HAVE LOWER-PAYING JOBS, and a chain whose value and whose pay concentrate at the same end is what that clause describes.",
  ),

 ("1,200 direct jobs stand behind 3,600 in total",
  "Recomputed from the record: 1,200 direct jobs, 900 at suppliers and 1,500 in local services total 3,600, and the region's employment falls from 48,000 to 44,100, a loss of 3,900. EK PSO-7.A.7 names multiplier effects among the things that transformed the contemporary economic landscape, and the same two channels that add employment subtract it when the plant goes.",
  ),

 ("eight named processes transformed the economic landscape as a whole",
  "EK PSO-7.A.5 supplies the two directions of the job shift, EK PSO-7.A.6 the zones and the division of labour with its wage clause, and EK PSO-7.A.7 the eight processes. Each rejected summary either turns a redistribution into a disappearance, drops the clause about lower-paying jobs, reduces a list of eight to one, or reverses the direction of the shift."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"7.7 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"7.7 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

# The exporter does not typeset this subject, so hand-written LaTeX would ship
# as literal backslashes, and a range written with a hyphen between two digits
# reads as a minus sign to any converter ever pointed at the bank. Explicit
# lookarounds, never \b -- a digit and a letter are both word characters.
DIGIT_RANGE = re.compile(r"[0-9]\s*[-/]\s*[0-9]")
for n, item in enumerate(g7_7.QUESTIONS, 1):
    strings = [item["q"], item["why"], *item["choices"]]
    tbl = item.get("table")
    if tbl:
        strings += list(tbl["headers"]) + [c for row in tbl["rows"] for c in row]
    for s in strings:
        assert "\\(" not in s and "\\[" not in s and "$" not in s, (
            f"7.7 q{n}: math delimiter in a prose subject: {s!r}")
        m = DIGIT_RANGE.search(s)
        assert not m, f"7.7 q{n}: digit range {m.group(0)!r} in {s!r}"

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    27: q27_employment_shift,
    28: q28_value_chain,
    29: q29_multiplier,
}

geo_check.check(g7_7, ANCHORS, TABLE_NOTES)
