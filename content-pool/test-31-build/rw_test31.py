#!/usr/bin/env python3
"""
Reading & Writing authored for Test 31.

All 81 items are original. The transcribed pool was spent long ago, and for R&W
authoring is in any case the safer route: a transcribed answer key has to be
re-derived by hand before it can be trusted (Test 5 shipped 6 wrong answers in
81 that way). Every item carries a `why` recording the reasoning that produced
the key AND the reason the strongest distractor fails — that record IS the
verification, so no key exists here without one.

Rationales name options by their CONTENT, never by letter, so balance_rw.py is
free to rotate every question when it evens out the key distribution.

Writing-domain choices are worded, never bare punctuation: every Boundaries
option repeats the words on either side of the blank so that each choice reads
as the resulting sentence. Form/Structure items whose options are genuinely
words ("is" / "are", "has" / "have") are left as words, which is how the real
test presents them.

Test 31's territory is poultry and egg grading, dovecotes and pigeon lofts,
falconry and the mews, decoy ponds and wildfowling, and eel traps and fish
ponds. Test 17 holds dairying and Test 21 sericulture, so nothing here leaves
birds and freshwater fish.

THE SIZING RULE THIS FILE IS BUILT ON, and the reason it is stated first.
Test 23 recorded the lowest corpus overlap of any build — 0.14 — and still
failed on 15 internal same-subject pairs, one at 0.56 where the same paragraph
appeared twice. Its territory was narrow, and a narrow territory collides with
ITSELF long before it collides with the bank. The fix is to size the topic list
to the ITEM count, not the block count: this file therefore carries **81
distinct sub-topics, one per item**, not five sub-topics rotated through nine
blocks.

The rule bites hardest on Rhetorical Synthesis. A synthesis note list is a
sub-topic's core facts stated plainly, one per bullet, so pairing it with a
Words-in-Context passage on the same sub-topic makes collision the default
rather than the accident. All nine note lists here therefore sit on sub-topics
used by NO other item in the file:

    R1 the brood patch          R2 falconry words in everyday English
    R3 flyways and count timing R4 the moult and the pause in laying
    R5 sex-linked chick sorting R6 the Dutch origin of the word "decoy"
    R7 the rock dove in cities  R8 fishponds and the Lenten diet
    R9 poultry shows and breed standards

Topics were screened against ../rw_authored_corpus.json — all 1,295 passages
banked or authored across Tests 1-21 — before anything was drafted; see
screen_topics.py, whose keyword pass reported 98 of 113 territory terms with
zero corpus hits. The four hits that genuinely constrained the plan, and what
was done about each:

    rw_test12:C5 tells the European eel's whole Sargasso life cycle — born in
      the Sargasso, drifting east, glass eel, silver eel, the return swim. The
      eel items here therefore avoid the life-cycle narrative entirely and take
      eels as a FISHERY: the buck set in a weir gap (W6), the elver run and the
      pass built for it (C3, E5) and the mesh rule (N5).
    rw_test10:S2 is the Chincha guano trade, so N2 takes dovecote dung to the
      saltpetre house instead of to the field.
    rw_test21:W14 counts a seabird colony by separating returning breeders from
      first-time recruits, so E7 and R3 count wildfowl by date rather than by
      age class.
    rw_test11:F1 is a ringing station on a headland with a neither/nor subject,
      so F4's neither/nor sits at a poultry show and no item here is set at a
      ringing station.

Block counts, fixed by the assembler's quota of 27 x 3:
    Words in Context 15, Text Structure and Purpose 6, Central Ideas and
    Details 6, Command of Evidence 9, Inferences 6, Boundaries 12,
    Form, Structure and Sense 9, Transitions 9, Rhetorical Synthesis 9.

Command of Evidence mixes three quotation items (E1-E3), three
finding-if-true items (E4-E6) and three data items (E7-E9). The data items
carry a real <table> in the passage using the house style block; none of them
describes a graph in prose, because no image can be produced from here.
"""

TABLE = '<table style="border-collapse:collapse;margin:0.75rem 0;">{head}{body}</table>'
TH = ('<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;'
      'text-align:left;background:#F4F6F8;">{}</th>')
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">{}</td>'


def table(headers, rows):
    head = "<tr>" + "".join(TH.format(h) for h in headers) + "</tr>"
    body = "".join("<tr>" + "".join(TD.format(c) for c in r) + "</tr>" for r in rows)
    return TABLE.format(head=head, body=body)


def wic(num, passage, choices, answer, why):
    return dict(num=num, skill="Words in Context", passage=passage,
                stem="Which choice completes the text with the most logical and precise "
                     "word or phrase?",
                choices=choices, answer=answer, why=why)


def wic_mean(num, passage, word, choices, answer, why):
    return dict(num=num, skill="Words in Context", passage=passage,
                stem=f"As used in the text, what does the word &ldquo;{word}&rdquo; most "
                     "nearly mean?",
                choices=choices, answer=answer, why=why)


def tsp(num, passage, choices, answer, why):
    return dict(num=num, skill="Text Structure and Purpose", passage=passage,
                stem="Which choice best describes the function of the underlined sentence "
                     "in the text as a whole?",
                choices=choices, answer=answer, why=why)


def tsp_purpose(num, passage, choices, answer, why):
    return dict(num=num, skill="Text Structure and Purpose", passage=passage,
                stem="Which choice best states the main purpose of the text?",
                choices=choices, answer=answer, why=why)


def cid(num, passage, choices, answer, why):
    return dict(num=num, skill="Central Ideas and Details", passage=passage,
                stem="Which choice best states the main idea of the text?",
                choices=choices, answer=answer, why=why)


def cid_detail(num, passage, stem, choices, answer, why):
    return dict(num=num, skill="Central Ideas and Details", passage=passage,
                stem=stem, choices=choices, answer=answer, why=why)


def coe_quote(num, passage, stem, choices, answer, why):
    return dict(num=num, skill="Command of Evidence", passage=passage, stem=stem,
                choices=choices, answer=answer, why=why)


def coe_find(num, passage, stem, choices, answer, why):
    return dict(num=num, skill="Command of Evidence", passage=passage, stem=stem,
                choices=choices, answer=answer, why=why)


def inf(num, passage, choices, answer, why):
    return dict(num=num, skill="Inferences", passage=passage,
                stem="Which choice most logically completes the text?",
                choices=choices, answer=answer, why=why)


def bnd(num, passage, choices, answer, why):
    return dict(num=num, skill="Boundaries", passage=passage,
                stem="Which choice completes the text so that it conforms to the "
                     "conventions of Standard English?",
                choices=choices, answer=answer, why=why)


def fss(num, passage, choices, answer, why):
    return dict(num=num, skill="Form, Structure, and Sense", passage=passage,
                stem="Which choice completes the text so that it conforms to the "
                     "conventions of Standard English?",
                choices=choices, answer=answer, why=why)


def trn(num, passage, choices, answer, why):
    return dict(num=num, skill="Transitions", passage=passage,
                stem="Which choice completes the text with the most logical transition?",
                choices=choices, answer=answer, why=why)


def rsy(num, notes, goal, choices, answer, why):
    bullets = "".join(f"<li>{n}</li>" for n in notes)
    return dict(num=num, skill="Rhetorical Synthesis",
                passage=("While researching a topic, a student has taken the following "
                         f"notes:<ul>{bullets}</ul>"),
                stem=f"The student wants to {goal} Which choice most effectively uses "
                     "relevant information from the notes to accomplish this goal?",
                choices=choices, answer=answer, why=why)


