#!/usr/bin/env python3
"""Throwaway originality screen for Test 21 R&W.

Two independent checks against content-pool/rw_authored_corpus.json (1,052 passages):

  keywords  - report any corpus passage containing a candidate topic keyword,
              matched on whole words only (a substring match once had "quire"
              hit *required* and "loom" hit *bloom*)
  ngrams    - shared 5-grams and Jaccard over content-word token sets, so a
              differently-worded passage on the same subject is still caught

Usage:
    python3 check_originality.py keywords          # screen TOPICS below
    python3 check_originality.py ngrams            # screen finished rw_test21
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

# Candidate topics for Test 21, drawn from the fifteen assigned territories.
TOPICS = [
    # viticulture and wine chemistry
    "phylloxera rootstock grafting vine", "terroir soil vineyard", "malolactic fermentation wine",
    "cork taint trichloroanisole", "tannin skin maceration red wine", "botrytis noble rot sweet wine",
    "sulphur dioxide preservative wine", "champagne secondary fermentation bottle",
    "grape ripening sugar acid harvest", "oak barrel toasting wine", "ice wine frozen grape",
    "vine training trellis canopy",
    # silk and sericulture
    "silkworm Bombyx mulberry leaf", "cocoon reeling filament silk", "sericin degumming silk",
    "silk road trade caravan", "silk moth flightless domestication", "wild tussah silk",
    "silk throwing mill organzine", "pebrine disease Pasteur silkworm",
    # wheelwrighting, carriages, road vehicles
    "wheelwright felloe spoke hub", "iron tyre shrinking wheel", "dish of a cart wheel",
    "elliptical leaf spring carriage", "turnpike road macadam surface", "stagecoach team horses",
    "hansom cab", "axle bearing grease cart", "wagon brake shoe descent",
    # observatories, telescopes, instrument making
    "equatorial mount telescope drive", "achromatic lens doublet objective",
    "speculum metal mirror reflector", "observatory dome slit rotating", "meridian circle transit instrument",
    "silvering glass mirror telescope", "seeing atmospheric turbulence site", "objective lens flint crown glass",
    "photographic plate astronomy survey", "clock drive sidereal telescope",
    # photography and imaging chemistry
    "silver halide emulsion latent image", "daguerreotype mercury plate", "collodion wet plate",
    "fixer sodium thiosulphate hypo", "dry gelatin plate", "orthochromatic panchromatic dye sensitiser",
    "colour film subtractive coupler", "shutter speed aperture exposure reciprocity",
    "developer reduction grain", "cyanotype blueprint iron",
    # meteorology and weather forecasting
    "barometer pressure falling storm", "weather balloon radiosonde upper air",
    "numerical weather prediction grid", "cold front warm front occlusion", "Beaufort scale wind",
    "ensemble forecast chaos initial conditions", "hygrometer humidity dew point",
    "synoptic chart telegraph weather map", "hurricane eye wall", "fog radiation advection",
    # Roman law and legal history
    "Twelve Tables Roman law", "praetor edict formula", "Justinian Digest codification",
    "jurist responsa opinion", "usucapio possession property Roman", "stipulatio contract oral Roman",
    "manumission slave freedman Rome", "provincial governor jurisdiction Rome",
    # cephalopod cognition and camouflage
    "chromatophore skin cuttlefish", "octopus arm nervous system", "colour blind cephalopod polarisation",
    "cuttlefish camouflage substrate", "octopus jar opening problem", "squid giant axon",
    "ink cloud decoy cephalopod", "mimic octopus", "nautilus shell chamber buoyancy",
    # crystallography and X-ray diffraction
    "Bragg law diffraction crystal", "unit cell lattice symmetry", "powder diffraction pattern identification",
    "phase problem heavy atom", "protein crystal growth", "electron density map model",
    "Laue photograph spot", "polymorph crystal form drug",
    # folk song collecting and ethnomusicology
    "phonograph cylinder field recording song", "variant version ballad collecting",
    "modal tune scale folk", "collector transcription notation folk song", "work song rhythm labour",
    "revival singer repertoire", "tune family melody comparison", "archive recording repatriation",
    # currency, coinage and banking history
    "mint die coin striking", "debasement silver content coin", "bimetallism gold silver ratio",
    "bill of exchange merchant banking", "double entry bookkeeping ledger", "banknote convertibility reserve",
    "clipping coin milled edge", "cowrie shell currency", "assay office hallmark silver",
    "clearing house cheque settlement",
    # wildfire ecology and fire management
    "serotinous cone fire seed", "prescribed burning fuel load", "fire suppression accumulation debt",
    "fire scar tree ring history", "smokejumper firefighting", "crown fire ladder fuel",
    "resprouting lignotuber fire plant", "fire return interval grassland",
    # knot theory, topology and graph theory
    "knot invariant polynomial distinguish", "Konigsberg bridges Euler path",
    "four colour map theorem", "Mobius strip one side", "planar graph crossing",
    "unknot recognition diagram move", "Euler characteristic polyhedron", "network shortest path algorithm",
    "topology rubber sheet deformation",
    # penguins and seabird colonies
    "emperor penguin huddle incubation", "penguin countershading swimming",
    "guano colony seabird nutrient", "albatross dynamic soaring", "colony census aerial photograph seabird",
    "krill diet penguin sea ice", "gannet plunge diving", "burrow nesting petrel predator",
    "seabird island rat eradication",
    # plant hormones and tropisms
    "auxin phototropism coleoptile", "gravitropism root statolith", "ethylene ripening fruit gas",
    "abscisic acid stomata drought", "gibberellin stem elongation dwarf", "apical dominance pruning bud",
    "thigmotropism tendril climbing", "cytokinin tissue culture shoot", "leaf abscission autumn hormone",
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
    from rw_test21 import QUESTIONS
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
    from rw_test21 import QUESTIONS
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
