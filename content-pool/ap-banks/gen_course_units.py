"""Turn a subject's committed CED topic list into a TypeScript units block.

    python3 gen_course_units.py HUMAN_GEO > /tmp/hg_units.ts

Reads `<SUBJ>_topics.json`, which the authoring agents write straight from the
Course and Exam Description, and prints the `ApUnit[]` literal for
`src/lib/ap/courses.ts`.

Generating rather than hand-typing is the point: the course outline a student
navigates and the topic codes the question bank is keyed on then come from one
file, so a topic cannot exist on the site with no questions behind it, or vice
versa. `check_course_coverage.py` asserts exactly that against production.

The JSON shape, written by the agent that read the CED:

    {
      "_units":    {"1": "Unit Title", ...},
      "_weights":  {"1": "12-17%", ...},        # optional
      "_blurbs":   {"1": "One line.", ...},     # optional
      "1.1": "Topic Title", "1.2": "...", ...
    }
"""
import json
import sys


def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def main():
    subj = sys.argv[1]
    data = json.load(open(f"{subj}_topics.json"))
    units = data.get("_units", {})
    weights = data.get("_weights", {})
    blurbs = data.get("_blurbs", {})
    codes = sorted(
        (k for k in data if not k.startswith("_")),
        key=lambda c: [int(p) for p in c.split(".")],
    )

    by_unit = {}
    for c in codes:
        by_unit.setdefault(c.split(".")[0], []).append(c)

    out = ["["]
    for u in sorted(by_unit, key=int):
        out.append("  {")
        out.append(f"    number: {int(u)},")
        out.append(f'    title: "{esc(units.get(u, ""))}",')
        if weights.get(u):
            out.append(f'    weight: "{esc(weights[u])}",')
        if blurbs.get(u):
            out.append(f'    blurb: "{esc(blurbs[u])}",')
        out.append("    topics: [")
        for c in by_unit[u]:
            out.append(f'      {{ code: "{c}", title: "{esc(data[c])}" }},')
        out.append("    ],")
        out.append("  },")
    out.append("]")
    print("\n".join(out))
    print(
        f"// {subj}: {len(by_unit)} units, {len(codes)} topics",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
