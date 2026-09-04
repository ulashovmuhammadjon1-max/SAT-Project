# AP ENVIRONMENTAL SCIENCE 9.1 Stratospheric Ozone Depletion
# CED effective Fall 2026, Unit 9 Global Change. Enduring understanding STB-4, local and
# regional human activities can have impacts at the global level. Learning objective
# STB-4.A: explain the importance of stratospheric ozone to life on Earth. Suggested
# skill 1.A, describe environmental concepts and processes.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-4.A.1  The stratospheric ozone layer is important to the evolution of life on
#              Earth and the continued health and survival of life on Earth.
#   STB-4.A.2  Stratospheric ozone depletion is caused by anthropogenic factors, such as
#              chlorofluorocarbons (CFCs), and natural factors, such as the melting of ice
#              crystals in the atmosphere at the beginning of the Antarctic spring.
#   STB-4.A.3  A decrease in stratospheric ozone increases the UV rays that reach the
#              Earth's surface. Exposure to UV rays can lead to skin cancer and cataracts
#              in humans.
#
# THE LAYER SWAP IS THE CENTRAL ERROR OF THIS TOPIC. Here the ozone is STRATOSPHERIC and
# the change is a DECREASE, and its human consequences are skin cancer and cataracts.
# Topic 8.14 is about ELEVATED ozone in the TROPOSPHERE, near the ground, whose stated
# consequences are respiratory problems and lung function (EIN-3.C.4). Items 8, 14 and 17
# invite exactly that confusion and their anchors in verify_e9_1.py carry BOTH the layer
# and the direction of the change, so an anchor cannot match the swapped option.
#
# ON SCOPE. Topic 9.2 keys the substitutes for CFCs (STB-4.B.1); nothing here keys a
# replacement chemical. Topic 7.2 keys how ozone forms near the ground; nothing here keys
# that formation.
#
# ON THE FIGURES. The bank carries no images, so every representation is a table and
# every keyed reading is recomputed in verify_e9_1.py from that table alone.
#
# NOT KEYED: no treaty, no year, no ozone concentration described as safe, no other
# health effect and no cause the framework does not name. The framework states none.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII.
TOPIC = ("9.1", "Stratospheric Ozone Depletion", 9)

_T_UV = dict(
    headers=["Ozone in the column above the site (Dobson units)",
             "Ultraviolet radiation measured at the surface (index units)"],
    rows=[["400", "6.0"],
          ["340", "8.0"],
          ["280", "11"],
          ["220", "15"]])

_T_CFC = dict(
    headers=["Period of the record",
             "Emissions of chlorofluorocarbons (thousands of tons per year)",
             "Lowest springtime ozone column measured over the pole (Dobson units)"],
    rows=[["Period 1", "30", "330"],
          ["Period 2", "180", "250"],
          ["Period 3", "340", "160"]])

_T_SEASON = dict(
    headers=["Part of the year over Antarctica",
             "Ozone column measured (Dobson units)"],
    rows=[["Late winter", "290"],
          ["Beginning of spring", "150"],
          ["Late spring", "210"],
          ["Summer", "300"]])

_T_LATITUDE = dict(
    headers=["Region studied", "Average yearly ultraviolet exposure (index units)",
             "Skin cancer cases per hundred thousand people",
             "Cataract cases per hundred thousand people"],
    rows=[["Region 1", "4.0", "22", "310"],
          ["Region 2", "7.0", "48", "460"],
          ["Region 3", "11", "96", "690"]])

_T_LAYERS = dict(
    headers=["Quantity measured", "Value in the earlier record", "Value in the later record"],
    rows=[["Ozone column high in the stratosphere over the pole (Dobson units)",
           "320", "150"],
          ["Ozone near the ground in a large city (parts per billion)", "40", "95"]])

_T_CAUSES = dict(
    headers=["Contribution to one year's springtime ozone loss",
             "Share of the loss attributed to it (percent)"],
    rows=[["Reactions involving chlorofluorocarbons released by people", "78"],
          ["Processes on ice crystals in the polar atmosphere at the beginning of spring",
           "22"]])

