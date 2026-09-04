"""Key audit for AP CHEMISTRY 3.12 Properties of Photons.

One (anchor, claim) per item, in module order.

WHY THIS FILE EXISTS AT ALL. h3_12.py was written by an agent that was stopped
by a session limit before it wrote a verifier, so thirty questions sat in the
bank with NO gate on them -- not a weak gate, none. Everything below was written
against the module afterwards, and the audit that produced it found three real
defects, all now fixed in h3_12.py:

  * item 18 was item 3 asked a second time. Both stems asked which equation the
    framework gives for wavelength and frequency and both keyed
    ``\\( c = \\lambda \\nu \\)``. Item 18 now asks which product is the same for
    every electromagnetic wave, which is the same sentence read for what it
    implies rather than recited twice.
  * two equation items carried a ``+`` distractor -- ``\\( c = \\lambda + \\nu \\)``
    against the keyed ``\\( c = \\lambda \\nu \\)``. ``cg.normalize`` drops a
    ``+``, so the two collapse to the SAME token string and the anchor pinning
    the key would have matched the distractor as well. The distractors are now
    rearrangements, which normalize apart. This is the same family as the sign
    bug fixed in ``cg.contains_phrase``: a matcher that looks right and quietly
    cannot tell two things apart.
  * item 21 asked for a frequency and offered a distractor labelled in joules,
    which a student could eliminate on units without doing the chemistry, and
    its other distractor was not the value any mistaken route actually gives.
    Both are now the two real mistaken routes, and both are recomputed here.

WHAT THE KEYS REST ON.

  3.12.A.1  a photon absorbed (or emitted) increases (or decreases) the energy
            of the species by an amount EQUAL TO the energy of the photon
                     1, 2, 11, 12, 19, 20, 23, 24, 27, 28, 30
  3.12.A.2  EQN c = lambda nu, and Planck's equation EQN E = h nu
                     3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 18, 20, 21,
                     22, 25, 26, 29, 30

THE SWAP THAT MUST NOT SHIP. EK 3.12.A.1 folds both cases into one sentence with
a parenthesis, which is exactly how a bank ends up keying absorption to a
decrease. ``pairing_never_swapped`` reads the process word and the direction word
out of each item -- from the KEY where the key states it and from the stem
otherwise -- and compares two named strings against one transcription of the
framework's sentence. Nothing is indexed into parallel lists, which is the
mistake that made an earlier verifier in this bank reject a correct key. There is
no exemption clause: no item here keys a mismatched pairing, so admitting one
would be an untested hole.

ARITHMETIC. Every number a key asserts is recomputed from the stimulus alone.
The stem values are read out of the stem by the WORDS in front of them
(``wavelength of``, ``speed of light as``, ``constant as``), never by position,
so reordering a stem cannot silently repoint a check at the wrong quantity; the
tabulated values are read from the table with the power of ten taken from the
COLUMN HEADER rather than from a constant here. Choices are compared as parsed
NUMBERS, not as formatted strings, and each check asserts that exactly one choice
matches the recomputed value and that it is the keyed one. Where a wrong route
gives a value that is offered, that value is recomputed too and required to sit
in exactly one distractor, so an item cannot quietly stop testing the error it
exists to test.

SCOPE. 3.11 owns which spectral region goes with which kind of transition and
3.13 owns absorbance and the Beer-Lambert law. ``no_other_topic`` bans both from
every stem and every KEYED choice. A distractor may name them -- item 29's
"the concentration of the absorbing species" is there precisely because the
letter c means something else in 3.13's equation -- and a rationale may explain
the distinction.

NEGATIVE CONTROL: ``python3 verify_h3_12.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h3_12

# ------------------------------------------------------------------- patterns

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below|the spectrum above|the spectrum below)(?![a-z])",
    re.I)

# 3.11 owns the region/transition associations; 3.13 owns Beer-Lambert.
_OTHER_TOPIC = re.compile(
    r"(?<![A-Za-z])(Beer-Lambert|absorbance|molar absorptivity|path length|"
    r"concentration|microwave|infrared|ultraviolet|rotational|vibrational)(?![A-Za-z])",
    re.I)

# Scientific notation as this module writes it: a mantissa, \times, a power of
# ten, all inside one hand-written span.
_SCI = re.compile(
    r"\\\(\s*(-?\d+(?:\.\d+)?)\s*\\times\s*10\^\{(-?\d+)\}\s*\\\)")

# The power of ten a table column header names, e.g. "(in units of \( 10^{14} \)
# per second)". Read from the header so an edited header cannot leave a stale
# scale factor in this file.
_HEADER_SCALE = re.compile(r"10\^\{(-?\d+)\}")

_NM = re.compile(r"(?<![0-9])(\d+)\s*nm(?![a-z])", re.I)

# The constants the stems themselves quote. Used only for the proportional
# items, where no number is asked for and only a ratio is.
C_LIGHT = 3.00e8
H_PLANCK = 6.626e-34


# ------------------------------------------------------- EK 3.12.A.2's equations

def frequency_from_wavelength(c, wavelength):
    """EK 3.12.A.2's EQN c = lambda nu, rearranged for the frequency."""
    return c / wavelength


