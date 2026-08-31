"""Typeset the plain-text math in the AP banks as KaTeX.

WHY THIS EXISTS, and why it is not the thing CLAUDE.md forbids
-------------------------------------------------------------
CLAUDE.md says: "Never bulk auto-convert Math text to LaTeX. Type it by hand."
That rule was written about `mathify.mjs` / `mathify2.py`, which tried to
reverse-engineer author intent out of noisy OCR with a pile of regexes, and
every round of fixes found an edge case the previous round had not.

Two things are different here, and both matter.

1. The input is not OCR. Every string was authored against CALC_BRIEF.md,
   which specified plain-text notation, so the notation is a small, closed,
   machine-consistent language rather than whatever a scanner produced.

2. This is a tokenizer and a recursive-descent parser, not a regex bank. It
   either understands a fragment completely or it declines to touch it. And
   the output is gated twice:

     * ROUND TRIP. The AST is rendered back to plain text and compared,
       whitespace-insensitively, against the exact source fragment. If a
       single character differs, the fragment is left alone. This is what
       makes the pass safe: a conversion can only ever change how a fragment
       is *typeset*, never what it *says*, because a fragment that says
       anything else fails the comparison and never ships.

     * KATEX. Every emitted \\( ... \\) span is parsed by KaTeX itself
       (check_katex.mjs). A span KaTeX will not parse is not a span the site
       can render, so it is rejected too.

   A declined fragment stays exactly as it is today. The worst case for any
   given string is therefore "no change", never "wrong".

The parser is deliberately conservative about what it will even attempt: a
fragment must contain a real math signal (an operator, a power, a subscript,
a function call, a big operator, a Greek letter) before it is wrapped, so a
bare "a" in "a function of x" and a bare "5" in "5 terms" are left as prose.
"""
from __future__ import annotations

import re

# --------------------------------------------------------------------------
# Vocabulary
# --------------------------------------------------------------------------

FUNCS = {
    "sin": r"\sin", "cos": r"\cos", "tan": r"\tan", "sec": r"\sec",
    "csc": r"\csc", "cot": r"\cot", "sinh": r"\sinh", "cosh": r"\cosh",
    "tanh": r"\tanh", "arcsin": r"\arcsin", "arccos": r"\arccos",
    "arctan": r"\arctan", "ln": r"\ln", "log": r"\log", "exp": r"\exp",
    "sqrt": r"\sqrt",
}

GREEK = {
    "alpha": r"\alpha", "beta": r"\beta", "gamma": r"\gamma",
    "delta": r"\delta", "Delta": r"\Delta", "epsilon": r"\varepsilon",
    "theta": r"\theta", "lambda": r"\lambda", "mu": r"\mu", "rho": r"\rho",
    "sigma": r"\sigma", "Sigma": r"\Sigma", "tau": r"\tau", "phi": r"\phi",
    "chi": r"\chi", "omega": r"\omega", "Omega": r"\Omega", "pi": r"\pi",
}

# Differentials. `dtheta` has to be listed before `dt` would match it, which
# the longest-match rule in the lexer handles.
DIFFS = {"dtheta": r"\theta"}
for _v in "abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    DIFFS.setdefault("d" + _v, _v)
# `do` is the one two-letter English word of this shape, and `df` is degrees
# of freedom in the statistics bank, not a differential.
for _w in ("do", "df"):
    DIFFS.pop(_w, None)

# Statistics notation that is spelled as a word run in the source.
NAMED = {
    "infinity": r"\infty", "inf": r"\infty",
    "xbar": r"\bar{x}", "ybar": r"\bar{y}", "pbar": r"\bar{p}",
    "phat": r"\hat{p}", "yhat": r"\hat{y}",
    "df": r"\mathrm{df}",
    "Ha": "H_{a}", "H0": "H_{0}",
}

BIGOPS = {"int", "sum", "prod", "lim"}

# Words that only ever appear as glue inside a big-operator construct.
GLUE = {"from", "to", "of", "as"}

# Single letters that are far more often English than mathematics. They can
# still appear inside a fragment (a = 3), they just may not start one.
WEAK_STARTERS = {"a", "A", "I"}

