# Brief: authoring AP Macroeconomics question banks

Every agent working on Macro follows this document. It exists so six people
writing in parallel produce one coherent bank rather than six different ones.

## The unit of work is one CED topic = one Python module = 50 questions

File name: `m<unit>_<topic>.py` in `content-pool/ap-banks/` — so Unit 3 topic 3.4
is `m3_4.py`. Unit 1 topic 1.1 (`m1_1.py`) is already written; read it first as
the reference for voice and structure.

```python
# MACRO 3.4 Long-Run Aggregate Supply — 50 questions
# Table verified: <work the arithmetic out here, line by line>
TOPIC = ("3.4", "Long-Run Aggregate Supply", 3)   # code, title, unit number
LRAS = dict(headers=[...], rows=[[...], ...])      # optional, only if needed
QUESTIONS = [
 dict(q="<stem>", choices=["...","...","...","...","..."], ans=1,
      why="<one sentence saying why the key is right>"),
 dict(q="<stem>", table=LRAS, choices=[...], ans=2, why="..."),
]
```

Exactly **50** questions, exactly **5** choices each, all five **distinct**,
`ans` a 0-based index. `why` is one sentence, written for a student who just got
it wrong. Use the CED topic code and title exactly as listed in
`src/lib/ap/courses.ts` — do not invent or reword them.

## Validate before you commit — the exporter is the gate

```
cd content-pool/ap-banks
python3 export_units.py m3_1 m3_2 --subject MACRO --out /tmp/check.json
```

It refuses to write a file unless every module has exactly fifty questions with
five distinct choices and an in-range key, and it warns on repeated stems. A
warning is not automatically a defect — a definition may legitimately recur
across units — but read every one and decide. Two stems repeated *inside your
own unit* is always a defect: rewrite one.

## Rules that come from defects already found in this project

1. **Every number in a table must be worked out in a comment at the top of the
   module.** A Unit 6 externality table shipped a "socially efficient quantity"
   question when no quantity in the table actually equated marginal social cost
   with marginal benefit — the question had no defensible answer. If you cannot
   derive the answer from the table you wrote, the table is wrong, not the
   question.
2. **Never name an option by its letter** ("as in option B"). Keys are shuffled
   at export, so a letter reference silently becomes wrong. Refer to choices by
   their content.
3. **Do not write the answer into the stem's grammar.** Avoid a correct choice
   that is conspicuously longer, hedged, or the only one that reads as a
   complete sentence. Distractors must be genuinely tempting and must be things
   a student actually believes.
4. **Do not cluster the key.** Vary `ans` as you write. The exporter reshuffles,
   but a bank written entirely with `ans=1` tends to have near-identical
   distractor structure, which is its own tell.
5. **Numeric choice lists stay in ascending order.** The exporter deliberately
   leaves numeric ladders unshuffled, because a student reasonably expects
   ordered values and a scrambled ladder reads as a typo.

## Coverage: aim at what the exam actually asks

Across a topic's fifty questions, roughly: 15 definitional and conceptual, 20
applied ("an increase in X causes Y to..."), 10 that require a calculation or a
table, and 5 that are genuinely hard — a two-step chain, a case where the
direction of an effect is indeterminate, or a common misconception cornered.
Macro rewards graph reasoning, so lean on questions that ask which curve shifts,
in which direction, and what happens to output, the price level, and
unemployment as a result.

Where a topic has a standard diagram (AD-AS, the money market, loanable funds,
the Phillips curve, the foreign exchange market), write questions that describe
the shift in words rather than assuming an image — there are no figures in this
bank. "An increase in the money supply shifts..." works; "in the graph shown"
does not.

## Committing — do this after every single topic, not at the end

The session running you can be cut off at any time. Work that is not pushed is
lost. After each module validates:

```
git add content-pool/ap-banks/m3_4.py
git commit -m "AP Macro 3.4: <topic title>, 50 questions"
git pull --rebase origin claude/new-session-3w59v3
git push -u origin claude/new-session-3w59v3
```

Several agents share this working directory, so `git` can fail with an
`index.lock` error or a rejected push. Both are expected and both are safe to
retry: wait a few seconds and run the command again. Never use `git push
--force`, never `git checkout`/`git reset` a file you did not write, and never
`git rm` another agent's module — you would be destroying a sibling's work.

Stay inside your assigned unit. Do not edit `export_units.py`, another agent's
modules, or anything outside `content-pool/ap-banks/`.
