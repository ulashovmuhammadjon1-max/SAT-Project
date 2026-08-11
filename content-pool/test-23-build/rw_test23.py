#!/usr/bin/env python3
"""
Reading & Writing authored for Test 23.

All 81 items are original. The transcribed pools were spent by Test 8, and for
R&W authoring is in any case the safer route: a transcribed key has to be
re-derived by hand before it can be trusted (Test 5 shipped 6 wrong answers in
81 that way). Every item below carries a `why` recording the reasoning that
produced the key AND the reason the strongest distractor fails; that record is
the verification, so no key exists here without one.

Rationales name options by their CONTENT, never by letter, so balance_rw.py is
free to rotate every question when it evens out the key distribution.

Writing-domain choices are never bare punctuation. The real test repeats the
words on either side of the blank inside every option so a choice reads as the
resulting sentence, and every Boundaries item here is written that way from the
start.

TERRITORY (Test 23's, disjoint from its siblings'): canal locks and pounds,
barge haulage, aqueducts, dredging, towpaths, wharves and quays, canal toll
keeping. Sub-themes actually used: mitre gates, staircase locks, pounds and
summit water supply, back-pumping, stop gates, legging and tunnel tugs, bow
hauliers, fly boats, boat horses, ice boats, iron trough aqueducts, puddled
clay, spoil banks, weed cutting, turnover bridges, rope grooves, towpath law,
gauging by freeboard, canal arms into warehouses, toll classes, toll evasion,
compensation tolls, statutory rate ceilings, canal mania, navvies, restoration
versus habitat, and modern water freight.

Every candidate topic was screened against ../rw_authored_corpus.json (1,295
banked passages) by keyword BEFORE any passage was drafted; screen_topics.py in
this directory is that check, and the finished passages are re-screened by
Jaccard and 5-gram with `python3 screen_topics.py final`. Topics abandoned
because the bank already held them are listed in DROPPED at the foot of this
file. They were abandoned, not paraphrased around.

Block counts (three modules x 27, matching assemble_test23.py's QUOTA):
    Words in Context 15, Text Structure and Purpose 6,
    Cross-Text Connections 3, Central Ideas and Details 6,
    Command of Evidence 9, Inferences 6,
    Boundaries 9, Form, Structure, and Sense 9, Transitions 9,
    Rhetorical Synthesis 9                                        = 81
"""

SOURCE = "AUTHORED-T23"
MODULE = "RW"

# The exact table style block from CLAUDE.md. Reused verbatim so tables look
# the same in every test.
TH = 'style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;"'
TD = 'style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;"'


