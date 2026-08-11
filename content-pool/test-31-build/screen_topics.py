#!/usr/bin/env python3
"""
Originality screen for the Test 31 Reading & Writing draft.

Two passes, because either one alone lets a collision through:

  * keyword — word-boundary matching on a topic's distinctive terms. Substring
    matching is useless here: an earlier run had "quire" fire on *required* and
    "loom" fire on *bloom*, so every term is matched with \\b...\\b.
  * n-gram / Jaccard — shared 5-grams and Jaccard overlap over content-word
    token sets, which catches a passage that covers the same ground in
    different words.

Usage:
    python3 screen_topics.py topics     # screen the planned topic list
    python3 screen_topics.py passages   # screen the finished rw_test31.py
"""
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(HERE, "..", "rw_authored_corpus.json")

STOP = set("""a an the and or but if while of in on at to for from by with as is are was were
be been being it its this that these those there their they them he she his her which who whom
whose what when where how than then so such not no nor only also very can could would should
may might must will shall do does did done have has had having into over under about after
before between through during above below up down out off again further once each other more
most some any all both few many much own same too s t just now one two three four five ten
per cent because since although though even still yet upon within without across along around
called known often usually always never sometimes rather instead whether either neither"""
           .split())


# Boilerplate shared by every item of a block. Left in, it dominates the n-gram
# count: every pair of Rhetorical Synthesis passages "shares" the six 5-grams of
# the notes preamble, and every pair of writing items shares the stem. Stripped,
# a shared 5-gram means shared content.
BOILER = re.compile(
    r"While researching a topic, a student has taken the following notes:?", re.I)


def tokens(text):
    text = BOILER.sub(" ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"&[a-z]+;", " ", text)
    return [w for w in re.findall(r"[a-z]+", text.lower()) if w not in STOP and len(w) > 2]


def ngrams(toks, n=5):
    return set(tuple(toks[i:i + n]) for i in range(len(toks) - n + 1))


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def load_corpus():
    with open(CORPUS) as fh:
        rows = json.load(fh)
    for r in rows:
        r["_tok"] = tokens(r.get("passage", ""))
        r["_set"] = set(r["_tok"])
        r["_5g"] = ngrams(r["_tok"])
    return rows


# ---------------------------------------------------------------- keyword pass
def keyword_hits(corpus, terms):
    pats = {t: re.compile(r"\b" + re.escape(t).replace(r"\ ", r"\s+") + r"\b", re.I)
            for t in terms}
    hits = Counter()
    where = {}
    for r in corpus:
        plain = re.sub(r"<[^>]+>", " ", r.get("passage", "") + " " + r.get("stem", ""))
        for t, p in pats.items():
            if p.search(plain):
                hits[t] += 1
                where.setdefault(t, []).append(f"{r['src']}:{r['num']}")
    return hits, where


TOPIC_TERMS = [
    # poultry, eggs and egg grading
    "poultry", "pullet", "hen", "cockerel", "junglefowl", "broody", "clutch",
    "incubation", "candling", "eggshell", "albumen", "yolk", "chalaza",
    "air cell", "bloom", "cuticle", "haugh unit", "egg grading", "battery",
    "free range", "comb", "wattles", "moult", "photoperiod", "laying flock",
    "brood patch", "precocial", "altricial", "imprinting", "down feather",
    "eiderdown", "quill", "keratin", "barbule", "preen", "uropygial",
    # dovecotes and pigeons
    "dovecote", "columbarium", "pigeon", "squab", "nest hole", "potence",
    "homing pigeon", "pigeon post", "pigeon racing", "carrier pigeon",
    "guano", "saltpetre", "rock dove", "crop milk", "loft",
    # falconry and the mews
    "falconry", "falcon", "peregrine", "goshawk", "sparrowhawk", "austringer",
    "mews", "jess", "creance", "lure", "hood", "bating", "imping", "cadge",
    "eyas", "haggard", "manning", "stoop", "quarry", "bell",
    # decoy ponds and wildfowling
    "decoy pond", "decoy", "pipe", "wildfowl", "wildfowling", "punt gun",
    "teal", "wigeon", "mallard", "pintail", "flyway", "ringing", "geolocator",
    "swan upping", "goose fair", "hide", "flighting", "saltings",
    # eel traps and fish ponds
    "eel", "elver", "eel buck", "eel trap", "fyke", "glass eel", "silver eel",
    "stew pond", "vivarium", "carp", "tench", "bream", "pike", "fish weir",
    "kiddle", "monastic fishpond", "puddled clay", "sluice", "fish pass",
    "stripping", "spawn", "fry", "leptocephalus", "sargasso",
]


def screen_topics():
    corpus = load_corpus()
    hits, where = keyword_hits(corpus, TOPIC_TERMS)
    print(f"corpus: {len(corpus)} passages\n")
    print("TERMS WITH HITS (topic likely already covered — read the matches):")
    for t, n in sorted(hits.items(), key=lambda kv: -kv[1]):
        print(f"  {t:<22} {n:>3}   {', '.join(where[t][:8])}")
    clean = [t for t in TOPIC_TERMS if t not in hits]
    print(f"\nTERMS WITH NO HIT ({len(clean)}):")
    print("  " + ", ".join(clean))


# --------------------------------------------------------------- passage pass
def screen_passages():
    corpus = load_corpus()
    sys.path.insert(0, HERE)
    from rw_test31 import QUESTIONS

    mine = []
    for q in QUESTIONS:
        t = tokens(q.get("passage", ""))
        mine.append(dict(num=q["num"], skill=q["skill"], tok=t,
                         set=set(t), g5=ngrams(t)))

    print(f"{len(mine)} authored passages vs {len(corpus)} corpus passages\n")
    worst = []
    for m in mine:
        best = max(corpus, key=lambda r: jaccard(m["set"], r["_set"]))
        j = jaccard(m["set"], best["_set"])
        shared = len(m["g5"] & best["_5g"])
        worst.append((j, shared, m["num"], f"{best['src']}:{best['num']}", best["skill"]))
    worst.sort(reverse=True)
    print("TOP 15 vs CORPUS  (jaccard, shared 5-grams, mine, nearest)")
    for j, g, num, ref, sk in worst[:15]:
        flag = "  <-- REWRITE" if j >= 0.5 or g > 0 else ""
        print(f"  {j:.3f}  {g:>2}  {num:<5} {ref:<22} {sk}{flag}")

    print("\nTOP 15 SELF-PAIRS  (jaccard, shared 5-grams)")
    pairs = []
    for i in range(len(mine)):
        for k in range(i + 1, len(mine)):
            j = jaccard(mine[i]["set"], mine[k]["set"])
            pairs.append((j, len(mine[i]["g5"] & mine[k]["g5"]),
                          mine[i]["num"], mine[k]["num"]))
    pairs.sort(reverse=True)
    for j, g, a, b in pairs[:15]:
        flag = "  <-- REWRITE" if j >= 0.5 or g > 0 else ""
        print(f"  {j:.3f}  {g:>2}  {a:<5} {b}{flag}")

    mx = worst[0][0]
    mxs = pairs[0][0]
    print(f"\nhighest jaccard vs corpus: {mx:.3f}   highest self-pair: {mxs:.3f}")
    ng = sum(1 for j, g, *_ in worst if g > 0) + sum(1 for j, g, *_ in pairs if g > 0)
    print(f"pairs sharing any 5-gram: {ng}")


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "topics"
    (screen_topics if what == "topics" else screen_passages)()
