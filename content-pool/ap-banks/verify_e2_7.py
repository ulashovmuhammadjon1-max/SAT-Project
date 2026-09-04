"""Key audit for AP ENVIRONMENTAL SCIENCE 2.7 Ecological Succession.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
ERT-2.I.1  two main types of ecological succession: primary and secondary
                                                    -- items 1, 2, 30
ERT-2.I.2  a keystone species is one whose activities have a particularly
           significant role in determining community structure
                                     -- items 3, 7, 18, 19, 20, 27, 28, 30
ERT-2.I.3  an indicator species is a plant or animal that, by its presence,
           abundance, scarcity, or chemical composition, demonstrates that some
           distinctive aspect of the character or quality of an ecosystem is
           present                    -- items 4, 5, 6, 7, 21, 22, 23, 24, 29, 30
ERT-2.J.1  pioneer members of an early successional species commonly move into
           unoccupied habitat and over time adapt to its particular conditions,
           which may result in the origin of new species
                                                -- items 8, 9, 10, 25, 26, 30
ERT-2.J.2  succession in a disturbed ecosystem will affect the total biomass,
           species richness, and net productivity over time
                                     -- items 11, 12, 14, 15, 16, 17, 30
Unit 2 overview: succession can occur in terrestrial and aquatic ecosystems in
both developed and developing areas                          -- item 13

THE BIGGEST TRAP IS WHAT ERT-2.I.1 DOES NOT SAY. It names two main types and
defines neither -- no bare rock, no soil, no rule about which disturbance leads
to which. So no item asks a student to sort a case into primary or secondary,
and no key states a distinguishing feature. Items 1 and 2 ask only the names.

ERT-2.J.2 names three quantities and gives no DIRECTION for any of them, so
every keyed direction in items 14 to 17 is read off the table in front of the
student, and the checks below recompute it from that table alone.

KEYSTONE AND INDICATOR INVITE THE SWAP, and the unit overview singles the pair
out as one students confuse. The anchor for item 7 therefore carries BOTH
clauses, because either alone matches the swapped distractor as readily as the
key. That defect was found once already in verify_e2_1.py.

DATA ITEMS: 14 to 26 carry tables, recomputed below by column header.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and EVERY data table in turn, and requires each
corruption to raise BEFORE the real gate runs. Four of these checks read a
relationship between two columns that a reversal preserves; e_check flattens
those tables next, and each check then fails because a flat column has no
relationship left in it. ``python3 verify_e2_7.py --selftest`` is the same run;
the controls are not behind the flag.
"""
import sys

import cg_check as cg
import e_check
import e2_7

YEARS = "Years since the disturbance"
BIOMASS = "Total biomass (tonnes per hectare)"
RICH = "Species richness (number of species present)"
NPP = "Net primary productivity (grams per square metre per year)"
SHORESPP = "Species present on the shore"
MUSSEL = "Percent of the rock covered by one mussel"
BEFORE = "Species present before the removal"
AFTER = "Species present three years after the removal"
SO2 = "Sulfur dioxide in the air (micrograms per cubic metre)"
LICHEN = "Lichen thalli counted on ten trees"
SEDIMENT = "Mercury in the lake sediment (milligrams per kilogram)"
TISSUE = "Mercury in the tissue of one fish species (milligrams per kilogram)"
LAVAYEARS = "Years since the lava flow cooled"
PLANTS = "Plant species growing on it"


def _rises(v):
    return all(v[i + 1] > v[i] for i in range(len(v) - 1))


def _falls(v):
    return all(v[i + 1] < v[i] for i in range(len(v) - 1))


def _by(table, key_header, *headers):
    keys = cg.col(table, key_header)
    order = sorted(range(len(table["rows"])), key=lambda i: keys[i])
    return [[cg.col(table, h)[i] for i in order] for h in headers]


def q14(table, item):
    cols = {BIOMASS: cg.col(table, BIOMASS), RICH: cg.col(table, RICH),
            NPP: cg.col(table, NPP)}
    for name, vals in cols.items():
        assert len(set(vals)) > 1, f"{name} must change across the record; got {vals}"
    return ("all three of the quantities the framework names change across the record: "
            + "; ".join(f"{k.split(' (')[0]} {v}" for k, v in cols.items()))


