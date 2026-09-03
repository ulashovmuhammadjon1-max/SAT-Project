# AP BIOLOGY 5.1 Meiosis
# CED effective Fall 2025, Unit 5 Heredity.
# Big Idea 3 Information Storage and Transmission.
# Learning objectives 5.1.A (explain how meiosis results in the transmission of
# chromosomes from one generation to the next) and 5.1.B (describe similarities
# and differences between the phases and outcomes of mitosis and meiosis).
# Suggested skill 1.B, explain biological concepts and processes.
#
# Essential knowledge, in the framework's own terms:
#   5.1.A.1     meiosis ensures the formation of HAPLOID GAMETE CELLS in
#               SEXUALLY REPRODUCING DIPLOID organisms
#   5.1.A.2     meiosis I:
#     i.        Prophase I: HOMOLOGOUS CHROMOSOMES PAIR UP and condense,
#               SYNAPSIS occurs and then CHIASMATA MAY FORM, meiotic spindle
#               begins to form, centrosomes move to opposite poles, the NUCLEAR
#               ENVELOPE BREAKS DOWN
#     ii.       Metaphase I: spindle fibers align HOMOLOGOUS PAIRS of
#               chromosomes along the equator at the METAPHASE PLATE
#     iii.      Anaphase I: HOMOLOGOUS CHROMOSOMES SEPARATE while SISTER
#               CHROMATIDS REMAIN ATTACHED
#     iv.       Telophase I: spindle breaks down, new nuclear envelope develops,
#               a CLEAVAGE FURROW (animal) or CELL PLATE (plant) forms,
#               cytokinesis occurs; TWO HAPLOID daughter cells are formed
#   5.1.A.3     meiosis II:
#     i.        Prophase II: meiotic spindle forms; SISTER CHROMATIDS CONNECTED
#               AT THE CENTROMERE attach to the spindle
#     ii.       Metaphase II: chromosomes align along the METAPHASE PLATE; the
#               KINETOCHORE of each chromatid is attached to a MICROTUBULE
#               extending from the poles
#     iii.      Anaphase II: PROTEINS AT THE CENTROMERES BREAK DOWN and SISTER
#               CHROMATIDS ARE PULLED APART toward opposite poles
#     iv.       Telophase II: spindle breaks down, new nuclear envelope
#               develops, cleavage furrow or cell plate forms, CHROMATIDS BEGIN
#               TO DECONDENSE, cytokinesis occurs; FOUR HAPLOID daughter cells
#               are formed, EACH WITH AN UNDUPLICATED CHROMATID
#   5.1.B.1     mitosis and meiosis are SIMILAR in the use of a SPINDLE
#               APPARATUS to move chromosomes but DIFFER in the NUMBER OF CELLS
#               PRODUCED and the GENETIC CONTENT of the daughter cells
#
# BOUNDARY WITH 5.2, HELD DELIBERATELY. Crossing over as a SOURCE OF GENETIC
# DIVERSITY, random assortment, fertilization and nondisjunction are essential
# knowledge of topic 5.2 and carry no key here. Chiasmata appear in item 12
# only because EK 5.1.A.2.i lists them among the events of prophase I, and that
# item asks WHEN they form, not what they produce.
#
# BOUNDARY WITH 4.5. The mitotic phases themselves are topic 4.5; items 10, 11,
# 16 and 23 compare the two processes because EK 5.1.B.1 is the statement that
# asks for the comparison, and each cites EK 4.5.B.1 for the mitotic half.
#
# NO FIGURES ANYWHERE. Meiosis invites a diagram more than any other topic in
# this unit and the bank cannot carry one, so every data item is a table of
# counts and the question is asked of the table.
#
# FIVE choices (A-E). Plain prose, no LaTeX.
TOPIC = ("5.1", "Meiosis", 5)

