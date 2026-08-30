"""Shared checking helpers for the AP Statistics Units 4-5 verifiers.

Every ``verify_s<unit>_<topic>.py`` in this directory imports this module. The
contract each verifier honours:

* every question index 1..25 is accounted for exactly once -- either it is
  checked numerically by :func:`check`, or it is declared conceptual by
  :func:`conceptual` with a one-line statement of the reasoning. ``finish``
  fails if any index is missing, so a question cannot escape the gate by being
  forgotten.
* a numeric check recomputes the answer from the stem's own numbers with
  scipy/numpy/statistics -- never from a recalled table value -- and then
  requires that the *keyed* choice is the one and only choice matching it.
  That second half is the duplicate-key guard: a distractor that is
  accidentally equal to the answer makes the question unanswerable, and this
  project has shipped that defect five times already.
* :func:`finish` additionally checks every question's choices are pairwise
  distinct as *numbers*, not merely as strings, so "0.50" and "0.5" collide.

Numbers are compared as vectors, so a confidence-interval choice written
"(0.412, 0.508)" is checked endpoint by endpoint, and a choice written
"z = 2.14, p-value = 0.0162" is checked on both values at once.
"""
import re

# A signed decimal, optionally in scientific notation. Thousands separators are
# stripped before matching so "1,250" reads as one number, not two.
_NUM = re.compile(r"-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?")


def numvec(text):
    """Every number in ``text``, in order, as floats."""
    return [float(t) for t in _NUM.findall(text.replace(",", ""))]


_WORD = re.compile(r"[A-Za-z]+")

# Words that are allowed to appear in a choice that still counts as "numeric in
# style" -- units, and the handful of connectives a numeric answer needs.
_UNIT_WORDS = {
    "minutes", "minute", "hours", "hour", "seconds", "second", "days", "day",
    "years", "year", "weeks", "week", "months", "month",
    "kg", "g", "mg", "cm", "mm", "m", "km", "in", "ft", "lb", "lbs", "oz",
    "ml", "l", "students", "people", "adults", "residents", "households",
    "points", "degrees", "dollars", "and", "to", "or", "about", "z", "t", "p",
    "df", "value", "n", "x", "s", "chi", "square", "approximately", "percent",
    "percentage", "than", "less", "greater", "more", "at", "least", "most",
    "mean", "standard", "deviation", "variance", "median", "with", "against",
    "for", "from", "mm", "grams", "kilograms", "cm2", "b", "r", "se", "slope",
    "intercept", "chirps", "mpg", "beats", "sample", "margin", "error", "width", "of", "point", "estimate",
}


def numeric_style(text):
    """True when ``text`` reads as a number (with units), not as prose.

    Used to decide which choices may be compared as numbers. A choice with more
    than two non-unit words is prose, and its digits are incidental.
    """
    if not _NUM.search(text):
        return False
    stray = [w for w in _WORD.findall(text.lower()) if w not in _UNIT_WORDS]
    return len(stray) <= 2


# Relational markers. Two choices carrying the same numbers but different
# relations -- "Ha: mu > 500" against "Ha: mu < 500" -- are different answers,
# so the duplicate check compares relations alongside numbers. Without this the
# check reports every pair of one-sided hypotheses as a duplicate, which is the
# over-matching failure that makes a checker worth ignoring. A space-delimited
# + or - counts as a relation too, because "yhat = 12.85 + 3.42x" and
# "yhat = 12.85 - 3.42x" carry identical NUMBERS -- numvec cannot claim the
# minus, since a digit does not follow it immediately -- and are nonetheless
# different answers.
_REL = re.compile(
    r"<=|>=|!=|<|>|=|(?<=\s)[+-](?=\s)|\bnot equal\b|\bgreater\b|\bless\b|"
    r"\bfewer\b|\bmore\b|\bexceeds?\b|\babove\b|\bbelow\b|\bat least\b|"
    r"\bat most\b",
    re.IGNORECASE,
)


