"""Key audit for AP ENVIRONMENTAL SCIENCE 2.3 Island Biogeography.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
ERT-2.D.1  Island biogeography is the study of the ecological relationships and
           distribution of organisms on islands, and of these organisms'
           community structures.            -- items 1, 2, 11, 22, 26, 30
ERT-2.D.2  Islands have been colonized in the past by new species arriving from
           elsewhere.                        -- items 3, 13, 14, 15, 16, 25, 30
ERT-2.E.1  Many island species have evolved to be specialists versus
           generalists because of the limited resources, such as food and
           territory, on most islands. The long-term survival of specialists
           may be jeopardized if and when invasive species, typically
           generalists, are introduced and outcompete the specialists.
                              -- items 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20,
                                 21, 24, 27, 28, 29, 30

NAMED CHAIN, used once. Item 29 sets ERT-2.E.1 beside EIN-4.A.2 (invasive
species are often generalist, r-selected species and may therefore outcompete
native species for resources), which belongs to unit 9. The claim names the
chain rather than passing the outside statement off as this topic's own.

THE SWAP DISTRACTORS ARE THE HAZARD HERE. Specialist and generalist appear on
both sides of three items, so the anchors for items 6, 17 and 27 carry BOTH
clauses -- which kind the invader is AND which kind loses -- because either
clause alone matches the swapped distractor as readily as the key. That defect
was found once already in verify_e2_1.py and is not repeated.

WHAT IS DELIBERATELY NOT ASKED. The framework defines neither specialist nor
generalist, so no item asks a student to sort a species into one of the two.
It gives no species-area rule, no distance rule and no arrival-extinction
equilibrium, so where a table shows species rising with area or falling with
distance the keyed conclusion is a reading OF THAT TABLE and the claim says so.

DATA ITEMS: 11 to 23 carry tables. Every keyed conclusion is recomputed below
from that table alone, read by column header rather than by index.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and EVERY data table in turn, and requires each
corruption to raise BEFORE the real gate runs. ``python3 verify_e2_3.py
--selftest`` is the same run; the controls are not behind the flag.
"""
import sys

import cg_check as cg
import e_check
import e2_3

LANDAREA = "Land area (square kilometres)"
BIRDS = "Resident bird species recorded"
DIST = "Distance from the mainland (kilometres)"
SHARED = "Plant species present that also grow on the mainland"
SPECIES = "Species recorded on the island"
SPEC = "Specialist bird species present"
GEN = "Generalist bird species present"
REACHED = "Islands in the group it has reached"
LOST = "Native specialist species lost from those islands"
FOREST = "Area of fruiting forest (hectares)"
TERR = "Territory one breeding pair requires (hectares)"
PAIRS = "Breeding pairs the island supports"
CONTDIST = "Distance from the nearest continent (kilometres)"
ENDEMIC = "Percent of its plant species found nowhere else"


def _falls(vals):
    return all(vals[i + 1] < vals[i] for i in range(len(vals) - 1))


def _rises(vals):
    return all(vals[i + 1] > vals[i] for i in range(len(vals) - 1))


def _by(table, key_header, *headers):
    """Rows sorted ascending on ``key_header``; one list back per header."""
    keys = cg.col(table, key_header)
    order = sorted(range(len(table["rows"])), key=lambda i: keys[i])
    return [[cg.col(table, h)[i] for i in order] for h in headers]


def q11(table, item):
    (spp,) = _by(table, LANDAREA, BIRDS)
    assert _rises(spp), f"species must rise with land area; got {spp}"
    assert spp[0] == min(spp), "'the smallest island holds the most species' must be false"
    assert len(set(spp)) == len(spp), "'every island holds the same count' must be false"
    return (f"sorted by land area the bird species counts read {spp}, strictly increasing "
            "across the four islands")


def q12(table, item):
    spp = cg.col(table, BIRDS)
    diff = max(spp) - min(spp)
    assert diff == 43, f"the difference must be 43 species; got {diff}"
    assert diff != min(spp), "'six' must not also be the difference"
    assert diff != max(spp) - 0, "the difference must not equal the larger count itself"
    return (f"the largest island records {max(spp):.0f} species and the smallest "
            f"{min(spp):.0f}, a difference of {diff:.0f}")


