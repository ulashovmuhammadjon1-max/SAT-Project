"""Key audit for AP ENVIRONMENTAL SCIENCE 4.1 Plate Tectonics.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student.

WHAT THE KEYS REST ON
---------------------
ERT-4.A.1  Convergent boundaries can result in the creation of mountains, island
           arcs, earthquakes, and volcanoes.
ERT-4.A.2  Divergent boundaries can result in seafloor spreading, rift valleys,
           volcanoes, and earthquakes.
ERT-4.A.3  Transform boundaries can result in earthquakes.
ERT-4.A.4  Maps that show the global distribution of plate boundaries can be used
           to determine the location of volcanoes, island arcs, earthquakes, hot
           spots, and faults.
ERT-4.A.5  An earthquake occurs when stress overcomes a locked fault, releasing
           stored energy.

    items 1, 4, 5, 6, 7, 14, 18, 19, 20, 22   ERT-4.A.1
    items 2, 4, 5, 6, 7, 15, 18, 19, 26       ERT-4.A.2
    items 3, 6, 7, 16, 20, 23, 24             ERT-4.A.3
    items 11, 12, 17, 30                      ERT-4.A.4
    items 8, 9, 10, 21, 28, 29                ERT-4.A.5
    items 13, 25                              the phrasing and the arithmetic

THE THREE LISTS OVERLAP AND THE OVERLAP IS THE CONTENT. Read side by side:
mountains and island arcs are convergent only; seafloor spreading and rift
valleys are divergent only; volcanoes are convergent and divergent but NOT
transform; earthquakes are all three; hot spots and faults are named only in
ERT-4.A.4 and attached to no boundary type at all. Items 4 to 7, 12, 18 and 19
each key one cell of that grid and nothing beyond it.

CONVERGENT AND DIVERGENT ARE THE SWAP THIS TOPIC INVITES, so items 1, 2, 4, 5,
14 and 15 each carry an anchor naming the WHOLE list, not one feature of it. An
anchor reading only "volcanoes and earthquakes" would match the divergent
distractor as well as the convergent key, which is the defect already found once
in verify_e2_1.py.

NOT KEYED, because the framework does not state it: what drives plate motion, how
fast plates move, subduction, the depth or magnitude of an earthquake, any named
plate or fault or range, and how a hot spot forms. Item 21's key marks that
absence rather than filling it.

DATA ITEMS: 22 to 30. Every keyed classification, maximum, difference and rate is
recomputed below from that table alone, and each check also falsifies the
distractors it can.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and EVERY data table in turn, and requires each
corruption to raise BEFORE the real gate runs. Items 28, 29 and 30 read an
agreement BETWEEN two columns, which reversing both columns preserves, so for
those e_check flattens the table next and each check fails on the uniqueness or
the inequality it also asserts -- a flat column has neither a unique maximum nor
a gap between itself and its neighbour. ``python3 verify_e4_1.py --selftest`` is
the same run; the controls are not behind the flag.
"""
import sys

import cg_check as cg
import e_check
import e4_1

MOTION = "Relative motion of the two plates"
MOUNTAINS = "Mountain ranges recorded along it"
VOLCANOES = "Volcanoes recorded along it"
QUAKES = "Earthquakes recorded in a ten year survey"
DISTANCE = "Distance from the ridge crest (kilometers)"
AGE = "Age of the seafloor rock (millions of years)"
LOCKED = "Years the segment stayed locked"
STRESS = "Stress stored on the segment (units)"
RELEASED = "Energy released when the segment moved (units)"
NEAR = "Number found within one hundred kilometers of a mapped plate boundary"
FAR = "Number found farther than one hundred kilometers from any mapped boundary"

TOWARD = "move toward each other"
APART = "move apart"
PAST = "slide past each other"


def _motions(table):
    return [str(r[1]) for r in table["rows"]]


def _row_with(table, predicate):
    """The indexes of the rows satisfying ``predicate(i)``."""
    return [i for i in range(len(table["rows"])) if predicate(i)]


