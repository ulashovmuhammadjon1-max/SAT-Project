"""Key audit for AP BIOLOGY 5.1 Meiosis.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the keyed choice and in no distractor, so the key
survives the shuffle ``export_units.py`` applies on export.

WHAT THE KEYS REST ON
---------------------
Every key traces to an essential knowledge statement of topic 5.1, listed at
the head of ``b5_1.py`` and cited by code in each claim below. The one
statement that carries more of the module than any other, because reversing it
is the single most common error in this topic, is:

  5.1.A.2.iii  in ANAPHASE I, HOMOLOGOUS CHROMOSOMES SEPARATE while SISTER
               CHROMATIDS REMAIN ATTACHED
  5.1.A.3.iii  in ANAPHASE II, proteins at the centromeres break down and
               SISTER CHROMATIDS ARE PULLED APART

Items 4, 14, 15, 17, 19, 20, 29 and 30 all turn on that pair, and the reversed
version is offered as a distractor in each.

BOUNDARY WITH 5.2. Crossing over as a SOURCE OF DIVERSITY, random assortment,
fertilization and nondisjunction are topic 5.2 and carry no key here. Chiasmata
appear only in item 12, because EK 5.1.A.2.i lists them among the events of
prophase I, and that item asks WHEN they form rather than what they produce.
Item 22's claim cites EK 5.2.A.1 for the composition of a haploid set, and says
so.

BOUNDARY WITH 4.5. The mitotic phases are topic 4.5; items 10, 11, 16, 21 and
23 compare the two processes only because EK 5.1.B.1 is the statement that asks
for that comparison, and each cites EK 4.5.B.1 for the mitotic half.

NO FIGURES. Meiosis invites a diagram more than anything else in these units
and the bank cannot carry one, so items 14 to 18 carry tables of counts
instead. Every number is HYPOTHETICAL and the stem says so; each keyed
conclusion is recomputed below from the table alone and the distractors are
shown false against the same numbers.

FIVE choices per item (A-E), per SCIENCE_BRIEF.md.
"""
import cg_check as cg
import b5_1

COUNTS = b5_1._T_COUNTS
COMPARE = b5_1._T_COMPARE
SEPARATION = b5_1._T_SEPARATION
DNA = b5_1._T_DNA

H_CELLS = "Cells present"
H_CHROM = "Chromosomes per cell"
H_CHTD = "Chromatids per chromosome"
H_DAUGHTERS = "Daughter cells produced from one parent cell"
H_SETS = "Chromosome sets per daughter cell, relative to the parent cell"
H_HOMOLOG = "Cells in which homologous chromosomes were separating"
H_SISTER = "Cells in which sister chromatids were separating"
H_DNA = "DNA per cell relative to the cell before replication (hypothetical)"


def _counts(table):
    cells = cg.col(table, H_CELLS)
    chrom = cg.col(table, H_CHROM)
    chtd = cg.col(table, H_CHTD)
    assert len(cells) == 3, "the table must hold the start and the end of each division"
    assert cells == [1.0, 2.0, 4.0], f"one cell becoming two and then four: got {cells}"
    return cells, chrom, chtd


def q14(table, item):
    cells, chrom, chtd = _counts(table)
    assert chrom[1] == chrom[0] / 2, f"the first division must halve the chromosome number: {chrom}"
    assert chrom[2] == chrom[1], f"the second division must leave it unchanged: {chrom}"
    assert chrom[0] != chrom[2], "'unchanged at both divisions' must be false"
    assert chrom[1] != 2 * chrom[0], "'doubled at the first division' must be false"
    return (f"chromosomes per cell run {chrom} as the cell count runs {cells}: halved at the first "
            f"division and unchanged at the second")


