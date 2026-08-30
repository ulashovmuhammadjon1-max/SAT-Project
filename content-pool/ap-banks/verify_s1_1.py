"""Verification for AP STATISTICS 1.1.

Statistics is not symbolic algebra, so there is no sympy check here. Every key
that is a number is recomputed from the numbers in its own stem with plain
Python and matched against the text of the choice the module marks correct.
Items whose key is a definition or a piece of reasoning cannot be computed;
they are listed in CONCEPTUAL with the reasoning that justifies them, and they
still get the structural and distractor checks.

Run: python3 verify_s1_1.py
"""
import re

import s1_1

Q = s1_1.QUESTIONS

# Conceptual items (1-based). The reasoning for each is stated in the module's
# `why` field; what is recorded here is why no computation is possible.
CONCEPTUAL = {
    1: "definition of a statistical study (EK 1.1.A.1)",
    2: "definition of a population (EK 1.1.A.4)",
    3: "N is the population size, n the sample size (EK 1.1.A.4, 1.1.A.5)",
    4: "why studies sample rather than census (EK 1.1.A.2)",
    5: "datum vs data set (EK 1.1.A.3)",
    6: "what 'in context' means (EK 1.1.A.6)",
    7: "an investigative question is fixed before analysis (EK 1.1.B.1)",
    8: "an investigative question must be answerable with collectable data (EK 1.1.B.2)",
    9: "identification of N and n in a scenario (EK 1.1.A.4, 1.1.A.5)",
    13: "the population is everyone the question is about, not the ones measured",
    14: "the measured subset is the sample (EK 1.1.A.5)",
    15: "a statistic generally differs from the parameter (EK 1.2.A.5 / 1.1.A.5)",
    16: "a census is possible when the whole population is available (EK 1.1.A.2)",
    17: "datum vs data set (EK 1.1.A.3)",
    18: "a question with no measurable quantity is not investigable (EK 1.1.B.2)",
    19: "the investigative question concerns the population, not the sample",
    20: "an investigative question must define population and time frame (EK 1.1.B.2)",
    22: "N is a property of the population, not of the sample drawn from it",
    23: "components of a statistical study (EK 1.1.A)",
    24: "in-context reporting names quantity, units and individuals (EK 1.1.A.6)",
    25: "a statistic generally differs from the parameter it estimates (EK 1.2.A.5)",
}

NUM = re.compile(r"^-?[\d,]+(?:\.\d+)?%?$")


def key_text(n):
    """Text of the choice the module marks correct for question n (1-based)."""
    item = Q[n - 1]
    return item["choices"][item["ans"]]


def as_number(text):
    """Parse a choice that is a bare number or percent; None if it is prose."""
    t = text.strip().replace("$", "")
    if not NUM.match(t):
        return None
    if t.endswith("%"):
        return float(t[:-1].replace(",", "")) / 100.0
    return float(t.replace(",", ""))


def structural():
    assert len(Q) == 25, f"expected 25 questions, found {len(Q)}"
    for i, item in enumerate(Q, 1):
        assert len(item["choices"]) == 5, f"q{i}: AP Statistics needs exactly 5 choices"
        assert len(set(item["choices"])) == 5, f"q{i}: duplicate choice text"
        assert 0 <= item["ans"] < 5, f"q{i}: answer index out of range"
        assert item["q"].strip() and item["why"].strip(), f"q{i}: empty field"
        assert set(item) <= {"q", "choices", "ans", "why", "table"}, f"q{i}: stray key"
    stems = [item["q"] for item in Q]
    assert len(set(stems)) == len(stems), "duplicate stem inside the module"


def choices_numerically_distinct():
    """Two choices that are different strings but the same number make a
    question unanswerable. This defect has already shipped in five units of
    this project, so it is checked on every module."""
    for i, item in enumerate(Q, 1):
        vals = [as_number(c) for c in item["choices"]]
        seen = [v for v in vals if v is not None]
        for a in range(len(seen)):
            for b in range(a + 1, len(seen)):
                assert abs(seen[a] - seen[b]) > 1e-12, (
                    f"q{i}: two choices are the same number ({seen[a]})")


def computed():
    """Recompute every numeric key from its stem."""
    checks = []

    # q10: 310 households sampled from a population of 12,400.
    frac = 310 / 12400
    checks.append((10, frac, as_number(key_text(10))))

    # q11: a sample that is 4% of 21,000 students.
    n = 0.04 * 21000
    checks.append((11, n, as_number(key_text(11))))

    # q12: 96 members is 15% of the membership.
    N = 96 / 0.15
    checks.append((12, N, as_number(key_text(12))))

    # q21: shipping sampling fraction, 234 of 7,800.
    checks.append((21, 234 / 7800, as_number(key_text(21))))

    for qn, expected, keyed in checks:
        assert keyed is not None, f"q{qn}: key is not a parseable number"
        assert abs(expected - keyed) < 1e-9, (
            f"q{qn}: computed {expected}, module keys {keyed}")
    return len(checks)


def conceptual_accounted_for():
    computed_qs = {10, 11, 12, 21}
    covered = set(CONCEPTUAL) | computed_qs
    missing = set(range(1, 26)) - covered
    assert not missing, f"questions neither computed nor documented as conceptual: {sorted(missing)}"
    overlap = set(CONCEPTUAL) & computed_qs
    assert not overlap, f"questions marked conceptual but also computed: {sorted(overlap)}"


if __name__ == "__main__":
    structural()
    choices_numerically_distinct()
    conceptual_accounted_for()
    n = computed()
    print(f"s1_1: 25 questions, structure OK, choices numerically distinct, "
          f"{n} numeric keys recomputed, {len(CONCEPTUAL)} conceptual items documented.")