def q22(table, item):
    mountains = cg.col(table, MOUNTAINS)
    volcanoes = cg.col(table, VOLCANOES)
    quakes = cg.col(table, QUAKES)
    motions = _motions(table)
    with_mountains = _row_with(table, lambda i: mountains[i] > 0)
    assert len(with_mountains) == 1, \
        f"exactly one boundary must record mountains; got rows {with_mountains}"
    i = with_mountains[0]
    assert TOWARD in motions[i], \
        f"the boundary recording mountains must be the converging one; got {motions[i]!r}"
    assert volcanoes[i] > 0 and quakes[i] > 0, \
        f"it must also record volcanoes and earthquakes; got {volcanoes[i]}, {quakes[i]}"
    return (f"the mountain counts are {mountains}, so exactly one boundary records "
            f"mountains, and its motion reads {motions[i]!r} with {volcanoes[i]:.0f} "
            f"volcanoes and {quakes[i]:.0f} earthquakes beside them")


def q23(table, item):
    mountains = cg.col(table, MOUNTAINS)
    volcanoes = cg.col(table, VOLCANOES)
    quakes = cg.col(table, QUAKES)
    motions = _motions(table)
    bare = _row_with(table, lambda i: mountains[i] == 0 and volcanoes[i] == 0)
    assert len(bare) == 1, \
        f"exactly one boundary must record neither mountains nor volcanoes; got {bare}"
    i = bare[0]
    assert PAST in motions[i], \
        f"that boundary must be the one sliding past; got {motions[i]!r}"
    assert quakes[i] > 0, f"it must still record earthquakes; got {quakes[i]}"
    return (f"with mountains {mountains} and volcanoes {volcanoes}, exactly one boundary "
            f"has neither, its motion reads {motions[i]!r}, and it still records "
            f"{quakes[i]:.0f} earthquakes")


def q24(table, item):
    quakes = cg.col(table, QUAKES)
    motions = _motions(table)
    i = max(range(len(quakes)), key=lambda k: quakes[k])
    assert quakes.count(quakes[i]) == 1, f"the largest count must be unique; got {quakes}"
    assert PAST in motions[i], \
        f"the most earthquakes must belong to the boundary sliding past; got {motions[i]!r}"
    assert min(quakes) > 0, f"every boundary must record earthquakes; got {quakes}"
    assert len(set(quakes)) == len(quakes), "'all three recorded the same number' must be false"
    return (f"the earthquake counts are {quakes}, all above zero and all different, and the "
            f"largest belongs to the boundary whose motion reads {motions[i]!r}")


def q25(table, item):
    quakes = cg.col(table, QUAKES)
    motions = _motions(table)
    past = [q for q, m in zip(quakes, motions) if PAST in m]
    apart = [q for q, m in zip(quakes, motions) if APART in m]
    assert len(past) == 1 and len(apart) == 1, \
        f"one sliding and one separating boundary must be tabulated; got {motions}"
    gap = past[0] - apart[0]
    assert gap == 270, f"the difference must be 270 earthquakes; got {gap}"
    assert gap != past[0] and gap != apart[0] and gap != past[0] + apart[0], \
        "the difference must not coincide with either count or with their sum"
    return (f"the sliding boundary records {past[0]:.0f} earthquakes and the separating one "
            f"{apart[0]:.0f}, a difference of {gap:.0f}")


def q26(table, item):
    distance = cg.col(table, DISTANCE)
    age = cg.col(table, AGE)
    pairs = sorted(zip(distance, age))
    ages = [a for _, a in pairs]
    assert all(ages[i + 1] > ages[i] for i in range(len(ages) - 1)), \
        f"the rock must be older the farther it lies from the crest; got {pairs}"
    assert ages[0] == min(ages), "the youngest rock must lie at the crest"
    assert len(set(ages)) == len(ages), "'the same age at every distance' must be false"
    return (f"ordered by distance from the crest the ages read {ages} million years, "
            "strictly increasing from the youngest rock at the crest")


