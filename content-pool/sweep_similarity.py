#!/usr/bin/env python3
"""
Similarity sweep across newly built tests — against each other and against the
whole bank.

Each build agent dedupes its own test. This runs afterwards over all of them at
once, which is the only way to catch two siblings independently writing the same
question: three agents handed the same reference template once produced
`f(x)=x²−4x` with `g(x)=3x+2` between them.

## Two signals, because plain Jaccard demonstrably misses the important case

`word` — Jaccard over content words. This is what previous builds used. Its
documented weakness is severe: across Tests 18-21, 57 Math questions were
rewritten as genuine template repeats and all but three scored BELOW the 0.75
reject line. A repeat that keeps the mathematics but changes the setting words
scores *low precisely because it changed the words*.

`shape` — Jaccard over the same text with every number replaced by `#` and the
setting nouns stripped to their skeleton. A template repeat with new numbers
scores HIGH here even when `word` scores low, which is exactly the blind spot.
The two together are far more informative than either alone.

Neither number is a verdict. Read every pair either signal ranks highly.

    python3 sweep_similarity.py 22 23 24 25 26 27 28 29 30 31
"""
import json
import os
import re
import sys
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))

MATH_MODULES = ("MATH_M1", "MATH_M2E", "MATH_M2H")
RW_MODULES = ("RW_M1", "RW_M2E", "RW_M2H")

# Reject outright at these; read everything above REVIEW.
MATH_REJECT, RW_REJECT, REVIEW = 0.75, 0.50, 0.45

TAG = re.compile(r"<[^>]+>")
WORD = re.compile(r"[a-z]+")

STOP = {
    "the", "a", "an", "of", "and", "or", "to", "in", "is", "are", "was", "were", "be", "been",
    "for", "on", "at", "by", "with", "as", "that", "this", "these", "those", "it", "its",
    "from", "which", "what", "how", "many", "much", "if", "then", "than", "each", "per",
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "value", "values", "following", "shown", "given", "must", "will", "would", "can",
    "there", "their", "they", "he", "she", "his", "her", "not", "no", "all", "any", "some",
}

# The words a template is built out of: quantities, comparisons, relations,
# question forms and arithmetic. Everything NOT in here is scenery and gets
# collapsed, so two questions with the same machinery and different settings
# still match.
SKELETON = STOP | {
    "more", "less", "fewer", "greater", "least", "most", "total", "sum", "difference",
    "product", "quotient", "twice", "half", "double", "triple", "times", "each", "every",
    "per", "rate", "ratio", "percent", "percentage", "average", "mean", "median", "mode",
    "increase", "increased", "decrease", "decreased", "remaining", "remains", "left",
    "together", "combined", "altogether", "apiece", "equal", "equals", "same", "different",
    "first", "second", "next", "last", "before", "after", "when", "while", "until",
    "how", "what", "why", "where", "who", "whose", "whom",
    "function", "equation", "system", "graph", "line", "slope", "intercept", "vertex",
    "solution", "solutions", "solve", "expression", "equivalent", "defined", "represents",
    "possible", "greatest", "smallest", "minimum", "maximum", "positive", "negative",
    "integer", "integers", "number", "numbers", "constant", "variable",
    "began", "begins", "started", "starts", "began", "gave", "gives", "given", "took",
    "takes", "holds", "held", "costs", "cost", "sold", "sells", "buys", "bought",
    "week", "weeks", "day", "days", "hour", "hours", "minute", "minutes", "year", "years",
}


def strip_html(s: str) -> str:
    return TAG.sub(" ", s or "")


# Mathematical tokens: LaTeX macros, single-letter variables, and operators.
# Numbers collapse to `#` so a template repeat with fresh numbers still matches.
MATH_TOKEN = re.compile(r"\\[A-Za-z]+|\d[\d,\.]*|[a-z](?![a-z])|[\^=+\-*/<>()]")

# Operators so common they carry almost no information — the stopwords of
# mathematics. Two unrelated one-line stems both contain "=", "(", ")" and a
# number, which alone was enough to push a pair of short stems to 0.78.
MATH_STOP = {"#", "=", "+", "-", "*", "/", "(", ")", "<", ">"}


