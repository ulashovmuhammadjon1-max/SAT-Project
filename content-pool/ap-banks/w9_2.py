# AP WORLD HISTORY: MODERN 9.2 Technological Advances and Limitations After
# 1900: Disease
# CED effective Fall 2026 (Course Framework V.1), Unit 9 Globalization,
# c. 1900 to the present. Thematic focus: Humans and the Environment (ENV).
# Reasoning process: Continuity and Change.
#
# Learning Objective: Unit 9 Learning Objective B -- explain how environmental
# factors affected human populations over time. Disease is treated on this page
# as one of those environmental factors, which is why the topic sits under ENV
# rather than under Technology. Suggested skill 5.B, explain how a historical
# development or process relates to another historical development or process.
# That skill is the shape of this bank: most items ask how one of these
# developments stands to another -- an outbreak to the research that followed it,
# longer life to a rising incidence, a persisting disease to an emerging one --
# rather than asking what a disease is.
#
# HISTORICAL DEVELOPMENTS this topic prints, and the only sentences the keys
# below rest on:
#   KC-6.1.III    Diseases, as well as medical and scientific developments, had
#                 significant effects on populations around the world.
#   KC-6.1.III.A  Diseases associated with poverty persisted while other diseases
#                 emerged as new epidemics and threats to human populations, in
#                 some cases leading to social disruption. These outbreaks
#                 spurred technological and medical advances. Some diseases
#                 occurred at higher incidence merely because of increased
#                 longevity.
#
# KC-6.1.III.A IS THREE CLAIMS IN ONE PARAGRAPH and the whole topic turns on
# keeping them apart:
#   (a) diseases associated with poverty PERSISTED WHILE other diseases EMERGED
#       as new epidemics -- a continuity and a change at the same time, not one
#       replacing the other -- and in SOME CASES this led to social disruption;
#   (b) those outbreaks SPURRED technological and medical advances -- the
#       direction runs from the outbreak to the advance;
#   (c) some diseases occurred at higher incidence MERELY BECAUSE OF increased
#       longevity -- a rise in recorded incidence that is not a rise in danger,
#       and the subtlest thing on the page.
# Items 5, 11, 16, 21 and 26 exist to hold (c) apart from (a), because reading a
# longevity-driven rise as a new epidemic is the error this topic invites.
#
# ILLUSTRATIVE EXAMPLES the CED prints on this page, in three lists:
#   Diseases associated with poverty: malaria; tuberculosis; cholera.
#   Emergent epidemic diseases: the 1918 influenza pandemic; Ebola; HIV/AIDS.
#   Diseases associated with increased longevity: heart disease; Alzheimer's
#     disease.
# Illustrative examples are optional course content, so exactly TWO items turn on
# them and both stems say the course prints them as such.
#
# WHAT IS DELIBERATELY NOT KEYED. Epidemic disease is ground on which people
# hold strong and current views. Every key here is limited to the framework's
# descriptive sentences. No key assigns blame for an outbreak to any country,
# government or group; no key states a death toll; no key recommends or condemns
# any public health measure; and no key describes any disease as characteristic
# of any people. Where an item involves a source arguing about a disease, it asks
# what the source claims or what would test it, never whether the source is
# right.
#
# THE QUALIFIERS ARE LOAD-BEARING. "In some cases" governs social disruption,
# not every outbreak; "merely because of increased longevity" governs a specific
# and limited claim. A bank that flattened either would teach the opposite of the
# framework's own sentence.
#
# DEDUPE NOTE. Topic 9.1 covers vaccines and antibiotics under KC-6.1.I.C,
# lengthening life; this module covers disease itself and the relation between
# outbreak and advance, and it uses longer life only as KC-6.1.III.A's stated
# cause of higher recorded incidence. Topic 9.3 covers the environmental debates
# about resources and climate. Topic 9.9 reviews these sentences as
# argumentation rather than as content.
#
# SOURCES. Section I is stimulus-based and this bank cannot display an image, so
# every stimulus is TEXT and none is attributed to a real person or document.
# TABLES are hypothetical, each states a whole and its parts, and every keyed
# conclusion is recomputed from the table alone. DATES are written "1950 to
# 1990", never with a hyphen.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md; the real Section I prints four.
TOPIC = ("9.2", "Technological Advances and Limitations After 1900: Disease", 9)

