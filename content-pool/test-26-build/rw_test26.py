#!/usr/bin/env python3
"""
Reading & Writing authored for Test 26.

All 81 items are original. The transcribed pool was spent by Test 8, and for
R&W authoring is in any case the safer route: a transcribed key has to be
re-derived by hand before it can be trusted (Test 5 shipped 6 wrong answers in
81 that way). Every item carries a `why` recording the reasoning that produced
the key AND the reason the strongest distractor fails; that record is the
verification, so no key exists here without one.

Rationales name options by their CONTENT, never by letter, so balance_rw.py is
free to rotate every question when it evens out the key distribution.

Writing-domain choices are never bare punctuation. Test 8 shipped Boundaries
items whose four options were ", " / "; " / ": " / " and ", which a student sees
as four empty rows. Every Boundaries item here repeats the words on either side
of the blank inside all four options, so each choice reads as the resulting
sentence.

Test 26's assigned territory is bell founding, campanology and change ringing,
organ building, pipe voicing, carillons, and tuning and temperament. Test 20
holds foundries, so the metalwork here is specifically about bells and never
about ironfounding in general. Nine further subjects fill out the 81 items and
were each keyword-screened against the corpus before use: room acoustics and
reverberation, ice cores and palaeoclimate, papermaking and paper conservation,
stained glass and leaded lights, corvid cognition, emerging sign languages,
metrology and the standard kilogram, falconry, and the acoustics of buildings
for speech.

Screened out before drafting, as collisions with the bank:
  * bell tuning by turning metal off the inside on a lathe, and the five
    partials of a bell (rw_test14:S4 is exactly that passage);
  * tone set by casting profile rather than by tin content (rw_test10:E2);
  * a restoration-grant sentence with a parallel infinitive series about an
    organ or a bell tower (rw_test13:F5 and rw_test11:F5 are both that item);
  * a campanile rebuilt after an earthquake (rw_test10:F6);
  * an ensemble tuned to itself rather than to an external standard
    (rw_test10:W8, gamelan).

Every passage was then scored by token Jaccard against
content-pool/rw_authored_corpus.json (1,295 banked passages); see MANIFEST.md
for the highest score reached.
"""

TH = ('<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;'
      'text-align:left;background:#F4F6F8;">')
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">'


def tbl(headers, rows):
    """The table style block mandated by CLAUDE.md, used verbatim."""
    out = ['<table style="border-collapse:collapse;margin:0.75rem 0;"><tr>']
    out += [f"{TH}{h}</th>" for h in headers]
    out.append("</tr>")
    for r in rows:
        out.append("<tr>" + "".join(f"{TD}{c}</td>" for c in r) + "</tr>")
    out.append("</table>")
    return "".join(out)


def notes(lines, lead="While researching a topic, a student has taken the following notes:"):
    return lead + "<ul>" + "".join(f"<li>{ln}</li>" for ln in lines) + "</ul>"


SENTENCES = "While planning an article, a student has written the following sentences:"

WIC_STEM = "Which choice completes the text with the most logical and precise word or phrase?"
CONV_STEM = "Which choice completes the text so that it conforms to the conventions of Standard English?"
TRANS_STEM = "Which choice completes the text with the most logical transition?"

QUESTIONS = []