def word_sig(text: str) -> frozenset:
    """Content words PLUS the mathematics.

    Words alone are not enough for a Math stem. `[a-z]{3,}` discards every
    digit, operator and exponent, so two questions whose only shared text is
    the boilerplate wrapper — "the expression … is equivalent to … where c is
    a constant. What is the value of c?" — scored a perfect 1.00 against each
    other while one was difference-of-squares factoring and the other was
    exponent rules. That is not near-duplication, it is the same sentence
    around completely different mathematics.

    Including LaTeX macros, variables and operators makes the signature
    actually about the question. Numbers are masked, so changing only the
    numbers still counts as a repeat.
    """
    plain = strip_html(text).lower()
    words = {w for w in WORD.findall(plain) if len(w) > 2 and w not in STOP}
    maths = {("#" if t[0].isdigit() else t) for t in MATH_TOKEN.findall(plain)}
    maths -= MATH_STOP
    return frozenset(words | {f"m:{t}" for t in maths})


def shape_sig(text: str) -> frozenset:
    """Structural skeleton of the question.

    The inverse of `word_sig`, and the inversion is the whole point. Content
    nouns are what a template repeat *changes* — casks become vine rows — so
    they are collapsed to a single placeholder. The function words are what it
    *keeps*: "3 more X than Y and 47 in all … each … how many … ?" is the
    template, and that phrasing survives any change of setting.

    An earlier version of this stripped the function words and kept the nouns,
    which scored a known template repeat at 0.02 against 0.13 for plain word
    overlap — worse than the signal it was meant to improve on. Keep the
    skeleton, drop the scenery.
    """
    s = strip_html(text).lower()
    s = re.sub(r"\d[\d,\.]*", " # ", s)
    toks = ["#" if t == "#" else (t if t in SKELETON else "_")
            for t in re.findall(r"#|[a-z]+", s)]
    return frozenset(zip(toks, toks[1:], toks[2:])) or frozenset(toks)


def jaccard(a: frozenset, b: frozenset) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


# Below this many skeleton trigrams a stem is too short for `shape` to mean
# anything: it collapses to mostly placeholders, and any two one-step word
# problems then look alike. Measured, not guessed — at 16 and 13 trigrams,
# "45 grams onto each of 16 skeins" (a multiplication) scored 0.71 against
# "4.5 litres equally into 6 moulds" (a division). Same genre, different
# mathematics, and not a repeat.
SHAPE_MIN_TRIGRAMS = 22


def shape_is_meaningful(a: frozenset, b: frozenset) -> bool:
    return len(a) >= SHAPE_MIN_TRIGRAMS and len(b) >= SHAPE_MIN_TRIGRAMS


# A one-line stem yields so few tokens that Jaccard is dominated by whichever
# handful they happen to share. Below this, a high score is reported for
# reading but never treated as an automatic reject — the same rule `shape`
# already follows, applied consistently.
WORD_MIN_TOKENS = 14


def word_is_conclusive(a: frozenset, b: frozenset) -> bool:
    return len(a) >= WORD_MIN_TOKENS and len(b) >= WORD_MIN_TOKENS


def load_items(nums):
    """(label, text, kind) for every Math stem and R&W passage in the new tests."""
    math, rw = [], []
    for n in nums:
        path = os.path.join(HERE, f"test-{n}-build", f"test{n}.json")
        if not os.path.exists(path):
            print(f"  (Test {n}: no assembled JSON yet — skipped)")
            continue
        t = json.load(open(path))
        for key in MATH_MODULES:
            for i, q in enumerate(t.get(key, []), 1):
                math.append((f"T{n} {key} Q{i}", q.get("stem", ""), n))
        seen = set()
        for key in RW_MODULES:
            for i, q in enumerate(t.get(key, []), 1):
                p = (q.get("passage") or "").strip()
                if p and p not in seen:
                    seen.add(p)
                    rw.append((f"T{n} {key} Q{i}", p, n))
    return math, rw


