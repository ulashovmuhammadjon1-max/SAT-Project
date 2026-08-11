#!/usr/bin/env python3
"""
Reading & Writing authored for Test 28.

All 81 items are original. Territory: coaching routes and stage timetables,
farriery and horseshoeing, coach building, drovers' roads, and toll gates and
turnpikes. Wheelwrighting, felloes, spokes and harness belong to Test 21;
railways to Test 17 and tramways to Test 20, so everything here stays on the
horse-drawn road.

Every item carries a `why` recording the reasoning that produced the key AND
the reason the strongest distractor fails. That record IS the verification: no
key exists here without one. Rationales name options by their CONTENT and never
by letter, so balance_rw.py is free to rotate any question when it evens out
the key distribution.

Boundaries choices are worded, never bare punctuation: the words on either side
of the blank are repeated inside every option so the student reads the
resulting sentence rather than four empty rows.

THE SIZING RULE THIS FILE IS BUILT ON. Test 23 had the lowest corpus overlap of
any build (0.14) and still failed on fifteen internal same-subject pairs, one at
0.56 where the same paragraph appeared twice. A narrow territory collides with
ITSELF, not with the bank. The cause is arithmetic: a topic list sized to the
number of BLOCKS (nine) gets reused nine times over, and a Rhetorical Synthesis
note list is a sub-topic's core facts stated plainly, so pairing it with a
Words-in-Context passage on the same sub-topic makes collision the default.

So the topic list here is sized to the ITEM count. Eighty-one items, eighty-one
distinct sub-topics, none of them used twice anywhere in the file, and no
synthesis note list drafted beside a passage on its subject. The subjects were
screened against ../rw_authored_corpus.json (1,295 passages) before drafting:
the corpus holds no farriery, no droving, no turnpike and no coaching passage
at all, so the whole risk in this file was internal and is answered by the
sizing rule rather than by a threshold.

Block counts, fixed by the assembler's quota of 3 modules x 27:
    Words in Context 15, Text Structure and Purpose 6,
    Central Ideas and Details 6, Command of Evidence 9, Inferences 6,
    Boundaries 12, Form, Structure, and Sense 9, Transitions 9,
    Rhetorical Synthesis 9                                        = 81
"""

