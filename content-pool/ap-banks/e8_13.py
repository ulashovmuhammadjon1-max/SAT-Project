# AP ENVIRONMENTAL SCIENCE 8.13 Dose Response Curve
# CED effective Fall 2026, Unit 8 Aquatic and Terrestrial Pollution. Enduring
# understanding EIN-3, pollutants can have both direct and indirect impacts on the health
# of organisms, including humans. Learning objective EIN-3.B: evaluate dose response
# curves. Suggested skill 5.E, explain what the data implies or illustrates about
# environmental issues.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-3.B.1  A dose response curve describes the effect on an organism or mortality rate
#              in a population based on the dose of a particular toxin or drug.
#
# THIS TOPIC IS NAMED AFTER A PICTURE AND THE BANK CANNOT SHOW ONE. So no stem here says
# "the curve shows", "in the graph" or "as plotted". Every dose response relationship is
# given as a TABLE of doses against responses, and every keyed reading is recomputed in
# verify_e8_13.py from that table alone. Where an item asks for the dose at which some
# stated share responds, a row carries that share exactly, so the value is readable from
# the rows given rather than guessed between them.
#
# WHAT THE ONE STATEMENT LICENSES, and what it does not. EIN-3.B.1 names three things:
# the response may be an EFFECT on an organism or a MORTALITY RATE in a population; the
# controlling variable is the DOSE; and the agent may be a TOXIN OR A DRUG. Items key
# those and reason from them. NOT KEYED, because the framework states none of them: any
# named shape of the relationship, any threshold model, any safe dose, any real chemical,
# any exposure duration and any extrapolation past the highest dose tested.
#
# ON SCOPE. Topic 8.12 keys the LD50 itself (EIN-3.A.1) and its reading from a dose
# table. Item 22 here is the only one that mentions the LD50, and it keys the relation
# between the two statements rather than re-asking either.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII.
TOPIC = ("8.13", "Dose Response Curve", 8)

_T_EFFECT = dict(
    headers=["Dose given to each group (micrograms per liter)",
             "Percent of the group whose growth was reduced"],
    rows=[["0", "0"],
          ["2.0", "8"],
          ["5.0", "25"],
          ["10", "52"],
          ["20", "80"]])

_T_BOTH = dict(
    headers=["Dose given to each group (micrograms per liter)",
             "Percent of the group that died",
             "Percent of the survivors with impaired reproduction"],
    rows=[["0", "0", "1"],
          ["5.0", "0", "12"],
          ["20", "4", "44"],
          ["60", "26", "78"],
          ["150", "62", "95"]])

_T_ENZYME = dict(
    headers=["Dose given to each group (milligrams per kilogram of body mass)",
             "Average activity of the enzyme in the exposed animals (units)"],
    rows=[["0", "100"],
          ["1.0", "92"],
          ["4.0", "71"],
          ["16", "38"],
          ["64", "12"]])

_T_DRUG = dict(
    headers=["Dose of the drug given to each group (milligrams)",
             "Percent of the group whose symptom improved"],
    rows=[["0", "5"],
          ["10", "28"],
          ["25", "61"],
          ["50", "83"],
          ["100", "90"]])

_T_TWO_SPECIES = dict(
    headers=["Dose given to each group (micrograms per liter)",
             "Percent of species R showing the effect",
             "Percent of species S showing the effect"],
    rows=[["1.0", "18", "0"],
          ["4.0", "50", "3"],
          ["16", "84", "11"],
          ["64", "97", "50"],
          ["256", "100", "88"]])

_T_RIVER = dict(
    headers=["Site on the river", "Concentration measured at the site (micrograms per liter)",
             "Percent of test animals showing the effect at that concentration in the "
             "laboratory"],
    rows=[["Site 1", "2.0", "6"],
          ["Site 2", "18", "40"],
          ["Site 3", "55", "76"]])

