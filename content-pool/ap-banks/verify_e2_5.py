"""Key audit for AP ENVIRONMENTAL SCIENCE 2.5 Natural Disruptions to Ecosystems.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
ERT-2.G.1  natural disruptions may, for a given occurrence, be as great as or
           greater than many human-made ones   -- items 1, 2, 12, 13, 26, 27, 30
ERT-2.G.2  Earth system processes run on a range of time scales, and can be
           periodic, episodic, or random       -- items 3, 4, 5, 18, 19, 20, 28, 30
ERT-2.G.3  Earth's climate has changed over geological time for many reasons
                                               -- items 6, 7, 16, 17, 30
ERT-2.G.4  sea level has varied significantly as a result of changes in the
           amount of glacial ice                -- items 8, 14, 15, 29, 30
ERT-2.G.5  major environmental change or upheaval commonly results in large
           swathes of habitat changes           -- items 9, 21, 22, 30
ERT-2.G.6  wildlife engages in both short- and long-term migration for a
           variety of reasons, including natural disruptions
                                               -- items 10, 11, 23, 24, 25, 30

THE HEDGES ARE WHAT SEVERAL ITEMS TURN ON. ERT-2.G.1 says MAY, says MANY
human-made disruptions rather than all, and makes the comparison FOR A GIVEN
OCCURRENCE rather than in total. ERT-2.G.3 says FOR MANY REASONS and names
none. ERT-2.G.5 says COMMONLY. ERT-2.G.6 says A VARIETY OF REASONS, INCLUDING
natural disruptions. Items 2, 7, 11 and 30 key exactly those hedges and no key
anywhere strengthens one.

WHAT IS DELIBERATELY NOT ASKED. Periodic, episodic and random are named and
none is defined, so no item asks a student to tell an episodic process from a
random one -- the framework supplies no way to draw that line. Item 18 asks
which tabulated process recurs at a CONSTANT interval, which is arithmetic on
the table plus the ordinary meaning of the word periodic, and the claim says
so. ERT-2.G.3 names no cause of past climate change, so no key names one;
ERT-2.G.4 names exactly one cause of sea level change and no key adds a second.

DATA ITEMS: 12 to 25 carry tables. Every keyed conclusion is recomputed below
from that table alone, read by column header rather than by index.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and EVERY data table in turn, and requires each
corruption to raise BEFORE the real gate runs. Several of these checks measure
a spread or a difference and so survive a column reversal, which reverses a
spread onto itself; e_check then flattens the table and every one of them fails
because a flat column has no spread at all. ``python3 verify_e2_5.py
--selftest`` is the same run; the controls are not behind the flag.
"""
import sys

import cg_check as cg
import e_check
import e2_5

DESTROYED = "Hectares of forest destroyed"
ICE = "Glacial ice on Earth (millions of cubic kilometres)"
SEA = "Sea level relative to today (metres)"
TEMP = "Average global surface temperature (degrees Celsius)"
GAP1 = "Years between the first and second occurrence"
GAP2 = "Years between the second and third occurrence"
GAP3 = "Years between the third and fourth occurrence"
DURATION = "Typical time over which one occurrence plays out (years)"
BEFORE = "Area before the eruption (hectares)"
AFTER = "Area two years after the eruption (hectares)"
KM = "Distance moved one way (kilometres)"
MONTHS = "Months spent away from the breeding area"
RAIN = "Rainfall in the season (millimetres)"
BIRDS = "Waterbirds counted on the wetland"


def _falls(vals):
    return all(vals[i + 1] < vals[i] for i in range(len(vals) - 1))


def _by(table, key_header, *headers):
    keys = cg.col(table, key_header)
    order = sorted(range(len(table["rows"])), key=lambda i: keys[i])
    return [[cg.col(table, h)[i] for i in order] for h in headers]


def q12(table, item):
    pairs = dict(zip(cg.labels(table), cg.col(table, DESTROYED)))
    natural = {k: v for k, v in pairs.items() if "a natural event" in k}
    human = {k: v for k, v in pairs.items() if "a human made activity" in k}
    assert len(natural) == 2 and len(human) == 2, \
        f"two events of each kind must be tabulated; got {len(natural)} and {len(human)}"
    assert max(natural.values()) > max(human.values()), \
        f"a natural event must exceed every human made one; got {natural} against {human}"
    assert sum(natural.values()) > max(human.values()), \
        "'the two natural events together destroyed less than the logging' must be false"
    assert len(set(pairs.values())) == len(pairs), "'all four destroyed the same' must be false"
    return (f"the natural events destroyed {sorted(natural.values(), reverse=True)} hectares "
            f"against {sorted(human.values(), reverse=True)} for the human made activities")


