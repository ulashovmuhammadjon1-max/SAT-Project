#!/usr/bin/env python3
"""
Reading & Writing authored for Test 29.

All 81 items are original. The transcribed pool was spent by Test 8, and for
R&W authoring is in any case the safer route: a transcribed key has to be
re-derived by hand before it can be trusted (Test 5 shipped 6 wrong answers in
81 that way). Every item carries a `why` that records the reasoning which
produced the key AND the reason the strongest distractor fails; that record is
the verification, so no key exists here without one.

Rationales name options by their CONTENT, never by letter, so balance_rw.py is
free to rotate every question when it evens out the key distribution.

Writing-domain choices are never bare punctuation. Test 8 shipped Boundaries
items whose four options were ", " / "; " / ": " / " and ", which a student
sees as four empty rows. The real test repeats the words on either side of the
blank inside every option so each choice reads as the resulting sentence.

TOPICS. Test 29's territory is the building trades that begin after the stone
leaves the ground: brickworks and kilns, tile making, plasterwork and lath,
stonemasonry and tracery, scaffolding and hoists. Test 23's lesson is written
into the topic list: a narrow territory collides with ITSELF long before it
collides with the bank, so the list is sized to the ITEM count (81 distinct
sub-topics), not to the block count, and no Rhetorical Synthesis note list
shares a sub-topic with any passage. Where two items are unavoidably near
neighbours they were pushed apart in wording and then checked by
screen_topics.py, which scores every passage against the 1,295-passage corpus
in ../rw_authored_corpus.json AND against every other passage in this file.

Neighbouring builds own ground this file therefore stays off: Test 18 has
quarrying (no stone is extracted here) and Test 19 has lime burning (nothing
here burns or slakes lime, and the lime-versus-cement mortar argument belongs
to rw_test19:F4/C3). Test 16 owns pottery kilns, saggars, glaze faults and
plaster slip-casting moulds; Test 14 and Test 15 own mosaic tesserae. See
DROPPED at the foot of this file.

Block counts (fixed by the assembler's quota, 3 modules x 27):
    Words in Context 12, Text Structure and Purpose 6,
    Cross-Text Connections 3, Central Ideas and Details 6,
    Command of Evidence 9, Inferences 6,
    Boundaries 12, Form, Structure, and Sense 9, Transitions 9,
    Rhetorical Synthesis 9                                        = 81
"""

SOURCE = "AUTHORED-T29"
MODULE = "RW"

TH = ('<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;'
      'background:#F4F6F8;">{}</th>')
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">{}</td>'


def table(headers, rows):
    head = "<tr>" + "".join(TH.format(h) for h in headers) + "</tr>"
    body = "".join("<tr>" + "".join(TD.format(c) for c in r) + "</tr>" for r in rows)
    return ('<table style="border-collapse:collapse;margin:0.75rem 0;">'
            + head + body + "</table>")


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


