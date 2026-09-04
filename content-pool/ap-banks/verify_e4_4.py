"""Key audit for AP ENVIRONMENTAL SCIENCE 4.4 Earth's Atmosphere.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student.

WHAT THE KEYS REST ON
---------------------
ERT-4.D.1  The atmosphere is made up of major gases, each with its own relative
           abundance.
                   -- items 1, 2, 10, 13, 15, 17, 30
ERT-4.D.2  The layers of the atmosphere are based on temperature gradients and
           include the troposphere, stratosphere, mesosphere, thermosphere, and
           exosphere.
                   -- items 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 16, 23, 27, 30

THE TOPIC IS TWO SENTENCES, AND WHAT THEY WITHHOLD GOVERNS THE MODULE. They name
no gas and give no abundance; they give no altitude for any layer; they say
nothing about which layer lies lowest; and they give no DIRECTION for the
temperature change in any layer. Items 18, 19, 20, 21, 22, 24, 25, 26, 28 and 29
are therefore readings of a tabulated record, and each of their claims below says
so explicitly: the framework licenses the question -- relative abundance is a
share, the layers rest on temperature gradients -- and the table settles the
answer. No key in this module states a gas, an abundance, an altitude or a
direction as an assertion of the framework.

TWO ITEMS TURN ON A SWAP and their anchors carry BOTH clauses: item 14, whose
rejected option exchanges this topic's subject with topic 4.5's, and item 15,
whose rejected option gives relative abundance to the layers and the temperature
gradient to the gases. An anchor naming one half would match the swap as well as
the key -- the defect already found once in verify_e2_1.py.

THE COMPOSITION FIGURES ARE STIMULUS, NOT DOCTRINE. They are the ordinary
measured shares of dry air and they add to one hundred percent, which q19
recomputes. If a reader disputes a figure, nothing keyed here depends on the
framework having asserted it.

DATA ITEMS: 17 to 29. Every keyed maximum, sum, ratio, thickness, difference and
direction is recomputed below from that table alone.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and EVERY data table in turn, and requires each
corruption to raise BEFORE the real gate runs. Three checks here read a quantity
a column reversal preserves -- a sum is invariant under reordering, an alternation
of signs stays an alternation, and four contiguous bands stay contiguous when
their altitudes are reordered together -- so for those e_check flattens the table
next, and each fails on the assertion it also makes: that the shares add to one
hundred rather than to four, that no layer's temperature change is zero, and that
every layer's lower altitude is strictly below its upper one.
``python3 verify_e4_4.py --selftest`` is the same run; the controls are not
behind the flag.
"""
import sys

import cg_check as cg
import e_check
import e4_4

SHARE = "Share of dry air by volume (percent)"
BEGINS = "Altitude at which it begins (kilometers above the surface)"
ENDS = "Altitude at which it ends (kilometers above the surface)"
LOWER_T = "Temperature at its lower edge (degrees Celsius)"
UPPER_T = "Temperature at its upper edge (degrees Celsius)"

FRAMEWORK_LAYERS = ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere",
                    "Exosphere"]


def _unique_max(values):
    i = max(range(len(values)), key=lambda k: values[k])
    assert values.count(values[i]) == 1, f"the maximum must be unique; got {values}"
    return i


def _unique_min(values):
    i = min(range(len(values)), key=lambda k: values[k])
    assert values.count(values[i]) == 1, f"the minimum must be unique; got {values}"
    return i


def _changes(table):
    """Temperature change across each layer, upper edge less lower edge."""
    return [u - l for l, u in zip(cg.col(table, LOWER_T), cg.col(table, UPPER_T))]


def q17(table, item):
    share = cg.col(table, SHARE)
    assert len(set(share)) == len(share), f"the four shares must differ; got {share}"
    assert min(share) > 0, f"every gas must be present; got {share}"
    return (f"the four shares read {share} percent of dry air by volume, all different and "
            "all above zero")


def q18(table, item):
    labs = cg.labels(table)
    share = cg.col(table, SHARE)
    i = _unique_max(share)
    assert labs[i] == "Nitrogen", f"the largest share must belong to nitrogen; got {labs[i]}"
    return (f"the shares are {dict(zip(labs, share))} percent and the largest is unique and "
            f"belongs to {labs[i]}")


def q19(table, item):
    share = cg.col(table, SHARE)
    total = sum(share)
    assert abs(total - 100) < 0.01, f"the four shares must add to about 100; got {total}"
    assert total <= 100.01, "'they add to more than one hundred percent' must be false"
    assert total > 60, "'about half' and 'about a tenth' must be false"
    return (f"the four shares {share} add to {total:.2f} percent, which is one hundred to "
            "within a hundredth of a point")


