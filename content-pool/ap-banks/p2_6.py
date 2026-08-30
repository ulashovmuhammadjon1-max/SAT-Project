# AP PSYCHOLOGY 2.6 Retrieving Memories — 30 questions
# CED effective Fall 2024/2025, Unit 2 Cognition. Learning objective 2.6.A.
#
# Essential knowledge relied on: 2.6.A.1 retrieval occurs through recall
# (remembering WITHOUT cues) or recognition (which RELIES ON retrieval cues);
# 2.6.A.2 retrieval is enhanced when a person is in the same environmental space
# (context-dependent memory), mood (mood-congruent memory), or physical state
# (state-dependent memory) as at encoding; 2.6.A.3 successful retrieval is more
# likely with retrieval practice processes, including the testing effect and
# metacognition.
#
# This EK is short, so breadth comes from application rather than from more
# definitions: each of the three matching effects gets a definition item, a
# scenario item, and a discrimination item against its nearest neighbour, and the
# CED's suggested skills for this topic (3.A and 3.C, identifying and
# interpreting data) are met by items that state a small result in prose and ask
# what it does and does not license. There are no figures in this bank, so no
# item refers to a graph.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
# Every key's grounding claim is stated item by item in verify_p2_6.py.
TOPIC = ("2.6", "Retrieving Memories", 2)
QUESTIONS = [
 dict(q="In the AP Psychology framework, memory retrieval is the process of", choices=[
   "getting information out of memory",
   "getting information into memory",
   "holding information in memory over time",
   "losing information that was once available"], ans=0,
   why="Learning objective 2.6.A is stated as explaining how memory retrieval processes get information out of memory; the other options name encoding, storage, and forgetting."),
 dict(q="Recall, as a form of retrieval, is best described as", choices=[
   "remembering without cues",
   "identifying the correct item from among several presented options",
   "learning material for the first time",
   "holding material briefly after the stimulus ends"], ans=0,
   why="EK 2.6.A.1 defines recall as remembering without cues, in contrast to recognition, which relies on retrieval cues."),
 dict(q="Recognition, as a form of retrieval, is best described as", choices=[
   "remembering that relies on retrieval cues",
   "remembering with no external prompt of any kind",
   "the strengthening of connections between neurons",
   "the deliberate repetition of material to keep it available"], ans=0,
   why="EK 2.6.A.1 states that recognition relies on retrieval cues, which is what separates it from recall."),
 dict(q="Which statement correctly distinguishes recall from recognition?", choices=[
   "recall proceeds without cues, while recognition relies on cues",
   "recognition proceeds without cues, while recall relies on cues",
   "recall applies to images and recognition to words",
   "the two terms describe the same process at different speeds"], ans=0,
   why="EK 2.6.A.1 separates the two solely by whether retrieval cues are supplied; the first distractor is that separation reversed."),
 dict(q="An exam question that asks a student to write out the definition of a term from memory tests", choices=[
   "recall",
   "recognition",
   "encoding",
   "sensory memory"], ans=0,
   why="EK 2.6.A.1's recall is remembering without cues, and producing a definition from a blank page supplies no options to choose among."),
 dict(q="An exam question that asks a student to choose the correct definition from four printed options tests", choices=[
   "recognition",
   "recall",
   "elaborative rehearsal",
   "the spacing effect"], ans=0,
   why="EK 2.6.A.1's recognition relies on retrieval cues, and the printed options are those cues."),
 dict(q="Context-dependent memory refers to improved retrieval when a person is in the same", choices=[
   "environmental space as when the information was encoded",
   "mood as when the information was encoded",
   "physical state as when the information was encoded",
   "social group as when the information was encoded"], ans=0,
   why="EK 2.6.A.2 attaches context-dependent memory specifically to being in the same environmental space at retrieval as at encoding."),
 dict(q="Mood-congruent memory refers to improved retrieval when a person is in the same", choices=[
   "mood as when the information was encoded",
   "environmental space as when the information was encoded",
   "physical state as when the information was encoded",
   "posture as when the information was encoded"], ans=0,
   why="EK 2.6.A.2 attaches mood-congruent memory specifically to being in the same mood at retrieval as at encoding."),
 dict(q="State-dependent memory refers to improved retrieval when a person is in the same", choices=[
   "physical state as when the information was encoded",
   "environmental space as when the information was encoded",
   "mood as when the information was encoded",
   "time of day as when the information was encoded"], ans=0,
   why="EK 2.6.A.2 attaches state-dependent memory specifically to being in the same physical state at retrieval as at encoding."),
 dict(q="A student who studied in a particular classroom recalls more of the material when tested in that same room than in an unfamiliar one. This illustrates", choices=[
   "context-dependent memory",
   "mood-congruent memory",
   "state-dependent memory",
   "the testing effect"], ans=0,
   why="EK 2.6.A.2's context-dependent memory concerns the environmental space, which is the only thing the scenario varies -- the student's mood and physical state are not mentioned."),
 dict(q="A person who is feeling sad finds that unhappy episodes from her past come to mind more readily than happy ones. This illustrates", choices=[
   "mood-congruent memory",
   "context-dependent memory",
   "state-dependent memory",
   "source amnesia"], ans=0,
   why="EK 2.6.A.2's mood-congruent memory concerns emotional state at encoding and retrieval, which is what the scenario varies; no change of room or physical condition is described."),
 dict(q="A person who learned a list while unusually tired recalls it better when tired again than when well rested. This illustrates", choices=[
   "state-dependent memory",
   "context-dependent memory",
   "mood-congruent memory",
   "the serial position effect"], ans=0,
   why="EK 2.6.A.2's state-dependent memory concerns physical state; fatigue is a physical condition rather than a location or an emotion."),
 dict(q="Which statement correctly distinguishes context-dependent memory from state-dependent memory?", choices=[
   "context-dependent memory concerns the external surroundings; state-dependent memory concerns the person's physical condition",
   "state-dependent memory concerns the external surroundings; context-dependent memory concerns the person's physical condition",
   "context-dependent memory applies to recall and state-dependent memory to recognition",
   "both concern emotion, but only one is deliberate"], ans=0,
   why="EK 2.6.A.2 separates environmental space from physical state as two distinct matching conditions; the first distractor reverses them and the last collapses both into mood, which is the third condition in the same EK."),
 dict(q="Which statement correctly distinguishes mood-congruent memory from context-dependent memory?", choices=[
   "mood-congruent memory concerns the emotional state at encoding and retrieval; context-dependent memory concerns the physical surroundings",
   "context-dependent memory concerns the emotional state at encoding and retrieval; mood-congruent memory concerns the physical surroundings",
   "mood-congruent memory occurs only in people who are sad",
   "context-dependent memory occurs only during recognition tasks"], ans=0,
   why="EK 2.6.A.2 lists mood and environmental space as separate matching conditions; the first distractor reverses them, and the remaining options add restrictions the framework does not state."),
 dict(q="The testing effect refers to the finding that", choices=[
   "retrieving material in a practice test improves later retention of it",
   "students perform worse on material they have been tested on before",
   "tests are more valid when they are longer",
   "recognition tests are easier than recall tests"], ans=0,
   why="EK 2.6.A.3 names the testing effect among retrieval practice processes that make successful retrieval more likely, so the act of retrieving during practice is what improves later retrieval."),
 dict(q="A student who has read a chapter twice wants the strongest retention. According to the AP Psychology framework, she should next", choices=[
   "close the book and try to retrieve the material without looking",
   "read the chapter a third time",
   "highlight the passages she found difficult",
   "copy her notes out again word for word"], ans=0,
   why="EK 2.6.A.3 states that successful retrieval is more likely when using retrieval practice processes, of which the testing effect is one; rereading, highlighting, and copying involve no retrieval attempt."),
 dict(q="Metacognition, as named in the AP Psychology framework's account of retrieval practice, is best described as", choices=[
   "thinking about one's own thinking, including judging what one does and does not know",
   "the biological strengthening of connections between neurons",
   "the tendency to remember the first items in a list",
   "the storage of information for a lifetime"], ans=0,
   why="EK 2.6.A.3 names metacognition alongside the testing effect as a retrieval practice process; it is the monitoring of one's own knowledge that lets a learner direct further study."),
 dict(q="A student pauses after a study session and asks herself which sections she could explain to someone else and which she could not. This is best described as", choices=[
   "metacognition",
   "maintenance rehearsal",
   "chunking",
   "recognition"], ans=0,
   why="EK 2.6.A.3 names metacognition among the retrieval practice processes; judging what one does and does not know is monitoring one's own knowledge rather than rehearsing or regrouping material."),
 dict(q="Why does rereading a chapter tend to be a weaker study strategy than self-testing?", choices=[
   "rereading involves no retrieval attempt, and retrieval practice is what improves later retrieval",
   "rereading takes more total time than self-testing",
   "rereading places material in sensory memory rather than long-term memory",
   "rereading is a form of recognition, which is not a kind of retrieval"], ans=0,
   why="EK 2.6.A.3 attributes the benefit to retrieval practice processes specifically, so a strategy that never requires retrieval does not engage the mechanism; the last distractor is false because EK 2.6.A.1 makes recognition one of the two forms of retrieval."),
 dict(q="A student can identify the correct answer on a multiple-choice quiz but cannot produce the same information on a short-answer question. The most precise description is that", choices=[
   "her recognition of the material is better than her recall of it",
   "her recall of the material is better than her recognition of it",
   "she has not encoded the material at all",
   "she is experiencing state-dependent memory"], ans=0,
   why="EK 2.6.A.1 distinguishes cued retrieval (recognition) from uncued retrieval (recall); succeeding with options present and failing without them is that difference, and it also shows the material was encoded."),
 dict(q="In a study, participants who studied a list in a quiet room recalled an average of 14 words when tested in that same room and 9 words when tested in a noisy room. This result most directly illustrates", choices=[
   "context-dependent memory",
   "the testing effect",
   "the misinformation effect",
   "maintenance rehearsal"], ans=0,
   why="EK 2.6.A.2's context-dependent memory predicts better retrieval in the encoding environment, and the only difference between the two testing conditions described is the environmental space."),
 dict(q="In the study described above, the difference between 14 and 9 words is best described as", choices=[
   "the difference in mean recall between the two testing conditions",
   "the standard deviation of the recall scores",
   "the percentile rank of the matched condition",
   "the range of scores in the noisy room"], ans=0,
   why="The two figures are stated as averages, so their difference is a difference in means; standard deviation, percentile rank, and range are different statistics that these numbers do not report."),
 dict(q="Participants who took a practice test scored an average of 78 percent on a final test, while participants who reread the material scored an average of 65 percent. Participants were randomly assigned to condition. The strongest supported conclusion is that", choices=[
   "practice testing caused better performance than rereading in this study",
   "practice testing is associated with better performance, but the cause is undetermined",
   "students who prefer testing are more motivated learners",
   "rereading has no effect on memory at all"], ans=0,
   why="Random assignment to a manipulated condition licenses a causal conclusion about the manipulation; the second option understates what an experiment supports and the fourth claims a zero effect that a comparison of two conditions cannot establish."),
 dict(q="A different study finds that students who report testing themselves more often also have higher grade point averages. Before concluding that self-testing raises grades, a careful reader should note that", choices=[
   "students were not assigned their study habits, so a third variable could explain both",
   "grade point average cannot be quantified",
   "self-testing has never been shown to aid retrieval",
   "the study randomly assigned students to testing conditions"], ans=0,
   why="Study habits were reported rather than assigned, so the design is correlational; EK 2.6.A.3 does support the benefit of retrieval practice, which is what makes the causal reading tempting rather than absurd."),
 dict(q="In an experiment testing whether matching the study and test environment aids retrieval, the independent variable is", choices=[
   "whether participants are tested in the same room in which they studied",
   "the number of words participants recall at test",
   "the length of the word list, which is the same for everyone",
   "the participants' ages"], ans=0,
   why="Science practice 2.B: the independent variable is the manipulated, randomly assigned condition, which here is the match or mismatch of environments; the recall count is the dependent variable."),
 dict(q="In that experiment, using the same word list for both groups matters because", choices=[
   "otherwise the difficulty of the lists, rather than the environment, could explain the difference",
   "otherwise the study would have no independent variable",
   "it makes the sample representative of the population",
   "it converts the experiment into a case study"], ans=0,
   why="A variable that differs alongside the manipulation and offers a rival explanation is a confounding variable; equating list difficulty removes it as an account of any difference in recall."),
 dict(q="Which is the best operational definition of \"retrieval success\" for such a study?", choices=[
   "the number of studied words a participant writes down correctly within three minutes",
   "how much of the list the participant seems to remember",
   "the participant's overall memory ability",
   "whether the participant felt the test went well"], ans=0,
   why="An operational definition states the countable measurement procedure; a word count within a fixed interval is measurable, while the alternatives restate the construct or measure confidence instead of performance."),
 dict(q="A study of context-dependent memory recruits only students at one university and concludes that the effect holds for adults in general. The strongest objection is that", choices=[
   "the sample may not represent the wider population, so the finding may not generalize",
   "context-dependent memory has never been observed in any study",
   "the study cannot have had a dependent variable",
   "recruiting from one place makes the study correlational"], ans=0,
   why="Generalizability turns on whether the sample resembles the population the claim is about; recruiting from one university does not change the design's classification, which is why the last option is wrong as well as unattractive."),
 dict(q="A student proposes the claim: \"Studying in the room where the exam will be held improves exam performance.\" Which piece of framework-based reasoning best supports it?", choices=[
   "EK 2.6.A.2's context-dependent memory holds that retrieval improves when the environmental space matches the one in which encoding occurred",
   "EK 2.6.A.1 distinguishes recall from recognition",
   "EK 2.5.A.4 lists conditions that impair memory storage",
   "EK 2.4.A.5's serial position effect favors the ends of a list"],  ans=0,
   why="Science practice 4.A and 4.B require reasoning grounded in psychology-derived evidence; only context-dependent memory bears on whether matching the study and test environment should help."),
 dict(q="A tutor advises a student to reread her notes in a different room each night so the material will not be \"tied to one place.\" Which framework finding most directly complicates that advice?", choices=[
   "context-dependent memory predicts an advantage when the retrieval environment matches the encoding environment",
   "the testing effect predicts that retrieval practice improves retention",
   "metacognition improves a learner's judgment of what she knows",
   "recognition relies on retrieval cues while recall does not"], ans=0,
   why="EK 2.6.A.2 predicts a benefit from matching environments, so varying the study room removes a cue that could aid retrieval in the exam room; the other findings are true but do not bear on where studying takes place."),
]
