"""
Originally authored Reading & Writing questions for Tests 6 and 7.

The source material is exhausted: 128 of the 162 questions needed were
transcribed from the October and August papers, and every remaining page either
duplicates a question already live in production or was never captured by the
screen recordings. `CLAUDE.md` sanctions authoring in exactly this situation —
"write original SAT-style questions rather than shipping an undersized module or
reusing content" — and this file supplies the other 34.

## What is authored, and why these domains

| Domain | Authored | Reason |
|---|---|---|
| Boundaries | 9 | punctuation between clauses is decidable by rule |
| Form, Structure, and Sense | 7 | agreement, tense and verb form are decidable by rule |
| Transitions | 7 | the logical relation is fixed by the surrounding sentences |
| Rhetorical Synthesis | 2 | the goal sentence makes exactly one choice correct |
| Words in Context | 6 | the surrounding sentence constrains the blank to one sense |
| Command of Evidence | 3 | built on tables written here, so the data settles the answer |

Writing dominates because writing was the binding constraint throughout: six
modules need about 78 writing questions and the source papers yielded 53.
Grammar-domain items are also the safest kind to author — correctness follows
from a stated convention rather than from a judgement call, the same property
that makes sympy verification work for the Math side. Every question below
carries a `rule` field naming the convention or relation it turns on, so the
answer can be checked against the rule rather than taken on trust.

## Sourcing constraints observed

No question here attributes a claim, quotation or study to a real person. Where
a question needs data, the data is presented as an unattributed measurement and
the table is written out in full, so nothing is fabricated on anyone's behalf.
Passage topics were chosen to avoid the subject matter already used across
Tests 1-5 and the 128 transcribed questions.

`verify_authored_rw.py` checks shape, answer-key sanity, and template/lexical
dedupe against all 405 live production R&W questions plus the 128 transcribed
here.
"""

SOURCE = "AUTHORED"

