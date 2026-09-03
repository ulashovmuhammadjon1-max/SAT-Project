"""Negative control for the AP Biology unit 5 to 7 verifiers written here.

SCIENCE_BRIEF.md: "Run a negative control on every check you write. Corrupt a key
or a figure on purpose and confirm the check fails. A checker that cannot fail is
worse than none -- it has cost this project five separate times."

So this file breaks each module on purpose and asserts the verifier notices.

Two sweeps per module:

1. KEY ROTATION. Every question in turn has its ``ans`` moved to the next
   choice. The verifier must raise for all thirty, because every key is pinned
   to an anchor that appears in the keyed choice and in no distractor. A pass
   here would mean the anchors were generic enough to match a distractor, which
   is the failure mode a bare index would have.

2. TABLE CORRUPTION. Every cell of every table is altered in turn -- numbers
   scaled, text replaced -- and the run is recorded as caught or not caught. Not
   every cell edit can be caught, and pretending otherwise would be the same
   dishonesty this control exists to prevent: a cell no keyed choice depends on
   is a cell whose value does not change the answer. What IS required is that
   each table is defended at all (at least one caught corruption) and that the
   per-table catch rate is printed, so a table check that has quietly stopped
   reading its table shows up as a row of zeros.

Run: ``python3 negcontrol_b5_7.py``            (all finished modules)
     ``python3 negcontrol_b5_7.py b5_3 b6_2``  (named modules)
"""
import contextlib
import copy
import importlib
import io
import os
import re
import sys

TOPICS = ["5_3", "5_4", "5_5",
          "6_1", "6_2", "6_3", "6_4", "6_5", "6_6", "6_7", "6_8",
          "7_1", "7_2", "7_3", "7_4"]


def _run_verifier(vname):
    """Import or re-execute the verifier. Returns None on pass, the error on fail."""
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            if vname in sys.modules:
                importlib.reload(sys.modules[vname])
            else:
                importlib.import_module(vname)
    except AssertionError as exc:
        return exc
    except Exception as exc:  # a KeyError or ValueError from a corrupted cell counts
        return exc
    return None


def _corrupt_cell(value):
    """Change a cell so that any check reading it must see something different."""
    if re.fullmatch(r"-?[\d,]+(?:\.\d+)?", str(value).strip()):
        n = float(str(value).replace(",", ""))
        return str(int(n * 2) + 7) if n == int(n) else str(n * 2 + 7)
    text = str(value)
    swaps = {"Affected": "Unaffected", "Unaffected": "Affected",
             "Male": "Female", "Female": "Male"}
    if text in swaps:
        return swaps[text]
    return text + " CORRUPTED"


def check_module(stem):
    mod_name, ver_name = f"b{stem}", f"verify_b{stem}"
    mod = importlib.import_module(mod_name)
    pristine = copy.deepcopy(mod.QUESTIONS)

    baseline = _run_verifier(ver_name)
    assert baseline is None, f"{ver_name} does not pass before corruption: {baseline}"

    # --- sweep 1: rotate every key
    missed = []
    for i in range(len(mod.QUESTIONS)):
        mod.QUESTIONS[:] = copy.deepcopy(pristine)
        item = mod.QUESTIONS[i]
        item["ans"] = (item["ans"] + 1) % len(item["choices"])
        if _run_verifier(ver_name) is None:
            missed.append(i + 1)
    mod.QUESTIONS[:] = copy.deepcopy(pristine)
    assert not missed, f"{mod_name}: key rotation NOT caught for q{missed}"

    # --- sweep 2: corrupt every table cell
    table_rows = []
    for i, item in enumerate(pristine, 1):
        if not item.get("table"):
            continue
        caught = total = 0
        for r in range(len(item["table"]["rows"])):
            for c in range(len(item["table"]["headers"])):
                mod.QUESTIONS[:] = copy.deepcopy(pristine)
                tab = mod.QUESTIONS[i - 1]["table"]
                tab["rows"][r][c] = _corrupt_cell(tab["rows"][r][c])
                total += 1
                if _run_verifier(ver_name) is not None:
                    caught += 1
        table_rows.append((i, caught, total))
    mod.QUESTIONS[:] = copy.deepcopy(pristine)
    assert _run_verifier(ver_name) is None, f"{ver_name} left broken after the sweep"

    for i, caught, total in table_rows:
        assert caught, (
            f"{mod_name} q{i}: NO corruption of its table was caught -- "
            "the table check is not reading the table"
        )
    detail = ", ".join(f"q{i} {c} of {t}" for i, c, t in table_rows) or "no tables"
    print(f"OK  {mod_name}: {len(pristine)} key rotations all caught; "
          f"table cells caught: {detail}")


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    wanted = [a.replace("b", "", 1) if a.startswith("b") else a for a in sys.argv[1:]]
    stems = wanted or [t for t in TOPICS
                       if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                      f"verify_b{t}.py"))]
    for stem in stems:
        check_module(stem)
    print(f"negative control passed for {len(stems)} module(s)")
