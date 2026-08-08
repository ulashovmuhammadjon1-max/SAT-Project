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
