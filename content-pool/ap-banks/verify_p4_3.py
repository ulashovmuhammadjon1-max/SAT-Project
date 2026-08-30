"""Key verification for AP PSYCH 4.3 (Psychology of Social Situations).

No computation is possible here, so for EVERY item the specific claim the key
rests on is written out: a CED definition, a named study's actual result, or
what a theory actually predicts. That statement is what replaces sympy.

Source: AP Psychology Course and Exam Description, (c) 2024 College Board,
Course Framework V.1, Topic 4.3, pp. 99-100.

The three constructs this topic is most often got wrong on are separated by
WHAT PRODUCES THE BEHAVIOR, and every item below is keyed to that test:
  conformity  -- an unspoken group norm, nobody asks (line-judgment studies)
  compliance  -- an explicit request from someone with no authority
                 (foot-in-the-door, door-in-the-face)
  obedience   -- a directive from a recognized authority (shock-generator studies)

Run: python3 verify_p4_3.py
"""
import p4_3
from psych_check import check

CLAIMS = [
 ("expectations about the behavior and roles appropriate to its members",
  "EK 4.3.A.1: social norms define the expectations and roles a society may have "
  "for its members in individual and social situations. Nothing in the definition "
  "requires codification, which is why the 'laws with a formal penalty' option is "
  "wrong -- most norms carry only social sanction."),

 ("wants to be accepted by the group or avoid its disapproval",
  "EK 4.3.A.2: social pressure can be normative or informational. Normative "
  "influence runs through the desire for acceptance and the fear of rejection, "
  "not through any belief that the group is better informed."),

 ("informational social influence",
  "EK 4.3.A.2. The tourist is UNCERTAIN and treats others as evidence about what "
  "is correct, which is the informational route. Normative influence would require "
  "a concern about the group's approval, which the item does not describe."),

 ("adjusting one's behavior or thinking to match a group standard, without being asked",
  "Conformity involves no explicit request and no authority (EK 4.3.A.4). The "
  "distractors are precise definitions of compliance (a direct request), obedience "
  "(an authority's instruction), and central-route persuasion."),

 ("normative, because participants knew the correct answer",
  "The line-judgment result: participants who conformed to a unanimous wrong "
  "majority typically reported afterward that they had known the answer was wrong. "
  "Knowing the correct answer rules out an INFORMATIONAL account -- the pressure "
  "was the social cost of dissenting, i.e. normative (EK 4.3.A.2). No request was "
  "made and no authority ordered anything, ruling out compliance and obedience."),

 ("one other person in the group breaks the unanimity",
  "EK 4.3.A.4 concerns conditions affecting conformity. Unanimity is the critical "
  "one: a single dissenting ally causes conformity to fall sharply. Every other "
  "option listed -- a larger majority, public rather than private responding, and "
  "a more ambiguous task -- RAISES conformity, which is what makes them effective "
  "distractors."),

 ("direct request from someone who holds no authority",
  "The middle term of the three-way distinction. Compliance requires an explicit "
  "request; conformity requires none; obedience requires the requester to hold "
  "authority."),

 ("foot-in-the-door",
  "EK 4.3.A.3.ii. The sequence is SMALL request granted first, larger target "
  "request second. The order of the two requests is the whole discriminator "
  "against door-in-the-face."),

 ("door-in-the-face",
  "EK 4.3.A.3.ii. The sequence is a LARGE request expected to be refused, then the "
  "smaller real request, which now reads as a concession. Reversing the order "
  "converts it to foot-in-the-door, which is the error to guard against."),

 ("experimenter gave instructions by telephone from another room",
  "EK 4.3.A.5 concerns the conditions that strengthen obedience. The physical "
  "presence and perceived legitimacy of the authority both raise obedience, so "
  "removing the authority to another room lowers it. The last option is the "
  "reversal trap: greater distance from the person being harmed RAISES obedience "
  "rather than lowering it."),

 ("conformity, compliance, obedience",
  "Three-way discrimination, keyed to what produced each behavior: an unspoken "
  "norm nobody mentioned (conformity), a peer's direct request (compliance), and "
  "an authority's instruction (obedience). The permutations are the distractors."),

 ("carefully evaluate the substance and quality of the arguments",
  "EK 4.3.A.3.i: the elaboration likelihood model outlines two routes, central and "
  "peripheral. The central route runs through effortful evaluation of the argument "
  "itself; the other three options are all peripheral cues."),

 ("peripheral route, through the halo effect",
  "EK 4.3.A.3.i names the halo effect explicitly as an example of a peripheral "
  "route to persuasion: a favorable impression on one dimension (appearance) "
  "spreads to unrelated judgments, with no argument evaluated."),

 ("individualist",
  "EK 4.3.B.1 lists individualism, collectivism, and multiculturalism. "
  "Individualism prioritizes personal goals and achievement over group "
  "obligation. Ethnocentrism is a different construct -- an evaluative standard, "
  "not a value orientation about the individual and the group."),

 ("group polarization",
  "EK 4.3.B.2. Group polarization is the STRENGTHENING of a group's pre-existing "
  "dominant leaning through discussion. The item deliberately supplies no "
  "suppressed dissent, which is what would be needed for groupthink."),

 ("groupthink",
  "EK 4.3.B.2. Groupthink is the desire for harmony and consensus overriding a "
  "realistic appraisal of alternatives; the diagnostic detail here is that a "
  "member's doubts were suppressed to preserve agreement. Polarization involves "
  "no such suppression."),

 ("social loafing",
  "EK 4.3.B.2. Social loafing is reduced individual effort on a collective task "
  "whose output is pooled so no contribution is identifiable. Note it is the "
  "OPPOSITE direction of effect from social facilitation, which is why that is the "
  "distractor to beat."),

 ("deindividuation",
  "EK 4.3.B.2. Deindividuation is the loss of self-awareness and normal restraint "
  "produced by anonymity and arousal in a group. Social loafing concerns reduced "
  "EFFORT, not reduced restraint -- a distinction students routinely collapse."),

 ("social facilitation",
  "EK 4.3.B.3: performing a mental or physical behavior in front of a group can "
  "lead to social facilitation. The piece being WELL REHEARSED is the detail that "
  "makes improvement, rather than impairment, the expected outcome."),

 ("false consensus effect",
  "EK 4.3.B.4: people often overestimate the levels to which others agree with "
  "them. Groupthink is excluded because no group deliberation has taken place -- "
  "this is a solitary misjudgment about a distribution of opinion."),

 ("superordinate goal",
  "EK 4.3.B.5: superordinate goals unite disparate groups under a common goal and "
  "help reduce negative affect and stereotyping among groups. The detail that "
  "neither department can finish alone is what makes the goal superordinate rather "
  "than merely shared."),

 ("social trap",
  "EK 4.3.B.5: social traps occur when individuals do not unite and act in their "
  "own self-interest to the detriment of the group. Each fisher's catch is "
  "individually rational and collectively ruinous. No one reduces effort, which "
  "rules out social loafing."),

 ("burnout",
  "EK 4.3.B.6: I/O psychologists study how people perform in the workplace, "
  "relationships among people working together, and how people feel about work "
  "(burnout). Emotional exhaustion and detachment from previously valued work is "
  "the construct the CED names here."),

 ("assumed that someone else in the crowd would take responsibility",
  "EK 4.3.C.2 states that situational and attentional variables predict whether "
  "someone helps, and EK 4.3.B.2 names diffusion of responsibility. The finding is "
  "SITUATIONAL: the presence of many potential helpers thins the felt obligation. "
  "The 'personally indifferent' option is the dispositional misreading of the "
  "bystander literature and is exactly the fundamental attribution error applied "
  "to it."),

 ("social responsibility norm",
  "EK 4.3.C.1 names both norms. The responsibility norm covers helping those who "
  "depend on us regardless of return; the reciprocity norm requires a prior favor "
  "to repay, and the item states none was given."),

 ("multicultural",
  "EK 4.3.B.1 lists multiculturalism alongside individualism and collectivism. It "
  "is the maintenance of distinct cultural identities rather than a position on "
  "the individual-versus-group dimension, so the collectivist and individualist "
  "options answer a different question."),

 ("responding to social debt",
  "EK 4.3.C.1, near-verbatim: altruism refers to selfless behavior, but some "
  "researchers suggest people act in prosocial ways due to incurring social debt, "
  "which the social reciprocity norm and the social responsibility norm explain."),

 ("social reciprocity norm",
  "EK 4.3.C.1. A prior favor creates the debt the reciprocity norm discharges. "
  "The responsibility norm is excluded because the colleague is not a dependent "
  "party, and foot-in-the-door is excluded because there is no escalating sequence "
  "of requests -- the earlier act was help GIVEN, not a small request granted."),

 ("substantial distress they had not been warned of",
  "Ethics item (Science Practice 2.D). Informed consent requires that participants "
  "know the risks they accept; deception about the task's nature meant they could "
  "not. Random assignment is a design STRENGTH, and sample size and replication "
  "are methodological rather than ethical concerns -- the distinction the practice "
  "is testing."),

 ("an experiment, because the researcher manipulated group size",
  "Research-design item (Science Practice 2.A). The defining feature of an "
  "experiment is manipulation of a variable. A public setting does not make the "
  "study naturalistic observation, which requires observing WITHOUT intervening -- "
  "and staging an emergency is intervening."),
]

check(p4_3, CLAIMS)
