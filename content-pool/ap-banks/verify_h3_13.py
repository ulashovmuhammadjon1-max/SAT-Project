"""Key audit for AP CHEMISTRY 3.13 Beer-Lambert Law.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  3.13.A.1  EQN A = epsilon b c; the molar absorptivity describes how intensely
            a species absorbs light of a SPECIFIC WAVELENGTH; the path length
            and the concentration are proportional to the number of
            light-absorbing particles in the light path
                     1, 2, 3, 4, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 26,
                     28, 29, 30
  3.13.A.2  the path length and wavelength are usually held constant, and IN
            SUCH CASES the absorbance is proportional only to the concentration;
            the instrument is set to the wavelength of maximum absorbance
            (optimum wavelength) to ensure the maximum sensitivity of
            measurement
                     5, 6, 7, 8, 9, 12, 14, 16, 22, 23, 24, 25, 27, 29, 30

THE CONDITION IS PART OF THE CLAIM, AND IT IS CHECKED. EK 3.13.A.2 does not say
the absorbance is proportional to the concentration. It says the path length and
the wavelength are usually held constant and that IN SUCH CASES the
proportionality holds. An item that asserts the proportionality without stating
that condition is asserting something the framework does not, and it is the
condition that makes items 29 and 30 -- the two experimental-error items
suggested skill 2.E asks for -- come out the way they do.
``proportionality_states_its_condition`` therefore requires every item in
``CONDITIONED`` to state the condition in its stem or its key, and
``_condition_matcher_self_check`` runs a positive AND a negative control on the
matcher itself every time this file is imported.

THE ARITHMETIC IS A PRODUCT OF THREE, WHICH IS WHY THE DISTRACTORS ARE ROUTES.
Nothing here has a sign to get backwards -- absorbance, path length,
concentration and molar absorptivity are all positive quantities, and
``absorbance`` and its three rearrangements assert that. What this topic has
instead is a DIRECTION of change, and it is just as easy to invert: a dilution
read as a concentration, a shorter cuvette read as a longer one. ``change`` and
``agrees`` handle that the way h6_thermo handles the enthalpy sign -- a record
with NAMED fields and two named booleans compared, never two lists indexed in
parallel -- and ``_change_matcher_self_check`` negative-controls it on import.

Every distractor carrying a number is a mistaken route recomputed here from the
stimulus: the path length left out, divided by instead of multiplied by, counted
twice, or a power of ten dropped from the concentration. ``wrong_route`` requires
each to sit in exactly one distractor and never in the key, so an item cannot
quietly stop testing the error it exists to test.

The stem values are read out of the stem by the words AROUND them ("molar
absorptivity of", "cm cuvette", "concentration of", "absorbance of"), never by
position; the tabulated values are read from the table with the power of ten
taken from the COLUMN HEADER.

SCOPE. 3.11 owns the spectral regions and 3.12 owns the photon equations.
``no_other_topic`` bans both from every stem and every keyed choice.

NEGATIVE CONTROL: ``python3 verify_h3_13.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h3_13

# ------------------------------------------------------------------- patterns

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below|the curve above|the curve below|"
    r"the calibration curve)(?![a-z])", re.I)

# 3.11 owns the region/transition associations; 3.12 owns the photon equations.
_OTHER_TOPIC = re.compile(
    r"(?<![A-Za-z])(Planck|photon|frequency|microwave|infrared|ultraviolet|"
    r"rotational|vibrational)(?![A-Za-z])", re.I)

_SCI = re.compile(r"(-?\d+(?:\.\d+)?)\s*\\times\s*10\^\{(-?\d+)\}")
_LEAD = re.compile(r"^(\d+(?:\.\d+)?)(?![\d.])")
_HEADER_SCALE = re.compile(r"10\^\{(-?\d+)\}")

_STEM_EPS = re.compile(r"molar absorptivity (?:of|is) (\d+(?:\.\d+)?)")
_STEM_PATH = re.compile(r"(\d+(?:\.\d+)?)\s*cm cuvette")
_STEM_CONC = re.compile(
    r"concentration (?:of\s+)?\\\(\s*(\d+(?:\.\d+)?)\s*\\times\s*10\^\{(-?\d+)\}\s*\\\)\s*M")
_STEM_ABS = re.compile(r"absorbance of (\d+(?:\.\d+)?)")

# The change a stem states in words, where it states one rather than giving two
# numbers. Read from the STEM only; the key states the same change in its own
# words and is what the check is testing.
_FACTOR_WORDS = [
    (re.compile(r"(?<![A-Za-z0-9])doubled(?![A-Za-z0-9])", re.I), 2.0),
    (re.compile(r"(?<![A-Za-z0-9])three times(?![A-Za-z0-9])", re.I), 3.0),
    (re.compile(r"(?<![A-Za-z0-9])one fifth(?![A-Za-z0-9])", re.I), 0.2),
    (re.compile(r"(?<![A-Za-z0-9])half the path length(?![A-Za-z0-9])", re.I), 0.5),
]

# EK 3.13.A.2's condition, in the several ways this module's stems state it.
_CONDITION = re.compile(
    r"(?<![A-Za-z0-9])(held constant|are unchanged|is unchanged|the same cuvette|"
    r"same wavelength|under the conditions|same 1\.00 cm cuvette)(?![A-Za-z0-9])", re.I)

# Items whose key asserts that the absorbance follows the concentration. Listed
# explicitly so the guard cannot quietly stop covering one that was edited.
CONDITIONED = (6, 12, 14, 16, 22, 23, 24, 25)


# ------------------------------------------------ EK 3.13.A.1's one equation

def absorbance(eps, path, conc):
    """EK 3.13.A.1's EQN: A = epsilon b c, written once and called everywhere.

    All four quantities in this topic are positive -- there is no sign to get
    backwards here, and a negative one would mean a rearrangement had been
    inverted somewhere upstream, so it is refused rather than propagated.
    """
    assert eps > 0 and path > 0 and conc > 0, (
        f"the molar absorptivity, path length and concentration are positive quantities: "
        f"{eps}, {path}, {conc}"
    )
    return eps * path * conc


def molar_absorptivity(a, path, conc):
    """The same equation rearranged for epsilon."""
    assert a > 0 and path > 0 and conc > 0, (a, path, conc)
    return a / (path * conc)


def concentration(a, eps, path):
    """The same equation rearranged for c."""
    assert a > 0 and eps > 0 and path > 0, (a, eps, path)
    return a / (eps * path)


def path_length(a, eps, conc):
    """The same equation rearranged for b."""
    assert a > 0 and eps > 0 and conc > 0, (a, eps, conc)
    return a / (eps * conc)


# ------------------------------------------------------ direction bookkeeping

RISES = "rises"
FALLS = "falls"

# A digit and a letter are both word characters, so the lookarounds exclude
# BOTH. This project has paid five separate times for a boundary that looked
# right beside a digit and silently was not; the selftest below asserts
# "2doubles4" is refused, which is what makes that concrete.
_UP = re.compile(
    r"(?<![A-Za-z0-9])(doubles|triples|twice|five times|nine times|larger)(?![A-Za-z0-9])",
    re.I)
_DOWN = re.compile(
    r"(?<![A-Za-z0-9])(halved|half|one third|one fifth|one quarter|one tenth)"
    r"(?![A-Za-z0-9])", re.I)


def change(factor):
    """Which way the absorbance moved, as a record with NAMED fields.

    Never a pair to be read by position. The inverted check this project already
    shipped compared index 0 of one tuple against index 0 of another that was
    ordered the other way, and rejected a correct key.
    """
    return dict(rises=factor > 1.0, falls=factor < 1.0, unchanged=factor == 1.0)


def stated_change(text):
    """Which way a piece of text says the absorbance moved, or None.

    None when the text states NEITHER and also when it states BOTH: a choice
    naming both leaves the direction ambiguous, and an anchor pinned to it would
    match a key that had the change inverted.
    """
    up, down = bool(_UP.search(text)), bool(_DOWN.search(text))
    if up and not down:
        return RISES
    if down and not up:
        return FALLS
    return None


def agrees(factor, text):
    """Does ``text`` name the direction the recomputed factor requires?

    Two named booleans compared, never two lists indexed in parallel.
    """
    assert factor != 1.0, (
        "a factor of one leaves the absorbance unchanged and has no direction word, so "
        "nothing can agree or disagree with it; the caller must handle it itself"
    )
    said = stated_change(text)
    if said is None:
        return False
    factor_rises = factor > 1.0
    text_says_rises = said == RISES
    return factor_rises == text_says_rises


def _change_matcher_self_check():
    """Positive AND negative control for ``agrees``, run every time."""
    assert agrees(2.0, "It doubles") and agrees(3.0, "It triples")
    assert agrees(0.5, "It is halved") and agrees(0.2, "It falls to one fifth")
    assert not agrees(2.0, "It is halved"), (
        "NEGATIVE CONTROL FAILED: a factor above one was allowed to be called a halving"
    )
    assert not agrees(0.5, "It doubles"), (
        "NEGATIVE CONTROL FAILED: a factor below one was allowed to be called a doubling"
    )
    assert not agrees(2.0, "It is unchanged"), (
        "NEGATIVE CONTROL FAILED: a text stating no direction was allowed to agree"
    )
    assert stated_change("It doubles, then falls to one half") is None, (
        "a text naming BOTH directions must be refused, or an anchor pinned to it would "
        "match a key with the change inverted"
    )
    # A digit and a letter are both word characters, so \b would silently not be
    # a boundary here. The explicit lookarounds must hold.
    assert stated_change("2doubles4") is None
    assert stated_change("halfway") is None, (
        "'half' inside 'halfway' must not be read as a halving"
    )
    try:
        agrees(1.0, "It doubles")
    except AssertionError:
        pass
    else:
        raise AssertionError(
            "NEGATIVE CONTROL FAILED: an unchanged absorbance was allowed a direction word"
        )
    print("OK  3.13 direction matcher: doubling, tripling, halving and one fifth all read "
          "correctly, and the inverted, the ambiguous and the directionless are all refused.")


def _condition_matcher_self_check():
    """Positive AND negative control for the EK 3.13.A.2 condition matcher."""
    assert _CONDITION.search("the path length and the wavelength are held constant")
    assert _CONDITION.search("measured in the same cuvette at the same wavelength")
    assert _CONDITION.search("under the conditions the standards were measured under")
    assert not _CONDITION.search(
        "the absorbance is proportional to the concentration of the species"), (
        "POSITIVE CONTROL FAILED: a sentence asserting the proportionality with NO condition "
        "attached was read as stating one, which is exactly the claim this guard exists to "
        "catch"
    )
    assert not _CONDITION.search("the wavelength was changed between the measurements")
    print("OK  3.13 condition matcher: EK 3.13.A.2's condition is recognised in each form "
          "this module states it, and a bare proportionality claim is not.")


# ------------------------------------------------------------- value reading

def value_of(text):
    """The single number a choice states, or None if it states none."""
    m = _SCI.search(text)
    if m:
        return float(m.group(1)) * 10.0 ** int(m.group(2))
    m = _LEAD.match(text.strip())
    if m:
        return float(m.group(1))
    return None


def _matches(value, target, tol=0.005):
    return value is not None and abs(value - target) <= tol * abs(target)


def numeric_key(item, expected):
    """Exactly one choice states ``expected``, and it is the keyed one."""
    vals = [value_of(c) for c in item["choices"]]
    close = [k for k, v in enumerate(vals) if _matches(v, expected)]
    assert close == [item["ans"]], (
        f"the recomputed value {expected:g} matches choice(s) {close}; it must match the "
        f"keyed choice {item['ans']} and no other -- choices {item['choices']}"
    )
    return expected


def wrong_route(item, value, origin):
    """A recomputed WRONG value must sit in exactly one distractor, never the key."""
    vals = [value_of(c) for c in item["choices"]]
    assert not _matches(vals[item["ans"]], value), (
        f"the mistaken value {value:g} ({origin}) is what the KEYED choice states, so the "
        f"item has two defensible answers -- {h.keyed(item)!r}"
    )
    hits = [k for k, v in enumerate(vals) if k != item["ans"] and _matches(v, value)]
    assert len(hits) == 1, (
        f"the recomputed mistake {value:g} ({origin}) appears in {len(hits)} distractor(s); "
        f"exactly one must carry it -- choices {item['choices']}"
    )
    return value


def stem_eps(stem):
    return [float(x) for x in _STEM_EPS.findall(stem)]


def stem_path(stem):
    return [float(x) for x in _STEM_PATH.findall(stem)]


def stem_conc(stem):
    return [float(a) * 10.0 ** int(b) for a, b in _STEM_CONC.findall(stem)]


def stem_abs(stem):
    return [float(x) for x in _STEM_ABS.findall(stem)]


def stem_factor(stem):
    hits = [f for pat, f in _FACTOR_WORDS if pat.search(stem)]
    assert len(hits) == 1, (
        f"the stem states {len(hits)} changes in words, not one -- {stem[:80]!r}"
    )
    return hits[0]


FACTOR_PHRASE = {
    3.0: "It triples",
    2.0: "It doubles",
    0.5: "It is halved",
    0.2: "It falls to one fifth of its original value",
}


def factor_phrase(factor):
    hits = [p for f, p in FACTOR_PHRASE.items() if abs(factor - f) < 1e-9]
    assert len(hits) == 1, f"the recomputed factor {factor!r} names {hits}, not one phrase"
    return hits[0]


def _facing(item):
    out = [item["q"], item["why"]] + list(item["choices"])
    t = item.get("table")
    if t:
        out += [str(x) for x in t["headers"]]
        out += [str(c) for r in t["rows"] for c in r]
    return out


# --------------------------------------------------------------- module gates

def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, which this bank "
                f"cannot show -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: the standards are carried as a table of "
          "concentration against absorbance, and no item points at a calibration curve.")


def no_other_topic(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        texts = [item["q"], h.keyed(item)]
        t = item.get("table")
        if t:
            texts += [str(x) for x in t["headers"]]
            texts += [str(c) for r in t["rows"] for c in r]
        for text in texts:
            hit = _OTHER_TOPIC.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: a stem or key uses {hit.group(0)!r}, which is "
                f"3.11's or 3.12's material -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no stem or key reaches for 3.11's spectral regions "
          "or 3.12's photon equations; wavelength enters only as an instrument setting.")


def proportionality_states_its_condition(module):
    """EK 3.13.A.2's proportionality is conditional, and every item says so."""
    for i in CONDITIONED:
        item = module.QUESTIONS[i - 1]
        assert _CONDITION.search(item["q"]) or _CONDITION.search(h.keyed(item)), (
            f"{module.TOPIC[0]} q{i}: the key ties the absorbance to the concentration, but "
            "neither the stem nor the key says the path length and wavelength are held "
            "constant. EK 3.13.A.2 states the proportionality only IN SUCH CASES -- "
            f"stem {item['q'][:80]!r}, key {h.keyed(item)!r}"
        )
    print(f"OK  {module.TOPIC[0]} condition: all {len(CONDITIONED)} item(s) tying the "
          "absorbance to the concentration state EK 3.13.A.2's condition that the path "
          "length and wavelength are held constant.")


