"""Verification for AP STATISTICS 2.4, introduction to probability.

Every probability here is obtained by ENUMERATING the sample space -- 36 ordered
dice pairs, 4 coin sequences, 52 cards, 8 spinner sectors -- and counting the
favourable outcomes. Nothing is quoted from memory: P(sum of 7) is counted, and
so is the number of face cards.

Two details of this module needed their own guards.

`fraction_choices_are_distinct` compares every choice that is written as a
fraction BY VALUE, using `fractions.Fraction`. The shared checker compares the
numbers a choice contains, so it reads "5/6" as the pair (5, 6) and "30/36" as
(30, 36) and sees two different answers -- which they are as text and are not as
numbers. A first draft of this module really did offer 5/6 and 30/36 in the same
question, and 1/18 alongside 2/36 in another; both were caught by this check and
rewritten. It runs over all 25 questions, not only the ones with fraction keys.

`check_fraction` then pins a fraction key by its (numerator, denominator) pair
while separately asserting that the pair equals the enumerated probability, so
the arithmetic is verified even though the choice is matched as text.

Run: python3 verify_s2_4.py
"""
from fractions import Fraction
from itertools import product
import re

import s_verify_util as U

import s2_4

c = U.Checker(s2_4)
Q = s2_4.QUESTIONS

_FRACTION_TEXT = re.compile(r"^\d+\s*/\s*\d+$")


def fraction_choices_are_distinct():
    """No two choices in a question may be the same number written differently."""
    for i, item in enumerate(Q, 1):
        seen = {}
        for choice in item["choices"]:
            text = choice.strip()
            try:
                value = Fraction(text)
            except (ValueError, ZeroDivisionError):
                continue
            if value in seen:
                raise AssertionError(
                    f"q{i}: {seen[value]!r} and {choice!r} are the same number "
                    f"({float(value)}), which makes the question unanswerable")
            seen[value] = choice


def check_fraction(qn, numerator, denominator, expected):
    """Pin a fraction-valued key, having first confirmed it equals `expected`."""
    assert Fraction(numerator, denominator) == Fraction(expected).limit_denominator(10**6), (
        f"q{qn}: the key {numerator}/{denominator} does not equal the computed {expected}")
    key = Q[qn - 1]["choices"][Q[qn - 1]["ans"]].strip()
    assert _FRACTION_TEXT.match(key), (
        f"q{qn}: the key {key!r} is not written as a plain fraction")
    assert Fraction(key) == Fraction(numerator, denominator), (
        f"q{qn}: the key reads {key!r} but was checked as {numerator}/{denominator}")
    c.check(qn, [numerator, denominator])


fraction_choices_are_distinct()

# --- enumerate the sample spaces ------------------------------------------------
DICE = [(a, b) for a in range(1, 7) for b in range(1, 7)]
assert len(DICE) == 36

COINS = ["".join(t) for t in product("HT", repeat=2)]
assert len(COINS) == 4 and sorted(COINS) == ["HH", "HT", "TH", "TT"]

