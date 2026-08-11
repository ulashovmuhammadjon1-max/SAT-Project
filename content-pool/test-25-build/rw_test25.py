#!/usr/bin/env python3
"""
Reading & Writing authored for Test 25.

All 81 items are original. The transcribed pool was spent long ago, and for R&W
authoring is in any case the safer route: a transcribed answer key has to be
re-derived by hand before it can be trusted (Test 5 shipped 6 wrong answers in
81 that way). Every item below carries a `why` recording the reasoning that
produced the key AND the reason the strongest distractor fails — that record IS
the verification, so no key exists here without one.

Rationales name options by their CONTENT, never by letter, so balance_rw.py is
free to rotate every question when it evens out the key distribution.

Writing-domain choices are worded, never bare punctuation: every Boundaries
option repeats the words on either side of the blank so that each choice reads
as the resulting sentence. Form/Structure items whose options are genuinely
words ("is" / "are", "stand" / "stands") are left as words, which is how the
real test presents them.

Command of Evidence mixes three quotation items (E1-E3), three finding-if-true
items (E4-E6) and three data items (E7-E9). The data items carry a real <table>
in the passage using the house style block; none of them describes a graph in
prose, because no image can be produced from here.

Rhetorical Synthesis appears in BOTH of its real shapes: six items quote "the
notes" and three (R2, R5, R8) quote "the given sentences". A build that knows
only the first shape misclassifies the second — that bug was live in Test 1.

Test 25's assigned territory is papermaking and pulp mills, dye works, ink and
pigment grinding, bookbinding, and paper marbling, together with the colour
science that sits behind them.

TOPICS SCREENED AND DROPPED BEFORE ANYTHING WAS DRAFTED. Test 16 (printing) is
the dangerous neighbour: it already holds most of the obvious ground in this
trade, and screen_topics.py found it by keyword before a word was written.
Dropped for that reason:

    the hand mould and deckle against the Fourdrinier web (rw_test16:T1);
    sizing a sheet with gelatine so ink will not spread (rw_test16:W2);
    iron gall ink biting into the page (rw_test16:W3, rw_test13:C6);
    a mordant such as alum linking dye to fibre (rw_test16:W7);
    lead white stacked over vinegar and tan bark (rw_test16:W10);
    the lightfastness of lake pigments measured in units (rw_test16:E8);
    orchil steeped from lichen (rw_test16:R5); rag paper against wood pulp and
    the acid left in the sheet (rw_test16:N7, rw_test16:I2);
    a binder resewing sections onto new cords (rw_test16:F4);
    two dyehouses working the same weld under a north light (rw_test16:F5) —
    which is also why no comparative item here takes the form "deeper than
    _____ in the other house";
    fastness tested at the window and in the wash (rw_test16:W14);
    the long fibres of the paper mulberry (rw_test18:I5);
    woad against Indian indigo by yield (rw_test14:T7); murex and Tyrian purple
    priced by the labour of collection (rw_test14:E5) — which also rules out any
    "the price was set by the labour rather than the secret" claim shape;
    cochineal exported from Oaxaca (rw_test8:R7); Prussian blue in Japanese
    woodblock prints (rw_test11:R7); synthetic ultramarine dating a panel
    (rw_test9:I5); a watermark placing a manuscript within a decade
    (rw_test8:B10, rw_test10:B10); and suminagashi, where a brush of surfactant
    makes each ring spread inside the last (rw_test15:B6) — which is why no item
    here explains ox gall.

Blocks (fixed by the assembler's quota, 3 modules x 27):
    Words in Context 15 (three of them the underlined-word-meaning variant),
    Text Structure and Purpose 6, Central Ideas and Details 6,
    Command of Evidence 9, Inferences 6, Boundaries 12,
    Form, Structure, and Sense 9, Transitions 9, Rhetorical Synthesis 9  = 81
"""

SOURCE = "AUTHORED-T25"
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
    """Rhetorical Synthesis, notes shape."""
    bullets = "".join(f"<li>{n}</li>" for n in notes)
    return dict(
        num=num, skill="Rhetorical Synthesis",
        passage=f"While researching a topic, a student has taken the following notes:<ul>{bullets}</ul>",
        stem=f"The student wants to {goal} Which choice most effectively uses relevant "
             "information from the notes to accomplish this goal?",
        choices=choices, answer=answer, why=why)


def syn_sentences(num, sentences, goal, choices, answer, why):
    """Rhetorical Synthesis, given-sentences shape — the second real phrasing."""
    bullets = "".join(f"<li>{n}</li>" for n in sentences)
    return dict(
        num=num, skill="Rhetorical Synthesis",
        passage="While working on a paragraph, a student has written the following "
                f"sentences:<ul>{bullets}</ul>",
        stem=f"The student wants to {goal} Which choice most effectively uses "
             "information from the given sentences to accomplish this goal?",
        choices=choices, answer=answer, why=why)


