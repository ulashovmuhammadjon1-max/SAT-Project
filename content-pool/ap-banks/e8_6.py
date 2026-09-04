# AP ENVIRONMENTAL SCIENCE 8.6 Thermal Pollution
# CED effective Fall 2026, Unit 8 Aquatic and Terrestrial Pollution. Enduring
# understanding STB-3. Learning objective STB-3.G: describe the effects of thermal
# pollution on aquatic ecosystems. Suggested skill 1.C, explain environmental concepts,
# processes, or models in applied contexts.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-3.G.1  Thermal pollution occurs when heat released into the water produces
#              negative effects to the organisms in that ecosystem.
#   STB-3.G.2  Variations in water temperature affect the concentration of dissolved
#              oxygen because warm water does not contain as much oxygen as cold water.
#
# ON SCOPE. Topic 8.5 keys the nutrient route to low oxygen (STB-3.F.2) and topic 8.2
# keys the oxygen sag curve and the dead zone (STB-3.B.5, STB-3.B.6). Nothing here
# attributes an oxygen change to nutrients, and no item re-asks a definition from those
# topics. Every key here turns on heat.
#
# ON THE FIGURES. The bank carries no images, so every representation is a table and
# every keyed reading is recomputed in verify_e8_6.py from that table alone. No stem
# refers to a graph or a curve.
#
# NOT KEYED: no numeric temperature threshold, no named power station, no oxygen
# concentration defined as lethal. The framework states none of those.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII.
TOPIC = ("8.6", "Thermal Pollution", 8)

_T_SATURATION = dict(
    headers=["Water temperature (degrees Celsius)",
             "Dissolved oxygen the water can hold (milligrams per liter)"],
    rows=[["5", "12.8"],
          ["10", "11.3"],
          ["15", "10.1"],
          ["20", "9.1"],
          ["25", "8.2"],
          ["30", "7.5"]])

_T_SITES = dict(
    headers=["Sampling site on the river",
             "Water temperature (degrees Celsius)",
             "Dissolved oxygen (milligrams per liter)",
             "Cold water fish counted in one hour"],
    rows=[["Two kilometers above the outfall", "14.0", "10.3", "42"],
          ["At the outfall", "27.0", "7.9", "3"],
          ["One kilometer below the outfall", "24.0", "8.4", "8"],
          ["Five kilometers below the outfall", "17.0", "9.8", "31"]])

_T_TOWER = dict(
    headers=["Stage of the plant upgrade",
             "Temperature rise the discharge adds to the river (degrees Celsius)",
             "Dissolved oxygen below the outfall (milligrams per liter)",
             "Fish found dead below the outfall each year"],
    rows=[["Before the cooling tower was built", "12.0", "6.9", "900"],
          ["First year after the cooling tower", "6.0", "8.1", "310"],
          ["Fifth year after the cooling tower", "3.0", "9.4", "60"]])

_T_SEASON = dict(
    headers=["Month of sampling", "River temperature (degrees Celsius)",
             "Dissolved oxygen (milligrams per liter)"],
    rows=[["January", "4.0", "12.5"],
          ["April", "11.0", "10.9"],
          ["July", "26.0", "7.8"],
          ["October", "15.0", "10.0"]])

_T_RIVERS = dict(
    headers=["River receiving a warm discharge",
             "Temperature rise the discharge adds (degrees Celsius)",
             "Fall in dissolved oxygen below the outfall (milligrams per liter)"],
    rows=[["River J", "2.0", "0.5"],
          ["River K", "6.0", "1.6"],
          ["River L", "11.0", "3.0"]])

_T_TOLERANCE = dict(
    headers=["Species living in the river",
             "Highest water temperature the species tolerates (degrees Celsius)",
             "Individuals counted at the warm outfall in one hour"],
    rows=[["Brook trout", "20.0", "0"],
          ["Walleye", "24.0", "4"],
          ["Yellow perch", "28.0", "26"],
          ["Common carp", "33.0", "58"]])

