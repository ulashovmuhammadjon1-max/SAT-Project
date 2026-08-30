# AP HUMAN GEOGRAPHY 2.8 Women and Demographic Change -- 30 questions
# CED Course Framework V.1, Unit 2. Enduring understanding SPS-2; learning
# objective SPS-2.B, "Explain how the changing role of females has demographic
# consequences in different parts of the world."
#
# Essential knowledge, in full -- two statements, and the second names a model:
#   SPS-2.B.1  Changing social values and access to education, employment,
#              health care, and contraception have reduced fertility rates in
#              most parts of the world.
#   SPS-2.B.2  Changing social, economic, and political roles for females have
#              influenced patterns of fertility, mortality, and migration, as
#              illustrated by Ravenstein's laws of migration.
#
# SPS-2.B.1 is a closed list of FOUR channels -- social values, education,
# employment, health care, contraception -- and it is careful about its claim:
# "in MOST parts of the world", not everywhere. Items 1-9, 13, 16, 20 and 26 are
# keyed to that list and cite it.
#
# SPS-2.B.2 does two things. It extends the consequence beyond fertility to
# MORTALITY and MIGRATION as well, which is the half students skip; and it names
# Ravenstein as the illustration. The laws, as the course states them:
#   1  Most migrants travel only a short distance.
#   2  Migration proceeds step by step, in stages up a settlement hierarchy.
#   3  Migrants going long distances head for the great centres of commerce and
#      industry.
#   4  Each migration stream produces a counterstream.
#   5  Rural residents are more migratory than urban residents.
#   6  Within a country females are more migratory than males; over long
#      international distances males predominate.
#   7  Most migrants are young adults.
#   8  Large towns grow more by migration than by natural increase.
#   9  Migration increases as commerce and transport develop.
#  10  Economic motives predominate among the causes.
#
# A point of honesty the module makes explicit rather than hiding, because a
# nineteenth-century generalization presented as a present-day fact is exactly
# the kind of wrong key this bank must not ship: Ravenstein's sixth law
# described Victorian Britain, and women are now close to half of international
# migrants worldwide. Items 15 and 24 test that the laws are a model to be
# checked against data rather than a description of the present.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g2_8.py. FIVE choices (A-E).
TOPIC = ("2.8", "Women and Demographic Change", 2)