QUESTIONS = [

 # ------------------------------------------------------ Words in Context (15)
 wic("W1",
     "Fibres that come out of the beater cut short give a sheet that is bulky and opaque but pulls "
     "apart in the hand. Fibres bruised and frayed along their length without being shortened give "
     "one that is hard, translucent and strong. The papermaker settles which he gets by the weight "
     "of the roll and the hours the stuff runs, so what happens in the beater is _____ of the "
     "finished sheet rather than a preparation for making it.",
     ["the character", "the cost", "the size", "the colour"], "A",
     "The passage lists opacity, bulk, hardness and strength as the properties the beating settles, "
     "and those together are what the sheet is like. The option naming cost points at an economic "
     "consequence the passage never raises."),

 wic("W2",
     "A sheet just formed on the wire is a mat of water held by nothing but the tangle of its own "
     "fibres, and it will not bear its own weight. The vatman turns the mould face down onto a "
     "woollen felt and presses; the sheet leaves the wire and lies on the felt, and a second felt "
     "goes on top of it. Until the whole pile has been through the press, every operation depends on "
     "a step whose only purpose is to make the sheet _____.",
     ["movable", "opaque", "thinner", "whiter"], "A",
     "The passage says the new sheet cannot bear its own weight and then describes transferring it "
     "onto a felt that can carry it, so the step exists to allow the sheet to be handled at all. "
     "The option about thinness names something the press does later and not what the couching is "
     "for."),

 wic("W3",
     "Wood is held together by lignin, and a mill that grinds the log to fibre leaves nearly all of "
     "it in the sheet. Cooking the chips in an alkaline liquor instead dissolves the lignin and "
     "frees fibres that are longer and far less brittle, though the yield from a tonne of wood falls "
     "by about half. A mill choosing between the two processes is deciding whether its paper must be "
     "cheap or _____.",
     ["strong", "smooth", "thin", "white"], "A",
     "The passage sets the halved yield of the alkaline process against fibres that are longer and "
     "less brittle, which is a description of strength bought at a price. The option naming "
     "smoothness picks a property the passage attaches to neither process."),

 meaning("W4",
         "A conservator mending a torn leaf uses wheat-starch paste and a thin tissue, both of "
         "which can be taken off again with water and nothing stronger. A synthetic adhesive makes "
         "the stronger mend, but lifting it later calls for solvents that attack the leaf as well "
         "as the mend. Conservators choose the weaker material because a mend that can be "
         "<u>undone</u> leaves the next generation a choice of its own.",
         "undone",
         ["reversed", "untied", "ruined", "neglected"], "A",
         "The passage contrasts a mend that comes away with water against one that cannot be "
         "lifted without damage, so the word means taken back rather than spoiled. The option "
         "meaning ruined names the outcome the conservator is trying to avoid, not the property "
         "being praised."),

 wic("W5",
     "A yellow struck on wool with alum comes out bright; the same plant liquor worked in an iron "
     "pot gives an olive so different that it was sold under another name. Nothing has been added "
     "that carries a colour of its own, and a dyer who wants the darker shade need change nothing "
     "but the vessel. The part iron plays in the bath is therefore _____.",
     ["modifying", "decorative", "temporary", "accidental"], "A",
     "The passage says the iron contributes no colour of its own and yet alters the colour the "
     "plant gave, which is a description of something acting on a result rather than adding to it. "
     "The option calling the effect temporary contradicts the fact that the olive is a shade dyers "
     "sold deliberately."),

 wic("W6",
     "Perkin was eighteen and trying to make quinine when a flask left a black sludge that stained "
     "alcohol a brilliant purple. He might have washed it down the sink; a hundred residues in the "
     "same laboratories were. Instead he dyed a strip of silk, sent it to a dye house for an "
     "opinion, and held a patent within the year. What separates his accident from the others was "
     "not the residue but the _____ that followed it.",
     ["enquiry", "publicity", "expense", "coincidence"], "A",
     "The passage lists dyeing a test strip, seeking an expert opinion and patenting, all of which "
     "are steps taken to find out what the substance was worth. The option about publicity would "
     "describe how the discovery was announced, which the passage never mentions."),

 wic("W7",
     "Wool is a protein fibre carrying places along its length that will bond with an acid dye "
     "directly, and an hour in a warm bath with a little acid colours it through. Cotton is "
     "cellulose and offers such a dye almost nothing, which is why cotton dyers turn to dyes that "
     "either lodge inside the fibre or form a chemical bond with it. The two fibres differ less in "
     "how deeply they can be coloured than in what the colour must find to _____.",
     ["grip", "cover", "outlast", "repeat"], "A",
     "The passage contrasts a fibre offering bonding places with one offering almost none, so the "
     "missing word names holding on rather than any quality of the colour itself. The option about "
     "covering describes what a pigment does on a surface, and the passage is about dye taken up "
     "inside the fibre."),

 wic("W8",
     "Vermilion is a brilliant red mercury sulphide, and on some medieval panels it has gone a dull "
     "grey-black at the surface while remaining red a fraction of a millimetre below. The change is "
     "found only where the paint has been exposed to light, and chlorides turn up wherever it has "
     "happened. The darkening is therefore not the pigment ageing throughout but a reaction that is "
     "strictly _____.",
     ["superficial", "gradual", "reversible", "harmless"], "A",
     "The passage stresses that the red survives a fraction of a millimetre below the blackened "
     "face, which confines the change to the surface. The option calling the change gradual "
     "describes its pace, which the passage never gives, and would not answer the contrast with "
     "ageing throughout."),

 wic("W9",
     "Verdigris gave a green no other pigment of the period could match, and manuscripts painted "
     "with it are now often pierced clean through wherever the green was laid on thickest. The "
     "copper salt attacks the cellulose beneath it, and the attack goes on in the dark and in dry "
     "air. A colour prized above all others for its brilliance turned out to be _____ to the page "
     "that carried it.",
     ["hostile", "indifferent", "superior", "essential"], "A",
     "Holes eaten clean through the page describe a pigment actively destroying its support. The "
     "option meaning indifferent would say the pigment did nothing to the page, which is the "
     "opposite of what the passage reports."),

 wic("W10",
     "A pigment ground finer covers more ground, but grinding can go too far: coarse azurite is a "
     "deep blue, and the same mineral reduced to a flour is pale. There is no number of turns that "
     "settles the question, because it differs with the mineral and with the oil. The colourman "
     "lifts the muller, looks and decides, so where the grinding should stop is a matter of _____.",
     ["judgement", "tradition", "arithmetic", "chance"], "A",
     "The passage denies that any fixed count of turns will serve and then describes the colourman "
     "looking and deciding, which is a description of skilled assessment. The option naming chance "
     "makes the outcome random, while the passage presents a decision being taken."),

 wic("W11",
     "A film of linseed oil left on glass does not dry as a puddle of water dries. It gains weight "
     "while it hardens, because what is happening is a reaction with oxygen from the air that links "
     "the molecules of the oil into a network. Nothing evaporates, and the film cannot afterwards be "
     "dissolved in the oil it was made from. To call such a paint dry is therefore _____.",
     ["misleading", "premature", "technical", "generous"], "A",
     "The passage shows that the ordinary sense of drying, in which something evaporates and leaves "
     "the rest behind, describes none of what happens here. The option meaning premature would say "
     "the film is not yet dry, but the passage says it has hardened."),

 wic("W12",
     "The binder of a watercolour is a gum that dissolves again the moment water touches it, which "
     "is what lets a painter lift a passage out of a wash weeks after it was laid down. The same "
     "property means a finished sheet must never meet damp, and a drop of rain on a mounted "
     "watercolour takes the paint with it. The gum's readiness to redissolve is at once the "
     "medium's greatest _____ and its worst weakness.",
     ["convenience", "expense", "mystery", "rarity"], "A",
     "The sentence pairs the missing word against 'weakness', and the advantage the passage has just "
     "described is the ease of correcting work already done. The option naming expense introduces a "
     "cost, which is not an advantage and is nowhere in the passage."),

 wic("W13",
     "Feathers carrying melanin wear far more slowly than white ones, which is why the wingtips of "
     "many gulls are black although the rest of the bird is not. The pigment does not merely colour "
     "the barbs: it packs into them and leaves them harder and stiffer, and a worn black tip is "
     "rarer than a worn white one on the same wing. Black at the wingtip is therefore best explained "
     "as _____.",
     ["protective", "decorative", "seasonal", "inherited"], "A",
     "The passage attributes slower wear to the pigment and locates the black exactly where wear is "
     "worst, so the colour is doing a defensive job. The option calling the black decorative names "
     "the reading the passage sets aside with the word 'merely'."),

 meaning("W14",
         "A binder who marbles the edges of a volume produces a pattern that runs continuously "
         "across the closed leaves. Take one leaf out and the pattern no longer meets; slip one in "
         "and it breaks in a different way. Nineteenth-century libraries valued marbled edges less "
         "for their appearance than for the way they made an interference with a book <u>plain</u>.",
         "plain",
         ["obvious", "ordinary", "modest", "unadorned"], "A",
         "The passage is about a pattern that stops matching, so a tampered book announces itself, "
         "and the word means readily seen. The option meaning unadorned is a common sense of the "
         "word but would contradict a page described as decorated."),

 meaning("W15",
         "Two pieces of cloth dyed with different mixtures can match exactly under a shop's lamps "
         "and differ unmistakably at the window. The eye reports only three signals, and two "
         "different spectra can produce the same three. A buyer who checks a match under one light "
         "has learned nothing about how the two pieces will <u>agree</u> under another.",
         "agree",
         ["correspond", "consent", "cooperate", "conclude"], "A",
         "The word describes two colours matching each other, not two people reaching a decision. "
         "The option meaning to give consent applies to people and cannot be said of two pieces of "
         "cloth."),

 # -------------------------------------------- Text Structure and Purpose (6)
 tsp("T1",
     "A hand mould covered in woven wire leaves no mark in the sheet formed on it. An older laid "
     "mould carries stout wooden ribs with fine wires running across them, and the pulp settles more "
     "thinly over every wire than beside it. <u>Hold a laid sheet up to a window and the ribs and "
     "wires appear as a ladder of lighter and darker lines.</u> Nothing has been printed on the "
     "paper; the pattern is a difference in thickness.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It offers a way of observing the difference the text has just described.",
      "It explains why laid moulds were given up in favour of woven ones.",
      "It corrects a mistaken account of how the pattern is produced.",
      "It introduces a second method of forming a sheet by hand."],
     "A",
     "The sentence tells a reader what to do — hold the sheet to the light — in order to see the "
     "uneven settling the previous sentence describes. The option about correcting a mistaken "
     "account fits the last sentence, which denies that the pattern is printed, rather than the "
     "underlined one."),

 tsp("T2",
     "Bark paper in Mesoamerica was never made from a pulp. Strips of inner bark were boiled in lime "
     "water, laid crosswise on a board and beaten with a grooved stone until the strips fused into a "
     "single sheet. Nothing was suspended in water and nothing was drained, so no mould was needed "
     "and no sheet had a fixed size. Amate is paper by what it does and not by how it is made.",
     "Which choice best states the main purpose of the text?",
     ["To show that a papermaking tradition arrived at a familiar product by an unfamiliar route.",
      "To argue that amate should not be described as paper at all.",
      "To trace the spread of bark paper across Mesoamerica.",
      "To compare the durability of amate with that of European paper."],
     "A",
     "The text describes an unusual process at length and closes by saying the result is still "
     "paper, which is a claim about route rather than category. The option saying amate is not "
     "paper reverses the final sentence."),

 tsp("T3",
     "Logwood yields a black deeper than any other dye then available, but the colour strikes only "
     "when the extract meets an iron salt, and cloth dyed with it greys within a few years in strong "
     "light. <u>English statutes of the sixteenth century forbade the import of the wood "
     "outright.</u> The ban stood for ninety years and was lifted only once dyers had learned to fix "
     "the colour with chrome.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It reports how an authority responded to the shortcoming just described.",
      "It identifies the discovery that removed the shortcoming.",
      "It questions whether the shortcoming was real.",
      "It explains where logwood was cut and how it was shipped."],
     "A",
     "The fading described in the first sentence is followed by a prohibition, so the underlined "
     "sentence supplies the official reaction to that fault. The option about the discovery that "
     "removed the shortcoming describes the chrome mordant in the final sentence."),

 tsp("T4",
     "A reader of a scroll who wants a passage in the middle must unwind everything before it and "
     "wind it up again afterwards, and can hold only one place at a time. A reader of a codex opens "
     "the boards at any leaf, keeps a finger in a second place, and moves between the two. The codex "
     "holds no more text than the roll it displaced and is no easier to make.",
     "Which choice best states the main purpose of the text?",
     ["To account for the adoption of a format in terms of what it allowed a reader to do.",
      "To argue that scrolls were more poorly made than codices.",
      "To describe in detail how a codex is bound.",
      "To establish when the codex replaced the scroll."],
     "A",
     "The text sets aside capacity and ease of manufacture in its last sentence and devotes the "
     "rest to what each format lets a reader do, which is an explanation of the change. The option "
     "about how a codex is bound describes material the text never supplies."),

 tsp("T5",
     "A marbler's colours float only on a bath thickened until it is barely pourable. Carragheen "
     "boiled from seaweed gives that consistency, but the strength of a batch varies with the weed "
     "and with the boiling, and a bath too thin lets the colours sink while one too thick will not "
     "let them spread. <u>Every marbler therefore drops a little colour on the bath and watches it "
     "before the first sheet of the day.</u>",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It describes a practical response to the variability the text has set out.",
      "It explains how carragheen is boiled from seaweed.",
      "It contrasts two ways of thickening a bath.",
      "It gives a reason for abandoning carragheen."],
     "A",
     "The preceding sentence says the thickness cannot be relied on from batch to batch, and the "
     "underlined sentence gives the test that answers that uncertainty. The option about how "
     "carragheen is boiled describes the material rather than the marbler's response to it."),

 tsp("T6",
     "A quire was twenty-four sheets and a ream twenty quires, or four hundred and eighty. A "
     "printer's ream held five hundred, the extra sheets being expected to spoil in the press. "
     "Stationers sold by one count and printers bought by the other, and contracts of the period "
     "take care to say which is meant. The two figures record not a disagreement about arithmetic "
     "but two trades measuring the same object for different purposes.",
     "Which choice best describes the overall structure of the text?",
     ["It presents two conflicting figures and then accounts for the difference between them.",
      "It defines a term and then traces how its meaning narrowed.",
      "It describes a dispute and then reports how it was settled.",
      "It lists several units of measure and then recommends one of them."],
     "A",
     "The text gives two counts for one word and closes by explaining why each trade needed its "
     "own, which is a difference accounted for rather than a dispute resolved. The option about a "
     "dispute being settled would need the passage to report an outcome, and it reports that both "
     "counts stayed in use."),

 # --------------------------------------------- Central Ideas and Details (6)
 cid("C1",
     "Until the 1840s a painter or an apprentice ground the day's colours into oil on a slab each "
     "morning, and whatever was left over skinned over and hardened by the next day. The "
     "collapsible metal tube, patented in 1841, held ground paint for months and went into a box "
     "with the brushes. Painters who had until then worked out of doors from sketches began to "
     "carry the whole picture out and finish it there.",
     "Which choice best states the main idea of the text?",
     ["A change in the way paint could be kept altered where painting was done.",
      "Paint ground by hand each morning was of better quality than paint sold in tubes.",
      "Painters before 1841 had almost never worked out of doors.",
      "The collapsible tube was devised in order that painters might work out of doors."],
     "A",
     "The passage moves from paint that could not be kept overnight, to paint that kept for "
     "months, to painters finishing canvases outdoors, which makes storage the cause and the place "
     "of work the effect. The option saying the tube was devised for outdoor painting supplies a "
     "purpose the passage never states, and the passage says painters were already outdoors making "
     "sketches."),

 cid("C2",
     "Ground lapis lazuli yields a dull grey powder, because the rock is mostly colourless mineral "
     "with the blue scattered through it. The colour was recovered by kneading the powder into a "
     "paste of wax and resin under warm lye: the blue particles passed into the water while the rest "
     "stayed behind in the paste. Three washings gave three grades, the first the richest and the "
     "last nearly grey, and the price of the pigment followed the yield of the first washing.",
     "According to the text, why did ground lapis lazuli have to be treated further before it could "
     "be used as a pigment?",
     ["The blue mineral in it was mixed with a great deal of colourless material.",
      "The rock could not otherwise be ground fine enough to use.",
      "The blue faded unless it had first been washed in lye.",
      "The wax and resin deepened the colour of the powder."],
     "A",
     "The first sentence gives the reason directly: the rock is mostly colourless mineral, so "
     "grinding alone gives grey. The option about fading reverses the passage, which says the "
     "washing separates the blue rather than preserving it."),

 cid("C3",
     "A binder's tool is heated and pressed through gold leaf onto leather that has first been "
     "washed with glaire, a thin wash of egg white. The heat sets the glaire, which holds the gold "
     "where the tool touched and nowhere else, and the surplus leaf is rubbed away afterwards with "
     "an oiled rag. The gold is not stuck down by an adhesive spread beforehand but by one that does "
     "nothing until the tool arrives.",
     "According to the text, what determines where the gold leaf remains on the leather?",
     ["The places at which the heated tool set a wash already on the surface.",
      "The places at which an adhesive was applied before the leaf was laid down.",
      "The pressure with which the surplus leaf was rubbed away afterwards.",
      "The pattern cut into the leather before the wash was applied."],
     "A",
     "The passage says the glaire covers the whole surface and is set only where the tool touches, "
     "so the tool decides the pattern. The option about adhesive applied beforehand is the reading "
     "the final sentence explicitly rejects."),

 cid("C4",
     "The red of a poppy petal and the blue of a cornflower are built from the same class of "
     "molecule. Anthocyanins shift colour with the acidity of the sap around them and with the metal "
     "ions bound to them, so one pigment serves for red, purple and blue in plants that are close "
     "relatives. A gardener who limes the soil under a hydrangea does not give the plant a different "
     "pigment; the pigment it already has behaves differently.",
     "According to the text, what accounts for the different colours anthocyanins produce?",
     ["The conditions surrounding the molecule rather than differences between molecules.",
      "The presence of a second pigment in the blue-flowered plants.",
      "The thickness of the petal in which the pigment sits.",
      "The age of the flower at the moment it is picked."],
     "A",
     "The passage names acidity and bound metal ions as what changes and states that the molecule "
     "itself is the same class throughout. The option about a second pigment supplies a mechanism "
     "the passage rules out by making one pigment do all three colours."),

 cid("C5",
     "A headband at the top of a spine was once worked in silk over a cord that was laced into the "
     "boards, and it took part of the strain when a reader hooked a finger over the head of the book "
     "to pull it off a shelf. Machine binding kept the look and dropped the work: a modern headband "
     "is a woven strip glued to the back of the sections and fastened to nothing. What survives is "
     "the appearance of a structural member.",
     "Which choice best states the main idea of the text?",
     ["A feature that once carried load is now kept only for the way it looks.",
      "Modern headbands are stronger than headbands worked by hand.",
      "Readers should not pull a book from a shelf by its headband.",
      "Silk headbands were given up because silk became too expensive."],
     "A",
     "The text contrasts a headband laced into the boards and bearing strain with one glued on and "
     "fastened to nothing, and calls what remains an appearance. The option about the cost of silk "
     "supplies a cause the passage never gives."),

 cid("C6",
     "A drop of a dye mixture placed near the end of a paper strip and stood in solvent separates as "
     "the solvent climbs: each component travels at a rate set by how strongly it clings to the "
     "paper against how readily it dissolves. A dye sold as one colour may resolve into four bands. "
     "The strip shows nothing about what those components are, only that they are several and in "
     "what proportion.",
     "According to the text, what does the separation on the paper strip establish about a dye?",
     ["How many components it contains and in what proportion, but not what they are.",
      "The chemical identity of each of its components.",
      "Whether its colour will fade in strong sunlight.",
      "How strongly it will bind to a length of cloth."],
     "A",
     "The last sentence states the limit exactly: number and proportion, not identity. The option "
     "about chemical identity is what the passage says the method cannot supply."),

 # ------------------------------------------------- Command of Evidence (9)
 coe("E1",
     "A notebook kept by the master of a paper mill between 1794 and 1801 survives in the mill's "
     "archive. Historian Aled Cannon argues that the master kept it in order to trace a faulty sheet "
     "back to the man who had made it, rather than to record how the paper was made.",
     "Which quotation from the notebook most effectively illustrates Cannon's claim?",
     ["&ldquo;Every post is chalked with the vatman&rsquo;s own mark before it goes under the press, "
      "so that a bad sheet may be carried back to him that made it.&rdquo;",
      "&ldquo;Rags of the third sort are to be cut small and boiled a full hour longer than the "
      "second.&rdquo;",
      "&ldquo;The new felts from Kendal are dearer by ninepence and wear the season "
      "longer.&rdquo;",
      "&ldquo;Three journeymen taken on at Michaelmas, one discharged before Christmas.&rdquo;"],
     "A",
     "The quotation describes a mark applied for the stated purpose of returning a defective sheet "
     "to its maker, which is precisely the tracing the claim describes. The quotation about boiling "
     "rags an hour longer is a note of method, which is the alternative purpose the claim sets "
     "aside."),

 coe("E2",
     "In 1873 a dyer gave evidence to an inquiry into cloth that had come out of his works clouded. "
     "Historian Ruth Ivimey argues that his evidence was framed throughout to show that the fault "
     "lay in the yarn he had been sent rather than in his dyeing.",
     "Which quotation from the evidence most effectively illustrates Ivimey&rsquo;s claim?",
     ["&ldquo;Both pieces went into one bath at one time and came out together, and only the piece "
      "woven from the Bradford yarn was clouded.&rdquo;",
      "&ldquo;I have dyed in this town one-and-thirty years, and my father before me.&rdquo;",
      "&ldquo;Indigo has risen a shilling on the pound since the spring, and the trade must bear "
      "it.&rdquo;",
      "&ldquo;The vat is set at blood heat and is never suffered to go cold overnight.&rdquo;"],
     "A",
     "One bath, one time, two pieces and only one of them faulty isolates the yarn as the single "
     "thing that differed, which is the argument the claim describes. The quotation about the vat "
     "never being allowed to go cold defends the dyeing in general and identifies nothing about the "
     "yarn."),

 coe("E3",
     "A conservator's report of 1879 on a cathedral library records the condition of some four "
     "hundred volumes. Historian Peter Bao argues that the report was written to show that the "
     "damage the library had suffered came from the way the books were bound and not from the way "
     "they were handled.",
     "Which quotation from the report most effectively illustrates Bao&rsquo;s claim?",
     ["&ldquo;In every instance the tear begins at the joint, where the leather has perished, and "
      "not at the fore-edge that a hand must touch.&rdquo;",
      "&ldquo;The room is lit by six windows facing south and is not heated in winter.&rdquo;",
      "&ldquo;Four hundred and eleven volumes were examined in the course of eleven days.&rdquo;",
      "&ldquo;The shelves are of oak and stand a foot clear of the outer wall.&rdquo;"],
     "A",
     "Locating every tear at the perished joint and expressly not at the edge a reader touches "
     "separates the binding from the handling, which is the distinction the claim rests on. The "
     "quotation about the number of volumes examined establishes the survey's scale and says "
     "nothing about the cause of any damage."),

 coe("E4",
     "Marbled papers are often attributed to particular workshops on the strength of their patterns. "
     "Conservator Ines Halloran argues that such attributions can be put on a firmer footing, "
     "because the spacing of the teeth on a workshop's comb is fixed and shows in the spacing of the "
     "lines drawn through the floating colour.",
     "Which finding, if true, would most directly support Halloran's argument?",
     ["Sheets from two workshops known to have worked to the same pattern name were found to differ "
      "consistently in the spacing of the lines drawn through the colour.",
      "Marbled papers made in the same workshop often use the same range of colours.",
      "Combs were usually made by the marblers themselves rather than bought from a supplier.",
      "The same pattern names were used by workshops in several different countries."],
     "A",
     "A consistent difference in line spacing between two workshops using one pattern name shows "
     "that the spacing distinguishes workshops where the pattern name does not, which is exactly "
     "what the argument requires. The finding that combs were made in the workshop explains why "
     "spacings might differ but does not show that they do."),

 coe("E5",
     "A sheet of white paper looks white under a candle and again at noon, although the light "
     "reaching the eye differs enormously between the two. Psychologist Tomas Lehr argues that the "
     "visual system achieves this by comparing regions of a scene with one another rather than by "
     "measuring the light from any region on its own.",
     "Which finding, if true, would most directly support Lehr's argument?",
     ["When observers viewed a patch through a tube that hid everything around it, they judged its "
      "colour by the light coming from it and lost the constancy entirely.",
      "Observers took longer to name a colour by candlelight than they did at noon.",
      "The retina contains three kinds of cone, each most sensitive in a different band of "
      "wavelengths.",
      "Colour constancy is measurably poorer in observers over the age of seventy."],
     "A",
     "Removing the surroundings removes the comparison the argument depends on, and the constancy "
     "goes with it, which ties the effect to the comparison rather than to the patch. The finding "
     "about three kinds of cone describes the receptors and is consistent with either account of "
     "what is done with their signals."),

 coe("E6",
     "The rust-brown spots called foxing are commonly explained as colonies of fungi that settled on "
     "a sheet during storage. Conservation scientist Mira Oyelaran argues instead that the spots "
     "mark particles of iron left in the sheet when it was made, and that fungi arrive afterwards.",
     "Which finding, if true, would most directly support Oyelaran's argument?",
     ["X-ray fluorescence located a concentration of iron at the centre of every spot examined, "
      "including spots on sheets kept in stores too dry for fungi to grow.",
      "Fungi have been cultured from the surface of foxed sheets in several collections.",
      "Foxing is commoner on papers made after 1800 than on papers made before it.",
      "Sheets kept in a damp store developed more spots than sheets kept in a dry one."],
     "A",
     "Iron at the centre of every spot puts the metal where the mark is, and the dry-store cases "
     "show the spots forming where fungi cannot, which meets the argument on both points. The "
     "finding that damp stores produce more spots is at least as easily explained by the fungal "
     "account it is meant to displace."),

 coe("E7",
     "A printer tested four inks on the same paper, recording how long each took to dry and how far "
     "each spread into the sheet from a printed line."
     + table(["Ink", "Drying time (hours)", "Spread into the sheet (mm)"],
             [["Ink 1", "2.5", "0.7"], ["Ink 2", "3.5", "0.3"],
              ["Ink 3", "6.0", "0.2"], ["Ink 4", "3.0", "0.6"]])
     + "The printer needed an ink that dried within four hours and spread no more than 0.4 "
       "millimetres, and the only ink meeting both requirements was _____",
     "Which choice most effectively uses data from the table to complete the text?",
     ["ink 2, which dried in 3.5 hours and spread 0.3 millimetres.",
      "ink 3, which spread least of the four, at 0.2 millimetres.",
      "ink 1, which dried fastest of the four, in 2.5 hours.",
      "ink 4, which dried in 3.0 hours and spread 0.6 millimetres."],
     "A",
     "Only the second ink is inside both limits, at 3.5 hours and 0.3 millimetres, while the third "
     "takes six hours and the first and fourth spread 0.7 and 0.6 millimetres. The option naming "
     "the ink that spread least ignores the drying requirement, which that ink fails by two "
     "hours."),

 coe("E8",
     "A dye house measured how much of the dye in the bath the wool had taken up after one hour at "
     "four bath temperatures."
     + table(["Bath temperature (&deg;C)", "Dye taken up after one hour (%)"],
             [["40", "38"], ["60", "71"], ["80", "92"], ["98", "95"]])
     + "Raising the bath from 60 to 80 degrees produced a far larger gain in uptake than raising it "
       "again from 80 to 98 degrees, since _____",
     "Which choice most effectively uses data from the table to complete the text?",
     ["uptake rose from 71 per cent to 92 per cent over the first of those steps but only from 92 "
      "per cent to 95 per cent over the second.",
      "uptake at the lowest temperature tested, 40 degrees, was only 38 per cent.",
      "uptake reached its highest recorded value, 95 per cent, at 98 degrees.",
      "uptake rose by more than 30 percentage points between 40 and 60 degrees."],
     "A",
     "The completion has to compare the two steps named in the sentence, and only this option gives "
     "both, 21 percentage points against 3. The option reporting the rise between 40 and 60 degrees "
     "is a true reading of the table but concerns neither of the two steps under comparison."),

 coe("E9",
     "A laboratory cut strips from the papers of four mills, along the grain and across it, and "
     "folded each strip until it broke."
     + table(["Mill", "Folds along the grain", "Folds across the grain"],
             [["Fenton", "1,150", "240"], ["Hulme", "780", "190"],
              ["Marlow", "2,100", "520"], ["Rushton", "410", "95"]])
     + "Every paper withstood more folds along the grain than across it, and the paper for which "
       "that difference was greatest was the one from _____",
     "Which choice most effectively uses data from the table to complete the text?",
     ["Marlow, which withstood 2,100 folds along the grain and 520 across it.",
      "Rushton, which withstood 410 folds along the grain and 95 across it.",
      "Fenton, which withstood 1,150 folds along the grain.",
      "Hulme, whose strips withstood 190 folds across the grain."],
     "A",
     "The difference of 1,580 folds for the Marlow paper is larger than the differences of 910, 590 "
     "and 315 recorded for the others. The option naming the Rushton paper reports the mill with "
     "the largest ratio between the two figures rather than the largest difference, and its "
     "difference is the smallest of the four."),

 # ---------------------------------------------------------- Inferences (6)
 inf("I1",
     "A fifteenth-century panel shows a sky that is green rather than blue, and analysis finds the "
     "green layer to be azurite, a blue copper carbonate that converts to green malachite in damp "
     "conditions. The conversion has taken place across the whole sky and nowhere in the robe on the "
     "same panel, which was painted in ultramarine. The state of the sky therefore _____",
     ["reflects the behaviour of the pigment used there rather than any intention of the painter.",
      "shows that the sky and the robe were painted at widely separated dates.",
      "proves that ultramarine was the preferred pigment for skies at the period.",
      "indicates that the panel was cleaned after the robe had been painted."],
     "A",
     "One pigment has changed and the other has not, on one panel under one history of storage, so "
     "the difference lies in the materials rather than in anything the painter did. The option "
     "about widely separated dates would need evidence about when each area was painted, and the "
     "passage gives none."),

 inf("I2",
     "Colour floated on a marbling bath will not stay on an untreated sheet: it lifts as soon as the "
     "sheet is rinsed. A sheet wiped beforehand with a solution of alum holds the same colour "
     "through the rinse, and a sheet wiped on one half only holds it on that half alone. The alum is "
     "therefore acting _____",
     ["on the sheet rather than on the colour floating in the bath.",
      "to thicken the bath so that the colours spread more slowly across it.",
      "to make the colours brighter than they would otherwise appear.",
      "to keep the sheet from taking up any water at all."],
     "A",
     "The colour is the same in every trial and only the treatment of the paper differs, and the "
     "half-treated sheet holds colour on exactly the treated half. The option about thickening the "
     "bath would predict the same result everywhere on a sheet, which the half-and-half trial rules "
     "out."),

 inf("I3",
     "Fibres recovered from waste paper are shorter than fibres that have not been used before, "
     "because every operation cuts them a little and each drying leaves them stiffer and less able "
     "to bond. A mill making cartons can work almost wholly from recovered stock; a mill making a "
     "paper that has to be folded and unfolded cannot go much beyond a third. The difference between "
     "the two mills therefore lies less in the fibre available to them than in _____",
     ["what the paper each of them makes is required to do.",
      "the quantity of waste paper each of them is able to collect.",
      "the age of the machinery each of them has installed.",
      "the price each of them pays for fibre that has not been used before."],
     "A",
     "Both mills are described as having the same recovered fibre available and differing only in "
     "the demands made on the paper they produce. The option about quantities collected introduces "
     "a supply difference the passage never mentions."),

 inf("I4",
     "An ink stick is lampblack ground with animal glue, moulded and dried, and it carries no water "
     "at all. The calligrapher rubs it on a wetted stone and makes only as much ink as the sitting "
     "needs. A stick two centuries old will still yield ink, while the same ink made up as a liquid "
     "and bottled grows mouldy within a season. Making the ink in solid form therefore _____",
     ["removes the ingredient that limits how long it can be kept.",
      "makes the black of the finished ink deeper than it would otherwise be.",
      "allows a wider range of pigments to be used in it.",
      "means that the ink can be applied without a brush."],
     "A",
     "The stick differs from the bottle in carrying no water, and it is the bottled ink that "
     "spoils, so the water is what shortens the life. The option about a deeper black claims an "
     "improvement in the colour, and the passage compares only how long each keeps."),

 inf("I5",
     "The human eye carries three kinds of cone; a starling's carries four, the extra one sensitive "
     "in the ultraviolet. Many starling feathers that look uniformly dark to us reflect strongly in "
     "the ultraviolet, in patterns that differ between males and females. A human observer sorting "
     "the birds by plumage alone would therefore _____",
     ["miss a difference that the birds themselves are equipped to see.",
      "be unable to tell the birds apart by any means whatever.",
      "find the two sexes easier to distinguish than another starling does.",
      "be right to conclude that the feathers reflect no ultraviolet."],
     "A",
     "The pattern that separates the sexes lies in a band the human eye cannot register and the "
     "starling's can, so the observer loses information the bird has. The option that the observer "
     "could not tell the birds apart at all goes further than the passage, which restricts the "
     "difficulty to sorting by plumage."),

 inf("I6",
     "Vellum takes up water from the air and gives it back again, and a leaf that has done so many "
     "times no longer lies flat. A medieval binding holds its text block closed between two boards "
     "under the pressure of a clasp, and volumes that have stayed clasped for five centuries open "
     "with their leaves still flat. Volumes whose clasps were stripped off in the nineteenth century "
     "have leaves that cockle. The clasp is therefore best understood as _____",
     ["a means of keeping the leaves under a pressure they need.",
      "a fastening meant to stop others from opening the book.",
      "a decorative fitting whose loss makes no practical difference.",
      "a device for holding the wooden boards themselves flat."],
     "A",
     "Clasped volumes stay flat and unclasped ones cockle, which makes the pressure the clasp "
     "maintains the working part of the fitting. The option calling the clasp decorative is exactly "
     "what the contrast between the two groups of volumes refutes."),

 # ---------------------------------------------------------- Boundaries (12)
 bnd("B1",
     "A rag engine will not make paper out of whatever is thrown into it. The rags must be sorted, "
     "cut and boiled first, and the sorting is done by hand and by eye. A single scrap of coloured "
     "cloth left among the white will show in every sheet of the _____ sorters were the best paid "
     "women in the mill.",
     ["post; the", "post, the", "post the", "post: and the"], "A",
     "Two complete statements stand on either side of the blank with no conjunction between them, "
     "which is what a semicolon is for. The comma on its own splices them together, and a colon "
     "cannot be followed by a conjunction."),

 bnd("B2",
     "Three faults will spoil a marbled sheet before the colour has even touched _____ too thin, a "
     "paper that has not been prepared, and a hand that hesitates as the sheet goes down.",
     ["it: a size", "it, a size", "it a size", "it; a size"], "A",
     "A complete statement announcing three faults is followed by the list of those faults, and a "
     "colon is the mark that introduces such a list. The semicolon would separate two complete "
     "statements, and what follows the blank is not one."),

 bnd("B3",
     "The dye that made Perkin's _____ was found by accident during a search for a way of making "
     "quinine.",
     ["fortune, mauveine,", "fortune mauveine,", "fortune, mauveine", "fortune: mauveine,"], "A",
     "The name interrupts the sentence to rename the dye already mentioned, and an interruption of "
     "that kind takes a comma at each end. Closing it without opening it, or opening it without "
     "closing it, leaves the sentence unbalanced."),

 bnd("B4",
     "Vermilion was made by heating mercury with sulphur in a closed pot, and what condensed on the "
     "lid was a black powder. Grinding that powder turned it _____ the change was so unlike anything "
     "else in the trade that some took the pigment for a proof of transmutation.",
     ["red; indeed,", "red, indeed,", "red indeed,", "red: indeed"], "A",
     "The words on either side of the blank are each a complete statement, and the second opens "
     "with a connecting adverb rather than a conjunction, so a semicolon is needed before it. The "
     "comma leaves two statements joined by nothing that can join them."),

 bnd("B5",
     "The rule the old colourmen are said to have taught their apprentices was _____ until the stone "
     "tells you to stop.",
     ["short: grind", "short, grind", "short grind", "short; grind"], "A",
     "A complete statement is followed by the rule it has just announced, which is what a colon "
     "introduces. A semicolon would call for a second complete statement, and the words after the "
     "blank are an instruction rather than one."),

 bnd("B6",
     "A colourman's apprentice was bound to the trade for seven _____ could not set up on his own "
     "account until the whole term had been served.",
     ["years, and he", "years and he", "years, he", "years; and, he"], "A",
     "Two complete statements are joined by a conjunction, and a comma belongs in front of that "
     "conjunction. Dropping the comma leaves the join unmarked, and dropping the conjunction "
     "splices the two statements together."),

 bnd("B7",
     "The long fibres of the paper mulberry, beaten only enough to part them from one _____ a sheet "
     "that can be pulled very thin and still hold together.",
     ["another, make", "another make", "another; make", "another: make"], "A",
     "The phrase describing how the fibres were beaten interrupts the sentence between its subject "
     "and its verb and must be closed with a comma. Leaving the comma out runs the interruption "
     "into the verb, and neither the semicolon nor the colon may stand between a subject and its "
     "verb."),

 bnd("B8",
     "Alizarin, the colouring matter of the madder _____ synthesised in 1869, and within twenty "
     "years the madder fields of Provence had gone out of cultivation.",
     ["root, was", "root was", "root; was", "root: was"], "A",
     "A phrase renaming alizarin has been opened with a comma and must be closed with one before "
     "the sentence resumes. A semicolon or colon at that point would cut the subject off from its "
     "own verb."),

 bnd("B9",
     "The bindery's day book records the work sent out that week: eleven volumes in half calf, for "
     "the cathedral library; six in cloth, for a _____ in vellum, for a private buyer who is not "
     "named.",
     ["school; and one", "school, and one", "school and one", "school: and one"], "A",
     "The items in this list carry commas inside them, so the items themselves are separated by "
     "semicolons. A comma at the blank would be the fourth in a row and could not be told from the "
     "commas inside the items."),

 bnd("B10",
     "The mill still runs the beater it installed in _____ is the last engine of its kind at work "
     "anywhere in the country.",
     ["1873, which", "1873 which", "1873; which", "1873: which"], "A",
     "The clause adds information about a beater already identified by its date, so it is set off "
     "with a comma. Without the comma it reads as picking out which beater is meant, and the "
     "sentence has already done that."),

 bnd("B11",
     "Because the tone of a finished sheet is settled long before it reaches the _____ mill sorts "
     "its white rags into four grades and keeps each grade in a bin of its own.",
     ["vat, the", "vat the", "vat; the", "vat: the"], "A",
     "An introductory subordinate clause stands before the main statement and is separated from it "
     "by a comma. A semicolon or a colon would need a complete statement on each side, and the "
     "words before the blank are not one."),

 bnd("B12",
     "Sheets are hung to dry in spurs of four or five over ropes strung the length of the drying "
     "_____ loft is boarded on all sides with slats the miller can open and shut, because a wind "
     "that dries them too quickly is as bad as no wind at all.",
     ["loft; the", "loft, the", "loft the", "loft: and the"], "A",
     "Two complete statements meet at the blank with nothing to join them, which calls for a "
     "semicolon. The comma produces a splice, and a colon does not take a conjunction after it."),

 # --------------------------------------------- Form, Structure, and Sense (9)
 fss("F1",
     "The dye house works four vats from a single boiler, and the steam will not serve two at once. "
     "Each of the four vats _____ set going at a different hour of the morning.",
     ["is", "are", "were", "have been"], "A",
     "The subject is 'each', which is singular, and the words naming the vats sit in a phrase that "
     "cannot change the number of the subject. The plural forms agree with 'vats' instead, which is "
     "not what the sentence is about."),

 fss("F2",
     "The colourman was grinding for three painters at once that week, and by noon on the Friday all "
     "three _____ orders were standing finished on the bench.",
     ["painters'", "painter's", "painters", "painters's"], "A",
     "The orders belong to all three painters, so the noun must be both plural and possessive, "
     "which puts the apostrophe after the plural ending. The singular possessive would say the "
     "orders belonged to one painter, and the plain plural marks no possession at all."),

 fss("F3",
     "By the time the mill fitted its first machine in 1807, the vatmen _____ paper there by hand "
     "for ninety years.",
     ["had been making", "have been making", "are making", "make"], "A",
     "The making runs up to a point in the past named in the sentence, which is what the past "
     "perfect is for. The present perfect would run the making up to the present day, and the mill "
     "stopped making by hand in 1807."),

 fss("F4",
     "Neither of the two dye houses would say what its yellow was struck with, and each guarded "
     "_____ recipe as closely as it guarded its accounts.",
     ["its", "their", "it&rsquo;s", "there"], "A",
     "The pronoun stands for 'each', which is singular, and the possessive form of the singular "
     "pronoun carries no apostrophe. The plural form disagrees with 'each', and the form with an "
     "apostrophe is the contraction of 'it is'."),

 fss("F5",
     "On the shelf above the muller _____ the four stoppered bottles of oil that the colourman keeps "
     "for grinding.",
     ["stand", "stands", "has stood", "is standing"], "A",
     "The sentence is inverted, and its subject is the bottles, which are plural, so the verb must "
     "be plural too. The singular forms agree with 'shelf', which is part of the introductory "
     "phrase rather than the subject."),

 fss("F6",
     "Beaten for four hours instead of one, _____",
     ["the pulp gave a sheet that was hard and translucent.",
      "the papermaker found the sheet hard and translucent.",
      "the sheet was found by the papermaker to be hard and translucent.",
      "hardness and translucency were what appeared in the sheet."], "A",
     "The opening phrase describes what was beaten, so the thing beaten has to be named "
     "immediately after it, and that is the pulp. The version that begins with the papermaker says "
     "the papermaker was beaten for four hours."),

 fss("F7",
     "The apprentice's day was spent sorting rags, cutting them small and _____ the boiler.",
     ["feeding", "to feed", "fed", "he fed"], "A",
     "The three activities are in one list and the first two are given as '-ing' forms, so the "
     "third must take the same form. The infinitive and the past form break the pattern the list "
     "has already set."),

 fss("F8",
     "Although the colour looked perfectly even while the cloth was still in the bath, streaks _____ "
     "as soon as the piece was hung up to dry.",
     ["appeared", "appear", "have appeared", "will appear"], "A",
     "Both of the sentence's other verbs report a completed past event, so the verb at the blank "
     "must be past as well. The present and future forms describe a time the rest of the sentence "
     "has already ruled out."),

 fss("F9",
     "The binder _____ the library sent the damaged volumes had worked on the same collection thirty "
     "years earlier.",
     ["to whom", "to who", "whom", "which"], "A",
     "The pronoun is the object of 'to', which calls for the object form of the pronoun that refers "
     "to a person. The subject form cannot follow a preposition, and the pronoun used for things "
     "cannot refer to a binder."),

 # --------------------------------------------------------- Transitions (9)
 trn("N1",
     "Rags came into the mill filthy and were boiled in a lye before they went anywhere near the "
     "beater. The boil loosens the dirt, but it also weakens the fibre, and an hour too long shows "
     "up months later as a sheet that tears at the fold. _____ the boiling time was the one figure "
     "the foreman set himself and gave to nobody.",
     ["As a result,", "Nevertheless,", "Similarly,", "In particular,"], "A",
     "The damage an over-long boil does is the reason the time was guarded, so the transition marks "
     "a consequence. A concession would require the last sentence to run against the danger just "
     "described, and it follows from it."),

 trn("N2",
     "Paper made on a machine has two faces that are not alike: the side that lay on the wire takes "
     "its impression and stays a little rougher, while the side under the felt is smoother and holds "
     "rather more filler. _____ a printer ordering paper for a fine halftone specifies which of the "
     "two faces is to be printed.",
     ["Accordingly,", "In contrast,", "For example,", "Admittedly,"], "A",
     "The two unlike faces are what oblige the printer to name one, so the last sentence states a "
     "consequence of the difference. A contrast would set the printer's practice against the "
     "difference rather than deriving it from it."),

 trn("N3",
     "Some pigments are chemically at war with the materials around them, and a painter who picks "
     "one for its colour alone may be storing up trouble for the picture. _____ orpiment is a "
     "sulphide, and the copper and lead colours laid beside it blacken where the two meet.",
     ["For instance,", "However,", "Therefore,", "Instead,"], "A",
     "A general statement about hostile pigments is followed by one such pigment named and its "
     "effect described, which is an illustration. A contrast would require orpiment to behave "
     "unlike the pigments just described, and it is a case of them."),

 trn("N4",
     "Perkin's mauve faded badly and was out of fashion within a decade of the excitement that "
     "greeted it. _____ the industry his accident began was selling several hundred coal-tar colours "
     "by 1900.",
     ["Even so,", "In short,", "Likewise,", "Meanwhile,"], "A",
     "The failure of the one colour is set against the growth of the whole industry, so the "
     "transition concedes the first before asserting the second. A transition of time would say "
     "only that the two things happened together and would lose the opposition between them."),

 trn("N5",
     "Libraries lit by gas took sulphur dioxide in with the air, and the acid it formed rotted the "
     "leather of every binding standing on an open shelf. _____ books shut away in closed presses in "
     "the very same rooms came through the century sound.",
     ["By contrast,", "Consequently,", "In addition,", "For instance,"], "A",
     "The books in closed presses escaped the damage that the books on open shelves suffered, so "
     "the second sentence opposes the first. A consequence marker would make the survival of the "
     "shut-away books follow from the rotting of the others."),

 trn("N6",
     "Lampblack is very nearly pure carbon and does not fade, and the black of a two-thousand-year-"
     "old ink is as deep now as the day it was laid down. _____ the paper under it has usually gone "
     "brown, so the contrast a reader sees today is not the contrast the scribe saw.",
     ["However,", "Therefore,", "Furthermore,", "For instance,"], "A",
     "The ink's permanence is set against the change in the sheet beneath it, which is an "
     "opposition. A consequence marker would make the browning of the paper follow from the "
     "stability of the ink, and the passage presents them as independent."),

 trn("N7",
     "A sheet lifted from the vat holds about ninety-five parts of water to five of fibre. The press "
     "drives out most of it in a few minutes; everything that remains has to leave as vapour. _____ "
     "it was the drying loft and not the vat that fixed how much paper an old mill could make in a "
     "year.",
     ["Consequently,", "By contrast,", "For example,", "Nonetheless,"], "A",
     "Water that can only leave slowly, as vapour, is what makes the loft rather than the vat the "
     "limiting stage, so the last sentence draws a consequence. A contrast would set the loft "
     "against the vat as an unrelated fact instead of explaining why it governs."),

 trn("N8",
     "The sections of a hand-bound book are sewn one after another onto cords stretched in a frame, "
     "and the ends of those cords are afterwards laced into the boards. _____ the boards, the sewing "
     "and the sections are a single structure rather than three parts stuck together.",
     ["In effect,", "Nevertheless,", "For example,", "Earlier,"], "A",
     "The last sentence restates what the described construction amounts to, which is what this "
     "transition marks. A concession would require the conclusion to run against the construction "
     "just described, and it summarises it."),

 trn("N9",
     "Ochre is dug out of the ground, washed, dried and ground, and it needs nothing else done to "
     "it. It costs next to nothing, covers well and does not fade. _____ it is both the oldest "
     "pigment we can identify and one still sold in every colourman's shop.",
     ["Not surprisingly,", "By contrast,", "Nevertheless,", "For instance,"], "A",
     "The cheapness, ease and permanence just listed are exactly what would lead a reader to expect "
     "long and continuing use, so the transition marks the expected outcome. A concession would "
     "present the continued use as unexpected, which the preceding sentences make it anything but."),

 # ------------------------------------------------- Rhetorical Synthesis (9)
 syn("R1",
     ["Turkey red is a brilliant red dyed on cotton with madder.",
      "The European process, learned from the Levant in the 1740s, could take three months.",
      "It ran to more than a dozen steps, among them steeping the cloth in rancid oil.",
      "Chemists could not say what the oil steps did until the 1880s.",
      "Cotton dyed by the process kept its colour through decades of washing."],
     "emphasise why dyers used the process in spite of its difficulty.",
     ["Although the Turkey red process ran to more than a dozen steps and could take three months, "
      "it gave cotton a red that survived decades of washing.",
      "The Turkey red process was learned from the Levant in the 1740s and involved steeping the "
      "cloth in rancid oil.",
      "Chemists could not explain what the oil steps in the Turkey red process did until the 1880s.",
      "Turkey red is a brilliant red dyed on cotton with madder."],
     "A",
     "The goal asks for the difficulty and the reason for accepting it, and only this option gives "
     "both, setting the steps and the months against a colour that lasted decades. The option about "
     "the chemists reports a gap in understanding rather than a reason for using the process."),

 syn_sentences("R2",
     ["A woad vat is set with bran and madder as well as with the woad itself.",
      "The bran and madder feed bacteria that strip the oxygen out of the liquor.",
      "Only once the oxygen has gone does the blue become soluble.",
      "A vat that has stopped working is said to have died."],
     "explain to an audience already familiar with dyeing why the bran and madder are added.",
     ["The bran and madder feed bacteria that strip the oxygen out of the liquor, and only once the "
      "oxygen has gone does the blue become soluble.",
      "A woad vat is set with bran and madder as well as with the woad itself, and a vat that has "
      "stopped working is said to have died.",
      "A woad vat contains three things: woad, bran and madder.",
      "Bacteria in a woad vat consume the bran and madder that are added to it."],
     "A",
     "The goal asks why the two extra ingredients are there, and only this option carries the chain "
     "from feeding the bacteria to removing the oxygen to dissolving the blue. The option saying "
     "the bacteria consume the bran and madder stops at the first link and never reaches the dye."),

 syn("R3",
     ["Indian yellow was a transparent yellow pigment imported into Europe from Bengal.",
      "It arrived as hard, foul-smelling balls.",
      "A British official reported in 1883 that it was made from the urine of cattle fed on mango "
      "leaves.",
      "No other account of its manufacture has ever been found, and the trade ended soon "
      "afterwards.",
      "Analysis of surviving balls has identified the compound that such a diet would produce."],
     "explain why the 1883 report is now taken seriously.",
     ["Although the 1883 report is the only account of how Indian yellow was made, analysis of "
      "surviving balls has identified the compound that the diet it describes would produce.",
      "Indian yellow reached Europe from Bengal as hard, foul-smelling balls.",
      "The trade in Indian yellow ended soon after 1883, and no further account of its manufacture "
      "has been found.",
      "A British official reported in 1883 that Indian yellow was made from the urine of cattle fed "
      "on mango leaves."],
     "A",
     "The goal asks what supports the report, and only this option pairs its isolation as a source "
     "with the chemical confirmation that backs it. The option that simply repeats what the official "
     "wrote gives the claim without any of the support that makes it credible."),

 syn("R4",
     ["Stare at a red patch for half a minute and then look at white paper: a green patch appears.",
      "The colour of an after-image is always the opposite of the colour stared at.",
      "Three kinds of cone by themselves do not explain why the pairs are red-green and "
      "blue-yellow.",
      "Cells further back in the visual system respond to the difference between cone signals.",
      "Such a cell is excited by one colour of a pair and inhibited by the other."],
     "explain what after-images suggest about the handling of colour signals.",
     ["Because an after-image is always the opposite of the colour stared at, colour cannot be "
      "handled by the cone types alone: cells further back respond to the difference between cone "
      "signals, excited by one colour of a pair and inhibited by the other.",
      "Staring at a red patch for half a minute produces a green after-image on white paper.",
      "The human retina contains three kinds of cone, and after-images appear when the eye is "
      "turned to a white surface.",
      "Cells in the visual system are excited by one colour and inhibited by another."],
     "A",
     "The goal asks what the after-image shows about processing, and only this option reasons from "
     "the opposition of the pairs to the cells that take differences between cone signals. The "
     "option describing the excitation and inhibition on its own states the mechanism without "
     "connecting it to the after-image that is supposed to be evidence for it."),

 syn_sentences("R5",
     ["Rags never bleach to a true white, and the sheet made from them keeps a yellow cast.",
      "Papermakers added a trace of blue pigment to the stuff in the vat.",
      "The blue does not remove the yellow; it absorbs a little more of the light that the yellow "
      "cast returns.",
      "The sheet reflects less light overall and yet is judged whiter."],
     "explain how adding a blue pigment can make a sheet look whiter.",
     ["A trace of blue does not remove the sheet's yellow cast but absorbs some of the light that "
      "cast returns, so the sheet reflects less light overall and is still judged whiter.",
      "Rags never bleach to a true white, and the sheet made from them keeps a yellow cast.",
      "Papermakers added a trace of blue pigment to the stuff in the vat.",
      "A sheet with blue pigment in it reflects less light than a sheet without any."],
     "A",
     "The goal asks how the addition works, and only this option carries the reader from the "
     "absorption of the light the yellow returns to the paradox of a darker sheet looking whiter. "
     "The option stating that the sheet reflects less light gives the surprising half of the result "
     "with none of the explanation."),

 syn("R6",
     ["Before 1931 a colour could be specified only by naming or sending a physical sample.",
      "Samples fade, and two people may disagree about whether two samples match.",
      "In 1931 an international body defined an average observer from matching experiments with a "
      "few dozen people.",
      "A colour could then be stated as three numbers worked out from its spectrum.",
      "Two dyers in different countries could specify one colour without exchanging anything "
      "physical."],
     "emphasise the practical change the 1931 definition brought about.",
     ["By defining an average observer, the 1931 standard allowed a colour to be stated as three "
      "numbers worked out from its spectrum, so that two dyers in different countries could specify "
      "one colour without exchanging anything physical.",
      "The 1931 standard observer was defined from matching experiments carried out with a few "
      "dozen people.",
      "Before 1931 a colour could be specified only by naming or sending a physical sample, and "
      "samples fade.",
      "An international body met in 1931 and defined an average observer."],
     "A",
     "The goal asks for the practical change, and only this option reaches the two dyers who no "
     "longer need to send each other anything. The option describing how the standard observer was "
     "derived explains the method and stops short of any consequence."),

 syn("R7",
     ["A binder trimmed a book's edges with a plough, a knife drawn across the closed leaves in a "
      "press.",
      "The plough cuts a few leaves at a time and takes several minutes for one book.",
      "The guillotine, introduced in the 1830s, cuts a stack of several hundred sheets at one "
      "stroke.",
      "Sheets can be guillotined before they are sewn.",
      "A book trimmed with a plough can be trimmed again only by losing more of its margins."],
     "explain how the guillotine changed the order in which a book is made.",
     ["Because the guillotine cuts several hundred sheets at one stroke, trimming could be done "
      "before the sheets were sewn rather than after the book was bound.",
      "The plough cuts a few leaves at a time and takes several minutes to trim one book.",
      "The guillotine was introduced in the 1830s and cuts a stack of several hundred sheets at "
      "one stroke.",
      "A book trimmed with a plough can be trimmed again only by losing more of its margins."],
     "A",
     "The goal is about the order of operations, and only this option says that trimming moved from "
     "after the binding to before the sewing. The option describing the guillotine's capacity gives "
     "the machine without the change in sequence that the goal asks for."),

 syn_sentences("R8",
     ["A dye that strikes the fibre very quickly colours the first part of the cloth it meets most "
      "deeply.",
      "The finished piece is then blotchy rather than evenly coloured.",
      "A retarding agent added to the bath competes with the dye for places on the fibre.",
      "The dye attaches more slowly and spreads through the cloth before it fixes."],
     "explain how a retarding agent improves an uneven dyeing.",
     ["A retarding agent competes with the dye for places on the fibre, so the dye attaches more "
      "slowly and spreads through the cloth before it fixes instead of colouring the first part it "
      "meets most deeply.",
      "A dye that strikes the fibre very quickly gives a blotchy piece rather than an evenly "
      "coloured one.",
      "A retarding agent is added to the dye bath before the cloth goes in.",
      "Dyes attach themselves to places on the surface of the fibre."],
     "A",
     "The goal asks how the agent improves the result, and only this option links the competition "
     "for places on the fibre to the slower, more even attachment. The option describing the "
     "blotchy piece states the problem the agent is meant to solve rather than how it solves it."),

 syn("R9",
     ["A girdle book was bound with a long tail of leather hanging below its boards.",
      "The tail was knotted and tucked under a belt, so the book hung upside down at the wearer's "
      "side.",
      "Lifted to the hands, the book came up the right way round and could be read without being "
      "unfastened.",
      "Fewer than thirty survive.",
      "Most are known from paintings rather than from surviving examples."],
     "explain the purpose of the leather tail to an audience unfamiliar with medieval bindings.",
     ["The long leather tail was knotted under a belt so that the book hung at the wearer's side "
      "and came up the right way round when it was lifted to be read.",
      "Fewer than thirty girdle books survive, and most are known from paintings.",
      "A girdle book was bound with a long tail of leather hanging below its boards.",
      "Girdle books were carried at the wearer's side rather than in the hand."],
     "A",
     "The goal asks what the tail was for, and only this option gives both what it did — hold the "
     "book at the belt — and why that mattered, namely that the book arrived the right way up. The "
     "option saying the books were carried at the side reports the result without mentioning the "
     "tail that produced it."),
]
