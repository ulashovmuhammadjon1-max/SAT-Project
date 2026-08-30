# AP HUMAN GEOGRAPHY 3.8 Effects of Diffusion -- 30 questions
# CED Course Framework V.1, Unit 3. Enduring understanding SPS-3; learning
# objective SPS-3.B, "Explain how the process of diffusion results in changes to
# the cultural landscape."
#
# Essential knowledge -- one statement, a closed list of four:
#   SPS-3.B.1  Acculturation, assimilation, syncretism, and multiculturalism are
#              effects of the diffusion of culture.
#
# Four names, no definitions. The definitions this module holds itself to, and
# which every key is traced back to, are:
#
#   acculturation     a group adopts some traits of another culture -- usually
#                     the dominant or host one -- while RETAINING substantial
#                     elements of its own. Both cultures are still identifiable
#                     in the group's practice.
#   assimilation      a group's distinctive traits are largely LOST, so it
#                     becomes culturally indistinguishable from the host
#                     society. Usually the end point of several generations.
#   syncretism        two traditions BLEND into a combined form, most often
#                     discussed for religion, so that the result carries
#                     elements of both fused rather than held side by side.
#   multiculturalism  several cultural groups COEXIST within one society, each
#                     maintaining distinctiveness, often supported deliberately
#                     by policy.
#
# THE AXIS THAT ORGANIZES THE FOUR, and the reason most items here are
# comparative rather than definitional. Acculturation and assimilation sit on
# one scale measuring how much of the original culture survives -- some, versus
# very little. Syncretism is a different thing entirely: not a degree of
# retention but a fusion producing a third form. Multiculturalism is a property
# of the SOCIETY rather than of a group inside it. Items 5, 9, 13, 17, 22 and 25
# turn on keeping those three kinds of claim apart.
#
# ON SYNCRETISM AND CREOLIZATION. Topic 3.5's creolization and this topic's
# syncretism describe closely related outcomes, and this module says so rather
# than pretending they are unrelated: both name a blend that belongs to neither
# parent. The CED assigns creolization to interaction with global forces and
# syncretism to the effects of diffusion, and items 14 and 21 keep to those
# assignments.
#
# A DISCIPLINE THE MODULE OBSERVES. These four terms carry political weight --
# assimilation in particular has been demanded of minorities by force. Items ask
# what a process IS and what conditions produce it, never whether it is
# desirable, because the second question has no answer a key could defend.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g3_8.py. FIVE choices (A-E).
TOPIC = ("3.8", "Effects of Diffusion", 3)

