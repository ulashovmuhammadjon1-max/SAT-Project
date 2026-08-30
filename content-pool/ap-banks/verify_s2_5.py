"""Verification for AP STATISTICS 2.5, mutually exclusive events.

Sample spaces are enumerated, so every disjointness claim is settled by actually
intersecting the two event sets rather than by reasoning about them. That is the
point of the topic: mutual exclusivity is the statement that the intersection is
empty, and here it is checked as one.

`disjoint_implies_dependent` is the load-bearing check. Items 17, 18 and 25 rest
on the claim that two mutually exclusive events with positive probability are
necessarily DEPENDENT, which is the opposite of what students expect. It is
proved here on a concrete sample space by computing P(A given B) and showing it
is 0 while P(A) is positive -- and, alongside it, an independent pair is
constructed on the same sample space and shown to be non-disjoint, so the two
properties are demonstrated to be different rather than merely asserted to be.

`fraction_choices_are_distinct` compares fraction-valued choices by value, since
the shared checker reads "1/2" as the pair (1, 2) and would not notice "2/4".

Run: python3 verify_s2_5.py
"""
from fractions import Fraction

import s_verify_util as U

import s2_5

c = U.Checker(s2_5)
Q = s2_5.QUESTIONS


def fraction_choices_are_distinct():
    for i, item in enumerate(Q, 1):
        seen = {}
        for choice in item["choices"]:
            try:
                value = Fraction(choice.strip())
            except (ValueError, ZeroDivisionError):
                continue
            assert value not in seen, (
                f"q{i}: {seen[value]!r} and {choice!r} are the same number ({float(value)})")
            seen[value] = choice


fraction_choices_are_distinct()

