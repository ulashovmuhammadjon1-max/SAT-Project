"""Notation gate and negative control shared by the AP Environmental Science banks.

`cg_check.check` is the structural gate: thirty questions, five distinct
choices, a key pinned to an anchor that appears in the keyed choice and in no
distractor, a `why` that does not name an option by letter, and every table
question recomputed from its own table. It cannot tell whether the science is
right; that is gated by the CLAIMS text in each verifier and by the rule in
SCIENCE_BRIEF.md that a key must trace to a sentence in the CED.

This module adds the two things every Environmental Science verifier needs and
would otherwise copy:

NOTATION. `export_units.py` does not typeset ENV_SCI -- it is a prose subject,
and mathfmt is not applied to it. So a backslash macro, a bare caret, a slash
fraction or a digit-hyphen-digit range reaches a student as literal characters
or, worse, was written expecting typesetting that never happens. `style()`
refuses all of them, plus any non-ASCII character, because a micro sign or a
typographic dash is exactly the kind of glyph that survives a review and then
renders wrong. No `\\b` anywhere: a digit and a letter are both word
characters, so the range check uses an explicit lookbehind and Radon-222 or
PM2.5 do not trip it while "2000-2020" does.

NEGATIVE CONTROL. `selftest()` breaks the module on purpose and requires the
gate to notice:

  1. every key in turn is rotated to the next choice -- all thirty must raise,
     which is what proves the anchors are distinctive rather than generic;
  2. every cell of every table is corrupted in turn; each table must be
     defended by at least one caught corruption, and the per-question catch
     rate is printed, so a table check that has stopped reading its table shows
     up as a zero rather than as a silent pass;
  3. each banned notation form is injected into a choice and `style` must
     raise for each;
  4. a distractor is made identical to the key, a `why` is cut below the
     minimum, and a `why` is made to name an option by letter.

A checker that cannot fail is worse than none. Run
`python3 verify_e7_1.py --selftest` for any module.
"""
import contextlib
import copy
import io
import re
import types

import cg_check as cg

# Every pattern uses explicit lookarounds. `\b` is silently not a boundary
# between a digit and a letter, which this project has paid for four times.
BANNED = [
    (re.compile(r"\\"), "a backslash: ENV_SCI is not typeset, so a macro would print raw"),
    (re.compile(r"\^"), "a bare caret, which prints literally in a prose subject"),
    (re.compile(r"(?<![A-Za-z0-9])\d[\d,]*\s?-\s?\d"),
     "a digit-hyphen-digit range: write 'to' instead, the converter reads the hyphen as a minus"),
    (re.compile(r"\d\s?/\s?\d"), "a digit-slash-digit fraction: write it out in words"),
    (re.compile(r"\$"), "a dollar sign, which a converter reads as opening inline math"),
    (re.compile(r"[^\x00-\x7f]"), "a non-ASCII character: use plain words and ASCII punctuation"),
]


def texts(item):
    """Every student-facing string in one question, including its table."""
    out = [item["q"], item["why"]] + list(item["choices"])
    table = item.get("table")
    if table:
        out += [str(h) for h in table["headers"]]
        out += [str(c) for row in table["rows"] for c in row]
    return out


