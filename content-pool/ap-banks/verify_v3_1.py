"""Structural audit for AP U.S. Government 3.1 The Bill of Rights.

The politics is not checkable by a script; see gov345_check.py for what is and
what that leaves to a human reader. What this file adds on top of the shared
checks is the arithmetic behind the two data stimulus items, recomputed from the
table rather than trusted from the prose.

Items 21 and 22 share one survey table, which is how the real exam builds a
quantitative set. The keyed claims are:

    q21  the gun ownership row has the largest gap between the two columns
    q22  four rows agree within a few points and one does not

Both are recomputed below from the table's own cells, so an edit to any figure
that broke either claim would fail this file rather than reach a student.
"""
import gov345_check as gc
import v3_1


def q21(t):
    """The largest owner / non-owner gap must be the firearms row."""
    gaps = {row[0]: abs(gc.num(row[1]) - gc.num(row[2])) for row in t["rows"]}
    biggest = max(gaps, key=gaps.get)
    assert biggest == "The right to own guns", f"largest gap is {biggest}"
    others = [g for k, g in gaps.items() if k != biggest]
    assert gaps[biggest] >= 5 * max(others), (
        f"the firearms gap {gaps[biggest]} is not decisively larger than {max(others)}"
    )
    return (f"largest gap {gaps[biggest]:.0f} points on '{biggest}'; "
            f"every other row within {max(others):.0f} points")


def q22(t):
    """Four rows near-agreement above 70 percent, one row far apart."""
    near, far = [], []
    for row in t["rows"]:
        a, b = gc.num(row[1]), gc.num(row[2])
        (far if abs(a - b) > 10 else near).append((row[0], a, b))
    assert len(near) == 4 and len(far) == 1, f"{len(near)} close rows, {len(far)} far"
    assert all(min(a, b) > 70 for _, a, b in near), "a close row falls below 70 percent"
    assert far[0][0] == "The right to own guns", f"the outlier row is {far[0][0]}"
    return (f"{len(near)} rows agree within 10 points and all exceed 70 percent; "
            f"the outlier is '{far[0][0]}' at {abs(far[0][1] - far[0][2]):.0f} points")


gc.check(v3_1, arith={21: q21, 22: q22})
