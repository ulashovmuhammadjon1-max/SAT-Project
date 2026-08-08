#!/usr/bin/env python3
"""
Reading & Writing authored for Test 13.

All 81 items are original. The transcribed pool was spent by Test 8, and for
R&W authoring is in any case the safer route: a transcribed answer key has to
be re-derived by hand before it can be trusted (Test 5 shipped 6 wrong answers
in 81 that way). Every item below carries a `why` recording the reasoning that
produced the key AND the reason the strongest distractor fails - that record IS
the verification, so no key exists here without one.

Rationales name options by their CONTENT, never by letter, so balance_rw.py is
free to rotate every question when it evens out the key distribution.

Writing-domain choices are worded, never bare punctuation. Test 8 shipped
Boundaries items whose four options were ", " / "; " / ": " / " and ", which a
student sees as four empty rows; the real test repeats the words on either side
of the blank inside every option so that each choice reads as the resulting
sentence. Every Boundaries item here is written that way from the start.
Form/Structure items whose options are genuinely words ("was" / "were",
"has" / "have") are left as words, which is also how the real test presents
them.

Topics were checked programmatically against rw_test8.py, rw_test9.py,
rw_test10.py, rw_test11.py and rw_test12.py - all 405 previously authored
passages - and nothing is reused. Candidates that collided with an earlier
test (Sequoyah, kintsugi, qanats, Timbuktu, lost-wax casting at Igbo-Ukwu, the
transatlantic telegraph, chinampas, Linear B, Tambora, amber, coral bleaching,
the Svalbard seed vault, Zheng He, Domesday, sourdough, ambergris, Bazalgette's
sewers, safety lamps, radar, desalination, fog nets, cast-iron columns, tidal
range and vertical farming) were dropped at the planning stage rather than
written and later discovered. What is left:

    bombardier beetles, hagfish slime, cuttlefish papillae, Silbo Gomero,
    Nicaraguan Sign Language, badgir wind towers, the Miura fold, marine snow,
    Ndebele wall painting, hummingbird torpor, ferrofluids, phage therapy,
    blind auditions, ballad burdens, painting media, Muybridge, Anna Atkins's
    cyanotypes, yakhchals, the Westinghouse air brake, the theremin, Pando,
    bar-headed geese, Cahokia, fig wasps, Hangul, the Erie Canal, the
    Archimedes palimpsest, whale falls, mycorrhizal networks, lidar over the
    Peten, Wolbachia, silphium, elephantnose fish, railway time, rotating
    savings clubs, cap carbonates, the deep sound channel, Jacquard cards,
    diatom silica, pneumatic post, sod houses, cloud-seeding trials, the
    Bessemer converter, the Mongol relay, the Highland clearances, silver
    stain, talking drums, the pyramids at Meroe, chained libraries, cochlear
    implants, bar codes, Nancarrow's player-piano studies, globe skimmers,
    Guna molas, moth traps, half-hull models, canal locks, estuary beacons, organ
    restoration, salt flats, salinity gauges, engravers' proofs, hill tracks,
    regenerative braking, roundabouts, chalk, rural electrification,
    Nightingale's wedge diagram, hydraulic rams, antlions, Whitworth threads,
    dark-sky lighting, Oetzi's axe, the kakapo, the Beaufort scale, the Chinese
    examinations, Cornish engine duty reports, Tuvan throat singing, the
    coelacanth, the 1925 serum run to Nome and the pitch-drop experiment.

Block counts (fixed by the assembler's quota, 3 modules x 27):
    Words in Context 15, Text Structure and Purpose 6,
    Central Ideas and Details 6, Command of Evidence 9, Inferences 6,
    Boundaries 12, Form, Structure, and Sense 9, Transitions 9,
    Rhetorical Synthesis 9                                        = 81
"""

