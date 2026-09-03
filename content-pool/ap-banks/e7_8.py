# AP ENVIRONMENTAL SCIENCE 7.8 Noise Pollution
# CED effective Fall 2026, Unit 7 Atmospheric Pollution. Enduring understanding STB-2.
# Learning objective STB-2.J: describe human activities that result in noise pollution
# and its effects. Suggested skill 3.C, describe the author's reasoning (use of
# evidence to support a claim).
#
# Essential knowledge relied on, in the framework's own words:
#   STB-2.J.1  Noise pollution is sound at levels high enough to cause physiological
#              stress and hearing loss.
#   STB-2.J.2  Sources of noise pollution in urban areas include transportation,
#              construction, and domestic and industrial activity.
#   STB-2.J.3  Some effects of noise pollution on animals in ecological systems include
#              stress, the masking of sounds used to communicate or hunt, damaged
#              hearing, and causing changes to migratory routes.
#
# ON WHAT IS NOT KEYED. The framework gives NO sound level, no exposure limit, no
# threshold in decibels, no named species and no named city. So every number in this
# module belongs to the study described in its own stem or table, is supplied to the
# student there, and is recomputed in verify_e7_8.py from that table alone. No key
# asks whether a particular level counts as noise pollution -- the framework's
# definition is qualitative, sound at levels high enough to cause physiological stress
# and hearing loss, and the keys stay inside it.
#
# ON THE SKILL. Suggested skill 3.C is about an author's use of evidence to support a
# claim, so roughly a third of the items give a claim and a piece of evidence and ask
# what the evidence does or does not establish. Those keys rest on the logic of the
# support, together with whichever of the three statements above the claim concerns.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII: export_units.py does not typeset
# ENV_SCI.
TOPIC = ("7.8", "Noise Pollution", 7)

_T_SOURCES = dict(
    headers=["Activity recorded in one city block",
             "Sound level measured at the sidewalk (decibels)",
             "Hours per day the activity was audible"],
    rows=[["Heavy road traffic", "82", "14"],
          ["Building demolition next door", "95", "6"],
          ["Rooftop ventilation plant of a factory", "74", "24"],
          ["Household appliances heard through a wall", "58", "9"]])

_T_HEARING = dict(
    headers=["Group of workers", "Years at the noisy work site",
             "Average shift in hearing threshold (decibels)"],
    rows=[["Group 1", "2", "3"],
          ["Group 2", "8", "11"],
          ["Group 3", "16", "23"],
          ["Comparison group away from the noise", "16", "2"]])

_T_STRESS = dict(
    headers=["Enclosure", "Background sound level (decibels)",
             "Average stress hormone in the animals (nanograms per milliliter)"],
    rows=[["Quiet enclosure", "40", "12"],
          ["Moderate enclosure", "65", "21"],
          ["Loud enclosure", "85", "38"]])

_T_MASK = dict(
    headers=["Background sound level during the trial (decibels)",
             "Distance at which a calling animal could still be heard by a listener (meters)"],
    rows=[["45", "400"],
          ["60", "180"],
          ["75", "60"],
          ["90", "15"]])

_T_ROUTE = dict(
    headers=["Season", "Shipping traffic through the corridor (vessels per week)",
             "Share of tracked animals using the corridor (percent)"],
    rows=[["Season 1", "20", "78"],
          ["Season 2", "55", "54"],
          ["Season 3", "110", "31"],
          ["Season 4", "180", "12"]])

_T_HUNT = dict(
    headers=["Trial condition", "Prey rustles detected by the hunting animal per hour",
             "Successful captures per hour"],
    rows=[["Quiet background", "24", "9"],
          ["Recorded traffic noise played back", "7", "2"]])

