#!/usr/bin/env python3
"""
Reading & Writing authored for Test 20.

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

Topics are drawn from the fifteen subject territories assigned to Test 20 so
that the three tests being built in parallel stay apart: mining and mineral
extraction; gas, electricity supply and public utilities; telegraphy and
communication networks; urban transit and street systems; foundries, alloys and
metallurgy; tunnelling and underground engineering; Byzantine and late-antique
history; ants, termites and social insects; particle physics and detectors;
oral epic poetry and formulaic composition; insurance, actuarial practice and
risk; coastal erosion and sediment transport; game theory and strategic
behaviour; bats and echolocation; immunology and vaccines.

Every candidate topic was screened against content-pool/rw_authored_corpus.json
(1,052 banked passages) by keyword and by 5-gram / Jaccard overlap before any
passage was written; screen_topics.py in this directory is that check. Its
keyword matcher works on word boundaries rather than raw substrings, because an
earlier build had "quire" match *required* and "loom" match *bloom* and threw
away clean topics on false collisions. The collisions it found are recorded in
DROPPED at the foot of this file and those topics were abandoned rather than
paraphrased around.

Block counts (fixed by the assembler's quota, 3 modules x 27):
    Words in Context 15, Text Structure and Purpose 6,
    Central Ideas and Details 6, Command of Evidence 9, Inferences 6,
    Boundaries 12, Form, Structure, and Sense 9, Transitions 9,
    Rhetorical Synthesis 9                                        = 81
"""