_T_COUNTS = dict(
    headers=["Point in the process (hypothetical organism with eight chromosomes per body cell)",
             "Cells present", "Chromosomes per cell", "Chromatids per chromosome"],
    rows=[["Before meiosis I begins", "1", "8", "2"],
          ["At the end of meiosis I", "2", "4", "2"],
          ["At the end of meiosis II", "4", "4", "1"]])

_T_COMPARE = dict(
    headers=["Process observed (hypothetical)",
             "Daughter cells produced from one parent cell",
             "Chromosome sets per daughter cell, relative to the parent cell"],
    rows=[["Mitosis", "2", "1.0"],
          ["Meiosis", "4", "0.5"]])

_T_SEPARATION = dict(
    headers=["Cells observed (hypothetical counts)",
             "Cells in which homologous chromosomes were separating",
             "Cells in which sister chromatids were separating"],
    rows=[["Cells scored in the first anaphase", "240", "0"],
          ["Cells scored in the second anaphase", "0", "190"]])

_T_DNA = dict(
    headers=["Point in the process",
             "DNA per cell relative to the cell before replication (hypothetical)"],
    rows=[["Before DNA replication", "1.0"],
          ["After replication, before meiosis I", "2.0"],
          ["After meiosis I", "1.0"],
          ["After meiosis II", "0.5"]])

