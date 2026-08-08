#!/usr/bin/env python3
"""
Reading & Writing authored for Test 17.

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
whose options are genuinely words ("has" / "have") are left as words, which is
also how the real test presents them.

Topics are drawn from the fifteen subject territories assigned to Test 17 so
that the three tests being built in parallel stay apart: mountaineering and
high-altitude physiology; land surveying and geodesy; railways and signalling;
forestry, timber and tree rings; seismology and earthquake engineering; Central
Asian and Silk Road history; insect flight; radio astronomy; cave science and
karst; Nordic and Icelandic literature; water rights and irrigation law; urban
trees and city ecology; the mathematics of voting and apportionment; whale
biology and cetacean acoustics; dairying and the chemistry of cheese.

Every candidate topic was screened against content-pool/rw_authored_corpus.json
(809 banked passages) by keyword and by 5-gram / Jaccard overlap before any
passage was written; screen_topics.py in this directory is that check. The
collisions it found are recorded in DROPPED at the foot of this file and those
topics were abandoned rather than paraphrased around.

Block counts (fixed by the assembler's quota, 3 modules x 27):
    Words in Context 15, Text Structure and Purpose 6,
    Central Ideas and Details 6, Command of Evidence 9, Inferences 6,
    Boundaries 12, Form, Structure, and Sense 9, Transitions 9,
    Rhetorical Synthesis 9                                        = 81
"""

