#!/usr/bin/env python3
"""
Reading & Writing authored for Test 9.

All 81 items are written here: the transcribed pool was exhausted by Test 8, and
authoring is in any case the more reliable route for R&W, since a transcribed
answer key has to be re-derived by hand before it can be trusted (Test 5 shipped
6 wrong answers in 81 that way). Every item below carries a `why` recording the
reasoning that produced the key and the reason the strongest distractor fails —
that record IS the verification, so no key exists here without one.

Rationales name options by their CONTENT, never by letter, so balance_rw.py is
free to rotate every question when it evens out the key distribution.

Passages are original prose, 40-110 words, and topics are deliberately spread
across science, history, art, technology and social science. Nothing here shares
a topic with rw_test8.py — that file was read in full first and its subjects
(octopuses, Ruth Asawa, Hertha Ayrton, Gutenberg, lichens, Florence Price,
bowerbirds, Roman concrete, sea otters, Marie Tharp, mangroves, Ada Lovelace,
Antikythera, cochineal, emperor penguins, Hedy Lamarr and the rest) are avoided.
"""

SOURCE = "AUTHORED-T9"
MODULE = "RW"


def wic(num, passage, choices, answer, why):
    return dict(num=num, skill="Words in Context", passage=passage,
                stem="Which choice completes the text with the most logical and precise word or phrase?",
                choices=choices, answer=answer, why=why)


def wicw(num, word, passage, choices, answer, why):
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


def rsy(num, passage, stem, choices, answer, why):
    return dict(num=num, skill="Rhetorical Synthesis", passage=passage,
                stem=stem, choices=choices, answer=answer, why=why)


