"""
October USB, Section 1 Module 2 (Reading & Writing) — hand transcription.

Page N of `pages/OctUSB/` holds question N-27, so p028 is Q1 and p054 is Q27.

Q21 and Q22-27 were harvested as Test 5 R&W top-ups and are excluded. Q18, Q19
and Q20 were set aside during the Test 5 build over key conflicts; under the
current policy (answer every R&W question here rather than trusting the source
key) they are usable again.
"""

SOURCE = "OctUSB"
MODULE = "RW_M2"

QUESTIONS = [
 dict(num=1, skill="Words in Context",
   passage="Cybersecurity experts often encourage users to create passwords that are fairly complicated "
           "and therefore difficult to guess. Nonetheless, research has shown that the more _____ "
           "approach to password selection seems to favor convenience over security: for example, the "
           "eighth most commonly used password in 2019 was the easily remembered "
           "&ldquo;iloveyou.&rdquo;",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["creative", "popular", "complex", "useful"], answer="B",
   why="The example is about what people most commonly choose ('the eighth most commonly used "
       "password'), so the blank names prevalence. 'Complex' would contradict 'favor convenience "
       "over security'."),

 dict(num=2, skill="Words in Context",
   passage="The fossil remains of the individual known as Denisova 8, discovered in Russia in 2010, can "
           "help paleoanthropologists not only _____ steps in the evolution of hominids but also "
           "illuminate the Pleistocene epoch generally, revealing important details about the time in "
           "which Denisova 8 lived.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["yield", "exploit", "prioritize", "discern"], answer="D",
   why="The 'not only... but also' pairing makes the blank parallel to 'illuminate', so it must mean "
       "to make out or perceive. The fossils reveal the steps rather than producing (A), using (B) or "
       "ranking (C) them."),

 dict(num=4, skill="Words in Context",
   passage="Some social scientists say that while an emphasis on preserving civil liberties is key to "
           "democracy, public understanding of history is also central to public comprehension of state "
           "politics, and if a citizenry is to function, historical issues cannot remain the domain "
           "only of experts. In short, knowledge of history is not _____ and must not be left to "
           "historians alone.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["unattainable", "superfluous", "commonplace", "equitable"], answer="B",
   why="The summary restates that historical knowledge is 'central' and belongs to everyone, so 'not "
       "_____' must deny that it is unnecessary. 'Not unattainable' and 'not commonplace' would say "
       "nothing about its importance."),

 dict(num=5, skill="Words in Context",
   passage="Mauricio Drelichman and Hans-Joachim Voth&rsquo;s analysis of the overall debt and revenue "
           "of the government of Philip II (who ruled an empire including Spain and Sicily from 1556 to "
           "1598) found an intriguing _____: although the government regularly defaulted on debt, it "
           "ran an even larger overall surplus than did the government of eighteenth-century Britain, "
           "which historians consider a model of fiscal virtue.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["harbinger", "exemplar", "sanction", "incongruity"], answer="D",
   why="The colon spells out a mismatch — habitual defaults alongside a bigger surplus than the "
       "model of fiscal virtue — which is what 'incongruity' names. 'Exemplar' would make Philip II's "
       "government the model rather than the anomaly."),

 dict(num=6, skill="Text Structure and Purpose",
   passage="Zurich has high pedestrian traffic, but simply replicating a feature of Zurich associated "
           "with walkability&mdash;e.g., its high number of street crossings&mdash;may be insufficient "
           "to induce increased walking in other cities. As urbanist Mariela Alfonzo argues, our "
           "understanding of individuals&rsquo; decision-making about whether to walk is insufficiently "
           "robust: some studies emphasize the role of <u>demographic characteristics</u>, others the "
           "role of <u>neighborhood type</u>, and so on, but walking decisions are made in complex "
           "contexts in which multiple conditions and needs inform individuals&rsquo; choices.",
   stem="Which choice best describes the function of the references to &ldquo;demographic "
        "characteristics&rdquo; and &ldquo;neighborhood type&rdquo; in the text as a whole?",
   choices=["They illustrate factors that researchers believe people consider when making walking decisions in most contexts but that the text argues are unique to walking decisions made by people in Zurich.",
            "They are examples of factors that studies suggest are important in people&rsquo;s decision-making about walking but that the text claims most people rarely consider when making walking decisions.",
            "They represent factors that have been identified as important influences on walking decisions but that the text suggests are merely some of the many factors that may contribute to people&rsquo;s decision-making about walking.",
            "They identify factors that Alfonzo argues have been overemphasized in studies of decision-making about walking but that the text asserts are relevant to most people&rsquo;s walking decisions."],
   answer="C",
   why="The two underlined phrases are what individual studies 'emphasize', introduced by 'some "
       "studies... others... and so on' and closed by 'multiple conditions and needs' — each is one "
       "factor among many. The text never confines them to Zurich (A) or says people rarely consider "
       "them (B)."),

 dict(num=8, skill="Central Ideas and Details",
   passage="The following text is from Virginia Woolf&rsquo;s 1919 novel <em>Night and Day</em>. The "
           "narrator describes a gathering of artists and intellectuals.</p><p>One person after another "
           "rose, and, as with an ill-balanced axe, attempted to hew out his conception of art a little "
           "more clearly, and sat down with the feeling that, for some reason which he could not grasp, "
           "his strokes had gone awry. As they sat down they turned almost invariably to the person "
           "sitting next them, and rectified and continued what they had just said in public.",
   stem="The text makes which point about the people at the gathering?",
   choices=["Each enjoys speaking publicly about abstract issues but dislikes speaking privately about them.",
            "Each fails at presenting a wholly coherent vision of art but does not understand why.",
            "Each is contemptuous of the other attendees but strives to impress them.",
            "Each becomes absorbed in a question about art, and no one knows how to answer the question."],
   answer="B",
   why="'His strokes had gone awry' is the failure and 'for some reason which he could not grasp' is "
       "the incomprehension — B's two halves exactly. A reverses the passage, which shows them "
       "continuing to talk privately, and nothing suggests contempt (C)."),

 dict(num=9, skill="Central Ideas and Details",
   passage="Nicolas Dussex and colleagues relied on historical DNA (hDNA)&mdash;genomic data "
           "incidentally preserved in specimens housed in natural history collections&mdash;to "
           "investigate the evolutionary trajectory of the kakapo parrot (<em>Strigops "
           "habroptilus</em>). Although this approach offers unique benefits, such as the ability to "
           "sample genomic material from extinct species, it remains relatively underutilized because "
           "archival specimens are sometimes stored in ways that compromise DNA quality, a situation "
           "not easily remediable under current methodological paradigms and with extant DNA extraction "
           "and analysis technologies.",
   stem="What does the text most strongly suggest about specimens from natural history collections?",
   choices=["While they were used in a study that made an important scientific discovery, they are generally of marginal value as sources of genomic data.",
            "Because of their often-deteriorated condition, they tend to yield genomic data that are time-consuming to extract and interpret.",
            "They are primarily used as sources of genomic data by scientists studying organisms that have undergone major evolutionary change.",
            "While they may contain valuable genomic data, not all of them can yield usable hDNA."],
   answer="D",
   why="The text pairs 'unique benefits' with storage that 'sometimes' compromises DNA quality and "
       "cannot easily be remedied — valuable in general, unusable in some cases. 'Sometimes' rules "
       "out A's blanket dismissal and B's 'often-deteriorated'."),

 dict(num=10, skill="Command of Evidence",
   passage="The utilization of deceptive antipredator displays is well documented in the little ringed "
           "plover (<em>Charadrius dubius</em>) and other species of the avian order Charadriiformes. "
           "An extensive literature review conducted by L&eacute;na de Framond et al. revealed that "
           "this trait has evolved across a surprisingly large phylogenetic distribution of 13 Aves "
           "orders, including Caprimulgiformes and Gruiformes. Subsequent investigation of potential "
           "selection mechanisms prompted the researchers to conclude that independent of avian order, "
           "the prevalence of the trait is mediated by environmental variations associated with the "
           "absolute latitude of brooding sites.",
   stem="Which finding, if true, would most strongly support the researchers&rsquo; conclusion?",
   choices=["Across the orders in the study, approximately 54% of the bird species brood in ranges from 50&deg; to 80&deg; absolute latitude, but most of the birds that are known to use deceptive antipredator displays brood between 0&deg; and 30&deg; absolute latitude.",
            "Deceptive antipredator displays are documented in Charadriiformes species across the entire range of absolute latitudes of brooding sites within that order, but in species from other orders, deceptive antipredator displays are documented only when brooding sites are at absolute latitudes 10&deg;&ndash;20&deg; higher than what is typical for those species.",
            "The use of deceptive antipredator displays is widespread among Charadriiformes species independent of the absolute latitude of their breeding sites, but its prevalence in other avian orders is limited to species with brooding sites located in absolute latitudes of 0&deg;&ndash;30&deg;.",
            "Across the orders in the study, deceptive antipredator displays are observed in approximately 34% of species with brooding ranges of 0&deg;&ndash;30&deg; absolute latitude and approximately 60% of species with brooding ranges of 50&deg;&ndash;80&deg; absolute latitude."],
   answer="D",
   why="The conclusion has two parts: prevalence tracks brooding latitude, and it does so regardless "
       "of order. Only D reports prevalence rising with latitude 'across the orders in the study'. B "
       "and C make the pattern order-dependent, which contradicts 'independent of avian order', and A "
       "compares where species brood rather than how prevalent the trait is."),

 dict(num=11, skill="Command of Evidence",
   passage="Honda&rsquo;s introduction of a walk-behind lawnmower in 1978 is an instance of brand "
           "extension&mdash;the company leveraged its brand recognition as an automobile manufacturer "
           "to enter a product category where it had not previously competed. To determine if perceived "
           "category similarity predicts consumers&rsquo; likelihood of purchasing brand extensions, "
           "Alicia Grasby et al. identified 30 extended-brand pairs (e.g., the same brand of hand "
           "lotion and mouthwash) in 52 weeks of purchases by approximately 60,000 households; for each "
           "pair, Grasby et al. had consumers rate the similarity of the product categories and "
           "calculated the change in probability of a brand in one category being purchased if the same "
           "brand was purchased in the other category.",
   stem="Which finding, if true, would provide evidence that the possibility Grasby et al. investigated "
        "does occur?",
   choices=["Consumers&rsquo; ratings and the changes in probability calculated by the researchers were both affected by level of brand recognition.",
            "There was a strong positive correlation between consumers&rsquo; ratings and the changes in probability calculated by the researchers.",
            "Consumers&rsquo; ratings varied substantially by category pair, whereas the changes in probability calculated by the researchers were broadly similar for each pair.",
            "Consumers tended to purchase more products in categories in which extended-brand pairs are found than in categories in which extended-brand pairs are not found."],
   answer="B",
   why="The possibility under test is that perceived category similarity (the ratings) predicts "
       "purchase likelihood (the probability change), so the evidence is the two moving together. C "
       "describes the opposite — ratings varying while probabilities do not — and A and D introduce "
       "brand recognition and category volume, neither of which is the relationship being tested."),
]

