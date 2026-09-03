"""Notation gate and negative-control harness for the AP CHEMISTRY (``h*``) banks.

Chemistry is NOT typeset on the way out. ``export_units.py`` deliberately keeps
CHEMISTRY out of ``TYPESET_SUBJECTS`` because ``mathfmt`` is a parser for
algebraic notation and a chemical formula is not that -- it split ``H2SO4`` into
``\\(H_{2}\\)SO4`` and read ``Fe2O3 + 3 CO`` across the formula boundary. So the
author hand-writes every ``\\( ... \\)`` span, and whatever is left outside a span
reaches the student verbatim.

That is the whole risk this file exists to gate. A bare ``^``, a stray
``\\frac``, or a slash fraction sitting outside a span does not fail anything at
export time; it renders literally on the page. ``MathContent`` runs KaTeX with
``throwOnError: false``, so a malformed span shows as red source text rather
than raising -- production is *less* strict than this check on purpose.

WHAT IS CHECKED, per module, over stems, choices, ``why`` text and table cells:

  outside a span   no ``^``, no backslash, no ``_{``, no ``$``, no digit/digit
                   slash fraction
  the spans        balanced and non-nesting ``\\(``/``\\)``, balanced braces,
                   non-empty, no nested ``\\(``
  spacing          a span may not abut an alphanumeric on either side, which is
                   the ``...length of\\(AB\\)is...`` defect from CLAUDE.md

NO ``\\b`` ANYWHERE, per the standing rule: a digit and a letter are both word
characters, so ``\\b`` is silently not a boundary exactly where it looks like
one. Every pattern here is anchored on characters that cannot be ambiguous.

Siblings authoring other Chemistry units may import this; it is not specific to
any unit. ``selftest`` is the negative control -- it corrupts a key, an anchor,
the notation and (via ``extra``) a table cell, and fails loudly if any of those
corruptions is NOT caught.
"""
import copy
import re
import types

import cg_check as cg

_SPAN = re.compile(r"\\\((.+?)\\\)", re.S)
_DELIM = re.compile(r"\\\(|\\\)")

# Outside a math span these all render as literal characters to the student.
_BAD_OUTSIDE = [
    (re.compile(r"\^"), "a bare caret outside a math span"),
    (re.compile(r"\\"), "a backslash outside a math span (a macro would print raw)"),
    (re.compile(r"_\{"), "a subscript brace outside a math span"),
    (re.compile(r"\$"), "a dollar sign, which some renderers read as inline math"),
    (re.compile(r"(?<![A-Za-z0-9])\d+(?:\.\d+)?\s*/\s*\d"),
     "a slash fraction outside a math span: typeset it or write it in words"),
]


def texts(item):
    """Every student-facing string on one question, table cells included."""
    out = [item["q"], item["why"]] + list(item["choices"])
    t = item.get("table")
    if t:
        out += [str(h) for h in t["headers"]]
        out += [str(c) for row in t["rows"] for c in row]
    return out


def notation(module):
    """Raise AssertionError on any notation defect in ``module``."""
    code = module.TOPIC[0]
    n_spans = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in texts(item):
            where = f"{code} q{i}"
            delims = _DELIM.findall(text)
            assert delims == [r"\(", r"\)"] * (len(delims) // 2), (
                f"{where}: math delimiters do not open and close in order "
                f"({delims}) in {text[:80]!r}"
            )
            for m in _SPAN.finditer(text):
                n_spans += 1
                body = m.group(1)
                assert body.strip(), f"{where}: an empty math span in {text[:80]!r}"
                assert body.count("{") == body.count("}"), (
                    f"{where}: unbalanced braces in the span {body!r}"
                )
                assert "\\(" not in body and "$" not in body, (
                    f"{where}: a nested delimiter inside the span {body!r}"
                )
                before = text[m.start() - 1] if m.start() else " "
                after = text[m.end()] if m.end() < len(text) else " "
                assert not before.isalnum(), (
                    f"{where}: a math span abuts {before!r} on its left in "
                    f"{text[max(0, m.start() - 30):m.end()]!r}; leave a space"
                )
                assert not after.isalnum(), (
                    f"{where}: a math span abuts {after!r} on its right in "
                    f"{text[m.start():m.end() + 30]!r}; leave a space"
                )
            outside = _SPAN.sub(" ", text)
            for pat, msg in _BAD_OUTSIDE:
                hit = pat.search(outside)
                assert not hit, f"{where}: {msg} -- {hit.group(0)!r} in {text[:90]!r}"
    print(f"OK  {code} notation: {len(module.QUESTIONS)} questions, "
          f"{n_spans} hand-written math span(s), nothing raw outside one.")


def audit(module, claims, table_checks=None):
    """The whole gate: notation, then the shared structural and key checks."""
    notation(module)
    cg.check(module, claims, table_checks=table_checks)


# --------------------------------------------------------------- negative control

def _mutant(module):
    m = types.ModuleType(module.__name__ + "_mutant")
    m.TOPIC = module.TOPIC
    m.QUESTIONS = copy.deepcopy(module.QUESTIONS)
    return m


def selftest(module, claims, table_checks=None, extra=()):
    """Corrupt each gate on purpose and require every corruption to be caught.

    ``extra`` is a sequence of ``(label, mutate)`` pairs for module-specific
    corruptions -- above all a table cell, which only the module's own
    ``table_checks`` can be expected to notice.
    """
    def must_fail(label, mutate):
        mod, cl = _mutant(module), list(claims)
        try:
            mutate(mod, cl)
            audit(mod, cl, table_checks=table_checks)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:88]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} was not caught")

    def caret_outside(mod, cl):
        mod.QUESTIONS[0]["choices"][0] += " at 3.0 x 10^-4 molar"

    def macro_outside(mod, cl):
        mod.QUESTIONS[0]["q"] += " Assume \\frac{1}{2} of the sample reacts."

    def unbalanced_span(mod, cl):
        mod.QUESTIONS[0]["q"] += r" Take \( \frac{1}{2 \) of it."

    def span_abuts(mod, cl):
        mod.QUESTIONS[0]["why"] += r" the value of\(K_c\)is fixed"

    def move_key(mod, cl):
        mod.QUESTIONS[0]["ans"] = (mod.QUESTIONS[0]["ans"] + 1) % 5

    def break_anchor(mod, cl):
        cl[1] = ("no such phrase appears anywhere", cl[1][1])

    def duplicate_choice(mod, cl):
        mod.QUESTIONS[0]["choices"][4] = mod.QUESTIONS[0]["choices"][0]

    def thin_why(mod, cl):
        mod.QUESTIONS[2]["why"] = "Because it is."

    def letter_reference(mod, cl):
        mod.QUESTIONS[3]["why"] = (
            "Option B is ruled out because the framework says so, and the rest "
            "of the reasoning follows directly from that one point."
        )

    print(f"negative controls for {module.TOPIC[0]}:")
    for label, fn in (
        ("a caret left outside a math span", caret_outside),
        ("a LaTeX macro outside a math span", macro_outside),
        ("a math span with unbalanced braces", unbalanced_span),
        ("a math span abutting a letter", span_abuts),
        ("the key moved off its anchor", move_key),
        ("an anchor that is in no choice", break_anchor),
        ("a distractor made identical to the key", duplicate_choice),
        ("a why reduced below the minimum", thin_why),
        ("a why naming an option by letter", letter_reference),
    ) + tuple(extra):
        must_fail(label, fn)
    print("all negative controls raised as required.")