def table(headers, rows):
    head = "".join(f"<th {TH}>{h}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rows)
    return ('<table style="border-collapse:collapse;margin:0.75rem 0;">'
            f"<tr>{head}</tr>{body}</table>")


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
    passage = ("<p><strong>Text 1</strong></p>" + text1 +
               "<p><strong>Text 2</strong></p>" + text2)
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
    """Rhetorical Synthesis, the 'from the notes' shape."""
    bullets = "".join(f"<li>{n}</li>" for n in notes)
    return dict(
        num=num, skill="Rhetorical Synthesis",
        passage=f"While researching a topic, a student has taken the following notes:<ul>{bullets}</ul>",
        stem=f"The student wants to {goal} Which choice most effectively uses relevant "
             "information from the notes to accomplish this goal?",
        choices=choices, answer=answer, why=why)


def syn_given(num, notes, goal, choices, answer, why):
    """Rhetorical Synthesis, the 'from the given sentences' shape.

    Real stems come in both forms and a classifier that knows only the 'notes'
    wording silently misfiles every question of this kind; both are written out
    here so neither shape is missing from the test.
    """
    bullets = "".join(f"<li>{n}</li>" for n in notes)
    return dict(
        num=num, skill="Rhetorical Synthesis",
        passage=f"While researching a topic, a student has taken the following notes:<ul>{bullets}</ul>",
        stem=f"{goal} Which choice most effectively uses information from the given "
             "sentences to accomplish this goal?",
        choices=choices, answer=answer, why=why)


QUESTIONS = [

 # ------------------------------------------------------ Words in Context (15)
 wic("W1",
     "Canal tunnels were cut without a towpath, so the horse was led over the hill and the boat was "
     "moved through by men who lay on planks across the bow and walked the tunnel wall with their "
     "feet. A long tunnel took four hours of this, in cold air and in the dark. Crews who could "
     "raise the fee for a tunnel tug were quick to abandon a method that was so _____.",
     ["laborious", "ingenious", "customary", "economical"], "A",
     "The text dwells on four hours of physical effort in cold and darkness, so the word must "
     "describe hard labour. Calling the method clever praises a quality the text never claims for "
     "it, and the crews' eagerness to pay a tug fee is evidence that they did not find it cheap."),

 wic("W2",
     "A lock gate is not a flat wall across the chamber. Each leaf is hung at an angle, so that the "
     "pair meets in a shallow V pointing towards the higher water. Pressure that would burst a flat "
     "gate instead drives the two leaves harder against one another and against the stone they "
     "close on. The design therefore _____ the very force that threatens it.",
     ["enlists", "withstands", "measures", "conceals"], "A",
     "The pressure is described as doing the closing work, not merely being survived, so the verb "
     "must mean putting that force to use. A word meaning that the design merely holds out against "
     "the pressure misses the point the text is making, which is that the pressure helps."),

 wic("W3",
     "A pumping engine at the foot of a flight returns water to the top of it, so that the same "
     "water serves a second boat instead of running away to the sea. Coal for the engine cost the "
     "company money every day of the year, while the water it saved mattered only in a dry summer. "
     "Directors who authorised such engines were buying _____ against a season they could not "
     "predict.",
     ["insurance", "prestige", "capacity", "goodwill"], "A",
     "A steady cost paid against an uncertain future loss is insurance. The engine adds no carrying "
     "capacity to the line, and nothing in the text suggests the directors were concerned with how "
     "the works looked or with the opinion of anyone outside the company."),

 wic("W4",
     "When a canal froze, the company sent out a short iron-shod boat drawn by a team of horses, "
     "with a dozen men standing along a rail down its centre. The men rocked it from side to side "
     "in time as it went, so that the hull rose and fell and broke a channel wider than its own "
     "beam. Crude as the machine looks, its action had to be carefully _____: rock too slowly and "
     "the ice closed again behind the boat.",
     ["timed", "concealed", "recorded", "priced"], "A",
     "The clause after the colon makes rate the issue, so the word must be about the tempo of the "
     "rocking. Nothing in the text concerns keeping the work secret, writing it down, or costing "
     "it."),

 wic("W5",
     "The men who dug the canals moved with the work, living in huts at the end of the cutting and "
     "leaving when it was finished. Parishes along the line complained about them and were glad to "
     "see them go; the contractors who needed them complained that no sooner had a gang learned the "
     "ground than it was gone to another line for a penny more a day. The workforce was skilled and "
     "_____ in equal measure.",
     ["itinerant", "impoverished", "youthful", "unionised"], "A",
     "Both complaints turn on the same fact, that the men did not stay, so the paired word must "
     "mean travelling from job to job. Their moving for an extra penny a day says nothing about "
     "their poverty, and the text mentions neither their ages nor any organisation among them."),

 wic("W6",
     "In the two years after 1791, subscription lists for new canals filled within hours of "
     "opening, sometimes for lines whose route had not yet been surveyed. Promoters found that the "
     "name of a river and a promise of coal were enough. Investment on those terms was necessarily "
     "_____, and by 1797 a third of the companies authorised had not cut a yard of channel.",
     ["speculative", "modest", "regulated", "collaborative"], "A",
     "Money committed before a route existed is a bet on an unknown, and the failure rate given in "
     "the last clause is the outcome such a bet produces. The sums were plainly not small, and the "
     "text describes an absence of scrutiny rather than any rule governing the subscriptions."),

 wic("W7",
     "Ordinary boats tied up at dusk. A fly boat did not: it carried two crews who slept in turn, "
     "changed horses at stages along the line, and held a company order entitling it to take a lock "
     "ahead of anything waiting. Perishable goods and light manufactures went this way and paid for "
     "the privilege. Set against the leisurely progress of the coal traffic, the fly service was "
     "deliberately _____.",
     ["expeditious", "economical", "seasonal", "unregulated"], "A",
     "Every detail listed &mdash; two crews, relays of horses, priority at locks &mdash; is a means "
     "of going faster, and the contrast drawn is with slow progress. The text says the shippers "
     "paid extra, so the service was not the cheap option, and it operated under a company order "
     "rather than outside the rules."),

 wic("W8",
     "The tow rope of a horse-drawn boat ran from the mast to the animal's collar, and at every "
     "bridge hole it dragged across the corner of the masonry. No single passage marked the stone. "
     "But the same rope crossed the same corner tens of thousands of times, and the grooves cut "
     "into the quoins of some bridges are now deep enough to take a hand. They are a record of "
     "nothing sudden, only of something _____.",
     ["relentless", "violent", "recent", "deliberate"], "A",
     "The text explicitly denies that any one passage did damage and sets the word against "
     "&ldquo;sudden,&rdquo; so it must describe force that never let up. A word meaning great force "
     "contradicts the statement that no single passage marked the stone."),

 wic("W9",
     "A canal company could not charge what it liked. Its Act fixed a maximum for each class of "
     "goods, and the classes were not alike: coal and limestone paid a few pence a ton over a long "
     "haul, while manufactured goods paid several times as much over the same water. The schedule "
     "was _____, and a clerk's decision about which class a cargo fell into could matter more to a "
     "trader than the distance he sent it.",
     ["graduated", "uniform", "provisional", "confidential"], "A",
     "The sentence before the blank sets out rates rising by class, which is what a graduated "
     "schedule is. A word meaning the same throughout states the opposite of the example given, and "
     "a schedule a trader could argue about was neither temporary nor secret."),

 wic("W10",
     "Where a towpath changed from one bank to the other, an ordinary bridge forced the boatman to "
     "unhitch his horse, lead it across and hitch it again, all while the boat carried its way "
     "under him. The bridges built at such crossings instead took the path up one side, over the "
     "arch, and back beneath itself on the far bank, so that the towline stayed attached the whole "
     "way round. The design's whole purpose was to make the change _____.",
     ["uninterrupted", "permanent", "inexpensive", "reversible"], "A",
     "The fault being corrected is the pause while the line comes off, and the remedy keeps the "
     "line attached, so the word must mean without a break. The crossing was already permanent and "
     "could already be made in either direction; neither of those was the problem."),

 wic("W11",
     "A horse pulling a boat at three miles an hour leaves the banks much as it found them. A "
     "propeller driven fast enough to save a day on the run throws a wave against both sides, and "
     "the wave carries away a little clay at every passage. The bank is the company's to repair; "
     "the day saved belongs to the carrier. Companies that imposed speed limits were answering a "
     "situation in which the party causing the damage and the party paying for it were _____.",
     ["distinct", "negligent", "cooperative", "anonymous"], "A",
     "The two sentences before the blank name the company as the payer and the carrier as the "
     "beneficiary, so the word must mark them as different parties. Nothing in the text accuses "
     "either of carelessness, and both are plainly identifiable."),

 wic("W12",
     "A boat carrying grain to a mill once tied up at a public wharf, where the sacks were craned "
     "onto a cart and hauled a quarter of a mile through the streets. The mills that prospered after "
     "1800 were those that cut a short channel of their own from the main line to a basin under "
     "their own walls. What such a mill bought for the price of the digging was the _____ of the "
     "cartage altogether.",
     ["elimination", "regulation", "postponement", "subsidy"], "A",
     "Bringing the water to the mill removes the road journey rather than shortening or deferring "
     "it, so the word must mean doing away with the cartage. A word meaning putting it off later "
     "implies the carts were still needed, which the new channel makes untrue."),

 meaning("W13",
     "Between one lock and the next the water lies dead level, and it is this level stretch, not "
     "the lock, that a boatman calls a <u>pound</u>. A long one holds enough water to absorb a busy "
     "morning's traffic without dropping. A short one, squeezed between two locks in a flight, can "
     "be drawn down several inches by a single boat and has to be refilled from above before the "
     "next boat may pass.",
     "pound",
     ["A unit of weight.", "An enclosure for stray animals.",
      "A level stretch of water between locks.", "A heavy repeated blow."], "C",
     "The first sentence defines the term outright as the level stretch, and both examples that "
     "follow describe quantities of water held between locks. The everyday senses of the word have "
     "nothing to hold water or to be refilled from above."),

 meaning("W14",
     "The surveyor divided the navigation into <u>reaches</u> and reported on each separately: so "
     "many tons of silt lifted from the two miles below the junction, so many from the straight "
     "above the aqueduct, so many from the curve at the mill. Dividing the work this way let the "
     "committee compare a mile of the summit with a mile of the valley and set a price for "
     "maintaining each.",
     "reaches",
     ["Acts of stretching out an arm.", "Distances that can be covered.",
      "Continuous stretches of a waterway.", "Attempts to influence an audience."], "C",
     "Each item in the list after the colon is a named length of water &mdash; two miles below the "
     "junction, the straight, the curve &mdash; so the word must denote a section of the "
     "navigation. Reading it as how far something can travel makes nonsense of lifting silt from "
     "one."),

 meaning("W15",
     "The main line ran past the town without entering it. A short <u>arm</u> was cut from it to a "
     "basin behind the corn mills, wide enough for two boats to pass and ending at a wall with "
     "cranes above it. Traffic for the mills left the main line at the junction and came back to it "
     "loaded, and the mills never had to send a cart to the public wharf at all.",
     "arm",
     ["A limb of the body.", "A branch channel leading off a main one.",
      "A weapon carried by a person.", "A division of a large organisation."], "B",
     "The thing named is cut from the main line, is wide enough for boats and ends at a basin, so "
     "it must be a branch of the waterway. The organisational sense would make the following "
     "description of width and cranes incoherent."),

 # ---------------------------------------------- Text Structure and Purpose (6)
 tsp("T1",
     "A canal cut through gravel will not hold water. The remedy the early engineers used was "
     "puddle: clay worked with water and trodden until it is uniform, then laid in layers against "
     "the bed and the sides. <u>The material has no strength of its own and depends entirely on "
     "staying wet.</u> A pound drained for repair in a hot summer could crack its lining beyond "
     "saving, which is why companies preferred to do heavy work in winter and to refill a length as "
     "soon as the masons were clear of it.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It identifies a property of the lining that accounts for the working practice described "
      "afterwards.",
      "It concedes a weakness in a claim that the text goes on to reject.",
      "It defines a technical term introduced in the previous sentence.",
      "It introduces a second method of lining that the text then compares with the first."], "A",
     "The sentence states that puddle must stay wet, and everything after it &mdash; winter "
     "working, prompt refilling &mdash; follows from that requirement. It does not define puddle, "
     "which the previous sentence has already defined, and no second lining method appears "
     "anywhere in the text."),

 tsp("T2",
     "On the river navigations that came before the canals, boats were pulled by gangs of men who "
     "worked the bank for hire and had no employer beyond the day. Canal companies built a made "
     "path, fenced it, and let it only to boats that had paid a toll &mdash; and a horse on a firm "
     "level path could do what six men on a rutted bank could not. Within a generation the bow "
     "hauliers were gone from every line that had a towpath, and survived only where the bank was "
     "still whatever the river had left of it.",
     "Which choice best states the main purpose of the text?",
     ["To explain how a change in the path itself displaced one kind of haulage with another.",
      "To argue that the men who hauled boats were treated unfairly by the canal companies.",
      "To describe in detail how a towpath was constructed.",
      "To compare the cost of horse haulage with the cost of steam towage."], "A",
     "The text turns on the made path: it is what lets a horse outwork six men and what marks the "
     "boundary of where the hauliers survived. The construction of the path is mentioned in a "
     "clause rather than described, and steam towage never appears."),

 tsp("T3",
     "An iron trough carried across a valley on stone piers has to be designed for the weight of "
     "the water standing in it. A loaded boat entering the trough pushes aside exactly its own "
     "weight of water, which runs out at the ends. The engineer therefore sizes the piers for a "
     "full trough and stops there: whether one boat is crossing or none makes no difference to what "
     "they carry, and a queue of them makes none either.",
     "Which choice best states the main purpose of the text?",
     ["To explain why the traffic crossing an aqueduct does not affect the load its piers carry.",
      "To describe how iron troughs and stone piers were built.",
      "To argue that iron aqueducts were superior to masonry ones.",
      "To recount the career of the engineer who devised the iron trough."], "A",
     "Each sentence advances one conclusion, that the load is fixed by the water rather than by the "
     "boats. Masonry aqueducts are never mentioned, so no comparison with them is being made, and "
     "no engineer is named."),

 tsp("T4",
     "A toll clerk took the boatman's declaration of what he carried and charged the rate for that "
     "class. A boatman who declared road stone and carried finished ironware paid a fraction of "
     "what he owed, and nothing in the toll house could tell the difference. <u>The company's loss "
     "was invisible: it appeared in no ledger, because the ledger recorded only what had been "
     "declared.</u> Check clerks were therefore stationed along the line to board boats at random, "
     "turn back the cloths and compare what they found with the ticket issued at the last toll "
     "house.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It explains why the company's own records could not reveal the problem, which is why an "
      "independent check was needed.",
      "It concedes that the sums involved were too small to be worth pursuing.",
      "It introduces a second form of fraud unrelated to the one already described.",
      "It restates the argument of the text as a whole in shorter form."], "A",
     "The sentence explains that the fraud left no trace in the accounts, and the next sentence "
     "sends men out to look at the boats themselves; the word &ldquo;therefore&rdquo; makes the "
     "link explicit. The text never says the losses were trivial, and only one fraud is described."),

 tsp("T5",
     "Two jobs on a navigation look alike from the bank and are not. Weed cutting takes off what "
     "has grown in the water this season; dredging takes out what has settled on the bed over many. "
     "A length cut clear in July may need cutting again in September and will not need dredging for "
     "twenty years. Committees that entered the two under one heading in the accounts never "
     "understood why the figure rose every year when much of the work behind it had not been done "
     "for a generation.",
     "Which choice best states the main purpose of the text?",
     ["To show that two superficially similar operations differ in ways that matter to a budget.",
      "To recommend that weed cutting be carried out more often than it usually is.",
      "To describe the machinery used to clear a navigation.",
      "To explain why silt settles faster in some lengths than in others."], "A",
     "The text opens by denying that the two jobs are the same and closes on the accounting "
     "confusion that follows from treating them as one. No machinery appears, and the reason silt "
     "settles is never raised."),

 tsp("T6",
     "A towpath was never a public road. It was company property, made for the horses of boats that "
     "had paid a toll, and walkers on it were trespassers whom the company tolerated. <u>That "
     "history explains the odd position the paths occupy now.</u> Most are open to the public by "
     "agreement rather than by right, and the navigation authority that maintains a length may "
     "close it for repair without the procedure a highway would demand.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It connects the historical account before it to the present-day consequence described after "
      "it.",
      "It states a conclusion that the rest of the text goes on to dispute.",
      "It offers an example of a towpath that has been closed to walkers.",
      "It defines a legal term used in the sentence that follows."], "A",
     "The sentence looks back to the company ownership just described and forward to the modern "
     "arrangement set out next, and the text does not dispute what it asserts. It names no "
     "particular path and defines no term."),

 # ----------------------------------------------- Cross-Text Connections (3)
 ctc("X1",
     "<p>Historians long explained the collapse of canal carrying in a sentence: the railway was "
     "faster. A train covered in a morning what a boat took three days to do, and no amount of "
     "management could close a gap of that size. On this account the canals were beaten by a "
     "technology against which they had no answer.</p>",
     "<p>Speed mattered less than that account supposes. Coal, stone and timber made up the bulk of "
     "canal tonnage and none of it was urgent; the owners would have gone on sending it by water at "
     "a low enough price. A canal company's Act, however, fixed the most it might charge on every "
     "class of goods. It could cut a rate, but it could not raise the rate on the traffic that "
     "stayed in order to fund the cut, because that rate already stood at its statutory ceiling. "
     "The railway companies, bound far more loosely, could attack one traffic and recover on "
     "another.</p>",
     "Based on the texts, how would the author of Text 2 most likely respond to the explanation "
     "offered in Text 1?",
     ["By arguing that it mistakes a difference in commercial freedom for a difference in speed.",
      "By agreeing that speed was decisive but adding that it took longer to matter than is usually "
      "supposed.",
      "By pointing out that most canal tonnage was in fact urgent traffic.",
      "By denying that railway companies ever cut their charges."], "A",
     "Text 2 accepts that the railway was faster and locates the decisive difference elsewhere, in "
     "what each kind of company was legally free to charge. It says the bulk of the tonnage was not "
     "urgent, the opposite of the claim about urgent traffic, and it describes railway companies "
     "cutting rates rather than denying that they did."),

 ctc("X2",
     "<p>A derelict canal is not a wildlife park; it is an unfinished piece of engineering. The "
     "societies that reopen a line hang the lock gates again, dredge the bed to its designed depth "
     "and return the water to a channel that was cut to hold it. The alternative is not "
     "preservation but slow disappearance: reed, then willow, then a ditch that nobody can "
     "find.</p>",
     "<p>Sixty years of neglect turn a canal into something its engineers never made. Shallow, "
     "weedy water of a kind that has become scarce in the surrounding country supports plants and "
     "invertebrates that a dredged and navigated channel cannot hold. Ecologists do not object to "
     "restoration as such. They object to a restored length being reported as a recovery when, "
     "measured by what actually lives in it, what has taken place is an exchange.</p>",
     "Based on the texts, the author of Text 2 would most likely characterise the outcome that "
     "Text 1 calls restoration as",
     ["a substitution of one set of living things for another rather than a straightforward gain.",
      "a change that leaves the wildlife of a canal essentially unaffected.",
      "an engineering failure that restoration societies have not been willing to admit.",
      "an improvement that ecologists have been slow to acknowledge."], "A",
     "Text 2's closing word is &ldquo;exchange,&rdquo; and its objection is to calling that "
     "exchange a recovery, which is precisely a denial that the outcome is a plain gain. It cannot "
     "be saying the wildlife is unaffected, since its whole case is that the scarce shallow-water "
     "species are lost."),

 ctc("X3",
     "<p>The steam tug that took over the long tunnels is usually described as a straightforward "
     "improvement. It brought a train of boats through in forty minutes where legging took four "
     "hours, and it ended a job that ruined men's backs. Nobody who had legged a tunnel would have "
     "wanted the practice kept.</p>",
     "<p>The tug charged by the boat, and the charge fell on the carrier whether his cargo could "
     "bear it or not. A fly boat carrying manufactures saved three hours that it could sell. A boat "
     "carrying coal at a few pence a ton saved three hours that it could not, and its crew went on "
     "legging until the company forbade it two decades later. What looks in retrospect like a clean "
     "replacement was for a generation a choice that different traffics made differently.</p>",
     "Based on the texts, the author of Text 2 would most likely respond to Text 1's description of "
     "the tug by",
     ["noting that the time it saved was worth paying for only to some of the traffic that could "
      "have used it.",
      "denying that the tug was in practice any faster than legging.",
      "arguing that the physical strain of legging has been exaggerated.",
      "showing that companies compelled every boat to use the tug from the outset."], "A",
     "Text 2 contrasts a boat that could sell the hours saved with one that could not, which is an "
     "argument about who the saving was worth its price to. It never questions the forty-minute "
     "figure, and it says compulsion came two decades later, so it does not claim compulsion from "
     "the start."),

 # ------------------------------------------------ Central Ideas and Details (6)
 cid("C1",
     "In an ordinary flight each lock has a pound above it and a pound below it, and two boats can "
     "work past one another in those intervals. A staircase has no pounds: the top gate of one "
     "chamber is the bottom gate of the next, so water leaving the upper chamber has nowhere to go "
     "except into the lower one. A boat coming down must find every chamber below it empty, and a "
     "boat going up must find every chamber above it full. Two boats meeting on a staircase cannot "
     "pass, and one of them has to be worked right through before the other may start.",
     "Which choice best states the main idea of the text?",
     ["Because a staircase's chambers share their gates, one boat's passage has to be finished "
      "before another's can begin.",
      "Staircase locks raise boats higher than ordinary flights of locks do.",
      "Staircase locks were built because they use less water than ordinary flights.",
      "Boats going up a staircase travel more slowly than boats coming down."], "A",
     "The shared gate is given as the reason there are no pounds, and the absence of pounds is what "
     "forces the chambers into opposite states for the two directions and rules out passing. The "
     "text compares neither the height nor the water consumption of the two arrangements."),

 cid("C2",
     "The mud lifted out of a navigation has to be put somewhere, and the cheapest somewhere is the "
     "field side of the bank, straight over the gunwale of the mud boat. A century of this raised "
     "the offside of many canals into a low ridge, which seeded itself with hawthorn and left the "
     "water sitting visibly above the meadow beyond. Farmers who had sold a strip of land for a "
     "channel found themselves living beside an embankment nobody had asked them about, and several "
     "companies were sued over it.",
     "According to the text, what was one consequence of the way dredged material was disposed of?",
     ["The bank on the side away from the towpath was gradually built up above the land around it.",
      "The channel became too shallow for loaded boats to work through.",
      "Companies were obliged to carry the material away by boat to a distant tip.",
      "Hawthorn was planted along the new bank to hold it together."], "A",
     "The text says the offside was raised into a ridge that left the water above the meadow, which "
     "is the consequence asked for. It says the hawthorn seeded itself, so nobody planted it, and "
     "tipping over the side is described as the alternative to carrying the mud away."),

 cid("C3",
     "A canal on an embankment holds several feet of water above a valley, and a hole in the lining "
     "will empty a mile of it in an hour. Companies could not prevent every breach, so they set out "
     "instead to limit what one would cost them. Pairs of gates were hung at intervals along the "
     "exposed lengths, standing open in the water and held back by a catch; a rush of water towards "
     "a breach knocks the catch and slams them shut, and the loss stops at the length between one "
     "pair and the next.",
     "Which choice best states the main idea of the text?",
     ["Rather than trying to prevent breaches, companies installed gates that confine the damage a "
      "breach can do.",
      "Embanked lengths of canal were abandoned because they could not be made safe.",
      "Stop gates were closed by a keeper as soon as a breach was reported to him.",
      "A breach in an embankment will empty the whole of a canal."], "A",
     "The second sentence states the strategy in so many words and the third describes the device "
     "that carries it out. The gates are shut by the rush of water itself rather than by anyone, "
     "and the text puts the loss at a mile rather than the whole line."),

 cid("C4",
     "A boat horse worked a stage of about fifteen miles and was then changed, and stables stood at "
     "the ends of every stage. The animal ate whether it worked or not, which is why a carrier with "
     "a heavy trade and a carrier with a light one made very different arrangements. The first "
     "owned his horses and his stables outright. The second hired both by the day from an innkeeper "
     "on the line, at a rate that would have ruined him had he needed them every day of the week.",
     "According to the text, why did a carrier with a light trade hire horses rather than own "
     "them?",
     ["Owning an animal meant paying to feed it on the days it earned nothing.",
      "Hired horses were stronger than any a small carrier could afford to buy.",
      "Innkeepers on the line refused to stable horses a carrier owned himself.",
      "Companies required carriers with light traffic to use hired animals."], "A",
     "The text gives the reason directly: the horse eats whether it works or not, and the light "
     "trader cannot spread that cost over enough working days. It makes no claim about the relative "
     "strength of hired animals and mentions no rule compelling anyone to hire."),

 cid("C5",
     "The warehouses built beside the early basins loaded across an open quay, and rain stopped the "
     "work. The next generation was built over the water instead. The channel ran in through an "
     "arch beneath the building, boats lay in the dark under the floors, and hoists in the ceiling "
     "lifted goods straight up through trapdoors into whichever storey had room for them. Nothing "
     "crossed open ground, nothing waited on the weather, and a cargo could go from hold to top "
     "floor without a cart being called for at all.",
     "Which choice best states the main idea of the text?",
     ["Bringing the water inside the building took both the weather and the cartage out of the "
      "transfer of goods.",
      "The early basins were abandoned because their quays had become too small.",
      "Hoists were the most expensive part of a canal warehouse to install.",
      "Goods stored on the upper floors were less likely to be spoiled by damp."], "A",
     "The final sentence names exactly two things the arrangement removed, waiting on the weather "
     "and the cart, and the rest of the text explains how. Cost and damp are never discussed, and "
     "the size of the early quays is not given as the reason for the change."),

 cid("C6",
     "Where one company's line joined another's, a boat passing from the first to the second "
     "stopped paying the first and began paying the second, and the first company lost a haul it "
     "had built its works to carry. Several Acts therefore provided for a compensation toll: a "
     "payment made by the second company to the first on every ton crossing the junction, "
     "reckoned as though part of the journey had been made on the older line. The arrangement kept "
     "the junctions open. It also made the through rate higher than the sum of what either company "
     "would have charged on its own.",
     "According to the text, what was one effect of compensation tolls?",
     ["Sending goods across a junction cost more than the two companies' own charges added "
      "together.",
      "Companies refused to build junctions with one another's lines.",
      "The older company had to pay the newer one for the traffic it had lost.",
      "A boat was charged twice by the same company for a single haul."], "A",
     "The last sentence states the effect outright. The payment runs from the newer company to the "
     "older one, so the option reversing that direction contradicts the text, and the text says the "
     "arrangement kept junctions open rather than preventing them."),

 # -------------------------------------------------- Command of Evidence (9)
 coe("E1",
     "A canal company's Act set a different maximum rate for each class of goods, and the traffic "
     "was not distributed as the classes might suggest. The table gives one company's tonnage and "
     "toll receipts for four classes of goods in 1838." +
     table(["Class of goods", "Tons carried", "Toll receipts (&pound;)"],
           [["Coal and coke", "214,000", "4,280"],
            ["Stone, sand and lime", "96,000", "2,400"],
            ["Timber", "31,000", "1,550"],
            ["Manufactured goods", "16,000", "2,700"]]) +
     " A student concluded that a small share of the tonnage could matter more to the company's "
     "income than its size suggests.",
     "Which choice most effectively uses data from the table to support the student's conclusion?",
     ["Manufactured goods made up under five per cent of the tonnage shown yet produced more toll "
      "income than stone, sand and lime, which were six times as heavy.",
      "Coal and coke produced more toll income than any other class shown.",
      "Timber produced less toll income than coal and coke did.",
      "Stone, sand and lime accounted for more tonnage than timber and manufactured goods "
      "together."], "A",
     "The conclusion needs a class that is light in tonnage and heavy in receipts, and manufactured "
     "goods are 16,000 of the 357,000 tons shown while earning 2,700 pounds against the 2,400 "
     "pounds earned by 96,000 tons of stone, sand and lime. The other statements are all true of "
     "the table but describe classes whose income tracks their tonnage, so none of them bears on "
     "the point."),

 coe("E2",
     "A canal loses water in two ways: through the locks, in proportion to how many boats pass, and "
     "through the bed and banks, whether any boat passes or not. An engineer gauged four pounds on "
     "one line during a week in which the traffic was also recorded, separating the volume that "
     "went down through the locks from the volume that disappeared without a boat moving." +
     table(["Pound", "Boats passed in the week", "Lost through the locks (cubic metres)",
            "Lost through bed and banks (cubic metres)"],
           [["Summit", "62", "8,680", "1,150"],
            ["Marsh", "58", "8,120", "6,900"],
            ["Highfield", "24", "3,360", "1,400"],
            ["Ryebank", "21", "2,940", "5,600"]]) +
     " The engineer argued that on some pounds restricting traffic would save far less water than "
     "repairing the lining.",
     "Which choice most effectively uses data from the table to support the engineer's argument?",
     ["At Ryebank the bed and banks lost nearly twice the volume that the whole week's lockages "
      "took.",
      "At the summit the locks accounted for far more of the loss than the bed and banks did.",
      "Marsh passed almost as many boats during the week as the summit did.",
      "Highfield lost less water in total than any other pound listed."], "A",
     "The argument needs a pound whose leakage dwarfs its lockage, and Ryebank lost 5,600 cubic "
     "metres through the bed and banks against 2,940 through the locks. The summit figures show the "
     "opposite relationship, and the traffic comparison and the total for Highfield say nothing "
     "about which of the two kinds of loss is the larger."),

 coe("E3",
     "A navigation authority imposed a speed limit on part of one line and left the rest unchanged, "
     "then measured how far the bank had retreated at four sites over the following three years." +
     table(["Site", "Speed limit in force", "Boats passing per year",
            "Bank retreat over three years (cm)"],
           [["Ashlock", "Yes", "3,100", "4"],
            ["Bramble", "No", "3,050", "19"],
            ["Coldwell", "Yes", "1,400", "3"],
            ["Denbrook", "No", "1,450", "11"]]) +
     " The authority concluded that the retreat depended more on the speed of the boats than on how "
     "many of them passed.",
     "Which choice most effectively uses data from the table to support the authority's "
     "conclusion?",
     ["Ashlock, where a limit was in force, carried more than twice Denbrook's traffic and lost "
      "about a third as much bank.",
      "Bramble lost more bank over the three years than any of the other sites.",
      "The two sites with the heavier traffic carried more than twice as many boats as the two "
      "with the lighter traffic.",
      "Coldwell lost the least bank of the four sites measured."], "A",
     "Only a comparison in which the busier site loses less bank can separate speed from volume, "
     "and Ashlock passed 3,100 boats for 4 centimetres of retreat while Denbrook passed 1,450 for "
     "11. Every other statement is true of the table but is consistent with traffic alone driving "
     "the retreat."),

 coe("E4",
     "Historian Ruth Aldwinckle argues that the authority a fly boat enjoyed at a lock rested less "
     "on the company's written order than on the readiness of waiting boatmen to give way without "
     "being shown it.",
     "Which quotation from Josiah Kemp's memoir of the carrying trade most effectively illustrates "
     "Aldwinckle's claim?",
     ["&ldquo;The fly came up behind us at the bottom lock and we drew our boat aside for her "
      "without a word said, as any crew would; the order in her cabin was never once produced in my "
      "hearing.&rdquo;",
      "&ldquo;The company's order was pinned inside the cabin door of every fly boat on the line, "
      "printed on stiff card and signed by the clerk.&rdquo;",
      "&ldquo;We were four hours in the tunnel that night and came out at Bledlow with the horse "
      "already waiting at the far end.&rdquo;",
      "&ldquo;The flys changed horses at Wharton and again at the summit, and never tied up between "
      "the one and the other.&rdquo;"], "A",
     "Aldwinckle's claim needs boatmen giving way of their own accord and the written order going "
     "unproduced, and the quotation about drawing aside without a word says both. Describing how "
     "the order was printed and signed supports the opposite emphasis, and the tunnel and horse "
     "quotations concern something else entirely."),

 coe("E5",
     "The committee of one canal company is often said to have resisted the expense of a pumping "
     "engine for as long as it possibly could, agreeing to consider the question again rather than "
     "settling it.",
     "Which quotation from the company's minute book most effectively illustrates that resistance?",
     ["&ldquo;Resolved, that the question of a pumping engine be referred once more to the works "
      "committee, the present season having proved less dry than was apprehended.&rdquo;",
      "&ldquo;Resolved, that a pumping engine be erected at the foot of the flight without delay, "
      "and that tenders be advertised within the month.&rdquo;",
      "&ldquo;Resolved, that the reservoir at Cheddleton be enlarged by ten acres, the land having "
      "been purchased in the last year.&rdquo;",
      "&ldquo;Resolved, that the surveyor do report upon the state of the lining between the third "
      "and the fourth locks.&rdquo;"], "A",
     "The claim is about postponing a decision, and only the resolution that sends the engine back "
     "to committee on the ground that the season turned out wet does that. One resolution orders "
     "the engine at once, and the other two concern a reservoir and a survey rather than the engine "
     "at all."),

 coe("E6",
     "In her account of a journey by canal in 1846, the traveller Anne Marbury dwells on the "
     "disorientation of passing through a long tunnel rather than on the labour it cost the men who "
     "moved the boat.",
     "Which quotation from Marbury's account most effectively illustrates this emphasis?",
     ["&ldquo;There was no up nor down in that place, and but for the drip that struck the cabin "
      "roof I could not have told whether we moved at all.&rdquo;",
      "&ldquo;The two men lay upon their planks and walked the wall, and their breath came hard "
      "enough to be heard the length of the boat.&rdquo;",
      "&ldquo;We were an hour and fifty minutes within, by my husband's watch, and came out into a "
      "cutting hung about with ferns.&rdquo;",
      "&ldquo;The horse had been sent over the hill at the mouth and stood waiting at the far end "
      "when we came out.&rdquo;"], "A",
     "Disorientation is a loss of one's bearings, and the quotation in which there is no up nor "
     "down and the writer cannot tell whether the boat is moving is exactly that. The quotation "
     "about hard breathing describes the labour Marbury is said to pass over, and the timed passage "
     "and the horse are plain narration."),

 coe("E7",
     "The stone at the corner of some canal bridges is cut with deep vertical grooves. One "
     "explanation is that they were worn by tow ropes dragging across the arris as boats were "
     "pulled past. Another is that they were cut on purpose to seat a timber rubbing post.",
     "Which finding, if true, would most strongly support the tow-rope explanation?",
     ["The grooves are absent from bridges where the towpath passed under the arch without changing "
      "sides, and are deepest where the rope had to cross the corner at a sharp angle.",
      "Grooves of similar depth are found on road bridges that boats never passed beneath.",
      "Timber posts survive at several of the bridges where grooves are also present.",
      "The grooves are cut into stone that is softer than the rest of the bridge."], "A",
     "If the rope made the grooves, they should appear only where a rope crossed the stone and "
     "should deepen with the angle, which is what the finding about towpath layout describes. "
     "Surviving timber posts point instead to the deliberate seating explanation, and grooves on "
     "bridges no boat passed would undermine the rope account altogether."),

 coe("E8",
     "After a pumping engine was installed at the foot of a flight in 1842, the summit pound held "
     "its level through several dry summers in which it had previously failed, and the company "
     "credited the engine. A modern historian suspects that a reservoir enlarged in the same decade "
     "and a fall in traffic after the railway opened did most of the work.",
     "Which finding, if true, would most directly weaken the company's explanation?",
     ["In the two dry summers after the engine was built but before the reservoir was enlarged, the "
      "summit fell to the same levels it had reached before the engine existed.",
      "The engine burned more coal in dry years than in wet ones.",
      "Traffic on the line rose in the years immediately after the engine was installed.",
      "Other companies on the same watershed installed similar engines during the same decade."],
     "A",
     "Isolating the engine from the reservoir is the only way to test the company's claim, and a "
     "period with the engine working and the reservoir still small in which the summit failed as "
     "before shows the engine was not what saved it. Rising traffic would strengthen rather than "
     "weaken the company's case, since the level then held under a heavier demand."),

 coe("E9",
     "Ecologists studying a derelict canal argued that the shallow weedy water it had become "
     "supported species a restored and navigated channel could not hold. A restoration society "
     "replied that the plants concerned would survive in the margins and in the pounds above the "
     "top lock, where boats seldom go.",
     "Which finding, if true, would most directly support the restoration society's reply?",
     ["Surveys of a line reopened twenty years ago find the same plants in its margins and its "
      "least-used pounds at densities close to those recorded before it was restored.",
      "The plants concerned also grow in ponds and ditches across the surrounding county.",
      "Traffic on restored canals has risen faster than restoration societies predicted it would.",
      "The derelict length supports more species than any restored length yet surveyed."], "A",
     "The society's claim is specifically that the plants persist within a restored canal, so the "
     "evidence has to come from a restored canal, and a reopened line still holding them at similar "
     "densities is exactly that. Their presence in ponds elsewhere says nothing about survival in "
     "the channel, and heavier traffic and a richer derelict length both cut against the reply."),

 # ------------------------------------------------------------- Inferences (6)
 inf("I1",
     "The leaves of a lock gate meet in a V pointing towards the higher water, and the pressure of "
     "that water is what holds them closed. A gate cannot be pushed open against it: the paddles "
     "must be drawn first and the two levels allowed to come together. A boatman who finds a gate "
     "that will not move should therefore suspect not that the gate is jammed but that _____",
     ["water is still standing higher on one side of it than on the other.",
      "the ironwork of the leaves has been damaged by an earlier boat.",
      "his boat is too wide for the chamber he is trying to enter.",
      "the gate has been locked by the company against unauthorised use."], "A",
     "The text gives one reason a gate will not move, an unequalised head of water, and says the "
     "paddles must be drawn before it will. Damaged ironwork, the width of a boat and a company "
     "padlock are all possible in the world but none of them is anything the text has established."),

 inf("I2",
     "A canal company's Act stated the most it might charge for each class of goods, a protection "
     "written into the law when the company was the only carrier on its route. Railway companies "
     "were incorporated under Acts that bound them far more loosely and could quote a low rate for "
     "one traffic and recover the loss on another. A canal company facing that competition could "
     "cut its own rates, but it could not _____",
     ["make up the shortfall by charging more to the traffic that remained.",
      "carry goods of a class its Act had not mentioned.",
      "reduce its charges below the maximum stated in its Act.",
      "apply to Parliament for any amendment of its powers."], "A",
     "The maximum binds the company only from above, so the freedom it lacks is the freedom to "
     "raise a rate, which is exactly the recovery the railway companies are described as making. "
     "The text says the canal company could cut its rates, so an option denying that contradicts "
     "it outright."),

 inf("I3",
     "Puddle depends on staying wet: dried out it shrinks, cracks and will not close again when the "
     "water comes back. Concrete lining, which replaced it on many lengths in the twentieth "
     "century, is indifferent to being left dry. The change therefore mattered far less to a canal "
     "in daily use than to one _____",
     ["that had to be emptied for long repairs or was left without water for years at a time.",
      "whose traffic consisted mainly of heavy and slow-moving cargoes.",
      "that crossed a valley on an embankment rather than running in a cutting.",
      "built by a company wealthy enough to employ masons of its own."], "A",
     "The only property distinguishing the two linings is what happens when they dry out, so the "
     "canals to which the change matters are the ones that dry out. The kind of cargo, the shape of "
     "the ground and the company's wealth are all irrelevant to whether a lining stays wet."),

 inf("I4",
     "A boatman who owned his boat was paid for what he delivered, not for the days he worked. A "
     "frozen canal did not reduce his earnings in proportion to the delay; it stopped them "
     "altogether, while the horse still ate and the family still lived aboard. Set beside a company "
     "boatman on weekly wages, an owner therefore had reason to _____",
     ["contribute far more willingly towards the cost of keeping a channel open in frost.",
      "prefer a route with more locks on it than his competitors used.",
      "carry only goods that could be delivered within a single day.",
      "regard the company's toll schedule as the chief threat to his living."], "A",
     "The owner alone loses his whole income to a stoppage while his costs continue, so the ice "
     "boat is worth more to him than to a man still drawing wages. Nothing in the text connects "
     "that difference to the number of locks, the length of a haul or the level of tolls."),

 inf("I5",
     "The towpath changes sides wherever the ground makes it necessary, and every change costs the "
     "boatman something. At an ordinary bridge he must stop, cast off the line, lead the horse "
     "across and pick the line up again, with the boat carrying its way under him the whole time. A "
     "turnover bridge takes the path over the arch and back beneath itself, so the line never comes "
     "off. The design was worth most, then, to a boat worked by _____",
     ["a single hand, who could not mind the horse and hold the tiller at the same time.",
      "a crew large enough to change its horses at every stage along the line.",
      "a company that owned the bridges as well as the boats that passed under them.",
      "a carrier whose cargo was perishable rather than bulky."], "A",
     "The cost named is that the boat carries its way while the line is off, and only a boatman with "
     "nobody else aboard must abandon the tiller to deal with the horse. A large crew can do both "
     "jobs at once, and neither ownership of the bridges nor the nature of the cargo affects who "
     "must leave the tiller."),

 inf("I6",
     "A lorry moving thirty tonnes uses several times as much fuel for each tonne it carries a "
     "kilometre as a barge moving three hundred. The barge is nonetheless the dearer option on most "
     "British routes, because hardly any factory or warehouse now stands on the water: the goods "
     "must be lifted twice and carried by road at each end of the voyage. The advantage of water "
     "carriage survives, then, only where _____",
     ["the origin and the destination both stand on the waterway itself.",
      "the cargo is light enough to be handled without cranes.",
      "the journey is short enough to be completed within a single day.",
      "fuel prices rise faster than the cost of labour does."], "A",
     "The text names one thing that cancels the fuel advantage, the road journey and double "
     "handling at each end, so the advantage survives where those are absent, which means both ends "
     "are on the water. Cargo weight, journey length and fuel prices leave the terminal handling "
     "exactly as it was."),

 # -------------------------------------------------------------- Boundaries (9)
 bnd("B1",
     "Three reservoirs in the hills feed the summit, and in a wet year the company needs very "
     "little of what they _____ August of 1826 the summit was down to eighteen inches over the "
     "sill and all traffic stopped for a fortnight.",
     ["hold. In the dry", "hold, in the dry", "hold in the dry", "hold: in the dry"], "A",
     "Two complete sentences meet at the blank and nothing joins them, so a full stop is the only "
     "option that separates them properly. A comma between them makes a splice, running them "
     "together with no mark at all leaves a fused sentence, and the second clause contrasts with "
     "the first rather than explaining it, which is what a colon would promise."),

 bnd("B2",
     "The level stretch of water between one lock and the next, known to boatmen as a _____ dead "
     "level, and a short one can be drawn down several inches by a single boat.",
     ["pound, is", "pound is", "pound; is", "pound: is"], "A",
     "The phrase beginning &ldquo;known to boatmen&rdquo; is a supplement opened by a comma, so it "
     "has to be closed by one before the sentence resumes with its verb. Leaving the mark out "
     "strands the opening comma, and neither a semicolon nor a colon may stand between a subject "
     "and its verb."),

 bnd("B3",
     "The company's Act named three classes of goods and fixed a separate maximum rate for _____ "
     "building stone and general merchandise.",
     ["each: coal,", "each, coal,", "each coal,", "each; coal,"], "A",
     "What stands before the blank is a complete sentence and what follows it is a list naming the "
     "three classes, and a colon is the mark that introduces a list after a complete sentence. A "
     "comma leaves the list looking like a continuation of the phrase &ldquo;rate for each,&rdquo; "
     "no punctuation at all makes coal the object of that phrase, and a semicolon must be followed "
     "by something that could stand as a sentence."),

 bnd("B4",
     "Because the top gate of one chamber is at the same time the bottom gate of the _____ boats "
     "cannot pass one another anywhere on a staircase.",
     ["next, two", "next two", "next; two", "next: two"], "A",
     "A long introductory clause beginning with &ldquo;Because&rdquo; must be closed off by a comma "
     "before the main clause starts. Without the comma the reader takes &ldquo;the next two "
     "boats&rdquo; as a single phrase, and a semicolon or a colon would require what precedes it to "
     "stand as a complete sentence, which a clause opening with &ldquo;Because&rdquo; does not."),

 bnd("B5",
     "The bridges built where the towpath changed banks &mdash; turnover bridges, in the boatmen's "
     "_____ the towline attached the whole way round the arch.",
     ["phrase &mdash; kept", "phrase, kept", "phrase kept", "phrase; kept"], "A",
     "The supplement is opened with a dash, so it must be closed with a dash; the marks at the two "
     "ends of a parenthetical have to match. A comma or a semicolon leaves the opening dash "
     "unanswered, and omitting the mark altogether runs the supplement into the predicate."),

 bnd("B6",
     "The two operations are not the same and are not costed the same way. Weed cutting removes "
     "what has grown in the water this _____ takes out what has settled on the bed over many.",
     ["season; dredging", "season, dredging", "season dredging", "season: dredging"], "A",
     "The blank falls between two complete statements that are closely paired, and a semicolon is "
     "the mark for exactly that. A comma between them is a splice, no mark at all fuses them, and a "
     "colon would announce that the second explains the first when it instead sets a contrasting "
     "case beside it."),

 bnd("B7",
     "The check clerk who boarded boats at random and compared what he found under the cloths with "
     "the ticket issued at the last toll _____ by the company rather than by the carrier.",
     ["house was paid", "house, was paid", "house; was paid", "house: was paid"], "A",
     "Everything from &ldquo;The check clerk&rdquo; to &ldquo;toll house&rdquo; is one long subject "
     "and &ldquo;was paid&rdquo; is its verb, and no punctuation belongs between a subject and its "
     "verb however long the subject grows."),

 bnd("B8",
     "A horse walking a made and level towpath could pull a load that six men on a rutted riverbank "
     "could _____ the bow hauliers vanished from every line that had such a path.",
     ["not, and", "not and", "not; and", "not: and"], "A",
     "Two complete statements are joined here by &ldquo;and,&rdquo; and a comma belongs before the "
     "conjunction when the clauses either side of it are both independent and this long. A "
     "semicolon or a colon before a coordinating conjunction is not a standard pairing, and leaving "
     "the comma out runs the two statements together."),

 bnd("B9",
     "Floated empty in a gauging dock and then loaded a ton at a time with iron _____ new boat "
     "yielded a table converting inches of freeboard into tons of cargo.",
     ["weights, each", "weights each", "weights; each", "weights: each"], "A",
     "The opening participial phrase describes the boat and must be marked off by a comma before "
     "the main clause begins. Without it the reader joins &ldquo;iron weights&rdquo; to "
     "&ldquo;each new boat,&rdquo; and a semicolon or colon would need a complete sentence in front "
     "of it, which a participial phrase is not."),

 # -------------------------------------------- Form, Structure, and Sense (9)
 fss("F1",
     "The record of the tolls taken at the four toll houses on the summit level _____ in the county "
     "archive, bound in a single volume.",
     ["is preserved", "are preserved", "have been preserved", "were being preserved"], "A",
     "The subject is the single record, not the four toll houses named in the phrase that follows "
     "it, so the verb must be singular. Every plural form agrees with the nearest noun instead of "
     "with the true subject."),

 fss("F2",
     "By the time the surveyor reached the bottom of the flight in March, the frost _____ two of "
     "the lower gates, and new leaves had to be hung before the season opened.",
     ["had split", "has split", "splits", "will have split"], "A",
     "The splitting happened before the surveyor arrived, and both surrounding verbs are in the "
     "past, so the earlier action needs the past perfect. A present or future form cannot describe "
     "something already complete when a past event took place."),

 fss("F3",
     "Each of the four companies whose lines met at the junction charged a compensation toll, and "
     "each reckoned _____ payment from a different point on the older route.",
     ["its", "their", "it&rsquo;s", "there"], "A",
     "The word before the blank is &ldquo;each,&rdquo; which is singular, so the possessive must be "
     "singular too. The contraction of &ldquo;it is&rdquo; is not a possessive at all, and an "
     "adverb of place cannot modify a noun."),

 fss("F4",
     "Tens of thousands of tow ropes crossed the same corner of the same bridge. The grooves in the "
     "quoins are the only record left of those _____ passage, and they are deepest where the line "
     "had to turn most sharply.",
     ["ropes&rsquo;", "rope&rsquo;s", "ropes", "ropes&rsquo;s"], "A",
     "The passage belongs to the many ropes named in the sentence before, so the plural possessive "
     "is required. A singular possessive contradicts the tens of thousands just given, and a plain "
     "plural leaves the noun with no possessive form at all."),

 fss("F5",
     "The number of boats legged through the tunnel _____ every year after the tug was introduced, "
     "although it did not reach nothing for another two decades.",
     ["fell", "fall", "have fallen", "were falling"], "A",
     "&ldquo;The number&rdquo; is the singular subject, so a plural verb cannot stand, and the "
     "surrounding clause is in the simple past. The form that agrees in both number and tense is "
     "the simple past singular."),

 fss("F6",
     "Cut through gravel and lined with clay trodden until it was uniform, _____",
     ["the channel held water only so long as the lining stayed wet.",
      "engineers found that the channel held water only so long as the lining stayed wet.",
      "keeping the lining wet was what held the water in the channel.",
      "it was necessary to keep the lining wet if the channel was to hold water."], "A",
     "The opening phrase describes something cut and lined, and the only thing in the sentence that "
     "was cut and lined is the channel, so the channel must be the subject that follows. Beginning "
     "with the engineers, with the keeping, or with an empty subject leaves the description "
     "attached to something it cannot describe."),

 fss("F7",
     "The toll clerk, along with the two check clerks stationed further down the line, _____ a "
     "printed copy of the classification schedule at the start of each year.",
     ["was issued", "were issued", "have been issued", "are issued"], "A",
     "A phrase introduced by &ldquo;along with&rdquo; does not add to the subject, so the verb "
     "agrees with the single toll clerk. The plural forms treat the check clerks as though they "
     "were part of the subject, and the present-tense forms clash with the past narration."),

 fss("F8",
     "The advantage of a fly boat lay in changing horses at every stage, working through the night, "
     "and _____ ahead of anything waiting at a lock.",
     ["taking its turn", "to take its turn", "it took its turn", "the taking of its turn"], "A",
     "The blank completes a list whose first two items are &ldquo;changing&rdquo; and "
     "&ldquo;working,&rdquo; so the third must take the same form. An infinitive, a full clause and "
     "a noun phrase each break the pattern the first two items establish."),

 fss("F9",
     "Standing open in the water and held back by nothing but a simple catch _____ the pairs of "
     "gates that limit how much a breach can empty.",
     ["are", "is", "was", "has been"], "A",
     "The sentence is inverted: the subject is &ldquo;the pairs of gates,&rdquo; which follows the "
     "verb and is plural, so the verb must be plural. Every singular form agrees with the "
     "participial phrase in front of it, which is not the subject."),

 # ------------------------------------------------------------ Transitions (9)
 trn("N1",
     "A canal company could cut a rate as far down as it liked; nothing in its Act set a floor. "
     "_____ it could not raise the rate on the traffic that stayed in order to pay for the cut, "
     "because that rate was already at the maximum the Act allowed.",
     ["However,", "Therefore,", "For example,", "Similarly,"], "A",
     "The first sentence grants a freedom and the second withdraws a related one, so the link is a "
     "contrast. Nothing in the freedom to cut rates causes the inability to raise them, so a "
     "conclusion word is wrong, and the second sentence is not an instance of the first."),

 trn("N2",
     "A pound drained in July can crack its clay lining beyond repair, and a cracked lining will "
     "not close again when the water comes back. _____ companies preferred to do their heavy "
     "repairs in winter and to refill a length as soon as the masons were clear of it.",
     ["Accordingly,", "Nevertheless,", "In contrast,", "For instance,"], "A",
     "The practice described in the second sentence follows directly from the danger set out in the "
     "first, which makes the relation causal. A concession or a contrast would require the practice "
     "to run against the danger, and it runs with it."),

 trn("N3",
     "Some canal words carry a meaning they have nowhere else. _____ a pound is not a weight or an "
     "enclosure but the level stretch of water lying between one lock and the next.",
     ["For example,", "By contrast,", "Consequently,", "Even so,"], "A",
     "The second sentence supplies a single instance of the general claim made in the first, which "
     "is what an example marker signals. The two sentences do not conflict, and the general claim "
     "does not cause the particular meaning of one word."),

 trn("N4",
     "The tug through the long tunnels brought a train of boats out at the far end in forty minutes "
     "instead of four hours. _____ it put an end to a job that had left men with ruined backs.",
     ["Moreover,", "Instead,", "In short,", "Otherwise,"], "A",
     "Both sentences describe benefits of the tug, and the second adds a further one, so an "
     "additive link is needed. The second is not a summary of the first and does not replace it "
     "with an alternative."),

 trn("N5",
     "A horse pulling a boat at three miles an hour leaves the banks very much as it found them. "
     "_____ a propeller driven fast enough to save a day on the run throws a wave against both "
     "sides that carries away a little clay every time.",
     ["By contrast,", "Likewise,", "Accordingly,", "Indeed,"], "A",
     "The two sentences set gentle haulage against damaging haulage, so the link must mark "
     "opposition. A word signalling similarity or agreement would tell the reader to expect the "
     "same effect from both, which is the reverse of what follows."),

 trn("N6",
     "Legging a boat through a two-mile tunnel took four hours and paid badly. _____ crews carrying "
     "cheap cargo went on doing it for twenty years after the tug appeared, because the tug's charge "
     "was more than their freight would bear.",
     ["Even so,", "As a result,", "In other words,", "For instance,"], "A",
     "The second sentence reports crews continuing with a practice the first has just made "
     "unattractive, so the link must be concessive. A result marker would claim that the hardship "
     "caused the crews to persist, which reverses the logic."),

 trn("N7",
     "A boat entering the trough of an aqueduct pushes aside exactly its own weight of water, and "
     "the displaced water runs out at the ends. _____ the traffic crossing the structure has no "
     "bearing at all on what the piers beneath it must carry.",
     ["In other words,", "By contrast,", "Nevertheless,", "Meanwhile,"], "A",
     "The second sentence restates the consequence of the first in plainer terms rather than adding "
     "new information, which is what a restatement marker signals. There is no opposition between "
     "the two sentences and no shift to a different time."),

 trn("N8",
     "A gauging table let a clerk read a cargo's weight off the side of a boat without opening a "
     "single hold. _____ the classification schedule let him fix a rate without inspecting the "
     "goods, provided the boatman's declaration was honest.",
     ["Similarly,", "However,", "As a result,", "In fact,"], "A",
     "Both sentences describe a document that spared the clerk a direct inspection, so the link "
     "marks a parallel. The second is neither an objection to the first nor something the first "
     "brings about."),

 trn("N9",
     "Subscription lists for new canals filled within hours of opening in 1792, sometimes before a "
     "route had been surveyed at all. _____ a third of the companies authorised in those years had "
     "not cut a yard of channel by 1797.",
     ["As a result,", "For instance,", "By contrast,", "In addition,"], "A",
     "Money subscribed to unsurveyed routes is what produced the failures reported next, so the "
     "link is causal. The failure figure is not an instance of a list filling quickly, and it "
     "follows from the first sentence rather than standing against it."),

 # ------------------------------------------------------ Rhetorical Synthesis (9)
 syn("R1",
     ["A canal company's Act fixed a maximum toll for each class of goods.",
      "Coal and limestone were placed in the lowest classes.",
      "Manufactured goods paid several times the coal rate over the same distance.",
      "In 1838 one company carried 214,000 tons of coal and 16,000 tons of manufactured goods.",
      "Manufactured goods brought the company more toll income in 1838 than stone, sand and lime "
      "did."],
     "emphasise how much a small tonnage could contribute to the company's income.",
     ["Although manufactured goods came to only 16,000 tons in 1838 against 214,000 tons of coal, "
      "they brought the company more toll income that year than stone, sand and lime did.",
      "A canal company's Act fixed a maximum toll for each class of goods, and coal and limestone "
      "were placed in the lowest classes.",
      "Manufactured goods paid several times the coal rate over the same distance.",
      "In 1838 one company carried 214,000 tons of coal, and coal and limestone were in the lowest "
      "classes."], "A",
     "The goal asks for the contrast between a small tonnage and a large contribution, and only one "
     "option sets the 16,000 tons beside the 214,000 and then reports the income. The others "
     "restate notes about how the classes were set without ever reaching the income at all."),

 syn("R2",
     ["A towpath changes banks wherever the ground requires it.",
      "At an ordinary bridge the boatman must cast off the line, lead the horse across and hitch "
      "it again.",
      "The boat carries its way while the line is off, so a single-handed boatman must leave the "
      "tiller.",
      "A turnover bridge takes the towpath over the arch and back beneath itself on the far bank.",
      "The towline stays attached throughout the crossing of a turnover bridge."],
     "explain the problem that the turnover bridge was designed to solve.",
     ["Because an ordinary crossing meant casting off the line and leaving the tiller while the "
      "boat carried its way, the turnover bridge was built to take the path over the arch and back "
      "beneath itself so that the line never had to come off.",
      "A towpath changes banks wherever the ground requires it, and a turnover bridge takes the "
      "path over the arch and back beneath itself on the far bank.",
      "At an ordinary bridge the boatman must cast off the line, lead the horse across and hitch it "
      "again.",
      "The towline stays attached throughout the crossing of a turnover bridge, which takes the "
      "path over the arch and back beneath itself."], "A",
     "Explaining the problem the design solves requires both the difficulty at an ordinary bridge "
     "and the feature that removes it, and only one option states the difficulty and then the "
     "remedy. Two options describe the turnover bridge without naming any problem, and one names "
     "the difficulty without connecting it to the design."),

 syn("R3",
     ["A canal on an embankment stands several feet above the valley beside it.",
      "A breach in the lining can empty a mile of channel within an hour.",
      "Companies could not prevent every breach.",
      "Pairs of gates were hung at intervals along the embanked lengths and held open by a catch.",
      "A rush of water towards a breach slams the gates shut and confines the loss to one length."],
     "explain the purpose of the gates hung along the embanked lengths.",
     ["Because a breach could not be prevented and would empty a mile of channel within an hour, "
      "gates were hung at intervals to be slammed shut by the rush itself and confine the loss to a "
      "single length.",
      "A canal on an embankment stands several feet above the valley beside it, and a breach can "
      "empty a mile of channel within an hour.",
      "Pairs of gates were hung at intervals along the embanked lengths and held open by a catch.",
      "Companies could not prevent every breach, and a canal on an embankment stands several feet "
      "above the valley beside it."], "A",
     "The purpose of the gates is to limit a loss that cannot be prevented, so the answer must join "
     "the impossibility of prevention to the confinement of the damage; only one option does both. "
     "The rest describe the embankment or the gates themselves without saying what they are for."),

 syn("R4",
     ["A frozen canal stopped all traffic on the line.",
      "The company's ice boat was short, iron-shod and drawn by a team of horses.",
      "A dozen men stood along a rail down the centre of the boat and rocked it in time as it "
      "went.",
      "The rocking made the hull rise and fall as the boat moved forward.",
      "The channel broken was wider than the boat's own beam."],
     "explain how the ice boat came to break a channel wider than itself.",
     ["Rocked in time by a dozen men standing along a rail, the hull rose and fell as the boat went "
      "forward, and the channel it broke was wider than its own beam.",
      "A frozen canal stopped all traffic, and the company's ice boat was short, iron-shod and "
      "drawn by a team of horses.",
      "The channel broken by the ice boat was wider than the boat's own beam.",
      "A dozen men stood along a rail down the centre of the ice boat, which was short, iron-shod "
      "and drawn by a team of horses."], "A",
     "The goal is the mechanism, so the answer must link the rocking to the rise and fall of the "
     "hull and then to the width of the channel; only one option carries that chain through. One "
     "option states the width without any cause, and the others describe the boat without "
     "explaining anything."),

 syn("R5",
     ["Weighing a loaded boat was not practicable.",
      "Each new hull was floated empty and then loaded with known weights a ton at a time.",
      "Its freeboard was recorded at every step, producing a table for that particular boat.",
      "Copies of the table were kept at every toll house on the line.",
      "A clerk measured the freeboard at a gauging stone and read the weight off the table."],
     "explain how a clerk could charge by weight without ever weighing a cargo.",
     ["Because each hull had already been calibrated against known weights, a clerk needed only to "
      "measure its freeboard at the gauging stone and read the cargo's weight off that boat's own "
      "table.",
      "Weighing a loaded boat was not practicable, and copies of the table were kept at every toll "
      "house on the line.",
      "Each new hull was floated empty and then loaded with known weights a ton at a time.",
      "A clerk measured the freeboard at a gauging stone, and the table for that boat was kept at "
      "every toll house."], "A",
     "The explanation needs the calibration done beforehand and the single measurement made "
     "afterwards, and only one option puts the two together as cause and method. The others give "
     "one half of the procedure or pair it with a detail about where the tables were kept."),

 syn("R6",
     ["Dredged mud was tipped over the offside of the mud boat onto the field side of the bank.",
      "A century of tipping raised the offside of many canals into a low ridge.",
      "Hawthorn seeded itself along the new ridge.",
      "The water came to sit visibly above the meadow beyond the bank.",
      "Several companies were sued by neighbouring farmers over the raised bank."],
     "explain why farmers went to law against the canal companies.",
     ["A century of mud tipped over the offside had raised the bank into a ridge that left the "
      "water sitting visibly above the meadow beyond, and several companies were sued by "
      "neighbouring farmers over it.",
      "Dredged mud was tipped over the offside of the mud boat onto the field side of the bank, "
      "where hawthorn seeded itself along the new ridge.",
      "Hawthorn seeded itself along the ridge raised by a century of tipping.",
      "Several companies were sued by neighbouring farmers, and the water came to sit visibly above "
      "the meadow beyond the bank."], "A",
     "A reason for the lawsuits requires the raised bank and its effect on the neighbouring land to "
     "be given as what the farmers complained of, which one option does in a single causal "
     "sentence. Another mentions the suits and the water level but merely places them side by side, "
     "and the rest are about hawthorn."),

 syn_given("R7",
     ["A pound is the level stretch of water between one lock and the next.",
      "A short pound can be drawn down several inches by a single boat.",
      "The Marsh pound is 600 metres long.",
      "The Marsh pound must be refilled from above before a second boat can pass."],
     "The student wants to explain the consequence of the Marsh pound's length to an audience "
     "already familiar with canal terminology.",
     ["At only 600 metres, the Marsh pound is drawn down several inches by a single boat and must "
      "be refilled from above before a second can pass.",
      "A pound is the level stretch of water between one lock and the next, and the Marsh pound is "
      "600 metres long.",
      "A short pound, meaning a level stretch of water between two locks, can be drawn down several "
      "inches by a single boat.",
      "The Marsh pound is 600 metres long and is a level stretch of water between one lock and the "
      "next."], "A",
     "An audience that already knows the terminology does not need the term defined, so the answer "
     "must spend its words on the length and what follows from it. Every other option gives over "
     "part of the sentence to a definition the stated audience already has."),

 syn_given("R8",
     ["Legging was the practice of moving a boat through a tunnel by walking along its walls.",
      "The Braddon tunnel is 2,800 metres long.",
      "Legging the Braddon tunnel took about four hours.",
      "A steam tug introduced in 1863 brought a train of boats through in forty minutes."],
     "The student wants to emphasise the scale of the time saved at the Braddon tunnel to an "
     "audience already familiar with legging.",
     ["The 2,800-metre Braddon tunnel took about four hours to leg, but the steam tug introduced in "
      "1863 brought a train of boats through in forty minutes.",
      "Legging, the practice of moving a boat through a tunnel by walking along its walls, took "
      "about four hours at the Braddon tunnel.",
      "The Braddon tunnel is 2,800 metres long, and legging was the practice of moving a boat "
      "through a tunnel by walking along its walls.",
      "A steam tug was introduced at the Braddon tunnel in 1863, and the tunnel is 2,800 metres "
      "long."], "A",
     "Emphasising the saving means putting the four hours and the forty minutes in the same "
     "sentence, which only one option does. Two options spend their words defining legging for an "
     "audience said to know it already, and one gives the tug without any time to compare."),

 syn_given("R9",
     ["A compensation toll was paid by one company to another on traffic crossing a junction.",
      "The Wenholme and Ashby companies met at Norbrook.",
      "The Ashby company paid the Wenholme company threepence a ton at Norbrook.",
      "The payment was made on every ton that crossed, whether or not it had used the Wenholme "
      "line."],
     "The student wants to specify the terms of the arrangement at Norbrook to an audience already "
     "familiar with compensation tolls.",
     ["At Norbrook the Ashby company paid the Wenholme company threepence on every ton crossing the "
      "junction, whether or not it had used the Wenholme line.",
      "A compensation toll was paid by one company to another on traffic crossing a junction, and "
      "the Wenholme and Ashby companies met at Norbrook.",
      "The Wenholme and Ashby companies met at Norbrook, where a compensation toll of the usual "
      "kind was in force.",
      "A compensation toll, paid by one company to another on traffic crossing a junction, was paid "
      "at Norbrook by the Ashby company."], "A",
     "Specifying the terms means naming the payer, the payee, the rate and the condition, and only "
     "one option supplies all four. The others use their words on a definition the stated audience "
     "already has, or leave the rate out entirely."),
]


