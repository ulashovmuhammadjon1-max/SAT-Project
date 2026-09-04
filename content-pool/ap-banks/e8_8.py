# AP ENVIRONMENTAL SCIENCE 8.8 Bioaccumulation and Biomagnification
# CED effective Fall 2026, Unit 8 Aquatic and Terrestrial Pollution. Enduring
# understanding STB-3. Learning objectives STB-3.I (describe bioaccumulation and
# biomagnification) and STB-3.J (describe their effects). Suggested skill 4.A, identify
# a testable hypothesis or scientific question for an investigation.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-3.I.1  Bioaccumulation is the selective absorption and concentration of elements
#              or compounds by cells in a living organism, most commonly fat-soluble
#              compounds.
#   STB-3.I.2  Biomagnification is the increase in concentration of substances per unit
#              of body tissue that occurs in successively higher trophic levels of a food
#              chain or in a food web.
#   STB-3.J.1  Some effects that can occur in an ecosystem when a persistent substance is
#              biomagnified in a food chain include eggshell thinning and developmental
#              deformities in top carnivores of the higher trophic levels.
#   STB-3.J.2  Humans also experience harmful effects from biomagnification, including
#              issues with the reproductive, nervous, and circulatory systems.
#   STB-3.J.3  DDT, mercury, and PCBs are substances that bioaccumulate and have
#              significant environmental impacts.
#
# THE SWAP IS THE POINT OF THIS TOPIC. Bioaccumulation is within one organism;
# biomagnification is across trophic levels. Wherever a distractor is the swap of the
# key, the anchor in verify_e8_8.py carries BOTH halves of the distinction so that it
# cannot also match the swapped option.
#
# ON SCOPE. Topic 8.7 keys the three properties of persistent organic pollutants
# themselves (STB-3.H.1 to STB-3.H.3) and topic 8.2 keys methylmercury (STB-3.B.10).
# Nothing here re-asks those definitions; every key rests on STB-3.I or STB-3.J.
#
# ON THE FIGURES. The bank carries no images, so every representation is a table and
# every keyed reading is recomputed in verify_e8_8.py from that table alone.
#
# NOT KEYED: no numeric magnification factor for a real ecosystem, no safe intake, no
# named place. The framework states none of them.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII.
TOPIC = ("8.8", "Bioaccumulation and Biomagnification", 8)

_T_CHAIN = dict(
    headers=["Position in one lake's food chain",
             "Concentration of the pollutant (parts per million)"],
    rows=[["Lake water", "0.0010"],
          ["Phytoplankton", "0.025"],
          ["Zooplankton", "0.20"],
          ["Small fish", "1.5"],
          ["Large fish", "8.0"],
          ["Fish eating bird", "40.0"]])

_T_AGE = dict(
    headers=["Age of the fish sampled (years)",
             "Concentration in the fish's fatty tissue (parts per million)"],
    rows=[["1", "0.40"],
          ["3", "1.3"],
          ["5", "2.6"],
          ["8", "4.9"],
          ["12", "7.8"]])

_T_FACTOR = dict(
    headers=["Step in a second lake's food chain",
             "Concentration of the pollutant (parts per million)"],
    rows=[["Water", "0.0020"],
          ["Plankton", "0.10"],
          ["Minnow", "2.0"],
          ["Trout", "20.0"],
          ["Eagle", "100.0"]])

_T_EGG = dict(
    headers=["Region where the top carnivore was sampled",
             "Concentration in the eggs (parts per million)",
             "Average eggshell thickness (millimeters)",
             "Chicks hatched per nest"],
    rows=[["Region with no history of use", "0.30", "0.55", "2.4"],
          ["Region with light past use", "2.0", "0.44", "1.5"],
          ["Region with heavy past use", "9.0", "0.31", "0.40"]])

_T_TWO = dict(
    headers=["Step in the food chain",
             "Concentration of the fat soluble compound (parts per million)",
             "Concentration of the water soluble compound (parts per million)"],
    rows=[["Algae", "0.050", "0.40"],
          ["Zooplankton", "0.45", "0.38"],
          ["Small fish", "3.6", "0.41"],
          ["Large fish", "22.0", "0.39"]])

_T_HUMAN = dict(
    headers=["Group of people surveyed",
             "Meals of predatory fish eaten each month",
             "Mercury measured in hair (parts per million)"],
    rows=[["Group 1", "0", "0.40"],
          ["Group 2", "2", "1.6"],
          ["Group 3", "8", "4.5"],
          ["Group 4", "20", "11.0"]])

