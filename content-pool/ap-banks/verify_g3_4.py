"""Key audit for AP HUMAN GEOGRAPHY 3.4 Types of Diffusion.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. This topic has exactly one essential-knowledge statement, and
it carries a structure rather than a flat list:

    IMP-3.A.1  Relocation and expansion -- including contagious, hierarchical,
               and stimulus expansion -- are types of diffusion.

The nesting is citable and it is the examinable content. TWO top-level types,
with THREE kinds of the second one. Item 1 asks for the structure and item 21
asks why the three sit under expansion rather than beside relocation; both cite
the sentence's own wording.

WHAT THE CED DOES NOT DEFINE. Every one of the five terms. So each key rests on
the definitions set out in the module header, and the claims say which:

    relocation    the trait travels because PEOPLE travel
    expansion     the trait spreads outward while REMAINING at the source
    contagious    spread by direct contact, so adoption follows DISTANCE
    hierarchical  spread by rank, so adoption follows SIZE and skips between
    stimulus      the specific trait is NOT adopted; the underlying idea is,
                  in a locally remade form

Three diagnostic tests carry most of the module, and each has an item asking for
the test itself rather than for an application:

    item 2   relocation vs expansion -- does the source keep the trait?
    item 6   contagious vs hierarchical -- does adoption order follow distance
             or rank? Items 26 and 27 are a deliberate pair of tables built to
             give opposite answers to exactly that question.
    item 20  stimulus is not "spread with minor variation"; the specific trait
             is rejected and only the principle crosses

Two items exist to stop overreach, and their claims say so. Item 13 keys to
"nothing decisive" -- a trait dying at its hearth long afterward is not evidence
about how it originally travelled. Item 19 keys to independent invention as NOT
diffusion, because similarity without transmission is the standing trap in this
topic.

A terminology constraint the checker enforces independently: hg_check's
SYNONYM_CLASSES treat "contagious diffusion" and "contagious expansion
diffusion" as one construct, and likewise for the other two subtypes, so no
question here offers both forms as separate options.

The five table items (26-30) are the computational gate:

  26  adoption order runs exactly OPPOSITE to distance and exactly WITH
      population -- the recompute asserts both correlations
  27  the mirror image: adoption order matches distance exactly while population
      runs in no order at all
  28  the hearth GAINS practitioners while three destinations go from zero,
      which is what separates expansion from relocation
  29  restaurants per thousand migrants is near-constant across a 140-to-1 range
      of migrant populations
  30  exactly one society took the idea while declining the practice

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g3_4


def _order(values):
    """Rank positions of a list, smallest first."""
    return [sorted(values).index(v) for v in values]


def q26_hierarchical_signature(table):
    """Adoption follows population and runs opposite to distance."""
    pop, dist, year = [], [], []
    for row in table["rows"]:
        d = rowdict(table, row)
        pop.append(num(d["Population"]))
        dist.append(num(d["Distance from source (km)"]))
        year.append(num(d["Year of adoption"]))
    # Sorting by adoption year must give strictly decreasing population...
    by_year = sorted(zip(year, pop, dist))
    pops = [p for _, p, _ in by_year]
    dists = [x for _, _, x in by_year]
    assert all(pops[i] > pops[i + 1] for i in range(len(pops) - 1)), pops
    # ...and strictly decreasing distance, which is the opposite of contagious.
    assert all(dists[i] > dists[i + 1] for i in range(len(dists) - 1)), dists
    # The first adopter is both the largest and the most distant.
    assert pops[0] == max(pop) and dists[0] == max(dist), (pops, dists)
    assert pops[-1] == min(pop) and dists[-1] == min(dist), (pops, dists)
    return "largest and most distant settlement adopted first"


def q27_contagious_signature(table):
    """Adoption follows distance while population runs in no order."""
    pop, dist, year = [], [], []
    for row in table["rows"]:
        d = rowdict(table, row)
        pop.append(num(d["Population"]))
        dist.append(num(d["Distance from source (km)"]))
        year.append(num(d["Year of adoption"]))
    by_year = sorted(zip(year, dist, pop))
    dists = [x for _, x, _ in by_year]
    pops = [p for _, _, p in by_year]
    assert all(dists[i] < dists[i + 1] for i in range(len(dists) - 1)), dists
    # Population must NOT be monotonic in either direction, or the item would
    # also fit a hierarchical reading.
    rising = all(pops[i] < pops[i + 1] for i in range(len(pops) - 1))
    falling = all(pops[i] > pops[i + 1] for i in range(len(pops) - 1))
    assert not rising and not falling, pops
    # And the largest settlement must adopt last, disposing of a distractor by
    # making its premise true and its inference wrong.
    assert pops[-1] == max(pop), pops
    return "adoption follows distance from the source"


def q28_expansion_not_relocation(table):
    """The hearth gains while the destinations go from zero."""
    hearth, dests = None, []
    for row in table["rows"]:
        d = rowdict(table, row)
        before = num(d["Practitioners before"])
        after = num(d["Practitioners after"])
        if d["Place"] == "Hearth region":
            hearth = (before, after)
        else:
            dests.append((before, after))
    assert hearth is not None and len(dests) == 3, (hearth, dests)
    assert hearth[1] > hearth[0], hearth
    assert all(b == 0 and a > 0 for b, a in dests), dests
    assert sum(a for _, a in dests) == 22700, dests
    return "grew at its source while also appearing in three new places"


def q29_relocation_tracks_migrants(table):
    """Restaurants per thousand migrants is near-constant across a wide range."""
    ratios, migrants = [], []
    for row in table["rows"]:
        d = rowdict(table, row)
        m = num(d["Migrants from the hearth region"])
        r = num(d["Restaurants serving the cuisine"])
        migrants.append(m)
        ratios.append(1000 * r / m)
    assert max(migrants) / min(migrants) > 100, migrants
    assert max(ratios) / min(ratios) < 1.5, ratios
    assert all(1.0 < x < 2.0 for x in ratios), ratios
    return "tracks the number of migrants"


def q30_stimulus_row(table):
    """Exactly one society took the idea while declining the practice."""
    stim, plain, none = [], [], []
    for row in table["rows"]:
        d = rowdict(table, row)
        as_is = d["Adopted the practice as encountered"] == "Yes"
        idea = d["Adopted the underlying idea in an altered form"] == "Yes"
        rejected = d["Rejected it entirely"] == "Yes"
        assert sum([as_is, idea, rejected]) == 1, d
        if idea:
            stim.append(d["Society"])
        elif as_is:
            plain.append(d["Society"])
        else:
            none.append(d["Society"])
    assert stim == ["Society X"], stim
    assert len(plain) == 2 and len(none) == 1, (plain, none)
    return "the only one that took the idea"


CLAIMS = [
 ("Relocation and expansion, with expansion including contagious",
  "EK IMP-3.A.1 names relocation and expansion as the two types and lists contagious, hierarchical and stimulus as kinds of expansion. The nesting matters: all three subtypes are ways a trait spreads while remaining at its source."),

 ("Whether the trait remains at its source",
  "EK IMP-3.A.1 separates the two types at the top level, and the difference is mechanism. Expansion spreads outward from a source that keeps the trait, while relocation carries the trait away with the people holding it; the CED does not state this, so it is argued from the terms."),

 ("travelled with the people who carried it",
  "EK IMP-3.A.1 names relocation among the types of diffusion, and its mechanism is the physical movement of the people holding the trait. That the practice also survives at the hearth does not make this an expansion, since nothing spread outward from the source to reach the new country."),

 ("spread follows direct contact and therefore distance",
  "EK IMP-3.A.1 lists contagious among the kinds of expansion diffusion. Its signature is that adoption falls off with distance from the source, because the mechanism is contact and contact is likelier between nearby people."),

 ("follows the size and rank of places rather than distance",
  "EK IMP-3.A.1 names hierarchical among the kinds of expansion diffusion, and its diagnostic is that intervening rural areas are skipped. Adoption ordered by settlement size rather than by proximity is what identifies it."),

 ("correlates better with distance from the source or with the size",
  "EK IMP-3.A.1 lists both as kinds of expansion, so what separates them is which variable orders the adoptions. Contagious spread is distance-ordered and hierarchical spread is rank-ordered, and comparing the two correlations is exactly how a geographer tells them apart."),

 ("underlying idea spread while the specific trait did not",
  "EK IMP-3.A.1 names stimulus among the kinds of expansion diffusion. What crossed was the principle rather than the artifact, and the local version exists because of the encounter, which is what makes it diffusion rather than independent invention."),

 ("remains at its source and often strengthens there",
  "EK IMP-3.A.1 treats expansion as one of the two top-level types, and the source retaining the trait is what separates it from relocation. All three subtypes share that property, which is why the CED nests them beneath it."),

 ("operating through the urban system",
  "EK IMP-3.A.1 lists hierarchical among the kinds of expansion diffusion, and an ordering by metropolitan rank across several countries is its clearest form. That the process is commercial does not exempt it, since a chain is a practice spreading between places."),

 ("each adoption comes from contact with a nearby adopter",
  "EK IMP-3.A.1 lists contagious among the kinds of expansion. A widening ring is the geometric signature of contact-based spread, since each new adopter can only be reached by someone already close by."),

 ("any migration stream is a potential diffusion channel",
  "EK IMP-3.A.1 defines relocation by movement rather than by contact, which makes migrants the carriers. Every chain, step and transnational stream from Unit 2 is therefore also a route along which practices travel."),

 ("reworked rather than reproduced",
  "EK IMP-3.A.1 names stimulus among the kinds of expansion diffusion, and the diagnostic is that the specific trait failed to take while its principle did. That traders were the channel identifies the route rather than the type."),

 ("Nothing decisive",
  "The distinction EK IMP-3.A.1 draws concerns the mechanism at the time of spread, not the fate of the source afterward. A hearth can lose a trait for reasons unrelated to how it travelled, so a later disappearance is not evidence about the type."),

 ("immigrants from a particular region settled there",
  "EK IMP-3.A.1 names relocation as the type in which the trait moves with people. The other options describe spread through contact, through the urban hierarchy, through adaptation of an idea, and through proximity, all of which are expansion kinds."),

 ("same distance-dependent contact mechanism",
  "EK IMP-3.A.1's contagious subtype takes its name from precisely this analogy. What a pathogen and a practice share is that transmission requires proximity, and that shared mechanism produces the same distance-decaying spatial pattern."),

 ("distant metropolis adopting years before a small town",
  "EK IMP-3.A.1 lists both subtypes, and hierarchical spread is identified by skipping: a far but important place adopting before a near but small one. A smooth outward ring and a distance-ordered sequence are both the contagious signature instead."),

 ("connect large places to one another",
  "EK IMP-3.A.1's hierarchical subtype spreads along a network ordered by rank, and a network of that kind links nodes rather than filling space. The gaps are a property of the channel and not of the people living in them."),

 ("a single trait can travel by more than one channel",
  "EK IMP-3.A.1's subtypes describe channels rather than mutually exclusive events, and nothing prevents a trait from using two. Recognising a mixed case is more accurate than forcing it into one category and losing half the pattern."),

 ("developing similar tools independently",
  "This is a NOT question, and EK IMP-3.A.1's types all describe a trait or an idea travelling from one place to another. Independent invention produces similarity without transmission, and similarity alone is never evidence that anything spread."),

 ("specific practice is not adopted at all",
  "EK IMP-3.A.1 lists stimulus as a distinct kind of expansion rather than as ordinary spread with minor variation. What distinguishes it is that the original trait was rejected or unusable while the principle behind it was kept and remade."),

 ("spreads outward from a source that retains it",
  "EK IMP-3.A.1 writes 'expansion -- including contagious, hierarchical, and stimulus expansion', which subordinates the three explicitly. What they share is that the source keeps the trait, and they differ only in which channel carries it outward."),

 ("travels in the mouths of people who move",
  "EK IMP-3.A.1 defines relocation by the physical movement of the people carrying the trait, and settlement and garrisoning are exactly that. Later local adoption by contact is a second process rather than the one that brought the language."),

 ("barriers that reduce ordinary contact",
  "EK IMP-3.A.1's contagious subtype spreads by direct contact, so whatever interrupts contact interrupts the spread. City size and the distance between capitals bear on hierarchical spread instead, which travels between nodes rather than across intervening ground."),

 ("usual distance friction is largely removed",
  "EK IMP-3.A.1's expansion types are defined by mechanism rather than by medium, and the source keeps the trait here. What changes online is that proximity stops governing contact, so the ordering falls to prominence and connection instead of to distance."),

 ("adopting the practice's purpose in a form using a local animal",
  "EK IMP-3.A.1 names stimulus among the kinds of expansion diffusion, and its structure is rejection of the specific plus retention of the principle. Unchanged adoption is ordinary expansion, complete rejection is no diffusion, and immigrant carriage is relocation."),

 ("largest and most distant settlement adopted first",
  "Recomputed from the table: sorting by adoption year gives strictly decreasing population AND strictly decreasing distance, so the first adopter is both the biggest and the furthest while the last is the smallest and the nearest. Ordering by rank rather than proximity is the hierarchical signature.",
  q26_hierarchical_signature),

 ("adoption follows distance from the source",
  "Recomputed from the table: sorting by adoption year gives strictly increasing distance while population runs in no order at all, rising and falling. The verifier confirms population is not monotonic in either direction, which is what rules out a hierarchical reading of the same data.",
  q27_contagious_signature),

 ("grew at its source while also appearing in three new places",
  "Recomputed from the table: the hearth rises from 40,000 to 58,000 practitioners while three destinations move from zero to 22,700 between them. A source that gains rather than loses while the trait appears elsewhere is the definition of expansion rather than relocation.",
  q28_expansion_not_relocation),

 ("tracks the number of migrants",
  "Recomputed from the table: restaurants per thousand migrants are 1.33, 1.42, 1.44 and 1.67 across migrant populations spanning more than a hundred to one. A near-constant ratio across that range is what carriage by migrants produces, which is EK IMP-3.A.1's relocation type.",
  q29_relocation_tracks_migrants),

 ("the only one that took the idea",
  "Recomputed from the table: exactly one row records adoption of the underlying idea in an altered form together with non-adoption of the practice as encountered, and the verifier confirms every row records exactly one response. Two societies took the practice unchanged, which is ordinary expansion, and one took nothing at all.",
  q30_stimulus_row),
]

hg_check.check(g3_4, CLAIMS, per_topic=30, n_choices=5)