def wavelength_from_frequency(c, nu):
    """The same equation rearranged the other way."""
    return c / nu


def photon_energy(h_planck, nu):
    """EK 3.12.A.2's Planck equation, EQN E = h nu."""
    return h_planck * nu


def frequency_from_energy(h_planck, energy):
    """Planck's equation rearranged for the frequency."""
    return energy / h_planck


# --------------------------------------------- EK 3.12.A.1's one transcription

# The framework's sentence, transcribed ONCE. Absorption with an increase,
# emission with a decrease, and the size of the change equal to the photon's
# energy either way.
PAIRING = {"absorbed": "increase", "emitted": "decrease"}

_PROCESS_WORDS = [
    ("absorbed", re.compile(
        r"(?<![a-z])(?:absorb(?:s|ed|ing)?|absorption)(?![a-z])", re.I)),
    ("emitted", re.compile(
        r"(?<![a-z])(?:emit(?:s|ted|ting)?|emission)(?![a-z])", re.I)),
]
_DIRECTION_WORDS = [
    ("increase", re.compile(r"(?<![a-z])increase[ds]?(?![a-z])", re.I)),
    ("decrease", re.compile(r"(?<![a-z])decrease[ds]?(?![a-z])", re.I)),
]


def _named(text, table):
    """Every distinct name from ``table`` whose pattern appears in ``text``."""
    return sorted({name for name, pat in table if pat.search(text)})


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
    print(f"OK  {module.TOPIC[0]} figures: every frequency, wavelength and energy is carried "
          "as a number in a table or a stem, and no item points at a picture.")


def no_other_topic(module):
    """Stems and KEYED choices only.

    A distractor is allowed to reach for a neighbouring topic's quantity, and
    one should: item 29 offers the concentration of the absorbing species
    because the letter c means that in 3.13's equation and the speed of light in
    this one, which is the confusion the item exists to test. What must not
    happen is a stem ASKING for one of those quantities or a KEY asserting one.
    """
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
                f"3.11's or 3.13's material -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no stem or key reaches for 3.11's spectral regions "
          "or 3.13's absorbance, path length and concentration.")


def pairing_never_swapped(module):
    """Every item stating one process and one direction must pair them EK 3.12.A.1's way."""
    checked = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key, stem = h.keyed(item), item["q"]
        # Precedence to the key, since the key is what is being asserted; the
        # stem supplies the half the key leaves implicit.
        processes = _named(key, _PROCESS_WORDS) or _named(stem, _PROCESS_WORDS)
        directions = _named(key, _DIRECTION_WORDS) or _named(stem, _DIRECTION_WORDS)
        if len(processes) != 1 or len(directions) != 1:
            # Zero or several of either: no single pairing is being asserted,
            # so there is nothing here for this check to read.
            continue

        process, direction = processes[0], directions[0]
        expected = PAIRING[process]
        assert direction == expected, (
            f"{module.TOPIC[0]} q{i}: this item pairs {process!r} with a(n) {direction!r} in "
            f"the energy of the species, but EK 3.12.A.1 pairs it with a(n) {expected!r} -- "
            f"stem {stem[:70]!r}, key {key!r}"
        )
        checked.append(i)

    assert len(checked) >= 6, (
        f"only {len(checked)} item(s) state one process and one direction, so this check has "
        "almost nothing to read and proves little"
    )
    print(f"OK  {module.TOPIC[0]} pairing: {len(checked)} item(s) state one of absorption or "
          f"emission together with one direction of energy change, and every one matches "
          f"EK 3.12.A.1: {checked}")


# The two equations EK 3.12.A.2 gives, transcribed once, and the items that ask
# for them by name.
EQUATIONS = {3: "c = \\lambda \\nu", 4: "E = h \\nu"}


def framework_equations(module):
    """The equation items key the framework's own form, and only it."""
    forms = {i: "\\( " + body + " \\)" for i, body in EQUATIONS.items()}
    for i, wanted in sorted(forms.items()):
        item = module.QUESTIONS[i - 1]
        assert h.keyed(item) == wanted, (
            f"{module.TOPIC[0]} q{i}: the keyed choice is {h.keyed(item)!r}, but EK 3.12.A.2 "
            f"gives {wanted!r}"
        )
        others = [k for k, c in enumerate(item["choices"])
                  if k != item["ans"] and c in forms.values()]
        assert not others, (
            f"{module.TOPIC[0]} q{i}: choice(s) {others} also state one of the framework's "
            "equations verbatim, so the item has more than one defensible answer"
        )
    print(f"OK  {module.TOPIC[0]} equations: the {len(forms)} item(s) asking for a framework "
          "equation key its exact form, and no distractor states either equation.")


