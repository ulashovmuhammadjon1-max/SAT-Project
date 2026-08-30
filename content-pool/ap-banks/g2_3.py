# AP HUMAN GEOGRAPHY 2.3 Population Composition -- 30 questions
# CED Course Framework V.1, Unit 2. Enduring understanding PSO-2; two learning
# objectives.
#
# Essential knowledge, in full:
#   PSO-2.E.1  Patterns of age structure and sex ratio vary across different
#              regions and may be mapped and analyzed at different scales.
#   PSO-2.F.1  Population pyramids are used to assess population growth and
#              decline and to predict markets for goods and services.
#
# PSO-2.E.1 names the two elements of composition -- AGE STRUCTURE and SEX RATIO
# -- and asserts that both vary regionally and are analyzable at more than one
# scale. PSO-2.F.1 says what the pyramid is FOR, and it names two uses, not one:
# assessing growth or decline, AND predicting markets for goods and services.
# The second use is the one students forget, and items 9, 10, 18, 22 and 27 are
# built on it because the CED authorizes it explicitly.
#
# The conventions every key here rests on, stated once so a reader can audit
# them. The CED does not define these, so items turning on them argue from the
# arithmetic rather than citing a code:
#   sex ratio        males per 100 females; above 100 means more males
#   age structure    the distribution of a population among age cohorts
#   cohort           everyone born in the same span of years, tracked together
#   a WIDE base      many children relative to adults: high fertility, growth
#   a NARROW base    few children relative to adults: below-replacement
#                    fertility, eventual decline
#   an indentation   a cohort reduced by war, famine, epidemic, or emigration
#   a bulge in the working ages with a narrow base is the signature of
#                    IN-MIGRATION of workers, not of a fertility change
#
# A note on what this bank can and cannot carry: it has no images, so no stem
# refers to "the pyramid shown." Where a pyramid is needed it is supplied as a
# real cohort table, which is the same information in the same structure. The
# CED's own sample activity for this topic has students build pyramids for
# SUBNATIONAL units, which is why items 8, 13, 20 and 26 work below the national
# scale.
#
# Six items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g2_3.py. FIVE choices (A-E).
TOPIC = ("2.3", "Population Composition", 2)