QUESTIONS = [

 dict(q="How does the framework define noise pollution?",
      choices=[
        "Sound at levels high enough to cause physiological stress and hearing loss",
        "Any sound produced by a machine rather than by a living thing",
        "Sound that can be heard at night but not during the day",
        "Sound of any level that a listener finds unpleasant",
        "Sound that carries more than one kilometer from its source"],
      ans=0,
      why="The framework defines noise pollution by its effects: sound at levels high "
          "enough to cause physiological stress and hearing loss. Neither the source of "
          "the sound, the hour, personal dislike, nor the distance travelled is the test "
          "it gives."),

 dict(q="Which of the following does the framework list as sources of noise pollution in "
        "urban areas?",
      choices=[
        "Transportation, construction, and domestic and industrial activity",
        "Wind through open country and rainfall on bare ground",
        "Volcanic eruptions and earthquakes",
        "Photochemical reactions in the afternoon air",
        "Radon moving upward through soil into buildings"],
      ans=0,
      why="The framework names transportation, construction, and domestic and industrial "
          "activity as urban sources of noise pollution. Weather, geological events, "
          "atmospheric chemistry and radon movement are not among them."),

 dict(q="Which effects on animals in ecological systems does the framework attribute to "
        "noise pollution?",
      choices=[
        "Stress, masking of sounds used to communicate or hunt, damaged hearing, and "
        "changes to migratory routes",
        "Loss of pigmentation, thinning of eggshells, and reduced bone density",
        "Increased body size, longer lifespans, and larger litters",
        "Blindness, loss of smell, and reduced tolerance of heat",
        "Acidification of the water in which they live"],
      ans=0,
      why="Those four are the effects the framework lists for animals in ecological "
          "systems. Eggshell thinning belongs to biomagnification, and the remaining "
          "options are attributed elsewhere or not at all."),

 dict(q="Measurements from one city block are shown.",
      table=_T_SOURCES,
      choices=[
        "The loudest activity is not the one heard for the longest time, so both the "
        "level and the duration matter in describing the noise at this site",
        "The loudest activity is also the one heard for the longest time",
        "All four activities were recorded at the same sound level",
        "The quietest activity was audible for the longest time",
        "Only one of the four activities is a source the framework recognizes"],
      ans=0,
      why="The largest sound level belongs to the demolition and the longest daily "
          "exposure to the factory ventilation plant, so the two rankings differ. All "
          "four entries fall under transportation, construction, or domestic and "
          "industrial activity, which are the urban sources the framework names."),

 dict(q="A researcher claims that work at a noisy site damages hearing and offers the "
        "measurements below as evidence.",
      table=_T_HEARING,
      choices=[
        "The evidence supports the claim, because the hearing shift grows with years at "
        "the noisy site while the comparison group of the same length of service shows "
        "almost none",
        "The evidence contradicts the claim, because the comparison group shows the "
        "largest shift",
        "The evidence is irrelevant, because hearing shift is not a measure of hearing",
        "The evidence supports the claim only because the workers are older than the "
        "comparison group",
        "The evidence shows that hearing shift falls as years at the site rise"],
      ans=0,
      why="The shift rises from the shortest to the longest service at the noisy site, "
          "and the group with equally long service away from the noise shows almost "
          "none, which is what separates exposure from time alone. Hearing loss is one "
          "of the two effects in the framework's definition."),

 dict(q="An author writes that noise pollution causes physiological stress in animals "
        "and cites the measurements below.",
      table=_T_STRESS,
      choices=[
        "The measurements support the claim, because the stress hormone rises as the "
        "background sound level rises across the three enclosures",
        "The measurements refute the claim, because the loudest enclosure has the lowest "
        "hormone level",
        "The measurements are unrelated to the claim, because a hormone is not a "
        "physiological measure",
        "The measurements show the hormone falling as the sound level rises",
        "The measurements show identical hormone levels in all three enclosures"],
      ans=0,
      why="Ordering the enclosures by background sound level puts the hormone "
          "measurements in the same order, so the two rise together. Stress is one of "
          "the effects the framework attributes to noise pollution in animals, and a "
          "hormone concentration is a physiological measurement."),

 dict(q="Results from a set of listening trials are shown.",
      table=_T_MASK,
      choices=[
        "The distance over which a call can be heard falls sharply as the background "
        "sound level rises, which is the masking of sounds used to communicate",
        "The distance over which a call can be heard rises with the background sound "
        "level",
        "The background sound level has no effect on the distance in these trials",
        "The calls could be heard at the same distance in every trial",
        "The trials show that animals stop calling when the background is loud"],
      ans=0,
      why="Each increase in background level is matched by a fall in the distance at "
          "which the call is still audible. Masking of the sounds animals use to "
          "communicate or hunt is one of the effects the framework lists, and the table "
          "records audibility rather than whether the animal called."),

 dict(q="Tracking data from one migration corridor are shown.",
      table=_T_ROUTE,
      choices=[
        "The share of animals using the corridor falls as vessel traffic through it "
        "rises, which is consistent with a change in the route taken",
        "The share of animals using the corridor rises as vessel traffic rises",
        "Vessel traffic fell across the four seasons",
        "The share of animals using the corridor was the same in every season",
        "The data show that the animals cannot hear the vessels"],
      ans=0,
      why="Vessel traffic rises at every step of the record and the share of animals "
          "using the corridor falls at every step. Causing changes to migratory routes "
          "is one of the effects the framework lists for noise pollution in ecological "
          "systems, and the data cannot show what the animals hear."),

 dict(q="Results from a hunting experiment are shown.",
      table=_T_HUNT,
      choices=[
        "Both detections of prey and successful captures fell when traffic noise was "
        "played, which is consistent with the masking of sounds used to hunt",
        "Detections fell but captures rose when traffic noise was played",
        "Both detections and captures rose when traffic noise was played",
        "Neither measurement changed between the two conditions",
        "The experiment shows that the animal hunts only in loud conditions"],
      ans=0,
      why="Both columns are smaller in the noise condition than in the quiet condition. "
          "The framework lists the masking of sounds used to communicate or hunt among "
          "the effects of noise pollution on animals, and a fall in detections alongside "
          "a fall in captures is what masking would produce."),

 dict(q="A city planner argues that a proposed elevated highway would add noise "
        "pollution to a residential district. Which piece of evidence would most "
        "directly support that argument?",
      choices=[
        "Measurements of sound levels beside existing highways of the same design, taken "
        "in comparable residential districts",
        "The number of vehicles registered in the city as a whole",
        "The cost of building the highway compared with other projects",
        "The average commuting time saved by drivers using the highway",
        "The number of residents who say they support the project"],
      ans=0,
      why="Suggested skill 3.C. The claim is about sound reaching a district, so the "
          "evidence that bears on it is a measurement of sound beside comparable roads. "
          "Registration counts, construction cost, travel time and opinion do not "
          "measure the sound."),

 dict(q="Which of the following would be classified as a transportation source of urban "
        "noise pollution?",
      choices=[
        "Traffic on a busy arterial road running through a neighborhood",
        "A pile driver working on a building foundation",
        "A stamping press operating inside a factory",
        "A household air conditioner heard through a shared wall",
        "A ventilation fan on the roof of an apartment block"],
      ans=0,
      why="The framework lists transportation among the urban sources of noise "
          "pollution, and road traffic is transportation. The pile driver is "
          "construction, the press is industrial activity, and the air conditioner and "
          "the fan are domestic and building activity."),

 dict(q="A study reports that residents near a construction site show raised blood "
        "pressure and disturbed sleep during the months the site is active. How does "
        "this evidence relate to the framework's definition of noise pollution?",
      choices=[
        "It reports the physiological stress that the definition uses to identify sound "
        "as noise pollution",
        "It reports hearing loss, which is the only effect in the definition",
        "It is irrelevant, because the definition concerns only animals",
        "It is irrelevant, because construction is not a source the framework recognizes",
        "It shows that the sound level must be below the level of ordinary conversation"],
      ans=0,
      why="The framework defines noise pollution as sound at levels high enough to cause "
          "physiological stress and hearing loss, so raised blood pressure and disturbed "
          "sleep are the stress half of that definition. Construction is one of the "
          "urban sources it names."),

 dict(q="An author claims that noise pollution can affect an animal population even "
        "where no individual loses its hearing. Which reasoning best supports the claim?",
      choices=[
        "The framework lists stress, masking of communication and hunting sounds, and "
        "changes to migratory routes as separate effects from damaged hearing",
        "The framework treats hearing loss as the only possible effect on animals",
        "The framework says that animals are unaffected by sound below a fixed level",
        "The framework says that noise pollution acts only on migrating species",
        "The framework says that noise pollution has no effects on ecological systems"],
      ans=0,
      why="The framework's list contains four effects, and only one of them is damaged "
          "hearing, so effects on a population do not require that one. It sets no fixed "
          "level and confines the effects to no particular kind of species."),

 dict(q="Which observation would most weaken a claim that a factory is the source of the "
        "noise disturbing a neighborhood?",
      choices=[
        "Sound levels in the neighborhood are the same on days when the factory is shut "
        "as on days when it is running",
        "The factory is the largest building in the neighborhood",
        "Residents dislike the appearance of the factory",
        "The factory employs many people who live elsewhere",
        "The factory was built more recently than the houses around it"],
      ans=0,
      why="Suggested skill 3.C. If the measured sound does not change when the suspected "
          "source stops, the source is not accounting for it. Building size, appearance, "
          "employment and construction date bear on none of the sound measurements."),

 dict(q="A researcher reports that birds in a noisy area sing at times of day when the "
        "traffic is lighter. Which framework effect does this observation most directly "
        "concern?",
      choices=[
        "The masking of sounds used to communicate",
        "The corrosion of human-made structures",
        "The acidification of soils and water",
        "Radon-induced illness in the animals",
        "The trapping of pollutants near the ground"],
      ans=0,
      why="Singing when the background is quieter concerns whether the sound can be "
          "heard, which is the masking of sounds used to communicate that the framework "
          "lists among the effects of noise pollution. The other options belong to acid "
          "deposition, indoor air pollution and thermal inversion."),

 dict(q="Which of the following best explains why the framework defines noise pollution "
        "by its effects rather than by the kind of activity making the sound?",
      choices=[
        "The same activity can produce sound that is harmful or harmless depending on "
        "how loud it is, so the definition turns on whether it reaches levels that cause "
        "stress and hearing loss",
        "The framework has not identified any sources of noise pollution",
        "Only sounds produced by machines can be harmful",
        "All sound is equally harmful regardless of its level",
        "The framework treats noise as harmful only when it is produced deliberately"],
      ans=0,
      why="The framework's definition is about levels high enough to cause physiological "
          "stress and hearing loss, and it separately lists the urban activities that "
          "produce such sound. The definition therefore depends on the level reached "
          "rather than on the identity of the activity."),

 dict(q="Two neighborhoods report the same average sound level, but only one reports "
        "widespread sleep disturbance. Which additional measurement would be most useful "
        "in explaining the difference?",
      choices=[
        "The sound levels recorded in each neighborhood hour by hour, including at night",
        "The total population of each neighborhood",
        "The number of parks in each neighborhood",
        "The average age of the buildings in each neighborhood",
        "The distance from each neighborhood to the city center"],
      ans=0,
      why="Suggested skill 3.C. An average conceals when the sound occurs, and a claim "
          "about sleep concerns the night hours specifically, so the hourly record is "
          "what could distinguish the two. Population, parks, building age and distance "
          "do not describe the sound."),

 dict(q="Which of the following is the best example of noise pollution from domestic "
        "activity as the framework uses the term?",
      choices=[
        "Sound from appliances, equipment and gatherings in homes, carrying to "
        "neighboring residences",
        "Sound from a passenger train passing on an elevated line",
        "Sound from a jackhammer breaking a street surface",
        "Sound from a metal foundry operating overnight",
        "Sound from a helicopter landing at a hospital"],
      ans=0,
      why="The framework lists domestic activity alongside transportation, construction "
          "and industrial activity as urban sources, and the domestic category is the "
          "activity of households. Trains and helicopters are transportation, the "
          "jackhammer is construction, and the foundry is industrial."),

 dict(q="A conservation group argues that shipping noise is altering where a migrating "
        "population travels. Which evidence would support that argument most directly?",
      choices=[
        "Tracking data showing that the share of the population using a corridor changes "
        "as vessel traffic through that corridor changes",
        "Photographs showing that vessels are large",
        "Records showing that shipping companies operate year-round",
        "Interviews with sailors who have seen the animals",
        "Charts showing the depth of the water in the corridor"],
      ans=0,
      why="Suggested skill 3.C. The claim is that the route changes with the noise, so "
          "the supporting evidence pairs route use with the traffic producing the noise. "
          "Vessel size, company schedules, sightings and water depth leave the pairing "
          "unmade."),

 dict(q="Why can a sound that is not loud enough to damage hearing still count as noise "
        "pollution under the framework's definition?",
      choices=[
        "The definition covers sound at levels high enough to cause physiological "
        "stress as well as sound that causes hearing loss",
        "The definition covers any sound that is audible indoors",
        "The definition covers only sounds produced at night",
        "The definition covers only sounds produced by transportation",
        "The definition requires both effects to occur in the same person"],
      ans=0,
      why="The framework's definition names physiological stress and hearing loss, so "
          "sound reaching the level that causes stress falls within it. Audibility, hour "
          "of day and source are not part of the definition, and it does not require "
          "both effects at once."),

 dict(q="An author claims that a new sound barrier beside a highway has reduced noise "
        "pollution in the houses behind it. Which measurement would best test the claim?",
      choices=[
        "Sound levels measured in those houses before and after the barrier was built, "
        "with traffic volumes recorded for both periods",
        "The height and length of the barrier",
        "The number of houses behind the barrier",
        "The cost of building the barrier",
        "The number of complaints made before the barrier was built"],
      ans=0,
      why="Suggested skill 3.C. A before-and-after comparison of the sound in the "
          "affected houses, with the traffic recorded so a change in traffic cannot be "
          "mistaken for a change in shielding, is what tests the claim. The barrier's "
          "dimensions, the house count and the cost measure no sound."),

 dict(q="Which statement best describes what an animal loses when noise masks the sounds "
        "it uses to hunt?",
      choices=[
        "The information it would otherwise obtain from sounds made by prey or by other "
        "animals",
        "Its ability to see prey at a distance",
        "The nutrients it obtains from the prey it has already eaten",
        "Its tolerance for cold temperatures",
        "The capacity to store fat before migration"],
      ans=0,
      why="Masking is an effect on what can be heard, so what is lost is the information "
          "carried by the sound. The framework lists the masking of sounds used to "
          "communicate or hunt and attributes no effect on vision, digestion, thermal "
          "tolerance or fat storage to noise."),

 dict(q="A city measures sound at one intersection for ten minutes in the middle of the "
        "night and concludes that the district has no noise pollution problem. What is "
        "the clearest weakness in that reasoning?",
      choices=[
        "A brief sample at one place and one hour cannot represent the sound the district "
        "experiences over a day",
        "Sound cannot be measured at night with any instrument",
        "Sound should have been measured in decibels rather than in another unit",
        "The measurement should have been taken indoors instead",
        "Noise pollution can only be assessed by asking residents"],
      ans=0,
      why="Suggested skill 3.C. A conclusion about a district over time needs samples "
          "that represent it, and one short reading at one point does not. The "
          "instrument, the unit and the choice of an outdoor site are not the flaw."),

 dict(q="Which pairing of an urban activity with the framework's source category is "
        "correct?",
      choices=[
        "A road rebuilding project, construction",
        "A road rebuilding project, transportation",
        "A city bus route, industrial activity",
        "A rooftop compressor on a factory, domestic activity",
        "A neighbor's stereo, construction"],
      ans=0,
      why="The framework's urban categories are transportation, construction, and "
          "domestic and industrial activity. Rebuilding a road is construction work, a "
          "bus route is transportation, a factory compressor is industrial, and a "
          "neighbor's stereo is domestic."),

 dict(q="A study finds that animals in a noisy enclosure show raised stress hormones and "
        "also eat less. Which conclusion is best supported by the framework?",
      choices=[
        "Noise pollution can cause stress in animals, and the study measured one "
        "physiological sign of it",
        "Noise pollution acts only on hearing and cannot affect any other system",
        "The animals' hearing must already have been damaged",
        "The animals' migratory route must have changed",
        "Noise pollution has no effects that can be measured"],
      ans=0,
      why="Stress is the first effect the framework lists for animals in ecological "
          "systems, and a stress hormone is a physiological measurement of it. Damaged "
          "hearing and changed migratory routes are separate effects that this study "
          "does not measure."),

 dict(q="Why does the framework treat noise pollution alongside other kinds of air "
        "pollution in this unit?",
      choices=[
        "It is a consequence of human activity that travels through the air and harms "
        "people and other organisms",
        "It is a chemical released by combustion",
        "It is a particulate that can be collected on a filter",
        "It is produced only by the same sources that release sulfur dioxide",
        "It changes the temperature profile of the atmosphere"],
      ans=0,
      why="The unit's enduring understanding is that human activities have consequences "
          "for the atmosphere, and noise pollution is sound produced by human activity "
          "that reaches people and animals through the air. It is not a chemical, not a "
          "particle, and not a temperature effect."),

 dict(q="An author claims that a proposed nighttime curfew on construction would reduce "
        "noise pollution. Which evidence would most strengthen the claim?",
      choices=[
        "Sound measurements showing that construction activity is the largest contributor "
        "to nighttime sound levels in the affected area",
        "Evidence that construction workers prefer to work during the day",
        "Evidence that the city has many construction sites",
        "Evidence that construction is expensive",
        "Evidence that residents in another city support a similar rule"],
      ans=0,
      why="Suggested skill 3.C. The claim is that removing nighttime construction lowers "
          "the noise, so the evidence that supports it identifies construction as the "
          "dominant nighttime contributor. Preferences, site counts, costs and opinions "
          "elsewhere do not."),

 dict(q="Which of the following best distinguishes the framework's two named effects on "
        "people from its named effects on animals in ecological systems?",
      choices=[
        "For people the framework names physiological stress and hearing loss, while for "
        "animals it adds masking of communication and hunting sounds and changes to "
        "migratory routes",
        "For people the framework names only hearing loss, while for animals it names "
        "only stress",
        "The framework names identical effects for people and for animals",
        "The framework names effects only for people and none for animals",
        "The framework names effects only for animals and none for people"],
      ans=0,
      why="The definition of noise pollution names physiological stress and hearing "
          "loss, and the separate statement about animals in ecological systems adds "
          "masking and changes to migratory routes to stress and damaged hearing. Both "
          "sets exist and they are not identical."),

 dict(q="Which summary best captures the framework's treatment of noise pollution?",
      choices=[
        "Sound loud enough to cause physiological stress and hearing loss, produced in "
        "urban areas by transportation, construction and domestic and industrial "
        "activity, and affecting animals through stress, masking, damaged hearing and "
        "changed migratory routes",
        "Any unwanted sound, produced mainly by natural sources, with effects limited to "
        "human annoyance",
        "Sound produced only by industry, affecting only the workers who hear it",
        "Sound that damages buildings but has no effect on living organisms",
        "Sound that becomes harmful only when it is trapped by a thermal inversion"],
      ans=0,
      why="Each clause of the keyed summary is one of the framework's three statements: "
          "the definition, the urban sources, and the effects on animals in ecological "
          "systems. Every rejected summary contradicts at least one of them."),

 dict(q="A team wants to distinguish damaged hearing from physiological stress in a "
        "group of people working near a loud machine. Which measurement would show "
        "damaged hearing specifically?",
      choices=[
        "The quietest sound each worker can detect, measured before the period of "
        "exposure and again afterward",
        "The stress hormone concentration in each worker's blood at the end of the shift",
        "Each worker's blood pressure recorded once during the shift",
        "The sound level at the machine, recorded without measuring any worker",
        "A survey asking each worker how annoying the machine is"],
      ans=0,
      why="Hearing loss is a change in what a person can hear, so the measurement that "
          "shows it is the faintest detectable sound compared before and after exposure. "
          "Hormones and blood pressure are measures of the stress the framework names "
          "separately, and a sound level or a survey measures neither effect."),
]
