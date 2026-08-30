# AP PSYCHOLOGY 2.4 Encoding Memories — 30 questions
# CED effective Fall 2024/2025, Unit 2 Cognition. Learning objective 2.4.A.
#
# Essential knowledge relied on: 2.4.A.1 encoding as the processes and strategies
# that get information into memory, and the claim that HOW information is encoded
# determines how effectively it is stored and retrieved; 2.4.A.2 mnemonic
# devices, with method of loci as the framework's example; 2.4.A.3 chunking,
# categories, and hierarchies; 2.4.A.4 the spacing effect, massed practice versus
# distributed practice; 2.4.A.5 the serial position effect, with the primacy
# effect for the beginning of a list and the recency effect for the end.
#
# The CED's suggested skills for THIS topic include 3.B -- calculate and interpret
# measures of central tendency, variation, and percentile rank -- so six items
# work with a small data set stated in the stem as prose. There are no figures
# anywhere in this bank, so no item refers to a graph or a printed table.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
# Every key's grounding claim is stated item by item in verify_p2_4.py.
TOPIC = ("2.4", "Encoding Memories", 2)
QUESTIONS = [
 dict(q="Encoding is best defined as", choices=[
   "the processes and strategies that get information into memory",
   "the maintenance of information in memory over time",
   "the process of bringing stored information back into awareness",
   "the loss of information that was once available"], ans=0,
   why="EK 2.4.A.1 defines encoding as processes and strategies to get information into memory; the other options name storage, retrieval, and forgetting, which are Topics 2.5, 2.6, and 2.7."),
 dict(q="According to the AP Psychology framework, how information is encoded matters because it", choices=[
   "determines how effectively the information is later stored and retrieved",
   "has no bearing on later recall once the information is in memory",
   "affects only the speed of learning, not the accuracy of recall",
   "matters for explicit memory but not for implicit memory"], ans=0,
   why="EK 2.4.A.1 states that how information is encoded can determine how effectively information is stored and retrieved, which is why encoding gets a topic of its own."),
 dict(q="A mnemonic device is best described as", choices=[
   "a process that aids in encoding information into working and long-term memory",
   "a biological process that strengthens connections between neurons",
   "a failure of memory caused by interference from similar material",
   "a shortcut used to make a quick judgment about probability"], ans=0,
   why="EK 2.4.A.2 defines mnemonic devices as processes that aid in encoding information into working and long-term memory."),
 dict(q="The method of loci works by", choices=[
   "associating each item to be remembered with a location along a familiar route",
   "grouping items into meaningful clusters so that fewer units must be held",
   "spreading study sessions out over several days rather than one",
   "rehearsing a list until the first items are learned best"], ans=0,
   why="EK 2.4.A.2 gives method of loci as its example of a mnemonic device; it encodes items by attaching them to remembered places, which is what distinguishes it from chunking and from the spacing effect."),
 dict(q="Chunking improves encoding by", choices=[
   "grouping information into meaningful units so that fewer separate items must be held",
   "repeating each item aloud a fixed number of times",
   "attaching each item to a physical location",
   "delaying study until just before it is needed"], ans=0,
   why="EK 2.4.A.3 states that encoding can be improved by grouping information together into meaningful chunks, categories, or hierarchies."),
 dict(q="Remembering the digit string 1 4 9 2 1 7 7 6 as two familiar dates rather than as eight separate digits is an example of", choices=[
   "chunking",
   "the spacing effect",
   "the recency effect",
   "long-term potentiation"], ans=0,
   why="EK 2.4.A.3's chunking is the grouping of information into meaningful units, which is exactly what recoding eight digits as two dates does."),
 dict(q="A student studying biology organizes her notes so that broad categories contain narrower subcategories, which in turn contain examples. According to the AP Psychology framework, this aids encoding through", choices=[
   "the use of hierarchies",
   "the spacing effect",
   "the primacy effect",
   "the method of loci"], ans=0,
   why="EK 2.4.A.3 names categories and hierarchies alongside chunks as ways of grouping information that improve encoding."),
 dict(q="The spacing effect concerns differences in encoding and memory consolidation that depend on", choices=[
   "whether information is studied all at once or distributed over time",
   "whether information appears at the beginning or the end of a list",
   "whether information is processed for meaning or for appearance",
   "whether the learner is tested immediately or after a delay"], ans=0,
   why="EK 2.4.A.4 defines the spacing effect as the difference in encoding and memory consolidation between information encoded all at once (massed practice) and distributed over time (distributed practice)."),
 dict(q="Studying the entire unit in one long session the night before an exam is an example of", choices=[
   "massed practice",
   "distributed practice",
   "chunking",
   "the method of loci"], ans=0,
   why="EK 2.4.A.4 names massed practice as encoding information all at once, which a single long session is."),
 dict(q="Studying the same material for thirty minutes on each of six days is an example of", choices=[
   "distributed practice",
   "massed practice",
   "the serial position effect",
   "a mnemonic device"], ans=0,
   why="EK 2.4.A.4 names distributed practice as encoding distributed over time, which six separate sessions are."),
 dict(q="A student wants the strongest long-term retention of a chapter she has two weeks to learn. The spacing effect predicts that she should", choices=[
   "study in several shorter sessions spread across the two weeks",
   "study in one long session on the final night",
   "study only the first and last pages of the chapter",
   "reread the chapter continuously without pausing"], ans=0,
   why="EK 2.4.A.4 makes the spacing effect a difference in encoding and consolidation between massed and distributed practice, and distributed practice is the condition the effect favors."),
 dict(q="The serial position effect states that memory is affected by", choices=[
   "the order in which the information was presented",
   "the meaning the learner assigned to the information",
   "the number of hours since the information was learned",
   "how many people were present during learning"], ans=0,
   why="EK 2.4.A.5 states that encoding processes can be affected by the order in which information is presented, which is called the serial position effect."),
 dict(q="The tendency to remember items presented at the BEGINNING of a list especially well is called", choices=[
   "the primacy effect",
   "the recency effect",
   "the spacing effect",
   "chunking"], ans=0,
   why="EK 2.4.A.5 names the primacy effect for information presented at the beginning of a list."),
 dict(q="The tendency to remember items presented at the END of a list especially well is called", choices=[
   "the recency effect",
   "the primacy effect",
   "the method of loci",
   "massed practice"], ans=0,
   why="EK 2.4.A.5 names the recency effect for information presented at the end of a list."),
 dict(q="According to the serial position effect, which items in a long list are recalled LEAST well?", choices=[
   "those in the middle of the list",
   "those at the very beginning",
   "those at the very end",
   "those that were repeated most often"], ans=0,
   why="EK 2.4.A.5 predicts that information at the beginning or the end of a list will be more memorable than information presented in the middle, so the middle is the disadvantaged position."),
 dict(q="Introduced to twelve people in a row, a woman later recalls the first two names and the last two names but almost none in between. This pattern illustrates", choices=[
   "the serial position effect",
   "the spacing effect",
   "functional fixedness",
   "echoic memory"], ans=0,
   why="EK 2.4.A.5's serial position effect predicts an advantage for both ends of a sequence over the middle, which is the pattern the scenario describes."),
 dict(q="A shopper recalls the last three items on a grocery list she read just before leaving the house. This is most specifically an example of", choices=[
   "the recency effect",
   "the primacy effect",
   "chunking",
   "a hierarchy"], ans=0,
   why="EK 2.4.A.5 attaches the recency effect to items at the end of a list; the items recalled are the final ones, which distinguishes this from primacy."),
 dict(q="Which statement correctly distinguishes chunking from a mnemonic device such as the method of loci?", choices=[
   "chunking regroups the material itself into meaningful units; the method of loci attaches the material to an external framework of places",
   "the method of loci regroups the material into meaningful units; chunking attaches the material to an external framework of places",
   "chunking works only for numbers and the method of loci only for words",
   "both are ways of spacing practice over time"], ans=0,
   why="EK 2.4.A.3 makes chunking a regrouping of the information itself while EK 2.4.A.2 makes the method of loci a mnemonic that attaches items to remembered locations; the first distractor is that contrast reversed."),
 dict(q="A researcher randomly assigns students either to study a word list in one 60-minute session or in four 15-minute sessions across four days, then tests recall a week later. The independent variable is", choices=[
   "whether study time was massed in one session or distributed across four",
   "the number of words the students recall a week later",
   "the total of 60 minutes of study time, which was the same for both groups",
   "the one-week delay before testing, which was the same for both groups"], ans=0,
   why="Science practice 2.B: the independent variable is the manipulated, randomly assigned condition, which here is the massed versus distributed schedule; total study time and delay were deliberately held constant."),
 dict(q="In the study described above, holding total study time at 60 minutes for both groups is important because", choices=[
   "otherwise the amount of study, rather than its spacing, could explain any difference",
   "otherwise the study would have no dependent variable",
   "it guarantees that the sample represents all students",
   "it converts the experiment into a correlational study"], ans=0,
   why="A variable that changes along with the manipulation and offers a rival explanation is a confounding variable; equating total study time removes amount of practice as an alternative account of the result."),
 dict(q="Which is the best operational definition of the dependent variable in a study of encoding strategies?", choices=[
   "the number of words from the studied list correctly written down in five minutes",
   "how well the participant seems to have learned the list",
   "the strength of the participant's memory",
   "whether the participant felt confident about the list"], ans=0,
   why="An operational definition states the specific countable measurement procedure; a count of correctly recalled words is measurable, while the other options restate the construct without specifying how it is measured."),
 dict(q="Six students recall the following numbers of words from a studied list: 4, 6, 7, 9, 10, 12. The mean number recalled is", choices=[
   "6",
   "7",
   "8",
   "9"], ans=2,
   why="The six scores total 48, and 48 divided by 6 is 8; the mean is the sum of the scores divided by how many there are."),
 dict(q="In a different class, six students recall 2, 5, 6, 8, 9, and 20 words. The median number recalled is", choices=[
   "6",
   "7",
   "8",
   "10"], ans=1,
   why="With an even number of scores the median is the mean of the two middle values; the middle pair is 6 and 8, whose mean is 7. The mean of this set is 10, higher than the median, because the score of 20 pulls it upward."),
 dict(q="Seven students recall 5, 5, 6, 8, 8, 8, and 11 words. The mode is", choices=[
   "5",
   "6",
   "7.3",
   "8"], ans=3,
   why="The mode is the most frequently occurring score; 8 appears three times, more often than any other value."),
 dict(q="Five students recall 3, 7, 9, 12, and 15 words. The range of these scores is", choices=[
   "3",
   "9",
   "12",
   "15"], ans=2,
   why="The range is the highest score minus the lowest, which is 15 minus 3."),
 dict(q="Two classes have the same mean recall score, but Class A's scores have a much larger standard deviation than Class B's. This means that", choices=[
   "Class A's scores are more spread out around the mean than Class B's",
   "Class A's average recall was higher than Class B's",
   "Class A had more students than Class B",
   "Class A's scores are more tightly clustered than Class B's"], ans=0,
   why="Standard deviation is a measure of variation, not of central tendency; a larger value means greater spread around the mean, and the means here are stated to be equal."),
 dict(q="A student's recall score is at the 80th percentile of her class. This means that", choices=[
   "she scored higher than about 80 percent of her classmates",
   "she recalled 80 percent of the words on the list",
   "she scored 80 points on the recall test",
   "about 80 percent of her classmates scored higher than she did"], ans=0,
   why="Percentile rank expresses the percentage of scores in the distribution that fall below a given score; it is a position within a group, not a percentage of items correct."),
 dict(q="Which of these findings would most directly SUPPORT the claim that distributed practice improves encoding?", choices=[
   "students randomly assigned to spaced study recall more a week later than those assigned to massed study",
   "students who choose to study in spaced sessions report enjoying studying more",
   "students who recall more words also tend to spend more total hours studying",
   "students recall the first and last words on a list better than the middle words"], ans=0,
   why="Only the first option manipulates the schedule and randomly assigns it, so only it can support a causal claim; the third is correlational and the fourth is the serial position effect, a different phenomenon."),
 dict(q="A survey finds that students who report using mnemonic devices also report higher grades. Before concluding that mnemonics raise grades, a careful reader should note that", choices=[
   "students who are already conscientious may both use mnemonics and earn higher grades",
   "mnemonic devices have never been shown to aid encoding",
   "grades cannot be quantified in any way",
   "the survey included random assignment to conditions"], ans=0,
   why="A survey manipulates nothing, so a third variable such as conscientiousness is a live rival explanation; EK 2.4.A.2 does say mnemonics aid encoding, which is what makes the causal reading tempting rather than absurd."),
 dict(q="A tutor tells a student that the best way to learn a long list of unrelated terms is to reread it repeatedly the night before the test. Which combination of framework findings best contradicts this advice?", choices=[
   "the spacing effect favors distributed practice, and grouping the terms into meaningful chunks would improve encoding",
   "the recency effect favors the end of a list, and the primacy effect favors the beginning",
   "long-term potentiation strengthens synaptic connections with frequent activation",
   "iconic and echoic memory hold sensory information briefly"], ans=0,
   why="The advice fails on two counts covered by this topic: EK 2.4.A.4's spacing effect favors distributing study rather than massing it the night before, and EK 2.4.A.3's chunking would improve encoding of an unstructured list that rereading leaves unstructured."),
]
