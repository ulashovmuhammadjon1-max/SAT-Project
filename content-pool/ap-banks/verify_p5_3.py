"""Key verification for AP PSYCH 5.3 (Explaining and Classifying Disorders).

No computation is possible here, so for EVERY item the specific claim the key
rests on is written out: a CED definition, a named study's actual result, or
what a theory actually predicts. That statement is what replaces sympy.

Source: AP Psychology Course and Exam Description, (c) 2024 College Board,
Course Framework V.1, Topic 5.3, pp. 117-118.

THE ATTRIBUTION MOST OFTEN GOT WRONG, keyed explicitly: the DSM was developed by
the American PSYCHIATRIC Association (EK 5.3.A.3); the American PSYCHOLOGICAL
Association is a different body and is the source of the ethical principles in
Topic 5.5. The ICD is the World Health Organization's.

The seven perspectives in EK 5.3.B.2-5.3.B.8 are each keyed once from the
framework's own wording, and the two pairs that blur are separated:
  cognitive vs psychodynamic -- accessible beliefs vs unconscious material
  biopsychosocial vs diathesis-stress -- three domains vs one interaction claim

LANGUAGE: checked by eye across the module. Person-first and neutral; no
diagnosis is used as a noun for a person, and no item frames a disorder as a
moral failing. This is not decoration -- EK 5.3.A.2 makes stigma part of the
required content, so an item written carelessly would contradict the content it
is testing.

Run: python3 verify_p5_3.py
"""
import p5_3
from psych_check import check

