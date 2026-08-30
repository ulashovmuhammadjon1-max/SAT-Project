# AP PSYCH 5.4 Selection of Categories of Psychological Disorders — 30 questions
# Required content: CED (c) 2024 College Board, Course Framework V.1, pp. 119-124.
# EK 5.4.A neurodevelopmental (ADHD, autism spectrum disorder);
# EK 5.4.B schizophrenic spectrum -- delusions, hallucinations, disorganized
#   thinking or speech, disorganized motor behavior, negative symptoms;
# EK 5.4.C depressive (major depressive, persistent depressive);
# EK 5.4.D bipolar (Bipolar I, Bipolar II);
# EK 5.4.E anxiety (specific phobia, agoraphobia, panic disorder, social anxiety
#   disorder, generalized anxiety disorder);
# EK 5.4.F obsessive-compulsive and related (OCD, hoarding disorder);
# EK 5.4.G dissociative (dissociative amnesia with and without fugue,
#   dissociative identity disorder);
# EK 5.4.H trauma and stressor-related (posttraumatic stress disorder);
# EK 5.4.I feeding and eating (anorexia nervosa, bulimia nervosa);
# EK 5.4.J personality disorders and their three clusters.
#
# The CED prints an exclusion statement at the head of this topic: the exam
# focuses on the disorders listed in 5.4 and no others. No item here keys on a
# disorder outside that list.
#
# LANGUAGE: person-first and clinically neutral throughout, consistent with
# DSM-5-TR practice and with EK 5.3.A.2's treatment of stigma as required
# content. No diagnosis is used as a noun for a person; no symptom is described
# in sensational terms; no item invites a judgment about a person's character.
#
# No sympy: every key's claim is stated item by item in verify_p5_4.py.
TOPIC = ("5.4", "Selection of Categories of Psychological Disorders", 5)
QUESTIONS = [
 dict(q="Neurodevelopmental disorders are distinguished as a category by the fact that", choices=[
   "they always resolve completely before adolescence",
   "their onset occurs during the developmental period, and symptoms concern whether behavior is appropriate for the person's age or maturity",
   "they can only be diagnosed after a person reaches adulthood",
   "they are caused exclusively by events occurring after birth"
], ans=1,
   why="EK 5.4.A.1: neurodevelopmental disorders have onset during the developmental period, and symptoms focus on whether the person is exhibiting behaviors appropriate for their age or maturity range."),

 dict(q="Which pair correctly matches the two neurodevelopmental disorders in scope with their core features?", choices=[
   "ADHD -- recurrent unexpected panic attacks; autism spectrum disorder -- difficulty discarding possessions",
   "ADHD -- disorganized speech; autism spectrum disorder -- alternating periods of mania and depression",
   "ADHD -- persistent inattention and/or hyperactivity-impulsivity; autism spectrum disorder -- persistent differences in social communication together with restricted, repetitive patterns of behavior or interests",
   "ADHD -- restricted, repetitive patterns of behavior; autism spectrum disorder -- persistent inattention and hyperactivity"
], ans=2,
   why="EK 5.4.A.1 names attention-deficit/hyperactivity disorder and autism spectrum disorder as the two neurodevelopmental disorders in scope. The reversed pairing is the trap; the remaining options import features from other categories entirely."),

 dict(q="According to the framework, possible causes of neurodevelopmental disorders", choices=[
   "are known to be entirely genetic",
   "are known to be entirely environmental",
   "have been established as resulting from parenting style",
   "may be environmental, physiological, or genetic in nature"
], ans=3,
   why="EK 5.4.A.2 states that possible causes may be environmental, physiological, or genetic. The parenting-style option is a discredited claim the framework does not make and which caused real harm historically."),

 dict(q="Schizophrenic spectrum disorders are characterized by difficulties in one or more of which five areas?", choices=[
   "delusions, compulsions, dissociation, mania, and negative symptoms",
   "hallucinations, phobias, obsessions, hypervigilance, and flat affect",
   "delusions, hallucinations, binge eating, fugue states, and mania",
   "delusions, hallucinations, disorganized thinking or speech, disorganized motor behavior, and negative symptoms"
], ans=3,
   why="EK 5.4.B.1 names exactly these five areas. Compulsions, dissociation, mania, phobias and binge eating each belong to a different category in Topic 5.4."),

 dict(q="Positive symptoms of a schizophrenic spectrum disorder are best described as", choices=[
   "the absence of behaviors that are typically present",
   "symptoms that improve a person's day-to-day functioning",
   "symptoms that respond well to treatment",
   "the presence of experiences or behaviors not typically present"
], ans=3,
   why="EK 5.4.B.1.i-iii classify delusions, hallucinations, and disorganized speech as positive symptoms. Positive means ADDED, not beneficial -- the misreading this item exists to prevent."),

 dict(q="Negative symptoms of a schizophrenic spectrum disorder are best described as", choices=[
   "the presence of unusual experiences not typically present",
   "symptoms that make a person's outlook pessimistic",
   "symptoms that appear only after treatment begins",
   "the lack of a behavior that is typically present"
], ans=3,
   why="EK 5.4.B.1.v: negative symptoms present as the LACK of a typical behavior, such as the lack of emotional expression or lack of movement. Negative means subtracted, not unpleasant."),

 dict(q="Delusions are best defined as", choices=[
   "false beliefs, which may take forms such as delusions of persecution or of grandeur",
   "false perceptions occurring without an external stimulus",
   "repetitive behaviors performed to reduce anxiety",
   "gaps in memory for important personal information"], ans=0,
   why="EK 5.4.B.1.i: delusions are false BELIEFS and are positive symptoms, and may manifest as delusions of persecution or grandeur. The false-perception option defines hallucinations, the pairing most often reversed."),

 dict(q="Hallucinations are best defined as", choices=[
   "intrusive unwanted thoughts a person tries to suppress",
   "sudden unexpected surges of intense fear",
   "false perceptions, which may involve one or more of the senses",
   "false beliefs held despite clear contrary evidence"
], ans=2,
   why="EK 5.4.B.1.ii: hallucinations are false PERCEPTIONS, are positive symptoms, and may involve one or more of the senses. Note the framework does not limit them to hearing."),

 dict(q="Speech consisting of words strung together in a way that conveys no coherent meaning is described in the framework as", choices=[
   "a delusion of grandeur, a positive symptom",
   "word salad, a manifestation of disorganized speech and a positive symptom",
   "flat affect, a negative symptom",
   "catatonic stupor, a negative symptom"
], ans=1,
   why="EK 5.4.B.1.iii: disorganized thinking or speech is a positive symptom and may manifest as speaking in a word salad, stringing together words in nonsensical ways."),

 dict(q="Catatonia can be classified as either a positive or a negative symptom because", choices=[
   "catatonia is always an added behavior but is sometimes mild",
   "catatonia is always an absence of behavior but is sometimes severe",
   "catatonia is reclassified depending on the person's age",
   "catatonic excitement is an added behavior, while catatonic stupor is the absence of movement"
], ans=3,
   why="EK 5.4.B.1.iv: catatonia may be experienced as excitement (a positive symptom manifestation) or stupor (a negative symptom manifestation). This is the one symptom in the category that can fall either way."),

 dict(q="A person experiences a marked reduction in outward emotional expression and initiates very little movement or speech. These experiences are best classified as", choices=[
   "negative symptoms",
   "positive symptoms",
   "compulsions",
   "dissociative symptoms"], ans=0,
   why="EK 5.4.B.1.v names lack of emotional expression and lack of movement as negative symptoms -- behaviors typically present that are reduced or absent."),

 dict(q="Which set of possible causes of schizophrenia does the framework identify?", choices=[
   "exclusively stressful experiences occurring in adulthood",
   "a single gene that has been identified as the sole cause",
   "a genetic or biological link, such as prenatal virus exposure or imbalances in certain neurotransmitters",
   "exclusively poor parenting during early childhood"
], ans=2,
   why="EK 5.4.B.2: possible causes suggest a genetic or biological link, such as prenatal virus exposure or neurotransmitter imbalances (the dopamine hypothesis). No single causal gene is claimed, and the parenting explanation is one the framework does not endorse."),

 dict(q="Depressive disorders as a category are characterized by", choices=[
   "dissociation from memory, identity, or perception",
   "sad, empty, or irritable mood along with physical and cognitive changes that affect the ability to function",
   "alternating periods of mania and depression",
   "excessive fear and anxiety with related behavioral disturbances"
], ans=1,
   why="EK 5.4.C.1, in substance verbatim. Note irritable mood is included, which matters because a person may not describe themselves as sad. The other options define the bipolar, anxiety, and dissociative categories."),

 dict(q="What most clearly distinguishes persistent depressive disorder from major depressive disorder?", choices=[
   "Persistent depressive disorder involves depressed mood that continues over a much longer span of time, typically at a less acute level",
   "Persistent depressive disorder involves periods of mania between episodes",
   "Persistent depressive disorder occurs only in people under eighteen",
   "Persistent depressive disorder involves hallucinations in every case"], ans=0,
   why="EK 5.4.C.1 names both as depressive disorders in scope. The distinction is chronicity: persistent depressive disorder is defined by long-standing depressed mood rather than by discrete episodes. Mania in either would move the diagnosis to the bipolar category."),

 dict(q="Bipolar disorders as a category are characterized by", choices=[
   "continuous depressed mood with no elevated periods",
   "recurrent unexpected panic attacks",
   "obsessions accompanied by compulsions",
   "periods of mania and periods of depression, alternating over varying lengths of time"
], ans=3,
   why="EK 5.4.D.1: bipolar disorders are characterized by periods of mania and periods of depression, with cycling that can last various amounts of time."),

 dict(q="What distinguishes Bipolar I disorder from Bipolar II disorder?", choices=[
   "Bipolar I involves at least one full manic episode, while Bipolar II involves hypomanic episodes together with major depressive episodes but no full manic episode",
   "Bipolar I involves only depression, while Bipolar II involves only mania",
   "Bipolar I occurs in adults and Bipolar II in adolescents",
   "Bipolar I is diagnosed by the ICD and Bipolar II by the DSM"], ans=0,
   why="EK 5.4.D.1 names both as in scope. The discriminator is the severity of the elevated mood episode: a full manic episode places the diagnosis in Bipolar I, while hypomania with major depression places it in Bipolar II."),

 dict(q="A person has had several extended periods of low mood, and also one period lasting over a week of markedly elevated mood, greatly reduced need for sleep, and impulsive decisions that disrupted their work. This history is most consistent with", choices=[
   "major depressive disorder, because the low periods are more numerous",
   "persistent depressive disorder, because the low mood has been long-standing",
   "generalized anxiety disorder, because the person's functioning was disrupted",
   "a bipolar disorder rather than a depressive disorder, because an episode of elevated mood is present"
], ans=3,
   why="EK 5.4.C.1 and 5.4.D.1. The presence of a manic episode is what separates the bipolar category from the depressive category, and it does so regardless of how much of the person's history is depressive -- which is exactly why this distinction is missed so often."),

 dict(q="Anxiety disorders as a category are characterized by", choices=[
   "excessive fear and/or anxiety with related disturbances to behavior",
   "the presence of obsessions and compulsions",
   "a break in the continuity of memory or identity",
   "altered consumption or absorption of food"], ans=0,
   why="EK 5.4.E.1, in substance verbatim. Note that in the current framework obsessive-compulsive disorders and trauma-related disorders are SEPARATE categories from anxiety disorders, not subtypes of it."),

 dict(q="Specific phobia involves", choices=[
   "prolonged worry that is not attached to any particular object",
   "fear or anxiety toward a particular object or situation, such as heights or spiders",
   "fear of being judged or watched by other people",
   "fear of a range of situations from which escape might be difficult"
], ans=1,
   why="EK 5.4.E.1.i: specific phobia involves fear or anxiety toward a SPECIFIC object or situation, giving acrophobia and arachnophobia as examples. The other options define social anxiety disorder, agoraphobia, and generalized anxiety disorder."),

 dict(q="Agoraphobia involves intense fear of situations such as", choices=[
   "speaking in front of a group that may evaluate one's performance",
   "a single specific animal or object",
   "contamination, accompanied by repeated washing",
   "using public transportation, being in open or enclosed spaces, standing in line or in a crowd, or being outside the home alone"
], ans=3,
   why="EK 5.4.E.1.ii lists precisely these situations. What links them is that escape may be difficult or help unavailable, which is what distinguishes agoraphobia from a specific phobia and from social anxiety disorder."),

 dict(q="Panic disorder involves", choices=[
   "fear confined to one identifiable object",
   "the experience of panic attacks -- unanticipated, overwhelming biological, cognitive, and emotional experiences of fear",
   "persistent low-level worry across many areas of life",
   "intrusive thoughts neutralized by repetitive behaviors"
], ans=1,
   why="EK 5.4.E.1.iii, in substance verbatim, with the framework emphasizing that the attacks are UNANTICIPATED. The framework also notes ataque de nervios, experienced mainly by people of Caribbean or Iberian descent, as a culturally specific presentation."),

 dict(q="Social anxiety disorder involves", choices=[
   "fear of open spaces and crowds specifically",
   "fear that is not attached to any particular situation",
   "recurrent intrusive thoughts about symmetry or order",
   "intense fear of being judged or watched by others"
], ans=3,
   why="EK 5.4.E.1.iv. The framework adds that social anxiety disorder is distinct from but may include agoraphobia, and names taijin kyofusho -- experienced mainly by Japanese people, involving fear that one's body is unpleasing to others -- as a culturally specific presentation."),

 dict(q="Generalized anxiety disorder involves", choices=[
   "anxiety triggered by one clearly identifiable object",
   "anxiety occurring only in evaluative social settings",
   "anxiety relieved by performing a specific ritual",
   "prolonged experiences of nonspecific anxiety or fear"
], ans=3,
   why="EK 5.4.E.1.v: generalized anxiety disorder involves prolonged experiences of NONSPECIFIC anxiety or fear. The absence of a particular trigger is the defining feature and separates it from every other anxiety disorder in scope."),

 dict(q="Obsessive-compulsive disorder is characterized by", choices=[
   "an enduring pattern of behavior that deviates from cultural expectations",
   "obsessions, which are intrusive thoughts, together with compulsions, which are repetitive behaviors intended to address those obsessions",
   "compulsions alone, with no accompanying thoughts",
   "prolonged worry across many life domains with no rituals"
], ans=1,
   why="EK 5.4.F.1 defines the category by the presence of obsessions (intrusive thoughts) and compulsions (intrusive, often repetitive, behaviors INTENDED TO ADDRESS the obsessions). The functional link between the two is what makes it OCD."),

 dict(q="What most clearly distinguishes obsessive-compulsive disorder from generalized anxiety disorder?", choices=[
   "In OCD, specific intrusive thoughts are paired with repetitive behaviors performed to address them; in generalized anxiety disorder the anxiety is nonspecific and no such rituals define the condition",
   "OCD involves anxiety while generalized anxiety disorder does not",
   "OCD is diagnosed in adults and generalized anxiety disorder in children",
   "OCD is a personality disorder while generalized anxiety disorder is not"], ans=0,
   why="EK 5.4.E.1.v describes generalized anxiety disorder as NONSPECIFIC and prolonged; EK 5.4.F.1 describes OCD as specific obsessions paired with compulsions that address them. Note OCD and generalized anxiety disorder sit in different categories in this framework, and obsessive-compulsive PERSONALITY disorder is a third, separate condition in Cluster C."),

 dict(q="Hoarding disorder, the other condition in scope in the obsessive-compulsive and related category, is characterized by", choices=[
   "recurrent episodes of binge eating followed by compensatory behavior",
   "an inability to recall important autobiographical information",
   "excessive fear of being observed by others",
   "persistent difficulty parting with possessions, leading to accumulation that interferes with the use of living spaces"
], ans=3,
   why="EK 5.4.F.1 names hoarding disorder alongside OCD as in scope for this category. The other options describe bulimia nervosa, dissociative amnesia, and social anxiety disorder."),

 dict(q="Which pair correctly matches the two dissociative disorders in scope with their features?", choices=[
   "dissociative amnesia -- inability to recall important personal information, which with fugue includes unexpected travel or wandering; dissociative identity disorder -- the presence of two or more distinct identity states with accompanying gaps in recall",
   "dissociative amnesia -- two or more distinct identity states; dissociative identity disorder -- inability to recall personal information",
   "dissociative amnesia -- loss of the ability to form new memories; dissociative identity disorder -- persistent low mood",
   "dissociative amnesia -- intrusive flashbacks to a trauma; dissociative identity disorder -- compulsive rituals"], ans=0,
   why="EK 5.4.G.1 names dissociative amnesia (with and without fugue) and dissociative identity disorder as the two in scope, and describes the category as dissociations from consciousness, memory, identity, emotion, perception, and behavior. EK 5.4.G.2 attributes possible causes to the experience of trauma or stress."),

 dict(q="Posttraumatic stress disorder, the disorder in scope in the trauma and stressor-related category, follows", choices=[
   "exposure to a traumatic or stressful event, with symptoms that may include hypervigilance, flashbacks, insomnia, and emotional detachment",
   "a gradual accumulation of everyday hassles with no identifiable event",
   "the onset of a medical condition in middle adulthood",
   "a period of elevated mood lasting more than one week"], ans=0,
   why="EK 5.4.H.1: trauma and stressor-related disorders are characterized by exposure to a traumatic or stressful event with subsequent psychological distress, and the framework lists hypervigilance, severe anxiety, flashbacks, insomnia, emotional detachment, and hostility among the symptoms."),

 dict(q="What most clearly distinguishes anorexia nervosa from bulimia nervosa?", choices=[
   "Anorexia nervosa occurs only in adolescence and bulimia nervosa only in adulthood",
   "Anorexia nervosa is a neurodevelopmental disorder and bulimia nervosa is not",
   "Anorexia nervosa centrally involves restriction of intake leading to significantly low body weight, while bulimia nervosa centrally involves recurrent binge eating followed by compensatory behavior, typically without that weight loss",
   "Anorexia nervosa involves binge eating while bulimia nervosa involves restriction"
], ans=2,
   why="EK 5.4.I.1 names both as the feeding and eating disorders in scope and describes the category as altered consumption or absorption of food impairing health or functioning. The reversed pairing is the trap, and EK 5.4.I.2 attributes possible causes to biological, genetic, social, cultural, behavioral, or cognitive sources."),

 dict(q="Personality disorders are characterized by enduring patterns of experience and behavior that deviate from a person's culture, are pervasive and inflexible, begin by early adulthood, and cause distress or impairment. The framework groups them into three clusters, of which", choices=[
   "Cluster A is anxious or fearful, Cluster B is odd or eccentric, and Cluster C is dramatic or erratic",
   "Cluster A is dramatic or erratic, Cluster B is anxious or fearful, and Cluster C is odd or eccentric",
   "the clusters are ordered by how common each disorder is rather than by shared features",
   "Cluster A is odd or eccentric, Cluster B is dramatic, emotional, or erratic, and Cluster C is anxious or fearful"
], ans=3,
   why="EK 5.4.J.1.i-iii: Cluster A (odd or eccentric) holds paranoid, schizoid, and schizotypal personality disorders; Cluster B (dramatic, emotional, or erratic) holds antisocial, histrionic, narcissistic, and borderline; Cluster C (anxious or fearful) holds avoidant, dependent, and obsessive-compulsive personality disorders. The permutations are the distractors."),
]
