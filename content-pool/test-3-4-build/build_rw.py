import json, re

SRC = "/home/user/SAT-Project/content-pool/test-3-4-5-reading-writing/test345_classified.json"
d = json.load(open(SRC))

DOMAIN_MAP = {
    "Information and Ideas": "INI", "Craft and Structure": "CAS",
    "Expression of Ideas": "EOI", "Standard English Conventions": "SEC",
}
SKILL_MAP = {
    "Central Ideas and Details": "INI-CI", "Inferences": "INI-IE", "Command of Evidence": "INI-CE",
    "Words in Context": "CAS-WV", "Text Structure and Purpose": "CAS-TS", "Cross-Text Connections": "CAS-CT",
    "Rhetorical Synthesis": "EOI-RS", "Transitions": "EOI-TR",
    "Boundaries": "SEC-BS", "Form, Structure, and Sense": "SEC-FS",
}

TH = 'style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;"'
TD = 'style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;"'


def html_table(headers, rows):
    th = "".join(f"<th {TH}>{h}</th>" for h in headers)
    trs = ""
    for r in rows:
        tds = "".join(f"<td {TD}>{c}</td>" for c in r)
        trs += f"<tr>{tds}</tr>"
    return f'<table style="border-collapse:collapse;margin:0.75rem 0;"><tr>{th}</tr>{trs}</table>'