DROPPED = {
 7:  "Cross-Text pair that duplicates OctIntB M2 Q6, already transcribed for this build. Text 1 is "
     "the same predator/prey vignette with the species swapped (feral cat and ash-grey mouse in "
     "Australia here, rough-legged hawk and collared lemming in the Northwest Territories there) "
     "and Text 2 is the same wolf-exclusion study with the prey swapped (moose in Quebec here, Dall "
     "sheep in Yukon there), down to the identical 'small, rapidly reproducing prey, like birds, "
     "[mice/lemmings], and rabbits' clause. The question asked differs, but a student would be "
     "reading the same two texts twice.",
 3:  "Same template as OctIntB M1 Q5, already transcribed for this build. Both are 'X can run/swim "
     "very fast - up to N km/hr - but is significantly slower than Y, which can fly at speeds up to "
     "M km/hr. The difference between these speeds is largely _____ of the fact that the features "
     "that make flight possible do less to limit top speeds than the features suitable for "
     "[swimming/running]', with the same four choices (a consequence / an objective / a repudiation "
     "/ an explanation) and the same answer. Only the animals and numbers differ.",
 21: "Already used as a Test 5 R&W top-up.",
 22: "Already used as a Test 5 R&W top-up.",
 23: "Already used as a Test 5 R&W top-up.",
 24: "Already used as a Test 5 R&W top-up.",
 25: "Already used as a Test 5 R&W top-up.",
 26: "Already used as a Test 5 R&W top-up.",
 27: "Already used as a Test 5 R&W top-up.",
}