QUESTIONS = [

 dict(q="How does the framework define bioaccumulation?",
      choices=[
        "The selective absorption and concentration of elements or compounds by cells "
        "inside a single living organism",
        "The increase in concentration of a substance per unit of body tissue at "
        "successively higher trophic levels",
        "The breakdown of a synthetic compound into smaller molecules by soil microbes",
        "The movement of a compound over long distances by wind and water",
        "The dilution of a compound as it passes from one organism to the next"],
      ans=0,
      why="STB-3.I.1 defines bioaccumulation as the selective absorption and "
          "concentration of elements or compounds by cells in a living organism. The "
          "first rejected option is the framework's definition of biomagnification, which "
          "is a different statement about a different scale."),

 dict(q="How does the framework define biomagnification?",
      choices=[
        "The increase in concentration of substances per unit of body tissue that occurs "
        "at successively higher trophic levels of a food chain or food web",
        "The selective absorption and concentration of a compound by the cells of one "
        "living organism",
        "The travel of a compound over long distances before it is redeposited",
        "The loss of a compound from an organism as it grows larger",
        "The conversion of a compound into a more toxic form by bacteria"],
      ans=0,
      why="STB-3.I.2 defines biomagnification as the increase in concentration of "
          "substances per unit of body tissue that occurs in successively higher trophic "
          "levels of a food chain or in a food web. The first rejected option is "
          "bioaccumulation, which describes one organism rather than a chain."),

 dict(q="Concentrations measured at each position in one lake's food chain are shown.",
      table=_T_CHAIN,
      choices=[
        "The concentration rises at every step from the water to the top consumer, which "
        "is what biomagnification describes",
        "The concentration falls at every step from the water to the top consumer",
        "The concentration is the same at every position in the chain",
        "The highest concentration is found in the lake water itself",
        "The concentration rises and then falls toward the top of the chain"],
      ans=0,
      why="Each row of the table carries a larger value than the row above it, so the "
          "concentration increases at successively higher positions. STB-3.I.2 defines "
          "biomagnification as exactly that increase across successively higher trophic "
          "levels."),

 dict(q="Which substances does the framework name as ones that bioaccumulate and have "
        "significant environmental impacts?",
      choices=[
        "DDT, mercury and PCBs",
        "Nitrate, phosphate and potassium",
        "Carbon dioxide, methane and water vapor",
        "Sulfur dioxide, ozone and carbon monoxide",
        "Sodium, calcium and chloride"],
      ans=0,
      why="STB-3.J.3 states that DDT, mercury and PCBs are substances that bioaccumulate "
          "and have significant environmental impacts. Nutrients, greenhouse gases, air "
          "pollutants and common ions are treated in other statements and are not named "
          "here."),

 dict(q="Which effects does the framework attribute to a persistent substance being "
        "biomagnified in a food chain?",
      choices=[
        "Eggshell thinning and developmental deformities in top carnivores of the higher "
        "trophic levels",
        "Immediate death of every producer at the base of the chain",
        "A permanent rise in the number of species in the ecosystem",
        "Thicker eggshells and larger clutches among top carnivores",
        "A loss of nutrients from the soil beneath the ecosystem"],
      ans=0,
      why="STB-3.J.1 names eggshell thinning and developmental deformities in top "
          "carnivores of the higher trophic levels as effects that can occur when a "
          "persistent substance is biomagnified. The rejected options reverse that effect "
          "or describe unrelated outcomes."),

 dict(q="Fish of different ages from the same population were sampled.",
      table=_T_AGE,
      choices=[
        "The older the fish, the higher the concentration in its fatty tissue, which is "
        "accumulation within individual organisms",
        "The older the fish, the lower the concentration in its fatty tissue",
        "Every fish sampled carries the same concentration regardless of age",
        "The youngest fish sampled carries the highest concentration",
        "Age and concentration are unrelated in these fish"],
      ans=0,
      why="The concentration rises at every step as the age of the fish rises, and all "
          "the fish come from one population and one trophic level, so the pattern is "
          "accumulation inside organisms. STB-3.I.1 describes that as the selective "
          "absorption and concentration of compounds by cells in a living organism."),

 dict(q="Which human body systems does the framework name as affected by "
        "biomagnification?",
      choices=[
        "The reproductive, nervous and circulatory systems",
        "The skeletal, muscular and integumentary systems",
        "The digestive system alone",
        "The respiratory system alone",
        "No human system is affected, according to the framework"],
      ans=0,
      why="STB-3.J.2 states that humans also experience harmful effects from "
          "biomagnification, including issues with the reproductive, nervous and "
          "circulatory systems. The framework names no other systems in this statement "
          "and does not exempt humans."),

 dict(q="Which kind of compound does the framework say most commonly bioaccumulates?",
      choices=[
        "Fat soluble compounds",
        "Compounds that dissolve only in water and not in fat",
        "Compounds that exist only as gases",
        "Compounds that break down within hours of release",
        "Compounds that occur only in rock and never in living tissue"],
      ans=0,
      why="STB-3.I.1 states that bioaccumulation is the selective absorption and "
          "concentration of elements or compounds by cells in a living organism, most "
          "commonly fat-soluble compounds. Each rejected option names a property that "
          "would work against storage in tissue."),

 dict(q="Concentrations at each step of a second lake's food chain are shown. About how "
        "many times higher is the concentration in the top consumer than in the water?",
      table=_T_FACTOR,
      choices=[
        "About 50,000 times higher",
        "About 5,000 times higher",
        "About 500 times higher",
        "About 50 times higher",
        "About 5 times higher"],
      ans=0,
      why="Dividing the top consumer's concentration by the concentration in the water "
          "gives a factor of tens of thousands. STB-3.I.2 describes biomagnification as "
          "the increase in concentration per unit of body tissue at successively higher "
          "trophic levels, and that increase compounds from one level to the next."),

 dict(q="Which statement correctly distinguishes the two processes this topic names?",
      choices=[
        "Bioaccumulation is a build-up within one organism, while biomagnification is a "
        "rise in concentration from each trophic level to the next",
        "Bioaccumulation is a rise in concentration from each trophic level to the next, "
        "while biomagnification is a build-up within one organism",
        "Both terms describe a rise from one trophic level to the next, and only the "
        "substances differ",
        "Both terms describe a build-up within a single organism, and only the tissue "
        "differs",
        "The two terms are interchangeable names for the same process"],
      ans=0,
      why="STB-3.I.1 places bioaccumulation inside a living organism, in the cells that "
          "absorb and concentrate the compound, while STB-3.I.2 places biomagnification "
          "across successively higher trophic levels of a food chain or web. The first "
          "rejected option swaps the two definitions."),

 dict(q="Why does the framework attach eggshell thinning and developmental deformities to "
        "top carnivores rather than to producers?",
      choices=[
        "Because the concentration rises at each higher trophic level, so the animals at "
        "the top of the chain carry the highest concentrations",
        "Because producers are unable to absorb any compound from their surroundings",
        "Because top carnivores are the only organisms with eggs of any kind",
        "Because the concentration is highest at the base of the chain and falls upward",
        "Because the framework says only birds can be harmed by any pollutant"],
      ans=0,
      why="STB-3.I.2 makes the concentration increase at successively higher trophic "
          "levels, and STB-3.J.1 places the eggshell thinning and developmental "
          "deformities in top carnivores of the higher trophic levels. The rejected "
          "options reverse that gradient or add claims the framework does not make."),

 dict(q="Eggs and nesting results for a top carnivore in three regions are shown.",
      table=_T_EGG,
      choices=[
        "The region with the highest concentration in the eggs has the thinnest shells and "
        "the fewest chicks hatched",
        "The region with the highest concentration in the eggs has the thickest shells",
        "Shell thickness is the same in all three regions",
        "The region with no history of use has the fewest chicks hatched",
        "Concentration in the eggs and shell thickness rise together across the regions"],
      ans=0,
      why="Ranking the regions by concentration in the eggs puts the shell thickness and "
          "the hatching success in the opposite order. STB-3.J.1 names eggshell thinning "
          "in top carnivores as an effect of a biomagnified persistent substance."),

 dict(q="Which of the following is the best testable scientific question about "
        "biomagnification in a lake?",
      choices=[
        "Does the concentration of the pollutant per unit of body tissue increase from "
        "plankton to small fish to predatory fish in this lake?",
        "Is pollution in this lake a serious problem for the community?",
        "Should the state prohibit the use of this compound?",
        "Which of the lake's fish species is the most beautiful?",
        "How many people have visited this lake since it was created?"],
      ans=0,
      why="STB-3.I.2 states biomagnification as a measurable increase in concentration "
          "per unit of body tissue across successively higher trophic levels, so a "
          "question naming those levels and that quantity can be answered with "
          "measurements. The rejected options ask for a value judgment, a policy choice, "
          "an opinion, or an unrelated count."),

 dict(q="A single osprey is sampled every year of its life and its tissue concentration "
        "of a persistent compound is found to rise steadily. Which process does this "
        "observation illustrate?",
      choices=[
        "Bioaccumulation, because the concentration is building up inside one organism "
        "over time",
        "Biomagnification, because the concentration is rising from one trophic level to "
        "the next",
        "Neither process, because a single organism cannot concentrate a compound",
        "Both processes equally, because the two terms mean the same thing",
        "Dilution, because the compound is being spread through the bird's tissues"],
      ans=0,
      why="STB-3.I.1 describes bioaccumulation as the selective absorption and "
          "concentration of a compound by cells in a living organism, which is what a "
          "record from one individual shows. STB-3.I.2 requires a comparison across "
          "trophic levels, which a single bird cannot provide."),

 dict(q="Two compounds were measured at each step of the same food chain.",
      table=_T_TWO,
      choices=[
        "The fat soluble compound rises steeply from step to step while the water soluble "
        "compound stays near the same value throughout",
        "The water soluble compound rises steeply while the fat soluble compound stays "
        "near the same value",
        "Both compounds rise steeply from step to step",
        "Both compounds stay near the same value at every step",
        "The fat soluble compound falls steadily from step to step"],
      ans=0,
      why="The fat soluble column rises by more than two orders of magnitude across the "
          "chain while the water soluble column stays within a narrow band. STB-3.I.1 "
          "states that bioaccumulation most commonly involves fat-soluble compounds, and "
          "STB-3.I.2 supplies the increase across trophic levels."),

 dict(q="A survey finds a compound at 0.05 parts per million in algae, 2 parts per "
        "million in the fish that eat them and 30 parts per million in the birds that eat "
        "those fish. Which process does the pattern illustrate?",
      choices=[
        "Biomagnification, because the concentration per unit of tissue rises at each "
        "higher trophic level",
        "Bioaccumulation, because the compound is building up inside one organism over "
        "its lifetime",
        "Neither, because concentrations always fall along a food chain",
        "Neither, because a compound cannot pass from prey to predator",
        "Dilution, because each consumer contains more tissue than its prey"],
      ans=0,
      why="STB-3.I.2 defines biomagnification as the increase in concentration per unit "
          "of body tissue at successively higher trophic levels of a food chain, which is "
          "what the three measurements show. A comparison across species is not the "
          "single-organism build-up of STB-3.I.1."),

 dict(q="Why does fat solubility make a compound especially likely to be concentrated in "
        "an organism's tissues?",
      choices=[
        "A compound that dissolves in fat is held in the body's fatty tissue rather than "
        "being carried away in watery wastes",
        "A compound that dissolves in fat is destroyed by the organism's cells",
        "A compound that dissolves in fat cannot enter an organism at all",
        "A compound that dissolves in fat is exhaled with every breath",
        "A compound that dissolves in fat is converted into a nutrient"],
      ans=0,
      why="STB-3.I.1 states that bioaccumulation is the selective absorption and "
          "concentration of compounds by cells, most commonly fat-soluble compounds, so "
          "the compound is retained rather than removed. The rejected options describe "
          "removal or destruction, which would prevent accumulation."),

 dict(q="Four groups of people who eat different amounts of predatory fish were compared.",
      table=_T_HUMAN,
      choices=[
        "The more meals of predatory fish a group eats, the higher the concentration "
        "measured in that group",
        "The more meals of predatory fish a group eats, the lower the concentration "
        "measured in that group",
        "All four groups show the same measured concentration",
        "The group that eats no predatory fish shows the highest measured concentration",
        "Diet and measured concentration are unrelated across these groups"],
      ans=0,
      why="Ranking the groups by meals eaten gives the same order as ranking them by the "
          "measured concentration. STB-3.J.2 states that humans experience harmful "
          "effects from biomagnification, and predatory fish occupy the higher trophic "
          "levels where STB-3.I.2 places the highest concentrations."),

 dict(q="Which observation would be evidence of biomagnification rather than of "
        "accumulation within an individual?",
      choices=[
        "Predatory fish carry a higher concentration per unit of tissue than the smaller "
        "fish they eat, which in turn carry more than the plankton",
        "One fish's concentration rises from year to year as it grows older",
        "One bird's concentration is higher in fat than in muscle",
        "A single organism's concentration is higher than the concentration in the water "
        "around it",
        "The pollutant is detected in the sediment of the lake"],
      ans=0,
      why="STB-3.I.2 requires a comparison across successively higher trophic levels, "
          "which only the keyed observation makes. Each rejected observation involves one "
          "organism or one compartment and so speaks to STB-3.I.1 or to nothing at all."),

 dict(q="Which study design would best test whether a pollutant biomagnifies in an "
        "estuary?",
      choices=[
        "Measure the concentration per unit of tissue in organisms from several trophic "
        "levels of the same food web at the same time",
        "Measure the concentration in one species of fish once",
        "Measure the total mass of every organism in the estuary",
        "Count the number of boats using the estuary each week",
        "Record the depth of the estuary at several points"],
      ans=0,
      why="STB-3.I.2 defines biomagnification across trophic levels, so the design must "
          "sample several levels of the same web and express the result per unit of "
          "tissue. A single species, a biomass total, a boat count and a depth survey "
          "cannot show a gradient across levels."),

 dict(q="Why does the framework say humans can be harmed by biomagnification even though "
        "humans are not named as a trophic level in a lake?",
      choices=[
        "Humans eat organisms from high trophic levels and so take in the concentrations "
        "that have built up there",
        "Humans absorb pollutants directly from the air and never from food",
        "Humans are unaffected by any pollutant found in fish",
        "Humans convert every pollutant they eat into a harmless form",
        "Humans occupy the lowest trophic level of every food web"],
      ans=0,
      why="STB-3.I.2 places the highest concentrations at the higher trophic levels and "
          "STB-3.J.2 states that humans also experience harmful effects from "
          "biomagnification, including issues with the reproductive, nervous and "
          "circulatory systems."),

 dict(q="Which pairing of a process with a matching observation is correct?",
      choices=[
        "Biomagnification, paired with a rise in concentration from prey to predator "
        "across a food web",
        "Biomagnification, paired with a rise in one animal's concentration over its "
        "lifetime",
        "Bioaccumulation, paired with a rise in concentration from prey to predator "
        "across a food web",
        "Bioaccumulation, paired with the breakdown of a compound in soil",
        "Biomagnification, paired with the movement of a compound by wind to a remote "
        "region"],
      ans=0,
      why="STB-3.I.2 makes biomagnification the increase across successively higher "
          "trophic levels, so a prey to predator rise is its observation. STB-3.I.1 makes "
          "bioaccumulation the build-up within an organism, and each rejected pairing "
          "attaches one term to the other's observation or to a statement from another "
          "topic."),

 dict(q="A student claims that a top predator has more of a pollutant only because it is "
        "a larger animal and therefore contains more tissue. Which framework point most "
        "directly answers that claim?",
      choices=[
        "Biomagnification is defined as an increase in concentration per unit of body "
        "tissue, so body size does not account for it",
        "Biomagnification is defined as an increase in the total mass of pollutant, so "
        "body size explains it entirely",
        "The framework states that predators are always smaller than their prey",
        "The framework states that concentration cannot be measured in a large animal",
        "The framework states that pollutants are distributed evenly across all trophic "
        "levels"],
      ans=0,
      why="STB-3.I.2 states the increase as one of concentration per unit of body tissue, "
          "which is already corrected for how much tissue an animal has, so a larger body "
          "does not by itself produce the pattern."),

 dict(q="Which of the following would most strengthen a claim that a compound is "
        "responsible for the thin eggshells observed in a population of top carnivores?",
      choices=[
        "Nests with higher concentrations of the compound in their eggs consistently have "
        "thinner shells than nests with lower concentrations",
        "The compound was manufactured in large amounts during the same decade",
        "The birds nest in trees rather than on cliffs",
        "The compound has a distinctive chemical structure",
        "The population has been counted every year for a long time"],
      ans=0,
      why="STB-3.J.1 names eggshell thinning as an effect in top carnivores when a "
          "persistent substance is biomagnified, so a within-population relationship "
          "between the measured concentration and the measured shell thickness tests the "
          "claim. Production totals, nesting habits, chemical structure and a long count "
          "do not."),

 dict(q="Why does the framework describe the effects of biomagnification in terms of a "
        "persistent substance?",
      choices=[
        "A substance that remains intact rather than breaking down is still present to be "
        "passed from prey to predator at each level",
        "A substance that breaks down quickly reaches higher concentrations at each level",
        "Persistence has no bearing on what happens along a food chain",
        "Only substances that dissolve in water can move along a food chain",
        "Persistence means the substance is produced continuously by the organisms "
        "themselves"],
      ans=0,
      why="STB-3.J.1 frames its effects around a persistent substance being biomagnified "
          "in a food chain, and STB-3.H.1 states that persistent organic pollutants do "
          "not easily break down. A compound that degraded quickly would not remain to "
          "climb the chain."),

 dict(q="Which of the following is NOT something the framework states about these two "
        "processes?",
      choices=[
        "Concentrations fall at each higher trophic level of a food chain",
        "Bioaccumulation most commonly involves fat soluble compounds",
        "Biomagnification is measured per unit of body tissue",
        "DDT, mercury and PCBs bioaccumulate and have significant environmental impacts",
        "Humans experience harmful effects from biomagnification"],
      ans=0,
      why="STB-3.I.2 states that concentrations increase, not fall, at successively "
          "higher trophic levels. The four rejected options restate STB-3.I.1, STB-3.I.2, "
          "STB-3.J.3 and STB-3.J.2 correctly."),

 dict(q="An investigator wants to know whether a compound builds up inside individual "
        "clams over time. Which hypothesis is testable and matched to that question?",
      choices=[
        "Clams held in the same water for longer will show higher tissue concentrations "
        "than clams held for a shorter time",
        "Clams are more important to the estuary than fish are",
        "The compound should be banned from use near the estuary",
        "Clams that are prettier will contain less of the compound",
        "The estuary has changed a great deal since it was first surveyed"],
      ans=0,
      why="STB-3.I.1 describes bioaccumulation as absorption and concentration by cells "
          "in a living organism, so a comparison of exposure durations in the same "
          "organism tests it directly. The rejected statements state a value, a policy or "
          "an unmeasurable comparison."),

 dict(q="A lake's top predator carries a far higher tissue concentration than the water it "
        "swims in, and its prey carry values in between. Which two framework processes "
        "together account for that?",
      choices=[
        "Absorption and concentration by the cells of each organism, together with an "
        "increase from each trophic level to the next",
        "Breakdown of the compound by microbes, together with dilution at each level",
        "Long distance transport by wind, together with redeposition in the lake",
        "Conversion of the compound to a harmless form, together with excretion",
        "Settling of the compound into sediment, together with burial"],
      ans=0,
      why="STB-3.I.1 supplies the uptake and retention inside each organism and STB-3.I.2 "
          "supplies the rise from one trophic level to the next, and together they "
          "produce a top predator far above the water it lives in."),

 dict(q="Which measurement would show that a compound is being concentrated by an organism "
        "rather than simply matching its surroundings?",
      choices=[
        "The concentration in the organism's tissue compared with the concentration in the "
        "water or food it takes in",
        "The volume of water the organism moves across its gills each day",
        "The number of organisms of that species in the lake",
        "The temperature of the water on the day of sampling",
        "The length of the organism at the time of sampling"],
      ans=0,
      why="STB-3.I.1 describes bioaccumulation as selective absorption and concentration "
          "by cells, so the test is whether the tissue value stands above the value in "
          "the surrounding water or food. Flow rate, abundance, temperature and body "
          "length do not answer that."),

 dict(q="Which summary best captures this topic?",
      choices=[
        "Compounds are absorbed and concentrated by the cells of individual organisms, "
        "most commonly fat soluble ones, and their concentration per unit of tissue rises "
        "at each higher trophic level, producing eggshell thinning and deformities in top "
        "carnivores and reproductive, nervous and circulatory harm in humans",
        "Compounds are diluted inside organisms and fall in concentration at each higher "
        "trophic level, so top carnivores are the least affected",
        "Only water soluble compounds build up in organisms, and no effect on wildlife or "
        "people has been described",
        "The two terms in this topic describe the same process at the same scale and "
        "produce no measurable effects",
        "Compounds accumulate only in producers and never reach the animals that eat them"],
      ans=0,
      why="Each clause of the keyed summary is one of STB-3.I.1, STB-3.I.2, STB-3.J.1 and "
          "STB-3.J.2. Every rejected summary reverses the direction of the gradient, "
          "denies the effects, or conflates the two processes."),
]
