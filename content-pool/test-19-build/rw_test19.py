#!/usr/bin/env python3
"""
Reading & Writing authored for Test 19.

All 81 items are original. The transcribed pool was spent long ago, and for R&W
authoring is in any case the safer route: a transcribed answer key has to be
re-derived by hand before it can be trusted (Test 5 shipped 6 wrong answers in
81 that way). Every item below carries a `why` recording the reasoning that
produced the key AND the reason the strongest distractor fails - that record IS
the verification, so no key exists here without one.

Rationales name options by their CONTENT, never by letter, so balance_rw.py is
free to rotate every question when it evens out the key distribution.

Writing-domain choices are worded, never bare punctuation: every Boundaries
option repeats the words on either side of the blank so that each choice reads
as the resulting sentence. Form/Structure items whose options are genuinely
words ("is" / "are", "has" / "have") are left as words, which is how the real
test presents them.

Command of Evidence mixes three quotation items (E1-E3), three finding-if-true
items (E4-E6) and three data items (E7-E9). The data items carry a real <table>
in the passage using the house style block; none of them describes a graph in
prose, because no image can be produced from here.

Topics were screened against content-pool/rw_authored_corpus.json - all 1,052
passages banked or authored across Tests 1-18 - by keyword (word-boundary, not
substring: an earlier run had "quire" fire on *required*) and by 5-gram /
Jaccard overlap, before anything was drafted. See screen_topics.py in this
directory; `python3 screen_topics.py topics` screens a planned list and
`python3 screen_topics.py passages` re-screens the finished file against the
corpus and against itself.

Test 19 was assigned these territories: peatlands, bogs and wetland
archaeology; tanning, leather and parchment; wind and water mills; charcoal and
woodland crafts; basketry, cordage and fibre crafts; thatch and vernacular
building; lime, mortar and cement; freshwater fish and eel migration; drainage,
pumping and land reclamation; saltmarsh and estuary ecology; Mesoamerican
archaeology; sign systems and writing invention; soil science and microbiology;
migratory shorebirds; the history of standardised measurement.

Candidates dropped at the planning stage because the corpus already covers
them, rather than written and later discovered:

    bog bodies and the acids that tan skin while dissolving bone (rw_test10:T5);
    bog butter and burial in cold, acid, airless ground (rw_test15:W11);
    pollen cores as a dating and land-use record (rw_test10:T8, rw_test11:R9);
    the coppice stool cut back every seven years (rw_test10:I6); turf and sod
    walling (rw_test13:I5, rw_test14:S1); rammed earth built from soil dug
    within sight of the wall (rw_test12:T5); hydraulic lime and the Eddystone
    (rw_test16:W4); slaked lime and the nixtamalisation of maize (rw_test14:W9);
    the European eel's Sargasso life cycle (rw_test12:C5); chinampas at
    Xochimilco (rw_test10:R1); lidar under the Peten canopy (rw_test14:E1);
    horseshoe crabs (rw_test12:W7); clay tokens sealed in envelopes as the
    ancestors of the earliest signs (rw_test10:S6); Linear A and Linear B
    (rw_test10:I5); Sequoyah's syllabary (rw_test12:R4); the kilogram prototype
    and its drift (rw_test14:I1); Asante gold weights (rw_test18:B10); bark that
    can be stripped only while the sap is running (rw_test10:S1, rw_test15:R2);
    riving along the grain rather than sawing across it (rw_test17:W4); bent
    beech chair legs (rw_test14:B8); the Dutch reclamation companies
    (rw_test11:E3); wetland vegetation slowing a flood surge (rw_test9:W13);
    and the Great Zimbabwe walls laid without mortar (rw_test11:W13,
    rw_test12:C3).

Six items were rewritten AFTER drafting, none of them because a number was over
threshold - every one scored below 0.30 Jaccard. They were caught by reading the
nearest match instead of trusting the score, which is the check that matters:

    E2 was a 19th-century engineer's report to a drainage board, with a
    historian claiming its object was to show that more pumping could not help
    while the outfall silted. That is rw_test16:E1 move for move (an engineer's
    report to harbour trustees, the real difficulty being the annual cost of
    keeping the channel open). Rewritten as an excavator's field notebook.
    N1 ran the rw_test11:I4 frame - matter that did not decay, the brake
    removed, the organisms resuming and the carbon leaving. Rewritten onto the
    drying of cut turf.
    N5 ran the rw_test16:R9 frame - gates that can be opened only inside a
    narrow window set by relative water levels, and the consequence for the
    hours available each day. Rewritten onto mole drainage in clay.
    F6 used "A bank of three pumps, together with the sluice, ___", which is
    rw_test12:F2's "The collection of Persian bindings, together with several
    hundred ___" with the nouns changed. Rewritten as a present-perfect item.
    F3 and W7 were two rope-twist passages in this file; F3 moved to the slath
    of a round basket. B4, W10 and B12 each repeated a fact carried by another
    item here (ridge wear, carbonation, and the Exchequer standard object) and
    were moved to the cruck frame, the permeability of limewash and a lowered
    weir.

Block counts (fixed by the assembler's quota, 3 modules x 27):
    Words in Context 15 (three of them the underlined-word-meaning variant),
    Text Structure and Purpose 6, Central Ideas and Details 6,
    Command of Evidence 9, Inferences 6, Boundaries 12,
    Form, Structure, and Sense 9, Transitions 9, Rhetorical Synthesis 9  = 81
"""

SOURCE = "AUTHORED-T19"
MODULE = "RW"

TBL = 'style="border-collapse:collapse;margin:0.75rem 0;"'
TH = ('style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;'
      'text-align:left;background:#F4F6F8;"')
TD = 'style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;"'