def q13(table, item):
    pairs = dict(zip(cg.labels(table), cg.col(table, DESTROYED)))
    erupt = [v for k, v in pairs.items() if "volcanic eruption" in k][0]
    log = [v for k, v in pairs.items() if "logging operation" in k][0]
    ratio = erupt / log
    assert abs(ratio - 4) < 0.05, f"the ratio must be about four; got {ratio}"
    assert abs(ratio - 2) > 0.5 and abs(ratio - 10) > 0.5, \
        "'twice' and 'ten times' must both be false"
    return (f"the eruption destroyed {erupt:.0f} hectares and the logging operation "
            f"{log:.0f}, a ratio of {ratio:.2f}")


def q14(table, item):
    (sea,) = _by(table, ICE, SEA)
    assert _falls(sea), f"sea level must fall as glacial ice grows; got {sea}"
    assert len(set(sea)) == len(sea), "'sea level was the same in all four' must be false"
    ice = cg.col(table, ICE)
    assert len(set(ice)) == len(ice), "'glacial ice was the same in all four' must be false"
    return (f"sorted by glacial ice the sea level readings run {sea} metres relative to "
            "today, strictly decreasing as the ice grows")


def q15(table, item):
    sea = cg.col(table, SEA)
    spread = max(sea) - min(sea)
    assert spread == 125, f"the spread must be 125 metres; got {spread}"
    assert spread != abs(min(sea)), "the spread must not coincide with the lowest reading"
    return (f"the readings run from {max(sea):.0f} to {min(sea):.0f} metres relative to "
            f"today, a spread of {spread:.0f}")


def q16(table, item):
    t = cg.col(table, TEMP)
    assert len(set(t)) > 1, f"the intervals must not all be equal; got {t}"
    assert t != sorted(t), "'rose steadily throughout' must be false"
    assert t != sorted(t, reverse=True), "'fell steadily throughout' must be false"
    return f"the five reconstructed averages read {t} degrees Celsius, neither equal nor in order"


def q17(table, item):
    t = cg.col(table, TEMP)
    spread = max(t) - min(t)
    assert spread == 11, f"the spread must be 11 degrees; got {spread}"
    assert spread != max(t), "the spread must not coincide with the warmest reading"
    return (f"the warmest interval averages {max(t):.0f} and the coolest {min(t):.0f} "
            f"degrees Celsius, a difference of {spread:.0f}")


def _gaps(table):
    labs = cg.labels(table)
    cols = [cg.col(table, GAP1), cg.col(table, GAP2), cg.col(table, GAP3)]
    return {lab: [c[i] for c in cols] for i, lab in enumerate(labs)}


def q18(table, item):
    g = _gaps(table)
    constant = [lab for lab, vals in g.items() if len(set(vals)) == 1]
    assert constant == ["Process 1"], \
        f"exactly Process 1 must have equal gaps; got {constant}"
    return (f"exactly one row records the same gap three times over, {g['Process 1']} years, "
            "while every other row records gaps that differ")


def q19(table, item):
    g = _gaps(table)
    longest = {lab: max(vals) for lab, vals in g.items()}
    top = max(longest, key=longest.get)
    assert top == "Process 4", f"the longest single gap must belong to Process 4; got {top}"
    assert list(longest.values()).count(longest[top]) == 1, \
        "'two processes share the longest gap' must be false"
    return (f"the longest gap anywhere in the record is {longest[top]:.0f} years and it "
            f"belongs to {top}, whose other gaps are {sorted(g[top])[:2]}")


def q20(table, item):
    d = cg.col(table, DURATION)
    assert min(d) > 0, "every duration must be positive"
    assert max(d) / min(d) >= 1e6, \
        f"the longest must exceed the shortest by a factor of a million; got {max(d) / min(d)}"
    assert len(set(d)) == len(d), "'all about the same length' must be false"
    assert min(d) <= 1, "'all longer than a million years' must be false"
    return (f"the four durations read {d} years, the longest exceeding the shortest by a "
            f"factor of {max(d) / min(d):.0f}")


def q21(table, item):
    before = cg.col(table, BEFORE)
    after = cg.col(table, AFTER)
    assert sum(before) == sum(after), \
        f"the valley's total area must be unchanged; got {sum(before)} then {sum(after)}"
    moved = sum(abs(a - b) for a, b in zip(before, after)) / 2
    share = moved / sum(before)
    assert share > 0.5, f"most of the valley must have changed habitat type; got {share}"
    assert any(a < b for a, b in zip(before, after)), "'every type increased' must be false"
    return (f"{moved:.0f} of the valley's {sum(before):.0f} hectares are under a different "
            f"habitat type after the eruption, a share of {share:.2f}")


