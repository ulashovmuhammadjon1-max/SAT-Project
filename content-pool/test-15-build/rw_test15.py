#!/usr/bin/env python3
"""
Reading & Writing authored for Test 15.

All 81 items are original. The transcribed pool was spent by Test 8, and for
R&W authoring is in any case the safer route: a transcribed answer key has to
be re-derived by hand before it can be trusted (Test 5 shipped 6 wrong answers
in 81 that way). Every item below carries a `why` that records the reasoning
which produced the key AND the reason the strongest distractor fails - that
record IS the verification, so no key exists here without one.

Rationales name options by their CONTENT, never by letter, so balance_rw.py is
free to rotate every question when it evens out the key distribution.

Writing-domain choices are never bare punctuation. Test 8 shipped Boundaries
items whose four options were ", " / "; " / ": " / " and ", which a student
sees as four empty rows. The real test repeats the words on either side of the
blank inside every option so each choice reads as the resulting sentence, and
every Boundaries item here is written that way from the start. Form/Structure
items whose options are genuinely words ("was" / "were", "has" / "have") stay
as words, which is also how the real test presents them.

Topics were checked programmatically against rw_test8.py, rw_test9.py,
rw_test10.py, rw_test11.py and rw_test12.py - roughly four hundred passages -
and nothing is reused. Candidates that collided with an existing passage
(amber, coral bleaching, beaver dams, hydrothermal tubeworms, aerogel,
kintsugi, fresco, Domesday, portolan charts, Timbuktu, Linear B, Lalibela's
masons, island-dwarfed elephants, wind turbines, lunar eclipses) were dropped
before drafting. What is left: cuttlefish colour matching, bombardier beetles,
hagfish slime, sandgrouse belly feathers, the theremin, Doggerland, Exchequer
tally sticks, Ndebele wall painting, Nicaraguan Sign Language, Prince Rupert's
drops, bog butter, wycinanki, the Great Trigonometrical Survey, organ stops,
the etcher's ground, firefly synchrony, the cavity magnetron, optical tweezers,
the Boston ice trade, the zoetrope, bar-headed geese, Clark's nutcracker,
railway standard time, Byzantine tesserae, Argo floats, Guna molas, kerb cuts,
Ophiocordyceps, the Iceman's copper axe, gecko setae, the Wollemi pine, the
Sogdian letters, snow algae, ranked-choice ballots, Scott's phonautograph,
platypus electroreception, zeolites, the Holmdel hiss, barnacle cement, the
equation of time, congestion charging, antlion pits, Roebling's wire rope,
Rafflesia, the Bessemer converter, netsuke, ferrofluids, suminagashi,
cassowary casques, capoeira, the Oseberg ship, the Erie Canal, bike-share
rebalancing, Anna Atkins's cyanotypes, lubok prints, clockwork tin toys,
winter ice roads, volcano seismographs, a gasholder frame, dawn-chorus
recording, paired rain gauges, a bell foundry, chalk streams, electronic
paper, maglev, colour-film stock, food deserts, the Flynn effect,
regenerative braking, bharatanatyam mudras, loanword phonology, the blue LED,
rural electrification, Arnhem Land bark painting, Tuvan khoomei, the camera
lucida, Norse place-names, school start times, Darwin's bark spider, the
Athenian kleroterion and the Pony Express.

Block counts (fixed by the assembler's quota, 3 modules x 27):
    Words in Context 15, Text Structure and Purpose 6,
    Central Ideas and Details 6, Command of Evidence 9, Inferences 6,
    Boundaries 12, Form, Structure, and Sense 9, Transitions 9,
    Rhetorical Synthesis 9                                        = 81
"""

SOURCE = "AUTHORED-T15"
MODULE = "RW"


def wic(num, passage, choices, answer, why):
    return dict(num=num, skill="Words in Context", passage=passage,
                stem="Which choice completes the text with the most logical and precise word or phrase?",
                choices=choices, answer=answer, why=why)


def meaning(num, passage, word, choices, answer, why):
    """Underlined-word-meaning variant of a Words in Context item."""
    return dict(num=num, skill="Words in Context", passage=passage,
                stem=f"As used in the text, what does the word &ldquo;{word}&rdquo; most nearly mean?",
                choices=choices, answer=answer, why=why)


def tsp(num, passage, stem, choices, answer, why):
    return dict(num=num, skill="Text Structure and Purpose", passage=passage,
                stem=stem, choices=choices, answer=answer, why=why)


def cid(num, passage, stem, choices, answer, why):
    return dict(num=num, skill="Central Ideas and Details", passage=passage,
                stem=stem, choices=choices, answer=answer, why=why)


def coe(num, passage, stem, choices, answer, why):
    return dict(num=num, skill="Command of Evidence", passage=passage,
                stem=stem, choices=choices, answer=answer, why=why)


def inf(num, passage, choices, answer, why):
    return dict(num=num, skill="Inferences", passage=passage,
                stem="Which choice most logically completes the text?",
                choices=choices, answer=answer, why=why)


def bnd(num, passage, choices, answer, why):
    return dict(num=num, skill="Boundaries", passage=passage,
                stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
                choices=choices, answer=answer, why=why)


def fss(num, passage, choices, answer, why):
    return dict(num=num, skill="Form, Structure, and Sense", passage=passage,
                stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
                choices=choices, answer=answer, why=why)


def trn(num, passage, choices, answer, why):
    return dict(num=num, skill="Transitions", passage=passage,
                stem="Which choice completes the text with the most logical transition?",
                choices=choices, answer=answer, why=why)


def syn(num, notes, goal, choices, answer, why):
    bullets = "".join(f"<li>{n}</li>" for n in notes)
    return dict(
        num=num, skill="Rhetorical Synthesis",
        passage=f"While researching a topic, a student has taken the following notes:<ul>{bullets}</ul>",
        stem=f"The student wants to {goal} Which choice most effectively uses relevant "
             "information from the notes to accomplish this goal?",
        choices=choices, answer=answer, why=why)


