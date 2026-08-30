"""The anchor-and-grounding gate every AP U.S. Government verifier runs.

``usgov_check.check`` enforces the key-first invariant: ``ans == 0`` on every
question. That guards the INDEX. It does not guard the TEXT, and the text is
what a later edit moves. Reorder a choice list, rewrite the first option, or
sharpen a distractor until it says what the key says, and ``ans`` is still 0 and
every structural check still passes.

So each verifier carries two per-question maps, and this module checks them:

ANCHORS
    A literal substring that must appear in the KEYED choice and in none of the
    other four. Comparison is case-sensitive and literal on purpose -- a
    normalised comparison would let a distractor edited to differ only in
    punctuation slip through. Written against the choice text as it stands, the
    map doubles as a compact record of what each item is keyed on, readable
    without opening the module.

GROUNDING
    The CED essential-knowledge statement, required Supreme Court case,
    foundational document or constitutional provision the key traces back to.
    SOCIAL_BRIEF.md's rule for these subjects is that a key must trace to the
    CED rather than to the author's memory; an unwritten trace is not a trace.
    Writing thirty of them is the review pass, because it cannot be done
    without deciding, item by item, what makes the key true. Every wrong key
    and wrong figure found in this bank so far was found doing it.

Neither map can check the politics. That is stated plainly in usgov_check.py
and it is still true here: nothing mechanical knows that McCulloch is about
federal supremacy. What these maps guarantee is that the human who did know
wrote it down, and that no later edit silently detaches a key from the choice
it was written for.
"""

MIN_GROUNDING = 40


def check(module, anchors, grounding):
    qs = module.QUESTIONS
    bad = []
    for i, item in enumerate(qs, 1):
        anchor = anchors.get(i)
        if not anchor:
            bad.append(f"q{i}: no anchor")
        else:
            key = item["choices"][item["ans"]]
            if anchor not in key:
                bad.append(f"q{i}: anchor {anchor!r} is not in the keyed choice {key!r}")
            for k, c in enumerate(item["choices"]):
                if k != item["ans"] and anchor in c:
                    bad.append(f"q{i}: anchor {anchor!r} also appears in distractor "
                               f"{'ABCDE'[k]}, so it does not identify the key")
        if len(grounding.get(i, "").strip()) < MIN_GROUNDING:
            bad.append(f"q{i}: grounding is missing or too thin to be a citation")
    for i in sorted(set(anchors) | set(grounding)):
        if not 1 <= i <= len(qs):
            bad.append(f"anchor/grounding names q{i}, which does not exist")
    if bad:
        print(f"FAIL {module.__name__} anchors/grounding")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} anchors: {len(anchors)} keys pinned to a distinctive "
          f"substring of their own choice text; {len(grounding)} keys traced to a CED "
          "statement, required case, foundational document or constitutional provision")


# --- notation ---------------------------------------------------------------
# export_units.py runs every string through mathfmt.convert on the way out, and
# that converter reads a hyphen OR a slash between two digits as arithmetic:
#
#     "a 5-4 decision"        ->  "a \(5 - 4\) decision"
#     "the 2024/2025 session" ->  "the \(2024/2025\) session"
#
# gov345_check enforces the hyphen half for Units 3 to 5. usgov_check does not
# enforce either, so Units 1 and 2 carry it here instead. Write "five to four",
# "ages 18 to 24", or an en dash. The pattern is spelled out rather than using
# \d so it cannot match a non-ASCII digit and confuse the error message.
import re as _re

_MATHY = _re.compile(r"[0-9]\s*[-/]\s*[0-9]")


def notation(module):
    """No digit-hyphen-digit and no digit-slash-digit anywhere in the module."""
    hits = []
    for i, item in enumerate(module.QUESTIONS, 1):
        strings = [("stem", item["q"]), ("why", item["why"])]
        strings += [(f"choice {'ABCDE'[k]}", c) for k, c in enumerate(item["choices"])]
        t = item.get("table")
        if t:
            strings += [("table header", h) for h in t["headers"]]
            strings += [("table cell", c) for row in t["rows"] for c in row]
        for label, s in strings:
            m = _MATHY.search(s)
            if m:
                hits.append(f"q{i} {label}: {m.group(0)!r} -- mathfmt.convert would "
                            "typeset this as arithmetic")
    if hits:
        print(f"FAIL {module.__name__} notation")
        for h in hits:
            print("  -", h)
        raise SystemExit(1)
    print(f"OK  {module.__name__} notation: no digit-hyphen-digit or digit-slash-digit "
          "anywhere, so mathfmt.convert has nothing to read as arithmetic")


# --- shape -------------------------------------------------------------------
# A question dict may hold exactly these keys. The check exists because of a
# real defect: a stray walrus expression was once left inside a question's dict
# literal, between `ans` and `why`. Python accepted it -- it bound an unused
# name to an empty string -- so the module imported cleanly, every structural
# check passed, and the dead code would have shipped inside a live question.
#
# That defect is invisible to reading and invisible to every content check in
# this bank, because it is syntactically valid and semantically inert. The only
# thing that catches it is asserting the key set is exactly what it should be.
_KEYS = {"q", "choices", "ans", "why"}
_OPTIONAL = {"table"}


def shape(module):
    """Every question dict holds exactly q/choices/ans/why, plus an optional table."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        keys = set(item)
        missing = _KEYS - keys
        extra = keys - _KEYS - _OPTIONAL
        if missing:
            bad.append(f"q{i}: missing {sorted(missing)}")
        if extra:
            bad.append(f"q{i}: unexpected key(s) {sorted(extra)} -- a stray expression or a "
                       "misspelled field name inside the dict literal")
        if not isinstance(item.get("choices"), list):
            bad.append(f"q{i}: choices is not a list")
        if not isinstance(item.get("ans"), int) or isinstance(item.get("ans"), bool):
            bad.append(f"q{i}: ans is not a plain integer")
        for k in ("q", "why"):
            if not isinstance(item.get(k), str):
                bad.append(f"q{i}: {k} is not a string")
    if bad:
        print(f"FAIL {module.__name__} shape")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} shape: every question dict holds exactly q, choices, ans "
          "and why, with no stray keys")
