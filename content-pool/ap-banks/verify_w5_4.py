"""Key audit for AP WORLD HISTORY: MODERN 5.4 Industrialization Spreads in the
Period from 1750 to 1900.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim cites the Key Concept or Learning
Objective the key traces to.

WHAT THE KEYS REST ON
---------------------
Two statements, and every key traces to one of them:

  KC-5.1.II.B  the rapid development of steam-powered industrial production in
               European countries and the U.S. contributed to the increase in
               these regions' SHARE of global manufacturing during the first
               Industrial Revolution; while Middle Eastern and Asian countries
               CONTINUED to produce manufactured goods, these regions' share in
               global manufacturing declined.
  KC-5.1.I.D   as new methods of industrial production became more common in
               parts of northwestern Europe, they spread to other parts of
               Europe and the United States, Russia, and Japan.

Items 6, 7, 8 and 17 key to the illustrative examples printed beside
KC-5.1.II.B: shipbuilding in India and Southeast Asia, iron works in India,
textile production in India and Egypt.

THE DISTINCTION THIS TOPIC TURNS ON
-----------------------------------
A SHARE is a proportion of a total; production can rise while a share falls, and
KC-5.1.II.B says both things in one sentence. The easiest wrong key in the unit
reads the falling share as a collapse in production, so items 1, 5, 10, 11, 12,
14, 19 and 26 are built on that difference, and the table in item 5 shows a
region whose output index rises while its share falls -- recomputed below from
the figures alone, together with every distractor.

WHAT THEY DELIBERATELY DO NOT REST ON
-------------------------------------
The framework assigns no cause to the Middle Eastern and Asian decline beyond the
rise of steam-powered production elsewhere, and item 29 keys that silence rather
than filling it. Nothing here dates a country's industrialization, ranks the
places in KC-5.1.I.D, or borrows the Meiji reforms from KC-5.2.II.A, which is
topic 5.6. The table figures are hypothetical and the stems say so.

SWAP ANCHORS
------------
Items 1, 11, 16 and 25 carry a distractor that is the key with its clauses
exchanged: production and share exchanged, continuity and change exchanged,
origin and destination of the spread exchanged, and cause and effect exchanged.
Every one of those anchors carries BOTH clauses -- the defect found in
verify_e2_1.py -- and the key-rotation control below requires all thirty keys to
fail when moved one place.

FIVE choices per item (A-E); see HISTORY_BRIEF.md.
"""
import sys

import cg_check as cg
import wh_check as wh
import w5_4

OUT_EARLY = "Manufacturing output, earlier year (index)"
OUT_LATE = "Manufacturing output, later year (index)"
SH_EARLY = "Share of global manufacturing, earlier year (percent)"
SH_LATE = "Share of global manufacturing, later year (percent)"


def q5(table, item):
    """A rising output with a falling share, and every rival reading refuted."""
    labels = cg.labels(table)
    out_early = dict(zip(labels, cg.col(table, OUT_EARLY)))
    out_late = dict(zip(labels, cg.col(table, OUT_LATE)))
    sh_early = dict(zip(labels, cg.col(table, SH_EARLY)))
    sh_late = dict(zip(labels, cg.col(table, SH_LATE)))
    for year, shares in (("earlier", sh_early), ("later", sh_late)):
        assert abs(sum(shares.values()) - 100) < 0.5, (
            f"the {year} shares must account for the whole of global manufacturing; "
            f"they sum to {sum(shares.values())}"
        )
    both = [lab for lab in labels
            if out_late[lab] > out_early[lab] and sh_late[lab] < sh_early[lab]]
    assert both, "the key requires at least one region whose output rises while its share falls"
    # 'every region whose share falls also produces less' must be false
    fell = [lab for lab in labels if sh_late[lab] < sh_early[lab]]
    assert any(out_late[lab] > out_early[lab] for lab in fell), \
        "'every region whose share falls produces less' must be false"
    assert fell, "'every region's share rises' must be false"
    top_late = max(labels, key=lambda lab: sh_late[lab])
    top_early = max(labels, key=lambda lab: sh_early[lab])
    assert top_late != top_early, \
        "'the largest later share had the largest earlier share' must be false"
    assert any(out_late[lab] != out_early[lab] for lab in labels), \
        "'no region's output changes' must be false"
    # Pin the shape of BOTH output columns, not just one comparison. Without this
    # the control caught 1 corrupted cell in 15: a share cell written as "35%"
    # survived corruption because the appended text left the number intact, and a
    # single output cell could be tripled without disturbing any inequality above.
    assert (out_late["Region A"] > out_late["Region C"] > out_late["Region B"]), (
        f"the later output column must run A above C above B; got {out_late}"
    )
    assert (out_early["Region B"] > out_early["Region A"] > out_early["Region C"]), (
        f"the earlier output column must run B above A above C; got {out_early}"
    )
    assert sh_late["Region A"] > sh_late["Region C"] > sh_late["Region B"], (
        f"the later share column must run A above C above B; got {sh_late}"
    )
    assert sh_early["Region B"] > sh_early["Region A"] > sh_early["Region C"], (
        f"the earlier share column must run B above A above C; got {sh_early}"
    )
    return (f"recomputed from the table: {both} raise output while losing share, the shares "
            f"sum to one hundred in each year, and the largest share passes from {top_early} "
            f"to {top_late}")


