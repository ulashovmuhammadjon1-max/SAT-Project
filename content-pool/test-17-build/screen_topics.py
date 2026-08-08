#!/usr/bin/env python3
"""Throwaway originality screen for Test 17 R&W topics.

Two passes:
  1. keyword hit — does any banked passage/stem mention a topic keyword at all
  2. n-gram / Jaccard — does any banked passage share content-word vocabulary or
     a 5-gram with a candidate passage (catches a differently-worded passage on
     the same subject)

Usage:
    python3 screen_topics.py keywords          # screen the candidate topic list
    python3 screen_topics.py final             # screen finished rw_test17 passages
"""
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(HERE, "..", "rw_authored_corpus.json")

STOP = set("""a an the and or but if of to in on at by for with from as is are was were be been
being it its this that these those which who whom whose what when where how why not no than then
so such can could will would may might must shall should do does did done have has had having
one two three four five six seven eight nine ten first second more most less least many much few
some any all each every other another same own very just also only into out up down over under
about after before during while because since until through between against among within without
their they them there here he she his her him we us our you your i me my than too s t
""".split())

WORD = re.compile(r"[a-z]+")


def strip_html(s):
    return re.sub(r"<[^>]+>", " ", s or "")


def toks(s):
    s = strip_html(s).lower().replace("&mdash;", " ").replace("&rsquo;", "'")
    s = re.sub(r"&[a-z]+;", " ", s)
    return [w for w in WORD.findall(s) if w not in STOP and len(w) > 2]


def ngrams(t, n=5):
    return set(tuple(t[i:i + n]) for i in range(len(t) - n + 1))


def load_corpus():
    with open(CORPUS) as fh:
        rows = json.load(fh)
    for r in rows:
        r["_t"] = toks((r.get("passage") or "") + " " + (r.get("stem") or ""))
        r["_s"] = set(r["_t"])
        r["_g"] = ngrams(r["_t"])
    return rows


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


