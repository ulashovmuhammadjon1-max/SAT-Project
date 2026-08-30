"""Key verification for AP PSYCH 5.5 (Treatment of Psychological Disorders).

No computation is possible here, so for EVERY item the specific claim the key
rests on is written out: a CED definition, a named study's actual result, or
what a theory actually predicts. That statement is what replaces sympy.

Source: AP Psychology Course and Exam Description, (c) 2024 College Board,
Course Framework V.1, Topic 5.5, pp. 125-127.

TECHNIQUE-TO-APPROACH, the central skill this topic tests. Every assignment
below comes from the framework, and one item tests the mapping directly:
  psychodynamic (EK 5.5.D.1) -- free association, dream interpretation
  cognitive    (EK 5.5.D.2) -- cognitive restructuring, fear hierarchies,
                               the cognitive triad
  behavioral   (EK 5.5.D.3) -- applied behavior analysis: exposure therapies
                               including systematic desensitization, aversion
                               therapies, token economies; plus biofeedback
  cognitive-behavioral (EK 5.5.D.4) -- dialectical behavior therapy,
                               rational-emotive behavior therapy
  humanistic   (EK 5.5.D.5) -- person-centered therapy: active listening,
                               unconditional positive regard

DRUG CLASSES. EK 5.5.G.1 states only that psychoactive medications interact with
specific neurotransmitters in the central nervous system and names
antidepressants, antianxiety drugs, lithium, and antipsychotics. The mechanisms
keyed below are the standard ones and are stated at the level the framework
supports: antidepressants raise serotonin availability, antianxiety medications
enhance GABA, antipsychotics act on dopamine systems (which is why EK 5.5.G.1's
named side effect, tardive dyskinesia, is dopamine-related), and lithium is
keyed to its CLINICAL ROLE as a mood stabilizer in bipolar disorders rather than
to a mechanism, because lithium's mechanism is not settled and the framework
asserts none.

THE FRAMEWORK'S CORRECTION OF A POPULAR BELIEF, keyed explicitly: EK 5.5.F.1
says research does NOT support using hypnosis to retrieve accurate memories or
to regress in age, while it IS effective for pain and anxiety.

Run: python3 verify_p5_5.py
"""
import p5_5
from psych_check import check

