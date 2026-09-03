"""Extract the topic list for an AP science subject from its CED text dump.

    python3 extract_topics.py /tmp/ced/BIOLOGY.txt BIOLOGY

Reads the UNIT AT A GLANCE tables rather than the TOPIC pages. The topic pages
are laid out in two interleaved columns, so a topic's title arrives split
across lines with skill text wedged between the halves; the glance tables put
the number and the title together in the left column, which is the only place
in the document where they are adjacent.

A title still wraps onto continuation lines, and the right column bleeds into
the same text row. The rules below are what survived reading real output from
all seven science CEDs:

  * A topic starts at `N.M ` in the left column. Everything after it on that
    line up to the skill column is the first line of the title.
  * The skill column begins at a code like `2.A` or `1.A` followed by a
    capital letter, so the title is cut there.
  * A continuation line belongs to the title only if it is indented under the
    title (not the number), holds no skill code, and is not one of the
    boilerplate lines the tables repeat.

Everything is checked afterwards: numbering must be contiguous within a unit
starting at 1, and every title must be non-empty and free of stray skill text.
A subject that fails those checks prints the problem rather than writing a
file, because a silently mangled topic list would be baked into the course
outline students navigate.
"""
import json
import re
import sys

# The skill column, e.g. "2.A Describe..." or "6.E Predict...". Requires the
# letter to be followed by whitespace-then-capital so a title like "1.A" alone
# cannot be mistaken for it.
SKILL = re.compile(r"\s{2,}\d\.[A-Z]\b|\s{2,}\d\.[A-Z]\s+[A-Z]")
TOPIC_START = re.compile(r"^(\s{0,24})(\d{1,2})\.(\d{1,2})\s+(\S.*)$")
NOISE = re.compile(
    r"Go to AP Classroom|Progress Check|Review the results|Course and Exam Description|"
    r"Return to Table of Contents|College Board|UNIT AT A GLANCE|Class Periods|"
    r"^\s*Topic\s*$|Suggested Skill|CLASS PERIODS|SAMPLE INSTRUCTIONAL|^\s*UNIT\s*$|"
    # Section headers that sit at the SAME indent as a topic title on the
    # TOPIC pages, so the indent rule alone does not exclude them.
    r"Required Course Content|AVAILABLE RESOURCES|SUGGESTED SKILL|ENDURING UNDERSTANDING|"
    r"LEARNING OBJECTIVE|ESSENTIAL KNOWLEDGE",
    re.IGNORECASE,
)


def clean(s: str) -> str:
    """Take the LEFT column only.

    These are two-column tables and pdftotext -layout preserves the gap, so the
    column boundary is a run of three or more spaces. Cutting there FIRST is
    what matters: the skill column wraps onto the same physical lines as the
    title, and its continuation carries no skill code to split on, which is how
    "Hydrogen Bonding" became "Hydrogen Bonding biological concepts and
    processes."
    """
    s = "".join(ch for ch in s if ord(ch) >= 32 or ch == "\t")
    s = re.split(r"\s{3,}", s.strip())[0]
    s = SKILL.split(s)[0]
    s = re.sub(r"\s+", " ", s).strip()
    # Titles never end in a lone digit-dot-letter fragment or a page number.
    s = re.sub(r"\s*\d+\.[A-Z]$", "", s).strip()
    return s


def dedupe_words(s: str) -> str:
    """Collapse an immediately repeated word or word pair.

    A TOPIC page prints the title as a heading and again in the body, so
    joining its lines repeats the tail: "Introduction to Macromolecules
    Macromolecules". This has to run AFTER the join -- the pieces are clean
    individually and only the concatenation is wrong, which is why doing it
    inside clean() had no effect.
    """
    s = re.sub(r"\b(\w+)(\s+\1)\b", r"\1", s, flags=re.IGNORECASE)
    s = re.sub(r"\b(\w+\s+\w+)(\s+\1)\b", r"\1", s, flags=re.IGNORECASE)
    return s.strip()