CLAIMS = [
 ("level of dysfunction, perception of distress, and deviation from the social norm",
  "EK 5.3.A.1 names exactly these three factors. Duration, intensity, heritability "
  "and age of onset appear in individual diagnostic criteria but are not the "
  "framework's general identification factors."),

 ("level of dysfunction",
  "EK 5.3.A.1. Dysfunction concerns interference with the ordinary demands of "
  "living -- work, relationships, self-care. It is separable from distress: a "
  "person can be markedly impaired while reporting little distress."),

 ("perception of distress",
  "EK 5.3.A.1. Distress is the person's own subjective experience of their "
  "symptoms, which is why the framework calls it PERCEPTION of distress and why it "
  "is listed separately from dysfunction."),

 ("deviation from the social norm",
  "EK 5.3.A.1. Deviation is defined relative to a community's expectations, which "
  "is exactly why it varies across cultures and across time within one culture -- "
  "the property that makes the next item's point."),

 ("unusual in a given community may cause no dysfunction or distress",
  "EK 5.3.A.1 supplies THREE factors rather than one. Relying on deviation alone "
  "would classify harmless nonconformity as disorder, which is the pathway to the "
  "stigma and discrimination EK 5.3.A.2 warns about. Note the claim that social "
  "norms are identical across cultures is false on its face."),

 ("both positive and negative consequences",
  "EK 5.3.A.2: diagnosing or classifying has positive and negative consequences "
  "depending on the nature of the disorder, the individual being diagnosed, and "
  "the presence of cultural and societal norms, stigma, and discrimination. Both "
  "one-sided options misstate the framework, which is deliberately balanced here."),

 ("negative social attitudes that can lead others to devalue or avoid",
  "EK 5.3.A.2 names stigma among the negative consequences of diagnosis. Stigma is "
  "a social response to the LABEL rather than a feature of the condition, which is "
  "why it can be reduced without any change in symptoms."),

 ("stigma, racism, sexism, ageism, and discrimination",
  "EK 5.3.A.2 lists these explicitly as bearing on whether a diagnosis helps or "
  "harms. The framework treats diagnosis as a social act as well as a clinical "
  "one, and this list is the framework's own."),

 ("specialized training and the use of evidence-based diagnostic tools",
  "EK 5.3.A.3 states this directly. Worth noting alongside it: no laboratory test "
  "confirms the disorders in Topic 5.4, which is part of why trained judgment and "
  "validated instruments are required rather than optional."),

 ("American Psychiatric Association",
  "EK 5.3.A.3: the American Psychiatric Association developed the DSM. The "
  "American PSYCHOLOGICAL Association is a different organization and is the "
  "source of the ethical principles in EK 5.5.C.1 -- which is exactly why it is "
  "the distractor here, and the confusion this item exists to prevent."),

 ("World Health Organization",
  "EK 5.3.A.3: the World Health Organization developed the ICD to classify mental "
  "disorders. Pairing it against the American Psychiatric Association is the check "
  "that both attributions are held, not just one."),

 ("responsive to new research and advances in practice",
  "EK 5.3.A.3 states that these classification systems are updated regularly to be "
  "responsive to new research and practice advances. The current DSM edition is "
  "the DSM-5-TR (2022), which is itself an instance of the claim."),

 ("eclectic approach",
  "EK 5.3.B.1: most psychologists employ an eclectic approach, using more than one "
  "psychological perspective when diagnosing and treating clients. The "
  "diathesis-stress model is a causal model rather than a professional practice, "
  "so it is not an alternative answer to this question."),

 ("maladaptive learned associations",
  "EK 5.3.B.2: the behavioral perspective proposes that the causes focus on "
  "maladaptive learned associations between or among responses to stimuli."),

 ("unconscious thoughts and experiences, often developed during childhood",
  "EK 5.3.B.3, in substance verbatim. The contrast that matters is with the "
  "cognitive perspective: psychodynamic causes are by definition NOT accessible to "
  "the person, which is why 'beliefs the person could report' is the wrong answer "
  "here and the right one two items later."),

 ("lack of social support and being unable to fulfill one's potential",
  "EK 5.3.B.4, in substance verbatim: the humanistic perspective proposes the "
  "causes focus on a lack of social support and being unable to fulfill one's "
  "potential."),

 ("maladaptive thoughts, beliefs, attitudes, or emotions",
  "EK 5.3.B.5, in substance verbatim. The distinguishing feature against the "
  "psychodynamic account is accessibility: these are thoughts the person can in "
  "principle report, which is what makes them a target for the cognitive therapies "
  "in EK 5.5.D.2."),

 ("reduce the likelihood of survival",
  "EK 5.3.B.6, in substance verbatim: the evolutionary perspective proposes the "
  "causes focus on behaviors and mental processes that reduce the likelihood of "
  "survival."),

 ("maladaptive social and cultural relationships and dynamics",
  "EK 5.3.B.7, in substance verbatim. The unit of analysis is the person's social "
  "and cultural context rather than anything internal, which is what separates it "
  "from the humanistic perspective's focus on the individual's unfulfilled "
  "potential."),

 ("physiological or genetic factors",
  "EK 5.3.B.8, in substance verbatim: the biological perspective proposes the "
  "causes focus on physiological or genetic issues."),

 ("behavioral perspective",
  "EK 5.3.B.2 applied. A fear acquired by association with an aversive event and "
  "maintained by avoidance is a maladaptive learned association. The stem "
  "deliberately supplies both the acquisition and the maintenance mechanism, so no "
  "appeal to unconscious material or physiology is needed."),

 ("cognitive perspective",
  "EK 5.3.B.5 applied. Persistent beliefs about the self sustaining the symptoms "
  "is the cognitive account, and the belief is one the client can state -- the "
  "detail that rules out the psychodynamic perspective."),

 ("combination of biological, psychological, and sociocultural factors",
  "EK 5.3.C.1, in substance verbatim: the biopsychosocial model assumes any "
  "psychological problem potentially involves a combination of biological, "
  "psychological, and sociocultural factors. The single-primary-cause option is "
  "the model it was formulated against."),

 ("genetic vulnerability combined with stressful life experiences",
  "EK 5.3.C.2, in substance verbatim: disorders develop due to a genetic "
  "vulnerability (diathesis) in COMBINATION with stressful life experiences "
  "(stress). Either factor ALONE is insufficient on this model, which is why both "
  "single-factor options are wrong."),

 ("diathesis-stress model",
  "EK 5.3.C.2 applied. The siblings share the vulnerability and differ in stress "
  "exposure, and the outcomes differ accordingly. Neither factor alone predicts "
  "the difference, which is what makes this the model's signature case rather than "
  "a biological or a stress explanation."),

 ("three broad domains of contributing factors, while the diathesis-stress model specifies an interaction",
  "EK 5.3.C.1 and EK 5.3.C.2 are separate statements in the framework. One lists "
  "the domains that may contribute; the other makes a specific claim about how "
  "vulnerability and stress must combine. Treating them as the same model is the "
  "error this item corners."),

 ("independent trained clinicians reach the same diagnosis",
  "Research-methods item. Reliability is AGREEMENT; whether a diagnosis correctly "
  "identifies the condition and predicts its course is validity, a separate "
  "property. The standardized criteria in the DSM and ICD (EK 5.3.A.3) exist "
  "largely to raise this agreement."),

 ("racism, sexism, ageism, and discrimination",
  "EK 5.3.A.2 names these factors explicitly. The design described holds the case "
  "description constant and varies only demographic details, which isolates bias "
  "in the diagnostic judgment itself -- exactly the concern the framework raises."),

 ("obtain independent clinician diagnoses for the same people",
  "Research-methods item (Science Practice 2.C). Agreement with an established "
  "standard requires both measures taken on the SAME people. Re-administering the "
  "tool a week later tests consistency over time, a different property, and "
  "comparing across different samples confounds the tool with the sample."),

 ("applying the biopsychosocial model",
  "EK 5.3.C.1. Each consideration maps onto one domain: family history is "
  "biological, habitual thinking is psychological, and the lost supportive "
  "community is sociocultural. Drawing on all three at once is what makes this the "
  "model rather than any single perspective from EK 5.3.B."),
]

check(p5_3, CLAIMS)
