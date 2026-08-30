"""Verification for AP STATISTICS 1.4, graphical displays of one categorical variable.

Counts are read back out of the module's own tables, so a table edited without
its keys will fail here. Both tables are first checked for internal consistency,
then every pie-chart central angle, proportion, percent and count keyed in the
module is recomputed as 360 * (count / total) or count / total as appropriate.

Several keys in this topic are category names or sentences rather than numbers,
so they cannot go through ``Checker.check``. Their arithmetic is still computed
in ``prose_arithmetic`` below and asserted -- including the two comparisons that
make this topic worth teaching: that Hip-hop is the *unique* genre with matching
relative frequencies, and that Pop has the larger count at School Q while having
the larger share at School P.

Run: python3 verify_s1_4.py
"""
import s_verify_util as U

import s1_4

c = U.Checker(s1_4)


def counts(table, col=1):
    out = {}
    for row in table["rows"]:
        if row[0].lower() == "total":
            continue
        out[row[0]] = int(row[col])
    return out


def total(table, col=1):
    for row in table["rows"]:
        if row[0].lower() == "total":
            return int(row[col])
    raise AssertionError("table has no Total row")


D = s1_4.TABLE_D
E = s1_4.TABLE_E
d, nD = counts(D), total(D)
p, nP = counts(E, 1), total(E, 1)
q, nQ = counts(E, 2), total(E, 2)

assert sum(d.values()) == nD, f"table D sums to {sum(d.values())}, total says {nD}"
assert sum(p.values()) == nP, f"School P sums to {sum(p.values())}, total says {nP}"
assert sum(q.values()) == nQ, f"School Q sums to {sum(q.values())}, total says {nQ}"


def angle(count, n):
    """Central angle in degrees of a pie slice holding `count` of `n` units."""
    return count / n * 360.0


# --- computed keys -----------------------------------------------------------
c.check(5, d["Dog"] / nD)                     # 210/500 = 0.42
c.check(6, angle(d["Dog"], nD))               # 0.42 * 360 = 151.2 degrees
c.check(7, angle(d["Fish"], nD))              # 0.12 * 360 =  43.2 degrees
c.check(9, 0.25 * 360)                        # a quarter of the circle = 90 degrees
c.check(10, 72 / 360)                         # 72 degrees is a share of 0.20
c.check(11, d["Cat"] + d["Fish"])             # 150 + 60 = 210 households
c.check(14, d["None"] / nD * 100)             # 50/500 = 10%
c.check(23, angle(q["Rock"], nQ))             # 250/1000 * 360 = 90 degrees


