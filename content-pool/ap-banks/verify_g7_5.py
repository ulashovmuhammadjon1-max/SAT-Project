"""Key audit for AP HUMAN GEOGRAPHY 7.5 Theories of Development.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective SPS-7.E, suggested skill 1.E, and ONE
essential knowledge statement:

    SPS-7.E.1 Different theories, such as Rostow's Stages of Economic Growth,
              Wallerstein's World System Theory, dependency theory, and
              commodity dependence, help explain spatial variations
              in development.

plus, where an item leans on them, four sentences the CED writes elsewhere:

    the unit 7 overview, page 121 -- the theories "are in turn useful in
        explaining spatial variations in development such as core-periphery
        relationships"
    SPS-7.A.3 -- investors in industry sought out more raw materials and new
        markets, a factor that contributed to the rise of colonialism and
        imperialism   (this is the CED sentence behind item 23)
    SPS-7.B.2 -- core, semiperiphery and periphery locations
    PSO-5.E.2 -- some countries have become highly dependent on one or more
        export commodities
    the unit 7 sample activity, page 123 -- students compare the four theories
        and discuss "how different countries are classified according to the
        different theories", which is the CED licensing items 9 and 17

ONE EK STATEMENT NAMES FOUR THEORIES AND DESCRIBES NONE OF THEM. That is the
whole authoring problem for this topic. SPS-7.E says "explain different theories
of economic and social development", so the theories' content is required and
the CED does not print it; the module supplies the discipline's standard account
and says so in its own header, exactly as g7_2 did for least cost theory. Every
definition item's `why` is therefore worded as an explanation of the model the
CED names, never as a quotation of a sentence the CED does not contain.

WHAT THIS MODULE REFUSES TO ASSERT: that any one of the four theories is
correct, that the framework prefers one, or that the framework ranks them.
SPS-7.E.1's verb is HELP EXPLAIN and item 30 keys on that hedge specifically,
with a distractor for each way of losing it -- one theory instead of four,
identical predictions, or nothing explained at all.

THE REPEAT THAT WAS AVAILABLE AND WAS NOT TAKEN. g7_2 q23 and g6_2 q7 both
already ask what core, semiperiphery and periphery refer to, and both key on
"positions in the world economy". Asking it a third time was the obvious opening
item for a world-systems block and would have been the tenth cross-topic
duplicate of the kind COMP_GOV_DEDUPE.md records. Items 13 to 18 ask instead
what each tier is CHARACTERIZED BY, what the theory takes as its unit of
analysis, and whether a position is permanent -- none of which either sibling
asks. Likewise g5_9 already covers commodity dependence from the agricultural
side, including its price risk, so items 25 and 26 ask what makes it an
explanation OF DEVELOPMENT and what it predicts that a stage model does not.

SKILL 1.E IS THIS TOPIC'S SUGGESTED SKILL and it asks for weaknesses and
limitations. Items 11, 12, 19 and 24 supply one limitation per theory, and each
is a limit on the theory's REACH rather than a claim that it is false. That is a
deliberate constraint on the distractors too: every rejected "criticism" in
those four items is an over-strong one (the theory denies trade, denies
industrialization, explains nothing), because the failure mode in a limitations
question is a student who learns that naming a model's weakness means rejecting
the model.

NO REAL COUNTRY IS NAMED ANYWHERE IN THIS MODULE. The three data items carry
hypothetical records attached to unnamed economies and unnamed groups.

The three table items (27, 28, 29) are the computational gate:

  27  the concentration share is DERIVED from the two money columns rather than
      read off, and each economy's loss is checked to be about a third of its
      own share -- the key's claim is that the loss tracks concentration and not
      the size of the export trade, so the totals are also checked NOT to order
      the losses. Two distractors are checked against directly: that some
      economy exceeds half its earnings from one commodity, and that the
      smallest share is not the largest fall.
  28  every row checked to add to 100, and the economy with the SMALLEST primary
      share checked to be the same one with the LARGEST tertiary share, because
      the key rests on the two measures agreeing. The largest secondary share is
      checked to sit elsewhere, since a distractor points at it.
  29  the two flows checked equal in value, each row's two shares checked to add
      to 100, and the compositions checked to be reversed between the rows.

ROUNDING. Every returned string is built from the recomputed values and rounded
the way a person would state them, with the exact value held by a bound beside
it. verify_g7_4.py had to be repaired for the opposite mistake -- it recomputed
3,696 and demanded those digits appear in a choice that correctly said "about
3,700", so it failed a question whose arithmetic was right. A containment check
must ask for the number the choice would print, not the number the division
produced.

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written. One item was cut and replaced during that pass: a draft item asked why
dependence on a single export commodity is risky for an economy, which is g5_9
q4 asked again in different words with the same key. It was replaced by item 26,
which asks what commodity dependence predicts that a stage model does not -- an
ask that only exists in this topic, because only this topic has both theories in
front of it.
"""
import re

