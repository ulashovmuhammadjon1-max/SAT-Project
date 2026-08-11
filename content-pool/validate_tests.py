#!/usr/bin/env python3
"""
Independent structural validation of assembled test JSON files.

Each build agent verifies its own test. This checks the same files again from
the outside, because the failures that actually reach production are the ones a
build's own verifier was never written to look for — Test 6 shipped 18 broken
Math questions precisely because every authored question passed and nothing
read the content that came from elsewhere.

Nothing here trusts a build script: it reads the assembled JSON, which is what
the inserter actually writes to the database.

    python3 validate_tests.py                 # every test*.json under content-pool
    python3 validate_tests.py 22 23 24        # only those test numbers

Exits non-zero if any check fails.
"""
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))

MODULES = {
    "RW_M1": 27, "RW_M2E": 27, "RW_M2H": 27,
    "MATH_M1": 22, "MATH_M2E": 22, "MATH_M2H": 22,
}
MATH_MODULES = ("MATH_M1", "MATH_M2E", "MATH_M2H")
RW_MODULES = ("RW_M1", "RW_M2E", "RW_M2H")

# The domain-block sequence, using the block names the assemblers actually
# write — read off Tests 19-21 rather than transcribed from CLAUDE.md's prose,
# which describes the same sequence in different words. Reading blocks (0-5)
# must all precede writing blocks (6-9); the rank sequence must be
# non-decreasing.
BLOCK_RANK = {
    "Words in Context": 0,
    "Text Structure and Purpose": 1,
    "Cross-Text Connections": 2,
    "Central Ideas and Details": 3,
    "Command of Evidence": 4,
    "Inferences": 5,
    # Writing begins here.
    "Boundaries": 6,
    "Form, Structure, and Sense": 7,
    "Transitions": 8,
    "Rhetorical Synthesis": 9,
}
FIRST_WRITING_RANK = 6

VALID_DOMAINS = {"INI", "CAS", "EOI", "SEC", "ALG", "ADV", "PSDA", "GT"}
VALID_SKILLS = {
    "INI-CI", "INI-IE", "INI-CE", "CAS-WV", "CAS-TS", "CAS-CT", "EOI-RS", "EOI-TR",
    "SEC-BS", "SEC-FS", "ALG-LE", "ALG-LF", "ALG-LI", "ADV-NF", "ADV-EQ", "ADV-NE",
    "PSDA-RP", "PSDA-ST", "PSDA-DI", "GT-AV", "GT-LA", "GT-TR",
}

IMG = re.compile(r"<img[^>]*>", re.I)
MATH_SPAN = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.S)


def outside_math(html: str) -> str:
    """Text with <img> tags and every math span removed.

    Both removals matter. Base64 image payloads match every raw-notation
    pattern below, and the patterns are *about* notation that escaped a math
    span, so the spans themselves must not be scanned.
    """
    return MATH_SPAN.sub(" ", IMG.sub(" ", html))


# Raw notation that must never appear outside a math span. Each of these
# shipped live at least once.
RAW_NOTATION = [
    ("caret exponent", re.compile(r"\^")),
    ("sqrt( )", re.compile(r"sqrt\s*\(", re.I)),
    ("asterisk as multiply", re.compile(r"(?<![\s>])\s*\*\s*(?![\s<])")),
    ("slash fraction", re.compile(r"(?<![\d/])\d+\s*/\s*\d+(?![\d/])")),
    ("ASCII !=", re.compile(r"!=")),
    ("ASCII <= or >=", re.compile(r"<=|>=")),
    ("LaTeX macro outside math", re.compile(r"\\(?:frac|sqrt|pi|le|ge|ne|cdot|times|div|theta|alpha|beta)(?![A-Za-z])")),
    # `pi` as a bare word. `\bpi` does NOT work — a digit and a letter are both
    # word characters, so "3pi" has no boundary. This is the documented bug.
    ("spelled-out pi", re.compile(r"(?<![A-Za-z])pi(?![A-Za-z])")),
    ("spelled-out Greek", re.compile(r"(?<![A-Za-z])(?:theta|alpha|beta|lambda)(?![A-Za-z])", re.I)),
    ("bare trig/log call", re.compile(r"(?<![A-Za-z\\])(?:sin|cos|tan|log|ln)\s*\(")),
]

# Tag balance. The pattern requires a non-name character after the tag name, so
# `<u` cannot match `<ul` — the exact bug that produced nine false findings in
# an earlier build.
PAIRED_TAGS = ("p", "u", "em", "strong", "table", "thead", "tbody", "tr", "th", "td", "ul", "ol", "li", "sup", "sub")

