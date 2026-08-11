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
     "A loaded boat seventy feet long cannot be turned round in a channel cut wide enough only to "
     "let two of them pass. Companies therefore widened the line at intervals into shallow bays "
     "just long enough to swing a bow into, and a boatman who ran past one had to work on for miles "
     "before he could turn. Knowing where those bays lay was _____ knowledge rather than a nicety "
     "of the trade.",
     ["indispensable", "ornamental", "outdated", "theoretical"], "A",
     "The text describes a boatman who misses a bay as losing miles of work, which makes the "
     "knowledge something he cannot do without. A word meaning merely decorative or no longer "
     "current sits against the practical consequence the passage has just spelled out."),

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
     "The man who walked a fixed beat of bank every day, watching for the soft place in the puddle "
     "before it could become a hole and known to the company as a _____ paid by the mile he covered "
     "rather than by the hour.",
     ["lengthsman, was", "lengthsman was", "lengthsman; was", "lengthsman: was"], "A",
     "The supplement beginning &ldquo;watching for the soft place&rdquo; is opened with a comma and "
     "must be closed with one before the sentence reaches its verb. Leaving the mark out strands "
     "the opening comma, and neither a semicolon nor a colon may stand between a subject and its "
     "verb."),

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
     "The slots cut into the masonry at each end of a pound &mdash; plank grooves, in the company's "
     "_____ what let a single length be drained for a winter's repairs without emptying the miles "
     "on either side of it.",
     ["language &mdash; were", "language, were", "language were", "language; were"], "A",
     "The supplement is opened with a dash and must be closed with a dash, since the marks at "
     "either end of a parenthetical have to match. A comma or a semicolon leaves the opening dash "
     "unanswered, and dropping the mark altogether runs the supplement into the predicate."),

 bnd("B6",
     "The two operations are not the same and are not costed the same way. Weed cutting removes "
     "what has grown in the water this _____ takes out what has settled on the bed over many.",
     ["season; dredging", "season, dredging", "season dredging", "season: dredging"], "A",
     "The blank falls between two complete statements that are closely paired, and a semicolon is "
     "the mark for exactly that. A comma between them is a splice, no mark at all fuses them, and a "
     "colon would announce that the second explains the first when it instead sets a contrasting "
     "case beside it."),

 bnd("B7",
     "The boy who walked the horse the whole length of a day's run and opened the paddles at every "
     "lock while the steerer stayed at the _____ a share of the trip money rather than a wage.",
     ["tiller took", "tiller, took", "tiller; took", "tiller: took"], "A",
     "Everything from &ldquo;The boy&rdquo; to &ldquo;the tiller&rdquo; is a single long subject "
     "and &ldquo;took&rdquo; is its verb, and no punctuation belongs between a subject and its verb "
     "however far the two are driven apart."),

 bnd("B8",
     "Ice forming in the joints of a lock wall lifts every stone a fraction each _____ the coping "
     "has to be taken up and reset long before the stone itself is anywhere near worn away.",
     ["winter, and", "winter and", "winter; and", "winter: and"], "A",
     "Two complete statements are joined here by &ldquo;and,&rdquo; and a comma belongs in front of "
     "the conjunction when the clauses either side of it are both independent and this long. A "
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
     "Two of the tunnels on the northern section _____ wide enough for boats to pass one another "
     "inside, and traffic through the rest had to be worked one way at a time.",
     ["were", "was", "has been", "is"], "A",
     "The subject is the two tunnels, which is plural, so the verb must be plural; the singular "
     "noun in the phrase that follows describes where they are and cannot govern it. Every singular "
     "form agrees with the section instead of with the tunnels the sentence is about."),

 fss("F2",
     "No boat moved on the line for three weeks that January: the summit had _____ hard enough for "
     "a cart to be driven across it below the top lock.",
     ["frozen", "froze", "freezed", "freezing"], "A",
     "The auxiliary &ldquo;had&rdquo; requires the past participle of the verb, which is "
     "&ldquo;frozen.&rdquo; The simple past cannot follow &ldquo;had,&rdquo; the regular form is "
     "not an English word at all, and the present participle would need a form of "
     "&ldquo;be&rdquo; in front of it rather than &ldquo;had.&rdquo;"),

 fss("F3",
     "The wharfinger _____ ledgers survive at Norbrook recorded the name of every boat that tied up "
     "at the wharf and the hour at which it left again.",
     ["whose", "who&rsquo;s", "who", "which"], "A",
     "The blank stands in front of a noun that belongs to the wharfinger, so a possessive relative "
     "pronoun is needed. The contraction of &ldquo;who is&rdquo; is not a possessive, the subject "
     "form cannot take a noun after it, and the pronoun for things cannot refer to a person."),

 fss("F4",
     "The company set a stone at every mile along the towpath and reckoned its charges from them. A "
     "boat that passed one paid for the mile behind it, so the _____ positions settled what a haul "
     "cost as surely as the cargo did.",
     ["stones&rsquo;", "stone&rsquo;s", "stones", "stones&rsquo;s"], "A",
     "The positions belong to the many stones set out in the sentence before, so the plural "
     "possessive is required. A singular possessive contradicts the stone at every mile, and a "
     "plain plural gives the noun no possessive form at all."),

 fss("F5",
     "Had the committee carried the line over the ridge in an open cutting instead of boring it "
     "through, the works _____ two years sooner and no crew would ever have had to leg a boat at "
     "all.",
     ["would have been finished", "would be finished", "will have been finished",
      "had been finished"], "A",
     "The opening clause imagines a past that did not happen, so the main clause has to name its "
     "unrealised past consequence, which takes the conditional perfect. A present conditional "
     "points at now rather than at the year of the works, and neither a future nor a past perfect "
     "can carry the consequence of a condition contrary to fact."),

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
     "The hand cranes along the wall of every warehouse on the arm _____ geared so low that a "
     "single man could lift a ton of grain to the third floor without help.",
     ["are", "is", "has been", "was"], "A",
     "The subject is the cranes, which is plural; &ldquo;every warehouse&rdquo; sits inside a "
     "prepositional phrase saying where the cranes are and cannot govern the verb. Each singular "
     "form agrees with that phrase rather than with the true subject."),

 fss("F8",
     "The advantage of a fly boat lay in changing horses at every stage, working through the night, "
     "and _____ ahead of anything waiting at a lock.",
     ["taking its turn", "to take its turn", "it took its turn", "the taking of its turn"], "A",
     "The blank completes a list whose first two items are &ldquo;changing&rdquo; and "
     "&ldquo;working,&rdquo; so the third must take the same form. An infinitive, a full clause and "
     "a noun phrase each break the pattern the first two items establish."),

 fss("F9",
     "Hanging on a hook inside the cabin door of every working boat _____ the windlasses with which "
     "the crew wound up the paddles at each lock they came to.",
     ["are", "is", "was", "has been"], "A",
     "The sentence is inverted: the subject is &ldquo;the windlasses,&rdquo; which follows the verb "
     "and is plural, so the verb must be plural. Every singular form agrees with the participial "
     "phrase in front of it, which is not the subject."),

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
     "A company that dammed a hill stream for its reservoirs took water the mills below it had used "
     "for centuries, and its Act obliged it to send a fixed flow down the old channel every day of "
     "the year. _____ the water a reservoir could actually put into the summit was always less than "
     "the water it held.",
     ["Accordingly,", "Nevertheless,", "In contrast,", "For instance,"], "A",
     "The shortfall in the second sentence follows directly from the obligation stated in the "
     "first, so the link is causal. A concession or a contrast would require the two to pull "
     "against each other, and the second sentence is a consequence rather than an instance."),

 trn("N3",
     "A canal company numbered every bridge on its line from one end to the other, and the boatmen "
     "took the numbers up in preference to the names of the places they passed. _____ a boat "
     "reported as lying below bridge ninety-four was somewhere no map named and every crew on the "
     "line could find.",
     ["For example,", "By contrast,", "Consequently,", "Even so,"], "A",
     "The second sentence gives one instance of the practice described in the first, which is what "
     "an example marker announces. The two do not conflict, and the numbering of the bridges is not "
     "what makes the map silent."),

 trn("N4",
     "The tug through the long tunnels brought a train of boats out at the far end in forty minutes "
     "instead of four hours. _____ it put an end to a job that had left men with ruined backs.",
     ["Moreover,", "Instead,", "In short,", "Otherwise,"], "A",
     "Both sentences describe benefits of the tug, and the second adds a further one, so an "
     "additive link is needed. The second is not a summary of the first and does not replace it "
     "with an alternative."),

 trn("N5",
     "A cabin boat carried its crew's home along with it, and the family slept aboard wherever the "
     "day's work happened to end. _____ a day boat had no cabin at all: it was an open box worked "
     "between two wharves by men who went home at night, and it never left the few miles it was "
     "built for.",
     ["By contrast,", "Likewise,", "Accordingly,", "Indeed,"], "A",
     "The two sentences set a boat that is a dwelling against a boat that is not, so the link must "
     "mark opposition. A word signalling similarity would tell the reader to expect the day boat to "
     "resemble the cabin boat, which is the reverse of what follows."),

 trn("N6",
     "Legging a boat through a two-mile tunnel took four hours and paid badly. _____ crews carrying "
     "cheap cargo went on doing it for twenty years after the tug appeared, because the tug's charge "
     "was more than their freight would bear.",
     ["Even so,", "As a result,", "In other words,", "For instance,"], "A",
     "The second sentence reports crews continuing with a practice the first has just made "
     "unattractive, so the link must be concessive. A result marker would claim that the hardship "
     "caused the crews to persist, which reverses the logic."),

 trn("N7",
     "The shafts sunk from the hillside down to a canal tunnel were driven to get the spoil out "
     "while the tunnel was being cut, and were left open afterwards only because capping them would "
     "have cost money. _____ the openings that later carried off a tug's smoke were put there for a "
     "reason that had nothing to do with smoke.",
     ["In other words,", "By contrast,", "Nevertheless,", "Meanwhile,"], "A",
     "The second sentence puts the point of the first in plainer terms rather than adding anything "
     "new to it, which is what a restatement marker signals. There is no opposition between the two "
     "and no move to a different time."),

 trn("N8",
     "A gauging table let a clerk read a cargo's weight off the side of a boat without opening a "
     "single hold. _____ the classification schedule let him fix a rate without inspecting the "
     "goods, provided the boatman's declaration was honest.",
     ["Similarly,", "However,", "As a result,", "In fact,"], "A",
     "Both sentences describe a document that spared the clerk a direct inspection, so the link "
     "marks a parallel. The second is neither an objection to the first nor something the first "
     "brings about."),

 trn("N9",
     "Goods lay in open boats overnight at every wharf on the line, and a parish constable had no "
     "authority a yard beyond his own parish. _____ several companies obtained Acts appointing "
     "constables of their own, who could stop and search a boat anywhere between one end of the "
     "navigation and the other.",
     ["As a result,", "For instance,", "By contrast,", "In addition,"], "A",
     "Goods left unguarded where no officer's authority reached are what produced the remedy "
     "described next, so the link is causal. The companies' own constables are not an instance of a "
     "parish constable's limits, and the second sentence follows from the first rather than "
     "standing against it."),

 # ------------------------------------------------------ Rhetorical Synthesis (9)
 syn("R1",
     ["Imported goods paid customs duty at the moment they were landed.",
      "A bonded warehouse held goods under a lock to which the Customs kept the key.",
      "Duty on goods held in bond fell due only when they were taken out again.",
      "A merchant could therefore hold a year's stock without finding the duty on it.",
      "The canal company charged rent for the space and moved the goods to and from the wharf."],
     "explain why a merchant would choose to keep goods in a bonded warehouse.",
     ["Because duty on goods in bond fell due only when they were taken out, a merchant could hold "
      "a year's stock without having to find the duty on any of it.",
      "A bonded warehouse held goods under a lock to which the Customs kept the key, and the canal "
      "company charged rent for the space.",
      "Imported goods paid customs duty at the moment they were landed.",
      "The canal company moved the goods to and from the wharf and charged rent for the space they "
      "occupied."], "A",
     "The reason for using such a warehouse is the deferral of the duty, so the answer has to state "
     "when the duty fell due and what that let the merchant do. The others describe the lock, the "
     "rent or the ordinary rule on landing without ever reaching the advantage."),

 syn("R2",
     ["A carrier's own horses worked fixed stages and were stabled at the ends of each one.",
      "Beyond those stages a carrier had no animal of his own.",
      "Innkeepers along the line kept horses and drivers for hire by the trip.",
      "A hired horse and its driver together were known as a horse-marine.",
      "Traffic running only occasionally beyond a carrier's own stages was worked this way."],
     "explain the circumstances in which a carrier would take a horse-marine.",
     ["Because a carrier's own horses worked only his fixed stages, traffic that went beyond them "
      "occasionally was worked instead by a hired horse and driver taken by the trip.",
      "A hired horse and its driver together were known as a horse-marine, and innkeepers along the "
      "line kept both for hire.",
      "A carrier's own horses worked fixed stages and were stabled at the ends of each one.",
      "Innkeepers along the line kept horses and drivers for hire by the trip, and beyond his own "
      "stages a carrier had no animal of his own."], "A",
     "The question asks when the hire happened, so the answer must join the limit of the carrier's "
     "own stages to the occasional traffic that went past it. Two options define the term or "
     "describe the innkeepers without naming an occasion, and one gives only the stages."),

 syn("R3",
     ["Working boats were painted with roses and with castles on their cabin doors and water cans.",
      "The pattern appears on boats from the 1860s onward.",
      "Some writers trace it to the fairground and clock-dial painting of the same period.",
      "Others argue that it grew out of the boatyards' own house styles.",
      "No boat painted before 1858 has been found carrying the pattern."],
     "emphasise the limits of the evidence bearing on where the pattern came from.",
     ["No boat painted before 1858 has been found carrying the pattern at all, so neither the "
      "fairground account of its origin nor the boatyard account can be tested against an earlier "
      "example.",
      "Working boats were painted with roses and with castles on their cabin doors and water cans, "
      "and the pattern appears from the 1860s onward.",
      "Some writers trace the pattern to fairground and clock-dial painting of the same period.",
      "Others argue that the pattern grew out of the boatyards' own house styles, which were "
      "established well before the 1860s."], "A",
     "Emphasising the limits of the evidence means saying what the evidence cannot settle, and only "
     "one option names the missing early boats and draws the consequence for both explanations. The "
     "rest simply report the pattern or one side of the argument."),

 syn("R4",
     ["Falling freight rates after 1850 left many boatmen unable to keep a house ashore.",
      "Whole families moved into cabins measuring about eight feet by seven.",
      "An Act of 1877 required every boat used as a dwelling to be registered.",
      "The registration stated the number of people who might lawfully sleep aboard.",
      "An inspector could board a registered boat and count those sleeping in it."],
     "explain what the Act of 1877 was intended to control.",
     ["Because whole families had moved into cabins of about eight feet by seven, the Act of 1877 "
      "made a boat used as a dwelling register the number who might lawfully sleep aboard, which an "
      "inspector could come and count.",
      "Falling freight rates after 1850 left many boatmen unable to keep a house ashore, and whole "
      "families moved into cabins measuring about eight feet by seven.",
      "An Act of 1877 required every boat used as a dwelling to be registered.",
      "An inspector could board a registered boat, whose registration stated the number of people "
      "who might lawfully sleep aboard."], "A",
     "What the Act controlled was overcrowding, so the answer must connect the size of the cabins "
     "to the registered limit and to the inspection that enforced it. One option gives the cause "
     "without the Act, and the others give the Act without what it was answering."),

 syn("R5",
     ["Locks on the northern canals were built about seven feet wide.",
      "Locks on the eastern navigations were built about fourteen feet wide.",
      "A boat built to pass a seven-foot lock will also pass a fourteen-foot one.",
      "A barge built for a fourteen-foot lock cannot pass a seven-foot one.",
      "A through route was open only to craft that could pass its narrowest lock."],
     "explain why the width of a single lock could govern a whole route.",
     ["Because a barge built for a fourteen-foot lock cannot pass a seven-foot one, a through route "
      "was open only to craft small enough for the narrowest lock anywhere along it.",
      "Locks on the northern canals were built about seven feet wide and those on the eastern "
      "navigations about fourteen.",
      "A boat built to pass a seven-foot lock will also pass a fourteen-foot one.",
      "A through route was open only to craft that could pass its narrowest lock, and the northern "
      "locks were about seven feet wide."], "A",
     "The governing fact is that the larger craft is excluded while the smaller is not, so the "
     "answer must state the asymmetry and then the consequence for a route. The others give the two "
     "widths, or the rule about the narrowest lock, without the asymmetry that produces it."),

 syn("R6",
     ["By 1900 several canal companies were carrying almost no traffic.",
      "Their reservoirs still gathered and held water off the hills.",
      "Towns below those hills were short of water.",
      "One such company sold its reservoirs to a municipal waterworks in 1902.",
      "The canal below them was left with no supply and closed within a decade."],
     "explain what the sale of 1902 meant for the canal itself.",
     ["Selling its reservoirs to the municipal waterworks in 1902 left the canal below them with no "
      "supply at all, and it closed within a decade.",
      "By 1900 several canal companies were carrying almost no traffic, though their reservoirs "
      "still gathered water off the hills.",
      "Towns below the hills were short of water, and one company sold its reservoirs to a "
      "municipal waterworks in 1902.",
      "Their reservoirs still gathered and held water off the hills, which the towns below them "
      "needed."], "A",
     "The question asks about the effect on the canal, and only one option carries the sale through "
     "to the loss of supply and the closure. The others explain why the sale was attractive or "
     "describe the reservoirs, stopping short of what became of the waterway."),

 syn_given("R7",
     ["An iron trough carrying a canal expands as it warms and contracts as it cools.",
      "The plates of the Braddon trough are bolted to one another at flanged joints.",
      "Every joint at Braddon is bedded in flannel dipped in white lead.",
      "The bedding lets the plates move slightly against one another without letting water "
      "through."],
     "The student wants to explain how the Braddon trough can move without leaking, to an audience "
     "already familiar with iron aqueducts.",
     ["The flanged joints of the Braddon trough are bedded in flannel dipped in white lead, which "
      "lets its plates move slightly against one another without letting water through.",
      "An iron trough carrying a canal expands as it warms and contracts as it cools, and the "
      "plates of the Braddon trough are bolted at flanged joints.",
      "The plates of the Braddon trough are bolted to one another at flanged joints.",
      "An iron trough expands as it warms, and every joint at Braddon is bedded in flannel dipped "
      "in white lead."], "A",
     "An audience that already knows iron aqueducts does not need to be told that iron expands, so "
     "the answer must spend its words on the bedding and what it permits. Every other option gives "
     "part of the sentence over to the expansion the stated audience takes for granted."),

 syn_given("R8",
     ["A stop lock stands where one company's line meets another's.",
      "The Wenholme summit lies four inches above the Ashby line at Norbrook.",
      "The stop lock at Norbrook has a fall of four inches.",
      "Its purpose is to keep the Wenholme company's water from running into the Ashby line."],
     "The student wants to explain the purpose of the unusually small fall at Norbrook, to an "
     "audience already familiar with stop locks.",
     ["The Norbrook lock falls only the four inches by which the Wenholme summit lies above the "
      "Ashby line, so that Wenholme water cannot run away into it.",
      "A stop lock stands where one company's line meets another's, and the one at Norbrook has a "
      "fall of four inches.",
      "The stop lock at Norbrook has a fall of four inches, and the Wenholme summit lies four "
      "inches above the Ashby line.",
      "Its purpose is to keep the Wenholme company's water from running into the Ashby line, where "
      "one company's line meets another's."], "A",
     "The small fall is explained by matching it to the difference in level and naming what that "
     "prevents, and only one option makes that connection. One option defines a stop lock for an "
     "audience said to know what one is, and another sets the two four-inch figures side by side "
     "without saying they are the same four inches."),

 syn_given("R9",
     ["Every boat was floated empty and then loaded with known weights a ton at a time.",
      "Its freeboard was recorded at each step, giving a table for that hull alone.",
      "A copy of the table was kept at every toll house on the line.",
      "A clerk measured the freeboard at the toll house and read the weight from the table."],
     "The student wants to explain how a toll clerk arrived at the weight of a cargo, to an "
     "audience already familiar with gauging.",
     ["The clerk measured a boat's freeboard at the toll house and read its weight from the table "
      "drawn up when that hull had been loaded with known weights.",
      "Every boat was floated empty and then loaded with known weights a ton at a time, and its "
      "freeboard was recorded at each step.",
      "A copy of the table for each hull was kept at every toll house on the line.",
      "Its freeboard was recorded at each step, giving a table for that hull alone, and a copy was "
      "kept at every toll house."], "A",
     "The question is about what the clerk did, so the answer must have him measuring and reading. "
     "The others describe the calibration or the filing of the tables and never reach the toll "
     "house counter."),
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
