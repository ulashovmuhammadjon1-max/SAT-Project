"""Key audit for AP ENVIRONMENTAL SCIENCE 1.1 Introduction to Ecosystems.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

The structural gate is shared with the other banks (``cg_check.py``). It cannot
tell whether the environmental science is right; that is gated by the CLAIMS
text and by the rule in SCIENCE_BRIEF.md that every key traces to a sentence in
the CED.

WHAT THE KEYS REST ON
---------------------
Items 1, 11, 19 and 30 rest on ERT-1.A.1: in a predator-prey relationship the
predator is an organism that eats another organism (the prey).

Items 2, 9, 10, 11, 16, 21, 23, 24 and 28 rest on ERT-1.A.2: symbiosis is a
close and long-term interaction between two species, and types of symbiosis
include mutualism, commensalism and parasitism. Where an item turns on WHICH of
the three (9, 10, 23, 24), the key rests only on the minimum that naming them as
distinct types requires -- mutualism benefits both, commensalism benefits one
while the other is unaffected, parasitism benefits one at the other's expense.

Items 3, 4, 5, 6, 7, 8, 13, 14, 15, 17, 18, 20, 22, 25, 26, 27 and 29 rest on
ERT-1.A.3: competition can occur within or between species where there are
limited resources, and resource partitioning -- using the resources in different
ways, places, or at different times -- can reduce the negative impact of
competition on survival. No item claims partitioning abolishes competition.

DATA ITEMS: 5, 6, 7, 12, 14, 18, 22, 23, 24 and 26 carry tables. Each keyed
conclusion is recomputed below from that table alone, and each check also
falsifies the distractors against the same numbers.

NEGATIVE CONTROL: ``python3 verify_e1_1.py --selftest`` corrupts a key, an
anchor, a table cell and the notation on purpose and confirms each check fires.
"""
import re
import sys

import cg_check as cg

# SCIENCE_BRIEF.md: Environmental Science is exported as prose. export_units.py does
# not typeset it, so a backslash macro would reach a student as literal text, and a
# digit-hyphen-digit range is what the converter mangled on the prose subjects.
# Explicit lookarounds, never \b beside a digit.
_BANNED = [
    (re.compile(r"\\"), "a backslash: this subject is not typeset, so LaTeX prints raw"),
    (re.compile(r"(?<![A-Za-z])\d+\s?-\s?\d"), "a digit-hyphen-digit range: write 'to' instead"),
    (re.compile(r"\d\s?/\s?\d"), "a digit-slash-digit fraction: write it out in words"),
    (re.compile(r"\^"), "a bare caret, which prints raw outside a math span"),
    (re.compile(r"\$"), "a dollar sign, which the converter reads as inline math"),
]


def style(module):
    """No typeset notation anywhere in the module's student-facing text."""
    for i, item in enumerate(module.QUESTIONS, 1):
        texts = [item["q"], item["why"]] + list(item["choices"])
        t = item.get("table")
        if t:
            texts += [str(h) for h in t["headers"]] + [str(c) for r in t["rows"] for c in r]
        for text in texts:
            for pat, msg in _BANNED:
                hit = pat.search(text)
                assert not hit, f"{module.TOPIC[0]} q{i}: {msg} -- {hit.group(0)!r} in {text[:70]!r}"
    print(f"OK  {module.TOPIC[0]} notation: no typeset markup in "
          f"{len(module.QUESTIONS)} questions.")


HEIGHT = "Mean foraging height in the canopy (meters)"
OUTER = "Percent of foraging time spent in the outer needles"
NIGHT = "Captures between midnight and dawn"
MORN = "Captures between dawn and midday"
WIDTH = "Mean seed width taken (millimeters)"
BIGSEED = "Percent of seeds taken that were wider than 6 millimeters"
HARES = "Hares counted per square kilometer"
LYNX = "Lynx counted per hundred square kilometers"
MDENS = "Mean cell density of Species M after ten days (cells per milliliter)"
NDENS = "Mean cell density of Species N after ten days (cells per milliliter)"
SHALLOW = "Percent of root mass above 20 centimeters depth"
DEEP = "Percent of root mass below 60 centimeters depth"
UPPER = "Percent cover in the upper shore zone"
LOWER = "Percent cover in the lower shore zone"
FIRST = "Change in growth of the first species when paired (percent)"
SECOND = "Change in growth of the second species when paired (percent)"
MITES = "Mean mites carried per beetle"
EGGS = "Mean eggs laid per female beetle"
EATEN = "Mean prey eaten per predator per day"


