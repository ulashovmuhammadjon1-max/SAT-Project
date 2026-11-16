# "30 Days to 1500": an interactive SAT story series (scenario for approval)

**The premise, in one line:** Max needs a 1500 on the SAT in 30 days to keep a full scholarship, and the audience
decides everything he does.

It's built on what made `@trz_ftb` and `@interactive_works` grow (see `video/PLAYBOOK.md`):
- an unfinished story,
- the audience votes and "the top answer decides" the next part,
- stakes shown as meters on screen,
- one part every day.

The premise, characters and look are our own. Every episode also contains one **real** question from a
scholarly.space test, so the series teaches as it entertains.

## The series rules (keep them honest)
- **One episode a day, 40 s at most** (the owner's cap), titled "DAY N / 30". Days can skip ("DAY 4") when nothing
  happens.
- **Every episode ends on an A/B choice:** "Comment A or B. The top answer decides Day N+1."
  - The option with more comments by the next morning wins, and the owner tells Claude which one.
  - We always follow the winner, even when it's the "wrong" choice.
- **Three meters on screen:**
  - DAYS LEFT
  - ⚡ ENERGY (0–100%): low energy makes his practice scores worse, and rest refills it
  - SCORE → GOAL 1500

  Energy is what makes every vote a real debate: studying drains it, rest refills it.
- **The score moves only when he takes a practice test,** by believable amounts (−20 to +60), and it can go down.
  **He can fail.** The finale isn't decided in advance, and that uncertainty is the reason to follow.
- **Each episode has one real question** with its source on screen ("From Test 31 · free on scholarly.space"), a
  3-2-1 countdown, and the trap revealed. Every answer is verified with sympy before it's used.
- **scholarly.space lives inside the story:** Max's practice tests run on it (the laptop shows the real site).
  Later, "The 1580", an older student who scored 1580 and tutors for free, can enter the story; that is a real
  free feature of the site. Never claim real-world score gains.
- **Fiction and AI:** label the voice and visuals as AI if the platform asks.

## Characters
- **Max** (17): our 3D student. Smart, overconfident, a little lazy, and you want him to win.
- **Mira** (12): his little sister. Sarcastic one-liners; she's secretly rooting for him.
- **Aziz:** his best friend, always planning something fun. He's the temptation, but he's not a villain.
- **The 1580** (enters around Day 3–5): calm, strict, free. She only helps if Max does the homework.

## Day 1: "1210"

Bedroom at night: desk, laptop, lamp, phone, a window with city lights, an unmade bed.
**HUD on screen the whole time (top):** `DAY 1 / 30` · `⚡ 30%` · `SCORE 1210 → 1500`.
**The question:** Test 31, Math Module 2 (Hard), Q22 (`AUTHORED/T31-MATH_M2H:M2H-22`).
- Stem: two similar conical hoppers, heights 2 : 5, the smaller holds 96 L. How much does the larger hold?
- Choices: 240 / 600 / 1,500 / 6,000, key **1,500**.
- Verified with sympy: 96 × (5/2)³ = 1,500. The traps are 240 (scaling the volume like a length) and 600 (scaling
  it like an area).

| Time | Visual | On screen (carries it on mute) | Voice |
|---|---|---|---|
| 0–3.5 | Push in on the laptop: a big red **1210**, Max's face lit by the screen | **HE NEEDS 1500 IN 30 DAYS** · **YOU CONTROL HIM** | "Max needs a fifteen hundred for a full scholarship. Thirty days. You decide everything." |
| 3.5–6 | The score report scrolls to the question his "240" click is still on | 1210 · 290 SHORT | "He just scored twelve-ten. This question cost him." |
| 6–10 | Full-screen question card: two cones (2 : 5), "96 L" on the small one, choices A–D | Two similar cones · heights 2 : 5 · small = 96 L · big = ? | "Two similar cones, heights two to five. The small one holds ninety-six litres. The big one?" |
| 10–13 | Countdown, ticking clock, music lifts | **SOLVE IT BEFORE MAX ⏱ 3 · 2 · 1** · From Test 31 · free on scholarly.space | (silence, tick) |
| 13–19 | A red ✗ on **A) 240** (buzzer), then the small cone pours into the big one; a green circle on **C) 1,500** (ding) | VOLUME GROWS WITH THE **CUBE** · (5/2)³ × 96 = **1,500** | "Max said two-forty. Wrong. Volume grows with the *cube*… fifteen hundred." |
| 19–22 | Hard cut: his phone buzzes in the dark. **Aziz 🎉**: *"party at mine TOMORROW. u in??"* The ⚡ meter flashes **30%** | (the chat bubble) · ⚡ 30% | "Then… his phone buzzes." |
| 22–31 | Split screen. **A:** Aziz's party, lights. **B:** Max at the desk with practice test #2 on scholarly.space. | **A) PARTY** ⚡ +50%, but lose a night · **B) STUDY** 📈 practice, but ⚡ −20% · **COMMENT A OR B 👇 · TOP ANSWER DECIDES DAY 2** | "Party… or study? Comment A or B. The top answer decides Day 2." |
| 31–34 | Max looks at the camera, unsure | **FOLLOW FOR DAY 2** | "Follow for Day 2." |
| 34–36 | Hard cut back to the red **1210** (the opening frame) | DAY 1 / 30 | — |

About 36 s and about 70 spoken words. Cut from the first draft: the scholarship letter (now in the first line), the
score breakdown, and the spoken energy explanation (the A/B cards carry it on screen). The phone buzz comes 1 s
after the answer, so there's no natural "it's over" point before the vote.

### Hook variants (test across days or platforms)
1. "Max needs a 1500 on the SAT in 30 days. And you decide everything he does." (in the script above)
2. "He just scored 1210. He needs 1500. You have 30 days to get him there."
3. "POV: you control a student who needs a 1500 in 30 days."
4. "Party or study? His full scholarship depends on what you comment."
5. "This SAT question tricked him. Can you do it before he does?"

### Caption
"Day 1 of 30 😬 Max needs a 1500 for a full scholarship, and YOU control every move. Party or study? Comment A or B
👇 The top answer decides Day 2. (The question is real: Test 31, free on scholarly.space.) #SAT #satprep #pov
#storytime #studytok #whatwouldyoudo"

## Where each answer leads (for us, never shown in advance)
- **A wins (party):** Day 2. He has fun and his energy goes to 80%. At the party, Aziz's cousin turns out to be
  "the 1580". She sees him doing math on a napkin and offers to help, but only if he does what she says.
- **B wins (study):** Day 2. He grinds through practice test #2 at 2 a.m. His energy drops to 10%, and his score
  barely moves (1230, +20). A sharp lesson: tired studying doesn't stick. The next vote is about sleep, or a
  shortcut.

Both branches stay interesting, so whatever wins, Day 2 has a twist.

## Production
- **Reuse:**
  - the 3D student,
  - the laptop with the real scholarly.space screen,
  - the countdown, ding and buzzer,
  - the caption and pill styles.
- **Build new for Day 1:**
  - a night bedroom set,
  - phone and chat UI overlays,
  - the HUD meters,
  - the cone-filling animation,
  - an A/B split-screen card.

  These become the reusable kit for every later day.
- **Voice:** one narrator, chosen from `video/voice/voice-audition.mp4`. A free voice means no credit limit on
  daily episodes.
- **Every day:** the owner reports the winning comment, Claude writes and renders the next day. The render takes
  about 20–30 min; the first episode takes longer because the sets are new.
