"""
August USE (Section 1 Reading & Writing) — hand transcription.

A different administration from the October set, so it does not carry the
October cross-form duplication — but a lexical check found 24 of its 54 captured
pages already exist, 19 in Tests 1-5 and 5 in the October material transcribed
for this build. Those pages were skipped without being read. Everything below
was additionally checked by eye for *template* duplication, which the lexical
check cannot catch.

Transcription order was writing-domain first (Boundaries, Form/Structure/Sense,
Transitions, Rhetorical Synthesis), because writing is the binding constraint
for six modules: they need ~78 writing questions and the October papers yielded
only 36.

`num` is the on-screen question badge.
"""

SOURCE = "AugUSE"
MODULE = "RW"

QUESTIONS = [
 dict(num=3, skill="Words in Context",
   passage="One way to _____ the importance of a scholar&rsquo;s research is to track how often other "
           "scholars refer to that research. For example, Yale University economist Xiaohong Chen, who "
           "studies statistical methods in economics, is among the world&rsquo;s most frequently cited "
           "researchers in her field, indicating that her work has been quite significant.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["increase", "measure", "diminish", "vary"], answer="B",
   why="Citation counts are offered as a way of gauging importance, and the example ends by saying "
       "the count 'indicat[es]' significance. Tracking citations does not change importance (A, C)."),

 dict(num=4, skill="Words in Context",
   passage="The discoverers of the minor planet 1227 Geranium named it after the plant genus that "
           "includes cranesbills. Most of the recently discovered minor planets, however, are given "
           "only an identification number, largely due to there being over 500,000 such bodies known at "
           "present, which makes the already challenging task of finding a unique name for each nearly "
           "_____.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["feasible", "unnecessary", "substantial", "insurmountable"], answer="D",
   why="'Already challenging' plus 500,000 bodies pushes the task past difficult, and 'nearly _____' "
       "wants a limit word. 'Feasible' reverses it and the other two do not describe a task's "
       "difficulty."),

 dict(num=5, skill="Text Structure and Purpose",
   passage="<em>The Last Report on the Miracles at Little No Horse</em> is a 2001 novel by Ojibwe "
           "writer Louise Erdrich. It explores how historical events affect families on a reservation "
           "in rural North Dakota. <em>The Last Report on the Miracles at Little No Horse</em> is "
           "typical of Erdrich&rsquo;s work. Her writing usually focuses on portrayals of everyday life "
           "in Ojibwe communities. Yet some of her novels have fantastical plots and take place outside "
           "Ojibwe communities. <u>For example, her 1991 novel <em>The Crown of Columbus</em> is "
           "essentially adventure fiction, and the thrilling events in its plot are set largely on a "
           "Caribbean island.</u>",
   stem="Which choice best describes the function of the underlined sentence in the text as a whole?",
   choices=["It recommends that readers avoid a particular novel by Erdrich.",
            "It lists the many similarities between two novels by Erdrich.",
            "It offers an example of a novel that differs from most of Erdrich&rsquo;s work.",
            "It discusses what inspired Erdrich to write one of her novels."],
   answer="C",
   why="The underlined sentence begins 'For example' and follows 'Yet some of her novels have "
       "fantastical plots and take place outside Ojibwe communities' — it illustrates the exception, "
       "not similarities (B)."),

 dict(num=8, skill="Central Ideas and Details",
   passage="Can field mustard plants grow on Mars? Can pea plants? You might think the answer to these "
           "questions is obviously no, but researchers in the Netherlands recently showed that the "
           "seeds of many common plant species can germinate in soil designed to simulate Martian "
           "conditions, as long as water is supplied. In fact, some species actually did <em>better</em> "
           "in Martian soil than in Earth soil: 30 percent of field mustard seeds sprouted when planted "
           "in simulated Martian soil, compared with 4 percent that did when planted in soil from their "
           "home planet.",
   stem="According to the text, what percentage of field mustard seeds planted in Martian soil sprouted?",
   choices=["18 percent", "30 percent", "100 percent", "5 percent"], answer="B",
   why="Stated directly. The 4 percent figure is the Earth-soil comparison, and the other two numbers "
       "do not appear."),

 dict(num=9, skill="Command of Evidence",
   passage="<em>Poems</em> is an 1895 collection of poetry by Frances E.W. Harper. In one of "
           "Harper&rsquo;s poems, the speaker declares her intention to create art that has a universal "
           "appeal across generations, saying, _____",
   stem="Which quotation from <em>Poems</em> most effectively illustrates the claim?",
   choices=["&ldquo;Our world, so worn and weary, / Needs music, pure and strong, / To hush the jangle and discords / Of sorrow, pain, and wrong.&rdquo; (from &ldquo;Songs for the People&rdquo;)",
            "&ldquo;Let me make the songs for the people, / Songs for the old and young; / Songs to stir like a battle-cry / Wherever they are sung.&rdquo; (from &ldquo;Songs for the People&rdquo;)",
            "&ldquo;God bless our native land, / Land of the newly free, / Oh may she ever stand / For truth and liberty.&rdquo; (from &ldquo;God Bless Our Native Land&rdquo;)",
            "&ldquo;My mother&rsquo;s kiss, my mother&rsquo;s kiss, / I feel its impress now; / As in the bright and happy days / She pressed it on my brow.&rdquo; (from &ldquo;My Mother&rsquo;s Kiss&rdquo;)"],
   answer="B",
   why="B has all three parts of the claim: the speaker's intention ('Let me make'), the reach across "
       "generations ('the old and young'), and universality ('Wherever they are sung'). A describes "
       "what the world needs rather than her intention, and C and D are on other subjects entirely."),

 dict(num=11, skill="Command of Evidence",
   passage="<em>The Underdogs</em> is a 1915 novel by Mariano Azuela, originally written in Spanish. In "
           "the novel, Azuela depicts a traveling group of soldiers as having a renewed sense of agency "
           "and authority as they set off on a new stage of their journey: _____",
   stem="Which quotation from a translation of <em>The Underdogs</em> most effectively illustrates the claim?",
   choices=["&ldquo;The sonorous, joyful bells rang again. From within the church, the honeyed voices of a female chorus rose melancholy and grave.&rdquo;",
            "&ldquo;All day long [the soldiers] rode through the canyon, up and down the steep, round hills, dirty and bald as a man&rsquo;s head, hill after hill in endless succession. At last, late in the afternoon, they descried several stone church towers in the heart of a bluish ridge, and, beyond, the white road with its curling spirals of dust and its gray telegraph poles.&rdquo;",
            "&ldquo;The men threw out their chests as if to breathe the widening horizon, the immensity of the sky, the blue from the mountains and the fresh air, redolent with the various odors of the sierra. They spurred their horses to a gallop as if in that mad race they laid claims of possession to the earth.&rdquo;",
            "&ldquo;Before Juchipila was lost from sight, Valderrama got off his horse, bent down, kneeled, and gravely kissed the ground.&rdquo;"],
   answer="C",
   why="'Laid claims of possession to the earth' is the authority and 'spurred their horses to a "
       "gallop' the agency, both at the start of a new stretch of road. B describes the same journey "
       "but with no sense of renewal, and A and D are about other characters and moods."),

 dict(num=17, skill="Form, Structure, and Sense",
   passage="In her work as a sociocultural anthropologist, L&iacute;via Barbosa studies food and "
           "sociability in contemporary Brazil&mdash;namely, how common Brazilian foods like tareco (a "
           "disk-shaped biscuit) and coxinha (a stuffed fried dough) _____ as central mechanisms in "
           "building social relationships, values, and identities.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["is functioning", "functions", "has functioned", "function"], answer="D",
   why="The subject of the blank is the plural 'foods like tareco and coxinha', and the surrounding "
       "verbs are simple present ('studies'), so the plural present 'function' is required."),

 dict(num=18, skill="Boundaries",
   passage="As a behavioral economist, Ai Hisano of Kyoto University recognizes that people sometimes "
           "make irrational economic decisions. Hisano&rsquo;s research can thus address anomalies that "
           "neoclassical economic _____ assume that people are consistently rational "
           "decision-makers&mdash;cannot explain.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["models which&mdash;", "models which", "models&mdash;which", "models, which"], answer="C",
   why="A dash already closes the aside before 'cannot explain', so the blank must open it with the "
       "matching dash: 'anomalies that neoclassical economic models&mdash;which assume...&mdash;cannot "
       "explain'. A puts the dash on the wrong side of 'which', and B and D leave the closing dash "
       "unpaired."),

 dict(num=19, skill="Boundaries",
   passage="During the decades-long movement to codify the rights of Latinos in the US, certain events "
           "were pivotal: the founding of labor rights group El Teatro Campesino in _____ <em>Serna v. "
           "Portales Schools</em> court decision in 1974, which affirmed the rights of Latino students, "
           "is another such event.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["1965, for one, the", "1965, for one. The", "1965 for one, the", "1965. For one, the"],
   answer="B",
   why="'The founding... in 1965, for one' and 'The Serna v. Portales Schools court decision... is "
       "another such event' are both independent clauses and need a sentence boundary. A and C splice "
       "them, and D detaches 'for one' from the clause it qualifies and attaches it to the second "
       "sentence, where 'another such event' already does that work."),

 dict(num=21, skill="Transitions",
   passage="In Argentina, the Chamber of Deputies is elected via a proportional representation (PR) "
           "system. In PR elections, votes are cast (not for specific candidates, as they are in "
           "single-member plurality systems, but for political parties) and then tabulated; _____ each "
           "qualifying party is awarded a number of seats proportional to the number of votes it "
           "received.",
   stem="Which choice completes the text with the most logical transition?",
   choices=["second of all,", "in fact,", "by contrast,", "accordingly,"], answer="D",
   why="Awarding seats in proportion to the votes counted is the consequence of the tabulation just "
       "described. 'Second of all' needs a first, there is no contrast with the preceding clause (C), "
       "and nothing is being intensified (B)."),

 dict(num=23, skill="Transitions",
   passage="Firefly luciferase (Fluc) is a distinctly evolved enzyme that can oxidize a substrate "
           "called D-luciferin to induce bioluminescence and can act as a fatty acyl-CoA synthetase "
           "(ACS) enzyme, a class of enzyme present in all insects. _____ Fluc is a bifunctional enzyme "
           "whose presence indicates an insect is capable of emitting light; in contrast, the presence "
           "of ACS alone would be insufficient for determining bioluminescence.",
   stem="Which choice completes the text with the most logical transition?",
   choices=["In fact,", "Moreover,", "That is,", "Nevertheless,"], answer="C",
   why="'Bifunctional' restates the two capabilities the first sentence has just listed, so the "
       "second sentence explains rather than adds (B), intensifies (A) or contrasts (D)."),

 dict(num=25, skill="Rhetorical Synthesis",
   passage="While researching a topic, a student has taken the following notes:</p><ul>"
           "<li>The Paralympic Games are a series of international sporting events involving athletes with an impairment.</li>"
           "<li>Swimming has been an event at the Paralympics since 1960.</li>"
           "<li>Mike Kenny competed as a Paralympic swimmer from 1976 to 1988.</li>"
           "<li>He won eighteen medals.</li>"
           "<li>Of these, sixteen were gold medals, which indicate a first-place finish.</li></ul>",
   stem="Which choice most effectively uses information from the given sentences to emphasize the "
        "number of medals won by Kenny?",
   choices=["An accomplished Paralympian with multiple gold medal wins, Mike Kenny competed as a swimmer from 1976 to 1988.",
            "During his career as a Paralympic swimmer, Mike Kenny earned a total of eighteen medals, sixteen of which were gold.",
            "Swimming, a sport in which Mike Kenny took home sixteen gold medals, has been an event at the Paralympic Games since 1960.",
            "Mike Kenny competed at the Paralympic Games, a series of international sporting events."],
   answer="B",
   why="Only B gives both counts and foregrounds them ('a total of eighteen medals, sixteen of which "
       "were gold'). A says 'multiple' without a number, C buries one figure inside a fact about the "
       "sport, and D gives none."),

 dict(num=26, skill="Rhetorical Synthesis",
   passage="While researching a topic, a student has taken the following notes:</p><ul>"
           "<li>Louis Ballard was a classical composer and citizen of the Quapaw Tribe.</li>"
           "<li>His compositions synthesize Western classical music with elements of various Native musical traditions.</li>"
           "<li>Ballard&rsquo;s classical piece <em>Katcina Dances</em> features traditional Hopi songs.</li>"
           "<li>Ballard&rsquo;s classical piece <em>Fantasy Aborigine No. 3</em> incorporates a Tewa seashell rattle.</li></ul>",
   stem="The student wants to emphasize a difference between the two compositions. Which choice most "
        "effectively uses relevant information from the notes to accomplish this goal?",
   choices=["<em>Katcina Dances</em> and <em>Fantasy Aborigine No. 3</em> are two compositions written by Ballard, a classical music composer.",
            "In his two compositions <em>Katcina Dances</em> and <em>Fantasy Aborigine No. 3</em>, Ballard blends elements of various Native musical traditions, such as Indigenous songs or instruments, with Western classical music.",
            "Ballard has different approaches to blending Western classical music with elements of various Native musical traditions, such as using Indigenous songs and instruments in his compositions.",
            "While both compositions integrate various Native musical traditions, <em>Katcina Dances</em> does so by featuring traditional Hopi songs and <em>Fantasy Aborigine No. 3</em> does so by incorporating a Tewa seashell rattle."],
   answer="D",
   why="D names what each piece does differently — Hopi songs versus a Tewa seashell rattle — against "
       "a shared background. A and B stress what the two have in common, and C asserts a difference "
       "without saying what it is."),

 dict(num=27, skill="Rhetorical Synthesis",
   passage="While researching a topic, a student has taken the following notes:</p><ul>"
           "<li>The Clovis First hypothesis proposes that ancient humans known as Clovis were the first to populate North America.</li>"
           "<li>The Clovis arrived around 13,000 years ago.</li>"
           "<li>Stone tools found at the Saltville site in Virginia date to approximately 16,000 years ago.</li>"
           "<li>These items support the idea that humans were present in North America before the Clovis population arrived.</li>"
           "<li>More than a dozen North American sites containing pre-Clovis items have been identified.</li></ul>",
   stem="The student wants to explain the implications of the discovery at the Saltville site. Which "
        "choice most effectively uses relevant information from the notes to accomplish this goal?",
   choices=["It is the contention of the Clovis First hypothesis that the Clovis, an ancient human population, were the first to inhabit North America, arriving around 13,000 years ago.",
            "Located in Virginia, Saltville is one of more than a dozen North American sites where pre-Clovis items have been discovered.",
            "The approximately 16,000-year-old stone tools found at Saltville, a site in Virginia, should not be overlooked: they have important implications for the Clovis First hypothesis.",
            "Contrary to the Clovis First hypothesis, the approximately 16,000-year-old stone tools found at Saltville suggest that humans were in North America before the Clovis arrived."],
   answer="D",
   why="Only D states what the discovery implies — humans predating the Clovis, against the "
       "hypothesis. C asserts that there are implications without naming them, A describes only the "
       "hypothesis, and B only locates the site."),

 # --- Module 2 (pages p029-p055 hold Q1-Q27). `num` is prefixed to keep it
 # distinct from the Module 1 badges above.
 dict(num="M2-19", skill="Boundaries",
   passage="Joy Williams&rsquo;s essay on &ldquo;cenote,&rdquo; a term referring to a deep sinkhole "
           "containing a pool of water, is just one of many essays included in <em>Home Ground: A Guide "
           "to the American _____ by Barry Lopez and Debra Gwartney, the book celebrates the rich "
           "language used to describe the landscape of North America.",
   choices_note="The book title's closing italics fall inside the answer choices.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["<em>Landscape</em>, edited", "<em>Landscape</em> edited", "<em>Landscape</em>. Edited",
            "<em>Landscape</em> and edited"],
   answer="C",
   why="'Joy Williams's essay... is just one of many essays included in <em>Home Ground</em>' and "
       "'the book celebrates the rich language...' are both independent clauses, so a sentence "
       "boundary is required; the second then opens with the participial phrase 'Edited by Barry "
       "Lopez and Debra Gwartney'. A, B and D all leave the two clauses spliced by the comma before "
       "'the book'."),

 dict(num="M2-20", skill="Form, Structure, and Sense",
   passage="Most US states and territories have had at least one woman serve as governor. In Nebraska, "
           "for example, Governor Kay A. Orr took office on January 9, 1987. In fact, the number of "
           "states and territories that have had only male governors _____ almost every year.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["shrinks", "shrink", "are shrinking", "have been shrinking"], answer="A",
   why="The subject is the singular 'the number' (not the plural 'states and territories' inside the "
       "modifier), and 'almost every year' calls for the simple present. Only 'shrinks' is both "
       "singular and simple present."),

 dict(num="M2-23", skill="Transitions",
   passage="Joseph Goodrich was an outspoken abolitionist whose Wisconsin home was a stop on the "
           "underground railroad (the network of people and places that some enslaved people used to "
           "escape to freedom). _____ supporters of the railroad were secretive about their antislavery "
           "views. By and large, they were vocal abolitionists like Goodrich.",
   stem="Which choice completes the text with the most logical transition?",
   choices=["Occasionally,", "For example,", "Accordingly,", "However,"], answer="A",
   why="The sentence that follows — 'By and large, they were vocal abolitionists' — marks secrecy as "
       "the exception, so the blank must limit the claim's frequency. Goodrich was outspoken, so "
       "secrecy is neither an example of (B) nor a consequence of (C) the first sentence."),

 dict(num="M2-24", skill="Transitions",
   passage="The work of contemporary Asian American poet John Yau often incorporates references to "
           "other poems and works of visual art. Typically, these allusive gestures are subtle, "
           "recognized by only the most attentive of Yau&rsquo;s readers. In his 2013 poem &ldquo;Further "
           "Adventures in Monochrome,&rdquo; _____ Yau explicitly identifies a particular "
           "artwork&mdash;Yves Klein&rsquo;s 1960 painting <em>Silence is Golden</em>&mdash;as the "
           "poem&rsquo;s inspiration.",
   stem="Which choice completes the text with the most logical transition?",
   choices=["though,", "fittingly,", "similarly,", "for example,"], answer="A",
   why="'Explicitly identifies' is the opposite of the 'typically... subtle' allusions just described, "
       "so the 2013 poem is an exception, not an illustration (D) or a parallel case (C)."),
]

