"""Key audit for AP ENVIRONMENTAL SCIENCE 1.6 The Phosphorus Cycle.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Items 13, 24 and 30 rest on ERT-1.F.1: the phosphorus cycle is the movement of
atoms and molecules containing the element phosphorus between sources and sinks.

Items 1, 2, 6, 7, 12, 13, 15, 18, 19, 23, 26, 28 and 29 rest on ERT-1.F.2: the
major reservoirs of phosphorus are rock and ocean sediments that contain
phosphorus-bearing minerals, and the phosphorus cycle lacks a significant
atmospheric component.

Items 3, 4, 5, 8, 9, 10, 11, 14, 16, 17, 20, 21, 22, 25, 27 and 30 rest on
ERT-1.F.3: phosphorus is relatively scarce in ecosystems because rocks weather
slowly, and as a result phosphorus is often a limiting nutrient for plants and
other producers, particularly in freshwater and some terrestrial ecosystems.
The words "often" and "some" are part of that claim, which is why item 27 keys a
mixed result rather than a universal one.

THE ONE CROSS-CYCLE COMPARISON is the framework's own. Items 6, 15 and 29 set
ERT-1.F.2 (no significant atmospheric component) against ERT-1.E.4 (the largest
reservoir of nitrogen is the atmosphere). Nothing else here reaches outside the
three phosphorus statements, and the bare sources-and-sinks definition is asked
only in topic 1.4, for carbon.

DATA ITEMS: 6, 7, 8, 9, 10, 11, 12 and 20 carry tables. Each keyed conclusion is
recomputed below from that table alone, and each check also falsifies the
distractors against the same numbers.

NEGATIVE CONTROL: ``python3 verify_e1_6.py --selftest`` corrupts a key, an
anchor, a table cell and the notation on purpose and confirms each check fires.
"""
import re
import sys

import cg_check as cg

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


PHELD = "Phosphorus held (billions of tonnes)"
DEPTH = "Depth of rock weathered in a century (millimeters)"
PREL = "Phosphorus released to the soil in a century (kilograms per hectare)"
ALGAE4 = "Algal mass after four weeks (grams per cubic meter)"
PADD = "Phosphorus added (kilograms per hectare)"
PMASS = "Plant mass grown (kilograms per hectare)"
PSOIL = "Phosphorus available in the soil (milligrams per kilogram)"
PMOVED = "Phosphorus moved each year (millions of tonnes)"
PDISS = "Dissolved phosphorus (micrograms per liter)"
ALGMASS = "Algal mass (grams per cubic meter)"


def q6(table, item):
    cells = {r[0]: r[1] for r in table["rows"]}
    assert set(cells) == {"Nitrogen", "Phosphorus"}, f"unexpected rows {list(cells)}"
    n_share = cg.num(cells["Nitrogen"])
    assert n_share > 50, f"the nitrogen share must be a large fraction of the air; got {n_share}"
    assert not re.search(r"\d", cells["Phosphorus"]), \
        f"the phosphorus cell must record no measurable share; got {cells['Phosphorus']!r}"
    assert "no measurable" in cg.normalize(cells["Phosphorus"]), \
        "the phosphorus cell must say the share is not measurable"
    return (f"nitrogen occupies about {n_share:.0f} percent of the dry air "
            "while phosphorus has no measurable gaseous share")


def q7(table, item):
    r = dict(zip(cg.labels(table), cg.col(table, PHELD)))
    rock = "Rock containing phosphorus-bearing minerals"
    mineral = r[rock] + r["Ocean sediments"]
    total = sum(r.values())
    assert mineral / total > 0.99, f"the two mineral reservoirs must hold almost everything; got {mineral / total:.4f}"
    assert r["Atmosphere"] == min(r.values()), "the atmosphere must be the smallest reservoir"
    assert r["Atmosphere"] < 1e-6 * r[rock], "the atmospheric share must be negligible against rock"
    assert r["Living organisms"] < r["Ocean sediments"], \
        "'living organisms hold more than ocean sediments' must be false"
    assert r["Soil"] < r[rock], "'soil holds more than rock' must be false"
    return (f"rock and ocean sediments hold {100 * mineral / total:.2f} percent of the "
            f"tabulated phosphorus while the atmosphere holds {r['Atmosphere']}")


