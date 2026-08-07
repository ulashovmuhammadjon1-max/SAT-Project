import re


PI_RE = re.compile(r"(?<![A-Za-z])pi(?![A-Za-z])")


def convert_sqrt(s):
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r"sqrt\(([^()]+)\)", lambda m: r"\sqrt{" + m.group(1) + "}", s)
    return s


def brace_exponents(s):
    return re.sub(r"\^(-?[A-Za-z0-9]{2,})", lambda m: "^{" + m.group(1) + "}", s)


def convert_fractions(s):
    # numerator may be a simple token OR end with a \sqrt{...} / \frac{...}{...} unit (e.g. "4\sqrt{17}")
    NUM = r"(?:\d+)?\\(?:sqrt|frac)\{[^{}]*\}(?:\{[^{}]*\})?|\d+|[a-zA-Z]"
    s = re.sub(rf"(?<![\\{{\w])({NUM})\s*/\s*(\d+|[a-zA-Z][a-zA-Z0-9]?)(?![\w}}])",
                r"\\frac{\1}{\2}", s)
    return s


def basic_math_convert(run):
    run = convert_sqrt(run)
    run = convert_fractions(run)
    run = brace_exponents(run)
    run = run.replace("*", r" \cdot ")
    run = re.sub(r"<=", r"\\le", run)
    run = re.sub(r">=", r"\\ge", run)
    run = re.sub(r"!=", r"\\ne", run)
    run = PI_RE.sub(r"\\pi", run)
    return run


# a clause "looks like an equation" if it contains an = sign (or <=/>=) plus at least one letter/digit token.
# Leading token may start with a letter, digit, or "(" (e.g. "(x - 4)^2 + ..."). Commas that are
# thousands-separators (digit,digit) do NOT terminate the clause; any other comma does.
NOT_CLAUSE_END = r"(?:[^.,;!?]|(?<=\d),(?=\d{3}\b))"
EQ_CLAUSE_RE = re.compile(
    r"(?<![\\(])\b((?:[A-Za-z][A-Za-z0-9_]*\([A-Za-z0-9_,\s\-]*\)|[A-Za-z0-9_.(]+)"
    r"(?:\s*[+\-*/^]\s*[A-Za-z0-9_.()]+)*"
    r"\s*(?:=|<=|>=|<|>)\s*"
    rf"{NOT_CLAUSE_END}+?"
    r")"
    r"(?=[.,;!?]|\s+(?:where|If|what|What|which|Which|and|is|has|In the|The)\b|$)"
)


def wrap_equations_in_stem(text):
    """Find equation-like clauses in prose and wrap each in \\( \\)."""
    out = []
    last = 0
    for m in EQ_CLAUSE_RE.finditer(text):
        start, end = m.span(1)
        if start < last:
            continue
        clause = m.group(1).rstrip()
        if "=" not in clause and "<" not in clause and ">" not in clause:
            continue
        # skip if clause has no real math signal (digit, function-call parens, exponent, or single-letter var before =)
        if not (re.search(r"\d", clause) or re.search(r"[A-Za-z]\(", clause)
                or "^" in clause or re.search(r"\b[a-zA-Z]\s*=", clause)):
            continue
        out.append(text[last:start])
        converted = basic_math_convert(clause)
        out.append(r"\(" + converted.strip() + r"\)")
        last = end
    out.append(text[last:])
    result = "".join(out)
    result = wrap_bare_function_calls(result)
    result = wrap_bare_pi_terms(result)
    result = wrap_bare_sqrt_terms(result)
    result = wrap_value_of_phrases(result)
    return result


VALUE_OF_RE = re.compile(
    r"\bvalue of ([A-Za-z0-9][A-Za-z0-9_^{}.\-\s\+\*/]*?[A-Za-z0-9}])(?=[?.,]|\s+(?:in|for|is|and)\b|$)"
)


def wrap_value_of_phrases(text):
    parts = re.split(r"(\\\(.*?\\\))", text)
    for i, p in enumerate(parts):
        if p.startswith(r"\("):
            continue

        def repl(m):
            expr = m.group(1)
            if not (re.search(r"\d", expr) or re.search(r"[A-Za-z]\(", expr) or "^" in expr):
                return m.group(0)  # leave plain-English "value of x" alone if no real expression signal... but x alone is fine too
            converted = basic_math_convert(expr)
            return "value of " + r"\(" + converted.strip() + r"\)"
        parts[i] = VALUE_OF_RE.sub(repl, p)
    return "".join(parts)


