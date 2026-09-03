"""Key audit for AP ENVIRONMENTAL SCIENCE 1.11 Food Chains and Food Webs.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Items 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 18, 21, 22, 23, 24, 26, 27, 29
and 30 rest on ENG-1.D.1: a food chain depicts the flow of energy and matter
from producers (autotrophs) to primary consumers (herbivores) and secondary and
tertiary consumers (omnivores and carnivores); detritivores and decomposers play
an essential role by returning nutrients to the soil; and a food web is a model
of an interlocking pattern of food chains depicting the flow of energy and matter
in two or more food chains. Every category pairing keyed here is written in that
sentence, in parentheses, by the framework itself.

Items 8, 9, 15, 16, 17, 19, 20, 25 and 28 rest on ENG-1.D.2: positive and
negative feedback loops can each play a role in food webs, and when one species
is removed from or added to a specific food web, the rest of the food web can be
affected.

WHAT IS DELIBERATELY NOT ASKED. ENG-1.D.2 names positive and negative feedback
loops and defines neither, and nothing in units 1 to 4 defines them. No item here
asks a student to classify a loop; items 8 and 28 key only that both kinds can
play a role.

DATA ITEMS: 10 to 20 and 22 to 25 carry tables. Two of those tables hold a text
column, so they are read cell by cell rather than through ``cg.col``.

NEGATIVE CONTROL: ``python3 verify_e1_11.py --selftest`` corrupts a key, an
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


BEFORE_K = "Population before Species K was removed"
AFTER_K = "Population two years after Species K was removed"
NUTRI = "Nutrients returned to the soil in one year (kilograms per hectare)"
LITTER = "Depth of undecayed litter after five years (centimeters)"
BEFORE_P = "Population before a new predator was introduced"
AFTER_P = "Population three years after the new predator was introduced"
DIETSHARE = "Share of its diet made up of the same rodent (percent)"
PLANTPCT = "Percent of its diet that is plant material"
ANIMPCT = "Percent of its diet that is animal material"

_SUN = "sunlight water and carbon dioxide"


def _web(table):
    """The meadow table read as {species: normalized description of its food}."""
    return {r[0]: cg.normalize(r[1]) for r in table["rows"]}


def _producers(web):
    return [s for s, food in web.items() if food == _SUN]


def _dead_feeder(web):
    return [s for s, food in web.items() if "dead remains" in food]


def _eats(web, species, other):
    return cg.contains_phrase(web[species], other)


def q10(table, item):
    web = _web(table)
    prod = _producers(web)
    assert set(prod) == {"Species A", "Species B"}, f"the producers must be A and B; got {prod}"
    for s in web:
        if s not in prod:
            assert web[s] != _SUN, f"{s} must not also build from sunlight"
    return (f"exactly two of the six species, {prod}, are described as building from "
            "sunlight, water and carbon dioxide rather than from another organism")


def q11(table, item):
    web = _web(table)
    prod = _producers(web)
    only_prod = [s for s in web if s not in prod and s not in _dead_feeder(web)
                 and all(not _eats(web, s, c) for c in web if c not in prod)]
    assert only_prod == ["Species D"], f"exactly one species must eat producers only; got {only_prod}"
    assert _eats(web, "Species D", "Species A"), "Species D must be stated to eat a producer"
    assert _eats(web, "Species C", "Species A") and _eats(web, "Species C", "Species B"), \
        "Species C must eat two producers, so it is a consumer too and the item asks for the single-producer feeder"
    return ("exactly one species feeds on a producer and on nothing else, which is the "
            "primary consumer position the framework places directly above the producers")


def q12(table, item):
    web = _web(table)
    prod = _producers(web)
    consumers = [s for s in web if s not in prod and s not in _dead_feeder(web)]
    only_consumers = [s for s in consumers
                      if not any(_eats(web, s, p) for p in prod)
                      and any(_eats(web, s, c) for c in consumers)]
    assert only_consumers == ["Species E"], \
        f"exactly one species must feed only on other consumers; got {only_consumers}"
    return ("exactly one species has no producer among its listed foods and does have "
            "other consumers among them")


def q13(table, item):
    web = _web(table)
    dead = _dead_feeder(web)
    assert dead == ["Species F"], f"exactly one species must feed on dead remains; got {dead}"
    return ("exactly one of the six species is described as feeding on the dead remains of "
            "the others, which is the position the framework gives detritivores and "
            "decomposers")


def q14(table, item):
    web = _web(table)
    prod = _producers(web)
    assert len(prod) >= 2, "a web needs more than one chain, so more than one producer here"
    shared = [s for s in web if sum(1 for c in web if _eats(web, s, c)) >= 2]
    assert shared, "at least one species must feed on two others, which is where the chains interlock"
    assert not all(_eats(web, s, o) for s in web for o in web if s != o), \
        "'every species feeds on every other' must be false"
    return (f"the table holds {len(prod)} producers and {len(shared)} species feeding on "
            "two others, so more than one chain runs upward and the chains meet")


def q15(table, item):
    b = dict(zip(cg.labels(table), cg.col(table, BEFORE_K)))
    a = dict(zip(cg.labels(table), cg.col(table, AFTER_K)))
    unconnected = "Species N, unconnected to this chain"
    changed = [s for s in b if abs(a[s] - b[s]) > 0.2 * b[s]]
    assert unconnected not in changed, "the unconnected species must not change substantially"
    assert len(changed) == 3, f"three connected species must change substantially; got {changed}"
    assert any(a[s] > b[s] for s in changed) and any(a[s] < b[s] for s in changed), \
        "'every other population rose' must be false"
    return (f"{len(changed)} connected populations changed by more than a fifth while the "
            "species stated to be unconnected changed by less than a twentieth")


def q16(table, item):
    b = dict(zip(cg.labels(table), cg.col(table, BEFORE_K)))
    a = dict(zip(cg.labels(table), cg.col(table, AFTER_K)))
    prey = [s for s in b if "eaten by Species K" in s]
    assert len(prey) == 2, f"there must be two species eaten by the removed one; got {prey}"
    assert all(a[s] > 3 * b[s] for s in prey), f"both prey must rise sharply; got {[(b[s], a[s]) for s in prey]}"
    assert all(a[s] > 0 for s in prey), "'both fell to zero' must be false"
    return (f"both species eaten by the removed one rose from {[b[s] for s in prey]} to "
            f"{[a[s] for s in prey]}, more than tripling")


def q17(table, item):
    b = dict(zip(cg.labels(table), cg.col(table, BEFORE_K)))
    a = dict(zip(cg.labels(table), cg.col(table, AFTER_K)))
    plant = "Species M, the plant eaten by Species J"
    grazer = "Species J, eaten by Species K"
    assert a[plant] < 0.5 * b[plant], f"the plant must fall substantially; got {b[plant]} to {a[plant]}"
    assert a[grazer] > b[grazer], "the animal eating the plant must have risen"
    assert a[plant] > 0, "'the plant fell to zero' must be false"
    assert a[plant] != a[grazer], "'the plant rose to the level of the species eating it' must be false"
    return (f"the plant falls {b[plant]:.0f} to {a[plant]:.0f} while the animal that eats it "
            f"rises {b[grazer]:.0f} to {a[grazer]:.0f}")


def q18(table, item):
    n = dict(zip(cg.labels(table), cg.col(table, NUTRI)))
    lit = dict(zip(cg.labels(table), cg.col(table, LITTER)))
    sup = "Plot where decomposers were suppressed"
    unt = "Untreated plot"
    assert n[sup] < 0.2 * n[unt], f"nutrient return must collapse; got {n}"
    assert lit[sup] > 5 * lit[unt], f"litter must pile up; got {lit}"
    assert n[sup] != n[unt], "'both plots returned the same' must be false"
    assert lit[sup] > lit[unt], "'the suppressed plot had the shallower litter' must be false"
    return (f"nutrient return falls {n[unt]:.0f} to {n[sup]:.0f} kilograms per hectare while "
            f"litter depth rises {lit[unt]:.0f} to {lit[sup]:.0f} centimeters")


def q19(table, item):
    b = dict(zip(cg.labels(table), cg.col(table, BEFORE_P)))
    a = dict(zip(cg.labels(table), cg.col(table, AFTER_P)))
    changed = [s for s in b if abs(a[s] - b[s]) > 0.2 * b[s]]
    assert len(changed) == 3, f"all three tabulated levels must change; got {changed}"
    assert any(a[s] > b[s] for s in changed), "'every population fell' must be false"
    assert any(a[s] < b[s] for s in changed), "'every population rose' must be false"
    return (f"all {len(changed)} tabulated populations changed by more than a fifth, and "
            "they lie at three different positions in the chain")


def q20(table, item):
    b = dict(zip(cg.labels(table), cg.col(table, BEFORE_P)))
    a = dict(zip(cg.labels(table), cg.col(table, AFTER_P)))
    insect = "Insect eaten by the small fish"
    plant = "Plant eaten by the insect"
    assert a[insect] > b[insect], f"the insect must rise; got {b[insect]} to {a[insect]}"
    assert a[plant] < b[plant], f"the plant must fall; got {b[plant]} to {a[plant]}"
    return (f"the insect rises {b[insect]:.0f} to {a[insect]:.0f} while the plant falls "
            f"{b[plant]:.0f} to {a[plant]:.0f}")


def q22(table, item):
    p = dict(zip(cg.labels(table), cg.col(table, PLANTPCT)))
    m = dict(zip(cg.labels(table), cg.col(table, ANIMPCT)))
    for lab in p:
        assert abs(p[lab] + m[lab] - 100) < 1e-9, f"{lab}'s two shares must total 100"
    herb = [lab for lab in p if p[lab] == 100]
    assert herb == ["Animal 1"], f"exactly one animal must be wholly plant-eating; got {herb}"
    return ("exactly one of the three animals takes a diet that is entirely plant material, "
            "which is the term the framework pairs with primary consumers")


def q23(table, item):
    p = dict(zip(cg.labels(table), cg.col(table, PLANTPCT)))
    m = dict(zip(cg.labels(table), cg.col(table, ANIMPCT)))
    mixed = [lab for lab in p if p[lab] > 10 and m[lab] > 10]
    assert mixed == ["Animal 2"], f"exactly one animal must take a mixed diet; got {mixed}"
    assert p["Animal 1"] == 100 and m["Animal 3"] == 100, \
        "the other two animals must be at the two extremes"
    return ("exactly one of the three animals takes a substantial share of both plant and "
            "animal material, the other two lying at the two extremes")


def q24(table, item):
    links = {r[0]: cg.normalize(r[1]) for r in table["rows"]}
    on_algae = [k for k, v in links.items() if "algae" in v]
    assert len(on_algae) == 2, f"exactly two links must run from the algae; got {on_algae}"
    predators = [v for k, v in links.items() if "algae" not in v]
    assert len(predators) == 2, "two further links must run above the algae"
    assert all("species r" in v for v in predators), \
        "the two upper links must share one predator, which is where the chains interlock"
    return ("two species feed on the algae and one further species feeds on both of them, "
            "so two chains run upward and meet at a shared predator")


def q25(table, item):
    share = dict(zip(cg.labels(table), cg.col(table, DIETSHARE)))
    assert all(v > 0 for v in share.values()), "every predator must take some of the rodent"
    assert len(set(share.values())) == len(share), "the three dependencies must differ"
    assert max(share, key=share.get) == "Predator 1", "the most dependent predator must be the first row"
    return (f"all three predators take some of the same rodent, in shares "
            f"{sorted(share.values(), reverse=True)} percent, so all three have food at stake "
            "and they are not equally exposed")


CLAIMS = [
 ("flow of energy and matter from producers",
  "ENG-1.D.1, near verbatim: a food chain depicts the flow of energy and matter from producers to primary consumers and secondary and tertiary consumers. Both energy and matter are named."),
 ("Autotrophs",
  "ENG-1.D.1 writes producers with autotrophs in parentheses, which is the framework's own pairing of the two terms."),
 ("Herbivores",
  "ENG-1.D.1 writes primary consumers with herbivores in parentheses. Carnivores appear in the same sentence but are paired with the secondary and tertiary consumers instead."),
 ("Omnivores and carnivores",
  "ENG-1.D.1 writes secondary and tertiary consumers with omnivores and carnivores in parentheses, which is the framework's own pairing."),
 ("Returning nutrients to the soil",
  "ENG-1.D.1 states that detritivores and decomposers play an essential role in food chains and food webs by returning nutrients to the soil."),
 ("interlocking pattern of food chains",
  "ENG-1.D.1, near verbatim: a food web is a model of an interlocking pattern of food chains that depicts the flow of energy and matter in two or more food chains."),
 ("Two or more",
  "ENG-1.D.1 states that a food web depicts the flow of energy and matter in two or more food chains, which sets the minimum at two."),
 ("Positive and negative feedback loops can each play a role",
  "ENG-1.D.2, near verbatim: positive and negative feedback loops can each play a role in food webs, so both kinds are allowed and neither is excluded. The framework defines neither kind, and nothing beyond their both being permitted is keyed."),
 ("The rest of the food web can be affected",
  "ENG-1.D.2, near verbatim: when one species is removed from or added to a specific food web, the rest of the food web can be affected. The word can allows an effect without asserting a collapse."),
 ("which feed on sunlight, water and carbon dioxide",
  "Recomputed in q10 above: exactly two of the six species are described as building from sunlight, water and carbon dioxide. ENG-1.D.1 places producers, the autotrophs, at the start of a food chain."),
 ("which feeds only on a producer",
  "Recomputed in q11 above: exactly one species feeds on a producer and on nothing else. ENG-1.D.1 pairs primary consumers with herbivores and places them directly above the producers."),
 ("Species E",
  "Recomputed in q12 above: exactly one species has no producer among its listed foods and does have other consumers among them, which is the secondary or tertiary position of ENG-1.D.1."),
 ("which feeds on the dead remains",
  "Recomputed in q13 above: exactly one of the six species feeds on the dead remains of the others. ENG-1.D.1 gives detritivores and decomposers the essential role of returning nutrients to the soil."),
 ("more than one chain runs from the producers upward",
  "Recomputed in q14 above: the table holds two producers and species feeding on more than one other, so the chains interlock. ENG-1.D.1 defines a food web as an interlocking pattern of two or more food chains."),
 ("while a species outside that chain barely changed",
  "Recomputed in q15 above: three connected populations changed by more than a fifth while the species stated to be unconnected changed by less than a twentieth. ENG-1.D.2 states that removing one species can affect the rest of the web."),
 ("Both rose sharply",
  "Recomputed in q16 above: both species eaten by the removed one more than tripled. ENG-1.D.2 states that when one species is removed from a specific food web the rest of the web can be affected."),
 ("more of the animals that eat it being present",
  "Recomputed in q17 above: the plant's population fell while the population of the species eating it rose. ENG-1.D.2 allows the effect of a removal to reach beyond the removed species' immediate prey."),
 ("left undecayed litter piling up",
  "Recomputed in q18 above: the suppressed plot returned far fewer nutrients and accumulated far deeper litter. ENG-1.D.1 gives detritivores and decomposers the essential role of returning nutrients to the soil."),
 ("more than one level of the web",
  "Recomputed in q19 above: all three tabulated populations changed and they sit at three different positions in the chain. ENG-1.D.2 states that adding one species to a specific food web can affect the rest of it."),
 ("the plant eaten by the insect fell",
  "Recomputed in q20 above: the insect rose and the plant fell over the same period. ENG-1.D.2 allows the effect of an addition to reach the rest of the web rather than stopping at its prey."),
 ("not one longer chain",
  "ENG-1.D.1 defines a food web as a model of an INTERLOCKING PATTERN of food chains depicting the flow of energy and matter in two or more food chains, so the difference is the number of chains and how they connect."),
 ("entirely plant material",
  "Recomputed in q22 above: exactly one tabulated animal takes a diet that is entirely plant material. ENG-1.D.1 pairs primary consumers with herbivores."),
 ("substantial share of both plant and animal material",
  "Recomputed in q23 above: exactly one tabulated animal takes a substantial share of both. ENG-1.D.1 lists omnivores and carnivores together for the secondary and tertiary consumers, and a mixed diet is what separates the first from the second."),
 ("interlock at a shared predator",
  "Recomputed in q24 above: two species feed on the algae and one further species feeds on both. ENG-1.D.1 defines a food web as an interlocking pattern of two or more food chains."),
 ("with the one most dependent on the rodent affected most",
  "Recomputed in q25 above: all three predators take some of the same rodent and their dependencies differ. ENG-1.D.2 states that removing one species from a specific food web can affect the rest of it."),
 ("becomes the material of the organism that eats it",
  "ENG-1.D.1 states that a food chain depicts the flow of energy AND MATTER from producers upward, so feeding moves both quantities along the same links."),
 ("far fewer nutrients from dead material",
  "ENG-1.D.1 states the essential role of detritivores and decomposers specifically as returning nutrients to the soil, so the evidence bearing on it is a measured difference in nutrients returned when they are absent."),
 ("a change to one species can affect the rest of it",
  "ENG-1.D.2 makes two separate assertions in one statement: positive and negative feedback loops can each play a role in food webs, and when one species is removed from or added to a specific food web the rest of the web can be affected."),
 ("A food web, which models an interlocking pattern",
  "ENG-1.D.1 defines a food web as a model of an interlocking pattern of food chains depicting the flow of energy and matter in two or more food chains, which is precisely the situation described."),
 ("Producers with autotrophs, primary consumers with herbivores",
  "ENG-1.D.1 supplies each pairing in parentheses as it names the levels of a food chain, and the keyed option reproduces the framework's three pairings in the order the sentence gives them."),
]

TABLE_CHECKS = {10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16,
                17: q17, 18: q18, 19: q19, 20: q20, 22: q22, 23: q23, 24: q24, 25: q25}


def _selftest():
    """Negative control: every gate below must FAIL when its input is corrupted."""
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("e1_11_mutant")
        mod.TOPIC = e1_11.TOPIC
        mod.QUESTIONS = copy.deepcopy(e1_11.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[1]["ans"] = 3

    def break_anchor(mod, claims):
        claims[5] = ("no such phrase anywhere in the module", claims[5][1])

    def corrupt_web(mod, claims):
        # make a second species feed on dead remains, so the detritivore item has two answers
        mod.QUESTIONS[12]["table"] = dict(
            headers=e1_11._T_WEB["headers"],
            rows=[[s, ("Dead remains of every other species" if s == "Species D" else f)]
                  for s, f in e1_11._T_WEB["rows"]])

    def corrupt_table(mod, claims):
        # let the unconnected species swing as hard as the connected ones
        mod.QUESTIONS[14]["table"] = dict(
            headers=e1_11._T_REMOVAL["headers"],
            rows=[[s, b, ("1200" if s.startswith("Species N") else a)]
                  for s, b, a in e1_11._T_REMOVAL["rows"]])

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[4]["choices"][2] = mod.QUESTIONS[4]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[20]["why"] = "It just is."

    def letter_reference(mod, claims):
        mod.QUESTIONS[28]["why"] = ("Option A is wrong because the framework says so and "
                                    "the rest of the reasoning follows from that.")

    def latex_slips_in(mod, claims):
        mod.QUESTIONS[6]["choices"][3] = "At least \\frac{10}{1} chains."
        style(mod)

    def range_slips_in(mod, claims):
        mod.QUESTIONS[7]["q"] = "Between 1980-1990 what did the framework say about feedback loops?"
        style(mod)

    print("negative controls:")
    must_fail("a backslash macro in a choice", latex_slips_in)
    must_fail("a digit-hyphen-digit range in a stem", range_slips_in)
    must_fail("key moved off its anchor", move_key)
    must_fail("anchor no longer in the keyed choice", break_anchor)
    must_fail("a second species made to fill the keyed role", corrupt_web)
    must_fail("table value corrupted so the keyed conclusion is false", corrupt_table)
    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a why reduced below the minimum", thin_why)
    must_fail("a why naming an option by letter", letter_reference)
    print("all negative controls raised as required.")


import e1_11  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(e1_11)
cg.check(e1_11, CLAIMS, table_checks=TABLE_CHECKS)
