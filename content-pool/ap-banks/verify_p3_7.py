"""Key audit for AP PSYCHOLOGY 3.7 Classical Conditioning.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states the framework assertion the
key rests on.

TWO EXCLUSION STATEMENTS LIVE IN THIS TOPIC, and both are checked first:

  * EK 3.7.A.2.v excludes DELAYED, TRACE, SIMULTANEOUS, and BACKWARD
    conditioning. None of those four words appears anywhere in this module -- not
    as a key, not as a distractor. This is worth stating because the framework
    DOES keep the principle those procedures illustrate: EK 3.7.A.2.ii says the
    ORDER of CS and UCS presentation matters for acquisition. Item 9 tests that
    principle in the framework's own words while naming none of the excluded
    procedures. Getting this wrong in either direction -- dropping the order
    principle, or teaching it through the excluded procedure names -- would
    misrepresent the course.
  * EK 3.7.A.3 excludes EXPECTANCY THEORY. It appears once, as the key to item
    30, where naming the excluded theory is the correct response.

THE FOUR-COMPONENT VOCABULARY IS WHERE THIS TOPIC IS ACTUALLY FAILED. UCS, UCR,
CS, and CR are four labels for two stimuli and two responses, and a student who
has memorised the four words still cannot assign them without one fact: WHICH
STIMULUS PRODUCED THE RESPONSE BEFORE ANY PAIRING. The CED's own sample
multiple-choice question is a CS-identification item, which is a fair signal of
how the exam uses this content. Items 5-8 therefore run one scenario through all
four labels, and the scenario states the pre-pairing effectiveness explicitly.
Each of the four items carries the other three labels as its distractors, so
none can be answered by elimination.

Two further pairs kept straight because each is a genuine near-miss:
  * GENERALIZATION (response spreads to similar stimuli) vs DISCRIMINATION
    (response occurs only to the trained stimulus) -- items 14-17, definitions
    and scenarios, each with the sibling as first distractor.
  * HABITUATION (EK 3.7.A.5, a diminished response to a repeated stimulus, with
    NO conditioning required) vs EXTINCTION (EK 3.7.A.2.iii, loss of a
    CONDITIONED response once the pairing stops). Item 27 asks for the contrast
    directly; the two are easy to conflate because both are decreases.

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p3_7

CLAIMS = [
 ("observable behavior, to the exclusion of mental processes",
  "EK 3.7.A.1, near verbatim: behaviorists have traditionally focused on observable behavior to the exclusion of mental processes. The distractors are the psychodynamic, biological, and cognitive perspectives, so all four options name real approaches."),
 ("one stimulus with another stimulus",
  "EK 3.7.A.2: classical conditioning focuses on the association of one stimulus with another stimulus to elicit a response. The first distractor is OPERANT conditioning as EK 3.8.A.1 defines it -- behavior with consequence -- which is the single most important contrast in Unit 3."),
 ("elicits a response without any prior learning",
  "EK 3.7.A.2.i: the unconditioned stimulus elicits an unconditioned response. 'Unconditioned' means the link is in place before any conditioning, which is what the key states and what makes the CS distractor wrong."),
 ("only after being paired with an unconditioned stimulus",
  "EK 3.7.A.2.i: the unconditioned response becomes the conditioned response when performed in response to the conditioned stimulus. The CS therefore acquires its power through the pairing, which is exactly what distinguishes it from the UCS."),
 ("unconditioned stimulus (UCS)",
  "EK 3.7.A.2.i. The stem states that food produced salivation BEFORE any pairing, which is the fact that fixes it as the unconditioned stimulus. Items 5-8 run one scenario through all four labels; this is the stimulus that was already effective."),
 ("conditioned stimulus (CS)",
  "EK 3.7.A.2.i. The bell produced nothing until it was paired with food, so it is the conditioned stimulus. Same scenario as item 5, the other stimulus."),
 ("unconditioned response (UCR)",
  "EK 3.7.A.2.i: the UCS elicits the UCR. Salivation to food required no learning, so it is the unconditioned response. Same scenario, first of the two responses."),
 ("conditioned response (CR)",
  "EK 3.7.A.2.i: the unconditioned response BECOMES the conditioned response when performed in response to the CS. Salivation to the bell alone is that response. Completing the set of four means a student cannot pass items 5-8 by elimination."),
 ("order in which the conditioned stimulus and the unconditioned stimulus are presented",
  "EK 3.7.A.2.ii states that the order of presentation of the CS with the UCS is important to successful acquisition. The framework keeps this principle while EK 3.7.A.2.v's exclusion statement removes delayed, trace, simultaneous, and backward conditioning from the exam -- so the item tests the principle and names none of the four procedures."),
 ("learning of the association between the two stimuli",
  "EK 3.7.A.2 identifies acquisition as learning the association. The three distractors are extinction, spontaneous recovery, and generalization, each defined in a following EK, so the item places acquisition within the sequence rather than testing it in isolation."),
 ("conditioned stimulus is presented repeatedly without the unconditioned stimulus",
  "EK 3.7.A.2.iii: a CR can become extinct when the CS is no longer paired with the UCS. The first distractor reverses which stimulus is presented alone, which is the error worth catching."),
 ("reappears after the conditioned stimulus is presented again following extinction",
  "EK 3.7.A.2.iii: a formerly extinct CR can be spontaneously recovered when the CS is again presented after extinction. Note that no new pairing is required, which is what makes it 'spontaneous'."),
 ("spontaneous recovery",
  "EK 3.7.A.2.iii. The stem supplies extinction, a delay, and the CS alone with no new food -- the absence of new pairings is what rules out a second acquisition, the first distractor."),
 ("elicited by stimuli similar to the conditioned stimulus",
  "EK 3.7.A.2.iv names stimulus discrimination and generalization as demonstrated in classical conditioning studies; generalization is the spread to similar stimuli. The first distractor is discrimination, its sibling in the same EK."),
 ("occurs to the conditioned stimulus but not to other similar stimuli",
  "EK 3.7.A.2.iv's discrimination: responding selectively to the trained stimulus. Items 14 and 15 are adjacent and each carries the other as its first distractor."),
 ("stimulus generalization",
  "EK 3.7.A.2.iv. Fear spreading from a white rat to a white rabbit and a cotton ball is response spreading to SIMILAR stimuli, which is generalization by definition."),
 ("stimulus discrimination",
  "EK 3.7.A.2.iv. Responding to one pitch and not to others is selective responding to the trained stimulus, the mirror image of item 16 and drawn from the same EK."),
 ("established conditioned stimulus is used as an unconditioned stimulus",
  "EK 3.7.A.2.v: a CS can be used as a UCS in higher-order conditioning. The final distractor is observational learning from EK 3.9.A.1, which is a different mechanism entirely."),
 ("higher-order conditioning",
  "EK 3.7.A.2.v applied. The bell is already an established CS from the earlier items' procedure, and it now serves as the UCS for conditioning the square -- which is the definition acted out."),
 ("emotional responses",
  "EK 3.7.A.3: research has demonstrated that emotional responses can be classically conditioned, and these findings form the basis of therapeutic interventions for many mental disorders."),
 ("therapeutic intervention grounded in the classical conditioning of emotional responses",
  "EK 3.7.A.3 names counterconditioning as its example of such an intervention. The distractors relocate the term to operant schedules (3.8.A.5), to generalization (3.7.A.2.iv), and to attachment (3.6.A.3)."),
 ("acquired through a single pairing and is not strengthened by further pairings",
  "EK 3.7.A.4, near verbatim. Both halves matter: one pairing suffices, AND further pairings do not strengthen it. A key stating only the first half would miss what makes one-trial learning distinctive."),
 ("biologically predisposed to learn certain stimulus-response pairings more quickly",
  "EK 3.7.A.4, verbatim in substance: biological preparedness refers to how animals are biologically predisposed to learning certain stimulus-response pairings more quickly than others. The first distractor -- all pairings learned at equal rates -- is the assumption preparedness contradicts."),
 ("taste aversion acquired through one-trial conditioning",
  "EK 3.7.A.4 identifies taste aversions as acquired through classical conditioning and as the demonstration of one-trial conditioning. The stem's clause that she KNOWS a virus caused the illness is deliberate: the conditioned aversion persists despite accurate knowledge, which shows the association is not a reasoned belief."),
 ("learned far more readily than most other pairings",
  "EK 3.7.A.4 links taste aversion research to biological preparedness as well as to one-trial conditioning. Preparedness is a claim about the RATE at which certain pairings are learned relative to others, which is what the key states."),
 ("grows accustomed to a repeated or enduring stimulus",
  "EK 3.7.A.5, near verbatim: habituation occurs when organisms grow accustomed to and exhibit a diminished response to a repeated or enduring stimulus."),
 ("habituation is a diminished response to a repeated stimulus; extinction is the loss of a conditioned response when the pairing stops",
  "EK 3.7.A.5 versus EK 3.7.A.2.iii. Habituation requires NO prior conditioning; extinction presupposes an established pairing that has ceased. The third distractor is false for exactly that reason, and the first is the contrast reversed. Both are decreases in responding, which is why they are confused."),
 ("deliberately inducing fear in children risks lasting harm",
  "Science practice 2.D, which the CED lists among this topic's suggested skills. Protection from harm limits what may be done to participants, and a deliberately conditioned fear that may generalize (EK 3.7.A.2.iv) and be spontaneously recovered (EK 3.7.A.2.iii) is a harm the framework's own content predicts will persist."),
 ("classical conditioning of emotional responses",
  "EK 3.7.A.3. Pairing a feared object with relaxation until the fear subsides is counterconditioning, the intervention that EK names, and it works on an emotional response -- which is what the same EK says can be classically conditioned."),
 ("expectancy theory",
  "The exclusion statement under EK 3.7.A.3 places the expectancy theory outside the scope of the exam. All three distractors are required content -- spontaneous recovery (3.7.A.2.iii), higher-order conditioning (3.7.A.2.v), biological preparedness (3.7.A.4) -- so the item tests the boundary rather than recognition of a term."),
]

psych_check.check(p3_7, CLAIMS, per_topic=30, n_choices=4)
