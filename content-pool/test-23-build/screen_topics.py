#!/usr/bin/env python3
"""Originality screen for Test 23 R&W topics against the banked corpus.

Two passes, run in this order and for different reasons:

  1. `keywords` — screen a candidate topic BEFORE writing its passage. A topic
     is cheap to abandon at this stage and expensive to abandon after drafting.
     Reports every banked passage that mentions any of the topic's keywords.

  2. `final` — screen the finished rw_test23 passages by content-word Jaccard
     and by shared 5-grams. Threshold: reject at 0.50, READ every match at or
     above 0.45. The Test 18-21 finding is that Jaccard is triage, not a
     verdict — a genuine repeat that changes its setting words scores LOW
     precisely because it changed the words.

Keyword note: every pattern is compiled with an explicit leading lookaround
`(?<![a-z])` and, where the word can be a prefix of an unrelated word, a
trailing one too. `\\b` is not enough and bare substrings are worse than no
check — `lock` matches "block"/"clock", `port` matches "important"/"support",
`pound` matches "compound", `tow` matches "town", `reach` and `gate` and
`lift` all have everyday senses. Those five are deliberately NOT used as
screening keywords on their own; they only appear inside multi-word phrases.

Usage:
    python3 screen_topics.py keywords
    python3 screen_topics.py final
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


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def load_corpus():
    with open(CORPUS) as fh:
        rows = json.load(fh)
    for r in rows:
        r["_t"] = toks((r.get("passage") or "") + " " + (r.get("stem") or ""))
        r["_s"] = set(r["_t"])
        r["_g"] = ngrams(r["_t"])
        r["_flat"] = " ".join(strip_html((r.get("passage") or "") + " " + (r.get("stem") or "")).lower().split())
    return rows


# ---------------------------------------------------------------- keyword pass
# Every entry is a candidate topic inside Test 23's territory: canal locks and
# pounds, barge haulage, aqueducts, dredging, towpaths, wharves and quays, and
# canal toll keeping.
CANDIDATES = {
    # locks and pounds
    "side ponds saving lock water": ["side pond", "side pound", "lockful", "back.?pump"],
    "staircase locks": ["staircase lock", "riser lock"],
    "mitre gates held shut by pressure": ["mitre gate", "miter gate", "gate recess"],
    "lock flight timing": ["lock flight", "flight of locks", "caen hill", "devizes"],
    "boat lift / inclined plane": ["boat lift", "inclined plane", "anderton", "falkirk wheel", "caisson lock"],
    "stop gates and breaches": ["stop gate", "stop plank", "breach"],
    "summit pound water supply": ["summit pound", "summit level", "feeder reservoir"],
    "guillotine gate": ["guillotine gate"],
    # barge haulage
    "legging through tunnels": ["legging", "legger", "tunnel wall"],
    "bow hauliers": ["bow haul", "hauliers"],
    "wash from powered boats eroding banks": ["bank erosion", "wash from", "speed limit"],
    "fly boats worked day and night": ["fly boat", "fly.?boat"],
    "boat families living aboard": ["boat family", "boatman", "boatwoman", "narrow boat", "narrowboat"],
    "boat horse feed and stabling": ["boat horse", "canal horse", "stabling"],
    "ice boats breaking ice": ["ice boat", "icebreak"],
    # aqueducts
    "a boat crossing adds no weight to an aqueduct": ["displaces its own", "adds no weight", "archimedes"],
    "swing aqueduct": ["swing aqueduct", "barton"],
    "puddled clay lining": ["puddled clay", "puddle clay", "clay lining"],
    "cast-iron trough aqueduct": ["cast.?iron trough", "iron trough", "pontcysyllte", "aqueduct"],
    # dredging
    "spoon and bucket-ladder dredgers": ["spoon dredger", "bucket ladder", "mud boat", "dredger"],
    "where dredged spoil goes": ["spoil bank", "dredged spoil", "offside bank"],
    "weed cutting vs dredging": ["weed cut", "weed boat"],
    # towpaths
    "turnover / changeline bridges": ["turnover bridge", "changeline", "roving bridge"],
    "rope grooves worn in bridge stone": ["rope groove", "roller post", "rubbing plate", "grooves worn"],
    "towpath as right of way": ["towpath"],
    # wharves and quays
    "gauging a boat by freeboard": ["gauging", "freeboard", "dry inches", "gauge table"],
    "canal arm into a warehouse": ["canal arm", "shipping hole", "warehouse arm"],
    "wharfinger and the private wharf": ["wharfinger", "wharf", "quay"],
    "limekilns at a canal wharf": ["limekiln", "lime kiln"],
    # toll keeping
    "toll by cargo class and ton-mile": ["ton.?mile", "toll table", "toll clerk", "toll house", "tollhouse"],
    "toll evasion and the check clerk": ["check clerk", "under.?declar"],
    "compensation / bar tolls between companies": ["compensation toll", "bar toll"],
    "published rate ceilings and railway competition": ["rate ceiling", "maximum toll", "act of parliament"],
    # wider canal setting
    "canal mania share speculation": ["canal mania", "subscription list", "share speculation"],
    "navvies who dug the cuttings": ["navvy", "navvies"],
    "canal restoration by volunteers": ["restoration society", "volunteer"],
    "freight on water vs road today": ["tonne.?kilometre", "ton.?kilometre", "modal shift"],
}


def keyword_pass(rows):
    print(f"corpus: {len(rows)} banked passages\n")
    clean = []
    for topic, kws in CANDIDATES.items():
        pats = [re.compile(r"(?<![a-z])(?:" + k + r")", re.I) for k in kws]
        hits = []
        for r in rows:
            for p in pats:
                m = p.search(r["_flat"])
                if m:
                    i = m.start()
                    hits.append(f"      {r.get('src')} {r.get('num')} [{m.group(0)}] "
                                f"…{r['_flat'][max(0, i - 60):i + 80].strip()}…")
                    break
        if hits:
            print(f"  HIT  {topic}  ({len(hits)})")
            for h in hits[:4]:
                print(h)
        else:
            clean.append(topic)
    print(f"\n  CLEAN, no banked mention ({len(clean)}):")
    for t in clean:
        print(f"      {t}")


# ------------------------------------------------------------------ final pass
def final_pass(rows):
    from rw_test23 import QUESTIONS
    worst = []
    for q in QUESTIONS:
        t = toks((q.get("passage") or "") + " " + (q.get("stem") or ""))
        s, g = set(t), ngrams(t)
        best = (0.0, None)
        for r in rows:
            j = jaccard(s, r["_s"])
            if j > best[0]:
                best = (j, r)
        shared = [r for r in rows if g & r["_g"]]
        worst.append((best[0], q["num"], best[1], shared))

    worst.sort(reverse=True, key=lambda x: x[0])
    print(f"{len(QUESTIONS)} authored items vs {len(rows)} banked passages\n")
    print("  highest Jaccard first — READ everything at or above 0.45\n")
    over = 0
    for j, num, r, shared in worst[:20]:
        flag = "  <-- REJECT" if j >= 0.50 else ("  <-- READ" if j >= 0.45 else "")
        if j >= 0.45:
            over += 1
        print(f"    {j:.2f}  {num:<5} vs {r.get('src')} {r.get('num')}{flag}")
    ng = [(num, ["%s %s" % (r.get("src"), r.get("num")) for r in shared])
          for j, num, r, shared in worst if shared]
    print(f"\n  items sharing a 5-gram with a banked passage: {len(ng)}")
    for num, srcs in ng[:10]:
        print(f"    {num}: {srcs[:4]}")
    print(f"\n  highest R&W Jaccard vs corpus: {worst[0][0]:.2f}")
    print(f"  items at or above 0.45: {over}")
    return 1 if worst[0][0] >= 0.50 else 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "keywords"
    corpus = load_corpus()
    if mode == "keywords":
        keyword_pass(corpus)
    else:
        raise SystemExit(final_pass(corpus))