SOURCE = "AUTHORED-T17"
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
     "An expedition that flies to a base at four thousand metres and starts for the top the next "
     "morning will lose most of its members to headache and vomiting inside two days. Parties that "
     "instead carry loads to a higher camp and come back down to sleep gain height far more slowly, "
     "and the body has time to settle into a faster resting breath and a thicker blood. Success on "
     "a high peak is therefore _____ rather than a matter of pace.",
     ["incremental", "accidental", "effortless", "competitive"], "A",
     "The passage sets a slow routine of carrying high and sleeping low against climbing straight "
     "for the top, so the blank names a gain built up by stages. The 'competitive' option would "
     "restore the idea of pace that the sentence explicitly sets aside."),

 wic("W2",
     "A levelling crew works from a mark of known height to a new one and then runs the whole line "
     "back to where it began. If the readings do not return to the height they started from, the "
     "difference is spread through the intermediate points in proportion to the distance between "
     "them. The return run is therefore a way of _____ the work rather than merely repeating it.",
     ["duplicating", "verifying", "postponing", "simplifying"], "B",
     "Comparing the closing readings with the known starting height is what exposes the error and "
     "allows it to be distributed, so the return run tests the survey. The 'duplicating' option "
     "names exactly what the sentence denies with 'rather than merely repeating'."),

 wic("W3",
     "Under the absolute block system a length of line counts as occupied from the moment a train "
     "enters it, and the signalman at the far end must send word back before a second train is "
     "admitted. No driver is asked to judge how far ahead the train in front may be. The safety of "
     "the arrangement rests on making the rule _____ rather than leaving it to the men on the "
     "footplate.",
     ["unconditional", "advisory", "occasional", "informal"], "A",
     "Nothing enters the section until word comes back, and no driver is left to judge, so the rule "
     "admits of no exception. The 'advisory' option describes precisely the discretionary practice "
     "the system was built to replace."),

 wic("W4",
     "A log sawn straight through gives boards whose growth rings lie nearly flat across the face, "
     "and boards of that kind cup as they dry. Splitting the log into quarters first and cutting "
     "each quarter so that the rings stand on edge wastes more wood and takes longer, but the "
     "finished boards move very little afterwards. The method trades yield for _____.",
     ["stability", "brightness", "novelty", "quantity"], "A",
     "Boards that move very little afterwards are boards that keep their shape, which is what the "
     "lost yield buys. The 'quantity' option names the thing the method gives up rather than the "
     "thing it gains."),

 wic("W5",
     "A building set on bearings of layered rubber and lead is not braced against an earthquake so "
     "much as separated from it. The bearings are soft enough sideways that the ground can travel a "
     "foot beneath the structure while the floors above sway slowly and stay together. The design "
     "works by making the connection between ground and building deliberately _____.",
     ["rigid", "loose", "watertight", "decorative"], "B",
     "The ground moves a foot while the building above barely follows, so the joint between the two "
     "is meant not to be tight. The 'rigid' option describes the braced connection that the first "
     "sentence says this design avoids."),

 wic("W6",
     "Han envoys sent west in the second century BCE came back with accounts of horses in the "
     "Ferghana valley taller than anything bred on the steppe and said to sweat blood. The court "
     "wanted them for its cavalry and in the end sent an army to fetch them. For the emperor the "
     "animals were less a curiosity than a _____, since mounted archers on the northern frontier "
     "could not be met on foot.",
     ["necessity", "luxury", "tribute", "rumour"], "A",
     "The closing clause explains that the frontier could not be held without horsemen, so the "
     "animals answered a military requirement. The 'luxury' option is the reading the sentence "
     "itself puts aside with 'less a curiosity than'."),

 wic("W7",
     "A fly has two wings and, behind them, two knobbed stalks that beat in time with the wings and "
     "produce no lift at all. When the insect is turned in flight, the stalks resist the turn and "
     "the strain is read by sensors at their base. The structure is best understood as an _____ "
     "rather than as a shrunken second pair of wings.",
     ["ornament", "instrument", "obstacle", "afterthought"], "B",
     "The stalks generate no lift and instead report the fly's rotation through sensors, which is "
     "the work of a measuring device. The 'ornament' option would deny the function the passage "
     "spends two sentences describing."),

 wic("W8",
     "No single dish can be built wide enough to show detail on the scale radio astronomers want. "
     "The signals from many small dishes spread over miles of ground are recorded with exact timing "
     "and combined afterwards, and the array then behaves as though it were one instrument as wide "
     "as the distance between its outermost dishes. Resolution on this scale is _____ rather than "
     "built.",
     ["computed", "abandoned", "purchased", "estimated"], "A",
     "The detail comes from combining separately recorded signals after the observation, which is a "
     "calculation rather than a piece of hardware. The 'estimated' option implies an approximation, "
     "whereas the passage has the array genuinely reaching the resolution of a far wider dish."),

 wic("W9",
     "The Icelandic family sagas report killings, lawsuits and feuds lasting decades in a level "
     "voice. A man run through with a spear remarks that broad-bladed weapons are coming into "
     "fashion, and then falls; nobody in the text says that the moment is terrible. Readers who "
     "arrive from later European narrative often find the effect _____, since the prose withholds "
     "exactly the commentary they expect.",
     ["disconcerting", "sentimental", "ornate", "reassuring"], "A",
     "The sagas refuse the emotional commentary a reader is looking for, and a reader deprived of "
     "what is expected is unsettled rather than soothed. The 'ornate' option describes a decorated "
     "style, which is the opposite of the plain reporting the passage illustrates."),

 wic("W10",
     "Under the doctrine that governs water in most of the American West, a right dates from the "
     "day the water was first put to use, and in a dry year the holder of the oldest right takes "
     "the whole of an allotment before a later holder takes any. Rights are not cut back in "
     "proportion when the river runs low. Seniority in such a system is therefore _____ rather than "
     "ceremonial.",
     ["decisive", "symbolic", "negotiable", "recent"], "A",
     "Because the oldest claim is filled completely before any later one receives water, the date "
     "of a right settles who goes without in a shortage. The 'negotiable' option conflicts with a "
     "rule that fills claims strictly in order of date."),

 wic("W11",
     "Air over a paved square on a July afternoon can stand several degrees warmer than the air a "
     "hundred metres away under a row of mature planes. Shade accounts for part of the gap; the "
     "rest comes from water drawn up through the trees and released from their leaves, which "
     "consumes heat as it evaporates. A large canopy therefore does not merely block the sun but "
     "_____ the air around it.",
     ["cools", "dries", "stirs", "shades"], "A",
     "Evaporation from the leaves takes heat out of the surrounding air, which is an effect beyond "
     "blocking sunlight. The 'shades' option repeats the very thing the sentence says the canopy "
     "does not merely do."),

 wic("W12",
     "When more than two candidates stand, a plurality count can hand the seat to someone most "
     "voters ranked last. A ballot that asks voters to rank the whole field allows the weakest "
     "candidate to be eliminated and those ballots passed to each voter's next name, and the count "
     "repeats until somebody holds a majority. The procedure treats a first preference for a losing "
     "candidate as _____ rather than as a vote thrown away.",
     ["transferable", "confidential", "provisional", "irrelevant"], "A",
     "Ballots for an eliminated candidate move to the next name on each voter's list, so the "
     "preference is carried forward instead of discarded. The 'provisional' option describes a vote "
     "that might be withdrawn, whereas these ballots are counted in every round."),

 meaning("W13",
     "Limestone is barely soluble in pure water, but rain that has taken up carbon dioxide from the "
     "air and from soil turns weakly acidic and carries the rock away in dissolved form. Caves in a "
     "limestone hill are not ground out; the passages are widened by <u>solution</u> along joints "
     "that were already there, at a rate of a few centimetres in a thousand years.",
     "solution",
     ["An answer to a problem.",
      "The process by which a solid is dissolved in a liquid.",
      "A liquid mixture used for cleaning.",
      "The breaking apart of rock by force."],
     "B",
     "The passage sets the widening against grinding and describes rock being carried away "
     "dissolved, so the word names dissolving. The 'answer to a problem' sense is the commonest "
     "meaning of the word but has no bearing on joints in limestone."),

 meaning("W14",
     "A forester walking a hillside records the species, the average diameter and the range of ages "
     "on each parcel before writing a management plan. Two parcels carrying the same species may "
     "still be handled quite differently: an even-aged <u>stand</u> planted after a clearance is "
     "thinned on a schedule, while one holding trees of many ages is worked tree by tree.",
     "stand",
     ["A piece of furniture for holding objects.",
      "A group of trees growing together on one site.",
      "A firmly held opinion.",
      "A halt in movement or growth."],
     "B",
     "The word takes the species, ages and diameters just recorded, so it names the trees occupying "
     "one parcel. The 'firmly held opinion' sense is a real meaning of the word but nothing in the "
     "passage concerns argument."),

 meaning("W15",
     "Curd cut into small pieces gives up more whey than curd left in large ones, and the drier the "
     "curd the firmer the cheese that comes of it. A maker who wants a paste that slices without "
     "crumbling will cut fine and press hard; one aiming at something that spreads under a knife "
     "will do neither. Almost every decision at the vat is taken with the <u>body</u> of the "
     "finished cheese in view.",
     "body",
     ["The main part of a written text.",
      "A group of people organised for a purpose.",
      "The physical consistency of a substance.",
      "A quantity of matter of no fixed shape."],
     "C",
     "Everything before the word concerns firmness, slicing and spreading, so the term names how "
     "the finished paste holds together. The 'group of people' sense is a genuine meaning of the "
     "word but no organisation appears anywhere in the passage."),

 # --------------------------------------------- Text Structure and Purpose (6)
 tsp("T1",
     "A large earthquake sends two kinds of wave through the interior of the planet: one that "
     "compresses the rock ahead of it and one that shears the rock from side to side. <u>A shearing "
     "wave cannot pass through a liquid, because a liquid offers nothing for the shear to act "
     "against.</u> Seismographs on the far side of the world record the compressional arrival and "
     "never the shearing one, and that absence is what first showed the core to be molten.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It supplies the physical principle that makes the missing arrival meaningful.",
      "It questions whether seismographs on the far side of the world are reliable.",
      "It defines the two kinds of wave named in the preceding sentence.",
      "It states a conclusion that the rest of the text goes on to dispute."],
     "A",
     "Explaining why a shearing wave stops at a liquid is what lets the absent arrival in the final "
     "sentence count as evidence of a molten core. The text never disputes that conclusion; it "
     "presents it as the finding the reasoning arrives at."),

 tsp("T2",
     "A graduate student assembling a radio survey in 1967 noticed a smear of signal returning in "
     "the same patch of sky. High-speed recordings resolved it into pulses arriving one and a third "
     "seconds apart, steadier than any clock then in service. The team spent months eliminating "
     "radar, unsuppressed car ignitions and the possibility of a message from another civilisation "
     "before settling on a natural source: a collapsed star spinning on its axis and sweeping a "
     "beam past the Earth.",
     "Which choice best states the main purpose of the text?",
     ["To recount how an unexplained signal was tracked down to a natural source.",
      "To argue that radio surveys are more productive than optical ones.",
      "To explain how a collapsed star comes to spin so rapidly.",
      "To describe the instruments used in radio surveys of the 1960s."],
     "A",
     "The text follows one anomaly from its first appearance through the elimination of "
     "alternatives to the identification of a spinning star, which is an account of detection. How "
     "a star comes to spin that fast is never explained, since the object is only named at the "
     "close."),

 tsp("T3",
     "The rings of a single tree record the growing conditions of one place, and a run of narrow "
     "rings marks a run of poor years. <u>Because those poor years fall in the same order in every "
     "tree in a district, a sequence of rings taken from a beam of unknown date can be slid along a "
     "sequence from living trees until the two patterns coincide.</u> A roof timber can be dated "
     "this way to the year the tree was felled, provided its outermost ring survives.",
     "Which choice best describes the function of the underlined sentence?",
     ["It explains the matching procedure that makes the dating in the final sentence possible.",
      "It concedes a limitation that the final sentence goes on to remove.",
      "It gives an example of a district in which the method has been used.",
      "It defines the term used for a run of narrow rings."],
     "A",
     "Sliding one ring sequence against another until the patterns line up is exactly the operation "
     "that yields the felling year named afterwards. The one limitation in the text, the survival "
     "of the outermost ring, appears in the final sentence rather than being answered by it."),

 tsp("T4",
     "Almost everything now read as Old Norse mythological poetry survives in one small book of "
     "forty-five leaves, written in Iceland in the thirteenth century and unnoticed until 1643. The "
     "poems in it are older than the book by an unknown margin, and for most of them no second copy "
     "exists anywhere. A gap of eight leaves in the middle has removed the connecting portion of a "
     "heroic cycle, and what stood there has been argued over ever since.",
     "Which choice best describes the overall structure of the text?",
     ["It identifies a unique source, notes what cannot be known about it, and points to a loss within it.",
      "It compares two manuscripts and explains why one is preferred to the other.",
      "It traces the passage of a poem from oral performance into print.",
      "It argues that the poems were composed later than is usually supposed."],
     "A",
     "The text moves from the single surviving book to the unknown age of its contents and then to "
     "the missing leaves and the dispute they left behind. No second manuscript is ever introduced, "
     "so nothing is being weighed against anything."),

 tsp("T5",
     "Calculations that treat an insect wing as a small aeroplane wing yield a lift too small to "
     "hold the animal up, and for years the discrepancy was repeated as a curiosity. <u>A wing "
     "sweeping through air at a steep angle sheds a spiral of air that clings to its upper surface "
     "instead of peeling away, and the low pressure inside that spiral pulls the wing upward.</u> "
     "Because the stroke reverses before the spiral can detach, the insect never loses the extra "
     "lift.",
     "Which choice best describes the function of the underlined sentence?",
     ["It introduces the mechanism that accounts for the discrepancy described in the first sentence.",
      "It restates the calculation reported in the first sentence in simpler terms.",
      "It concedes that the discrepancy has never been explained.",
      "It describes an experiment in which insect wings were measured."],
     "A",
     "The clinging spiral supplies lift that the aeroplane-wing calculation leaves out, which is "
     "just what the shortfall in the opening sentence requires. Far from leaving the shortfall "
     "unexplained, the closing sentence adds why the extra lift is never lost."),

 tsp("T6",
     "A signal box controls both the signals that give a driver permission to proceed and the "
     "levers that move the points beneath the track. Left to itself the arrangement lets a "
     "signalman clear a route while the points at the far end still lie for a different one. "
     "Nineteenth-century engineers answered this by locking the levers to one another in a frame of "
     "bars and notches, so that a signal cannot be pulled off unless every point in its route is "
     "already set and locked.",
     "Which choice best states the main purpose of the text?",
     ["To describe a hazard in early signalling and the mechanical answer devised for it.",
      "To argue that mechanical frames were superior to the electrical systems that followed them.",
      "To explain how points are moved beneath a running line.",
      "To trace the career of a nineteenth-century signalling engineer."],
     "A",
     "The passage states the danger of a route cleared over wrongly set points and then describes "
     "the locking frame built to prevent it. No later electrical system is mentioned at all, so "
     "nothing is being ranked against one."),

 # ----------------------------------------------- Central Ideas and Details (6)
 cid("C1",
     "Every male humpback in an ocean basin sings the same song, and the song drifts through the "
     "season as small alterations spread from one singer to the next. Recordings off eastern "
     "Australia show a song replaced outright within a single season by one that had been current "
     "further west, and the replacement then travelled eastward across the Pacific over the years "
     "that followed. The new song was not a variation on the old one: the population dropped what "
     "it had been singing and took up the arriving version whole.",
     "Which choice best states the main idea of the text?",
     ["Humpback song is learned and can be replaced wholesale by a version arriving from another population.",
      "Humpback whales sing chiefly in order to defend a feeding territory.",
      "Songs recorded off eastern Australia are longer than those recorded further west.",
      "Each humpback develops a song of its own that changes as the animal ages."],
     "A",
     "One population abandoning its song for an imported one that then spreads across an ocean is "
     "only possible if the song is copied rather than inborn. The claim that each whale has a song "
     "of its own contradicts the opening statement that all the males in a basin sing the same "
     "one."),

 cid("C2",
     "The round holes in a wheel of Alpine cheese are bubbles of gas that formed while the wheel "
     "sat in a warm room. A bacterium the makers tolerate feeds on the lactic acid left behind by "
     "the starter cultures and gives off carbon dioxide, and the paste at that stage is elastic "
     "enough to stretch around the gas rather than crack. Wheels ripened cold from the first day "
     "contain the same bacterium and stay solid.",
     "According to the text, why do wheels ripened cold lack holes?",
     ["They are made without the bacterium responsible for producing the gas.",
      "They are never given the warmth the bacterium needs to produce gas.",
      "Their paste is too elastic to hold a bubble open.",
      "The starter cultures leave no lactic acid behind in them."],
     "B",
     "The final sentence says the cold-ripened wheels hold the same bacterium and stay solid, so "
     "what they lack is the warm room in which the gas is generated. The option denying the "
     "bacterium is ruled out by that same sentence, which states that it is present."),

 cid("C3",
     "Fish and crayfish shut into cave streams for many generations lose their eyes and their "
     "colour, and the loss is not simply neglect: in some cave fish the tissue that would become an "
     "eye begins to form in the embryo and is then broken down again. Eyes are expensive to build "
     "and to run, and in permanent darkness they return nothing. Related populations that still "
     "meet daylight at a cave mouth keep both eyes and colour.",
     "Which choice best states the main idea of the text?",
     ["Cave animals lose their eyes because darkness prevents their embryos from developing normally.",
      "The loss of eyes in cave animals reflects the cost of maintaining a useless organ rather than mere disuse.",
      "Cave fish and cave crayfish are more closely related to one another than to surface species.",
      "Populations living at a cave mouth will lose their eyes in time as well."],
     "B",
     "The text stresses that eye tissue is dismantled deliberately and that eyes cost something to "
     "build and run, so the loss is presented as a saving. The claim that darkness prevents normal "
     "development is contradicted by the embryo starting to build the eye before it is removed."),

 cid("C4",
     "A stand managed by selection is entered every ten or fifteen years and a scattering of trees "
     "is taken from every size class, leaving gaps small enough that the surrounding canopy closes "
     "over them within a few seasons. The stand is never bare and never made up of trees of one "
     "age. Yields per entry are small, the roads have to be kept open permanently, and marking "
     "individual trees costs more per cubic metre than felling a block outright.",
     "Which choice best states the main idea of the text?",
     ["Selection forestry keeps a stand continuously covered and mixed in age at a higher cost per unit of timber.",
      "Selection forestry produces more timber per hectare than felling a block outright.",
      "Gaps left by selection forestry take many decades to close over.",
      "Roads are unnecessary in a stand that is managed by selection."],
     "A",
     "The first half describes a stand that is never empty and never uniform in age, and the second "
     "half lists the extra costs of working it that way. The passage puts the closing of the gaps "
     "at a few seasons, which rules out the option claiming decades."),

 cid("C5",
     "Seats in a legislature come in whole numbers and a state's exact share of them almost never "
     "does. One rule long used in the United States handed each state the whole-number part of its "
     "share and then gave the leftover seats to the states with the largest fractions. In 1880 a "
     "clerk noticed that enlarging the chamber from 299 seats to 300 would take a seat away from "
     "Alabama, because the fractions did not all grow at the same rate. Methods now in use avoid "
     "ranking fractions directly.",
     "According to the text, why would Alabama lose a seat when the chamber was enlarged?",
     ["Its population had fallen relative to that of the other states.",
      "The fractional parts of the states' shares grew unevenly as the total rose.",
      "The rule in use awarded the leftover seats to the smallest states first.",
      "A chamber of 300 seats could not be divided evenly among the states."],
     "B",
     "The text gives the reason outright: the fractions did not all grow at the same rate, so a "
     "state could slip down the ranking as the chamber grew. Nothing in the passage concerns a "
     "change in population, which is held fixed while only the number of seats varies."),

 cid("C6",
     "A yurt travels on two or three animals and is raised by two people in about an hour. Its wall "
     "is a lattice of pivoted laths that opens like a concertina and is drawn closed by a woven "
     "band; the roof poles spring from the top of that lattice to a wooden crown, and the felt goes "
     "on over the whole. Nothing in the frame is nailed, and it is the tension in the band that "
     "keeps the roof poles seated.",
     "Which choice best states the main idea of the text?",
     ["The yurt's frame is held together by tension rather than by fixed joints, which is what makes it portable.",
      "The felt covering is the heaviest part of a yurt to transport.",
      "A yurt is raised more quickly in summer than in winter.",
      "The wooden crown is the part of a yurt most often replaced."],
     "A",
     "The closing sentence says nothing is nailed and that the band's tension seats the roof poles, "
     "and the opening sentence ties the design to being carried and pitched quickly. The relative "
     "weight of the felt is never given, so no part is identified as the heaviest."),

 # ---------------------------------------------------- Command of Evidence (9)
 coe("E1",
     "A physiologist measured resting arterial oxygen saturation and resting breathing rate in four "
     "climbers on each of five mornings spent at a camp at 4,900 metres, with no further gain in "
     "height during the study. Saturation at sea level is normally about 98 per cent."
     "<table style=\"border-collapse:collapse;margin:0.75rem 0;\">"
     "<tr>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Day at 4,900 m</th>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Mean saturation (%)</th>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Mean breaths per minute</th>"
     "</tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">1</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">82</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">20</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">2</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">84</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">22</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">3</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">86</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">23</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">4</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">88</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">23</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">5</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">89</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">23</td></tr>"
     "</table>",
     "Which choice best describes data from the table that support the conclusion that the climbers "
     "were adjusting to the altitude over the five days?",
     ["Mean saturation rose from 82 per cent on the first day to 89 per cent on the fifth while the height of the camp stayed the same.",
      "Mean saturation on every day of the study was below the sea-level figure of about 98 per cent.",
      "Mean breathing rate was the same on the third, fourth and fifth days.",
      "Mean saturation on the fifth day was 89 per cent."],
     "A",
     "Adjustment shows itself as improvement over time at an unchanging height, and only the option "
     "pairing the rise from 82 to 89 per cent with the fixed camp altitude reports both halves of "
     "that. The option noting that every reading stayed below the sea-level figure describes the "
     "effect of altitude itself rather than any change across the five days."),

 coe("E2",
     "Recordings from a fixed hydrophone in the eastern Pacific show that the tonal unit of the "
     "blue whale call has fallen in pitch over several decades. One suggestion is that whales lower "
     "the pitch as ocean noise rises; another is that they can afford a lower, less far-carrying "
     "call because more whales are within range to hear it."
     "<table style=\"border-collapse:collapse;margin:0.75rem 0;\">"
     "<tr>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Decade</th>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Mean call frequency (hertz)</th>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Estimated whales in the region</th>"
     "</tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">1970s</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">22.0</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">1,200</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">1980s</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">20.5</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">1,600</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">1990s</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">19.0</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">2,300</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">2000s</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">17.5</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">3,400</td></tr>"
     "</table>",
     "Which choice best describes data from the table that support the second suggestion?",
     ["Mean call frequency fell in every decade in which the estimated number of whales in the region rose.",
      "The estimated number of whales in the region roughly tripled between the 1970s and the 2000s.",
      "Mean call frequency in the 2000s was 17.5 hertz.",
      "Mean call frequency fell by 1.5 hertz between the 1970s and the 1980s."],
     "A",
     "The second suggestion ties falling pitch to rising numbers of whales within earshot, so the "
     "support has to bring the two columns together, which only the option tracking the fall "
     "against the rise does. Reporting the tripling of the population on its own leaves the pitch "
     "out and so cannot connect the two."),

 coe("E3",
     "A dairy scientist followed twelve wheels of a washed-rind cheese through eight weeks in the "
     "ripening room, recording the pH and the moisture of the paste and having the wheels tasted "
     "each fortnight. Bitterness in this style is generally blamed on peptides that are broken down "
     "further only once the paste has stopped being acid."
     "<table style=\"border-collapse:collapse;margin:0.75rem 0;\">"
     "<tr>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Week</th>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">pH of paste</th>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Moisture (%)</th>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Wheels judged bitter (of 12)</th>"
     "</tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">2</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">5.2</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">46</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">9</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">4</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">5.6</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">44</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">5</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">6</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">6.0</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">42</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">2</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">8</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">6.3</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">40</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">0</td></tr>"
     "</table>",
     "Which choice best describes data from the table that support the explanation of bitterness "
     "given in the text?",
     ["The number of wheels judged bitter fell at every fortnight in which the pH of the paste rose.",
      "The moisture of the paste fell steadily from week 2 to week 8.",
      "The pH of the paste reached 6.3 by week 8.",
      "Nine of the twelve wheels were judged bitter at week 2."],
     "A",
     "The explanation has bitterness disappearing once the paste stops being acid, so the support "
     "must set rising pH beside falling bitterness, which only one option does. The steady fall in "
     "moisture is real in the table, but the text never links moisture to bitterness at all."),

 coe("E4",
     "In <em>The Saga of Hrafn of Grimsdal</em>, an anonymous Icelandic prose narrative, the farmer "
     "Hrafn is put off his land by a neighbour and takes no revenge for eleven years. A scholar "
     "argues that the saga presents Hrafn's long silence as a deliberate strategy rather than as "
     "weakness.",
     "Which quotation from <em>The Saga of Hrafn of Grimsdal</em> most effectively illustrates the scholar's claim?",
     ["&ldquo;Hrafn said nothing when the boundary stones were moved, and men thought the less of him for it.&rdquo;",
      "&ldquo;Hrafn counted the winters as a man counts coin, and said that a case is worth more at the Thing than a body is in a ditch.&rdquo;",
      "&ldquo;It was a hard winter, and the sheep were brought down early from the upper pasture.&rdquo;",
      "&ldquo;Hrafn's wife asked whether he meant to sit by the fire until he died there.&rdquo;"],
     "B",
     "The claim is that the silence was a plan, and only the quotation in which Hrafn weighs the "
     "passing winters and prefers a case at the assembly to a killing shows him choosing to wait. "
     "The quotation reporting that men thought the less of him records how others read the silence, "
     "which is the impression the claim is arguing against."),

 coe("E5",
     "In the novel <em>The Ash Fall</em>, a young geologist returns to the farm she left as a child "
     "and spends her first days walking the moraine above it. A critic argues that the narrator's "
     "close attention to rock and weather is a way of putting off the conversation she has come "
     "home to have.",
     "Which quotation from <em>The Ash Fall</em> most effectively illustrates the critic's claim?",
     ["&ldquo;The moraine was well sorted, the cobbles laid down by meltwater rather than dropped from the ice, and I catalogued them all afternoon while my mother waited in the kitchen.&rdquo;",
      "&ldquo;The farm was smaller than I remembered, and the roof had been mended with sheeting that did not match.&rdquo;",
      "&ldquo;My mother asked what I had been doing on the hill, and I told her about the meltwater until she laughed.&rdquo;",
      "&ldquo;Ash from the eruption lay across the pasture in a grey band a finger deep.&rdquo;"],
     "A",
     "The claim requires the landscape to stand between the narrator and the meeting she is "
     "avoiding, and only the quotation setting an afternoon of cataloguing cobbles against a mother "
     "waiting indoors puts the two side by side. The quotation in which she answers her mother's "
     "question shows the conversation taking place rather than being deferred."),

 coe("E6",
     "Skaldic poetry names things by compound substitution: a ship becomes a horse of the sea, gold "
     "the fire of the river. A scholar argues that in the verses attributed to the tenth-century "
     "poet Ulf the Silent these substitutions are not decoration but a means of forcing two unlike "
     "activities to be seen as one.",
     "Which quotation from Ulf's verses most effectively illustrates the scholar's claim?",
     ["&ldquo;The wave-horse ran, and the sail was wide.&rdquo;",
      "&ldquo;We sowed the sea-field with oars and reaped a harvest of salt; the ploughman ashore knows nothing of that tillage.&rdquo;",
      "&ldquo;Ulf made this verse in the winter that the ice came early.&rdquo;",
      "&ldquo;Gold is called the fire of the river by the poets of the north.&rdquo;"],
     "B",
     "The claim is that a substitution makes two unlike activities read as one, and only the "
     "quotation carrying rowing right through the vocabulary of sowing, reaping and tillage does "
     "that. The quotation calling a ship a wave-horse is a substitution but stands alone, with no "
     "second activity drawn into it."),

 coe("E7",
     "Climbers who spend a fortnight above 5,000 metres lose muscle even when they are generously "
     "fed. Physiologist Ingrid S&aelig;ther argues that the loss is caused by the shortage of "
     "oxygen itself rather than by the reduced appetite that also sets in at altitude.",
     "Which finding, if true, would most directly support S&aelig;ther's argument?",
     ["Volunteers held for a fortnight in a low-oxygen chamber at sea level, on a diet they finished in full each day, lost muscle at the same rate as climbers at altitude.",
      "Climbers at altitude report eating roughly a third fewer calories than they do at home.",
      "Muscle lost during an expedition is regained within a few weeks of the return to sea level.",
      "Cold slows the rate at which muscle protein is rebuilt."],
     "A",
     "Feeding the volunteers a full diet removes the appetite explanation while leaving the oxygen "
     "shortage in place, so muscle lost anyway points at the oxygen. The finding that climbers eat "
     "a third less supports the very explanation the argument is set against."),

 coe("E8",
     "A midge beats its wings a thousand times a second, far faster than a nerve can deliver "
     "separate commands. Entomologist Rafael Duarte argues that the wingbeat rate is set by the "
     "mechanical resonance of the thorax rather than by the rate at which signals arrive at the "
     "muscle.",
     "Which finding, if true, would most directly support Duarte's argument?",
     ["Gluing a trace of extra mass to the wings lowers the wingbeat rate by exactly the amount a resonating system predicts, while the rate of nerve signals to the muscle is unchanged.",
      "The thorax of a midge is a stiff box whose walls are deformed by the flight muscle.",
      "Midges beat their wings more slowly in cold air than in warm air.",
      "A midge that loses part of one wing flies in circles."],
     "A",
     "Loading the wings alters the mechanical system while leaving the nerve traffic untouched, so "
     "a rate that shifts by exactly the predicted amount is what resonance requires. Describing the "
     "thorax as a stiff deformable box shows only that a structure capable of resonating exists, "
     "not that it rather than the nerve sets the rate."),

 coe("E9",
     "Wells drawing on one aquifer interfere with each other: pumping at one lowers the water table "
     "at the next. Economist Hana Bergstr&ouml;m argues that the fall in the water table beneath "
     "one irrigation district was halted by the metering and transferable pumping quota introduced "
     "there, rather than by the run of wetter years that began at about the same time.",
     "Which finding, if true, would most directly support Bergstr&ouml;m's argument?",
     ["Neighbouring districts drawing on the same aquifer, which had the same wetter years but no metering, went on losing water table at the earlier rate.",
      "Rainfall across the region in the years after the quota was introduced was above the long-term average.",
      "Farmers in the district traded a quarter of the quota among themselves in the first three years.",
      "The aquifer is recharged mainly by rain falling on its outcrop at the edge of the district."],
     "A",
     "The wetter years fell on the neighbouring districts as well, so a water table that steadied "
     "only where the quota was imposed isolates the quota as the cause. Above-average rainfall "
     "after the change supports the rival explanation rather than this one."),

 # -------------------------------------------------------------- Inferences (6)
 inf("I1",
     "A radio dish focuses the waves it collects only if its surface departs from a true paraboloid "
     "by much less than the wavelength being observed. Panels can be set to within a fraction of a "
     "millimetre, but a large dish also sags under its own weight as it tips, and the sag changes "
     "with the angle at which it is pointed. A dish built to work at centimetre wavelengths can "
     "therefore be enlarged much further than one intended for _____",
     ["the same wavelengths at a fixed elevation.",
      "wavelengths of a millimetre or less.",
      "sources that are unusually faint.",
      "observations made only at night."],
     "B",
     "The tolerance is set by the wavelength, so a shorter wavelength leaves less room for sag and "
     "caps the diameter sooner. The option about faint sources concerns how much signal is "
     "gathered, which the passage never ties to the accuracy of the surface."),

 inf("I2",
     "Loose sand below the water table holds itself up through the contact between its grains. "
     "Shaking packs the grains closer, and because the water between them cannot escape quickly, "
     "the water takes up the load and the grain contacts are relieved of it. Ground in that state "
     "carries no more than a heavy liquid does, which means that a building founded on it during an "
     "earthquake is most at risk of _____",
     ["being shaken apart by the vibration itself.",
      "sinking or tilting while otherwise remaining intact.",
      "sliding downhill along a buried fault.",
      "catching fire from ruptured mains."],
     "B",
     "If the ground behaves as a liquid, a building resting on it loses its support from below and "
     "settles or leans, which is a failure of the foundation rather than of the frame. Being shaken "
     "apart describes damage done by the vibration, whereas the passage's point is that the ground "
     "itself stops bearing load."),

 inf("I3",
     "Satellite positioning returns heights measured from a smooth mathematical ellipsoid fitted to "
     "the planet as a whole. Water, however, settles according to gravity, and gravity varies with "
     "the rock beneath: the surface gravity defines rises over dense mountain roots and falls over "
     "deep sedimentary basins, departing from the ellipsoid by as much as a hundred metres. An "
     "engineer laying a canal that must run downhill the whole way therefore cannot rely on _____",
     ["a survey carried out with satellite receivers alone.",
      "measurements taken during the winter months.",
      "any height measured more than a century ago.",
      "the precision of modern satellite positioning."],
     "A",
     "Water follows the gravity surface while a satellite height is reckoned from the ellipsoid, so "
     "satellite heights on their own can send a canal uphill even as the numbers fall. The option "
     "doubting the precision of satellite positioning mistakes the problem, which is not error but "
     "the wrong reference surface."),

 inf("I4",
     "Air moves in and out of some caves through a single small opening, at times hard enough to be "
     "heard. The direction depends on the difference between the temperature inside, which stays "
     "near the local annual mean all year, and the temperature outside. Cavers who feel cold air "
     "pouring steadily out of a crack in a limestone hillside in August can reasonably conclude "
     "that the crack opens into _____",
     ["a passage that has been surveyed before.",
      "a space of substantial volume beyond it.",
      "an underground stream in flood.",
      "a chamber holding standing water."],
     "B",
     "A steady outward current in the warmest month means a large body of cool air is being "
     "displaced, which requires substantial space behind the opening. Standing water can occur in "
     "any cave and has nothing to do with the volume of air moving through the crack."),

 inf("I5",
     "Most mammals stop producing the enzyme that digests milk sugar soon after weaning, and most "
     "human adults do the same. In several herding populations, however, a change in the control "
     "region of the gene keeps production going for life, and the change has arisen by different "
     "routes in Europe, in Arabia and in East Africa. That the same ability appeared separately in "
     "each of these regions suggests that the benefit of digesting fresh milk was _____",
     ["restricted to populations that also grew cereals.",
      "great enough to be favoured wherever herds were kept.",
      "confined to periods of famine.",
      "smaller in Europe than in East Africa."],
     "B",
     "One trait arising by three separate routes among herders points to a strong advantage "
     "attached to keeping animals wherever it occurred. The famine option would account for an "
     "occasional advantage, but a benefit that rare would not fix the trait independently three "
     "times over."),

 inf("I6",
     "A steel rail lengthens by about a centimetre in every hundred metres for each ten degrees it "
     "warms. Jointed track left a gap at each rail end to take that movement, at the cost of a "
     "hammering that wore out rail and wheel alike. Continuous welded rail has no gaps; the rails "
     "are instead stretched to a set tension as they are fastened down, which means that track of "
     "this kind can only be laid _____",
     ["on ballast that traffic has already packed.",
      "within a defined range of temperature.",
      "where the line runs straight for long distances.",
      "by machine rather than by hand."],
     "B",
     "Fastening rail at a set tension only works if the steel is at a known temperature when it is "
     "fixed, since the tension it holds afterwards depends on how far conditions have moved from "
     "that point. Straightness matters for other reasons, but nothing in the passage links thermal "
     "expansion to curvature."),

 # --------------------------------------------------------------- Boundaries (12)
 bnd("B1",
     "Headache, nausea and broken sleep appear in perhaps a quarter of people who climb above three "
     "thousand metres in a single day. The standard advice is to gain no more than three hundred "
     "metres of sleeping height a day and to go down at once if the symptoms _____ acetazolamide, "
     "which makes the blood slightly acid and so prompts deeper breathing, is often carried as "
     "well.",
     ["worsen; acetazolamide", "worsen, acetazolamide", "worsen acetazolamide",
      "worsen: and acetazolamide"],
     "A",
     "Each side of the blank is a complete statement and no conjunction joins them, so the "
     "semicolon is the mark that will do the work. Joining them with nothing but a comma produces a "
     "splice."),

 bnd("B2",
     "A deed written by metes and bounds walks the reader around a parcel from one landmark to the "
     "next, and the landmarks were often perishable. The surveyors sent west after 1785 worked "
     "instead from a system that needed no landmarks at _____ north&ndash;south principal meridian, "
     "an east&ndash;west base line, and townships six miles square counted off from where the two "
     "cross.",
     ["all: a", "all; a", "all, and a", "all a"],
     "A",
     "The words in front of the blank form a complete sentence, and what follows is a list naming "
     "the parts of the system, which is the colon's proper use. The semicolon would require a full "
     "sentence after it, and a list of noun phrases is not one."),

 bnd("B3",
     "A track circuit passes a small current through one rail and back along the other, and the "
     "axles of a train short it out. Because the relay at the far end of the section drops as soon "
     "as that current is _____ engineers describe the arrangement as failing safe: a broken wire "
     "produces exactly the indication an occupied line would.",
     ["diverted, signalling", "diverted; signalling", "diverted: signalling",
      "diverted and signalling"],
     "A",
     "The clause opening with 'Because' is dependent and must be closed with a comma before the "
     "main clause starts. The semicolon and the colon both need a complete sentence in front of "
     "them, and a dependent clause is not one."),

 bnd("B4",
     "Rivers carried timber out of country that had no roads, and a mill could stand a hundred "
     "miles below the felling. The river driver, a man who walked the moving logs with a pole and a "
     "pair of spiked _____ the jams apart at the head of the run and rode the loose wood down.",
     ["boots, broke", "boots; broke", "boots: broke", "boots broke"],
     "A",
     "The appositive beginning 'a man who walked' was opened with a comma and has to be closed with "
     "a matching comma before the verb belonging to the subject. Leaving the punctuation out runs "
     "the description straight into the predicate."),

 bnd("B5",
     "An earthquake warning system predicts nothing; it detects the fast compressional wave at "
     "stations near the source and sends word ahead of the slower shaking that does the damage. "
     "Where the distance is short &mdash; a city standing almost on the fault, for _____ arrives "
     "too late to be of any use.",
     ["instance &mdash; the warning", "instance, the warning", "instance; the warning",
      "instance: the warning"],
     "A",
     "The interruption was opened with a dash, so it has to be closed with a matching dash before "
     "the sentence resumes. Closing it with a comma leaves the opening dash without a partner and "
     "blurs where the interruption ends."),

 bnd("B6",
     "The Kushan kings ruled from the Oxus to the Ganges and struck coins in gold and copper for "
     "two centuries. The legends on those coins run in Greek script and the deities on their "
     "reverses are Iranian, Greek and Indian by _____ coinage is one of the few sources showing how "
     "the dynasty presented itself to each of the populations it governed.",
     ["turns; the", "turns, the", "turns the", "turns: and the"],
     "A",
     "Two complete statements meet at the blank with no conjunction between them, which is what the "
     "semicolon is for. The comma on its own leaves a splice, and putting a conjunction after a "
     "colon adds one where that mark does not take it."),

 bnd("B7",
     "A water strider's legs are covered in hairs so fine and so densely packed that water cannot "
     "get between them, and each foot rests in a dimple on the surface rather than in the water. "
     "The insect is far denser than the liquid it stands _____ it never breaks through unless the "
     "surface has been fouled with detergent.",
     ["on, and", "on; and", "on: and", "on and"],
     "A",
     "Two independent clauses joined by the coordinating conjunction 'and' take a comma in front of "
     "that conjunction. The semicolon and the colon are not used before a coordinating conjunction, "
     "and dropping the comma leaves two full clauses unseparated."),

 bnd("B8",
     "A radio telescope collects signals measured in fractions of a millionth of a millionth of a "
     "watt, and a mobile phone on a nearby hill outshines every object in the sky. Although the "
     "observatory at Green Bank sits inside a zone in which transmitters are restricted by _____ "
     "engineers still drive the local roads with a receiver, hunting for a faulty microwave oven.",
     ["law, its", "law; its", "law: its", "law and its"],
     "A",
     "'Although' opens a dependent clause, and a dependent clause standing in front of the main "
     "clause is separated from it by a comma. The semicolon would demand an independent clause on "
     "both sides of it."),

 bnd("B9",
     "Most limestone caves are dissolved from above by rain made weakly acid in the soil. "
     "Lechuguilla was dissolved from below, and the evidence consists of three features found "
     "nowhere in an ordinary _____ blocks of gypsum left behind as a residue, sulphur crusts on the "
     "walls, and passages that climb instead of following the water table.",
     ["cave: massive", "cave; massive", "cave, and massive", "cave massive"],
     "A",
     "What stands before the blank is a complete sentence announcing three features, and the colon "
     "introduces the list that names them. The semicolon would demand a full sentence after it, "
     "which a string of noun phrases is not."),

 bnd("B10",
     "A right to divert water in the western states is held only for as long as the water is "
     "actually put to a use the law counts as beneficial. A farmer who lines a leaking ditch and "
     "needs less water as a result may find the saved portion forfeit rather than _____ rule "
     "written to stop hoarding now discourages the very efficiency it was meant to encourage.",
     ["retained; the", "retained, the", "retained the", "retained: and the"],
     "A",
     "The blank falls between two complete statements with no conjunction, which is the semicolon's "
     "use. A comma on its own would splice them, and no punctuation at all would run them "
     "together."),

 bnd("B11",
     "A rule that compares candidates in pairs can return a majority for one candidate over a "
     "second, for the second over a third, and for the third over the first. When those three "
     "results are set out in a _____ candidate can be said to have beaten every rival, and the rule "
     "produces no winner at all.",
     ["row, no", "row; no", "row: no", "row and no"],
     "A",
     "A subordinate clause opening with 'When' comes in front of the main clause here and is closed "
     "off from it by a comma. Neither the semicolon nor the colon may follow a clause that cannot "
     "stand on its own."),

 bnd("B12",
     "A rorqual takes in a volume of water larger than its own body in one lunge and then forces it "
     "out again through the baleen. The throat is built for exactly that _____ running from the "
     "chin to the navel and opening like a bellows under the load.",
     ["job: pleats", "job; pleats", "job, and pleats", "job pleats"],
     "A",
     "The words before the blank make a complete statement and what follows names what the "
     "structure consists of, which the colon introduces. The semicolon would need an independent "
     "clause after it, and a noun with a participial phrase hanging on it is not one."),

 # ------------------------------------------------ Form, Structure, and Sense (9)
 fss("F1",
     "The hut warden keeps a log of every party that goes up and comes back down, and the entries "
     "are checked each evening against the boots left in the porch. Neither the guide nor the two "
     "clients _____ signed the book on the morning they set out for the col.",
     ["has", "have", "was", "is"], "B",
     "With 'neither ... nor', the verb agrees with whichever subject stands nearer to it, and 'the "
     "two clients' is plural."),

 fss("F2",
     "A plane table is a drawing board on a tripod, and the map grows on it in the field rather "
     "than back in an office. The board's collection of sight rules, together with several boxwood "
     "scales, _____ kept in a felt-lined case.",
     ["are", "have been", "were", "was"], "D",
     "The subject is the singular noun 'collection'; the interrupting phrase beginning 'together "
     "with' does not turn a singular subject plural."),

 fss("F3",
     "The box at the junction was rebuilt in stages and worked with a temporary frame for most of a "
     "year. By the time the new colour-light signals were commissioned in October, every semaphore "
     "arm on the approach _____ already been taken down.",
     ["has", "had", "will have", "is"], "B",
     "The removal was finished before the commissioning, and the commissioning is itself in the "
     "past, so the past perfect is the tense that places one past event before another."),

 fss("F4",
     "The mill runs two shifts and stops only to change a blade. Each of the four saws _____ its "
     "own set of guides and a jet of water to carry the sawdust away.",
     ["have", "has", "having", "were having"], "B",
     "'Each' is the subject and is singular; the prepositional phrase naming four saws does not "
     "alter the number of the subject."),

 fss("F5",
     "The church has been shut since a survey found the tower leaning, and the grant took four "
     "years to obtain. The money is to tie the walls to the floors, to grout the rubble core and "
     "_____ the roof to the masonry beneath it.",
     ["fixing", "to fix", "it fixes", "having fixed"], "B",
     "The three items joined by 'and' all follow 'is to', and the first two are infinitives, so the "
     "third must be an infinitive as well. The gerund and the finite clause both break the parallel "
     "structure."),

 fss("F6",
     "The array is worked through the night from a control room a mile from the nearest dish, and a "
     "fault on one antenna is easy to miss among twenty-seven. Scanning the recorded data the "
     "following morning, _____",
     ["one antenna's readings were plainly wrong.",
      "the wrong readings came from a single antenna.",
      "the duty astronomer saw that one antenna's readings were wrong.",
      "there was one antenna with wrong readings."],
     "C",
     "The opening participial phrase has to describe whoever did the scanning, and only the option "
     "beginning with the duty astronomer supplies that person. Beginning with the readings says the "
     "data were scanning themselves."),

 fss("F7",
     "A co-operative creamery takes milk from thirty farms and pays for it on butterfat and "
     "protein. Every farm that supplies the creamery must have _____ bulk tank tested twice a year, "
     "and a sample is drawn at each collection.",
     ["their", "its", "there", "it's"], "B",
     "The antecedent is the singular 'Every farm', so the singular possessive is required. The "
     "plural possessive would need a plural antecedent, and the spelling with an apostrophe is the "
     "contraction of 'it is'."),

 fss("F8",
     "Not every tree planted along a street survives its first two summers, and the borough makes "
     "good the losses each winter. The number of young limes lost to drought last year _____ higher "
     "than in any year since the planting programme began.",
     ["were", "have been", "was", "are"], "C",
     "'The number of' takes a singular verb, because the subject is the count itself rather than "
     "the trees being counted."),

 fss("F9",
     "Very few of the bays along this coast have been watched with any consistency, and most of the "
     "records that exist break off in the 1980s. This inlet is one of the few sites in the region "
     "that _____ been surveyed for whales every summer since 1979.",
     ["has", "have", "having", "is"], "B",
     "The relative pronoun 'that' refers back to 'sites', which is plural, so the plural verb is "
     "required; the singular would agree with 'one' instead, which is not what the clause "
     "describes."),

 # -------------------------------------------------------------- Transitions (9)
 trn("N1",
     "Living for several weeks at 2,500 metres raises the oxygen-carrying capacity of an endurance "
     "athlete's blood. _____ hard interval sessions cannot be run as fast at that height, and the "
     "loss of training quality can cancel the gain. Coaches now have athletes sleep high and drive "
     "down to a valley track to train.",
     ["However,", "Consequently,", "Likewise,", "For instance,"], "A",
     "The drawback works against the benefit stated in the first sentence, so the transition has to "
     "mark a contrast rather than a consequence."),

 trn("N2",
     "Brunel laid his line to a gauge of just over seven feet, and his carriages rode more steadily "
     "than those on the narrower track used elsewhere. _____ every wagon reaching the boundary "
     "between the two systems had to be unloaded and its contents carried across to another wagon.",
     ["In other words,", "Even so,", "For example,", "Similarly,"], "B",
     "Transhipment at the boundary is a cost standing against the smoother ride just praised, so "
     "the transition concedes a drawback. Treating the second sentence as a restatement would be "
     "wrong, since it introduces a new fact rather than rephrasing the first."),

 trn("N3",
     "Freshly felled oak holds about as much water as it does wood, and it shrinks across the grain "
     "as that water leaves. _____ a board cut to size while still green will be narrower, and "
     "possibly cupped, by the time it comes to be fitted.",
     ["Nevertheless,", "As a result,", "By contrast,", "In other words,"], "B",
     "The narrowed and cupped board follows directly from the shrinkage described first, which is a "
     "cause-and-effect relation. Calling it a restatement would be wrong because the second "
     "sentence adds a consequence rather than rephrasing the first."),

 trn("N4",
     "A tall building sways in a strong wind at a period fixed by its height and its stiffness, and "
     "the sway is uncomfortable long before it is dangerous. A heavy block hung near the top on "
     "springs and dampers can be tuned to swing against that motion. _____ the same device does "
     "much less for the short, sharp movements of an earthquake, which arrive across a wide range "
     "of periods.",
     ["Therefore,", "However,", "Likewise,", "In short,"], "B",
     "The device's poor showing in an earthquake works against the usefulness just described, so a "
     "contrastive transition is called for. A consequence transition would make the performance in "
     "wind the cause of the shortcoming in an earthquake."),

 trn("N5",
     "An observatory can shelter from transmitters on the ground by sitting in a valley and asking "
     "its neighbours to switch things off. _____ satellite constellations broadcast from directly "
     "overhead, where no hill stands between the transmitter and the dish.",
     ["By contrast,", "For example,", "Consequently,", "In addition,"], "A",
     "A source overhead defeats the very shelter that works against transmitters on the ground, so "
     "the two cases are being set against each other. Presenting the satellites as one more item on "
     "a list would hide the fact that the protection described fails against them."),

 trn("N6",
     "Surface water in the western states has been allocated by dated rights for well over a "
     "century, and a river's flow can be watched as it is taken. _____ groundwater in many of the "
     "same states was pumped for decades under no rule at all, because a well is out of sight and "
     "its effect on a neighbour's well takes years to appear.",
     ["By contrast,", "As a result,", "For instance,", "In other words,"], "A",
     "The passage sets an old and visible system of surface allocation against an unregulated and "
     "invisible one underground, so the transition marks a difference. Nothing in the second "
     "sentence follows from the first, which rules out the consequence transition."),

 trn("N7",
     "A street planted with a single species matures evenly, and every tree along it can be pruned "
     "on the same cycle. _____ a disease that finds one of those trees will find all of them, which "
     "is what happened to the elms of North American cities in the middle of the twentieth century.",
     ["Likewise,", "For this reason,", "However,", "In fact,"], "C",
     "The vulnerability of a uniform planting is a drawback set against the convenience just "
     "described, so the transition has to mark a contrast. A result transition would make the "
     "shared pruning cycle the cause of the disease spreading."),

 trn("N8",
     "A voting rule worth trusting ought to respect a unanimous preference, ought to ignore "
     "candidates who are not in the running when comparing two who are, and ought not to hand the "
     "decision to a single voter. _____ Kenneth Arrow showed in 1951 that no rule ranking three or "
     "more options can satisfy all of these at once.",
     ["Nevertheless,", "For instance,", "Similarly,", "In short,"], "A",
     "The proof denies that the reasonable-sounding requirements just listed can be met together, "
     "so the transition marks a reversal of expectation. Offering the theorem as an instance of "
     "those requirements would misstate what it establishes."),

 trn("N9",
     "Heating milk before it is made into cheese kills the bacteria that cause disease and also the "
     "mixed population that would otherwise ripen the paste in its own way. _____ a pasteurised "
     "cheese depends entirely on the cultures the maker adds, and its flavour is more predictable "
     "and narrower than that of a cheese made from raw milk.",
     ["Nevertheless,", "As a result,", "By contrast,", "For example,"], "B",
     "Reliance on added cultures follows from the heat having removed the milk's own population, so "
     "the relation is cause and effect. A contrastive transition would set the two sentences "
     "against each other when the second states the outcome of the first."),

 # ------------------------------------------------------ Rhetorical Synthesis (9)
 syn("R1",
     ["Before 1978 it was widely held that Everest could not be climbed without supplementary oxygen.",
      "Physiologists had calculated that the pressure at the summit left too little oxygen for useful work.",
      "Reinhold Messner and Peter Habeler reached the summit without oxygen sets in May 1978.",
      "Measurements taken on the summit in 1981 found the pressure higher than the standard atmospheric model predicted.",
      "The extra pressure comes from a bulge in the atmosphere over the equator that is greatest in the northern summer."],
     "explain why the summit proved to be within reach without supplementary oxygen.",
     ["Reinhold Messner and Peter Habeler reached the summit without oxygen sets in May 1978.",
      "Because the atmosphere bulges over the equator, the pressure at the summit is higher than the standard model predicted, leaving more oxygen than the earlier calculations allowed for.",
      "Physiologists had calculated that too little oxygen was available at the summit for useful work.",
      "Before 1978 it was widely held that Everest could not be climbed without supplementary oxygen."],
     "B",
     "The goal asks for the reason the climb turned out to be possible, and only the option "
     "connecting the equatorial bulge to a pressure higher than the calculations assumed supplies "
     "one. Naming the two climbers reports that it was done without saying how it could be."),

 syn("R2",
     ["Australia sits on a plate that moves about seven centimetres a year to the north-east.",
      "The national coordinate framework was last fixed to the ground in 1994.",
      "By 2020 positions measured by satellite differed from the 1994 framework by about 1.8 metres.",
      "Machinery that steers itself by satellite works to a few centimetres.",
      "A new framework was adopted that states where a point will lie in 2020 and how fast it is moving."],
     "explain why the older framework had to be replaced.",
     ["Australia sits on a plate that moves about seven centimetres a year to the north-east.",
      "The national coordinate framework was last fixed to the ground in 1994.",
      "Because the continent had drifted about 1.8 metres from its 1994 positions, a framework fixed in that year could no longer serve machinery that steers itself to a few centimetres.",
      "A new framework was adopted that states where a point will lie in 2020 and how fast it is moving."],
     "C",
     "The goal asks what forced the change, and only the option setting the accumulated drift of "
     "1.8 metres against equipment working to centimetres names a problem the old framework could "
     "not solve. Describing the new framework reports the remedy rather than the reason for it."),

 syn("R3",
     ["A single line worked in both directions can carry a head-on collision if two trains are admitted at once.",
      "Under the staff-and-ticket system only the driver holding a metal staff could enter the section.",
      "A second train could follow the first if the signalman showed the staff and issued a paper ticket.",
      "Electric token instruments were introduced in the 1880s and hold a set of tokens at each end of the section.",
      "The instruments are wired so that only one token can be out of the machines at any moment."],
     "explain how the electric instruments improved on the staff-and-ticket arrangement.",
     ["Under the staff-and-ticket system only the driver holding a metal staff could enter the section.",
      "Electric token instruments were introduced in the 1880s and hold a set of tokens at each end of the section.",
      "Because the instruments are wired so that only one token can leave them at a time, the electric system enforced through machinery a rule that staff and ticket had left in the signalman's keeping.",
      "A single line worked in both directions can carry a head-on collision if two trains are admitted at once."],
     "C",
     "The goal is the improvement, and only the option contrasting a rule enforced by the wiring "
     "with one previously entrusted to a person states what changed. Giving the date of "
     "introduction and the position of the tokens describes the device without saying what it made "
     "safer."),

 syn("R4",
     ["A cave map is drawn from measurements taken underground, station by station.",
      "A rough sketch made from memory is recorded as a grade 1 survey.",
      "A grade 5 survey uses a calibrated compass and clinometer and a tape measured between stations.",
      "In a grade 5 survey the passage walls are plotted from measurements at each station rather than sketched.",
      "The grade is printed on the finished map."],
     "explain why the grade is printed on the finished map.",
     ["A grade 5 survey uses a calibrated compass and clinometer and a tape measured between stations.",
      "Because the grade records how the measurements were taken, a later party can judge how far the map may be trusted before relying on it.",
      "A rough sketch made from memory is recorded as a grade 1 survey.",
      "A cave map is drawn from measurements taken underground, station by station."],
     "B",
     "The goal asks for the point of printing the grade, and only the option tying the recorded "
     "grade to a later party's judgement of the map's reliability gives one. Describing the "
     "instruments behind a grade 5 survey explains what a grade means without saying why the label "
     "is published."),

 syn("R5",
     ["Rice terraces on Bali are watered from streams through a network of tunnels and channels.",
      "A subak is an association of the farmers who draw from one channel.",
      "Water temples set the dates on which each subak floods and drains its terraces.",
      "Flooding a whole block of terraces at once drowns the pests living in it.",
      "Staggering the dates between neighbouring blocks keeps peak demand within what the stream can supply."],
     "explain why the timing is set by the temple calendar rather than left to each subak.",
     ["A subak is an association of the farmers who draw from one channel.",
      "Water temples set the dates on which each subak floods and drains its terraces.",
      "Coordinating the dates across subaks both drowns the pests in a whole block at once and keeps peak demand within the stream's supply, neither of which a subak deciding alone could achieve.",
      "Rice terraces on Bali are watered from streams through a network of tunnels and channels."],
     "C",
     "The goal asks why the timing is set centrally, and only the option naming the two benefits "
     "that require several subaks to act together answers it. Stating that the temples set the "
     "dates repeats the arrangement without giving any reason for it."),

 syn("R6",
     ["A city forestry department competes for money with roads and drains.",
      "Software developed by the US Forest Service estimates what a tree canopy does in measurable terms.",
      "Its inputs include the species, the trunk diameter and the position of each tree in a sample.",
      "Its outputs include the rainfall intercepted, the pollutants removed and the energy saved on cooling, each priced in dollars.",
      "A survey of one city's canopy returned an annual benefit of about 26 dollars for every dollar spent on maintenance."],
     "explain how the software helps a forestry department make its case for funding.",
     ["Software developed by the US Forest Service estimates what a tree canopy does in measurable terms.",
      "Its inputs include the species, the trunk diameter and the position of each tree in a sample.",
      "By pricing the rainfall, pollution and cooling benefits of a canopy, the software allowed one city to show a return of about 26 dollars a year for every dollar spent on maintenance.",
      "A city forestry department competes for money with roads and drains."],
     "C",
     "The goal is how the tool helps in a contest for money, and only the option turning canopy "
     "benefits into a stated return per dollar shows the argument actually being made. Listing the "
     "inputs describes how the software works without showing what it produces at a budget "
     "hearing."),

 syn("R7",
     ["A legislative map can be drawn to favour one party while giving every district an equal population.",
      "Courts have often asked whether a district is compact in shape.",
      "One compactness score divides a district's area by the area of the smallest circle enclosing it.",
      "A coastline or a winding river can give an honestly drawn district a very low score.",
      "Newer tests compare a proposed map with thousands of maps generated at random under the same rules."],
     "explain why the newer tests were developed.",
     ["One compactness score divides a district's area by the area of the smallest circle enclosing it.",
      "Because a shape score penalises districts that merely follow a coastline or a winding river, the newer tests judge a map against thousands of alternatives drawn under the same rules instead.",
      "Courts have often asked whether a district is compact in shape.",
      "A legislative map can be drawn to favour one party while giving every district an equal population."],
     "B",
     "The goal asks what the newer tests were for, and only the option naming the weakness of a "
     "shape score and the comparison that replaces it gives a reason. Defining the circle-based "
     "score explains the older measure without saying why anything had to succeed it."),

 syn("R8",
     ["A group of humpbacks feeding on herring may dive together beneath the school.",
      "One whale swims a rising spiral while releasing a curtain of bubbles.",
      "Herring will not swim through the curtain and pack into the ring it encloses.",
      "The whales then rise through the ring with their mouths open.",
      "The same individuals off south-east Alaska have been recorded feeding together for more than a decade."],
     "explain how the bubbles make the group's feeding effective.",
     ["A group of humpbacks feeding on herring may dive together beneath the school.",
      "Because herring will not cross a curtain of bubbles, the rising spiral released by one whale packs the school into a ring through which the group can rise with open mouths.",
      "The same individuals off south-east Alaska have been recorded feeding together for more than a decade.",
      "One whale swims a rising spiral while releasing a curtain of bubbles."],
     "B",
     "The goal asks how the bubbles do the work, and only the option joining the fish's refusal to "
     "cross the curtain to the ring the whales rise through explains the effect. Reporting that one "
     "whale releases a spiral of bubbles describes the action without saying what it accomplishes."),

 syn("R9",
     ["A single cow's milk in one day yields far too little for a wheel of the size the Alpine trade wanted.",
      "Wheels of forty kilograms keep and travel better than small ones.",
      "From the thirteenth century villages pooled the day's milk from every household's cows.",
      "Each household was credited with the milk it contributed and drew wheels in proportion later in the year.",
      "The arrangement was recorded in writing and audited by elected villagers."],
     "explain why the villages pooled their milk.",
     ["Wheels of forty kilograms keep and travel better than small ones.",
      "From the thirteenth century villages pooled the day's milk from every household's cows.",
      "Because no household had enough milk in a day for the large wheels that keep and travel best, the villages combined their milk and credited each household with its share.",
      "The arrangement was recorded in writing and audited by elected villagers."],
     "C",
     "The goal asks for the reason behind the pooling, and only the option setting one household's "
     "daily yield against the size of wheel the trade wanted supplies it. Noting that the "
     "arrangement was written down and audited describes how it was administered rather than why it "
     "began."),
]