def q8(table, item):
    pairs = sorted(zip(cg.col(table, DEPTH), cg.col(table, PREL)))
    assert all(pairs[i + 1][1] > pairs[i][1] for i in range(len(pairs) - 1)), \
        f"phosphorus released must rise with depth weathered; got {pairs}"
    assert pairs[0][1] != max(p for _, p in pairs), \
        "'the least weathered rock released the most' must be false"
    assert len(set(d for d, _ in pairs)) == len(pairs), "'all four weathered equally' must be false"
    return (f"sorted by depth weathered the phosphorus released reads {[p for _, p in pairs]}, "
            "strictly increasing across the four rock types")


def q9(table, item):
    a = dict(zip(cg.labels(table), cg.col(table, ALGAE4)))
    treat = {r[0]: r[1] for r in table["rows"]}
    ctrl = [k for k, v in treat.items() if v == "Nothing"][0]
    only_n = [k for k, v in treat.items() if v == "Nitrogen"][0]
    only_p = [k for k, v in treat.items() if v == "Phosphorus"][0]
    both = [k for k, v in treat.items() if v == "Nitrogen and phosphorus"][0]
    assert abs(a[only_n] - a[ctrl]) < 0.3 * a[ctrl], \
        f"nitrogen alone must barely differ from the control; got {a[only_n]} against {a[ctrl]}"
    assert a[only_p] > 3 * a[ctrl], "phosphorus alone must raise algal mass several-fold"
    assert a[both] > 3 * a[ctrl], "the combined treatment must also rise, since it includes phosphorus"
    assert a[ctrl] == min(a.values()), "'the untreated enclosure grew the most' must be false"
    return (f"the untreated enclosure holds {a[ctrl]} grams per cubic meter, nitrogen alone "
            f"{a[only_n]}, phosphorus alone {a[only_p]} and both together {a[both]}")


def q10(table, item):
    pairs = sorted(zip(cg.col(table, PADD), cg.col(table, PMASS)))
    assert all(pairs[i + 1][1] > pairs[i][1] for i in range(len(pairs) - 1)), \
        f"plant mass must rise with phosphorus added; got {pairs}"
    base = pairs[0][1]
    assert pairs[1][1] > 1.2 * base, \
        "the smallest addition must already differ clearly, so 'only the largest differed' is false"
    assert base == min(m for _, m in pairs), "'the untreated plot grew the most' must be false"
    return (f"sorted by phosphorus added the plant mass reads {[m for _, m in pairs]}, rising "
            "at every step including the smallest addition")


def q11(table, item):
    age = [cg.num(r[0]) for r in table["rows"]]
    p = cg.col(table, PSOIL)
    assert all(age[i + 1] > age[i] for i in range(len(age) - 1)), "rows must run from young to old"
    assert all(p[i + 1] < p[i] for i in range(len(p) - 1)), f"available phosphorus must fall; got {p}"
    assert p[-1] == min(p), "'the oldest surface holds the most' must be false"
    assert p[0] == max(p), "'the youngest surface holds the least' must be false"
    return (f"as surface age rises {age} thousand years, available soil phosphorus falls {p} "
            "milligrams per kilogram")


def q12(table, item):
    f = dict(zip(cg.labels(table), cg.col(table, PMOVED)))
    dust = "Carried through the air as dust"
    others = {k: v for k, v in f.items() if k != dust}
    assert all(f[dust] < 0.1 * v for v in others.values()), \
        f"the airborne route must be far smaller than each other route; got {f}"
    assert f[dust] != max(f.values()), "'the airborne route moves the most' must be false"
    assert f["Burial in ocean sediments"] > 0, "'burial moves no phosphorus' must be false"
    assert f["Weathering of rock into soil and water"] > f[dust], \
        "'weathering moves less than the airborne route' must be false"
    return (f"the airborne route moves {f[dust]:.0f} million tonnes a year against "
            f"{sorted(others.values())} for the other three routes")


def q20(table, item):
    pairs = sorted(zip(cg.col(table, PDISS), cg.col(table, ALGMASS)))
    assert all(pairs[i + 1][1] > pairs[i][1] for i in range(len(pairs) - 1)), \
        f"algal mass must rise with dissolved phosphorus; got {pairs}"
    assert pairs[0][1] != max(m for _, m in pairs), \
        "'the lake with the least phosphorus carries the most algae' must be false"
    assert len(set(p for p, _ in pairs)) == len(pairs), \
        "'dissolved phosphorus is the same in all four lakes' must be false"
    assert len(set(m for _, m in pairs)) == len(pairs), "'algal mass is the same' must be false"
    return (f"sorted by dissolved phosphorus the algal mass reads {[m for _, m in pairs]}, "
            "strictly increasing across the four lakes")