_T_CASES = dict(
    headers=["Period (hypothetical record of a region's recorded cases, thousands)",
             "Cases recorded",
             "Of those, from diseases long associated with poverty",
             "Of those, from diseases newly emergent in the period"],
    rows=[["1950s", "900", "860", "40"],
          ["1970s", "850", "770", "80"],
          ["1990s", "820", "640", "180"]])

_T_AGES = dict(
    headers=["Age group (hypothetical survey of one population, thousands of persons)",
             "Persons in the group",
             "Of those, living with a condition of the kind associated with longer life",
             "Of those, not so affected"],
    rows=[["Under 40", "500", "10", "490"],
          ["40 to 64", "300", "45", "255"],
          ["65 and over", "200", "90", "110"]])

_T_PROGRAMMES = dict(
    headers=["Decade (hypothetical record of new medical research programmes)",
             "New programmes begun",
             "Of those, begun within two years of a recorded outbreak",
             "Of those, not so begun"],
    rows=[["1950s", "40", "22", "18"],
          ["1970s", "65", "39", "26"],
          ["1990s", "110", "71", "39"]])

QUESTIONS = [

 dict(q="A hypothetical regional health report of 1985 notes that the illnesses filling its clinics include both a long-familiar infection of the poorest districts and a disease unknown in the region twenty years earlier. According to this course, the report describes",
   choices=[
     "diseases associated with poverty persisting while other diseases emerged as new epidemics",
     "diseases associated with poverty disappearing as new epidemic diseases replaced them",
     "new epidemic diseases disappearing as diseases associated with poverty replaced them",
     "the elimination of both kinds of disease by medical and scientific advance",
     "the confinement of both kinds of disease to a single district of the region"],
   ans=0,
   why="KC-6.1.III.A states that diseases associated with poverty PERSISTED WHILE other diseases emerged as new epidemics and threats to human populations. The framework describes a continuity and a change running at the same time rather than one kind of disease displacing the other, which is why the key names both halves in the framework's own relation."),

 dict(q="This course states that the outbreaks of new epidemic diseases had a further consequence beyond their effects on populations. What was it?",
   choices=[
     "They spurred technological and medical advances",
     "They halted technological and medical research for the duration of each outbreak",
     "They caused diseases associated with poverty to disappear",
     "They reduced the average length of human life across the whole century",
     "They led governments to abandon the collection of health statistics"],
   ans=0,
   why="KC-6.1.III.A states that these outbreaks spurred technological and medical advances. The direction of the relation runs from the outbreak to the advance, which is the connection skill 5.B asks a student to explain, and none of the other consequences appears in the framework's sentence."),

 dict(q="A hypothetical record divides a region's recorded cases in each period into two groups. Which conclusion does the table alone support?",
   table=_T_CASES,
   choices=[
     "Cases from diseases long associated with poverty appear in every period, while cases from newly emergent diseases rise across the record",
     "Cases from diseases long associated with poverty disappear from the record entirely",
     "Cases from newly emergent diseases fall across the record",
     "The total number of cases recorded rose in each period after the first",
     "In every period more cases come from newly emergent diseases than from diseases associated with poverty"],
   ans=0,
   why="KC-6.1.III.A states that diseases associated with poverty persisted while other diseases emerged as new epidemics, which is a continuity and a change at once. The record is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="An epidemiologist's note of 1990 observes that a certain condition is diagnosed far more often than it was fifty years earlier, and that this is because far more people now reach the ages at which it appears. According to this course, this is an instance of",
   choices=[
     "a disease occurring at higher incidence merely because of increased longevity",
     "a disease emerging as a new epidemic threat to human populations",
     "a disease associated with poverty persisting in a population",
     "an outbreak spurring technological and medical advance",
     "the elimination of a disease by medical and scientific development"],
   ans=0,
   why="KC-6.1.III.A states that some diseases occurred at higher incidence MERELY BECAUSE OF increased longevity. The framework distinguishes that kind of rise from the emergence of a new epidemic, and the note supplies the framework's own explanation, that more people now reach the ages at which the condition appears."),

 dict(q="Two developments are set beside each other: a severe outbreak in one decade and a new class of treatments developed in the years after it. What relation does this course draw between them?",
   choices=[
     "The outbreak spurred the advance, running from the disease to the response",
     "The advance spurred the outbreak, running from the response to the disease",
     "The two are unrelated developments that happened to occur in sequence",
     "The advance preceded the outbreak and made it more severe",
     "Neither is treated by the framework as bearing on populations at all"],
   ans=0,
   why="KC-6.1.III.A states that these outbreaks spurred technological and medical advances, fixing the outbreak as prior and the advance as the response. Reversing that order is the characteristic error, so the key names the direction as well as the two terms, which is what skill 5.B's relation of one process to another requires."),

 dict(q="This course prints certain diseases as illustrative examples of diseases associated with poverty. Which list is the one the course prints?",
   choices=[
     "Malaria, tuberculosis, and cholera",
     "The 1918 influenza pandemic, Ebola, and HIV/AIDS",
     "Heart disease and Alzheimer's disease",
     "Vaccines, antibiotics, and modern methods of birth control",
     "Deforestation, desertification, and declining air quality"],
   ans=0,
   why="The CED prints malaria, tuberculosis and cholera beside KC-6.1.III.A as illustrative examples of diseases associated with poverty. The second list is the same page's examples of emergent epidemic diseases and the third its examples of diseases associated with increased longevity, while the remaining lists belong to KC-6.1.I.C, KC-6.1.III.B and KC-6.1.II.A."),

 dict(q="A student writes that this course says every outbreak of a new epidemic disease produced social disruption. What is the best correction?",
   choices=[
     "The framework says such outbreaks led to social disruption in some cases, not in every case",
     "The framework says such outbreaks never led to social disruption in any case",
     "The framework says no new epidemic diseases emerged during this period",
     "The framework says social disruption preceded the outbreaks rather than following them",
     "The framework says social disruption occurred only where diseases of poverty had been eliminated"],
   ans=0,
   why="KC-6.1.III.A states that other diseases emerged as new epidemics and threats to human populations, IN SOME CASES leading to social disruption. The qualifier is the framework's own and it rules out the universal claim as well as the opposite absolute, so the correction has to preserve the middle position."),

 dict(q="A hypothetical survey divides each age group of one population into two parts. Which conclusion does the table alone support?",
   table=_T_AGES,
   choices=[
     "The share living with such a condition rises with each older age group recorded",
     "The share living with such a condition falls with each older age group recorded",
     "No person recorded under 40 is living with a condition of that kind",
     "The number of persons recorded in each group rises with the age of the group",
     "The share living with such a condition is above half in every age group recorded"],
   ans=0,
   why="KC-6.1.III.A states that some diseases occurred at higher incidence merely because of increased longevity, and a condition whose prevalence climbs with age is what makes a longer-lived population record more of it. The survey is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="According to this course, what effects did diseases, together with medical and scientific developments, have?",
   choices=[
     "Significant effects on populations around the world",
     "Effects confined to a single continent and to a single century",
     "No measurable effects on any population during this period",
     "Effects on governments and their institutions but not on populations",
     "Effects that were limited to the years before 1900"],
   ans=0,
   why="KC-6.1.III states that diseases, as well as medical and scientific developments, had significant effects on populations around the world. The framework pairs the diseases with the responses to them and states that the effects were both significant and worldwide."),

 dict(q="A public health administrator argues in 1995 that because the incidence of a certain condition has risen sharply, an epidemic must be under way. What consideration from this course would most directly qualify that inference?",
   choices=[
     "Some conditions occur at higher incidence merely because more people live to the ages at which they appear",
     "Some conditions occur at lower incidence when populations grow older on average",
     "New epidemic diseases never produce a rise in recorded incidence",
     "Diseases associated with poverty cannot rise in incidence at any time",
     "Recorded incidence is unrelated to the number of people in a population"],
   ans=0,
   why="KC-6.1.III.A states that some diseases occurred at higher incidence MERELY BECAUSE OF increased longevity, which is a rise that is not the emergence of a new epidemic. Skill 5.B asks how one development relates to another, and the relation between an ageing population and a rising count is what the administrator's inference leaves out."),

 dict(q="An unattributed medical journal editorial of 1925 argues that the great respiratory epidemic of the previous decade taught its profession more about contagion than the preceding fifty years had. According to this course, the editorial describes",
   choices=[
     "an outbreak spurring technological and medical advance",
     "a disease associated with poverty persisting in a population",
     "a disease occurring at higher incidence because of increased longevity",
     "the elimination of epidemic disease by scientific development",
     "the confinement of an epidemic disease to a single social class"],
   ans=0,
   why="KC-6.1.III.A states that these outbreaks spurred technological and medical advances, and the CED prints the 1918 influenza pandemic among its illustrative examples of emergent epidemic diseases. An editorial reporting that an epidemic taught the profession about contagion is that spur described from inside the profession."),

 dict(q="Which pair of developments does this course present as running at the same time rather than one after the other?",
   choices=[
     "The persistence of diseases associated with poverty, and the emergence of new epidemic diseases",
     "The emergence of new epidemic diseases, and the elimination of diseases associated with poverty",
     "The elimination of all epidemic disease, and the lengthening of human life",
     "The disappearance of medical research, and the spread of new epidemics",
     "The end of population growth, and the rise of new epidemic threats"],
   ans=0,
   why="KC-6.1.III.A states that diseases associated with poverty PERSISTED WHILE other diseases emerged as new epidemics, and the word while is what makes the two simultaneous rather than sequential. The framework nowhere states that diseases of poverty were eliminated, which is what each distractor supposes."),

 dict(q="A hypothetical record divides the new research programmes of each decade into two groups. Which conclusion does the table alone support?",
   table=_T_PROGRAMMES,
   choices=[
     "The number of new programmes rose in each decade, and in every decade most began within two years of a recorded outbreak",
     "In every decade most new programmes began without a recorded outbreak in the preceding two years",
     "The number of new programmes fell in each decade after the first one recorded",
     "No programme recorded in the 1950s began within two years of an outbreak",
     "The three decades recorded the same number of new programmes as one another"],
   ans=0,
   why="KC-6.1.III.A states that these outbreaks spurred technological and medical advances, and research programmes clustering after outbreaks are one form that spur takes. The record is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="Beside its statement that some diseases occurred at higher incidence merely because of increased longevity, this course prints two illustrative examples. Which are they?",
   choices=[
     "Heart disease and Alzheimer's disease",
     "Malaria, tuberculosis, and cholera",
     "Ebola and HIV/AIDS",
     "Deforestation and desertification",
     "Vaccines and antibiotics"],
   ans=0,
   why="The CED prints heart disease and Alzheimer's disease beside KC-6.1.III.A as illustrative examples of diseases associated with increased longevity, which is the sentence about higher incidence arising merely because more people reach the relevant ages. The other lists are the same page's examples of diseases of poverty and of emergent epidemics, or belong to other topics."),

 dict(q="In a hypothetical case, a government's statistical office reports that deaths from a long-standing infectious disease of the poorest districts have not fallen over thirty years, while deaths from a disease first recorded in the region ten years ago have risen. This pattern is best described by this course as",
   choices=[
     "a continuity in one kind of disease alongside a change in another",
     "a change in one kind of disease that eliminated the other",
     "a continuity in both kinds of disease with no change in either",
     "a change in both kinds of disease with no continuity in either",
     "a pattern the framework treats as impossible to observe"],
   ans=0,
   why="KC-6.1.III.A states that diseases associated with poverty persisted while other diseases emerged as new epidemics, which is a continuity and a change side by side. The reasoning process the CED prints beside this topic is continuity and change, and the report is that process observed in one region's figures."),

 dict(q="A demographer argues that a country's rising count of a particular chronic condition should be read as a consequence of its success in extending life rather than as a new threat. According to this course, this argument",
   choices=[
     "is available within the framework, which states that some diseases occurred at higher incidence merely because of increased longevity",
     "is unavailable within the framework, which treats every rise in incidence as a new epidemic",
     "is unavailable within the framework, which denies that human life lengthened during the period",
     "is available within the framework, which states that longer life reduced the incidence of every disease",
     "is unavailable within the framework, which treats chronic conditions as diseases of poverty"],
   ans=0,
   why="KC-6.1.III.A states that some diseases occurred at higher incidence merely because of increased longevity, which is exactly the reading the demographer proposes. KC-6.1.I.C in the adjacent topic supplies the lengthening of life, so the framework supports both halves of the argument."),

 dict(q="Why does this course place disease under the theme of humans and the environment rather than under technology alone?",
   choices=[
     "Because it treats disease as an environmental factor affecting human populations over time",
     "Because it treats disease as a form of technology developed by human societies",
     "Because it treats disease as a subject of government policy rather than of biology",
     "Because it treats disease as unrelated to human populations",
     "Because it treats disease as confined to the years before industrialization"],
   ans=0,
   why="Unit 9 Learning Objective B, printed on this topic's page, is to explain how environmental factors affected human populations over time, and the thematic focus the CED prints beside it is Humans and the Environment. KC-6.1.III then states that diseases had significant effects on populations around the world, which is that objective's subject matter."),

 dict(q="Which statement about disease in this period is NOT supported by this course?",
   choices=[
     "Diseases associated with poverty were eliminated as new epidemic diseases emerged",
     "Diseases associated with poverty persisted during this period",
     "Other diseases emerged as new epidemics and threats to human populations",
     "Outbreaks spurred technological and medical advances",
     "Some diseases occurred at higher incidence because more people lived longer"],
   ans=0,
   why="KC-6.1.III.A states that diseases associated with poverty PERSISTED while other diseases emerged, so their elimination is the claim the framework does not support. The item asks which statement is NOT supported, so the key is deliberately the false one; the other four restate parts of KC-6.1.III.A."),

 dict(q="An unattributed relief agency bulletin of 1972 reports that a waterborne infection continues to appear each year in districts without piped water, while it has not been seen for a decade in districts that have it. The bulletin bears most directly on which of this course's statements?",
   choices=[
     "That diseases associated with poverty persisted through this period",
     "That new epidemic diseases emerged as threats to human populations",
     "That some diseases occurred at higher incidence merely because of increased longevity",
     "That outbreaks spurred technological and medical advances",
     "That the release of greenhouse gases contributed to debates about climate change"],
   ans=0,
   why="KC-6.1.III.A states that diseases associated with poverty persisted, and a waterborne infection recurring only where piped water is absent is that association and that persistence in one document. The CED prints cholera among its illustrative examples of diseases associated with poverty."),

 dict(q="A researcher wants to test the claim that a particular rise in recorded cases reflects an ageing population rather than a new threat. Which evidence would bear most directly on the claim?",
   choices=[
     "The incidence of the condition within each age group, compared across the same years",
     "The total number of cases recorded in the country each year",
     "The number of hospitals built in the country over the same years",
     "The number of research papers published about the condition",
     "The country's total consumption of petroleum over the same years"],
   ans=0,
   why="KC-6.1.III.A states that some diseases occurred at higher incidence MERELY BECAUSE OF increased longevity, a claim about the composition of the population rather than about the disease. Incidence held constant within each age group while the population ages is what would establish it, and a bare total cannot distinguish the two explanations."),

 dict(q="Two regions record the same new epidemic disease. In one it produces widespread disruption of ordinary life; in the other it does not. How does this course's framework accommodate both?",
   choices=[
     "It states that such outbreaks led to social disruption in some cases rather than in all",
     "It states that such outbreaks always led to social disruption",
     "It states that such outbreaks never led to social disruption",
     "It states that new epidemic diseases appeared in only one region of the world",
     "It states that social disruption occurred only where no outbreak had taken place"],
   ans=0,
   why="KC-6.1.III.A states that other diseases emerged as new epidemics and threats to human populations, IN SOME CASES leading to social disruption. A framework using some rather than all or none is one that both regions fit, so the key names the qualifier together with the alternative it excludes."),

 dict(q="An unattributed laboratory annual report of 1988 states that the year's largest new programme was established in direct response to a disease first identified a few years earlier. This course would treat the report as evidence for",
   choices=[
     "the relation in which outbreaks spurred technological and medical advances",
     "the relation in which technological advances spurred outbreaks",
     "the persistence of diseases associated with poverty in poorer districts",
     "the rise in incidence of conditions associated with longer life",
     "the effects of energy technologies on the production of material goods"],
   ans=0,
   why="KC-6.1.III.A states that these outbreaks spurred technological and medical advances, and a research programme established in direct response to a recently identified disease is that relation documented by the laboratory itself. The reversed relation is the tempting misreading, so the key names the direction."),

 dict(q="What does this course say, in its own words, about the diseases it describes as emergent?",
   choices=[
     "They emerged as new epidemics and threats to human populations, in some cases leading to social disruption",
     "They replaced the diseases associated with poverty wherever they appeared",
     "They occurred at higher incidence merely because of increased longevity",
     "They were eliminated by medical advances within a decade of appearing",
     "They had no significant effect on any population during this period"],
   ans=0,
   why="KC-6.1.III.A states that other diseases emerged as new epidemics and threats to human populations, in some cases leading to social disruption. The key restates the framework's sentence and no more of it: it names no country, no group of people and no death toll, because the framework names none."),

 dict(q="How does this course relate the emergence of new diseases to the state of medical knowledge?",
   choices=[
     "It presents the outbreaks as having spurred the technological and medical advances that followed",
     "It presents medical knowledge as having been unaffected by any outbreak",
     "It presents medical advances as having produced the outbreaks that followed them",
     "It presents medical knowledge as having declined over the course of the century",
     "It presents the two as belonging to different centuries and therefore unrelated"],
   ans=0,
   why="KC-6.1.III.A states that these outbreaks spurred technological and medical advances. Skill 5.B, the suggested skill for this topic, asks a student to explain how one development or process relates to another, and the framework's own sentence fixes both the pair and the direction between them."),

 dict(q="A history of medicine argues that the twentieth century saw both remarkable advance and persistent failure in the control of disease. Which pair of the framework's statements best supports that double claim?",
   choices=[
     "That outbreaks spurred technological and medical advances, and that diseases associated with poverty persisted",
     "That outbreaks spurred advances, and that all diseases associated with poverty were eliminated",
     "That no advances were made, and that diseases associated with poverty persisted",
     "That new epidemic diseases never emerged, and that advances continued regardless",
     "That advances eliminated every disease, and that no disease persisted anywhere"],
   ans=0,
   why="KC-6.1.III.A supplies both halves in one paragraph: outbreaks spurred technological and medical advances, and diseases associated with poverty persisted. Skill 5.B asks a student to relate one development to another, and the double claim holds precisely because the framework asserts the advance and the persistence together."),

 dict(q="An unattributed insurance actuary's memorandum of 1993 explains that its firm now expects to pay more claims for conditions of later life than it did a generation earlier, and attributes this to how many more policyholders now reach those ages. The memorandum illustrates",
   choices=[
     "a higher incidence arising merely because of increased longevity",
     "a new epidemic disease emerging as a threat to a population",
     "a disease associated with poverty persisting in a population",
     "an outbreak spurring a technological and medical advance",
     "a decline in the effects of disease on populations around the world"],
   ans=0,
   why="KC-6.1.III.A states that some diseases occurred at higher incidence merely because of increased longevity, and an actuary attributing more claims to more policyholders reaching the relevant ages gives the framework's own reason. The framework distinguishes this from the emergence of a new epidemic, which is the distractor it is set against."),

 dict(q="Which question about a rise in a country's recorded cases of a disease would this course's framework treat as the first one to settle?",
   choices=[
     "Whether the rise reflects a new threat or a population in which more people reach the relevant ages",
     "Whether the country's government published the figures in its own language",
     "Whether the disease was first described inside or outside the country",
     "Whether the country's total population is larger than that of its neighbours",
     "Whether the figures were printed in a book or in a periodical"],
   ans=0,
   why="KC-6.1.III.A distinguishes diseases emerging as new epidemics and threats from diseases occurring at higher incidence merely because of increased longevity, and those are two different explanations of the same rising number. Skill 5.B asks how one development relates to another, and which of the two relations holds is what a rising count leaves open."),

 dict(q="An unattributed municipal report of 1961 argues that the city's disease problem will be solved by economic growth alone. Which consideration from this course would most directly complicate that argument?",
   choices=[
     "New diseases emerged as epidemics during this period alongside the diseases associated with poverty",
     "Diseases associated with poverty had already been eliminated everywhere by 1961",
     "Medical and scientific developments had no effect on populations in this period",
     "Recorded incidence of disease cannot be measured in an urban population",
     "Economic growth is not treated by the framework as bearing on anything"],
   ans=0,
   why="KC-6.1.III.A states that diseases associated with poverty persisted WHILE other diseases emerged as new epidemics and threats to human populations. An argument that addresses only the first kind leaves the second unaccounted for, which is the complication the framework's own conjunction supplies."),

 dict(q="Considered across this topic, what makes disease in the twentieth century a story of both continuity and change?",
   choices=[
     "Old diseases of poverty continued while new epidemics appeared and some conditions rose merely because people lived longer",
     "Old diseases of poverty ended and nothing new appeared to take their place",
     "Nothing about disease altered at any point during the century",
     "Every disease known in 1900 had been eliminated by the century's end",
     "Disease affected governments and institutions but left populations unchanged"],
   ans=0,
   why="KC-6.1.III.A gives the continuity in the persistence of diseases associated with poverty and the change in the emergence of new epidemics, and adds a third element, the higher incidence arising merely from increased longevity. The reasoning process the CED prints beside this topic is continuity and change, and the key carries all three of those strands."),

 dict(q="Taking the topic as a whole, which single sentence best states what this course says about disease after 1900?",
   choices=[
     "Diseases of poverty persisted while new epidemics emerged and sometimes disrupted societies, those outbreaks drove medical and technological advance, and some conditions grew more common simply because more people lived to an age at which they appear",
     "Disease ceased to affect populations once medical and scientific development began in the twentieth century",
     "New epidemic diseases replaced the diseases of poverty, and no advance in medicine followed from either",
     "Every rise in the recorded incidence of a disease in this period represented the emergence of a new epidemic",
     "Disease affected populations only in the years before 1900 and had no bearing on the twentieth century"],
   ans=0,
   why="KC-6.1.III states that diseases and the medical and scientific developments answering them had significant effects on populations around the world, and KC-6.1.III.A supplies the persistence, the emergence, the social disruption in some cases, the spur to advance, and the higher incidence arising merely from increased longevity. The key is the conjunction of those and each distractor contradicts at least one."),
]