def q5(table, item):
    h = dict(zip(cg.labels(table), cg.col(table, HEIGHT)))
    assert len(set(h.values())) == len(h), "the four mean heights must differ"
    assert max(h.values()) - min(h.values()) >= 10, "the heights must separate the species"
    o = dict(zip(cg.labels(table), cg.col(table, OUTER)))
    tallest = max(h, key=h.get)
    assert min(o, key=o.get) != tallest, \
        "the 'tallest also spends least time in the outer needles' distractor must be false"
    return (f"the four mean heights {sorted(h.values())} are all different and span "
            f"{max(h.values()) - min(h.values())} meters, and the tallest forager is not "
            "the one spending least time in the outer needles")


def q6(table, item):
    n = dict(zip(cg.labels(table), cg.col(table, NIGHT)))
    m = dict(zip(cg.labels(table), cg.col(table, MORN)))
    assert n["Mammal J"] > 5 * m["Mammal J"], "Mammal J is not concentrated before dawn"
    assert m["Mammal K"] > 5 * n["Mammal K"], "Mammal K is not concentrated after dawn"
    assert (n["Mammal J"] > n["Mammal K"]) and (m["Mammal K"] > m["Mammal J"]), \
        "the two mammals must peak in opposite halves of the day"
    return ("each mammal was caught more than five times as often in one half of the day "
            "as in the other, and the two halves are opposite ones")


def q7(table, item):
    w = dict(zip(cg.labels(table), cg.col(table, WIDTH)))
    b = dict(zip(cg.labels(table), cg.col(table, BIGSEED)))
    assert w["Finch P"] != w["Finch Q"], "'same mean width' must be false"
    narrower = min(w, key=w.get)
    assert b[narrower] < b[max(w, key=w.get)], \
        "the 'narrower-seed finch takes the larger share of wide seeds' distractor must be false"
    return (f"the mean widths {w['Finch P']} and {w['Finch Q']} millimeters differ, and the "
            "finch taking the narrower seeds takes the smaller share of the wide seeds")


def q12(table, item):
    years = cg.labels(table)
    hares = cg.col(table, HARES)
    lynx = cg.col(table, LYNX)
    hpeak = years[hares.index(max(hares))]
    lpeak = years[lynx.index(max(lynx))]
    assert hpeak != lpeak, "'same year' must be false"
    assert years.index(lpeak) == years.index(hpeak) + 1, \
        f"lynx peak {lpeak} is not the year after the hare peak {hpeak}"
    assert any(lynx[i + 1] > lynx[i] for i in range(len(lynx) - 1)), \
        "'lynx fell every year' must be false"
    assert any(hares[i + 1] < hares[i] for i in range(len(hares) - 1)), \
        "'hares rose every year' must be false"
    return (f"hares peak at {hpeak} and lynx at {lpeak}, one survey later, and neither "
            "column is monotone")


def q14(table, item):
    m_alone = cg.cell(table, "Species M grown alone", MDENS)
    n_alone = cg.cell(table, "Species N grown alone", NDENS)
    m_both = cg.cell(table, "Both species grown together", MDENS)
    n_both = cg.cell(table, "Both species grown together", NDENS)
    assert m_both < m_alone and n_both < n_alone, "both species must fall when grown together"
    assert m_both > 0, "'Species M was eliminated' must be false"
    assert m_both + n_both < min(m_alone, n_alone), \
        "'the mixed culture held more cells in total' must be false"
    return (f"Species M falls from {m_alone:.0f} to {m_both:.0f} and Species N from "
            f"{n_alone:.0f} to {n_both:.0f}, and the mixed total {m_both + n_both:.0f} is "
            "below either single culture")