def q15(table, item):
    cells, chrom, chtd = _counts(table)
    assert chtd[1] == chtd[0], f"the first division must leave chromatids per chromosome alone: {chtd}"
    assert chtd[2] == chtd[1] / 2, f"the second division must halve it: {chtd}"
    assert chtd[2] == 1, "each final cell must hold an unduplicated chromatid"
    assert chtd[0] != chtd[2], "'unchanged at both divisions' must be false"
    return (f"chromatids per chromosome run {chtd}: unchanged through the first division and halved "
            f"at the second, ending at one per chromosome")


def q16(table, item):
    labs = cg.labels(table)
    daughters = dict(zip(labs, cg.col(table, H_DAUGHTERS)))
    sets = dict(zip(labs, cg.col(table, H_SETS)))
    mit = [k for k in labs if "mitosis" in k.lower()]
    mei = [k for k in labs if "meiosis" in k.lower()]
    assert len(mit) == 1 and len(mei) == 1, f"one row each for mitosis and meiosis; got {labs}"
    a, b = mit[0], mei[0]
    assert daughters[a] != daughters[b], "'identical in both respects' must be false on the cell count"
    assert sets[a] != sets[b], "'identical in both respects' must be false on chromosome content"
    more_cells = max(labs, key=lambda k: daughters[k])
    more_sets = max(labs, key=lambda k: sets[k])
    assert more_cells != more_sets, \
        "'the process producing more daughter cells also gives each more chromosome sets' must be false"
    assert daughters[b] == 2 * daughters[a] and sets[b] == sets[a] / 2, \
        f"meiosis must double the cell count and halve the content: {daughters}, {sets}"
    return (f"{a} gives {daughters[a]:.0f} cells at {sets[a]} sets each and {b} gives "
            f"{daughters[b]:.0f} at {sets[b]}, so the two differ on both measures and in opposite directions")


def q17(table, item):
    labs = cg.labels(table)
    homolog = dict(zip(labs, cg.col(table, H_HOMOLOG)))
    sister = dict(zip(labs, cg.col(table, H_SISTER)))
    first = [k for k in labs if "first" in k.lower()]
    second = [k for k in labs if "second" in k.lower()]
    assert len(first) == 1 and len(second) == 1, f"one first and one second anaphase row; got {labs}"
    f, s = first[0], second[0]
    assert homolog[f] > 0 and sister[f] == 0, \
        f"the first anaphase must show only homologous separation: {homolog[f]}, {sister[f]}"
    assert sister[s] > 0 and homolog[s] == 0, \
        f"the second anaphase must show only chromatid separation: {homolog[s]}, {sister[s]}"
    assert (homolog[f], sister[f]) != (homolog[s], sister[s]), \
        "'the two anaphases are indistinguishable' must be false"
    return (f"the first anaphase scores {homolog[f]:.0f} homologous separations and "
            f"{sister[f]:.0f} chromatid separations; the second scores {homolog[s]:.0f} and "
            f"{sister[s]:.0f}, so each kind occurs in exactly one of them")


def q18(table, item):
    labs = cg.labels(table)
    dna = dict(zip(labs, cg.col(table, H_DNA)))
    pre = [k for k in labs if "before dna" in k.lower()]
    post = [k for k in labs if "after replication" in k.lower()]
    one = [k for k in labs if "after meiosis i" in k.lower() and "ii" not in k.lower().split("meiosis")[1]]
    two = [k for k in labs if "after meiosis ii" in k.lower()]
    assert len(pre) == len(post) == len(one) == len(two) == 1, \
        f"one row each for before replication, after replication, after meiosis I and after meiosis II; got {labs}"
    a, b, c, d = pre[0], post[0], one[0], two[0]
    assert dna[b] == 2 * dna[a], f"replication must double the DNA: {dna[a]} to {dna[b]}"
    assert dna[c] == dna[b] / 2, f"the first division must halve it: {dna[b]} to {dna[c]}"
    assert dna[d] == dna[c] / 2, f"the second division must halve it again: {dna[c]} to {dna[d]}"
    assert dna[c] != dna[b], "'halved only at the second division' must be false"
    assert len(set(dna.values())) > 1, "'unchanged throughout' must be false"
    return (f"DNA per cell runs {dna[a]}, {dna[b]}, {dna[c]}, {dna[d]}: one doubling before the first "
            f"division and one halving at each of the two divisions")