QUESTIONS = [
 dict(q="Which set of changes does the framework identify as having reduced fertility rates in most parts of the world?",
   choices=[
     "Changing social values together with access to education, employment, health care, and contraception",
     "Rising food prices and falling agricultural yields",
     "Expanding land area and falling population density",
     "Improved mapping and better census records",
     "Rising international migration and falling internal migration"],
   ans=0,
   why="EK SPS-2.B.1 lists exactly these channels, and the list is closed. Each of them acts on the same decision from a different direction, which is why fertility has fallen across societies with very different politics and religions."),

 dict(q="A country's female secondary school enrolment rises from 30 to 85 percent over a generation, and its fertility falls from 5.6 to 2.4. What is the most direct mechanism linking the two?",
   choices=[
     "Schooling delays marriage and first birth and raises the earnings a woman gives up by leaving work, so families choose fewer children",
     "Schooling directly reduces a woman's biological capacity to bear children",
     "Schooling causes emigration, which lowers the birth count",
     "Schooling raises the death rate, which lowers the population",
     "There is no mechanism; the two changes are unrelated"],
   ans=0,
   why="EK SPS-2.B.1 names access to education among the channels reducing fertility. The mechanism runs through timing and opportunity cost -- years in school are years not spent childbearing, and qualifications make the forgone earnings of a large family much larger."),

 dict(q="Why does access to contraception appear on the framework's list separately from changing social values?",
   choices=[
     "Wanting a smaller family and being able to achieve one are different things, and a gap between desired and actual fertility persists where supply is limited",
     "Contraception is the only factor that affects fertility",
     "Social values do not change in any society",
     "Contraception raises the desired number of children",
     "The two are listed separately only for historical reasons"],
   ans=0,
   why="EK SPS-2.B.1 lists social values and access to contraception as separate items, and the separation is substantive. Where the means are unavailable, unintended births keep measured fertility above what couples say they want, which is a supply failure rather than a preference."),

 dict(q="How does improved health care reduce fertility, according to the framework's account?",
   choices=[
     "When more children survive, families no longer need to bear extra children to reach the family size they want",
     "Health care makes childbearing physically impossible",
     "Health care raises the death rate among children",
     "Health care has no relationship to fertility",
     "Health care increases the number of children each family wants"],
   ans=0,
   why="EK SPS-2.B.1 names access to health care among the channels reducing fertility, and the mechanism runs through child survival. Where a large share of children died young, high fertility was the insurance; removing the risk removes the reason for the insurance."),

 dict(q="A rise in women's paid employment outside the home is associated with lower fertility. Which explanation fits best?",
   choices=[
     "Time out of the labour force to bear and raise a child costs earnings and advancement, so each additional child has a real price",
     "Employed women are biologically less fertile",
     "Employment causes women to emigrate",
     "Employment raises the number of children families want",
     "The association is coincidental and has no mechanism"],
   ans=0,
   why="EK SPS-2.B.1 lists employment among the channels through which fertility has fallen. The cost of a child is not only what it consumes but what its mother forgoes, and that second cost rises as her earning opportunities do."),

 dict(q="The framework says these changes have reduced fertility 'in most parts of the world.' Why is that qualification important?",
   choices=[
     "Fertility remains high in some regions where the same access has not been achieved, so the claim is about a widespread pattern rather than a universal law",
     "It means the changes have had no effect anywhere",
     "It means fertility has risen in most places",
     "It means the claim applies only to one continent",
     "It is a stylistic choice with no substantive meaning"],
   ans=0,
   why="EK SPS-2.B.1's own wording is 'in most parts of the world', and taking that seriously is the difference between a geographic generalization and an overstatement. Where schooling, work and contraception remain out of reach, the fall has not occurred."),

 dict(q="Which statement best captures what SPS-2.B.2 adds to SPS-2.B.1?",
   choices=[
     "That changing roles for women affect mortality and migration as well as fertility",
     "That fertility is the only demographic variable affected",
     "That women's roles have not changed anywhere",
     "That migration is unrelated to gender",
     "That mortality is determined only by health care spending"],
   ans=0,
   why="EK SPS-2.B.1 covers fertility alone, while EK SPS-2.B.2 extends the consequence to fertility, mortality AND migration. The second and third of those are the half of the topic students most often leave out."),

 dict(q="How do changing roles for women affect MORTALITY, as the framework's second statement implies?",
   choices=[
     "Better-educated women use health services more effectively for themselves and their children, so maternal and infant mortality fall",
     "Women's education raises adult mortality",
     "Changing roles affect only fertility, never mortality",
     "Mortality changes only through migration",
     "Women's employment eliminates all causes of death"],
   ans=0,
   why="EK SPS-2.B.2 names mortality among the patterns influenced by changing social, economic and political roles for females. Literacy, income and autonomy each raise the chance that a health problem is recognized, treated and paid for in time."),

 dict(q="Which of the following is Ravenstein's law that the framework's mention of female roles most directly illustrates?",
   choices=[
     "That within a country women are more migratory than men, while men predominate over long international distances",
     "That most migrants travel long distances",
     "That migration streams produce no counterstreams",
     "That most migrants are elderly",
     "That urban residents are more migratory than rural residents"],
   ans=0,
   why="EK SPS-2.B.2 names Ravenstein's laws as the illustration of gendered migration patterns, and only one of the laws is about sex. The other options invert real laws, which is why each of them is wrong rather than merely irrelevant."),

 dict(q="According to Ravenstein, most migrants",
   choices=[
     "Travel only a short distance, so the volume of movement falls off sharply with distance",
     "Travel across international borders",
     "Move only once, and never in stages",
     "Are past retirement age",
     "Move for cultural rather than economic reasons"],
   ans=0,
   why="The first of Ravenstein's laws is that most migration is short-distance, which is distance decay stated for people. The other four options each contradict one of the remaining laws about stages, age and economic motive."),

 dict(q="Ravenstein's observation that migration 'proceeds step by step' means that",
   choices=[
     "Migrants often move up the settlement hierarchy in stages, from village to town to city, rather than in one jump",
     "Migrants move once a year",
     "Migrants always return to their place of origin",
     "Migrants move only within one country",
     "Migrants travel in organized groups"],
   ans=0,
   why="Step migration describes a sequence of shorter moves reaching the same destination a single long move would, and it is the law that connects the short-distance rule to the growth of large cities. Each step is short even though the total displacement is large."),

 dict(q="Ravenstein's law that each migration stream produces a counterstream is best illustrated by",
   choices=[
     "A flow of young workers from a rural region to the capital accompanied by a smaller flow of returnees and retirees back to the region",
     "A flow of workers to the capital with no movement in the other direction",
     "Two regions exchanging exactly equal numbers of migrants",
     "A population that does not move at all",
     "Migration that occurs only between countries"],
   ans=0,
   why="A counterstream is a smaller flow in the opposite direction produced by the same connection that created the main stream: information, family ties and return after work or retirement. Equal exchange would leave no net migration at all, which is a different situation."),

 dict(q="A country reports that fertility fell fastest in its cities and much more slowly in its remote rural districts. Which explanation best matches the framework?",
   choices=[
     "Schooling, employment, clinics, and contraception are all more accessible in cities, so the channels the framework names operate more strongly there",
     "Rural women want more children for biological reasons",
     "Cities have a lower carrying capacity",
     "Fertility cannot be measured in rural areas",
     "Rural districts have higher mortality, which raises fertility"],
   ans=0,
   why="EK SPS-2.B.1 makes access to education, employment, health care and contraception the mechanisms, and access is precisely what varies between a capital and a remote district. The uneven geography of the fall follows from the uneven geography of the channels."),

 dict(q="Which of these would most directly RAISE a country's fertility, reversing one of the framework's channels?",
   choices=[
     "Withdrawing girls from secondary school and restricting women's paid employment",
     "Expanding rural clinics",
     "Improving roads to remote villages",
     "Extending electricity to rural households",
     "Publishing more accurate population statistics"],
   ans=0,
   why="EK SPS-2.B.1's channels work by raising the cost of a large family and the alternatives available to women, so closing them removes both. The other options improve access generally and would if anything strengthen the fall the framework describes."),

 dict(q="Ravenstein wrote in the 1880s, and women are now close to half of all international migrants. What does this show about the laws?",
   choices=[
     "They are a model generalized from one era's data and must be checked against current evidence rather than assumed",
     "They have been shown to be wrong in every particular",
     "They apply only to the nineteenth century and are of no use now",
     "The current data must be inaccurate",
     "Women have always been half of international migrants"],
   ans=0,
   why="EK SPS-2.B.2 offers Ravenstein as an ILLUSTRATION of gendered migration patterns rather than as a law of nature. Most of the laws still describe migration well, and the one about sex is the clearest case where the world has moved since they were written."),

 dict(q="A programme that trains and employs women as community health workers is followed by falls in both fertility and infant mortality. Which framework statement covers both outcomes?",
   choices=[
     "That changing social, economic, and political roles for females influence fertility, mortality, and migration",
     "That fertility is unaffected by employment",
     "That mortality is unaffected by women's roles",
     "That only contraception affects fertility",
     "That migration is the only variable women's roles affect"],
   ans=0,
   why="EK SPS-2.B.2 names fertility and mortality together as patterns influenced by women's changing roles, which is exactly the pair of outcomes described. A single intervention moving both is the framework's claim in its clearest form."),

 dict(q="Which of Ravenstein's laws best explains why a large city can grow rapidly even when its own residents have few children?",
   choices=[
     "That large towns grow more by migration than by natural increase",
     "That most migrants travel short distances",
     "That most migrants are young adults",
     "That each stream produces a counterstream",
     "That economic motives predominate"],
   ans=0,
   why="One of the laws states the point directly: the growth of a large town is fed by arrivals rather than by births to the people already there. The others are true and describe who moves and why, but only this one is about the city's own growth accounting."),

 dict(q="Why does Ravenstein's law that most migrants are young adults matter for the places they leave?",
   choices=[
     "Losing people of childbearing and working age removes both current labour and future births from the origin",
     "It means the origin's population becomes younger",
     "It means the origin gains workers",
     "It has no consequence for the origin",
     "It means the destination's population ages"],
   ans=0,
   why="A selective loss changes composition as well as size, because the migrants take their future children with them. Both the labour force and the birth count at the origin fall, which is why sustained out-migration ages a region."),

 dict(q="A geographer argues that women's changing political roles matter demographically. Which example best supports that argument?",
   choices=[
     "Women's enfranchisement and representation being followed by legislation on maternal health, childcare, and family planning",
     "A rise in the number of women in a country's population",
     "A fall in a country's total land area",
     "A rise in the country's arithmetic population density",
     "A change in the country's map projection"],
   ans=0,
   why="EK SPS-2.B.2 names political roles alongside social and economic ones. Political voice changes which problems reach the statute book, and the policies that follow act on exactly the fertility and mortality channels EK SPS-2.B.1 lists."),

 dict(q="A country's fertility has fallen to 1.6 and its government is concerned. Which framework-consistent statement about the cause is most accurate?",
   choices=[
     "The same expansions of schooling, work, and health care that improved women's lives also lowered fertility, so the fall is a consequence of gains rather than of a failure",
     "The fall must have been caused by government policy alone",
     "The fall shows that access to education has decreased",
     "The fall is unrelated to women's roles",
     "The fall must be an error in the statistics"],
   ans=0,
   why="EK SPS-2.B.1 identifies the channels, and every one of them is something a country pursues for its own sake. Recognising that low fertility is a by-product of widely desired gains is what makes the policy question hard rather than obvious."),

 dict(q="Which pattern would be evidence AGAINST the framework's claim about the channels that reduce fertility?",
   choices=[
     "A country in which female schooling, employment, contraception, and health care all expanded sharply while fertility stayed at 6.0 for thirty years",
     "A country in which fertility fell as schooling expanded",
     "A country in which fertility is lower in cities than in the countryside",
     "A country in which contraception use rose and fertility fell",
     "A country in which fertility fell faster among educated women"],
   ans=0,
   why="A claim is tested by the case in which its stated causes are present and its predicted effect is absent. The other four options are all instances of the pattern EK SPS-2.B.1 describes rather than challenges to it."),

 dict(q="Which of Ravenstein's laws is closest to the concept of distance decay?",
   choices=[
     "That the majority of migrants move only a short distance, so numbers fall as distance rises",
     "That most migrants are adults",
     "That large towns grow by migration",
     "That economic motives predominate",
     "That migration increases as transport improves"],
   ans=0,
   why="Distance decay is the decline of interaction with separation, and the short-distance law is exactly that statement applied to migration. The others describe who migrates, why, and what the destination gains, none of which is a distance relationship."),

 dict(q="A rural district's out-migration is dominated by young women moving to the nearest city, while the country's emigration to other continents is dominated by men. How should this be described?",
   choices=[
     "It matches Ravenstein's sixth law, which distinguishes internal migration, where women predominate, from long-distance international migration, where men do",
     "It contradicts Ravenstein entirely",
     "It matches Ravenstein's law that most migrants travel long distances",
     "It shows that gender has no bearing on migration",
     "It matches Ravenstein's law about counterstreams"],
   ans=0,
   why="EK SPS-2.B.2 cites Ravenstein as the illustration of gendered migration, and the sixth law is the one that makes the distinction by distance and by border. The pattern described has both halves of that law in the same country at the same time."),

 dict(q="What is the most defensible way for a student to use Ravenstein's laws in an argument today?",
   choices=[
     "As a set of tendencies to be tested against current data, noting where a country's pattern departs from them and asking why",
     "As fixed rules that every migration must obey",
     "As a description of one country in one century with no present relevance",
     "As a theory about fertility rather than migration",
     "As a set of government policies"],
   ans=0,
   why="EK SPS-2.B.2 calls the laws an illustration, which is a claim about usefulness rather than about universality. The productive use of a generalization is to notice the exceptions, since a departure from the expected pattern is where the geography of a particular case shows up."),

 dict(q="Which combination best explains why fertility decline is usually irreversible once the channels the framework names are in place?",
   choices=[
     "The changes in schooling, work, and expectations that produced it are themselves durable, and few societies reverse them deliberately",
     "Biological capacity to bear children is permanently lost",
     "Governments legally prohibit larger families",
     "Contraception cannot be withdrawn once introduced",
     "Fertility rates are never measured accurately after they fall"],
   ans=0,
   why="EK SPS-2.B.1's channels are social and economic conditions rather than events, and they persist once established. That durability is what makes pronatalist policy so much harder than the antinatalist policy of the previous topic."),

 dict(q="Female schooling and fertility are shown for four countries. Using the table, which statement is best supported?",
   table=dict(
     headers=["Country", "Female secondary enrolment (%)", "Total fertility rate"],
     rows=[
       ["Country A", "24", "5.8"],
       ["Country B", "51", "3.9"],
       ["Country C", "78", "2.3"],
       ["Country D", "94", "1.7"]]),
   choices=[
     "Fertility falls steadily as female enrolment rises, from 5.8 at 24 percent enrolment to 1.7 at 94 percent",
     "Fertility rises as female enrolment rises",
     "Fertility is unrelated to female enrolment in these four countries",
     "The country with the highest enrolment has the highest fertility",
     "Only the two countries with enrolment above 70 percent show any relationship"],
   ans=0,
   why="Enrolment rises 24, 51, 78, 94 while fertility falls 5.8, 3.9, 2.3, 1.7, with no reversal at any step. Four points cannot establish causation, but they do show the association the framework's account predicts."),

 dict(q="Contraceptive prevalence and fertility are shown for four countries. Using the table, which country's data is least consistent with the others?",
   table=dict(
     headers=["Country", "Contraceptive prevalence (%)", "Total fertility rate"],
     rows=[
       ["Country J", "14", "6.1"],
       ["Country K", "38", "4.2"],
       ["Country L", "62", "2.6"],
       ["Country M", "58", "4.4"]]),
   choices=[
     "Country M, whose prevalence is nearly as high as Country L's but whose fertility is higher than Country K's",
     "Country J, which has the lowest prevalence and the highest fertility",
     "Country K, whose figures fall between the others",
     "Country L, which has the highest prevalence and the lowest fertility",
     "None of them, since all four fit the same pattern"],
   ans=0,
   why="Three countries line up in order -- 14 with 6.1, 38 with 4.2, 62 with 2.6 -- while the fourth pairs the second-highest prevalence with the second-highest fertility. Prevalence is one of the framework's channels rather than the only one, so a country can be off the line."),

 dict(q="Internal and international migrants are broken down by sex. Using the table, which of Ravenstein's laws does the pattern support?",
   table=dict(
     headers=["Type of move", "Female migrants", "Male migrants"],
     rows=[
       ["Rural to nearest town, within country", "62,000", "41,000"],
       ["Between provinces, within country", "48,000", "44,000"],
       ["To another continent", "19,000", "57,000"]]),
   choices=[
     "The sixth law, since women outnumber men in both internal flows while men outnumber women three to one in the long-distance international flow",
     "The first law, since most migrants travel a long distance",
     "The fourth law, since each stream produces a counterstream",
     "The eighth law, since large towns grow by migration",
     "No law, since the numbers are similar in every row"],
   ans=0,
   why="Women lead 62,000 to 41,000 and 48,000 to 44,000 inside the country while men lead 57,000 to 19,000 on the intercontinental move, which is three to one. That contrast between internal and long-distance international movement is the law's exact content."),

 dict(q="A country's maternal mortality and female literacy are shown across four decades. Using the table, what does the trend suggest?",
   table=dict(
     headers=["Decade", "Female literacy (%)", "Maternal deaths per 100,000 births"],
     rows=[
       ["1980s", "31", "620"],
       ["1990s", "48", "410"],
       ["2000s", "67", "230"],
       ["2010s", "84", "110"]]),
   choices=[
     "Maternal mortality fell by more than 80 percent as literacy rose, which is the mortality half of the framework's claim about women's roles",
     "Maternal mortality fell by 510 percent",
     "Literacy and maternal mortality rose together",
     "Maternal mortality was unaffected by the change in literacy",
     "The framework's claim concerns fertility only, so the table is irrelevant"],
   ans=0,
   why="Maternal deaths fall from 620 to 110 per 100,000, which is a reduction of 82 percent, while literacy rises from 31 to 84 percent. EK SPS-2.B.2 names mortality alongside fertility, so this is the framework's claim rather than a departure from it."),

 dict(q="Fertility is shown for one country by the mother's level of education. Using the table, what does the pattern within a single country show?",
   table=dict(
     headers=["Mother's education", "Total fertility rate", "Share of women in this group (%)"],
     rows=[
       ["No formal schooling", "6.4", "22"],
       ["Primary only", "5.1", "31"],
       ["Secondary", "3.2", "34"],
       ["Tertiary", "2.0", "13"]]),
   choices=[
     "Fertility falls with each additional level of schooling within the same country, so the relationship does not depend on comparing different national contexts",
     "Fertility is the same at every level of schooling",
     "The largest group of women has the highest fertility",
     "The relationship disappears when only one country is examined",
     "Tertiary-educated women have the highest fertility in this country"],
   ans=0,
   why="Fertility runs 6.4, 5.1, 3.2 and 2.0 across the four levels, and the shares confirm the groups are all substantial rather than one being negligible. Holding country constant removes the objection that a cross-national association reflects differences between whole societies."),
]
