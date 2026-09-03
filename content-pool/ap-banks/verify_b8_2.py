"""Key audit for AP BIOLOGY 8.2 Energy Flow Through Ecosystems.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor, so an off-by-one key stops matching; the
claim states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Items 1 to 25 are keyed to sentences the CED prints, one apiece: EK 8.2.A.1
(the four uses of energy; endotherms against ectotherms; net gain and net
loss), EK 8.2.A.2 (reproductive strategies and the alternation of asexual and
sexual reproduction), EK 8.2.B.1 (the ecological levels of organization),
EK 8.2.B.2 (energy FLOWS while matter CYCLES; conservation of matter; the
cycles are interdependent), EK 8.2.B.3 (abiotic and biotic reservoirs and the
processes between them), EK 8.2.B.4 to EK 8.2.B.7 (the hydrologic, carbon,
nitrogen and phosphorus cycles, each with the framework's own reservoirs and
processes), EK 8.2.C.1 and EK 8.2.C.2 (energy availability, population size,
disruption, and the trophic levels), and EK 8.2.D.1 and EK 8.2.D.2 (autotrophs,
chemosynthesis in the absence of oxygen, and the heterotroph list).

Items 26 to 30 carry a table. Every number a key states is RECOMPUTED below
from that table alone. The trophic ratio is computed from the biomass column
rather than asserted: THE CED PRINTS NO FIXED TRANSFER PERCENTAGE between
trophic levels, so the item can only be a question about its own stimulus, and
the check confirms the ratio is in fact constant down the column before
accepting a single-ratio key.

NEGATIVE CONTROL. Moving any key, or changing any table cell the keys depend
on, makes this file raise; confirmed by running exactly that.
"""
import re

import cg_check as cg
import b8_2

QS = b8_2.QUESTIONS
T_BUDGET = b8_2._T_BUDGET
T_TROPHIC = b8_2._T_TROPHIC
T_PROCESSES = b8_2._T_PROCESSES

MASS = "Change in total body mass over the study, in grams"
OFFSPRING = "Mean number of offspring produced per individual"
BIOMASS = "Biomass in a hypothetical study area, in kilograms"
CYCLE = "Cycle in which the framework lists this process"

NUMBER_WORDS = ["Zero", "One", "Two", "Three", "Four", "Five", "Six"]


def keyed(item):
    return item["choices"][item["ans"]]


def raw(table, row_label, header):
    j = [cg.normalize(h) for h in table["headers"]].index(cg.normalize(header))
    i = [cg.normalize(lab) for lab in cg.labels(table)].index(cg.normalize(row_label))
    return str(table["rows"][i][j])


def _budget(table):
    """The rows with a net gain, a near balance and a net loss, each unique."""
    mass = {lab: cg.cell(table, lab, MASS) for lab in cg.labels(table)}
    off = {lab: cg.cell(table, lab, OFFSPRING) for lab in cg.labels(table)}
    gains = [lab for lab, v in mass.items() if v > 0]
    losses = [lab for lab, v in mass.items() if v < 0]
    assert len(losses) == 1, f"exactly one row must record a net loss of mass; {losses} do"
    assert gains, "at least one row must record a gain in mass"
    best = max(mass, key=mass.get)
    assert sorted(mass.values())[-2] < mass[best], \
        f"the largest gain in mass must be unique; the column reads {mass}"
    assert sorted(off.values())[-2] < max(off.values()), \
        f"the largest reproductive output must be unique; the column reads {off}"
    assert sorted(off.values())[1] > min(off.values()), \
        f"the smallest reproductive output must be unique; the column reads {off}"
    assert max(off, key=off.get) == best, \
        "the largest gain in mass must also carry the largest reproductive output"
    assert min(off, key=off.get) == losses[0], \
        "the row losing mass must also carry the smallest reproductive output"
    return mass, off, best, losses[0]


def q26(table, item):
    mass, off, best, _ = _budget(table)
    assert cg.contains_phrase(keyed(item), best), \
        f"q26 key {keyed(item)!r} but the net-gain row is {best}"
    return (f"mass changes are {mass} and offspring {off}; {best} holds the largest of both, "
            "which is what a net gain predicts")


