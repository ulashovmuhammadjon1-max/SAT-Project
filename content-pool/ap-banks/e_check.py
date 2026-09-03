"""Shared gate for the AP ENVIRONMENTAL SCIENCE topic banks (prefix ``e``).

Every ``verify_e<unit>_<n>.py`` is thin: it imports its module, states one
``(anchor, claim)`` per question, supplies a ``table_checks`` callable for every
data item, and calls :func:`run`. Everything mechanical lives here so the same
gate runs identically on all thirty-three modules.

WHAT IS CHECKED
---------------
1. ``cg_check.check`` -- 30 questions, five distinct choices, a key in range, no
   choice wholly contained in another, a non-thin ``why`` and ``claim``, no
   option named by letter, no two stems opening alike, and the ANCHOR test:
   the anchor substring must appear in the keyed choice and in no distractor,
   so an off-by-one key or a reordered choice list fails here rather than
   reaching a student. ``export_units.py`` reshuffles choices, so a key stored
   as a bare index is one edit away from pointing at a distractor.
2. :func:`style` -- SCIENCE_BRIEF.md: Environmental Science is exported as
   prose and ``export_units.py`` does NOT typeset it, so a backslash macro
   would reach a student as literal text. A digit-hyphen-digit range and a
   digit-slash-digit fraction are the two shapes the converter mangled on the
   prose subjects; both are banned outright, so a year range is written
   "2000 to 2020" and a third is written in words.
3. Every question carrying a ``table`` must have a callable in ``table_checks``
   that recomputes the keyed conclusion FROM THAT TABLE ALONE.
   ``cg_check.check`` fails if one is missing, so a data question cannot ship
   unverified by being forgotten.

WHAT IS NOT CHECKED, stated plainly so nobody mistakes a pass for a warrant:
none of this can tell whether the environmental science is right. That is
gated by the CLAIMS text -- each of which must cite the essential-knowledge
statement the key rests on -- and by the rule in SCIENCE_BRIEF.md that a key
must trace to a sentence in the CED and an uncertain question is cut, never
guessed.

THE NEGATIVE CONTROL RUNS EVERY TIME, not behind a flag. A checker that cannot
fail is worse than none; this project has paid for that five separate times.
Before the real gate runs, :func:`run` corrupts a key, an anchor, a choice, a
``why``, the notation, and EVERY data table in turn, and requires each
corruption to raise. If a control does not raise, the module fails.

NO ``\\b`` ANYWHERE. A digit and a letter are both word characters, so ``\\b``
is silently not a boundary exactly where it looks like one.
"""
import copy
import re
import types

import cg_check as cg

_BANNED = [
    (re.compile(r"\\"), "a backslash: ENV_SCI is not typeset, so LaTeX would print raw"),
    (re.compile(r"(?<![A-Za-z])\d+\s?-\s?\d"), "a digit-hyphen-digit range: write 'to' instead"),
    (re.compile(r"\d\s?/\s?\d"), "a digit-slash-digit fraction: write it out in words"),
    (re.compile(r"\$"), "a dollar sign, which a converter reads as inline math"),
    (re.compile(r"(?<![A-Za-z])\^"), "a bare caret, which would render literally"),
]


def _texts(item):
    out = [item["q"], item["why"]] + list(item["choices"])
    t = item.get("table")
    if t:
        out += [str(h) for h in t["headers"]]
        out += [str(c) for r in t["rows"] for c in r]
    return out


