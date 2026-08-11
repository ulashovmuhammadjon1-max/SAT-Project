#!/usr/bin/env python3
"""Throwaway originality screen for Test 16 R&W.

Two checks against content-pool/rw_authored_corpus.json (809 banked passages):

  keyword  - does any corpus passage/stem mention a candidate topic keyword?
  n-gram   - shared 5-grams and Jaccard over content-word token sets, so a
             differently-worded passage on the same subject is still caught.

Usage:
    python3 screen_topics.py keywords          # screen the candidate topic list
    python3 screen_topics.py final             # screen finished rw_test16 passages
"""
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(HERE, "..", "rw_authored_corpus.json")

STOP = set("""a an the and or but if then than that this these those of in on at to for with
from by as is are was were be been being it its it's he she they them their there here
which who whom whose what when where why how not no nor so such only own same too very
can will just should now into out up down over under again further once about above
below between through during before after both each few more most other some any all
one two three four five six seven eight nine ten first second next last also however
therefore thus because while although though rather instead has have had do does did
made make makes making take takes taken took give gives given get gets got would could
may might must shall said says say new old long short big small great many much less
own per year years time times way ways part parts kind sort thing things text passage
student notes choice choices word words sentence sentences""".split())


def tokens(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = re.sub(r"&[a-z]+;", " ", s)
    return [w for w in re.findall(r"[a-z]+", s.lower()) if len(w) > 2 and w not in STOP]


def load_corpus():
    with open(CORPUS) as fh:
        rows = json.load(fh)
    out = []
    for r in rows:
        text = (r.get("passage") or "") + " " + (r.get("stem") or "")
        out.append((f"{r.get('src')}:{r.get('num')}", text, tokens(text)))
    return out


def jaccard(a, b):
    a, b = set(a), set(b)
    return len(a & b) / len(a | b) if a | b else 0.0


def ngrams(toks, n=5):
    return set(tuple(toks[i:i + n]) for i in range(len(toks) - n + 1))


# ---------------------------------------------------------------- keyword screen
CANDIDATES = {
    # printing / papermaking / bookbinding
    "punchcutting": ["punch", "matrix", "typefounder", "movable type"],
    "type metal antimony": ["antimony", "type metal"],
    "paper sizing": ["sizing", "gelatine size"],
    "watermark laid paper": ["watermark", "laid paper", "deckle"],
    "Fourdrinier machine": ["fourdrinier", "papermaking machine"],
    "iron gall ink": ["iron gall", "gall ink", "oak gall"],
    "rag paper acidity": ["rag paper", "wood pulp", "lignin paper"],
    "marbled endpapers": ["marbled", "endpaper"],
    "sewn binding codex": ["codex", "quire", "signature sewn", "bookbinding"],
    "gold tooling": ["tooling", "gilt edge"],
    "linotype": ["linotype", "hot metal"],
    "imposition chase": ["imposition", "quoin", "forme"],
    # navigation / cartography
    "Mercator projection": ["mercator", "rhumb"],
    "portolan chart": ["portolan", "wind rose"],
    "sounding lead": ["sounding", "lead line", "armed tallow"],
    "log line knots": ["log line", "chip log", "knot speed"],
    "lunar distance": ["lunar distance", "lunars"],
    "dead reckoning": ["dead reckoning", "leeway"],
    "magnetic declination": ["declination", "isogonic", "variation compass"],
    "compass deviation": ["deviation", "flinders bar", "binnacle"],
    "echo sounding": ["echo sound", "fathometer"],
    "chart datum": ["chart datum", "lowest astronomical tide"],
    "buoyage": ["buoy", "cardinal mark", "lateral mark"],
    "sextant": ["sextant", "artificial horizon"],
    # timekeeping at sea
    "marine chronometer": ["chronometer", "harrison", "longitude prize"],
    "time ball": ["time ball", "time signal"],
    "chronometer rate": ["going rate", "rating a chronometer"],
    # textile and dye
    "indigo vat": ["indigo", "woad"],
    "madder alizarin": ["madder", "alizarin"],
    "Tyrian purple murex": ["tyrian", "murex", "purple dye"],
    "alum mordant": ["mordant", "alum"],
    "mauveine": ["mauveine", "perkin", "aniline"],
    "cochineal": ["cochineal", "carmine"],
    "warp weighted loom": ["loom", "warp", "weft"],
    "felting wool scales": ["felting", "fulling"],
    "mercerisation": ["mercer", "mercerised"],
    "flax retting": ["retting", "flax", "bast"],
    "tapestry cartoon": ["tapestry", "gobelins"],
    "lightfastness": ["lightfast", "fading dye"],
    # beekeeping / pollination
    "waggle dance": ["waggle", "bee dance"],
    "bee space Langstroth": ["langstroth", "bee space", "movable frame"],
    "propolis": ["propolis"],
    "royal jelly caste": ["royal jelly", "queen larva"],
    "buzz pollination": ["buzz pollination", "sonication"],
    "honey moisture capping": ["capping", "honey moisture", "nectar water"],
    "varroa": ["varroa", "mite bee"],
    "skep": ["skep"],
    "mason bee": ["mason bee", "leafcutter bee", "solitary bee"],
    "ultraviolet nectar guide": ["nectar guide", "ultraviolet flower"],
    # glass and ceramics
    "glassblowing": ["glassblow", "gather glass", "blowpipe"],
    "soda lime potash glass": ["soda-lime", "potash glass", "forest glass"],
    "crown glass cylinder": ["crown glass", "cylinder glass", "broad glass"],
    "lead crystal": ["lead crystal", "flint glass"],
    "celadon glaze": ["celadon", "reduction firing"],
    "saggar": ["saggar"],
    "tin glaze majolica": ["tin glaze", "majolica", "maiolica", "delft"],
    "porcelain kaolin": ["kaolin", "porcelain", "petuntse"],
    "crazing thermal expansion": ["crazing", "thermal expansion glaze"],
    "annealing lehr": ["annealing", "lehr"],
    "bone china": ["bone china", "bone ash"],
    "slip casting": ["slip cast", "plaster mould"],
    "Lycurgus cup nanoparticle": ["lycurgus", "dichroic glass", "colloidal gold"],
    # harbour and canal engineering
    "caisson": ["caisson"],
    "breakwater armour": ["breakwater", "tetrapod", "dolos"],
    "dredging littoral drift": ["dredg", "littoral drift", "longshore"],
    "training walls": ["training wall", "river mouth bar"],
    "hydraulic lime Eddystone": ["hydraulic lime", "eddystone", "smeaton", "pozzolan"],
    "dry dock": ["graving dock", "dry dock"],
    "boat lift inclined plane": ["boat lift", "inclined plane", "falkirk"],
    "half tide dock": ["half-tide", "wet dock", "tidal basin"],
    "canal aqueduct": ["aqueduct canal", "pontcysyllte"],
    "puddle clay": ["puddle clay", "puddling clay"],
    # Andean / Amazonian archaeology
    "quipu": ["quipu", "khipu"],
    "terra preta": ["terra preta", "dark earth"],
    "chuno freeze drying": ["chuno", "freeze-dried potato"],
    "raised fields waru waru": ["raised field", "waru waru", "tiwanaku"],
    "Inca road tambo": ["inca", "tambo", "qhapaq"],
    "Moche portrait vessel": ["moche", "portrait vessel"],
    "Caral Norte Chico": ["caral", "norte chico", "supe"],
    "Acre geoglyphs": ["geoglyph", "acre earthwork"],
    "vertical archipelago": ["vertical archipelago", "ecological tier"],
    "Machu Picchu drainage": ["machu picchu", "terrace drainage"],
    # birdsong / animal acoustics
    "song learning critical period": ["song learning", "zebra finch", "tutor song"],
    "sparrow dialect": ["dialect", "white-crowned"],
    "lyrebird mimicry": ["lyrebird", "mimicry"],
    "syrinx two voices": ["syrinx"],
    "wren duet": ["duet", "antiphonal"],
    "Lombard effect": ["lombard effect", "traffic noise bird"],
    "acoustic monitoring spectrogram": ["spectrogram", "acoustic monitoring", "autonomous recorder"],
    # pigments
    "Egyptian blue": ["egyptian blue"],
    "ultramarine lapis": ["ultramarine", "lapis"],
    "lead white stack": ["lead white", "stack process"],
    "Prussian blue": ["prussian blue"],
    "Indian yellow": ["indian yellow"],
    "vermilion cinnabar": ["vermilion", "cinnabar"],
    "Scheele green arsenic": ["scheele", "arsenic green", "emerald green"],
    "smalt": ["smalt"],
    "titanium white": ["titanium white", "titanium dioxide"],
    # museum conservation
    "relative humidity case": ["relative humidity", "silica gel case"],
    "anoxic pest treatment": ["anoxic", "nitrogen treatment pest"],
    "XRF Raman pigment id": ["raman", "x-ray fluorescence", "xrf"],
    "reversibility": ["reversib"],
    "Vasa polyethylene glycol": ["vasa", "polyethylene glycol", "waterlogged wood"],
    "tratteggio inpainting": ["tratteggio", "inpaint", "retouch"],
    "lux hours textile": ["lux", "light exposure textile"],
    "bronze disease": ["bronze disease", "chloride corrosion"],
    "paper deacidification": ["deacidif"],
    # Pacific seafaring
    "star compass etak": ["star compass", "etak", "wayfind"],
    "stick chart": ["stick chart", "marshall islands"],
    "voyaging canoe Hokulea": ["hokule", "voyaging canoe", "double-hulled"],
    "swell refraction": ["swell", "wave refraction"],
    "crab claw sail": ["crab-claw", "lateen"],
    # fungi and lichens
    "lichen symbiosis": ["lichen", "schwendener"],
    "lichenometry": ["lichenometry"],
    "fairy ring": ["fairy ring"],
    "ballistospore discharge": ["ballistospore", "spore discharge"],
    "brown rot white rot": ["brown rot", "white rot", "lignin decay"],
    "lichen air quality": ["air quality lichen", "bioindicator"],
    "orchil lichen dye": ["orchil", "lichen dye"],
    # polar logistics
    "depot laying": ["depot", "man-haul"],
    "pemmican": ["pemmican"],
    "sledge dogs ponies": ["sledge dog", "pony haul"],
    "polar scurvy": ["scurvy"],
    "fuel can leather washer": ["primus", "paraffin leak", "fuel depot"],
    "snow blindness": ["snow blindness"],
    "sastrugi": ["sastrugi"],
    "Fram rounded hull": ["fram", "ice-strengthened", "nansen"],
    "crevasse detection": ["crevasse"],
    # economics of ports
    "containerisation": ["container", "mclean"],
    "bonded warehouse": ["bonded warehouse", "port dues", "lighterage"],
    "entrepot": ["entrepot", "entrep"],
    "berth productivity": ["berth", "crane move", "turnaround ship"],
    "transit shed": ["transit shed", "quayside warehouse"],
    "tidal window draught": ["draught", "tidal window"],
}


def keyword_screen():
    corpus = load_corpus()
    hits = 0
    for topic, kws in sorted(CANDIDATES.items()):
        found = []
        for ref, text, _ in corpus:
            low = text.lower()
            for kw in kws:
                if kw in low:
                    found.append((ref, kw))
                    break
        if found:
            hits += 1
            print(f"COLLISION  {topic:<34} {len(found)} hit(s): "
                  f"{', '.join(f'{r}[{k}]' for r, k in found[:4])}")
    print(f"\n{hits} of {len(CANDIDATES)} candidate topics collide.")


def final_screen():
    sys.path.insert(0, HERE)
    # Retargeted: this file was copied from ../test-16-build and its `final`
    # mode still imported that build's questions, so it screened Test 16
    # against the corpus no matter which directory it was run from.
    from rw_test28 import QUESTIONS
    corpus = load_corpus()
    mine = [(q["num"], (q["passage"] or "") + " " + q["stem"]) for q in QUESTIONS]
    mine = [(n, t, tokens(t)) for n, t in mine]

    worst_corpus = (0.0, "", "")
    worst_ng = 0
    for num, _, tk in mine:
        mg = ngrams(tk)
        for ref, _, ctk in corpus:
            j = jaccard(tk, ctk)
            if j > worst_corpus[0]:
                worst_corpus = (j, num, ref)
            shared = len(mg & ngrams(ctk))
            worst_ng = max(worst_ng, shared)
    print(f"vs corpus  max Jaccard {worst_corpus[0]:.3f}  "
          f"({worst_corpus[1]} ~ {worst_corpus[2]})   max shared 5-grams {worst_ng}")

    worst_self = (0.0, "", "")
    self_ng = 0
    for i in range(len(mine)):
        for j2 in range(i + 1, len(mine)):
            j = jaccard(mine[i][2], mine[j2][2])
            if j > worst_self[0]:
                worst_self = (j, mine[i][0], mine[j2][0])
            self_ng = max(self_ng, len(ngrams(mine[i][2]) & ngrams(mine[j2][2])))
    print(f"vs itself  max Jaccard {worst_self[0]:.3f}  "
          f"({worst_self[1]} ~ {worst_self[2]})   max shared 5-grams {self_ng}")

    over = []
    for num, _, tk in mine:
        for ref, _, ctk in corpus:
            if jaccard(tk, ctk) >= 0.5:
                over.append((num, ref, round(jaccard(tk, ctk), 3)))
    for i in range(len(mine)):
        for j2 in range(i + 1, len(mine)):
            v = jaccard(mine[i][2], mine[j2][2])
            if v >= 0.5:
                over.append((mine[i][0], mine[j2][0], round(v, 3)))
    print(f"pairs at or above 0.5 Jaccard: {len(over)}")
    for row in over:
        print("   ", row)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "keywords"
    (keyword_screen if mode == "keywords" else final_screen)()
