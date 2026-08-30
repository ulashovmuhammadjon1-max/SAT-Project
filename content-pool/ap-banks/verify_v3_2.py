"""Structural audit for AP U.S. Government 3.2 First Amendment: Freedom of Religion.

Shared checks in gov345_check.py. The two additions here are the arithmetic
behind the school prayer survey used by items 15 and 16, recomputed from the
table's own cells:

    q15  silent individual prayer is the single most supported practice
    q16  the practices the SCHOOL DIRECTS draw less support than the ones it
         merely permits -- the sorting variable the key names

q16 is the item worth guarding, because its key asserts a relationship between
two groups of rows rather than a single largest number. The function below
splits the five rows into school-directed and not-school-directed and checks
that the two groups do not overlap at all, so the claim "support falls as the
school's own role grows" cannot survive an edit that muddies the split.
"""
import gov345_check as gc
import v3_2

DIRECTED = {"A teacher leading the class in prayer",
            "A prayer written by the school board and recited daily"}


def _support(t):
    return {row[0]: gc.num(row[1]) for row in t["rows"]}


def q15(t):
    s = _support(t)
    for row in t["rows"]:
        assert gc.num(row[1]) + gc.num(row[2]) == 100, f"row {row[0]} does not total 100"
    top = max(s, key=s.get)
    assert top == "A student praying silently on her own", f"highest support is {top}"
    runner = max(v for k, v in s.items() if k != top)
    return (f"highest support {s[top]:.0f} percent for '{top}', "
            f"{s[top] - runner:.0f} points above the next practice; every row totals 100")


def q16(t):
    s = _support(t)
    assert DIRECTED <= set(s), "the school-directed rows are not both present"
    directed = [v for k, v in s.items() if k in DIRECTED]
    permitted = [v for k, v in s.items() if k not in DIRECTED]
    assert len(directed) == 2 and len(permitted) == 3, "the split is not two against three"
    assert max(directed) < min(permitted), (
        f"the groups overlap: directed up to {max(directed)}, permitted down to {min(permitted)}"
    )
    return (f"school-directed practices {sorted(directed)} all fall below the "
            f"permitted ones {sorted(permitted)}; the groups do not overlap")


gc.check(v3_2, arith={15: q15, 16: q16})