def q27(table, item):
    mass, off, _, loser = _budget(table)
    assert mass[loser] < 0 and off[loser] == min(off.values()), \
        "the net-loss row must record both a fall in mass and the lowest reproductive output"
    assert cg.contains_phrase(keyed(item), "loss of body mass"), \
        f"q27 key {keyed(item)!r} does not describe a loss of body mass"
    assert cg.contains_phrase(keyed(item), "lowest reproductive output"), \
        f"q27 key {keyed(item)!r} does not describe the lowest reproductive output"
    return f"{loser} records {mass[loser]} grams and {off[loser]} offspring, the lowest of both"


def q28(table, item):
    levels = cg.col(table, BIOMASS)
    assert all(v > 0 for v in levels), "every biomass must be positive"
    ratios = [a / b for a, b in zip(levels, levels[1:])]
    assert len({round(r, 9) for r in ratios}) == 1, \
        f"a single ratio can only be keyed if the column is a constant ladder; ratios are {ratios}"
    r = ratios[0]
    assert abs(r - round(r)) < 1e-9, "the ratio must be whole for a calculator-free item"
    assert keyed(item) == f"{int(round(r))} to 1", \
        f"q28 key {keyed(item)!r} but the constant ratio down the column is {r}"
    return f"the biomass column reads {levels}, a constant ratio of {int(round(r))} to 1 at every step"


def q29(table, item):
    levels = cg.col(table, BIOMASS)
    labs = cg.labels(table)
    assert cg.contains_phrase(labs[0], "producers"), \
        f"the first row must be the producers; it reads {labs[0]}"
    assert all(a > b for a, b in zip(levels, levels[1:])), \
        f"every level above the producers must hold less biomass; the column reads {levels}"
    assert len(labs) > 1, "the key concerns levels other than the producers"
    return (f"producers hold {int(levels[0])} kilograms and each level above holds less, "
            f"down to {int(levels[-1])}, so the levels above depend on what the producers supply")


# The four biogeochemical cycles EK 8.2.B.4 to EK 8.2.B.7 name. A cell holding
# anything else is a defect, not a value: matching the column loosely would let
# an edited cell pass, and an under-matching check is worse than none.
_CYCLES = {"hydrologic", "carbon", "nitrogen", "phosphorus"}


def q30(table, item):
    counts = {}
    for lab in cg.labels(table):
        c = cg.normalize(raw(table, lab, CYCLE))
        assert c in _CYCLES, f"{lab}: the cycle column reads {c!r}, not one of {sorted(_CYCLES)}"
        counts[c] = counts.get(c, 0) + 1
    named = [c for c in counts if cg.contains_phrase(item["q"], c)]
    assert len(named) == 1, f"the stem names cycles {named}; it must name exactly one"
    n = counts[named[0]]
    assert keyed(item) == NUMBER_WORDS[n], \
        f"q30 key {keyed(item)!r} but the table assigns {n} rows to the {named[0]} cycle"
    assert len(counts) > 1, "the table must cover more than one cycle for the count to mean anything"
    return f"the cycle column reads {counts}; the cycle the stem names carries {n} of the rows"


TABLE_CHECKS = {26: q26, 27: q27, 28: q28, 29: q29, 30: q30}


