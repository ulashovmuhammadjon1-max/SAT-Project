"""Key audit for AP HUMAN GEOGRAPHY 4.9 Challenges to Sovereignty.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. One learning objective, four essential knowledge statements:

    SPS-4.B.1  Devolution occurs when states fragment into autonomous regions;
               subnational political-territorial units, such as those within
               Spain, Belgium, Canada, and Nigeria; or when states disintegrate,
               as happened in Sudan and the former Soviet Union.
    SPS-4.B.2  Advances in communication technology have facilitated devolution,
               supranationalism, and democratization.
    SPS-4.B.3  Global efforts to address transnational and environmental
               challenges and to create economies of scale, trade agreements,
               and military alliances help to further supranationalism.
    SPS-4.B.4  Supranational organizations -- including the UN, NATO, the EU,
               ASEAN, the Arctic Council, and the African Union -- can challenge
               state sovereignty by limiting the economic or political actions of
               member states.

B.1 supplies items 1-4, 18 and 27; B.2 items 5, 6, 7, 19, 25, 28 and 29; B.3
items 8, 9, 10, 11, 20 and 21; B.4 items 12-16, 22, 23, 24 and 26. Item 17 and
item 30 draw on the set as a whole.

THE ONE CLAIM THIS MODULE IS MOST CAREFUL ABOUT is the verb in SPS-4.B.4.
Supranational organizations CAN CHALLENGE sovereignty BY LIMITING the economic
or political ACTIONS of member states. They are not said to abolish sovereignty,
to override it, or to govern members. Items 13, 14, 15, 16, 22 and 30 are keyed
against the stronger reading, and item 22 supplies the reason it is wrong: a
body with no coercive apparatus of its own operates through the members'
continuing consent. A state that agreed to a limit and may withdraw from it has
been constrained by its own bargain, which is a genuine challenge and not a
replacement.

THE SECOND STRUCTURAL POINT is that this topic and 4.8 pull in opposite
directions and the CED puts them in the same enduring understanding. Devolution
moves authority down; supranationalism moves it up. SPS-4.B.2 credits the same
technological change with facilitating both, so a student who reads them as
alternatives has misread the statement. Items 7, 17, 18 and 25 are built on that
and item 25 keys directly against the "they are opposites, therefore mutually
exclusive" inference.

NAMING REAL PLACES IS PERMITTED HERE, unlike in Topics 4.7 and 4.8, because this
statement names them itself. Spain, Belgium, Canada and Nigeria are the CED's
own examples of states containing subnational political-territorial units, and
Sudan and the former Soviet Union are its own examples of disintegration. Items
3 and 4 turn on keeping those two lists apart, which is the mistake the pairing
invites. No claim about any of the six goes beyond what SPS-4.B.1 states, and no
organization outside SPS-4.B.4's list is asserted to be supranational -- item 12
only says the World Health Assembly IS NOT NAMED THERE, which is a fact about
the CED rather than about the body.

The three table items (26, 27, 28) are the computational gate:

  26  counts constraints per member state, and asserts the spread is 4/3/1/0 --
      the item's whole point is that membership in one bloc does not mean the
      same loss of freedom of action, which a tie would destroy
  27  finds the single case whose original state no longer exists, and pins the
      number of successor states
  28  both series are checked to rise in every decade, and the endpoints are
      pinned; the recompute deliberately does NOT assert causation, because
      item 29 keys against exactly that inference

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written. One correction was made during the pass: item 26's `why` originally
described the three non-keyed states as recording "three, two and none"
constraints when the record gives three, one and none. The recompute below now
pins all four counts, so that sentence cannot drift from the table again.
"""
import re

import geo_check
import g4_9


def q26_count_constraints(table):
    """Count the limits each member state has accepted, from the record itself."""
    counts = {}
    for row in table["rows"]:
        state, tariff, currency, negotiates, court = row
        n = 0
        n += tariff == "Yes"          # bound by the common external tariff
        n += currency == "No"         # gave up its own currency
        n += negotiates == "No"       # cannot negotiate trade deals alone
        n += court == "Yes"           # bound by the bloc's court
        counts[state] = n
    # The spread is the point of the item: same bloc, four different degrees of
    # constraint. A tie at the top would make the key indefensible.
    assert counts == {"State 1": 4, "State 2": 3, "State 3": 1, "State 4": 0}, counts
    row1 = {r[0]: r for r in table["rows"]}["State 1"]
    assert row1[2] == "No" and row1[3] == "No", row1
    return "given up its own currency and independent trade negotiation"


