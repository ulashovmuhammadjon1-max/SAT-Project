"""Key audit for AP ENVIRONMENTAL SCIENCE 3.1 Generalist and Specialist Species.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
ERT-3.A.1 is the topic's only essential knowledge statement, and every key here
rests on it: specialist species TEND TO BE advantaged in habitats that REMAIN
CONSTANT, while generalist species TEND TO BE advantaged in habitats that ARE
CHANGING. The unit overview repeats it in the same words.

  which kind in a constant habitat  -- items 1, 7, 12, 14, 20, 26
  which kind in a changing habitat  -- items 2, 6, 8, 27, 28
  the comparison entire             -- items 3, 11, 13, 15, 17, 18, 19, 21,
                                       22, 23, 24, 25, 29, 30
  the hedge, TEND TO BE             -- items 4, 29
  what the framework does not supply-- items 5, 9, 10, 30

WHAT IS DELIBERATELY NOT ASKED. The framework never defines specialist or
generalist, anywhere in the course, so no item asks a student to sort a species
into one of the two. Item 5 keys that absence, and the two words appear here
only as labels on counts, exactly as the framework uses them.

TWO BOUNDARIES ARE MARKED RATHER THAN CROSSED. ERT-2.A.4 (topic 2.1) gives the
ORDER of losses as habitat is LOST, and ERT-2.E.1 (topic 2.3) gives the ISLAND
case of introduced generalists outcompeting specialists. Items 9 and 10 key the
DISTINCTION between this statement and each of those, naming the chain; no item
here is about fragmentation, islands or introductions.

THE SWAP IS THE HAZARD IN EVERY ITEM THAT NAMES BOTH KINDS, so the anchors for
items 3, 7, 11, 15, 17, 22 and 23 carry BOTH clauses. Half an anchor matches
the reversed distractor as readily as the key -- the defect found once already
in verify_e2_1.py.

DATA ITEMS: 11 to 24 carry tables, recomputed below by column header.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and EVERY data table in turn, and requires each
corruption to raise BEFORE the real gate runs. Several of these checks read a
relationship across a sorted gradient, which a reversal of every column
preserves; e_check flattens those tables next and the checks fail because a
flat column carries no gradient. ``python3 verify_e3_1.py --selftest`` is the
same run; the controls are not behind the flag.
"""
import sys

import cg_check as cg
import e_check
import e3_1

VAR = "Year to year variation in temperature and rainfall (index)"
SPEC = "Specialist species present"
GEN = "Generalist species present"
CHANGES = "Years in the period with a marked change in conditions"
SPECEND = "Specialist species present at the end of the period"
GENEND = "Generalist species present at the end of the period"
IDX = "Change in mean conditions over thirty years (index)"
DSPEC = "Change in the number of specialist species"
DGEN = "Change in the number of generalist species"
MARKED = "Marked changes in conditions recorded over twenty years"
SHARE = "Specialists as a percent of the species present"
WOBBLE = "Years per decade in which the water level varied by more than a metre"
SPECC = "Specialist species in the constant habitat"
SPECX = "Specialist species in the changing habitat"
GENC = "Generalist species in the constant habitat"
GENX = "Generalist species in the changing habitat"


def _rises(v):
    return all(v[i + 1] > v[i] for i in range(len(v) - 1))


def _falls(v):
    return all(v[i + 1] < v[i] for i in range(len(v) - 1))


def _by(table, key_header, *headers):
    keys = cg.col(table, key_header)
    order = sorted(range(len(table["rows"])), key=lambda i: keys[i])
    return [[cg.col(table, h)[i] for i in order] for h in headers]


def q11(table, item):
    spec, gen = _by(table, VAR, SPEC, GEN)
    assert _falls(spec), f"specialists must fall as variation rises; got {spec}"
    assert _rises(gen), f"generalists must rise as variation rises; got {gen}"
    return (f"sorted by year to year variation the specialists read {spec} and the "
            "generalists {0}, one strictly falling and the other strictly rising".format(gen))