def q27(table, item):
    pairs = sorted(zip(cg.col(table, DISTANCE), cg.col(table, AGE)))
    span_km = pairs[-1][0] - pairs[0][0]
    span_my = pairs[-1][1] - pairs[0][1]
    assert span_my != 0, f"the record must span a nonzero age; got {pairs}"
    rate = span_km / span_my
    assert rate == 20, f"the rate must be 20 kilometers per million years; got {rate}"
    steps = [(b[0] - a[0]) / (b[1] - a[1]) for a, b in zip(pairs, pairs[1:]) if b[1] != a[1]]
    assert steps and all(s == rate for s in steps), \
        f"every consecutive pair must give the same rate; got {steps}"
    assert rate != span_km and rate != span_my, \
        "the rate must not coincide with either span"
    return (f"the record spans {span_km:.0f} kilometers and {span_my:.0f} million years, a "
            f"rate of {rate:.0f} kilometers per million years, matched by every "
            f"consecutive pair: {steps}")


def q28(table, item):
    stress = cg.col(table, STRESS)
    released = cg.col(table, RELEASED)
    matches = [abs(s - r) < 1e-9 for s, r in zip(stress, released)]
    assert all(matches), \
        f"the energy released must equal the stress stored on every segment; " \
        f"got {stress} against {released}"
    assert len(set(stress)) == len(stress), \
        f"'the same energy on all three segments' must be false; got {stress}"
    assert min(released) > 0, f"every segment must release energy; got {released}"
    return (f"the stress stored reads {stress} and the energy released {released}, equal "
            "segment by segment and different from one segment to the next")


def q29(table, item):
    locked = cg.col(table, LOCKED)
    stress = cg.col(table, STRESS)
    most_stress = max(range(len(stress)), key=lambda i: stress[i])
    longest_locked = max(range(len(locked)), key=lambda i: locked[i])
    assert stress.count(stress[most_stress]) == 1, \
        f"the largest stored stress must be unique; got {stress}"
    assert locked.count(locked[longest_locked]) == 1, \
        f"the longest time locked must be unique; got {locked}"
    assert most_stress == longest_locked, (
        f"the segment storing most stress must be the one locked longest; stress {stress} "
        f"points at row {most_stress} and the years locked {locked} at row {longest_locked}"
    )
    return (f"the stress stored reads {stress} and the years locked {locked}, and the "
            f"unique maximum of each falls on the same segment, row {most_stress}")


def q30(table, item):
    labs = cg.labels(table)
    near = cg.col(table, NEAR)
    far = cg.col(table, FAR)
    for lab, n, f in zip(labs, near, far):
        assert n > f, f"{lab}: the count near a boundary must exceed the count away from one"
        assert n > 3 * f, f"{lab}: {n} must be several times {f}, not merely larger"
    concentrated = [lab for lab, n, f in zip(labs, near, far) if n > f]
    assert len(concentrated) == len(labs), \
        "'only the earthquake epicenters are concentrated near the boundaries' must be false"
    return (f"for all {len(labs)} kinds of feature the count near a boundary {near} exceeds "
            f"the count away from one {far} by more than three times over")


