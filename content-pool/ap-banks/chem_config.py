r"""Ground-state electron configurations, derived rather than recalled.

Shared by the AP Chemistry verifiers that key a configuration (1.5, 1.6, 1.7,
1.8). A configuration in a choice is a string, and a string is exactly what a
verifier cannot check -- so these helpers read the configuration back out of
its LaTeX span and rebuild the correct one from the electron count in the
Aufbau order EK 1.5.A.3 names. A keyed configuration is then compared against a
derivation instead of against the author's memory.

The filling order stops well short of the whole periodic table on purpose: the
CED excludes writing configurations for elements that are exceptions to the
Aufbau principle (exclusion statement at 1.7.A.1), and these banks stay inside
that boundary, so an order long enough to reach the exceptions would only
invite one to be written.
"""
import re

_SUBSHELL = re.compile(r"(\d)([spdf])\^\{?(\d+)\}?")

ORDER = [("1s", 2), ("2s", 2), ("2p", 6), ("3s", 2), ("3p", 6), ("4s", 2),
         ("3d", 10), ("4p", 6), ("5s", 2)]

CAPACITY = dict(ORDER)


def parse(text):
    """Every (subshell, electron count) in a configuration string, in order."""
    return [(f"{n}{l}", int(k)) for n, l, k in _SUBSHELL.findall(text)]


def total(text):
    return sum(k for _, k in parse(text))


def ground_state(n_electrons):
    """The ground-state configuration for n electrons, built in Aufbau order."""
    out, left = [], n_electrons
    for name, cap in ORDER:
        if left <= 0:
            break
        k = min(cap, left)
        out.append((name, k))
        left -= k
    assert left == 0, f"{n_electrons} electrons do not fit the filling order used here"
    return out


def assert_ground(text, n_electrons, where):
    """Fail unless ``text`` is exactly the ground state for n electrons."""
    got, want = parse(text), ground_state(n_electrons)
    assert got == want, (
        f"{where}: the keyed configuration {got} is not the ground state for "
        f"{n_electrons} electrons, which is {want}")
    return want


def is_ground(text):
    """True if the configuration is the ground state for its own electron count."""
    got = parse(text)
    if not got:
        return False
    try:
        return got == ground_state(total(text))
    except AssertionError:
        return False


def from_peak_heights(heights, where=""):
    """Assign PES peak heights, ordered from the HIGHEST binding energy down, to
    subshells in Aufbau order -- the reading EK 1.6.A.1 licenses.

    Returns the configuration as a list of (subshell, count). Raises if any
    height exceeds the subshell's capacity, which would make the spectrum
    describe no possible atom.
    """
    out = []
    for i, h in enumerate(heights):
        assert i < len(ORDER), f"{where}: more peaks than the filling order covers"
        name, cap = ORDER[i]
        n = int(round(h))
        assert abs(h - n) < 1e-9, f"{where}: peak height {h} is not a whole number of electrons"
        assert 1 <= n <= cap, f"{where}: {n} electrons will not fit subshell {name} (capacity {cap})"
        out.append((name, n))
    return out


def _selftest():
    """A gate that cannot fail is worse than none."""
    assert ground_state(11) == [("1s", 2), ("2s", 2), ("2p", 6), ("3s", 1)]
    assert is_ground(r"\(1s^2\,2s^2\,2p^6\,3s^1\)")
    assert not is_ground(r"\(1s^2\,2s^2\,2p^5\,3s^1\)"), \
        "CONTROL FAILED: a configuration skipping a 2p vacancy passed as a ground state"
    assert not is_ground(r"\(1s^2\,2s^1\,2p^2\)"), \
        "CONTROL FAILED: an excited boron configuration passed as a ground state"
    assert total(r"\(1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,4s^2\,3d^6\)") == 26
    assert from_peak_heights([2, 2, 6, 1]) == [("1s", 2), ("2s", 2), ("2p", 6), ("3s", 1)]
    for bad, why in (([2, 2, 7], "a 2p subshell over capacity"),
                     ([2, 2, 6, 3], "a 3s subshell over capacity"),
                     ([3, 2], "a 1s subshell over capacity")):
        try:
            from_peak_heights(bad)
        except AssertionError:
            continue
        raise SystemExit(f"CONTROL FAILED: {why} was accepted -- {bad}")
    try:
        assert_ground(r"\(1s^2\,2s^2\,2p^6\)", 11, "control")
    except AssertionError:
        print("chem_config: all controls behaved as required.")
        return
    raise SystemExit("CONTROL FAILED: a ten-electron configuration passed as eleven")


if __name__ == "__main__":
    _selftest()