def q13(table, item):
    (shared,) = _by(table, DIST, SHARED)
    assert _falls(shared), f"shared species must fall as distance rises; got {shared}"
    assert shared[-1] == min(shared), \
        "'the furthest island shares the most species' must be false"
    assert len(set(shared)) == len(shared), "'every island shares the same number' must be false"
    return (f"sorted by distance from the mainland the shared plant species read {shared}, "
            "strictly decreasing")


def q14(table, item):
    labs = cg.labels(table)
    shared = dict(zip(labs, cg.col(table, SHARED)))
    fewest = min(shared, key=shared.get)
    assert fewest == "Island D", f"Island D must share the fewest species; got {fewest}"
    assert len(set(shared.values())) == len(shared), "the four counts must all differ"
    return (f"{fewest} shares {shared[fewest]:.0f} species with the mainland, the smallest "
            f"of the four counts {sorted(shared.values())}")


def q15(table, item):
    spp = cg.col(table, SPECIES)
    assert _rises(spp), f"the species count must rise at every survey; got {spp}"
    assert spp[0] != max(spp), "'the island was full within five years' must be false"
    return (f"the successive surveys record {spp} species, rising at every one of them")


def q16(table, item):
    diff = cg.cell(table, "Fifty", SPECIES) - cg.cell(table, "Five", SPECIES)
    assert diff == 41, f"the increase must be 41 species; got {diff}"
    return (f"the fifty-year survey exceeds the five-year survey by {diff:.0f} species, "
            "the difference between two entries in one column")


def q17(table, item):
    spec = cg.col(table, SPEC)
    gen = cg.col(table, GEN)
    assert _falls(spec), f"the specialist count must fall throughout; got {spec}"
    assert _rises(gen), f"the generalist count must rise throughout; got {gen}"
    assert spec != gen, "the two columns must be distinguishable"
    return (f"the specialists read {spec} and the generalists {gen}, one strictly falling "
            "and the other strictly rising over the same three stages")


def q18(table, item):
    spec = cg.col(table, SPEC)
    gen = cg.col(table, GEN)
    assert spec[0] == 9 and spec[-1] == 2, \
        f"the specialists must run from 9 to 2; got {spec[0]} to {spec[-1]}"
    assert gen[0] != spec[0], "the generalist column must not open at the same value"
    return (f"the specialist column opens at {spec[0]:.0f} and closes at {spec[-1]:.0f}, so "
            "that fraction of the original specialists remains")


def q19(table, item):
    (lost,) = _by(table, REACHED, LOST)
    assert _rises(lost), f"specialists lost must rise with islands reached; got {lost}"
    assert lost[0] == min(lost), \
        "'the species reaching one island caused the largest loss' must be false"
    assert max(lost) > 0, "'no specialists were lost anywhere' must be false"
    return (f"sorted by islands reached the specialists lost read {lost}, strictly "
            "increasing with the spread of the introduced species")


def q20(table, item):
    area = cg.col(table, FOREST)
    terr = cg.col(table, TERR)
    pairs = cg.col(table, PAIRS)
    assert len(set(terr)) == 1 and terr[0] > 1, \
        f"one territory requirement must apply to every row and exceed one; got {terr}"
    for a, t, p in zip(area, terr, pairs):
        assert abs(a / t - p) < 1e-9, f"{a} over {t} is not {p}"
        assert abs(a * t - p) > 1e-9, "the product must not also equal the pair count"
    assert len(set(pairs)) == len(pairs), \
        "the four pair counts must all differ, so the relation is not read off a flat column"
    return (f"the forest areas {area} divided by the territory {terr[0]:.0f} give exactly "
            f"the pair counts {pairs} on all four islands")


def q21(table, item):
    labs = cg.labels(table)
    pairs = dict(zip(labs, cg.col(table, PAIRS)))
    fewest = min(pairs, key=pairs.get)
    assert fewest == "Island W", f"Island W must support the fewest pairs; got {fewest}"
    assert len(set(pairs.values())) == len(pairs), "'all four support the same number' must be false"
    return (f"{fewest} supports {pairs[fewest]:.0f} pairs, the smallest of "
            f"{sorted(pairs.values())}")


