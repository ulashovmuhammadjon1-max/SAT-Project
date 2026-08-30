# AP PSYCHOLOGY 1.5 Sleep — 25 questions
# CED effective Fall 2024/2025, Unit 1 Biological Bases of Behavior.
# Learning objective 1.5.A. Essential knowledge: 1.5.A.1 consciousness has
# varying levels of awareness, and sleep and wakefulness are two types of
# consciousness; 1.5.A.2 the sleep/wake cycle is a circadian rhythm of about
# 24 hours, disrupted by jet lag and shift work; 1.5.A.3 sleep stages are
# identified by their EEG patterns; 1.5.A.3.i NREM Stages 1-3, decreasing in
# duration through the cycle, with hypnagogic sensations on entering initial
# Stage 1; 1.5.A.3.ii REM as paradoxical sleep -- waves like wakefulness with the
# body at its most relaxed -- where dreaming typically occurs, increasing in
# frequency as the cycle progresses, with REM rebound after deprivation;
# 1.5.A.4 activation-synthesis and consolidation theories of dreams; 1.5.A.5
# memory consolidation and restoration as theories of why sleep occurs; 1.5.A.6
# the five sleep disorders in scope -- insomnia, narcolepsy, REM sleep behavior
# disorder, sleep apnea, somnambulism.
#
# Exclusion statements respected: the psychoanalytic theory of dreams is out of
# scope and is never a key; no sleep disorder outside EK 1.5.A.6's closed list
# appears anywhere in the module.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
# Every key's grounding claim is stated item by item in verify_p1_5.py.
TOPIC = ("1.5", "Sleep", 1)
QUESTIONS = [
 dict(q="In the AP Psychology framework, consciousness is best described as", choices=[
   "varying levels of awareness of one's internal and external worlds",
   "the single state a person is in whenever the eyes are open",
   "the total quantity of information stored in long-term memory",
   "the portion of experience that can never be reported"], ans=0,
   why="EK 1.5.A.1 defines consciousness as having varying levels of awareness of thoughts, feelings, behavior, and events in a person's internal and external worlds."),
 dict(q="Sleep and wakefulness are best understood as", choices=[
   "two types of consciousness",
   "the presence and the complete absence of consciousness",
   "two circadian rhythms operating independently",
   "the same state distinguished only by posture"], ans=0,
   why="EK 1.5.A.1 states that sleep and wakefulness are two types of consciousness, so sleep is not the absence of consciousness."),
 dict(q="The sleep/wake cycle is an example of a circadian rhythm, which in humans is", choices=[
   "a cycle of roughly 24 hours",
   "a cycle of roughly 90 minutes",
   "a cycle that repeats once each week",
   "a cycle that varies randomly from day to day"], ans=0,
   why="EK 1.5.A.2 states that the sleep/wake cycle is a circadian rhythm, which in humans is about a 24-hour cycle."),
 dict(q="A nurse who has just moved from day shifts to overnight shifts sleeps poorly and feels alert at the wrong times. This is best described as", choices=[
   "a disruption of the circadian rhythm",
   "REM rebound",
   "narcolepsy",
   "a hypnagogic sensation"], ans=0,
   why="EK 1.5.A.2 names shift work, along with jet lag, as a disruption of the circadian rhythm."),
 dict(q="A traveler flies from New York to Tokyo and for several days feels sleepy in the afternoon and wide awake at 3 a.m. The most precise explanation is that", choices=[
   "her circadian rhythm is still aligned to her original time zone",
   "she has developed insomnia as a disorder",
   "she is experiencing REM sleep behavior disorder",
   "her sleep stages have been permanently reordered"], ans=0,
   why="EK 1.5.A.2 gives jet lag as a disruption of the circadian rhythm; the internal roughly 24-hour cycle has not yet realigned with local time, which is a temporary mismatch rather than a disorder."),
 dict(q="The stages of sleep are identified by", choices=[
   "their specific EEG patterns",
   "the sleeper's self-report on waking",
   "the position of the sleeper's body",
   "the length of time since the sleeper went to bed"], ans=0,
   why="EK 1.5.A.3 states that the stages of sleep are identified by their specific EEG patterns, which is why Topic 1.4's list of research methods matters here."),
 dict(q="NREM sleep occurs in", choices=[
   "Stages 1 through 3",
   "Stages 1 through 5",
   "the final stage of each cycle only",
   "the period immediately after each REM episode only"], ans=0,
   why="EK 1.5.A.3.i states that NREM sleep occurs in Stages 1 through 3."),
 dict(q="Across a full night's sleep, the duration of NREM sleep", choices=[
   "decreases as the cycle progresses",
   "increases as the cycle progresses",
   "stays exactly the same in every cycle",
   "disappears entirely after the first cycle"], ans=0,
   why="EK 1.5.A.3.i states that NREM sleep decreases in duration throughout the cycle, the mirror image of REM's increasing frequency in EK 1.5.A.3.ii."),
 dict(q="Across a full night's sleep, the frequency of REM sleep", choices=[
   "increases as the cycle progresses",
   "decreases as the cycle progresses",
   "remains constant throughout the night",
   "peaks in the first ten minutes and then stops"], ans=0,
   why="EK 1.5.A.3.ii states that the frequency of REM sleep typically increases as the cycle progresses."),
 dict(q="The brief sensations of falling or of a flash of light that occur as a person is just drifting off to sleep are called", choices=[
   "hypnagogic sensations",
   "REM rebound",
   "night terrors",
   "circadian shifts"], ans=0,
   why="EK 1.5.A.3.i states that hypnagogic sensations occur as one enters initial Stage 1 sleep."),
 dict(q="REM sleep is described as paradoxical because", choices=[
   "the brain produces waves similar to wakefulness while the body is at its most relaxed",
   "it occurs only in people who are sleep deprived",
   "the sleeper is fully aware of the surrounding room",
   "the body moves vigorously while the brain is inactive"], ans=0,
   why="EK 1.5.A.3.ii states that REM sleep is considered paradoxical because it produces waves similar to wakefulness but the body is at its most relaxed."),
 dict(q="Dreaming typically occurs during", choices=[
   "REM sleep",
   "Stage 1 NREM sleep only",
   "the transition between wakefulness and Stage 1",
   "periods of complete EEG silence"], ans=0,
   why="EK 1.5.A.3.ii states that dreaming typically occurs in REM sleep."),
 dict(q="A participant is repeatedly awakened whenever she enters REM sleep. On the following undisturbed night she spends considerably more time in REM sleep than usual. This effect is called", choices=[
   "REM rebound",
   "sleep apnea",
   "a hypnagogic sensation",
   "somnambulism"], ans=0,
   why="EK 1.5.A.3.ii states that when deprived of REM sleep, REM rebound can occur."),
 dict(q="Activation-synthesis theory explains dreams as", choices=[
   "the mind's attempt to make sense of random neural activity during sleep",
   "disguised expressions of unconscious wishes",
   "rehearsals of the following day's planned activities",
   "the result of the body's failure to relax during REM sleep"], ans=0,
   why="EK 1.5.A.4 names activation-synthesis as one of two theories of dreams in scope; it treats the dream as the brain's synthesis of activity generated during sleep. The psychoanalytic account of disguised wishes is explicitly excluded from the exam."),
 dict(q="Consolidation theory explains dreams and sleep in terms of", choices=[
   "the organizing and strengthening of memories formed during the day",
   "the release of unconscious conflicts from childhood",
   "random firing that carries no relationship to waking life",
   "the body's need to lower its temperature at night"], ans=0,
   why="EK 1.5.A.4 names consolidation theory alongside activation-synthesis, and EK 1.5.A.5 states that sleep is useful for organizing and consolidating memories."),
 dict(q="Which theory of dreaming is explicitly outside the scope of the AP Psychology Exam?", choices=[
   "the psychoanalytic theory of dreams",
   "activation-synthesis theory",
   "consolidation theory",
   "the restoration account of sleep"], ans=0,
   why="The exclusion statement under EK 1.5.A.4 places the psychoanalytic theory of dreams outside the scope of the exam, while activation-synthesis and consolidation are the two theories in scope."),
 dict(q="The restoration theory of why sleep occurs proposes that sleep", choices=[
   "replenishes resources the body and brain depleted during the day",
   "reorganizes memories into a coherent narrative",
   "exists only to conserve energy in cold climates",
   "protects a person from encountering predators"], ans=0,
   why="EK 1.5.A.5 gives memory consolidation and restoration as the current theories of why sleep occurs, with restoration meaning the restoring of depleted resources used throughout a given day."),
 dict(q="A person regularly has great difficulty falling asleep and staying asleep, and feels tired the next day. The disorder that best matches this description is", choices=[
   "insomnia",
   "narcolepsy",
   "somnambulism",
   "REM sleep behavior disorder"], ans=0,
   why="Insomnia is one of the five disorders EK 1.5.A.6 keeps in scope, and it is defined by persistent difficulty falling or staying asleep."),
 dict(q="A person suddenly falls into sleep during the day, sometimes in the middle of a conversation. The disorder that best matches this description is", choices=[
   "narcolepsy",
   "insomnia",
   "sleep apnea",
   "somnambulism"], ans=0,
   why="Narcolepsy, on EK 1.5.A.6's list, is characterized by sudden uncontrollable episodes of sleep during waking hours."),
 dict(q="A person repeatedly stops breathing for short periods during the night, wakes briefly each time without remembering it, and is exhausted during the day. The disorder that best matches this description is", choices=[
   "sleep apnea",
   "insomnia",
   "narcolepsy",
   "REM sleep behavior disorder"], ans=0,
   why="Sleep apnea, on EK 1.5.A.6's list, involves repeated interruptions of breathing during sleep and the daytime fatigue that follows."),
 dict(q="A child gets out of bed, walks through the house, and returns to bed with no memory of it in the morning. The disorder that best matches this description is", choices=[
   "somnambulism",
   "narcolepsy",
   "sleep apnea",
   "insomnia"], ans=0,
   why="Somnambulism, on EK 1.5.A.6's list, is sleepwalking: complex motor behavior during sleep that the sleeper does not recall."),
 dict(q="An adult physically acts out the content of his dreams, kicking and shouting, because the muscle relaxation typical of one sleep stage is absent. The disorder that best matches this description is", choices=[
   "REM sleep behavior disorder",
   "somnambulism",
   "insomnia",
   "sleep apnea"], ans=0,
   why="REM sleep behavior disorder, on EK 1.5.A.6's list, is defined by the loss of the muscle relaxation that normally accompanies REM sleep, allowing dream content to be enacted; sleepwalking occurs in NREM sleep instead."),
 dict(q="According to EK 1.5.A.6, treating sleep disorders and keeping a regular sleep schedule", choices=[
   "can improve waking performance and overall well-being",
   "affects nighttime experience but not daytime functioning",
   "is effective only for insomnia",
   "eliminates the need for REM sleep"], ans=0,
   why="EK 1.5.A.6 states that treating sleep disorders and following regular sleeping schedules can improve waking performance and overall well-being."),
 dict(q="A researcher records participants' EEG patterns overnight and counts the minutes spent in each sleep stage, without introducing any treatment. This study is best described as", choices=[
   "descriptive research, which cannot establish a cause",
   "an experiment with sleep stage as the independent variable",
   "a case study of a single unusual participant",
   "a correlational study with a randomly assigned treatment"], ans=0,
   why="Nothing was manipulated and nothing was assigned, so the design describes and measures rather than tests a cause; the phrase 'randomly assigned' in the last option contradicts 'correlational' and is the giveaway that it is not a real design."),
 dict(q="A study reports that students who sleep fewer than six hours a night earn lower grades than students who sleep more. Before concluding that short sleep lowers grades, a careful reader should note that", choices=[
   "students were not assigned their sleep durations, so a third variable such as workload could explain both",
   "grades cannot be measured objectively",
   "sleep duration has no relationship to cognitive performance",
   "the study must have used an EEG to be valid"], ans=0,
   why="Science practice 2: sleep duration was measured rather than manipulated, so the design is correlational and a third variable remains a live explanation, even though EK 1.5.A.6 does say sleep disruption can affect cognitive performance."),
 dict(q="A sleep researcher watches a monitor and must decide whether a participant is currently in REM sleep or in Stage 3. The most reliable basis for that decision is", choices=[
   "the EEG pattern, which in REM resembles wakefulness rather than deep sleep",
   "how long the participant has been asleep in total",
   "whether the participant's body is moving",
   "whether the participant later reports having dreamed"], ans=0,
   why="EK 1.5.A.3 states that sleep stages are identified by their specific EEG patterns, and EK 1.5.A.3.ii adds that REM's waves resemble wakefulness; body stillness cannot distinguish the two because REM is when the body is most relaxed."),
 dict(q="A commuter drives a familiar route home and arrives with almost no memory of the drive itself, although she stopped at every light. This is best described as", choices=[
   "a lower level of awareness within waking consciousness",
   "a brief episode of REM sleep",
   "an instance of somnambulism",
   "a disruption of the circadian rhythm"], ans=0,
   why="EK 1.5.A.1 describes consciousness as having varying levels of awareness rather than being all-or-nothing; the driver remained awake and responsive, so no sleep state or circadian disruption is involved."),
 dict(q="According to the AP Psychology framework, chronic sleep disruption is most likely to", choices=[
   "impair both physical and cognitive performance during waking hours",
   "affect mood at night but leave daytime functioning unchanged",
   "produce effects only in people who already have a sleep disorder",
   "increase the total amount of NREM sleep obtained each night"], ans=0,
   why="EK 1.5.A.6 states that sleep disruptions can affect physical and cognitive performance during wakefulness, and that treating disorders and keeping regular schedules improves waking performance."),
 dict(q="Researchers plan a study in which participants will be kept awake for 30 hours and then tested on a reaction-time task. Which step is most necessary for the study to meet ethical standards?", choices=[
   "telling participants in advance what the procedure involves and that they may withdraw at any time",
   "concealing the true purpose of the study from every participant permanently",
   "recruiting only participants who report no interest in sleep research",
   "guaranteeing in advance that no participant will feel any discomfort"], ans=0,
   why="Science practice 2.D concerns whether a research scenario followed appropriate ethical procedures; informed consent and the right to withdraw are the standard safeguards, whereas a guarantee of zero discomfort is not something a sleep-deprivation study could honestly offer."),
 dict(q="A researcher studying sleep wants to operationally define \"sleep quality.\" The best operational definition is", choices=[
   "the number of times per night the participant's EEG shows a return to wakefulness",
   "how rested the participant seems to the researcher",
   "the general restfulness of the participant's night",
   "whether the participant enjoyed sleeping"], ans=0,
   why="An operational definition must state the specific measurement procedure; a count of EEG-recorded awakenings can be tallied, while the other options restate the construct in words that are no more measurable than the construct itself."),
]
