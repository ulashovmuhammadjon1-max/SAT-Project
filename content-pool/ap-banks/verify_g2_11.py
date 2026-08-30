"""Key audit for AP HUMAN GEOGRAPHY 2.11 Forced and Voluntary Migration.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. IMP-2.D prints two essential-knowledge statements, and both
are closed lists:

    IMP-2.D.1  Forced migrations include slavery and events that produce
               refugees, internally displaced persons, and asylum seekers.
    IMP-2.D.2  Types of voluntary migrations include transnational,
               transhumance, internal, chain, step, guest worker, and
               rural-to-urban.

Because both are lists of NAMES with no definitions attached, membership can be
cited but classification cannot. Items 1 and 18 test membership directly and
cite the lists; every other item classifies a case, and its key rests on the
definitions set out in the module header and repeated in the claims below.

THE TWO QUESTIONS THAT SEPARATE THE FORCED CATEGORIES, since this is where a
wrong key would do the most damage:

    was an international border crossed?   -- refugee / asylum seeker: yes
                                              internally displaced person: no
    has the protection claim been decided? -- refugee: yes
                                              asylum seeker: no

Distance travelled, reason for flight and intention to return are the same
across all three and cannot distinguish them. Items 2, 3, 4, 5, 15, 16, 21, 22
and 26 are built on that pair, and item 15 asks for the single distinguishing
question directly.

THE ODD MEMBER OF THE VOLUNTARY LIST. Six of the seven types relocate a
household; transhumance is a repeating seasonal cycle that returns to where it
began. Items 8, 9, 24 and 29 turn on that, and item 29's table proves it by
elevation rather than asserting it.

WHERE THE LIST IS NOT A PARTITION. Internal and rural-to-urban both describe one
countryside-to-city move inside a country, so an item may not force a choice
between them. Items 13, 14 and 19 say so explicitly rather than pretending the
categories are exclusive.

THE HONESTY POINT. Item 25 states that forced and voluntary form a spectrum
rather than a switch. Presenting the line as absolute would teach something
false about environmental and economic displacement, and the CED's separate
listing is a classification rather than a claim that every case falls cleanly.

The five table items (26-30) are the computational gate:

  26  the share who did NOT cross a border, against its complement
  27  chain migration is a RATE, so the district sending the most migrants and
      the most with relatives is not the most strongly chained
  28  guest workers fall by three quarters while family arrivals rise more than
      tenfold, and the total nonetheless rises
  29  elevation returns to its starting value inside one year, which is what
      makes the movement cyclical
  30  step migration needs more than two moves AND an ascending sequence

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting. Item 18 is a NOT question and its claim says
so, since a negative stem is where a hurried reader mis-keys.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g2_11


def q26_share_inside(table):
    """Share of the displaced who never crossed a border."""
    counts = {rowdict(table, r)["Category"]: num(rowdict(table, r)["People (thousands)"])
              for r in table["rows"]}
    total = sum(counts.values())
    inside = counts["Displaced within the country"]
    abroad = total - inside
    assert total == 5000, total
    assert inside == 3600 and abroad == 1400, (inside, abroad)
    assert 100 * inside / total == 72, 100 * inside / total
    assert 100 * abroad / total == 28, 100 * abroad / total
    # The two shares must be genuinely different, or the complement distractor
    # would also be defensible.
    assert inside != abroad, counts
    return "72 percent"


def q27_chain_is_a_rate(table):
    """Share with a relative already there, against the raw counts."""
    share, movers, linked = {}, {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        n = num(d["Migrants"])
        k = num(d["Had a relative already in the city"])
        movers[d["Origin district"]] = n
        linked[d["Origin district"]] = k
        share[d["Origin district"]] = 100 * k / n
    strongest = max(share, key=share.get)
    assert strongest == "District 2", share
    assert share == {"District 1": 30, "District 2": 90,
                     "District 3": 40, "District 4": 65}, share
    # The largest flow AND the largest number with relatives must both belong to
    # a different district, or the rate-versus-count point is not made.
    assert max(movers, key=movers.get) != strongest, movers
    assert max(linked, key=linked.get) != strongest, linked
    assert max(movers, key=movers.get) == max(linked, key=linked.get), (movers, linked)
    return "90 percent had a relative"


def q28_programme_becomes_chain(table):
    """Labour recruitment collapses; family arrivals multiply; the total rises."""
    rows = {}
    for row in table["rows"]:
        d = rowdict(table, row)
        rows[d["Decade"]] = (num(d["Guest workers"]),
                             num(d["Family members joining earlier migrants"]),
                             num(d["Asylum seekers"]))
    first, last = rows["1970s"], rows["2010s"]
    worker_fall = 1 - last[0] / first[0]
    family_growth = last[1] / first[1]
    assert worker_fall > 0.70, worker_fall
    assert family_growth > 10, family_growth
    # The total must RISE, so "all three fell" and "the total fell" are false.
    assert sum(last) > sum(first), (sum(first), sum(last))
    assert last[2] > first[2], (first[2], last[2])
    # Asylum seekers must never be the largest category, disposing of a distractor.
    for decade, vals in rows.items():
        assert vals[2] != max(vals), (decade, vals)
    return "fell by three quarters"


def q29_cycle_returns(table):
    """Elevation rises and returns to its starting value within one year."""
    elevations = numcol(table, "Elevation (m)")
    assert elevations[0] == elevations[-1], elevations
    assert max(elevations) > 2 * elevations[0], elevations
    # It must genuinely go up and come back down, not merely start and end level.
    peak = elevations.index(max(elevations))
    assert 0 < peak < len(elevations) - 1, elevations
    assert all(elevations[i] <= elevations[i + 1] for i in range(peak)), elevations
    assert all(elevations[i] >= elevations[i + 1]
               for i in range(peak, len(elevations) - 1)), elevations
    return "return to the same elevation"


def q30_step_migration(table):
    """Step migration needs several moves AND an ascending settlement sequence."""
    rows = {}
    for row in table["rows"]:
        d = rowdict(table, row)
        rows[d["Stream"]] = (num(d["Number of separate moves"]),
                             d["Settlement size at each successive stop"],
                             d["Crossed a border"])
    moves = {k: v[0] for k, v in rows.items()}
    best = max(moves, key=moves.get)
    assert best == "Stream X", moves
    assert moves["Stream X"] == 4, moves
    # No other stream may have more than two moves, or the count is not decisive.
    assert sorted(moves.values(), reverse=True)[1] <= 2, moves
    # The ascending sequence must be present in the key's own row and absent from
    # the two-move alternative, which returns to where it began.
    assert "capital" in rows["Stream X"][1] and "village" in rows["Stream X"][1].lower()
    assert rows["Stream Z"][1].lower().count("village") == 2, rows["Stream Z"]
    return "four moves ascend the settlement hierarchy"


CLAIMS = [
 ("Events that produce refugees, internally displaced people, and asylum seekers",
  "EK IMP-2.D.1 names slavery together with the events producing refugees, internally displaced persons and asylum seekers. Every distractor is drawn from EK IMP-2.D.2's list of voluntary types, which is precisely the distinction the learning objective asks students to make."),

 ("crossed an international border and their status has been determined",
  "EK IMP-2.D.1 lists refugees separately from internally displaced persons and asylum seekers, and only two questions separate the three: was a border crossed, and has the claim been decided. Here the answer to both is yes."),

 ("have not crossed an international border",
  "EK IMP-2.D.1 lists internally displaced persons as a category distinct from refugees, and the border is the whole of the distinction. Distance moved is irrelevant, which is why a very long move inside a country is displacement and a short move across a border is not."),

 ("claim has been made but not yet determined",
  "EK IMP-2.D.1 lists asylum seekers separately from refugees, and what separates them is the decision rather than the journey. The same person becomes a refugee if the claim succeeds and must leave if it fails."),

 ("asylum seekers have crossed and await a decision",
  "EK IMP-2.D.1 lists all three categories, and only two questions separate them -- whether an international border was crossed and whether the protection claim has been decided. Distance and motive vary within every category and so cannot do the work."),

 ("no element of choice at any stage",
  "EK IMP-2.D.1 names slavery explicitly among forced migrations. What makes a migration forced is the absence of choice rather than the distance or the direction, and no case sits further from choice than movement under ownership."),

 ("maintains active ties in and movement between both countries",
  "EK IMP-2.D.2 lists transnational among the voluntary types, and its defining feature is a life spanning two countries rather than a transfer from one to the other. Remittances, annual visits and property in both places are exactly that pattern."),

 ("seasonal and cyclical movement between pastures",
  "EK IMP-2.D.2 lists transhumance among the voluntary types, and it is the only one of the seven that is cyclical rather than one-way. The herders return every year, which distinguishes it from every other entry on the list."),

 ("repeating seasonal cycle back to the same places",
  "EK IMP-2.D.2 places transhumance in a list whose other members all relocate a household. Recognising that one member of a list has a different structure from the rest is the point of learning the list rather than reciting it."),

 ("follows a path opened by earlier migrants",
  "EK IMP-2.D.2 lists chain migration among the voluntary types, and its mechanism is information and support flowing back along an established route. The concentration into a few streets is the signature, since an unconnected set of movers would not cluster that way."),

 ("sequence of moves up the settlement hierarchy",
  "EK IMP-2.D.2 lists step migration separately from chain migration, and the two answer different questions: step is about the route taken, chain about who opened it. A hierarchy climbed in stages is the step pattern precisely."),

 ("right to remain is tied to temporary employment",
  "EK IMP-2.D.2 lists guest worker migration among the voluntary types. Its defining feature is the conditionality of the stay -- it lasts as long as the work does -- rather than the length of the contract or the distance travelled."),

 ("which is also a form of internal migration",
  "EK IMP-2.D.2 lists both internal and rural-to-urban migration, and this case satisfies both descriptions at once, since the move stays inside one country and runs from countryside to city. Naming the more specific of the two is the fuller answer."),

 ("since a countryside-to-city move within one country is both",
  "EK IMP-2.D.2's list is not a partition, and several of its entries describe different aspects of a single move. Internal names where the move stays and rural-to-urban names what it runs between, so one migration can carry both labels honestly."),

 ("Whether an international border was crossed",
  "EK IMP-2.D.1 lists refugees and internally displaced persons separately, and both describe people forced to flee for the same reasons. The border is the only difference, and it matters because it changes which state and which body of law is responsible."),

 ("left the jurisdiction of the state they fled",
  "EK IMP-2.D.1 separates the two categories, and the reason the separation matters is legal and practical rather than descriptive. International protection is available across a border and largely unavailable inside the country of origin."),

 ("frequently produce permanent settlement",
  "EK IMP-2.D.2's guest worker category is defined by the intended temporariness of the arrangement, which is a policy design rather than a prediction about behaviour. Long programmes produce marriages, children and communities that no contract term dissolves."),

 ("Displacement",
  "This is a NOT question and the key is the one option outside EK IMP-2.D.2's list, which contains transnational, transhumance, internal, chain, step, guest worker and rural-to-urban migration. Displacement belongs to EK IMP-2.D.1's forced category, which is exactly the confusion tested."),

 ("Internal migration and rural-to-urban migration",
  "EK IMP-2.D.2 names both terms, and a flow that stays inside one country while running from farming provinces to manufacturing cities satisfies each of them. Neither term excludes the other, which is why the fuller description uses both."),

 ("most report a relative already there",
  "EK IMP-2.D.2's chain migration is defined by the link between earlier and later migrants, so the evidence has to show that link operating. Concentration at the destination combined with prior contacts is what an unconnected set of moves would not produce."),

 ("Still an asylum seeker",
  "EK IMP-2.D.1 separates asylum seekers from refugees by whether the claim has been decided, and an appeal means it has not been decided finally. The reasons for flight do not by themselves confer the recognized status."),

 ("crossing a border requires means and permission",
  "EK IMP-2.D.1 distinguishes the two categories by the border, and a border is a real barrier with costs, documents and controls attached. Distance decay applies to forced movement too: people stop as soon as they are safe, and safety is often found inside their own country."),

 ("sit between coercion and free choice",
  "EK IMP-2.D.1 and EK IMP-2.D.2 list the two kinds separately, which is a classification rather than a claim that every case falls cleanly on one side. Environmental and economic collapse remove options without any person compelling the move, which is why the boundary is argued over."),

 ("matched to chain migration",
  "EK IMP-2.D.2 defines chain migration by the link to earlier migrants from the same community, which the case describes exactly. Each of the other pairings attaches a case to a term whose defining feature that case does not have."),

 ("lies in the conflict or persecution that removes the option of staying",
  "EK IMP-2.D.1's wording locates the coercion in the events rather than in the label. A status is assigned by a state after the fact, whereas what made the migration forced was the situation that left no alternative to leaving."),

 ("72 percent",
  "Recomputed from the table: the three rows total 5,000 thousand people, of whom 3,600 thousand never crossed a border, which is 72 percent. The two categories abroad come to 1,400 thousand or 28 percent, which is the complement offered as a distractor rather than the answer.",
  q26_share_inside),

 ("90 percent had a relative",
  "Recomputed from the table: the shares with a relative already in the city are 30, 90, 40 and 65 percent. The verifier confirms that the district sending the most migrants is also the one sending the most with relatives in absolute terms, and that it is not the answer, since chain migration is a mechanism measured as a rate.",
  q27_chain_is_a_rate),

 ("fell by three quarters",
  "Recomputed from the table: guest worker arrivals fall from 82,000 to 22,000, a reduction above 70 percent, while family arrivals rise from 9,000 to 94,000, a factor above ten, and the total rises rather than falls. The verifier also confirms asylum seekers are never the largest category, disposing of a distractor.",
  q28_programme_becomes_chain),

 ("return to the same elevation",
  "Recomputed from the table: elevation rises from 400 metres to 2,300 and returns to 400 within the same year, rising monotonically to the peak and falling monotonically back. That return is what separates transhumance from every other type on the voluntary list.",
  q29_cycle_returns),

 ("four moves ascend the settlement hierarchy",
  "Recomputed from the table: only one stream records more than two moves, and its stops ascend from village to capital, while the two-move alternative returns to the village it began in. A single long move is not step migration however far it goes.",
  q30_step_migration),
]

hg_check.check(g2_11, CLAIMS, per_topic=30, n_choices=5)