def q22(table, item):
    (end,) = _by(table, CONTDIST, ENDEMIC)
    assert _rises(end), f"the endemic share must rise with distance; got {end}"
    assert end[0] == min(end), \
        "'the nearest group holds the largest share' must be false"
    assert min(end) > 0, "'no group holds any species found nowhere else' must be false"
    return (f"sorted by distance from the nearest continent the endemic shares read {end} "
            "percent, strictly increasing")


def q23(table, item):
    labs = cg.labels(table)
    end = dict(zip(labs, cg.col(table, ENDEMIC)))
    top = max(end, key=end.get)
    assert top == "Group 4", f"Group 4 must hold the largest endemic share; got {top}"
    assert len(set(end.values())) == len(end), "the four shares must all differ"
    return (f"{top} records {end[top]:.0f} percent found nowhere else, the largest of "
            f"{sorted(end.values())}")


CLAIMS = [
 ("community structures",
  "ERT-2.D.1, near verbatim: island biogeography is the study of the ecological relationships and distribution of organisms on islands, and of these organisms' community structures. Every rejected option names something other than the organisms."),
 ("mineral composition",
  "ERT-2.D.1 names ecological relationships, distribution of organisms on islands, and those organisms' community structures. The geology of the island itself is outside the three."),
 ("arriving from elsewhere",
  "ERT-2.D.2, near verbatim: islands have been colonized in the past by new species arriving from elsewhere, so an island community was assembled by arrivals rather than fixed at the island's origin."),
 ("food and territory are limited",
  "ERT-2.E.1 gives the limited resources on most islands, such as food and territory, as the reason many island species have evolved to be specialists versus generalists."),
 ("Food and territory",
  "ERT-2.E.1 names food and territory as its two examples of the limited resources found on most islands. The rejected pairs name conditions the statement does not list."),
 # Both clauses, because two distractors keep the first clause and reverse the second.
 ("typically generalists, and they outcompete the specialists",
  "ERT-2.E.1, near verbatim: invasive species, typically generalists, are introduced and outcompete the specialists. The rejected options swap which kind the invader is, reverse which kind loses, or deny that competition follows."),
 ("the island's specialists",
  "ERT-2.E.1 states that the long-term survival of SPECIALISTS may be jeopardized when introduced invasive species outcompete them. It names one group at risk, and it is not the generalists."),
 ("depends on an introduction taking place",
  "ERT-2.E.1 is written with may and with if and when, which make the loss conditional on an introduction and uncertain even where one occurs."),
 ("most islands but is not asserted of every island",
  "ERT-2.E.1 locates the limited resources on MOST islands, which asserts a prevailing pattern and leaves room for islands where resources are not limiting."),
 ("common among island species without covering all of them",
  "ERT-2.E.1 says MANY island species have evolved to be specialists versus generalists, which is a statement about how common the pattern is rather than a universal one, and it says nothing about mainland species."),
 ("More bird species are recorded on the larger islands",
  "Recomputed in q11 above: sorted by land area the species counts are strictly increasing. ERT-2.D.1 makes the distribution of organisms on islands the subject matter of the field, and this record is one such distribution."),
 ("Forty-three",
  "Recomputed in q12 above: 49 species less 6 is 43. The count is read from the record rather than from any rule about area, which the framework does not supply."),
 ("further from the mainland share fewer plant species",
  "Recomputed in q13 above: sorted by distance the shared species counts are strictly decreasing. ERT-2.D.2 supplies arrival from elsewhere as how island floras were assembled, and the record measures how much of each is shared with a possible source."),
 ("Island D",
  "Recomputed in q14 above: the smallest shared count belongs to the island lying furthest out. The comparison is a direct reading of one column."),
 ("rose at every survey",
  "Recomputed in q15 above: the successive counts are strictly increasing. ERT-2.D.2 states that islands have been colonized by new species arriving from elsewhere, which is the only way an island that began bare could gain them."),
 ("Forty-one",
  "Recomputed in q16 above: 44 species at fifty years less 3 at five years is 41. The figure is a difference between two entries in one column."),
 # Both clauses, because the distractor is the SWAP of the two columns.
 ("specialist count fell at both later stages while the generalist count rose",
  "Recomputed in q17 above: the specialist column strictly falls and the generalist column strictly rises over the same three stages. ERT-2.E.1 states that introduced invasive species, typically generalists, outcompete the specialists."),
 ("Two of the original nine",
  "Recomputed in q18 above: the specialist column opens at 9 and closes at 2. The generalist column opens at 5 and is a different measurement, which is what the rejected counts confuse it with."),
 ("most islands is associated with the most native specialists lost",
  "Recomputed in q19 above: sorted by islands reached the specialists lost are strictly increasing. ERT-2.E.1 attaches the jeopardy to the arrival of introduced species that outcompete the specialists."),
 ("forest area divided by the territory one pair requires",
  "Recomputed in q20 above: on all four islands the forest area divided by the twenty hectares one pair needs gives exactly the pair count, and the product does not. ERT-2.E.1 names territory as one of the limited resources on most islands."),
 ("Island W",
  "Recomputed in q21 above: the smallest pair count belongs to the island with the least fruiting forest. ERT-2.E.1 names territory among the limited resources that shape island populations."),
 ("more distant groups hold a larger percent",
  "Recomputed in q22 above: sorted by distance from the nearest continent the endemic shares are strictly increasing. ERT-2.D.1 makes the distribution of island organisms the field's subject and ERT-2.D.2 supplies arrival from elsewhere."),
 ("Group 4",
  "Recomputed in q23 above: the largest endemic share belongs to the group lying furthest from any continent. The comparison is a direct reading of one column."),
 ("where the generalist was never introduced, held steady",
  "ERT-2.E.1 attributes the jeopardy to the introduced competitor, so the evidence must separate the introduction from everything else that changed over the same years. A comparable island without the introduction does that and none of the rejected observations does."),
 ("assembled rather than fixed when the island formed",
  "ERT-2.D.2 states that islands have been colonized in the past by new species arriving from elsewhere. It asserts that arrival happened; it does not make the arrivals human-assisted, simultaneous, or identical to the mainland stock."),
 ("ecological relationships among the organisms and the community structures",
  "ERT-2.D.1 names three things, and a bare species list covers only the distribution. The relationships and the community structures are what such a list leaves out."),
 # Both clauses, because the distractor swaps which kind the framework puts at risk.
 ("the specialists, not every native species, at risk",
  "ERT-2.E.1 names the long-term survival of specialists as what may be jeopardized when introduced invasive species, typically generalists, outcompete them. It makes no equivalent claim about natives that are themselves generalists."),
 ("introduced generalist that outcompetes it",
  "ERT-2.E.1 states that the long-term survival of specialists may be jeopardized if and when invasive species, typically generalists, are introduced and outcompete the specialists. That is the only risk the statement names."),
 ("typically a generalist and that the native specialists lose",
  "NAMED CHAIN: EIN-4.A.2 states that invasive species are often generalist, r-selected species and may therefore outcompete native species for resources, and ERT-2.E.1 states that invasive species, typically generalists, outcompete the specialists. Both make the invader usually a generalist and the native the one outcompeted."),
 ("limited resources have made many island species specialists that introduced generalists",
  "ERT-2.D.1 supplies the subject matter, ERT-2.D.2 the colonisation from elsewhere and ERT-2.E.1 the limited resources, the specialisation and the introduced generalists that may outcompete the specialists. Each rejected summary changes the subject matter, denies colonisation, reverses which kind is advantaged, or hardens may into certainty."),
]

TABLE_CHECKS = {11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16, 17: q17,
                18: q18, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23}

if "--selftest" in sys.argv:
    print("note: e_check.run negative-controls every gate on every run; "
          "--selftest is the same run, not a separate one.")

e_check.run(e2_3, CLAIMS, TABLE_CHECKS)