QUESTIONS = [

 # ------------------------------------------------------ Words in Context (15)
 wic("W1",
     "A cuttlefish changes the colour and the pattern of its skin in under a second, matching "
     "gravel, weed or sand as it passes over each of them. Its eyes, however, contain a single "
     "kind of visual pigment, so by every test that has been applied the animal is colour blind. "
     "How it matches a colour it cannot see remains _____, and no explanation yet offered has won "
     "general agreement.",
     ["unresolved", "exaggerated", "undisputed", "trivial"], "A",
     "The closing clause says no explanation has won agreement, so the blank names a question "
     "still open. The 'undisputed' option asserts the opposite of the very clause that follows "
     "the blank."),

 wic("W2",
     "The bombardier beetle stores hydrogen peroxide in one chamber and hydroquinone in another "
     "and keeps the two apart until something threatens it. Mixed over a catalyst in a third "
     "chamber, they react and are fired out at the temperature of boiling water. Keeping the "
     "ingredients _____ until the instant of use is what lets the animal carry a weapon that would "
     "otherwise destroy the body holding it.",
     ["diluted", "segregated", "chilled", "concentrated"], "B",
     "The passage describes two substances held in separate chambers and combined only at the "
     "moment of firing, so the blank names their being kept apart. The 'diluted' option describes "
     "weakening the chemicals, which the passage never mentions and which would undercut a spray "
     "delivered at boiling point."),

 wic("W3",
     "A hagfish seized by a shark releases a thimbleful of protein and coiled fibre into the "
     "water, and within a fraction of a second the material has become litres of gel that clogs "
     "the attacker's gills. Nothing is manufactured at the moment of need. The threads are stored "
     "ready-made in glands along the animal's flank and are simply _____ by contact with seawater.",
     ["hardened", "unfurled", "consumed", "concealed"], "B",
     "Something stored coiled and occupying litres a moment later has been let out to its full "
     "length rather than made afresh, which is what the sentence contrasts with manufacture. The "
     "'hardened' option contradicts the passage, which describes the product as a gel that clogs "
     "gills."),

 wic("W4",
     "A male sandgrouse may nest fifty kilometres from the nearest water. Each morning he flies to "
     "a waterhole, wades in and rocks his body until the specialised feathers of his belly are "
     "soaked; the barbs of those feathers coil when dry and uncoil in water, gripping it against "
     "the pull of the air on the flight home. The plumage works here less as covering than as "
     "_____.",
     ["insulation", "camouflage", "a container", "ballast"], "C",
     "The feathers are described as taking up water and holding it for fifty kilometres, which is "
     "the work of a vessel. The 'insulation' option names a use for feathers in general but not "
     "the one the passage sets out, which concerns water rather than heat."),

 wic("W5",
     "A theremin is played without being touched. Two antennas radiate weak radio fields, and the "
     "performer's hands, moving in the air beside them, alter pitch and volume by changing the "
     "capacitance of the circuit. Because nothing in the empty air marks where one note ends and "
     "the next begins, the instrument offers a player no _____, and every pitch has to be found by "
     "ear alone.",
     ["landmarks", "amplification", "resonance", "notation"], "A",
     "The sentence explains that nothing marks the boundary between notes, so the missing word "
     "names the fixed reference points a fretted or keyed instrument supplies. The 'notation' "
     "option concerns whether music is written down, which has no bearing on locating a pitch in "
     "open air."),

 wic("W6",
     "Trawlers working the southern North Sea bring up peat, freshwater shells and worked flint "
     "along with the fish. The ground beneath them was dry until about eight thousand years ago, "
     "when rising seas closed over a plain that had joined Britain to the continent. What the nets "
     "recover is therefore not rubbish washed out from the shore but a landscape _____ where its "
     "people left it.",
     ["scattered", "submerged", "imagined", "quarried"], "B",
     "The passage says the sea rose over a plain and that the material sits where its inhabitants "
     "left it, so the word has to mean covered by water in place. The 'scattered' option "
     "contradicts the phrase 'where its people left it', which insists that nothing was moved."),

 wic("W7",
     "The English Exchequer recorded a debt by notching a hazel stick across its width and then "
     "splitting it lengthwise, so that creditor and debtor each kept a half. The grain of any "
     "given stick runs in a way no other stick repeats, so the two halves fit each other and "
     "nothing else. Since a forged half would fail the simplest test there is, the system was "
     "remarkably _____.",
     ["portable", "expensive", "tamper-resistant", "modern"], "C",
     "The split grain means a substituted half cannot be made to match, which is a defence against "
     "forgery and is what the final sentence is summing up. The 'portable' option is true of a "
     "stick but has nothing to do with the matching test the passage describes."),

 wic("W8",
     "Ndebele women paint the outer walls of their houses in blocks of saturated colour bounded by "
     "black lines, working freehand with a chicken feather and no drawn guide. A wall is repainted "
     "after each rainy season, and a painter will alter the design rather than copy the last one "
     "exactly. The practice the wall records is therefore continuous without being _____.",
     ["communal", "fixed", "decorative", "visible"], "B",
     "Repainting every year with deliberate alteration means the tradition persists while no "
     "single design does, so the blank names the quality the practice lacks. The 'communal' option "
     "fails because the passage never suggests the work is solitary; what it denies is that a "
     "design is repeated unchanged."),

 wic("W9",
     "Deaf children brought together at a school in Managua in the late 1970s had no language in "
     "common: each arrived with gestures invented at home. Within a few years the older pupils "
     "were signing fluently to one another, and the youngest, who learned from them, produced a "
     "grammar more regular than anything the first cohort had used. The language was not taught to "
     "them; it _____ among them.",
     ["survived", "declined", "spread", "emerged"], "D",
     "The passage insists the children began with no shared language and ended with a regular "
     "grammar nobody supplied, so the word must name something coming into existence. The 'spread' "
     "option presupposes a language that already existed somewhere else, which the first sentence "
     "rules out."),

 wic("W10",
     "Molten glass dropped into cold water freezes from the outside in. The skin sets first and the "
     "interior contracts as it cools afterwards, leaving the surface squeezed and the core pulled "
     "taut. Such a drop will take a hammer blow on its head, yet snipping its thin tail releases "
     "the stored strain and the whole thing bursts to powder. Strength and fragility here are not "
     "opposites but _____ of one arrangement.",
     ["substitutes", "consequences", "measurements", "exceptions"], "B",
     "Both the resistance to the hammer and the collapse at the tail are traced to the same "
     "sequence of cooling, so the word names what follows from that arrangement. The 'substitutes' "
     "option would say one property stands in for the other, which is not the relation the passage "
     "describes."),

 wic("W11",
     "Wooden vessels packed with a waxy fat are turned up in Irish and Scottish peat bogs, some of "
     "them three thousand years old and some still edible. Peat is cold, acid and nearly free of "
     "oxygen, which halts the bacteria that would otherwise spoil the contents. Burial in ground of "
     "that kind was therefore not disposal but _____.",
     ["storage", "concealment", "ceremony", "waste"], "A",
     "The passage explains that the bog's chemistry stops spoilage and that the contents remain "
     "edible, so the burial keeps the fat rather than getting rid of it. The 'concealment' option "
     "would explain hiding the vessels but not why the chemistry of the peat is the fact the "
     "passage supplies."),

 wic("W12",
     "A wycinanki maker folds a sheet of paper once and cuts through both halves in a single "
     "stroke, so the finished cockerel or spruce is identical on either side of the fold. The tool "
     "is a pair of sheep shears, held in one hand and worked against paper turned by the other. "
     "The symmetry of the result is neither drawn nor measured; it is _____ by the method itself.",
     ["hidden", "imitated", "guaranteed", "sacrificed"], "C",
     "Cutting both halves at once means the two sides cannot come out unlike each other, so the "
     "method makes the symmetry certain rather than approximating it. The 'imitated' option "
     "implies one side is copied from the other, and the passage says both are produced in the "
     "same stroke."),

 wic("W13",
     "The trigonometrical survey of India began with a baseline measured on the plain south of "
     "Madras with steel chains laid end to end. Every later distance in the chain of triangles was "
     "computed from that one line rather than paced out, so an error in it would have propagated "
     "through the entire network. The accuracy of everything downstream was _____ on a single "
     "measurement, which is why the baseline was remeasured again and again.",
     ["irrelevant", "contingent", "improved", "reported"], "B",
     "The passage says every later distance was computed from the baseline and that an error there "
     "would run through the whole network, so the downstream accuracy depends on it. The "
     "'improved' option would say the network made the baseline better, reversing the direction of "
     "the relation the passage sets out."),

 meaning("W14",
     "An organ is not one instrument but many. Each rank of pipes has a timbre of its own, and the "
     "player admits wind to a rank by drawing the knob that governs it; drawing several at once "
     "blends their voices into a single sound. A large instrument may offer sixty such "
     "<u>stops</u>, and no two organs are laid out alike.",
     "stops",
     ["Periods during which an activity is suspended.",
      "Places where a vehicle halts to take on passengers.",
      "Sets of pipes of one timbre, together with the controls that bring them into play.",
      "Obstructions placed inside a pipe to block the flow of air."],
     "C",
     "The passage defines the term as it uses it: ranks of pipes with distinct timbres, admitted by "
     "knobs the player draws. The obstruction sense inverts the passage, since drawing one of these "
     "lets wind into the pipes rather than blocking it."),

 meaning("W15",
     "Before an etcher touches the copper, the plate is covered with a thin acid-resistant coating "
     "of wax and resin and smoked black so that the lines will show. The needle takes this coating "
     "away wherever it passes, and when the plate goes into the bath the acid bites only where the "
     "<u>ground</u> has been cleared.",
     "ground",
     ["Solid earth at the surface of the land.",
      "A protective coating laid on a plate before it is etched.",
      "A reason offered in support of a claim.",
      "The background against which a figure is seen."],
     "B",
     "The passage names the layer directly - wax and resin, removed by the needle and resisted by "
     "the acid - so the word refers to that coating. The background sense is a real term in "
     "painting, but here the word denotes something scratched through, not an area lying behind a "
     "figure."),

 # --------------------------------------------- Text Structure and Purpose (6)
 tsp("S1",
     "Along some rivers in Thailand whole bankside trees of fireflies flash in unison, and the "
     "rhythm holds for hours. <u>Each insect shifts its own cycle a little earlier or later "
     "whenever it sees a neighbour flash, and a population of insects doing only that settles into "
     "a common beat with none of them leading.</u> Searches for a conductor among the flashing "
     "beetles have all failed, because there is nothing of the kind to find.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It supplies the mechanism that accounts for the coordination described, and that the final sentence depends on.",
      "It questions whether the flashing is genuinely synchronised.",
      "It describes the habitat in which the fireflies gather.",
      "It reports the outcome of a search for a leading insect."],
     "A",
     "The sentence shows how a shared rhythm can arise from purely local adjustment, which is "
     "exactly why looking for a conductor was bound to fail. Reporting the failed search is the "
     "business of the closing sentence, not of the underlined one."),

 tsp("S2",
     "An early airborne radar set needed a transmitter small enough to fly and powerful enough to "
     "return an echo from a submarine's conning tower. The valves then available could deliver one "
     "of those or the other. In 1940 two physicists at Birmingham cut a ring of resonant cavities "
     "into a solid copper block, sent an electron stream spinning through it, and produced a device "
     "the size of a fist that put out more power at short wavelengths than anything in service. "
     "Airborne sets followed within two years.",
     "Which choice best states the main purpose of the text?",
     ["To describe a design requirement that existing equipment could not meet and the compact device that met it.",
      "To argue that British radar was superior to the radar of other combatants.",
      "To trace the history of the vacuum valve from its invention onward.",
      "To explain how the timing of an echo is used to measure the range of a target."],
     "A",
     "The text states the two-sided requirement, notes that no existing valve satisfied both halves "
     "of it, and then describes the copper block that did. How an echo yields a distance is assumed "
     "throughout and never explained."),

 tsp("S3",
     "A glass bead a micron across cannot be picked up with anything solid. <u>Light carries "
     "momentum, and a bead sitting near the waist of a tightly focused beam bends the rays passing "
     "through it, which pushes the bead back towards the brightest point whenever it drifts "
     "away.</u> Biologists use the effect to hold a single bacterium still, or to take one end of a "
     "strand of DNA and measure the force needed to stretch it.",
     "Which choice best describes the function of the underlined sentence?",
     ["It states the physical principle that makes the applications in the final sentence possible.",
      "It lists the organisms that can be held by the technique.",
      "It concedes a limitation of tightly focused beams.",
      "It explains why glass is chosen for the bead rather than another material."],
     "A",
     "The sentence supplies the restoring push a focused beam exerts on a transparent particle, "
     "which is what allows a bacterium to be held or a strand pulled. Why the bead is glass in "
     "particular is a question the text never takes up."),

 tsp("S4",
     "In 1806 Frederic Tudor shipped 130 tons of pond ice from Boston to Martinique and lost most "
     "of the cargo and all of his money. The trouble was not the voyage but the storage at the far "
     "end. Over the next two decades he built insulated icehouses in the ports he sold to, packed "
     "the cargo in sawdust from the mills of Maine, and gave chilled drinks away until a taste for "
     "them existed. By 1850 ice was among the largest exports leaving Massachusetts.",
     "Which choice best states the main purpose of the text?",
     ["To describe how a failed venture was made viable by changes in storage and in demand.",
      "To explain the physics by which sawdust insulates a block of ice.",
      "To argue that the ice trade was more profitable than the timber trade.",
      "To recount the history of imports into Martinique in the nineteenth century."],
     "A",
     "The text opens with the loss, identifies storage as its cause, lists what Tudor then changed, "
     "and closes with the result. Sawdust occupies one clause as an item on that list, and no "
     "physics of insulation is offered anywhere."),

 tsp("S5",
     "A drawing does not move. Set a strip of drawings inside a slotted drum and spin it, and an "
     "eye at the slots sees each drawing for an instant and the wall of the drum between them. The "
     "gaps matter as much as the pictures: without them the images would smear into one another "
     "and nothing would appear to move at all. What the device supplies is not motion but the "
     "interruption that lets a sequence of stills read as motion.",
     "Which choice best describes the overall structure of the text?",
     ["It states a limitation, describes a device that appears to overcome it, and identifies what the device actually contributes.",
      "It compares the zoetrope with the motion-picture cameras that followed it.",
      "It traces the invention of the zoetrope through its several patents.",
      "It argues that the human eye is easily deceived by rapid images."],
     "A",
     "The opening denies that drawings move, the middle describes the spinning drum, and the close "
     "names the interruption as the real contribution. No second device is described at any point, "
     "so nothing is being weighed against anything else."),

 tsp("S6",
     "Bar-headed geese cross the Himalaya on migration, flying where the air holds about a third of "
     "the oxygen available at sea level. <u>Their haemoglobin binds oxygen more tightly than that "
     "of lowland geese, and the capillaries in their flight muscle run closer to the fibres they "
     "supply.</u> Birds flown in a chamber with the oxygen reduced to match those heights keep "
     "beating their wings at a rate a lowland goose cannot sustain for a minute.",
     "Which choice best describes the function of the underlined sentence?",
     ["It identifies the physiological features that account for the performance reported elsewhere in the text.",
      "It describes the route the geese follow across the mountains.",
      "It questions whether the geese fly as high as has been reported.",
      "It explains how the oxygen level in the chamber was reduced."],
     "A",
     "The sentence names the blood chemistry and the vessel layout that let the bird work in thin "
     "air, which is what the chamber result then demonstrates. How the chamber's oxygen was lowered "
     "is not described anywhere in the text."),

 # ----------------------------------------------- Central Ideas and Details (6)
 cid("C1",
     "A Clark's nutcracker buries pine seeds through the autumn in tens of thousands of separate "
     "caches, a few seeds to a hole, spread across square kilometres of mountainside. It recovers "
     "most of them in spring, months later, including caches lying under fresh snow. Birds tested "
     "in an aviary dig in the right places when the surrounding landmarks are left alone and in "
     "predictably shifted places when those landmarks are moved.",
     "Which choice best states the main idea of the text?",
     ["Nutcrackers depend on the smell of the seeds to relocate what they have buried.",
      "Nutcrackers relocate their scattered caches by remembering positions relative to landmarks.",
      "Nutcrackers bury far more seeds than they are ever able to recover.",
      "Mountain pines depend entirely on nutcrackers to disperse their seeds."],
     "B",
     "Moving the landmarks moves where the birds dig, and moves it predictably, which identifies "
     "the memory as a record of position rather than of the seeds themselves. The smell option is "
     "the explanation the aviary result rules out, since a scent would not shift with a landmark."),

 cid("C2",
     "Before 1883 a town in the United States kept whatever time its own noon gave it, and a "
     "traveller crossing the country reset a watch dozens of times. That was tolerable at the speed "
     "of a horse. It was not tolerable on a railway, where two trains sharing one track are held "
     "apart by a timetable, and a timetable is worthless if the two crews are working to different "
     "clocks. The railway companies, not the government, cut the country into four zones and "
     "imposed them on 18 November 1883; the law caught up thirty-five years later.",
     "According to the text, why did locally kept time become unworkable?",
     ["Travellers found resetting their watches at every town inconvenient.",
      "Trains sharing a track were kept apart by timetables that required every crew to keep the same clock.",
      "The federal government required a single national standard from 1883.",
      "Astronomers could not agree among themselves on when noon occurred."],
     "B",
     "The text names the safety arrangement outright: two trains on one track separated by a "
     "timetable that fails when the crews' clocks differ. The inconvenience to travellers is the "
     "thing the text calls tolerable, which is exactly why it is not the reason given."),

 cid("C3",
     "The gold tesserae of a Byzantine apse are not laid flat. Each cube of glass with its leaf of "
     "gold is pressed into the setting bed at a slight angle to its neighbours, and the angles vary "
     "across the surface. A wall set that way never returns the same reflection twice: as a visitor "
     "moves, different cubes catch the light from the windows and the gold seems to travel across "
     "the vault. Set flush, the same material gives one hard glare and nothing moves.",
     "Which choice best states the main idea of the text?",
     ["The gold used in Byzantine wall mosaics was of unusually high purity.",
      "Setting the tesserae at varying angles makes the reflected light shift as the viewer moves.",
      "Byzantine mosaicists worked more slowly than their Roman predecessors.",
      "The apse was the most difficult part of a Byzantine church to decorate."],
     "B",
     "The passage contrasts the tilted setting with a flush one and attributes the travelling light "
     "to the varying angles alone. Purity of the gold is never discussed, and the material is the "
     "same in both of the cases the text compares."),

 cid("C4",
     "An Argo float sinks to two kilometres, drifts with the current for ten days, descends "
     "further, then rises to the surface measuring temperature and salinity as it climbs and "
     "radios the profile to a satellite before sinking again. Four thousand of them work the open "
     "ocean. Before the programme, most subsurface measurements came from ships, which meant they "
     "came from shipping lanes, in summer, in the northern hemisphere. The floats do not measure "
     "more accurately than a ship does; they measure where no ship goes.",
     "According to the text, what is the main advantage of the floats over ship-based measurement?",
     ["They record temperature and salinity more precisely than shipboard instruments do.",
      "They sample parts of the ocean and times of year that ships rarely reach.",
      "They are considerably cheaper to build than a research vessel.",
      "They can remain at the surface indefinitely without maintenance."],
     "B",
     "The closing sentence denies any gain in accuracy and states the gain as coverage, and the "
     "sentence before it lists the gaps in shipboard sampling. Greater precision is the option the "
     "text explicitly rules out in its last line."),

 cid("C5",
     "A mola is made by stacking three or four cloths of different colours, cutting a shape through "
     "the top layer to reveal the one beneath, then cutting a smaller shape through that, and "
     "turning every cut edge under with a needle. Nothing is applied to the surface; the design "
     "exists only where cloth has been taken away. A Guna woman judges another's work by turning "
     "the panel over, because the quality of a mola lies in the hemming the front is arranged to "
     "hide.",
     "Which choice best states the main idea of the text?",
     ["A mola's design is produced by cutting layers away, and its quality is judged by stitching that the front conceals.",
      "Guna women prefer saturated colours to muted ones in the panels they make.",
      "A mola takes longer to make than an embroidered panel of the same size.",
      "The number of cloth layers used in a mola has increased over time."],
     "A",
     "The text says the design exists only where cloth has been removed and that the panel is "
     "turned over to judge the hemming, which are the two halves of that statement. How long a mola "
     "takes beside an embroidered panel is never mentioned at all."),

 cid("C6",
     "Ramps cut into the kerb at street corners were won by disabled campaigners in Berkeley in the "
     "1970s over objections that the expense would serve very few people. Counts taken at "
     "intersections afterwards found that most of those using the ramps were pushing prams, "
     "wheeling luggage or delivery trolleys, or riding bicycles. The ramps had not created these "
     "users. The users had been lifting and dragging.",
     "Which choice best states the main idea of the text?",
     ["The ramps proved to serve far more people than the group who campaigned for them.",
      "Berkeley was the first city in the United States to install ramps of this kind.",
      "Objections to the ramps were based mainly on how they would look.",
      "Most people using kerb ramps today are wheelchair users."],
     "A",
     "The counts found prams, luggage and bicycles predominating, and the last two sentences "
     "explain that those users existed beforehand and were simply struggling, so the benefit is far "
     "wider than the objection allowed. The text states the objection was expense, which rules out "
     "the option about appearance."),

 # ---------------------------------------------------- Command of Evidence (9)
 coe("E1",
     "An ant infected by the fungus Ophiocordyceps leaves its nest, climbs a sapling and clamps its "
     "jaws onto a leaf vein about twenty-five centimetres above the ground before it dies; the "
     "fungus then fruits from the back of its head. Mycologist Sunil Raghavan argues that the "
     "height and the timing are not incidental but are what the fungus requires.",
     "Which finding, if true, would most directly support Raghavan's argument?",
     ["Fungi that fruited on ants moved to other heights released spores that infected far fewer ants than those released at about twenty-five centimetres, where humidity and temperature best suit the fungus.",
      "Infected ants have been found on the leaves of many different species of sapling.",
      "The fungus can be grown on a laboratory medium with no insect host at all.",
      "Uninfected ants sometimes climb saplings in the course of ordinary foraging."],
     "A",
     "Tying transmission success to that particular height, and to the conditions the fungus needs "
     "there, is what makes the climb a requirement rather than an accident. Growing the fungus "
     "without a host shows only that an insect is not always necessary, which says nothing about "
     "why an infected ant stops where it does."),

 coe("E2",
     "The man found in a glacier on the Italian-Austrian border in 1991 carried an axe with a blade "
     "of nearly pure copper. Because the Alpine copper workings known at the time are later than "
     "his radiocarbon date, several accounts have him carrying metal traded up from the Balkans. "
     "Archaeometallurgist Petra Wenzel argues instead that the copper was smelted from ore close to "
     "where he died.",
     "Which finding, if true, would most directly support Wenzel's argument?",
     ["The lead isotope ratios in the blade match those of ore bodies in the southern Alps within a few days' walk of the find, and not those of Balkan ores.",
      "Copper axes of similar shape have been found across central Europe.",
      "The haft of the axe is yew, a wood available throughout the Alps.",
      "Balkan copper of the period is known to have been traded over long distances."],
     "A",
     "Lead isotopes fix the source of the metal itself, and a match to nearby ore is what a local "
     "smelt predicts and what an import cannot produce. The yew haft establishes that the wooden "
     "part is local, and the claim at issue concerns the copper."),

 coe("E3",
     "A gecko walks up a pane of glass. Its toes carry millions of hairs, each splitting into finer "
     "tips, and the pads leave no residue behind. Physicist Amara Boateng argues that the adhesion "
     "comes from van der Waals attraction between those tips and the surface rather than from "
     "suction.",
     "Which finding, if true, would most directly support Boateng's argument over the alternative?",
     ["Geckos adhere just as strongly inside a chamber pumped down to a near-vacuum, where there is no surrounding air to be excluded from beneath the pads.",
      "A gecko's toes peel away from the surface tip first when it lifts a foot.",
      "Gecko pads adhere better to smooth surfaces than to rough ones.",
      "Some spiders and beetles also carry adhesive hairs on their feet."],
     "A",
     "Suction requires a pressure difference, and removing the surrounding air removes any such "
     "difference, so adhesion that survives a near-vacuum cannot be suction. Better grip on smooth "
     "surfaces is consistent with either account, since both mechanisms need close contact."),

 coe("E4",
     "Fewer than a hundred Wollemi pines survive in a canyon west of Sydney, and the species was "
     "known only from fossils until 1994. Botanist Ngaire Whitcombe argues that the surviving trees "
     "amount to a single individual, propagated by shoots from the base rather than from seed.",
     "Which finding, if true, would most directly support Whitcombe's argument?",
     ["Sequencing of trees taken from every part of the grove finds no detectable genetic variation between them.",
      "The trees bear both male and female cones on the same individual.",
      "Fossil pollen of the genus is found across Australia and Antarctica.",
      "The steep walls of the canyon have sheltered the grove from fire."],
     "A",
     "Any grove grown from seed would carry the variation that sexual reproduction produces, so the "
     "complete absence of it is what a clonal origin predicts. Shelter from fire explains how a "
     "small population persisted without saying anything about how its trees are related."),

 coe("E5",
     "Five letters written on paper in the Sogdian language were recovered from a watchtower west "
     "of Dunhuang, abandoned in transit early in the fourth century. Historian Lu Wenqing argues "
     "that the merchants who wrote them were not itinerant peddlers but agents of family firms with "
     "permanent establishments in the towns they wrote from.",
     "Which finding, if true, would most directly support Lu's argument?",
     ["The letters instruct correspondents to collect debts owed at named addresses and to hold goods in a warehouse until prices rise.",
      "The letters are written on paper rather than on parchment or on wooden slips.",
      "Sogdian was widely used as a language of trade along the routes east of Samarkand.",
      "The watchtower where the letters were found stood on the main route into China."],
     "A",
     "Standing debts at fixed addresses and goods held back against a future price both require a "
     "settled establishment rather than a traveller passing through once. The route the watchtower "
     "stood on tells us where the letters were going, not how the writers' businesses were "
     "organised."),

 coe("E6",
     "Late-summer snowfields in the Arctic turn pink where algae bloom in the melting surface "
     "layer, and the same fields have been photographed from the air every August since the 1970s. "
     "Clean snow returns most of the sunlight that falls on it, while a pigmented surface takes "
     "more of that light in as heat. Glaciologist Tomas Halvorsen argues that these blooms are "
     "themselves a significant cause of the melting rather than merely a symptom of it.",
     "Which finding, if true, would most directly support Halvorsen's argument?",
     ["Plots in which the algae were suppressed reflected about a seventh more sunlight across the season and lost measurably less depth than untreated plots beside them.",
      "Blooms appear earlier in years when the spring is warm.",
      "Algae of the same kind are found on snowfields on four continents.",
      "Pigmented algal cells survive the winter frozen into the snowpack."],
     "A",
     "Suppressing the algae while leaving everything else alike isolates their contribution, and "
     "more reflected light with less melting is precisely the effect the claim predicts. Blooms "
     "appearing earlier in warm springs makes the algae a consequence of warmth, which is the "
     "reading being argued against."),

 coe("E7",
     "Under a ranked ballot a candidate who cannot win outright may still gain from being placed "
     "second by a rival's supporters. Political scientist Dolores Ibarra argues that this feature "
     "of the rules, rather than the character of the candidates who stand, is what makes campaigns "
     "under the system less hostile.",
     "Which finding, if true, would most directly support Ibarra's argument?",
     ["The same candidates who had run negative advertisements in their cities' earlier plurality elections ran markedly fewer of them after the switch to ranked ballots.",
      "Voters in ranked-ballot elections report being more satisfied with the outcome.",
      "Turnout is slightly higher in ranked-ballot elections than in plurality elections.",
      "Ranked-ballot elections take longer to count than plurality elections."],
     "A",
     "Holding the candidates constant and changing only the ballot isolates the rules as the cause, "
     "which is exactly what the claim asserts. Higher satisfaction among voters says nothing about "
     "why the candidates themselves behaved differently."),

 coe("E8",
     "In 1860 &Eacute;douard-L&eacute;on Scott de Martinville traced sound onto soot-blackened "
     "paper with a stylus attached to a membrane. He built no way of playing the tracings back and "
     "said he had never intended one. Historian Ruth Nakamura argues that the phonautograph was "
     "designed as an instrument for studying the shapes of speech rather than as a failed attempt "
     "at recorded sound.",
     "Which finding, if true, would most directly support Nakamura's argument?",
     ["Scott's notebooks pair his tracings with the vowels being spoken and compare their shapes, and he petitioned for the device to be adopted in the teaching of shorthand.",
      "Modern software has reconstructed audible sound from Scott's surviving tracings.",
      "Scott worked as a typesetter and had access to printed accounts of acoustics.",
      "Edison's phonograph, which could play sound back, appeared seventeen years later."],
     "A",
     "Tracings annotated with the vowels that produced them, and a proposed use in teaching "
     "shorthand, are applications that require no playback whatever. Modern reconstruction of the "
     "sound shows what the traces contain, not what their maker was trying to do with them."),

 coe("E9",
     "A platypus dives with its eyes, ears and nostrils shut and finds shrimp in muddy water. Its "
     "bill carries tens of thousands of pores, some sensitive to touch and some to weak electric "
     "fields. Zoologist Elspeth Corrigan argues that the animal locates prey by combining the two "
     "kinds of pore rather than by relying on either alone.",
     "Which finding, if true, would most directly support Corrigan's argument?",
     ["A platypus strikes accurately at a battery-driven electrode only when a pressure wave reaches the bill at the same moment, and misses when either signal is presented on its own.",
      "The electrically sensitive pores are concentrated along the front edge of the bill.",
      "Muscle contractions in a shrimp generate electric fields strong enough to detect.",
      "Platypuses forage mainly at night."],
     "A",
     "Accurate strikes only when both signals arrive together, with failure on either alone, is "
     "what combining two channels predicts and what neither channel could produce by itself. Shrimp "
     "muscle generating a field establishes that there is something to detect, not that two senses "
     "are being used at once."),

 # ------------------------------------------------------------- Inferences (6)
 inf("I1",
     "A zeolite is an aluminosilicate whose crystal structure is riddled with channels of a single "
     "fixed width. Molecules narrower than the channel pass in and are held; molecules wider than "
     "it cannot enter at all. The width does not change with temperature or pressure in the way a "
     "filter's pores might. To separate one gas from another with such a material, then, an "
     "engineer has to choose a zeolite whose channels are _____",
     ["wider than either of the two molecules to be separated.",
      "intermediate in width between the two molecules.",
      "narrower than both of the molecules involved.",
      "able to widen as the gas is heated."],
     "B",
     "Separation happens only when one molecule fits and the other is turned away, which requires a "
     "channel lying between the two in size. Channels wider than both would admit both and separate "
     "nothing at all."),

 inf("I2",
     "In 1964 two radio astronomers at Holmdel could not get rid of a faint hiss in their horn "
     "antenna. They pointed the horn in every direction and the hiss did not change; they cleared "
     "out the pigeons roosting inside it and the hiss did not change; they watched it through the "
     "seasons and it did not change. Any signal coming from a particular source would vary as the "
     "antenna turned. That the hiss never varied indicated that its source was _____",
     ["somewhere inside the antenna itself.",
      "in the atmosphere directly above the site.",
      "spread uniformly across the whole sky.",
      "an intermittent fault in the receiving equipment."],
     "C",
     "The text's stated premise is that a signal from a definite direction changes as the "
     "instrument turns, so a hiss that never changes cannot be coming from a direction and must "
     "fill the sky evenly. The interior of the antenna was investigated and cleaned with no effect, "
     "which rules out a source inside it."),

 inf("I3",
     "A barnacle glues itself to rock that is already wet, and its cement sets under water. "
     "Ordinary adhesives fail there because a film of water sits between the glue and the surface "
     "and neither will bond through it. Analysis of a settling larva shows that its first secretion "
     "is an oily phase that spreads out ahead of the cement. The purpose of that oily phase is "
     "therefore most likely to _____",
     ["harden into the bond that holds the animal down.",
      "displace the water film so that the cement can reach the surface.",
      "dissolve the outer layer of the rock beneath it.",
      "shield the cement from predators while it sets."],
     "B",
     "The obstacle the passage identifies is the water film that keeps glue and rock apart, and "
     "something spreading ahead of the cement is placed exactly where that film is. The passage "
     "assigns the bond itself to the cement, so the oily phase is not what does the holding."),

 inf("I4",
     "A sundial reads the sun; a clock reads an average. The Earth's orbit is elliptical, so the "
     "planet moves faster along it in January than in July, and the tilt of the axis changes how "
     "the sun's daily motion projects onto the dial. Taken together the two effects put solar noon "
     "as much as sixteen minutes away from clock noon at some times of year and bring the two "
     "together at others. An accurate clock and a well-made sundial will therefore agree _____",
     ["at every time of year, once the dial has been correctly aligned.",
      "on only a few dates in the year.",
      "only during the summer months.",
      "only at the equator."],
     "B",
     "The passage describes an offset that swings across the year between sixteen minutes and "
     "nothing, so the two readings coincide only where that swing passes through zero. Correct "
     "alignment cannot remove a discrepancy that changes with the date."),

 inf("I5",
     "A charge for driving into a city centre at peak hours reduces the number of cars entering it. "
     "The drivers who stop coming are by definition those who valued the trip at less than the "
     "charge. Which trips those are depends on what else is available: someone whose route is "
     "served by a frequent train has an easy substitute, while someone starting at four in the "
     "morning from an outer suburb may have none. Introduced without any improvement to those "
     "alternatives, such a charge falls hardest on _____",
     ["drivers making the most valuable trips.",
      "drivers with the fewest other ways of making the trip.",
      "residents of the city centre itself.",
      "commercial deliveries made during the working day."],
     "B",
     "The passage makes the burden depend on what substitutes a driver has, and a driver with none "
     "must either pay the charge or give up the journey. Drivers making the most valuable trips are "
     "the ones the passage says will keep driving and simply pay."),

 inf("I6",
     "An antlion digs its pit in dry sand and in nothing else. It flicks sand out in a spiral until "
     "the walls stand at the steepest angle loose grains will hold, and no steeper. An ant stepping "
     "onto such a wall starts a slide it cannot escape, because every step removes the grains "
     "beneath it. Built in damp sand, which holds a much steeper face without slipping, the same "
     "pit would _____",
     ["collapse before the larva had finished digging it.",
      "fail to give way beneath an ant that walked into it.",
      "take the larva considerably longer to excavate.",
      "trap ants more reliably than a pit in dry sand."],
     "B",
     "The trap works because the wall sits at the limit of what will hold and slips under a "
     "footfall, so material that holds a steeper face without slipping takes the slide away. "
     "Greater difficulty in digging may well be true, but the passage's account turns on whether "
     "the wall gives way, not on the effort of excavation."),

 # ------------------------------------------------------------- Boundaries (12)
 bnd("B1",
     "A single iron bar thick enough to carry a bridge deck cannot be bent onto a drum, and it "
     "cannot be repaired when it fails. John Roebling's mill at Trenton twisted fine wires into "
     "strands and the strands into _____ so made bends around a sheave, and a broken wire inside it "
     "can be found and replaced without taking the whole thing down.",
     ["rope; a rope", "rope, a rope", "rope a rope", "rope: and a rope"],
     "A",
     "Each half of the sentence is a complete statement and no conjunction joins them, so the "
     "semicolon is the only mark that works. Joining them with nothing but a comma produces a "
     "splice."),

 bnd("B2",
     "Rafflesia has no leaves, no stem and no roots of its own; it lives as threads inside a jungle "
     "vine and shows itself only as a flower a metre across. Because the plant spends all but a few "
     "days of its life entirely hidden inside its _____ working in Sumatra map the vines rather "
     "than the flowers.",
     ["host, botanists", "host; botanists", "host: botanists", "host and botanists"],
     "A",
     "The clause opening with 'Because' is dependent and has to be closed off with a comma before "
     "the main clause begins. Both the semicolon and the colon require a complete sentence in front "
     "of them, and a dependent clause is not one."),

 bnd("B3",
     "Wrought iron was made a few kilograms at a time by a puddler stirring a bath by hand. "
     "Bessemer's converter blew cold air up through tonnes of molten pig iron and delivered three "
     "things at _____ with the carbon burned out of it, a charge that stayed hot with no fuel at "
     "all, and a batch finished in twenty minutes rather than in a day.",
     ["once: a metal", "once; a metal", "once, and a metal", "once a metal"],
     "A",
     "The words before the blank form a complete sentence announcing three things, and the colon is "
     "the mark that introduces the list naming them. The semicolon would require a complete "
     "sentence after it, and what follows is a series of noun phrases rather than a sentence."),

 bnd("B4",
     "A netsuke is the toggle that stops a cord from slipping through a sash, and it is handled "
     "constantly, so it can carry no sharp projection anywhere on it. The carver Kaigyokusai "
     "Masatsugu, a man who worked in ivory and boxwood in nineteenth-century _____ his figures so "
     "that every limb folds back into the mass of the piece.",
     ["Osaka, arranged", "Osaka; arranged", "Osaka: arranged", "Osaka arranged"],
     "A",
     "The appositive beginning 'a man who worked' was opened with a comma and must be closed with a "
     "matching comma before the verb that belongs to the subject. Leaving the punctuation out runs "
     "the appositive straight into the predicate."),

 bnd("B5",
     "A ferrofluid is a suspension of iron oxide grains a few nanometres across, each one coated so "
     "that the grains cannot clump together. The liquid pours like any other with no magnet _____ a "
     "field held beneath the dish draws the surface up into a bed of spikes that stand while the "
     "magnet is there and collapse the moment it is taken away.",
     ["near it, but", "near it; but", "near it: but", "near it but"],
     "A",
     "Two independent clauses joined by the coordinating conjunction 'but' take a comma in front of "
     "that conjunction. Neither the semicolon nor the colon is used before a coordinating "
     "conjunction, and dropping the comma altogether leaves two full clauses unseparated."),

 bnd("B6",
     "A suminagashi print is lifted off the surface of a bath of still water. The maker touches the "
     "water alternately with a brush of ink and a brush of surfactant so that each ring spreads "
     "inside the last, then lays down a sheet of absorbent _____ up the whole pattern in a single "
     "contact and cannot be laid down twice.",
     ["paper, which takes", "paper; which takes", "paper: which takes", "paper. Which takes"],
     "A",
     "The clause beginning 'which takes up the whole pattern' is a non-essential relative clause, "
     "and such a clause attaches to the main clause with a comma. The semicolon and the full stop "
     "both need an independent clause after them, and a relative clause is not independent."),

 bnd("B7",
     "A cassowary carries a tall horny casque on its skull, and what it is for has been argued over "
     "for a century. Every explanation offered so far &mdash; a helmet for pushing through "
     "vegetation, an ornament, a resonator for the bird's very low _____ something measurable, and "
     "the measurements have so far settled nothing.",
     ["call &mdash; predicts", "call, predicts", "call; predicts", "call: predicts"],
     "A",
     "The list of explanations was opened with a dash, so it has to be closed with a matching dash "
     "before the sentence resumes. Closing it with a comma leaves the opening dash without a "
     "partner and blurs where the interruption ends."),

 bnd("B8",
     "Capoeira is played inside a ring of people who clap and sing, and the two players move to the "
     "rhythm the ring sets. A stranger watching often cannot tell what is happening, because the "
     "form withholds the one thing a fight would make _____ are thrown to be seen and are pulled "
     "before they land.",
     ["obvious: the blows", "obvious; and the blows", "obvious, the blows", "obvious the blows"],
     "A",
     "The words in front of the blank make a complete sentence, and what follows spells out the "
     "very thing "
     "it has just referred to, which is the colon's work. The comma on its own splices two "
     "independent statements together."),

 bnd("B9",
     "The ship buried at Oseberg in 834 was already old when it went into the ground, and its "
     "timbers were carved along every visible edge. Blue clay and a cap of turf sealed the mound "
     "and kept the air out of _____ wood, the textiles and a wooden cart came out of it in a "
     "condition no ordinary grave would have left them in.",
     ["it; the", "it, the", "it the", "it: and the"],
     "A",
     "The blank sits between two complete statements with no conjunction between them, which is "
     "precisely what the semicolon marks. The comma alone produces a splice, and no punctuation at "
     "all runs the two statements together."),

 bnd("B10",
     "One horse can pull a barge carrying a load no road of the period could take. Although the "
     "ditch dug between Albany and Buffalo was only twelve feet wide and four feet _____ rates "
     "between the Great Lakes and New York fell by something like ninety per cent within a decade "
     "of its opening.",
     ["deep, freight", "deep; freight", "deep: freight", "deep and freight"],
     "A",
     "'Although' opens a dependent clause, and a dependent clause standing in front of its main "
     "clause is separated from it by a comma. The semicolon would require an independent clause on "
     "both sides of it."),

 bnd("B11",
     "A bike-share system empties one part of a city and fills another every weekday morning, and "
     "no amount of forecasting prevents it. Riders take the bikes downhill and towards work in the "
     "_____ carry them back up the hill and out to the residential streets overnight.",
     ["morning; vans", "morning, vans", "morning vans", "morning: and vans"],
     "A",
     "Two complete statements meet at the blank with no conjunction between them, so the semicolon "
     "is the mark required. The comma in that position gives a splice, and the version with no mark "
     "at all makes 'morning vans' read as a single noun phrase."),

 bnd("B12",
     "A cyanotype needs no camera: an object laid on treated paper and left in the sun prints as a "
     "white silhouette on a blue ground. Anna Atkins, a botanist who had been trained to draw "
     "specimens by _____ seaweed directly onto the paper and issued the results in 1843 as the "
     "first book illustrated by photographs.",
     ["hand, laid", "hand; laid", "hand: laid", "hand laid"],
     "A",
     "The appositive describing her opened with a comma and must be closed with a comma before the "
     "verb that belongs to the subject. Any of the other marks would break the sentence at a point "
     "where the subject has not yet reached its verb."),

 # ------------------------------------------------ Form, Structure, and Sense (9)
 fss("F1",
     "Lubok sheets were sold at fairs for a few kopecks and almost none of them were kept. Neither "
     "the museum's curator nor the two visiting conservators _____ able to say which of the four "
     "surviving sheets had been pulled from the same block.",
     ["was", "were", "has been", "is"], "B",
     "With 'neither ... nor', the verb agrees with whichever subject stands nearer to it, and 'the "
     "two visiting conservators' is plural."),

 fss("F2",
     "Clockwork toys were stamped out of tinplate offcuts and painted by hand, and very few of them "
     "ever left the factory in a box. The museum's collection of clockwork tin toys, together with "
     "several hundred trade catalogues, _____ moved to a drier store last winter.",
     ["are", "have been", "were", "was"], "D",
     "The subject is the singular noun 'collection'; the interrupting phrase beginning 'together "
     "with' does not make a singular subject plural."),

 fss("F3",
     "The winter road across the lake is opened when the ice will carry a loaded truck and closed "
     "the moment it will not. By the time the inspectors reached the northern crossing in April, "
     "the ice there _____ to less than half the thickness a loaded truck requires.",
     ["thins", "had thinned", "will thin", "is thinning"], "B",
     "The thinning was complete before the inspectors arrived, and their arrival is itself in the "
     "past, so the past perfect is what places one past event before another."),

 fss("F4",
     "The network reports continuously, and a station that falls silent for more than an hour "
     "brings a technician up the mountain. Each of the seven seismographs on the flank _____ its "
     "own battery, a solar panel and a radio link back to the observatory.",
     ["have", "has", "having", "were having"], "B",
     "'Each' is the subject and is singular; the prepositional phrase naming seven seismographs "
     "does not change the number of the subject."),

 fss("F5",
     "The gasholder frame has stood empty since 1975 and is now a listed structure. The trust's "
     "grant is to strip the lead paint from the ironwork, to light the frame from below and _____ "
     "the ground inside it to the public as an open space.",
     ["opening", "to open", "it opens", "having opened"], "B",
     "The three items joined by 'and' all follow 'is to', and the first two are infinitives, so the "
     "third has to be an infinitive as well. The gerund and the finite clause each break the "
     "parallel structure."),

 fss("F6",
     "A microphone left out overnight records the rain as loudly as it records the birds, and a "
     "single lorry on a distant road spoils an hour of tape. The usable window opens perhaps "
     "twenty minutes before sunrise and closes once the traffic starts, so everything has to be "
     "set up in the dark and left alone. Recording the dawn chorus from the edge of the wood, "
     "_____",
     ["the parabolic reflector was aimed at a single singing blackbird.",
      "a single singing blackbird was picked out by the reflector.",
      "the sound recordist aimed the reflector at a single singing blackbird.",
      "there was a blackbird singing in front of the reflector."],
     "C",
     "The opening participial phrase has to describe whoever was doing the recording, and only the "
     "option beginning with the sound recordist supplies that subject. Beginning with the reflector "
     "says the equipment was recording the dawn chorus on its own."),

 fss("F7",
     "Two gauges of the same pattern were read every morning for thirty years, one on the "
     "escarpment and one in the town below it. The rainfall recorded at the upland gauge is nearly "
     "double _____ recorded at the gauge in the town.",
     ["that", "those", "them", "which"], "A",
     "The pronoun stands in for the singular noun 'rainfall', so the singular form is required; the "
     "plural would need a plural antecedent and the sentence contains none."),

 fss("F8",
     "The foundry took four apprentices at a time and each of them kept a bench of her own. The "
     "foreman inspected all four _____ benches on the last Friday of the month, and no bell was "
     "cast until every tool on them was accounted for.",
     ["apprentices", "apprentice's", "apprentices'", "apprentices's"], "C",
     "The benches belong to all four apprentices, so the noun has to be plural and possessive at "
     "once, which puts the apostrophe after the plural ending. The singular possessive would credit "
     "the benches to one apprentice only."),

 fss("F9",
     "Almost every lowland river in the county was straightened for drainage at some point in the "
     "last two centuries, and a straightened channel loses the gravel riffles that trout spawn "
     "over. The wildlife trust has spent a decade putting bends back into two of them. This brook "
     "is one of the few chalk streams in the district that _____ never been dredged or realigned.",
     ["has", "have", "having", "is"], "B",
     "The relative pronoun 'that' refers back to 'streams', which is plural, so the plural verb is "
     "required; the singular would agree with 'one' instead, which is not what the clause "
     "describes."),

 # -------------------------------------------------------------- Transitions (9)
 trn("T1",
     "An electronic-paper display holds its image with no power at all: the pigment particles stay "
     "where the last pulse of voltage put them, and a page left open for a week costs nothing to "
     "keep on the screen. _____ redrawing the screen is slow, which is why the technology suits a "
     "book and not a film.",
     ["However,", "Therefore,", "Likewise,", "For instance,"], "A",
     "The slow redraw works against the advantage just described, so the transition has to mark a "
     "contrast rather than a consequence."),

 trn("T2",
     "A maglev train is held a centimetre clear of its guideway by magnetic force, and nothing on "
     "the vehicle touches anything on the track. _____ the wear that dominates the maintenance bill "
     "of a conventional railway &mdash; on rails, on wheels, on flanges &mdash; does not arise at "
     "all.",
     ["Nevertheless,", "As a result,", "By contrast,", "In other words,"], "B",
     "The absence of wear follows directly from the absence of contact set out in the first "
     "sentence, which is a cause-and-effect relation. Calling it a restatement would be wrong, "
     "since the second sentence introduces the maintenance consequence rather than rephrasing what "
     "precedes it."),

 trn("T3",
     "Colour film stocks were designed around a reference card showing a pale-skinned model, and "
     "laboratories printed to that reference for decades, so darker skin came out flat and "
     "underexposed. _____ stocks reformulated in the 1970s, under pressure from furniture and "
     "chocolate advertisers who wanted brown to reproduce properly, held detail across a far wider "
     "range of tones.",
     ["By contrast,", "Consequently,", "In addition,", "For example,"], "A",
     "The reformulated stocks behave in the opposite way to the stocks just described, so the "
     "transition sets the two against each other. Presenting it as a consequence would make the "
     "failure of the old stocks the cause of the new ones' performance."),

 trn("T4",
     "Whether a neighbourhood has a supermarket turns out to explain less about what its residents "
     "eat than researchers first expected. Cost, cooking time and what is sold at the places people "
     "already pass on the way home all weigh at least as heavily. _____ a study that opened a "
     "full-service grocery in a district that had none found almost no change in what households "
     "bought over the following year.",
     ["Nevertheless,", "For example,", "In contrast,", "Consequently,"], "B",
     "The grocery study is one instance of the general claim the first two sentences make, so the "
     "transition introduces an example. Nothing in the last sentence works against what precedes "
     "it, which rules out the contrastive options."),

 trn("T5",
     "Scores on standardised intelligence tests rose in every country that kept records through the "
     "twentieth century, and the tests were periodically made harder so that the average would come "
     "back to a hundred. _____ the number such a test reports is set by comparison with the current "
     "population rather than against any fixed standard.",
     ["In other words,", "Nevertheless,", "For instance,", "Meanwhile,"], "A",
     "The second sentence states in general terms exactly what the repeated rescaling shows, which "
     "makes it a restatement. It is not a further instance, since it introduces no new case."),

 trn("T6",
     "An electric car slows itself by running its motor backwards as a generator, returning some of "
     "the energy of motion to the battery instead of throwing it away as heat. _____ every such car "
     "is still built with friction brakes, because a generator cannot hold a stationary vehicle on "
     "a hill and loses its grip entirely as the wheels stop turning.",
     ["Nonetheless,", "Consequently,", "Likewise,", "In short,"], "A",
     "The friction brakes are fitted in spite of the recovery system just described, so the "
     "transition has to concede a contrast. Treating it as a consequence would have the "
     "regenerative system causing the friction brakes to be installed."),

 trn("T7",
     "A dancer trained in bharatanatyam tells a story with the hands, and the vocabulary of hand "
     "positions is fixed: the same shape carries the same meaning for any audience that knows the "
     "form. _____ a passage of the dance can be followed by someone sitting too far back to see the "
     "dancer's face, provided the hands are held clear of the body.",
     ["For this reason,", "By contrast,", "Even so,", "Similarly,"], "A",
     "Being readable at a distance follows from a fixed vocabulary the audience already knows, so "
     "the transition marks a result. Nothing in the second sentence stands against the first, which "
     "rules out the concessive and contrastive options."),

 trn("T8",
     "A word borrowed into a language is usually reshaped until it can be said with the sounds the "
     "borrowing language already has, and speakers stop hearing it as foreign within a generation "
     "or two. _____ a word taken over with its original consonants intact, as happens where many "
     "speakers are bilingual, can introduce a sound the language had no use for before.",
     ["By contrast,", "Consequently,", "In addition,", "For example,"], "A",
     "The second case runs the opposite way from the first: instead of the word being reshaped to "
     "suit the language, the language acquires a new sound. Presenting it as a consequence would "
     "make the first process the cause of the second."),

 trn("T9",
     "Red and green light-emitting diodes were in production by the 1970s, but a blue one required "
     "a crystal of gallium nitride grown with few enough defects to emit light rather than absorb "
     "it, and for twenty years nobody could grow one. _____ the white light-emitting diode, which "
     "is a blue diode behind a yellow phosphor, could not be made until the blue problem had been "
     "solved.",
     ["Consequently,", "Nevertheless,", "Similarly,", "In contrast,"], "A",
     "The white diode's dependence on the blue one makes the delay described in the second sentence "
     "follow from the difficulty described in the first. No contrast is being drawn between them."),

 # ------------------------------------------------------ Rhetorical Synthesis (9)
 syn("R1",
     ["In 1935 about one farm in ten in the United States had electric power.",
      "Private utilities held that rural lines could never recover what they cost to build.",
      "The Rural Electrification Administration lent money to cooperatives formed by farmers themselves.",
      "Cooperative members dug post holes and cleared right-of-way without payment.",
      "By 1950 about nine farms in ten had power."],
     "explain how the objection about cost was answered.",
     ["In 1935 about one farm in ten in the United States had electric power.",
      "Private utilities held that rural lines could never recover their cost; cooperatives built them anyway, on money lent by the Rural Electrification Administration and with their own members' unpaid labour.",
      "By 1950 about nine farms in ten in the United States had electric power.",
      "The Rural Electrification Administration lent money to cooperatives formed by farmers themselves."],
     "B",
     "The goal asks how the expense objection was met, and only the option pairing the loans with "
     "the members' unpaid labour names the two things that brought the cost down. The note about "
     "lending alone gives half of the mechanism and never mentions the objection it answers."),

 syn("R2",
     ["Bark for painting is cut from the stringybark eucalyptus only in the wet season, when it will lift from the trunk.",
      "The sheet is warmed over a fire and weighted flat for several weeks.",
      "Pigments are ochres ground on stone and bound with the sap of an orchid.",
      "Paintings collected in the 1940s were catalogued as artefacts rather than as works by named artists.",
      "Museums have since re-attributed many of them to individual painters."],
     "explain why the material can be gathered only at certain times of year.",
     ["Bark will lift from the stringybark eucalyptus only in the wet season, which is when sheets for painting are cut.",
      "A bark sheet is warmed over a fire and weighted flat for several weeks before it is painted.",
      "Pigments are ochres ground on stone and bound with the sap of an orchid.",
      "Paintings collected in the 1940s were catalogued as artefacts rather than as works by named artists."],
     "A",
     "The goal concerns the timing of the gathering, and only the option tying the cutting season to "
     "the bark lifting from the trunk supplies a reason. Warming and flattening describe what "
     "happens after the sheet is off the tree and say nothing about when it can be taken."),

 syn("R3",
     ["In khoomei a singer produces a low drone and a whistling melody at the same time.",
      "The drone is a single note produced at the vocal folds.",
      "The melody is made of harmonics already present in that drone.",
      "Changing the shape of the mouth and tongue amplifies one harmonic at a time.",
      "A listener hears two voices although only one note is being sung."],
     "explain how a single singer produces two lines at once.",
     ["In khoomei a singer produces a low drone and a whistling melody at the same time.",
      "A listener hears two voices although only one note is being sung.",
      "The melody is not a second note but a harmonic of the drone, picked out one at a time by changes in the shape of the mouth and tongue.",
      "The drone in khoomei is a single note produced at the vocal folds."],
     "C",
     "The goal asks for the mechanism, and only the option identifying the melody as an amplified "
     "harmonic of the one drone explains how a single note yields two lines. Reporting that a "
     "listener hears two voices restates the puzzle instead of resolving it."),

 syn("R4",
     ["A camera lucida is a prism on a stand, patented by William Wollaston in 1806.",
      "Looking through it, the artist sees the subject and the paper superimposed.",
      "The image is not projected; it exists only in the eye of the person at the prism.",
      "The device cannot be shared, photographed or checked by anyone else.",
      "Nineteenth-century drawing manuals complained that beginners lost the image whenever they moved their heads."],
     "explain why the device is difficult to use.",
     ["A camera lucida is a prism on a stand, patented by William Wollaston in 1806.",
      "Because the superimposed image exists only in the eye of the person at the prism, the slightest movement of the head loses it, as nineteenth-century drawing manuals complained.",
      "Looking through the prism, the artist sees the subject and the paper superimposed.",
      "The image produced by a camera lucida cannot be shared or photographed."],
     "B",
     "The goal is the difficulty of working with it, and only the option connecting an image that "
     "exists solely in the viewer's eye to its loss on the slightest movement supplies one. Noting "
     "that the image cannot be shared describes a limitation on it as evidence, not a difficulty in "
     "drawing with it."),

 syn("R5",
     ["Place-names ending in -by and -thorpe are Old Norse in origin.",
      "Names ending in -ton and -ham are Old English.",
      "The Norse endings are dense in Lincolnshire and Yorkshire and rare in Devon.",
      "Written records of Scandinavian settlement in England are thin and were made by hostile chroniclers.",
      "Names stay attached to the land through changes of ownership."],
     "explain why place-names are useful evidence for settlement.",
     ["Place-names ending in -by and -thorpe are Old Norse, while those ending in -ton and -ham are Old English.",
      "The Norse endings are dense in Lincolnshire and Yorkshire and rare in Devon.",
      "Because written accounts of the settlement are thin and hostile, historians turn to names, which stay attached to the land through changes of ownership and so map where Norse speakers settled.",
      "Written records of Scandinavian settlement in England are thin and were made by hostile chroniclers."],
     "C",
     "The goal asks what makes the names useful, and only the option setting the weakness of the "
     "written record against the durability of names on the land answers it. Listing which endings "
     "are Norse identifies the evidence without saying why anyone relies on it."),

 syn("R6",
     ["Adolescent sleep timing shifts later at puberty for biological reasons.",
      "Many secondary schools begin before eight in the morning.",
      "A district in Minneapolis moved its high school start from 7.15 to 8.40 in 1997.",
      "Attendance rose and reported sleep on school nights increased by about an hour.",
      "Bus fleets are shared between primary and secondary schools, so one timetable constrains the other."],
     "emphasise an obstacle to changing school start times.",
     ["Adolescent sleep timing shifts later at puberty for biological reasons.",
      "A district in Minneapolis moved its high school start from 7.15 to 8.40 in 1997, and attendance rose.",
      "Although the Minneapolis change raised attendance and added about an hour of sleep on school nights, bus fleets shared between primary and secondary schools mean that one timetable constrains the other.",
      "Reported sleep on school nights increased by about an hour after the Minneapolis change."],
     "C",
     "The goal calls for something standing in the way, and only the option carrying the shared bus "
     "fleets alongside the result names a constraint. The option reporting the extra hour of sleep "
     "gives the benefit with none of the obstacle."),

 syn("R7",
     ["Caerostris darwini spins webs across rivers in Madagascar, some spanning twenty-five metres.",
      "The bridging line is anchored on both banks before the orb is built.",
      "The spider releases a line into the wind and waits for it to catch on the far side.",
      "Its dragline silk absorbs about twice the energy before breaking that any other spider silk tested absorbs.",
      "A web over open water intercepts insects emerging from the river itself."],
     "explain what the toughness of the silk is needed for.",
     ["Caerostris darwini spins webs across rivers in Madagascar, some of them spanning twenty-five metres.",
      "A bridging line stretched twenty-five metres over a river has to absorb the impact of insects struck at speed above open water, which is what this spider's unusually tough dragline silk allows.",
      "The spider releases a line into the wind and waits for it to catch on the far bank.",
      "The silk absorbs about twice the energy before breaking that any other spider silk tested absorbs."],
     "B",
     "The goal asks what the toughness is for, so the answer has to connect the property to the "
     "span and the impacts it must survive, which only one option does. Stating the energy figure "
     "on its own reports the property without saying what work it does."),

 syn("R8",
     ["Most Athenian public offices in the fourth century BCE were filled by lot rather than by election.",
      "A kleroterion was a stone slab with columns of slots and a tube down one side.",
      "Citizens' name tokens were slotted into the columns; black and white balls were fed into the tube.",
      "Each ball drawn selected or rejected a whole row of tokens at once.",
      "The order of the balls could not be known in advance."],
     "explain how the device kept the outcome from being fixed.",
     ["A kleroterion was a stone slab with columns of slots and a tube down one side.",
      "Most Athenian public offices in the fourth century BCE were filled by lot rather than by election.",
      "Because each ball drawn took or rejected a whole row of name tokens and the order of the balls could not be known beforehand, no official could arrange which citizens were chosen.",
      "Citizens' name tokens were slotted into the columns of the slab."],
     "C",
     "The goal is about resistance to tampering, and only the option tying the whole-row selection "
     "to the unknowable order of the balls explains why the result could not be arranged. "
     "Describing the slab and its slots gives the apparatus with no account of what made it "
     "trustworthy."),

 syn("R9",
     ["The Pony Express carried mail from Missouri to California in about ten days from April 1860.",
      "It used around 180 relay stations and 400 horses.",
      "A letter cost five dollars a half-ounce at the start of the service.",
      "The transcontinental telegraph line was completed on 24 October 1861.",
      "The Pony Express announced its closure two days later."],
     "emphasise how quickly the service was made obsolete.",
     ["The Pony Express used around 180 relay stations and 400 horses to carry mail from Missouri to California.",
      "A service that had opened in April 1860 announced its closure two days after the transcontinental telegraph was completed in October 1861.",
      "The transcontinental telegraph line was completed on 24 October 1861.",
      "A letter carried by the Pony Express cost five dollars a half-ounce at the start of the service."],
     "B",
     "The goal is the speed with which the service was overtaken, and only the option putting the "
     "opening date beside a closure announced two days after the telegraph was finished conveys it. "
     "Giving the telegraph's completion date alone leaves out the service it displaced."),
]

DROPPED = {}
