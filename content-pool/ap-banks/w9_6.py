# AP WORLD HISTORY: MODERN 9.6 Globalized Culture After 1900
# CED effective Fall 2026 (Course Framework V.1), Unit 9 Globalization,
# c. 1900 to the present. Thematic focus: Cultural Developments and Interactions
# (CDI). Reasoning process: Continuity and Change.
#
# Learning Objective: Unit 9 Learning Objective F -- explain HOW AND WHY
# globalization changed culture over time. Both halves are in the objective, and
# the second is the one a bank forgets: the framework supplies a cause for the
# change in the arts and this module keeps it. Suggested skill 4.B, explain how a
# specific historical development or process is situated within a broader
# historical context.
#
# HISTORICAL DEVELOPMENTS this topic prints, and the only sentences the keys
# below rest on:
#   KC-6.3.IV.i    Political and social changes of the 20th century led to
#                  changes in the arts and in the second half of the century,
#                  popular and consumer culture became more global.
#   KC-6.3.IV.ii   Arts, entertainment, and popular culture increasingly
#                  reflected the influence of a globalized society.
#   KC-6.3.IV.iii  Consumer culture became globalized and transcended national
#                  borders.
#
# THE THREE SENTENCES ARE CLOSE IN MEANING, WHICH IS THE HAZARD HERE. A bank
# that did not separate them would be thirty ways of saying "culture became
# global". They divide like this and every claim in the verifier says which one
# it is using:
#   * KC-6.3.IV.i carries a CAUSE and a TIMING. Political and social changes LED
#     TO changes in the arts; and it is in the SECOND HALF of the century that
#     popular and consumer culture became more global. Items 2, 10, 18 and 25
#     turn on the cause; items 6 and 21 on the timing.
#   * KC-6.3.IV.ii is about arts, entertainment and popular culture REFLECTING
#     the influence of a globalized society -- reflecting, which is not the same
#     as causing it. Items 4, 13 and 23 hold that verb.
#   * KC-6.3.IV.iii is specifically about CONSUMER culture and specifically about
#     TRANSCENDING NATIONAL BORDERS. Items 8, 16 and 27 stay on that.
#
# ILLUSTRATIVE EXAMPLES the CED prints on this page, in two lists:
#   Global culture: music, reggae; movies, Bollywood; social media, Facebook and
#     Twitter; television, the BBC; sports, World Cup soccer and the Olympics.
#   Global consumerism: online commerce, Alibaba and eBay; global brands, Toyota
#     and Coca-Cola.
# Illustrative examples are optional course content, so exactly TWO items turn on
# them and both stems say the course prints them as such.
#
# WHAT IS DELIBERATELY NOT KEYED. Whether the globalization of culture was good
# or bad for the societies it reached is a live argument and the framework does
# not settle it. NO key here says a global culture enriched or impoverished
# anyone, that any tradition was lost or saved, that any culture is more or less
# authentic than another, or that any country's cultural influence was deserved
# or excessive. The framework's claims are that changes in the arts followed
# political and social change, that arts and popular culture reflected a
# globalized society, and that consumer culture crossed borders. Those are what
# is keyed. The objections belong to Topic 9.7, which covers responses to rising
# cultural and economic globalization, and they are neither imported here nor
# argued away.
#
# DEDUPE NOTE. Topic 9.4 covers the economics of the global age -- multinational
# corporations, trade agreements, where manufacturing was carried on. This module
# covers CULTURE, including consumer culture as a cultural fact rather than as an
# industry, and the economic sentences appear here only as distractors. Topic 9.1
# covers the communication technologies themselves under KC-6.1.I.A; this module
# uses them only as the setting in which a cultural development is situated.
#
# SOURCES. Section I is stimulus-based and this bank cannot display an image, so
# every stimulus is TEXT and none is attributed to a real person or document. No
# real work of art, film, song or programme is described or evaluated. TABLES are
# hypothetical, each states a whole and its parts, and every keyed conclusion is
# recomputed from the table alone. DATES are written "1950 to 1990", never with a
# hyphen.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md; the real Section I prints four.
TOPIC = ("9.6", "Globalized Culture After 1900", 9)

_T_FILMS = dict(
    headers=["Period (hypothetical record of feature films released in one country)",
             "Films released",
             "Of those, shown also outside the country",
             "Of those, shown only within it"],
    rows=[["1930s", "120", "12", "108"],
          ["1960s", "200", "60", "140"],
          ["1990s", "310", "186", "124"]])

