#!/usr/bin/env python3
"""
Reading & Writing authored for Test 21.

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
items whose options are genuinely words ("was" / "were", "its" / "their") stay
as words, which is also how the real test presents them.

Topics were screened programmatically against content-pool/rw_authored_corpus
.json - 1,052 passages banked or authored across Tests 1-18 - with a keyword
check and a shared-5-gram / Jaccard check, using check_originality.py in this
directory. Test 21 was assigned fifteen subject territories to keep it clear of
the sibling Test 19 and Test 20 builds: viticulture and wine chemistry; silk
and sericulture; wheelwrighting and road vehicles; observatories and optical
instrument making; photography and imaging chemistry; meteorology and
forecasting; Roman law; cephalopod cognition; crystallography and X-ray
diffraction; folk song collecting; currency, coinage and banking; wildfire
ecology; knot theory and graph theory; penguins and seabird colonies; and
plant hormones and tropisms.

Candidates that collided with an existing passage were dropped before drafting
rather than paraphrased around: the cyanotype (Test 13 has Anna Atkins), the
Beaufort wind scale (Test 13), cuttlefish camouflage in both its texture and
its colour-blind forms (Tests 13 and 15), the emperor penguin huddle (Test 8),
seabird guano as fertiliser (Test 10), double-entry bookkeeping (Test 14),
serotinous cones in lodgepole pine (Test 11), fire-scar and tree-ring dating
(Tests 9 and 17), the fire lookout's triangulation (Test 14), shortest-path
networks (Test 11's slime mould), the camera obscura and the camera lucida
(Tests 11 and 15), segmented telescope mirrors (Test 10), octopus tool use
(Test 8), and ballad variants collected in one valley (Test 13). Two
near-misses were deliberately steered: silk is written as the insect, the
reeling and the trade, never as dyeing or weaving (Test 16 holds textiles and
dyes), and observatories are written as optical instruments, domes and
mountings, never as radio astronomy (Test 17).

Block counts (fixed by the assembler's quota, 3 modules x 27):
    Words in Context 15, Text Structure and Purpose 6,
    Central Ideas and Details 6, Command of Evidence 9, Inferences 6,
    Boundaries 12, Form, Structure, and Sense 9, Transitions 9,
    Rhetorical Synthesis 9                                        = 81
"""

SOURCE = "AUTHORED-T21"
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


# The CLAUDE.md table style block, emitted as real <table> markup. Data-based
# Command of Evidence items get a genuine table; a prose description of a graph
# is never acceptable, since no image can be produced for this pool.
_TSTY = "border-collapse:collapse;margin:0.75rem 0;"
_TH = "border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;"
_TD = "border:1px solid #D9DEE5;padding:0.35rem 0.6rem;"


def table(headers, rows):
    head = "".join(f'<th style="{_TH}">{h}</th>' for h in headers)
    body = "".join(
        "<tr>" + "".join(f'<td style="{_TD}">{c}</td>' for c in r) + "</tr>"
        for r in rows)
    return f'<table style="{_TSTY}"><tr>{head}</tr>{body}</table>'