def framework_equation(module):
    """The equation item keys the framework's own form, and only it."""
    wanted = "\\( A = \\varepsilon b c \\)"
    item = module.QUESTIONS[1]
    assert h.keyed(item) == wanted, (
        f"{module.TOPIC[0]} q2: the keyed choice is {h.keyed(item)!r}, but EK 3.13.A.1 gives "
        f"{wanted!r}"
    )
    others = [k for k, c in enumerate(item["choices"]) if k != item["ans"] and c == wanted]
    assert not others, (
        f"{module.TOPIC[0]} q2: choice(s) {others} also state the framework's equation "
        "verbatim, so the item has more than one defensible answer"
    )
    print(f"OK  {module.TOPIC[0]} equation: the item asking for the Beer-Lambert law keys "
          "EK 3.13.A.1's exact form, and no distractor states it.")


# ------------------------------------------------------------- stem numerics

def n12(item):
    f = stem_factor(item["q"])
    before = absorbance(1500.0, 1.00, 1.0e-4)
    after = absorbance(1500.0, 1.00, f * 1.0e-4)
    factor = after / before
    assert agrees(factor, h.keyed(item)), (
        f"the concentration change recomputes to a factor of {factor:g} on the absorbance, "
        f"which {change(factor)}, but the keyed choice says {stated_change(h.keyed(item))!r}"
    )
    h.shows(item, factor_phrase(factor))
    return (f"the stated change in concentration takes the absorbance from {before:g} to "
            f"{after:g} through the framework's equation, a factor of {factor:g}")