def q20(table, item):
    nitrogen = cg.cell(table, "Nitrogen", SHARE)
    oxygen = cg.cell(table, "Oxygen", SHARE)
    ratio = nitrogen / oxygen
    assert 3 < ratio < 5, f"the ratio must be about four; got {ratio}"
    for wrong in (20, 78, 1):
        assert abs(ratio - wrong) > 1, f"a ratio of about {wrong} must be false"
    assert ratio > 1, "'less nitrogen than oxygen' must be false"
    return (f"nitrogen stands at {nitrogen} percent against oxygen's {oxygen}, a ratio of "
            f"{ratio:.2f}, nearest to four among the values offered")


def q21(table, item):
    labs = cg.labels(table)
    change = _changes(table)
    falling = [lab for lab, c in zip(labs, change) if c < 0]
    assert falling == ["Troposphere", "Mesosphere"], \
        f"the temperature must fall in exactly the troposphere and the mesosphere; " \
        f"got {falling} from changes {dict(zip(labs, change))}"
    assert len(falling) < len(labs), "'in all four of the layers' must be false"
    return (f"the change across each layer reads {dict(zip(labs, change))} degrees, "
            f"negative in exactly {len(falling)} of the {len(labs)}: {falling}")


def q22(table, item):
    labs = cg.labels(table)
    change = _changes(table)
    rising = [lab for lab, c in zip(labs, change) if c > 0]
    falling = [lab for lab, c in zip(labs, change) if c < 0]
    assert rising == ["Stratosphere", "Thermosphere"], \
        f"the temperature must rise in exactly the stratosphere and the thermosphere; " \
        f"got {rising}"
    assert not set(rising) & set(falling), "no layer may both rise and fall"
    return (f"the change across each layer reads {dict(zip(labs, change))} degrees, "
            f"positive in exactly {rising} and negative in {falling}")


def q23(table, item):
    labs = cg.labels(table)
    change = _changes(table)
    assert all(c != 0 for c in change), \
        f"no layer's temperature may be unchanged across it; got {change}"
    reversals = [change[i] * change[i + 1] < 0 for i in range(len(change) - 1)]
    assert all(reversals), (
        f"the sign of the change must reverse at every boundary; got {change} giving "
        f"{reversals}"
    )
    assert len(reversals) > 1, "'it reverses at one boundary only' must be false"
    return (f"the changes across the layers read {dict(zip(labs, change))} degrees, none "
            f"of them zero, and the sign is opposite in all {len(reversals)} neighbouring "
            "pairs")


def q24(table, item):
    labs = cg.labels(table)
    begins = cg.col(table, BEGINS)
    i = _unique_min(begins)
    assert labs[i] == "Troposphere", \
        f"the lowest layer must be the troposphere; got {labs[i]}"
    assert begins[i] == 0, f"the lowest layer must begin at the surface; got {begins[i]}"
    return (f"the layers begin at {dict(zip(labs, begins))} kilometers, and the unique "
            f"lowest is {labs[i]}, at the surface itself")


def q25(table, item):
    labs = cg.labels(table)
    thickness = [e - b for b, e in zip(cg.col(table, BEGINS), cg.col(table, ENDS))]
    i = _unique_max(thickness)
    assert labs[i] == "Thermosphere", \
        f"the thickest layer must be the thermosphere; got {labs[i]}"
    assert len(set(thickness)) == len(thickness), \
        "'the four layers are of equal thickness' must be false"
    return (f"the thicknesses are {dict(zip(labs, thickness))} kilometers, all different, "
            f"and the largest belongs to {labs[i]}")


def q26(table, item):
    labs = cg.labels(table)
    begins = cg.col(table, BEGINS)
    ends = cg.col(table, ENDS)
    for lab, b, e in zip(labs, begins, ends):
        assert b < e, f"{lab}: its lower altitude {b} must be strictly below its upper {e}"
    order = sorted(range(len(begins)), key=lambda i: begins[i])
    for a, b in zip(order, order[1:]):
        assert ends[a] == begins[b], (
            f"{labs[b]} must begin exactly where {labs[a]} ends; {begins[b]} against "
            f"{ends[a]}"
        )
    return (f"the layers run {[(labs[i], begins[i], ends[i]) for i in order]}, each with a "
            "nonzero thickness and each beginning exactly where the one below it ends, so "
            "there is neither a gap nor an overlap")


def q27(table, item):
    labs = cg.labels(table)
    begins = cg.col(table, BEGINS)
    missing = [name for name in FRAMEWORK_LAYERS if name not in labs]
    assert missing == ["Exosphere"], \
        f"exactly the exosphere must be absent from the record; got {missing}"
    assert all(name in FRAMEWORK_LAYERS for name in labs), \
        f"every tabulated layer must be one the framework names; got {labs}"
    assert begins == sorted(begins), \
        f"the record must run upward in altitude, so the omitted layer is the topmost; " \
        f"got {dict(zip(labs, begins))}"
    return (f"the record carries {len(labs)} of the framework's {len(FRAMEWORK_LAYERS)} "
            f"layers, in ascending order of altitude {begins}, and the one absent is "
            f"{missing[0]}")