def q22(table, item):
    labs = cg.labels(table)
    loss = {lab: b - a for lab, b, a in
            zip(labs, cg.col(table, BEFORE), cg.col(table, AFTER))}
    worst = max(loss, key=loss.get)
    assert worst == "Mature forest", f"mature forest must lose the most; got {worst}"
    assert list(loss.values()).count(loss[worst]) == 1, "the largest loss must be unique"
    assert loss[worst] > 0, "'no habitat type lost area' must be false"
    return (f"the changes by row are {loss} hectares, and the largest loss, "
            f"{loss[worst]:.0f}, belongs to {worst}")


def q23(table, item):
    km = cg.col(table, KM)
    mo = cg.col(table, MONTHS)
    assert min(km) <= 20, f"one migration must be short; got a minimum of {min(km)}"
    assert max(km) >= 5000, f"one migration must be long; got a maximum of {max(km)}"
    assert min(mo) == 1 and max(mo) == 7, f"the absences must run 1 to 7 months; got {mo}"
    assert len(set(km)) == len(km), "'every species moved about the same distance' must be false"
    return (f"the distances read {km} kilometres and the absences {mo} months, spanning "
            "short movements and long ones")


def q24(table, item):
    labs = cg.labels(table)
    mo = dict(zip(labs, cg.col(table, MONTHS)))
    longest = max(mo, key=mo.get)
    assert longest == "Species 3", f"Species 3 must be away longest; got {longest}"
    assert list(mo.values()).count(mo[longest]) == 1, \
        "'two species share the longest absence' must be false"
    return (f"the absences recorded are {sorted(mo.values())} months and the longest, "
            f"{mo[longest]:.0f}, belongs to {longest}")


def q25(table, item):
    rain = cg.col(table, RAIN)
    birds = cg.col(table, BIRDS)
    assert rain[1] < 0.3 * rain[0], f"rainfall must collapse in the drought year; got {rain}"
    assert birds[1] < 0.2 * birds[0], f"the bird count must collapse with it; got {birds}"
    assert rain[2] > 0.8 * rain[0], "rainfall must recover after the drought"
    assert birds[2] > 0.8 * birds[0], "most of the birds must be counted there again"
    return (f"rainfall runs {rain} millimetres and the bird count {birds}, both collapsing "
            "and both recovering over the same three seasons")


