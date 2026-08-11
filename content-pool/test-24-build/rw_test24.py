#!/usr/bin/env python3
"""
Reading & Writing authored for Test 24.

All 81 items are original. The transcribed pool was spent by Test 8, and for
R&W authoring is in any case the safer route: a transcribed answer key has to
be re-derived by hand before it can be trusted (Test 5 shipped 6 wrong answers
in 81 that way). Every item below carries a `why` that records the reasoning
which produced the key AND the reason the strongest distractor fails — that
record IS the verification, so no key exists here without one.

Rationales name options by their CONTENT, never by letter, so balance_rw.py is
free to rotate every question when it evens out the key distribution. (The
LETTER_REF pattern in that script used to match the ARTICLE "A" starting a
sentence and silently locked questions against rotation; it now requires an
explicit marker or a following verb.)

Writing-domain choices are never bare punctuation. Test 8 shipped Boundaries
items whose four options were ", " / "; " / ": " / " and ", which a student
sees as four empty rows. The real test repeats the words on either side of the
blank inside every option so each choice reads as the resulting sentence, and
every Boundaries item here is written that way from the start.

Topics were screened programmatically against ../rw_authored_corpus.json — the
READ-ONLY 1,295-passage corpus at the content-pool root, covering every
authored and transcribed pool — with a keyword check before drafting, using
check_originality.py in this directory. Test 24's Math territory is the rope
and canvas trades; the R&W territories widen that out while staying clear of
the nine sibling builds:

    ropewalks and cordage, sailmaking lofts and canvas, wire rope and bridge
    cable spinning, netting and mesh in engineering, the mathematics of knots,
    fibre science and tensile strength, bookbinding and sewn structures,
    eyewitness memory, mycorrhizal networks, braille and tactile reading,
    lava flow behaviour, antibiotic resistance, machine translation and corpus
    linguistics, the dating of cave art, hoisting gear and safety brakes.

Candidates that collided with an existing passage were dropped before drafting
rather than paraphrased around: the Inca khipu (already rw_test10/W3), the chip
log and its knotted line (rw_test16/T2), carpet knot counts (rw_test12/W8),
cellulose decay in paper and timber (rw_test16/E4 and I2), spider dragline silk
(rw_test14/T8, rw_test15/R7), lichen symbiosis (twelve corpus passages),
origami folding (fourteen), urban tree canopy (thirteen), hydrothermal vents
(seven), ice cores (six), salt marshes and estuaries (nine), and beaver dams
(twenty-seven).

Block counts (fixed by the assembler's quota, 3 modules x 27):
    Words in Context 15, Text Structure and Purpose 6,
    Central Ideas and Details 6, Command of Evidence 9, Inferences 6,
    Boundaries 12, Form, Structure, and Sense 9, Transitions 9,
    Rhetorical Synthesis 9                                        = 81
"""

SOURCE = "AUTHORED-T24"
MODULE = "RW"

TABLE = ('<table style="border-collapse:collapse;margin:0.75rem 0;">'
         '<tr>{head}</tr>{body}</table>')
TH = ('<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;'
      'text-align:left;background:#F4F6F8;">{}</th>')
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">{}</td>'


def tbl(headers, rows):
    head = "".join(TH.format(h) for h in headers)
    body = "".join("<tr>" + "".join(TD.format(cc) for cc in r) + "</tr>" for r in rows)
    return TABLE.format(head=head, body=body)


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
    bullets = "".join(f"<li>{nn}</li>" for nn in notes)
    return dict(
        num=num, skill="Rhetorical Synthesis",
        passage=f"While researching a topic, a student has taken the following notes:<ul>{bullets}</ul>",
        stem=f"The student wants to {goal} Which choice most effectively uses relevant "
             "information from the notes to accomplish this goal?",
        choices=choices, answer=answer, why=why)