CLAIMS = [
 ("Organize, grow, reproduce, and maintain homeostasis",
  "EK 8.2.A.1 states that organisms use energy to organize, grow, reproduce, and maintain homeostasis. Each distractor keeps one item of that list and discards the others."),
 ("thermal energy generated by their own metabolism",
  "EK 8.2.A.1 states that endotherms use thermal energy generated by metabolism to maintain homeostatic body temperatures. Moving into sun or shade and aggregating are the behavioural routes the same statement assigns to ectotherms."),
 ("lack efficient internal mechanisms",
  "EK 8.2.A.1 states that ectotherms lack efficient internal mechanisms for maintaining body temperature, ALTHOUGH they may regulate their temperature behaviorally. That concession is why denying them any influence over their temperature is wrong."),
 ("Moving into the sun or shade, or aggregating with other individuals",
  "EK 8.2.A.1 names exactly those two behavioural routes by which an ectotherm may regulate its temperature. Generating heat internally is what the same statement assigns to endotherms."),
 ("Energy storage, growth of the organism, and increased reproductive output",
  "EK 8.2.A.1 states that a net gain in energy results in energy storage, the growth of an organism, and increased reproductive output. The nearest distractor is the same statement's account of a net loss."),
 ("Loss of mass, a decrease in reproductive output, and eventually death",
  "EK 8.2.A.1 states that a net loss of energy results in loss of mass, a decrease in reproductive output, and, eventually, the death of an organism. The word eventually places death last rather than first."),
 ("some alternate between asexual and sexual reproduction",
  "EK 8.2.A.2 states that different organisms use various reproductive strategies in response to energy availability and that some alternate between asexual and sexual reproduction in response to it."),
 ("Populations, communities, ecosystems, and biomes",
  "EK 8.2.B.1 states that ecological levels of organization include populations, communities, ecosystems, and biomes. The other lists name levels within an organism, trophic roles, parts of a cycle, or taxonomic ranks."),
 ("Energy flows through the ecosystem, while matter and nutrients cycle",
  "EK 8.2.B.2 states that energy flows through ecosystems while matter and nutrients cycle between the environment and organisms via biogeochemical cycles. The contrast between flowing and cycling is the whole content of the statement."),
 ("each demonstrates the conservation of matter, and they are interdependent",
  "EK 8.2.B.2 states all three properties: the cycles are essential for life, each demonstrates the conservation of matter, and the cycles are interdependent. Conservation of matter is why creation or destruction of matter is excluded."),
 ("Abiotic and biotic reservoirs, and processes that cycle matter between them",
  "EK 8.2.B.3 states that biogeochemical cycles include abiotic and biotic reservoirs as well as processes that cycle matter between reservoirs. Both kinds of reservoir and the processes are named together."),
 ("The atmosphere",
  "EK 8.2.B.4 names oceans, surface water, the atmosphere and living organisms as reservoirs of the hydrologic cycle. The distractors are reservoirs or forms belonging to the phosphorus, nitrogen and carbon cycles."),
 ("Transpiration",
  "EK 8.2.B.4 names evaporation, condensation, precipitation and transpiration as the processes of the hydrologic cycle. Nitrification and ammonification belong to the nitrogen cycle, combustion to the carbon cycle, weathering to the phosphorus cycle."),
 ("Photosynthesis, cellular respiration, decomposition, and combustion",
  "EK 8.2.B.5 states that at the highest levels of organization the carbon cycle simplifies into those four parts. The distractor lists are the hydrologic and nitrogen cycles, the phosphorus cycle, and the uses of energy in EK 8.2.A.1."),
 ("as carbohydrates and back into the atmosphere as carbon dioxide",
  "EK 8.2.B.5 states that carbon is recycled through the biosphere into organisms as carbohydrates and back into the atmosphere as carbon dioxide. Reversing the two forms is the error the nearest distractor carries."),
 ("Nitrogen fixation, assimilation, ammonification, nitrification, and denitrification",
  "EK 8.2.B.6 lists exactly those steps for the nitrogen cycle and adds that they are performed by microorganisms in the soil."),
 ("The atmosphere",
  "EK 8.2.B.6 states that the largest reservoir of nitrogen is the atmosphere. Rock is what EK 8.2.B.7 identifies as the source reservoir for phosphorus, which is why that distractor is offered."),
 ("ionizes to ammonium by acquiring hydrogen ions from the soil solution",
  "EK 8.2.B.6 states that in nitrogen fixation nitrogen gas is fixed into ammonia, which ionizes to ammonium by acquiring hydrogen ions from the soil solution. Returning nitrogen to the atmosphere is denitrification, a different step in the same list."),
 ("Weathering of rocks releases phosphate",
  "EK 8.2.B.7 states that the phosphorus cycle involves weathering rocks releasing phosphate into soil and groundwater. Fixation from the atmosphere belongs to nitrogen and combustion to carbon."),
 ("Decomposition of biomass, and excretion",
  "EK 8.2.B.7 states that phosphorus returns to the soil via decomposition of biomass, or excretion, and that phosphate can also be returned via decomposition of decaying organic matter. The distractors name processes of the hydrologic, nitrogen and carbon cycles."),
 ("A change in population size",
  "EK 8.2.C.1 states that changes in energy availability can result in changes in population size, and EK 8.2.C.2 adds that they can also result in disruptions to an ecosystem."),
 ("Producers; primary, secondary, tertiary, and quaternary consumers; and decomposers",
  "EK 8.2.C.2 gives exactly that list of trophic levels. Populations through biomes are the ECOLOGICAL LEVELS OF ORGANIZATION of EK 8.2.B.1, which is a different list and the distractor offered for it."),
 ("Physical or chemical sources in the environment",
  "EK 8.2.D.1 states that autotrophs capture energy from physical or chemical sources in the environment. Capturing energy in carbon compounds by consuming organic matter is what EK 8.2.D.2 assigns to heterotrophs."),
 ("small inorganic molecules, which can occur in the absence of oxygen",
  "EK 8.2.D.1 states that chemosynthetic organisms capture energy from small inorganic molecules present in their environment, which can occur in the absence of oxygen. They are autotrophs in that same statement."),
 ("Carnivores, herbivores, omnivores, decomposers, and scavengers",
  "EK 8.2.D.2 names those five as heterotrophs and states that they metabolize carbohydrates, lipids and proteins as sources of energy. Photosynthetic and chemosynthetic organisms are the autotrophs of EK 8.2.D.1."),
 ("more food than it uses",
  "EK 8.2.A.1 states that a net gain in energy results in energy storage, growth, and increased reproductive output. The table check above confirms that exactly one row carries both the largest gain in mass and the largest reproductive output."),
 ("loss of body mass together with the lowest reproductive output",
  "EK 8.2.A.1 states that a net loss of energy results in loss of mass and a decrease in reproductive output. The table check above confirms exactly one row records a negative change in mass and that the same row records the fewest offspring."),
 ("10 to 1",
  "Skill 5.A includes ratios. The table check above divides each level's biomass by the level below it, confirms the value is the same at every step before a single ratio may be keyed, and confirms it is whole. The CED prints no fixed transfer percentage, so this is a question about the stimulus and not about a remembered rule."),
 ("number and size of the other trophic levels could be affected",
  "EK 8.2.C.2 states that a change in the biomass or number of producers in a given geographic area can affect the number and size of other trophic levels. The table check above confirms that every level above the producers holds less biomass than the one below it."),
 ("Two",
  "EK 8.2.B.6 lists nitrogen fixation, assimilation, ammonification, nitrification and denitrification as steps of the nitrogen cycle. The table check above counts the rows the table assigns to the cycle the stem names and confirms more than one cycle appears in the column."),
]