# ---------------------------------------------------------------- Words in Context
# Twelve fill-in-the-blank items (the blank is a literal five-underscore run)
# and three underlined-word-meaning items, one of the latter per module.
QUESTIONS += [
    {
        "num": "W1", "skill": "Words in Context",
        "passage": "A bell is cast in the gap between two moulds: an inner core built up in loam over "
                   "brick, and an outer cope shaped by sweeping a board cut to the bell's profile around "
                   "a fixed spindle. The same board governs both surfaces, so every dimension of the "
                   "finished casting is fixed before any metal is melted. The founder's work at the "
                   "sweep board therefore _____ the tone the bell will have.",
        "stem": WIC_STEM,
        "choices": ["settles", "obscures", "records", "exaggerates"],
        "answer": "A",
        "why": "One board governs both surfaces and every dimension is fixed before the metal is melted, "
               "so the shape that produces the tone is decided at the board. The option about recording "
               "would mean the board merely registers a tone determined somewhere else, which reverses "
               "the order the passage gives.",
    },
    {
        "num": "W2", "skill": "Words in Context",
        "passage": "In change ringing no bell may move more than one place in the order from one row to "
                   "the next. A band cannot therefore jump from one arrangement of the bells to any "
                   "other it fancies; it has to arrive there through a chain of rows each differing "
                   "only slightly from the last. The rule makes the progress of a method _____.",
        "stem": WIC_STEM,
        "choices": ["incremental", "arbitrary", "inaudible", "instantaneous"],
        "answer": "A",
        "why": "Moving one place at a time forces the band through a chain of nearly identical rows, "
               "which is change by small steps. The option meaning unconstrained contradicts the stated "
               "rule, which is the one thing the passage says governs the order.",
    },
    {
        "num": "W3", "skill": "Words in Context",
        "passage": "In a tracker organ a thin wooden strip runs from each key to the valve under its "
                   "pipe, so that the finger opens the valve through the strip and nothing else. The "
                   "weight the finger meets rises with the number of stops drawn, and the player can "
                   "feel the moment the valve breaks free of its seat. The action gives the organist "
                   "an _____ contact with the pipework.",
        "stem": WIC_STEM,
        "choices": ["immediate", "intermittent", "imagined", "involuntary"],
        "answer": "A",
        "why": "Nothing stands between finger and valve but the strip, and the player feels the valve "
               "break free, so the contact is unmediated. The option meaning occasional is ruled out by "
               "the passage, in which the resistance is present at every key and rises with the stops.",
    },
    {
        "num": "W4", "skill": "Words in Context",
        "passage": "Two flue pipes made to the same measurements will not speak alike. The voicer widens "
                   "or narrows the opening at the mouth, raises or lowers the upper lip, and files small "
                   "nicks into the languid, listening after each change. None of this appears on the "
                   "drawings from which the pipe was made; the work is _____ rather than specified.",
        "stem": WIC_STEM,
        "choices": ["empirical", "decorative", "provisional", "hereditary"],
        "answer": "A",
        "why": "Every adjustment is made by listening and none of it is written down in advance, which "
               "describes work settled by trial rather than by instruction. The option meaning ornamental "
               "misses that the adjustments determine whether the pipe speaks at all.",
    },
    {
        "num": "W5", "skill": "Words in Context",
        "passage": "In a well temperament the fifths are not all narrowed by the same amount. The tuner "
                   "takes more from some and leaves others very nearly pure, so that the keys with few "
                   "sharps come out sweet while the remote keys come out rough. Such a scheme "
                   "<u>tempers</u> the octave without equalising it.",
        "stem": "As used in the text, what does the word \"tempers\" most nearly mean?",
        "choices": ["Adjusts by small amounts", "Hardens by heating and cooling",
                    "Divides into equal parts", "Softens in volume"],
        "answer": "A",
        "why": "The tuner narrows each fifth by a different small quantity, so the word names the making "
               "of slight adjustments. The metalworking sense involving heat is the wrong sense here, and "
               "the sense of equal division is the very thing the closing clause denies.",
    },
    {
        "num": "W6", "skill": "Words in Context",
        "passage": "A carillon is played from a cabin inside the tower, so the player hears the bells "
                   "through the louvres a few metres away rather than as the town hears them from the "
                   "square below. Recordings made at street level regularly surprise carillonneurs, "
                   "whose judgement of their own balance is therefore _____.",
        "stem": WIC_STEM,
        "choices": ["unreliable", "unnecessary", "unmistakable", "unrehearsed"],
        "answer": "A",
        "why": "The player hears the instrument from a position nobody else occupies and is surprised by "
               "recordings taken where the audience stands, so the judgement formed in the cabin cannot "
               "be trusted. The option meaning beyond doubt asserts the opposite of what the recordings "
               "keep showing.",
    },
    {
        "num": "W7", "skill": "Words in Context",
        "passage": "A hawk that has not been flown for a week will not come to the fist for the sake of "
                   "the falconer's company. The bird stays because being flown and fed is a better "
                   "arrangement than the one it would find for itself, and it will leave the moment that "
                   "ceases to be true. The bond between falconer and hawk is thus _____.",
        "stem": WIC_STEM,
        "choices": ["conditional", "affectionate", "irreversible", "ceremonial"],
        "answer": "A",
        "why": "The bird stays only while the arrangement suits it and leaves as soon as it does not, "
               "which is a bond that holds on terms. The option about affection is what the opening "
               "sentence explicitly rules out.",
    },
    {
        "num": "W8", "skill": "Words in Context",
        "passage": "A church that flatters a choir may ruin a recital of fast music. Where reverberation "
                   "runs to three seconds or more, the beginning of each note falls into the tail of the "
                   "one before it. A slow line gains warmth from this; a rapid passage is left _____.",
        "stem": WIC_STEM,
        "choices": ["indistinct", "inaudible", "abbreviated", "unaccompanied"],
        "answer": "A",
        "why": "Notes overlapping their predecessors smear one into the next, which costs a fast passage "
               "its separation rather than its volume. The option meaning it cannot be heard at all "
               "overstates the effect the passage describes, which is blurring and not silence.",
    },
    {
        "num": "W9", "skill": "Words in Context",
        "passage": "Bell metal carries far more tin than the bronze used for statuary &mdash; roughly a "
                   "fifth of the alloy by weight. The extra tin makes a casting hard and brilliant in "
                   "tone, and also brittle enough to crack under a badly hung clapper. The founder's "
                   "choice of alloy is accordingly a _____ between sound and survival.",
        "stem": WIC_STEM,
        "choices": ["compromise", "contradiction", "correspondence", "sequence"],
        "answer": "A",
        "why": "More tin buys tone and costs toughness, so the founder gives up some of one to get the "
               "other. The option meaning a match between two things ignores that the two properties "
               "here pull in opposite directions.",
    },
    {
        "num": "W10", "skill": "Words in Context",
        "passage": "Snow falling on the summit of an ice sheet is buried before it can melt, and the air "
                   "held between its grains is closed off as the snow compacts into ice. A core drilled "
                   "from such a sheet therefore brings up samples of ancient atmosphere, each one _____ "
                   "at the depth where it was sealed.",
        "stem": WIC_STEM,
        "choices": ["preserved", "diluted", "generated", "displaced"],
        "answer": "A",
        "why": "The air is shut in unaltered and comes back up in the core, so it has been kept as it "
               "was. The option about dilution would mean the sample had been mixed with something else, "
               "which is exactly what burial without melting prevents.",
    },
    {
        "num": "W11", "skill": "Words in Context",
        "passage": "Paper sized with alum and rosin, the standard method after about 1850, holds an acid "
                   "that goes on attacking its own fibres for as long as the sheet survives. A "
                   "conservator can wash the sheet and leave a reserve of calcium carbonate in it, but "
                   "the fibres already broken cannot be mended. Treatment of this kind is therefore "
                   "_____ rather than restorative.",
        "stem": WIC_STEM,
        "choices": ["preventive", "cosmetic", "speculative", "reversible"],
        "answer": "A",
        "why": "Washing and the alkaline reserve stop further attack while doing nothing about damage "
               "already done, which is protection against what has not yet happened. The option meaning "
               "merely superficial is wrong because the treatment changes the chemistry of the sheet and "
               "not its appearance.",
    },
    {
        "num": "W12", "skill": "Words in Context",
        "passage": "Medieval glaziers had no way of making a large sheet, so a window had to be assembled "
                   "from small pieces held in grooved strips of lead. Those strips are structural, and "
                   "they are also drawn: the glazier ran them along the fold of a sleeve or the line of "
                   "a jaw, so that a limitation of the material became a _____ of the design.",
        "stem": WIC_STEM,
        "choices": ["resource", "casualty", "concealment", "measurement"],
        "answer": "A",
        "why": "The lead had to be there and the glazier put it where the drawing wanted a line, turning "
               "a constraint into something the design used. The option meaning a loss suffered gets the "
               "direction backwards, since the passage says the limitation was put to work.",
    },
    {
        "num": "W13", "skill": "Words in Context",
        "passage": "A jackdaw that has watched another bird hide food will go back to the place once its "
                   "companion has left. Birds that have themselves pilfered in this way are the readiest "
                   "to shift their own stores when they are being watched. The result suggests that a "
                   "bird's own history of theft <u>informs</u> its treatment of others.",
        "stem": "As used in the text, what does the word \"informs\" most nearly mean?",
        "choices": ["Shapes", "Notifies", "Accuses", "Transcribes"],
        "answer": "A",
        "why": "Having stolen is what makes a bird cautious with its own stores, so the past experience "
               "influences the later behaviour. The sense of telling someone something needs a recipient "
               "of the news, and the only thing named here is the bird's own conduct.",
    },
    {
        "num": "W14", "skill": "Words in Context",
        "passage": "When deaf children were brought together in a single school for the first time, the "
                   "home-made gestures each had arrived with began to converge. Within a few cohorts the "
                   "system had a settled order of parts and a set of markers no individual child had "
                   "introduced, and the youngest signers used it more consistently than those who had "
                   "built it. The language was therefore _____ rather than invented.",
        "stem": WIC_STEM,
        "choices": ["cumulative", "arbitrary", "borrowed", "temporary"],
        "answer": "A",
        "why": "Each cohort added regularity that no single child had supplied, so the system was built "
               "up across successive users. The option about borrowing would require a source outside the "
               "school, and the passage says the children arrived with nothing but their own gestures.",
    },
    {
        "num": "W15", "skill": "Words in Context",
        "passage": "For ninety years the kilogram was a cylinder of platinum and iridium kept under three "
                   "bell jars near Paris. Copies sent to other countries were brought back and compared "
                   "with it at long intervals, and over the century the copies and the cylinder drifted "
                   "apart by a few tens of micrograms. Because the cylinder <u>defined</u> the unit, it "
                   "could not itself be said to have gained or lost mass.",
        "stem": "As used in the text, what does the word \"defined\" most nearly mean?",
        "choices": ["Fixed the meaning of", "Explained the purpose of",
                    "Limited the use of", "Described the appearance of"],
        "answer": "A",
        "why": "The cylinder was the unit, which is why no drift could be charged to it, so the word "
               "names the setting of what the term meant. The sense of describing an appearance would "
               "leave the mass of the cylinder open to question, and the closing clause says it is not.",
    },
]

