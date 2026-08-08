#!/usr/bin/env python3
"""
Reading & Writing authored for Test 12.

All 81 items are original. The transcribed pool was spent by Test 8, and for
R&W authoring is in any case the safer route: a transcribed answer key has to
be re-derived by hand before it can be trusted (Test 5 shipped 6 wrong answers
in 81 that way). Every item below carries a `why` recording the reasoning that
produced the key and the reason the strongest distractor fails - that record IS
the verification, so no key exists here without one.

Rationales name options by their CONTENT, never by letter, so balance_rw.py is
free to rotate every question when it evens out the key distribution.

Writing-domain choices are worded, never bare punctuation. Test 8 shipped
Boundaries items whose four options were ", " / "; " / ": " / " and ", so the
student saw four empty rows; the real test repeats the words on either side of
the blank inside every option so that each choice reads as the resulting
sentence. Every Boundaries item here, and every Form/Structure item that turns
on punctuation, is written that way from the start.

Topics were checked against rw_test8.py, rw_test9.py and rw_test10.py and none
is reused: icefish antifreeze, Gee's Bend quilts, wootz steel, pistol shrimp,
Angkor's reservoirs, tape music, horseshoe crab blood, carpet knot density,
naked mole-rats, Goebekli Tepe, honeyguides, Wang Zhenyi, cross-laminated
timber, Noh masks, Shaker furniture, Mary Anning, participatory budgeting, the
Venetian Arsenal, gravitational-wave detection, Anni Albers, ostracism,
axolotls, periodical cicadas, Great Zimbabwe, Maine lobster territories, eels,
woodblock printing, Rapa Nui, bamboo masting, dialect levelling, desert
varnish, vampire bats, default enrolment, Roman frontier pottery, ground
squirrels, atomic clocks, pitcher plants, sodium-ion cells, Nineveh, ant-sown
seeds, satellite gravimetry, and so on.

Block counts (fixed by the assembler's quota, 3 modules x 27):
    Words in Context 15, Text Structure and Purpose 6,
    Central Ideas and Details 6, Command of Evidence 9, Inferences 6,
    Boundaries 12, Form, Structure, and Sense 9, Transitions 9,
    Rhetorical Synthesis 9                                        = 81
"""

