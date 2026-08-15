# -*- coding: utf-8 -*-
"""Show an agent its next questions, with the page image path and NO key.

    python3 dump_q.py <agent> --todo 6
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
U = "/root/.claude/uploads/16335d00-5283-5db6-a7a3-023a1a5fae45"
os.makedirs(f"{HERE}/pages", exist_ok=True)
name = sys.argv[1]
n = int(sys.argv[sys.argv.index("--todo") + 1]) if "--todo" in sys.argv else 6
qs = json.load(open(f"{HERE}/out/{name}.slice.json"))
done = set()
jl = f"{HERE}/out/{name}.jsonl"
if os.path.exists(jl):
    for line in open(jl):
        line = line.strip()
        if line:
            try: done.add(json.loads(line)["id"])
            except Exception: pass
todo = [q for q in qs if q["id"] not in done][:n]
print(f"# {len(done)}/{len(qs)} done — next {len(todo)}\n")
for q in todo:
    # Named by (source file, PDF page), unambiguous for all three books.
    # Naming by printed page broke for Math 3.0, which prints none, and
    # silently pointed a Math 2.0 question at the wrong file's page 2.
    pg = q.get("pdf_page") or q.get("page")
    img = f"{HERE}/pages/{q.get('src')}-{pg:03d}.png"
    print("=" * 70)
    print(f"id        {q['id']}")
    print(f"book      {q['book']}   topic {q['topic']}   #{q['num']}"
          + (f"   exam {q['exam']}" if q.get("exam") else ""))
    print(f"PAGE IMAGE {img}")
    if not os.path.exists(img):
        print("  render it first:")
        print(f"  pdftoppm -f {pg} -l {pg} -r 150 -png -singlefile '{U}/{q.get('src')}' '{img[:-4]}'")
    print(f"\n-- extracted text (UNRELIABLE for maths; use it only to find the question on the page) --")
    print(q["body"][:900])
    for c in q["choices"]:
        print(f"  {c['label']}) {c['content'][:160]}")
    print()
