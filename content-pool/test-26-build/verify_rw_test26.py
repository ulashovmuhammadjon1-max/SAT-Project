#!/usr/bin/env python3
"""
Verification pass over the 81 authored Reading & Writing items for Test 26.

Six passes:

  1. Shape        — four distinct choices, a key among them, a passage on every
                    item, a five-underscore blank wherever the stem promises one.
  2. Corpus       — token-signature Jaccard of every passage against the 1,295
                    banked passages in ../rw_authored_corpus.json. 0.50 is the
                    reject line, but the line is triage, not a verdict: anything
                    from 0.45 up is printed in full so it can be read and judged.
  3. Self         — the same measure inside Test 26, so two items do not end up
                    describing the same scene.
  4. Rationale    — no `why` may name an option by letter, or balance_rw.py will
                    refuse to rotate it. Uses the fixed LETTER_REF pattern, which
                    requires an explicit marker or a following verb; the old
                    bare-letter version matched the ARTICLE "A".
  5. Markup       — raw notation outside a math span, paired-tag balance and
                    markdown asterisks, mirroring ../validate_tests.py so a
                    failure surfaces here rather than three commands later. Tag
                    counting requires a non-name character after the tag name so
                    that `<u` cannot match `<ul`.
  6. Writing      — every Boundaries option carries a letter or digit, and the
                    four options of a Boundaries item really do differ in their
                    punctuation rather than in their words.
"""
import json
import os
import re
import sys
from collections import Counter

from rw_test26 import QUESTIONS

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(HERE, "..", "rw_authored_corpus.json")

REJECT = 0.50
READ = 0.45

STOP = set("""a an the and or but if of to in on at by for with from as is are was were be been
being it its this that these those which who whom whose what when where how why not no than
then so such can could will would may might must shall should do does did done have has had
having one two three four five six seven eight nine ten first second more most less least many
much few some any all each every other another same own very just also only into out up down over
under about after before during while because since until through between against among within
without their they them there here he she his her him we us our you your i me my too s t""".split())
WORD = re.compile(r"[a-z]+")


def toks(s):
    s = re.sub(r"<[^>]+>", " ", s or "").lower()
    s = re.sub(r"&[a-z]+;", " ", s)
    return set(w for w in WORD.findall(s) if w not in STOP and len(w) > 2)


def jac(a, b):
    return len(a & b) / max(1, len(a | b))


IMG = re.compile(r"<img[^>]*>", re.I)
MATH_SPAN = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.S)
RAW_NOTATION = [
    ("caret exponent", re.compile(r"\^")),
    ("sqrt( )", re.compile(r"sqrt\s*\(", re.I)),
    ("asterisk as multiply", re.compile(r"(?<![\s>])\s*\*\s*(?![\s<])")),
    ("slash fraction", re.compile(r"(?<![\d/])\d+\s*/\s*\d+(?![\d/])")),
    ("ASCII !=", re.compile(r"!=")),
    ("ASCII <= or >=", re.compile(r"<=|>=")),
    ("LaTeX macro outside math",
     re.compile(r"\\(?:frac|sqrt|pi|le|ge|ne|cdot|times|div|theta|alpha|beta)(?![A-Za-z])")),
    ("spelled-out pi", re.compile(r"(?<![A-Za-z])pi(?![A-Za-z])")),
    ("spelled-out Greek",
     re.compile(r"(?<![A-Za-z])(?:theta|alpha|beta|lambda)(?![A-Za-z])", re.I)),
    ("bare trig/log call", re.compile(r"(?<![A-Za-z\\])(?:sin|cos|tan|log|ln)\s*\(")),
]
PAIRED = ("p", "u", "em", "strong", "table", "thead", "tbody", "tr", "th", "td",
          "ul", "ol", "li", "sup", "sub")

