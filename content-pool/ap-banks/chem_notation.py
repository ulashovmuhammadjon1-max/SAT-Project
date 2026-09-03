r"""Notation gate for the AP CHEMISTRY topic banks (prefix ``h``).

SCIENCE_BRIEF.md: **the converter does not run on Chemistry.** ``mathfmt.py``
parses algebraic notation and a chemical formula is not that -- it split
``H2SO4`` into ``\(H_{2}\)SO4``, read ``Fe2O3 + 3 CO`` across the formula
boundary, and set ``1s2 2s2 2p6`` with SUBscripts where a configuration needs
SUPERscripts. So every span is hand-written, and what a hand writes a checker
has to police.

Student-facing text reaches the browser through ``MathContent``
(``src/components/shared/math-content.tsx``): the ``\( ... \)`` spans go to
KaTeX and **everything outside them is injected as raw HTML**. Two distinct
hazards follow, and this module gates both.

OUTSIDE a span, the text is HTML, so:
  * a backslash macro prints literally (``2\pi`` reaches the student as
    backslash-p-i -- the defect CLAUDE.md's math audit already shipped once);
  * a bare ``^`` or ``_`` prints literally;
  * ``<`` and ``>`` are read as the start of an HTML tag and can swallow the
    rest of the sentence -- write "less than", never ``pH < 7``;
  * ``&`` opens an entity;
  * ``1.8 x 10^-5`` and ``3/4`` are the plain-text math the brief forbids.

INSIDE a span, KaTeX runs with ``throwOnError: false`` in production, which
means a bad macro does **not** fail -- it renders as red source text that only
a human looking at the page would notice. A checker that mirrors production
therefore sees nothing, exactly as CLAUDE.md records for the Calculus banks. So
the gate here is stricter than the site: braces must balance, and every macro
must be on an explicit allow list. A macro this bank has never needed is far
more likely to be a typo than a considered choice.

NO ``\b`` ANYWHERE. A digit and a letter are both word characters, so ``\b`` is
silently not a boundary exactly where it looks like one. Explicit lookarounds
only -- this project has paid for that lesson five times.

Every verifier calls :func:`style` on its own module and negative-controls it
by injecting each defect on purpose; :func:`selftest` here runs the same
controls over this module's own patterns so a regression in the gate itself is
caught even if a verifier's control is weak.
"""
import re

# ---------------------------------------------------------------- math spans

# Inline math only. Display math (\[ ... \]) is not used in these banks: an AP
# stem is prose with numbers in it, and a centered display block inside a
# sentence reads as a rendering error.
_SPAN = re.compile(r"\\\((.*?)\\\)", re.S)
_OPEN = re.compile(r"\\\(")
_CLOSE = re.compile(r"\\\)")

# Macros this bank actually needs. Anything else is a typo until a human adds
# it here deliberately.
ALLOWED_MACROS = frozenset("""
    times cdot div frac sqrt mathrm text left right
    Delta delta pi lambda nu mu varepsilon epsilon theta sigma alpha beta gamma
    approx ne le ge pm to rightarrow leftarrow rightleftharpoons longrightarrow
    log ln circ degree infty cdots ldots
    quad qquad
""".split())

# Non-letter escapes: the thin space and the escaped percent/brace.
ALLOWED_ESCAPES = frozenset([",", ";", "!", "%", "{", "}", " "])

_MACRO = re.compile(r"\\([A-Za-z]+|.)", re.S)

# ------------------------------------------------------- outside-span hazards
#
# Each entry is (pattern, message). The message names the fix, because a
# checker that only says "failed" trains you to ignore it.
OUTSIDE_BANNED = [
    (re.compile(r"\\"),
     r"a backslash outside a \( ... \) span: it prints literally to the student"),
    (re.compile(r"\^"),
     r"a bare ^ outside a span: write the exponent inside \( ... \)"),
    (re.compile(r"_"),
     r"a bare _ outside a span: a formula in prose is plain text (H2SO4), a "
     r"subscript in math is \(\mathrm{H_2SO_4}\)"),
    (re.compile(r"\$"),
     "a dollar sign: KaTeX and several checkers read it as inline math"),
    (re.compile(r"[<>]"),
     "a bare < or >: the text outside a span is injected as HTML, so the "
     "browser reads it as a tag. Write 'less than' / 'greater than'"),
    (re.compile(r"&"),
     "a bare ampersand: outside a span the text is HTML and this opens an entity"),
    (re.compile(r"(?<![A-Za-z0-9])\d+(?:\.\d+)?\s*/\s*\d"),
     r"a slash fraction in prose: use \(\frac{a}{b}\) or write the ratio in words"),
    (re.compile(r"\d\s*[xX×]\s*10(?![A-Za-z0-9])"),
     r"plain-text scientific notation: write \(6.022 \times 10^{23}\)"),
    # NOT a range. U+00B2/U+00B3/U+00B9 sit far below U+2070, so [⁰-₉] silently
    # misses the three commonest superscripts -- the same shape of bug as \b.
    (re.compile("[" + "".join("¹²³⁰⁴⁵⁶⁷⁸⁹⁺⁻ⁿ₀₁₂₃₄₅₆₇₈₉₊₋") + "]"),
     "a Unicode superscript or subscript character: use a math span"),
    (re.compile(r"[≤≥≠±√∞]"),
     "a Unicode math operator: use a math span"),
    (re.compile(r"!="),
     r"ASCII !=: write \(\ne\) inside a span"),
]