# ------------------------------------------------------- Text Structure and Purpose
QUESTIONS += [
    {
        "num": "S1", "skill": "Text Structure and Purpose",
        "passage": "The founder builds the mould in a pit and melts the charge in a furnace above it, so "
                   "that the metal can be run down into the mould in a single pour lasting under a "
                   "minute. <u>A casting that cools unevenly locks stresses into itself that may show up "
                   "as a crack years afterwards, so the mould is banked round with sand and left "
                   "undisturbed for days.</u> Nothing in the process allows a second attempt at any "
                   "detail: what the pour leaves is what the bell is.",
        "stem": "Which choice best describes the function of the underlined sentence in the text as a whole?",
        "choices": [
            "It explains why a stage of the process is deliberately drawn out.",
            "It questions whether a single pour is really necessary.",
            "It describes the construction of the furnace above the pit.",
            "It offers an example of a bell that failed after long service.",
        ],
        "answer": "A",
        "why": "The sentence ties uneven cooling to cracking and gives that as the reason the mould is "
               "banked with sand and left for days, which accounts for the slowness of a stage the "
               "surrounding sentences present as otherwise quick. The option about an example of failure "
               "is wrong because no particular bell is named; the sentence states a general risk.",
    },
    {
        "num": "S2", "skill": "Text Structure and Purpose",
        "passage": "An organ is finished twice. The builder voices every pipe on a bench in the workshop, "
                   "where the room is small and dry. The instrument is then set up in the building it is "
                   "to live in, and every pipe is voiced again against walls that may add three seconds "
                   "of reverberation and a floor that may absorb none of it. The second round takes "
                   "longer than the first and cannot be shortened, because no measurement made in the "
                   "workshop predicts what a building will do to a pipe.",
        "stem": "Which choice best states the main purpose of the text?",
        "choices": [
            "To explain why the tonal work on an organ has to be finished in the building where it will stand.",
            "To argue that voicing in the workshop should be given up altogether.",
            "To compare the acoustics of two particular churches.",
            "To describe the training an organ builder receives.",
        ],
        "answer": "A",
        "why": "Every sentence works towards the closing claim that the workshop cannot predict what the "
               "building will do, which is why the second round of voicing happens on site and cannot be "
               "cut short. The option about abandoning workshop voicing overshoots the text, which "
               "presents the first round as a normal and retained stage.",
    },
    {
        "num": "S3", "skill": "Text Structure and Purpose",
        "passage": "A peal is five thousand changes or more rung without a break and without any row "
                   "repeating, and it takes about three hours. <u>The band rings from memory: no music "
                   "stands in front of anyone, and nobody beats time.</u> Each ringer follows a path "
                   "through the order that the method defines, and the conductor's only spoken words are "
                   "the calls that alter it.",
        "stem": "Which choice best describes the function of the underlined sentence in the text as a whole?",
        "choices": [
            "It supplies the conditions that make the feat described around it a severe one.",
            "It concedes a point that the rest of the text goes on to reject.",
            "It gives an example of a method a band might choose to ring.",
            "It explains how the length of a peal is calculated.",
        ],
        "answer": "A",
        "why": "Three hours of non-repeating rows would be a lesser matter with written music and a beat; "
               "stating that there is neither is what makes the surrounding description demanding. The "
               "option about a conceded point is wrong because nothing later in the text disputes the "
               "sentence.",
    },
]