QUESTIONS = [
 dict(q="What does the framework say meiosis ensures?",
   choices=[
     "The formation of haploid gamete cells in sexually reproducing diploid organisms",
     "The formation of diploid body cells in sexually reproducing haploid organisms",
     "The formation of two genetically identical daughter cells",
     "The repair of damaged tissue in an adult organism",
     "The asexual reproduction of single-celled organisms"],
   ans=0,
   why="EK 5.1.A.1 states that meiosis is a process that ensures the formation of haploid gamete cells, sometimes referred to as daughter cells, in sexually reproducing diploid organisms."),

 dict(q="Which events does the framework place in prophase I?",
   choices=[
     "Homologous chromosomes pair up and condense, synapsis occurs, the spindle begins to form, and the nuclear envelope breaks down",
     "Homologous pairs align along the equator of the cell",
     "Homologous chromosomes separate toward opposite poles",
     "Sister chromatids are pulled apart toward opposite poles",
     "Four haploid daughter cells are formed"],
   ans=0,
   why="EK 5.1.A.2.i lists these as the events of prophase I: homologous chromosomes pair up and condense, synapsis occurs and then chiasmata may form, the meiotic spindle begins to form, centrosomes move to opposite poles, and the nuclear envelope breaks down."),

 dict(q="What does the framework say the spindle fibers align at the equator during metaphase I?",
   choices=[
     "Homologous pairs of chromosomes",
     "Individual chromatids separated from their partners",
     "The centrosomes of the cell",
     "The two daughter nuclei formed earlier",
     "The nuclear envelope fragments"],
   ans=0,
   why="EK 5.1.A.2.ii states that meiotic spindle fibers align homologous pairs of chromosomes along the equator of the cell at the metaphase plate. It is the pairs, not single chromatids, that are aligned."),

 dict(q="What separates during anaphase I, and what stays together?",
   choices=[
     "Homologous chromosomes separate while sister chromatids remain attached",
     "Sister chromatids separate while homologous chromosomes remain attached",
     "Both homologous chromosomes and sister chromatids separate at once",
     "Neither separates; the cell simply divides its cytoplasm",
     "The centrosomes separate while the chromosomes remain at the equator"],
   ans=0,
   why="EK 5.1.A.2.iii states that in anaphase I homologous chromosomes separate while sister chromatids remain attached, as meiotic spindle fibers pull chromosomes toward poles."),

 dict(q="How many cells are present at the end of meiosis I, and what is their chromosome status?",
   choices=[
     "Two cells, and both are haploid",
     "Two cells, and both are diploid",
     "Four cells, and all are haploid",
     "One cell, still diploid",
     "Four cells, and all are diploid"],
   ans=0,
   why="EK 5.1.A.2.iv states that two haploid daughter cells are formed at the end of meiosis I, after the spindle breaks down, a new nuclear envelope develops and cytokinesis occurs."),

 dict(q="What does the framework say happens in prophase II?",
   choices=[
     "The meiotic spindle forms and sister chromatids connected at the centromere attach to it",
     "Homologous chromosomes pair up and undergo synapsis",
     "Sister chromatids are pulled apart toward opposite poles",
     "Four haploid daughter cells complete their cytokinesis",
     "The chromosomes align along the metaphase plate"],
   ans=0,
   why="EK 5.1.A.3.i states that in prophase II the meiotic spindle forms and sister chromatids connected at the centromere attach to the meiotic spindle."),

 dict(q="What does the framework say about the attachment of chromatids in metaphase II?",
   choices=[
     "The kinetochore of each chromatid is attached to a microtubule extending from the poles",
     "The centromere of each chromatid is attached to the nuclear envelope",
     "Each chromatid is attached to its homologous partner rather than to the spindle",
     "The chromatids are unattached and drift freely in the cytoplasm",
     "Each chromatid is attached to a cell plate forming at the equator"],
   ans=0,
   why="EK 5.1.A.3.ii states that in metaphase II chromosomes align along the metaphase plate and the kinetochore of each chromatid is attached to a microtubule extending from the poles."),

 dict(q="What does the framework say happens at the centromeres during anaphase II?",
   choices=[
     "Proteins at the centromeres break down and the sister chromatids are pulled apart",
     "Proteins at the centromeres are synthesized so the chromatids are joined more tightly",
     "The centromeres attach the chromatids to their homologous partners",
     "The centromeres form the cleavage furrow that divides the cytoplasm",
     "The centromeres become the new nuclear envelope"],
   ans=0,
   why="EK 5.1.A.3.iii states that in anaphase II proteins at the centromeres break down, and sister chromatids are pulled apart and toward opposite poles in the cell."),

 dict(q="How many cells does the framework say are formed at the end of meiosis II, and what does each contain?",
   choices=[
     "Four haploid cells, each with an unduplicated chromatid",
     "Two haploid cells, each with a duplicated chromosome",
     "Four diploid cells, each with a duplicated chromosome",
     "Two diploid cells, each with an unduplicated chromatid",
     "One haploid cell with all of the chromatids"],
   ans=0,
   why="EK 5.1.A.3.iv states that four haploid daughter cells are formed at the end of telophase II, each with an unduplicated chromatid."),

 dict(q="In what respect does the framework say mitosis and meiosis are SIMILAR?",
   choices=[
     "Both use a spindle apparatus to move chromosomes",
     "Both produce the same number of daughter cells",
     "Both produce daughter cells with the same genetic content as the parent",
     "Both involve the pairing of homologous chromosomes",
     "Both occur only in cells that are about to form gametes"],
   ans=0,
   why="EK 5.1.B.1 states that mitosis and meiosis are similar in the use of a spindle apparatus to move chromosomes, and that the differences lie elsewhere."),

 dict(q="In what two respects does the framework say mitosis and meiosis DIFFER?",
   choices=[
     "In the number of cells produced and in the genetic content of the daughter cells",
     "In whether a spindle apparatus is used and in how long the process takes",
     "In whether chromosomes are moved at all and in the size of the parent cell",
     "In the number of parent cells required and in the temperature at which they occur",
     "In whether the cell is eukaryotic and in whether it contains a nucleus"],
   ans=0,
   why="EK 5.1.B.1 states that the two differ in the number of cells produced and the genetic content of the daughter cells. The spindle apparatus is what they share."),

 dict(q="At which point in meiosis does the framework place synapsis and the possible formation of chiasmata?",
   choices=[
     "Prophase I",
     "Metaphase I",
     "Anaphase II",
     "Telophase II",
     "After the four daughter cells have formed"],
   ans=0,
   why="EK 5.1.A.2.i states that in prophase I homologous chromosomes pair up and condense, synapsis occurs and then chiasmata may form. No later stage in the framework's list mentions either event."),

 dict(q="How many times does a cell that completes meiosis divide its cytoplasm, and at which points?",
   choices=[
     "Twice, once at the end of each of the two meiotic divisions",
     "Once, only at the end of the second meiotic division",
     "Once, only at the end of the first meiotic division",
     "Four times, once for each daughter cell that is eventually produced",
     "Not at all, since the four nuclei remain within a single cell"],
   ans=0,
   why="EK 5.1.A.2.iv places cytokinesis at the end of telophase I, giving two haploid cells, and EK 5.1.A.3.iv places it again at the end of telophase II, giving four. The cytoplasm is therefore divided once per division."),

 dict(q="Cells and chromosomes were counted at three points in meiosis, with the results shown. What happens to the chromosome number per cell across the two divisions?",
   table=_T_COUNTS,
   choices=[
     "It is halved at the first division and unchanged at the second",
     "It is halved at the second division and unchanged at the first",
     "It is halved at both divisions",
     "It is unchanged at both divisions",
     "It is doubled at the first division and halved at the second"],
   ans=0,
   why="EK 5.1.A.2.iii has homologous chromosomes separate at the first division, which halves the number per cell, while EK 5.1.A.3.iii has sister chromatids separate at the second, which does not change the number of chromosomes."),

 dict(q="Using the same counts, what happens to the number of chromatids per chromosome across the two divisions?",
   table=_T_COUNTS,
   choices=[
     "It is unchanged at the first division and halved at the second",
     "It is halved at the first division and unchanged at the second",
     "It is halved at both divisions",
     "It is unchanged at both divisions",
     "It is doubled at the second division"],
   ans=0,
   why="EK 5.1.A.2.iii states that sister chromatids remain attached through the first division, and EK 5.1.A.3.iii states that they are pulled apart in the second, leaving each daughter cell with an unduplicated chromatid per EK 5.1.A.3.iv."),

 dict(q="The outcomes of two processes were compared, with the results shown. Which statement about the comparison is supported?",
   table=_T_COMPARE,
   choices=[
     "The two processes differ both in how many daughter cells they produce and in the chromosome content of those cells",
     "The two processes differ in how many daughter cells they produce but not in chromosome content",
     "The two processes differ in chromosome content but not in how many daughter cells they produce",
     "The two processes are identical in both respects",
     "The process producing more daughter cells also gives each of them more chromosome sets"],
   ans=0,
   why="EK 5.1.B.1 states that mitosis and meiosis differ in the number of cells produced and the genetic content of the daughter cells, which is exactly the pair of differences the two columns show."),

 dict(q="Cells caught in the two anaphases were scored, with the results shown. Which conclusion do the data support?",
   table=_T_SEPARATION,
   choices=[
     "Homologous chromosomes separate in the first anaphase and sister chromatids in the second",
     "Sister chromatids separate in the first anaphase and homologous chromosomes in the second",
     "Both kinds of separation occur in both anaphases",
     "Neither kind of separation was observed in either anaphase",
     "The two anaphases are indistinguishable on the measures reported"],
   ans=0,
   why="EK 5.1.A.2.iii places the separation of homologous chromosomes in anaphase I with sister chromatids still attached, and EK 5.1.A.3.iii places the separation of sister chromatids in anaphase II."),

 dict(q="A cell entering meiosis was sampled before replication and again after each of its two divisions, with the results shown. Which interpretation is best supported?",
   table=_T_DNA,
   choices=[
     "DNA doubles before the first division and is then halved at each of the two divisions",
     "DNA doubles before the first division and is halved only at the second division",
     "DNA is halved before the first division and doubled at each division",
     "DNA is unchanged throughout the whole process",
     "DNA doubles again between the first and the second division"],
   ans=0,
   why="EK 5.1.A.2.iv gives two haploid cells at the end of meiosis I and EK 5.1.A.3.iv gives four haploid cells each with an unduplicated chromatid at the end of meiosis II, so the replicated material is divided twice."),

 dict(q="Which of the two meiotic divisions reduces the chromosome number of the cell, and why?",
   choices=[
     "The first, because homologous chromosomes separate into different cells",
     "The second, because homologous chromosomes separate into different cells",
     "The first, because sister chromatids are pulled apart into different cells",
     "The second, because the nuclear envelope re-forms around fewer chromosomes",
     "Neither, because both divisions leave the chromosome number unchanged"],
   ans=0,
   why="EK 5.1.A.2.iii states that homologous chromosomes separate in anaphase I, and EK 5.1.A.2.iv states that two haploid daughter cells are formed at the end of meiosis I."),

 dict(q="What is the essential difference between anaphase I and anaphase II?",
   choices=[
     "In the first, whole chromosomes with attached chromatids move apart; in the second, the chromatids themselves are pulled apart",
     "In the first, chromatids are pulled apart; in the second, whole chromosomes move apart",
     "In the first, the spindle is absent; in the second, the spindle is present",
     "In the first, no chromosomes move; in the second, all chromosomes move",
     "There is no difference between the two anaphases"],
   ans=0,
   why="EK 5.1.A.2.iii has homologous chromosomes separate while sister chromatids remain attached, and EK 5.1.A.3.iii has proteins at the centromeres break down so that sister chromatids are pulled apart."),

 dict(q="How many daughter cells does one parent cell produce by the end of meiosis, and how does that compare with mitosis?",
   choices=[
     "Four, which is twice the number mitosis produces from one parent cell",
     "Two, which is the same number mitosis produces from one parent cell",
     "Four, which is half the number mitosis produces from one parent cell",
     "One, which is fewer than mitosis produces from one parent cell",
     "Eight, which is four times the number mitosis produces from one parent cell"],
   ans=0,
   why="EK 5.1.A.3.iv gives four haploid daughter cells at the end of meiosis, EK 4.5.B.1 gives two daughter cells for mitosis, and EK 5.1.B.1 names the number of cells produced as one of the two differences."),

 dict(q="What does it mean, in the framework's account, for a gamete cell to be haploid?",
   choices=[
     "It carries one chromosome set where the diploid parent cell carried two",
     "It carries twice as many chromosomes as the parent cell",
     "It carries no chromosomes at all",
     "It carries chromosomes that have not yet been replicated in the parent",
     "It carries the same number of chromosomes as the parent cell"],
   ans=0,
   why="EK 5.1.A.1 makes meiosis the formation of haploid gamete cells in sexually reproducing DIPLOID organisms, and EK 5.2.A.1 describes the haploid set as one that comprises an assortment of both maternal and paternal chromosomes."),

 dict(q="Both mitosis and meiosis move chromosomes with a spindle. What does that shared feature tell you about the two processes?",
   choices=[
     "The mechanism of chromosome movement is common to both, even though the outcomes differ",
     "The two processes must produce the same number of daughter cells",
     "The two processes must produce daughter cells of the same genetic content",
     "The two processes are the same process under two names",
     "Neither process can occur without the other occurring first"],
   ans=0,
   why="EK 5.1.B.1 states that mitosis and meiosis are similar in the use of a spindle apparatus to move chromosomes but differ in the number of cells produced and in the genetic content of the daughter cells."),

 dict(q="What is aligned at the metaphase plate in metaphase I compared with metaphase II?",
   choices=[
     "Homologous pairs of chromosomes in the first, and individual chromosomes in the second",
     "Individual chromosomes in the first, and homologous pairs in the second",
     "Homologous pairs in both",
     "Individual chromatids detached from their partners in both",
     "Nothing is aligned in either, since alignment occurs only in mitosis"],
   ans=0,
   why="EK 5.1.A.2.ii has spindle fibers align homologous PAIRS along the equator at the metaphase plate, while EK 5.1.A.3.ii has chromosomes align along the metaphase plate with each chromatid's kinetochore attached to a microtubule."),

 dict(q="A drug prevents the meiotic spindle from forming during meiosis I while leaving everything else intact. What is the most reasonable prediction?",
   choices=[
     "Chromosomes are not pulled toward the poles, so the division does not proceed normally",
     "Chromosomes are pulled toward the poles more quickly than usual",
     "Homologous chromosomes pair up twice instead of once",
     "The cell produces eight daughter cells instead of four",
     "The cell completes meiosis II without ever completing meiosis I"],
   ans=0,
   why="EK 5.1.A.2.iii makes the meiotic spindle fibers what pulls chromosomes toward the poles in anaphase I, and EK 5.1.B.1 names the spindle apparatus as the mechanism of chromosome movement in both processes."),

 dict(q="At which points in meiosis does the framework say a new nuclear envelope develops?",
   choices=[
     "In telophase I and again in telophase II",
     "In prophase I and again in prophase II",
     "In metaphase I only",
     "In anaphase II only",
     "At no point, because the nuclear envelope never re-forms"],
   ans=0,
   why="EK 5.1.A.2.iv and EK 5.1.A.3.iv both state that the meiotic spindle breaks down and a new nuclear envelope develops, in telophase I and in telophase II respectively."),

 dict(q="What does the framework say happens to the chromatids during telophase II?",
   choices=[
     "They begin to decondense",
     "They begin to condense for the first time",
     "They pair with their homologous partners",
     "They are replicated to restore the diploid number",
     "They are attached to microtubules extending from the poles"],
   ans=0,
   why="EK 5.1.A.3.iv states that in telophase II the meiotic spindle breaks down, a new nuclear envelope develops, a cleavage furrow or cell plate forms, chromatids begin to decondense, and cytokinesis occurs."),

 dict(q="Which sequence of events does the framework give for meiosis?",
   choices=[
     "Prophase I, metaphase I, anaphase I, telophase I, then prophase II, metaphase II, anaphase II, telophase II",
     "Prophase I, prophase II, metaphase I, metaphase II, anaphase I, anaphase II, telophase I, telophase II",
     "Telophase I, anaphase I, metaphase I, prophase I, then the same order again",
     "Prophase II, metaphase II, anaphase II, telophase II, then the first division",
     "Metaphase I, prophase I, telophase I, anaphase I, then the second division"],
   ans=0,
   why="EK 5.1.A.2 lists the four steps of meiosis I in order and EK 5.1.A.3 then lists the four steps of meiosis II in order, with two haploid cells formed between them."),

 dict(q="Which statement about meiosis is NOT supported by the framework?",
   choices=[
     "Four haploid daughter cells are already present at the end of meiosis I",
     "Homologous chromosomes pair up and undergo synapsis in prophase I",
     "The kinetochore of each chromatid attaches to a microtubule in metaphase II",
     "Chromatids begin to decondense during telophase II",
     "Mitosis and meiosis both use a spindle apparatus to move chromosomes"],
   ans=0,
   why="EK 5.1.A.2.iv states that TWO haploid daughter cells are formed at the end of meiosis I, and EK 5.1.A.3.iv puts the count of four at the end of meiosis II. The other four options restate EK 5.1.A.2.i, EK 5.1.A.3.ii, EK 5.1.A.3.iv and EK 5.1.B.1."),

 dict(q="Taken together, how does the framework describe what the two meiotic divisions accomplish?",
   choices=[
     "The first separates homologous chromosomes to give two haploid cells, and the second separates sister chromatids to give four",
     "The first separates sister chromatids to give two haploid cells, and the second separates homologous chromosomes to give four",
     "Both divisions separate homologous chromosomes, giving four diploid cells",
     "Both divisions separate sister chromatids, giving two diploid cells",
     "Neither division changes the chromosome content of the cell"],
   ans=0,
   why="EK 5.1.A.2.iii and EK 5.1.A.2.iv give homologous separation and two haploid cells for the first division, and EK 5.1.A.3.iii and EK 5.1.A.3.iv give chromatid separation and four haploid cells for the second."),
]