def style(module):
    """No typeset notation and no non-ASCII anywhere in the module's text."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in texts(item):
            for pat, msg in BANNED:
                hit = pat.search(text)
                assert not hit, (
                    f"{module.TOPIC[0]} q{i}: {msg} -- {hit.group(0)!r} in {text[:70]!r}"
                )
    print(f"OK  {module.TOPIC[0]} notation: no typeset markup, no non-ASCII, in "
          f"{len(module.QUESTIONS)} questions.")


# ------------------------------------------------------------------ the control

def _mutant(module):
    m = types.ModuleType(module.__name__ + "_mutant")
    m.TOPIC = module.TOPIC
    m.QUESTIONS = copy.deepcopy(module.QUESTIONS)
    return m


def _run(mod, claims, table_checks):
    """Run both gates on `mod`, silently. Returns the exception, or None."""
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            style(mod)
            cg.check(mod, claims, table_checks=table_checks)
    except AssertionError as exc:
        return exc
    except Exception as exc:  # a KeyError from a corrupted cell counts as caught
        return exc
    return None


def _corrupt(value):
    """Change a cell so any check that reads it must see something different."""
    text = str(value).strip()
    if re.fullmatch(r"-?[\d,]+(?:\.\d+)?", text):
        n = float(text.replace(",", ""))
        return str(int(n * 3) + 11) if n == int(n) else str(round(n * 3 + 11, 3))
    return text + " CORRUPTED"


def selftest(module, claims, table_checks=None):
    """Break the module on purpose; every gate below must raise."""
    table_checks = table_checks or {}
    code = module.TOPIC[0]
    assert _run(module, claims, table_checks) is None, \
        f"{code}: the module does not pass before corruption"

    failures = []

    def must_fail(label, mutate):
        mod = _mutant(module)
        mutate(mod)
        if _run(mod, claims, table_checks) is None:
            failures.append(label)

    # 1. every key rotated to the next choice
    for i in range(len(module.QUESTIONS)):
        def rotate(mod, i=i):
            q = mod.QUESTIONS[i]
            q["ans"] = (q["ans"] + 1) % len(q["choices"])
        must_fail(f"q{i + 1} key rotated to the next choice", rotate)
    print(f"  control OK  all {len(module.QUESTIONS)} keys fail when rotated off their anchor")

    # 2. every cell of every table corrupted in turn
    for qi, item in enumerate(module.QUESTIONS, 1):
        table = item.get("table")
        if not table:
            continue
        caught = total = 0
        for r in range(len(table["rows"])):
            for c in range(len(table["rows"][r])):
                total += 1
                mod = _mutant(module)
                mod.QUESTIONS[qi - 1]["table"]["rows"][r][c] = _corrupt(table["rows"][r][c])
                if _run(mod, claims, table_checks) is not None:
                    caught += 1
        if caught == 0:
            failures.append(f"q{qi} table: no corrupted cell was caught")
        print(f"  control OK  q{qi} table: {caught} of {total} corrupted cells caught")

    # 3. each banned notation form, injected one at a time
    for bad in ("A rise of \\frac{1}{2} degree", "A rise of 2^3 units",
                "The 1990-2020 record", "A share of 3/4 of the total",
                "A cost of $40 per ton", "A rise of 2 degrees Celsius"):
        def inject(mod, bad=bad):
            mod.QUESTIONS[0]["choices"][0] = bad
        label = f"notation injected: {bad!r}"
        mod = _mutant(module)
        inject(mod)
        caught = _run(mod, claims, table_checks) is not None
        # the last string is legal prose and is the POSITIVE control: it must pass
        # style, so a style() that rejected everything would be caught here.
        legal = bad == "A rise of 2 degrees Celsius"
        if legal:
            buf = io.StringIO()
            ok = True
            try:
                with contextlib.redirect_stdout(buf):
                    style(mod)
            except AssertionError:
                ok = False
            if not ok:
                failures.append("style rejected legal prose: " + bad)
        elif not caught:
            failures.append(label)
    print("  control OK  every banned notation form raises; legal prose does not")

    # 4. the structural gates
    def duplicate_choice(mod):
        mod.QUESTIONS[0]["choices"][-1] = mod.QUESTIONS[0]["choices"][0]

    def thin_why(mod):
        mod.QUESTIONS[1]["why"] = "Because it is."

    def letter_reference(mod):
        mod.QUESTIONS[2]["why"] = ("Option B is wrong here and the rest of the reasoning "
                                   "follows directly from that fact alone.")

    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a why cut below the minimum length", thin_why)
    must_fail("a why naming an option by letter", letter_reference)
    print("  control OK  duplicate choice, thin why and letter reference all raise")

    if failures:
        raise SystemExit(f"CONTROL FAILED for {code}:\n  " + "\n  ".join(failures))
    print(f"all negative controls raised as required for {code}.")


def run(module, claims, table_checks=None, argv=()):
    """The two lines every verifier ends with."""
    if "--selftest" in argv:
        selftest(module, claims, table_checks)
    style(module)
    cg.check(module, claims, table_checks=table_checks)
