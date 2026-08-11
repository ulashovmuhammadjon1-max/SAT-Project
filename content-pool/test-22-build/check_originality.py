#!/usr/bin/env python3
"""Throwaway originality screen for Test 22 R&W.

Two independent checks against content-pool/rw_authored_corpus.json (1,295 passages):

  keywords  - report any corpus passage containing a candidate topic keyword,
              matched on whole words only (a substring match once had "quire"
              hit *required* and "loom" hit *bloom*)
  ngrams    - shared 5-grams and Jaccard over content-word token sets, so a
              differently-worded passage on the same subject is still caught

Usage:
    python3 check_originality.py keywords          # screen TOPICS below
    python3 check_originality.py ngrams            # screen finished rw_test22
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

# Candidate topics for Test 22, drawn from the fifteen assigned territories.
TOPICS = [
    # bee biology and colony behaviour
    "queen pheromone mandibular colony", "drone congregation area mating flight",
    "swarm quorum scout nest site decision", "winter cluster thermoregulation shivering",
    "royal jelly caste queen larva", "bee bread pollen lactic fermentation",
    "hygienic behaviour uncapping diseased brood", "orientation flight landmark hive return",
    "robbing colony defence guard bee", "laying worker drone brood queenless",
    "nosema gut parasite spore bee", "wax gland scale festoon comb building",
    "cell size worker drone comb", "foulbrood spore inspector destruction",
    "stingless bee meliponine pot honey", "bumblebee colony annual queen hibernate",
    # honey chemistry, extraction and provenance
    "invertase sucrose inversion honey enzyme", "glucose oxidase hydrogen peroxide honey",
    "granulation crystal seeding set honey", "thixotropic heather honey press",
    "honeydew aphid forest honey", "melissopalynology pollen grain provenance honey",
    "radial extractor centrifuge frame honey", "hydroxymethylfurfural heating marker honey",
    "diastase number freshness honey", "mead fermentation honey yeast",
    "honey wound dressing antibacterial osmotic",
    # apiary history and management
    "bee space movable frame Langstroth hive", "queen excluder brood super",
    "migratory beekeeping lorry orchard pollination contract", "bee bole wall niche skep shelter",
    "observation hive glass teaching", "hive scale telemetry nectar flow record",
    # sugar refining
    "bone char decolourising sugar filter", "vacuum pan massecuite crystal sugar",
    "centrifugal curing molasses separation", "molasses exhaustion recovery sugar",
    "raffinose beet molasses crystallisation", "carbonatation lime carbon dioxide juice",
    "polarimeter optical rotation sugar assay", "sugar loaf cone nippers grocer",
    "carbon isotope cane beet adulteration", "Brix hydrometer syrup density",
    # beet processing
    "diffusion battery cossette beet juice", "beet pulp fodder cattle",
    "soil tare weighbridge beet delivery", "Marggraf Achard beet sugar origin",
    "Continental blockade beet industry Napoleon", "multigerm beet seed cluster singling",
    "bolting vernalisation beet flowering",
    # confectionery boiling
    "hard crack soft ball boiling stage sugar", "invert sugar graining doctoring confectionery",
    "fondant crystal size mouthfeel", "sugar thermometer boiling point elevation",
    "pulled sugar aeration satin", "isomalt sugar sculpture",
    "humectant shelf life sweet", "pectin gelatine set jelly sweet",
    "caramelisation Maillard browning sugar", "supersaturation nucleation crystal growth",
    "rock candy string crystal", "barley sugar twist boiled sweet",
    # beeswax, tallow and candles
    "beeswax melting point bloom polish", "dipping moulding candle chandler",
    "plaited wick self consuming candle", "spermaceti standard candle candela photometry",
    "tallow rush light dip", "encaustic painting wax pigment",
    "lost wax investment casting", "wax seal impression matrix document",
    "candle flame structure luminous soot Faraday", "paraffin stearin candle nineteenth century",
    "cuticular wax leaf water repellent", "comb foundation embossed sheet wire",
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
    # Whole-word token sets, so matching never runs on substrings.
    rows = [(c, set(tokens(c["passage"]) + tokens(c.get("stem", "")))) for c in corpus]
    hits = 0
    for topic in TOPICS:
        keys = tokens(topic)
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
    from rw_test22 import QUESTIONS
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
        if len(set(q["choices"])) != 4:
            print("DUPLICATE CHOICE", q["num"]); bad += 1
        if q["answer"] not in "ABCD":
            print("BAD ANSWER", q["num"]); bad += 1
        for c in q["choices"]:
            if not _re.search(r"[A-Za-z0-9]", c):
                print("WORDLESS CHOICE", q["num"], repr(c)); bad += 1
        p = q["passage"]
        if p.count("<table") != p.count("</table>") or p.count("<td") != p.count("</td>") \
           or p.count("<tr") != p.count("</tr>") or p.count("<th ") != p.count("</th>"):
            print("TABLE MARKUP", q["num"]); bad += 1
    print(f"structural problems: {bad}")
    print(Counter(q["skill"] for q in QUESTIONS))


def cmd_near(n=12):
    """Print the nearest corpus matches for each of my passages, to read by eye."""
    from rw_test22 import QUESTIONS
    corpus = load_corpus()
    ctoks = [(c, set(tokens(c["passage"]))) for c in corpus]
    scored = []
    for q in QUESTIONS:
        qs = set(tokens(q["passage"]))
        best = max(ctoks, key=lambda cc: jaccard(qs, cc[1]))
        scored.append((jaccard(qs, best[1]), q["num"], f"{best[0]['src']}:{best[0]['num']}",
                       best[0]["passage"][:220]))
    scored.sort(reverse=True)
    for j, num, ref, txt in scored[:n]:
        print(f"{j:.3f}  {num} ~ {ref}\n        {txt}\n")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "near":
        cmd_near(int(sys.argv[2]) if len(sys.argv) > 2 else 12)
    else:
        {"keywords": cmd_keywords, "ngrams": cmd_ngrams}[cmd]()