def n13(item):
    paths = stem_path(item["q"])
    assert len(paths) == 2, f"the stem states the path lengths {paths}"
    before = absorbance(1500.0, paths[0], 2.0e-4)
    after = absorbance(1500.0, paths[1], 2.0e-4)
    factor = after / before
    assert agrees(factor, h.keyed(item)), (
        f"the cuvette change recomputes to a factor of {factor:g}, but the keyed choice says "
        f"{stated_change(h.keyed(item))!r}"
    )
    h.shows(item, factor_phrase(factor))
    wrong_squared = factor * factor
    assert abs(wrong_squared - 9.0) < 1e-9, wrong_squared
    return (f"the two stated path lengths {paths} take the absorbance from {before:g} to "
            f"{after:g}, a factor of {factor:g}, with the squared factor {wrong_squared:g} "
            "offered as a distractor")


def n14(item):
    f = stem_factor(item["q"])
    before = absorbance(1500.0, 1.00, 5.0e-4)
    after = absorbance(1500.0, 1.00, f * 5.0e-4)
    factor = after / before
    assert agrees(factor, h.keyed(item)), (
        f"the dilution recomputes to a factor of {factor:g}, but the keyed choice says "
        f"{stated_change(h.keyed(item))!r}"
    )
    h.shows(item, factor_phrase(factor))
    return (f"the stated dilution takes the absorbance from {before:g} to {after:g} through "
            f"the framework's equation, a factor of {factor:g}")


