# Mission

**Scholarly exists to give a student anywhere the preparation that, until now,
only a paid tutor in the right city could give them — and to be honest with
them about what it is worth.**

The platform is a Digital SAT practice environment (full-length adaptive tests
in a Bluebook-style interface, a question bank, vocabulary sets with spaced
repetition, analytics, mentoring and classes) and a growing library of AP
subject banks. It is free to the student. It is built for the student who has
a phone, an internet connection, and no one to ask.

## What we are actually promising

A student sitting a practice test is spending hours they cannot get back, and
they are deciding what to study next based on what we tell them. That makes two
things non-negotiable:

1. **A question must be right.** Not plausible, not close — right. A wrong
   answer key does more damage than a missing question, because the student
   learns the error and trusts it.
2. **A number we show must be true.** The public impact page computes every
   figure from the live database on render, so nothing can quietly go stale or
   be inflated. *A claim anyone can check is worth more than a bigger claim
   nobody can.*

Everything procedural in `CLAUDE.md` — the verification gates, the negative
controls, the refusal to bulk-convert notation, the rule that an uncertain
question is cut rather than guessed — is downstream of those two sentences.
None of it is bureaucracy. Each rule is there because the failure it prevents
already happened once and reached a real student.

## The principles that follow

**Verify, don't assume.** Every measurable claim in this repository was
measured. The books we bought have wrong answer keys about once in eighteen
questions. Transcribed content misreports its keys; authored content does not.
We know these rates because we counted, and we counted before deciding.

**A checker that cannot fail is worse than no checker**, because it teaches you
to trust output that means nothing. Every check runs a negative control: corrupt
the thing on purpose, confirm the check screams. This has caught real defects
five separate times, including a topic extractor that returned zero topics and
reported success.

**Withhold the answer from the tool that is grading it.** Authoring agents never
see the marked key; they derive the answer themselves and their answer is
compared afterwards. This is the difference between an instruction an agent can
drift from and a property of the workflow. Across 1,233 questions it held back
29 disputed keys and shipped zero explanations arguing for a wrong one.

**Cut what you are unsure of.** A short topic honestly reported beats a full one
with a lie in it. Where the source is silent — as the Biology CED genuinely is
about the mechanism of exocytosis — we key only what the source supports, and we
do not fill the hole from memory.

**Never destroy a student's history.** Past attempts store the *index* a student
selected. Questions are retired, never deleted; stored strings are converted in
place, never re-exported. A shuffle that moves one choice silently rewrites what
every past student appears to have answered.

**Ship durably.** Commit after every topic, never at the end. Sessions die
mid-run; the work that was committed survives and the work that was buffered
does not. This rule has rescued an authoring run repeatedly.

## Scope

Free for students, and intended to stay that way. The content is original — the
exam interface recreates general layout conventions without copying proprietary
assets or text, and the question banks are written against the College Board's
published Course and Exam Descriptions rather than lifted from them.

---

`CLAUDE.md` is the operating manual and the accumulated record of what has gone
wrong. This file is why any of it matters. Read this one first.
