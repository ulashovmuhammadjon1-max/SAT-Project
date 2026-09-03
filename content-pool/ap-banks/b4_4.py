# AP BIOLOGY 4.4 Feedback
# CED effective Fall 2025, Unit 4 Cell Communication and Cell Cycle.
# Big Idea 2 Energetics. Learning objective 4.4.A, explain how positive and
# negative feedback helps maintain homeostasis. Suggested skill 6.E, predict
# the causes or effects of a change in, or disruption to, one or more
# components in a biological system.
#
# Essential knowledge, in the framework's own terms:
#   4.4.A.1     Organisms use FEEDBACK MECHANISMS to maintain their internal
#               environments in response to INTERNAL AND EXTERNAL CHANGES.
#     i.        NEGATIVE feedback mechanisms maintain homeostasis by REDUCING
#               THE INITIAL STIMULUS to regulate physiological processes. If a
#               system is perturbed or disrupted, negative feedback returns the
#               system back to its TARGET SET POINT. These processes operate at
#               the MOLECULAR, CELLULAR, AND ORGANISMAL levels.
#     ii.       POSITIVE feedback mechanisms AMPLIFY responses and processes.
#               The variable initiating the response is MOVED FURTHER AWAY FROM
#               THE INITIAL SET POINT. Amplification occurs when the stimulus is
#               FURTHER INTENSIFIED, which in turn initiates an ADDITIONAL
#               RESPONSE that produces system change.
#
# The CED prints illustrative examples against each sub-statement, and this
# module uses them as instances of the category rather than as facts of their
# own:
#   under EK 4.4.A.1.i   blood sugar regulation by insulin and glucagon
#   under EK 4.4.A.1.ii  lactation in mammals; onset of labor in childbirth;
#                        ripening of fruit
#
# TWO EXAMPLES ARE SHARED WITH OTHER TOPICS AND ARE ASKED DIFFERENTLY HERE.
# Insulin is listed under EK 4.1.B.2 as a long-distance signal, and module b4_1
# asks it as a question about RANGE; item 8 here asks which FEEDBACK CATEGORY
# blood sugar regulation belongs to. Fruit ripening is listed under EK 4.3.B.1
# as a change in gene expression altering phenotype, and module b4_3 asks it
# that way; item 11 here asks which feedback category it is listed under. In
# neither case would one key answer the other question.
#
# NOTHING IS ASSERTED ABOUT HOW A POSITIVE FEEDBACK PROCESS ENDS. The framework
# does not say, so no item here asks. Items about positive feedback are keyed
# only to amplification and to movement away from the initial set point, which
# is what EK 4.4.A.1.ii states.
#
# Tables are labelled HYPOTHETICAL and every keyed conclusion is recoverable
# from the table itself. No stem refers to a figure.
#
# FIVE choices (A-E). Plain prose, no LaTeX.
TOPIC = ("4.4", "Feedback", 4)

_T_RETURN = dict(
    headers=["Time after the disturbance (minutes)",
             "Measured value of the variable (hypothetical units)"],
    rows=[["0", "50"],
          ["5", "72"],
          ["10", "64"],
          ["20", "56"],
          ["40", "51"],
          ["60", "50"]])

_T_AMPLIFY = dict(
    headers=["Time after the stimulus (minutes)",
             "Measured value of the variable (hypothetical units)",
             "Strength of the response produced (hypothetical units)"],
    rows=[["0", "50", "0"],
          ["5", "58", "10"],
          ["10", "70", "26"],
          ["15", "88", "55"],
          ["20", "112", "98"]])

_T_GLUCOSE = dict(
    headers=["Time after a meal (minutes)",
             "Blood glucose (hypothetical, milligrams per deciliter)",
             "Insulin in the blood (hypothetical, arbitrary units)"],
    rows=[["0", "90", "4"],
          ["30", "150", "38"],
          ["60", "120", "25"],
          ["120", "95", "6"],
          ["180", "90", "4"]])

_T_LEVELS = dict(
    headers=["System observed",
             "Deviation from the set point at the start (hypothetical units)",
             "Deviation from the set point one hour later (hypothetical units)"],
    rows=[["Activity of one enzyme, a molecular level process", "20", "3"],
          ["Ion concentration in one cell, a cellular level process", "18", "2"],
          ["Body temperature of a whole animal, an organismal level process", "15", "1"]])