def extract(path: str):
    lines = open(path, encoding="utf-8", errors="replace").read().split("\n")
    inside = False
    topics: dict[str, str] = {}
    order: list[str] = []
    current: str | None = None
    col = 0

    for raw in lines:
        if "UNIT AT A GLANCE" in raw:
            inside = True
            current = None
            continue
        # A glance table ends at the progress-check footer or the next section.
        if inside and re.search(r"Go to AP Classroom|SAMPLE INSTRUCTIONAL", raw):
            inside = False
            current = None
            continue
        if not inside:
            continue
        if NOISE.search(raw):
            continue

        m = TOPIC_START.match(raw)
        if m:
            indent, unit, num, rest = len(m.group(1)), m.group(2), m.group(3), m.group(4)
            code = f"{int(unit)}.{int(num)}"
            title = clean(rest)
            if code not in topics:
                topics[code] = title
                order.append(code)
            current, col = code, indent
            continue

        if current and raw.strip():
            # Continuation of the title: indented under it, no skill code.
            if SKILL.search(raw) or re.match(r"^\s{0,24}\d{1,2}\.\d", raw):
                current = None
                continue
            tail = clean(raw)
            here = len(raw) - len(raw.lstrip())
            # Relative to the topic column: a wrapped title lines up just past
            # the number, while the right-hand column sits far to the right.
            if tail and col < here <= col + 12:
                topics[current] = dedupe_words(topics[current] + " " + tail)
            else:
                current = None
    return topics, order


# `TOPIC 8.7` sometimes shares its line with the right-hand SUGGESTED SKILL
# column, so anything after a wide gap is tolerated and ignored.
TOPIC_PAGE = re.compile(r"^(\s*)TOPIC\s+(\d{1,2})\.(\d{1,2})(?:\s*$|\s{3,}\S.*$)")


def fill_from_topic_pages(path: str, topics: dict[str, str], order: list[str]) -> list[str]:
    """Recover topics the UNIT AT A GLANCE tables leave out.

    Chemistry's unit 8 glance table lists 8.1-8.4, 8.6 and 8.9 and simply omits
    8.5, 8.7, 8.8 and 8.10 -- they appear in the Course at a Glance overview
    and on their own TOPIC pages, but not in the per-unit table this extractor
    reads. So the glance tables are the primary source, because they put the
    number and title adjacent in one column, and the TOPIC pages are the
    fallback for whatever is missing.

    A TOPIC page is `TOPIC N.M` alone on a line, with the title on the lines
    directly beneath at the SAME indent. The surrounding skill and resource
    columns sit at a different indent, which is what makes them separable.
    """
    lines = open(path, encoding="utf-8", errors="replace").read().split("\n")
    added = []
    for i, raw in enumerate(lines):
        m = TOPIC_PAGE.match(raw)
        if not m:
            continue
        code = f"{int(m.group(2))}.{int(m.group(3))}"
        if code in topics:
            continue
        indent = len(m.group(1))
        parts = []
        # The two columns interleave line by line, so the skill column can sit
        # BETWEEN the TOPIC heading and its title -- 8.8's title is four lines
        # below, with "6.D / Provide reasoning to justify / a claim using
        # chemical" in between at a different indent. Lines from the other
        # column are skipped rather than treated as the end of the title.
        for nxt in lines[i + 1 : i + 14]:
            if not nxt.strip():
                continue
            here = len(nxt) - len(nxt.lstrip())
            if abs(here - indent) > 2:
                continue
            if NOISE.search(nxt) or SKILL.search(nxt):
                break
            piece = clean(nxt)
            if piece:
                parts.append(piece)
            if len(parts) >= 3:
                break
        title = dedupe_words(" ".join(x for x in parts if x))
        if title:
            topics[code] = title
            order.append(code)
            added.append(code)
    order.sort(key=lambda c: tuple(int(x) for x in c.split(".")))
    return added


# A title left dangling on a joining word, or reduced to a stub, was cut off by
# a layout the glance pass mishandled -- Chemistry's unit 9 sits in the
# multi-column Course at a Glance, where a class-period digit in the left
# gutter shifts the indent and truncates "Gibbs Free Energy and Thermodynamic
# Favorability" to "Gibbs".
DANGLING = re.compile(r"\b(and|or|of|the|in|for|to|a|an|with|under|between)$", re.IGNORECASE)


def suspect(title: str) -> bool:
    """Only a title left dangling on a joining word is definitely truncated.

    Length is NOT a usable signal: "Hess's Law", "pH and pKa", "Solubility" and
    "Catalysis" are all real, complete AP Chemistry topic titles.
    """
    return bool(DANGLING.search(title))