CLAIMS = [
 # The whole list, not one feature of it: the rejected option is ERT-4.A.2's list.
 ("creation of mountains, island arcs",
  "ERT-4.A.1, near verbatim: convergent boundaries can result in the creation of mountains, island arcs, earthquakes, and volcanoes. The rejected list of seafloor spreading and rift valleys is ERT-4.A.2's, belonging to divergent boundaries."),
 ("Seafloor spreading, rift valleys, volcanoes",
  "ERT-4.A.2, near verbatim: divergent boundaries can result in seafloor spreading, rift valleys, volcanoes, and earthquakes. The rejected list of mountains and island arcs is ERT-4.A.1's, belonging to convergent boundaries."),
 ("no other feature in that statement",
  "ERT-4.A.3 is a single clause: transform boundaries can result in earthquakes. Rift valleys and seafloor spreading belong to ERT-4.A.2 and island arcs to ERT-4.A.1, and no statement anywhere adds one of them to a transform boundary."),
 ("mountains and island arcs",
  "ERT-4.A.1 names mountains and island arcs and ERT-4.A.2 does not. Volcanoes and earthquakes appear in both lists, seafloor spreading and rift valleys in the divergent list alone, and hot spots only in ERT-4.A.4."),
 ("Seafloor spreading and rift valleys",
  "ERT-4.A.2 names seafloor spreading and rift valleys and ERT-4.A.1 does not. Mountains and island arcs appear in the convergent list alone, volcanoes and earthquakes in both, and faults only in ERT-4.A.4."),
 ("Volcanoes",
  "Volcanoes appear in ERT-4.A.1 and in ERT-4.A.2 but not in ERT-4.A.3, which names earthquakes alone for transform boundaries. Island arcs and mountains belong to the convergent list only and rift valleys and seafloor spreading to the divergent list only."),
 ("Earthquakes",
  "Earthquakes are named in ERT-4.A.1, in ERT-4.A.2 and in ERT-4.A.3, so they are the one feature common to all three boundary statements. Volcanoes fall short by one and each remaining feature appears in a single statement."),
 ("stress overcomes a locked fault",
  "ERT-4.A.5, near verbatim: an earthquake occurs when stress overcomes a locked fault, releasing stored energy. The fault is already locked when the stress overcomes it, so an option in which the locking follows the earthquake reverses the statement's own order."),
 ("Stored energy",
  "ERT-4.A.5 states that overcoming the locked fault releases stored energy. Weathered parent material belongs to the soil statement ERT-4.B.1 and new seafloor to ERT-4.A.2, and neither is what this statement releases."),
 ("A locked fault",
  "ERT-4.A.5 states that an earthquake occurs when stress overcomes a locked fault. The rejected options are features named elsewhere in the topic, none of which the statement places in the path of the stress."),
 ("volcanoes, island arcs, earthquakes, hot spots",
  "ERT-4.A.4 states that maps showing the global distribution of plate boundaries can be used to determine the location of volcanoes, island arcs, earthquakes, hot spots, and faults. The statement offers a LOCATION, and no date, depth, composition or rate."),
 ("Hot spots and faults",
  "ERT-4.A.1 to ERT-4.A.3 between them name mountains, island arcs, earthquakes, volcanoes, seafloor spreading and rift valleys. Hot spots and faults appear only in ERT-4.A.4's list of what a boundary record locates, with no boundary type attached to either."),
 ("possible results of that kind of boundary rather than ones present at every",
  "Each of ERT-4.A.1, ERT-4.A.2 and ERT-4.A.3 is written CAN RESULT IN, which commits the framework to the connection while stopping short of asserting that every boundary of that kind carries all of the features. Hardening it is stronger than the statement and denying it is weaker."),
 ("Convergent boundaries can result in the creation of mountains",
  "Plates moving toward one another meet at a convergent boundary, and ERT-4.A.1 names mountains, island arcs, earthquakes and volcanoes among what such a boundary can result in, which covers the mountains, volcanoes and earthquakes the case reports."),
 ("Divergent boundaries can result in seafloor spreading",
  "Crust being pulled apart is a divergent boundary, and ERT-4.A.2 names rift valleys, volcanoes and earthquakes among what such a boundary can result in. ERT-4.A.1's convergent list contains no rift valley."),
 ("Transform boundaries can result in earthquakes",
  "Plates sliding past one another meet at a transform boundary, and ERT-4.A.3 names earthquakes and nothing further for that kind, which matches a record of earthquakes with no volcanoes and no mountain building. Both other boundary statements include volcanoes."),
 ("convergent, divergent and transform boundaries alike",
  "Earthquakes appear in all three of ERT-4.A.1, ERT-4.A.2 and ERT-4.A.3, and ERT-4.A.4 puts earthquakes among the things the global distribution of plate boundaries can be used to locate. No statement confines them to one kind of boundary or places them away from boundaries."),
 ("island arcs",
  "ERT-4.A.2 names seafloor spreading, rift valleys, volcanoes and earthquakes for divergent boundaries. Island arcs appear in ERT-4.A.1, among what convergent boundaries can result in, and in no other statement."),
 ("Rift valleys",
  "ERT-4.A.1 names mountains, island arcs, earthquakes and volcanoes for convergent boundaries. Rift valleys appear in ERT-4.A.2, among what divergent boundaries can result in, and in no other statement."),
 ("names only earthquakes for transform boundaries",
  "ERT-4.A.3 is a single clause naming earthquakes, while ERT-4.A.1 and ERT-4.A.2 each name volcanoes. Sharing one feature with those two statements does not carry the remainder of their lists across to transform boundaries."),
 ("stress overcomes a locked fault and stored energy is released",
  "ERT-4.A.1 to ERT-4.A.3 say which features each kind of boundary can result in, and ERT-4.A.5 says what has to happen for one earthquake to occur. Neither the speed of the plates nor the depth of an earthquake is stated anywhere in the topic."),
 ("records mountains, volcanoes and earthquakes together",
  "Recomputed in q22 above: exactly one of the three surveyed boundaries records mountain ranges, it is the one along which the plates move toward each other, and it records volcanoes and earthquakes as well. ERT-4.A.1 names mountains, island arcs, earthquakes and volcanoes as what a convergent boundary can result in."),
 ("records earthquakes but no volcanoes and no mountains",
  "Recomputed in q23 above: exactly one boundary records neither mountains nor volcanoes, it is the one along which the plates slide past each other, and it still records earthquakes. ERT-4.A.3 names earthquakes and nothing further for a transform boundary."),
 ("slide past each other",
  "Recomputed in q24 above: the three earthquake counts are all different and all above zero, and the largest belongs to the boundary along which the plates slide past each other. ERT-4.A.1, ERT-4.A.2 and ERT-4.A.3 between them name earthquakes for every kind of boundary, which is why none of the three counts is zero."),
 ("270 more",
  "Recomputed in q25 above: 530 less 260 is 270, which coincides with neither count nor with their sum. The rejected values are the differences between other pairs of rows and that sum."),
 ("older the farther it lies from the ridge crest",
  "Recomputed in q26 above: ordered by distance from the crest the ages are strictly increasing and the youngest rock lies at the crest. ERT-4.A.2 names seafloor spreading among what a divergent boundary can result in, and seafloor forming at the crest and moving away is what that pattern of ages records."),
 ("About 20 kilometers per million years",
  "Recomputed in q27 above: 120 kilometers over 6 million years is 20 kilometers per million years, and every consecutive pair of points in the record gives the same figure. The rejected values are the two spans themselves and an intermediate age."),
 ("matched the stress that had been stored",
  "Recomputed in q28 above: on every segment the energy released equals the stress stored, and the three amounts differ from one another. ERT-4.A.5 states that an earthquake occurs when stress overcomes a locked fault, releasing stored energy."),
 ("stayed locked the longest",
  "Recomputed in q29 above: the largest stored stress and the longest time locked are each unique in their column and fall on the same segment. ERT-4.A.5 makes the stress building on a locked fault the thing that is eventually released."),
 ("far more common near a boundary than away from one",
  "Recomputed in q30 above: for each of the three kinds of feature the count within one hundred kilometers of a boundary exceeds the count beyond it by more than three times over, so no kind is the exception. ERT-4.A.4 states that the global distribution of plate boundaries can be used to determine the location of volcanoes, island arcs, earthquakes, hot spots, and faults."),
]

TABLE_CHECKS = {22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27, 28: q28,
                29: q29, 30: q30}

if "--selftest" in sys.argv:
    print("note: e_check.run negative-controls every gate on every run; "
          "--selftest is the same run, not a separate one.")

e_check.run(e4_1, CLAIMS, TABLE_CHECKS)
