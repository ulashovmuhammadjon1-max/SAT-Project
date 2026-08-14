# -*- coding: utf-8 -*-
"""Build legacy_fixes.json from legacy_defects.json + the source pages.

Two kinds of defect, both from EliteXSAT transcription:

  underline  the stem asks about "the underlined sentence/portion" but the
             passage has no <u> at all.  Every one of these transcriptions
             DID record which span was underlined, as a trailing parenthetical
             note -- but a note is not markup, so the student sees nothing.
             The span was confirmed against the source page image in every
             case before it was wrapped (see MANIFEST notes / the agent log).

  figure     the stem says "uses data from the table/graph" but the passage
             has no <table>, no <img> and no imageUrl.

Verification (run by --verify, and by this script before it writes):
  * underline: exactly one <u>...</u>, and stripping the <u>/</u> tags
    reproduces the original passage character for character.
  * figure: tags balanced, every table row the same width.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFECTS = os.path.join(HERE, "legacy_defects.json")
CHARTS = os.path.join(HERE, "legacy_charts.json")
OUT = os.path.join(HERE, "legacy_fixes.json")

TBL = 'style="border-collapse:collapse;margin:0.75rem 0;"'
TH = ('style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;'
      'text-align:left;background:#F4F6F8;"')
TD = 'style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;"'


def table(headers, rows):
    out = [f"<table {TBL}><tr>"]
    out += [f"<th {TH}>{h}</th>" for h in headers]
    out.append("</tr>")
    for r in rows:
        out.append("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>")
    out.append("</table>")
    return "".join(out)


def figure_block(title, html):
    return f"<p><strong>{title}</strong></p>{html}"


def img(b64, alt):
    return (f'<p><img src="{b64}" alt="{alt}" '
            'style="max-width:100%;height:auto;" /></p>')


# ---------------------------------------------------------------------------
# The underlined spans, each verified against the source page render.
#
#   Dec2023E  = 2023 Dec IntB EliteXSAT (053253c1 / f56bac17, byte-identical),
#               R&W Module 1 -- Dunbar q6 p.5, Johnson q7 p.6, Gregory q8 p.6
#   Dec2023_12A = 2023 Dec IntA EliteXSAT (6baa7e5d), R&W Module 1 p.3 --
#               Hoocak q7, Moran/parks q8
#   Nov2023   = 2023 Nov EliteXSAT (69ee8c05) p.13
#
# Each span is quoted exactly as it appears in the CURRENT passage text, so the
# fix is a pure markup insertion.  Where the same words also appear inside the
# passage's trailing "(Underlined sentence: ...)" note, only the FIRST (body)
# occurrence is wrapped -- asserted below.
# ---------------------------------------------------------------------------
UNDERLINES = {
    "e534f4ce-d32e-4fdb-90ff-b1445ecfd878": (
        "Turning away from landscapes painted in an expressionist style—a style "
        "that often involves using fluid, distorted shapes and thick, textured "
        "brushstrokes to express the artist's subjective experience of reality—"
        "Johnson began painting portraits of Black Americans in a bold new way."
    ),
    "46dc9715-803e-401f-9043-791ccd0f50b0": (
        "Now the house is a museum dedicated to Dunbar's life and writings."
    ),
    "8ab77272-90b5-4547-8125-f5196e27164c": (
        "like a flock of crows on seed potatoes"
    ),
    "5ed97e52-2471-4d43-b0c4-de66a9843902": (
        'In this case, the element "para" in paras gets repeated in paraparač.'
    ),
    "618cdc97-9c2b-4c3d-ba86-e1ce405deee0": (
        "was much lower than"
    ),
    # Nov 2023 p.13: the underline runs from "that" to the end of the sentence.
    "f7af0f2a-a574-4029-a3cb-dcbe46380e6e": (
        "that there were more medicine and health research topics submitted in "
        "2019 than in any other year."
    ),
}

NOTES = {
    "e534f4ce-d32e-4fdb-90ff-b1445ecfd878":
        "2023 Dec IntB EliteXSAT p.6 (R&W M1 q7): the underline runs from "
        "\"Turning away\" to \"bold new way.\" inclusive of the final period.",
    "46dc9715-803e-401f-9043-791ccd0f50b0":
        "2023 Dec IntB EliteXSAT p.5 (R&W M1 q6): whole sentence \"Now the "
        "house is a museum...writings.\" is underlined, final period included.",
    "8ab77272-90b5-4547-8125-f5196e27164c":
        "2023 Dec IntB EliteXSAT p.6 (R&W M1 q8): the underline covers the "
        "simile only - \"like a flock of crows on seed potatoes\" - and stops "
        "before the closing period.",
    "5ed97e52-2471-4d43-b0c4-de66a9843902":
        "2023 Dec IntA EliteXSAT p.3 (R&W M1 q7): the underline spans the whole "
        "sentence \"In this case...paraparač.\", final period included.",
    "618cdc97-9c2b-4c3d-ba86-e1ce405deee0":
        "2023 Dec IntA EliteXSAT p.3 (R&W M1 q8): only the three words \"was "
        "much lower than\" are underlined.",
}

PLACEHOLDER = re.compile(r"<p><em>\[Graph/figure not available[^]]*\]</em></p>")


def strip_u(s):
    return s.replace("<u>", "").replace("</u>", "")


def check_underline(original, fixed):
    assert fixed.count("<u>") == 1, "expected exactly one <u>"
    assert fixed.count("</u>") == 1, "expected exactly one </u>"
    assert fixed.index("<u>") < fixed.index("</u>"), "tags out of order"
    assert strip_u(fixed) == original, "stripping <u> did not restore the original"


def check_figure(fixed):
    for tag in ("p", "strong", "table", "tr", "th", "td", "u"):
        o = len(re.findall(r"<%s[ >]" % tag, fixed))
        c = len(re.findall(r"</%s>" % tag, fixed))
        assert o == c, f"unbalanced <{tag}>: {o} open, {c} close"
    for tbl in re.findall(r"<table.*?</table>", fixed, re.S):
        widths = {len(re.findall(r"<t[hd][ >]", row))
                  for row in re.findall(r"<tr>.*?</tr>", tbl, re.S)}
        assert len(widths) == 1, f"table is not rectangular: row widths {widths}"


def main():
    defects = {d["id"]: d for d in json.load(open(DEFECTS))}
    charts = json.load(open(CHARTS))
    fixes, failed = [], []

    # ---------------------------------------------------------------- underlines
    for qid, span in UNDERLINES.items():
        d = defects[qid]
        p = d["passage"]
        if p.count(span) < 1:
            failed.append({"id": qid, "reason": "underlined span not found verbatim "
                                                "in the current passage"})
            continue
        fixed = p.replace(span, f"<u>{span}</u>", 1)
        d["_fixed_underline"] = fixed
        if qid != "f7af0f2a-a574-4029-a3cb-dcbe46380e6e":
            check_underline(p, fixed)
            fixes.append({
                "id": qid,
                "passage": fixed,
                "kind": "underline",
                "note": NOTES[qid],
            })

    # -------------------------------------------------------------------- figures
    # 1. Test 3 M2 Hard q12 (May p.17) -- the urban-agriculture ranking table.
    qid = "5d220a8d-713b-4bc5-acd6-2f680a0ffd67"
    d = defects[qid]
    tbl = table(
        ["Social or ecological service", "Project leaders", "Stakeholders",
         "General public"],
        [["improvement of attitudes and outlooks", "8", "1", "4"],
         ["provision of food", "4", "15", "8"],
         ["provision of raw materials", "22", "25", "15"],
         ["improvement of physical health", "5", "4", "7"],
         ["enhancement of pollination", "1", "7", "12"]],
    )
    body = PLACEHOLDER.sub("", d["passage"]).strip()
    fixed = figure_block(
        "Ranking of Environmental and Sociocultural Benefits of Urban "
        "Agriculture (scale of 1 to 25; 1=highest)", tbl) + body
    check_figure(fixed)
    fixes.append({
        "id": qid, "passage": fixed, "kind": "figure",
        "note": ("2023 May EliteXSAT p.17: real 5-row table recovered from the "
                 "embedded bitmaps (pdfimages), values exact; the source spells "
                 "the last row \"pullination\", corrected to \"pollination\" "
                 "(no answer choice refers to that row)."),
    })

    # 2. Test 3 M2 Easy q12 (March p.7) -- women judges line graph.
    qid = "2abe301e-35f7-41d2-8dec-1b9f02b5468a"
    d = defects[qid]
    fixed = figure_block(
        "Women Judges and Magistrates on High Courts, 2009–2013",
        img(charts["judges"],
            "Line graph of the number of women judges and magistrates on the "
            "high courts of Slovenia, Finland and the Dominican Republic, "
            "2009 to 2013."),
    ) + d["passage"]
    check_figure(fixed)
    fixes.append({
        "id": qid, "passage": fixed, "kind": "figure",
        "note": ("2023 March EliteXSAT p.7: graph was missing entirely; "
                 "redrawn from pixel-measured values Slovenia 4/4/5/5/5, "
                 "Finland 7/6/6/7/7, Dominican Republic 5/5/8/4/4."),
    })

    # 3. Test 4 M2 Easy q11 (Nov p.13) -- science-fair line graph AND the
    #    underlined claim, which this question needs both of.
    qid = "f7af0f2a-a574-4029-a3cb-dcbe46380e6e"
    d = defects[qid]
    body = PLACEHOLDER.sub("", d["_fixed_underline"]).strip()
    check_underline(PLACEHOLDER.sub("", d["passage"]).strip(), body)
    fixed = figure_block(
        "Total Science Research Submissions by Topic, 2016–2019",
        img(charts["science_fair"],
            "Line graph of the number of science fair submissions in cellular "
            "and molecular biology, physics and space science, medicine and "
            "health, and animal science, 2016 to 2019."),
    ) + body
    check_figure(fixed)
    fixes.append({
        "id": qid, "passage": fixed, "kind": "figure",
        "note": ("2023 Nov EliteXSAT p.13: BOTH defects in one question - graph "
                 "redrawn from pixel-measured values (cellular 200/300/280/280, "
                 "physics 95/90/87/100, medicine 220/220/224/286, animal "
                 "50/50/50/90) and the claim \"that there were more medicine "
                 "and health...\" wrapped in <u>, matching the source underline."),
    })

    out = fixes if not failed else fixes + [{"failed": failed}]
    with open(OUT, "w") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print(f"wrote {OUT}: {len(fixes)} fixes, {len(failed)} failed")
    for f in fixes:
        print(f"  {f['id']}  {f['kind']}")
    for f in failed:
        print(f"  FAILED {f['id']}: {f['reason']}")


if __name__ == "__main__":
    sys.exit(main())