SOURCE = "AUTHORED-T13"
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
     "A bombardier beetle keeps hydrogen peroxide and hydroquinone in separate chambers and brings "
     "them together only when something seizes it. The reaction is violent enough to boil the "
     "mixture, which leaves the abdomen as a pulsed spray at close to a hundred degrees. Storing "
     "the ingredients apart until the moment of use is what makes an otherwise _____ chemistry "
     "safe to carry about inside an insect.",
     ["explosive", "harmless", "expensive", "odourless"], "A",
     "The passage describes a reaction violent enough to boil its own products, and the sentence "
     "explains why keeping the ingredients apart matters, so the blank has to name the danger being "
     "managed. The 'harmless' option would remove the very reason the two chambers exist."),

 wic("W2",
     "Threaten a hagfish and it releases a thimbleful of material that becomes litres of gel in a "
     "fraction of a second. The gel is mostly seawater held in a mesh of protein threads, each one "
     "finer than a spider's silk and wound in the gland into a tight skein. What makes the defence "
     "work is not the quantity secreted but the speed with which the threads _____.",
     ["dissolve", "unravel", "harden", "decay"], "B",
     "Turning a thimbleful into litres of gel in an instant depends on skeins of thread opening out "
     "in the water, which is what the closing sentence credits the defence to. The 'harden' option "
     "contradicts the description of a watery gel that clogs a predator's gills."),

 wic("W3",
     "A cuttlefish can raise fleshy spikes called papillae from skin that was smooth a second "
     "earlier, matching the texture of the weed or rubble beside it. The animal holds the shape "
     "with muscle rather than with any rigid support, and can therefore let it go as quickly as it "
     "took it up. Its camouflage is _____ in a way that a fixed pattern never could be.",
     ["reversible", "permanent", "inherited", "conspicuous"], "A",
     "Holding a texture with muscle and releasing it at will is what allows a disguise to be "
     "adopted and then abandoned, which the sentence sets against a fixed pattern. The 'inherited' "
     "option describes where a trait comes from rather than whether it can be undone."),

 wic("W4",
     "Silbo Gomero is Spanish, whistled. Speakers carry the vowels and consonants of the spoken "
     "language over on pitch and interruption alone, and a whistled sentence crosses a ravine on La "
     "Gomera that a shouted one would not. The system is best understood not as a code with a "
     "vocabulary of its own but as a way of _____ a language its users already speak.",
     ["translating", "transmitting", "simplifying", "replacing"], "B",
     "The whistles carry the sounds of ordinary Spanish across a distance, and the sentence denies "
     "that the system has any vocabulary of its own, so the blank names the sending of a language "
     "that already exists. The 'translating' option would require a second language to translate "
     "into, which the text rules out."),

 wic("W5",
     "When deaf children from across Nicaragua were brought together in a new school in the late "
     "1970s, the teachers taught in spoken Spanish and the pupils largely failed to follow. Among "
     "themselves, though, the children pooled the home-made gestures each had arrived with, and the "
     "younger pupils who joined afterwards produced from that pool a grammar their elders had never "
     "used. The language was not taught to them; it was _____ by them.",
     ["borrowed", "invented", "recorded", "abandoned"], "B",
     "The younger pupils produced grammatical structure that nobody had shown them, and the "
     "sentence sets the blank against being taught, so it has to name their own making of the "
     "language. The 'borrowed' option credits an outside source, which is exactly what the passage "
     "denies."),

 wic("W6",
     "A badgir is a shaft raised above the roof with openings on one or more of its faces. Air "
     "entering the shaft is drawn down through the rooms below and out again, and where the shaft "
     "passes over an underground channel of water the air arrives cooled. The tower has no moving "
     "parts and consumes nothing, so a house fitted with one stays tolerable through the afternoon "
     "at no _____ cost.",
     ["recurring", "initial", "social", "apparent"], "A",
     "Something with no moving parts that consumes nothing avoids the kind of cost that would "
     "arrive again every day, which is what the sentence is claiming. The 'initial' option names "
     "the one cost the passage implies was certainly paid, since the tower had to be built."),

 wic("W7",
     "The Miura fold divides a sheet into parallelograms whose creases run in two directions at "
     "once, so that pulling one corner opens the entire sheet in a single motion and pushing it "
     "closes the sheet again. Engineers folding a solar array for launch want exactly that: a panel "
     "the spacecraft can deploy without a separate mechanism at every hinge. The virtue of the "
     "pattern is that its many creases act as one _____.",
     ["obstacle", "mechanism", "ornament", "measurement"], "B",
     "One pull opens every crease at once, which is why no hinge needs machinery of its own; the "
     "creases together do the work of a single device. The 'obstacle' option treats the creases as "
     "an impediment, whereas the passage credits them with the deployment."),

 wic("W8",
     "Almost everything living below the reach of sunlight depends on what falls from above: dead "
     "plankton, faecal pellets and the discarded mucus of animals nearer the surface, drifting down "
     "in pale flakes that take weeks to reach the seabed. Most of the material is eaten on the way "
     "down. What arrives at the bottom is therefore not a sample of the surface but the _____ of it.",
     ["remainder", "duplicate", "forecast", "measure"], "A",
     "Most of the falling material is consumed during the descent, so what reaches the seabed is "
     "only what was left uneaten. The 'duplicate' option is what the sentence explicitly rejects "
     "when it says the arriving material is not a sample of the surface."),

 wic("W9",
     "Ndebele women paint the outside walls of their houses in blocks of colour bounded by black "
     "lines, and the whole surface is renewed after the rains. Early photographs show earth "
     "pigments in a narrow range of ochres; since commercial paint became available the palette has "
     "widened without the geometry changing at all. The tradition has proved _____ about materials "
     "while remaining exact about form.",
     ["exacting", "flexible", "secretive", "indifferent"], "B",
     "New commercial paints were taken up while the geometry stayed as it was, so the blank names "
     "an openness that applies to materials only, which the sentence contrasts with exactness about "
     "form. The 'indifferent' option would suggest the painters do not care what they use, whereas "
     "the passage shows them adopting a better material deliberately."),

 wic("W10",
     "A hummingbird burns through its reserves so fast that a cold night without food would kill "
     "it. On such nights its body cools by more than twenty degrees and its heartbeat drops to a "
     "small fraction of the daytime rate, and it needs the best part of an hour at dawn before it "
     "can fly. The state is not sleep; it is a _____ of the whole metabolism.",
     ["suspension", "quickening", "record", "disguise"], "A",
     "Temperature and heartbeat both drop far below their working levels and take an hour to "
     "return, which is a shutting down of the rate at which the body runs. The 'quickening' option "
     "reverses the direction of every change the passage describes."),

 wic("W11",
     "A ferrofluid is a suspension of iron particles so small that they never settle out, each one "
     "wrapped in a coating that keeps it from sticking to its neighbours. Bring a magnet near and "
     "the liquid climbs into spikes along the field lines; take the magnet away and the spikes "
     "slump back into a puddle. The material is unusual because it is magnetic without ceasing to "
     "be _____.",
     ["visible", "fluid", "solid", "cold"], "B",
     "Spikes that collapse into a puddle the moment the magnet is removed show that the material "
     "still flows, and a magnetic substance that flows is what the sentence calls unusual. The "
     "'solid' option names a state the passage says the material never takes."),

 wic("W12",
     "Phages are viruses that attack bacteria and nothing else, and each kind attacks a narrow "
     "range of hosts. That narrowness was a drawback when antibiotics arrived: a drug that works "
     "against many species is far easier to prescribe than a virus that has to be matched to the "
     "strain in front of you. As resistance spreads, the same _____ is being reconsidered as a "
     "virtue, since a phage leaves the rest of a patient's bacteria alone.",
     ["expense", "specificity", "delay", "toxicity"], "B",
     "The passage twice describes phages as acting on a narrow range of hosts and then says that "
     "sparing the other bacteria is now an advantage, so the blank names that narrowness. The "
     "'toxicity' option raises harm to the patient, which the text never mentions."),

 wic("W13",
     "Several orchestras began seating candidates behind a screen in the 1970s, and some asked them "
     "to take off their shoes so that a heel on the boards would not give anything away. The change "
     "was made to keep the panel's attention on the sound. Whatever else the screen did, it made "
     "the judgement _____ of everything about a player that could be seen.",
     ["independent", "suspicious", "typical", "protective"], "A",
     "Screening the candidate and removing the shoes leave the panel with nothing but what it hears, so the judgement "
     "no longer rests on anything visible. The 'protective' option describes what the screen does "
     "for the candidate rather than what it does to the judgement, which is what the blank is about."),

 meaning("W14",
     "The collector wrote down thirty versions of the same ballad in a single valley, and the "
     "verses differ from village to village: a name changes, a stanza drops out, a rival suitor "
     "appears from nowhere. What holds the versions together is the <u>burden</u> &mdash; the line "
     "sung after every stanza, which the whole room joins in even when only one singer knows how "
     "the story ends.",
     "burden",
     ["A heavy load carried with difficulty.",
      "A line repeated after each stanza of a song.",
      "The main point of an argument.",
      "A duty imposed on someone."],
     "B",
     "The passage defines the term as it uses it: the line that follows every stanza and that "
     "everyone in the room sings. The heavy-load sense is the commonest meaning of the word, but "
     "nothing here concerns carrying anything."),

 meaning("W15",
     "Egg tempera dries within seconds and cannot be blended once it is on the panel, so a painter "
     "builds a shadow out of hundreds of separate strokes laid side by side. Oil stays workable for "
     "days and can be pushed about with a finger. A painter moving from one <u>medium</u> to the "
     "other gives up a habit of working as much as a material.",
     "medium",
     ["A means of mass communication such as television.",
      "The material in which a work of art is made.",
      "A person claiming to pass on messages from the dead.",
      "Something occupying a middle position between two extremes."],
     "B",
     "The word is applied to egg tempera and to oil, two substances a painter works in, and the "
     "sentence says that moving between them means changing a way of working. The middle-position "
     "sense is a genuine meaning of the word but nothing here concerns a point between two "
     "extremes."),


 # --------------------------------------------- Text Structure and Purpose (6)
 tsp("S1",
     "Painters had argued for years about whether a galloping horse ever has all four feet off the "
     "ground at once. In 1878 Eadweard Muybridge set a row of cameras along a track in California "
     "and ran a trip wire from the track to each shutter. <u>The horse photographed itself, firing "
     "the shutters in sequence as it went past.</u> The plates settled the question in an "
     "afternoon: at one point in the stride all four feet are indeed clear of the ground, and "
     "gathered under the body rather than splayed as painters had drawn them.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It explains the arrangement by which the sequence of images was obtained.",
      "It concedes that the photographs failed to settle the dispute.",
      "It describes the way painters had depicted a galloping horse.",
      "It identifies the location at which the cameras were set up."],
     "A",
     "The sentence states that the animal itself tripped each shutter in turn, which is the method "
     "that produced a sequence no photographer could have timed by hand. The location is given in "
     "the sentence before it, so naming it is not the underlined sentence's work."),

 tsp("S2",
     "A cyanotype needs no camera. Paper brushed with two iron salts and dried in the dark turns "
     "deep blue where light falls on it and stays white wherever something has lain on the surface. "
     "Anna Atkins laid dried algae on such paper and set it out in the sun, and from 1843 she "
     "issued the results in parts, with handwritten captions, as a book. It is the earliest book "
     "known to be illustrated with photographs, and it was made because engraving could not render "
     "a specimen of algae accurately enough for the botanists who needed it.",
     "Which choice best states the main purpose of the text?",
     ["To describe a photographic process and the botanical purpose to which it was first put.",
      "To argue that Atkins has been unfairly overlooked in histories of photography.",
      "To explain the chemistry by which iron salts change colour in sunlight.",
      "To compare cyanotypes with the engravings that botanists had used before."],
     "A",
     "The text sets out how the process works and then reports what Atkins made with it and why the "
     "botanists needed it, so it is an account of a process and its first use. The comparison with "
     "engraving occupies the final clause and serves to explain the motive rather than to organise "
     "the text."),

 tsp("S3",
     "A yakhchal is not a store for ice fetched down from the mountains. Water was run into shallow "
     "trenches on winter nights, in the shade of a wall built to keep the low sun off, and it froze "
     "where it lay; the ice was then packed into a domed pit whose thick walls of mud and ash "
     "admitted almost no heat, with a shaft above to draw off whatever warmth did accumulate. Ice "
     "made in a desert in December could in this way be served in July.",
     "Which choice best describes the overall structure of the text?",
     ["It corrects a likely assumption, describes the actual process, and states the outcome.",
      "It presents two rival explanations of the structure and endorses one of them.",
      "It traces the spread of the technique from one region to another.",
      "It lists the materials used in the walls in order of importance."],
     "A",
     "The opening denies a plausible idea about where the ice came from, the middle describes the "
     "freezing and the storage, and the last sentence gives the result. No second explanation is "
     "ever stated, so nothing is being weighed against anything."),

 tsp("S4",
     "Early train brakes were applied by hand, one carriage at a time, and a driver whistling for "
     "brakes could only hope the brakemen heard him. George Westinghouse ran a pipe of compressed "
     "air the length of the train. <u>His crucial decision was to let the pressure hold the brakes "
     "off rather than push them on.</u> A hose that bursts, a coupling that parts, a carriage that "
     "breaks loose &mdash; each of these drops the pressure, and each therefore stops the train "
     "instead of leaving it to run on unbraked.",
     "Which choice best describes the function of the underlined sentence?",
     ["It identifies the design choice whose consequences the rest of the text spells out.",
      "It describes the hand-braking practice that the new system replaced.",
      "It gives the reason compressed air was chosen in preference to steam.",
      "It concedes a weakness in the system that was never resolved."],
     "A",
     "The underlined sentence names the inversion at the heart of the design, and the closing "
     "sentence works through what follows from it whenever something fails. Hand braking is "
     "described in the opening sentence, not in the underlined one."),

 tsp("S5",
     "Leon Theremin's instrument is played without being touched. Two aerials radiate weak radio "
     "fields; the player's hands alter the capacitance around each one, and the circuit turns those "
     "changes into pitch and into volume. There are no keys, frets or stops, so nothing on the "
     "instrument marks where a note lies, and the player has to find every pitch in empty air by "
     "ear. Few instruments are easier to make a sound on and fewer are harder to play in tune.",
     "Which choice best states the main purpose of the text?",
     ["To explain how the instrument works and why playing it accurately is difficult.",
      "To argue that the theremin deserves to be taken more seriously by composers.",
      "To describe the career of the instrument's inventor.",
      "To compare the theremin with the keyboard instruments of its period."],
     "A",
     "The middle of the text explains the aerials and the capacitance, and the last two sentences "
     "explain why an instrument with nothing marking a note is hard to play in tune. The inventor "
     "is named in four words and his career is never discussed."),

 tsp("S6",
     "The stand of aspen in Utah known as Pando covers forty hectares and looks like a wood. "
     "<u>Every trunk in it has grown from one root system and carries the same genes, so the stand "
     "is a single organism rather than a population of them.</u> An individual trunk lives perhaps "
     "a hundred and fifty years; the roots beneath them are older than any trunk by a wide margin, "
     "and put up replacements as the old ones die.",
     "Which choice best describes the function of the underlined sentence?",
     ["It states the fact about the stand that the rest of the text goes on to develop.",
      "It questions whether the trunks are genetically identical.",
      "It explains why aspen trunks are comparatively short-lived.",
      "It compares Pando with other very large organisms."],
     "A",
     "Identifying the stand as one organism sharing a root system is what makes the closing "
     "contrast between short-lived trunks and much older roots meaningful. The lifespan of a trunk "
     "is reported in the final sentence and is not what the underlined sentence asserts."),

 # ----------------------------------------------- Central Ideas and Details (6)
 cid("C1",
     "Bar-headed geese cross the Himalaya twice a year, at heights where the air holds less than "
     "half the oxygen available at sea level. Their haemoglobin takes up oxygen more readily than "
     "that of related lowland geese, their lungs are proportionally larger, and the capillaries "
     "running through their flight muscle are packed more densely. None of this is switched on for "
     "the journey: birds hatched and kept at sea level show the same features.",
     "Which choice best states the main idea of the text?",
     ["The geese are equipped for high flight by inherited traits rather than by changes brought on by the journey.",
      "The geese cross the Himalaya at greater heights than any other bird.",
      "Lowland geese could make the same crossing if they were trained for it.",
      "The birds' flight muscle grows denser capillaries during the migration itself."],
     "A",
     "The text lists physical features and then reports that birds never exposed to altitude have "
     "them too, which puts the source in inheritance rather than in the trip. The option about "
     "capillaries growing during the migration contradicts that closing sentence directly."),

 cid("C2",
     "At its height around 1100 CE, Cahokia held more people than London did, on floodplain across "
     "the river from present-day St Louis. Its builders raised some hundred and twenty earthen "
     "mounds, the largest with a base wider than the Great Pyramid's, and they moved the soil in "
     "baskets: there was no wheel and no draught animal in use. Within two centuries the site was "
     "largely empty, and no single cause of that has been established.",
     "Which choice best states the main idea of the text?",
     ["Cahokia was a very large earthwork city built without wheels or draught animals and later abandoned for reasons still unsettled.",
      "Cahokia's mounds were built to a plan borrowed from Mesoamerica.",
      "Cahokia declined because its floodplain could no longer feed the population.",
      "Cahokia was the only large settlement in North America before European contact."],
     "A",
     "The passage gives the scale of the place, notes that the earth was carried by hand without "
     "wheel or animal, and closes by saying the cause of its emptying is unknown. The option naming "
     "exhaustion of the floodplain supplies precisely the single cause the text says has not been "
     "established."),

 cid("C3",
     "A fig is not a fruit but a chamber of flowers turned inward. A female wasp forces her way in "
     "through a passage so narrow that she loses her wings and often her antennae doing it, lays "
     "her eggs, pollinates the flowers and dies inside. The wasps that hatch mate in the dark; the "
     "males chew an exit and never leave the tree, while the new females fly off carrying pollen to "
     "another fig. Neither the tree nor the insect has any other way of reproducing.",
     "According to the text, what happens to the female wasp that enters a fig?",
     ["She leaves the fig after laying her eggs and carries pollen to another tree.",
      "She is injured entering, lays her eggs, pollinates the flowers and dies inside.",
      "She chews an exit for the males that hatch from her eggs.",
      "She mates inside the fig before she enters it."],
     "B",
     "The second sentence follows the founding female from the injuries she takes at the entrance "
     "through egg-laying and pollination to her death in the chamber. Flying off with pollen belongs "
     "to the next generation of females, whom the passage carefully distinguishes from her."),

 cid("C4",
     "The Korean alphabet promulgated in 1446 was designed rather than inherited. Its consonant "
     "letters are drawn to show the position of the tongue, the lips or the throat that produces "
     "them, and letters for related sounds are built by adding a stroke to a basic shape; vowels "
     "are assembled from three elements. The preface states plainly that the aim was a script an "
     "unlettered person could learn in a morning, at a time when writing Korean meant using Chinese "
     "characters learned over years.",
     "Which choice best states the main idea of the text?",
     ["The alphabet's shapes and structure were built deliberately around the sounds they represent and around ease of learning.",
      "The alphabet replaced Chinese characters immediately after 1446.",
      "The alphabet was the first writing system ever devised for a spoken language.",
      "The alphabet's vowels were borrowed from an earlier Korean script."],
     "A",
     "Letters shaped after the speech organs, related sounds built by adding strokes, and a stated "
     "aim of learning in a morning all point to a script designed around sound and around ease of "
     "learning. The passage says nothing about how quickly Chinese characters were displaced, which "
     "the immediate-replacement option asserts."),

 cid("C5",
     "Before 1825 a ton of flour cost about a hundred dollars to move from Buffalo to New York City "
     "and took three weeks by wagon. The canal that opened that year cut the charge to under ten "
     "dollars and the journey to eight days. Farmers in Ohio who had been feeding surplus wheat to "
     "their pigs, because the grain would not repay the cost of carriage, began shipping it east "
     "instead; within fifteen years the tolls had repaid the whole cost of construction.",
     "According to the text, why had Ohio farmers previously fed surplus wheat to their pigs?",
     ["The wheat they grew was of too poor a quality to sell in the east.",
      "Moving the wheat to market cost more than the wheat would fetch there.",
      "Pigs were worth more in eastern markets than grain was.",
      "There were too few wagons available to carry the wheat east."],
     "B",
     "The passage says the surplus went to the pigs because the grain would not repay carriage, and "
     "the figures just before it show what carriage cost. The option about pigs being worth more "
     "makes a comparison the text never draws."),

 cid("C6",
     "Parchment was expensive enough to be worth reusing. A scribe in 1229 scraped the ink from a "
     "much older book of mathematics, cut the leaves down, turned them and copied a prayer book "
     "onto them. The older text was not removed so much as thinned: iron in the original ink had "
     "bitten into the skin and stayed there. X-ray fluorescence, which maps that iron without "
     "touching the page, has recovered most of the earlier writing from beneath the prayers.",
     "Which choice best states the main idea of the text?",
     ["Traces of the original ink survived the scraping and have been read by mapping the iron they left behind.",
      "The prayer book copied in 1229 is of greater historical value than the mathematics beneath it.",
      "Parchment was reused because scribes disapproved of mathematical writing.",
      "X-ray fluorescence has been used to establish the age of the parchment."],
     "A",
     "The passage explains that iron from the first ink remained in the skin and that a technique "
     "mapping iron has recovered the writing. Establishing the age of the parchment is not what the "
     "text describes the technique doing; it describes it recovering an erased text."),

 # ---------------------------------------------------- Command of Evidence (9)
 coe("E1",
     "A dead whale sinking to the abyssal floor supports a succession of animals for decades, "
     "several of which are known from nowhere else. Biologist Meret Haas argues that these "
     "specialists move from one carcass to the next rather than persisting at a single site.",
     "Which finding, if true, would most directly support Haas's argument?",
     ["Larvae of the specialist species have been trapped in the water column hundreds of kilometres from any known carcass.",
      "A single carcass can support the succession for more than fifty years.",
      "The specialists have been recorded on carcasses in several different oceans.",
      "Bone-eating worms are among the last animals to colonise a carcass."],
     "A",
     "Larvae drifting far from any carcass are the specialists in transit, which is what moving "
     "between sites requires and what a population staying put would not produce. The finding that "
     "one carcass supports the succession for fifty years tells in favour of persisting at a single "
     "site, which is the account being argued against."),

 coe("E2",
     "Fungal threads link the roots of neighbouring trees, and carbon labelled in one tree can "
     "later be detected in another. Ecologist Tom&aacute;s Ferreira argues that the carbon is moved "
     "by the fungus for its own use rather than passed deliberately from tree to tree.",
     "Which finding, if true, would most directly support Ferreira's argument?",
     ["Most of the labelled carbon stays in the fungal tissue itself, and the small amount reaching the second tree arrives whether or not that tree is short of carbon.",
      "Carbon labelled in one tree can be detected in a neighbour within a few days.",
      "Seedlings growing near a large tree survive better than seedlings growing in the open.",
      "The fungal threads link trees of different species as well as trees of the same species."],
     "A",
     "Carbon that mostly remains in the fungus and arrives without regard to the recipient's need "
     "is what a fungus serving itself would produce, and it is not what a transfer aimed at helping "
     "a neighbour would look like. Seedlings faring better near a large tree fits either account, "
     "since shade and shelter would produce the same result."),

 coe("E3",
     "Airborne lidar strips the forest canopy out of the resulting image and shows the ground "
     "beneath it. Surveys of the Pet&eacute;n lowlands have revealed causeways, field walls and "
     "house platforms across country mapped for decades as empty forest. Archaeologist Rosa "
     "Villalobos argues that the population of the region has been badly underestimated, rather "
     "than that the newly visible features belong to a later period than the known centres.",
     "Which finding, if true, would most directly support Villalobos's argument?",
     ["Test excavations on the newly detected house platforms recover pottery of the same periods as the pottery from the long-known city centres.",
      "Lidar detects features under canopy that ground survey would take years to find.",
      "The causeways run between centres that were already known to archaeologists.",
      "Some of the field walls stand less than a metre high."],
     "A",
     "Pottery of the same periods on the new platforms puts people there at the same time as the "
     "known centres, which is what an underestimate of contemporary population requires and what a "
     "later date would rule out. That lidar sees more than ground survey explains how the features "
     "were found without saying anything about when they were occupied."),

 coe("E4",
     "Mosquitoes carrying the bacterium Wolbachia transmit dengue poorly, and the bacterium spreads "
     "through a wild population once enough infected insects have been released. Epidemiologist "
     "Kwame Boateng argues that the fall in dengue cases after such releases is caused by the "
     "bacterium itself rather than by the drop in mosquito numbers that the releases also produced.",
     "Which finding, if true, would most directly support Boateng's argument?",
     ["Neighbourhoods where mosquito numbers fell by the same amount without any release saw no comparable fall in dengue cases.",
      "Dengue cases fell in every neighbourhood where infected mosquitoes were released.",
      "Wolbachia spreads to a majority of the wild population within a year of release.",
      "Dengue is transmitted only by mosquitoes of the genus Aedes."],
     "A",
     "Holding the drop in mosquito numbers constant while leaving the bacterium out isolates which "
     "of the two is doing the work, and the absence of any fall points at the bacterium. The "
     "finding that cases fell wherever releases occurred leaves both explanations standing, since a "
     "release changes both things at once."),

 coe("E5",
     "Silphium, a plant harvested in Cyrenaica and prized across the Roman world, appears on the "
     "coins of the city and then vanishes from the record entirely in the first century CE. "
     "Historian Livia Sartori argues that overharvesting rather than a change in climate ended it.",
     "Which finding, if true, would most directly support Sartori's argument?",
     ["Roman authors record grazing and root-digging pushed to the very edge of the plant's range in its final decades, while pollen cores from Cyrenaica show no shift in rainfall across the same period.",
      "Silphium was valuable enough to be weighed against silver.",
      "No plant matching the ancient descriptions of silphium grows in the region today.",
      "Attempts to cultivate silphium outside Cyrenaica are recorded as having failed."],
     "A",
     "Evidence of harvesting pressure at the same time as pollen cores showing a steady climate "
     "separates the two explanations in exactly the way the claim requires. That no matching plant "
     "grows there now is agreed by both accounts, since each of them ends with the plant gone."),

 coe("E6",
     "An elephantnose fish emits a weak electrical pulse and senses the distortion that nearby "
     "objects impose on the field it creates. Zoologist Ingrid S&oslash;lve argues that the fish "
     "uses these pulses to locate objects around it rather than solely to signal to other fish.",
     "Which finding, if true, would most directly support S&oslash;lve's argument?",
     ["A fish alone in a tank raises its pulse rate sharply when an unfamiliar object is lowered in, and lowers it again once it has swum around the object.",
      "Fish of this species emit pulses of characteristic and distinguishable waveforms.",
      "Pulse rates rise when two fish are placed in the same tank.",
      "The electric organ develops from modified muscle tissue."],
     "A",
     "Stepping up the pulses at a new object and settling once the object has been explored is "
     "what using the pulses to examine surroundings predicts, and no other fish is present to be "
     "signalled. Waveforms that differ between individuals is what the signalling account would "
     "predict instead."),

 coe("E7",
     "Until the 1840s a British town set its clocks by the sun, and Bristol ran some ten minutes "
     "behind London. Historian Alun Pryce argues that the adoption of a single national time was "
     "driven by the railway timetable rather than by the electric telegraph, which came into use at "
     "about the same period.",
     "Which finding, if true, would most directly support Pryce's argument?",
     ["Railway companies had imposed London time along their lines several years before the telegraph reached most of the towns on those lines.",
      "The telegraph allowed a time signal to be sent from Greenwich to a distant town in an instant.",
      "Some town councils resisted the change and kept their own time for years afterwards.",
      "Bristol lies far enough west of London for the difference between them to be noticeable."],
     "A",
     "Companies imposing London time before the telegraph had arrived puts the change earlier than "
     "the mechanism the rival account credits, which is what the claim needs. The instantaneous "
     "Greenwich signal describes the telegraph's capability and so tells for the account being "
     "argued against."),

 coe("E8",
     "In a rotating savings club, a fixed group of members pays the same sum into a pot at every "
     "meeting and each member in turn takes the whole pot away. Economist Ndidi Achebe argues that "
     "what keeps a member who has already taken the pot from walking away is that member's standing "
     "among the others rather than any penalty that could be enforced.",
     "Which finding, if true, would most directly support Achebe's argument?",
     ["Default is rarest in clubs whose members are neighbours or worship together, and no club in the sample has ever recovered money through a court.",
      "Members who take the pot early gain more from the arrangement than those who take it late.",
      "Clubs are commonest in districts where bank branches are few.",
      "The order in which members take the pot is usually settled by lot."],
     "A",
     "Default falling away where members share a community, combined with courts never being used, "
     "points at reputation and away from enforcement. Clubs being common where banks are scarce "
     "explains why people join and says nothing about what keeps them paying afterwards."),

 coe("E9",
     "Glacial deposits of about 635 million years ago are found on every continent, including "
     "several that lay at the equator at the time. Directly above them, worldwide, lies a "
     "distinctive layer of carbonate rock tens of metres thick. Geologist Hana Oyelaran argues that "
     "this cap carbonate records a rapid end to a global glaciation rather than the slow, piecemeal "
     "retreat of separate ice sheets.",
     "Which finding, if true, would most directly support Oyelaran's argument?",
     ["The cap carbonate rests straight on the glacial deposits everywhere it occurs, with no weathered surface and no gap in deposition between the two.",
      "Glacial deposits of this age are found on every continent.",
      "Carbonate rock forms readily in warm, shallow seas.",
      "The carbonate layer is thickest in sections that lay closest to the equator."],
     "A",
     "Carbonate lying straight on the glacial deposits with nothing in between means the change "
     "happened everywhere without a pause, which is what a rapid worldwide end requires and what a "
     "piecemeal retreat would not produce. The worldwide spread of the glacial deposits is already "
     "stated in the passage and establishes only that the glaciation was global."),

 # -------------------------------------------------------------- Inferences (6)
 inf("I1",
     "Sound travels faster in warm water and faster again under pressure. Between the warm surface "
     "and the cold, high-pressure deep there is therefore a depth at which the speed of sound "
     "reaches a minimum, and sound that strays above or below that depth is bent back towards it. "
     "A low call made at that depth is trapped in the layer and can be picked up thousands of "
     "kilometres away, which suggests that the range of such a call depends less on its loudness "
     "than on _____",
     ["the depth at which it is made.",
      "the temperature of the water at the surface.",
      "the size of the animal that makes it.",
      "the direction in which it is aimed."],
     "A",
     "The passage makes the trapping depend on the call being made at the depth where the speed of "
     "sound is least, and it is the trapping that carries the sound so far. Surface temperature "
     "helps to fix where that depth lies but is not the condition a particular call has to meet."),

 inf("I2",
     "A Jacquard loom reads a chain of punched cards. Where a hole appears, a hook passes through "
     "and lifts its warp thread; where the card is solid, the hook is blocked. The pattern woven "
     "into the cloth is fixed entirely by the cards, and the same loom weaves an altogether "
     "different design as soon as a different chain is hung on it. Changing what the machine "
     "produced therefore required no alteration to _____",
     ["the design punched into the cards.",
      "the machine itself.",
      "the thread used in the warp.",
      "the speed at which the loom was worked."],
     "B",
     "The passage says the same loom weaves a new design the moment a new chain of cards is hung on "
     "it, so what goes untouched is the mechanism. The design punched into the cards is precisely "
     "what does have to change."),

 inf("I3",
     "Diatoms build their cases from silica dissolved in seawater, and where they bloom they draw "
     "the surface water almost clear of it. The cases sink when the cell dies, and much of the "
     "silica they carry down is buried in the sediment rather than returning to the surface. Rivers "
     "deliver fresh silica to the ocean at a rate that has been measured. Over the long run, then, "
     "the silica available at the surface must be governed by _____",
     ["the number of diatom species present.",
      "the balance between river supply and burial in the sediment.",
      "the depth at which the sinking cases finally settle.",
      "the temperature of the surface water."],
     "B",
     "The passage names exactly two processes that move silica into and out of the surface ocean, "
     "delivery by rivers and loss to the sediment, so what remains available depends on how the two "
     "compare. The depth at which the cases settle does not change the fact that the silica has "
     "left the surface."),

 inf("I4",
     "The pneumatic tube networks that carried letters beneath several European cities charged by "
     "the canister rather than by the mile, and a canister crossed a capital in minutes at any hour "
     "of the day. The tubes were shut down in the 1980s. What ended them was not that anything "
     "faster had appeared on the streets above, since the traffic there had only grown worse, but "
     "that the messages themselves _____",
     ["had become too heavy for the canisters.",
      "no longer had to be carried as objects at all.",
      "were now sent at night rather than by day.",
      "cost more to write than they did to deliver."],
     "B",
     "The passage rules out a faster physical alternative, so the change has to lie in the messages "
     "rather than in the transport, and a message that need not be moved physically leaves nothing "
     "for a tube to carry. Weight was never at issue for letters, which the tubes had always taken."),

 inf("I5",
     "Settlers reaching the treeless grassland found no timber within a hundred miles and no money "
     "to freight any in. They cut the turf itself into blocks and laid them like masonry, roofing "
     "the result with more turf over whatever poles could be found. The walls stood two feet thick "
     "and cost nothing but labour. That such houses were built by families who had put up timber "
     "houses elsewhere suggests that the choice of material was governed by _____",
     ["a preference for the appearance of turf.",
      "what the site itself could supply.",
      "building regulations in force on the grassland.",
      "the speed with which turf could be cut."],
     "B",
     "The families are described as knowing perfectly well how to build in timber, so the switch is "
     "explained by there being no timber within reach and no money to bring any, which is a matter "
     "of local supply. Speed of cutting is never mentioned and would not explain why timber was "
     "unavailable."),

 inf("I6",
     "A seeding aircraft releases silver iodide into a cloud that is already producing some snow, "
     "and snow falls afterwards. Since the cloud would have produced snow in any case, a single "
     "flight tells an observer nothing on its own. Establishing an effect requires that suitable "
     "clouds be assigned at random to be seeded or left alone, over many seasons, because otherwise "
     "the operators' judgement about which clouds are worth flying into would _____",
     ["reduce the total quantity of snow produced.",
      "make the seeded and the unseeded clouds different to begin with.",
      "have no bearing at all on the results obtained.",
      "be impossible to record accurately."],
     "B",
     "If operators pick out the clouds most likely to snow, the seeded group is already unlike the "
     "unseeded group before any silver iodide is released, and that is the confusion random "
     "assignment exists to prevent. Saying the judgement has no bearing would leave no reason to "
     "randomise anything."),

 # ------------------------------------------------------------- Boundaries (12)
 bnd("B1",
     "Steel had been made in crucibles a few pounds at a time and cost accordingly. Henry Bessemer "
     "found that blowing cold air up through molten pig iron burns out the carbon and raises the "
     "temperature of the charge rather than lowering _____ converter of thirty tons could be blown "
     "in twenty minutes with no fuel under it at all.",
     ["it; a converter", "it, a converter", "it a converter", "it: and a converter"], "A",
     "Two complete statements stand on either side of the blank with no conjunction between them, "
     "which is what the semicolon is for. The comma on its own splices the two together, and adding "
     "a conjunction after a colon puts a mark where the colon does not take one."),

 bnd("B2",
     "A rider on the Mongol relay carried a message only as far as the next station. Because fresh "
     "horses, food and a bed waited at intervals of a day's ride the whole way from the Danube to "
     "_____ dispatch could travel at a speed no single horse and no single rider could have "
     "sustained.",
     ["Beijing, a dispatch", "Beijing; a dispatch", "Beijing: a dispatch", "Beijing and a dispatch"],
     "A",
     "The clause opening with 'Because' is dependent and has to be closed off with a comma before "
     "the main clause begins. Both the semicolon and the colon require a complete sentence in front "
     "of them, and a dependent clause is not one."),

 bnd("B3",
     "Between 1780 and 1850 landlords across the Scottish Highlands replaced tenants with sheep. "
     "The parish register of one estate records what became of the twenty-four families evicted in "
     "a single _____ eleven to the coast to work at the kelp, nine to Glasgow, and four aboard a "
     "ship for Nova Scotia.",
     ["decade: eleven", "decade; eleven", "decade, and eleven", "decade eleven"], "A",
     "The words before the blank make a complete sentence announcing what the register records, and "
     "the colon is the mark that introduces the list which specifies it. The semicolon would demand "
     "a complete sentence after it, and a list of destinations is not one."),

 bnd("B4",
     "Medieval glaziers coloured glass in the pot by stirring metal oxides into the melt, so that a "
     "blue was blue the whole way through. Silver stain, which reached northern workshops in the "
     "fourteenth century, was painted onto the surface of a finished sheet and fired _____ the same "
     "sheet could now carry a pot colour and a yellow laid over the top of it.",
     ["in, and", "in; and", "in: and", "in and"], "A",
     "Two independent clauses joined by the coordinating conjunction take a comma in front of that "
     "conjunction. The semicolon and the colon are not used before a coordinating conjunction, and "
     "dropping the comma leaves two full clauses running together."),

 bnd("B5",
     "A drummer on a talking drum reproduces the tone pattern of speech rather than a code agreed "
     "in advance. Because the spoken language is itself tonal, a phrase beaten out on the drum "
     "&mdash; the pitch, the rhythm, the length of every _____ is recognisable to a listener who "
     "has never learned a drum alphabet of any kind.",
     ["syllable &mdash; is recognisable", "syllable, is recognisable",
      "syllable; is recognisable", "syllable: is recognisable"], "A",
     "The list of features was opened with a dash and has to be closed with a matching dash before "
     "the sentence resumes. Closing it with a comma leaves the opening dash without a partner and "
     "blurs where the interruption ends."),

 bnd("B6",
     "The pyramids at Meroe are steeper and very much smaller than the Egyptian ones, and there are "
     "a great many more of them. Meroe, the capital of the kingdom of Kush for some six hundred "
     "_____ over two hundred of them along a few kilometres of desert.",
     ["years, holds", "years; holds", "years: holds", "years holds"], "A",
     "The appositive beginning 'the capital of the kingdom of Kush' was opened with a comma and "
     "must be closed with a matching comma before the verb. Any other mark would break the sentence "
     "at a point where the subject has not yet reached its verb."),

 bnd("B7",
     "A book in the fifteenth century could cost more than the desk it lay on. In the libraries "
     "that survive at Hereford and at Wells, every volume is fastened to a rod by a chain long "
     "enough to reach a reading _____ was never long enough to reach the door.",
     ["desk, which", "desk; which", "desk: which", "desk. Which"], "A",
     "'which' opens a non-essential relative clause, and such a clause attaches to the main clause "
     "with a comma. The semicolon and the full stop both require an independent clause after them, "
     "and a relative clause is not independent."),

 bnd("B8",
     "A cochlear implant does not make sound louder. It converts sound into pulses delivered "
     "straight to the auditory nerve, and a recipient has to learn to hear all over again. Adults "
     "fitted with one describe the first weeks in strikingly similar _____ whistling, static, and "
     "voices that seem to arrive through a badly tuned radio.",
     ["terms: whistling", "terms; whistling", "terms, and whistling", "terms whistling"], "A",
     "What stands before the blank is a complete sentence announcing the terms, so the colon is the "
     "mark that introduces the list giving them. The semicolon would demand a complete sentence "
     "after it, and a list of three descriptions is not one."),

 bnd("B9",
     "The first patent for a bar code was granted in 1952 and nothing came of it for twenty years, "
     "because no reader cheap enough to sit at a till could make out the pattern. The laser and the "
     "microprocessor changed _____ grocery in Ohio scanned a packet of chewing gum in 1974, and the "
     "system spread from there.",
     ["that; a grocery", "that, a grocery", "that a grocery", "that: and a grocery"], "A",
     "Both halves are complete sentences with no conjunction between them, so the semicolon is the "
     "only mark that will serve. The comma alone would splice them, and putting a conjunction after "
     "a colon adds a word the mark does not take."),

 bnd("B10",
     "Conlon Nancarrow wrote for the player piano because no pianist could play what he wanted "
     "written. Although the studies he punched into the rolls call for speeds and combinations of "
     "tempo that no pair of hands could _____ composer punched every hole in them by hand, one at a "
     "time, for more than forty years.",
     ["manage, the composer", "manage; the composer", "manage: the composer", "manage and the composer"],
     "A",
     "'Although' opens a dependent clause, and a dependent clause standing in front of the main "
     "clause is separated from it by a comma. The semicolon and the colon each require an "
     "independent clause in front of them."),

 bnd("B11",
     "A globe skimmer weighs less than a gram and is the most widely distributed dragonfly on "
     "earth. It is not built to cross an ocean under its own power; _____ rides the monsoon winds "
     "between India and East Africa, refuelling at pools that appear only in the wet season.",
     ["however, it", "however it", "however; it", "however: it"], "A",
     "Any conjunctive adverb opening the second clause takes a comma after it, the semicolon in front "
     "of it having already done the joining. Leaving the comma out runs the adverb straight into "
     "the clause it introduces."),

 bnd("B12",
     "A mola is built from several layers of cloth basted together, and the design is made by "
     "cutting away the upper layers to show the colours lying beneath them. Molas, the panels sewn "
     "into the front and back of a Guna woman's _____ sold to collectors long before anyone outside "
     "the islands understood how they had been made.",
     ["blouse, were", "blouse; were", "blouse: were", "blouse were"], "A",
     "The appositive beginning 'the panels sewn into the front and back' opened with a comma and "
     "must be closed with one before the verb belonging to the subject. Without that closing comma "
     "the appositive runs straight into the predicate."),

 # ------------------------------------------------ Form, Structure, and Sense (9)
 fss("F1",
     "The trap is run on the same three nights of every month and emptied at first light, and the "
     "catch is recorded before the moths have warmed up enough to fly. Neither the recorder nor the "
     "two volunteers who sort the catch _____ able to account for the run of southern species that "
     "turned up last August.",
     ["was", "were", "has been", "is"], "B",
     "With 'neither ... nor', the verb agrees with whichever subject stands nearer to it, and 'the "
     "two volunteers' is plural."),

 fss("F2",
     "The models were made in the yards that built the ships, at a fixed scale, and half of them "
     "still carry their original rigging. A number of the builders' half-hulls in the store _____ "
     "never been catalogued at all.",
     ["has", "have", "is", "was"], "B",
     "The phrase 'a number of' takes a plural verb, because it refers to the several half-hulls "
     "themselves rather than to a single count of them. The singular verb would agree with the word "
     "'number' alone, which is not what the sentence is about."),

 fss("F3",
     "The lock was to be rebuilt in a single closed season and the work ran into a second. By the "
     "time the boats came back through in April, the timber gates that had leaked all through the "
     "previous summer _____ for the last time.",
     ["are replaced", "had been replaced", "will be replaced", "are being replaced"], "B",
     "The replacement was finished before the boats returned, and the return is itself in the past, "
     "so the past perfect is what places one past event before another."),

 fss("F4",
     "The beacons are inspected once a quarter, and a light that fails between inspections is "
     "usually reported by the fishing boats before anyone ashore has noticed. Each of the nine "
     "beacons on the estuary _____ its own solar panel and a battery sized to carry it through a "
     "fortnight of cloud.",
     ["have", "has", "having", "were having"], "B",
     "'Each' is the subject and is singular; the prepositional phrase naming nine beacons does not "
     "change the number of the subject."),

 fss("F5",
     "The organ has not been played since the roof leaked over it in 1998, and half the pipework is "
     "stored in crates in the vestry. The grant is to clean the pipes, to rebuild the bellows and "
     "_____ the instrument for a recital at Easter.",
     ["tuning", "to tune", "it tunes", "having tuned"], "B",
     "The three items joined by 'and' all follow 'is to', and the first two are infinitives, so the "
     "third has to be an infinitive as well. The gerund and the finite clause both break the "
     "parallel structure."),

 fss("F6",
     "The salt flat is crossed only in the hour after dawn, while the crust is still hard enough to "
     "bear weight and the standing water has not yet been stirred up by the wind. Timing the "
     "crossing badly, _____",
     ["the crust gave way under the vehicle.",
      "the vehicle broke through the crust and had to be dug out.",
      "the survey team broke through the crust and lost a morning digging the vehicle out.",
      "there was a break in the crust beneath the vehicle."],
     "C",
     "The opening participial phrase has to describe whoever did the timing, and only the option "
     "beginning with the survey team supplies that subject. Beginning with the crust makes the "
     "ground itself responsible for timing the crossing."),

 fss("F7",
     "Two gauges record the salinity of the same estuary, one at the mouth and one six miles "
     "upstream. The salinity measured at the mouth in August is nearly twice _____ recorded at the "
     "upstream gauge in the same month.",
     ["that", "those", "them", "which"], "A",
     "The pronoun stands in for the singular noun 'salinity', so the singular form is required; the "
     "plural form would need a plural antecedent and the sentence contains none."),

 fss("F8",
     "Two engravers worked on the plates for the atlas, and each pulled proofs of his own before "
     "any sheet went to press. The library holds both _____ proofs, and the differences between "
     "them show where a line was strengthened after the first pull.",
     ["engravers", "engraver's", "engravers'", "engravers's"], "C",
     "The proofs belong to both engravers, so the noun has to be plural and possessive at once, "
     "which puts the apostrophe after the plural ending. The singular possessive would credit every "
     "proof to one engraver."),

 fss("F9",
     "Three tracks cross the ridge, and the two western ones carry walkers all summer. Of the "
     "three, the eastern track is the _____, which is why the estate keeps it clear for the "
     "shepherds and lets the others go back to grass.",
     ["shorter", "shortest", "more short", "short"], "B",
     "The comparison is among three tracks, so the superlative is required; the comparative form "
     "would set only two of them against each other."),

 # -------------------------------------------------------------- Transitions (9)
 trn("T1",
     "A train slowing into a station turns its motors into generators, and the current they produce "
     "can be pushed back into the overhead line for another train to draw on. _____ that works only "
     "if a train on the same section happens to be taking power at the moment of braking; where "
     "none is, the energy is dumped as heat in a bank of resistors.",
     ["However,", "Therefore,", "Likewise,", "For instance,"], "A",
     "The condition set out in the second sentence cuts against the advantage described in the "
     "first, so the transition has to mark a contrast rather than a consequence."),

 trn("T2",
     "A signalised junction stops one stream of traffic in order to release another, and a vehicle "
     "arriving on a red light waits whether or not anything is actually crossing. A roundabout has "
     "no signal to obey: a driver gives way only to traffic already on the ring. _____ a roundabout "
     "carries more vehicles an hour than a signalised junction of the same size at everything short "
     "of the heaviest flows.",
     ["Nevertheless,", "As a result,", "By contrast,", "In other words,"], "B",
     "The higher capacity follows from drivers waiting only when something is genuinely crossing, "
     "which is a cause-and-effect relation. Calling it a restatement would be wrong, since the "
     "second sentence reports a measured outcome rather than rephrasing the rule."),

 trn("T3",
     "The white cliffs are built from the plates of single-celled algae, each plate a few "
     "thousandths of a millimetre across, that settled onto a shelf seabed one at a time. _____ a "
     "block of chalk the size of a hand represents the quiet accumulation of countless generations.",
     ["Consequently,", "Nevertheless,", "By contrast,", "For example,"], "A",
     "The size of a single plate and the settling one at a time are what make a small block the "
     "record of so many organisms, so the second sentence follows from the first. No contrast is "
     "being drawn between them."),

 trn("T4",
     "When the federal programme began in 1935, nine farms in ten in the United States had no "
     "electricity, and the private utilities had declined to run lines out to them at any price "
     "they were willing to charge. The programme lent money instead to cooperatives formed by the "
     "farmers themselves, who dug the holes and set the poles. _____ within twenty years the "
     "proportion had reversed, and nine farms in ten were connected.",
     ["Nevertheless,", "By contrast,", "For example,", "As a result,"], "D",
     "The reversal of the proportion is the outcome of the loans and the cooperatives just "
     "described, which is a cause-and-effect relation. Nothing in the second sentence works against "
     "the first, which rules out the contrastive options."),

 trn("T5",
     "Nightingale's report set out the mortality figures for the army hospitals month by month, and "
     "the columns of numbers went to men who had every reason not to read them. She drew the same "
     "figures as wedges of a circle, one wedge to a month, with the area of each wedge standing for "
     "the deaths and the deaths from preventable disease shaded separately. _____ a reader who "
     "would never have worked through the table could see at a glance that most of the dead had "
     "been killed by something other than wounds.",
     ["Consequently,", "Nevertheless,", "Similarly,", "In contrast,"], "A",
     "Seeing the point at a glance is the effect of turning the columns into shaded wedges, so the "
     "second sentence follows from the first. No contrast is being drawn, since both sentences "
     "concern the same figures presented two ways."),

 trn("T6",
     "An electric pump raises water for as long as it is supplied with power, and a village on a "
     "hillside with no grid connection gets nothing out of one. A hydraulic ram uses the momentum "
     "of falling water to lift a fraction of that water higher than it started, and it has two "
     "moving parts and no external supply of any kind. _____ a ram installed on a stream runs "
     "unattended for years at the cost of an occasional valve.",
     ["By contrast,", "Consequently,", "In addition,", "For example,"], "B",
     "Running unattended for years follows from having two moving parts and needing no supply, both "
     "of which are stated in the sentence immediately before. The contrastive option would have to "
     "set the ram against itself, since the electric pump is two sentences back."),

 trn("T7",
     "An antlion larva digs a pit in loose sand and waits at the bottom of it. The slope is cut as "
     "steep as the sand will hold, so that an ant walking over the rim starts a small slide it "
     "cannot climb out of, and the larva throws up more sand to keep the slide going. _____ a "
     "trapdoor spider sinks a burrow with a hinged lid that it holds shut from below, letting the "
     "ground itself do the work of concealment.",
     ["Consequently,", "Similarly,", "Nevertheless,", "For example,"], "B",
     "The spider is a second case of a predator making the ground do its hunting for it, so the "
     "transition has to signal comparison. The spider is not an instance of an antlion, which is "
     "what the example transition would claim."),

 trn("T8",
     "Before 1841 every workshop cut its own threads, and a bolt made in one shop would not enter a "
     "nut tapped in another; a machine repaired away from home had to have its fastenings made on "
     "the spot. Joseph Whitworth measured screws from workshops across the country and proposed a "
     "single thread angle and a fixed number of threads to the inch for each diameter. _____ a bolt "
     "could be bought rather than made, and a broken one replaced out of a drawer.",
     ["As a result,", "Nevertheless,", "By contrast,", "In other words,"], "A",
     "Buying a bolt instead of making one is the outcome of a single agreed thread form, which is a "
     "cause-and-effect relation. It is not a restatement, since the second sentence introduces a "
     "consequence rather than rephrasing the proposal."),

 trn("T9",
     "Several towns have rewritten their street-lighting rules to require shielded fittings that "
     "throw no light above the horizontal. The stated aim is usually the night sky, which such "
     "fittings do measurably darken. _____ the same fittings put more of each lamp's output onto "
     "the road, so the towns concerned have generally been able to fit lower-powered lamps and cut "
     "the lighting bill as well.",
     ["Nevertheless,", "In addition,", "In contrast,", "For example,"], "B",
     "The second sentence sets a further benefit alongside the darker sky rather than qualifying "
     "it, so the transition marks addition. Nothing in it works against the first sentence, which "
     "rules out the concessive and contrastive options."),

 # ------------------------------------------------------ Rhetorical Synthesis (9)
 syn("R1",
     ["The body found in the &Ouml;tztal Alps in 1991 dates to about 3300 BCE.",
      "It was buried with an axe whose blade is almost pure copper.",
      "Copper working had been thought to reach the region several centuries later than that.",
      "Lead isotopes in the blade match ores in southern Tuscany, some 500 km away.",
      "Hair from the body carries traces of arsenic, a by-product of smelting copper."],
     "explain what the axe indicates about the spread of copper working.",
     ["The body found in the &Ouml;tztal Alps in 1991 dates to about 3300 BCE.",
      "An almost pure copper axe buried about 3300 BCE, its blade matching Tuscan ores some 500 km off, puts copper working in the region centuries earlier than had been thought and ties it to a distant source.",
      "Hair from the body carries traces of arsenic, a by-product of smelting copper.",
      "The blade of the axe is almost pure copper rather than an alloy."],
     "B",
     "The goal asks what the axe shows about the spread of the craft, and only the option carrying "
     "the early date, the distant ore source and the revision to the accepted chronology answers "
     "it. The note about arsenic in the hair bears on whether the man smelted metal himself, not on "
     "how far the craft had travelled."),

 syn("R2",
     ["The kakapo is a flightless, nocturnal parrot found only in New Zealand.",
      "By 1995 only 51 birds were known to survive.",
      "Females breed only in years when the rimu tree fruits heavily, which happens every two to four years.",
      "Every living bird wears a transmitter and has a file of its own.",
      "Supplementary feeding was found to raise the proportion of male chicks, and the feeding was changed."],
     "emphasise a difficulty that the recovery programme has had to work around.",
     ["Every living kakapo wears a transmitter and has a file of its own.",
      "The kakapo is a flightless, nocturnal parrot found only in New Zealand, and by 1995 only 51 birds were known to survive.",
      "Because females breed only in the years when the rimu fruits heavily, the programme can add chicks only once every two to four years.",
      "By 1995 only 51 kakapo were known to survive."],
     "C",
     "The goal calls for something the programme has to work around, and breeding tied to an "
     "irregular fruiting year is the constraint the notes supply. The count of 51 birds states how "
     "bad the position had become rather than naming an obstacle to putting it right."),

 syn("R3",
     ["Before 1805 ships' logs described the wind in whatever words each captain chose.",
      "Francis Beaufort defined thirteen numbered forces.",
      "Each force was defined by the sail a full-rigged ship could carry in it, not by a measured speed.",
      "The scale was made compulsory in Royal Navy logs in 1838.",
      "Speeds in miles per hour were attached to the forces only in the twentieth century."],
     "explain how the scale made log entries comparable between one ship and another.",
     ["Francis Beaufort defined thirteen numbered forces, and the scale became compulsory in Royal Navy logs in 1838.",
      "By defining each force by the sail a full-rigged ship could carry in it, the scale replaced each captain's private wording with a standard that any other captain could read.",
      "Speeds in miles per hour were attached to the forces only in the twentieth century.",
      "Before 1805 ships' logs described the wind in whatever words each captain chose."],
     "B",
     "The goal is comparability, so the answer has to pair the shared definition with the private "
     "wording it displaced, which only one option does. The note about miles per hour describes a "
     "later addition and says nothing about how entries were made comparable."),

 syn("R4",
     ["Candidates for the Chinese civil service sat written examinations on the classics.",
      "Papers were recopied by clerks so that examiners could not recognise a hand.",
      "Names were replaced by numbers before any paper was marked.",
      "Candidates were searched and then sealed into individual cells for up to three days.",
      "Success rates at the highest level fell below one per cent in some years."],
     "explain the measures taken to keep the marking impartial.",
     ["Candidates sat written examinations on the classics and were sealed into individual cells for up to three days.",
      "Success rates at the highest level fell below one per cent in some years.",
      "Papers were recopied by clerks and names replaced by numbers, so that an examiner could recognise neither the handwriting nor the candidate.",
      "Candidates were searched before they entered the examination cells."],
     "C",
     "The goal is impartial marking, and only the option pairing the recopying with the numbering "
     "explains how an examiner was kept from telling whose paper he was reading. Searching a "
     "candidate prevents cheating by the candidate rather than partiality by the marker."),

 syn("R5",
     ["Cornish mines burned coal shipped in from Wales, so fuel was their largest running cost.",
      "From 1811 a monthly report listed each engine's duty: pounds of water raised one foot per bushel of coal.",
      "The reports named the engine, the mine and the engineer responsible.",
      "Average reported duty roughly trebled between 1815 and 1840.",
      "Engineers copied features from whichever engine stood at the head of the list."],
     "explain how the published reports contributed to the improvement in duty.",
     ["Cornish mines burned coal shipped in from Wales, so fuel was their largest running cost.",
      "Average reported duty roughly trebled between 1815 and 1840.",
      "Because the monthly reports ranked every named engine by the water it raised per bushel of coal, engineers could see which engine was doing best and copy its features.",
      "From 1811 a monthly report listed each engine's duty in pounds of water raised one foot per bushel of coal."],
     "C",
     "The goal asks how publication produced the improvement, so the answer has to connect the "
     "ranking of named engines with engineers copying whichever stood highest. Stating that duty "
     "trebled reports the result without saying what the reports had to do with it."),

 syn("R6",
     ["A throat singer sounds a low drone and a whistling melody at the same time.",
      "The melody is made of overtones already present in the drone, not of a second note.",
      "Changing the shape of the mouth and tongue strengthens one overtone and damps the rest.",
      "The styles are named for the herding landscape: rivers, wind, animals.",
      "Herders sing while riding, without any accompaniment."],
     "explain how a single voice produces two parts at once.",
     ["A throat singer sounds a low drone and a whistling melody at the same time.",
      "By reshaping the mouth and tongue the singer strengthens one of the overtones already contained in the drone and damps the others, so the melody is drawn out of the drone rather than sung separately.",
      "The styles are named for the rivers, wind and animals of the herding landscape.",
      "Herders sing while riding, without any accompaniment."],
     "B",
     "The goal asks for the mechanism, and only the option identifying the melody as overtones "
     "selected from the drone by the shape of the mouth explains how one voice yields two parts. "
     "Saying that the singer produces a drone and a melody at once restates the puzzle instead of "
     "accounting for it."),

 syn("R7",
     ["Coelacanths were known only as fossils and were thought to have died out 66 million years ago.",
      "In December 1938 a trawler landed a large blue fish off East London, South Africa.",
      "Marjorie Courtenay-Latimer, curator of a local museum, kept the specimen and sketched it.",
      "The coelacanth's nearest living relatives are lungfish and four-limbed vertebrates, not most other fish.",
      "A second population was found off Indonesia in 1997."],
     "explain why the specimen landed in 1938 was significant.",
     ["In December 1938 a trawler landed a large blue fish off East London, South Africa, and a local curator kept it and sketched it.",
      "A second population of coelacanths was found off Indonesia in 1997.",
      "The fish landed in 1938 belonged to a group known only from fossils and believed to have died out 66 million years ago, so a living specimen overturned that belief.",
      "Marjorie Courtenay-Latimer was the curator of a local museum."],
     "C",
     "The goal is the significance of the catch, and only the option setting a living fish against "
     "a group believed extinct for 66 million years supplies it. The Indonesian population turned "
     "up almost sixty years later and cannot explain why the first specimen mattered."),

 syn("R8",
     ["Diphtheria appeared in Nome, Alaska, in January 1925.",
      "The port was frozen in and the territory's only aircraft had been dismantled for the winter.",
      "Serum was carried 1,085 km from Nenana by twenty dog teams working in relay.",
      "The relay took five and a half days in temperatures near minus 50 degrees Celsius.",
      "The last driver arrived with the serum frozen but still usable."],
     "explain why dog teams were used to deliver the serum.",
     ["Serum was carried 1,085 km from Nenana to Nome by twenty dog teams working in relay.",
      "With the port frozen in and the territory's only aircraft dismantled for the winter, dog teams were the sole means left of getting serum to Nome.",
      "The relay took five and a half days in temperatures near minus 50 degrees Celsius.",
      "Diphtheria appeared in Nome, Alaska, in January 1925."],
     "B",
     "The goal asks why dogs were used, and only the option naming the frozen port and the "
     "dismantled aircraft rules out the alternatives and leaves the teams as what remained. Stating "
     "the distance and the number of teams describes what was done without saying why nothing else "
     "would serve."),

 syn("R9",
     ["In 1927 Thomas Parnell heated a sample of pitch and poured it into a sealed funnel.",
      "Pitch shatters like glass when it is struck with a hammer.",
      "The funnel was unsealed in 1930 and the pitch began to flow.",
      "Nine drops have fallen since, the most recent in 2014.",
      "The experiment shows the pitch to be a fluid roughly 100 billion times more viscous than water."],
     "explain what the experiment demonstrates about the pitch.",
     ["In 1927 Thomas Parnell heated a sample of pitch and poured it into a sealed funnel, which was unsealed in 1930.",
      "Nine drops of pitch have fallen from the funnel since 1930, the most recent of them in 2014.",
      "Although pitch shatters like glass when struck, the drops falling from the funnel since 1930 show it to be a fluid, roughly 100 billion times more viscous than water.",
      "Pitch shatters like glass when it is struck with a hammer."],
     "C",
     "The goal asks what the experiment demonstrates, so the answer has to set the brittle behaviour "
     "against the slow flow and name the conclusion drawn from it. Counting the drops reports the "
     "observation without stating what it establishes about the material."),
]

DROPPED = {}