CLAIMS = [
 ("haploid gamete cells in sexually reproducing diploid organisms",
  "EK 5.1.A.1 states that meiosis ensures the formation of haploid gamete cells, sometimes referred to as daughter cells, in sexually reproducing diploid organisms."),
 ("synapsis occurs, the spindle begins to form",
  "EK 5.1.A.2.i lists the events of prophase I: homologous chromosomes pair up and condense, synapsis occurs and then chiasmata may form, the meiotic spindle begins to form, centrosomes move to opposite poles, and the nuclear envelope breaks down."),
 ("Homologous pairs of chromosomes",
  "EK 5.1.A.2.ii states that meiotic spindle fibers align homologous pairs of chromosomes along the equator of the cell at the metaphase plate. It is the pairs, not single chromatids, that are aligned."),
 ("Homologous chromosomes separate while sister chromatids remain attached",
  "EK 5.1.A.2.iii states that in anaphase I homologous chromosomes separate while sister chromatids remain attached, as meiotic spindle fibers pull chromosomes toward poles. The reversed version is the standard error."),
 ("Two cells, and both are haploid",
  "EK 5.1.A.2.iv states that two haploid daughter cells are formed at the end of meiosis I, after the spindle breaks down, a new nuclear envelope develops and cytokinesis occurs."),
 ("sister chromatids connected at the centromere attach to it",
  "EK 5.1.A.3.i states that in prophase II the meiotic spindle forms and sister chromatids connected at the centromere attach to the meiotic spindle."),
 ("kinetochore of each chromatid is attached to a microtubule",
  "EK 5.1.A.3.ii states that in metaphase II chromosomes align along the metaphase plate and the kinetochore of each chromatid is attached to a microtubule extending from the poles."),
 ("Proteins at the centromeres break down",
  "EK 5.1.A.3.iii states that in anaphase II proteins at the centromeres break down, and sister chromatids are pulled apart and toward opposite poles in the cell."),
 ("Four haploid cells, each with an unduplicated chromatid",
  "EK 5.1.A.3.iv states that four haploid daughter cells are formed at the end of telophase II, each with an unduplicated chromatid."),
 ("Both use a spindle apparatus to move chromosomes",
  "EK 5.1.B.1 states that mitosis and meiosis are similar in the use of a spindle apparatus to move chromosomes, and locates the differences elsewhere."),
 ("number of cells produced and in the genetic content",
  "EK 5.1.B.1 states that the two differ in the number of cells produced and the genetic content of the daughter cells. The spindle apparatus is what they share."),
 ("Prophase I",
  "EK 5.1.A.2.i states that in prophase I homologous chromosomes pair up and condense, synapsis occurs and then chiasmata may form. No later stage in the framework's list mentions either event."),
 ("cleavage furrow forms in an animal cell or a cell plate forms in a plant cell",
  "EK 5.1.A.2.iv and EK 5.1.A.3.iv both state that a cleavage furrow forms in an animal cell or a cell plate forms in a plant cell as cytokinesis occurs."),
 ("halved at the first division and unchanged at the second",
  "Recomputed in q14 above. EK 5.1.A.2.iii separates homologous chromosomes at the first division, halving the number per cell, while EK 5.1.A.3.iii separates sister chromatids at the second, which does not change the chromosome count."),
 ("unchanged at the first division and halved at the second",
  "Recomputed in q15 above. EK 5.1.A.2.iii keeps sister chromatids attached through the first division and EK 5.1.A.3.iii pulls them apart in the second, leaving each cell with an unduplicated chromatid per EK 5.1.A.3.iv."),
 ("differ both in how many daughter cells they produce and in the chromosome content",
  "Recomputed in q16 above. EK 5.1.B.1 states that mitosis and meiosis differ in the number of cells produced and the genetic content of the daughter cells, the two differences the columns show."),
 ("Homologous chromosomes separate in the first anaphase and sister chromatids in the second",
  "Recomputed in q17 above. EK 5.1.A.2.iii places homologous separation in anaphase I with sister chromatids still attached, and EK 5.1.A.3.iii places chromatid separation in anaphase II."),
 ("halved at each of the two divisions",
  "Recomputed in q18 above. EK 5.1.A.2.iv gives two haploid cells after the first division and EK 5.1.A.3.iv four haploid cells each with an unduplicated chromatid after the second, so the replicated material is divided twice."),
 ("The first, because homologous chromosomes separate into different cells",
  "EK 5.1.A.2.iii states that homologous chromosomes separate in anaphase I, and EK 5.1.A.2.iv states that two haploid daughter cells are formed at the end of meiosis I."),
 ("whole chromosomes with attached chromatids move apart",
  "EK 5.1.A.2.iii has homologous chromosomes separate while sister chromatids remain attached, and EK 5.1.A.3.iii has proteins at the centromeres break down so that sister chromatids are pulled apart."),
 ("Four, which is twice the number mitosis produces",
  "EK 5.1.A.3.iv gives four haploid daughter cells at the end of meiosis, EK 4.5.B.1 gives two daughter cells for mitosis, and EK 5.1.B.1 names the number of cells produced as one of the two differences."),
 ("carries one chromosome set where the diploid parent cell carried two",
  "EK 5.1.A.1 makes meiosis the formation of haploid gamete cells in sexually reproducing DIPLOID organisms, and EK 5.2.A.1 describes each gamete as receiving a haploid set comprising an assortment of maternal and paternal chromosomes."),
 ("mechanism of chromosome movement is common to both",
  "EK 5.1.B.1 states that mitosis and meiosis are similar in the use of a spindle apparatus to move chromosomes but differ in the number of cells produced and in the genetic content of the daughter cells."),
 ("Homologous pairs of chromosomes in the first, and individual chromosomes in the second",
  "EK 5.1.A.2.ii aligns homologous PAIRS at the metaphase plate in metaphase I, while EK 5.1.A.3.ii aligns chromosomes with each chromatid's kinetochore attached to a microtubule in metaphase II."),
 ("not pulled toward the poles, so the division does not proceed normally",
  "EK 5.1.A.2.iii makes the meiotic spindle fibers what pulls chromosomes toward the poles in anaphase I, and EK 5.1.B.1 names the spindle apparatus as the mechanism of chromosome movement in both processes."),
 ("In telophase I and again in telophase II",
  "EK 5.1.A.2.iv and EK 5.1.A.3.iv both state that the meiotic spindle breaks down and a new nuclear envelope develops, in telophase I and in telophase II respectively."),
 ("They begin to decondense",
  "EK 5.1.A.3.iv states that in telophase II the spindle breaks down, a new nuclear envelope develops, a cleavage furrow or cell plate forms, chromatids begin to decondense, and cytokinesis occurs."),
 ("Prophase I, metaphase I, anaphase I, telophase I, then prophase II",
  "EK 5.1.A.2 lists the four steps of meiosis I in order and EK 5.1.A.3 then lists the four steps of meiosis II in order, with two haploid cells formed between the two divisions."),
 ("Sister chromatids separate during anaphase I while homologous chromosomes remain attached",
  "EK 5.1.A.2.iii states the opposite: homologous chromosomes separate in anaphase I while sister chromatids remain attached. The other four options restate EK 5.1.A.2.i, EK 5.1.A.2.iv, EK 5.1.A.3.iv and EK 5.1.B.1."),
 ("first separates homologous chromosomes to give two haploid cells",
  "EK 5.1.A.2.iii and EK 5.1.A.2.iv give homologous separation and two haploid cells for the first division, and EK 5.1.A.3.iii and EK 5.1.A.3.iv give chromatid separation and four haploid cells for the second."),
]

cg.check(b5_1, CLAIMS, table_checks={14: q14, 15: q15, 16: q16, 17: q17, 18: q18})
