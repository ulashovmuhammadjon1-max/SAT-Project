"""Key audit for AP COMPARATIVE GOVERNMENT 5.3 Challenges from Globalization.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states what the key rests on.

WHAT THE KEYS REST ON
---------------------
Learning objective IEF-3.C, two essential knowledge statements:

  IEF-3.C.1  many aspects of globalization CAN CHALLENGE REGIME SOVEREIGNTY:
             .a FDI and MNCs FROM ORIGINATING REGIMES challenge a government's
                FOUNDATIONAL ECONOMIC AND POLITICAL IDEAS AND PRINCIPLES
             .b CULTURAL INFLUENCES accompanying investment and trade can provoke
                a DOMESTIC BACKLASH
             .c INCREASED ECONOMIC DEVELOPMENT can cause ENVIRONMENTAL
                DEGRADATION AND ACCOMPANYING HEALTH ISSUES THAT ALIENATE CITIZENS
             .d FOREIGN GOVERNMENTS bring PRESSURES -- TREATY REVERSALS, PUBLIC
                CONDEMNATION AT INTERGOVERNMENTAL ORGANIZATIONS, ECONOMIC
                SANCTIONS -- on countries whose ACTIONS OFFEND THEM
  IEF-3.C.2  governments STRIVE TO RESPOND TO INTERNAL DEMANDS FOR DOMESTIC
             REFORM; they ALSO WORK TO CONTROL DOMESTIC POLICY DEBATES and EXTEND
             INFLUENCE REGIONALLY TO DEFLECT CRITICISM and improve economic
             conditions

ONLY ONE OF THE FOUR CHALLENGES COMES FROM ABROAD. That is the reading this
module is built to test. IEF-3.C.1.d names foreign governments; IEF-3.C.1.b's
backlash is the country's own public; IEF-3.C.1.c's alienation is its own
citizens; IEF-3.C.1.a's challenge falls on the government's own commitments, not
on its territory. A student who hears "challenge to sovereignty" as "pressure
from abroad" misplaces three of the four. Items 10, 11, 12, 17, 20 and 29 key
that, and item 29's table check confirms exactly one case in the table has an
external actor, so the item cannot have two answers.

IEF-3.C.1.c IS A THREE-STEP CHAIN INSIDE ONE SENTENCE: development causes
degradation, degradation brings health issues, health issues alienate citizens.
The environment table has one column for each step plus the output that starts
it, which is why item 24's check requires all four to move rather than sampling
one -- a table where only output and admissions rose would leave the key half
true.

IEF-3.C.2 IS TWO CLAIMS, NOT ONE SOFTENED. Responding to internal demands for
reform grants something; controlling the debate and extending regional influence
to DEFLECT criticism does not. Items 8, 9 and 18 keep them apart, and item 18's
key states the difference rather than restating either half.

NOTHING HERE TURNS ON CURRENT EVENTS. No sanction, treaty, dispute or condition
of any actual country is asserted anywhere in the module; the framework's three
instruments are named as instruments and the pressure table's country is
unnamed. Every table figure is HYPOTHETICAL and labelled so.

DATA ITEMS
----------
Items 21-23 read the pressure table, 24-26 the environment table, 27-29 the case
table. Item 21's check confirms the table's three rows ARE the framework's three
instruments, so the comparison cannot drift outside the statement it tests. Every
arithmetic distractor is verified to be a wrong operation on the same table.

FIVE choices per item (A-E); see AP_COMP_GOV_CED.md.
"""
import cg_check as cg
import k5_3

USES = "Times used against one country in a decade (hypothetical)"
OUTPUT = "Index of industrial output (first year = 100)"
AIR = "Days on which air quality was rated unhealthy"
ADMIT = "Hospital admissions for respiratory illness per 100,000 residents"
BLAME = "Residents saying the government is not protecting their health (percent)"