# --------------------------------------------------------- Cross-Text Connections
# Both texts sit in one passage field, per CLAUDE.md.
QUESTIONS += [
    {
        "num": "X1", "skill": "Cross-Text Connections",
        "passage": "<p><strong>Text 1</strong></p><p>An instrument rebuilt three times is a document of "
                   "nothing. Where an eighteenth-century organ survives in outline, the later additions "
                   "should be stripped out and the original pipework and wind pressures put back, so "
                   "that the music written for such an instrument can be heard as its composers heard "
                   "it.</p><p><strong>Text 2</strong></p><p>The organ builder Mira Adeyemi treats the "
                   "later work as evidence in its own right. A nineteenth-century swell box or an added "
                   "reed records what a congregation wanted and what a builder of that decade could "
                   "make, and taking it out destroys the only surviving trace of both. Adeyemi restores "
                   "earlier material wherever it survives but leaves the additions standing, holding "
                   "that an instrument is a sequence of decisions rather than a single moment.</p>",
        "stem": "Based on the texts, how would Adeyemi (Text 2) most likely respond to the recommendation made in Text 1?",
        "choices": [
            "By arguing that removing the later work destroys historical evidence of its own.",
            "By agreeing that original wind pressures should be restored wherever they can be established.",
            "By denying that any eighteenth-century organ survives in recognisable form.",
            "By observing that congregations seldom notice which pipes are old.",
        ],
        "answer": "A",
        "why": "Adeyemi's stated reason for leaving additions in place is that each one records a want "
               "and a capability otherwise unrecorded, so stripping them is a loss of evidence. The "
               "option about agreeing on wind pressures picks up something Adeyemi does do for earlier "
               "material but says nothing about the recommendation at issue, which is removal.",
    },
    {
        "num": "X2", "skill": "Cross-Text Connections",
        "passage": "<p><strong>Text 1</strong></p><p>Annual layers in a Greenland core can be counted "
                   "like the rings of a tree. Summer snow differs from winter snow in the size of its "
                   "crystals and in its dust content, and for the last eleven thousand years the count "
                   "gives an age at each depth good to a few years.</p><p><strong>Text 2</strong></p>"
                   "<p>Counting works only while the layers can still be told apart. Deep in a sheet the "
                   "ice has been stretched and thinned by its own flow until a year occupies less than "
                   "the sampling resolution, which is to say in precisely the oldest part of any core. "
                   "There an age is obtained instead by fitting the record to a model of how the ice has "
                   "moved, and the uncertainty grows from years to centuries.</p>",
        "stem": "Based on the texts, what would the author of Text 2 most likely say about the accuracy claimed in Text 1?",
        "choices": [
            "It holds only for the part of a core in which layers can still be distinguished.",
            "It is overstated even for the most recent ice in a core.",
            "It could be extended to the oldest ice by counting more carefully.",
            "It rests on a flow model rather than on the layers themselves.",
        ],
        "answer": "A",
        "why": "Text 2 does not dispute the count where layers survive; it says the method stops working "
               "once flow has thinned a year below the sampling resolution, which confines the claimed "
               "accuracy to the upper part of a core. The option about more careful counting is ruled "
               "out by Text 2, which treats the loss of resolution as physical rather than a matter of "
               "effort.",
    },
    {
        "num": "X3", "skill": "Cross-Text Connections",
        "passage": "<p><strong>Text 1</strong></p><p>Equal temperament divides the octave into twelve "
                   "identical steps. Every key is then equally usable and equally out of tune, and a "
                   "keyboard can be taken through music written in any of them without being retuned "
                   "between pieces. The convenience is decisive, and by the middle of the nineteenth "
                   "century it had displaced everything else.</p><p><strong>Text 2</strong></p><p>What "
                   "was displaced, the organist Piotr Nowak insists, was not merely an older habit. In "
                   "an unequal tuning each key carries a quality of its own &mdash; one bright, another "
                   "rough &mdash; and composers picked keys for those qualities as a painter picks a "
                   "colour. Nowak tunes the instruments in his care unequally and holds that a listener "
                   "who has never heard the differences cannot know what a choice of key was for.</p>",
        "stem": "Based on the texts, how would Nowak (Text 2) most likely respond to the claim in Text 1 that the convenience of equal temperament is decisive?",
        "choices": [
            "By observing that the convenience was bought at the cost of distinctions composers relied on.",
            "By denying that equal temperament allows a keyboard to play in every key.",
            "By agreeing that no listener can hear the difference between one tuning and another.",
            "By arguing that an unequal tuning is quicker for a tuner to set.",
        ],
        "answer": "A",
        "why": "Nowak's objection is that keys once had qualities composers chose among and that equal "
               "steps abolish them, so what Text 1 counts as a gain he counts as a purchase with a "
               "price. The option about listeners hearing no difference contradicts his position, which "
               "depends on the differences being audible to anyone given the chance.",
    },
]

