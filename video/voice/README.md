# The house voice: Liam

The owner's pick after SAT Short #2 v4 ("insanely good"). Use this voice for every scholarly.space video unless
told otherwise.

| | |
|---|---|
| Voice | ElevenLabs premade **"Liam - Energetic, Social Media Creator"** (young adult male, warm, energetic) |
| Voice ID | `TX3LPaxmHKxFdv7VOQHJ` |
| Generated through | the **vidIQ connector**, `vidiq_voiceover_generate` |
| Reference take | `liam-reference.mp3` (38.5 s, the full v4 script below, unedited) |
| Speed in the video | **1.2×** (`atempo=1.2`), the long end-card line 1.28×, the short sign-off 1.12× |

The earlier videos used Kokoro `am_puck` (local, free). The owner found Liam much better, so don't fall back to
Kokoro without saying so.

## Generating a new take

1. Write the whole script as one text, **one paragraph per line** of the video (the pauses between paragraphs
   become the cut points).
2. Spell out anything the voice could misread:
   - "three to the two s", not "3^(2s)"
   - "fifteen-eighty", not "1580"
   - "scholarly dot space", not "scholarly.space"
   - "thirty-one plus", not "31+"

   Captions on screen still use digits; only the voice script is spelled out.
3. Call `vidiq_voiceover_generate` with `voiceId: "TX3LPaxmHKxFdv7VOQHJ"`, the script, and `output: "url_only"`.
4. Poll `vidiq_job_poll` until it's done, then download the MP3.
5. Transcribe it (`npx hyperframes transcribe take.mp3`) to find where each line starts and ends.
6. Write a ranges file and cut it:
   ```
   ./cut_lines.sh take.mp3 my-video.ranges ../my-video/assets/voice
   ```
   `sat-hardest.ranges` is a worked example. Running it on `liam-reference.mp3` reproduces the v4 lines exactly.
   You can drop a phrase by starting a cut after it: L3 skips "Here's the trick:".
7. Place each line as its own `<audio>` clip at volume 1.15. After rendering, normalise the whole mix:
   ```
   ffmpeg -i raw.mp4 -c:v copy -af loudnorm=I=-15:TP=-2:LRA=11 -c:a aac -b:a 192k -ar 48000 final.mp4
   ```

## The mix that went with it (v4)
- Music bed (also from vidIQ, `vidiq_generate_music`) at 0.15, lifted to 0.34 during the 3-second countdown.
- Whoosh on cuts, a ticking clock under the countdown, buzzer on the wrong path, ding on the answer.
- The final file measured −15.7 LUFS integrated, with every section within ±1.5 LU.

## Cost
- The v4 take (about 470 characters of script, 38.5 s of audio) cost **28 vidIQ credits**; the music cost 25.
- The plan refills to 150 credits each billing cycle (the next refill after v4 was 12 Dec 2026).
- Check `vidiq_balance` before generating, and don't start a take the balance can't cover.
- Mark these videos as AI-voiced where the platform asks.

## The v4 script, as sent
```
The hardest type of SAT math question. Can you solve it?

Three to the two s equals seven. What is three to the six s?

Here's the trick: you don't need to find s. Six s is just two s, times three.

So three to the six s is three to the two s... cubed.

And that's seven cubed. Three hundred forty-three. The answer is A!

Scholarly dot space is a non-profit, with thirty-one plus free SAT practice tests, and free one-on-one sessions with a fifteen-eighty scorer.

Join the community!
```