_T_PLATEAU = dict(
    headers=["Dose given to each group (milligrams per kilogram of body mass)",
             "Percent of the group showing the response"],
    rows=[["0", "0"],
          ["10", "30"],
          ["50", "88"],
          ["250", "100"],
          ["1250", "100"]])

_T_CONTROL = dict(
    headers=["Group in the experiment", "Dose received (milligrams per liter)",
             "Percent of the group showing the effect"],
    rows=[["Control group", "0", "2"],
          ["Low dose group", "5.0", "19"],
          ["Middle dose group", "20", "48"],
          ["High dose group", "80", "81"]])

QUESTIONS = [

 dict(q="What does the framework say a dose response curve describes?",
      choices=[
        "The effect on an organism, or the mortality rate in a population, based on the "
        "dose of a particular toxin or drug",
        "The length of time a chemical remains in the environment before breaking down",
        "The distance a chemical travels from its source before it is redeposited",
        "The share of a chemical that dissolves in fat rather than in water",
        "The number of species present in an ecosystem after a chemical is released"],
      ans=0,
      why="EIN-3.B.1 states that a dose response curve describes the effect on an organism "
          "or mortality rate in a population based on the dose of a particular toxin or "
          "drug. Persistence, transport, fat solubility and species counts belong to other "
          "statements in the course."),

 dict(q="Which two kinds of response does the framework allow a dose response "
        "relationship to describe?",
      choices=[
        "An effect on an organism, or a mortality rate in a population",
        "A mortality rate in a population, and nothing else",
        "The market price of a chemical, or the quantity produced",
        "The rate at which a chemical breaks down, or the rate at which it evaporates",
        "The number of organisms in an ecosystem, or the area the ecosystem covers"],
      ans=0,
      why="EIN-3.B.1 names both an effect on an organism and a mortality rate in a "
          "population as what the relationship describes, so death is one possible "
          "response rather than the only one."),

 dict(q="Groups of one species were given different doses and their growth was recorded.",
      table=_T_EFFECT,
      choices=[
        "The share of the group whose growth was reduced rises at every higher dose, and "
        "no reduction occurred in the group that received none",
        "The share whose growth was reduced falls at every higher dose",
        "The same share of every group had reduced growth",
        "The group that received the largest dose had the smallest share affected",
        "The group that received no dose had the largest share affected"],
      ans=0,
      why="Each higher dose in the table carries a larger percentage than the row above "
          "it, and the row with no dose carries none. EIN-3.B.1 makes such a relationship "
          "between dose and an effect on the organism what a dose response describes."),

 dict(q="In a dose response relationship, which quantity is the one the response depends "
        "on?",
      choices=[
        "The dose of the toxin or drug that was given",
        "The number of species living in the study area",
        "The temperature of the room in which the study was run",
        "The length of the report describing the study",
        "The order in which the groups were tested"],
      ans=0,
      why="EIN-3.B.1 states that the relationship describes the effect or mortality rate "
          "based on the dose of a particular toxin or drug, so the dose is the controlling "
          "quantity."),

 dict(q="Deaths and a nonlethal effect were recorded for the same groups.",
      table=_T_BOTH,
      choices=[
        "A substantial share of survivors shows the nonlethal effect at doses that killed "
        "few or none of the group",
        "The nonlethal effect appears only at doses that killed most of the group",
        "Deaths and the nonlethal effect appear at exactly the same doses",
        "No group shows the nonlethal effect at any dose",
        "The share showing the nonlethal effect falls as the dose rises"],
      ans=0,
      why="At the lower doses the mortality column is at or near zero while the effect "
          "column already reaches double figures, and both rise with dose. EIN-3.B.1 "
          "allows the response to be an effect on an organism as well as a mortality rate "
          "in a population."),

 dict(q="Does the framework's statement apply only to poisons?",
      choices=[
        "No, it refers to the dose of a particular toxin or drug, so a drug is covered as "
        "well",
        "Yes, it refers only to substances classified as toxins",
        "Yes, it refers only to substances that are lethal at some dose",
        "No, it refers to any measurement at all, whether or not a substance is involved",
        "No, it refers only to drugs and not to toxins"],
      ans=0,
      why="EIN-3.B.1 refers to the dose of a particular toxin or drug, so both are within "
          "the statement. It does not extend to measurements with no administered "
          "substance."),

 dict(q="Why must a study give several different doses in order to describe a dose "
        "response relationship?",
      choices=[
        "The relationship is between the dose and the response, and a relationship cannot "
        "be described from a single value of the dose",
        "A single dose would be too small to produce any response",
        "Several doses make the substance less toxic to the organisms",
        "Regulations require at least five doses in any study",
        "Several doses shorten the time the study takes to complete"],
      ans=0,
      why="EIN-3.B.1 describes the response as based on the dose, which is a relationship "
          "between two quantities, so the dose must be varied for the relationship to be "
          "observed."),

 dict(q="A measured biological quantity was recorded in animals given different doses.",
      table=_T_ENZYME,
      choices=[
        "The measured activity falls at every higher dose, so the response here is a graded "
        "effect rather than a count of deaths",
        "The measured activity rises at every higher dose",
        "The measured activity is the same at every dose given",
        "The animals given the largest dose showed the highest activity",
        "The table records deaths rather than a measured activity"],
      ans=0,
      why="The activity column falls at every step as the dose rises and no column records "
          "deaths. EIN-3.B.1 allows the response to be an effect on an organism, which a "
          "measured activity is."),

 dict(q="What does the framework's phrase about an effect on an organism allow a dose "
        "response relationship to record besides death?",
      choices=[
        "Any measurable effect the dose produces in the organism, such as impaired growth "
        "or a changed body function",
        "Only the number of organisms present in the ecosystem",
        "Only the price of the substance being tested",
        "Only the persistence of the substance in soil",
        "Nothing besides death, since the framework restricts the term to mortality"],
      ans=0,
      why="EIN-3.B.1 names the effect on an organism alongside the mortality rate in a "
          "population, so a response short of death is within the statement. Abundance, "
          "price and persistence are not responses of an organism to a dose."),

 dict(q="Patients were given different doses of one drug and their symptoms were followed.",
      table=_T_DRUG,
      choices=[
        "The share of the group whose symptom improved rises with the dose given",
        "The share whose symptom improved falls as the dose rises",
        "The same share improved at every dose given",
        "No group showed any improvement at any dose",
        "The group that received no drug showed the largest improvement"],
      ans=0,
      why="Each higher dose in the table carries a larger percentage improved than the row "
          "above it, and the group receiving none carries the smallest. EIN-3.B.1 covers a "
          "drug as well as a toxin."),

 dict(q="Which design would produce the data a dose response relationship requires?",
      choices=[
        "Several comparable groups, each given a different dose, with the same response "
        "measured in every group",
        "One group given one dose, with the response measured once",
        "Several groups given the same dose, with a different response measured in each",
        "One group observed without any substance being given",
        "Several groups given different substances at doses that are not recorded"],
      ans=0,
      why="EIN-3.B.1 makes the relationship one between the dose and the response, so the "
          "dose must vary across groups while the response measured stays the same. Each "
          "rejected design holds the dose fixed, changes the response, or leaves the dose "
          "unrecorded."),

 dict(q="A study tested doses from one to sixty units and found the response rising "
        "throughout. What does the framework's statement license the researchers to say "
        "about a dose of six hundred units?",
      choices=[
        "Nothing, because the relationship describes the responses at the doses that were "
        "actually given",
        "That the response at six hundred units will be ten times the response at sixty",
        "That the response at six hundred units will be zero",
        "That every organism will die at six hundred units",
        "That the response will begin to fall above sixty units"],
      ans=0,
      why="EIN-3.B.1 describes the response based on the dose, and a study describes the "
          "doses it administered. The framework supplies no rule for projecting the "
          "relationship beyond the range tested."),

 dict(q="Why is a dose response relationship tied to one particular substance?",
      choices=[
        "The framework states it for the dose of a particular toxin or drug, so a "
        "relationship measured for one substance describes that substance",
        "Every substance produces exactly the same response at the same dose",
        "The relationship depends on the container the substance was stored in",
        "The relationship applies to all substances of the same color",
        "The relationship is fixed by the species alone and not by the substance"],
      ans=0,
      why="EIN-3.B.1 refers to the dose of a particular toxin or drug, which ties the "
          "relationship to the substance administered as well as to the organisms tested."),

 dict(q="Two species were given the same doses and the same effect was recorded in each.",
      table=_T_TWO_SPECIES,
      choices=[
        "Half of the first species shows the effect at a dose many times smaller than the "
        "dose at which half of the second species does",
        "Half of the second species shows the effect at a dose many times smaller than the "
        "dose at which half of the first species does",
        "The two species reach half showing the effect at the same dose",
        "Neither species reaches half showing the effect at any dose given",
        "The first species never shows the effect at any dose given"],
      ans=0,
      why="Each species has a row at exactly half showing the effect, and the dose in the "
          "row for the first species is many times smaller. EIN-3.B.1 makes the response "
          "depend on the dose, so the species needing less dose for the same response is "
          "the more sensitive."),

 dict(q="A dose response relationship shows the response rising as the dose rises. What "
        "does that pattern mean in the framework's terms?",
      choices=[
        "The size of the response depends on the dose, with larger doses producing larger "
        "responses over the range tested",
        "The size of the dose depends on the response",
        "The response is unrelated to the dose over the range tested",
        "The substance is present in the environment at a higher concentration",
        "The organisms tested belong to more than one species"],
      ans=0,
      why="EIN-3.B.1 states that the relationship describes the response based on the "
          "dose, so a response that rises with dose is the dose controlling the response "
          "rather than the reverse."),

 dict(q="Which of the following is the response rather than the dose in a study of a "
        "pollutant?",
      choices=[
        "The percentage of exposed animals whose reproduction was impaired",
        "The concentration of the pollutant in the water each group received",
        "The number of milligrams administered to each animal",
        "The amount of the substance placed in each tank",
        "The strength of the solution prepared for each group"],
      ans=0,
      why="EIN-3.B.1 makes the dose the administered quantity and the effect or mortality "
          "rate the response. The four rejected options all describe how much substance "
          "the organisms received."),

 dict(q="Concentrations measured at three river sites are listed beside the share of test "
        "animals affected at each concentration in the laboratory.",
      table=_T_RIVER,
      choices=[
        "The site with the highest measured concentration corresponds to the largest share "
        "of test animals affected, so conditions there are of most concern",
        "The site with the lowest measured concentration corresponds to the largest share "
        "affected",
        "All three sites correspond to the same share of test animals affected",
        "None of the three sites corresponds to any share of animals affected",
        "The share affected falls as the measured concentration rises"],
      ans=0,
      why="Ranking the sites by measured concentration gives the same order as ranking "
          "them by the share affected. EIN-3.B.1 makes the response depend on the dose, "
          "which is what lets a field concentration be read against laboratory data."),

 dict(q="Why does the framework describe the mortality response as a rate in a population "
        "rather than as an outcome for one organism?",
      choices=[
        "A rate expresses what share of a group is affected, which one organism cannot "
        "show",
        "One organism cannot be exposed to a toxin or a drug",
        "A rate is easier to calculate than an individual outcome",
        "A single organism always responds in the same way as the whole population",
        "The framework does not permit any measurement on a single organism"],
      ans=0,
      why="EIN-3.B.1 pairs the mortality rate with a population while it pairs an effect "
          "with an organism, so the rate is a property of the group. The framework does "
          "allow an effect to be measured in an organism."),

 dict(q="A researcher gives one dose to one group and records that forty percent showed "
        "the effect. What is the limitation of that result?",
      choices=[
        "It gives the response at a single dose and so does not describe how the response "
        "depends on the dose",
        "It gives the response at every dose, so nothing further can be learned",
        "It gives the dose but not the response",
        "It cannot be recorded because a percentage requires two doses",
        "It shows that the substance has no effect at any dose"],
      ans=0,
      why="EIN-3.B.1 describes a response based on the dose, which requires the dose to "
          "vary. A single dose yields one point rather than the dependence the statement "
          "names."),

 dict(q="Groups were given doses spanning more than two orders of magnitude and the "
        "response was recorded.",
      table=_T_PLATEAU,
      choices=[
        "Above a certain dose every individual in the group responded, so no higher dose "
        "could raise the percentage further",
        "The percentage responding continued to rise at the two highest doses",
        "The percentage responding fell at the highest dose given",
        "No individual responded at any dose given",
        "The percentage responding was the same at every dose given"],
      ans=0,
      why="The two highest rows both record the entire group responding, and a percentage "
          "cannot exceed the whole group. EIN-3.B.1 makes the response depend on the dose, "
          "and the table shows where that dependence has run out of room."),

 dict(q="What does a dose response relationship let a scientist say about an environmental "
        "issue?",
      choices=[
        "It connects a concentration organisms are exposed to with the response expected at "
        "that concentration",
        "It states how much of a substance was manufactured in a given year",
        "It states how long a substance will remain in the environment",
        "It states how far a substance will travel on the wind",
        "It states the number of species in the ecosystem before the substance arrived"],
      ans=0,
      why="EIN-3.B.1 describes the effect or mortality rate based on the dose, so it links "
          "an exposure to an expected response. Production, persistence, transport and "
          "species counts are described by other statements in the course."),

 dict(q="How does an LD50 relate to a dose response relationship?",
      choices=[
        "It is the single dose at which the mortality response reaches half of the "
        "population",
        "It is the whole relationship between dose and response for a substance",
        "It is the dose at which the response first becomes measurable",
        "It is the dose at which the entire population dies",
        "It is unrelated to any dose response relationship"],
      ans=0,
      why="EIN-3.A.1 defines the LD50 as the dose lethal to 50 percent of the population "
          "of a particular species, and EIN-3.B.1 makes the mortality rate a response "
          "based on dose, so the LD50 is one point of that relationship rather than the "
          "whole of it."),

 dict(q="Why does a dose response study normally include a group that receives no dose at "
        "all?",
      choices=[
        "It shows what share of a group responds without the substance, so the responses at "
        "other doses can be compared against it",
        "It shows the largest response the substance can produce",
        "It doubles the number of doses that can be reported",
        "It is required in order to calculate a percentage",
        "It removes the need to measure any response at all"],
      ans=0,
      why="EIN-3.B.1 makes the response depend on the dose, so a group at zero dose "
          "establishes the response attributable to something other than the substance. "
          "It is not itself the largest response nor a calculating device."),

 dict(q="One experiment reported four groups and their results.",
      table=_T_CONTROL,
      choices=[
        "A small share of the group receiving no dose showed the effect, and the share rose "
        "with each higher dose above it",
        "The group receiving no dose showed the largest share with the effect",
        "Every group showed the same share with the effect",
        "No group receiving a dose showed more of the effect than the group receiving none",
        "The share showing the effect fell as the dose rose"],
      ans=0,
      why="The row with no dose carries a small percentage and every dosed row carries a "
          "larger one, rising with the dose. EIN-3.B.1 makes the response depend on the "
          "dose, and the untreated group is what the dosed groups are read against."),

 dict(q="Which conclusion would NOT be supported by a dose response study alone?",
      choices=[
        "That the doses used in the study are the doses organisms receive in the wild",
        "That the response measured rose as the dose rose over the range tested",
        "That the substance produced a measurable response in the organisms tested",
        "That a larger dose produced a larger share of affected individuals",
        "That the group given no dose responded less than the dosed groups"],
      ans=0,
      why="EIN-3.B.1 describes the response based on the dose administered, which says "
          "nothing about what organisms in the field are exposed to. The four rejected "
          "conclusions are readings of the study's own doses and responses."),

 dict(q="Two populations of the same species respond to the same substance, but one "
        "requires a much larger dose for the same share to be affected. What does that "
        "difference show?",
      choices=[
        "The population needing the larger dose is less sensitive to that substance",
        "The two populations are equally sensitive to that substance",
        "The substance is more persistent in the environment of the less affected "
        "population",
        "The substance travels farther in the environment of the more affected population",
        "The population needing the larger dose received a different substance"],
      ans=0,
      why="EIN-3.B.1 makes the response depend on the dose of a particular substance, so "
          "needing more of the same substance for the same response is lower sensitivity. "
          "Persistence and transport are properties of the substance in the environment "
          "rather than of the response."),

 dict(q="A regulator has dose response data for a pollutant and measured concentrations "
        "at several sites. Which use of the two together is best supported?",
      choices=[
        "Identifying the sites whose measured concentrations fall where the data show a "
        "large share of organisms responding",
        "Concluding that no site is of concern because the study was run in a laboratory",
        "Concluding that every site is equally affected regardless of its concentration",
        "Estimating how long the pollutant will persist in the sediment at each site",
        "Estimating how far the pollutant travelled before reaching each site"],
      ans=0,
      why="EIN-3.B.1 links a dose to an expected response, so matching measured "
          "concentrations against the doses at which responses are large is what the two "
          "sets of data support together. Persistence and transport are not part of this "
          "statement."),

 dict(q="Why does the framework word its statement as a response based on the dose rather "
        "than as a response to the presence of a substance?",
      choices=[
        "The size of the response depends on how much of the substance is received, not "
        "merely on whether any is present",
        "The framework denies that any substance produces a response",
        "The framework treats every dose as producing the same response",
        "The framework treats presence and dose as identical terms",
        "The framework measures the substance rather than the organism"],
      ans=0,
      why="EIN-3.B.1 makes the effect or mortality rate depend on the dose of a particular "
          "toxin or drug, which distinguishes how much is received from whether any is "
          "present."),

 dict(q="Which pairing of a study result with the framework's terms is correct?",
      choices=[
        "The percentage of a population that died at each administered amount, paired with "
        "a mortality rate described on the basis of dose",
        "The percentage of a population that died at each administered amount, paired with "
        "the persistence of the substance",
        "The number of years a substance stays in soil, paired with a response based on "
        "dose",
        "The distance a substance travels on the wind, paired with a mortality rate in a "
        "population",
        "The price of a substance, paired with an effect on an organism"],
      ans=0,
      why="EIN-3.B.1 pairs the dose with an effect on an organism or a mortality rate in a "
          "population. Persistence, transport and price belong to other statements and are "
          "not responses based on dose."),

 dict(q="Which summary best captures this topic?",
      choices=[
        "A dose response relationship records how an effect on an organism, or the share of "
        "a population that dies, changes with the dose of a particular toxin or drug, and "
        "it describes only the doses that were actually given",
        "A dose response relationship records only deaths and can describe no other effect",
        "A dose response relationship applies to toxins but never to drugs",
        "A dose response relationship states the dose below which a substance is safe for "
        "every organism",
        "A dose response relationship describes how long a substance persists after it is "
        "released"],
      ans=0,
      why="The keyed summary states EIN-3.B.1 together with the limit that follows from "
          "it, since a study describes the doses it administered. Every rejected summary "
          "drops the nonlethal effect, excludes drugs, invents a safety threshold, or "
          "replaces the response with persistence."),
]