SOURCE = "AUTHORED-T20"
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
     "In room-and-pillar working the men cut chambers out of a coal seam and leave a block of the "
     "seam standing at intervals to carry the roof. As much as half the coal in a panel may be "
     "locked up in those blocks, and they can be robbed on the retreat only where the roof is "
     "allowed to come down behind the men. Judged against the coal actually present, the method is "
     "therefore _____.",
     ["wasteful", "protective", "exhaustive", "unpredictable"], "A",
     "Half the seam left standing in pillars, recoverable only where the roof is dropped, is coal "
     "the method never takes, so the blank names a cost in material left underground. The "
     "'exhaustive' option claims the opposite, that the working removes everything the seam holds."),

 wic("W2",
     "A generating station is built for the highest demand it will ever have to meet, and that peak "
     "may last an hour on a winter evening. For much of the rest of the year a good deal of the "
     "plant stands still. The cost of each unit sold therefore depends less on the price of fuel "
     "than on how _____ the machinery is, which is why utilities have long offered cheap night "
     "tariffs.",
     ["fully used", "newly built", "idle", "widely admired"], "A",
     "Plant that stands still for most of the year spreads its cost over few units, and the cheap "
     "night tariff exists to keep it working, so the blank names how much of the time the machinery "
     "earns. The 'idle' option names the very condition the tariff is designed to reduce."),

 wic("W3",
     "A single wire between two cities could at first carry one message at a time in one direction. "
     "Duplex working balanced the sending instrument against an artificial line so that an "
     "operator's own signals cancelled at his own receiver and only the distant operator's reached "
     "it. The capacity of the wire was thereby _____ without a metre of new copper being strung.",
     ["doubled", "restored", "measured", "protected"], "A",
     "The arrangement lets each end send while the other is sending, so one wire now carries two "
     "messages where it carried one, and no new line is built. The 'restored' option would mean the "
     "wire had lost a capacity it once held, which the passage never suggests."),

 wic("W4",
     "Buses on a frequent route do not stay evenly spaced. A bus running slightly late finds more "
     "passengers waiting at the next stop, which delays it further, while the bus behind it finds "
     "fewer and gains. Left alone the pattern is _____: small differences in spacing grow until "
     "vehicles arrive in pairs with a long gap behind them.",
     ["self-reinforcing", "self-correcting", "imperceptible", "seasonal"], "A",
     "Each delay makes the next delay larger and the gap widens without anything further being "
     "done, so the blank names a process that feeds on itself. The 'self-correcting' option "
     "describes the opposite, a spacing that would recover on its own."),

 wic("W5",
     "Hammering a copper sheet makes it harder and stiffer, and past a certain point it will crack "
     "rather than bend. Heating the sheet to a dull red and letting it cool allows the strained "
     "grain structure to re-form, and the metal becomes workable again. A coppersmith raising a "
     "bowl from a flat disc therefore has to _____ the hammering several times before the shape is "
     "finished.",
     ["interrupt", "abandon", "conceal", "accelerate"], "A",
     "The metal can be worked again only after it has been heated and allowed to cool, so the "
     "hammering must stop and then resume, repeatedly. The 'abandon' option would leave the bowl "
     "unmade, whereas the passage has the work carried through to a finished shape."),

 wic("W6",
     "A tunnel boring machine cuts rock at the head and erects a ring of concrete segments "
     "immediately behind it, so that the ground is supported before it has had time to move. "
     "Drill-and-blast advances in rounds, and the newly exposed rock stands bare until a lining "
     "crew reaches it. The machine's real advantage is thus not speed alone but the _____ of "
     "excavation and support.",
     ["simultaneity", "separation", "expense", "novelty"], "A",
     "The machine places its lining directly behind the cutting head, so the two operations happen "
     "at the same moment rather than one after the other. The 'separation' option names the "
     "arrangement the passage attributes to the older method it is being contrasted with."),

 wic("W7",
     "The incendiary the Byzantine fleet pumped at enemy ships burned on water and could not be put "
     "out with it. The recipe was held by a small number of families and never set down in full; "
     "one emperor advised his son to tell foreign envoys only that an angel had brought it. By the "
     "time the city fell the formula had been _____, and no later account reproduces it.",
     ["forgotten", "published", "improved", "translated"], "A",
     "A recipe kept within a few families and deliberately never written down complete is one that "
     "can be lost, and the passage adds that no later account reproduces it. The 'published' option "
     "contradicts the secrecy the rest of the text describes."),

 wic("W8",
     "An army ant colony builds no nest. At the end of a day's march the workers link legs and "
     "hooked claws until the whole colony hangs as a mass the size of a football, with the queen "
     "and the brood inside it and galleries running through it. The structure goes up in an hour "
     "and comes down the next morning, so the colony's shelter is entirely _____.",
     ["provisional", "underground", "inherited", "decorative"], "A",
     "A shelter assembled in an hour out of the ants' own bodies and dismantled the following "
     "morning lasts no longer than the halt it serves. The 'underground' option is ruled out by a "
     "structure that hangs in the open air."),

 wic("W9",
     "A modern collider produces tens of millions of collisions a second, and no system could "
     "record them all. Fast electronics examine each event for a handful of coarse features and "
     "discard all but a few hundred, which are written to disk for later study. The physics such a "
     "detector can report is therefore limited by what its designers thought worth _____ in "
     "advance.",
     ["keeping", "measuring", "funding", "publishing"], "A",
     "The electronics throw nearly every event away and only the retained few hundred can ever be "
     "analysed, so the decision taken in advance is which events to save. The 'measuring' option "
     "misses that every event is examined briefly and only a few are preserved."),

 wic("W10",
     "A singer performing a long epic before an audience cannot pause to search for a phrase. The "
     "traditions that produced such poems supply ready-made word groups fitted to the recurring "
     "positions in the line, so that a hero can be given a name and a descriptive tag which "
     "together fill the measure exactly. Composition and performance are therefore _____ rather "
     "than successive.",
     ["simultaneous", "rehearsed", "written", "private"], "A",
     "The ready-made phrases let the singer build each line while he is delivering it, which puts "
     "the making and the performing at the same moment. The 'rehearsed' option would place the "
     "composing before the performance, the sequence the sentence rejects with 'rather than "
     "successive'."),

 wic("W11",
     "An individual householder cannot say whether a fire will reach him, and the loss if it does "
     "may exceed everything he owns. An insurer writing ten thousand such houses cannot say either, "
     "but the proportion of them that burns in a year varies very little from one year to the next. "
     "The business rests on the fact that an event unpredictable singly becomes _____ in the "
     "aggregate.",
     ["regular", "impossible", "invisible", "costly"], "A",
     "The passage sets one house, about which nothing can be said, against ten thousand, whose "
     "yearly proportion barely moves, so the blank names steadiness across many cases. The "
     "'impossible' option would deny that the losses occur, when the point is that their total is "
     "steady."),

 wic("W12",
     "Waves arriving at an angle move sand along a beach in a series of small steps, and a timber "
     "groyne built across the beach halts that movement and piles sand up on its updrift side. The "
     "sand has not been created, only intercepted, and the beaches beyond the last groyne receive "
     "less than they did before. Works of this kind are therefore best judged _____.",
     ["over the whole stretch of coast they affect",
      "by the height of the sand they retain",
      "during the summer months only",
      "by the cost of the timber used"], "A",
     "Sand held behind one groyne is sand withheld from the shore beyond it, so an assessment "
     "confined to the protected beach records only half the transaction. The option measuring the "
     "height of retained sand looks at exactly that protected beach and ignores the loss downdrift."),

 meaning("W13",
     "In a game of this kind each player chooses without knowing what the other has chosen. Suppose "
     "that whatever the second player does, the first earns more by confessing than by keeping "
     "silent; confessing is then a <u>dominant</u> strategy for that player, and no reasoning about "
     "the other's likely choice is needed to justify it. Games in which both players hold such a "
     "strategy are the easiest to analyse and often the most discouraging to read.",
     "dominant",
     ["Occupying the highest position in a hierarchy.",
      "Better than the alternative whatever the other party does.",
      "Occurring most frequently within a population.",
      "Exercising control over another person."], "B",
     "The sentence defines the term as it uses it: confessing pays more no matter what the other "
     "player picks, which is a comparison between two options rather than a rank. The 'highest "
     "position in a hierarchy' sense is the commonest meaning of the word, but nothing in the "
     "passage arranges the strategies in a hierarchy."),

 meaning("W14",
     "A bat hunting among foliage must separate the echo of a moth from the echoes of the leaves "
     "behind it, and the two return only a fraction of a millisecond apart. Species that hunt in "
     "dense cover emit very short calls of wide bandwidth, because a short call can <u>resolve</u> "
     "two echoes that a long one runs together. The cost is that a short call carries little energy "
     "and cannot be heard far away.",
     "resolve",
     ["To settle a dispute between parties.",
      "To make a firm decision about a course of action.",
      "To distinguish as separate.",
      "To break something down into simpler parts."], "C",
     "The sentence contrasts a call that keeps two close echoes apart with one that runs them "
     "together, so the word names telling two returns apart. The 'firm decision' sense is a common "
     "meaning of the word, but the thing doing the work here is a call rather than a person."),

 meaning("W15",
     "A first encounter with a pathogen leaves behind a population of long-lived cells specific to "
     "it. Those cells do nothing while the pathogen is absent, but on a second encounter they "
     "divide and produce antibody within days rather than the weeks the first response took. "
     "Immunological <u>memory</u> is what a vaccine is designed to establish without the illness "
     "that would otherwise establish it.",
     "memory",
     ["The faculty by which past events are recalled.",
      "A capacity to respond more rapidly to something met before.",
      "A device in which data are stored.",
      "An account of past events written by a participant."], "B",
     "The passage defines the term through cells that lie dormant and then answer a repeat "
     "encounter in days instead of weeks, so it names a faster reaction on second exposure. The "
     "'faculty by which past events are recalled' sense is the ordinary meaning of the word, but no "
     "recollection by a mind is involved."),

 # --------------------------------------------- Text Structure and Purpose (6)
 tsp("T1",
     "Charles Wilson built a chamber in which moist air could be expanded suddenly, hoping to make "
     "clouds indoors. <u>A charged particle crossing the chamber strips electrons from the "
     "molecules it meets, and each ion left behind serves as a seed on which a droplet can "
     "form.</u> What the expanded air produced was not a cloud but a thin line of droplets marking "
     "the path of something invisible, and the instrument became the first to make a single "
     "particle's track visible.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It explains the mechanism by which the track described afterwards becomes visible.",
      "It questions whether the droplets Wilson observed were genuine.",
      "It describes the method Wilson used to expand the air in the chamber.",
      "It states a conclusion that the rest of the text goes on to qualify."], "A",
     "Ions left along the particle's path give droplets somewhere to condense, which is exactly "
     "what turns an invisible passage into the visible line the closing sentence reports. The text "
     "never puts the droplets in doubt; it presents them as the instrument's achievement."),

 tsp("T2",
     "The late Roman army in the east was paid in coin raised by taxation and quartered wherever it "
     "was needed. From the seventh century, with the wealthiest eastern provinces lost and the "
     "treasury much reduced, soldiers were instead settled on land in the provinces and drew their "
     "maintenance from it, serving when called. The districts so organised took their names from "
     "the units stationed in them, and their commanders came to hold civil as well as military "
     "authority.",
     "Which choice best states the main purpose of the text?",
     ["To describe a change in how an army was supported and what that change did to provincial government.",
      "To argue that the seventh-century army was more effective than its predecessor.",
      "To explain how taxes were assessed in the late Roman provinces.",
      "To trace the career of a provincial commander."], "A",
     "The passage moves from an army paid in cash to one settled on land and then notes that the "
     "districts were renamed and their commanders given civil powers, which is an account of a "
     "change together with its consequences. Nothing in it weighs the fighting quality of the two "
     "arrangements against each other."),

 tsp("T3",
     "Sinking a shaft through water-bearing gravel was for a long time impossible, because the "
     "ground flowed into the excavation as fast as it could be dug out. <u>Sealing the working "
     "chamber and raising the air pressure inside it until it balances the water outside holds the "
     "ground back and lets men work dry.</u> The men themselves paid for it: coming back to normal "
     "pressure too quickly left nitrogen coming out of solution in their blood, and the crippling "
     "pains that followed were common on such works until slow decompression was imposed.",
     "Which choice best describes the function of the underlined sentence?",
     ["It presents the technique that answered the problem stated before it and produced the hazard described after it.",
      "It offers evidence that water-bearing gravel cannot be excavated safely.",
      "It defines a term introduced in the opening sentence.",
      "It concedes a limitation that the final sentence removes."], "A",
     "The pressurised chamber solves the inflowing-ground problem named first and is also what puts "
     "nitrogen into the men's blood, so the sentence stands between the difficulty and its cost. "
     "Calling it a concession that the ending removes reverses the structure, since the final "
     "sentence adds a harm rather than cancelling one."),

 tsp("T4",
     "A stretch of coast can often be treated as a closed compartment: sand enters it from a river "
     "mouth or an eroding cliff, travels along it under the waves, and leaves it down a submarine "
     "canyon at the far end. Within such a compartment a loss at one place is usually a gain at "
     "another. Armouring a cliff protects the houses on top of it and at the same time cuts off the "
     "supply that fed the beaches downdrift, where the deficit appears some years later.",
     "Which choice best describes the overall structure of the text?",
     ["It sets out a way of accounting for sand along a coast and then applies it to a particular intervention.",
      "It compares two methods of protecting a cliff and recommends one of them.",
      "It traces the history of coastal engineering in a single region.",
      "It disputes the claim that sand travels along a coast."], "A",
     "The opening sentences describe the compartment as a balance sheet of sources and losses, and "
     "the last uses that balance to explain why armouring one cliff starves the beaches beyond it. "
     "No second method of protection is ever introduced for comparison."),

 tsp("T5",
     "Milman Parry had argued from the Greek text alone that the recurring descriptive tags of the "
     "<em>Iliad</em> were a poet's tools rather than his ornaments. In the 1930s he and Albert Lord "
     "took recording equipment into rural Yugoslavia and worked with singers who could perform "
     "epics of many thousands of lines without any written text. Those singers proved to use the "
     "same phrase in the same metrical position again and again, and no two performances of one "
     "song by one singer were identical.",
     "Which choice best states the main purpose of the text?",
     ["To describe how a claim about an ancient text was tested against a living practice.",
      "To argue that the Yugoslav epics are older than the Greek ones.",
      "To explain the metre in which Greek epic was composed.",
      "To describe the recording equipment available in the 1930s."], "A",
     "The text opens with a claim made from the Greek alone and then reports fieldwork among living "
     "singers whose practice bore it out, which is an account of a test. The relative age of the "
     "two traditions is never raised anywhere in the passage."),

 tsp("T6",
     "A purified protein taken from a pathogen is far safer to inject than the whole organism and "
     "much less effective: the immune system meets it, finds nothing else amiss, and mounts little "
     "response. <u>Substances called adjuvants are added to such vaccines to produce a small local "
     "disturbance at the injection site, which draws in the cells that carry the protein to the "
     "rest of the system.</u> Aluminium salts have served this purpose since the 1920s, and the "
     "mechanism is still not fully understood.",
     "Which choice best describes the function of the underlined sentence?",
     ["It introduces the remedy for the shortcoming described in the preceding sentence.",
      "It restates the preceding sentence in more technical language.",
      "It concedes that purified proteins cannot be used in vaccines.",
      "It gives an example of a pathogen against which vaccination has failed."], "A",
     "A purified protein provokes little response, and the sentence names what is added in order to "
     "provoke one, so it supplies the answer to the problem just set out. Treating it as a "
     "restatement would miss that it brings in a new ingredient rather than rewording the "
     "difficulty."),

 # ----------------------------------------------- Central Ideas and Details (6)
 cid("C1",
     "In several desert ant species certain workers never leave the nest. Nestmates feed them until "
     "the crop swells the abdomen to the size of a grape and the animal can no longer walk; it "
     "hangs from the ceiling of a deep chamber for months at a time. When forage fails, a worker "
     "strokes one of these swollen individuals and receives a drop of the stored liquid. The colony "
     "has in effect turned a run of good weeks into a store that neither dries out nor is carried "
     "off by others.",
     "Which choice best states the main idea of the text?",
     ["Certain ants serve their colonies as living containers holding a surplus against lean periods.",
      "Desert ants avoid foraging during the hottest part of the year.",
      "Ants that can no longer walk are removed from the nest by their nestmates.",
      "Ant colonies in deserts are smaller than those in wetter regions."], "A",
     "The swollen workers are filled during plenty and drawn on when forage fails, and the closing "
     "sentence calls the arrangement a store, so the point is storage inside the bodies of "
     "nestmates. The claim that immobile ants are removed contradicts the passage, in which they "
     "are kept and fed."),

 cid("C2",
     "Steel quenched from red heat into water comes out very hard and so brittle that a file will "
     "chip it and a blow will snap it. The structure formed by the sudden cooling is strained "
     "internally, and reheating the piece to a few hundred degrees lets part of that strain relax. "
     "The result is a little softer than the quenched steel and far less liable to break, which is "
     "why an edge tool is always tempered after hardening and never used straight from the quench.",
     "According to the text, why is a tool reheated after quenching?",
     ["To make it harder than quenching alone can make it.",
      "To relieve internal strain at the cost of a little hardness.",
      "To restore a shape lost during the sudden cooling.",
      "To allow a file to cut it during the final shaping."], "B",
     "The passage says the reheating lets part of the strain relax and leaves the steel slightly "
     "softer but much less likely to snap, which is a trade of hardness for toughness. The option "
     "claiming greater hardness contradicts the statement that the tempered steel is softer than "
     "the quenched steel."),

 cid("C3",
     "Several firms bidding for the right to drill a tract each estimate what it holds, and their "
     "estimates scatter around the true value. The tract goes to whoever estimated highest, and the "
     "highest estimate in a scattered set is more likely to be too high than too low. A firm that "
     "bids what it believes the tract is worth will therefore tend to overpay on the occasions when "
     "it wins, and an experienced bidder shades its offer below its own estimate for that reason.",
     "Which choice best states the main idea of the text?",
     ["Winning such an auction is itself a sign that the winner's estimate was too high, so bids should be shaded downward.",
      "Firms bidding for drilling rights rarely have any information about the tract.",
      "Auctions with many bidders raise more money than auctions with few.",
      "A firm's estimate of what a tract holds is usually accurate."], "A",
     "The tract goes to the highest estimate, and the highest of a scattered set is likelier to be "
     "an overestimate, which is why the experienced bidder offers less than it believes the tract "
     "is worth. The claim that estimates are usually accurate is ruled out by the scatter the whole "
     "argument depends on."),

 cid("C4",
     "Most metal ores contain a few per cent of the mineral wanted and a great deal of rock that "
     "resembles it. Flotation exploits a difference in wetting: the crushed ore is stirred into "
     "water with a reagent that clings to the mineral surface and makes it repel water, and air "
     "blown through the pulp carries those particles up in a froth that is skimmed off. The rock, "
     "still wetted, sinks. Ore bodies too poor for any earlier method became workable within a "
     "decade of the process being introduced.",
     "According to the text, what makes the wanted mineral rise in a flotation cell?",
     ["It is lighter than the rock that accompanies it.",
      "A reagent makes its surface repel water so that air bubbles carry it up.",
      "It dissolves in the water and is drawn off with the froth.",
      "The stirring throws the finer particles to the surface."], "B",
     "The text attributes the separation to a reagent that clings to the mineral and makes it repel "
     "water so that blown air lifts it, not to any difference in weight. The option about lightness "
     "names a property the passage never claims and would leave the reagent with nothing to do."),

 cid("C5",
     "The gold coin struck at Constantinople from the fourth century held its weight and its "
     "fineness almost unchanged for some seven hundred years, at a time when most western coinages "
     "were repeatedly debased. Merchants from Alexandria to the Baltic priced goods in it and took "
     "it without weighing. The advantage to the issuing state lay less in the metal than in the "
     "demand: a coin accepted on sight anywhere is one that foreigners will hold, and holding it is "
     "a loan to the state that issued it.",
     "Which choice best states the main idea of the text?",
     ["A coinage of constant fineness was accepted far beyond its issuer's territory and benefited the issuer accordingly.",
      "Merchants of the period preferred to weigh coins rather than to count them.",
      "Western rulers debased their coinages in order to imitate Constantinople.",
      "The gold used in the coin was mined within the issuing state's own borders."], "A",
     "The passage joins seven centuries of unchanged fineness to acceptance from Alexandria to the "
     "Baltic and then to the benefit the issuer drew from foreigners holding the coin. The claim "
     "about weighing is contradicted by the statement that merchants took it without weighing."),

 cid("C6",
     "A vine of the Cuban rainforest opens flowers whose nectar is taken almost entirely by bats. "
     "Above each flower stands a dish-shaped leaf, concave and unusually stiff, which returns a "
     "strong echo from a wide range of directions instead of the narrow one an ordinary leaf "
     "reflects. Bats trained to find a feeder among artificial foliage located it in about half the "
     "time when a similar dish was fixed above it. The plant appears to advertise in the medium its "
     "pollinators use.",
     "Which choice best states the main idea of the text?",
     ["A plant's leaf is shaped so as to be conspicuous to pollinators that navigate by echo.",
      "Bats find flowers more easily at night than during the day.",
      "The nectar of the vine is richer than that of related species.",
      "Stiff leaves reflect less sound than flexible ones."], "A",
     "The dish-shaped leaf returns a strong echo from many directions and halves the time bats need "
     "to find a feeder, so the shape works as a signal to animals that hunt by sound. The claim "
     "that stiff leaves reflect less sound reverses the passage, in which the stiff dish returns a "
     "stronger echo."),

 # ---------------------------------------------------- Command of Evidence (9)
 coe("E1",
     "A trial measured antibody concentration in the blood of volunteers given a single dose of a "
     "vaccine and in volunteers given a second dose eight weeks after the first. Concentrations are "
     "in arbitrary units, and a level above 40 units is taken to indicate protection."
     "<table style=\"border-collapse:collapse;margin:0.75rem 0;\">"
     "<tr>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Weeks after first dose</th>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Single-dose group (units)</th>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Two-dose group (units)</th>"
     "</tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">4</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">88</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">88</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">8</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">52</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">51</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">12</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">31</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">210</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">24</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">18</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">140</td></tr>"
     "</table>",
     "Which choice best describes data from the table that support the conclusion that the second "
     "dose did more than restore the level the first dose had reached?",
     ["At weeks 12 and 24 the two-dose group stood at 210 and 140 units, well above the 88 units the single-dose group reached at week 4.",
      "Both groups recorded 88 units at week 4, before the second dose was given.",
      "The single-dose group had fallen below 40 units by week 12.",
      "The two-dose group's concentration fell between week 12 and week 24."], "A",
     "Merely restoring the first dose's level would mean a return to about 88 units, and the "
     "figures recorded after the booster stand far above that mark for months. The identical "
     "week-4 readings were taken before the second dose was given and so say nothing about its "
     "effect."),

 coe("E2",
     "A groyne was completed in 1998 at a point midway along an eroding shore where sand moves "
     "steadily from north to south. Beach width was measured at four stations before construction "
     "and again ten years afterwards."
     "<table style=\"border-collapse:collapse;margin:0.75rem 0;\">"
     "<tr>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Station</th>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Beach width 1997 (m)</th>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Beach width 2008 (m)</th>"
     "</tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">1 km north of groyne</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">34</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">41</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">Immediately north</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">30</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">48</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">Immediately south</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">31</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">19</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">1 km south</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">33</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">26</td></tr>"
     "</table>",
     "Which choice best describes data from the table that support the conclusion that the groyne "
     "redistributed sand rather than adding to the shore as a whole?",
     ["The beach widened at both northern stations and narrowed at both southern ones over the same period.",
      "The widest beach recorded in 2008 was the one immediately north of the groyne.",
      "All four stations measured between 30 and 34 metres in 1997.",
      "The beach 1 km south of the groyne narrowed by 7 metres."], "A",
     "Gains updrift matched by losses downdrift are what a redistribution looks like, and only the "
     "option reporting both directions at once shows that pattern. Naming the widest beach of 2008 "
     "gives a gain with no offsetting loss, which would be equally consistent with sand having been "
     "added to the coast."),

 coe("E3",
     "A transit agency compared two operating rules on one bus route over four weeks. Under the "
     "first, drivers ran to a published timetable; under the second, a driver held at a control "
     "point whenever the bus in front was less than three minutes ahead. Headway is the interval "
     "between successive buses at a stop."
     "<table style=\"border-collapse:collapse;margin:0.75rem 0;\">"
     "<tr>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Measure</th>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Timetable rule</th>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Holding rule</th>"
     "</tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">Mean headway (min)</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">8.0</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">8.4</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">Standard deviation of headway (min)</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">4.6</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">1.9</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">Buses arriving in pairs (%)</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">21</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">4</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">Mean passenger wait (min)</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">6.2</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">4.7</td></tr>"
     "</table>",
     "Which choice best describes data from the table that support the conclusion that steadier "
     "spacing shortened passenger waits even though buses ran slightly less often?",
     ["Mean headway rose from 8.0 to 8.4 minutes under the holding rule while mean passenger wait fell from 6.2 to 4.7 minutes.",
      "The proportion of buses arriving in pairs fell from 21 per cent to 4 per cent.",
      "The standard deviation of headway under the holding rule was 1.9 minutes.",
      "Mean headway under the timetable rule was 8.0 minutes."], "A",
     "The conclusion pairs a slightly longer interval between buses with a shorter wait, so the "
     "support has to report both figures moving in opposite directions. The fall in paired arrivals "
     "shows the spacing improving but says nothing about how long passengers waited."),

 coe("E4",
     "In <em>The Ride of Marko</em>, an epic recorded from a village singer in 1934, the hero is "
     "given a small set of descriptive phrases that recur whenever his name falls at a particular "
     "place in the line. A scholar argues that these phrases are chosen for the space they fill "
     "rather than for what they say about the hero at that moment.",
     "Which quotation from <em>The Ride of Marko</em> most effectively illustrates the scholar's claim?",
     ["&ldquo;Marko of the sharp sword slept until noon, and Marko of the sharp sword woke and called for wine.&rdquo;",
      "&ldquo;Marko drew his sharp sword, and the horsemen fell back from the ford.&rdquo;",
      "&ldquo;The singer asked for silence, and the hearth was banked before he began.&rdquo;",
      "&ldquo;Marko's mother wept when the horse came home without him.&rdquo;"], "A",
     "The claim needs the same phrase attached to the hero when it has no bearing on what he is "
     "doing, and only the quotation calling him sharp-sworded while he sleeps and calls for wine "
     "shows that. The quotation in which he actually draws the sword makes the phrase fit the "
     "moment, which is what the claim denies."),

 coe("E5",
     "In the novel <em>The Deep Seam</em>, a young engineer is sent to manage a colliery where his "
     "father had worked at the face. A critic argues that the narrator's technical vocabulary "
     "functions in the book as a way of holding the place at a distance rather than of describing "
     "it.",
     "Which quotation from <em>The Deep Seam</em> most effectively illustrates the critic's claim?",
     ["&ldquo;I recorded the section as forty inches of clean coal over a dirt band, and did not write down that my father had knelt in it for nineteen years.&rdquo;",
      "&ldquo;The seam ran forty inches of clean coal over a dirt band, and the roof above it was good.&rdquo;",
      "&ldquo;My father's boots were still standing by the door of the shed.&rdquo;",
      "&ldquo;The winding engine had been rebuilt twice since the pit was sunk.&rdquo;"], "A",
     "The claim requires the technical language to stand in the way of something the narrator will "
     "not say, and only the quotation setting a measured section against the years his father knelt "
     "in it does both at once. The plain description of the seam and the roof uses the same "
     "vocabulary with nothing being withheld."),

 coe("E6",
     "In the novel <em>The Ledger of Small Risks</em>, a clerk in a marine insurance office spends "
     "his days pricing voyages he will never make. A critic argues that the novel presents his work "
     "as an exercise of imagination rather than of calculation.",
     "Which quotation from <em>The Ledger of Small Risks</em> most effectively illustrates the critic's claim?",
     ["&ldquo;Before I set a rate I had first to see the ship: her plates, her master, the ice off Newfoundland in March, the whole of a voyage that had not yet happened.&rdquo;",
      "&ldquo;The premium was three and a half per cent, which was what the office had charged on that route for eleven years.&rdquo;",
      "&ldquo;I reached the office at nine and left it at six, and the ledgers were ruled in red and black.&rdquo;",
      "&ldquo;My chief said that a clerk who could not add had no business in an underwriting room.&rdquo;"], "A",
     "The claim is that the pricing is an act of picturing, and only the quotation in which the "
     "clerk must see the plates, the master and an ice-strewn voyage that has not happened shows "
     "him doing so. The quotation about a rate unchanged for eleven years presents the work as the "
     "application of a settled figure, which is the calculation the claim is set against."),

 coe("E7",
     "A detector recorded more events of a particular kind than the accepted theory predicts. "
     "Physicist Ana Okonkwo argues that the excess arises in the apparatus itself rather than in "
     "the collisions.",
     "Which finding, if true, would most directly support Okonkwo's argument?",
     ["A second detector of a different design, running on the same beam over the same period, recorded no excess of the same events.",
      "The excess appeared in every month of the run at roughly the same rate.",
      "The accepted theory has been confirmed to high precision in other experiments.",
      "The detector's calorimeter was rebuilt during a shutdown two years before the run."], "A",
     "An excess produced by the collisions would show in any instrument watching that beam, so its "
     "absence in a differently built detector on the same beam points to the first apparatus as the "
     "source. A steady rate through the run is equally expected whether the cause lies in the "
     "instrument or in the collisions and separates nothing."),

 coe("E8",
     "Workers in an ant colony switch between nursing, foraging and nest repair, and the "
     "proportions shift within hours when the colony's needs change. Entomologist Piet Vandersteen "
     "argues that no worker is directed to a task: each responds to a local cue once that cue "
     "crosses its own threshold, and the thresholds differ between individuals.",
     "Which finding, if true, would most directly support Vandersteen's argument?",
     ["Removing the workers that repair the nest is followed by nurses taking up repair, beginning with those that had previously been slowest to nurse.",
      "Colonies with more workers repair damage to the nest faster than colonies with few.",
      "Workers that forage are on average older than workers that nurse.",
      "A queen removed from a colony stops laying within a day."], "A",
     "Thresholds that differ between individuals predict that when the repairers are gone the gap "
     "is filled first by the workers least readily drawn to their previous job, which is what the "
     "finding reports. Faster repair in larger colonies follows from having more workers of every "
     "kind and is just as consistent with central direction."),

 coe("E9",
     "A horseshoe bat's echoes return shifted upward in frequency because the animal is flying "
     "towards the target, and the size of the shift changes constantly. Neuroethologist Tomas "
     "Reinholt argues that the bat lowers the frequency of its outgoing call by exactly the amount "
     "of the shift, so that the returning echo always arrives in the narrow band its ear is best "
     "tuned to.",
     "Which finding, if true, would most directly support Reinholt's argument?",
     ["A bat flown towards a loudspeaker that returned artificially raised echoes lowered its call by the amount of the artificial rise, holding the echo at a constant frequency.",
      "Horseshoe bats emit calls of longer duration than bats that hunt in the open.",
      "The ear of a horseshoe bat is most sensitive within a band about two hundred hertz wide.",
      "Horseshoe bats hunt insects that beat their wings rapidly."], "A",
     "Imposing an artificial shift and watching the animal cancel it with an equal drop in its own "
     "call is the direct test of a compensation being made, and the echo held steady is the "
     "predicted result. The width of the sensitive band establishes only that a narrow band exists, "
     "not that the bat keeps its echoes inside it."),

 # -------------------------------------------------------------- Inferences (6)
 inf("I1",
     "A tunnel driven through sound rock needs no lining to hold the roof up: the rock above the "
     "opening will arch and carry itself, provided the blocks close to the surface of the "
     "excavation do not loosen and drop out first. Steel bolts grouted into holes drilled several "
     "metres into the roof clamp those blocks to the mass behind them. Support of this kind "
     "therefore works by _____",
     ["adding strength that the rock itself lacks.",
      "helping the rock carry its own load rather than replacing it.",
      "sealing the excavation against water.",
      "spreading the load onto the floor of the tunnel."], "B",
     "The rock is described as arching and supporting itself once the loose blocks at the surface "
     "are held in place, and holding them is all the bolts do. The option about adding strength the "
     "rock lacks misstates the premise, since the rock is sound and already capable of carrying the "
     "load."),

 inf("I2",
     "Power lost as heat in a transmission line falls as the square of the current carried, and the "
     "same power can be delivered at a lower current by raising the voltage. A transformer changes "
     "voltage with almost no loss and has no moving parts, but it will do nothing at all with a "
     "steady current. In the 1890s a scheme that generated at a moderate voltage, transmitted at a "
     "high one and delivered at a low one could therefore be built only with _____",
     ["a supply whose current reverses many times a second.",
      "conductors of unusually large cross-section.",
      "generating stations placed close to the consumers.",
      "insulation made from natural rubber."], "A",
     "The transformer is what makes three different voltages possible in one scheme, and it does "
     "nothing with a steady current, so the supply has to be one that alternates. Large conductors "
     "would cut the loss without any change of voltage and so would leave the transformer, and the "
     "scheme described, unnecessary."),

 inf("I3",
     "An infection spreads while an infectious person meets, on average, more than one susceptible "
     "person before recovering. Vaccination takes people out of the susceptible pool, and once that "
     "pool is small enough each case gives rise to fewer than one further case and the chain dies "
     "out. A disease that spreads readily needs a larger fraction of the population immune than one "
     "that spreads with difficulty, which means the proportion that must be vaccinated is fixed by "
     "_____",
     ["how contagious the disease itself is.",
      "the severity of the illness it causes.",
      "the number of people already vaccinated elsewhere.",
      "how long immunity from the vaccine lasts."], "A",
     "The passage makes the required fraction rise with how readily the disease spreads, so the "
     "threshold follows from the infection's own transmissibility. Severity governs how much harm "
     "each case does but never enters the count of secondary cases the argument turns on."),

 inf("I4",
     "In a matching scheme of this kind, applicants apply to their first choice; each institution "
     "provisionally holds the best applications it has so far and rejects the rest; and rejected "
     "applicants apply to their next choice, the process repeating until nobody is left to apply. "
     "An institution never has to commit before the end, and an applicant is never turned away by a "
     "place that would rather have had them. Applicants in such a scheme therefore have no reason "
     "to _____",
     ["list a safer institution ahead of the one they most want.",
      "apply to more than one institution.",
      "accept the place they are finally offered.",
      "submit their applications early in the process."], "A",
     "Because every holding is provisional and no applicant is rejected by a place that would "
     "prefer them, putting a likelier institution first can only forfeit the better outcome and can "
     "never protect it. Applying to several institutions is exactly what the procedure requires, so "
     "there is every reason to do it."),

 inf("I5",
     "Sulphide minerals sit unaltered in a coal or metal deposit for as long as they are out of "
     "contact with air. Working the deposit exposes fresh sulphide surfaces in the roadways and in "
     "the waste heaps, and the pumping that keeps the workings dry admits air to them as well. When "
     "a mine closes and the pumps are stopped, water rises through those roadways and finds its way "
     "to the surface, so a closure is likely to be followed by _____",
     ["an immediate improvement in the streams nearby.",
      "a discharge more acid than anything produced while the mine worked.",
      "the collapse of the roadways within a few weeks.",
      "a fall in the water table across the district."], "B",
     "Closure floods roadways whose sulphide surfaces have been open to the air for years, and the "
     "rising water carries what has formed on them out to the surface. Predicting an immediate "
     "improvement ignores that the pumps had been keeping that water away from the streams all "
     "along."),

 inf("I6",
     "Current sent along a land telegraph line weakens with distance, and beyond a few hundred "
     "kilometres the receiving instrument no longer moves reliably. A relay is a sensitive "
     "instrument whose armature closes a second circuit fed by its own local battery, so that the "
     "feeble arriving current does no work except to operate a switch. A line fitted with relays at "
     "intervals can therefore be extended _____",
     ["as far as relays and their batteries can be placed along it.",
      "only where an operator is stationed at each relay.",
      "at a lower cost per kilometre than a short line.",
      "only for signals sent in a single direction."], "A",
     "Each relay starts the signal afresh from a local battery, so what limits the length is no "
     "longer the strength arriving at the far end but the provision of relays along the way. The "
     "option requiring an operator at every relay ignores that the relay is a switch worked by the "
     "arriving current itself."),

 # -------------------------------------------------------------- Boundaries (12)
 bnd("B1",
     "Air is drawn through a colliery by a fan at the upcast shaft and finds its way to every "
     "working place through a system of doors and hanging cloth. A single door propped open "
     "short-circuits the current and leaves a whole district without _____ boys were once employed "
     "for no other purpose than to open a door for a tub and close it again.",
     ["air; young", "air, young", "air young", "air: and young"], "A",
     "Complete statements stand on both sides of the blank with no conjunction to join them, which "
     "is the semicolon's work. A comma alone between two full sentences leaves a splice."),

 bnd("B2",
     "Heating coal out of contact with air drives off everything volatile in it and leaves coke "
     "behind. A nineteenth-century gasworks sold four things from that one _____ gas for lighting, "
     "coke for furnaces, tar for road dressing, and ammoniacal liquor for fertiliser.",
     ["operation: gas", "operation; gas", "operation, and gas", "operation gas"], "A",
     "The words before the blank make a complete statement announcing four products, and what "
     "follows is the list naming them, which the colon introduces. The semicolon would require "
     "another full sentence after it, and a run of noun phrases is not one."),

 bnd("B3",
     "A street fire-alarm box of the older kind held a clockwork mechanism and a handle and nothing "
     "else. Because pulling the handle set the clockwork tapping out that box's own number on a "
     "wire running to the central _____ the officer on duty learned which corner the alarm had come "
     "from without a word being spoken.",
     ["station, the", "station; the", "station: the", "station and the"], "A",
     "The clause opening with 'Because' cannot stand on its own and is closed off with a comma "
     "before the main statement begins. Both the semicolon and the colon require a complete "
     "sentence in front of them."),

 bnd("B4",
     "The cars on the surviving San Francisco lines are pulled by a steel rope that runs in a slot "
     "beneath the street at a constant nine and a half miles an hour. The gripman, the member of "
     "the crew who works the lever closing a pair of jaws on that moving _____ the car by taking "
     "hold of the rope and stops it by letting go.",
     ["rope, starts", "rope; starts", "rope: starts", "rope starts"], "A",
     "The description beginning 'the member of the crew' was opened with a comma and must be closed "
     "with a matching comma before the verb belonging to the subject. Leaving the mark out runs the "
     "description straight into the predicate."),

 bnd("B5",
     "A sand mould is made in two boxes, and the pattern has to be drawn out of the sand before "
     "they are closed on one another. Anything that would lock the pattern in place &mdash; an "
     "undercut, a boss on the side of the casting, for _____ made as a separate piece of sand and "
     "set into the mould afterwards.",
     ["instance &mdash; has to be", "instance, has to be", "instance; has to be",
      "instance: has to be"], "A",
     "The interruption was opened with a dash and needs a matching dash to close it before the "
     "sentence resumes. Closing it with a comma leaves the opening dash without a partner and blurs "
     "where the interruption ends."),

 bnd("B6",
     "An immersed tube is not bored at all. Lengths of tunnel are built in a dry dock, floated out "
     "to the crossing with their ends sealed, and sunk into a trench dredged in the river _____ the "
     "joints are made underwater and the trench is backfilled over the finished tube.",
     ["bed; the", "bed, the", "bed the", "bed: and the"], "A",
     "Two complete statements meet at the blank with no conjunction between them, and the semicolon "
     "is the mark that joins such a pair. The comma on its own produces a splice, and a conjunction "
     "after a colon puts one where that mark does not take it."),

 bnd("B7",
     "The jurists whose opinions Justinian's commissioners condensed had written across four "
     "centuries and disagreed with one another freely. The commissioners cut the excerpts to a "
     "fiftieth of their original _____ they gave the result the force of law and forbade any "
     "commentary on it.",
     ["length, and", "length; and", "length: and", "length and"], "A",
     "Two independent clauses joined by the coordinating conjunction 'and' take a comma in front of "
     "that conjunction. Neither the semicolon nor the colon is used before a coordinating "
     "conjunction, and omitting the comma leaves two full clauses unseparated."),

 bnd("B8",
     "A trail laid by a foraging ant evaporates within minutes unless it is walked again, which "
     "gives the colony a way of forgetting. A path to a source that has been emptied loses the one "
     "thing that keeps it in _____ the feet of ants that are still finding food at the end of it.",
     ["existence: the", "existence; the", "existence, and the", "existence the"], "A",
     "The words in front of the blank make a complete statement, and what follows is a noun phrase "
     "naming the one thing just referred to, which is a colon's use. The semicolon would demand an "
     "independent clause after it, and a noun phrase is not one."),

 bnd("B9",
     "A bubble chamber holds liquid hydrogen just below its boiling point, and dropping the "
     "pressure for a few milliseconds leaves it briefly ready to boil anywhere. Although the "
     "chamber has to be photographed and reset before another expansion can be _____ physicists "
     "worked through millions of such photographs in the 1960s and found several new particles "
     "among them.",
     ["made, physicists", "made; physicists", "made: physicists", "made and physicists"], "A",
     "'Although' opens a clause that cannot stand alone, and such a clause placed in front of the "
     "main statement is separated from it by a comma. The semicolon would require an independent "
     "clause on both sides of it."),

 bnd("B10",
     "General average is the oldest rule in marine insurance and long predates the writing of "
     "policies. A loss deliberately incurred to save the whole _____ by every interest in it, in "
     "proportion to the value each has at stake.",
     ["venture is borne", "venture, is borne", "venture; is borne", "venture: is borne"], "A",
     "The words before the blank form the subject of the verb that follows, and no mark of "
     "punctuation separates a subject from its verb. The semicolon and the colon additionally "
     "require a complete sentence on the left, which a subject alone is not."),

 bnd("B11",
     "Faced with a sea wall that would have to be rebuilt every generation, an English estuary "
     "authority took a different course in 2002. Breaching the old embankment at a chosen point and "
     "letting the tide back onto two hundred hectares of former _____ the authority created a marsh "
     "that absorbs wave energy and needs no maintenance at all.",
     ["farmland, the", "farmland; the", "farmland: the", "farmland and the"], "A",
     "The opening phrase runs from 'Breaching' to the blank and must be closed with a comma before "
     "the main statement begins. The semicolon and the colon each need a complete sentence in front "
     "of them, and a participial phrase is not one."),

 bnd("B12",
     "A bat in hibernation cools almost to the temperature of the cave and lives until spring on "
     "fat laid down in autumn. Rousing enough to fly costs several days' worth of that fat; a "
     "colony disturbed a few times over the winter may reach spring with nothing _____ the same "
     "disturbance in summer costs the animals very little.",
     ["left; however,", "left, however,", "left however,", "left: however,"], "A",
     "Two complete statements meet at the blank, and the word joining them is an adverb rather than "
     "a conjunction, so the mark in front of it has to be a semicolon. A comma in that position "
     "leaves the two statements spliced together."),

 # ------------------------------------------------ Form, Structure, and Sense (9)
 fss("F1",
     "Repair of a breach in the nest wall begins within minutes and stops as soon as the damage has "
     "been made good. Soil is carried to the gap a grain at a time in the _____ mandibles, and an "
     "opening the width of a hand can be closed over in an afternoon.",
     ["workers", "worker's", "workers'", "workers's"], "C",
     "Many ants are at work and the mandibles belong to those ants, so the plural noun takes an "
     "apostrophe after its s. The singular possessive would mean a single worker, and the plain "
     "plural cannot show possession at all."),

 fss("F2",
     "The substation at the edge of the town was commissioned in 1961 and has been enlarged twice "
     "since. Since the aluminium works opened on the far side of the valley, demand on the feeder "
     "_____ in every year but one.",
     ["rose", "has risen", "had risen", "rises"], "B",
     "The clause opening with 'Since' names a point in the past, and the counting runs from that "
     "point up to the present, which is what the present perfect expresses. The simple past would "
     "close the period off in the past and leave the present out of it."),

 fss("F3",
     "The Post Office trained its telegraphists at a school in London and posted them wherever a "
     "circuit needed working. The two operators to _____ the night shift at Newcastle was given had "
     "each spent a year at that school.",
     ["who", "whom", "which", "whose"], "B",
     "The pronoun is the object of the preposition 'to', and the objective form is required after a "
     "preposition. The subjective form would be right only if the pronoun were doing the giving "
     "rather than receiving."),

 fss("F4",
     "Two alignments were put forward for the new tram route, one along the river and one over the "
     "hill. Of the two, the river alignment is the _____, though it serves fewer houses along the "
     "way.",
     ["shorter", "shortest", "more shorter", "most short"], "A",
     "Only two alignments are being compared, and a comparison between two takes the comparative "
     "form. The superlative would need at least three things to choose among."),

 fss("F5",
     "A hot-metal foundry runs to a timetable that nothing is allowed to disturb. Once the furnace "
     "is tapped, the metal has to be carried to the moulds without a pause, poured at a steady "
     "rate, and _____ before the boxes can be knocked out.",
     ["cooling slowly", "left to cool slowly", "it cools slowly", "to cool slowly"], "B",
     "The three things the metal must undergo all follow 'has to be', and the first two are past "
     "participles, so the third has to be one as well. The gerund and the infinitive both break the "
     "series the sentence has set up."),

 fss("F6",
     "The two headings were driven towards each other from opposite banks and met four years after "
     "the first ground was broken. Surveyed from the surface every fortnight throughout the drive, "
     "_____",
     ["the engineers found the two headings only fifty millimetres apart at the meeting.",
      "the meeting showed the two headings only fifty millimetres apart.",
      "the two headings proved to be only fifty millimetres apart at the meeting.",
      "there was a difference of only fifty millimetres at the meeting."], "C",
     "The opening phrase describes whatever was surveyed from the surface, and only the option "
     "beginning with the headings names something that could have been surveyed. Beginning with the "
     "engineers says that the engineers themselves were the object of the fortnightly survey."),

 fss("F7",
     "A marine risk is rarely carried by one office alone. The underwriters on the slip, together "
     "with the broker who placed it, _____ a copy of every survey report as soon as it is issued.",
     ["receives", "is receiving", "receive", "has received"], "C",
     "The subject is the plural 'underwriters', and the phrase beginning 'together with' neither "
     "adds to the subject nor changes its number. The singular verb would agree with the broker, "
     "who is named only inside that interrupting phrase."),

 fss("F8",
     "The counters that surround the target are replaced on a rolling schedule, since a counter "
     "left in the beam too long loses efficiency. A number of the counters in the forward array "
     "_____ changed during the shutdown last winter.",
     ["was", "were", "has been", "is"], "B",
     "'A number of' followed by a plural noun takes a plural verb, because the phrase means several "
     "of the counters rather than the count itself. The singular would be right only for 'the "
     "number of', which names a figure."),

 fss("F9",
     "A player who cooperates while the other defects does worst of the four possible outcomes, and "
     "the arithmetic of the game is what makes the trap. The payoff to a player who cooperates is "
     "in every case lower than _____",
     ["a player who defects.", "that of a player who defects.", "when a player defects.",
      "defecting."], "B",
     "The sentence compares one payoff with another, so the second term has to name a payoff rather "
     "than a person, and the pronoun standing in for 'the payoff' supplies it. Naming the player "
     "compares a payoff with a person, which is not a comparison the sentence can make."),

 # -------------------------------------------------------------- Transitions (9)
 trn("N1",
     "Flotation made it worth working ore bodies carrying less than one per cent copper, and the "
     "tonnage of metal produced in the twentieth century owes more to it than to any new "
     "discovery. _____ the process leaves behind a slurry of finely ground rock in far greater "
     "volume than the coarse waste of earlier methods, and the dams built to hold that slurry are "
     "among the largest structures on earth.",
     ["However,", "Consequently,", "Likewise,", "For instance,"], "A",
     "The volume of slurry and the dams needed to hold it stand against the benefit just credited "
     "to the process, so the transition marks a drawback. A consequence transition would make the "
     "extra waste follow from the metal produced rather than qualify the achievement."),

 trn("N2",
     "Electricity cannot be stored in quantity on a grid, and what is generated in a given second "
     "is consumed in that second. _____ the plant a system owns has to be sized for the highest "
     "demand of the year rather than for the average, and a good deal of it stands unused for "
     "months at a time.",
     ["Nevertheless,", "As a result,", "By contrast,", "In other words,"], "B",
     "Sizing the plant for the annual peak follows directly from the impossibility of storing what "
     "is generated, which is a cause-and-effect relation. Treating the second sentence as a "
     "restatement would miss that it draws a consequence rather than rewording the first."),

 trn("N3",
     "An overhead telegraph wire strung on poles could be repaired by a lineman with a ladder, and "
     "a fault was usually found within a day. _____ a fault in a buried cable gave no sign at all "
     "of where it lay, and the engineers had to measure the resistance from each end and calculate "
     "the distance before a spade was put into the ground.",
     ["By contrast,", "For example,", "Consequently,", "In addition,"], "A",
     "The buried cable behaves in the opposite way to the overhead wire that could simply be walked "
     "and inspected, so the two cases are being set against each other. Presenting the buried cable "
     "as an example would suggest it illustrates the ease just described."),

 trn("N4",
     "A flat fare is simple to collect and simple to explain, and it needs no equipment at the exit "
     "of a station. _____ it charges the same for a journey of two stops as for one across the "
     "whole system, and the short-distance passengers a network most wants to attract are the ones "
     "it overcharges.",
     ["Therefore,", "However,", "Likewise,", "In short,"], "B",
     "Overcharging the short-distance passenger works against the simplicity just praised, so the "
     "transition marks a drawback. A consequence transition would make the simplicity the cause of "
     "the mispricing, which the passage does not claim."),

 trn("N5",
     "Steel contracts as it cools, and the outside of a quenched bar reaches the temperature of the "
     "bath long before the middle does. The core is still shrinking when the skin has stopped. "
     "_____ a section that changes thickness abruptly, or a sharp internal corner, is where a "
     "quench crack is most often found.",
     ["Nevertheless,", "For this reason,", "By contrast,", "In other words,"], "B",
     "Cracks appearing where the section changes follow from the uneven shrinkage just described, "
     "which is a cause-and-effect relation. A contrastive transition would set the crack against "
     "the shrinkage when it is the shrinkage's result."),

 trn("N6",
     "A boring machine assembled underground for one contract is built for a particular diameter "
     "and a particular kind of ground, and it can drive a bore far faster than any other method. "
     "_____ a machine that meets a fault zone it was not designed for can be held up for months "
     "while a chamber is dug by hand around its cutting head.",
     ["Even so,", "In other words,", "For example,", "Similarly,"], "A",
     "Months lost to hand excavation stand against the speed just credited to the machine, so the "
     "transition concedes a drawback. Treating the second sentence as a restatement would be wrong, "
     "since it introduces a new circumstance rather than rephrasing the first."),

 trn("N7",
     "The walls thrown across the landward approach to Constantinople in the fifth century stood in "
     "three lines, each higher than the one in front of it, with a flooded ditch beyond them all. "
     "An attacker who took the outer wall found himself in a narrow space commanded from above on "
     "both sides. _____ the city withstood every land assault brought against it for more than a "
     "thousand years, and fell at last to a besieger with cannon.",
     ["Nevertheless,", "As a result,", "For instance,", "By contrast,"], "B",
     "A thousand years of successful defence follows from the tiered walls and the trap between "
     "them, so the relation is cause and effect. A contrastive transition would set the record of "
     "the defence against the design that produced it."),

 trn("N8",
     "A detector can be made more sensitive by putting more material in the path of the beam, since "
     "a particle that crosses more matter is likelier to interact and be seen. _____ every extra "
     "layer also scatters the particles the experiment is trying to track, and the measurement of "
     "direction grows worse as the measurement of energy grows better.",
     ["Likewise,", "For this reason,", "However,", "In fact,"], "C",
     "The scattering works against the sensitivity gained from the same material, so the transition "
     "marks a countervailing effect. A result transition would present the worse direction "
     "measurement as the purpose of adding material, when the passage sets it against the gain."),

 trn("N9",
     "An insurer that offers one price to everyone attracts most eagerly those who know themselves "
     "to be at greatest risk, while the healthy and the careful decide the cover is not worth its "
     "cost and stay out. The pool that remains is worse than the average the price was set for. "
     "_____ the price has to rise, which drives out the next healthiest group in turn.",
     ["Nevertheless,", "As a result,", "By contrast,", "For example,"], "B",
     "The rise in price follows from a pool that has become worse than the one the price was "
     "calculated for, which is cause and effect. A contrastive transition would set the increase "
     "against the deterioration when it is its direct outcome."),

 # ------------------------------------------------------ Rhetorical Synthesis (9)
 syn("R1",
     ["Hydraulic mines in California turned water jets on gravel banks to wash out the gold they held.",
      "A single nozzle could move more gravel in a day than a hundred men with shovels.",
      "The washed gravel travelled down the rivers and settled across the farmland of the valleys below.",
      "Riverbeds rose until towns that had never flooded were flooded in ordinary winters.",
      "A federal court forbade the discharge of mining debris into the rivers in 1884."],
     "explain why the courts moved against a method that was working so well.",
     ["Hydraulic mines in California turned water jets on gravel banks to wash out the gold they held.",
      "Because a single nozzle shifted more gravel than a hundred men could, the debris it sent downstream raised the riverbeds until ordinary winters flooded towns that had never flooded before.",
      "A federal court forbade the discharge of mining debris into the rivers in 1884.",
      "A single nozzle could move more gravel in a day than a hundred men with shovels."],
     "B",
     "The goal asks what drove the courts to act against an effective method, and only the option "
     "tracing the nozzle's output to raised riverbeds and flooded towns supplies the harm. Stating "
     "that a court forbade the discharge in 1884 reports the decision without the reason behind "
     "it."),

 syn("R2",
     ["Demand on a grid rises sharply in the early evening and falls away overnight.",
      "Nuclear and large coal plant is slow and costly to start and to stop.",
      "A pumped-storage station pumps water up to a high reservoir when demand is low.",
      "It can release that water through turbines within about a minute when demand is high.",
      "Roughly a quarter of the energy is lost over the round trip."],
     "explain what a pumped-storage station does for a grid despite the energy it loses.",
     ["A pumped-storage station pumps water up to a high reservoir when demand is low.",
      "Roughly a quarter of the energy is lost over the round trip.",
      "Because large plant is slow and costly to start and stop, a station that stores cheap overnight output and returns it within a minute at the evening peak is worth the quarter of the energy the round trip costs.",
      "Demand on a grid rises sharply in the early evening and falls away overnight."],
     "C",
     "The goal requires the loss to be set against what is gained, and only the option connecting "
     "inflexible plant to output stored overnight and returned in a minute does that. Stating the "
     "size of the loss on its own names a cost with no benefit to weigh it against."),

 syn("R3",
     ["A manual exchange required an operator to look up or remember every subscriber's number.",
      "Almon Strowger patented an automatic switch in 1891.",
      "The switch stepped through a bank of contacts under pulses sent from the caller's own dial.",
      "The earliest automatic exchanges gave every subscriber a switch of his own.",
      "Most subscribers' lines are in use for only a few minutes in the day."],
     "explain how later designs cut the amount of equipment an automatic exchange needed.",
     ["Almon Strowger patented an automatic switch in 1891.",
      "The switch stepped through a bank of contacts under pulses sent from the caller's own dial.",
      "Because most lines are in use for only a few minutes in the day, later designs shared a small number of switches among many subscribers instead of providing one for each.",
      "A manual exchange required an operator to look up or remember every subscriber's number."],
     "C",
     "The goal asks how the equipment was reduced, and only the option joining idle lines to "
     "switches shared among subscribers states both the change and its justification. Giving the "
     "date of Strowger's patent identifies the invention without touching the later economy."),

 syn("R4",
     ["Marc Brunel watched a shipworm bore through timber behind a shell it pushed ahead of itself.",
      "He patented a tunnelling shield in 1818: an iron frame divided into cells in which miners worked at the face.",
      "The frame was pushed forward by screws and brickwork was built up immediately behind it.",
      "The Thames Tunnel, driven with the shield, opened in 1843.",
      "Earlier attempts to tunnel under the Thames had all been abandoned when the river broke in."],
     "explain why the shield succeeded where the earlier attempts under the river had failed.",
     ["Marc Brunel watched a shipworm bore through timber behind a shell it pushed ahead of itself.",
      "The Thames Tunnel, driven with the shield, opened in 1843.",
      "He patented a tunnelling shield in 1818: an iron frame divided into cells in which miners worked at the face.",
      "Because the iron frame held the ground at the face while brickwork closed up immediately behind it, no length of the bore was ever left open for the river to break into."],
     "D",
     "The earlier attempts ended when the river broke in, so the explanation has to show the ground "
     "never left unsupported, which only the option pairing the frame at the face with brickwork "
     "closing up behind it does. Naming the year the tunnel opened records the success without "
     "accounting for it."),

 syn("R5",
     ["Life annuities in seventeenth-century Europe were commonly sold at one price whatever the buyer's age.",
      "Edmond Halley obtained the register of births and burials kept at Breslau, which recorded age at death.",
      "From it he built a table showing how many of a thousand people born survive to each year of age.",
      "The table allowed the worth of payments continuing for the rest of a named person's life to be calculated.",
      "Governments went on selling age-blind annuities for decades after the table was published."],
     "explain what Halley's table made possible that had not been possible before.",
     ["Edmond Halley obtained the register of births and burials kept at Breslau, which recorded age at death.",
      "Governments went on selling age-blind annuities for decades after the table was published.",
      "Because the table showed how many of a thousand people born survive to each year of age, the worth of payments continuing for the rest of a named person's life could be calculated for the first time.",
      "Life annuities in seventeenth-century Europe were commonly sold at one price whatever the buyer's age."],
     "C",
     "The goal asks what became possible, and only the option joining the survivorship figures to "
     "the pricing of a lifelong stream of payments states a new capability. Noting that governments "
     "went on selling age-blind annuities reports what the table failed to change."),

 syn("R6",
     ["Carl Anderson photographed cosmic-ray tracks in a cloud chamber placed in a magnetic field in 1932.",
      "The field bends a positive particle one way and a negative particle the other.",
      "A lead plate across the middle of the chamber slowed any particle that passed through it.",
      "One track curved as a positive particle would, and curved more sharply after the plate than before it.",
      "The curvature was far too great for a proton of that energy."],
     "explain how the photograph showed the particle to be positive and light rather than a proton.",
     ["Carl Anderson photographed cosmic-ray tracks in a cloud chamber placed in a magnetic field in 1932.",
      "Because the sharper curve after the lead plate fixed the direction of travel, the sense of the bending identified the charge as positive, while the tightness of the curve ruled out a proton of that energy.",
      "The field bends a positive particle one way and a negative particle the other.",
      "A lead plate across the middle of the chamber slowed any particle that passed through it."],
     "B",
     "The goal asks how the picture established both facts at once, and only the option using the "
     "plate to fix the direction and the tightness of the curve to exclude a proton does so. "
     "Stating that the field bends the two signs differently gives the principle without showing "
     "which way the particle was going."),

 syn("R7",
     ["The epic of Sunjata is performed in Mande West Africa by hereditary specialists trained from childhood.",
      "No two performances agree in length, and one may run from a single evening to a week.",
      "Certain praise-names, genealogies and proverbs recur in the same wording in every version recorded.",
      "Performers describe themselves as transmitting rather than composing.",
      "Written versions published since the 1960s freeze one performance out of many."],
     "explain how such a tradition can be at once fixed and variable.",
     ["The epic of Sunjata is performed in Mande West Africa by hereditary specialists trained from childhood.",
      "Written versions published since the 1960s freeze one performance out of many.",
      "Although no two performances agree in length, the praise-names, genealogies and proverbs recur word for word in every version recorded, so what is fixed is the material rather than the whole.",
      "Performers describe themselves as transmitting rather than composing."],
     "C",
     "The goal calls for the two properties to be reconciled, and only the option setting the "
     "varying length against the wording that never varies shows what stays constant and what does "
     "not. Noting that written versions freeze one performance describes what publication does "
     "rather than how the tradition itself works."),

 syn("R8",
     ["A nourishment scheme places sand dredged offshore onto an eroding beach.",
      "The sand placed may be coarser or finer than the sand already there, depending on where it was dredged.",
      "Waves carry finer sand offshore again within a season or two.",
      "One beach given sand coarser than its own held its width for eleven years.",
      "Nourishment does nothing to stop the process that removed the sand in the first place."],
     "explain why the grain size of the imported sand matters.",
     ["A nourishment scheme places sand dredged offshore onto an eroding beach.",
      "Nourishment does nothing to stop the process that removed the sand in the first place.",
      "The sand placed may be coarser or finer than the sand already there, depending on where it was dredged.",
      "Because waves carry fine sand offshore within a season or two while a beach given coarser sand held its width for eleven years, the size of the imported grains decides how long the work lasts."],
     "D",
     "The goal asks why grain size matters, and only the option contrasting fine sand lost in a "
     "season with coarse sand holding for eleven years ties the size to the outcome. Observing that "
     "nourishment leaves the underlying process untouched is true whatever the grain size and so "
     "answers nothing."),

 syn("R9",
     ["Most vaccines lose potency if they are allowed to freeze or to rise above about eight degrees Celsius.",
      "A dose that has lost potency looks exactly like one that has not.",
      "Vials can carry a small square of heat-sensitive material that darkens irreversibly with cumulative exposure.",
      "A health worker compares the square with a printed reference ring before giving the dose.",
      "Millions of doses used to be discarded on suspicion after a refrigerator failure."],
     "explain how the heat-sensitive square changed what happens after a refrigerator failure.",
     ["Most vaccines lose potency if they are allowed to freeze or to rise above about eight degrees Celsius.",
      "Because a spoiled dose is indistinguishable by eye from a sound one, a square that darkens with cumulative heat lets a worker keep the vials that are still good instead of discarding a whole batch on suspicion.",
      "Vials can carry a small square of heat-sensitive material that darkens irreversibly with cumulative exposure.",
      "A health worker compares the square with a printed reference ring before giving the dose."],
     "B",
     "The goal asks what changed after a failure, and only the option joining the invisibility of "
     "spoilage to the saving of sound vials states the difference the indicator makes. Describing "
     "the square itself explains the device without saying what it altered in practice."),
]