def prose_arithmetic():
    """The arithmetic behind the keys that are category names or sentences."""
    # q8: a 36-degree slice is a share of 0.10; exactly one category matches.
    share = 36 / 360
    matches = [k for k, v in d.items() if abs(v / nD - share) < 1e-12]
    assert matches == ["None"], f"q8: a 36-degree slice matches {matches}, key says None"

    # q12: the tallest bar is the largest count, and it is unique.
    biggest = max(d.values())
    tallest = [k for k, v in d.items() if v == biggest]
    assert tallest == ["Dog"], f"q12: tallest bar is {tallest}, key says Dog"

    # q15: exactly one genre has matching relative frequencies in the two schools.
    same = [g for g in p if abs(p[g] / nP - q[g] / nQ) < 1e-12]
    assert same == ["Hip-hop"], f"q15: genres with equal shares are {same}, key says Hip-hop"
    assert abs(p["Hip-hop"] / nP - 0.30) < 1e-12 and abs(q["Hip-hop"] / nQ - 0.30) < 1e-12

    # q16: Rock's share is larger at School Q.
    rock_p, rock_q = p["Rock"] / nP, q["Rock"] / nQ
    assert (rock_p, rock_q) == (0.20, 0.25), f"q16: Rock shares are {rock_p}, {rock_q}"
    assert rock_q > rock_p, "q16: the key says Rock is proportionally more popular at School Q"

    # q17: the counts-versus-proportions trap. Q has more Pop listeners, P has
    # the larger Pop share. Both halves are asserted, since the distractors
    # differ only in which half they get right.
    assert q["Pop"] > p["Pop"], "q17: School Q must have the larger Pop count"
    pop_p, pop_q = p["Pop"] / nP, q["Pop"] / nQ
    assert pop_p > pop_q, "q17: School P must have the larger Pop share"
    assert (pop_p, pop_q) == (0.39, 0.35), f"q17: Pop shares are {pop_p}, {pop_q}"

    # q21: the labelled slices must not sum to 100%.
    assert 30 + 25 + 25 + 25 == 105, "q21: the four labelled percentages total 105"

    # q22: dogs exactly equal cats plus fish, so 'more than' is false.
    assert d["Dog"] == d["Cat"] + d["Fish"] == 210, (
        f"q22: Dog {d['Dog']} vs Cat+Fish {d['Cat'] + d['Fish']}")

    # q25: a difference of shares, not of counts.
    assert abs((0.35 - 0.15) - 0.20) < 1e-12, "q25: 0.35 - 0.15 = 0.20"

    # q13: dividing every count by the same total is a single rescaling, so the
    # ordering of the bars is preserved exactly.
    by_count = sorted(d, key=lambda k: d[k])
    by_share = sorted(d, key=lambda k: d[k] / nD)
    assert by_count == by_share, "q13: relative frequency must preserve the bar ordering"


prose_arithmetic()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 1.4.A.1: each bar represents one category and its height is that category's frequency or relative frequency.")
c.conceptual(2, "EK 1.4.A.2: a slice's area as a fraction of the total area is that category's relative frequency.")
c.conceptual(3, "EK 1.4.A.2: the slices' areas together equal 1, or 100% of the total area.")
c.conceptual(4, "EK 1.4.A.1: a bar chart's scale may show either counts or proportions.")
c.conceptual(8, "EK 1.4.A.2: computed above, a 36-degree slice is a share of 0.10 and only 'None' (50 of 500) matches.")
c.conceptual(12, "EK 1.4.A.1: computed above, Dog has the unique largest count, 210, so its bar is tallest.")
c.conceptual(13, "EK 1.4.A.1: computed above, dividing every count by the same total preserves the ordering and relative heights of the bars.")
c.conceptual(15, "EK 1.4.C.1: computed above, Hip-hop is the only genre whose relative frequency, 0.30, is the same in both schools.")
c.conceptual(16, "EK 1.4.C.1: computed above, Rock's share is 0.20 at P and 0.25 at Q, so it is proportionally more popular at Q.")
c.conceptual(17, "EK 1.4.C.1: computed above, Q has the larger Pop count (350 vs 156) but P the larger Pop share (0.39 vs 0.35).")
c.conceptual(18, "EK 1.4.C.1: with enrolments of 400 and 1000, only relative frequencies put the two distributions on a comparable scale.")
c.conceptual(19, "EK 1.4.A.2: a pie chart displays how one categorical variable divides a single whole, and needs few categories to stay readable.")
c.conceptual(20, "EK 1.4.A.1: categories are distinct labels rather than adjoining intervals, which is why the bars are drawn separated.")
c.conceptual(21, "EK 1.4.A.2: computed above, the labelled slices total 105%, but a pie chart's slices must total 100%.")
c.conceptual(22, "EK 1.4.B.1: computed above, Cat + Fish = 210 exactly equals the Dog count, so the 'more than' claim fails.")
c.conceptual(24, "EK 1.4.A.1: a categorical variable's categories carry no inherent order, so reordering the axis changes no bar height.")
c.conceptual(25, "EK 1.4.A.1: computed above, bars on a relative frequency chart give shares, so 0.35 - 0.15 = 0.20 is a difference of proportions and no count can be read off.")

c.finish()
