#!/usr/bin/env python3
"""
Reading & Writing authored for Test 10.

Every item here is original: the transcribed pool was exhausted by Test 8, and
the source papers that remain recycle each other (see the Test 6 finding in
CLAUDE.md). Writing the questions outright also removes the failure mode that
cost Test 5 six wrong answers: a transcribed answer key nobody re-derived.

Each item therefore carries a `why` that records the reasoning which produced
the key AND names why the strongest distractor fails. Rationales refer to
options by their CONTENT, never by letter, so `balance_rw.py` is free to rotate
the choice order without invalidating the record.

Topics are chosen to be specific and unusual rather than the standard SAT
staples, and no topic is reused from rw_test8.py: Nabataean cisterns, quipus,
sea silk, whale earwax, terra preta, Wardian cases, gamelan tuning, Hallstatt
salt, katsuobushi, lunar laser ranging, muon tomography, tardigrades, Ainu bark
cloth, the guano trade, violin dendrochronology, the Tswana kgotla, tuned mass
dampers, cuneiform accounting, leafcutter agriculture, radiolarian ooze, the
Vasa, Nushu, the Svalbard vault, ambergris, and so on.

Block counts (fixed by the assembler's quota, 3 modules x 27):
    Words in Context 15, Text Structure and Purpose 6,
    Central Ideas and Details 6, Command of Evidence 9, Inferences 6,
    Boundaries 12, Form, Structure, and Sense 9, Transitions 9,
    Rhetorical Synthesis 9                                        = 81
"""

SOURCE = "AUTHORED-T10"
MODULE = "RW"


def wic(num, passage, choices, answer, why):
    return dict(num=num, skill="Words in Context", passage=passage,
                stem="Which choice completes the text with the most logical and precise word or phrase?",
                choices=choices, answer=answer, why=why)