def q15(table, item):
    b = cg.col(table, BIOMASS)
    diff = b[-1] - b[0]
    assert diff == 208, f"the rise must be 208 tonnes per hectare; got {diff}"
    assert diff > 0, "'it fell' must be false"
    assert diff != b[-1], "the change must not coincide with the final reading"
    return (f"biomass runs {b[0]:.0f} to {b[-1]:.0f} tonnes per hectare, a rise of "
            f"{diff:.0f}")


def q16(table, item):
    yrs = cg.col(table, YEARS)
    rich = cg.col(table, RICH)
    peak = max(zip(rich, yrs))
    assert peak[1] == 40, f"richness must peak at forty years; got {peak[1]}"
    assert list(rich).count(peak[0]) == 1, "the peak must be unique"
    assert len(set(rich)) > 1, "'richness was the same at every measurement' must be false"
    return f"the richness figures are {rich} and the largest, {peak[0]:.0f}, falls at year {peak[1]:.0f}"


def q17(table, item):
    b = dict(zip(cg.col(table, YEARS), cg.col(table, BIOMASS)))
    r = dict(zip(cg.col(table, YEARS), cg.col(table, RICH)))
    p = dict(zip(cg.col(table, YEARS), cg.col(table, NPP)))
    assert b[80] > b[40], f"biomass must rise over that interval; got {b[40]} then {b[80]}"
    assert r[80] < r[40], f"richness must fall over that interval; got {r[40]} then {r[80]}"
    assert p[80] < p[40], f"net productivity must fall; got {p[40]} then {p[80]}"
    return (f"between years 40 and 80 biomass moves {b[40]:.0f} to {b[80]:.0f}, richness "
            f"{r[40]:.0f} to {r[80]:.0f} and net productivity {p[40]:.0f} to {p[80]:.0f}")


def q18(table, item):
    spp = cg.col(table, SHORESPP)
    cover = cg.col(table, MUSSEL)
    assert _falls(spp), f"the species count must fall throughout; got {spp}"
    assert _rises(cover), f"the mussel's cover must rise throughout; got {cover}"
    assert cover[-1] > 0, "'the mussel disappeared' must be false"
    return (f"species present read {spp} while the mussel's cover reads {cover} percent, "
            "one strictly falling and the other strictly rising")


def q19(table, item):
    spp = cg.col(table, SHORESPP)
    lost = (spp[0] - spp[-1]) / spp[0]
    assert abs(lost - 2 / 3) < 0.02, f"two thirds of the species must be lost; got {lost}"
    assert lost > 0, "'it did not fall' must be false"
    return (f"the shore holds {spp[0]:.0f} species before the removal and {spp[-1]:.0f} "
            f"after, a loss of {lost:.2f} of them")


def q20(table, item):
    labs = cg.labels(table)
    drop = {lab: b - a for lab, b, a in
            zip(labs, cg.col(table, BEFORE), cg.col(table, AFTER))}
    worst = max(drop, key=drop.get)
    assert worst == "Species P", f"the first removal must change the community most; got {worst}"
    others = [v for k, v in drop.items() if k != worst]
    assert drop[worst] > 2 * max(others), \
        f"that removal must stand well clear of the others; got {drop}"
    assert min(others) == 0, "one removal must leave the community unchanged"
    return (f"the removals leave losses of {drop} species, and only one of them changes the "
            "community substantially")


def q21(table, item):
    (lich,) = _by(table, SO2, LICHEN)
    assert _falls(lich), f"lichen counts must fall as sulfur dioxide rises; got {lich}"
    assert lich[-1] != max(lich), "'the dirtiest site carried the most lichen' must be false"
    assert len(set(lich)) == len(lich), "'the same count at every site' must be false"
    return (f"sorted by sulfur dioxide the lichen counts read {lich}, strictly decreasing")


def q22(table, item):
    labs = cg.labels(table)
    lich = dict(zip(labs, cg.col(table, LICHEN)))
    so2 = dict(zip(labs, cg.col(table, SO2)))
    best = max(lich, key=lich.get)
    assert best == "Site 1", f"Site 1 must carry the most lichen; got {best}"
    assert so2[best] == min(so2.values()), \
        "the site with the most lichen must also carry the least sulfur dioxide"
    return (f"{best} carries {lich[best]:.0f} lichen thalli, the most of the four, and "
            f"{so2[best]:.0f} micrograms per cubic metre, the least")


def q23(table, item):
    (tis,) = _by(table, SEDIMENT, TISSUE)
    assert _rises(tis), f"tissue mercury must rise with sediment mercury; got {tis}"
    assert min(tis) > 0, "'no mercury in any fish tissue' must be false"
    assert len(set(tis)) == len(tis), "'every lake's fish carried the same' must be false"
    return (f"sorted by sediment mercury the tissue readings run {tis} milligrams per "
            "kilogram, strictly increasing")


