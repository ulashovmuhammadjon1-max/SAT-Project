# -*- coding: utf-8 -*-
"""Similarity signatures for Math questions.

Shared by the band survey and the allocator so both score identically.

A Math question's *setting* words (bakery, cyclist, reservoir) are what a
template repeat changes while keeping the mathematics — so a signature built
from words alone scores a genuine repeat LOW, which is the failure CLAUDE.md
records across Tests 18-21. The numbers and the operator shape are what stay
constant, so both are kept as their own channel and scored separately.
"""
import re

TAG = re.compile(r"<[^>]+>")
IMG = re.compile(r"<img[^>]*>", re.I)
WORD = re.compile(r"[a-z]{3,}")
NUM = re.compile(r"(?<![\w.])\d+(?:\.\d+)?")
# Structural tokens: the operators and function names that describe the shape
# of the mathematics rather than its dressing.
OPS = re.compile(r"\\frac|\\sqrt|\\pi|\\sin|\\cos|\\tan|\\log|\\ln|\^|<=|>=|\\le|\\ge|\\ne|[=+*/<>]")

STOP = {
    "the", "and", "for", "are", "was", "were", "which", "that", "this", "with",
    "from", "has", "have", "had", "not", "but", "its", "his", "her", "their",
    "what", "when", "where", "who", "whom", "how", "why", "can", "could",
    "would", "should", "will", "shall", "may", "might", "must", "does", "did",
    "following", "value", "values", "given", "shown", "above", "below",
    "question", "answer", "choice", "choices", "most", "nearly", "equal",
    "equals", "equivalent", "expression", "function", "equation", "system",
    "graph", "table", "figure", "line", "point", "points",
}


def strip(html):
    return TAG.sub(" ", IMG.sub(" ", html or ""))


def distinctive(tok):
    """Keep only constants that could identify a question.

    Every SAT question is full of 1, 2, 3, 4 — sharing them means nothing, and
    counting them made unrelated pairs score 0.67 on the numeric channel alone
    during the band survey. A multi-digit value or a decimal is the kind of
    constant a template repeat actually carries over.
    """
    return len(tok) > 1 and tok not in {"10", "12", "20", "100"}


ENT = re.compile(r"&[a-z]+;|&#\d+;")
TOKEN = re.compile(r"[a-z]+|\d+(?:\.\d+)?")


def shingles(text, k=4):
    """Overlapping k-grams of the normalised token stream.

    This replaces a bag-of-words Jaccard, which was unusable here: SAT Math
    stems are short and heavily boilerplated, so after stopword removal two
    completely different questions can share their entire remaining vocabulary
    and score 1.00 — "If 6/7 p + 12 = 54, what is 7p?" against
    "If (x-16)/27 = (x-16)/9, what is x+16?" did exactly that. k-grams keep
    word ORDER, so shared boilerplate contributes only the boilerplate's own
    grams and cannot swamp a short stem.
    """
    toks = TOKEN.findall(text)
    if len(toks) < k:
        return {" ".join(toks)} if toks else set()
    return {" ".join(toks[i:i + k]) for i in range(len(toks) - k + 1)}


def sig(q):
    """Setting words, distinctive constants, operator shape, and text grams."""
    text = strip(q.get("stem", ""))
    for c in q.get("choices") or []:
        text += " " + strip(c.get("content", ""))
    low = ENT.sub(" ", text.lower())
    words = {w for w in WORD.findall(low) if w not in STOP}
    nums = {t for t in NUM.findall(low) if distinctive(t)}
    ops = tuple(sorted(OPS.findall(q.get("stem", "") or "")))
    return words, nums, ops, shingles(low)


def jac(a, b):
    if not a and not b:
        return 0.0
    return len(a & b) / max(len(a | b), 1)


def score(sa, sb):
    """Two independent ways of being the same question, taken as a maximum.

    A template repeat can preserve the WORDING and change the numbers ("a
    triangle with base 48" -> "base 82"), or preserve the NUMBERS and change
    the setting ("bakery" -> "cannery", same 2x^2-12x+23). Shingles catch the
    first, distinctive constants catch the second. Averaging the channels
    buries whichever one fired, which is how a 0.42-scoring mixture problem
    shipped twice on Test 21 — so take the max.
    """
    wa, na, oa, ga = sa
    wb, nb, ob, gb = sb
    g = jac(ga, gb)
    n = jac(na, nb)
    # Two questions sharing a couple of distinctive constants is coincidence —
    # a frequency table of 11/18/25/32 scored 0.43 against an unrelated system
    # of equations on shared 4s and 11s. Trust the numeric channel only with
    # four shared constants AND some textual overlap to corroborate it.
    n_trust = n if len(na & nb) >= 4 and g >= 0.10 else 0.0
    return max(g, n_trust), g, n, jac(wa, wb)
