# Verification for CALC 8.1. Run: python3 verify_c8_1.py
import sympy as sp
from c8_1 import QUESTIONS as Q

x = sp.Symbol('x')


def key(i):
    return Q[i - 1]["choices"][Q[i - 1]["ans"]]


def avg(f, a, b):
    return sp.simplify(sp.integrate(f, (x, a, b)) / (b - a))


def eq(i, value):
    assert sp.simplify(sp.sympify(key(i).replace("pi", "pi").replace("e - 1", "E - 1")) - value) == 0, \
        (i, key(i), value)


assert len(Q) == 25
for i, item in enumerate(Q, 1):
    assert len(item["choices"]) == 4 and len(set(item["choices"])) == 4, i
    assert 0 <= item["ans"] < 4, i

assert key(1).startswith("(1/(b - a))")

assert avg(x**2, 0, 3) == 3 and key(2) == "3"
assert avg(2 * x, 1, 5) == 6 and key(3) == "6"
assert avg(sp.sin(x), 0, sp.pi) == 2 / sp.pi and key(4) == "2/pi"
assert avg(x**3, 0, 2) == 2 and key(5) == "2"

# q6 the endpoint average is not the average value
assert (0 + 9) / 2 == 4.5 and avg(x**2, 0, 3) == 3
assert key(6).startswith("averaging the endpoint values")

assert sp.simplify(avg(1 / x, 1, sp.E) - 1 / (sp.E - 1)) == 0 and key(7) == "1/(e - 1)"
assert sp.simplify(avg(sp.exp(x), 0, 1) - (sp.E - 1)) == 0 and key(8) == "e - 1"
assert avg(sp.Integer(7), 2, 11) == 7 and key(9) == "7"
assert 5 * 4 == 20 and key(10) == "20"
assert key(11) == "f is continuous on [a, b]"

# q12 average value 7 vs average rate of change 5
assert avg(x**2, 1, 4) == 7
assert sp.Rational((4**2 - 1**2), 3) == 5
assert key(12).startswith("the average value is 7 and the average rate of change is 5")

assert avg(sp.sqrt(x), 0, 4) == sp.Rational(4, 3) and key(13) == "4/3"
t = sp.Symbol('t')
assert sp.integrate(3 * t**2, (t, 0, 4)) / 4 == 16 and key(14) == "16"
b = sp.Symbol('b', positive=True)
assert sp.solve(sp.Eq(sp.integrate(x, (x, 0, b)) / b, 5), b) == [10] and key(15) == "10"
assert avg(sp.cos(x), 0, sp.pi / 2) == 2 / sp.pi and key(16) == "2/pi"
assert avg(sp.Abs(x), -2, 2) == 1 and key(17) == "1"
assert avg(x**3, -2, 2) == 0 and key(18) == "0"

# q19 MVT for integrals value of c
c = sp.Symbol('c', positive=True)
assert sp.solve(sp.Eq(c**2, avg(x**2, 0, 3)), c) == [sp.sqrt(3)] and key(19) == "sqrt(3)"

assert avg(4 - x**2, 0, 2) == sp.Rational(8, 3) and key(20) == "8/3"
assert key(21) == "gallons per minute"
assert avg(1 / x**2, 1, 2) == sp.Rational(1, 2) and key(22) == "1/2"
assert avg(6 * x, 0, 4) == 12 and key(23) == "12"
# q24 combining two averages
assert (7 * 4 + 3 * 4) / 8 == 5 and key(24) == "5"
assert sp.Rational(36, 4) == 9 and key(25) == "9"

print("verify_c8_1: all checks passed")