def n15(item):
    """Two species, equal path length and concentration, one twice the other's epsilon."""
    weaker = absorbance(1000.0, 1.00, 2.0e-4)
    stronger = absorbance(2 * 1000.0, 1.00, 2.0e-4)
    factor = stronger / weaker
    assert agrees(factor, h.keyed(item)), (
        f"twice the molar absorptivity recomputes to a factor of {factor:g}, but the keyed "
        f"choice says {stated_change(h.keyed(item))!r}"
    )
    h.shows(item, "Species M shows twice the absorbance of species N")
    return (f"with the path length and concentration held equal, twice the molar "
            f"absorptivity takes the absorbance from {weaker:g} to {stronger:g}, a factor of "
            f"{factor:g}")


def n16(item):
    """The proportionality itself, recomputed rather than asserted."""
    concs = [1.0e-4, 2.0e-4, 5.0e-4]
    ratios = [absorbance(1500.0, 1.00, c) / c for c in concs]
    assert max(ratios) - min(ratios) < 1e-9 * max(ratios), (
        f"the absorbance is not proportional to the concentration: {ratios}"
    )
    squares = [absorbance(1500.0, 1.00, c) / (c * c) for c in concs]
    assert max(squares) - min(squares) > 1e-9 * max(squares), (
        "a check that cannot separate a direct proportionality from a square one proves "
        f"nothing: {squares}"
    )
    h.shows(item, "It is directly proportional to the concentration")
    return (f"the framework's equation gives a constant absorbance-to-concentration ratio "
            f"{ratios[0]:g} across the concentrations {concs}, while the ratio to the SQUARE "
            "of the concentration is not constant")


def n17(item):
    f = stem_factor(item["q"])
    before = absorbance(1500.0, 2.00, 2.0e-4)
    after = absorbance(1500.0, f * 2.00, 2.0e-4)
    factor = after / before
    assert agrees(factor, h.keyed(item)), (
        f"halving the path length recomputes to a factor of {factor:g}, but the keyed choice "
        f"says {stated_change(h.keyed(item))!r}"
    )
    h.shows(item, factor_phrase(factor))
    return (f"the stated change in path length takes the absorbance from {before:g} to "
            f"{after:g} through the framework's equation, a factor of {factor:g}")


def n18(item):
    (eps,), (b,), (c,) = (stem_eps(item["q"]), stem_path(item["q"]), stem_conc(item["q"]))
    a = absorbance(eps, b, c)
    numeric_key(item, a)
    wrong_route(item, eps * c, "the path length left out of the product")
    wrong_route(item, eps * c / b, "divided by the path length instead of multiplied")
    wrong_route(item, eps * b * b * c, "the path length counted twice")
    wrong_route(item, eps * b * (10 * c), "a power of ten lost from the concentration")
    return (f"the stated molar absorptivity {eps:g}, path length {b:g} cm and concentration "
            f"{c:g} M multiply to an absorbance of {a:g}, with four mistaken routes each "
            "recomputed into one distractor")


def n19(item):
    (a,), (b,), (c,) = (stem_abs(item["q"]), stem_path(item["q"]), stem_conc(item["q"]))
    eps = molar_absorptivity(a, b, c)
    numeric_key(item, eps)
    wrong_route(item, a / c, "the path length left out of the divisor")
    wrong_route(item, a / (b * b * c), "the path length counted twice")
    wrong_route(item, a / (b * 10 * c), "a power of ten lost from the concentration")
    wrong_route(item, a / (b * c / 10), "a power of ten gained by the concentration")
    return (f"the stated absorbance {a:g} over the product of the path length {b:g} cm and "
            f"concentration {c:g} M gives {eps:g}, with four mistaken routes each recomputed "
            "into one distractor")


def n20(item):
    (a,), (eps,), (b,) = (stem_abs(item["q"]), stem_eps(item["q"]), stem_path(item["q"]))
    c = concentration(a, eps, b)
    numeric_key(item, c)
    wrong_route(item, a / eps, "the path length left out of the divisor")
    wrong_route(item, a / (eps * b * b), "the path length counted twice")
    wrong_route(item, 10 * c, "a power of ten misplaced in the answer")
    wrong_route(item, a * eps * b, "the three quantities multiplied instead of divided")
    return (f"the stated absorbance {a:g} over the product of the molar absorptivity {eps:g} "
            f"and path length {b:g} cm gives {c:g} M, with four mistaken routes each "
            "recomputed into one distractor")


