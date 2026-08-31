"""Controls for mathfmt.convert.

A checker that only ever agrees with itself is worthless -- CLAUDE.md has the
scar tissue from four of them. So this file is half positive controls (math
that MUST be typeset, with the exact LaTeX asserted) and half negative
controls (prose that must come back byte-identical). The negative half is the
important half: it is what proves the converter is not quietly reaching into
English.
"""
import sys

from mathfmt import convert

POSITIVE = [
    # basic algebra
    ("If f(x) = x^2 sin(x), then f'(x) =",
     r"If \(f\left(x\right) = x^{2}\sin\left(x\right)\), then \(f'\left(x\right)\) ="),
    ("2x sin(x) + x^2 cos(x)",
     r"\(2x\sin\left(x\right) + x^{2}\cos\left(x\right)\)"),
    # fractions
    ("1/2", r"\(\frac{1}{2}\)"),
    ("(x^2 + 1)^4/4 + C",
     r"\(\frac{\left(x^{2} + 1\right)^{4}}{4} + C\)"),
    ("e^(2x)/4", r"\(\frac{e^{2x}}{4}\)"),
    ("1088*pi/15", r"\(\frac{1088\pi}{15}\)"),
    # roots
    ("sqrt(x^2 + 1)/x", r"\(\frac{\sqrt{x^{2} + 1}}{x}\)"),
    ("6.5/sqrt(20)", r"\(\frac{6.5}{\sqrt{20}}\)"),
    # big operators
    ("What is int e^(3x + 1) dx?",
     r"What is \(\int e^{3x + 1}\,dx\)?"),
    ("int from 0 to 4 of f'(x) dx = 7",
     r"\(\int_{0}^{4} f'\left(x\right)\,dx = 7\)"),
    ("sum from n=1 to infinity of x^n/n",
     r"\(\sum_{n = 1}^{\infty} \frac{x^{n}}{n}\)"),
    ("Evaluate lim as x -> 0 of tan(x)/(3x).",
     r"Evaluate \(\lim_{x \to 0} \frac{\tan\left(x\right)}{3x}\)."),
    ("lim as x -> 2^+ of (x + 1)/(x - 2)",
     r"\(\lim_{x \to 2^{+}} \frac{x + 1}{x - 2}\)"),
    # subscripts, factorials, absolute value, inequalities
    ("the bound |S - S_n| <= b_(n+1) available",
     r"the bound \(\left|S - S_{n}\right| \le b_{n + 1}\) available"),
    ("sum from n=0 to infinity of (-1)^n*x^(2n+1)/(2n+1)!",
     r"\(\sum_{n = 0}^{\infty} \frac{\left(-1\right)^{n}x^{2n + 1}}"
     r"{\left(2n + 1\right)!}\)"),
    # statistics
    ("z = (63 - 60)/2 = 1.50",
     r"\(z = \frac{63 - 60}{2} = 1.50\)"),
    ("H0: mu = 40 versus Ha: mu is not equal to 40",
     r"\(H_{0}\): \(\mu = 40\) versus \(H_{a}\): \(\mu\) is not equal to 40"),
    ("The standard deviation of xbar is 8/sqrt(16) = 2",
     r"The standard deviation of \(\bar{x}\) is \(\frac{8}{\sqrt{16}} = 2\)"),
    ("p^k times q^(n-k)", r"\(p^{k}\) times \(q^{n - k}\)"),
    # derivative notation
    ("For differentiable functions f and g, d/dx[f(x) g(x)] =",
     r"For differentiable functions f and g, "
     r"\(\frac{d}{dx}\left[f\left(x\right)g\left(x\right)\right]\) ="),
    # vectors
    ("r(t) = <2cos(t), 3sin(t)>",
     r"\(r\left(t\right) = \left\langle 2\cos\left(t\right), "
     r"3\sin\left(t\right) \right\rangle\)"),
    # logs against an absolute value
    ("the integral is -ln|u|", r"the integral is \(-\ln\left|u\right|\)"),
    # a bare function argument, and differentials of an arbitrary variable
    ("(200 ln 2)/3, or about 46.2 cells per hour",
     r"\(\frac{200\ln 2}{3}\), or about 46.2 cells per hour"),
    ("dA/dt = 0.5 sqrt(A)", r"\(\frac{dA}{dt} = 0.5\sqrt{A}\)"),
    ("k e^(kx)", r"\(ke^{kx}\)"),
    ("(x^2 + 2xh + h^2 + 1 - x^2 - 1)/h",
     r"\(\frac{x^{2} + 2xh + h^{2} + 1 - x^{2} - 1}{h}\)"),
    ("<t^2/2, t^3/3> + C",
     r"\(\left\langle \frac{t^{2}}{2}, \frac{t^{3}}{3} \right\rangle + C\)"),
    ("lim as x -> 0 from the right of x*ln(x) is",
     r"\(\lim_{x \to 0^{+}} x\ln\left(x\right)\) is"),
    ("[-1/2, 1/2)", r"\(\left[-\frac{1}{2}, \frac{1}{2}\right)\)"),
    ("N = 18,500 and n = 150",
     r"\(N = 18{,}500\) and \(n = 150\)"),
    ("giving A = 150 * 300 = 45,000.",
     r"giving \(A = 150 \cdot 300 = 45{,}000\)."),
    ("For x^2 + xy + y^2 = 3, dy/dx equals",
     r"For \(x^{2} + xy + y^{2} = 3\), \(\frac{dy}{dx}\) equals"),
    ("A/(x - 2) + B/(x - 2)^2",
     r"\(\frac{A}{x - 2} + \frac{B}{\left(x - 2\right)^{2}}\)"),
    ("tends to +infinity from the right and -infinity from the left",
     r"tends to \(+\infty\) from the right and \(-\infty\) from the left"),
    ("the next term is +1/5", r"the next term is \(+\frac{1}{5}\)"),
    ("To say that sum a_n diverges means that",
     r"To say that \(\sum a_{n}\) diverges means that"),
    ("f'(x) is zero at x = +/- 1", r"\(f'\left(x\right)\) is zero at \(x = \pm 1\)"),
    ("-pi/2 <= theta <= pi/2", r"\(-\frac{\pi}{2} \le \theta \le \frac{\pi}{2}\)"),
    ("(-y + x dy/dx)/y^2",
     r"\(\frac{-y + \frac{x\,dy}{dx}}{y^{2}}\)"),
    ("d/dt[(4/3)pi*r^3]",
     r"\(\frac{d}{dt}\left[\left(\frac{4}{3}\right)\pi r^{3}\right]\)"),
    ("dA/dt = sqrt(kA)", r"\(\frac{dA}{dt} = \sqrt{kA}\)"),
    ("parabolas of the form y = Cx^2", r"parabolas of the form \(y = Cx^{2}\)"),
    ("The derivative of tan is sec^2 and the derivative of sec is sec tan.",
     r"The derivative of tan is \(\sec^{2}\) and the derivative of sec is sec tan."),
    ("sqrt(cos^2 + sin^2) = 1",
     r"\(\sqrt{\cos^{2} + \sin^{2}} = 1\)"),
    ("the terms a_n approach 0", r"the terms \(a_{n}\) approach 0"),
    ("The integrand at the upper limit is (sin x)^2",
     r"The integrand at the upper limit is \(\left(\sin x\right)^{2}\)"),
    # the economics banks use real Unicode operators
    ("22.5 \u2212 21.0 = 1.5 trillion",
     r"\(22.5 - 21.0 = 1.5\) trillion"),
    ("Real GDP \u00d7 100 \u00f7 4 = 25",
     "Real GDP \u00d7 " + r"\(\frac{100}{4} = 25\)"),
    ("nominal 120 \u00d7 100/150 = 80",
     r"nominal \(\frac{120 \times 100}{150} = 80\)"),
    ("1,000 + 50 + 120 - 50 = $1,120 billion.",
     r"\(1{,}000 + 50 + 120 - 50 = \$1{,}120\) billion."),
    ("The tax multiplier is \u2212 9 \u00d7 100 = \u2212900.",
     r"The tax multiplier is \(-9 \times 100 = -900\)."),
    ("M2 adds near-monies less liquid than M1.",
     r"\(M_{2}\) adds near-monies less liquid than \(M_{1}\)."),
]

