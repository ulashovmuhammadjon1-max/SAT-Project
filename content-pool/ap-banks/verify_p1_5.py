"""Key audit for AP PSYCHOLOGY 1.5 Sleep.

One (anchor, claim) per item: the anchor must appear in the keyed choice and in
no distractor, which is the machine-checkable half; the claim records what the
key rests on in the framework's own terms, which is the half a human audits.

Two closed lists and one exclusion govern this topic, and all three are enforced
by reading rather than by a regex, so they are stated here:

  * EK 1.5.A.6 lists the sleep disorders in scope -- insomnia, narcolepsy, REM
    sleep behavior disorder, sleep apnea, somnambulism. No disorder outside that
    list appears as a key OR as a distractor, so a student is never asked to
    reject a term the course never taught.
  * The exclusion statement under EK 1.5.A.4 places the psychoanalytic theory of
    dreams outside the exam. It appears only in item 16, where rejecting it IS
    the point, and as a distractor in item 14; it is never a key.
  * EK 1.5.A.4 and 1.5.A.5 give exactly two dream theories (activation-synthesis,
    consolidation) and two theories of why sleep occurs (memory consolidation,
    restoration). Nothing else is offered as a correct account.

The direction pairs this topic invites a writer to reverse, tested against each
other on purpose: NREM DECREASES in duration across the night (EK 1.5.A.3.i)
while REM INCREASES in frequency (EK 1.5.A.3.ii) -- items 8 and 9 are adjacent so
that neither can be answered by pattern-matching the other. Likewise
somnambulism (NREM sleepwalking, no recall) against REM sleep behavior disorder
(dream enactment because REM's muscle relaxation is absent) in items 21 and 22.

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p1_5

CLAIMS = [
 ("varying levels of awareness",
  "EK 1.5.A.1: consciousness has varying levels of awareness of thoughts, feelings, behavior, and events in the internal and external worlds. 'Levels', not a switch, is the load-bearing word."),
 ("two types of consciousness",
  "EK 1.5.A.1 states that sleep and wakefulness are two types of consciousness, which rules out treating sleep as the absence of consciousness -- the distractor most students would accept."),
 ("roughly 24 hours",
  "EK 1.5.A.2: the sleep/wake cycle is a circadian rhythm, which in humans is about a 24-hour cycle."),
 ("disruption of the circadian rhythm",
  "EK 1.5.A.2 names shift work explicitly as a disruption of the circadian rhythm. Narcolepsy would be a disorder from the EK 1.5.A.6 list, which this scenario does not describe."),
 ("still aligned to her original time zone",
  "EK 1.5.A.2 names jet lag as a circadian disruption. The key states the mechanism -- an internal cycle out of step with local time -- rather than just the label, and it is temporary, so no disorder from the EK 1.5.A.6 list applies."),
 ("their specific EEG patterns",
  "EK 1.5.A.3, verbatim: the stages of sleep are identified by their specific EEG patterns. This is what connects Topic 1.5 to the research methods in EK 1.4.A.7."),
 ("Stages 1 through 3",
  "EK 1.5.A.3.i: NREM sleep occurs in Stages 1 through 3. The 'Stages 1 through 5' distractor is the pre-revision numbering students still meet in older material."),
 ("decreases as the cycle progresses",
  "EK 1.5.A.3.i: NREM sleep decreases in duration throughout the cycle. Paired deliberately with the next item, which runs the opposite direction."),
 ("increases as the cycle progresses",
  "EK 1.5.A.3.ii: the frequency of REM sleep typically increases as the cycle progresses. Adjacent to item 8 so the two directions must actually be known, not guessed from a single remembered fact."),
 ("hypnagogic sensations",
  "EK 1.5.A.3.i: hypnagogic sensations occur as one enters initial Stage 1 sleep."),
 ("waves similar to wakefulness while the body is at its most relaxed",
  "EK 1.5.A.3.ii, near verbatim: REM is considered paradoxical because it produces waves similar to wakefulness but the body is at its most relaxed. The final distractor inverts both halves at once."),
 ("REM sleep",
  "EK 1.5.A.3.ii: dreaming typically occurs in REM sleep. 'Typically' is the framework's own hedge and the key does not overstate it."),
 ("REM rebound",
  "EK 1.5.A.3.ii: when deprived of REM sleep, REM rebound can occur. The scenario supplies the deprivation and the subsequent excess, which is the definition."),
 ("random neural activity during sleep",
  "EK 1.5.A.4 names activation-synthesis as one of the two dream theories in scope: the dream is the mind's synthesis of neural activity generated during sleep. The 'disguised wishes' distractor is the psychoanalytic account, excluded from the exam by the statement under EK 1.5.A.4, so it can appear as a distractor but never as a key."),
 ("organizing and strengthening of memories",
  "EK 1.5.A.4 names consolidation theory, and EK 1.5.A.5 supplies its content: sleep is useful for organizing and consolidating memories. The 'random firing' distractor is activation-synthesis, the other in-scope theory, so the item discriminates within the pair rather than against a straw man."),
 ("psychoanalytic theory of dreams",
  "The exclusion statement under EK 1.5.A.4 places the psychoanalytic theory of dreams outside the scope of the AP Psychology Exam. This is the one item where naming the excluded theory is the correct response."),
 ("replenishes resources",
  "EK 1.5.A.5: restoration theory holds that sleep restores depleted resources used throughout a given day. Its partner theory, memory consolidation, is the first distractor, so the item separates the two accounts EK 1.5.A.5 gives together."),
 ("insomnia",
  "Insomnia is on EK 1.5.A.6's closed list; persistent difficulty falling and staying asleep with daytime tiredness is what the term denotes. Every distractor is also drawn from that list, so nothing outside the course appears."),
 ("narcolepsy",
  "Narcolepsy is on EK 1.5.A.6's closed list and denotes sudden, uncontrollable sleep episodes during waking hours."),
 ("sleep apnea",
  "Sleep apnea is on EK 1.5.A.6's closed list and denotes repeated interruptions of breathing during sleep, with unremembered brief awakenings and consequent daytime exhaustion."),
 ("somnambulism",
  "Somnambulism is on EK 1.5.A.6's closed list and denotes sleepwalking -- complex motor behavior during sleep with no memory of it afterward."),
 ("REM sleep behavior disorder",
  "REM sleep behavior disorder is on EK 1.5.A.6's closed list. The stem supplies its mechanism: the muscle relaxation that EK 1.5.A.3.ii says accompanies REM is absent, so dream content is enacted. That mechanism is what separates it from somnambulism in item 21, which occurs in NREM sleep."),
 ("improve waking performance and overall well-being",
  "EK 1.5.A.6, near verbatim: treating sleep disorders and following regular schedules for sleeping can improve waking performance and overall well-being."),
 ("descriptive research, which cannot establish a cause",
  "Science practice 2.C: nothing is manipulated and nothing is assigned, so the design measures and describes. The last distractor is self-contradictory -- a correlational study has no randomly assigned treatment -- which is itself the thing being tested."),
 ("not assigned their sleep durations, so a third variable",
  "Science practice 2: sleep duration was measured, not manipulated, so workload or another third variable could produce both the short sleep and the lower grades. EK 1.5.A.6 does say sleep disruption affects cognitive performance, which makes the causal conclusion tempting rather than absurd -- that is why the item is worth asking."),
 ("EEG pattern, which in REM resembles wakefulness",
  "EK 1.5.A.3 (stages are identified by EEG patterns) plus EK 1.5.A.3.ii (REM's waves resemble wakefulness). The 'body is moving' distractor is wrong for a reason the topic supplies directly: REM is when the body is MOST relaxed, so stillness cannot separate REM from deep NREM."),
 ("lower level of awareness within waking consciousness",
  "EK 1.5.A.1's 'varying levels of awareness' applies within wakefulness, not only between sleep and waking. The driver was awake and responsive throughout, so no sleep stage, no disorder from the EK 1.5.A.6 list, and no circadian disruption is involved."),
 ("impair both physical and cognitive performance",
  "EK 1.5.A.6: sleep disruptions can affect physical and cognitive performance during wakefulness. The key deliberately keeps both halves, because the common half-answer is to remember only the cognitive effects."),
 ("may withdraw at any time",
  "Science practice 2.D. Informed consent and the right to withdraw are the applicable safeguards for a procedure this demanding. The 'no discomfort' distractor is the trap: ethical review requires disclosure and consent, not a promise of comfort that a 30-hour deprivation study could not keep."),
 ("number of times per night the participant's EEG shows a return to wakefulness",
  "An operational definition states the countable measurement procedure. EEG-recorded awakenings can be tallied; 'seems rested', 'general restfulness', and 'enjoyed sleeping' restate the construct without operationalizing it."),
]

psych_check.check(p1_5, CLAIMS, per_topic=30, n_choices=4)