def n21(item):
    (a,), (eps,), (c,) = (stem_abs(item["q"]), stem_eps(item["q"]), stem_conc(item["q"]))
    b = path_length(a, eps, c)
    numeric_key(item, b)
    wrong_route(item, eps * c / a, "the quotient taken the other way round")
    wrong_route(item, a * eps * c, "the three quantities multiplied instead of divided")
    wrong_route(item, a / (eps * c / 10), "a power of ten gained by the concentration")
    wrong_route(item, a / (eps * 10 * c), "a power of ten lost from the concentration")
    return (f"the stated absorbance {a:g} over the product of the molar absorptivity {eps:g} "
            f"and concentration {c:g} M gives a path length of {b:g} cm, with four mistaken "
            "routes each recomputed into one distractor")


def n22(item):
    (first,) = stem_abs(item["q"])
    f = stem_factor(item["q"])
    second = first * f
    numeric_key(item, second)
    wrong_route(item, first / f, "the ratio taken the other way round")
    wrong_route(item, first, "the absorbance taken to be unaffected by the concentration")
    wrong_route(item, first * f * f, "the factor applied twice")
    return (f"the stated absorbance {first:g} at the stated factor of {f:g} in concentration "
            f"gives {second:g}, with three mistaken routes each recomputed into one "
            "distractor")


def n23(item):
    (c_p,) = stem_conc(item["q"])
    absorbances = stem_abs(item["q"])
    assert len(absorbances) == 2, f"the stem states the absorbances {absorbances}"
    a_p, a_q = absorbances
    c_q = c_p * (a_q / a_p)
    assert c_q > c_p, (
        f"the second absorbance {a_q:g} is the larger, so its concentration {c_q:g} M must "
        f"exceed the first's {c_p:g} M"
    )
    numeric_key(item, c_q)
    wrong_route(item, c_p * (a_p / a_q), "the ratio of absorbances inverted")
    wrong_route(item, c_q / 10, "a power of ten lost from the answer")
    wrong_route(item, a_q * c_p, "the second absorbance multiplied by the first concentration")
    wrong_route(item, (a_q / a_p) * 1.0e-4, "the bare ratio read as the answer")
    return (f"the stated concentration {c_p:g} M scaled by the ratio of the stated "
            f"absorbances {a_q:g} to {a_p:g} gives {c_q:g} M, with four mistaken routes each "
            "recomputed into one distractor")


def n29(item):
    paths = stem_path(item["q"])
    assert len(paths) == 2, f"the stem states the path lengths {paths}"
    standards, unknown = paths
    # The standards fix the absorbance-to-concentration ratio at the SHORTER path
    # length. The unknown is measured at the longer one, so the absorbance it
    # gives is raised by the ratio of the path lengths and the concentration read
    # off the standards is raised by the same factor.
    true_conc = 3.0e-4
    measured = absorbance(1500.0, unknown, true_conc)
    reported = concentration(measured, 1500.0, standards)
    factor = reported / true_conc
    assert abs(factor - unknown / standards) < 1e-12, (factor, unknown / standards)
    assert agrees(factor, h.keyed(item)), (
        f"the mismatched cuvettes recompute to a reported concentration {factor:g} times the "
        f"true one, but the keyed choice says {stated_change(h.keyed(item))!r}"
    )
    h.shows(item, "twice the true value, because the longer path length raises the absorbance")
    return (f"a true concentration of {true_conc:g} M read in the {unknown:g} cm cuvette "
            f"gives an absorbance of {measured:g}, which the {standards:g} cm standards turn "
            f"back into {reported:g} M, a factor of {factor:g}")


NUMERIC = {12: n12, 13: n13, 14: n14, 15: n15, 16: n16, 17: n17, 18: n18, 19: n19,
           20: n20, 21: n21, 22: n22, 23: n23, 29: n29}


# --------------------------------------------------------------- table items

def _scale(header):
    hits = _HEADER_SCALE.findall(str(header))
    assert len(hits) == 1, f"the header {header!r} names {len(hits)} powers of ten, not one"
    return 10.0 ** int(hits[0])


def _scaled_col(table, header):
    """A column's values with the power of ten its own header names applied."""
    return [v * _scale(header) for v in cg.col(table, header)]


def _cal_ratio(table):
    """The absorbance-to-concentration ratio the standards fix, checked constant."""
    conc_header = table["headers"][1]
    concs = _scaled_col(table, conc_header)
    absorbs = cg.col(table, "Absorbance")
    ratios = [a / c for a, c in zip(absorbs, concs)]
    assert max(ratios) - min(ratios) < 1e-9 * max(ratios), (
        f"the tabulated standards are not proportional, so no single ratio exists: {ratios}"
    )
    return ratios[0], dict(zip(cg.labels(table), zip(concs, absorbs)))


def q24(table, item):
    ratio, rows = _cal_ratio(table)
    (c,) = stem_conc(item["q"])
    a = ratio * c
    numeric_key(item, a)
    tabulated = {lab: pair[1] for lab, pair in rows.items()}
    wrong_route(item, tabulated["Standard 2"], "a tabulated absorbance read off directly")
    wrong_route(item, tabulated["Standard 3"], "the next tabulated absorbance read off")
    wrong_route(item, tabulated["Standard 2"] + tabulated["Standard 3"],
                "two tabulated absorbances added")
    wrong_route(item, tabulated["Standard 1"] / 3.0,
                "the first standard divided by three instead of multiplied")
    return (f"the tabulated standards {rows} fix one absorbance-to-concentration ratio of "
            f"{ratio:g}, which at the stated concentration {c:g} M gives {a:g}")


def q25(table, item):
    ratio, rows = _cal_ratio(table)
    (a,) = stem_abs(item["q"])
    c = a / ratio
    numeric_key(item, c)
    wrong_route(item, c / 2, "the ratio applied to half the absorbance")
    wrong_route(item, c * 2, "the ratio applied to twice the absorbance")
    wrong_route(item, c * 10, "a power of ten gained in the answer")
    wrong_route(item, c / 10, "a power of ten lost from the answer")
    return (f"the tabulated standards {rows} fix one absorbance-to-concentration ratio of "
            f"{ratio:g}, which turns the stated absorbance {a:g} back into {c:g} M")