CLAIMS = [
 ("psychotherapies are generally effective",
  "EK 5.5.A.1: many researchers who have conducted meta-analytic studies of "
  "psychotherapy conclude that psychotherapies are generally effective. The "
  "'no better than no treatment' option is the claim this body of research "
  "settled against."),

 ("supported by research findings on its effectiveness",
  "EK 5.5.A.1 states that many psychologists use evidence-based interventions to "
  "develop treatment plans. What makes an intervention evidence-based is research "
  "support -- not the therapist's comfort, tradition, or brevity, which are the "
  "three distractors."),

 ("collaborative working relationship between therapist and client",
  "EK 5.5.A.1: therapists should establish a therapeutic alliance with the client "
  "to deliver therapy successfully. The framework names it as a CONDITION of "
  "successful delivery, which is why it is content rather than atmosphere."),

 ("limits of one's own cultural perspective",
  "EK 5.5.A.1 states therapists should exhibit cultural humility. Humility means "
  "holding one's own perspective as partial and staying open to the client's. The "
  "trap is the option that treats cultural knowledge as generalizations to apply "
  "to a client -- which is closer to stereotyping (EK 4.2.A.1) than to humility."),

 ("increased use and effectiveness of psychotropic medication therapy",
  "EK 5.5.B.1, in substance verbatim: due to the increased use and effectiveness "
  "of psychotropic medication therapy, hospitals and asylums deinstitutionalized "
  "massive numbers of people in the late 20th century."),

 ("decentralized treatment, often combining medication with psychological therapies",
  "EK 5.5.B.1: therapists now prefer to treat in decentralized ways, often with a "
  "COMBINATION of medication and psychological therapies. The combination is the "
  "framework's point, so both single-modality options misstate current practice."),

 ("nonmaleficence, fidelity, integrity, and respect for people's rights and dignity",
  "EK 5.5.C.1 names exactly these four principles as established by the APA. Note "
  "this is the American PSYCHOLOGICAL Association, distinct from the American "
  "Psychiatric Association that publishes the DSM (EK 5.3.A.3) -- the two are "
  "easily swapped and are kept apart deliberately across these two topics."),

 ("nonmaleficence",
  "EK 5.5.C.1 names nonmaleficence, the obligation to avoid causing harm. It is "
  "the principle governing a proposed course of action that carries a risk of "
  "injury to the client, which is what the stem describes. Fidelity concerns "
  "faithfulness to professional obligations and integrity concerns honesty, so "
  "neither is the principle at issue."),

 ("free association and dream interpretation",
  "EK 5.5.D.1: psychodynamic therapies employ free association and dream "
  "interpretation to uncover the unconscious mind. The three distractors name the "
  "cognitive, humanistic, and behavioral technique pairs respectively, so the item "
  "discriminates all four approaches at once."),

 ("identifying maladaptive thoughts and working to replace them",
  "EK 5.5.D.2: cognitive therapies may employ cognitive restructuring to combat "
  "maladaptive thinking. The TARGET is the thought itself, which is what makes the "
  "technique cognitive rather than behavioral."),

 ("oneself, the world, and the future",
  "EK 5.5.D.2 states it exactly: cognitive therapy proposes people should focus on "
  "the cognitive triad -- negative thoughts about oneself, the world, and the "
  "future. The past/present/future option is the plausible substitute and is "
  "wrong."),

 ("ordered list of feared situations arranged from least to most anxiety-provoking",
  "EK 5.5.D.2 names fear hierarchies among the techniques cognitive therapies may "
  "employ. The graded ordering is what allows a client to work upward through "
  "progressively harder situations, and it is what systematic desensitization "
  "(EK 5.5.D.3) moves through."),

 ("applying principles of conditioning to address mental disorders and developmental disabilities",
  "EK 5.5.D.3, in substance verbatim. The framework groups exposure therapies, "
  "aversion therapies, and token economies under applied behavior analysis as "
  "applications of conditioning principles."),

 ("gradual exposure to a feared stimulus while the client practices a relaxation response",
  "EK 5.5.D.3 names systematic desensitization as an exposure therapy employing "
  "applied behavior analysis. Graded exposure PAIRED WITH a relaxation response is "
  "what distinguishes it from the other behavioral techniques in the same "
  "statement -- and note it is the exact inverse of aversion therapy's pairing."),

 ("pairing an unwanted behavior with an unpleasant stimulus",
  "EK 5.5.D.3 names aversion therapies among the applications of applied behavior "
  "analysis. Its mechanism is association of the behavior with an unpleasant "
  "stimulus, which is the reverse of exposure therapy pairing a feared stimulus "
  "with relaxation. Keeping the two straight is the point of having both items."),

 ("reinforcing target behaviors with tokens that can later be exchanged",
  "EK 5.5.D.3 names token economies among the applications of applied behavior "
  "analysis. The token is a conditioned reinforcer whose value comes entirely from "
  "what it can be exchanged for -- so the option describing REMOVAL of privileges "
  "describes a different contingency altogether."),

 ("regulate body systems that contribute to feelings of anxiety or depression",
  "EK 5.5.D.3, in substance verbatim: biofeedback uses principles of conditioning "
  "to help clients regulate body systems, such as the sympathetic and "
  "parasympathetic nervous systems, that contribute to feelings of anxiety or "
  "depression."),

 ("cognitive-behavioral therapies, combining techniques from the cognitive and behavioral",
  "EK 5.5.D.4 names dialectical behavior therapy and rational-emotive behavior "
  "therapy explicitly as cognitive-behavioral therapies combining techniques from "
  "the cognitive and behavioral perspectives. Both are frequently misfiled as "
  "purely cognitive."),

 ("active listening and unconditional positive regard",
  "EK 5.5.D.5, in substance verbatim: therapy from the humanistic perspective, "
  "commonly referred to as person-centered therapy, employs active listening and "
  "unconditional positive regard. This is the therapy counterpart of the "
  "personality material in EK 4.4.B.1."),

 ("person-centered therapy",
  "EK 5.5.D.5. Both named humanistic techniques are present in the stem: "
  "reflecting statements back to confirm understanding is active listening, and "
  "acceptance that does not depend on what the client discloses is unconditional "
  "positive regard."),

 ("systematic desensitization -- behavioral; free association -- psychodynamic; cognitive restructuring -- cognitive",
  "EK 5.5.D.3, 5.5.D.1, and 5.5.D.2 respectively. Matching technique to "
  "theoretical approach is the central skill of this topic, and the distractors "
  "are permutations of the correct assignment rather than invented pairings, so "
  "the item cannot be answered by eliminating nonsense."),

 ("feedback from others facing similar difficulties, at the cost of some individual attention",
  "LO 5.5.E asks how group therapy differs from individual therapy. The honest "
  "answer is a trade-off: group formats supply peer feedback and the recognition "
  "that difficulties are shared, individual therapy supplies undivided attention. "
  "The 'guarantee of faster improvement' option is the overclaim, and neither "
  "format removes the need for a trained therapist."),

 ("pain and anxiety",
  "EK 5.5.F.1: hypnosis has shown effectiveness in treating pain and anxiety. The "
  "framework claims effectiveness for these two applications and no others, so a "
  "wider claim would go beyond it."),

 ("retrieve accurate memories or to regress a person to an earlier age",
  "EK 5.5.F.1 states directly that research does NOT support the use of hypnosis "
  "to retrieve accurate memories or regress in age. This is the framework's "
  "clearest correction of a widely held popular belief, and the other three "
  "options are uses the framework does support or permit."),

 ("increasing the availability of certain neurotransmitters, such as serotonin",
  "EK 5.5.G.1 states that psychoactive medications interact with specific "
  "neurotransmitters in the central nervous system and names antidepressants among "
  "them. Antidepressants characteristically raise the availability of serotonin "
  "and related neurotransmitters. The distractors are, in order, the antipsychotic "
  "mechanism, the antianxiety mechanism, and psychosurgery -- so the item "
  "discriminates the classes rather than testing one in isolation."),

 ("increasing the activity of the neurotransmitter GABA",
  "EK 5.5.G.1's general claim applied to the antianxiety class it names. These "
  "medications act largely by enhancing GABA, the principal inhibitory "
  "neurotransmitter, which is why their calming effect is comparatively rapid "
  "where an antidepressant's onset takes weeks -- the contrast the second option "
  "is built from."),

 ("bipolar disorders, where it reduces the intensity and frequency of mood episodes",
  "EK 5.5.G.1 names lithium among psychoactive medications. It is keyed here to "
  "its CLINICAL ROLE as a mood stabilizer in the bipolar disorders of EK 5.4.D "
  "rather than to a mechanism, deliberately: lithium's mechanism of action is not "
  "settled and the framework asserts none, so keying a mechanism would be "
  "asserting more than the source supports."),

 ("tardive dyskinesia, a movement disorder related to the regulation of dopamine",
  "EK 5.5.G.1 names tardive dyskinesia explicitly as a side effect and describes "
  "it as a movement disorder related to the regulation of dopamine in the nervous "
  "system. The side effect follows from the mechanism, since antipsychotics act on "
  "the same dopamine systems -- which is why the item pairs the two. Note the "
  "'immediate and permanent cure' option is false and would also misrepresent the "
  "course of a schizophrenic spectrum disorder."),

 ("psychosurgery, transcranial magnetic stimulation, and electroconvulsive therapy",
  "EK 5.5.G.2 names exactly these three as surgical or invasive interventions, "
  "noting that psychosurgery may involve lesioning. Every distractor lists "
  "non-invasive psychological techniques from EK 5.5.D, which is the distinction "
  "being tested."),

 ("popular in the mid-twentieth century but is rarely, if ever, performed today",
  "EK 5.5.G.2, in substance verbatim: the lobotomy is a form of psychosurgery that "
  "was popular in the mid-20th century but is rarely, if ever, performed today. "
  "The historical framing is the content -- the framework presents it as a "
  "discontinued practice, not a current option."),
]

check(p5_5, CLAIMS)
