"""Key audit for AP BIOLOGY 4.5 Cell Cycle.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the keyed choice and in no distractor, so the key
survives the shuffle ``export_units.py`` applies on export.

WHAT THE KEYS REST ON
---------------------
Every key traces to an essential knowledge statement of topic 4.5, listed at
the head of ``b4_5.py`` and cited by code in each claim below. The statements
most often misremembered, and therefore the ones the distractors deliberately
offer wrong, are:

  4.5.A.1.iii  DNA replicates in S phase           -- not G1, not G2
  4.5.A.1.iv   CENTROSOMES replicate in G2         -- not S
  4.5.A.1.v    a G0 cell CAN REENTER the cycle     -- the exit is not permanent
  4.5.B.1.vii  CLEAVAGE FURROW in animal cells,
               CELL PLATE in plant cells           -- routinely swapped

BOUNDARY WITH 4.6 AND 5.1. Checkpoints, cyclins, cyclin-dependent kinases and
the consequences of disruption belong to topic 4.6 and carry no key here;
meiosis, homologous pairs and crossing over belong to 5.1 and 5.2.

THE ARITHMETIC ITEMS. The topic's suggested skills are 4.B (describe data from
a table) and 5.A (means, rates, ratios, percentages and percent changes), so
items 16, 17 and 20 ask for a calculation and the keyed value is recomputed
below from the table alone. Items 18 and 19 ask skill 4.B questions of two
further tables.

NO FIGURES. The cell cycle invites a diagram and the bank cannot carry one, so
no stem here refers to a figure; every data item is a table of counts.

FIVE choices per item (A-E), per SCIENCE_BRIEF.md.
"""
import cg_check as cg
import b4_5

PHASES = b4_5._T_PHASES
DNA = b4_5._T_DNA
TISSUE = b4_5._T_TISSUE
GROWTH = b4_5._T_GROWTH

H_COUNT = "Cells counted in a sample of 400 (hypothetical)"
H_DNA = "DNA per cell relative to a cell in G1 (hypothetical)"
H_DIV = "Cells dividing, out of 500 counted"
H_G0 = "Cells in G0, out of 500 counted"
H_START = "Cells present at the start"
H_END = "Cells present after twenty-four hours"

CYCLE_HOURS = 20.0  # stated in the stem of item 17


def _interphase_share(table):
    labs = cg.labels(table)
    counts = dict(zip(labs, cg.col(table, H_COUNT)))
    inter = [k for k in labs if "interphase" in k.lower()]
    assert len(inter) == 1, f"exactly one interphase row is required; got {labs}"
    total = sum(counts.values())
    assert total == 400, f"the stem says a sample of 400; the rows total {total:.0f}"
    return counts, inter[0], total


def q16(table, item):
    counts, inter, total = _interphase_share(table)
    pct = 100 * counts[inter] / total
    assert pct == 75, f"the keyed seventy-five percent recomputes to {pct}"
    for wrong in (50, 25, 12, 100):
        assert pct != wrong, f"the distractor {wrong} percent must be false"
    return (f"{counts[inter]:.0f} interphase cells out of {total:.0f} counted is {pct:.0f} percent, "
            f"and none of the four distractor values equals it")


def q17(table, item):
    counts, inter, total = _interphase_share(table)
    hours = CYCLE_HOURS * counts[inter] / total
    assert hours == 15, f"the keyed fifteen hours recomputes to {hours}"
    for wrong in (10, 5, 2, 20):
        assert hours != wrong, f"the distractor {wrong} hours must be false"
    return (f"{counts[inter]:.0f} of {total:.0f} cells in interphase over a {CYCLE_HOURS:.0f} hour "
            f"cycle gives {hours:.0f} hours, and no distractor value matches")


def q18(table, item):
    labs = cg.labels(table)
    dna = dict(zip(labs, cg.col(table, H_DNA)))
    g1 = [k for k in labs if "g1" in k.lower()]
    s_end = [k for k in labs if "end of s" in k.lower()]
    g2 = [k for k in labs if k.lower().strip() == "g2"]
    daughter = [k for k in labs if "daughter" in k.lower()]
    assert len(g1) == len(s_end) == len(g2) == len(daughter) == 1, \
        f"one row each for G1, end of S, G2 and the daughter cells; got {labs}"
    a, b, c, d = g1[0], s_end[0], g2[0], daughter[0]
    assert dna[b] == 2 * dna[a], f"DNA must double by the end of S: {dna[a]} to {dna[b]}"
    assert dna[c] == dna[b], "G2 must hold the doubled amount"
    assert dna[d] == dna[a], f"each daughter must hold the G1 amount: {dna[d]} against {dna[a]}"
    assert dna[d] != 2 * dna[a], "'a daughter holds twice the G1 amount' must be false"
    assert len(set(dna.values())) > 1, "'unchanged throughout the cycle' must be false"
    return (f"DNA per cell runs {dna[a]} in G1, {dna[b]} at the end of S, {dna[c]} in G2 and "
            f"{dna[d]} in each daughter cell, a doubling then an equal division")


