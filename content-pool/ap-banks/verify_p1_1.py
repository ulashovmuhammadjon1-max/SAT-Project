"""Key audit for AP PSYCHOLOGY 1.1 Interaction of Heredity and Environment.

There is no computation to verify in psychology, so the discipline that replaces
sympy is this: for every one of the 30 items, state the specific claim the key
rests on and where in the course framework it comes from -- a definition, a named
study design, or what a theory actually predicts. An assertion nobody wrote down
is exactly how a wrong key ships.

Each CLAIMS entry is (anchor, claim). `psych_check` asserts mechanically that the
anchor appears in the keyed choice and in NO distractor, so an off-by-one key or
a reordered choice list fails the check rather than shipping. It also checks the
count, choice distinctness, and -- the psychology-specific defect -- that no two
choices in one question name the same construct in different words.

FOUR choices per item (A-D): the current exam's format, confirmed from the CED
itself. See AP_PSYCH_CED.md.

Scope note: the Topic 1.1 exclusion statement puts genotype, phenotype, DNA,
chromosomes, and dominant/recessive expression outside the exam. Item 25 tests
that boundary deliberately; no other item depends on those terms.
"""
import psych_check
import p1_1

CLAIMS = [
 ("genetically predisposed characteristics",
  "EK 1.1.A.1.i defines heredity, or nature, as genetic or predisposed characteristics that influence physical, behavioral, and mental traits and processes."),
 ("external factors a person experiences",
  "EK 1.1.A.1.ii defines environmental factors, or nurture, as the external factors one experiences, giving family interactions and education as the examples."),
 ("interact, and behavior arises",
  "EK 1.1.A.1 states that heredity and environmental factors interact to shape behavior and mental processes; the framework does not treat either as sufficient alone."),
 ("interaction between hereditary predisposition",
  "A predisposition whose expression depends on experience is the textbook case of the interaction asserted in EK 1.1.A.1; it is not a purely hereditary or purely environmental account."),
 ("natural selection favors traits that increase survival",
  "EK 1.1.A.2 defines the evolutionary perspective as exploring how natural selection affects the expression of behavior and mental processes to increase survival and reproductive success."),
 ("used to discriminate against groups",
  "EK 1.1.A.2 states that some theorists sought to apply principles of the evolutionary perspective in ways that discriminate against others, naming eugenics."),
 ("program for deciding which people should reproduce",
  "The evolutionary perspective is descriptive -- it accounts for traits selection has already shaped. Eugenics converts that into a prescriptive program, which is the discriminatory misapplication EK 1.1.A.2 flags."),
 ("more genetically similar to each other than fraternal",
  "The inferential logic of a twin study, and the CED's own framing in the sample AAQ: fraternal twins are only as genetically similar as any sibling pair, so greater similarity in identical pairs implicates heredity."),
 ("biological relatives and the family members who raised them",
  "EK 1.1.A.3 lists adoption studies among the designs used to study genetic influence; the design works because rearing family and biological family are different people and can be compared separately."),
 ("share environments as well as ancestry",
  "Family studies (EK 1.1.A.3) confound relatedness with shared environment, which is why the framework pairs them with twin and adoption designs rather than relying on any one."),
 ("hereditary influence on the trait is substantial",
  "Greater similarity in the more genetically similar pairs despite less similar rearing is the pattern that implicates heredity; the reverse pattern would implicate environment."),
 ("cannot randomly assign participants to be more or less genetically related",
  "Science practice 2: an experiment requires a manipulated independent variable. Genetic relatedness and rearing family cannot be assigned, so these are correlational designs and support association only."),
 ("does not establish causation",
  "Correlation-is-not-causation, the limit the CED's own sample multiple-choice item 2 tests: a conclusion of cause and effect cannot be drawn where no independent variable was manipulated."),
 ("number of hours per week a caregiver reads aloud",
  "An operational definition specifies the measurement procedure. Hours of reading aloud is countable; 'stimulating', 'benefits', and 'quality' restate the construct without specifying how it is measured."),
 ("more likely without making it certain",
  "EK 1.1.A.1.i says predisposed characteristics *influence* traits. Influence rather than determination is what makes a predisposition different from a guaranteed outcome."),
 ("resemble the family that raises them or the family they were born to",
  "The defining feature of an adoption study is that rearing and biological families are distinct; a twin study cannot separate those unless the twins were also adopted apart."),
 ("energy-rich foods aided survival in ancestral environments",
  "EK 1.1.A.2: an evolutionary account explains a widespread behavior by the survival or reproductive advantage it conferred."),
 ("raised in different countries differ sharply",
  "A strictly hereditary account predicts similarity between genetically identical people; a large difference between identical twins reared in different settings is direct evidence of environmental influence."),
 ("treated more alike by parents and teachers",
  "A confounding variable varies along with the variable of interest and offers a rival explanation. Differential treatment of identical pairs would inflate their similarity for a reason other than ancestry."),
 ("effect of a stressful environment on the behavior is larger for people with a particular inherited predisposition",
  "A statistical interaction means the effect of one factor depends on the level of the other; that is precisely the interaction claim of EK 1.1.A.1, and a main effect alone does not demonstrate it."),
 ("rapid fear response to snakes",
  "The evolutionary perspective in psychology is applied to behavior and mental processes; height, eye color, and bone healing are physical traits outside what this perspective is invoked to explain in the course."),
 ("relationship between siblings' exercise habits, whose cause is undetermined",
  "A survey manipulates nothing, so shared ancestry and shared household both remain live explanations; the only supported conclusion is that a relationship exists."),
 ("adoption study",
  "Only this pairing states what the design can show. A twin study cannot test a drug against a placebo, a family study cannot establish that a treatment causes improvement, and naturalistic observation cannot quantify an ancestral contribution."),
 ("rather than dividing it into separate portions within one person",
  "EK 1.1.A.1 frames the two influences as interacting to shape a trait. A percentage split applied to one person's talent misreads an interaction as a partition."),
 ("which specific chromosomes carry a trait",
  "The Topic 1.1 exclusion statement places genotype, phenotype, DNA, chromosomes, and recessive/dominant gene expression outside the scope of the AP Psychology Exam."),
 ("naturalistic observation",
  "Science practice 2.A: the design is defined by recording behavior in its ordinary setting with no intervention. Nothing is manipulated, so it is not an experiment; rearing and biological families are not compared, so it is not an adoption study; more than one family is observed, so it is not a case study."),
 ("informed consent and protecting the confidentiality",
  "Science practice 2.D. A study built on identifiable adoption records turns on consent and confidentiality. The distractor promising the findings in advance describes a bias, not a safeguard, and is the one a hurried reader accepts."),
 ("direction of influence runs the opposite way",
  "A correlation constrains neither the direction of influence nor the existence of an outside cause. This objection is specifically the reverse-direction one, which is why the third-variable option -- also a real limitation of correlational data -- is wrong for THIS objection."),
 ("random sampling determines who is studied",
  "Random sampling governs who enters the study and therefore generalizability; random assignment governs which condition a participant receives and is what licenses a causal claim. Twin and adoption studies (EK 1.1.A.3) can sample randomly but can never assign randomly, which is why they stay correlational."),
 ("may not represent the wider population",
  "Generalizability, the skill the exam's Article Analysis Question tests directly, depends on whether the sample resembles the population the claim is about. Psychology students at one university differ systematically in age, education, and background from people in general."),
]

psych_check.check(p1_1, CLAIMS, per_topic=30, n_choices=4)