# Wording that points at something rendered on the page, as opposed to the
# ordinary English senses of the same nouns.
FIG = r"(?:table|graph|chart|plot|diagram|figure)"
REFERS_TO_DISPLAYED_FIGURE = re.compile(
    r"(?:"
    rf"(?:data|information|values?)\s+(?:from|in)\s+the\s+{FIG}"
    rf"|the\s+{FIG}\s+(?:above|below|shown|gives|shows|summari[sz]es|lists|displays)"
    rf"|(?:shown|given|summari[sz]ed|listed|displayed)\s+in\s+the\s+{FIG}"
    rf"|the\s+(?:following|accompanying|preceding)\s+{FIG}"
    rf"|according\s+to\s+the\s+{FIG}"
    r")",
    re.I,
)


def tag_counts(html: str, tag: str):
    opens = len(re.findall(rf"<{tag}(?=[\s/>])", html, re.I))
    closes = len(re.findall(rf"</{tag}\s*>", html, re.I))
    return opens, closes


def question_html(q: dict) -> str:
    parts = [q.get("stem", ""), q.get("passage") or ""]
    parts += [c.get("content", "") for c in q.get("choices", []) or []]
    return " ".join(parts)


def validate(num: int, path: str, problems: list):
    def bad(msg):
        problems.append(f"Test {num}: {msg}")

    with open(path) as fh:
        test = json.load(fh)

    missing = [k for k in MODULES if k not in test]
    if missing:
        bad(f"missing modules {missing}")
        return

    for key, expected in MODULES.items():
        got = len(test[key])
        if got != expected:
            bad(f"{key} has {got} questions, expected {expected}")

    # ---- Math ------------------------------------------------------------
    for key in MATH_MODULES:
        qs = test[key]
        mc = sum(1 for q in qs if q.get("type") == "MULTIPLE_CHOICE")
        fr = sum(1 for q in qs if q.get("type") == "FREE_RESPONSE")
        if fr > 3:
            bad(f"{key} has {fr} free-response questions, the cap is 3")
        elif fr != 3:
            bad(f"{key} has {fr} free-response questions, the target is exactly 3")
        if mc + fr != len(qs):
            bad(f"{key} has questions of an unexpected type")

        for i, q in enumerate(qs, 1):
            if q.get("type") == "FREE_RESPONSE":
                raw = q.get("correctAnswerFR")
                if raw is None:
                    bad(f"{key} Q{i} free-response has no correctAnswerFR")
                elif not isinstance(raw, str):
                    bad(f"{key} Q{i} correctAnswerFR is {type(raw).__name__}, must be a JSON-encoded string")
                else:
                    try:
                        parsed = json.loads(raw)
                    except json.JSONDecodeError:
                        bad(f"{key} Q{i} correctAnswerFR is not valid JSON: {raw!r}")
                    else:
                        if not isinstance(parsed, list) or not parsed:
                            bad(f"{key} Q{i} correctAnswerFR decodes to {parsed!r}, must be a non-empty array")
            else:
                choices = q.get("choices") or []
                if len(choices) != 4:
                    bad(f"{key} Q{i} has {len(choices)} choices, expected 4")
                keys = [c for c in choices if c.get("isCorrect")]
                if len(keys) != 1:
                    bad(f"{key} Q{i} has {len(keys)} correct choices, expected exactly 1")
                contents = [str(c.get("content", "")).strip() for c in choices]
                if len(set(contents)) != len(contents):
                    bad(f"{key} Q{i} has duplicate answer choices")
                for c in contents:
                    if not re.search(r"[A-Za-z0-9]", c):
                        bad(f"{key} Q{i} has an answer choice with no letter or digit")

    # ---- R&W block order -------------------------------------------------
    for key in RW_MODULES:
        ranks, unknown = [], set()
        for q in test[key]:
            block = q.get("block")
            if block in BLOCK_RANK:
                ranks.append(BLOCK_RANK[block])
            elif block:
                unknown.add(block)
        if unknown:
            bad(f"{key} has unrecognised blocks {sorted(unknown)}")
        for i in range(1, len(ranks)):
            if ranks[i] < ranks[i - 1]:
                inv = {v: k for k, v in BLOCK_RANK.items()}
                bad(f"{key} block order is not monotonic at question {i + 1}: "
                    f"{inv[ranks[i]]} follows {inv[ranks[i - 1]]}")
                break

        # Reading must be at most ~15 of 27, so the writing block gets the rest.
        reading = sum(1 for q in test[key] if BLOCK_RANK.get(q.get("block"), 99) < FIRST_WRITING_RANK)
        if reading > 16:
            bad(f"{key} has {reading} reading questions, leaving too few for writing")

    # The answer key is balanced across the whole 81-question R&W section, not
    # per module — `balance_rw.py` rotates to 21/20/20/20 over the test.
    letters = Counter()
    for key in RW_MODULES:
        for q in test[key]:
            for c in q.get("choices") or []:
                if c.get("isCorrect"):
                    letters[c.get("label")] += 1
    if letters and (max(letters.values()) - min(letters.values())) > 4:
        bad(f"R&W answer key is skewed across the test: {dict(sorted(letters.items()))}")

    # ---- Whole test ------------------------------------------------------
    all_qs = [(k, i, q) for k in MODULES for i, q in enumerate(test[k], 1)]

    for key, i, q in all_qs:
        if q.get("domain") not in VALID_DOMAINS:
            bad(f"{key} Q{i} has unknown domain {q.get('domain')!r}")
        if q.get("skill") not in VALID_SKILLS:
            bad(f"{key} Q{i} has unknown skill {q.get('skill')!r}")

        html = question_html(q)
        clean = outside_math(html)
        for label, pattern in RAW_NOTATION:
            m = pattern.search(clean)
            if m:
                ctx = clean[max(0, m.start() - 40):m.start() + 40].replace("\n", " ")
                bad(f"{key} Q{i} raw {label} outside a math span: …{ctx.strip()}…")
                break

        for tag in PAIRED_TAGS:
            o, c = tag_counts(html, tag)
            if o != c:
                bad(f"{key} Q{i} has {o} <{tag}> and {c} </{tag}>")

        if re.search(r"(?<!\*)\*(?!\*)[^*\n]{1,80}\*(?!\*)", html):
            bad(f"{key} Q{i} contains markdown asterisks that will render literally")

        # A stem that promises a *displayed* figure must carry one.
        #
        # Deliberately not the bare words "table"/"graph"/"figure": a corrected
        # "figure" is a number, "Halley's table" is a historical object, and
        # "the graph of f" is an abstraction that needs no picture. Both of
        # those false-fired on already-published tests. Only deictic phrasing —
        # wording that points at something on the page — counts.
        stem = q.get("stem", "")
        if REFERS_TO_DISPLAYED_FIGURE.search(stem):
            if "<table" not in html and not q.get("imageUrl"):
                bad(f"{key} Q{i} points at a displayed figure but has no <table> and no imageUrl: "
                    f"{REFERS_TO_DISPLAYED_FIGURE.search(stem).group(0)!r}")

    # Provenance: no question may still carry another test's tag.
    for key, i, q in all_qs:
        ref = str(q.get("_ref", ""))
        m = re.search(r"T(\d+)", ref)
        if m and int(m.group(1)) != num:
            bad(f"{key} Q{i} carries Test {m.group(1)} provenance in _ref {ref!r}")

    # Duplicate questions.
    #
    # Math is keyed on the stem alone, which carries the whole question. R&W
    # stems are deliberately formulaic — "Which choice completes the text with
    # the most logical and precise word or phrase?" appears a dozen times per
    # test by design — so an R&W question is only a duplicate when its
    # *passage* repeats too.
    math_stems = Counter(q.get("stem", "").strip() for k, _, q in all_qs if k in MATH_MODULES)
    for stem, n in math_stems.items():
        if n > 1:
            bad(f"a Math stem appears {n} times: {stem[:90]!r}")

    rw_pairs = Counter(
        (q.get("stem", "").strip(), (q.get("passage") or "").strip())
        for k, _, q in all_qs if k in RW_MODULES
    )
    for (stem, passage), n in rw_pairs.items():
        if n > 1 and passage:
            bad(f"an R&W stem+passage pair appears {n} times: {passage[:80]!r}")

    rw_passages = Counter(
        (q.get("passage") or "").strip() for k, _, q in all_qs if k in RW_MODULES
    )
    for passage, n in rw_passages.items():
        if n > 2 and passage:
            bad(f"an R&W passage is reused {n} times: {passage[:80]!r}")


def main():
    wanted = [int(a) for a in sys.argv[1:] if a.isdigit()]
    paths = []
    for entry in sorted(os.listdir(HERE)):
        d = os.path.join(HERE, entry)
        if not os.path.isdir(d):
            continue
        m = re.fullmatch(r"test-(\d+)-build", entry)
        if not m:
            continue
        num = int(m.group(1))
        if wanted and num not in wanted:
            continue
        p = os.path.join(d, f"test{num}.json")
        if os.path.exists(p):
            paths.append((num, p))

    if not paths:
        print("No assembled test JSON found.")
        return 1

    problems = []
    for num, p in paths:
        validate(num, p, problems)

    print(f"Validated {len(paths)} test(s): {', '.join(str(n) for n, _ in paths)}")
    if problems:
        print(f"\nFAIL — {len(problems)} problem(s):")
        for p in problems:
            print(f"  {p}")
        return 1
    print("PASS — module shapes, question types, free-response encoding, answer keys,")
    print("       block order, domain/skill codes, raw notation, tag balance and")
    print("       provenance all clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
