"""Key audit for AP WORLD HISTORY: MODERN 6.4 Global Economic Development from 1750 to 1900.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is ``cg_check.check``; the notation gate and the negative
control are ``es_check``, reused unchanged, because World History is a prose
subject that ``export_units.py`` does not typeset, exactly as ENV_SCI is.

WHAT THE KEYS REST ON
---------------------
This topic prints one historical development, and nearly every item traces to a
clause of it:

    KC-5.1.II.A  The need for raw materials for factories and increased food
                 supplies for the growing population in urban centers led to the
                 growth of export economies around the world that specialized in
                 commercial extraction of natural resources and the production of
                 food and industrial crops. The profits from these raw materials
                 were used to purchase finished goods.

Items 1, 20, 22 rest on the two named needs. Items 2, 4, 21, 24 rest on the two
named specializations. Items 3, 14, 30 rest on the closing sentence about the
profits, whose DIRECTION is the whole content of items 3 and 30, so both anchors
carry two clauses and the exact reversal is a distractor in each.

Items 5, 6, 7 sort three of the CED's printed illustrative examples into the
framework's own two categories. The CED prints the categories and the examples
separately and does not pair them itself, so each why states the ground for the
sorting: meat is eaten, diamonds are dug rather than grown, guano is extracted.
No item asks what any example produced, when, in what quantity or for whom.

Items 8 and 28 rest on the Humans and the Environments thematic focus, that the
environment shapes human societies and that growing and changing populations in
turn shape their environments, together with learning objective D. Items 18 and
19 rest on the CED's naming of continuity and change as this topic's reasoning
process. Items 15, 16, 17 and 26 rest on suggested skill 2.B, explaining how a
source's point of view, purpose, historical situation and audience affect its
interpretation; their keys rest on the logic of evidence rather than on a claim
about what happened, and the claims below say so rather than citing a key
concept they do not follow from.

Items 23, 25, 27 and 29 are reasoning items about what the framework's statements
do and do not settle. Item 27 asserts only that this topic and the state
expansion topic are separate strands of one period, which the CED's own unit
layout gives.

DATA ITEMS: 9 to 14 carry tables whose values are hypothetical and labelled so in
the stem. Each keyed conclusion is recomputed below from that table alone, and
each check also falsifies the distractors. The port register's two categorical
columns are checked against an exact vocabulary rather than by substring, so a
corrupted cell fails instead of still reading as its original category.

NEGATIVE CONTROL: ``python3 verify_w6_4.py --selftest`` rotates every key off its
anchor, corrupts every table cell in turn, injects each banned notation form (and
one legal string that must pass), duplicates a choice, thins a why and makes a
why name an option by letter, and requires every one of those to raise.
"""
import sys

import cg_check as cg
import es_check as es
import w6_4

EXPORT = "Leading export by value"
IMPORT = "Leading import by value"
SHARE = "Share of the economy's export earnings (hypothetical, percent)"
FIBRE = "Raw fibre exported (thousands of bales)"
CLOTH = "Finished cloth imported (thousands of bolts)"

UNPROCESSED = {"Unprocessed fibre", "Crude mineral ore", "Chilled meat", "Raw gum and latex"}
FINISHED = {"Woven cloth", "Machine tools", "Manufactured hardware", "Finished rubber goods"}

RESOURCE = "A single extracted natural resource"
FOOD = "Foodstuffs"
TEXTILES = "Textiles woven in the territory"
MACHINERY = "Machinery assembled in the territory"
OTHER = "All other goods"


def _rows(table):
    idx = {h: j for j, h in enumerate(table["headers"])}
    return [{h: str(r[j]) for h, j in idx.items()} for r in table["rows"]]


def _ports(table):
    """Rows of the port register, with both goods columns validated by exact match.

    Exact membership, not a substring test: `es_check._corrupt` appends text to a
    cell, and a substring test would still read "Woven cloth CORRUPTED" as a
    finished good. The control would then pass while proving nothing.
    """
    rows = _rows(table)
    for r in rows:
        assert r[EXPORT] in UNPROCESSED, f"unexpected export {r[EXPORT]!r}"
        assert r[IMPORT] in FINISHED, f"unexpected import {r[IMPORT]!r}"
    return rows


