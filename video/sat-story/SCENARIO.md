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
- **One episode a day,** 55–75 s, titled "DAY N / 30". Days can skip ("DAY 4") when nothing happens.
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
| 0.0–4.5 | Push in on the laptop: a big red **1210** on the score report, Max's face lit by the screen | **HE NEEDS 1500 IN 30 DAYS** / **YOU CONTROL EVERYTHING** | "Max needs a fifteen hundred on the SAT. He has thirty days. And you decide everything he does." |
| 4.5–9.5 | His phone lights up on the desk: *SCHOLARSHIP OFFER: full tuition. Condition: SAT 1500+.* Max leans back, hands on his head | FULL SCHOLARSHIP · ONLY IF 1500+ | "If he hits fifteen hundred, the scholarship is his. Tonight, he took his first practice test." |
| 9.5–12.5 | Score report close-up: R&W 640 + Math 570; the gap counter ticks to **−290** | **1210 · 290 SHORT** | "Twelve-ten. Two hundred ninety points short." |
| 12.5–15.5 | Max scrolls to the last question; his click on "240" is still highlighted | THE ONE HE WAS SURE ABOUT… | "And the one he was *sure* he got right… was this one." |
| 15.5–22 | Full-screen question card: two cones (2 : 5), "96 L" on the small one, choices A–D | Two similar cones · heights 2 : 5 · small = 96 L · big = ? | "Two similar cones. Heights two to five. The small one holds ninety-six litres. The big one?" |
| 22–25 | Countdown with a ticking clock, music lifts | **SOLVE IT BEFORE MAX ⏱ 3 · 2 · 1** · From Test 31 · free on scholarly.space | (silence, tick) |
| 25–28 | A red ✗ slams on **A) 240**, buzzer | ✗ 240 · THE TRAP | "Max said two-forty. Wrong." |
| 28–34 | The small cone pours into the big one: it fills ×2.5 high, ×2.5 wide, ×2.5 deep. Green circle on **C) 1,500**, ding | VOLUME GROWS WITH THE **CUBE** · (5/2)³ × 96 = **1,500** | "Volume grows with the *cube*. Five-halves, cubed, times ninety-six… fifteen hundred." |
| 34–37 | Hard cut: his phone buzzes in the dark. Group chat **Aziz 🎉**: *"party at mine TOMORROW. everyone's coming. u in??"* | (the chat bubble itself) | "Then, at midnight… his phone buzzes." |
| 37–41 | Max looks between the phone and the laptop. The ⚡ meter flashes **30%** | ⚡ 30% · SCORE −290 | "His energy is at thirty percent. And he's two hundred ninety points short." |
| 41–49 | Split screen. **A:** Aziz's party, lights and music. **B:** Max at the desk with practice test #2 on scholarly.space. | **A) GO TO THE PARTY** (rest, but lose a night) · **B) STAY & STUDY** (practice, but exhausted) | "So what does Max do? A… go to the party. Or B… stay home and take another practice test." |
| 49–53 | Both cards pulse; a comment-arrow animation | **COMMENT A OR B 👇** · THE TOP ANSWER DECIDES DAY 2 | "Comment A or B. The top answer decides Day 2." |
| 53–56 | Max turns to the camera, unsure | **FOLLOW FOR DAY 2** | "Follow, so you don't miss what happens." |
| 56–57.5 | Hard cut back to the red **1210** (the opening frame) | DAY 1 / 30 | — |

About 57 s, about 150 spoken words. The story opens a new loop (the phone buzz) 1 s after the answer, so nobody
reaches a natural "it's over" point until the vote.

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
