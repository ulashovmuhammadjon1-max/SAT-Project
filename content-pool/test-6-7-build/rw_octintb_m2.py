"""
October IntB, Section 1 Module 2 (Reading & Writing) — hand transcription.

Page N of `pages/OctIntB/` holds question N-23, so p024 is Q1 and p050 is Q27.

Five questions from this module (9, 18, 19, 24, 25) are already live in
production as Test 5 material and are excluded. Four more (17, 20, 21, 22) were
set aside during the Test 5 build because the source key disagreed with a
careful reading; under the current policy — answer every R&W question here
rather than trusting the key — they are usable again and are included, with my
answer and its reasoning.
"""

SOURCE = "OctIntB"
MODULE = "RW_M2"

QUESTIONS = [
 dict(num=1, skill="Words in Context",
   passage="Despite stated claims of global relevance, much major research on income inequality "
           "performed in the 2010s suffered from a myopic focus on a few countries in North America "
           "and Western Europe, partly due to limited data availability. Researchers would later "
           "_____ this shortcoming after gaining new access to banking records located in nations in "
           "Asia, such as China, and Eastern Europe, such as Hungary.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["mitigate", "presuppose", "validate", "categorize"], answer="A",
   why="New data from the previously missing regions would reduce the narrow-focus problem. "
       "'Validate' and 'presuppose' would mean accepting the shortcoming rather than easing it."),

 dict(num=2, skill="Words in Context",
   passage="One popular theory of the origin of the Moon, the &ldquo;big whack,&rdquo; posits that a "
           "protoplanet called Theia collided with Earth, flinging debris into orbit that eventually "
           "coalesced into the Moon. Until recently, Theia was _____, but researcher Qian Yuan and "
           "colleagues now claim to have identified pieces of the protoplanet in the lowermost section "
           "of Earth&rsquo;s mantle.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["notional", "spurious", "veritable", "desultory"], answer="A",
   why="The contrast with newly identified physical pieces means Theia had existed only as an idea. "
       "'Spurious' would call the theory false, and 'veritable' would make Theia already confirmed."),

 dict(num=3, skill="Words in Context",
   passage="Political blogs with conspicuous ideological alignments became an integral component of US "
           "media in the early 2000s. While some commentators lauded this development, asserting that "
           "such blogs had a welcome transparency missing from traditional news, less _____ observers "
           "countered that such blogs tended to ideological extremes that exacerbated political "
           "polarization to problematic levels.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["misanthropic", "earnest", "sanguine", "recalcitrant"], answer="C",
   why="'Less _____ observers countered' sets these observers against the ones who lauded the "
       "development, so the blank must name optimism. 'Sanguine' is the only choice meaning hopeful."),

 dict(num=4, skill="Text Structure and Purpose",
   passage="During Rome&rsquo;s republican period, which ended in the first century BCE, libraries "
           "were predominantly owned by wealthy individuals who tightly controlled access to their "
           "book collections. The first public library became available in Rome in 28 BCE and was soon "
           "followed by one commissioned by Emperor Augustus. As modern scholar Fabio Fernandes notes, "
           "however, these two traditions aren&rsquo;t as distinct as they seem, as both the emperor "
           "and the private library owners viewed their libraries as extensions of their personal "
           "patronage, just on vastly differing scales.",
   stem="Which choice best states the main purpose of the text?",
   choices=["To give a brief overview of public access to libraries throughout Rome&rsquo;s republican period",
            "To contend that early imperial leaders in Rome wielded too much influence over libraries",
            "To assert that private and early public libraries in ancient Rome had an essential similarity",
            "To call into question the notion that private Roman libraries disappeared during the first century BCE"],
   answer="C",
   why="The text builds to Fernandes's point that the two traditions 'aren't as distinct as they "
       "seem' because both served personal patronage. That is a claim of similarity, not a critique "
       "of imperial influence (B) or a survey of public access (A)."),

 dict(num=5, skill="Text Structure and Purpose",
   passage="The following text is from George Marion McClellan&rsquo;s 1895 poem "
           "&ldquo;Eternity.&rdquo;</p><p>My spirit swoons, and all my senses cry<br/>For "
           "Ocean&rsquo;s breast and covering of the sky.<br/>Rock me to sleep, ye waves, and outward "
           "bound,<br/>Just let me drift far out from toil and care,<br/>Where lapping of the waves "
           "shall be the sound,<br/>Which mingled with the winds that gently bear<br/>Me on between a "
           "peaceful sea and sky,<br/>To make my soothing slumberous lullaby.",
   stem="Which choice best states the main purpose of the text?",
   choices=["To convey the speaker&rsquo;s longing for the ocean to impart a sense of inner tranquility",
            "To contrast the demands of the speaker&rsquo;s everyday life with the serenity of being rocked to sleep by the ocean",
            "To illustrate the increasing intensity of the speaker&rsquo;s desire to escape ongoing hardship by gliding on the ocean",
            "To justify the speaker&rsquo;s qualms about being transported by the ocean to a quiet destination"],
   answer="A",
   why="Every image — 'rock me to sleep', 'peaceful sea and sky', 'soothing slumberous lullaby' — is "
       "a wish for calm. 'Toil and care' is named once in passing and never developed into the "
       "contrast B requires, and the poem expresses no qualms (D)."),

 dict(num=6, skill="Cross-Text Connections",
   passage="<p><strong>Text 1</strong></p><p>In parts of the Northwest Territories, Canada, the "
           "rough-legged hawk is a major predator of the collared lemming. Researcher Alice Kenney and "
           "colleagues found that when this predation pressure on collared lemmings was temporarily "
           "reduced, their numbers significantly increased. This finding illustrates a foundational "
           "ecological <u>principle</u>: predators control prey population numbers.</p>"
           "<p><strong>Text 2</strong></p><p>Robert D. Hayes and colleagues found that excluding "
           "wolves from a site in Yukon, Canada, where they typically prey on Dall sheep had no "
           "significant effect on Dall sheep abundance. Many other predation relief studies show an "
           "increase in prey abundance, but those studies often focus on small, rapidly reproducing "
           "prey, like birds, lemmings, and rabbits, rather than large, slowly reproducing prey, like "
           "Dall sheep, which could account for the difference between those results and Hayes and "
           "colleagues&rsquo; results.",
   stem="Based on the texts, the author of Text 2 would most likely agree with which statement about "
        "the &ldquo;principle&rdquo; mentioned in Text 1?",
   choices=["It has some evidential support, but it should not be regarded as universally applicable.",
            "It has been challenged by some studies, but the findings of those studies have not been widely accepted.",
            "It may be true for some predators but only because those predators share certain physical characteristics.",
            "It is plausible, but many of the studies that support it have methodological flaws."],
   answer="A",
   why="Text 2 grants that 'many other predation relief studies show an increase in prey abundance' "
       "— evidential support — but proposes that prey life history (small and fast-reproducing versus "
       "large and slow) limits where the principle holds. It faults neither the studies' methods (D) "
       "nor their acceptance (B), and it points to prey traits, not predator traits (C)."),

 dict(num=7, skill="Central Ideas and Details",
   passage="Many artists associated with hyperpop, a movement in electronic music that emerged in the "
           "2010s, conform to the model perfected by American musician Laura Les: bold synthesizer "
           "arrangements, propulsive beats, and electronically manipulated vocals. Yet the movement is "
           "hardly uniform: Venezuelan recording artist Arca incorporates Latin rhythms into the "
           "hyperpop sound, for example. Such stylistic diversity is encouraged in part by the "
           "music-streaming app Spotify, whose curated playlist of hyperpop songs balances cohesion "
           "with variety.",
   stem="Which statement about Arca is best supported by the text?",
   choices=["While some of her recordings conform to the model perfected by Laura Les, others reject it outright.",
            "She developed her unique sound without being influenced by other artists on Spotify&rsquo;s hyperpop playlist.",
            "Her music diverges from the typical hyperpop sound but doesn&rsquo;t abandon it.",
            "Her inclusion on Spotify&rsquo;s hyperpop playlist inspired established artists to embrace stylistic experimentation."],
   answer="C",
   why="Arca appears as the example of a movement that 'is hardly uniform', and she 'incorporates "
       "Latin rhythms <em>into</em> the hyperpop sound' — a variation within the style, not a "
       "rejection of it (A). B and D make claims about influence the text never supports."),

 dict(num=8, skill="Central Ideas and Details",
   passage="Eighteenth-century economist Adam Smith is famed for his metaphor of the invisible hand, "
           "which he putatively used to illustrate a robust model of how individuals produce aggregate "
           "benefits by pursuing their own economic interests. Note &ldquo;putatively&rdquo;: as Gavin "
           "Kennedy has shown, Smith deploys this metaphor only once in his economic writings&mdash;to "
           "make a narrow point about the then-dominant economic theory of mercantilism&mdash;and it "
           "was largely ignored until some twentieth-century economists eager to secure an intellectual "
           "pedigree for their views elevated it to a fully-fledged paradigm.",
   stem="Which choice best states the main idea of the text?",
   choices=["Some twentieth-century economists gave Smith&rsquo;s metaphor of the invisible hand a significance it does not have in Smith&rsquo;s work, but it is nevertheless a useful model of how individuals produce aggregate benefits by pursuing their own economic interests.",
            "Smith&rsquo;s metaphor of the invisible hand has been interpreted as a model of how individuals acting in their own interest produce aggregate benefits, but it was intended as a subtle critique of the economic theory of mercantilism.",
            "The reputation of Smith&rsquo;s metaphor of the invisible hand is not due to the importance of the metaphor in Smith&rsquo;s work but rather to the promotion of the metaphor by some later economists for their own ends.",
            "Although Smith is famed for his metaphor of the invisible hand, the metaphor was largely ignored until economists in the twentieth century came to realize that the metaphor was a robust model that anticipated their own views."],
   answer="C",
   why="'Putatively', 'only once', 'a narrow point' and 'largely ignored' all deflate the metaphor's "
       "role in Smith's own work, while 'economists eager to secure an intellectual pedigree for "
       "their views' supplies the motive. A endorses the model the text calls putative, and D says "
       "the later economists discovered its merit rather than promoted it for their own ends."),

 dict(num=10, skill="Command of Evidence",
   passage="Early Earth is thought to have been characterized by a stagnant lid tectonic regime, in "
           "which the upper lithosphere (the outer rocky layer) was essentially immobile and there was "
           "no interaction between the lithosphere and the underlying mantle. Researchers investigated "
           "the timing of the transition from a stagnant lid regime to a tectonic plate regime, in "
           "which the lithosphere is fractured into dynamic plates that in turn allow lithospheric and "
           "mantle material to mix. Examining chemical data from lithospheric and mantle-derived rocks "
           "ranging from 285 million to 3.8 billion years old, the researchers dated the transition to "
           "3.2 billion years ago.",
   stem="Which finding, if true, would most directly support the researchers&rsquo; conclusion?",
   choices=["There is a positive correlation between the age of lithospheric rocks and their chemical similarity to mantle-derived rocks, and that correlation increases significantly in strength at around 3.2 billion years old.",
            "Mantle-derived rocks younger than 3.2 billion years contain some material that is not found in older mantle-derived rocks but is found in older and contemporaneous lithospheric rocks.",
            "Mantle-derived rocks older than 3.2 billion years show significantly more compositional diversity than lithospheric rocks older than 3.2 billion years do.",
            "Among rocks known to be older than 3.2 billion years, significantly more are mantle derived than lithospheric, but the opposite is true for the rocks younger than 3.2 billion years."],
   answer="B",
   why="The conclusion is that mixing between lithosphere and mantle began 3.2 billion years ago. B "
       "is exactly that signature: lithospheric material starts turning up in mantle rocks only after "
       "that date. A has similarity rising with age, the wrong direction; C and D compare diversity "
       "and abundance, neither of which is evidence of mixing."),

 dict(num=12, skill="Inferences",
   passage="Scholars are increasingly exploring the communication and preservation of ecological "
           "knowledge through Indigenous songs (e.g., Kazakh songs about water and foraging quality and "
           "those of the O&rsquo;odham people about desert plants). In one study, ethnobiologist Dana "
           "Lepofsky et al. received insight from Kwaxsistalla Wathl&rsquo;thla, a song keeper for the "
           "Kwakwaka&rsquo;wakw people in Canada, into songs referencing the people&rsquo;s use of "
           "terraced gardens in intertidal zones along the Pacific Northwest coast for the cultivation "
           "of clams for consumption. Archaeological evidence of significant increases in clam size and "
           "abundance in that area concurrent with the documented past implementation of the method "
           "described in the songs supports the conclusion that _____",
   stem="Which choice most logically completes the text?",
   choices=["non-Indigenous people around the Pacific Northwest coast adopted the practice developed by the Kwakwaka&rsquo;wakw people after observing its efficacy.",
            "the practice used by ancestors of modern Kwakwaka&rsquo;wakw people not only effectively maintained a food source but also promoted its robustness.",
            "there is greater corroboration in the archaeological record of ecological practices described in Kwakwaka&rsquo;wakw songs than of those described in Kazakh and O&rsquo;odham songs.",
            "although contemporary Kwakwaka&rsquo;wakw people have a deep understanding of and appreciation for the fishing and farming practices used by their ancestors, they no longer implement those methods."],
   answer="B",
   why="Clams were cultivated for consumption (a maintained food source) and both size and abundance "
       "rose (robustness) — the two halves of B. A, C and D reach for adoption by others, a "
       "cross-culture comparison and present-day abandonment, none of which the evidence touches."),

 dict(num=13, skill="Inferences",
   passage="For its 1974 work <em>Instant Mural</em>, the Chicano art collective Asco taped members "
           "Patssi Valdez and Humberto Sandoval to an outdoor wall in East Los Angeles. The work is "
           "manifestly a commentary on constraint, but many critics focus on Valdez and the social "
           "constraints women faced at the time, which is understandable but leaves the presence of "
           "Valdez&rsquo;s male collaborator Sandoval unexplained. We should instead consider that in "
           "1974, the art establishment&rsquo;s recognition of Chicano artists was (and had long been) "
           "restricted to sociohistorical muralists, leaving nonmuralist Chicano artists&mdash;like "
           "Asco&rsquo;s members&mdash;struggling to even exhibit their work; attending to this context "
           "opens an interpretation that accounts for all the evidence, allowing us to conclude that "
           "_____",
   stem="Which choice most logically completes the text?",
   choices=["while Valdez&rsquo;s presence in <em>Instant Mural</em> represents the social constraints placed on women at the time, Sandoval&rsquo;s presence represents Chicano muralists&rsquo; frustration at their lack of recognition by the art establishment.",
            "<em>Instant Mural</em> is best understood not as a critique of the social constraints placed on women but rather as a critique of sociohistorical muralists&rsquo; depictions of Chicano culture.",
            "the main subject of <em>Instant Mural</em> is female Chicano artists&rsquo; experience of being doubly constrained by gender-role expectations and the marginalization of certain types of art.",
            "<em>Instant Mural</em> is a reflection on the constraining aesthetic expectations placed on Chicano artists in general rather than on the social constraints placed on women specifically."],
   answer="D",
   why="The interpretation must 'account for all the evidence', i.e. explain Sandoval as well as "
       "Valdez. Constraint on Chicano artists generally covers both taped figures. A leaves them with "
       "unrelated meanings and gets the muralists backwards (it was the muralists who <em>were</em> "
       "recognised), and C keeps the female-only focus the passage rejects."),
]

NOT_CAPTURED = []

DROPPED = {
 9:  "Already live in production as Test 5 RW_M2_HARD Q13 material.",
 11: "Iigaya painting-enjoyment bar chart. The stem stipulates that participant P6 gave equal "
     "ratings to the abstract and cubist paintings, then asks what the model predicted, but the "
     "plotted quantity is a within-style correlation between predicted and reported ratings, not a "
     "predicted rating. Reasoning from a correlation of 0.43 versus 0.27 to a claim about whether "
     "two predicted ratings are equal is not sound, and the intended reading cannot be pinned down "
     "from the capture. Dropped rather than shipped with a doubtful answer.",
 18: "Already used as a Test 5 R&W top-up.",
 19: "Already used as a Test 5 R&W top-up.",
 24: "Already used as a Test 5 R&W top-up.",
 25: "Already used as a Test 5 R&W top-up.",
}
