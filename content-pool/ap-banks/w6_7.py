# AP WORLD HISTORY: MODERN 6.7 Effects of Migration
# CED effective Fall 2026, Unit 6 Consequences of Industrialization, c. 1750 to
# c. 1900. Thematic focus SIO, Social Interactions and Organization: "The process by
# which societies group their members and the norms that govern the interactions
# between these groups and between individuals influence political, economic, and
# cultural institutions and organization."
#
# Unit 6 Learning Objective H: "Explain how and why new patterns of migration
# affected society from 1750 to 1900."
# Reasoning process: Causation. Suggested skill 5.B, explain how a historical
# development or process relates to another historical development or process.
#
# The historical developments this topic prints, in the framework's own words:
#   KC-5.4.III.A  Migrants tended to be male, leaving women to take on new roles in
#                 the home society that had been formerly occupied by men.
#   KC-5.4.III.B  Migrants often created ethnic enclaves in different parts of the
#                 world that helped transplant their culture into new environments.
#   KC-5.4.III.C  Receiving societies did not always embrace immigrants, as seen in
#                 the various degrees of ethnic and racial prejudice and the ways
#                 states attempted to regulate the increased flow of people across
#                 their borders.
#
# Illustrative examples the CED prints for this topic, under its own two headings.
# These are the only named groups and measures in this module:
#   Migrant ethnic enclaves: Chinese in Southeast Asia, the Caribbean, South America,
#     and North America; Indians in East and Southern Africa, the Caribbean, and
#     Southeast Asia; Irish in North America; Italians in North and South America.
#   Regulation of immigrants: Chinese Exclusion Act; White Australia policy.
#
# WHAT THIS BANK DOES NOT DO. The CED NAMES the Chinese Exclusion Act and the White
# Australia policy and says not one word about what either provided, when it passed,
# who enacted it or how long it lasted. Item 12 therefore asks only which pair the
# framework names, and item 13 only which of the unit's statements the CED prints
# the Chinese Exclusion Act beside -- the two things the CED settles -- and no item
# states a provision of either. The same restraint governs the enclave list: the
# framework gives regions, so items ask for regions and never for a date, a number or
# an occupation.
#
# TWO CAREFUL POINTS.
#   1. KC-5.4.III.A is a SWAP waiting to happen: it is women in the HOME society who
#      take on roles formerly occupied by men, not men in the receiving society
#      taking on women's roles, and not women in the receiving society. Wherever the
#      reversal is offered the anchor in verify_w6_7.py carries both clauses.
#   2. KC-5.4.III.C is a qualified claim -- receiving societies did NOT ALWAYS
#      embrace immigrants -- and reading it as "never embraced" is as wrong as
#      reading it as "always embraced". Items 5 and 6 turn on the qualification.
#
# Every source is UNATTRIBUTED and labelled illustrative; tables are labelled
# hypothetical and every keyed conclusion is recomputable from the table alone.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md. Dates are written "1750 to 1900".
TOPIC = ("6.7", "Effects of Migration", 6)

_T_ARRIVALS = dict(
    headers=["Arrival record (hypothetical)",
             "Men among every hundred arrivals",
             "Women among every hundred arrivals"],
    rows=[["Record 1", "78", "22"],
          ["Record 2", "71", "29"],
          ["Record 3", "84", "16"],
          ["Record 4", "66", "34"]])

_T_TASKS = dict(
    headers=["Task in one hypothetical home district",
             "Households in which a woman performed it before the departures, out of one hundred",
             "Households in which a woman performed it after the departures, out of one hundred"],
    rows=[["Managing the family holding", "12", "57"],
          ["Selling produce at market", "19", "61"],
          ["Hiring seasonal labour", "7", "44"],
          ["Weaving cloth for household use", "88", "86"]])

_T_QUARTER = dict(
    headers=["Institution recorded in one hypothetical migrant quarter",
             "Number recorded in the quarter"],
    rows=[["Places of worship of the migrants' own tradition", "6"],
          ["Schools teaching the migrants' language", "4"],
          ["Mutual aid societies formed by the migrants", "9"],
          ["Newspapers printed in the migrants' language", "3"]])