def q21(table, item):
    rows = [r.lower() for r in cg.labels(table)]
    assert rows == ["treaty reversal",
                    "public condemnation at an intergovernmental organization",
                    "economic sanctions"], \
        f"the rows must be the framework's three instruments; they read {rows}"
    v = {lab: cg.cell(table, lab, USES) for lab in cg.labels(table)}
    top = max(v, key=v.get)
    assert top == "Public condemnation at an intergovernmental organization", f"the most used instrument is {top}"
    assert v[top] == 19, f"the keyed count reads {v[top]}"
    assert v["Economic sanctions"] == 11 and v["Treaty reversal"] == 4, \
        "each rejected option must state its own row's true count"
    assert len(set(v.values())) == 3, "'all three equally often' must be false"
    return f"the three counts are {[v[l] for l in v]}, and each option states the true count for a different instrument"


def q22(table, item):
    c = cg.col(table, USES)
    total = sum(c)
    assert total == 34, f"the keyed total recomputes to {total}"
    assert total - min(c) == 30, "the 30 distractor must be the total with the smallest row omitted"
    assert max(c) + min(c) == 23, "the 23 distractor must be the largest and smallest rows added"
    assert max(c) == 19, "the 19 distractor must be the largest single row"
    assert sorted(c)[1] == 11, "the 11 distractor must be the middle row"
    return f"the usage column reads {c} and sums to {total:.0f}, with every distractor a wrong sum of the same column"


def q23(table, item):
    c = cg.col(table, USES)
    diff = max(c) - min(c)
    assert diff == 15, f"the keyed difference recomputes to {diff}"
    pairs = {abs(a - b) for a in c for b in c if a != b}
    assert 8 in pairs and 7 in pairs, f"the 8 and 7 distractors must be the other gaps in that column; gaps are {sorted(pairs)}"
    assert max(c) == 19 and min(c) == 4, f"the 19 and 4 distractors must be the extreme rows; the column reads {c}"
    return f"the usage column reads {c}, so the largest minus the smallest is {diff:.0f}"


def q24(table, item):
    cols = {h: cg.col(table, h) for h in (OUTPUT, AIR, ADMIT, BLAME)}
    for h, c in cols.items():
        assert c == sorted(c), f"the column {h!r} must rise across the three years; it reads {c}"
        assert len(set(c)) == 3, f"the column {h!r} must change in every year, or 'none changed' is defensible"
    assert cols[OUTPUT][0] == 100, "the output index must be based at 100 in the first year"
    assert cols[BLAME][-1] > cols[BLAME][0], \
        "residents' views must worsen, so 'their views improved' is false"
    return "all four columns rise together: " + "; ".join(
        f"{h.split(' ')[0].lower()} {c}" for h, c in cols.items())


def q25(table, item):
    a = cg.col(table, AIR)
    rise = a[2] - a[0]
    assert rise == 78, f"the keyed increase recomputes to {rise}"
    assert a[2] - a[1] == 43, "the 43 distractor must be the increase between the second and third years"
    assert a[1] - a[0] == 35, "the 35 distractor must be the increase between the first and second years"
    assert a[2] == 119, "the 119 distractor must be the third year's own figure"
    assert a[0] + a[2] == 160, "the 160 distractor must be the first and third years added instead of subtracted"
    return f"the unhealthy-air column reads {a}, so the rise from the first year to the third is {rise:.0f} days"


def q26(table, item):
    b, o = cg.col(table, BLAME), cg.col(table, OUTPUT)
    rise = b[2] - b[0]
    assert rise == 36, f"the keyed rise recomputes to {rise}"
    assert b[2] - b[1] == 19, "the 19 distractor must be the rise between the second and third years"
    assert b[1] - b[0] == 17, "the 17 distractor must be the rise between the first and second years"
    assert b[2] == 58, "the 58 distractor must be the final share read as a rise"
    assert o[2] - o[0] == 87, "the 87 distractor must be the change in the output index"
    return f"the complaint column reads {b}, so it rises {rise:.0f} percentage points across the period"


def _cases(table):
    return {str(r[0]): str(r[1]).lower() for r in table["rows"]}


def q27(table, item):
    v = _cases(table)
    assert "stated economic and political principles" in v["Case 1"], f"the keyed case reads {v['Case 1']!r}"
    others = [k for k in v if k != "Case 1" and "principles" in v[k]]
    assert not others, f"no other case may turn on the government's stated principles; also {others}"
    assert "foreign-owned firm" in v["Case 1"], "the keyed case must name a foreign-owned firm as the source"
    return "one case alone sets a foreign-owned firm's terms against the government's own stated principles"


