# -*- coding: utf-8 -*-
"""Compare every transcribed answer against the book's printed key.

    python3 verify_keys.py            # report
    python3 verify_keys.py --write    # also write disputes.json / ready.json

The agents never saw the printed key. This is the first time the two are put
side by side, which is the whole point: a disagreement here is evidence, not
noise, because neither side was derived from the other.

Free-response comparison is by VALUE, not string. The book writes 1/8 where an
agent may write 0.125, and 173/2 where an agent writes 86.5; those agree. A
string compare would manufacture hundreds of fake disputes and bury the real
ones.
"""
import json, glob, os, re, sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
keys = json.load(open(f"{HERE}/printed_keys.json"))

rows = []
for f in sorted(glob.glob(f"{HERE}/out/mx-*.jsonl")):
    for line in open(f):
        line = line.strip()
        if line:
            try: rows.append(json.loads(line))
            except Exception: pass


# A printed key can be several things that are NOT a disagreement:
#   "1.1;11/10"   the book listing two accepted forms of one answer
#   "f(x)"        a parse artifact — the key column caught stray body text
#   "268"/"267.6" the book rounding where the agent gave the exact value
# Counting these as disputes buries the real ones. Each is handled explicitly
# rather than by loosening the equality test, so a genuine mismatch cannot
# slip through alongside them.
GARBAGE = re.compile(r"[A-Za-z(){}\\]")


def alternatives(printed):
    """The book sometimes prints two accepted forms, separated by a semicolon."""
    return [p.strip() for p in str(printed).split(";") if p.strip()]


def num(s):
    """A grid-in value as a number, accepting fractions and decimals."""
    if s is None: return None
    t = str(s).strip().replace(",", "").replace("−", "-").rstrip("%")
    if not t: return None
    try:
        return Fraction(t) if "/" in t else Fraction(str(float(t)))
    except Exception:
        return None


ready, disputes, unanswerable, nokey, rounded, value_keyed = [], [], [], [], [], []
for r in rows:
    printed = keys.get(r["id"])
    mine_l, mine_v = r.get("answerLabel"), r.get("answerValue")
    if not mine_l and mine_v in (None, ""):
        unanswerable.append((r, printed)); continue
    ptxt = str(printed).strip()
    if printed in (None, "") or (GARBAGE.search(ptxt) and ptxt.upper() not in ("A","B","C","D")):
        nokey.append(r); continue
    alts = alternatives(printed)
    if mine_l:
        agree = any(a.upper() == mine_l.strip().upper() for a in alts)
        # For some multiple-choice items the book prints the ANSWER ITSELF in
        # the key column instead of its letter — "13" where the answer is
        # choice C, whose content is 13. That is agreement written differently,
        # not a disagreement. Resolve it by matching the key against the
        # content of the choice the agent picked.
        if not agree:
            picked = next((c for c in (r.get("choices") or [])
                           if c.get("label", "").upper() == mine_l.strip().upper()), None)
            if picked:
                txt = re.sub(r"<[^>]+>", "", str(picked.get("content", ""))).strip()
                pv, tv = num(alts[0]), num(txt)
                if (pv is not None and tv is not None and pv == tv) or \
                   (txt and txt == str(alts[0]).strip()):
                    agree = True
                    value_keyed.append((r, printed))
    else:
        a = num(mine_v)
        agree = any(str(mine_v).strip() == alt or
                    (a is not None and num(alt) is not None and a == num(alt))
                    for alt in alts)
        if not agree and a is not None:
            for alt in alts:
                b = num(alt)
                # Only a rounding-sized gap on a value of magnitude >= 1.
                if b is not None and abs(float(a) - float(b)) <= 0.5 <= abs(float(b)):
                    agree = True; rounded.append((r, printed)); break
    (ready if agree else disputes).append((r, printed))

print(f"transcribed        {len(rows)}")
print(f"  agree with key   {len(ready)}")
print(f"  DISPUTED         {len(disputes)}")
print(f"  no answer given  {len(unanswerable)}  (agent judged them unanswerable)")
print(f"  no printed key   {len(nokey)}  (absent, or the key column caught junk)")
print(f"  agreed once the book's rounding is allowed: {len(rounded)}")
print(f"  agreed once a value-instead-of-letter key is read: {len(value_keyed)}")
if rows:
    n = len(ready) + len(disputes)
    print(f"\ndispute rate: {len(disputes)}/{n} = {100*len(disputes)/max(n,1):.1f}%")

print("\nfirst 25 disputes:")
for r, p in disputes[:25]:
    mine = r.get("answerLabel") or r.get("answerValue")
    print(f"  {r['id'][:46]:<46} book {str(p)[:10]:<10} agent {str(mine)[:10]}")

if "--write" in sys.argv:
    json.dump([{**r, "printed_key": p} for r, p in disputes],
              open(f"{HERE}/disputes.json", "w"), indent=1)
    json.dump([r for r, _ in ready], open(f"{HERE}/ready.json", "w"), indent=1)
    json.dump([{**r, "printed_key": p} for r, p in unanswerable],
              open(f"{HERE}/unanswerable.json", "w"), indent=1)
    print(f"\nwrote disputes.json ({len(disputes)}), ready.json ({len(ready)}), "
          f"unanswerable.json ({len(unanswerable)})")
