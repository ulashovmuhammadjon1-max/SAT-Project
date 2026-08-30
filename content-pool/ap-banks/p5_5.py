# AP PSYCH 5.5 Treatment of Psychological Disorders — 30 questions
# Required content: CED (c) 2024 College Board, Course Framework V.1, pp. 125-127.
# EK 5.5.A.1 meta-analytic studies find psychotherapies generally effective;
#   evidence-based interventions, cultural humility, therapeutic alliance;
# EK 5.5.B.1 deinstitutionalization and the present preference for decentralized
#   treatment, often combining medication with psychological therapies;
# EK 5.5.C.1 APA ethical principles -- nonmaleficence, fidelity, integrity, and
#   respect for people's rights and dignity;
# EK 5.5.D.1 psychodynamic therapies: free association, dream interpretation;
# EK 5.5.D.2 cognitive therapies: cognitive restructuring, fear hierarchies, and
#   the cognitive triad (negative thoughts about oneself, the world, the future);
# EK 5.5.D.3 applied behavior analysis: exposure therapies such as systematic
#   desensitization, aversion therapies, token economies; and biofeedback;
# EK 5.5.D.4 cognitive-behavioral therapies: dialectical behavior therapy and
#   rational-emotive behavior therapy;
# EK 5.5.D.5 humanistic therapy, commonly called person-centered therapy: active
#   listening and unconditional positive regard;
# LO 5.5.E group versus individual therapy;
# EK 5.5.F.1 hypnosis is effective for pain and anxiety, and research does NOT
#   support its use to retrieve accurate memories or to regress in age;
# EK 5.5.G.1 psychoactive medications and side effects such as tardive
#   dyskinesia; EK 5.5.G.2 psychosurgery, TMS, and electroconvulsive therapy.
#
# LANGUAGE: person-first and clinically neutral. Treatments are described by what
# they involve, without endorsement or sensationalism, and the two with a
# difficult history -- aversion therapy and the lobotomy -- are presented as the
# framework presents them.
#
# No sympy: every key's claim is stated item by item in verify_p5_5.py.
TOPIC = ("5.5", "Treatment of Psychological Disorders", 5)
QUESTIONS = [
 dict(q="What do meta-analytic studies of psychotherapy generally conclude?", choices=[
   "that only medication produces measurable improvement",
   "that the evidence is too sparse to support any conclusion",
   "that psychotherapies are generally effective",
   "that psychotherapies are no better than no treatment at all"
], ans=2,
   why="EK 5.5.A.1: many researchers who have conducted meta-analytic studies of psychotherapy conclude that psychotherapies are generally effective."),

 dict(q="An evidence-based intervention is best described as one that", choices=[
   "the therapist personally finds most comfortable to deliver",
   "has been used by clinicians for the longest time",
   "requires the fewest sessions to complete",
   "has been supported by research findings on its effectiveness"
], ans=3,
   why="EK 5.5.A.1 states that many psychologists use evidence-based interventions to develop treatment plans. What makes an intervention evidence-based is research support, not familiarity or tradition."),

 dict(q="The therapeutic alliance refers to", choices=[
   "the insurance arrangement covering the course of treatment",
   "the collaborative working relationship between therapist and client",
   "an agreement between two therapists to share a caseload",
   "the client's relationship with other members of a therapy group"
], ans=1,
   why="EK 5.5.A.1 states that therapists should establish a therapeutic alliance with the client to deliver therapy successfully. It is the working relationship itself, and it is named as a condition of effective treatment rather than an optional extra."),

 dict(q="Cultural humility on the part of a therapist involves", choices=[
   "requiring clients to adopt the therapist's cultural framework",
   "recognizing the limits of one's own cultural perspective and remaining open to the client's",
   "assuming that clients from a given culture will share the same values",
   "avoiding any discussion of a client's cultural background"
], ans=1,
   why="EK 5.5.A.1 states that therapists should exhibit cultural humility. Humility means holding one's own perspective as partial rather than treating cultural knowledge as a set of generalizations to apply -- which is what the second option describes and what makes it the trap."),

 dict(q="According to the framework, the large-scale deinstitutionalization of the late twentieth century was driven primarily by", choices=[
   "the introduction of the first diagnostic manual",
   "the increased use and effectiveness of psychotropic medication therapy",
   "a decline in the number of people experiencing psychological disorders",
   "the discovery that psychological disorders resolve without treatment"
], ans=1,
   why="EK 5.5.B.1: due to the increased use and effectiveness of psychotropic medication therapy, hospitals and asylums deinstitutionalized massive numbers of people in the late 20th century."),

 dict(q="The framework describes present-day treatment practice as favoring", choices=[
   "psychological therapy used alone in nearly all cases",
   "decentralized treatment, often combining medication with psychological therapies",
   "long-term inpatient care as the standard approach",
   "medication used alone in nearly all cases"
], ans=1,
   why="EK 5.5.B.1: therapists now prefer to treat in decentralized ways, often with a combination of medication and psychological therapies. The combination is the framework's point, so either treatment alone misstates it."),

 dict(q="Which set names the ethical principles the framework identifies for psychologists in clinical or therapeutic situations?", choices=[
   "diagnosis, treatment, referral, and discharge",
   "nonmaleficence, fidelity, integrity, and respect for people's rights and dignity",
   "confidentiality, punctuality, efficiency, and profitability",
   "objectivity, detachment, neutrality, and anonymity"
], ans=1,
   why="EK 5.5.C.1 names exactly these four principles as established by the APA. Note this is the American PSYCHOLOGICAL Association, distinct from the American Psychiatric Association that publishes the DSM."),

 dict(q="A therapist who declines to use a technique that carries a substantial risk of harming a client, despite a family member's request, is most directly applying which principle?", choices=[
   "respect for people's rights and dignity",
   "nonmaleficence",
   "fidelity",
   "integrity"
], ans=1,
   why="EK 5.5.C.1 names nonmaleficence, the obligation to avoid causing harm. It is the principle that governs when a proposed course of action carries a risk of injury to the client."),

 dict(q="Psychodynamic therapies employ which pair of techniques?", choices=[
   "cognitive restructuring and fear hierarchies",
   "active listening and unconditional positive regard",
   "token economies and biofeedback",
   "free association and dream interpretation"
], ans=3,
   why="EK 5.5.D.1: psychodynamic therapies employ free association and dream interpretation to uncover the unconscious mind. The distractors name the cognitive, humanistic, and behavioral techniques respectively."),

 dict(q="Cognitive restructuring involves", choices=[
   "reporting whatever comes to mind without censoring it",
   "identifying maladaptive thoughts and working to replace them with more accurate ones",
   "gradually approaching a feared object while remaining relaxed",
   "rewarding target behaviors with tokens exchangeable for privileges"
], ans=1,
   why="EK 5.5.D.2: cognitive therapies may employ cognitive restructuring to combat maladaptive thinking. The target is the thought itself, which is what makes it cognitive rather than behavioral."),

 dict(q="The cognitive triad, as used in cognitive therapy, refers to negative thoughts about", choices=[
   "the client, the therapist, and the family",
   "oneself, the world, and the future",
   "the past, the present, and the future",
   "the body, the mind, and the spirit"
], ans=1,
   why="EK 5.5.D.2 states that cognitive therapy proposes people should focus on the cognitive triad -- negative thoughts about oneself, the world, and the future."),

 dict(q="A fear hierarchy, as used in therapy, is", choices=[
   "a schedule of medication doses increasing over time",
   "a list of the therapist's professional qualifications",
   "an ordered list of feared situations arranged from least to most anxiety-provoking",
   "a ranking of clients by the severity of their symptoms"
], ans=2,
   why="EK 5.5.D.2 names fear hierarchies among the techniques cognitive therapies may employ; it is the graded ordering that allows a client to work upward through progressively harder situations."),

 dict(q="Applied behavior analysis involves", choices=[
   "interpreting the symbolic content of a client's dreams",
   "identifying distorted beliefs and testing them against evidence",
   "providing acceptance that is not made conditional on the client's progress",
   "applying principles of conditioning to address mental disorders and developmental disabilities"
], ans=3,
   why="EK 5.5.D.3, in substance verbatim. The framework groups exposure therapies, aversion therapies, and token economies under it as applications of conditioning principles."),

 dict(q="Systematic desensitization involves", choices=[
   "monitoring a physiological signal in order to learn to regulate it",
   "gradual exposure to a feared stimulus while the client practices a relaxation response",
   "pairing an unwanted behavior with an unpleasant stimulus",
   "exchanging earned tokens for privileges"
], ans=1,
   why="EK 5.5.D.3 names systematic desensitization as an exposure therapy employing applied behavior analysis. Graded exposure paired with a relaxation response is what distinguishes it from the other behavioral techniques in the same statement."),

 dict(q="Aversion therapy involves", choices=[
   "recording brain activity to detect distorted thinking",
   "pairing an unwanted behavior with an unpleasant stimulus so the behavior becomes less appealing",
   "gradually approaching a feared situation while relaxed",
   "granting acceptance regardless of the client's behavior"
], ans=1,
   why="EK 5.5.D.3 names aversion therapies among the applications of applied behavior analysis. Its mechanism is the association of the behavior with an unpleasant stimulus, which is the reverse of exposure therapy's pairing of the feared stimulus with relaxation."),

 dict(q="A token economy operates by", choices=[
   "reinforcing target behaviors with tokens that can later be exchanged for privileges or items",
   "removing privileges whenever a target behavior occurs",
   "interpreting the meaning a client assigns to a reward",
   "using a hierarchy of feared situations"], ans=0,
   why="EK 5.5.D.3 names token economies among the applications of applied behavior analysis. The token is a conditioned reinforcer whose value comes from what it can be exchanged for."),

 dict(q="Biofeedback uses principles of conditioning to help clients", choices=[
   "regulate body systems that contribute to feelings of anxiety or depression",
   "recover memories of events they cannot otherwise recall",
   "identify the unconscious meaning of physical symptoms",
   "rank feared situations in order of difficulty"
], ans=0,
   why="EK 5.5.D.3: biofeedback uses principles of conditioning to help clients regulate body systems, such as the sympathetic and parasympathetic nervous systems, that contribute to feelings of anxiety or depression."),

 dict(q="Dialectical behavior therapy and rational-emotive behavior therapy are both classified as", choices=[
   "humanistic therapies centered on unconditional positive regard",
   "biological interventions acting on neurotransmitters",
   "cognitive-behavioral therapies, combining techniques from the cognitive and behavioral perspectives",
   "psychodynamic therapies aimed at uncovering unconscious material"
], ans=2,
   why="EK 5.5.D.4 names both explicitly as cognitive-behavioral therapies that combine techniques from the cognitive and behavioral perspectives."),

 dict(q="Therapy from the humanistic perspective, commonly called person-centered therapy, employs", choices=[
   "fear hierarchies and cognitive restructuring",
   "token economies and aversion techniques",
   "active listening and unconditional positive regard",
   "free association and dream interpretation"
], ans=2,
   why="EK 5.5.D.5, in substance verbatim: therapy from the humanistic perspective, commonly referred to as person-centered therapy, employs active listening and unconditional positive regard."),

 dict(q="A therapist reflects a client's statements back to confirm understanding and conveys acceptance of the client regardless of what the client discloses. This therapist is practicing", choices=[
   "person-centered therapy",
   "psychodynamic therapy",
   "applied behavior analysis",
   "rational-emotive behavior therapy"
], ans=0,
   why="EK 5.5.D.5. Both named humanistic techniques appear: reflecting statements back is active listening, and acceptance that does not depend on what is disclosed is unconditional positive regard."),

 dict(q="Which pairing of a technique with its theoretical approach is correct?", choices=[
   "all three techniques belong to the humanistic approach",
   "systematic desensitization -- behavioral; free association -- psychodynamic; cognitive restructuring -- cognitive",
   "systematic desensitization -- psychodynamic; free association -- cognitive; cognitive restructuring -- behavioral",
   "systematic desensitization -- humanistic; free association -- behavioral; cognitive restructuring -- psychodynamic"
], ans=1,
   why="EK 5.5.D.1, 5.5.D.2, and 5.5.D.3 assign these techniques to the psychodynamic, cognitive, and behavioral approaches respectively. Matching technique to approach is the central skill this topic tests, and the distractors are permutations of the correct assignment."),

 dict(q="Compared with individual therapy, group therapy characteristically offers", choices=[
   "the chance to receive feedback from others facing similar difficulties, at the cost of some individual attention",
   "more time devoted to each participant's specific circumstances",
   "a guarantee of faster improvement for every participant",
   "the elimination of any need for a trained therapist"
], ans=0,
   why="LO 5.5.E asks how group therapy differs from individual therapy. Group formats supply peer feedback and the recognition that difficulties are shared, while individual therapy supplies undivided attention -- a genuine trade-off rather than one format being superior."),

 dict(q="According to the framework, hypnosis has shown effectiveness in treating", choices=[
   "neurodevelopmental disorders",
   "dissociative identity disorder",
   "pain and anxiety",
   "delusions and hallucinations"
], ans=2,
   why="EK 5.5.F.1 states that hypnosis has shown effectiveness in treating pain and anxiety. The framework claims effectiveness for these two applications specifically and no others."),

 dict(q="What does research NOT support regarding the use of hypnosis?", choices=[
   "using it to retrieve accurate memories or to regress a person to an earlier age",
   "using it as one component in the management of pain",
   "using it to help reduce anxiety",
   "using it alongside other evidence-based treatments"
], ans=0,
   why="EK 5.5.F.1 states directly that research does NOT support the use of hypnosis to retrieve accurate memories or regress in age. This is one of the framework's clearest corrections of a popular belief."),

 dict(q="Antidepressant medications most commonly act by", choices=[
   "enhancing the activity of GABA to produce rapid sedation",
   "removing damaged tissue from a specific brain region",
   "increasing the availability of certain neurotransmitters, such as serotonin, in the central nervous system",
   "blocking dopamine receptors to reduce hallucinations and delusions"
], ans=2,
   why="EK 5.5.G.1 states that psychoactive medications interact with specific neurotransmitters in the central nervous system. Antidepressants characteristically raise the availability of serotonin and related neurotransmitters; the other options describe antipsychotics, antianxiety medication, and psychosurgery."),

 dict(q="Antianxiety medications most commonly act by", choices=[
   "increasing the activity of the neurotransmitter GABA, which dampens central nervous system activity",
   "blocking the reuptake of serotonin over a period of weeks",
   "blocking dopamine receptors",
   "stimulating the release of growth hormone"
], ans=0,
   why="EK 5.5.G.1's general claim, applied: antianxiety medications act largely by enhancing GABA, the main inhibitory neurotransmitter, which is why their calming effect is comparatively rapid where an antidepressant's takes weeks."),

 dict(q="Lithium is used in the treatment of", choices=[
   "autism spectrum disorder, where it restores social communication",
   "dissociative amnesia, where it restores lost memories",
   "bipolar disorders, where it reduces the intensity and frequency of mood episodes",
   "specific phobias, where it removes the feared association"
], ans=2,
   why="EK 5.5.G.1 names lithium among psychoactive medications. It is a mood stabilizer, and its clinical role is in the bipolar disorders of EK 5.4.D -- the one medication in the framework's list tied to a specific diagnostic category."),

 dict(q="Antipsychotic medications act largely on dopamine systems, which is also why they can produce", choices=[
   "increased accuracy of autobiographical memory",
   "a reduction in the need for any psychological therapy",
   "tardive dyskinesia, a movement disorder related to the regulation of dopamine",
   "an immediate and permanent cure for schizophrenic spectrum disorders"
], ans=2,
   why="EK 5.5.G.1 names tardive dyskinesia explicitly as a side effect and describes it as a movement disorder related to the regulation of dopamine in the nervous system -- the same system the medication acts on, which is why the side effect follows from the mechanism."),

 dict(q="Which set correctly identifies the surgical or invasive interventions the framework names?", choices=[
   "cognitive restructuring, fear hierarchies, and the cognitive triad",
   "psychosurgery, transcranial magnetic stimulation, and electroconvulsive therapy",
   "systematic desensitization, biofeedback, and token economies",
   "free association, dream interpretation, and active listening"
], ans=1,
   why="EK 5.5.G.2 names exactly these three as surgical or invasive interventions, noting psychosurgery may involve lesioning. The distractors list behavioral, psychodynamic, humanistic, and cognitive techniques, none of which are invasive."),

 dict(q="What does the framework say about the lobotomy?", choices=[
   "It was never actually performed on human patients",
   "It is a form of medication therapy rather than surgery",
   "It is a form of psychosurgery that was popular in the mid-twentieth century but is rarely, if ever, performed today",
   "It remains a standard treatment for schizophrenic spectrum disorders"
], ans=2,
   why="EK 5.5.G.2 states this directly. The historical framing matters: the framework presents the lobotomy as a discontinued practice, not as a current option."),
]
