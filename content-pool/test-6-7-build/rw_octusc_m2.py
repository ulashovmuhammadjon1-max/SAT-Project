"""
October USC, Section 1 Module 2 (Reading & Writing) — hand transcription.

**This module is a near-clone of October USB Module 2.** Of the first seven
questions, six are the same item as an OctUSB M2 question with only the proper
nouns and numbers swapped. That is the strongest form yet of the finding
recorded in `rw_octusc_m1.py`: the three October papers are parallel forms of
one administration, and USC Module 2 in particular reuses USB Module 2's
Words-in-Context and Text-Structure block almost wholesale.

Yield from this module is therefore very low, and it is not worth transcribing
past the point where the pattern is established. Page N holds question N-16.
"""

SOURCE = "OctUSC"
MODULE = "RW_M2"

QUESTIONS = [
 dict(num=6, skill="Words in Context",
   passage="Although oil shocks&mdash;such as the 16% rise in oil prices from April to September of "
           "1973&mdash;can strongly affect individual consumers, Gbadebo Oladosu and colleagues have "
           "shown that at the level of national economies, their effects are often quite _____. The "
           "effect of recent oil shocks on the gross domestic product of China, for example, was only "
           "slightly greater than zero.",
   stem="Which choice completes the text with the most logical and precise word or phrase?",
   choices=["subdued", "variable", "beneficial", "persistent"], answer="A",
   why="'Only slightly greater than zero' is the example the blank must summarise, and it is set "
       "against 'can strongly affect individual consumers'. 'Subdued' is the only choice meaning "
       "small in effect; 'variable' and 'persistent' describe a pattern over time, not a magnitude."),
]

# Everything else read from this module duplicates an OctUSB Module 2 item.
DROPPED = {
 1: "Same template as OctUSB M2 Q1: '[Web developers / Cybersecurity experts] often encourage users "
    "to create passwords that are fairly complicated and therefore difficult to guess. Nonetheless, "
    "research has shown that the more _____ approach to password selection seems to favor "
    "convenience over security: for example, the [seventh/eighth] most commonly used password in "
    "[2012/2019] was the easily remembered '[letmein/iloveyou]'.' Same four choices, same answer.",
 2: "Same template as OctUSB M2 Q2: 'The fossil remains of the individual known as [LD 350-1 / "
    "Denisova 8], discovered in [Ethiopia/Russia] in [2013/2010], can help paleoanthropologists not "
    "only _____ steps in the evolution of hominids but also illuminate the [Pliocene/Pleistocene] "
    "epoch generally...' Same four choices, same answer.",
 4: "Third instance of the fast-animal template already rejected twice — OctUSB M2 Q3 and OctIntB "
    "M1 Q5. Springbok and peregrine falcon here.",
 5: "Same template as OctUSB M2 Q4 (knowledge of history is not _____ and must not be left to "
    "historians alone). Same four choices, same answer; the opening clause swaps 'an emphasis on "
    "preserving civil liberties' for 'a government with effective checks and balances' and "
    "'experts' for 'specialists'.",
 7: "Same item as OctUSB M2 Q6 (Mariela Alfonzo on walkability), with Copenhagen and its "
    "'human-scaled architecture' in place of Zurich and its 'high number of street crossings', and "
    "'population density'/'average commuting distance' in place of 'demographic "
    "characteristics'/'neighborhood type'. The four choices are identical in wording and order is "
    "only shuffled.",
}

NOT_TRANSCRIBED = (
    "Q8-Q27 were not transcribed. Six of the first seven questions were duplicates of OctUSB "
    "Module 2, so the expected yield does not justify the transcription cost while the August "
    "papers - a different administration, with no observed overlap - remain untouched. If more "
    "supply is ever needed, start at Q8 and dedupe every item against rw_octusb_m2.py first."
)
