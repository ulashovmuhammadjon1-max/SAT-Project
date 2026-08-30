# AP HUMAN GEOGRAPHY 3.7 Diffusion of Religion and Language -- 30 questions
# CED Course Framework V.1, Unit 3. Enduring understanding IMP-3; learning
# objective IMP-3.B, "Explain what factors lead to the diffusion of
# universalizing and ethnic religions."
#
# Essential knowledge, in full -- five statements, the most of any topic in
# Unit 3:
#   IMP-3.B.1  Language families, languages, dialects, world religions, ethnic
#              cultures, and gender roles diffuse from cultural hearths.
#   IMP-3.B.2  Diffusion of language families, including Indo-European, and
#              religious patterns and distributions can be visually represented
#              on maps, in charts and toponyms, and in other representations.
#   IMP-3.B.3  Religions have distinct places of origin from which they diffused
#              to other locations through different processes. Practices and
#              belief systems impacted how widespread the religion diffused.
#   IMP-3.B.4  Universalizing religions, including Christianity, Islam,
#              Buddhism, and Sikhism, are spread through expansion and
#              relocation diffusion.
#   IMP-3.B.5  Ethnic religions, including Hinduism and Judaism, are generally
#              found near the hearth or spread through relocation diffusion.
#
# THE CENTRAL DISTINCTION, and it is citable rather than inferred, because the
# CED assigns each religion by name:
#   universalizing  Christianity, Islam, Buddhism, Sikhism -- these seek
#                   adherents everywhere, so BOTH expansion and relocation
#                   diffusion are available to them (IMP-3.B.4)
#   ethnic          Hinduism, Judaism -- these are bound to a particular people
#                   and place, so they stay near the hearth or move by
#                   RELOCATION ONLY (IMP-3.B.5)
# IMP-3.B.3 supplies the reason: "practices and belief systems impacted how
# widespread the religion diffused". A faith that instructs adherents to seek
# converts spreads by contact; one that does not spreads only when its people
# move. Items 3-9, 12-16, 19, 22, 26 and 27 turn on that pair.
#
# WHAT THIS MODULE WILL AND WILL NOT ASSERT ABOUT REAL RELIGIONS AND LANGUAGES.
# The four universalizing and two ethnic religions are named by the CED and are
# used as named. Their hearths are standard, uncontested course content and are
# stated only at that level: Christianity and Judaism in the eastern
# Mediterranean, Islam on the Arabian Peninsula, Hinduism in South Asia, Buddhism
# in the northern South Asian subcontinent, Sikhism in the Punjab. Where a fact
# is genuinely disputed among scholars, this module says so rather than picking a
# side -- item 21 does exactly that for the Indo-European hearth, which is
# contested between an Anatolian and a steppe origin. SOCIAL_BRIEF.md's rule is
# that an uncertain claim is cut or reported, never guessed.
#
# IMP-3.B.2 is the "how do you see it" statement, and it names TOPONYMS as
# evidence alongside maps and charts. Items 10, 17, 24 and 28 use them.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g3_7.py. FIVE choices (A-E).
TOPIC = ("3.7", "Diffusion of Religion and Language", 3)