def q27_which_disintegrated(table):
    """Disintegration is the case in which the original state no longer exists."""
    words = {2: "two", 3: "three", 4: "four", 5: "five"}
    gone = [r for r in table["rows"] if r[1] == "No"]
    assert len(gone) == 1, gone
    case = gone[0]
    successors = int(case[2])
    assert successors > 1, case
    # Every other case keeps one sovereign state, so only this one can be read
    # as disintegration rather than as devolution within a surviving state.
    for r in table["rows"]:
        if r is not case:
            assert r[1] == "Yes" and int(r[2]) == 1, r
    return f"{words[successors]} sovereign states occupy the territory"


def q28_both_series_rise(table):
    """Access and movement counts both rise in every decade; endpoints pinned."""
    access = [float(r[1]) for r in table["rows"]]
    movements = [int(r[2]) for r in table["rows"]]
    assert len(access) == 4, access
    assert all(b > a for a, b in zip(access, access[1:])), access
    assert all(b > a for a, b in zip(movements, movements[1:])), movements
    assert access[0] == 4 and access[-1] == 89, access
    assert movements[0] == 2 and movements[-1] == 7, movements
    # Deliberately NOT asserting causation: item 29 keys against that inference,
    # and the keyed choice here stops at "is consistent with".
    return "from 4 percent to 89 percent"


