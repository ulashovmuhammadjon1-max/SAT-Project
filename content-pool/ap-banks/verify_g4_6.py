"""Key audit for AP HUMAN GEOGRAPHY 4.6 Internal Boundaries.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart. Claims are checked here for length and for letter references, which
geo_check does not see.

WHAT MAY BE CITED. This topic has exactly one essential-knowledge statement:

    IMP-4.B.5  Voting districts, redistricting, and gerrymandering affect
               election results at various scales.

Three terms and one claim. The CLAIM is the citable part and it is stronger than
it looks: internal boundaries CHANGE OUTCOMES. Items 1, 9, 13, 18, 22, 26, 28
and 30 are keyed to it, and items 26 and 28 prove it with data rather than
asserting it -- 28 in particular holds the votes constant and varies only the
map, which is the cleanest demonstration available.

The phrase AT VARIOUS SCALES is also citable and item 11 uses it: the same
process operates for a municipal ward and a national constituency.

WHAT THE CED DOES NOT DEFINE, and which every key therefore argues from the
definitions in the module header: voting district, redistricting, gerrymandering,
packing, cracking and malapportionment. Three distinctions carry most of the
module:

  * redistricting vs gerrymandering (item 3) -- every gerrymander is a
    redistricting and most redistricting is not a gerrymander. The difference is
    INTENT, which is also why item 25 keys to the fact that two experts can
    disagree about the same map.
  * packing vs cracking (items 6, 7, 8, 20, 26) -- opposite methods, identical
    purpose, because a surplus vote in a safe district is wasted exactly as a
    losing vote is.
  * gerrymandering vs malapportionment (items 12, 21, 27) -- shape versus size.
    Malapportionment needs no intent at all and commonly arises from simply not
    redistricting, which item 16 makes explicit.

TWO EDITORIAL CONSTRAINTS OBSERVED THROUGHOUT.

First, no item names a real party or asks which side benefits from any real
map. Groups are lettered. EK IMP-4.B.5 describes a mechanism, and a key
asserting who gains from a particular country's districts would be a partisan
claim rather than a geographic one.

Second, item 23 keys to the position that drawing a district so a minority can
elect a representative is judged differently from a partisan gerrymander,
because purpose is what distinguishes them. That is a genuinely contested area
of law and the key is worded as a distinction of purpose rather than as an
endorsement, which is as far as the CED's own sentence supports.

The three table items (26, 27, 28) are the computational gate:

  26  60 percent of the votes converting into 40 percent of the seats
  27  a sevenfold difference in the weight of a vote
  28  identical total support, different seat counts, from the map alone

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import re

import geo_check
import g4_6


def q26_packing(table):
    """60 percent of the votes, 40 percent of the seats."""
    x = y = 0.0
    seats_x = seats_y = 0
    margins = []
    for row in table["rows"]:
        vx = float(row[1].replace(",", ""))
        vy = float(row[2].replace(",", ""))
        x += vx
        y += vy
        if vx > vy:
            seats_x += 1
            margins.append(vx / vy)
        else:
            seats_y += 1
    total = x + y
    assert x == 30000 and total == 50000, (x, total)
    assert 100 * x / total == 60, 100 * x / total
    assert seats_x == 2 and seats_y == 3, (seats_x, seats_y)
    # The two seats it wins must be won overwhelmingly -- that is what makes the
    # surplus votes wasted rather than merely unlucky.
    assert all(m > 8 for m in margins), margins
    # And its seat share must fall below its vote share.
    assert seats_x / (seats_x + seats_y) < x / total
    return "Two seats with 60 percent of the vote"


def q27_malapportionment(table):
    """Ratio of the largest district to the smallest, each electing one member."""
    sizes = {row[0]: float(row[1].replace(",", "")) for row in table["rows"]}
    assert len(sizes) == 4, sizes
    lo, hi = min(sizes.values()), max(sizes.values())
    assert lo == 20000 and hi == 140000, sizes
    ratio = hi / lo
    assert ratio == 7, ratio
    words = {2: "Twice", 4: "Four times", 7: "Seven times"}
    return words[int(ratio)]


def q28_map_decides(table):
    """Same total support under both maps; different numbers of majorities."""
    m1, m2 = [], []
    for row in table["rows"]:
        m1.append(float(row[1]))
        m2.append(float(row[2]))
    assert len(m1) == len(m2) == 5, (m1, m2)
    # Equal districts, so the mean share is the group's overall support.
    mean1 = sum(m1) / len(m1)
    mean2 = sum(m2) / len(m2)
    assert mean1 == mean2 == 30, (mean1, mean2)
    seats1 = sum(1 for v in m1 if v > 50)
    seats2 = sum(1 for v in m2 if v > 50)
    assert seats1 == 0 and seats2 == 1, (seats1, seats2)
    return "no seats under one map and one seat under the other"


CLAIMS = [
 ("affect election results at various scales",
  "EK IMP-4.B.5 states that voting districts, redistricting and gerrymandering affect election results at various scales. The claim concerns outcomes rather than eligibility, and the phrase about scales is what places it in a geography course."),

 ("area whose residents elect one representative",
  "EK IMP-4.B.5 names voting districts without defining them, and the standard definition is the geographic unit from which a representative is chosen. Because the unit is geographic, moving its boundary changes which voters are counted together."),

 ("Every gerrymander is a redistricting",
  "EK IMP-4.B.5 names redistricting and gerrymandering separately, which implies they are not identical. Redistricting is the routine redrawing of lines after population shifts, while gerrymandering is doing so with a particular result in view."),

 ("equal representation requires the lines to be adjusted",
  "EK IMP-4.B.5 names redistricting as one of the three things affecting election results. A district that has gained or lost population relative to its neighbours no longer represents an equal number of people, and a census is what reveals the imbalance."),

 ("deliberately so as to advantage a particular party",
  "EK IMP-4.B.5 names gerrymandering alongside redistricting and voting districts as influences on election results. The distinguishing feature is intent: drawing lines becomes a gerrymander when the purpose is advantage rather than equality."),

 ("surplus votes elect nobody",
  "Packing concentrates opposing voters into a few districts they win overwhelmingly, so every vote above the winning margin is wasted. EK IMP-4.B.5 makes gerrymandering a way of affecting results, and this is one of its two standard methods."),

 ("split so that it is a minority everywhere",
  "Cracking splits a group across many districts so that it is a majority in none, converting a substantial minority into no seats at all. It is the opposite method from packing and serves exactly the same purpose."),

 ("share of seats falls below its share of the vote",
  "The two techniques are opposite in method and identical in purpose. A vote cast for a loser elects nobody and so does a vote cast for a winner far beyond the needed margin, which is the arithmetic behind EK IMP-4.B.5's claim about affected results."),

 ("converts its votes into seats inefficiently",
  "EK IMP-4.B.5 states that voting districts and how they are drawn affect election results. A seat share below a vote share means the group's votes are concentrated where they are not needed or dispersed where they are not enough, which district geography determines."),

 ("extremely irregular shape that split towns and neighbourhoods",
  "EK IMP-4.B.5 names gerrymandering as an influence on results, and shape is the most visible symptom because hitting a target usually requires abandoning natural units. Compactness, contiguity and respect for existing boundaries are what an untargeted map tends to produce."),

 ("municipal wards, provincial constituencies, and national legislatures",
  "EK IMP-4.B.5 ends with the phrase 'at various scales', which generalizes the claim beyond national legislatures. A city ward and a national constituency are drawn by the same kind of decision and are open to the same manipulations."),

 ("Malapportionment, which makes votes unequal in weight",
  "Unequal district populations make one voter's ballot worth several of another's, which is a defect of size rather than of shape. It commonly arises from failing to redistrict as population moves, so it can exist with no intent to advantage anyone."),

 ("depends on where the lines are drawn",
  "EK IMP-4.B.5 states that voting districts and redistricting affect election results, and holding the votes fixed while varying the map is the cleanest possible demonstration. The difference in outcome can come only from the boundaries."),

 ("have an interest in the outcome",
  "EK IMP-4.B.5 makes gerrymandering a real influence on results, which is what creates the conflict of interest for legislators drawing their own districts. The design response is to move the decision to a body whose seats do not depend on the map."),

 ("compact, contiguous, and as far as possible respectful of existing communities",
  "EK IMP-4.B.5's gerrymandering is defined against something, and that something is a set of neutral criteria. Compactness, contiguity, equal population and respect for existing communities are the standard tests, and none of them refers to how anyone votes."),

 ("progressively under-represented",
  "EK IMP-4.B.5 names redistricting among the processes affecting results, and failing to do it is itself a decision with consequences. A district whose population has doubled still elects one member, so each of its voters holds half the influence of a voter elsewhere."),

 ("can win fewer seats than a group with the same total votes spread more evenly",
  "Seats are won district by district, so votes beyond the needed margin in a safe district elect nobody. A group's spatial distribution therefore matters independently of its total support, which is why concentration can be a disadvantage under this kind of system."),

 ("same voters now help decide a different contest",
  "EK IMP-4.B.5 states that redistricting affects election results. Moving a bloc of voters from one district to another changes the balance in both districts at once, which is why the placement of a single suburb can be fought over."),

 ("Supranational organizations",
  "This is a NOT question, and EK IMP-4.B.5 names voting districts, redistricting and gerrymandering as the things affecting election results. Supranational organizations belong to Topic 4.9's statement about challenges to sovereignty rather than to this one about internal boundaries."),

 ("wasted in exactly the way packing is designed to achieve",
  "A district elects one representative regardless of the winning margin, so a vote beyond the threshold changes nothing. Packing works precisely because surplus votes are as wasted as losing ones, which is what EK IMP-4.B.5's claim about affected results rests on."),

 ("addresses malapportionment but leaves gerrymandering by shape",
  "Equal population constrains size and says nothing about which voters are placed together. A map can satisfy an equal-population rule exactly while pursuing any partisan target, which is why compactness rules are treated as a separate safeguard."),

 ("converted into political power",
  "EK IMP-4.B.5 sits inside a learning objective covering international AND internal boundaries, and it attaches an effect on election results to the internal ones. A line that decides who governs is doing political work of the same order as a state border."),

 ("purpose is representation rather than partisan advantage",
  "EK IMP-4.B.5 makes district drawing an influence on results without saying that every deliberate use of it is illegitimate. Purpose is what distinguishes the cases, and drawing to enable representation is a different purpose from drawing to entrench a party; the key states the distinction rather than endorsing any particular map."),

 ("intent must be inferred from shape, outcome, and the process",
  "EK IMP-4.B.5 names gerrymandering without supplying a test for it, and the distinguishing feature is purpose rather than any measurable property. A very irregular map can have an innocent explanation and a tidy one can have been drawn to a target."),

 ("packs the group's strongest areas into a few districts and cracks the remainder",
  "The two techniques are complementary rather than alternative: packing wastes surplus votes and cracking wastes losing ones, so applying both to one group wastes as many of its votes as possible. EK IMP-4.B.5's claim about gerrymandering affecting results is at its maximum here."),

 ("Two seats with 60 percent of the vote",
  "Recomputed from the votes: Group X takes 30,000 of 50,000 cast, or 60 percent, and wins the first two districts by more than nine to one while losing the other three narrowly. The verifier confirms its seat share falls below its vote share, which is what packing produces.",
  ),

 ("Seven times as much",
  "Recomputed from the registers: 140,000 voters against 20,000 for one representative each is a ratio of exactly seven. This is malapportionment, a defect of unequal size rather than of shape, and it requires no partisan intent to arise.",
  ),

 ("no seats under one map and one seat under the other",
  "Recomputed from the shares: both maps average exactly 30 percent across five equal districts, so the group's total support is identical, yet it holds a majority in none under one map and in one district under the other. Only the boundaries differ.",
  ),

 ("do not stand for election in those districts",
  "EK IMP-4.B.5 makes gerrymandering a real influence on election results, which means legislators drawing the lines are selecting part of their own electorate. Removing the decision from those with a stake in it addresses the cause rather than the symptom."),

 ("converts a fixed set of votes into a set of seats",
  "EK IMP-4.B.5 states that voting districts, redistricting and gerrymandering affect election results at various scales, which is a claim about mechanism and generality at once. Treating the map as part of the result rather than as its container is what the statement asks students to understand."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"4.6 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"4.6 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_packing,
    27: q27_malapportionment,
    28: q28_map_decides,
}

geo_check.check(g4_6, ANCHORS, TABLE_NOTES)