QUESTIONS = [
 dict(q="Which four effects of cultural diffusion does the framework name?",
   choices=[
     "Acculturation, assimilation, syncretism, and multiculturalism",
     "Acculturation, migration, syncretism, and urbanization",
     "Assimilation, colonialism, syncretism, and globalization",
     "Acculturation, assimilation, creolization, and nationalism",
     "Syncretism, multiculturalism, relocation, and expansion"],
   ans=0,
   why="EK SPS-3.B.1 names exactly these four as effects of the diffusion of culture. Creolization belongs to Topic 3.5's statement, relocation and expansion are types of diffusion from Topic 3.4, and migration and urbanization are processes rather than effects."),

 dict(q="A migrant community adopts the host country's language for work and schooling while continuing to speak its own at home, keep its own religious calendar, and cook its own food. This is best described as",
   choices=[
     "Acculturation, since traits of the host culture have been adopted while substantial elements of the original remain",
     "Assimilation, since the host language is now used",
     "Syncretism, since two cultures are present",
     "Multiculturalism, since two cultures exist in one household",
     "No cultural effect, since the community has not changed"],
   ans=0,
   why="EK SPS-3.B.1 names acculturation among the effects of diffusion, and the defining feature is partial adoption with substantial retention. Both cultures remain identifiable in the community's practice, which is what separates it from assimilation."),

 dict(q="By the third generation, a migrant-origin community speaks only the national language, keeps only national holidays, and is not distinguishable in practice from other citizens. This is",
   choices=[
     "Assimilation, since the group's distinctive traits have largely been lost",
     "Acculturation, since some adoption has occurred",
     "Syncretism, since the two cultures met",
     "Multiculturalism, since the group lives in a diverse society",
     "Not an effect of diffusion at all"],
   ans=0,
   why="EK SPS-3.B.1 names assimilation among the effects of diffusion. It differs from acculturation in degree rather than in kind: the distinctive traits are not merely supplemented but largely gone, which is usually the work of several generations."),

 dict(q="A religious festival in one region combines observances, symbols, and dates from two traditions into a single celebration that adherents of both recognize as their own. This is",
   choices=[
     "Syncretism, since two traditions have blended into a combined form",
     "Assimilation, since one tradition absorbed the other",
     "Acculturation, since some practices were adopted",
     "Multiculturalism, since two traditions exist",
     "Not diffusion, since the festival is local"],
   ans=0,
   why="EK SPS-3.B.1 names syncretism among the effects of diffusion, and its defining feature is fusion rather than coexistence or replacement. Neither tradition is intact and neither has vanished; what exists is a third form built from both."),

 dict(q="What is the essential difference between acculturation and assimilation?",
   choices=[
     "How much of the original culture survives: acculturation retains substantial elements while assimilation loses nearly all of them",
     "Acculturation applies to individuals and assimilation to groups",
     "Acculturation is voluntary and assimilation is always forced",
     "Acculturation concerns language and assimilation concerns religion",
     "There is no difference between the two"],
   ans=0,
   why="EK SPS-3.B.1 lists both as effects of diffusion without defining either, and the standard distinction is one of degree along a single dimension. Both can be voluntary or coerced and both operate on groups, so neither of those axes separates them."),

 dict(q="A country's policy recognizes several languages officially, funds community institutions for different groups, and does not require newcomers to abandon their practices. This is best described as",
   choices=[
     "Multiculturalism, since the society is organized to let several cultures coexist while remaining distinct",
     "Assimilation, since the country has one government",
     "Acculturation, since newcomers learn about the country",
     "Syncretism, since the cultures are in contact",
     "Not an effect of diffusion, since it is a policy"],
   ans=0,
   why="EK SPS-3.B.1 names multiculturalism among the effects of diffusion. Unlike the other three it describes the SOCIETY rather than a group inside it, and it is frequently a deliberate arrangement rather than an outcome nobody chose."),

 dict(q="Which of the four effects is a property of a whole society rather than of a particular group within it?",
   choices=[
     "Multiculturalism",
     "Acculturation",
     "Assimilation",
     "Syncretism",
     "None of them, since all four describe groups"],
   ans=0,
   why="Acculturation and assimilation describe what happens to a group's traits, and syncretism describes what happens to two traditions. Multiculturalism describes how a society is arranged, which is why it is the one term that could be a stated policy."),

 dict(q="A geographer says a community 'has acculturated but not assimilated'. What does this mean?",
   choices=[
     "It has taken on host-society traits while keeping enough of its own that it remains culturally distinguishable",
     "It has lost all of its original traits",
     "It has refused all contact with the host society",
     "It has blended two religions into one",
     "It has become a separate country"],
   ans=0,
   why="EK SPS-3.B.1 lists both terms, and using them together in this way places the community at a particular point on the retention scale. The claim is precise: substantial adoption has occurred and substantial distinctiveness has survived it."),

 dict(q="Which of the following distinguishes syncretism from acculturation?",
   choices=[
     "Syncretism produces a fused third form, while acculturation leaves two identifiable cultures operating in one group",
     "Syncretism applies only to language",
     "Acculturation produces a fused form and syncretism does not",
     "Syncretism occurs only in societies with a policy of multiculturalism",
     "There is no difference between them"],
   ans=0,
   why="EK SPS-3.B.1 lists the two separately, and the difference is what the result looks like. An acculturated community can be described as doing some things one way and some the other; a syncretic form cannot be separated back into its sources."),

 dict(q="A state requires all schooling in one language, bans minority-language publications, and makes citizenship conditional on cultural conformity. Which effect is being pursued, and how?",
   choices=[
     "Assimilation, pursued by state coercion rather than arising through ordinary contact",
     "Multiculturalism, since the state is making a cultural policy",
     "Syncretism, since two cultures are involved",
     "Acculturation, since some traits will be adopted",
     "No effect, since policy cannot change culture"],
   ans=0,
   why="EK SPS-3.B.1 names assimilation among the effects of diffusion without saying how it comes about, and it can arise gradually or be demanded. Naming the mechanism is what makes the description accurate, since the outcome sought is the same in both cases."),

 dict(q="A second-generation member of a migrant community is fluent in both languages, observes both sets of holidays, and moves easily between the two settings. Which term fits best?",
   choices=[
     "Acculturation, since host-society traits have been added without the original being displaced",
     "Assimilation, since the person is fluent in the national language",
     "Syncretism, since the person combines two cultures",
     "Multiculturalism, since the person knows two cultures",
     "None of the four, since the person is an individual"],
   ans=0,
   why="EK SPS-3.B.1's acculturation is adoption with retention, and holding both repertoires intact is exactly that. Syncretism would require the two to have fused into something new rather than being kept available separately."),

 dict(q="Which observation would best indicate that assimilation rather than acculturation has occurred?",
   choices=[
     "The group's language, observances, and distinctive practices are no longer transmitted to children",
     "The group has adopted the national language for work",
     "The group lives in a diverse city",
     "The group's members hold citizenship",
     "The group has adopted some national holidays"],
   ans=0,
   why="EK SPS-3.B.1 lists both effects and the difference is retention, which is measured by what passes to the next generation. Adopting a working language or a holiday is compatible with keeping everything else, whereas the end of transmission is not."),

 dict(q="Which pairing correctly matches a case to the framework term it illustrates?",
   choices=[
     "A society funding schools in several community languages, matched to multiculturalism",
     "A community losing its language entirely, matched to acculturation",
     "Two religious traditions fusing into one observance, matched to assimilation",
     "A community adding a second language while keeping its first, matched to assimilation",
     "A society with one official culture, matched to syncretism"],
   ans=0,
   why="EK SPS-3.B.1 names all four terms, and only the first pairing attaches a case to the term whose defining feature it has. Losing a language entirely is assimilation, fusion is syncretism, and adding a language while keeping the first is acculturation."),

 dict(q="How are Topic 3.5's creolization and this topic's syncretism related?",
   choices=[
     "Both name a blend that belongs to neither parent, and the framework places one under interaction with global forces and the other under the effects of diffusion",
     "They are unrelated concepts",
     "Creolization applies to religion and syncretism to language",
     "Syncretism is a stage that always precedes creolization",
     "They mean the same thing and the framework lists both by mistake"],
   ans=0,
   why="EK SPS-3.A.1 names creolization among the new forms interaction produces and EK SPS-3.B.1 names syncretism among the effects of diffusion. The underlying idea is the same -- fusion into a third form -- and the difference is which process the CED attaches each to."),

 dict(q="Which of the four effects is most likely to be the subject of explicit government policy?",
   choices=[
     "Multiculturalism, since it describes how a society is arranged and can therefore be legislated for",
     "Syncretism, since religion is regulated",
     "Acculturation, since it happens gradually",
     "Assimilation, since it is automatic",
     "None of them, since culture cannot be legislated"],
   ans=0,
   why="EK SPS-3.B.1's multiculturalism describes an arrangement of a society rather than a change inside a group, and arrangements are what policy makes. Assimilation has also been pursued by policy, but it is an outcome rather than a way of organizing coexistence."),

 dict(q="Two communities arrive in the same city in the same decade. One assimilates within two generations and the other retains its distinctiveness. Which explanation is most consistent with the framework?",
   choices=[
     "Group size, spatial concentration, institutional support, and how the host society treats each community all affect the rate of retention",
     "One community was inherently more resistant to change",
     "The two communities cannot really have arrived at the same time",
     "Assimilation always takes exactly two generations",
     "Retention is determined by climate"],
   ans=0,
   why="EK SPS-3.B.1 lists acculturation and assimilation as effects rather than as inevitabilities, so the rate at which either occurs must depend on conditions. A large, concentrated community with its own institutions can transmit practices that a small dispersed one cannot."),

 dict(q="A religious tradition arriving in a new region absorbs local festivals, saints, and calendar dates, producing observances found nowhere else. This is",
   choices=[
     "Syncretism, since the two traditions have fused into a locally distinctive form",
     "Assimilation of the arriving tradition",
     "Multiculturalism, since two traditions are present",
     "Acculturation, since the local tradition adopted new practices",
     "No effect, since religions always vary locally"],
   ans=0,
   why="EK SPS-3.B.1 names syncretism among the effects of diffusion. The diagnostic is that the result exists in neither source region: a form that could be found intact somewhere else would be diffusion without fusion."),

 dict(q="Why can the four effects the framework names occur in the same city at the same time?",
   choices=[
     "They describe different groups, different generations, and different domains of life, so one city can show all four at once",
     "Because the four terms mean the same thing",
     "Because only one can occur at a time and cities change quickly",
     "Because the framework lists them in order of occurrence",
     "They cannot occur simultaneously"],
   ans=0,
   why="EK SPS-3.B.1 lists four effects without ordering them or making them exclusive. One community may be assimilating while another acculturates, a religious practice fuses, and the city's institutions operate multiculturally, all in the same year."),

 dict(q="A student writes that acculturation is 'the first stage of assimilation'. What is the most accurate response?",
   choices=[
     "Acculturation can persist indefinitely without leading to assimilation, so treating it as a stage assumes an outcome that often does not occur",
     "The student is exactly right in every case",
     "Acculturation never precedes assimilation",
     "Acculturation and assimilation are unrelated",
     "Assimilation always precedes acculturation"],
   ans=0,
   why="EK SPS-3.B.1 lists the two as separate effects rather than as points on a required sequence. Communities have remained acculturated and distinct for centuries, so treating retention as a temporary condition builds a prediction into a definition."),

 dict(q="A city district contains institutions, businesses, and public signage serving four different origin communities, none of which is losing its practices. Which term describes the district?",
   choices=[
     "Multiculturalism, since several cultures coexist while remaining distinct",
     "Assimilation, since all four communities are in one city",
     "Syncretism, since four cultures are in contact",
     "Acculturation, since each community adapts somewhat",
     "None of the four, since the district is small"],
   ans=0,
   why="EK SPS-3.B.1 names multiculturalism as an effect of diffusion, and it describes coexistence with maintained distinctiveness. That each community also adapts somewhat is true and is a separate observation about each group rather than about the district."),

 dict(q="Which is the strongest reason syncretism is discussed most often in relation to religion?",
   choices=[
     "Religious systems supply calendars, figures, and rituals that can be recombined, and arriving faiths have frequently absorbed local observances rather than replacing them",
     "Religion is the only cultural domain that changes",
     "Religion cannot diffuse in any other way",
     "Religions are always more tolerant than other institutions",
     "The framework applies syncretism only to religion"],
   ans=0,
   why="EK SPS-3.B.1 names syncretism without restricting it to religion, so the explanation has to be about why the case is common rather than exclusive. Faiths carry many separable elements and have often gained adherents faster by absorbing local practice than by forbidding it."),

 dict(q="A community's cuisine, music, and dress persist while its language shifts to the national one within two generations. How should this be described?",
   choices=[
     "Acculturation that is uneven across domains, since retention differs from one part of cultural life to another",
     "Complete assimilation",
     "Complete retention with no change",
     "Syncretism of two languages",
     "Multiculturalism within the community"],
   ans=0,
   why="EK SPS-3.B.1's acculturation is partial adoption with retention, and nothing requires the partition to fall the same way in every domain. Language shifts fastest because school and work require it, while food and music carry no comparable pressure."),

 dict(q="Which of the following is NOT one of the framework's four effects of diffusion?",
   choices=[
     "Nationalism",
     "Acculturation",
     "Assimilation",
     "Syncretism",
     "Multiculturalism"],
   ans=0,
   why="EK SPS-3.B.1's list contains acculturation, assimilation, syncretism and multiculturalism, and only those four. Nationalism is a political force treated in Unit 4 rather than an effect of cultural diffusion named here."),

 dict(q="A host society's attitude changes from requiring newcomers to abandon their practices to funding their community institutions. Which shift does this represent?",
   choices=[
     "From a policy pursuing assimilation to one supporting multiculturalism",
     "From syncretism to acculturation",
     "From multiculturalism to assimilation",
     "From acculturation to syncretism",
     "No shift, since both policies produce the same outcome"],
   ans=0,
   why="EK SPS-3.B.1 names both assimilation and multiculturalism among the effects of diffusion, and a state can pursue either. Requiring abandonment aims at the loss of distinctiveness while funding institutions aims at its maintenance, which are opposite goals."),

 dict(q="What is the most defensible general statement about which of the four effects a given case of diffusion will produce?",
   choices=[
     "It depends on the size and concentration of the arriving group, the institutions available to it, and how the receiving society responds",
     "Diffusion always produces assimilation eventually",
     "Diffusion always produces multiculturalism",
     "Diffusion always produces syncretism",
     "The outcome is random and cannot be explained"],
   ans=0,
   why="EK SPS-3.B.1 lists four effects side by side without ranking them or making any of them inevitable. The listing itself implies that circumstances select among them, which is why an honest general statement names the circumstances rather than an outcome."),

 dict(q="Language use is recorded for one migrant-origin community across three generations. Using the table, which effect do the data show?",
   table=dict(
     headers=["Generation", "Speak the community language at home (%)", "Speak the national language fluently (%)"],
     rows=[
       ["First", "97", "34"],
       ["Second", "71", "96"],
       ["Third", "58", "99"]]),
   choices=[
     "Acculturation, since fluency in the national language reaches nearly all while a majority still uses the community language at home",
     "Assimilation, since national language fluency reaches 99 percent",
     "Syncretism, since two languages are used",
     "Multiculturalism, since the community speaks two languages",
     "No effect, since both figures are high in the third generation"],
   ans=0,
   why="National language fluency rises from 34 to 99 percent while home use of the community language falls only from 97 to 58, so a majority still transmits it. Adoption with substantial retention is acculturation, and the two columns are independent shares rather than a composition summing to 100."),

 dict(q="The same measures are recorded for a different community. Using the table, which effect do these data show?",
   table=dict(
     headers=["Generation", "Speak the community language at home (%)", "Speak the national language fluently (%)"],
     rows=[
       ["First", "94", "29"],
       ["Second", "38", "97"],
       ["Third", "4", "100"]]),
   choices=[
     "Assimilation, since home use of the community language has fallen to 4 percent and is no longer being transmitted",
     "Acculturation, since some households still use the community language",
     "Syncretism, since the two languages blended",
     "Multiculturalism, since the community remains identifiable",
     "The same pattern as any acculturating community"],
   ans=0,
   why="Home use falls from 94 to 4 percent across three generations while national fluency reaches 100, which is a collapse rather than a partial shift. Comparing this with an acculturating community's fall from 97 to 58 is what shows the two outcomes are different in degree rather than in kind."),

 dict(q="Elements of a regional religious festival are traced to their sources. Using the table, which effect does the festival illustrate?",
   table=dict(
     headers=["Element of the festival", "Source"],
     rows=[
       ["Date in the calendar", "Pre-existing local tradition"],
       ["Central figure honoured", "Arriving tradition"],
       ["Procession route and music", "Pre-existing local tradition"],
       ["Liturgical texts used", "Arriving tradition"],
       ["Foods prepared", "Both, combined in one dish"]]),
   choices=[
     "Syncretism, since elements of both traditions are fused into a single observance found in neither source",
     "Assimilation, since the arriving tradition prevailed",
     "Acculturation, since the local tradition adopted some elements",
     "Multiculturalism, since two traditions are represented",
     "No effect, since festivals always vary"],
   ans=0,
   why="Two elements come from each tradition and one is a combination of both, so the festival is neither tradition intact nor either one replaced. EK SPS-3.B.1's syncretism is exactly a fused form, and one that exists in neither source region cannot be a case of simple transfer."),

 dict(q="Institutional provision for four origin communities in one city is recorded. Using the table, what does the city's arrangement illustrate?",
   table=dict(
     headers=["Community", "Publicly funded schools in the community language", "Community associations receiving public funds", "Public signage in the community language"],
     rows=[
       ["Community 1", "6", "14", "Yes"],
       ["Community 2", "3", "9", "Yes"],
       ["Community 3", "2", "11", "Yes"],
       ["Community 4", "4", "7", "Yes"]]),
   choices=[
     "Multiculturalism, since public institutions support four communities in maintaining their distinctiveness",
     "Assimilation, since all four communities live in one city",
     "Acculturation, since each community uses public services",
     "Syncretism, since four cultures are present",
     "No framework effect, since the numbers are small"],
   ans=0,
   why="All four communities receive funded schools, funded associations and public signage in their own languages, which is a society organized for coexistence rather than for convergence. EK SPS-3.B.1's multiculturalism is the only one of the four terms that describes an arrangement of a society."),

 dict(q="Retention of four cultural domains is recorded for one community after four generations. Using the table, what is the most accurate description?",
   table=dict(
     headers=["Domain", "Households still practising (%)"],
     rows=[
       ["Community language at home", "11"],
       ["Religious observance", "62"],
       ["Festival participation", "78"],
       ["Cuisine at family occasions", "91"]]),
   choices=[
     "Acculturation that is highly uneven across domains, with language nearly lost while cuisine, festivals, and observance persist",
     "Complete assimilation across all domains",
     "Complete retention across all domains",
     "Syncretism, since four domains are involved",
     "No change, since three of the four exceed 60 percent"],
   ans=0,
   why="Retention runs from 11 percent for language to 91 percent for cuisine, a range of 80 points across four domains of one community. EK SPS-3.B.1's acculturation is partial adoption with retention, and nothing requires the partition to fall the same way in every part of cultural life."),
]
