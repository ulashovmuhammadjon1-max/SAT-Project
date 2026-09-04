"""Thermochemical arithmetic and SIGN bookkeeping for the AP CHEMISTRY unit 6 banks.

Unit 6 is the arithmetic-heavy unit of the course, and in almost every item the
answer turns on a SIGN rather than on a magnitude. An exothermic process has a
negative enthalpy change; reversing a step in Hess's law flips the sign; bond
energy is a cost on the way in and a refund on the way out. Getting one of those
backwards produces a number that looks right and teaches a student the opposite
of the truth, so every unit 6 verifier recomputes its arithmetic through this
module rather than each writing its own.

THE SHAPE OF EVERY FUNCTION HERE IS A DELIBERATE RESPONSE TO A REAL BUG. A
verifier in this project rejected a CORRECT key because the check itself was
inverted: it built one tuple ordered (acid, base) and another ordered (base,
acid) and compared index 0 against index 0 as though they were parallel. An
endothermic/exothermic guard has exactly that shape. So nothing here returns a
pair to be read by position. ``direction`` returns a record with NAMED fields,
``agrees`` compares two named booleans, and the words are module constants
rather than literals retyped at each call site.

WHAT EACH PIECE COMPUTES, and the framework sentence it serves:

  ``heat``                EK 6.4.A.1's EQN, q = mc(delta T), with the sign of
                          the temperature change carried through
  ``phase_heat``          EK 6.5.A.1: moles times the molar enthalpy of the
                          transition
  ``reaction_heat``       EK 6.6.A.1: moles of reaction times the molar
                          enthalpy of reaction
  ``bond_enthalpy``       EK 6.7.A.2: energy required to break the reactant
                          bonds minus energy released forming the product bonds
  ``formation_enthalpy``  EK 6.8.A.1's EQN, sum over products minus sum over
                          reactants
  ``hess_sum``            EK 6.9.B.2: reverse a step and its enthalpy changes
                          sign, multiply a step by c and its enthalpy is
                          multiplied by c, add the steps and add the enthalpies

NO ``\\b`` ANYWHERE. A digit and a letter are both word characters, so ``\\b``
is silently not a boundary exactly where it looks like one -- this project has
paid for that five separate times. Every phrase match here uses explicit
lookarounds.

``selftest()`` is the negative control for this module itself, and it is what
makes a passing unit 6 verifier mean anything: it runs values known to be right
AND values corrupted on purpose, and fails if a corrupted one is accepted.
"""
import re

EXOTHERMIC = "exothermic"
ENDOTHERMIC = "endothermic"

_EXO = re.compile(r"(?<![A-Za-z0-9])exothermic(?![A-Za-z0-9])", re.I)
_ENDO = re.compile(r"(?<![A-Za-z0-9])endothermic(?![A-Za-z0-9])", re.I)
# The macroscopic pair EK 6.1.A.3 and EK 6.6.A.2 use for the same distinction.
# "released" is the exothermic word and "absorbed" the endothermic one.
_RELEASED = re.compile(
    r"(?<![A-Za-z0-9])(?:released|gives off|lost by the system)(?![A-Za-z0-9])", re.I)
_ABSORBED = re.compile(
    r"(?<![A-Za-z0-9])(?:absorbed|taken in|gained by the system)(?![A-Za-z0-9])", re.I)


# ------------------------------------------------------------------ arithmetic

def heat(mass_g, specific_heat, delta_t):
    """EK 6.4.A.1: q = mc(delta T), in joules, with the sign of delta T kept.

    A positive result is energy absorbed BY the substance being heated. The
    caller decides whose books that lands on -- reversing it for the reaction
    inside a calorimeter is EK 6.4.A.2's conservation step, and it is written
    out at each call site rather than hidden in here, because that reversal is
    the single sign most often dropped.
    """
    return mass_g * specific_heat * delta_t


def phase_heat(moles, molar_enthalpy):
    """EK 6.5.A.1: energy for a phase transition, moles times molar enthalpy."""
    return moles * molar_enthalpy


def reaction_heat(moles_of_reaction, molar_enthalpy):
    """EK 6.6.A.1: energy for a reaction, moles of reaction times molar enthalpy."""
    return moles_of_reaction * molar_enthalpy


def opposite(molar_enthalpy):
    """EK 6.5.A.2: a complementary phase change has the enthalpy negated."""
    return -molar_enthalpy