# Topics screened out by screen_topics.py because a banked passage already
# covers them. Each was abandoned rather than paraphrased around.
DROPPED = {
    "Great Trigonometrical Survey baseline": "rw_test15:W13, rw_test14:F9",
    "the metre defined from a meridian arc": "rw_test14:F9",
    "Struve geodetic arc": "rw_test14:F9 (same meridian-arc subject)",
    "railway time and the national timetable": "rw_test13:E7",
    "Westinghouse air brake": "rw_test13:S4",
    "bristlecone pine chronologies": "rw_test10:I1",
    "coppicing and pollarding": "rw_test10:I6",
    "karez / qanat irrigation tunnels": "rw_test10:E6",
    "Sogdian merchant letters": "rw_test15:E5",
    "Aral Sea diversion": "rw_test12:R1",
    "acequia community ditches": "rw_test14:C4",
    "caravanserai and caravan logistics": "rw_test14:W12",
    "Mongol yam relay post": "rw_test13:B2, rw_test15:R9",
    "urban wildlife and city birdsong": "rw_test8:I4, rw_test10:E3",
    "speleothems as climate archives": "rw_test14:B1",
    "sinkholes and blue holes": "rw_test10:I3",
    "cheese ripened in limestone caves": "rw_test14:E3",
    "whale earwax plugs as life records": "rw_test10:W5",
    "the SOFAR channel and long-range calls": "rw_test9:T5",
    "sperm whale codas": "rw_test10:C6",
    "green roofs and urban stormwater": "rw_authored:A-T7",
    "street trees growing faster in cities": "rw_test8:E1",
    "Samarkand": "rw_test12:B1, rw_test12:B3",
}