def q26(table, item):
    eps_header = table["headers"][1]
    epsilons = dict(zip(cg.labels(table), cg.col(table, eps_header)))
    (b,) = stem_path(item["q"])
    (c,) = stem_conc(item["q"])
    absorbances = {lab: absorbance(e, b, c) for lab, e in epsilons.items()}
    lab = _unique_extreme(absorbances, max)
    h.shows(item, lab)
    return (f"the tabulated molar absorptivities {epsilons} at the stated path length {b:g} "
            f"cm and concentration {c:g} M give absorbances {absorbances}, whose unique "
            f"maximum is at {lab}")


def q27(table, item):
    absorbances = dict(zip(cg.labels(table), cg.col(table, "Absorbance of the sample")))
    lab = _unique_extreme(absorbances, max)
    h.shows(item, f"{lab} nm")
    return (f"the tabulated absorbances {absorbances} have their unique maximum at {lab} nm, "
            "which EK 3.13.A.2 names as the setting giving the maximum sensitivity")


def q28(table, item):
    labels = cg.labels(table)
    eps_header, path_header, conc_header = table["headers"][1:]
    epsilons = dict(zip(labels, cg.col(table, eps_header)))
    paths = dict(zip(labels, cg.col(table, path_header)))
    concs = dict(zip(labels, _scaled_col(table, conc_header)))
    absorbances = {lab: absorbance(epsilons[lab], paths[lab], concs[lab]) for lab in labels}
    lab = _unique_extreme(absorbances, max)
    h.shows(item, lab)
    # The whole point of the item is that no single column decides it. If the
    # winner also held the largest molar absorptivity or the longest path
    # length, a student could read one column and be right for the wrong reason.
    assert lab != _unique_extreme(epsilons, max), (
        f"{lab} also holds the largest tabulated molar absorptivity, so the item can be "
        f"answered from one column: {epsilons}"
    )
    assert lab != _unique_extreme(paths, max), (
        f"{lab} also holds the longest tabulated path length, so the item can be answered "
        f"from one column: {paths}"
    )
    assert lab != _unique_extreme(concs, max), (
        f"{lab} also holds the highest tabulated concentration, so the item can be answered "
        f"from one column: {concs}"
    )
    return (f"the tabulated molar absorptivities {epsilons}, path lengths {paths} and "
            f"concentrations {concs} multiply to absorbances {absorbances}, whose unique "
            f"maximum is at {lab} -- which holds no column's maximum on its own")


def _unique_extreme(values, pick):
    lab = pick(values, key=values.get)
    ties = [k for k, v in values.items() if abs(v - values[lab]) < 1e-30]
    assert ties == [lab], f"the extreme is not unique: {ties} all hold {values[lab]}"
    return lab


TABLE_CHECKS = {24: q24, 25: q25, 26: q26, 27: q27, 28: q28}