# ---------------------------------------------------------- numeric machinery

_QUANTITY = [
    ("wavelength", re.compile(r"wavelength of\s*$", re.I)),
    ("speed_of_light", re.compile(r"speed of\s+light as\s*$", re.I)),
    ("frequency", re.compile(r"frequency of\s*$", re.I)),
    ("planck", re.compile(r"constant as\s*$", re.I)),
    ("energy", re.compile(r"(?:energy is|carries)\s*$", re.I)),
]


def stem_values(stem):
    """Every scientific-notation value in a stem, named by the WORDS before it.

    Never by position. A stem that says "taking the speed of light as X and
    Planck's constant as Y" can be rewritten in the other order without this
    check silently swapping the two.
    """
    out = {}
    for m in _SCI.finditer(stem):
        before = stem[:m.start()]
        hits = [name for name, pat in _QUANTITY if pat.search(before)]
        assert len(hits) == 1, (
            f"the value {m.group(0)!r} is introduced by words this check cannot name "
            f"({hits}) -- {before[-40:]!r}"
        )
        assert hits[0] not in out, f"{hits[0]!r} is given twice in {stem[:70]!r}"
        out[hits[0]] = float(m.group(1)) * 10.0 ** int(m.group(2))
    return out


def choice_value(text):
    """The single scientific-notation value a choice states, or None."""
    hits = _SCI.findall(text)
    if len(hits) != 1:
        return None
    return float(hits[0][0]) * 10.0 ** int(hits[0][1])


def _matches(value, target, tol=0.005):
    return value is not None and abs(value - target) <= tol * abs(target)


def sci_key(item, expected, direction=None):
    """Exactly one choice states ``expected``, and it is the keyed one.

    ``direction`` is for the items where the MAGNITUDE alone cannot separate the
    key from its distractor: EK 3.12.A.1 makes the change equal in size whether
    a photon is absorbed or emitted, so the reversed choice carries the same
    number and only the word tells them apart. Where a direction is given, the
    choices matching the value are filtered by the direction they state, the
    keyed one must be the only one stating the right direction, and the reversed
    choice must EXIST in exactly one distractor -- otherwise the item has
    quietly stopped testing the one error this topic is exposed to.
    """
    vals = [choice_value(c) for c in item["choices"]]
    close = [k for k, v in enumerate(vals) if _matches(v, expected)]
    if direction is None:
        assert close == [item["ans"]], (
            f"the recomputed value {expected:g} matches choice(s) {close}; it must match the "
            f"keyed choice {item['ans']} and no other -- choices {item['choices']}"
        )
        return expected

    assert direction in ("increase", "decrease"), direction
    reversed_word = "decrease" if direction == "increase" else "increase"
    said = [_named(c, _DIRECTION_WORDS) for c in item["choices"]]
    right = [k for k in close if said[k] == [direction]]
    assert right == [item["ans"]], (
        f"the recomputed value {expected:g} stated with a(n) {direction!r} appears in "
        f"choice(s) {right}; it must be the keyed choice {item['ans']} and no other -- "
        f"choices {item['choices']}"
    )
    flipped = [k for k in close if said[k] == [reversed_word]]
    assert len(flipped) == 1, (
        f"the same magnitude stated with a(n) {reversed_word!r} appears in {len(flipped)} "
        "choice(s); exactly one distractor must carry it, or the item stops testing the "
        f"reversal EK 3.12.A.1 is exposed to -- choices {item['choices']}"
    )
    return expected


def wrong_route(item, value, origin):
    """A recomputed WRONG value must sit in exactly one distractor, never the key."""
    vals = [choice_value(c) for c in item["choices"]]
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


FACTOR_WORD = {
    2.0: "It doubles",
    0.5: "It is halved",
    4.0: "It quadruples",
    1.0: "It is unchanged",
    0.25: "It falls to one quarter",
}


def factor_word(factor):
    hits = [w for f, w in FACTOR_WORD.items() if abs(factor - f) < 1e-9]
    assert len(hits) == 1, f"the recomputed factor {factor!r} names {hits}, not one phrase"
    return hits[0]


# ------------------------------------------------------------- stem numerics

def n5(item):
    """Planck's equation with the frequency doubled."""
    nu = 5.00e14
    factor = photon_energy(H_PLANCK, 2 * nu) / photon_energy(H_PLANCK, nu)
    word = factor_word(factor)
    h.shows(item, word)
    return (f"Planck's equation gives {photon_energy(H_PLANCK, nu):g} J at the base frequency "
            f"and {photon_energy(H_PLANCK, 2 * nu):g} J at twice it, a factor of {factor:g}, "
            f"which is {word.lower()}")