QUESTIONS = [

 # ==================================================== Words in Context (15)
 wic("W1", "The dishes of the array are spread across two hundred kilometres of desert, so the "
           "signals they collect must be combined with _____ timing: an error of a few "
           "nanoseconds smears the finished image beyond any use.",
     ["approximate", "exacting", "flexible", "occasional"], "B",
     "Tolerances measured in nanoseconds are the definition of demanding accuracy, so the word "
     "must mean 'extremely precise'. The 'approximate' option is what the sentence rules out, "
     "since approximation is exactly what would smear the image."),
 wic("W2", "The pianist's late recordings are admired above all for their _____: a phrase begins "
           "where the listener expects silence, and it stops several beats before the line seems "
           "finished.",
     ["unpredictability", "precision", "warmth", "brevity"], "A",
     "Both examples given describe the music defeating what the listener expects, which is "
     "unpredictability. The 'precision' option names accuracy, but nothing in the sentence "
     "measures how exactly the notes are played."),
 wic("W3", "Narrowing the city's widest avenue was expected to choke it with traffic. Instead the "
           "number of vehicles using the corridor fell, a result that _____ the assumption that "
           "drivers simply fill whatever road space they are given.",
     ["confirmed", "upended", "measured", "predicted"], "B",
     "The outcome is the opposite of what was expected, so the verb must mean 'overturned'. The "
     "'confirmed' option reverses the logic the sentence has just set up with 'Instead'."),
 wic("W4", "Amber preserves what rock cannot. A wing membrane caught in resin a hundred million "
           "years ago can remain _____, down to the individual hairs along its trailing edge, "
           "while the same structure in mudstone survives only as a stain.",
     ["compressed", "intact", "altered", "enlarged"], "B",
     "The contrast with a mere stain, plus the surviving individual hairs, calls for a word "
     "meaning undamaged and complete. The 'compressed' option describes what flattening in rock "
     "does, which is the fate the sentence contrasts amber with."),
 wic("W5", "The programme's first evaluations were _____: borrowers repaid at rates the designers "
           "had not dared hope for, yet household incomes in the villages served rose no faster "
           "than in villages that received nothing at all.",
     ["mixed", "damning", "conclusive", "enthusiastic"], "A",
     "One clearly good result and one clearly disappointing one is a divided verdict. The "
     "'damning' option ignores the repayment rates, which the sentence presents as a success."),
 wic("W6", "A kintsugi repairer does not hide the break. Filling the crack with lacquer and dusting "
           "it with gold makes the damage the most _____ feature of the finished bowl, the first "
           "thing the eye follows.",
     ["conspicuous", "fragile", "valuable", "recent"], "A",
     "'The first thing the eye follows' is about visibility, so the word must mean noticeable. "
     "The 'valuable' option is tempting because gold is mentioned, but the sentence measures "
     "attention, not worth."),
 wic("W7", "Fragments of the virus turn up in a city's sewage several days before patients turn up "
           "in its clinics. Sampling wastewater therefore gives public health officials _____ "
           "warning of an outbreak that case counts cannot match.",
     ["belated", "advance", "ambiguous", "reluctant"], "B",
     "The sewage signal arrives days ahead of the clinical one, so the warning comes early. The "
     "'belated' option inverts the timing the first sentence establishes."),
 wic("W8", "The wind towers of Yazd cool the rooms beneath them without a moving part or a watt of "
           "electricity. Architects working in hot climates have begun to treat the design not as a "
           "picturesque survival but as a _____ answer to a present problem.",
     ["viable", "decorative", "temporary", "traditional"], "A",
     "The contrast is with a 'picturesque survival', so the word must assert present usefulness. "
     "The 'traditional' option restates the idea being rejected rather than opposing it."),
 wic("W9", "Deaf children brought together at a new school invented a shared sign system within a "
           "few years. Each entering cohort then made it more _____, adding a consistent word order "
           "and grammatical markers that the first signers had managed without.",
     ["elaborate", "informal", "widespread", "ancient"], "A",
     "Added word order and grammatical markers are additions to the system's internal complexity. "
     "The 'widespread' option describes how far a language travels, which the sentence never "
     "addresses."),
 wic("W10", "Runners who set out faster than the pace they trained at almost always _____ over the "
            "final third of the race, surrendering more time than their early lead ever gained them.",
     ["accelerate", "falter", "recover", "persist"], "B",
     "Surrendering time in the last third means slowing badly. The 'persist' option would mean "
     "holding the pace, which contradicts the time lost."),
 wic("W11", "Continuity editing is built to be _____. The cut from one shot to the next succeeds "
            "precisely when the viewer, absorbed in the scene, never registers that it happened.",
     ["invisible", "abrupt", "expressive", "deliberate"], "A",
     "The cut succeeds when nobody registers it, so the word must mean unseen. The 'deliberate' "
     "option is true of any editing choice and fails to capture the going-unnoticed the sentence "
     "makes the criterion of success."),
 wic("W12", "The waggle dance of a honeybee is astonishingly _____: the angle of the straight run "
            "encodes the direction of the food relative to the sun, and the length of the run "
            "encodes the distance to within a few metres.",
     ["ornamental", "informative", "laborious", "erratic"], "B",
     "Direction and distance encoded in one movement is a transfer of information. The 'erratic' "
     "option contradicts the regular encoding the sentence spells out."),
 wicw("W13", "check",
      "Restored wetlands do not stop a flood so much as slow one. Water spreading across marsh "
      "grass moves at a fraction of the speed it reaches in a straightened channel, and that "
      "delay is often enough to check a surge before it reaches the town downstream.",
      ["To verify.", "To restrain.", "To mark with a tick.", "To inspect closely."], "B",
      "The object of the verb is a surge of water and the mechanism given is slowing it, so the "
      "sense is holding something back. The 'verify' sense is the commonest meaning of the word "
      "but makes no sense applied to moving water."),
 wicw("W14", "coin",
      "No term in the literature fitted what the geologist had found, so she had to coin one. The "
      "word she settled on, welded together from two Greek roots, struck her colleagues as ugly "
      "at first and now appears in every textbook on the subject.",
      ["To invent.", "To mint as currency.", "To translate.", "To borrow from another field."], "A",
      "The sentence says no existing term fitted, so she made a new one, and the next sentence "
      "describes her building it from roots. The 'borrow from another field' option is ruled out "
      "by the absence of any existing term."),
 wic("W15", "The two surviving accounts of the retreat were written by officers who had fought on "
            "opposite sides and who agreed on nothing else. Their agreement about the hour the "
            "line broke is therefore especially _____.",
     ["suspicious", "persuasive", "incidental", "ambiguous"], "B",
     "Witnesses with opposing interests who nonetheless agree are unlikely to be repeating each "
     "other's bias, so the agreement carries extra weight. The 'suspicious' option would fit "
     "witnesses who had colluded, which is the opposite of the situation described."),

 # ========================================= Text Structure and Purpose (6)
 tsp("S1",
     "In 1977 Wangari Maathai began paying rural Kenyan women a small sum for every tree seedling "
     "that was still alive a year after it went into the ground. <u>The scheme was built around a "
     "fact that professional forestry programmes had consistently overlooked: planting a tree is "
     "cheap, and keeping it alive is not.</u> Payment on survival put the cost where the "
     "difficulty was. Within three decades the women of the Green Belt Movement had established "
     "more than thirty million trees.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It identifies the insight on which the programme described was built.",
      "It questions whether the programme's results were accurately counted.",
      "It contrasts Maathai's planting techniques with those of professional foresters.",
      "It explains why rural women were willing to take part in the programme."],
     "A",
     "The underlined sentence names the overlooked fact about survival, and the following sentence "
     "says the payment structure was designed around it, so it supplies the reasoning behind the "
     "scheme. The 'contrasts techniques' option misreads the mention of forestry programmes, which "
     "appear only as parties who missed the point, never as a rival method."),
 tsp("S2",
     "Zero appears on Babylonian tablets as a placeholder, a wedge marking an empty column so that "
     "one numeral could not be mistaken for another. What Brahmagupta set down in 628 was something "
     "else: rules for adding zero, subtracting it and multiplying by it, which treat it as a "
     "quantity in its own right. The symbol was old. Granting it the standing of a number was not.",
     "Which choice best states the main purpose of the text?",
     ["To trace the route by which the zero symbol travelled from Babylon to India.",
      "To distinguish an earlier use of zero from a later and more consequential one.",
      "To argue that Babylonian mathematics has been unfairly neglected by historians.",
      "To set out the arithmetical rules that Brahmagupta proposed."],
     "B",
     "The text presents two uses of zero and closes by naming what separates them, which is the "
     "shift from placeholder to number. The 'set out the rules' option mistakes evidence for "
     "purpose: the rules are cited only to show that zero was being treated as a quantity."),
 tsp("S3",
     "<u>A desert is defined by what falls on it, not by how hot it gets.</u> The interior of "
     "Antarctica receives less precipitation in a year than the central Sahara, and by the standard "
     "meteorological criterion it is the largest desert on the planet. Aridity, not temperature, "
     "is what the category records.",
     "Which choice best describes the function of the underlined sentence?",
     ["It states a principle that the rest of the text illustrates and then restates.",
      "It concedes a point that the text goes on to dispute.",
      "It offers an example of a category that the text defines later.",
      "It summarises a disagreement among geographers."],
     "A",
     "The opening asserts the rainfall criterion, the middle sentence gives Antarctica as the "
     "illustration, and the last sentence repeats the criterion in other words. The 'concedes a "
     "point' option fails because nothing in the text disputes the opening claim."),
 tsp("S4",
     "A NASA satellite had been measuring ozone over Antarctica for years. So had three men on the "
     "ground at Halley Bay, using a spectrophotometer older than either of the junior operators. "
     "When the ground readings began to drop, the satellite showed nothing unusual. The discrepancy "
     "was eventually traced to the processing software, which had been written to discard readings "
     "that fell below a plausible threshold and had been quietly throwing the lowest values away.",
     "Which choice best describes the overall structure of the text?",
     ["It describes two sources of data, notes a disagreement between them, and explains its cause.",
      "It criticises the design of a satellite instrument and proposes a replacement for it.",
      "It presents a hypothesis and reviews the evidence gathered for and against it.",
      "It compares the cost of satellite monitoring with that of ground monitoring."],
     "A",
     "Three moves in order: two measurement programmes, a conflict between their results, and the "
     "software behaviour that produced the conflict. The 'criticises the instrument' option "
     "misplaces the fault, which the text puts in the processing software rather than the hardware, "
     "and no replacement is ever proposed."),
 tsp("S5",
     "A camera can read a faded lane marking that radar cannot see at all; radar can measure the "
     "closing speed of a car ahead that a camera can only estimate. <u>Combining the two does not "
     "simply add their strengths together, because the systems contradict each other often enough "
     "that deciding which to believe becomes a design problem in itself.</u> Most manufacturers now "
     "weight each sensor according to how reliable it has proved in the conditions of the moment.",
     "Which choice best describes the function of the underlined sentence?",
     ["It qualifies the advantage implied by the previous sentence and sets up the response described next.",
      "It provides evidence that cameras are more reliable than radar in most conditions.",
      "It defines a technical term that was introduced earlier in the text.",
      "It restates the previous sentence in more general language."],
     "A",
     "The sentence checks the assumption that two complementary sensors combine straightforwardly, "
     "and the closing sentence gives the industry's answer to the difficulty it raises. The "
     "'restates the previous sentence' option fails because it introduces a new problem rather "
     "than repeating the comparison."),
 tsp("S6",
     "A tree lays down one growth ring a year, so a beam cut from an old trunk carries a record of "
     "the seasons it lived through. Matching the pattern of wide and narrow rings in that beam "
     "against a master sequence built from other timbers can fix the year the tree was felled. The "
     "method delivers this precision only where a master sequence already exists for the species "
     "and region in question, which is why it has transformed the archaeology of the American "
     "Southwest and barely touched that of the humid tropics.",
     "Which choice best states the main purpose of the text?",
     ["To describe a dating method and identify the condition that limits where it can be used.",
      "To argue that tree-ring dating is more accurate than radiocarbon dating.",
      "To explain why trees in the humid tropics grow without visible rings.",
      "To recount how tree-ring dating was first discovered."],
     "A",
     "The first two sentences explain how ring-matching dates a timber and the last names the "
     "requirement for a master sequence that restricts its reach. The 'tropics grow without rings' "
     "option supplies a cause the text never states; the limit given is the absence of a reference "
     "sequence, not the absence of rings."),

 # ========================================== Central Ideas and Details (6)
 cid("C1",
     "The Namib is among the driest places on earth, yet fog rolls in off the cold Atlantic on most "
     "mornings. Certain darkling beetles climb the dune crests before dawn and tilt their bodies "
     "into the incoming air. Droplets condense on their backs, run down grooves in the wing cases "
     "and arrive at the mouth. The insects meet nearly all their water needs from air that almost "
     "never falls as rain.",
     "Which choice best states the main idea of the text?",
     ["Darkling beetles obtain the water they need from fog rather than from rainfall.",
      "The Namib receives more moisture than other deserts at a similar latitude.",
      "Darkling beetles are the only animals capable of surviving in the Namib.",
      "Fog is more frequent on the Namib coast than it is inland."],
     "A",
     "Every sentence builds to the last one, which says the beetles get nearly all their water from "
     "fog in a place where rain almost never falls. The 'only animals' option asserts an exclusivity "
     "the text never claims."),
 cid("C2",
     "Nutrients in Amazonian soil are washed out almost as fast as decay releases them, which makes "
     "the forest's productivity a long-standing puzzle. Part of the answer arrives from an unlikely "
     "direction. Dust lifted from a dried lake bed in Chad crosses the Atlantic every year, and the "
     "phosphorus it carries settles over the basin. Satellite estimates put the annual delivery at "
     "roughly the quantity the rivers carry away.",
     "According to the text, what role does Saharan dust play in the Amazon?",
     ["It replaces phosphorus that is washed out of the basin's soil.",
      "It reduces rainfall over the basin by scattering incoming sunlight.",
      "It supplies most of the nitrogen the basin's trees require.",
      "It settles into the rivers and is eventually carried out to sea."],
     "A",
     "The text names phosphorus specifically and says the amount arriving roughly matches the amount "
     "the rivers remove, which is replacement. The 'nitrogen' option swaps in an element the text "
     "never mentions."),
 cid("C3",
     "The bronzes excavated at Igbo-Ukwu in south-eastern Nigeria were cast by the lost-wax method "
     "in the ninth century, centuries before the technique is documented at Ife or Benin. Their "
     "surfaces carry insects and knotted cords rendered so finely that early European scholars "
     "assigned them a much later date, on the assumption that work of that quality required contact "
     "with Portuguese traders. Radiocarbon dates from the site made the assumption untenable.",
     "Which choice best states the main idea of the text?",
     ["The Igbo-Ukwu bronzes are older than assumptions about outside contact allowed for.",
      "Lost-wax casting was invented independently in several parts of Africa.",
      "The Igbo-Ukwu bronzes are more finely made than those of Ife or Benin.",
      "Portuguese traders introduced bronze casting to west Africa."],
     "A",
     "The text sets a ninth-century date against a scholarly assumption that tied the work to much "
     "later European contact, and says radiocarbon settled it against the assumption. The 'more "
     "finely made than Ife or Benin' option invents a comparison of quality; the only comparison "
     "made with those centres is one of date."),
 cid("C4",
     "The high-yielding wheat varieties introduced across South Asia in the 1960s roughly doubled "
     "harvests within a decade. They also depended on irrigation and on fertiliser bought each "
     "season, neither of which the smallest holdings could reliably afford. In several districts "
     "the gap in income between large and small farms widened as the new seed spread. The gains in "
     "output were real, and so was the unevenness in who collected them.",
     "According to the text, what happened in several districts as the new wheat spread?",
     ["The income gap between large and small farms grew wider.",
      "Harvests on the smallest farms fell below their earlier levels.",
      "Fertiliser became cheaper as more farmers began to buy it.",
      "Farmers abandoned the new varieties and returned to older seed."],
     "A",
     "The third sentence states the widening gap between large and small farms in so many words. "
     "The 'harvests fell' option overstates the text, which says small farms could not always "
     "afford the inputs, never that their output declined."),
 cid("C5",
     "Corals bleach when heat drives out the algae that live in their tissue and feed them. Some "
     "colonies on reefs in the southern Red Sea, where summer water already runs hotter than "
     "temperatures that kill corals elsewhere, host an unusual strain of algae instead. Transplant "
     "experiments have now settled where the tolerance resides: colonies given the unusual strain "
     "survive temperatures that bleach their untreated neighbours on the same reef.",
     "According to the text, what do the transplant experiments show?",
     ["The heat tolerance of these colonies comes from the strain of algae they host.",
      "Red Sea corals belong to a species distinct from corals elsewhere.",
      "Bleached corals can recover if the water cools quickly enough.",
      "The algae survive better outside coral tissue than within it."],
     "A",
     "Colonies that receive the unusual strain survive heat that bleaches their neighbours, so the "
     "tolerance travels with the algae. The 'distinct species' option would locate the tolerance in "
     "the coral, which is precisely what the transplant result rules out."),
 cid("C6",
     "The Domesday survey of 1086 recorded who held each manor in England, how many ploughs worked "
     "its land, and what the holding was worth. It is the most complete administrative record to "
     "survive from eleventh-century Europe, and it is also a partial one: it omits London and "
     "Winchester, passes over most of the far north, and counts households rather than people. "
     "Historians use it constantly and qualify it constantly.",
     "Which choice best states the main idea of the text?",
     ["The Domesday survey is an unusually rich record whose omissions have to be allowed for.",
      "The Domesday survey is too incomplete to be of much use to historians.",
      "The Domesday survey was compiled chiefly to assess the wealth of London.",
      "The Domesday survey counted every person then living in England."],
     "A",
     "The closing sentence gives both halves at once: constant use and constant qualification. The "
     "'too incomplete to be of much use' option keeps only the qualification and drops the "
     "'most complete record to survive' the text insists on."),

 # ============================================= Command of Evidence (9)
 coe("E1",
     "Rails, a family of ground-dwelling birds, have lost the power of flight repeatedly on remote "
     "islands. One biologist argues that flight was abandoned because the islands held no mammalian "
     "predators, so the metabolic cost of maintaining flight muscle no longer bought anything. A "
     "rival account attributes the loss to island size: on a small island, a bird that took off was "
     "liable to be carried out to sea and never return.",
     "Which finding, if true, would most directly support the first biologist's explanation over the rival one?",
     ["Flightless rails occur on islands of widely varying size, but only on islands that lacked mammalian predators.",
      "Flightless rails have smaller flight muscles than their flying relatives on the mainland.",
      "Storms are more frequent around remote oceanic islands than along continental coasts.",
      "Rails reached most of these islands within the last two million years."],
     "A",
     "Island size varies across the flightless populations while predator absence holds for all of "
     "them, which is exactly the pattern that separates the two accounts and favours the predator "
     "explanation. The 'smaller flight muscles' option is predicted equally by both accounts, since "
     "flightlessness produces reduced muscle whatever caused it."),
 coe("E2",
     "A pottery style with a distinctive cord-impressed rim appears at settlement after settlement "
     "across a river valley over the course of a century. An archaeologist argues that the style "
     "spread through trade and imitation between established communities rather than through the "
     "arrival of a new population.",
     "Which finding, if true, would most directly support the archaeologist's argument?",
     ["Ancient DNA from burials in the valley shows no change in ancestry across the century in question.",
      "The style eventually appears at every settlement in the valley.",
      "The clay in the pots was quarried locally at each settlement where they are found.",
      "Pots in the new style are more durable than the pots they replaced."],
     "A",
     "Unchanged ancestry through the period rules out the incoming-population explanation and leaves "
     "transmission between existing communities. The 'clay quarried locally' option cannot decide "
     "the question, since potters who had newly arrived would also dig the clay under their feet."),
 coe("E3",
     "Roadside nitrogen dioxide in one European capital fell sharply in the three years after it "
     "introduced a congestion charge. A transport economist attributes the fall to the charge. "
     "Others point out that the oldest diesel vehicles were leaving the national fleet over the "
     "same period, and attribute the fall to that turnover instead.",
     "Which finding, if true, would most directly support the economist's attribution?",
     ["Neighbouring cities whose fleets turned over at the same rate, but which imposed no charge, recorded no comparable fall.",
      "Nitrogen dioxide fell further in the second year of the charge than in the first.",
      "The charge reduced the number of vehicles entering the central zone on a typical weekday.",
      "Diesel engines emit more nitrogen dioxide per kilometre than petrol engines do."],
     "A",
     "Matching the fleet turnover and varying only the charge isolates the charge as the difference "
     "that matters. The 'reduced the number of vehicles' option shows the charge worked on traffic "
     "but leaves open whether the pollution fall came from that or from the cleaner fleet."),
 coe("E4",
     "The opening miniature of a fifteenth-century psalter has long been described as the work of "
     "two painters, one to each half of the page. A conservator now argues that a single hand "
     "painted both halves, pointing to an unusual technique for laying in shadow (short strokes "
     "worked wet into wet) that appears identically on either side of the join.",
     "Which finding, if true, would most directly weaken the conservator's argument?",
     ["Apprentices in the workshop that produced the psalter were trained to lay in shadow exactly as the master did.",
      "The two halves of the miniature use blue pigment from the same mineral source.",
      "The psalter was bound within a year of the miniature's completion.",
      "Shadow technique varied widely between workshops in this period."],
     "A",
     "The argument depends on the shadow technique being personal to one painter. If every "
     "apprentice in the shop was taught the same stroke, the shared technique no longer points to a "
     "single hand. The 'varied widely between workshops' option cuts the other way, since it makes "
     "the technique more distinctive rather than less."),
 coe("E5",
     "A cod population inside a marine reserve has roughly tripled in the fifteen years since "
     "fishing there was banned. A fisheries scientist attributes the recovery to the ban. A "
     "colleague notes that the same fifteen years included an unusual run of warm springs "
     "favourable to cod spawning, and attributes the recovery to that instead.",
     "Which finding, if true, would most directly support the scientist's attribution?",
     ["Cod stocks in the same warm waters immediately outside the reserve did not recover over the period.",
      "Cod inside the reserve now grow to a greater average length than cod outside it.",
      "The run of warm springs began in the reserve's first year of operation.",
      "Fishing effort outside the reserve increased after the reserve was established."],
     "A",
     "Waters just outside the reserve were equally warm, so a recovery inside and none outside "
     "isolates the fishing ban. The 'warm springs began in the first year' option is if anything "
     "help for the rival account, since it makes the two explanations run in step."),
 coe("E6",
     "People recall a list of words better after a night's sleep than after an equal period awake. "
     "One researcher proposes that this is because the sleeping brain actively replays and "
     "consolidates what was learned. A simpler explanation is available: a sleeper encounters "
     "nothing new, so nothing interferes with the memory in the interval.",
     "Which finding, if true, would most directly support the researcher's proposal?",
     ["Participants kept awake in a dark, silent room for the interval still recall less than participants allowed to sleep.",
      "Participants who sleep for eight hours recall more than participants who sleep for four.",
      "Recall is worse when participants learn a second list immediately before sleeping.",
      "Participants often report dreaming about the material they have learned."],
     "A",
     "The dark silent room removes interfering experience without providing sleep, so a remaining "
     "advantage for sleep cannot be explained by interference and points to something the sleeping "
     "brain does. The 'eight hours versus four' option is predicted by both accounts, since longer "
     "sleep is also a longer stretch free of interference."),
 coe("E7",
     "A road nine metres wide runs in a straight line for twenty kilometres from a pueblo to an "
     "isolated shrine in a side canyon. It is far wider than the footpaths that link the region's "
     "other settlements, and it was surfaced and kerbed along its whole length. An archaeologist "
     "who has surveyed it argues that it was built for formal processions to the shrine rather "
     "than for the everyday movement of goods.",
     "Which finding, if true, would most directly support the archaeologist's argument?",
     ["The road holds its width and bearing straight across ridges that a loaded traveller would have walked around.",
      "The road is wider than any other prehistoric road known in the region.",
      "Pottery made at the pueblo has been found in quantity at the shrine.",
      "The road was built in stages across several generations."],
     "A",
     "Refusing to detour around ridges is costly for anyone carrying a load and makes sense only if "
     "the line itself mattered, which is what a processional route implies. The 'pottery at the "
     "shrine' option supports the rival reading, since it shows goods did travel to the shrine."),
 coe("E8",
     "A farm's maize yield rose eighteen percent in a single season. The farmer had made two "
     "changes that year: winter cover crops were sown for the first time, and the irrigation "
     "schedule was shifted from weekly to daily. An agronomist attributes the gain to the cover "
     "crops.",
     "Which finding, if true, would most directly support the agronomist's attribution?",
     ["Neighbouring farms that adopted the same daily irrigation schedule without sowing cover crops recorded no yield gain.",
      "Cover crops are known to increase the organic matter in soil.",
      "The farm's yield rose again, by a smaller margin, in the following season.",
      "Rainfall during the growing season was close to the long-term average."],
     "A",
     "Neighbours who changed the irrigation but not the cover crops and gained nothing show that "
     "irrigation alone does not produce the effect, leaving the cover crops. The 'increase organic "
     "matter' option gives a plausible mechanism but says nothing about which of this farm's two "
     "changes actually produced its gain."),
 coe("E9",
     "A fishing community on an offshore island has kept a vowel system that disappeared from the "
     "mainland dialect two centuries ago. A sociolinguist argues that the system survived because "
     "contact with mainland speakers was rare, rather than because islanders deliberately maintained "
     "it as a badge of local identity.",
     "Which finding, if true, would most directly support the sociolinguist's argument?",
     ["Islanders asked about their vowels are unaware that they differ from those of mainland speakers.",
      "Older islanders use the vowel system more consistently than younger ones do.",
      "The island could be reached only by boat until a causeway was built in the 1970s.",
      "Comparable vowel systems survive in two other island communities."],
     "A",
     "Speakers cannot be deliberately maintaining a feature as a badge of identity if they do not "
     "know the feature marks them out, so unawareness removes the rival account. The 'reachable "
     "only by boat' option establishes the isolation but is compatible with both explanations, since "
     "an isolated community could still be maintaining the feature on purpose."),

 # ================================================== Inferences (6)
 inf("I1",
     "A tardigrade can be dried to a few percent of its normal water content and survive. The water "
     "it loses is replaced by a sugar that vitrifies as it dries, holding the cell's structures in "
     "place as though set in glass. In this state the animal is not merely living slowly: its "
     "metabolism has stopped altogether. Records of tardigrades revived after decades of storage "
     "therefore say little about _____",
     ["how long the species lives, since the dried years are not years of living.",
      "how the sugar keeps the cell's structures from collapsing.",
      "how quickly the animals take up water again when it returns.",
      "whether other invertebrates can be dried without being harmed."],
     "A",
     "The passage stresses that metabolism stops entirely while the animal is dried, so time spent "
     "in that state cannot be counted as time spent alive and a revival record measures storage "
     "rather than lifespan. The 'how the sugar works' option names something the passage has already "
     "explained, so it is not what those records fail to tell us."),
 inf("I2",
     "Maize cobs recovered from a rock shelter in the Tehuac&aacute;n valley are barely five "
     "centimetres long and carry eight rows of small kernels; they date to roughly 5,000 years ago. "
     "Teosinte, the wild grass from which maize descends, bears a handful of kernels in a single "
     "row. A cob bought in a market today carries several hundred kernels in a dozen or more rows. "
     "The rock-shelter cobs suggest that by 5,000 years ago maize _____",
     ["had been changed substantially from its wild ancestor but had not yet reached its modern form.",
      "was already almost indistinguishable from the maize grown today.",
      "was cultivated only within the Tehuac&aacute;n valley.",
      "had not yet been brought under deliberate cultivation."],
     "A",
     "Eight rows is far beyond teosinte's single row and far short of today's dozen or more, so the "
     "cobs sit between the two states. The 'not yet cultivated' option cannot be right, because the "
     "departure from teosinte is itself the evidence of selection."),
 inf("I3",
     "A city made evening bus travel free from the first of October and reported a twelve percent "
     "rise in evening ridership by the end of December. Ridership on this network climbs every "
     "autumn as daylight shortens and cycling falls away; over the previous three years the average "
     "rise from October to December was nine percent. Taken on its own, the twelve percent figure "
     "therefore _____",
     ["overstates the increase that can be credited to the fare change.",
      "shows that the fare change had no effect on ridership at all.",
      "cannot meaningfully be compared with figures from earlier years.",
      "understates how many riders gave up cycling during the period."],
     "A",
     "Nine of the twelve points would have arrived with the season anyway, so crediting the whole "
     "twelve to the fare change inflates it. The 'no effect at all' option overshoots: three points "
     "above the seasonal norm is a residual, not a zero."),
 inf("I4",
     "The transit method detects a planet by the dip in a star's brightness as the planet crosses "
     "in front of it. A large planet on a short orbit produces dips that are both deep and "
     "frequent, and a survey can confirm one within a few months. A small planet on a wide orbit may "
     "transit once a decade, and by an amount at the edge of what current instruments can resolve. "
     "Catalogues assembled from transit surveys therefore _____",
     ["overrepresent large, close-orbiting planets relative to their true abundance.",
      "contain no planets smaller than Earth.",
      "are reliable only for stars brighter than the sun.",
      "show that most planetary systems closely resemble our own."],
     "A",
     "The method finds one kind of planet easily and the other barely at all, so the resulting "
     "catalogue is skewed towards what is easy to see. The 'no planets smaller than Earth' option "
     "goes too far: the passage says such transits are hard to resolve, not that none has ever been "
     "detected."),
 inf("I5",
     "The panel is signed and dated 1631. Analysis of its ground layer, however, has identified a "
     "synthetic ultramarine first manufactured in the 1820s, and the pigment appears not in a patch "
     "of retouching but distributed evenly through the preparatory layer beneath the paint. Unless "
     "the analysis is mistaken, the panel _____",
     ["cannot have been prepared before the nineteenth century.",
      "was retouched at some point after the 1820s.",
      "was painted by an artist other than the one whose signature it bears.",
      "was catalogued incorrectly by a later owner."],
     "A",
     "Pigment that did not exist until the 1820s, spread through the preparation the painting sits "
     "on, dates the preparation no earlier than that decade. The 'retouched' option is closed off "
     "explicitly, since the passage says the pigment is in the ground layer and not in retouching."),
 inf("I6",
     "Students who study a set of terms in four short sessions spread across two weeks remember more "
     "of them a month later than students who spend the same total time in a single sitting. Asked "
     "straight afterwards which approach felt more effective, the single-sitting students report the "
     "greater confidence, because material worked through in one block feels fluent while it is "
     "still fresh. A student who selects a study method by how well it feels to be working _____",
     ["will tend to choose the method that leaves less in memory a month later.",
      "will end up spending more total time studying than is necessary.",
      "will remember more of the terms after a month than other students do.",
      "is unlikely to notice any difference between the two methods."],
     "A",
     "The method that feels better is the massed one, and the massed one is the method that produces "
     "the weaker month-later recall, so choosing on felt effectiveness selects against retention. "
     "The 'notice no difference' option contradicts the passage, which reports that the two "
     "conditions differ in reported confidence."),

 # ================================================== Boundaries (12)
 bnd("B1", "The mycologist catalogued more than four hundred specimens in a single field season "
           "_____ fewer than a dozen had ever been recorded in the region before her survey began.",
     ["; ", ", ", " ", ": and"], "A",
     "Two independent clauses joined by no coordinating conjunction take a semicolon; the bare "
     "comma would produce a comma splice."),
 bnd("B2", "After the reservoir was drained so that the dam could be repaired _____ the outline of "
           "the drowned village reappeared in the mud.",
     [", ", "; ", ": ", " and "], "A",
     "The introductory dependent clause beginning 'After' is separated from the main clause by a "
     "comma; a semicolon would wrongly imply an independent clause on its left."),
 bnd("B3", "The tin contains everything needed for a first repair _____ a spool of solder, a length "
           "of shrink tubing and a spare fuse.",
     [": ", "; ", ", and ", " which is"], "A",
     "The colon introduces the list that specifies the 'everything' announced by the complete "
     "clause standing before it."),
 bnd("B4", "Zheng He, the admiral who commanded seven voyages across the Indian Ocean _____ sailed "
           "with fleets larger than any Europe would launch for the next three centuries.",
     [", ", "; ", ": ", " "], "A",
     "The appositive 'the admiral who commanded seven voyages' was opened with a comma and must be "
     "closed with one before the verb 'sailed'."),
 bnd("B5", "The redesigned kiln fires at a lower temperature _____ it also produces a glaze that "
           "resists crazing.",
     [", and ", ", ", "; also ", " "], "A",
     "Two independent clauses may be joined by a comma plus the coordinating conjunction 'and'; "
     "the comma on its own would splice them."),
 bnd("B6", "Divers brought up timbers, rigging blocks and a single leather shoe _____ all of which "
           "were waterlogged and had to be stabilised before they could be allowed to dry.",
     [", ", "; ", ": ", ". "], "A",
     "'all of which' opens a non-essential relative clause, which attaches with a comma; a "
     "semicolon would require a complete independent clause after it."),
 bnd("B7", "Whenever the river drops below its summer minimum _____ the mill wheel stops turning "
           "altogether.",
     [", ", "; ", ": ", " that "], "A",
     "The dependent clause opening with 'Whenever' comes before the main clause and is followed "
     "by a comma."),
 bnd("B8", "The kite balloon rose steadily for forty minutes _____ then, with no change in the wind "
           "that anyone on the ground could detect, it began to sink.",
     ["; ", ", ", ": ", " "], "A",
     "'then' is an adverb rather than a coordinating conjunction, so a comma between these two "
     "independent clauses would be a splice; the semicolon is required."),
 bnd("B9", "Three ingredients give the stew its colour _____ saffron, smoked paprika and the fat "
           "rendered out of the sausage.",
     [": ", "; ", ", but ", " and"], "A",
     "The complete clause is followed by a colon introducing the list that names the three "
     "ingredients it has just promised."),
 bnd("B10", "Though the score survives only in a copyist's hand _____ the corrections crowded into "
            "its margins are almost certainly the composer's own.",
     [", ", "; ", ": ", " and "], "A",
     "'Though' opens a dependent clause, which is separated from the main clause that follows it "
     "by a comma."),
 bnd("B11", "The vaccination team reached the last village in the district in March _____ the "
            "outbreak was declared over in July.",
     ["; ", ", ", ": ", " "], "A",
     "Two independent clauses with no conjunction between them require the semicolon."),
 bnd("B12", "Rani ki Vav, a stepwell cut into the ground in Gujarat in the eleventh century _____ "
            "descends seven storeys and carries more than five hundred sculpted figures.",
     [", ", "; ", ": ", " "], "A",
     "The appositive describing the stepwell must be closed with a comma before the verb "
     "'descends'; without it the sentence loses its subject-verb boundary."),

 # ======================================== Form, Structure, and Sense (9)
 fss("F1", "The number of applicants to the conservation course _____ risen every year since the "
           "tuition fee was abolished.",
     ["have", "has", "are", "were"], "B",
     "'The number' is the singular subject; the plural 'applicants' sits inside a prepositional "
     "phrase and does not control the verb."),
 fss("F2", "Neither the copper pipes nor the boiler _____ replaced during the renovation.",
     ["were", "was", "have been", "are"], "B",
     "With 'neither ... nor' the verb agrees with the nearer subject, which here is the singular "
     "'boiler'; the plural verb agrees with the wrong element."),
 fss("F3", "By the time the tide turned that afternoon, the crew _____ the last of the cargo "
           "ashore.",
     ["carry", "carries", "had carried", "will carry"], "C",
     "The carrying was finished before the past-tense turning of the tide, so the earlier of two "
     "past actions takes the past perfect."),
 fss("F4", "The committee released _____ findings in November without naming the members who had "
           "dissented.",
     ["their", "its", "it's", "they're"], "B",
     "'Committee' is a singular noun taking a singular possessive pronoun; the contraction "
     "'it's' means 'it is' and cannot show possession at all."),
 fss("F5", "The grant supports the digitisation of the archive, the training of local staff and "
           "_____ of a public reading room.",
     ["to construct", "the construction", "constructing", "construct"], "B",
     "Parallel structure: the first two items are noun phrases beginning with 'the', so the third "
     "must match; an infinitive or a participle breaks the series."),
 fss("F6", "Walking the shoreline at first light, _____",
     ["the tide had left a line of amber along the sand.",
      "a line of amber had been left along the sand by the tide.",
      "the collector found a line of amber left along the sand by the tide.",
      "there was a line of amber along the sand."], "C",
     "The introductory participial phrase must modify whoever is walking, so the main clause has "
     "to open with that person. The 'tide had left' version attaches the walking to the tide, "
     "which cannot walk."),
 fss("F7", "The 1959 catalogue lists the drawing as untraced; the museum acquired it two years "
           "later and _____ it in the print room ever since.",
     ["has displayed", "displays", "had displayed", "will display"], "A",
     "An action beginning in the past and continuing to the present takes the present perfect, "
     "which is what 'ever since' requires; the simple present would strand that phrase."),
 fss("F8", "Among the papers found at the back of the architect's desk _____ a letter from her "
           "first client.",
     ["were", "was", "have been", "are"], "B",
     "The sentence is inverted, so the subject is the singular 'a letter' that follows the verb, "
     "not the plural 'papers' inside the opening prepositional phrase."),
 fss("F9", "The trial found the compound to be both effective at low doses and _____ over long "
           "periods of use.",
     ["it was safe", "safely", "safe", "being safe"], "C",
     "'both ... and' must join grammatically matching elements, and the first is the adjective "
     "'effective', so the second has to be an adjective too; a clause or an adverb breaks the "
     "pairing."),

 # ================================================== Transitions (9)
 trn("T1", "The dye fades noticeably within a single season of exposure to daylight. _____ museums "
           "hang these textiles under very low light and rotate them out of the galleries every "
           "few months.",
     ["For this reason,", "Nevertheless,", "By contrast,", "In other words,"], "A",
     "The lighting and rotation policy is the consequence of the fading, so the transition must "
     "mark cause and effect. Marking contrast instead would wrongly present the policy as working "
     "against the fact just stated."),
 trn("T2", "Sourdough starters have a reputation for being delicate. _____ a starter left unfed at "
           "the back of a refrigerator for a year can usually be brought back within a week.",
     ["Consequently,", "In fact,", "Similarly,", "For example,"], "B",
     "The second sentence corrects the impression left by the first, and a corrective intensifier "
     "is what marks that move. The 'Similarly' option would present robustness as another instance "
     "of delicacy, which reverses the relationship."),
 trn("T3", "Some plants defend themselves by recruiting animals to do the fighting. _____ certain "
           "acacias house stinging ants in hollowed thorns and feed them sugar in exchange for "
           "driving off browsing herbivores.",
     ["For example,", "However,", "Therefore,", "Meanwhile,"], "A",
     "The acacia is a specific case of the general defence strategy just described, which calls "
     "for an exemplifying transition. Marking cause instead would misread the acacia as a result of the "
     "generalisation rather than an instance of it."),
 trn("T4", "The steam catapult launched aircraft from carrier decks reliably for half a century. "
           "_____ it consumed fresh water at a rate that limited how long a ship could stay at sea "
           "between resupplies.",
     ["Even so,", "Therefore,", "Likewise,", "In summary,"], "A",
     "The water consumption is a drawback set against reliability, and that requires a concessive contrast. The causal "
     "option would make the water consumption a result of the reliability, which makes no sense."),
 trn("T5", "Sea water absorbs low-frequency sound far less readily than air does. _____ a whale "
           "call at twenty hertz can be picked up hundreds of kilometres from the animal that made "
           "it.",
     ["Consequently,", "Nevertheless,", "By comparison,", "Admittedly,"], "A",
     "The long detection range follows from the low absorption, so a result marker fits. The "
     "'Nevertheless' option would signal that the range holds despite the low absorption, which "
     "inverts the physics the first sentence supplies."),
 trn("T6", "A chameleon changes colour by rearranging nanoscale crystals in its skin rather than by "
           "moving pigment about. _____ the blue of a morpho butterfly's wing comes from the "
           "structure of its scales, and no blue pigment is involved at all.",
     ["Similarly,", "However,", "Therefore,", "Instead,"], "A",
     "Both sentences describe colour produced by structure rather than pigment, so the transition "
     "marks a parallel case. Marking contrast would suggest the butterfly works differently from "
     "the chameleon, which is the reverse of the point."),
 trn("T7", "Taking notes by hand is slower than typing and captures a smaller share of what the "
           "lecturer actually says. _____ students who write by hand answer more conceptual "
           "questions correctly when they are tested a week later.",
     ["Accordingly,", "Nonetheless,", "That is,", "For instance,"], "B",
     "The better later performance is surprising given the disadvantages just listed, so the "
     "transition must signal that the result runs against expectation. The result marker would "
     "claim the advantage follows from writing less down, which the sentence does not argue."),
 trn("T8", "The tin in the buckle was mined in Cornwall and the copper in it came from the eastern "
           "Alps. _____ the workshop that made it was drawing on trade routes that spanned the "
           "continent.",
     ["Thus,", "Conversely,", "Meanwhile,", "Admittedly,"], "A",
     "The distant metal sources are the evidence and the continental trade network is the "
     "conclusion drawn from them, so a concluding transition is needed. Marking simultaneity with "
     "'Meanwhile' would suggest the two sentences describe simultaneous events instead."),
 trn("T9", "Any map of the world projects a sphere onto a flat sheet, and no projection can "
           "preserve area and shape at once. _____ every world map distorts something, and the "
           "cartographer's only real choice is what to distort.",
     ["In other words,", "For example,", "Nevertheless,", "Earlier,"], "A",
     "The second sentence restates the geometric impossibility in plainer terms, which is what a "
     "restatement marker signals. The exemplifying option would require a particular map, and none "
     "is named."),

 # ========================================== Rhetorical Synthesis (9)
 rsy("R1",
     "While researching a topic, a student has taken the following notes:<ul>"
     "<li>Mistaken Point in Newfoundland preserves fossils from about 565 million years ago.</li>"
     "<li>The organisms there were buried where they lived by falls of volcanic ash.</li>"
     "<li>Ash layers can be dated directly in the laboratory.</li>"
     "<li>Most fossil beds preserve organisms that were carried some distance after death.</li></ul>",
     "The student wants to explain why the Mistaken Point site is scientifically valuable. Which "
     "choice most effectively uses relevant information from the notes to accomplish this goal?",
     ["Fossils at Mistaken Point in Newfoundland date from about 565 million years ago.",
      "Because falls of volcanic ash buried the organisms where they lived, Mistaken Point preserves them in position and its layers can be dated directly.",
      "Most fossil beds preserve organisms that were carried some distance after they died.",
      "Volcanic ash buried the organisms preserved at Mistaken Point in Newfoundland."],
     "B",
     "Scientific value here rests on two things the notes supply, burial in position and directly "
     "datable layers, and only one option joins them. The plain date statement is accurate but "
     "gives no reason the site is more useful than any other of that age."),
 rsy("R2",
     "While researching a topic, a student has taken the following notes:<ul>"
     "<li>A qanat is a gently sloping tunnel that carries groundwater from a highland aquifer to a village.</li>"
     "<li>Water moves along it entirely by gravity, with no pump of any kind.</li>"
     "<li>Because the channel runs underground, very little water is lost to evaporation.</li>"
     "<li>Some qanats in Iran have been in continuous use for more than two thousand years.</li></ul>",
     "The student wants to explain why the qanat design suits an arid climate. Which choice most "
     "effectively uses relevant information from the notes to accomplish this goal?",
     ["A qanat is a gently sloping tunnel that carries groundwater from a highland aquifer to a village.",
      "Some qanats in Iran have been in continuous use for more than two thousand years.",
      "Running underground and relying entirely on gravity, a qanat delivers highland groundwater to a village with very little lost to evaporation.",
      "Water moves along a qanat by gravity rather than by pump."],
     "C",
     "Suitability to an arid climate turns on losing almost no water, and only one option ties the "
     "underground channel to that saving. The two-thousand-year option shows durability, which is "
     "impressive but is not a point about aridity."),
 rsy("R3",
     "While researching a topic, a student has taken the following notes:<ul>"
     "<li>Beaver dams slow streams into ponds and wet meadows.</li>"
     "<li>Ponded water seeps downward and raises the water table around it.</li>"
     "<li>A raised water table keeps nearby vegetation green later into the dry season.</li>"
     "<li>Green vegetation burns far less readily than dry vegetation.</li></ul>",
     "The student wants to explain how beaver dams reduce the risk of wildfire. Which choice most "
     "effectively uses relevant information from the notes to accomplish this goal?",
     ["Beaver dams slow streams into ponds and wet meadows, and green vegetation burns less readily than dry vegetation.",
      "By raising the water table around them, beaver ponds keep nearby vegetation green later into the dry season, and green vegetation resists burning.",
      "Water ponded behind a beaver dam seeps downward into the surrounding ground.",
      "Vegetation near beaver ponds stays green later into the dry season than vegetation elsewhere."],
     "B",
     "The goal asks for the mechanism, so the chain from raised water table to green vegetation to "
     "reduced burning has to be complete, and only one option carries all of it. The option pairing "
     "dams with flammability states the two ends of the chain without the step that connects them."),
 rsy("R4",
     "While researching a topic, a student has taken the following notes:<ul>"
     "<li>Inuit snow goggles are carved from caribou antler, driftwood or bone.</li>"
     "<li>They admit light through a narrow horizontal slit.</li>"
     "<li>The slit blocks most of the glare reflected off snow.</li>"
     "<li>Narrowing an opening also sharpens distant objects, as a pinhole does.</li></ul>",
     "The student wants to explain how a single feature of the goggles serves two purposes. Which "
     "choice most effectively uses relevant information from the notes to accomplish this goal?",
     ["Inuit snow goggles are carved from caribou antler, driftwood or bone.",
      "The narrow slit in Inuit snow goggles blocks most of the glare reflected off snow and, like a pinhole, sharpens distant objects as well.",
      "Inuit snow goggles admit light through a narrow horizontal slit.",
      "Narrowing an opening sharpens distant objects, as a pinhole does."],
     "B",
     "The goal names one feature and two purposes, so the slit has to appear alongside both glare "
     "reduction and sharpened vision. The option describing only the pinhole effect gives one "
     "purpose and never mentions glare."),
 rsy("R5",
     "While researching a topic, a student has taken the following notes:<ul>"
     "<li>The warship Mary Rose sank in 1545 and was raised from the seabed in 1982.</li>"
     "<li>Its waterlogged oak would have split apart if it had been left to dry.</li>"
     "<li>Conservators sprayed the hull with polyethylene glycol for nineteen years.</li>"
     "<li>The wax replaced the water in the timber cell by cell.</li></ul>",
     "The student wants to explain why the hull did not fall apart after it was recovered. Which "
     "choice most effectively uses relevant information from the notes to accomplish this goal?",
     ["The Mary Rose sank in 1545 and was raised from the seabed in 1982.",
      "Conservators sprayed the hull of the Mary Rose with polyethylene glycol for nineteen years.",
      "Sprayed with polyethylene glycol for nineteen years, the hull had the water in its timber replaced cell by cell with wax, so it did not split as it dried.",
      "Waterlogged oak splits apart if it is allowed to dry out."],
     "C",
     "The question asks why the hull survived, so the answer needs the treatment, the replacement "
     "of water by wax and the splitting that was thereby avoided. The option naming only the spraying "
     "reports the treatment without saying what it did or prevented."),
 rsy("R6",
     "While researching a topic, a student has taken the following notes:<ul>"
     "<li>Vertical farms stack growing trays in racks under LED lighting.</li>"
     "<li>They use roughly a twentieth of the water that field-grown lettuce requires.</li>"
     "<li>Lighting accounts for most of their running cost.</li>"
     "<li>They are usually built close to the cities they supply.</li></ul>",
     "The student wants to present both an advantage and a drawback of vertical farms. Which "
     "choice most effectively uses relevant information from the notes to accomplish this goal?",
     ["Vertical farms use roughly a twentieth of the water that field-grown lettuce requires, though lighting accounts for most of their running cost.",
      "Vertical farms stack growing trays under LED lighting and are usually built close to the cities they supply.",
      "Lighting accounts for most of the running cost of a vertical farm.",
      "Vertical farms use roughly a twentieth of the water that field-grown lettuce requires."],
     "A",
     "The goal requires one of each, and only one option puts the water saving and the lighting "
     "cost in a single sentence. The water-saving option alone gives the advantage and omits the "
     "drawback entirely."),
 rsy("R7",
     "While researching a topic, a student has taken the following notes:<ul>"
     "<li>Excavators at Ebla in Syria recovered about 17,000 cuneiform tablets and fragments in 1975.</li>"
     "<li>The tablets were still shelved in order when the palace burned in about 2300 BCE.</li>"
     "<li>The fire baked the clay and hardened it.</li>"
     "<li>Most cuneiform archives survive only as scattered, unbaked fragments.</li></ul>",
     "The student wants to explain why the Ebla archive is unusually informative. Which choice most "
     "effectively uses relevant information from the notes to accomplish this goal?",
     ["Excavators recovered about 17,000 cuneiform tablets and fragments at Ebla in 1975.",
      "The palace at Ebla burned in about 2300 BCE, and the fire baked the clay tablets stored in it.",
      "Baked hard by the fire that destroyed the palace, the Ebla tablets survive in the order they were shelved, unlike the scattered fragments that make up most cuneiform archives.",
      "Most cuneiform archives survive only as scattered, unbaked fragments."],
     "C",
     "What makes the archive informative is that the tablets survived intact and in their original "
     "order, which is what the comparison with scattered fragments establishes; only one option "
     "carries both. The option about the fire baking the clay gives the cause of preservation but "
     "not the shelving order that makes the archive readable as a whole."),
 rsy("R8",
     "While researching a topic, a student has taken the following notes:<ul>"
     "<li>The Svalbard Global Seed Vault stores duplicate samples sent by seed banks worldwide.</li>"
     "<li>It is cut into permafrost 130 metres above sea level.</li>"
     "<li>Depositors keep ownership of their samples and may withdraw them at any time.</li>"
     "<li>Researchers withdrew Syrian samples in 2015 after the seed bank near Aleppo became unreachable.</li></ul>",
     "The student wants to illustrate with a specific case how the vault has served its purpose. "
     "Which choice most effectively uses relevant information from the notes to accomplish this goal?",
     ["The Svalbard Global Seed Vault stores duplicate samples sent by seed banks worldwide.",
      "When the seed bank near Aleppo became unreachable in 2015, researchers were able to withdraw the duplicate samples that had been deposited at Svalbard.",
      "The vault is cut into permafrost 130 metres above sea level.",
      "Depositors keep ownership of their samples and may withdraw them at any time."],
     "B",
     "The goal asks for a specific case, and the 2015 withdrawal is the only event in the notes. "
     "The withdrawal-rights option states the policy that made the case possible but is a general "
     "rule rather than an instance of the vault working."),
 rsy("R9",
     "While researching a topic, a student has taken the following notes:<ul>"
     "<li>The first transatlantic telegraph cable was completed in August 1858.</li>"
     "<li>Messages that had taken ten days to cross by ship now arrived in minutes.</li>"
     "<li>The cable failed after about three weeks of service.</li>"
     "<li>No durable transatlantic cable was in operation until 1866.</li></ul>",
     "The student wants to emphasise that the achievement of 1858 was short-lived. Which choice "
     "most effectively uses relevant information from the notes to accomplish this goal?",
     ["The first transatlantic telegraph cable was completed in August 1858.",
      "The 1858 cable cut a ten-day crossing to a matter of minutes, but it failed within three weeks, and no durable cable operated until 1866.",
      "Messages that had taken ten days to cross the Atlantic by ship arrived in minutes instead.",
      "No durable transatlantic cable was in operation until 1866."],
     "B",
     "Calling the achievement short-lived requires both the achievement and its swift end, and only "
     "one option supplies the speed gained together with the failure and the eight-year gap. The "
     "option naming only the 1866 date records the gap without ever stating what was achieved and "
     "then lost."),
]

DROPPED = {}
