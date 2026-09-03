"""Key audit for AP ENVIRONMENTAL SCIENCE 7.8 Noise Pollution.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
Items 1, 5, 12, 16, 20 and 29 rest on STB-2.J.1, that noise pollution is sound
at levels high enough to cause physiological stress and hearing loss.
Items 2, 11, 18 and 24 rest on STB-2.J.2, the urban sources: transportation,
construction, and domestic and industrial activity.
Items 3, 6, 7, 8, 9, 13, 15, 22 and 25 rest on STB-2.J.3, the effects on
animals in ecological systems: stress, masking of sounds used to communicate or
hunt, damaged hearing, and changes to migratory routes.
Items 4, 10, 14, 17, 19, 21, 23, 27 and 28 are reasoning items under suggested
skill 3.C, describe the author's use of evidence to support a claim; each key
turns on whether the cited evidence bears on the claim, together with whichever
statement above the claim concerns.
Item 26 rests on the unit's enduring understanding STB-2, that human activities
have consequences for the atmosphere, which is why this topic sits in the air
pollution unit. Item 30 joins all three statements.

WHAT IS NOT CLAIMED. The framework gives no sound level, no exposure limit, no
threshold in decibels, no named species and no named place, and no key states
one. Every decibel figure in the module belongs to the study in its own stem or
table and is recomputed below from that table.

DATA ITEMS: 4, 5, 6, 7, 8 and 9 carry tables and every keyed reading is
recomputed from the table alone, with the rejected readings falsified against
the same numbers.

NEGATIVE CONTROL: `python3 verify_e7_8.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e7_8

LEVEL = "Sound level measured at the sidewalk (decibels)"
HOURS = "Hours per day the activity was audible"
YEARS = "Years at the noisy work site"
SHIFT = "Average shift in hearing threshold (decibels)"
BG = "Background sound level (decibels)"
HORMONE = "Average stress hormone in the animals (nanograms per milliliter)"
BG_TRIAL = "Background sound level during the trial (decibels)"
REACH = "Distance at which a calling animal could still be heard by a listener (meters)"
VESSELS = "Shipping traffic through the corridor (vessels per week)"
SHARE = "Share of tracked animals using the corridor (percent)"
DETECT = "Prey rustles detected by the hunting animal per hour"
CAPTURE = "Successful captures per hour"


def q4(table, item):
    acts = cg.labels(table)
    level = dict(zip(acts, cg.col(table, LEVEL)))
    hours = dict(zip(acts, cg.col(table, HOURS)))
    loudest = max(level, key=level.get)
    longest = max(hours, key=hours.get)
    assert loudest != longest, f"the loudest and the longest are both {loudest}"
    assert len(set(level.values())) == len(level), "'all recorded at the same level' must be false"
    quietest = min(level, key=level.get)
    assert quietest != longest, "'the quietest was audible longest' must be false"
    return (f"the loudest activity is {loudest} at {level[loudest]:.0f} decibels while the "
            f"longest exposure is {longest} at {hours[longest]:.0f} hours, so the two rankings differ")


def q5(table, item):
    groups = cg.labels(table)
    years = dict(zip(groups, cg.col(table, YEARS)))
    shift = dict(zip(groups, cg.col(table, SHIFT)))
    comp = [g for g in groups if "Comparison" in g]
    exposed = [g for g in groups if g not in comp]
    assert len(comp) == 1, "one comparison group is required"
    c = comp[0]
    ordered = sorted(exposed, key=lambda g: years[g])
    assert all(shift[ordered[i]] < shift[ordered[i + 1]] for i in range(len(ordered) - 1)), \
        f"the shift does not grow with years at the site: {[shift[g] for g in ordered]}"
    assert years[c] == max(years.values()), \
        "the comparison group must have served as long as the longest exposed group"
    assert shift[c] < min(shift[g] for g in exposed), \
        f"the comparison group does not show the smallest shift: {shift}"
    return (f"the exposed groups shift {[shift[g] for g in ordered]} decibels with "
            f"{[years[g] for g in ordered]} years of exposure, while the comparison group at "
            f"{years[c]:.0f} years shifts only {shift[c]:.0f}")


def q6(table, item):
    pens = cg.labels(table)
    bg = cg.col(table, BG)
    horm = cg.col(table, HORMONE)
    pairs = sorted(zip(bg, horm))
    assert all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"the hormone does not rise with the sound level: {pairs}"
    assert horm[bg.index(max(bg))] == max(horm), "'the loudest has the lowest hormone' must be false"
    assert len(set(horm)) == len(horm), "'identical in all three' must be false"
    return (f"sorted by background level the hormone readings are {[h for _, h in pairs]}, "
            f"rising throughout, with the largest in {pens[bg.index(max(bg))]}")


def q7(table, item):
    bg = cg.col(table, BG_TRIAL)
    reach = cg.col(table, REACH)
    pairs = sorted(zip(bg, reach))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"the audible distance does not fall as the background rises: {pairs}"
    assert pairs[0][1] > 10 * pairs[-1][1], "the fall should be large across the range tested"
    assert len(set(reach)) == len(reach), "'the same distance in every trial' must be false"
    return (f"sorted by background level the audible distances are {[r for _, r in pairs]} meters, "
            "falling at every step and by more than a factor of ten across the range")


def q8(table, item):
    ships = cg.col(table, VESSELS)
    share = cg.col(table, SHARE)
    assert all(ships[i] < ships[i + 1] for i in range(len(ships) - 1)), \
        f"vessel traffic does not rise across the seasons: {ships}"
    assert all(share[i] > share[i + 1] for i in range(len(share) - 1)), \
        f"the share using the corridor does not fall across the seasons: {share}"
    return (f"vessel traffic runs {ships} per week, rising at every step, while the share using "
            f"the corridor runs {share} percent, falling at every step")


def q9(table, item):
    conds = cg.labels(table)
    det = dict(zip(conds, cg.col(table, DETECT)))
    cap = dict(zip(conds, cg.col(table, CAPTURE)))
    quiet = [c for c in conds if "Quiet" in c][0]
    noisy = [c for c in conds if c != quiet][0]
    assert det[noisy] < det[quiet], "detections must fall under the noise condition"
    assert cap[noisy] < cap[quiet], "captures must fall under the noise condition"
    return (f"detections fall from {det[quiet]:.0f} to {det[noisy]:.0f} per hour and captures from "
            f"{cap[quiet]:.0f} to {cap[noisy]:.0f} per hour when the noise is played")


CLAIMS = [
 ("high enough to cause physiological stress and hearing loss",
  "STB-2.J.1 verbatim: noise pollution is sound at levels high enough to cause physiological stress and hearing loss. The source of the sound, the hour of day, personal dislike and the distance travelled are not part of the definition the framework gives."),
 ("Transportation, construction, and domestic and industrial activity",
  "STB-2.J.2 verbatim: sources of noise pollution in urban areas include transportation, construction, and domestic and industrial activity. Weather, geological events, atmospheric chemistry and radon movement appear nowhere in that list."),
 ("masking of sounds used to communicate or hunt",
  "STB-2.J.3 near verbatim: some effects of noise pollution on animals in ecological systems include stress, the masking of sounds used to communicate or hunt, damaged hearing, and causing changes to migratory routes. Eggshell thinning belongs to STB-3.J.1, and the other options are attributed elsewhere or not at all."),
 ("both the level and the duration matter",
  "Recomputed in q4 above: the largest sound level and the longest daily exposure belong to different activities, and the quietest is not the longest. All four entries fall within the urban categories of STB-2.J.2, so none of them is outside the framework's list."),
 ("comparison group of the same length of service shows almost none",
  "Recomputed in q5 above: the shift grows with years at the noisy site while the equally long-serving comparison group shifts by less than any exposed group. Hearing loss is one of the two effects in STB-2.J.1, and the comparison is what separates exposure from length of service."),
 ("stress hormone rises as the background sound level rises",
  "Recomputed in q6 above: ordering the enclosures by background level puts the hormone readings in the same order, all distinct. Stress is the first effect STB-2.J.3 lists for animals in ecological systems, and a hormone concentration is a physiological measurement of it."),
 ("falls sharply as the background sound level rises",
  "Recomputed in q7 above: the audible distance falls at every step and by more than a factor of ten across the range. That is the masking of sounds used to communicate in STB-2.J.3; the table records audibility rather than whether the animal called."),
 ("falls as vessel traffic through it rises",
  "Recomputed in q8 above: vessel traffic rises at every step of the record while the share using the corridor falls at every step. STB-2.J.3 lists causing changes to migratory routes among the effects of noise pollution."),
 ("Both detections of prey and successful captures fell",
  "Recomputed in q9 above: both columns are smaller under the noise condition. STB-2.J.3 names the masking of sounds used to hunt, and a fall in detections alongside a fall in captures is exactly what masking would produce."),
 ("beside existing highways of the same design",
  "Suggested skill 3.C. The claim concerns sound reaching a residential district, so the evidence that bears on it is a sound measurement beside comparable roads in comparable districts. Vehicle registrations, cost, travel time and opinion measure nothing about the sound."),
 ("Traffic on a busy arterial road",
  "STB-2.J.2 lists transportation among the urban sources of noise pollution, and road traffic is transportation. The pile driver is construction, the stamping press is industrial activity, and the air conditioner and rooftop fan are domestic and building activity."),
 ("physiological stress that the definition uses",
  "STB-2.J.1 defines noise pollution as sound at levels high enough to cause physiological stress and hearing loss, so raised blood pressure and disturbed sleep are the stress half of the definition. Construction is one of the urban sources named in STB-2.J.2."),
 ("four separate effects from damaged hearing",
  "STB-2.J.3 lists four effects on animals, only one of which is damaged hearing, so an effect on a population does not require hearing loss. The framework sets no fixed level below which animals are unaffected and confines the effects to no one kind of species."),
 ("same on days when the factory is shut",
  "Suggested skill 3.C. If the measured sound is unchanged when the suspected source stops, that source is not accounting for it. Building size, appearance, employment and construction date bear on none of the measurements."),
 ("masking of sounds used to communicate",
  "Singing when the background is quieter concerns whether the sound can be heard, which is the masking effect named in STB-2.J.3. Corrosion and acidification belong to STB-2.I.2, radon illness to STB-2.F.2, and trapping to STB-2.C.2."),
 ("depending on how loud it is",
  "STB-2.J.1 defines noise pollution by the level reached and the harm it causes, while STB-2.J.2 separately lists the activities that produce such sound in cities. So the definition turns on level rather than on the identity of the activity, and the framework does name sources."),
 ("hour by hour, including at night",
  "Suggested skill 3.C. An average conceals when the sound occurs, and a claim about sleep concerns the night hours, so the hourly record is the measurement that could distinguish the two neighborhoods. Population, parks, building age and distance describe no sound."),
 ("appliances, equipment and gatherings in homes",
  "STB-2.J.2 lists domestic activity alongside transportation, construction and industrial activity, and domestic activity is the activity of households. Trains and helicopters are transportation, a jackhammer is construction, and a foundry is industrial."),
 ("as vessel traffic through that corridor changes",
  "Suggested skill 3.C with STB-2.J.3's changes to migratory routes. The claim pairs route use with the noise source, so the supporting evidence must pair them too; vessel size, company schedules, sightings and water depth leave that pairing unmade."),
 ("physiological stress as well as sound that causes hearing loss",
  "STB-2.J.1 names two harms, physiological stress and hearing loss, so sound reaching the level that causes stress falls within the definition without causing hearing loss. Audibility, hour of day and source are not part of it, and it does not require both harms at once."),
 ("before and after the barrier was built, with traffic volumes recorded",
  "Suggested skill 3.C. Testing the claim requires the sound in the affected houses on both sides of the change, with traffic recorded so a change in traffic is not mistaken for a change in shielding. Dimensions, house counts, cost and past complaints measure no sound."),
 ("information it would otherwise obtain from sounds",
  "STB-2.J.3 names the masking of sounds used to communicate or hunt, and masking is an effect on what can be heard, so what is lost is the information the sound carried. The framework attributes to noise no effect on vision, digestion, thermal tolerance or fat storage."),
 ("brief sample at one place and one hour cannot represent",
  "Suggested skill 3.C. A conclusion about a district across time requires samples that represent it, and one short reading at a single point does not. The instrument, the unit and the outdoor placement are not the flaw."),
 ("road rebuilding project, construction",
  "STB-2.J.2's categories are transportation, construction, and domestic and industrial activity. Rebuilding a road is construction work rather than transportation, a bus route is transportation, a factory compressor is industrial, and a stereo in a home is domestic."),
 ("measured one physiological sign of it",
  "STB-2.J.3 lists stress first among the effects on animals in ecological systems, and a stress hormone is a physiological measurement of stress. Damaged hearing and changed migratory routes are separate effects in the same list and are not measured by this study."),
 ("travels through the air and harms people and other organisms",
  "Enduring understanding STB-2 makes the unit about human activities having consequences for the atmosphere, and STB-2.J.1 to STB-2.J.3 place noise pollution there as sound produced by human activity that reaches people and animals. It is not a chemical, not a particulate, and not a temperature effect."),
 ("largest contributor to nighttime sound levels",
  "Suggested skill 3.C with STB-2.J.2, which names construction among the urban sources. The claim is that removing nighttime construction lowers the noise, so what supports it is evidence identifying construction as the dominant nighttime contributor; preferences, site counts, costs and opinions elsewhere do not."),
 ("adds masking of communication and hunting sounds",
  "STB-2.J.1 names physiological stress and hearing loss, and STB-2.J.3 separately lists stress, masking, damaged hearing and changes to migratory routes for animals in ecological systems. Both sets exist in the framework and they are not identical."),
 ("quietest sound each worker can detect",
  "STB-2.J.1 names physiological stress and hearing loss as two distinct harms, so distinguishing them requires a measure of hearing itself, which is the faintest detectable sound compared across the exposure. A hormone or a blood pressure measures the stress half, and a sound level or a survey measures neither."),
 ("Sound loud enough to cause physiological stress and hearing loss, produced in urban areas",
  "Each clause is one of the framework's three statements: the definition in STB-2.J.1, the urban sources in STB-2.J.2, and the effects on animals in STB-2.J.3. Every rejected summary contradicts at least one of them."),
]

TABLE_CHECKS = {4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9}

es.run(e7_8, CLAIMS, TABLE_CHECKS, sys.argv)