QUESTIONS = [
 dict(q="What does the framework say organisms use feedback mechanisms for?",
   choices=[
     "To maintain their internal environments in response to internal and external changes",
     "To increase the rate at which their cells divide under all conditions",
     "To change their genomes in response to the surroundings",
     "To eliminate every difference between themselves and their surroundings",
     "To remove the need for any exchange with the environment"],
   ans=0,
   why="EK 4.4.A.1 states that organisms use feedback mechanisms to maintain their internal environments in response to internal and external changes. Both sources of change are named."),

 dict(q="How does the framework say a negative feedback mechanism maintains homeostasis?",
   choices=[
     "By reducing the initial stimulus that set the response in motion",
     "By intensifying the initial stimulus that set the response in motion",
     "By removing the set point the system is regulated around",
     "By preventing any stimulus from ever reaching the system",
     "By replacing the disturbed component with a newly synthesized one"],
   ans=0,
   why="EK 4.4.A.1.i states that negative feedback mechanisms maintain homeostasis by reducing the initial stimulus to regulate physiological processes."),

 dict(q="According to the framework, what happens to a perturbed system that has an intact negative feedback mechanism?",
   choices=[
     "It is returned back to its target set point",
     "It is held permanently at the perturbed value",
     "It is driven further away from its target set point",
     "It loses its target set point and adopts a new one at random",
     "It stops responding to any further disturbance"],
   ans=0,
   why="EK 4.4.A.1.i states that if a system is perturbed or disrupted, negative feedback mechanisms return the system back to its target set point."),

 dict(q="At which levels of biological organization does the framework say negative feedback processes operate?",
   choices=[
     "The molecular, the cellular, and the organismal levels",
     "The organismal level only",
     "The molecular level only",
     "The cellular level only",
     "Only levels above the individual organism"],
   ans=0,
   why="EK 4.4.A.1.i states that these processes operate at the molecular, cellular, and organismal levels, naming all three."),

 dict(q="What does the framework say positive feedback mechanisms do?",
   choices=[
     "They amplify responses and processes in biological organisms",
     "They reduce responses and processes in biological organisms",
     "They hold every response at a constant strength",
     "They replace negative feedback in organisms that lack a set point",
     "They prevent any response from beginning"],
   ans=0,
   why="EK 4.4.A.1.ii states that positive feedback mechanisms amplify responses and processes in biological organisms."),

 dict(q="In a positive feedback mechanism, what happens to the variable that initiated the response?",
   choices=[
     "It is moved further away from the initial set point",
     "It is returned to the initial set point",
     "It is held exactly at the initial set point",
     "It ceases to be measurable once the response begins",
     "It becomes the set point for a different variable"],
   ans=0,
   why="EK 4.4.A.1.ii states that the variable initiating the response is moved further away from the initial set point, which is what distinguishes positive from negative feedback."),

 dict(q="How does the framework describe the way amplification occurs in a positive feedback mechanism?",
   choices=[
     "The stimulus is further intensified, which initiates an additional response producing system change",
     "The stimulus is reduced, which initiates a smaller response each time",
     "The stimulus is held constant while the response grows on its own",
     "The response is removed so that only the stimulus remains",
     "The set point is raised until it matches the stimulus"],
   ans=0,
   why="EK 4.4.A.1.ii states that amplification occurs when the stimulus is further intensified, which in turn initiates an additional response that produces system change."),

 dict(q="Blood sugar regulation by insulin and glucagon is listed by the framework as an example of which kind of feedback?",
   choices=[
     "Negative feedback",
     "Positive feedback",
     "Neither kind, because hormones are not feedback mechanisms",
     "Both kinds acting at the same time on the same variable",
     "A mechanism that has no set point of any kind"],
   ans=0,
   why="The CED lists blood sugar regulation by insulin and glucagon as its illustrative example for EK 4.4.A.1.i, the statement about negative feedback returning a system to its target set point."),

 dict(q="Lactation in mammals is listed by the framework as an example of which kind of feedback?",
   choices=[
     "Positive feedback",
     "Negative feedback",
     "A process involving no feedback at all",
     "A process that reduces its own initial stimulus",
     "A process that operates only at the molecular level"],
   ans=0,
   why="The CED lists lactation in mammals as an illustrative example for EK 4.4.A.1.ii, the statement about positive feedback amplifying responses and moving the variable further from the initial set point."),

 dict(q="The onset of labor in childbirth is listed by the framework as an example of which kind of feedback?",
   choices=[
     "Positive feedback, in which the stimulus is further intensified",
     "Negative feedback, in which the stimulus is reduced",
     "A process with no stimulus and no response",
     "A process that returns the system to its target set point",
     "A process restricted to the cellular level"],
   ans=0,
   why="The CED lists the onset of labor in childbirth as an illustrative example for EK 4.4.A.1.ii, which describes amplification through a stimulus that is further intensified, initiating an additional response."),

 dict(q="The ripening of fruit is listed by the framework among the examples of which kind of feedback?",
   choices=[
     "Positive feedback, which amplifies the response",
     "Negative feedback, which reduces the initial stimulus",
     "A process that returns the system to its target set point",
     "A process that occurs without any stimulus",
     "A process that operates only in animals"],
   ans=0,
   why="The CED lists the ripening of fruit among the illustrative examples for EK 4.4.A.1.ii, the statement that positive feedback mechanisms amplify responses and processes in biological organisms."),

 dict(q="What is the clearest way to tell a negative feedback mechanism from a positive one?",
   choices=[
     "Whether the variable is brought back toward the set point or driven further from it",
     "Whether the mechanism involves a hormone or an enzyme",
     "Whether the mechanism occurs in an animal or in a plant",
     "Whether the response is fast or slow",
     "Whether the stimulus originates inside or outside the organism"],
   ans=0,
   why="EK 4.4.A.1.i has negative feedback return the system to its target set point while EK 4.4.A.1.ii has the initiating variable moved further away from the initial set point. Direction relative to the set point is the distinction the framework draws."),

 dict(q="A variable was measured repeatedly after a disturbance, with the results shown. Which kind of feedback do these data indicate?",
   table=_T_RETURN,
   choices=[
     "Negative feedback, because the variable is brought back to the value it started from",
     "Positive feedback, because the variable is driven further from the value it started from",
     "Neither kind, because the variable never changed",
     "Positive feedback, because the variable rose at first",
     "Negative feedback, because the variable ended further from its starting value than it began"],
   ans=0,
   why="EK 4.4.A.1.i states that negative feedback returns a perturbed system back to its target set point, and the series rises after the disturbance and then falls back to its starting value."),

 dict(q="A variable and the response it produces were measured after a stimulus, with the results shown. Which kind of feedback do these data indicate?",
   table=_T_AMPLIFY,
   choices=[
     "Positive feedback, because the variable moves further from its starting value while the response grows",
     "Negative feedback, because the variable moves further from its starting value while the response grows",
     "Positive feedback, because the variable returns to its starting value",
     "Negative feedback, because the response stays the same size throughout",
     "Neither kind, because the response never changes"],
   ans=0,
   why="EK 4.4.A.1.ii states that positive feedback amplifies responses and that the initiating variable is moved further away from the initial set point. Both features are present in the table at every successive time."),

 dict(q="Blood glucose and blood insulin were measured after a meal, with the results shown. Which interpretation is best supported?",
   table=_T_GLUCOSE,
   choices=[
     "A rise in glucose is followed by a rise in insulin and a return of glucose to its starting level",
     "A rise in glucose is followed by a fall in insulin and a further rise in glucose",
     "Insulin rises steadily while glucose rises steadily throughout",
     "Glucose ends the measurement period further from its starting level than it began",
     "Insulin and glucose are unrelated across the measurement period"],
   ans=0,
   why="EK 4.4.A.1.i states that negative feedback returns a perturbed system back to its target set point, and the CED lists blood sugar regulation by insulin and glucagon as its example. The two columns show that pattern."),

 dict(q="Three systems were disturbed and their deviation from the set point measured an hour later, with the results shown. Which conclusion is supported?",
   table=_T_LEVELS,
   choices=[
     "Each system moved back toward its set point, at all three levels of organization observed",
     "Each system moved further from its set point, at all three levels of organization observed",
     "Only the whole-animal system moved back toward its set point",
     "Only the single-enzyme system moved back toward its set point",
     "None of the three systems changed its deviation over the hour"],
   ans=0,
   why="EK 4.4.A.1.i states that negative feedback processes operate at the molecular, cellular, and organismal levels, and the three rows in the table are one system from each of those levels."),

 dict(q="A negative feedback mechanism regulating a variable is disabled while the disturbance that raised the variable continues. What is the most reasonable prediction?",
   choices=[
     "The variable stays away from its set point instead of being returned to it",
     "The variable returns to its set point more quickly than before",
     "The variable becomes the new set point for the system",
     "The disturbance is eliminated by the loss of the mechanism",
     "The mechanism is replaced automatically by a positive feedback mechanism"],
   ans=0,
   why="EK 4.4.A.1.i makes the return to the target set point the work of the negative feedback mechanism, so removing the mechanism removes the return. Skill 6.E asks for the effect of disrupting one component of a system."),

 dict(q="A positive feedback process is under way and the stimulus continues to be further intensified. What does the framework predict about the initiating variable?",
   choices=[
     "It continues to move further away from the initial set point",
     "It moves back toward the initial set point as the response grows",
     "It stops changing once the first response has occurred",
     "It becomes identical to the strength of the response",
     "It causes the set point itself to move with it"],
   ans=0,
   why="EK 4.4.A.1.ii states that the variable initiating the response is moved further away from the initial set point, and that amplification occurs when the stimulus is further intensified, initiating an additional response."),

 dict(q="An animal's body temperature rises above its usual value, and processes begin that bring the temperature back down. Which kind of feedback is this and at what level does it operate?",
   choices=[
     "Negative feedback operating at the organismal level",
     "Positive feedback operating at the organismal level",
     "Negative feedback operating only at the molecular level",
     "Positive feedback operating only at the cellular level",
     "Neither kind, because temperature is set by the surroundings alone"],
   ans=0,
   why="EK 4.4.A.1.i makes returning a perturbed system to its target set point the mark of negative feedback and names the organismal level among the three at which such processes operate."),

 dict(q="One mechanism reduces the stimulus that started it and another intensifies the stimulus that started it. How does the framework classify them?",
   choices=[
     "The first is negative feedback and the second is positive feedback",
     "The first is positive feedback and the second is negative feedback",
     "Both are negative feedback, since both respond to a stimulus",
     "Both are positive feedback, since both produce a response",
     "Neither can be classified without knowing which organism is involved"],
   ans=0,
   why="EK 4.4.A.1.i defines negative feedback by the reduction of the initial stimulus and EK 4.4.A.1.ii defines positive feedback by the stimulus being further intensified. The two definitions assign the two mechanisms directly."),

 dict(q="Why does a mechanism that drives a variable away from its set point still count as a feedback mechanism in the framework's account?",
   choices=[
     "Because the response it produces feeds back on the stimulus, intensifying it further",
     "Because every mechanism in an organism is a feedback mechanism by definition",
     "Because it returns the variable to the set point once the response is complete",
     "Because it operates only at the molecular level, where set points do not apply",
     "Because it involves no stimulus and therefore cannot move anything"],
   ans=0,
   why="EK 4.4.A.1.ii describes the loop explicitly: amplification occurs when the stimulus is further intensified, which in turn initiates an additional response that produces system change. The output acting back on the stimulus is what makes it feedback."),

 dict(q="A student says that positive feedback is beneficial and negative feedback is harmful. What is the best correction?",
   choices=[
     "The two terms describe the direction of the effect on the stimulus, not whether the outcome is good",
     "The student has the two reversed, because negative feedback is the beneficial one",
     "The student is right, because amplification always helps an organism",
     "Neither kind of feedback occurs in healthy organisms",
     "The two terms describe how fast a response occurs rather than what it does"],
   ans=0,
   why="EK 4.4.A.1.i and EK 4.4.A.1.ii define the two by what happens to the stimulus and to the variable relative to the set point. The framework names both among the mechanisms organisms use, and lists ordinary biological processes under each."),

 dict(q="A system with intact negative feedback is perturbed twice, by different amounts. What does the framework predict in both cases?",
   choices=[
     "The system is returned to the same target set point after each perturbation",
     "The system settles at a different set point after each perturbation",
     "The system moves further from its set point after each perturbation",
     "The system responds only to the larger of the two perturbations",
     "The system loses its ability to respond after the first perturbation"],
   ans=0,
   why="EK 4.4.A.1.i states that if a system is perturbed or disrupted, negative feedback mechanisms return the system back to its TARGET set point, a value the mechanism regulates around rather than one set by the disturbance."),

 dict(q="What does the framework mean by the target set point of a regulated system?",
   choices=[
     "The value the negative feedback mechanism returns the system to after a disturbance",
     "The largest value the variable reaches during a disturbance",
     "The value the variable holds only while a positive feedback process is running",
     "The value at which a system stops requiring any energy input",
     "The average of every value the variable has ever taken"],
   ans=0,
   why="EK 4.4.A.1.i states that negative feedback mechanisms return the system back to its target set point, which identifies the set point as the regulated value rather than an extreme or an average."),

 dict(q="The activity of one enzyme in a cell is regulated so that a rise in its product slows its own reaction. How does the framework classify this?",
   choices=[
     "Negative feedback at the molecular level",
     "Positive feedback at the molecular level",
     "Negative feedback at the organismal level",
     "Positive feedback at the organismal level",
     "A process outside the scope of feedback because only one molecule is involved"],
   ans=0,
   why="EK 4.4.A.1.i defines negative feedback by the reduction of the initial stimulus and states that these processes operate at the molecular, cellular, and organismal levels. A product slowing its own production is that mechanism at the first of those levels."),

 dict(q="Which observation would justify the claim that a process is a positive rather than a negative feedback mechanism?",
   choices=[
     "The response grows larger as the variable moves further from its starting value",
     "The response grows larger as the variable moves back toward its starting value",
     "The response is the same size no matter what the variable does",
     "The process occurs in an organism rather than in a laboratory preparation",
     "The process involves a hormone rather than an enzyme"],
   ans=0,
   why="EK 4.4.A.1.ii pairs amplification of the response with movement of the initiating variable further away from the initial set point, so evidence for the claim has to show both features together."),

 dict(q="An organism faces a change originating outside its body and another originating inside it. What does the framework say about the feedback mechanisms involved?",
   choices=[
     "Feedback mechanisms respond to internal and external changes alike",
     "Feedback mechanisms respond only to changes originating outside the body",
     "Feedback mechanisms respond only to changes originating inside the body",
     "Feedback mechanisms respond to neither, since they act before any change",
     "Feedback mechanisms respond only when both kinds of change occur together"],
   ans=0,
   why="EK 4.4.A.1 states that organisms use feedback mechanisms to maintain their internal environments in response to internal AND EXTERNAL changes, naming both sources."),

 dict(q="Two processes are compared: one reduces a rising variable back to its usual value, and the other makes a rising variable rise faster still. Which pairing with the framework's terms is correct?",
   choices=[
     "The first illustrates negative feedback and the second illustrates amplification by positive feedback",
     "The first illustrates amplification by positive feedback and the second illustrates negative feedback",
     "Both illustrate amplification, since both involve a change in the variable",
     "Both illustrate negative feedback, since both involve a response",
     "Neither illustrates feedback, because only a whole organism can show feedback"],
   ans=0,
   why="EK 4.4.A.1.i assigns the reduction of the initial stimulus and the return to the set point to negative feedback, and EK 4.4.A.1.ii assigns amplification and movement away from the set point to positive feedback."),

 dict(q="Which statement about feedback is NOT supported by the framework?",
   choices=[
     "Negative feedback moves the initiating variable further from the target set point",
     "Positive feedback amplifies responses and processes in organisms",
     "Negative feedback processes operate at the molecular, cellular, and organismal levels",
     "Feedback mechanisms respond to internal as well as external changes",
     "In positive feedback the stimulus is further intensified"],
   ans=0,
   why="EK 4.4.A.1.i has negative feedback RETURN the system to its target set point; moving further away is what EK 4.4.A.1.ii assigns to positive feedback. The other four restate EK 4.4.A.1.ii, EK 4.4.A.1.i and EK 4.4.A.1."),

 dict(q="Taken together, how does the framework distinguish the two kinds of feedback?",
   choices=[
     "One reduces the initial stimulus and returns the system to its set point; the other intensifies the stimulus and moves the variable further away",
     "One occurs in animals and the other occurs in plants",
     "One acts quickly and the other acts slowly",
     "One involves a set point and the other involves no stimulus",
     "One occurs at the molecular level only and the other at the organismal level only"],
   ans=0,
   why="EK 4.4.A.1.i gives reduction of the initial stimulus and return to the target set point, and EK 4.4.A.1.ii gives amplification through a further intensified stimulus with the variable moved further from the initial set point."),
]