def n6(item):
    """c = lambda nu with the wavelength doubled."""
    lam = 6.00e-7
    factor = (frequency_from_wavelength(C_LIGHT, 2 * lam)
              / frequency_from_wavelength(C_LIGHT, lam))
    word = factor_word(factor)
    h.shows(item, word)
    return (f"the fixed speed of light gives {frequency_from_wavelength(C_LIGHT, lam):g} per "
            f"second at the base wavelength and "
            f"{frequency_from_wavelength(C_LIGHT, 2 * lam):g} at twice it, a factor of "
            f"{factor:g}, which is {word.lower()}")


def n7(item):
    """Both equations in sequence, with the wavelength halved."""
    lam = 6.00e-7
    before = photon_energy(H_PLANCK, frequency_from_wavelength(C_LIGHT, lam))
    after = photon_energy(H_PLANCK, frequency_from_wavelength(C_LIGHT, lam / 2))
    factor = after / before
    word = factor_word(factor)
    h.shows(item, word)
    return (f"halving the wavelength takes the energy from {before:g} J to {after:g} J "
            f"through the two equations in sequence, a factor of {factor:g}, which is "
            f"{word.lower()}")


def n8(item):
    v = stem_values(item["q"])
    nu = frequency_from_wavelength(v["speed_of_light"], v["wavelength"])
    sci_key(item, nu)
    wrong_route(item, v["speed_of_light"] * v["wavelength"],
                "the two multiplied instead of divided")
    wrong_route(item, v["wavelength"] / v["speed_of_light"],
                "the division taken the other way round")
    return (f"the stated wavelength {v['wavelength']:g} m into the stated speed of light "
            f"{v['speed_of_light']:g} m/s gives {nu:g} per second, with two mistaken routes "
            "each recomputed and each in exactly one distractor")


def n9(item):
    v = stem_values(item["q"])
    e = photon_energy(v["planck"], v["frequency"])
    sci_key(item, e)
    wrong_route(item, v["planck"] / v["frequency"], "the constant divided by the frequency")
    wrong_route(item, v["frequency"] / v["planck"], "the frequency divided by the constant")
    return (f"Planck's equation on the stated frequency {v['frequency']:g} per second and "
            f"constant {v['planck']:g} J s gives {e:g} J, with both mistaken quotients "
            "recomputed and each in exactly one distractor")


def n10(item):
    v = stem_values(item["q"])
    lam = wavelength_from_frequency(v["speed_of_light"], v["frequency"])
    sci_key(item, lam)
    wrong_route(item, v["speed_of_light"] * v["frequency"],
                "the two multiplied instead of divided")
    return (f"the stated speed of light {v['speed_of_light']:g} m/s over the stated frequency "
            f"{v['frequency']:g} per second gives {lam:g} m, with the multiplied route "
            "recomputed and sitting in exactly one distractor")


def n11(item):
    """EK 3.12.A.1: the increase is EQUAL to the photon's energy."""
    v = stem_values(item["q"])
    sci_key(item, v["energy"], direction="increase")
    wrong_route(item, v["energy"] / 2, "half the photon's energy transferred")
    wrong_route(item, v["energy"] * 2, "twice the photon's energy transferred")
    return (f"the stated photon energy is {v['energy']:g} J and EK 3.12.A.1 makes the change "
            "equal to it, with the halved and doubled routes each recomputed into one "
            "distractor")


def n12(item):
    v = stem_values(item["q"])
    sci_key(item, v["energy"], direction="decrease")
    wrong_route(item, v["energy"] / 2, "half the photon's energy transferred")
    wrong_route(item, v["energy"] * 2, "twice the photon's energy transferred")
    return (f"the stated photon energy is {v['energy']:g} J and EK 3.12.A.1 makes the "
            "decrease equal to it, with the halved and doubled routes each recomputed into "
            "one distractor")


def n21(item):
    v = stem_values(item["q"])
    nu = frequency_from_energy(v["planck"], v["energy"])
    sci_key(item, nu)
    wrong_route(item, v["energy"] * v["planck"],
                "the two multiplied instead of divided")
    wrong_route(item, v["planck"] / v["energy"],
                "the division taken the other way round")
    return (f"the stated energy {v['energy']:g} J over the stated constant {v['planck']:g} "
            f"J s gives {nu:g} per second, with both mistaken routes recomputed and each in "
            "exactly one distractor")


def n22(item):
    v = stem_values(item["q"])
    nu = frequency_from_wavelength(v["speed_of_light"], v["wavelength"])
    e = photon_energy(v["planck"], nu)
    sci_key(item, e)
    wrong_route(item, v["planck"] / nu, "the constant divided by the frequency")
    return (f"the stated wavelength {v['wavelength']:g} m gives {nu:g} per second through the "
            f"speed of light, and Planck's constant then gives {e:g} J, with the inverted "
            "second step recomputed into exactly one distractor")


