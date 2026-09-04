# AP ENVIRONMENTAL SCIENCE 8.11 Sewage Treatment
# CED effective Fall 2026, Unit 8 Aquatic and Terrestrial Pollution. Enduring
# understanding STB-3. Learning objective STB-3.N: describe best practices in sewage
# treatment. Suggested skill 2.A, describe characteristics of an environmental concept,
# process, or model represented visually.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-3.N.1  Primary treatment of sewage is the physical removal of large objects, often
#              through the use of screens and grates, followed by the settling of solid
#              waste in the bottom of a tank.
#   STB-3.N.2  Secondary treatment is a biological process in which bacteria break down
#              organic matter into carbon dioxide and inorganic sludge, which settles in
#              the bottom of a tank. The tank is aerated to increase the rate at which the
#              bacteria break down the organic matter.
#   STB-3.N.3  Tertiary treatment is the use of ecological or chemical processes to remove
#              any pollutants left in the water after primary and secondary treatment.
#   STB-3.N.4  Prior to discharge, the treated water is exposed to one or more
#              disinfectants (usually, chlorine, ozone, or UV light) to kill bacteria.
#
# ON SCOPE. Topic 8.5 keys eutrophication and names wastewater release as one of its
# anthropogenic causes (STB-3.F.5); topic 8.14 keys dysentery from untreated sewage
# (EIN-3.C.2). Nothing here re-asks either. Every key rests on what a stage of treatment
# is or does.
#
# ON THE FIGURES. Suggested skill 2.A is about a process represented visually and the
# bank carries no images, so every representation here is a table and every keyed reading
# is recomputed in verify_e8_11.py from that table alone. No stem refers to a diagram.
#
# NOT KEYED: no residence time, no discharge limit, no dose of any disinfectant and no
# named plant. The framework states none of them.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII.
TOPIC = ("8.11", "Sewage Treatment", 8)

_T_STAGES = dict(
    headers=["Point in the treatment plant",
             "Suspended solids (milligrams per liter)",
             "Organic matter measured as oxygen demand (milligrams per liter)",
             "Bacteria (colonies per hundred milliliters)"],
    rows=[["Raw sewage entering the plant", "240", "200", "2000000"],
          ["After primary treatment", "120", "150", "1800000"],
          ["After secondary treatment", "20", "20", "400000"],
          ["After tertiary treatment", "5.0", "8.0", "300000"],
          ["After the disinfection step", "5.0", "8.0", "20"]])

_T_PRIMARY = dict(
    headers=["Material arriving at the plant each day",
             "Mass taken out by the screens, grates and settling tank (kilograms)",
             "Mass still in the water after primary treatment (kilograms)"],
    rows=[["Rags and plastic objects", "310", "5.0"],
          ["Grit and sand", "540", "20"],
          ["Dissolved organic matter", "0", "1800"]])

_T_AERATION = dict(
    headers=["Secondary tank in a side by side trial",
             "Air pumped into the tank (cubic meters per hour)",
             "Organic matter broken down in eight hours (percent)"],
    rows=[["Tank A", "0", "22"],
          ["Tank B", "50", "58"],
          ["Tank C", "120", "84"]])

_T_TERTIARY = dict(
    headers=["Substance measured in the water",
             "Concentration after secondary treatment (milligrams per liter)",
             "Concentration after tertiary treatment (milligrams per liter)"],
    rows=[["Nitrogen", "18", "3.0"],
          ["Phosphorus", "6.0", "0.50"],
          ["Suspended solids", "20", "4.0"]])

_T_DISINFECT = dict(
    headers=["Treatment applied to the water before discharge",
             "Bacteria before the step (colonies per hundred milliliters)",
             "Bacteria after the step (colonies per hundred milliliters)"],
    rows=[["Chlorine", "300000", "15"],
          ["Ozone", "300000", "22"],
          ["Ultraviolet light", "300000", "30"],
          ["No disinfectant applied", "300000", "290000"]])

_T_PLANTS = dict(
    headers=["Plant discharging to the same river",
             "Number of treatment stages used before discharge",
             "Nitrogen remaining in the discharge (milligrams per liter)"],
    rows=[["Plant 1", "1", "32"],
          ["Plant 2", "2", "17"],
          ["Plant 3", "3", "3.0"]])

