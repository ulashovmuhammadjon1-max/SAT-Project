# Brief: authoring AP Calculus AB/BC question banks

Every agent working on Calculus follows this document. Read it in full before
writing anything, and read `m1_1.py` for the module format.

## Why Calculus is scoped differently from the economics banks

The economics courses have 36 and 42 CED topics and carry 50 questions each.
Calculus has **111** — the CED subdivides far more finely (8.9 and 8.11 are
separate topics for the disc and washer methods). Fifty questions on "10.3 The
nth Term Test for Divergence" would be forty questions of padding, so the target
here is **25 per topic**, which every topic can carry honestly.

## Module format

File `c<unit>_<topic>.py` in `content-pool/ap-banks/` — topic 6.9 is `c6_9.py`.

```python
# CALC 6.9 Integrating Using Substitution — 25 questions
# Answers verified with sympy; see verify_calc.py
TOPIC = ("6.9", "Integrating Using Substitution", 6)
QUESTIONS = [
 dict(q="<stem>", choices=["...","...","...","..."], ans=2, why="<one sentence>"),
]
```

**Exactly 25 questions. Exactly FOUR choices** (A–D) — that is the real AP
Calculus multiple-choice format, not the five used in economics. All four
distinct, `ans` a 0-based index, `why` one sentence.

## Notation: plain text, no LaTeX

These render as plain text, with no KaTeX. Write mathematics the way a
calculator or a textbook's plain-text answer key would:

- `f'(x)`, `f''(x)`, `dy/dx`, `d^2y/dx^2`
- `x^2`, `x^(3/2)`, `e^(2x)`, `ln(x)`, `sqrt(x)`, `|x|`
- `int f(x) dx`, `int from 0 to 3 of (2x + 1) dx`
- `lim as x -> 2 of (x^2 - 4)/(x - 2)`, `lim as x -> infinity`
- `pi`, `theta`, `sum from n=1 to infinity of 1/n^2`

Be consistent within a module. Never write a bare `^` inside prose that is not
an exponent, and never use `$...$`.

## Every answer must be verified with sympy — this is the hard rule

Economics answers are verified by a derivation in a comment. Calculus answers
are verified by **computation**. Before committing a module, write and run a
check that confirms each key symbolically:

```python
import sympy as sp
x = sp.Symbol('x')
assert sp.simplify(sp.diff(x**3*sp.sin(x), x) - (3*x**2*sp.sin(x) + x**3*sp.cos(x))) == 0
assert sp.limit((sp.sin(x))/x, x, 0) == 1
assert sp.integrate(2*x*sp.exp(x**2), x) == sp.exp(x**2)
```

Keep the checks in a file named `verify_c<unit>_<topic>.py` next to the module
and commit it. A question whose answer sympy will not confirm does not ship:
fix it or replace it. For a question that is conceptual rather than
computational (a statement of the Mean Value Theorem's hypotheses, say), no
sympy check is possible — state that in the module header and be certain the
reasoning is right.

**Also verify the distractors.** A distractor that is accidentally *equal* to
the key makes the question unanswerable. Check that the four choices are
pairwise non-equivalent, not merely different strings: `2*sqrt(x)` and
`2*x**sp.Rational(1,2)` are the same number written two ways.

## What makes a good Calculus question

Distractors must be the answers a real student would reach:

- forgetting the chain rule's inner derivative
- differentiating a quotient with the numerator and denominator reversed
- dropping the `+ C`, or dropping a constant multiple after substitution
- sign errors from the derivative of `cos`
- evaluating a definite integral as `F(a) - F(b)`
- confusing `f'` changing sign (an extremum) with `f''` changing sign (an
  inflection point)

Do not use "none of the above" or "cannot be determined" as filler; use it only
where it is genuinely the answer and the reasoning supports it.

Across a topic's 25 questions aim for roughly: 5 that state or identify a
definition or theorem's conditions, 15 that compute, and 5 harder ones — a
multi-step chain, a case that needs a hypothesis checked before a theorem
applies, or a common misconception cornered directly.

**No question may depend on a figure.** There are no images in this bank. A
topic about slope fields or curve sketching must describe the situation in
words or give a table of values, not refer to "the graph shown".

## Validate, then commit — after every topic

```
cd content-pool/ap-banks
python3 export_units.py c6_9 --subject CALC_BC --out /tmp/chk.json
```

The exporter enforces four or five choices, distinctness, and a valid key; it
warns on repeated stems. Read every warning. Two near-identical stems inside one
unit is a defect — rewrite one.

Then, and this matters because the session can be cut off at any time:

```
git add content-pool/ap-banks/c6_9.py content-pool/ap-banks/verify_c6_9.py
git commit -m "AP Calc 6.9: Integrating Using Substitution, 25 questions"
git pull --rebase origin claude/new-session-3w59v3
git push -u origin claude/new-session-3w59v3
```

Several agents share this directory. `index.lock` errors and rejected pushes are
expected; wait a few seconds and retry. Never `git push --force`, never
`git checkout`/`reset` a file you did not write, never touch a sibling's module.

Stay inside your assigned unit and do not edit `export_units.py`.