def q28(table, item):
    v = _cases(table)
    assert "foreign customs" in v["Case 2"], f"the keyed case reads {v['Case 2']!r}"
    others = [k for k in v if k != "Case 2" and "customs" in v[k]]
    assert not others, f"no other case may involve a campaign against foreign customs; also {others}"
    assert "trade" in v["Case 2"], "the keyed case must tie the campaign to the arrival of trade, as the framework does"
    return "one case alone reports a public campaign against foreign customs following a trade opening"


def q29(table, item):
    v = _cases(table)
    external = [k for k in v if "other governments" in v[k]]
    assert external == ["Case 4"], f"exactly one case may have another state as its actor; these do: {external}"
    for word in ("treaty", "condemned", "sanctions"):
        assert word in v["Case 4"], f"the keyed case must carry the framework's instrument {word!r}"
    for k in ("Case 1", "Case 2", "Case 3"):
        assert "other governments" not in v[k], f"{k} must place its actor inside the country"
    return "one case alone names other governments as the actor, and it carries all three of the framework's instruments"


CLAIMS = [
 ("regime sovereignty",
  "EK IEF-3.C.1 opens by stating that many aspects of globalization can challenge regime sovereignty, and the four items it then lists are the ways that challenge arrives."),
 ("foundational economic and political ideas and principles",
  "EK IEF-3.C.1.a states that foreign direct investment and multinational corporations from originating regimes can pose a challenge to a government's foundational economic and political ideas and principles, so what is challenged is the regime's own commitments rather than its borders."),
 ("a domestic backlash",
  "EK IEF-3.C.1.b states that cultural influences, often Western, that accompany investment and trade with a given regime can provoke a domestic backlash, which locates the reaction inside the country."),
 ("environmental degradation and accompanying health issues",
  "EK IEF-3.C.1.c states that increased economic development can cause environmental degradation and accompanying health issues that alienate citizens, which makes the alienation a consequence of a country's own growth."),
 ("foreign governments",
  "EK IEF-3.C.1.d states that foreign governments can bring political and economic pressures to bear on countries whose actions offend them, and it is the only one of the four challenges whose actor is another state."),
 ("treaty reversals, public condemnation at intergovernmental organizations, and economic sanctions",
  "EK IEF-3.C.1.d names treaty reversals, public condemnation at intergovernmental organizations like the United Nations, and economic sanctions as the political and economic pressures foreign governments can bring to bear."),
 ("actions that offend them, including human rights violations",
  "EK IEF-3.C.1.d states that these pressures fall on countries whose actions, including human rights violations, offend the governments applying them, so the trigger is conduct another state finds objectionable."),
 ("respond to internal demands for domestic reform",
  "EK IEF-3.C.2 states that in response to global market forces governments frequently strive to respond to internal demands for domestic reform, which places the demand inside the country and the response with the government."),
 ("extend their influence regionally to deflect criticism",
  "EK IEF-3.C.2 adds that governments also work to control domestic policy debates and attempt to extend their influence regionally to deflect criticism and improve economic conditions, which is a different response from answering the demands."),
 ("the pressures applied by foreign governments",
  "EK IEF-3.C.1.d names foreign governments as its actor, while EK IEF-3.C.1.b's backlash comes from the country's own public, EK IEF-3.C.1.c's alienation from its own citizens, and EK IEF-3.C.1.a's challenge falls on the government's own commitments."),
 ("the backlash provoked by the cultural influences",
  "EK IEF-3.C.1.b states that cultural influences accompanying investment and trade can provoke a domestic backlash, and the word domestic places that reaction among the country's own people rather than abroad."),
 ("caused by increased economic development",
  "EK IEF-3.C.1.c states that increased economic development can cause environmental degradation and accompanying health issues that alienate citizens, so the chain begins with the country's own growth rather than with anything done to it."),
 ("posing a challenge to a government's foundational economic and political ideas",
  "EK IEF-3.C.1.a states that foreign direct investment and multinational corporations from originating regimes can pose a challenge to a government's foundational economic and political ideas and principles, which a condition of investment requiring the abandonment of such a commitment is."),
 ("cultural influences accompanying investment and trade provoking a domestic backlash",
  "EK IEF-3.C.1.b states that cultural influences, often Western, that accompany investment and trade with a given regime can provoke a domestic backlash, and a public campaign in defense of traditional practices after a trade opening is that backlash."),
 ("health issues that alienate citizens",
  "EK IEF-3.C.1.c states that increased economic development can cause environmental degradation and accompanying health issues that alienate citizens, and the scenario runs through development, degradation, illness and alienation in turn."),
 ("countries whose actions offend them",
  "EK IEF-3.C.1.d names treaty reversals, public condemnation at intergovernmental organizations like the United Nations, and economic sanctions as pressures foreign governments bring to bear on countries whose actions, including human rights violations, offend them."),
 ("narrows what a government can decide for itself within its own territory",
  "The learning objective for EK IEF-3.C is to explain how globalization creates challenges to regime sovereignty, and each of the four items constrains what a government can settle on its own, which is why the framework groups them under that heading rather than calling them mere difficulties."),
 ("turns attention elsewhere without granting it",
  "EK IEF-3.C.2 states the two responses separately, first striving to respond to internal demands for domestic reform and then working to control domestic policy debates and extend influence regionally to deflect criticism, so deflecting and answering are different acts."),
 ("managing domestic political debate and extending influence beyond the country's borders",
  "EK IEF-3.B.3.c and EK IEF-3.B.3.d name controlling domestic political debates to maintain or increase power and extending national influence regionally and internationally, and EK IEF-3.C.2 names controlling domestic policy debates and extending influence regionally to deflect criticism."),
 ("neither of which depends on a state being weak",
  "EK IEF-3.C.1.b locates a backlash among a country's own public and EK IEF-3.C.1.c locates alienation among its own citizens as a consequence of development, so two of the four challenges arise from within a country and follow from its own growth."),
 ("public condemnation at an intergovernmental organization, 19 times",
  "EK IEF-3.C.1.d names treaty reversals, public condemnation at intergovernmental organizations like the United Nations, and economic sanctions. Recomputed in q21 above, which also confirms the table's three rows are exactly those instruments and that each option states its own row truly."),
 ("34",
  "Recomputed in q22 above by summing the usage column across the three instruments. The distractors are the total with the smallest row omitted, the largest and smallest rows added, the largest single row, and the middle row."),
 ("15",
  "Recomputed in q23 above by subtracting the smallest row from the largest. The distractors are the other two gaps within the same column and the two extreme rows read as though they were differences."),
 ("all rose with it",
  "EK IEF-3.C.1.c states that increased economic development can cause environmental degradation and accompanying health issues that alienate citizens. Recomputed in q24 above, where each of the four columns is tested separately, since the key asserts that all of them move."),
 ("78",
  "Recomputed in q25 above by subtracting the first year's figure from the third year's. The distractors are the increases across the other pairs of years, the third year's own figure, and the first and third years added instead of subtracted."),
 ("36 percentage points",
  "Recomputed in q26 above by subtracting the first year's share from the third year's. The distractors are the rises across the other pairs of years, the final share read as a rise, and the change in the output index read as though it were a share of residents."),
 ("required changes at odds with the government's stated principles",
  "EK IEF-3.C.1.a states that foreign direct investment and multinational corporations from originating regimes can pose a challenge to a government's foundational economic and political ideas and principles. Recomputed in q27 above, where only one case sets a foreign firm's terms against those principles."),
 ("a public campaign against foreign customs",
  "EK IEF-3.C.1.b states that cultural influences accompanying investment and trade can provoke a domestic backlash. Recomputed in q28 above, where only one case reports such a campaign and ties it to the arrival of trade."),
 ("other governments withdrew from a treaty",
  "EK IEF-3.C.1.d is the only one of the four statements whose actor is another state. Recomputed in q29 above, which confirms exactly one case names other governments and that it carries all three of the framework's instruments."),
 ("through investors' terms, a public reacting against cultural change",
  "EK IEF-3.C.1 lists four aspects of globalization that can challenge regime sovereignty, two of them arising inside the country, and EK IEF-3.C.2 gives both responses, striving to answer internal demands for reform and working to control the debate while extending regional influence."),
]

cg.check(k5_3, CLAIMS,
         table_checks={21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29})