CLAIMS = [
 ("ocean sediments that contain phosphorus-bearing minerals",
  "ERT-1.F.2, near verbatim: the major reservoirs of phosphorus in the phosphorus cycle are rock and ocean sediments that contain phosphorus-bearing minerals."),
 ("significant atmospheric component",
  "ERT-1.F.2 states plainly that the phosphorus cycle lacks a significant atmospheric component. ERT-1.F.1 and the rest of ERT-1.F.2 supply the movement, the rock reservoir and the sediment reservoir that the rejected options wrongly deny."),
 ("weather slowly",
  "ERT-1.F.3, near verbatim: phosphorus is relatively scarce in ecosystems because rocks weather slowly. The scarcity is a matter of the rate at which the store is opened, not of the size of the store."),
 ("often a limiting nutrient",
  "ERT-1.F.3, near verbatim: as a result, phosphorus is often a limiting nutrient for plants and other producers."),
 ("some terrestrial ecosystems",
  "ERT-1.F.3 states that phosphorus is often a limiting nutrient for plants and other producers, particularly in freshwater and some terrestrial ecosystems."),
 ("nitrogen cycle has a large atmospheric reservoir",
  "Recomputed in q6 above from the tabulated shares. ERT-1.E.4 makes the atmosphere the largest reservoir of nitrogen and ERT-1.F.2 states that the phosphorus cycle lacks a significant atmospheric component, which is the asymmetry the table records."),
 ("together hold almost all",
  "Recomputed in q7 above: the two mineral reservoirs sum to more than ninety-nine percent of the tabulated total while the atmospheric entry is negligible. ERT-1.F.2 names rock and ocean sediments as the major reservoirs and denies the cycle a significant atmospheric component."),
 ("releases more phosphorus",
  "Recomputed in q8 above: sorting the rock types by depth weathered leaves the phosphorus released strictly increasing. ERT-1.F.3 makes the slowness of rock weathering the reason phosphorus is scarce, so weathering rate governs supply."),
 ("adding nitrogen alone did not",
  "Recomputed in q9 above: the nitrogen enclosure barely differs from the untreated one while both enclosures receiving phosphorus rose several-fold. ERT-1.F.3 states that phosphorus is often the limiting nutrient, particularly in freshwater ecosystems."),
 ("raised the plant mass grown",
  "Recomputed in q10 above: plant mass increases at every step up the phosphorus column, including the smallest addition. ERT-1.F.3 makes phosphorus often limiting for producers, particularly in freshwater and some terrestrial ecosystems, and grassland is a terrestrial case."),
 ("falls as the land surface gets older",
  "Recomputed in q11 above: available soil phosphorus falls steadily with surface age. ERT-1.F.2 gives the cycle no significant atmospheric component to resupply a soil and ERT-1.F.3 makes the rock supply slow to open."),
 ("moves far less phosphorus",
  "Recomputed in q12 above: the airborne figure is smaller than each of the other three routes by more than an order of magnitude, which is what ERT-1.F.2 means in saying the cycle lacks a significant atmospheric component."),
 ("phosphorus gas in the atmosphere",
  "ERT-1.F.2 states that the phosphorus cycle lacks a significant atmospheric component, while ERT-1.F.1 supplies the movement between sources and sinks, ERT-1.F.2 supplies the two mineral reservoirs, and ERT-1.F.3 makes phosphorus a nutrient for producers."),
 ("More phosphorus would be released",
  "ERT-1.F.3 states that phosphorus is relatively scarce because rocks weather slowly, which makes the weathering rate the gate on supply, so opening that gate wider lets more phosphorus through."),
 ("comes from rock and sediments instead",
  "ERT-1.F.2 states that the phosphorus cycle lacks a significant atmospheric component and names rock and ocean sediments as its major reservoirs, while ERT-1.E.4 makes the atmosphere the largest nitrogen reservoir, so the two cycles differ exactly here."),
 ("Add phosphorus to some enclosures",
  "ERT-1.F.3 states that phosphorus is often a limiting nutrient for producers, particularly in freshwater ecosystems, and a limiting nutrient is tested by relieving the limit in some units and comparing them against untreated ones."),
 ("adding other nutrients alone does not",
  "A limiting nutrient is identified by the response to relieving it, so the diagnostic comparison is between adding phosphorus and adding something else. Merely containing phosphorus, or holding it in rock, does not show that its supply is what constrains growth."),
 ("only as they weather",
  "ERT-1.F.2 places the major reservoirs in rock and ocean sediments and denies the cycle a significant atmospheric component, and ERT-1.F.3 makes rock weathering slow, so both routes that might act quickly are closed."),
 ("one of the major reservoirs of phosphorus",
  "ERT-1.F.2 names rock and ocean sediments that contain phosphorus-bearing minerals as the major reservoirs of the cycle, so burial on the seafloor is phosphorus arriving at one of them."),
 ("carry more algae",
  "Recomputed in q20 above: sorting the lakes by dissolved phosphorus leaves algal mass strictly increasing. ERT-1.F.3 states that phosphorus is often a limiting nutrient for producers, particularly in freshwater ecosystems."),
 ("already given up much",
  "ERT-1.F.3 attributes phosphorus scarcity to slow rock weathering and ERT-1.F.2 gives the cycle no significant atmospheric route, so a long-weathered surface has neither a fast source nor an aerial resupply."),
 ("is not the constraint",
  "ERT-1.F.2 grants that rock is a major reservoir, and ERT-1.F.3 states that phosphorus is relatively scarce in ecosystems BECAUSE rocks weather slowly, so the constraint is the rate of release rather than the size of the store."),
 ("slowly weathering rock and sediments",
  "ERT-1.F.3 gives slow rock weathering as the cause of scarcity and ERT-1.F.2 denies the cycle a significant atmospheric component, so both of the ways a supply might be replenished quickly are absent."),
 ("eventually in ocean sediments",
  "ERT-1.F.1 defines the phosphorus cycle as the movement of phosphorus-containing atoms and molecules between sources and sinks, so tracing the same phosphorus through successive reservoirs is what shows the movement; a single measurement shows only a standing amount."),
 ("support more producer growth",
  "ERT-1.F.3 states that phosphorus is often a limiting nutrient for plants and other producers, particularly in freshwater ecosystems, so a difference in the limiting nutrient is expected to appear as a difference in growth."),
 ("In rock and in ocean sediments",
  "ERT-1.F.2 names rock and ocean sediments containing phosphorus-bearing minerals as the major reservoirs of phosphorus and denies the cycle a significant atmospheric component."),
 ("but not in all of them",
  "ERT-1.F.3 says phosphorus is OFTEN a limiting nutrient, particularly in freshwater and SOME terrestrial ecosystems. Those two qualifiers are part of the claim, so a mixed result across two grassland stretches is what the statement leads one to expect."),
 ("no widespread airborne supply",
  "ERT-1.F.2 states that the phosphorus cycle lacks a significant atmospheric component, so unlike an element with a large atmospheric reservoir, phosphorus has no aerial route by which a depleted place can be resupplied from a distance."),
 ("while nitrogen has its largest reservoir in the atmosphere",
  "ERT-1.F.2 names rock and ocean sediments as the major phosphorus reservoirs and denies that cycle a significant atmospheric component, while ERT-1.E.4 states that the largest reservoir of nitrogen is the atmosphere."),
 ("faster than slow weathering replaces it",
  "ERT-1.F.1 makes the cycle a movement between sources and sinks and ERT-1.F.3 makes the rock source slow, so an outflow exceeding the weathering supply is exactly what those two statements together allow."),
]

