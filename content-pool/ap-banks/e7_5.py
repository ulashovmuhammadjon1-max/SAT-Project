# AP ENVIRONMENTAL SCIENCE 7.5 Indoor Air Pollutants
# CED effective Fall 2026, Unit 7 Atmospheric Pollution. Enduring understanding STB-2.
# Learning objectives STB-2.E, identify indoor air pollutants, and STB-2.F, describe
# the effects of indoor air pollutants. Suggested skill 5.C, explain patterns and
# trends in data to draw conclusions.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-2.E.1  Carbon monoxide is an indoor air pollutant that is classified as an
#              asphyxiant.
#   STB-2.E.2  Indoor air pollutants that are classified as particulates include
#              asbestos, dust, and smoke.
#   STB-2.E.3  Indoor air pollutants can come from natural sources, human-made
#              sources, and combustion.
#   STB-2.E.4  Common natural source indoor air pollutants include radon, mold, and
#              dust.
#   STB-2.E.5  Common human-made indoor air pollutants include insulation, Volatile
#              Organic Compounds (VOCs) from furniture, paneling and carpets;
#              formaldehyde from building materials, furniture, upholstery, and
#              carpeting; and lead from paints.
#   STB-2.E.6  Common combustion air pollutants include carbon monoxide, nitrogen
#              oxides, sulfur dioxide, particulates, and tobacco smoke.
#   STB-2.E.7  Radon-222 is a naturally occurring radioactive gas that is produced by
#              the decay of uranium found in some rocks and soils.
#   STB-2.F.1  Radon gas can infiltrate homes as it moves up through the soil and
#              enters homes via the basement or cracks in the walls or foundation. It
#              is also dissolved in groundwater that enters homes through a well.
#   STB-2.F.2  Exposure to radon gas can lead to radon-induced lung cancer, which is
#              the second leading cause of lung cancer in America.
#
# ON THE THREE CATEGORIES. STB-2.E.3 gives natural, human-made and combustion as the
# three kinds of indoor source, and STB-2.E.4 to STB-2.E.6 populate them. Dust appears
# in two of the framework's own lists -- as a particulate in STB-2.E.2 and as a natural
# source pollutant in STB-2.E.4 -- so no item here asks a student to assign dust to one
# category to the exclusion of the other.
#
# ON WHAT IS NOT KEYED. The framework gives no action level, no measured
# concentration, no ventilation rate and no radon half-life, so none is keyed. The
# only quantity it states is that radon-induced lung cancer is the second leading
# cause of lung cancer in America. Nothing here names a product, a brand or a
# regulation.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII: export_units.py does not typeset
# ENV_SCI.
TOPIC = ("7.5", "Indoor Air Pollutants", 7)

_T_FLOORS = dict(
    headers=["Level of the house", "Height above the soil surface (meters)",
             "Radon measured (picocuries per liter)"],
    rows=[["Basement", "0", "8.4"],
          ["Ground floor", "3", "4.1"],
          ["Second floor", "6", "1.9"],
          ["Attic", "9", "0.8"]])

_T_SEAL = dict(
    headers=["House", "Foundation cracks sealed and basement vented",
             "Radon measured in the basement (picocuries per liter)"],
    rows=[["House 1", "no", "9.0"],
          ["House 2", "no", "7.6"],
          ["House 3", "yes", "2.1"],
          ["House 4", "yes", "1.4"]])

_T_BEDROCK = dict(
    headers=["Neighborhood", "Uranium in the underlying rock (parts per million)",
             "Average indoor radon (picocuries per liter)"],
    rows=[["Neighborhood P", "1", "0.9"],
          ["Neighborhood Q", "3", "2.6"],
          ["Neighborhood R", "6", "5.0"],
          ["Neighborhood S", "12", "9.7"]])

_T_HEATER = dict(
    headers=["Condition in a closed room",
             "Carbon monoxide after two hours (parts per million)"],
    rows=[["Unvented fuel-burning heater running", "68"],
          ["Same heater running with the flue open to the outside", "9"],
          ["Heater switched off", "2"]])

_T_NEW = dict(
    headers=["Age of the pressed-wood furniture in the room",
             "Formaldehyde measured indoors (parts per billion)"],
    rows=[["New this week", "94"],
          ["One year old", "42"],
          ["Five years old", "18"],
          ["Twelve years old", "7"]])