QUESTIONS = [

 dict(q="Why does the framework say the stratospheric ozone layer matters?",
      choices=[
        "It is important to the evolution of life on Earth and to the continued health and "
        "survival of life on Earth",
        "It supplies the oxygen that organisms breathe at the surface",
        "It provides the surface temperature necessary for life to exist",
        "It carries heat from the equator toward the poles",
        "It is the source of the rain that falls on land"],
      ans=0,
      why="STB-4.A.1 states that the stratospheric ozone layer is important to the "
          "evolution of life on Earth and the continued health and survival of life on "
          "Earth. Breathable oxygen, the surface temperature, heat transport and rainfall "
          "are attributed to other processes in the course."),

 dict(q="Which anthropogenic cause of stratospheric ozone depletion does the framework "
        "name?",
      choices=[
        "Chlorofluorocarbons",
        "Nitrate fertilizer washed from farmland",
        "Asbestos fibers released from old buildings",
        "Untreated sewage discharged to rivers",
        "Heat released into rivers by power stations"],
      ans=0,
      why="STB-4.A.2 states that stratospheric ozone depletion is caused by anthropogenic "
          "factors, such as chlorofluorocarbons. Fertilizer, asbestos, sewage and waste "
          "heat are pollutants treated in unit 8 and are not named here."),

 dict(q="Ozone overhead and ultraviolet radiation at the ground were measured together.",
      table=_T_UV,
      choices=[
        "The less ozone in the column above the site, the more ultraviolet radiation "
        "reached the surface",
        "The less ozone in the column above the site, the less ultraviolet radiation "
        "reached the surface",
        "The ultraviolet radiation at the surface was the same at every ozone value",
        "The largest ozone column carried the most ultraviolet radiation at the surface",
        "Ozone overhead and ultraviolet radiation at the ground are unrelated in these "
        "data"],
      ans=0,
      why="Ordering the rows by the ozone column gives the reverse of the order by "
          "ultraviolet radiation measured at the surface. STB-4.A.3 states that a decrease "
          "in stratospheric ozone increases the ultraviolet rays that reach the surface."),

 dict(q="Which natural factor in stratospheric ozone depletion does the framework name?",
      choices=[
        "The melting of ice crystals in the atmosphere at the beginning of the Antarctic "
        "spring",
        "The eruption of volcanoes along the mid ocean ridges",
        "The seasonal migration of birds across the equator",
        "The decay of organic matter in tropical soils",
        "The evaporation of seawater from the tropical ocean"],
      ans=0,
      why="STB-4.A.2 names the melting of ice crystals in the atmosphere at the beginning "
          "of the Antarctic spring as its example of a natural factor. Eruptions, "
          "migration, decay and evaporation appear nowhere in this statement."),

 dict(q="What does the framework say a decrease in stratospheric ozone does?",
      choices=[
        "It increases the ultraviolet rays that reach the surface of the Earth",
        "It decreases the ultraviolet rays that reach the surface of the Earth",
        "It raises the amount of ozone measured near the ground",
        "It lowers the surface temperature of the Earth",
        "It has no measurable effect at the surface"],
      ans=0,
      why="STB-4.A.3 states that a decrease in stratospheric ozone increases the "
          "ultraviolet rays that reach the Earth's surface. Each rejected option reverses "
          "that, substitutes a different quantity, or denies the effect."),

 dict(q="Emissions and springtime ozone measurements were recorded over three periods.",
      table=_T_CFC,
      choices=[
        "As the emissions of chlorofluorocarbons rose across the periods, the lowest "
        "springtime ozone column fell",
        "As the emissions of chlorofluorocarbons rose, the lowest springtime ozone column "
        "rose with them",
        "The ozone column was the same in all three periods",
        "The period with the largest emissions had the largest ozone column",
        "Emissions fell across the three periods"],
      ans=0,
      why="The emissions column rises at every step while the ozone column falls at every "
          "step. STB-4.A.2 names chlorofluorocarbons as an anthropogenic cause of "
          "stratospheric ozone depletion."),

 dict(q="Which human health effects does the framework attribute to exposure to the "
        "ultraviolet rays that reach the surface?",
      choices=[
        "Skin cancer and cataracts",
        "Respiratory problems and reduced lung function",
        "Dysentery and other intestinal illness",
        "Mesothelioma and other cancers of the chest lining",
        "Damage to the reproductive and circulatory systems from a biomagnified pollutant"],
      ans=0,
      why="STB-4.A.3 states that exposure to ultraviolet rays can lead to skin cancer and "
          "cataracts in humans. Respiratory effects belong to elevated tropospheric ozone "
          "under EIN-3.C.4, and the remaining options belong to other statements in "
          "unit 8."),

 dict(q="Which layer of the atmosphere holds the ozone this topic is about, and is that "
        "ozone increasing or decreasing in the framework's account?",
      choices=[
        "The stratosphere, high above the ground, where the ozone is being depleted",
        "The troposphere, near the ground, where the ozone is building up",
        "The stratosphere, high above the ground, where the ozone is building up",
        "The troposphere, near the ground, where the ozone is being depleted",
        "Both layers at once, with the ozone changing in the same direction in each"],
      ans=0,
      why="STB-4.A.2 and STB-4.A.3 concern the depletion of ozone in the stratosphere. "
          "EIN-3.C.4 concerns elevated ozone in the troposphere near the ground, so the "
          "layer and the direction of change both differ between the two statements."),

 dict(q="Ozone over Antarctica was measured through the year.",
      table=_T_SEASON,
      choices=[
        "The smallest ozone column of the year was measured at the beginning of spring",
        "The smallest ozone column of the year was measured in summer",
        "The ozone column was the same throughout the year",
        "The largest ozone column of the year was measured at the beginning of spring",
        "The ozone column fell steadily from late winter through summer"],
      ans=0,
      why="The row for the beginning of spring carries the smallest value in the table and "
          "the values rise again afterward. STB-4.A.2 names processes involving ice "
          "crystals in the atmosphere at the beginning of the Antarctic spring among the "
          "factors in ozone depletion."),

 dict(q="Why does less stratospheric ozone mean more ultraviolet radiation at the surface?",
      choices=[
        "The ozone in that layer stands between the Sun and the surface, so less of it "
        "leaves more of those rays to reach the ground",
        "The ozone in that layer produces ultraviolet rays, so less of it produces fewer",
        "The ozone in that layer reflects heat back to the surface",
        "The ozone in that layer is what people breathe at the surface",
        "The ozone in that layer determines how much rain falls"],
      ans=0,
      why="STB-4.A.3 states that a decrease in stratospheric ozone increases the "
          "ultraviolet rays reaching the Earth's surface, so the layer stands between the "
          "source and the ground. The framework does not make stratospheric ozone a source "
          "of ultraviolet rays, a reflector of heat, breathable, or a control on "
          "rainfall."),

 dict(q="Which of the following is NOT a cause of stratospheric ozone depletion the "
        "framework names?",
      choices=[
        "Sediment washed into rivers from bare farmland",
        "Chlorofluorocarbons released by human activity",
        "Anthropogenic factors in general",
        "Natural factors in general",
        "Processes involving ice crystals at the beginning of the Antarctic spring"],
      ans=0,
      why="STB-4.A.2 names anthropogenic factors such as chlorofluorocarbons and natural "
          "factors such as the melting of ice crystals at the beginning of the Antarctic "
          "spring. Sediment in rivers belongs to STB-3.B.9 and has no role in this "
          "statement."),

 dict(q="A country prohibits the manufacture of chlorofluorocarbons. Which framework "
        "statement makes that a response to stratospheric ozone depletion?",
      choices=[
        "Stratospheric ozone depletion is caused by anthropogenic factors, such as "
        "chlorofluorocarbons",
        "The stratospheric ozone layer is important to the evolution of life on Earth",
        "A decrease in stratospheric ozone increases the ultraviolet rays reaching the "
        "surface",
        "Exposure to ultraviolet rays can lead to skin cancer and cataracts in humans",
        "Natural factors also contribute to stratospheric ozone depletion"],
      ans=0,
      why="STB-4.A.2 identifies chlorofluorocarbons as an anthropogenic cause, so removing "
          "them addresses a stated cause. The rejected statements describe why the layer "
          "matters, what a decrease does, and what the resulting exposure can lead to."),

 dict(q="Three regions differing in ultraviolet exposure were compared.",
      table=_T_LATITUDE,
      choices=[
        "The region with the highest ultraviolet exposure carries the highest rates of both "
        "conditions the framework attributes to those rays",
        "The region with the lowest ultraviolet exposure carries the highest rates of both "
        "conditions",
        "The three regions carry the same rates of both conditions",
        "Ultraviolet exposure rises with one condition and falls with the other across the "
        "regions",
        "Ultraviolet exposure and these conditions are unrelated across the regions"],
      ans=0,
      why="Ranking the regions by ultraviolet exposure gives the same order as ranking them "
          "by each of the two case rates. STB-4.A.3 states that exposure to ultraviolet "
          "rays can lead to skin cancer and cataracts in humans."),

 dict(q="A student writes that ozone depletion causes asthma and other breathing problems. "
        "What is the clearest correction from the framework?",
      choices=[
        "Depletion of ozone in the stratosphere is linked to skin cancer and cataracts, "
        "while breathing problems are linked to elevated ozone near the ground",
        "Depletion of ozone in the stratosphere is linked to breathing problems, and the "
        "student is correct",
        "Elevated ozone near the ground is linked to skin cancer and cataracts",
        "Neither layer of ozone has any effect on human health",
        "Both layers of ozone produce exactly the same health effects"],
      ans=0,
      why="STB-4.A.3 attaches skin cancer and cataracts to the increased ultraviolet rays "
          "that follow a decrease in stratospheric ozone, while EIN-3.C.4 attaches "
          "respiratory problems and lung function to elevated tropospheric ozone. The two "
          "statements differ in both the layer and the direction of change."),

 dict(q="Why does the framework mention both the evolution of life and its continued "
        "health and survival?",
      choices=[
        "The layer mattered while life was developing and it continues to matter to life "
        "living now",
        "The layer mattered only in the past and no longer affects living organisms",
        "The layer matters only to organisms that have not yet evolved",
        "The layer matters only to humans and not to other organisms",
        "The two phrases are alternative names for the same period of time"],
      ans=0,
      why="STB-4.A.1 states that the stratospheric ozone layer is important to the "
          "evolution of life on Earth and the continued health and survival of life on "
          "Earth, which covers both the past and the present."),

 dict(q="Which measurement would most directly show that stratospheric ozone above a site "
        "has been depleted?",
      choices=[
        "The amount of ozone in the column of atmosphere above that site",
        "The amount of ozone measured in the air people breathe at that site",
        "The temperature of the air at the surface of that site",
        "The amount of rain that falls at that site each year",
        "The number of people living within a day's travel of that site"],
      ans=0,
      why="STB-4.A.2 and STB-4.A.3 concern ozone in the stratosphere, so the overhead "
          "column is the quantity that shows its depletion. Ozone measured in breathing air "
          "is the tropospheric ozone of EIN-3.C.4, and temperature, rainfall and population "
          "measure something else entirely."),

 dict(q="Two ozone measurements from different parts of the atmosphere were compared "
        "between an earlier and a later record.",
      table=_T_LAYERS,
      choices=[
        "The ozone high in the stratosphere fell while the ozone near the ground rose, so "
        "the two changed in opposite directions",
        "Both measurements fell between the two records",
        "Both measurements rose between the two records",
        "The ozone high in the stratosphere rose while the ozone near the ground fell",
        "Neither measurement changed between the two records"],
      ans=0,
      why="The stratospheric row falls between the two records while the ground level row "
          "rises. STB-4.A.3 concerns a decrease in stratospheric ozone and EIN-3.C.4 "
          "concerns elevated ozone near the ground, so the two statements describe "
          "opposite changes in different layers."),

 dict(q="Which study design would best test the framework's claim about ozone and "
        "ultraviolet radiation?",
      choices=[
        "Measuring the overhead ozone column and the ultraviolet radiation at the surface "
        "at the same site on many days",
        "Measuring the overhead ozone column once at a single site",
        "Measuring the ultraviolet radiation at the surface without measuring ozone",
        "Counting the number of sunny days in a year at the site",
        "Measuring the ozone in the air people breathe at the site"],
      ans=0,
      why="STB-4.A.3 links two quantities, the stratospheric ozone and the ultraviolet "
          "rays reaching the surface, so both must be measured together and allowed to "
          "vary. Ground level ozone belongs to a different statement."),

 dict(q="Why does the framework attach its natural factor to the beginning of the "
        "Antarctic spring in particular?",
      choices=[
        "That is when it says ice crystals in the atmosphere melt, which is the natural "
        "factor it names",
        "That is when chlorofluorocarbons are manufactured each year",
        "That is when the Antarctic receives the least sunlight of the year",
        "That is when the ozone layer is thickest over the Antarctic",
        "That is when the Antarctic is warmest at the surface"],
      ans=0,
      why="STB-4.A.2 names the melting of ice crystals in the atmosphere at the beginning "
          "of the Antarctic spring as its natural factor, so the timing belongs to that "
          "process rather than to manufacturing or to sunlight."),

 dict(q="Which pairing of a cause with the framework's own category is correct?",
      choices=[
        "Chlorofluorocarbons, paired with the anthropogenic factors",
        "Chlorofluorocarbons, paired with the natural factors",
        "The melting of atmospheric ice crystals, paired with the anthropogenic factors",
        "The melting of atmospheric ice crystals, paired with a cause the framework does "
        "not recognize",
        "Both causes, paired with a single category that the framework does not divide"],
      ans=0,
      why="STB-4.A.2 gives chlorofluorocarbons as an example of an anthropogenic factor and "
          "the melting of ice crystals at the beginning of the Antarctic spring as an "
          "example of a natural factor, so the framework does divide the causes into two "
          "categories."),

 dict(q="One year's springtime ozone loss was divided between two contributions.",
      table=_T_CAUSES,
      choices=[
        "Both a contribution from chemicals people released and a contribution from a "
        "natural polar process are present, and together they account for the whole loss",
        "Only the contribution from chemicals people released is present",
        "Only the natural polar contribution is present",
        "Neither contribution accounts for any of the loss",
        "The two contributions together account for less than half of the loss"],
      ans=0,
      why="Both rows carry a positive share and the two shares sum to the whole. STB-4.A.2 "
          "states that stratospheric ozone depletion is caused by anthropogenic factors "
          "such as chlorofluorocarbons and natural factors such as the melting of ice "
          "crystals at the beginning of the Antarctic spring."),

 dict(q="Which evidence would most strengthen the claim that increased ultraviolet exposure "
        "raises the rate of the eye condition the framework names?",
      choices=[
        "Populations with higher measured ultraviolet exposure show higher rates of "
        "cataracts than populations with lower exposure",
        "Populations with higher measured ultraviolet exposure live at higher elevations",
        "The ultraviolet index is reported daily in the news",
        "Cataracts have been recorded in medical records for many years",
        "Ultraviolet radiation can be measured with an instrument"],
      ans=0,
      why="STB-4.A.3 states that exposure to ultraviolet rays can lead to skin cancer and "
          "cataracts in humans, so a comparison of exposure against the condition's rate is "
          "what tests it. Elevation, reporting, record keeping and measurability do not."),

 dict(q="Why does the framework name both anthropogenic and natural factors rather than "
        "only one?",
      choices=[
        "Both kinds of factor contribute to the depletion it describes, so naming only one "
        "would leave out part of the cause",
        "Only the natural factors matter and the anthropogenic ones are listed by mistake",
        "Only the anthropogenic factors matter and the natural ones are listed by mistake",
        "The two kinds of factor are different names for the same process",
        "Naming two kinds of factor shows that neither one has any effect"],
      ans=0,
      why="STB-4.A.2 gives an example of each kind, which places both within the stated "
          "cause of stratospheric ozone depletion. Nothing in the framework subordinates "
          "one to the other or treats them as one process."),

 dict(q="What kind of substance are the chlorofluorocarbons the framework names?",
      choices=[
        "Chemicals released by human activity that the framework identifies as an "
        "anthropogenic cause of stratospheric ozone depletion",
        "Gases produced naturally in the polar atmosphere each spring",
        "Minerals dissolved in seawater that reach the atmosphere by evaporation",
        "Bacteria that convert one form of a pollutant to another",
        "Particles released by the erosion of exposed soil"],
      ans=0,
      why="STB-4.A.2 names chlorofluorocarbons as an example of the anthropogenic factors "
          "that cause stratospheric ozone depletion, so they are of human origin rather "
          "than natural, mineral, biological or geologic."),

 dict(q="A region with a persistently thin ozone column reports rising rates of a "
        "condition of the eye. Which framework statement bears on that report?",
      choices=[
        "A decrease in stratospheric ozone increases the ultraviolet rays reaching the "
        "surface, and exposure to those rays can lead to cataracts",
        "Elevated ozone near the ground can affect respiratory problems and lung function",
        "The stratospheric ozone layer is important to the evolution of life on Earth",
        "Natural factors contribute to stratospheric ozone depletion",
        "Chlorofluorocarbons are an anthropogenic cause of stratospheric ozone depletion"],
      ans=0,
      why="STB-4.A.3 joins the increase in ultraviolet rays that follows a decrease in "
          "stratospheric ozone to skin cancer and cataracts in humans, which is the chain "
          "the report describes. The rejected statements name causes or a different layer."),

 dict(q="A long record shows the ozone column above a site rising back toward its earlier "
        "values. What does the framework's account predict for ultraviolet radiation at "
        "that site?",
      choices=[
        "Less ultraviolet radiation should reach the surface as the ozone column recovers",
        "More ultraviolet radiation should reach the surface as the ozone column recovers",
        "The ultraviolet radiation at the surface should be unaffected by the ozone column",
        "The ozone near the ground should fall as the ozone column recovers",
        "The surface temperature should rise as the ozone column recovers"],
      ans=0,
      why="STB-4.A.3 states that a decrease in stratospheric ozone increases the "
          "ultraviolet rays reaching the surface, so a recovery in the column works in the "
          "opposite direction. The framework attaches no temperature or ground level ozone "
          "consequence to the column."),

 dict(q="Which claim about this topic is NOT supported by the framework?",
      choices=[
        "Ozone depletion in the stratosphere is caused only by natural processes",
        "Ozone depletion in the stratosphere has anthropogenic causes",
        "A thinner ozone layer lets more ultraviolet radiation reach the surface",
        "Ultraviolet exposure is linked to skin cancer in humans",
        "The stratospheric ozone layer matters to the survival of life on Earth"],
      ans=0,
      why="STB-4.A.2 names anthropogenic factors such as chlorofluorocarbons alongside "
          "natural factors, so attributing the depletion to natural processes alone "
          "contradicts it. The four rejected claims restate STB-4.A.1, STB-4.A.2 and "
          "STB-4.A.3."),

 dict(q="How does the framework connect the ozone layer to the survival of organisms "
        "generally rather than to humans alone?",
      choices=[
        "It states that the layer is important to the continued health and survival of "
        "life on Earth, and names skin cancer and cataracts as effects in humans "
        "specifically",
        "It states that only humans are affected by any change in the layer",
        "It states that only organisms in the ocean are affected by the layer",
        "It states that the layer has no relationship to living organisms",
        "It states that the layer affects organisms only through the temperature at the "
        "surface"],
      ans=0,
      why="STB-4.A.1 speaks of life on Earth, while STB-4.A.3 names skin cancer and "
          "cataracts in humans, so the framework makes a general claim and a specific human "
          "one."),

 dict(q="Which sequence describes the process this topic asks students to explain?",
      choices=[
        "Ozone in the stratosphere is depleted, more ultraviolet radiation reaches the "
        "surface, and exposure to those rays can lead to skin cancer and cataracts",
        "Ozone builds up near the ground, less ultraviolet radiation reaches the surface, "
        "and breathing improves",
        "Ultraviolet radiation increases first, which then destroys the ozone layer, which "
        "then cools the surface",
        "Skin cancer rates rise first, which then thins the ozone layer",
        "Ozone in the stratosphere increases, more ultraviolet radiation reaches the "
        "surface, and cataracts become more common"],
      ans=0,
      why="STB-4.A.2 supplies the depletion and its causes, and STB-4.A.3 supplies the "
          "increase in ultraviolet rays reaching the surface and the health effects that "
          "can follow, in that order."),

 dict(q="Which summary best captures this topic?",
      choices=[
        "The ozone layer high in the stratosphere matters to the evolution and survival of "
        "life, it is depleted by human released chlorofluorocarbons and by a natural polar "
        "process, and its depletion lets more ultraviolet radiation reach the surface, "
        "where exposure can cause skin cancer and cataracts",
        "The ozone near the ground protects life from ultraviolet radiation and its "
        "depletion causes breathing problems",
        "Ozone depletion has no human causes and no consequences for human health",
        "A thinner ozone layer blocks more ultraviolet radiation from reaching the surface",
        "The ozone layer matters only to the evolution of life in the past and not to life "
        "living now"],
      ans=0,
      why="Each clause of the keyed summary is one of STB-4.A.1, STB-4.A.2 and STB-4.A.3. "
          "Every rejected summary moves the ozone to the wrong layer, denies a stated cause "
          "or effect, reverses the direction of the ultraviolet change, or drops the "
          "framework's claim about life living now."),
]