QUESTIONS = [

 # ------------------------------------------------------ Words in Context (15)
 wic("W1",
     "A grader holds each egg in front of a small bright lamp in an otherwise dark room and "
     "turns it once. The shell becomes translucent, and the pocket of air at the blunt end "
     "shows as a dark crescent whose depth can be read off against a gauge. Nothing is "
     "opened and nothing is broken. Candling is valued at a packing station precisely "
     "because it leaves the egg it judges _____",
     ["intact.", "chilled.", "sorted.", "weighed."], "A",
     "The passage stresses that nothing is opened or broken and that the reading is taken "
     "through the shell, so the property being praised is that the egg survives the test "
     "unharmed. The option about sorting names what the grader does next rather than the "
     "condition the test leaves the egg in."),

 wic("W2",
     "A newly laid egg carries a thin moist layer over the shell that dries within minutes "
     "into a film across the thousands of pores. Washing takes that film off. An egg whose "
     "surface has been scrubbed loses water faster and admits bacteria that the film would "
     "have stopped, which is why some countries forbid washing altogether. The bloom is "
     "best understood as a coating that _____",
     ["seals.", "hardens.", "colours.", "cushions."], "A",
     "The film is described as lying across the pores and as keeping water in and bacteria "
     "out, which is the work of a seal. The option about hardening would describe a change "
     "in the shell's strength, and the passage attributes no strength to the film at all."),

 wic("W3",
     "The nest holes of a large dovecote run from the floor to the roof, and a keeper cannot "
     "reach them from a fixed ladder. A post is therefore stepped into the centre of the "
     "floor and pivoted at both ends, with two arms carrying a ladder at their outer tips. "
     "One push sends the whole assembly travelling round the wall. The potence turns a "
     "building whose contents are spread over every wall into one a single keeper can _____",
     ["work.", "afford.", "roof.", "enlarge."], "A",
     "The problem set up is that the holes cannot be reached, and the pivoted arms are "
     "described as bringing the ladder to every part of the wall, so what the device "
     "restores is the keeper's ability to get at the birds. Affordability is never at issue "
     "in the passage."),

 wic("W4",
     "A hawk that is startled throws itself off the fist and hangs upside down by its "
     "jesses, and each such attempt tires it and can break feathers. A close-fitting plume "
     "of leather slipped over its head ends the reaction at once, because a bird that sees "
     "nothing has nothing to launch itself away from. The hood is not a punishment but a "
     "way of making the bird's surroundings _____",
     ["irrelevant.", "familiar.", "quieter.", "smaller."], "A",
     "The explanation given is that a bird which cannot see has nothing to react to, so the "
     "hood removes the surroundings from the bird's calculations altogether. The option "
     "about familiarity would describe habituation over time, which is the opposite of the "
     "immediate effect the passage reports."),

 wic("W5",
     "From the open water a decoy pipe looks like nothing more than a ditch curving away "
     "under a hoop of netting, and the curve is deliberate: a duck swimming up it can never "
     "see the narrow end where the net closes. Screens of reed along the bank hide the "
     "decoyman, who works from behind them. The whole apparatus depends on keeping the "
     "outcome of the journey _____",
     ["hidden.", "delayed.", "shared.", "reversible."], "A",
     "The passage says twice that the birds cannot see the closed end and that the "
     "decoyman works out of sight, so the pipe works by concealing where the swim leads. "
     "The option about delay would suggest the birds eventually see the end, which the "
     "curve is designed to prevent."),

 wic("W6",
     "An eel buck is a wicker funnel some four metres long, set mouth upstream in a gap "
     "left in a weir so that the whole flow of that gap must pass through it. Eels moving "
     "downstream at night are carried in and cannot turn against the current to get out "
     "again. The fisherman builds no trap around the river; he simply makes the river's own "
     "movement _____",
     ["inescapable.", "measurable.", "gentler.", "seasonal."], "A",
     "The eels are described as being carried in by the flow and unable to swim back "
     "against it, so the current itself becomes the thing they cannot escape. The option "
     "about measurement describes a use for a gauge rather than the working of the trap."),

 wic("W7",
     "A stew pond that has carried carp for several years accumulates a black layer of "
     "waste on the bottom, and fish raised on it grow slowly and taste of mud. The keeper "
     "therefore lets the water off in spring, leaves the bed open to the sun and the frost "
     "for a season and sows it with a crop before flooding it again. Summering a pond is a "
     "way of letting the bed _____",
     ["recover.", "drain.", "settle.", "spread."], "A",
     "The passage sets a fouled bed against a season of sun, frost and cropping followed by "
     "reflooding, so the year out of use restores the bed to a state that will grow good "
     "fish. Draining names the first step of the process rather than what the season "
     "achieves."),

 wic("W8",
     "For the first week of its life a squab is fed on nothing its parents have gathered. "
     "The lining of the crop of both the cock and the hen thickens and sheds a substance "
     "richer in protein and fat than the milk of any mammal, and it is this that the young "
     "bird takes. Grain begins to appear in the diet only later. Crop milk allows a pigeon "
     "pair to raise young whose growth is briefly independent of what the fields _____",
     ["yield.", "cost.", "resemble.", "shelter."], "A",
     "The point of the paragraph is that the squab is fed on a secretion rather than on "
     "gathered food, so the growth is freed from what the fields produce. Cost would "
     "introduce a market that the passage never mentions."),

 wic("W9",
     "A punt gun is fired once. It is bolted into a boat barely wider than a man, and the "
     "gunner lies flat and paddles with his hands for the last two hundred metres so that "
     "nothing above the gunwale breaks the line of the water. If the birds lift before he "
     "is in range there is no second attempt that morning. Everything that matters in "
     "wildfowling of this kind happens before the shot, in the _____",
     ["approach.", "loading.", "aftermath.", "bargain."], "A",
     "The sentences describe the crawl across the water and the single chance it buys, and "
     "the closing sentence places the decisive work before the shot. Loading is part of "
     "preparing the gun and is not something the passage describes at all."),

 wic("W10",
     "A hawk that breaks a flight feather cannot simply be rested until it moults, because "
     "the next moult may be ten months away. The falconer keeps the feathers dropped in "
     "previous years, selects one of the same rank and wing, cuts both shafts at a slant "
     "and joins them on a splinter of bamboo. The repaired feather is dead tissue in any "
     "case, so imping restores the wing without waiting for the bird to _____",
     ["regrow it.", "be manned.", "put on weight.", "be rehooded."], "A",
     "The problem stated is the ten-month wait for the next moult, and the repair is "
     "presented as the way round that wait, so what is avoided is waiting for a new feather "
     "to grow. Manning is the separate business of accustoming a hawk to people."),

 wic_mean("W11",
          "A hen that has gone broody sits tight over her clutch, refuses food for most of "
          "the day and will strike at a hand put under her. She loses condition steadily and "
          "lays nothing at all while it lasts. To a keeper who wants eggs this is a fault; to "
          "one who wants chicks it is the whole point. The same behaviour is a nuisance or an "
          "asset according to what the flock is <u>kept</u> for.",
          "kept",
          ["maintained", "detained", "withheld", "postponed"], "A",
          "The sentence asks what the flock exists to produce — eggs or chicks — so the word "
          "carries the sense of keeping livestock. The sense of detaining would describe "
          "confining the birds, which is not what the contrast between eggs and chicks is "
          "about."),

 wic("W12",
     "A peregrine hunts in the open, climbs above its quarry and falls on it, and it needs a "
     "long sky to do so. A goshawk hunts the other way. Its wings are short and broad and "
     "its tail long, and it flies between trunks and through gaps at head height, changing "
     "line in its own length. The two birds are not better and worse but shaped for terrain "
     "that is _____",
     ["different.", "restricted.", "wooded.", "shifting."], "A",
     "The closing sentence explicitly refuses a ranking and the passage has just set open "
     "sky against woodland, so what distinguishes the birds is the kind of country each "
     "suits. Calling the terrain wooded describes only one of the two birds."),

 wic("W13",
     "Every July boats work up the Thames and lift the broods of swans out of the water "
     "one family at a time. The birds are weighed, checked for injury, marked and put back "
     "within minutes. What began as a count of who owned which bird now produces a run of "
     "figures on the health of the population going back further than any survey designed "
     "for the purpose. Swan upping has outlived its original object and become a _____",
     ["record.", "ceremony.", "levy.", "rehearsal."], "A",
     "The passage contrasts the old purpose of establishing ownership with a long run of "
     "figures on the birds' health, so what the practice now supplies is data over time. "
     "Calling it a ceremony would describe its form rather than the run of figures the "
     "sentence is about."),

 wic("W14",
     "A monastery rarely built one fishpond. It built three or four at different levels "
     "down a small valley, joined by short channels, so that fish could be moved from the "
     "spawning water to the growing water and finally to a small pond by the kitchen from "
     "which they could be taken as needed. Water let out of one filled the next. The "
     "arrangement made a supply of fresh fish available in winter that a single pond could "
     "never have kept _____",
     ["ready.", "cheap.", "hidden.", "cold."], "A",
     "The chain is described as ending in a pond by the kitchen from which fish could be "
     "taken as required, so what the arrangement secures is fish on hand when wanted. Price "
     "is not mentioned anywhere in the passage."),

 wic_mean("W15",
          "Laying is triggered by lengthening days, not by warmth or by feed, and a flock left "
          "to the natural year stops in autumn and starts again in spring. Lighting a house to "
          "hold the day at fourteen hours removes the autumn signal, and the birds go on "
          "laying. The <u>practice</u> keeps eggs on the market in the months when a flock out "
          "of doors would supply none.",
          "practice",
          ["procedure", "rehearsal", "custom", "profession"], "A",
          "The word points back to the specific technique just described, holding the day at "
          "fourteen hours, so it names a method that is carried out. The sense of a custom "
          "would make the lighting a habit the trade had fallen into, where the passage "
          "presents it as a deliberate method with a stated effect."),

 # --------------------------------------------- Text Structure and Purpose (6)
 tsp("T1",
     "A dovecote of the twelfth century might hold a thousand nest holes, and a thousand "
     "pairs of pigeons feed themselves. <u>The birds took their grain from the fields "
     "around, which in practice meant the fields of the tenants rather than those of the "
     "lord who owned the cote.</u> The right to build one was therefore restricted, and "
     "disputes about it fill manorial records. Meat that cost its owner nothing to raise "
     "cost somebody, and the law spent four centuries deciding who.",
     ["It identifies the cost that the rest of the text shows falling on people other than "
      "the owner.",
      "It explains how the nest holes inside a dovecote were arranged.",
      "It establishes the century in which the first dovecotes were built.",
      "It contrasts the diet of pigeons with the diet of other farm animals."], "A",
     "The underlined sentence says whose grain the birds actually ate, and the two "
     "sentences after it turn that fact into a legal argument about who bore the cost. The "
     "date appears in the opening sentence rather than in the underlined one."),

 tsp("T2",
     "A young hawk taken from the nest before it can fly grows up knowing nothing else and "
     "is easy to handle, but it may never hunt with much conviction. <u>A haggard, trapped "
     "as a full adult that has already fed itself through a winter, arrives with every skill "
     "the falconer cannot teach and none of the tolerance he needs.</u> Most falconers have "
     "preferred the bird taken in its first autumn, after it has hunted but before its "
     "habits have set.",
     ["It states the second of two extremes between which the text's preferred option sits.",
      "It explains how an adult hawk is trapped.",
      "It gives the reason a nestling is easier to handle than an adult.",
      "It introduces a disagreement among falconers about which bird is best."], "A",
     "The passage sets the nestling's tameness against the adult's skill and then endorses "
     "a bird taken between the two, so the underlined sentence supplies the far end of that "
     "range. How the adult is trapped is mentioned only in passing and is not what the "
     "sentence is doing."),

 tsp_purpose("T3",
             "A fyke is a line of hoops, largest at the mouth and smallest at the tail, with "
             "netting stretched over them and two or three internal funnels along the length. "
             "A fish that swims through a funnel finds the opening behind it much harder to "
             "locate from the wide side than it was from the narrow. Nothing in the net holds "
             "the fish; each funnel simply makes going forward easier than going back, and "
             "three of them in series make return unlikely.",
             ["To explain how a net catches fish without confining them by force.",
              "To argue that fyke nets should be used in place of other traps.",
              "To describe the materials from which a fyke net is made.",
              "To trace the history of the fyke net from its earliest use."], "A",
             "The text describes the funnels and then states that nothing holds the fish, so "
             "its object is to show how the trap works by making one direction easier than the "
             "other. It never recommends the net over any alternative."),

 tsp("T4",
     "Break a fresh egg onto a flat plate and the thick white stands up around the yolk; "
     "break a stale one and it spreads. <u>In 1937 Raymond Haugh turned that difference "
     "into a number by measuring the height of the thick white with a micrometer and "
     "correcting it for the weight of the egg.</u> The correction matters because a large "
     "egg spreads further than a small one of the same freshness. Graders have used the "
     "figure ever since.",
     ["It describes the step that converted a visible difference into a measurement.",
      "It explains why a large egg spreads further than a small one.",
      "It gives the reason graders prefer fresh eggs to stale ones.",
      "It reports a disagreement about how freshness should be judged."], "A",
     "The sentence before it describes what the eye can see and the underlined sentence "
     "supplies the micrometer and the correction that produce a figure, which the last "
     "sentence says is still used. The explanation of why large eggs spread further comes "
     "in the sentence after the underlined one."),

 tsp_purpose("T5",
             "Ducks on open water will not swim towards a person, but they will follow a fox. "
             "A small reddish dog is therefore sent out from behind one screen and in behind "
             "the next, showing itself briefly in each gap along the pipe. The birds come after "
             "it, mobbing as they go, and each appearance draws them further up the curve. The "
             "decoyman never shows himself until the birds are past the point at which they "
             "could turn.",
             ["To explain how a dog is used to turn a defensive reaction into a means of "
              "leading birds up a pipe.",
              "To argue that dogs are more effective than decoy ducks at a pond.",
              "To describe the breeds of dog historically used at decoy ponds.",
              "To warn that ducks are difficult to approach on open water."], "A",
             "The passage explains that the birds mob what they take for a fox and that each "
             "appearance draws them further along, so its purpose is to show how the reaction is "
             "put to use. No comparison with decoy ducks is made anywhere."),

 tsp("T6",
     "A pond dug in permeable ground empties as fast as it fills. <u>The remedy is to spread "
     "clay over the bed in thin layers and work each one under foot or under the hooves of "
     "cattle until the particles lie flat against one another and no channel is left through "
     "the thickness.</u> Cattle were often driven round a new pond for this reason alone. "
     "Puddling costs nothing but labour and is why ponds survive on gravel where no natural "
     "basin exists.",
     ["It sets out the process whose effect and cost the rest of the text goes on to state.",
      "It explains why cattle were kept near ponds in the first place.",
      "It identifies the kind of ground in which a pond will not hold water.",
      "It compares puddled clay with modern pond liners."], "A",
     "The underlined sentence describes the layering and treading, and the sentences after "
     "it give the reason cattle were used and what the technique costs and achieves. The "
     "permeable ground is named in the opening sentence, not the underlined one."),

 # ------------------------------------------ Central Ideas and Details (6)
 cid("C1",
     "The red junglefowl of southern Asia is the ancestor of every domestic chicken, but the "
     "date at which the two parted has proved hard to fix. Bones alone are unreliable: a "
     "junglefowl and an early domestic bird are nearly identical in the ground, and chicken "
     "bones travel downward through soft deposits into layers far older than themselves. "
     "Claims of very early domestication have repeatedly collapsed when the bones "
     "responsible were dated directly rather than by the layer they were found in.",
     ["Dating the domestication of the chicken has been difficult because the bones "
      "themselves are ambiguous and can move between layers.",
      "The red junglefowl is no longer thought to be the ancestor of the domestic chicken.",
      "Direct dating of bones has confirmed that chickens were domesticated very early.",
      "Domestic chickens and junglefowl can be told apart easily from their bones."], "A",
     "The passage gives two reasons the date is hard to fix — the bones look alike and they "
     "shift downward — and reports that early claims failed when the bones were dated "
     "directly. The option saying direct dating confirmed early domestication reverses the "
     "outcome the last sentence describes."),

 cid_detail("C2",
            "A message sent by pigeon travels in a light tube on the bird's leg, and its weight "
            "sets the limit on what can be sent. Ordinary paper was abandoned early. During the "
            "siege of Paris in 1870 despatches were photographed down to a film a few "
            "centimetres square, so that a single bird could carry many thousands of messages "
            "at once, and the film was projected and copied out at the far end.",
            "According to the text, what problem did photographing the despatches solve?",
            ["The weight a bird could carry limited how much could be sent.",
             "Pigeons released from Paris were unable to find their way home.",
             "Written messages could be read by anyone who intercepted the bird.",
             "Paper despatches were damaged by rain during the flight."], "A",
            "The text states that the weight of the tube sets the limit on what can be sent and "
            "then describes reduction to film as the way many thousands of messages were carried "
            "at once. Interception is never mentioned, so secrecy is not the problem being "
            "solved."),

 cid("C3",
     "Elvers arriving from the sea reach a weir and stop. They are the length of a match and "
     "cannot leap, but they climb readily on any wet rough surface, and a smooth concrete "
     "apron defeats them absolutely. An elver pass is therefore not a ladder of pools but a "
     "sloping trough lined with bristles kept damp by a trickle, which offers the one thing "
     "the weir has taken away. The obstacle is not the height of the weir but the "
     "smoothness of it.",
     ["Elvers are stopped by weirs because the surfaces are smooth rather than because "
      "they are high, so passes give them something to climb.",
      "Elver passes are built as a series of pools that allow the fish to leap in stages.",
      "Elvers are strong swimmers that can pass most weirs without assistance.",
      "Weirs have little effect on elvers compared with their effect on larger fish."], "A",
     "The passage says the fish climb wet rough surfaces but are defeated by smooth "
     "concrete, and describes a bristle trough as the remedy, ending by naming smoothness "
     "as the obstacle. The option describing a ladder of pools is what the passage says an "
     "elver pass is not."),

 cid_detail("C4",
            "The Royal Mews at Charing Cross was not a stable. It was where the king's hawks "
            "were kept while they moulted, and the word itself is from the French for the "
            "change of feather. The building was given over to horses only in the sixteenth "
            "century, after a fire, and the name went with the site rather than with its "
            "function. Every London mews now used as a garage or a house takes its name from "
            "birds that left the place four hundred years ago.",
            "According to the text, why is the word &ldquo;mews&rdquo; now attached to buildings "
            "that house vehicles?",
            ["The name stayed with a site whose use changed from housing hawks to housing "
             "horses.",
             "The word has always meant a building in which animals of any kind are kept.",
             "Hawks and horses were kept together in the same buildings for centuries.",
             "The word was borrowed a second time from French with its modern sense."], "A",
            "The passage says the building was given over to horses after a fire and that the "
            "name went with the site rather than the function. The claim that the word always "
            "meant any animal housing contradicts the stated derivation from the change of "
            "feather."),

 cid("C5",
     "Tench were long called doctor fish, on the belief that sick fish rubbed against their "
     "slime and were cured, and the belief survived into print for three centuries. No "
     "experiment has ever supported it. What tench do have is a tolerance of water so low "
     "in oxygen that carp go to the surface and pike die, which is why they were stocked in "
     "the muddiest ponds. The reputation appears to record where the fish was found "
     "rather than anything it did.",
     ["The tench's healing reputation is unsupported, and probably arose from its ability "
      "to live in water where other fish could not.",
      "Tench secrete a slime that has been shown to heal injuries in other fish.",
      "Tench were stocked in muddy ponds because they were believed to cure other fish.",
      "The belief that tench heal other fish disappeared once it was tested."], "A",
     "The passage denies experimental support, states the real trait as tolerance of low "
     "oxygen, and closes by saying the reputation records where the fish was found. The "
     "option about the belief disappearing is contradicted by the statement that it "
     "survived in print for three centuries."),

 cid_detail("C6",
            "A hen laying daily puts more calcium into shells in a year than is present in her "
            "whole skeleton, and she cannot eat it fast enough overnight, when the shell is "
            "actually formed. Before she comes into lay she builds a second kind of bone inside "
            "the marrow cavities of her long bones, loose and easily dissolved. That store is "
            "drawn down each night and rebuilt each day from the feed, so the skeleton is not "
            "the thing being spent.",
            "According to the text, what is the function of the bone formed in the marrow "
            "cavities?",
            ["It is a store of calcium that is emptied overnight and refilled during the day.",
             "It strengthens the long bones against the strain of daily laying.",
             "It replaces the calcium that the hen is unable to absorb from her feed.",
             "It forms the innermost layer of the shell before the egg is laid."], "A",
            "The passage says the loose bone is drawn down each night, when the shell is made, "
            "and rebuilt each day from the feed. Strengthening the bones is the opposite of "
            "what a store that is repeatedly emptied would do."),

 # ----------------------------------------------- Command of Evidence (9)
 coe_quote("E1",
           "In 1889 a wildfowler kept a game book on a stretch of estuary saltings. The "
           "historian Ines Balcombe argues that the book was written to record the "
           "conditions under which shooting was possible, not the size of the bag, and that "
           "its author regarded a blank day as worth as much to the record as a full one.",
           "Which quotation from the game book most effectively illustrates Balcombe's claim?",
           ["&ldquo;Nothing moved and nothing was fired at; wind south and soft, the birds "
            "lying out on the tide all day, which is the whole of the entry and the whole of "
            "the lesson.&rdquo;",
            "&ldquo;Eleven wigeon and a brace of teal, the best morning since the frost "
            "set in.&rdquo;",
            "&ldquo;The punt was recaulked at Michaelmas and the gun sent to Colchester to "
            "be rebreeched.&rdquo;",
            "&ldquo;My father shot over these same saltings for forty years before "
            "me.&rdquo;"], "A",
           "The quotation records a day on which nothing was shot, states the weather and the "
           "birds' behaviour, and insists that the empty entry is itself the point, which is "
           "exactly the practice the claim describes. The quotation listing eleven wigeon and "
           "two teal reports a bag, which is the kind of entry the claim says the book was "
           "not for."),

 coe_quote("E2",
           "A falconry treatise of about 1610 survives in a single manuscript. The scholar "
           "Ovidio Tamm argues that its author's distinctive position was that a hawk cannot "
           "be compelled at all, and that everything the falconer does is a matter of "
           "arranging conditions under which the bird chooses to do what is wanted.",
           "Which quotation from the treatise most effectively illustrates Tamm's claim?",
           ["&ldquo;Thou canst not make her come; thou canst only make the fist the place "
            "she would soonest be, and then she comes of her own reckoning.&rdquo;",
            "&ldquo;The mews should stand to the south, and be swept upon the Monday of "
            "every week.&rdquo;",
            "&ldquo;Her jesses shall be of doeskin, cut the length of a man's hand and no "
            "longer.&rdquo;",
            "&ldquo;I have kept goshawks these thirty years, and gerfalcons but "
            "twice.&rdquo;"], "A",
           "The quotation denies that the bird can be made to come and describes the "
           "falconer's work as making the fist the place she most wants to be, which is the "
           "arranging of conditions the claim identifies. The passage about the length of the "
           "jesses is a specification for equipment and says nothing about compulsion or "
           "choice."),

 coe_quote("E3",
           "The accounts of a Norfolk manor for 1465 record the dovecote among the "
           "buildings. The historian Priya Anandan argues that the accounts treat the "
           "dovecote as a source of manure first and of meat only second, reversing the "
           "priority usually assumed for such buildings.",
           "Which quotation from the accounts most effectively illustrates Anandan's claim?",
           ["&ldquo;Item, for the carriage of eleven loads from under the cote to the "
            "close, 3s. 8d.; and the squabs of that season, 2s. 1d.&rdquo;",
            "&ldquo;Item, for a new door to the cote, with the ironwork, 1s. 4d.&rdquo;",
            "&ldquo;Item, the cote standeth on eight posts and is thatched with "
            "reed.&rdquo;",
            "&ldquo;Item, the lord's licence for the said cote, granted in the eighth "
            "year.&rdquo;"], "A",
           "The quotation prices the carting of the dung well above the squabs of the same "
           "season and lists it first, which is precisely the reversed priority the claim "
           "asserts. The entry for a new door is an expense on the building and gives no "
           "comparison between the two products."),

 coe_find("E4",
          "Decoy ponds took most of their birds between November and February. One "
          "explanation is that hard weather drives wildfowl inland from frozen coasts, so "
          "the ponds simply had more birds within reach. A second is that the decoyman's "
          "method works best on hungry birds, which follow the dog more readily, so it is "
          "the birds' condition rather than their number that matters.",
          "Which finding, if true, would most directly support the second explanation?",
          ["In seasons when bird numbers at the ponds were unchanged, catches still rose "
           "sharply during periods of frost.",
           "Catches at coastal ponds were consistently higher than catches at inland ponds.",
           "The number of wildfowl counted on the ponds was highest in the coldest months.",
           "Decoymen worked longer hours in winter than at any other time of year."], "A",
          "The second explanation says condition rather than abundance is doing the work, so "
          "a rise in catches during frost while numbers stay level separates the two causes. "
          "The finding that counts peaked in the coldest months is what the first explanation "
          "predicts and does not distinguish them."),

 coe_find("E5",
          "A bristle pass was fitted to a weir on a small river in an attempt to let elvers "
          "reach the water above it. Counts taken above the weir rose in the two years after "
          "the pass was installed. The engineers who fitted it claim the rise shows the pass "
          "is working; a fisheries scientist replies that elver numbers rose that year in "
          "rivers all along the coast, whether or not anything had been built.",
          "Which finding, if true, would most directly support the engineers' claim?",
          ["Numbers above the weir rose by far more than numbers above unaltered weirs on "
           "neighbouring rivers over the same two years.",
           "Numbers below the weir also rose over the two years in question.",
           "Elver numbers along the whole coast were higher in those two years than in the "
           "preceding decade.",
           "The pass was inspected each month and was found to be undamaged."], "A",
          "The scientist's objection is that a coast-wide rise explains the increase without "
          "the pass, so the engineers need a rise at their weir larger than the one seen "
          "where nothing was built. A finding that the whole coast rose is the objection "
          "itself rather than an answer to it."),

 coe_find("E6",
          "Shells laid by a flock grow thinner as the birds age, and the eggs crack more "
          "often in handling. One account holds that older hens absorb calcium less "
          "efficiently. Another holds that the shell gland deposits roughly the same amount "
          "of material at any age, but that the egg itself grows larger as the hen ages, so "
          "the same shell is stretched over a bigger area.",
          "Which finding, if true, would most directly support the second account?",
          ["The total mass of shell material per egg was found to be almost unchanged from "
           "the first year of lay to the third, while egg weight rose steadily.",
           "Older hens were found to crack more eggs during handling than younger hens.",
           "Adding calcium to the feed of older hens did not restore shell thickness to "
           "the level seen in young birds.",
           "Shell thickness was found to fall more slowly in flocks kept in cooler "
           "houses."], "A",
          "The second account predicts a constant quantity of shell spread over a growing "
          "egg, so unchanged shell mass alongside rising egg weight is exactly its signature. "
          "The finding that older hens crack more eggs restates the phenomenon both accounts "
          "were proposed to explain."),

 coe_find("E7",
          "A research flock was held under four different day lengths, all other conditions "
          "being equal, and the eggs laid per hen per week were recorded over the same "
          "eight-week period in each house."
          + table(["Day length (hours)", "Eggs per hen per week"],
                  [["10", "2.6"], ["12", "3.9"], ["14", "5.4"], ["16", "5.6"]])
          + "A student concludes that lengthening the day raises the rate of lay, but that "
            "the gain becomes very small once the day is long enough.",
          "Which choice best describes data from the table that support the student's "
          "conclusion?",
          ["The rate rises by 2.8 eggs per hen per week between the 10-hour and 14-hour "
           "houses but by only 0.2 between the 14-hour and 16-hour houses.",
           "The rate rises steadily by about the same amount for each two-hour increase in "
           "day length.",
           "The 16-hour house recorded the highest rate of lay of the four.",
           "The 10-hour house recorded fewer than three eggs per hen per week."], "A",
          "The conclusion has two parts — a rise and then a levelling off — and only the "
          "option contrasting the large gain up to fourteen hours with the very small gain "
          "beyond it addresses both. Noting that the longest day gave the highest rate "
          "supports the rise but says nothing about the gain becoming small."),

 coe_find("E8",
          "Elvers were counted at the mouth of one river over four seasons, using the same "
          "trap in the same weeks of each year."
          + table(["Season", "Elvers counted (thousands)"],
                  [["2016", "148"], ["2017", "96"], ["2018", "212"], ["2019", "104"]])
          + "A researcher argues that a single season's count at this site is a poor guide "
            "to the following season's.",
          "Which choice best describes data from the table that support the researcher's "
          "argument?",
          ["The count roughly doubled from 2017 to 2018 and then fell by more than half "
           "from 2018 to 2019.",
           "The count in 2018 was the highest of the four seasons recorded.",
           "The counts in 2017 and 2019 were within about ten thousand of each other.",
           "The average of the four counts is about 140 thousand elvers."], "A",
          "The argument is that one year does not predict the next, and only the option "
          "tracking a doubling immediately followed by a fall of more than half shows "
          "consecutive years moving sharply in opposite directions. Identifying 2018 as the "
          "highest season describes one year alone."),

 coe_find("E9",
          "The keeper of a decoy pond recorded the birds taken in each of three winters, "
          "by species."
          + table(["Species", "2018-19", "2019-20", "2020-21"],
                  [["Teal", "410", "372", "455"], ["Wigeon", "268", "301", "244"],
                   ["Mallard", "96", "88", "104"], ["Pintail", "31", "14", "22"]])
          + "A student claims that the pond's catch was dominated by two species "
            "throughout the period.",
          "Which choice best describes data from the table that support the student's claim?",
          ["In each of the three winters, teal and wigeon together account for more than "
           "eighty per cent of the birds taken.",
           "Teal were the most numerous species taken in each of the three winters.",
           "Pintail were the least numerous species taken in each of the three winters.",
           "The total number of birds taken was greatest in the winter of 2020-21."], "A",
          "The claim is about two species dominating, so it needs their combined share, "
          "which the option giving teal and wigeon together as more than four-fifths of the "
          "catch supplies for every winter. Naming teal as the most numerous species "
          "concerns one species and gives no share of the total."),

 # -------------------------------------------------------- Inferences (6)
 inf("I1",
     "Pigeons carried in a closed basket to a place they have never seen, released, and "
     "watched from the ground set off in a consistent direction within a minute or two, "
     "long before any landmark could be recognised. Birds carried by a route deliberately "
     "made circuitous, with the basket rotated throughout, do the same. It follows that the "
     "initial choice of direction cannot depend on _____",
     ["the bird's having kept track of the outward journey.",
      "the bird's ability to see the ground below it.",
      "the distance at which the release takes place.",
      "the bird's having been released at that site before."], "A",
     "The birds were carried by a deliberately confusing route in a rotating basket and "
     "still chose a consistent direction at once, which rules out any method that relies on "
     "following the outward path. Seeing the ground is not ruled out by anything in the "
     "passage, since the birds are watched from the ground after release."),

 inf("I2",
     "The shell of an egg is porous, and from the day it is laid the contents lose water "
     "vapour through it while air enters to take the place of what has gone. The pocket of "
     "air at the blunt end therefore grows steadily, and the egg as a whole becomes less "
     "dense. An egg dropped into a bowl of water will float when it is old enough, so the "
     "test works because floating depends on _____",
     ["how much of the shell's volume the air pocket has come to occupy.",
      "how thick the shell of the egg has become over time.",
      "whether the egg was washed before it was stored.",
      "the temperature at which the egg has been kept."], "A",
     "The passage attributes the loss of density entirely to the growth of the air pocket "
     "as water vapour leaves, so what determines floating is how large that pocket has "
     "grown. Shell thickness is never said to change after laying."),

 inf("I3",
     "A hawk that is carrying too much fat has no reason to come back to the fist, and one "
     "flown too light is weak and will not fly hard. The falconer therefore weighs the bird "
     "on the same scales at the same hour every day and adjusts what it is given by a few "
     "grams at a time. The daily weighing matters because the range within which a hawk "
     "will fly well is _____",
     ["narrow enough that small changes carry the bird out of it.",
      "different for every species of hawk that is flown.",
      "impossible to establish without flying the bird first.",
      "wider in winter than it is in summer."], "A",
     "The passage describes adjustments of a few grams made daily and sets the fat bird "
     "against the weak one, which only makes sense if the usable range is small. The claim "
     "that the range differs between species may be true but is not what the daily weighing "
     "of one bird implies."),

 inf("I4",
     "The wooden frames that carried eel bucks stood in the gaps of a Thames weir for "
     "centuries, and photographs from the 1890s show them still in place. The fishery "
     "itself had by then been unprofitable for two generations, and no bucks were being "
     "set. The frames were nevertheless maintained, because under the terms by which the "
     "gap was held the structure had to be kept up. The frames survived so long because "
     "their upkeep had become _____",
     ["a condition of holding the site rather than a cost of catching fish.",
      "cheaper than the fishery had ever been at its most profitable.",
      "the responsibility of the river authority rather than the fisherman.",
      "a means of measuring the flow of water through the weir."], "A",
     "The passage says no bucks were being set yet the frames were maintained because the "
     "terms of holding the gap required it, which detaches the upkeep from the fishing. "
     "Nothing in the text transfers the responsibility to a river authority."),

 inf("I5",
     "In a dovecote built against a rat-infested farmyard the lowest tier of nest holes "
     "begins a full metre above the floor, and the wall below that line is rendered smooth "
     "and given a projecting course of stone. Cotes standing free on a stone staddle have "
     "holes running all the way down. The difference suggests that the empty band of wall "
     "was left _____",
     ["to deny climbing animals a route to the nests.",
      "to allow the keeper to sweep the floor more easily.",
      "to strengthen the wall at the point of greatest load.",
      "to leave room for the potence to swing."], "A",
     "The band is smooth-rendered and topped by a projecting course in the cote next to a "
     "rat-infested yard, while free-standing cotes on a staddle have no such band, which "
     "points to keeping animals off the nests. Sweeping would not require the rendering or "
     "the projecting course."),

 inf("I6",
     "A carp's scales grow with the fish, and the bone laid down in summer is spaced widely "
     "while the little laid down in winter is packed close, so the scale carries alternating "
     "bands. A fish from a heated pond that never cools shows the summer spacing throughout. "
     "Reading a carp's age from its scales therefore depends on the fish having lived where "
     "growth was _____",
     ["interrupted by a season each year.",
      "faster than it would have been in a river.",
      "recorded by the keeper from the time of stocking.",
      "limited by the food available in the pond."], "A",
     "The bands exist because winter growth differs from summer growth, and the heated-pond "
     "fish shows no bands at all, so the method needs an annual check to growth. Food supply "
     "may affect how fast the fish grows but the passage ties the bands specifically to the "
     "cold season."),

 # -------------------------------------------------------- Boundaries (12)
 bnd("B1",
     "Geese were walked to market over distances of a hundred miles and more, and the roads "
     "wore their feet raw. Drovers took the flock through a shallow trough of tar and then "
     "through a bed of sand, which set into a rough shoe that lasted several days. The "
     "practice sounds cruel and was in fact protective, since a goose that went lame on the "
     "_____ was a total loss.",
     ["road", "road,", "road;", "road:"], "A",
     "The words before the blank are the subject of the verb that follows it, and nothing "
     "may stand between a subject and its verb, so the blank takes no mark at all. A "
     "semicolon would require a complete statement on each side of it, and the words after "
     "the blank cannot stand alone as a sentence."),

 bnd("B2",
     "A flight feather is not a solid sheet. Hundreds of barbs run out from the shaft, and "
     "from each barb run smaller barbules carrying hooks that catch on the barbules of the "
     "neighbouring barb. Drag a finger the wrong way and the vane splits open; the bird "
     "draws the feather through its bill and the split _____ the hooks find their "
     "neighbours again and the surface is whole.",
     ["closes:", "closes,", "closes", "closes; and"], "A",
     "What follows the blank explains what the closing consists of, and a colon is the mark "
     "that introduces an explanation of the statement before it. The comma alone would "
     "splice two complete statements together."),

 bnd("B3",
     "An egg left undisturbed for a day develops adhesions between the membrane and the "
     "growing embryo. A hen turns her clutch with her bill several times an hour, and a "
     "machine must do the same. Every commercial incubator therefore carries a tray that "
     "tilts through ninety degrees on a slow _____ it is the one moving part the machine "
     "cannot do without.",
     ["cycle;", "cycle,", "cycle", "cycle: and"], "A",
     "Two complete statements meet at the blank with no conjunction between them, which is "
     "what a semicolon is for. The comma alone produces a splice, and a colon does not take "
     "a conjunction after it."),

 bnd("B4",
     "A gunning punt sits so low that a few centimetres of chop will come over the "
     "foredeck. The gunner lies on his back with his head towards the stern and works the "
     "boat with a pair of short hand paddles. Every fitting stands below the level of the "
     "gunwale, and the gun itself is bedded into the hull rather than mounted on _____",
     ["it.", "it", "it,", "it;"], "A",
     "The sentence ends at the blank and needs the full stop that closes it. A semicolon or "
     "a comma would leave the sentence without an end and with nothing after the mark."),

 bnd("B5",
     "Before refrigeration, eggs for winter were laid down in a solution of sodium silicate "
     "in a crock in the cellar. The liquid filled the pores of the shell and stopped the "
     "loss of water and the entry of bacteria alike. Eggs preserved this way keep for eight "
     "months and are perfectly good for baking, though the shells crack in boiling unless "
     "they are pricked _____",
     ["first.", "first", "first;", "first,"], "A",
     "The sentence is complete at the blank and requires a full stop. A semicolon would "
     "call for a second complete statement after it, and there is none."),

 bnd("B6",
     "A pigeon race is won on speed, not on arrival, and the birds are released together "
     "from one point but fly home to lofts scattered across a county. Each fancier's clock "
     "is sealed before the race by an official of the _____ this is what makes the recorded "
     "times comparable at all.",
     ["club;", "club,", "club", "club: which"], "A",
     "The blank falls between two complete statements with no conjunction, so a semicolon "
     "is required. The comma alone splices them, and the version adding a relative pronoun "
     "after a colon creates a fragment."),

 bnd("B7",
     "Hawks travelling to the field cannot be carried on the fist all at once. A cadge is a "
     "rectangular frame with padded rails, slung from the shoulders of the man inside it, "
     "and four or five hooded birds ride on the rails facing outward. The man who carried "
     "it was the _____ the word survives in the modern sense of one who begs a ride.",
     ["cadger, and", "cadger and", "cadger; and", "cadger and,"], "A",
     "Two complete statements are joined by a coordinating conjunction, and the comma "
     "before that conjunction is the standard mark. Omitting the comma joins the statements "
     "with nothing at all."),

 bnd("B8",
     "The entrance to a loft is not a plain hole. A row of light wires hangs across it, "
     "each one hinged along the top so that it swings inward under the head of a bird "
     "pushing in and falls back into place behind. A returning racer drives through the "
     "_____ dropping onto the board inside and finding no way out again.",
     ["wires,", "wires;", "wires", "wires:"], "A",
     "What follows the blank is a participial phrase describing how the bird arrives, not "
     "a complete statement, so a comma is the mark that attaches it. A semicolon would "
     "require a full statement on each side of it."),

 bnd("B9",
     "A kiddle is a fixed fence of stakes and netting run out into a tidal channel to catch "
     "fish on the ebb. Because a line of them across an estuary blocks navigation as "
     "effectively as it blocks fish, they were a standing grievance among boatmen. Magna "
     "Carta devotes a clause to _____ all kiddles were to be removed from the Thames and "
     "the Medway.",
     ["them:", "them,", "them", "them; and"], "A",
     "The words after the blank state what the clause actually says, and a colon is the "
     "mark that introduces that statement. A comma alone would splice two complete "
     "statements together."),

 bnd("B10",
     "Eider ducks line their nests with down plucked from the female's own breast, and the "
     "down is gathered by hand after the ducklings have left. A nest yields perhaps "
     "seventeen grams. The colonies on the Icelandic coast are protected and encouraged "
     "for the sake of the harvest, so the birds are in effect farmed without ever being "
     "_____",
     ["confined.", "confined", "confined;", "confined,"], "A",
     "The sentence finishes at the blank and needs a full stop. A semicolon would demand "
     "another complete statement, and none follows."),

 bnd("B11",
     "The first eggs a pullet lays are small, often under forty grams, and they are graded "
     "and priced separately. The size climbs over the following two months and then "
     "steadies. A packing station that sells to bakers welcomes these early eggs, because "
     "the yolk is a larger share of a small egg than of a large _____",
     ["one.", "one", "one;", "one,"], "A",
     "The sentence is complete at the blank and takes a full stop. A semicolon or a comma "
     "would leave the sentence hanging with nothing after the mark."),

 bnd("B12",
     "Carp are netted from a stew pond at Michaelmas, when the water is cold enough that "
     "the fish handle well and the year's growth is finished. The pond is drawn down over "
     "several days so the fish collect in a deep sump at the _____ which is the only part "
     "of the bed still holding water. Only the largest are taken; the rest go back for "
     "another season.",
     ["outlet,", "outlet", "outlet;", "outlet:"], "A",
     "The words after the blank form a relative clause describing the sump, and a clause "
     "of that kind is attached to the noun it describes with a comma. A semicolon would "
     "require a complete statement after it, and a relative clause opening with "
     "&ldquo;which&rdquo; cannot stand alone."),

 # ------------------------------------------- Form, Structure, and Sense (9)
 fss("F1",
     "A dovecote of any size is inspected tier by tier, and the keeper works round the wall "
     "on the potence rather than moving a ladder. Each of the nest holes on the lower four "
     "tiers _____ checked for a sitting bird before the squabs of that round are taken.",
     ["is", "are", "were", "have been"], "A",
     "The subject is &ldquo;each&rdquo;, which is singular, and the words naming the holes "
     "sit in a phrase that cannot change the number of the subject. The plural forms agree "
     "with &ldquo;holes&rdquo; instead, which is not what the sentence is about."),

 fss("F2",
     "The falconer had a rule about the order of things. By the time a young hawk was first "
     "carried out to the field, it _____ already fed from the fist indoors for a fortnight "
     "and been walked through the yard among people twice a day.",
     ["had", "has", "will have", "would be having"], "A",
     "The sentence describes what was already finished at a point in the past, which calls "
     "for the past perfect. The present perfect would place the feeding in a period running "
     "up to now, and the whole passage is set in the past."),

 fss("F3",
     "Two men worked the pond, and the arrangement was strict about whose voice the dog "
     "answered. The birds followed the dog, and the dog answered only the _____ signals, "
     "which were given by hand from behind the screens.",
     ["decoyman's", "decoymans", "decoymans'", "decoyman"], "A",
     "One decoyman possesses the signals, so the singular possessive with an apostrophe "
     "before the s is required. The form with the apostrophe after the s would refer to "
     "signals belonging to more than one decoyman, and the passage names only one."),

 fss("F4",
     "The judging at a poultry show runs to a written standard, and a bird is placed "
     "against that standard rather than against the others on the bench. Neither the two "
     "stewards nor the breeder _____ permitted to speak to the judge while the class is "
     "being judged.",
     ["is", "are", "were", "have been"], "A",
     "With &ldquo;neither ... nor&rdquo; the verb agrees with whichever subject stands "
     "nearer to it, and the nearer subject here is the singular &ldquo;breeder&rdquo;. The "
     "plural forms agree with &ldquo;stewards&rdquo;, which is the further of the two "
     "subjects and does not govern the verb."),

 fss("F5",
     "Small bells are fitted so that a hawk lost in cover can be found by ear, and each "
     "bird carries a pair tuned a semitone apart. On the day of a large meet the sound "
     "carries across the whole field, and the _____ bells can be told from one another at "
     "fifty paces.",
     ["falconers'", "falconer's", "falconers", "falconers's"], "A",
     "The bells belong to more than one falconer, since the sentence describes a large "
     "meet, so the plural possessive takes the apostrophe after the s. The singular "
     "possessive would attribute every bell on the field to one person."),

 fss("F6",
     "The elver fishery on this river is licensed by weight, and the licences are reviewed "
     "against the run each spring. Numbers reaching the trap _____ by more than nine tenths "
     "since the first counts were made in the 1970s, and the quota has been cut four times.",
     ["have fallen", "fell", "falls", "had fallen"], "A",
     "The fall runs from a point in the past up to the present, which the present perfect "
     "expresses. The simple past would close the fall off in the past, and the sentence "
     "goes on to report a consequence that still stands."),

 fss("F7",
     "A laying flock is managed as a unit from the day the pullets arrive, and individual "
     "birds are not tracked. The flock _____ moved into the laying house at sixteen weeks "
     "and lit to a fourteen-hour day from the week after that.",
     ["is", "are", "have been", "were being"], "A",
     "&ldquo;Flock&rdquo; is treated as a single unit here, as the first sentence makes "
     "explicit by saying individual birds are not tracked, so the singular verb is "
     "required. The plural form would treat the birds as acting separately."),

 fss("F8",
     "Working the gun from a prone position is what makes the approach possible at all. "
     "_____ the gunner can bring the punt within range of birds that would lift at the "
     "sight of a man sitting upright.",
     ["Lying flat on his back and paddling with his hands,",
      "Lying flat on his back and paddling with his hands",
      "By lying flat on his back and paddling with his hands",
      "Lying flat on his back, and paddling with his hands"], "A",
     "The opening phrase describes the gunner, who must therefore be the subject that "
     "follows, and an introductory participial phrase is closed with a comma. The version "
     "with no comma runs the phrase into the subject it modifies."),

 fss("F9",
     "The grading line reports two figures at the end of every shift, and they are not "
     "interchangeable. The number of eggs rejected for cracks _____ risen this month, while "
     "the proportion rejected for stains has stayed where it was.",
     ["has", "have", "are", "were"], "A",
     "The subject is &ldquo;the number&rdquo;, which is singular however many eggs it "
     "counts, so the singular verb is needed. The plural forms agree with "
     "&ldquo;eggs&rdquo;, which sits inside a modifying phrase."),

 # ------------------------------------------------------- Transitions (9)
 trn("N1",
     "A newly laid egg carries a natural coating that seals its pores, and an unwashed egg "
     "will sit on a shelf for weeks. Washing removes that coating along with the dirt. "
     "_____ eggs washed at the packing station must be refrigerated from that moment until "
     "they are sold, and the cold chain may not be broken.",
     ["Consequently,", "Nevertheless,", "Similarly,", "For example,"], "A",
     "The removal of the seal stated in the second sentence is the reason the refrigeration "
     "in the third becomes necessary, so the transition marks a result. A contrast would "
     "require the refrigeration to cut against the washing, and it follows from it."),

 trn("N2",
     "The floor of a large dovecote accumulates a deep bed of droppings, and the nitrates "
     "in it were valuable for reasons that had nothing to do with farming. Saltpetre for "
     "gunpowder was extracted by leaching such material with water and wood ash. _____ "
     "commissioners held the right to enter a dovecote and dig its floor, whether or not "
     "the owner consented.",
     ["Accordingly,", "By contrast,", "Meanwhile,", "In particular,"], "A",
     "The value of the floor for gunpowder is what produced the right of entry, so the "
     "transition marks a consequence. A contrast would require the right of entry to cut "
     "against the value of the nitrates."),

 trn("N3",
     "A peregrine stooping at three hundred kilometres an hour meets air that would dry and "
     "abrade an unprotected eye within seconds. A third eyelid sweeps across the surface "
     "from the inner corner several times a second throughout the dive. _____ the membrane "
     "is largely transparent, so the bird keeps its quarry in sight the whole way down.",
     ["Crucially,", "Otherwise,", "In contrast,", "Afterwards,"], "A",
     "The sentence adds the property that makes the eyelid workable rather than merely "
     "protective, and marking it as the decisive point is what the passage needs. "
     "&ldquo;Otherwise&rdquo; would introduce what happens in the absence of the membrane, "
     "which is not what the sentence states."),

 trn("N4",
     "Of the several hundred decoy ponds once working in England, fewer than ten are still "
     "operated, and none of those takes birds for the table. The ponds themselves have "
     "proved too valuable to fill in: the pipes and screens that once led ducks to the net "
     "now lead them to a ringing station. _____ a technique developed to kill wildfowl "
     "supplies much of what is known about where they go.",
     ["Thus,", "Even so,", "Likewise,", "Previously,"], "A",
     "The last sentence states the outcome of the change described in the sentence before "
     "it, so the transition marks a conclusion drawn from what precedes. "
     "&ldquo;Even so&rdquo; would signal that the outcome runs against the preceding "
     "sentence, and it follows directly from it."),

 trn("N5",
     "A trap made of small mesh takes everything that enters it, including elvers and the "
     "fry of other species, most of which are dead before the net is lifted. Regulations "
     "therefore set a minimum mesh for eel traps on most rivers. _____ the rule is easier "
     "to write than to enforce, since a legal net can be fished with an illegal liner "
     "inside it.",
     ["However,", "Therefore,", "Similarly,", "In addition,"], "A",
     "The third sentence undercuts the regulation announced in the second by describing how "
     "it is evaded, so the transition marks a contrast. &ldquo;Therefore&rdquo; would "
     "present the difficulty as a result of the rule, which it is not."),

 trn("N6",
     "Ducklings and chicks can walk and feed within hours of hatching, and they follow the "
     "first large moving object they meet, which in the ordinary case is the parent. The "
     "attachment forms within a day and is not easily undone. _____ birds hatched in an "
     "incubator will follow a person, a box on wheels or a wooden decoy just as readily.",
     ["For this reason,", "Nonetheless,", "Earlier,", "By comparison,"], "A",
     "The behaviour described in the first two sentences is what makes the incubator-reared "
     "birds follow whatever they meet, so the transition marks a consequence. "
     "&ldquo;Nonetheless&rdquo; would present the following of a box as surprising given "
     "the preceding sentences, and it is exactly what they predict."),

 trn("N7",
     "Displaced pigeons find their way home from places they have never seen, and two "
     "explanations have been pursued for half a century. Birds fitted with small magnets "
     "are disoriented under overcast skies, which points to a magnetic sense. _____ birds "
     "whose sense of smell has been blocked are disoriented too, which points somewhere "
     "else entirely.",
     ["On the other hand,", "As a result,", "For instance,", "In short,"], "A",
     "The second finding points away from the magnetic explanation the first supports, so "
     "the transition marks the opposition between two lines of evidence. &ldquo;As a "
     "result&rdquo; would make the second finding follow from the first."),

 trn("N8",
     "Mute swans on open water in England belong to the Crown unless another right can be "
     "shown, a rule that dates from a time when the bird was a dish for a feast. The status "
     "has long ceased to have anything to do with food. _____ it has proved useful, because "
     "an owner exists who can be prosecuted when swans are harmed.",
     ["Nevertheless,", "Consequently,", "Similarly,", "In other words,"], "A",
     "The last sentence reports a benefit that persists despite the rule having lost its "
     "original purpose, so the transition marks a concession. &ldquo;Consequently&rdquo; "
     "would make the usefulness follow from the loss of purpose."),

 trn("N9",
     "The carp is not native to western Europe and was carried there deliberately, reaching "
     "England by the fifteenth century. It tolerates warm, still, low-oxygen water that "
     "would kill a trout, and it grows fast on food a pond produces without help. _____ it "
     "suited a system of small ponds attached to houses far better than any native fish, "
     "and it spread with that system rather than by its own movement.",
     ["As a result,", "Even so,", "Beforehand,", "Similarly,"], "A",
     "The tolerances listed in the second sentence are the reason the fish suited the pond "
     "system, so the transition marks a consequence. &ldquo;Even so&rdquo; would signal "
     "that its suitability runs against those tolerances."),

 # ----------------------------------------------- Rhetorical Synthesis (9)
 rsy("R1",
     ["Eggs must be held near 37&deg;C for the embryo to develop.",
      "Feathers are excellent insulators and would keep the sitting bird's heat away "
      "from the eggs.",
      "Before incubation begins, a sitting bird sheds the down from a patch on its "
      "underside.",
      "Blood vessels in the bare patch enlarge, and the skin's surface temperature "
      "rises by several degrees.",
      "The feathers regrow after the young have hatched."],
     "explain how the bare patch allows the sitting bird to warm its eggs.",
     ["Eggs must be held near 37&deg;C for the embryo to develop.",
      "The feathers on the patch regrow once the young have hatched.",
      "Shedding the down from a patch of the underside puts enlarged blood vessels and "
      "warmed skin directly against eggs that feathers would otherwise have insulated.",
      "Feathers are excellent insulators."], "C",
     "The goal asks how the patch does its work, and only the choice joining the shed down "
     "to the enlarged vessels, the warmed skin and the insulating effect that is thereby "
     "removed explains the mechanism. Stating the temperature an embryo needs gives the "
     "requirement without saying how the bird meets it."),

 rsy("R2",
     ["A hawk that has eaten its fill is described as &ldquo;fed up&rdquo; and will not "
      "fly.",
      "A bird held with the jesses under the falconer's thumb cannot leave the fist.",
      "&ldquo;Hoodwink&rdquo; originally meant to cover a hawk's eyes with the hood.",
      "All three phrases entered general English between 1500 and 1600.",
      "Few speakers who use them today are aware of their origin."],
     "illustrate the claim that ordinary English phrases can outlive the practice that "
     "produced them.",
     ["A hawk that has eaten its fill is described as &ldquo;fed up&rdquo;.",
      "Phrases such as &ldquo;fed up&rdquo; and &ldquo;hoodwink&rdquo; came from falconry "
      "in the sixteenth century and are still in general use, though few speakers now know "
      "where they came from.",
      "&ldquo;Hoodwink&rdquo; originally meant to cover a hawk's eyes.",
      "All three phrases entered general English between 1500 and 1600."], "B",
     "The claim has two halves — the phrases survive and the practice behind them does not — "
     "and only the choice pairing continued general use with speakers' ignorance of the "
     "origin states both. Giving the original meaning of a single phrase supplies half the "
     "claim without the survival."),

 rsy("R3",
     ["Wildfowl using the same flyway pass a given estuary within a few weeks each autumn.",
      "The date of the passage shifts by up to three weeks from year to year with the "
      "weather.",
      "A count made on a fixed calendar date may fall before or after the passage.",
      "Counts at one site are now made on five dates spread across six weeks.",
      "The highest of the five is taken as that season's figure for the site."],
     "explain why counts at the site are no longer made on a single fixed date.",
     ["Wildfowl using the same flyway pass a given estuary within a few weeks each autumn.",
      "Because the passage shifts by up to three weeks with the weather, a single fixed "
      "date can miss it altogether, so the site now counts on five dates across six weeks "
      "and takes the highest.",
      "Counts at one site are made on five dates spread across six weeks.",
      "The date of the passage shifts by up to three weeks from year to year."], "B",
     "The goal asks for the reason the practice changed, and only the choice linking the "
     "shifting date to the risk of missing the passage and then to the five-date method "
     "supplies it. Reporting that counts are made on five dates describes the new practice "
     "without giving the reason for it."),

 rsy("R4",
     ["Growing a new set of feathers requires a large amount of protein.",
      "A hen in full lay is already using most of the protein in her feed for egg white.",
      "Laying stops almost entirely while a hen is moulting.",
      "A moult lasts between six and twelve weeks.",
      "Flocks kept for eggs are often replaced rather than carried through a moult."],
     "explain why a hen stops laying while she is moulting.",
     ["A moult lasts between six and twelve weeks.",
      "Growing feathers and making egg white both draw on the protein in a hen's feed, and "
      "a moulting hen cannot supply both, so laying stops almost entirely until the new "
      "feathers are grown.",
      "Flocks kept for eggs are often replaced rather than carried through a moult.",
      "Laying stops almost entirely while a hen is moulting."], "B",
     "The goal asks for the cause, and only the choice identifying protein as the resource "
     "both processes compete for explains why one displaces the other. Stating that laying "
     "stops during the moult restates the fact to be explained."),

 rsy("R5",
     ["In some breeds the gene for barred feathers sits on the sex chromosome.",
      "A barred hen crossed with a plain cock gives barred sons and plain daughters.",
      "The difference shows as a pale spot on the head and is visible at hatching.",
      "Sorting chicks by sex at a day old otherwise requires long training.",
      "The cross was widely adopted by hatcheries from the 1930s."],
     "explain how the cross allows a hatchery to sort chicks without special training.",
     ["Sorting chicks by sex at a day old otherwise requires long training.",
      "In some breeds the gene for barred feathers sits on the sex chromosome.",
      "Crossing a barred hen with a plain cock gives barred sons and plain daughters, and "
      "the difference shows as a pale head spot at hatching, so the sexes can be told apart "
      "by eye.",
      "The cross was widely adopted by hatcheries from the 1930s."], "C",
     "The goal asks how the sorting is done, and only the choice giving the cross, the "
     "resulting difference between the sexes and its visibility at hatching accounts for "
     "it. Naming the chromosome the gene sits on gives the reason the cross works without "
     "describing the sorting."),

 rsy("R6",
     ["The English word &ldquo;decoy&rdquo; comes from the Dutch <em>eendenkooi</em>, a "
      "duck cage.",
      "The first ponds of this type in England were built in the 1660s by Dutch builders.",
      "The word at first named the pond, not the wooden birds set out on the water.",
      "The wooden birds were called &ldquo;stales&rdquo; in the seventeenth century.",
      "By 1800 &ldquo;decoy&rdquo; had come to mean the wooden birds as well."],
     "explain how the meaning of the word changed after it entered English.",
     ["The word came into English from the Dutch <em>eendenkooi</em>, a duck cage.",
      "The first ponds of this type in England were built in the 1660s by Dutch builders.",
      "Entering English as the name of the pond itself, the word had by 1800 spread to the "
      "wooden birds, which the seventeenth century had called stales.",
      "The wooden birds were called &ldquo;stales&rdquo; in the seventeenth century."], "C",
     "The goal is about a change of meaning over time, and only the choice tracking the word "
     "from the pond to the wooden birds and naming the older term for those birds describes "
     "the shift. Giving the Dutch source explains where the word came from, not how its "
     "sense moved."),

 rsy("R7",
     ["The rock dove nests on ledges on sea cliffs and in caves.",
      "It does not build in trees and does not need cover overhead.",
      "The ledges and window heads of masonry buildings present the same conditions.",
      "Feral pigeons in cities descend from domestic birds that themselves descend from "
      "rock doves.",
      "Cities support pigeon densities far higher than any natural cliff."],
     "explain why the rock dove's ancestry accounts for the pigeon's success in cities.",
     ["The rock dove nests on ledges on sea cliffs and in caves.",
      "Cities support pigeon densities far higher than any natural cliff.",
      "Because the rock dove nests on bare ledges rather than in trees, the ledges and "
      "window heads of masonry buildings offer its descendants exactly the conditions it "
      "already required.",
      "Feral pigeons descend from domestic birds that descend from rock doves."], "C",
     "The goal asks how the ancestry explains the success, and only the choice matching the "
     "cliff-ledge requirement to what masonry provides makes that connection. Stating that "
     "cities hold high densities reports the success without accounting for it."),

 rsy("R8",
     ["Meat was forbidden on about a third of the days of the medieval year.",
      "Fish was not, and demand for it was therefore steady and predictable.",
      "Sea fish could not be brought inland fresh before the railways.",
      "A pond stocked with carp and tench supplied fresh fish at any season.",
      "Most large monastic houses and many manors held at least one such pond."],
     "explain why fishponds were built at inland houses.",
     ["Meat was forbidden on about a third of the days of the medieval year.",
      "A steady demand for fish on the many meatless days could not be met inland with sea "
      "fish before the railways, so a stocked pond supplied fresh fish at any season.",
      "Most large monastic houses and many manors held at least one such pond.",
      "Sea fish could not be brought inland fresh before the railways."], "B",
     "The goal asks why the ponds were built, and only the choice joining the steady demand "
     "to the impossibility of supplying it from the sea explains the need a pond met. "
     "Reporting how many houses held a pond states how common they were, not why."),

 rsy("R9",
     ["Before the 1840s a breed of poultry had no written description.",
      "Exhibitors and judges disagreed constantly about what a breed should look like.",
      "The first published standards described each breed point by point.",
      "A judge now scores a bird against the written description rather than against the "
      "other birds present.",
      "Two judges working independently now reach much the same placings."],
     "explain how the written standards changed the way poultry are judged.",
     ["Before the 1840s a breed of poultry had no written description.",
      "Publishing a point-by-point description of each breed moved judging from comparison "
      "with the other birds on the bench to comparison with a fixed written account, and "
      "independent judges now reach much the same placings.",
      "Exhibitors and judges disagreed constantly about what a breed should look like.",
      "The first published standards described each breed point by point."], "B",
     "The goal asks what the standards changed, and only the choice contrasting judging "
     "against the other birds with judging against a fixed description, and noting the "
     "agreement that followed, states the change. Reporting that breeds once had no written "
     "description gives the situation before the change without describing it."),
]