DROPPED = {
 16: "Same template as OctIntB M1 Q18, already transcribed for this build: 'Trade [with other "
     "societies] was vital to the X Empire, which reigned in [region] from around [year] CE to "
     "[year] CE. Its people ...' followed by a past-tense verb-form choice. Byzantine Empire and "
     "'items that _____ greatly in demand' here; Srivijaya Empire and 'Its people _____ tin, "
     "medicines, and wood' there.",
 20: "Passage reuse. Module 1 Q20 is built on the same Sei Shonagon <em>Pillow Book</em> 'Splendid "
     "Things' list already live in Test 5 RW_M1 as an Oct IntB top-up, sharing the "
     "'grape-colored fabric' and 'snow-covered garden' details and the tenth-century-courtly-life "
     "framing. The question tested differs (a colon boundary here, subject-verb agreement there), "
     "but a student who has taken Test 5 would be reading the same passage again.",
}

# Pages skipped without reading because a lexical check matched them to a question already live in
# production or already transcribed for this build. Recorded so a later session does not re-check
# them: AugUSE p002, p003, p007, p008, p016, p023, p025, p029, p030, p032, p033, p034, p035, p037,
# p038, p040, p041, p045, p046, p047, p050, p051, p054, p055.
SKIPPED_AS_DUPLICATE_PAGES = [2, 3, 7, 8, 16, 23, 25, 29, 30, 32, 33, 34, 35, 37, 38, 40, 41, 45,
                              46, 47, 50, 51, 54, 55]