def q12(table, item):
    labs = cg.labels(table)
    margin = {lab: s - g for lab, s, g in
              zip(labs, cg.col(table, SPEC), cg.col(table, GEN))}
    best = max(margin, key=margin.get)
    assert best == "Habitat 1", f"Habitat 1 must show the largest specialist margin; got {best}"
    assert margin[best] > 0, "'specialists never outnumber generalists' must be false"
    assert list(margin.values()).count(margin[best]) == 1, "the largest margin must be unique"
    var = dict(zip(labs, cg.col(table, VAR)))
    assert var[best] == min(var.values()), \
        "the habitat with the largest specialist margin must be the least variable one"
    return (f"the specialist margins are {margin} species, and the largest belongs to "
            f"{best}, whose variation index {var[best]:.0f} is the lowest")


def q13(table, item):
    labs = cg.labels(table)
    doubled = [lab for lab, s, g in zip(labs, cg.col(table, SPEC), cg.col(table, GEN))
               if g > 2 * s]
    assert doubled == ["Habitat 4"], \
        f"exactly Habitat 4 must have generalists at more than twice the specialists; got {doubled}"
    var = dict(zip(labs, cg.col(table, VAR)))
    assert var["Habitat 4"] == max(var.values()), \
        "that habitat must also be the most variable of the four"
    return (f"exactly one habitat has generalists at more than twice the specialists, and "
            f"it is the most variable: {doubled[0]}")


def q14(table, item):
    labs = cg.labels(table)
    spec = dict(zip(labs, cg.col(table, SPEC)))
    var = dict(zip(labs, cg.col(table, VAR)))
    fewest = min(spec, key=spec.get)
    assert fewest == "Habitat 4", f"Habitat 4 must hold the fewest specialists; got {fewest}"
    assert len(set(spec.values())) == len(spec), "'all four hold the same number' must be false"
    assert var[fewest] == max(var.values()), \
        "the habitat with the fewest specialists must be the most variable one"
    return (f"the specialist counts are {spec} and the smallest belongs to {fewest}, whose "
            f"variation index {var[fewest]:.0f} is the highest")


def q15(table, item):
    spec, gen = _by(table, CHANGES, SPECEND, GENEND)
    assert _falls(spec), f"specialists must fall as marked changes rise; got {spec}"
    assert _rises(gen), f"generalists must rise as marked changes rise; got {gen}"
    return (f"sorted by the number of marked changes the specialists read {spec} and the "
            f"generalists {gen}, one strictly falling and the other strictly rising")


def q16(table, item):
    spec = cg.col(table, SPECEND)
    drop = spec[0] - spec[-1]
    assert drop == 19, f"the specialist count must fall by 19; got {drop}"
    assert drop > 0, "'it rose' must be false"
    assert drop != spec[0] and drop != spec[-1], \
        "the change must not coincide with either endpoint"
    return (f"the specialist count runs {spec[0]:.0f} to {spec[-1]:.0f} across the four "
            f"periods, a fall of {drop:.0f}")


def q17(table, item):
    labs = cg.labels(table)
    dspec = dict(zip(labs, cg.col(table, DSPEC)))
    dgen = dict(zip(labs, cg.col(table, DGEN)))
    idx = dict(zip(labs, cg.col(table, IDX)))
    const = "Reserve held constant by management"
    flux = "Reserve left to fluctuate"
    assert idx[const] < idx[flux], \
        f"the managed reserve must be the more constant of the two; got {idx}"
    assert dspec[const] > 0 and dgen[const] < 0, \
        f"the constant reserve must gain specialists and lose generalists; got {dspec[const]}, {dgen[const]}"
    assert dspec[flux] < 0 and dgen[flux] > 0, \
        f"the fluctuating reserve must lose specialists and gain generalists; got {dspec[flux]}, {dgen[flux]}"
    return (f"the constant reserve changes by {dspec[const]:+.0f} specialists and "
            f"{dgen[const]:+.0f} generalists while the fluctuating one changes by "
            f"{dspec[flux]:+.0f} and {dgen[flux]:+.0f}")