def bond_enthalpy(broken, formed):
    """EK 6.7.A.2: energy required to break reactant bonds, minus energy released.

    ``broken`` and ``formed`` are sequences of ``(count, average bond energy)``.
    Bond energies are positive quantities -- breaking costs and forming refunds
    -- so the subtraction, not a stored sign, is what makes an exothermic
    reaction come out negative.
    """
    required = sum(n * e for n, e in broken)
    released = sum(n * e for n, e in formed)
    assert required >= 0 and released >= 0, (
        f"average bond energies are positive quantities: broken {broken}, formed {formed}"
    )
    return required - released


def formation_enthalpy(products, reactants):
    """EK 6.8.A.1's EQN: sum over the products minus sum over the reactants.

    Each sequence holds ``(coefficient, standard enthalpy of formation)``.
    """
    return (sum(n * h for n, h in products) - sum(n * h for n, h in reactants))


def hess_step(molar_enthalpy, factor=1, reversed_=False):
    """EK 6.9.B.2 i and ii: one step scaled by c, and reversed if asked.

    ``reversed_`` is a named argument on purpose. A caller passing a negative
    ``factor`` to mean "reversed" works out to the same number, but it hides
    which of the framework's two rules is being applied, and the two are
    separately examinable.
    """
    assert factor > 0, (
        "EK 6.9.B.2 ii multiplies a reaction by a factor c; a reversal is the separate "
        "rule i and must be asked for by name"
    )
    scaled = factor * molar_enthalpy
    return -scaled if reversed_ else scaled


def hess_sum(steps):
    """EK 6.9.B.2 iii: the overall enthalpy is the sum of the steps' enthalpies.

    ``steps`` is a sequence of ``(molar enthalpy, factor, reversed)`` triples.
    """
    return sum(hess_step(h, factor=f, reversed_=r) for h, f, r in steps)


# --------------------------------------------------------------- sign bookkeeping

def direction(delta_h):
    """Which way the energy went, as a record with NAMED fields.

    Never a pair to be read by position. The inverted check this project
    already shipped compared index 0 of one tuple against index 0 of another
    that was ordered the other way, and rejected a correct key.
    """
    return dict(exothermic=delta_h < 0,
                endothermic=delta_h > 0,
                neither=delta_h == 0)


def word(delta_h):
    """The framework's word for the sign of ``delta_h``, or None at zero."""
    d = direction(delta_h)
    if d["exothermic"]:
        return EXOTHERMIC
    if d["endothermic"]:
        return ENDOTHERMIC
    return None


def stated_direction(text):
    """Which of the two words a piece of text states, or None.

    None when the text states NEITHER word and also when it states BOTH: a
    choice naming both leaves the direction ambiguous, and an anchor pinned to
    it would match a key that had the sign backwards. Returning None makes the
    caller handle that case rather than silently picking the first match.
    """
    exo, endo = bool(_EXO.search(text)), bool(_ENDO.search(text))
    if exo and not endo:
        return EXOTHERMIC
    if endo and not exo:
        return ENDOTHERMIC
    return None


def stated_transfer(text):
    """The macroscopic pair: released is exothermic, absorbed is endothermic.

    Same rule as ``stated_direction`` -- None when both or neither appears.
    """
    rel, abso = bool(_RELEASED.search(text)), bool(_ABSORBED.search(text))
    if rel and not abso:
        return EXOTHERMIC
    if abso and not rel:
        return ENDOTHERMIC
    return None


def agrees(delta_h, text, transfer=False):
    """Does ``text`` name the direction that the SIGN of ``delta_h`` requires?

    Two named booleans compared, never two tuples indexed in parallel.
    """
    assert delta_h != 0, (
        "a thermoneutral value has no direction word, so nothing can agree or disagree "
        "with it; the caller must handle zero itself"
    )
    said = stated_transfer(text) if transfer else stated_direction(text)
    if said is None:
        return False
    value_is_exothermic = delta_h < 0
    text_says_exothermic = said == EXOTHERMIC
    return value_is_exothermic == text_says_exothermic


def report(delta_h, unit="kJ/mol"):
    """A sentence naming the number and its direction, for a check's return value."""
    w = word(delta_h)
    return (f"{delta_h:+g} {unit}, which is {w}" if w
            else f"{delta_h:g} {unit}, neither exothermic nor endothermic")


# ------------------------------------------------------------------- selftest