# Prose that must come back UNCHANGED. Every one of these is a real shape from
# the banks that a careless converter would maul.
NEGATIVE = [
    "The sum of the series is 3.",
    "A continuous function h increases and then decreases.",
    "a function of one variable",
    "Which of the following is a correct interpretation?",
    "The student answered 5 questions in 20 minutes.",
    "In a random sample of 200 adults, 64 said yes.",
    "the t-distribution with 19 degrees of freedom",
    "A z-score measures distance in standard deviations.",
    "the x-axis and the y-intercept",
    "I, II, and III only",
    "The natural log of a product is the sum of the logs.",
    "The area under the curve is measured in square units.",
    "Questions 1, 10 and 20 are conceptual.",
    "It is a well-defined limit.",
    "The confidence level is 95%.",
    "A test statistic is compared to a critical value.",
    "the p-value is small",
    "Take a simple random sample of size 30.",
    "The answer is None of these.",
    "an increase of 12 percent over the year",
    # the shapes the three newest rules could have broken
    "Do not use the quotient rule here.",
    "The limit is 1 because sin is bounded by 1.",
    "The natural log of a product is a sum.",
    "a continuous function on a closed interval",
    "I do think a graph would help.",
    "The 3rd and 4th terms are equal.",
    "The interval is 20 cm long.",
    "The third partial sum is larger.",
    "Only choices I, II, and III remain.",
    "Add 1, 10 and 20 to the total.",
    "Sort the values by hand, or use a calculator.",
    "Ratios of 2 to 3 are common in the data.",
    "Transfer payments make the after-tax, after-transfer distribution flatter.",
    "The pre-test and post-test scores differ.",
    "Carbon-14 has a half-life of about 5730 years.",
    "For that same 2-by-2 table, the degrees of freedom are",
    "The stem-4 row holds five values.",
    # Flush year ranges. Found in the COMP_GOV export, where 46 of them were
    # set with a real minus sign and read as subtraction. The round trip is
    # blind to this -- no character moves -- so it is refused at the parse.
    "Change in seat share, 2000-2020, by party",
    "Turnout 1990-2020 fell in every country listed.",
    "Between 2015-2020 the legislature met twice a year.",
    "A 3-by-3 table of 300 responses is shown.",
    # a bracket holding prose, which the variable-run rule must not split
    "The result (in units of dollars) is reported below.",
    # economics and psychology shapes: possessives, money, infinity as a noun
    "Given M's cost of 2 hats per shirt and N's cost of 3 hats per shirt",
    "Country A's GDP per capita is what multiple of Country B's?",
    "EK 3.5.A.1's generativity is what allows novel sentences.",
    "Suppose you own a bond paying $50 a year and rates jump.",
    "At $5 a vendor sells 40 drinks a day; at $4 he sells 50.",
    "Remembering the digit string 1 4 9 2 1 7 7 6 as two familiar dates",
    "The sequence 2 4 6 8 is read aloud one digit at a time.",
    "B's GDP is larger in total ($900b vs $600b).",
    "a finite set of symbols and rules can produce an infinity of ideas",
    "Objective 3.1.B's two designs differ in what is followed.",
    "EK 5.2.B.3 says growth MAY result -- a possibility, not a rule.",
    "M gives up 2 hats per shirt against N's 3, while N gives up more.",
    "A country's currency is described as a 'safe haven.'",
    "Suppose you own a bond paying $50 a year and rates jump.",
    "At $5 a vendor sells 40 drinks a day; at $4 he sells 50.",
    "Remembering the digit string 1 4 9 2 1 7 7 6 as two familiar dates",
    "The sequence 2 4 6 8 is read aloud one digit at a time.",
    "Use the rule (see the note) carefully.",
    "The estimate (not the parameter) varies.",
    "Choose the interval (one of the four) that works.",
]


