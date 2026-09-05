# AP WORLD HISTORY: MODERN 8.7 Global Resistance to Established Power Structures
# After 1900
# CED effective Fall 2026 (Course Framework V.1), Unit 8 Cold War and
# Decolonization, c. 1900 to the present. Thematic focus: Cultural Developments
# and Interactions (CDI). Reasoning process: Causation.
#
# Learning Objective: Unit 8 Learning Objective I -- explain various reactions to
# existing power structures in the period after 1900. Suggested skill 2.B,
# explain the point of view, purpose, historical situation, and/or audience of a
# source. That skill is the shape of this bank: a majority of the items below ask
# what a source was FOR, whom it addressed, or what situation produced it, which
# is what distinguishes 8.7 from 8.6's use of evidence against an argument.
#
# TITLE. WORLD_HISTORY_topics.json gives this topic as "Global Resistance to
# Established Power Structures After 1900", and that is what is used here. The
# CED page prints the title across a column break, so a shorter form can be
# reconstructed from the text dump by mistake; the JSON is the authority per the
# authoring brief and it matches the CED page read in full.
#
# HISTORICAL DEVELOPMENTS this topic prints, and the only sentences the keys
# below rest on:
#   KC-6.2.V    Although conflict dominated much of the 20th century, many
#               individuals and groups -- including states -- opposed this trend.
#               Some individuals and groups, however, intensified the conflicts.
#   KC-6.2.V.A  Groups and individuals challenged the many wars of the century,
#               and some, such as Mohandas Gandhi, Martin Luther King Jr., and
#               Nelson Mandela, promoted the practice of nonviolence as a way to
#               bring about political change.
#   KC-6.2.V.C  Militaries and militarized states often responded to the
#               proliferation of conflicts in ways that further intensified
#               conflict.
#   KC-6.2.V.D  Some movements used violence against civilians in an effort to
#               achieve political aims.
#
# ILLUSTRATIVE EXAMPLES the CED prints on this page, in two lists:
#   Responses that intensified conflict: Chile under Augusto Pinochet; Spain
#     under Francisco Franco; Uganda under Idi Amin; the buildup of the
#     military-industrial complex and weapons trading.
#   Movements that used violence: Shining Path; Al-Qaeda.
# Illustrative examples are optional course content, so exactly TWO items turn on
# them and both stems say the course prints them as such.
#
# NAMED PEOPLE, AND THE LINE THIS BANK DOES NOT CROSS. Gandhi, King and Mandela
# are named inside KC-6.2.V.A itself, so they are required content rather than
# optional examples and items may say what the framework says about them: that
# they promoted the practice of nonviolence as a way to bring about political
# change. NOTHING here puts words in their mouths. Every stimulus in this module
# is an unattributed, explicitly illustrative text; inventing a speech for a
# named twentieth-century figure would be read by a student as fact, and this
# topic is the one where that temptation is strongest.
#
# CONTESTED GROUND, AND WHAT IS DELIBERATELY NOT KEYED. This topic covers
# political violence and names particular regimes and particular movements. The
# framework's sentences are descriptive and so are the keys: that militarized
# states often responded in ways that further intensified conflict, and that some
# movements used violence against civilians in an effort to achieve political
# aims. No key here justifies, condemns, ranks or excuses any actor, assigns
# responsibility for any particular episode, or takes a side in any dispute that
# remains live. Where a question involves a source produced by a party to a
# conflict, it asks what the source's purpose and audience were, which is the
# skill, and not who was in the right.
#
# THE QUANTIFIERS ARE LOAD-BEARING. KC-6.2.V says MANY opposed the trend and
# SOME intensified it; KC-6.2.V.A says SOME of those who challenged the wars
# promoted nonviolence; KC-6.2.V.C says militarized states OFTEN responded in
# ways that intensified conflict; KC-6.2.V.D says SOME movements used violence.
# Not one of those is a universal, and a bank that flattened any of them would
# teach the opposite of the framework's own sentence. Items 4, 9, 14, 20 and 26
# hold them open.
#
# DEDUPE NOTE. KC-6.2.V.B, on the Non-Aligned Movement opposing and promoting
# alternatives to existing orders, sits on the Topic 8.2 page and belongs there;
# it appears here only as a distractor. Topic 9.7 covers responses to rising
# cultural and economic globalization, so anti-IMF activism and locally developed
# social media are its material and appear nowhere in this module. Topic 8.3
# covers proxy wars and military alliances as effects of the Cold War; this
# module stays on reactions to power structures.
#
# SOURCES. Section I is stimulus-based and this bank cannot display an image, so
# every stimulus is TEXT and none is attributed to a real person or document.
# TABLES are hypothetical, each states a whole and its parts, and every keyed
# conclusion is recomputed from the table alone. DATES are written "1950 to
# 1990", never with a hyphen; the CED states that events and processes are not
# constrained by its given dates, so no key here depends on a boundary year.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md; the real Section I prints four.
TOPIC = ("8.7", "Global Resistance to Established Power Structures After 1900", 8)