def n25(item):
    """Energy against wavelength, from the two wavelengths the stem states."""
    nm = [int(x) for x in _NM.findall(item["q"])]
    assert len(nm) == 2 and len(set(nm)) == 2, f"the stem states the wavelengths {nm}"
    energies = {n: photon_energy(H_PLANCK, frequency_from_wavelength(C_LIGHT, n * 1e-9))
                for n in nm}
    short = min(energies, key=lambda n: n)
    long_ = max(energies, key=lambda n: n)
    assert energies[short] > energies[long_], (
        f"the shorter wavelength must carry the greater energy: {energies}"
    )
    ratio = energies[short] / energies[long_]
    assert abs(ratio - 2.0) < 1e-9, f"the energies stand in the ratio {ratio}"
    h.shows(item, f"The {short} nm photon carries twice the energy")
    return (f"the two stated wavelengths give photon energies {energies}, whose ratio is "
            f"{ratio:g}, so the {short} nm photon carries twice what the {long_} nm photon "
            "does")


NUMERIC = {5: n5, 6: n6, 7: n7, 8: n8, 9: n9, 10: n10, 11: n11, 12: n12,
           21: n21, 22: n22, 25: n25}


# --------------------------------------------------------------- table items

def _scale(header):
    """The power of ten the column header names."""
    hits = _HEADER_SCALE.findall(str(header))
    assert len(hits) == 1, f"the header {header!r} names {len(hits)} powers of ten, not one"
    return 10.0 ** int(hits[0])


def _column(table):
    """``{row label: value}`` from the table's one data column, header scale applied."""
    header = table["headers"][1]
    scale = _scale(header)
    return {lab: v * scale for lab, v in zip(cg.labels(table), cg.col(table, header))}


def _unique_extreme(values, pick):
    lab = pick(values, key=values.get)
    ties = [k for k, v in values.items() if abs(v - values[lab]) < 1e-30]
    assert ties == [lab], f"the extreme is not unique: {ties} all hold {values[lab]}"
    return lab


def q13(table, item):
    """Planck's equation applied to every tabulated frequency."""
    freqs = _column(table)
    energies = {lab: photon_energy(H_PLANCK, f) for lab, f in freqs.items()}
    lab = _unique_extreme(energies, max)
    h.shows(item, lab)
    return (f"the tabulated frequencies {freqs} give photon energies {energies} through "
            f"Planck's equation, whose unique maximum is at {lab}")


def q14(table, item):
    """c = lambda nu applied to every tabulated wavelength."""
    waves = _column(table)
    freqs = {lab: frequency_from_wavelength(C_LIGHT, w) for lab, w in waves.items()}
    lab = _unique_extreme(freqs, max)
    h.shows(item, lab)
    return (f"the tabulated wavelengths {waves} give frequencies {freqs} through the fixed "
            f"speed of light, whose unique maximum is at {lab}")


def q15(table, item):
    """Both equations in sequence, over every tabulated wavelength."""
    waves = _column(table)
    energies = {lab: photon_energy(H_PLANCK, frequency_from_wavelength(C_LIGHT, w))
                for lab, w in waves.items()}
    lab = _unique_extreme(energies, min)
    h.shows(item, lab)
    return (f"the tabulated wavelengths {waves} give photon energies {energies} through the "
            f"two equations in sequence, whose unique minimum is at {lab}")


def q16(table, item):
    waves = _column(table)
    v = stem_values(item["q"])
    nu = frequency_from_wavelength(v["speed_of_light"], waves["Photon L"])
    sci_key(item, nu)
    return (f"the tabulated wavelength for that row is {waves['Photon L']:g} m, which with "
            f"the stated speed of light {v['speed_of_light']:g} m/s gives {nu:g} per second")


def q27(table, item):
    """EK 3.12.A.1 makes the increase equal to the photon's energy."""
    energies = _column(table)
    lab = _unique_extreme(energies, max)
    h.shows(item, lab)
    return (f"the tabulated photon energies are {energies}, and EK 3.12.A.1 makes each "
            f"increase equal to one of them, so the unique maximum at {lab} gives the "
            "largest increase")


def q28(table, item):
    energies = _column(table)
    sci_key(item, energies["Photon R"])
    wrong_route(item, energies["Photon R"] / 2, "half the photon's energy transferred")
    wrong_route(item, energies["Photon R"] * 2, "twice the photon's energy transferred")
    return (f"the tabulated energy for that row is {energies['Photon R']:g} J and EK 3.12.A.1 "
            "makes the increase equal to it, with the halved and doubled routes each "
            "recomputed into one distractor")


TABLE_CHECKS = {13: q13, 14: q14, 15: q15, 16: q16, 27: q27, 28: q28}