QUESTIONS = [

 # ------------------------------------------------------ Words in Context (15)
 wic("W1",
     "The root louse that reached Europe in the 1860s killed vines by the hectare, and no spray "
     "applied to a leaf ever reached it underground. American vines, which had evolved alongside "
     "the insect, lost nothing to it but a few fine roots. Growers eventually replanted whole "
     "regions by grafting European fruiting wood onto American stocks, so that almost every vine "
     "now standing in Bordeaux is _____: French above the ground and American below it.",
     ["composite", "uniform", "untended", "provisional"], "A",
     "The colon spells out one plant made of two different origins joined at the graft, and the "
     "blank has to name that doubleness. The 'uniform' option asserts the opposite of the division "
     "the rest of the sentence sets out."),

 wic("W2",
     "Four thousand years of selection have left the domesticated silkmoth unable to live outside a "
     "rearing house. The adult's wings are far too small to carry its body, the larvae will not "
     "crawl in search of food when a mulberry branch is taken away, and the pale colouring that "
     "makes a cocoon easy to sort would betray the insect to any bird. The moth is now wholly _____ "
     "the people who keep it.",
     ["dependent on", "indifferent to", "hostile to", "distinguishable from"], "A",
     "Every detail in the list names something the moth can no longer do for itself, so the blank "
     "must state that its survival rests with its keepers. The 'indifferent to' option treats the "
     "relationship as a matter of no consequence, which the catalogue of lost capacities rules "
     "out."),

 wic("W3",
     "A cart wheel is not a flat disc. Its spokes lean outward from the hub so that the rim stands "
     "in a shallow cone, and to anyone who has not built one the wheel looks as though it has "
     "already begun to collapse. The shape is in fact _____: a loaded cart rocks from side to side "
     "on rough ground, and the cone braces the wheel against the thrust that the rocking sends "
     "along the axle.",
     ["deliberate", "decorative", "temporary", "unavoidable"], "A",
     "The colon supplies the reason the cone is built into the wheel, so the blank marks the shape "
     "as intended rather than as a defect. The 'unavoidable' option would make the cone something "
     "the wheelwright could not help, whereas the passage has him bracing the wheel on purpose."),

 wic("W4",
     "A larger mirror gathers more light, but that light has already crossed several miles of moving "
     "air, and the motion smears a star into a trembling disc. No further polishing of the glass "
     "improves matters. Committees that had once chosen a site by the convenience of the nearest "
     "railway began instead to send an assistant to camp on a ridge for a season with a small "
     "telescope, judging the steadiness of the air before any foundation was laid. The ground had "
     "come to seem no less _____ than the instrument.",
     ["consequential", "expensive", "accessible", "familiar"], "A",
     "The passage has the air, not the optics, setting the limit on what a telescope can show, and "
     "the closing sentence puts the site on a level with the instrument in deciding results. The "
     "'accessible' option names the very criterion the committees are said to have abandoned."),

 wic("W5",
     "A plate taken out of the camera looks exactly as it did before the shutter opened. Light has "
     "altered a few atoms in each grain of silver halide it struck, and nothing more. Development "
     "multiplies that alteration many million times, turning a whole grain to metallic silver "
     "wherever the change had begun, and the picture appears in the dish. Until that moment the "
     "photographer is working on a record that is entirely _____.",
     ["invisible", "permanent", "accidental", "borrowed"], "A",
     "The passage states that the exposed plate looks unchanged and that the picture appears only "
     "in the developing dish, so nothing can be seen before then. The 'permanent' option speaks to "
     "how long an image lasts, a question the text never raises, and would not explain why there is "
     "nothing to look at."),

 wic("W6",
     "A forecast produced from one set of starting conditions yields a single future and no "
     "indication of how firmly it should be held. Because the instruments that measure the "
     "atmosphere always leave small errors behind, forecasters now run the same model fifty times "
     "from fifty slightly different starting states. Where the fifty runs still agree on the fifth "
     "day, the forecast is worth acting on; where they have diverged by the third, it is not. The "
     "spread among the runs makes the confidence of a forecast _____.",
     ["explicit", "uniform", "unnecessary", "temporary"], "A",
     "The passage contrasts agreement among the runs with divergence and treats that difference as "
     "what tells a reader how far to trust the forecast, so the spread puts the confidence on the "
     "record. The 'uniform' option would give every forecast the same confidence, which is the "
     "opposite of a spread that varies from case to case."),

 wic("W7",
     "A praetor held office for a single year and published at the start of it the remedies he "
     "undertook to grant. He was not bound by anything his predecessor had written, but in practice "
     "he reissued that document and added to it, since litigants expected a form of action once "
     "granted to be available again. The edict therefore grew _____, clause upon clause, until "
     "Hadrian had the accumulated text fixed and closed.",
     ["incrementally", "abruptly", "erratically", "privately"], "A",
     "Each praetor is said to keep his predecessor's text and add to it, and the image of clause "
     "upon clause describes growth by small additions. The 'abruptly' option would suit a document "
     "rewritten at a stroke, which is precisely what the passage says did not happen."),

 wic("W8",
     "Rather more than half the neurons of an octopus lie in its eight arms and not in the brain "
     "between its eyes. An arm separated from the body will still recoil from an irritant and will "
     "still pass a piece of food along its suckers towards a mouth that is no longer there. In "
     "intact animals the brain appears to name a target and to leave the arm to find its own way to "
     "it. Control of the limbs is therefore _____.",
     ["devolved", "centralised", "interrupted", "inherited"], "A",
     "The passage puts most of the animal's nervous tissue in the arms and has the brain issue only "
     "a broad instruction, so the working decisions are taken away from the centre. The "
     "'centralised' option states the arrangement the text is at pains to deny."),

 wic("W9",
     "A crystalline solid ground to a fine powder presents its planes of atoms in every orientation "
     "at once, and a beam of X-rays passed through it emerges as a set of concentric rings. The "
     "spacing of those rings and their relative strength depend on the arrangement of the atoms and "
     "on nothing else, so two samples of one compound give the same set whatever their history. A "
     "chemist matching an unknown against a catalogue of published patterns therefore treats the "
     "rings as _____.",
     ["diagnostic", "approximate", "provisional", "ornamental"], "A",
     "The passage says the pattern depends on the atomic arrangement alone and repeats for every "
     "sample of a compound, which is what lets it settle an identification. The 'approximate' "
     "option would leave the match uncertain, whereas the text stresses that the pattern does not "
     "vary."),

 wic("W10",
     "A collector who worked with a notebook wrote down what a singer sang in the staff notation he "
     "had been taught at school. That notation has no sign for a note sung a little below the third "
     "of the scale, none for a line ended by letting the voice fall away, and none for a beat held "
     "a fraction longer than the bar allows. Whatever he could not spell simply left the record. "
     "His transcriptions are therefore _____ rather than false.",
     ["partial", "illegible", "anonymous", "disputed"], "A",
     "The passage lists features of the singing that the notation had no means of representing and "
     "says they dropped out, which leaves the record incomplete without making it wrong. The "
     "'illegible' option concerns whether the writing can be read, which the text never puts in "
     "question."),

 wic("W11",
     "A mint that put less silver into a penny while leaving its face value untouched kept the "
     "difference, and a treasury short of money found the temptation hard to resist. Merchants, "
     "however, weighed coin as readily as they counted it. Within a season of a debasement the old "
     "heavy pennies had gone into hoards or out of the country, prices quoted in the new money had "
     "risen to match its metal, and the crown's gain had proved _____.",
     ["short-lived", "imaginary", "unlawful", "unpopular"], "A",
     "The gain is described as real at the moment of striking and then eaten away within a season "
     "by hoarding and rising prices, so the blank marks it as temporary. The 'imaginary' option "
     "denies there was ever any gain, which the opening sentence establishes."),

 wic("W12",
     "Before 1910 the pine forests of the interior West burned lightly every ten or fifteen years, "
     "and the flames consumed the litter and the seedlings without reaching the crowns of the older "
     "trees. Eighty years of prompt suppression allowed both to accumulate, until the small trees "
     "formed a continuous ladder from the ground to the canopy. The fires that eventually arrive "
     "are not the fires that were stopped. Suppression did not remove the hazard; it _____ it.",
     ["compounded", "measured", "halved", "concealed"], "A",
     "Fuel is described as building through the decades of suppression until the ladder reaches the "
     "canopy, so the practice made the eventual fire worse rather than smaller. The 'concealed' "
     "option would leave the hazard unchanged and merely hidden, which does not account for the "
     "ladder the passage describes."),

 meaning("W13",
     "A knot is studied as a diagram: a closed loop drawn on paper with a mark at each crossing to "
     "show which strand passes over. Two diagrams stand for the same knot when one can be turned "
     "into the other by a sequence of three permitted alterations, which twist a loop, slide one "
     "strand across another, or lift a strand past a crossing. Anything done to a diagram outside "
     "that list changes the knot and not merely the picture, so every step of a proof is written as "
     "a <u>move</u> of one of the three kinds.",
     "move",
     ["A change of position from one place to another.",
      "One of a fixed set of permitted alterations that leaves the knot itself unchanged.",
      "A calculated action taken in order to achieve an aim.",
      "A player's turn in a game played on a board."],
     "B",
     "The passage defines three permitted alterations and then applies the word to a step of one of "
     "those kinds, so it names a licensed operation rather than any change at all. The everyday "
     "sense of a change of position would cover alterations the text has just excluded as changing "
     "the knot."),

 meaning("W14",
     "A colony's size in any season reflects two quantities that are counted separately. Adults "
     "that bred the year before return to the same ledges and are recorded as such. Birds hatched "
     "three or four seasons earlier arrive to breed for the first time, take a place at the edge of "
     "the colony and are entered under a different heading, since a colony losing adults faster "
     "than it gains these newcomers is in decline however many eggs it laid. Long runs of ringing "
     "data are kept chiefly in order to measure <u>recruitment</u>.",
     "recruitment",
     ["The enlistment of new members into an armed force.",
      "The entry of young birds into the breeding population of a colony.",
      "The hiring of staff to fill posts in an organisation.",
      "A fresh supply of stores brought to a remote settlement."],
     "B",
     "The passage separates returning adults from birds arriving to breed for the first time and "
     "applies the word to the second group, so it names their entry into the breeding population. "
     "The enlistment sense belongs to armies and answers to nothing in a count of birds hatched "
     "three seasons earlier."),

 meaning("W15",
     "A lettuce is harvested for its leaves, and a lettuce that has begun to flower is worth "
     "nothing: the stem lengthens, the rosette opens and the remaining leaves turn bitter within "
     "days. The change is set off by gibberellin, which the plant makes in quantity as the nights "
     "shorten and the temperature rises. Breeders select for varieties slow to produce it, and "
     "growers sow early so that the crop is cut before the weather that makes a plant <u>bolt</u> "
     "arrives.",
     "bolt",
     ["To fasten two components together with a threaded pin.",
      "To run to flower and seed before the crop can be harvested.",
      "To swallow food hurriedly and without chewing it.",
      "To break away suddenly and run off."],
     "B",
     "The passage describes the stem lengthening and the plant flowering ahead of the harvest and "
     "then names that event, so the word refers to premature flowering. The sense of breaking away "
     "and running belongs to a startled animal and cannot be brought on by gibberellin in a "
     "lettuce."),

 # --------------------------------------------- Text Structure and Purpose (6)
 tsp("T1",
     "Collodion is poured onto a glass plate in the dark, sensitised in a bath of silver nitrate, "
     "exposed while the surface is still tacky and developed before the film can dry, because a "
     "dry collodion plate loses almost all its sensitivity. The whole sequence takes about ten "
     "minutes. A photographer who wanted a view of a mountain therefore took the darkroom to the "
     "mountain: a tent, a water supply, a chest of chemicals and a cart to carry them, so that the "
     "plate could be coated within sight of the subject and developed a few minutes after the "
     "exposure.",
     "Which choice best states the main purpose of the text?",
     ["To explain a property of a process and the working arrangements it imposed on those who used it.",
      "To argue that collodion plates produced better pictures than the plates that replaced them.",
      "To describe the chemical reaction by which silver nitrate is reduced to metallic silver.",
      "To trace the career of a particular nineteenth-century landscape photographer."],
     "A",
     "The text sets out the requirement that the plate be coated, exposed and developed wet, then "
     "shows what a photographer had to carry in order to meet it, which ties a property of the "
     "process to the practice it forced. The chemistry of the reduction is never described; only "
     "the order of the steps is given."),

 tsp("T2",
     "X-rays scattered by a crystal leave it in almost every direction, and the scattered waves "
     "cancel one another out except along a few sharp beams. <u>W. L. Bragg showed that such a beam "
     "appears only where the extra distance travelled by a wave turned back from one plane of "
     "atoms, rather than from the plane above it, comes to a whole number of wavelengths.</u> The "
     "relation contains the wavelength, the angle at which the beam leaves and the spacing between "
     "the planes. Two of the three can be measured directly, and the spacing follows.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It states the condition that makes the measurement described at the end of the text possible.",
      "It explains why X-rays are scattered by the electrons of an atom at all.",
      "It questions whether the sharp beams can be located accurately enough to be useful.",
      "It describes the apparatus with which the scattered beams are recorded."],
     "A",
     "The sentence supplies the whole-wavelength condition, and the closing lines use exactly the "
     "three quantities it relates in order to obtain the spacing, so it grounds that calculation. "
     "Why X-rays are scattered in the first place is assumed throughout and nowhere explained."),

 tsp("T3",
     "By the sixth century the writings of the classical jurists ran to something like two thousand "
     "volumes, many of them contradicting one another and some surviving only in quotation. "
     "Justinian appointed a commission to reduce the whole of it to one work. The compilers cut "
     "what had become obsolete, altered the wording where two opinions clashed, and arranged what "
     "remained by subject, attributing each extract to the jurist who wrote it. The Digest that "
     "resulted is a fiftieth of the bulk it was drawn from and reads as though the law had never "
     "been in dispute.",
     "Which choice best describes the overall structure of the text?",
     ["It describes a body of material and the difficulties it presented, then explains how a compilation altered it and what the result is like.",
      "It traces the careers of the classical jurists whose writings were eventually compiled.",
      "It argues that the compilers should have preserved the disagreements they removed.",
      "It compares Roman law with the legal systems that came after it."],
     "A",
     "The text opens on the bulk and the contradictions of the juristic writings, describes the "
     "cutting, altering and rearranging done by the commission, and closes on the character of the "
     "finished book. Whether the removals were a loss is a judgement the passage never delivers."),

 tsp("T4",
     "A gannet enters the water from thirty metres up at something near a hundred kilometres an "
     "hour, and an impact of that kind would drive water into the skull of most birds. <u>The "
     "gannet has no external nostrils at all, and a network of air sacs lies between the skin of "
     "its breast and the muscle beneath, taking up the blow much as packing takes up the shock to a "
     "crate.</u> A bird may make several hundred such dives in a day's fishing and shows no injury "
     "from any of them.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It identifies the features that account for the outcome reported in the final sentence.",
      "It explains how the bird judges the depth at which a fish is swimming.",
      "It compares the gannet's diving speed with the speeds reached by other seabirds.",
      "It concedes that the diving method carries a risk the bird cannot avoid."],
     "A",
     "The sentence names the closed nostrils and the air sacs, and the closing sentence reports "
     "hundreds of dives without injury, which those two features are what make possible. How a "
     "swimming fish is located is a separate question the passage never takes up."),

 tsp("T5",
     "The town of K&ouml;nigsberg was built on both banks of a river and on two islands, and seven "
     "bridges connected the four pieces of ground. Residents asked whether a walk could be made "
     "that crossed every bridge exactly once. Euler observed that what happened inside any one "
     "piece of ground made no difference to the question, and that only the number of bridges "
     "meeting it mattered. Reduced to four points and seven lines, the problem answered itself: a "
     "walk must enter and leave every point it neither begins nor ends at, and all four points had "
     "an odd number of bridges.",
     "Which choice best states the main purpose of the text?",
     ["To describe how discarding most of the features of a physical problem made it solvable.",
      "To explain why seven bridges rather than some other number were built at K&ouml;nigsberg.",
      "To argue that the question the residents asked has never been satisfactorily answered.",
      "To recount the history of a European town and its river crossings."],
     "A",
     "The text moves from a town with bridges to four points and seven lines and shows the answer "
     "following once the geography has been thrown away, which makes that abstraction its subject. "
     "The closing sentence supplies a definite answer, so the question is not left unresolved."),

 tsp("T6",
     "A bottle described as corked has not oxidised and has not turned to vinegar. It carries a "
     "trace of trichloroanisole, a compound formed when moulds in the bark act on chlorinated "
     "residues left there by bleaching, and the human nose detects it at a few parts in a million "
     "million, well below the level at which any instrument in ordinary cellar use will report it. "
     "The fault lies in the closure and not in the wine, which is why a second bottle from the same "
     "case is very often sound.",
     "Which choice best states the main purpose of the text?",
     ["To identify the cause of a particular fault in bottled wine and to place it in the closure rather than the wine.",
      "To argue that screw caps ought to replace cork in the bottling of wine.",
      "To describe the process by which cork bark is harvested and prepared for use.",
      "To explain why some drinkers detect faint smells that others cannot."],
     "A",
     "The text names the compound responsible, explains where it forms and closes by locating the "
     "defect in the stopper rather than in the contents of the bottle. No alternative closure is "
     "proposed anywhere in the passage."),

 # ---------------------------------------------- Central Ideas and Details (6)
 cid("C1",
     "A silkworm spins its cocoon from a single filament about a kilometre long, laid down in a "
     "figure of eight until the insect is enclosed. That filament is far too fine to be woven on "
     "its own. A reeler softens the gum in hot water, catches the loose ends of five or eight "
     "cocoons at once and draws them off together, the gum binding them into one thread as it "
     "dries. The result is not spun from short lengths in the manner of wool or cotton but "
     "assembled from filaments that were never cut.",
     "Which choice best states the main idea of the text?",
     ["Silk thread is built by combining several unbroken filaments rather than by spinning short fibres together.",
      "A cocoon must be softened in hot water before a reeler can handle it.",
      "Silk is finer than either wool or cotton and is for that reason harder to weave.",
      "A single silkworm cocoon yields a filament roughly a kilometre in length."],
     "A",
     "Every sentence works towards the closing contrast between a thread assembled from uncut "
     "filaments and one spun from short lengths, which is the point the passage exists to make. The "
     "kilometre of filament is a fact the argument uses along the way rather than its conclusion."),

 cid("C2",
     "A barometer tells an observer what the pressure is where he stands, and a falling glass gave "
     "a captain some warning of a storm already close. What no observer could obtain was the state "
     "of the atmosphere across a whole country at one moment, since a letter reporting yesterday's "
     "wind at a distant station arrived days after it could be of use. The electric telegraph "
     "removed the delay. From 1849 stations wired their readings to a central office, a clerk "
     "entered them on a blank map, and the shape of a storm could be seen for the first time.",
     "Which choice best states the main idea of the text?",
     ["Weather could be mapped across a region only once reports were able to travel faster than the weather itself.",
      "The barometer was of little use to sailors until the telegraph was invented.",
      "Storms came to be understood by clerks in a central office rather than by observers in the field.",
      "Nineteenth-century observers recorded atmospheric pressure more accurately than their predecessors had."],
     "A",
     "The passage sets a single observer's reading against the need for reports from everywhere at "
     "once and credits the telegraph with removing the delay that had made a map impossible. The "
     "barometer is said to have given a captain real warning, so the text does not dismiss it as "
     "useless."),

 cid("C3",
     "Fire kills the visible part of a mallee eucalypt and leaves the plant alive. Beneath the soil "
     "sits a woody swelling formed in the seedling's first years and packed with dormant buds and "
     "stored starch, and the heat that removes the stems does not reach it. Within weeks of a fire "
     "the swelling sends up a dozen new shoots at once, drawing on reserves the burnt canopy had "
     "laid down. A stand that appears to have been destroyed may consist of individuals that were "
     "already old when the fire passed through it.",
     "Which choice best states the main idea of the text?",
     ["A mallee survives fire in a buried structure holding both buds and food, so a stand regrows from established plants rather than from seed.",
      "Fire removes the canopy of a mallee eucalypt but leaves the surrounding ground unharmed.",
      "The woody swelling of a mallee is formed during the first years of the seedling's life.",
      "Stands of mallee recover from fire more quickly than other kinds of woodland do."],
     "A",
     "The passage traces the recovery to a buried swelling holding buds and starch and closes by "
     "saying the regrown plants are the old ones, which is the claim all the details support. When "
     "the swelling forms is a supporting fact rather than the point being made."),

 cid("C4",
     "A hammered coin has an irregular edge, and a sliver pared from it leaves nothing behind to "
     "show what has been taken. Clipping was accordingly common, and was punished savagely without "
     "becoming rare. The screw press introduced in the seventeenth century struck coins of even "
     "shape and allowed a legend or a pattern of grooves to be impressed around the rim. A clipped "
     "coin now announced itself: the missing grooves could be seen across a counter, and the coin "
     "would not pass at its face value.",
     "Which choice best states the main idea of the text?",
     ["Machine striking discouraged clipping by making interference with a coin's edge obvious to anyone handling it.",
      "Clipping came to be punished more severely after the screw press was introduced.",
      "Hammered coins were struck less accurately than coins made by machine.",
      "The screw press allowed mints to produce coins in far greater numbers than before."],
     "A",
     "The passage contrasts a pared edge that left no trace with a grooved rim whose absence could "
     "be seen across a counter, so the deterrent lies in the visibility of the theft. Greater "
     "output is a property of the press that the text never mentions."),

 cid("C5",
     "Ethylene is a gas, and a ripening apple gives it off. The gas spreads through the air of a "
     "closed store and is taken up by the fruit around it, where it begins the same softening and "
     "the same conversion of starch to sugar that produced it. A single over-ripe apple will "
     "therefore bring a whole crate forward by several days. Commercial stores hold fruit in air "
     "from which the gas is continuously scrubbed, and bring a consignment on by admitting ethylene "
     "deliberately when the market calls for ripe fruit.",
     "Which choice best states the main idea of the text?",
     ["Because the ripening signal travels as a gas between fruit, ripening can be both spread by one fruit and controlled by a store.",
      "An over-ripe apple gives off more ethylene than a fruit picked before it is ready.",
      "Ethylene converts the starch held in a fruit into sugar and softens its flesh.",
      "Commercial fruit stores keep their crops in air from which gases have been removed."],
     "A",
     "The passage builds from a signal passing through the air between fruit to both of the "
     "consequences a store depends on, spreading ripeness and withholding it, which is what ties "
     "the details together. The conversion of starch to sugar is one of the effects named along the "
     "way rather than the point being made."),

 cid("C6",
     "A star crosses the sky because the Earth turns, and a telescope on an ordinary tripod must be "
     "pushed in two directions at once to follow it. The equatorial mounting sets one of its axes "
     "parallel to the Earth's own, so that the whole apparent motion of the sky becomes a rotation "
     "about that single axis. A clock turning it once a day holds a star still in the field, and "
     "the second axis is touched only when the observer moves to a new object. Photography of any "
     "length became possible on such a mounting and on no other.",
     "Which choice best states the main idea of the text?",
     ["Aligning one axis with the Earth's reduces the tracking of a star to a single steady motion that a clock can supply.",
      "A telescope on an ordinary tripod cannot be pointed accurately at a star.",
      "The rotation of the Earth is the reason stars appear to cross the sky at night.",
      "Long photographic exposures of the night sky were first attempted in the nineteenth century."],
     "A",
     "The passage sets the two simultaneous motions of a plain tripod against a mounting on which "
     "the sky's movement becomes one rotation, and everything that follows depends on that "
     "reduction. That the Earth's turning causes the apparent motion is the premise the passage "
     "starts from, not what it argues."),

 # ---------------------------------------------------- Command of Evidence (9)
 coe("E1",
     "A wheelwright in a Sussex village kept a daybook from 1878 until his shop closed, entering "
     "the work of each day alongside notes on the timber standing in his yard. Historian Marcus "
     "Ellery argues that the book treats the seasoning of the wood, rather than any operation at "
     "the bench, as the thing that decided whether a wheel would last.",
     "Which quotation from the daybook most effectively illustrates Ellery's claim?",
     ["&ldquo;Felloes cut from the elm that came in at Michaelmas four years since. It has stood through four summers and will not stir now, and a wheel of it will outlast the cart it is put under.&rdquo;",
      "&ldquo;Six spokes driven before dinner, the mortises cleaned out with the same chisel my father used.&rdquo;",
      "&ldquo;The smith set the tyre this morning and we cooled it at the trough, as neat a shrink as I have seen him make.&rdquo;",
      "&ldquo;Two wheels ordered for the miller, to be ready by Lady Day, the price agreed at thirty shillings the pair.&rdquo;"],
     "A",
     "The claim is that seasoning decided how long a wheel lasted, and only the entry crediting four "
     "summers of standing timber with a wheel that outlasts the cart makes that connection. The "
     "entry praising the shrinking of the tyre singles out an operation at the bench, which is what "
     "the argument sets aside."),

 coe("E2",
     "An assistant at a hilltop observatory kept the nightly log for eleven years, recording the "
     "instrument used, the objects observed and the state of the air. Historian Nuria Falc&oacute; "
     "argues that the log is organised around the atmosphere rather than around the observing "
     "programme, treating a night's work as something the air granted or refused.",
     "Which quotation from the log most effectively illustrates Falc&oacute;'s claim?",
     ["&ldquo;Sky clear from ten o'clock, but the disc boiled at every magnification above two hundred. Nothing attempted, and the sheets for the double stars laid by until the air will carry them.&rdquo;",
      "&ldquo;The great refractor was used throughout, the twelve-inch being still without its new eyepiece.&rdquo;",
      "&ldquo;Observations of the fourth satellite continued, and the times of the eclipses entered in the usual register.&rdquo;",
      "&ldquo;A visitor from the county society was shown the instrument between eleven and midnight.&rdquo;"],
     "A",
     "The claim concerns a log built around what the air allowed, and only the entry abandoning a "
     "clear night because the image boiled, and postponing the programme until the air improves, "
     "shows work being granted or refused in that way. The entry recording which instrument was "
     "used names equipment without any reference to the state of the atmosphere."),

 coe("E3",
     "A collector who spent four summers in the Hebrides between 1906 and 1910 kept a diary "
     "alongside her notebooks of tunes. Ethnomusicologist Jonah Bercovitch argues that the diary "
     "treats the singers as the authorities on their own repertoire rather than as sources whose "
     "performances required correction by the person writing them down.",
     "Which quotation from the diary most effectively illustrates Bercovitch's claim?",
     ["&ldquo;Mrs MacAulay sang the second verse to a different close, and when I asked which was right she said both were, and that her mother had sung them so. I have set down the two and will not choose between them.&rdquo;",
      "&ldquo;The weather kept us indoors for three days, and I copied out the tunes taken at Barra in a fair hand.&rdquo;",
      "&ldquo;Eleven songs taken this week, of which four are variants of tunes already in the notebook.&rdquo;",
      "&ldquo;The singer's voice is low and carries little, and I sat close by the fire in order to hear the words at all.&rdquo;"],
     "A",
     "The claim is that the singers were treated as the authority, and only the entry accepting a "
     "singer's ruling that both endings are right, and declining to choose between them, shows that "
     "deference. Counting the week's variants records what was collected without indicating who "
     "decided what was correct."),

 coe("E4",
     "Forecast accuracy at five days improved steadily from the 1980s onward, and two things "
     "changed across the same period: the models were run on far finer grids, and satellites began "
     "to supply temperature and humidity through the depth of the atmosphere over the oceans, where "
     "almost no measurements had existed. Meteorologist Ola Tveit argues that the improvement is "
     "owed chiefly to the new observations rather than to the finer grids.",
     "Which finding, if true, would most directly support Tveit's argument?",
     ["When the modern model was rerun at its finest grid using only the observations available in 1980, its five-day forecasts were no better than those actually issued in 1980, while the 1980 model rerun with modern satellite data improved sharply.",
      "The finest grids in use today divide the atmosphere into cells about a tenth the width of those used in 1980.",
      "Satellites now supply the great majority of the observations that enter a global forecast model.",
      "Forecasts issued for two days ahead improved less across the period than forecasts issued for five days ahead."],
     "A",
     "Exchanging the two ingredients one at a time separates them, and the result described puts "
     "the whole gain on the observations while the finer grid alone delivers none. That satellites "
     "now supply most of the data reports their quantity and leaves open whether they, rather than "
     "resolution, produced the improvement."),

 coe("E5",
     "A cuttlefish offered a crab in the morning will normally eat it. In one laboratory the "
     "animals were also given a shrimp, which they prefer, every evening at a fixed hour. After "
     "some days most of them stopped eating the morning crab. Behavioural ecologist Priya Raman "
     "argues that the animals were holding out for the evening shrimp rather than losing their "
     "appetite for crab.",
     "Which finding, if true, would most directly support Raman's argument?",
     ["A second group given the shrimp at unpredictable hours went on eating the morning crab throughout, and the first group returned to eating it as soon as the evening shrimp was withdrawn.",
      "Cuttlefish in the wild take crabs less often than they take shrimp.",
      "The animals that stopped eating the morning crab grew no more slowly than those that ate it.",
      "Cuttlefish can be trained to approach a mark on the wall of a tank in exchange for food."],
     "A",
     "Making the evening shrimp unpredictable removes any reason to wait, and the animals go on "
     "eating the crab, which is what holding out predicts and what a simple loss of appetite for "
     "crab does not. A preference for shrimp in the wild would apply to both groups alike and "
     "cannot explain why only one of them changed."),

 coe("E6",
     "Seed of several South African shrubs lies in the soil for years and germinates in numbers "
     "only after a fire has passed over it. Two things a fire delivers might account for that: a "
     "brief pulse of heat through the top few centimetres of soil, and the smoke that soaks into "
     "the ground as it drifts. Botanist Thabo Nkosi argues that the cue is chemical rather than "
     "thermal.",
     "Which finding, if true, would most directly support Nkosi's argument?",
     ["Seed watered with smoke that had been bubbled through cold water germinated as freely as seed lifted from a burnt site, while seed heated in an oven to the temperatures a fire produces germinated no better than untreated seed.",
      "Fires in the region are most frequent at the end of a dry summer.",
      "The temperature a metre below the surface hardly changes while a fire passes overhead.",
      "Seedlings appearing after a fire face less competition than seedlings appearing in unburnt vegetation."],
     "A",
     "Applying smoke without heat and heat without smoke separates the two candidates, and "
     "germination follows the smoke alone. That deep soil stays cool shows only how far the heat "
     "reaches, not whether heat is the trigger for seed lying in the top few centimetres."),

 coe("E7",
     "Acid inherited from the grape gives a white wine its freshness, and a grape loses acid as it "
     "ripens. Four blocks of one variety, all picked at the same sugar level, were compared over a "
     "single season. Oenologist Ines Barreto argues that the acid a grape keeps depends on how cool "
     "its nights are rather than on how much sun the block receives."
     + table(["Block", "Mean night temperature during ripening (&deg;C)",
              "Direct sun (hours per day)", "Acidity at harvest (g/L)"],
             [["North ridge", "12", "8.5", "7.4"],
              ["Valley floor", "19", "8.4", "5.1"],
              ["Coastal terrace", "13", "6.9", "7.1"],
              ["Inland slope", "18", "7.0", "5.3"]]),
     "Which choice most effectively uses data from the table to support Barreto's argument?",
     ["The two blocks with the coolest nights, the north ridge at 12 &deg;C and the coastal terrace at 13 &deg;C, finished at 7.4 and 7.1 g/L, while the valley floor and the inland slope, at 19 &deg;C and 18 &deg;C, finished at 5.1 and 5.3 g/L, even though those pairs do not divide by hours of sun.",
      "The north ridge received 8.5 hours of direct sun a day, more than any other block, and finished at 7.4 g/L.",
      "The valley floor recorded the warmest nights, at 19 &deg;C, and the lowest acidity at harvest, 5.1 g/L.",
      "The coastal terrace received 6.9 hours of direct sun a day and finished at 7.1 g/L."],
     "A",
     "The argument sets one variable against the other, so it needs the blocks to sort by night "
     "temperature while the hours of sun fail to sort them, and only the response giving all four "
     "blocks on both measures shows that. Quoting the warmest block beside its lowest acidity gives "
     "one consistent pair and leaves the sunshine untested."),

 coe("E8",
     "Adults of this species carry food to the chick from open water, and a colony sits wherever "
     "there is bare rock to nest on. Four colonies on one coast were counted in the same season, "
     "and the distance each faced to open water was measured from the ice edge. Ecologist Bruno "
     "Salgado argues that the foraging distance a colony faces, rather than the number of birds in "
     "it, governs how many chicks it raises."
     + table(["Colony", "Breeding pairs", "Distance to open water (km)",
              "Chicks fledged per pair"],
             [["Cape Rennick", "3,200", "12", "0.71"],
              ["Ilse Point", "21,500", "14", "0.68"],
              ["Drift Bay", "4,100", "58", "0.24"],
              ["Sturge Head", "18,900", "61", "0.27"]]),
     "Which choice most effectively uses data from the table to support Salgado's argument?",
     ["The two colonies within fifteen kilometres of open water fledged 0.71 and 0.68 chicks per pair although they differ almost sixfold in size, while the two nearly sixty kilometres away fledged 0.24 and 0.27.",
      "Ilse Point, with 21,500 breeding pairs, fledged 0.68 chicks per pair.",
      "Drift Bay, the smaller of the two distant colonies, fledged 0.24 chicks per pair, the lowest figure recorded.",
      "The largest colony, Ilse Point, did not record the highest number of chicks fledged per pair."],
     "A",
     "The argument needs distance to sort the colonies where size does not, and only the response "
     "setting the two near colonies against the two distant ones, and noting that the near pair "
     "differ almost sixfold in size, supplies both halves. The observation that the largest colony "
     "did not fledge the most chicks defeats one simple version of the size explanation without "
     "showing that distance accounts for the figures."),

 coe("E9",
     "A photographic emulsion is a suspension of silver halide grains in gelatin, and a larger "
     "grain catches more light but records a coarser detail. Four plates were coated in one "
     "factory, exposed on the same subject and measured on the same bench. Emulsion chemist Karin "
     "L&oslash;vold argues that the speed of a plate is bought at the cost of the detail it can "
     "record."
     + table(["Plate", "Mean grain diameter (micrometres)", "Speed (ISO)",
              "Resolving power (lines per mm)"],
             [["Process", "0.2", "25", "200"],
              ["Portrait", "0.5", "100", "125"],
              ["Press", "1.1", "400", "80"],
              ["Night", "2.0", "1600", "45"]]),
     "Which choice most effectively uses data from the table to support L&oslash;vold's argument?",
     ["The night plate, at ISO 1600, resolved 45 lines per millimetre while the process plate, at ISO 25, resolved 200, and resolving power fell at every step as speed rose across the four plates.",
      "The press plate had a mean grain diameter of 1.1 micrometres.",
      "The portrait plate resolved 125 lines per millimetre, more than the press plate managed.",
      "The process plate had the smallest grains of the four plates tested."],
     "A",
     "The claim is that speed is paid for in detail, so it needs the fastest and the slowest plates "
     "set against each other on both measures together with the trend across the range, and only "
     "one response supplies that. Reporting that the slowest plate had the smallest grains "
     "describes the emulsion without linking speed to the detail recorded."),

 # ------------------------------------------------------------- Inferences (6)
 inf("I1",
     "A wheelwright builds a wheel slightly larger than the iron tyre that will go round it. The "
     "smith heats the tyre until it has expanded enough to drop over the rim, and water is thrown "
     "on at once; as the iron contracts it draws every joint in the wheel tight and holds the whole "
     "structure in compression. Wooden felloes shrink through a long dry summer while the iron does "
     "not. A wheel left standing in an open yard through such a season will therefore _____",
     ["slacken at the joints the tyre had been holding closed.",
      "grip its tyre more firmly than it did when the wheel was new.",
      "swell until the tyre can no longer be taken off it.",
      "carry a heavier load than a wheel kept under cover."],
     "A",
     "The tightness of the wheel comes from iron squeezing wood, so wood that loses volume inside a "
     "ring which keeps its own leaves the squeeze reduced and the joints open. The response "
     "promising a firmer grip reverses the effect the passage has just described."),

 inf("I2",
     "A single crystal held in a beam can be turned so that every set of planes reflects in turn, "
     "and each reflection is recorded separately with its own direction and its own strength. That "
     "separation is what allows an atomic arrangement to be worked out. In a powder the crystallites "
     "lie in every orientation at once, so reflections that would have been recorded separately "
     "arrive superimposed at the same angle. A compound that cannot be persuaded to grow a crystal "
     "large enough to mount can therefore still be _____",
     ["recognised by comparison with a pattern already on record, though not solved from first principles.",
      "solved as completely as one that grows large crystals readily.",
      "studied only by methods that involve no X-rays at all.",
      "identified from the strength of its strongest reflection alone."],
     "A",
     "The passage says the powder destroys the separation on which working out an arrangement "
     "depends while leaving a pattern that the compound reproduces, so matching stays available and "
     "solving does not. The response promising a complete solution ignores the superposition the "
     "text identifies as the obstacle."),

 inf("I3",
     "Roman law allowed a possessor to become owner after holding a thing for a fixed period, one "
     "year for movables and two for land. The rule closed disputes that no evidence could settle, "
     "but it was hedged about: the possession had to have begun in good faith, and the thing itself "
     "had to be capable of the benefit, a stolen object being permanently barred from it however "
     "long it was held and through however many hands it passed. A jurist advising a purchaser who "
     "had bought in complete innocence from a thief would therefore have said that the buyer _____",
     ["could never acquire ownership of the thing by holding it, whatever his own state of mind.",
      "became owner of the thing after one year, since he had acquired it in good faith.",
      "could acquire ownership only after the longer period fixed for land.",
      "was liable to the same penalty as the thief who had sold it to him."],
     "A",
     "The bar is attached to the object rather than to the holder, and the passage says a stolen "
     "thing never qualifies through however many hands it passes, so the buyer's own innocence "
     "cannot cure it. The response granting ownership after a year applies the good-faith condition "
     "and ignores the separate condition laid on the thing."),

 inf("I4",
     "An archive holds a wax cylinder recorded in a Somerset kitchen in 1907. The singer was "
     "seventy, sang a single verse because the cylinder would hold no more, and had learned the "
     "song from a carter who died before anyone thought to write anything down. Twenty other people "
     "in the same parish are known to have sung it. A scholar who treats the cylinder as the song "
     "rather than as one performance of it is therefore liable to _____",
     ["mistake the features of a single occasion for properties of the song itself.",
      "underestimate the age of the version the singer had learned.",
      "attribute the song to the carter rather than to the singer.",
      "overlook the technical limitations of early recording equipment."],
     "A",
     "The passage stresses that the cylinder caught one elderly singer, on one occasion, under a "
     "limit of length, among twenty others who sang the same song, so whatever belongs to that "
     "occasion risks being read as belonging to the song. The age of the version is not something "
     "the text gives any means of judging."),

 inf("I5",
     "A merchant in fifteenth-century Genoa who owed money in Bruges could avoid sending coin "
     "across Europe. He paid a banker in Genoa, who wrote an order on a correspondent in Bruges "
     "directing him to pay the sum there in the money of that place. The paper travelled in a "
     "saddlebag and was worth nothing to a robber who was not the named payee. The whole "
     "arrangement rested on the fact that the Genoese banker _____",
     ["stood in a settled relationship with a house in Bruges that held funds on his account.",
      "had accepted the risk of carrying coin himself on an earlier journey.",
      "charged the merchant less than the cost of hiring an armed escort.",
      "could compel the authorities in Bruges to enforce the order he had written."],
     "A",
     "The order directs someone else to pay in another city, which can only work if that "
     "correspondent already holds or owes money to the writer, so the arrangement depends on the "
     "standing connection between the two houses. The relative cost of an escort would explain why "
     "a merchant chose the instrument, not how the payment in Bruges could be made at all."),

 inf("I6",
     "The growing tip of a shoot produces auxin, which travels down the stem and holds the buds in "
     "the leaf axils below it dormant. Remove the tip and the supply stops; within days the two "
     "buds nearest the cut begin to grow, and each of the new shoots then produces auxin of its own "
     "and suppresses the buds beneath it in turn. A gardener who shortens every leading shoot of a "
     "young hedge each spring is therefore _____",
     ["turning the plant's own signal against itself in order to obtain a denser hedge.",
      "delaying the plant's growth until the following season.",
      "reducing the number of shoots the hedge will eventually carry.",
      "removing the tissue in which the hedge stores its reserves."],
     "A",
     "Cutting the tip removes the source of the suppressing signal and releases two buds where one "
     "shoot stood, and repeating that every spring multiplies the shoots, which is what thickens a "
     "hedge. The response about fewer shoots contradicts the release of dormant buds the passage "
     "describes."),

 # ------------------------------------------------------------ Boundaries (12)
 bnd("B1",
     "Malolactic fermentation is carried out not by yeast but by bacteria, and it converts a sharp "
     "acid inherited from the grape into a softer one. A winemaker who wants a red to lose its edge "
     "encourages _____ is making a crisp white in a warm region generally works to prevent it.",
     ["it; one who", "it, one who", "it one who", "it: and one who"], "A",
     "A complete statement stands on either side of the blank and no conjunction joins them, so the "
     "mark has to be one that can separate two sentences. Setting a comma there leaves a splice, "
     "and omitting punctuation altogether runs the second statement straight into the first."),

 bnd("B2",
     "A cocoon is killed before the moth emerges, because a moth chewing its way out cuts the "
     "filament into short lengths. Since the whole value of a cocoon lies in the fact that its "
     "filament is _____ stifle the pupae in hot air within a few days of spinning.",
     ["unbroken, growers", "unbroken; growers", "unbroken: growers", "unbroken and growers"], "A",
     "The words running from &ldquo;Since&rdquo; to the blank form a subordinate clause, and a "
     "subordinate clause placed ahead of the main clause is separated from it by a comma. Both the "
     "semicolon and the colon demand a full sentence in front of them, and no full sentence stands "
     "there."),

 bnd("B3",
     "A wheelwright keeps three timbers in his yard and does not substitute one for _____ for the "
     "hub, which must take the spokes without splitting, oak for the spokes themselves, and ash for "
     "the curved segments of the rim.",
     ["another: elm", "another, elm", "another; elm", "another elm"], "A",
     "A complete statement stands before the blank and the words after it name the three timbers "
     "that statement refers to, which is the work a colon does. A semicolon would require another "
     "full sentence after it, and a list of timbers is not one."),

 bnd("B4",
     "Every large telescope built before 1890 used a lens, and a lens more than a metre across sags "
     "under its own weight. The reflector that replaced _____ whose mirror can be supported across "
     "the whole of its back, has no such limit.",
     ["it, a design", "it; a design", "it: a design", "it a design"], "A",
     "The words between the blank and the comma after &ldquo;back&rdquo; supply a supplementary "
     "description of the reflector, and a supplement of that kind sits inside a matching pair of "
     "commas. Neither a semicolon nor a colon can open a pair that a comma closes, and leaving the "
     "mark out runs the description into the noun with nothing to set it off."),

 bnd("B5",
     "The bath in which a wet plate is sensitised holds silver nitrate in solution, and it grows "
     "weaker with every plate that passes through it. A photographer who has coated six plates in "
     "an afternoon and has begun to see thin, patchy _____ the strength of the bath before blaming "
     "the light.",
     ["negatives tests", "negatives, tests", "negatives; tests", "negatives: tests"], "A",
     "The long relative clause describing the photographer ends at the blank and the verb of the "
     "main sentence begins immediately afterwards, and no mark belongs between a subject and its "
     "verb. Every punctuation mark offered would cut the subject off from the verb that completes "
     "it."),

 bnd("B6",
     "A radiosonde is released twice a day from several hundred stations and reports temperature, "
     "humidity and wind as it climbs. The instrument is not _____ no attempt is made to find it "
     "after the balloon bursts and the package falls back through the cloud.",
     ["recovered, and", "recovered and", "recovered; and", "recovered: and"], "A",
     "Both halves of the sentence are complete statements joined by a coordinating conjunction, and "
     "a comma belongs in front of that conjunction. Running them together with no mark fuses two "
     "sentences, and putting a semicolon or a colon before the conjunction doubles the join."),

 bnd("B7",
     "A Roman contract of stipulation was made by question and answer in set words, and the words "
     "had to correspond exactly. The rule looks like a trap for the unwary but served the purpose "
     "that writing served _____ moment at which a promise became binding could be fixed precisely, "
     "and witnesses could say whether the words had been spoken or not.",
     ["elsewhere: the", "elsewhere, the", "elsewhere the", "elsewhere; and the"], "A",
     "A complete statement stands before the blank and what follows spells out the purpose that "
     "statement refers to, which is what a colon introduces. The comma leaves two statements "
     "spliced together, and a semicolon followed by a conjunction doubles the join between them."),

 bnd("B8",
     "An octopus has neither bone nor shell, and the only rigid part of the whole animal is the "
     "beak at the centre of its arms. It can therefore squeeze through any gap a little wider than "
     "that _____ is why the lid of an aquarium tank is clamped down rather than merely laid on.",
     ["beak, which", "beak which", "beak; which", "beak: which"], "A",
     "The clause opening with &ldquo;which&rdquo; comments on the whole statement before it instead "
     "of narrowing the noun, so a comma is needed to set it off. A semicolon or a colon would "
     "require a complete sentence after it, and a relative clause is not one."),

 bnd("B9",
     "A protein crystal is mostly water and is easily destroyed by the very beam that is meant to "
     "measure it. Cooling the crystal to a hundred kelvin before the exposure slows that damage by "
     "a large _____ does not prevent it, and a full measurement is still assembled from several "
     "crystals rather than taken from one.",
     ["factor; however, it", "factor, however, it", "factor however, it", "factor: however, it"],
     "A",
     "Two complete statements meet at the blank, and the adverb that opens the second cannot join "
     "them, so the mark in front of it must be one that separates sentences. A comma there produces "
     "a splice, and a colon would announce that what follows explains what precedes, which a "
     "contrast does not."),

 bnd("B10",
     "The collector printed a hundred and twelve versions of one ballad and grouped them by melody "
     "rather than by text. The four _____ open on a rising fourth are placed together, although "
     "their words have almost nothing in common.",
     ["versions that", "versions, that", "versions; that", "versions: that"], "A",
     "The clause beginning with &ldquo;that&rdquo; picks out which four versions are meant, and a "
     "clause doing that work joins its noun with no mark between them. Each punctuation mark "
     "offered would separate the noun from the words that identify it."),

 bnd("B11",
     "A prescribed burn is lit under conditions chosen in advance: a narrow band of humidity, a "
     "wind from a settled quarter, and a fuel bed dry on top and damp beneath. Working down the "
     "slope against the _____ keeps the flames low enough to consume the litter without carrying "
     "into the crowns.",
     ["wind, the crew", "wind the crew", "wind; the crew", "wind: the crew"], "A",
     "The opening participial phrase describes the crew named after the blank, and such a phrase is "
     "separated from the main clause by a comma. A semicolon or a colon would need a complete "
     "statement in front of it, and the phrase about descending the slope is not one."),

 bnd("B12",
     "The Bank of England's notes were payable in gold on demand through most of the nineteenth "
     "century, and the promise was kept. Two wars suspended that _____ note that circulates today "
     "is legal tender because Parliament says so, and not because anything is held against it.",
     ["promise. The", "promise, the", "promise the", "promise: and the"], "A",
     "The words on either side of the blank form complete sentences with no conjunction between "
     "them, so a full stop is what belongs there. A comma alone splices two sentences together, and "
     "a colon followed by a conjunction doubles the join."),

 # ----------------------------------------------- Form, Structure, and Sense (9)
 fss("F1",
     "A magistrate's edict bound only the year in which he held office, and the opinions of the "
     "jurists bound nobody at all until an emperor gave particular jurists the right to have their "
     "views followed. Neither the edicts nor the commentary written upon them _____ collected in an "
     "authoritative form before the sixth century.",
     ["was", "were", "have been", "are"], "A",
     "With two subjects joined by &ldquo;neither ... nor&rdquo; the verb agrees with the one nearer "
     "to it, and the nearer subject here is the singular &ldquo;commentary&rdquo;. The plural verb "
     "would agree with the edicts, which stand on the far side of the conjunction."),

 fss("F2",
     "A dry plate can be bought ready-coated, exposed weeks later and developed weeks after that, "
     "none of which the wet process ever allowed. By the time the manufacturer's first "
     "advertisement appeared in 1878, the emulsion _____ in the firm's own darkroom for nearly "
     "three years.",
     ["is tested", "had been tested", "will be tested", "is being tested"], "B",
     "The testing was finished before the advertisement appeared, and the appearance is itself in "
     "the past, so the past perfect is what places one past event ahead of another. The present "
     "forms put the testing in the writer's own time, which the date rules out."),

 fss("F3",
     "Cuttlefish and octopuses hunt in quite different ways, one waiting on the sand for a passing "
     "crab and the other quartering a reef by daylight, but each of them controls the colour of "
     "_____ skin with the same arrangement of muscle-worked pigment sacs.",
     ["its", "their", "it's", "them"], "A",
     "The pronoun refers back to &ldquo;each&rdquo;, which is singular however many kinds of animal "
     "are under discussion, so the singular possessive is required. The plural form would agree "
     "with the two species named earlier rather than with the subject of the clause, and the "
     "contracted form spells out &ldquo;it is&rdquo;."),

 fss("F4",
     "Sericulture reached Byzantium in the sixth century, and the Mediterranean has produced raw "
     "silk in some quantity ever since. The filatures of Piedmont and Lombardy _____ the European "
     "trade for four hundred years before Japanese and Chinese silk displaced them in the 1870s.",
     ["dominate", "have dominated", "dominated", "will dominate"], "C",
     "The four hundred years named are closed off by the displacement of the 1870s, so the sentence "
     "reports a finished stretch of the past and takes the simple past. The present perfect would "
     "carry the domination up to the present day, which the closing date denies."),

 fss("F5",
     "Two diagrams of what may be the same knot rarely look alike, and the only way to be sure is "
     "to reach one from the other by permitted moves. Working through a long sequence of such moves "
     "on a diagram of eleven crossings, _____",
     ["the number of crossings fell to seven and then rose again to nine.",
      "a student in the seminar brought it down to seven crossings and then watched it rise again to nine.",
      "it became clear that the count does not fall steadily.",
      "there was no steady fall in the number of crossings."],
     "B",
     "The opening phrase describes whoever was working through the moves, so the clause after it "
     "has to begin with that person, and only the version naming the student in the seminar does. "
     "Opening with the number of crossings makes the count itself perform the work."),

 fss("F6",
     "Two wheels came back from the same farm in the same week, both with the felloes opening at "
     "the joints. The _____ tyres had been set by different smiths, and only one of the two had "
     "cooled the iron quickly enough to draw the joints closed.",
     ["wheels", "wheel's", "wheels'", "wheelses"], "C",
     "The tyres belong to both of the wheels, so the noun must be plural and possessive at once, "
     "which puts the apostrophe after the plural ending. The singular possessive would assign both "
     "tyres to one wheel, and the bare plural marks no possession at all."),

 fss("F7",
     "A supercell is not merely a large thunderstorm. What sets it apart is a single updraught that "
     "rotates, and that rotation _____ the storm to stand clear of the rain it produces instead of "
     "being killed by its own downdraught within the hour.",
     ["allowing", "allows", "to allow", "having allowed"], "B",
     "The words after the conjunction form the second half of a compound sentence and need a finite "
     "verb to complete them. The participle and the infinitive would both leave that half of the "
     "sentence without one."),

 fss("F8",
     "The census counts birds on the nest, and the surveyors work along the ledges from the "
     "seaward end. Among the birds recorded on the eastern ledges last season _____ nearly two "
     "thousand non-breeders, which the survey enters under a heading of its own.",
     ["was", "were", "has been", "is"], "B",
     "The sentence is inverted, and its subject is the plural phrase naming two thousand "
     "non-breeders, which stands after the verb rather than before it. A singular verb would agree "
     "with the introductory phrase about the ledges, which is not the subject at all."),

 fss("F9",
     "An observatory of the 1880s ran on one steam engine in an outbuilding. The dome, the rising "
     "floor and the clock drive all _____ their power from a single shaft, so a failure in the "
     "engine house halted every part of the night's work at once.",
     ["draws", "drew", "has drawn", "is drawing"], "B",
     "Three subjects joined by &ldquo;and&rdquo; make a plural subject, which rules out the "
     "singular form, and the sentence describes an observatory of the 1880s, so the past tense is "
     "what the rest of the sentence has already established."),

]

DROPPED = {}