def table(headers, rows):
    """The house-style data table used by the Command of Evidence data items."""
    head = "".join(f"<th {TH}>{h}</th>" for h in headers)
    body = "".join(
        "<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"<table {TBL}><tr>{head}</tr>{body}</table>"


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
     "A charcoal burner stacks cordwood into a dome, covers it with earth and dust, and lights it "
     "from a shaft down the middle. Air must reach the wood, or the fire goes out and the stack is "
     "wasted; too much air and the wood burns away to ash instead of charring. The burner opens one "
     "small vent and stops another through the night, so the making of charcoal is less an act of "
     "lighting a fire than a matter of keeping it _____.",
     ["starved", "hidden", "sheltered", "portable"], "A",
     "The passage sets the danger of too much air against the danger of none and describes the "
     "burner rationing air vent by vent, so the fire is kept deliberately short of it. The "
     "'sheltered' option describes protection from the weather, which the earth covering is never "
     "said to provide."),

 wic("W2",
     "A hide is moved through a series of pits, each holding a stronger liquor of crushed oak bark "
     "than the last, and a year may pass before it comes out. A tanner who hurries the sequence "
     "fixes the outer faces of the hide before the liquor has reached the middle, and the leather "
     "cracks along the fold. The slowness of the older pits was therefore _____ rather than a mark "
     "of an industry that had not yet been improved.",
     ["deliberate", "customary", "unrecorded", "seasonal"], "A",
     "The passage explains what goes wrong when the sequence is hurried, which makes the pace a "
     "choice serving a purpose. The 'customary' option says only that the practice was habitual, "
     "which is exactly the reading the sentence sets aside."),

 wic("W3",
     "Parchment is not tanned. The skin is soaked in lime, scraped clear of hair and flesh, and then "
     "laced to a frame and dried under tension while it is pared thinner. The tension pulls the "
     "fibres into layers lying parallel with the surface, and it is that arrangement, not any "
     "coating, that gives the sheet its whiteness and its hard writing surface. Drying under strain "
     "is therefore _____ to parchment rather than a finishing operation applied to it.",
     ["fundamental", "incidental", "detrimental", "preliminary"], "A",
     "The sentence contrasts a final operation with something the material could not exist without, "
     "and the passage credits the fibre arrangement produced by the tension for the sheet's central "
     "properties. The 'preliminary' option makes the stretching a first step among others, which "
     "misses the claim that the stretching is what makes the sheet what it is."),

 wic("W4",
     "A tower mill grinds only while its sails face the wind, and on an exposed site the wind may "
     "back through ninety degrees in an afternoon. Early millers turned the cap by hauling on a tail "
     "pole, which meant leaving the stones and going outside. A small wheel set at right angles "
     "behind the cap, geared down to the curb it sits on, turns the cap whenever the wind strikes it "
     "sideways, so that winding the mill became _____.",
     ["automatic", "communal", "seasonal", "hazardous"], "A",
     "The passage sets the miller's trip outside against a wheel that turns the cap by itself "
     "whenever the wind shifts, so the work stops requiring an operator. The 'hazardous' option "
     "names a risk the passage attaches to nothing, since the tail pole is described as inconvenient "
     "rather than dangerous."),

 wic("W5",
     "The face of a millstone is not flat. Shallow furrows are cut from the centre outward in "
     "groups, and the flat lands between them are pitted with fine tooling. Grain travelling out "
     "between the stones is caught by the edges where furrow meets land and is cut rather than "
     "crushed, and the furrows carry the meal and the air that cools it towards the rim. A stone "
     "left smooth heats the flour and spoils it, so the pattern is strictly _____.",
     ["functional", "traditional", "ornamental", "provisional"], "A",
     "Every feature of the pattern is given a job in the sentences before the blank, and the "
     "consequence of leaving it off is a spoiled product. The 'ornamental' option is the reading the "
     "passage rules out, since nothing about the dressing is described as being for show."),

 wic("W6",
     "Willow rods cut in winter can be used in three states. Rods boiled in their own bark for hours "
     "take up the tannin in it and come out a warm brown; rods stripped after boiling are cream; "
     "rods stripped in spring, when the bark lifts of itself, are white. A basket made from all "
     "three shows bands of colour that no dye has touched, so the pattern is a _____ of how each "
     "bundle of rods was prepared.",
     ["record", "distortion", "forecast", "concealment"], "A",
     "The three colours come from three preparations and nothing else, so the finished bands report "
     "what was done to each bundle. The 'forecast' option points at something still to come, while "
     "the colours date from before the basket was woven."),

 wic("W7",
     "Fibres are twisted one way into yarns, the yarns are twisted the opposite way into strands, "
     "and the strands are twisted back the first way into rope. Each layer is trying to unwind "
     "itself and is prevented by the layer around it, which is winding the other way. Cut the rope "
     "and the end will fray, but along its length the opposed twists hold one another in _____.",
     ["equilibrium", "suspension", "sequence", "reserve"], "A",
     "The passage describes two opposed tendencies that cancel each other out along the rope's "
     "length, which is a balance of forces. The 'sequence' option describes an order in time, and "
     "the twists are acting against each other at the same moment rather than one after another."),

 wic("W8",
     "A thatched roof is not sealed. Water reed is laid in overlapping courses with the cut butts "
     "facing outward, and rain that strikes the surface runs down the outside of the stems and off "
     "the eaves without passing more than a few centimetres into the coat. The pitch matters more "
     "than the depth, because a shallow roof lets the water travel along the stems instead of down "
     "them: the covering works by _____ the rain rather than by blocking it.",
     ["shedding", "absorbing", "storing", "filtering"], "A",
     "The passage says the water runs down the outside and off the eaves without penetrating, which "
     "is a matter of directing it away. The 'absorbing' option describes taking the water in, and "
     "the text states that it barely enters the coat at all."),

 wic("W9",
     "A cob wall is raised from a stiff mixture of subsoil, straw and water thrown up in courses "
     "about half a metre high. Each course must dry and take its own weight before the next can go "
     "on, and the sides are pared back with a spade once they are firm. A wall of any height "
     "therefore takes a season and cannot be hurried, so building in cob is necessarily _____.",
     ["incremental", "collaborative", "improvised", "inexpensive"], "A",
     "The passage describes a wall that goes up one drying course at a time and cannot be pushed "
     "faster, which is growth by stages. The 'inexpensive' option raises cost, and the text mentions "
     "only time and the sequence of courses."),

 wic("W10",
     "Limewash is slaked lime thinned with water and brushed on in coats so thin that the wall shows "
     "through the first of them. It shuts nothing in: damp reaching the face of a limewashed wall "
     "passes out through the coating and dries, so no water is trapped behind a skin. A fresh coat "
     "costs the price of the lime and a morning of somebody's time. Its virtue is not that it lasts "
     "but that it is so easily _____.",
     ["repeated", "tinted", "removed", "imitated"], "A",
     "The passage contrasts durability with the cheap yearly recoating the material invites, so what "
     "is being praised is the ease of putting it on again. The 'removed' option describes taking the "
     "coating off, which the text never treats as an advantage or even mentions."),

 meaning("W11",
         "A lime kiln is loaded from the top in alternating layers: a bed of coal, then broken "
         "limestone, then coal again, until the shaft is full. The burner draws quicklime from the "
         "grate at the bottom as the column settles and adds another <u>charge</u> at the top, so "
         "that the kiln runs for months without being emptied or allowed to cool.",
         "charge",
         ["quantity loaded in", "accusation made", "fee demanded", "duty assigned"], "A",
         "The word names the thing added at the top of a shaft that is drawn off at the bottom, "
         "which is a measured load of fuel and stone. The 'fee demanded' sense is the commercial "
         "one, and nothing in the passage concerns payment."),

 wic("W12",
     "Elvers reaching the foot of a weir will climb anything they can grip, even a wetted wall, but "
     "they cannot cross a smooth vertical face with water sheeting down it. A shallow channel lined "
     "with stiff bristles and fed with a trickle of water gives them purchase for the whole height "
     "of the structure. The fitting costs little and moves nothing, yet it renders a barrier that "
     "had been _____ merely inconvenient.",
     ["impassable", "unlawful", "expensive", "invisible"], "A",
     "The passage says the elvers cannot cross the smooth face at all and then describes a fitting "
     "that lets them up it, so the barrier's former condition was total exclusion. The 'expensive' "
     "option refers to cost, which the sentence attaches to the fitting rather than to the weir."),

 wic("W13",
     "Glasswort grows on the bare mud at the seaward edge of a marsh, where every tide covers it. "
     "Salt entering its tissue is not excluded and not excreted; instead the plant takes up water "
     "until its stems are swollen and almost translucent, and the salt inside is spread through a "
     "far larger volume of sap. The succulence of the plant is therefore a means of _____ rather "
     "than a store laid up against drought.",
     ["dilution", "insulation", "flotation", "concealment"], "A",
     "The passage states that the salt is neither shut out nor thrown off but distributed through a "
     "greater volume of water, which is what the swelling achieves. The 'flotation' option would "
     "explain buoyancy, and the text is concerned with the concentration of salt inside the stems."),

 meaning("W14",
         "A bar-tailed godwit crossing the Pacific completes the journey in one flight, but a knot "
         "travelling the same distance up the Atlantic coast breaks it into three. Each <u>stage</u> "
         "ends at an estuary rich enough to let the bird replace the fat it has burned in a fortnight "
         "of feeding, and the schedule of the whole journey is set by when those few estuaries are "
         "productive.",
         "stage",
         ["leg of a journey", "raised platform", "level of development", "scene of an event"], "A",
         "The word names one of the three parts into which the flight is divided, each ending at a "
         "feeding estuary. The 'level of development' sense fits a process of growth, and what is "
         "being divided here is a distance travelled."),

 meaning("W15",
         "The bronze yard kept at the Exchequer was not a description of a length; it was the "
         "length. Nothing defined it and nothing could correct it, because there was no longer "
         "measure behind it to appeal to. Every yard in the kingdom descended from that one bar, so "
         "a dispute about a yard could in principle be settled by fetching the <u>standard</u> out "
         "and laying the two side by side.",
         "standard",
         ["object others are checked against", "flag carried in procession", "level of quality "
          "expected", "usual way of proceeding"], "A",
         "The passage describes a physical bar that copies are laid against and derived from, so the "
         "word names that object rather than any abstract measure. The 'level of quality expected' "
         "sense is the common modern one and cannot be fetched and compared, which the sentence "
         "requires."),

 # ---------------------------------------------- Text Structure and Purpose (6)
 tsp("T1",
     "A plank walkway laid across a reed swamp about 3800 BCE survives beneath a Somerset peat "
     "field. <u>Its builders drove pairs of pegs into the swamp in a long crossed line, dropped a "
     "rail into the notch where each pair crossed, and pegged the planks down onto the rail.</u> "
     "Nothing in the structure rested on the surface itself. The result carried people in single "
     "file above ground that would not have held a standing adult.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It sets out the arrangement whose purpose the rest of the text explains.",
      "It establishes the date at which the walkway was built.",
      "It accounts for the survival of the timbers in the peat.",
      "It compares the walkway with roads built later in the same region."],
     "A",
     "The underlined sentence describes how the pegs, rail and planks were assembled, and the two "
     "sentences after it state what that assembly achieved: a load carried clear of unbearing "
     "ground. The date appears in the opening sentence rather than in the underlined one."),

 tsp("T2",
     "Stones grind the whole grain at once, so the oil of the germ is smeared through the meal and "
     "the flour turns rancid within weeks. <u>Rollers set in pairs and turned at different speeds "
     "shear each grain open instead of crushing it, so that bran and germ come away in flakes large "
     "enough to be sifted out whole.</u> The flour that resulted was white, kept for months and "
     "could be sent anywhere, and the country mills lost the trade within a generation.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It identifies the change in method that accounts for the qualities described afterwards.",
      "It concedes that stone-ground flour had advantages the new method lacked.",
      "It explains why the germ of the grain contains oil.",
      "It estimates how quickly the country mills lost their trade."],
     "A",
     "The underlined sentence describes the shearing action that separates bran and germ, and the "
     "closing sentence lists the keeping quality and whiteness that follow from that separation. The "
     "loss of trade is stated in the final sentence, not in the underlined one."),

 tsp("T3",
     "River water carrying clay meets salt water part way down an estuary. In fresh water the clay "
     "particles carry like charges and repel one another, so they stay in suspension; in salt water "
     "the charges are neutralised and the particles clump into flocs heavy enough to sink. The mud "
     "therefore drops out along a band that shifts up and down the estuary with the tide and the "
     "river's flow, and the dredgers keep returning to the same few miles of channel year after year.",
     "Which choice best states the main purpose of the text?",
     ["To explain why mud settles along one stretch of an estuary rather than throughout it.",
      "To describe the equipment used to dredge a shipping channel.",
      "To argue that dredging an estuary channel is a waste of money.",
      "To compare the clay carried by two different rivers."],
     "A",
     "The text traces the settling of the mud to a change in the clay's behaviour where fresh water "
     "meets salt, and closes on the narrow band of channel that has to be dredged repeatedly. The "
     "option about dredging equipment picks up a word from the last sentence, which names no "
     "equipment at all."),

 tsp("T4",
     "<u>A Maya vault is built by setting each course of stone a little further out than the course "
     "below until the two sides almost meet, and closing the gap with a capstone.</u> Nothing in the "
     "structure carries a load sideways, so the walls must be thick enough to hold the overhang up "
     "by sheer weight. Rooms roofed in this way are narrow, tall and dark, and widening a room by a "
     "metre costs far more than a metre of extra masonry.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It describes the construction whose consequences the rest of the text traces.",
      "It contrasts the Maya vault with the arch used in other building traditions.",
      "It explains why the capstone is the heaviest element in the roof.",
      "It states how tall the rooms roofed in this way could be made."],
     "A",
     "The underlined sentence sets out the stepped-course method, and everything after it follows "
     "from that method: no sideways thrust, thick walls, narrow rooms, rising cost with width. No "
     "arch of any other tradition is mentioned anywhere in the text."),

 tsp("T5",
     "A stone left lying on old pasture sinks. <u>Worms swallow soil at depth and void it at the "
     "surface as casts, and a stone resting on the turf is undermined grain by grain as those casts "
     "wash down around its edges.</u> Darwin collected and weighed the casts thrown up on measured "
     "plots and calculated that the worms of an acre could raise a fifth of an inch of soil in a "
     "year. The Roman pavements lying a foot below English grass were buried by nobody.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It explains the mechanism behind the sinking asserted in the opening sentence.",
      "It reports the quantity of soil the worms of an acre move in a year.",
      "It questions whether the pavements were buried deliberately.",
      "It describes the method by which the casts were collected and weighed."],
     "A",
     "The opening sentence states that stones sink and the underlined sentence supplies the process "
     "that makes them sink, which the rest of the text then quantifies. The figure for an acre "
     "belongs to the sentence about Darwin's measurements rather than to the underlined one."),

 tsp("T6",
     "Six species of wader feed on one mudflat at the same tide. Their bills run from the "
     "two-centimetre probe of a stint to the twelve-centimetre curve of a curlew, and the animals "
     "buried in the mud are arranged by depth: small snails and thin worms near the surface, thick "
     "worms and burrowing crabs well below. Records of what each species swallows show almost no "
     "overlap at all between the shortest bills and the longest.",
     "Which choice best states the main purpose of the text?",
     ["To explain how species feeding on the same ground take different prey from it.",
      "To argue that curlews drive smaller waders off the flats they share.",
      "To describe how the animals buried in a mudflat construct their burrows.",
      "To establish which of the six species is the most numerous on the flat."],
     "A",
     "The text pairs a range of bill lengths with prey sorted by depth and closes on the absence of "
     "overlap in what the birds eat, which is a division of one feeding ground. The option about "
     "curlews driving other birds away describes a conflict the text never reports."),

 # ------------------------------------------------ Central Ideas and Details (6)
 cid("C1",
     "Rain falling on cool upland with poor drainage keeps the ground saturated, and the moss that "
     "dies beneath the living surface does not rot but accumulates. The peat that builds up holds "
     "many times its own weight in water and releases it slowly, so the waterlogging that began the "
     "process is afterwards maintained by the peat itself. A bog of this kind is not confined to "
     "hollows: it can climb a slope and carry on over the watershed.",
     "Which choice best states the main idea of the text?",
     ["Peat sustains the wet conditions that formed it, which is why such a bog is not restricted to "
      "low ground.",
      "Bogs of this kind form only where standing water collects in hollows.",
      "Moss grows more quickly on a slope than it does on level ground.",
      "Drainage on upland ground improves as the peat above it thickens."],
     "A",
     "The text says the accumulated peat holds the water that keeps the ground saturated and "
     "concludes that such a bog can spread over slopes and watersheds. The option restricting the "
     "bog to hollows states the opposite of the closing sentence."),

 cid("C2",
     "Two constructions account for nearly every basket ever made. In the first, a bundle of grass "
     "or straw is wound in a rising spiral and each turn is stitched to the one below it, so the "
     "wall grows by sewing. In the second, stout rods are set upright as a framework and finer rods "
     "are woven in and out between them, so the wall grows by weaving. The first needs a needle and "
     "almost no strength; the second needs rods that bend without cracking and a maker who can hold "
     "them under strain.",
     "Which choice best states the main idea of the text?",
     ["The two methods build a wall in different ways and therefore ask different things of the "
      "maker's material and tools.",
      "Coiled baskets are stronger than woven ones and last considerably longer.",
      "Both methods were developed in order to make use of grass and straw.",
      "Basketmakers generally learn the woven method before attempting the coiled one."],
     "A",
     "The text describes one wall grown by stitching and another grown by weaving, then pairs each "
     "with what it demands: a needle in one case, pliable rods and strength in the other. The "
     "comparison of strength between the two kinds of basket is never made in the passage."),

 cid("C3",
     "A lime mortar is weaker than the brick or stone it beds, and that is the point of it. As a "
     "wall moves, the fine cracks open along the joints rather than through the units, and a joint "
     "is the one part of a wall a mason can rake out and replace. A cement mortar is much stronger "
     "and much stiffer, and in a wall of soft brick the crack runs through the brick instead. "
     "Repointing an old soft wall in cement can leave it worse than it was.",
     "Which choice best states the main idea of the text?",
     ["Mortar weaker than the masonry sends damage into the joints, where it can be repaired, which "
      "is why cement can harm a soft old wall.",
      "Cement mortar cracks more readily than lime mortar does.",
      "Soft bricks should be replaced with harder ones before a wall is repointed.",
      "The chief advantage of lime mortar is that it costs less than cement."],
     "A",
     "The text explains that the weaker material concentrates cracking in the replaceable joints and "
     "that a stiffer mortar sends the cracking into the brick instead. The option saying cement "
     "cracks more readily reverses the passage, which describes cement as the stronger material and "
     "the brick as the part that fails."),

 cid("C4",
     "A knapper works a lump of obsidian into a fluted cylinder and then presses blades from it one "
     "after another, each running the whole length of the core. Sixty or more usable blades can come "
     "from a core the size of a fist, and every cutting edge is a fracture surface a few molecules "
     "thick. The same edge is brittle: it dulls after a short use, and it cannot be sharpened again, "
     "only struck off and replaced.",
     "Which choice best states the main idea of the text?",
     ["Pressing blades from a prepared core yields many extremely sharp edges from little stone, but "
      "each edge is short-lived.",
      "Obsidian was valued chiefly because its tools could be resharpened many times over.",
      "A core the size of a fist was more than most households could obtain.",
      "The sharpness of an obsidian edge depends on the strength of the knapper."],
     "A",
     "The text pairs the yield and fineness of the edges with the fact that they dull quickly and "
     "cannot be renewed. The option about resharpening contradicts the closing sentence, which says "
     "an edge can only be replaced."),

 cid("C5",
     "The signs of the earliest alphabet are pictures: an ox head, a house, a door. Each sign stands "
     "not for the thing drawn but for the sound that opens the word naming it, so the ox head writes "
     "the first sound of the word for ox. Twenty-odd signs used this way covered a language that "
     "would have needed several hundred to be written word by word, and a list that short could be "
     "learned in days by people who were not scribes by trade.",
     "Which choice best states the main idea of the text?",
     ["Letting each picture stand for the first sound of its own name cut writing down to a couple "
      "of dozen signs.",
      "The pictures were chosen because they were the easiest shapes to draw.",
      "Scribes resisted the new signs because the older system suited them better.",
      "An alphabet of twenty-odd signs cannot represent every sound of a language."],
     "A",
     "The text explains the sound-for-picture principle and then draws the consequence: a couple of "
     "dozen signs in place of several hundred, learnable outside the scribal trade. The option about "
     "ease of drawing offers a reason for the choice of pictures that the passage never gives."),

 cid("C6",
     "An acre began as a day's work rather than a quantity of ground: the strip a man with a yoke of "
     "oxen could plough between morning and evening. Its size therefore moved with the soil, and a "
     "heavy clay acre was a good deal smaller than an acre of light loam. The unit told a farmer the "
     "one thing he needed, which was how long a field would take him. It told a purchaser at a "
     "distance nothing whatever about how much ground he was buying.",
     "Which choice best states the main idea of the text?",
     ["A unit defined by a day's labour reported effort accurately and area only loosely.",
      "Ploughmen working heavy clay were less productive than those working light loam.",
      "The acre was abandoned once oxen were replaced by horses at the plough.",
      "Farmers preferred light loam because it could be ploughed into larger fields."],
     "A",
     "The text derives the acre from a day at the plough, shows its area shifting with the soil, and "
     "then separates what it tells the farmer from what it fails to tell a distant buyer. The option "
     "about productivity treats the varying size as a difference between ploughmen, when the passage "
     "attributes it to the ground."),

 # -------------------------------------------------- Command of Evidence (9)
 coe("E1",
     "In 1846 a surveyor reported to the owners of a tide mill standing at the head of a creek. "
     "Historian Marta Ellery argues that the report was written to show the owners that the mill's "
     "working hours were fixed by the tide and could not be lengthened by any improvement to the "
     "machinery.",
     "Which quotation from the report most effectively illustrates Ellery's claim?",
     ["&ldquo;The wheel turns while the pond empties and no longer, and at the neaps that period is "
      "shorter by an hour whatever gearing be put behind it.&rdquo;",
      "&ldquo;The stones are of French burr and were dressed within the twelvemonth.&rdquo;",
      "&ldquo;A new pair of gates, with the ironwork, would stand the owners in some ninety "
      "pounds.&rdquo;",
      "&ldquo;The corn brought to this mill comes chiefly from farms lying within four miles of "
      "it.&rdquo;"],
     "A",
     "The quotation ties the running time to the emptying of the pond and then states that no change "
     "of gearing alters it, which is exactly the limit the claim says the report was written to "
     "establish. The quotation costing a new pair of gates concerns expenditure and says nothing "
     "about how long the mill can run."),

 coe("E2",
     "Between 1936 and 1939 an amateur excavator kept a notebook while a ditch was deepened along "
     "the edge of a fen, where rows of oak piles kept appearing in the cut. Archaeologist Nils Rask "
     "argues that the notebook shows its author satisfying himself that the piles were the footings "
     "of a built structure some two years before he could persuade anyone else of it.",
     "Which quotation from the notebook most effectively illustrates Rask's claim?",
     ["&ldquo;They stand four abreast and at even spacing, and no flood I can picture would set them "
      "so; I take them for the footings of something raised above the water.&rdquo;",
      "&ldquo;The ditch was opened to a depth of five feet and the spoil laid along the western "
      "bank.&rdquo;",
      "&ldquo;Mr Ridley of the Manor Farm allows that we may work the field until Michaelmas next "
      "year.&rdquo;",
      "&ldquo;Two of the piles were sawn through at the waterline and the sections carried to the "
      "county museum.&rdquo;"],
     "A",
     "The quotation reasons from the regular spacing of the piles to a structure deliberately raised "
     "above the water, which is the conclusion the claim says he had reached early. The quotation "
     "about sawing two piles through records an action taken without saying what the excavator made "
     "of them."),

 coe("E3",
     "The letter book of a Munster tannery covers the years 1783 to 1791, and its entries record "
     "purchases, wages and the state of the pits alongside the partners' correspondence with their "
     "agents in Cork and Bristol. Historian Aoife Larkin argues that what governed the firm's output "
     "in those years was its supply of oak bark rather than its supply of hides.",
     "Which quotation from the letter book most effectively illustrates Larkin's claim?",
     ["&ldquo;Hides we may have out of Cork whenever we send for them; it is the bark that settles "
      "how many pits we dare lay down.&rdquo;",
      "&ldquo;The new pits behind the drying loft were finished at Michaelmas and are of the same "
      "depth as the old.&rdquo;",
      "&ldquo;Sole leather is fetching a better price this season than at any time since the "
      "war.&rdquo;",
      "&ldquo;We have taken on two men for the beam house and shall want a third before "
      "spring.&rdquo;"],
     "A",
     "The quotation sets the ready availability of hides against bark as the thing that decides how "
     "many pits can be worked, which is the comparison the claim rests on. The quotation about the "
     "price of sole leather concerns what the product fetches rather than what limits how much of it "
     "the tannery can make."),

 coe("E4",
     "Salmon hatched in a small tributary return years later to the same tributary, choosing "
     "correctly at every fork on the way up. Biologist Ingrid S&oslash;rensen argues that the fish "
     "make those choices by smell, having learned the odour of their own stream before they went to "
     "sea.",
     "Which finding, if true, would most directly support S&oslash;rensen's argument?",
     ["Adults whose nostrils were plugged turned into the two branches of a confluence at random, "
      "while untagged fish from the same run turned overwhelmingly into their natal branch.",
      "Salmon return to the river in greater numbers in years when the autumn flow is high.",
      "Young salmon spend between one and three years in fresh water before going to sea.",
      "The two branches of the confluence differ in temperature by about one degree in summer."],
     "A",
     "Blocking the sense of smell and finding that the choice at the fork becomes random is what "
     "distinguishes an odour cue from any other, since everything else about the fish is unchanged. "
     "The finding about a one-degree difference in temperature names an alternative cue rather than "
     "supporting the one being argued for."),

 coe("E5",
     "A saltmarsh gains height as each tide leaves a film of sediment on it, and it loses height as "
     "the sea rises against it. Ecologist Tomas Beaudry argues that whether a marsh keeps its "
     "position relative to the tide depends on how much sediment the estuary delivers to it, not on "
     "how vigorously its plants grow.",
     "Which finding, if true, would most directly support Beaudry's argument?",
     ["Marshes on an estuary whose river was dammed in 1960 fell relative to the tide over the next "
      "thirty years, while marshes on a neighbouring undammed estuary rose over the same period.",
      "Marsh plants grow taller on the parts of a marsh that are flooded least often.",
      "The plants of the two estuaries belong to the same species and flower at the same time.",
      "Sediment settles more readily on a marsh surface than on the bare flat in front of it."],
     "A",
     "Damming a river cuts the sediment delivered while leaving the vegetation as it was, so the "
     "divergence between the two estuaries isolates sediment supply as the thing that decides the "
     "outcome. The finding that the plants are the same species removes a difference without showing "
     "which factor drives the change in level."),

 coe("E6",
     "In a few arable fields a root disease that is present in the soil nevertheless fails to damage "
     "the crop, and the fields keep this property for decades. Soil scientist Wren Achebe argues "
     "that the suppression is the work of living organisms in the soil rather than of its chemistry.",
     "Which finding, if true, would most directly support Achebe's argument?",
     ["Heating a suppressive soil destroys the suppression, and mixing one part of untreated soil "
      "into fifty parts of the heated soil restores it.",
      "Suppressive fields hold more organic matter than neighbouring fields that lack the property.",
      "The disease damages crops most severely in warm, wet seasons.",
      "Suppressive soils have been recorded on several continents and in several soil types."],
     "A",
     "Heat destroys organisms but leaves the mineral chemistry, and a small untreated inoculum "
     "restoring the effect is what a living, self-multiplying agent does and a chemical property does "
     "not. The finding about organic matter records a difference between the soils without showing "
     "that anything alive is responsible."),

 coe("E7",
     "Knots feeding on an estuary before their northward flight are caught, weighed and released. A "
     "team recorded the mean mass of the birds caught in the week of their arrival and again in the "
     "week before they left, at four estuaries in the same spring."
     + table(["Estuary", "Mean mass on arrival (g)", "Mean mass before departure (g)"],
             [["Dornoch", "130", "205"], ["Solway", "128", "196"],
              ["Ribble", "126", "171"], ["Wash", "133", "188"]])
     + "The birds gained mass at every estuary in the study, and the largest gain was recorded at "
       "_____",
     "Which choice most effectively uses data from the table to complete the text?",
     ["Dornoch, where a mean of 130 grams on arrival had become 205 grams before departure.",
      "the Wash, where the birds arrived at a mean of 133 grams.",
      "the Ribble, where a mean of 126 grams on arrival had become 171 grams before departure.",
      "the Solway, where the birds weighed a mean of 196 grams before departure."],
     "A",
     "The gain of 75 grams from 130 to 205 is larger than the gains of 68, 55 and 45 grams recorded "
     "at the other three estuaries. The entry reporting 133 grams on arrival gives the heaviest "
     "arrival mass rather than the largest gain, and its gain of 55 grams is among the smaller ones."),

 coe("E8",
     "Water enters a soil no faster than its pores allow, and a soil packed tight by traffic has "
     "fewer pores open to take it. Four fields on the same soil series, differing only in how "
     "heavily they had been worked, were tested for bulk density and for the rate at which water "
     "soaked in. Local rainfall reaches 20 millimetres in an hour in the heaviest summer storms."
     + table(["Field", "Bulk density (g/cm&sup3;)", "Infiltration rate (mm/hour)"],
             [["Barn Close", "1.62", "6"], ["Long Meadow", "1.45", "14"],
              ["Coldharbour", "1.28", "31"], ["Slade", "1.51", "9"]])
     + "Only one of the four fields could take in the heaviest hourly rainfall as fast as it fell, "
       "namely _____",
     "Which choice most effectively uses data from the table to complete the text?",
     ["Coldharbour, whose infiltration rate of 31 millimetres an hour was the only one above 20.",
      "Long Meadow, whose infiltration rate was 14 millimetres an hour.",
      "Slade, whose bulk density of 1.51 grams per cubic centimetre was below that of Barn Close.",
      "Barn Close, whose infiltration rate of 6 millimetres an hour was the lowest measured."],
     "A",
     "Only the field taking 31 millimetres an hour exceeds the 20 millimetres of the heaviest storm; "
     "the other three take 14, 9 and 6. The entry for a bulk density of 1.51 compares two fields for "
     "compaction without addressing whether either could absorb the rain."),

 coe("E9",
     "A commission of 1826 collected the bushel measures actually in use in four market towns, had "
     "each of them filled with water and weighed, and set the result against the Winchester standard "
     "of 35.2 litres."
     + table(["Town", "Capacity of local bushel (litres)"],
             [["Barrowden", "37.7"], ["Chettle", "33.1"], ["Denton", "35.2"], ["Elsdon", "40.0"]])
     + "Three of the four towns were using a measure that differed from the standard, and the "
       "measure furthest from it was the one in use at _____",
     "Which choice most effectively uses data from the table to complete the text?",
     ["Elsdon, whose bushel of 40.0 litres exceeded the standard by 4.8 litres.",
      "Chettle, whose bushel of 33.1 litres fell short of the standard by 2.1 litres.",
      "Barrowden, whose bushel of 37.7 litres exceeded the standard by 2.5 litres.",
      "Denton, whose bushel held exactly 35.2 litres."],
     "A",
     "The difference of 4.8 litres at 40.0 is larger than the differences of 2.5 and 2.1 litres "
     "recorded at the other two towns that departed from the standard. The town whose bushel held "
     "exactly 35.2 litres is the one that matched the standard, so it cannot be the furthest from it."),

 # ---------------------------------------------------------------- Inferences (6)
 inf("I1",
     "When a peat fen is drained the peat dries, shrinks and wastes away as air reaches it. In 1851 "
     "an iron column was driven down through the peat of one such fen until it rested on the clay "
     "beneath, and its top was set flush with the surface of the field. The column has not been "
     "touched since, and its top now stands more than three metres above the ground around it. The "
     "column therefore serves as _____",
     ["a measure of how far the surface of the fen has fallen since the drainage.",
      "evidence that the clay beneath the peat has been pushed slowly upward.",
      "a record of the height reached by the water in the drain beside it.",
      "proof that the wasting of the peat has now come to an end."],
     "A",
     "The column is fixed on the clay and was set level with the ground, so the gap that has opened "
     "between its top and the field can only be ground that has gone. The option about the clay "
     "being pushed upward would require the column to have risen, which the passage rules out by "
     "saying it has not moved."),

 inf("I2",
     "Two marsh plants divide the shore between them. One holds the low marsh, which is covered by "
     "every tide; the other holds the high marsh, which is covered a few times a month. Moved down "
     "into the low marsh, the high-marsh plant dies within a season. Moved up into the high marsh, "
     "the low-marsh plant grows perfectly well so long as its neighbour is cut away, and is crowded "
     "out within two years if it is not. The evidence indicates that _____",
     ["the lower plant is held down by competition and the upper plant by its tolerance of flooding.",
      "each plant grows only where its own tolerance permits, competition playing no part.",
      "the lower plant grows faster than the upper plant wherever the two are found together.",
      "both plants would spread across the whole marsh if the tide were excluded from it."],
     "A",
     "The low-marsh plant thrives high on the shore once its neighbour is removed, so nothing "
     "physical stops it, while the high-marsh plant dies low down whether or not anything else is "
     "present. The option denying competition any part contradicts the two-year result, in which the "
     "transplant is crowded out by a neighbour rather than killed by the tide."),

 inf("I3",
     "Tannin enters a hide slowly, working inward from both faces at once, and a hide lifted too "
     "early looks finished from the outside. A tanner therefore cuts a narrow strip from the edge of "
     "a hide and examines the cut end: where the liquor has done its work the section is brown "
     "throughout, and where it has not an untanned core shows as a pale line down the middle. A pale "
     "line in the sample tells the tanner that _____",
     ["the hide must go back into the pits, since the liquor has not yet reached its centre.",
      "the liquor was too strong and has scorched the outer faces of the hide.",
      "the hide was cut from an animal too young to yield usable leather.",
      "the sample was taken from the wrong part of the hide and must be cut again."],
     "A",
     "The passage states that the pale core is untanned material and that tannin works inward from "
     "both faces, so a pale middle means the process is unfinished rather than spoiled. The option "
     "about scorching would describe damage at the surfaces, and it is the surfaces that the passage "
     "says are already brown."),

 inf("I4",
     "Egyptian inscriptions run left to right in some places and right to left in others, and a "
     "single wall may carry lines of both kinds. The signs themselves settle the question: the human "
     "and animal figures always face towards the start of the line, so a row of owls and seated men "
     "looking leftward is to be read from the left. A reader who has never seen a particular "
     "inscription before can therefore _____",
     ["work out which end of each line to begin at from the direction the figures face.",
      "translate the inscription without knowing anything of the language it records.",
      "date the inscription by the direction in which its lines were cut.",
      "tell which of the figures the inscription was composed to honour."],
     "A",
     "The passage gives one rule, that the figures look towards the beginning, and that rule "
     "supplies exactly one thing: the end at which a line starts. The option about translating "
     "without the language goes far beyond a rule that fixes direction and nothing else."),

 inf("I5",
     "Ammonium carries a positive charge, and the clay and humus of a soil carry negative ones, so "
     "ammonium is held on the surfaces it meets and travels very little. Soil bacteria convert "
     "ammonium into nitrate within days in warm, moist ground, and nitrate carries a negative charge "
     "that nothing in the soil attracts. A field given its nitrogen in autumn rather than in spring "
     "is therefore likely to _____",
     ["lose a larger share of it to the water draining out of the soil over the winter.",
      "retain a larger share of it, because cool soil converts ammonium more quickly.",
      "hold the nitrogen in place until the crop begins to grow in the spring.",
      "need a heavier application of lime before the crop can take the nitrogen up."],
     "A",
     "Nitrogen applied in autumn sits in the soil long enough to be converted, and once it is nitrate "
     "nothing holds it against the winter drainage. The option about cool soil converting ammonium "
     "more quickly reverses the passage, which ties rapid conversion to warm, moist conditions."),

 inf("I6",
     "A tracking device recovered from a bar-tailed godwit recorded a departure from an Alaskan "
     "estuary and a landfall in New Zealand eight days later, with no stop anywhere in between. "
     "Before leaving, the bird had roughly doubled its lean weight in fat, and the organs it uses to "
     "digest food had shrunk to a fraction of their usual size. Taken together, these observations "
     "indicate that the bird _____",
     ["had to carry the whole of its fuel from the start, being in no condition to feed on the way.",
      "fed on small animals taken from the surface of the sea during the crossing.",
      "made the crossing more slowly than a bird that had not laid down fat.",
      "would have been unable to complete the flight without a following wind."],
     "A",
     "A doubled fat load and a digestive system reduced to a fraction of its working size describe a "
     "bird equipped to burn stores and not to process food, over a flight with no landfall. The "
     "option about feeding at sea contradicts the shrunken digestive organs, which are what makes "
     "feeding impossible."),

 # ---------------------------------------------------------------- Boundaries (12)
 bnd("B1",
     "Quicklime drawn from the kiln is not yet mortar. Water poured onto it releases enough heat to "
     "boil the slurry, and the lumps fall apart into a putty that goes on softening for months "
     "afterwards. A mason working to a lime specification plans for the delay and slakes the lime "
     "long before the wall is _____ mixed the same week is gritty, harsh under the trowel and slow "
     "to set.",
     ["begun; mortar", "begun, mortar", "begun mortar", "begun: and mortar"], "A",
     "Two complete statements stand on either side of the blank with no conjunction between them, "
     "which is what the semicolon is for. The comma alone splices them together, and a colon does "
     "not take a conjunction after it."),

 bnd("B2",
     "A patent sail carries rows of hinged shutters linked by a rod that runs the length of the "
     "whip, and a weight hung on the striking rod sets the pressure at which they fly open. The gear "
     "does the one thing no earlier sail could _____ the gusts without the miller stopping the mill, "
     "climbing out and reefing cloth on each of the four sails in turn.",
     ["do: it spills", "do, it spills", "do it spills", "do: and it spills"], "A",
     "What follows the blank explains the claim made before it, and a colon is the mark that "
     "introduces an explanation of that kind. The comma produces a splice between two complete "
     "statements, and a colon is never followed by a coordinating conjunction."),

 bnd("B3",
     "Willow cut in winter is graded before anything is made from it, and a basketmaker will run a "
     "whole bolt through the hand before choosing. The longest _____ are kept back for the uprights, "
     "which have to carry the shape of the basket from the base to the rim without kinking.",
     ["rods, those over five feet, are",
      "rods those over five feet are",
      "rods, those over five feet are",
      "rods those over five feet, are"], "A",
     "The phrase naming the rods over five feet interrupts the sentence and has to be closed off at "
     "both ends, so a comma is needed before it and after it. Each of the other arrangements leaves "
     "one end of the interruption unmarked."),

 bnd("B4",
     "A cruck frame is cut from a single curved tree split down its length, so the two blades of "
     "each pair are mirror images and meet at the ridge without any fitting. The frames were reared "
     "one after another and pegged together along the length of the building _____ walls were built "
     "around them afterwards and carry no part of the roof at all.",
     ["first, and the", "first and the", "first, the", "first and, the"], "A",
     "Two complete statements are joined by a coordinating conjunction, which takes a comma in front "
     "of it. Dropping the comma runs the two statements together, and putting the comma after the "
     "conjunction cuts it off from the clause it introduces."),

 bnd("B5",
     "A tanner judges a pit by smell and by the feel of the hide rather than by any measurement. The "
     "hides that come out of the strongest _____ enough to stand on edge by themselves, and they have "
     "to be worked with oil and a slicker before they will bend around a last.",
     ["liquor are stiff", "liquor, are stiff", "liquor are, stiff", "liquor, are, stiff"], "A",
     "The words naming which hides are meant belong to the subject and must not be cut off from the "
     "verb that follows them. Every other arrangement drops a comma between the subject and its "
     "verb, or between the verb and what completes it."),

 bnd("B6",
     "A sea lamprey passes its first years buried in river silt as a blind, toothless larva, "
     "straining fine particles out of the water above it. Only after it changes _____ does it grow "
     "the sucking disc and the rasping tongue with which the adult feeds on other fish.",
     ["&mdash; a transformation that can take a year &mdash;",
      ", a transformation that can take a year &mdash;",
      "&mdash; a transformation that can take a year,",
      "a transformation that can take a year"], "A",
     "The description of the transformation interrupts the sentence and needs the same mark at both "
     "ends of it. Mixing a comma with a dash marks the two ends differently, and leaving the phrase "
     "unpunctuated runs it into the words on either side."),

 bnd("B7",
     "A drained catchment can be held no lower than the level to which its water can be lifted or "
     "run away. Gravity does the whole of the work wherever the outfall lies below the fields it "
     "serves _____ most of this fen now lies below the river it drains into, and the difference has "
     "to be made up by pumping.",
     ["; however,", ", however,", " however,", ": however"], "A",
     "Two complete statements meet at the blank, and the connecting adverb does not join them, so a "
     "semicolon is needed in front of it. A comma there leaves the two statements spliced, and a "
     "colon would announce an explanation rather than a contrast."),

 bnd("B8",
     "A survey of a saltmarsh follows the creeks before it records anything else, because the creeks "
     "govern the rest. Their branching pattern settles the one question that matters to every plant "
     "growing on the _____ long each patch of ground lies under salt water on each tide.",
     ["marsh: how", "marsh, how", "marsh how", "marsh; how"], "A",
     "What follows the blank is not a complete statement but the content of the question just "
     "mentioned, and a colon is the mark that introduces it. A semicolon requires a complete "
     "statement on both sides, and a comma is too weak to carry the announcement."),

 bnd("B9",
     "Teotihuacan was laid out on a grid before most of the city standing on it existed, and the "
     "grid was held to for centuries afterwards. The _____ along its side streets housed groups far "
     "larger than a single family, each compound with its own courtyard, its own drains and its own "
     "small shrine.",
     ["compounds that stand", "compounds, that stand", "compounds, that stand,", "compounds that, stand"],
     "A",
     "The clause identifies which compounds are meant and therefore belongs to the noun without any "
     "punctuation cutting it away. The versions with commas treat identifying information as though "
     "it could be lifted out, and one of them also separates the subject of the clause from its verb."),

 bnd("B10",
     "A clay tablet from Ugarit, scratched about 1400 BCE, lists thirty signs in a fixed order and "
     "nothing else. The order is not the order of anything in the world, and it is not alphabetical "
     "in any sense the signs themselves could supply. It is nonetheless the order our own alphabet "
     "still runs _____ list of signs was already being recited and learned by heart as a sequence.",
     ["in. The", "in, the", "in the", "in, and, the"], "A",
     "Two complete statements meet at the blank with no conjunction, so the first has to be closed "
     "before the second begins. The comma splices them, running one straight into the other."),

 bnd("B11",
     "Rain moving down through the sandy floor of a conifer wood picks up iron and aluminium from "
     "the top of the profile and drops them again a hand's breadth lower. Because the same water "
     "carries the colour down with _____ podzol shows a bleached grey band lying directly above a "
     "rust-coloured one.",
     ["it, a", "it a", "it; a", "it: a"], "A",
     "The introductory clause beginning with 'because' has to be closed with a comma before the main "
     "statement starts. A semicolon or colon would require a complete statement in front of it, and "
     "the clause is not one."),

 bnd("B12",
     "The weir at the mill stood two metres high and was cut down to a low sill in 2011, the first "
     "of eleven on the river to be lowered. Salmon now pass the site at almost any state of the "
     "flow, and redds have been counted every spring since in the Kirkby reach above it, four miles "
     "of clean _____ which had held no spawning fish since the weir was raised in the 1830s.",
     ["gravel, which", "gravel which", "gravel; which", "gravel: which"], "A",
     "The reach has already been named and measured, so the clause about spawning fish adds "
     "information rather than picking out which gravel is meant, and a comma marks it off. A "
     "semicolon or a colon would need a complete statement after it, and a clause opening with "
     "'which' is not one."),

 # -------------------------------------------------- Form, Structure, and Sense (9)
 fss("F1",
     "The charcoal burner sleeps beside the stack for the whole of the burn, and a stack left "
     "unwatched for two hours can be lost. Each of the vents cut around the base of the clamp _____ "
     "opened and stopped again by hand as the smoke changes colour.",
     ["is", "are", "were", "have been"], "A",
     "The subject is 'each', which is singular, and the words naming the vents sit inside a phrase "
     "that cannot change the number of the subject. The plural forms agree with 'vents' instead, "
     "which is not what the sentence is about."),

 fss("F2",
     "The mill at the bridge had ground on two pairs of stones since 1780, and it had taken the corn "
     "of six parishes. By the time the roller plant opened in the valley in 1889, the trade in "
     "stone-ground flour _____ already begun to fall away.",
     ["had", "has", "have", "having"], "A",
     "The falling away happens before the roller plant opens, and both events lie in the past, so "
     "the earlier one takes the past perfect. The present perfect would place the decline in a "
     "period reaching up to now, which the dates rule out."),

 fss("F3",
     "A round basket starts from a slath: short rods split down the middle, threaded through one "
     "another at right angles and then opened out like the spokes of a wheel. Longer rods are worked "
     "in around them until the base is closed. Bent up out of the finished base and held under "
     "strain until the first rows of weaving lock them in position, _____",
     ["the stakes take the shape that the whole basket will keep.",
      "the shape that the whole basket will keep is taken by the stakes.",
      "there is a shape taken by the stakes that the whole basket keeps.",
      "taking the shape the whole basket keeps is what the stakes do."],
     "A",
     "The opening phrase describes whatever has been bent up and held under strain, and only the "
     "stakes can be, so the stakes have to be the subject of the clause that follows. Each of the "
     "other versions puts the shape, or the taking of it, in that position, and neither can be bent "
     "up out of a basket base."),

 fss("F4",
     "The parish had specified a lime mortar for the repair of the church, on the advice of an "
     "architect who had seen what cement does to soft stone. The masons brought in for the work had "
     "all been trained on cement and had never mixed lime in their lives. _____ first batch set so "
     "slowly that the scaffold had to stand for a month while it hardened.",
     ["The masons'", "The mason's", "The masons", "The masons's"], "A",
     "The batch belongs to more than one mason, so the plural noun takes an apostrophe after the "
     "final letter. The singular possessive would point at one worker, and the passage has named "
     "several."),

 fss("F5",
     "Eleven weirs stand between the tide and the headwaters of this river, and each of them now "
     "carries a bristle-lined channel up which the young eels can climb. Every pass is inspected in "
     "April, before the elvers arrive in numbers. The bristles are lifted out and washed, and any "
     "pass whose channel has silted up has _____ trickle of water restored before the run begins.",
     ["its", "it's", "their", "they're"], "A",
     "The pronoun stands for a single pass and shows possession, which is the form without an "
     "apostrophe. The contracted form means 'it is', and the plural would disagree with the singular "
     "'any pass'."),

 fss("F6",
     "The last of the windpumps on this level was taken down in 1938 and sold for its timber, and "
     "the land it once drained lies well below the river that carries the water away. Ever since "
     "that winter the district _____ dry by three diesel pumps and a tidal sluice at the outfall.",
     ["has been kept", "is kept", "was kept", "had been kept"], "A",
     "The stretch of time runs from a point in the past up to the present, which is what the present "
     "perfect marks. The simple past would close the period off in 1938, and the past perfect would "
     "put the pumping before some other past event that the sentence never supplies."),

 fss("F7",
     "The pyramid was enlarged five times, each new shell built over the last, and the tunnels "
     "driven into the mound in the 1930s found the earlier stairways still standing inside it. The "
     "two archaeologists who worked on the tunnels disagreed for years about the date of the "
     "earliest of them. The report that finally settled the sequence was written jointly by the "
     "field director and _____.",
     ["her", "she", "hers", "herself"], "A",
     "The pronoun is one of two objects of the preposition 'by', so it takes the object form. The "
     "subject form would be required only if the pronoun were doing the writing rather than being "
     "named after 'by'."),

 fss("F8",
     "The commission wrote to every market town in the kingdom, asked what measures were in daily "
     "use there, and printed the returns without amending them. Some towns sent in three or four "
     "measures for different commodities. The number of distinct local bushels reported to it in "
     "1826 _____ greater than the number of counties that answered at all.",
     ["was", "were", "have been", "are"], "A",
     "The subject is 'the number', which is singular however many things are being counted. The "
     "plural verbs agree with 'bushels', a noun that sits inside a phrase modifying the subject."),

 fss("F9",
     "A wader that has just crossed an ocean cannot be followed to its feeding grounds, but it can "
     "be weighed. The team works the high-tide roost with mist nets, takes each bird's mass to the "
     "gram and lets it go within the hour, and the same flock is caught again eleven days later. "
     "Caught at the roost and weighed before release, _____",
     ["the birds had gained a third of their arrival mass in eleven days.",
      "eleven days had been enough for a gain of a third of their arrival mass.",
      "it was found that a third of their arrival mass had been gained in eleven days.",
      "a gain of a third of their arrival mass had taken eleven days."],
     "A",
     "The opening phrase describes whatever was caught and weighed, and only birds can be, so the "
     "birds must be the subject of the clause that follows. Each of the other versions puts a period "
     "of time or a gain in that position, neither of which can be trapped at a roost."),

 # --------------------------------------------------------------- Transitions (9)
 trn("N1",
     "Peat lifted from the bank is two-thirds water by weight, and a wet turf will not take a flame "
     "at all. The cutter stacks the turves in open lattices with the wind blowing through them, "
     "turns the stack twice before autumn and carts it home only when it rings under the hand. "
     "_____ a fuel that costs nothing to buy costs a summer of work before it will burn.",
     ["Therefore,", "However,", "Similarly,", "For instance,"], "A",
     "The summer of stacking and turning described in the second sentence is what produces the cost "
     "in labour stated in the third, so the transition marks a consequence. A contrast would require "
     "the last sentence to cut against the drying work, and it follows from it instead."),

 trn("N2",
     "Sole leather is tanned slowly and left thick and firm, so that it wears down under the foot "
     "instead of stretching out of shape. _____ the leather of an upper is curried with oils and "
     "tallow until it is soft enough to fold around the foot at every step.",
     ["By contrast,", "Accordingly,", "In addition,", "In other words,"], "A",
     "The two sentences set two leathers against each other, one made firm and the other made "
     "supple, so the transition marks the opposition. A consequence relation would require the "
     "second leather to follow from the first, and it does not."),

 trn("N3",
     "A stack of green wood loses well over half its weight when it is charred, and what remains "
     "burns hotter than the wood it came from. _____ charcoal was made in the wood where the timber "
     "grew and carried out on horseback, rather than the timber being carted whole to the town.",
     ["Consequently,", "Nevertheless,", "For example,", "Meanwhile,"], "A",
     "The weight lost in charring is the reason for burning the wood where it stood and moving only "
     "the product, so the second sentence states a consequence of the first. A contrast would "
     "require the second sentence to cut against the first, which it does not."),

 trn("N4",
     "Water reed cut in winter stands almost upright in a roof and can last sixty years before it is "
     "stripped. Long straw is softer, lies flatter and is generally renewed after twenty-five. _____ "
     "a straw roof is cheaper to lay and can be patched in a morning where a gale has lifted it.",
     ["Even so,", "Therefore,", "Similarly,", "In particular,"], "A",
     "The final sentence gives straw an advantage that stands against the shorter life just reported "
     "for it, so the transition concedes rather than concludes. A consequence relation would make "
     "cheap patching follow from the shorter life, which it does not."),

 trn("N5",
     "Water travels through a heavy clay only as fast as the cracks and worm channels in it allow, "
     "and a pipe drain laid in such a soil can run dry while the field a metre above it stands "
     "waterlogged. Drainers pull a bullet-shaped mole through the clay at half the depth of the "
     "pipe, splitting the ground into fissures that lead down to it. _____ the water reaches the "
     "pipe by a route the soil could not have provided for itself.",
     ["As a result,", "Nonetheless,", "By comparison,", "For instance,"], "A",
     "The fissures split into the clay are what carry the water down to a pipe it could not "
     "otherwise reach, so the last sentence states the outcome of the operation described before it. "
     "A concession would require that sentence to work against the moling, and it reports its "
     "effect."),

 trn("N6",
     "The sacbeob are raised limestone roads, plastered white and in places ten metres across, and "
     "some run twenty miles from one centre to another. They were built in a country that had no "
     "wheeled vehicles and no pack animals, so everything moving along them moved on somebody's "
     "back. _____ they were made wide, level and hard enough to carry traffic of a kind that did not "
     "exist.",
     ["Nevertheless,", "Consequently,", "Likewise,", "That is,"], "A",
     "The width and hard surface stand against the absence of carts and animals that the sentence "
     "before has just established, so the transition marks that tension. A consequence relation would "
     "have the absence of vehicles producing the wide road, which reverses the sense."),

 trn("N7",
     "The earliest Greek inscriptions run from right to left, the direction of the Phoenician script "
     "they were adapted from. Others run in alternating directions, turning at the end of each line "
     "the way a plough turns at the end of a furrow. _____ the left-to-right arrangement that became "
     "standard was for well over a century only one option among several.",
     ["In short,", "By contrast,", "For example,", "Nevertheless,"], "A",
     "The final sentence gathers the varied directions just listed into a single statement about "
     "them, which is a summary rather than a new case. A contrast would set the last sentence against "
     "the examples, and it instead sums them up."),

 trn("N8",
     "Soil organisms respond both to temperature and to how much water fills the pores between the "
     "grains, and neither factor on its own predicts what a soil will do. _____ a warm soil that is "
     "saturated gives off less carbon dioxide than a cool one that is merely damp, because the "
     "organisms in the wet soil are short of oxygen.",
     ["For example,", "However,", "As a result,", "In conclusion,"], "A",
     "The second sentence supplies a particular case illustrating the general claim that one factor "
     "alone predicts nothing. A contrast would set the case against the claim, but the case is an "
     "instance of it."),

 trn("N9",
     "A knot feeding on a mudflat swallows small shellfish whole and grinds them in a muscular "
     "gizzard that grows heavier the harder the shells it works on. That same organ shrinks to a "
     "fraction of its weight in the days before a long flight, and it takes several days to rebuild "
     "afterwards. _____ the first food a bird takes at the far end of its journey tends to be "
     "soft-bodied worms rather than shellfish.",
     ["Accordingly,", "Even so,", "By contrast,", "Specifically,"], "A",
     "A gizzard that has shrunk and has not yet been rebuilt cannot grind shells, so the choice of "
     "soft prey on arrival follows from what the previous sentence describes. A concession would "
     "require the last sentence to work against that, and it agrees with it."),

 # ------------------------------------------------------- Rhetorical Synthesis (9)
 syn("R1",
     ["Peat forms only while the ground stays waterlogged, and it wastes away once air reaches it.",
      "A drained peat field loses several millimetres of its surface every year.",
      "Blocking the ditches on a drained bog raises the water table back to within a few "
      "centimetres of the surface.",
      "Sphagnum moss returns to the wetted surface within a few seasons.",
      "Gas measurements on rewetted bogs record far less carbon dioxide leaving the ground than "
      "before the ditches were blocked."],
     "explain how blocking the ditches changes what a drained bog does.",
     ["Peat forms only while the ground stays waterlogged.",
      "Sphagnum moss returns to a rewetted surface within a few seasons.",
      "Blocking the ditches raises the water table to within a few centimetres of the surface, and "
      "gas measurements then record far less carbon dioxide leaving the ground.",
      "A drained peat field loses several millimetres of its surface every year."],
     "C",
     "The goal asks what the blocking changes, and only the choice joining the raised water table to "
     "the fall in carbon dioxide leaving the ground states the change. The return of the moss "
     "reports a further effect without connecting it to what the ditch blocking did."),

 syn("R2",
     ["Tanning binds tannin into the fibres of a hide, and a tanned hide never returns to its raw "
      "state.",
      "Parchment is made by liming a skin, scraping it and drying it under tension; no tannin is "
      "used at all.",
      "Parchment that is wetted relaxes, shrinks and cockles as it dries again.",
      "A tanned hide that is wetted dries flat and unchanged.",
      "Parchment and leather are both made from animal skin."],
     "explain why parchment is not a kind of leather.",
     ["Parchment and leather are both made from animal skin.",
      "Parchment is dried under tension without tannin, so wetting relaxes and cockles it, whereas a "
      "tanned hide dries flat and unchanged.",
      "Parchment is made by liming a skin and then scraping it.",
      "A tanned hide never returns to its raw state once the tannin is in the fibres."],
     "B",
     "The goal asks for the distinction, and only the choice contrasting the tension-dried, "
     "tannin-free sheet with the tanned hide's behaviour when wetted supplies one. Noting that both "
     "are made from skin gives what the two have in common, which is the opposite of what the goal "
     "asks for."),

 syn("R3",
     ["An undershot wheel is turned by water striking the paddles at the bottom of the wheel.",
      "An overshot wheel is turned by the weight of water carried down in buckets from the top.",
      "An overshot wheel needs a head of water at least as high as the wheel itself.",
      "Building a leat along the contour can carry water from far upstream to the top of a wheel.",
      "For the same flow, an overshot wheel yields roughly twice the power of an undershot one."],
     "explain why a millwright would go to the expense of digging a leat.",
     ["An undershot wheel is turned by water striking its paddles at the bottom.",
      "A leat carried along the contour delivers water at the height an overshot wheel needs, and "
      "such a wheel yields about twice the power of an undershot one on the same flow.",
      "An overshot wheel is turned by the weight of water carried down in buckets.",
      "Building a leat along the contour can carry water from far upstream."],
     "B",
     "The goal asks what justifies the cost of the channel, and only the choice linking the head the "
     "leat provides to the doubled power gives a reason. Stating that a leat can carry water from "
     "upstream describes what it does without saying what is gained by it."),

 syn("R4",
     ["A pollard is a tree cut back to a permanent trunk two or three metres above the ground.",
      "The height of the cut puts the regrowth out of reach of cattle and deer.",
      "Wood pasture carries grazing animals and a wood crop on the same ground.",
      "A tree that is cut in this way regularly can go on producing for several centuries.",
      "The cut poles were used for fuel, fencing and tool handles."],
     "explain how one piece of ground could yield two things at once.",
     ["A pollard is a tree cut back to a permanent trunk above the ground.",
      "The cut poles were used for fuel, fencing and tool handles.",
      "Cutting above the height cattle and deer can reach keeps the regrowth safe from them, so the "
      "same ground carries grazing animals and a wood crop together.",
      "A tree cut in this way regularly can go on producing for several centuries."],
     "C",
     "The goal asks how one acre produced both, and only the choice tying the height of the cut to "
     "the protection of the regrowth explains how the grazing and the wood crop coexist. The note "
     "about several centuries of production reports longevity, which is a separate benefit."),

 syn("R5",
     ["The ridge of a thatched roof takes more weather than the slopes below it.",
      "A ridge is renewed every ten to fifteen years.",
      "A full re-coat of the slopes is needed only every twenty-five to sixty years, depending on "
      "the material.",
      "Re-ridging requires a few days of work and one bundle of sedge in ten of the coat.",
      "The ridge is fixed with hazel spars and can be stripped without disturbing the coat beneath "
      "it."],
     "explain why the ridge is dealt with separately from the rest of the roof.",
     ["The ridge of a thatched roof takes more weather than the slopes below it.",
      "A ridge is renewed every ten to fifteen years.",
      "Because the ridge wears out several times over during the life of the coat and can be "
      "stripped without disturbing it, it is renewed on its own in a few days.",
      "Re-ridging requires one bundle of sedge in every ten of the coat."],
     "C",
     "The goal asks why the ridge is treated on its own, and only the choice pairing its faster wear "
     "with the fact that it comes off without touching the coat gives the reason. The interval of "
     "ten to fifteen years states how often the work is done without saying why it is done "
     "separately."),

 syn("R6",
     ["Limestone is burned in a kiln, which drives carbon dioxide out of it and leaves quicklime.",
      "Water added to quicklime slakes it into a putty.",
      "Mortar made from the putty sets by taking carbon dioxide back out of the air.",
      "The set material is calcium carbonate, the substance the limestone was made of.",
      "A lime mortar goes on hardening for years as the change works inward from the surface."],
     "explain why lime mortar is described as returning to the rock it came from.",
     ["Limestone is burned in a kiln, which drives carbon dioxide out of it.",
      "Burning drives carbon dioxide out of the limestone and the set takes it back from the air, "
      "leaving the mortar as the same carbonate the stone was.",
      "A lime mortar goes on hardening for years after it is laid.",
      "Water added to quicklime slakes it into a putty."],
     "B",
     "The goal asks for the sense in which the material comes full circle, and only the choice "
     "pairing the carbon dioxide driven off in the kiln with the same gas taken back during the set "
     "completes the circle. The note about years of hardening describes the rate of the change rather "
     "than what the change produces."),

 syn("R7",
     ["Maya monuments carry dates counted in days from a fixed starting point in 3114 BCE.",
      "The count runs continuously and does not restart with a new ruler.",
      "Neighbouring cultures dated events by the reign in which they fell.",
      "A Long Count date can be placed to the individual day.",
      "Fixing the whole count against the European calendar took scholars several decades."],
     "explain why Maya dates can be placed more precisely than those of neighbouring cultures.",
     ["Fixing the count against the European calendar took scholars several decades.",
      "Maya monuments carry dates counted in days from a fixed starting point.",
      "Because the Maya count runs in days from one fixed point and does not restart with each "
      "ruler, a date can be placed to the day, while neighbouring cultures dated events by reign.",
      "Neighbouring cultures dated events by the reign in which they fell."],
     "C",
     "The goal asks for a comparison, and only the choice setting a continuous count in days against "
     "dating by reign explains the difference in precision. The decades spent on the correlation "
     "concern modern scholarship rather than the precision of the original dates."),

 syn("R8",
     ["Local measures varied from town to town across the kingdom.",
      "From 1497 bronze standards were sent out to the market towns from the Exchequer.",
      "Market officers compared the traders' measures against the town's bronze standard.",
      "A measure that matched was stamped, and an unstamped measure could be seized.",
      "The bronze standards were themselves copied from a single set kept in London."],
     "explain how a single standard was made to reach an individual trader's measure.",
     ["Local measures varied from town to town across the kingdom.",
      "The bronze standards were copied from a single set kept in London.",
      "Copies of one London set were sent to the market towns, where officers compared each trader's "
      "measure against them and stamped the ones that matched.",
      "From 1497 bronze standards were sent out to the market towns."],
     "C",
     "The goal asks how the chain ran from the one original down to a trader's vessel, and only the "
     "choice following the copies out to the towns and then to the stamping of individual measures "
     "traces it. Stating that the standards were copied from a London set covers only the first link."),

 syn("R9",
     ["A sea wall built across an estuary in 1850 cut off two hundred hectares of grazing from the "
      "tide.",
      "The marsh in front of the wall narrowed as the sea rose against it.",
      "A new wall was built inland in 2002 and the old one was breached.",
      "Glasswort colonised the bare mud behind the breach within two seasons.",
      "Counts of feeding waders on the site rose sharply in the years after the breach."],
     "explain how breaching the old wall changed the life of the site.",
     ["A sea wall built across the estuary in 1850 cut off two hundred hectares from the tide.",
      "Letting the tide back through the breach allowed glasswort to colonise the bare mud within "
      "two seasons, and counts of feeding waders on the site rose sharply afterwards.",
      "A new wall was built further inland in 2002.",
      "The marsh in front of the old wall narrowed as the sea rose against it."],
     "B",
     "The goal asks what the breach did to the living community, and only the choice pairing the "
     "colonising plants with the rise in feeding waders reports it. Building the new wall inland "
     "describes the engineering step without any consequence for what lives there."),
]

DROPPED = {}