# --- sample spaces --------------------------------------------------------------
SUITS = ["hearts", "diamonds", "clubs", "spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
DECK = [(r, s) for s in SUITS for r in RANKS]
DICE = [(a, b) for a in range(1, 7) for b in range(1, 7)]
SPINNER10 = list(range(1, 11))
assert (len(DECK), len(DICE), len(SPINNER10)) == (52, 36, 10)


def prob(event, space):
    return Fraction(len(event), len(space))


def disjoint(a, b):
    return not (set(a) & set(b))


# --- disjoint sums, complements -------------------------------------------------
c.check(3, 0)                                       # P(A and B) = 0 when disjoint
c.check(5, 0.35 + 0.40)                             # 0.75
c.check(6, 0.0)                                     # joint probability of disjoint events
c.check(7, 1 - (0.35 + 0.40))                       # neither: 0.25
assert abs(0.35 * 0.40 - 0.14) < 1e-12, "q5: 0.14 is the product distractor, which would need independence"

# --- cards ----------------------------------------------------------------------
hearts = [c_ for c_ in DECK if c_[1] == "hearts"]
spades = [c_ for c_ in DECK if c_[1] == "spades"]
kings = [c_ for c_ in DECK if c_[0] == "K"]
reds = [c_ for c_ in DECK if c_[1] in ("hearts", "diamonds")]
faces = [c_ for c_ in DECK if c_[0] in ("J", "Q", "K")]

# q8: exactly one of the offered pairs is disjoint.
pairs = {
    "heart & king": (hearts, kings),
    "heart & red": (hearts, reds),
    "heart & spade": (hearts, spades),
    "face & king": (faces, kings),
    "red & ace": (reds, [c_ for c_ in DECK if c_[0] == "A"]),
}
disjoint_pairs = [name for name, (a, b) in pairs.items() if disjoint(a, b)]
assert disjoint_pairs == ["heart & spade"], f"q8: disjoint pairs are {disjoint_pairs}"

heart_or_spade = set(hearts) | set(spades)
assert len(heart_or_spade) == 26
c.check(9, [1, 2])
assert prob(heart_or_spade, DECK) == Fraction(1, 2) == prob(hearts, DECK) + prob(spades, DECK), (
    "q9: disjoint events add exactly")

heart_and_king = set(hearts) & set(kings)
assert heart_and_king == {("K", "hearts")}, "q10: exactly the king of hearts"
c.check(10, [1, 52])
assert prob(heart_and_king, DECK) != 0, "q10: hearts and kings are NOT mutually exclusive"

heart_or_king = set(hearts) | set(kings)
assert len(heart_or_king) == 16
c.check(11, [4, 13])
assert prob(heart_or_king, DECK) == Fraction(4, 13)
assert (prob(hearts, DECK) + prob(kings, DECK) - prob(heart_and_king, DECK)
        == prob(heart_or_king, DECK)), "q11: the addition rule must reproduce the enumeration"
assert prob(hearts, DECK) + prob(kings, DECK) == Fraction(17, 52), (
    "q11: 17/52 is the forgot-to-subtract-the-overlap distractor")

# --- dice -----------------------------------------------------------------------
sum7 = [d for d in DICE if sum(d) == 7]
sum11 = [d for d in DICE if sum(d) == 11]
first3 = [d for d in DICE if d[0] == 3]
even_sum = [d for d in DICE if sum(d) % 2 == 0]
first2 = [d for d in DICE if d[0] == 2]
at_least_8 = [d for d in DICE if sum(d) >= 8]
at_least_10 = [d for d in DICE if sum(d) >= 10]
match = [d for d in DICE if d[0] == d[1]]

dice_pairs = {
    "7 & first is 3": (sum7, first3),
    "7 & 11": (sum7, sum11),
    "even & first is 2": (even_sum, first2),
    ">=8 & >=10": (at_least_8, at_least_10),
    "match & even": (match, even_sum),
}
dice_disjoint = [name for name, (a, b) in dice_pairs.items() if disjoint(a, b)]
assert dice_disjoint == ["7 & 11"], f"q12: disjoint dice pairs are {dice_disjoint}"

assert (len(sum7), len(sum11)) == (6, 2)
c.check(13, [2, 9])
assert prob(set(sum7) | set(sum11), DICE) == Fraction(8, 36) == Fraction(2, 9)

# --- bounds on a joint probability ----------------------------------------------
pa, pb = 0.6, 0.7
assert pa + pb > 1, "q14: disjointness would force P(A or B) = 1.3, which is impossible"
smallest_joint = pa + pb - 1.0
assert abs(smallest_joint - 0.30) < 1e-9, f"q15: the minimum joint probability is {smallest_joint}"
c.check(15, smallest_joint)

# --- the addition rule run backwards --------------------------------------------
joint_19 = 0.30 + 0.50 - 0.80
assert abs(joint_19) < 1e-12, "q19: P(A and B) = 0, so the events are mutually exclusive"
joint_20 = 0.30 + 0.50 - 0.65
assert abs(joint_20 - 0.15) < 1e-9, f"q20: P(A and B) = {joint_20}"
c.check(20, joint_20)

# --- the spinner ----------------------------------------------------------------
mult3 = [s for s in SPINNER10 if s % 3 == 0]
mult5 = [s for s in SPINNER10 if s % 5 == 0]
assert mult3 == [3, 6, 9] and mult5 == [5, 10]
assert disjoint(mult3, mult5), "q21: within 1 to 10 no number is a multiple of both"
assert 15 % 3 == 0 and 15 % 5 == 0 and 15 not in SPINNER10, (
    "q21: 15 would overlap but lies outside this sample space, which is the distractor")
c.check(22, float(prob(set(mult3) | set(mult5), SPINNER10)))     # 0.5

# --- three pairwise disjoint events ---------------------------------------------
union_abc = 0.2 + 0.3 + 0.4
assert abs(union_abc - 0.9) < 1e-12
c.check(23, 1 - union_abc)                                       # 0.1


def disjoint_implies_dependent():
    """q17, q18, q25: disjoint with positive probability means DEPENDENT.

    Proved on the dice sample space. A is 'sum is 7' and B is 'sum is 11': both
    have positive probability and they are disjoint, so P(A given B) = 0 while
    P(A) = 1/6. An independent, non-disjoint pair is built on the same space for
    contrast, so the two properties are shown to be different, not merely said
    to be.
    """
    A, B = sum7, sum11
    assert prob(A, DICE) > 0 and prob(B, DICE) > 0, "both events must be possible"
    assert disjoint(A, B)
    p_a_given_b = Fraction(len(set(A) & set(B)), len(B))
    assert p_a_given_b == 0, "disjointness forces the conditional probability to 0"
    assert prob(A, DICE) == Fraction(1, 6) and p_a_given_b != prob(A, DICE), (
        "q17/q18: P(A given B) differs from P(A), so the events are dependent")

    # Contrast: 'first die is 3' and 'second die is 5' are independent and NOT
    # disjoint -- the outcome (3, 5) belongs to both.
    C = [d for d in DICE if d[0] == 3]
    D = [d for d in DICE if d[1] == 5]
    assert not disjoint(C, D), "an independent pair here is not disjoint"
    p_c_given_d = Fraction(len(set(C) & set(D)), len(D))
    assert p_c_given_d == prob(C, DICE), "q25: independence is P(C given D) = P(C)"
    assert prob(set(C) & set(D), DICE) == prob(C, DICE) * prob(D, DICE)

    # So the two properties genuinely come apart: one pair is disjoint and
    # dependent, the other independent and overlapping.
    assert disjoint(A, B) and not disjoint(C, D)
    assert p_a_given_b != prob(A, DICE) and p_c_given_d == prob(C, DICE)


disjoint_implies_dependent()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 2.5.A.1: the joint probability is the probability of the intersection, that both events occur.")
c.conceptual(2, "EK 2.5.A.2: mutually exclusive, or disjoint, means the events cannot occur at the same time.")
c.conceptual(4, "EK 2.5.A.2 with 2.7.A.3: the addition rule subtracts P(A and B), which is 0 for disjoint events.")
c.conceptual(8, "EK 2.5.A.2: enumerated above -- 'heart and spade' is the only pair among the options with an empty intersection.")
c.conceptual(12, "EK 2.5.A.2: enumerated above -- 'sum is 7' and 'sum is 11' is the only disjoint pair among the options.")
c.conceptual(14, "EK 2.5.A.2: computed above -- disjointness would force P(A or B) = 1.3, so the events must overlap.")
c.conceptual(16, "EK 2.5.A.2: an event and its complement share no outcome, so they are always mutually exclusive as well as exhaustive.")
c.conceptual(17, "EK 2.5.A.2 with 2.7.A.1: proved above -- for two disjoint events of positive probability, P(A given B) = 0 while P(A) > 0, so they are dependent.")
c.conceptual(18, "EK 2.5.A.2 with 2.7.A.1: proved above -- mutual exclusivity and independence are different properties and, for positive-probability events, incompatible.")
c.conceptual(19, "EK 2.5.A.2: computed above -- the addition rule gives P(A and B) = 0, which is exactly what mutually exclusive means.")
c.conceptual(21, "EK 2.5.A.2: enumerated above -- multiples of 3 are 3, 6, 9 and of 5 are 5, 10, with no overlap inside this sample space.")
c.conceptual(24, "EK 2.5.A.2: each unit is cross-classified into exactly one row, so distinct rows are disjoint and together exhaust the table.")
c.conceptual(25, "EK 2.5.A.2 with 2.7.A.1: proved above -- disjointness is the empty-intersection test, whereas P(A given B) = P(A) tests independence.")

c.finish()