# ------------------------------------------------------------- span placement
#
# CLAUDE.md, on the Math banks: "Always leave a space either side of an inline
# span" -- KaTeX emits an inline-block, so a span glued to a word runs the two
# together with no gap.
_BEFORE_OK = set("  ([—–-\n\t")
_AFTER_OK = set("  ,.;:?!)]—–\n\t")


def _texts(item):
    """Every student-facing string in one question, including its table."""
    out = [item["q"], item["why"]] + list(item["choices"])
    table = item.get("table")
    if table:
        out += [str(h) for h in table["headers"]]
        out += [str(c) for row in table["rows"] for c in row]
    return out


def check_text(text, where=""):
    """Raise AssertionError if ``text`` breaks the notation rules."""
    n_open, n_close = len(_OPEN.findall(text)), len(_CLOSE.findall(text))
    assert n_open == n_close, (
        rf"{where}: {n_open} '\(' against {n_close} '\)' -- an unclosed math span "
        rf"swallows the rest of the sentence into KaTeX: {text[:90]!r}"
    )

    for m in _SPAN.finditer(text):
        tex = m.group(1)
        assert tex.strip(), f"{where}: an empty math span"
        assert tex.count("{") == tex.count("}"), (
            f"{where}: unbalanced braces in the span {tex!r}"
        )
        for mac in _MACRO.findall(tex):
            ok = (mac in ALLOWED_MACROS) if mac[:1].isalpha() else (mac in ALLOWED_ESCAPES)
            assert ok, (
                f"{where}: unknown macro '\\{mac}' in the span {tex!r}. KaTeX runs "
                "with throwOnError false in production, so this would reach the "
                "student as red source text rather than failing. Add it to "
                "ALLOWED_MACROS only if it is really wanted."
            )
        # Placement: a span must not be glued to the word beside it.
        before = text[m.start() - 1] if m.start() else " "
        after = text[m.end()] if m.end() < len(text) else " "
        assert before in _BEFORE_OK, (
            f"{where}: no space before the span {m.group(0)[:40]!r} -- KaTeX emits "
            f"an inline block, so it runs into {text[max(0, m.start() - 12):m.start()]!r}"
        )
        assert after in _AFTER_OK, (
            f"{where}: no space after the span {m.group(0)[:40]!r} -- it runs into "
            f"{text[m.end():m.end() + 12]!r}"
        )

    stripped = _SPAN.sub(" @ ", text)
    for pat, msg in OUTSIDE_BANNED:
        hit = pat.search(stripped)
        assert not hit, f"{where}: {msg} -- found {hit.group(0)!r} in {text[:90]!r}"


def style(module):
    """Run :func:`check_text` over every student-facing string in a module."""
    code = module.TOPIC[0]
    spans = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _texts(item):
            check_text(text, f"{code} q{i}")
            spans += len(_SPAN.findall(text))
    print(f"OK  {code} notation: {len(module.QUESTIONS)} questions, {spans} hand-written "
          "math span(s), nothing typeset outside one.")


# ------------------------------------------------------------ negative control

_CONTROLS = [
    ("a backslash macro loose in prose", r"The value is 2\pi times the radius."),
    ("a bare caret in prose", "The concentration is 1.0 x 10^-3 molar."),
    ("a bare subscript in prose", "The formula unit is Ca_3(PO_4)_2 in the solid."),
    ("a slash fraction in prose", "The mole ratio of the two gases is 3/4 overall."),
    ("plain-text scientific notation", "There are 6.022 x 10 particles per mole."),
    ("a bare less-than sign", "The solution has pH < 7 at that point."),
    ("an unclosed math span", r"The mass is \(12.0 grams of carbon in the sample."),
    ("an unknown macro inside a span", r"The value is \(\frobnicate{4}\) overall."),
    ("unbalanced braces inside a span", r"The value is \(\frac{1}{2\) overall."),
    ("a span glued to the following word", r"A mass of \(2.0\)grams was weighed out."),
    ("a span glued to the preceding word", r"A mass of\(2.0\) grams was weighed out."),
    ("a Unicode superscript", "The count is 10²³ particles in the sample."),
]


def selftest():
    """Every pattern above must FAIL on text built to break it."""
    print("chem_notation negative controls:")
    for label, text in _CONTROLS:
        try:
            check_text(text, "control")
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:80]}")
            continue
        raise SystemExit(f"CONTROL FAILED: {label} did not raise on {text!r}")
    # ...and clean text must PASS, or the gate is merely a refusal machine.
    clean = [
        r"Avogadro's number is \(6.022 \times 10^{23}\) per mole of particles.",
        "A sample of H2SO4 was weighed on a balance to the nearest milligram.",
        r"The configuration \(1s^2\,2s^2\,2p^6\,3s^1\) has one valence electron.",
        r"The value of \(K_a\) is \(1.8 \times 10^{-5}\) at 25 degrees Celsius.",
        r"For the reaction \(\Delta H = -92\ \mathrm{kJ/mol}\) as written.",
        "The equation N2(g) + 3 H2(g) → 2 NH3(g) is balanced as written.",
    ]
    for text in clean:
        check_text(text, "clean control")
    print(f"  control OK  {len(clean)} clean strings passed unchanged.")
    print("all chem_notation controls behaved as required.")


if __name__ == "__main__":
    selftest()