def meaning(num, passage, word, choices, answer, why):
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
     "The Nabataeans built Petra in a desert that receives less than fifteen centimetres of rain "
     "in a year. Channels cut into the sandstone caught whatever fell on the surrounding slopes "
     "and carried it to cisterns hollowed out beneath the streets, so that the city's water "
     "supply stayed _____ even through years in which no rain fell at all.",
     ["intermittent", "dependable", "abundant", "seasonal"], "B",
     "The clause 'even through years in which no rain fell' says the supply held up when the "
     "rain failed, so the blank needs a word meaning reliable. The 'abundant' option describes "
     "quantity, which fifteen centimetres of rainfall caught and stored cannot promise."),

 wic("W2",
     "Georgian villages have kept a three-voice singing tradition alive for centuries without "
     "written scores. Every part is learned by ear from other singers, and two villages a valley "
     "apart may harmonise the same song quite differently. The tradition is therefore not fixed "
     "but _____, shifting a little with each generation that carries it forward.",
     ["static", "mutable", "obsolete", "uniform"], "B",
     "The sentence sets the blank against 'not fixed' and then glosses it as shifting with each "
     "generation, so the word must mean liable to change. The 'uniform' option is ruled out by "
     "two villages harmonising the same song differently."),

 wic("W3",
     "Inca administrators kept their records on quipus, bundles of cords in which the type of "
     "knot and its position along the cord both carried meaning. Spanish officials who could not "
     "read them assumed the cords were ornamental. Modern study has shown the opposite: the quipu "
     "is a _____ system, capable of holding censuses, tribute rolls and dates with precision.",
     ["rudimentary", "notational", "ceremonial", "provisional"], "B",
     "Knot type and position encoding censuses and tribute precisely is a system of notation. "
     "The 'rudimentary' option contradicts the precision the sentence claims for it."),

 wic("W4",
     "Byssus is the fine thread a pen shell spins to anchor itself to the seabed. Gathered and "
     "combed, it was once woven into gloves light enough to be folded inside a walnut shell. Few "
     "weavers ever learned the technique, and today it is practised by a single family on "
     "Sardinia; the craft is thus all but _____.",
     ["extinct", "commercial", "renowned", "mechanised"], "A",
     "One family is all that remains, so 'all but ___' calls for a word meaning gone. The "
     "'renowned' option describes reputation rather than survival, and nothing in the text says "
     "the craft is widely known."),

 wic("W5",
     "A whale's ear canal fills with wax in layers, one pale and one dark for every year of the "
     "animal's life, and each layer traps the hormones that were circulating in its blood at the "
     "time. A single plug pulled from a stranded whale can therefore be read as a _____ of stress "
     "across the whole of that animal's life, decade by decade.",
     ["chronicle", "summary", "forecast", "symptom"], "A",
     "Layered, year-by-year, decade-by-decade evidence is a record kept over time. The 'summary' "
     "option loses exactly the sequence the annual layers preserve, which is what the sentence "
     "emphasises."),

 wic("W6",
     "Patches of unusually dark and fertile soil scattered through the Amazon basin were for a "
     "long time assumed to be a natural formation. They are now understood to be _____, built up "
     "over centuries from the charcoal, fish bone and broken pottery that the people living there "
     "discarded around their settlements.",
     ["anthropogenic", "sedimentary", "volcanic", "transient"], "A",
     "Soil built up from charcoal, bone and pottery that people discarded was made by human "
     "activity. The 'sedimentary' option would simply restate the natural origin the sentence "
     "rejects."),

 wic("W7",
     "Before the sealed glass Wardian case, plants shipped across an ocean died of salt spray and "
     "neglect within weeks, and a collector counted on losing almost every specimen. The case made "
     "survival almost _____: ferns packed in London in 1834 reached Sydney alive after eight "
     "months at sea, and the return shipment arrived in the same condition.",
     ["routine", "miraculous", "incidental", "negotiable"], "A",
     "The example shows survival becoming the ordinary, expected outcome rather than a rarity. "
     "The 'miraculous' option points back to the earlier situation the case replaced instead of "
     "describing what it achieved."),

 wic("W8",
     "No two gamelan orchestras in Java are tuned quite alike. A set of instruments is tuned as a "
     "group and to itself, and an instrument borrowed from a different set will sound wrong "
     "beside them however carefully it was made. Tuning is therefore _____ to each ensemble "
     "rather than fixed by any external standard.",
     ["peculiar", "indifferent", "adjacent", "secondary"], "A",
     "The sentence needs a word meaning belonging to that one ensemble alone, which 'peculiar to' "
     "expresses, and the contrast with 'fixed by any external standard' confirms it. The "
     "'secondary to' option would rank tuning below the ensemble in importance, which is not the "
     "relation described."),

 wic("W9",
     "The prehistoric salt workings at Hallstatt have given up wooden shovels, leather caps, "
     "lengths of rope and even fragments of woven clothing. Salt draws the water out of organic "
     "material and halts decay, so objects that would long ago have rotted away in ordinary "
     "ground were instead _____ underground for three thousand years.",
     ["buried", "preserved", "discarded", "compressed"], "B",
     "The sentence explains that salt halts decay and contrasts that with rotting, so the blank "
     "needs a word meaning kept intact. The 'buried' option is true of the objects but says "
     "nothing about the contrast with rotting that the sentence is drawing."),

 wic("W10",
     "Making katsuobushi takes the better part of a year. The fish is simmered, then smoked over "
     "many separate firings, then deliberately inoculated with a mould that draws out the last of "
     "the moisture. The finished block is hard enough that it must be shaved with a plane, and the "
     "process is far too _____ to be hurried along by machinery.",
     ["exacting", "lucrative", "obscure", "recent"], "A",
     "Months of simmering, repeated smoking and a controlled mould growth describe a demanding, "
     "precise process, which is what 'too ___ to be hurried' requires. The 'obscure' option says "
     "the method is little known, not that it resists being sped up."),

 wic("W11",
     "The retroreflectors left on the lunar surface by Apollo crews send a laser pulse straight "
     "back to whichever telescope fired it. Timing the round trip gives the Earth-Moon distance "
     "to within a few centimetres, and repeating that measurement for half a century has shown "
     "the Moon to be _____ from the Earth by about 3.8 centimetres a year.",
     ["receding", "wobbling", "brightening", "contracting"], "A",
     "What the technique measures is a distance, so a steady change of 3.8 centimetres a year in "
     "that figure means the Moon is moving away. The 'contracting' option would be a change in "
     "the Moon's own size, which a distance measurement does not report."),

 wic("W12",
     "Cosmic-ray muons pass through solid stone, but they are absorbed at a rate that depends on "
     "how much stone lies along their path. Detectors set up in a chamber inside a pyramid record "
     "an excess of muons arriving from any direction in which the rock is thinner, and can "
     "therefore _____ a hidden void overhead without a single block being moved.",
     ["excavate", "detect", "reinforce", "date"], "B",
     "The point of the sentence is that the void is found without any block being moved, so the "
     "verb has to be one of observation. The 'excavate' option flatly contradicts the closing "
     "clause."),

 wic("W13",
     "A tardigrade caught in drying moss expels almost all the water in its body, draws itself "
     "into a barrel shape and stops metabolising altogether. In this state it survives boiling, "
     "freezing and the vacuum of space, and a drop of water will revive it decades later. Its "
     "dormancy is therefore not sleep but a _____ of life itself.",
     ["prolongation", "suspension", "repudiation", "celebration"], "B",
     "Metabolism stops entirely and then resumes decades later once water is added, which is a "
     "temporary halt. The 'prolongation' option says the opposite of a stop, and nothing in the "
     "passage is being rejected."),

 meaning("W14",
     "The canal was cut for barges carrying coal, and its locks were built to the dimensions "
     "those barges required. A vessel of greater <u>draft</u> could not use the canal at all: "
     "below a certain depth the hull would ground on the silt of the bottom long before it "
     "reached the next lock, and the crew would have to unload to float it off again.",
     "draft",
     ["A preliminary version of a document.", "A current of cold air.",
      "The depth of water a vessel requires.", "A demand for payment."],
     "C",
     "The passage explains the term as it uses it, a hull grounding on the bottom in shallow "
     "water, so the sense required is the depth of water a vessel needs. The 'preliminary "
     "version' sense is a genuine meaning of the word but has nothing to do with hulls and silt."),

 meaning("W15",
     "The columns were roughed out in the quarry and finished on site. Each <u>capital</u> was "
     "cut last of all, partly because its acanthus leaves were the part most easily chipped in "
     "transport and partly because the carver wanted to see the shaft standing in place before "
     "deciding how deeply to undercut the stone.",
     "capital",
     ["A city that is the seat of a government.", "Wealth used to produce further wealth.",
      "The carved block at the top of a column.", "An uppercase letter."],
     "C",
     "The word names something cut from stone, carved with acanthus leaves and chipped in "
     "transport, which is the architectural sense. The financial sense is far more common in "
     "ordinary use but cannot be undercut by a carver."),

 # --------------------------------------------- Text Structure and Purpose (6)
 tsp("S1",
     "Ainu weavers make attush cloth from the inner bark of the elm. <u>The bark has to be "
     "stripped in early summer, while the sap is running, or it cannot be separated into usable "
     "fibre at all.</u> Once the strips have been soaked in a stream and split by hand, they are "
     "spun and woven on a body-tension loom, then dyed in patterns that also appear on Ainu "
     "woodcarving.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It identifies a constraint that governs when the raw material can be gathered.",
      "It argues that elm bark is superior to other fibres used in weaving.",
      "It explains why attush patterns resemble the patterns on Ainu woodcarving.",
      "It contrasts two competing methods of preparing bark for the loom."],
     "A",
     "The sentence states a timing requirement, early summer while the sap runs, and the "
     "consequence of missing it, which is a constraint on gathering. The resemblance to "
     "woodcarving appears only in the final sentence and is not what the underlined sentence "
     "accounts for."),

 tsp("S2",
     "For three decades in the nineteenth century the Chincha Islands off Peru supplied Europe "
     "with the most effective fertiliser then obtainable: seabird guano, laid down over millennia "
     "on rock that almost never sees rain. Ships waited months in the roadstead for a cargo, and "
     "two governments went to war over the trade. Then the deposits ran out. Nitrate mines and "
     "later synthetic ammonia took the market, and the islands are now visited mainly by "
     "ornithologists.",
     "Which choice best states the main purpose of the text?",
     ["To explain the chemical properties that made guano so effective as a fertiliser.",
      "To trace the rise and collapse of a trade and note what became of its source.",
      "To argue that synthetic ammonia was a more sustainable alternative to guano.",
      "To describe the working conditions of the labourers on the Chincha Islands."],
     "B",
     "The text moves from boom, through exhaustion and replacement, to the islands' present "
     "quiet, which is a rise-and-fall account. It never explains what makes guano effective, only "
     "asserts that it was."),

 tsp("S3",
     "Dating a violin used to mean trusting the label pasted inside it. Now a good photograph of "
     "the spruce top will often do: the growth rings visible in the wood can be matched against "
     "master chronologies assembled from thousands of Alpine trees. <u>An instrument cannot have "
     "been made before its youngest ring finished growing.</u> Several violins bearing "
     "eighteenth-century labels have turned out to contain wood felled a full century later.",
     "Which choice best describes the function of the underlined sentence?",
     ["It states the principle that makes the dating method decisive.",
      "It concedes a weakness in the ring-matching technique.",
      "It describes how the master chronologies are assembled.",
      "It offers an example of an instrument found to be mislabelled."],
     "A",
     "The underlined sentence gives the rule that ties a ring date to the earliest possible date "
     "of manufacture, and the closing sentence applies that rule to expose false labels. How the "
     "chronologies are assembled is covered by the sentence before it, not by this one."),

 tsp("S4",
     "A kgotla is a Tswana assembly held in the open, usually in the shade of a particular tree. "
     "Any adult present may speak, and speakers are heard in turn until nobody has anything "
     "further to add. The chief does not vote. He listens, and at the end he states the sense of "
     "the meeting; a chief who states it wrongly can expect to be corrected on the spot.",
     "Which choice best describes the overall structure of the text?",
     ["It defines an institution, describes how its proceedings run, and specifies the limited role of its leader.",
      "It compares two forms of assembly and argues that one of them is fairer.",
      "It presents a chronological account of how the kgotla developed.",
      "It raises a criticism of the kgotla and then rebuts that criticism."],
     "A",
     "The text names and defines the assembly, then describes the order of speaking, then narrows "
     "to what the chief may and may not do. No second institution is ever mentioned, so nothing "
     "is being compared."),

 tsp("S5",
     "A skyscraper does not resist the wind by rigidity alone. Near the top of Taipei 101 hangs a "
     "polished steel sphere weighing 660 tonnes, suspended on cables and free to swing. When the "
     "tower leans in a gust the sphere lags behind and pulls against the motion. <u>Sway on the "
     "upper floors is cut by roughly forty per cent, which is the difference between a nuisance "
     "and an evacuation.</u>",
     "Which choice best describes the function of the underlined sentence?",
     ["It quantifies the effect of the device just described and indicates why that effect matters.",
      "It introduces a second engineering problem that the text goes on to solve.",
      "It questions whether the sphere performs as its designers intended.",
      "It explains the method by which the sphere is suspended."],
     "A",
     "The sentence supplies a figure for the reduction in sway and then says what that reduction "
     "means for the people inside, so it both measures and evaluates the damper. Nothing in it "
     "casts doubt on the design."),

 tsp("S6",
     "Writing in Mesopotamia did not begin with poetry. The earliest tablets record quantities of "
     "barley, beer and livestock, and their signs descend from small clay tokens once sealed "
     "inside hollow clay envelopes to certify a debt. To show what an envelope held, the tokens "
     "were pressed into its outer surface before it was closed. Someone eventually noticed that "
     "the impressions made the tokens inside unnecessary.",
     "Which choice best states the main purpose of the text?",
     ["To explain the administrative origins of a writing system.",
      "To argue that Mesopotamian literature has been undervalued.",
      "To describe how clay tablets were fired and then stored.",
      "To compare Mesopotamian writing with the alphabets that followed it."],
     "A",
     "Every sentence concerns accounting: tallies of barley and livestock, tokens certifying a "
     "debt, and the step from impressed envelope to tablet. Literature is raised only in the "
     "opening sentence, and only in order to be set aside."),

 # ----------------------------------------------- Central Ideas and Details (6)
 cid("C1",
     "Leafcutter ants do not eat the leaves they carry into the nest. They chew them into a "
     "mulch, and on that mulch they grow a fungus, and the fungus is what feeds the colony. The "
     "garden is vulnerable to a parasitic mould that would overrun it in days. On their bodies "
     "the ants carry a bacterium producing a compound that suppresses exactly that mould; remove "
     "the bacterium and the garden fails.",
     "Which choice best states the main idea of the text?",
     ["Leafcutter ants feed on leaves that they first soften into a mulch.",
      "The colony depends on a cultivated fungus, which a bacterium carried by the ants protects.",
      "A parasitic mould has caused the collapse of many leafcutter colonies.",
      "The bacterium carried by the ants is the colony's principal source of food."],
     "B",
     "The text says the fungus feeds the colony and that removing the bacterium makes the garden "
     "fail, so the colony rests on both partners. The claim that the ants eat the leaves is "
     "denied outright in the first sentence."),

 cid("C2",
     "Radiolarians are single-celled drifters that build intricate skeletons out of silica. When "
     "they die the skeletons sink, and over millions of years they pile up on the deep seafloor "
     "as a fine ooze. Because different radiolarian species lived in different intervals, and "
     "because the shape of a skeleton reflects the water the animal grew in, a core drilled "
     "through the ooze gives geologists both a calendar and a thermometer for ancient oceans.",
     "According to the text, why is radiolarian ooze useful to geologists?",
     ["It contains the only fossils that survive at great depth in the ocean.",
      "Species turnover within it marks time while skeleton shape indicates past conditions.",
      "It accumulates quickly enough to record events from one year to the next.",
      "Silica skeletons can be dated more easily than carbonate ones."],
     "B",
     "The final sentence names both uses and their sources: a calendar from the succession of "
     "species, a thermometer from the shape of the skeletons. The text says the ooze piles up "
     "over millions of years, which rules out year-by-year resolution."),

 cid("C3",
     "The warship Vasa capsized in Stockholm harbour in 1628, less than a mile from where she was "
     "launched. She lay in the mud for 333 years and came up with her carvings still crisp. The "
     "Baltic is too brackish for the shipworm that would have eaten an oak hull in open salt "
     "water, and the harbour mud sealed her timbers away from oxygen. What sank the ship is also "
     "what saved her.",
     "Which choice best states the main idea of the text?",
     ["The Vasa survives because the conditions that sank her also protected her wreck.",
      "Shipworms are the principal threat to wooden wrecks in all waters.",
      "Stockholm harbour has preserved a number of seventeenth-century vessels.",
      "The Vasa's carvings were recarved after the ship was raised."],
     "A",
     "The closing sentence states the paradox the passage has been building: sinking into "
     "brackish, oxygen-poor mud is precisely what kept the hull whole. The passage mentions no "
     "other wreck, and no recarving of any kind."),

 cid("C4",
     "N&uuml;shu, a script used by women in one corner of Hunan, was written on folding fans and "
     "embroidered handkerchiefs rather than on paper. Its characters are not the characters that "
     "boys learned in school; they are slanted, thinner in the stroke, and they record the local "
     "speech by sound rather than by meaning. Women who had never been taught to read the "
     "official script could nevertheless read one another.",
     "Which choice best states the main idea of the text?",
     ["N&uuml;shu was a decorative variant of the characters taught in Hunan schools.",
      "N&uuml;shu gave women a means of writing to each other independent of the official script.",
      "N&uuml;shu was written on cloth because paper was scarce in that part of Hunan.",
      "Men in Hunan were forbidden from learning to read N&uuml;shu."],
     "B",
     "The passage insists that the characters are not the school characters and that women with "
     "no schooling could still read each other, which together amount to independence from the "
     "official script. Nothing is said about a shortage of paper or about any prohibition."),

 cid("C5",
     "The seed vault on Svalbard is cut into a mountainside above the permafrost line. Its purpose "
     "is not to collect seed in its own right but to hold duplicates of collections kept "
     "elsewhere, so that a gene bank destroyed by war, fire or accident can be restocked from the "
     "copies. Depositors keep ownership of their own boxes, and the vault has been drawn on only "
     "once, at the request of a collection displaced from Syria.",
     "According to the text, what is the vault's function?",
     ["To gather wild plant species that no other gene bank holds.",
      "To keep backup copies for gene banks that may lose their own holdings.",
      "To distribute seed to farmers in the aftermath of natural disasters.",
      "To hold seed whose ownership its depositors have signed over to Norway."],
     "B",
     "The text states directly that the vault holds duplicates so a destroyed gene bank can be "
     "restocked, and the single withdrawal by a displaced Syrian collection illustrates the "
     "point. Ownership is said to stay with the depositors, which contradicts the transfer "
     "option."),

 cid("C6",
     "Ambergris forms in the gut of a sperm whale around the indigestible beaks of the squid it "
     "swallows. Expelled at sea, a lump may float for years, and sun and salt water alter it as "
     "it drifts: fresh ambergris smells foul, aged ambergris only faintly sweet. Perfumers prized "
     "the aged material because it held other scents on the skin for hours longer than they would "
     "otherwise last, not for any quality of its own smell.",
     "According to the text, why did perfumers prize aged ambergris?",
     ["Because it was the strongest-smelling material available to them.",
      "Because it made other scents last longer rather than for its own odour.",
      "Because it could be gathered fresh from beaches in large quantities.",
      "Because its own smell shifted over the course of a single day."],
     "B",
     "The last sentence separates the two possible reasons and picks one: the material held other "
     "scents on the skin, not that its own smell was valued. The passage calls fresh ambergris "
     "foul-smelling, so nothing supports prizing it for the strength of its odour."),

 # ---------------------------------------------------- Command of Evidence (9)
 coe("E1",
     "The sweet potato is native to South America, yet it was being grown across Polynesia well "
     "before any European ship reached the Pacific. Botanist Hine Waititi argues that Polynesian "
     "voyagers reached the American coast and carried the plant home with them. A rival account "
     "holds that seed capsules drifted across the ocean unaided and took root where they washed "
     "ashore.",
     "Which finding, if true, would most directly support Waititi's argument over the rival one?",
     ["Sweet potato seed capsules can remain viable in seawater for several weeks.",
      "The Polynesian name for the plant closely resembles the name used for it on the South American coast.",
      "Sweet potatoes grow well in the soils of several Pacific island groups.",
      "Coastal peoples in South America cultivated a number of distinct sweet potato varieties."],
     "B",
     "The shared name has to travel with people who speak it; a drifting seed capsule carries no "
     "vocabulary, so a matching word is evidence of contact rather than of drift. Viability in "
     "seawater would support the rival drift account instead."),

 coe("E2",
     "Two bells cast from the same bronze can sound quite unlike each other. Metallurgist Ines "
     "Duarte maintains that a bell's tone is set by the profile to which it is cast &mdash; the way the "
     "wall thickens from lip to crown &mdash; rather than by the small variations in tin content that "
     "distinguish one founder's alloy from another's.",
     "Which finding, if true, would most directly support Duarte's claim?",
     ["Bells cast to the same profile from alloys of differing tin content sound nearly identical.",
      "Bells with a higher tin content are harder and more brittle than bells with less.",
      "Founders have traditionally guarded their alloy recipes with great secrecy.",
      "The largest bells take several days to cool once they have been cast."],
     "A",
     "Holding the profile fixed while the tin content varies, and finding the tone unchanged, "
     "shows the alloy is not what sets the note, which is exactly the claim. Hardness and "
     "brittleness describe the metal's mechanical behaviour, not the pitch it sounds."),

 coe("E3",
     "Great tits living in cities sing at a higher pitch than those in woodland a few kilometres "
     "away. Ornithologist Karel Novak argues that the shift is a response to low-frequency traffic "
     "noise, which would otherwise mask their songs. Others suggest that city birds are simply "
     "smaller on average, and that smaller birds sing higher.",
     "Which finding, if true, would most directly support Novak's explanation over the alternative?",
     ["City great tits weigh slightly less on average than woodland great tits.",
      "Individual birds raise the pitch of their song within minutes when nearby traffic noise increases.",
      "Traffic noise in the cities studied is concentrated below two kilohertz.",
      "Great tits in cities defend smaller territories than those in woodland."],
     "B",
     "The size of a bird's body cannot change within minutes, so a bird that lifts its pitch as "
     "the noise rises must be reacting to the noise itself. Traffic noise concentrated at low "
     "frequencies fits either account, since it does not show that the birds respond to it."),

 coe("E4",
     "The Norse settlements in Greenland were abandoned during the fifteenth century. Historian "
     "Petra Solheim argues that the cause was economic: walrus ivory, effectively the colony's "
     "only export, lost its European market once elephant ivory became available again. Others "
     "point instead to a cooling climate that shortened the growing season for the colony's hay.",
     "Which finding, if true, would most directly support Solheim's argument?",
     ["Ice cores show that summers in southern Greenland grew colder from about 1350 onward.",
      "Hay yields recorded at the settlements were normal in the years before abandonment, and the collapse in ivory prices preceded the departures.",
      "The walrus hunting grounds lay several weeks' sail north of the settlements.",
      "Norse farmers in Iceland came through the same period without abandoning their farms."],
     "B",
     "Normal hay yields remove the fodder failure that the climate account requires, and putting "
     "the price collapse before the departures gives the economic account the order of events it "
     "needs. The ice-core cooling supports the rival explanation instead."),

 coe("E5",
     "A shrub that grows on high Andean slopes fills its leaves with a bitter compound. Botanist "
     "Luis Ferrer proposes that the compound deters insect herbivores. A colleague argues instead "
     "that it screens the leaf against the intense ultraviolet light found at that altitude.",
     "Which finding, if true, would most directly support Ferrer's proposal?",
     ["The compound absorbs strongly in the ultraviolet part of the spectrum.",
      "Plants grown under insect-proof netting produce far less of the compound than exposed plants at the same altitude.",
      "Leaves at the top of the shrub contain more of the compound than leaves lower down.",
      "The compound is concentrated in the outermost cell layers of the leaf."],
     "B",
     "The netting holds altitude and sunlight constant while removing insect access, and the plant "
     "then stops investing in the compound, which points to herbivory as the trigger. Strong "
     "ultraviolet absorbance and higher concentrations in the most exposed leaves both fit the "
     "light-screening account."),

 coe("E6",
     "A qanat is a gently sloping tunnel that carries groundwater from a mountain aquifer to a "
     "village, and it silts up unless it is cleaned every few years. Historian Farah Adeli argues "
     "that the qanats of one Iranian valley stayed in use for eight centuries because of a "
     "customary law assigning each household a share of the maintenance in proportion to its "
     "share of the water, and not merely because the geology there was favourable.",
     "Which finding, if true, would most directly support Adeli's argument?",
     ["Neighbouring valleys with the same geology, but without such a customary law, saw their qanats abandoned within two centuries.",
      "The valley's aquifer is recharged by snowmelt every spring.",
      "The qanat tunnels in the valley are lined throughout with fired clay hoops.",
      "The customary law was first written down in the nineteenth century."],
     "A",
     "Same geology, different institution, different outcome isolates the custom as what kept the "
     "tunnels open. The spring recharge is a feature of the valley that the geological "
     "explanation could claim just as easily."),

 coe("E7",
     "Many pterosaurs carried a bony crest on the skull, and in some species it projected backwards "
     "further than the length of the skull itself. Palaeontologist Marta Oyelaran argues that the "
     "crest served for display to other members of the species rather than as an aerodynamic "
     "rudder for steering in flight.",
     "Which finding, if true, would most directly support Oyelaran's argument?",
     ["Crests are found only in adults, and are far larger in one sex than in the other.",
      "Crested and uncrested pterosaur species occupied the same habitats.",
      "The crest is built of dense bone and would have added little drag in flight.",
      "Crest shape varies considerably from one species to another."],
     "A",
     "Appearing only at maturity and differing between the sexes is the signature of a signal "
     "aimed at other individuals; a flight surface would be needed by juveniles too and would "
     "have no reason to differ by sex. Variation between species is compatible with either "
     "function."),

 coe("E8",
     "Membership of Britain's friendly societies, which pooled workers' contributions to pay "
     "sickness benefits, fell sharply after 1911. Sociologist Denis Kaur argues that the state "
     "insurance scheme introduced in that year displaced them. Others attribute the decline to "
     "workers moving into cities, where the societies' local ties counted for less.",
     "Which finding, if true, would most directly support Kaur's argument?",
     ["Urban branches of the societies had always been smaller than rural ones.",
      "In districts where movement into the cities was negligible, membership fell just as steeply after 1911.",
      "Friendly societies had been losing members slowly since the 1890s.",
      "The state scheme paid a smaller weekly benefit than most societies did."],
     "B",
     "Where the migration did not happen the fall occurred anyway, which removes migration as the "
     "explanation and leaves the change of 1911. The slow decline from the 1890s fails to "
     "separate the two accounts, since either cause could have acted gradually."),

 coe("E9",
     "Large bronzes were usually cast in pieces and joined afterwards, since a single pour of that "
     "volume is difficult to control. A conservator argues that one particular figure was instead "
     "cast in a single pour, citing the complete absence of visible joins anywhere on its surface.",
     "Which finding, if true, would most directly undermine the conservator's argument?",
     ["X-rays of comparable figures show that joins between separately cast parts were routinely filed down and disguised.",
      "The alloy composition of the figure is uniform throughout.",
      "Casting a figure of this size in one pour was technically possible at the time it was made.",
      "The figure stands on a base that was cast separately from the body."],
     "A",
     "The argument runs from no visible joins to no joins at all, and that step collapses if joins "
     "were routinely hidden by finishing work. The separately cast base concerns a different "
     "element altogether and says nothing about the body."),

 # -------------------------------------------------------------- Inferences (6)
 inf("I1",
     "Bristlecone pines at the treeline add so little wood in a year that a single ring can be "
     "thinner than a sheet of paper. What they do lay down is dense and heavily resinous, and a "
     "dead trunk may stand for a thousand years without rotting. Trees of the same species growing "
     "lower down the mountain, in deeper soil and out of the wind, grow far faster and _____",
     ["produce rings that are easier for researchers to count.",
      "do not live anything like as long as those at the treeline.",
      "resist decay for even longer once they have died.",
      "yield wood denser than that of the treeline trees."],
     "B",
     "The passage ties slow growth to dense resinous wood and to standing for a millennium after "
     "death, so faster-growing trees lower down should lack that durability and longevity. The "
     "option giving them denser wood reverses the relationship the passage has just set up."),

 inf("I2",
     "Giant tubeworms crowd around hydrothermal vents on the deep seafloor, far below any "
     "sunlight. An adult worm has neither mouth nor gut. What it has instead is a body cavity "
     "packed with bacteria that oxidise the hydrogen sulphide streaming out of the vent and build "
     "sugars from it. If the vent a colony sits on ceases to flow, the colony _____",
     ["can fall back on filtering particles from the surrounding water.",
      "loses the chemical supply on which its food production depends.",
      "migrates along the ridge to a vent that is still erupting.",
      "reverts to obtaining its energy from sunlight."],
     "B",
     "The worms have no gut and depend on bacteria that need vent sulphide, so a vent that stops "
     "flowing cuts off the input to the whole food chain inside the animal. Filtering and "
     "migration are abilities the passage never grants them, and no sunlight reaches the "
     "seafloor."),

 inf("I3",
     "A blue hole is a flooded sinkhole whose still, oxygen-starved bottom water allows fine "
     "sediment to settle in undisturbed annual layers. When a hurricane passes overhead, it "
     "washes coarse sand off the surrounding reef and into the hole, where the sand settles as a "
     "distinct band within the fine layers. Cores drilled from Bahamian blue holes therefore "
     "allow researchers to _____",
     ["predict the track a hurricane will take before it makes landfall.",
      "count the storms that struck the area long before written records began.",
      "measure the wind speed of individual historical hurricanes.",
      "determine how much rain fell during each of those storms."],
     "B",
     "One coarse band per storm, set into a datable annual sequence, yields a tally of past "
     "storms, which is what the described mechanism delivers. Wind speed and rainfall are not "
     "encoded by the mere presence of a sand band, and nothing in the passage is predictive."),

 inf("I4",
     "Moths caught at street lights were found to fly in tighter spirals than moths netted in "
     "unlit fields a kilometre away. The researchers are careful to note that they sampled only "
     "moths already gathered at the lights. If the moths that spiral tightly are also the ones "
     "drawn to lights in the first place, then the finding _____",
     ["shows that artificial light alters the flight of moths over time.",
      "may reflect which moths are drawn to lights rather than any effect of the light on flight.",
      "would be reversed if the lights were switched off for a whole season.",
      "applies only to the unlit fields that were sampled."],
     "B",
     "The researchers' caution raises the possibility that the trait precedes the exposure, so the "
     "difference could be a sorting effect rather than an effect of the lighting. The option "
     "asserting that light alters flight over time states the causal reading the caution is "
     "putting in doubt."),

 inf("I5",
     "Linear B was deciphered once someone guessed that the language behind it was an early form "
     "of Greek; the guess was confirmed when the readings produced sensible inventories of chariot "
     "wheels and sheep. Linear A uses many of the same signs, but applying the Linear B sound "
     "values to it yields no words in any language anyone has been able to identify. The signs of "
     "Linear A can therefore be pronounced, but the resulting text _____",
     ["cannot be assigned to any language that scholars can recognise.",
      "has been shown to record an early form of Greek after all.",
      "is too badly damaged for the individual signs to be read.",
      "consists mostly of inventories like those written in Linear B."],
     "A",
     "Sound values carry across from the one script to the other while the words they generate "
     "match no known language, which is precisely what being pronounceable but unidentifiable "
     "means. The passage attaches the Greek reading to the deciphered script only, so the option "
     "claiming an early form of Greek for the undeciphered one contradicts it."),

 inf("I6",
     "A coppiced hazel stool is cut back to the ground every seven years and throws up a fresh "
     "crop of straight poles from the surviving root, and it can be worked this way for centuries. "
     "Felling the same hazel outright yields considerably more wood at once, but the stool is then "
     "gone for good. A woodland manager who compared the two practices by the volume removed in a "
     "single year would therefore _____",
     ["overstate the long-run return from felling.",
      "find coppicing the more productive of the two in that year.",
      "conclude that a coppiced stool never regrows.",
      "underestimate the volume that a felled hazel yields."],
     "A",
     "Single-year volume favours felling, while the facts the comparison leaves out, centuries of "
     "repeated cutting from a stool that stays alive, favour coppicing over the long term, so a "
     "one-year measure flatters felling. Coppicing yields less in the year in question, so calling "
     "it more productive contradicts the passage."),

 # --------------------------------------------------------------- Boundaries (12)
 bnd("B1",
     "Bronze needs tin, and tin is scarce almost everywhere in the eastern Mediterranean. Ingots "
     "recovered from a Bronze Age wreck off the Turkish coast have been traced by their trace "
     "elements to mines in Central Asia _____ the metal had travelled some three thousand "
     "kilometres before it ever reached a smith.",
     ["; ", ", ", " ", ": and"], "A",
     "The blank joins two complete sentences with no coordinating conjunction between them, so "
     "the semicolon is the only option that avoids a comma splice."),

 bnd("B2",
     "A sourdough culture is a community of wild yeasts and bacteria rather than a single "
     "organism. Because the balance between those organisms responds to flour, water and room "
     "temperature _____ two starters divided from one jar and kept in different kitchens will "
     "drift apart in flavour within months.",
     [", ", "; ", ": ", " and "], "A",
     "The introductory clause opening with 'Because' is dependent and must be marked off from the "
     "main clause by a comma; both the semicolon and the colon require a complete sentence to "
     "stand in front of them."),

 bnd("B3",
     "Rubbish pits tell an excavator more than temples do, because nobody arranges them for "
     "posterity. The pit behind the fort's granary produced three things the archaeologists had "
     "not expected _____ a child's leather shoe, a wooden writing tablet and the better part of a "
     "barrel of oysters.",
     [": ", "; ", ", and ", " which are"], "A",
     "What comes before the blank is a complete sentence announcing 'three things', and the colon "
     "is the mark that introduces the list specifying them."),

 bnd("B4",
     "Russian universities were closed to women in her lifetime, so she was taught privately and "
     "then abroad. Sofia Kovalevskaya, the first woman appointed to a full professorship in "
     "mathematics in northern Europe _____ won the Bordin Prize in 1888 for her work on the "
     "rotation of a rigid body.",
     [", ", "; ", ": ", " "], "A",
     "The appositive beginning 'the first woman appointed...' was opened with a comma and has to "
     "be closed with a matching comma before the verb 'won'."),

 bnd("B5",
     "The mill stood derelict for sixty years and has been grinding again since 2014. It fills its "
     "pond as the tide floods and works the stones as the tide ebbs _____ and the wheel turns for "
     "roughly five hours out of every twelve.",
     [", ", "; ", ": ", " "], "A",
     "Two independent clauses joined by the coordinating conjunction 'and' take a comma in front "
     "of that conjunction; the semicolon and colon are not used before a coordinating "
     "conjunction, and omitting the punctuation altogether leaves the clauses unseparated."),

 bnd("B6",
     "Volcanic ash settles across an ice sheet within days of an eruption and is then buried by "
     "the next winter's snow. Cores drilled at three sites in Greenland returned a series of thin "
     "ash layers _____ each of which can be matched to a dated eruption somewhere else in the "
     "world.",
     [", ", "; ", ": ", ". "], "A",
     "'each of which' opens a non-essential relative clause, which attaches to the main clause "
     "with a comma; the semicolon and the full stop both require an independent clause to follow "
     "them, and this one is not independent."),

 bnd("B7",
     "Aurorae normally stay within a ring drawn around each magnetic pole. When the solar wind is "
     "strong enough to compress the Earth's magnetic field on the sunward side _____ they can be "
     "seen far to the south of the latitudes where they usually appear.",
     [", ", "; ", ": ", " and "], "A",
     "The sentence opens with a dependent clause introduced by 'When', and a dependent clause "
     "placed before the main clause is followed by a comma."),

 bnd("B8",
     "The flight had been sold as a gentle hour over the valley, and for most of it that is what it "
     "was. The balloon rose steadily for "
     "forty minutes _____ then the burner went out and the basket dropped nearly a hundred metres "
     "before the pilot could relight it.",
     ["; ", ", ", ": ", " "], "A",
     "'then' is an adverb rather than a coordinating conjunction, so joining these two complete "
     "sentences with nothing but a comma would produce a splice."),

 bnd("B9",
     "Timbuktu stood where the desert trade met the river trade, and its markets handled both. An "
     "inventory drawn up in 1591 lists the goods on which the town's wealth rested _____ salt cut "
     "from the desert mines, gold carried up from the south, and books copied by hand in the town "
     "itself.",
     [": ", "; ", ", but ", " and"], "A",
     "The words before the blank form a complete sentence, and the colon introduces the list that "
     "specifies the goods it refers to."),

 bnd("B10",
     "Documents of this period are rarely dated, so scholars date them from their contents "
     "instead. Although the papyrus fragment carries no date of its own _____ the tax officials "
     "named on the back of it held office for only a few years, which fixes the document to within "
     "a decade.",
     [", ", "; ", ": ", " and "], "A",
     "'Although' opens a dependent clause, and a dependent clause standing before the main clause "
     "is separated from it by a comma."),

 bnd("B11",
     "This is the only lock on the canal still worked entirely by hand, and the keeper lives in the "
     "cottage built beside it. He opened the "
     "upper paddles a little before dawn _____ the barge was through the lock and moored below the "
     "town by noon.",
     ["; ", ", ", ": ", " "], "A",
     "Both halves are complete sentences and no conjunction joins them, so the semicolon is "
     "required; the colon would announce that the second half explains the first, whereas here it "
     "simply reports what happened next."),

 bnd("B12",
     "Saturn's outermost ring is faint, enormously wide, and fed from a source outside the ring "
     "system altogether. Enceladus, a moon barely five "
     "hundred kilometres across _____ vents plumes of water vapour from fractures near its south "
     "pole, and a part of that vapour freezes into the ring.",
     [", ", "; ", ": ", " "], "A",
     "The appositive describing the moon's size opened with a comma, so it must be closed with a "
     "comma before the verb 'vents'."),

 # ------------------------------------------------ Form, Structure, and Sense (9)
 fss("F1",
     "The pottery closed in 1924, and because no catalogue of its output was ever printed, its "
     "wares are now identified by eye alone. Neither the glaze "
     "recipe nor the firing schedules _____ recorded anywhere in the workshop notebooks that "
     "survive.",
     ["was", "were", "has been", "is"], "B",
     "With 'neither ... nor', the verb agrees with the subject nearer to it, and 'the firing "
     "schedules' is plural."),

 fss("F2",
     "Pressed specimens do not photograph well without lighting chosen for the purpose, and the "
     "cabinets holding them are opened as seldom as the curators can manage. The "
     "herbarium's collection of ferns, together with its several thousand lichen specimens, _____ "
     "digitised over the winter, sheet by sheet.",
     ["are", "was", "have been", "were"], "B",
     "The subject is the singular noun 'collection'; the interrupting phrase 'together with its "
     "several thousand lichen specimens' does not make a singular subject plural."),

 fss("F3",
     "Pumping ran for six weeks before anyone was allowed underground again, and the shaft was "
     "still dripping when the survey party went down. By the time the "
     "inspectors reached the tunnel in March, the water that flooded it in January _____ to a "
     "depth of barely two metres.",
     ["falls", "will fall", "had fallen", "is falling"], "C",
     "The fall in the water level was complete before the inspectors arrived, and their arrival is "
     "itself in the past, so the past perfect is what places one past event before another."),

 fss("F4",
     "The telescope's mirror is not a single piece of glass but a mosaic of hexagons, each polished "
     "separately and aligned only once it is in place. Each of the "
     "observatory's four mirror segments _____ its own set of actuators, which adjust the surface "
     "as the instrument tilts.",
     ["have", "has", "having", "were having"], "B",
     "'Each' is singular, and the prepositional phrase naming four segments does not change the "
     "number of the subject."),

 fss("F5",
     "The inquiry ran for two years, took evidence from more than ninety witnesses, and produced a "
     "report that is unusually blunt. The inspectors faulted the shipyard "
     "for using undocumented welds and for _____ the results of the tests it did carry out.",
     ["misreporting", "it misreported", "having misreport", "to misreport"], "A",
     "The two items joined by 'and' both follow the preposition 'for', so 'for using' requires a "
     "matching gerund; a finite clause or an infinitive breaks the parallel structure."),

 fss("F6",
     "The bell tower at the corner of the square looks untouched from the piazza below, and the "
     "guidebooks still describe it as medieval. Having "
     "been rebuilt twice since the earthquake of 1908, the campanile _____ almost nothing of its "
     "original fabric above the foundations.",
     ["retaining", "retains", "to retain", "having retained"], "B",
     "The introductory participial phrase is not a clause, so what follows it must be a main "
     "clause with a finite verb; the participles and the infinitive leave the sentence without "
     "one."),

 fss("F7",
     "The ridge running down the spine of the island splits it into a wet side and a dry one, and "
     "the two halves are farmed quite differently as a result. The annual rainfall recorded at "
     "the station on the windward slope is nearly three times _____ recorded at the station on the "
     "leeward side.",
     ["that", "those", "it", "which"], "A",
     "The pronoun stands in for the singular noun 'rainfall', so the singular form is required; "
     "the plural form would need a plural antecedent and there is none in the sentence."),

 fss("F8",
     "Work on the wreck is done in pairs at a depth of forty metres, in water cold enough to limit "
     "a single dive to twenty minutes. The surface team monitors all "
     "four _____ air supply continuously, and any diver whose gauge falls below a set pressure is "
     "called up at once.",
     ["divers", "diver's", "divers'", "divers's"], "C",
     "The air supply belongs to all four divers, so the noun has to be both plural and possessive, "
     "which puts the apostrophe after the plural ending. The singular possessive would credit the "
     "supply to one diver only."),

 fss("F9",
     "The heating pipes beneath the nave were replaced in 2011, and what had been booked as a "
     "fortnight of plumbing turned into a season of archaeology. Beneath the cathedral floor "
     "_____ the foundations of an earlier church, their "
     "outline cutting clean across the modern aisles.",
     ["lies", "lie", "lying", "has lain"], "B",
     "The subject follows the verb in this inverted sentence, and that subject, 'the "
     "foundations', is plural, so the plural verb is required."),

 # -------------------------------------------------------------- Transitions (9)
 trn("T1",
     "Aerogel is the lightest solid ever manufactured, and a slab of it a centimetre thick "
     "insulates about as well as a course of bricks. _____ it crumbles under the pressure of a "
     "thumbnail, which has kept it out of nearly every building application proposed for it.",
     ["However,", "Therefore,", "Likewise,", "For example,"], "A",
     "The fragility works against the advantages just listed, so the transition has to mark a "
     "contrast rather than a consequence."),

 trn("T2",
     "The eruption of Mount Tambora in 1815 was the largest anywhere in the past thousand years, "
     "and it threw enough ash and sulphur into the stratosphere to dim sunlight across the whole "
     "of the northern hemisphere. _____ farmers in New England recorded frost in "
     "every month of the following summer.",
     ["Nevertheless,", "Consequently,", "By contrast,", "Similarly,"], "B",
     "The frosts follow from the dimming of sunlight described in the first sentence, which is a "
     "cause-and-effect relation and not a contrast."),

 trn("T3",
     "Resurrection plants can lose almost all the water in their tissues and lie dormant for "
     "years, greening again within hours of a rain. _____ brine shrimp lay eggs that survive being "
     "dried out completely and hatch when a desert pool refills.",
     ["Consequently,", "In other words,", "Similarly,", "Nevertheless,"], "C",
     "The second sentence offers a parallel case of surviving complete desiccation in an unrelated "
     "organism, so the transition must signal comparison."),

 trn("T4",
     "Resurfacing the ring road took an entire summer and cut the number of reported potholes by "
     "four fifths within a year of the work being finished. "
     "_____ complaints from drivers about the condition of the road rose over the same period.",
     ["Accordingly,", "Nonetheless,", "Indeed,", "That is,"], "B",
     "Rising complaints are the opposite of what far fewer potholes would lead one to expect, so "
     "the transition has to mark the unexpected turn."),

 trn("T5",
     "A body left in a peat bog can come out two thousand years later with its skin, hair and "
     "stomach contents intact. _____ the same acids that tan the skin dissolve the bones, so the "
     "bodies recovered are often oddly boneless.",
     ["For instance,", "In fact,", "However,", "Thus,"], "C",
     "The loss of the skeleton qualifies the impression of complete preservation given in the "
     "first sentence, so a contrastive transition is what is needed."),

 trn("T6",
     "A SQUID magnetometer exploits the way current behaves across a pair of junctions in a superconducting "
     "ring, and it registers magnetic fields a billion times fainter than the Earth's own. "
     "_____ it can pick up the field generated by the current running along a single human nerve.",
     ["Nevertheless,", "For example,", "In contrast,", "Instead,"], "B",
     "The nerve measurement is an instance of the sensitivity claimed in the first sentence, which "
     "calls for an exemplifying transition."),

 trn("T7",
     "The first submarine telegraph cables had to lie on the seabed for years at a stretch, under "
     "pressure and in the dark, without their insulation cracking or dissolving away. _____ "
     "engineers wrapped the copper core in gutta-percha, "
     "a latex that stays flexible in cold salt water.",
     ["For this reason,", "Even so,", "By comparison,", "In summary,"], "A",
     "The choice of gutta-percha follows directly from the requirement stated before it, so the "
     "transition must express cause."),

 trn("T8",
     "Pollen survives in buried soil for millennia and identifies the plants that were in flower when "
     "the soil was sealed. Pollen taken from inside a Bronze Age burial mound comes almost entirely from meadowsweet "
     "and other plants that flower in high summer. _____ the burial was made somewhere between "
     "June and August.",
     ["Conversely,", "Thus,", "Meanwhile,", "Admittedly,"], "B",
     "The pollen is the evidence and the season of the burial is the conclusion drawn from it, so "
     "the transition must introduce an inference."),

 trn("T9",
     "Desalination plants along the Gulf coast now supply most of the region's drinking water. "
     "_____ the concentrated brine they return to the sea is denser than seawater and sinks, "
     "settling over the seabed and smothering the animals that live in the sediment.",
     ["Unfortunately,", "Likewise,", "For instance,", "In summary,"], "A",
     "The damage done by the brine is a drawback of the solution just described, and the "
     "transition must mark it as an unwelcome complication. The exemplifying option would present "
     "the brine as an instance of the water supplied, which it is not."),

 # ------------------------------------------------------ Rhetorical Synthesis (9)
 syn("R1",
     ["Chinampas are narrow plots built up from lake mud in the shallow water at Xochimilco.",
      "Willows planted along their edges hold the plots together with their roots.",
      "Canals run between the plots on every side.",
      "The soil stays wet without irrigation, and a chinampa can be cropped several times a year."],
     "explain how chinampas stay productive without irrigation.",
     ["Chinampas are narrow plots built up from lake mud in the shallow water at Xochimilco.",
      "Because canals run between the plots on every side, the soil stays wet without irrigation, and a chinampa can be cropped several times a year.",
      "Willows planted along the edges of a chinampa hold the plot together with their roots.",
      "Plots at Xochimilco can be cropped several times in a single year."],
     "B",
     "The stated goal names productivity without irrigation, and only the option that links the "
     "surrounding canals to permanently wet soil and then to repeated cropping supplies both "
     "halves of it. The willow option explains how the plot holds together instead."),

 syn("R2",
     ["A gold-plated copper disc was fixed to each Voyager probe before launch in 1977.",
      "It carries spoken greetings in 55 languages, music and 116 encoded images.",
      "Instructions for playing it are etched on the cover as diagrams.",
      "Both probes have now passed beyond the heliosphere."],
     "emphasise that the record was designed to be understood by a finder who shares no language "
     "with its makers.",
     ["The Voyager probes each carry a gold-plated copper disc fixed to them before launch in 1977.",
      "Since any finder would share no language with the record's makers, the instructions for playing it are etched on the cover as diagrams.",
      "The record carries spoken greetings in 55 languages along with music and images.",
      "Both Voyager probes have now passed beyond the heliosphere."],
     "B",
     "Only the option about the diagrammed instructions speaks to being understood without a "
     "shared language. Greetings in 55 human languages would be of no use whatever to a finder "
     "who speaks none of them, so that option works against the stated goal."),

 syn("R3",
     ["Fog nets are panels of fine mesh strung across ridges on the Chilean coast.",
      "Fog blown against the mesh condenses on the threads and runs down into a gutter.",
      "One large net can yield several hundred litres on a foggy day.",
      "A village in the region has used the nets to supply a small brewery."],
     "explain how a fog net produces water.",
     ["Fog nets are panels of fine mesh strung across ridges on the Chilean coast.",
      "Fog blown against the mesh condenses on the threads and runs down into a gutter, so that one large net yields several hundred litres on a foggy day.",
      "A village on the Chilean coast has used fog nets to supply a small brewery.",
      "Several hundred litres of water can be collected from a single net on a foggy day."],
     "B",
     "The goal asks for the mechanism, and only the option tracing fog to condensation to the "
     "gutter, with the resulting yield attached, describes how the water is actually produced. "
     "The brewery option reports a use rather than a mechanism."),

 syn("R4",
     ["The Bayeux Tapestry is nearly 70 metres long.",
      "It is embroidered in wool on linen rather than woven on a loom.",
      "It depicts the events leading to the Norman conquest of England in 1066.",
      "Halley's Comet, seen in that year, appears among the figures in its border."],
     "correct a common misunderstanding about the object.",
     ["The Bayeux Tapestry is nearly 70 metres long and depicts the events leading to 1066.",
      "Though it is called a tapestry, the object is embroidered in wool on linen rather than woven, so the name is inaccurate.",
      "Halley's Comet appears among the figures embroidered in the border of the tapestry.",
      "The Norman conquest of England, the subject of the work, took place in 1066."],
     "B",
     "The only misunderstanding the notes make available is the name itself, and just one option "
     "sets embroidery against weaving in order to correct it. The comet option is a striking "
     "detail but corrects nothing."),

 syn("R5",
     ["In 1769 observers were sent to Tahiti, to Hudson Bay and to Lapland.",
      "Each timed the passage of Venus across the face of the Sun.",
      "The Sun's distance is calculated by comparing timings taken from widely separated places.",
      "Transits of Venus come in pairs eight years apart and then not again for over a century."],
     "explain why the 1769 expeditions had to be sent so far apart.",
     ["In 1769 observers travelled to Tahiti, to Hudson Bay and to Lapland to watch the transit.",
      "Because the Sun's distance is calculated by comparing timings from widely separated places, observers were sent as far apart as Tahiti and Lapland.",
      "Transits of Venus come in pairs eight years apart and then not again for more than a century.",
      "Each observer timed the passage of Venus across the face of the Sun."],
     "B",
     "The question is why the separation mattered, and only the option joining the method of "
     "calculation to the choice of stations answers it. The rarity of transits explains the "
     "urgency of the expeditions rather than their geography."),

 syn("R6",
     ["The Thames was so foul in the summer of 1858 that Parliament hung lime-soaked curtains at its windows.",
      "Joseph Bazalgette was authorised that year to build a system of intercepting sewers.",
      "The sewers carried waste to outfalls downstream of the city instead of into the central Thames.",
      "Cholera deaths in the districts they served fell sharply afterwards."],
     "explain what the new sewers changed and what followed from the change.",
     ["Parliament hung lime-soaked curtains at its windows during the summer of 1858.",
      "The intercepting sewers carried waste to outfalls downstream of the city rather than into the central Thames, and cholera deaths in the districts they served fell sharply.",
      "Joseph Bazalgette was authorised in 1858 to build a system of intercepting sewers.",
      "The Thames was extremely foul during the summer of 1858."],
     "B",
     "The goal asks for both the change and its consequence, and only the option pairing the "
     "diversion of the waste with the fall in cholera deaths supplies the two together. The "
     "authorisation option names the project without saying what it altered."),

 syn("R7",
     ["Maize, beans and squash are planted together in a single mound.",
      "The maize stalk gives the bean vine something to climb.",
      "Bacteria on the bean roots add nitrogen to the soil.",
      "Broad squash leaves shade the ground and suppress weeds."],
     "explain how the three crops support one another.",
     ["Maize, beans and squash are all planted together in a single mound.",
      "The maize gives the beans something to climb, the beans add nitrogen to the soil through their roots, and the squash leaves shade out the weeds.",
      "Bacteria living on the roots of the bean plants add nitrogen to the soil.",
      "The broad leaves of the squash shade the ground around the mound."],
     "B",
     "Mutual support requires all three contributions to appear, and only the option naming the "
     "stalk, the nitrogen and the shade shows each crop doing something for the others. The "
     "nitrogen option describes one contribution in isolation."),

 syn("R8",
     ["The painted cave at Lascaux was opened to visitors in 1948.",
      "Carbon dioxide and moisture from visitors' breath encouraged algae and crystal growth on the painted surfaces.",
      "The cave was closed to the public in 1963.",
      "A full-size replica opened a short distance away in 1983."],
     "explain why the replica was built.",
     ["A full-size replica of the painted cave opened a short distance from Lascaux in 1983.",
      "Because moisture and carbon dioxide from visitors' breath were damaging the paintings, the cave was closed in 1963 and a full-size replica opened nearby in 1983.",
      "Lascaux was open to visitors for fifteen years, between 1948 and 1963.",
      "Algae and crystals grew over the painted surfaces inside the cave."],
     "B",
     "The reason lies in the damage done by visitors, and only the option carrying the damage, the "
     "closure and the replica together answers the question asked. Simply reporting that a replica "
     "opened supplies the fact without the reason."),

 syn("R9",
     ["Conventional paving sheds rainfall straight into storm drains.",
      "Sponge city designs use permeable paving, constructed wetlands and rooftop planting.",
      "These surfaces absorb rain where it falls and release it slowly.",
      "Trial districts in Wuhan cut peak storm runoff by about half."],
     "convey how effective the approach has proved.",
     ["Sponge city designs use permeable paving, constructed wetlands and rooftop planting.",
      "Permeable surfaces absorb rain where it falls and then release it slowly.",
      "By absorbing rain where it falls, trial districts in Wuhan cut peak storm runoff by about half.",
      "Conventional paving sheds rainfall straight into the storm drains."],
     "C",
     "Effectiveness needs the measured outcome, and only the option reporting the halving of peak "
     "runoff in the Wuhan trial districts provides one. The other options describe the design "
     "without saying what it achieved."),
]

DROPPED = {}