def ctc(num, text1, text2, stem, choices, answer, why):
    """Cross-Text Connections: BOTH texts live in one passage field."""
    passage = ("<p><strong>Text 1</strong></p><p>" + text1 + "</p>"
               "<p><strong>Text 2</strong></p><p>" + text2 + "</p>")
    return dict(num=num, skill="Cross-Text Connections", passage=passage,
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


def syn_given(num, sentences, goal, choices, answer, why):
    """The second real shape of a Rhetorical Synthesis item.

    A pipeline that knows only the notes template misfiles this one; that bug
    was live in Test 1. Three of the nine items here use it.
    """
    bullets = "".join(f"<li>{s}</li>" for s in sentences)
    return dict(
        num=num, skill="Rhetorical Synthesis",
        passage=f"While working on an assignment, a student has written the following sentences:<ul>{bullets}</ul>",
        stem=f"The student wants to {goal} Which choice most effectively uses relevant "
             "information from the given sentences to accomplish this goal?",
        choices=choices, answer=answer, why=why)


QUESTIONS = [

 # ------------------------------------------------------ Words in Context (12)
 wic("W1",
     "Clay dug in the autumn was not used at once. It was spread in a heap a spade deep and left "
     "through the winter, where water taken into the fine cracks froze and split the lumps apart "
     "night after night. By spring the heap could be turned with a fork instead of broken with a "
     "hammer. The season of exposure did work the yard would otherwise have paid men to do, so the "
     "frost served the brickmaker as a _____.",
     ["rival", "labourer", "customer", "witness"], "B",
     "The sentence says the frost did work the yard would otherwise have paid men for, so the "
     "blank has to name a worker. Calling the frost a rival would set it against the brickmaker, "
     "and the passage has it doing the yard's own work."),

 wic("W2",
     "Clay taken straight from the heap is a mixture rather than a material: stiff lumps, soft "
     "lumps, grit and pockets of air lie side by side in it. The pug mill drives the whole mass "
     "through a barrel fitted with knives, and what comes out at the far end is the same clay "
     "throughout, with nothing left in it that would tear a moulded shape as it dried. The mill's "
     "purpose is not to soften the clay but to make it _____.",
     ["uniform", "abundant", "watertight", "colourful"], "A",
     "What comes out is described as the same clay throughout, which is a matter of consistency "
     "from one part to the next. The option about softening is the very purpose the last sentence "
     "sets aside."),

 wic("W3",
     "A machine that squeezes a column of clay through a die and cuts it with a wire will turn out "
     "in an hour what a moulder turns out in a day, and every brick it makes is the same size to "
     "within a hair. Builders who wanted the soft, sanded face of a moulded brick complained that "
     "the wire-cut article looked as though it had been sliced from a loaf, and for the fronts of "
     "houses they went on paying for the slower work. The machine's regularity was, to that trade, "
     "less a merit than a _____.",
     ["bargain", "liability", "necessity", "mystery"], "B",
     "The buyers of fronts objected to the sliced look and paid more to avoid it, so the evenness "
     "counted against the machine brick with them. Calling it a bargain would reverse the "
     "complaint the sentence has just reported."),

 meaning("W4",
         "Green bricks leave the moulder soft enough to take a thumbprint, and they cannot go into "
         "the fire until the water has left them. They are set out in long open stacks called "
         "hacks, laid on edge with a finger's gap between them so that air passes on every side, "
         "and a light roof of straw or boards is drawn over the top against rain and hard sun. A "
         "shower on unprotected bricks will <u>raise</u> the faces and lose the whole row.",
         "raise",
         ["lift up", "cultivate", "damage", "collect"], "C",
         "The sentence ends with the whole row being lost, so what the shower does to the faces "
         "must be harm. The everyday sense of lifting something up does not fit a face of a brick "
         "that is being ruined by rain."),

 wic("W5",
     "In an ordinary kiln the fire is lit, the ware is burned, the whole chamber is allowed to "
     "cool, and only then is it emptied and refilled. A continuous kiln is built instead as a ring "
     "of chambers, and the fire is walked round it from one to the next: the chamber behind the "
     "fire is cooling, the chamber ahead of it is being warmed by the gases drawn through, and men "
     "are emptying and filling chambers further round the ring at the same time. Nothing in the "
     "building ever goes cold, so the heat of a burned chamber is not lost but _____.",
     ["measured", "inherited", "discarded", "concealed"], "B",
     "The gases drawn on from a chamber that has been fired are what warm the chamber next in "
     "line, so the heat passes forward to the following chamber. The option about discarding names "
     "what the ring kiln is built to prevent."),

 wic("W6",
     "The hollow pressed into the bed face of a brick is called the frog, and it is not there to "
     "save clay. Mortar spread on the course below is pushed up into the hollow as the brick is "
     "bedded, and when it sets it forms a block of mortar keyed into the brick itself, which a "
     "sliding force must break before the joint will give way. The hollow makes the finished joint "
     "_____ against movement along the bed.",
     ["thinner", "cheaper", "smoother", "stiffer"], "D",
     "A block of mortar keyed into the brick has to be broken before the joint can slide, which is "
     "a gain in resistance. Nothing in the passage concerns the cost of the brick, which is the "
     "explanation the first sentence rules out."),

 wic("W7",
     "A wall two bricks thick can be built as two separate walls standing side by side, and such a "
     "wall will split along its length under load. Laying some bricks across the thickness rather "
     "than along it, so that a single brick reaches from one face through to the other, binds the "
     "two together into one member. The pattern of these crossing bricks in the face of a wall is "
     "therefore not ornament but _____.",
     ["structure", "decoration", "repair", "measurement"], "A",
     "Bricks reaching through the thickness are said to bind the two leaves into one member, which "
     "is a load-carrying function. The option naming decoration is what the closing phrase "
     "explicitly denies."),

 meaning("W8",
         "New brickwork often shows a white bloom across its face within a few months. Salts "
         "already present in the brick and in the mortar dissolve in the water the wall took in "
         "during building; as the wall dries, that water travels to the surface and evaporates "
         "there, leaving the salt behind as a crust. The bloom therefore <u>marks</u> the end of "
         "the drying rather than the beginning of decay, and it is usually brushed off once and "
         "does not return.",
         "marks",
         ["stains", "indicates", "scores", "celebrates"], "B",
         "The bloom is being read as a sign that drying has finished, so the verb reports what the "
         "bloom shows. The sense of leaving a stain would describe the crust itself rather than "
         "the information it gives."),

 wic("W9",
     "A plain roofing tile hangs on a horizontal batten by a small projection moulded on its back "
     "near the head. Nothing but that projection and the tile's own weight holds it in place, "
     "which is why a tiled roof can be stripped and reset by hand and why a single broken tile can "
     "be lifted out and another slid in. The whole covering is thus _____ rather than fixed.",
     ["hung", "sealed", "welded", "buried"], "A",
     "Each tile rests on a batten by a projection and its own weight, which is the arrangement the "
     "blank has to name and which the passage contrasts with being fixed. Nothing in the passage "
     "describes a seal, and a covering that could be sealed could not be lifted tile by tile."),

 wic("W10",
     "A painted pattern on a floor tile wears away under boots within a generation. The medieval "
     "tiler instead stamped the pattern into the soft clay to the depth of a finger-nail, filled "
     "the hollow with a white clay of a different colour and fired the two together, so that the "
     "design ran through the thickness of the tile rather than lying on top of it. Wear on such a "
     "floor is _____ the pattern, because the same pattern appears again at every level.",
     ["powerless against", "fatal to", "responsible for", "invisible on"], "A",
     "The design runs through the thickness and reappears at every level, so wearing the surface "
     "away cannot remove it. Saying wear is fatal to the pattern would contradict the reason the "
     "closing clause supplies."),

 wic("W11",
     "Along the south coast whole terraces that appear to be built of brick are in fact timber "
     "houses hung with tiles shaped so that the exposed part of each is the size and colour of a "
     "brick face, its lower edge thickened to throw a shadow like a joint. Only at a corner, or "
     "where a tile has fallen, does the arrangement become _____ to a passer-by.",
     ["apparent", "acceptable", "profitable", "traditional"], "A",
     "The whole point of the covering is that it passes for brickwork, so a corner or a gap is "
     "where the truth of it can be seen. An option about the covering becoming profitable would "
     "have nothing to do with what a passer-by notices."),

 meaning("W12",
         "A block comes to the mason's bench sawn to a rough rectangle and no more. He squares one "
         "face with a chisel, works the next square to it, and only then cuts the mouldings, "
         "checking each stage against a zinc template. A block <u>dressed</u> in that order can be "
         "set in the wall as it stands, because every later measurement has been taken from a face "
         "already known to be true.",
         "dressed",
         ["clothed", "worked", "arranged", "bandaged"], "B",
         "The passage describes squaring faces and cutting mouldings with a chisel, so the word "
         "names the shaping of the stone. The clothing sense belongs to the ordinary use of the "
         "word and not to a block of stone under a chisel."),

 # ---------------------------------------------- Text Structure and Purpose (6)
 tsp("T1",
     "In the older sort of kiln the flame rises from the fire mouths straight up through the "
     "setting and out at a hole in the crown, and the ware at the top of the chamber is always "
     "hotter than the ware at the bottom. <u>A gas will travel wherever the draught takes it, "
     "regardless of whether that path leads upward or downward.</u> The down-draught kiln closes "
     "the crown, carries the flame up the side walls and lets it fall through the setting to flues "
     "in the floor, which are joined to a chimney tall enough to pull it there.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It states the principle that makes the arrangement described afterwards possible.",
      "It concedes a weakness in the down-draught kiln described afterwards.",
      "It defines a technical term introduced in the preceding sentence.",
      "It questions whether the older kiln behaved as the first sentence claims."],
     "A",
     "Pulling flame downward through a setting only makes sense once the reader accepts that gas "
     "follows the draught rather than simply rising, which is what the sentence establishes. The "
     "option about conceding a weakness misreads a statement that enables the later design into an "
     "objection to it."),

 tsp("T2",
     "Cut into the faces of many medieval churches are small incised figures, a few strokes each, "
     "repeated on stone after stone. They are not decoration: the same mark appears on blocks in "
     "quite different parts of a building and never twice in one course by accident. Where a "
     "cathedral's accounts survive alongside its walls, the marks can sometimes be matched to the "
     "men named in them as paid by the piece. The marks are, in short, the record a paymaster "
     "needed of who had worked which stone.",
     "Which choice best states the main purpose of the text?",
     ["To argue that the marks were a decorative scheme that later builders abandoned.",
      "To explain what the incised marks on medieval church stones were for.",
      "To compare the accounts of two cathedrals with one another.",
      "To describe the tools with which the marks were made."],
     "B",
     "The text moves from what the marks look like to what the paymaster needed them for, so it "
     "sets out to account for their purpose. The option calling them a decorative scheme names the "
     "reading the second sentence rejects outright."),

 tsp("T3",
     "Square holes appear in the faces of many old walls, often in regular rows a metre or so "
     "apart and at intervals up the height of the building. <u>The horizontal poles that carried "
     "the working platforms were bedded in the wall as it rose and cut off when it was finished.</u> "
     "An archaeologist can therefore read from the empty holes how high the builders went in a "
     "season, where they stopped and started again, and which parts of the front were being worked "
     "at the same time.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It offers the explanation of the holes that lets the closing sentence treat them as evidence.",
      "It gives an example of a wall in which such holes can be seen.",
      "It disputes the claim about spacing made in the first sentence.",
      "It summarises the conclusions the archaeologist reaches."],
     "A",
     "The final sentence can read building seasons off the holes only once the holes are known to "
     "be the sockets of the working platform, which the underlined sentence supplies. The option "
     "calling it a summary of the archaeologist's conclusions puts it after the reasoning when it "
     "comes before it."),

 tsp("T4",
     "The great wheel still standing in the roof of more than one English church is some five "
     "metres across, and two men walked inside it to turn it. A man's weight is a poor engine, but "
     "a wheel of that diameter turning a drum a fifth as wide multiplies what he can pull by five, "
     "and a man walking can push against the boards for hours without the jerks a team of haulers "
     "gives. What such a wheel offered a medieval builder was not power so much as steady power "
     "under close control, which is exactly what a stone hanging over a finished vault requires.",
     "Which choice best states the main purpose of the text?",
     ["To explain why a machine of modest power suited the work it was built for.",
      "To trace the spread of the great wheel from one country to another.",
      "To argue that medieval builders lacked any better source of power.",
      "To describe the churches in which such wheels survive."],
     "A",
     "The text sets the wheel's small power against the steadiness and control it gave, and closes "
     "by matching that steadiness to the job of landing a stone over a vault. The option about "
     "tracing the machine's spread describes a history the passage never touches."),

 tsp("T5",
     "Terracotta blocks were pressed in moulds from a fine clay and fired hard enough to shed "
     "water, and a Victorian architect could order a whole cornice by the yard. <u>Every block was "
     "made hollow, with thin webs of clay across the void.</u> A solid block of that size would "
     "have taken weeks to dry and would have cracked in the fire; hollow, it dried evenly, weighed "
     "little enough for one man to set, and could be filled with mortar once it was in place.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It introduces the feature that the rest of the text explains the reasons for.",
      "It admits a defect that the closing sentence proposes a remedy for.",
      "It repeats in other words the claim made in the first sentence.",
      "It supplies a measurement needed for the calculation that follows."],
     "A",
     "Everything after the underlined sentence gives reasons the blocks were made hollow, so the "
     "sentence names the feature to be accounted for. Reading it as an admitted defect misses that "
     "hollowness is presented throughout as the advantage."),

 tsp("T6",
     "For centuries a brick was whatever size a local mould happened to be, and a bricklayer "
     "moving twenty miles found the courses of a wall no longer met his rule. The change came from "
     "the counting house rather than the trade: once bricks were taxed by the thousand, a maker "
     "who enlarged his brick paid the same tax for more wall, and once they were sold by the "
     "thousand at a distance, a buyer needed to know what a thousand would build. The size that "
     "settled out of that argument is very nearly the size still made.",
     "Which choice best describes the overall structure of the text?",
     ["It presents a problem, identifies the pressures that resolved it, and notes the result.",
      "It describes a tool and then lists the trades that used it.",
      "It sets out two competing theories and endorses neither.",
      "It follows one bricklayer through a single day's work."],
     "A",
     "The text opens on the difficulty of unequal bricks, turns to the tax and the distant trade "
     "that forced a standard, and ends with the size that survives, which is a problem followed by "
     "its resolution. The option about two competing theories describes a shape the passage never "
     "takes, since it settles on one account."),

 # --------------------------------------------- Cross-Text Connections (3)
 ctc("X1",
     "A tile pressed by machine is the same weight and the same thickness as the last, and a roof "
     "laid with such tiles lies flat and takes fewer of them to the square yard. The handmade tile "
     "was admired for a variation that was, in plain terms, a failure to hold a size. Nobody who "
     "has stripped a two-hundred-year-old roof and found a third of the tiles cracked at the nib "
     "will mourn the loss of that irregularity.",
     "Handmade tiles vary in thickness by a few millimetres, and the variation is what gives an "
     "old roof its broken surface and its changing colour under a low sun. It also does work: a "
     "roof of slightly uneven tiles drains along many small channels rather than lying in one "
     "plane, and it tolerates a rafter that has moved. Machine tiles laid over the same old timber "
     "must either be bedded on packing or be allowed to ride, and the roofer's answer is usually "
     "to renew the timber instead.",
     "Based on the texts, how would the author of Text 2 most likely respond to the claim in Text "
     "1 that the variation of handmade tiles is simply a failure to hold a size?",
     ["By agreeing that the variation is a fault but arguing that buyers have grown fond of it.",
      "By pointing out that the variation has practical uses on an old roof that a uniform tile does not serve.",
      "By noting that machine tiles crack at the nib as often as handmade ones do.",
      "By denying that handmade tiles vary in thickness at all."],
     "B",
     "Text 2 credits the uneven tiles with draining along many channels and tolerating a moved "
     "rafter, which treats the variation as useful rather than as a mere defect. The option "
     "denying that handmade tiles vary contradicts Text 2's own opening sentence."),

 ctc("X2",
     "Scored into the plaster floor of a chamber high in the cathedral are full-size curves, "
     "circles and mouldings, cut with a compass and a straightedge and overlaid one on another. "
     "The lines are working drawings. A mason setting out a window needed the shapes at their true "
     "size, and the floor was the only surface large enough to carry them; a zinc or board "
     "template could then be cut directly from the line on the floor and carried down to the bench.",
     "The floor carries far more lines than any one window can account for, and some of the curves "
     "belong to no opening in the building. Read as a record of jobs, that is waste. Read as a "
     "place where apprentices were taught the geometry of a traceried head by drawing it out "
     "under a master's eye, the crowding is exactly what one would expect, and the few lines that "
     "match built windows are the exercises that happened to be used.",
     "Which choice best describes the relationship between the two texts?",
     ["Text 2 offers a different account of the same evidence that Text 1 explains.",
      "Text 2 supplies the measurements that Text 1 says are missing.",
      "Text 2 questions whether the lines on the floor exist at all.",
      "Text 2 applies Text 1's conclusion to a second cathedral."],
     "A",
     "Both texts are about the same scored floor, and the second reads the crowded lines as "
     "teaching exercises where the first reads them as working drawings, which is a rival "
     "explanation of one body of evidence. The option about a second cathedral introduces a "
     "building neither text mentions."),

 ctc("X3",
     "The duty laid on bricks in 1784 was charged by the thousand, and makers answered it in the "
     "obvious way: they made the brick bigger. Bricks a third larger than the old size appear in "
     "the yards within a few years of the duty, and the Act of 1803 that taxed large bricks at a "
     "higher rate reads as an admission that the first duty had been evaded exactly so.",
     "Bricks larger than the old size were being moulded in several counties before 1784, and the "
     "largest of all come from yards that lay outside the duty altogether. Size followed the clay "
     "and the kiln: a heavy brick made from a lean clay could be burned through, while the same "
     "brick in a fat clay warped. The duty may have hurried a change along, but a maker who "
     "enlarged his brick after 1784 was doing what his clay had already allowed his neighbour to "
     "do before it.",
     "Based on the texts, the author of Text 2 would most likely characterise the explanation "
     "offered in Text 1 as",
     ["mistaken about the date at which the duty was first charged.",
      "correct in every respect but too narrowly focused on a single county.",
      "plausible but incomplete, since it overlooks a cause already at work.",
      "impossible to test, because no bricks of the period survive."],
     "C",
     "Text 2 allows that the duty may have hurried the change while insisting that clay and kiln "
     "were enlarging bricks before it, which treats Text 1's account as partial rather than wrong. "
     "The option calling the explanation untestable is ruled out by Text 2's own appeal to bricks "
     "moulded before 1784."),
]