# ------------------------------------------------------- Central Ideas and Details
QUESTIONS += [
    {
        "num": "C1", "skill": "Central Ideas and Details",
        "passage": "The lettering round the waist of a medieval bell was made by pressing wax stamps into "
                   "the loam of the mould, and a founder owned one set of stamps and used it for years. "
                   "Two bells a hundred miles apart may carry the same crowned letter with the same "
                   "small flaw in its serif. Where the written records have gone, that flaw is often the "
                   "only evidence of who cast a bell and roughly when, and whole workshops have been "
                   "reassembled from it.",
        "stem": "Which choice best states the main idea of the text?",
        "choices": [
            "A damaged letter repeated in bell inscriptions can identify the workshop that cast a bell when documents do not survive.",
            "Medieval founders competed with one another to produce the most elaborate lettering.",
            "Bells cast in one workshop were normally hung in towers close to it.",
            "Wax stamps proved an unsatisfactory way of lettering a bell and were soon given up.",
        ],
        "answer": "A",
        "why": "The passage moves from how the lettering was made to the point that a repeated flaw "
               "attributes a bell where no document does, and it closes on workshops reconstructed from "
               "that evidence. The option about elaborate lettering introduces a competition the text "
               "never mentions.",
    },
    {
        "num": "C2", "skill": "Central Ideas and Details",
        "passage": "Before electric blowers, an organ's wind came from bellows worked by hand or by foot. "
                   "The pumper had to keep a weighted reservoir between two marks scratched on the case: "
                   "too low and the pipes sagged in pitch, too high and a valve blew off with a report "
                   "audible in the nave. Organists complained less of the labour than of its "
                   "unevenness. A tiring pumper let the pressure wander, and the whole instrument "
                   "wandered with it.",
        "stem": "According to the text, what was organists' chief complaint about hand-raised wind?",
        "choices": [
            "It varied as the person working the bellows grew tired.",
            "It needed more people than most churches could pay for.",
            "It could not reach the pressure the largest pipes required.",
            "It made a noise that covered the quieter stops.",
        ],
        "answer": "A",
        "why": "The text says outright that the complaint was of unevenness rather than of labour, and "
               "then explains that a tiring pumper let the pressure wander. The option about noise picks "
               "up the report of a blown valve, which the passage gives as a consequence of too much "
               "pressure and not as the standing complaint.",
    },
    {
        "num": "C3", "skill": "Central Ideas and Details",
        "passage": "A hawk is not tamed by being made docile. The falconer's work is to persuade a bird "
                   "that would otherwise leave that coming back to the fist is the surest route to a "
                   "meal, and the whole of the training turns on weight. A hawk carrying too much is "
                   "indifferent to the offer and drifts away; one carrying too little is desperate and "
                   "unfit to fly at all. The falconer weighs the bird before every flight and adjusts "
                   "the evening meal by a few grams.",
        "stem": "Which choice best states the main idea of the text?",
        "choices": [
            "Training a hawk turns on holding its appetite within a narrow range rather than on subduing it.",
            "A hawk that is fed generously becomes the most reliable hunter.",
            "Falconers seldom fly the same bird more than once in a day.",
            "A hawk's weight varies too much from day to day for weighing to be of use.",
        ],
        "answer": "A",
        "why": "The opening denies that taming is the point and the rest of the passage describes a "
               "margin bounded by indifference above and weakness below, policed by weighing before "
               "every flight. The option about generous feeding is the condition the text says makes a "
               "bird drift away.",
    },
    {
        "num": "C4", "skill": "Central Ideas and Details",
        "passage": "Many old carillons carry two mechanisms in one tower. A barrel studded with pegs, "
                   "turned by the tower clock, drops hammers on the outside of the bells at the quarters "
                   "and plays the same tune for months together; the pegs are shifted by hand when the "
                   "tune is changed, usually twice a year. The clavier, by contrast, works clappers "
                   "inside the bells and sounds only when a carillonneur has climbed to it. The two "
                   "never play together, and a lever throws the barrel out of engagement before a "
                   "recital begins.",
        "stem": "According to the text, how is the tune played by the barrel mechanism changed?",
        "choices": [
            "By moving the pegs on the barrel by hand.",
            "By replacing the hammers that strike the bells.",
            "By resetting the tower clock that turns the barrel.",
            "By throwing the barrel out of engagement with a lever.",
        ],
        "answer": "A",
        "why": "The passage states that the pegs are shifted by hand when the tune is changed, twice a "
               "year or so. The option about the lever describes how the barrel is silenced for a "
               "recital, which is a different operation and leaves the tune untouched.",
    },
    {
        "num": "C5", "skill": "Central Ideas and Details",
        "passage": "Rag paper made before the machine age has often come through five hundred years with "
                   "its fibres sound, while a newspaper from 1905 crumbles at a touch. The difference is "
                   "not craftsmanship but chemistry. Rag was beaten in water and needed no acid; wood "
                   "pulp was bleached and then sized with compounds that leave the sheet acidic from the "
                   "day it is made. The older sheet is not better made. It is made of something that "
                   "does not attack itself.",
        "stem": "Which choice best states the main idea of the text?",
        "choices": [
            "Older paper outlasts newer paper because of what it is made of rather than because it was made with more care.",
            "Papermakers before the machine age worked to standards their successors abandoned.",
            "Newspapers were always printed on the cheapest paper a publisher could obtain.",
            "Bleaching improved the look of paper without affecting its strength.",
        ],
        "answer": "A",
        "why": "The passage rejects craftsmanship as the explanation in its second sentence and closes by "
               "saying the older sheet is not better made but made of a different material. The option "
               "about abandoned standards is the reading the text sets out specifically to deny.",
    },
    {
        "num": "C6", "skill": "Central Ideas and Details",
        "passage": "A method is a rule telling each bell where to go next, and it is learned as a path "
                   "rather than as a list of rows. A ringer on the treble in Plain Bob traces the same "
                   "shape whatever the other bells are doing: out to the back one place at a time, a row "
                   "at the back, and home again. Because the path does not change, a ringer who has "
                   "learned it can join a band that rings the method faster, or on heavier bells, "
                   "without learning anything new.",
        "stem": "According to the text, why can a ringer who has learned a method ring it with an unfamiliar band?",
        "choices": [
            "The path each bell follows is the same from one performance to another.",
            "The conductor calls out each row as it comes round.",
            "Heavier bells are always rung more slowly than light ones.",
            "Every method is assembled from the same underlying sequence of rows.",
        ],
        "answer": "A",
        "why": "The final sentence gives the constancy of the path as the reason the ringer needs nothing "
               "new, and the treble example shows the shape holding whatever the other bells do. The "
               "option about a conductor calling every row contradicts the idea of a path learned in "
               "advance and is nowhere in the text.",
    },
]

