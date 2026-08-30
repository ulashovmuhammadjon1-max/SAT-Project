# AP PSYCH 5.3 Explaining and Classifying Psychological Disorders — 30 questions
# Required content: CED (c) 2024 College Board, Course Framework V.1, pp. 117-118.
# EK 5.3.A.1 level of dysfunction, perception of distress, and deviation from the
#   social norm as the factors used to identify psychological disorders;
# EK 5.3.A.2 the positive and negative consequences of diagnosis, including
#   stigma, racism, sexism, ageism, and discrimination;
# EK 5.3.A.3 diagnosis requires specialized training and evidence-based tools;
#   the DSM (American Psychiatric Association) and the ICD (World Health
#   Organization), both updated regularly;
# EK 5.3.B.1 the eclectic approach; 5.3.B.2-5.3.B.8 the behavioral,
#   psychodynamic, humanistic, cognitive, evolutionary, sociocultural, and
#   biological perspectives on the causes of disorders;
# EK 5.3.C.1 the biopsychosocial model; EK 5.3.C.2 the diathesis-stress model.
#
# LANGUAGE: person-first and neutral throughout, consistent with DSM-5-TR
# practice and with EK 5.3.A.2's own concern about stigma. No item uses a
# diagnosis as a noun for a person, and none frames a disorder as a moral failing
# or a person as defined by a diagnosis. The current edition of the DSM is the
# DSM-5-TR (2022); the CED refers to the manual generically as the DSM.
#
# No sympy: every key's claim is stated item by item in verify_p5_3.py.
TOPIC = ("5.3", "Explaining and Classifying Psychological Disorders", 5)
QUESTIONS = [
 dict(q="Which three factors does the framework identify as used to determine whether behavior and mental processes constitute a psychological disorder?", choices=[
   "heritability, age of onset, and response to medication",
   "the person's intelligence, income, and education",
   "level of dysfunction, perception of distress, and deviation from the social norm",
   "duration, intensity, and frequency of the behavior"
], ans=2,
   why="EK 5.3.A.1 names exactly these three: level of dysfunction, perception of distress, and deviation from the social norm."),

 dict(q="A person's long-standing difficulty maintaining employment, relationships, and self-care because of persistent symptoms most directly reflects which of the three factors?", choices=[
   "deviation from the social norm",
   "duration of symptoms",
   "level of dysfunction",
   "perception of distress"
], ans=2,
   why="EK 5.3.A.1. Dysfunction concerns interference with the ordinary demands of living -- work, relationships, self-care -- rather than how the person feels about it or how unusual it is."),

 dict(q="A person who describes their symptoms as deeply upsetting and difficult to bear is reporting which of the three factors?", choices=[
   "perception of distress",
   "level of dysfunction",
   "deviation from the social norm",
   "an evidence-based diagnostic criterion unique to the DSM"], ans=0,
   why="EK 5.3.A.1. Distress is the person's own subjective experience of their symptoms, which is why a person can be highly distressed while still functioning, or impaired while reporting little distress."),

 dict(q="Behavior judged unusual because it departs sharply from what a community expects reflects which of the three factors?", choices=[
   "perception of distress",
   "the biopsychosocial model",
   "deviation from the social norm",
   "level of dysfunction"
], ans=2,
   why="EK 5.3.A.1. Deviation is defined relative to a community's expectations, which is exactly why it varies across cultures and across time within a culture."),

 dict(q="Why is deviation from the social norm, by itself, an inadequate basis for identifying a psychological disorder?", choices=[
   "Behavior that is unusual in a given community may cause no dysfunction or distress at all",
   "Social norms are identical in every culture, so the criterion adds nothing",
   "Unusual behavior is always a sign of a disorder, making the criterion redundant",
   "Deviation cannot be observed or measured in any way"], ans=0,
   why="EK 5.3.A.1 supplies three factors rather than one. Relying on deviation alone would classify harmless nonconformity as disorder, which is the pathway to the stigma and discrimination EK 5.3.A.2 warns about."),

 dict(q="The framework notes that diagnosing or classifying psychological disorders", choices=[
   "has both positive and negative consequences, depending on the disorder, the person, and the social context",
   "has only benefits, since it always leads to appropriate treatment",
   "has only costs, since a label never helps a person",
   "has no consequences beyond the clinical record"], ans=0,
   why="EK 5.3.A.2: diagnosing or classifying has positive AND negative consequences depending on the nature of the disorder, the individual being diagnosed, and the presence of cultural and societal norms, stigma, and discrimination."),

 dict(q="Stigma associated with a psychological disorder is best described as", choices=[
   "the amount of distress the person reports experiencing",
   "negative social attitudes that can lead others to devalue or avoid a person who has been diagnosed",
   "the physiological symptoms that accompany the disorder",
   "the accuracy with which a clinician applies diagnostic criteria"
], ans=1,
   why="EK 5.3.A.2 names stigma among the negative consequences of diagnosis. Stigma is a social response to the label rather than a feature of the condition itself, which is why it can be reduced without the symptoms changing."),

 dict(q="The framework specifically warns that the consequences of diagnosis can be shaped by", choices=[
   "the season in which the diagnosis is made",
   "the alphabetical position of the disorder in the manual",
   "the length of the diagnostic interview alone",
   "stigma, racism, sexism, ageism, and discrimination"
], ans=3,
   why="EK 5.3.A.2 lists these explicitly as factors bearing on whether a diagnosis helps or harms, which is why the framework treats diagnosis as a social act as well as a clinical one."),

 dict(q="According to the framework, diagnosing psychological disorders requires", choices=[
   "the agreement of the person's family members",
   "specialized training and the use of evidence-based diagnostic tools",
   "only a checklist that any observer can apply",
   "a laboratory test that confirms the diagnosis biologically"
], ans=1,
   why="EK 5.3.A.3 states this directly. Note that no laboratory test confirms the disorders in Topic 5.4, which is part of why trained judgment and validated instruments are necessary."),

 dict(q="The Diagnostic and Statistical Manual of Mental Disorders (DSM) was developed by", choices=[
   "the World Health Organization",
   "the American Psychological Association",
   "the United States Department of Education",
   "the American Psychiatric Association"
], ans=3,
   why="EK 5.3.A.3 states that the American Psychiatric Association developed the DSM. The American PSYCHOLOGICAL Association is a different body and is the source of the ethical principles in Topic 5.5, which makes it the trap here."),

 dict(q="The International Classification of Mental Disorders (ICD) was developed by", choices=[
   "the World Health Organization",
   "the American Psychiatric Association",
   "the United Nations Educational, Scientific and Cultural Organization",
   "the National Institute of Mental Health"], ans=0,
   why="EK 5.3.A.3 states that the World Health Organization developed the ICD to classify mental disorders."),

 dict(q="Why does the framework describe both the DSM and the ICD as being updated regularly?", choices=[
   "Because the manuals expire after a fixed period",
   "So the classifications remain responsive to new research and advances in practice",
   "Because the number of disorders is required by law to increase each decade",
   "So that each edition can use entirely different disorder names"
], ans=1,
   why="EK 5.3.A.3 states that these classification systems are updated regularly to be responsive to new research and practice advances. The current edition of the DSM is the DSM-5-TR, published in 2022."),

 dict(q="A clinician who draws on more than one psychological perspective when understanding and treating a client is using", choices=[
   "a projective assessment",
   "the medical model exclusively",
   "an eclectic approach",
   "the diathesis-stress model"
], ans=2,
   why="EK 5.3.B.1: most psychologists employ an eclectic approach, using more than one psychological perspective when diagnosing and treating clients."),

 dict(q="The behavioral perspective locates the causes of psychological disorders in", choices=[
   "physiological or genetic abnormalities",
   "a lack of social support and unfulfilled potential",
   "maladaptive learned associations among stimuli and responses",
   "unconscious conflicts formed in childhood"
], ans=2,
   why="EK 5.3.B.2: the behavioral perspective proposes that the causes of mental disorders focus on maladaptive learned associations between or among responses to stimuli."),

 dict(q="The psychodynamic perspective locates the causes of psychological disorders in", choices=[
   "unconscious thoughts and experiences, often developed during childhood",
   "maladaptive beliefs the person could report if asked",
   "cultural dynamics outside the individual",
   "learned associations between stimuli and responses"], ans=0,
   why="EK 5.3.B.3, in substance verbatim. The contrast with the cognitive perspective matters: cognitive causes are thoughts the person can in principle access, psychodynamic causes are not."),

 dict(q="The humanistic perspective locates the causes of psychological disorders in", choices=[
   "genetic vulnerability interacting with stress",
   "maladaptive learned associations",
   "unconscious conflict from early life",
   "a lack of social support and being unable to fulfill one's potential"
], ans=3,
   why="EK 5.3.B.4, in substance verbatim: the humanistic perspective proposes the causes focus on a lack of social support and being unable to fulfill one's potential."),

 dict(q="The cognitive perspective locates the causes of psychological disorders in", choices=[
   "unconscious material inaccessible to the person",
   "the physiological functioning of the nervous system",
   "the social and cultural relationships surrounding the person",
   "maladaptive thoughts, beliefs, attitudes, or emotions"
], ans=3,
   why="EK 5.3.B.5, in substance verbatim. The distinguishing feature against the psychodynamic account is that these thoughts and beliefs are accessible, which is what makes them a target for cognitive therapy in Topic 5.5."),

 dict(q="The evolutionary perspective locates the causes of psychological disorders in", choices=[
   "the person's reinforcement history",
   "maladaptive beliefs about the self and the future",
   "the structure of the family the person grew up in",
   "behaviors and mental processes that reduce the likelihood of survival"
], ans=3,
   why="EK 5.3.B.6, in substance verbatim: the evolutionary perspective proposes the causes focus on behaviors and mental processes that reduce the likelihood of survival."),

 dict(q="The sociocultural perspective locates the causes of psychological disorders in", choices=[
   "genetic and physiological abnormalities",
   "unconscious conflicts developed in childhood",
   "an inability to fulfill one's individual potential",
   "maladaptive social and cultural relationships and dynamics"
], ans=3,
   why="EK 5.3.B.7, in substance verbatim. The unit of analysis is the person's social and cultural context rather than anything internal to the individual."),

 dict(q="The biological perspective locates the causes of psychological disorders in", choices=[
   "maladaptive thoughts and beliefs",
   "cultural dynamics and social relationships",
   "learned associations between stimuli",
   "physiological or genetic factors"
], ans=3,
   why="EK 5.3.B.8, in substance verbatim: the biological perspective proposes the causes focus on physiological or genetic issues."),

 dict(q="A clinician who suggests that a client's persistent fear of driving began after a serious collision and was maintained by consistently avoiding cars is reasoning from which perspective?", choices=[
   "the behavioral perspective",
   "the psychodynamic perspective",
   "the evolutionary perspective",
   "the biological perspective"], ans=0,
   why="EK 5.3.B.2. A fear acquired by association with an aversive event and maintained by avoidance is a maladaptive learned association -- the behavioral account, stated without appeal to unconscious material or physiology."),

 dict(q="A clinician who emphasizes that a client's symptoms are sustained by persistent beliefs that any setback proves they are worthless is reasoning from which perspective?", choices=[
   "the cognitive perspective",
   "the sociocultural perspective",
   "the humanistic perspective",
   "the behavioral perspective"], ans=0,
   why="EK 5.3.B.5. Maladaptive beliefs about the self are the cognitive account. They are beliefs the client can state, which is what separates this from the psychodynamic perspective."),

 dict(q="The biopsychosocial model assumes that a psychological problem", choices=[
   "is best explained by genetic factors alone",
   "arises only from a person's social environment",
   "potentially involves a combination of biological, psychological, and sociocultural factors",
   "has one primary cause that careful assessment will identify"
], ans=2,
   why="EK 5.3.C.1, in substance verbatim: the biopsychosocial model assumes any psychological problem potentially involves a combination of biological, psychological, and sociocultural factors."),

 dict(q="The diathesis-stress model assumes that psychological disorders develop from", choices=[
   "a genetic vulnerability combined with stressful life experiences",
   "stressful life experiences alone, regardless of vulnerability",
   "genetic vulnerability alone, regardless of experience",
   "the absence of social support in adulthood"], ans=0,
   why="EK 5.3.C.2, in substance verbatim: the diathesis-stress model assumes disorders develop due to a genetic vulnerability (diathesis) in COMBINATION with stressful life experiences (stress). Either factor alone is insufficient on this model."),

 dict(q="Two siblings share a family history of a disorder. One experiences a period of severe stress and develops symptoms; the other does not encounter comparable stress and remains well. This pattern is best explained by", choices=[
   "an eclectic approach to treatment",
   "the diathesis-stress model",
   "the behavioral perspective",
   "the evolutionary perspective"
], ans=1,
   why="EK 5.3.C.2. The shared vulnerability and the differing stress exposure together account for the differing outcome, which is precisely the interaction the model describes; neither factor alone would predict the difference."),

 dict(q="What is the clearest difference between the biopsychosocial model and the diathesis-stress model?", choices=[
   "The two are different names for the same model",
   "The biopsychosocial model names three broad domains of contributing factors, while the diathesis-stress model specifies an interaction between vulnerability and stress",
   "The biopsychosocial model concerns only biology, while the diathesis-stress model concerns only stress",
   "The biopsychosocial model applies to adults and the diathesis-stress model to children"
], ans=1,
   why="EK 5.3.C.1 and 5.3.C.2 are separate statements. One is a framework listing the domains that may contribute; the other is a specific interaction claim about how vulnerability and stress combine."),

 dict(q="Interrater reliability in diagnosis refers to", choices=[
   "the extent to which independent trained clinicians reach the same diagnosis for the same person",
   "the extent to which a diagnosis predicts a person's future symptoms",
   "the number of criteria a person must meet for a diagnosis",
   "how distressing a person finds receiving a diagnosis"], ans=0,
   why="Research-methods item. Reliability is agreement; whether the diagnosis correctly identifies the condition and predicts its course is validity, a separate property. Standardized criteria in the DSM and ICD exist largely to raise this agreement."),

 dict(q="A study finds that clinicians shown identical case descriptions assign different diagnoses depending on the demographic details attached to the case. This finding is most relevant to which of the framework's cautions?", choices=[
   "that most psychologists use an eclectic approach",
   "that the DSM and ICD were developed by different organizations",
   "that diagnostic consequences can be shaped by racism, sexism, ageism, and discrimination",
   "that classification systems are updated regularly"
], ans=2,
   why="EK 5.3.A.2 names these factors explicitly. Holding the case description constant while varying only demographics isolates bias in the diagnostic judgment, which is the concern the framework raises."),

 dict(q="A researcher wants to establish whether a new brief screening tool agrees with diagnoses made by trained clinicians. The most appropriate design would be to", choices=[
   "administer the tool and obtain independent clinician diagnoses for the same people, then compare the two sets of results",
   "administer the tool twice to the same people a week apart",
   "ask people whether they found the tool easy to complete",
   "compare the tool's results across two entirely different samples"], ans=0,
   why="Research-methods item (Science Practice 2.C). Agreement with an established standard requires both measures on the SAME people. Re-administering the tool tests consistency over time, which is a different property, and ease of completion tests neither."),

 dict(q="A clinician considers a client's family history of the disorder, the client's habitual patterns of thinking, and the loss of a supportive community after a recent move. This approach is best described as", choices=[
   "using deviation from the social norm as the sole diagnostic criterion",
   "applying the evolutionary perspective alone",
   "applying the biopsychosocial model",
   "applying the behavioral perspective alone"
], ans=2,
   why="EK 5.3.C.1. Each of the three considerations maps onto one of the model's domains: family history is biological, habitual thinking is psychological, and the lost community is sociocultural -- which is what makes this the model rather than any single perspective."),
]