QUESTIONS = [

 dict(q="How does the framework define thermal pollution?",
      choices=[
        "It occurs when heat released into the water produces negative effects to the "
        "organisms in that ecosystem",
        "It occurs when a body of water is enriched in nutrients from farmland",
        "It occurs when sediment washed from bare soil settles over a streambed",
        "It occurs when litter is carried into a waterway and swallowed by wildlife",
        "It occurs when a waterway is made more acidic by deposition from the air"],
      ans=0,
      why="STB-3.G.1 states that thermal pollution occurs when heat released into the "
          "water produces negative effects to the organisms in that ecosystem. Nutrient "
          "enrichment, sediment, litter and acidity are separate impacts the course "
          "treats under other statements."),

 dict(q="What relationship between water temperature and dissolved oxygen does the "
        "framework state?",
      choices=[
        "Warm water does not contain as much oxygen as cold water",
        "Warm water contains more oxygen than cold water",
        "Water temperature has no effect on how much oxygen the water contains",
        "Only salt water shows any relationship between temperature and oxygen",
        "Oxygen content depends on depth alone and not on temperature"],
      ans=0,
      why="STB-3.G.2 states that variations in water temperature affect the "
          "concentration of dissolved oxygen because warm water does not contain as much "
          "oxygen as cold water. Every rejected option denies or reverses that "
          "statement."),

 dict(q="The oxygen a sample of fresh water can hold at each temperature is shown.",
      table=_T_SATURATION,
      choices=[
        "The oxygen the water can hold falls at every step as the temperature rises",
        "The oxygen the water can hold rises at every step as the temperature rises",
        "The oxygen the water can hold is the same at every temperature listed",
        "The warmest water listed holds the most oxygen of any row",
        "The oxygen the water can hold rises and then falls as the temperature rises"],
      ans=0,
      why="Reading down the table, each higher temperature carries a smaller oxygen "
          "value than the row above it. That is the direction STB-3.G.2 states, since "
          "warm water does not contain as much oxygen as cold water."),

 dict(q="A power station draws river water for cooling and returns it much warmer. "
        "Measurements along the river are shown.",
      table=_T_SITES,
      choices=[
        "The warmest site carries the least dissolved oxygen and the fewest cold water "
        "fish, and both recover as the river cools downstream",
        "The warmest site carries the most dissolved oxygen of any site sampled",
        "The temperature is the same at every site sampled along the river",
        "The site above the outfall carries the fewest cold water fish",
        "Dissolved oxygen and fish counts are unchanged from one site to the next"],
      ans=0,
      why="The outfall row holds the highest temperature, the lowest oxygen and the "
          "smallest fish count, and the two downstream rows return toward the upstream "
          "values as the temperature falls. STB-3.G.1 makes negative effects on "
          "organisms the defining feature of thermal pollution and STB-3.G.2 supplies "
          "the oxygen link."),

 dict(q="Why does the framework treat a discharge of heated water as pollution even "
        "though heat is not a chemical substance?",
      choices=[
        "Its definition of thermal pollution turns on the negative effects the released "
        "heat has on the organisms in that ecosystem, not on whether a substance is added",
        "The framework classifies heat as a chemical substance dissolved in water",
        "Heat is only pollution when a toxic chemical is released with it",
        "The framework treats warm water as pollution only in salt water",
        "Heated water is pollution only when the discharge is illegal"],
      ans=0,
      why="STB-3.G.1 defines thermal pollution by the negative effects that released "
          "heat produces on the organisms in the ecosystem, so the harm rather than the "
          "chemistry is what makes it pollution."),

 dict(q="Results from a plant that added a cooling tower are shown.",
      table=_T_TOWER,
      choices=[
        "As the temperature rise fell, the dissolved oxygen below the outfall rose and "
        "the number of dead fish fell",
        "As the temperature rise fell, the dissolved oxygen below the outfall fell "
        "further",
        "As the temperature rise fell, the number of dead fish rose",
        "None of the three measurements changed after the cooling tower was built",
        "The temperature rise the discharge added grew larger at each stage"],
      ans=0,
      why="The temperature rise falls at every stage while the oxygen rises at every "
          "stage and the yearly death count falls at every stage. That is STB-3.G.1 and "
          "STB-3.G.2 running in reverse as the heat load is cut."),

 dict(q="Which change would most directly reduce the thermal pollution a power station "
        "causes in the river it discharges into?",
      choices=[
        "Cooling the water in a tower or pond so that it enters the river closer to the "
        "river's own temperature",
        "Adding fertilizer to the river to feed the fish that survive",
        "Releasing the same heated water through a longer pipe at the same temperature",
        "Measuring the discharge temperature more often without changing it",
        "Screening litter out of the discharge before it leaves the plant"],
      ans=0,
      why="STB-3.G.1 attributes the harm to the heat released into the water, so "
          "removing heat before discharge addresses the cause. A longer pipe, more "
          "frequent measurement and litter screens leave the heat load unchanged, and "
          "fertilizer adds a different pollutant."),

 dict(q="River measurements taken through one year are shown.",
      table=_T_SEASON,
      choices=[
        "The month with the highest river temperature carries the lowest dissolved "
        "oxygen, and the coldest month carries the highest",
        "The month with the highest river temperature carries the highest dissolved "
        "oxygen",
        "Dissolved oxygen is identical in all four months sampled",
        "The coldest month sampled carries the least dissolved oxygen",
        "The two measurements change independently of one another across the year"],
      ans=0,
      why="July is the warmest row and holds the smallest oxygen value while January is "
          "the coldest row and holds the largest, so the two quantities run in opposite "
          "directions. STB-3.G.2 states that warm water does not contain as much oxygen "
          "as cold water."),

 dict(q="A student says a heated discharge cannot harm fish because the fish can simply "
        "swim away from the warm water. Which framework point most directly complicates "
        "that reasoning?",
      choices=[
        "The heat lowers the oxygen the water can hold, so the warmed reach offers less "
        "oxygen as well as more heat",
        "The framework states that fish cannot swim in warm water at all",
        "The framework states that heat has no effect on dissolved oxygen",
        "The framework states that thermal pollution affects only plants",
        "The framework states that warm water always contains more oxygen"],
      ans=0,
      why="STB-3.G.2 ties the temperature rise to a fall in dissolved oxygen, so the "
          "warmed water is doubly unfavorable, and STB-3.G.1 defines the pollution by "
          "the negative effects on the organisms in the ecosystem."),

 dict(q="Three rivers receiving warm discharges of different sizes are compared.",
      table=_T_RIVERS,
      choices=[
        "The larger the temperature rise the discharge adds, the larger the fall in "
        "dissolved oxygen below the outfall",
        "The larger the temperature rise, the smaller the fall in dissolved oxygen",
        "All three rivers show the same fall in dissolved oxygen",
        "The river with the smallest temperature rise shows the largest oxygen fall",
        "The size of the temperature rise tells nothing about the oxygen in these data"],
      ans=0,
      why="Ranking the three rivers by temperature rise gives the same order as ranking "
          "them by the fall in dissolved oxygen. STB-3.G.2 makes the oxygen "
          "concentration depend on the water temperature."),

 dict(q="Which observation would be the strongest evidence that a discharge is causing "
        "thermal pollution as the framework defines it?",
      choices=[
        "The river below the outfall is warmer than the river above it and holds fewer "
        "of the species that lived there before",
        "The river below the outfall is warmer than the river above it",
        "The plant reports the volume of water it withdraws each day",
        "The outfall pipe is larger in diameter than it was ten years ago",
        "The river above the outfall supports several species of fish"],
      ans=0,
      why="STB-3.G.1 requires both parts, released heat and negative effects on the "
          "organisms in that ecosystem, so a temperature difference alone, a withdrawal "
          "volume, a pipe size or an upstream species list does not establish the "
          "definition."),

 dict(q="Species tolerances and counts at a warm outfall are shown.",
      table=_T_TOLERANCE,
      choices=[
        "The species with the lowest temperature tolerance are the least numerous at the "
        "outfall, and the most tolerant species is the most numerous",
        "The species with the lowest temperature tolerance are the most numerous at the "
        "outfall",
        "Every species listed is equally numerous at the outfall",
        "Tolerance and abundance are unrelated across these four species",
        "The most tolerant species listed is entirely absent from the outfall"],
      ans=0,
      why="Ordering the four species by the temperature each tolerates puts the outfall "
          "counts in the same order, from none for the least tolerant to the largest "
          "count for the most tolerant. STB-3.G.1 makes negative effects on organisms "
          "the mark of thermal pollution."),

 dict(q="Why does the framework connect the temperature of the water to the survival of "
        "aquatic organisms through dissolved oxygen?",
      choices=[
        "Temperature sets how much oxygen the water can hold, and the organisms depend on "
        "that dissolved oxygen",
        "Temperature changes the salinity of the water, which the organisms depend on",
        "Temperature changes the depth of the water, which the organisms depend on",
        "Temperature changes the acidity of the water, which the organisms depend on",
        "Temperature has no effect on the organisms once they have grown"],
      ans=0,
      why="STB-3.G.2 makes the concentration of dissolved oxygen depend on water "
          "temperature, and STB-3.G.1 makes the negative effects on organisms the "
          "definition of thermal pollution. The framework gives no salinity, depth or "
          "acidity role in this statement."),

 dict(q="A factory withdraws cold water, uses it once to absorb waste heat, and returns "
        "it to the same river. Which framework statement bears most directly on the "
        "returned water?",
      choices=[
        "Heat released into the water can produce negative effects to the organisms in "
        "that ecosystem",
        "Nutrient enrichment causes an algal bloom that microbes later digest",
        "Litter in aquatic ecosystems can create intestinal blockage in wildlife",
        "Increased sediment in waterways reduces the light reaching primary producers",
        "Bacteria convert elemental mercury into a more toxic form"],
      ans=0,
      why="The returned water carries waste heat, which is exactly the case STB-3.G.1 "
          "describes. The rejected statements belong to nutrient, litter, sediment and "
          "mercury impacts covered by other topics in this unit."),

 dict(q="Which pairing of a framework claim with its consequence is correct?",
      choices=[
        "Warm water holds less oxygen, so a heated reach can leave organisms with less "
        "oxygen than a cool reach",
        "Warm water holds more oxygen, so a heated reach is richer in oxygen than a cool "
        "reach",
        "Cold water holds less oxygen, so a cooled reach starves organisms of oxygen",
        "Temperature sets the number of species directly and does not act through oxygen",
        "Heat added to water raises its oxygen content until the water boils"],
      ans=0,
      why="STB-3.G.2 states that warm water does not contain as much oxygen as cold "
          "water, and STB-3.G.1 makes the resulting harm to organisms the definition of "
          "thermal pollution. Each rejected pairing reverses one half of that."),

 dict(q="Which measurement pair would best test whether a discharge is warming a stream "
        "enough to change its dissolved oxygen?",
      choices=[
        "Temperature and dissolved oxygen measured together above and below the outfall",
        "Dissolved oxygen measured only below the outfall on one day",
        "Temperature measured only above the outfall through the year",
        "The width of the stream channel at the outfall",
        "The number of pipes the plant operates"],
      ans=0,
      why="STB-3.G.2 links two quantities, so a test needs both measured where the "
          "discharge should have an effect and where it should not. A single downstream "
          "reading, an upstream temperature alone, channel width and pipe counts each "
          "leave one side of the relationship unmeasured."),

 dict(q="A cold water fishery disappears from a reach of river below a new discharge "
        "while warm water species increase there. How does this fit the framework's "
        "account?",
      choices=[
        "The released heat produced negative effects on the organisms that had lived "
        "there, which is what thermal pollution means",
        "The change shows that heat has no effect on aquatic organisms",
        "The change shows that dissolved oxygen rises when water is warmed",
        "The change shows that the reach was polluted by nutrients rather than heat",
        "The change shows that the species were removed by fishing"],
      ans=0,
      why="STB-3.G.1 defines thermal pollution by the negative effects released heat "
          "produces on the organisms in that ecosystem, and the loss of the resident cold "
          "water community is such an effect. Nothing in the observation points to "
          "nutrients or fishing."),

 dict(q="Which of the following best explains why the same discharge can cause more harm "
        "in late summer than in early spring?",
      choices=[
        "The river is already warm in late summer, so the added heat pushes it further "
        "and the oxygen it can hold is already lower",
        "The river holds more oxygen in late summer than in spring",
        "The discharge is colder in late summer than in spring by definition",
        "The framework states that heat has no effect during warm months",
        "Fish do not require dissolved oxygen during the summer"],
      ans=0,
      why="STB-3.G.2 makes the oxygen a river can hold fall as its temperature rises, so "
          "a warm starting temperature leaves less oxygen before the discharge is added. "
          "STB-3.G.1 then attaches the harm to organisms to that heat."),

 dict(q="A plant proposes to spread its heated discharge over a wider area of the river "
        "instead of releasing it at one point, without reducing the total heat released. "
        "What does the framework's account suggest about this?",
      choices=[
        "The total heat entering the water is unchanged, so heat is still being released "
        "into the ecosystem and can still produce negative effects",
        "Spreading the discharge removes the heat from the water entirely",
        "Spreading the discharge raises the oxygen the whole river can hold",
        "The framework states that only concentrated discharges count as pollution",
        "The framework states that a wider discharge cools the water it enters"],
      ans=0,
      why="STB-3.G.1 turns on heat released into the water and its negative effects on "
          "organisms, and spreading the same heat does not remove it. The framework "
          "offers no statement making a discharge harmless by being distributed."),

 dict(q="Which of the following is the clearest anthropogenic source of the heat the "
        "framework describes?",
      choices=[
        "Water used to carry waste heat away from an industrial process and then returned "
        "to a river",
        "Rain falling directly onto the surface of a lake",
        "Groundwater seeping into a stream from a cold spring",
        "Snowmelt entering a river in the spring",
        "Shade cast over a stream by streamside trees"],
      ans=0,
      why="STB-3.G.1 describes heat released into the water, and cooling water returned "
          "from an industrial process carries exactly that heat. Rain, cold groundwater, "
          "snowmelt and shade do not release waste heat into the water."),

 dict(q="Why is dissolved oxygen a useful measurement for monitoring thermal pollution "
        "even though the pollutant itself is heat?",
      choices=[
        "The framework ties the oxygen concentration to the water temperature, so a "
        "change in heat shows up as a change in oxygen",
        "Dissolved oxygen is the substance being released by the discharge",
        "Dissolved oxygen is easier to measure than anything else in a river",
        "The framework states that oxygen and temperature are unrelated, so oxygen is an "
        "independent check",
        "Dissolved oxygen falls only when nutrients are added to the water"],
      ans=0,
      why="STB-3.G.2 makes the concentration of dissolved oxygen depend on water "
          "temperature, so the oxygen record carries the signature of the heat. The "
          "discharge releases heat rather than oxygen, and the framework does not make "
          "the two quantities independent."),

 dict(q="An engineer claims that returning cooling water at the same temperature it was "
        "withdrawn would eliminate the thermal pollution from a plant. How does that "
        "claim relate to the framework's definition?",
      choices=[
        "It follows from the definition, because with no heat released into the water "
        "there is no basis for negative effects from heat",
        "It contradicts the definition, because the framework says any withdrawal is "
        "thermal pollution",
        "It contradicts the definition, because the framework says pollution depends on "
        "the volume of water used",
        "It is irrelevant, because the framework does not connect heat with harm",
        "It follows only if the plant also removes nutrients from the water"],
      ans=0,
      why="STB-3.G.1 makes released heat the cause and negative effects on organisms the "
          "consequence, so removing the heat removes the mechanism. The framework does "
          "not define the pollution by withdrawal or by volume."),

 dict(q="Which of the following results would most weaken a claim that a warm discharge "
        "is harming a river's fish?",
      choices=[
        "The reach below the outfall holds the same species at the same abundances as the "
        "reach above it over several years",
        "The reach below the outfall is warmer than the reach above it",
        "The plant discharges more water in summer than in winter",
        "The river below the outfall holds less dissolved oxygen than the river above it",
        "Fish are more numerous above the outfall than below it"],
      ans=0,
      why="STB-3.G.1 requires negative effects on the organisms, so an unchanged "
          "community below the outfall removes the harm the claim asserts. A temperature "
          "difference, a seasonal discharge pattern, a lower oxygen reading and fewer "
          "fish below the outfall all point the other way."),

 dict(q="Two lakes receive the same amount of waste heat, but one is much larger. Which "
        "expectation follows from the framework's account?",
      choices=[
        "The same heat spread through a larger volume of water raises its temperature "
        "less, so the change in dissolved oxygen and the effect on organisms should be "
        "smaller",
        "The larger lake must warm more because it holds more water",
        "The two lakes must warm by exactly the same amount",
        "Neither lake can warm, because lakes are too large to be heated",
        "The larger lake will lose all of its oxygen faster than the smaller lake"],
      ans=0,
      why="STB-3.G.2 makes the oxygen concentration follow the temperature, and a given "
          "quantity of heat produces a smaller temperature change in a larger volume, so "
          "the negative effects STB-3.G.1 describes should be smaller as well."),

 dict(q="Which statement correctly separates thermal pollution from eutrophication as "
        "this unit treats them?",
      choices=[
        "Thermal pollution begins with heat released into the water, while eutrophication "
        "begins with a body of water becoming enriched in nutrients",
        "Both begin with nutrients, and only the temperature of the water differs",
        "Thermal pollution begins with nutrients, while eutrophication begins with heat",
        "The two terms name the same process in different kinds of water",
        "Thermal pollution refers to salt water and eutrophication to fresh water"],
      ans=0,
      why="STB-3.G.1 makes released heat the cause of thermal pollution, while STB-3.F.1 "
          "makes nutrient enrichment the cause of eutrophication. The two lead to low "
          "oxygen by different routes and neither is defined by the type of water."),

 dict(q="A monitoring program finds that the oxygen deficit below an outfall is largest "
        "on the hottest days of the year. Which explanation is best supported by the "
        "framework?",
      choices=[
        "The river is warmest on those days, so it can hold the least oxygen, and the "
        "discharge adds heat on top of that",
        "The discharge releases oxygen on cool days and consumes it on hot days",
        "The river holds the most oxygen on the hottest days",
        "Heat has no relationship to oxygen, so the pattern must be a measurement error",
        "The framework states that oxygen deficits occur only in winter"],
      ans=0,
      why="STB-3.G.2 makes the oxygen the water can hold fall as temperature rises, so "
          "the hottest days start from the lowest oxygen and the added heat deepens the "
          "deficit further."),

 dict(q="Which of the following would best show that a stream's low oxygen comes from "
        "heat rather than from another cause?",
      choices=[
        "The oxygen falls exactly where and when the water is warmed by the discharge and "
        "recovers as the water cools downstream",
        "The oxygen is low at every site in the watershed in every season",
        "The stream carries visible litter near the outfall",
        "The stream drains an area with many farms",
        "The stream is deeper below the outfall than above it"],
      ans=0,
      why="A pattern that tracks the warming in both space and time is what ties the "
          "oxygen change to the heat STB-3.G.2 describes. Uniformly low oxygen, litter, "
          "farmland and a depth difference point to other causes or to none."),

 dict(q="Why does the framework state the temperature and oxygen relationship as part of "
        "a topic about pollution rather than as a fact about water alone?",
      choices=[
        "Because the relationship is what turns released heat into a negative effect on "
        "the organisms living in the water",
        "Because the relationship applies only to water that has been polluted",
        "Because the relationship is reversed in unpolluted water",
        "Because the framework treats dissolved oxygen as a pollutant",
        "Because the relationship holds only in water that has been heated by people"],
      ans=0,
      why="STB-3.G.2 supplies the mechanism that STB-3.G.1's definition depends on: the "
          "heat lowers the oxygen, and the lowered oxygen is one of the negative effects "
          "on organisms. The relationship itself is a property of water and is not "
          "confined to polluted or heated water."),

 dict(q="A regulator must choose one limit to place on a plant's discharge to protect "
        "the river's aquatic life from thermal pollution. Which limit follows most "
        "directly from the framework?",
      choices=[
        "A limit on how much the discharge may raise the temperature of the receiving "
        "water",
        "A limit on the number of employees working at the plant",
        "A limit on the color of the water leaving the plant",
        "A limit on the depth of the pipe carrying the discharge",
        "A limit on the hours of daylight during which the plant may operate"],
      ans=0,
      why="STB-3.G.1 attributes the harm to heat released into the water, so a cap on "
          "the temperature rise addresses the cause directly. Staffing, color, pipe depth "
          "and operating hours do not bound the heat delivered."),

 dict(q="Which summary best captures this topic?",
      choices=[
        "Heat released into a waterway harms the organisms living there, and part of the "
        "harm comes through dissolved oxygen, because warm water cannot hold as much "
        "oxygen as cold water",
        "Heat released into a waterway raises its dissolved oxygen and benefits the "
        "organisms living there",
        "Thermal pollution is caused by fertilizer runoff and is measured as a nutrient "
        "concentration",
        "Water temperature and dissolved oxygen are unrelated, so heated discharges are "
        "harmless",
        "Only very cold discharges harm aquatic organisms, and warm discharges are "
        "regulated for other reasons"],
      ans=0,
      why="The keyed summary joins STB-3.G.1, which makes negative effects on organisms "
          "the definition, with STB-3.G.2, which supplies the oxygen mechanism. Each "
          "rejected summary reverses the oxygen relationship or replaces heat with a "
          "different pollutant."),
]