# ----------------------------------------------------------- Command of Evidence
# Three of each kind, one per module: a table item, a quotation item, and a
# finding-that-would-support-or-weaken item.
QUESTIONS += [
    {
        "num": "E1", "skill": "Command of Evidence",
        "passage": "An acoustician measured the reverberation time of four halls of similar size and, in "
                   "each, the proportion of consonants that listeners at the back of the hall identified "
                   "correctly from recorded speech." + tbl(
            ["Hall", "Reverberation time (seconds)", "Consonants identified correctly (percent)"],
            [["Ashwell", "0.9", "95"], ["Brindle", "1.6", "89"],
             ["Coleford", "2.4", "78"], ["Dunmow", "3.5", "61"]]),
        "stem": "Which choice best describes data from the table that support the conclusion that each further second of reverberation costs a listener more consonants than the second before it?",
        "choices": [
            "The rise of 0.7 seconds between Ashwell and Brindle cost 6 points, while the rise of 1.1 seconds between Coleford and Dunmow cost 17.",
            "Dunmow had both the longest reverberation time and the lowest score of the four halls.",
            "Ashwell, with a reverberation time of 0.9 seconds, was correctly understood 95 percent of the time.",
            "Every hall with a reverberation time above 2 seconds scored below 80 percent.",
        ],
        "answer": "A",
        "why": "The conclusion is about a rate that steepens, so it needs two comparable stretches of the "
               "scale: about nine points a second at the short end against about fifteen at the long "
               "end. The option naming Dunmow as longest and worst establishes only that the two "
               "quantities move together, which would be equally true of a straight line.",
    },
    {
        "num": "E2", "skill": "Command of Evidence",
        "passage": "In a study of the eighteenth-century organ builder Gottfried Silbermann, the scholar "
                   "Renata Iversen argues that Silbermann's refusal to vary his tonal scheme from one "
                   "instrument to the next was not conservatism but a commercial method: a customer knew "
                   "in advance exactly what he would receive, and the workshop could cut and cast the "
                   "parts before any contract was signed.",
        "stem": "Which quotation from Silbermann's surviving correspondence would best illustrate Iversen's argument?",
        "choices": [
            "\"The specification is as in the others; the pipework for it stands ready in my shop, and the price is therefore as before.\"",
            "\"I have not yet seen the church, and I cannot say what the building will ask of the instrument.\"",
            "\"The organ at Freiberg gave me more trouble than any other I have built.\"",
            "\"I ask that the contract be settled before Michaelmas, since my journeymen must be paid.\"",
        ],
        "answer": "A",
        "why": "Iversen's claim has three parts &mdash; an unvarying scheme, stock made before a contract "
               "exists, and a price that follows from both &mdash; and the quotation about a "
               "specification as in the others, pipework already standing ready and the usual price "
               "supplies all three. The quotation about not having seen the church shows a builder "
               "waiting on the building, which is the opposite of a scheme settled in advance.",
    },
    {
        "num": "E3", "skill": "Command of Evidence",
        "passage": "Bell metal is close to four parts copper to one part tin. Adding tin beyond that "
                   "point makes a casting harder still, and the metallurgist Ines Duarte has proposed "
                   "that founders stopped where they did not because they had arrived at the best tone "
                   "but because the alloy becomes unworkably brittle past it: a bell of higher tin "
                   "content would sound as well but would not survive being rung.",
        "stem": "Which finding, if true, would most directly support Duarte's proposal?",
        "choices": [
            "Test bars cast with a higher proportion of tin matched bell metal in laboratory measurements of tone but fractured under a small part of the impact energy bell metal withstood.",
            "Founders working in different countries arrived at slightly different proportions of tin.",
            "Bells cast with a lower proportion of tin than bell metal are generally judged dull in tone.",
            "Present-day founders use very nearly the proportions their predecessors used.",
        ],
        "answer": "A",
        "why": "Duarte's proposal needs two things at once: that the tone does not improve past the usual "
               "proportion and that the metal does get brittle, which is exactly what bars matching bell "
               "metal in tone but failing at a fraction of the impact energy would show. The finding "
               "about dullness at lower tin says nothing about what happens above the usual proportion, "
               "which is where the proposal lives.",
    },
    {
        "num": "E4", "skill": "Command of Evidence",
        "passage": "A conservator measured the surface acidity of four sheets of paper of known date and "
                   "then measured the force each needed to tear, expressed as a percentage of the force "
                   "needed to tear a newly made sheet of rag paper." + tbl(
            ["Sheet (date)", "Surface pH", "Tear strength (percent of new rag paper)"],
            [["1560", "7.4", "88"], ["1720", "6.9", "81"],
             ["1870", "5.1", "34"], ["1935", "4.4", "19"]]),
        "stem": "Which choice best describes data from the table that support the conclusion that the loss of strength follows acidity rather than age?",
        "choices": [
            "The sheet of 1720 is older than the sheet of 1870 and yet is both less acid and more than twice as strong.",
            "The sheet of 1935 is the most acid of the four and also the weakest.",
            "The sheet of 1560 is the only one whose surface pH is above 7.",
            "Both sheets made after 1800 have a surface pH below 6.",
        ],
        "answer": "A",
        "why": "Only a case in which the older sheet is the stronger one separates the two explanations, "
               "and the 1720 sheet is 150 years the elder of the 1870 sheet while standing at 81 against "
               "34. The option pairing the most acid sheet with the weakest is consistent with age doing "
               "the damage as well, since that sheet is also the newest.",
    },
    {
        "num": "E5", "skill": "Command of Evidence",
        "passage": "The linguist Aur&eacute;lie Mensah has argued that the youngest signers in a new "
                   "language community do not merely learn what their elders sign. They regularise it, "
                   "supplying a consistent rule where the models in front of them are inconsistent.",
        "stem": "Which quotation from Mensah's report would best illustrate her argument?",
        "choices": [
            "\"Where the first cohort marked the ending in about half of the contexts that called for it, the third cohort marked it in very nearly all of them.\"",
            "\"The first cohort had no vocabulary in common on the day the school opened.\"",
            "\"Signers of every cohort produced the same handshape for this verb.\"",
            "\"Adults who arrived at the school after the age of twenty rarely became fluent.\"",
        ],
        "answer": "A",
        "why": "The argument is that later signers impose regularity their models lacked, which needs a "
               "measure of the same feature in two cohorts moving from patchy to consistent, and the "
               "quotation about an ending marked half the time and then almost always is that measure. "
               "The quotation about an identical handshape across cohorts shows something transmitted "
               "unchanged, which is the case Mensah's argument is meant to be distinguished from.",
    },
    {
        "num": "E6", "skill": "Command of Evidence",
        "passage": "Rooks in the laboratory drop stones into a tube of water until a floating worm rises "
                   "within reach. A sceptic has proposed that the birds are not reasoning about water "
                   "level at all but repeating an action that has been followed by food before, and "
                   "would go on dropping stones into a tube in which doing so could not possibly work.",
        "stem": "Which finding, if true, would most directly weaken the sceptic's proposal?",
        "choices": [
            "Birds given a tube packed with sawdust, in which dropped stones did not lift the worm, gave up after a few attempts and moved to a water tube instead.",
            "Birds dropped stones into a water tube more quickly on later trials than on earlier ones.",
            "Birds chose large stones in preference to small ones when both sizes were available.",
            "Some birds dropped stones into a tube on occasions when no worm had been placed in it.",
        ],
        "answer": "A",
        "why": "The sceptic's prediction is precisely that the birds will persist where the action cannot "
               "work, so birds abandoning the sawdust tube and switching to one where stones do lift the "
               "worm is the case that prediction fails on. The finding about speeding up over trials is "
               "what a repeated rewarded action looks like and fits the sceptic's account rather than "
               "damaging it.",
    },
    {
        "num": "E7", "skill": "Command of Evidence",
        "passage": "An organ builder measured how long one flue pipe took to settle on its pitch, its "
                   "speech time, at four wind pressures, leaving the voicing otherwise untouched, and "
                   "recorded the loudness of the settled note at each." + tbl(
            ["Wind pressure (millimetres of water)", "Speech time (milliseconds)", "Loudness (decibels)"],
            [["60", "140", "71"], ["70", "95", "74"], ["80", "72", "76"], ["90", "66", "77"]]),
        "stem": "Which choice best describes data from the table that support the builder's claim that raising the pressure beyond a certain point buys very little further improvement in speech?",
        "choices": [
            "Going from 60 to 70 millimetres cut the speech time by 45 milliseconds, whereas going from 80 to 90 cut it by 6.",
            "Speech time fell at every increase in wind pressure that was tried.",
            "The loudest reading was obtained at the highest pressure tested.",
            "At 60 millimetres of pressure the pipe took 140 milliseconds to settle on its pitch.",
        ],
        "answer": "A",
        "why": "The claim is about diminishing returns, so it needs two equal steps in pressure producing "
               "very unequal gains, and 45 milliseconds against 6 for the same rise of 10 millimetres is "
               "that comparison. The option noting that speech time fell at every step supports only "
               "that more pressure helps, which is the part of the claim not in question.",
    },
    {
        "num": "E8", "skill": "Command of Evidence",
        "passage": "The historian Ines Achebe argues that the campaign to replace the platinum kilogram "
                   "with a definition drawn from a constant of nature was driven less by the drift of "
                   "the artefact than by the impossibility of checking it. The cylinder could be "
                   "compared only with copies taken from it, so no comparison could establish which of "
                   "them had moved.",
        "stem": "Which quotation from a metrologist's memorandum would best illustrate Achebe's argument?",
        "choices": [
            "\"We can state that the copies and the prototype now differ by some fifty micrograms; we cannot state which of them has changed, and no measurement open to us will settle it.\"",
            "\"The prototype is kept under three bell jars and is handled once in a generation.\"",
            "\"The copies are made of the same platinum and iridium alloy as the prototype itself.\"",
            "\"A definition drawn from a constant of nature could be realised in any sufficiently equipped laboratory.\"",
        ],
        "answer": "A",
        "why": "Achebe's point is not that the artefact drifted but that nothing could say which side of "
               "the comparison had moved, and the quotation stating a known difference alongside an "
               "unanswerable question of attribution says exactly that. The quotation about realising a "
               "definition anywhere describes the advantage of the replacement rather than the defect in "
               "the artefact that Achebe puts at the centre.",
    },
    {
        "num": "E9", "skill": "Command of Evidence",
        "passage": "A ring of heavy bells swung in a tower makes the tower sway. The movement is small, "
                   "but engineers have proposed that it feeds back into the ringing itself, because a "
                   "tower that leans away with a bell shortens that bell's swing and hands it back to "
                   "the ringer early.",
        "stem": "Which finding, if true, would most directly support the engineers' proposal?",
        "choices": [
            "In a tower measured to sway by four millimetres, the heaviest bell came back to hand consistently earlier than it did after the frame had been tied into the masonry and the sway halved.",
            "Ringers working in tall towers report that the bells feel heavier than their weight would suggest.",
            "Towers built of brick sway further under a ring of bells than towers built of stone.",
            "The sway of a tower increases with the number of bells being rung at once.",
        ],
        "answer": "A",
        "why": "The proposal is that sway changes the timing of a bell's return, so the finding has to "
               "hold the bell fixed and change the sway, which is what tying the frame into the masonry "
               "does. The finding that brick towers sway further than stone ones concerns how much "
               "towers move and never reaches the timing of the stroke.",
    },
]

