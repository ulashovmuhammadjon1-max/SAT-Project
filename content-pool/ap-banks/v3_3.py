# AP U.S. GOVERNMENT AND POLITICS 3.3 First Amendment: Freedom of Speech -- 30 questions
# CED V.1 (c) 2026, Unit 3 Civil Liberties and Civil Rights.
# Learning objective 3.3.A: explain THE EXTENT TO WHICH the Supreme Court's
# interpretation of the First Amendment reflects a commitment to free speech.
# Suggested skill for this topic (CED p. 84): SCOTUS analysis.
#
# Essential knowledge relied on, with the CED's own parentheticals, which are
# examinable text:
#   EK 3.3.A.1 -- "The Supreme Court has held that speech, including SYMBOLIC
#     SPEECH (nonverbal action that communicates an idea or belief), is
#     protected by the First Amendment."
#   EK 3.3.A.2 -- "Efforts to balance social order and individual freedom are
#     reflected in interpretations of the First Amendment that LIMIT speech,
#     including:
#       i.   TIME, PLACE, AND MANNER regulations that impose restrictions such
#            as limits on the time of day an event can be held, limits on where
#            an event can be held, and limits on the noise levels at an event
#       ii.  Limitations on some obscene and offensive communication.
#       iii. Protections against DEFAMATION (language that harms the reputation
#            of another) including LIBEL (written communication) and SLANDER
#            (oral communication).
#       iv.  Restrictions on speech that create a CLEAR AND PRESENT DANGER and
#            subsequent interpretations which have refined those restrictions."
#
# THE TOPIC IS THE TENSION, NOT EITHER SIDE OF IT. EK 3.3.A.1 says speech is
# protected; EK 3.3.A.2 lists four ways it is limited. LO 3.3.A asks about THE
# EXTENT of the commitment, which is a question a student can only answer if
# they hold both statements at once. Items 1 to 8 are protection, items 9 to 20
# are the four limits, and items 27 to 30 ask how far the commitment reaches.
#
# THREE DEFINITIONS THE CED SUPPLIES AND A BANK MUST NOT PARAPHRASE:
#   * SYMBOLIC SPEECH is "nonverbal action that communicates an idea or belief."
#     Not "speech-like conduct", not "expressive activity" -- the framework's
#     wording is what an exam will use.
#   * DEFAMATION is "language that harms the reputation of another", with LIBEL
#     written and SLANDER oral. Students reverse the last two constantly, and
#     item 15 exists for exactly that.
#   * TIME, PLACE, AND MANNER regulations are illustrated by the CED itself with
#     three examples: time of day, location, and noise level. Item 11 uses them.
#
# EK 3.3.A.2.iv's TAIL IS LOAD-BEARING: restrictions on clear-and-present-danger
# speech "AND SUBSEQUENT INTERPRETATIONS WHICH HAVE REFINED THOSE RESTRICTIONS."
# The framework does not present Schenck's formula as the current test; it
# presents it as a starting point later refined. Item 19 keys on that, because a
# bank that stops at Schenck teaches a rule that has been narrowed.
#
# Documents the CED attaches to 3.3.A (p. 26-27): "Letter from a Birmingham
# Jail."
# Required cases the CED attaches to 3.3.A (p. 31-32): Schenck v. United States,
# Tinker v. Des Moines.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: the First Amendment and "Letter from a
# Birmingham Jail" are quoted verbatim. Non-required cases are described with
# the facts a student needs and are never named. Both tables are labelled
# hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere; gov345_check
# enforces the hyphen half and the verifier enforces both.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("3.3", "First Amendment: Freedom of Speech", 3)

_CLAIMS = ("In a hypothetical study, the table reports how a national high court disposed of "
           "free speech claims in four categories over one decade.")