# ---------------------------------------------------------------------- DROPPED
# Topics screened against ../rw_authored_corpus.json and abandoned rather than
# reworded, because the bank already holds the same subject. Recorded so a
# later build does not spend the effort again.
DROPPED = [
    ("water accounting per lockage", "rw_test16 T6 already states that every passage sends a "
     "lockful of water down to the level below"),
    ("side ponds that recover part of a lockful", "same rw_test16 T6 passage"),
    ("boat lifts and inclined planes", "rw_test16 T6 contrasts an inclined plane with a flight of "
     "locks"),
    ("the timing of a long lock flight", "rw_test16 T6"),
    ("Pontcysyllte and the cast-iron trough carried high above a river",
     "rw_test16 R1 is a Rhetorical Synthesis item built on exactly that aqueduct"),
    ("Roman aqueducts", "rw_test8 T5"),
    ("limekilns loaded at a canal wharf", "rw_test19 W11 describes the loading of a lime kiln"),
    ("cargo handled at competing quays, as a data table", "rw_test16 E9 is that table"),
    ("the transit shed on a quay", "rw_test16 B6"),
    ("lighterage: cargo taken ashore in barges from a ship at anchor", "rw_test16 N9"),
    ("a lock keeper drawing the upper paddles before dawn", "rw_test10 B11"),
    ("lock dimensions fixing the size of the boats, and hulls grounding on silt", "rw_test10 W14"),
    ("one horse outpulling what a road could carry", "rw_test15 B10 makes that comparison"),
    ("the collapse of freight rates on a newly opened canal", "rw_test13 C5"),
    ("half-tide basins and impounded dock water", "rw_test16 R9"),
    ("maintenance dredging returning to the same lengths of an estuary", "rw_test19 T3"),
    ("the scheduling and overrun of a harbour-mouth dredging contract", "rw_test11 F3"),
    ("weirs on a river and the fish passes cut through them", "rw_test19 F5, W12 and B12"),
    ("a neither/nor agreement item built on volunteers", "the same construction is already used in "
     "rw_test11 F1, rw_test13 F1, rw_test16 F1 and rw_test16 F7"),
]