def repair_from_topic_pages(path: str, topics: dict[str, str]) -> list[str]:
    """Prefer the TOPIC-page title wherever it is longer than the glance one.

    No cleverness about which titles "look" truncated -- truncation only ever
    SHORTENS, so taking the longer of the two independent sources repairs the
    mangled ones and leaves the good ones alone. Chemistry's unit 9 lives in
    the multi-column Course at a Glance, where a class-period digit in the left
    gutter shifts the indent and cuts "Gibbs Free Energy and Thermodynamic
    Favorability" down to "Gibbs".
    """
    probe: dict[str, str] = {}
    fill_from_topic_pages(path, probe, [])
    fixed = []
    for code, old_title in list(topics.items()):
        cand = probe.get(code, "")
        if len(cand) > len(old_title) and not NOISE.search(cand):
            topics[code] = cand
            fixed.append(f"{code}: {old_title!r} -> {cand!r}")
    return fixed


# Titles the layout defeats outright, read by eye from the CED and cited by
# line so the correction is auditable rather than remembered.
#
# Chemistry's unit 9 pages interleave the two columns WITHIN a line -- topic
# 9.1's page reads "Support a claim Introduction" then "to Entropy", with the
# skill sentence and the title sharing one physical row. No indent rule can
# separate that, and guessing is exactly what SOCIAL_BRIEF forbids, so these
# four are transcribed from the Course at a Glance overview instead.
OVERRIDES = {
    "CHEMISTRY": {
        "9.1": "Introduction to Entropy",                      # CED text line 1046
        "9.5": "Free Energy and Equilibrium",                  # lines 1060-1062
        "9.7": "Coupled Reactions",                            # line 1074
        "9.10": "Cell Potential Under Nonstandard Conditions",  # lines 1083-1084
    },
}


def check(topics: dict[str, str]) -> list[str]:
    problems = []
    if len(topics) < 10:
        problems.append(
            f"only {len(topics)} topics parsed -- every AP science CED has dozens, so this is a "
            "layout the extractor did not match, not a small subject"
        )
    units: dict[int, list[int]] = {}
    for code, title in topics.items():
        u, n = (int(x) for x in code.split("."))
        units.setdefault(u, []).append(n)
        if not title:
            problems.append(f"{code}: empty title")
        elif len(title) < 3:
            problems.append(f"{code}: implausibly short title {title!r}")
        elif suspect(title):
            problems.append(f"{code}: title left dangling on a joining word: {title!r}")
        elif re.search(
            r"Suggested Skill|\d\.[A-Z]\s|\bDescribe\b|\bPredict\b|\bExplain\b|"
            r"concepts and processes|one or more components|applied contexts|"
            r"observation, data|biological theories|graphs?\(|, including:",
            title,
        ):
            problems.append(f"{code}: skill text leaked into the title: {title!r}")
    for u, nums in sorted(units.items()):
        nums.sort()
        if nums != list(range(1, len(nums) + 1)):
            problems.append(f"unit {u}: topic numbers are {nums}, not 1..{len(nums)}")
    return problems


def main():
    path, subject = sys.argv[1], sys.argv[2]
    topics, order = extract(path)
    added = fill_from_topic_pages(path, topics, order)
    if added:
        print(f"(recovered {len(added)} topic(s) from TOPIC pages: {', '.join(added)})")
    fixed = repair_from_topic_pages(path, topics)
    if fixed:
        print(f"(repaired {len(fixed)} truncated title(s))")
        for f in fixed:
            print("   ", f)
    # Applied LAST: an override is the hand-read ground truth and must not be
    # overwritten by either automated pass.
    for code, title in OVERRIDES.get(subject, {}).items():
        if topics.get(code) != title:
            print(f"(override {code}: {topics.get(code)!r} -> {title!r})")
            topics[code] = title
    problems = check(topics)
    print(f"{subject}: {len(topics)} topics across {len({c.split('.')[0] for c in topics})} units")
    for code in order:
        print(f"  {code:6s} {topics[code]}")
    if problems:
        print(f"\n{len(problems)} PROBLEM(S) — not writing a file:")
        for p in problems:
            print("  -", p)
        raise SystemExit(1)
    out = {"_units": sorted({int(c.split(".")[0]) for c in topics})}
    out.update({c: topics[c] for c in order})
    dest = f"{subject}_topics.json"
    json.dump(out, open(dest, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"\nwrote {dest}")


if __name__ == "__main__":
    main()