def selftest():
    """Positive AND negative controls for this module itself."""
    # q = mc(delta T), and the sign follows the temperature change.
    assert heat(100.0, 4.18, 10.0) == 4180.0, heat(100.0, 4.18, 10.0)
    assert heat(100.0, 4.18, -10.0) == -4180.0, heat(100.0, 4.18, -10.0)
    assert heat(50.0, 4.18, 10.0) == 2090.0, heat(50.0, 4.18, 10.0)
    # EK 6.4.A.3: the same energy into equal masses of different substances
    # gives different temperature changes. Stated as a computation, not assumed.
    dt_water = 1000.0 / (100.0 * 4.18)
    dt_iron = 1000.0 / (100.0 * 0.449)
    assert dt_iron > dt_water, (dt_iron, dt_water)

    assert phase_heat(2.0, 40.7) == 81.4, phase_heat(2.0, 40.7)
    assert opposite(40.7) == -40.7
    assert opposite(opposite(40.7)) == 40.7
    assert reaction_heat(0.5, -92.0) == -46.0, reaction_heat(0.5, -92.0)

    # EK 6.7.A.2, on the formation of ammonia from its elements:
    # break one N-N triple (946) and three H-H (436); form six N-H (391).
    dh = bond_enthalpy([(1, 946), (3, 436)], [(6, 391)])
    assert dh == 946 + 1308 - 2346 == -92, dh
    assert direction(dh)["exothermic"] and not direction(dh)["endothermic"]
    # NEGATIVE CONTROL: the subtraction the other way round is the classic
    # error, and it must not come out with the same sign.
    wrong = bond_enthalpy([(6, 391)], [(1, 946), (3, 436)])
    assert wrong == -dh and direction(wrong)["endothermic"], wrong

    # EK 6.8.A.1's EQN on the combustion of methane, with the elements' zeros
    # supplied explicitly, as a tabulated stimulus must.
    dh = formation_enthalpy([(1, -394), (2, -286)], [(1, -75), (2, 0)])
    assert dh == -394 - 572 + 75 == -891, dh
    # NEGATIVE CONTROL: reactants minus products is the same magnitude and the
    # WRONG sign, which is the whole defect this unit is exposed to.
    flipped = formation_enthalpy([(1, -75), (2, 0)], [(1, -394), (2, -286)])
    assert flipped == -dh and direction(flipped)["endothermic"], flipped

    # EK 6.9.B.2, all three rules.
    assert hess_step(-283, factor=2) == -566
    assert hess_step(-283, reversed_=True) == 283
    assert hess_step(-283, factor=2, reversed_=True) == 566
    assert hess_sum([(-394, 1, False), (-283, 1, True)]) == -394 + 283 == -111
    try:
        hess_step(-283, factor=-1)
    except AssertionError:
        pass
    else:
        raise AssertionError(
            "NEGATIVE CONTROL FAILED: a negative factor was accepted, which hides a "
            "reversal inside EK 6.9.B.2's scaling rule"
        )

    # The sign words.
    assert word(-92) == EXOTHERMIC and word(92) == ENDOTHERMIC and word(0) is None
    assert stated_direction("This process is exothermic") == EXOTHERMIC
    assert stated_direction("This process is endothermic") == ENDOTHERMIC
    assert stated_direction("Exothermic, not endothermic") is None, (
        "a text naming BOTH words must be refused, or an anchor pinned to it would "
        "match a key with the sign backwards"
    )
    assert stated_direction("The temperature rises") is None
    assert stated_transfer("Energy is released by the system") == EXOTHERMIC
    assert stated_transfer("Energy is absorbed by the system") == ENDOTHERMIC
    assert stated_transfer("Energy is released and absorbed in turn") is None

    assert agrees(-92, "The reaction is exothermic")
    assert not agrees(-92, "The reaction is endothermic"), (
        "NEGATIVE CONTROL FAILED: a negative enthalpy was allowed to be called endothermic"
    )
    assert agrees(92, "The reaction is endothermic")
    assert not agrees(92, "The reaction is exothermic"), (
        "NEGATIVE CONTROL FAILED: a positive enthalpy was allowed to be called exothermic"
    )
    assert agrees(-92, "energy is released to the surroundings", transfer=True)
    assert not agrees(-92, "energy is absorbed from the surroundings", transfer=True)
    assert not agrees(-92, "the temperature of the flask changes"), (
        "NEGATIVE CONTROL FAILED: a text stating no direction was allowed to agree"
    )
    try:
        agrees(0, "The reaction is exothermic")
    except AssertionError:
        pass
    else:
        raise AssertionError(
            "NEGATIVE CONTROL FAILED: a thermoneutral value was allowed a direction word"
        )

    # ``\b`` would break these. A digit abutting a letter is not a boundary.
    assert stated_direction("2exothermic4") is None, (
        "the lookarounds must not match a word run together with digits"
    )
    assert stated_direction("nonexothermic") is None

    print("OK  h6_thermo: q=mc(delta T), phase, reaction, bond, formation and Hess "
          "arithmetic checked against known values; the reversed subtraction, the "
          "hidden reversal, the both-words case and the wrong direction word all "
          "rejected.")


if __name__ == "__main__":
    selftest()