def q18(table, item):
    labs = cg.labels(table)
    dspec = dict(zip(labs, cg.col(table, DSPEC)))
    losers = [lab for lab, v in dspec.items() if v < 0]
    assert losers == ["Reserve left to fluctuate"], \
        f"only the fluctuating reserve must lose specialists; got {losers}"
    return (f"the two specialist changes are {dspec}, and exactly one of them is negative")


def q19(table, item):
    (share,) = _by(table, MARKED, SHARE)
    assert _falls(share), f"the specialist share must fall as change becomes commoner; got {share}"
    assert share[-1] != max(share), \
        "'the most disturbed site has the largest share' must be false"
    assert len(set(share)) == len(share), "'the same share at all four sites' must be false"
    return (f"sorted by the number of marked changes the specialist shares read {share} "
            "percent, strictly decreasing")


def q20(table, item):
    labs = cg.labels(table)
    share = dict(zip(labs, cg.col(table, SHARE)))
    marked = dict(zip(labs, cg.col(table, MARKED)))
    top = max(share, key=share.get)
    assert top == "Site A", f"Site A must carry the largest specialist share; got {top}"
    assert marked[top] == min(marked.values()), \
        "the site with the largest specialist share must be the least disturbed one"
    return (f"the specialist shares are {share} percent, and the largest belongs to {top}, "
            f"which records {marked[top]:.0f} marked changes")


def q21(table, item):
    share = cg.col(table, SHARE)
    spread = max(share) - min(share)
    assert spread == 73, f"the fall must be 73 percentage points; got {spread}"
    assert spread != max(share) and spread != min(share), \
        "the difference must not coincide with either endpoint"
    return (f"the specialist share runs {max(share):.0f} percent to {min(share):.0f} "
            f"percent, a fall of {spread:.0f} points")


def q22(table, item):
    labs = cg.labels(table)
    wob = dict(zip(labs, cg.col(table, WOBBLE)))
    spec = dict(zip(labs, cg.col(table, SPEC)))
    gen = dict(zip(labs, cg.col(table, GEN)))
    before = "Before the river was regulated"
    after = "After the river was regulated"
    assert wob[after] < wob[before], \
        f"the water level must vary less after regulation; got {wob}"
    assert spec[after] > spec[before], \
        f"the specialists must rise as the level steadies; got {spec}"
    assert gen[after] < gen[before], \
        f"the generalists must fall as the level steadies; got {gen}"
    return (f"years of large variation fall {wob[before]:.0f} to {wob[after]:.0f} per decade "
            f"while specialists rise {spec[before]:.0f} to {spec[after]:.0f} and generalists "
            f"fall {gen[before]:.0f} to {gen[after]:.0f}")


def q23(table, item):
    labs = cg.labels(table)
    rows = list(zip(labs, cg.col(table, SPECC), cg.col(table, SPECX),
                    cg.col(table, GENC), cg.col(table, GENX)))
    for lab, sc, sx, gc, gx in rows:
        assert sc > sx, f"{lab}: the constant habitat must hold more specialists; got {sc} against {sx}"
        assert gx > gc, f"{lab}: the changing habitat must hold more generalists; got {gx} against {gc}"
    return (f"in all {len(rows)} pairs the constant habitat holds more specialists and the "
            "changing habitat more generalists")


def q24(table, item):
    labs = cg.labels(table)
    diff = {lab: c - x for lab, c, x in
            zip(labs, cg.col(table, SPECC), cg.col(table, SPECX))}
    top = max(diff, key=diff.get)
    assert top == "Pair 2", f"Pair 2 must show the largest specialist difference; got {top}"
    assert list(diff.values()).count(diff[top]) == 1, \
        "'the three differences are equal' must be false, and the largest must be unique"
    return (f"the specialist differences are {diff} species, and the largest, {diff[top]:.0f}, "
            f"belongs to {top}")


