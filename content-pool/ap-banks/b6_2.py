# AP BIOLOGY 6.2 DNA Replication
# CED effective Fall 2025, Unit 6 Gene Expression and Regulation. Big idea 3
# (Information Storage and Transmission). Learning objective 6.2.A, describe the
# mechanisms by which genetic information is copied for transmission between
# generations. Suggested skill 2.B, explain relationships between
# characteristics of biological models in both theoretical and applied contexts.
#
# Essential knowledge relied on, in the framework's own words:
#   6.2.A.1      DNA replication ensures CONTINUITY of hereditary information.
#   6.2.A.1.i    DNA is synthesized in the 5 prime to 3 prime direction.
#   6.2.A.1.ii   Replication is a SEMICONSERVATIVE process, meaning one strand
#                of DNA serves as the template for a new strand of complementary
#                DNA.
#   6.2.A.1.iii  Helicase unwinds the DNA strands.
#   6.2.A.1.iv   Topoisomerase relaxes supercoiling in front of the replication
#                fork.
#   6.2.A.1.v    DNA polymerase requires RNA primers to initiate DNA synthesis.
#   6.2.A.1.vi   DNA polymerase synthesizes new strands of DNA continuously on
#                the leading strand and discontinuously on the lagging strand.
#   6.2.A.1.vii  Ligase joins the fragments on the lagging strand.
#
#   EXCLUSION STATEMENT printed with this topic: the names of the steps and
#   particular enzymes involved, EXCLUDING DNA polymerase, ligase, RNA
#   polymerase, helicase, and topoisomerase, are beyond the scope of the AP
#   Exam. No item here names any other enzyme, in a stem, a key or a distractor.
#
# DIVISION OF LABOUR ACROSS 6.1 TO 6.4 is set out in the header of b6_1.py.
# 6.1 owns which base pairs with which; no item here asks a student to write a
# complementary sequence, and no item there involves an enzyme. The 5 prime to
# 3 prime direction is asked in 6.2 as the direction DNA is SYNTHESIZED and in
# 6.3 as the direction RNA polymerase READS ITS TEMPLATE, which are two
# different statements of the framework, EK 6.2.A.1.i and EK 6.3.A.3.
#
# ON FIGURES. No stem refers to a diagram of a replication fork. The density
# and inhibitor data are delivered as table=.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. Prose notation, no LaTeX.
TOPIC = ("6.2", "DNA Replication", 6)

# Cells grown for generations in a medium supplying a heavy form of nitrogen
# are moved to a medium supplying only the light form, and the DNA is separated
# by density after each round of replication.
_T_GEN = dict(
    headers=["Round of replication completed",
             "Percent of molecules with two heavy strands",
             "Percent of molecules with one heavy and one light strand",
             "Percent of molecules with two light strands"],
    rows=[["None", "100", "0", "0"],
          ["One", "0", "100", "0"],
          ["Two", "0", "50", "50"],
          ["Three", "0", "25", "75"]])

# The number of molecules produced from one starting molecule.
_T_COUNT = dict(
    headers=["Rounds of replication completed",
             "Number of double-stranded DNA molecules present"],
    rows=[["0", "1"],
          ["1", "2"],
          ["2", "4"],
          ["3", "8"]])

# What was made on each of the two new strands at one replication fork.
_T_FRAG = dict(
    headers=["New strand", "Number of separate DNA segments synthesized",
             "Number of joins needed to give one continuous strand"],
    rows=[["Leading strand", "1", "0"],
          ["Lagging strand", "12", "11"]])

# Four inhibitors applied separately to a cell copying its DNA.
_T_INHIB = dict(
    headers=["Inhibitor applied", "What is observed at the replication fork"],
    rows=[["Inhibitor 1", "The two strands stay wound around each other and no fork opens"],
          ["Inhibitor 2", "A fork opens, but the DNA ahead of it becomes steadily more supercoiled"],
          ["Inhibitor 3", "Short segments pile up along one new strand and are never joined to each other"],
          ["Inhibitor 4", "No new nucleotides are added at all, because no starting segment of RNA is laid down first"]])