# Manually built table replacements: (testKey, idx) -> (title, headers, rows, prefix_text, suffix_text)
TABLE_OVERRIDES = {
    ("test3|RW_M1", 11): dict(
        headers=["Researchers", "Crop", "Tilling yield (kg/ha)", "No-tilling yield (kg/ha)"],
        rows=[
            ["Bharat Sharma Achayara and colleagues", "soybeans", "3,062", "2,670"],
            ["Adrian Gracia-Romero and colleagues", "maize", "2,420", "2,990"],
            ["Daniel Jug and colleagues", "winter wheat", "4,860", "3,910"],
            ["Min Huang and colleagues", "rice", "2,534", "5,226"],
        ],
        title="Studies of the Effects of Tilling vs. No Tilling on Crop Yields",
        suffix="Danijel Jug and colleagues found that tilling—the practice of turning soil with hoes, plows, or other machines before planting crops—was associated with an increased yield of winter wheat. But some studies of other crops have found the opposite effect, for example ____",
    ),
    ("test4|RW_M1", 10): dict(
        headers=["Plant", "State", "Mode", "Average power generation (MWh/yr)", "Water source"],
        rows=[
            ["Scanlon", "Minnesota", "run-of-river", "7,511", "St. Louis River"],
            ["Kansas River", "Kansas", "run-of-river", "15,345", "Kansas River"],
            ["Squa Pan Hydro Station", "Maine", "peaking", "881", "Squa Pan Stream"],
            ["Great Falls", "Tennessee", "peaking", "124,392", "Caney Fork River"],
        ],
        title="US Hydroelectric Power Plants, 2019",
        suffix="A run-of-river hydroelectric power plant, as the name suggests, uses the natural flow of a water source to generate electricity but is unable to start or stop that flow through its generators. In contrast, a peaking hydroelectric power plant (used when demand for electricity peaks) controls the flow of water through its generators: starting flow when demand is high enough, stopping it when demand is too low, and otherwise regulating it to keep pace with changing electricity needs. Although peaking plants do not typically operate continuously as run-of-river plants do, peaking plants can generate more megawatt-hours of power per year (MWh/yr) than some run-of-river plants. For example, the ______",
    ),
    ("test4|RW_M1", 11): dict(
        headers=["Industry", "Approximate total contribution by industry", "Number of people employed by industry", "Average contribution per employee by industry"],
        rows=[
            ["Administration/waste", "$5,830,600,000", "96,964", "$60,132"],
            ["Construction", "$6,797,300,000", "77,247", "$87,994"],
            ["Transportation/warehousing", "$12,414,600,000", "52,891", "$234,720"],
            ["Tribal economic activity", "$7,312,400,000", "51,674", "$141,510"],
        ],
        title="Impact of Four Key Industries on Oklahoma Economy in 2017",
        suffix="The Cherokee Nation, the Quapaw Tribe, and the more than thirty other tribes in Oklahoma operate numerous businesses and generate billions of dollars in revenue. An economics student is researching the tribes' collective activity as a single industry. The student wants to compare the average amount that industry contributed per employee to Oklahoma's economy with the average amount contributed per employee by three other industries. Looking at the table, the student finds that tribal economic activity contributed over $141,000 per employee, on average, ranking it _____",
    ),
    ("test4|RW_M2_EASY", 8): dict(
        headers=["Title", "Lifetime gross earnings", "Opening weekend box office gross earnings", "US release date", "Director", "Oscar nominated?"],
        rows=[
            ["Crouching Tiger, Hidden Dragon", "$128,078,872", "$663,205", "December 8, 2000", "Ang Lee", "Yes"],
            ["Eat Drink Man Woman", "$7,294,403", "$155,512", "August 3, 1994", "Ang Lee", "Yes"],
            ["Iron Monkey", "$11,694,904", "$6,014,653", "October 12, 2001", "Yuen Woo-ping", "No"],
            ["The Girl Who Played with Fire", "$7,638,241", "$904,998", "July 9, 2010", "Daniel Alfredson", "No"],
        ],
        title="Highest-Grossing Films in a Language Other than English at US Box Office",
        suffix="Many films in a language other than English grow to be financially successful over the course of their time in movie theaters in the United States, but some become immediate successes in their opening weekends. Such success is driven by many factors like advertising, genre popularity, and the fame of the actors and directors. A student claims that opening weekend earnings can reliably predict whether a film will be nominated for an Oscar: films that draw large audiences at the beginning of their release are the most likely contenders to earn these coveted award nominations.",
    ),
    ("test4|RW_M2_EASY", 9): dict(
        headers=["Pyramid", "Country", "Height (meters)", "Age (years before present)"],
        rows=[
            ["The Pyramid of the Sun", "Mexico", "71.2", "2,100"],
            ["The Pyramid of Djedefre", "Egypt", "67", "4,500 to 4,600"],
            ["The Pyramid of Userkaf", "Egypt", "49", "4,400 to 4,500"],
            ["El Castillo", "Belize", "40", "1,100 to 1,400"],
        ],
        title="Pyramids in Egypt and the Americas",
        suffix="A student is writing an essay about four pyramids for a history class and wants to note how long ago each pyramid was built and how tall each pyramid is. Consulting the table, the student finds that el Castillo was built 1,100 to 1,400 years ago and is _____",
    ),
    ("test4|RW_M2_HARD", 8): dict(
        headers=["Lake", "Latitude (degrees)", "1980-81", "1985-86", "1990-91", "1995-96", "2000-01", "2005-06"],
        rows=[
            ["Kalmarinjärvi", "62.79", "198", "172", "175", "184", "131", "152"],
            ["Lake Neusiedl", "47.82", "77", "86", "87", "128", "50", "104"],
            ["Mirror Lake", "43.94", "122", "129", "125", "136", "141", "119"],
        ],
        title="Days per Winter That Lakes Have Surface Ice",
        suffix="It is common for freshwater lakes near or above a latitude of 45° north of the equator, like Lake Mjøsa in Norway, to accumulate surface ice in winter. The amount and duration of ice depends on many factors, including local weather conditions as well as the lake's depth, volume, and surface area, but a climate researcher claims that some lakes in these latitudes have seen a decline in the duration of ice between the early 1980s and the mid-2000s.",
    ),
    ("test4|RW_M2_HARD", 9): dict(
        headers=["Lake", "Latitude (degrees)", "1980-81", "1985-86", "1990-91", "1995-96", "2000-01", "2005-06"],
        rows=[
            ["Kalmarinjärvi", "62.79", "198", "172", "175", "184", "131", "152"],
            ["Lake Neusiedl", "47.82", "77", "86", "87", "128", "50", "104"],
            ["Mirror Lake", "43.94", "122", "129", "125", "136", "141", "119"],
        ],
        title="Days per Winter That Lakes Have Surface Ice",
        suffix="It is common for freshwater lakes near or above a latitude of 45° north of the equator, like Lake Mjøsa in Norway, to accumulate surface ice in winter. The amount and duration of ice depends on many factors, including local weather conditions as well as the lake's depth, volume, and surface area, but a climate researcher claims that some lakes in these latitudes have seen a decline in the duration of ice between the early 1980s and the mid-2000s.",
    ),
}