SUITS = ["hearts", "diamonds", "clubs", "spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
DECK = [(r, s) for s in SUITS for r in RANKS]
assert len(DECK) == 52 and len(RANKS) == 13

SPINNER = list(range(1, 9))
assert len(SPINNER) == 8


def p(favourable, total):
    return Fraction(favourable, total)


# --- complements and legality ---------------------------------------------------
c.check(5, 1 - 0.28)                                  # 0.72
c.check(6, 1 - 0.15)                                  # 0.85
c.check(7, 1.4)                                       # the value that cannot be a probability
assert not (0 <= 1.4 <= 1), "q7: 1.4 lies outside [0, 1]"
for legal in (0, 0.001, 0.5, 1):
    assert 0 <= legal <= 1, f"q7: {legal} must be a legal probability, so it is a distractor"

# --- two dice -------------------------------------------------------------------
c.check(8, len(DICE))                                 # 36

sum7 = [d for d in DICE if sum(d) == 7]
assert len(sum7) == 6, f"there are {len(sum7)} ways to roll a sum of 7"
check_fraction(9, 1, 6, p(len(sum7), len(DICE)))

sum2 = [d for d in DICE if sum(d) == 2]
assert sum2 == [(1, 1)], "only (1, 1) sums to 2"
check_fraction(10, 1, 36, p(len(sum2), len(DICE)))

not7 = [d for d in DICE if sum(d) != 7]
assert len(not7) == 30 and len(not7) + len(sum7) == len(DICE)
check_fraction(11, 5, 6, p(len(not7), len(DICE)))
assert p(len(not7), len(DICE)) == 1 - p(len(sum7), len(DICE)), "the complement must agree"

doubles = [d for d in DICE if d[0] == d[1]]
assert len(doubles) == 6
check_fraction(12, 1, 6, p(len(doubles), len(DICE)))

at_least_10 = [d for d in DICE if sum(d) >= 10]
assert len(at_least_10) == 6, f"sums of 10, 11, 12 arise {len(at_least_10)} ways"
assert sorted(sum(d) for d in at_least_10).count(10) == 3
check_fraction(13, 1, 6, p(len(at_least_10), len(DICE)))

# --- two coin tosses ------------------------------------------------------------
exactly_one_head = [s for s in COINS if s.count("H") == 1]
assert len(exactly_one_head) == 2
c.check(14, float(p(len(exactly_one_head), len(COINS))))          # 0.50

at_least_one_head = [s for s in COINS if "H" in s]
assert len(at_least_one_head) == 3, "only TT has no head"
c.check(15, float(p(len(at_least_one_head), len(COINS))))         # 0.75
assert p(len(at_least_one_head), len(COINS)) == 1 - p(1, 4), "complement rule"

# --- a standard deck ------------------------------------------------------------
hearts = [card for card in DECK if card[1] == "hearts"]
assert len(hearts) == 13
check_fraction(16, 1, 4, p(len(hearts), len(DECK)))

kings = [card for card in DECK if card[0] == "K"]
assert len(kings) == 4
check_fraction(17, 1, 13, p(len(kings), len(DECK)))

face = [card for card in DECK if card[0] in ("J", "Q", "K")]
assert len(face) == 12, f"there are {len(face)} face cards"
not_face = [card for card in DECK if card not in face]
assert len(not_face) == 40
check_fraction(18, 10, 13, p(len(not_face), len(DECK)))

# --- the spinner ----------------------------------------------------------------
above5 = [s for s in SPINNER if s > 5]
assert above5 == [6, 7, 8]
check_fraction(19, 3, 8, p(len(above5), len(SPINNER)))

multiples_of_3 = [s for s in SPINNER if s % 3 == 0]
assert multiples_of_3 == [3, 6]
not_multiple = [s for s in SPINNER if s % 3 != 0]
assert len(not_multiple) == 6
check_fraction(20, 3, 4, p(len(not_multiple), len(SPINNER)))

# --- probability models ---------------------------------------------------------
c.check(22, 1 - 0.30)                                 # 0.70, no rain
c.check(23, 1 - (0.20 + 0.35 + 0.15))                 # 0.30, the missing probability

invalid_model = [0.4, 0.3, 0.2, 0.2]
assert abs(sum(invalid_model) - 1.1) < 1e-12, "q24: the four probabilities sum to 1.1"
assert all(0 <= v <= 1 for v in invalid_model), (
    "q24: each value is individually legal, which is why the distractor is tempting")

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 2.4.A.1: the sample space is the set of all possible nonoverlapping outcomes.")
c.conceptual(2, "EK 2.4.A.1: some outcome must occur, so the sample space has probability 1.")
c.conceptual(3, "EK 2.4.A.3: a probability is a number between 0 and 1 inclusive.")
c.conceptual(4, "EK 2.4.A.2: with equally likely outcomes, P(E) is the count in E over the count in the sample space.")
c.conceptual(21, "EK 2.4.A.3: probability 0 is the probability of an impossible event.")
c.conceptual(24, "EK 2.4.A.1: computed above -- each value is individually legal but they total 1.1, and a sample space's probabilities must total exactly 1.")
c.conceptual(25, "EK 2.4.A.4: 'at least one' spans many cases while its complement 'none' is a single case, so 1 - P(none) is far less work.")

c.finish()
