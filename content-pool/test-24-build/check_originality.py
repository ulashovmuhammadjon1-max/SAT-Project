#!/usr/bin/env python3
"""Throwaway originality screen for Test 24 R&W.

Two independent checks against content-pool/rw_authored_corpus.json (1,295 passages):

  keywords  - report any corpus passage containing a candidate topic keyword
  ngrams    - shared 5-grams and Jaccard over content-word token sets, so a
              differently-worded passage on the same subject is still caught

Usage:
    python3 check_originality.py keywords          # screen TOPICS below
    python3 check_originality.py ngrams            # screen finished rw_test24
"""
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(HERE, "..", "rw_authored_corpus.json")

STOP = set("""a an the and or but of in on at to for with from by as is are was were be been being
it its it's this that these those which who whom whose what when where while how not no nor so
than then there here their they them he she his her him you your we our us i me my one two three
than into over under about between during after before again more most much many few some any all
each both other another such own same very can will just don should now has have had do does did
having doing up down out off above below only also because if while although though however
thus therefore per cent percent year years first second new old made make makes making use used
uses using take takes taken took give gives given gave get got put set well back even still
""".split())

# Candidate topics for Test 24, drawn from the assigned territories.
TOPICS = [
    # ropewalks, cordage and fibre
    "ropewalk cordage rope laying", "hemp retting hackling fibre",
    "twine spinning hank", "fibre bundle load sharing tensile",
    # sailmaking and canvas
    "sailcloth panel seam broadseam", "sail loft floor lofting",
    "tarpaulin dressing waterproof canvas",
    # wire rope, netting, hoisting
    "wire rope cable spinning suspension bridge", "safety net mesh arresting fall",
    "hoist governor safety brake guide rail",
    # knots and their mathematics
    "knot invariant crossing diagram", "splice eye tuck strand",
    # other territories
    "bookbinding sewn gathering cord board", "eyewitness confidence lineup feedback",
    "mycorrhizal fungus phosphorus seedling network", "braille cell contraction tactile reading",
    "lava tube crust insulated flow basalt", "antibiotic resistance plasmid fitness cost",
    "machine translation parallel corpus alignment", "cave art charcoal ochre radiocarbon dating",
]


def tokens(text):
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = re.sub(r"&[a-z]+;", " ", text)
    words = re.findall(r"[a-z']+", text.lower())
    return [w for w in words if w not in STOP and len(w) > 2]


def load_corpus():
    with open(CORPUS) as fh:
        return json.load(fh)


def five_grams(toks):
    return set(tuple(toks[i:i + 5]) for i in range(len(toks) - 4))


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def cmd_keywords():
    corpus = load_corpus()
    rows = [(c, set(tokens(c["passage"]))) for c in corpus]
    hits = 0
    for topic in TOPICS:
        keys = [k for k in tokens(topic)]
        best = []
        for c, ts in rows:
            overlap = [k for k in keys if k in ts]
            if len(overlap) >= 2 or (len(keys) == 1 and overlap):
                best.append((len(overlap), c["src"], c["num"], overlap))
        if best:
            best.sort(reverse=True)
            hits += 1
            print(f"COLLISION  {topic!r}")
            for n, src, num, ov in best[:3]:
                print(f"           {src}:{num}  shares {ov}")
    print(f"\n{len(TOPICS)} topics screened, {hits} collided")


def cmd_ngrams():
    from rw_test24 import QUESTIONS
    corpus = load_corpus()
    ctoks = [(c, tokens(c["passage"]), five_grams(tokens(c["passage"]))) for c in corpus]

    worst_corpus = (0.0, None, None)
    worst_self = (0.0, None, None)
    flagged = []

    mine = [(q, tokens(q["passage"]), five_grams(tokens(q["passage"]))) for q in QUESTIONS]

    for q, qt, qg in mine:
        qs = set(qt)
        for c, ct, cg in ctoks:
            j = jaccard(qs, set(ct))
            shared = len(qg & cg)
            if j > worst_corpus[0]:
                worst_corpus = (j, q["num"], f"{c['src']}:{c['num']}")
            if j >= 0.5 or shared >= 3:
                flagged.append(("CORPUS", q["num"], f"{c['src']}:{c['num']}", round(j, 3), shared))

    for i, (q, qt, qg) in enumerate(mine):
        for q2, q2t, q2g in mine[i + 1:]:
            j = jaccard(set(qt), set(q2t))
            shared = len(qg & q2g)
            if j > worst_self[0]:
                worst_self = (j, q["num"], q2["num"])
            if j >= 0.5 or shared >= 3:
                flagged.append(("SELF", q["num"], q2["num"], round(j, 3), shared))

    for f in flagged:
        print("FLAG", f)
    print(f"\nhighest Jaccard vs corpus: {worst_corpus[0]:.3f}  ({worst_corpus[1]} ~ {worst_corpus[2]})")
    print(f"highest Jaccard among own:  {worst_self[0]:.3f}  ({worst_self[1]} ~ {worst_self[2]})")
    print(f"flagged (>=0.5 Jaccard or >=3 shared 5-grams): {len(flagged)}")

    # structural checks
    import re as _re
    from balance_rw import LETTER_REF
    bad = 0
    for q in QUESTIONS:
        if not q.get("why", "").strip():
            print("NO WHY", q["num"]); bad += 1
        if LETTER_REF.search(q.get("why", "")):
            print("LETTER-NAMING WHY", q["num"], q["why"][:90]); bad += 1
        if len(q["choices"]) != 4:
            print("CHOICE COUNT", q["num"]); bad += 1
        if q["answer"] not in "ABCD":
            print("BAD ANSWER", q["num"]); bad += 1
        for c in q["choices"]:
            if not _re.search(r"[A-Za-z0-9]", c):
                print("WORDLESS CHOICE", q["num"], repr(c)); bad += 1
    print(f"structural problems: {bad}")
    print(Counter(q["skill"] for q in QUESTIONS))


if __name__ == "__main__":
    {"keywords": cmd_keywords, "ngrams": cmd_ngrams}[sys.argv[1]]()