CLAIMS = [
 ("as great as, or greater than, many human-made",
  "ERT-2.G.1, near verbatim: natural disruptions to ecosystems have environmental consequences that may, for a given occurrence, be as great as, or greater than, many human-made disruptions."),
 ("single events are being compared",
  "ERT-2.G.1 compares occurrences rather than totals, says may rather than does, and says many human-made disruptions rather than all. Every rejected option strengthens one of those three hedges."),
 ("a range of scales in terms of time",
  "ERT-2.G.2, near verbatim: Earth system processes operate on a range of scales in terms of time, so no single scale covers them all."),
 ("Periodic, episodic or random",
  "ERT-2.G.2 states that processes can be periodic, episodic, or random. Each rejected set replaces at least one of those three words."),
 ("Reversible",
  "ERT-2.G.2 gives three descriptions: periodic, episodic, and random. Reversible is not among them."),
 ("changed over geological time for many reasons",
  "ERT-2.G.3, near verbatim: Earth's climate has changed over geological time for many reasons. It asserts the change, places it in geological time, and puts more than one reason behind it."),
 ("more than one cause and names none of them here",
  "ERT-2.G.3 says MANY REASONS, which is more than one, and the statement lists no reason of its own, so both a single-cause and a no-cause answer go beyond it."),
 ("amount of glacial ice on Earth",
  "ERT-2.G.4 states that sea level has varied significantly as a result of changes in the amount of glacial ice on Earth over geological time. That is the one cause the statement supplies."),
 ("Large swathes of habitat changes",
  "ERT-2.G.5, near verbatim: major environmental change or upheaval commonly results in large swathes of habitat changes. The claim is about habitat over a large area, not extinction or recovery."),
 ("both short-term and long-term migration",
  "ERT-2.G.6 states that wildlife engages in both short- and long-term migration for a variety of reasons, including natural disruptions. Both durations are named and natural disruption is one reason among several."),
 ("variety of reasons and includes natural disruptions among them",
  "ERT-2.G.6 says a variety of reasons INCLUDING natural disruptions, which places natural disruption inside a larger set rather than alone in it, and does not remove it from the set either."),
 ("single natural event destroyed more forest",
  "Recomputed in q12 above: the largest natural event exceeds both human made activities, and the two natural events together exceed the logging operation. ERT-2.G.1 states that a natural disruption's consequences may, for a given occurrence, be as great as or greater than many human-made ones."),
 ("four times as much",
  "Recomputed in q13 above: 60,000 hectares over 15,000 is 4. The comparison is arithmetic on two entries in one column."),
 ("lower in the intervals when more glacial ice",
  "Recomputed in q14 above: sorted by glacial ice the sea level readings are strictly decreasing. ERT-2.G.4 attributes sea level variation to changes in the amount of glacial ice on Earth."),
 ("125 metres",
  "Recomputed in q15 above: 5 metres above today to 120 metres below is a spread of 125. ERT-2.G.4 calls the variation significant, and this is its size in the record."),
 ("differed from one interval to another",
  "Recomputed in q16 above: the five reconstructed averages are neither all equal nor in order. ERT-2.G.3 states that Earth's climate has changed over geological time."),
 ("Eleven degrees Celsius",
  "Recomputed in q17 above: 22 degrees Celsius less 11 is 11. The difference is arithmetic on the two extreme entries of one column."),
 ("Process 1",
  "Recomputed in q18 above: exactly one row records the same gap three times over. ERT-2.G.2 lists periodic among the descriptions a process can take, and a constant interval is what the ordinary meaning of that word describes; the framework defines none of the three, so nothing here asks a student to tell episodic from random."),
 ("Process 4",
  "Recomputed in q19 above: the longest single gap in the whole record is 55 years and it belongs to one row alone. The comparison is a search of every entry in the three gap columns."),
 ("span a range of scales, from about a year",
  "Recomputed in q20 above: the longest duration exceeds the shortest by a factor of two million. ERT-2.G.2 states that Earth system processes operate on a range of scales in terms of time."),
 ("Most of the valley's area changed from one habitat type",
  "Recomputed in q21 above: the valley's total area is unchanged and more than half of it lies under a different habitat type after the eruption. ERT-2.G.5 states that major upheaval commonly results in large swathes of habitat changes."),
 ("Mature forest",
  "Recomputed in q22 above: mature forest falls by 8,600 hectares, the largest loss in the table and a unique one. The comparison is a subtraction carried out on every row."),
 ("short movements lasting a month to long ones lasting most of a year",
  "Recomputed in q23 above: the distances run 15 to 6,000 kilometres and the absences 1 to 7 months. ERT-2.G.6 states that wildlife engages in both short- and long-term migration."),
 ("Species 3",
  "Recomputed in q24 above: the longest absence is 7 months and it belongs to one species alone. The comparison is a direct reading of one column."),
 ("left the wetland as the rainfall collapsed and most were counted",
  "Recomputed in q25 above: rainfall and the bird count collapse together and recover together over the same three seasons. ERT-2.G.6 states that wildlife migrates for a variety of reasons including natural disruptions, and a drought is such a disruption."),
 ("area of habitat altered by the single storm",
  "ERT-2.G.1 compares the environmental consequences of a given natural occurrence with those of human-made disruptions, so the test is a like-for-like measurement of altered area. A storm count, a repair bill, a species list and a wind speed each measure something else."),
 ("hurricane crossing a stretch of coastal forest",
  "ERT-2.G.1 sets natural disruptions beside human-made ones, and a hurricane is an event of the Earth system rather than an act of construction. Every rejected option is something people built or planted."),
 ("periodic, episodic or random",
  "ERT-2.G.2 makes two assertions in one statement: processes operate on a range of scales in terms of time, and processes can be periodic, episodic, or random. Each rejected statement collapses the range to one scale or the three descriptions to one."),
 ("attributes that variation to changes in the amount of glacial ice",
  "ERT-2.G.4 asserts both that sea level has varied significantly and that changes in the amount of glacial ice are the cause, so denying the variation, denying the cause, or substituting another cause all depart from it."),
 ("natural disruption among them",
  "The keyed sentence carries ERT-2.G.1's hedged comparison, ERT-2.G.2's range of time scales and three descriptions, ERT-2.G.3's many reasons, ERT-2.G.4's glacial ice, ERT-2.G.5's large swathes of habitat change, and ERT-2.G.6's two durations and several reasons. Each rejected summary hardens a hedge, denies a statement, or swaps a cause."),
]

TABLE_CHECKS = {12: q12, 13: q13, 14: q14, 15: q15, 16: q16, 17: q17, 18: q18,
                19: q19, 20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25}

if "--selftest" in sys.argv:
    print("note: e_check.run negative-controls every gate on every run; "
          "--selftest is the same run, not a separate one.")

e_check.run(e2_5, CLAIMS, TABLE_CHECKS)