QUESTIONS = [
 # ---------------------------------------------------------------- Boundaries (9)
 dict(num="A-B1", skill="Boundaries", rule="two independent clauses need more than a comma",
   passage="The Hall of Mirrors at the Palace of Versailles took six years to _____ its 357 mirrors were "
           "among the most expensive objects in seventeenth-century France.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["complete,", "complete, and,", "complete", "complete;"], answer="D",
   why="'The Hall of Mirrors took six years to complete' and 'its 357 mirrors were among the most "
       "expensive objects...' are both independent clauses, so only the semicolon can join them. The bare "
       "comma splices them, 'complete' alone runs them together, and 'and,' strands a comma after the "
       "conjunction."),

 dict(num="A-B2", skill="Boundaries", rule="a supplementary element takes a matched pair of marks",
   passage="The axolotl&mdash;a salamander that keeps its larval features into _____ can regrow not only "
           "its limbs but also parts of its heart and brain.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["adulthood,", "adulthood", "adulthood&mdash;", "adulthood:"], answer="C",
   why="A dash opens the supplementary description of the axolotl, so a dash must close it. Swapping in a "
       "comma or a colon breaks the pair, and omitting the mark leaves the aside running into the verb."),

 dict(num="A-B3", skill="Boundaries", rule="no punctuation between a subject and its verb",
   passage="The practice of storing grain in raised stone granaries _____ several communities in the "
           "Atlas Mountains through centuries of unpredictable harvests.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["sustained", "sustained,", "; sustained", ", sustained"], answer="A",
   why="'The practice of storing grain in raised stone granaries' is the subject and 'sustained' its "
       "verb; nothing belongs between them."),

 dict(num="A-B4", skill="Boundaries", rule="a colon introduces an explanation after a complete clause",
   passage="Sourdough bakers rely on a starter that is never entirely used _____ a portion is always held "
           "back to leaven the next loaf.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["up:", "up,", "up and", "up"], answer="A",
   why="The first clause is complete and the second explains what makes the starter never entirely used "
       "up, which is a colon's job. The comma alone splices two independent clauses, 'and' joins them "
       "without the comma it needs, and the unpunctuated version is a run-on."),

 dict(num="A-B5", skill="Boundaries", rule="a nonrestrictive clause is set off by commas on both sides",
   passage="The tuatara, a reptile found only on a few islands off New _____ is the sole surviving member "
           "of an order that otherwise died out roughly 60 million years ago.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["Zealand", "Zealand:", "Zealand;", "Zealand,"], answer="D",
   why="'A reptile found only on a few islands off New Zealand' is a nonrestrictive appositive opened by "
       "a comma, so a comma must close it before the main verb 'is'. A semicolon or colon would break the "
       "sentence in two, and omitting the mark leaves the appositive unclosed."),

 dict(num="A-B6", skill="Boundaries", rule="a comma plus a coordinating conjunction joins independent clauses",
   passage="Icelandic turf houses were built with thick walls of stacked sod to hold heat through the "
           "winter, _____ the same walls kept interiors cool during the long days of summer.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["and", "and,", "however", "therefore"], answer="A",
   why="Both halves are independent clauses, so the comma needs a coordinating conjunction after it. "
       "'However' and 'therefore' are conjunctive adverbs, which cannot join clauses with only a comma, "
       "and B adds a comma with nothing to set off."),

 dict(num="A-B7", skill="Boundaries", rule="a conjunctive adverb between clauses needs a semicolon before it",
   passage="Cochineal insects yield a red dye so vivid that it was once traded across three "
           "_____ synthetic alternatives had replaced it in most industries.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["continents, by 1900,", "continents by 1900,", "continents; by 1900,", "continents by 1900"],
   answer="C",
   why="'Cochineal insects yield a red dye...' and 'synthetic alternatives had replaced it...' are "
       "independent clauses, and 'by 1900' introduces the second. A semicolon is required; a comma "
       "splices them and the unpunctuated versions run on."),

 dict(num="A-B8", skill="Boundaries", rule="items in a series are separated by commas",
   passage="A traditional Japanese toolbox holds only a handful of implements&mdash;a pull saw, a marking "
           "gauge, a set of chisels, and a _____ each of which is sharpened rather than replaced.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["plane&mdash;", "plane,", "plane;", "plane"], answer="A",
   why="A dash opened the list, so a dash closes it before the relative clause 'each of which...'. A "
       "comma or semicolon would leave the opening dash unmatched."),

 dict(num="A-B9", skill="Boundaries", rule="a sentence boundary is needed between two complete thoughts",
   passage="Bioluminescent fungi glow steadily rather than in _____ researchers studying one species "
           "recorded emission that varied by less than a tenth over a full night.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["pulses,", "pulses. Researchers", "pulses, researchers", "pulses researchers"],
   answer="B",
   why="Two complete thoughts require a sentence boundary. A leaves the second clause without a subject "
       "position, C is a comma splice, and D is a run-on. Only B closes the first sentence and starts the "
       "second."),

 # ------------------------------------------- Form, Structure, and Sense (7)
 dict(num="A-F1", skill="Form, Structure, and Sense", rule="subject-verb agreement across a modifier",
   passage="The collection of woodblock prints donated to the museum by three separate families _____ "
           "views of the same mountain in every season.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["show", "have shown", "showing", "shows"], answer="D",
   why="The subject is the singular 'collection', not the plural nouns inside the modifier, so the "
       "singular 'shows' is required. 'Showing' supplies no finite verb at all."),

 dict(num="A-F2", skill="Form, Structure, and Sense", rule="pronoun-antecedent agreement",
   passage="Because the glaciers of the Southern Alps advance and retreat on different schedules, "
           "surveyors measure _____ individually rather than treating the range as a single system.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["it", "that", "this", "them"], answer="D",
   why="The antecedent is the plural 'glaciers', so the plural object pronoun 'them' is required."),

 dict(num="A-F3", skill="Form, Structure, and Sense", rule="tense agreement with a fixed past time marker",
   passage="In 1783, the Laki fissure in Iceland began an eruption that lasted eight months. Ash carried "
           "on the wind _____ harvests as far away as central Europe that year.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["damages", "is damaging", "damaged", "will damage"], answer="C",
   why="'In 1783' and 'that year' fix the event in the completed past, and the surrounding verbs "
       "('began', 'lasted') are simple past."),

 dict(num="A-F4", skill="Form, Structure, and Sense", rule="a participle, not a finite verb, after a subject that already has one",
   passage="Cartographers _____ the coastline before satellite imagery existed relied on chains of "
           "triangles measured from hilltop to hilltop.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["mapping", "mapped", "map", "have mapped"], answer="A",
   why="'Relied' is already the sentence's main verb, so the blank must open a participial phrase "
       "modifying 'cartographers'. Any finite form gives the subject two verbs with no conjunction."),

 dict(num="A-F5", skill="Form, Structure, and Sense", rule="possessive versus plural",
   passage="The weavers guild kept its patterns secret for generations, and even today several of the "
           "_____ techniques are known only to families who have practiced them since the 1700s.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["guilds", "guild&rsquo;s", "guilds&rsquo;", "guilds&rsquo;s"], answer="B",
   why="The techniques belong to the one guild named in the first clause, so the singular possessive is "
       "correct. A is a bare plural, C is a plural possessive, and D is not a form English uses."),

 dict(num="A-F6", skill="Form, Structure, and Sense", rule="parallel structure in a series",
   passage="A restorer working on an oil painting must document the damage, stabilize the flaking paint, "
           "and _____ any varnish that has yellowed with age.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["removing", "to remove", "remove", "removes"], answer="C",
   why="The series is governed by 'must': document, stabilize, and remove. Only the bare infinitive keeps "
       "the three parallel."),

 dict(num="A-F7", skill="Form, Structure, and Sense", rule="subject-verb agreement with an inverted subject",
   passage="Among the instruments recovered from the shipwreck _____ a brass astrolabe engraved with a "
           "date two decades earlier than the voyage itself.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["were", "was", "have been", "are"], answer="B",
   why="The sentence is inverted: the subject is the singular 'a brass astrolabe', which follows the verb. "
       "'Instruments' sits inside the opening prepositional phrase and cannot govern the verb."),

 # ------------------------------------------------------------- Transitions (7)
 dict(num="A-T1", skill="Transitions", rule="cause and effect",
   passage="Saffron must be harvested by hand, and each crocus flower yields only three usable stigmas. "
           "_____ a single kilogram of the spice represents the picking of roughly 150,000 flowers.",
   stem="Which choice completes the text with the most logical transition?",
   choices=["Nevertheless,", "In contrast,", "Similarly,", "Consequently,"], answer="D",
   why="The flower count follows from the hand harvest and the three-stigma yield, so the relation is "
       "causal rather than contrastive or parallel."),

 dict(num="A-T2", skill="Transitions", rule="contrast",
   passage="Most bridges are designed so that the roadway carries the load down to the piers. _____ in a "
           "suspension bridge the roadway hangs from cables, and the load travels upward before it reaches "
           "the towers.",
   stem="Which choice completes the text with the most logical transition?",
   choices=["Likewise,", "For instance,", "By contrast,", "As a result,"], answer="C",
   why="An upward load path is the opposite of the downward one just described. 'Likewise' would require "
       "the two designs to agree, and a suspension bridge is not an instance of the general case."),

 dict(num="A-T3", skill="Transitions", rule="illustration",
   passage="Several languages mark evidentiality, requiring a speaker to indicate how a claim was learned. "
           "_____ in Tariana a verb ending distinguishes something seen from something merely reported by "
           "another person.",
   stem="Which choice completes the text with the most logical transition?",
   choices=["For example,", "However,", "Instead,", "Therefore,"], answer="A",
   why="Tariana is one instance of the general claim about evidentiality, not a contrast with it or a "
       "consequence of it."),

 dict(num="A-T4", skill="Transitions", rule="sequence",
   passage="To cast a bronze sculpture by the lost-wax method, an artist first builds a wax model and "
           "coats it in a heat-resistant shell. _____ the wax is melted out, leaving a cavity that molten "
           "bronze will fill.",
   stem="Which choice completes the text with the most logical transition?",
   choices=["In summary,", "Next,", "By comparison,", "Regardless,"], answer="B",
   why="'First' in the preceding sentence sets up a sequence of steps, and melting the wax is the step "
       "that follows."),

 dict(num="A-T5", skill="Transitions", rule="concession",
   passage="The Antikythera mechanism is often called the first analog computer, and its gear train can "
           "model the motion of the Sun and Moon with real precision. _____ it was built to predict "
           "positions rather than to perform calculations a user supplies.",
   stem="Which choice completes the text with the most logical transition?",
   choices=["Accordingly,", "Furthermore,", "Admittedly,", "Meanwhile,"], answer="C",
   why="The second sentence concedes a limit on the 'first computer' description just given. 'Furthermore' "
       "would add support rather than qualify it, and 'accordingly' would make the limit a consequence."),

 dict(num="A-T6", skill="Transitions", rule="restatement",
   passage="A tidal bore forms when an incoming tide is funneled into a narrowing river channel and the "
           "water piles up faster than it can spread out. _____ the river briefly runs backward.",
   stem="Which choice completes the text with the most logical transition?",
   choices=["In other words,", "Nonetheless,", "For example,", "Previously,"], answer="A",
   why="Running backward restates the piling-up description in plainer terms rather than adding an "
       "instance (C) or a contrast (B)."),

 dict(num="A-T7", skill="Transitions", rule="addition",
   passage="Green roofs reduce the volume of stormwater that reaches a city&rsquo;s drains, easing pressure "
           "on systems that were sized for a smaller population. _____ the soil layer insulates the "
           "building beneath it, lowering the energy needed to heat and cool the top floors.",
   stem="Which choice completes the text with the most logical transition?",
   choices=["In short,", "Instead,", "Moreover,", "Until then,"], answer="C",
   why="Insulation is a second, separate benefit added to the stormwater benefit. 'Instead' would replace "
       "the first claim and 'in short' would summarise it."),

 # ------------------------------------------------- Rhetorical Synthesis (2)
 dict(num="A-R1", skill="Rhetorical Synthesis", rule="the goal names the one fact the sentence must foreground",
   passage="While researching a topic, a student has taken the following notes:</p><ul>"
           "<li>A qanat is an underground channel that carries water from an aquifer to the surface by gravity alone.</li>"
           "<li>Qanats have been built across arid regions of Asia and North Africa for more than 2,500 years.</li>"
           "<li>The Qanat of Gonabad in Iran is about 33 kilometers long.</li>"
           "<li>Its main well shaft reaches a depth of roughly 300 meters.</li>"
           "<li>It still supplies water to farms today.</li></ul>",
   stem="The student wants to emphasize the depth of the Qanat of Gonabad&rsquo;s main well shaft. Which "
        "choice most effectively uses relevant information from the notes to accomplish this goal?",
   choices=["The Qanat of Gonabad, which is about 33 kilometers long, is an underground channel in Iran.", "Qanats have carried water across arid regions of Asia and North Africa for more than 2,500 years.", "The main well shaft of the Qanat of Gonabad descends roughly 300 meters below the surface.", "The Qanat of Gonabad still supplies water to farms today, using gravity alone."], answer="C",
   why="Only the 'descends roughly 300 meters' choice gives the shaft depth. One choice gives the "
       "33-kilometer length instead, and the other two are about qanats generally and about present-day "
       "use."),

 dict(num="A-R2", skill="Rhetorical Synthesis", rule="the goal specifies which contrast to draw",
   passage="While researching a topic, a student has taken the following notes:</p><ul>"
           "<li>Cuneiform and hieroglyphic writing were both used in the ancient world.</li>"
           "<li>Cuneiform was written by pressing a reed stylus into wet clay.</li>"
           "<li>Hieroglyphs were most often carved into stone or painted onto plaster.</li>"
           "<li>Both systems were used for administrative records as well as religious texts.</li></ul>",
   stem="The student wants to emphasize a difference between how the two scripts were produced. Which "
        "choice most effectively uses relevant information from the notes to accomplish this goal?",
   choices=["Cuneiform and hieroglyphic writing were both used for administrative records as well as religious texts.",
            "Cuneiform was pressed into wet clay with a reed stylus, whereas hieroglyphs were most often carved into stone or painted onto plaster.",
            "Cuneiform and hieroglyphic writing were two writing systems of the ancient world.",
            "Hieroglyphs served religious purposes in addition to administrative ones."],
   answer="B",
   why="B names the production method for each and marks the contrast with 'whereas'. A and C state what "
       "the two share, and D describes only one script's uses."),

 # ------------------------------------------------------- Words in Context (6)
 dict(num="A-W1", skill="Words in Context", rule="the second sentence defines the blank",
   passage="Early mechanical clocks were notoriously _____: two clocks in the same town could disagree by "
           "a quarter of an hour by the end of a single day.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["ornate", "portable", "expensive", "imprecise"], answer="D",
   why="The colon spells out the blank: clocks that disagree by a quarter of an hour keep inaccurate time. "
       "Ornateness, cost and portability are never at issue."),

 dict(num="A-W2", skill="Words in Context", rule="the contrast marker fixes the sense",
   passage="Although the first printed maps of the region were widely copied, their coastlines were "
           "largely _____, drawn from sailors&rsquo; recollections rather than from any survey.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["conjectural", "official", "decorative", "restricted"], answer="A",
   why="Coastlines drawn from recollection rather than survey are guessed at. The 'although' concedes the "
       "maps' popularity before this limitation, and none of the other choices describes how a line was "
       "arrived at."),

 dict(num="A-W3", skill="Words in Context", rule="the example constrains the blank",
   passage="The composer&rsquo;s late works are unusually _____: a single movement may quote a folk tune, "
           "a hymn, and a march within the space of two minutes.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["restrained", "eclectic", "repetitive", "somber"], answer="B",
   why="Drawing on a folk tune, a hymn and a march at once is drawing from varied sources. 'Repetitive' "
       "would require the same material to return, which is the opposite of what the example shows."),

 dict(num="A-W4", skill="Words in Context", rule="the blank must fit the argumentative move",
   passage="Critics initially dismissed the technique as a novelty, but its steady adoption by studios "
           "over the following decade _____ that assessment.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["confirmed", "undermined", "anticipated", "restated"], answer="B",
   why="'But' signals that what followed worked against the dismissal, and steady adoption is evidence "
       "the technique was more than a novelty. 'Confirmed' and 'restated' would support the critics."),

 dict(num="A-W5", skill="Words in Context", rule="the sentence's own gloss fixes the sense",
   passage="Because seed banks must remain viable for decades without power, engineers site them in "
           "permafrost, where the surrounding ground keeps temperatures low even if the cooling system "
           "fails&mdash;a design that is deliberately _____.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["redundant", "temporary", "compact", "ornamental"], answer="A",
   why="Ground that holds the temperature when the cooling system fails is a backup for a function "
       "already provided, which is what a redundant design means. The others describe duration, size and "
       "appearance."),

 dict(num="A-W6", skill="Words in Context", rule="underlined-word meaning in context",
   passage="Museums once treated conservation as a matter of arresting decay, and any change to an object "
           "was considered a loss. Newer approaches <u>temper</u> that view, accepting that some materials "
           "were designed to age and that halting the process can misrepresent what the maker intended.",
   stem="As used in the text, what does the word &ldquo;temper&rdquo; most nearly mean?",
   choices=["Harden", "Moderate", "Abandon", "Anticipate"], answer="B",
   why="The newer approaches soften the older absolute view rather than discarding it — they still "
       "conserve, but accept some aging. 'Abandon' overstates it and 'harden' reverses it."),

 # ----------------------------------------------------- Command of Evidence (3)
 dict(num="A-C1", skill="Command of Evidence", rule="the completion must match the table",
   table=("Germination Rate of Four Wildflower Species after Cold Storage",
          ["Species", "Stored 0 weeks", "Stored 4 weeks", "Stored 12 weeks"],
          [["Prairie smoke", "12%", "31%", "58%"],
           ["Wild bergamot", "44%", "47%", "49%"],
           ["Purple coneflower", "18%", "40%", "61%"],
           ["Butterfly weed", "9%", "26%", "55%"]]),
   passage="Many wildflower seeds germinate poorly when sown immediately after collection, and a period of "
           "cold, damp storage is often used to improve the rate. A grower wanted to know whether the "
           "benefit of longer storage is the same for every species, and measured germination for four "
           "species after 0, 4, and 12 weeks of cold storage. The results show that it is not: _____",
   stem="Which choice most effectively uses data from the table to complete the statement?",
   choices=["prairie smoke germinated at a lower rate than purple coneflower did at every storage duration.", "purple coneflower reached the highest germination rate of the four species after 12 weeks.", "every species germinated at a higher rate after 12 weeks of storage than after none.", "wild bergamot gained only 5 percentage points between 0 and 12 weeks, whereas butterfly weed gained 46."], answer="D",
   why="The claim is that the <em>benefit</em> of longer storage differs by species, so the completion "
       "must compare gains. Wild bergamot moves 44 to 49 while butterfly weed moves 9 to 55. The "
       "'every species germinated at a higher rate' choice states a pattern all four share, and the "
       "prairie-smoke and purple-coneflower choices compare levels rather than gains."),

 dict(num="A-C2", skill="Command of Evidence", rule="the hypothesis fixes which comparison counts",
   table=("Average Time to Locate a Buried Food Cache",
          ["Group", "Landmarks present (seconds)", "Landmarks removed (seconds)"],
          [["Adults", "31", "94"],
           ["Juveniles", "38", "45"]]),
   passage="Some birds that store food recover it months later, and researchers disagree about what guides "
           "the search. One proposal is that adult birds rely on landmarks near the cache while juveniles "
           "have not yet learned to use them. To test this, an experiment timed how long adults and "
           "juveniles took to locate a buried cache, first with nearby landmarks in place and then with "
           "those landmarks removed.",
   stem="Which choice best describes data from the table that support the proposal?",
   choices=["Juveniles took longer than adults did when landmarks were present.",
            "Both groups took longer to locate the cache once the landmarks had been removed.",
            "Removing the landmarks slowed adults from 31 to 94 seconds but slowed juveniles only from 38 to 45.",
            "Adults located the cache faster than juveniles did when landmarks were present."],
   answer="C",
   why="If adults rely on landmarks and juveniles do not, removing the landmarks should cost adults far "
       "more — which is exactly the 63-second penalty against the juveniles' 7. A, B and D are all true of "
       "the table but say nothing about who depends on the landmarks."),

 dict(num="A-C3", skill="Command of Evidence", rule="the finding must bear on the stated conclusion",
   passage="Sea otters eat large numbers of sea urchins, and sea urchins graze on kelp. Along stretches of "
           "coast where otters have returned after a long absence, kelp forests have expanded within a few "
           "years. A marine ecologist concluded that the otters&rsquo; return is what allowed the kelp to "
           "recover, rather than any change in water temperature over the same period.",
   stem="Which finding, if true, would most directly support the ecologist&rsquo;s conclusion?",
   choices=["Kelp grows more slowly in warmer water than in colder water.",
            "Along stretches of coast where water temperature changed by the same amount but otters did not return, kelp forests did not expand.",
            "Sea urchin populations along the coast have declined over the past decade.",
            "Sea otters were absent from the region for several decades before their recent return."],
   answer="B",
   why="The conclusion singles out the otters over temperature, so the support must hold temperature "
       "constant and vary the otters — which is what B does. C omits the cause of the urchin decline, and "
       "A and D restate background the passage already gives."),
]
