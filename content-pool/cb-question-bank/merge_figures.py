"""
Fold rebuilt figures back into the parsed bank.

    python3 merge_figures.py <bank.json> <figures.json> <out.json>

The 73 `needs_figure` questions were excluded from every test build, because
their charts are vector glyphs that text extraction shredded into unusable
axis fragments. With the figure rebuilt — as a real <table> where the data is
discrete, or a regenerated chart image where the question depends on the shape
of a trend — the question becomes usable and the flag can be cleared.

The figure is stored on the question rather than spliced into its text, so the
inserter can put a table into the passage HTML and a chart into
`Question.imageUrl`, which is what the schema expects.
"""
import json
import sys


def main():
    bank_path, figs_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    bank = json.load(open(bank_path))
    figs = {f["id"]: f for f in json.load(open(figs_path))}

    cleared = 0
    for q in bank:
        f = figs.get(q.get("id"))
        if not f:
            continue
        if "error" in q:
            continue
        q["question"] = f["question"]
        if f.get("figure_html"):
            q["figure_html"] = f["figure_html"]
        if f.get("figure_png_b64"):
            q["figure_image"] = f["figure_png_b64"]
        q["needs_figure"] = False
        q["figure_rebuilt"] = True
        cleared += 1

    still = [q["id"] for q in bank if q.get("needs_figure")]
    print(f"cleared needs_figure on {cleared} questions")
    print(f"still flagged: {len(still)}")
    tables = sum(1 for q in bank if q.get("figure_html"))
    charts = sum(1 for q in bank if q.get("figure_image"))
    print(f"  as a real <table>: {tables}   as a chart image: {charts}")
    json.dump(bank, open(out_path, "w"), indent=1)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