def q19(table, item):
    labs = cg.labels(table)
    div = dict(zip(labs, cg.col(table, H_DIV)))
    g0 = dict(zip(labs, cg.col(table, H_G0)))
    for k in labs:
        assert div[k] + g0[k] <= 500, f"{k}: the two counts exceed the 500 cells counted"
        assert g0[k] > 0, "'no tissue contains any cells in G0' must be false"
        assert div[k] < 500, "'every cell counted was dividing' must be false"
    most_g0 = max(labs, key=lambda k: g0[k])
    fewest_div = min(labs, key=lambda k: div[k])
    assert most_g0 == fewest_div, \
        f"the most quiescent tissue must also be the least mitotic: {most_g0} against {fewest_div}"
    assert len(set(g0.values())) == len(labs), "'the same number in G0 in all three' must be false"
    order_g0 = sorted(labs, key=lambda k: g0[k])
    order_div = sorted(labs, key=lambda k: div[k], reverse=True)
    assert order_g0 == order_div, f"the two columns must run in opposite order: {order_g0} vs {order_div}"
    return (f"{most_g0} holds the most cells in G0 ({g0[most_g0]:.0f}) and the fewest dividing "
            f"({div[most_g0]:.0f}); ranking by either column reverses the other exactly")


def q20(table, item):
    labs = cg.labels(table)
    start = dict(zip(labs, cg.col(table, H_START)))
    end = dict(zip(labs, cg.col(table, H_END)))
    assert len(set(start.values())) == 1, \
        f"every culture must begin from the same number for the comparison to hold: {start}"
    ratios = {k: end[k] / start[k] for k in labs}
    best = max(ratios, key=ratios.get)
    assert list(ratios.values()).count(ratios[best]) == 1, "the largest increase must be unique"
    assert ratios[best] == 4, f"the keyed fourfold increase recomputes to {ratios[best]}"
    unchanged = [k for k in labs if end[k] == start[k]]
    assert unchanged and unchanged[0] != best, "'the culture that ended unchanged' must be false"
    gained200 = [k for k in labs if end[k] - start[k] == 200]
    assert gained200 and gained200[0] != best, "'the culture that gained two hundred cells' must be false"
    assert len(set(ratios.values())) == len(labs), "'all three increased by the same percentage' must be false"
    assert any(r > 1 for r in ratios.values()), "'none of the cultures increased' must be false"
    return (f"from an equal start of {start[best]:.0f} cells the ratios are "
            f"{[round(v, 2) for v in ratios.values()]}, and only {best} multiplied its number, "
            f"by {ratios[best]:.0f}")