def style(module):
    """No typeset notation anywhere in the module's student-facing text."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _texts(item):
            for pat, msg in _BANNED:
                hit = pat.search(text)
                assert not hit, (
                    f"{module.TOPIC[0]} q{i}: {msg} -- {hit.group(0)!r} in {text[:70]!r}"
                )


def no_figure_reference(module):
    """No stem may point at a picture the bank cannot show.

    A stem that says "the diagram shows" with nothing behind it is the defect
    this project has already shipped once. A stem may name a figure only when
    the question actually carries a ``table``.
    """
    pat = re.compile(
        r"(?<![a-z])(diagram|graph|figure|chart|photograph|image|map|illustration|"
        r"cross[ -]section|profile shown|pictured)(?![a-z])",
        re.IGNORECASE,
    )
    for i, item in enumerate(module.QUESTIONS, 1):
        hit = pat.search(item["q"])
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: stem names a {hit.group(0)!r} the bank cannot "
            f"show; put the data in a table= instead"
        )


# ------------------------------------------------------------------ corruptions

def _mutant(module):
    m = types.ModuleType(module.__name__ + "_mutant")
    m.TOPIC = module.TOPIC
    m.QUESTIONS = copy.deepcopy(module.QUESTIONS)
    return m


def _reverse_numbers(table):
    """Reverse each numeric column in place, keeping row labels put."""
    t = copy.deepcopy(table)
    width = len(t["headers"])
    for j in range(width):
        vals = [r[j] for r in t["rows"]]
        try:
            [cg.num(v) for v in vals]
        except AssertionError:
            continue
        if j == 0 and width > 1:
            continue
        for r, v in zip(t["rows"], reversed(vals)):
            r[j] = v
    return t


def _flatten_numbers(table):
    """Replace every numeric cell outside the label column with the same value."""
    t = copy.deepcopy(table)
    width = len(t["headers"])
    for r in t["rows"]:
        for j in range(width):
            if j == 0 and width > 1:
                continue
            try:
                cg.num(r[j])
            except AssertionError:
                continue
            r[j] = "1"
    return t


def _controls(module, claims, table_checks):
    """Every gate must FAIL when its input is corrupted. Raises if one does not."""
    fired = []

    def must_fail(label, mutate):
        mod = _mutant(module)
        cl = list(claims)
        try:
            cl = mutate(mod, cl) or cl
            style(mod)
            no_figure_reference(mod)
            cg.check(mod, cl, table_checks=table_checks)
        except AssertionError:
            fired.append(label)
            return True
        return False

    def require(label, mutate):
        assert must_fail(label, mutate), (
            f"{module.TOPIC[0]} CONTROL FAILED: {label} did not raise"
        )

    def move_key(mod, cl):
        mod.QUESTIONS[0]["ans"] = (mod.QUESTIONS[0]["ans"] + 1) % 5

    def break_anchor(mod, cl):
        return [("no such phrase appears anywhere", cl[0][1])] + list(cl[1:])

    def duplicate_choice(mod, cl):
        q = mod.QUESTIONS[1]
        q["choices"][(q["ans"] + 1) % 5] = q["choices"][q["ans"]]

    def thin_why(mod, cl):
        mod.QUESTIONS[2]["why"] = "Because it is."

    def letter_reference(mod, cl):
        mod.QUESTIONS[3]["why"] = (
            "The reason the framework gives is that option B restates the "
            "definition rather than applying it to the case described."
        )

    def latex_slips_in(mod, cl):
        mod.QUESTIONS[4]["choices"][0] = "About \\frac{1}{3} of the water is lost"

    def year_range_slips_in(mod, cl):
        mod.QUESTIONS[5]["q"] = mod.QUESTIONS[5]["q"] + " Between 2000-2020, what changed?"

    def figure_reference_slips_in(mod, cl):
        mod.QUESTIONS[6]["q"] = "According to the diagram, which statement is accurate?"

    require("key moved off its anchor", move_key)
    require("anchor no longer in the keyed choice", break_anchor)
    require("a distractor made identical to the key", duplicate_choice)
    require("a why reduced below the minimum", thin_why)
    require("a why naming an option by letter", letter_reference)
    require("a backslash macro in a choice", latex_slips_in)
    require("a digit-hyphen-digit year range in a stem", year_range_slips_in)
    require("a stem pointing at a figure the bank cannot show", figure_reference_slips_in)

    # Every data item's arithmetic, independently.
    for i in sorted(table_checks or {}):
        def corrupt(mod, cl, i=i, how=_reverse_numbers):
            mod.QUESTIONS[i - 1]["table"] = how(mod.QUESTIONS[i - 1]["table"])

        label = f"table for q{i} corrupted"
        if not must_fail(label, corrupt):
            def flatten(mod, cl, i=i):
                mod.QUESTIONS[i - 1]["table"] = _flatten_numbers(mod.QUESTIONS[i - 1]["table"])

            assert must_fail(label + " (flattened)", flatten), (
                f"{module.TOPIC[0]} CONTROL FAILED: the check for q{i} still passes "
                f"when its table is reversed AND flattened, so it is not reading the data"
            )
    return len(fired)


def run(module, claims, table_checks=None):
    """Negative-control every gate, then run the gate for real."""
    table_checks = table_checks or {}
    n = _controls(module, claims, table_checks)
    style(module)
    no_figure_reference(module)
    cg.check(module, claims, table_checks=table_checks)
    print(f"    {n} negative controls all raised as required "
          f"({len(table_checks)} data item(s) among them).")
