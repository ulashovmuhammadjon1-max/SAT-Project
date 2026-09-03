"""Key audit for AP ENVIRONMENTAL SCIENCE 1.9 Trophic Levels.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Items 1, 2, 8, 12, 14, 17, 20, 23, 25, 28, 29 and 30 rest on ENG-1.B.1: all
ecosystems depend on a continuous inflow of high-quality energy in order to
maintain their structure and function of transferring matter between the
environment and organisms via biogeochemical cycles.

Items 3, 4, 9, 10, 13, 18, 19, 22, 23, 26 and 30 rest on ENG-1.B.2:
biogeochemical cycles are essential for life and each cycle demonstrates the
conservation of matter.

Items 5, 6, 7, 11, 15, 16, 21, 24, 27, 28 and 29 rest on ENG-1.B.3: in
terrestrial and near-surface marine communities, energy flows from the sun to
producers in the lowest trophic levels and then upward to higher trophic levels.

WHAT IS DELIBERATELY NOT ASKED. The QUANTITY passed between levels is ENG-1.C.1,
the ten percent rule, and belongs to topic 1.10; no item here tabulates or keys a
transfer efficiency. The named consumer categories and food-web structure are
ENG-1.D.1 and ENG-1.D.2 and belong to topic 1.11; no item here asks a student to
classify an organism as herbivore, omnivore, carnivore, detritivore or
decomposer. Items 15 and 16 use a table that states outright what each organism
eats, so no classification is required.

DATA ITEMS: 8, 9, 10, 11, 12, 15, 16, 17 and 19 carry tables. Items 9, 10 and 19
require a budget to close, and each is recomputed below by addition.

NEGATIVE CONTROL: ``python3 verify_e1_9.py --selftest`` corrupts a key, an
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


HOURS = "Light supplied each day (hours)"
REMAIN = "Living mass remaining after six months (percent of the starting mass)"
AMOUNT = "Amount"
SUNPCT = "Percent of sunlight allowed to reach the water"
PRODMASS = "Mass of producers after one season (grams per square meter)"
CONSMASS = "Mass of consumers after one season (grams per square meter)"
ARRIVE = "Sunlight arriving each year (kilocalories per square meter)"
CAPTURE = "Energy captured by producers each year (kilocalories per square meter)"
WASHED = "Organic matter washed in each month (grams)"
POOLMASS = "Living mass of the pool community (grams)"


def _budget(table, in_key, out_key, store_key):
    v = dict(zip(cg.labels(table), cg.col(table, AMOUNT)))
    inflow, outflow, stored = v[in_key], v[out_key], v[store_key]
    assert abs(inflow - (outflow + stored)) < 1e-9, \
        f"the budget must close: {inflow} against {outflow} plus {stored}"
    assert stored > 0, "'nothing was retained' must be false"
    assert outflow < inflow, "'more left than entered' must be false"
    assert stored < inflow, "'more was retained than entered' must be false"
    return inflow, outflow, stored


def q8(table, item):
    h = dict(zip(cg.labels(table), cg.col(table, HOURS)))
    m = dict(zip(cg.labels(table), cg.col(table, REMAIN)))
    pairs = sorted((h[k], m[k]) for k in h)
    assert all(pairs[i + 1][1] > pairs[i][1] for i in range(len(pairs) - 1)), \
        f"living mass retained must rise with light; got {pairs}"
    dark = min(h, key=h.get)
    assert h[dark] == 0 and m[dark] < 10, "the unlit chamber must retain almost nothing"
    assert m[dark] == min(m.values()), "'the unlit chamber retained the most' must be false"
    assert len(set(m.values())) == len(m), "'all three retained about the same' must be false"
    return (f"sorted by light supplied the living mass retained reads {[x for _, x in pairs]} "
            "percent, rising with the light and near zero in the dark")


def q9(table, item):
    inflow, outflow, stored = _budget(
        table, "Nitrogen entering the field", "Nitrogen leaving the field",
        "Increase in nitrogen stored in the field")
    assert outflow != inflow, "'the outflow equals the inflow' must be false"
    return (f"{inflow:.0f} entering equals {outflow:.0f} leaving plus {stored:.0f} added to "
            "storage, so the nitrogen budget closes exactly")


def q10(table, item):
    intake, back, stored = _budget(
        table, "Carbon taken in from the air by producers",
        "Carbon returned to the air by all organisms",
        "Increase in carbon held in wood and soil")
    assert back < intake, "'more carbon returned than was taken in' must be false"
    return (f"{intake:.0f} tonnes taken in equals {back:.0f} returned plus {stored:.0f} added "
            "to wood and soil, so the carbon budget closes exactly")


def q11(table, item):
    labs = cg.labels(table)
    trio = sorted(zip(cg.col(table, SUNPCT), cg.col(table, PRODMASS), cg.col(table, CONSMASS)))
    prod = [p for _, p, _ in trio]
    cons = [c for _, _, c in trio]
    assert all(prod[i + 1] > prod[i] for i in range(len(prod) - 1)), f"producers must rise with light; got {prod}"
    assert all(cons[i + 1] > cons[i] for i in range(len(cons) - 1)), f"consumers must rise with light; got {cons}"
    assert cons[0] != max(cons), "'consumers were unaffected' must be false"
    assert prod[0] != max(prod), "'the darkest enclosure held the most producers' must be false"
    return (f"sorted by sunlight the producer mass reads {prod} and the consumer mass {cons}, "
            "both rising together")


def q12(table, item):
    pairs = sorted(zip(cg.col(table, ARRIVE), cg.col(table, CAPTURE)))
    assert all(pairs[i + 1][1] > pairs[i][1] for i in range(len(pairs) - 1)), \
        f"captured energy must rise with arriving sunlight; got {pairs}"
    assert all(c < 0.05 * a for a, c in pairs), \
        f"the captured share must stay a small fraction of what arrives; got {pairs}"
    assert len(set(c for _, c in pairs)) == len(pairs), "'the same amount was captured' must be false"
    return (f"arriving sunlight {[a for a, _ in pairs]} and captured energy "
            f"{[c for _, c in pairs]} rise together, with capture below five percent of "
            "arrival at every site")


def _levels(table):
    return {r[0]: r[1] for r in table["rows"]}


def q15(table, item):
    src = _levels(table)
    base = [k for k, v in src.items() if cg.normalize(v) == "sunlight"]
    assert base == ["Organism 1"], f"exactly one organism must feed on sunlight; got {base}"
    for k, v in src.items():
        if k != "Organism 1":
            assert "eating" in cg.normalize(v), f"{k} must obtain its energy by eating"
    return ("exactly one of the four organisms draws its energy directly from sunlight and "
            "the other three obtain theirs by eating another of them")


def q16(table, item):
    src = _levels(table)
    order = ["Organism 1", "Organism 2", "Organism 3", "Organism 4"]
    assert cg.normalize(src["Organism 1"]) == "sunlight", "Organism 1 must be the producer"
    for lower, upper in zip(order, order[1:]):
        assert cg.normalize(lower) in cg.normalize(src[upper]), \
            f"{upper} must be stated to eat {lower}; got {src[upper]!r}"
    return ("the table states that each organism after the first eats the one before it, "
            "and that the first draws its energy from sunlight, which fixes the order")


def q17(table, item):
    washed = cg.col(table, WASHED)
    mass = cg.col(table, POOLMASS)
    assert all(washed[i + 1] < washed[i] for i in range(len(washed) - 1)), f"inflow must fall; got {washed}"
    assert all(mass[i + 1] < mass[i] for i in range(len(mass) - 1)), f"living mass must fall; got {mass}"
    assert mass[washed.index(min(washed))] == min(mass), \
        "'the smallest inflow month held the largest community' must be false"
    assert len(set(washed)) == len(washed), "'the inflow was the same every month' must be false"
    return (f"the inflow falls {washed} grams a month while the community's living mass "
            f"falls {mass} grams alongside it")


def q19(table, item):
    inflow, outflow, stored = _budget(
        table, "Matter entering in the inflowing stream",
        "Matter leaving in the outflowing stream",
        "Matter added to the wetland's sediments and living tissue")
    return (f"{inflow:.0f} tonnes entering equals {outflow:.0f} leaving plus {stored:.0f} "
            "retained, so nothing in the budget is unaccounted for")


CLAIMS = [
 ("continuous inflow of high-quality energy",
  "ENG-1.B.1, near verbatim: all ecosystems depend on a continuous inflow of high-quality energy. The word continuous is part of the claim, which rules out a single initial pulse."),
 ("structure and its function of transferring matter",
  "ENG-1.B.1, near verbatim: the inflow maintains an ecosystem's structure and function of transferring matter between the environment and organisms via biogeochemical cycles."),
 ("The conservation of matter",
  "ENG-1.B.2, near verbatim: biogeochemical cycles are essential for life and each cycle demonstrates the conservation of matter."),
 ("essential for life",
  "ENG-1.B.2 states plainly that biogeochemical cycles are essential for life, and ENG-1.B.1 keeps the inflow of energy as a separate requirement rather than one the cycles can replace."),
 ("producers in the lowest trophic levels and then upward",
  "ENG-1.B.3, near verbatim: in terrestrial and near-surface marine communities, energy flows from the sun to producers in the lowest trophic levels and then upward to higher trophic levels."),
 ("Producers",
  "ENG-1.B.3 states that energy flows from the sun to producers in the lowest trophic levels and then upward, which places producers at the bottom of the sequence it describes."),
 ("Terrestrial and near-surface marine communities",
  "ENG-1.B.3 opens with the phrase 'in terrestrial and near-surface marine communities', so the scope of the statement is written into the framework's own wording."),
 ("received less energy lost more of their living mass",
  "Recomputed in q8 above: living mass retained rises with the light supplied and is near zero in the unlit chamber. ENG-1.B.1 states that all ecosystems depend on a continuous inflow of high-quality energy to maintain their structure."),
 ("none is unaccounted for",
  "Recomputed in q9 above: the outflow plus the increase in storage reproduces the inflow exactly. ENG-1.B.2 states that each biogeochemical cycle demonstrates the conservation of matter."),
 ("accounted for by the carbon returned",
  "Recomputed in q10 above: the carbon returned plus the carbon added to wood and soil reproduces the intake exactly, which is what ENG-1.B.2's conservation of matter looks like in a budget."),
 ("reduced the mass of producers and of consumers together",
  "Recomputed in q11 above: both the producer column and the consumer column fall as the sunlight column falls. ENG-1.B.3 has energy flow from the sun to producers and then upward, so restricting the sun restricts what reaches the levels above."),
 ("a small part of what arrived",
  "Recomputed in q12 above: arriving sunlight and captured energy rise together while capture stays below five percent of arrival. ENG-1.B.3 makes the sun the source producers draw on and ENG-1.B.1 makes the inflow continuous rather than complete."),
 ("energy must be supplied continuously from outside",
  "ENG-1.B.2 puts matter in cycles that demonstrate its conservation, while ENG-1.B.1 makes an ecosystem depend on a continuous INFLOW of high-quality energy, which is not the description of something that cycles."),
 ("depend on a continuous inflow of high-quality energy",
  "ENG-1.B.1 states that all ecosystems depend on a continuous inflow of high-quality energy in order to maintain their structure and function, so removing the inflow removes what maintains the structure."),
 ("obtains its energy from sunlight",
  "Recomputed in q15 above: exactly one of the four organisms is stated to draw its energy from sunlight. ENG-1.B.3 places producers in the lowest trophic levels and has energy flow from the sun to them and then upward."),
 ("Sunlight, then Organism 1",
  "Recomputed in q16 above from the feeding relationships the table states outright. ENG-1.B.3 gives the direction: from the sun to producers in the lowest trophic levels and then upward to higher trophic levels."),
 ("fell as the inflow of material fell",
  "Recomputed in q17 above: the inflow column and the living-mass column fall together across the record. ENG-1.B.1 states that all ecosystems depend on a continuous inflow of high-quality energy to maintain their structure and function."),
 ("neither created nor destroyed",
  "ENG-1.B.2 states that each biogeochemical cycle demonstrates the conservation of matter, which is precisely the claim that matter is neither created nor destroyed as it moves between reservoirs."),
 ("Everything that entered is accounted for",
  "Recomputed in q19 above: the outflow plus the material retained reproduces the inflow exactly, which is what ENG-1.B.2's conservation of matter looks like in a closing budget."),
 ("in a usable form supplied from outside",
  "ENG-1.B.1 specifies a continuous inflow of HIGH-QUALITY energy as what maintains an ecosystem's structure and function, so both the continuity and the quality of the supply are conditions the framework sets."),
 ("Energy enters the community at the producers",
  "ENG-1.B.3 states that energy flows from the sun to producers in the lowest trophic levels and then upward to higher trophic levels, so the producers are the point of entry for everything above them."),
 ("inputs equal the outputs plus the change",
  "ENG-1.B.2 states that each biogeochemical cycle demonstrates the conservation of matter, and conservation is shown by a budget that closes rather than by a single standing measurement or an inventory of places."),
 ("continuous supply of energy from outside",
  "ENG-1.B.1 states the dependence on a continuous inflow of high-quality energy and ENG-1.B.2 states that each biogeochemical cycle demonstrates the conservation of matter, so the two statements concern different quantities."),
 ("more energy entering at its producers",
  "ENG-1.B.3 states that energy flows from the sun to producers in the lowest trophic levels and then upward, so a larger supply at the source is a larger supply at the point of entry."),
 ("maintains both the structure and the function",
  "ENG-1.B.1 places both in one clause: the inflow of high-quality energy maintains an ecosystem's structure AND its function of transferring matter between the environment and organisms via biogeochemical cycles."),
 ("Each biogeochemical cycle demonstrates the conservation of matter",
  "Large flows in and out that leave the standing amount unchanged is a balance of inputs against outputs, and ENG-1.B.2 states that each biogeochemical cycle demonstrates the conservation of matter."),
 ("rather than for every community on Earth",
  "ENG-1.B.3 opens with a clause naming terrestrial and near-surface marine communities, and a clause of that kind states the scope of the sentence that follows it."),
 ("indefinitely without any energy entering",
  "ENG-1.B.1 makes the dependence on a continuous inflow universal across ecosystems, so the keyed statement contradicts it, while each rejected option restates part of ENG-1.B.1 or ENG-1.B.3."),
 ("becomes harder to maintain",
  "ENG-1.B.3 puts the producers at the point where energy enters and sends it upward, and ENG-1.B.1 makes the continuous inflow what maintains an ecosystem's structure and function, so reducing the inflow acts on both at once."),
 ("Energy must keep arriving from outside",
  "ENG-1.B.1 requires a continuous inflow of high-quality energy from outside, while ENG-1.B.2 states that each biogeochemical cycle demonstrates the conservation of matter, so the two quantities behave differently."),
]

TABLE_CHECKS = {8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 15: q15, 16: q16, 17: q17, 19: q19}


def _selftest():
    """Negative control: every gate below must FAIL when its input is corrupted."""
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("e1_9_mutant")
        mod.TOPIC = e1_9.TOPIC
        mod.QUESTIONS = copy.deepcopy(e1_9.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[4]["ans"] = 2

    def break_anchor(mod, claims):
        claims[6] = ("no such phrase anywhere in the module", claims[6][1])

    def corrupt_budget(mod, claims):
        # break the nitrogen budget so it no longer closes
        mod.QUESTIONS[8]["table"] = dict(
            headers=e1_9._T_MATTER["headers"],
            rows=[[k, ("70" if k.startswith("Nitrogen leaving") else v)]
                  for k, v in e1_9._T_MATTER["rows"]])

    def corrupt_table(mod, claims):
        # let the unlit chamber retain the most living mass
        mod.QUESTIONS[7]["table"] = dict(
            headers=e1_9._T_DARK["headers"],
            rows=[[c, h, ("99" if h == "0" else v)]
                  for c, h, v in e1_9._T_DARK["rows"]])

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[2]["choices"][4] = mod.QUESTIONS[2]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[13]["why"] = "It just is."

    def letter_reference(mod, claims):
        mod.QUESTIONS[21]["why"] = ("Option B is wrong because the framework says so and "
                                    "the rest of the reasoning follows from that.")

    def latex_slips_in(mod, claims):
        mod.QUESTIONS[0]["choices"][3] = "A single pulse of \\frac{1}{2} the energy"
        style(mod)

    def range_slips_in(mod, claims):
        mod.QUESTIONS[3]["q"] = "Over 1950-1970 how did the framework describe biogeochemical cycles?"
        style(mod)

    print("negative controls:")
    must_fail("a backslash macro in a choice", latex_slips_in)
    must_fail("a digit-hyphen-digit range in a stem", range_slips_in)
    must_fail("key moved off its anchor", move_key)
    must_fail("anchor no longer in the keyed choice", break_anchor)
    must_fail("a matter budget that no longer closes", corrupt_budget)
    must_fail("table value corrupted so the keyed conclusion is false", corrupt_table)
    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a why reduced below the minimum", thin_why)
    must_fail("a why naming an option by letter", letter_reference)
    print("all negative controls raised as required.")


import e1_9  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(e1_9)
cg.check(e1_9, CLAIMS, table_checks=TABLE_CHECKS)
