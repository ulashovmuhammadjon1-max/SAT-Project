# AP PSYCH 5.1 Introduction to Health Psychology — 30 questions
# Required content: CED (c) 2024 College Board, Course Framework V.1, pp. 114-115.
# LO 5.1.A health psychology and issues of physical health and wellness;
# EK 5.1.B.1 stress raises susceptibility to disorders and disease, and has been
#   linked to hypertension, headaches, and immune suppression;
# EK 5.1.B.2 eustress (motivating) vs distress (debilitating); traumatic
#   stressors vs daily hassles; adverse childhood experiences (ACEs);
# EK 5.1.C.1 the general adaptation syndrome -- alarm reaction (via a
#   fight-flight-freeze response), resistance, exhaustion -- with the greatest
#   susceptibility to illness occurring during the EXHAUSTION phase;
# EK 5.1.C.2 the tend-and-befriend theory, which the CED notes seems to occur
#   mostly in women;
# EK 5.1.D.1 problem-focused coping; EK 5.1.D.2 emotion-focused coping.
#
# Health psychology and positive psychology (5.2) are both NEW in the redesigned
# framework -- the pre-2024 course had neither -- so most older test-prep material
# has no coverage of this topic at all.
#
# No sympy: every key's claim is stated item by item in verify_p5_1.py.
TOPIC = ("5.1", "Introduction to Health Psychology", 5)
QUESTIONS = [
 dict(q="Health psychology is best described as the field that studies", choices=[
   "the biological structures underlying sensation and perception",
   "how children acquire language and social skills",
   "how behavior and mental processes relate to physical health and wellness",
   "the diagnosis and classification of psychological disorders"
], ans=2,
   why="LO 5.1.A: health psychology addresses issues of physical health and wellness as they apply to behavior and mental processes. The distractors describe Topics 5.3, 1.6, and 3.5."),

 dict(q="According to the framework, stress is a factor in", choices=[
   "the elimination of physiological arousal",
   "a permanent increase in cognitive capacity",
   "heightened susceptibility to disorders and disease",
   "improved immune function over the long term"
], ans=2,
   why="EK 5.1.B.1 states it directly: stress is a factor in heightened susceptibility to disorders and disease."),

 dict(q="Which set of physiological problems does the framework specifically link to stress?", choices=[
   "fractures, sprains, and lacerations",
   "food allergies, lactose intolerance, and celiac disease",
   "hypertension, headaches, and immune suppression",
   "colorblindness, hearing loss, and myopia"
], ans=2,
   why="EK 5.1.B.1 names exactly these three: stress has been linked to physiological issues such as hypertension, headaches, and immune suppression."),

 dict(q="Eustress refers to stress that is", choices=[
   "motivating",
   "debilitating",
   "entirely absent of physiological arousal",
   "experienced only in childhood"], ans=0,
   why="EK 5.1.B.2: stressors can be viewed as motivating (eustress) or debilitating (distress). Eustress is not the absence of stress but stress experienced as energizing."),

 dict(q="Distress refers to stress that is", choices=[
   "debilitating",
   "motivating",
   "brief rather than prolonged",
   "caused only by physical rather than psychological events"], ans=0,
   why="EK 5.1.B.2 pairs the two terms: distress is the debilitating form, eustress the motivating one. Duration and cause are not what separates them."),

 dict(q="Two musicians face the same recital. One describes the pressure as energizing and performs at her best; the other feels overwhelmed and performs poorly. The framework would describe their experiences as", choices=[
   "eustress for both, since the stressor is identical",
   "neither, since a recital is not a stressor",
   "eustress for the first and distress for the second",
   "distress for the first and eustress for the second"
], ans=2,
   why="EK 5.1.B.2. The stressor is the same, so the distinction lies in how it is experienced -- motivating versus debilitating -- which is exactly the point of having two terms."),

 dict(q="Daily hassles differ from traumatic stressors in that daily hassles", choices=[
   "affect only people who are already unwell",
   "produce no physiological response of any kind",
   "are individually minor but can build up over time",
   "always produce more severe illness than traumatic events"
], ans=2,
   why="EK 5.1.B.2: stressors can be experienced as traumatic or as daily hassles that can BUILD UP over time. Accumulation is what makes small stressors consequential."),

 dict(q="Adverse childhood experiences (ACEs) are significant in health psychology because they", choices=[
   "are unrelated to adult physical health outcomes",
   "have been shown to produce eustress in most people",
   "are sources of stress that can affect a person throughout the lifespan",
   "affect health only during the childhood years themselves"
], ans=2,
   why="EK 5.1.B.2 names ACEs as sources of stress that can affect a person THROUGHOUT THE LIFESPAN -- the point being that the health consequences are not confined to childhood."),

 dict(q="The general adaptation syndrome describes the response to stress as proceeding through which sequence?", choices=[
   "alarm reaction, resistance, exhaustion",
   "resistance, alarm reaction, exhaustion",
   "exhaustion, alarm reaction, resistance",
   "alarm reaction, exhaustion, resistance"], ans=0,
   why="EK 5.1.C.1 gives the order: alarm reaction when the stress is first encountered, then resistance as the stress is confronted, then exhaustion."),

 dict(q="The alarm reaction phase of the general adaptation syndrome occurs", choices=[
   "after the body's resources have been depleted",
   "only if the stressor lasts several weeks",
   "once the person has successfully removed the stressor",
   "when the stressor is first encountered, via a fight-flight-freeze response"
], ans=3,
   why="EK 5.1.C.1: initially, alarm reaction occurs when the stress is encountered, via a fight-flight-freeze response."),

 dict(q="The resistance phase of the general adaptation syndrome is characterized by", choices=[
   "sustained mobilization of resources while the stress is being confronted",
   "the first sudden burst of arousal on encountering the stressor",
   "the depletion of the body's resources",
   "a complete return to the pre-stress baseline"], ans=0,
   why="EK 5.1.C.1: a resistance phase occurs as the stress is CONFRONTED -- the body stays mobilized rather than returning to baseline, which is why the phase is costly."),

 dict(q="According to the general adaptation syndrome, the exhaustion phase occurs", choices=[
   "when the stress subsides or the body's resources are spent",
   "immediately upon first encountering any stressor",
   "only in people who have experienced adverse childhood experiences",
   "whenever a person uses emotion-focused coping"], ans=0,
   why="EK 5.1.C.1 states it in these terms: an exhaustion phase occurs when the stress subsides, or resources are spent."),

 dict(q="During which phase of the general adaptation syndrome is susceptibility to illness greatest?", choices=[
   "resistance",
   "susceptibility is equal across all three phases",
   "exhaustion",
   "alarm reaction"
], ans=2,
   why="EK 5.1.C.1 states explicitly that the greatest susceptibility to illness occurs during the EXHAUSTION phase. The intuitive guess is the alarm phase, because that is when arousal peaks, and it is wrong."),

 dict(q="The tend-and-befriend theory proposes that some people respond to stress by", choices=[
   "suppressing every outward sign of the stress",
   "tending to their own or others' needs and seeking connection with others",
   "withdrawing entirely from all social contact",
   "confronting the source of the stress with aggression"
], ans=1,
   why="EK 5.1.C.2: the tend-and-befriend theory proposes that some people react to stress by tending to their own needs and/or the needs of others and seeking connection with others."),

 dict(q="What does the framework note about the distribution of the tend-and-befriend response?", choices=[
   "It seems to occur mostly in women",
   "It seems to occur mostly in men",
   "It occurs equally often in all groups",
   "It has only been observed in non-human animals"], ans=0,
   why="EK 5.1.C.2 states that this phenomenon seems to occur mostly in women. The hedged wording is the framework's own."),

 dict(q="How does the tend-and-befriend response differ from the fight-flight-freeze response?", choices=[
   "Tend-and-befriend involves no physiological change of any kind",
   "Tend-and-befriend occurs only after the exhaustion phase",
   "Tend-and-befriend turns toward others and toward caregiving, while fight-flight-freeze prepares the body to confront, escape, or become immobile",
   "Tend-and-befriend prepares the body to escape, while fight-flight-freeze turns toward caregiving"
], ans=2,
   why="EK 5.1.C.1 attaches fight-flight-freeze to the alarm reaction; EK 5.1.C.2 describes tend-and-befriend as an alternative pattern oriented toward connection and care rather than confrontation or escape."),

 dict(q="Problem-focused coping involves", choices=[
   "waiting for the stressor to resolve without acting",
   "treating the stressor as a problem to be solved and working at solutions until one is found",
   "managing the emotional reaction the stressor produces",
   "avoiding thinking about the stressor entirely"
], ans=1,
   why="EK 5.1.D.1, in substance verbatim: problem-focused coping involves seeing stress as a problem to be solved and working solutions until a solution is found."),

 dict(q="Emotion-focused coping involves", choices=[
   "managing one's emotional reactions to the stressor",
   "removing the source of the stress directly",
   "increasing the intensity of the stressor to build tolerance",
   "assigning responsibility for the stressor to another person"], ans=0,
   why="EK 5.1.D.2: emotion-focused coping involves managing emotional reactions to stress as a means of coping. Strategies named include deep breathing, meditation, and medication aimed at reducing stressful emotional responses."),

 dict(q="A student overwhelmed by a heavy course load sits down, lists every assignment, builds a schedule, and begins working through it. This is", choices=[
   "the tend-and-befriend response",
   "problem-focused coping",
   "emotion-focused coping",
   "the alarm reaction phase of the general adaptation syndrome"
], ans=1,
   why="EK 5.1.D.1. The action is aimed at the stressor itself -- organizing and reducing the workload -- rather than at the feelings the workload produces."),

 dict(q="A person awaiting the result of a medical test they cannot influence practices deep breathing and meditation to stay calm. This is", choices=[
   "an adverse childhood experience",
   "emotion-focused coping",
   "problem-focused coping",
   "the resistance phase of the general adaptation syndrome"
], ans=1,
   why="EK 5.1.D.2 names deep breathing and meditation among emotion-focused strategies. The target is the emotional reaction, not the stressor, which in this case cannot be altered."),

 dict(q="Coping research generally finds that problem-focused strategies are most useful when", choices=[
   "the stressor is something the person can actually change",
   "the stressor is entirely outside the person's control",
   "the person has already reached the exhaustion phase",
   "the stressor is a traumatic rather than a daily one"], ans=0,
   why="EK 5.1.D.1 defines problem-focused coping as working solutions until a solution is found, which presupposes a stressor that admits of a solution. When nothing can be changed, effort spent on solving is effort wasted, and EK 5.1.D.2's emotion-focused strategies fit better."),

 dict(q="What is the clearest difference between problem-focused and emotion-focused coping?", choices=[
   "Problem-focused coping targets the stressor itself, while emotion-focused coping targets the person's reaction to it",
   "Problem-focused coping targets the reaction, while emotion-focused coping targets the stressor",
   "Problem-focused coping is always more effective than emotion-focused coping",
   "Problem-focused coping is unconscious, while emotion-focused coping is deliberate"], ans=0,
   why="EK 5.1.D.1 and 5.1.D.2. The discriminator is the TARGET of the effort. Neither is universally superior -- which strategy fits depends on whether the stressor can be changed."),

 dict(q="Taking prescribed medication to reduce a stressful emotional response is classified by the framework as", choices=[
   "a problem-focused coping strategy",
   "an instance of the alarm reaction",
   "a form of eustress",
   "an emotion-focused coping strategy"
], ans=3,
   why="EK 5.1.D.2 names taking medication aimed at reducing stressful emotional responses among emotion-focused strategies, alongside deep breathing and meditation."),

 dict(q="A researcher reports that people reporting more chronic stress also report more frequent illness. The strongest conclusion available is that", choices=[
   "stress and illness are unrelated",
   "chronic stress and illness frequency are associated in this sample",
   "chronic stress causes illness",
   "illness causes people to report more stress"
], ans=1,
   why="Research-methods item (Science Practice 2.C). Both variables were measured rather than manipulated, so the correlation supports only an associational claim; either causal direction, or a third variable, remains possible."),

 dict(q="Which is the best operational definition of 'stress' for a study measuring daily hassles?", choices=[
   "the amount of underlying tension present in a participant's psyche",
   "whether a participant seems like a stressed person",
   "the number of hassles a participant records in a standardized daily diary over two weeks",
   "how burdened a participant feels by life in general"
], ans=2,
   why="Research-methods item (Science Practice 2.B). An operational definition specifies the observable measurement procedure. The other three restate the construct without specifying how anything would be counted."),

 dict(q="A study asks adults to report adverse experiences from their childhood and relates those reports to current health. A key methodological limitation is that", choices=[
   "adult health cannot be measured objectively",
   "adverse childhood experiences cannot be studied at all",
   "the design requires random assignment to adverse experiences",
   "the childhood reports depend on memory collected long after the events, which may be incomplete or inaccurate"
], ans=3,
   why="Research-methods item (Science Practice 2.C). This is a retrospective design and its central weakness is recall accuracy. Random assignment is not merely impractical here but ethically impossible, which is why the correlational design is used."),

 dict(q="Which finding would most directly SUPPORT the framework's claim that stress raises susceptibility to disease?", choices=[
   "Participants can accurately describe what stress feels like",
   "Participants exposed to a virus under controlled conditions develop symptoms more often when they report higher prior stress",
   "Participants report feeling tired after a stressful week",
   "Participants who are ill report that being ill is unpleasant"
], ans=1,
   why="Argumentation item (Science Practice 4.B). EK 5.1.B.1's claim is about susceptibility to disease, so the supporting evidence must link prior stress to an objective disease outcome under controlled exposure. The other findings concern subjective experience and bear on nothing."),

 dict(q="A person who has managed a demanding project for months without a break begins catching every passing illness once the project finally ends. In terms of the general adaptation syndrome, this pattern reflects", choices=[
   "the alarm reaction, since the illness appeared suddenly",
   "the resistance phase, since the project was completed successfully",
   "eustress, since the project was a motivating challenge",
   "the exhaustion phase, when resources are spent and susceptibility to illness is greatest"
], ans=3,
   why="EK 5.1.C.1. Illness appearing AFTER the stress subsides, once resources are spent, is the exhaustion phase, which the framework identifies as the point of greatest susceptibility -- and the timing is exactly what makes this the recognizable case."),

 dict(q="A researcher proposes to induce severe distress in participants to observe the exhaustion phase directly. The strongest ethical objection is that", choices=[
   "the study would require too many participants",
   "the exhaustion phase is not a psychological construct",
   "distress cannot be measured in a laboratory",
   "the design exposes participants to a risk of harm that cannot be justified by the knowledge gained"
], ans=3,
   why="Ethics item (Science Practice 2.D). Research must minimize harm, and deliberately driving participants to resource depletion imposes a serious risk that a milder design could avoid -- which is why the stress-illness literature relies on correlational and naturally occurring stressors."),

 dict(q="A person facing a job loss updates her resume and applies for positions, and also runs each morning to manage her anxiety. Her approach is best described as", choices=[
   "not coping, since the stressor has not been removed",
   "using problem-focused and emotion-focused strategies together",
   "using problem-focused coping only",
   "using emotion-focused coping only"
], ans=1,
   why="EK 5.1.D.1 and 5.1.D.2 are not mutually exclusive. Applying for positions targets the stressor; running to manage anxiety targets the emotional reaction, so both categories are in use at once."),
]
