#!/usr/bin/env python3
"""
Apply the HTML formatting pass to Test 5's banked Reading & Writing content.

The reserved pool in content-pool/test-3-4-5-reading-writing/ is raw
pre-formatting text. This converts it to the same markup Test 1 and Test 2 use
(see the HTML conventions in CLAUDE.md):

  * "Bulleted notes: - a - b"  ->  real <ul><li> markup
  * pipe-delimited data        ->  a real <table> with the standard style block
  * "Text 1 ... Text 2 ..."    ->  one passage with <strong> labels
  * [UNDERLINED: x]            ->  <u>x</u>
  * *italics*                  ->  <em>italics</em>

It also drops the questions that cannot be shipped honestly -- ones whose
figure was never captured, and ones whose own transcript flags the text as an
inference from an obscured source image.

Run:  python3 format_rw.py
Out:  test5_rw_formatted.json  (+ a report of what was dropped)
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
POOL = os.path.join(HERE, "..", "test-3-4-5-reading-writing", "test345_classified.json")

TABLE_OPEN = '<table style="border-collapse:collapse;margin:0.75rem 0;">'
TH = ('<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;'
      'text-align:left;background:#F4F6F8;">')
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">'

# Questions that cannot be shipped. Keyed (module, index) with the reason.
UNUSABLE = {
    ("test5|RW_M1", 10): "Line graph (Costa Rica forest patch size) — the source PDF was not "
                         "kept, so the figure cannot be produced and the question would have to "
                         "describe its own graph in prose. Rule 3 forbids that.",
    ("test5|RW_M1", 15): "Boundaries question whose choices A and B differ only by a comma that "
                         "a watermark obscured in the source image. The transcript says so "
                         "itself; the distinction cannot be verified.",
    ("test5|RW_M1", 18): "Choice D was hidden behind a cursor icon in the source capture and was "
                         "transcribed by inference. Unverifiable.",
    ("test5|RW_M2_EASY", 7): "Line graph (women judges 2009–2013) — source PDF not kept, same "
                             "problem as RW_M1 idx10.",
}



# --- Hand-built tables ------------------------------------------------------
# The source stores these on one line with implicit row breaks, e.g.
# "... | Fungi | Insects Lithuania | 8 | ...", where "Insects Lithuania" is the
# last header cell running straight into the first row label. No regex can split
# that reliably, so all five are written out by hand and each one's answer was
# re-checked against the data below.
HAND_TABLES = {
 ("test5|RW_M1", 8): (
   'Numbers of the 23 Non-native Tree Species Reported and the Insect and Fungus Threats to Them',
   ["Country", "Trees", "Fungi", "Insects"],
   [["Lithuania", "8", "12", "7"], ["Poland", "10", "25", "105"], ["Austria", "13", "51", "50"]]),
 ("test5|RW_M1", 9): (
   'Studies of the Effects of Tilling vs. No Tilling on Crop Yields',
   ["Authors", "Crop", "Crop yield with tilling (kilograms per hectare)",
    "Crop yield with no tilling (kilograms per hectare)"],
   [["Salem Alhajj Ali and colleagues", "winter wheat", "3,700", "5,300"],
    ["Nayasha Kafesu and colleagues", "maize", "3,078", "3,574"],
    ["G.F. Botta and colleagues", "soybeans", "3,300", "2,700"],
    ["Laila Nazirah and colleagues", "rice", "4,370", "2,450"]]),
 ("test5|RW_M2_EASY", 8): (
   'Dated Ages of Lunar Samples from Select Missions',
   ["Mission name", "Year", "Landing site",
    "Approximate age of lunar samples (billions of years)"],
   [["Apollo 11", "1969", "Mare Tranquillitatis", "3.6"],
    ["Apollo 15", "1971", "Mare Imbrium", "3.3"],
    ["Apollo 17", "1972", "Mare Serenitatis", "3.8"],
    ["Chang&rsquo;e 5", "2020", "Oceanus Procellarum", "2.0"]]),
 ("test5|RW_M2_HARD", 8): (
   'Days per Winter That Lakes Have Surface Ice',
   ["Lake", "Latitude (degrees)", "1980-81", "1985-86", "1990-91",
    "1995-96", "2000-01", "2005-06"],
   [["Spirit Lake", "43.46", "102", "135", "121", "134", "147", "126"],
    ["Lake Kegonsa", "42.97", "94", "116", "104", "113", "124", "101"],
    ["N&auml;ckten", "62.913", "177", "168", "144", "174", "133", "134"]]),
 ("test5|RW_M2_HARD", 9): (
   'Total Areas of Five Tribal Nations around the United States',
   ["Tribal nation", "Location", "Area (square miles)"],
   [["Tohono O&rsquo;odham Nation", "Arizona", "4,453"],
    ["Crow Tribe", "Montana", "3,606"],
    ["Leech Lake Band of Ojibwe", "Minnesota", "1,311"],
    ["Yakama Nation", "Washington", "2,188"],
    ["Muscogee Nation", "Oklahoma", "4,867"]]),
}


def build_table(title, headers, rows):
    return (f'<p><strong>{title}</strong></p>' + TABLE_OPEN + "<thead><tr>"
            + "".join(f"{TH}{h}</th>" for h in headers) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"{TD}{c}</td>" for c in r) + "</tr>" for r in rows)
            + "</tbody></table>")


# The narrative that follows each table in the source string, written out so no
# regex has to guess where the inlined table data ends and the prose begins.
TABLE_PROSE = {
 ("test5|RW_M1", 8):
   "Elisabeth P&ouml;tzelsberger and colleagues gathered data on 23 non-native tree species "
   "grown in Europe. They analyzed reports from Austria, Poland, and Lithuania about the number "
   "of these species grown in those countries as well as the numbers of insect and fungus "
   "species that damage those trees. The researchers concluded that in only one of these "
   "countries are there more insect species than fungus species that pose risks to these trees.",
 ("test5|RW_M1", 9):
   "Laila Nazirah and colleagues found that tilling&mdash;the practice of turning soil with "
   "hoes, plows, or other machines before planting crops&mdash;was associated with an increased "
   "yield of rice. But some studies of other crops have found the opposite effect, raising the "
   "question of whether the increase in yield found by Nazirah and colleagues is specific to "
   "their study crop. However, this doesn&rsquo;t seem to be the case: _____",
 ("test5|RW_M2_EASY", 8):
   "The Apollo program missions were spaceflights to the moon led by the United States during "
   "the 1960s and 1970s during which astronauts collected some samples of the moon&rsquo;s "
   "surface. More recently, China launched the Chang&rsquo;e 5 mission, which returned "
   "additional lunar surface samples. Researchers have analyzed and dated each of the samples, "
   "concluding that the lunar samples collected during the Chang&rsquo;e 5 mission are "
   "significant because _____",
 ("test5|RW_M2_HARD", 8):
   "It is common for freshwater lakes near or above a latitude of 45&deg; north of the equator, "
   "like Lake Stechlin in Germany, to accumulate surface ice in winter. A study from 1980 to "
   "2006 showed that, in general, the number of days per winter that such lakes have measurable "
   "amounts of surface ice is declining. However, a researcher claimed that some lakes have "
   "instead seen an increase in the duration of ice.",
 ("test5|RW_M2_HARD", 9):
   "In terms of total area, the Muscogee Nation is one of the largest tribal nations in the "
   "United States. It covers 4,867 square miles in what is now eastern Oklahoma. In comparison, "
   "the total area of the Leech Lake Band of Ojibwe in Minnesota is only _____",
}


def bullets_to_html(text):
    """'Bulleted notes: - a - b - c' -> intro plus a real <ul>."""
    m = re.search(r"(?is)\bbulleted notes\b\s*:?\s*(.*)$", text)
    if not m:
        return None
    head = text[: m.start()].strip()
    items = [s.strip(" .;") for s in re.split(r"\s*[-•]\s+", m.group(1)) if s.strip(" .;")]
    if len(items) < 2:
        return None
    lis = "".join(f"<li>{i}</li>" for i in items)
    intro = f"<p>{head}</p>" if head else "<p>While researching a topic, a student has taken the following notes:</p>"
    return f"{intro}<ul>{lis}</ul>"


def pipes_to_table(text):
    """Pipe-delimited rows -> a real <table>; returns (html, leftover_prose)."""
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    rows = [l for l in lines if l.count("|") >= 1]
    if len(rows) < 2:
        return None, text
    cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows]
    width = max(len(r) for r in cells)
    cells = [r + [""] * (width - len(r)) for r in cells]
    head, body = cells[0], cells[1:]
    html = (TABLE_OPEN + "<thead><tr>"
            + "".join(f"{TH}{c}</th>" for c in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"{TD}{c}</td>" for c in r) + "</tr>" for r in body)
            + "</tbody></table>")
    prose = " ".join(l for l in lines if l not in rows).strip()
    return html, prose


def split_texts(text):
    """A Cross-Text passage stays ONE passage, with <strong> labels."""
    if not (re.search(r"\bText ?1\b", text) and re.search(r"\bText ?2\b", text)):
        return None
    out = re.sub(r"\bText ?1\b\s*:?\s*", "</p><p><strong>Text 1</strong></p><p>", text, count=1)
    out = re.sub(r"\bText ?2\b\s*:?\s*", "</p><p><strong>Text 2</strong></p><p>", out, count=1)
    return ("<p>" + out + "</p>").replace("<p></p>", "")


def inline_marks(text):
    text = re.sub(r"\[UNDERLINED[^:\]]*:\s*(.*?)\]", r"<u>\1</u>", text, flags=re.S)
    text = re.sub(r"(?<!\w)\*([A-Za-z][^*]{1,60})\*(?!\w)", r"<em>\1</em>", text)
    return text


def to_html(passage):
    if not passage or not passage.strip():
        return ""
    p = inline_marks(passage.strip())

    b = bullets_to_html(p)
    if b:
        return b

    t = split_texts(p)
    if t:
        return t

    if p.count("|") >= 4:
        table, prose = pipes_to_table(p)
        if table:
            return (f"<p>{prose}</p>{table}" if prose else table)

    paras = [x.strip() for x in re.split(r"\n\s*\n|\n", p) if x.strip()]
    return "".join(f"<p>{x}</p>" for x in paras)


def main():
    pool = json.load(open(POOL))
    out, dropped = {}, []
    for mod in ("test5|RW_M1", "test5|RW_M2_EASY", "test5|RW_M2_HARD"):
        keep = []
        for i, q in enumerate(pool[mod]):
            if (mod, i) in UNUSABLE:
                dropped.append((mod, i, q["skill"], UNUSABLE[(mod, i)]))
                continue
            passage_html = to_html(q.get("passage", ""))
            if (mod, i) in HAND_TABLES:
                title, headers, rows = HAND_TABLES[(mod, i)]
                prose = TABLE_PROSE[(mod, i)]
                passage_html = build_table(title, headers, rows) + f"<p>{prose}</p>"
            keep.append({
                "source": q["source"],
                "sourceNum": q["num"],
                "type": q["type"],
                "passageHtml": passage_html,
                "stem": inline_marks((q.get("stem") or "").strip()),
                "choices": [{"label": c["label"], "content": inline_marks(c["content"])}
                            for c in q["choices"]],
                "correct": q["correct"],
                "domain": q["domain"],
                "skill": q["skill"],
                "diagramNote": q.get("diagram", ""),
            })
        out[mod] = keep

    with open(os.path.join(HERE, "test5_rw_formatted.json"), "w") as fh:
        json.dump(out, fh, indent=1)

    print("Formatted:")
    for m, qs in out.items():
        tables = sum(1 for q in qs if "<table" in q["passageHtml"])
        lists = sum(1 for q in qs if "<ul>" in q["passageHtml"])
        print(f"  {m:22} {len(qs):3} kept   tables={tables} lists={lists}")
    print(f"\nDropped {len(dropped)} unusable:")
    for m, i, skill, why in dropped:
        print(f"  {m} idx{i} ({skill}): {why[:96]}")
    need = {m: 27 - len(qs) for m, qs in out.items()}
    print("\nTop-up still required:", need, "=", sum(need.values()), "questions")


if __name__ == "__main__":
    main()
