# AP PSYCHOLOGY 1.1 Interaction of Heredity and Environment — 25 questions
# CED effective Fall 2024/2025, Unit 1 Biological Bases of Behavior.
# Learning objective 1.1.A; essential knowledge 1.1.A.1 (heredity/"nature" and
# environmental factors/"nurture", and their interaction), 1.1.A.2 (the
# evolutionary perspective, natural selection, and the misuse of evolutionary
# principles in eugenics), 1.1.A.3 (twin, family, and adoption studies).
#
# FOUR choices (A-D). The current AP Psychology exam uses four options, not the
# five of the pre-2024 exam -- see AP_PSYCH_CED.md in this directory.
#
# Exclusion statement on 1.1: genotype, phenotype, DNA, chromosomes, and
# dominant/recessive gene expression are outside the scope of the exam, so no
# question here turns on them. "Heritability" as a statistic does not appear in
# the CED either and is never the key.
#
# Every key's grounding claim is stated item by item in verify_p1_1.py.
TOPIC = ("1.1", "Interaction of Heredity and Environment", 1)
QUESTIONS = [
 dict(q="In psychology, heredity — the \"nature\" side of the nature-and-nurture question — refers to", choices=[
   "genetically predisposed characteristics that influence physical, behavioral, and mental traits",
   "the external circumstances a person encounters, such as schooling and family interactions",
   "the deliberate choices a person makes about how to behave in a given situation",
   "the cultural expectations a society places on people of a particular age"], ans=0,
   why="The CED defines heredity, or nature, as the genetic or predisposed characteristics that influence physical, behavioral, and mental traits and processes."),
 dict(q="Environmental factors, the \"nurture\" side of the nature-and-nurture question, are best described as", choices=[
   "the external factors a person experiences, such as family interactions or education",
   "inherited predispositions that are present from conception onward",
   "the physical structures of the brain and nervous system",
   "reflexes that appear in the same form in every healthy newborn"], ans=0,
   why="Nurture refers to the external factors one experiences, family interactions and education being the CED's own examples."),
 dict(q="Which statement best represents how contemporary psychology understands the relationship between heredity and environment?", choices=[
   "Heredity and environmental factors interact, and behavior arises from that interaction",
   "Heredity determines behavior, and environmental factors merely delay its expression",
   "Environmental factors determine behavior, and heredity is relevant only to physical traits",
   "Heredity governs mental processes while environmental factors govern observable behavior"], ans=0,
   why="EK 1.1.A.1 states that heredity and environmental factors interact to shape behavior and mental processes; the course rejects the either/or framing."),
 dict(q="A researcher argues that a tendency toward anxiety is inherited but that whether it becomes a persistent problem depends on how stressful a person's early home life is. This argument is an example of", choices=[
   "an interaction between hereditary predisposition and environmental experience",
   "a purely evolutionary account of anxiety",
   "the claim that anxiety is entirely learned",
   "the claim that early experience has no measurable effect on temperament"], ans=0,
   why="A predisposition whose expression depends on experience is exactly the heredity-environment interaction described in EK 1.1.A.1."),
 dict(q="The evolutionary perspective in psychology explains behavior and mental processes primarily in terms of", choices=[
   "how natural selection favors traits that increase survival and reproductive success",
   "how unconscious conflicts formed in early childhood shape adult personality",
   "how rewards and punishments in the immediate environment shape responses",
   "how a person interprets and organizes incoming sensory information"], ans=0,
   why="EK 1.1.A.2 defines the evolutionary perspective as exploring how natural selection affects the expression of behavior and mental processes to increase survival and reproductive success."),
 dict(q="Eugenics is best described as", choices=[
   "an application of evolutionary principles used to discriminate against groups of people",
   "a research method for separating hereditary from environmental influences",
   "the study of how hormones outside the nervous system affect behavior",
   "a therapy that changes behavior by altering a person's environment"], ans=0,
   why="EK 1.1.A.2 notes that some theorists sought to apply evolutionary principles in ways that discriminate against others, which is what eugenics names."),
 dict(q="Why is eugenics treated in the AP Psychology course as a misuse of the evolutionary perspective rather than an extension of it?", choices=[
   "It converts a descriptive account of natural selection into a program for deciding which people should reproduce",
   "It relies on twin studies, which cannot say anything about inherited traits",
   "It assumes that natural selection operates on populations rather than individuals",
   "It denies that behavior has any hereditary component at all"], ans=0,
   why="The evolutionary perspective describes how selection has shaped existing traits; eugenics turns that description into a prescriptive program about who should reproduce, which is the discriminatory application the CED flags."),
 dict(q="Researchers compare pairs of identical twins with pairs of fraternal twins on a trait. The logic of this design rests on the fact that", choices=[
   "identical twins are more genetically similar to each other than fraternal twins are",
   "identical twins are always raised in more similar environments than fraternal twins",
   "fraternal twins share no more genetic similarity than two unrelated people",
   "identical twins are the only siblings who can be studied from birth"], ans=0,
   why="Twin studies work because identical pairs are more genetically alike than fraternal pairs, who are only as genetically similar as any sibling pair; a larger similarity in identical pairs points toward hereditary influence."),
 dict(q="An adoption study examines the influence of heredity and environment by comparing adopted children with", choices=[
   "both their biological relatives and the family members who raised them",
   "children of the same age who were never adopted",
   "their own scores measured at two different ages",
   "a group of identical twins reared together"], ans=0,
   why="EK 1.1.A.3 lists adoption studies as a method for separating hereditary from environmental influence; the comparison that does the separating is adopted children against biological relatives on one side and rearing family on the other."),
 dict(q="A family study finds that a trait appears more often among close relatives of a person who has the trait than among distant relatives. By itself, this finding is difficult to interpret because", choices=[
   "close relatives tend to share environments as well as ancestry",
   "family studies cannot measure a trait in more than one person",
   "distant relatives share no ancestry with the person studied",
   "the number of relatives available is always too small to analyze"], ans=0,
   why="Family studies confound relatedness with shared environment, which is why the CED pairs them with twin and adoption designs rather than treating any one method as sufficient."),
 dict(q="A researcher reports that identical twins raised apart are more similar in a trait than fraternal twins raised together. This pattern most directly supports the conclusion that", choices=[
   "hereditary influence on the trait is substantial",
   "the trait is entirely determined by the rearing environment",
   "shared rearing environment is the single largest influence on the trait",
   "the trait cannot be measured reliably"], ans=0,
   why="Greater similarity in the more genetically similar pairs despite less similar environments points to hereditary influence, which is the reason twin studies are used at all."),
 dict(q="Twin, family, and adoption studies are all correlational rather than experimental designs. The reason is that", choices=[
   "the researcher cannot randomly assign participants to be more or less genetically related",
   "the researcher never measures more than one variable in these designs",
   "these studies use samples that are too small for an experiment",
   "these studies always take place outside of a laboratory"], ans=0,
   why="An experiment requires the researcher to manipulate the independent variable; genetic relatedness and rearing family cannot be assigned, so these designs can establish association but not causation."),
 dict(q="A news article states that because a trait runs in families, having that family background causes the trait. The clearest flaw in this reasoning is that", choices=[
   "a relationship observed without a manipulated variable does not establish causation",
   "traits that run in families are always caused by the environment instead",
   "correlations among relatives cannot be calculated",
   "the article should have reported a mean rather than a relationship"], ans=0,
   why="Nothing was manipulated and nothing was randomly assigned, so the observed association supports a claim of relationship only, the correlation-is-not-causation limit that applies to every heredity study in this topic."),
 dict(q="Which of the following is an operational definition of \"early environmental enrichment\" suitable for a developmental study?", choices=[
   "the number of hours per week a caregiver reads aloud to the child",
   "the degree to which the child's home life is stimulating",
   "how much the child benefits from being at home",
   "the overall quality of the child's upbringing"], ans=0,
   why="An operational definition states the specific, countable procedure used to measure a variable; hours of reading aloud per week can be recorded, whereas the other options restate the construct in equally vague words."),
 dict(q="In studies of the interaction of heredity and environment, the phrase \"predisposition\" is best understood to mean", choices=[
   "an inherited tendency that makes an outcome more likely without making it certain",
   "a guarantee that a trait will appear regardless of experience",
   "a habit acquired through repeated practice",
   "a temporary physical state produced by a drug"], ans=0,
   why="Heredity in the CED is described as predisposed characteristics that influence traits; influence, not determination, is what distinguishes a predisposition from a guaranteed outcome."),
 dict(q="Which research question is best answered with an adoption study rather than a twin study?", choices=[
   "Do children come to resemble the family that raises them or the family they were born to?",
   "Do two people who share more ancestry respond more similarly to a stressor?",
   "Does a drug reduce anxiety more than a placebo does?",
   "How many hours of sleep does the average adolescent get?"], ans=0,
   why="An adoption study is defined by the fact that rearing family and biological family are different people, which is precisely what the first question compares."),
 dict(q="A psychologist studying whether a preference for sweet foods was shaped by natural selection would most likely argue that the preference", choices=[
   "was favored because energy-rich foods aided survival in ancestral environments",
   "is learned entirely through advertising in the modern food industry",
   "reflects an unconscious conflict originating in early childhood",
   "results from a hormone released only during adolescence"], ans=0,
   why="The evolutionary perspective explains a widespread behavior by the survival or reproductive advantage it conferred, per EK 1.1.A.2."),
 dict(q="Which finding would most weaken a strictly hereditary explanation of a behavior?", choices=[
   "Identical twins raised in different countries differ sharply on the behavior",
   "Identical twins raised together are highly similar on the behavior",
   "The behavior appears in every human culture ever studied",
   "Close relatives resemble each other on the behavior more than distant relatives do"], ans=0,
   why="A strictly hereditary account predicts similarity in genetically identical people; a sharp difference between identical twins reared in different settings is evidence of environmental influence."),
 dict(q="In a study of the nature-and-nurture question, which of the following would be a confounding variable when comparing identical twins raised together with fraternal twins raised together?", choices=[
   "identical twins may be treated more alike by parents and teachers than fraternal twins are",
   "identical twins share more ancestry than fraternal twins do",
   "the trait is measured with the same instrument in both groups",
   "the two groups are the same average age"], ans=0,
   why="A confounding variable is one that differs along with the variable of interest and offers a rival explanation; more similar treatment of identical pairs would inflate their similarity for a non-hereditary reason."),
 dict(q="A psychologist claims that a behavior is \"the product of nature and nurture in interaction.\" The strongest evidence for this claim would be a finding that", choices=[
   "the effect of a stressful environment on the behavior is larger for people with a particular inherited predisposition",
   "the behavior is more common in relatives of people who show it",
   "the behavior appears at the same age in every culture",
   "the behavior can be produced in the laboratory by a reward"], ans=0,
   why="An interaction means the effect of one factor depends on the level of the other, which is exactly what a larger environmental effect in one predisposed group demonstrates."),
 dict(q="Which of the following is the clearest example of the evolutionary perspective being applied to a mental process rather than to a physical trait?", choices=[
   "explaining a rapid fear response to snakes as an advantage in ancestral environments",
   "explaining differences in adult height as the result of inherited growth patterns",
   "explaining eye color differences among populations",
   "explaining why a bone heals faster in children than in adults"], ans=0,
   why="A fear response is a behavioral and mental process; the other options concern physical traits, which the evolutionary perspective in psychology is not primarily invoked to explain."),
 dict(q="Researchers survey 500 pairs of adult siblings about how often they exercise and find that siblings resemble one another. Which conclusion is supported?", choices=[
   "There is a relationship between siblings' exercise habits, whose cause is undetermined",
   "Shared ancestry causes siblings to exercise at similar rates",
   "Growing up in the same household causes siblings to exercise at similar rates",
   "Exercise habits are unrelated to family background"], ans=0,
   why="A survey manipulates nothing, so it supports a statement of relationship; ancestry and shared household remain rival explanations and neither can be selected over the other from this design."),
 dict(q="Which pair correctly matches a research method with what it is best suited to reveal?", choices=[
   "adoption study — whether children resemble the family that raised them or the one they were born to",
   "twin study — whether a drug changes behavior more than a placebo does",
   "family study — whether a treatment causes an improvement in symptoms",
   "naturalistic observation — the exact proportion of a trait attributable to ancestry"], ans=0,
   why="Only the adoption pairing states what that design can actually show; the others attribute causal or quantitative conclusions to designs that cannot support them."),
 dict(q="A teacher says, \"Musical talent is 60 percent inherited, so practice matters only for the other 40 percent.\" The best objection is that", choices=[
   "hereditary and environmental influences act together on a trait rather than dividing it into separate portions within one person",
   "musical talent has never been studied in twins",
   "practice has been shown to have no effect on musical performance",
   "inherited influences on behavior have never been demonstrated"], ans=0,
   why="EK 1.1.A.1 frames heredity and environment as interacting to shape a trait, not as carving up an individual's trait into independent shares."),
 dict(q="Which of the following would a psychologist studying the interaction of heredity and environment be LEAST likely to investigate, according to the AP Psychology course framework?", choices=[
   "which specific chromosomes carry a trait",
   "whether adopted children resemble their biological relatives",
   "whether identical twins are more alike than fraternal twins",
   "whether a stressful home environment amplifies an inherited tendency"], ans=0,
   why="The exclusion statement on Topic 1.1 places chromosomes, along with DNA, genotype, phenotype, and dominant/recessive expression, outside the scope of the exam."),
 dict(q="A psychologist sits in a public park and records how often parents and toddlers make eye contact, without approaching anyone or changing anything about the setting. This research design is", choices=[
   "naturalistic observation",
   "an experiment",
   "an adoption study",
   "a case study of one family"], ans=0,
   why="Naturalistic observation is defined by recording behavior in its ordinary setting without intervening; nothing is manipulated, no group is assigned, and more than one family is watched."),
 dict(q="A researcher plans to obtain adoption agency records in order to compare adopted adults with their biological relatives. Which safeguard is most necessary for the study to meet ethical standards?", choices=[
   "obtaining informed consent and protecting the confidentiality of the records",
   "guaranteeing in advance that the findings will support the hypothesis",
   "concealing from participants that a study is taking place at all",
   "excluding anyone who has ever met a biological relative"], ans=0,
   why="Science practice 2.D concerns whether a research scenario followed appropriate ethical procedures, and consent plus confidentiality are the safeguards a study using identifiable personal records requires."),
 dict(q="A study finds that more anxious parents have more anxious children. A second researcher points out that anxious children may make their parents more anxious, rather than the reverse. This objection identifies", choices=[
   "the possibility that the direction of influence runs the opposite way",
   "a confounding third variable that causes both",
   "a failure to operationally define anxiety",
   "an unrepresentative sample"], ans=0,
   why="A correlation is consistent with influence running either way; this specific objection concerns direction of influence, not an outside variable, a definition, or a sample."),
 dict(q="Which statement correctly distinguishes random sampling from random assignment?", choices=[
   "random sampling determines who is studied; random assignment determines which condition a participant is placed in",
   "random sampling determines which condition a participant is placed in; random assignment determines who is studied",
   "the two terms describe the same procedure at different stages of a study",
   "random sampling is used only in experiments and random assignment only in surveys"], ans=0,
   why="Random sampling concerns who is in the study and therefore generalizability; random assignment concerns group equivalence and is what permits a causal conclusion. Twin and adoption studies can sample randomly but can never assign randomly."),
 dict(q="A large twin study recruits every participant from a single university's psychology courses and concludes that its findings describe people in general. The strongest objection is that", choices=[
   "the sample may not represent the wider population, so the findings may not generalize",
   "twins cannot be used to study hereditary influence",
   "the study has no measured outcome",
   "recruiting participants from one place turns the study into an experiment"], ans=0,
   why="Generalizability depends on whether the sample resembles the population the claim is about, and psychology students at one university differ systematically in age, education, and background from people in general."),
]
