# AP PSYCHOLOGY 3.5 Communication and Language Development — 30 questions
# CED effective Fall 2024/2025, Unit 3 Development and Learning.
# Learning objectives 3.5.A (key components of language and communication) and
# 3.5.B (how language develops in humans).
#
# Essential knowledge relied on, and both EKs are single dense sentences worth
# quoting in full because every item traces to one of them:
#
#   3.5.A.1  "Language is a shared (mutually agreed upon) system of arbitrary
#            symbols (often expressed as and combined into phonemes, morphemes,
#            and semantics) that are rule-governed (via grammar and syntax) and
#            generative to produce an infinity of ideas."
#   3.5.B.1  "In language development across all cultures, people use nonverbal
#            manual gestures (e.g., pointing) to communicate and develop formal
#            language through specific stages (cooing, babbling, one-word stage,
#            and telegraphic speech). People learning a language often make
#            errors such as overgeneralization of language rules as they learn."
#
# EXCLUSION STATEMENT respected: EK 3.5.A.1 places the PRAGMATICS of language
# outside the scope of the AP Psychology Exam. The word does not appear in this
# module, and no item turns on how context or social convention shapes utterance
# meaning.
#
# The four developmental stages are the CED's own closed list -- cooing,
# babbling, one-word stage, telegraphic speech -- and no other stage name is used
# as a key or as a distractor.
#
# The CED lists 2.D (research ethics) among this topic's suggested skills, which
# is why several items concern the ethics of studying language in children.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
# Every key's grounding claim is stated item by item in verify_p3_5.py.
TOPIC = ("3.5", "Communication and Language Development", 3)
QUESTIONS = [
 dict(q="According to the AP Psychology framework, language is a system of symbols that are", choices=[
   "shared, arbitrary, rule-governed, and generative",
   "innate, fixed, universal, and unchanging",
   "learned individually and understood by only one person",
   "identical in form across every human language"], ans=0,
   why="EK 3.5.A.1 describes language as a shared, mutually agreed upon system of arbitrary symbols that are rule-governed and generative."),
 dict(q="To call the symbols of a language \"arbitrary\" means that", choices=[
   "the connection between a symbol and what it stands for is a matter of convention rather than resemblance",
   "speakers may use any word they like for any meaning at any time",
   "the rules of the language change randomly over time",
   "the language has no rules governing word order"], ans=0,
   why="EK 3.5.A.1 calls the symbols arbitrary and, in the same sentence, shared and mutually agreed upon; arbitrariness is about the lack of a natural link, and the agreement is what keeps it from being individual whim."),
 dict(q="To call language \"generative\" means that", choices=[
   "a finite set of symbols and rules can produce an infinity of ideas",
   "every speaker generates a private language of their own",
   "language generates the emotions a speaker feels",
   "new words are added to a language every year"], ans=0,
   why="EK 3.5.A.1 states that language is generative to produce an infinity of ideas, which is a claim about the productive power of a limited system rather than about vocabulary growth."),
 dict(q="A phoneme is best described as", choices=[
   "a basic unit of sound in a language",
   "the smallest unit that carries meaning",
   "the rule governing the order of words in a sentence",
   "the meaning conveyed by a whole sentence"], ans=0,
   why="EK 3.5.A.1 lists phonemes, morphemes, and semantics as the levels into which linguistic symbols are combined; the phoneme is the sound level, as distinct from the meaning-bearing morpheme."),
 dict(q="A morpheme is best described as", choices=[
   "the smallest unit of language that carries meaning",
   "a basic unit of sound with no meaning of its own",
   "a complete grammatical sentence",
   "the physical gesture that accompanies speech"], ans=0,
   why="EK 3.5.A.1 lists morphemes alongside phonemes; the morpheme is the smallest meaning-bearing unit, which is what separates it from the phoneme."),
 dict(q="Which statement correctly distinguishes phonemes from morphemes?", choices=[
   "phonemes are units of sound; morphemes are the smallest units of meaning",
   "morphemes are units of sound; phonemes are the smallest units of meaning",
   "phonemes appear only in written language and morphemes only in speech",
   "the two terms describe the same unit at different sizes"], ans=0,
   why="EK 3.5.A.1 names both among the units into which linguistic symbols are combined, distinguished by sound versus meaning; the first distractor is that distinction reversed."),
 dict(q="Semantics, as EK 3.5.A.1 uses the term, concerns", choices=[
   "the meaning carried by words and combinations of words",
   "the physical sounds a speaker produces",
   "the order in which words may be arranged",
   "the loudness at which a sentence is spoken"], ans=0,
   why="EK 3.5.A.1 lists semantics with phonemes and morphemes as the levels at which linguistic symbols are expressed and combined; semantics is the meaning level."),
 dict(q="Grammar and syntax are cited in EK 3.5.A.1 as what makes language", choices=[
   "rule-governed",
   "arbitrary",
   "generative",
   "nonverbal"], ans=0,
   why="EK 3.5.A.1 states that the symbols of language are rule-governed via grammar and syntax, which is a different property from arbitrariness and from generativity."),
 dict(q="Syntax specifically concerns", choices=[
   "the rules governing how words may be arranged into sentences",
   "the meanings individual words carry",
   "the sounds available in a particular language",
   "the gestures speakers use while talking"], ans=0,
   why="EK 3.5.A.1 pairs grammar and syntax as the rule systems governing language; syntax is the arrangement of words, as distinct from the semantic level named in the same sentence."),
 dict(q="Two speakers of the same language understand one another because language is", choices=[
   "shared and mutually agreed upon",
   "arbitrary",
   "generative",
   "acquired through imitation alone"], ans=0,
   why="EK 3.5.A.1's parenthetical 'mutually agreed upon' is the property that makes communication possible; arbitrariness and generativity are properties of the system that do not by themselves produce mutual understanding."),
 dict(q="Which property of language explains how a speaker can produce and understand a sentence she has never encountered before?", choices=[
   "language is generative",
   "language is arbitrary",
   "language is shared",
   "language is expressed in phonemes"], ans=0,
   why="EK 3.5.A.1's generativity -- producing an infinity of ideas from a finite system -- is what allows novel sentences to be produced and understood."),
 dict(q="Which of the following is explicitly excluded from the scope of the AP Psychology Exam by EK 3.5.A.1?", choices=[
   "the pragmatics of language",
   "phonemes",
   "syntax",
   "telegraphic speech"], ans=0,
   why="The exclusion statement under EK 3.5.A.1 places the pragmatics of language outside the scope of the exam; phonemes and syntax are named in that same EK and telegraphic speech in EK 3.5.B.1."),
 dict(q="According to EK 3.5.B.1, people across all cultures use which form of communication before formal language?", choices=[
   "nonverbal manual gestures such as pointing",
   "written symbols",
   "complete grammatical sentences",
   "sign language taught by an adult"], ans=0,
   why="EK 3.5.B.1 states that in language development across all cultures, people use nonverbal manual gestures, giving pointing as its example."),
 dict(q="Which list gives the stages of formal language development named in the AP Psychology framework, in order?", choices=[
   "cooing, babbling, one-word stage, telegraphic speech",
   "babbling, cooing, telegraphic speech, one-word stage",
   "one-word stage, cooing, babbling, telegraphic speech",
   "cooing, one-word stage, babbling, telegraphic speech"], ans=0,
   why="EK 3.5.B.1 names the specific stages as cooing, babbling, one-word stage, and telegraphic speech, in that order."),
 dict(q="An infant produces drawn-out vowel-like sounds with no consonants. This is best described as", choices=[
   "cooing",
   "babbling",
   "the one-word stage",
   "telegraphic speech"], ans=0,
   why="EK 3.5.B.1 names cooing as the first of the specific stages of formal language development; it precedes the consonant-containing sounds of babbling."),
 dict(q="An infant repeats consonant-vowel combinations such as \"ba-ba-ba\" that do not yet refer to anything. This is best described as", choices=[
   "babbling",
   "cooing",
   "the one-word stage",
   "overgeneralization"], ans=0,
   why="EK 3.5.B.1 names babbling as the second stage; it involves consonant-vowel repetition that does not yet carry reference."),
 dict(q="A child says \"milk\" to mean that she wants milk. This is best described as", choices=[
   "the one-word stage",
   "babbling",
   "telegraphic speech",
   "cooing"], ans=0,
   why="EK 3.5.B.1 names the one-word stage as the third stage; a single word used to convey a whole intention is its defining case."),
 dict(q="A child says \"want cookie\" or \"daddy go,\" omitting smaller function words. This is best described as", choices=[
   "telegraphic speech",
   "the one-word stage",
   "babbling",
   "overgeneralization"], ans=0,
   why="EK 3.5.B.1 names telegraphic speech as the fourth stage; short strings carrying the content words and omitting function words are what the term denotes."),
 dict(q="Overgeneralization of language rules refers to", choices=[
   "applying a regular rule to a word that is an exception, as in saying \"goed\" for \"went\"",
   "using a word to refer to more objects than adults would",
   "failing to learn any grammatical rules at all",
   "speaking in longer sentences than a listener expects"], ans=0,
   why="EK 3.5.B.1 states that people learning a language often make errors such as overgeneralization of language rules; extending a regular pattern to an irregular case is what the term names."),
 dict(q="Why is a child's production of \"mouses\" instead of \"mice\" evidence that she is learning rules rather than merely imitating?", choices=[
   "she has produced a form she is unlikely to have heard, which means she applied a rule",
   "adults commonly use that form in speech to children",
   "the form appears in written texts she has seen",
   "it shows that she has stopped acquiring language"], ans=0,
   why="EK 3.5.B.1 pairs rule learning with overgeneralization errors; a form the child has almost certainly never heard cannot be imitation, so it must be produced by a rule she has extracted."),
 dict(q="EK 3.5.B.1 states that the pattern of language development it describes is found", choices=[
   "across all cultures",
   "only in cultures with written languages",
   "only in children raised by two parents",
   "only in children exposed to a single language"], ans=0,
   why="EK 3.5.B.1 opens with 'In language development across all cultures', which is the scope claim the framework makes about the gestures and the stages."),
 dict(q="A parent worries because her 10-month-old babbles but says no words. The most accurate framework-based response is that", choices=[
   "babbling precedes the one-word stage in the sequence the framework describes",
   "babbling indicates that language development has stopped",
   "the child has skipped the cooing stage",
   "words normally appear before babbling"], ans=0,
   why="EK 3.5.B.1 orders the stages cooing, babbling, one-word, telegraphic, so babbling without words is the expected state between the second and third stages."),
 dict(q="Which pairing of a stage with an example is correct?", choices=[
   "telegraphic speech — \"more juice\"",
   "cooing — \"more juice\"",
   "one-word stage — \"ba-ba-ba\"",
   "babbling — \"doggy runned away\""], ans=0,
   why="EK 3.5.B.1's telegraphic speech consists of short content-word strings; the other options attach one stage's label to another stage's characteristic output."),
 dict(q="Gestures such as pointing matter to the study of language development because they show that", choices=[
   "communication begins before formal spoken language does",
   "spoken language is unnecessary for human communication",
   "children imitate adults exactly",
   "language is not rule-governed"], ans=0,
   why="EK 3.5.B.1 places nonverbal manual gestures alongside the development of formal language, which means communication is under way before the spoken stages arrive."),
 dict(q="A researcher wants to study language development in toddlers by recording them at home. Which safeguard is most necessary for the study to meet ethical standards?", choices=[
   "obtaining informed consent from parents or guardians and protecting the recordings' confidentiality",
   "recording without telling the family so behavior stays natural",
   "guaranteeing in advance that the children will reach every stage on schedule",
   "requiring each child to speak a fixed number of words per session"], ans=0,
   why="Science practice 2.D, this topic's stated skill: children cannot consent for themselves, so consent comes from a guardian, and home recordings require confidentiality protection."),
 dict(q="A proposed study would deliberately restrict some infants' exposure to language in order to test whether a critical period exists. The decisive ethical objection is that", choices=[
   "the study would expose participants to a serious risk of lasting harm that no consent can justify",
   "the study would take too long to complete",
   "language development cannot be measured in infants",
   "critical periods have already been disproven"], ans=0,
   why="Science practice 2.D: protection from harm is not waivable by consent, and withholding language exposure risks a lasting deficit -- which is why evidence about critical periods for language, named in EK 3.2.B.4, comes from natural cases rather than from experiments."),
 dict(q="Which is the best operational definition of \"vocabulary size\" for a study of toddlers?", choices=[
   "the number of distinct words a caregiver records the child using during a fixed two-week period",
   "how verbal the child seems to the researcher",
   "the child's general language ability",
   "whether the child enjoys being read to"], ans=0,
   why="An operational definition states a countable measurement procedure; a distinct-word count over a fixed interval is measurable, while the alternatives restate the construct or measure enjoyment."),
 dict(q="A study finds that toddlers whose parents talk to them more have larger vocabularies. Before concluding that parental talk builds vocabulary, a careful reader should note that", choices=[
   "parents were not assigned how much to talk, so a third variable could produce both",
   "vocabulary size cannot be measured in toddlers",
   "the study must have used random assignment",
   "the framework denies that language develops through interaction"], ans=0,
   why="Nothing was manipulated, so the design is correlational and a third variable such as household resources remains a live explanation; the last option is also false, since EK 3.4.A.2's Vygotskian account is built on interaction."),
 dict(q="A researcher observes that children in two different countries pass through the same sequence of language stages. This finding is most consistent with", choices=[
   "EK 3.5.B.1's claim that the pattern holds across all cultures",
   "the exclusion of pragmatics from the exam",
   "the claim that language symbols resemble what they stand for",
   "the claim that language is not generative"], ans=0,
   why="EK 3.5.B.1 asserts the sequence for language development across all cultures, so cross-national agreement in the sequence is exactly the observation that claim predicts."),
 dict(q="A student claims: \"Children learn language purely by imitating what they hear.\" Which observation most directly challenges that claim?", choices=[
   "children produce overgeneralized forms such as \"goed\" that adults around them do not say",
   "children point at objects before they can speak",
   "children in all cultures pass through the same stages",
   "language uses arbitrary symbols agreed upon by a community"], ans=0,
   why="Science practice 4.B: an imitation account predicts only forms the child has heard, and EK 3.5.B.1's overgeneralization errors are forms the child has not heard, so they are the observation that bears directly against it."),
]
