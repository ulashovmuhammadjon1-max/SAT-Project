"""Key audit for AP PSYCHOLOGY 3.5 Communication and Language Development.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states the framework assertion the
key rests on.

This topic's entire required content is TWO SENTENCES, so both are quoted here
in full and every claim below traces to one of them:

  EK 3.5.A.1  "Language is a shared (mutually agreed upon) system of arbitrary
              symbols (often expressed as and combined into phonemes, morphemes,
              and semantics) that are rule-governed (via grammar and syntax) and
              generative to produce an infinity of ideas."
  EK 3.5.B.1  "In language development across all cultures, people use nonverbal
              manual gestures (e.g., pointing) to communicate and develop formal
              language through specific stages (cooing, babbling, one-word stage,
              and telegraphic speech). People learning a language often make
              errors such as overgeneralization of language rules as they learn."

EXCLUSION STATEMENT, checked first: EK 3.5.A.1 places the PRAGMATICS of language
outside the scope of the AP Psychology Exam. The word appears in this module
exactly once, as the KEY to item 12, where naming the excluded topic is the
correct response. No item tests pragmatics content, and no item turns on how
context or social convention shapes an utterance's meaning.

Two closed lists, and nothing outside either is ever used:
  * the units -- phonemes, morphemes, semantics (items 4-7)
  * the stages -- cooing, babbling, one-word stage, telegraphic speech
    (items 14-18, 23). No other stage name appears anywhere, as key or
    distractor.

EK 3.5.A.1 packs four distinct properties into one sentence -- SHARED, ARBITRARY,
RULE-GOVERNED, GENERATIVE -- and they are easy to blur because they arrive
together. Items 2, 3, 8, 10 and 11 each isolate one property by asking what it
explains that the others do not: arbitrariness explains the lack of resemblance,
sharedness explains mutual understanding, rule-governedness is what grammar and
syntax supply, and generativity explains novel sentences.

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p3_5

CLAIMS = [
 ("shared, arbitrary, rule-governed, and generative",
  "EK 3.5.A.1 names all four properties in one sentence: a shared (mutually agreed upon) system of arbitrary symbols that are rule-governed and generative. The key lists exactly those four and no others."),
 ("matter of convention rather than resemblance",
  "EK 3.5.A.1 calls the symbols arbitrary AND, in the same clause, shared and mutually agreed upon. Arbitrariness is the absence of a natural link between symbol and referent; the agreement is what stops it collapsing into the second distractor's individual whim, which is the standard misreading of the word."),
 ("finite set of symbols and rules can produce an infinity of ideas",
  "EK 3.5.A.1: generative to produce an infinity of ideas. This is a claim about the productive power of a limited system, not about vocabulary growth -- which is what the fourth distractor offers."),
 ("basic unit of sound",
  "EK 3.5.A.1 lists phonemes, morphemes, and semantics as the levels into which the symbols are expressed and combined. The phoneme is the sound level."),
 ("smallest unit of language that carries meaning",
  "EK 3.5.A.1's morpheme, the smallest meaning-bearing unit. Paired with item 4 so both members of the pair are defined before item 6 contrasts them."),
 ("phonemes are units of sound; morphemes are the smallest units of meaning",
  "EK 3.5.A.1 names both among the units of language, separated by sound versus meaning. The first distractor is that separation reversed; the third invents a written/spoken split the framework does not make."),
 ("meaning carried by words",
  "EK 3.5.A.1 lists semantics with phonemes and morphemes; semantics is the meaning level. The third distractor is syntax, which is named in the same sentence as a rule system rather than as a unit."),
 ("rule-governed",
  "EK 3.5.A.1 states that the symbols are rule-governed VIA GRAMMAR AND SYNTAX. Arbitrariness, generativity, and nonverbal communication are three other properties from the same EK and the next one, so the item discriminates among the framework's own list."),
 ("rules governing how words may be arranged into sentences",
  "EK 3.5.A.1 pairs grammar and syntax as the rule systems. Syntax concerns arrangement, which is what distinguishes it from the semantic level named in the same sentence."),
 ("shared and mutually agreed upon",
  "EK 3.5.A.1's parenthetical. Mutual agreement is the property that makes communication between two speakers possible; arbitrariness and generativity are real properties of the system that do not by themselves yield shared understanding, which is why they are the distractors."),
 ("language is generative",
  "EK 3.5.A.1: generative to produce an infinity of ideas. Producing and understanding a sentence never encountered before is precisely what a finite-system-infinite-output property explains and what the other three properties do not."),
 ("pragmatics of language",
  "The exclusion statement under EK 3.5.A.1 places the pragmatics of language outside the scope of the AP Psychology Exam. This is the one item in the module where the excluded term appears, and naming it is the correct response; phonemes and syntax are in EK 3.5.A.1 and telegraphic speech is in EK 3.5.B.1, so all three distractors are in scope."),
 ("nonverbal manual gestures such as pointing",
  "EK 3.5.B.1: in language development across all cultures, people use nonverbal manual gestures (e.g., pointing) to communicate. Pointing is the framework's own example."),
 ("cooing, babbling, one-word stage, telegraphic speech",
  "EK 3.5.B.1 names the specific stages in exactly this order. The three distractors are permutations of the same four stages, so the item tests the ORDER and not merely the membership of the list."),
 ("cooing",
  "EK 3.5.B.1's first stage. Vowel-like sounds without consonants is what cooing denotes, and the absence of consonants is the clause that separates it from babbling."),
 ("babbling",
  "EK 3.5.B.1's second stage: consonant-vowel repetition that does not yet refer to anything. The stem states that the sounds do not refer, which excludes the one-word stage."),
 ("one-word stage",
  "EK 3.5.B.1's third stage: a single word carrying a whole intention. The stem states that the word conveys a want, which is reference and so excludes babbling."),
 ("telegraphic speech",
  "EK 3.5.B.1's fourth stage: short strings of content words with function words omitted. The stem states the omission, which is the defining feature."),
 ("applying a regular rule to a word that is an exception",
  "EK 3.5.B.1: people learning a language often make errors such as overgeneralization of language rules. Extending a regular pattern to an irregular case is what the term names; the second distractor describes overextension of a word's reference, a different error the framework does not name."),
 ("produced a form she is unlikely to have heard, which means she applied a rule",
  "EK 3.5.B.1 pairs rule learning with overgeneralization errors, and the inference runs through the fact that the form is NOT in the input. This item supplies the reasoning that item 30 then uses against a pure imitation account."),
 ("across all cultures",
  "EK 3.5.B.1 opens with 'In language development across all cultures'. That is the framework's own scope claim for both the gestures and the stages, and it is what item 29's observation confirms."),
 ("babbling precedes the one-word stage",
  "EK 3.5.B.1's stage order. A child who babbles but has no words is between the second and third stages, which is the expected state rather than a sign of arrest. The fourth distractor reverses the framework's order."),
 ("telegraphic speech",
  "EK 3.5.B.1. This is the matching item: each distractor attaches one stage's label to another stage's characteristic output ('more juice' to cooing, 'ba-ba-ba' to the one-word stage, an overgeneralized sentence to babbling), so it cannot be answered by recognising a single term."),
 ("communication begins before formal spoken language",
  "EK 3.5.B.1 places nonverbal manual gestures alongside the development of FORMAL language, which means communicative behavior is under way before the spoken stages. The second distractor overstates this into a claim the framework does not make."),
 ("informed consent from parents or guardians and protecting the recordings' confidentiality",
  "Science practice 2.D, which the CED lists as one of this topic's two suggested skills. Toddlers cannot consent for themselves, so consent comes from a guardian, and home recordings carry a confidentiality obligation. The 'record without telling the family' distractor is an active violation dressed as methodological rigour."),
 ("serious risk of lasting harm that no consent can justify",
  "Science practice 2.D. Protection from harm is not waivable by consent, and withholding language exposure risks a lasting deficit. This is also why evidence about critical periods for language -- named in EK 3.2.B.4 -- comes from natural cases rather than from experiments, which connects the ethics point to real methodology rather than leaving it abstract."),
 ("number of distinct words a caregiver records the child using during a fixed two-week period",
  "An operational definition states a countable procedure with a stated interval. 'Seems verbal', 'general language ability', and enjoying being read to restate the construct or measure something else."),
 ("parents were not assigned how much to talk",
  "Nothing was manipulated, so the design is correlational and a third variable such as household resources remains live. The fourth distractor is additionally FALSE on the content: EK 3.4.A.2's Vygotskian account has children learning through interaction, so the framework does not deny the mechanism -- only this study's design fails to establish it."),
 ("holds across all cultures",
  "EK 3.5.B.1 asserts the sequence for language development across all cultures, so agreement in the sequence between two countries is the observation that claim predicts. The distractors are the exclusion statement and two denials of properties EK 3.5.A.1 asserts."),
 ("overgeneralized forms such as \"goed\" that adults around them do not say",
  "Science practice 4.B. A pure imitation account predicts only forms present in the input; EK 3.5.B.1's overgeneralization errors are forms that are NOT in the input, so they bear directly against it. The other three options are true framework statements that an imitation account could absorb without difficulty, which is what makes them wrong rather than merely weaker."),
]

psych_check.check(p3_5, CLAIMS, per_topic=30, n_choices=4)