_CLAIMS_TABLE = dict(
    headers=["Category of claim", "Claims brought", "Claims upheld for the speaker"],
    rows=[["Political speech in a public forum", "142", "119"],
          ["Symbolic expression", "68", "51"],
          ["Speech alleged to be defamatory", "94", "26"],
          ["Speech alleged to create imminent danger", "37", "9"]])

_RULES = ("In a hypothetical municipality, the table lists four ordinances restricting a "
          "planned demonstration and what each restricts.")
_RULES_TABLE = dict(
    headers=["Ordinance", "What it restricts", "Does it depend on the message?"],
    rows=[["Amplified sound above a set level after ten at night", "Manner and time", "No"],
          ["No demonstrations inside the courthouse itself", "Place", "No"],
          ["Permits required for gatherings over five hundred people", "Manner", "No"],
          ["No demonstrations criticizing the city council", "Content of the message", "Yes"]])

QUESTIONS = [
 dict(q="According to the course framework, symbolic speech is",
   choices=[
     "nonverbal action that communicates an idea or belief",
     "any spoken statement made in a public place",
     "written communication that harms another's reputation",
     "speech that creates a clear and present danger",
     "communication that a court has found obscene"], ans=0,
   why="EK 3.3.A.1 gives this definition in its own parenthesis. The other options define defamation, the danger standard and obscenity, which are all limits on speech rather than kinds of it."),

 dict(q="According to the course framework, what has the Supreme Court held about symbolic speech?",
   choices=[
     "It is protected by the First Amendment",
     "It is protected only when accompanied by spoken words",
     "It receives no First Amendment protection",
     "It is protected only outside of school buildings",
     "It is protected only when a majority approves of the message"], ans=0,
   why="EK 3.3.A.1 says speech 'including symbolic speech' is protected by the First Amendment, which means nonverbal expression is inside the guarantee rather than outside it."),

 dict(q="Read the following excerpt.\n\n“Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances.”\n—U.S. Constitution, First Amendment\n\nHow does the course framework's account of speech limits fit this text?",
   choices=[
     "The text states the protection in absolute terms, but the Court's interpretations have recognized categories in which speech may be limited",
     "The text lists the exceptions to free speech that the Court has applied",
     "The text applies only to symbolic speech",
     "The text permits Congress to abridge speech whenever public order requires it",
     "The text has no bearing on speech restrictions imposed by state governments"], ans=0,
   why="The Amendment's words admit no exception, and EK 3.3.A.2's four limits come from interpretation rather than from the text. EK 3.7's selective incorporation is why the guarantee reaches the states."),

 dict(q="In Tinker v. Des Moines Independent Community School District (1969), the Supreme Court held that a prohibition against public school students wearing black armbands to protest the Vietnam War violated the students' freedom of speech under the First Amendment. Which claim from the course framework does the case most directly support?",
   choices=[
     "That symbolic speech, nonverbal action communicating an idea or belief, is protected by the First Amendment",
     "That speech creating a clear and present danger may be limited",
     "That defamatory language may be restricted",
     "That time, place and manner regulations are permissible",
     "That obscene communication may be limited"], ans=0,
   why="An armband is nonverbal action communicating a belief, which is EK 3.3.A.1's symbolic speech, and the CED states the holding as a violation of the students' freedom of speech."),

 dict(q="A student wears a plain colored sash to school to express a political position, and the school prohibits it although no disruption occurs. Which required case is the closest comparison?",
   choices=[
     "Tinker v. Des Moines (1969), in which a ban on students wearing black armbands to protest the war violated their freedom of speech",
     "Schenck v. United States (1919), in which speech creating a clear and present danger was held unprotected",
     "Engel v. Vitale (1962), in which school sponsorship of religious activities was held to violate the Establishment Clause",
     "Wisconsin v. Yoder (1972), in which compelling Amish students to attend school past the eighth grade violated the Free Exercise Clause",
     "New York Times Co. v. United States (1971), in which the Court established a heavy presumption against prior restraint"], ans=0,
   why="The facts match almost exactly: a public school, a silent nonverbal symbol, a political message, no disruption. The other four required cases concern danger, religion and the press."),

 dict(q="Which of the following would be symbolic speech under the framework's definition?",
   choices=[
     "Silently displaying a banner with no words at a public rally",
     "Publishing a newspaper editorial",
     "Delivering a speech at a public meeting",
     "Sending a letter to a member of Congress",
     "Testifying before a legislative committee"], ans=0,
   why="EK 3.3.A.1's definition requires NONVERBAL action that communicates an idea or belief. The other four options are all verbal or written communication, which is speech in the ordinary sense rather than symbolic speech."),

 dict(q="Why does the framework treat the protection of symbolic speech as a significant extension of the First Amendment?",
   choices=[
     "The Amendment's text speaks of speech and the press, so covering nonverbal action required an interpretation of what counts as speech",
     "Symbolic speech is mentioned expressly in the Amendment's text",
     "Symbolic speech is the only form of expression the Amendment protects",
     "Symbolic speech was added to the Amendment by later ratification",
     "Symbolic speech receives greater protection than spoken words"], ans=0,
   why="The text names speech and the press, so EK 3.3.A.1's holding rests on reading nonverbal expression into that guarantee. Nothing in the Amendment mentions symbolic speech by name."),

 dict(q="According to the course framework, what do the First Amendment interpretations that LIMIT speech reflect?",
   choices=[
     "Efforts to balance social order and individual freedom",
     "A judgment that the First Amendment protects nothing",
     "The preferences of whichever party controls Congress",
     "A requirement that all speech be approved in advance",
     "The Court's view that symbolic speech deserves no protection"], ans=0,
   why="EK 3.3.A.2 opens with exactly this: the limiting interpretations reflect 'efforts to balance social order and individual freedom.' That balance is what LO 3.3.A's phrase 'the extent to which' asks a student to assess."),

 dict(q="According to the course framework, time, place, and manner regulations impose restrictions such as",
   choices=[
     "limits on the time of day an event can be held, on where it can be held, and on noise levels",
     "limits on which political positions may be expressed at an event",
     "limits on who may attend an event based on their views",
     "a requirement that organizers submit their speeches for approval",
     "a prohibition on all outdoor gatherings"], ans=0,
   why="EK 3.3.A.2.i gives these three illustrations itself: time of day, location and noise levels. Each is about the circumstances of expression rather than about its content."),

 dict(q="What distinguishes a permissible time, place, and manner regulation from an impermissible restriction on speech?",
   choices=[
     "It restricts the circumstances of expression rather than the message expressed",
     "It restricts written communication rather than spoken communication",
     "It applies only to symbolic speech",
     "It restricts messages a majority of residents oppose",
     "It applies only during declared emergencies"], ans=0,
   why="EK 3.3.A.2.i's three examples -- time of day, location, noise -- are all content-neutral circumstances. A rule that turned on which message was being expressed would not be a time, place and manner regulation at all."),

 dict(q="A city requires organizers of any gathering of more than a thousand people to obtain a permit specifying the route and the hours, and applies the requirement to every gathering regardless of subject. How is this rule best characterized?",
   choices=[
     "A time, place and manner regulation, since it governs circumstances and applies without regard to the message",
     "A content restriction, since it requires prior permission",
     "A prohibition on symbolic speech, since it applies to gatherings",
     "A restriction on defamation, since large gatherings may harm reputations",
     "A clear and present danger restriction, since large crowds may become dangerous"], ans=0,
   why="EK 3.3.A.2.i's category covers rules about when, where and how, and the stem specifies the rule applies regardless of subject. A permit requirement is not by itself a judgment about content."),

 dict(q="According to the course framework, defamation is",
   choices=[
     "language that harms the reputation of another",
     "language that creates a clear and present danger",
     "nonverbal action communicating an idea or belief",
     "communication a court has found obscene",
     "any criticism of a public official"], ans=0,
   why="EK 3.3.A.2.iii gives this definition in its own parenthesis. Criticism of officials is not defamation unless it meets that standard, which is why the fifth option is false."),

 dict(q="According to the course framework, what is the difference between libel and slander?",
   choices=[
     "Libel is written communication and slander is oral communication",
     "Libel is oral communication and slander is written communication",
     "Libel harms reputation and slander creates danger",
     "Libel applies to public figures and slander to private individuals",
     "There is no difference; the two terms are interchangeable"], ans=0,
   why="EK 3.3.A.2.iii is explicit: libel is written and slander is oral. Students reverse these constantly, and the framework's own parenthesis settles it."),

 dict(q="A radio host states on air that a local business owner has been convicted of fraud, which is false and damages the owner's business. Under the framework's categories, this is best described as",
   choices=[
     "slander, since the communication was oral",
     "libel, since the communication was broadcast",
     "obscenity, since the statement was offensive",
     "symbolic speech, since it communicated a belief",
     "a time, place and manner problem, since it occurred during a broadcast"], ans=0,
   why="EK 3.3.A.2.iii defines slander as oral communication, and a spoken statement on air is oral. Reputational harm makes it defamation; the medium being spoken makes it slander rather than libel."),

 dict(q="Why does the framework include protections against defamation among the LIMITS on speech rather than among its protections?",
   choices=[
     "Allowing a person to recover for reputational harm necessarily restricts what a speaker may say",
     "Defamation law protects speakers rather than subjects",
     "Defamation is a form of symbolic speech",
     "Defamation law applies only to government officials",
     "Defamation law is imposed by the First Amendment's text"], ans=0,
   why="EK 3.3.A.2 lists defamation protections among interpretations 'that limit speech,' because the protection runs to the person harmed and the limit falls on the speaker."),

 dict(q="According to the course framework, which category of communication may be subject to limitation as obscene or offensive?",
   choices=[
     "Some obscene and offensive communication, rather than all of it",
     "All communication a listener finds offensive",
     "All communication about political subjects",
     "All symbolic speech",
     "All communication that criticizes a public official"], ans=0,
   why="EK 3.3.A.2.ii says 'limitations on SOME obscene and offensive communication.' The qualifier is the framework's own, and dropping it would make any offensive speech restrictable."),

 dict(q="In Schenck v. United States (1919), the Supreme Court held that speech creating a clear and present danger was not protected by the First Amendment and could be limited. Which category of EK 3.3.A.2 does the case establish?",
   choices=[
     "Restrictions on speech that create a clear and present danger",
     "Time, place, and manner regulations",
     "Limitations on obscene and offensive communication",
     "Protections against defamation",
     "Protection for symbolic speech"], ans=0,
   why="The CED states the Schenck holding in exactly the words EK 3.3.A.2.iv uses, so the case is the source of that category rather than of any other."),

 dict(q="EK 3.3.A.2.iv does not stop at the clear and present danger formula. What does it add?",
   choices=[
     "Subsequent interpretations which have refined those restrictions",
     "That the formula applies only during wartime",
     "That the formula was adopted by constitutional amendment",
     "That the formula applies only to symbolic speech",
     "That the formula has been abandoned entirely"], ans=0,
   why="EK 3.3.A.2.iv's own tail is 'and subsequent interpretations which have refined those restrictions,' so the framework presents Schenck's formula as a starting point rather than as the current test."),

 dict(q="Why does it matter that the framework describes the danger standard as having been REFINED by later interpretation?",
   choices=[
     "A student who treats the original formula as the current test will overstate how easily speech may be restricted",
     "It means the First Amendment no longer protects political speech",
     "It means Schenck was overruled by constitutional amendment",
     "It means the Court has abandoned all limits on dangerous speech",
     "It means the formula now applies to defamation as well"], ans=0,
   why="EK 3.3.A.2.iv's refinement clause narrows the category over time, so reciting the 1919 formula as though nothing followed it misstates the current extent of the protection LO 3.3.A asks about."),

 dict(q="Which pairing of a restriction with its category in EK 3.3.A.2 is correct?",
   choices=[
     "A rule barring amplified sound after ten at night, with time, place and manner",
     "A rule barring criticism of the mayor, with time, place and manner",
     "A false written statement damaging a person's business, with obscenity",
     "A silent armband worn in school, with clear and present danger",
     "An oral statement harming a reputation, with libel"], ans=0,
   why="A noise limit is one of EK 3.3.A.2.i's own examples. Barring criticism of an official is a content restriction, a false written statement is libel, an armband is protected symbolic speech, and an oral statement is slander."),

 dict(q="Read the following excerpt.\n\n“Injustice anywhere is a threat to justice everywhere. We are caught in an inescapable network of mutuality, tied in a single garment of destiny.”\n—Martin Luther King, Jr., “Letter from a Birmingham Jail,” 1963\n\nHow does this passage relate to the First Amendment's protection of expression?",
   choices=[
     "It is an argument for the value of speech and protest that reaches beyond the immediate community, which is what a broad speech protection makes possible",
     "It argues that speech should be restricted to preserve social order",
     "It argues that only written communication deserves protection",
     "It argues that protest should be confined to those directly affected",
     "It argues that the First Amendment applies only to Congress"], ans=0,
   why="The CED attaches the Letter to 3.3.A, and the passage's claim is that injustice concerns everyone -- a justification for expression addressed beyond one's own community, which broad speech protection allows."),

 dict(q="Read the following excerpt.\n\n“Freedom is never voluntarily given by the oppressor; it must be demanded by the oppressed.”\n—Martin Luther King, Jr., “Letter from a Birmingham Jail,” 1963\n\nWhat does this claim imply about the importance of speech and assembly protections?",
   choices=[
     "If change must be demanded rather than granted, then the rights to speak and assemble are the means by which it is demanded",
     "It implies that speech protections are unnecessary because change comes from courts",
     "It implies that only those in power may speak effectively",
     "It implies that demands should be made privately rather than publicly",
     "It implies that assembly should be limited to preserve order"], ans=0,
   why="The sentence makes demand the mechanism of change, and the First Amendment's speech, assembly and petition clauses are what make public demand possible. The Letter is a required document the CED attaches to this topic."),

 dict(q=_CLAIMS + " Which conclusion is best supported by the data?",
   table=_CLAIMS_TABLE,
   choices=[
     "The court upheld a large majority of political and symbolic expression claims and a small minority of defamation and danger claims",
     "The court upheld a majority of claims in all four categories",
     "The court upheld a minority of claims in all four categories",
     "Symbolic expression claims were the most numerous category",
     "Defamation claims succeeded more often than political speech claims"], ans=0,
   why="Political speech runs 119 of 142 and symbolic 51 of 68, both above four fifths; defamation is 26 of 94 and danger 9 of 37, both under a third. Political speech is the largest category."),

 dict(q=_CLAIMS + " Which claim from the course framework do these data most directly illustrate?",
   table=_CLAIMS_TABLE,
   choices=[
     "That the Court protects speech, including symbolic speech, while recognizing categories in which speech may be limited",
     "That the Court protects all speech without exception",
     "That the Court permits speech to be restricted in every category",
     "That defamation is protected by the First Amendment",
     "That symbolic speech receives no protection"], ans=0,
   why="EK 3.3.A.1 and EK 3.3.A.2 together describe protection plus limited categories, and a table with two high-success categories and two low ones is that pattern. Either extreme would require a table with uniform results."),

 dict(q=_CLAIMS + " A student concludes from these data that the court is hostile to defamation plaintiffs. Which limitation of the data most undercuts that conclusion?",
   table=_CLAIMS_TABLE,
   choices=[
     "The table counts outcomes for the SPEAKER, so a low figure in the defamation row means plaintiffs often won rather than that they fared badly",
     "The table omits defamation claims entirely, so no comparison is possible",
     "The table covers a single year, so no pattern can be observed",
     "The table reports percentages that do not sum to one hundred",
     "The table gives no information about how many claims were brought"], ans=0,
   why="The second column is claims upheld FOR THE SPEAKER, so the defamation row's 26 of 94 means the person alleging harm prevailed in most cases. Misreading which party a column counts is the commonest data error of all."),

 dict(q=_RULES + " Which conclusion is best supported by the table?",
   table=_RULES_TABLE,
   choices=[
     "Three of the four ordinances restrict circumstances without regard to the message, and one restricts the message itself",
     "All four ordinances restrict the content of the message",
     "None of the ordinances depends on the message",
     "The ordinance about the courthouse is the only one that does not depend on the message",
     "Every ordinance restricts the manner of expression"], ans=0,
   why="The last column reads No three times and Yes once. The courthouse rule is one of the three content-neutral ones, and the four ordinances restrict manner, place, time and content in various combinations."),

 dict(q=_RULES + " Which ordinance would be the hardest to defend as a time, place, and manner regulation under EK 3.3.A.2.i?",
   table=_RULES_TABLE,
   choices=[
     "The ordinance barring demonstrations that criticize the city council, since it turns on the message",
     "The ordinance limiting amplified sound after ten at night, since it restricts noise",
     "The ordinance barring demonstrations inside the courthouse, since it restricts location",
     "The ordinance requiring permits for large gatherings, since it restricts manner",
     "None of them, since all four regulate circumstances"], ans=0,
   why="EK 3.3.A.2.i's category is about circumstances -- time of day, place, noise level -- and the fourth ordinance is the only one whose application depends on what is being said."),

 dict(q=_RULES + " Which of the CED's three examples of time, place, and manner restrictions appears in the table?",
   table=_RULES_TABLE,
   choices=[
     "All three: a limit on the time of day, a limit on where an event may be held, and a limit on noise levels",
     "Only the limit on noise levels",
     "Only the limit on where an event may be held",
     "Only the limit on the time of day",
     "None of them"], ans=0,
   why="EK 3.3.A.2.i names time of day, location and noise level, and the first two rows supply all three between them: amplified sound above a set level after ten at night covers time and noise, and the courthouse rule covers place."),

 dict(q="LO 3.3.A asks about THE EXTENT to which the Court's interpretation reflects a commitment to free speech. Which answer is best supported by the course framework as a whole?",
   choices=[
     "The commitment is substantial but not unlimited, since the framework states both broad protection and four categories of permissible limitation",
     "The commitment is absolute, since the framework states that speech is protected",
     "There is no commitment, since the framework lists four categories of limitation",
     "The commitment applies only to symbolic speech",
     "The extent cannot be assessed, since the framework takes no position"], ans=0,
   why="EK 3.3.A.1 and EK 3.3.A.2 are both in the framework, and LO 3.3.A's phrase 'the extent to which' asks a student to weigh them rather than to choose one. Either extreme drops half of what the framework says."),

 dict(q="A commentator argues that the four categories in EK 3.3.A.2 show the First Amendment's protection is weak. Which response is best supported by the framework?",
   choices=[
     "Each category is narrow and defined, and the framework's own account of the danger standard notes that later interpretation has refined it further",
     "The four categories do not exist in the framework",
     "The four categories apply to all speech equally",
     "The framework says the First Amendment protects no speech at all",
     "The four categories were added to the Constitution by amendment"], ans=0,
   why="EK 3.3.A.2's categories are bounded rather than general, and EK 3.3.A.2.iv's refinement clause records that one of them has been narrowed over time -- which is why the extent of the commitment is a matter of degree."),
]