# ---------------------------------------------------------------- keyword pass
CANDIDATES = {
    # mountaineering / high-altitude physiology
    "acclimatisation red cells": ["acclimat", "haemoglobin", "hemoglobin", "erythropoi"],
    "hypoxia / death zone": ["hypox", "death zone", "8,000", "summit oxygen"],
    "supplementary oxygen sets": ["oxygen set", "oxygen cylinder", "everest"],
    "acute mountain sickness": ["mountain sickness", "acetazolamide", "altitude sickness"],
    "crampons and ice axes": ["crampon", "ice axe", "self-arrest"],
    "live high train low": ["altitude training", "train low"],
    "Tibetan altitude adaptation": ["tibetan", "sherpa", "andean highland"],
    # surveying / geodesy
    "Great Trigonometrical Survey": ["trigonometrical survey", "everest survey", "baseline measure"],
    "geoid vs ellipsoid": ["geoid", "ellipsoid", "datum"],
    "triangulation networks": ["triangulat", "theodolite", "trilater"],
    "levelling and benchmarks": ["benchmark", "levelling", "spirit level"],
    "Struve arc": ["struve"],
    "metre from the meridian": ["delambre", "m&eacute;chain", "meridian arc"],
    "GNSS reference stations": ["gnss", "gps station", "plate motion"],
    "plane table": ["plane table", "alidade"],
    # railways and signalling
    "absolute block signalling": ["block signal", "signalman", "absolute block"],
    "interlocking": ["interlock"],
    "track circuits": ["track circuit"],
    "railway standard time": ["railway time", "standard time", "timetable"],
    "cab signalling": ["cab signal", "automatic warning"],
    "break of gauge": ["gauge", "broad gauge"],
    "continuous welded rail": ["welded rail", "fishplate", "rail expansion"],
    "semaphore to colour light": ["semaphore", "colour-light"],
    # forestry / timber / tree rings
    "cross-dating tree rings": ["cross-dat", "dendrochronol", "tree ring", "tree-ring"],
    "bristlecone chronologies": ["bristlecone"],
    "coppicing": ["coppic", "pollard"],
    "seasoning timber": ["season", "moisture content", "kiln-dried"],
    "quartersawn lumber": ["quartersawn", "sawmill", "kerf"],
    "log driving": ["log drive", "log driving", "river drive"],
    "selection silviculture": ["silvicultur", "clearcut", "clear-cut"],
    # seismology / earthquake engineering
    "P and S waves / core": ["shadow zone", "s-wave", "p-wave", "seismic wave"],
    "base isolation": ["base isolat", "isolation bearing"],
    "magnitude vs intensity": ["mercalli", "moment magnitude", "richter"],
    "earthquake early warning": ["early warning"],
    "soil liquefaction": ["liquefaction"],
    "tuned mass damper": ["mass damper", "damper"],
    "masonry retrofit": ["retrofit", "unreinforced masonry"],
    "palaeoseismology trenching": ["palaeoseism", "paleoseism", "fault trench"],
    # Central Asia / Silk Road
    "karez and qanat": ["karez", "qanat"],
    "Sogdian letters": ["sogdian"],
    "Bactrian camels": ["bactrian", "caravan"],
    "Kushan coinage": ["kushan"],
    "yurt construction": ["yurt", "ger "],
    "Mongol yam relay post": ["yam ", "relay station", "post station"],
    "Ferghana horses": ["ferghana", "fergana"],
    "Aral Sea diversion": ["aral"],
    # insect flight
    "asynchronous flight muscle": ["asynchronous", "flight muscle"],
    "halteres": ["halter"],
    "clap and fling / leading-edge vortex": ["leading-edge vortex", "clap and fling"],
    "water striders": ["water strider", "surface tension"],
    "resilin catapult": ["resilin", "catapult"],
    "dragonfly wing control": ["dragonfl"],
    "cockroach locomotion": ["cockroach"],
    # radio astronomy
    "aperture synthesis": ["aperture synthesis", "interferomet", "very large array"],
    "pulsar discovery": ["pulsar"],
    "21 cm hydrogen line": ["hydrogen line", "21 cm", "21-centimetre"],
    "radio quiet zone": ["radio quiet", "interference"],
    "cosmic microwave background": ["microwave background", "penzias"],
    "dish surface accuracy": ["radio dish", "parabol"],
    "fast radio bursts": ["fast radio burst", "dispersion measure"],
    # caves / karst
    "speleothem climate record": ["speleothem", "stalagmite", "stalactite"],
    "sinkholes and dolines": ["sinkhole", "doline"],
    "cave survey grades": ["cave survey"],
    "troglobite eye loss": ["troglobit", "cavefish", "cave fish"],
    "dye tracing": ["dye trac", "fluorescein"],
    "breathing caves": ["breathing cave", "cave air"],
    "sulfuric acid speleogenesis": ["lechuguilla", "speleogenesis"],
    # Nordic / Icelandic literature
    "skaldic kennings": ["kenning", "skald"],
    "saga understatement": ["saga"],
    "Codex Regius / Eddic poetry": ["codex regius", "edda", "eddic"],
    "Icelandic neologism policy": ["icelandic", "neologism"],
    "rimur chanting": ["r&iacute;mur", "rimur"],
    "Laxness": ["laxness"],
    "runestones": ["runeston", "runic"],
    # water rights / irrigation law
    "prior appropriation": ["prior appropriation", "riparian"],
    "acequia": ["acequia"],
    "water markets": ["water market", "water right"],
    "Colorado River Compact": ["colorado river", "compact"],
    "Balinese subak": ["subak", "water temple"],
    "groundwater common pool": ["groundwater", "aquifer"],
    "beneficial use doctrine": ["beneficial use"],
    # urban trees / city ecology
    "structural soil and compaction": ["structural soil", "soil compaction", "street tree"],
    "urban heat island canopy": ["heat island", "canopy cover"],
    "stormwater tree pits": ["stormwater", "bioswale", "tree pit"],
    "i-Tree valuation": ["i-tree", "ecosystem service"],
    "urban wildlife adaptation": ["urban fox", "urban bird", "city bird"],
    "street tree monoculture": ["dutch elm", "monocultur"],
    # voting / apportionment
    "Huntington-Hill apportionment": ["apportion", "huntington", "alabama paradox"],
    "Arrow's theorem": ["arrow", "impossibility"],
    "Condorcet cycles": ["condorcet"],
    "ranked choice / instant runoff": ["ranked choice", "instant runoff", "approval voting"],
    "compactness and districting": ["gerrymander", "district"],
    "quota rule divisor methods": ["divisor method", "quota rule"],
    # whales / cetacean acoustics
    "humpback song transmission": ["humpback", "whale song"],
    "SOFAR channel": ["sofar", "sound channel"],
    "baleen lunge feeding": ["baleen", "lunge feed"],
    "sperm whale codas": ["sperm whale", "coda"],
    "earplug records": ["earplug", "earwax"],
    "ship noise masking": ["ship noise", "masking"],
    "blue whale call pitch": ["blue whale"],
    # dairying / cheese
    "rennet and casein": ["rennet", "casein", "curd"],
    "propionic eyes in cheese": ["propionic", "emmental", "cheese eye"],
    "affinage and rind washing": ["affinage", "rind", "cheese cave"],
    "raw milk flavour": ["raw milk", "pasteuris", "pasteuriz"],
    "whey": ["whey"],
    "alpine transhumance dairies": ["transhumance", "alpine dairy", "cheese cooperative"],
    "lactase persistence": ["lactase", "lactose"],
}