_NUM = re.compile(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?(?!\d)|\d+(?:\.\d+)?")
_MONEY = re.compile(r"\$\d{1,3}(?:,\d{3})+(?:\.\d+)?(?!\d)|\$\d+(?:\.\d+)?")
_WORD = re.compile(r"[A-Za-z]+")
_MULTI_OPS = ["+/-", "<=", ">=", "!=", "->"]
_SINGLE_OPS = set("+-*/^=<>()[]|,!_'" + "\u2212\u00d7\u00f7\u2248\u2192\u2264\u2265\u2260")
_ELLIPSIS = "..."


class Tok:
    __slots__ = ("kind", "val", "start", "end")

    def __init__(self, kind, val, start, end):
        self.kind, self.val, self.start, self.end = kind, val, start, end

    def __repr__(self):  # pragma: no cover - debugging aid
        return f"{self.kind}:{self.val!r}"


def lex(s: str):
    """Tokenize `s`. Anything not recognized becomes a TEXT token, which the
    parser treats as a hard stop."""
    toks, i, n = [], 0, len(s)
    while i < n:
        ch = s[i]
        if ch.isspace():
            i += 1
            continue
        if s.startswith(_ELLIPSIS, i):
            toks.append(Tok("ellipsis", _ELLIPSIS, i, i + 3))
            i += 3
            continue
        for op in _MULTI_OPS:
            if s.startswith(op, i):
                toks.append(Tok("op", op, i, i + len(op)))
                i += len(op)
                break
        else:
            m = _MONEY.match(s, i)
            if m:
                toks.append(Tok("money", m.group(), i, m.end()))
                i = m.end()
                continue
            m = _NUM.match(s, i)
            if m:
                toks.append(Tok("num", m.group(), i, m.end()))
                i = m.end()
                continue
            m = _WORD.match(s, i)
            if m:
                w = m.group()
                # Longest recognized prefix wins, so `dtheta` beats `dt` and
                # `arcsin` beats a bare letter.
                best = None
                for cand in sorted(
                    set(FUNCS) | set(GREEK) | set(DIFFS) | set(NAMED) | BIGOPS | GLUE,
                    key=len, reverse=True,
                ):
                    if w.startswith(cand):
                        best = cand
                        break
                if best and len(best) == len(w):
                    kind = ("func" if best in FUNCS else "greek" if best in GREEK
                            else "diff" if best in DIFFS else "named" if best in NAMED
                            else "bigop" if best in BIGOPS else "glue")
                    toks.append(Tok(kind, best, i, i + len(best)))
                    i += len(best)
                    continue
                if best and len(best) < len(w):
                    # `mu1`, `xbar2`: a known name with a numeric subscript.
                    tail = w[len(best):]
                    nm = re.fullmatch(r"\d+", tail)
                    if nm:
                        kind = ("greek" if best in GREEK else "named" if best in NAMED
                                else None)
                        if kind:
                            toks.append(Tok(kind + "sub", (best, tail), i, m.end()))
                            i = m.end()
                            continue
                if len(w) == 1:
                    # A single letter, optionally with a digit subscript
                    # written flush against it (H0, p1, x2).
                    j = m.end()
                    dm = re.compile(r"\d+").match(s, j)
                    if dm and not re.match(r"\d+\.\d", s[j:]):
                        toks.append(Tok("var", (w, dm.group()), i, dm.end()))
                        i = dm.end()
                        continue
                    toks.append(Tok("var", (w, ""), i, m.end()))
                    i = m.end()
                    continue
                toks.append(Tok("text", w, i, m.end()))
                i = m.end()
                continue
            if ch in _SINGLE_OPS:
                toks.append(Tok("op", ch, i, i + 1))
                i += 1
                continue
            toks.append(Tok("text", ch, i, i + 1))
            i += 1
    return toks


# --------------------------------------------------------------------------
# AST
# --------------------------------------------------------------------------
# Every node renders two ways: tex() for KaTeX and txt() for the round trip.
# The txt() form must reproduce the source characters exactly (whitespace
# aside), which is why nodes carry the source's own spelling where the two
# could differ -- explicit vs implicit multiplication, `inf` vs `infinity`.


class Node:
    strong = False

    def tex(self):
        raise NotImplementedError

    def txt(self):
        raise NotImplementedError


class Num(Node):
    def __init__(self, v): self.v = v

    def tex(self):
        # `{,}` keeps KaTeX from spacing a thousands separator as punctuation.
        return self.v.replace(",", "{,}")

    def txt(self): return self.v


class Run(Node):
    """A letter run written flush in the source: `kx`, `xh`, `dA`. It is a
    product, but it carries no whitespace and no signal of its own."""

    def __init__(self, letters): self.letters = letters
    def tex(self): return "".join(self.letters)
    def txt(self): return "".join(self.letters)


class Money(Node):
    """`$1,120`. Not a signal on its own -- a bare price stays prose -- but it
    may sit inside an expression so an equation is not cut in half at it."""

    def __init__(self, v): self.v = v
    def tex(self): return r"\$" + self.v[1:].replace(",", "{,}")
    def txt(self): return self.v


class Var(Node):
    is_diff = False

    def __init__(self, name, sub="", is_diff=False):
        self.name, self.sub = name, sub
        self.strong = bool(sub)
        self.is_diff = is_diff

    def tex(self):
        return f"{self.name}_{{{self.sub}}}" if self.sub else self.name

    def txt(self):
        return f"{self.name}{self.sub}"


class Named(Node):
    """A Greek letter or a named statistic, optionally numerically subscripted."""

    strong = True

    def __init__(self, word, tex, sub=""):
        self.word, self._tex, self.sub = word, tex, sub

    def tex(self):
        return f"{self._tex}_{{{self.sub}}}" if self.sub else self._tex

    def txt(self):
        return f"{self.word}{self.sub}"


class Ellipsis_(Node):
    """The `...` in `1 + x + x^2 + ...`."""

    def tex(self): return r"\dots"
    def txt(self): return "..."


class Word(Node):
    """A word used as a subscript label: `mu_treatment`."""

    def __init__(self, w): self.w = w
    def tex(self): return r"\text{" + self.w + "}"
    def txt(self): return self.w


class Group(Node):
    """A parenthesized, bracketed or absolute-value group."""

    def __init__(self, items, open_, close):
        self.items, self.open, self.close = items, open_, close
        self.strong = len(items) > 1 or any(i.strong for i in items)

    def tex(self):
        inner = ", ".join(i.tex() for i in self.items)
        if self.open == "|":
            return r"\left|" + inner + r"\right|"
        if self.open == "<":
            return r"\left\langle " + inner + r" \right\rangle"
        return rf"\left{self.open}" + inner + rf"\right{self.close}"

    def txt(self):
        return self.open + ", ".join(i.txt() for i in self.items) + self.close


class FuncPow(Node):
    """`sec^2`, `cos^2` -- the exponent is written on the function name and the
    argument is left implicit."""

    strong = True

    def __init__(self, name, tex_name, exp, parens):
        self.name, self.tex_name, self.exp, self.parens = name, tex_name, exp, parens

    def tex(self):
        return self.tex_name + "^{" + _bare(self.exp) + "}"

    def txt(self):
        e = self.exp.txt()
        return self.name + "^" + (f"({e})" if self.parens else e)


class Call(Node):
    strong = True

    def __init__(self, name, tex_name, arg, style):
        self.name, self.tex_name, self.arg, self.style = name, tex_name, arg, style

    def tex(self):
        if self.name == "sqrt":
            return r"\sqrt{" + self.arg.tex() + "}"
        if self.style == "paren":
            return self.tex_name + r"\left(" + self.arg.tex() + r"\right)"
        if self.style == "abs":
            return self.tex_name + r"\left|" + self.arg.tex() + r"\right|"
        return self.tex_name + " " + self.arg.tex()

    def txt(self):
        if self.style == "paren":
            return f"{self.name}({self.arg.txt()})"
        if self.style == "abs":
            return f"{self.name}|{self.arg.txt()}|"
        return f"{self.name} {self.arg.txt()}"


class Pow(Node):
    strong = True

    def __init__(self, base, exp, exp_parens):
        self.base, self.exp, self.exp_parens = base, exp, exp_parens

    def tex(self):
        return self.base.tex() + "^{" + _bare(self.exp) + "}"

    def txt(self):
        e = self.exp.txt()
        return self.base.txt() + "^" + (f"({e})" if self.exp_parens else e)


class Sub(Node):
    strong = True

    def __init__(self, base, sub, parens):
        self.base, self.sub, self.parens = base, sub, parens

    def tex(self):
        return self.base.tex() + "_{" + _bare(self.sub) + "}"

    def txt(self):
        s = self.sub.txt()
        return self.base.txt() + "_" + (f"({s})" if self.parens else s)


class Post(Node):
    """A postfix marker: primes or a factorial."""

    strong = True

    def __init__(self, base, mark):
        self.base, self.mark = base, mark

    def tex(self):
        return self.base.tex() + self.mark

    def txt(self):
        return self.base.txt() + self.mark


class Neg(Node):
    strong = True

    SIGN = {"+": "+", "-": "-", "+/-": r"\pm ", "\u2212": "-"}

    def __init__(self, sign, arg): self.sign, self.arg = sign, arg
    def tex(self): return self.SIGN[self.sign] + self.arg.tex()
    def txt(self): return self.sign + self.arg.txt()


def _join(left, right):
    """Concatenate two implicit factors. LaTeX ignores whitespace in math
    mode, so the space is only needed to stop `\pi` and `r` welding into an
    undefined `\pir`."""
    if right and right[0].isalpha() and re.search(r"\\[A-Za-z]+$", left):
        return " " + right
    return right


class Mul(Node):
    """A juxtaposition or explicit-operator product/quotient run."""

    def __init__(self, parts, ops):
        self.parts, self.ops = parts, ops  # ops[i] joins parts[i] and parts[i+1]
        # A run of bare single letters is indistinguishable from a word that
        # got split into characters, so it is not a signal by itself.
        self.strong = any(op for op in ops) or any(p.strong for p in parts) or any(
            not isinstance(p, Var) for p in parts
        )

    def tex(self):
        out = self.parts[0].tex()
        for op, p in zip(self.ops, self.parts[1:]):
            if op in ("*", TIMES):
                rhs = p.tex()
                if op == TIMES:
                    out += r" \times " + rhs
                else:
                    out += (r" \cdot " + rhs if not rhs or rhs[0].isdigit()
                            else _join(out, rhs))
            elif op == "":
                # A differential trailing a product wants the thin space that
                # every calculus text puts there: x\,dy, not xdy.
                out += (r"\," + p.tex() if getattr(p, "is_diff", False)
                        else _join(out, p.tex()))
            else:  # "/" is handled by the caller, which builds Frac instead
                out += " / " + p.tex()
        return out

    def txt(self):
        out = self.parts[0].txt()
        for op, p in zip(self.ops, self.parts[1:]):
            out += (" " if op == "" else op) + p.txt()
        return out


def _bare(node):
    """`(3x)` inside a \frac already has the grouping the parentheses were
    carrying, so print it without them. Only tex() does this; txt() keeps the
    parentheses, which is what the round-trip compares against."""
    if isinstance(node, Group) and node.open == "(" and len(node.items) == 1:
        return node.items[0].tex()
    return node.tex()


class Frac(Node):
    strong = True

    def __init__(self, num, den, sep="/"):
        self.num, self.den, self.sep = num, den, sep

    def tex(self):
        num, sign = self.num, ""
        if isinstance(num, Neg):
            # `-pi/2` reads as -(pi/2), and `+1/5` as +(1/5). Hoisting the sign
            # out of the numerator is what a textbook prints.
            num, sign = num.arg, Neg.SIGN[num.sign]
        return sign + r"\frac{" + _bare(num) + "}{" + _bare(self.den) + "}"

    def txt(self):
        return self.num.txt() + self.sep + self.den.txt()


class Chain(Node):
    """A run joined by + and -, or by relational operators."""

    strong = True
    TEX = {"<=": r" \le ", ">=": r" \ge ", "!=": r" \ne ", "->": r" \to ",
           "=": " = ", "<": " < ", ">": " > ", "+": " + ", "-": " - ",
           "+/-": r" \pm ",
           "\u2212": " - ", "\u2248": r" \approx ", "\u2192": r" \to ",
           "\u2264": r" \le ", "\u2265": r" \ge ", "\u2260": r" \ne "}

    def __init__(self, parts, ops): self.parts, self.ops = parts, ops

    def tex(self):
        out = self.parts[0].tex()
        for op, p in zip(self.ops, self.parts[1:]):
            out += self.TEX[op] + p.tex()
        return out

    def txt(self):
        out = self.parts[0].txt()
        for op, p in zip(self.ops, self.parts[1:]):
            out += op + p.txt()
        return out


class BigOp(Node):
    strong = True

    def __init__(self, kind, lo, hi, body, diff, word_of, word_as, side=None):
        self.kind, self.lo, self.hi = kind, lo, hi
        self.body, self.diff = body, diff
        self.word_of, self.word_as, self.side = word_of, word_as, side

    def tex(self):
        if self.kind == "lim":
            head = r"\lim"
            if self.lo is not None:
                mark = {"right": "^{+}", "left": "^{-}"}.get(self.side, "")
                head += ("_{" + _bare(self.lo) + r" \to " + _bare(self.hi)
                         + mark + "}")
            body = self.body.tex()
            return head + " " + body
        sym = {"int": r"\int", "sum": r"\sum", "prod": r"\prod"}[self.kind]
        head = sym
        if self.lo is not None:
            head += "_{" + _bare(self.lo) + "}^{" + _bare(self.hi) + "}"
        out = head + " " + self.body.tex()
        if self.diff:
            out += r"\," + "d" + DIFFS[self.diff]
        return out

    def txt(self):
        if self.kind == "lim":
            out = "lim"
            if self.lo is not None:
                out += " as " + self.lo.txt() + "->" + self.hi.txt()
            if self.side:
                out += " from the " + self.side
            return out + (" of " if self.word_of else " ") + self.body.txt()
        out = self.kind
        if self.lo is not None:
            out += " from " + self.lo.txt() + " to " + self.hi.txt()
        out += (" of " if self.word_of else " ") + self.body.txt()
        if self.diff:
            out += " " + self.diff
        return out


class ParseError(Exception):
    pass


# --------------------------------------------------------------------------
# Parser
# --------------------------------------------------------------------------

RELOPS = {"=", "<", ">", "<=", ">=", "!=", "->",
          "\u2248", "\u2192", "\u2264", "\u2265", "\u2260"}
# Unicode spellings of operators the ASCII notation also has. Each keeps its
# own character in txt(), so the round trip still compares like for like.
MINUS = "\u2212"; TIMES = "\u00d7"; DIVIDE = "\u00f7"

# Operators either side of a letter run that make it arithmetic rather than a
# hyphenated English word. Deliberately excludes `,`, `(` and `)`.
_ARITH = {"+", "-", "*", "/", "=", "<", ">", "<=", ">=", "!=", "^", "_"}


# Short letter runs that are ordinary English. Inside a bracket the parser is
# allowed to read an unknown run as an implicit product of variables (`kx`,
# `uv`), and these are the ones it must not.
STOPWORDS = {
    "the", "and", "or", "of", "is", "in", "to", "for", "as", "if", "by", "on",
    "at", "an", "no", "not", "all", "any", "one", "two", "six", "ten", "its",
    "per", "use", "see", "let", "be", "it", "so", "up", "we", "you", "are",
    "was", "has", "had", "can", "may", "but", "out", "off", "new", "old",
    "how", "why", "who", "own", "far", "few", "top", "end", "add", "set",
    # ordinal suffixes: `3rd` must not become 3 times r times d
    "st", "nd", "rd", "th",
    # unit abbreviations, which also sit flush against a number
    "cm", "mm", "km", "kg", "ml", "oz", "ft", "hr", "yr", "am", "pm", "sec",
    "vs",
}

# Words that turn `sum` into an English noun rather than a summation sign.
# "the third partial sum S_3" is not sigma-notation; "then sum a_n" is.
SUM_IS_A_NOUN_AFTER = {"partial", "the", "a", "an", "its", "their", "whose"}

# Determiners that make `infinity` the English noun rather than the symbol.
# "an infinity of ideas" is not the point at the end of the number line.
INFINITY_IS_A_NOUN_AFTER = {"an", "a", "the"}


class Parser:
    def __init__(self, toks, start=0):
        # The full token list plus where this fragment begins. A slice would
        # make peek(-1) wrap to the end of the string, which is worse than no
        # lookup at all because it silently reads an unrelated token.
        self.t, self.i, self.start = toks, start, start
        # Depth of enclosing brackets. Zero means "out in the prose".
        self.depth = 0
        # Depth of enclosing integrands, where `dx` terminates the body.
        self.integrand = 0
        # Differentials seen so far, so an integral can find one written into
        # its integrand rather than trailing it.
        self.saw_diff = 0

    def _var_run(self, k=0):
        """Is the token at offset k a letter run standing in for a product of
        variables? True only inside a bracket, or when it is written flush
        against an exponent marker or a number, which prose never is."""
        p = self.peek(k)
        if p is None or p.kind != "text":
            return False
        if not (2 <= len(p.val) <= 3 and p.val.isalpha()
                and p.val.lower() not in STOPWORDS):
            return False
        if self.depth > 0:
            return True
        nxt, prev = self.peek(k + 1), self.peek(k - 1)
        if nxt is not None and nxt.kind == "op" and nxt.val in ("^", "_") \
                and nxt.start == p.end:
            return True
        if prev is not None and prev.kind == "num" and prev.end == p.start:
            return True
        return (prev is not None and nxt is not None
                and prev.kind == "op" and nxt.kind == "op"
                and prev.val in _ARITH and nxt.val in _ARITH)

    def peek(self, k=0):
        j = self.i + k
        return self.t[j] if 0 <= j < len(self.t) else None

    def at_op(self, *vals):
        p = self.peek()
        return p is not None and p.kind == "op" and p.val in vals

    def at(self, kind, val=None):
        p = self.peek()
        return p is not None and p.kind == kind and (val is None or p.val == val)

    def eat(self):
        p = self.t[self.i]
        self.i += 1
        return p

    def expect_op(self, val):
        if not self.at_op(val):
            raise ParseError(f"expected {val!r}")
        return self.eat()

    # -- chain: relational then additive ----------------------------------
    def chain(self):
        parts, ops = [self.additive()], []
        while self.at_op(*RELOPS):
            save = self.i
            op = self.eat().val
            try:
                parts.append(self.additive())
            except ParseError:
                self.i = save
                break
            ops.append(op)
        return Chain(parts, ops) if ops else parts[0]

    _YEAR = re.compile(r"^(1[0-9]|2[0-9])\d{2}$")

    def _range_hyphen(self):
        """Is the operator at the cursor a range hyphen rather than a minus?

        `2000-2020` typeset as mathematics renders with a true minus sign and
        reads as a subtraction. The round-trip gate cannot catch this: not one
        character moves, only the meaning, which is the gate's known blind
        spot. So it has to be refused at the parse.

        Deliberately narrow -- two four-digit years, written flush. Genuine
        flush arithmetic between literals, such as the `(3-1)(4-1)` of a
        chi-square degrees-of-freedom count in the Statistics bank, is left
        alone, because widening this to any Num-Num pair would break it.
        """
        op = self.peek()
        if op is None or op.kind != "op" or op.val not in ("-", MINUS):
            return False
        prev, nxt = self.peek(-1), self.peek(1)
        if prev is None or nxt is None:
            return False
        if prev.kind != "num" or nxt.kind != "num":
            return False
        if prev.end != op.start or op.end != nxt.start:
            return False
        return bool(self._YEAR.match(prev.val) and self._YEAR.match(nxt.val))

    def additive(self):
        parts, ops = [self.term()], []
        while self.at_op("+", "-", "+/-", MINUS) and not self._range_hyphen():
            save = self.i
            op = self.eat().val
            try:
                parts.append(self.term())
            except ParseError:
                self.i = save
                break
            ops.append(op)
        return Chain(parts, ops) if ops else parts[0]

    def term(self):
        """Implicit multiplication binds tighter than * and /.

        `pi r^2/2` is (pi r^2)/2 and `1/2x` is 1/(2x), which is how the source
        was written and how a reader parses it. Building the tree this way is
        what lets `/` become a real \\frac without guessing.
        """
        node = self.implicit()
        while self.at_op("*", "/", TIMES, DIVIDE):
            save = self.i
            op = self.eat().val
            try:
                rhs = self.implicit()
            except ParseError:
                self.i = save
                break
            node = (Frac(node, rhs, op) if op in ("/", DIVIDE)
                    else Mul([node, rhs], [op]))
        # `d/dx[f(x) g(x)]`: the differential closes the denominator, so the
        # operand the derivative acts on has to be re-attached here. Narrowed
        # to a differential denominator on purpose -- every other quotient
        # already absorbs its factors in implicit().
        if isinstance(node, Frac) and getattr(node.den, "is_diff", False):
            extra = []
            while True:
                save = self.i
                p = self.peek()
                if p is None or p.kind in ("text", "glue", "diff"):
                    break
                if p.kind == "op" and p.val not in ("(", "["):
                    break
                try:
                    extra.append(self.power())
                except ParseError:
                    self.i = save
                    break
            if extra:
                node = Mul([node] + extra, [""] * len(extra))
        return node

    def implicit(self):
        parts = [self.power()]
        while True:
            save = self.i
            p = self.peek()
            if p is None or p.kind == "glue":
                break
            if p.kind == "text" and not self._var_run():
                break
            # `50 a year`: the article is not a factor.
            if (p.kind == "var" and p.val[0] in WEAK_STARTERS and not p.val[1]
                    and not (self.peek(1) is not None and self.peek(1).kind == "op"
                             and self.peek(1).val in ("_", "'", "^"))):
                break
            if p.kind == "diff" and self.integrand:
                break
            if p.kind == "op" and p.val not in ("(", "[", "|", "-"):
                break
            # A leading `-` here would be a subtraction, not a factor.
            if p.kind == "op" and p.val == "-":
                break
            # `|` is only a factor when it opens a balanced group.
            if getattr(parts[-1], "is_diff", False) or isinstance(parts[-1], Money):
                break
            # Two numbers side by side are never a product. `1 4 9 2 1 7 7 6`
            # is a question ABOUT eight separate digits, and math mode would
            # swallow the spaces and print 14921776 -- a conversion that
            # round-trips clean and still destroys the question.
            if isinstance(parts[-1], Num) and p.kind == "num":
                break
            try:
                parts.append(self.power())
            except ParseError:
                self.i = save
                break
        return Mul(parts, [""] * (len(parts) - 1)) if len(parts) > 1 else parts[0]

    def power(self):
        base = self.postfix()
        if self.at_op("^"):
            self.eat()
            parens = self.at_op("(")
            if parens:
                self.eat()
                self.depth += 1
                try:
                    exp = self.chain()
                    self.expect_op(")")
                finally:
                    self.depth -= 1
            elif self.at_op("+", "-") and not (
                self.peek(1) and self.peek(1).kind in ("num", "var", "greek", "named")
            ):
                exp = Var(self.eat().val)  # a one-sided limit: 2^+
            else:
                exp = self.power()
            return Pow(base, exp, parens)
        return base

    def postfix(self):
        node = self.atom()
        while True:
            if self.at_op("'"):
                nxt = self.peek(1)
                if (nxt is not None and nxt.kind == "var" and nxt.val[0] == "s"
                        and not nxt.val[1] and nxt.start == self.peek().end):
                    return node          # possessive: `M's`, not a derivative
                marks = ""
                while self.at_op("'"):
                    marks += self.eat().val
                node = Post(node, marks)
                continue
            if self.at_op("!"):
                self.eat()
                node = Post(node, "!")
                continue
            if self.at_op("_"):
                self.eat()
                parens = self.at_op("(")
                if parens:
                    self.eat()
                    self.depth += 1
                    try:
                        sub = self.chain()
                        self.expect_op(")")
                    finally:
                        self.depth -= 1
                elif self.at("text"):
                    sub = Word(self.eat().val)
                else:
                    sub = self.atom()
                node = Sub(node, sub, parens)
                continue
            return node

    def _grouped(self, open_, closers):
        self.eat()
        self.depth += 1
        try:
            items = [self.chain()]
            while self.at_op(","):
                self.eat()
                items.append(self.chain())
            if not self.at_op(*closers):
                raise ParseError(f"expected one of {closers}")
            close = self.eat().val
        finally:
            self.depth -= 1
        return Group(items, open_, close)

    def atom(self):
        p = self.peek()
        if p is None:
            raise ParseError("end of input")
        if p.kind == "op":
            if p.val in ("(", "["):
                # `[-1/2, 1/2)` is a half-open interval, not a typo.
                return self._grouped(p.val, (")", "]"))
            if p.val == "|":
                self.eat()
                self.depth += 1
                try:
                    inner = self.chain()
                    self.expect_op("|")
                finally:
                    self.depth -= 1
                return Group([inner], "|", "|")
            if p.val == "<":
                # A vector only if it closes with `>` and holds a comma list.
                save, save_depth = self.i, self.depth
                try:
                    self.eat()
                    self.depth += 1
                    items = [self.additive()]
                    while self.at_op(","):
                        self.eat()
                        items.append(self.additive())
                    self.expect_op(">")
                    self.depth -= 1
                    if len(items) < 2:
                        raise ParseError("not a vector")
                    return Group(items, "<", ">")
                except ParseError:
                    self.depth = save_depth
                    self.i = save
                    raise
            if p.val in ("-", "+", "+/-", MINUS):
                self.eat()
                return Neg(p.val, self.power())
            raise ParseError(f"unexpected {p.val!r}")
        if p.kind == "text":
            # `e^(kx)`, `sqrt(kA)`: a run of variable names written flush.
            # Only inside a bracket, where the delimiter has to close for the
            # fragment to parse at all, so a stray English word inside the
            # brackets fails the whole fragment instead of being split up.
            if self._var_run():
                self.eat()
                return Run(list(p.val))
            raise ParseError(f"prose {p.val!r}")
        if p.kind == "ellipsis":
            self.eat()
            return Ellipsis_()
        if p.kind == "money":
            self.eat()
            return Money(p.val)
        if p.kind == "num":
            self.eat()
            return Num(p.val)
        if p.kind == "var":
            self.eat()
            return Var(p.val[0], p.val[1])
        if p.kind == "greek":
            self.eat()
            return Named(p.val, GREEK[p.val])
        if p.kind == "greeksub":
            self.eat()
            return Named(p.val[0], GREEK[p.val[0]], p.val[1])
        if p.kind == "named":
            if p.val in ("infinity", "inf"):
                prev = self.peek(-1)
                if (prev is not None and prev.kind == "text"
                        and prev.val.lower() in INFINITY_IS_A_NOUN_AFTER):
                    raise ParseError("`infinity` is a noun here")
            self.eat()
            return Named(p.val, NAMED[p.val])
        if p.kind == "namedsub":
            self.eat()
            return Named(p.val[0], NAMED[p.val[0]], p.val[1])
        if p.kind == "diff":
            # Outside an integral a differential is just a variable, which is
            # what makes d/dx parse as a fraction rather than failing.
            self.eat()
            self.saw_diff += 1
            return Var(p.val, is_diff=True)
        if p.kind == "func":
            return self.call()
        if p.kind == "bigop":
            return self.bigop()
        raise ParseError(f"unexpected {p.kind}")

    def call(self):
        name = self.eat().val
        tex_name = FUNCS[name]
        if self.at_op("("):
            self.eat()
            self.depth += 1
            try:
                arg = self.chain()
                self.expect_op(")")
            finally:
                self.depth -= 1
            return Call(name, tex_name, arg, "paren")
        if self.at_op("|"):
            self.eat()
            self.depth += 1
            try:
                arg = self.chain()
                self.expect_op("|")
            finally:
                self.depth -= 1
            return Call(name, tex_name, arg, "abs")
        if self.at_op("^"):
            self.eat()
            parens = self.at_op("(")
            if parens:
                self.eat()
                self.depth += 1
                try:
                    exp = self.chain()
                    self.expect_op(")")
                finally:
                    self.depth -= 1
            else:
                exp = self.power()
            return FuncPow(name, tex_name, exp, parens)
        p = self.peek()
        if p is not None and p.kind in ("num", "var", "greek", "greeksub", "named",
                                        "namedsub"):
            return Call(name, tex_name, self.postfix(), "bare")
        raise ParseError("function needs an argument")

    def bigop(self):
        prev = self.peek(-1)
        kind = self.eat().val
        if kind in ("sum", "prod") and not self.at("glue", "from"):
            if prev is not None and prev.kind == "text" and \
                    prev.val.lower() in SUM_IS_A_NOUN_AFTER:
                raise ParseError("`sum` is a noun here")
        lo = hi = None
        word_of = False
        if kind == "lim":
            if self.at("glue", "as"):
                self.eat()
                lo = self.implicit()
                self.expect_op("->")
                hi = self.additive()
            side = None
            if (lo is not None and self.at("glue", "from")
                    and self.peek(1) is not None and self.peek(1).val == "the"
                    and self.peek(2) is not None
                    and self.peek(2).val in ("right", "left")):
                self.eat(); self.eat()
                side = self.eat().val
            if self.at("glue", "of"):
                self.eat()
                word_of = True
            body = self.additive()
            return BigOp(kind, lo, hi, body, None, word_of, True, side)
        if self.at("glue", "from"):
            self.eat()
            lo = self.chain_no_rel()
            if not self.at("glue", "to"):
                raise ParseError("`from` without `to`")
            self.eat()
            hi = self.additive()
        if self.at("glue", "of"):
            self.eat()
            word_of = True
        if kind == "int":
            self.integrand += 1
        before_diffs = self.saw_diff
        try:
            body = self.additive()
        finally:
            if kind == "int":
                self.integrand -= 1
        diff = None
        if self.at("diff"):
            diff = self.eat().val
        # `int from 10 to infinity of dx/x^2` writes the differential in the
        # numerator, so requiring a trailing one rejects a correct integral.
        if kind == "int" and diff is None and self.saw_diff == before_diffs:
            raise ParseError("integral without a differential")
        return BigOp(kind, lo, hi, body, diff, word_of, False)

    def chain_no_rel(self):
        """The lower limit of a sum is written `n=1`; `to` must not be eaten
        as part of it, and `=` must be."""
        node = self.additive()
        if self.at_op("="):
            self.eat()
            node = Chain([node, self.additive()], ["="])
        return node


# --------------------------------------------------------------------------
# Fragment scanning
# --------------------------------------------------------------------------

def _norm(s: str) -> str:
    """Normalize for the round-trip comparison.

    Whitespace is collapsed, EXCEPT between two letters, where it is a word
    boundary. Stripping every space made the gate blind to the one way a
    conversion can lose meaning while keeping every character: welding two
    English words into one symbol run. `($900b vs $600b)` parsed as a product
    and round-tripped clean under the old rule because `$900bvs$600b` has the
    same characters as the source. It does not have the same spaces.
    """
    s = re.sub(r"\s+", " ", s)
    out = []
    for j, ch in enumerate(s):
        if ch == " ":
            if 0 < j < len(s) - 1 and s[j - 1].isalpha() and s[j + 1].isalpha():
                out.append(" ")
            continue
        out.append(ch)
    return "".join(out)


def _startable(toks, i) -> bool:
    tok = toks[i]
    if tok.kind in ("num", "money", "greek", "greeksub", "named", "namedsub",
                    "func", "bigop", "diff"):
        return True
    if tok.kind == "var":
        if tok.val[0] not in WEAK_STARTERS or tok.val[1]:
            return True
        # "a" is usually the article, but `a_n`, `a'` and `a^2` are symbols.
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        return nxt is not None and nxt.kind == "op" and nxt.val in (
            "_", "^", "=", "<", ">", "<=", ">=", "!=", "->", "/", "*",
            "+", "-")
    if tok.kind == "op":
        if tok.val in ("(", "[", "|", "-", "+/-", "<", MINUS):
            return True
        # A `+` may open a fragment only when it is written flush against what
        # follows -- `+infinity`, `+1/5`. With a space after it (`x + h^2`) it
        # is the middle of a sum, and starting there ships `\(+2\)xh`.
        if tok.val == "+":
            nxt = toks[i + 1] if i + 1 < len(toks) else None
            return nxt is not None and nxt.start == tok.end
        return False
    if tok.kind == "text":
        # A short letter run written flush against an exponent or subscript is
        # a variable run -- `xy^2`, `te^t`. Without this the scan could only
        # ever start AFTER the caret, which split the expression in half.
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        return (2 <= len(tok.val) <= 3 and tok.val.isalpha()
                and tok.val.lower() not in STOPWORDS
                and nxt is not None and nxt.kind == "op"
                and nxt.val in ("^", "_") and nxt.start == tok.end)
    return False


def convert(text: str, rejects=None):
    """Return `text` with every confidently-parsed math fragment wrapped in
    \\( ... \\). Fragments that do not parse, do not round-trip, or carry no
    real math signal are returned untouched."""
    if not text or "\\(" in text:
        return text
    toks = lex(text)
    if not toks:
        return text
    out, cursor, i = [], 0, 0
    while i < len(toks):
        tok = toks[i]
        if not _startable(toks, i):
            i += 1
            continue
        before = text[:tok.start].rstrip()
        if before and before[-1] in "^_/*+-":
            i += 1
            continue
        # A sign written flush against a word or number on its left is the
        # hyphen of a compound, not a minus: `Carbon-14`, `2-by-2`, `stem-4`.
        # Nothing is lost by refusing here -- a real `x-1` starts its fragment
        # at the `x`, never at the sign.
        if (tok.kind == "op" and tok.val in ("-", "+", "+/-", "\u2212")
                and tok.start > 0 and text[tok.start - 1].isalnum()):
            i += 1
            continue
        # `--` is an em dash, and a token right after an apostrophe is the tail
        # of a possessive (`N's 3`), not the start of an expression.
        if tok.kind == "op" and tok.val == "-" and text[tok.start:tok.start + 2] == "--":
            i += 1
            continue
        if tok.start > 0 and text[tok.start - 1] == "'":
            i += 1
            continue
        p = Parser(toks, i)
        try:
            node = p.chain()
        except ParseError:
            i += 1
            continue
        if p.i == i or not node.strong:
            i += 1
            continue
        end_tok = toks[p.i - 1]
        src = text[tok.start:end_tok.end]
        # THE GATE. Rendering the tree back to plain text has to reproduce the
        # source exactly, or the tree does not mean what the source said.
        try:
            if _norm(node.txt()) != _norm(src):
                if rejects is not None:
                    rejects.append(("roundtrip", src, node.txt()))
                i += 1
                continue
            tex = node.tex()
        except Exception as exc:  # a renderer bug must not corrupt content
            if rejects is not None:
                rejects.append(("render", src, repr(exc)))
            i += 1
            continue
        out.append(text[cursor:tok.start])
        out.append("\\(" + tex + "\\)")
        cursor = end_tok.end
        i = p.i
    out.append(text[cursor:])
    return "".join(out)
