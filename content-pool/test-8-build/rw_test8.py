#!/usr/bin/env python3
"""
Reading & Writing authored for Test 8.

The transcribed pool is spent — 19 items survive Tests 3-7 — so the rest of
Test 8's 81 questions are written here. Weighted to the writing domains, which
is both where supply was always thinnest and where correctness is decidable:
a Boundaries or Form/Structure item is right or wrong by a stated convention,
the same property that makes sympy verification work for Math. Reading items
carry a `why` recording the reasoning that produced the key, because a key
without a reason is exactly what went wrong in Test 5 (6 wrong answers in 81).

Passages are original. Topics are deliberately spread across science, history,
art and social science so no two items read as siblings.
"""

SOURCE = "AUTHORED-T8"
MODULE = "RW"


def wic(num, passage, choices, answer, why):
    return dict(num=num, skill="Words in Context", passage=passage,
                stem="Which choice completes the text with the most logical and precise word or phrase?",
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


QUESTIONS = [
 # ---------------------------------------------------- Words in Context (15)
 wic("W1", "Marine biologist Ayanna Osei was initially _____ about the claim that octopuses use "
           "discarded coconut shells as portable shelters; only after watching hours of her own "
           "footage did she accept it.",
     ["adamant", "sceptical", "indifferent", "informed"], "B",
     "'Only after watching hours of footage did she accept it' means she doubted it first. "
     "'Indifferent' would mean she did not care, which the effort contradicts."),
 wic("W2", "Rather than confining herself to a single medium, the sculptor Ruth Asawa worked in "
           "wire, clay and paper with equal _____, moving between them throughout her career.",
     ["reluctance", "facility", "obscurity", "restraint"], "B",
     "'With equal ___' plus 'moving between them' calls for a word meaning skill or ease. "
     "'Reluctance' and 'restraint' both contradict the range being praised."),
 wic("W3", "The archive's holdings are so _____ that a researcher can spend a week there and "
           "examine only a fraction of the material on a single decade.",
     ["fragile", "disorganised", "extensive", "specialised"], "C",
     "The consequence given — a week yields only a fraction — measures size, not condition or "
     "arrangement, so 'extensive' is what the sentence supports."),
 wic("W4", "Because the two research teams published within weeks of each other, the discovery "
           "is now conventionally _____ to both.",
     ["attributed", "confined", "opposed", "referred"], "A",
     "Credit is 'attributed to' someone. 'Referred' needs a different preposition, and the "
     "other two reverse the meaning."),
 wic("W5", "Far from being a _____ record of what the painter saw, the sketchbook is full of "
           "revisions, abandoned starts and figures redrawn three or four times.",
     ["faithful", "hurried", "detailed", "private"], "A",
     "'Far from being ___' must be contradicted by what follows; revisions and abandoned starts "
     "contradict faithfulness to what was seen, not hurry or privacy."),
 wic("W6", "The committee's report was praised for its _____: it set out the evidence for each "
           "recommendation without overstating what the data could show.",
     ["brevity", "candour", "novelty", "urgency"], "B",
     "Not overstating the evidence is honesty about limits. Brevity is about length, which the "
     "sentence never mentions."),
 wic("W7", "Although the technique was developed for restoring frescoes, conservators soon found "
           "it _____ to textiles as well.",
     ["applicable", "comparable", "preferable", "susceptible"], "A",
     "'Found it ___ to textiles' means it could be used on them. 'Comparable to' would compare "
     "the technique with textiles, which makes no sense."),
 wic("W8", "The novel's structure is deliberately _____, doubling back on events the reader has "
           "already been shown and retelling them from a second vantage point.",
     ["linear", "recursive", "abrupt", "conventional"], "B",
     "Doubling back and retelling is recursion. 'Linear' and 'conventional' are the opposite of "
     "what is described."),
 wic("W9", "Early attempts to cultivate the orchid outside its native range were uniformly "
           "_____, and it was fifty years before a grower succeeded.",
     ["profitable", "unsuccessful", "controversial", "expensive"], "B",
     "'It was fifty years before a grower succeeded' tells us the earlier attempts failed."),
 wic("W10", "The mayor's proposal was criticised as _____, addressing the symptoms of "
            "overcrowding while leaving its causes untouched.",
     ["superficial", "costly", "premature", "unpopular"], "A",
     "Treating symptoms and not causes is the definition of a superficial remedy; the other "
     "three name faults the sentence does not describe."),
 wic("W11", "Historians once dismissed the diaries as _____, but chemical analysis of the ink "
            "has since confirmed that they date from the period they describe.",
     ["derivative", "fraudulent", "trivial", "incomplete"], "B",
     "Dating the ink to the right period rebuts a charge of forgery specifically, not of "
     "triviality or incompleteness."),
 wic("W12", "The engineer's design is admired less for its elegance than for its _____: it has "
            "run for thirty years with almost no maintenance.",
     ["ingenuity", "durability", "simplicity", "economy"], "B",
     "Thirty years with almost no maintenance is lasting well. Simplicity and economy are not "
     "what the evidence given measures."),
 wic("W13", "As used in the text, the word &ldquo;register&rdquo; most nearly means",
     None, None, None),  # replaced below
 wic("W14", "Grasses colonised the plain so quickly that within two decades they had all but "
            "_____ the shrubs that once dominated it.",
     ["sheltered", "supplanted", "resembled", "preserved"], "B",
     "'All but ___ the shrubs that once dominated' describes replacement; the other options do "
     "not account for the shrubs' loss of dominance."),
 wic("W15", "The theory remains _____ among specialists: three recent papers endorse it, and "
            "three others argue it cannot be reconciled with the fossil record.",
     ["settled", "contested", "obscure", "outdated"], "B",
     "An even split between endorsement and rejection is a live dispute, not a settled or "
     "obscure question."),

 # --------------------------------------- Text Structure and Purpose (6)
 dict(num="S1", skill="Text Structure and Purpose",
      passage="In 1901 the physicist Hertha Ayrton became the first woman to read her own paper "
              "before the Institution of Electrical Engineers. <u>The paper concerned the hissing "
              "of electric arcs, a nuisance that had defeated better-funded laboratories for "
              "years.</u> Ayrton traced the noise to a chemical reaction at the carbon rods and "
              "showed that reshaping them silenced it.",
      stem="Which choice best describes the function of the underlined sentence in the text as a whole?",
      choices=["It concedes a limitation in the research the text goes on to describe.",
               "It establishes the significance of the problem Ayrton is then shown to have solved.",
               "It contrasts Ayrton's methods with those of her better-funded contemporaries.",
               "It explains why Ayrton was invited to address the Institution."],
      answer="B",
      why="The sentence says the problem had defeated well-resourced labs for years, which sets "
          "up the final sentence in which Ayrton solves it. It never says her methods differed, "
          "nor why she was invited."),
 dict(num="S2", skill="Text Structure and Purpose",
      passage="Most accounts of the printing revolution begin with Gutenberg. Yet movable type "
              "had been in use in Korea for two centuries before him, cast in bronze rather than "
              "the lead alloy Gutenberg favoured. What Europe added was not the idea of movable "
              "type but a metallurgy cheap enough to make it disposable.",
      stem="Which choice best states the main purpose of the text?",
      choices=["To argue that Gutenberg's contribution has been overstated by historians.",
               "To describe the metallurgical differences between Korean and European type.",
               "To correct a common account by specifying what was actually new in Europe.",
               "To trace the spread of printing from Korea to Europe."],
      answer="C",
      why="The text grants that Korean type came first, then names precisely what Europe "
          "contributed. It does not claim Gutenberg is overrated, nor trace any transmission "
          "between the two."),
 dict(num="S3", skill="Text Structure and Purpose",
      passage="<u>Lichens are not single organisms.</u> Each is a partnership between a fungus, "
              "which supplies structure and moisture, and an alga or cyanobacterium, which "
              "supplies sugars through photosynthesis. Neither partner can occupy bare rock alone.",
      stem="Which choice best describes the function of the underlined sentence?",
      choices=["It states the claim that the rest of the text explains.",
               "It raises an objection that the rest of the text answers.",
               "It offers an example of a phenomenon defined later.",
               "It qualifies a generalisation made elsewhere in the text."],
      answer="A",
      why="The sentence asserts that lichens are not single organisms, and the following "
          "sentences explain the partnership that makes this so. Nothing in the text objects to "
          "it or qualifies it."),
 dict(num="S4", skill="Text Structure and Purpose",
      passage="The composer Florence Price sent her scores to conductors who never replied. She "
              "kept composing anyway, filling notebooks that stayed in a summer house outside "
              "Chicago for decades. In 2009 the house was being renovated when the new owners "
              "found the manuscripts stacked in a room they had assumed was empty.",
      stem="Which choice best describes the overall structure of the text?",
      choices=["It poses a question about Price's career and then answers it.",
               "It describes a setback, notes a response to it, and reports a later discovery.",
               "It compares Price's reception during her life with her reputation today.",
               "It lists the works Price completed in chronological order."],
      answer="B",
      why="Three moves in order: conductors ignore her, she keeps composing, the manuscripts are "
          "found in 2009. The text never states her present reputation, so no comparison is made."),
 dict(num="S5", skill="Text Structure and Purpose",
      passage="Ordinary glass is a liquid that has been cooled too quickly to crystallise. Its "
              "molecules are frozen in the disordered arrangement they held while molten. "
              "<u>This is why a pane of glass has no grain and can be cut in any direction.</u>",
      stem="Which choice best describes the function of the underlined sentence?",
      choices=["It introduces a distinction the text then develops.",
               "It draws a practical consequence from the explanation given.",
               "It provides evidence contradicting the preceding claim.",
               "It defines a term used earlier in the text."],
      answer="B",
      why="Having explained the disordered molecular arrangement, the sentence draws out what "
          "follows from it for cutting glass. It supplies no evidence and defines nothing."),
 dict(num="S6", skill="Text Structure and Purpose",
      passage="A team surveying the seafloor off Norway expected to map sediment. What the sonar "
              "returned instead were parallel ridges, regular as ploughed furrows, running for "
              "kilometres. They were the scours left by icebergs that had dragged along the "
              "bottom as the last ice sheet collapsed.",
      stem="Which choice best states the main purpose of the text?",
      choices=["To explain how sonar surveys of the seafloor are conducted.",
               "To recount an unexpected finding and identify its cause.",
               "To argue that the last ice sheet collapsed faster than believed.",
               "To compare seafloor sediment with glacial deposits on land."],
      answer="B",
      why="The text sets up an expectation, reports what was found instead, and explains what "
          "made the ridges. It makes no argument about the speed of collapse."),

 # ------------------------------------------ Central Ideas and Details (6)
 dict(num="C1", skill="Central Ideas and Details",
      passage="Bowerbirds build elaborate structures from twigs and decorate them with objects "
              "sorted by colour. The bower is not a nest; no eggs are laid in it, and it is "
              "abandoned once the breeding season ends. Females inspect several bowers before "
              "choosing, and males whose decorations are removed by researchers are chosen less "
              "often.",
      stem="Which choice best states the main idea of the text?",
      choices=["Bowerbirds build nests that are unusually elaborate for their size.",
               "The bower functions in mate choice rather than in raising young.",
               "Female bowerbirds prefer bowers decorated in a single colour.",
               "Researchers have disrupted bowerbird breeding by removing decorations."],
      answer="B",
      why="The text says explicitly that the bower is not a nest and that decoration affects "
          "female choice. It never says females prefer one colour, only that objects are sorted."),
 dict(num="C2", skill="Central Ideas and Details",
      passage="Roman concrete harbours have stood in seawater for two thousand years while modern "
              "marine concrete degrades within decades. Analysis of Roman samples shows that "
              "seawater percolating through the material reacts with volcanic ash to grow "
              "interlocking crystals in the cracks. The concrete is strengthened by the very "
              "process that weakens its modern counterpart.",
      stem="According to the text, what accounts for the durability of Roman marine concrete?",
      choices=["It contains far less water than modern concrete.",
               "Its cracks are sealed by crystals that seawater helps to form.",
               "It was mixed to a consistency that resists cracking altogether.",
               "The volcanic ash used in it repels seawater."],
      answer="B",
      why="The text says seawater reacting with volcanic ash grows crystals in the cracks. It "
          "does not claim the concrete resists cracking or repels water — the opposite, since "
          "the water must get in."),
 dict(num="C3", skill="Central Ideas and Details",
      passage="The Voynich manuscript has resisted every attempt at decipherment. Its script "
              "shows the statistical regularities of a natural language — word lengths cluster, "
              "and certain characters recur in fixed positions — which argues against its being "
              "random. But no one has matched it to a known tongue, and its illustrations depict "
              "plants that do not exist.",
      stem="Which choice best states the main idea of the text?",
      choices=["The manuscript is almost certainly an elaborate hoax.",
               "The manuscript's script has been matched to an extinct language.",
               "Evidence about the manuscript points in conflicting directions.",
               "The manuscript's illustrations are its most studied feature."],
      answer="C",
      why="Statistical regularity argues for a real language; the unmatched script and "
          "impossible plants argue against. The text draws no conclusion, so 'hoax' overstates it."),
 dict(num="C4", skill="Central Ideas and Details",
      passage="In the 1930s the mathematician Mary Cartwright was asked to explain why radio "
              "amplifiers behaved erratically at high power. The equations she studied produced "
              "solutions that never settled and never repeated. Decades later those solutions "
              "were recognised as early examples of what is now called chaos.",
      stem="According to the text, what was notable about the solutions Cartwright studied?",
      choices=["They settled into a repeating cycle after a long delay.",
               "They neither reached a steady state nor repeated themselves.",
               "They could not be calculated without electronic computers.",
               "They applied only to radio amplifiers and to no other system."],
      answer="B",
      why="'Never settled and never repeated' is stated directly. The text says the solutions "
          "were later recognised as chaos generally, which contradicts the last option."),
 dict(num="C5", skill="Central Ideas and Details",
      passage="Sea otters eat sea urchins, and urchins eat kelp. Where otters were hunted out, "
              "urchin populations exploded and kelp forests were grazed to bare rock. Where "
              "otters have returned, the kelp has come back within a decade — but only where "
              "the rock still holds enough sediment for young kelp to anchor.",
      stem="Which choice best states the main idea of the text?",
      choices=["Sea otters are the only predator capable of controlling urchin numbers.",
               "Kelp forests recover once otters return, provided the substrate permits it.",
               "Urchins cause more damage to kelp forests than any other grazer.",
               "Hunting otters was the sole cause of kelp forest decline."],
      answer="B",
      why="The final clause is the qualification the answer must carry: recovery follows the "
          "otters' return only where young kelp can anchor. The other options make claims of "
          "sole cause or sole predator that the text does not support."),
 dict(num="C6", skill="Central Ideas and Details",
      passage="Between 1935 and 1943 the Federal Writers' Project sent interviewers to record the "
              "recollections of formerly enslaved people. The resulting narratives are "
              "indispensable and also difficult: most interviewers were white, most subjects were "
              "elderly and dependent on local goodwill, and what was said was shaped by both facts.",
      stem="Which choice best states the main idea of the text?",
      choices=["The narratives are unreliable and should be used with caution only rarely.",
               "The narratives are valuable evidence whose conditions of production affected them.",
               "The interviewers deliberately altered the accounts they recorded.",
               "The project should have employed interviewers of the same background as its subjects."],
      answer="B",
      why="'Indispensable and also difficult' is the balance the text strikes, and it names the "
          "conditions that shaped what was said. It never alleges deliberate alteration."),

 # ------------------------------------------- Command of Evidence (9)
 dict(num="E1", skill="Command of Evidence",
      passage="Ecologist Tomas Lindqvist has proposed that urban street trees grow faster than "
              "their rural counterparts because city air is warmer, lengthening the growing "
              "season. A rival explanation holds that the difference is instead due to nitrogen "
              "deposited from vehicle exhaust, which acts as a fertiliser.",
      stem="Which finding, if true, would most directly support Lindqvist's explanation over the rival one?",
      choices=["Street trees in cities are on average taller than rural trees of the same age.",
               "Trees in cool coastal cities with heavy traffic grow no faster than rural trees nearby.",
               "Nitrogen levels in city soils are higher than in rural soils.",
               "Rural trees planted beside motorways grow faster than those planted inland."],
      answer="B",
      why="Lindqvist's account depends on warmth, the rival's on traffic nitrogen. A cool city "
          "with heavy traffic separates the two: no growth advantage there means nitrogen alone "
          "is not enough, favouring warmth. Option D would support the rival."),
 dict(num="E2", skill="Command of Evidence",
      passage="A curator argues that a small panel long catalogued as a workshop copy is in fact "
              "by the master herself, pointing to the confidence of the underdrawing revealed by "
              "infrared imaging.",
      stem="Which finding, if true, would most directly undermine the curator's argument?",
      choices=["Infrared imaging of the panel shows no changes between underdrawing and paint layer.",
               "Several documented workshop copies show underdrawing of comparable confidence.",
               "The panel's wooden support comes from a tree felled during the master's lifetime.",
               "The master is known to have completed few panels of this size."],
      answer="B",
      why="The argument rests on confident underdrawing being distinctive of the master. If "
          "documented workshop copies show the same, the evidence no longer distinguishes. The "
          "dating in C would support the attribution, not undermine it."),
 dict(num="E3", skill="Command of Evidence",
      passage="A linguist claims that a community's shift away from its heritage language was "
              "driven mainly by schooling policy rather than by migration to cities, since the "
              "shift accelerated sharply in the decade a monolingual school system was imposed.",
      stem="Which finding, if true, would most directly support the linguist's claim?",
      choices=["Migration to cities from the community continued at a steady rate throughout the century.",
               "The heritage language is still spoken by elders in the community today.",
               "Neighbouring communities that migrated at similar rates but kept bilingual schooling retained the language.",
               "The monolingual school system was abandoned after thirty years."],
      answer="C",
      why="The claim needs schooling separated from migration. Communities with the same "
          "migration but different schooling, and a different outcome, isolate schooling as the "
          "cause. A alone shows migration was constant but not what the schooling did."),
 dict(num="E4", skill="Command of Evidence",
      passage="Researchers studying a songbird found that males raised in isolation produce songs "
              "that are simpler than those of wild males but that still contain the species' "
              "characteristic opening phrase. They concluded that the opening phrase is innate "
              "while the rest is learned.",
      stem="Which finding, if true, would most directly weaken the researchers' conclusion?",
      choices=["Isolated males sing less often than wild males.",
               "Wild males vary considerably in the length of their songs.",
               "Isolated males can hear recordings of adult song played elsewhere in the facility.",
               "The opening phrase is shorter in isolated males than in wild males."],
      answer="C",
      why="The conclusion depends on the isolated males never having heard the phrase. If they "
          "could hear recordings, the phrase might have been learned after all. Frequency and "
          "length differences leave the innate/learned split untouched."),
 dict(num="E5", skill="Command of Evidence",
      passage="A historian argues that a medieval town's sudden prosperity came from a change in "
              "trade routes rather than from a local increase in wool production.",
      stem="Which finding, if true, would most directly support the historian's argument?",
      choices=["Wool exports recorded at the town's port rose sharply in the same decade.",
               "The number of sheep grazed in the surrounding countryside was unchanged across the period.",
               "The town's population grew steadily over the following century.",
               "Several neighbouring towns also prospered during the same decade."],
      answer="B",
      why="If local flocks did not grow, the prosperity cannot be explained by more local wool, "
          "which is exactly the alternative the historian rejects. A is consistent with either "
          "explanation, since goods could be passing through."),
 dict(num="E6", skill="Command of Evidence",
      passage="A materials scientist claims that a new alloy resists fatigue because of its "
              "unusually fine grain structure, not because of the trace niobium it contains.",
      stem="Which finding, if true, would most directly support the scientist's claim?",
      choices=["Alloys with the same niobium content but coarser grains fail after far fewer cycles.",
               "The alloy's grain structure is finer than that of any comparable alloy.",
               "Removing niobium from the alloy makes it harder to cast.",
               "The alloy costs more to produce than conventional alternatives."],
      answer="A",
      why="Holding niobium constant and varying grain size isolates grain structure as the "
          "cause. B establishes the fineness but not that fineness is what does the work."),
 dict(num="E7", skill="Command of Evidence",
      passage="A team argues that a cave's hand stencils were made by adolescents rather than "
              "adults, on the basis of the small size of the hands.",
      stem="Which finding, if true, would most directly weaken the team's argument?",
      choices=["The stencils were made over a period of several centuries.",
               "Adult women in the population had hands within the same size range as the stencils.",
               "Similar stencils are found in caves elsewhere in the region.",
               "The pigment used in the stencils was traded over long distances."],
      answer="B",
      why="The inference runs from small hands to adolescence. If adult women's hands were the "
          "same size, small hands no longer indicate age. The other options say nothing about "
          "who made them."),
 dict(num="E8", skill="Command of Evidence",
      passage="A psychologist proposes that people recall the beginnings and ends of lists better "
              "than the middles because attention lapses during the middle, not because of how "
              "memory stores order.",
      stem="Which finding, if true, would most directly support the psychologist's proposal?",
      choices=["The effect is stronger for long lists than for short ones.",
               "Participants warned that they will be tested on middle items recall them as well as the ends.",
               "The effect appears in participants of all ages.",
               "Participants recall the last item best of all."],
      answer="B",
      why="If directing attention to the middle removes the deficit, the deficit was about "
          "attention rather than storage — exactly the proposal. A and D are consistent with "
          "either explanation."),
 dict(num="E9", skill="Command of Evidence",
      passage="An engineer argues that a bridge's unexpected swaying was caused by pedestrians "
              "unconsciously matching their steps to the bridge's motion, rather than by wind.",
      stem="Which finding, if true, would most directly support the engineer's argument?",
      choices=["The swaying occurred on days with little or no wind whenever the bridge was crowded.",
               "The bridge was designed to withstand winds far stronger than any recorded.",
               "Pedestrians reported feeling unsteady while crossing.",
               "The swaying stopped when the bridge was closed for repairs."],
      answer="A",
      why="Swaying on windless days rules out wind, and its coinciding with crowds points to "
          "pedestrians. B shows the bridge could survive wind, not that wind was absent; D is "
          "consistent with either cause since closing removes both."),

 # ------------------------------------------------------ Inferences (6)
 dict(num="I1", skill="Inferences",
      passage="The tuatara of New Zealand is often called a living fossil, but the label misleads. "
              "Its lineage is indeed ancient, having diverged from other reptiles over two hundred "
              "million years ago. Yet molecular studies show that tuatara DNA has accumulated "
              "changes faster than that of any other vertebrate yet measured. The animal's "
              "appearance has changed little; its genome, by contrast, _____",
      stem="Which choice most logically completes the text?",
      choices=["has remained essentially unaltered since the lineage diverged.",
               "has changed more rapidly than its outward form would suggest.",
               "resembles that of other reptiles more closely than expected.",
               "cannot be compared with that of other vertebrates."],
      answer="B",
      why="The contrast is between an unchanged appearance and a fast-changing genome, which is "
          "what B states. A contradicts the molecular finding outright."),
 dict(num="I2", skill="Inferences",
      passage="Anthropologist Nadia Behrouz notes that in the communities she studied, gift-giving "
              "at weddings is meticulously recorded, and a family that receives a large gift is "
              "expected to give one of similar value when the giver's own children marry. The "
              "practice functions less as generosity than as _____",
      stem="Which choice most logically completes the text?",
      choices=["a form of credit extended between families over time.",
               "a display of wealth intended to establish social rank.",
               "a ritual whose original meaning has been forgotten.",
               "an obligation imposed by religious authorities."],
      answer="A",
      why="Recording gifts and repaying at equal value later is lending and settling — credit "
          "across time. Nothing in the text concerns rank, forgetting, or religious authority."),
 dict(num="I3", skill="Inferences",
      passage="Solar panels lose efficiency as they heat, and a panel in direct desert sun can run "
              "far hotter than its rated temperature. Engineers testing installations in Morocco "
              "found that panels mounted a few centimetres higher above the ground, allowing air "
              "to pass beneath, produced measurably more power than identical panels mounted "
              "flush. This suggests that in hot climates the mounting height _____",
      stem="Which choice most logically completes the text?",
      choices=["matters more than the efficiency rating of the panel itself.",
               "affects output by influencing how well the panels shed heat.",
               "should be minimised to reduce wind loading on the array.",
               "has no measurable effect once panels exceed their rated temperature."],
      answer="B",
      why="Airflow beneath cools the panel, and cooler panels are more efficient — so height "
          "acts through heat shedding. A makes a comparison the text never sets up."),
 dict(num="I4", skill="Inferences",
      passage="A study of urban foxes found that individuals living near busy roads were bolder "
              "in approaching novel objects than those in quiet parks. The researchers caution, "
              "however, that they measured boldness only in adults. If bold foxes are more likely "
              "to settle near roads in the first place, then the study's finding _____",
      stem="Which choice most logically completes the text?",
      choices=["would be strengthened by adding juveniles to the sample.",
               "may reflect where bold foxes choose to live rather than an effect of traffic.",
               "would apply only to foxes in the parks studied.",
               "shows that traffic makes foxes bolder over time."],
      answer="B",
      why="The caution raises self-selection: boldness could precede the location rather than "
          "result from it. D asserts the causal reading the caution puts in doubt."),
 dict(num="I5", skill="Inferences",
      passage="Manuscripts copied in the scriptorium at Corbie can be identified by a distinctive "
              "letterform. Scholars long assumed the form was invented there. But a charter from a "
              "monastery three hundred kilometres away, securely dated forty years earlier, uses "
              "the same form. The Corbie scribes, it now appears, _____",
      stem="Which choice most logically completes the text?",
      choices=["adopted a letterform that already existed elsewhere.",
               "were trained at the monastery that produced the charter.",
               "invented the letterform independently of the charter's scribe.",
               "copied the charter directly into their own manuscripts."],
      answer="A",
      why="An earlier, securely dated use elsewhere means Corbie did not originate the form. B "
          "and D add specific histories the evidence does not establish."),
 dict(num="I6", skill="Inferences",
      passage="Coffee plants grown in full sun yield more beans per hectare than those grown "
              "under shade trees. Shade-grown plots, however, retain more soil nitrogen, suffer "
              "less erosion, and continue producing for decades after full-sun plots have been "
              "abandoned. A grower comparing the two systems on yield alone would therefore _____",
      stem="Which choice most logically completes the text?",
      choices=["overstate the long-term advantage of full-sun cultivation.",
               "find shade-grown coffee more profitable in the first season.",
               "conclude that shade trees have no effect on soil quality.",
               "underestimate the number of beans a full-sun plot produces."],
      answer="A",
      why="Yield alone favours full sun, while the omitted factors all favour shade over time — "
          "so a yield-only comparison overstates full sun's long-run case."),

 # ----------------------------------------------------- Boundaries (12)
 bnd("B1", "The cartographer Marie Tharp spent years plotting soundings by hand _____ the result "
           "was the first map to show the mid-Atlantic ridge as a continuous feature.",
     ["; ", ", ", " ", ": and"], "A",
     "Two independent clauses with no coordinating conjunction require a semicolon; a comma "
     "alone is a splice."),
 bnd("B2", "Because the samples had been stored improperly _____ the team could not use them to "
           "establish a baseline.",
     [", ", "; ", ": ", " and "], "A",
     "An introductory dependent clause beginning 'Because' is followed by a comma before the "
     "main clause."),
 bnd("B3", "The library holds three items of interest to the project _____ a ledger, a bundle of "
           "letters and a hand-drawn plan of the estate.",
     [": ", "; ", ", and ", " which are"], "A",
     "A colon introduces the list that specifies the 'three items' announced by the complete "
     "clause before it."),
 bnd("B4", "Aksum, a kingdom centred on what is now northern Ethiopia _____ minted its own "
           "coinage from the third century onward.",
     [", ", "; ", ": ", " "], "A",
     "The appositive 'a kingdom centred on...' needs a closing comma to match the one that "
     "opened it."),
 bnd("B5", "The revised design reduced material use by a fifth _____ it also cut assembly time "
           "almost in half.",
     [", and ", ", ", "; also ", " "], "A",
     "Two independent clauses joined by a comma plus the coordinating conjunction 'and'."),
 bnd("B6", "Researchers have recovered pollen, seeds and insect remains from the peat _____ each "
           "of which helps date the layers around it.",
     [", ", "; ", ": ", ". "], "A",
     "'each of which' opens a non-essential relative clause, attached with a comma; a semicolon "
     "would need an independent clause after it."),
 bnd("B7", "When the tide is out _____ the causeway is passable on foot.",
     [", ", "; ", ": ", " that "], "A",
     "The dependent clause 'When the tide is out' precedes the main clause and takes a comma."),
 bnd("B8", "The engine ran for eleven hours without fault _____ then, without warning, it seized.",
     ["; ", ", ", ": ", " "], "A",
     "'then' is not a coordinating conjunction, so a comma between these two independent clauses "
     "would be a splice."),
 bnd("B9", "Hedgerows shelter species that farmland cannot support on its own _____ dormice, "
           "several warblers and a great many invertebrates.",
     [": ", "; ", ", but ", " and"], "A",
     "The complete clause is followed by a colon introducing the list that specifies the species."),
 bnd("B10", "Although the manuscript is undated _____ its watermark places it within a decade.",
     [", ", "; ", ": ", " and "], "A",
     "'Although' opens a dependent clause, which is separated from the main clause by a comma."),
 bnd("B11", "The survey covered every district in the city _____ the results were published the "
            "following spring.",
     ["; ", ", ", ": ", " "], "A",
     "Two independent clauses with no conjunction: semicolon."),
 bnd("B12", "Mercury, the smallest planet in the solar system _____ has almost no atmosphere to "
            "retain heat.",
     [", ", "; ", ": ", " "], "A",
     "The appositive must be closed with a comma before the verb 'has'."),

 # ------------------------------------------ Form, Structure, and Sense (9)
 fss("F1", "Neither the surveyor nor the two assistants _____ able to reach the summit before dark.",
     ["was", "were", "has been", "is"], "B",
     "With 'neither...nor', the verb agrees with the nearer subject, 'the two assistants', which "
     "is plural."),
 fss("F2", "The collection of maps, along with several atlases, _____ kept in a climate-"
           "controlled room.",
     ["are", "is", "have been", "were"], "B",
     "The subject is 'collection', singular; 'along with several atlases' is an interrupting "
     "phrase and does not change the number."),
 fss("F3", "By the time the expedition reached the coast, the supplies they had packed in "
           "September _____ almost entirely.",
     ["are depleted", "deplete", "had been depleted", "will be depleted"], "C",
     "The depletion finished before the past-tense arrival, so the past perfect is required."),
 fss("F4", "Each of the three prototypes _____ its own control board.",
     ["have", "has", "having", "were having"], "B",
     "'Each' is singular regardless of the prepositional phrase that follows it."),
 fss("F5", "The report criticises the ministry for failing to consult residents and for _____ "
           "the objections it did receive.",
     ["ignoring", "it ignored", "having ignore", "to ignore"], "A",
     "Parallel structure: 'for failing' and 'for ignoring' must take the same form."),
 fss("F6", "Having been restored twice in the last century, the fresco _____ more of the "
           "restorers' work than of the original.",
     ["showing", "shows", "to show", "shown"], "B",
     "The introductory participial phrase must be followed by a main clause with a finite verb."),
 fss("F7", "The results were more consistent than _____ obtained in the earlier trial.",
     ["that", "those", "them", "it"], "B",
     "The pronoun stands for the plural 'results', so 'those' is required."),
 fss("F8", "The committee published its findings in March, and by June the recommendations "
           "_____ into policy.",
     ["are written", "have written", "had been written", "writing"], "C",
     "The writing was complete by June, a point in the past, so the past perfect passive fits."),
 fss("F9", "Not only did the storm damage the pier, but it also _____ the harbour wall.",
     ["breaching", "breached", "breach", "had breach"], "B",
     "'Not only did... but it also' takes a matching past-tense verb after 'also'."),

 # ------------------------------------------------------ Transitions (9)
 trn("T1", "The alloy is light and unusually stiff. _____ it is expensive enough that it is used "
           "only where weight is critical.",
     ["However,", "Therefore,", "Likewise,", "For example,"], "A",
     "The cost is a drawback set against the advantages just listed, so a contrast is needed."),
 trn("T2", "The colony's records were destroyed in a fire in 1698. _____ almost everything known "
           "about its first decade comes from letters held elsewhere.",
     ["Nevertheless,", "Consequently,", "By contrast,", "Similarly,"], "B",
     "The reliance on letters is the result of the records being destroyed."),
 trn("T3", "Some frogs freeze almost solid through the winter, their hearts stopping entirely. "
           "_____ certain fish survive by producing proteins that prevent ice crystals from "
           "forming at all.",
     ["Consequently,", "In other words,", "Similarly,", "Nevertheless,"], "C",
     "A second example of the same phenomenon — surviving freezing — calls for a comparison."),
 trn("T4", "The new timetable reduced the average journey by four minutes. _____ passenger "
           "numbers on the line fell in the same period.",
     ["Accordingly,", "Nonetheless,", "Indeed,", "That is,"], "B",
     "Falling numbers are unexpected given the improvement, so the transition must signal "
     "contrast."),
 trn("T5", "Lead pipes were used in Roman aqueducts for centuries. _____ the water they carried "
           "was so heavily mineralised that a layer of scale quickly coated the metal.",
     ["For instance,", "In fact,", "However,", "Thus,"], "C",
     "The scale layer works against the expected danger of lead, so it qualifies the preceding "
     "sentence."),
 trn("T6", "The instrument records tremors far too faint for anyone to feel. _____ it can detect "
           "a quarry blast fifty kilometres away.",
     ["Nevertheless,", "For example,", "In contrast,", "Instead,"], "B",
     "The blast is an instance of the sensitivity just claimed."),
 trn("T7", "Early photographs required exposures of several minutes. _____ portrait subjects were "
           "clamped into frames to hold their heads still.",
     ["For this reason,", "Even so,", "By comparison,", "In summary,"], "A",
     "The clamping follows from the long exposure — a cause-and-effect link."),
 trn("T8", "The two manuscripts share the same scribal errors in the same places. _____ they "
           "were almost certainly copied from a common source.",
     ["Conversely,", "Thus,", "Meanwhile,", "Admittedly,"], "B",
     "The shared errors are the evidence and the common source the conclusion drawn from it."),
 trn("T9", "Wind turbines are usually sited on ridgelines to catch stronger, steadier air. "
           "_____ ridgelines are often the routes migrating birds follow.",
     ["Unfortunately,", "Likewise,", "As a result,", "In particular,"], "A",
     "The bird routes are a problem created by the siting choice, so the transition must mark "
     "the complication."),

 # ----------------------------------------- Rhetorical Synthesis (9)
 *[dict(num=f"R{i}", skill="Rhetorical Synthesis", passage=p, stem=st, choices=ch, answer=a, why=w)
   for i, (p, st, ch, a, w) in enumerate([
   ("While researching a topic, a student has taken the following notes:<ul>"
    "<li>Mangrove forests grow in salt water along tropical coasts.</li>"
    "<li>Their roots trap sediment carried by rivers.</li>"
    "<li>Trapped sediment raises the seabed over time.</li>"
    "<li>A raised seabed reduces the height of waves reaching the shore.</li></ul>",
    "The student wants to explain how mangroves protect coastlines. Which choice most effectively "
    "uses relevant information from the notes to accomplish this goal?",
    ["Mangrove forests grow in salt water along tropical coasts, where rivers carry sediment.",
     "By trapping river sediment, mangrove roots raise the seabed, which reduces the height of waves reaching the shore.",
     "Mangrove roots trap sediment, and mangroves grow along tropical coasts.",
     "Waves reaching tropical shores are lower than they would otherwise be."],
    "B",
    "The goal is the mechanism of protection, and only B links trapping to raising to smaller "
    "waves. C and A state facts without connecting them to protection."),
   ("While researching a topic, a student has taken the following notes:<ul>"
    "<li>Ada Lovelace wrote notes on Charles Babbage's Analytical Engine in 1843.</li>"
    "<li>Her notes were three times longer than the paper she was translating.</li>"
    "<li>They included a method for computing Bernoulli numbers.</li>"
    "<li>That method is often called the first published computer program.</li></ul>",
    "The student wants to emphasise the significance of Lovelace's notes. Which choice most "
    "effectively uses relevant information from the notes to accomplish this goal?",
    ["Lovelace's 1843 notes were three times longer than the paper she was translating.",
     "Lovelace translated a paper about Charles Babbage's Analytical Engine in 1843.",
     "Lovelace's 1843 notes contained a method for computing Bernoulli numbers that is often called the first published computer program.",
     "Charles Babbage designed the Analytical Engine, which Lovelace wrote about in 1843."],
    "C",
    "Significance is carried by the 'first published computer program' claim. Length and the "
    "fact of translation are incidental."),
   ("While researching a topic, a student has taken the following notes:<ul>"
    "<li>The Antikythera mechanism was recovered from a shipwreck in 1901.</li>"
    "<li>It contains at least 30 interlocking bronze gears.</li>"
    "<li>It was used to predict eclipses and track the calendar.</li>"
    "<li>No comparable geared device is known for the next thousand years.</li></ul>",
    "The student wants to explain why the mechanism is considered remarkable. Which choice most "
    "effectively uses relevant information from the notes to accomplish this goal?",
    ["The mechanism was recovered from a shipwreck in 1901 and contains at least 30 gears.",
     "The mechanism used at least 30 interlocking gears to predict eclipses, and nothing comparable is known for the next thousand years.",
     "The mechanism was used to track the calendar and predict eclipses.",
     "No geared device comparable to the mechanism appeared for a thousand years after it."],
    "B",
    "Remarkableness rests on the sophistication and the gap that followed; B is the only choice "
    "carrying both."),
   ("While researching a topic, a student has taken the following notes:<ul>"
    "<li>Fungi form networks of thin filaments called hyphae.</li>"
    "<li>Hyphae connect to tree roots and exchange nutrients with them.</li>"
    "<li>Trees supply the fungus with sugars.</li>"
    "<li>The fungus supplies the tree with phosphorus from the soil.</li></ul>",
    "The student wants to describe the exchange between fungi and trees. Which choice most "
    "effectively uses relevant information from the notes to accomplish this goal?",
    ["Fungi form networks of thin filaments called hyphae that connect to tree roots.",
     "Trees and fungi both benefit from the connection between hyphae and roots.",
     "Through hyphae connected to tree roots, trees supply fungi with sugars while fungi supply trees with soil phosphorus.",
     "Fungi obtain phosphorus from the soil and pass some of it on."],
    "C",
    "The goal names the exchange, so both directions must appear. B asserts mutual benefit "
    "without saying what is exchanged."),
   ("While researching a topic, a student has taken the following notes:<ul>"
    "<li>The Great Bath at Mohenjo-daro was built around 2500 BCE.</li>"
    "<li>It is lined with tightly fitted brick sealed with bitumen.</li>"
    "<li>The seal has kept it watertight for over four thousand years.</li>"
    "<li>Its purpose is still debated.</li></ul>",
    "The student wants to emphasise the builders' technical skill. Which choice most effectively "
    "uses relevant information from the notes to accomplish this goal?",
    ["The Great Bath was built around 2500 BCE, and its purpose is still debated.",
     "The Great Bath's brick lining, sealed with bitumen, has remained watertight for over four thousand years.",
     "The Great Bath at Mohenjo-daro is lined with tightly fitted brick.",
     "Archaeologists continue to debate the purpose of the Great Bath."],
    "B",
    "Technical skill is demonstrated by the seal still working after four millennia, which only "
    "B states."),
   ("While researching a topic, a student has taken the following notes:<ul>"
    "<li>Bessie Coleman was refused entry to American flight schools in 1918.</li>"
    "<li>She learned French in order to train abroad.</li>"
    "<li>She earned her licence in France in 1921.</li>"
    "<li>She was the first African American woman to hold a pilot's licence.</li></ul>",
    "The student wants to emphasise the lengths Coleman went to in order to fly. Which choice "
    "most effectively uses relevant information from the notes to accomplish this goal?",
    ["Bessie Coleman earned her pilot's licence in France in 1921.",
     "Refused entry to American flight schools, Coleman learned French so that she could train abroad, earning her licence in 1921.",
     "Coleman was the first African American woman to hold a pilot's licence.",
     "American flight schools refused Coleman entry in 1918."],
    "B",
    "The lengths are the obstacle and the response to it; B carries both, while C states an "
    "outcome rather than an effort."),
   ("While researching a topic, a student has taken the following notes:<ul>"
    "<li>Cochineal is a red dye made from insects that feed on cactus.</li>"
    "<li>It was produced in Oaxaca and exported to Europe from the 1500s.</li>"
    "<li>For two centuries it was Mexico's second most valuable export after silver.</li>"
    "<li>Synthetic dyes replaced it in the late 1800s.</li></ul>",
    "The student wants to convey the economic importance of cochineal. Which choice most "
    "effectively uses relevant information from the notes to accomplish this goal?",
    ["Cochineal is a red dye made from insects that feed on cactus.",
     "Cochineal was exported to Europe from Oaxaca beginning in the 1500s.",
     "For two centuries cochineal was Mexico's second most valuable export, behind only silver.",
     "Synthetic dyes replaced cochineal in the late 1800s."],
    "C",
    "Only C measures economic importance; the others describe what the dye is, where it went, "
    "or how it ended."),
   ("While researching a topic, a student has taken the following notes:<ul>"
    "<li>Emperor penguins huddle in tight groups during Antarctic winter.</li>"
    "<li>Birds on the windward edge lose heat fastest.</li>"
    "<li>The huddle moves slowly, in waves, as birds shuffle inward.</li>"
    "<li>Over time every bird spends a similar period at the edge.</li></ul>",
    "The student wants to explain how the huddle shares the cost of warmth. Which choice most "
    "effectively uses relevant information from the notes to accomplish this goal?",
    ["Emperor penguins huddle in tight groups during the Antarctic winter.",
     "Because the huddle shuffles inward in slow waves, each bird spends a similar period on the cold windward edge.",
     "Birds on the windward edge of the huddle lose heat fastest.",
     "The huddle moves slowly and in waves during the winter."],
    "B",
    "Sharing the cost requires linking the shuffling to the equal time spent at the edge, which "
    "only B does."),
   ("While researching a topic, a student has taken the following notes:<ul>"
    "<li>Hedy Lamarr co-patented a frequency-hopping system in 1942.</li>"
    "<li>The system was designed to stop radio-guided torpedoes being jammed.</li>"
    "<li>The navy did not adopt it during the war.</li>"
    "<li>Frequency hopping underlies modern Bluetooth and Wi-Fi.</li></ul>",
    "The student wants to emphasise the lasting influence of Lamarr's patent. Which choice most "
    "effectively uses relevant information from the notes to accomplish this goal?",
    ["Lamarr co-patented a frequency-hopping system in 1942 to prevent the jamming of torpedoes.",
     "The navy did not adopt Lamarr's frequency-hopping system during the war.",
     "Though the navy passed over her 1942 patent, the frequency hopping Lamarr co-invented underlies Bluetooth and Wi-Fi today.",
     "Lamarr's system was intended to stop radio-guided torpedoes from being jammed."],
    "C",
    "Lasting influence is the link from the ignored patent to today's technologies, which only "
    "C makes."),
   ], 1)],
]

# W13 was drafted as an underlined-word item and needs its own passage, so it is
# defined here rather than through the `wic` helper.
QUESTIONS[12] = dict(
    num="W13", skill="Words in Context",
    passage="The surveyor's field book does not record impressions. It is a register of angles, "
            "distances and bearings, set down in the same hand for thirty years, from which the "
            "shape of a coastline can be reconstructed but nothing of the weather or the company.",
    stem="As used in the text, what does the word &ldquo;register&rdquo; most nearly mean?",
    choices=["A formal tone of writing.", "A systematic record.", "An official who keeps records.",
             "A range of musical pitch."],
    answer="B",
    why="The field book holds angles, distances and bearings set down over thirty years — a "
        "systematic record. The 'tone' sense is a real meaning of the word but is ruled out by "
        "the list of measurements.")

DROPPED = {}