def q18(table, item):
    s = dict(zip(cg.labels(table), cg.col(table, SHALLOW)))
    d = dict(zip(cg.labels(table), cg.col(table, DEEP)))
    top = max(s, key=s.get)
    assert d[top] == min(d.values()), \
        "the 'more shallow roots also more deep roots' distractor must be false"
    assert max(d.values()) > 0, "'neither plant has roots below sixty centimeters' must be false"
    assert s[top] > 50 and d[max(d, key=d.get)] > 50, "the two plants must occupy different depths"
    return (f"the shallow-rooted plant holds {s[top]:.0f} percent of its roots near the "
            f"surface and only {d[top]:.0f} percent deep, the reverse of the other plant")


def q22(table, item):
    u = dict(zip(cg.labels(table), cg.col(table, UPPER)))
    lo = dict(zip(cg.labels(table), cg.col(table, LOWER)))
    high = max(u, key=u.get)
    assert lo[high] == min(lo.values()), \
        "the 'more upper cover also more lower cover' distractor must be false"
    assert max(u.values()) > 50, "'neither species is present in the upper zone' must be false"
    assert max(lo, key=lo.get) != high, "the two species must peak in opposite zones"
    return (f"the species with {u[high]:.0f} percent cover above has only {lo[high]:.0f} "
            "percent below, and the other species is the reverse")


def q23(table, item):
    a = dict(zip(cg.labels(table), cg.col(table, FIRST)))
    b = dict(zip(cg.labels(table), cg.col(table, SECOND)))
    one_gains_one_flat = [p for p in a if a[p] > 0 and b[p] == 0]
    assert one_gains_one_flat == ["Pairing 2"], \
        f"exactly one pairing must show a gain against no change; got {one_gains_one_flat}"
    assert a["Pairing 1"] > 0 and b["Pairing 1"] > 0, "Pairing 1 must show two gains"
    assert a["Pairing 3"] > 0 > b["Pairing 3"], "Pairing 3 must show a gain against a loss"
    return ("only Pairing 2 pairs a positive change with a change of zero; the other two "
            "pair two gains and a gain against a loss")


def q24(table, item):
    m = dict(zip(cg.labels(table), cg.col(table, MITES)))
    e = dict(zip(cg.labels(table), cg.col(table, EGGS)))
    carried = max(m, key=m.get)
    assert e[carried] < min(v for k, v in e.items() if k != carried), \
        "the group carrying mites must lay fewer eggs"
    assert e[carried] != max(e.values()), "'the mite benefits the beetle' must be false"
    assert len(set(e.values())) > 1, "'no measurable effect' must be false"
    return (f"beetles carrying {m[carried]:.0f} mites laid {e[carried]:.0f} eggs against "
            f"{max(e.values()):.0f} for beetles with the mites removed")


def q26(table, item):
    offered = [cg.num(r[0]) for r in table["rows"]]
    eaten = cg.col(table, EATEN)
    assert all(eaten[i + 1] > eaten[i] for i in range(len(eaten) - 1)), "consumption must rise"
    steps = [eaten[i + 1] - eaten[i] for i in range(len(eaten) - 1)]
    assert all(steps[i + 1] <= steps[i] for i in range(len(steps) - 1)), \
        f"the increments must not grow; got {steps}"
    assert steps[-1] < steps[0], "the rise must slow across the range"
    ratios = [e / o for o, e in zip(offered, eaten)]
    assert len(set(round(r, 6) for r in ratios)) > 1, "'exact proportion' must be false"
    assert all(e < o for o, e in zip(offered, eaten)), "'eats every prey offered' must be false"
    return (f"consumption rises {eaten} while the successive increments {steps} shrink, so "
            "the response is rising and decelerating rather than proportional")


