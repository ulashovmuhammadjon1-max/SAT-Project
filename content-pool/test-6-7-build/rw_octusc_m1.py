"""
October USC, Section 1 Module 1 (Reading & Writing) — hand transcription.

IMPORTANT FINDING recorded here for later builds: **the three October papers
(IntB, USB, USC) are parallel forms of the same administration and share
questions outright.** Three items in this module alone are the same question as
one already transcribed from Oct IntB Module 1, either verbatim or with only
the proper nouns swapped. Every October transcription must therefore be deduped
against the other two October papers, not just against production.

Only 16 of this module's 27 questions were captured by the source screen
recording; `num` is the on-screen badge, not the page index.
"""

SOURCE = "OctUSC"
MODULE = "RW_M1"

QUESTIONS = [
 dict(num=1, skill="Words in Context",
   passage="Folk and traditional art can take a wide variety of forms, including arts as _____ one "
           "another as storytelling and quilting. The National Heritage Fellowship was created to "
           "honor people for their accomplishments in these diverse arts and includes among its "
           "winners the Puerto Rican stringed-instrument maker Diomedes Matos.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["confused with", "humble about", "useful to", "different from"], answer="D",
   why="The frame is 'as ___ one another as', and the sentence stresses variety and diversity, so "
       "the blank must express unlikeness. Only 'different from' completes the comparison idiom."),

 dict(num=3, skill="Words in Context",
   passage="Possessing an outstanding collection of public art, Chicago has everything from monumental "
           "sculptures like Joan Mir&oacute;&rsquo;s <em>Mir&oacute;&rsquo;s Chicago</em> at sites like "
           "Brunswick Plaza to innovative street art like Justus Roe&rsquo;s mural <em>South Shore</em> "
           "located on South Exchange Avenue. The _____ public art on display in the city can thus "
           "satisfy any art lover.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["breadth of", "controversy over", "confusion about", "apathy toward"], answer="A",
   why="'Everything from monumental sculptures... to innovative street art' describes range, and "
       "'can thus satisfy any art lover' depends on that range. The other three are negative and "
       "unsupported."),

 dict(num=4, skill="Words in Context",
   passage="As with other river deltas, the Paran&aacute; River delta is _____: it is a constantly "
           "evolving network of channels and strips of land that change in size and shape as the river "
           "deposits new sedimentary particles where the river meets the waters of the Atlantic Ocean.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["dynamic", "immutable", "sustainable", "unrivaled"], answer="A",
   why="The colon makes the rest of the sentence a definition of the blank: 'constantly evolving... "
       "change in size and shape'. 'Immutable' is the opposite."),

 dict(num=5, skill="Text Structure and Purpose",
   passage="The <em>San Pedro</em> is just one of approximately three million known historical "
           "shipwrecks spread throughout the world&rsquo;s oceans, and their impact on sea life and "
           "underwater ecosystems is of great interest to researchers. Leila Hamdan and colleagues were "
           "particularly curious about the effects of wooden shipwrecks on seafloor microbial "
           "communities. The researchers studied two wooden shipwrecks in the Gulf of Mexico by placing "
           "pieces of pine and oak between zero and 200 meters away from each shipwreck to collect "
           "samples of three kinds of microbes: bacteria, archaea, and fungi. They found that across "
           "the three microbial communities, peak diversity and richness was observed on pine and oak "
           "samples placed approximately 125 meters from the shipwrecks.",
   stem="Which choice best describes the overall structure of the text?",
   choices=["It introduces a study of microbial communities near shipwrecks that has received significant scholarly attention, summarizes the results of that study, and then describes a research team&rsquo;s reaction to the study.",
            "It notes a general scientific interest in shipwrecks&rsquo; ecological effects, describes a specific study related to that interest, and then states one of the study&rsquo;s findings.",
            "It states the number of known shipwrecks, describes the historical significance of one of those shipwrecks, and then comments on the various microbes found at the shipwreck site.",
            "It names a famous historical shipwreck, describes the type of wood used to build that ship, and then explains how that wood type influences underwater microbial communities."],
   answer="B",
   why="General interest -> Hamdan's specific study and method -> the 125-metre finding. The text "
       "never gives the <em>San Pedro</em>'s history (C), its construction (D), or any scholarly "
       "reaction (A)."),

 dict(num=6, skill="Text Structure and Purpose",
   passage="The Federalist Papers are a collection of 85 essays written by Alexander Hamilton, John "
           "Jay, and James Madison. They were published pseudonymously in the <em>Independent "
           "Journal</em> and other New York newspapers in 1787&ndash;88 and argue that New Yorkers "
           "should vote to ratify the proposed United States Constitution. Though the authorship of "
           "most of the individual essays is certain, that of a few is in question: for instance, while "
           "No. 15, &ldquo;The Insufficiency of the Present Confederation to Preserve the Union,&rdquo; "
           "was surely penned by Hamilton, No. 52, &ldquo;The House of Representatives,&rdquo; may have "
           "been written by either Hamilton or Madison.",
   stem="Which choice best describes the overall structure of the text?",
   choices=["The text mentions a collection of essays and then points out something about these essays that is not completely known.",
            "The text summarizes an argument made in a collection of essays and then suggests that the essays&rsquo; authors didn&rsquo;t unanimously agree with the argument.",
            "The text lists the authors of a collection of essays and then notes that some of the essays were written by one person, while others were written by two people.",
            "The text describes why a collection of essays is notable and then details its publication history."],
   answer="A",
   why="The text introduces the collection, then turns on 'that of a few is in question' — uncertain "
       "authorship. C misreads that uncertainty as co-authorship, and B invents disagreement among "
       "the authors."),

 dict(num=8, skill="Central Ideas and Details",
   passage="The following text is adapted from Jerome K. Jerome&rsquo;s 1889 novel <em>Three Men in a "
           "Boat (To Say Nothing of the Dog)</em>. The narrator is traveling by boat with Harris and "
           "another friend.</p><p>[Harris] told us anecdotes of how he had gone across the [English] "
           "Channel when it was so rough that the passengers had to be tied into their [beds], and he "
           "and the captain were the only two living souls on board who were not ill. Sometimes it was "
           "he and the second mate who were not ill; but it was generally he and one other man. If not "
           "he and another man, then it was he by himself.",
   stem="Which choice best states the main idea of the text?",
   choices=["During a previous boat trip, Harris spent more time with the other passengers than with the captain.",
            "Harris has a hard time remembering his first trip across the English Channel when his friends ask about it.",
            "When Harris speaks of an earlier trip, he often changes the details but always brags about his own wellness.",
            "Harris is worried that he and his friends will encounter rough waters during their boat trip."],
   answer="C",
   why="The companion shifts each retelling — the captain, then the second mate, then 'one other "
       "man', then nobody — while the one fixed element is that Harris was never ill. That is a "
       "changing story with a constant boast, not forgetfulness (B)."),

 dict(num=12, skill="Command of Evidence", needs_figure="OctUSC p009 bar chart, 'Orientation of Leaf Pairs in Grapevines'",
   figure_source=("OctUSC", "p009.jpeg"),
   passage="Auxins are a class of hormones that influence plant growth, including leaf orientation "
           "(the tendency of leaves to be larger on one side of their long central axis than the "
           "other). University of California, Berkeley biologist Ciera Martinez and colleagues noted "
           "that in certain plants in which leaves grow in pairs, auxins will typically be concentrated "
           "in opposite sides of each leaf in the pair (e.g., on the left side of one leaf in the pair "
           "and the right side of the other). Accordingly, they hypothesized that paired leaves should "
           "tend to show opposite-side orientation, and they tested their hypothesis by examining "
           "paired leaves from several species of grapevines.",
   stem="Which choice best describes data from the graph that support Martinez and colleagues&rsquo; "
        "hypothesis?",
   choices=["The number of leaf pairs showing opposite-side orientation is fairly high in the July grape, but not as high as it is in the graybark grape.",
            "Although the number of leaf pairs showing same-side orientation is fairly high in the July grape, it is much lower in both the frost grape and graybark grape.",
            "Although the exact ratio varies by species, the graybark grape, frost grape, and July grape all show more leaf pairs with opposite-side orientations than with same-side orientations.",
            "In the graybark grape, frost grape, and July grape, all the leaf pairs show opposite-side orientation."],
   answer="C",
   why="The hypothesis is that paired leaves <em>tend</em> to show opposite-side orientation, so the "
       "support must be that opposite beats same in every species — which the chart shows (roughly "
       "105 vs 48, 200 vs 100, 265 vs 90). A and B compare species instead of orientations, and D "
       "overstates it to 'all', which the same-side bars contradict."),

 dict(num=13, skill="Inferences",
   passage="Researchers have noted that people with clinically typical hearing perceive sounds they "
           "believe to be meaningful as quieter than sounds of the same volume that they believe to be "
           "noise (i.e., meaningless to the listener). In a recent study, Antonia Olivia Dolan and "
           "colleagues allowed participants to listen to (and adjust the volume of) recordings of music "
           "in popular genres like acoustic folk and orchestral, as well as recordings of nature "
           "sounds. The researchers noted that participants may have treated the nature sounds as "
           "noise, which suggests that if a participant was exposed to Jose Gonzalez&rsquo;s "
           "&ldquo;Heartbeats&rdquo; and the nature sounds at a volume of 61.5 decibels, the "
           "participant likely would have _____",
   stem="Which choice most logically completes the text?",
   choices=["adjusted the volume of the nature sounds to be greater than 61.5 decibels.",
            "believed that neither the nature sounds nor &ldquo;Heartbeats&rdquo; were at a volume of 61.5 decibels.",
            "experienced the nature sounds as louder than &ldquo;Heartbeats&rdquo; even though they were not.",
            "perceived the nature sounds and &ldquo;Heartbeats&rdquo; to be comparably meaningful despite perceiving the music to be quieter."],
   answer="C",
   why="Meaningful sounds are heard as quieter than equally loud noise. The music is meaningful and "
       "the nature sounds were treated as noise, so at an identical 61.5 dB the nature sounds should "
       "seem louder. A is about adjusting rather than perceiving, and D contradicts the premise."),

 dict(num=14, skill="Inferences",
   passage="Evan MacLean and colleagues evaluated behavioral and genetic data from over 14,000 dogs, "
           "representing more than 100 breeds, and found that variations in behavior between breeds can "
           "be attributed to genetic variations between those breeds, suggesting a genetic basis for "
           "breed differences in behavior. This was the case for both separation problems and energy "
           "but was especially pronounced for trainability, which can be seen when a dog demonstrates "
           "willingness to fetch objects. In a different study, researchers found that, with regard to "
           "trainability, the English mastiff behaves in notably different ways than the Yorkshire "
           "terrier. Together, these findings imply that _____",
   stem="Which choice most logically completes the text?",
   choices=["the English mastiff and the Yorkshire terrier will likely become more genetically similar over time.",
            "the English mastiff and the Yorkshire terrier differ with respect to the genetic underpinnings for trainability.",
            "individual English mastiffs may display higher levels of trainability than individual Yorkshire terriers.",
            "English mastiffs and Yorkshire terriers show a greater tendency toward trainability than most other dog breeds do."],
   answer="B",
   why="Premise one: between-breed behavioural differences are genetic, especially for trainability. "
       "Premise two: these two breeds differ in trainability. The conclusion that follows is a "
       "genetic difference in trainability. C picks a direction the text never gives, and A and D go "
       "well beyond both premises."),

 dict(num=15, skill="Inferences",
   passage="The jade hawkmoth, a large-bodied moth, defends itself against Brandt&rsquo;s myotis and "
           "other insect-eating bats, which use echolocation to hunt, by emitting ultrasonic clicks "
           "that can, for instance, signal the moths&rsquo; unpleasant taste. To investigate "
           "moths&rsquo; defensive ultrasound&mdash;which researchers had thought was exclusive to "
           "tiger moths, hawkmoths, and one species of geometer moths&mdash;Jesse R. Barber et al. "
           "recorded the responses of moths from 252 genera, representing most families of large-bodied "
           "moths, to audio playback of bat echolocation. The researchers found that 52 of the genera, "
           "including several genera belonging to the geometer family, produced defensive ultrasonic "
           "clicks. This result suggests that _____",
   stem="Which choice most logically completes the text?",
   choices=["unlike the 52 moth genera that emit ultrasonic clicks, most moth genera have likely not developed defenses specifically against bat attacks.",
            "some genera of large-bodied moths may use ultrasonic signaling for purposes other than avoiding capture by predators such as Brandt&rsquo;s myotis.",
            "ultrasound production is only one of a diverse range of effective strategies moths employ to evade bat attacks.",
            "anti-bat ultrasound production may be a more prevalent defense strategy among large-bodied moths than previously known to researchers."],
   answer="D",
   why="Researchers expected the behaviour in three narrow groups and found it in 52 genera, "
       "including several new geometer genera — the finding is that it is commoner than thought. B "
       "and C introduce other purposes and other strategies the study never examined, and A draws a "
       "negative conclusion the sampling cannot support."),

 dict(num=19, skill="Boundaries",
   passage="On February 1, 2018, a Florida-based research team&mdash;Martha A. Scholl, Maoya Bassiouni, "
           "and Angel J. Torres-S&aacute;nchez&mdash;compiled climate data from several sites in Puerto "
           "Rico&rsquo;s Luquillo Mountains. At 8:30 a.m., the air temperature was 16&deg;C at site CC1, "
           "the site with the highest _____ it had shifted to 16.8&deg;C by 11:00 p.m.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["elevation and", "elevation", "elevation,", "elevation, and"], answer="D",
   why="'The air temperature was 16&deg;C at site CC1, the site with the highest elevation' and 'it "
       "had shifted to 16.8&deg;C by 11:00 p.m.' are both independent clauses, so they need a comma "
       "plus a coordinating conjunction. C alone is a comma splice and B is a run-on."),

 dict(num=20, skill="Boundaries",
   passage="Two of the most celebrated examples of visual allegory in painting, <em>The Four Elements: "
           "Air</em> by Joachim Beuckelaer and <em>Ceres (Summer)</em> by Antoine Watteau, were "
           "completed in 1570 and _____ such allegorical artwork was particularly popular from the 15th "
           "through the late 18th centuries.",
   stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
   choices=["1712 respectively,", "1712, respectively;", "1712, respectively,", "1712; respectively,"],
   answer="B",
   why="'Respectively' is a parenthetical closing the first independent clause and takes a comma "
       "before it; the second independent clause then needs a semicolon, not a comma (C is a splice). "
       "D puts the semicolon before 'respectively', detaching it from the dates it modifies."),

 dict(num=25, skill="Rhetorical Synthesis",
   passage="While researching a topic, a student has taken the following notes:</p><ul>"
           "<li>The Wairakei geothermal power plant in New Zealand uses a flash steam system to generate electricity.</li>"
           "<li>Flash steam technology requires geothermal reservoir temperatures above 180&deg;C.</li>"
           "<li>The use of flash steam systems worldwide is limited because many geothermal reservoirs aren&rsquo;t hot enough.</li>"
           "<li>The Traunreut geothermal power plant in Germany uses a binary cycle system.</li>"
           "<li>Binary cycle technology can generate energy from lower-temperature (less than 180&deg;C) geothermal reservoirs.</li>"
           "<li>Binary cycle systems involve higher maintenance costs than flash steam systems.</li></ul>",
   stem="The student wants to compare the disadvantages of the geothermal systems used at the Wairakei "
        "and Traunreut plants. Which choice most effectively uses relevant information from the notes "
        "to accomplish this goal?",
   choices=["Unlike the Traunreut plant, the Wairakei plant uses a flash steam system, which requires a less common resource: geothermal reservoirs with temperatures above 180&deg;C.",
            "Compared with the system used at the Wairakei plant, the system used at the Traunreut plant has a notable disadvantage: its cost.",
            "The system used at the Traunreut plant overcomes the temperature limitations of the Wairakei plant&rsquo;s system but is more costly to maintain.",
            "The system at the Wairakei plant requires temperatures above 180&deg;C, while the system at the Traunreut plant can operate at lower temperatures."],
   answer="C",
   why="The goal needs a drawback of <em>both</em> systems. C names Wairakei's temperature limitation "
       "and Traunreut's maintenance cost. A and B each give only one plant's disadvantage, and D "
       "gives a neutral capability comparison with no disadvantage at all."),
]

# Never captured by the source screen recording:
NOT_CAPTURED = [2, 10, 11, 16, 17, 18, 21, 22, 23, 24, 26]

# Duplicates of questions already transcribed from Oct IntB Module 1 — the
# October papers are parallel forms and share items. Kept the IntB copy.
DROPPED = {
 7:  "Same question as OctIntB M1 Q7 (community science / Abbigail Merrill butterfly study). The "
     "answer choices are identical word for word and the answer is the same; only two clauses of "
     "the passage differ ('assist with conservation efforts' vs 'offer insight into the daily life "
     "of a scientist', 'how butterfly color relates to flower choice' vs 'how weather relates to a "
     "butterfly's flower choice').",
 9:  "Same template as OctIntB M1 Q9 (loanwords via Spanish). Identical structure, identical answer "
     "choices, identical answer; only the words differ ('Coyote'/'Condor'/Quechua here versus "
     "'Tomato'/'Maize'/Taino there).",
 27: "Same template as OctIntB M1 Q27 (two lighthouse keepers, emphasise which began first). "
     "Identical note structure and goal; only the names, states and dates differ (Barbara Mabrity "
     "and Flora McNeil here versus Catherine A. Moore and Laura J. Hecox there).",
}