QUESTIONS = [
 dict(q="Replication is described in the framework as a semiconservative process. What does that term mean?",
   choices=[
     "One strand of the original molecule serves as the template for a new strand of complementary DNA",
     "The two original strands stay together and both new strands pair with each other",
     "Each new molecule is built entirely from newly made nucleotides with no original strand retained",
     "Each new molecule contains fragments of original and new DNA scattered along both strands",
     "Only one of the two strands of the original molecule is copied, and the other is discarded"], ans=0,
   why="EK 6.2.A.1.ii states that replication is a semiconservative process, meaning one strand of DNA serves as the template for a new strand of complementary DNA. Each product therefore keeps one original strand and gains one new one, which is what the other four descriptions each deny in a different way."),
 dict(q="Cells that had been grown so that all of their DNA carried a heavy form of nitrogen were moved to a medium supplying only the light form. The table reports the density of the DNA after each round of replication. Which row shows the result that semiconservative replication predicts for the first round?",
   table=_T_GEN,
   choices=[
     "The row for one completed round, in which every molecule has one heavy and one light strand",
     "The row for one completed round, in which half of the molecules have two heavy strands",
     "The row for two completed rounds, in which half of the molecules have one strand of each",
     "The row for no completed rounds, in which every molecule has two heavy strands",
     "The row for three completed rounds, in which three quarters of the molecules have two light strands"], ans=0,
   why="EK 6.2.A.1.ii makes each original strand the template for one new strand, so after one round every molecule consists of one original heavy strand paired with one newly made light strand and none is left with two heavy strands. The table records exactly that at one completed round."),
 dict(q="Using the same density data, what fraction of the molecules still contains a strand from the original DNA after two rounds of replication?",
   table=_T_GEN,
   choices=[
     "One half, which is the proportion carrying one heavy and one light strand",
     "All of them, since replication is semiconservative at every round",
     "One quarter, which is the proportion carrying two heavy strands",
     "Three quarters, which is the proportion carrying at least one light strand",
     "None of them, since the original strands are broken down after the first round"], ans=0,
   why="An original strand is a heavy strand, and EK 6.2.A.1.ii means an original strand is retained intact in whichever molecule it templates. After two rounds the table records 50 percent of molecules with one heavy and one light strand and none with two heavy strands, so half of the molecules contain original DNA."),
 dict(q="A student proposes that replication is conservative, meaning that the two original strands stay together and the two new strands pair with each other. What result after one round of replication would this proposal predict, and what did the density data actually show?",
   choices=[
     "It predicts half of the molecules entirely heavy and half entirely light, whereas every molecule was found to carry one strand of each",
     "It predicts every molecule carrying one strand of each, whereas half of the molecules were found to be entirely heavy",
     "It predicts every molecule entirely light, whereas every molecule was found to be entirely heavy",
     "It predicts the same result as the semiconservative model, so the data cannot distinguish them",
     "It predicts no replication at all, since the original strands would never separate"], ans=0,
   why="A conservative model reunites the two original strands, so after one round in light medium half of the molecules would be the reconstituted heavy original and half entirely new and light. EK 6.2.A.1.ii instead makes each original strand the template for one new one, giving molecules that are half heavy and half light, which is what a single hybrid band at one round shows."),
 dict(q="What does helicase do during DNA replication?",
   choices=[
     "It unwinds the DNA strands",
     "It relaxes supercoiling in the DNA ahead of the replication fork",
     "It joins the fragments made on the lagging strand",
     "It adds nucleotides to a growing strand of DNA",
     "It lays down the RNA primers that DNA polymerase requires"], ans=0,
   why="EK 6.2.A.1.iii states that helicase unwinds the DNA strands. The other four descriptions belong to the other named participants: topoisomerase in EK 6.2.A.1.iv, ligase in EK 6.2.A.1.vii, DNA polymerase in EK 6.2.A.1.vi and the RNA primers of EK 6.2.A.1.v."),
 dict(q="What does topoisomerase do during DNA replication?",
   choices=[
     "It relaxes supercoiling in front of the replication fork",
     "It unwinds the two strands of the double helix at the fork",
     "It joins the fragments made on the lagging strand into one continuous strand",
     "It synthesizes the new strand continuously on the leading strand",
     "It removes the RNA primers once DNA synthesis is under way"], ans=0,
   why="EK 6.2.A.1.iv states that topoisomerase relaxes supercoiling in front of the replication fork. Unwinding the strands themselves is helicase's role under EK 6.2.A.1.iii, and the framework's exclusion statement puts any additional enzyme beyond the scope of the exam."),
 dict(q="Why can DNA polymerase not begin synthesizing a new strand on a bare template?",
   choices=[
     "It requires an RNA primer in order to initiate DNA synthesis",
     "It requires the template strand to be supercoiled before it can bind",
     "It requires ligase to join two nucleotides together before it can extend them",
     "It requires the two template strands to remain wound together",
     "It requires a completed leading strand before any synthesis can start"], ans=0,
   why="EK 6.2.A.1.v states that DNA polymerase requires RNA primers to initiate DNA synthesis. Supercoiling is what topoisomerase relaxes under EK 6.2.A.1.iv, ligase acts on already-made fragments under EK 6.2.A.1.vii, and helicase separates the strands under EK 6.2.A.1.iii."),
 dict(q="In which direction is a new strand of DNA synthesized?",
   choices=[
     "In the 5 prime to 3 prime direction",
     "In the 3 prime to 5 prime direction",
     "In the 5 prime to 3 prime direction on the leading strand and the 3 prime to 5 prime direction on the lagging strand",
     "In whichever direction the template strand runs, which differs between the two new strands",
     "In both directions at once from the point where the primer was laid down"], ans=0,
   why="EK 6.2.A.1.i states without qualification that DNA is synthesized in the 5 prime to 3 prime direction. The framework applies that one direction to both new strands, and EK 6.2.A.1.vi accounts for the difference between them by the continuity of synthesis rather than by a reversal of direction."),
 dict(q="How does DNA polymerase build the new strand on the leading strand at a replication fork?",
   choices=[
     "Continuously, as a single uninterrupted stretch of new DNA",
     "Discontinuously, as a series of separate segments that are later joined",
     "In short segments that are made in the 3 prime to 5 prime direction",
     "Only after the lagging strand has been completed and joined by ligase",
     "Without any primer, since a primer is needed only on the lagging strand"], ans=0,
   why="EK 6.2.A.1.vi states that DNA polymerase synthesizes new strands of DNA continuously on the leading strand and discontinuously on the lagging strand. EK 6.2.A.1.v makes RNA primers a requirement of DNA polymerase generally rather than of one strand, and EK 6.2.A.1.i fixes one direction of synthesis for both."),
 dict(q="How does DNA polymerase build the new strand on the lagging strand, and what must happen afterward?",
   choices=[
     "Discontinuously, as separate fragments that ligase then joins",
     "Continuously, as one stretch that ligase then trims to length",
     "Discontinuously, as separate fragments that helicase then joins",
     "Continuously, so that no joining step is needed on this strand",
     "Discontinuously, as separate fragments that remain separate in the finished molecule"], ans=0,
   why="EK 6.2.A.1.vi states that synthesis is discontinuous on the lagging strand and EK 6.2.A.1.vii states that ligase joins the fragments on the lagging strand. Helicase unwinds the strands under EK 6.2.A.1.iii and has no joining role, and fragments that stayed separate would not give the continuous molecule EK 6.2.A.1 requires."),
 dict(q="The table reports what was synthesized on each of the two new strands at one replication fork. How many joining events does the lagging strand require to become one continuous strand, and which participant carries them out?",
   table=_T_FRAG,
   choices=[
     "11 joins, carried out by ligase",
     "12 joins, carried out by ligase",
     "11 joins, carried out by helicase",
     "1 join, carried out by DNA polymerase",
     "No joins, because the fragments are made continuously"], ans=0,
   why="Joining a row of separate segments into one strand takes one fewer join than there are segments, so 12 segments require 11 joins, which is the number the table records. EK 6.2.A.1.vii states that ligase joins the fragments on the lagging strand; helicase unwinds strands under EK 6.2.A.1.iii and DNA polymerase adds nucleotides under EK 6.2.A.1.vi."),
 dict(q="The table reports what happens at the replication fork when each of four inhibitors is applied on its own. Which inhibitor is acting on ligase?",
   table=_T_INHIB,
   choices=[
     "Inhibitor 3, because short segments pile up along one new strand and are never joined",
     "Inhibitor 1, because the strands stay wound around each other and no fork opens",
     "Inhibitor 2, because the DNA ahead of the fork becomes steadily more supercoiled",
     "Inhibitor 4, because no nucleotides are added without a starting segment of RNA",
     "None of them, because ligase acts after replication is complete and would not be seen at the fork"], ans=0,
   why="EK 6.2.A.1.vii states that ligase joins the fragments on the lagging strand, so blocking it leaves those fragments made but unjoined. The other three observations match helicase in EK 6.2.A.1.iii, topoisomerase in EK 6.2.A.1.iv and the RNA primer requirement in EK 6.2.A.1.v."),
 dict(q="Using the same set of inhibitor results, which inhibitor is acting on topoisomerase?",
   table=_T_INHIB,
   choices=[
     "Inhibitor 2, because the DNA ahead of the fork becomes steadily more supercoiled",
     "Inhibitor 1, because the strands stay wound around each other and no fork opens",
     "Inhibitor 3, because segments along one new strand are never joined to each other",
     "Inhibitor 4, because synthesis never begins on either new strand",
     "Inhibitor 1 and inhibitor 2 equally, because both concern the winding of the DNA"], ans=0,
   why="EK 6.2.A.1.iv states that topoisomerase relaxes supercoiling in front of the replication fork, so blocking it lets supercoiling build up ahead of a fork that has nevertheless opened. Blocking helicase would prevent the fork from opening at all under EK 6.2.A.1.iii, which is why the two winding-related observations are not interchangeable."),
 dict(q="A drug prevents helicase from working in a dividing cell. What is the most direct consequence for replication?",
   choices=[
     "The two strands are not separated, so no template is exposed for a new strand to be built on",
     "The two strands separate normally but no primer can be laid down on them",
     "The new strands are built but the fragments on the lagging strand are never joined",
     "Supercoiling builds up ahead of the fork while synthesis continues normally behind it",
     "Replication proceeds normally, since helicase acts only after the new strands are finished"], ans=0,
   why="EK 6.2.A.1.iii states that helicase unwinds the DNA strands, and EK 6.2.A.1.ii requires a single strand to serve as the template for the new complementary strand. With the strands still wound together there is no exposed template, so the failure comes before priming, synthesis or joining."),
 dict(q="Cells are treated so that RNA primers can no longer be made. What is the most direct consequence for replication?",
   choices=[
     "DNA polymerase cannot initiate synthesis, so no new DNA strand is started",
     "DNA polymerase synthesizes the leading strand normally but cannot start the lagging strand",
     "The DNA strands cannot be unwound, so no replication fork opens",
     "The fragments on the lagging strand are made but cannot be joined together",
     "Replication proceeds normally, because primers are made of RNA rather than DNA"], ans=0,
   why="EK 6.2.A.1.v states that DNA polymerase requires RNA primers to initiate DNA synthesis, and the framework attaches that requirement to the polymerase rather than to one of the two strands. Unwinding is helicase's role under EK 6.2.A.1.iii and joining is ligase's under EK 6.2.A.1.vii, so neither is what fails first here."),
 dict(q="Why does the framework say that DNA replication ensures continuity of hereditary information?",
   choices=[
     "Each new molecule carries the same sequence as the original, so the information passes unchanged to the next generation of cells",
     "Each new molecule carries a different sequence from the original, which keeps the information varied",
     "Replication removes the original strands, so only newly made information is transmitted",
     "Replication happens only in gametes, so hereditary information reaches offspring and nowhere else",
     "Replication joins the two daughter molecules together, so they cannot be separated at division"], ans=0,
   why="EK 6.2.A.1 states that DNA replication ensures continuity of hereditary information, and EK 6.2.A.1.ii supplies the mechanism: each original strand templates a complementary new strand, so each product reproduces the original sequence. An original strand is retained rather than removed, which is what semiconservative means."),
 dict(q="The table reports how many double-stranded DNA molecules are present after each round of replication of a single starting molecule. How many molecules will be present after four rounds?",
   table=_T_COUNT,
   choices=[
     "16 molecules",
     "8 molecules",
     "10 molecules",
     "32 molecules",
     "4 molecules"], ans=0,
   why="Each round of replication makes two molecules from every one present, which the table records as 1, 2, 4 and 8 across the first three rounds. Doubling the eight molecules present after three rounds gives 16 after the fourth."),
 dict(q="Using the same starting molecule, how many of the molecules present after four rounds of replication will contain a strand from the original molecule?",
   table=_T_COUNT,
   choices=[
     "2 molecules, because the original molecule contributed exactly two strands",
     "16 molecules, because every molecule descends from the original",
     "8 molecules, because half of the molecules always retain original DNA",
     "4 molecules, because the number of original strands doubles at each round",
     "None, because original strands are broken down after the first round"], ans=0,
   why="EK 6.2.A.1.ii keeps each original strand intact as the template for a new complementary strand, so the two strands of the starting molecule survive replication and end up in two different molecules. The table shows the number of molecules doubling each round to 16, but the number of original strands cannot grow, since replication makes new strands rather than new original ones."),
 dict(q="At one replication fork, both new strands are being built at the same time. What is the relationship between the two template strands used?",
   choices=[
     "Each of the two original strands serves as the template for one new strand",
     "One original strand serves as the template for both new strands",
     "The two original strands are joined and serve together as a single template",
     "The leading strand is copied from an original strand and the lagging strand from the leading strand",
     "Neither original strand is used, because both new strands are copied from the RNA primers"], ans=0,
   why="EK 6.2.A.1.ii states that one strand of DNA serves as the template for a new strand of complementary DNA, and it is the semiconservative outcome that requires both original strands to be used, since each of the two products keeps one of them."),
 dict(q="A researcher finds that a cell's new DNA strands contain short stretches of RNA at intervals along one strand and only at the start of the other. What accounts for the difference?",
   choices=[
     "The strand made discontinuously required a primer for each of its many segments, while the continuously made strand needed only one",
     "The strand made discontinuously is built out of RNA and the continuously made strand out of DNA",
     "The strand made discontinuously required no primer at all, so the RNA came from the template",
     "The two strands are copied in opposite directions, so one uses RNA primers and the other uses DNA primers",
     "The RNA stretches mark the places where ligase joined two fragments together"], ans=0,
   why="EK 6.2.A.1.v requires an RNA primer for DNA polymerase to initiate synthesis and EK 6.2.A.1.vi makes synthesis discontinuous on the lagging strand and continuous on the leading strand. Each separate initiation needs its own primer, so many segments mean many primers, while one continuous stretch needs one."),
 dict(q="A cell inherits a defective form of ligase. Which observation is expected in its newly replicated DNA?",
   choices=[
     "One of the two new strands consists of separate segments that have not been connected",
     "Neither new strand is started, because no primer can be laid down",
     "The two original strands remain wound together throughout the cell cycle",
     "The new DNA is built in the 3 prime to 5 prime direction instead",
     "Supercoiling accumulates ahead of the replication fork until it stops"], ans=0,
   why="EK 6.2.A.1.vii states that ligase joins the fragments on the lagging strand, so a defective ligase leaves those fragments unjoined while everything before that step proceeds. The other four observations correspond to failures of priming, helicase, the fixed direction of synthesis and topoisomerase."),
 dict(q="Which sequence of events at a replication fork is consistent with the framework's account?",
   choices=[
     "The strands are unwound, a primer is laid down, DNA polymerase extends the new strand, and fragments on one strand are joined",
     "DNA polymerase extends a new strand, the strands are then unwound, and a primer is laid down afterward",
     "Fragments are joined into a continuous strand, and only then does DNA polymerase begin to add nucleotides",
     "A primer is laid down, the primer is joined to a second primer, and the strands are unwound last",
     "The strands are unwound only after both new strands have been completed"], ans=0,
   why="The order follows from the statements themselves: helicase unwinds the strands in EK 6.2.A.1.iii to expose the template EK 6.2.A.1.ii requires, DNA polymerase needs the RNA primer of EK 6.2.A.1.v before it can extend anything, and the joining in EK 6.2.A.1.vii acts on fragments that must already exist."),
 dict(q="Why is a joining step needed on one new strand and not on the other?",
   choices=[
     "Only one of the two new strands is synthesized discontinuously, and only separate segments need joining",
     "Only one of the two new strands is made of DNA, and only DNA segments can be joined",
     "Only one of the two new strands is built in the 5 prime to 3 prime direction",
     "Only one of the two new strands is copied from an original template strand",
     "Only one of the two new strands receives an RNA primer"], ans=0,
   why="EK 6.2.A.1.vi states that DNA polymerase synthesizes new strands continuously on the leading strand and discontinuously on the lagging strand, and EK 6.2.A.1.vii gives ligase the fragments on the lagging strand. A continuous strand has no gaps to close. EK 6.2.A.1.i gives both strands the same direction of synthesis and EK 6.2.A.1.ii gives each a template."),
 dict(q="A biologist describes DNA replication as a model in which the product of each round can itself be copied in the next round. Which feature of the process makes that possible?",
   choices=[
     "Each product is a complete double-stranded molecule whose two strands can each serve as a template",
     "Each product is a single strand, which is the only form a template can take",
     "Each product contains only newly made DNA, so the original is never copied twice",
     "Each product is joined to the original molecule, so the original is copied again with it",
     "Each product is copied from an RNA primer rather than from DNA"], ans=0,
   why="EK 6.2.A.1.ii makes each product one original strand paired with one new complementary strand, so every product is itself a complete double-stranded molecule with two usable templates. That is why EK 6.2.A.1 can describe replication as ensuring continuity across generations rather than for one round only."),
 dict(q="A drug blocks topoisomerase but leaves every other participant working. What is expected at the replication fork?",
   choices=[
     "The fork opens and synthesis begins, but the DNA ahead of the fork becomes progressively more supercoiled",
     "The fork never opens, because unwinding cannot begin",
     "The fork opens normally and synthesis continues without any change",
     "The new strands are made but the fragments on one of them are never joined",
     "The new strands are built in the opposite direction to the usual one"], ans=0,
   why="EK 6.2.A.1.iv states that topoisomerase relaxes supercoiling in front of the replication fork, so its loss allows supercoiling to accumulate there while the unwinding of EK 6.2.A.1.iii and the synthesis of EK 6.2.A.1.vi still take place. Preventing the fork from opening at all would be a failure of helicase instead."),
 dict(q="Which of the following correctly matches a participant in replication with what the framework says it does?",
   choices=[
     "DNA polymerase adds nucleotides to a new strand, continuously on one strand and discontinuously on the other",
     "Ligase unwinds the two strands so that each can act as a template",
     "Helicase relaxes the supercoiling that builds up ahead of the fork",
     "Topoisomerase joins the fragments made on the lagging strand",
     "The RNA primer adds nucleotides to the new strand once synthesis is under way"], ans=0,
   why="EK 6.2.A.1.vi assigns synthesis, continuous on the leading strand and discontinuous on the lagging strand, to DNA polymerase. The other four options exchange the roles the framework gives to ligase in EK 6.2.A.1.vii, helicase in EK 6.2.A.1.iii, topoisomerase in EK 6.2.A.1.iv and the RNA primer in EK 6.2.A.1.v."),
 dict(q="A cell completes one round of replication just before dividing. What does this accomplish for the two daughter cells?",
   choices=[
     "Each daughter cell receives a complete copy of the same hereditary information",
     "Each daughter cell receives half of the hereditary information, which is restored at the next division",
     "Each daughter cell receives a different half of the original strands and no new DNA",
     "Each daughter cell receives entirely newly made DNA, and the original molecule is discarded",
     "Each daughter cell receives two copies of the hereditary information, one original and one new"], ans=0,
   why="EK 6.2.A.1 states that DNA replication ensures continuity of hereditary information, and EK 6.2.A.1.ii makes each product a faithful copy carrying one original strand. Doubling the molecules before division is what allows both daughter cells to receive the full complement rather than a share of it."),
 dict(q="Which statement about the direction of DNA synthesis is consistent with the framework?",
   choices=[
     "Both new strands are synthesized in the 5 prime to 3 prime direction, and the difference between them lies in whether synthesis is continuous",
     "Both new strands are synthesized in the 3 prime to 5 prime direction, and the difference between them lies in which enzyme builds them",
     "The leading strand is synthesized in one direction and the lagging strand in the other, which is why one needs joining",
     "The direction of synthesis reverses each time a new primer is laid down",
     "The direction of synthesis depends on which organism is replicating its DNA"], ans=0,
   why="EK 6.2.A.1.i states that DNA is synthesized in the 5 prime to 3 prime direction, with no exception for either strand, and EK 6.2.A.1.vi locates the difference between the strands in continuous against discontinuous synthesis. The framework treats the mechanism as general rather than varying by organism."),
 dict(q="An investigator finds a cell in which the number of separate DNA segments on the lagging strand keeps rising while the leading strand is finished normally. Which participant is most likely impaired?",
   choices=[
     "Ligase, whose role is to join those fragments into a continuous strand",
     "Helicase, whose role is to unwind the two strands at the fork",
     "Topoisomerase, whose role is to relax supercoiling ahead of the fork",
     "DNA polymerase, whose role is to add nucleotides to the growing strand",
     "The RNA primer, whose role is to allow synthesis to begin"], ans=0,
   why="EK 6.2.A.1.vi has DNA polymerase making the lagging strand as separate fragments, and EK 6.2.A.1.vii gives ligase the job of joining them. Fragments accumulating means they are being made but not joined, so the synthesis, unwinding, supercoiling and priming steps are all working."),
 dict(q="Why would a purely conservative model of replication fail to explain the continuity that the framework attributes to the process?",
   choices=[
     "It is not the model the framework describes, because the framework states that one original strand templates each new strand",
     "It would produce daughter molecules with different sequences from one another",
     "It would prevent the DNA from being unwound by helicase",
     "It would require synthesis to run in the 3 prime to 5 prime direction",
     "It would leave the lagging strand in fragments that ligase could not join"], ans=0,
   why="EK 6.2.A.1.ii states plainly that replication is semiconservative, meaning one strand of DNA serves as the template for a new strand of complementary DNA, and the density data in this topic show a single hybrid band after one round. The other options attribute failures to a model that the framework simply does not adopt."),
]
