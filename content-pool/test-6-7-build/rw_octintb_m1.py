"""
October IntB, Section 1 Module 1 (Reading & Writing) — hand transcription.

Same method as `rw_octusb_m1.py`: read page by page from `pages/OctIntB/pNNN.jpeg`
and answer every question here rather than trusting the source key.

Page-to-question mapping is NOT 1:1 in this capture — the test-taker's screen
recording skipped four questions (2, 14, 20, 24 were never photographed), so the
`num` field records the on-screen question badge, not the page index.

Q21 is deliberately absent: it is already live in production as Test 5
RW_M1 Q17 (the Ann Quinby / "Kentucky played" Boundaries item).
"""

SOURCE = "OctIntB"
MODULE = "RW_M1"

QUESTIONS = [
 dict(num=1, skill="Words in Context",
   passage="The following text is adapted from Mary Seacole&rsquo;s 1857 autobiography <em>Wonderful "
           "Adventures of Mrs. Seacole in Many Lands</em>.</p><p>That journey across the Isthmus [of "
           "Panama], insignificant in distance as it was, was by no means an easy one. It seemed as if "
           "nature had determined to throw every <u>conceivable</u> obstacle in the way of those who "
           "should seek to join the two great oceans of the world.",
   stem="As used in the text, what does the word &ldquo;conceivable&rdquo; most nearly mean?",
   choices=["Imaginable", "Obvious", "Reasonable", "Dependable"], answer="A",
   why="'Every conceivable obstacle' means every obstacle that could be thought of. 'Obvious', "
       "'reasonable' and 'dependable' are all senses the word does not carry here."),

 dict(num=3, skill="Words in Context",
   passage="Often, the Nobel Prize in Chemistry is given to a single person, such as Theodore William "
           "Richards in 1914. But sometimes the Nobel Committee wants to reward work attributed to two "
           "or three individuals, in which case, the award is given _____. For instance, in 2020, "
           "Jennifer Doudna was among those awarded for &ldquo;the development of a method for genome "
           "editing.&rdquo;",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["retroactively", "jointly", "ceremoniously", "reluctantly"], answer="B",
   why="The contrast is between one recipient and 'two or three individuals', so the blank must mean "
       "shared. 'Jointly' is the only choice about sharing an award."),

 dict(num=4, skill="Words in Context",
   passage="The following text is adapted from the 1895 poem &ldquo;Ojistoh&rdquo; by Emily Pauline "
           "Johnson, a Kanienkahagen (Mohawk) writer also known as Tekahionwake.</p><p>I am Ojistoh, I "
           "am she, the wife<br/>Of him whose name <u>breathes</u> bravery and life<br/>And courage to "
           "the tribe who calls him chief.<br/>I am Ojistoh, his white star, and he<br/>Is land, and "
           "lake, and sky&mdash;and soul to me.",
   stem="As used in the text, what does the word &ldquo;breathes&rdquo; most nearly mean?",
   choices=["Imparts", "Renounces", "Assents", "Absorbs"], answer="A",
   why="His name gives bravery, life and courage <em>to</em> the tribe, so the verb must mean to "
       "give out. 'Absorbs' reverses the direction and the other two do not fit."),

 dict(num=5, skill="Words in Context",
   passage="The swordfish can swim very fast&mdash;up to 97 kilometers per hour (km/hr)&mdash;but it "
           "is significantly slower than the golden eagle, which can fly at speeds up to 320 km/hr. The "
           "difference between these speeds is largely _____ of the fact that the features that make "
           "flight possible do less to limit top speeds than the features suitable for swimming through "
           "water.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["a consequence", "an objective", "a repudiation", "an explanation"], answer="A",
   why="The stated fact about flight versus swimming is the cause and the speed gap is the effect, so "
       "the gap is 'a consequence of' it. 'An explanation of' reverses which one explains which."),

 dict(num=6, skill="Text Structure and Purpose",
   passage="Though John Crowley, author of <em>Engine Summer</em>, is perhaps not as well known as the "
           "most commercially successful American writers of the past fifty years, influential figures "
           "have championed his work, including the poet James Merrill and the literary critic Harold "
           "Bloom. In his afterword to Crowley&rsquo;s book <em>Little, Big</em>, Bloom praises the "
           "novel&rsquo;s adroit blend of what playwright Friedrich Schiller termed the naive and "
           "sentimental modes&mdash;while Schiller thought works could be classified as either naive "
           "(seeking to describe reality) or sentimental (seeking to develop ideas), <em>Little, Big</em> "
           "demonstrates that a work can be both.",
   stem="Which choice best states the main purpose of the text?",
   choices=["To argue that all writing must be classified as belonging to one of two categories",
            "To compare the work of a writer with the work of a poet who admired him",
            "To explain what inspired an author to write a particular work",
            "To present a reason why a literary critic is impressed by a certain novel"],
   answer="D",
   why="The text builds to why Bloom praises <em>Little, Big</em>: it blends two modes Schiller "
       "treated as exclusive. A inverts the point, B never compares Merrill's poetry with Crowley's "
       "novel, and nothing addresses Crowley's inspiration."),

 dict(num=7, skill="Text Structure and Purpose",
   passage="Community science, which involves professional scientists collaborating with amateur "
           "science enthusiasts to study a topic, is often an effective and engaging way to conduct "
           "research. It can allow people to assist with conservation efforts, spark youth interest in "
           "science, and increase the amount of data researchers can collect. This approach was "
           "essential to the success of a study by biologist Abbigail Merrill and colleagues of how "
           "butterfly color relates to flower choice, which included findings from hundreds of students "
           "and community members in northwestern Arkansas.",
   stem="Which choice best describes the overall structure of the text?",
   choices=["It introduces the topic of a scientific study, describes the study&rsquo;s importance, and then presents the study&rsquo;s results.",
            "It argues for a new approach to scientific research, comments on the public&rsquo;s opinion about the approach, and then describes how that approach was applied in a certain study.",
            "It identifies a particular approach to research, lists some benefits of that approach, and then mentions a study in which that approach was used.",
            "It describes the development of a type of scientific collaboration, shows how that type of collaboration has been used in a particular field of study, and then suggests future collaborative projects."],
   answer="C",
   why="Three sentences, three moves: name community science, list three benefits, cite the Merrill "
       "study. No results are given (A), no public opinion (B), and no future projects (D)."),

 dict(num=8, skill="Text Structure and Purpose",
   passage="The following text is adapted from Jerome K. Jerome&rsquo;s 1889 novel <em>Three Men in a "
           "Boat (To Say Nothing of the Dog)</em>.</p><p>We [people] are creatures of the sun. We love "
           "light and life. That is why we crowd into the towns and cities, and the country grows more "
           "and more deserted every year. In the sunlight&mdash;in the daytime, when Nature is alive "
           "and busy all around us, we like the open hill-sides and the deep woods well enough: but in "
           "the night, when our Mother Earth has gone to sleep, and left us waking, oh! the world seems "
           "so lonesome, and we get frightened, like children in a silent house. Then we sit and sob, "
           "and long for the gas-lit streets, and the sound of human voices, and the answering throb of "
           "human life.",
   stem="Which choice best states the main purpose of the text?",
   choices=["To convey that crowded areas can cause people to experience feelings of sadness",
            "To caution people not to be so quick to dismiss the natural beauty that can be found in rural areas",
            "To illustrate the idea that most people tend to prefer hillsides in the country to certain aspects of towns and cities",
            "To address common traits that motivate many people to choose to live in urban environments"],
   answer="D",
   why="'That is why we crowd into the towns and cities' announces the purpose: explaining the shared "
       "traits — love of light, fear of night loneliness — behind urban living. C reverses the "
       "preference the passage describes."),

 dict(num=9, skill="Central Ideas and Details",
   passage="&ldquo;Tomato&rdquo; is an example of a loanword&mdash;that is, a word that originated in "
           "one language and was later adopted by another. The word came to English indirectly from "
           "<em>tomate</em>, the Spanish word for the widely cultivated plant. Spanish had borrowed it "
           "from Nahuatl, an Indigenous language of Central Mexico, in which the word&rsquo;s original "
           "form is <em>tomatl</em>. &ldquo;Maize&rdquo; is also Indigenous in origin and entered "
           "English through Spanish. But in this case, the original source was Ta&iacute;no, a language "
           "of the Caribbean islands, in which the word for the corn plant is <em>mah&iacute;s</em>.",
   stem="The author makes which point about the Spanish language?",
   choices=["It has borrowed words from Indigenous languages and contributed words to them.",
            "Its contribution to English vocabulary roughly equals the collective contribution by Indigenous languages.",
            "It has served as a medium through which Indigenous languages have influenced English.",
            "It adopted Nahuatl and Ta&iacute;no words in approximately equal numbers."],
   answer="C",
   why="Both examples travel Indigenous language -> Spanish -> English, which is exactly the "
       "'medium' role. The text never says Spanish gave words back to Indigenous languages (A) and "
       "offers no counts to support B or D."),

 dict(num=11, skill="Command of Evidence",
   table=("Defensive Behavior and Reproductive Traits of Select Bird Species",
          ["Scientific name", "Common name", "Performs broken-wing display?",
           "Length of incubation (days)", "Incubation duty", "Maximum number of broods per year"],
          [["<em>Bucephala islandica</em>", "Barrow&rsquo;s goldeneye", "No", "34", "1 parent", "1"],
           ["<em>Numenius arquata</em>", "Eurasian curlew", "No", "30", "2 parents", "1"],
           ["<em>Eremophila alpestris</em>", "horned lark", "Yes", "12", "1 parent", "3"],
           ["<em>Zenaida asiatica</em>", "white-winged dove", "Yes", "14", "2 parents", "2"]]),
   passage="In an extensive review of existing literature, L&eacute;na de Framond and team cataloged "
           "the prevalence of broken-wing display&mdash;a defensive behavior observed in "
           "<em>Haematopus longirostris</em> (pied oystercatcher) and many other species&mdash;"
           "throughout the Aves class. Documentation of the display in 285 species across 52 families "
           "suggests the behavior likely evolved independently multiple times, prompting the team to "
           "consider ecological and life-history characteristics with hypothesized associations to the "
           "behavior&rsquo;s emergence, including traits related to reproduction investment and future "
           "reproduction potential. Based on their review of those traits, the team concluded that _____",
   stem="Which choice most effectively uses data from the table to complete the conclusion?",
   choices=["capacity for multiple broods, number of parental incubators, and incubation duration are equally associated with the use of broken-wing display.",
            "incubation duration and capacity for multiple broods are more strongly associated with the use of broken-wing display than the number of parental incubators is.",
            "broken-wing display is most often observed in species with less opportunity to reproduce in a year due to longer incubation periods.",
            "among species with more than one parental incubator, the use of broken-wing display is associated with greater incubation duration."],
   answer="B",
   why="In the table the two display species have short incubation (12, 14) and multiple broods "
       "(3, 2) while the two non-display species have long incubation (34, 30) and one brood — both "
       "traits track the display perfectly. Incubation duty does not: each group contains one "
       "1-parent and one 2-parent species. C reverses the incubation relationship, and D is false "
       "(among the 2-parent species the display one has the shorter incubation)."),

 dict(num=12, skill="Command of Evidence",
   passage="Water flowing around an obstruction creates vortices (patterns of swirls) of varying size; "
           "by detecting the vortices, fish can determine the size and position of the obstruction. "
           "Testing by Yuzo R. Yanagisuru, Otar Akanyeti, and James C. Liao using models of three head "
           "shapes&mdash;narrow (low ratio of width to length), intermediate, and wide (high ratio of "
           "width to length)&mdash;showed that for medium-sized vortices, fish with wide heads would be "
           "least able to distinguish between vortices and general turbulence in the water. A second "
           "research team has therefore hypothesized that in low-visibility conditions, wider-headed "
           "fish will be less likely than narrower-headed fish to detect obstructions.",
   stem="Which finding, if true, would most directly support the second research team&rsquo;s hypothesis?",
   choices=["A study using obstructions that created medium-sized vortices in low-visibility conditions found that some specimens of dusky smooth-hound (<em>Mustelus canis</em>), which has a relatively narrow head, bumped into the obstructions more often than other specimens of the same fish did.",
            "A study using obstructions that created medium-sized vortices in low-visibility conditions found that the wider-headed bristlemouth (<em>Chaetostoma yurubiense</em>) bumped into obstructions more often than the narrower-headed dusky smooth-hound (<em>Mustelus canis</em>) did.",
            "A study using obstructions that created medium-sized vortices in low-visibility conditions found that the narrower-headed dusky smooth-hound (<em>Mustelus canis</em>) bumped into the obstructions just as often as the wider-headed bristlemouth (<em>Chaetostoma yurubiense</em>) did.",
            "A study using obstructions that created medium-sized vortices in low-visibility conditions found that the bristlemouth (<em>Chaetostoma yurubiense</em>), which has a relatively wide head, bumped into more than half of the obstructions."],
   answer="B",
   why="The hypothesis is comparative — wider-headed fish detect obstructions less well than "
       "narrower-headed ones — so the supporting finding must compare the two head shapes and favour "
       "the narrow one. A compares members of one narrow-headed species, C finds no difference, and "
       "D reports a wide-headed rate with nothing to compare it against."),

 dict(num=13, skill="Command of Evidence",
   passage="<em>Cane</em> is a 1923 novel by Jean Toomer. In one portion of the novel, Toomer "
           "establishes a contrast between the narrator&rsquo;s attitude toward life and the attitude "
           "of the narrator&rsquo;s love interest, Avey, writing, _____",
   stem="Which quotation from <em>Cane</em> most effectively illustrates the claim?",
   choices=["&ldquo;Avey was as silent as those great trees whose tops we looked down upon. She has always been like that. At least, to me.&rdquo;",
            "&ldquo;A band in one of the buildings a fair distance off was playing a march. I wished they would stop. Their playing was like a tin spoon in one&rsquo;s mouth.&rdquo;",
            "&ldquo;[Avey would] smile appreciation, but it was an impersonal smile, never for me.&rdquo;",
            "&ldquo;As time went on, [Avey&rsquo;s] indifference to things began to pique me; I was ambitious. I left [our small hometown] earlier than she did.&rdquo;"],
   answer="D",
   why="Only D names both attitudes and sets them against each other: Avey's indifference versus the "
       "narrator's ambition. A and C describe Avey alone, and B is about a band."),

 dict(num=15, skill="Inferences",
   passage="Pigments give paints and dyes their color. Ocher is a mineral-based pigment used to make "
           "several colors, including red. Red ocher gets its color from iron oxide. Pigments can also "
           "be plant-based; plant-based pigments contain a high level of carbon. In a 2023 study, "
           "archaeologists tested the red pigment on decorated beads made by members of the Natufian "
           "culture approximately 15,000 years ago. The test showed that the pigment found on several "
           "beads contained no iron but had a high level of carbon. This finding led the researchers to "
           "conclude that _____",
   stem="Which choice most logically completes the text?",
   choices=["the Natufian beadmakers used plant-based pigments rather than ocher to decorate some of the beads examined in the study.",
            "the pigments used by the Natufian beadmakers likely came from plants because ocher was difficult to find.",
            "the Natufian beadmakers preferred to use plant-based pigments because they are much brighter than mineral-based pigments are.",
            "the Natufian beads examined in the study are the oldest surviving examples of the use of plant-based pigments for decorating beads."],
   answer="A",
   why="No iron rules out red ocher and high carbon points to a plant source — exactly A. B, C and D "
       "add claims about availability, brightness and record-setting age that the text never supports."),

 dict(num=16, skill="Boundaries",
   passage="Works by Rafael Soriano and Rupert Garc&iacute;a were featured in the Smithsonian American "
           "Art Museum&rsquo;s exhibition <em>Our America: The Latino Presence in American Art</em>. "
           "This 2013 exhibition celebrated the diverse achievements _____ artists of Latin American "
           "descent.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["of;", "of:", "of,", "of"], answer="D",
   why="'The diverse achievements of artists of Latin American descent' is a single noun phrase; no "
       "punctuation belongs between a preposition and its object."),

 dict(num=17, skill="Boundaries",
   passage="On December 2, 1992, the space shuttle <em>Discovery</em> blasted off into space, "
           "commencing Mission _____ seven days and seven hours, the mission ended when the shuttle "
           "landed at Edwards Air Force Base in California.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["STS-53, lasting", "STS-53, it lasted", "STS-53 lasting", "STS-53. Lasting"],
   answer="D",
   why="'...blasted off into space, commencing Mission STS-53' and 'the mission ended when the "
       "shuttle landed...' are both independent clauses, so a sentence boundary is required. A and C "
       "leave the second clause spliced on with a comma, and B splices two clauses outright."),

 dict(num=18, skill="Form, Structure, and Sense",
   passage="Trade was vital to the Srivijaya Empire, which reigned in Southeast Asia from around 600 CE "
           "to 1200 CE. Its people _____ tin, medicines, and wood to sell to neighboring societies. In "
           "exchange, they received valuable items, such as spices, silk, and porcelain.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["are producing", "produce", "produced", "will produce"], answer="C",
   why="The surrounding sentences are in the simple past ('was vital', 'they received') about an "
       "empire that ended in 1200 CE, so the past tense 'produced' is required."),

 dict(num=19, skill="Form, Structure, and Sense",
   passage="The Globe Theatre in London is a reconstruction of the famed venue where many of "
           "Shakespeare&rsquo;s plays were first performed. In 1613, a prop cannon _____ during a "
           "performance and ignited the Globe&rsquo;s thatched roof. No one was hurt, but in two hours "
           "the original Globe was gone.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["has malfunctioned", "malfunctioned", "will malfunction", "malfunctions"], answer="B",
   why="'In 1613' fixes a completed past event, and the blank is coordinated with the simple past "
       "'ignited'. Only 'malfunctioned' matches."),

 dict(num=22, skill="Transitions",
   passage="Famous for its four-degree tilt, the leaning Garisenda Tower is a popular attraction in "
           "Bologna&rsquo;s city center. However, measurements taken in 2023 showed that the tower was "
           "rotating in a concerning way. _____ city officials closed the area around the tower so "
           "experts could explore solutions to stabilize the historical twelfth-century structure.",
   stem="Which choice completes the text with the most logical transition?",
   choices=["In comparison,", "As a result,", "For example,", "Similarly,"], answer="B",
   why="Closing the area is the response to the concerning measurements, so the link is causal."),

 dict(num=23, skill="Transitions",
   passage="When languages are no longer spoken, they are considered extinct. _____ the Umbrian "
           "language went extinct around the first century BCE, though it was once widely spoken in "
           "parts of central Italy.",
   stem="Which choice completes the text with the most logical transition?",
   choices=["Therefore,", "Admittedly,", "For example,", "In conclusion,"], answer="C",
   why="Umbrian is one instance of the general definition in the first sentence — an illustration, "
       "not a consequence, concession or summary."),

 dict(num=25, skill="Rhetorical Synthesis",
   passage="While researching a topic, a student has taken the following notes:</p><ul>"
           "<li>Dinosaur fossil specimens can be found at science museums all over the world.</li>"
           "<li>Many dinosaur fossil specimens are given nicknames.</li>"
           "<li>The Great Plains Dinosaur Museum and Field Station in Malta, Montana, houses a dinosaur fossil specimen nicknamed Roberta.</li>"
           "<li>Roberta lived in the Late Cretaceous period, which ended more than 65 million years ago.</li>"
           "<li>It is a member of the genus <em>Brachylophosaurus</em>.</li></ul>",
   stem="The student wants to provide an example of a dinosaur fossil specimen&rsquo;s nickname. Which "
        "choice most effectively uses relevant information from the notes to accomplish this goal?",
   choices=["Nicknames are given to many dinosaur fossil specimens, including one housed at a museum in Malta, Montana.",
            "Dinosaur fossil specimens can be found at museums all over the world, and many of these specimens are given nicknames.",
            "Roberta is the nickname of a <em>Brachylophosaurus</em> fossil specimen housed at the Great Plains Dinosaur Museum and Field Station in Malta, Montana.",
            "A <em>Brachylophosaurus</em> fossil specimen from the Late Cretaceous period, which ended more than 65 million years ago, is housed at the Great Plains Dinosaur Museum and Field Station."],
   answer="C",
   why="Only C actually states a nickname ('Roberta'). A and B say nicknames exist without giving "
       "one, and D omits the nickname entirely."),

 dict(num=26, skill="Rhetorical Synthesis",
   passage="While researching a topic, a student has taken the following notes:</p><ul>"
           "<li>The A.M. Turing Award is a prestigious award given for &ldquo;major contributions of lasting importance to computing.&rdquo;</li>"
           "<li>Manuel Blum won the award in 1995 for contributions to the foundations of computational complexity theory.</li>"
           "<li>Raj Reddy won the award in 1994 for pioneering the development of large-scale artificial intelligence systems.</li></ul>",
   stem="The student wants to emphasize the order in which Manuel Blum and Raj Reddy won the A.M. "
        "Turing Award. Which choice most effectively uses relevant information from the notes to "
        "accomplish this goal?",
   choices=["Manuel Blum and Raj Reddy both won the A.M. Turing Award, which is given for &ldquo;major contributions of lasting importance to computing.&rdquo;",
            "Raj Reddy won the A.M. Turing Award in 1994; Manuel Blum won it later, in 1995.",
            "In 1995, Manuel Blum won the A.M. Turing Award for contributions to the foundations of computational complexity theory.",
            "It was in 1994 that Raj Reddy won the A.M. Turing Award."],
   answer="B",
   why="Only B mentions both men and marks the sequence explicitly with 'later'. C and D each cover "
       "one winner, and A gives no dates at all."),

 dict(num=27, skill="Rhetorical Synthesis",
   passage="While researching a topic, a student has taken the following notes:</p><ul>"
           "<li>Lighthouses send out crucial light signals to help ships and other watercraft navigate at night.</li>"
           "<li>Before automation, lighthouses were run by lighthouse keepers.</li>"
           "<li>Catherine A. Moore was the lighthouse keeper at Black Rock Harbor Light in Connecticut.</li>"
           "<li>She held this position from 1817 to 1878.</li>"
           "<li>Laura J. Hecox was the lighthouse keeper at Santa Cruz Light in California.</li>"
           "<li>She held this position from 1883 to 1917.</li></ul>",
   stem="The student wants to emphasize the order in which the two lighthouse keepers began their "
        "careers. Which choice most effectively uses relevant information from the notes to accomplish "
        "this goal?",
   choices=["Catherine A. Moore&rsquo;s career as a lighthouse keeper ended in 1878, whereas Laura J. Hecox&rsquo;s ended in 1917.",
            "Laura J. Hecox began her career as a lighthouse keeper years after Catherine A. Moore did.",
            "From 1817 to 1878, the nighttime waters of Connecticut were more navigable thanks to lighthouse keepers Laura J. Hecox and Catherine A. Moore.",
            "Before automation, lighthouse keepers like Catherine A. Moore and Laura J. Hecox were crucial to ensuring safe navigation for watercraft."],
   answer="B",
   why="The goal is when each <em>began</em>: Moore in 1817, Hecox in 1883. B states that order. A "
       "compares end dates instead, C wrongly places Hecox in Connecticut, and D has no dates."),
]

# Never captured by the source screen recording — the badge numbers simply skip:
NOT_CAPTURED = [2, 14, 20, 24]

# Transcribed but deliberately not shipped:
DROPPED = {
 10: "Template repeat. The passage is the same park-use study design already live in Test 5 "
     "RW_M2_HARD Q5 — same researchers (Mika R. Moran, Daniel A. Rodriguez and colleagues), same "
     "two-city survey with percentages, and the same 'given that access was much lower..., the "
     "difference can't be explained by access' turn. Only the cities differ (Panama City and "
     "Fortaleza here, Mexico City and Buenos Aires there). A student who has taken Test 5 would "
     "recognise it, so it is rejected rather than shipped.",
 21: "Already live in production as Test 5 RW_M1 Q17 (Ann Quinby / 'Kentucky played').",
}
