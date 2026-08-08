#!/usr/bin/env python3
"""
Reading & Writing authored for Test 11.

All 81 items are original. The transcribed pool was spent by Test 8, and for
R&W authoring is in any case the safer route: a transcribed key has to be
re-derived by hand before it can be trusted (Test 5 shipped 6 wrong answers in
81 that way). Every item below carries a `why` that records the reasoning which
produced the key AND the reason the strongest distractor fails — that record is
the verification, so no key exists here without one.

Rationales name options by their CONTENT, never by letter, so balance_rw.py is
free to rotate every question when it evens out the key distribution.

Writing-domain choices are never bare punctuation. Test 8 shipped Boundaries
items whose four options were ", " / "; " / ": " / " and ", which a student sees
as four empty rows. The real test repeats the words on either side of the blank
inside every option so the choice reads as the resulting sentence, and every
Boundaries item here is written that way from the start. Form/Structure items
whose options are genuinely words ("was" / "were") are left as words, which is
also how the real test presents them.

Topics were checked against rw_test8.py, rw_test9.py and rw_test10.py in full
and nothing is reused: axolotls, periodical cicadas, Marshall Islands stick
charts, Jacob Lawrence, shipping containers, Antarctic icefish, Gee's Bend,
Maine lobster gangs, zircon, Kevlar, Vermeer's optics, desert locusts, Great
Zimbabwe, sunstones, the marine chronometer, Lalibela, Wald's armour, the steel
pan, nitinol, naked mole-rats, the Loess Plateau, glass sponges, Braille,
tsunami stones, vanilla, monarch navigation, Nazca, polders, anchoring,
terracotta-army chromium, serotinous cones, auto-enrolment, island dwarfing,
treelines, IceCube, aluminium, Foucault, permafrost carbon, saffron, census
undercount, oracle bones, reindeer herding, Fresnel lenses, the Hanse,
cross-laminated timber, magnetic reversals, crater-lake gas, burdock hooks,
salt cod, Sinan, participatory budgeting, Anni Albers, heat pumps, bomb-pulse
radiocarbon, error correction, cooling centres, clock rates with altitude, wind
tunnels, kente, vulcanisation, glacial erratics, Nok terracotta, Cavendish,
kohanga reo, the Chartists, mantis shrimp, Galton's ox, Prussian blue, slime
mould and the Landnamabok.

Block counts (fixed by the assembler's quota, 3 modules x 27):
    Words in Context 15, Text Structure and Purpose 6,
    Central Ideas and Details 6, Command of Evidence 9, Inferences 6,
    Boundaries 12, Form, Structure, and Sense 9, Transitions 9,
    Rhetorical Synthesis 9                                        = 81
"""

