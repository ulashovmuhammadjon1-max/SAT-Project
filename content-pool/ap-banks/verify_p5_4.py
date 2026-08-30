"""Key verification for AP PSYCH 5.4 (Selection of Categories of Disorders).

No computation is possible here, so for EVERY item the specific claim the key
rests on is written out: a CED definition, a named study's actual result, or
what a theory actually predicts. That statement is what replaces sympy.

Source: AP Psychology Course and Exam Description, (c) 2024 College Board,
Course Framework V.1, Topic 5.4, pp. 119-124.

THE FOUR DISCRIMINATIONS THIS TOPIC LIVES OR DIES ON, each keyed by an item and
each with the reversal supplied as a distractor:
  * positive vs negative symptoms -- ADDED experience vs ABSENT behavior.
    "Positive" never means beneficial. Catatonia is the one symptom that can
    fall either way (excitement positive, stupor negative).
  * delusion vs hallucination -- false BELIEF vs false PERCEPTION.
  * bipolar vs depressive -- the presence of a manic episode moves the
    diagnosis to the bipolar category no matter how much of the history is
    depressive. Bipolar I takes a full manic episode; Bipolar II takes
    hypomania plus major depression and no full manic episode.
  * OCD vs generalized anxiety disorder -- specific obsessions paired with
    compulsions that address them, vs prolonged NONSPECIFIC anxiety with no
    such rituals. They are separate categories in this framework, and
    obsessive-compulsive PERSONALITY disorder is a third, distinct condition
    sitting in Cluster C.

SCOPE: the CED prints an exclusion statement at the head of this topic -- the
exam focuses on the disorders listed in 5.4 and no others. Checked by eye: no
item keys on a disorder outside that list.

LANGUAGE: person-first and clinically neutral, verified by reading. No diagnosis
is used as a noun for a person, no symptom is described sensationally, and no
item invites a judgment about character. EK 5.3.A.2 makes stigma required
content, so a carelessly written item would contradict the material it tests.

Run: python3 verify_p5_4.py
"""
import p5_4
from psych_check import check