LETTER_REF = re.compile(
    r"\((?:[ABCD])\)"
    r"|\b(?:[Oo]ptions?|[Cc]hoices?|[Aa]nswers?)\s+([ABCD])\b"
    r"|(?:^|(?<=[\s(]))([ABCD])\s+(?:is|are|was|were|would|will|does|do|fails?|"
    r"states?|says?|gives?|makes?|describes?|names?|answers?|contradicts?|"
    r"reverses?|adds?|omits?|leaves?|treats?|asserts?|reads?|works?|"
    r"establishes?|supports?|overstates?|understates?|misses?)\b"
)

# The blank is a literal five-underscore run. Only the stems that promise one
# are checked: a "function of the underlined sentence" item has no blank.
NEEDS_BLANK = ("most logical and precise word or phrase",
               "most logically completes the text",
               "conventions of Standard English",
               "most logical transition")
PUNCT = set(".,;:!?&—-")


def main():
    bad = []
    print(f"== pass 1: shape  ({len(QUESTIONS)} items)")
    for q in QUESTIONS:
        n = q["num"]
        if len(q["choices"]) != 4:
            bad.append(f"{n}: {len(q['choices'])} choices")
        if len(set(c.strip() for c in q["choices"])) != 4:
            bad.append(f"{n}: duplicate choices")
        if q["answer"] not in "ABCD":
            bad.append(f"{n}: bad key {q['answer']!r}")
        if not (q.get("passage") or "").strip():
            bad.append(f"{n}: no passage")
        if not (q.get("why") or "").strip():
            bad.append(f"{n}: no rationale")
        promises = any(k in q["stem"] for k in NEEDS_BLANK)
        has = "_____" in (q.get("passage") or "")
        # Rhetorical Synthesis and the dangling-modifier item complete a
        # sentence rather than filling a gap inside one.
        if promises and not has and q["skill"] != "Rhetorical Synthesis" \
                and not (q.get("passage") or "").rstrip().endswith("_____"):
            bad.append(f"{n}: stem promises a blank, passage has none")
        if q["skill"] == "Cross-Text Connections":
            if "<strong>Text 1</strong>" not in q["passage"] or \
               "<strong>Text 2</strong>" not in q["passage"]:
                bad.append(f"{n}: cross-text item is missing one of its two texts")
        if q["skill"] == "Rhetorical Synthesis" and "<li>" not in q["passage"]:
            bad.append(f"{n}: synthesis item has no bulleted notes")
    print(f"   blocks: {dict(sorted(Counter(q['skill'] for q in QUESTIONS).items()))}")

    print("== pass 2: corpus similarity")
    rows = json.load(open(CORPUS))
    sigs = [(f"{r.get('src')}:{r.get('num')}",
             toks((r.get("passage") or "") + " " + (r.get("stem") or "")),
             r.get("passage") or "") for r in rows]
    print(f"   corpus: {len(sigs)} banked passages")
    top = []
    for q in QUESTIONS:
        s0 = toks(q["passage"] + " " + q["stem"])
        best = max(((jac(s0, s), lab, p) for lab, s, p in sigs), key=lambda t: t[0])
        top.append((best[0], q["num"], best[1], best[2]))
        if best[0] >= REJECT:
            bad.append(f"{q['num']}: corpus Jaccard {best[0]:.2f} vs {best[1]} — over the reject line")
    # The same measure over the PASSAGE alone. Reading passages are long enough
    # that the stem barely moves the score, but a writing item's passage is two
    # lines and its stem is one of four fixed sentences repeated all over the
    # bank, so passage+stem overstates the overlap of short writing items badly.
    psigs = [(f"{r.get('src')}:{r.get('num')}", toks(r.get("passage") or "")) for r in rows]
    ptop = sorted((max((jac(toks(q["passage"]), s), lab) for lab, s in psigs) + (q["num"],)
                   for q in QUESTIONS), reverse=True)
    print(f"   highest passage-only Jaccard: {ptop[0][0]:.2f}  ({ptop[0][2]} vs {ptop[0][1]})")

    top.sort(reverse=True)
    for sc, n, lab, p in top[:8]:
        flag = "  <== READ" if sc >= READ else ""
        print(f"     {sc:.2f}  {n}  vs {lab}{flag}")
        if sc >= READ:
            print("           " + re.sub(r"<[^>]+>", " ", p)[:300])
    print(f"   highest R&W Jaccard vs corpus: {top[0][0]:.2f}")

    print("== pass 3: self-collision")
    mine = [(q["num"], toks(q["passage"])) for q in QUESTIONS]
    pairs = []
    for i in range(len(mine)):
        for j in range(i + 1, len(mine)):
            pairs.append((jac(mine[i][1], mine[j][1]), mine[i][0], mine[j][0]))
    pairs.sort(reverse=True)
    for sc, a, b in pairs[:6]:
        print(f"     {sc:.2f}  {a} vs {b}")
        if sc >= REJECT:
            bad.append(f"{a}/{b}: internal Jaccard {sc:.2f}")

    print("== pass 4: rationales")
    locked = [q["num"] for q in QUESTIONS if LETTER_REF.search(q["why"])]
    print(f"   rationales naming an option by letter: {len(locked)} {locked}")
    if locked:
        bad.append(f"letter-naming rationales would lock {len(locked)} items against rebalancing")

    print("== pass 5: markup")
    for q in QUESTIONS:
        html = " ".join([q["stem"], q["passage"]] + list(q["choices"]))
        clean = MATH_SPAN.sub(" ", IMG.sub(" ", html))
        for label, pat in RAW_NOTATION:
            m = pat.search(clean)
            if m:
                bad.append(f"{q['num']}: raw {label}: …{clean[max(0,m.start()-40):m.start()+40]}…")
                break
        for tag in PAIRED:
            o = len(re.findall(rf"<{tag}(?=[\s/>])", html, re.I))
            c = len(re.findall(rf"</{tag}\s*>", html, re.I))
            if o != c:
                bad.append(f"{q['num']}: {o} <{tag}> vs {c} </{tag}>")
        if re.search(r"(?<!\*)\*(?!\*)[^*\n]{1,80}\*(?!\*)", html):
            bad.append(f"{q['num']}: markdown asterisks")
        if "<table" in q["passage"] and 'border-collapse:collapse' not in q["passage"]:
            bad.append(f"{q['num']}: table is not in the house style block")

    print("== pass 6: writing-domain options")
    for q in QUESTIONS:
        if q["skill"] not in ("Boundaries", "Form, Structure, and Sense"):
            continue
        for c in q["choices"]:
            if not re.search(r"[A-Za-z0-9]", c):
                bad.append(f"{q['num']}: option {c!r} renders as an empty row")
        if q["skill"] == "Boundaries":
            # The signal that separates Boundaries from Form/Structure/Sense is
            # that the options differ in their PUNCTUATION. It is not that they
            # differ ONLY in punctuation: a real Boundaries item routinely
            # offers ". The" against ", the" against " and the", or pairs a
            # comma with "which" against no comma with "that". An earlier
            # version of this check demanded four distinct marks and identical
            # words and reported seven findings on correct items — the same
            # family of over-matching checker bug as `<u` matching `<ul`.
            marks = set("".join(ch for ch in re.sub(r"&[a-z]+;", "—", c) if ch in PUNCT)
                        for c in q["choices"])
            if len(marks) < 2:
                bad.append(f"{q['num']}: Boundaries options do not differ in punctuation at all: {sorted(marks)}")

    print()
    if bad:
        print(f"FAIL — {len(bad)} finding(s):")
        for b in bad:
            print("  " + b)
        return 1
    print(f"ALL CHECKS PASSED — {len(QUESTIONS)} items, "
          f"highest corpus Jaccard {top[0][0]:.2f}, highest internal {pairs[0][0]:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