SOURCE = "AUTHORED-T11"
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
     "An axolotl that loses a limb grows the whole thing back &mdash; bone, muscle, nerve and skin, "
     "in the right order and at the right size &mdash; and no scar is left where the break was. "
     "Biologists who study wound healing in mammals are interested in the animal precisely because "
     "its response to injury is _____ rather than merely protective.",
     ["defensive", "regenerative", "cosmetic", "temporary"], "B",
     "The passage describes a lost limb being rebuilt entirely, and the sentence sets the blank "
     "against 'merely protective', so the word has to name rebuilding. The 'defensive' option "
     "simply restates the protective response that the sentence is contrasting."),

 wic("W2",
     "Periodical cicadas spend either thirteen or seventeen years underground and then emerge all "
     "at once. Both numbers are prime, so a predator whose own population peaks every two, three "
     "or four years can almost never have its own peak _____ with an emergence. Broods that shared "
     "a cycle with their predators were eaten out long ago.",
     ["compete", "interfere", "coincide", "alternate"], "C",
     "The sentence needs a word for two cycles falling in the same year, which is what a prime "
     "interval prevents. The 'alternate' option describes cycles that take turns, which is the "
     "opposite of what a predator would need."),

 wic("W3",
     "Navigators in the Marshall Islands built charts from palm ribs and shells, but the ribs do "
     "not stand for islands or coastlines. They map the way ocean swells bend around land, and a "
     "navigator studied the chart ashore and left it at home before sailing. The object is "
     "therefore less a map than a _____ for a body of knowledge carried in the head.",
     ["substitute", "mnemonic", "receipt", "container"], "B",
     "The chart is memorised on land and deliberately left behind, so its use is to fix knowledge "
     "in the memory. The 'substitute' option fails for the same reason: nothing that stands in for "
     "the knowledge would be left at home on the voyage where the knowledge is needed."),

 wic("W4",
     "Jacob Lawrence painted the sixty panels of the Migration Series on one table at one time, "
     "mixing a colour and laying it on every panel that needed it before mixing the next. The "
     "result is a palette so _____ across the whole sequence that the panels read as a single work "
     "rather than as sixty separate paintings.",
     ["consistent", "vivid", "restrained", "unpredictable"], "A",
     "One batch of each colour used across all sixty panels makes the palette the same throughout, "
     "which is what holds the sequence together as one work. The 'restrained' option describes how "
     "intense the colours are, not whether they match from panel to panel."),

 wic("W5",
     "Before standardisation, cargo was loaded piece by piece and a ship could sit at a wharf for a "
     "week. The shipping container changed less about the box than about everything around it: "
     "cranes, chassis, railway wagons and hulls were all rebuilt to one set of dimensions. Its "
     "power lay in being _____ rather than in any property of the steel it was made from.",
     ["interchangeable", "durable", "spacious", "inexpensive"], "A",
     "Everything that handles the box is built to the same dimensions, so any container fits any "
     "crane, chassis or hold, which is what the sentence contrasts with a property of the steel. "
     "The 'durable' option names exactly the kind of material property being ruled out."),

 wic("W6",
     "The water under the Antarctic sea ice sits below the freezing point of ordinary blood. "
     "Notothenioid fish live in it because their blood carries proteins that fasten onto the first "
     "ice crystals to appear and stop them growing any further. The proteins do not warm the fish "
     "at all; they simply keep the crystals _____.",
     ["minute", "dissolved", "mobile", "uniform"], "A",
     "Growth is halted at the moment a crystal forms, so what the proteins maintain is small size. "
     "The 'dissolved' option would mean no crystal exists, whereas the passage says the crystals "
     "form and are then held in check."),

 wic("W7",
     "The quilts made at Gee's Bend were pieced from worn work clothes and feed sacks, and their "
     "makers had no use for the repeating block patterns sold in catalogues. Strips run off at an "
     "angle; a colour stops where the cloth ran out. What looks _____ is in fact the outcome of "
     "choices made stitch by stitch with whatever material was to hand.",
     ["improvised", "traditional", "accidental", "laborious"], "C",
     "The sentence opposes the look of the quilts to the choices behind them, so the blank has to "
     "name something unchosen. The 'improvised' option still credits the maker with deciding on "
     "the spot, which is the very thing the sentence goes on to affirm rather than deny."),

 wic("W8",
     "Economists long assumed that a fishery open to everyone would be stripped bare. The "
     "lobstering harbours of the Maine coast are a standing exception: the gang working out of each "
     "harbour settles who may set traps in its waters, how many and where, and enforces those "
     "limits itself. Access to the ground is neither free nor state-controlled but _____ by the "
     "fishermen who work it.",
     ["rationed", "abandoned", "advertised", "subsidised"], "A",
     "Deciding who may fish, how many traps and where is the allotting of a limited resource, and "
     "the sentence rules out both open access and state control. The 'subsidised' option describes "
     "money paid to the fishermen, which the passage never mentions."),

 wic("W9",
     "Most minerals are reset by the heat of burial and re-melting. Zircon is not. A crystal that "
     "grew four billion years ago can pass through mountain-building, erosion and burial inside a "
     "sandstone and still hold the uranium clock sealed in it. What makes the mineral so useful to "
     "geologists is that it is so nearly _____.",
     ["indestructible", "abundant", "transparent", "recent"], "A",
     "Surviving mountain-building, erosion and reburial with its internal clock intact is a claim "
     "about resisting destruction. The 'abundant' option speaks to how much zircon there is, which "
     "the passage never raises."),

 wic("W10",
     "Stephanie Kwolek was looking for a fibre stiff enough to reinforce tyres when a batch of "
     "polymer came out of the reactor cloudy instead of clear. Standard practice was to throw such "
     "a batch away. She had it spun anyway, and the fibre that came off the spinneret was stronger "
     "by weight than steel &mdash; an outcome that owed as much to her refusal to treat the oddity "
     "as _____ as it did to the chemistry.",
     ["worthless", "novel", "hazardous", "reproducible"], "A",
     "Standard practice was to discard the cloudy batch, so treating the oddity in the usual way "
     "would have meant judging it of no value. The 'novel' option describes the batch as new and "
     "interesting, which is what she in fact did with it rather than what she refused to do."),

 wic("W11",
     "No lens appears in any inventory of Vermeer's possessions, and the case that he worked with a "
     "camera obscura rests on the paintings themselves: highlights rendered as small unfocused "
     "discs, foreground objects blurred in a way the eye does not blur them. The evidence is _____ "
     "rather than documentary, which is why the question is still argued over.",
     ["circumstantial", "conclusive", "anecdotal", "fabricated"], "A",
     "The paintings point to a lens without recording one, and the sentence sets that against "
     "documentary proof, which is what indirect evidence means. The 'anecdotal' option would mean "
     "second-hand reports, whereas what the passage offers is physical detail in the pictures."),

 wic("W12",
     "A desert locust reared on its own is green, sluggish and solitary. Crowd it &mdash; brush the "
     "hind legs of enough individuals against one another &mdash; and within hours it starts to "
     "change colour, eat more and seek out others of its kind. The two forms were once described as "
     "separate species, so _____ is the change that crowding sets off.",
     ["thorough", "gradual", "reversible", "familiar"], "A",
     "Trained naturalists took the two forms for different species, which means the change goes "
     "all the way through the animal. The 'gradual' option is contradicted by the passage's 'within "
     "hours'."),

 wic("W13",
     "The walls at Great Zimbabwe were laid without mortar, in courses of granite blocks split from "
     "the surrounding hills with fire and water. The finest of the coursing is so _____ that a "
     "blade cannot be pushed between two stones, and the walls have stood for six centuries with "
     "nothing binding them together.",
     ["precise", "decorative", "recent", "irregular"], "A",
     "Joints too tight for a blade are a matter of exact fit, which is also what allows a mortarless "
     "wall to stand. The 'decorative' option describes appearance and would not explain why the "
     "wall holds up without mortar."),

 meaning("W14",
     "Clay dug from the riverbank cracks as it dries unless something coarse is worked into it "
     "first. The potters at this site used crushed shell, and the <u>temper</u> in a sherd is often "
     "the quickest way to tell one workshop's output from another's, since what was added was "
     "usually whatever lay nearest to hand.",
     "temper",
     ["A habitual state of mind.",
      "Coarse material mixed into clay before it is fired.",
      "The hardness given to steel by heating and cooling it.",
      "A moderating influence on a dispute."],
     "B",
     "The passage defines the term as it uses it: something coarse worked into the clay, here "
     "crushed shell. The steel-hardening sense is a real meaning of the word but nothing in the "
     "passage concerns metal."),

 meaning("W15",
     "The survey party mapped the valley floor in a fortnight, but the plateau above it took a "
     "month. On flat ground a single reading serves for a wide area; where the <u>relief</u> is "
     "broken the instrument has to be moved every few hundred metres, and each new station has to "
     "be tied back to the last.",
     "relief",
     ["The easing of pain or distress.",
      "Assistance given to people in need.",
      "Variation in the height of a land surface.",
      "A design carved so that it projects from a flat background."],
     "C",
     "The word is contrasted with flat ground and is what forces the instrument to be moved, so it "
     "names the ups and downs of the terrain. The carving sense is a genuine meaning of the word "
     "but has nothing to do with survey stations on a plateau."),

 # --------------------------------------------- Text Structure and Purpose (6)
 tsp("S1",
     "The sagas say that Norse sailors carried a sunstone that showed where the sun stood on an "
     "overcast day. Crystals of Iceland spar split light into two beams whose relative brightness "
     "depends on how the sky above is polarised. <u>Turning the crystal until the two beams match "
     "identifies the plane of polarisation, and that plane points back towards the sun.</u> "
     "A crystal of just this kind was lifted from an Elizabethan wreck in the Channel in 2013.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It explains the physical principle by which the described object would work.",
      "It questions whether the sagas can be trusted on the matter.",
      "It describes the circumstances in which a crystal was recovered from a wreck.",
      "It compares Iceland spar with other crystals available to Norse sailors."],
     "A",
     "The sentence sets out the procedure and the optics that turn a crystal into a direction "
     "finder, which is what makes the saga claim workable. The recovery from the wreck is the "
     "business of the closing sentence, not of the underlined one."),

 tsp("S2",
     "Finding longitude at sea means comparing local noon with the time at a known meridian, and "
     "that requires a clock that keeps time on a rolling deck through months of heat and damp. The "
     "astronomers of the Board of Longitude expected the answer to come from tables of the moon's "
     "position. It came instead from a Yorkshire joiner whose fourth timekeeper lost a few seconds "
     "on the passage to Jamaica. The prize was paid only after a long argument and the "
     "intervention of the king.",
     "Which choice best states the main purpose of the text?",
     ["To explain a navigational problem and describe the unexpected source of its solution.",
      "To argue that lunar tables were never a workable method of finding longitude.",
      "To trace the development of clock escapements during the eighteenth century.",
      "To criticise the Board of Longitude for its treatment of rival methods."],
     "A",
     "The text states the problem, names the solution the experts anticipated, and then reports "
     "where the working solution actually came from. The argument over the prize is one sentence "
     "at the end and is reported rather than pressed as a criticism."),

 tsp("S3",
     "The churches at Lalibela were not built up from the ground. Masons began at the surface of a "
     "slab of red volcanic rock, cut a trench around the block they wanted, and then worked "
     "downwards and inwards, hollowing nave, aisles and windows out of a single mass of stone. "
     "Nothing was assembled and nothing can be added. A church of this kind is finished the moment "
     "the last chip is carried out of it.",
     "Which choice best describes the overall structure of the text?",
     ["It states what the method is not, describes what it is, and draws out a consequence of it.",
      "It presents two theories of how the churches were made and endorses one of them.",
      "It narrates the reign of the king who commissioned the churches.",
      "It lists the churches in the order in which they were carved."],
     "A",
     "The opening denies that the churches were built up, the middle describes cutting down into "
     "the rock, and the close draws the consequence that nothing can be added afterwards. No "
     "second theory is ever stated, so nothing is being weighed against anything."),

 tsp("S4",
     "Analysts in 1943 mapped the bullet holes in aircraft returning from raids over Europe and "
     "proposed adding armour wherever the holes clustered. <u>Abraham Wald pointed out that the "
     "sample consisted entirely of aircraft that had come back.</u> Hits to the engines were rare "
     "in the data not because engines were seldom struck but because an aircraft struck there did "
     "not return to be examined. The armour went on the engines.",
     "Which choice best describes the function of the underlined sentence?",
     ["It identifies the flaw in the reasoning that the rest of the text goes on to explain.",
      "It supplies statistical support for the analysts' original proposal.",
      "It describes the method by which the bullet holes were mapped.",
      "It concedes that Wald's recommendation was never adopted."],
     "A",
     "Naming what the sample leaves out is the objection, and the following sentence spells out why "
     "that omission inverts the conclusion. The final sentence reports that the armour did go on "
     "the engines, so nothing is conceded about the recommendation being ignored."),

 tsp("S5",
     "The steel pan began with oil drums left on the wharves of Trinidad after the Second World "
     "War. Players noticed that a dented drumhead sounded more than one note, and set about placing "
     "the dents on purpose, sinking the head into a shallow bowl and hammering out a facet for each "
     "pitch. Tuning a pan still means striking, listening and striking again; the note is shaped "
     "rather than fitted.",
     "Which choice best states the main purpose of the text?",
     ["To describe how an instrument was developed out of salvaged material and how it is made.",
      "To argue that the steel pan deserves a place in the orchestral repertoire.",
      "To compare the steel pan with other percussion instruments of the Caribbean.",
      "To explain why oil drums were abundant in Trinidad after the war."],
     "A",
     "The text moves from where the drums came from to how the notes are hammered into them, so it "
     "is an account of origin and manufacture. Why the drums were lying on the wharves is given in "
     "half of one clause and is not what the rest of the text is about."),

 tsp("S6",
     "An alloy of nickel and titanium in roughly equal parts can be bent flat and will spring back "
     "to its original shape when it is warmed. <u>The metal has two crystal structures, and the "
     "change from one to the other is set off by temperature rather than by force.</u> Surgeons "
     "make use of this: a stent folded small enough to travel up an artery opens itself out at body "
     "heat, with no mechanism that could fail.",
     "Which choice best describes the function of the underlined sentence?",
     ["It gives the mechanism that accounts for the behaviour just described.",
      "It raises a limitation of the alloy that the final sentence resolves.",
      "It explains why nickel and titanium are combined in equal proportions.",
      "It describes a surgical application of the alloy."],
     "A",
     "The sentence supplies the two crystal structures and the temperature trigger, which is the "
     "reason the metal recovers its shape when warmed. The stent is the application, and it belongs "
     "to the sentence that follows."),

 # ----------------------------------------------- Central Ideas and Details (6)
 cid("C1",
     "A naked mole-rat colony has one breeding female. The rest of the animals &mdash; several "
     "dozen, sometimes hundreds &mdash; dig, carry food and defend the tunnels without reproducing "
     "at all, and they will go on doing so for years. Suppress the queen's scent and several of the "
     "other females begin to develop ovaries within days. What holds the arrangement in place is "
     "therefore not anatomy but the queen's continuing presence.",
     "Which choice best states the main idea of the text?",
     ["Naked mole-rats are the only mammals known to live underground in large groups.",
      "Non-breeding mole-rats stay that way because of the queen's presence, not because they are incapable of breeding.",
      "A naked mole-rat colony collapses as soon as its queen dies.",
      "Work in a mole-rat colony is divided among the animals according to their age."],
     "B",
     "Ovaries developing within days of the queen's scent being removed shows the other females are "
     "able to breed and are being held back, which is what the closing sentence states. The passage "
     "reports that the females develop, not that the colony collapses, so the collapse option goes "
     "beyond the text."),

 cid("C2",
     "Wind-blown silt lies hundreds of metres deep across the Loess Plateau, and it is fertile, "
     "soft and easily washed away; the Yellow River takes both its name and its colour from it. "
     "From 1999 farmers on the plateau were paid to stop cultivating the steepest slopes and to "
     "plant them instead. Grain output did not fall, because the terraced ground lower down now "
     "held the water that had previously run off it, and the sediment reaching the river dropped by "
     "more than half.",
     "According to the text, why did grain output hold up after the steepest slopes were retired?",
     ["Farmers were compensated in grain for the land they took out of cultivation.",
      "The terraced land lower down retained water that had previously run off, making up for the lost slopes.",
      "The steepest slopes had never produced much grain in the first place.",
      "Sediment removed from the river was returned to the fields as fertiliser."],
     "B",
     "The text gives the reason directly: water that used to run off the slopes was now held on the "
     "terraces below. Payment to the farmers is mentioned, but it is payment to stop cultivating, "
     "not compensation in grain that would offset a lost harvest."),

 cid("C3",
     "The skeleton of a Venus's flower basket is spun from silica at the temperature of the deep "
     "sea, with neither heat nor pressure to help. Its lattice of struts is braced diagonally at "
     "every corner, and the fibres themselves are laid down in layers of alternating thickness, so "
     "that a crack running through one layer is stopped at the next. Engineers who have modelled "
     "the structure find little in it that could be taken away without weakening the whole.",
     "Which choice best states the main idea of the text?",
     ["The sponge builds an efficiently braced, crack-resistant skeleton at ordinary deep-sea temperatures.",
      "Silica is a stronger material than the alloys ordinarily used in engineering.",
      "The sponge grows more slowly than other animals of comparable size.",
      "Engineers have succeeded in manufacturing copies of the sponge's skeleton."],
     "A",
     "Diagonal bracing, crack-stopping layers and nothing spare in the design are all points about "
     "an efficient structure, and the passage stresses that it is made in cold water without heat "
     "or pressure. The passage says engineers have modelled the skeleton, which is not the same as "
     "having built one."),

 cid("C4",
     "Embossed alphabets for blind readers already existed when Louis Braille was a student. They "
     "used raised versions of ordinary letters, which a sighted teacher could read at a glance. "
     "Braille's system does not resemble the alphabet at all. Each cell is small enough to sit "
     "under a fingertip without the finger having to travel across it, and, unlike raised letters, "
     "it can be written by a blind person as readily as it can be read. Schools resisted it for "
     "decades.",
     "Which choice best states the main idea of the text?",
     ["Braille's system was adopted quickly because teachers found it easy to learn.",
      "Braille's system was designed around the reader's finger and hand rather than the sighted teacher's eye.",
      "Raised-letter alphabets were invented only after Braille's system had appeared.",
      "Blind readers before Braille had no means of reading at all."],
     "B",
     "The cell fits under a fingertip and the system can be written as well as read by a blind "
     "person, in contrast to a script shaped so that sighted teachers could read it. The closing "
     "sentence says schools resisted the system for decades, which contradicts the quick-adoption "
     "option."),

 cid("C5",
     "Carved stones stand on hillsides along the Sanriku coast of Japan, some of them six centuries "
     "old, marking the height a wave once reached and warning against building below the line. "
     "Villages that kept to the warning came through 2011 intact; several that had spread downhill "
     "in the intervening decades did not. The stones give no dates and predict nothing. They record "
     "only how far the water once came.",
     "Which choice best states the main idea of the text?",
     ["The stones preserve a record of past wave heights that proved a reliable guide to safe ground.",
      "The stones were placed by scientists who had calculated the likely height of future waves.",
      "Every village along the Sanriku coast observed the warnings carved on the stones.",
      "The stones were the only structures left standing along the coast after 2011."],
     "A",
     "The text says twice over what the stones do &mdash; they mark how far the water came &mdash; "
     "and reports that settlements above the line survived. The passage explicitly denies that the "
     "stones predict anything, which rules out the option crediting them to calculation of future "
     "waves."),

 cid("C6",
     "The vanilla orchid is pollinated in Mexico by insects that live nowhere else, so plants "
     "carried to other colonies flowered and set nothing. In 1841 Edmond Albius, a twelve-year-old "
     "enslaved on R&eacute;union, worked out that lifting the flap which separates the flower's "
     "male and female parts with a sliver of bamboo and pressing the two together does the job by "
     "hand. The method is still used, flower by flower, on the one morning each bloom is open.",
     "According to the text, why did vanilla grown outside Mexico fail to produce pods before 1841?",
     ["The soils of the colonies were unsuited to the orchid.",
      "The insects that pollinate the flower were not present.",
      "The flowers opened for too short a time to be harvested.",
      "Growers had not yet learned how to cure the pods properly."],
     "B",
     "The first sentence ties the failure to pollinators that live only in Mexico, and the rest of "
     "the passage describes replacing them by hand. The brief opening of the bloom is mentioned as "
     "a constraint on the hand method, not as the reason the plants set nothing beforehand."),

 # ---------------------------------------------------- Command of Evidence (9)
 coe("E1",
     "Monarch butterflies flying south in autumn hold a steady bearing over hundreds of kilometres. "
     "Biologist Iris Mwangi argues that they steer by the sun, correcting for its movement across "
     "the sky with an internal clock, rather than by the Earth's magnetic field.",
     "Which finding, if true, would most directly support Mwangi's argument over the alternative?",
     ["Butterflies held for several days under lights shifted six hours out of step with the sun set off on a bearing rotated by a correspondingly predictable amount.",
      "Monarchs from eastern and western populations travel to separate wintering grounds.",
      "Monarchs continue to fly south on days when the sky is completely overcast.",
      "Magnetite has been found in the body tissue of several migratory insects."],
     "A",
     "Shifting the internal clock while leaving the magnetic field untouched changes the bearing by "
     "just the amount a sun-and-clock mechanism predicts, which the magnetic account cannot "
     "explain. Flying on under complete overcast would tell against the sun account rather than "
     "for it."),

 coe("E2",
     "The geoglyphs on the Nazca plain are best seen from the air, which nobody could reach for "
     "centuries after they were made. Archaeologist Paulo Ferrari argues that the lines were meant "
     "to be walked in procession rather than viewed whole.",
     "Which finding, if true, would most directly support Ferrari's argument?",
     ["Each figure is drawn as a single continuous line that returns to its starting point, and the ground along the lines is compacted by heavy foot traffic.",
      "Several of the largest figures are visible from hills at the edge of the plain.",
      "The plain is one of the driest places on earth, which is why the lines have survived.",
      "Some of the figures depict animals that do not live anywhere in the region."],
     "A",
     "An unbroken path that returns to where it began is a route to be walked, and compaction is "
     "the physical trace of people walking it. Visibility from the surrounding hills supports "
     "viewing the figures rather than moving along them."),

 coe("E3",
     "Draining a lake behind a dyke meant lifting water higher than any single mill could raise it. "
     "Historian Joost Bakker maintains that the decisive innovation in the great Dutch reclamations "
     "of the seventeenth century was organisational &mdash; the joint-stock company that financed "
     "and coordinated the work &mdash; rather than mechanical.",
     "Which finding, if true, would most directly support Bakker's claim?",
     ["Mills capable of the necessary lift had been in use for a century before the large reclamations began, and no lake of that size was drained until the companies were formed.",
      "The mills built for the reclamations turned to face the wind on a movable cap.",
      "Reclaimed land sold for several times what it had cost to drain it.",
      "Peat cutting had enlarged many of the lakes that were later drained."],
     "A",
     "Holding the machinery constant for a century and dating the drainings to the arrival of the "
     "companies isolates the finance and coordination as what changed. The movable cap is a "
     "mechanical improvement, which is the explanation the claim is arguing against."),

 coe("E4",
     "Asked to estimate a quantity they cannot look up, people are pulled towards any number they "
     "have just been shown, even one they know to be irrelevant. Psychologist Nils Hartmann argues "
     "that the effect is not simply a matter of inattention.",
     "Which finding, if true, would most directly support Hartmann's argument?",
     ["Participants who were warned about the effect beforehand and paid a bonus for accuracy were pulled towards the number just as strongly as those who were not.",
      "Participants shown a larger number gave larger estimates than participants shown a smaller one.",
      "Participants took longer to answer when the number they had been shown was wildly implausible.",
      "Experts estimating quantities in their own field are pulled towards the number less than novices are."],
     "A",
     "Warning and payment remove the excuse of not attending, and the effect survives both, which "
     "is precisely the claim. The finding that a larger number produces larger estimates only "
     "establishes that the effect exists, which nobody in the passage disputes."),

 coe("E5",
     "The bronze weapons buried with the terracotta army came out of the ground bright. Chromium "
     "was detected on their surfaces, and for decades this was read as a deliberate anti-corrosion "
     "treatment two thousand years ahead of its time. A conservator now argues that the chromium "
     "came from lacquer applied to the wooden hafts and the fittings of the pit, and migrated onto "
     "the metal.",
     "Which finding, if true, would most directly support the conservator's argument?",
     ["Chromium appears on the blades only where they lay against lacquered material and is absent from weapons buried away from it.",
      "The bronze itself contains tin at a level that resists corrosion well.",
      "The soil of the pit is mildly alkaline, which slows the corrosion of bronze.",
      "Lacquer was used widely in the workshops that supplied the tomb."],
     "A",
     "Chromium tracking contact with lacquer, and vanishing where there was none, is what migration "
     "predicts and what a deliberate coating would not. Widespread use of lacquer in the workshops "
     "shows only that the source was available, not that it reached the blades."),

 coe("E6",
     "Lodgepole pines in some stands hold their seed in cones sealed with resin that opens only in "
     "the heat of a fire; in other stands the cones open as they ripen. Ecologist Dawn Ferreira "
     "argues that the sealed form is favoured where fire sweeps through a stand at intervals "
     "shorter than the lifespan of a tree.",
     "Which finding, if true, would most directly support Ferreira's argument?",
     ["The proportion of trees bearing sealed cones is highest in the stands whose fire scars record the shortest intervals between burns.",
      "Sealed cones keep seed viable for longer than cones that open as they ripen.",
      "Lodgepole seedlings grow faster on ground cleared by fire than under a closed canopy.",
      "Squirrels harvest cones of both kinds at similar rates."],
     "A",
     "Matching the frequency of the sealed form to the measured fire interval is the correlation "
     "the argument predicts. Longer seed viability explains how the sealed form could work but says "
     "nothing about where it is common, which is what the claim is about."),

 coe("E7",
     "When a firm changes its retirement plan so that employees are enrolled unless they opt out, "
     "participation rises sharply. Economist Amara Silva argues that the rise comes from the effort "
     "of filling in a form rather than from any signal that enrolment is what the employer "
     "recommends.",
     "Which finding, if true, would most directly support Silva's argument?",
     ["Participation rose just as much at firms that told employees in writing that the default carried no recommendation.",
      "Participation rose most sharply among the youngest employees at each firm.",
      "Employees enrolled by default went on contributing at the default rate for years afterwards.",
      "Firms that adopted the automatic default also increased their matching contributions."],
     "A",
     "Telling employees the default means nothing removes the recommendation while leaving the "
     "paperwork exactly as it was, so an undiminished rise points to the effort. Continuing at the "
     "default rate for years is consistent with either explanation of why people enrolled."),

 coe("E8",
     "Elephants that reached Mediterranean islands in the Pleistocene evolved to a fraction of the "
     "size of their mainland ancestors. Palaeontologist Yusuf Demir argues that the driver was the "
     "limited food supply of a small island rather than the absence of large predators.",
     "Which finding, if true, would most directly support Demir's argument?",
     ["Across the islands studied, the degree of dwarfing tracks island area closely and shows no relation to whether large predators were present.",
      "No fossils of large carnivores have been recovered from any of the islands.",
      "Dwarf elephants reached maturity at a younger age than mainland elephants did.",
      "Mainland elephants of the same period were among the largest land mammals ever to live."],
     "A",
     "Size tracking area, and not tracking predators, separates the two explanations in exactly the "
     "way the claim requires. Finding no carnivores anywhere leaves the predator variable constant, "
     "so it cannot distinguish between the accounts at all."),

 coe("E9",
     "The upper edge of the forest on several Scandinavian mountainsides has climbed tens of metres "
     "since 1950, and birch now grows on ground that was open fell within living memory. Summers in "
     "the region have warmed over the same period, and the sheep and cattle that were driven up to "
     "the high pastures each June have almost all gone. Ecologist Sanna Virtanen argues that the "
     "cause of the shift is the ending of that grazing rather than the warming.",
     "Which finding, if true, would most directly support Virtanen's argument?",
     ["On slopes where summer grazing continued at the same intensity throughout, the treeline did not move despite the same rise in temperature.",
      "Summer temperatures across the region have risen by roughly one degree since 1950.",
      "Seedlings above the present treeline survive better in warm years than in cold ones.",
      "Grazing animals eat tree seedlings as readily as they eat grass."],
     "A",
     "Warming applies to grazed and ungrazed slopes alike, so a treeline that moves only where the "
     "grazing stopped points at the grazing. Seedlings surviving better in warm years is what the "
     "climate explanation would predict."),

 # -------------------------------------------------------------- Inferences (6)
 inf("I1",
     "A neutrino crossing the Antarctic ice sheet very occasionally strikes a nucleus, and the "
     "collision throws off a faint flash of blue light. Detectors frozen into the ice reconstruct "
     "the neutrino's direction from the timing of that flash across a cubic kilometre of "
     "instruments. Because the light has to travel hundreds of metres before it reaches the nearest "
     "sensor, the array could not have been built in ice that was _____",
     ["free of trapped air bubbles.",
      "anything less than exceptionally clear.",
      "colder than the bedrock beneath it.",
      "younger than a few thousand years."],
     "B",
     "Light crossing hundreds of metres to be detected at all requires ice that scatters almost "
     "nothing, so poor transparency would defeat the method. Trapped bubbles are what spoils "
     "clarity, so ice free of them is what the array needs rather than what it cannot use."),

 inf("I2",
     "Aluminium is the most abundant metal in the earth's crust, but it occurs only in compounds "
     "that hold onto it tightly. Until an electrolytic process was worked out in 1886, freeing it "
     "took so much effort that a bar of the metal was displayed in Paris beside the crown jewels. "
     "The price collapsed within a decade of 1886, which suggests that the metal's earlier value "
     "had reflected _____",
     ["the rarity of the element itself.",
      "the difficulty of separating it from its ores.",
      "a passing fashion for light metals among European jewellers.",
      "the small number of deposits then known."],
     "B",
     "Nothing about how much aluminium is in the ground changed in 1886; only the method of "
     "extraction did, so the price must have been tracking the cost of extraction. The passage "
     "opens by calling the metal the most abundant in the crust, which rules out rarity and a "
     "shortage of deposits alike."),

 inf("I3",
     "A pendulum set swinging is acted on by gravity and by the tension in its wire, and neither "
     "force can turn the plane in which it swings. Yet the plane of a long pendulum hung in Paris "
     "is observed to rotate steadily through the day. Since nothing is turning the pendulum, what "
     "is actually rotating must be _____",
     ["the wire from which the pendulum hangs.",
      "the building and the ground beneath it.",
      "the bob about its own axis.",
      "the air through which the bob passes."],
     "B",
     "The passage rules out any force capable of turning the plane of swing, so the apparent "
     "rotation has to belong to the frame the observer is standing in. The wire and the bob are "
     "parts of the pendulum, which the passage has just said is not being turned."),

 inf("I4",
     "Plant matter that fell on the Siberian tundra thousands of years ago did not rot. It froze "
     "before the soil organisms could break it down and has been locked in the ground ever since. "
     "Those organisms are still present, and they resume feeding as soon as the soil thaws. Where "
     "the permafrost thaws, then, the carbon held in that ancient material _____",
     ["remains fixed in the soil indefinitely.",
      "begins to be released as the organisms resume feeding on it.",
      "is taken up by the plants growing above it.",
      "sinks below the depth at which soil organisms live."],
     "B",
     "Only the freezing stopped the decay, and the organisms are described as still present and "
     "ready to act, so thawing restarts the process that releases the carbon. Remaining fixed "
     "indefinitely is what the frozen state provided and what thawing ends."),

 inf("I5",
     "Saffron is the dried stigma of a crocus, three to a flower, and the flowers open for a few "
     "days in autumn and have to be picked at dawn before the sun opens them fully. No machine has "
     "been built that can take the stigmas out. That the spice is still the most expensive in the "
     "world by weight is therefore largely a matter of _____",
     ["the small area of land on which the crocus will grow.",
      "the hand labour that each gram of it requires.",
      "the difficulty of storing the dried stigmas.",
      "the demand for it in a handful of cuisines."],
     "B",
     "Three stigmas per flower, a dawn harvest and no machine that can do the work all point to the "
     "hours of human work behind a small quantity. The passage says nothing about where the crocus "
     "can be grown or how the harvest is stored."),

 inf("I6",
     "A census that misses people does not miss them at random: those in irregular housing, those "
     "moving between addresses and those wary of officials are all harder to count. The formulas "
     "that distribute public money per head are calculated from the census total. Districts where "
     "such households are concentrated are therefore likely to receive _____",
     ["more money than their population warrants.",
      "less money than their true population warrants.",
      "the same money as districts that were counted accurately.",
      "money that is adjusted for the undercount automatically."],
     "B",
     "Money follows the counted head, and these districts have heads that go uncounted, so the "
     "allocation falls short of the real population. The passage describes no correction step, "
     "which rules out the automatic adjustment."),

 # --------------------------------------------------------------- Boundaries (12)
 bnd("B1",
     "Chinese pharmacists sold &lsquo;dragon bones&rsquo; as a remedy well into the nineteenth "
     "century, and the bones were ground up by the sackful. Scholars eventually recognised the "
     "marks scratched on them as an early form of Chinese _____ the bones turned out to be the "
     "divination records of a dynasty known until then only from much later accounts.",
     ["writing; the bones", "writing, the bones", "writing the bones", "writing: and the bones"],
     "A",
     "Each half of the sentence is a complete statement and no conjunction joins them, so the "
     "semicolon is the only option that works. Joining them with nothing but a comma, as the second "
     "option does, produces a splice."),

 bnd("B2",
     "A reindeer herd moves between coastal summer pasture and inland winter grazing, and the route "
     "matters more than the acreage. Because a fence or a railway line laid across a migration "
     "route puts far more pasture out of reach than it physically _____ herders have opposed "
     "developments that look small on a map.",
     ["occupies, S&aacute;mi", "occupies; S&aacute;mi", "occupies: S&aacute;mi", "occupies and S&aacute;mi"],
     "A",
     "The clause opening with 'Because' is dependent and has to be closed off with a comma before "
     "the main clause begins. Both the semicolon and the colon require a complete sentence in front "
     "of them, and a dependent clause is not one."),

 bnd("B3",
     "A solid lens large enough to throw a beam twenty miles would be too heavy to turn and too "
     "thick to pass light through at all. The board's inventory of the apparatus that replaced it "
     "listed three _____ a drum of ring-shaped lenses, a stack of angled prisms above the drum, and "
     "a clockwork train that turned the whole assembly on a bath of mercury.",
     ["parts: a drum", "parts; a drum", "parts, and a drum", "parts a drum"],
     "A",
     "The words before the blank form a complete sentence announcing three parts, and the colon is "
     "the mark that introduces the list naming them. The semicolon would require a complete "
     "sentence after it, and the list that follows is not one."),

 bnd("B4",
     "Merchants in the Baltic ports had more to fear from pirates and from local rulers than from "
     "one another. The Hanseatic League, an association of trading towns that at its height "
     "stretched from Novgorod to _____ its own warehouses, negotiated its own treaties and on "
     "occasion fought its own wars.",
     ["Bruges, maintained", "Bruges; maintained", "Bruges: maintained", "Bruges maintained"],
     "A",
     "The appositive beginning 'an association of trading towns' was opened with a comma and must "
     "be closed with a matching comma before the verb. Leaving the punctuation out runs the "
     "appositive straight into the predicate."),

 bnd("B5",
     "Timber laid up in layers set at right angles to one another behaves quite unlike a solid "
     "beam, and a panel of it will carry a floor load across a wide span. The material weighs about "
     "a fifth of what an equivalent concrete slab _____ a building framed in it can therefore stand "
     "on much lighter foundations.",
     ["weighs, and", "weighs; and", "weighs: and", "weighs and"],
     "A",
     "Two independent clauses joined by the coordinating conjunction 'and' take a comma in front of "
     "that conjunction. The semicolon and the colon are not used before a coordinating conjunction, "
     "and dropping the comma altogether leaves two full clauses unseparated."),

 bnd("B6",
     "Lava cooling on the seafloor locks in the direction of the magnetic field at the moment it "
     "hardens. Cores drilled on either side of a mid-ocean ridge return matching sequences of "
     "reversed and normal _____ each of which can be tied to the same reversal recorded on the "
     "opposite side.",
     ["layers, each of which", "layers; each of which", "layers: each of which", "layers. Each of which"],
     "A",
     "'each of which' opens a non-essential relative clause, which attaches to the main clause with "
     "a comma. The semicolon and the full stop both need an independent clause after them, and a "
     "relative clause is not independent."),

 bnd("B7",
     "Carbon dioxide seeps into the deep water of some volcanic crater lakes and stays there, held "
     "down by the weight of the water above. If anything disturbs the layering &mdash; a landslide, "
     "a cold night, a heavy _____ the gas can come out of solution all at once and pour downhill as "
     "an invisible flood.",
     ["rain &mdash; the gas", "rain, the gas", "rain; the gas", "rain: the gas"],
     "A",
     "The list of disturbances was set off with a dash, so it has to be closed with a matching "
     "dash before the sentence resumes. Closing it with a comma leaves the opening dash without a "
     "partner and blurs where the interruption ends."),

 bnd("B8",
     "George de Mestral pulled burdock burs out of his dog's coat after a walk and put one of them "
     "under a microscope. Each bur was covered in hooks fine enough to catch on any loop of thread "
     "or _____ the fastener he patented eight years later reproduces those hooks in nylon and "
     "supplies the loops as well.",
     ["hair; the fastener", "hair, the fastener", "hair the fastener", "hair: and the fastener"],
     "A",
     "Both halves are complete sentences with no conjunction between them, so the semicolon is "
     "required. The comma alone would splice them together, and adding 'and' after a colon puts a "
     "conjunction where the mark does not take one."),

 bnd("B9",
     "Cod caught off Newfoundland reached Mediterranean markets in good condition because the fish "
     "were split, salted and dried until they were as stiff as board. The trade needed three things "
     "in _____ boats able to cross the Atlantic, crews willing to spend a season on the Banks, and "
     "salt, which the Basque ports bought from the pans of the Bay of Biscay.",
     ["quantity: boats", "quantity; boats", "quantity, and boats", "quantity boats"],
     "A",
     "What comes before the blank is a complete sentence announcing three things, so the colon "
     "introduces the list that specifies them. The semicolon would demand a full sentence after it "
     "and the list is not one."),

 bnd("B10",
     "Sinan built more than three hundred structures for the Ottoman court and wrote almost nothing "
     "about any of them. Although the dome of the Selimiye mosque at Edirne is wider than the dome "
     "of Hagia _____ the architect mentions the achievement only in passing.",
     ["Sophia, the architect", "Sophia; the architect", "Sophia: the architect", "Sophia and the architect"],
     "A",
     "'Although' opens a dependent clause, and a dependent clause standing in front of the main "
     "clause is separated from it by a comma. The semicolon would require an independent clause on "
     "both sides of it."),

 bnd("B11",
     "Porto Alegre began letting residents vote directly on part of the municipal capital budget in "
     "1989. Neighbourhood assemblies met through the winter to rank their own _____ the delegates "
     "they elected then argued those rankings out against the claims of every other district.",
     ["priorities; the delegates", "priorities, the delegates", "priorities the delegates",
      "priorities: and the delegates"],
     "A",
     "The blank sits between two complete sentences with no conjunction, which is what the "
     "semicolon is for. The comma on its own produces a splice, and no punctuation at all leaves "
     "the two statements running together."),

 bnd("B12",
     "The weaving workshop was the one department at the Bauhaus that women could enter without "
     "argument, and its output paid a good part of the school's bills. Anni Albers, a student there "
     "who went on to run the _____ the loom as an instrument for research rather than as a means of "
     "decorating cloth.",
     ["workshop, treated", "workshop; treated", "workshop: treated", "workshop treated"],
     "A",
     "The appositive describing her began with a comma and must be closed with a comma before the "
     "verb that belongs to the subject. Any of the other marks would break the sentence in a place "
     "where the subject has not yet reached its verb."),

 # ------------------------------------------------ Form, Structure, and Sense (9)
 fss("F1",
     "The ringing station on the headland is staffed from first light for six weeks each autumn, "
     "and the nets are furled the moment the wind gets up. Neither the warden nor the two "
     "volunteers _____ able to account for the sudden run of birds arriving from the east.",
     ["was", "were", "has been", "is"], "B",
     "With 'neither ... nor', the verb agrees with whichever subject stands nearer to it, and 'the "
     "two volunteers' is plural."),

 fss("F2",
     "Glass negatives crack if they are stacked flat, so each one is stored upright in a sleeve of "
     "its own. The town's archive of glass negatives, along with several hundred lantern slides, "
     "_____ moved to a cooler room last spring.",
     ["are", "have been", "were", "was"], "D",
     "The subject is the singular noun 'archive'; the interrupting phrase beginning 'along with' "
     "does not make a singular subject plural."),

 fss("F3",
     "Dredging the harbour mouth was booked for a fortnight and ran into a second month. By the "
     "time the survey boat came back in June, the channel that silted up over the winter _____ to "
     "less than half its charted depth.",
     ["narrows", "had narrowed", "will narrow", "is narrowing"], "B",
     "The narrowing was complete before the boat returned, and the return is itself in the past, so "
     "the past perfect is what places one past event before another."),

 fss("F4",
     "The network reports every fifteen minutes, and a gap of more than an hour brings an engineer "
     "out to the site. Each of the twelve weather stations _____ its own battery and a small solar "
     "panel to keep the battery charged.",
     ["have", "has", "having", "were having"], "B",
     "'Each' is the subject and is singular; the prepositional phrase naming twelve stations does "
     "not change the number of the subject."),

 fss("F5",
     "The tower has been fenced off since a stone fell from the parapet in 1974, and the bells have "
     "hung silent in the frame ever since. The trust's application for the repair grant ran to "
     "ninety pages and was refused twice before it succeeded. The money is to stabilise the roof, "
     "to rehang the bells and _____ the tower to visitors for the first time in half a century.",
     ["opening", "to open", "it opens", "having opened"], "B",
     "The three items joined by 'and' all follow 'is to', and the first two are infinitives, so the "
     "third has to be an infinitive as well. The gerund and the finite clause break the parallel "
     "structure."),

 fss("F6",
     "The ridge is walked at the end of the day, when the light is going and the party is tired, "
     "and a station set over the wrong mark costs a whole morning to put right. Surveying the ridge "
     "in poor light, _____",
     ["the theodolite was set up over the wrong mark.",
      "the wrong mark was used for the theodolite.",
      "the survey party set the theodolite up over the wrong mark.",
      "there was a wrong mark under the theodolite."],
     "C",
     "The opening participial phrase has to describe whoever was doing the surveying, and only the "
     "option that begins with the survey party supplies that subject. Beginning with the theodolite "
     "says the instrument was surveying the ridge."),

 fss("F7",
     "Two kilns fired the same clay on opposite sides of the valley, and their wares are told apart "
     "by the colour of the slip. The iron content measured in the sherds from the eastern kiln is "
     "nearly double _____ measured in the sherds from the western one.",
     ["that", "those", "them", "which"], "A",
     "The pronoun stands in for the singular noun 'content', so the singular form is required; the "
     "plural form would need a plural antecedent and the sentence contains none."),

 fss("F8",
     "The dig runs with three trench supervisors, and each of them keeps a day book of her own. The "
     "site director compares all three _____ notes at the end of every week, and any disagreement "
     "is settled on the ground before a trench is closed.",
     ["supervisors", "supervisor's", "supervisors'", "supervisors's"], "C",
     "The notes belong to all three supervisors, so the noun has to be plural and possessive at "
     "once, which puts the apostrophe after the plural ending. The singular possessive would credit "
     "the notes to one supervisor only."),

 fss("F9",
     "Very little of the marsh survives in a condition anyone would call natural, and most of what "
     "does survive was cut for peat at some point. This fen is one of the few lowland sites in the "
     "county that _____ never been drained for agriculture.",
     ["has", "have", "having", "is"], "B",
     "The relative pronoun 'that' refers back to 'sites', which is plural, so the plural verb is "
     "required; the singular would agree with 'one' instead, which is not what the clause "
     "describes."),

 # -------------------------------------------------------------- Transitions (9)
 trn("T1",
     "A heat pump moves heat rather than making it, and even at freezing temperatures there is "
     "heat outdoors to be moved. _____ the efficiency of the machine falls as the outside air gets "
     "colder, which is exactly when a building needs the most heat.",
     ["However,", "Therefore,", "Likewise,", "For instance,"], "A",
     "The falling efficiency cuts against the advantage just described, so the transition has to "
     "mark a contrast rather than a consequence."),

 trn("T2",
     "Atmospheric weapons testing in the 1950s and early 1960s nearly doubled the amount of "
     "radiocarbon in the air, and the level has been falling along a well-measured curve ever "
     "since. _____ tissue formed in a given year carries a radiocarbon signature that fixes that "
     "year to within about eighteen months.",
     ["Nevertheless,", "As a result,", "By contrast,", "In other words,"], "B",
     "The datable signature follows from the spike and the measured decline described in the first "
     "sentence, which is a cause-and-effect relation. Calling it a restatement would be wrong "
     "because the second sentence introduces a new fact about tissue rather than rephrasing the "
     "first."),

 trn("T3",
     "A data transmission adds check bits that carry no message of their own, and a receiver uses "
     "them to reconstruct a symbol that arrived corrupted. _____ ordinary English carries enough "
     "redundancy that a reader recovers a misprinted word without noticing the misprint.",
     ["Consequently,", "Similarly,", "Nevertheless,", "For example,"], "B",
     "The second sentence offers a parallel case of redundancy repairing damage, so the transition "
     "must signal comparison. Written English is not an instance of a data transmission protocol, "
     "which is what the example transition would claim."),

 trn("T4",
     "Lending books now accounts for a shrinking share of what a public library actually does. Its "
     "buildings are among the few indoor spaces in most towns that anyone may enter and stay in "
     "without paying or explaining why, and city departments with nothing to do with reading have "
     "begun to make use of that. _____ several city systems have designated their branches as "
     "cooling centres, open through the afternoon on any day the temperature passes a set "
     "threshold.",
     ["Nevertheless,", "For example,", "In contrast,", "Consequently,"], "B",
     "The cooling centres are one instance of the non-lending work the first sentence refers to, so "
     "the transition introduces an example. Nothing in the second sentence works against the first, "
     "which rules out the contrastive options."),

 trn("T5",
     "Two atomic clocks of the same design, one at the foot of a tower and one at the top, no "
     "longer agree after a few days: the upper clock has run slightly fast. _____ a clock further "
     "from the mass of the Earth ticks at a faster rate than one closer to it.",
     ["In other words,", "Nevertheless,", "For instance,", "Meanwhile,"], "A",
     "The second sentence states in general terms exactly what the tower experiment showed, which "
     "is a restatement. It is not a further instance, since it introduces no new case."),

 trn("T6",
     "Simulating airflow on a computer costs a fraction of what a session in a wind tunnel costs, "
     "and the models have improved steadily for thirty years. _____ every new airliner wing is "
     "still tested on a physical model, because a simulation is only as good as its assumptions "
     "about turbulence.",
     ["Nonetheless,", "Consequently,", "Likewise,", "In short,"], "A",
     "Physical testing persists in spite of the cheaper and improving alternative, so the "
     "transition has to concede a contrast. Treating it as a consequence would have the cheap "
     "simulations causing the expensive tests."),

 trn("T7",
     "Kente is woven in strips a hand's breadth wide, and the finished cloth is made by sewing the "
     "strips edge to edge so that their patterns line up. _____ the pattern of the whole cloth has "
     "to be worked out before the first strip goes on the loom, since a motif that spans two strips "
     "cannot be corrected afterwards.",
     ["For this reason,", "By contrast,", "Even so,", "Similarly,"], "A",
     "Planning ahead is the consequence of a pattern that only appears once separate strips are "
     "joined, so the transition marks a result. Nothing in the second sentence stands against the "
     "first, which rules out the concessive and contrastive options."),

 trn("T8",
     "Untreated rubber turns sticky in summer heat and stiffens to brittleness in a hard winter, "
     "which is why the first rubber overshoes sold in the 1830s were unusable within a year. _____ "
     "rubber cured with sulphur holds its elasticity across the whole range of temperatures a shoe "
     "is likely to meet.",
     ["By contrast,", "Consequently,", "In addition,", "For example,"], "A",
     "The cured material behaves in the opposite way to the untreated material just described, so "
     "the transition sets the two against each other. Presenting it as a consequence would make the "
     "failure of the overshoes the cause of the cure's performance."),

 trn("T9",
     "The boulder sitting in a Norfolk field is a granite that outcrops nowhere within four hundred "
     "kilometres, and its nearest source lies in southern Norway. _____ the ice that carried it can "
     "be shown to have crossed what is now the North Sea.",
     ["Consequently,", "Nevertheless,", "Similarly,", "In contrast,"], "A",
     "The route of the ice is inferred from the mismatch between where the rock sits and where it "
     "comes from, so the second sentence follows from the first. No contrast is being drawn between "
     "them."),

 # ------------------------------------------------------ Rhetorical Synthesis (9)
 syn("R1",
     ["Nok terracotta heads were made in central Nigeria between about 900 BCE and 200 CE.",
      "Many were found by tin miners washing gravel rather than by archaeologists.",
      "A head washed out of gravel carries no record of the layer it came from.",
      "Radiocarbon dating requires organic material found alongside the object.",
      "Heads excavated in place at Taruga lay in a layer that also contained charcoal."],
     "explain why the Taruga heads can be dated when most Nok heads cannot.",
     ["Nok terracotta heads were made in central Nigeria between about 900 BCE and 200 CE.",
      "Because the Taruga heads were excavated in place, charcoal from the same layer could be used to date them, whereas heads washed out of gravel carry no such context.",
      "Tin miners washing gravel found a great many Nok heads.",
      "Radiocarbon dating requires organic material, and charcoal is organic material."],
     "B",
     "The goal asks for the contrast between the two kinds of find, and only the option that pairs "
     "the in-place excavation with the loss of context in the gravel supplies it. The note about "
     "charcoal being organic states half of the mechanism but never mentions the Taruga heads or "
     "the ones that cannot be dated."),

 syn("R2",
     ["Newton's law gives the force between two masses but not the value of the constant it contains.",
      "In 1798 Henry Cavendish hung two small lead balls from the ends of a rod suspended on a wire.",
      "Bringing two large lead spheres close to the small ones twisted the wire through a measurable angle.",
      "The angle of twist gave the strength of the attraction between the balls.",
      "Once the constant was known, the mass of the Earth could be calculated for the first time."],
     "explain how Cavendish's apparatus made the measurement possible.",
     ["Cavendish measured the tiny attraction between lead balls from the angle through which it twisted a suspended wire.",
      "Newton's law gives the force between two masses but does not supply the constant it contains.",
      "Cavendish carried out his experiment in 1798, more than a century after Newton.",
      "Once the constant had been measured, the mass of the Earth could be calculated."],
     "A",
     "The goal is the workings of the apparatus, and only the option describing the twist of the "
     "wire as the measurement explains how so small a force was detected. The option about the mass "
     "of the Earth reports what the result made possible rather than how it was obtained."),

 syn("R3",
     ["In 1975 fewer than five per cent of M&#257;ori children in New Zealand could speak M&#257;ori.",
      "The first k&#333;hanga reo, or language nest, opened in 1982.",
      "Preschoolers at a nest spend the day with fluent older speakers and hear only M&#257;ori.",
      "By 1993 more than 800 nests were operating.",
      "Children leaving the nests entered primary schools that taught in English."],
     "emphasise a limitation the language nests faced.",
     ["The first language nest opened in 1982, and preschoolers there heard only M&#257;ori all day.",
      "Fewer than five per cent of M&#257;ori children could speak the language in 1975.",
      "Although more than 800 nests were operating by 1993, the children left them for primary schools that taught in English.",
      "More than 800 language nests were operating by 1993."],
     "C",
     "The goal calls for something that worked against the nests, and only the option pairing their "
     "growth with the English-medium schools the children moved on to supplies a limitation. The "
     "option giving the 1975 figure describes the problem the nests were founded to address, not a "
     "constraint on the nests themselves."),

 syn("R4",
     ["The Chartists demanded a vote for every adult man and a secret ballot, among six points in all.",
      "Their third petition was presented to Parliament in 1848.",
      "The petition was said to carry nearly six million signatures.",
      "A parliamentary committee counted fewer than two million and reported forgeries among them.",
      "All but one of the six demands had become law within seventy years."],
     "emphasise the movement's eventual success despite the reception of the 1848 petition.",
     ["The Chartists demanded a vote for every adult man and a secret ballot, among six points in all.",
      "Although a parliamentary committee found the 1848 petition to carry far fewer signatures than had been claimed, all but one of the Chartists' six demands became law within seventy years.",
      "The third Chartist petition was presented to Parliament in 1848 and was said to carry nearly six million signatures.",
      "A parliamentary committee counted fewer than two million signatures and reported forgeries among them."],
     "B",
     "The goal requires both halves &mdash; the discredited petition and the demands that passed "
     "anyway &mdash; and only one option puts them together. The option that stops at the "
     "committee's count gives the setback with none of the success."),

 syn("R5",
     ["Human eyes have three kinds of colour receptor.",
      "A mantis shrimp's eyes have twelve.",
      "Each of its eyes moves independently and judges distance on its own.",
      "Tests show that mantis shrimp discriminate between similar colours less finely than humans do.",
      "Researchers suggest the twelve receptors let the animal recognise a colour at once, without comparing signals."],
     "explain what the shrimp's twelve receptors appear to be for.",
     ["A mantis shrimp has twelve kinds of colour receptor where a human has three.",
      "Each of the shrimp's eyes moves independently and judges distance on its own.",
      "Although a mantis shrimp has twelve kinds of colour receptor to a human's three, it discriminates similar colours less finely; the receptors appear to allow quick recognition rather than fine comparison.",
      "Tests show that mantis shrimp discriminate between similar colours less finely than humans do."],
     "C",
     "The goal asks what the receptors are for, and only the option that carries the finding "
     "through to the researchers' interpretation answers it. Stating the poorer discrimination on "
     "its own leaves the purpose of the twelve receptors unexplained."),

 syn("R6",
     ["At a country fair in 1906 Francis Galton collected 787 written guesses at the weight of an ox.",
      "No individual guess was exactly right.",
      "The middle value of the guesses fell within one pound of the true weight.",
      "Galton had expected the crowd to do badly.",
      "Later work finds the effect holds only when the guesses are made independently of one another."],
     "emphasise the condition on which the effect depends.",
     ["Galton collected 787 guesses at the weight of an ox at a country fair in 1906.",
      "The middle of 787 guesses came within a pound of the ox's true weight, and later work finds that the effect holds only where the guesses are made independently.",
      "Galton had expected the crowd of fairgoers to do badly, and no individual guess was exactly right.",
      "No single guess at the weight of the ox was exactly right, though the middle value was close."],
     "B",
     "The goal names the condition, and only the option that carries the independence requirement "
     "alongside the result meets it. The option contrasting individual guesses with the middle value "
     "reports the finding accurately but says nothing about what the effect requires."),

 syn("R7",
     ["Japanese woodblock printers used a blue made from dayflower petals that faded within a few years.",
      "Prussian blue, a synthetic pigment, reached Japan through Dutch traders in the 1820s.",
      "Prussian blue does not fade and can be printed in graded washes.",
      "Hokusai's wave series of about 1831 uses it throughout.",
      "Prints made from the 1830s onward keep their blues; earlier prints have usually lost theirs."],
     "explain the effect of the new pigment on the prints that survive today.",
     ["Prussian blue reached Japan through Dutch traders in the 1820s and can be printed in graded washes.",
      "Because Prussian blue does not fade as the dayflower blue did, prints made from the 1830s onward keep the blues that earlier prints have lost.",
      "Hokusai's wave series of about 1831 uses Prussian blue throughout.",
      "Japanese printers had used a blue made from dayflower petals, which faded within a few years."],
     "B",
     "The goal is about surviving prints, so the answer has to link the pigment's permanence to what "
     "later prints still look like, which only one option does. The note on the dayflower blue "
     "explains the old problem without saying anything about the prints that came after."),

 syn("R8",
     ["Physarum polycephalum is a single-celled organism that spreads as a network of tubes.",
      "Researchers laid oat flakes on a map of the Tokyo region where the suburban stations lie.",
      "The mould first spread across the whole surface, then thinned its tubes back to the routes carrying the most flow.",
      "The surviving network resembled the Tokyo rail network in total length and in resilience to a severed link.",
      "The organism has no nervous system of any kind."],
     "explain what the experiment demonstrated about the organism.",
     ["Physarum polycephalum is a single-celled organism that spreads as a network of tubes.",
      "Researchers laid oat flakes on a map of the Tokyo region at the positions of the suburban stations.",
      "By thinning its tubes back to the busiest routes, an organism with no nervous system produced a network resembling the Tokyo rail system in length and in resilience.",
      "The surviving network resembled the Tokyo rail network in total length and in resilience to a severed link."],
     "C",
     "The goal asks what the experiment showed about the organism, so the answer needs the "
     "mechanism, the result and the absence of a nervous system together. The option reporting only "
     "the resemblance leaves out what makes it remarkable."),

 syn("R9",
     ["The Landn&aacute;mab&oacute;k lists some four hundred settlers of Iceland and the land each of them claimed.",
      "It was compiled roughly two centuries after the settlement it describes.",
      "Pollen cores show birch woodland disappearing from the lowlands within a century of settlement.",
      "The book says almost nothing about the clearance of woodland.",
      "Archaeologists now use the two kinds of source together, checking one against the other."],
     "emphasise why the written source is not sufficient on its own.",
     ["The Landn&aacute;mab&oacute;k lists some four hundred settlers and the land each of them claimed.",
      "Because the Landn&aacute;mab&oacute;k was compiled two centuries later and says almost nothing about woodland clearance, archaeologists check it against pollen cores showing the lowland birch disappearing within a century of settlement.",
      "Pollen cores show birch woodland disappearing from the Icelandic lowlands within a century of settlement.",
      "Archaeologists use written and environmental sources together, checking one against the other."],
     "B",
     "The goal asks what the book cannot do, so the answer must name its silence on clearance and "
     "the evidence that fills the gap, which only one option does. The option stating the general "
     "practice of combining sources omits the reason the combination is necessary here."),
]

DROPPED = {}