_T_REACTIONS = dict(
    headers=["Decade (hypothetical survey of organized responses to conflict)",
             "Organizations recorded",
             "Of those, opposing the trend toward conflict",
             "Of those, acting in ways that intensified conflict"],
    rows=[["1950s", "22", "15", "7"],
          ["1960s", "31", "20", "11"],
          ["1970s", "27", "18", "9"],
          ["1980s", "24", "16", "8"]])

_T_METHODS = dict(
    headers=["Region (hypothetical survey of movements challenging existing power structures)",
             "Movements recorded",
             "Of those, whose campaigns were conducted without violence",
             "Of those, whose campaigns used violence"],
    rows=[["Region one", "19", "13", "6"],
          ["Region two", "15", "9", "6"],
          ["Region three", "12", "8", "4"]])

_T_TRANSFERS = dict(
    headers=["Decade (hypothetical record of arms transfers)",
             "Transfers recorded",
             "Of those, to a state already engaged in an armed conflict",
             "Of those, to a state not so engaged"],
    rows=[["1960s", "40", "26", "14"],
          ["1970s", "62", "41", "21"],
          ["1980s", "85", "58", "27"]])

QUESTIONS = [

 dict(q="An unattributed circular distributed in several countries in 1955 invites readers to join an association whose stated object is to end the resort to war between states. According to this course, the circular belongs among",
   choices=[
     "the many individuals and groups that opposed the trend toward conflict in the twentieth century",
     "the individuals and groups that intensified the conflicts of the twentieth century",
     "the militaries and militarized states that responded to conflict in ways that intensified it",
     "the movements that used violence against civilians in an effort to achieve political aims",
     "the international organizations formed to supervise trade between member states"],
   ans=0,
   why="KC-6.2.V states that although conflict dominated much of the twentieth century, many individuals and groups, including states, opposed this trend. An association formed to end the resort to war is one of those groups, and the same sentence separates them from the individuals and groups that intensified the conflicts."),

 dict(q="This course names three figures as examples of people who promoted a particular method of bringing about political change. What was that method?",
   choices=[
     "The practice of nonviolence",
     "The formation of military alliances between states",
     "The redistribution of farmland to landless households",
     "The encouragement of free-market economic policies",
     "The founding of international organizations to arbitrate disputes"],
   ans=0,
   why="KC-6.2.V.A states that groups and individuals challenged the many wars of the century, and some, such as Mohandas Gandhi, Martin Luther King Jr., and Nelson Mandela, promoted the practice of nonviolence as a way to bring about political change. Nonviolence is the method the framework attaches to those three names, and the distractors belong to statements in other topics."),

 dict(q="A defence ministry's internal paper of 1968 argues that the rise in the number of armed conflicts abroad requires the state to enlarge its own forces and to supply weapons to friendly governments. According to this course, a response of this kind is described as one that",
   choices=[
     "further intensified conflict, which is how militarized states often responded to its proliferation",
     "reduced conflict, which is how militarized states usually responded to its proliferation",
     "had no recorded effect on the level of conflict in the period",
     "was confined to states that had recently become independent",
     "belonged to the movements that used violence against civilians for political aims"],
   ans=0,
   why="KC-6.2.V.C states that militaries and militarized states often responded to the proliferation of conflicts in ways that further intensified conflict. Enlarging forces and supplying weapons in answer to conflict elsewhere is that response as the framework describes it, so the key names the effect and the actor together because a distractor reverses the effect."),

 dict(q="A hypothetical survey places each organization it records under exactly one of two headings. Which conclusion does the table alone support?",
   table=_T_REACTIONS,
   choices=[
     "Organizations of both kinds appear in every decade, and in each decade those opposing the trend outnumber those intensifying it",
     "Only organizations opposing the trend toward conflict are recorded in the survey",
     "In every decade recorded, organizations intensifying conflict outnumber those opposing it",
     "No organization of either kind is recorded in the 1980s",
     "The decade recording the most organizations of either kind is the 1950s"],
   ans=0,
   why="KC-6.2.V states that many individuals and groups opposed the trend toward conflict while SOME, however, intensified the conflicts, which makes both kinds present and the opposing kind the larger. The survey is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="A leaflet issued in 1962 by a campaign against a government's policy states that its supporters will occupy a public building and will not resist arrest. Judging by what the leaflet announces, its authors are best described as",
   choices=[
     "challenging an existing power structure through the practice of nonviolence",
     "challenging an existing power structure through violence against civilians",
     "supporting the existing power structure against those who challenged it",
     "responding to the proliferation of conflicts as a militarized state would",
     "withdrawing from political activity in favour of private life"],
   ans=0,
   why="KC-6.2.V.A states that groups and individuals challenged the many wars of the century and that some promoted the practice of nonviolence as a way to bring about political change. Announcing in advance that supporters will not resist arrest is that practice stated as a method, and the leaflet is directed at a government rather than at civilians."),

 dict(q="Which statement best captures the two-sided claim this course makes about reactions to conflict in the twentieth century?",
   choices=[
     "Many individuals and groups opposed the trend toward conflict, while some others intensified the conflicts",
     "Many individuals and groups intensified the conflicts, while no one opposed the trend toward conflict",
     "Every individual and group of the century opposed the trend toward conflict",
     "Every individual and group of the century contributed to intensifying conflict",
     "Individuals and groups had no bearing on the level of conflict in the century"],
   ans=0,
   why="KC-6.2.V states that although conflict dominated much of the twentieth century, many individuals and groups, including states, opposed this trend, and that some individuals and groups, however, intensified the conflicts. Both halves are in one sentence, so the key carries both; a distractor keeps one and denies the other."),

 dict(q="An unattributed communique released in 1978 claims responsibility for an attack on a market and states that the attack was intended to force a government to change its policy. According to this course, this belongs among",
   choices=[
     "the movements that used violence against civilians in an effort to achieve political aims",
     "the movements that promoted the practice of nonviolence to bring about political change",
     "the militaries of states responding to the proliferation of conflicts",
     "the international organizations formed to maintain world peace",
     "the nationalist parties seeking varying degrees of autonomy from imperial rule"],
   ans=0,
   why="KC-6.2.V.D states that some movements used violence against civilians in an effort to achieve political aims. A communique claiming an attack on a market and stating a political object is that sentence exactly, and the framework distinguishes such movements from the states of KC-6.2.V.C and from the nonviolent campaigns of KC-6.2.V.A."),

 dict(q="A government press office issues a statement in 1974 describing its own security operations as measures that will restore order. A historian is asked what this source is most useful for. The best answer is that it is most useful as evidence of",
   choices=[
     "how the government wished its own actions to be understood by the public it addressed",
     "the number of people affected by the operations it describes",
     "the opinions held by the government's opponents at the time",
     "whether order was in fact restored in the months that followed",
     "the terms on which neighbouring states conducted their own security policy"],
   ans=0,
   why="Skill 2.B, the suggested skill for this topic, asks for the point of view, purpose and audience of a source, and a press office statement is produced to shape public understanding rather than to measure outcomes. KC-6.2.V.C establishes that militarized states often responded to conflict in ways that intensified it, which is the claim such a statement is placed to obscure and which the source therefore cannot settle."),

 dict(q="A student writes that in the twentieth century every group challenging the wars of the period adopted nonviolence. What is the best correction?",
   choices=[
     "The framework says some of those who challenged the wars promoted nonviolence, not all of them",
     "The framework says none of those who challenged the wars promoted nonviolence",
     "The framework says no group challenged the wars of the twentieth century",
     "The framework says nonviolence was promoted only by states rather than by groups or individuals",
     "The framework says nonviolence was promoted only in the years before 1900"],
   ans=0,
   why="KC-6.2.V.A states that groups and individuals challenged the many wars of the century, and SOME, such as Mohandas Gandhi, Martin Luther King Jr., and Nelson Mandela, promoted the practice of nonviolence. The word some makes nonviolence one method among those used, so the correction has to preserve that rather than replace one absolute with another."),

 dict(q="A hypothetical survey places each movement it records under exactly one of two headings. Which conclusion does the table alone support?",
   table=_T_METHODS,
   choices=[
     "In every region surveyed, movements of both kinds are recorded and neither kind accounts for all of them",
     "Every movement surveyed conducted its campaigns using violence",
     "No movement in region three is recorded as having campaigned without violence",
     "Region two recorded more movements than any other region listed",
     "The three regions recorded the same number of movements as one another"],
   ans=0,
   why="KC-6.2.V.A records that some who challenged existing power structures promoted the practice of nonviolence and KC-6.2.V.D that some movements used violence, so the framework describes both methods without making either universal. The survey is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="This course prints certain cases as illustrative examples of responses that intensified conflict. Which list is the one the course prints?",
   choices=[
     "Chile under Augusto Pinochet, Spain under Francisco Franco, Uganda under Idi Amin, and the buildup of the military-industrial complex and weapons trading",
     "Sukarno in Indonesia and Kwame Nkrumah in Ghana",
     "Israel, Cambodia, and Pakistan as states created by redrawn boundaries",
     "The Korean War, the Angolan Civil War, and the Sandinista and Contras conflict in Nicaragua",
     "The World Trade Organization, NAFTA, and ASEAN"],
   ans=0,
   why="The CED prints these four beside KC-6.2.V.C as illustrative examples of responses that intensified conflict. The other lists are illustrative examples the framework prints beside the Non-Aligned Movement, beside states created by redrawn boundaries, beside proxy wars and beside regional trade agreements, all in other topics."),

 dict(q="An open letter published in 1965 addresses the citizens of the writer's own country rather than its government, arguing that they should refuse to cooperate with a policy the writer opposes. The letter's choice of audience is best explained by the fact that",
   choices=[
     "a campaign of nonviolent action depends on the withdrawal of ordinary cooperation, which only the public can give or withhold",
     "governments in this period did not read letters published in newspapers",
     "the writer was legally forbidden to address any government in writing",
     "citizens rather than governments were responsible for setting the policy in question",
     "an open letter cannot be addressed to an institution under any circumstances"],
   ans=0,
   why="KC-6.2.V.A states that some who challenged the wars of the century promoted the practice of nonviolence as a way to bring about political change, and nonviolent action works by withholding cooperation rather than by force. Skill 2.B asks why a source addresses the audience it addresses, and the method the letter urges determines who has to receive it."),

 dict(q="A military journal published in 1971 argues that a neighbouring state's recent purchase of aircraft obliges its own state to purchase more. This course would treat the argument as an illustration of",
   choices=[
     "a militarized state responding to conflict in a way that further intensified it",
     "a state opposing the trend toward conflict in the twentieth century",
     "a movement using violence against civilians to achieve a political aim",
     "an individual promoting the practice of nonviolence to bring about change",
     "a newly independent government guiding economic life to promote development"],
   ans=0,
   why="KC-6.2.V.C states that militaries and militarized states often responded to the proliferation of conflicts in ways that further intensified conflict. An argument that one purchase of arms obliges another is that pattern stated as a principle, and the CED prints the buildup of the military-industrial complex and weapons trading as an illustrative example beside the same sentence."),

 dict(q="Which statement about movements that used violence is supported by this course?",
   choices=[
     "Some movements used violence against civilians in an effort to achieve political aims",
     "All movements challenging existing power structures used violence against civilians",
     "No movement of the twentieth century used violence against civilians",
     "Violence against civilians was used only by states and never by movements",
     "Movements using violence had no political aims of any kind"],
   ans=0,
   why="KC-6.2.V.D states that some movements used violence against civilians in an effort to achieve political aims. The word some makes this one pattern among the reactions the topic covers rather than a universal, and the same sentence attributes a political aim to the movements it describes."),

 dict(q="An unattributed pamphlet of 1959 written by an exiled opponent of a government is discovered in an archive. Which consideration most affects how a historian should use it?",
   choices=[
     "It was produced by someone outside the country and opposed to the government it describes, which shapes what it reports and omits",
     "It was written in 1959, and no document of that decade can serve as historical evidence",
     "It is a pamphlet, and pamphlets were not produced anywhere during this period",
     "It survives in an archive, and archived documents describe only the archive that holds them",
     "It concerns politics, and political documents bear on no course development"],
   ans=0,
   why="Skill 2.B, the suggested skill for this topic, asks for the point of view and historical situation of a source, and exile plus opposition is that situation stated. KC-6.2.V places both those who opposed existing power structures and those who upheld them inside the same period, so a source from one side is evidence about that side's account rather than a neutral record."),

 dict(q="Two sources describe the same demonstration. A police report calls it a disturbance requiring dispersal. A participant's letter calls it a peaceful assembly broken up without cause. What does this course's suggested skill direct a student to do with the pair?",
   choices=[
     "Ask what purpose each account served and whom each was written for before weighing either",
     "Accept the police report, because official documents are compiled for the record",
     "Accept the participant's letter, because eyewitnesses are always accurate",
     "Discard both, because two accounts that disagree cancel each other out",
     "Combine the two accounts by averaging their descriptions of the event"],
   ans=0,
   why="Skill 2.B asks for the point of view, purpose, historical situation and audience of a source, which is a question to be asked of both accounts rather than a rule for ranking them. KC-6.2.V describes a century in which power structures were both upheld and challenged, so accounts produced from the two positions are expected to differ in exactly this way."),

 dict(q="A trade journal of 1985 reports that firms supplying military equipment have expanded their sales for the eleventh consecutive year. Read in the framework of this course, the report is most relevant to",
   choices=[
     "the buildup of arms as a response to conflict that the framework treats as intensifying it further",
     "the promotion of nonviolence as a method of bringing about political change",
     "the movements that used violence against civilians to achieve political aims",
     "the migration of former colonial subjects to imperial metropoles",
     "the growth of a globalized consumer culture across national borders"],
   ans=0,
   why="KC-6.2.V.C states that militaries and militarized states often responded to the proliferation of conflicts in ways that further intensified conflict, and the CED prints the buildup of the military-industrial complex and weapons trading beside that sentence as an illustrative example. A sustained expansion in military sales is that buildup reported commercially."),

 dict(q="An unattributed manifesto of 1970 argues that its authors' aims cannot be achieved by petition or election and that only force will serve. According to this course, which category does the manifesto place its authors in?",
   choices=[
     "Movements that turned to violence in an effort to achieve political aims",
     "Groups that promoted the practice of nonviolence to bring about political change",
     "States that opposed the trend toward conflict in the twentieth century",
     "Militaries responding to a proliferation of conflicts elsewhere",
     "International organizations formed to maintain world peace"],
   ans=0,
   why="KC-6.2.V.D states that some movements used violence against civilians in an effort to achieve political aims, and a manifesto rejecting petition and election in favour of force announces that choice of method. KC-6.2.V.A describes the opposite choice within the same topic, which is why it is the near-miss distractor."),

 dict(q="A government's own broadcast of 1976 tells listeners abroad that its recent measures were requested by its own population. What is the strongest reason for caution in using this broadcast?",
   choices=[
     "It was produced by the government whose measures it describes and was aimed at an audience outside the country",
     "It was broadcast rather than printed, and broadcasts leave no historical trace",
     "It was made in 1976, and sources of that year are too recent to be historical",
     "It concerns a government, and governments are the only reliable sources about themselves",
     "It was addressed to listeners abroad, and foreign audiences cannot be studied"],
   ans=0,
   why="Skill 2.B asks for the purpose and audience of a source, and a state broadcast aimed abroad is made to secure a foreign reputation rather than to record domestic opinion. KC-6.2.V.C establishes that militarized states often responded to conflict in ways that intensified it, so a state's account of its own measures is precisely the claim that needs independent support."),

 dict(q="A hypothetical record places each arms transfer it lists under exactly one of two headings. Which conclusion does the table alone support?",
   table=_T_TRANSFERS,
   choices=[
     "The number of transfers rose in each successive decade, and in every decade most went to states already engaged in an armed conflict",
     "In every decade, most transfers went to states not already engaged in an armed conflict",
     "The number of recorded transfers fell after the 1960s",
     "No recorded transfer went to a state already engaged in an armed conflict",
     "The three decades recorded the same number of transfers as one another"],
   ans=0,
   why="KC-6.2.V.C states that militaries and militarized states often responded to the proliferation of conflicts in ways that further intensified conflict, and the CED prints weapons trading beside it as an illustrative example. A rising record of transfers going mostly to states already fighting is that pattern made countable, and the figures are hypothetical, with the key recomputed from the table alone in the verifier."),

 dict(q="A history textbook asserts that the twentieth century was a century of conflict and nothing else. How would this course's framework qualify that assertion?",
   choices=[
     "Conflict did dominate much of the century, but many individuals and groups opposed that trend",
     "Conflict did not dominate any part of the century, and the assertion is simply mistaken",
     "Conflict dominated the century entirely, and no individual or group opposed the trend",
     "Conflict was confined to the states that had recently become independent",
     "Conflict is not a subject the framework treats in this period at all"],
   ans=0,
   why="KC-6.2.V states that ALTHOUGH conflict dominated much of the twentieth century, many individuals and groups, including states, opposed this trend. The framework grants the textbook's premise and adds the opposition, so the qualification keeps both halves rather than denying either."),

 dict(q="This course prints two movements as illustrative examples of movements that used violence. Which pair is the one the course prints?",
   choices=[
     "Shining Path and Al-Qaeda",
     "The Indian National Congress and the Muslim League in British India",
     "Greenpeace and the Green Belt Movement in Kenya",
     "The Non-Aligned Movement and the World Fair Trade Organization",
     "The Biafra secessionist movement in Nigeria and the Quebecois separatist movement in Canada"],
   ans=0,
   why="The CED prints Shining Path and Al-Qaeda beside KC-6.2.V.D as illustrative examples of movements that used violence. The other pairs are illustrative examples the framework prints beside nationalist parties, beside environmental movements, beside the Non-Aligned Movement and economic movements, and beside regional and ethnic movements, all in other topics."),

 dict(q="A campaign publishes a code of conduct in 1963 instructing its members to accept injury without returning it. Its purpose in publishing the code, rather than merely circulating it internally, is best explained as an attempt to",
   choices=[
     "make the campaign's method visible to the wider public whose support it sought",
     "conceal the campaign's intentions from the authorities it opposed",
     "recruit members of the armed forces into the campaign's leadership",
     "obtain the agreement of a foreign government before acting",
     "satisfy a legal requirement that campaigns publish their internal rules"],
   ans=0,
   why="KC-6.2.V.A states that some who challenged the wars of the century promoted the practice of nonviolence as a way to bring about political change, and a method that works through public sympathy has to be publicly known to work at all. Skill 2.B asks what purpose a source served and whom it addressed, which is what publication rather than internal circulation reveals."),

 dict(q="According to this course, who is included among those who opposed the trend toward conflict in the twentieth century?",
   choices=[
     "Individuals, groups, and states alike",
     "Individuals only, since groups and states were uniformly committed to conflict",
     "States only, since individuals and groups had no means of acting",
     "Groups only, since individuals and states are not treated by the framework",
     "No one, since the framework records no opposition to the trend"],
   ans=0,
   why="KC-6.2.V states that many individuals and groups, INCLUDING STATES, opposed this trend. The parenthetical inclusion of states is part of the framework's sentence, so a key naming only individuals or only groups would drop what the sentence deliberately adds."),

 dict(q="An unattributed appeal circulated in 1980 asks readers in several countries to write to their own governments about a war being fought elsewhere. The appeal's assumption about how political change happens is best described as",
   choices=[
     "that pressure brought by ordinary people on their own governments can affect the conduct of conflict",
     "that conflicts can be ended only by the armed forces engaged in them",
     "that political change is produced by international organizations without public involvement",
     "that violence against civilians is the only effective means of changing a policy",
     "that governments are unaffected by anything their populations do or say"],
   ans=0,
   why="KC-6.2.V.A states that groups and individuals challenged the many wars of the century and that some promoted the practice of nonviolence as a way to bring about political change, which rests on the belief that public pressure can move a government. Skill 2.B asks what point of view a source expresses, and an appeal to write to one's own government expresses that one."),

 dict(q="Which pair of reactions to existing power structures does this course place side by side in the same period?",
   choices=[
     "Campaigns that challenged wars and promoted nonviolence, and movements that used violence against civilians for political aims",
     "Campaigns that promoted nonviolence, and campaigns that promoted free-market economic liberalization",
     "Movements that used violence against civilians, and international organizations that supervised trade",
     "Militaries responding to conflict, and the migration of former colonial subjects to metropoles",
     "Nationalist parties seeking autonomy, and consumer culture crossing national borders"],
   ans=0,
   why="KC-6.2.V.A describes those who challenged the many wars of the century and promoted the practice of nonviolence, and KC-6.2.V.D describes movements that used violence against civilians in an effort to achieve political aims. Unit 8 Learning Objective I asks for the VARIOUS reactions to existing power structures, and these two are the contrasting pair the topic sets out."),

 dict(q="A retired officer's memoir published in 1995 explains that measures taken in the 1970s were unavoidable given the threat then facing the state. What limits this source as evidence about the effects of those measures?",
   choices=[
     "It is written by a participant, long afterward, to explain and justify his own part in what happened",
     "It was published in 1995, and no memoir published after an event can be used",
     "It concerns the 1970s, a decade that falls outside the period this course covers",
     "It was written by an officer, and military witnesses are the only sources on military matters",
     "It is a memoir, and memoirs never contain any information about the past"],
   ans=0,
   why="Skill 2.B asks how a source's point of view, purpose and situation bear on its use, and a participant writing retrospectively to justify his own conduct has a purpose that shapes what the account can establish. KC-6.2.V.C states that militarized states often responded to the proliferation of conflicts in ways that further intensified conflict, which is exactly the effect such a memoir is placed to deny."),

 dict(q="A researcher wants to explain why the level of conflict in a region rose over a decade rather than fell. According to this course, which line of inquiry is most directly relevant?",
   choices=[
     "How the militaries and militarized states of the region responded to the conflicts already under way",
     "How many international conferences were held in the region during the decade",
     "How many books about the region were published elsewhere in the same years",
     "How the region's climate changed over the same period",
     "How many people emigrated from the region to a former imperial metropole"],
   ans=0,
   why="KC-6.2.V.C states that militaries and militarized states often responded to the proliferation of conflicts in ways that further intensified conflict, which makes their responses the framework's own explanation for conflict rising rather than falling. The reasoning process printed beside this topic is causation, and the other lines of inquiry bear on developments the framework treats elsewhere."),

 dict(q="Considered across this topic, what makes the reactions to existing power structures after 1900 various rather than uniform?",
   choices=[
     "They ranged from opposing conflict and practising nonviolence to intensifying conflict and using violence against civilians",
     "They consisted entirely of nonviolent campaigns pursuing identical aims",
     "They consisted entirely of armed responses by states to threats from abroad",
     "They were confined to a single region and to a single decade of the century",
     "They were organized from one centre and followed one common programme"],
   ans=0,
   why="KC-6.2.V sets opposition to the trend toward conflict beside its intensification, KC-6.2.V.A adds the promotion of nonviolence, KC-6.2.V.C the responses of militarized states and KC-6.2.V.D the movements that used violence against civilians. Unit 8 Learning Objective I asks for the various reactions, and the range between those poles is what makes them various."),

 dict(q="Taking the topic as a whole, which single sentence best states what this course says about reactions to power structures after 1900?",
   choices=[
     "Conflict dominated much of the century and many individuals, groups and states opposed that trend, some of them through nonviolence, while militarized states often answered conflict in ways that deepened it and some movements turned violence on civilians for political ends",
     "Conflict dominated the century and no one, whether individual, group or state, sought to oppose it in any way",
     "The century was free of conflict, so reactions to power structures took only cultural and artistic forms",
     "Every reaction to an existing power structure in the century took the form of nonviolent protest",
     "Reactions to power structures were confined to the militaries of states and involved no movements or individuals"],
   ans=0,
   why="KC-6.2.V supplies the dominance of conflict and the opposition to it including states, KC-6.2.V.A the promotion of nonviolence by some who challenged the wars, KC-6.2.V.C the militarized responses that further intensified conflict, and KC-6.2.V.D the movements that used violence against civilians for political aims. The key is the conjunction of those four with every quantifier intact, and each distractor contradicts at least one."),
]