QUESTIONS = [
 dict(q="What does a population pyramid display?",
   choices=[
     "The size of each age cohort, divided by sex, for a defined population at one point in time",
     "The change in a country's total population over the past century",
     "The distribution of population across a country's regions",
     "The number of births expected in each of the next fifty years",
     "The ratio of urban to rural residents by age"],
   ans=0,
   why="EK PSO-2.F.1 makes the pyramid the standard tool for assessing growth and decline, and it does that by showing composition: how many people fall in each age band and how those numbers divide between the sexes at a single moment."),

 dict(q="A country's population pyramid has a very wide base that narrows sharply with each older cohort. What does this indicate?",
   choices=[
     "High fertility together with high mortality, and a population that will grow as the large young cohorts reach childbearing age",
     "Low fertility and an aging population",
     "A population that has stopped growing",
     "Heavy in-migration of working-age adults",
     "A population that is evenly distributed among age groups"],
   ans=0,
   why="EK PSO-2.F.1 makes the pyramid a tool for assessing growth and decline. Each cohort being larger than the one above it means more people are being born than were born before, and that momentum carries growth forward even if fertility later falls."),

 dict(q="A country's pyramid is narrower at the base than in the middle and has a substantial top. The most defensible reading is that",
   choices=[
     "Fertility has fallen below the level needed to replace the parent generation, so the population will eventually decline without migration",
     "The country is experiencing very rapid natural increase",
     "The country has an unusually high infant mortality rate",
     "The country's population is growing because the middle cohorts are large",
     "The country must be receiving large numbers of child migrants"],
   ans=0,
   why="A base smaller than the cohorts above it means each generation is being replaced by a smaller one. Growth may continue for some years while the large middle cohorts survive, but the structure guarantees decline once they age out, absent migration."),

 dict(q="Sex ratio, as geographers use the term, is",
   choices=[
     "The number of males per 100 females in a population",
     "The share of a population that is female",
     "The difference between male and female life expectancy",
     "The ratio of male to female births over a decade",
     "The proportion of households headed by a man"],
   ans=0,
   why="EK PSO-2.E.1 names sex ratio as an element of population composition without defining it, and the standard convention is males per 100 females. A value above 100 therefore indicates a male-majority population and a value below 100 a female-majority one."),

 dict(q="A country whose economy depends on temporary contract labour in construction reports a national sex ratio of 220. The most likely explanation is",
   choices=[
     "Large-scale in-migration of working-age men, which raises the male count without changing the resident female population",
     "An unusually high male birth rate",
     "Very low female life expectancy",
     "A recent war that killed many women",
     "An error, since sex ratios cannot exceed 100"],
   ans=0,
   why="EK PSO-2.E.1 says sex ratio patterns vary across regions, and labour migration is the mechanism that produces the most extreme national values. Only migration can move a whole country's ratio that far, because births and deaths cannot generate a two-to-one imbalance."),

 dict(q="In most countries the sex ratio is above 100 in the youngest cohorts and below 100 in the oldest. What accounts for the pattern?",
   choices=[
     "Slightly more boys are born than girls, and women live longer on average, so the balance reverses with age",
     "Boys migrate away and girls remain",
     "The oldest cohorts were counted less accurately",
     "Sex ratios are calculated differently for different age groups",
     "More girls than boys are born, and men live longer"],
   ans=0,
   why="The pattern is produced by two independent facts working in opposite directions across the life course: a small male surplus at birth and a female advantage in survival. The crossover point is where cumulative mortality has erased the initial excess."),

 dict(q="A rural county's pyramid shows a deep notch in the 20-39 age bands for both sexes, with children and older adults well represented. The best explanation is",
   choices=[
     "Out-migration of young adults to cities for work and education, leaving children and the elderly behind",
     "A sudden fall in fertility forty years ago",
     "A war that killed only young adults",
     "In-migration of retirees",
     "An epidemic that spared the young and the old"],
   ans=0,
   why="EK PSO-2.E.1 allows age structure to be analyzed at scales below the national, and at the county scale migration reshapes composition faster than fertility or mortality can. A notch confined to the working ages while children remain is the signature of adults leaving and not taking everyone with them."),

 dict(q="A pyramid for a single city district shows a large bulge in the 18-24 cohort and very few children or people over 50. The district most likely contains",
   choices=[
     "A large university, whose students dominate the district's population for a few years each",
     "A retirement community",
     "A new suburban subdivision of family houses",
     "An industrial zone with no housing",
     "A district experiencing very high fertility"],
   ans=0,
   why="EK PSO-2.E.1 states that age structure may be mapped and analyzed at different scales, and at the district scale a single institution can dominate the profile. A cohort confined to a four-year band with almost nothing above or below it is what a student population looks like."),

 dict(q="A country's pyramid has a very wide base. Which set of goods and services should a planner expect demand for first?",
   choices=[
     "Primary schools, pediatric care, and childhood vaccination",
     "Nursing homes and mobility aids",
     "Retirement housing and pension administration",
     "Assisted-living facilities and geriatric medicine",
     "Bereavement and estate services"],
   ans=0,
   why="EK PSO-2.F.1 states that population pyramids are used to predict markets for goods and services. A wide base is a large cohort of children, and the services a child needs arrive on a known schedule that the pyramid makes visible years in advance."),

 dict(q="A country's pyramid is top-heavy, with its largest cohorts between 55 and 74. Which market is most likely to expand over the next fifteen years?",
   choices=[
     "Geriatric health care, long-term residential care, and retirement income products",
     "Maternity wards and infant formula",
     "Primary school construction",
     "Playground equipment and children's clothing",
     "University dormitories"],
   ans=0,
   why="EK PSO-2.F.1 names market prediction as a use of the pyramid. Reading the largest cohorts forward fifteen years puts them into the ages where health, care and pension needs are highest, which is a demand forecast made from composition alone."),

 dict(q="A pyramid shows a sharp indentation affecting one cohort in BOTH sexes, with normal-sized cohorts above and below it. Which explanation fits best?",
   choices=[
     "A period of war, famine, or epidemic that reduced births or raised deaths for a few years and left the surrounding cohorts intact",
     "Sustained out-migration over the last fifty years",
     "A permanent fall in fertility",
     "A change in the age at which people are counted",
     "Unusually high male mortality in that cohort"],
   ans=0,
   why="A defect confined to one cohort and affecting both sexes equally points to a short, dated event rather than a trend, since a trend would deform every cohort after it began. Both sexes being affected rules out a cause specific to one of them."),

 dict(q="Twenty-five years after a large baby boom, a country's pyramid shows a second, smaller bulge at the youngest ages. What is this?",
   choices=[
     "An echo effect, in which an unusually large cohort reaching childbearing age produces an unusually large cohort of births even at normal fertility",
     "A second baby boom caused by rising fertility",
     "An error in the census",
     "The result of immigration of families with children",
     "Evidence that fertility rose in exactly the same proportion"],
   ans=0,
   why="The number of births is the fertility rate multiplied by the number of women of childbearing age, so a large parent cohort produces many births without any change in the rate. The echo is smaller than the original boom because fertility itself is lower."),

 dict(q="A national pyramid looks broadly balanced while the pyramids of the country's largest city and its rural interior look completely different from each other. What does this show?",
   choices=[
     "Composition varies at scales below the national, and a national profile is an average of very different local ones",
     "One of the three pyramids must be wrong",
     "National pyramids are more accurate than local ones",
     "Population composition cannot be analyzed below the national scale",
     "The city and the interior have the same age structure in reality"],
   ans=0,
   why="EK PSO-2.E.1 states that age structure and sex ratio may be mapped and analyzed at different scales. Internal migration moves young adults from one part of a country to another without changing the national total, so the national picture conceals the two opposite local ones."),

 dict(q="Which pair of features on a pyramid together indicate recent in-migration of workers rather than a change in fertility?",
   choices=[
     "A pronounced bulge in the 25-44 cohorts combined with a narrow base",
     "A wide base combined with a narrow top",
     "A narrow base combined with a wide top",
     "Equal-sized cohorts at every age",
     "A bulge in the 0-9 cohorts combined with a narrow middle"],
   ans=0,
   why="Fertility change reshapes the pyramid from the bottom upward over decades, while migration inserts people directly into the ages at which they move. Working-age adults arriving without children produce exactly the combination described."),

 dict(q="A geographer says that a population pyramid is 'a history of the last hundred years read from the bottom up.' What does this mean?",
   choices=[
     "Each cohort's size records the births, deaths, and migrations that shaped it, so past events remain visible in the structure for decades",
     "Pyramids are drawn from historical documents rather than censuses",
     "The pyramid predicts the next hundred years exactly",
     "Only the base of a pyramid carries information",
     "Pyramids can be constructed only for countries with long records"],
   ans=0,
   why="A cohort is a group of people born together and thereafter only shrinks or is added to by migration, so whatever happened to it stays legible as a notch or a bulge. Reading upward is reading backward in time through the events each cohort lived through."),

 dict(q="Which statement about age structure and economic planning is best supported by the framework?",
   choices=[
     "Because a cohort's size is known years before it reaches school or working age, composition supports planning that population totals alone cannot",
     "Age structure is useful only for historical study",
     "Only total population matters for planning",
     "Age structure changes too quickly to be used for planning",
     "Age structure is relevant only in rapidly growing countries"],
   ans=0,
   why="EK PSO-2.F.1 names assessing growth or decline and predicting markets as the two uses of the pyramid, and both depend on cohorts aging predictably. A child counted today will need a secondary school place in a decade, which a headline total does not tell a planner."),

 dict(q="Two countries have identical total populations, but one has 40 percent of its people under 15 and the other has 18 percent over 65. Which comparison is most defensible?",
   choices=[
     "They face different demands on public spending, one weighted toward education and the other toward health and pensions",
     "They face identical demands, since their totals are equal",
     "The younger country will always be wealthier",
     "The older country's population must be declining faster",
     "Neither composition affects public spending"],
   ans=0,
   why="EK PSO-2.F.1 makes the pyramid a tool for predicting demand for goods and services, and the two compositions place their people in different service-consuming stages of life. Equal totals therefore imply nothing about equal budgets."),

 dict(q="A consumer goods firm uses national pyramids to decide which markets to enter. Which use is the framework explicitly endorsing?",
   choices=[
     "Predicting markets for goods and services from the size of the cohorts that buy them",
     "Estimating the accuracy of a national census",
     "Measuring the physical area of a country",
     "Determining a country's carrying capacity",
     "Calculating a country's arithmetic density"],
   ans=0,
   why="EK PSO-2.F.1 states in so many words that population pyramids are used to predict markets for goods and services. Cohort size is the number of potential buyers in the ages at which a product is used, which is what a market forecast rests on."),

 dict(q="Which is the strongest reason a sex ratio far from 100 at the SUBNATIONAL scale usually reflects migration rather than births and deaths?",
   choices=[
     "Births and deaths are close to balanced between the sexes everywhere, so only selective movement can shift a local ratio sharply",
     "Births are not recorded at the subnational scale",
     "Migration is the only demographic process that occurs locally",
     "Sex ratios are defined only for whole countries",
     "Local mortality differs enormously between the sexes"],
   ans=0,
   why="EK PSO-2.E.1 places sex ratio among the compositional patterns analyzable at different scales. Because the sexes are born and die in roughly similar numbers, a mining camp, a garrison, or a garment-factory town can only reach an extreme ratio by attracting one sex."),

 dict(q="A city planner builds separate pyramids for a new suburb, an inner-city district, and a coastal retirement town within the same metropolitan area. What is the strongest justification?",
   choices=[
     "The three areas attract different age groups, so a single metropolitan pyramid would average away the differences that determine what each area needs",
     "Metropolitan pyramids cannot be drawn",
     "Each area has a different total population",
     "Pyramids are valid only for areas under 100,000 people",
     "The three areas have identical compositions"],
   ans=0,
   why="EK PSO-2.E.1 states that composition may be mapped and analyzed at different scales, and the CED's own sample activity for this topic builds pyramids for subnational units. Averaging a student district with a retirement town produces a profile that describes neither."),

 dict(q="Which of the following would NOT be visible on a population pyramid?",
   choices=[
     "The share of the population living in cities",
     "An unusually small cohort born during a war",
     "A surplus of men in the working ages",
     "A large cohort of children under five",
     "A cohort of women markedly larger than the men of the same age"],
   ans=0,
   why="EK PSO-2.E.1 names age structure and sex ratio as the elements of composition, and a pyramid is built from exactly those two variables. Urban residence is a different attribute entirely and would require a separate cross-tabulation to appear."),

 dict(q="A pharmaceutical company notes that a country's 60-69 cohort is by far its largest. Which planning conclusion follows most directly?",
   choices=[
     "Demand for treatments used mainly in later life will rise over the next decade as that cohort ages",
     "The country's total population will fall next year",
     "Demand for childhood vaccines will rise sharply",
     "The country's sex ratio will move above 100",
     "The company should leave the market"],
   ans=0,
   why="EK PSO-2.F.1 authorizes the pyramid as a tool for predicting markets, and the prediction is made by advancing a known cohort through the ages at which a product is consumed. Nothing else in the structure is needed for that inference."),

 dict(q="Which statement correctly distinguishes population composition from population distribution?",
   choices=[
     "Composition describes what a population is made of by age and sex; distribution describes where its members are located",
     "Composition and distribution are two words for the same thing",
     "Composition describes location and distribution describes age",
     "Composition applies only to countries and distribution only to cities",
     "Distribution can be mapped and composition cannot"],
   ans=0,
   why="EK PSO-2.E.1 defines composition through age structure and sex ratio, which are properties of the people, while distribution is the arrangement of those people across territory. Two places with identical compositions can have entirely different distributions and the reverse holds too."),

 dict(q="A country's pyramid is nearly rectangular from the base to about age 60 before tapering. What does the shape indicate?",
   choices=[
     "Fertility close to replacement and low mortality until old age, so successive cohorts are of similar size",
     "Very rapid population growth",
     "A recent collapse in fertility",
     "Heavy emigration of young adults",
     "A population dominated by children"],
   ans=0,
   why="Cohorts of similar size mean each generation is being replaced by one about as large, and the taper starting only in old age means few people are lost before then. That combination is stability rather than growth or decline."),

 dict(q="Why can two countries with the same rate of natural increase have very different age structures?",
   choices=[
     "The same rate can arise from high fertility with high mortality or from low fertility with low mortality, and the two produce different cohort profiles",
     "The rate of natural increase determines age structure completely",
     "Age structure depends only on total population",
     "One of the two rates must have been calculated incorrectly",
     "Age structure and natural increase are unrelated concepts"],
   ans=0,
   why="A rate of natural increase is a difference between two other rates, so it can be reached from many combinations of them. High births with high deaths concentrates a population in the young ages, while low births with low deaths spreads it toward the old ones."),

 dict(q="A district's population by age and sex is shown. Using the table, what is the district's sex ratio, and what does the age profile suggest?",
   table=dict(
     headers=["Age group", "Males", "Females"],
     rows=[
       ["0-14", "1,200", "1,150"],
       ["15-24", "900", "880"],
       ["25-44", "6,400", "2,100"],
       ["45-64", "1,300", "900"],
       ["65+", "300", "420"]]),
   choices=[
     "A sex ratio of about 185, with the imbalance concentrated in the 25-44 group, suggesting in-migration of male workers",
     "A sex ratio of about 185, with the imbalance spread evenly across all of the age groups",
     "A sex ratio of about 53, since females outnumber males",
     "A sex ratio of about 100, since the youngest and oldest groups are nearly balanced",
     "A sex ratio that cannot be calculated without birth records"],
   ans=0,
   why="Totals of 10,100 males and 5,450 females give 185 males per 100 females, and the 25-44 band alone runs above 300 while the youngest and oldest bands are near balance or female-majority. An imbalance confined to the working ages is the migration signature."),

 dict(q="A country's population by age is shown for one year. Using the table, which market should grow fastest over the following decade?",
   table=dict(
     headers=["Age group", "Population (millions)"],
     rows=[
       ["0-9", "3.1"],
       ["10-19", "3.4"],
       ["20-29", "4.0"],
       ["30-39", "4.6"],
       ["40-49", "5.2"],
       ["50-59", "7.9"],
       ["60-69", "5.0"],
       ["70+", "3.8"]]),
   choices=[
     "Goods and services used from the early sixties onward, since the 7.9 million now aged 50-59 will move into that range",
     "Primary school places, since the 0-9 cohort is the one that will age",
     "Maternity services, since the 20-29 cohort is large",
     "University places, since the 10-19 cohort will reach university age within the decade",
     "Nothing can be predicted, since the table gives only one year"],
   ans=0,
   why="The largest cohort in the table is the 50-59 group at 7.9 million, and in ten years it will occupy the 60-69 band, replacing a group of 5.0 million. Advancing a known cohort by a known number of years is exactly the market prediction the pyramid supports."),

 dict(q="Two countries' age structures are compared. Using the table, which statement is best supported?",
   table=dict(
     headers=["Age group", "Country A (% of population)", "Country B (% of population)"],
     rows=[
       ["0-14", "42", "16"],
       ["15-64", "55", "63"],
       ["65+", "3", "21"]]),
   choices=[
     "Country A faces rising demand for schooling while Country B faces rising demand for elder care, although both have 100 percent of their population accounted for",
     "Country A has more people than Country B",
     "Country B has a wider pyramid base than Country A",
     "The two countries face identical service demands",
     "Country A's population is older than Country B's"],
   ans=0,
   why="Both columns sum to 100 percent, so the comparison is about shape rather than size: 42 percent under 15 against 16, and 3 percent over 65 against 21. Percentages carry no information about totals, which is why the option about which country has more people cannot be evaluated from this table."),

 dict(q="Cohort sizes for one country are shown by year of birth. Using the table, which cohort was most affected by a short crisis?",
   table=dict(
     headers=["Years of birth", "Cohort size (thousands)"],
     rows=[
       ["1930-1934", "820"],
       ["1935-1939", "845"],
       ["1940-1944", "410"],
       ["1945-1949", "870"],
       ["1950-1954", "905"]]),
   choices=[
     "The 1940-1944 cohort, which is less than half the size of the cohorts on either side of it",
     "The 1950-1954 cohort, which is the largest in the table",
     "The 1930-1934 cohort, which is the smallest of the pre-war cohorts",
     "The 1945-1949 cohort, which grew after the previous one",
     "No cohort, since the sizes rise overall across the table"],
   ans=0,
   why="One cohort at 410 thousand sits between neighbours of 845 and 870, a shortfall of more than half, while every other step in the series is small. A defect confined to a single span with normal cohorts on both sides points to a brief dated event rather than a trend."),

 dict(q="Sex ratios by age are shown for one country. Using the table, at which age band does the ratio first fall below 100, and what explains the pattern?",
   table=dict(
     headers=["Age band", "Males per 100 females"],
     rows=[
       ["0-14", "105"],
       ["15-29", "104"],
       ["30-44", "102"],
       ["45-59", "99"],
       ["60-74", "91"],
       ["75+", "72"]]),
   choices=[
     "At 45-59, because a small male surplus at birth is gradually erased by higher male mortality at every age",
     "At 0-14, because more girls are born than boys",
     "At 75+, because that is where the ratio is lowest",
     "At 60-74, because that is the first band below 100",
     "The ratio never falls below 100 in this table"],
   ans=0,
   why="The sequence runs 105, 104, 102, 99, 91 and 72, so the first value under 100 appears in the 45-59 band and the decline continues from there. A steady slide across every band, rather than a jump, is what accumulated mortality differences produce."),
]