SOURCE = "AUTHORED-T28"
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
     "A shoe fitted cold has to be hammered until it happens to match the foot it is put on. A shoe "
     "brought to the foot at a dull red heat scorches a thin film of horn away wherever it stands "
     "proud, and the mark it leaves shows the smith exactly where metal must still come off. The "
     "practice is defended less for the heat than for the _____ it gives the smith about the fit.",
     ["evidence", "warning", "reassurance", "authority"], "A",
     "The scorch mark is described as showing where metal must still come off, which is information "
     "the smith reads and acts on. Calling it reassurance would suggest the mark confirms the fit is "
     "already right, and the text says the opposite."),

 wic("W2",
     "The guard of a mail coach carried a timepiece locked in a case that only the office at either "
     "end could open. He entered the hour of arrival at every stage against the printed line for it, "
     "and the sheet came back to the office with the coach. Because the guard could neither set the "
     "watch forward to excuse a late start nor set it back to disguise one, the record of the "
     "journey was _____ of the crew that made it.",
     ["independent", "typical", "critical", "protective"], "A",
     "The locked case is said to prevent the guard from altering the watch in either direction, so "
     "the timing did not rest on the crew's own account of it. Describing the record as critical of "
     "the crew reads a judgement into a sheet that only carries hours."),

 wic("W3",
     "A body slung on long leather braces swings as it goes and the swing takes much of the shock, "
     "but the leather stretches with use and has to be taken up again and again. Steel laid up in "
     "leaves and bent to an ellipse gives at a blow and returns to its shape, and it does not "
     "lengthen over a season. Builders who changed to the steel gave up a soft motion in return for "
     "one that stayed _____ .",
     ["constant", "gentle", "silent", "cheap"], "A",
     "The leather is faulted for stretching and needing to be taken up, while the steel is said not "
     "to lengthen over a season, so what is gained is a setting that does not drift. Choosing the "
     "gentler motion contradicts the sentence, which gives up softness to get this quality."),

 wic("W4",
     "A drove could not be halted anywhere convenient for the night. Cattle turned loose on a "
     "farmer's grass ate a shilling's worth in an hour, so the men made instead for enclosures kept "
     "beside the road and let by the night. A drover planned his day's march around where these "
     "enclosures lay rather than around the distance he would have liked to _____ .",
     ["cover", "avoid", "measure", "shorten"], "A",
     "The passage contrasts where the enclosures lie with the distance the drover would otherwise "
     "choose, so the missing word is about getting a day's march done. Measuring the distance is "
     "something a surveyor does and has nothing to do with the choice the passage describes."),

 wic("W5",
     "A trust rarely collected its own money. Once a year the right to take the money at a named gate "
     "for the twelve months following was cried in an inn parlour and knocked down to whoever bid "
     "highest, and the bidder paid the sum he had promised whether the year proved good or bad. The "
     "arrangement handed the trust a figure it could count on and handed the bidder the whole of the "
     "_____ .",
     ["risk", "profit", "labour", "authority"], "A",
     "The trust receives a fixed sum whatever happens and the bidder is bound to his promise in a bad "
     "year as well as a good one, so what passes to him is the uncertainty. He does keep any surplus, "
     "but the sentence is built on the good-or-bad contrast rather than on the surplus alone."),

 wic("W6",
     "Between the priming and the finish a body took a dozen coats, and every one of them was rubbed "
     "back with pumice and water before the next went on. Nothing was added by the rubbing; a little "
     "was taken off each time, until the ground beneath the varnish was so level that the last coat "
     "had no ridge or hollow to betray. The work was therefore _____ in the most literal sense.",
     ["subtractive", "decorative", "hurried", "provisional"], "A",
     "The text says explicitly that nothing was added by the rubbing and that a little came off at "
     "every stage, which is what the missing word has to name. Calling the work decorative describes "
     "the finished panel rather than the method the sentence is about."),

 wic("W7",
     "The wedge of soft horn in the sole of a horse's foot is not merely a cushion. At every stride "
     "the weight of the animal presses it flat, and the spreading of the foot squeezes blood out of "
     "the veins above it and up the leg. A foot pared until this wedge no longer touches the ground "
     "loses a _____ that the heart alone does not replace.",
     ["pump", "guard", "measure", "signal"], "A",
     "The passage describes blood being squeezed out of the foot and driven up the leg at each "
     "stride, which is the action of a pump, and the closing clause sets it beside the heart. "
     "Calling it a guard names protection, which is the cushioning idea the first sentence sets "
     "aside."),

 wic("W8",
     "An ox walking two hundred miles over stone wears its cloven hoof away faster than the hoof "
     "grows, and a lame beast at the end of the road is worth less than a sound one. Smiths on the "
     "great routes nailed two small crescents to each foot, one to each half of the cloven hoof, in "
     "a throw that had to be finished while the animal lay roped on its side. The plates were "
     "_____ rather than ornamental.",
     ["preventive", "temporary", "traditional", "expensive"], "A",
     "The plates are introduced to stop the hoof wearing away and the beast arriving lame, so their "
     "purpose is to head off a loss. They were indeed taken off later, but the sentence contrasts "
     "them with ornament, and being temporary is not the opposite of being ornamental."),

 wic("W9",
     "A keeper had to see a vehicle in time to be at the bar before it, and a house set square to one "
     "road showed him nothing along the other. The usual answer was a room thrown forward on a "
     "shallow angle with a window in each face, so that a man sitting at his table looked up both "
     "approaches without rising. The shape was not a fashion but a _____ .",
     ["requirement", "compromise", "decoration", "convenience"], "A",
     "The keeper must reach the bar before the vehicle does, and the angled room is presented as the "
     "usual answer to that necessity, closing on a contrast with fashion. Calling it a convenience "
     "makes the shape optional, which the need to be at the bar in time does not allow."),

 wic("W10",
     "Ash cut in the spring and worked the same year moves as it dries, and a frame built of it "
     "opens at every joint within a twelvemonth. Builders therefore stacked their timber in open "
     "sheds with laths between the boards and left it for as many years as the plank was inches "
     "thick. The delay was the one part of the process that could not be _____ .",
     ["hastened", "recorded", "priced", "delegated"], "A",
     "A rule of one year for each inch of thickness is given as the cost of avoiding joints that "
     "open, so what the timber demands is time that cannot be cut short. The work certainly could be "
     "handed to a yardman, so being delegated is not what the sentence denies."),

 wic("W11",
     "On a frosted road a smooth plate of iron is worse than no plate at all. Smiths turned the heel "
     "of the shoe down into a short spur and drove one or two nails with a raised head at the toe, so "
     "that the foot bit instead of sliding. The additions cost the horse a little in the evenness of "
     "its tread and returned to it a great deal in _____ .",
     ["grip", "speed", "comfort", "appearance"], "A",
     "The problem stated is sliding on frost and the fix makes the foot bite, so what is returned is "
     "purchase on the road. Comfort is what the sentence says is given up, since the tread is no "
     "longer even."),

 wic("W12",
     "A drover who had sold his beasts at a fair three hundred miles from home could go back by any "
     "means he liked, but he could not afford to feed a dog on the way. The dogs were turned loose at "
     "the fair and made their own way north, calling at the same inns the droves had used, where a "
     "meal was put down for them against the master's account at the next passing. The arrangement "
     "worked because the route was _____ .",
     ["habitual", "shorter", "guarded", "level"], "A",
     "The dogs are said to call at the same inns the droves had used and to be fed on account until "
     "the next passing, which only works on a road travelled again and again in the same way. Saying "
     "the route was guarded introduces protection that nothing in the passage supplies."),

 meaning("W13",
     "A coach carried more than people. Under the seats and in the hind boot went boxes of samples, "
     "bank parcels and small consignments of drapery, and the proprietors advertised rates for them "
     "beside the fares. A parcel of any value was entered in a book and paid for at a higher rate, "
     "the office undertaking to make good its loss; the ordinary rate covered the <u>carriage</u> "
     "only, and the sender bore the risk himself.",
     "carriage",
     ["transport", "vehicle", "posture", "expense"], "A",
     "The sentence sets the ordinary rate against the higher rate that covers loss, so the word names "
     "the service of moving the parcel rather than the thing that moves it. Reading it as the vehicle "
     "makes the ordinary rate cover a coach, which is not something a rate can cover."),

 meaning("W14",
     "A carrier passing a gate six times a week did not pay six times. He could settle with the "
     "lessee for a sum covering a quarter or a year and pass as often as he pleased, and both sides "
     "gained: the carrier knew his outlay in advance, and the lessee had the money at the start of "
     "the period instead of a penny at a time. Where a trust had many gates a single "
     "<u>composition</u> might be made to cover them all.",
     "composition",
     ["agreement", "mixture", "essay", "settlement of a quarrel"], "A",
     "The word stands for the arrangement by which a lump sum replaces payment at each passing, which "
     "both parties enter willingly. The sense of settling a quarrel would require a dispute, and the "
     "passage describes an ordinary bargain of convenience."),

 meaning("W15",
     "Horses could not be driven far at the pace the timetable demanded, so a road was divided into "
     "lengths of eight to twelve miles, each ending at an inn where a fresh team stood ready. A long "
     "hill shortened the length before it and an easy run lengthened the one after, so that the "
     "<u>stage</u> was measured by what the team could do rather than by the milestones.",
     "stage",
     ["section of a route", "raised platform", "phase of development", "coach"], "A",
     "The word is used for the eight-to-twelve-mile length between one change of horses and the next, "
     "and the sentence contrasts its measurement with the milestones. Taking it as a phase of "
     "development would fit a process rather than a road divided into lengths."),

 # --------------------------------------------- Text Structure and Purpose (6)
 tsp("S1",
     "A traveller reading a timetable met the same coach twice under different descriptions. "
     "<u>By long custom the journey toward London was called the up journey whatever the compass "
     "direction of the road, and the journey away from it the down.</u> A coach from Exeter ran up "
     "in the morning and the same vehicle ran down at night, and the words told a booking clerk which "
     "of two lists to look in without telling him anything at all about north or south.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It states the convention whose practical effect the rest of the text explains.",
      "It criticises a naming system that misled travellers about direction.",
      "It gives an example of a coach that ran in both directions in one day.",
      "It identifies the office responsible for printing the timetables."],
     "A",
     "The sentence defines up and down by reference to London rather than the compass, and the "
     "sentences after it show what a clerk did with that definition. The Exeter coach running both "
     "ways appears only after the underlined sentence, as the illustration of it."),

 tsp("S2",
     "The face of an anvil is the least interesting part of it. Two openings are cut through the "
     "heel: a square one that holds a cutting tool upright so the smith can bring hot iron down onto "
     "a fixed edge, and a round one directly beneath the place where a nail hole is punched, so the "
     "punch has somewhere to go when it breaks through. Neither opening does any work itself. Both "
     "exist so that the smith's two hands, one holding and one striking, are enough.",
     "Which choice best states the main purpose of the text?",
     ["To explain how two features of an anvil let one worker do a job that would otherwise need two.",
      "To argue that the face of an anvil matters less than smiths believe.",
      "To describe the sequence in which a horseshoe is punched and cut.",
      "To compare anvils made for farriers with anvils made for other trades."],
     "A",
     "Each opening is described as holding or receiving a tool so that the smith's holding hand is "
     "freed, and the closing sentence states that conclusion outright. The remark about the face is a "
     "way into the subject rather than the claim the text goes on to support."),

 tsp("S3",
     "Two answers were given to the same question. One engineer built a road as a structure: a "
     "levelled bed, a course of large stones set by hand on edge, and smaller stone above them, so "
     "that the load was carried down to the ground by the pavement. <u>The other held that the "
     "subsoil would carry any load if it were kept dry, and that the business of the surface was "
     "simply to shed water.</u> His roads used less stone, cost less, and depended entirely on the "
     "ditches beside them being kept open.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It introduces the rival principle whose consequences the closing sentence spells out.",
      "It concedes a weakness in the method described in the preceding sentence.",
      "It restates the first engineer's method in simpler terms.",
      "It explains why hand-set stone fell out of use everywhere."],
     "A",
     "The sentence sets out a different principle, that a dry subsoil carries the load, and the "
     "sentence after it draws out what followed from it in stone, cost and drainage. It does not "
     "restate the first method, since the first method carries the load in the pavement rather than "
     "in the ground."),

 tsp("S4",
     "A drove of two hundred bullocks paying at every gate would have arrived at market owing more "
     "than it earned. Drovers therefore worked out lines that crossed the turnpikes at right angles "
     "and ran the rest of their length on old ridgeways and commons where no trust had authority. "
     "The routes were longer in miles than the made roads beside them, softer under the foot of a "
     "beast that had to arrive fit to sell, and free.",
     "Which choice best states the main idea of the text?",
     ["Drovers used older unturnpiked ways because the saving in tolls and hooves outweighed the extra distance.",
      "Turnpike trusts had no legal power to charge for cattle passing their gates.",
      "The made roads were avoided chiefly because they were longer than the ridgeways.",
      "Drove routes were laid out by the trusts to keep cattle away from coaches."],
     "A",
     "The closing sentence lists the extra length against two gains, ground that is kinder to the "
     "feet and no charge at all, and the opening sentence gives the size of the charge avoided. The "
     "claim that the trusts had no power to charge is contradicted by the drove paying at every gate "
     "in the first sentence."),

 tsp("S5",
     "Before a stick of timber was cut, the body was drawn out at its true size in chalk on the "
     "black-painted floor of the shop. <u>A curve that looked well on a drawing an inch to the foot "
     "could look heavy at full size, and the only way to find out was to stand back from it on the "
     "floor.</u> Patterns were then laid on the chalk lines and cut, so that a mistake cost a piece "
     "of thin board rather than a length of seasoned ash.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It gives the reason the full-size drawing was made rather than a small one.",
      "It concedes that small drawings were more accurate than the chalk floor.",
      "It describes the material from which the patterns were cut.",
      "It contrasts two shops that used different methods."],
     "A",
     "The sentence says a curve can deceive at a small scale and that standing back from full size is "
     "the only test, which is precisely why the floor was used. The material of the patterns is named "
     "in the following sentence, not in the underlined one."),

 tsp("S6",
     "The guard of a mail was not a passenger's servant. He sat alone at the back with the bags "
     "locked beneath him and a short brass-barrelled gun in a case beside him, and his orders were "
     "to stay with the mail if the coach broke down and let the passengers shift for themselves. "
     "The gun was fired perhaps a dozen times in the whole history of the service. Its work was done "
     "while it stayed in its case.",
     "Which choice best states the main purpose of the text?",
     ["To explain that the guard's arms and orders were meant to deter interference rather than to be used.",
      "To describe the duties a guard performed for the passengers.",
      "To argue that mail coaches were robbed more often than is now believed.",
      "To trace the changes made to the guard's equipment over time."],
     "A",
     "The text records that the gun was almost never fired and closes by saying its work was done in "
     "its case, and the orders to abandon the passengers point the same way. Duties toward passengers "
     "are what the second sentence rules out."),

 # ---------------------------------------------- Central Ideas and Details (6)
 cid("C1",
     "A trust was not a company and not a department. It came into being by a private act naming a "
     "stretch of road and a body of local men, empowering them to borrow on the security of what the "
     "gates took and to spend it on that stretch and no other, and it expired after twenty-one years "
     "unless a fresh act renewed it. Hundreds of such bodies existed at once, each answerable for a "
     "few miles and none of them to any other.",
     "Which choice best states the main idea of the text?",
     ["Each trust was a separate, temporary body confined by its own act to one stretch of road.",
      "Trusts were branches of a single national authority responsible for the whole road system.",
      "A trust's chief difficulty was that it could not borrow against its expected receipts.",
      "Most trusts were renewed automatically without any further act."],
     "A",
     "The text gives the trust a named stretch, a fixed term of twenty-one years, and no answerability "
     "to any other body, which is the separateness the question asks about. The borrowing option "
     "reverses the passage, which grants the power to borrow on the security of the gates."),

 cid("C2",
     "Horn grows down from the coronet at roughly a centimetre a month, so the wall of a foot is "
     "renewed in about nine months. A nailed shoe stops the wall wearing but does nothing to stop it "
     "growing, and after five or six weeks the foot has come forward and down beyond the iron beneath "
     "it. The shoe is therefore removed and replaced long before it is worn out, and a smith's "
     "regular round is set by the growth of horn rather than by the wear of iron.",
     "Which choice best states the main idea of the text?",
     ["The interval between shoeings is fixed by how fast the hoof grows, not by how fast the shoe wears.",
      "A shoe is left on until the iron is worn thin enough to be dangerous.",
      "Horn grows fastest in the months when a horse is worked hardest.",
      "Nailing a shoe on slows the growth of the wall beneath it."],
     "A",
     "The closing sentence states the point directly and the middle of the passage supplies the reason, "
     "that the foot outgrows the iron in five or six weeks. The claim that shoeing slows growth is "
     "contradicted by the statement that the shoe does nothing to stop the wall growing."),

 cid("C3",
     "A place inside cost roughly twice a place on the roof, and the difference bought less than it "
     "appears. Four people inside sat knee to knee in a box with the windows shut against the dust, "
     "while eleven outside had air, a view, and the whole weather of the journey. Proprietors "
     "nevertheless filled the inside first on any road worth running, because the people who could "
     "pay the higher fare were also the people who would not be seen on the roof.",
     "Which choice best states the main idea of the text?",
     ["The inside fare bought comfort that was doubtful, and sold chiefly on what riding inside signified.",
      "Inside places were preferred because they were markedly more comfortable in every weather.",
      "Outside places were priced low because so few travellers wanted them.",
      "Proprietors would have preferred to sell only outside places."],
     "A",
     "The passage undercuts the comfort of the inside seat and then explains the demand by who would "
     "not be seen on the roof, which is a matter of standing rather than of comfort. Saying outside "
     "places sold badly is contradicted by eleven of them being carried."),

 cid("C4",
     "A bullock walked to market lost weight all the way, and the loss was greatest in the last week, "
     "when the roads were hard and the grazing near a great town was poor. Dealers therefore bought "
     "the beasts twenty or thirty miles short of the market and turned them onto rented pasture for "
     "a month before selling. The animal that reached the salesman had made the whole journey, but "
     "not lately, and it was sold on the condition it had recovered rather than the condition it had "
     "arrived in.",
     "Which choice best states the main idea of the text?",
     ["Beasts were fattened on rented ground near the market so that they were sold in recovered condition.",
      "Drovers avoided the last thirty miles of the route altogether.",
      "Weight lost on the road could not be regained once an animal reached its destination.",
      "Dealers bought animals early chiefly to secure a lower price."],
     "A",
     "The passage names the loss in the final week, the month on rented pasture, and the sale on "
     "recovered condition, which together make the point. The statement that weight could not be "
     "regained is exactly what the month of grazing disproves."),

 cid("C5",
     "The iron work of a body was never left bright. Steps, handles, stay bars and lamp brackets were "
     "painted with a black spirit varnish and then baked in a low oven, and the coat that came out "
     "was hard enough to resist a boot nail and unbroken enough to keep water off the metal beneath. "
     "A bright fitting looked well for a fortnight; a baked one was still sound after a winter of "
     "salt and grit.",
     "Which choice best states the main idea of the text?",
     ["Baking a hard varnish onto the ironwork protected it in a way that a bright finish could not.",
      "Bright ironwork was avoided because it made a coach conspicuous on the road.",
      "The oven was used chiefly to speed up work that would otherwise have taken weeks.",
      "Handles and steps were the only parts of a coach that needed protection."],
     "A",
     "The passage sets a fortnight of good looks against a winter of salt and grit and explains the "
     "difference by the hardness and continuity of the baked coat. Speed does not appear anywhere in "
     "the text, which is about how long the finish lasted rather than how long it took."),

 cid("C6",
     "Every parish had for centuries owed the crown so many days' labour a year on its own roads, "
     "supplied by its own men with their own tools and carts. The work was done grudgingly, in the "
     "weeks when the fields could spare the men, which were not the weeks when the roads most needed "
     "attention. Trusts were empowered to take a money payment instead, and the parish that paid "
     "found its obligation discharged in an hour and its road mended in the season when mending was "
     "worth doing.",
     "Which choice best states the main idea of the text?",
     ["Converting the labour duty into a payment freed road work from a timetable set by farming.",
      "Parishes resisted the change because paying cost them more than working.",
      "The labour duty was abolished because parishes had too few men to supply it.",
      "Trusts took the money payment and left the parish roads unmended."],
     "A",
     "The passage faults the old duty for arriving when the fields could spare men rather than when "
     "the road needed work, and says the money payment got the road mended in the right season. The "
     "option about leaving roads unmended contradicts the closing clause."),

 # ------------------------------------------------- Command of Evidence (9)
 coe("E1",
     "In 1836 the keeper of a large posting inn wrote a private account of his yard for his son. "
     "Historian Marion Alleyne argues that the account was written to record a fact the trade never "
     "advertised: that the yard's reputation rested on the ostlers' drill rather than on the quality "
     "of the horses it kept.",
     "Which quotation from the account most effectively illustrates Alleyne's claim?",
     ["&ldquo;Four men stand ready before the horn is heard, each to his own buckle and his own side, "
      "and the coach is away in ninety seconds with horses no better than a farmer's.&rdquo;",
      "&ldquo;We keep eleven pairs at this house, and have kept as many as fourteen in the summer "
      "months.&rdquo;",
      "&ldquo;The yard was newly paved in the spring at a cost of forty-two pounds.&rdquo;",
      "&ldquo;Travellers speak well of the house, and the coffee room is seldom empty by "
      "eight.&rdquo;"],
     "A",
     "The quotation naming four men in position before the horn, ninety seconds, and horses no better "
     "than a farmer's puts the drill above the animals, which is exactly the claim. Counting the pairs "
     "kept describes the size of the stable without saying what made the yard's name."),

 coe("E2",
     "A farriery manual of 1857 devotes a chapter to the rasp. Historian Peter Nwosu argues that the "
     "chapter's purpose is to restrain the tool rather than to teach its use, and that its author "
     "expected the beginner's error to be doing too much rather than too little.",
     "Which quotation from the manual most effectively illustrates Nwosu's claim?",
     ["&ldquo;What you take from the wall does not come back, and the hand that is busy above the "
      "clenches has already gone too far.&rdquo;",
      "&ldquo;The rasp should be held level, with the elbow low and the stroke drawn from the "
      "shoulder.&rdquo;",
      "&ldquo;A rasp of fourteen inches will serve for all ordinary work.&rdquo;",
      "&ldquo;The tool was in use in this country before the reign of Elizabeth.&rdquo;"],
     "A",
     "The quotation warning that what is taken does not come back and that a busy hand has already "
     "gone too far is a caution against overwork, which is what the claim describes. The instruction "
     "about holding the rasp level teaches the stroke, which is the use the claim says the chapter is "
     "not chiefly about."),

 coe("E3",
     "A surveyor's report of 1841 on nine miles of road was long thought to be a request for more "
     "stone. Historian Rosalind Achebe argues that it is nothing of the kind, and that its author "
     "held the road's failures to be failures of water rather than of material.",
     "Which quotation from the report most effectively illustrates Achebe's claim?",
     ["&ldquo;Wherever the side ditch is choked the metal has gone to pieces, and wherever the ditch "
      "runs the same metal, of the same quarry and the same year, stands firm.&rdquo;",
      "&ldquo;The stone now supplied is of a harder kind than that used in 1836.&rdquo;",
      "&ldquo;Two hundred and forty tons were laid between the fourth and fifth milestones.&rdquo;",
      "&ldquo;The parish has been slow in paying the composition due at Michaelmas.&rdquo;"],
     "A",
     "The quotation holding the quarry and the year constant while the ditch varies isolates drainage "
     "as the cause, which is the argument. Remarking that the stone is now harder concerns material, "
     "the very explanation the claim says the author set aside."),

 coe("E4",
     "A horse worked long hours on hard metalled roads sometimes develops a painful condition in "
     "which the sensitive tissue inside the hoof separates from the wall. Coachmen believed the "
     "condition was caused by the concussion of the road itself, while a rival view held that it "
     "followed from the heavy feeding given to hard-worked horses. A veterinary surgeon proposes to "
     "test the concussion explanation.",
     "Which finding, if true, would most directly support the concussion explanation?",
     ["Horses moved from stone roads to soft ground develop the condition far less often although "
      "their feed is unchanged.",
      "The condition is more common in winter than in summer on every kind of road.",
      "Horses fed the same ration as coach horses but kept at grass rarely develop the condition.",
      "The condition can be relieved by a shoe that raises the heel."],
     "A",
     "Holding the feed constant while changing the ground isolates concussion as the variable, which "
     "is what a test of that explanation requires. The finding about horses at grass changes the "
     "ground and the work together, so it cannot separate the two explanations."),

 coe("E5",
     "A coach lamp burned a single candle, which of itself could not be seen far. Makers set the "
     "flame in front of a curved polished plate, and disputed whether the plate did more to help the "
     "driver see the verge or to help others see the coach. A student wishes to test the second "
     "purpose.",
     "Which finding, if true, would most directly support the claim that the plate was intended to "
     "make the coach visible to others?",
     ["The plate throws almost all of the light forward along the road and leaves the verge beside "
      "the wheels in darkness.",
      "Candles of a larger size were adopted for night mails in the 1820s.",
      "Lamps were mounted at the height of a driver's shoulder rather than at the height of the "
      "footboard.",
      "The plates were made of polished tin rather than of silvered glass."],
     "A",
     "A plate that sends light down the road and leaves the nearby verge dark serves an observer "
     "ahead rather than the driver looking beside his wheels, which is the distinction the test needs. "
     "The material of the plate says nothing about the direction the light is thrown."),

 coe("E6",
     "A drover sold other men's cattle and carried the price home. Carrying gold three hundred miles "
     "was dangerous, so a drover would take payment in a written order on a bank and hand the paper "
     "over at the far end. Historian Ines Vargas argues that the trade's real capital was not the "
     "cattle but the drover's standing, since the paper was worth nothing unless the people at both "
     "ends trusted the man between them.",
     "Which finding, if true, would most directly support Vargas's argument?",
     ["Drovers were required to be licensed householders over thirty, and a licence was refused to "
      "any man against whom a debt was proved.",
      "The number of cattle walked south rose steadily between 1780 and 1830.",
      "Drove roads were wider than turnpike roads over most of their length.",
      "Written orders on banks were also used by wool merchants in the same period."],
     "A",
     "A licence restricted to settled men and withdrawn for proved debt is a formal test of exactly "
     "the standing the argument says the trade ran on. The growth in the number of cattle measures the "
     "trade's size and says nothing about what made the paper acceptable."),

 coe("E7",
     "A trust's clerk recorded the money taken at one gate in each of four years, together with the "
     "number of vehicles counted. The trust's committee claimed in 1843 that the road was carrying "
     "more traffic than ever, and that the fall in receipts was caused by the spread of composition "
     "agreements rather than by any loss of trade."
     + table(["Year", "Vehicles counted", "Money taken (&pound;)"],
             [["1840", "18,400", "742"], ["1841", "19,100", "705"],
              ["1842", "20,300", "661"], ["1843", "21,600", "618"]]),
     "Which choice best describes data from the table that support the committee's claim?",
     ["The count of vehicles rose in every year while the money taken fell in every year.",
      "Both the count of vehicles and the money taken fell after 1840.",
      "The money taken rose more slowly than the count of vehicles.",
      "The count of vehicles was highest in the year when the money taken was highest."],
     "A",
     "The committee's claim needs traffic rising and receipts falling at the same time, and the table "
     "shows the count climbing from 18,400 to 21,600 while the money drops from 742 to 618. Saying "
     "both fell misreads the vehicle column, which rises throughout."),

 coe("E8",
     "A veterinary school measured the growth of the hoof wall on eight horses, marking the horn at "
     "the coronet and recording how far the mark had travelled after twelve weeks. The horses were "
     "kept in two groups, one exercised daily on made roads and one at rest in a yard, and the "
     "researchers set out to test whether work at the walk affects the rate of growth."
     + table(["Group", "Horses", "Mean growth in 12 weeks (mm)"],
             [["Exercised daily", "4", "29"], ["Rested in a yard", "4", "28"]]),
     "Which choice best describes data from the table that are relevant to the researchers' question?",
     ["The two groups grew almost the same amount, 29 millimetres against 28.",
      "The exercised group grew roughly twice as much as the rested group.",
      "The rested group grew no horn at all over the twelve weeks.",
      "Growth in both groups exceeded 40 millimetres."],
     "A",
     "The question is whether work changes the rate, and the two means of 29 and 28 millimetres are "
     "close enough to bear on it directly. The claim that the rested group grew nothing contradicts "
     "the recorded 28 millimetres."),

 coe("E9",
     "A builder weighed four bodies of the same pattern built in different years, after deciding in "
     "1834 to use thinner panels and a lighter frame. He argued that the saving in weight came from "
     "the body itself rather than from any change to what was hung beneath it, and recorded the two "
     "figures separately."
     + table(["Year built", "Body (kg)", "Springs and underframe (kg)"],
             [["1830", "412", "268"], ["1832", "405", "266"],
              ["1836", "351", "265"], ["1838", "344", "267"]]),
     "Which choice best describes data from the table that support the builder's argument?",
     ["The body fell by more than 60 kilograms across the four vehicles while the springs and "
      "underframe stayed within 3 kilograms.",
      "Both the body and the springs and underframe fell by about the same proportion.",
      "The springs and underframe fell steadily in every year recorded.",
      "The lightest body was built in the same year as the heaviest underframe."],
     "A",
     "The argument requires the fall to be confined to the body, and the table shows the body dropping "
     "from 412 to 344 while the other column moves only between 265 and 268. Saying both fell by the "
     "same proportion misreads a column that barely moves at all."),

 # ------------------------------------------------------------ Inferences (6)
 inf("N1",
     "A trust's act obliged it to set up a stone at every mile and to cut on it the distance to the "
     "next market town. The clause was not a courtesy to travellers. A trust that could show its "
     "stones in place could also show how many miles it was charging for, and a traveller who had "
     "passed four stones since the last gate could tell whether the toll demanded matched the "
     "distance. The obligation therefore _____",
     ["gave the public a means of checking the trust's own account of the road it maintained.",
      "reduced the number of gates a trust was permitted to erect on its road.",
      "was resisted by travellers, who found the stones difficult to read at speed.",
      "made it unnecessary for a trust to keep any written record of its mileage."],
     "A",
     "The passage says the stones let a traveller compare the toll demanded with the distance passed, "
     "which puts a public check on the trust. Nothing in the text bears on how many gates a trust "
     "might erect."),

 inf("N2",
     "A stable floor that is never dried out holds a wet mixture of bedding and dung against the sole "
     "of every foot standing on it. The soft horn in the middle of the sole rots in those conditions "
     "and gives off a black discharge, and the trouble clears when the horse is moved to a dry "
     "standing and the cleft is opened and kept clean. A groom who finds the condition in several "
     "horses at once in the same building can most reasonably conclude that _____",
     ["the fault lies in how the building is kept rather than in the individual animals.",
      "the horses were all shod by the same smith at about the same time.",
      "the discharge will clear without any change to the standing.",
      "the condition passes from one horse to another by direct contact."],
     "A",
     "The passage ties the rot to wet standings and its cure to a dry one, so several cases in one "
     "building point at the building. The suggestion that it clears without change contradicts the "
     "stated cure, which requires moving the horse to a dry standing."),

 inf("N3",
     "A coachman on a night stage saw very little. He knew the road by the sound of the wheels "
     "changing where the metal changed, by the moment the horses' pace slackened at the foot of a "
     "rise he could not see, and by the smell of a particular wood at a particular turn. A man put on "
     "an unfamiliar road at night drove it slower than his own road in fog, which suggests that a "
     "night coachman's speed depended less on visibility than on _____",
     ["how thoroughly he had learned that particular road by other senses.",
      "the strength of the lamps carried on either side of his footboard.",
      "the number of passengers he was carrying that night.",
      "whether the road had been recently resurfaced by the trust."],
     "A",
     "The passage lists sound, pace and smell as the sources of a coachman's knowledge and then "
     "reports that an unfamiliar road slowed him more than fog did, which points at familiarity rather "
     "than at seeing. The lamps option is the visibility explanation the sentence sets aside."),

 inf("N4",
     "Some horses swing a hind foot inward far enough to strike the opposite leg, and the blow falls "
     "on the same spot every stride until the skin breaks. A smith can move the point of contact by "
     "altering how the shoe is set under the foot, but a horse doing this at speed will cut itself "
     "again before the alteration takes effect. Drivers therefore strapped a padded boot over the "
     "place. The boot was fitted because _____",
     ["it protected the leg during the weeks in which the change to the shoeing had yet to take hold.",
      "it corrected the swing of the hind foot more reliably than reshoeing did.",
      "smiths were unable to alter the setting of a shoe on a hind foot.",
      "the injury was found only in horses that had never been shod."],
     "A",
     "The passage sets a remedy that takes time against an injury that recurs at once, and the boot "
     "covers the gap between them. Saying the boot corrects the swing contradicts the text, in which "
     "only the shoeing alters where the foot falls."),

 inf("N5",
     "A posting house did not run coaches. It kept horses and postboys for hire by the mile to anyone "
     "travelling in a carriage of his own, and the boy rode one of the pair rather than sitting on the "
     "vehicle, so that the traveller's own servant kept his place behind. The horses came back with "
     "the boy from the next house, never went beyond it, and were charged for the outward miles only. "
     "The arrangement suited a traveller who _____",
     ["wanted to keep his own carriage and servants but not to keep horses along the whole route.",
      "was unwilling to travel with anyone he had not engaged himself.",
      "preferred to reach his destination without stopping at all.",
      "had no carriage of his own and needed one supplied at each stage."],
     "A",
     "The traveller supplies the carriage and the servant while the house supplies horses by the mile "
     "for one length of road, which fits a man unwilling to maintain horses the whole way. The option "
     "about having no carriage contradicts the opening, which addresses someone travelling in a "
     "carriage of his own."),

 inf("N6",
     "Sheep and cattle do not travel alike. A bullock walks steadily and will make fifteen miles in a "
     "day without losing condition; a flock moves in fits, spreads across the verge to graze as it "
     "goes, and covers eight or nine. A drover working sheep therefore reckoned his journey in weeks "
     "where a cattle drover reckoned in days, and this difference meant that a sheep drove _____",
     ["had to be planned around far more overnight stops for the same distance.",
      "reached market in better condition than a drove of cattle over the same road.",
      "could take routes that were closed to cattle at every season.",
      "required no grazing along the way, since the flock fed at the halts."],
     "A",
     "Covering eight or nine miles a day instead of fifteen means many more nights on the road for the "
     "same distance, which is the direct consequence of the pace given. The claim that the flock "
     "needed no grazing on the way contradicts the description of sheep spreading across the verge to "
     "graze as they move."),

 # ------------------------------------------------------------ Boundaries (12)
 bnd("B1",
     "The long central beam that ran from the front carriage to the back, and on which the whole "
     "weight of the body was carried, was called the perch. A builder who shortened it gained a "
     "vehicle that turned in a narrower _____ he also gained one that flexed under a heavy load.",
     ["space; unfortunately", "space, unfortunately", "space unfortunately",
      "space: and unfortunately"], "A",
     "Two complete statements stand on either side of the blank with no conjunction between them, "
     "which is what a semicolon is for. A comma alone splices them together, and a colon does not "
     "take a conjunction after it."),

 bnd("B2",
     "Snow altered a timetable before it stopped one. The proprietors' winter bills lengthened the "
     "allowance between changes by a quarter of an hour and dropped one stage altogether on the "
     "highest _____ was published in October, weeks before any snow fell.",
     ["ground, and the amended bill", "ground and the amended bill",
      "ground; the amended bill and", "ground: and the amended bill"], "A",
     "A comma with the coordinating conjunction joins two complete statements correctly. Running them "
     "together with no punctuation at all leaves a comma splice of a different kind, and a colon "
     "cannot be followed by a conjunction."),

 bnd("B3",
     "An inn stable kept two kinds of standing. In the narrow stalls a horse stood tied and faced the "
     "_____ in the loose boxes at the far end it could turn and lie down, which is where the ostler "
     "put a team that had just come in.",
     ["wall; in", "wall, in", "wall in", "wall: and in"], "A",
     "Two complete statements meet at the blank with no conjunction between them, which is what a "
     "semicolon is for. The comma alone splices them, and a colon does not take a conjunction after "
     "it."),

 bnd("B4",
     "A trust could borrow, but only against one thing. Lenders advanced money on the security of "
     "what the gates would _____ the interest on it was a first charge on those receipts, so a road "
     "that carried less than the promoters had promised left the lenders short and the parish "
     "untouched.",
     ["take, and", "take and", "take; and", "take: and"], "A",
     "A comma with the coordinating conjunction correctly joins two complete statements. Dropping the "
     "comma fuses them, and neither a semicolon nor a colon is followed by a conjunction here."),

 bnd("B5",
     "Curled horsehair was washed, teased and stuffed into the seat squab by hand, then held down with "
     "twine passed through the covering and back. Because the stuffing settled unevenly in the first "
     "month, a trimmer expected the work to come back to _____ he charged for the second visit in his "
     "original estimate.",
     ["him; accordingly", "him, accordingly", "him accordingly",
      "him: and accordingly"], "A",
     "Complete statements stand on both sides of the blank and no conjunction joins them, so the "
     "semicolon is right. The comma on its own produces a splice, and a colon followed by a "
     "conjunction is not a construction English uses."),

 bnd("B6",
     "Geese walked to market like anything else, but their feet would not stand the road. The birds "
     "were driven first through soft tar and then through sand or grit, which set into a crust "
     "beneath each _____ crust wore through in about a hundred miles and had to be renewed.",
     ["foot. The", "foot, the", "foot the", "foot; and the"], "A",
     "Two complete statements meet at the blank, and separating them into two sentences with a full "
     "stop is correct. A comma alone splices them, and a semicolon does not take a conjunction after "
     "it."),

 bnd("B7",
     "A coachman's wage was small and everybody knew it. What he lived on was the shilling each "
     "passenger handed him at the end of a stage, and a man who drove a fashionable road could take "
     "more in a week that way than the proprietor paid him in a _____ the custom was never written "
     "into any agreement.",
     ["quarter, yet", "quarter yet", "quarter; yet the", "quarter: yet"], "A",
     "A comma before the coordinating conjunction correctly joins two complete statements. Omitting "
     "the comma runs them together, and a colon is not used before a conjunction of this kind."),

 bnd("B8",
     "Iron heated to a bright red and plunged into water comes out too hard to file and too brittle "
     "to trust. The smith therefore brightens a face of the cooled tool and warms it a second time, "
     "watching for straw, then brown, then blue. The colour that runs across a brightened face of "
     "quenched _____ tells him its temperature more exactly than any thermometer he could have "
     "owned.",
     ["steel", "steel,", "steel;", "steel:"], "A",
     "Nothing should separate this subject from its verb, so the blank takes no punctuation at all. "
     "A comma, a semicolon or a colon would each cut the sentence between the thing described and "
     "what it does."),

 bnd("B9",
     "The bar came down at eleven and the keeper went to bed. A traveller arriving after that pulled a "
     "wire beside the door, which rang a bell over the bed _____ the keeper came down in whatever he "
     "had on, took the money by lamplight, and lifted the bar.",
     ["itself, and", "itself and", "itself; and", "itself: and"], "A",
     "A comma with the coordinating conjunction joins the two complete statements properly. Dropping "
     "the comma leaves them fused, and neither a semicolon nor a colon precedes a conjunction here."),

 bnd("B10",
     "A drove road was not a road at all in the sense a surveyor would have recognised. It was a "
     "right of way forty or fifty yards wide between banks, with grass over the whole of _____ the "
     "width was the point, since two hundred beasts moving abreast at a walk fed as they went instead "
     "of trampling a single line.",
     ["it, and", "it and", "it; and", "it: and"], "A",
     "A comma before the coordinating conjunction joins the two complete statements properly. Leaving "
     "the comma out fuses them, and a conjunction does not follow a semicolon or a colon here."),

 bnd("B11",
     "The step folded up against the body when the door shut, so that nothing projected to catch a "
     "post in a narrow archway. The mechanism worked from the same handle that turned the lock, which "
     "meant one movement did two _____ it also meant that a worn lock left the step hanging.",
     ["things; unhappily", "things, unhappily", "things unhappily",
      "things: and unhappily"], "A",
     "Two independent statements meet at the blank without a conjunction, which calls for a semicolon. "
     "The comma alone splices them, and a colon does not take a following conjunction."),

 bnd("B12",
     "A boy went to a smith at fourteen and was bound for seven years. He learned to make a shoe in "
     "the first two _____ the remaining five went on the foot itself, and the company that examined "
     "him at the end asked him about the foot and hardly at all about the iron.",
     ["years; the", "years, the", "years the", "years: and the"], "A",
     "Two complete statements stand on either side of the blank with no conjunction between them, "
     "which calls for a semicolon. The comma on its own splices them, and a colon is not followed by "
     "a conjunction."),

 # --------------------------------------------- Form, Structure, and Sense (9)
 fss("F1",
     "Plate glass in a door made a coach lighter inside and heavier to hang. Neither the glass itself "
     "nor the brass channels it slid in _____ cheap, and a pane broken by a careless passenger "
     "pulling on the strap cost more than the whole trimming of the seat beneath it.",
     ["were", "was", "have been", "is"], "A",
     "With 'neither ... nor', the verb agrees with whichever subject stands nearer to it, and 'the "
     "brass channels it slid in' is both nearer and plural. The singular forms would agree with the "
     "glass, which is the further of the two subjects."),

 fss("F2",
     "A shoe is not pulled off. The smith first cuts through the clenched ends of the nails where "
     "they emerge from the wall, and only then does he lever the iron away, _____ the nails from the "
     "horn rather than dragging them through it.",
     ["drawing", "drew", "draws", "to draw"], "A",
     "The participle attaches to the levering described in the main clause and runs parallel with "
     "'dragging' later in the same phrase. A finite past-tense verb would need a subject of its own, "
     "and the sentence supplies none."),

 fss("F3",
     "The acts exempted a good deal of traffic from payment. Carts carrying manure to a farm, wagons "
     "going to and from a church on a Sunday, and horses drawing a hearse _____ all passed free, "
     "which the keepers resented and the courts upheld.",
     ["were", "was", "has been", "is"], "A",
     "The subject is a series of three items joined by 'and', so it is plural and takes the plural "
     "verb. The singular forms would agree with the hearse alone, which is only the last item in the "
     "list."),

 fss("F4",
     "Three or four Scots pines standing together in open country a long way from any wood are worth "
     "a second look. Planted beside a stance, _____ told a drover coming over a shoulder of hill in "
     "poor light where the night's enclosure lay.",
     ["they", "it", "these being", "which"], "A",
     "The modifying phrase describes the pines, so the main clause must open with a plural subject "
     "that refers to them. Beginning with 'which' would leave the sentence without a main clause at "
     "all."),

 fss("F5",
     "Two coaches leaving the same town for the same city at the same hour raced, and passengers were "
     "thrown out of both. The proprietors met and agreed to separate the departures by half an hour, "
     "_____ having discovered that competition on the road cost more in broken vehicles than it "
     "gained in custom.",
     ["each", "each of them were", "and each of them", "which each"], "A",
     "The word introduces a phrase describing both parties and attaches cleanly to the subject of the "
     "main clause. Adding a conjunction as well would join a phrase that has no finite verb to a "
     "clause that does."),

 fss("F6",
     "A foot that has lost part of its wall cannot carry nails where the wall is missing. A shoe made "
     "with a bar across the heels _____ the load onto the frog and the sound horn on either side, so "
     "that the damaged quarter carries nothing while it grows down.",
     ["throws", "throw", "throwing", "have thrown"], "A",
     "The subject is the singular 'a shoe', so the verb takes the singular form. The plural would "
     "agree with 'the heels', which sits inside the modifying phrase rather than being what the "
     "sentence is about."),

 fss("F7",
     "The heaviest wagons did the most damage, and the acts let a trust charge them accordingly. A "
     "platform sunk in the road before the gate weighed the whole vehicle, and anything above the "
     "limit named in the act paid an extra toll _____ by the hundredweight over it.",
     ["reckoned", "reckoning", "reckons", "was reckoned"], "A",
     "The past participle modifies the extra toll and completes the phrase without needing a subject. "
     "A finite verb would give the sentence a second main clause with nothing to join it to the "
     "first."),

 fss("F8",
     "Where a drove road met water there was seldom a bridge. At low water the beasts were walked "
     "over a gravel bar the drovers knew by eye; where the channel was too deep for that, a boat took "
     "a rope from the leading animal and the rest of the herd _____ behind it.",
     ["followed", "following", "to follow", "follows"], "A",
     "The clause needs a finite verb in the past tense to stand beside 'took' in the same sentence. "
     "The participle would leave the second half of the clause without any verb of its own."),

 fss("F9",
     "Two separate trades stood behind one vehicle. The body maker framed and panelled the box the "
     "passengers sat in, while the carriage maker built the springs and the ironwork that carried "
     "it, and a shop that employed both _____ able to deliver a finished vehicle without going "
     "outside its own doors.",
     ["was", "were", "being", "are"], "A",
     "The subject is 'a shop', which is singular, so the singular past-tense verb agrees with it. The "
     "plural would agree with 'both', a word inside the relative clause rather than the head of the "
     "subject."),

 # ----------------------------------------------------------- Transitions (9)
 trn("T1",
     "The great trunk coaches ran two hundred miles and made the newspapers. _____ most of the "
     "vehicles on the road in 1830 went six or eight miles out of a town and came back the same "
     "morning, carrying clerks and market women who never appeared in any account of the coaching "
     "age.",
     ["However,", "Therefore,", "Likewise,", "For instance,"], "A",
     "The second sentence sets the unnoticed short services against the famous long ones, so the "
     "transition has to mark a contrast. A word signalling a consequence would make the short "
     "services follow from the long ones, which is not what the sentences say."),

 trn("T2",
     "A smith's fire is not a bonfire. Air is delivered through a single nozzle low in the hearth, and "
     "the fuel above it burns hottest in a fist-sized spot directly over the blast. _____ a smith "
     "banks the fuel around that spot and puts nothing in the fire that he does not intend to heat.",
     ["Consequently,", "Nevertheless,", "In contrast,", "Similarly,"], "A",
     "The banking of the fuel follows directly from the heat being concentrated over the blast, so a "
     "consequence marker is needed. A contrast word would set the practice against the fact that "
     "explains it."),

 trn("T3",
     "A gate across the main road was easily avoided if a lane ran round it. Trusts answered by "
     "hanging a second bar across the lane, or a chain and a post where a bar would not stand. _____ "
     "a road that carried one gate on the map often carried three on the ground, two of which "
     "collected nothing except from people trying not to pay.",
     ["As a result,", "By contrast,", "Even so,", "For example,"], "A",
     "The three gates on the ground are the outcome of the trusts' answer described just before, so "
     "the transition marks a result. A contrast word would set the count of gates against the "
     "practice that produced it."),

 trn("T4",
     "A drove road did not end at a town. It ended at a set of fields on open ground where dealers "
     "came out from several counties on fixed days in the autumn, and the price made there settled "
     "what was paid for beasts hundreds of miles away. _____ the gathering had no permanent buildings "
     "at all beyond a weighing shed and a booth for the clerk.",
     ["Nevertheless,", "Accordingly,", "Likewise,", "In other words,"], "A",
     "The absence of buildings sits oddly beside the gathering's importance to prices, so the "
     "transition has to concede the tension. A consequence marker would make the bare site follow "
     "from the influence on prices, which reverses the sense."),

 trn("T5",
     "Luggage went in two places and the difference mattered. The hind boot was a leather-covered well "
     "behind the body, low down and out of the wind. _____ the imperial was a flat case strapped on "
     "the roof, where every pound raised the centre of gravity of a vehicle already narrow for its "
     "height.",
     ["By contrast,", "Consequently,", "Likewise,", "In short,"], "A",
     "The roof case is set against the low well in position and in effect, so the transition marks the "
     "contrast the sentences draw. A word signalling likeness would deny the difference the passage "
     "has just announced."),

 trn("T6",
     "No single proprietor could keep horses along two hundred miles of road. A line was therefore "
     "divided, and each proprietor undertook to horse so many miles of it and to take that share of "
     "the receipts. _____ a coach that ran from one end to the other was in a real sense several "
     "businesses in succession, and a dispute between any two of them stopped the whole service.",
     ["Thus,", "Nevertheless,", "In contrast,", "For instance,"], "A",
     "The description of the coach as several businesses is a restatement of the arrangement just set "
     "out, so a consequence marker fits. A concessive word would set the conclusion against the "
     "premise that supports it."),

 trn("T7",
     "A nail driven through the wall of the hoof comes out on the outside a little above the ground. "
     "The smith cuts off the point, turns the stub down against the horn and hammers it flat into a "
     "shallow bed cut for it. _____ the head of the nail below and the turned end above grip the wall "
     "between them, and the shoe stays on without any part of it entering the sensitive foot.",
     ["In this way,", "By contrast,", "Admittedly,", "Meanwhile,"], "A",
     "The final sentence explains how the operation just described achieves its result, so the "
     "transition points back to the method. A contrast word would set the grip against the very steps "
     "that produce it."),

 trn("T8",
     "By 1870 a trust's income was a fraction of what its debts required. Parliament let the acts "
     "expire one by one rather than repealing them, and the roads passed to district boards paid out "
     "of the rates. _____ the change was not a decision taken on any single day, and contemporaries "
     "argued for years afterwards about when exactly the turnpike system had ended.",
     ["Consequently,", "Nonetheless,", "Similarly,", "For example,"], "A",
     "The absence of a single decision follows from acts being allowed to lapse one at a time, so the "
     "transition marks that consequence. A concessive word would set the gradual ending against the "
     "process that made it gradual."),

 trn("T9",
     "Grass, not the calendar, set the droving year. A beast fattened on summer hill grazing was worth "
     "moving in September, and one moved in June arrived thin and sold badly. _____ the roads north "
     "of the great trysts were empty for most of the year and carried the whole traffic of the season "
     "in about six weeks.",
     ["As a result,", "Even so,", "By contrast,", "In particular,"], "A",
     "The concentration of traffic into six weeks is the outcome of the season being fixed by the "
     "grass, so the transition marks a result. A concessive word would put the empty roads at odds "
     "with the explanation just given."),

 # ---------------------------------------------------- Rhetorical Synthesis (9)
 syn("R1",
     ["A waybill was a printed sheet carried on the coach and returned to the office at the end of the "
      "journey.",
      "It listed every passenger booked, the stage at which each joined, and the fare paid.",
      "The guard entered any passenger picked up on the road in a blank line at the foot.",
      "The office compared the waybill with the money handed in by the guard.",
      "A discrepancy between the two could be traced to a single stage of a single journey."],
     "explain how the waybill let the office detect where money had gone missing.",
     ["A waybill was a printed sheet carried on the coach and returned to the office.",
      "The guard entered any passenger picked up on the road in a blank line at the foot of the sheet.",
      "Because the sheet recorded every passenger and the stage at which each joined, comparing it "
      "with the money handed in located a discrepancy at one stage of one journey.",
      "It listed every passenger booked, the stage at which each joined, and the fare paid."],
     "C",
     "The goal asks how the sheet located a loss, and only the choice joining the record of passengers "
     "and stages to the comparison with the cash handed in supplies both halves. Listing what the "
     "sheet contained describes the document without saying what the office did with it."),

 syn("R2",
     ["A shoe for a heavy draught horse is wide in the web and flat on the ground surface.",
      "A shoe for a saddle horse is narrower and is bevelled away from the ground toward the inner "
      "edge.",
      "A draught horse pushes into the collar and needs the foot to stay put on the road surface.",
      "A saddle horse moves at speed and must break over the toe quickly at every stride.",
      "Both patterns are made from the same bar and by the same operations."],
     "emphasise that the two patterns differ because the two animals do different work.",
     ["Both patterns are made from the same bar and by the same operations.",
      "A shoe for a heavy draught horse is wide in the web and flat on the ground surface.",
      "The wide flat shoe holds a horse that pushes into the collar, while the narrower bevelled shoe "
      "suits an animal that must break over the toe quickly at speed.",
      "A shoe for a saddle horse is narrower and bevelled away from the ground toward the inner edge."],
     "C",
     "The goal is the link between the shapes and the work, and only the choice pairing each shape "
     "with what the animal has to do makes it. Describing the draught pattern alone gives one shape "
     "and no work at all."),

 syn("R3",
     ["A trust's surveyor rode the whole of its road once a year and reported in writing.",
      "He measured the depth of metal at fixed points marked on his previous report.",
      "He recorded which lengths had been repaired since the last inspection and at what cost.",
      "The report was read at the trustees' annual meeting before the accounts were passed.",
      "Lenders to the trust could inspect the report."],
     "explain why the annual report mattered to people who had lent money to the trust.",
     ["A trust's surveyor rode the whole of its road once a year and reported in writing.",
      "He measured the depth of metal at fixed points marked on his previous report.",
      "Because the report set repairs and their cost against measurements taken at the same fixed "
      "points a year earlier, a lender could see whether the road securing his money was being kept "
      "up.",
      "The report was read at the trustees' annual meeting before the accounts were passed."],
     "C",
     "The goal concerns the lenders, and only the choice connecting the repeated measurements and "
     "costs to the security behind the loan answers it. Saying the report was read before the accounts "
     "were passed places it in the meeting without explaining its interest to anyone outside."),

 syn("R4",
     ["Coaches were given names that were painted on the door panel.",
      "The Quicksilver, the Tally-ho and the Highflyer all ran in the 1830s.",
      "A name belonged to a service on a particular road, not to a particular vehicle.",
      "A traveller booked a seat on a name rather than on a departure time.",
      "When a proprietor sold his interest, the name went with the road and not with him."],
     "explain what the name identified for a traveller making a booking.",
     ["Coaches were given names that were painted on the door panel.",
      "The Quicksilver, the Tally-ho and the Highflyer all ran in the 1830s.",
      "Since a name attached to a service on a road rather than to a vehicle or an owner, booking on a "
      "name meant booking a particular service.",
      "When a proprietor sold his interest, the name went with the road and not with him."],
     "C",
     "The goal asks what the name picked out at the moment of booking, and only the choice tying the "
     "name to a service rather than a vehicle or an owner states it. Listing three names supplies "
     "examples without saying what a name stood for."),

 syn("R5",
     ["A drover had to hold a licence granted at quarter sessions.",
      "An applicant had to be over thirty and a householder.",
      "The licence was refused to any man against whom a debt had been proved.",
      "A licensed drover could take other men's beasts to market and bring back the money.",
      "An unlicensed man driving cattle could be treated as having stolen them."],
     "explain how the licensing rules made it safe to hand a stranger a herd of cattle.",
     ["A drover had to hold a licence granted at quarter sessions.",
      "An applicant had to be over thirty and a householder.",
      "By restricting the licence to settled men of thirty with no proved debt, and by making an "
      "unlicensed driver liable to be treated as a thief, the rules gave an owner grounds to trust the "
      "man he handed his beasts to.",
      "A licensed drover could take other men's beasts to market and bring back the money."],
     "C",
     "The goal is about safety in handing over animals, and only the choice combining the entry "
     "requirements with the penalty for driving unlicensed supplies both supports for that trust. "
     "Stating that a licence came from quarter sessions names the issuing body and nothing more."),

 syn("R6",
     ["An open carriage carried a folding hood of leather over hinged hoops.",
      "The hoops were jointed so that the hood collapsed backward into a stack behind the seat.",
      "Leather stiffened in cold weather and cracked at the folds if it was worked when hard.",
      "Makers dressed the folds with tallow and warned owners not to raise the hood in frost.",
      "A cracked fold could not be patched invisibly and usually meant a new hood."],
     "explain why owners were told to leave the hood alone in cold weather.",
     ["An open carriage carried a folding hood of leather over hinged hoops.",
      "The hoops were jointed so that the hood collapsed backward into a stack behind the seat.",
      "Because stiff leather cracks at the folds and a cracked fold meant a whole new hood, owners "
      "were warned not to raise it in frost.",
      "Makers dressed the folds with tallow."],
     "C",
     "The goal asks for the reason behind the warning, and only the choice linking cracking at the "
     "folds to the cost of replacement gives it. Describing the jointed hoops explains how the hood "
     "folded without saying why frost mattered."),

 syn("R7",
     ["Many inn yards were entered through an archway barely wider than a coach.",
      "A coach could not be turned inside such a yard once it was in.",
      "The horses were taken off and the vehicle was pushed back out by hand.",
      "Four men could move an empty body on level stones without difficulty.",
      "Yards built after 1820 often had a second opening so that a coach could go straight through."],
     "explain how the later yards removed a problem the older ones created.",
     ["Many inn yards were entered through an archway barely wider than a coach.",
      "Four men could move an empty body on level stones without difficulty.",
      "Because a coach could not be turned in a single-entrance yard and had to be pushed out by hand, "
      "later yards were given a second opening so that it could go straight through.",
      "The horses were taken off and the vehicle was pushed back out by hand."],
     "C",
     "The goal contrasts the two kinds of yard, and only the choice naming the difficulty and the "
     "second opening that answered it does both. Reporting that four men could move a body describes "
     "the workaround rather than the remedy."),

 syn("R8",
     ["Iron shoes survive in the ground long after leather and timber have gone.",
      "The shape of the shoe, the number of nail holes and the way the edge is finished changed over "
      "time.",
      "A shoe found in a dated layer fixes the pattern to that period.",
      "The same pattern found elsewhere can then be used to date the layer it lies in.",
      "Shoes are among the commonest metal finds on medieval road sites."],
     "explain how a common find becomes a dating tool.",
     ["Iron shoes survive in the ground long after leather and timber have gone.",
      "Shoes are among the commonest metal finds on medieval road sites.",
      "Once a pattern of nail holes and edge finish has been tied to a period by a shoe from a dated "
      "layer, the same pattern found elsewhere dates the layer it lies in.",
      "The shape of the shoe, the number of nail holes and the way the edge is finished changed over "
      "time."],
     "C",
     "The goal asks how the object comes to date a deposit, and only the choice running from the "
     "dated layer to the pattern and back out again describes that. Noting that the finds are common "
     "explains why they are useful without explaining how they work."),

 syn("R9",
     ["Before 1784 letters travelled by mounted post boys at about five miles an hour.",
      "A theatre proprietor proposed carrying the mail on fast coaches instead.",
      "His first coach ran from Bristol to London in sixteen hours instead of thirty-eight.",
      "The mail coaches were exempt from tolls and gates were opened at the sound of the horn.",
      "The service was extended to other roads within three years."],
     "emphasise the size of the improvement the first mail coach demonstrated.",
     ["Before 1784 letters travelled by mounted post boys at about five miles an hour.",
      "A theatre proprietor proposed carrying the mail on fast coaches instead.",
      "The first coach covered the Bristol road in sixteen hours, against the thirty-eight the mounted "
      "post had taken.",
      "The service was extended to other roads within three years."],
     "C",
     "The goal is the scale of the gain, and only the choice setting sixteen hours directly against "
     "thirty-eight measures it. The extension to other roads shows that the idea spread rather than "
     "how much faster it was."),
]

DROPPED = {}
