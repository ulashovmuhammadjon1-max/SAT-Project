#!/usr/bin/env python3
"""
Reading & Writing authored for Test 30.

All 81 items are original. The transcribed pool was spent by Test 8, and for
R&W authoring is in any case the safer route: a transcribed answer key has to
be re-derived by hand before it can be trusted (Test 5 shipped 6 wrong answers
in 81 that way). Every item below carries a `why` that records the reasoning
which produced the key AND the reason the strongest distractor fails — that
record IS the verification, so no key exists here without one.

Rationales name options by their CONTENT, never by letter, so balance_rw.py is
free to rotate every question when it evens out the key distribution.

Writing-domain choices are never bare punctuation. Test 8 shipped Boundaries
items whose four options were ", " / "; " / ": " / " and ", which a student
sees as four empty rows. The real test repeats the words on either side of the
blank inside every option so each choice reads as the resulting sentence, and
every Boundaries item here is written that way from the start.

WHAT THIS BUILD HAD TO DO DIFFERENTLY — the Test 23 lesson
----------------------------------------------------------
Test 30's territory is narrow: physic gardens, essential-oil distilling,
apothecary dispensing and weights, herbarium pressing, and seed drying and
storage. Test 23 had the LOWEST corpus overlap of any build (0.14) and still
failed on 15 internal same-subject pairs, one at 0.56 where the same paragraph
appeared twice. A narrow territory collides with ITSELF, not with the bank.

So the topic list here is sized to the ITEM count (81 distinct sub-topics), not
to the block count, and every one is written out below against the item that
uses it. The specific trap Test 23 named is that a Rhetorical Synthesis note
list is a sub-topic's core facts stated plainly, so pairing it with a
Words-in-Context passage on the same sub-topic makes collision the default.
The nine synthesis subjects (S1-S9) are therefore drawn from sub-topics that NO
passage in this file uses:

    S1 layering            S2 camera lucida       S3 pollinator plantings
    S4 clary sage          S5 herbarium loans     S6 the fragment packet
    S7 seed provenance     S8 teaching medical students
    S9 Latin abbreviations on prescriptions

Topics were screened against ../rw_authored_corpus.json — 1,295 passages banked
or authored across Tests 1-29 — with check_originality.py in this directory.
Four candidates were dropped before drafting rather than paraphrased around,
each because a corpus passage already covers it:

    seed-bank accession numbering        (rw_test18:W15 already numbers lots)
    germination testing on a fixed cycle (rw_test18:N8 sows and counts)
    grow-out regeneration of a bank lot  (rw_test18:N8 again)
    historical DNA from old specimens    (rw_octusb_m2:9)

Their slots went to stored-seed insect pests, vacuum drying, seed oil rancidity
and the herbarium as evidence of a former range.

Block counts (fixed by the assembler's quota, 3 modules x 27):
    Words in Context 15, Text Structure and Purpose 6,
    Central Ideas and Details 6, Command of Evidence 9, Inferences 6,
    Boundaries 12, Form, Structure, and Sense 9, Transitions 9,
    Rhetorical Synthesis 9                                        = 81
"""

SOURCE = "AUTHORED-T30"
MODULE = "RW"

TABLE = '<table style="border-collapse:collapse;margin:0.75rem 0;">{head}{body}</table>'
TH = '<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;">{}</th>'
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">{}</td>'


