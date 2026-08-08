#!/usr/bin/env python3
"""Throwaway originality screen for Test 18 R&W.

Two independent checks against content-pool/rw_authored_corpus.json (809 passages):

  keywords  - report any corpus passage containing a candidate topic keyword
  ngrams    - shared 5-grams and Jaccard over content-word token sets, so a
              differently-worded passage on the same subject is still caught

Usage:
    python3 check_originality.py keywords          # screen TOPICS below
    python3 check_originality.py ngrams            # screen finished rw_test18
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

# Candidate topics for Test 18, drawn from the assigned territories.
TOPICS = [
    # aviation / ballooning / flight
    "hot-air balloon Montgolfier", "wind tunnel Wright brothers", "airship dirigible hydrogen",
    "autogyro rotor Cierva", "pitot tube airspeed", "glider soaring thermal",
    "aircraft rivet flush drag", "de Havilland Comet fatigue window", "ejection seat",
    "parachute silk canopy", "aerial photography survey aircraft", "stall angle of attack wing",
    # brewing / fermentation / food microbiology
    "lager yeast Saccharomyces eubayanus", "sourdough starter", "koji Aspergillus soy",
    "kimchi lactic fermentation", "vinegar acetic mother", "cheese rind ripening",
    "hop resin bitterness beer", "wort mash enzyme barley", "botulism canning",
    "pasteurisation milk", "kefir grain", "cocoa bean fermentation chocolate",
    # watchmaking / precision mechanics
    "escapement lever watch", "hairspring balance wheel", "jewel bearing ruby watch",
    "tourbillon", "quartz crystal watch oscillator", "gear cutting engine dividing",
    "screw thread standard Whitworth", "gauge blocks Johansson metrology",
    # quarrying / stonemasonry / building stone
    "quarry plug and feather splitting", "Portland stone", "marble Carrara",
    "mason banker chisel", "granite polishing", "slate roofing splitting",
    "limestone weathering facade", "flint knapping wall",
    # orchards / grafting / fruit breeding
    "apple grafting rootstock", "pollination orchard cross", "pear espalier",
    "citrus budwood virus", "cider apple tannin", "seedling variety chance apple",
    "chill hours dormancy fruit", "banana clone Cavendish",
    # epidemiology / public health history
    "John Snow cholera pump", "quarantine lazaretto plague", "smallpox variolation vaccination",
    "sanitation sewer typhoid", "yellow fever mosquito", "puerperal fever handwashing",
    "cohort study smoking", "contact tracing tuberculosis", "iodised salt goitre",
    "pellagra niacin diet", "scurvy citrus naval",
    # medieval manuscripts / palaeography
    "parchment vellum scribe", "illumination gold leaf initial", "palimpsest scraped",
    "Carolingian minuscule script", "abbreviation mark scribal", "quire gathering binding",
    "marginalia gloss", "oak gall iron ink", "catchword",
    # desert ecology / arid-land agriculture
    "qanat underground channel irrigation", "saguaro cactus", "camel water",
    "date palm oasis", "dew harvesting fog net", "seed dormancy desert annual",
    "salt crust soil salinity irrigation", "terrace runoff farming Negev",
    "sand dune stabilisation grass", "kangaroo rat kidney",
    # semiconductors / computing hardware
    "transistor germanium point contact", "integrated circuit planar process",
    "photolithography wafer mask", "core memory ferrite", "Moore's law transistor density",
    "clean room dust", "silicon crystal Czochralski boule", "punched card tabulating",
    "hard disk head flying", "vacuum tube computer ENIAC",
    # West African metallurgy / empires
    "Nok terracotta iron smelting", "bloomery furnace tuyere", "Mali Mansa Musa gold",
    "Benin brass plaque lost wax", "Ife bronze head", "Songhai Gao trade",
    "salt gold trans-Saharan caravan", "Igbo-Ukwu casting",
    # sleep / circadian science
    "circadian clock suprachiasmatic", "melatonin light evening", "jet lag phase shift",
    "REM sleep dreaming", "sleep spindle memory consolidation", "shift work night",
    "chronotype morning evening", "blind free-running rhythm",
    # tidal / wave energy
    "tidal barrage estuary turbine", "tidal stream turbine current", "oscillating water column wave",
    "point absorber buoy wave", "tidal range Fundy", "biofouling marine turbine",
    "grid intermittency predictability tidal",
    # Japanese woodblock / paper arts
    "ukiyo-e woodblock carver printer", "registration kento mark print",
    "washi paper kozo mulberry", "origami crease pattern", "baren rubbing print",
    "Prussian blue print pigment", "key block outline colour block",
    # seed banks / crop diversity
    "seed bank Svalbard vault", "Vavilov centre of origin", "landrace variety farmer",
    "germination test viability seed", "cryopreservation clone crop", "wheat rust resistance gene",
    "potato blight diversity Andes", "orthodox recalcitrant seed drying",
    # sports biomechanics / training science
    "force plate ground reaction running", "Fosbury flop high jump",
    "altitude training haemoglobin", "tendon elastic energy running",
    "interval training lactate", "pitching elbow torque", "swimming stroke drag",
    "running shoe foam midsole", "sprint start block", "muscle fibre type",
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
    from rw_test18 import QUESTIONS
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