def report(pairs, reject, title, limit=25):
    """Prints the worst matches. Returns the count at or above the reject line."""
    pairs.sort(key=lambda r: -max(r[0], r[1]))
    over = [p for p in pairs if max(p[0], p[1]) >= reject and p[4]]
    print(f"\n{title}")
    print(f"  reject at {reject:.2f}; read everything at or above {REVIEW:.2f}")
    shown = [p for p in pairs if max(p[0], p[1]) >= REVIEW][:limit]
    if not shown:
        best = max((max(p[0], p[1]) for p in pairs), default=0.0)
        print(f"  nothing at or above {REVIEW:.2f}. Highest pair scored {best:.2f}.")
    else:
        for w, sh, a, b, ok in shown:
            flag = "REJECT" if max(w, sh) >= reject else "read  "
            note = "" if ok else "  (stem too short to judge — read it)"
            print(f"  {flag} word {w:.2f} shape {sh:.2f}  {a}  vs  {b}{note}")
    return len(over)


def main():
    nums = [int(a) for a in sys.argv[1:] if a.isdigit()] or list(range(22, 32))
    print(f"Sweeping tests: {', '.join(str(n) for n in nums)}")

    math, rw = load_items(nums)
    if not math and not rw:
        print("Nothing to sweep yet.")
        return 0
    print(f"{len(math)} Math stems, {len(rw)} R&W passages from the new tests.")

    m_word = {lab: word_sig(txt) for lab, txt, _ in math}
    m_shape = {lab: shape_sig(txt) for lab, txt, _ in math}
    r_word = {lab: word_sig(txt) for lab, txt, _ in rw}

    failures = 0

    # --- new tests against each other -----------------------------------
    cross = []
    for (la, _, na), (lb, _, nb) in combinations(math, 2):
        if na == nb:
            continue  # each agent already checked itself
        ok = shape_is_meaningful(m_shape[la], m_shape[lb])
        conclusive = word_is_conclusive(m_word[la], m_word[lb]) and ok
        cross.append((jaccard(m_word[la], m_word[lb]),
                      jaccard(m_shape[la], m_shape[lb]) if ok else 0.0, la, lb, conclusive))
    failures += report(cross, MATH_REJECT, "MATH — new tests against each other")

    cross_rw = []
    for (la, _, na), (lb, _, nb) in combinations(rw, 2):
        if na == nb:
            continue
        cross_rw.append((jaccard(r_word[la], r_word[lb]), 0.0, la, lb, True))
    failures += report(cross_rw, RW_REJECT, "R&W PASSAGES — new tests against each other")

    # --- new tests against the banked corpus ----------------------------
    bank = json.load(open(os.path.join(HERE, "prod_math_stems.json")))
    b_word = [(b["label"], word_sig(b["stem"])) for b in bank]
    b_shape = [(b["label"], shape_sig(b["stem"])) for b in bank]
    vs_bank = []
    for lab, _, n in math:
        # A test already published is in the bank, so it would match itself at
        # 1.00. Skip its own entries rather than reporting a fake collision.
        own = f"Test {n} "
        best = (0.0, 0.0, None, True)
        for (bl, bw), (_, bs) in zip(b_word, b_shape):
            if bl.startswith(own):
                continue
            ok = shape_is_meaningful(m_shape[lab], bs)
            w = jaccard(m_word[lab], bw)
            sh = jaccard(m_shape[lab], bs) if ok else 0.0
            if max(w, sh) > max(best[0], best[1]):
                best = (w, sh, bl, word_is_conclusive(m_word[lab], bw) or ok)
        vs_bank.append((best[0], best[1], lab, f"bank: {best[2]}", best[3]))
    failures += report(vs_bank, MATH_REJECT, f"MATH — new tests against {len(bank)} banked stems")

    corpus = json.load(open(os.path.join(HERE, "rw_authored_corpus.json")))
    c_word = [(f"{c['src']} {c.get('num','')}", word_sig(c["passage"])) for c in corpus]
    vs_corpus = []
    for lab, _, _ in rw:
        best = (0.0, None)
        for cl, cw in c_word:
            w = jaccard(r_word[lab], cw)
            if w > best[0]:
                best = (w, cl)
        vs_corpus.append((best[0], 0.0, lab, f"corpus: {best[1]}", True))
    failures += report(vs_corpus, RW_REJECT, f"R&W — new tests against {len(corpus)} banked passages")

    print()
    if failures:
        print(f"FAIL — {failures} pair(s) at or above the reject line.")
        return 1
    print("PASS — nothing at or above the reject lines.")
    print("Matches printed above are for reading, not automatic rejection: a template")
    print("repeat that changed its setting words scores LOW on `word` and HIGH on `shape`.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