def keyword_pass():
    rows = load_corpus()
    blobs = [(r, (strip_html(r.get("passage", "")) + " " + strip_html(r.get("stem", ""))).lower())
             for r in rows]
    clean, hit = [], []
    for topic, kws in CANDIDATES.items():
        found = []
        for kw in kws:
            for r, b in blobs:
                if kw in b:
                    found.append((kw, r["src"], r["num"]))
                    break
        if found:
            hit.append((topic, found))
        else:
            clean.append(topic)
    print(f"CLEAN ({len(clean)}):")
    for t in clean:
        print("   ", t)
    print(f"\nCOLLISION ({len(hit)}):")
    for t, f in hit:
        print("   ", t, "->", f)


def final_pass():
    sys.path.insert(0, HERE)
    from rw_test17 import QUESTIONS
    rows = load_corpus()
    mine = []
    for q in QUESTIONS:
        t = toks((q.get("passage") or "") + " " + (q.get("stem") or ""))
        mine.append((q["num"], t, set(t), ngrams(t)))

    worst_corpus, worst_self = [], []
    for num, t, s, g in mine:
        best = max(((jaccard(s, r["_s"]), len(g & r["_g"]), r["src"], r["num"]) for r in rows),
                   default=(0, 0, "", ""))
        worst_corpus.append((best[0], num, best[1], best[2], best[3]))
    for i, (num, t, s, g) in enumerate(mine):
        for num2, t2, s2, g2 in mine[i + 1:]:
            worst_self.append((jaccard(s, s2), len(g & g2), num, num2))

    worst_corpus.sort(reverse=True)
    worst_self.sort(reverse=True)
    print("Top Jaccard vs 809-passage corpus:")
    for j, num, ng, src, n2 in worst_corpus[:12]:
        flag = "  <-- REWRITE" if j >= 0.5 else ""
        print(f"  {j:.3f}  {num:>4}  shared5grams={ng}  vs {src}:{n2}{flag}")
    print("\nTop Jaccard among Test 17 passages:")
    for j, ng, a, b in worst_self[:12]:
        flag = "  <-- REWRITE" if j >= 0.5 else ""
        print(f"  {j:.3f}  {a} / {b}  shared5grams={ng}{flag}")
    over = [x for x in worst_corpus if x[0] >= 0.5] + [x for x in worst_self if x[0] >= 0.5]
    print(f"\n{len(over)} pair(s) at or above 0.5 Jaccard")
    shared = [x for x in worst_corpus if x[2] > 0] + [x for x in worst_self if x[1] > 0]
    print(f"{len(shared)} pair(s) sharing any 5-gram")
    return 0 if not over else 1


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "keywords"
    if mode == "keywords":
        keyword_pass()
    else:
        raise SystemExit(final_pass())
