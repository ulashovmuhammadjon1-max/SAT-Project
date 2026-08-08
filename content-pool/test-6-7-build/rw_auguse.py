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
]

DROPPED = {
 16: "Same template as OctIntB M1 Q18, already transcribed for this build: 'Trade [with other "
     "societies] was vital to the X Empire, which reigned in [region] from around [year] CE to "
     "[year] CE. Its people ...' followed by a past-tense verb-form choice. Byzantine Empire and "
     "'items that _____ greatly in demand' here; Srivijaya Empire and 'Its people _____ tin, "
     "medicines, and wood' there.",
}

# Pages skipped without reading because a lexical check matched them to a question already live in
# production or already transcribed for this build. Recorded so a later session does not re-check
# them: AugUSE p002, p003, p007, p008, p016, p023, p025, p029, p030, p032, p033, p034, p035, p037,
# p038, p040, p041, p045, p046, p047, p050, p051, p054, p055.
SKIPPED_AS_DUPLICATE_PAGES = [2, 3, 7, 8, 16, 23, 25, 29, 30, 32, 33, 34, 35, 37, 38, 40, 41, 45,
                              46, 47, 50, 51, 54, 55]