FUNC_CALL_RE = re.compile(r"(?<!\\\()\b([a-zA-Z]\((?:-?\d+(?:\.\d+)?|[a-zA-Z])\))(?!\\\))")


def wrap_bare_function_calls(text):
    """Wrap standalone function-evaluation references like h(-3), f(2) that weren't caught as part of an equation."""
    parts = re.split(r"(\\\(.*?\\\))", text)  # skip already-wrapped spans
    for i, p in enumerate(parts):
        if p.startswith(r"\("):
            continue
        parts[i] = FUNC_CALL_RE.sub(lambda m: r"\(" + m.group(1) + r"\)", p)
    return "".join(parts)


BARE_PI_RE = re.compile(r"(?<![\\\w])(\d+)\s*\*\s*pi\b(?![A-Za-z])")


def wrap_bare_pi_terms(text):
    parts = re.split(r"(\\\(.*?\\\))", text)
    for i, p in enumerate(parts):
        if p.startswith(r"\("):
            continue
        parts[i] = BARE_PI_RE.sub(lambda m: r"\(" + m.group(1) + r"\pi\)", p)
    return "".join(parts)


BARE_SQRT_EXPR_RE = re.compile(r"(?<![\\\w])(\d*\s*[+\-]?\s*\d*\s*\*?\s*sqrt\([^()]+\))")


def wrap_bare_sqrt_terms(text):
    parts = re.split(r"(\\\(.*?\\\))", text)
    for i, p in enumerate(parts):
        if p.startswith(r"\("):
            continue

        def repl(m):
            return r"\(" + basic_math_convert(m.group(1)).strip() + r"\)"
        parts[i] = BARE_SQRT_EXPR_RE.sub(repl, p)
    return "".join(parts)


def _is_structurally_suspicious(original, converted):
    if converted.count(r"\(") != converted.count(r"\)"):
        return True
    # a thousands-separated number must never get split across a wrap boundary
    for m in re.finditer(r"\d{1,3}(?:,\d{3})+", original):
        num = m.group(0)
        if num in original and num not in converted and num.replace(",", "") not in converted:
            # check the digits still appear contiguously (allowing the whole number inside one \(\) span)
            if not re.search(re.escape(num), converted):
                return True
    # a stray "^\(" or ")\^" indicates a mid-token break from a bad clause boundary
    if re.search(r"\^\\\(|\)\\\^", converted):
        return True
    # a decimal number split across a wrap boundary: "...4\).9..." or "...4.\(9..."
    if re.search(r"\d\\\)\.\d", converted) or re.search(r"\d\.\\\(\d", converted):
        return True
    # any digit immediately touching a wrap delimiter with no separating space/punct (mid-number split)
    if re.search(r"\d\\\(", converted) or re.search(r"\\\)\d", converted):
        return True
    return False


def mathify_stem(text):
    converted = wrap_equations_in_stem(text)
    if _is_structurally_suspicious(text, converted):
        return text  # fail safe: ship plain, unwrapped text rather than broken LaTeX
    return converted


def looks_like_pure_math(converted, original):
    if re.match(r"^[A-Za-z][A-Za-z ,'\-]*\.?$", original.strip()):
        return False  # plain english like "Zero", "Exactly one", "Increasing linear"
    return bool(re.search(r"[0-9]|\\pi|\\sqrt|\\frac|[+\-*/=<>^]", converted))


def wrap_choice(content):
    converted = basic_math_convert(content)
    if looks_like_pure_math(converted, content):
        wrapped = r"\(" + converted.strip() + r"\)"
        if _is_structurally_suspicious(content, wrapped):
            return content
        return wrapped
    return converted


if __name__ == "__main__":
    tests = [
        "13x = 42 - x. What value of x is the solution to the given equation?",
        "f(x) = 5x + b. For the linear function f, b is a constant and f(7) = 35. What is the value of b?",
        "The function h is defined by h(x) = 5|x|. What is the value of h(-3)?",
        "If 5x = 4, what is the value of 40x?",
        "y = -(1/7)x; y = (1/11)x. The solution to the given system of equations is (x, y). What is the value of x?",
        "A circle has diameters AC and BD. The circumference of the circle is 84*pi, and the length of arc AB is 14*pi.",
        "f(x) = a^x + b, where a and b are positive constants.",
    ]
    for t in tests:
        print(mathify_stem(t))
        print()
    print("CHOICES:")
    for c in ["4", "22\\sqrt{3}", "Zero", "Increasing linear", "x^{16}", "-7", "13/2"]:
        print(repr(c), "->", wrap_choice(c))
