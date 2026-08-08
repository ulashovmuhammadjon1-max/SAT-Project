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
]

DROPPED = {
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