import geo_check
import g7_5

for _n, _item in enumerate(g7_5.QUESTIONS, 1):
    assert isinstance(_item.get("ans"), int), f"7.5 q{_n}: `ans` is {_item.get('ans')!r}"
    assert 0 <= _item["ans"] < len(_item["choices"]), f"7.5 q{_n}: ans out of range"


def _num(cell):
    return float(str(cell).replace(",", ""))


def q27_commodity_concentration(table):
    """Concentration share derived from the money columns; loss tracks share."""
    largest = [_num(r[1]) for r in table["rows"]]
    total = [_num(r[2]) for r in table["rows"]]
    fall = [_num(r[3]) for r in table["rows"]]
    share = [a / b * 100 for a, b in zip(largest, total)]
    # The shares are the point of the item and none of them is printed in the
    # table -- a student has to divide. Check the division, then the claim.
    assert [round(s) for s in share] == [80, 20, 50, 10], share
    for s, f in zip(share, fall):
        assert abs(f - s / 3) <= 1, (s, f)
    # A distractor says none exceeds half; another says the smallest share takes
    # the largest fall. Both must be false of this record.
    assert max(share) > 50, share
    assert share.index(min(share)) != fall.index(max(fall)), (share, fall)
    # A distractor says the totals are identical; and the key says the loss
    # tracks concentration RATHER THAN the size of the export trade, so the
    # totals must not order the losses either.
    assert len(set(total)) > 1, total
    assert sorted(range(4), key=lambda i: total[i]) != sorted(
        range(4), key=lambda i: fall[i]), (total, fall)
    hi, lo = round(max(share)), round(min(share))
    assert abs(max(share) - hi) < 0.5 and abs(min(share) - lo) < 0.5, share
    return f"runs from {hi} percent down to {lo} percent"


def q28_sectoral_shares(table):
    """Rows add to 100; smallest primary share is also the largest tertiary."""
    primary = [_num(r[1]) for r in table["rows"]]
    secondary = [_num(r[2]) for r in table["rows"]]
    tertiary = [_num(r[3]) for r in table["rows"]]
    for r, row in enumerate(table["rows"]):
        assert _num(row[1]) + _num(row[2]) + _num(row[3]) == 100, row
    # The key rests on the two measures agreeing on the same economy.
    i = primary.index(min(primary))
    assert i == tertiary.index(max(tertiary)), (primary, tertiary)
    assert i == 3, i
    # A distractor points at the largest secondary share; it must be elsewhere.
    assert secondary.index(max(secondary)) != i, secondary
    return (f"only {primary[i]:.0f} percent of employment remains in the "
            f"primary sector and {tertiary[i]:.0f} percent is in services")


def q29_trade_composition(table):
    """Flows equal in value, shares add to 100, compositions reversed."""
    value = [_num(r[1]) for r in table["rows"]]
    raw = [_num(r[2]) for r in table["rows"]]
    made = [_num(r[3]) for r in table["rows"]]
    assert len(table["rows"]) == 2, table["rows"]
    assert value[0] == value[1], value
    for a, b in zip(raw, made):
        assert a + b == 100, (a, b)
    # Opposite composition, not merely different: each flow's majority is the
    # other flow's minority.
    assert raw[0] > made[0] and made[1] > raw[1], (raw, made)
    assert raw[0] > 80 and made[1] > 90, (raw, made)
    return (f"equal in value but opposite in composition, with {raw[0]:.0f} "
            "percent")