def convert_underline(text):
    def repl_inline(m):
        return f"<u>{m.group(1)}</u>"
    text = re.sub(r"\[UNDERLINED[^:\]]*:\s*([^\]]+)\]", repl_inline, text)
    while re.search(r"\[UNDERLINED[^:\]]*:\]", text):
        m = re.search(r"\[UNDERLINED[^:\]]*:\]", text)
        rest = text[m.end():]
        sm = re.match(r"\s*(.+?[\.\!\?])(\s|$)", rest)
        if sm:
            sentence = sm.group(1)
            replacement = " <u>" + sentence + "</u>"
            text = text[:m.start()] + replacement + rest[sm.end():]
        else:
            text = text[:m.start()] + text[m.end():]
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text


def convert_asterisks(text):
    return re.sub(r"\*([^*\n]+)\*", r"<em>\1</em>", text)


def convert_text12(passage):
    m = re.match(r"^\s*Text 1\s+(.*?)\s+Text 2\s+(.*)$", passage, re.S)
    if not m:
        return None
    t1, t2 = m.group(1).strip(), m.group(2).strip()
    return f"<p><strong>Text 1</strong></p><p>{t1}</p><p><strong>Text 2</strong></p><p>{t2}</p>"


def convert_bullets(passage):
    m = re.match(r"^\s*Bulleted notes:\s*(.*)$", passage, re.S)
    if not m:
        return None
    body = m.group(1).strip()
    items = re.split(r"\s*-\s+", body)
    items = [i.strip() for i in items if i.strip()]
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f"<ul>{lis}</ul>"


def build_passage_html(test_key, idx, q):
    key = (test_key, idx)
    if key in TABLE_OVERRIDES:
        t = TABLE_OVERRIDES[key]
        table_html = html_table(t["headers"], t["rows"])
        return f'<p><strong>{t["title"]}</strong></p>{table_html}<p>{t["suffix"]}</p>'

    passage = q.get("passage", "")
    passage = convert_underline(passage)
    passage = convert_asterisks(passage)

    t12 = convert_text12(passage)
    if t12:
        return t12

    bullets = convert_bullets(passage)
    if bullets:
        return bullets

    diagram = (q.get("diagram") or "").strip()
    note = ""
    if diagram:
        clean = re.sub(r"^\[DIAGRAM:\s*", "", diagram).rstrip("]")
        note = f'<p><em>[Graph/figure not available in this environment -- described here for reference: {clean}]</em></p>'

    return f"<p>{passage}</p>" + note


def build_question(test_key, idx, q):
    stem = convert_asterisks(q.get("stem", ""))
    choices = []
    for c in q["choices"]:
        choices.append({"label": c["label"], "content": convert_asterisks(c["content"])})
    domain_code = DOMAIN_MAP[q["domain"]]
    skill_code = SKILL_MAP[q["skill"]]
    return {
        "passage": build_passage_html(test_key, idx, q),
        "stem": stem,
        "choices": choices,
        "correct": q["correct"],
        "domain": domain_code,
        "skill": skill_code,
        "_source": q.get("source"), "_num": q.get("num"),
    }


if __name__ == "__main__":
    out = {}
    for k in ["test3|RW_M1", "test3|RW_M2_EASY", "test3|RW_M2_HARD",
              "test4|RW_M1", "test4|RW_M2_EASY", "test4|RW_M2_HARD",
              "test5|RW_M1", "test5|RW_M2_EASY", "test5|RW_M2_HARD"]:
        out[k] = [build_question(k, i, q) for i, q in enumerate(d[k])]
    json.dump(out, open("rw_built.json", "w"), indent=2, ensure_ascii=False)
    for k, arr in out.items():
        print(k, len(arr))
