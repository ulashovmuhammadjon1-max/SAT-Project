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
    r"^\s*Topic\s*$|Suggested Skill|CLASS PERIODS|SAMPLE INSTRUCTIONAL|^\s*UNIT\s*$",
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
    s = re.split(r"\s{3,}", s.strip())[0]
    s = SKILL.split(s)[0]
    s = re.sub(r"\s+", " ", s).strip()
    # Titles never end in a lone digit-dot-letter fragment or a page number.
    s = re.sub(r"\s*\d+\.[A-Z]$", "", s).strip()
    return s


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
                topics[current] = (topics[current] + " " + tail).strip()
            else:
                current = None
    return topics, order


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