_T_ADMISSION = dict(
    headers=["Category of applicant at one hypothetical receiving state's border",
             "Admitted for every hundred who applied"],
    rows=[["Applicants from the neighbouring country", "94"],
          ["Applicants holding capital above a stated sum", "89"],
          ["Applicants from a country whose nationals the state had restricted", "11"],
          ["Labourers from that restricted country", "4"]])

QUESTIONS = [
 dict(q="What does the course framework say about the sex of migrants in this period?",
   choices=[
     "Migrants tended to be male",
     "Migrants tended to be female",
     "Migrants were divided evenly between men and women in every stream",
     "The framework makes no statement about the sex of migrants",
     "Only married couples travelling together are counted as migrants"], ans=0,
   why="KC-5.4.III.A opens by stating that migrants tended to be male. The framework does say something about the sex of migrants, so the option denying it is false, and it describes a tendency rather than an even division or a restriction to couples."),
 dict(q="The framework draws a consequence from the sex composition of migration. What is it?",
   choices=[
     "Women in the home society took on new roles that had formerly been occupied by men",
     "Men in the home society took on new roles that had formerly been occupied by women",
     "Women in the receiving society took on new roles that had formerly been occupied by migrants",
     "Roles in the home society passed from women to the state",
     "No role in the home society changed hands as a result of migration"], ans=0,
   why="KC-5.4.III.A states that migrants tending to be male left women to take on new roles in the HOME society that had been formerly occupied by men. Which sex takes up which roles, and in which society, are the whole content of that clause, so the reversed reading and the relocation of the change to the receiving society are both offered as distractors."),
 dict(q="The framework says migrants often created ethnic enclaves. What does it say those enclaves helped do?",
   choices=[
     "They helped transplant the migrants' culture into new environments",
     "They helped the receiving state regulate the flow of people across its borders",
     "They helped migrants abandon the culture of the society they had left",
     "They helped end the practice of coerced labour migration",
     "They helped receiving societies avoid contact with the migrants entirely"], ans=0,
   why="KC-5.4.III.B states that migrants often created ethnic enclaves in different parts of the world that helped transplant their culture into new environments. Border regulation is the subject of KC-5.4.III.C, and abandoning a culture is the opposite of transplanting it."),
 dict(q="Where does the framework say those ethnic enclaves were created?",
   choices=[
     "In different parts of the world",
     "Only in the country each migrant group had left",
     "Only in societies that had industrialized before 1750",
     "Only in territories governed by the migrants' own state",
     "In no place the framework is willing to identify"], ans=0,
   why="KC-5.4.III.B states that migrants often created ethnic enclaves in different parts of the world, and the CED's own illustrative list runs across Southeast Asia, the Caribbean, South America, North America and East and Southern Africa. That breadth is what makes each of the restricting options false."),
 dict(q="How does the framework describe the way receiving societies treated immigrants?",
   choices=[
     "Receiving societies did not always embrace immigrants",
     "Receiving societies always embraced immigrants",
     "Receiving societies never admitted immigrants at all",
     "Receiving societies were indifferent to the arrival of immigrants",
     "The framework makes no statement about receiving societies"], ans=0,
   why="KC-5.4.III.C states that receiving societies did not always embrace immigrants. The qualification is the framework's own: a claim that they always did and a claim that they never admitted anyone are both stronger than the sentence, and indifference is not what a statement about prejudice and regulation describes."),
 dict(q="KC-5.4.III.C says that the treatment of immigrants could be seen in two things. What are they?",
   choices=[
     "Various degrees of ethnic and racial prejudice, and the ways states attempted to regulate the flow of people across their borders",
     "Various degrees of religious conversion, and the ways states encouraged further immigration",
     "The wages paid to immigrants, and the routes by which they had travelled",
     "The size of each enclave, and the language spoken within it",
     "The number of migrants who returned home, and the reasons they gave"], ans=0,
   why="KC-5.4.III.C names exactly those two: the various degrees of ethnic and racial prejudice, and the ways states attempted to regulate the increased flow of people across their borders. Wages, routes, enclave size and rates of return are not what that sentence points to, and encouraging immigration is the reverse of regulating it."),
 dict(q="In which regions does the framework's illustrative list place Chinese ethnic enclaves?",
   choices=[
     "Southeast Asia, the Caribbean, South America and North America",
     "East and Southern Africa, the Caribbean and Southeast Asia",
     "North America alone",
     "North and South America alone",
     "Western Europe and the Pacific"], ans=0,
   why="The CED prints Chinese in Southeast Asia, the Caribbean, South America, and North America under its heading Migrant ethnic enclaves for topic 6.7, illustrating KC-5.4.III.B. The second option is the framework's Indian entry, the third its Irish entry and the fourth its Italian entry, so each names a real list belonging to another group."),
 dict(q="In which regions does the framework's illustrative list place Indian ethnic enclaves?",
   choices=[
     "East and Southern Africa, the Caribbean and Southeast Asia",
     "Southeast Asia, the Caribbean, South America and North America",
     "North America alone",
     "North and South America alone",
     "The Pacific islands and Australia"], ans=0,
   why="The CED prints Indians in East and Southern Africa, the Caribbean, and Southeast Asia under its heading Migrant ethnic enclaves for topic 6.7, illustrating KC-5.4.III.B. The Chinese, Irish and Italian entries in the same list name the other combinations offered here."),
 dict(q="Which group's enclaves does the framework's illustrative list place in Africa?",
   choices=[
     "Indians",
     "Chinese",
     "Irish",
     "Italians",
     "Japanese"], ans=0,
   why="The CED's enclave list for topic 6.7 names Indians in East and Southern Africa and places no other group there: the Chinese entry runs through Southeast Asia and the Americas, the Irish entry is North America and the Italian entry North and South America. Japanese agricultural workers appear in topic 6.6's list of returning migrants, not in this one, and KC-5.4.III.B is the statement all of these illustrate."),
 dict(q="Which group does the framework's enclave list place in North America and nowhere else?",
   choices=[
     "Irish",
     "Italians",
     "Chinese",
     "Indians",
     "Lebanese"], ans=0,
   why="The CED prints Irish in North America under Migrant ethnic enclaves for topic 6.7, with no second region beside it, while Italians are listed in North and South America and the Chinese and Indian entries each run across several regions. Lebanese merchants belong to topic 6.6's returning migrants, and KC-5.4.III.B is the statement the list illustrates."),
 dict(q="The framework's enclave list places Italians in which regions?",
   choices=[
     "North and South America",
     "North America alone",
     "South America alone",
     "Southeast Asia and the Caribbean",
     "East and Southern Africa"], ans=0,
   why="The CED prints Italians in North and South America under Migrant ethnic enclaves for topic 6.7, illustrating KC-5.4.III.B. Naming one of the two continents alone drops half of the entry, and the remaining options belong to the Chinese and Indian entries in the same list."),
 dict(q="Which pair does the framework give as its illustrations of states attempting to regulate the flow of people across their borders?",
   choices=[
     "The Chinese Exclusion Act and the White Australia policy",
     "The Chinese Exclusion Act and the Opium Wars",
     "The White Australia policy and the construction of the Port of Buenos Aires",
     "The Sokoto Caliphate and the Cherokee Nation",
     "The Ghost Dance and the Mahdist wars"], ans=0,
   why="The CED prints the Chinese Exclusion Act and the White Australia policy under its heading Regulation of immigrants for topic 6.7, illustrating KC-5.4.III.C. The Opium Wars and the Port of Buenos Aires illustrate economic imperialism in topic 6.5, and the remaining names belong to topic 6.3's list of new states and rebellions."),
 dict(q="The framework prints the Chinese Exclusion Act as an illustration of which of its statements?",
   choices=[
     "That states attempted to regulate the increased flow of people across their borders",
     "That migrants often created ethnic enclaves that transplanted their culture",
     "That migrants tended to be male",
     "That many individuals chose freely to relocate in search of work",
     "That new methods of transportation allowed many migrants to return home"], ans=0,
   why="The CED prints the Chinese Exclusion Act under its heading Regulation of immigrants for topic 6.7, beside KC-5.4.III.C, the statement that receiving societies did not always embrace immigrants as seen in the ways states attempted to regulate the increased flow of people across their borders. KC-5.4.III.B, KC-5.4.III.A, KC-5.4.II.A and KC-5.4.I.B are the four other statements offered, each a real statement of this unit and none the one this example illustrates. The framework names the measure and describes nothing whatever about it."),
 dict(q="An illustrative letter from a village, quoted here without attribution, reports that since the young men went overseas 'the fields are sown and the accounts kept by their wives and mothers, who never did either before'. Which of the framework's statements does the letter illustrate?",
   choices=[
     "That women in the home society took on roles formerly occupied by men",
     "That migrants created ethnic enclaves that transplanted their culture",
     "That receiving societies did not always embrace immigrants",
     "That states attempted to regulate the flow of people across their borders",
     "That migrants were able to return home periodically or permanently"], ans=0,
   why="KC-5.4.III.A states that migrants tending to be male left women to take on new roles in the home society that had been formerly occupied by men, and a village where wives and mothers now sow and keep accounts is that clause in a source. Enclaves, prejudice, border regulation and return are separate statements of this unit."),
 dict(q="An illustrative traveller's description of a quarter in a large port city, quoted here without attribution, notes that its residents worship as they did at home, print a newspaper in their own language and settle disputes through their own associations. Within this topic's framework, the quarter is best described as",
   choices=[
     "an ethnic enclave that helped transplant a culture into a new environment",
     "an example of a receiving state regulating the flow of people across its border",
     "an example of migrants abandoning the culture of the society they had left",
     "an example of a home society taking on roles formerly occupied by men",
     "an example of a resource export economy"], ans=0,
   why="KC-5.4.III.B states that migrants often created ethnic enclaves in different parts of the world that helped transplant their culture into new environments, and worship, a newspaper and associations of the migrants' own are the institutions that do the transplanting. Border regulation belongs to KC-5.4.III.C, the change of roles to KC-5.4.III.A and export economies to topic 6.4."),
 dict(q="An illustrative newspaper column in a receiving city, quoted here without attribution, argues that the newcomers 'are of a race that cannot be made part of this people'. Which of the framework's statements does the column illustrate most directly?",
   choices=[
     "That receiving societies did not always embrace immigrants, prejudice being one form that took",
     "That receiving societies always embraced the immigrants who arrived",
     "That migrants created ethnic enclaves in different parts of the world",
     "That migrants tended to be male",
     "That many individuals chose freely to relocate in search of work"], ans=0,
   why="KC-5.4.III.C states that receiving societies did not always embrace immigrants, as seen in the various degrees of ethnic and racial prejudice, and an argument that a group cannot be made part of a people is prejudice of that kind. The remaining options name other statements of this unit rather than the one the column illustrates."),
 dict(q="An illustrative statute of the period, quoted here without attribution, forbids the entry of labourers of one named nationality while admitting merchants and students of the same nationality. Within this topic's framework, the statute illustrates",
   choices=[
     "a state attempting to regulate the increased flow of people across its border",
     "a state encouraging the free movement of people across its border",
     "the creation of an ethnic enclave by the migrants themselves",
     "the transfer of roles in a home society from men to women",
     "the return of migrants to their home societies"], ans=0,
   why="KC-5.4.III.C names the ways states attempted to regulate the increased flow of people across their borders as one of the two things in which the treatment of immigrants could be seen, and a statute admitting some categories while barring others is regulation of exactly that kind. Encouragement is its opposite, and enclaves, changed roles and return are separate statements."),
 dict(q="An illustrative annual report of a mutual aid society in a migrant quarter, quoted here without attribution, records that the society maintained a school in the migrants' language and organized the festivals of their calendar. This source supports which of the framework's claims?",
   choices=[
     "That ethnic enclaves helped transplant the migrants' culture into new environments",
     "That ethnic enclaves prevented the migrants from settling permanently",
     "That receiving states funded the institutions migrants established",
     "That migrants abandoned the observances of their home society on arrival",
     "That migrants tended to be female rather than male"], ans=0,
   why="KC-5.4.III.B states that migrants often created ethnic enclaves that helped transplant their culture into new environments, and a school in the migrants' language and the festivals of their calendar are that transplanting in practice. The framework says nothing about receiving states funding such institutions, and the last two options contradict KC-5.4.III.B and KC-5.4.III.A."),
 dict(q="An illustrative report by an official of a receiving state describes an immigrant district as orderly and industrious. Considering the point of view of the source, what does it most importantly limit?",
   choices=[
     "Its usefulness as evidence of how the district's residents understood their own situation",
     "Its usefulness as evidence that an immigrant district existed",
     "Its usefulness as evidence of what the official's own administration valued",
     "Its usefulness as a document produced in the period it describes",
     "Its usefulness as an indication of where the district was"], ans=0,
   why="The report is written from the receiving state's side, so it is good evidence of what that administration noticed and valued and poor evidence of the residents' own understanding, which it does not attempt to record. KC-5.4.III.C makes the attitude of receiving societies part of this topic, which is why the point of view of an official source matters here."),
 dict(q="The record below reports, for four hypothetical arrival records, how many of every hundred arrivals were men and how many were women. What pattern does it show?",
   choices=[
     "In every record men outnumbered women among the arrivals",
     "In every record women outnumbered men among the arrivals",
     "Men and women arrived in equal numbers in every record",
     "Men outnumbered women in two records and women outnumbered men in two",
     "The record does not distinguish men from women"], ans=0,
   table=_T_ARRIVALS,
   why="Read from the record alone: 78 against 22, 71 against 29, 84 against 16 and 66 against 34, so men lead in all four rows and the two columns are given separately for every record. KC-5.4.III.A states that migrants tended to be male, which is the tendency this record sets out."),
 dict(q="Using the same hypothetical arrival records, which record comes closest to an even division between men and women?",
   choices=[
     "Record 4",
     "Record 1",
     "Record 2",
     "Record 3",
     "The records are equally far from an even division"], ans=0,
   table=_T_ARRIVALS,
   why="Read from the record alone: the gap between the two columns is 56 in Record 1, 42 in Record 2, 68 in Record 3 and 32 in Record 4, so Record 4 is the narrowest and the gaps are not equal. KC-5.4.III.A describes a tendency, which is consistent with streams differing in how pronounced it is."),
 dict(q="The table below reports, for one hypothetical home district, how many households in every hundred had a woman performing each task before and after the departures. Which conclusion does it support?",
   choices=[
     "The three tasks women had seldom performed before the departures passed largely to women afterwards, while the task they already performed changed little",
     "All four tasks passed from men to women in equal measure",
     "The task women already performed showed the largest change of the four",
     "Women performed fewer of every task after the departures than before",
     "The table records no change in any task"], ans=0,
   table=_T_TASKS,
   why="Read from the table alone: managing the holding runs 12 to 57, selling produce 19 to 61 and hiring labour 7 to 44, while weaving, already at 88, ends at 86. KC-5.4.III.A states that women took on new roles in the home society formerly occupied by men, and a task women already did is not a new role, which is why it moves differently."),
 dict(q="In the same hypothetical district record, which task shows the largest rise in the number of households where a woman performed it?",
   choices=[
     "Managing the family holding",
     "Selling produce at market",
     "Hiring seasonal labour",
     "Weaving cloth for household use",
     "Every task rose by the same amount"], ans=0,
   table=_T_TASKS,
   why="Read from the table alone: the rises are 45 for managing the holding, 42 for selling produce and 37 for hiring labour, while weaving falls by 2, so the rises are neither equal nor led by weaving. KC-5.4.III.A is the statement about new roles that this record illustrates."),
 dict(q="The table below counts the institutions recorded in one hypothetical migrant quarter. Which conclusion does it support?",
   choices=[
     "The quarter sustained institutions of the migrants' own worship, language and mutual assistance",
     "The quarter recorded no institution belonging to the migrants themselves",
     "The only institutions recorded in the quarter were places of worship",
     "The quarter recorded more newspapers than mutual aid societies",
     "The quarter recorded more schools than mutual aid societies"], ans=0,
   table=_T_QUARTER,
   why="Read from the table alone: six places of worship, four schools in the migrants' language, nine mutual aid societies and three newspapers, so all four kinds are present and mutual aid societies outnumber both the newspapers and the schools. KC-5.4.III.B states that ethnic enclaves helped transplant the migrants' culture into new environments, and these are the institutions through which that happens."),
 dict(q="The table below records how many applicants in every hundred were admitted at one hypothetical receiving state's border, by category of applicant. Which conclusion is best supported?",
   choices=[
     "Admission turned on where an applicant came from and on the means they held, not on the wish to enter alone",
     "Admission turned only on the number of applicants presenting themselves",
     "Every category of applicant was admitted at about the same rate",
     "Applicants from the restricted country were admitted more readily than their neighbours",
     "The state admitted no applicant in any category"], ans=0,
   table=_T_ADMISSION,
   why="Read from the table alone: 94 in every hundred from the neighbouring country and 89 of those holding capital above a stated sum are admitted, against 11 from the restricted country and 4 of its labourers. KC-5.4.III.C describes the ways states attempted to regulate the increased flow of people across their borders, and a rate that varies this widely by category is such an attempt."),
 dict(q="A student reading the same hypothetical admission record concludes that the state admitted everyone who applied. Which figure most directly refutes that conclusion?",
   choices=[
     "Four in every hundred labourers from the restricted country were admitted",
     "Ninety-four in every hundred applicants from the neighbouring country were admitted",
     "The record distinguishes four categories of applicant",
     "The record gives its figures for every hundred who applied",
     "Applicants holding capital were admitted at a lower rate than their neighbours"], ans=0,
   table=_T_ADMISSION,
   why="The refutation has to come from the data the student is using, and the lowest rate in the record is 4 in every hundred, which is not everyone. The high rate for the neighbouring country, the number of categories and the units are true of the record and leave the claim standing, and KC-5.4.III.C is the statement about regulated borders that the record illustrates."),
 dict(q="Learning objective H asks students to explain how and why new patterns of migration affected society. Which of the following is a question of that kind?",
   choices=[
     "Why did the departure of many men change what women did in the societies they left?",
     "In which year did the largest migration stream of the period begin?",
     "How many people left each country in each decade of the period?",
     "Which migration stream was the most important of the period?",
     "What was the name of every association founded in a migrant quarter?"], ans=0,
   why="Unit 6 Learning Objective H asks how and why new patterns of migration affected society from 1750 to 1900, and KC-5.4.III.A is precisely such an effect with a cause attached. Dates, totals, rankings and lists of names are not what that objective asks for, and the framework prints none of them for this topic."),
 dict(q="Why does the framework place the effects of migration under the theme of social interactions and organization?",
   choices=[
     "Because migration changed how societies grouped their members and how those groups treated one another",
     "Because the framework treats migration as a subject belonging only to economic history",
     "Because migration is said to have left every society's social organization unchanged",
     "Because the theme concerns only the internal organization of receiving states",
     "Because the framework treats social organization as fixed by geography alone"], ans=0,
   why="The Social Interactions and Organization focus concerns the process by which societies group their members and the norms governing interactions between those groups. KC-5.4.III.A changes roles within a home society, KC-5.4.III.B creates new groups within receiving ones and KC-5.4.III.C concerns how those groups were treated, which is that theme in operation rather than an economic or geographic account."),
 dict(q="Which question about the effects of migration can be answered from the framework, and which cannot?",
   choices=[
     "What kinds of effect the framework identifies can be answered; what any named measure provided cannot",
     "What any named measure provided can be answered; what kinds of effect the framework identifies cannot",
     "Neither the kinds of effect nor the regions of the enclaves can be answered",
     "Both the kinds of effect and the year each enclave was founded can be answered",
     "Only the number of migrants in each enclave can be answered"], ans=0,
   why="KC-5.4.III.A, KC-5.4.III.B and KC-5.4.III.C name changed roles in the home society, ethnic enclaves and the treatment of immigrants, so the kinds of effect are answerable, and the CED prints the enclave regions as well. It names the Chinese Exclusion Act and the White Australia policy without stating a single provision, date or number, so those cannot be answered here. The anchor carries both clauses because the exact reversal is offered."),
 dict(q="Taking this topic's three statements together, what account of the effects of migration do they give?",
   choices=[
     "Migration changed the roles left open in the societies migrants left, created enclaves that carried their culture abroad, and met treatment in receiving societies that ranged from acceptance to prejudice and legal restriction",
     "Migration changed nothing in the societies migrants left, and receiving societies accepted every arrival",
     "Migration changed the societies migrants left but had no effect of any kind on the societies that received them",
     "Migration affected receiving societies alone, the societies of departure being unchanged",
     "The framework describes the causes of migration but identifies none of its effects"], ans=0,
   why="KC-5.4.III.A gives the change in the home society, KC-5.4.III.B the enclaves that transplanted culture into new environments and KC-5.4.III.C the qualified reception, including prejudice and attempts at regulation. The key holds all three together, while each rejected option deletes one side of the account or denies that the framework gives it."),
]