CLAIMS = [
 ("eats another organism",
  "ERT-1.A.1, near verbatim: in a predator-prey relationship the predator is an organism that eats another organism (the prey). The hawk is the eater, so it holds the predator role."),
 ("close and long-term interaction",
  "ERT-1.A.2 defines symbiosis as a close and long-term interaction between two species. A single brief contest satisfies neither closeness nor duration, so the term does not apply regardless of the outcome."),
 ("both drawing on the same limited oxygen supply",
  "ERT-1.A.3, near verbatim: competition can occur within or between species in an ecosystem where there are limited resources. The keyed option is the only one that keeps both the within-species and the between-species case and ties them to scarcity."),
 ("different ways, places, or at different times",
  "ERT-1.A.3 states the three modes of resource partitioning and states its effect as reducing the negative impact of competition on survival. It does not claim competition ends or that the resource base grows."),
 ("foraging in different places",
  "Recomputed in q5 above. The tabulated variable is position within the canopy, so place is the only axis of separation the data can show; ERT-1.A.3 names using the resources in different places as one mode."),
 ("at different times",
  "Recomputed in q6 above: each mammal was trapped overwhelmingly in one half of the day and the two halves are opposite. ERT-1.A.3 names using the resources at different times as one mode of partitioning."),
 ("handling seeds of different sizes",
  "Recomputed in q7 above. The two finches are separated only by the size of seed taken, which is a difference in how the shared resource is used; ERT-1.A.3 names using the resources in different ways as one mode."),
 ("within a species",
  "ERT-1.A.3 states that competition can occur within or between species where there are limited resources. Browse has become limited and the contest is among members of one species, which is the within-species case the statement allows."),
 ("both species gain from the association",
  "ERT-1.A.2 names mutualism, commensalism and parasitism as distinct types of symbiosis. The minimum that distinguishing them requires is that mutualism is the type in which both partners gain, which is what the stem describes."),
 ("not measurably affected",
  "ERT-1.A.2 names commensalism as a type of symbiosis distinct from the other two, and the minimum that distinction requires is that one partner gains while the other is unaffected. Attachment alone does not establish a cost to the host."),
 ("close and long-term between two species",
  "ERT-1.A.2 defines symbiosis by closeness and duration, and ERT-1.A.1 defines the predator simply as an organism that eats another organism. A lifelong internal association is what places this case under the symbiosis statement."),
 ("one year after",
  "Recomputed in q12 above from the two count columns: the predator maximum falls one survey after the prey maximum, and neither column is monotone, so the three rival readings are false on the same numbers."),
 ("scarcity is a condition of the interaction",
  "ERT-1.A.3 places competition in ecosystems where there are limited resources, so scarcity is written into the statement rather than being incidental to it."),
 ("lower density when grown with the other",
  "Recomputed in q14 above: both species fall when combined and the mixed total is below either single culture. ERT-1.A.3 makes competition the interaction arising where two populations draw on the same limited resource."),
 ("in different forms",
  "ERT-1.A.3 defines resource partitioning as using the resources in different ways, places, or at different times, so direct evidence of partitioning is evidence of separation along one of those three axes and nothing else."),
 ("its own species",
  "ERT-1.A.2 requires a close and long-term interaction between two species. A brief contest between two members of one species fails both conditions; the framework files that case under competition in ERT-1.A.3 instead."),
 ("rather than removing competition",
  "ERT-1.A.3 states that resource partitioning can reduce the negative impact of competition on survival. It asserts a reduction in impact, not the disappearance of the interaction."),
 ("draw water from different depths",
  "Recomputed in q18 above: one plant holds most of its root mass near the surface and the other most of it deep. Depth is a matter of position, which ERT-1.A.3 calls using the resources in different places."),
 ("releases the second population",
  "ERT-1.A.1 makes the predator the organism that eats another organism, so removing it removes that source of mortality on the prey, which is what the observed rise in the small fish reflects."),
 ("an interaction between two species",
  "ERT-1.A.2 specifies two species in the definition of symbiosis, so a within-species association falls outside it. The framework still allows within-species interaction, but under the competition statement ERT-1.A.3."),
 ("a different shore zone",
  "Recomputed in q22 above: each species holds its high cover in the opposite zone from the other. Zone is position on the shore, which is the mode ERT-1.A.3 calls using the resources in different places."),
 ("Pairing 2",
  "Recomputed in q23 above: exactly one pairing shows a gain to one partner against no change in the other, which is the outcome pattern that distinguishes commensalism from the other two types named in ERT-1.A.2."),
 ("at the expense of the other",
  "Recomputed in q24 above: the beetles carrying the mite laid fewer eggs than those from which it was removed. ERT-1.A.2 names parasitism as the type of symbiosis in which one partner gains at the other's cost."),
 ("holes in dead trees for nesting",
  "ERT-1.A.3 requires a shared resource that is limited. Only the keyed pair needs the same scarce structure; the remaining options describe unshared resources, a predator-prey relationship, or separation in time."),
 ("the rise gets smaller",
  "Recomputed in q26 above: consumption rises with supply while the successive increments shrink, so the relationship is neither proportional, flat nor falling, and the predator never takes every prey offered."),
 ("in years when the shared food is plentiful",
  "ERT-1.A.3 conditions competition on limited resources, so the argument that resource availability determines whether two species compete predicts an effect that appears under scarcity and fades under plenty. Only the keyed finding tests that prediction."),
 ("drawing on the same limited resource",
  "ERT-1.A.1 defines predation by the act of eating another organism and ERT-1.A.3 defines competition by a shared limited resource, allowing it within or between species. Neither statement restricts the interaction by habitat or duration."),
 ("types of symbiosis",
  "ERT-1.A.2 lists mutualism, commensalism and parasitism as types of symbiosis, and defines symbiosis as a close and long-term interaction between two species, so that definition is what the three share."),
 ("no partitioning available",
  "The two populations draw on the same limited nutrients in the same place, in the same form and at the same times, which is both the condition ERT-1.A.3 sets for competition and the absence of all three modes of partitioning it names."),
 ("which organism does the eating",
  "ERT-1.A.1 assigns the predator role to the organism that eats another organism, so the role belongs to a particular relationship rather than to the animal, and one organism can hold either role in different pairings."),
]