CLAIMS = [
 ("onset occurs during the developmental period",
  "EK 5.4.A.1: neurodevelopmental disorders have onset during the developmental "
  "period, and symptoms focus on whether the person is exhibiting behaviors "
  "appropriate for their age or maturity range. The age-appropriateness standard "
  "is part of the definition, not an afterthought."),

 ("persistent inattention and/or hyperactivity-impulsivity",
  "EK 5.4.A.1 names ADHD and autism spectrum disorder as the two in scope. ADHD's "
  "core features are inattention and/or hyperactivity-impulsivity; ASD's are "
  "differences in social communication together with restricted, repetitive "
  "patterns. The reversed pairing is the trap."),

 ("environmental, physiological, or genetic",
  "EK 5.4.A.2, in substance verbatim. Both 'entirely genetic' and 'entirely "
  "environmental' overstate the framework, and the parenting-style option is a "
  "discredited claim the framework does not make -- one that caused real harm to "
  "families historically, which is why it is worth naming as wrong rather than "
  "merely omitting."),

 ("delusions, hallucinations, disorganized thinking or speech, disorganized motor behavior, and negative symptoms",
  "EK 5.4.B.1 names exactly these five areas. Each distractor imports a feature "
  "from a different category in Topic 5.4 -- compulsions, dissociation, mania, "
  "phobias, binge eating -- which is what makes them plausible."),

 ("presence of experiences or behaviors not typically present",
  "EK 5.4.B.1.i-iii classify delusions, hallucinations, and disorganized speech as "
  "POSITIVE symptoms. Positive means ADDED, not beneficial. The 'improve "
  "functioning' option is the misreading this item exists to prevent, and it is a "
  "common one because the everyday sense of the word points the wrong way."),

 ("lack of a behavior that is typically present",
  "EK 5.4.B.1.v: negative symptoms present as the lack of a typical behavior, such "
  "as the lack of emotional expression or lack of movement. Negative means "
  "SUBTRACTED, not unpleasant -- the mirror of the previous item's misreading."),

 ("false beliefs",
  "EK 5.4.B.1.i: delusions are false BELIEFS, are positive symptoms, and may "
  "manifest as delusions of persecution or grandeur. The false-perception option "
  "defines hallucinations, and belief/perception is the pair most often reversed "
  "on this content."),

 ("false perceptions",
  "EK 5.4.B.1.ii: hallucinations are false PERCEPTIONS, are positive symptoms, and "
  "may involve one or more of the senses. Checked in the opposite direction from "
  "the delusion item on purpose, so a reversal cannot pass both. Note the "
  "framework does not restrict hallucinations to hearing."),

 ("word salad",
  "EK 5.4.B.1.iii: disorganized thinking or speech is a positive symptom and may "
  "manifest as speaking in a word salad -- stringing together words in nonsensical "
  "ways. It is a positive symptom because speech is added, however incoherent."),

 ("catatonic excitement is an added behavior, while catatonic stupor is the absence",
  "EK 5.4.B.1.iv: catatonia may be experienced as excitement (a positive symptom "
  "manifestation) or stupor (a negative symptom manifestation). It is the one "
  "symptom in the category that can fall on either side, which is precisely why "
  "the framework spells both out."),

 ("negative symptoms",
  "EK 5.4.B.1.v names lack of emotional expression and lack of movement as "
  "negative symptoms. The stem describes behaviors typically present that are "
  "reduced or absent, with nothing added -- which is the test."),

 ("genetic or biological link, such as prenatal virus exposure",
  "EK 5.4.B.2: possible causes suggest a genetic or biological link, such as "
  "prenatal virus exposure or imbalances with certain neurotransmitters -- the "
  "dopamine hypothesis. Note the framework claims no single causal gene, and does "
  "not endorse the parenting explanation offered as a distractor."),

 ("sad, empty, or irritable mood",
  "EK 5.4.C.1, in substance verbatim: depressive disorders are characterized by "
  "sad, empty, or IRRITABLE mood along with physical and cognitive changes "
  "affecting the ability to function. Irritable mood being included matters "
  "clinically, since a person may never describe themselves as sad."),

 ("continues over a much longer span of time",
  "EK 5.4.C.1 names major depressive disorder and persistent depressive disorder "
  "as the two in scope. The distinction is CHRONICITY -- persistent depressive "
  "disorder is defined by long-standing depressed mood rather than discrete "
  "episodes. Mania appearing in either would move the diagnosis out of the "
  "depressive category entirely, which is why that distractor is wrong."),

 ("periods of mania and periods of depression",
  "EK 5.4.D.1: bipolar disorders are characterized by periods of mania and periods "
  "of depression, with cycling that can last various amounts of time. The "
  "'continuous depressed mood with no elevated periods' option is the depressive "
  "category."),

 ("Bipolar I involves at least one full manic episode",
  "EK 5.4.D.1 names Bipolar I and Bipolar II as the two in scope. The "
  "discriminator is the SEVERITY of the elevated-mood episode: a full manic "
  "episode places the diagnosis in Bipolar I, while hypomania together with major "
  "depression and no full manic episode places it in Bipolar II. Neither disorder "
  "is 'only depression' or 'only mania', which is what the second option gets "
  "wrong."),

 ("bipolar disorder rather than a depressive disorder, because an episode of elevated mood is present",
  "EK 5.4.C.1 versus 5.4.D.1, and the single most consequential distinction in "
  "this topic. A week of elevated mood, reduced need for sleep, and impulsive "
  "disruptive decisions is a manic episode, and its presence moves the diagnosis "
  "to the bipolar category REGARDLESS of how much of the history is depressive. "
  "Counting depressive periods, as the second option invites, is exactly the error."),

 ("excessive fear and/or anxiety with related disturbances to behavior",
  "EK 5.4.E.1, in substance verbatim. Worth flagging: in the current framework "
  "obsessive-compulsive disorders (5.4.F) and trauma and stressor-related "
  "disorders (5.4.H) are SEPARATE categories, not subtypes of anxiety disorders "
  "as older material often has them."),

 ("particular object or situation",
  "EK 5.4.E.1.i: specific phobia involves fear or anxiety toward a SPECIFIC object "
  "or situation, with acrophobia and arachnophobia given as examples. The three "
  "distractors are precise definitions of social anxiety disorder, agoraphobia, "
  "and generalized anxiety disorder, so the item discriminates all four."),

 ("public transportation, being in open or enclosed spaces",
  "EK 5.4.E.1.ii lists exactly these situations. What links them is that escape "
  "may be difficult or help unavailable, which is what distinguishes agoraphobia "
  "from a specific phobia (one object) and from social anxiety disorder (fear of "
  "evaluation)."),

 ("unanticipated, overwhelming biological, cognitive, and emotional experiences of fear",
  "EK 5.4.E.1.iii, in substance verbatim, with the framework stressing that the "
  "attacks are UNANTICIPATED -- which is what separates panic disorder from a "
  "phobia, where the trigger is known. The framework also names ataque de nervios, "
  "experienced mainly by people of Caribbean or Iberian descent, as a culturally "
  "specific presentation."),

 ("intense fear of being judged or watched by others",
  "EK 5.4.E.1.iv, verbatim in substance. The framework adds that social anxiety "
  "disorder is distinct from but may include agoraphobia, and names taijin "
  "kyofusho -- experienced mainly by Japanese people, involving fear that one's "
  "body is unpleasing or offensive to others -- as a culturally specific "
  "presentation."),

 ("prolonged experiences of nonspecific anxiety",
  "EK 5.4.E.1.v: generalized anxiety disorder involves prolonged experiences of "
  "NONSPECIFIC anxiety or fear. The absence of a particular trigger is the "
  "defining feature and is what separates it from every other anxiety disorder in "
  "scope -- and from OCD, per the item two later."),

 ("obsessions, which are intrusive thoughts, together with compulsions",
  "EK 5.4.F.1 defines the category by obsessions (intrusive thoughts) AND "
  "compulsions (intrusive, often repetitive, behaviors intended to address the "
  "obsessions). The functional link between them is what makes it OCD rather than "
  "either feature alone."),

 ("specific intrusive thoughts are paired with repetitive behaviors performed to address them",
  "EK 5.4.E.1.v versus EK 5.4.F.1. Generalized anxiety disorder is prolonged and "
  "NONSPECIFIC; OCD is specific obsessions paired with compulsions that address "
  "them. Two traps are ruled out by the distractors: generalized anxiety disorder "
  "obviously does involve anxiety, and obsessive-compulsive PERSONALITY disorder "
  "is a third and separate condition sitting in Cluster C (EK 5.4.J.1.iii)."),

 ("persistent difficulty parting with possessions",
  "EK 5.4.F.1 names hoarding disorder alongside OCD as the two conditions in "
  "scope for this category. The distractors describe bulimia nervosa, dissociative "
  "amnesia, and social anxiety disorder, all of which are in scope elsewhere."),

 ("inability to recall important personal information, which with fugue includes unexpected travel",
  "EK 5.4.G.1 names dissociative amnesia (with and without fugue) and dissociative "
  "identity disorder as the two in scope, and describes the category as "
  "dissociations from consciousness, memory, identity, emotion, perception, and "
  "behavior. EK 5.4.G.2 attributes possible causes to the experience of trauma or "
  "stress. The reversed pairing is the trap."),

 ("exposure to a traumatic or stressful event",
  "EK 5.4.H.1: trauma and stressor-related disorders are characterized by exposure "
  "to a traumatic or stressful event with subsequent psychological distress, and "
  "the framework lists hypervigilance, severe anxiety, flashbacks, insomnia, "
  "emotional detachment, and hostility. Posttraumatic stress disorder is the only "
  "disorder in scope in this category."),

 ("restriction of intake leading to significantly low body weight",
  "EK 5.4.I.1 names anorexia nervosa and bulimia nervosa as the two in scope and "
  "describes the category as altered consumption or absorption of food impairing "
  "health or psychological functioning. The reversed pairing is the trap. EK "
  "5.4.I.2 attributes possible causes to biological, genetic, social, cultural, "
  "behavioral, or cognitive sources -- so no single-cause account is licensed."),

 ("Cluster A is odd or eccentric, Cluster B is dramatic, emotional, or erratic, and Cluster C is anxious or fearful",
  "EK 5.4.J.1.i-iii, in the framework's own words. Cluster A holds paranoid, "
  "schizoid, and schizotypal; Cluster B holds antisocial, histrionic, narcissistic, "
  "and borderline; Cluster C holds avoidant, dependent, and obsessive-compulsive "
  "personality disorders. The stem carries EK 5.4.J.1's full definition -- "
  "enduring, deviating from one's culture, pervasive and inflexible, beginning by "
  "early adulthood, stable, causing distress or impairment -- so every element of "
  "the definition is stated even though the question turns on the clusters."),
]

check(p5_4, CLAIMS)