QUESTIONS = [
 dict(q="According to the framework, what do language families, religions, ethnic cultures, and gender roles have in common?",
   choices=[
     "Each diffuses from a cultural hearth",
     "Each is unchanging once established",
     "Each is confined to a single country",
     "Each spreads only through migration",
     "Each is determined by physical geography"],
   ans=0,
   why="EK IMP-3.B.1 lists all of these as things that diffuse from cultural hearths. A hearth is the area where a trait originated and from which it spread, and naming so varied a list under one mechanism is the statement's point."),

 dict(q="What is a cultural hearth?",
   choices=[
     "The area in which a cultural trait originated and from which it spread outward",
     "The area in which a trait is most widely practised today",
     "The geographic centre of a country",
     "The place where a trait was first written down",
     "The area with the largest population practising a trait"],
   ans=0,
   why="EK IMP-3.B.1 makes cultural hearths the source areas from which these traits diffuse. Origin and present concentration are different things, and a trait can be almost absent from the region where it began."),

 dict(q="Which four religions does the framework name as universalizing?",
   choices=[
     "Christianity, Islam, Buddhism, and Sikhism",
     "Christianity, Islam, Hinduism, and Judaism",
     "Buddhism, Sikhism, Hinduism, and Judaism",
     "Christianity, Judaism, Islam, and Buddhism",
     "Islam, Hinduism, Sikhism, and Judaism"],
   ans=0,
   why="EK IMP-3.B.4 names exactly these four. EK IMP-3.B.5 names Hinduism and Judaism as its examples of ethnic religions, so any option mixing the two lists misassigns at least one religion."),

 dict(q="Which two religions does the framework name as ethnic religions?",
   choices=[
     "Hinduism and Judaism",
     "Buddhism and Sikhism",
     "Christianity and Islam",
     "Hinduism and Buddhism",
     "Judaism and Christianity"],
   ans=0,
   why="EK IMP-3.B.5 names Hinduism and Judaism as its examples of ethnic religions found near the hearth or spread through relocation diffusion. The other four religions named in this topic appear in EK IMP-3.B.4's universalizing list."),

 dict(q="According to the framework, universalizing religions spread through",
   choices=[
     "Both expansion and relocation diffusion",
     "Relocation diffusion only",
     "Expansion diffusion only",
     "Neither expansion nor relocation diffusion",
     "Stimulus diffusion only"],
   ans=0,
   why="EK IMP-3.B.4 states that universalizing religions are spread through expansion AND relocation diffusion. Both channels are open because such a religion seeks adherents wherever it can reach them, whether by contact or by carriage."),

 dict(q="According to the framework, ethnic religions are",
   choices=[
     "Generally found near the hearth or spread through relocation diffusion",
     "Spread through expansion diffusion only",
     "Spread through both expansion and relocation diffusion",
     "Never found outside their hearth",
     "Spread through stimulus diffusion"],
   ans=0,
   why="EK IMP-3.B.5 uses exactly this wording. The word GENERALLY matters: ethnic religions are found beyond the hearth wherever their adherents have moved, but the mechanism that brought them there is relocation rather than conversion."),

 dict(q="Why does an ethnic religion not usually spread by expansion diffusion?",
   choices=[
     "Its practices and beliefs tie it to a particular people, history, and place rather than instructing adherents to seek converts",
     "Its adherents never travel",
     "Its beliefs are too complicated to explain",
     "Its adherents are always too few",
     "Expansion diffusion applies only to languages"],
   ans=0,
   why="EK IMP-3.B.3 states that practices and belief systems impacted how widespread a religion diffused, and EK IMP-3.B.5 records the result for ethnic religions. Where membership is bound to descent and to a homeland, conversion is not the mechanism through which the faith grows."),

 dict(q="A community of one ethnic religion's adherents establishes itself far from the religion's hearth after a period of emigration. Which type of diffusion moved the religion there?",
   choices=[
     "Relocation diffusion, since the faith travelled with the people who held it",
     "Contagious diffusion, since neighbours were converted",
     "Hierarchical diffusion, since the community settled in a city",
     "Stimulus diffusion, since practices were adapted",
     "No diffusion, since the religion remains ethnic"],
   ans=0,
   why="EK IMP-3.B.5 names relocation diffusion as the way ethnic religions reach places beyond the hearth. The faith is present in the new location because its adherents are, which is exactly what relocation means."),

 dict(q="A universalizing religion spreads into a region where missionaries convert local populations who had no prior connection to the faith. Which type of diffusion is this?",
   choices=[
     "Expansion diffusion, since the religion spreads outward by contact while remaining at its source",
     "Relocation diffusion, since missionaries travelled",
     "Stimulus diffusion, since local practices were incorporated",
     "No diffusion, since converts are not migrants",
     "Hierarchical diffusion only, since missions began in cities"],
   ans=0,
   why="EK IMP-3.B.4 says universalizing religions spread through expansion as well as relocation diffusion. Conversion of a resident population is spread by contact from a source that keeps the faith, which is the definition of expansion from Topic 3.4."),

 dict(q="How does the framework say religious and linguistic diffusion can be visually represented?",
   choices=[
     "On maps, in charts and toponyms, and in other representations",
     "Only on maps",
     "Only in written texts",
     "Only through census tables",
     "It cannot be represented visually"],
   ans=0,
   why="EK IMP-3.B.2 lists maps, charts, toponyms and other representations. Including toponyms in a list of VISUAL representations is deliberate: a place name on a map is evidence about who named the place and in what language."),

 dict(q="Which of the following best states what the framework means by a language family?",
   choices=[
     "A group of languages descended from a shared ancestral language, and therefore related to one another",
     "A group of languages spoken in the same country",
     "A group of languages with similar alphabets",
     "A group of languages used for trade",
     "A group of languages spoken by the same number of people"],
   ans=0,
   why="EK IMP-3.B.1 names language families among the things that diffuse from cultural hearths, and EK IMP-3.B.2 names Indo-European as an example. A family is defined by common descent, which is why it can be mapped back to a hearth at all."),

 dict(q="Which is the most important reason universalizing religions have far wider distributions than ethnic religions?",
   choices=[
     "Their belief systems direct adherents to bring others in, which opens expansion diffusion in addition to relocation",
     "Their adherents migrate more often",
     "They originated earlier in history",
     "Their hearths are more centrally located",
     "They have simpler practices"],
   ans=0,
   why="EK IMP-3.B.3 says practices and belief systems impacted how widespread a religion diffused, and EK IMP-3.B.4 and B.5 record the resulting difference in mechanism. A faith open to converts can grow without anyone moving, which no relocation-only faith can do."),

 dict(q="A universalizing religion is carried to a distant continent by settlers and then grows there through conversion of the resident population. Which framework statement covers both stages?",
   choices=[
     "That universalizing religions are spread through expansion AND relocation diffusion",
     "That ethnic religions spread through relocation diffusion",
     "That religions have distinct places of origin",
     "That language families diffuse from hearths",
     "That diffusion can be represented on maps"],
   ans=0,
   why="EK IMP-3.B.4 names both mechanisms in one sentence, and this case uses them in sequence: carriage by settlers is relocation and subsequent conversion is expansion. Naming both is what makes the answer complete."),

 dict(q="Which statement about the hearths of the religions the framework names is accurate?",
   choices=[
     "Christianity and Judaism arose in the eastern Mediterranean, Islam on the Arabian Peninsula, and Hinduism, Buddhism, and Sikhism in South Asia",
     "All six arose in South Asia",
     "All six arose in the eastern Mediterranean",
     "The hearths of these religions are unknown",
     "Each of the six arose on a different continent"],
   ans=0,
   why="EK IMP-3.B.3 states that religions have distinct places of origin, and these locations are standard, uncontested course content stated at region level. Two clusters of hearths -- southwest Asia and South Asia -- account for all six religions the CED names in this topic."),

 dict(q="A religion's adherents are concentrated overwhelmingly in and around the region where it began, with small communities elsewhere formed entirely by emigration. This distribution is characteristic of",
   choices=[
     "An ethnic religion, which is generally found near the hearth or spread through relocation diffusion",
     "A universalizing religion",
     "A religion that has never diffused at all",
     "A religion spread through contagious diffusion",
     "A religion spread through stimulus diffusion"],
   ans=0,
   why="EK IMP-3.B.5 describes exactly this distribution: near the hearth, plus communities formed where adherents moved. The absence of converted populations distant from the hearth is what separates the pattern from a universalizing one."),

 dict(q="Which observation would be strongest evidence that a religion diffuses by expansion as well as relocation?",
   choices=[
     "Large populations of adherents in regions where no substantial migration from the hearth ever occurred",
     "Adherents living in many countries",
     "Adherents concentrated near the hearth",
     "Adherents who speak many languages",
     "A religion with written scriptures"],
   ans=0,
   why="EK IMP-3.B.4 and B.5 differ on exactly this point, so the diagnostic must separate carriage from conversion. Adherents where nobody migrated from the hearth can only have been converted, which relocation alone cannot explain."),

 dict(q="A region's place names are overwhelmingly drawn from a language no longer spoken there. What does this evidence support?",
   choices=[
     "That speakers of that language once occupied the region, and that the linguistic landscape changed after they were displaced or assimilated",
     "That the language is still widely spoken there",
     "That place names are chosen randomly",
     "That the region has never been settled",
     "That place names cannot be used as evidence"],
   ans=0,
   why="EK IMP-3.B.2 names toponyms among the representations in which linguistic diffusion can be read. Names are unusually durable because changing them requires deliberate effort, so they outlast the population that coined them and record an earlier layer."),

 dict(q="Which pairing correctly matches a religion to the category the framework assigns it?",
   choices=[
     "Sikhism to universalizing and Judaism to ethnic",
     "Sikhism to ethnic and Judaism to universalizing",
     "Buddhism to ethnic and Hinduism to universalizing",
     "Islam to ethnic and Christianity to universalizing",
     "Christianity to ethnic and Buddhism to universalizing"],
   ans=0,
   why="EK IMP-3.B.4 names Sikhism among the universalizing religions and EK IMP-3.B.5 names Judaism among the ethnic ones. Every other pairing reverses at least one of the CED's own assignments."),

 dict(q="What does EK IMP-3.B.3 mean by saying practices and belief systems 'impacted how widespread the religion diffused'?",
   choices=[
     "What a religion teaches about membership and conversion determines which diffusion mechanisms are available to it",
     "That all religions diffuse to the same extent",
     "That geography alone determines a religion's spread",
     "That belief systems are irrelevant to diffusion",
     "That only political power determines religious spread"],
   ans=0,
   why="EK IMP-3.B.3 makes the content of a faith a cause of its geographic extent, which is an unusual and specific claim. Whether a religion instructs adherents to seek converts decides whether expansion diffusion is open to it at all."),

 dict(q="Which is the best example of religious diffusion represented in a chart rather than on a map?",
   choices=[
     "A table of adherents by world region at three dates, showing where growth occurred",
     "A shaded map of majority religion by country",
     "A place name of religious origin",
     "A photograph of a place of worship",
     "A description of a pilgrimage route"],
   ans=0,
   why="EK IMP-3.B.2 names maps, charts and toponyms as separate kinds of representation. A chart holds quantities and changes over time that a shaded map cannot show, which is why the statement lists more than one form."),

 dict(q="A student asks where the Indo-European language family originated. What is the most accurate answer a geography course can give?",
   choices=[
     "The hearth is genuinely disputed among scholars, with an Anatolian origin and a steppe origin the two leading proposals",
     "The hearth is known with certainty to be in western Europe",
     "The hearth is known with certainty to be in South Asia",
     "Indo-European has no hearth",
     "Indo-European is not a language family"],
   ans=0,
   why="EK IMP-3.B.2 names Indo-European as its example of a language family whose diffusion can be represented, and EK IMP-3.B.1 places hearths behind such diffusion, but the CED does not locate this one. The honest answer names the disagreement rather than inventing a settled fact."),

 dict(q="Two religions originated within a few hundred kilometres of one another, yet one is now practised on every continent by hundreds of millions and the other remains concentrated near its hearth. What best explains the difference?",
   choices=[
     "Their belief systems differ on whether adherents should seek converts, which opens expansion diffusion to one and not the other",
     "One hearth is closer to the sea",
     "One religion is much older than the other",
     "One religion has written scriptures and the other does not",
     "The difference cannot be explained"],
   ans=0,
   why="EK IMP-3.B.3 says practices and belief systems impacted how widespread a religion diffused, which is precisely a claim that proximity of hearths does not determine extent. Holding geography roughly constant leaves the content of the faiths as the explanatory difference."),

 dict(q="Which of the following diffuses from a cultural hearth according to EK IMP-3.B.1, in addition to religions and languages?",
   choices=[
     "Gender roles and ethnic cultures",
     "Climate zones and landforms",
     "Soil types and river systems",
     "Latitude and elevation",
     "Mineral deposits and ore bodies"],
   ans=0,
   why="EK IMP-3.B.1's list is language families, languages, dialects, world religions, ethnic cultures AND gender roles. The distractors are all physical features, which do not diffuse from hearths because nobody transmits them."),

 dict(q="A geographer maps the distribution of a religion's place names across a continent and finds them dense along old routes and sparse elsewhere. What does this suggest?",
   choices=[
     "The religion diffused along those routes, since naming follows the arrival of the people or the faith that does the naming",
     "Place names are unrelated to religion",
     "The religion originated on the continent",
     "The routes were built after the names were given",
     "Toponyms cannot be mapped"],
   ans=0,
   why="EK IMP-3.B.2 names toponyms among the representations of religious and linguistic diffusion. A pattern of names concentrated along corridors is the diffusion channel made visible, since names are given where the naming population went."),

 dict(q="Why does the framework include DIALECTS alongside languages and language families in its list of things that diffuse from hearths?",
   choices=[
     "A dialect also originates in a particular area and spreads outward from it, so the same hearth-and-diffusion account applies at a finer scale",
     "Dialects are the same thing as language families",
     "Dialects do not actually diffuse",
     "Dialects diffuse only through writing",
     "Dialects are physical rather than cultural features"],
   ans=0,
   why="EK IMP-3.B.1 lists language families, languages and dialects together, which places the same process at three scales. A regional pronunciation spreads from where it arose exactly as a language family does, only over a smaller area."),

 dict(q="Adherents of two religions are recorded by region. Using the table, which religion's distribution is characteristic of a universalizing religion?",
   table=dict(
     headers=["Region", "Religion 1 (millions of adherents)", "Religion 2 (millions of adherents)"],
     rows=[
       ["Hearth region", "310", "940"],
       ["Neighbouring regions", "560", "22"],
       ["Other continents", "1,140", "6"],
       ["Total", "2,010", "968"]]),
   choices=[
     "Religion 1, with 85 percent of adherents outside the hearth region and the largest group on other continents",
     "Religion 2, with more adherents in the hearth region than Religion 1 has",
     "Religion 1, because it has more adherents in total",
     "Religion 2, because its adherents are concentrated",
     "Neither, since both have adherents outside the hearth"],
   ans=0,
   why="One religion holds 310 million of 2,010 in its hearth, so 85 percent are elsewhere and the largest single group is on other continents; the other holds 940 of 968, or 97 percent, at home. EK IMP-3.B.4 and B.5 differ on exactly that distribution, and total size is not the criterion."),

 dict(q="Growth in adherents is broken down by source for two religions. Using the table, which religion is diffusing by expansion?",
   table=dict(
     headers=["Source of new adherents over a decade", "Religion A", "Religion B"],
     rows=[
       ["Born to existing adherents", "41,000,000", "18,000,000"],
       ["Conversion of previously unaffiliated people", "26,000,000", "120,000"],
       ["Arrived through migration of adherents", "3,000,000", "2,900,000"]]),
   choices=[
     "Religion A, since 26 million of its new adherents are converts against 120,000 for the other",
     "Religion B, since migration accounts for a larger share of its growth",
     "Religion A, since it has more adherents born to existing members",
     "Religion B, since it grew at all",
     "Neither, since both gained adherents"],
   ans=0,
   why="Conversion is 37 percent of one religion's growth and under one percent of the other's, while migration contributes almost the same absolute number to each. EK IMP-3.B.4 opens expansion diffusion to universalizing religions, and conversion of previously unaffiliated people is what expansion looks like counted."),

 dict(q="Place names of two linguistic origins are counted across four districts of one region. Using the table, what does the pattern indicate?",
   table=dict(
     headers=["District", "Place names of older linguistic origin", "Place names of later linguistic origin"],
     rows=[
       ["District 1", "184", "12"],
       ["District 2", "96", "88"],
       ["District 3", "41", "170"],
       ["District 4", "9", "213"]]),
   choices=[
     "A gradient from districts still dominated by the older naming layer to districts almost entirely renamed, which maps the advance of the later language",
     "That the older language was never spoken in the region",
     "That the later language arrived everywhere at the same time",
     "That the two languages are unrelated",
     "That place names give no information about language"],
   ans=0,
   why="The older layer falls from 184 to 9 across the four districts while the later layer rises from 12 to 213, with the crossover in the second district. EK IMP-3.B.2 names toponyms among the representations of linguistic diffusion, and a gradient of this kind is a diffusion front made visible."),

 dict(q="Speakers of a language family's branches are recorded. Using the table, what share of the family's speakers belong to its largest branch?",
   table=dict(
     headers=["Branch", "Speakers (millions)"],
     rows=[
       ["Branch 1", "1,300"],
       ["Branch 2", "700"],
       ["Branch 3", "480"],
       ["Branch 4", "320"],
       ["All remaining branches", "200"]]),
   choices=[
     "About 43 percent, since 1,300 of 3,000 million speakers belong to the largest branch",
     "About 65 percent, since the largest branch has 1,300 million speakers",
     "About 13 percent, since there are five categories",
     "About 100 percent, since all branches belong to the family",
     "The share cannot be calculated without knowing the number of languages"],
   ans=0,
   why="The five rows total 3,000 million speakers and the largest branch holds 1,300 of them, which is 43.3 percent. A branch holding well under half of a family's speakers is why a family cannot be described by its largest branch alone."),

 dict(q="Modes by which a religion reached four regions are recorded. Using the table, which region's case is relocation diffusion alone?",
   table=dict(
     headers=["Region", "Adherents arriving as migrants", "Adherents gained by conversion", "Adherents today"],
     rows=[
       ["Region W", "2,400,000", "0", "2,600,000"],
       ["Region X", "180,000", "14,000,000", "14,900,000"],
       ["Region Y", "900,000", "3,200,000", "4,300,000"],
       ["Region Z", "60,000", "8,700,000", "9,100,000"]]),
   choices=[
     "Region W, where every adherent traces to migration and none to conversion",
     "Region X, where the most adherents were gained by conversion",
     "Region Y, where migration and conversion both contributed",
     "Region Z, where the fewest migrants arrived",
     "All four, since migrants arrived everywhere"],
   ans=0,
   why="Exactly one region records zero adherents gained by conversion, so its present community can only descend from the 2.4 million who arrived. EK IMP-3.B.5 names relocation diffusion as the mechanism by which a religion reaches a place without converting anyone there."),
]