TABLE_CHECKS = {6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 20: q20}


def _selftest():
    """Negative control: every gate below must FAIL when its input is corrupted."""
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("e1_6_mutant")
        mod.TOPIC = e1_6.TOPIC
        mod.QUESTIONS = copy.deepcopy(e1_6.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[2]["ans"] = 4

    def break_anchor(mod, claims):
        claims[1] = ("no such phrase anywhere in the module", claims[1][1])

    def corrupt_table(mod, claims):
        # give the nitrogen-only enclosure the large algal response
        mod.QUESTIONS[8]["table"] = dict(
            headers=e1_6._T_LAKEADD["headers"],
            rows=[[e, n, ("11.9" if n == "Nitrogen" else v)]
                  for e, n, v in e1_6._T_LAKEADD["rows"]])

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[0]["choices"][1] = mod.QUESTIONS[0]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[15]["why"] = "It just is."

    def letter_reference(mod, claims):
        mod.QUESTIONS[27]["why"] = ("Choice C is wrong because the framework says so and "
                                    "the rest of the reasoning follows from that.")

    def latex_slips_in(mod, claims):
        mod.QUESTIONS[3]["choices"][2] = "Phosphorus reaches \\frac{1}{2} of the atmosphere"
        style(mod)

    def range_slips_in(mod, claims):
        mod.QUESTIONS[4]["q"] = "Between 1980-2000 which ecosystems did the framework single out?"
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


import e1_6  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(e1_6)
cg.check(e1_6, CLAIMS, table_checks=TABLE_CHECKS)