def q28(table, item):
    labs = cg.labels(table)
    lower = cg.cell(table, "Troposphere", LOWER_T)
    upper = cg.cell(table, "Troposphere", UPPER_T)
    span = abs(upper - lower)
    assert span == 70, f"the troposphere must span 70 degrees; got {span}"
    assert span != abs(lower) and span != abs(upper), \
        "the span must not coincide with either edge temperature"
    others = [abs(c) for lab, c in zip(labs, _changes(table)) if lab != "Troposphere"]
    assert span not in others, f"another layer must not share that span; got {others}"
    return (f"the troposphere runs from {lower:.0f} to {upper:.0f} degrees Celsius, a span "
            f"of {span:.0f} degrees, matched by no other layer in the record")


def q29(table, item):
    labs = cg.labels(table)
    spans = [abs(c) for c in _changes(table)]
    i = _unique_max(spans)
    assert labs[i] == "Thermosphere", \
        f"the largest temperature change must belong to the thermosphere; got {labs[i]}"
    assert len(set(spans)) == len(spans), \
        "'the change is the same across all four' must be false"
    return (f"the temperature spans are {dict(zip(labs, spans))} degrees, all different, "
            f"and the largest belongs to {labs[i]}")


CLAIMS = [
 ("each with its own relative abundance",
  "ERT-4.D.1, near verbatim: the atmosphere is made up of major gases, each with its own relative abundance. The statement names more than one gas and gives every one of them a share of its own."),
 ("each with its own share of the whole",
  "ERT-4.D.1 gives each major gas its OWN relative abundance, which makes the abundance a share belonging to that gas rather than a quantity divided equally among them. The statement neither equalises the shares nor ties them to temperature."),
 ("Temperature gradients",
  "ERT-4.D.2 states that the layers of the atmosphere are based on temperature gradients and offers no other basis for them. Relative abundance is what ERT-4.D.1 attaches to the gases, not to the layers."),
 ("thermosphere, and exosphere",
  "ERT-4.D.2 names the troposphere, stratosphere, mesosphere, thermosphere, and exosphere. Two rejected options drop one or two of the five, one replaces the last with the hydrosphere, and one leaves the atmosphere altogether."),
 ("Five",
  "ERT-4.D.2 names the troposphere, stratosphere, mesosphere, thermosphere, and exosphere, which is five names in a single list."),
 ("The hydrosphere",
  "ERT-4.D.2 names the troposphere, stratosphere, mesosphere, thermosphere, and exosphere. The hydrosphere is not among them and is not a layer of the atmosphere at all."),
 ("without its asserting that the atmosphere can be divided in no other way",
  "ERT-4.D.2 gives the five names after the word INCLUDE, which commits the framework to those five while making no claim about arrangements it does not discuss. The same statement also gives the basis of the layers, so an option denying that is false as well."),
 ("layers of the atmosphere are based on temperature gradients",
  "ERT-4.D.2 states that the layers of the atmosphere are based on temperature gradients, which is what makes one layer distinguishable from the next. The rejected statements belong to ERT-4.D.1, ERT-4.E.1, ERT-4.B.2 and ERT-4.F.1."),
 ("while relative abundance is what the framework attaches to the gases",
  "ERT-4.D.2 bases the layers on temperature gradients and ERT-4.D.1 attaches relative abundance to the major gases. The student has taken a property the framework gives to one thing and applied it to the other."),
 ("Which gas is the most abundant",
  "ERT-4.D.1 supplies the four rejected options in its own words. It names no gas and gives no abundance, so which gas is the most abundant is not something the statement settles."),
 ("altitude at which each layer begins and ends",
  "ERT-4.D.2 supplies the basis of the layers and the five names, and no altitude for any of them. Where an altitude is needed it has to come from a measurement rather than from the statement."),
 ("a change in the gradient is what marks one layer from the next",
  "ERT-4.D.2 states that the layers of the atmosphere are based on temperature gradients, so a record of how temperature changes with altitude is a record of the very thing the layers rest on. The composition statement concerns the gases rather than the temperature."),
 ("share of a sample of air that the gas makes up",
  "ERT-4.D.1 gives each major gas its own relative abundance, which is a share of the whole, so measuring that share is what establishes it. A temperature or an altitude bears on ERT-4.D.2 and the layers instead."),
 # Both clauses, in order: the rejected option exchanges this topic's subject
 # with topic 4.5's, so an anchor naming one clause matches both.
 ("what the atmosphere is made of and how its layers are defined, while that statement says what causes the winds",
  "ERT-4.D.1 and ERT-4.D.2 give the composition of the atmosphere and the basis of its layers. ERT-4.E.1, in the next topic, states that global wind patterns primarily result from the most intense solar radiation arriving at the equator. One describes the thing and the other explains a motion within it."),
 # Both clauses: the rejected option gives each term to the other subject.
 ("Relative abundance is about the gases, and a temperature gradient is about the layers",
  "ERT-4.D.1 attaches relative abundance to the major gases and ERT-4.D.2 bases the layers on temperature gradients, so each term belongs to one statement and not to the other."),
 ("temperature gradients and that five of them are named",
  "ERT-4.D.2 supplies both halves at once: the layers are based on temperature gradients, and the troposphere, stratosphere, mesosphere, thermosphere and exosphere are named. Each rejected option replaces the basis or the count."),
 ("differing shares, each with a share of its own",
  "Recomputed in q17 above: the four measured shares are all different and all above zero. ERT-4.D.1 states that the atmosphere is made up of major gases, each with its own relative abundance, which is what a set of unequal nonzero shares is."),
 ("Nitrogen",
  "Recomputed in q18 above: the largest share in the record is unique. ERT-4.D.1 gives each major gas its own relative abundance without naming a gas or saying which share is largest, so the answer is settled by the tabulated measurements and not by the framework."),
 ("add to about one hundred percent",
  "Recomputed in q19 above: 78.08, 20.95, 0.93 and 0.04 add to 100.00 percent, so the four account for very nearly all of dry air and for no more than all of it. ERT-4.D.1 describes the gases as having relative abundances, which are shares of one whole."),
 ("About 4 times as much",
  "Recomputed in q20 above: 78.08 divided by 20.95 is about 3.7, which is nearest to four and more than a point away from every other value offered. The rejected values are the two shares themselves read as a ratio, or a comparison the numbers contradict."),
 ("In the troposphere and in the mesosphere",
  "Recomputed in q21 above: the temperature at the upper edge is below the temperature at the lower edge in exactly two of the four layers. ERT-4.D.2 states that the layers are based on temperature gradients and gives no direction for any layer, so the direction is read from the record."),
 ("In the stratosphere and in the thermosphere",
  "Recomputed in q22 above: the temperature at the upper edge is above that at the lower edge in exactly two of the four layers, and they are not the two in which it falls. The framework supplies no direction, so the record does."),
 ("reverses at every boundary",
  "Recomputed in q23 above: no layer's temperature change is zero and the sign of the change is opposite in every neighbouring pair. ERT-4.D.2 states that the layers of the atmosphere are based on temperature gradients, and a reversal of the gradient is what the record shows at each boundary."),
 ("The troposphere",
  "Recomputed in q24 above: exactly one of the tabulated layers begins at the surface and the rest begin above it. ERT-4.D.2 names the layers without saying which lies lowest, so the ordering comes from the altitudes in the record."),
 ("The thermosphere",
  "Recomputed in q25 above: the four thicknesses are 12, 38, 35 and 515 kilometers, all different, and the largest is unique. ERT-4.D.2 gives no altitude for any layer, so the comparison is settled by the record."),
 ("begins at exactly the altitude at which the layer below it ends",
  "Recomputed in q26 above: every layer has a nonzero thickness and each begins at exactly the altitude at which the one below it ends, so the four are continuous with neither a gap nor an overlap. The framework gives no altitudes, so the arrangement is read from the record."),
 ("The exosphere",
  "Recomputed in q27 above: every tabulated layer is one the framework names, the record runs upward in altitude, and exactly one of the framework's five names is absent from it. ERT-4.D.2 names five layers and the record carries four."),
 ("By 70 degrees",
  "Recomputed in q28 above: the troposphere runs from 15 degrees Celsius to minus 55, a span of 70 degrees, which coincides with neither edge temperature and is matched by no other layer. The rejected values are the edge temperatures themselves and a span the record does not support."),
 ("The thermosphere",
  "Recomputed in q29 above: the temperature spans across the four layers are 70, 55, 90 and 790 degrees, all different, and the largest is unique. ERT-4.D.2 bases the layers on temperature gradients and gives no size for any of them, so the comparison is settled by the record."),
 ("relative abundance, and its layers are based on temperature gradients and include the troposphere, stratosphere",
  "ERT-4.D.1 supplies the major gases and their individual relative abundances and ERT-4.D.2 supplies the temperature gradients and the five names. Each rejected summary reduces the gases to one, equalises their abundances, replaces the basis of the layers, or shortens the list of names."),
]

TABLE_CHECKS = {17: q17, 18: q18, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23,
                24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29}

if "--selftest" in sys.argv:
    print("note: e_check.run negative-controls every gate on every run; "
          "--selftest is the same run, not a separate one.")

e_check.run(e4_4, CLAIMS, TABLE_CHECKS)