_T_SMOKE = dict(
    headers=["Room", "Tobacco smoked indoors",
             "Fine particulates measured (micrograms per cubic meter)"],
    rows=[["Room 1", "yes", "180"],
          ["Room 2", "yes", "142"],
          ["Room 3", "no", "21"],
          ["Room 4", "no", "16"]])

_T_WELL = dict(
    headers=["Home water supply", "Radon in the water (picocuries per liter)",
             "Radon in the bathroom air after showering (picocuries per liter)"],
    rows=[["Private well", "4,000", "6.2"],
          ["Treated municipal supply", "120", "0.7"]])

QUESTIONS = [

 dict(q="Carbon monoxide is classified as an asphyxiant when it is treated as an indoor "
        "air pollutant. Which description matches that classification?",
      choices=[
        "It interferes with the delivery of oxygen the body needs",
        "It burns the skin on contact with a heated surface",
        "It is a solid particle that lodges in the lung tissue",
        "It is a radioactive gas that decays inside the lungs",
        "It causes irritation of the eyes but has no other effect"],
      ans=0,
      why="The framework classifies carbon monoxide as an asphyxiant, and an asphyxiant "
          "acts by depriving the body of the oxygen it needs. It is a gas rather than a "
          "particle, it is not radioactive, and the framework does not describe it as a "
          "skin or eye irritant."),

 dict(q="Which indoor air pollutants does the framework classify as particulates?",
      choices=[
        "Asbestos, dust, and smoke",
        "Carbon monoxide, radon, and formaldehyde",
        "Nitrogen gas, oxygen, and argon",
        "Ozone, nitric acid, and photochemical smog",
        "Lead dissolved in drinking water and in soil"],
      ans=0,
      why="The framework states that indoor air pollutants classified as particulates "
          "include asbestos, dust, and smoke. Carbon monoxide, radon and formaldehyde "
          "are gases, the third list is clean air, and the fourth belongs to outdoor "
          "atmospheric chemistry."),

 dict(q="Which three kinds of source does the framework give for indoor air pollutants?",
      choices=[
        "Natural sources, human-made sources, and combustion",
        "Agricultural sources, marine sources, and volcanic sources",
        "Stratospheric sources, tropospheric sources, and oceanic sources",
        "Point sources, nonpoint sources, and mobile sources",
        "Primary sources and secondary sources only"],
      ans=0,
      why="The framework states that indoor air pollutants can come from natural "
          "sources, human-made sources, and combustion, and it populates each of those "
          "three categories in the statements that follow. The other groupings belong to "
          "different parts of the course or are not used for indoor air at all."),

 dict(q="Which group lists only pollutants the framework gives as common indoor "
        "pollutants from natural sources?",
      choices=[
        "Radon, mold, and dust",
        "Formaldehyde, insulation, and lead paint",
        "Carbon monoxide, nitrogen oxides, and tobacco smoke",
        "Volatile organic compounds from carpets and paneling",
        "Sulfur dioxide from a coal-fired power station"],
      ans=0,
      why="The framework names radon, mold and dust as common natural source indoor air "
          "pollutants. The second and fourth lists are its human-made examples, and the "
          "third and fifth are combustion products."),

 dict(q="Which group lists only indoor pollutants the framework attributes to human-made "
        "sources?",
      choices=[
        "Insulation, formaldehyde from building materials, and lead from paints",
        "Radon, mold, and dust",
        "Carbon monoxide, sulfur dioxide, and tobacco smoke",
        "Uranium in bedrock beneath the foundation",
        "Groundwater entering a home through a well"],
      ans=0,
      why="The framework's human-made list is insulation, volatile organic compounds "
          "from furniture, paneling and carpets, formaldehyde from building materials "
          "and furnishings, and lead from paints. The second list is its natural "
          "examples, the third is combustion, and the last two are the setting for radon "
          "rather than human-made pollutants."),

 dict(q="Which group lists only pollutants the framework gives as common combustion air "
        "pollutants?",
      choices=[
        "Carbon monoxide, nitrogen oxides, sulfur dioxide, particulates, and tobacco "
        "smoke",
        "Radon, mold, and asbestos",
        "Formaldehyde, insulation, and paint",
        "Uranium, thorium, and lead ore",
        "Pollen, spores, and animal dander"],
      ans=0,
      why="Those five are exactly the common combustion air pollutants the framework "
          "lists. Radon and mold are its natural examples, formaldehyde and insulation "
          "its human-made examples, and neither ore minerals nor biological allergens "
          "appear in the combustion list."),

 dict(q="What does the framework say produces radon-222?",
      choices=[
        "The decay of uranium found in some rocks and soils",
        "The combustion of fuel oil in a household furnace",
        "The evaporation of solvents from newly installed carpet",
        "The growth of mold in a damp basement",
        "The wearing away of asbestos insulation around pipes"],
      ans=0,
      why="The framework describes radon-222 as a naturally occurring radioactive gas "
          "produced by the decay of uranium found in some rocks and soils. Combustion, "
          "solvent evaporation, mold growth and asbestos wear are separate indoor "
          "sources of other pollutants."),

 dict(q="Radon measurements taken on the same day at four levels of one house are shown.",
      table=_T_FLOORS,
      choices=[
        "Radon is highest at the level closest to the soil and falls with height above it",
        "Radon is highest in the attic and falls toward the basement",
        "Radon is the same on every level of the house",
        "Radon rises with height above the soil surface",
        "The measurements show no relationship with position in the house"],
      ans=0,
      why="The largest value is in the basement, at the soil surface, and each level "
          "further up carries a smaller value. That pattern fits the framework's account "
          "of radon moving up through the soil and entering the home at the basement."),

 dict(q="Basement radon in four homes of similar age is shown alongside whether the "
        "foundation was sealed and the basement vented.",
      table=_T_SEAL,
      choices=[
        "The homes with sealed foundations and vented basements recorded lower radon "
        "than the homes without them",
        "The homes with sealed foundations recorded higher radon",
        "Sealing and venting made no difference to the measurements",
        "The lowest radon was recorded in a home with an unsealed foundation",
        "The measurements cannot be compared because the homes differ in age"],
      ans=0,
      why="Both treated homes carry smaller values than either untreated home. The "
          "framework has radon entering via the basement or cracks in the walls or "
          "foundation, so closing those routes is expected to lower what accumulates "
          "indoors."),

 dict(q="Which route does the framework describe for radon entering a home?",
      choices=[
        "Upward through the soil and in through the basement or cracks in the walls or "
        "foundation",
        "Downward from the atmosphere through the roof and attic vents",
        "Sideways from a neighboring building through a shared wall",
        "Through the electrical wiring and outlets",
        "Only in air brought in by a ventilation fan"],
      ans=0,
      why="The framework states that radon gas infiltrates homes as it moves up through "
          "the soil and enters via the basement or cracks in the walls or foundation. It "
          "gives no route from the roof, from a neighboring building, or through wiring."),

 dict(q="Measurements from four neighborhoods are shown.",
      table=_T_BEDROCK,
      choices=[
        "Indoor radon rises with the amount of uranium in the underlying rock",
        "Indoor radon falls as the uranium content of the rock rises",
        "Indoor radon is the same in all four neighborhoods",
        "Indoor radon is highest where the uranium content is lowest",
        "The two measurements are unrelated in these data"],
      ans=0,
      why="Ranking the neighborhoods by uranium in the rock gives the same order as "
          "ranking them by indoor radon. The framework has radon produced by the decay "
          "of uranium found in some rocks and soils, so more uranium beneath a home "
          "means more of the gas available to move up into it."),

 dict(q="Which health effect does the framework attribute to exposure to radon gas?",
      choices=[
        "Radon-induced lung cancer, the second leading cause of lung cancer in America",
        "Mesothelioma caused by fibers lodging in the chest lining",
        "Immediate loss of consciousness from oxygen deprivation",
        "Permanent hearing loss from prolonged exposure",
        "Irritation of the eyes and skin on contact"],
      ans=0,
      why="The framework states that exposure to radon gas can lead to radon-induced "
          "lung cancer, which is the second leading cause of lung cancer in America. "
          "Fiber-related disease, asphyxiation, hearing loss and surface irritation are "
          "effects of other pollutants."),

 dict(q="A room is monitored under three conditions.",
      table=_T_HEATER,
      choices=[
        "Carbon monoxide is highest when the fuel-burning heater runs without venting "
        "and falls sharply once the exhaust can leave the room",
        "Carbon monoxide is highest when the heater is switched off",
        "Carbon monoxide is the same in all three conditions",
        "Venting the heater raises the carbon monoxide in the room",
        "The heater has no effect on carbon monoxide in the room"],
      ans=0,
      why="The unvented condition carries by far the largest value, venting reduces it "
          "several fold, and switching the heater off reduces it further. Carbon "
          "monoxide is one of the common combustion air pollutants the framework lists."),

 dict(q="Formaldehyde measured in rooms furnished at different times is shown.",
      table=_T_NEW,
      choices=[
        "Formaldehyde is highest where the pressed-wood furniture is newest and falls as "
        "the furnishings age",
        "Formaldehyde is highest where the furnishings are oldest",
        "Formaldehyde is unrelated to the age of the furnishings",
        "Formaldehyde is the same in every room measured",
        "Formaldehyde rises as the furnishings age"],
      ans=0,
      why="The values fall at every step from the newest furnishings to the oldest. The "
          "framework names formaldehyde from building materials, furniture, upholstery "
          "and carpeting among the common human-made indoor air pollutants."),

 dict(q="Fine particulate measurements from four rooms are shown.",
      table=_T_SMOKE,
      choices=[
        "The rooms where tobacco was smoked carry higher particulate concentrations than "
        "the rooms where it was not",
        "The rooms without smoking carry the higher particulate concentrations",
        "Particulate concentrations are equal in all four rooms",
        "Only one of the smoking rooms differs from the rooms without smoking",
        "The particulate measurements show no relationship to smoking"],
      ans=0,
      why="Both smoking rooms carry values several times larger than either room without "
          "smoking. Tobacco smoke is one of the common combustion air pollutants the "
          "framework lists, and smoke is also one of its indoor particulates."),

 dict(q="Radon measurements in two homes with different water supplies are shown.",
      table=_T_WELL,
      choices=[
        "The home supplied by a private well has more radon in its water and more radon "
        "in its bathroom air",
        "The home on the municipal supply has more radon in its water",
        "Radon in the water and radon in the air are the same in both homes",
        "The home supplied by a private well has more radon in its water but less in its "
        "bathroom air",
        "The measurements show that radon cannot enter a home through water"],
      ans=0,
      why="The well-supplied home carries the larger value in both columns. The "
          "framework states that radon is also dissolved in groundwater that enters "
          "homes through a well, which is a second route alongside movement up through "
          "the soil."),

 dict(q="A family is advised to seal cracks in the foundation and to vent the basement. "
        "Which indoor pollutant is that advice aimed at?",
      choices=[
        "Radon entering from the soil beneath the house",
        "Formaldehyde released by new carpeting",
        "Lead released from old paint on interior walls",
        "Asbestos fibers shed by pipe insulation",
        "Mold growing on a damp bathroom ceiling"],
      ans=0,
      why="The framework has radon move up through the soil and enter homes via the "
          "basement or cracks in the walls or foundation, so those are exactly the routes "
          "the advice closes. The other pollutants originate inside the house rather than "
          "in the ground beneath it."),

 dict(q="Which of the following best explains why a home can have high indoor pollutant "
        "concentrations even though nothing is being burned inside it?",
      choices=[
        "Indoor air pollutants also come from natural sources and from human-made "
        "materials in the building",
        "Indoor air pollutants can only come from combustion, so the measurement must be "
        "wrong",
        "Outdoor pollutants cannot enter a building",
        "Indoor pollutants are produced by the measuring instrument",
        "A building with no combustion has no air to measure"],
      ans=0,
      why="The framework gives three kinds of indoor source -- natural, human-made and "
          "combustion -- so removing combustion leaves the other two. Radon and mold on "
          "one side and furnishings and paints on the other are its own examples."),

 dict(q="A student groups indoor pollutants by source and places tobacco smoke with "
        "carbon monoxide and nitrogen oxides. Which justification is best supported?",
      choices=[
        "All three appear in the framework's list of common combustion air pollutants",
        "All three are radioactive gases produced in soil",
        "All three are released by paints and adhesives",
        "All three are produced by mold growing on damp surfaces",
        "All three are natural source pollutants like radon"],
      ans=0,
      why="The framework's combustion list is carbon monoxide, nitrogen oxides, sulfur "
          "dioxide, particulates and tobacco smoke, so all three of these belong to that "
          "list. None of them is radioactive, released from paint, or produced by mold."),

 dict(q="Which measurement would best test whether the radon in a particular home is "
        "entering from the soil rather than from the water supply?",
      choices=[
        "Compare the radon concentration in the basement air with the radon "
        "concentration in the water drawn from the tap",
        "Measure the radon concentration in the attic only",
        "Measure the number of cracks in the foundation without measuring radon",
        "Measure the radon concentration in the outdoor air a kilometer away",
        "Measure the uranium content of the paint on the interior walls"],
      ans=0,
      why="The framework gives two routes, soil gas entering through the foundation and "
          "radon dissolved in well water, so distinguishing them requires measuring both "
          "the air near the entry point and the water. A crack count without a "
          "measurement, a distant outdoor reading and a paint analysis test neither route."),

 dict(q="Two rooms are identical except that one has new pressed-wood furniture and new "
        "carpet. Which pollutant is most likely to differ between them, according to the "
        "framework?",
      choices=[
        "Formaldehyde and other volatile organic compounds released by the furnishings",
        "Radon entering through the foundation",
        "Carbon monoxide from an unvented heater",
        "Sulfur dioxide from a coal-fired power station",
        "Mold growing behind the wall covering"],
      ans=0,
      why="The framework names volatile organic compounds from furniture, paneling and "
          "carpets, and formaldehyde from building materials, furniture, upholstery and "
          "carpeting, among the common human-made indoor pollutants. The other options "
          "have sources that the stem holds identical between the rooms."),

 dict(q="Why does the framework describe radon as a naturally occurring indoor "
        "pollutant even though it is found inside houses?",
      choices=[
        "It is produced by the decay of uranium in rocks and soils and then moves into "
        "the building",
        "It is manufactured for use in building insulation",
        "It is a product of burning fuel in household appliances",
        "It is released by paint applied to interior walls",
        "It forms indoors when volatile organic compounds react with sunlight"],
      ans=0,
      why="The framework attributes radon-222 to the decay of uranium found in some "
          "rocks and soils, which is a natural process outside the building, and then "
          "describes it infiltrating homes. It is not manufactured, burned or painted on, "
          "and no indoor photochemical route is given for it."),

 dict(q="A home inspector finds deteriorating paint in a house built long before lead "
        "paint was restricted. Which indoor pollutant does that finding most directly "
        "concern?",
      choices=[
        "Lead, which the framework lists among the common human-made indoor pollutants "
        "with paints as its source",
        "Radon, which enters from the soil beneath the house",
        "Carbon monoxide, which is produced by combustion appliances",
        "Mold, which grows on damp surfaces",
        "Nitrogen oxides, which are produced by burning fuel"],
      ans=0,
      why="The framework names lead from paints among the common human-made indoor air "
          "pollutants, so deteriorating paint is the source at issue. Radon comes from "
          "soil, carbon monoxide and nitrogen oxides from combustion, and mold from damp "
          "surfaces."),

 dict(q="A study finds that indoor particulate concentrations in a group of homes rise "
        "on days when candles and unvented heaters are used. Which conclusion does the "
        "framework support?",
      choices=[
        "Combustion inside the home is one source of indoor particulates",
        "Particulates indoors can only come from outdoor air",
        "Particulates are not classified as indoor air pollutants",
        "Radon accounts for the rise in particulates",
        "Formaldehyde is the particulate being measured"],
      ans=0,
      why="Particulates appear in the framework's list of common combustion air "
          "pollutants and among the indoor particulates alongside asbestos and dust, so "
          "burning things indoors is a source of them. Radon and formaldehyde are gases "
          "rather than particulates."),

 dict(q="Which pattern in a set of household measurements would most strongly suggest "
        "that a combustion appliance rather than the soil is the source of a pollutant?",
      choices=[
        "The concentration rises while the appliance is running and falls after it is "
        "switched off, at every level of the house",
        "The concentration is highest in the basement and falls with height",
        "The concentration is higher in homes built on uranium-rich rock",
        "The concentration is higher in homes supplied by a private well",
        "The concentration is unchanged whether the appliance runs or not"],
      ans=0,
      why="Tracking the operation of the appliance ties the pollutant to it, while the "
          "basement gradient, the uranium-rich rock and the private well are all patterns "
          "the framework associates with radon entering from soil or groundwater."),

 dict(q="Why is the classification of carbon monoxide as an asphyxiant important for "
        "understanding indoor air quality?",
      choices=[
        "It identifies the way the pollutant harms people, which is by interfering with "
        "the oxygen the body needs rather than by irritating tissue",
        "It identifies where the pollutant comes from, which is the soil beneath the "
        "house",
        "It shows that the pollutant is a particulate rather than a gas",
        "It shows that the pollutant is radioactive",
        "It shows that the pollutant is harmless at any concentration found indoors"],
      ans=0,
      why="The framework's classification describes how carbon monoxide acts on the "
          "body. It is separately identified as a combustion product, and nothing in the "
          "framework makes it a particulate, a radioactive substance or a harmless gas."),

 dict(q="A homeowner asks why two neighboring houses have very different indoor radon "
        "concentrations. Which explanation is best supported by the framework?",
      choices=[
        "The houses differ in how readily soil gas can enter, since radon comes in "
        "through the basement or cracks in the walls or foundation",
        "Radon is produced inside the house, so it depends on the furnishings",
        "Radon concentrations are identical in all houses on the same street",
        "Radon enters only through the roof, so roof condition explains the difference",
        "Radon is a combustion product, so it depends on the heating fuel used"],
      ans=0,
      why="The framework describes radon moving up through the soil and entering via the "
          "basement or cracks in the walls or foundation, so differences in those "
          "openings bear directly on how much gets in. It is not produced by furnishings, "
          "not a combustion product, and not described as entering through the roof."),

 dict(q="Which of the following would be the best evidence that a room's high "
        "formaldehyde concentration comes from its furnishings?",
      choices=[
        "The concentration falls steadily over the years after the furnishings are "
        "installed and is highest when they are new",
        "The concentration is highest in the basement and lowest in the attic",
        "The concentration rises when a fuel-burning appliance is used",
        "The concentration is higher in homes with a private well",
        "The concentration is unchanged when the room is ventilated"],
      ans=0,
      why="The framework names formaldehyde from building materials, furniture, "
          "upholstery and carpeting, so a decline as those furnishings age points to them "
          "as the source. A basement gradient and a well supply are radon patterns, and "
          "an appliance effect points to combustion."),

 dict(q="A public health message states that radon exposure matters even in homes where "
        "nobody smokes. Which framework statement most directly supports the message?",
      choices=[
        "Radon-induced lung cancer is the second leading cause of lung cancer in America",
        "Tobacco smoke is one of the common combustion air pollutants",
        "Radon is produced by the decay of uranium in rocks and soils",
        "Indoor pollutants come from natural, human-made and combustion sources",
        "Carbon monoxide is classified as an asphyxiant"],
      ans=0,
      why="The message is about a health consequence, and the framework states that "
          "exposure to radon gas can lead to radon-induced lung cancer, which is the "
          "second leading cause of lung cancer in America. The other statements describe "
          "sources or a different pollutant."),

 dict(q="Which summary best captures what this topic asks a student to be able to do?",
      choices=[
        "Identify indoor air pollutants and their natural, human-made and combustion "
        "sources, and describe the effects they have on people",
        "Calculate the concentration at which each indoor pollutant becomes dangerous",
        "Rank all indoor pollutants by the number of homes in which they are found",
        "Explain the chemical reactions by which outdoor smog forms",
        "Describe the design of a ventilation system for a large building"],
      ans=0,
      why="The two learning objectives for this topic are to identify indoor air "
          "pollutants and to describe their effects, and the framework supplies the "
          "three source categories that organize them. Dangerous concentrations, national "
          "rankings, outdoor smog chemistry and engineering design are not stated."),
]