CLAIMS = [
 ("molar absorptivity, the path length, and the concentration",
  "EK 3.13.A.1 states that the Beer-Lambert law relates the absorption of light by a solution to three variables, and its equation names exactly these three."),
 ("A = \\varepsilon b c",
  "EK 3.13.A.1's EQN, verbatim; framework_equation checks the keyed choice against that transcription and rejects any distractor stating it too."),
 ("How intensely a chemical species absorbs light of a specific wavelength",
  "EK 3.13.A.1's own sentence about the molar absorptivity, including the qualification that it is fixed for light of a specific wavelength."),
 ("The number of light-absorbing particles in the light path",
  "EK 3.13.A.1 states that the path length and concentration are proportional to the number of light-absorbing particles in the light path."),
 ("The path length and the wavelength of light",
  "EK 3.13.A.2's opening sentence: in most experiments the path length and wavelength of light are held constant."),
 ("The concentration of the absorbing molecules or ions",
  "EK 3.13.A.2: in such cases the absorbance is proportional only to the concentration of absorbing molecules or ions."),
 ("wavelength of maximum absorbance for the species being analyzed",
  "EK 3.13.A.2 says the spectrophotometer is typically set to that wavelength, chosen for the species under study rather than for the solvent or the instrument."),
 ("To ensure the maximum sensitivity of the measurement",
  "EK 3.13.A.2 gives that reason in those words for setting the instrument to the wavelength of maximum absorbance."),
 ("The optimum wavelength",
  "EK 3.13.A.2 puts that term in parentheses immediately after the wavelength of maximum absorbance, so the two name one setting."),
 ("The path length",
  "EK 3.13.A.1 names the symbols as it introduces the variables, calling b the path length."),
 ("The absorption of light by the solution",
  "EK 3.13.A.1 introduces the equation as relating the absorption of light by a solution to the three variables on the right."),
 ("It doubles",
  "EK 3.13.A.2 makes the absorbance proportional only to the concentration once the path length and wavelength are held constant. n12 recomputes both absorbances and the factor between them."),
 ("It triples",
  "EK 3.13.A.1's equation multiplies the path length into the absorbance. n13 recomputes both absorbances from the two path lengths the stem states."),
 ("It falls to one fifth of its original value",
  "EK 3.13.A.2's proportionality applied to a dilution measured under the stated constant conditions. n14 recomputes both absorbances and the factor."),
 ("Species M shows twice the absorbance of species N",
  "EK 3.13.A.1 makes the molar absorptivity one of the three factors, so with the other two equal it sets the ratio. n15 recomputes both absorbances."),
 ("It is directly proportional to the concentration",
  "EK 3.13.A.2 states the proportionality for exactly these conditions. n16 recomputes the absorbance-to-concentration ratio at three concentrations and confirms a square-law ratio is not constant."),
 ("It is halved",
  "EK 3.13.A.1's equation multiplies the path length into the absorbance. n17 recomputes both absorbances and the factor between them."),
 ("0.60",
  "EK 3.13.A.1's equation on the stem's own three quantities. n18 recomputes it and four mistaken routes, each of which sits in exactly one distractor."),
 ("3000 \\( \\mathrm{M^{-1}\\,cm^{-1}} \\)",
  "EK 3.13.A.1's equation rearranged for the molar absorptivity. n19 recomputes it from the stem's own absorbance, path length and concentration, and recomputes four mistaken routes."),
 ("3.0 \\times 10^{-4}",
  "EK 3.13.A.1's equation rearranged for the concentration. n20 recomputes it and four mistaken routes."),
 ("2.00 cm",
  "EK 3.13.A.1's equation rearranged for the path length. n21 recomputes it and four mistaken routes."),
 ("0.72",
  "EK 3.13.A.2's proportionality under the stated constant conditions, which is why neither the molar absorptivity nor the path length is needed. n22 recomputes it and three mistaken routes."),
 ("5.0 \\times 10^{-4}",
  "EK 3.13.A.2's proportionality read as a ratio between two solutions of one species. n23 recomputes it and four mistaken routes."),
 ("0.45",
  "EK 3.13.A.2's proportionality applied to the tabulated standards. q24 recomputes the ratio from all three rows, checks it is the same in each, and predicts from it."),
 ("5.0 \\times 10^{-4}",
  "The same ratio read the other way, which is what a calibration is for. q25 recomputes it and four mistaken routes."),
 ("Species Y",
  "EK 3.13.A.1 makes the absorbance the product of the three variables, so with two held equal the tabulated molar absorptivity decides. q26 recomputes all three absorbances."),
 ("510 nm",
  "EK 3.13.A.2 says the instrument is set to the wavelength of maximum absorbance to ensure the maximum sensitivity of measurement. q27 finds that wavelength in the table and checks it is unique."),
 ("Solution F",
  "EK 3.13.A.1's equation over all three tabulated columns. q28 recomputes every product and further checks the answer is not the row holding the largest molar absorptivity or the longest path length."),
 ("twice the true value, because the longer path length raises the absorbance",
  "EK 3.13.A.2 states the proportionality to concentration only where the path length is held constant, and here it was not. n29 recomputes the reported concentration from the two path lengths the stem states."),
 ("molar absorptivity applies to light of a specific wavelength",
  "EK 3.13.A.1 says the molar absorptivity describes how intensely a species absorbs light of a specific wavelength, so changing the wavelength changes that factor at one concentration."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[23]["q"] = "From the calibration curve, what absorbance would it give?"
        no_figure_language(mod)

    def photon_arithmetic_creeps_in(mod, cl):
        mod.QUESTIONS[0]["q"] = (mod.QUESTIONS[0]["q"]
                                 + " Use Planck's equation to decide.")
        no_other_topic(mod)

    def condition_dropped_from_a_stem(mod, cl):
        # The proportionality left standing with no condition attached, which is
        # a claim EK 3.13.A.2 does not make. Every choice is untouched, the key
        # is still the best of the five, and nothing else in this file notices.
        mod.QUESTIONS[15]["q"] = (
            "In an experiment on a solution of an absorbing species, how does the absorbance "
            "vary with the concentration?")
        proportionality_states_its_condition(mod)

    def condition_dropped_from_the_ratio_item(mod, cl):
        mod.QUESTIONS[21]["q"] = (
            "A solution gives an absorbance of 0.24. A second solution of the same species, "
            "at three times the concentration, is measured. What is its absorbance?")
        proportionality_states_its_condition(mod)

    def equation_key_moved(mod, cl):
        mod.QUESTIONS[1]["ans"] = 4
        cl[1] = ("\\varepsilon = A b c", cl[1][1])
        framework_equation(mod)

    def framework_equation_offered_twice(mod, cl):
        ch = list(mod.QUESTIONS[1]["choices"])
        ch[2] = "\\( A = \\varepsilon b c \\)"
        mod.QUESTIONS[1]["choices"] = ch
        framework_equation(mod)

    def direction_inverted(mod, cl):
        # A dilution keyed to a RISE in absorbance: the magnitude is untouched
        # and only the direction is wrong, which is this topic's analogue of the
        # sign defect in unit 6.
        mod.QUESTIONS[13]["ans"] = 1
        cl[13] = ("It is five times its original value", cl[13][1])

    def path_length_change_inverted(mod, cl):
        mod.QUESTIONS[16]["ans"] = 1
        cl[16] = ("It doubles", cl[16][1])

    def stem_factor_edited(mod, cl):
        # The stem says the concentration is tripled while the key still says it
        # doubles. Nothing but the recomputation can see it.
        mod.QUESTIONS[11]["q"] = mod.QUESTIONS[11]["q"].replace(
            "is doubled", "is increased three times")
        mod.QUESTIONS[11]["q"] = mod.QUESTIONS[11]["q"].replace(
            "increased three times", "raised by three times")

    def stem_path_lengths_swapped(mod, cl):
        mod.QUESTIONS[12]["q"] = mod.QUESTIONS[12]["q"].replace(
            "from a 1.00 cm cuvette to a 3.00 cm cuvette",
            "from a 3.00 cm cuvette to a 1.00 cm cuvette")

    def stem_concentration_edited(mod, cl):
        mod.QUESTIONS[17]["q"] = mod.QUESTIONS[17]["q"].replace(
            "2.0 \\times 10^{-4}", "3.0 \\times 10^{-4}")

    def numeric_key_moved(mod, cl):
        mod.QUESTIONS[18]["ans"] = 1
        cl[18] = ("6000 \\( \\mathrm{M^{-1}\\,cm^{-1}} \\)", cl[18][1])

    def mistaken_route_distractor_removed(mod, cl):
        ch = list(mod.QUESTIONS[19]["choices"])
        ch[2] = "\\( 8.8 \\times 10^{-7} \\) M"
        mod.QUESTIONS[19]["choices"] = ch

    def inverted_quotient_keyed(mod, cl):
        # The path-length item keyed to the reciprocal, which is the mistake the
        # item exists to test.
        mod.QUESTIONS[20]["ans"] = 1
        cl[20] = ("0.50 cm", cl[20][1])

    def ratio_inverted_in_the_two_solution_item(mod, cl):
        mod.QUESTIONS[22]["ans"] = 1
        cl[22] = ("8.0 \\times 10^{-5}", cl[22][1])

    def calibration_row_made_nonproportional(mod, cl):
        # One tabulated absorbance edited so the standards no longer fix a single
        # ratio. The key is untouched and still looks reasonable.
        mod.QUESTIONS[23]["table"] = dict(
            headers=h3_13._T_CAL["headers"],
            rows=[["Standard 1", "1.0", "0.15"],
                  ["Standard 2", "2.0", "0.40"],
                  ["Standard 3", "4.0", "0.60"]])

    def calibration_scale_changed(mod, cl):
        # Only the column header edited. Every row value is untouched.
        mod.QUESTIONS[24]["table"] = dict(
            headers=["Standard", "Concentration (in units of \\( 10^{-3} \\) M)",
                     "Absorbance"],
            rows=list(h3_13._T_CAL["rows"]))

    def tabulated_absorptivity_moved(mod, cl):
        mod.QUESTIONS[25]["table"] = dict(
            headers=h3_13._T_EPS["headers"],
            rows=[["Species X", "3000"], ["Species Y", "2500"], ["Species Z", "1200"]])

    def tabulated_maximum_wavelength_moved(mod, cl):
        mod.QUESTIONS[26]["table"] = dict(
            headers=h3_13._T_WL["headers"],
            rows=[["440", "0.12"], ["510", "0.62"], ["590", "0.71"]])

    def tabulated_absorbances_tied(mod, cl):
        mod.QUESTIONS[26]["table"] = dict(
            headers=h3_13._T_WL["headers"],
            rows=[["440", "0.12"], ["510", "0.62"], ["590", "0.62"]])

    def three_column_winner_also_wins_a_column(mod, cl):
        # The winning row given the largest molar absorptivity as well, so the
        # item can be answered by reading one column. The KEY is still correct,
        # which is why nothing but the explicit guard can reject it.
        mod.QUESTIONS[27]["table"] = dict(
            headers=h3_13._T_SOLN["headers"],
            rows=[["Solution D", "2500", "0.50", "4.0"],
                  ["Solution E", "1000", "2.00", "2.0"],
                  ["Solution F", "3000", "1.00", "3.0"]])

    def three_column_row_edited(mod, cl):
        mod.QUESTIONS[27]["table"] = dict(
            headers=h3_13._T_SOLN["headers"],
            rows=[["Solution D", "2500", "0.50", "9.0"],
                  ["Solution E", "1000", "2.00", "2.0"],
                  ["Solution F", "2000", "1.00", "3.0"]])

    def mismatched_cuvette_direction_inverted(mod, cl):
        mod.QUESTIONS[28]["ans"] = 1
        cl[28] = ("half the true value, because the longer path length lowers the absorbance",
                  cl[28][1])

    return [
        ("a stem referring to a calibration curve the bank cannot show", figure_language),
        ("3.12's photon arithmetic creeping into a stem", photon_arithmetic_creeps_in),
        ("EK 3.13.A.2's condition dropped from a proportionality item",
         condition_dropped_from_a_stem),
        ("the constant conditions dropped from the two-solution ratio item",
         condition_dropped_from_the_ratio_item),
        ("the equation item keyed to a rearrangement", equation_key_moved),
        ("the framework's equation offered as a distractor as well as the key",
         framework_equation_offered_twice),
        ("a dilution keyed to a rise in absorbance", direction_inverted),
        ("a shorter cuvette keyed to a rise in absorbance", path_length_change_inverted),
        ("the change stated in a stem edited under an untouched key", stem_factor_edited),
        ("the two path lengths exchanged in a stem", stem_path_lengths_swapped),
        ("a stem's concentration edited under an untouched keyed absorbance",
         stem_concentration_edited),
        ("a numeric key moved onto the path-length-omitted route", numeric_key_moved),
        ("the distractor carrying a recomputed wrong route replaced",
         mistaken_route_distractor_removed),
        ("the path-length item keyed to the inverted quotient", inverted_quotient_keyed),
        ("the two-solution item keyed to the inverted ratio",
         ratio_inverted_in_the_two_solution_item),
        ("a calibration row edited so the standards are no longer proportional",
         calibration_row_made_nonproportional),
        ("the power of ten in the calibration header changed", calibration_scale_changed),
        ("a tabulated molar absorptivity raised so the strongest absorber moves",
         tabulated_absorptivity_moved),
        ("a tabulated absorbance raised so the optimum wavelength moves",
         tabulated_maximum_wavelength_moved),
        ("two tabulated absorbances tied at the maximum", tabulated_absorbances_tied),
        ("the winning row given the largest molar absorptivity too, so one column answers it",
         three_column_winner_also_wins_a_column),
        ("a tabulated concentration raised so the greatest absorbance moves",
         three_column_row_edited),
        ("the mismatched-cuvette item keyed to a fall in the reported concentration",
         mismatched_cuvette_direction_inverted),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h3_13, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

_change_matcher_self_check()
_condition_matcher_self_check()
no_figure_language(h3_13)
no_other_topic(h3_13)
proportionality_states_its_condition(h3_13)
framework_equation(h3_13)
h.run(h3_13, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