SOURCE = "AUTHORED-T12"
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
     "Blood taken from an Antarctic icefish freezes at a lower temperature than the sea the fish "
     "swims in. Proteins circulating in that blood bind to the first ice crystals to form in the "
     "tissue and stop them growing any larger. The crystals are not dissolved; they are simply "
     "held in check. The effect is _____ enough that the animal can spend an entire life in water "
     "that would freeze the blood of any fish from warmer seas.",
     ["dependable", "temporary", "novel", "modest"], "A",
     "The sentence measures the effect against an entire lifetime spent below the freezing point "
     "of ordinary blood, which calls for a word meaning consistently effective. The 'modest' "
     "option understates an effect the passage credits with keeping the fish alive permanently."),

 wic("W2",
     "The quilts sewn at Gee's Bend were made from worn work clothes, feed sacks and whatever else "
     "a household had to hand. Nothing about the results is _____: blocks are cut off-square on "
     "purpose, stripes run out of alignment, and a pattern begun on one edge is abandoned halfway "
     "across. Museums that once collected quilts for their neat symmetry now hang these instead.",
     ["regimented", "improvised", "colourful", "durable"], "A",
     "The colon lists off-square blocks, misaligned stripes and abandoned patterns, so the word "
     "denied by 'Nothing ... is' must mean strictly ordered. The 'improvised' option names what "
     "the quilts in fact are, which the negative construction would then contradict."),

 wic("W3",
     "Blades of wootz steel carry a watered pattern of light and dark bands that no polishing "
     "produces and no engraver cuts. The bands come from carbides that gather in rows as the ingot "
     "cools, so the figure is not applied to the surface but _____ in the metal itself. "
     "Nineteenth-century smiths who reproduced the appearance with acid never reproduced the "
     "structure beneath it.",
     ["etched", "inherent", "imitated", "concealed"], "B",
     "The clause opposes 'applied to the surface', and the pattern is described as arising from "
     "the metal's own cooling structure, so the word must mean built in. The 'etched' option "
     "names exactly what the later smiths did to the surface, which the passage sets apart from "
     "the real thing."),

 wic("W4",
     "A pistol shrimp closes its outsized claw so fast that the water leaving it turns briefly to "
     "vapour. When the resulting bubble collapses it produces a snap loud enough to stun a small "
     "fish and a flash of light too brief for the eye to catch. The claw itself never touches the "
     "prey, so the shrimp's weapon is _____, delivered entirely through the water around it.",
     ["indirect", "audible", "defensive", "reusable"], "A",
     "The reason clause states that the claw never touches the prey and that the effect travels "
     "through the water, which is the definition of acting at a remove. The 'audible' option is "
     "true of the snap but has nothing to do with the contrast the sentence draws."),

 wic("W5",
     "The reservoirs and channels at Angkor caught the monsoon and released it slowly across the "
     "rice fields through a dry season that lasts half the year. That system, rather than the "
     "temples above it, is what allowed a city of several hundred thousand people to stand where "
     "no rain falls for six months. Once the channels silted up faster than they could be cleared, "
     "the advantage Angkor held over its neighbours _____.",
     ["evaporated", "hardened", "multiplied", "recurred"], "A",
     "The advantage rested entirely on the water system, so a system that fails takes the "
     "advantage with it and the blank needs a word meaning disappeared. The 'multiplied' option "
     "reverses the consequence the sentence has just set up."),

 wic("W6",
     "Delia Derbyshire had no synthesiser when she realised the theme in 1963. Every note in it is "
     "a length of magnetic tape cut from a recording of a plucked wire or a filtered oscillator, "
     "trimmed until it sounded the right pitch, and spliced to the note after it. Assembling a "
     "single minute took days of measuring and cutting. The finished piece sounds effortless, "
     "which _____ the labour behind it.",
     ["belies", "records", "prolongs", "justifies"], "A",
     "Days of measuring and splicing stand behind a result that sounds like no work at all, so "
     "the verb must mean gives a false impression of. The 'records' option would mean the music "
     "preserves evidence of the labour, which is the opposite of sounding effortless."),

 wic("W7",
     "Horseshoe crab blood clots on contact with traces of bacterial contamination far below what "
     "other tests detect, and every injectable drug licensed in the United States is checked with "
     "it. Demand has grown until the supply is visibly _____: several hundred thousand animals are "
     "bled each year, and counts along parts of the Atlantic coast have fallen for a decade.",
     ["strained", "secure", "synthetic", "seasonal"], "A",
     "Hundreds of thousands of animals bled annually and a decade of falling counts describe a "
     "supply under pressure. The 'secure' option contradicts the falling counts the colon "
     "introduces as evidence."),

 wic("W8",
     "Knot count is the first thing a carpet dealer quotes, and a rug with four hundred knots to "
     "the square inch will fetch more than one with a hundred. Weavers themselves treat the number "
     "as _____ rather than decisive: fine wool badly dyed, or a design copied by someone who never "
     "understood it, makes a poor carpet at any density.",
     ["preliminary", "conclusive", "arbitrary", "fraudulent"], "A",
     "Set against 'decisive', the word must mean informative but not final, which is what the "
     "weavers' qualification amounts to. The 'arbitrary' option denies the number any meaning at "
     "all, yet the passage has just said it moves the price."),

 wic("W9",
     "A naked mole-rat colony contains one breeding female, and the hundred or so animals around "
     "her do not reproduce at all. They dig, carry food and defend the tunnels on behalf of a "
     "queen whose young are their siblings rather than their offspring. Among mammals the "
     "arrangement is nearly _____: outside a couple of African burrowers it is found only in "
     "insects.",
     ["unique", "universal", "obsolete", "incidental"], "A",
     "Found in only a couple of mammal species and otherwise confined to insects, the arrangement "
     "is close to one of a kind. The 'universal' option asserts the reverse of what the colon "
     "goes on to demonstrate."),

 wic("W10",
     "The carved pillars at G&ouml;bekli Tepe were raised by people with no pottery, no metal and, "
     "as far as anyone can tell, no fields. Archaeologists had long assumed that monuments on that "
     "scale came after agriculture, since only settled farmers could feed a workforce for years at "
     "a time. The site _____ that order, putting the building first and the farming afterwards.",
     ["reverses", "confirms", "obscures", "postpones"], "A",
     "The assumed sequence was farming and then monuments, and the site puts the building first, "
     "so the verb must mean turns the order around. The 'confirms' option would require the "
     "builders to have been farmers, which the opening sentence rules out."),

 wic("W11",
     "In parts of Mozambique a honeyguide will lead a person to a bees' nest, flying ahead and "
     "waiting on a branch until the follower catches up. Hunters answer with a trilled call "
     "learned from their fathers, and the birds respond to that call and not to others. The "
     "exchange is _____: the hunters carry off the honey, and the birds are left the wax and grubs "
     "they could never have reached alone.",
     ["reciprocal", "accidental", "one-sided", "recent"], "A",
     "The colon shows each party getting something the other cannot use, which is an exchange of "
     "mutual benefit. The 'one-sided' option is refuted by the second half of that same list."),

 wic("W12",
     "Wang Zhenyi wanted to explain a lunar eclipse to readers who had none of the mathematics. "
     "She set a lamp on a table for the sun, hung a round mirror above it for the moon, and moved "
     "a garden globe between them for the earth until its shadow fell exactly where she wanted it. "
     "The demonstration was _____: anyone standing in the room could see for herself why the moon "
     "went dark.",
     ["concrete", "abstract", "provisional", "elaborate"], "A",
     "Three household objects arranged so that observers see the shadow fall makes the argument "
     "physical and immediate. The 'elaborate' option misdescribes a lamp, a mirror and a globe, "
     "and elaborateness would not explain why anyone could follow it."),

 wic("W13",
     "Cross-laminated timber is made by gluing boards in layers, with the grain of each layer "
     "turned across the grain of the one below it. Wood is strong along the grain and weak across "
     "it, so alternating the direction produces a panel that behaves much the same way in both "
     "directions and can carry a floor load. The strength of the panel is thus a product of its "
     "_____ rather than of the species of tree it came from.",
     ["arrangement", "thickness", "finish", "origin"], "A",
     "The passage attributes the strength to the crossing of grain direction layer by layer, "
     "which is a matter of how the boards are laid up. The 'thickness' option names a property "
     "the passage never mentions and does not explain the two-directional behaviour."),

 meaning("W14",
         "A Noh mask is carved to hold one expression and no more. The actor cannot alter it, but "
         "he can turn it: tipped a few degrees toward the light the mask reads as grief, and tipped "
         "back it reads as composure. Nothing on the wood has moved. Critics who write that the "
         "angle of the head can <u>qualify</u> the mask mean that the carving by itself never "
         "settles what an audience sees.",
         "qualify",
         ["certify", "modify", "restrict", "describe"], "B",
         "The tilt changes grief into composure without altering the wood, so the verb must mean "
         "alter the sense of. The 'restrict' option catches a common use of the word but not this "
         "one: the angle does not narrow the mask's meaning, it changes it outright."),

 meaning("W15",
         "Shaker cabinetmakers worked to a rule that whatever was not needed for use should not be "
         "made. Drawers go unbanded, chairs are pegged rather than carved, and a whole wall of "
         "built-in cupboards may carry no ornament except the run of its own joints. Furniture "
         "historians who praise the <u>economy</u> of this work are not talking about what it cost "
         "to build.",
         "economy",
         ["thrift with money", "restraint in means", "speed of production", "resistance to wear"],
         "B",
         "Unbanded drawers, pegged joints and absent ornament describe using no more than the work "
         "requires, and the closing sentence explicitly rules out a financial reading. The 'thrift "
         "with money' option is the sense the last sentence exists to exclude."),

 # --------------------------------------------- Text Structure and Purpose (6)
 tsp("S1",
     "Mary Anning found and prepared the first complete ichthyosaur skeleton to reach London, and "
     "dealers and professors bought fossils from her for thirty years. <u>None of the papers those "
     "men published on her specimens carried her name.</u> She was never admitted to the "
     "Geological Society, which did not accept women, and the labels in the collections holding "
     "her work were corrected only long after her death.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It introduces the gap between what she contributed and the credit she was given.",
      "It explains the technique she used to prepare the skeleton.",
      "It questions whether the specimens were correctly identified.",
      "It gives the reason the Geological Society was founded."],
     "A",
     "The sentence about missing attribution sits between her finds and the exclusions that "
     "follow, so it opens the theme of unacknowledged work that the rest of the passage develops. "
     "The preparation technique is mentioned only as something she did, never explained."),

 tsp("S2",
     "From 1989 the residents of Porto Alegre met by district each year to decide how part of the "
     "city's capital budget would be spent. Delegates elected at those meetings ranked the "
     "proposals, and the ranking bound the council. Spending on water and sewer connections in the "
     "poorest districts rose sharply over the decade that followed. The process was slow, and "
     "turnout never rose above a small fraction of the city, but dozens of other municipalities "
     "have since copied it.",
     "Which choice best states the main purpose of the text?",
     ["To describe a budgeting practice, note its measurable effect and acknowledge its limits.",
      "To argue that elected municipal councils should be abolished.",
      "To compare the finances of Porto Alegre with those of other Brazilian cities.",
      "To explain the procedure by which district delegates are elected."],
     "A",
     "The passage defines the practice, reports the rise in spending it produced, then concedes "
     "slowness and low turnout before noting its spread, which is description plus effect plus "
     "limits. Delegate elections are mentioned in one clause and never explained."),

 tsp("S3",
     "The Arsenal did not build a ship in one place. Hulls were floated down a canal past a line "
     "of sheds, and each shed handed over one thing: rigging at the first, then arms, then oars, "
     "then bread and water. A galley could be fitted out between morning and evening. None of this "
     "was written down as a system, and the foreign visitors who described it in the sixteenth "
     "century treated it as a curiosity of Venice rather than a way of making anything else.",
     "Which choice best describes the overall structure of the text?",
     ["It describes a production method, gives evidence of its speed, and notes that observers drew no general lesson from it.",
      "It traces the decline of Venetian shipbuilding after the sixteenth century.",
      "It contrasts two competing accounts of how galleys were armed.",
      "It argues that the Arsenal's method was inferior to later assembly lines."],
     "A",
     "The passage moves from how the sheds worked, to the day it took to fit out a galley, to the "
     "visitors who saw only a local oddity, which is method then evidence then reception. No "
     "decline is described: the text stops at the sixteenth-century visitors."),

 tsp("S4",
     "The detector's two arms are four kilometres long, and a passing gravitational wave stretches "
     "one and squeezes the other by less than the width of a proton. <u>A lorry on a road twenty "
     "kilometres away shifts the mirrors far more than the signal does.</u> Each site therefore "
     "records hundreds of channels of local vibration alongside the main measurement, and a "
     "candidate event is kept only if it appears at both sites, thousands of kilometres apart, "
     "within the time light needs to travel between them.",
     "Which choice best describes the function of the underlined sentence?",
     ["It states the problem that the arrangement described afterwards is built to solve.",
      "It concedes that the detector has never recorded a genuine signal.",
      "It compares two methods of measuring the length of the arms.",
      "It explains how gravitational waves are produced."],
     "A",
     "The sentence establishes that ordinary local noise swamps the signal, and the sentence after "
     "it introduces the vibration channels and the two-site coincidence requirement as the answer "
     "to exactly that. Nothing in the passage denies that real signals have been recorded."),

 tsp("S5",
     "Anni Albers arrived at the Bauhaus meaning to paint and was directed to the weaving workshop, "
     "which was where the women were sent. She stayed. Treating the loom as a set of constraints to "
     "work against rather than a craft to be preserved, she wove with cellophane and horsehair, "
     "published on the structure of cloth as a subject in its own right, and in 1949 became the "
     "first weaver given a solo exhibition at the Museum of Modern Art.",
     "Which choice best states the main purpose of the text?",
     ["To trace how an assignment she did not choose became the medium of her achievement.",
      "To argue that the Bauhaus was hostile to painting as a discipline.",
      "To describe the technical differences between cellophane and horsehair as fibres.",
      "To catalogue the exhibitions held at the Museum of Modern Art after 1949."],
     "A",
     "The passage begins with a workshop she was assigned to against her intention and ends with "
     "the recognition her weaving earned, so the arc runs from imposed medium to achievement in "
     "it. Hostility to painting is not claimed; only that the women were directed to weaving."),

 tsp("S6",
     "Once a year the Athenian assembly voted on whether an ostracism should be held at all. If it "
     "voted yes, citizens gathered two months later and scratched a name on a broken potsherd. "
     "<u>The man named on the most sherds left Attica for ten years, keeping his property and his "
     "citizenship.</u> Thousands of sherds have since been dug out of the city's wells, and "
     "several bundles carry the same name in the same handwriting, which suggests that some were "
     "prepared in advance for voters to collect.",
     "Which choice best describes the function of the underlined sentence?",
     ["It specifies what the vote actually did to the man it named.",
      "It explains why the sherds ended up in the city's wells.",
      "It offers evidence that the outcome of the vote was manipulated.",
      "It defines the general powers of the Athenian assembly."],
     "A",
     "Having described the procedure, the sentence states the penalty and its limits, ten years' "
     "exile with property and citizenship intact. Evidence of manipulation is the point of the "
     "final sentence about matching handwriting, not of this one."),

 # ------------------------------------------------- Central Ideas and Details (6)
 cid("C1",
     "An axolotl that loses a limb grows another with the same bones in the same order. Cells at "
     "the wound surface give up their identity, gather into a mass called a blastema, and are then "
     "instructed by signals from the surrounding tissue about what they are to become. Those "
     "signals carry position: a blastema formed at the wrist produces a hand, and one formed at "
     "the shoulder produces the entire arm. Nothing is copied from the limb that was lost.",
     "Which choice best states the main idea of the text?",
     ["What regrows is determined by where the wound is, not by any record of the missing limb.",
      "Axolotls regrow limbs faster than any other vertebrate does.",
      "The blastema is made of cells that retain their original identities throughout.",
      "Signals from the surrounding tissue play only a minor part in regeneration."],
     "A",
     "The wrist-versus-shoulder contrast and the closing sentence together say that position "
     "supplies the instructions and no memory of the lost limb is involved. The option about "
     "retained identities contradicts the statement that the cells give up their identity."),

 cid("C2",
     "Periodical cicadas spend thirteen or seventeen years underground and then emerge in a single "
     "week, in numbers no predator can eat through. Both intervals are prime numbers. A predator "
     "whose own population peaks every two, three or four years can come into step with a "
     "thirteen-year brood only once in a very long while, and the same holds for any hybrid brood "
     "emerging on a shorter, non-prime cycle. Broods on even cycles, if they ever existed, would "
     "have been eaten out long ago.",
     "Which choice best states the main idea of the text?",
     ["The prime-numbered cycles make it hard for predator populations to fall into step with the cicadas.",
      "Cicadas emerge in a single week because their food is available only then.",
      "Predators of periodical cicadas reach peak numbers every thirteen years.",
      "Hybrid broods survive better than the broods that produced them."],
     "A",
     "The passage explains that a predator cycling every two, three or four years rarely coincides "
     "with a prime interval, and that non-prime broods were eaten out. The hybrid option inverts "
     "the passage's claim that shorter, non-prime cycles fare worse."),

 cid("C3",
     "The stone walls at Great Zimbabwe stand up to eleven metres high and were laid without "
     "mortar, each granite block cut to sit on the one beneath it. European visitors in the "
     "nineteenth century credited them to Phoenicians, Arabs, anyone but the people living around "
     "them. Excavation has since produced Chinese celadon, Persian glass and a great deal of local "
     "pottery, and the pottery below the walls is continuous with the pottery above them.",
     "Based on the text, what does the pottery sequence indicate?",
     ["The community already living on the site was the one that built the walls.",
      "The walls were built by traders who had arrived from Persia.",
      "The site was abandoned before the walls were finished.",
      "Chinese celadon reached the site before the earliest walls were raised."],
     "A",
     "Pottery continuous from below the walls to above them means the same occupation runs through "
     "the building phase, which answers the visitors who looked for outside builders. The option "
     "about Persian traders is the assumption the excavated sequence undercuts."),

 cid("C4",
     "Lobstering harbours along the Maine coast are divided into fishing territories that appear "
     "on no chart. A boat setting traps on another harbour's ground finds the buoys of its warps "
     "cut, and a skipper who persists loses gear faster than he can replace it. The state licenses "
     "anyone who qualifies and recognises none of these boundaries. Catches per trap are "
     "nonetheless higher inside the tightly held territories than along the stretches of coast "
     "where the custom has broken down.",
     "Which choice best states the main idea of the text?",
     ["An unofficial system of territories that fishers enforce themselves coincides with better catches.",
      "State licensing has successfully replaced the harbours' informal boundaries.",
      "Cutting another boat's warps is the commonest cause of gear loss in Maine.",
      "Lobster catches are falling everywhere along the Maine coast."],
     "A",
     "The passage sets an unofficial, self-policed boundary system against state licensing that "
     "ignores it, then reports higher catches per trap where the custom holds. The option about "
     "licensing replacing the boundaries reverses the sentence saying the state recognises none of "
     "them."),

 cid("C5",
     "Every European eel is born in the Sargasso Sea, and no one has ever seen one spawn there. "
     "The larvae drift east on the current for a year or more, enter rivers as glass eels, and "
     "live in fresh water for a decade or two. Then the gut shrinks, the eyes enlarge, the body "
     "turns silver, and the animal swims back across the ocean without eating. Tags recovered from "
     "the Atlantic have followed a handful of them most of the way; none has ever returned.",
     "According to the text, which of the following is true of the eels' return migration?",
     ["The eels change physically before setting out and take no food on the way.",
      "The eels feed heavily during the crossing in order to fuel it.",
      "Researchers have observed the eels spawning at the end of the crossing.",
      "The eels come back to fresh water once they have spawned."],
     "A",
     "The passage lists shrinking gut, enlarged eyes and silver colouring before departure and "
     "states that the crossing is made without eating. The option about observed spawning is "
     "denied by the first sentence."),

 cid("C6",
     "A Japanese woodblock print is signed by the artist who drew it, and the drawing itself is "
     "destroyed in the making. The block cutter pastes it face down on cherry wood and cuts away "
     "everything the artist did not draw, so the lines survive only as the ridges left standing. "
     "Printers then pull one impression for every colour, holding the sheet in place with two "
     "notches cut into each block. Publishers, who paid for all of it, chose the subjects.",
     "Which choice best states the main idea of the text?",
     ["A print credited to one artist is in fact the product of several trades.",
      "Block cutters were more highly skilled than the artists who signed the prints.",
      "The registration notches were the printers' most important invention.",
      "Publishers seldom influenced the subjects of the prints they financed."],
     "A",
     "The passage names an artist, a cutter, a printer and a publisher, each doing part of the "
     "work behind a single signature. The option denying publishers any influence contradicts the "
     "final sentence, which gives them the choice of subject."),

 # ---------------------------------------------------- Command of Evidence (9)
 coe("E1",
     "The stone figures on Rapa Nui were quarried inland, and some of them stand more than fifteen "
     "kilometres from the quarry. One account has them dragged flat on wooden sledges over "
     "rollers, which would have consumed a great deal of timber. Another proposes that they were "
     "moved upright, rocked from side to side by teams hauling on ropes tied at the head, in the "
     "way a heavy cabinet is walked across a floor. Islanders questioned in the nineteenth century "
     "said the statues walked.",
     "Which finding, if true, would most strongly support the second account?",
     ["Figures abandoned along the transport routes have bases cut convex and lean forward, a shape that makes an upright statue rock from side to side rather than topple.",
      "Pollen cores show that the island was densely forested during the period when the figures were carved.",
      "The quarry contains dozens of unfinished figures still attached to the bedrock.",
      "Figures already erected on their platforms have bases cut flat and level."],
     "A",
     "The rocking account needs a statue that can stand and sway, and a convex, forward-leaning "
     "base is precisely the shape that permits it, found on the figures still in transit. Dense "
     "forest would supply the timber the sledge account requires and so favours the rival."),

 coe("E2",
     "A stand of bamboo may flower once in a century, and when it does every plant in the stand "
     "flowers at the same time, sets seed and dies. Biologist Rahel Tesfaye argues that the long "
     "interval and the synchrony are both defences: seed-eating animals cannot maintain a "
     "population on a food supply that appears twice in a lifetime, and the quantity released at "
     "once exceeds anything the animals present can eat.",
     "Which finding, if true, would most strongly support Tesfaye's argument?",
     ["In a mass-flowering year rodent numbers climb sharply, yet the proportion of seed eaten is far lower than in stands that flower in small patches every year.",
      "Bamboo stands that flower synchronously grow at higher altitudes than stands that do not.",
      "Bamboo seedlings grow more quickly in shade than in full sun.",
      "Rodents in bamboo forests eat fruit and insects when no seed is available."],
     "A",
     "The argument predicts that flooding the market beats the seed-eaters, so a lower proportion "
     "eaten during a mass flowering than during annual small flowerings is the comparison that "
     "tests it. The option about rodents eating fruit and insects would let a population persist "
     "between flowerings, working against the claim."),

 coe("E3",
     "A fresco fragment in a regional museum has been catalogued for a century as the work of an "
     "unknown hand. Curator Elena Ruiz argues that it came instead from the workshop of a named "
     "master whose documented frescoes survive in two churches within a day's ride of the museum.",
     "Which finding, if true, would most strongly support Ruiz's claim?",
     ["The fragment's plaster was laid in daily sections of the same size and order as those in the two documented frescoes, and its underdrawing was transferred from cartoons pricked at the same spacing.",
      "The fragment shows a subject that was painted throughout the region in the same period.",
      "The fragment's plaster was made with sand from a riverbed used by workshops across the whole province.",
      "Records show that the master received more commissions than his workshop could complete."],
     "A",
     "Matching daily plaster sections and identical pricking spacing are workshop habits rather "
     "than regional conventions, so they tie the fragment to that particular shop. Sand from a "
     "riverbed everyone used identifies nothing, since it is shared with every rival workshop."),

 coe("E4",
     "A market town forty minutes from a large city by a rail line opened in 1998 has been surveyed "
     "twice, in 1995 and again in 2020. Linguist Peter Nyman argues that the town's distinctive "
     "vowel system is being levelled by daily contact with city speech, rather than simply fading "
     "of its own accord.",
     "Which finding, if true, would most strongly support Nyman's argument?",
     ["In the 2020 survey the older vowels are strongest among residents who never travel to the city and weakest among those who commute there daily.",
      "The town's population grew by roughly a fifth between 1995 and 2020.",
      "The same vowels have weakened just as much in towns that have no rail link to any city.",
      "Residents surveyed in 2020 said they valued the local accent and hoped it would survive."],
     "A",
     "Contact is the proposed mechanism, so a gradient running with the amount of contact each "
     "speaker has is the evidence that distinguishes it from ordinary drift. Equal weakening in "
     "towns with no rail link removes contact from the explanation altogether."),

 coe("E5",
     "Desert varnish is a dark coating a few micrometres thick that forms on exposed rock in arid "
     "country. It is unusually rich in manganese, which is scarce in the rock beneath it. "
     "Geochemist Amara Ndiaye proposes that bacteria living on the surface concentrate the "
     "manganese, rather than the coating being left behind as windblown dust is wetted and dried.",
     "Which finding, if true, would most strongly support Ndiaye's proposal?",
     ["Sterilised rock chips left on the desert surface for a decade show no manganese enrichment, while untreated chips beside them do.",
      "Varnish is thicker on rock faces sheltered from the prevailing wind than on exposed ones.",
      "Dust settling on desert rock contains small quantities of manganese.",
      "Varnish forms on many kinds of rock, including sandstone and basalt."],
     "A",
     "Sterilising removes the organisms and nothing else, so enrichment that stops when the "
     "microbes are killed points at the microbes as the cause. Manganese present in settling dust "
     "supports the dust explanation Ndiaye is arguing against."),

 coe("E6",
     "Female vampire bats that fail to find a meal are fed by roostmates, which regurgitate part "
     "of what they took. Behavioural ecologist Ines Molina argues that the sharing is sustained by "
     "reciprocity between particular individuals rather than by kinship alone.",
     "Which finding, if true, would most strongly support Molina's argument?",
     ["Among unrelated bats housed together, how readily one bat donates to a given partner tracks how often that partner has fed it in the past.",
      "Bats that share blood tend to roost closer together than bats that do not.",
      "Mothers donate to their own pups far more often than to any other bat in the roost.",
      "A vampire bat can survive only about sixty hours without a blood meal."],
     "A",
     "Unrelated bats remove kinship from the picture, and donation that follows a partner's past "
     "generosity is reciprocity by definition. The finding about mothers and pups supports the "
     "kinship explanation Molina is arguing against."),

 coe("E7",
     "An employer changed its retirement plan so that new staff were enrolled unless they opted "
     "out; previously they joined only by opting in. Participation among new staff rose from 40 "
     "percent to 88 percent. Economist Daniel Okafor argues that the change worked by removing the "
     "effort of enrolling, not by persuading anyone that saving was worthwhile.",
     "Which finding, if true, would most strongly support Okafor's argument?",
     ["Contributions among the newly enrolled cluster tightly at the plan's default percentage rather than at the levels staff themselves called adequate in a survey.",
      "Staff hired after the change reported greater satisfaction with their employer overall.",
      "Participation also rose among staff hired before the change, who still had to opt in.",
      "The plan's investments returned more in the year after the change than in the year before."],
     "A",
     "If people had been persuaded that saving mattered, their contributions would sit near what "
     "they consider adequate; clustering at whatever the form already says instead is the "
     "signature of effort avoidance. Rising participation among opt-in staff would show "
     "persuasion at work, which is the rival account."),

 coe("E8",
     "A Roman fort on the northern frontier has produced cooking pots of a shape not made anywhere "
     "in the surrounding province. Archaeologist Sonia Braga argues that the unit garrisoned there "
     "was raised on the Rhine and brought its own foodways north with it.",
     "Which finding, if true, would most strongly support Braga's argument?",
     ["Chemical analysis shows the pots were made from clay dug within a few kilometres of the fort, in shapes otherwise recorded only in the Rhineland.",
      "The pots are the commonest single find in the fort's rubbish pits.",
      "Pots of the same shape have been found at forts across the empire, including in North Africa.",
      "A dedication stone from the fort names an emperor who reigned for two years."],
     "A",
     "Local clay in a foreign shape means the vessels were made on the spot by or for people who "
     "already knew that shape, which is what carrying a tradition looks like. Finding the shape "
     "empire-wide would make it a general army style rather than a Rhineland marker."),

 coe("E9",
     "An Arctic ground squirrel in hibernation lets its body temperature fall below freezing for "
     "weeks at a stretch without ice forming in its tissues. Physiologist Tomas Halloran proposes "
     "that the animal manages this by clearing its blood of the particles around which ice "
     "crystals would otherwise begin to grow.",
     "Which finding, if true, would most strongly support Halloran's proposal?",
     ["Blood drawn from hibernating squirrels freezes at a markedly lower temperature than the same blood does after fine particles have been stirred into it.",
      "Hibernating squirrels rewarm themselves briefly every two or three weeks.",
      "Squirrels hibernate in burrows dug below the depth reached by seasonal frost.",
      "The squirrels' blood contains the same salts, at the same concentrations, as that of related species that do not hibernate."],
     "A",
     "Adding particles back and watching the freezing point rise shows that their absence is what "
     "was holding it down, which is the mechanism proposed. Identical salt concentrations rule out "
     "one alternative but say nothing in favour of the particle explanation itself."),

 # -------------------------------------------------------------- Inferences (6)
 inf("I1",
     "A clock runs more slowly the deeper it sits in a gravitational field, an effect so small "
     "that only atomic timekeeping can register it over short distances. Two identical optical "
     "clocks were compared, one left on a laboratory bench and the other raised thirty centimetres "
     "above it on a support. Over several days the raised clock ran measurably ahead of the one "
     "below. If the same comparison were repeated with the upper clock raised a full metre instead, "
     "the gap that opened between the two clocks would _____",
     ["disappear altogether.",
      "grow larger than it did at thirty centimetres.",
      "reverse, so that the lower clock ran ahead.",
      "stay exactly what it was at thirty centimetres."],
     "B",
     "Height above the bench is what produced the gap, so tripling the height should widen it. The "
     "option keeping the gap unchanged would mean the separation had no effect, which contradicts "
     "the result already reported at thirty centimetres."),

 inf("I2",
     "One highland pitcher plant in Borneo grows a pitcher too wide and too shallow to drown much "
     "of anything, with a rim of nectar on the underside of its lid. Tree shrews climb up to lick "
     "the nectar, and the distance from the pitcher's rim to that lid matches the length of a "
     "shrew almost exactly, so a feeding animal sits with its hindquarters directly over the "
     "opening. The fluid inside is rich in nitrogen of animal origin. For this plant the pitcher "
     "works less as a trap than as _____",
     ["a lavatory that its visitors are encouraged to use.",
      "a store of nectar kept for the plant's own use.",
      "a shelter in which shrews can raise their young.",
      "a container for rainwater collected from the canopy."],
     "A",
     "The pitcher cannot drown a shrew, is sized so the animal's hindquarters overhang the "
     "opening, and fills with nitrogen of animal origin, which describes collecting droppings "
     "rather than prey. The nectar-store option ignores that the nectar is offered outward, to the "
     "visitors."),

 inf("I3",
     "Lithium is expensive and unevenly distributed. Sodium sits directly below it in the periodic "
     "table, behaves similarly, and is abundant almost everywhere. Sodium-ion cells work on the "
     "same principle as lithium-ion ones, but a sodium ion is larger and heavier, so a cell of a "
     "given mass stores less energy. Sodium cells also tolerate being run flat and cost less per "
     "kilowatt-hour. It follows that sodium-ion cells are best suited to uses in which _____",
     ["the weight of the battery matters less than what it costs.",
      "the battery must be made as light as it possibly can be.",
      "the cell must never be allowed to discharge fully.",
      "lithium happens to be locally abundant."],
     "A",
     "The passage grants sodium a cost advantage and a durability advantage while conceding lower "
     "energy for a given mass, so the good applications are the ones indifferent to weight. The "
     "option demanding the lightest possible battery selects for exactly the property sodium "
     "lacks."),

 inf("I4",
     "The tablets from Nineveh were written on unfired clay, which crumbles in damp ground and can "
     "be soaked back into mud. When the city was sacked in 612 BCE the palace burned, and the fire "
     "was hot enough to bake the tablets stacked in its rooms. Tens of thousands of them were dug "
     "out of the ash in the nineteenth century, a great many unbroken and still legible. "
     "Paradoxically, then, the destruction of the library _____",
     ["is the reason so much of its contents survives.",
      "left almost nothing for later excavators to recover.",
      "proves the tablets had been fired before they were shelved.",
      "rendered the surviving tablets impossible to read."],
     "A",
     "Unfired clay dissolves in damp ground, and the fire fired it, so the burning is what made "
     "survival possible, which is the paradox the last sentence announces. The option about "
     "prior firing is ruled out by the statement that the tablets were unfired when written."),

 inf("I5",
     "Some woodland plants attach a small oil-rich body to each seed. Ants carry these seeds back "
     "to the nest, feed the oil body to their larvae, and discard the seed itself undamaged in the "
     "refuse chamber, a warm pocket of soil enriched by the colony's waste. Plants of this kind "
     "advance only a few metres a year. They are scarce in woods that were cleared and replanted "
     "within the last century, even where the soil is otherwise suitable, most likely because "
     "_____",
     ["they have not yet had time to spread into ground that was cleared.",
      "the ants avoid seeds produced by plants growing in young woodland.",
      "such plants require soil that has never been disturbed by ploughing.",
      "the oil bodies grow smaller on plants living in replanted woods."],
     "A",
     "Spreading a few metres a year is the only rate the passage gives, and a century of it "
     "covers a very short distance, which explains scarcity in recently replanted ground. The "
     "option about undisturbed soil is blocked by the clause conceding that the soil is otherwise "
     "suitable."),

 inf("I6",
     "A pair of satellites following one another in the same orbit measure the distance between "
     "them to a fraction of a millimetre. Passing over a concentration of mass, the leading "
     "satellite is tugged forward first and the gap widens, then closes again as the trailing "
     "satellite reaches the same point. Groundwater is heavy, and removing it lightens the ground "
     "beneath. A plain from which water is pumped faster than rain replaces it should therefore "
     "show, month after month, _____",
     ["a steady weakening of the tug it exerts on the passing satellites.",
      "no measurable change in the separation of the satellites at all.",
      "an increase in the mass measured beneath its surface.",
      "a change in the satellites' altitude but not in their separation."],
     "A",
     "Water leaving the ground reduces the mass below, and the instrument reads mass as a tug on "
     "the leading satellite, so continued pumping should weaken that tug over time. The option "
     "predicting increasing mass runs the arithmetic backwards, since pumping removes water rather "
     "than adding it."),

 # --------------------------------------------------------------- Boundaries (12)
 bnd("B1",
     "Paper was made in China for centuries before the technique travelled west. Craftsmen taken "
     "prisoner at Talas in 751 are said to have set up the first mills in Samarkand _____ within "
     "fifty years paper was being made in Baghdad, and within four hundred it had reached Spain.",
     ["Samarkand; within fifty years", "Samarkand, within fifty years",
      "Samarkand within fifty years", "Samarkand: and within fifty years"], "A",
     "Two complete sentences meet at the blank with no coordinating conjunction between them, so "
     "the semicolon is the only option that joins them without producing a comma splice."),

 bnd("B2",
     "Rice in the Kerala backwaters grows below sea level, behind earth bunds that have to be "
     "pumped dry before every season. Because the fields lie lower than the water on the far side "
     "of the bund _____ a failure of the pumps lasting even a few days will drown a crop that has "
     "already been planted.",
     ["bund, a failure", "bund; a failure", "bund: a failure", "bund and a failure"], "A",
     "The opening clause introduced by 'Because' is dependent and has to be marked off from the "
     "main clause with a comma; the semicolon and the colon both require a complete sentence in "
     "front of them."),

 bnd("B3",
     "Nothing in a Viking-age grave got there by accident. The burial at the head of the fjord "
     "held three objects nobody expected to find together _____ a set of folding scales, a "
     "whetstone quarried in Norway and a silver coin struck in Samarkand.",
     ["together: a set of folding scales", "together; a set of folding scales",
      "together, and a set of folding scales", "together which a set of folding scales"], "A",
     "The words before the blank form a complete sentence announcing three objects, and the colon "
     "is the mark that introduces the list naming them."),

 bnd("B4",
     "Optics before him rested on the idea that the eye sends something out towards whatever it "
     "sees. Ibn al-Haytham, the scholar who wrote the Book of Optics while under house arrest in "
     "Cairo _____ argued instead that light travels from the object to the eye, and tested the "
     "claim with a darkened room and a pinhole.",
     ["Cairo, argued", "Cairo; argued", "Cairo: argued", "Cairo argued"], "A",
     "The appositive beginning 'the scholar who wrote' was opened with a comma and must be closed "
     "with a matching comma before the verb 'argued'."),

 bnd("B5",
     "A roof painted with the new coating stays cooler than the air above it even in full sun. The "
     "paint throws back almost all of the sunlight that strikes it _____ and it radiates the heat "
     "it does absorb at a wavelength that passes straight out through the atmosphere.",
     ["it, and it radiates", "it and it radiates", "it; and it radiates", "it: and it radiates"],
     "A",
     "Two independent clauses joined by the coordinating conjunction 'and' take a comma before "
     "that conjunction; neither the semicolon nor the colon is used in front of a coordinating "
     "conjunction, and leaving the punctuation out runs the clauses together."),

 bnd("B6",
     "Meteorites are easier to find on ice than anywhere else, because a dark stone on a white "
     "sheet has nowhere to hide. Teams working the blue-ice fields of Antarctica bring back several "
     "hundred stones in a season _____ most of which have lain where they fell for tens of "
     "thousands of years.",
     ["season, most of which", "season; most of which", "season: most of which",
      "season. Most of which"], "A",
     "'most of which' opens a non-essential relative clause, which attaches to the main clause "
     "with a comma; the semicolon and the full stop each require an independent clause after them, "
     "and this one cannot stand alone."),

 bnd("B7",
     "The abbey stands on a rock in a bay with one of the largest tidal ranges in Europe. When the "
     "tide runs out across the sand _____ the causeway is dry for six hours and the island stops "
     "being an island at all.",
     ["sand, the causeway", "sand; the causeway", "sand: the causeway", "sand and the causeway"],
     "A",
     "The sentence opens with a dependent clause introduced by 'When', and a dependent clause "
     "standing in front of the main clause is followed by a comma."),

 bnd("B8",
     "The lift beneath the opera house stage carries a complete set from the workshops up to stage "
     "level in ninety seconds. It rose smoothly through the first two floors on the night of the "
     "dress rehearsal _____ then a hydraulic seal failed and the platform sank back into the "
     "basement with the scenery still aboard.",
     ["rehearsal; then a hydraulic seal", "rehearsal, then a hydraulic seal",
      "rehearsal: then a hydraulic seal", "rehearsal then a hydraulic seal"], "A",
     "'then' is an adverb, not a coordinating conjunction, so joining these two complete sentences "
     "with nothing stronger than a comma would leave a splice."),

 bnd("B9",
     "The Hanseatic ships that worked the Baltic sailed on a short list of goods. The league's "
     "warehouse at Bergen dealt in almost nothing else _____ dried cod from the north, grain out "
     "of the eastern ports and salt carried up from the Bay of Biscay.",
     ["else: dried cod", "else; dried cod", "else, and dried cod", "else dried cod"], "A",
     "What precedes the blank is a complete sentence, and the colon is the mark that introduces "
     "the list specifying the goods it refers to."),

 bnd("B10",
     "A portolan chart is drawn from sailing directions rather than from any survey. Although "
     "nobody who made these charts had a means of fixing longitude at sea _____ the outlines of "
     "the Mediterranean on the earliest of them are accurate to within a few kilometres.",
     ["sea, the outlines", "sea; the outlines", "sea: the outlines", "sea and the outlines"], "A",
     "'Although' opens a dependent clause, and a dependent clause placed before the main clause is "
     "separated from it by a comma."),

 bnd("B11",
     "An mbira is a set of metal tongues bolted to a wooden board and played with the thumbs. "
     "Bottle caps threaded on a wire buzz against the board as the notes sound _____ the tongues "
     "themselves are tuned by hammering them thinner, and a player may retune several of them in "
     "the course of an evening.",
     ["sound; the tongues", "sound, the tongues", "sound the tongues", "sound: and the tongues"],
     "A",
     "Both halves are complete sentences and no conjunction joins them, so the semicolon is "
     "required; the second half reports a separate fact about tuning rather than explaining the "
     "buzz, which is what a colon would promise."),

 bnd("B12",
     "Not everything in the asteroid belt is a fragment of something larger. Ceres, the biggest "
     "object between Mars and Jupiter and round enough to count as a dwarf planet _____ holds more "
     "fresh water, most of it frozen, than any body in the inner solar system except the Earth.",
     ["planet, holds", "planet; holds", "planet: holds", "planet holds"], "A",
     "The appositive describing the object opened with a comma, so it has to be closed with a "
     "comma before the verb 'holds'."),

 # ------------------------------------------------ Form, Structure, and Sense (9)
 fss("F1",
     "A steelpan begins life as an oil drum, and the sinking and grooving of its face are done "
     "entirely by ear. Neither the tuner's hammer nor the templates pinned above the bench _____ "
     "able to settle a note; only listening can do that.",
     ["are", "is", "was", "has been"], "A",
     "With 'neither ... nor' the verb agrees with whichever subject stands nearer to it, and "
     "'the templates' is plural."),

 fss("F2",
     "The library keeps its manuscripts in a room held at a fixed humidity all year, and every few "
     "seasons one part of the holdings is taken out and given new housing while the rest stays "
     "where it is. The collection of Persian bindings, together with several hundred loose folios, "
     "_____ rehoused in acid-free boxes last winter, one item at a time.",
     ["was", "were", "are", "have been"], "A",
     "The subject is the singular noun 'collection'; an interrupting phrase beginning 'together "
     "with' does not turn a singular subject plural, and the present-perfect option clashes with "
     "'last winter'."),

 fss("F3",
     "The survey crew had been camped on the plain for a fortnight, reading the tilt of the ground "
     "twice a day, when the volcano at the head of the valley began to settle and the readings "
     "started to run away from them. By the time the ash cloud reached the camp that evening, they "
     "_____ their instruments and started inland on foot.",
     ["had packed", "packed", "have packed", "were packing"], "A",
     "The packing was finished before the ash arrived, and the past perfect is what marks one past "
     "action as completed before another."),

 fss("F4",
     "The museum's basement holds three hundred safety lamps, each one stamped with the name of "
     "the pit that issued it and with the name of the man it was issued to. The _____ names are "
     "punched into the brass rather than painted on, which is why they can still be read a century "
     "after the last of the pits closed.",
     ["miners'", "miner's", "miners", "miners's"], "A",
     "The names belong to more than one miner, and a plural noun already ending in s takes the "
     "apostrophe after that s. The singular possessive would leave three hundred lamps to a single "
     "owner."),

 fss("F5",
     "The studio's negatives came to the archive in tea chests, unlabelled and in no order, and "
     "nobody has been able to say how many of them there are. A grant from the trust now covers "
     "the whole of the work. It pays for cataloguing the negatives, digitising the most fragile "
     "among them, and _____",
     ["making the entire collection searchable online.",
      "the entire collection is made searchable online.",
      "to make the entire collection searchable online.",
      "for the searching of the entire collection online."], "A",
     "The list already runs 'cataloguing ... digitising ...', so the third item has to be another "
     "gerund phrase. The infinitive option breaks the pattern the first two items establish."),

 fss("F6",
     "The colliery has not raised coal since 1986, but the workings below it are still kept clear "
     "of water. The winding gear had been stopped for the afternoon tour and the whole yard was "
     "silent. Standing at the top of the shaft in that silence, _____",
     ["the visitors could hear the pumps working four hundred metres below.",
      "the pumps working four hundred metres below could be heard.",
      "there was the sound of pumps four hundred metres below.",
      "it was possible to hear the pumps four hundred metres below."], "A",
     "The opening participle needs the people doing the standing as the subject of the main "
     "clause. The option beginning with the pumps makes the machinery stand at the top of the "
     "shaft."),

 fss("F7",
     "Blistering in a glaze is usually a sign that the ware has been brought down through its "
     "cooling range too quickly. The kiln was rebuilt over the winter with a taller chimney and a "
     "slower cooling cycle. The panels fired in it this spring came out with fewer blisters than "
     "_____ fired in the old one.",
     ["those", "that", "them", "it"], "A",
     "The comparison is with the earlier panels, a plural noun, so the plural demonstrative is "
     "the pronoun that stands in for them."),

 fss("F8",
     "What is left of the pier is a line of iron stumps that shows at low water and a ticket "
     "office at the landward end. The 1931 guidebook describes the structure as newly built and "
     "lists four kiosks along its length. Storms in the decade that followed _____ two thirds of "
     "it away.",
     ["took", "take", "have taken", "had taken"], "A",
     "The storms are placed in a decade that is over, so the simple past is the tense that matches "
     "the completed period the sentence names."),

 fss("F9",
     "The panel was painted on oak boards joined edge to edge and held in a frame made for it in "
     "the same workshop. Cracks have since opened along one of those joins, and the frame no "
     "longer holds the panel square. The conservators recommended that the painting _____ moved "
     "until the frame had been rebuilt.",
     ["not be", "is not", "was not", "will not be"], "A",
     "Verbs of recommendation are followed by the subjunctive, which uses the base form, so none "
     "of the indicative options can stand after 'recommended that'."),

 # --------------------------------------------------------------- Transitions (9)
 trn("T1",
     "Ultrasonic welding joins two plastic parts in a fraction of a second and uses no adhesive at "
     "all. _____ it works only where the parts can be pressed together against a fixed anvil, "
     "which rules it out for most repairs.",
     ["However,", "Likewise,", "Therefore,", "For example,"], "A",
     "The first sentence lists advantages and the second states a limitation, so the link is "
     "contrastive. 'Therefore' would present the limitation as a consequence of the advantages, "
     "which it is not."),

 trn("T2",
     "A basalt quarry at the head of the valley supplied millstones to half the region for two "
     "hundred years, and a finished stone weighed the better part of a tonne and had to be rolled "
     "on its edge to the river. _____ the roads leading down from the quarry were metalled "
     "centuries before any others in the district.",
     ["Consequently,", "Nevertheless,", "Meanwhile,", "In contrast,"], "A",
     "Heavy stone leaving the quarry is the reason the roads were surfaced early, so the second "
     "sentence gives a result. 'Nevertheless' would mark the roads as surprising given the traffic, "
     "when they follow from it."),

 trn("T3",
     "Some fish change sex during their lives, and the direction of the change is not the same in "
     "every species. _____ a clownfish group has one breeding female, and when she dies the "
     "largest male turns female and replaces her.",
     ["For instance,", "Instead,", "As a result,", "In addition,"], "A",
     "The second sentence supplies a particular species to illustrate the general statement before "
     "it. 'As a result' would make the clownfish arrangement a consequence of the generalisation "
     "rather than a case of it."),

 trn("T4",
     "The lighthouse was automated in 1988 and the last keepers were taken off the rock that "
     "autumn. _____ the fog signal went on being sounded by hand for two more winters, because the "
     "automatic timer could not be relied on in hard frost.",
     ["Even so,", "Likewise,", "Because of this,", "In short,"], "A",
     "Automation removing the keepers would predict no more hand-sounded signals, and the second "
     "sentence reports the opposite, so the link concedes an exception. 'Because of this' would "
     "make the hand-sounding a result of the automation."),

 trn("T5",
     "Rammed-earth walls are built from soil compacted inside shuttering, layer by layer, and the "
     "soil is normally dug within sight of the wall itself. Walls of this kind need no firing, no "
     "cement and almost no transport. _____ they hold heat through the day and give it back after "
     "dark, which suits a climate with cold nights.",
     ["In addition,", "Nonetheless,", "Otherwise,", "By contrast,"], "A",
     "Both sentences list advantages of the same construction, so the second adds to the first. "
     "'Nonetheless' would set the thermal behaviour against the earlier advantages instead of "
     "joining it to them."),

 trn("T6",
     "A written Chinese character gives a reader almost no guide to how the word it stands for is "
     "pronounced, which is why speakers of dialects that cannot understand one another in "
     "conversation can read the same page. _____ an alphabetic spelling records the sound and "
     "leaves the meaning to be worked out from the word itself.",
     ["By contrast,", "Accordingly,", "Similarly,", "In fact,"], "A",
     "The two writing systems are set against each other, one withholding sound and the other "
     "recording it. 'Similarly' would claim the systems behave alike, which is the reverse of what "
     "the sentences say."),

 trn("T7",
     "Type was broken up and redistributed as soon as a print run finished, so a book reset for a "
     "second printing almost never repeats the errors of the first. Every surviving copy of the "
     "1543 edition carries exactly the same misprint in exactly the same place on page ninety. "
     "_____ all of them were pulled from a single setting of the type.",
     ["Thus,", "Nevertheless,", "For example,", "Meanwhile,"], "A",
     "The second sentence draws a conclusion from the shared misprint, so the link marks an "
     "inference. 'For example' would make the single setting an instance of the misprint, which "
     "makes no sense."),

 trn("T8",
     "Cast iron carries a compressive load as well as stone does, and mill builders used it for "
     "columns for the better part of a century. Pulled rather than pressed, it snaps with no "
     "warning at all. _____ a beam cast in iron may give no sign whatever before it fails.",
     ["In other words,", "Nevertheless,", "For example,", "Earlier,"], "A",
     "The final sentence restates the preceding one in the concrete case of a beam, so the link "
     "signals rephrasing. 'For example' is close but the sentence adds no new instance; it says "
     "the same thing about the same material."),

 trn("T9",
     "Until 1861 almost all the cotton spun in Lancashire came from a single source, and buyers in "
     "Liverpool judged every other crop in the world against it. _____ the mills were buying from "
     "Egypt and from India as well, and the trade never again rested on one country's harvest.",
     ["Thereafter,", "Likewise,", "In particular,", "Admittedly,"], "A",
     "'Until 1861' sets a boundary in time and the second sentence describes what happened after "
     "it, so the link is temporal. 'Likewise' would claim the later situation resembled the "
     "earlier one, when the passage says it differed."),

 # ------------------------------------------------------ Rhetorical Synthesis (9)
 syn("R1",
     ["The Aral Sea lost most of its volume after its two feeder rivers were diverted for irrigation in the 1960s.",
      "In 2005 a dam was finished across the strait joining the northern basin to the southern one.",
      "The water level in the northern basin rose eight metres in the seven months that followed.",
      "The southern basin, cut off from the northern one, has continued to shrink."],
     "specify the effect of the 2005 dam on the northern basin.",
     ["The Aral Sea lost most of its volume after its two feeder rivers were diverted in the 1960s.",
      "After a dam was finished across the strait in 2005, the water level in the northern basin rose eight metres in seven months.",
      "The southern basin of the Aral Sea has continued to shrink since it was cut off.",
      "Two rivers fed the Aral Sea before irrigation took their water away."],
     "B",
     "The goal asks for the dam's effect on the northern basin, and only the option pairing the "
     "2005 dam with the eight-metre rise supplies both the cause and the measured result. The "
     "southern-basin option reports what happened on the other side of the dam instead."),

 syn("R2",
     ["Katherine Johnson computed flight trajectories at Langley from 1953.",
      "Before the Friendship 7 flight in 1962, NASA had begun calculating orbits on electronic computers.",
      "John Glenn would not fly until Johnson had checked the machine's numbers herself.",
      "She worked through the same equations on a desk calculator and confirmed the result."],
     "explain why Johnson's hand calculation was carried out.",
     ["Katherine Johnson had been computing flight trajectories at Langley since 1953.",
      "Because John Glenn would not fly until the electronic computer's figures had been checked by hand, Johnson worked through the same equations herself and confirmed the result.",
      "NASA had begun calculating orbits on electronic computers before the 1962 flight.",
      "Johnson confirmed the orbital figures using a desk calculator."],
     "B",
     "The goal asks for the reason the check happened, so the option must join Glenn's refusal to "
     "fly to the calculation she then performed. The option reporting only that she used a desk "
     "calculator states the act without the reason for it."),

 syn("R3",
     ["New York Harbor once held roughly 220,000 acres of oyster reef.",
      "Dredging, landfill and sewage had destroyed almost all of it by 1920.",
      "A single adult oyster filters as much as 190 litres of water a day.",
      "Restoration projects have returned more than 100 million oysters to the harbour since 2014."],
     "explain why returning the oysters is expected to improve the water in the harbour.",
     ["New York Harbor once held roughly 220,000 acres of oyster reef, almost all of it destroyed by 1920.",
      "Since a single adult oyster filters as much as 190 litres a day, the more than 100 million oysters returned to the harbour since 2014 are expected to improve its water.",
      "Dredging, landfill and sewage destroyed the harbour's oyster reefs before 1920.",
      "Restoration projects have returned more than 100 million oysters to New York Harbor since 2014."],
     "B",
     "Only the option that multiplies one oyster's filtering rate by the number returned connects "
     "the restoration to the water quality the goal names. The option giving the number returned "
     "alone leaves out the filtering that makes the number matter."),

 syn("R4",
     ["Sequoyah could neither read nor write any language when he began work in 1809.",
      "He first tried giving every word its own symbol and gave the attempt up after several years.",
      "He then devised 85 symbols, one for each syllable in the Cherokee language.",
      "Within a few years of its adoption in 1821 a majority of Cherokee could read it."],
     "emphasise the change of approach that made the syllabary workable.",
     ["Sequoyah could neither read nor write any language when he began work in 1809.",
      "Having given up an attempt to provide every word with its own symbol, Sequoyah devised 85 symbols instead, one for each syllable of the language.",
      "Within a few years of its adoption in 1821, a majority of Cherokee could read the syllabary.",
      "Sequoyah worked on the problem from 1809 until the syllabary was adopted in 1821."],
     "B",
     "The goal names a change of approach, and only the option setting the abandoned "
     "word-by-word scheme against the 85 syllable symbols contains both halves of that change. The "
     "option about widespread reading records the outcome rather than the shift that produced it."),

 syn("R5",
     ["Power stations throw away most of the heat they produce while generating electricity.",
      "Copenhagen pipes that heat to buildings across the city instead of releasing it.",
      "About 98 percent of the city's buildings are connected to the network.",
      "The pipes run in a loop, so the cooled water returns to the plant to be heated again."],
     "explain what makes the city's heating network efficient.",
     ["About 98 percent of the buildings in Copenhagen are connected to the heating network.",
      "Copenhagen's network pipes to its buildings the heat that power stations would otherwise throw away while generating electricity.",
      "The pipes of the network run in a loop between the buildings and the plant.",
      "Power stations produce a great deal of heat as well as electricity."],
     "B",
     "Efficiency here means using heat that would have been wasted, and only one option states "
     "both the waste and its capture. The option giving the connection rate measures the network's "
     "reach without saying anything about what makes it efficient."),

 syn("R6",
     ["Drilling began on the Kola Peninsula in 1970 and was abandoned in 1992.",
      "The deepest hole reached 12,262 metres, roughly a third of the way through the crust.",
      "Rock at that depth proved much hotter than predicted, about 180 degrees Celsius.",
      "The heat made the rock behave plastically, and the hole kept closing on the drill."],
     "explain why the drilling stopped short of its target.",
     ["Drilling on the Kola Peninsula began in 1970 and was abandoned twenty-two years later.",
      "Rock at 12,262 metres proved far hotter than predicted, about 180 degrees Celsius, and behaved so plastically that the hole kept closing on the drill.",
      "The deepest hole reached about a third of the way through the earth's crust.",
      "The Kola hole is 12,262 metres deep, the deepest ever drilled."],
     "B",
     "The goal asks why the work stopped early, and only the option joining the unexpected heat to "
     "rock that flowed back into the hole gives a cause. The option reporting the abandonment date "
     "records that the drilling ended without saying why."),

 syn("R7",
     ["Farmers digging a well near Xi'an in 1974 struck fragments of fired clay.",
      "Excavation has since uncovered more than 8,000 life-size figures in three pits.",
      "The heads were formed in a small number of moulds and then modelled by hand.",
      "Traces of pigment show that the figures were originally painted."],
     "explain how the figures could be individually detailed and mass-produced at the same time.",
     ["Farmers digging a well near Xi'an in 1974 struck the first fragments of fired clay.",
      "Although the heads came from only a handful of moulds, each was modelled by hand afterwards, so the figures are individual and mass-produced at once.",
      "Excavation has uncovered more than 8,000 life-size figures in three pits.",
      "Traces of pigment show that the figures were painted when they were made."],
     "B",
     "The goal requires both sides of the paradox, and only the option combining the handful of "
     "moulds with the hand modelling that followed supplies them. The option giving the total "
     "number of figures speaks to scale alone."),

 syn("R8",
     ["The steelpan was developed in Trinidad during the 1930s and 1940s.",
      "Players began with biscuit tins and brake drums before turning to discarded oil drums.",
      "The playing surface is sunk into a shallow bowl and divided into note areas by hammering.",
      "Each area is then worked thinner or thicker until it sounds the pitch the tuner wants."],
     "explain how a particular pitch is produced on the instrument.",
     ["The steelpan was developed in Trinidad during the 1930s and 1940s.",
      "The playing surface is sunk into a shallow bowl and divided by hammering into areas, each worked thinner or thicker until it sounds the pitch the tuner wants.",
      "Players used biscuit tins and brake drums before they turned to discarded oil drums.",
      "The steelpan is made from a discarded oil drum rather than from purpose-built material."],
     "B",
     "The goal is about producing a pitch, and only the option describing the division into areas "
     "and the thinning or thickening of each explains how a note is arrived at. The option about "
     "biscuit tins and brake drums is a point of origin, not a method of tuning."),

 syn("R9",
     ["A lighthouse lens has to be large to gather light, and a solid lens that size would be too heavy to turn.",
      "Augustin-Jean Fresnel cut the lens into concentric rings in 1822.",
      "Each ring bends light through the same angle as the corresponding part of a solid lens would.",
      "The glass between the rings, which had only added weight, was left out."],
     "explain how the design cut the weight of the lens without weakening the beam.",
     ["Augustin-Jean Fresnel cut the lighthouse lens into concentric rings in 1822.",
      "Because each ring bends light through the same angle as the corresponding part of a solid lens, the glass between the rings, which had only added weight, could be left out.",
      "A lighthouse lens must be large if it is to gather enough light to be seen at a distance.",
      "A solid glass lens large enough for a lighthouse would be too heavy to turn."],
     "B",
     "The goal names both weight and beam, and only the option pairing the preserved bending angle "
     "with the omitted glass accounts for the two together. The option stating that a solid lens "
     "would be too heavy sets out the problem without describing the solution."),

]

DROPPED = {}
