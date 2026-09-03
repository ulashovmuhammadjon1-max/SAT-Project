"""Chemistry-specific gates shared by every ``verify_h<u>_<n>.py``.

The structural gate (30 questions, five distinct choices, a key pinned to a
distinctive substring of its own choice text, no choice contained in another,
every table recomputed) lives in ``cg_check.py`` and is subject-neutral. This
module adds the two things Chemistry needs on top of it:

``notation``   AP Chemistry is NOT typeset by ``export_units.py``. The
               converter was tried on this subject and removed -- it split
               ``H2SO4`` into ``\\(H_{2}\\)SO4`` and set an electron
               configuration with subscripts where it needs superscripts. So
               every ``\\( ... \\)`` span in a Chemistry module is hand-written,
               and a bare ``^``, a stray backslash macro or a slash fraction
               left OUTSIDE a span reaches a student as literal text. This
               check reads the module's own student-facing strings, splits them
               into inside-span and outside-span text, and bans the markup that
               only renders inside a span from appearing outside one -- and
               bans unescaped function names from appearing inside one.

``numeric``    Units 7 to 9 are the most quantitative in the course. Where a
               keyed choice asserts a number -- a pH, a ratio, a ``K``, a
               ``\\Delta G^\\circ``, a cell potential, a mass deposited -- the
               verifier recomputes it from the stimulus alone and asserts the
               recomputed value appears in the KEYED choice. ``cg_check`` does
               this for questions carrying a ``table=``; this does it for the
               ones whose numbers are in the stem.

NO ``\\b`` ANYWHERE, for the reason recorded in ``cg_check`` and CLAUDE.md: a
digit and a letter are both word characters, so ``\\b`` is silently not a
boundary exactly where it looks like one. Every phrase match uses explicit
lookarounds.
"""
import re

import cg_check as cg

# ------------------------------------------------------------------ notation

_SPAN = re.compile(r"\\\((.*?)\\\)", re.S)

# Markup that renders only inside a math span. Outside one it prints raw.
_OUTSIDE_BANNED = [
    (re.compile(r"\\"), "a backslash macro outside a math span: it prints raw"),
    (re.compile(r"\^"), "a bare caret outside a math span: write \\(x^{2}\\)"),
    (re.compile(r"_"), "a bare underscore outside a math span"),
    (re.compile(r"\$"), "a dollar sign: MathContent reads $ as inline math"),
    (re.compile(r"(?<![A-Za-z])\d+\s*/\s*\d"), "a slash fraction outside a math span"),
    (re.compile(r"°"), "a raw degree glyph: write 'degrees Celsius' or \\(25\\,^\\circ\\mathrm{C}\\)"),
    (re.compile(r"[ΔΣ]"), "a raw Greek capital: write \\(\\Delta H^\\circ\\) inside a span"),
    (re.compile(r"[×÷≤≥≠→⇌]"), "a raw operator glyph: write it inside a math span"),
]

# Function names must be escaped inside a span, or KaTeX sets them as a product
# of italic variables: bare ``log`` renders as l times o times g.
_INSIDE_BANNED = [
    (re.compile(r"(?<![\\A-Za-z])log(?![A-Za-z])"), "an unescaped log inside a span: write \\log"),
    (re.compile(r"(?<![\\A-Za-z])ln(?![A-Za-z])"), "an unescaped ln inside a span: write \\ln"),
    (re.compile(r"(?<![\\A-Za-z])exp(?![A-Za-z])"), "an unescaped exp inside a span: write \\exp"),
    (re.compile(r"°"), "a raw degree glyph inside a span: write ^\\circ"),
    (re.compile(r"\$"), "a dollar sign inside a span"),
]


def _strings(item):
    """Every student-facing string on one question, including its table."""
    out = [item["q"], item["why"]] + list(item["choices"])
    t = item.get("table")
    if t:
        out += [str(h) for h in t["headers"]]
        out += [str(c) for r in t["rows"] for c in r]
    return out


def notation(module):
    """Hand-written spans only, and nothing span-only left outside a span."""
    code = module.TOPIC[0]
    n_spans = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _strings(item):
            opens, closes = text.count("\\("), text.count("\\)")
            assert opens == closes, (
                f"{code} q{i}: {opens} '\\(' against {closes} '\\)' in {text[:80]!r}"
            )
            spans = _SPAN.findall(text)
            n_spans += len(spans)
            for s in spans:
                assert "\\(" not in s, f"{code} q{i}: nested math span in {text[:80]!r}"
                for pat, msg in _INSIDE_BANNED:
                    hit = pat.search(s)
                    assert not hit, f"{code} q{i}: {msg} -- {hit.group(0)!r} in {s[:60]!r}"
            outside = _SPAN.sub(" ", text)
            for pat, msg in _OUTSIDE_BANNED:
                hit = pat.search(outside)
                assert not hit, (
                    f"{code} q{i}: {msg} -- {hit.group(0)!r} in {outside[:80]!r}"
                )
            # A span welded to a word renders with no space in front of it.
            for m in _SPAN.finditer(text):
                before = text[m.start() - 1] if m.start() else " "
                after = text[m.end()] if m.end() < len(text) else " "
                assert not before.isalnum(), (
                    f"{code} q{i}: math span opens against {before!r} with no space: "
                    f"{text[max(0, m.start() - 25):m.end()]!r}"
                )
                assert not after.isalnum(), (
                    f"{code} q{i}: math span closes against {after!r} with no space: "
                    f"{text[m.start():m.end() + 25]!r}"
                )
    print(f"OK  {code} notation: {n_spans} hand-written span(s), nothing span-only "
          f"left outside one, across {len(module.QUESTIONS)} questions.")


