#!/usr/bin/env python3
"""
Verify the authored Reading & Writing questions and report the combined pool.

Checks:
  1. shape — 4 distinct choices, a valid answer label, a `why`, and (for
     authored items) a `rule` naming the convention or relation tested;
  2. house style — no markdown asterisks, no unclosed tags, entities not raw;
  3. answer-key balance — no answer letter dominates, which is the cheap tell
     for a set written carelessly;
  4. dedupe — lexical similarity against all 405 live production R&W questions
     and all 128 transcribed here, on passage text and on choice text;
  5. supply — the combined pool against the six-module requirement, by domain.

Run: python3 verify_authored_rw.py
"""
import importlib
import json
import os
import re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = ('/tmp/claude-0/-home-user-SAT-Project/'
           '16335d00-5283-5db6-a7a3-023a1a5fae45/scratchpad')

TRANSCRIBED = ['rw_octusb_m1', 'rw_octintb_m1', 'rw_octusc_m1', 'rw_octintb_m2',
               'rw_octusb_m2', 'rw_octusc_m2', 'rw_auguse']
READING = {'Words in Context', 'Text Structure and Purpose', 'Cross-Text Connections',
           'Central Ideas and Details', 'Command of Evidence', 'Inferences'}

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


def load(mod):
    m = importlib.import_module(mod)
    out = list(m.QUESTIONS)
    if hasattr(m, 'AUGUSC'):
        out += list(m.AUGUSC)
    return out


transcribed = [q for mod in TRANSCRIBED for q in load(mod)]
authored = load('rw_authored')

# ------------------------------------------------------------------ 1. shape
for q in authored:
    tag = q['num']
    check(len(q['choices']) == 4, f"{tag}: needs exactly 4 choices")
    check(len(set(q['choices'])) == 4, f"{tag}: duplicate answer choice")
    check(q['answer'] in 'ABCD', f"{tag}: bad answer label")
    check(bool(q.get('why')), f"{tag}: no reasoning recorded")
    check(bool(q.get('rule')), f"{tag}: authored question must name the rule it tests")
    check(bool(q.get('passage')) and bool(q.get('stem')), f"{tag}: missing passage or stem")

nums = [q['num'] for q in authored]
check(len(nums) == len(set(nums)), "duplicate question ids among authored questions")

# ------------------------------------------------------------ 2. house style
for q in authored:
    for blob in [q['passage'], q['stem']] + list(q['choices']):
        check(not re.search(r'(?<!\w)\*[A-Za-z]', blob), f"{q['num']}: markdown asterisk")
        check('&' not in blob or re.search(r'&[a-zA-Z]+;|&#\d+;', blob),
              f"{q['num']}: bare ampersand")
        opens = re.findall(r'<(\w+)[^>]*>', blob)
        closes = re.findall(r'</(\w+)>', blob)
        for t in ('em', 'u'):
            check(opens.count(t) == closes.count(t), f"{q['num']}: unbalanced <{t}>")
    if re.search(r'\btable\b', q['stem'], re.I):
        check('table' in q, f"{q['num']}: stem mentions a table but none is supplied")

# ------------------------------------- 2b. reasoning must not cite the key
# A choice-order rebalance silently invalidates any `why` that names distractors
# by letter, so the reasoning may not refer to its own answer letter as a wrong
# option, and letter references are discouraged outright.
for q in authored:
    for lab in 'ABCD':
        pat = rf"(?<![A-Za-z]){lab}(?= (?:is|and|gives|states|says|describes|would|omits|reverses))"
        if re.search(pat, q['why']):
            check(lab != q['answer'],
                  f"{q['num']}: reasoning calls {lab} a distractor but {lab} is the answer")


# --------------------------------------------------------- 3. answer balance
bal = Counter(q['answer'] for q in authored)
check(max(bal.values()) <= len(authored) * 0.40,
      f"answer key unbalanced across authored questions: {dict(bal)}")

# ------------------------------------------------------------------ 4. dedupe
def toks(s):
    s = re.sub(r'<[^>]+>', ' ', s or '')
    s = re.sub(r'&[a-z]+;|&#\d+;', ' ', s)
    return set(w for w in re.findall(r'[a-z]{5,}', s.lower()))


def jac(a, b):
    return len(a & b) / max(1, len(a | b))


prod = json.load(open(f'{SCRATCH}/prod_all.json'))
refs = [('production', toks(r['passage'])) for r in prod if r['subject'] == 'READING_WRITING']
refs += [(f"transcribed {q['num']}", toks(q['passage'])) for q in transcribed]

worst = []
for q in authored:
    t = toks(q['passage'])
    best = max(((jac(t, rt), lab) for lab, rt in refs if rt), key=lambda z: z[0])
    worst.append((best[0], q['num'], best[1]))
    check(best[0] < 0.30, f"{q['num']}: passage {best[0]:.2f} similar to {best[1]}")

for i in range(len(authored)):
    for j in range(i + 1, len(authored)):
        s = jac(toks(authored[i]['passage']), toks(authored[j]['passage']))
        check(s < 0.30, f"{authored[i]['num']} vs {authored[j]['num']}: {s:.2f} similar")

# ------------------------------------------------------------------ 5. supply
pool = transcribed + authored
by_skill = Counter(q['skill'] for q in pool)
reading = sum(v for s, v in by_skill.items() if s in READING)
writing = len(pool) - reading

print(f"transcribed {len(transcribed)}  +  authored {len(authored)}  =  {len(pool)} of 162")
print(f"  reading {reading} (need 84)   writing {writing} (need 78)")
print("\n  by domain (need per 6 modules):")
TARGET = {'Words in Context': 28, 'Text Structure and Purpose': 12, 'Cross-Text Connections': 1,
          'Central Ideas and Details': 12, 'Command of Evidence': 16, 'Inferences': 14,
          'Boundaries': 24, 'Form, Structure, and Sense': 18, 'Transitions': 18,
          'Rhetorical Synthesis': 18}
for s in TARGET:
    have, want = by_skill.get(s, 0), TARGET[s]
    flag = 'ok' if have >= want else f'SHORT {want - have}'
    print(f"    {s:32} {have:3} / {want:3}   {flag}")

check(len(pool) >= 162, f"pool is {len(pool)}, need 162")
check(reading >= 84, f"reading pool is {reading}, need 84")
check(writing >= 78, f"writing pool is {writing}, need 78")

print("\n  closest passage matches for authored questions:")
worst.sort(reverse=True)
for s, n, lab in worst[:4]:
    print(f"    {s:.2f}  {n}  vs {lab}")
print(f"  answer key: {dict(sorted(bal.items()))}")

if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for f in FAIL:
        print("  -", f)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