CLAIMS = [
 ("help explain spatial variations in development",
  "EK SPS-7.E.1 states that different theories help explain spatial variations in development. The verb is HELP EXPLAIN, which credits the theories with illuminating a pattern rather than with dictating policy or forecasting a date."),

 ("commodity dependence",
  "EK SPS-7.E.1 names Rostow's Stages of Economic Growth, Wallerstein's World System Theory, dependency theory and commodity dependence as its four examples. The rejected lists are real bodies of theory drawn from other units, which is what makes the distinction worth drawing."),

 ("a sequence of stages that an economy is held to pass through in order",
  "The CED names the model without stating it and learning objective SPS-7.E requires it to be explained. Its defining feature is the ordered sequence, which is what puts it in opposition to the three relational theories listed beside it."),

 ("subsistence agriculture, technology is limited",
  "Learning objective SPS-7.E asks students to explain the theories the CED names. The first stage is defined by the absence of the surplus later investment requires, and the four rejected descriptions are the model's other four stages, so the item can only be answered by knowing the sequence rather than by elimination."),

 ("creating the conditions industry will need before industry itself grows",
  "Learning objective SPS-7.E asks for an explanation of Rostow's Stages of Economic Growth. This stage is defined by investment in what is not itself industry -- roads, ports, credit, farms selling into markets -- and the ordering is the model's claim, since industry cannot grow without them already there."),

 ("cities draw in labour, and growth begins to sustain itself",
  "Learning objective SPS-7.E asks for the model to be explained. Take-off is narrow rather than general: growth starts in a few sectors and stops depending on an outside push, which is the stage's content and also the part of the model most often disputed."),

 ("spreads beyond the first leading sectors",
  "Learning objective SPS-7.E asks for an explanation of the model. The difference between the fourth stage and the third is breadth rather than speed, which is why the model treats maturity as the point at which growth no longer rests on any single industry."),

 ("manufactured consumer goods are widely owned across the population",
  "Learning objective SPS-7.E asks for the model to be explained, and EK SPS-7.B.1 supplies the vocabulary of sectors the last stage is described in. The stage is named for consumption because it is defined by what households can buy as much as by what the economy makes."),

 ("preconditions for take-off",
  "The unit 7 sample activity asks students to discuss how countries are classified according to the different theories. Infrastructure and commercial agriculture are in place while industry is not, and that combination is the second stage rather than the first or the third."),

 ("the accumulation and investment of capital in leading sectors",
  "Learning objective SPS-7.E asks students to explain different theories, and the theories differ most in where they place the cause. A stage model is internalist, explaining a country's position by what that country has done, which is the assumption dependency theory attacks directly."),

 ("cannot account for the effect one country's development has on another's",
  "Suggested skill 1.E asks for the weaknesses and limitations of a theory in a specified context. EK SPS-7.A.3 records that industrial investors sought raw materials and new markets abroad, which is exactly one country's development acting on another's, and a model of independent national paths has nowhere to put it."),

 ("generalized from the histories of a small number of countries that industrialized early",
  "Suggested skill 1.E asks for the limitations of a model in a specified context. A generalization holds only over the range it was drawn from, and a country industrializing now faces a world already containing industrialized competitors, which the early cases did not."),

 ("a single world economy, within which countries occupy positions",
  "EK SPS-7.E.1 names the theory and learning objective SPS-7.E requires it to be explained. Choosing the unit of analysis is the theory's first and largest move: if the world economy is one system, a country's development is a fact about its position rather than about the country alone."),

 ("the largest share of the profits from world trade",
  "EK SPS-7.B.2 names core, semiperiphery and periphery locations, and the unit 7 overview says these theories explain spatial variations such as core-periphery relationships. The core is defined by the kind of production it holds, which is why skill, capital and the share of the returns are named together."),

 ("turned into higher-value products elsewhere",
  "EK SPS-7.B.2 names periphery locations among those the manufacturing factors influence. The definition turns on where in a chain of production the work sits rather than on how much work there is, which is how a peripheral economy can be busy and still capture little of the value."),

 ("both draws value from the periphery and supplies lower-value production to the core",
  "EK SPS-7.B.2 names the semiperiphery alongside the other two, and a three-part division rather than a two-part one is a substantive claim. A tier exploited on one side and exploiting on the other has interests pulling both ways, which is what the theory means by a stabilizing middle."),

 ("stands above the suppliers it buys from and below the economies that design what it assembles",
  "The unit 7 sample activity asks students to discuss how countries are classified according to the different theories. Exporting manufactures is not a core characteristic when the design and the patents sit elsewhere, and buying materials from poorer suppliers is not a peripheral one, so the case is defined by holding both relations at once."),

 ("the three-tier structure itself persists",
  "Learning objective SPS-7.E asks for the theories to be explained, and this is the distinction students most often lose. The claim is about the structure rather than about any occupant of it, in the way that mobility between income groups does not abolish the groups."),

 ("placing a particular country is a matter of judgement rather than of calculation",
  "Suggested skill 1.E asks for the limitations of a theory in a specified context. EK SPS-7.C.1 and EK SPS-7.C.3 supply measured indicators such as gross national income per capita and the Human Development Index, and a category with no agreed threshold cannot be applied the way a measured index can."),

 ("produced and maintained by their relationship with wealthier ones",
  "EK SPS-7.E.1 names dependency theory among the theories that help explain spatial variations in development. Its explanation is relational: the connections that make one place rich are what keep another poor, so poverty is an outcome of a link rather than a starting condition."),

 ("an early point on a path everyone travels or a position created by its links with rich countries",
  "EK SPS-7.E.1 names both theories and the unit 7 sample activity asks students to compare and contrast them. The disagreement is about the cause rather than about the facts: both accept that countries differ, and they differ over whether the difference is a stage or a relation."),

 ("the stages that add most of the value, and the profits from them, remain in the wealthier countries",
  "EK SPS-7.E.1 names dependency theory, and EK PSO-5.E.1 places products in a global supply chain in which value is added at successive stages. If the later stages happen abroad the earnings from them accrue abroad, which is the mechanism the theory points at rather than any prohibition."),

 ("treats the trading relationships formed then as the source of present inequality",
  "EK SPS-7.A.3 states that investors in industry sought out more raw materials and new markets, a factor that contributed to the rise of colonialism and imperialism. That sentence describes the formation of the very material-for-manufactures relationship dependency theory takes as its subject."),

 ("moved from supplying materials to exporting manufactures",
  "Suggested skill 1.E asks for the limitations of a theory in a specified context. A theory built to explain why a condition persists is under most strain from the cases in which it did not persist, and saying so is what distinguishes a limitation from a rejection."),

 ("ties the whole economy's income to prices set outside it",
  "EK PSO-5.E.2 records that some countries have become highly dependent on one or more export commodities, and EK SPS-7.E.1 lists commodity dependence among the theories that help explain spatial variations in development. Concentration is what turns an export pattern into an explanation, because it makes one external price a fact about the entire economy."),

 ("still not build the diversified industry a stage model treats as the next step",
  "EK SPS-7.E.1 names both commodity dependence and Rostow's Stages of Economic Growth, and the two read the same evidence differently. A stage model takes high earnings as progress along the path; commodity dependence takes them as a fact about one price that need not broaden the economy at all."),

 ("runs from 80 percent down to 10 percent",
  "Recomputed from the record: dividing the largest commodity's earnings by total earnings gives shares of 80, 20, 50 and 10 percent, and the losses of 27, 7, 17 and 3 percent are each about a third of the economy's own share, while total earnings of 4,500, 4,500, 5,400 and 4,800 do not order the losses. EK SPS-7.E.1 names commodity dependence as a theory helping explain spatial variations in development, and concentration rather than size is what the record shows doing the work.",
  ),

 ("only 4 percent of employment remains in the primary sector",
  "Recomputed from the record: every row adds to 100, and the economy with the smallest primary share is also the one with the largest tertiary share, so the two measures agree on which is furthest along. EK SPS-7.B.1 says the sectors are characterized by distinct development patterns, and Rostow's final stage is defined by services dominating employment.",
  ),

 ("equal in value but opposite in composition",
  "Recomputed from the record: both flows are 1,800 million currency units, each row's two shares add to 100, and the compositions are reversed between them. The unit 7 overview says these theories explain spatial variations in development such as core-periphery relationships, and a balanced value of trade carrying an unbalanced composition is what such a relationship looks like in data.",
  ),

 ("help explain spatial variations in development rather than that any one of them is the settled answer",
  "EK SPS-7.E.1 says that DIFFERENT theories, such as the four it lists, HELP EXPLAIN spatial variations in development. Both hedges carry weight: the plural means the framework is not choosing between them, and the verb means each is a partial aid to explanation rather than a proven law."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"7.5 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"7.5 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

# The CED does not typeset this subject, and the brief forbids hand-written
# LaTeX and ranges written with a hyphen between two digits (they read as a
# minus sign once a converter is ever pointed at the bank). Explicit
# lookarounds, never \b -- a digit and a letter are both word characters.
DIGIT_RANGE = re.compile(r"[0-9]\s*[-/]\s*[0-9]")
for n, item in enumerate(g7_5.QUESTIONS, 1):
    strings = [item["q"], item["why"], *item["choices"]]
    tbl = item.get("table")
    if tbl:
        strings += list(tbl["headers"]) + [c for row in tbl["rows"] for c in row]
    for s in strings:
        assert "\\(" not in s and "\\[" not in s and "$" not in s, (
            f"7.5 q{n}: math delimiter in a prose subject: {s!r}")
        m = DIGIT_RANGE.search(s)
        assert not m, f"7.5 q{n}: digit range {m.group(0)!r} in {s!r}"

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    27: q27_commodity_concentration,
    28: q28_sectoral_shares,
    29: q29_trade_composition,
}

geo_check.check(g7_5, ANCHORS, TABLE_NOTES)