def q24(table, item):
    sed, tis = _by(table, SEDIMENT, SEDIMENT, TISSUE)
    assert _rises(sed) and _rises(tis), \
        f"both readings must rise together; got {sed} and {tis}"
    for s, t in zip(sed, tis):
        assert t > s, f"the tissue reading {t} must exceed the sediment reading {s}"
    return (f"the sediment readings {sed} and the tissue readings {tis} rise together, and "
            "the organism's reading is the larger in every lake")


def q25(table, item):
    spp = cg.col(table, PLANTS)
    assert _rises(spp), f"plant species must rise at every survey; got {spp}"
    assert spp[0] < 5, "'the flow was fully vegetated at the first survey' must be false"
    assert min(spp) > 0, "'the flow held no plants at any survey' must be false"
    return f"the surveys record {spp} plant species, rising at every one of them"


def q26(table, item):
    diff = cg.cell(table, "120", PLANTS) - cg.cell(table, "15", PLANTS)
    assert diff == 35, f"the increase must be 35 species; got {diff}"
    return (f"the last survey records {cg.cell(table, '120', PLANTS):.0f} species and the "
            f"second {cg.cell(table, '15', PLANTS):.0f}, a difference of {diff:.0f}")


CLAIMS = [
 ("primary and secondary succession",
  "ERT-2.I.1, near verbatim: there are two main types of ecological succession, primary and secondary succession. The framework gives the count and the two names and nothing more."),
 ("Tertiary succession",
  "ERT-2.I.1 names two main types, primary and secondary. Tertiary succession is not among them."),
 ("particularly significant role in determining community structure",
  "ERT-2.I.2, near verbatim: a keystone species is a species whose activities have a particularly significant role in determining community structure. The criterion is the effect of its activities, not abundance, rarity, signalling value or arrival order."),
 ("demonstrates that some distinctive aspect of the character",
  "ERT-2.I.3, near verbatim: an indicator species is a plant or animal that demonstrates that some distinctive aspect of the character or quality of an ecosystem is present. Its role is to reveal a condition."),
 ("presence, abundance, scarcity or chemical composition",
  "ERT-2.I.3 lists presence, abundance, scarcity, and chemical composition as the four properties by which an indicator species demonstrates something about its ecosystem. Each rejected set replaces at least one of the four."),
 ("character or quality of an ecosystem is present",
  "ERT-2.I.3 states that an indicator species demonstrates that some distinctive aspect of the character or quality of an ecosystem is present, and it attaches no other conclusion to that demonstration."),
 # Both clauses, because the distractor is the SWAP of the two definitions.
 ("significant role in determining community structure, while an indicator species demonstrates a condition",
  "ERT-2.I.2 defines a keystone species by the significant role its activities play in determining community structure and ERT-2.I.3 defines an indicator species by its demonstrating that some distinctive aspect of an ecosystem is present. The rejected options exchange the two or collapse them."),
 ("move into unoccupied habitat and over time adapt",
  "ERT-2.J.1, near verbatim: pioneer members of an early successional species commonly move into unoccupied habitat and over time adapt to its particular conditions."),
 ("The origin of new species",
  "ERT-2.J.1 states that the pioneers' adaptation may result in the origin of new species, which is the only outcome the statement attaches to it."),
 ("usual rather than universal, and that the new species is possible",
  "ERT-2.J.1's COMMONLY describes what usually happens without covering every case, and its MAY asserts possibility rather than necessity. Each rejected option hardens one of the two hedges or denies the claim."),
 ("Total biomass, species richness and net productivity",
  "ERT-2.J.2, near verbatim: succession in a disturbed ecosystem will affect the total biomass, species richness, and net productivity over time. Each rejected set swaps at least one of the three."),
 ("mineral composition of the bedrock",
  "ERT-2.J.2 names total biomass, species richness and net productivity. The geology beneath the ecosystem is not among the three."),
 ("terrestrial and aquatic ecosystems alike, and in developed",
  "The unit's own overview states that ecological succession can occur in terrestrial and aquatic ecosystems in both developed and developing areas, so no restriction of habitat or of country applies."),
 ("All three changed over the eighty years",
  "Recomputed in q14 above: none of the three columns is constant across the record. ERT-2.J.2 states that succession in a disturbed ecosystem will affect exactly total biomass, species richness and net productivity over time."),
 ("rose by 208 tonnes per hectare",
  "Recomputed in q15 above: 210 less 2 tonnes per hectare is 208, and the change is a rise. ERT-2.J.2 names total biomass among the quantities succession affects, and the size is read from the record."),
 ("At forty years",
  "Recomputed in q16 above: the richness figures are 9, 31, 58 and 47 species and the unique largest falls at the third measurement. ERT-2.J.2 gives no direction for richness, so the direction is read from the record."),
 ("Total biomass rose while species richness and net productivity both fell",
  "Recomputed in q17 above: over that interval biomass rises while richness and net productivity both fall. ERT-2.J.2 states that succession affects all three but assigns no direction to any of them."),
 ("number of species fell while a single mussel took over",
  "Recomputed in q18 above: the species count strictly falls while the mussel's cover strictly rises. ERT-2.I.2 defines a keystone species by the particularly significant role its activities play in determining community structure, which is what the removal reveals."),
 ("By two thirds",
  "Recomputed in q19 above: 15 species before the removal and 5 after leaves ten of fifteen gone. The share is arithmetic on two entries in one column."),
 ("The removal of Species P",
  "Recomputed in q20 above: one removal leaves 5 of the original 15 while the others leave 14 and 15. ERT-2.I.2 defines a keystone species by a particularly significant role in determining community structure, and only one of these three removals changes the community substantially."),
 ("Fewer lichens were counted where the sulfur dioxide concentration was higher",
  "Recomputed in q21 above: sorted by sulfur dioxide the lichen counts are strictly decreasing. ERT-2.I.3 makes abundance or scarcity one of the ways an indicator species demonstrates an aspect of an ecosystem's quality."),
 ("Site 1",
  "Recomputed in q22 above: the largest lichen count belongs to the site with the lowest sulfur dioxide reading. ERT-2.I.3 makes the abundance of an indicator species a demonstration of an aspect of an ecosystem's quality."),
 ("carried more mercury in their tissue",
  "Recomputed in q23 above: sorted by sediment mercury the tissue readings are strictly increasing. ERT-2.I.3 names chemical composition as one of the properties by which an indicator species demonstrates an aspect of its ecosystem."),
 ("fish tissue is the indicator reading",
  "Recomputed in q24 above: both readings rise together and the organism's reading is the larger in every lake. ERT-2.I.3 makes the indicator a PLANT OR ANIMAL whose chemical composition demonstrates an aspect of the ecosystem, so the fish is the indicator and the lake is what it demonstrates something about."),
 ("accumulated on ground that had none",
  "Recomputed in q25 above: the species counts rise at every survey from a count below five. ERT-2.J.1 states that pioneer members of an early successional species commonly move into unoccupied habitat and over time adapt to its conditions."),
 ("Thirty-five",
  "Recomputed in q26 above: 46 species less 11 is 35. The rejected values are the two entries themselves or differences between other pairs of surveys."),
 ("changes little when comparable species are removed",
  "ERT-2.I.2 defines a keystone species by the particularly significant role its activities play in determining community structure, so the evidence must be a community change traceable to that species and not to a comparable one. Abundance, rarity, arrival order and pollutant load are each something else."),
 ("in determining community structure, not abundance",
  "ERT-2.I.2 defines a keystone species by what its activities do to community structure. Abundance is not the test, and the framework attaches no restriction of habitat, of kingdom or of arrival order to the term."),
 ("scarcity in a valley demonstrates that the air",
  "ERT-2.I.3 makes an indicator species a plant or animal that, by its presence, abundance, scarcity or chemical composition, demonstrates that some distinctive aspect of the character or quality of an ecosystem is present. The rejected options describe a keystone role, a pioneer, a dominant and a long migrant."),
 ("may in time give rise to new species",
  "ERT-2.I.1 supplies the count and the two names, ERT-2.I.2 and ERT-2.I.3 supply the two definitions in their own directions, ERT-2.J.1 supplies the hedged pioneer claim and ERT-2.J.2 the three quantities. Each rejected summary changes the count, swaps the definitions, hardens a hedge, or drops one of the three quantities."),
]

TABLE_CHECKS = {14: q14, 15: q15, 16: q16, 17: q17, 18: q18, 19: q19, 20: q20,
                21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26}

if "--selftest" in sys.argv:
    print("note: e_check.run negative-controls every gate on every run; "
          "--selftest is the same run, not a separate one.")

e_check.run(e2_7, CLAIMS, TABLE_CHECKS)
