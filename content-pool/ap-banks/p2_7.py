# AP PSYCHOLOGY 2.7 Forgetting and Other Memory Challenges — 30 questions
# CED effective Fall 2024/2025, Unit 2 Cognition. Learning objective 2.7.A.
#
# Essential knowledge relied on: 2.7.A.1 the forgetting curve -- forgetting occurs
# rapidly after initial learning and then levels off over time; 2.7.A.2 memories
# difficult to retrieve because of encoding failure, interference (proactive or
# retroactive), or inadequate retrieval, with the tip-of-the-tongue phenomenon as
# the framework's example; 2.7.A.3 repression, the psychodynamic account of
# forgetting to defend the ego from distress; 2.7.A.4 the accuracy of memories
# affected by the misinformation effect, source amnesia, and constructive memory
# via memory consolidation and imagination inflation.
#
# Two things this module is careful about.
#
# PROACTIVE versus RETROACTIVE interference is the single most reversible pair in
# Unit 2. Every scenario item states which material was learned FIRST and which
# SECOND and which one is now hard to retrieve, so exactly one direction fits;
# items 12 and 13 are the two directions side by side and item 14 asks for the
# distinction outright with the reversed version as its first distractor.
#
# REPRESSION is attributed, not asserted. EK 2.7.A.3 says that PSYCHODYNAMIC
# THEORISTS BELIEVE memories can be forgotten to defend the ego from distress.
# The key in item 17 keeps that attribution rather than presenting repression as
# an established mechanism, because the framework does not.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
# Every key's grounding claim is stated item by item in verify_p2_7.py.
TOPIC = ("2.7", "Forgetting and Other Memory Challenges", 2)
QUESTIONS = [
 dict(q="The forgetting curve shows that", choices=[
   "forgetting occurs rapidly after initial learning and then levels off over time",
   "forgetting occurs slowly at first and then accelerates sharply",
   "forgetting proceeds at a constant rate for as long as it is measured",
   "material once learned is never forgotten"], ans=0,
   why="EK 2.7.A.1 states that forgetting occurs rapidly after initial learning and levels off over time, which is what makes time a significant factor in forgetting."),
 dict(q="According to the forgetting curve, the greatest amount of forgetting occurs", choices=[
   "in the period shortly after learning",
   "several months after learning",
   "only after the material is relearned",
   "at an unpredictable point that varies randomly"], ans=0,
   why="EK 2.7.A.1's curve is steepest early: forgetting is rapid after initial learning before it levels off, so the earliest interval carries the largest loss."),
 dict(q="A student learns a list of terms and is tested on it a week later. According to the forgetting curve, most of what she will lose was already lost", choices=[
   "within the first hours and days after learning",
   "in the final hour before the test",
   "at a steady rate spread evenly across the week",
   "only if she never reviewed the material at all"], ans=0,
   why="EK 2.7.A.1 makes forgetting rapid immediately after learning and then level; a steady even rate is the shape the curve specifically contradicts."),
 dict(q="Encoding failure as a cause of forgetting means that", choices=[
   "the information never entered memory in a durable form in the first place",
   "the information was stored but the retrieval cue is missing",
   "newer learning has displaced older learning",
   "the information is being withheld to protect the person from distress"], ans=0,
   why="EK 2.7.A.2 lists encoding failure as one reason memories are difficult to retrieve; the failure is at the point of getting information in, which is Topic 2.4's process, rather than at storage or retrieval."),
 dict(q="A person cannot describe which way the head faces on a coin she has handled thousands of times. This is best explained by", choices=[
   "encoding failure",
   "retroactive interference",
   "the misinformation effect",
   "repression"], ans=0,
   why="EK 2.7.A.2's encoding failure covers information that was never encoded in a form that could be retrieved; frequent exposure without attention to a detail does not encode that detail."),
 dict(q="Proactive interference occurs when", choices=[
   "previously learned information makes it harder to retrieve newly learned information",
   "newly learned information makes it harder to retrieve previously learned information",
   "information is lost because it was never attended to",
   "a memory is altered by information supplied after the event"], ans=0,
   why="EK 2.7.A.2 names proactive and retroactive interference as two directions of the same problem; proactive runs forward from the older material onto the newer."),
 dict(q="Retroactive interference occurs when", choices=[
   "newly learned information makes it harder to retrieve previously learned information",
   "previously learned information makes it harder to retrieve newly learned information",
   "a cue that was present at encoding is absent at retrieval",
   "a person forgets material to defend against distress"], ans=0,
   why="EK 2.7.A.2 names retroactive interference as the backward-acting direction: the newer material interferes with retrieval of the older."),
 dict(q="A woman who has used the same computer password for years keeps typing it after her employer requires a new one. The new password is hard to recall. This is", choices=[
   "proactive interference",
   "retroactive interference",
   "encoding failure",
   "source amnesia"], ans=0,
   why="The OLD password was learned first and is disrupting retrieval of the NEW one, which is EK 2.7.A.2's proactive direction."),
 dict(q="After learning a new phone number, a man finds he can no longer recall the number he used for the previous ten years. This is", choices=[
   "retroactive interference",
   "proactive interference",
   "the tip-of-the-tongue phenomenon",
   "imagination inflation"], ans=0,
   why="The NEW number was learned second and is disrupting retrieval of the OLDER one, which is EK 2.7.A.2's retroactive direction."),
 dict(q="A student who studied Spanish for three years now struggles to recall Italian vocabulary because the Spanish words keep coming to mind. This is", choices=[
   "proactive interference",
   "retroactive interference",
   "constructive memory",
   "encoding failure"], ans=0,
   why="Spanish was learned first and is interfering with the later-learned Italian, which is the proactive direction in EK 2.7.A.2."),
 dict(q="Which statement correctly distinguishes proactive from retroactive interference?", choices=[
   "proactive interference is older material disrupting newer; retroactive interference is newer material disrupting older",
   "retroactive interference is older material disrupting newer; proactive interference is newer material disrupting older",
   "proactive interference affects recall and retroactive interference affects recognition",
   "both describe the same process, differing only in how long ago the learning occurred"], ans=0,
   why="EK 2.7.A.2 names the two as the directions of interference; the first distractor is that distinction reversed, and the last denies that there is a directional difference at all."),
 dict(q="Inadequate retrieval as a cause of forgetting means that", choices=[
   "the information is in memory but cannot be brought out at the moment it is needed",
   "the information was never encoded",
   "the information has been permanently erased from storage",
   "the information has been altered by a misleading question"], ans=0,
   why="EK 2.7.A.2 lists inadequate retrieval as a third reason memories are difficult to retrieve, distinct from encoding failure and from interference, and gives the tip-of-the-tongue phenomenon as its example."),
 dict(q="A man is certain he knows an actor's name, feels it is about to come to him, and can even say what letter it starts with, but cannot produce it. This is", choices=[
   "the tip-of-the-tongue phenomenon",
   "encoding failure",
   "source amnesia",
   "repression"], ans=0,
   why="EK 2.7.A.2 gives the tip-of-the-tongue phenomenon as its example of inadequate retrieval; partial access to a memory shows it was encoded and stored but cannot be fully retrieved."),
 dict(q="Which cause of forgetting is best distinguished from the tip-of-the-tongue phenomenon by the fact that the information was never in memory to begin with?", choices=[
   "encoding failure",
   "retroactive interference",
   "proactive interference",
   "the forgetting curve"], ans=0,
   why="EK 2.7.A.2 separates encoding failure from inadequate retrieval by where the process broke down; in the tip-of-the-tongue case the memory demonstrably exists, while in encoding failure it never formed."),
 dict(q="Repression is described in the AP Psychology framework as", choices=[
   "a process psychodynamic theorists believe defends the ego from distress by keeping memories out of awareness",
   "an established biological mechanism that erases traumatic memories from storage",
   "the tendency to recall the beginning and end of a list better than the middle",
   "the alteration of a memory by information encountered after the event"], ans=0,
   why="EK 2.7.A.3 states that PSYCHODYNAMIC THEORISTS BELIEVE information or memories can be forgotten to defend the ego from distress; the framework attributes the account to a perspective rather than asserting it as established."),
 dict(q="Why does the AP Psychology framework present repression differently from interference?", choices=[
   "repression is attributed to what psychodynamic theorists believe, while interference is presented as a documented cause of retrieval difficulty",
   "repression applies only to childhood memories, while interference applies only to adult memories",
   "repression concerns recognition, while interference concerns recall",
   "repression is a stage of the forgetting curve"], ans=0,
   why="EK 2.7.A.3 opens with 'Psychodynamic theorists believe', whereas EK 2.7.A.2 states interference flatly among the reasons memories are difficult to retrieve; the difference in wording is the framework's own."),
 dict(q="The misinformation effect refers to", choices=[
   "the alteration of a memory by information encountered after the event",
   "the failure to notice a change in a visual scene",
   "the belief that an outcome is due because it has not happened recently",
   "the loss of memories formed before an injury"], ans=0,
   why="EK 2.7.A.4 names the misinformation effect among the influences on the ACCURACY of memories; the distractors are change blindness (2.1.A.5.ii), the gambler's fallacy (2.2.A.6), and retrograde amnesia (2.5.A.4)."),
 dict(q="Witnesses asked how fast two cars were going when they \"smashed into\" each other later report more broken glass than witnesses asked how fast the cars were going when they \"hit\" each other. This illustrates", choices=[
   "the misinformation effect",
   "source amnesia",
   "proactive interference",
   "the forgetting curve"], ans=0,
   why="EK 2.7.A.4's misinformation effect covers memory accuracy altered by information supplied after the event, and the wording of the question is exactly such post-event information."),
 dict(q="Source amnesia refers to", choices=[
   "remembering information while misremembering where it came from",
   "forgetting all information acquired before a particular date",
   "being unable to form any new memories",
   "an inability to remember one's own early childhood"], ans=0,
   why="EK 2.7.A.4 names source amnesia among the influences on memory accuracy; the content survives while its origin is lost or misattributed, which is what separates it from the amnesias in EK 2.5.A.4."),
 dict(q="A man is confident that he read a particular fact in a scientific journal, but he actually saw it in an advertisement. This is best described as", choices=[
   "source amnesia",
   "the misinformation effect",
   "encoding failure",
   "retroactive interference"], ans=0,
   why="EK 2.7.A.4's source amnesia is the loss or misattribution of where information came from; the content itself is retained accurately, which rules out the misinformation effect."),
 dict(q="Constructive memory, in the AP Psychology framework, refers to the idea that", choices=[
   "memories are assembled rather than replayed, so they can change in the process",
   "memories are stored as exact recordings that never change",
   "memories can only be retrieved with an external cue",
   "memories are lost at a constant rate over time"], ans=0,
   why="EK 2.7.A.4 lists constructive memory among the influences on memory accuracy, operating via memory consolidation and imagination inflation, which presupposes that a memory is built rather than played back unchanged."),
 dict(q="Imagination inflation refers to the finding that", choices=[
   "vividly imagining an event can increase confidence that it actually happened",
   "memories become more accurate the more often they are retrieved",
   "confidence in a memory is unrelated to its accuracy",
   "imagining an event makes it harder to encode"], ans=0,
   why="EK 2.7.A.4 names imagination inflation as one route by which constructive memory affects accuracy: imagining an event raises confidence that it occurred."),
 dict(q="Which of the following is named in the AP Psychology framework as an influence on the ACCURACY of memories rather than as a cause of forgetting?", choices=[
   "source amnesia",
   "encoding failure",
   "proactive interference",
   "inadequate retrieval"], ans=0,
   why="EK 2.7.A.4 groups the misinformation effect, source amnesia, and constructive memory as influences on accuracy, while EK 2.7.A.2 lists encoding failure, interference, and inadequate retrieval as reasons memories are difficult to retrieve."),
 dict(q="Which statement correctly distinguishes the misinformation effect from source amnesia?", choices=[
   "the misinformation effect changes the content of a memory; source amnesia leaves the content but loses its origin",
   "source amnesia changes the content of a memory; the misinformation effect leaves the content but loses its origin",
   "the misinformation effect applies only to eyewitnesses and source amnesia only to students",
   "both concern where a memory came from, differing only in how long ago it formed"], ans=0,
   why="EK 2.7.A.4 lists both among the influences on accuracy, but one alters what is remembered and the other where it is believed to have come from; the first distractor reverses that."),
 dict(q="A researcher shows all participants the same video, then asks half of them a question containing a misleading detail and the other half a neutral question, and later tests both groups' memory of the video. The independent variable is", choices=[
   "whether the question contained the misleading detail",
   "how many details participants remember at the later test",
   "the content of the video, which was identical for everyone",
   "the amount of time between the video and the test, which was the same for both groups"], ans=0,
   why="Science practice 2.B: the independent variable is the manipulated condition, which here is the presence of the misleading detail; the memory measure is the dependent variable and the video and delay were held constant."),
 dict(q="In that study, showing both groups the same video matters because", choices=[
   "otherwise a difference in what was witnessed, rather than the misleading question, could explain the results",
   "otherwise the study would have no dependent variable",
   "it makes the sample representative of all eyewitnesses",
   "it turns the experiment into a naturalistic observation"], ans=0,
   why="A variable differing alongside the manipulation and offering a rival explanation is a confounding variable; equating the witnessed event removes it as an account of any later difference."),
 dict(q="Which is the best operational definition of memory accuracy for that study?", choices=[
   "the number of details a participant reports that match the video, out of a fixed set of test questions",
   "how vividly the participant remembers the video",
   "the participant's overall confidence in her memory",
   "whether the participant believes her memory is reliable"], ans=0,
   why="An operational definition states the countable measurement procedure; matching reported details against a fixed set of questions is measurable, and confidence is a different construct that EK 2.7.A.4's imagination inflation shows can rise without accuracy rising."),
 dict(q="A student claims: \"An eyewitness who is highly confident must be accurate.\" Which framework content most directly refutes this claim?", choices=[
   "imagination inflation shows that confidence in an event can rise without the event having occurred",
   "the forgetting curve shows that forgetting is rapid at first",
   "proactive interference shows that older learning disrupts newer learning",
   "recognition relies on retrieval cues while recall does not"], ans=0,
   why="Science practice 4.B requires reasoning grounded in psychology-derived evidence; EK 2.7.A.4's imagination inflation directly separates confidence from accuracy, which is what the claim assumes are linked."),
 dict(q="A defense attorney argues that a witness's testimony should be treated cautiously because police questioned her repeatedly using leading questions. The strongest framework-based support for that argument is", choices=[
   "the misinformation effect, by which post-event information can alter a memory",
   "the tip-of-the-tongue phenomenon, by which a known word cannot be produced",
   "encoding failure, by which information never enters memory",
   "the psychodynamic account of repression"], ans=0,
   why="EK 2.7.A.4's misinformation effect is specifically about post-event information altering memory accuracy, and leading questions asked after the event are that information."),
 dict(q="A teacher tells students that once material is learned it stays learned, so review is unnecessary. Which framework finding most directly contradicts this?", choices=[
   "the forgetting curve, which shows rapid loss soon after initial learning",
   "source amnesia, which concerns where information came from",
   "the misinformation effect, which concerns post-event information",
   "encoding failure, which concerns information never encoded"], ans=0,
   why="EK 2.7.A.1 makes time a significant factor in forgetting, with rapid loss after initial learning; the other three findings concern accuracy or encoding rather than the passage of time after successful learning."),
]
