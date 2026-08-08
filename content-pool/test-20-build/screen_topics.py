#!/usr/bin/env python3
"""Throwaway originality screen for Test 20 R&W topics.

Two passes:
  1. keyword hit — does any banked passage/stem mention a topic keyword at all
  2. n-gram / Jaccard — does any banked passage share content-word vocabulary or
     a 5-gram with a candidate passage (catches a differently-worded passage on
     the same subject)

Keywords are matched on WORD BOUNDARIES, not as raw substrings: a previous run
had "quire" match *required* and "loom" match *bloom*. A trailing "*" on a
keyword means "prefix match on a whole word" (e.g. "acclimat*").

Usage:
    python3 screen_topics.py keywords          # screen the candidate topic list
    python3 screen_topics.py final             # screen finished rw_test20 passages
"""
import json
import os
import re
import sys

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


def kw_regex(kw):
    """Whole-word (or whole-word-prefix, with a trailing *) matcher."""
    if kw.endswith("*"):
        return re.compile(r"\b" + re.escape(kw[:-1]) + r"[a-z]*\b")
    parts = [re.escape(p) for p in kw.split()]
    return re.compile(r"\b" + r"\s+".join(parts) + r"\b")


# ---------------------------------------------------------------- keyword pass
CANDIDATES = {
    # mining and mineral extraction
    "room and pillar / longwall": ["longwall", "room and pillar", "pit prop*"],
    "mine ventilation and firedamp": ["firedamp", "ventilat*", "methane"],
    "the safety lamp": ["safety lamp", "davy lamp", "flame lamp"],
    "mine drainage engines": ["mine drainage", "pumping engine", "adit"],
    "froth flotation": ["flotation", "froth"],
    "placer and hydraulic gold": ["placer", "sluice", "hydraulic mining"],
    "assay and ore grade": ["assay*", "ore grade", "cut-off grade"],
    "canaries and gas detection": ["canary", "canaries"],
    "salt mining and evaporation": ["salt mine", "brine", "halite"],
    "acid mine drainage": ["acid mine", "tailings"],
    # gas, electricity supply and public utilities
    "coal gas and gasworks": ["gasworks", "coal gas", "town gas", "retort"],
    "the gasholder": ["gasholder", "gasometer"],
    "AC vs DC distribution": ["alternating current", "direct current", "transformer*"],
    "the electric grid and load balancing": ["power grid", "national grid", "load factor"],
    "pumped storage": ["pumped storage", "peak demand"],
    "street lighting": ["street lamp*", "gas lamp*", "lamplighter*", "arc lamp*"],
    "electricity metering and tariffs": ["kilowatt", "tariff*", "meter reading"],
    "water mains and pressure": ["water main*", "standpipe*", "reservoir head"],
    # telegraphy and communication networks
    "submarine telegraph cable": ["submarine cable", "telegraph cable", "atlantic cable"],
    "Morse code and the sounder": ["morse", "sounder", "telegraph key"],
    "telegraph relays and repeaters": ["repeater*", "relay*"],
    "the telephone exchange": ["exchange", "switchboard", "strowger"],
    "packet switching": ["packet switching", "arpanet", "packet*"],
    "semaphore optical telegraph": ["optical telegraph", "chappe", "semaphore"],
    "signal attenuation and gutta-percha": ["gutta-percha", "attenuation", "insulation"],
    "time signals by telegraph": ["time signal*", "time ball"],
    # urban transit and street systems
    "horse-drawn omnibus and tram": ["omnibus", "horsecar", "horse tram"],
    "cable-hauled street railway": ["cable car", "cable railway", "grip"],
    "the electric streetcar and trolley pole": ["streetcar", "trolley", "tramcar"],
    "bus headway and bunching": ["headway", "bunching", "bus route"],
    "the grid street plan": ["street grid", "grid plan", "block size"],
    "traffic signal timing": ["traffic signal*", "green wave", "traffic light*"],
    "fare zones and transfers": ["fare*", "transfer ticket"],
    "one-way systems and gyratories": ["one-way", "gyratory", "roundabout*"],
    # foundries, alloys and metallurgy
    "the blast furnace": ["blast furnace", "pig iron", "coke"],
    "the Bessemer converter": ["bessemer", "converter", "open hearth"],
    "sand casting and the pattern": ["sand casting", "foundry", "moulding sand", "cope and drag"],
    "bell founding and tuning": ["bell found*", "bell metal"],
    "steel quenching and tempering": ["quench*", "temper*", "martensit*"],
    "brass and bronze composition": ["brass", "bronze", "zinc"],
    "wrought iron and puddling": ["puddl*", "wrought iron"],
    "lost-wax casting": ["lost-wax", "cire perdue"],
    "aluminium electrolysis": ["aluminium", "aluminum", "hall-h&eacute;roult", "bauxite"],
    # tunnelling and underground engineering
    "the tunnelling shield": ["tunnelling shield", "tunneling shield", "brunel shield"],
    "compressed air working and the bends": ["caisson disease", "compressed air", "decompression"],
    "tunnel boring machines": ["tunnel boring", "boring machine", "cutterhead"],
    "cut-and-cover underground railway": ["cut-and-cover", "underground railway", "subway"],
    "rock bolts and shotcrete": ["rock bolt*", "shotcrete", "lining"],
    "immersed tube tunnels": ["immersed tube"],
    "tunnel surveying and breakthrough alignment": ["breakthrough", "heading*"],
    # Byzantine and late-antique history
    "Greek fire": ["greek fire", "siphon*"],
    "the Theodosian walls": ["theodosian", "constantinople", "byzantine"],
    "Justinian's law code": ["justinian", "corpus juris", "digest"],
    "Hagia Sophia's pendentives": ["hagia sophia", "pendentive*", "dome"],
    "the theme system": ["theme system", "thematic army"],
    "Byzantine coinage and the solidus": ["solidus", "nomisma", "hyperpyron"],
    "icons and iconoclasm": ["iconoclas*", "icon*"],
    "the late Roman annona grain supply": ["annona", "grain dole", "corn dole"],
    # ants, termites and social insects
    "ant pheromone trails": ["pheromone*", "trail*"],
    "leafcutter ants and fungus gardens": ["leafcutter", "leaf-cutter", "fungus garden"],
    "termite mound ventilation": ["termite*", "mound*"],
    "honeypot ants and repletes": ["honeypot ant", "replete*"],
    "army ant bivouacs": ["army ant*", "bivouac*"],
    "ant colony task allocation": ["task allocation", "division of labour", "colony"],
    "the waggle dance": ["waggle", "dance language"],
    "aphid farming by ants": ["aphid*", "honeydew"],
    # particle physics and detectors
    "the cloud chamber": ["cloud chamber", "bubble chamber"],
    "the cyclotron and synchrotron": ["cyclotron", "synchrotron", "accelerator*"],
    "the neutrino and missing energy": ["neutrino*", "beta decay"],
    "scintillation counters and photomultipliers": ["scintillat*", "photomultiplier*"],
    "the positron and antimatter": ["positron", "antimatter", "antiparticle*"],
    "cosmic ray showers": ["cosmic ray*", "air shower*"],
    "the Cherenkov detector": ["cherenkov", "&#268;erenkov"],
    "the wire chamber and tracking": ["wire chamber", "drift chamber", "spark chamber"],
    "the neutron and the chain reaction": ["neutron*", "chain reaction"],
    # oral epic poetry and formulaic composition
    "the Homeric epithet and formula": ["homer*", "epithet*", "formula*"],
    "Parry and Lord in Yugoslavia": ["parry", "guslar", "yugoslav*"],
    "the Serbian gusle singer": ["gusle", "epic singer"],
    "Central Asian epic Manas": ["manas", "manaschi"],
    "West African griots and jeliya": ["griot*", "jeli*", "sunjata", "sundiata"],
    "oral formula and metre": ["hexameter", "metrical", "oral poetry"],
    "the Mahabharata's oral transmission": ["mahabharata", "sanskrit epic"],
    # insurance, actuarial practice and risk
    "marine insurance and Lloyd's coffee house": ["lloyd*", "marine insurance", "underwrit*"],
    "the life table and mortality": ["life table", "mortality table", "annuit*"],
    "adverse selection": ["adverse selection", "moral hazard"],
    "reinsurance and catastrophe layers": ["reinsur*", "catastrophe bond"],
    "the law of large numbers in pricing": ["law of large numbers", "premium*"],
    "general average in shipping": ["general average", "jettison"],
    "friendly societies and mutual aid": ["friendly societ*", "mutual societ*", "burial club*"],
    # coastal erosion and sediment transport
    "longshore drift and groynes": ["longshore", "groyne*", "groin*"],
    "beach nourishment": ["nourish*", "shingle"],
    "sea cliffs and undercutting": ["sea cliff*", "wave-cut", "undercut*"],
    "sediment budgets and littoral cells": ["littoral cell", "sediment budget"],
    "managed retreat": ["managed retreat", "coastal defence", "coastal defense"],
    "barrier islands and overwash": ["barrier island*", "overwash"],
    "dune stabilisation with marram": ["marram", "dune*"],
    # game theory and strategic behaviour
    "the prisoner's dilemma": ["prisoner's dilemma", "prisoners dilemma", "defect*"],
    "Nash equilibrium": ["nash", "equilibrium"],
    "tit for tat and repeated games": ["tit for tat", "repeated game*"],
    "the tragedy of the commons": ["tragedy of the commons", "common pool"],
    "auction design and the winner's curse": ["auction*", "winner's curse", "sealed bid"],
    "cake cutting and fair division": ["fair division", "cake-cutting", "envy-free"],
    "the stable matching algorithm": ["stable matching", "deferred acceptance", "gale-shapley"],
    "mixed strategies and bluffing": ["mixed strateg*", "bluff*"],
    # bats and echolocation
    "bat echolocation calls and Doppler": ["echolocat*", "doppler"],
    "the moth's ultrasound ear": ["moth*", "ultrasound", "ultrasonic"],
    "bat wing membrane and flight": ["patagium", "bat wing*"],
    "nectar bats and pollination": ["nectar bat*", "pollinat*"],
    "vampire bat food sharing": ["vampire bat*", "blood meal"],
    "bat roosts and hibernacula": ["roost*", "hibernacul*", "white-nose"],
    "the cochlea and auditory foveae": ["cochlea*", "auditory fovea"],
    # immunology and vaccines
    "variolation and Jenner's cowpox": ["variolation", "cowpox", "jenner", "smallpox"],
    "adjuvants": ["adjuvant*"],
    "herd immunity thresholds": ["herd immunity"],
    "antigenic drift in influenza": ["antigenic drift", "influenza"],
    "the cold chain": ["cold chain", "vaccine storage"],
    "memory B cells and boosters": ["memory cell*", "booster*", "antibod*"],
    "attenuated vs inactivated vaccine": ["attenuated", "inactivated"],
    "the polio vaccine trials": ["polio*", "salk", "sabin"],
}


def keyword_pass():
    rows = load_corpus()
    blobs = [(r, (strip_html(r.get("passage", "")) + " " + strip_html(r.get("stem", ""))).lower())
             for r in rows]
    clean, hit = [], []
    for topic, kws in CANDIDATES.items():
        found = []
        for kw in kws:
            rx = kw_regex(kw)
            for r, b in blobs:
                if rx.search(b):
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
    from rw_test20 import QUESTIONS
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
    print(f"Top Jaccard vs {len(rows)}-passage corpus:")
    for j, num, ng, src, n2 in worst_corpus[:15]:
        flag = "  <-- REWRITE" if j >= 0.5 else ""
        print(f"  {j:.3f}  {num:>4}  shared5grams={ng}  vs {src}:{n2}{flag}")
    print("\nTop Jaccard among Test 20 passages:")
    for j, ng, a, b in worst_self[:15]:
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
