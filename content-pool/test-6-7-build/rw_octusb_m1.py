"""
October USB, Section 1 Module 1 (Reading & Writing) — hand transcription.

Read page by page from the source screen captures (`pages/OctUSB/pNNN.jpeg`,
where page number == question number). OCR is not used for anything but a
cross-check: it garbles the answer choices badly ("solidified" -> "soliditiea").

**Answers here are mine, derived from the question, not taken from the source.**
Test 5 established that this publisher's R&W keys are wrong often enough to be
useless (7 of 18 spot-checked disagreed with a careful reading), while the same
papers' Math keys were clean. Every `answer` below carries the reasoning that
produced it in `why`.

`skill` uses the CLAUDE.md block names, which map to Domain/Skill codes at
assembly time.
"""

SOURCE = "OctUSB"
MODULE = "RW_M1"

QUESTIONS = [
 dict(num=1, skill="Words in Context",
   passage="The following text is adapted from John Matheus&rsquo;s 1925 short story &ldquo;Fog.&rdquo; "
           "A train has stopped at a station, where heavy fog has set in.</p><p>The little conductor "
           "stood on tiptoe in an effort to keep one hand on the signal rope, craning his neck in a "
           "vain and dissatisfied endeavor to pierce the miasma of the fog. The motorman chafed in "
           "his box, thinking of the drudging lot of the laboring man. He <u>registered</u> discontent.",
   stem="As used in the text, what does the word &ldquo;registered&rdquo; most nearly mean?",
   choices=["Bypassed", "Enrolled", "Valued", "Displayed"], answer="D",
   why="The motorman is chafing and resentful; 'registered discontent' means he showed it. "
       "'Enrolled' and 'valued' are the word's other senses and do not fit an emotion."),

 dict(num=2, skill="Words in Context",
   passage="As a member of Indigenous Photograph, artist Tshepiso Mabula ka Ndogngeni (Xhosa) can "
           "_____ her work more broadly than she could without the organization&rsquo;s reach. "
           "Photography editors around the world can search for Indigenous photographer members on "
           "the organization&rsquo;s website to find images that document and reflect the lives of "
           "Indigenous communities.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["empty", "promote", "alter", "discover"], answer="B",
   why="The second sentence explains that editors worldwide can find her work through the "
       "organization, i.e. the membership helps her publicise it more widely. 'Promote' is the "
       "only choice that means making work more widely known."),

 dict(num=3, skill="Words in Context",
   passage="Originating in the traditional stories of the <em>Kanaka Maoli</em>, the Native Hawaiian "
           "people, the literature of Hawaii has a rich history that was later brought to "
           "international prominence by writers such as Mary Kawena Pukui. Now, by producing "
           "acclaimed works, Gary Pak has _____ his place in that literary tradition.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["contemplated", "subverted", "solidified", "extricated"], answer="C",
   why="Producing acclaimed works secures rather than questions his standing. 'Subverted' and "
       "'extricated' reverse the sense; 'contemplated' does not fit 'his place'."),

 dict(num=4, skill="Words in Context",
   passage="In a 2018 article about films depicting the experiences of Black Americans, critics for "
           "the <em>New York Times</em> praise Madeline Anderson&rsquo;s 1970 film <em>I Am "
           "Somebody</em> as &ldquo;galvanizing&rdquo; and Reginald Hudlin&rsquo;s 1990 film "
           "<em>House Party</em> as &ldquo;exuberant.&rdquo; Fans of the two films hope that such "
           "_____ will attract new audiences to these works.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["impartiality", "ambivalence", "foresight", "acclaim"], answer="D",
   why="'Such _____' refers back to the critics' praise. Only 'acclaim' names praise; "
       "'impartiality' and 'ambivalence' contradict it."),

 dict(num=5, skill="Text Structure and Purpose",
   passage="Researchers C&eacute;sar A. Hidalgo, Elisa Casta&ntilde;er, and Andres Sevtsuk created a "
           "computer model to predict the mix of businesses and places of interest found in a given "
           "neighborhood. The team used data from the Google Places API service to help identify "
           "florists, beauty salons, and other businesses and map their locations. This approach has "
           "some limits&mdash;<u>data from Places API tend to be restricted to places that are "
           "customer facing</u>&mdash;but the data set nonetheless provides an extremely reliable "
           "source to study colocation patterns of neighborhood amenities.",
   stem="Which choice best describes the function of the underlined portion in the text as a whole?",
   choices=["It describes the imprecise and subjective nature of neighborhood boundaries.",
            "It introduces a model that a research team built to evaluate the mix of amenities in urban neighborhoods.",
            "It emphasizes the potential utility of the team&rsquo;s model.",
            "It identifies a specific flaw in using a data set about amenities in cities."],
   answer="D",
   why="The underlined clause is the content of 'this approach has some limits' — it names one "
       "specific shortcoming of the Places API data. The model itself is introduced in the first "
       "sentence, not here, and the utility claim is the clause after the dash."),

 dict(num=6, skill="Text Structure and Purpose",
   passage="Known for the albums <em>Someday My Prince Will Come</em> and <em>Milestones</em>, jazz "
           "trumpeter Miles Davis collaborated several times with pianist Gil Evans. Their 1958 "
           "adaptation of George Gershwin&rsquo;s opera <em>Porgy and Bess</em> bears little "
           "resemblance to the 1935 original. Davis and Evans felt no desire to please listeners "
           "expecting an exact duplication of the opera. <u>They omitted parts, such as the aria "
           "&ldquo;I Got Plenty of Nuthin&rsquo;,&rdquo; and sometimes made only brief gestures "
           "toward Gershwin&rsquo;s melodies.</u> But Davis and Evans&rsquo;s willingness to "
           "recompose Gershwin&rsquo;s work led to one of the most enduring albums in "
           "Davis&rsquo;s catalog.",
   stem="Which choice best describes the function of the underlined sentence in the text as a whole?",
   choices=["It presents examples to support a claim made earlier in the text.",
            "It shows how two artists benefited from ignoring certain conventions.",
            "It proposes a reason why one work of art is widely thought to be more successful than another.",
            "It undermines an assertion made later in the text."],
   answer="A",
   why="The omitted aria and the brief gestures are concrete instances of the earlier claim that "
       "the adaptation 'bears little resemblance to the 1935 original'. The benefit appears in the "
       "following sentence, not the underlined one."),

 dict(num=7, skill="Text Structure and Purpose",
   passage="Scholarly interest in literary juvenilia&mdash;writings by children and "
           "teenagers&mdash;tends to focus on unpublished works by authors who became famous as "
           "adults, such as W.H. Auden&rsquo;s poem &ldquo;Autumn,&rdquo; which he wrote around age "
           "15, because they offer insights into their authors&rsquo; artistic development. But some "
           "scholars also argue that recovering juvenilia by lesser-known writers is essential to "
           "understanding literary history: Daisy Ashford&rsquo;s novels, which she published as a "
           "child, were widely read by contemporaries and are therefore deserving of closer attention.",
   stem="Which choice best states the main purpose of the text?",
   choices=["To describe the challenges famous writers encountered when seeking to publish works written in their childhood",
            "To argue that Ashford&rsquo;s novels have more literary merit than Auden&rsquo;s juvenilia do",
            "To compare the accomplishments of young writers with those of their adult contemporaries",
            "To present reasons why literary scholars consider juvenilia to be valuable resources"],
   answer="D",
   why="The text gives two reasons juvenilia is studied — insight into artistic development, and "
       "understanding literary history — without ranking the two writers or discussing publication "
       "difficulties."),

 dict(num=8, skill="Central Ideas and Details",
   passage="Superlubricity, the state of virtually no friction between materials, has desirable "
           "applications in many industries. For example, it can make aircraft engines more "
           "efficient. To produce a coating that achieves superlubricity, Chanaka Kumara and "
           "colleagues broke down carbon nanotubes into fragments of graphene to fully cover two "
           "surfaces that would rub together. Friction between pieces of graphene is generally "
           "extremely low, and when the researchers added a drop of oil as lubrication, that friction "
           "nearly vanished. This new coating may drastically lower friction-related energy costs.",
   stem="According to the text, what happened when the researchers added oil to the surfaces covered in graphene fragments?",
   choices=["All the pieces of graphene collected on just one of the two surfaces.",
            "The low amount of friction between the surfaces became even lower.",
            "Carbon nanotubes on the surfaces fractured into smaller pieces.",
            "Friction between the surfaces did not noticeably change right away."],
   answer="B",
   why="Stated directly: friction between graphene is 'generally extremely low', and with the oil "
       "it 'nearly vanished'. That is low becoming lower."),

 dict(num=9, skill="Central Ideas and Details",
   passage="Roy McLendon&rsquo;s <em>Moonlit St. Lucie</em>, a riverscape featuring the silhouette of "
           "a single palm tree against the backdrop of shimmering water and a brilliant moonlit sky, "
           "is typical of paintings by the Florida Highwaymen, an informal collective of landscape "
           "artists mainly active in the 1950s and &rsquo;60s. Remarkable for anticipating and "
           "amplifying cultural perceptions of Florida that became pervasive in the public "
           "consciousness, paintings by the Highwaymen are readily identifiable by the natural "
           "iconography&mdash;placid inland rivers, windswept palm trees&mdash;that McLendon and "
           "colleagues perpetually revisited.",
   stem="Which choice best states the main idea of the text?",
   choices=["Although similar in its subject matter to many paintings by the Florida Highwaymen, <em>Moonlit St. Lucie</em> is now more highly regarded than other Florida Highwaymen paintings are.",
            "Representative images found across many paintings by McLendon and other Florida Highwaymen came to be widely associated with Florida in part due to the Florida Highwaymen&rsquo;s influence.",
            "Although paintings by the Florida Highwaymen were once celebrated for their depictions of Florida&rsquo;s natural environments, the popularity of these paintings waned after the 1960s.",
            "The placid inland rivers and windswept palm trees that are typical of McLendon&rsquo;s works, which are otherwise indistinguishable from other Florida Highwaymen paintings, help to differentiate McLendon&rsquo;s paintings from those of his colleagues."],
   answer="B",
   why="'Anticipating and amplifying cultural perceptions of Florida that became pervasive' is "
       "exactly B. The text never ranks McLendon above his colleagues (A, D — and D is "
       "self-contradictory), and never says popularity waned (C)."),

 dict(num=10, skill="Central Ideas and Details",
   passage="The following text is from George Eliot&rsquo;s 1857 short story &ldquo;The Sad Fortunes "
           "of the Rev. Amos Barton.&rdquo; In the text, the narrator addresses the reader directly "
           "and alludes to a discussion among Rev. Amos Barton&rsquo;s neighbors.</p><p>It was happy "
           "for the Rev. Amos Barton that he did not, like us, overhear the conversation recorded in "
           "the last chapter. Indeed, what mortal is there of us, who would find his satisfaction "
           "enhanced by an opportunity of comparing the picture he presents to himself of his own "
           "doings, with the picture they make on the mental retina of his neighbours? We are poor "
           "plants buoyed up by the air-vessels of our own conceit: alas for us, if we get a few "
           "pinches that empty us of that windy self-subsistence! The very capacity for good would go "
           "out of us.",
   stem="Which choice best states the main idea of the text?",
   choices=["Although people grasp the importance of honesty, they typically resist confronting others about their flaws.",
            "Although people wish to be seen as considerate, the slightest setbacks will often discourage them from being so.",
            "People tend to fixate more often than they should on whether their acquaintances think highly of them.",
            "People are better off not knowing about the discrepancy between their own self-image and what others think of them."],
   answer="D",
   why="'It was happy for [Barton] that he did not overhear' plus the rhetorical question about "
       "comparing one's self-image with 'the picture they make on the mental retina of his "
       "neighbours' — the narrator argues such knowledge would drain the 'capacity for good'."),

 dict(num=12, skill="Command of Evidence",
   table=("Monthly Temperatures and Wing Centroid Sizes of Fruit Fly Specimens",
          ["Month", "Average high (&deg;F)", "Average low (&deg;F)",
           "Average male wing centroid size (mm)", "Average female wing centroid size (mm)"],
          [["October", "67", "44", "1.98", "2.29"],
           ["July", "87", "62", "2.02", "2.31"],
           ["June", "80", "56", "2.01", "2.31"],
           ["May", "73", "50", "1.98", "2.27"]]),
   passage="<em>Drosophila</em> (fruit flies) have generation times of 10&ndash;12 days, so seasonal "
           "changes in humidity and other environmental conditions can drive seasonal fluctuations in "
           "chromosome rearrangements in species such as <em>D. persimilis</em> and <em>D. "
           "mediopunctata</em>. <em>Drosophila</em> body size (for which wing centroid size serves as "
           "a proxy measure) correlates with life span. Banu &#350;ebnem &Ouml;nder and Cansu Fidan "
           "Aksoy measured the wing sizes of members of a <em>D. melanogaster</em> population in "
           "Ye&#351;il&ouml;z, Turkey, that were collected monthly between May and October over three "
           "years. Their research suggests that <em>Drosophila</em> collected in relatively warmer "
           "months should tend to have a longer life span, as is illustrated by the finding that _____",
   stem="Which choice most effectively uses data from the table to complete the assertion?",
   choices=["the average monthly low temperature was higher in June than in May.",
            "the average male wing centroid size was larger in July than in October.",
            "the average female wing centroid size was 2.02 mm in July but was 2.31 mm in June.",
            "the average female wing centroid size was consistently larger than the average male wing centroid size in all four months in the table."],
   answer="B",
   why="The assertion needs warmer month -> larger body size (wing centroid) -> longer life span. "
       "July (87/62) is the warmest month and October (67/44) the coolest; male centroid 2.02 vs "
       "1.98 makes exactly that link. A cites temperature with no size, D cites size with no "
       "temperature, and C misreads the table (July female is 2.31, not 2.02)."),

 dict(num=13, skill="Inferences",
   passage="A road was recently built in a Maryland woodland that is home to the house finch. Some "
           "finches&rsquo; nests were situated close to the new road and others were deeper in the "
           "woodland. Common ravens, which eat finch eggs, can spot nests near the open spaces of "
           "roads more easily than they can spot nests surrounded by woodland. Accordingly, "
           "researchers in Maryland trying to predict the impact of the new road on finches have "
           "suggested that _____",
   stem="Which choice most logically completes the text?",
   choices=["finch eggs will make up about the same percentage of common ravens&rsquo; diet as they did before the road was built.",
            "the number of finches building nests near the road will gradually increase as the finches adapt to the presence of the common ravens.",
            "finches nesting near the road will lose eggs to common ravens at a higher rate than will finches nesting far from the road.",
            "finches nesting far from the road will lay fewer eggs per nest than will finches nesting near the road."],
   answer="C",
   why="Ravens spot roadside nests more easily and eat finch eggs, so roadside nests should lose "
       "more eggs. Nothing in the text supports claims about diet percentage, adaptation, or "
       "clutch size."),

 dict(num=14, skill="Inferences",
   passage="Biologists Rebecca M. Calisi-Rodriguez and George E. Bentley examined research on species "
           "such as dark-eyed juncos and tucos, which have both been studied under laboratory "
           "conditions as well as in the wild, to see whether there were significant differences "
           "between findings in the wild and in the lab. And, for example, they found for tucos that "
           "daytime is the most active period for wild individuals but not for captive individuals. "
           "Calisi-Rodriguez and Bentley therefore concluded that the laboratory setting was likely _____",
   stem="Which choice most logically completes the text?",
   choices=["more suitable than wild settings for studying tucos&rsquo; patterns of rest and activity.",
            "affecting the results for both tucos and dark-eyed juncos.",
            "more suitable for studying dark-eyed juncos than for studying tucos.",
            "interfering with tucos&rsquo; patterns of rest and activity."],
   answer="D",
   why="Captive tucos lose the daytime activity peak that wild ones have, so captivity is changing "
       "the behaviour being measured. The text gives no junco result (B) and never compares "
       "suitability across species (C) or endorses the lab (A)."),

 dict(num=15, skill="Inferences",
   passage="All stainless steel contains varying amounts of iron, carbon, and corrosion-inhibiting "
           "chromium. However, ferritic stainless steel, often used for induction cookers, contains a "
           "higher percentage of chromium (at least 10.5%) than does austenitic stainless steel as "
           "well as a higher concentration of iron. Unlike ferritic stainless steel, austenitic "
           "stainless steel has a face-centered cubic crystalline structure held stable by the "
           "presence of nickel and nitrogen. Austenitic stainless steel has two subtypes: the 200 "
           "series, often used for washing machines, and the 300 series, which has more nickel than "
           "the 200 series and is often used for storage containers or furnaces. Thus, stainless "
           "steel used to manufacture _____",
   stem="Which choice most logically completes the text?",
   choices=["furnaces and stainless steel used to manufacture washing machines will both have a chromium content of less than 10.5%.",
            "washing machines will have a higher concentration of nickel in its composition than stainless steel used to manufacture furnaces will.",
            "induction cookers will have a face-centered cubic crystalline structure, but stainless steel used to manufacture storage containers will not.",
            "storage containers and stainless steel used to manufacture induction cookers will have a similar concentration of nitrogen in their compositions."],
   answer="A",
   why="Furnaces (300 series) and washing machines (200 series) are both austenitic, and austenitic "
       "has less chromium than ferritic's at-least-10.5%. B reverses the nickel comparison (the 300 "
       "series has more), C reverses the crystalline structure (cookers are ferritic, which is not "
       "face-centered cubic), and D is unsupported."),

 dict(num=16, skill="Form, Structure, and Sense",
   passage="An emulsifier is a type of compound that serves to stabilize an emulsion&mdash;a mixture "
           "of two or more liquids that otherwise would not easily blend together. In the cosmetics "
           "industry, emulsifiers such as stearyl alcohol _____ to blend oil and water into "
           "homogeneous formulations, like lotions and perfumes.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["employed", "being employed", "are employed", "that they employ"], answer="C",
   why="The sentence has no other main verb, so the blank must supply one for the plural subject "
       "'emulsifiers'. Only 'are employed' is a finite plural verb; the rest leave a fragment."),

 dict(num=17, skill="Form, Structure, and Sense",
   passage="The Akhundov National Library in Baku houses many historical newspapers, but it "
           "isn&rsquo;t necessary to travel to Baku to access them. Because these rare items are "
           "digitized, people around the world can access _____ regardless of where they live.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["it", "them", "this", "that"], answer="B",
   why="The antecedent is the plural 'these rare items' (the newspapers), so the plural pronoun "
       "'them' is required."),

 dict(num=18, skill="Form, Structure, and Sense",
   passage="The constitution of Spain, enacted in 1978, enshrines 60 total rights across 17,608 words "
           "of text. According to constitutional scholar George Tsebelis, who examines the "
           "implications of constitutional length on civil rights, _____ 105th in a global ranking of "
           "the shortest constitutions.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["its", "it&rsquo;s", "they&rsquo;re", "their"], answer="B",
   why="The clause needs a subject and a verb: 'it is 105th'. 'Its' and 'their' are possessives with "
       "no noun to attach to, and the singular antecedent (the constitution) rules out 'they're'."),

 dict(num=19, skill="Boundaries",
   passage="Featuring works by the photographers Liselotte Grschebina and Else &ldquo;Yva&rdquo; "
           "Neul&auml;nder-Simon, the 2021 exhibition <em>The New Woman Behind the Camera</em> set out "
           "to provide a wide-ranging overview of photography by women in the 1920s through the _____ "
           "given the collection&rsquo;s breadth of more than 120 photos, its efforts were largely "
           "successful.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["1950s,", "1950s", "1950s and", "1950s, and"], answer="D",
   why="Two independent clauses ('the exhibition set out to provide...' and 'its efforts were largely "
       "successful') need a comma plus a coordinating conjunction. A alone is a comma splice, B is a "
       "run-on, and C drops the comma required before 'and' joining independent clauses."),

 dict(num=20, skill="Boundaries",
   passage="The Austronesian language family comprises some 1,200 languages&mdash;including the _____ "
           "Javanese and Bikol, which are spoken by 100 million and 4.6 million speakers, "
           "respectively&mdash;and accounts for one-fifth of the world&rsquo;s languages, making it of "
           "keen interest to linguists like Li Jen-kuei.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["languages", "languages:", "languages&mdash;", "languages,"], answer="A",
   why="A pair of dashes already sets off the whole 'including...' aside. Inside it, 'the languages "
       "Javanese and Bikol' is a noun plus its appositive names and takes no punctuation; a third "
       "dash or a colon would break the pair."),

 dict(num=21, skill="Transitions",
   passage="Blair L.M. Kelley, a historian specializing in the history of segregation in the US, "
           "conducted extensive research while writing a book about the landmark <em>Brown v. Board of "
           "Education</em> court case. _____ when the book was released, colleagues in her field "
           "regarded it as a reliable source of information on the subject.",
   stem="Which choice completes the text with the most logical transition?",
   choices=["Likewise,", "Consequently,", "Next,", "Nevertheless,"], answer="B",
   why="The reliability her colleagues perceived follows from the extensive research, so the link is "
       "causal. 'Likewise' needs a parallel, 'Next' a sequence, 'Nevertheless' a contrast."),

 dict(num=22, skill="Transitions",
   passage="Many English adjectives share a linguistic origin with their associated nouns, like the "
           "adjective &ldquo;monetary&rdquo; and the noun &ldquo;money,&rdquo; both of which come from "
           "the Latin &ldquo;monetarius.&rdquo; _____ some adjectives do not share an origin with their "
           "associated nouns. For example, the adjective &ldquo;bovine&rdquo; ultimately comes from the "
           "Latin &ldquo;bos,&rdquo; while its associated noun, &ldquo;cow,&rdquo; comes from the Old "
           "English &ldquo;c&#363;.&rdquo;",
   stem="Which choice completes the text with the most logical transition?",
   choices=["Subsequently,", "For this reason,", "Nevertheless,", "Specifically,"], answer="C",
   why="'Some adjectives do not share an origin' contradicts the opening generalisation, so a "
       "contrast is needed. The other three signal sequence, cause and elaboration."),

 dict(num=23, skill="Transitions",
   passage="The decades since the Second World War have seen a range of outcomes for the independence "
           "movements of Micronesia, Melanesia, and Polynesia. Many of the regions&rsquo; islands and "
           "groups of islands have become independent nations. _____ the Northern Mariana Islands, a "
           "commonwealth in Micronesia consisting of fifteen islands, are part of the US, and the "
           "Society Islands, a group of islands in Polynesia including Tahiti and Bora Bora, are part "
           "of the territory of French Polynesia.",
   stem="Which choice completes the text with the most logical transition?",
   choices=["For example,", "Therefore,", "In fact,", "On the other hand,"], answer="D",
   why="Islands that remain part of the US and of French Polynesia are the opposite of the preceding "
       "sentence's independent nations — the 'range of outcomes' the first sentence promised. They "
       "are not examples of independence (A), nor a consequence (B) or intensification (C) of it."),

 dict(num=25, skill="Rhetorical Synthesis",
   passage="While researching a topic, a student has taken the following notes:</p><ul>"
           "<li>Ixmiquilpan is a municipality in the state of Hidalgo, Mexico.</li>"
           "<li>Municipalities are governmental regions responsible for providing many public services to their residents.</li>"
           "<li>One service they provide is water treatment.</li>"
           "<li>Ixmiquilpan&rsquo;s population was 98,654 in 2020.</li>"
           "<li>Hidalgo is divided into 84 municipalities.</li></ul>",
   stem="The student wants to provide an example of a public service that Ixmiquilpan is responsible "
        "for. Which choice most effectively uses relevant information from the notes to accomplish "
        "this goal?",
   choices=["As a municipality, Ixmiquilpan is responsible for providing water treatment to its residents.",
            "Ixmiquilpan is one of 84 municipalities in Hidalgo providing public services to their communities.",
            "Ixmiquilpan&mdash;a governmental region in the state of Hidalgo, Mexico&mdash;provides public services to its residents.",
            "In 2020, the municipality of Ixmiquilpan had a population of 98,654."],
   answer="A",
   why="Only A names a specific service (water treatment). B and C stay at the general 'public "
       "services' level and D is about population."),

 dict(num=26, skill="Rhetorical Synthesis",
   passage="While researching a topic, a student has taken the following notes:</p><ul>"
           "<li>Square Tower House is a former Ancestral Puebloan settlement in southwestern Colorado that was inhabited from approximately 1200&ndash;1300 CE.</li>"
           "<li>It contained elaborate multistory buildings primarily made of adobe and stone.</li>"
           "<li>The Ancestral Puebloan civilization (approximately 1200 BCE&ndash;1600 CE) was the precursor of modern Pueblo tribal nations.</li>"
           "<li>These modern nations include Zuni Pueblo and Isleta Pueblo.</li>"
           "<li>Buildings in Zuni Pueblo and Isleta Pueblo often incorporate traditional elements, such as adobe and stone, alongside more contemporary elements.</li></ul>",
   stem="The student wants to connect Square Tower House to modern-day Pueblo buildings. Which choice "
        "most effectively uses relevant information from the notes to accomplish this goal?",
   choices=["Modern-day Pueblo buildings, such as those in Zuni Pueblo and Isleta Pueblo, incorporate elements that wouldn&rsquo;t have been found in Square Tower House.",
            "The Ancestral Puebloan settlement of Square Tower House was built with adobe and stone, materials still used in the buildings of Zuni Pueblo and Isleta Pueblo.",
            "The elaborate buildings of Square Tower House in southwestern Colorado incorporate both traditional and modern-day elements in their design.",
            "Square Tower House, located in southwestern Colorado, was inhabited from approximately 1200&ndash;1300 CE, but its buildings aren&rsquo;t actively occupied today."],
   answer="B",
   why="B is the only choice naming something the two share — adobe and stone. A stresses a "
       "difference, C misattributes modern elements to Square Tower House, and D mentions only "
       "Square Tower House."),

 dict(num=27, skill="Rhetorical Synthesis",
   passage="While researching a topic, a student has taken the following notes:</p><ul>"
           "<li>Element abundance is a relative measure of the occurrence of a chemical element in a given environment.</li>"
           "<li>An element&rsquo;s relative abundance can be expressed as a mass fraction, mole fraction, or volume fraction.</li>"
           "<li>Mass fraction is the ratio of an element&rsquo;s mass to the combined mass of all elements in a given environment.</li>"
           "<li>The mass fraction of calcium (Ca) is 17,100 parts per million (ppm), or 1.71%, on Earth.</li>"
           "<li>The mass fraction of potassium (K) is 160 ppm, or 0.016%, on Earth.</li></ul>",
   stem="The student wants to specify an element&rsquo;s relative abundance on Earth. Which choice "
        "most effectively uses relevant information from the notes to accomplish this goal?",
   choices=["Mass fraction, mole fraction, and volume fraction can all be used to express an element&rsquo;s relative abundance in a given environment.",
            "Expressed as a mass fraction, the relative abundance of potassium on Earth is 160 ppm, or 0.016%.",
            "The relative abundance of the element potassium on Earth can be expressed in three different ways.",
            "On Earth, the mass fraction of potassium is greater than that of calcium."],
   answer="B",
   why="Only B gives an actual figure for one element. A and C describe the available measures "
       "rather than specifying an abundance, and D is false (calcium's 17,100 ppm far exceeds "
       "potassium's 160 ppm)."),
]

# Dropped, with the reason, rather than shipped:
DROPPED = {
 11:"The capture is a phone photo of a monitor and the left edge of the passage is cut off "
     "mid-word on every line ('dy of interactions between plants...'). The table and the answer "
     "(musk thistle grows alongside the Peruvian lily in Argentina) are both legible, but the "
     "passage would have to be reconstructed by inference, which CLAUDE.md forbids. There is "
     "enough surplus supply to drop it instead.",
 24: "Template repeat. The note set is the supercontinent one already live in Test 5 RW_M2_HARD "
     "Q25 (same definition of a supercontinent, same supercontinent-cycle bullet, same Euramerica "
     "'about 300 million years ago' fact) with Kenorland swapped for Ur and a different goal "
     "sentence. The standing rule rejects a template reused with only the details changed.",
}