# SCIENCE_BRIEF.md: Biology is exported untypeset, so a backslash macro or a
# dollar span would reach a student as literal characters, and a
# digit-hyphen-digit run reads as a subtraction. Explicit lookarounds, never \b.
_BANNED = [
    (re.compile(r"\\"), "a backslash: this bank carries no LaTeX"),
    (re.compile(r"\$"), "a dollar-delimited math span"),
    (re.compile(r"(?<![A-Za-z])\d+\s*-\s*\d+(?![A-Za-z])"), "a digit-hyphen-digit range"),
    (re.compile(r"\d\s*/\s*\d"), "a digit-slash-digit fraction"),
]

_FIGURE_TALK = re.compile(
    r"(?<![A-Za-z])(the (?:graph|figure|diagram|chart|pyramid|web) (?:shown|above|below)|"
    r"in the (?:graph|figure|diagram|chart|pyramid|web) (?:shown|above|below)|"
    r"shown in the (?:graph|figure|diagram|chart|pyramid|web))(?![A-Za-z])",
    re.IGNORECASE)


def style():
    hits = 0
    for i, item in enumerate(QS, 1):
        texts = [("stem", item["q"]), ("why", item["why"])]
        texts += [(f"choice {k}", c) for k, c in enumerate(item["choices"])]
        if item.get("table"):
            texts.append(("table", " | ".join(item["table"]["headers"])))
            texts += [("table", " | ".join(str(c) for c in r)) for r in item["table"]["rows"]]
        for where, text in texts:
            for pat, why_bad in _BANNED:
                m = pat.search(text)
                assert not m, f"q{i} {where} contains {m.group(0)!r}, {why_bad}"
                hits += 1
            m = _FIGURE_TALK.search(text)
            assert not m, (
                f"q{i} {where} says {m.group(0)!r}, promising a figure the bank cannot show"
            )
            hits += 1
    return hits


def main():
    n_style = style()
    cg.check(b8_2, CLAIMS, table_checks=TABLE_CHECKS)
    print(f"    {n_style} notation and figure-reference checks clean.")


main()