CLAIMS = [
 ("increases by an amount equal to the energy of the photon",
  "EK 3.12.A.1: when a photon is absorbed by an atom or molecule the energy of the species is increased by an amount equal to the energy of the photon."),
 ("decreases by an amount equal to the energy of the photon",
  "EK 3.12.A.1's parenthesis: emission decreases the energy of the species by the same amount, so only the direction differs from the absorbing case."),
 ("c = \\lambda \\nu",
  "EK 3.12.A.2's first EQN, verbatim; framework_equations checks the keyed choice against that transcription and rejects any distractor stating it too."),
 ("E = h \\nu",
  "EK 3.12.A.2's second EQN, which the framework names Planck's equation, checked the same way."),
 ("It doubles",
  "EK 3.12.A.2's Planck equation makes the energy a constant times the frequency. n5 recomputes both energies and the factor between them."),
 ("It is halved",
  "EK 3.12.A.2 fixes the product of wavelength and frequency at the speed of light. n6 recomputes both frequencies and the factor between them."),
 ("It doubles",
  "EK 3.12.A.2's two equations in sequence: halving the wavelength doubles the frequency and therefore the energy. n7 recomputes both energies."),
 ("5.00 \\times 10^{14}",
  "EK 3.12.A.2's first EQN rearranged for the frequency. n8 recomputes it from the stem's own wavelength and speed of light, and recomputes two mistaken routes."),
 ("3.31 \\times 10^{-19}",
  "EK 3.12.A.2's Planck equation on the stem's own frequency and constant. n9 recomputes it and both mistaken quotients."),
 ("3.00 \\times 10^{-7}",
  "EK 3.12.A.2's first EQN rearranged for the wavelength. n10 recomputes it and the multiplied route."),
 ("increases by \\( 4.0 \\times 10^{-19} \\) joules",
  "EK 3.12.A.1 makes the change equal in size to the photon's energy and upward for an absorption. n11 recomputes the equality and both partial-transfer routes."),
 ("decreases by \\( 2.5 \\times 10^{-19} \\) joules",
  "The same sentence read for emission, where the change is equal in size and downward. n12 recomputes it."),
 ("Photon 2",
  "EK 3.12.A.2's Planck equation applied to every tabulated frequency. q13 recomputes all three energies and checks the maximum is unique."),
 ("Photon J",
  "EK 3.12.A.2's first EQN applied to every tabulated wavelength. q14 recomputes all three frequencies and checks the maximum is unique."),
 ("Photon K",
  "EK 3.12.A.2's two equations in sequence over the tabulated wavelengths. q15 recomputes all three energies and checks the minimum is unique."),
 ("1.0 \\times 10^{15}",
  "EK 3.12.A.2's first EQN on that row's tabulated wavelength. q16 reads the value and its power of ten from the table and header, not from a constant here."),
 ("The frequency of the electromagnetic wave",
  "EK 3.12.A.2 says the energy of a photon is related to the FREQUENCY of the electromagnetic wave through Planck's equation; wavelength enters only through the other equation."),
 ("wavelength and the frequency",
  "EK 3.12.A.2 sets the product of wavelength and frequency equal to the speed of light, which is the same for every electromagnetic wave, while Planck's equation fixes no product at all."),
 ("The two are equal",
  "EK 3.12.A.1 says the energy of the species is decreased by an amount EQUAL TO the energy of the photon, so the two quantities are the same number."),
 ("higher frequency, since Planck's equation gives it the larger energy",
  "EK 3.12.A.2 makes the photon energy proportional to frequency and EK 3.12.A.1 makes the change in the species' energy equal to that energy."),
 ("3.00 \\times 10^{15}",
  "EK 3.12.A.2's Planck equation rearranged for the frequency. n21 recomputes it from the stem's own energy and constant, and recomputes both mistaken routes."),
 ("9.94 \\times 10^{-19}",
  "Both of EK 3.12.A.2's equations in order, the wavelength giving the frequency and the frequency the energy. n22 recomputes the pathway and the inverted second step."),
 ("only part of the photon's energy is transferred",
  "EK 3.12.A.1's word is EQUAL, which makes the whole of the photon's energy the size of the change; the rejected statements are each part of what the sentence does assert."),
 ("Emitted",
  "EK 3.12.A.1 pairs emission with a decrease in the energy of the species, so the direction of the observed change identifies the process."),
 ("400 nm photon carries twice the energy",
  "EK 3.12.A.2's two equations make the photon energy inversely proportional to wavelength. n25 recomputes both energies from the wavelengths the stem states."),
 ("Inversely, so a longer wavelength means a lower energy",
  "EK 3.12.A.2 makes frequency inversely proportional to wavelength and energy directly proportional to frequency, which together leave energy falling as wavelength rises."),
 ("Photon Q",
  "EK 3.12.A.1 makes the increase equal to the energy of the photon absorbed. q27 recomputes the tabulated energies and checks the maximum is unique."),
 ("3.0 \\times 10^{-19}",
  "EK 3.12.A.1 applied to that row's tabulated energy, with the power of ten read from the column header. q28 recomputes it and both partial-transfer routes."),
 ("The speed of light",
  "EK 3.12.A.2 introduces the equation as relating the wavelength of the electromagnetic wave to its frequency and the speed of light."),
 ("absorbing or emitting it changes the species' energy by that same amount",
  "EK 3.12.A.2 supplies both equations and EK 3.12.A.1 the equality between the photon's energy and the change in the species' energy; each rejected option breaks one of those links."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[12]["q"] = "In the graph above, which photon carries the most energy?"
        no_figure_language(mod)

    def beer_lambert_creeps_in(mod, cl):
        mod.QUESTIONS[0]["q"] = (mod.QUESTIONS[0]["q"]
                                 + " Use the Beer-Lambert law to decide.")
        no_other_topic(mod)

    def spectral_region_creeps_in(mod, cl):
        ch = list(mod.QUESTIONS[16]["choices"])
        ch[0] = "The frequency of the infrared radiation"
        mod.QUESTIONS[16]["choices"] = ch
        cl[16] = ("The frequency of the infrared radiation", cl[16][1])
        no_other_topic(mod)

    def absorption_keyed_to_a_decrease(mod, cl):
        # The classic defect: EK 3.12.A.1's parenthesis read backwards, so an
        # absorption is keyed to the atom LOSING energy. Every choice is
        # untouched and the new anchor matches only the new key, so nothing but
        # the pairing check can reject it.
        mod.QUESTIONS[0]["ans"] = 1
        cl[0] = ("decreases by an amount equal to the energy of the photon", cl[0][1])
        pairing_never_swapped(mod)

    def decrease_keyed_to_absorption(mod, cl):
        # The same swap read the other way: an atom that LOST energy keyed to
        # having absorbed a photon.
        mod.QUESTIONS[23]["ans"] = 1
        cl[23] = ("Absorbed", cl[23][1])
        pairing_never_swapped(mod)

    def nothing_left_to_pair(mod, cl):
        # A control on the pairing check's own coverage, not on a key. If the
        # process words are edited out of the stems, every item falls through
        # the "no single pairing is asserted" branch and the check would pass
        # while reading almost nothing. The count assertion must fire instead.
        # All seven readable items have to be neutralised for this to reach
        # that branch, so all seven are done here.
        for idx, was, now in ((0, "absorbs", "receives"), (1, "emits", "gives out"),
                              (10, "absorbs", "receives"), (11, "emits", "gives out"),
                              (26, "Absorbing", "Taking in"),
                              (27, "absorbs", "takes in")):
            mod.QUESTIONS[idx]["q"] = mod.QUESTIONS[idx]["q"].replace(was, now)
        ch = list(mod.QUESTIONS[23]["choices"])
        ch[0] = "Given out"
        mod.QUESTIONS[23]["choices"] = ch
        cl[23] = ("Given out", cl[23][1])
        pairing_never_swapped(mod)

    def equation_key_moved(mod, cl):
        mod.QUESTIONS[2]["ans"] = 3
        cl[2] = ("\\lambda = c \\nu", cl[2][1])
        framework_equations(mod)

    def framework_equation_offered_twice(mod, cl):
        ch = list(mod.QUESTIONS[3]["choices"])
        ch[3] = "\\( c = \\lambda \\nu \\)"
        mod.QUESTIONS[3]["choices"] = ch
        framework_equations(mod)

    def stem_wavelength_edited(mod, cl):
        # The stem's wavelength changed under an untouched key, so the keyed
        # frequency no longer follows from the numbers the student is given.
        mod.QUESTIONS[7]["q"] = mod.QUESTIONS[7]["q"].replace(
            "6.00 \\times 10^{-7}", "4.00 \\times 10^{-7}")

    def numeric_key_moved(mod, cl):
        # The key moved onto the sign-flipped exponent, which is the mistake
        # this family of item exists to test.
        mod.QUESTIONS[8]["ans"] = 1
        cl[8] = ("3.31 \\times 10^{19}", cl[8][1])

    def mistaken_route_distractor_removed(mod, cl):
        # The distractor carrying a recomputed wrong route replaced by an
        # unrelated number. The key is still right and every choice still
        # distinct; the item has simply stopped testing that error.
        ch = list(mod.QUESTIONS[8]["choices"])
        ch[2] = "\\( 8.00 \\times 10^{-30} \\) J"
        mod.QUESTIONS[8]["choices"] = ch

    def partial_transfer_keyed(mod, cl):
        # EK 3.12.A.1 says EQUAL. The key moved to the half-transfer choice.
        mod.QUESTIONS[10]["ans"] = 2
        cl[10] = ("increases by \\( 2.0 \\times 10^{-19} \\) joules", cl[10][1])

    def reversal_distractor_removed(mod, cl):
        # The distractor stating the SAME magnitude with the opposite direction
        # replaced by a different number. The key is still right and every
        # choice still distinct -- the item has simply stopped testing the one
        # reversal EK 3.12.A.1's parenthesis invites.
        ch = list(mod.QUESTIONS[10]["choices"])
        ch[1] = "It decreases by \\( 7.0 \\times 10^{-19} \\) joules"
        mod.QUESTIONS[10]["choices"] = ch

    def proportional_key_moved(mod, cl):
        mod.QUESTIONS[4]["ans"] = 2
        cl[4] = ("It quadruples", cl[4][1])

    def stem_wavelengths_swapped(mod, cl):
        # 400 and 800 exchanged in the stem, so the key now names the LONGER
        # wavelength as the one carrying twice the energy.
        mod.QUESTIONS[24]["q"] = mod.QUESTIONS[24]["q"].replace(
            "400 nm and 800 nm", "800 nm and 400 nm").replace(
            "wavelengths of 800", "wavelengths of 800")
        ch = list(mod.QUESTIONS[24]["choices"])
        ch[0] = "The 800 nm photon carries twice the energy"
        ch[1] = "The 400 nm photon carries twice the energy"
        mod.QUESTIONS[24]["choices"] = ch
        cl[24] = ("800 nm photon carries twice the energy", cl[24][1])

    def tabulated_frequency_moved(mod, cl):
        mod.QUESTIONS[12]["table"] = dict(
            headers=h3_12._T_FREQ["headers"],
            rows=[["Photon 1", "9.0"], ["Photon 2", "6.0"], ["Photon 3", "4.0"]])

    def tabulated_wavelengths_permuted(mod, cl):
        mod.QUESTIONS[13]["table"] = dict(
            headers=h3_12._T_WAVE["headers"],
            rows=[["Photon J", "6.0"], ["Photon K", "2.0"], ["Photon L", "3.0"]])

    def tabulated_minimum_tied(mod, cl):
        # Two rows given the same longest wavelength, so the least-energy photon
        # is no longer unique and the item has two defensible answers.
        mod.QUESTIONS[14]["table"] = dict(
            headers=h3_12._T_WAVE["headers"],
            rows=[["Photon J", "2.0"], ["Photon K", "6.0"], ["Photon L", "6.0"]])

    def header_power_of_ten_changed(mod, cl):
        # Only the column header edited. The row values are untouched, so
        # nothing looks wrong until the scale is read from the header.
        mod.QUESTIONS[15]["table"] = dict(
            headers=["Photon", "Wavelength (in units of \\( 10^{-6} \\) metres)"],
            rows=list(h3_12._T_WAVE["rows"]))

    def tabulated_energy_moved(mod, cl):
        mod.QUESTIONS[26]["table"] = dict(
            headers=h3_12._T_ENERGY["headers"],
            rows=[["Photon P", "9.0"], ["Photon Q", "5.0"], ["Photon R", "3.0"]])

    def tabulated_row_changed_under_a_key(mod, cl):
        mod.QUESTIONS[27]["table"] = dict(
            headers=h3_12._T_ENERGY["headers"],
            rows=[["Photon P", "2.0"], ["Photon Q", "5.0"], ["Photon R", "4.0"]])

    return [
        ("a stem referring to a graph the bank cannot show", figure_language),
        ("3.13's Beer-Lambert law creeping into a stem", beer_lambert_creeps_in),
        ("3.11's spectral regions creeping into a key", spectral_region_creeps_in),
        ("an absorption keyed to a decrease in the atom's energy",
         absorption_keyed_to_a_decrease),
        ("an observed decrease keyed to an absorbed photon", decrease_keyed_to_absorption),
        ("every process word edited out, so the pairing check reads nothing",
         nothing_left_to_pair),
        ("an equation item keyed to a rearrangement of the framework's equation",
         equation_key_moved),
        ("a framework equation offered as a distractor as well as the key",
         framework_equation_offered_twice),
        ("a stem's wavelength edited under an untouched keyed frequency",
         stem_wavelength_edited),
        ("a numeric key moved onto the sign-flipped exponent", numeric_key_moved),
        ("the distractor carrying a recomputed wrong route replaced",
         mistaken_route_distractor_removed),
        ("a partial transfer keyed, against EK 3.12.A.1's word EQUAL",
         partial_transfer_keyed),
        ("the reversed-direction distractor replaced, so the item stops testing the swap",
         reversal_distractor_removed),
        ("a proportional-reasoning key moved off the recomputed factor",
         proportional_key_moved),
        ("the two wavelengths exchanged in a stem, so the key names the longer one",
         stem_wavelengths_swapped),
        ("a tabulated frequency raised so the greatest-energy photon moves",
         tabulated_frequency_moved),
        ("the tabulated wavelengths permuted", tabulated_wavelengths_permuted),
        ("two tabulated wavelengths tied at the longest", tabulated_minimum_tied),
        ("the power of ten in a column header changed", header_power_of_ten_changed),
        ("a tabulated photon energy raised so the largest increase moves",
         tabulated_energy_moved),
        ("a tabulated row edited under a keyed energy", tabulated_row_changed_under_a_key),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h3_12, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h3_12)
no_other_topic(h3_12)
pairing_never_swapped(h3_12)
framework_equations(h3_12)
h.run(h3_12, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