TABLE_CHECKS = {5: q5, 6: q6, 7: q7, 12: q12, 14: q14, 18: q18,
                21: q22, 22: q23, 23: q24, 25: q26}


def _selftest():
    """Negative control: every gate below must FAIL when its input is corrupted."""
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("e1_1_mutant")
        mod.TOPIC = e1_1.TOPIC
        mod.QUESTIONS = copy.deepcopy(e1_1.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[0]["ans"] = 2

    def break_anchor(mod, claims):
        claims[3] = ("no such phrase anywhere in the module", claims[3][1])

    def corrupt_table(mod, claims):
        # push the lynx maximum into the same year as the hare maximum
        mod.QUESTIONS[11]["table"] = dict(
            headers=e1_1._T_CYCLE["headers"],
            rows=[[y, h, ("99" if y == "Year 3" else lx)]
                  for y, h, lx in e1_1._T_CYCLE["rows"]])

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[4]["choices"][3] = mod.QUESTIONS[4]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[8]["why"] = "Because it is."

    def letter_reference(mod, claims):
        mod.QUESTIONS[6]["why"] = ("Option C is wrong because the framework says so and "
                                   "the rest of the reasoning follows from that.")

    def latex_slips_in(mod, claims):
        mod.QUESTIONS[2]["choices"][1] = "Only \\frac{1}{2} of the oxygen is available"
        style(mod)

    def range_slips_in(mod, claims):
        mod.QUESTIONS[1]["q"] = "Between 2000-2020 two ant species met once at a range edge."
        style(mod)

    print("negative controls:")
    must_fail("a backslash macro in a choice", latex_slips_in)
    must_fail("a digit-hyphen-digit range in a stem", range_slips_in)
    must_fail("key moved off its anchor", move_key)
    must_fail("anchor no longer in the keyed choice", break_anchor)
    must_fail("table value corrupted so the keyed conclusion is false", corrupt_table)
    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a why reduced below the minimum", thin_why)
    must_fail("a why naming an option by letter", letter_reference)
    print("all negative controls raised as required.")


import e1_1  # noqa: E402  (after the helpers, so the selftest can import it too)

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(e1_1)
cg.check(e1_1, CLAIMS, table_checks=TABLE_CHECKS)