def q8(table, item):
    """The framework's own pairing of illustrative industry with location."""
    pairs = {str(row[0]): str(row[1]) for row in table["rows"]}
    egypt = [ind for ind, loc in pairs.items() if "egypt" in loc.lower()]
    assert egypt == ["Textile production"], (
        f"exactly one industry must be named beside Egypt, and it must be textiles; got {egypt}"
    )
    assert "southeast asia" in pairs["Shipbuilding"].lower(), \
        "shipbuilding must be named in India and Southeast Asia"
    assert pairs["Iron works"].strip() == "India", \
        "iron works must be named in India alone"
    return ("read from the table alone: Egypt appears beside textile production and beside no "
            "other industry, while shipbuilding carries Southeast Asia and iron works India")


CLAIMS = [
 ("continued to produce manufactured goods while their share of global manufacturing declined",
  "KC-5.1.II.B states both halves in one sentence: while Middle Eastern and Asian countries continued to produce manufactured goods, these regions' share in global manufacturing declined. The anchor carries both clauses because a distractor exchanges the rising and falling terms."),
 ("steam-powered industrial production",
  "KC-5.1.II.B names the cause explicitly: the rapid development of steam-powered industrial production in European countries and the U.S. contributed to the increase in these regions' share. Chemicals and precision machinery belong to KC-5.1.I.E instead."),
 ("parts of northwestern Europe",
  "KC-5.1.I.D opens with new methods of industrial production becoming more common in parts of northwestern Europe. Russia and Japan appear in the same sentence as places the methods spread TO, which is why neither can be the starting point."),
 ("Russia, and Japan",
  "KC-5.1.I.D names the destinations exactly: other parts of Europe and the United States, Russia, and Japan. The rejected lists name regions the framework places under KC-5.1.V.B, KC-5.1.II.B or KC-5.3.II.iii."),
 ("output rises between the two years while its share of global manufacturing falls",
  "KC-5.1.II.B describes precisely this combination, and q5 above recomputes it from the table: one region's output index rises while its share falls, the shares sum to one hundred in each year, and every rival reading is checked false on the same figures."),
 ("Shipbuilding",
  "The illustrative examples printed beside KC-5.1.II.B name shipbuilding in India and Southeast Asia. Steel and precision machinery belong to KC-5.1.I.E and railways to KC-5.1.IV, so none of the rejected options is on this list."),
 ("Iron works",
  "The illustrative examples printed beside KC-5.1.II.B name iron works in India alongside shipbuilding and textile production. Chemicals and electrical equipment are second industrial revolution products under KC-5.1.I.E."),
 ("Textile production",
  "The illustrative examples printed beside KC-5.1.II.B name textile production in India and Egypt, and q8 above checks the table reproduces that pairing: Egypt stands beside textiles and beside nothing else."),
 ("first Industrial Revolution",
  "KC-5.1.II.B places the increase in the European and United States share during the first Industrial Revolution. KC-5.1.I.E names a second industrial revolution separately, and the other options are periods the framework treats in other units."),
 ("continued to produce manufactured goods even as their share of the global total declined",
  "KC-5.1.II.B's word is CONTINUED: while Middle Eastern and Asian countries continued to produce manufactured goods, these regions' share in global manufacturing declined. A reading of collapse discards the framework's own verb."),
 ("Continuity in the production of manufactured goods, change in the share of the global total",
  "KC-5.1.II.B supplies one of each: production continued, the share declined. The reasoning process assigned to this topic is continuity and change, and the anchor carries both halves because a distractor exchanges which one moved."),
 ("production continued in these regions while their share of global manufacturing declined",
  "KC-5.1.II.B pairs continued production with a declining share, and the illustrative examples printed beside it name shipbuilding in India and Southeast Asia among those cases. A yard still launching ships with a smaller fraction of the world's tonnage is that pairing in one scene."),
 ("how the way it was organized changed",
  "Unit 5 Learning Objective E asks students to explain how different modes and locations of production have developed and changed over time. The rejected questions belong to the objectives behind KC-5.3.I.A, KC-5.3.II.ii, KC-5.3.I.C and KC-5.1.VI.C."),
 ("Global manufacturing as a whole grew faster than the region that lost share",
  "A share is a proportion of a total, which is what lets KC-5.1.II.B report continued production alongside a declining share. A region growing more slowly than the world total loses share without producing less."),
 ("became common in one part of Europe and then spread to further regions",
  "KC-5.1.I.D describes a sequence rather than a simultaneous appearance: as new methods became more common in parts of northwestern Europe, they spread to other parts of Europe and the United States, Russia, and Japan. Suggested skill 5.A is identifying that connection."),
 ("The methods became common in northwestern Europe and spread from there to Russia and Japan",
  "KC-5.1.I.D runs in one direction only, and the anchor carries both the origin and the destinations because the distractor exchanges them. The student's version reverses the sentence the framework prints."),
 ("Textile production in India and Egypt",
  "The illustrative examples printed beside KC-5.1.II.B name textile production in India and Egypt among the cases of a declining Middle Eastern and Asian share. The rejected options name other entries on that list or developments under KC-5.1.I.E and KC-5.1.IV."),
 ("spreading from northwestern Europe to the United States, Russia, and Japan",
  "KC-5.1.II.B names steam-powered industrial production in European countries and the U.S., and KC-5.1.I.D names the spread of new methods from parts of northwestern Europe to other parts of Europe and the United States, Russia, and Japan. Each rejected pair inverts one of those sentences."),
 ("continued to produce manufactured goods while their share declined",
  "KC-5.1.II.B holds continued production and a falling share together, so the inference from a halved share to closed works is exactly what that sentence rules out. The rejected options are true framework statements that bear on other questions."),
 ("European countries and the United States",
  "KC-5.1.II.B attributes the increase in share to European countries and the U.S., where steam-powered industrial production developed rapidly, and places the Middle East and Asia on the declining side of the same sentence."),
 ("spread outward over time rather than appearing everywhere at once",
  "KC-5.1.I.D describes methods becoming more common in parts of northwestern Europe and then spreading to other parts of Europe and the United States, Russia, and Japan. A spread of that kind takes time, which is what a later date of adoption records."),
 ("includes places in Europe, in North America and in Asia",
  "KC-5.1.I.D names other parts of Europe, the United States, Russia and Japan in one sentence, which spans those three areas. Each rejected option shrinks or misdescribes the list the framework prints."),
 ("different modes of production existed alongside one another",
  "KC-5.1.I.D has methods spreading gradually from parts of northwestern Europe while KC-5.1.II.B has Middle Eastern and Asian countries still producing manufactured goods throughout. Unit 5 Learning Objective E asks about modes and locations of production, and coexistence is what a spread in progress looks like."),
 ("set beside the world total for the same years",
  "KC-5.1.II.B distinguishes continued production from a declining share, and only a region's own output measured against the world total separates the two. The rejected options leave the absolute and the relative readings equally open."),
 ("steam-powered production contributed to a rising share",
  "KC-5.1.II.B puts the technology on the causal side: the rapid development of steam-powered industrial production contributed to the increase in these regions' share. The anchor carries both cause and effect because a distractor reverses them."),
 ("rest of the world's manufacturing grew far faster",
  "This is the arithmetic KC-5.1.II.B rests on when it reports continued production alongside a declining share: a share falls when the denominator grows faster than the numerator, with no error and no fall in output required."),
 ("named both among the regions whose share rose and among the places new methods spread to",
  "KC-5.1.II.B places the U.S. with European countries among the regions whose share increased, and KC-5.1.I.D names the United States among the places new methods spread to. Both sentences name it, in different roles."),
 ("the share of global manufacturing tended to rise, and where they did not, it tended to fall",
  "KC-5.1.I.D names the places new methods reached and KC-5.1.II.B names the regions whose share rose and fell, and the two lists line up. Suggested skill 5.A for this topic is identifying exactly this connection between developments."),
 ("reports the decline without assigning it a cause in this statement",
  "KC-5.1.II.B records continued production and a declining share and stops; the only cause it names is the rapid development of steam-powered production elsewhere. Supplying a further cause from outside the CED is what HISTORY_BRIEF.md forbids, so the limitation is the answer."),
 ("raising some regions' share of global manufacturing while others kept producing with a smaller share",
  "The summary joins KC-5.1.I.D's outward spread from parts of northwestern Europe with KC-5.1.II.B's rising and falling shares and its statement that production continued. Each rejected option contradicts one of those two sentences."),
]

TABLE_CHECKS = {5: q5, 8: q8}

wh.run(w5_4, CLAIMS, TABLE_CHECKS, sys.argv)