def q9(table, item):
    rows = _ports(table)
    assert len(rows) == 4, f"the stem says four port economies; the register holds {len(rows)}"
    assert all(r[EXPORT] in UNPROCESSED and r[IMPORT] in FINISHED for r in rows), \
        "every row must pair an unprocessed export with a finished import"
    assert not any(r[EXPORT] in FINISHED for r in rows), "'exports a finished good' must be false"
    return ("all four rows pair an unprocessed export with a finished import, which is "
            "KC-5.1.II.A's closing sentence set out as a table")


def q10(table, item):
    rows = _ports(table)
    manufactured_exports = [r for r in rows if r[EXPORT] in FINISHED]
    assert not manufactured_exports, \
        "the keyed statement must be FALSE on the register: no row may export a manufactured good"
    assert all(r[EXPORT] in UNPROCESSED for r in rows), "'every export unprocessed' must be true"
    assert all(r[IMPORT] in FINISHED for r in rows), "'every import manufactured' must be true"
    assert len(rows) == 4, "'four separate port economies' must be true"
    assert not any(r[IMPORT] in UNPROCESSED for r in rows), "'no unprocessed import' must be true"
    return ("no row exports a manufactured good, so the keyed claim is unsupported, while each "
            "rejected statement reads directly off the same two columns")


def _shares(table):
    rows = _rows(table)
    shares = {r["Commodity leaving one hypothetical export economy"]: cg.num(r[SHARE])
              for r in rows}
    for lab in (RESOURCE, FOOD, TEXTILES, MACHINERY, OTHER):
        assert lab in shares, f"row {lab!r} missing from the table"
    return shares


def q11(table, item):
    shares = _shares(table)
    top = max(shares, key=shares.get)
    assert top == RESOURCE, f"largest share is {top!r}"
    assert shares[RESOURCE] > sum(v for k, v in shares.items() if k != RESOURCE), \
        "the extracted resource must exceed all other categories combined"
    assert len(set(shares.values())) > 1, "'spread evenly' must be false"
    return (f"a single extracted natural resource takes {shares[RESOURCE]:g} percent of export "
            "earnings, more than the other four categories combined")


def q12(table, item):
    shares = _shares(table)
    total = sum(shares.values())
    made_here = shares[TEXTILES] + shares[MACHINERY]
    assert total == 100, f"the shares sum to {total:g}, not 100"
    assert made_here == total / 10, \
        f"textiles plus machinery is {made_here:g} percent, not one tenth of the total"
    assert made_here < shares[RESOURCE], "the manufactured share must fall below the extracted share"
    return (f"textiles at {shares[TEXTILES]:g} and machinery at {shares[MACHINERY]:g} come to "
            f"{made_here:g} percent, one tenth of the {total:g} percent total")


def q13(table, item):
    rows = _rows(table)
    fib = [cg.num(r[FIBRE]) for r in rows]
    clo = [cg.num(r[CLOTH]) for r in rows]
    assert len(rows) == 4, f"the stem says four decades; the record holds {len(rows)}"
    assert all(b > a for a, b in zip(fib, fib[1:])), f"fibre exports do not rise throughout: {fib}"
    assert all(b > a for a, b in zip(clo, clo[1:])), f"cloth imports do not rise throughout: {clo}"
    assert "exported" in FIBRE and "imported" in CLOTH, \
        "the reversed reading is refuted by the column headings, which must name the direction"
    return f"fibre exports run {fib} and cloth imports run {clo}, so both columns rise at every step"


def q14(table, item):
    rows = _rows(table)
    fib = [cg.num(r[FIBRE]) for r in rows]
    clo = [cg.num(r[CLOTH]) for r in rows]
    assert all(b > a for a, b in zip(fib, fib[1:])) and all(b > a for a, b in zip(clo, clo[1:])), \
        "the key requires both columns to rise together, so neither may fall"
    assert clo[-1] > clo[0] and fib[-1] > fib[0], "both columns must end above where they began"
    return ("raw material sent out and finished goods taken in both rise across the four decades, "
            "so they move together rather than in opposite directions")


TABLE_CHECKS = {9: q9, 10: q10, 11: q11, 12: q12, 13: q13, 14: q14}