def table(headers, rows):
    head = "<tr>" + "".join(TH.format(h) for h in headers) + "</tr>"
    body = "".join("<tr>" + "".join(TD.format(c) for c in r) + "</tr>" for r in rows)
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
     "The garden laid out at Padua in 1545 was walled and planted in geometric quarters, and its "
     "beds were arranged so that a student could walk the paths and meet the plants of a lecture "
     "in the order the lecturer treated them. Nothing about the design was ornamental in intention. "
     "The layout was a piece of _____, built so that the ground itself would hold the lesson "
     "together.",
     ["teaching apparatus", "civic display", "private recreation", "commercial nursery"], "A",
     "The passage says the beds follow the order of a lecture so the ground holds the lesson "
     "together, which makes the garden an instrument for instruction. The civic-display option is "
     "ruled out by the sentence denying that anything in the design was ornamental in intention."),

 wic("W2",
     "Living plants shipped from the tropics in the eighteenth century usually arrived dead: salt "
     "spray, darkness below deck and a sailor's grudging ration of fresh water killed almost every "
     "consignment. Nathaniel Ward's sealed glazed box changed the arithmetic. Water transpired by "
     "the leaves condensed on the glass and ran back to the soil, so a case needed no attention at "
     "all for months, and survival on the long voyages became the _____ rather than the exception.",
     ["rule", "hazard", "expense", "argument"], "A",
     "The sentence sets what happened after the case against the word exception, so the blank names "
     "the ordinary outcome, and the passage has just explained why consignments now lived. The "
     "hazard option reverses the sense, since a hazard is what the sealed case removed."),

 wic("W3",
     "The oldest way of taking oil from a plant was to boil the material in water over a direct "
     "fire, but anything resting on the bottom of the vessel scorched, and burnt notes carried "
     "through into the distillate. Passing steam up through a loosely packed charge instead keeps "
     "the plant material off the heated metal altogether. The change was made not to raise the "
     "yield but to _____ a fault that no later rectification could remove.",
     ["forestall", "diagnose", "tolerate", "disguise"], "A",
     "The passage says the burnt character could not be removed once it had passed into the "
     "distillate, so the point of the new method is to stop the fault arising at all. The "
     "disguise option would mean covering up a fault that had already occurred, which is exactly "
     "what the text says cannot be done afterwards."),

 wic("W4",
     "What runs from the condenser is not oil but a mixture: a small volume of oil and a much "
     "larger volume of water that came over with it. The two are collected in a narrow vessel with "
     "an outlet at the neck and another at the foot, so that the lighter layer can be drawn from "
     "the top while the heavier is bled away below. The vessel performs no chemistry whatever; its "
     "whole function is _____.",
     ["separation", "purification", "measurement", "storage"], "A",
     "The vessel is described as drawing off one layer at the top and the other at the foot, which "
     "is the dividing of a mixture into its parts. The purification option overstates what the "
     "text allows, since the passage insists the vessel performs no chemistry."),

 wic("W5",
     "An apothecary's scale ran in grains, twenty grains to the scruple and three scruples to the "
     "drachm, and a dispenser weighing out a powerful drug worked at the bottom of that ladder. A "
     "difference of two or three grains in a dose meant nothing in a mild preparation and a great "
     "deal in a strong one, so the same balance and the same weights were used with a care that "
     "looked _____ to anyone who did not know which drug was on the pan.",
     ["excessive", "careless", "habitual", "inexpensive"], "A",
     "The sentence contrasts what an outsider sees with what the dispenser knows, and the outsider "
     "does not know that a few grains matter, so the care looks like more than the job requires. "
     "The habitual option describes a settled routine rather than the mismatch of appearances the "
     "sentence is built on."),

 wic("W6",
     "Nineteenth-century pharmacies kept their most dangerous preparations in bottles moulded with "
     "deep vertical ribs, and often in a distinctive dark blue as well. The ribbing was not "
     "decorative. A hand reaching along a dark shelf at night meets the ridges before it lifts the "
     "bottle, so the container announces its contents by _____ before anyone has read a word of the "
     "label.",
     ["touch", "colour", "weight", "smell"], "A",
     "The passage describes a hand meeting the ridges in the dark, which is recognition through "
     "feel. The colour option is mentioned in the passage but cannot be what the sentence means, "
     "since the situation described is one in which nothing can be seen."),

 wic("W7",
     "A specimen laid in a press is not simply squeezed. Sheets of blotting paper drink the water "
     "out of the leaves, corrugated ventilators let a current of warm air run between the layers, "
     "and the blotters are changed daily until nothing more comes out. Pressure alone would give a "
     "flat brown specimen; it is the steady removal of water that leaves the colour _____.",
     ["intact", "muted", "uniform", "faded"], "A",
     "The sentence sets the brown result of pressure alone against what drying achieves, so the "
     "blank names colour that has been kept. The faded option restates the bad outcome the "
     "sentence is contrasting with."),

 wic("W8",
     "A pressed plant with no label is a curiosity; a pressed plant with a full label is evidence. "
     "The slip glued to the corner of the sheet gives the collector, the number, the day, the "
     "parish and the ground the plant was standing in, and every later use of the specimen &mdash; "
     "mapping a range, dating a flowering, matching a name &mdash; draws on that slip rather than "
     "on the plant. The specimen is the label's _____.",
     ["attachment", "author", "duplicate", "successor"], "A",
     "The passage says every later use draws on the slip rather than on the plant, which inverts "
     "the expected relation and makes the plant the thing that comes with the record. The author "
     "option would make the plant the source of the label's information, which is the ordinary "
     "relation the sentence is deliberately reversing."),

 wic("W9",
     "Most seeds can be dried to a few per cent of their weight in water and stored for decades. "
     "The seeds of oaks, horse chestnuts and many rainforest trees cannot: dry them below about a "
     "quarter of their fresh weight and they die outright, so a store that would preserve wheat "
     "for a century destroys an acorn in a fortnight. For these species the standard method of "
     "conservation is not merely ineffective but _____.",
     ["actively destructive", "unusually costly", "widely misunderstood", "difficult to arrange"], "A",
     "The passage says drying kills these seeds outright and that the store destroys an acorn, so "
     "the method does harm rather than simply failing. The costly option introduces expense, which "
     "the passage never raises."),

 wic("W10",
     "A drying room can be brought to a low humidity with refrigeration and heat, but the "
     "machinery is expensive and stops when the current does. A tin of self-indicating silica gel "
     "does the same work for a small quantity of seed: the gel takes up water vapour until the air "
     "in the sealed tin is very dry, and its colour shows when it has taken all it can. For a "
     "collector working far from a laboratory the tin's chief merit is its _____.",
     ["self-sufficiency", "capacity", "precision", "durability"], "A",
     "The passage sets the gel against machinery that is expensive and stops with the current, and "
     "praises it for a collector working far from a laboratory, so the merit is that it needs "
     "nothing else to work. The capacity option points to how much water the gel holds, which the "
     "passage treats as limited rather than as its advantage."),

 wic("W11",
     "Sowing a sample and counting the seedlings answers the question of viability in a fortnight "
     "or more, and for a species that must first be chilled it can take a season. Soaking a cut "
     "seed in a colourless salt of tetrazolium answers it in a few hours instead: living tissue "
     "reduces the salt to a red dye and dead tissue stays pale, so the embryo reports its own "
     "condition. The test does not improve on sowing for accuracy; what it offers is _____.",
     ["speed", "cheapness", "simplicity", "certainty"], "A",
     "The passage measures the two methods against each other in time, a fortnight or a season set "
     "against a few hours, and then denies any gain in accuracy. The certainty option is ruled out "
     "by the sentence saying the stain does not improve on sowing for accuracy."),

 wic("W12",
     "Early herbals held that a plant's use could be read from its appearance: a leaf shaped like a "
     "liver treated the liver, and a root with the look of a joint treated joints. The rule made "
     "the pharmacopoeia easy to teach and easy to remember, which is a great deal of its "
     "attraction, but it offered no way of finding out that it was wrong. Any failure could be "
     "charged to the preparation or the practitioner, so the doctrine was in practice _____.",
     ["untestable", "unpopular", "unwritten", "unremarkable"], "A",
     "The passage says any failure could be blamed on something other than the rule, which leaves "
     "no observation that could count against it. The unpopular option contradicts the sentence "
     "crediting the doctrine with a great deal of attraction."),

 wic("W13",
     "A tincture can be made by steeping the drug in spirit for days and then straining, or by "
     "letting spirit trickle slowly down through a packed column of it. Steeping stops when the "
     "liquid and the drug reach a balance and no more will come out. Percolation never reaches that "
     "balance, because fresh spirit is always arriving at the top, and the difference in strength "
     "between the two products is therefore _____ rather than accidental.",
     ["structural", "slight", "temporary", "disputed"], "A",
     "The passage traces the difference to the way each method works &mdash; one reaches a balance "
     "and one cannot &mdash; so it follows from the arrangement itself. The slight option is "
     "contradicted by the passage treating the difference as something to be explained."),

 wic("W14",
     "It takes something in the region of three tonnes of petals to make a kilogram of rose oil, "
     "and the petals must be picked before the sun is high and distilled the same day. No amount of "
     "skill at the still alters that ratio, which is fixed by how little oil a rose flower contains. "
     "The price of the oil is therefore governed less by the distiller's art than by _____.",
     ["the labour of the harvest", "the design of the still", "the length of the season",
      "the cost of the fuel"], "A",
     "The passage fixes the ratio in the flower and then denies that skill at the still can change "
     "it, leaving the three tonnes of hand-picked petals as the governing cost. The design of the "
     "still is ruled out by the sentence saying no amount of skill at the still alters the ratio."),

 wic("W15",
     "Seed of many northern trees will not germinate when it is sown fresh, however warm and moist "
     "the ground. It must first pass some weeks cold and damp, a condition the seed meets under snow "
     "and the nurseryman supplies in a box of moist sand in a cold shed. The delay is not a defect "
     "in the seed but a _____: it keeps a seed shed in autumn from sprouting into the winter that "
     "would kill it.",
     ["safeguard", "consequence", "measurement", "coincidence"], "A",
     "The colon explains that the delay stops autumn-shed seed from sprouting into a killing "
     "winter, which makes it a protection. The consequence option names the delay as a result of "
     "something rather than as something that does work for the seed, which is the contrast the "
     "sentence draws with the word defect."),

 # ---------------------------------------------- Text Structure and Purpose (6)
 tsp("T1",
     "Botanic gardens have exchanged seed by printed list for more than two centuries. Each garden "
     "issues a catalogue of what it has ripened that year and may request from any other garden's "
     "catalogue in return, with no money passing in either direction. <u>The arrangement survives "
     "because a garden's surplus costs it nothing and its wants cost it nothing either.</u> A "
     "curator with a spare hundred seeds of a plant nobody else grows loses no advantage by "
     "sending ninety of them away.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It identifies the feature of the exchange that accounts for its persistence.",
      "It concedes a weakness in the exchange that later gardens had to correct.",
      "It compares the exchange with the commercial seed trade of the same period.",
      "It questions whether the catalogues accurately describe what is offered."], "A",
     "The underlined sentence gives the reason the arrangement survives, and the sentence after it "
     "illustrates that reason with the curator who loses nothing. Nothing in the passage sets the "
     "exchange against a commercial trade, so the comparison option describes a move the text "
     "never makes."),

 tsp("T2",
     "Rose petals give up their oil grudgingly, and a first distillation leaves much of the most "
     "fragrant material dissolved in the water that comes over with it. Distillers therefore "
     "return that water to the still and pass it through a second time, sometimes with a fresh "
     "charge of petals in it. The practice recovers oil that would otherwise be poured away, and "
     "it also concentrates the water itself into the rose water sold as a product in its own right.",
     "Which choice best states the main purpose of the text?",
     ["To explain a step in rose distilling and identify the two benefits it yields",
      "To argue that rose water is more valuable than the oil recovered alongside it",
      "To trace the history of rose distilling from its origins to the present day",
      "To compare the yields obtained by distillers working in different regions"], "A",
     "The passage describes returning the distillation water to the still and then names two "
     "results, recovered oil and a saleable rose water. The claim that rose water is worth more "
     "than the oil is never made; the text presents both as gains from the same step."),

 tsp("T3",
     "The tall waisted jar of tin-glazed earthenware that stood on an apothecary's shelf is now "
     "prized for its painted decoration, but the panel that matters is the plain band across its "
     "belly. On it the contents were written in abbreviated Latin, and because the glaze could be "
     "scraped and repainted the band could be rewritten when the jar was given to another drug. "
     "<u>The jar was designed to outlast any particular thing put into it.</u>",
     "Which choice best describes the function of the underlined sentence in the text?",
     ["It draws a conclusion from the rewritable label the passage has just described.",
      "It introduces an objection to the value collectors place on the jars.",
      "It provides an example of the abbreviated Latin used on the band.",
      "It shifts the discussion from the jar's decoration to its manufacture."], "A",
     "The sentence follows the account of a band that could be scraped and repainted and states "
     "what that feature shows about the jar's purpose, which is a conclusion drawn from the "
     "evidence given. It offers no example of the Latin, so the example option describes something "
     "the sentence does not contain."),

 tsp("T4",
     "When a botanist publishes a new species, one pressed specimen is designated as the permanent "
     "point of reference for the name. Later workers who disagree about what the name covers do not "
     "argue from descriptions, which are always incomplete, but go back to that sheet. The specimen "
     "settles nothing about how wide the species should be drawn; it settles only which plant the "
     "name is anchored to, which is a smaller question and a far more answerable one.",
     "Which choice best states the main purpose of the text?",
     ["To explain what the designated specimen does and does not decide",
      "To criticise botanists for publishing incomplete species descriptions",
      "To describe how a specimen is pressed, mounted and stored for reference",
      "To recommend that more than one specimen be designated for each name"], "A",
     "The text describes the specimen as the anchor for a name and then explicitly separates the "
     "question it settles from the one it does not. Incomplete descriptions are mentioned only as "
     "the reason for going back to the sheet, so criticism of botanists is not the point being "
     "made."),

 tsp("T5",
     "A paper packet lets water vapour through, slowly but without limit, so seed stored in paper "
     "eventually comes to the humidity of the room around it however dry it was when it went in. A "
     "laminate of aluminium foil between two plastic films does not, and a seam heat-sealed across "
     "it does not either. The packet does not dry the seed. It fixes whatever dryness the seed "
     "already had at the moment it was closed.",
     "Which choice best describes the overall structure of the text?",
     ["It contrasts two packaging materials and then states precisely what the better one achieves.",
      "It describes a sequence of steps in the order a seed store performs them.",
      "It presents a claim about packaging and then supplies data that qualify it.",
      "It defines a technical term and then traces how its meaning has changed."], "A",
     "The first two sentences set paper against foil laminate, and the last two say what the "
     "laminate does, which is to hold a dryness rather than create one. No figures appear anywhere "
     "in the passage, so the option about supplying data misdescribes it."),

 tsp("T6",
     "A germination cabinet held at a steady temperature will fail to sprout seed that germinates "
     "readily in a seedbed. Many species respond instead to the swing between a warm day and a cool "
     "night, and cabinets are therefore run on a cycle, sixteen hours at one temperature and eight "
     "at another. <u>The seed is not measuring warmth; it is measuring change.</u> A constant "
     "twenty degrees carries no information about whether the seed is buried deep or lying near the "
     "surface, and a daily swing does.",
     "Which choice best describes the function of the underlined sentence in the text?",
     ["It states the principle that the surrounding sentences illustrate.",
      "It acknowledges a limitation of germination cabinets that the text goes on to accept.",
      "It reports a finding that contradicts the claim made in the first sentence.",
      "It defines a term that the rest of the passage uses in a specialised sense."], "A",
     "The sentence names what the seed is responding to, and the sentences on either side give the "
     "cabinet cycle and the depth signal as instances of it. It agrees with the first sentence "
     "rather than contradicting it, since the failure at a steady temperature is exactly what the "
     "principle predicts."),

 # ------------------------------------------------ Central Ideas and Details (6)
 cid("C1",
     "A brick wall running east and west does more for the garden on its southern side than block "
     "the wind. It takes in heat all day and gives it back through the night, so the air within a "
     "few feet of it never falls as far as the air in the open ground beyond. Gardeners planted "
     "apricots and figs against such walls in counties where those trees will not set fruit "
     "otherwise, and the plants were not hardier there; the frost simply reached them later and "
     "left them sooner.",
     "Which choice best states the main idea of the text?",
     ["A wall extends the growing season next to it by moderating night temperatures rather than "
      "by altering the plants.",
      "Apricots and figs grown against walls are hardier than the same varieties grown in open "
      "ground.",
      "The chief benefit of a garden wall is the shelter it provides from prevailing winds.",
      "Gardeners in cold counties abandoned tender fruit once open-ground varieties became "
      "available."], "A",
     "The passage attributes the success of the fruit to heat released at night and then states "
     "directly that the plants were not hardier. The option calling the plants hardier is the "
     "reading the last clause was written to rule out."),

 cid("C2",
     "The peppermint plant makes its oil in glands on the leaf, and the composition of that oil "
     "changes as the season advances. Early in flowering the oil is high in menthone, which smells "
     "sharp and slightly bitter; as flowering proceeds the menthone is progressively converted to "
     "menthol, which gives the cooling character the crop is grown for. A grower who cuts too early "
     "loses nothing in weight of oil and a great deal in what buyers will pay for it.",
     "According to the text, what is the consequence of cutting a peppermint crop early?",
     ["The oil obtained is worth less because less of its menthone has become menthol.",
      "The oil obtained is smaller in quantity because the glands are not yet full.",
      "The plants regrow more slowly and yield less at the following cutting.",
      "The oil obtained contains no menthol at all and cannot be sold."], "A",
     "The last sentence says an early cut costs nothing in weight but a great deal in price, and "
     "the sentence before it explains that menthol accumulates at menthone's expense as flowering "
     "proceeds. The option about a smaller quantity is contradicted by the statement that nothing "
     "is lost in weight of oil."),

 cid("C3",
     "Two systems of weight were in daily use in an English shop. Goods over the counter were sold "
     "by the avoirdupois ounce, of which there are sixteen to the pound; drugs were compounded by "
     "the troy ounce, of which there are twelve. The troy ounce is the heavier of the two, so an "
     "ounce of a drug and an ounce of sugar were different quantities, and a dispenser who reached "
     "for the wrong set of weights made an error that no arithmetic later in the prescription would "
     "reveal.",
     "According to the text, why was confusion between the two systems particularly serious in "
     "dispensing?",
     ["The mistake left no trace that the rest of the calculation would expose.",
      "The troy system was being withdrawn while the avoirdupois system remained in use.",
      "Drugs were sold over the counter in the same shop as ordinary goods.",
      "The two kinds of ounce were so close in weight that a balance could not tell them apart."], "A",
     "The final clause says no arithmetic later in the prescription would reveal the error, which "
     "is what makes the confusion dangerous. The passage states that the troy ounce is the heavier "
     "of the two, so the option calling them too close for a balance contradicts the text."),

 cid("C4",
     "A nineteenth-century botanist who found an interesting plant in quantity would press fifty or "
     "a hundred sheets of it, number them identically, and post sets to institutions across Europe. "
     "The recipients bound them into their own collections, so a single afternoon's collecting is "
     "now represented on shelves in a dozen countries. The practice has an unintended value: when "
     "one herbarium burned, as several did in the twentieth century, the sheets it held were "
     "seldom unique.",
     "Which choice best states the main idea of the text?",
     ["Distributing identical sets of specimens widely had the incidental effect of protecting the "
      "material against loss.",
      "Botanists distributed duplicate specimens chiefly in order to guard against fires in "
      "herbaria.",
      "Herbarium fires in the twentieth century destroyed most of the specimens collected in the "
      "nineteenth.",
      "A specimen is valuable only when the herbarium holding it can show that no copy exists "
      "elsewhere."], "A",
     "The passage describes a distribution practice and then calls its protective effect "
     "unintended, which is precisely an incidental benefit. The option making protection the chief "
     "motive is ruled out by the word unintended."),

 cid("C5",
     "Two rules of thumb have guided seed storage since the 1960s. Each one per cent reduction in "
     "the moisture content of a seed roughly doubles the time it will remain alive, and so does "
     "each fall of about five degrees Celsius in the storage temperature. The rules hold only "
     "within limits &mdash; below about five per cent moisture further drying stops helping and "
     "may harm &mdash; but within those limits they let a store predict the effect of a change "
     "before making it.",
     "According to the text, what is the practical value of the two rules?",
     ["They allow the effect of a change in storage conditions to be estimated in advance.",
      "They identify the single storage condition that matters more than any other.",
      "They establish the exact number of years a given seed lot will remain alive.",
      "They show that drying seed is beneficial no matter how far it is taken."], "A",
     "The last clause says the rules let a store predict the effect of a change before making it. "
     "The option about drying being always beneficial contradicts the passage's statement that "
     "below about five per cent further drying may harm."),

 cid("C6",
     "A pressed orchid flower is a brown smear, and a pressed fungus is worse. Herbaria therefore "
     "keep a second, wet collection: the flower or the fruiting body goes whole into a jar of "
     "spirit, where it holds its shape and something of its colour indefinitely. The jars take a "
     "hundred times the shelf space of a sheet and cannot be posted, so nothing goes into spirit "
     "that would survive the press, and the two collections between them cover what neither could "
     "cover alone.",
     "According to the text, why do herbaria not preserve all their material in spirit?",
     ["Spirit collections demand far more space and cannot be sent through the post.",
      "Specimens kept in spirit lose their colour more quickly than pressed ones do.",
      "The cost of spirit rose beyond what most herbaria could afford.",
      "Pressed sheets record collecting data that jars have no room to carry."], "A",
     "The passage gives two reasons in one clause, a hundred times the shelf space and the "
     "impossibility of posting, and draws the restriction from them. The option about colour "
     "reverses the text, which says spirit holds something of the colour indefinitely."),

 # --------------------------------------------------- Command of Evidence (9)
 coe("E1",
     "Distillers of lavender disagree about how long a charge should be run. A grower kept the "
     "still going for four hours on one charge and recorded the oil collected in each hour "
     "separately, obtaining the results shown."
     + table(["Hour of the run", "Oil collected in that hour (millilitres)"],
             [["First", "310"], ["Second", "96"], ["Third", "24"], ["Fourth", "9"]]),
     "Which choice best describes data from the table that support the claim that most of a "
     "lavender charge's oil comes over early in the run?",
     ["The first hour yielded 310 millilitres, more than twice the total collected in the "
      "remaining three hours.",
      "The fourth hour yielded 9 millilitres, the smallest quantity recorded in the run.",
      "The oil collected fell in every hour of the run after the first.",
      "The second hour yielded 96 millilitres, which is more than the third and fourth hours "
      "together."], "A",
     "The claim is about the share of the total taken early, so the support must weigh the first "
     "hour against the rest, and 310 against a remaining 129 does exactly that. Noting that the "
     "fourth hour was smallest describes the shape of the decline without showing that the early "
     "part dominates the whole."),

 coe("E2",
     "The head gardener of a physic garden kept a daily book through the winter of 1837, recording "
     "the temperature of each glasshouse at seven in the morning together with what he had done to "
     "the flues the night before. Historians of horticulture have used the book to argue that he "
     "was managing the houses to a target rather than simply keeping them from freezing.",
     "Which quotation from the daily book most effectively illustrates the historians' claim?",
     ["&ldquo;Stove at 62 this morning, three degrees above what I want it; damped the flue at ten "
      "last night and shall damp it earlier tonight.&rdquo;",
      "&ldquo;Hard frost again, and the water in the tank frozen an inch thick by morning.&rdquo;",
      "&ldquo;The new house is finished, and the glazier has left his ladder against the "
      "orangery.&rdquo;",
      "&ldquo;Fired the stove late, the wind being in the east and the night bitter.&rdquo;"], "A",
     "The claim is that the gardener worked to a target, and the quotation naming a figure he "
     "wants, measuring the departure from it and adjusting the flue accordingly shows exactly "
     "that. The entry about firing late on a bitter night shows a response to cold without any "
     "target being named."),

 coe("E3",
     "Oil of peppermint has long been diluted with cheaper material before sale. A pure oil rotates "
     "the plane of polarised light through a characteristic angle, and mixtures do not, so a "
     "polarimeter reading has been used as a check on purity since the nineteenth century. A "
     "chemist proposes that the reading cannot by itself establish that a sample is unadulterated.",
     "Which finding, if true, would most directly support the chemist's proposal?",
     ["Two different diluents, added together in the right proportions, leave the sample's rotation "
      "unchanged from that of the pure oil.",
      "The rotation of pure peppermint oil varies slightly with the temperature at which it is "
      "measured.",
      "Polarimeters manufactured before 1900 were less precise than modern instruments.",
      "Some adulterated samples show a rotation far outside the range expected of pure oil."], "A",
     "The proposal is that a normal reading does not prove purity, and a pair of diluents that "
     "cancel each other's effect on the rotation produces exactly that situation. The finding "
     "about adulterated samples reading far outside the expected range shows the test working, "
     "which is the opposite of what the chemist claims."),

 coe("E4",
     "A store dried one seed lot to several different moisture contents, sealed each portion, held "
     "them all at the same temperature for ten years and then tested them. The results are shown."
     + table(["Moisture content at sealing", "Seeds germinating after ten years"],
             [["11 per cent", "18 per cent"], ["9 per cent", "54 per cent"],
              ["7 per cent", "88 per cent"], ["5 per cent", "91 per cent"]]),
     "Which choice best describes data from the table that support the claim that the benefit of "
     "further drying falls away at the dry end of the range?",
     ["Germination rose by 34 points between 9 and 7 per cent moisture but by only 3 points "
      "between 7 and 5 per cent.",
      "Germination was highest, at 91 per cent, in the portion sealed at 5 per cent moisture.",
      "Germination was lowest, at 18 per cent, in the portion sealed at 11 per cent moisture.",
      "Germination rose at every step as the moisture content at sealing was reduced."], "A",
     "The claim concerns how much each further step of drying buys, so the support must compare "
     "the size of successive gains, and 34 points against 3 points does that. Reporting that the "
     "driest portion germinated best shows drying helping without saying anything about "
     "diminishing returns."),

 coe("E5",
     "An apothecary in a market town kept a register in which every prescription dispensed was "
     "copied out with the date, the prescriber and the patient. A historian argues that the "
     "register was kept as a defence against later dispute rather than as a stock record.",
     "Which quotation from the register most effectively supports the historian's argument?",
     ["&ldquo;Sent this day to Mrs Havering, per Dr Ellis's order of the 4th, which order I have "
      "pinned within and witnessed by my apprentice.&rdquo;",
      "&ldquo;Six ounces of syrup of poppies made up this morning and set upon the second "
      "shelf.&rdquo;",
      "&ldquo;Received of the wholesaler two pounds of senna and one of jalap.&rdquo;",
      "&ldquo;The mortar cracked in use and a new one is bespoke from Bristol.&rdquo;"], "A",
     "The historian's claim is about protection in a dispute, and the entry that keeps the "
     "prescriber's written order pinned in place and has a witness to the dispensing is a record "
     "built for exactly that. The entry recording a quantity made up and shelved is stock-keeping, "
     "which is the alternative the historian rejects."),

 coe("E6",
     "The leaves of a plant take up some of what is in the air around them, and a pressed leaf "
     "keeps that burden for as long as the sheet survives. A researcher proposes that herbarium "
     "collections can be read as a record of air quality in the districts where the plants were "
     "gathered.",
     "Which finding, if true, would most directly support the researcher's proposal?",
     ["Sheets gathered downwind of coal-burning towns carry markedly more sulphur than sheets of "
      "the same species gathered the same year in remote uplands.",
      "Herbarium sheets from the nineteenth century are more likely than modern ones to carry a "
      "full locality on the label.",
      "The species most often collected in the nineteenth century were those easiest to press and "
      "mount.",
      "Sulphur in the atmosphere over Britain fell sharply after coal burning declined."], "A",
     "The proposal requires the sheets themselves to distinguish between places, and same-species, "
     "same-year sheets differing by district according to what was upwind of them is that "
     "distinction. The finding about atmospheric sulphur falling comes from measurements of the "
     "air rather than from any specimen, so it leaves the sheets untested."),

 coe("E7",
     "Seed arriving from the field carries chaff, dust and broken seed, and a cleaner removes them "
     "in stages. A merchant weighed a thousand seeds drawn at random from the same lot after each "
     "stage."
     + table(["Stage of cleaning", "Weight of 1,000 seeds (grams)"],
             [["As received", "27.4"], ["After screening", "31.9"],
              ["After winnowing", "35.6"], ["After gravity table", "36.1"]]),
     "Which choice best describes data from the table that support the claim that winnowing removed "
     "material that screening had left behind?",
     ["The weight of a thousand seeds rose from 31.9 grams to 35.6 grams across the winnowing "
      "stage.",
      "The weight of a thousand seeds was lowest, at 27.4 grams, in the lot as received.",
      "The weight of a thousand seeds rose by only 0.5 grams across the gravity table.",
      "The weight of a thousand seeds rose at every stage of cleaning."], "A",
     "A thousand-seed weight rises as light rubbish is taken out, so a rise across the winnowing "
     "stage in particular shows that stage removing something, and the figures either side of it "
     "give that rise. Reporting that the weight rose at every stage attributes nothing to "
     "winnowing rather than to the other stages."),

 coe("E8",
     "A collector sent to south-west China in the 1900s was instructed to bring back living plants "
     "as well as pressed specimens. His field journal has been used to argue that he chose what to "
     "collect by what he judged would survive the journey rather than by what was botanically "
     "novel.",
     "Which quotation from the journal most effectively supports that argument?",
     ["&ldquo;Passed a slope of the finest new primula I have seen, and took seed only; the roots "
      "would never have kept three months in a mule pannier.&rdquo;",
      "&ldquo;The rain has not stopped for nine days and the presses are all full of mouldering "
      "paper.&rdquo;",
      "&ldquo;This valley holds four species I cannot name from any book I carry.&rdquo;",
      "&ldquo;The headman has lent me two men and a mule for the week, on the usual terms.&rdquo;"],
     "A",
     "The argument is that survival governed his choices, and the entry in which he takes seed "
     "rather than roots because roots would not last the journey states that reasoning outright. "
     "The entry about four unnameable species records novelty without saying what he decided to "
     "collect."),

 coe("E9",
     "A plant now confined to a few sites in the north of England is listed in county floras of the "
     "1850s from parishes where it has not been seen since. A botanist proposes that herbarium "
     "sheets can settle whether the plant has genuinely retreated or was simply misidentified by "
     "the earlier recorders.",
     "Which finding, if true, would most directly support the botanist's proposal?",
     ["Sheets collected in those southern parishes in the 1850s, re-examined today, are correctly "
      "named and carry full locality data.",
      "The county floras of the 1850s were compiled by recorders who rarely travelled outside "
      "their own parishes.",
      "The plant is difficult to distinguish in the field from a commoner relative.",
      "Modern surveys of the northern sites find the plant in smaller numbers each decade."], "A",
     "The proposal is that the sheets can decide between retreat and misidentification, and sheets "
     "from the disputed parishes that prove correctly named and precisely localised do decide it. "
     "The fact that the plant is hard to tell apart in the field states the problem rather than "
     "showing that the sheets can resolve it."),

 # --------------------------------------------------------------- Inferences (6)
 inf("I1",
     "A herbarium sheet records the day a plant was in flower at a named place, and collectors have "
     "been writing that date on labels for two hundred years. Researchers comparing the flowering "
     "dates on old sheets with dates recorded today have found the two sets separated by a fortnight "
     "or more for many species. The comparison works only because the collectors were not thinking "
     "about the question at all: a date written down to identify a specimen carries none of the "
     "expectations that would attach to a date written down to _____",
     ["demonstrate that flowering had shifted.", "distinguish one species from another.",
      "record the locality where the plant grew.", "establish who had collected the specimen."], "A",
     "The passage says the comparison works because the collectors were not thinking about the "
     "question, which is the question of shifting flowering dates, so the contrast is with a date "
     "recorded in order to show a shift. A date written to tell two species apart is not the "
     "expectation the passage has just raised."),

 inf("I2",
     "Jasmine and tuberose give almost nothing to a still. The compounds that carry their scent are "
     "destroyed at the temperature distillation requires, and what survives smells little like the "
     "flower. Perfumers therefore laid the blossoms on trays of purified fat, which absorbs the "
     "scent as the flowers continue to give it off, renewing the flowers daily for weeks before "
     "washing the fat with spirit. The method is laborious and was kept in use for as long as it "
     "was because, for these flowers, it _____",
     ["preserved a scent that heat would have ruined.",
      "produced a larger quantity of oil than distillation.",
      "required less skilled labour than distillation did.",
      "allowed the flowers to be stored before processing."], "A",
     "The passage explains that the scent compounds are destroyed at distillation temperatures, so "
     "the reason for keeping a laborious cold method is that it avoids the heat. The option about "
     "a larger quantity is not supported, since the passage measures the method against fidelity "
     "of scent rather than against volume."),

 inf("I3",
     "Leaves of foxglove gathered from two hillsides may differ several-fold in the strength of the "
     "drug they yield, and the difference cannot be seen or tasted. Before a way of assaying the "
     "strength was adopted, a physician prescribing a dose by weight of leaf was in effect "
     "prescribing an unknown quantity of the active substance. The adoption of an assay changed "
     "what a prescription could mean, because it made the dose _____",
     ["a statement about the drug rather than about the leaf.",
      "cheaper for the patient to obtain from an apothecary.",
      "easier for a physician to write down without error.",
      "less dependent on the season in which leaves were gathered."], "A",
     "The passage contrasts prescribing by weight of leaf, which left the active quantity unknown, "
     "with what an assay makes possible, so the dose comes to specify the drug itself. The option "
     "about cost introduces a matter the passage never raises."),

 inf("I4",
     "Every pure essential oil bends a ray of light passing through it by a fixed amount at a given "
     "temperature, and the instrument that measures this takes a single drop and reads in seconds. "
     "The figure it returns will not name what has been added to a sample, and two different "
     "adulterants may push the reading in opposite directions. A refractometer reading is therefore "
     "best understood as a way of _____",
     ["deciding quickly which samples deserve a fuller examination.",
      "identifying precisely which substance has been added to a sample.",
      "measuring the proportion of adulterant present in a sample.",
      "confirming that a sample has not been adulterated at all."], "A",
     "The passage says the reading is fast and takes one drop but names nothing and can be pushed "
     "either way, which fits a first sort rather than a verdict. The option about identifying the "
     "added substance is ruled out by the sentence saying the figure will not name what has been "
     "added."),

 inf("I5",
     "Plants from high mountains die in ordinary garden soil more often from wet than from cold. In "
     "their own ground they spend the winter under snow, dry at the neck, with meltwater draining "
     "instantly away through broken rock. A bed built for them is therefore made mostly of stone "
     "chippings with very little soil among them, an arrangement that looks starved and is in fact "
     "chosen because it _____",
     ["lets water leave the root as fast as it arrives.",
      "holds warmth around the root through the winter.",
      "supplies the minerals such plants take from rock.",
      "prevents the plants from growing beyond their natural size."], "A",
     "The passage identifies wet rather than cold as the killer and describes meltwater draining "
     "instantly through broken rock, so a chippings bed is chosen for drainage. The warmth option "
     "addresses cold, which the first sentence sets aside as the lesser danger."),

 inf("I6",
     "A weevil laid in a bean in the field completes its development in the store, and a single "
     "generation can be followed by several more among seed that never leaves the sack. Cold slows "
     "the insects long before it slows the seed, and at the temperature a long-term store is held "
     "the beetles do not breed at all. A store built to keep seed alive for decades therefore "
     "controls its insects _____",
     ["as a by-product of the conditions it maintains anyway.",
      "by fumigating each sack before it is placed on the shelf.",
      "at the cost of shortening the life of the seed itself.",
      "only in the first season after the seed is taken in."], "A",
     "The passage says the beetles stop breeding at the temperature the store already holds for "
     "the seed's sake, so no separate measure is needed. The fumigation option introduces a "
     "treatment the passage never mentions."),

 # --------------------------------------------------------------- Boundaries (12)
 bnd("B1",
     "The Society of Apothecaries leased four acres beside the Thames at Chelsea in 1673 and "
     "planted them for the instruction of its _____ the ground is still a garden today.",
     ["apprentices;", "apprentices,", "apprentices", "apprentices and"], "A",
     "Two complete sentences stand on either side of the break, one about the leasing and planting "
     "and one about the ground today, so they need a mark that can join independent clauses. "
     "Placing only a comma between them runs the two sentences together."),

 bnd("B2",
     "A pill mass was rolled into a rope on a flat slab of glazed earthenware and then cut on a "
     "brass machine with parallel grooves, which divided the rope into equal _____ each of them "
     "then rounded between the palms.",
     ["lengths,", "lengths;", "lengths.", "lengths and"], "A",
     "What follows the break has no subject and no finite verb; it is a phrase describing the "
     "lengths, so it attaches to the main clause with a comma. A semicolon would announce a second "
     "independent clause that never arrives."),

 bnd("B3",
     "Marble absorbs oils and stains, glass chips under a hard drug, and porcelain, which resists "
     "both, became the usual material for a dispensing _____ was less easily broken.",
     ["mortar. Iron", "mortar, iron", "mortar; and iron", "mortar and iron"], "A",
     "The words after the break form a complete sentence of their own about iron, and the words "
     "before it form another about porcelain, so a full stop separates them cleanly. Joining them "
     "with only a comma produces a run-on."),

 bnd("B4",
     "The shoot that will bear the fruit is called the _____ the root it is joined to is called "
     "the stock, and the two may come from quite different plants.",
     ["scion;", "scion,", "scion", "scion and"], "A",
     "The clause naming the scion and the clause naming the stock are each complete, and a "
     "semicolon holds them together as the closely paired definitions they are. A comma alone "
     "cannot join two independent clauses."),

 bnd("B5",
     "Vapour leaving the still head passes into a copper pipe coiled inside a tub of running "
     "_____ by the time it reaches the foot of the coil it has condensed to a liquid.",
     ["water;", "water,", "water", "water but"], "A",
     "A complete sentence about the vapour entering the pipe is followed by another complete "
     "sentence about what has happened by the foot of the coil, so a semicolon is required. A "
     "comma between two independent clauses is a comma splice."),

 bnd("B6",
     "Lavender cut before the flowers open yields little oil, and lavender cut after they have "
     "faded yields oil of a coarser _____ growers watch the field daily through the fortnight in "
     "between.",
     ["character;", "character,", "character", "character and which"], "A",
     "The material before the break is a complete sentence with two coordinated clauses, and the "
     "material after it is a complete sentence about the growers, so the two need a semicolon. "
     "Adding a comma alone leaves the second sentence spliced to the first."),

 bnd("B7",
     "Sheets of a single genus are gathered into a stiff folder, the folders are stacked in "
     "_____ and the fascicles are shelved in the order the classification prescribes.",
     ["fascicles,", "fascicles;", "fascicles.", "fascicles"], "A",
     "Three clauses are strung together in a single sentence joined by <em>and</em> before the "
     "last, so the break before that conjunction takes a comma. A semicolon there would be "
     "inconsistent with the comma used earlier in the same series."),

 bnd("B8",
     "Beetles that eat dried plant tissue can empty a cabinet in a season, so every incoming sheet "
     "is sealed in a bag and held at twenty degrees below _____ for four days before it goes to "
     "the shelf.",
     ["freezing", "freezing,", "freezing;", "freezing:"], "A",
     "The phrase naming the temperature runs straight into the phrase naming the period, and no "
     "punctuation belongs between a modifier and the phrase it modifies. Inserting a comma "
     "separates elements that form one continuous description."),

 bnd("B9",
     "Screening takes out what is larger or smaller than the seed, winnowing takes out what is "
     "lighter, and a gravity table takes out what is the same size and the same weight but less "
     "_____ each machine answers a different question about the sample.",
     ["dense;", "dense,", "dense", "dense but"], "A",
     "A three-part series ends the first sentence, and a second complete sentence about the "
     "machines follows, so the two sentences must be divided by a semicolon or a full stop. A "
     "comma would splice them, and the sentence already uses commas within its series."),

 bnd("B10",
     "Warm air dries seed quickly but can damage the embryo, so a vacuum drier lowers the pressure "
     "instead, letting water leave at a temperature the seed can _____ tolerate for the many hours "
     "the process takes.",
     ["safely", "safely,", "safely;", "safely:"], "A",
     "The adverb belongs directly to the verb it modifies, and nothing should stand between them. "
     "A comma at that point cuts the verb phrase in half."),

 bnd("B11",
     "A pharmacopoeia monograph fixes what a preparation must contain and how it is to be tested "
     "for _____ it does not tell a dispenser when the preparation should be used.",
     ["strength;", "strength,", "strength", "strength which"], "A",
     "Both halves are complete sentences, one about what the monograph fixes and one about what it "
     "does not do, and the contrast between them is best carried by a semicolon. A comma alone "
     "joins two independent clauses incorrectly."),

 bnd("B12",
     "Heat from a brick flue running under the floor of the orangery kept the tubs of citrus above "
     "freezing through the _____ the smoke was carried out through the far wall.",
     ["winter, and", "winter and", "winter,", "winter"], "A",
     "Two independent clauses are joined here, so the coordinating conjunction needs a comma "
     "before it. Dropping the comma before <em>and</em> between two full clauses leaves the join "
     "unmarked."),

 # ------------------------------------------------- Form, Structure, and Sense (9)
 fss("F1",
     "The small weights of an apothecary's set _____ kept in a fitted case, and the smallest of "
     "them are lifted with forceps so that the warmth and grease of a finger never reach the pan.",
     ["are", "is", "was", "has been"], "A",
     "The subject is the plural <em>weights</em>, and the phrase beginning <em>of an "
     "apothecary's set</em> does not change that, so the verb must be plural and present to match "
     "the present-tense verb later in the sentence. The singular form agrees with the nearest noun "
     "instead of with the true subject."),

 fss("F2",
     "A label written in ink on wood lasts a season, while one struck into lead or zinc _____ the "
     "life of the plant it names, which is why the older gardens ordered them by the hundred.",
     ["outlasts", "outlasting", "to outlast", "having outlasted"], "A",
     "The clause introduced by <em>while</em> needs a finite verb of its own to carry the "
     "contrast, and the present tense matches <em>lasts</em> in the first clause. The participial "
     "form leaves that clause without a main verb."),

 fss("F3",
     "Crude turpentine tapped from a pine is a thick resin; distilling it drives off the volatile "
     "oil and leaves the hard rosin behind, and the two products _____ sold into quite different "
     "trades.",
     ["are", "is", "was being", "being"], "A",
     "The subject <em>the two products</em> is plural, and the sentence is describing a standing "
     "practice, so the plural present verb is required. The participle without a helping verb "
     "leaves the final clause incomplete."),

 fss("F4",
     "The water that comes over with the oil is not a waste product: it holds a little of the same "
     "scent in solution, and bottling it _____ a saleable article out of what a distiller once "
     "poured on the ground.",
     ["makes", "make", "making", "to make"], "A",
     "The subject of the final clause is the gerund phrase <em>bottling it</em>, which is "
     "singular, so the verb takes the singular present form. The plural verb would agree with "
     "nothing in the sentence."),

 fss("F5",
     "Corrugated aluminium ventilators are set between the layers of a press so that warm air can "
     "run through the stack; without them the blotters nearest the middle _____ damp for days.",
     ["stay", "stays", "staying", "to stay"], "A",
     "The subject is the plural <em>blotters</em>, and the clause needs a finite verb to complete "
     "it, so the plural present form is correct. The singular form disagrees with the plural "
     "subject."),

 fss("F6",
     "Each collector keeps a single running series of numbers across a whole career, so a specimen "
     "labelled with that collector's name and a number _____ be matched to a field notebook "
     "entry decades afterwards.",
     ["can", "canned", "could have", "having"], "A",
     "The clause needs a modal followed by the bare infinitive <em>be</em>, and the present modal "
     "matches the present tense of <em>keeps</em> earlier in the sentence. The perfect form would "
     "place the matching in a past that the sentence does not establish."),

 fss("F7",
     "A layer of bark or straw spread over a bed does not feed the soil beneath it; what it does "
     "_____ slow the loss of water from the surface through a dry summer.",
     ["is", "are", "being", "to be"], "A",
     "The subject is the noun clause <em>what it does</em>, which takes a singular verb, and the "
     "sentence needs a finite verb to complete the contrast. The plural form disagrees with that "
     "singular subject."),

 fss("F8",
     "The coats of many legume seeds are impermeable when ripe, and a nurseryman who wants an even "
     "stand _____ them with sandpaper or hot water before sowing.",
     ["scratches", "scratching", "to scratch", "having scratched"], "A",
     "The relative clause <em>who wants an even stand</em> ends before the blank, leaving the "
     "singular subject <em>a nurseryman</em> in need of a main verb in the present tense. A "
     "participle leaves the second half of the sentence with no finite verb at all."),

 fss("F9",
     "A simple is a preparation made from one plant only, and a syrup is a preparation carried in "
     "sugar; neither term _____ anything about how strong the medicine is.",
     ["says", "say", "saying", "to say"], "A",
     "The subject <em>neither term</em> is singular, so the verb takes the singular present form. "
     "The plural verb agrees with the plural noun beside it rather than with the singular "
     "determiner that governs the subject."),

 # -------------------------------------------------------------- Transitions (9)
 trn("R1",
     "The lightest components of an essential oil are terpenes, which boil low and come over first. "
     "The compounds that carry most of the characteristic odour are heavier and boil higher, and "
     "they arrive later in the run. _____ a distillate collected only from the beginning of a run "
     "smells thin, however clean the material that went into the still.",
     ["Consequently,", "Nevertheless,", "By contrast,", "For instance,"], "A",
     "The sentence states a result that follows from the two facts before it: if the odour-bearing "
     "compounds arrive late, an early cut must lack them. A contrast marker would signal that the "
     "sentence opposes what precedes it, which it does not."),

 trn("R2",
     "Distillers divide a run into three portions and judge each separately. The first and last "
     "are set aside or redistilled, and only the middle portion is bottled as it stands. _____ the "
     "three portions of a single run may be sold at three different prices.",
     ["As a result,", "Even so,", "In contrast,", "Similarly,"], "A",
     "The different prices follow directly from the practice of treating the three portions "
     "differently, so the sentence draws a consequence. A concessive marker would suggest the "
     "prices hold in spite of the practice, which reverses the relation."),

 trn("R3",
     "Steam ruins the oil in a citrus peel, which is why citrus is one of the few crops whose oil "
     "is not distilled at all. The peel is instead pricked and squeezed, and the oil runs out cold. "
     "_____ a cold-pressed lemon oil contains waxes and pigments that no distilled oil carries.",
     ["Because of this,", "In spite of this,", "Meanwhile,", "In other words,"], "A",
     "The presence of waxes and pigments is a consequence of pressing rather than distilling, "
     "since nothing is left behind in a still. The restatement marker would claim the sentence "
     "says the same thing again, but it adds a new fact."),

 trn("R4",
     "Seeds rich in oil go stale in the way that a nut goes stale, and the process runs faster in "
     "warm damp air. Cold dry storage slows it, as it slows everything else that shortens a seed's "
     "life. _____ an oily seed kept under the same conditions as a starchy one will still fail "
     "first.",
     ["Nonetheless,", "Therefore,", "For example,", "In addition,"], "A",
     "The sentence concedes that the remedy just described does not equalise the two kinds of "
     "seed, so it stands against the expectation the previous sentence raises. A marker of "
     "consequence would suggest the earlier failure follows from cold dry storage, which is the "
     "opposite of what is meant."),

 trn("R5",
     "A trained nose can tell a good oil from a poor one and will often detect an adulterant that "
     "an instrument misses. It cannot say what the adulterant is, or how much of it is present. "
     "_____ a gas chromatograph separates a sample into its components and reports the size of "
     "each.",
     ["A chromatograph, by contrast,", "A chromatograph, likewise,",
      "A chromatograph, for instance,", "A chromatograph, in short,"], "A",
     "The sentence sets the instrument's ability to name and quantify components against the "
     "nose's inability to do either, so the relation is one of opposition. A marker of similarity "
     "would claim the chromatograph shares the limitation just described."),

 trn("R6",
     "A specimen fixed to its sheet with glue cannot be lifted for dissection without damage. One "
     "held down by narrow paper straps can be released and replaced as often as a worker needs. "
     "_____ many herbaria that once glued everything now strap the specimens they expect to be "
     "studied most.",
     ["Accordingly,", "However,", "Beforehand,", "Admittedly,"], "A",
     "The change in practice follows from the advantage of straps that the previous sentence "
     "states, so the sentence draws a consequence. A contrastive marker would present the change "
     "as running against that advantage."),

 trn("R7",
     "Arranging a herbarium alphabetically by genus lets anyone find a name without knowing any "
     "botany. Arranging it by classification puts related plants side by side, so that a worker "
     "comparing a doubtful specimen with its relatives finds them all in one bay. _____ the "
     "alphabetical arrangement serves the visitor and the systematic one serves the specialist.",
     ["In short,", "Even so,", "By comparison,", "Afterwards,"], "A",
     "The sentence condenses the two arrangements just described into a single summarising "
     "statement, which is what a marker of summary signals. A concessive marker would set the "
     "sentence against the preceding material rather than gathering it up."),

 trn("R8",
     "A closure that a child cannot work must be one that requires two motions at once, since a "
     "small hand can supply force but not co-ordination. The same two motions defeat a good many "
     "arthritic adults. _____ the design that protects one household most reliably is the design "
     "that some households cannot use at all.",
     ["Thus,", "Otherwise,", "Instead,", "Previously,"], "A",
     "The sentence states the outcome that follows from the two preceding observations taken "
     "together, so a marker of consequence is required. The alternative marker would introduce "
     "something done in place of the design, which is not what the sentence does."),

 trn("R9",
     "A tender shrub moved straight from a heated house to open ground in April is often killed by "
     "a wind that would not have troubled it in June. Gardeners therefore stand the pots outside "
     "for a few hours a day, extending the period over a fortnight before planting. _____ the "
     "plant's tissues harden while it is still able to be brought back in.",
     ["In this way,", "Even so,", "By contrast,", "Beforehand,"], "A",
     "The sentence explains how the practice just described achieves its effect, which is what a "
     "marker of means signals. A contrastive marker would set the hardening against the practice "
     "rather than presenting it as its result."),

 # ------------------------------------------------------- Rhetorical Synthesis (9)
 syn("S1",
     ["Layering roots a shoot while it is still attached to the parent plant.",
      "A shoot is bent to the ground, wounded on its underside and pegged under soil.",
      "The parent continues to supply the shoot with water until roots form.",
      "A cutting, by contrast, is severed first and must survive on its own reserves.",
      "Layering is slower than taking cuttings but succeeds with species that root poorly."],
     "explain to an audience unfamiliar with propagation why layering succeeds with difficult "
     "species.",
     ["Because a layered shoot stays attached to its parent and goes on being supplied with water "
      "while it roots, it is not thrown onto its own reserves as a severed cutting is, which is "
      "why layering succeeds with species that root poorly.",
      "Layering is slower than taking cuttings, and a shoot is bent to the ground, wounded on its "
      "underside and pegged under soil.",
      "A cutting is severed first and must survive on its own reserves, while a layered shoot is "
      "bent to the ground and pegged under soil.",
      "Species that root poorly are propagated by layering, a method in which a shoot is wounded "
      "on its underside before being pegged down."], "A",
     "The goal asks why the method works with difficult species, and only the choice that links "
     "the continuing water supply from the parent to the absence of any demand on the shoot's own "
     "reserves supplies that reason. The choice pairing the slowness of layering with the "
     "mechanics of pegging a shoot down reports two notes without connecting either to success."),

 syn("S2",
     ["A camera lucida is a prism on a stand that superimposes a view of an object on the paper "
      "below.",
      "The draughtsman sees the object and the pencil point in the same visual field.",
      "Outlines can be traced at a fixed scale without measuring.",
      "The device does not record anything by itself; the drawing is still made by hand.",
      "Botanical artists used it for the outline and then worked up detail by eye."],
     "emphasise what the device did and did not do for a botanical artist.",
     ["The camera lucida let a botanical artist trace an outline at a fixed scale without "
      "measuring, because object and pencil point appeared in the same visual field; it recorded "
      "nothing by itself, and the detail was still worked up by eye.",
      "The camera lucida is a prism on a stand, and botanical artists used it to trace outlines "
      "before working up the detail by eye.",
      "Because the draughtsman sees the object and the pencil point in the same visual field, "
      "outlines can be traced at a fixed scale without measuring.",
      "Botanical artists worked up detail by eye, and the camera lucida did not record anything by "
      "itself."], "A",
     "The goal is a two-sided statement, and only the choice that both names the tracing the "
     "device made possible and states that it recorded nothing on its own covers both sides. The "
     "choice about the shared visual field gives only the enabling half and never says what the "
     "device failed to do."),

 syn("S3",
     ["A garden planted only with showy double-flowered varieties supports few insects.",
      "Double flowers have extra petals in place of the parts that make pollen and nectar.",
      "Single-flowered forms of the same species carry both.",
      "A survey of one garden found four times as many bee visits to single-flowered beds.",
      "Many gardeners now keep a proportion of single-flowered forms for this reason."],
     "explain to a general audience why double flowers support fewer insects.",
     ["Double flowers carry extra petals in place of the parts that produce pollen and nectar, so "
      "they offer insects nothing to collect; one garden survey counted four times as many bee "
      "visits to beds of single-flowered forms, which retain both.",
      "A survey of one garden found four times as many bee visits to single-flowered beds, and "
      "many gardeners now keep a proportion of single-flowered forms.",
      "Gardens planted only with showy double-flowered varieties support few insects, and many "
      "gardeners now keep a proportion of single-flowered forms.",
      "Single-flowered forms of a species carry both pollen and nectar, and double flowers have "
      "extra petals."], "A",
     "The goal asks for the reason, and only the choice that says the extra petals replace the "
     "pollen- and nectar-bearing parts explains what the insects are missing. The choice pairing "
     "the survey with the gardeners' response reports the effect and the reaction without giving "
     "the cause at all."),

 syn("S4",
     ["Clary sage yields an oil containing sclareol.",
      "Sclareol can be converted into a substance with the fixing properties of ambergris.",
      "Ambergris comes from sperm whales and was scarce and costly.",
      "A fixative slows the evaporation of the lighter parts of a perfume.",
      "Clary sage is grown as a field crop in France, Russia and the United States."],
     "explain to an audience unfamiliar with perfumery why clary sage became a field crop.",
     ["Clary sage is grown on a field scale because its oil contains sclareol, which can be "
      "converted into a substitute for the scarce and costly whale product ambergris, a fixative "
      "that slows the evaporation of a perfume's lighter parts.",
      "Clary sage is grown as a field crop in France, Russia and the United States, and its oil "
      "contains sclareol.",
      "Ambergris comes from sperm whales and was scarce and costly, and a fixative slows the "
      "evaporation of the lighter parts of a perfume.",
      "Sclareol can be converted into a substance with the fixing properties of ambergris, which "
      "comes from sperm whales."], "A",
     "The goal asks why the crop is grown at scale, and only the choice that runs from sclareol "
     "through the ambergris substitute to what a fixative does supplies that chain. The choice "
     "naming the growing countries alongside the oil's content states the fact to be explained "
     "without explaining it."),

 syn("S5",
     ["A herbarium lends specimens to researchers at other institutions.",
      "Loans travel between institutions rather than to individuals.",
      "The borrowing institution takes responsibility for the sheets while they are held.",
      "A specialist revising a group may borrow several hundred sheets at once.",
      "Sheets returned from loan often carry a new determination slip added by the specialist."],
     "explain to a general audience how a loan benefits the lending herbarium.",
     ["A specialist revising a group may borrow several hundred sheets at once and often returns "
      "them with a new determination slip attached, so the lending herbarium gets its material "
      "named by an expert it does not employ.",
      "Loans travel between institutions rather than to individuals, and the borrowing institution "
      "takes responsibility for the sheets while they are held.",
      "A herbarium lends specimens to researchers at other institutions, and a specialist may "
      "borrow several hundred sheets at once.",
      "Sheets returned from loan often carry a new determination slip added by the specialist, and "
      "loans travel between institutions rather than to individuals."], "A",
     "The goal concerns what the lender gains, and only the choice that connects the returned "
     "determination slips to expert naming the lender did not pay for states a benefit. The choice "
     "about institutional responsibility describes how loans are governed rather than what the "
     "lender gets out of them."),

 syn("S6",
     ["Loose seeds, fallen petals and broken fragments cannot be glued to a sheet.",
      "A small paper envelope is fixed to a corner of the sheet to hold them.",
      "The envelope carries the same number as the specimen.",
      "Material from the envelope can be examined under a microscope and returned.",
      "Seeds from such envelopes have been germinated a century after collection."],
     "explain to a general audience why the envelope is worth the trouble of attaching.",
     ["The envelope keeps loose seeds and fragments with the specimen that produced them, and "
      "because material can be taken out, examined under a microscope and put back, seeds from "
      "such envelopes have even been germinated a century after collection.",
      "A small paper envelope is fixed to a corner of the sheet and carries the same number as the "
      "specimen.",
      "Loose seeds, fallen petals and broken fragments cannot be glued to a sheet, so a small "
      "paper envelope is fixed to a corner.",
      "Material from the envelope can be examined under a microscope and returned, and the "
      "envelope carries the same number as the specimen."], "A",
     "The goal asks what makes the envelope worth attaching, and only the choice that names both "
     "the repeated examination it permits and the century-old germination shows the return on the "
     "trouble. The choice describing what cannot be glued explains why an envelope is used at all "
     "without saying what is gained by it."),

 syn("S7",
     ["A wild-collected seed lot is recorded with the exact place, altitude and habitat of "
      "collection.",
      "Two lots of the same species from different valleys may differ in cold tolerance.",
      "A lot without collection data cannot be matched to a site for reintroduction.",
      "Provenance data are recorded at the moment of collection and cannot be recovered later.",
      "Some older collections in store carry only a country name."],
     "explain to a general audience why provenance data must be recorded in the field.",
     ["Provenance data cannot be recovered once the collector has left the site, and without the "
      "exact place, altitude and habitat a lot cannot be matched to a site for reintroduction &mdash; "
      "which matters because two lots of one species from different valleys may differ in cold "
      "tolerance.",
      "Some older collections in store carry only a country name, and a wild-collected seed lot is "
      "recorded with the exact place, altitude and habitat of collection.",
      "Two lots of the same species from different valleys may differ in cold tolerance, and a lot "
      "without collection data cannot be matched to a site for reintroduction.",
      "A wild-collected seed lot is recorded with the exact place, altitude and habitat of "
      "collection, and provenance data are recorded at the moment of collection."], "A",
     "The goal asks why the recording must happen in the field, and only the choice that states "
     "the data cannot be recovered afterwards answers the question of timing. The choice about "
     "valleys and reintroduction explains why the data matter but says nothing about when they "
     "have to be taken."),

 syn("S8",
     ["Medical students in the sixteenth century learned drugs from written descriptions.",
      "A description could be matched to more than one plant growing in the field.",
      "University physic gardens grew named plants in labelled beds for students to see.",
      "A demonstrator walked the beds with the class and named each plant aloud.",
      "Students who had walked the beds could recognise the plants when they later prescribed "
      "them."],
     "explain to a general audience what the garden added to the students' textbooks.",
     ["Because a written description could fit more than one plant growing in the field, the "
      "labelled beds and the demonstrator who named each plant aloud gave students a direct "
      "acquaintance with the drug plants that they could carry into practice.",
      "University physic gardens grew named plants in labelled beds, and a demonstrator walked the "
      "beds with the class and named each plant aloud.",
      "Medical students in the sixteenth century learned drugs from written descriptions, and "
      "students who had walked the beds could recognise the plants later.",
      "A description could be matched to more than one plant growing in the field, and students "
      "learned drugs from written descriptions."], "A",
     "The goal is what the garden supplied that books did not, and only the choice that names the "
     "ambiguity of a written description and then the direct acquaintance the beds provided draws "
     "that contrast. The choice describing the beds and the demonstrator reports the garden's "
     "arrangements without saying what they remedied."),

 syn("S9",
     ["Prescriptions were written in abbreviated Latin until well into the twentieth century.",
      "The abbreviations covered the drug, the quantity, the form and the timing of a dose.",
      "A dispenser anywhere in Europe could read a prescription written in another country.",
      "A patient reading the same prescription could not.",
      "Some of the abbreviations were similar enough to be confused with one another."],
     "present a balanced account of the abbreviated Latin used on prescriptions.",
     ["The abbreviations gave the drug, the quantity, the form and the timing compactly enough "
      "that a dispenser anywhere in Europe could read a prescription written abroad, though the "
      "patient could not and some of the abbreviations were similar enough to be confused.",
      "Prescriptions were written in abbreviated Latin until well into the twentieth century, and "
      "the abbreviations covered the drug, the quantity, the form and the timing of a dose.",
      "Some of the abbreviations were similar enough to be confused with one another, and a "
      "patient reading a prescription could not understand it.",
      "A dispenser anywhere in Europe could read a prescription written in another country, "
      "because prescriptions were written in abbreviated Latin."], "A",
     "A balanced account needs both the advantage and the drawbacks, and only the choice that "
     "pairs the cross-border legibility with the patient's exclusion and the risk of confusion "
     "gives both. The choice listing only the similar abbreviations and the patient's exclusion "
     "presents the drawbacks alone."),
]