CLAIMS = [
 ("fragmented into autonomous regions",
  "EK SPS-4.B.1 states that devolution occurs when states fragment into autonomous regions or into subnational political-territorial units. The state in the stem survives and keeps every power it did not transfer, which is what separates fragmentation from the disintegration the same statement describes."),

 ("the state ceases to exist and separate states replace it",
  "EK SPS-4.B.1 names two outcomes under one heading -- fragmentation into autonomous regions and disintegration -- and the difference between them is whether the original state remains. The statement attaches neither outcome to wealth, to violence or to permanence."),

 ("Sudan and the former Soviet Union",
  "EK SPS-4.B.1 gives Sudan and the former Soviet Union as its examples of states that disintegrated, and gives Spain, Belgium, Canada and Nigeria as its examples of states containing subnational political-territorial units. The item tests keeping the CED's own two lists apart."),

 ("subnational political-territorial units",
  "EK SPS-4.B.1 names Spain, Belgium, Canada and Nigeria as examples of subnational political-territorial units within states rather than as states that broke apart. All four remain single sovereign states, which is why they illustrate fragmentation and not disintegration."),

 ("communication technology have facilitated devolution",
  "EK SPS-4.B.2 states that advances in communication technology have facilitated devolution, supranationalism and democratization. A regional movement able to reach every one of its speakers without the central state's presses or permission is the mechanism that claim describes."),

 ("supranationalism, and democratization",
  "EK SPS-4.B.2 names exactly three processes, and the interesting feature of the statement is that they point in different directions. The same fall in the cost of communication is credited with helping authority move down to regions, up to supranational bodies and outward to citizens."),

 ("one downward to regions and one upward to bodies above it",
  "EK SPS-4.B.2 lists devolution and supranationalism together and enduring understanding SPS-4 groups both as challenges to state sovereignty. Cheap communication lowers the cost of coordinating inside one region and across many states alike, and the state loses relative standing in either case."),

 ("transnational and environmental challenges",
  "EK SPS-4.B.3 names global efforts to address transnational and environmental challenges among the things that further supranationalism. A shared fish stock is the standard instance of a problem whose geography does not correspond to any single state's boundaries."),

 ("Ethnic separatism",
  "EK SPS-4.B.3 names transnational and environmental challenges, economies of scale, trade agreements and military alliances. Ethnic separatism appears instead in EK SPS-4.A.1's list of devolutionary factors, which is the statement pulling in the opposite direction."),

 ("acting as one buyer",
  "EK SPS-4.B.3 names the creation of economies of scale among the efforts that further supranationalism. Bargaining weight is precisely what a small state lacks and what pooling supplies, which is the material reason small states join such arrangements."),

 ("North Atlantic Treaty Organization",
  "EK SPS-4.B.3 names military alliances among the drivers of supranationalism and EK SPS-4.B.4 names NATO among the supranational organizations. A pledge that an attack on one is an attack on all is the defining commitment of a military alliance rather than of a trading or environmental body."),

 ("the World Health Assembly",
  "EK SPS-4.B.4 names six bodies -- the UN, NATO, the EU, ASEAN, the Arctic Council and the African Union -- and the World Health Assembly is not among them. The claim keyed here is about what the CED's list contains, not about the nature of any body outside it."),

 ("limiting the economic or political actions",
  "EK SPS-4.B.4 says supranational organizations can challenge state sovereignty by limiting the economic or political actions of member states. The verb is doing the work: a limit on what a state may do is a real constraint but is weaker than abolition, direct government or border change."),

 ("limited an economic action",
  "EK SPS-4.B.4 describes exactly this kind of constraint, in which the organization limits an economic action the state would otherwise be free to take. The state keeps every power the treaty does not reach and keeps the power to leave, so this is a challenge to sovereignty rather than its end."),

 ("freedom to conduct its own external relations",
  "EK SPS-4.B.4 names political as well as economic actions among the things a supranational organization may limit. Concluding treaties with foreign states is one of the classic marks of sovereignty, so giving it up in one field is a political constraint as well as a commercial one."),

 ("retains the power to withdraw",
  "EK SPS-4.B.4 says such organizations CAN CHALLENGE sovereignty by limiting actions, which is a claim about constraint rather than about abolition. A state that accepted the limits by agreement and may still leave has been bound by its own bargain, which is why the framework's wording stops where it does."),

 ("so the state holds less in both directions",
  "EK SPS-4.B.1 describes states fragmenting into autonomous regions and EK SPS-4.B.4 describes organizations above the state limiting what it may do. Enduring understanding SPS-4 groups both as challenges to sovereignty, which puts the state at the level squeezed from below and above at once."),

 ("separation is made less costly",
  "EK SPS-4.B.1 covers fragmentation and EK SPS-4.B.2 lists devolution and supranationalism as facilitated by the same changes. A wider economic framework above the state reduces the price a departing region would pay, which is why the two processes so often appear together in one argument."),

 ("harder for a government to control than a printing press",
  "EK SPS-4.B.2 names democratization among the three processes that communication technology has facilitated. The common mechanism across all three is the loss of the state's former control over who can reach a large audience, which bears on internal politics as much as on regional organizing."),

 ("help to further supranationalism",
  "EK SPS-4.B.3 names efforts to address transnational and environmental challenges among the drivers of supranationalism. Emissions are the standard case of a harm generated inside one state's borders whose effects disregard them entirely, so no single state can address it alone."),

 ("worth more than the freedom of action it gives up",
  "EK SPS-4.B.3 lists trade agreements, economies of scale, military alliances and shared challenges as the things furthering supranationalism, and each of those names a benefit. Membership is a bargain in which a state exchanges some freedom of action for something it cannot obtain by itself."),

 ("continuing consent and the costs of defiance",
  "EK SPS-4.B.4 says these organizations CAN CHALLENGE sovereignty by limiting actions, which is deliberately weaker than saying they govern their members. Enforcement runs through membership, reciprocity and reputation rather than through any coercive apparatus the body owns."),

 ("formed around different problems",
  "EK SPS-4.B.4 names both the Arctic Council and the European Union in one list, and EK SPS-4.B.3 names both environmental challenges and economies of scale among the drivers. The list is mixed on purpose: supranationalism grows out of several different kinds of shared problem."),

 ("composed of states and acts by their agreement",
  "EK SPS-4.B.4 describes supranational organizations as bodies whose members are states and whose effect is to limit those states' actions. The framework never attributes territory or a population of its own to such a body, which is what keeps it distinct from a state."),

 ("nothing prevents both from operating at once",
  "EK SPS-4.B.2 lists devolution and supranationalism together as facilitated by advances in communication technology, so the framework itself pairs them rather than opposing them. A state can transfer authority to its regions and accept limits from a bloc in the same decade."),

 ("given up its own currency and independent trade negotiation",
  "Recomputed from the record: the four member states have accepted four, three, one and none of the four listed constraints, so belonging to one bloc plainly does not mean the same loss of freedom of action. EK SPS-4.B.4 describes supranational organizations as limiting the economic or political actions of member states, and the record counts those limits.",
  ),

 ("five sovereign states occupy the territory",
  "Recomputed from the record: exactly one case reports that the original state no longer exists, and five sovereign states now occupy its territory, while each of the other three keeps a single sovereign state. EK SPS-4.B.1 distinguishes fragmentation into autonomous regions from disintegration, and survival of the original state is the dividing line.",
  ),

 ("from 4 percent to 89 percent",
  "Recomputed from the figures: household internet access rises in every decade from 4 to 89 percent and the count of active autonomy movements rises in every decade from two to seven. EK SPS-4.B.2 says communication technology has FACILITATED devolution, so a record consistent with the claim is the most the figures can support.",
  ),

 ("does not establish that one caused the other",
  "EK SPS-4.B.2's verb is 'facilitated', which asserts that something was made easier rather than that it was produced. Two series rising across the same four decades is consistent with that without demonstrating it, since a span of decades carries every other change as well."),

 ("challenged from below by devolution and from above",
  "EK SPS-4.B.1 supplies the downward challenge, EK SPS-4.B.4 the upward one, and EK SPS-4.B.2 the technological change that facilitated both. Each rejected summary states one of those relationships more strongly than the CED does, and overstating SPS-4.B.4 is the commonest of those errors."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"4.9 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"4.9 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_count_constraints,
    27: q27_which_disintegrated,
    28: q28_both_series_rise,
}

geo_check.check(g4_9, ANCHORS, TABLE_NOTES)