# ------------------------------------------------------------------- numeric

def keyed(item):
    """The text of the choice the module keys."""
    return item["choices"][item["ans"]]


def shows(item, value):
    """The keyed choice states ``value``, and no distractor states it."""
    text = str(value)
    assert cg.contains_phrase(keyed(item), text), (
        f"recomputed {text!r} is not in the keyed choice {keyed(item)!r}"
    )
    also = [k for k, c in enumerate(item["choices"])
            if k != item["ans"] and cg.contains_phrase(c, text)]
    assert not also, f"recomputed {text!r} also appears in choice(s) {also}"
    return text


def numeric(module, checks):
    """Recompute every stem-numeric key. ``checks`` maps question number to fn."""
    code = module.TOPIC[0]
    n = len(module.QUESTIONS)
    for i in checks:
        assert 1 <= i <= n, f"{code}: numeric check {i} is out of range"
    notes = 0
    for i, fn in sorted(checks.items()):
        item = module.QUESTIONS[i - 1]
        note = fn(item)
        assert isinstance(note, str) and len(note.split()) >= 4, (
            f"{code} q{i}: a numeric check must return a sentence saying what it recomputed"
        )
        notes += 1
    print(f"OK  {code} arithmetic: {notes} stem-numeric key(s) recomputed from the "
          "stimulus alone.")


# -------------------------------------------------------------- selftest driver

def selftest(module, claims, table_checks=None, numeric_checks=None, mutations=()):
    """Negative control: every gate must FAIL when its own input is corrupted.

    ``mutations`` is a sequence of (label, fn(mod, claims)) run in addition to
    the standard ones. Each must make ``run`` raise.
    """
    import copy
    import types

    table_checks = table_checks or {}
    numeric_checks = numeric_checks or {}

    def fresh():
        mod = types.ModuleType(module.__name__ + "_mutant")
        mod.TOPIC = module.TOPIC
        mod.QUESTIONS = copy.deepcopy(module.QUESTIONS)
        return mod

    def run(mod, cl):
        notation(mod)
        cg.check(mod, cl, table_checks=table_checks)
        numeric(mod, numeric_checks)

    def must_fail(label, mutate):
        mod, cl = fresh(), list(claims)
        try:
            mutate(mod, cl)
            run(mod, cl)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:100]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, cl):
        mod.QUESTIONS[0]["ans"] = (mod.QUESTIONS[0]["ans"] + 1) % 5

    def break_anchor(mod, cl):
        cl[0] = ("no such phrase appears anywhere", cl[0][1])

    def duplicate_choice(mod, cl):
        mod.QUESTIONS[1]["choices"][4] = mod.QUESTIONS[1]["choices"][0]

    def thin_why(mod, cl):
        mod.QUESTIONS[2]["why"] = "Because it is."

    def letter_reference(mod, cl):
        mod.QUESTIONS[3]["why"] = ("Option B is wrong because the framework says so, and "
                                   "the rest of the reasoning follows from that fact.")

    def bare_caret(mod, cl):
        mod.QUESTIONS[4]["q"] = mod.QUESTIONS[4]["q"] + " Consider 10^-5 molar."

    def stray_macro(mod, cl):
        mod.QUESTIONS[4]["choices"][0] = mod.QUESTIONS[4]["choices"][0] + " \\Delta H"

    def unescaped_log(mod, cl):
        mod.QUESTIONS[5]["q"] = mod.QUESTIONS[5]["q"] + " Use \\( pH = -log[H_3O^+] \\) here."

    def unbalanced_span(mod, cl):
        mod.QUESTIONS[6]["q"] = mod.QUESTIONS[6]["q"] + " \\( K_a"

    print("negative controls:")
    must_fail("key moved off its anchor", move_key)
    must_fail("anchor no longer in the keyed choice", break_anchor)
    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a why reduced below the minimum", thin_why)
    must_fail("a why naming an option by letter", letter_reference)
    must_fail("a bare caret outside a math span", bare_caret)
    must_fail("a stray backslash macro outside a math span", stray_macro)
    must_fail("an unescaped log inside a math span", unescaped_log)
    must_fail("an unbalanced math span", unbalanced_span)
    for label, fn in mutations:
        must_fail(label, fn)
    print("all negative controls raised as required.")


def run(module, claims, table_checks=None, numeric_checks=None):
    notation(module)
    cg.check(module, claims, table_checks=table_checks or {})
    numeric(module, numeric_checks or {})