def signature(text):
    """The comparable content of a choice: its relations and its numbers."""
    lowered = text.lower()
    return (tuple(m.group(0) for m in _REL.finditer(lowered)), tuple(numvec(text)))


def _match(vec, expected, tol):
    if len(vec) != len(expected):
        return False
    return all(abs(a - b) <= tol * max(1.0, abs(b)) for a, b in zip(vec, expected))


class Checker:
    """Accumulates the per-question verdicts for one topic module."""

    def __init__(self, module, total=25):
        self.m = module
        self.total = total
        self.seen = {}
        assert len(module.QUESTIONS) == total, (
            f"{module.TOPIC[0]}: expected {total} questions, found {len(module.QUESTIONS)}"
        )

    def check(self, q, expected, tol=0.002, note=""):
        """Question ``q`` (1-based) must key the unique choice matching ``expected``.

        ``expected`` is a number or a sequence of numbers -- every number the
        keyed choice states, in the order it states them. ``tol`` is relative.
        """
        if isinstance(expected, (int, float)):
            expected = [expected]
        expected = [float(v) for v in expected]
        item = self.m.QUESTIONS[q - 1]
        assert numeric_style(item["choices"][item["ans"]]), (
            f"q{q}: check() is for numeric answers, but the key "
            f"{item['choices'][item['ans']]!r} reads as prose"
        )
        hits = [i for i, c in enumerate(item["choices"])
                if numeric_style(c) and _match(numvec(c), expected, tol)]
        assert hits, (
            f"q{q}: computed {expected} matches no choice; choices={item['choices']}"
        )
        assert len(hits) == 1, (
            f"q{q}: computed {expected} matches {len(hits)} choices "
            f"{[item['choices'][i] for i in hits]} -- the question is unanswerable"
        )
        assert hits[0] == item["ans"], (
            f"q{q}: computed {expected} is choice {hits[0]} "
            f"({item['choices'][hits[0]]!r}) but the key says {item['ans']} "
            f"({item['choices'][item['ans']]!r})"
        )
        self.seen[q] = note or "computed"

    def conceptual(self, q, reason):
        """Question ``q`` carries no computable answer; ``reason`` states why the key holds."""
        assert reason and len(reason) > 15, f"q{q}: conceptual questions need a real reason"
        self.seen[q] = f"conceptual: {reason}"

    def finish(self):
        missing = [q for q in range(1, self.total + 1) if q not in self.seen]
        assert not missing, f"{self.m.TOPIC[0]}: questions not verified at all: {missing}"
        # Pairwise numeric distinctness, over and above the exporter's string check.
        # Only choices that are *numeric in style* are compared this way. A prose
        # choice such as "computed with n - 1 in the denominator" carries a stray
        # 1, and comparing those numbers would report every such pair as a
        # duplicate -- an over-matching check is worse than no check, because it
        # trains you to ignore the output.
        for i, item in enumerate(self.m.QUESTIONS, 1):
            vecs = [signature(c) if numeric_style(c) else None for c in item["choices"]]
            for a in range(len(vecs)):
                for b in range(a + 1, len(vecs)):
                    if vecs[a] and vecs[a][1] and vecs[a] == vecs[b]:
                        raise AssertionError(
                            f"q{i}: choices {a} and {b} are the same number(s): "
                            f"{item['choices'][a]!r} / {item['choices'][b]!r}"
                        )
            assert len(item["choices"]) == 5, f"q{i}: AP Statistics needs five choices"
            assert 0 <= item["ans"] < 5, f"q{i}: answer index out of range"
        code, title, unit = self.m.TOPIC
        ncomp = sum(1 for v in self.seen.values() if not v.startswith("conceptual"))
        print(f"{code} {title}: {self.total} questions verified "
              f"({ncomp} computed, {self.total - ncomp} conceptual)")
