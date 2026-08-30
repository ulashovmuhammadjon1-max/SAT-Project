# AP PSYCH 4.3 Psychology of Social Situations — 30 questions
# Required content: CED (c) 2024 College Board, Course Framework V.1, pp. 99-100.
# EK 4.3.A.1 social norms; 4.3.A.2 normative vs informational social influence;
# 4.3.A.3 persuasion, 4.3.A.3.i elaboration likelihood model + halo effect,
# 4.3.A.3.ii foot-in-the-door / door-in-the-face; 4.3.A.4 conformity research;
# 4.3.A.5 obedience research; 4.3.B.1 individualism/collectivism/multiculturalism;
# 4.3.B.2 group polarization, groupthink, diffusion of responsibility, social
# loafing, deindividuation; 4.3.B.3 social facilitation; 4.3.B.4 false consensus
# effect; 4.3.B.5 superordinate goals and social traps; 4.3.B.6 I/O psychology and
# burnout; 4.3.C.1 altruism and the reciprocity/responsibility norms;
# 4.3.C.2 bystander effect.
#
# The current CED names NO researchers in its required content (a search of the
# whole PDF finds Asch, Milgram, Rogers, Bandura and Festinger zero times). The
# classic studies are described here because every course teaches them, but each
# item is written so the description alone makes the answer derivable -- no item
# turns on recalling a surname.
#
# No sympy: every key's claim is stated item by item in verify_p4_3.py.
TOPIC = ("4.3", "Psychology of Social Situations", 4)
QUESTIONS = [
 dict(q="Social norms are best described as", choices=[
   "the emotions a society considers most valuable",
   "a society's expectations about the behavior and roles appropriate to its members",
   "laws that carry a formal penalty when they are broken",
   "the personality traits most common in a given society"
], ans=1,
   why="EK 4.3.A.1: social norms define the expectations and roles a society may have for its members in individual and social situations; they need not be codified as law."),

 dict(q="Normative social influence leads a person to go along with a group because the person", choices=[
   "believes the group has better information than they do",
   "has been given a direct order by someone in authority",
   "has already agreed to a smaller request from the group",
   "wants to be accepted by the group or avoid its disapproval"
], ans=3,
   why="EK 4.3.A.2 distinguishes normative from informational pressure: normative influence operates through the desire for acceptance and the fear of rejection."),

 dict(q="A tourist unsure which line to join at an unfamiliar train station watches what everyone else does and copies them. This behavior reflects", choices=[
   "informational social influence",
   "normative social influence",
   "obedience to a legitimate authority",
   "deindividuation in a crowd"], ans=0,
   why="EK 4.3.A.2: informational influence operates when others are treated as a source of evidence about what is correct, which is what an uncertain person in an unfamiliar setting does."),

 dict(q="Conformity is best defined as", choices=[
   "following an instruction issued by an authority figure",
   "changing an attitude after carefully evaluating an argument",
   "adjusting one's behavior or thinking to match a group standard, without being asked to",
   "agreeing to a direct request made by another person"
], ans=2,
   why="Conformity involves no explicit request and no authority: the person aligns with an unspoken group norm (EK 4.3.A.4). The other options define compliance, obedience, and central-route persuasion."),

 dict(q="In a classic line-judgment study, participants gave an obviously incorrect answer about which line matched a standard after hearing several confederates give that same wrong answer first. Most conforming participants later reported that they had known the answer was wrong. This pattern indicates that the conformity was mainly", choices=[
   "obedience, because the experimenter had ordered them to agree",
   "compliance, because participants had been asked directly to agree",
   "normative, because participants knew the correct answer and still went along",
   "informational, because participants genuinely doubted their own eyes"
], ans=2,
   why="Knowing the right answer rules out an informational account: the pressure was the social cost of dissenting, which is normative influence (EK 4.3.A.2, 4.3.A.4)."),

 dict(q="In studies of the conditions affecting conformity, the sharpest DROP in conformity occurs when", choices=[
   "the size of the majority is increased from three people to eight",
   "responses are given aloud rather than written privately",
   "the task is made more ambiguous and difficult to judge",
   "one other person in the group breaks the unanimity by dissenting"
], ans=3,
   why="EK 4.3.A.4 concerns the conditions that strengthen conformity. Unanimity is the crucial one: a single ally breaks it and conformity falls sharply, whereas the other three listed changes all RAISE conformity."),

 dict(q="Compliance, as distinguished from conformity and obedience, refers to", choices=[
   "carrying out an order from a recognized authority figure",
   "changing a private belief to match a publicly stated one",
   "agreeing to a direct request from someone who holds no authority over you",
   "matching one's behavior to an unspoken group norm"
], ans=2,
   why="The three constructs are separated by what produces the behavior: an unspoken norm (conformity), an explicit request from a peer (compliance), or a directive from an authority (obedience)."),

 dict(q="A canvasser first asks a homeowner to sign a short petition, and a week later asks the same homeowner to display a large sign in the yard, which the homeowner agrees to do. This technique is", choices=[
   "informational social influence",
   "the foot-in-the-door technique",
   "the door-in-the-face technique",
   "the central route to persuasion"
], ans=1,
   why="EK 4.3.A.3.ii. Foot-in-the-door begins with a SMALL request that is granted and escalates to the larger target request."),

 dict(q="A fundraiser asks for a $500 annual pledge, is refused, and then asks for $25, which the donor accepts. This sequence illustrates", choices=[
   "the halo effect",
   "group polarization",
   "the door-in-the-face technique",
   "the foot-in-the-door technique"
], ans=2,
   why="EK 4.3.A.3.ii. Door-in-the-face opens with a LARGE request expected to be refused, so the smaller real request appears to be a concession."),

 dict(q="In classic obedience research, participants were instructed by an experimenter to deliver what they believed were increasingly severe shocks to another person. Obedience rates were LOWEST when", choices=[
   "the study was described as sponsored by a prestigious university",
   "the participant could not see or hear the other person at all",
   "the experimenter gave instructions by telephone from another room",
   "the experimenter stood beside the participant in a laboratory coat"
], ans=2,
   why="EK 4.3.A.5 concerns the conditions strengthening obedience: physical presence and perceived legitimacy of the authority raise it, so removing the authority from the room lowers it, while increasing distance from the victim raises it."),

 dict(q="A student wears the same brand of shoes as her friends without anyone mentioning it, later agrees when a classmate asks her to swap seats, and then hands in her phone when the principal instructs the class to do so. These three behaviors are, in order,", choices=[
   "obedience, compliance, conformity",
   "conformity, obedience, compliance",
   "conformity, compliance, obedience",
   "compliance, conformity, obedience"
], ans=2,
   why="The discriminating question is what produced each behavior: an unspoken norm, a peer's direct request, and an authority's directive respectively."),

 dict(q="According to the elaboration likelihood model, a person is persuaded by the CENTRAL route when they", choices=[
   "accept a claim because it was repeated many times",
   "carefully evaluate the substance and quality of the arguments presented",
   "are swayed by the speaker's attractiveness or confident delivery",
   "agree because a large majority already agrees"
], ans=1,
   why="EK 4.3.A.3.i: the elaboration likelihood model outlines a central and a peripheral route; the central route runs through effortful evaluation of the argument itself."),

 dict(q="A voter who supports a candidate because the candidate is polished and good-looking, without examining any policy positions, has been persuaded", choices=[
   "by the peripheral route, through the halo effect",
   "by the central route, through argument quality",
   "through informational social influence",
   "through the door-in-the-face technique"], ans=0,
   why="EK 4.3.A.3.i names the halo effect as an example of a PERIPHERAL route cue: a favorable impression in one domain spreads to unrelated judgments without any argument being evaluated."),

 dict(q="A culture that emphasizes personal goals, individual achievement, and self-reliance over group obligation is best described as", choices=[
   "individualist",
   "collectivist",
   "multicultural",
   "ethnocentric"
], ans=0,
   why="EK 4.3.B.1 lists individualism, collectivism, and multiculturalism as cultural phenomena influencing how one perceives and behaves toward oneself and others; individualism prioritizes the person over the group."),

 dict(q="A committee whose members already mildly favored a proposal discusses it for an hour and emerges strongly in favor. This shift illustrates", choices=[
   "the false consensus effect",
   "group polarization",
   "groupthink",
   "social facilitation"
], ans=1,
   why="EK 4.3.B.2. Group polarization is the STRENGTHENING of the group's pre-existing dominant leaning through discussion; nothing here indicates that dissent was suppressed."),

 dict(q="A tightly knit team suppresses a member's doubts about a plan because everyone wants to preserve agreement, and the team adopts the plan without examining alternatives. This is", choices=[
   "groupthink",
   "group polarization",
   "social loafing",
   "deindividuation"
], ans=0,
   why="EK 4.3.B.2. Groupthink is defined by the desire for harmony and consensus overriding a realistic appraisal of alternatives; the diagnostic detail is the suppressed dissent."),

 dict(q="Five students are graded on a single shared product, and each puts in noticeably less effort than when graded individually. This reduction in effort is", choices=[
   "groupthink",
   "social loafing",
   "social facilitation",
   "deindividuation"
], ans=1,
   why="EK 4.3.B.2. Social loafing is reduced individual effort on a collective task whose output is pooled, so no one person's contribution is identifiable."),

 dict(q="Members of a large costumed crowd behave far more recklessly than any of them would alone, and afterward describe feeling anonymous and swept along. This is best explained by", choices=[
   "social loafing",
   "the bystander effect",
   "informational social influence",
   "deindividuation"
], ans=3,
   why="EK 4.3.B.2. Deindividuation is the loss of self-awareness and normal self-restraint that group anonymity and arousal produce; social loafing concerns effort, not restraint."),

 dict(q="An experienced pianist performs a well-rehearsed piece noticeably better in front of an audience than when practicing alone. This improvement illustrates", choices=[
   "group polarization",
   "the false consensus effect",
   "normative social influence",
   "social facilitation"
], ans=3,
   why="EK 4.3.B.3: performing a mental or physical behavior in front of a group can lead to social facilitation. The piece being well rehearsed is what makes improvement rather than impairment the expected outcome."),

 dict(q="A student who dislikes a new school policy assumes that most other students dislike it too, when in fact opinion is evenly divided. This assumption illustrates", choices=[
   "groupthink",
   "in-group bias",
   "informational social influence",
   "the false consensus effect"
], ans=3,
   why="EK 4.3.B.4: people often overestimate the levels to which others agree with them. Groupthink is excluded because no group deliberation has occurred."),

 dict(q="Two rival departments that have feuded for years are assigned a project that neither can complete alone, and their hostility declines. The mechanism at work is", choices=[
   "the reciprocity norm",
   "a superordinate goal",
   "a social trap",
   "group polarization"
], ans=1,
   why="EK 4.3.B.5: superordinate goals unite disparate groups under a common goal and help reduce negative affect and stereotyping among them. A social trap is the opposite case, in which self-interested action harms the group."),

 dict(q="Every fisher on a lake takes as large a catch as possible, and the fish population collapses, leaving all of them worse off. This situation is", choices=[
   "a superordinate goal",
   "diffusion of responsibility",
   "social loafing",
   "a social trap"
], ans=3,
   why="EK 4.3.B.5: social traps occur when individuals do not unite and act in their own self-interest to the detriment of the group. Nobody's effort is reduced, which rules out social loafing."),

 dict(q="An industrial-organizational psychologist studying employees who report emotional exhaustion and detachment from work they once cared about is investigating", choices=[
   "an approach-avoidance conflict",
   "the halo effect",
   "burnout",
   "deindividuation"
], ans=2,
   why="EK 4.3.B.6: I/O psychologists study how people perform in the workplace and how they feel about work, and the CED names burnout specifically."),

 dict(q="A person collapses in a crowded plaza and, although dozens of people notice, no one steps forward. The best-supported explanation is that each onlooker", choices=[
   "assumed that someone else in the crowd would take responsibility for helping",
   "was personally indifferent to the person's welfare",
   "wanted to be accepted by the other onlookers",
   "was following an instruction from someone in authority"], ans=0,
   why="EK 4.3.C.2 states that situational and attentional variables predict helping, and EK 4.3.B.2 names diffusion of responsibility; the presence of many potential helpers spreads the felt obligation thin. The bystander effect is a situational finding, not evidence about individual character."),

 dict(q="A neighbor shovels the walk of an elderly resident who cannot do it herself and expects nothing in return. This behavior is best explained by", choices=[
   "the social responsibility norm",
   "the social reciprocity norm",
   "the false consensus effect",
   "normative social influence"], ans=0,
   why="EK 4.3.C.1 names both norms: the responsibility norm covers helping those who depend on us regardless of return, while the reciprocity norm covers repaying those who have helped us."),

 dict(q="A workplace that actively maintains the distinct cultural identities of its employees rather than expecting them to adopt a single dominant culture is best characterized as", choices=[
   "multicultural",
   "collectivist",
   "individualist",
   "deindividuated"
], ans=0,
   why="EK 4.3.B.1 lists multiculturalism alongside individualism and collectivism; it is the maintenance of multiple distinct cultural identities rather than a position on the individual-versus-group dimension."),

 dict(q="Some researchers argue that behavior which appears altruistic is not entirely selfless because helpers may be", choices=[
   "conforming to the judgments of a unanimous majority",
   "responding to social debt created by norms of exchange and obligation",
   "unable to recognize that another person needs help",
   "acting on a directive from a person in authority"
], ans=1,
   why="EK 4.3.C.1 states that altruism refers to selfless behavior but that some researchers suggest people act prosocially due to incurring social debt, explained by the reciprocity and responsibility norms."),

 dict(q="A colleague who covered several of a coworker's shifts last month now asks that coworker for a favor, and the coworker agrees at once. The coworker's willingness is best explained by", choices=[
   "the social responsibility norm",
   "the foot-in-the-door technique",
   "diffusion of responsibility",
   "the social reciprocity norm"
], ans=3,
   why="EK 4.3.C.1: the reciprocity norm covers returning help to someone who has helped you, which is what a prior debt creates. The responsibility norm concerns helping those who depend on us regardless of any prior favor, and no escalating sequence of requests occurred."),

 dict(q="Obedience research in which participants believed they were harming another person is now the standard case study in research ethics. The clearest ethical concern such a study raises is that", choices=[
   "the researchers failed to obtain a large enough sample",
   "the results could not be replicated by other laboratories",
   "participants were assigned to conditions at random",
   "participants experienced substantial distress they had not been warned of when consenting"
], ans=3,
   why="Ethics item (Science Practice 2.D). Informed consent requires that participants know the risks they are accepting; deception about the nature of the task meant they could not. Random assignment is a design strength, and sample size and replication are methodological rather than ethical issues."),

 dict(q="To study whether group size affects helping, a researcher stages the same emergency in a public setting and varies only the number of bystanders present, recording how often help is offered. This study is best described as", choices=[
   "a naturalistic observation, because it took place in a public setting",
   "a case study, because a single emergency was examined in depth",
   "an experiment, because the researcher manipulated group size",
   "a correlational study, because two variables were measured together"
], ans=2,
   why="Research-design item (Science Practice 2.A). The defining feature of an experiment is that the researcher manipulates a variable; a public setting does not make a manipulated study naturalistic observation, which requires observing without intervening."),
]
