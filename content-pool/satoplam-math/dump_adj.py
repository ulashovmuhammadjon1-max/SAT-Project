# -*- coding: utf-8 -*-
"""Show an adjudicator its next disputed questions — question text only.

    python3 dump_adj.py adj-1 --todo 6

Neither the printed key nor the first agent's answer appears anywhere in the
slice or in this output. That is the point: a key only moves when two readings
that could not see each other agree against the book.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
name = sys.argv[1]
n = int(sys.argv[sys.argv.index("--todo") + 1]) if "--todo" in sys.argv else 6
qs = json.load(open(f"{HERE}/adj/{name}.slice.json"))
done = set()
p = f"{HERE}/adj/{name}.jsonl"
if os.path.exists(p):
    for line in open(p):
        if line.strip():
            try: done.add(json.loads(line)["id"])
            except Exception: pass
todo = [q for q in qs if q["id"] not in done][:n]
print(f"# {len(done)}/{len(qs)} done — next {len(todo)}\n")
for q in todo:
    print("=" * 70)
    print(f"id   {q['id']}    ({q['type']})")
    if q.get("needsFigure"):
        print("!! depends on a figure — the transcriber's reading of it is below")
    if q.get("book_note"):
        print(f"note from transcription: {q['book_note'][:400]}")
    print(f"\n{q['stem']}\n")
    for c in q["choices"]:
        print(f"  {c['label']}) {c['content']}")
    print()