CLAIMS = [
 ("highly regulated series of events",
  "EK 4.5.A.1 states that the cell cycle is a highly regulated series of events that controls the growth and reproduction of eukaryotic cells."),
 ("Interphase, made up of G1, S and G2, then mitosis, then cytokinesis",
  "EK 4.5.A.1.i states that the cell cycle consists of sequential stages of interphase (G1, S, G2), mitosis, and cytokinesis, in that order."),
 ("duplicating organelles and cytosolic components",
  "EK 4.5.A.1.ii states that in G1 phase the cell is metabolically active, duplicating organelles and cytosolic components. DNA replication belongs to S and centrosome replication to G2."),
 ("replicates to form two sister chromatids joined at a centromere",
  "EK 4.5.A.1.iii states that in S phase DNA is in the form of chromatin and replicates to form two sister chromatids connected at a centromere."),
 ("centrosomes replicate",
  "EK 4.5.A.1.iv states that in G2 phase protein synthesis occurs, ATP is produced in large quantities, and centrosomes replicate."),
 ("can reenter the cell cycle in response to appropriate cues",
  "EK 4.5.A.1.v states that a cell can enter a stage, G0, in which it no longer divides, but it can reenter the cell cycle in response to appropriate cues. Both halves belong to the statement."),
 ("exit the cell cycle or be held at a particular stage",
  "EK 4.5.A.1.vi states that nondividing cells may exit the cell cycle or be held at a particular stage in the cell cycle, naming both possibilities."),
 ("two genetically identical daughter cells",
  "EK 4.5.B.1 states that mitosis ensures the transfer of a complete genome from a parent cell to two genetically identical daughter cells in eukaryotes."),
 ("Growth, tissue repair, and asexual reproduction",
  "EK 4.5.B.1.i states that mitosis plays a role in growth, tissue repair, and asexual reproduction, naming all three."),
 ("Prophase, metaphase, anaphase, telophase, alternating with interphase",
  "EK 4.5.B.1.ii states that mitosis occurs in sequential steps, prophase, metaphase, anaphase, telophase, and alternates with interphase in the cell cycle."),
 ("chromatids condense, the mitotic spindle begins to form",
  "EK 4.5.B.1.iii states that in prophase sister chromatids condense, the mitotic spindle begins to form, and centrosomes move to opposite poles of the cell."),
 ("align the chromosomes along the equator",
  "EK 4.5.B.1.iv states that in metaphase spindle fibers align chromosomes along the equator of the cell."),
 ("separate as spindle fibers pull chromatids toward the poles",
  "EK 4.5.B.1.v states that in anaphase paired sister chromatids separate as spindle fibers pull chromatids toward poles."),
 ("spindle breaks down, a new nuclear envelope develops, and then the cytoplasm divides",
  "EK 4.5.B.1.vi states that in telophase the mitotic spindle breaks down, a new nuclear envelope develops, and then the cytoplasm divides."),
 ("cleavage furrow forms in animal cells and a cell plate forms in plant cells",
  "EK 4.5.B.1.vii states that in cytokinesis a cleavage furrow forms in animal cells or a cell plate forms in plant cells, resulting in two new daughter cells. The two are routinely swapped."),
 ("Seventy-five percent",
  "Recomputed in q16 above from the counts alone. Skill 5.A asks students to calculate percentages from a table, and no distractor value equals the computed one."),
 ("About fifteen hours",
  "Recomputed in q17 above. Skill 5.A asks for ratios and rates, and EK 4.5.A.1 makes the cycle a sequence of stages, so the share of cells in a stage estimates the share of the cycle it occupies."),
 ("doubles before division and each daughter cell receives the original amount",
  "Recomputed in q18 above. EK 4.5.A.1.iii has DNA replicate in S phase and EK 4.5.B.1 has mitosis transfer a complete genome to each of two daughter cells; the table shows both as numbers."),
 ("most cells in G0 has the fewest dividing cells",
  "Recomputed in q19 above. EK 4.5.A.1.v states that a cell in G0 no longer divides, so quiescent cells are not among the dividing ones, and skill 4.B asks for the relationship between the two columns."),
 ("four times as many cells as it began with",
  "Recomputed in q20 above. Skill 5.A asks for percent changes from a table; the three cultures begin equal, so the largest final count is also the largest percent increase."),
 ("entered G0 and later reentered the cell cycle",
  "EK 4.5.A.1.v states that a cell can enter G0, in which it no longer divides, but can reenter the cell cycle in response to appropriate cues, which is exactly the sequence described."),
 ("S phase",
  "EK 4.5.A.1.iii places DNA replication in S phase, where DNA in the form of chromatin replicates to form two sister chromatids connected at a centromere."),
 ("G2 phase",
  "EK 4.5.A.1.iv states that in G2 phase protein synthesis occurs, ATP is produced in large quantities, and centrosomes replicate. DNA replication is what belongs to S under EK 4.5.A.1.iii."),
 ("complete genome from the parent cell to each of them",
  "EK 4.5.B.1 states that mitosis ensures the transfer of a complete genome from a parent cell to two genetically identical daughter cells; complete transfer to each is what makes them identical."),
 ("plant cell forms a cell plate while the animal cell forms a cleavage furrow",
  "EK 4.5.B.1.vii states that in cytokinesis a cleavage furrow forms in animal cells or a cell plate forms in plant cells, resulting in two new daughter cells in both."),
 ("sister chromatids separate and move toward the poles",
  "EK 4.5.B.1.ii gives the order prophase, metaphase, anaphase, telophase, while EK 4.5.B.1.iv places alignment at the equator in metaphase and EK 4.5.B.1.v the separation of chromatids in anaphase."),
 ("Formed during S phase and separated during anaphase",
  "EK 4.5.A.1.iii has DNA replicate in S phase to form two sister chromatids joined at a centromere, and EK 4.5.B.1.v has paired sister chromatids separate in anaphase."),
 ("share caught in a stage reflects the share of the cycle",
  "EK 4.5.A.1 makes the cycle a sequential series of stages and skill 5.A asks students to work with ratios. Many independently cycling cells distribute across the stages in proportion to the time each takes."),
 ("can never return to the cell cycle",
  "EK 4.5.A.1.v states that a cell in G0 can reenter the cell cycle in response to appropriate cues. The other four options restate EK 4.5.A.1.iv, EK 4.5.B.1, EK 4.5.B.1.iv and EK 4.5.A.1.vi directly."),
 ("delivers a complete genome to each of two identical daughter cells",
  "EK 4.5.A.1 and EK 4.5.A.1.i give the regulated sequence of interphase, mitosis and cytokinesis, and EK 4.5.B.1 gives the transfer of a complete genome to two genetically identical daughter cells."),
]

cg.check(b4_5, CLAIMS, table_checks={16: q16, 17: q17, 18: q18, 19: q19, 20: q20})