def gate_control():
    """Prove the round-trip gate can actually FIRE.

    A gate that has never rejected anything is indistinguishable from a gate
    that is wired to nothing -- which is the exact failure CLAUDE.md records
    twice. So corrupt the plain-text renderer on purpose and check that the
    conversion is refused rather than shipped.
    """
    import mathfmt

    original = mathfmt.Frac.txt
    mathfmt.Frac.txt = lambda self: self.num.txt() + "/" + self.den.txt() + "9"
    try:
        rejects = []
        got = mathfmt.convert("1/2", rejects=rejects)
        ok = got == "1/2" and any(r[0] == "roundtrip" for r in rejects)
    finally:
        mathfmt.Frac.txt = original
    if not ok:
        print("GATE CONTROL FAILED: a corrupted renderer was not rejected")
    # And the negative control on the gate: with the renderer intact, the same
    # input must convert.
    if mathfmt.convert("1/2") != r"\(\frac{1}{2}\)":
        print("GATE CONTROL FAILED: the gate rejects a correct conversion")
        ok = False
    return 0 if ok else 1


def main():
    bad = 0
    for src, want in POSITIVE:
        got = convert(src)
        if got != want:
            bad += 1
            print("POSITIVE FAILED")
            print("   in   :", src)
            print("   want :", want)
            print("   got  :", got)
    for src in NEGATIVE:
        got = convert(src)
        if got != src:
            bad += 1
            print("NEGATIVE FAILED (prose was touched)")
            print("   in   :", src)
            print("   got  :", got)
    bad += gate_control()
    print(f"{len(POSITIVE)} positive, {len(NEGATIVE)} negative controls, "
          f"plus the gate control; {bad} failing")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