# Topics screened out by screen_topics.py because a banked passage already
# covers them. Each was abandoned rather than paraphrased around.
DROPPED = {
    "submarine telegraph cable / gutta-percha": "rw_test10:T7, rw_test9:R9",
    "the first transatlantic cable": "rw_test9:R9",
    "Chappe's optical telegraph": "rw_test14:I4",
    "time signals and railway standard time": "rw_test13:E7",
    "pneumatic tube post": "rw_test13:I4",
    "the Bessemer converter / blast furnace": "rw_test13:B1, rw_test15:B3",
    "wrought iron and puddling": "rw_test15:B3",
    "lost-wax casting": "rw_test9:C3",
    "bell founding and bell tone": "rw_test10:E2",
    "aluminium electrolysis": "rw_test11:I2",
    "ore provenance by lead isotopes": "rw_test13:R1, rw_test15:E2",
    "the miner's safety lamp": "rw_test12:F4, rw_test12:F6",
    "salt from brine": "rw_test10:T3",
    "the gasholder frame": "rw_test15:F5",
    "rural electrification cooperatives": "rw_test13:T4",
    "regenerative braking on trams": "rw_test13:T1",
    "shielded street lighting and the night sky": "rw_test13:T9",
    "roundabouts versus signalised junctions": "rw_test13:T2",
    "leafcutter ants and fungus gardens": "rw_test10:C1",
    "termite mound ventilation": "rw_test14:W2",
    "ants dispersing oil-body seeds": "rw_test12:I5",
    "acacia ants and plant defence": "rw_test9:T3",
    "the honeybee waggle dance": "rw_test9:W12",
    "neutrino detection in ice": "rw_test11:I1",
    "gravitational-wave interferometers": "rw_test12:S4",
    "muon tomography of a pyramid": "rw_test10:W12",
    "vampire bat food sharing": "rw_test12:E6",
    "moth ultrasound against bats": "rw_octusc_m1:15",
    "the cochlear implant": "rw_test13:B8",
    "variolation and Jenner's cowpox": "rw_test18:T3",
    "friendly societies and state insurance": "rw_test10:E8",
    "marram grass and dune stabilisation": "rw_test18:N3",
    "chalk cliffs and coccolith accumulation": "rw_test13:T3",
    "desalination brine on the seabed": "rw_test10:T9",
    "Byzantine gold mosaic tesserae": "rw_test15:C3",
    "Hagia Sophia's dome": "rw_test11:B10",
    "ballad variants collected in one valley": "rw_test13:W14",
}