CLAIMS = [
 ("raw materials for factories, and the need for increased food supplies",
  "KC-5.1.II.A names exactly two needs behind the growth of export economies: raw materials for factories, and increased food supplies for the growing population in urban centers. Settlement, religious conversion, skilled labour, tax revenue and military bases are not among them."),
 ("commercial extraction of natural resources, and the production of food and industrial crops",
  "KC-5.1.II.A, near verbatim: the export economies that grew specialized in commercial extraction of natural resources and the production of food and industrial crops. Manufacturing, refining, shipbuilding, weaving, banking and insurance are not named as their specializations."),
 ("profits from the raw materials were used to purchase finished goods",
  "KC-5.1.II.A's closing sentence, near verbatim. The reversal is offered as a distractor, so the anchor carries both clauses; the framework asserts nothing about reinvestment, treaty restrictions or barter."),
 ("export economy specializing in an industrial crop",
  "KC-5.1.II.A describes the growth of export economies specializing in the production of food and industrial crops, which is what a district turning from mixed local farming to a single export crop illustrates. Manufacturing, settler colonies, company transfers and rebellions belong to other statements in this unit."),
 ("Meat from Argentina and Uruguay",
  "KC-5.1.II.A names the production of food among these economies' specializations, and of the CED's printed examples meat is the one that is eaten. Diamonds, rubber and guano are extracted and cotton is grown to be spun, so the sorting rests on what each commodity is rather than on a pairing the CED prints."),
 ("Diamonds from Africa",
  "KC-5.1.II.A distinguishes commercial extraction of natural resources from the production of food and industrial crops. Diamonds are dug rather than grown or raised; cotton and palm oil are crops and meat is a food. Milling in an imperial capital is processing and is not among the CED's examples at all."),
 ("commercial extraction of a natural resource for export",
  "KC-5.1.II.A names commercial extraction of natural resources as one of the two specializations, and the CED prints the guano industries in Peru and Chile among its illustrative resource export economies. Finished goods, colonial transfers, new states and migration are treated elsewhere in the unit."),
 ("rested on what particular environments could yield",
  "The Humans and the Environments focus states that the environment shapes human societies and that growing and changing populations in turn shape their environments; learning objective D asks how environmental factors contributed to the global economy. KC-5.1.II.A's economies of extraction and cultivation are that relationship in operation."),
 ("sends out an unprocessed good and takes in a finished one",
  "Recomputed in q9 above: all four rows pair an unprocessed export with a finished import, which is KC-5.1.II.A's closing sentence in tabular form. The reversal is offered as a distractor and is false on the register."),
 ("exports goods it has manufactured itself",
  "Recomputed in q10 above: no row of the register exports a manufactured good, so the keyed claim is the one the data cannot support, while each rejected statement reads directly off the export and import columns."),
 ("depend overwhelmingly on a single extracted natural resource",
  "Recomputed in q11 above: one extracted natural resource accounts for 78 percent of export earnings, more than the other four categories combined. That concentration is what KC-5.1.II.A means in calling these economies specialized."),
 ("Textiles and machinery together account for one tenth",
  "Recomputed in q12 above: textiles at 6 and machinery at 4 are the table's two manufactured categories and come to 10 of the 100 percent total. The food share, the residual category, the row count and the fact that the shares sum to a whole say nothing about manufacturing."),
 ("raw fibre exported and the finished cloth imported rise in every decade",
  "Recomputed in q13 above: fibre exports run 40, 75, 130, 210 and cloth imports run 22, 51, 96, 170, so both rise at every step, and the column headings name which good moves in which direction."),
 ("also took in more finished goods over time",
  "KC-5.1.II.A states that the profits from raw materials were used to purchase finished goods, and q14 above confirms both columns rise together across four decades. Every rejected option asserts an opposing movement the record does not show."),
 ("presented to people whose money was being sought",
  "Suggested skill 2.B asks how a source's purpose and audience bear on its interpretation. A prospectus exists to attract investment, so it is evidence of the case made to investors, not of quantities, wages, local opinion or later prices."),
 ("each is reliable about different things",
  "Suggested skill 2.B makes purpose and audience central to interpretation. A ledger kept as a commercial record and a narrative written to interest readers answer different questions well, which is a reason to use each for what it is good for rather than to declare either false."),
 ("how the trade was experienced by the people producing the goods",
  "Suggested skill 2.B asks how point of view affects interpretation. An official of the importing country writes from the receiving side, so the report is good evidence of what his government valued and poor evidence of the producers' experience, which it does not attempt to record."),
 ("what about the territory's production changed and what carried on unchanged",
  "The CED names continuity and change as the reasoning process for topic 6.4, and that reasoning is the joint identification of what altered and what persisted. It is not a demand for a date, a ranking of territories, or an instruction to attend to half of the pair."),
 ("technique of cultivation persisted while the destination and purpose of the crop changed",
  "The source states unchanged tools and field boundaries alongside a changed crop and a changed destination, so the continuity is in technique and the change is in what is grown and for whom. The anchor carries both clauses because the exact reversal is a distractor; KC-5.1.II.A is the process illustrated."),
 ("food supplies that were increasingly obtained from distant export economies",
  "KC-5.1.II.A names increased food supplies for the growing population in urban centers as one of the two needs that led to the growth of export economies specializing in food production. Emigration, factory finance and governance by consuming cities are not asserted there."),
 ("concentrated on a narrow range of goods sold outside the territory",
  "KC-5.1.II.A speaks of export economies that SPECIALIZED in extraction and in food and industrial crops, and pairs that with profits used to purchase finished goods. Concentration on a narrow range of exports with other goods bought in is what that pairing describes; worker training and the number of trading partners are not mentioned."),
 ("need for raw materials for factories was one of the causes",
  "KC-5.1.II.A opens by naming the need for raw materials for factories as one of the two causes of the growth of export economies, which is a direct connection to industrial production. The statement does not place factories in the exporting territories and says the opposite of the last two options."),
 ("move a bulky export more cheaply",
  "KC-5.1.II.A describes export economies specializing in extraction and in food and industrial crops, and a request for transport from the interior to the coast serves getting such produce out of the territory. The petition asks for no factory, no prohibition, no mission and no new state."),
 ("sold abroad what its environment could yield",
  "KC-5.1.II.A groups commercial extraction with the production of food and industrial crops as these economies' specializations and states that the profits from the raw materials were used to purchase finished goods. Ownership by the importing government, continental restriction and cessation are asserted nowhere in that statement."),
 ("What kinds of production such economies specialized in can be answered; how many tons any one of them shipped cannot",
  "KC-5.1.II.A names the specializations and states what the profits bought, so those questions are answerable; tonnages, wages and starting dates appear nowhere in this topic, whose examples are listed without figures. The anchor carries both clauses because the exact reversal is a distractor."),
 ("conditions in the market where the foodstuff was sold rather than in the territory that produced it",
  "Suggested skill 2.B asks how a source's historical situation bears on interpretation. A newspaper item written in the consuming market reports prices and consumption there; production methods, wages, environment and government in the exporting territory lie outside what it observes."),
 ("while the other describes how state power over territory shifted",
  "KC-5.1.II.A is a statement about export economies and purchases of finished goods, while KC-5.2.I and KC-5.2.II describe shifts in state power. Both are printed in Unit 6, whose span is c. 1750 to c. 1900, so they are separate strands of one period rather than the same claim."),
 ("growing and changing population reshaped the environment",
  "The Humans and the Environments focus states that the environment shapes human societies and that populations, as they grow and change, in turn shape their environments. Clearing land to plant an export crop is the second half of that sentence, and KC-5.1.II.A is the economic process it serves."),
 ("share of the territory's export earnings coming from its largest export, measured at several dates",
  "Specialization is a claim about concentration, so testing it needs a measure of concentration compared across time. A single year's export total, a ship count, a city population and an official headcount measure size or administration instead."),
 ("Industrial and urban demand grew, export economies specialized to meet it",
  "KC-5.1.II.A runs in that order: the two needs LED TO the growth of specialized export economies, and the profits from those raw materials were then used to purchase finished goods. The anchor carries both clauses because the reversal of the first two stages is offered as a distractor."),
]

es.run(w6_4, CLAIMS, TABLE_CHECKS, sys.argv)