QUESTIONS = [

 dict(q="How does the framework describe primary treatment of sewage?",
      choices=[
        "The physical removal of large objects, often with screens and grates, followed by "
        "the settling of solid waste in the bottom of a tank",
        "A biological process in which bacteria break down organic matter into carbon "
        "dioxide and inorganic sludge",
        "The use of ecological or chemical processes to remove whatever pollutants remain "
        "in the water",
        "Exposure of the water to chlorine, ozone or ultraviolet light to kill bacteria",
        "The evaporation of the water so that only dry solids are left behind"],
      ans=0,
      why="STB-3.N.1 states that primary treatment is the physical removal of large "
          "objects, often through the use of screens and grates, followed by the settling "
          "of solid waste in the bottom of a tank. The rejected options state STB-3.N.2, "
          "STB-3.N.3 and STB-3.N.4."),

 dict(q="How does the framework describe secondary treatment?",
      choices=[
        "A biological process in which bacteria break down organic matter into carbon "
        "dioxide and inorganic sludge that settles in the bottom of a tank",
        "The physical removal of large objects with screens and grates",
        "The use of ecological or chemical processes to remove whatever pollutants remain",
        "Exposure of the water to a disinfectant to kill bacteria before discharge",
        "The pumping of untreated sewage directly into a river"],
      ans=0,
      why="STB-3.N.2 states that secondary treatment is a biological process in which "
          "bacteria break down organic matter into carbon dioxide and inorganic sludge, "
          "which settles in the bottom of a tank. The rejected options state the other "
          "stages or no treatment at all."),

 dict(q="How does the framework describe tertiary treatment?",
      choices=[
        "The use of ecological or chemical processes to remove any pollutants left in the "
        "water after primary and secondary treatment",
        "The physical removal of large objects with screens and grates",
        "A biological process carried out by bacteria in an aerated tank",
        "The application of a disinfectant immediately before the water is discharged",
        "The return of sludge to the head of the plant for a second pass"],
      ans=0,
      why="STB-3.N.3 states that tertiary treatment is the use of ecological or chemical "
          "processes to remove any pollutants left in the water after primary and "
          "secondary treatment. The rejected options describe the other stages."),

 dict(q="Water was sampled at several points through one treatment plant.",
      table=_T_STAGES,
      choices=[
        "Solids and organic matter fall across the earlier stages, but the bacteria count "
        "only collapses at the last step",
        "The bacteria count collapses during primary treatment and changes little "
        "afterward",
        "Solids and organic matter are unchanged from the raw sewage to the discharge",
        "The bacteria count rises at every stage of the plant",
        "Every measured quantity reaches its lowest value immediately after primary "
        "treatment"],
      ans=0,
      why="The solids and oxygen demand columns fall sharply through the first three "
          "stages while the bacteria column stays in the hundreds of thousands until the "
          "final row, where it falls to a small number. STB-3.N.4 places a disinfectant "
          "step prior to discharge to kill bacteria."),

 dict(q="Which disinfectants does the framework name as usual choices before discharge?",
      choices=[
        "Chlorine, ozone or ultraviolet light",
        "Nitrogen, phosphorus or potassium",
        "Lead, mercury or cadmium",
        "Sand, gravel or clay",
        "Methane, carbon dioxide or nitrous oxide"],
      ans=0,
      why="STB-3.N.4 states that prior to discharge the treated water is exposed to one or "
          "more disinfectants, usually chlorine, ozone or ultraviolet light, to kill "
          "bacteria. The rejected options list nutrients, heavy metals, filter media and "
          "gases."),

 dict(q="Why does the framework say the secondary treatment tank is aerated?",
      choices=[
        "To increase the rate at which the bacteria break down the organic matter",
        "To kill the bacteria before the water is discharged",
        "To float the large objects so that screens can catch them",
        "To cool the water so that the sludge settles faster",
        "To add nutrients that the bacteria require as food"],
      ans=0,
      why="STB-3.N.2 states that the tank is aerated to increase the rate at which the "
          "bacteria break down the organic matter. Killing bacteria is the disinfection "
          "step of STB-3.N.4, and screening is the physical step of STB-3.N.1."),

 dict(q="Into what does the framework say the bacteria in secondary treatment break "
        "organic matter down?",
      choices=[
        "Carbon dioxide and inorganic sludge",
        "Chlorine and ozone",
        "Nitrogen gas and pure water",
        "Rags, grit and sand",
        "Methane and fertilizer pellets"],
      ans=0,
      why="STB-3.N.2 states that bacteria break down organic matter into carbon dioxide "
          "and inorganic sludge, which settles in the bottom of a tank. The rejected "
          "options name disinfectants, an unstated product, the material of primary "
          "treatment and products the framework does not attribute to this stage."),

 dict(q="What one plant's screens, grates and settling tank removed in a day is compared "
        "with what stayed in the water.",
      table=_T_PRIMARY,
      choices=[
        "The rags and the grit were almost entirely taken out, while nearly all the "
        "dissolved organic matter stayed in the water",
        "The dissolved organic matter was almost entirely taken out while the rags stayed "
        "in the water",
        "All three materials were removed to the same extent",
        "None of the three materials was removed at all",
        "The grit stayed in the water while the dissolved organic matter was removed"],
      ans=0,
      why="The two rows of solid material carry large removed masses and small remaining "
          "masses, while the dissolved organic matter row carries no removal at all. "
          "STB-3.N.1 makes primary treatment a physical removal of large objects and "
          "settleable solids, and STB-3.N.2 assigns the organic matter to the biological "
          "stage."),

 dict(q="In what order does the framework place the stages of sewage treatment?",
      choices=[
        "Primary, then secondary, then tertiary, with disinfection prior to discharge",
        "Disinfection, then primary, then secondary, then tertiary",
        "Tertiary, then secondary, then primary, with disinfection first",
        "Secondary, then primary, then disinfection, with tertiary last",
        "Disinfection alone, since the other stages are optional"],
      ans=0,
      why="STB-3.N.3 describes tertiary treatment as removing pollutants left after "
          "primary and secondary treatment, which fixes those three in order, and "
          "STB-3.N.4 places the disinfectant step prior to discharge."),

 dict(q="What does the framework say happens to the solid waste during primary treatment?",
      choices=[
        "It settles in the bottom of a tank after the large objects have been screened out",
        "It is broken down into carbon dioxide by bacteria",
        "It is killed by exposure to chlorine or ultraviolet light",
        "It is removed by ecological or chemical processes designed for leftover pollutants",
        "It is dissolved into the water and discharged with it"],
      ans=0,
      why="STB-3.N.1 states that primary treatment is the physical removal of large "
          "objects, often through screens and grates, followed by the settling of solid "
          "waste in the bottom of a tank. Bacterial breakdown is STB-3.N.2 and "
          "disinfection is STB-3.N.4."),

 dict(q="What is the stated purpose of exposing the treated water to a disinfectant?",
      choices=[
        "To kill bacteria before the water is discharged",
        "To settle the remaining solids to the bottom of a tank",
        "To feed the bacteria that break down organic matter",
        "To screen out the large objects that arrived with the sewage",
        "To warm the water so that it mixes with the receiving river"],
      ans=0,
      why="STB-3.N.4 states that prior to discharge the treated water is exposed to one or "
          "more disinfectants to kill bacteria. Settling belongs to STB-3.N.1 and feeding "
          "the bacteria would work against the stated purpose."),

 dict(q="Three secondary tanks were run side by side with different amounts of air.",
      table=_T_AERATION,
      choices=[
        "The more air pumped into a tank, the greater the share of organic matter broken "
        "down in eight hours",
        "The more air pumped into a tank, the smaller the share of organic matter broken "
        "down",
        "All three tanks broke down the same share of the organic matter",
        "The tank with no air broke down the largest share",
        "The amount of air makes no difference to the share broken down in these data"],
      ans=0,
      why="Ranking the tanks by air supplied gives the same order as ranking them by the "
          "share broken down. STB-3.N.2 states that the tank is aerated to increase the "
          "rate at which the bacteria break down the organic matter."),

 dict(q="A plant operator wants to keep rags and grit out of the rest of the plant. Which "
        "stage does that work belong to?",
      choices=[
        "Primary treatment, which physically removes large objects with screens and grates",
        "Secondary treatment, which uses bacteria in an aerated tank",
        "Tertiary treatment, which uses ecological or chemical processes",
        "Disinfection, which exposes the water to chlorine, ozone or ultraviolet light",
        "None of the stages, since rags and grit are not removed at a treatment plant"],
      ans=0,
      why="STB-3.N.1 assigns the physical removal of large objects, often through the use "
          "of screens and grates, to primary treatment. The other stages are biological, "
          "chemical or ecological, and disinfection targets bacteria."),

 dict(q="Which stage does the framework describe as a biological process?",
      choices=[
        "Secondary treatment, carried out by bacteria",
        "Primary treatment, carried out by screens and grates",
        "Tertiary treatment, carried out by ecological or chemical processes",
        "The disinfection step, carried out with chlorine or ozone",
        "None of the stages, since all of them are purely physical"],
      ans=0,
      why="STB-3.N.2 calls secondary treatment a biological process in which bacteria "
          "break down organic matter. STB-3.N.1 is physical, STB-3.N.3 is ecological or "
          "chemical, and STB-3.N.4 applies a disinfectant."),

 dict(q="Why does the framework describe tertiary treatment as using ecological or "
        "chemical processes rather than naming a single method?",
      choices=[
        "Its job is to remove whatever pollutants are still left after the first two "
        "stages, and different leftover pollutants call for different processes",
        "Its job is to remove the large objects that the screens missed",
        "Its job is to kill the bacteria that survived secondary treatment",
        "Its job is to aerate the tank so that bacteria work faster",
        "Its job is to return the sludge to the head of the plant"],
      ans=0,
      why="STB-3.N.3 defines tertiary treatment by the pollutants left in the water after "
          "primary and secondary treatment and describes the means as ecological or "
          "chemical processes rather than one fixed technique."),

 dict(q="Water leaving one plant's secondary stage was compared with the same water after "
        "the next stage.",
      table=_T_TERTIARY,
      choices=[
        "Every substance measured fell substantially between the two stages, which is what "
        "a stage aimed at leftover pollutants would do",
        "Every substance measured rose between the two stages",
        "The substances were unchanged between the two stages",
        "Only one of the three substances fell between the two stages",
        "The substance present in the largest amount after secondary treatment was the "
        "only one that did not fall"],
      ans=0,
      why="Each row's second value is a fraction of its first, so all three substances "
          "fall. STB-3.N.3 states that tertiary treatment uses ecological or chemical "
          "processes to remove any pollutants left in the water after primary and "
          "secondary treatment."),

 dict(q="A plant discharges water that is clear and low in organic matter but still "
        "carries very high numbers of bacteria. Which step has most likely failed?",
      choices=[
        "The disinfection applied prior to discharge",
        "The screens and grates of primary treatment",
        "The settling tank of primary treatment",
        "The aeration of the secondary tank",
        "The ecological or chemical processes of tertiary treatment"],
      ans=0,
      why="STB-3.N.4 assigns the killing of bacteria to the disinfectant applied prior to "
          "discharge, and the other measurements show that the physical and biological "
          "stages have done their own work."),

 dict(q="A plant removes rags, grit and settleable solids but its discharge is still very "
        "high in dissolved organic matter. Which stage is most likely missing or failing?",
      choices=[
        "Secondary treatment, in which bacteria break the organic matter down",
        "Primary treatment, which removes large objects and settleable solids",
        "The disinfection step applied before discharge",
        "The screening of the incoming flow",
        "No stage, since organic matter is not removed at a treatment plant"],
      ans=0,
      why="STB-3.N.1 covers the physical removal that has plainly worked, and STB-3.N.2 "
          "assigns the breakdown of organic matter to the bacteria of secondary treatment, "
          "so that is the stage the result points to."),

 dict(q="Which of the following is NOT one of the disinfectants the framework names?",
      choices=[
        "Powdered lime added to the settling tank",
        "Chlorine",
        "Ozone",
        "Ultraviolet light",
        "A combination of two of the disinfectants the framework names"],
      ans=0,
      why="STB-3.N.4 names chlorine, ozone and ultraviolet light and states that the water "
          "is exposed to one or more of them, so a combination is allowed by the "
          "statement. Lime added to a settling tank appears nowhere in the framework's "
          "sewage treatment statements."),

 dict(q="Four batches of the same water were handled differently before discharge.",
      table=_T_DISINFECT,
      choices=[
        "Each of the three named disinfectants cut the bacteria to a tiny fraction of the "
        "starting count, while the untreated batch barely changed",
        "The untreated batch showed the largest reduction in bacteria",
        "All four batches finished with about the same bacteria count",
        "Only one of the three named disinfectants reduced the bacteria count",
        "The three named disinfectants raised the bacteria count"],
      ans=0,
      why="The three named disinfectant rows finish at a few tens of colonies from a "
          "shared starting value in the hundreds of thousands, while the untreated row is "
          "almost unchanged. STB-3.N.4 names chlorine, ozone and ultraviolet light as the "
          "usual disinfectants applied to kill bacteria."),

 dict(q="Which pairing of a stage with its defining feature is correct?",
      choices=[
        "Secondary treatment, paired with bacteria breaking organic matter down in an "
        "aerated tank",
        "Secondary treatment, paired with screens and grates removing large objects",
        "Primary treatment, paired with ecological or chemical removal of leftover "
        "pollutants",
        "Tertiary treatment, paired with the killing of bacteria before discharge",
        "Disinfection, paired with the settling of solid waste in the bottom of a tank"],
      ans=0,
      why="STB-3.N.2 gives secondary treatment its bacteria and its aerated tank, "
          "STB-3.N.1 gives primary treatment its screens, grates and settling, STB-3.N.3 "
          "gives tertiary treatment its ecological or chemical removal, and STB-3.N.4 "
          "gives disinfection the killing of bacteria. Each rejected pairing crosses two "
          "of those."),

 dict(q="Why is primary treatment alone not enough to protect a receiving river, on the "
        "framework's account of the stages?",
      choices=[
        "It removes only what can be screened out or settled, leaving the dissolved "
        "organic matter and the bacteria for the later stages",
        "It removes the bacteria but leaves every solid object in the water",
        "It removes all the organic matter but leaves the grit behind",
        "It adds pollutants to the water rather than removing any",
        "It is the only stage the framework describes, so nothing is left out"],
      ans=0,
      why="STB-3.N.1 limits primary treatment to physical removal and settling, STB-3.N.2 "
          "assigns organic matter to bacteria in the secondary stage, and STB-3.N.4 "
          "assigns bacteria to the disinfectant before discharge."),

 dict(q="Which measurement would best show that a plant's secondary treatment is working?",
      choices=[
        "The organic matter in the water, measured before and after the aerated tank",
        "The number of large objects caught on the incoming screens",
        "The bacteria count measured after the disinfectant is applied",
        "The volume of the settling tank in cubic meters",
        "The number of pipes leaving the plant"],
      ans=0,
      why="STB-3.N.2 makes the breakdown of organic matter by bacteria the work of "
          "secondary treatment, so a before and after measurement of organic matter across "
          "that tank is the direct test. Screenings belong to STB-3.N.1 and the bacteria "
          "count after disinfection to STB-3.N.4."),

 dict(q="Three plants on one river use different numbers of treatment stages.",
      table=_T_PLANTS,
      choices=[
        "The more stages a plant uses, the less nitrogen remains in its discharge",
        "The more stages a plant uses, the more nitrogen remains in its discharge",
        "All three plants discharge the same amount of nitrogen",
        "The plant using the fewest stages discharges the least nitrogen",
        "The number of stages tells nothing about the discharge in these data"],
      ans=0,
      why="Ranking the plants by the number of stages gives the reverse of the order by "
          "nitrogen remaining. STB-3.N.3 states that tertiary treatment removes pollutants "
          "left in the water after primary and secondary treatment."),

 dict(q="Why does the framework call the second stage biological when the first and third "
        "are not described that way?",
      choices=[
        "Living bacteria do the work of breaking the organic matter down in that stage",
        "The water is filtered through a bed of living plants in that stage",
        "The stage is carried out only during the growing season",
        "The stage removes only material that was once alive, whatever does the removing",
        "The stage uses a chemical that is manufactured by living organisms"],
      ans=0,
      why="STB-3.N.2 calls secondary treatment a biological process in which bacteria "
          "break down organic matter, so the agent of the process is what makes it "
          "biological. STB-3.N.1 is physical and STB-3.N.3 is ecological or chemical."),

 dict(q="What does the framework say happens to the inorganic sludge produced in secondary "
        "treatment?",
      choices=[
        "It settles in the bottom of a tank",
        "It is discharged to the river with the treated water",
        "It is converted into chlorine for the disinfection step",
        "It floats to the surface and is skimmed away with the large objects",
        "It is broken down further into large objects that screens can catch"],
      ans=0,
      why="STB-3.N.2 states that bacteria break down organic matter into carbon dioxide "
          "and inorganic sludge, which settles in the bottom of a tank. The framework "
          "makes no statement about discharging the sludge or converting it."),

 dict(q="An engineer wants to know whether adding more air to a secondary tank speeds up "
        "treatment. Which comparison tests that directly?",
      choices=[
        "Identical tanks run at several different air supply rates, with the organic "
        "matter broken down in a fixed time recorded for each",
        "One tank run at a single air supply rate for one day",
        "The number of screens installed at the head of the plant",
        "The bacteria count in the water after the disinfectant is applied",
        "The nitrogen concentration in the river upstream of the plant"],
      ans=0,
      why="STB-3.N.2 states that the tank is aerated to increase the rate at which the "
          "bacteria break down the organic matter, so varying the air and measuring the "
          "breakdown is what tests the claim. A single condition provides no comparison."),

 dict(q="Why does the framework place the disinfection step prior to discharge rather than "
        "at the head of the plant?",
      choices=[
        "Its purpose is to kill bacteria in the water that is about to leave the plant, "
        "after the other stages have done their work",
        "Its purpose is to kill the bacteria that secondary treatment depends on before "
        "they can act",
        "Its purpose is to remove the large objects before the screens are reached",
        "Its purpose is to settle the solids before the tank is filled",
        "Its purpose is to warm the incoming sewage so that it flows faster"],
      ans=0,
      why="STB-3.N.4 states that prior to discharge the treated water is exposed to one or "
          "more disinfectants to kill bacteria, and STB-3.N.2 depends on living bacteria "
          "doing the breakdown, so disinfecting first would remove the agent of the "
          "biological stage."),

 dict(q="A plant's discharge still carries nutrients after its bacteria have broken down "
        "the organic matter. Which stage does the framework assign to that remaining "
        "problem?",
      choices=[
        "Tertiary treatment, using ecological or chemical processes on what is left",
        "Primary treatment, using screens and grates on what is left",
        "A second pass through the aerated tank",
        "The disinfection step applied prior to discharge",
        "No stage, since nutrients are not treated at a sewage plant"],
      ans=0,
      why="STB-3.N.3 states that tertiary treatment is the use of ecological or chemical "
          "processes to remove any pollutants left in the water after primary and "
          "secondary treatment, which is exactly the situation described."),

 dict(q="Which summary best captures this topic?",
      choices=[
        "Large objects are screened out and solids settle, bacteria in an aerated tank then "
        "break the organic matter into carbon dioxide and sludge, ecological or chemical "
        "processes remove what is still left, and a disinfectant kills bacteria before the "
        "water is discharged",
        "Bacteria are killed first, then the organic matter is screened out, and no further "
        "treatment is needed",
        "All three stages are physical processes and no living organism is involved at any "
        "point",
        "Sewage is discharged to a river without treatment and the river completes the "
        "process",
        "Disinfection removes the solids and the settling tank kills the bacteria"],
      ans=0,
      why="Each clause of the keyed summary is one of STB-3.N.1 through STB-3.N.4 in the "
          "order the framework gives them. Every rejected summary reverses the order, "
          "denies the biological stage, or assigns a stage the wrong job."),
]
