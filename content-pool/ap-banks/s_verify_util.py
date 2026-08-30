"""Shared checking helpers for the AP Statistics (Units 3-4, inference) verifiers.

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

    def check(self, q, expected, tol=0.02, note=""):
        """Question ``q`` (1-based) must key the unique choice matching ``expected``.

        ``expected`` is a number or a sequence of numbers -- every number the
        keyed choice states, in the order it states them. ``tol`` is relative.
        """
        if isinstance(expected, (int, float)):
            expected = [expected]
        expected = [float(v) for v in expected]
        item = self.m.QUESTIONS[q - 1]
        hits = [i for i, c in enumerate(item["choices"]) if _match(numvec(c), expected, tol)]
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
        for i, item in enumerate(self.m.QUESTIONS, 1):
            vecs = [numvec(c) for c in item["choices"]]
            for a in range(len(vecs)):
                for b in range(a + 1, len(vecs)):
                    if vecs[a] and vecs[a] == vecs[b]:
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