CLAIMS = [
 ("Specialist species",
  "ERT-3.A.1 states that specialist species tend to be advantaged in habitats that remain constant, which is the half of the comparison attached to constancy."),
 ("Generalist species",
  "ERT-3.A.1 states that generalist species tend to be advantaged in habitats that are changing, which is the half of the comparison attached to change."),
 # Both clauses, because the distractor is the SWAP.
 ("advantaged where habitats remain constant, and generalists where habitats are changing",
  "ERT-3.A.1 pairs specialists with habitats that remain constant and generalists with habitats that are changing. The rejected options exchange the two kinds, give one kind the advantage everywhere, or deny that constancy matters."),
 ("advantage is a tendency, so an individual case may run the other way",
  "ERT-3.A.1 is written twice with TEND TO BE, which asserts a prevailing pattern rather than a rule without exceptions."),
 ("uses both terms without defining either",
  "ERT-3.A.1 says which kind tends to be advantaged in which habitat and supplies no definition of either kind, and no other statement in the course supplies one. Each rejected option states a definition the framework does not give."),
 ("toward generalist species being the advantaged kind",
  "ERT-3.A.1 attaches the generalists' advantage to habitats that are changing, so a habitat becoming variable moves from the half of the comparison favouring specialists to the half favouring generalists."),
 # Both clauses, because two distractors keep one half and swap the other.
 ("Specialist species, because the habitat remains constant",
  "ERT-3.A.1 pairs the specialists' advantage with habitats that remain constant. The rejected options swap the kind, misdescribe the habitat, or deny the connection."),
 ("only that generalists tend to be the advantaged kind there",
  "ERT-3.A.1 speaks of which kind tends to be advantaged and says nothing about disappearance. It does address changing habitats, and it puts the generalists at the advantage in them."),
 ("favoured as a habitat stays constant or changes, while that statement is about the order of losses",
  "NAMED BOUNDARY: ERT-3.A.1 compares constant habitats with changing ones, while ERT-2.A.4 in the biodiversity unit gives the sequence in which the two kinds are lost as habitat is lost. The variable differs: constancy in one, extent in the other."),
 ("compares constant habitats with changing ones, while that statement concerns species introduced",
  "NAMED BOUNDARY: ERT-3.A.1 is a comparison between constant and changing habitats, while ERT-2.E.1 in the biodiversity unit concerns island species, the limited resources on most islands, and introduced generalists outcompeting specialists."),
 # Both clauses: the distractor swaps which column falls.
 ("the specialist count falls and the generalist count rises",
  "Recomputed in q11 above: sorted by year to year variation the specialist column strictly falls and the generalist column strictly rises. ERT-3.A.1 places the specialists' advantage in constant habitats and the generalists' in changing ones."),
 ("Habitat 1",
  "Recomputed in q12 above: the largest specialist margin is unique and belongs to the least variable habitat, which is where ERT-3.A.1 places the specialists' advantage."),
 ("Habitat 4 alone",
  "Recomputed in q13 above: exactly one habitat has generalists at more than twice the specialists, and it is the most variable of the four, which is where ERT-3.A.1 places the generalists' advantage."),
 ("Habitat 4",
  "Recomputed in q14 above: the smallest specialist count belongs to the most variable habitat. ERT-3.A.1 places the specialists' advantage in habitats that remain constant."),
 # Both clauses: the distractor swaps which kind rises.
 ("fewer specialists and more generalists",
  "Recomputed in q15 above: sorted by the number of marked changes the specialists strictly fall and the generalists strictly rise. ERT-3.A.1 places the generalists' advantage in habitats that are changing."),
 ("It fell by 19",
  "Recomputed in q16 above: 24 species less 5 is 19, and the direction is a fall. The rejected values reverse the direction or name an endpoint."),
 # Both clauses: the distractor swaps the two reserves.
 ("held constant gained specialists and lost generalists",
  "Recomputed in q17 above: the managed reserve is the more constant of the two, and it gains specialists and loses generalists while the fluctuating one does the reverse. ERT-3.A.1 makes exactly that pairing."),
 ("The reserve left to fluctuate",
  "Recomputed in q18 above: exactly one of the two specialist changes is negative, and it belongs to the reserve whose conditions changed. ERT-3.A.1 places the specialists' advantage in habitats that remain constant."),
 ("smaller at the sites where conditions changed more often",
  "Recomputed in q19 above: sorted by the number of marked changes the specialist shares are strictly decreasing. ERT-3.A.1 places the specialists' advantage in constant habitats."),
 ("Site A",
  "Recomputed in q20 above: the largest specialist share belongs to the site at which no marked change was recorded. ERT-3.A.1 pairs constancy with the specialists' advantage."),
 ("73 points",
  "Recomputed in q21 above: 82 percent less 9 percent is 73 points. The rejected values are the endpoints or differences between other pairs of sites."),
 # Both clauses: the distractor swaps which count rose.
 ("the specialist count rose and the generalist count fell",
  "Recomputed in q22 above: after regulation the water level varies in fewer years, the specialists rise and the generalists fall. ERT-3.A.1 places the specialists' advantage in habitats that remain constant."),
 # Both clauses: the distractor swaps the two habitats of each pair.
 ("holds more specialists and the changing habitat holds more generalists",
  "Recomputed in q23 above: in every one of the three pairs the constant habitat holds more specialists and the changing habitat holds more generalists. ERT-3.A.1 makes exactly that pairing, and the record repeats it three times."),
 ("Pair 2",
  "Recomputed in q24 above: the largest specialist difference between the two habitats of a pair is unique and belongs to the second pair."),
 ("comparing the two counts across that gradient",
  "ERT-3.A.1 is a comparison between constant and changing habitats, so a direct test needs both kinds of habitat and both kinds of species counted across them. A single site, a diet survey, an area measurement and an endemism count each leave out one half of the comparison."),
 ("Keeping the reserve's conditions as constant as possible",
  "ERT-3.A.1 states that specialist species tend to be advantaged in habitats that remain constant, so constancy is the condition the statement associates with the specialists' advantage. Area and introductions are not part of this statement."),
 ("advantage only where habitats are changing",
  "ERT-3.A.1 is a conditional comparison: generalists tend to be advantaged where habitats are changing and specialists where they remain constant, so an unqualified advantage everywhere is not what either half says."),
 ("generalist species there tend to be the advantaged kind",
  "ERT-3.A.1 attaches the generalists' advantage to habitats that are changing, and a climate becoming more variable is such a habitat. The statement offers no prediction of extinction and does not treat the two kinds alike."),
 ("Specialists increasing and generalists declining in a habitat that has become far",
  "ERT-3.A.1 expects the generalists to be the advantaged kind where a habitat is changing, so the observation running against the tendency is the opposite result in exactly that setting. Two rejected options match the statement rather than contradicting it, and two concern area, which the statement does not mention."),
 ("where habitats remain constant and generalists where habitats are changing, and the framework defines neither kind",
  "ERT-3.A.1 supplies the two halves of the comparison and the hedge, and supplies no definition of either kind. Each rejected summary exchanges the halves, hardens the tendency into an absolute, or adds a definition the framework does not give."),
]

TABLE_CHECKS = {11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16, 17: q17,
                18: q18, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23, 24: q24}

if "--selftest" in sys.argv:
    print("note: e_check.run negative-controls every gate on every run; "
          "--selftest is the same run, not a separate one.")

e_check.run(e3_1, CLAIMS, TABLE_CHECKS)