# -------------------------------------------------------------------- Inferences
QUESTIONS += [
    {
        "num": "I1", "skill": "Inferences",
        "passage": "Metal shrinks as it cools, so a bell comes out of the mould a little smaller than the "
                   "mould that shaped it. Founders allow for this by sweeping the mould oversize by a "
                   "known proportion, but the proportion depends on the alloy and on how thick the wall "
                   "is at each point down the profile. A founder working with an unfamiliar alloy "
                   "therefore cannot _____",
        "stem": "Which choice most logically completes the text?",
        "choices": [
            "predict the dimensions of the finished bell as closely as usual.",
            "make a mould for the bell at all.",
            "melt the metal to the temperature the pour requires.",
            "cast a bell of the usual weight.",
        ],
        "answer": "A",
        "why": "The allowance that turns mould size into finished size is said to vary with the alloy, so "
               "an unknown alloy leaves that one step uncertain and nothing else. The option about being "
               "unable to make a mould overshoots the premise, which concerns how much oversize the "
               "mould should be and not whether it can be built.",
    },
    {
        "num": "I2", "skill": "Inferences",
        "passage": "In a pneumatic action a key opens a small valve that sends a puff of air along a lead "
                   "tube to a motor beside the pipe, and the motor opens the pallet. The tube may run "
                   "many metres, and the air takes a measurable time to travel it. Nothing in the key "
                   "itself changes as the puff travels. Compared with a tracker action, a pneumatic "
                   "action therefore _____",
        "stem": "Which choice most logically completes the text?",
        "choices": [
            "inserts a delay between key and pipe that the finger has no way of sensing.",
            "needs more wind to sound the same pipe.",
            "cannot be used on instruments above a certain size.",
            "makes every pipe in the instrument sound louder.",
        ],
        "answer": "A",
        "why": "The passage supplies a measurable travel time and then says the key itself gives no sign "
               "of it, which together make a lag the player cannot feel. The option about more wind "
               "introduces a quantity the text never raises; what it describes is a signal in transit, "
               "not a larger supply.",
    },
    {
        "num": "I3", "skill": "Inferences",
        "passage": "A tuner setting equal temperament cannot check a fifth by listening for a pure "
                   "interval, because no fifth in the tuning is pure. Each fifth is instead set to beat "
                   "at a stated rate, and the rate that is right for one fifth is wrong for the fifth a "
                   "semitone above it. Setting the temperament by ear accordingly depends on _____",
        "stem": "Which choice most logically completes the text?",
        "choices": [
            "counting rather than on recognising a sound as clean.",
            "tuning all the octaves before any of the fifths.",
            "an instrument whose pitch does not drift during the work.",
            "leaving one fifth somewhere in the octave pure.",
        ],
        "answer": "A",
        "why": "With no pure interval available and a different beat rate required at each step, the only "
               "thing left for the ear to do is register a rate against time. The option about leaving "
               "one fifth pure is ruled out by the opening sentence, which says no fifth in the tuning "
               "is pure.",
    },
    {
        "num": "I4", "skill": "Inferences",
        "passage": "Air is not sealed into an ice sheet at the surface but tens of metres down, where the "
                   "snow finally closes; until then the air in the pores exchanges freely with the "
                   "atmosphere above. The gas in a bubble is therefore younger than the ice around it, "
                   "and the difference is greatest where snow accumulates slowly, since the closing "
                   "takes longer. A core drilled at a site of low accumulation will accordingly _____",
        "stem": "Which choice most logically completes the text?",
        "choices": [
            "show a wider gap between the age of its trapped gas and the age of the ice enclosing it.",
            "hold gas older than the ice enclosing it.",
            "contain fewer bubbles than a core from a snowier site.",
            "yield no usable measurement of trapped gas at all.",
        ],
        "answer": "A",
        "why": "Slow accumulation lengthens the time the pores stay open, and the passage states that the "
               "age difference grows with that time. The option putting the gas older than the ice "
               "reverses the direction the passage establishes, which is that exchange continues after "
               "the ice around it has formed.",
    },
    {
        "num": "I5", "skill": "Inferences",
        "passage": "A window seen from inside is lit by whatever stands behind it, and how it looks "
                   "depends on how much of that light the glass scatters instead of passing straight "
                   "through. Cleaning takes off the grime that dims a window; restorers have found that "
                   "it also takes off a pitted layer of corrosion that had been scattering light across "
                   "the whole surface. A window cleaned down to bare glass will therefore look _____",
        "stem": "Which choice most logically completes the text?",
        "choices": [
            "brighter than before but flatter.",
            "darker than before but more even.",
            "unchanged except when seen from outside.",
            "cloudier than before in strong sunlight.",
        ],
        "answer": "A",
        "why": "Removing grime lets more light through while removing the pitted layer takes away the "
               "scattering that spread light across the surface, so the window gains in brightness and "
               "loses in modelling. The option predicting a darker result contradicts the removal of "
               "grime that the passage says dims the window.",
    },
    {
        "num": "I6", "skill": "Inferences",
        "passage": "A bell rung full circle stands still for an instant at the top of each stroke, and a "
                   "ringer's control over it is exercised during that instant. A very light bell passes "
                   "through the balance quickly and leaves almost no time to act; a heavier one lingers "
                   "there. A tower teaching beginners will therefore usually start them on _____",
        "stem": "Which choice most logically completes the text?",
        "choices": [
            "a bell heavy enough to give them time at the balance.",
            "the lightest bell hanging in the tower.",
            "a bell that is not hung to swing at all.",
            "whichever bell the band does not need that evening.",
        ],
        "answer": "A",
        "why": "Control is said to happen in the instant at the balance, and weight is what lengthens that "
               "instant, so a learner needs the longer one. The option choosing the lightest bell selects "
               "the case the passage describes as leaving almost no time to act.",
    },
]