QUESTIONS = [

 # ------------------------------------------------------ Words in Context (15)
 wic("W1",
     "A ropewalk had to be as long as the rope it made, because the yarns were stretched out at "
     "full length before they were twisted together. Some ran to a quarter of a mile under one "
     "roof. The building's shape was therefore not a matter of style but a _____ of the process "
     "carried on inside it.",
     ["consequence", "criticism", "rejection", "decoration"], "A",
     "The sentence contrasts style with something the process itself forced on the building, so "
     "the blank names a result of that process. The 'decoration' option would return the shape to "
     "the realm of style, which the sentence has just ruled out."),

 wic("W2",
     "Sailcloth is graded by the weight of a fixed area of it, and a loft keeps several grades on "
     "hand. A cloth heavy enough to hold its shape in a gale is needlessly stiff in light air, "
     "while a light cloth that draws well in a breeze will stretch out of shape when pressed. "
     "Choosing a grade is thus an exercise in _____ rather than in finding a single best cloth.",
     ["compromise", "duplication", "concealment", "improvisation"], "A",
     "Each grade is described as good in one condition and bad in the other, so the choice trades "
     "one advantage against another. The 'improvisation' option suggests working without a plan, "
     "but the text describes a deliberate selection from known grades."),

 wic("W3",
     "The cables of a suspension bridge are not lowered into place ready made. A wheel runs back "
     "and forth across the span laying single wires, thousands of them, until the bundle is thick "
     "enough; only then is it squeezed round and bound. The finished cable is therefore _____ in "
     "place rather than delivered to it.",
     ["assembled", "inspected", "concealed", "replaced"], "A",
     "The passage describes wires being laid one at a time until a cable exists where none did, "
     "which is building it on site. The 'inspected' option would describe checking a cable that "
     "already existed, which is exactly what the sentence denies."),

 wic("W4",
     "To a mathematician a knot is a closed loop in space, and two knots count as the same if one "
     "can be slid and stretched into the other without cutting the strand. Because such a "
     "deformation can leave a diagram looking utterly unlike the one it started from, telling two "
     "knots apart by eye is _____.",
     ["unreliable", "customary", "inexpensive", "instantaneous"], "A",
     "If sliding and stretching can make the same knot look completely different, appearance is a "
     "poor guide to identity. The 'inexpensive' option speaks to cost, which the sentence never "
     "raises."),

 wic("W5",
     "A single fibre in a rope will break at a load that varies a good deal from fibre to fibre. "
     "The rope as a whole is steadier: when one fibre parts, its share of the load is taken up by "
     "its neighbours, and the rope goes on holding. The bundle's strength is therefore more _____ "
     "than that of any strand within it.",
     ["predictable", "impressive", "expensive", "familiar"], "A",
     "The contrast is between fibre strengths that vary a good deal and a rope that behaves "
     "steadily, so the blank must mean consistent from one specimen to the next. The 'impressive' "
     "option speaks to the size of the strength, not to how much it varies."),

 wic("W6",
     "A book sewn through the folds of its gathered sheets opens flat, because every leaf is held "
     "by thread that runs along the fold rather than by glue applied to a cut edge. Modern paper"
     "back bindings, which saw off the folds and glue the raw edges, gain speed of manufacture but "
     "_____ that behaviour.",
     ["sacrifice", "exaggerate", "recover", "predict"], "A",
     "The sentence sets a gain in speed against something lost, and the flat opening belongs to "
     "the sewn structure that the glued binding cuts away. The 'recover' option would mean the "
     "glued binding restores the very property the sawing destroys."),

 wic("W7",
     "Asked to describe a face they had seen once, witnesses in one study grew markedly more "
     "confident after being told that another witness had picked the same person. Their accounts "
     "did not become more accurate. Confidence and accuracy, the researchers concluded, can move "
     "_____.",
     ["independently", "simultaneously", "backwards", "reluctantly"], "A",
     "Confidence rose while accuracy did not, so the two are shown to vary without reference to "
     "each other. The 'simultaneously' option would mean they rose together, which is the opposite "
     "of what the study found."),

 wic("W8",
     "A seedling growing in deep shade may draw carbon from a mature tree of another species "
     "through the fungal threads that link their roots. The transfer runs from the plant with more "
     "sugar to the plant with less. Whether the mature tree gains anything by it remains _____.",
     ["unsettled", "unpublished", "unpopular", "unavoidable"], "A",
     "The passage reports what is known about the direction of transfer and then marks the "
     "question of benefit as still open. The 'unpublished' option would claim the work has not "
     "appeared in print, which the text does not say."),

 wic("W9",
     "Louis Braille's cells use at most six dots, few enough that a fingertip takes in a whole "
     "character at rest. Earlier raised alphabets copied the shapes of printed letters, which the "
     "finger had to trace curve by curve. Braille's design succeeded because it was _____ to the "
     "sense that would read it rather than to the eye.",
     ["suited", "opposed", "invisible", "indifferent"], "A",
     "The contrast is between a system matched to how a fingertip works and one copied from print, "
     "so the blank names a fit with touch. The 'indifferent' option would say the design took no "
     "account of touch, which is the reverse of the point."),

 wic("W10",
     "Basaltic lava is runny enough to spread in sheets and to travel miles from its vent, while "
     "the stiffer lava of some other volcanoes piles up over the opening it came from. The shape "
     "of a volcano is thus largely _____ by the chemistry of what it erupts.",
     ["determined", "obscured", "reversed", "borrowed"], "A",
     "Two chemistries are shown producing two shapes, so the chemistry fixes the form. The "
     "'obscured' option would mean the chemistry hides the shape rather than setting it."),

 wic("W11",
     "A bacterium that carries a gene for resistance pays for it: making the protein costs energy "
     "that would otherwise go to growth. Where the drug is absent, such bacteria are outbred by "
     "their unburdened neighbours. Resistance is therefore not simply acquired and kept but _____ "
     "by the presence of the drug.",
     ["sustained", "invented", "disguised", "forbidden"], "A",
     "Without the drug the resistant bacteria lose ground, so the drug is what keeps resistance in "
     "the population. The 'invented' option would make the drug create the gene, but the text says "
     "the gene is already carried."),

 wic("W12",
     "Early translation programs worked from rules written out by linguists and failed on any "
     "sentence the rules had not anticipated. Later systems were given millions of sentences "
     "already translated by people and left to find the regularities themselves. The change moved "
     "the labour from stating the language to _____ the examples.",
     ["gathering", "shortening", "disputing", "translating"], "A",
     "The later systems need a large stock of existing translations, so the work becomes one of "
     "collecting them. The 'translating' option would describe producing the examples afresh, "
     "which is the very work the system is meant to take over."),

 wic("W13",
     "Charcoal drawn on a cave wall can be dated directly, because the carbon in it once belonged "
     "to a living tree. A figure drawn in red ochre cannot: the pigment is a mineral, and its age "
     "is the age of the rock, not of the hand that ground it. The two techniques of the same cave "
     "are therefore not equally _____.",
     ["datable", "durable", "visible", "elaborate"], "A",
     "The passage contrasts charcoal, which can be dated, with ochre, which cannot, so the blank "
     "is about yielding a date. The 'durable' option concerns survival, and the text says nothing "
     "about either pigment fading."),

 meaning("M1",
         "Netting is used in engineering wherever a surface must catch something without stopping "
         "the air. A net stretched below a bridge deck slows a falling worker over a long distance "
         "instead of over the inch or two a solid platform would allow. Its mesh <u>yields</u> as "
         "the load comes on, and the force never rises to the value a rigid surface would produce.",
         "yields",
         ["gives way", "surrenders", "produces", "concedes a point"], "A",
         "The mesh is described as slowing a fall over a long distance, so it stretches under the "
         "load. The 'produces' sense of the word is the one used of a crop or a return, which does "
         "not fit a mesh under a falling weight."),

 meaning("M2",
         "A hoist's safety brake does not depend on the driver noticing anything. Weights on the "
         "cage press outward as it descends, and beyond a set speed they swing far enough to bite "
         "into the guide rails. The whole arrangement <u>engages</u> without a signal from anyone "
         "and cannot be talked out of acting.",
         "engages",
         ["takes hold", "occupies", "promises", "attracts"], "A",
         "The weights are described biting into the rails, so the word names the brake gripping. "
         "The 'promises' sense belongs to an engagement between people and has nothing to do with "
         "a mechanism catching."),

 # ------------------------------------------------- Text Structure & Purpose (6)
 tsp("T1",
     "The following text is adapted from a technical history of rope manufacture. "
     "<u>Every twist in a rope is put in against the twist below it.</u> The fibres are spun one "
     "way into yarn, the yarns are turned the other way into strands, and the strands are turned "
     "back again into rope. Each layer, trying to unwind, is held by the layer it is wound "
     "against, and the rope holds itself together without any binding at all.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It states the principle that the rest of the text then works out in detail.",
      "It records an objection that the rest of the text answers.",
      "It gives an example of a practice described later in more general terms.",
      "It draws a conclusion from evidence presented earlier in the text."],
     "A",
     "The underlined sentence announces the alternating-twist rule, and the sentences after it "
     "trace that rule through fibre, yarn, strand and rope. Calling it a conclusion drawn from "
     "earlier evidence misreads its position, since nothing precedes it."),

 tsp("T2",
     "A sail is not a flat sheet. The sailmaker cuts each cloth with a slight curve along the edge "
     "that will be sewn to its neighbour, so that when the panels are joined the finished sail "
     "bellies out into a shape it will hold under wind. The curve is measured in inches over the "
     "length of a seam, and a loft floor is marked out full size so that it can be laid off "
     "exactly.",
     "What is the main purpose of the text?",
     ["To explain how a curved sail is produced from flat pieces of cloth.",
      "To argue that hand cutting produces better sails than machine cutting.",
      "To trace the history of the sailmaking loft as a building.",
      "To compare the shapes of sails used in different kinds of weather."],
     "A",
     "The passage moves from the claim that a sail is not flat to the seam curves and the full-"
     "size floor markings that create the shape, which is a description of a method. Nothing in "
     "the text compares hand work with machine work."),

 tsp("T3",
     "The strength of a rope cannot be found by multiplying the strength of one fibre by the "
     "number of fibres in it. <u>Fibres do not all break at once.</u> The weakest give way first, "
     "and the load they were carrying passes to those still intact, which are then closer to their "
     "own limits. A rope fails in a cascade, and the total it can bear is always less than the sum "
     "of its parts.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It introduces the mechanism that explains the shortfall stated in the first sentence.",
      "It qualifies a claim about fibre strength made later in the text.",
      "It offers a counterexample to the cascade described in the final sentence.",
      "It restates the opening sentence in more technical language."],
     "A",
     "The first sentence says the simple multiplication fails; the underlined sentence supplies "
     "the reason, which the rest of the passage then develops into the cascade. Treating it as a "
     "counterexample to the cascade reverses the relationship, since the cascade follows from it."),

 tsp("T4",
     "Witnesses are often asked how sure they are, and juries treat the answer as a measure of "
     "how reliable the identification is. Research over four decades has found the link between "
     "the two to be strong at the moment of a first, untainted identification and weak afterwards. "
     "What happens in between is feedback: a word of encouragement, a second viewing, a remark "
     "from another witness.",
     "What is the main purpose of the text?",
     ["To identify the conditions under which a witness's confidence does and does not track "
      "accuracy.",
      "To argue that juries should not be told how confident a witness is.",
      "To describe the procedures police use when arranging an identification.",
      "To show that most eyewitness identifications turn out to be mistaken."],
     "A",
     "The passage separates the first untainted identification, where confidence tracks accuracy, "
     "from everything after it, and names feedback as what comes between. It stops short of "
     "recommending what juries should be told."),

 tsp("T5",
     "A translation program trained on parallel texts learns which strings tend to appear opposite "
     "which, without being told what any of them mean. That is enough to render a weather report. "
     "It is not enough for a legal contract, where a term carries a definition fixed elsewhere in "
     "the document and a system with no notion of reference has nothing to hold on to.",
     "What is the main purpose of the text?",
     ["To mark the boundary of what a system trained only on parallel text can do.",
      "To explain how parallel texts are collected and aligned.",
      "To argue that legal documents should be translated only by specialists.",
      "To compare the accuracy of two competing translation systems."],
     "A",
     "The text grants the method a success with weather reports and then names the case it cannot "
     "handle and why, which is a statement of limits. It never describes how the parallel texts "
     "are gathered."),

 tsp("T6",
     "Two figures on the same cave wall need not be the same age. A wall may be painted, left for "
     "a thousand years and painted again, and nothing in the images announces the gap. Dating a "
     "cave therefore means dating each mark that can be dated and admitting that the rest float "
     "free, rather than assigning a single date to the chamber and its contents together.",
     "Which choice best states the main idea of the text?",
     ["A cave's paintings must be dated individually, because a single date for the whole wall "
      "cannot be justified.",
      "Most cave paintings were made within a short period of one another.",
      "Radiocarbon dating is the only method available for cave art.",
      "Caves were repainted so often that their earliest images are lost."],
     "A",
     "The passage argues from the possibility of long gaps between paintings to the practice of "
     "dating each datable mark separately. Saying that most paintings were made close together is "
     "the assumption the text is written against."),

 # ---------------------------------------------- Central Ideas and Details (6)
 cid("C1",
     "A wire rope is stronger than a steel bar of the same weight, but that is not why it is used "
     "on a crane. A bar of the necessary section could not be wound round a drum: bending it once "
     "would leave a permanent set, and bending it repeatedly would crack it. A rope made of many "
     "thin wires bends because each wire moves a little against its neighbours, and it can be "
     "wound and unwound thousands of times.",
     "Which choice best states the main idea of the text?",
     ["Wire rope is used on cranes chiefly because it can be bent repeatedly without damage.",
      "Wire rope is stronger than any solid steel bar of the same dimensions.",
      "Crane drums are designed to reduce the bending a rope must undergo.",
      "Thin wires are easier to manufacture than bars of large section."],
     "A",
     "The passage sets aside strength in its first sentence and spends the rest on the bending "
     "that a bar cannot survive and a rope can. Comparing strength at the same dimensions "
     "misstates the opening, which compares them at the same weight."),

 cid("C2",
     "Knot theorists look for quantities that stay the same however a knot is pushed about. If two "
     "diagrams give different values for such a quantity, they cannot be the same knot. The "
     "reverse does not follow: two diagrams may agree on every quantity yet still be different "
     "knots, and for a long while no known quantity could separate certain pairs.",
     "According to the text, an invariant of the kind described can be used to",
     ["prove that two diagrams represent different knots, but not that they represent the same "
      "knot.",
      "prove that two diagrams represent the same knot, but not that they represent different "
      "knots.",
      "settle either question, provided enough invariants are computed.",
      "settle neither question without an examination of the diagrams by hand."],
     "A",
     "Differing values are said to rule out sameness, while agreement is explicitly said not to "
     "establish it. Reversing the two directions gets the logic exactly backwards."),

 cid("C3",
     "The fungal threads that sheathe a tree's roots take sugar from the tree and pass back "
     "phosphorus drawn from a volume of soil the roots could never reach. Seedlings cut off from "
     "the network in one experiment grew more slowly than seedlings left connected, even where "
     "both had the same light and water. The exchange is not a favour on either side; each partner "
     "is trading a surplus for something scarce.",
     "According to the text, what does the tree gain from the fungus?",
     ["Access to phosphorus from soil beyond the reach of its own roots.",
      "Protection of its roots from drying out in shallow soil.",
      "A supply of sugar that supplements what its leaves produce.",
      "A faster rate of growth in the absence of light."],
     "A",
     "The text says the threads pass back phosphorus drawn from soil the roots cannot reach. The "
     "sugar runs the other way, from tree to fungus, so naming it as the tree's gain reverses the "
     "trade."),

 cid("C4",
     "Braille is read at speed only when whole words are taken in as patterns rather than spelled "
     "out cell by cell, which is why the contracted form, with its signs for common letter groups, "
     "is taught from the start in most schools. The uncontracted form is easier to learn and "
     "slower to read, and a reader who begins with it must later unlearn the habit of tracking "
     "every letter.",
     "Which choice best states the main idea of the text?",
     ["Contracted braille is taught first because the reading speed it allows outweighs its extra "
      "difficulty.",
      "Uncontracted braille is no longer taught in schools.",
      "Braille readers recognise individual cells faster than sighted readers recognise letters.",
      "The contracted form was developed after the uncontracted form had proved too slow."],
     "A",
     "The passage weighs the contracted form's speed against the uncontracted form's ease of "
     "learning and reports that schools choose speed. Saying the uncontracted form is no longer "
     "taught overstates a text that says only that most schools begin with the other."),

 cid("C5",
     "A lava flow does not cool evenly. A crust forms on the surface within minutes and insulates "
     "what is beneath it, so the interior can stay fluid for weeks and go on advancing through "
     "tubes roofed by its own solidified skin. Flows that would have stopped within a few hundred "
     "metres in the open have travelled tens of kilometres in this way.",
     "According to the text, lava tubes allow a flow to travel further because they",
     ["keep the interior of the flow hot enough to remain fluid.",
      "carry the lava downhill more steeply than an open channel would.",
      "reduce the amount of gas escaping from the lava.",
      "spread the flow over a wider area as it advances."],
     "A",
     "The crust is said to insulate the interior so that it stays fluid for weeks, and that is "
     "what lets the flow keep moving. Steeper descent is never mentioned; the tube's contribution "
     "is thermal, not gravitational."),

 cid("C6",
     "A sewn book is built from folded gatherings, and the sewing thread passes through the fold of "
     "each one and round a cord laid across the spine. Because the cords are then laced into the "
     "boards, the covers are attached to the sewing rather than to the paper. A binding of this "
     "kind can be pulled off its boards and re-covered without the leaves being disturbed.",
     "According to the text, what makes it possible to re-cover a sewn book without disturbing the "
     "leaves?",
     ["The covers are held by cords attached to the sewing rather than to the paper itself.",
      "The gatherings are glued to one another along the spine.",
      "The leaves are trimmed after the covers have been fitted.",
      "The thread passes round the outside of each gathering rather than through it."],
     "A",
     "The passage says the cords are laced into the boards and that the covers are therefore "
     "attached to the sewing rather than to the paper. Glue along the spine is the opposite of the "
     "structure described, in which the thread runs through the folds."),

 # -------------------------------------------------- Command of Evidence (9)
 coe("E1",
     "Rope laid up from long fibres and rope laid up from short ones can be spun to the same "
     "diameter and the same weight. Cordage historian Ines Farrow argues that the difference "
     "between them shows itself not in a straight pull but in the way the rope holds a load that "
     "is applied and released over and over.",
     "Which finding, if true, would most directly support Farrow's argument?",
     ["Ropes of the two kinds broke at nearly the same load when pulled steadily to failure, but "
      "the short-fibre ropes lost strength far faster under repeated loading and unloading.",
      "Long-fibre rope was more expensive to produce than short-fibre rope of the same diameter.",
      "Short-fibre ropes absorbed more water than long-fibre ropes of the same weight.",
      "Both kinds of rope were laid up on the same machinery at the same twist."],
     "A",
     "Matching behaviour in a steady pull together with a divergence under repeated loading is "
     "exactly the split the argument predicts, and no other property separates the two ropes in "
     "that way. The difference in cost says nothing about how either rope behaves under load."),

 coe("E2",
     "The panels of a sail are cut so that the threads of the cloth run along the line of greatest "
     "pull. Sail designer Petra Halloran argues that a sail's tendency to lose its shape after a "
     "season depends more on how the panels were laid out than on the grade of cloth used.",
     "Which finding, if true, would most directly support Halloran's argument?",
     ["Sails cut in two different panel layouts from the same bolt of cloth differed markedly in "
      "how much their shape had changed after a season, while sails of different cloth grades cut "
      "in the same layout differed hardly at all.",
      "Heavier cloth grades were found to stretch less than lighter grades under a fixed load.",
      "Sails cut in the more common layout were quicker to make than sails cut in the other.",
      "Sailmakers disagree about which of the two layouts should be used for a given sail."],
     "A",
     "Holding the cloth constant while varying the layout, and then the reverse, isolates layout as "
     "the thing that governs the change in shape. That heavier cloth stretches less under a fixed "
     "load is a property of the cloth and leaves the comparison with layout untouched."),

 coe("E3",
     "Mycorrhizal fungi are often described as passing carbon between trees, but carbon moving out "
     "of one tree and into a fungus need not reach a second tree at all. Ecologist Solveig Naess "
     "argues that most of what leaves a mature tree by this route is consumed by the fungus itself.",
     "Which finding, if true, would most directly support Naess's argument?",
     ["Labelled carbon fed to a mature tree was recovered in large quantities in fungal tissue and "
      "in only trace amounts in the neighbouring seedlings connected to the same network.",
      "Seedlings connected to a network grew faster than seedlings isolated from it.",
      "Fungal networks were found to link trees of several different species in the same stand.",
      "The quantity of carbon leaving a mature tree rose when the tree was shaded."],
     "A",
     "Following a labelled carbon atom and finding it in the fungus but not in the seedlings tests "
     "precisely where the carbon ends up. Faster growth in connected seedlings is consistent with "
     "many causes, including nutrients other than the carbon at issue."),

 coe("E4",
     "A bacterial population exposed to an antibiotic can recover its numbers within days, and it "
     "is usually assumed that the survivors carry a resistance gene. Microbiologist Tomas Elstad "
     "argues that in some populations the survivors are not genetically different at all, but "
     "simply happen to be dormant when the drug arrives.",
     "Which finding, if true, would most directly support Elstad's argument?",
     ["Survivors regrown from a treated culture were no more resistant to a second dose than the "
      "original population had been, and their descendants died at the usual rate.",
      "The treated cultures took several days longer to recover than untreated cultures took to "
      "reach the same density.",
      "Resistance genes were detected in a small fraction of the cells before treatment began.",
      "Higher doses of the antibiotic killed a larger fraction of the population."],
     "A",
     "If the survivors were genetically resistant, their descendants would survive a second dose; "
     "finding them as vulnerable as the original population is what dormancy rather than genetics "
     "predicts. Detecting resistance genes before treatment points the other way, toward the "
     "explanation the argument rejects."),

 coe("E5",
     "Witnesses who pick a face from a lineup are sometimes told afterwards that they chose the "
     "person the police suspected. Psychologist Adaeze Nwora argues that such a remark alters not "
     "only how confident a witness feels but also what the witness later reports about the "
     "original viewing conditions.",
     "Which finding, if true, would most directly support Nwora's argument?",
     ["Witnesses given confirming feedback afterwards recalled having had a longer and clearer "
      "view of the face than witnesses given no feedback, although both groups had viewed it for "
      "the same time.",
      "Witnesses given confirming feedback afterwards reported feeling more certain of their "
      "choice than witnesses given no feedback.",
      "Witnesses viewed the face for a shorter time than they later estimated.",
      "Lineups conducted by an officer who did not know the suspect produced fewer identifications."],
     "A",
     "A changed report of the view itself, with viewing time held constant, is the part of the "
     "claim that goes beyond confidence, and only the recollection of a longer and clearer view "
     "tests it. Greater certainty after feedback supports the confidence half alone, which the "
     "argument treats as already established."),

 coe("E6",
     "Charcoal from a hearth on a cave floor gives a date for the fire, not for the paintings on "
     "the wall above it. Archaeologist Gunnar Liest argues that the hearth dates commonly quoted "
     "for one decorated chamber are too early to belong to the painting of it.",
     "Which finding, if true, would most directly support Liest's argument?",
     ["Pigment scraped from the painted figures themselves yielded dates several thousand years "
      "later than the charcoal from the hearths below them.",
      "The hearths contained burnt bone as well as charcoal.",
      "Several chambers in the same cave contain hearths but no paintings.",
      "The charcoal from the hearths was well enough preserved to give a precise date."],
     "A",
     "Dating the pigment directly and finding it much younger separates the fire from the painting, "
     "which is the whole of the claim. A precise date for the charcoal establishes only that the "
     "fire is well dated, leaving the link to the paintings untested."),

 coe("E7",
     "A hoist's speed governor must trip before a falling cage reaches a dangerous speed, but a "
     "governor set too finely will stop a cage that is merely descending briskly. Two settings "
     "were trialled across a year of ordinary service in a group of buildings, and the results are "
     "summarised below. Engineer Ravi Chaudhuri argues that the coarser setting gives the better "
     "balance of the two demands." +
     tbl(["Governor setting", "Genuine overspeed events caught",
          "Stops on cages descending normally"],
         [["Fine (0.9 m/s above rated)", "12 of 12", "47"],
          ["Coarse (1.4 m/s above rated)", "12 of 12", "3"]]),
     "Which choice most effectively uses data from the table to support Chaudhuri's argument?",
     ["Both settings caught all 12 genuine overspeed events, but the coarse setting stopped only 3 "
      "normally descending cages against the fine setting's 47.",
      "The fine setting stopped 47 normally descending cages, while the coarse setting caught 12 "
      "genuine overspeed events.",
      "The coarse setting trips at 1.4 metres per second above the rated speed, while the fine "
      "setting trips at 0.9.",
      "The fine setting caught 12 of 12 genuine overspeed events, which is as many as the coarse "
      "setting caught."],
     "A",
     "The argument needs both halves of the comparison at once: equal safety performance and far "
     "fewer nuisance stops, which is what the pairing of 12 of 12 with 3 against 47 shows. "
     "Reporting the two settings' trip speeds repeats the labels of the rows without using any of "
     "the results."),

 coe("E8",
     "A rope's residual strength was measured after it had been bent repeatedly round sheaves of "
     "different diameters, expressed as a multiple of the rope's own diameter. Rigging researcher "
     "Marte Vollan argues that sheave diameter matters far more to the life of a rope than the "
     "number of bends it undergoes." +
     tbl(["Sheave diameter", "Strength retained after 10,000 bends",
          "Strength retained after 40,000 bends"],
         [["10 times rope diameter", "58%", "51%"],
          ["20 times rope diameter", "89%", "85%"],
          ["30 times rope diameter", "96%", "94%"]]),
     "Which choice most effectively uses data from the table to support Vollan's argument?",
     ["Quadrupling the number of bends cost each rope at most 7 percentage points of strength, "
      "while going from the largest sheave to the smallest cost 38 points at 10,000 bends.",
      "Ropes bent round the smallest sheave retained 58 percent of their strength after 10,000 "
      "bends and 51 percent after 40,000.",
      "Ropes bent round the largest sheave retained 96 percent of their strength after 10,000 "
      "bends.",
      "Every rope in the trial lost some strength as the number of bends increased."],
     "A",
     "Setting the loss from four times as many bends beside the loss from changing sheave size is "
     "the only comparison that ranks the two factors, which is what the argument asserts. Quoting "
     "the smallest sheave's two figures describes one row and never brings the sheave sizes into "
     "comparison with one another."),

 coe("E9",
     "Readers of contracted braille and readers of the uncontracted form were timed on the same "
     "passages and then tested on what they had understood. Reading specialist Denise Oyelaran "
     "argues that the contracted form's advantage is one of speed alone." +
     tbl(["Group", "Words per minute", "Comprehension score"],
         [["Contracted braille", "118", "82%"],
          ["Uncontracted braille", "74", "81%"]]),
     "Which choice most effectively uses data from the table to support Oyelaran's argument?",
     ["Contracted readers read at 118 words per minute against 74, but scored 82 percent on "
      "comprehension against 81 percent.",
      "Contracted readers read at 118 words per minute, while uncontracted readers read at 74.",
      "Contracted readers scored 82 percent on comprehension, and uncontracted readers scored 81 "
      "percent.",
      "Both groups read the same passages before being tested on what they had understood."],
     "A",
     "Speed alone as the advantage requires the reading rates to differ while the comprehension "
     "scores do not, and only the pairing of both figures shows that. The reading rates on their "
     "own establish the advantage but say nothing about whether it is the only one."),

 # ------------------------------------------------------------- Inferences (6)
 inf("I1",
     "A rope stored in a coil takes a set, and a rope that has taken a set runs badly through a "
     "block. Riggers therefore coil a new rope in the direction of its own lay, so that the bend "
     "the coil puts in agrees with the twist already there. A rope coiled against its lay develops "
     "kinks that no amount of pulling will take out, which means such a rope will _____",
     ["run through a block less easily than one coiled with its lay.",
      "be stronger under a straight pull than one coiled with its lay.",
      "take a set more slowly than a rope stored uncoiled.",
      "regain its original shape once the coil is opened."],
     "A",
     "The passage links a set to poor running through a block and then says coiling against the "
     "lay produces kinks that cannot be pulled out, so the running must suffer. Regaining the "
     "original shape is ruled out by the statement that the kinks are permanent."),

 inf("I2",
     "A knot invariant is only useful if it can actually be computed for a given diagram. One "
     "classical invariant separates every pair of knots yet tabulated, but the work needed to "
     "evaluate it grows so steeply with the number of crossings that diagrams of modest size lie "
     "beyond any machine. For knots drawn with many crossings, then, this invariant is _____",
     ["of little practical help despite its theoretical power.",
      "the only invariant that can be relied upon.",
      "equivalent to counting the crossings in the diagram.",
      "unable to distinguish knots that other invariants can separate."],
     "A",
     "The passage grants the invariant complete success in principle and then says it cannot be "
     "evaluated for larger diagrams, which is a gap between theory and use. Saying it fails to "
     "separate knots contradicts the statement that it separates every pair tabulated."),

 inf("I3",
     "Sailcloth woven from a fibre that creeps under sustained load will slowly lengthen while it "
     "is held taut, and a sail that has lengthened no longer presents the curve it was cut to. "
     "Laminated cloths hold their length because the load is carried by straight fibres bonded "
     "between films rather than by a woven structure that can pull tighter. A sail made from such "
     "a laminate should therefore _____",
     ["hold its designed shape for longer than a woven sail of similar weight.",
      "be lighter than a woven sail of the same area.",
      "prove easier to repair than a woven sail.",
      "stretch further before it reaches its breaking load."],
     "A",
     "Creep is tied to loss of the designed curve, and the laminate is said not to creep, so its "
     "shape should last longer. Weight is never compared, and the passage gives no basis for "
     "ranking the two cloths by it."),

 inf("I4",
     "Translation systems trained on parallel text reproduce the distribution of the text they "
     "were trained on. A corpus assembled from parliamentary proceedings is heavy with formal "
     "argument and light on the language of a kitchen or a playground. A system trained on such a "
     "corpus alone can be expected to _____",
     ["handle formal argument better than everyday conversation.",
      "translate between any two languages with equal facility.",
      "produce shorter sentences than the ones it was trained on.",
      "improve steadily as it is used, without further training."],
     "A",
     "If the system reproduces the distribution of its training text, and that text is rich in "
     "formal argument and poor in everyday speech, its performance should follow the same shape. "
     "Steady improvement through use is not something the passage attributes to these systems."),

 inf("I5",
     "The tube that carries a lava flow is roofed by the flow's own crust, and the roof is thin. "
     "Where a tube runs close beneath the surface, the ground above it stands warmer than the "
     "ground on either side, and the difference persists while lava is still moving inside. A "
     "survey of surface temperatures taken from the air should therefore be able to _____",
     ["trace the path of an active tube without the tube being opened.",
      "measure how much lava a tube is carrying at a given moment.",
      "predict where a new tube will form on a flow.",
      "distinguish lava tubes from tubes that have already drained and cooled only after "
      "excavation."],
     "A",
     "A warm strip over an active tube that persists while lava moves is a signature visible from "
     "above, which is exactly what mapping the path requires. The passage links the warmth to the "
     "presence of moving lava but offers nothing about how much is moving."),

 inf("I6",
     "A resistance gene carried on a plasmid can pass from one bacterium to another, and often "
     "from one species to another, without either cell dividing. A gene carried on the chromosome "
     "spreads only as its owner reproduces. Where a hospital finds the same resistance gene in "
     "several unrelated species at once, the likeliest explanation is that the gene _____",
     ["sits on a plasmid that has moved between them.",
      "arose independently in each species under the same drug pressure.",
      "has been carried on the chromosome of each species for a long time.",
      "confers a larger advantage in some of those species than in others."],
     "A",
     "Only the plasmid is described as crossing between species without reproduction, which is "
     "what appearance in several unrelated species at once requires. Long residence on each "
     "chromosome would predict divergence between the species' copies rather than the same gene."),

 # ------------------------------------------------------------- Boundaries (12)
 bnd("B1",
     "The ropewalk at Chatham is a quarter of a mile long and still in use. The building's single "
     "purpose is written into its _____ nothing else needs a room that shape.",
     ["proportions: nothing", "proportions, nothing", "proportions nothing",
      "proportions, and nothing,"],
     "A",
     "A colon can stand between a complete statement and the explanation that follows it, which is "
     "the relation here. Setting the two off with only a comma joins two complete sentences with "
     "no conjunction."),

 bnd("B2",
     "The sailmaker draws the seam curves full size on the loft floor, then lays the cloth over "
     "the drawing and marks _____ the panels are cut only when every line has been checked.",
     ["them; the", "them, the", "them the", "them: and the"],
     "A",
     "Two complete statements stand on either side of the blank, and a semicolon is the mark that "
     "joins them without a conjunction. A comma alone between them produces a run-on."),

 bnd("B3",
     "Wire for a bridge cable arrives on the site in coils, each _____ galvanised and tested "
     "before it leaves the mill.",
     ["one already", "one, already", "one; already", "one. Already"],
     "A",
     "The phrase beginning with the participle modifies the coils and needs no mark to attach it. "
     "A semicolon would demand a complete statement on its right, and no verb follows."),

 bnd("B4",
     "Because the mesh of a safety net must stretch as the load comes _____ woven from a fibre "
     "that recovers rather than one that simply resists.",
     ["on, it is", "on it is", "on; it is", "on: it is"],
     "A",
     "An introductory clause beginning with a subordinating conjunction is followed by a comma "
     "before the main clause. A semicolon requires a complete statement on each side, and the "
     "opening clause is not one."),

 bnd("B5",
     "Alexander _____ who worked for decades on tabulating knots, arranged them by the smallest "
     "number of crossings in any diagram of them.",
     ["Renshaw, a clergyman", "Renshaw a clergyman", "Renshaw; a clergyman",
      "Renshaw: a clergyman,"],
     "A",
     "The appositive naming his occupation is set off from the name by a comma, matching the comma "
     "that closes it before the verb. Leaving out that comma runs the name and the appositive "
     "together."),

 bnd("B6",
     "The load a fibre bundle can carry depends on how the load is shared out among its _____ and "
     "the sharing depends in turn on how tightly the bundle is twisted.",
     ["members,", "members;", "members", "members:"],
     "A",
     "Two complete statements joined by the conjunction take a comma before it. A semicolon in "
     "front of a conjunction joining two main clauses is not a standard construction."),

 bnd("B7",
     "The binder sews each gathering round three cords, laces the cord ends into the _____ and "
     "covers the whole in leather.",
     ["boards", "boards,", "boards;", "boards:"],
     "A",
     "The sentence lists three actions performed by one subject, and the last two are joined by a "
     "conjunction without a mark. Inserting a comma there would split a compound predicate."),

 bnd("B8",
     "Witnesses are asked to rate their confidence immediately, before anyone has spoken to them "
     "about their _____ later ratings are worth much less.",
     ["choice; the", "choice, the", "choice the", "choice: and the"],
     "A",
     "Both sides of the blank are complete statements, and a semicolon joins them without a "
     "conjunction. A colon followed by a conjunction is not a standard pairing."),

 bnd("B9",
     "The fungal threads that sheathe a root are thinner than the finest root _____ they reach "
     "into pores no root could enter.",
     ["hair, so", "hair so", "hair; so", "hair: so"],
     "A",
     "A comma precedes the coordinating conjunction that joins two complete statements. Omitting "
     "the comma runs them together."),

 bnd("B10",
     "Braille's six-dot cell has sixty-three usable _____ the alphabet, the digits, punctuation "
     "and a stock of contractions all fit inside that number.",
     ["patterns;", "patterns,", "patterns", "patterns: and"],
     "A",
     "Two complete statements stand on either side of the blank and a semicolon joins them without "
     "a conjunction. A comma alone between two main clauses produces a splice."),

 bnd("B11",
     "When a flow's crust thickens enough to bear a person's _____ the lava beneath it may still "
     "be moving at walking pace.",
     ["weight,", "weight", "weight;", "weight:"],
     "A",
     "The sentence opens with a subordinate clause, which is followed by a comma before the main "
     "clause. A semicolon cannot follow a clause that is not itself complete."),

 bnd("B12",
     "A parallel corpus is not simply two texts in two _____ every sentence in one has to be "
     "matched to the sentence that renders it in the other.",
     ["languages:", "languages,", "languages", "languages; and"],
     "A",
     "A colon can introduce the statement that specifies what the first clause has denied. Joining "
     "the two complete statements with only a comma leaves a run-on."),

 # ------------------------------------------------- Form, Structure and Sense (9)
 fss("F1",
     "The yarns that go into a strand of rope _____ spun in the opposite direction to the strand "
     "itself.",
     ["are", "is", "was", "has been"],
     "A",
     "The subject is the plural noun standing before the relative clause, so the verb takes the "
     "plural form. The singular alternatives agree with the nearest noun rather than with the "
     "actual subject."),

 fss("F2",
     "Neither the cloth grade nor the seam curves _____ enough to explain how long a sail keeps "
     "its shape.",
     ["tell us", "tells us", "telling us", "to tell us"],
     "A",
     "With a compound subject joined by the correlative pair, the verb agrees with the nearer "
     "element, which here is plural. The participle and the infinitive leave the sentence without "
     "a main verb."),

 fss("F3",
     "Having laid the wires one at a time across the span, the compacting machine _____ the bundle "
     "into a circular section.",
     ["squeezes", "squeezing", "to squeeze", "having squeezed"],
     "A",
     "The opening participial phrase must be followed by a main clause with a finite verb. Each of "
     "the other forms leaves the sentence with no main verb at all."),

 fss("F4",
     "The two diagrams look nothing alike, but they represent the same knot, and each can be "
     "deformed into _____ without cutting the strand.",
     ["the other", "another", "each other", "the others"],
     "A",
     "With exactly two items in view, the definite form is the one that points to the remaining "
     "member of the pair. The plural form would imply more than two diagrams."),

 fss("F5",
     "A bundle of fibres that shares its load evenly among its members _____ more predictably than "
     "one in which a few fibres carry most of it.",
     ["behaves", "behave", "behaving", "have behaved"],
     "A",
     "The subject is the singular noun at the head of the sentence, not the plural noun inside the "
     "relative clause, so the verb is singular. The plural forms agree with the nearer noun "
     "instead of the true subject."),

 fss("F6",
     "The binder laced the cords into the boards and then _____ the whole in calf.",
     ["covered", "covers", "covering", "has covered"],
     "A",
     "The two verbs joined by the conjunction describe one sequence of actions and must share a "
     "tense, and the first is in the past. The present forms break that agreement."),

 fss("F7",
     "Witnesses who were told that they had picked the suspect later reported that _____ view of "
     "the face had been clearer than it was.",
     ["their", "there", "they're", "its"],
     "A",
     "The blank calls for the possessive pronoun that belongs with the plural subject. The other "
     "spellings are an adverb, a contraction of a pronoun and a verb, and a singular possessive."),

 fss("F8",
     "Because a resistance gene costs energy to maintain, bacteria carrying it grow more slowly "
     "than _____ do in the absence of the drug.",
     ["their neighbours", "them", "theirs", "its neighbours"],
     "A",
     "A comparison of this kind takes a subject on the far side of the conjunction, since a verb "
     "follows the blank. The object pronoun cannot serve as the subject of that verb."),

 fss("F9",
     "The system had been trained on parliamentary proceedings, so its rendering of kitchen talk "
     "_____ nobody by being stilted.",
     ["surprised", "surprise", "surprising", "to surprise"],
     "A",
     "The main clause needs a finite verb in a tense consistent with the past perfect that opens "
     "the sentence. The bare and participial forms leave the clause without a main verb."),

 # ------------------------------------------------------------ Transitions (9)
 trn("N1",
     "A rope's fibres are spun one way and its strands twisted the other, so that each layer holds "
     "the layer inside it. _____ nothing binds a rope together but the tension between its own "
     "parts.",
     ["In effect,", "By contrast,", "For instance,", "Nevertheless,"],
     "A",
     "The second sentence restates the consequence of the first in a more sweeping form, which "
     "calls for a transition marking summary. A contrast marker would suggest the two sentences "
     "disagree, and they do not."),

 trn("N2",
     "Sailcloth is graded by weight, and a heavier grade holds its shape better under load. _____ "
     "a sail cut from the heaviest grade available will not set well in light air.",
     ["However,", "Therefore,", "Similarly,", "In addition,"],
     "A",
     "The second sentence limits what the first appears to recommend, so a contrastive transition "
     "is needed. A consequence marker would suggest the poor performance follows from the "
     "advantage just described."),

 trn("N3",
     "Wire rope is used wherever a load must be lifted round a drum or a sheave rather than "
     "hauled in a straight line. _____ a crane's hoisting gear runs its rope over three sheaves "
     "and on to a drum, bending it four times in every lift.",
     ["For example,", "In contrast,", "As a result,", "Even so,"],
     "A",
     "The second sentence gives a particular case of the general practice stated in the first, so "
     "the transition must introduce an illustration. A consequence marker would make the crane's "
     "arrangement follow from the general statement rather than exemplify it."),

 trn("N4",
     "A knot invariant that agrees on two diagrams leaves open whether the diagrams show the same "
     "knot. _____ an invariant that disagrees settles the question at once: the knots are "
     "different.",
     ["By contrast,", "Likewise,", "Consequently,", "In short,"],
     "A",
     "The sentence sets the case of disagreement against the case of agreement just described, so "
     "the transition must mark opposition. A marker of similarity would claim the two cases behave "
     "alike, and the text says they do not."),

 trn("N5",
     "Fungal threads reach into soil pores far too small for a root. _____ they take up phosphorus "
     "from a volume of ground the tree could never work on its own.",
     ["As a result,", "Even so,", "In contrast,", "Beforehand,"],
     "A",
     "The second sentence states what follows from the fine threads described in the first, so a "
     "consequence marker is called for. A concessive marker would set the two sentences against "
     "each other."),

 trn("N6",
     "Raised alphabets that copied printed letters had to be traced curve by curve. Braille's "
     "cells, _____ can be taken in whole at a single touch.",
     ["on the other hand,", "for instance,", "in addition,", "as a result,"],
     "A",
     "The two systems are set against each other, one traced and the other read at rest, so the "
     "transition marks a contrast. An additive marker would present the second as a further "
     "example of the first."),

 trn("N7",
     "Lava moving inside a tube is shielded from the air and loses heat slowly. _____ the tube "
     "confines the flow to a narrow path instead of letting it spread out and thin.",
     ["In addition,", "By contrast,", "For instance,", "Beforehand,"],
     "A",
     "The second sentence names a further effect of the tube alongside the one already given, so "
     "an additive transition is called for. A contrastive marker would set the narrow path against "
     "the slow heat loss, and the two work together."),

 trn("N8",
     "Maintaining a resistance gene costs a bacterium energy that would otherwise go into growth. "
     "_____ resistant strains lose ground to their neighbours wherever the drug is withdrawn.",
     ["Accordingly,", "Nonetheless,", "Similarly,", "Meanwhile,"],
     "A",
     "The second sentence draws the consequence of the cost stated in the first, which calls for a "
     "result marker. A concessive marker would present the loss of ground as unexpected given the "
     "cost, when it is exactly what the cost predicts."),

 trn("N9",
     "A system trained on parliamentary records handles formal argument well. _____ it stumbles "
     "over the ordinary language of a kitchen, which its training text barely contains.",
     ["Even so,", "For that reason,", "In much the same way,", "To begin with,"],
     "A",
     "The second sentence names a weakness that stands against the strength just reported, so the "
     "transition must be contrastive. A causal marker would make the weakness follow from the "
     "strength."),

 # -------------------------------------------------- Rhetorical Synthesis (9)
 syn("R1",
     ["A ropewalk is a long narrow building in which rope is laid.",
      "The Chatham ropewalk, built in 1729, is 346 metres long.",
      "Its length was set by the length of the cables made in it.",
      "Cables for a first-rate warship were about 200 metres long.",
      "The building is still used to make rope today."],
     "explain to an audience unfamiliar with the trade why the Chatham ropewalk is so long.",
     ["The Chatham ropewalk, built in 1729, is 346 metres long because rope was laid at full "
      "length, and the cables made there ran to about 200 metres.",
      "The Chatham ropewalk, built in 1729, is 346 metres long and is still used to make rope "
      "today.",
      "A ropewalk is a long narrow building, and the one at Chatham was built in 1729.",
      "Cables for a first-rate warship were about 200 metres long, and the Chatham ropewalk is "
      "still in use."],
     "A",
     "The goal is to account for the length, and only the sentence pairing the building's "
     "dimension with the full-length laying of cables of about 200 metres supplies the reason. "
     "Noting that the building is still in use is true but says nothing about why it is long."),

 syn("R2",
     ["Sailcloth is graded by the weight of a fixed area.",
      "A heavier grade holds its shape better under a strong wind.",
      "A heavier grade is stiff and sets poorly in light air.",
      "Lofts keep several grades in stock.",
      "Grade is chosen for the conditions a sail will most often meet."],
     "emphasise that no single grade of sailcloth is best.",
     ["A heavier grade holds its shape better in a strong wind but sets poorly in light air, so "
      "the grade is chosen for the conditions a sail will most often meet.",
      "Sailcloth is graded by the weight of a fixed area, and lofts keep several grades in stock.",
      "A heavier grade of sailcloth holds its shape better under a strong wind than a lighter grade "
      "does.",
      "Lofts keep several grades of sailcloth in stock, and each is graded by the weight of a fixed "
      "area."],
     "A",
     "Showing the same grade winning in one condition and losing in another is what establishes "
     "that none is best overall. Reporting only that a heavy grade holds its shape better makes "
     "the opposite case, naming a single winner."),

 syn("R3",
     ["A bridge cable is spun on site from individual wires.",
      "A wheel carries wires back and forth across the span.",
      "The Brooklyn Bridge's cables each contain 5,434 wires.",
      "The bundle is compacted and wrapped only after spinning.",
      "Spinning a large cable can take several months."],
     "describe the spinning process for an audience unfamiliar with bridge building.",
     ["A bridge cable is spun in place: a wheel carries wires back and forth across the span, and "
      "the bundle is compacted and wrapped only when all of them are laid.",
      "The cables of the Brooklyn Bridge each contain 5,434 wires, and spinning a large cable can "
      "take several months.",
      "Spinning a large cable can take several months, and the bundle is compacted afterwards.",
      "A bridge cable is spun on site rather than delivered ready made to the bridge."],
     "A",
     "Describing the process calls for the sequence of operations, and only the sentence giving the "
     "wheel's traverse followed by compaction and wrapping supplies it. The wire count and the "
     "months taken are facts about scale rather than an account of how the work is done."),

 syn("R4",
     ["A knot invariant assigns a value to a knot diagram.",
      "Deforming the diagram without cutting leaves the value unchanged.",
      "Two diagrams with different values must be different knots.",
      "Two diagrams with the same value may still be different knots.",
      "No invariant known distinguishes every pair of distinct knots."],
     "explain the limits of invariants to an audience unfamiliar with knot theory.",
     ["Differing values prove that two diagrams are different knots, but matching values prove "
      "nothing, and no known invariant separates every pair.",
      "A knot invariant assigns a value to a diagram, and deforming the diagram leaves that value "
      "unchanged.",
      "Two diagrams with different values must be different knots, and deformation never changes a "
      "value.",
      "No invariant known distinguishes every pair of distinct knots, though each assigns a value "
      "to a diagram."],
     "A",
     "The limit is the asymmetry between what differing and matching values prove, together with "
     "the gap no invariant closes, and only one sentence states both. Explaining that deformation "
     "leaves the value unchanged describes how invariants work rather than where they fall short."),

 syn("R5",
     ["Fungal threads sheathe the roots of many forest trees.",
      "The fungus receives sugar made by the tree's leaves.",
      "The tree receives phosphorus the fungus draws from fine soil pores.",
      "Roots cannot enter pores of that size.",
      "Seedlings cut off from the network grew more slowly in one experiment."],
     "explain to an audience unfamiliar with the subject what each partner gains.",
     ["The fungus takes sugar made by the tree's leaves and returns phosphorus drawn from soil "
      "pores too fine for any root to enter.",
      "Fungal threads sheathe the roots of many forest trees, and seedlings cut off from the "
      "network grew more slowly in one experiment.",
      "Roots cannot enter the fine soil pores from which the fungus draws phosphorus.",
      "Seedlings cut off from the fungal network grew more slowly than seedlings left connected to "
      "it."],
     "A",
     "Both sides of the exchange have to appear, and only the sentence naming the sugar going one "
     "way and the phosphorus coming back does that. The seedling experiment shows that the network "
     "matters without saying what either partner receives."),

 syn("R6",
     ["Braille cells contain at most six dots.",
      "A fingertip can take in a whole cell without moving.",
      "Earlier raised alphabets copied the shapes of printed letters.",
      "Those shapes had to be traced curve by curve.",
      "Braille was adopted in most schools by the late nineteenth century."],
     "explain to an audience unfamiliar with the subject why braille replaced earlier raised "
     "alphabets.",
     ["Braille's six-dot cell can be taken in by a fingertip at rest, while the earlier raised "
      "alphabets copied printed letters that had to be traced curve by curve.",
      "Braille cells contain at most six dots, and braille was adopted in most schools by the late "
      "nineteenth century.",
      "Earlier raised alphabets copied the shapes of printed letters used by sighted readers.",
      "Braille was adopted in most schools by the late nineteenth century, and a fingertip can take "
      "in a whole cell without moving."],
     "A",
     "The reason for the replacement is the contrast between reading a cell at rest and tracing a "
     "letter's curves, and only one sentence sets the two side by side. The date of adoption "
     "records the outcome rather than the cause."),

 syn("R7",
     ["A lava flow forms a solid crust within minutes of reaching the surface.",
      "The crust insulates the lava beneath it.",
      "Insulated lava can stay fluid for weeks.",
      "Flows advancing in tubes have travelled tens of kilometres.",
      "Uninsulated flows commonly stop within a few hundred metres."],
     "explain to an audience unfamiliar with volcanology why some flows travel so much further "
     "than others.",
     ["A crust forms within minutes and insulates the lava beneath it, which stays fluid and "
      "advances tens of kilometres where an uninsulated flow stops within a few hundred metres.",
      "A lava flow forms a solid crust within minutes of reaching the surface, and that crust "
      "insulates the lava beneath it.",
      "Flows advancing in tubes have travelled tens of kilometres from the vent that produced them.",
      "Uninsulated flows commonly stop within a few hundred metres of the vent."],
     "A",
     "The question is why the distances differ, so the answer needs the insulation and both "
     "distances in one statement. Giving the tube distance alone leaves the comparison, and "
     "therefore the explanation, unmade."),

 syn("R8",
     ["Making a resistance protein costs a bacterium energy.",
      "Energy spent that way is not available for growth.",
      "Where no drug is present, resistant strains are outgrown by others.",
      "Where the drug is present, only resistant strains survive.",
      "Resistance can decline in a population after a drug is withdrawn."],
     "explain to an audience unfamiliar with the subject why resistance can decline.",
     ["Because making the protein costs energy that would otherwise go into growth, resistant "
      "strains are outgrown by others once the drug is withdrawn.",
      "Where the drug is present, only resistant strains survive, and resistance can decline after "
      "it is withdrawn.",
      "Making a resistance protein costs a bacterium energy that is not then available for growth.",
      "Resistance can decline in a population after a drug is withdrawn from use."],
     "A",
     "The decline needs its cause attached to it, and only the sentence linking the energy cost to "
     "being outgrown after withdrawal supplies one. Restating that resistance can decline names "
     "the phenomenon without explaining it."),

 syn("R9",
     ["Early translation systems worked from rules written by linguists.",
      "Those systems failed on sentences the rules had not anticipated.",
      "Later systems were trained on large collections of existing translations.",
      "Such systems find regularities in the data rather than being told them.",
      "Assembling a large parallel corpus is itself demanding work."],
     "emphasise that the newer approach changed the nature of the work rather than removing it.",
     ["Later systems find regularities in existing translations instead of following rules written "
      "by linguists, but assembling a large parallel corpus is demanding work in its own right.",
      "Early translation systems worked from rules written by linguists and failed on sentences "
      "those rules had not anticipated.",
      "Later systems were trained on large collections of existing translations rather than on "
      "rules.",
      "Assembling a large parallel corpus is itself demanding work for those who undertake it."],
     "A",
     "The point is that effort moved rather than vanished, so both the change of method and the "
     "cost of the corpus must appear. Describing the new training data alone records the change "
     "and drops the half about the work that remains."),
]