_T_SCHEDULE = dict(
    headers=["Period (hypothetical schedule of one broadcaster, hours per week)",
             "Broadcast hours",
             "Of those, programmes made in other countries",
             "Of those, programmes made at home"],
    rows=[["1955", "60", "6", "54"],
          ["1975", "120", "36", "84"],
          ["1995", "240", "108", "132"]])

_T_MARKETS = dict(
    headers=["Firm (hypothetical survey of consumer goods firms)",
             "Countries in which the firm sells",
             "Of those, countries outside its home region",
             "Of those, countries within its home region"],
    rows=[["Firm one", "90", "72", "18"],
          ["Firm two", "45", "30", "15"],
          ["Firm three", "12", "4", "8"]])

QUESTIONS = [

 dict(q="A gallery catalogue of 1965 observes that the paintings it exhibits took their subjects from the political upheavals of the preceding decades and could not have been made in the same form before them. According to this course, the catalogue describes",
   choices=[
     "changes in the arts that followed the political and social changes of the twentieth century",
     "changes in the arts that produced the political and social changes of the twentieth century",
     "the globalization of consumer culture across national borders",
     "the growth of knowledge economies in some regions of the world",
     "the reduction of the problem of geographic distance by new technologies"],
   ans=0,
   why="KC-6.3.IV.i states that political and social changes of the twentieth century LED TO changes in the arts. The catalogue puts the upheavals before the paintings and makes the paintings depend on them, which is the framework's own order, and a distractor reverses it."),

 dict(q="According to this course, what led to the changes in the arts during the twentieth century?",
   choices=[
     "The political and social changes of the century",
     "The invention of the shipping container and of air travel",
     "The spread of vaccines and antibiotics",
     "The redrawing of political boundaries after colonial withdrawals",
     "The release of greenhouse gases into the atmosphere"],
   ans=0,
   why="KC-6.3.IV.i states that political and social changes of the twentieth century led to changes in the arts. Unit 9 Learning Objective F asks HOW AND WHY globalization changed culture, and this sentence is the framework's answer to the why; the distractors name developments the framework states in other topics."),

 dict(q="A hypothetical record divides one country's film releases into two groups in each period. Which conclusion does the table alone support?",
   table=_T_FILMS,
   choices=[
     "The number of films released rose in each period, and the share shown outside the country rose with it",
     "The number of films released fell in each period after the first one recorded",
     "The share shown outside the country fell across the record",
     "The number of films shown only within the country rose in each period recorded",
     "Most of the films released were shown outside the country in every period recorded"],
   ans=0,
   why="KC-6.3.IV.i states that in the second half of the century popular and consumer culture became more global, and films crossing borders in rising proportion are one form that takes. The record is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="How does this course describe the relation between arts, entertainment and popular culture on one side and a globalized society on the other?",
   choices=[
     "They increasingly reflected the influence of a globalized society",
     "They increasingly resisted every influence from outside their own country",
     "They created a globalized society where none had existed",
     "They were unaffected by the society around them during this period",
     "They ceased to be produced once societies became globalized"],
   ans=0,
   why="KC-6.3.IV.ii states that arts, entertainment, and popular culture increasingly REFLECTED the influence of a globalized society. Reflected is the framework's own verb and it makes the culture the register of the change rather than its author, which is why a key saying they created that society would go past the sentence."),

 dict(q="A department store's buying guide of 1988 lists goods it stocks from twelve countries and notes that customers now ask for them by name. Within this course's framework, the guide illustrates",
   choices=[
     "consumer culture becoming globalized and transcending national borders",
     "the arts reflecting the influence of a globalized society",
     "political and social changes leading to changes in the arts",
     "the growth of knowledge economies following advances in communications",
     "movements protesting the inequality of the consequences of global integration"],
   ans=0,
   why="KC-6.3.IV.iii states that consumer culture became globalized and transcended national borders. Goods from a dozen countries asked for by name in one shop is that crossing of borders at the point of sale, and the framework treats it as a fact about consumer culture rather than about the arts."),

 dict(q="This course places the moment at which popular and consumer culture became more global at a particular point. Where?",
   choices=[
     "In the second half of the twentieth century",
     "In the first decade of the twentieth century",
     "In the years immediately before World War I",
     "In the nineteenth century, before the period this unit covers",
     "At no point the framework identifies"],
   ans=0,
   why="KC-6.3.IV.i states that political and social changes of the twentieth century led to changes in the arts and IN THE SECOND HALF OF THE CENTURY popular and consumer culture became more global. The framework's own phrase places the second development in the century's later half, distinguishing it from the changes in the arts that the same sentence does not date so narrowly."),

 dict(q="A hypothetical schedule divides one broadcaster's weekly hours into two groups in each period. Which conclusion does the table alone support?",
   table=_T_SCHEDULE,
   choices=[
     "Total hours rose in each period, and the share given to programmes made abroad rose without ever reaching a majority",
     "No programme made in another country was broadcast in the earliest period recorded",
     "The share given to programmes made abroad fell across the record",
     "The hours given to programmes made at home fell in each period recorded",
     "Programmes made abroad filled more than half the schedule in the last period recorded"],
   ans=0,
   why="KC-6.3.IV.ii states that arts, entertainment, and popular culture increasingly reflected the influence of a globalized society, and a schedule taking in more foreign-made programmes over time is that influence in one broadcaster's week. The record is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="This course prints certain things as illustrative examples of a global culture. Which list is the one the course prints?",
   choices=[
     "Reggae in music, Bollywood in movies, Facebook and Twitter in social media, the BBC in television, and World Cup soccer and the Olympics in sports",
     "Alibaba and eBay in online commerce, and Toyota and Coca-Cola as global brands",
     "The World Trade Organization, NAFTA, and ASEAN",
     "Greenpeace, the Green Belt Movement in Kenya, and the World Fair Trade Organization",
     "The Universal Declaration of Human Rights, global feminism movements, and the Negritude movement"],
   ans=0,
   why="The CED prints these beside KC-6.3.IV.i and KC-6.3.IV.ii as illustrative examples of global culture. The second list is this page's separate list of global consumerism, and the rest are printed beside statements in other topics, on trade agreements and on the movements of Topic 9.5. The item asks which list the course prints and evaluates none of the works or organizations in it."),

 dict(q="An unattributed magazine essay of 1978 argues that the novels of its decade cannot be read without knowing what had happened politically to the societies that produced them. According to this course, the essay's premise is",
   choices=[
     "consistent with the framework, which states that political and social changes led to changes in the arts",
     "inconsistent with the framework, which states that the arts changed independently of politics",
     "inconsistent with the framework, which states that the arts did not change in this century",
     "consistent with the framework, which states that the arts produced the political changes of the century",
     "inconsistent with the framework, which places all changes in the arts before 1900"],
   ans=0,
   why="KC-6.3.IV.i states that political and social changes of the twentieth century led to changes in the arts, which is the essay's premise stated as course content. The distractors either deny the relation, reverse it or move it outside the period, and each is a reading of the sentence the sentence does not permit."),

 dict(q="A hypothetical record shop's inventory of 1982 shows that a musical form which had originated on one island is now stocked in its main section rather than among imports. This local change is best situated within",
   choices=[
     "popular culture becoming more global in the second half of the twentieth century",
     "political and social changes leading to changes in the arts early in the century",
     "the growth of manufacturing in Asia and Latin America",
     "the widening of access to education in much of the world",
     "the release of pollutants into the atmosphere and the debates it produced"],
   ans=0,
   why="KC-6.3.IV.i states that in the second half of the century popular and consumer culture became more global, and the CED prints reggae among its illustrative examples of a global culture in music. A form moving from the imports rack to the main section is that globalization inside one shop, which skill 4.B asks a student to situate in the broader process."),

 dict(q="Which of the following does this course say about consumer culture in particular?",
   choices=[
     "It became globalized and transcended national borders",
     "It remained confined within the borders of each national market",
     "It disappeared during the second half of the twentieth century",
     "It was replaced by state provision of goods in every country",
     "It is not a subject the framework treats in this period"],
   ans=0,
   why="KC-6.3.IV.iii states that consumer culture became globalized and TRANSCENDED NATIONAL BORDERS. Transcending borders is the framework's own phrase for what happened to consumer culture, and it is the sentence that distinguishes KC-6.3.IV.iii from the two beside it."),

 dict(q="A hypothetical survey divides each firm's markets into two groups. Which conclusion does the table alone support?",
   table=_T_MARKETS,
   choices=[
     "Every firm surveyed sells outside its home region, and for two of the three most of their markets lie outside it",
     "No firm surveyed sells in any country outside its home region",
     "For every firm surveyed, most of its markets lie within its home region",
     "Every firm surveyed sells in the same number of countries",
     "Firm three sells in more countries than firm two sells in"],
   ans=0,
   why="KC-6.3.IV.iii states that consumer culture became globalized and transcended national borders, and firms selling beyond their home regions are one form that crossing takes. The survey is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier; the key says two of three rather than all three because that is what the figures show."),

 dict(q="A theatre programme of 1991 explains that the production borrows staging conventions from three continents and expects its audience to recognize them. According to this course, the production is an instance of",
   choices=[
     "the arts increasingly reflecting the influence of a globalized society",
     "the arts increasingly rejecting the influence of a globalized society",
     "consumer culture transcending national borders",
     "political and social change leading to a change in economic policy",
     "the reduction of the problem of geographic distance by transportation"],
   ans=0,
   why="KC-6.3.IV.ii states that arts, entertainment, and popular culture increasingly reflected the influence of a globalized society. A staging that borrows across continents and expects to be understood is that influence registered in the work itself, and the framework's verb is reflected rather than rejected."),

 dict(q="Which statement about culture in this period is NOT supported by this course?",
   choices=[
     "Consumer culture remained wholly contained within national borders",
     "Political and social changes of the century led to changes in the arts",
     "Popular culture became more global in the second half of the century",
     "Arts and entertainment increasingly reflected a globalized society",
     "Consumer culture became globalized during this period"],
   ans=0,
   why="KC-6.3.IV.iii states that consumer culture became globalized and TRANSCENDED national borders, so a claim that it stayed wholly within them reverses the framework's sentence. The item asks which statement is NOT supported, so the key is deliberately the false one; the other four restate KC-6.3.IV.i, KC-6.3.IV.ii and KC-6.3.IV.iii."),

 dict(q="An unattributed trade journal of 1997 reports that a firm's advertising now runs in the same form in thirty countries, with only the language changed. Within this course's framework, this belongs to",
   choices=[
     "consumer culture becoming globalized and transcending national borders",
     "the political and social changes that led to changes in the arts",
     "the movements protesting the inequality of global integration's consequences",
     "the widening of participation in new professional roles",
     "the growth of knowledge economies in some regions"],
   ans=0,
   why="KC-6.3.IV.iii states that consumer culture became globalized and transcended national borders, and the CED prints global brands among its illustrative examples of global consumerism. One campaign running in thirty countries with only the language changed is that transcendence in its plainest commercial form."),

 dict(q="A student writes that this course says the arts caused the political changes of the twentieth century. What is the best correction?",
   choices=[
     "The framework says political and social changes led to changes in the arts, which is the reverse relation",
     "The framework says the arts and politics changed independently of one another",
     "The framework says the arts did not change during the twentieth century",
     "The framework says political change occurred only in the second half of the century",
     "The framework says the arts are not a subject it treats in this period"],
   ans=0,
   why="KC-6.3.IV.i states that political and social changes of the twentieth century LED TO changes in the arts, which fixes politics as prior and the arts as what followed. The student has the relation the right pair but the wrong way round, so the correction has to name the direction rather than deny the connection."),

 dict(q="A hypothetical sports federation's report of 1972 notes that its championship is now followed in countries with no team in it. This course would situate the report within",
   choices=[
     "popular culture becoming more global in the second half of the century",
     "political and social changes leading to changes in the arts",
     "consumer culture being confined within national markets",
     "the strong role newly independent governments took in guiding economic life",
     "the encouragement of free-market policies in the late twentieth century"],
   ans=0,
   why="KC-6.3.IV.i states that in the second half of the century popular and consumer culture became more global, and the CED prints World Cup soccer and the Olympics among its illustrative examples of a global culture in sports. An audience in countries with no team in the competition is that globalization measured by attention rather than by participation."),

 dict(q="Unit 9 Learning Objective F asks a student to explain two things about globalization and culture. What are they?",
   choices=[
     "How globalization changed culture, and why it did so",
     "When globalization began, and which country began it",
     "How many people took part in it, and where they lived",
     "Which forms of culture are the most valuable, and why",
     "Whether globalization should have been allowed to happen"],
   ans=0,
   why="Unit 9 Learning Objective F, printed on this topic's page, is to explain HOW AND WHY globalization changed culture over time. The framework supplies the why in KC-6.3.IV.i, where political and social changes led to changes in the arts, and it does not ask a student to rank cultures or to judge whether globalization should have occurred."),

 dict(q="This course prints certain firms and services as illustrative examples of global consumerism. Which list is the one the course prints?",
   choices=[
     "Alibaba and eBay in online commerce, and Toyota and Coca-Cola as global brands",
     "Reggae, Bollywood, the BBC, and the Olympics",
     "Nestle, Nissan, and Mahindra and Mahindra",
     "Finland, Japan, and the United States",
     "The World Trade Organization, NAFTA, and ASEAN"],
   ans=0,
   why="The CED prints Alibaba and eBay under online commerce and Toyota and Coca-Cola as global brands, beside KC-6.3.IV.iii on global consumerism. The second option is this page's separate list of global culture, and the rest are printed beside KC-6.3.II.B and KC-6.3.I.E in Topic 9.4. The item asks which list the course prints and evaluates none of the firms named."),

 dict(q="Two developments of the century are set side by side: changes in what artists made, and the spread of popular culture across borders. What does this course say about their timing?",
   choices=[
     "The framework attributes the changes in the arts to the century's political and social changes and dates the spread of popular culture to the century's second half",
     "The framework dates both to the first decade of the century",
     "The framework dates both to the years before 1900",
     "The framework states that the spread of popular culture preceded any change in the arts",
     "The framework gives no indication of when either occurred"],
   ans=0,
   why="KC-6.3.IV.i contains both: political and social changes of the twentieth century led to changes in the arts, AND in the second half of the century popular and consumer culture became more global. The sentence attributes the first and dates the second, and the key reports each in the framework's own terms."),

 dict(q="A researcher wants to test the claim that a country's popular culture became more global over the second half of the century. Which evidence would bear most directly on the claim?",
   choices=[
     "Records over time of how much of what was watched, heard and read there came from elsewhere",
     "Records of the country's total electricity generation over the same years",
     "Records of the number of political parties contesting its elections",
     "Records of the tonnage of grain it harvested each year",
     "Records of the average age of its population over the same years"],
   ans=0,
   why="KC-6.3.IV.i states that in the second half of the century popular and consumer culture became more global, and KC-6.3.IV.ii that arts, entertainment and popular culture increasingly reflected the influence of a globalized society. What people watched, heard and read, and where it came from, is the direct measure of both; the other records bear on developments the framework treats in other topics."),

 dict(q="An unattributed exhibition review of 1969 describes a work that draws on techniques from several traditions and argues that this is now unremarkable. Which of this course's statements does the review's observation match?",
   choices=[
     "That arts and popular culture increasingly reflected the influence of a globalized society",
     "That arts and popular culture increasingly withdrew from any influence beyond their own tradition",
     "That consumer culture remained bounded by national borders",
     "That political and social change ceased to affect the arts after 1950",
     "That the arts of this period are not treated by the framework"],
   ans=0,
   why="KC-6.3.IV.ii states that arts, entertainment, and popular culture INCREASINGLY reflected the influence of a globalized society, and a reviewer finding such borrowing unremarkable is reporting that increase as an accomplished fact. The key describes what the work does and makes no judgement of its quality or authenticity."),

 dict(q="How does this course relate the globalization of consumer culture to national borders?",
   choices=[
     "Consumer culture transcended those borders rather than being contained by them",
     "Consumer culture reinforced those borders and stayed inside them",
     "Consumer culture caused those borders to be redrawn",
     "Consumer culture abolished national borders entirely",
     "The framework states no relation between the two"],
   ans=0,
   why="KC-6.3.IV.iii states that consumer culture became globalized and TRANSCENDED national borders. Transcended is the framework's own verb: the culture crossed the borders rather than being confined by them, and it is not the same as abolishing them, which is why the key states the crossing and a distractor overstates it."),

 dict(q="A commentator argues that culture in the twentieth century changed for reasons entirely internal to the arts themselves. Which of this course's statements most directly complicates that argument?",
   choices=[
     "That political and social changes of the century led to changes in the arts",
     "That consumer culture transcended national borders",
     "That access to education became more inclusive in much of the world",
     "That manufacturing was increasingly situated in Asia and Latin America",
     "That new international organizations formed to maintain world peace"],
   ans=0,
   why="KC-6.3.IV.i states that political and social changes of the twentieth century led to changes in the arts, which locates a cause outside the arts themselves. Unit 9 Learning Objective F asks for the WHY of cultural change, and the framework's answer is what the commentator's argument leaves out."),

 dict(q="An unattributed customs return of 1993 records that recorded consumer goods now enter the country from four times as many places of origin as in 1953. Within this course's framework, the return documents",
   choices=[
     "consumer culture becoming globalized across national borders",
     "the arts reflecting the influence of a globalized society",
     "political and social change producing changes in the arts",
     "the movements protesting the consequences of global integration",
     "the growth of knowledge economies in some regions of the world"],
   ans=0,
   why="KC-6.3.IV.iii states that consumer culture became globalized and transcended national borders. Goods arriving from four times as many origins over forty years is that crossing recorded by the authority that counts what crosses, and skill 4.B asks a student to situate the specific record in the broader process."),

 dict(q="Which pair states a change and a continuity in culture as this course presents the century?",
   choices=[
     "The sources on which arts and popular culture drew widened, while societies went on producing arts and popular culture",
     "Societies ceased to produce arts and popular culture, while the sources they drew on widened",
     "The sources narrowed to a single tradition, while production continued as before",
     "Neither the sources nor the production of culture altered in any way",
     "Both the sources and the production of culture ceased during the century"],
   ans=0,
   why="KC-6.3.IV.ii states that arts, entertainment, and popular culture increasingly reflected the influence of a globalized society, which is a widening of what they drew on within an activity that continued. The reasoning process the CED prints beside this topic is continuity and change, and the key holds one of each."),

 dict(q="A hypothetical cultural ministry's annual report of 1986 asks whether the country's audiences now have more in common with audiences abroad than with their own grandparents. This course would treat the question as belonging to",
   choices=[
     "the globalization of popular and consumer culture in the second half of the century",
     "the political and social changes that led to changes in the arts",
     "the widening of access to education and professional roles",
     "the encouragement of free-market economic policies by governments",
     "the emergence of new epidemic diseases as threats to populations"],
   ans=0,
   why="KC-6.3.IV.i states that in the second half of the century popular and consumer culture became more global, and KC-6.3.IV.iii that consumer culture transcended national borders. A ministry asking whether its audiences now resemble foreign audiences more than earlier generations of their own is asking about that process, and the framework supplies no answer about whether it is to be welcomed."),

 dict(q="Considered across this topic, what does this course say happened to culture as globalization proceeded?",
   choices=[
     "The arts changed under the century's political and social pressures, popular culture became more global, and consumer culture crossed national borders",
     "The arts were unaffected by politics, popular culture stayed local, and consumer culture stayed within borders",
     "The arts changed but popular and consumer culture were untouched by any wider influence",
     "Culture of every kind was replaced by commerce during the second half of the century",
     "Culture became identical everywhere and no local production of any kind continued"],
   ans=0,
   why="KC-6.3.IV.i supplies the political and social changes leading to changes in the arts and the globalization of popular and consumer culture in the century's second half, KC-6.3.IV.ii the arts reflecting a globalized society, and KC-6.3.IV.iii consumer culture transcending national borders. The key is the conjunction of the three, and the framework nowhere states that culture became identical everywhere."),

 dict(q="A student is asked why this course treats consumer culture as part of the history of culture rather than only as part of the history of trade. Which answer best fits the framework?",
   choices=[
     "Because the framework names consumer culture alongside popular culture as something that became global and crossed borders",
     "Because the framework treats consumer culture as identical with the arts",
     "Because the framework treats trade as having no history of its own",
     "Because the framework denies that consumer goods are bought and sold",
     "Because the framework places consumer culture before the twentieth century"],
   ans=0,
   why="KC-6.3.IV.i names popular AND CONSUMER culture together as what became more global in the second half of the century, and KC-6.3.IV.iii gives consumer culture its own sentence about transcending national borders. The framework therefore places it inside the cultural statements of this unit rather than only inside the economic ones of Topic 9.4."),

 dict(q="Taking the topic as a whole, which single sentence best states what this course says about culture after 1900?",
   choices=[
     "The century's political and social upheavals changed what artists made, popular and consumer culture became more global in the century's second half, and what people watched, heard and bought increasingly reflected a world that crossed its own borders",
     "Culture in the twentieth century was unaffected by politics, stayed within national borders and drew on no influence from beyond them",
     "Culture in the twentieth century became identical in every country and all local production ceased",
     "Culture in the twentieth century changed only in the arts, while popular and consumer culture remained exactly as they had been",
     "Culture in the twentieth century is treated by this course only as a branch of trade and not as a subject of its own"],
   ans=0,
   why="KC-6.3.IV.i supplies the political and social changes leading to changes in the arts and the globalization of popular and consumer culture in the second half of the century, KC-6.3.IV.ii the arts and popular culture increasingly reflecting a globalized society, and KC-6.3.IV.iii consumer culture transcending national borders. The key is the conjunction of the three and each distractor contradicts at least one; none of the five passes judgement on whether the change was good."),
]
