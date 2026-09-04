# AP ENVIRONMENTAL SCIENCE 8.7 Persistent Organic Pollutants (POPs)
# CED effective Fall 2026, Unit 8 Aquatic and Terrestrial Pollution. Enduring
# understanding STB-3. Learning objective STB-3.H: describe the effect of persistent
# organic pollutants (POPs) on ecosystems. Suggested skill 1.B, explain environmental
# concepts and processes.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-3.H.1  Persistent organic pollutants (POPs) do not easily break down in the
#              environment because they are synthetic, carbon-based molecules (such as
#              DDT and PCBs).
#   STB-3.H.2  Persistent organic pollutants (POPs) can be toxic to organisms because
#              they are soluble in fat, which allows them to accumulate in organisms'
#              fatty tissues.
#   STB-3.H.3  Persistent organic pollutants (POPs) can travel over long distances via
#              wind and water before being redeposited.
#
# ON SCOPE. Topic 8.8 keys bioaccumulation and biomagnification (STB-3.I.1, STB-3.I.2)
# and their effects (STB-3.J.1 to STB-3.J.3). Nothing here defines either term or keys a
# rise in concentration across trophic levels; every key here rests on the three
# properties of the molecules themselves. Topic 8.2 keys methylmercury (STB-3.B.10),
# which is not a synthetic carbon-based molecule and is not keyed here.
#
# ON THE FIGURES. The bank carries no images, so every representation is a table and
# every keyed reading is recomputed in verify_e8_7.py from that table alone.
#
# NOT KEYED: no half-life figure for any real compound, no treaty, no concentration
# called safe or unsafe. The framework states none of them, so the data items key only
# directions, rank orders and comparisons that the tables themselves carry.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII.
TOPIC = ("8.7", "Persistent Organic Pollutants (POPs)", 8)

_T_PERSIST = dict(
    headers=["Compound tested in the same soil", "Description of the molecule",
             "Days for half of the amount applied to break down"],
    rows=[["Compound R", "synthetic and carbon based", "4000"],
          ["Compound S", "synthetic and carbon based", "2600"],
          ["Compound T", "readily broken down by soil microbes", "30"],
          ["Compound U", "readily broken down by soil microbes", "12"]])

_T_TISSUE = dict(
    headers=["Tissue sampled from one seal",
             "Fat content of the tissue (percent by mass)",
             "Concentration of the pollutant (parts per million)"],
    rows=[["Blubber", "82", "12.0"],
          ["Liver", "9", "1.1"],
          ["Muscle", "4", "0.60"],
          ["Blood", "1", "0.05"]])

_T_REMOTE = dict(
    headers=["Sampling site", "Distance from the nearest area of use (kilometers)",
             "Was the compound ever applied at this site",
             "Concentration in surface soil (nanograms per gram)"],
    rows=[["Farmland where the compound was applied", "0", "yes", "21.0"],
          ["Woodland downwind of that farmland", "80", "no", "6.4"],
          ["Coastal plain far from any use", "1200", "no", "2.2"],
          ["Polar site with no agriculture", "5000", "no", "1.1"]])

_T_DECLINE = dict(
    headers=["Years since both compounds stopped being used",
             "Concentration of the persistent organic pollutant (parts per billion)",
             "Concentration of the readily broken down pesticide (parts per billion)"],
    rows=[["0", "100", "100"],
          ["5", "88", "6.0"],
          ["10", "76", "0.40"],
          ["20", "58", "0.02"]])

_T_SPECIES = dict(
    headers=["Animal sampled from one bay",
             "Concentration in fatty tissue (parts per million)",
             "Concentration in muscle (parts per million)"],
    rows=[["Harbor seal", "14.0", "0.70"],
          ["Cormorant", "5.0", "0.30"],
          ["Bass", "1.2", "0.09"],
          ["Clam", "0.40", "0.03"]])

_T_SOLUBILITY = dict(
    headers=["Compound", "Solubility in water (milligrams per liter)",
             "Solubility in fat (units of the same scale)",
             "Concentration measured in animal fat (parts per million)"],
    rows=[["Compound V", "0.001", "900", "12.0"],
          ["Compound W", "0.010", "400", "5.0"],
          ["Compound X", "1.2", "60", "0.80"],
          ["Compound Y", "40.0", "3", "0.05"]])

QUESTIONS = [

 dict(q="Why does the framework say persistent organic pollutants do not easily break "
        "down in the environment?",
      choices=[
        "They are synthetic, carbon based molecules",
        "They are naturally occurring mineral salts",
        "They are heavy metals released by mining",
        "They are gases that rise into the stratosphere",
        "They are living organisms that resist decay"],
      ans=0,
      why="STB-3.H.1 states that persistent organic pollutants do not easily break down "
          "in the environment because they are synthetic, carbon based molecules. "
          "Mineral salts, heavy metals, gases and organisms are different categories the "
          "course treats elsewhere."),

 dict(q="Why can persistent organic pollutants be toxic to organisms, according to the "
        "framework?",
      choices=[
        "They are soluble in fat, which allows them to accumulate in the fatty tissues of "
        "organisms",
        "They are soluble in water, which allows them to be flushed out quickly",
        "They bind to bone and are removed whenever bone is remodeled",
        "They dissolve only in air and never enter a body at all",
        "They are converted to harmless sugars once they are absorbed"],
      ans=0,
      why="STB-3.H.2 states that persistent organic pollutants can be toxic to organisms "
          "because they are soluble in fat, which allows them to accumulate in organisms' "
          "fatty tissues. Each rejected option replaces fat solubility with a route that "
          "would remove rather than store the compound."),

 dict(q="Four compounds were applied to the same soil and followed until half of each had "
        "broken down.",
      table=_T_PERSIST,
      choices=[
        "The two compounds described as synthetic and carbon based took far longer to "
        "break down by half than the two that soil microbes readily break down",
        "The two compounds described as synthetic and carbon based broke down fastest",
        "All four compounds took about the same time to break down by half",
        "The compound that broke down fastest is one of the synthetic carbon based ones",
        "The table shows that time to break down does not depend on the molecule"],
      ans=0,
      why="Both rows described as synthetic and carbon based carry breakdown times of "
          "thousands of days while both readily broken down rows carry tens of days. "
          "STB-3.H.1 gives that difference as the reason these compounds are called "
          "persistent."),

 dict(q="Which examples of persistent organic pollutants does the framework itself name?",
      choices=[
        "DDT and PCBs",
        "Lead and cadmium",
        "Nitrate and phosphate",
        "Carbon dioxide and methane",
        "Sulfur dioxide and nitrogen oxides"],
      ans=0,
      why="STB-3.H.1 names DDT and PCBs as examples of the synthetic, carbon based "
          "molecules it calls persistent organic pollutants. Metals, nutrients, "
          "greenhouse gases and acid rain precursors belong to other statements in the "
          "course."),

 dict(q="What does the framework say about how far persistent organic pollutants can "
        "move?",
      choices=[
        "They can travel over long distances by wind and water before being redeposited",
        "They stay within a few meters of where they were released",
        "They move only through the bodies of migrating animals",
        "They move only downward into groundwater and never sideways",
        "They cannot move at all once they have been applied to soil"],
      ans=0,
      why="STB-3.H.3 states that persistent organic pollutants can travel over long "
          "distances via wind and water before being redeposited. Every rejected option "
          "denies or narrows that statement."),

 dict(q="Tissues from one seal were analyzed for a persistent organic pollutant.",
      table=_T_TISSUE,
      choices=[
        "The tissue with the highest fat content carries by far the highest concentration, "
        "and the tissue with the lowest fat content the lowest",
        "The tissue with the highest fat content carries the lowest concentration",
        "Every tissue sampled carries the same concentration",
        "The concentration is highest in the tissue with the least fat",
        "Fat content and concentration are unrelated across these tissues"],
      ans=0,
      why="Ranking the tissues by fat content puts the pollutant concentrations in the "
          "same order, with blubber highest and blood lowest. STB-3.H.2 states that these "
          "compounds are soluble in fat, which allows them to accumulate in fatty "
          "tissues."),

 dict(q="A compound is measured in soil in a region where it was never applied and where "
        "no factory has ever produced it. Which framework statement best explains the "
        "measurement?",
      choices=[
        "Persistent organic pollutants can travel over long distances by wind and water "
        "before being redeposited",
        "Persistent organic pollutants are synthetic, carbon based molecules",
        "Persistent organic pollutants are soluble in fat",
        "Persistent organic pollutants accumulate in the fatty tissues of organisms",
        "Persistent organic pollutants are broken down quickly by soil microbes"],
      ans=0,
      why="STB-3.H.3 is the statement about movement, and long distance transport by wind "
          "and water followed by redeposition is what puts a compound where it was never "
          "used. The other statements explain persistence and storage rather than "
          "transport."),

 dict(q="Why is a persistent organic pollutant more likely to be found concentrated in an "
        "animal's fat than in its blood?",
      choices=[
        "The molecule dissolves in fat far better than in the watery fluids of the body, "
        "so it collects where the fat is",
        "The molecule dissolves in water far better than in fat, so it collects in blood",
        "Blood is replaced too slowly for any compound to be measured in it",
        "Fat is the only tissue in which any pollutant can be measured",
        "The molecule is destroyed by contact with blood but not by contact with fat"],
      ans=0,
      why="STB-3.H.2 attributes the accumulation to solubility in fat, which is what "
          "makes fatty tissue rather than a watery compartment the place the compound "
          "collects. The framework makes no claim that blood cannot be sampled or that "
          "blood destroys the compound."),

 dict(q="Soil samples taken at increasing distance from the only area where a compound "
        "was ever applied are shown.",
      table=_T_REMOTE,
      choices=[
        "The compound is present at every site, including sites thousands of kilometers "
        "away where it was never applied, with the concentration falling as distance rises",
        "The compound is present only at the site where it was applied",
        "The concentration rises as the distance from the area of use rises",
        "The compound is absent from every site where it was never applied",
        "All four sites carry the same concentration of the compound"],
      ans=0,
      why="Every row carries a measurable concentration, three of them at sites marked as "
          "never having received the compound, and the concentrations fall as the distance "
          "grows. STB-3.H.3 states that these compounds travel long distances by wind and "
          "water before being redeposited."),

 dict(q="A student says persistent organic pollutants are dangerous because they dissolve "
        "readily in water and so spread through rivers. What is the clearest correction "
        "based on the framework?",
      choices=[
        "The framework attributes their toxicity to solubility in fat, which lets them "
        "accumulate in fatty tissue rather than wash away",
        "The framework attributes their toxicity to solubility in water, so the statement "
        "is exactly right",
        "The framework says these compounds cannot move through water at all",
        "The framework says these compounds are harmless in any solvent",
        "The framework says these compounds break down as soon as they enter a river"],
      ans=0,
      why="STB-3.H.2 gives fat solubility as the reason for the toxicity, and STB-3.H.1 "
          "gives resistance to breakdown as the reason for the persistence. STB-3.H.3 "
          "does allow water to carry them, but that is transport rather than the source "
          "of the toxicity."),

 dict(q="Which measurement would best establish that a newly detected compound belongs to "
        "the class the framework calls persistent?",
      choices=[
        "The length of time the compound remains in soil or water before it breaks down",
        "The price of the compound when it was manufactured",
        "The color of the compound in its pure form",
        "The number of countries in which the compound was sold",
        "The volume of the container the compound was shipped in"],
      ans=0,
      why="STB-3.H.1 makes resistance to breaking down in the environment the defining "
          "property, so the time until breakdown is the measurement that tests it. Price, "
          "color, sales and packaging bear on none of the three statements."),

 dict(q="Two compounds stopped being used in the same year and were then followed in soil.",
      table=_T_DECLINE,
      choices=[
        "The persistent compound is still at more than half its starting concentration "
        "after twenty years, while the other has nearly disappeared",
        "The persistent compound disappeared faster than the other one",
        "Both compounds fell to nearly zero within five years",
        "Neither compound changed at all over the twenty years",
        "The readily broken down pesticide is the one still present after twenty years"],
      ans=0,
      why="The persistent column falls only from its starting value to a little over half "
          "across twenty years while the other column falls to a small fraction of one "
          "part per billion. STB-3.H.1 makes resistance to breakdown the reason these "
          "compounds remain long after use has stopped."),

 dict(q="Why does banning the manufacture of a persistent organic pollutant not remove it "
        "from an ecosystem immediately?",
      choices=[
        "The molecules already released do not easily break down, so they remain in the "
        "environment after new releases stop",
        "A ban has no effect on how much of the compound is released",
        "The compound is regenerated by soil microbes after a ban",
        "The compound is only produced by natural processes, so a ban is irrelevant",
        "The compound evaporates completely within days of a ban"],
      ans=0,
      why="STB-3.H.1 states that these compounds do not easily break down in the "
          "environment, so a stock already released persists after the input is stopped. "
          "The framework describes them as synthetic rather than naturally produced."),

 dict(q="Which of the following is NOT a property the framework attributes to persistent "
        "organic pollutants?",
      choices=[
        "They break down quickly once released into soil or water",
        "They are synthetic, carbon based molecules",
        "They are soluble in fat",
        "They can travel long distances by wind and water",
        "They can accumulate in the fatty tissues of organisms"],
      ans=0,
      why="STB-3.H.1 states the opposite, that these compounds do not easily break down "
          "in the environment. The other four options restate STB-3.H.1, STB-3.H.2 and "
          "STB-3.H.3."),

 dict(q="Fatty tissue and muscle from four animals in one bay were compared.",
      table=_T_SPECIES,
      choices=[
        "In every animal sampled the concentration in fatty tissue is many times the "
        "concentration in muscle",
        "In every animal sampled the concentration in muscle is higher than in fatty tissue",
        "The two tissues carry the same concentration in every animal sampled",
        "Only one of the four animals shows a higher concentration in fatty tissue",
        "The comparison of the two tissues differs in direction from animal to animal"],
      ans=0,
      why="Each row's fatty tissue value is well above its muscle value, and the pattern "
          "holds for all four animals. STB-3.H.2 attributes that to solubility in fat, "
          "which allows these compounds to accumulate in fatty tissues."),

 dict(q="What does the word persistent refer to in the name of this class of pollutants?",
      choices=[
        "That the molecules resist breaking down and therefore remain in the environment "
        "for a long time",
        "That the pollutants are released continuously from a single source",
        "That the pollutants are used persistently by farmers year after year",
        "That the pollutants keep the same color no matter how they are stored",
        "That the pollutants persist only inside living organisms and not in soil"],
      ans=0,
      why="STB-3.H.1 defines the class by the fact that these compounds do not easily "
          "break down in the environment. The name refers to the molecule's fate rather "
          "than to a pattern of release, a pattern of use, or an appearance."),

 dict(q="A chemical is synthetic and carbon based but is broken down by soil microbes "
        "within two weeks of application. How does the framework's account apply?",
      choices=[
        "It fails the property that defines the class, since these pollutants are those "
        "that do not easily break down in the environment",
        "It belongs to the class, because being synthetic and carbon based is sufficient",
        "It belongs to the class, because all pesticides belong to the class",
        "It fails the property, because the class includes only naturally occurring "
        "molecules",
        "The framework offers no way to judge the case"],
      ans=0,
      why="STB-3.H.1 gives being synthetic and carbon based as the reason these compounds "
          "resist breakdown, and resistance to breakdown is what the class is named for, "
          "so a compound that degrades in two weeks does not show the defining behavior."),

 dict(q="Four compounds with different solubilities were measured in the fat of animals "
        "from the same area.",
      table=_T_SOLUBILITY,
      choices=[
        "The compounds that dissolve best in fat and least in water are the ones found at "
        "the highest concentrations in animal fat",
        "The compounds that dissolve best in water are the ones found at the highest "
        "concentrations in animal fat",
        "All four compounds are found at the same concentration in animal fat",
        "The compound with the lowest solubility in fat is found at the highest "
        "concentration in animal fat",
        "Solubility tells nothing about the concentration found in animal fat here"],
      ans=0,
      why="Ranking the compounds by solubility in fat gives the same order as ranking them "
          "by the concentration found in animal fat, and the reverse of the order by "
          "solubility in water. STB-3.H.2 makes solubility in fat the reason these "
          "compounds accumulate in fatty tissues."),

 dict(q="By which two routes does the framework say these pollutants travel before being "
        "redeposited?",
      choices=[
        "Wind and water",
        "Groundwater and bedrock",
        "Lava flows and ash falls",
        "Root systems and leaf litter",
        "Trade routes and shipping containers"],
      ans=0,
      why="STB-3.H.3 states that persistent organic pollutants can travel over long "
          "distances via wind and water before being redeposited. The framework names no "
          "other transport route for them."),

 dict(q="What does the framework mean by saying these pollutants are redeposited after "
        "traveling?",
      choices=[
        "They leave the air or water at a new location and settle there, far from where "
        "they were released",
        "They are collected and returned to the factory that made them",
        "They are destroyed in transit and leave nothing behind",
        "They remain permanently airborne and never reach a surface",
        "They are buried by people at the site where they were first used"],
      ans=0,
      why="STB-3.H.3 pairs long distance travel by wind and water with redeposition, "
          "which is how a compound comes to be measured in a place far from its release. "
          "Destruction in transit would contradict the persistence stated in STB-3.H.1."),

 dict(q="Why does solubility in fat rather than solubility in water lead to accumulation "
        "inside an organism?",
      choices=[
        "A fat soluble compound is held in fatty tissue instead of being carried out in "
        "watery wastes",
        "A fat soluble compound is broken down faster inside the body than a water soluble "
        "one",
        "A water soluble compound cannot enter an organism at all",
        "Fatty tissue destroys any compound stored in it",
        "Organisms contain no watery fluids in which a compound could be carried"],
      ans=0,
      why="STB-3.H.2 states that solubility in fat allows these compounds to accumulate in "
          "organisms' fatty tissues, which is a matter of where the compound is held "
          "rather than of how fast it is destroyed."),

 dict(q="Which evidence would most directly test the claim that a compound travels long "
        "distances before being redeposited?",
      choices=[
        "Measurements of the compound in soil, air or snow at sites far from any use, "
        "with wind or current records connecting them to areas of use",
        "Measurements of the compound only at the field where it was applied",
        "A count of how many companies once manufactured the compound",
        "The temperature at which the compound was stored before use",
        "The mass of the compound produced in a single year"],
      ans=0,
      why="STB-3.H.3 asserts movement followed by redeposition, so the test is detection "
          "at distant sites together with a transport pathway. Measurements only at the "
          "source, production statistics and storage conditions test none of that."),

 dict(q="Why does the framework describe these molecules as synthetic?",
      choices=[
        "They are manufactured rather than produced by natural processes, and that origin "
        "is part of why they resist breakdown",
        "They are produced only by bacteria in wetland soils",
        "They are formed naturally when organic matter decays",
        "They are extracted from rock and refined without alteration",
        "They are found in the tissues of every organism from birth"],
      ans=0,
      why="STB-3.H.1 describes persistent organic pollutants as synthetic, carbon based "
          "molecules and gives that as the reason they do not easily break down. Natural "
          "production, decay products and mined minerals are different origins."),

 dict(q="Which pairing of a framework property with its consequence is correct?",
      choices=[
        "Resistance to breakdown, so the compound remains in the environment long after "
        "its release",
        "Resistance to breakdown, so the compound disappears within a season",
        "Solubility in fat, so the compound is quickly excreted in urine",
        "Long distance transport, so the compound is confined to the place it was used",
        "Being synthetic, so the compound is produced continuously by soil organisms"],
      ans=0,
      why="STB-3.H.1 makes resistance to breakdown the reason these compounds persist in "
          "the environment. Each rejected pairing states a property from STB-3.H.1 to "
          "STB-3.H.3 and then attaches the opposite consequence."),

 dict(q="A country that never manufactured or used DDT finds it in the fat of its "
        "wildlife. Which combination of framework statements explains this best?",
      choices=[
        "The compound resists breakdown and travels long distances by wind and water, and "
        "its fat solubility means it collects in fatty tissue once it arrives",
        "The compound is produced naturally inside the animals themselves",
        "The compound must have been manufactured secretly in that country",
        "The compound dissolves in water and is therefore flushed out of any animal that "
        "takes it in",
        "The compound breaks down within days, so the measurement must be an error"],
      ans=0,
      why="STB-3.H.1 supplies the persistence, STB-3.H.3 the long distance transport and "
          "redeposition, and STB-3.H.2 the accumulation in fatty tissue, which together "
          "account for a residue in a place with no history of use."),

 dict(q="Which comparison would best test the framework's claim that a compound is stored "
        "because it is fat soluble?",
      choices=[
        "The concentration measured in fatty tissue against the concentration measured in "
        "a low fat tissue of the same animal",
        "The concentration measured in one tissue of one animal on a single day",
        "The number of animals sampled in the study",
        "The distance the animal traveled during the year",
        "The mass of the animal at the time of sampling"],
      ans=0,
      why="STB-3.H.2 predicts that the compound collects in fatty tissue, so a comparison "
          "between a fatty and a low fat tissue in the same animal is what tests it. A "
          "single value, a sample size, a travel distance and a body mass do not."),

 dict(q="Why does the framework mention that these molecules are carbon based as well as "
        "synthetic?",
      choices=[
        "Both together describe the kind of molecule that resists breaking down in the "
        "environment, which is what makes the class persistent",
        "Being carbon based means the molecules are alive",
        "Being carbon based means the molecules dissolve only in water",
        "Being carbon based means the molecules are removed by photosynthesis",
        "Being carbon based means the molecules are naturally occurring"],
      ans=0,
      why="STB-3.H.1 gives synthetic and carbon based together as the reason these "
          "compounds do not easily break down in the environment. The framework makes no "
          "claim that carbon based molecules are alive, water soluble, natural or removed "
          "by photosynthesis."),

 dict(q="Sediment cored from a lake bed shows a layer laid down decades ago that still "
        "contains measurable PCBs. Which framework statement bears most directly on that "
        "result?",
      choices=[
        "These compounds do not easily break down in the environment",
        "These compounds accumulate in the fatty tissues of organisms",
        "These compounds are toxic because they are soluble in fat",
        "These compounds travel long distances by wind and water",
        "These compounds are removed from sediment by microbes within a year"],
      ans=0,
      why="A residue still measurable decades after deposition is the persistence stated "
          "in STB-3.H.1. Fat solubility and transport are the subjects of STB-3.H.2 and "
          "STB-3.H.3 and do not explain survival in sediment."),

 dict(q="Which monitoring design would best show that a persistent organic pollutant "
        "reaches a remote region through the atmosphere?",
      choices=[
        "Air and freshly fallen snow sampled at the remote region over several years, "
        "compared with the timing of releases upwind",
        "A single soil sample taken once at the remote region",
        "A survey of how many people live in the remote region",
        "A record of the compound's price in the region where it is used",
        "A map showing the area of farmland in the region where it is used"],
      ans=0,
      why="STB-3.H.3 names wind as one of the two transport routes, so sampling the air "
          "and fresh deposition at the receiving end and matching it to upwind releases "
          "tests that pathway. A single soil sample cannot distinguish a route, and "
          "population, price and farmland area test nothing about transport."),

 dict(q="Which summary best captures this topic?",
      choices=[
        "Synthetic carbon based molecules such as DDT and PCBs resist breaking down, "
        "travel long distances by wind and water before being redeposited, and are toxic "
        "because their fat solubility lets them accumulate in fatty tissues",
        "Naturally occurring mineral pollutants break down quickly and are stored in bone",
        "Water soluble compounds that break down within days are the main persistent "
        "pollutants",
        "These pollutants stay where they are released and never reach remote regions",
        "These pollutants are harmless to organisms because they cannot enter tissues"],
      ans=0,
      why="Each clause of the keyed summary is one of STB-3.H.1, STB-3.H.2 and STB-3.H.3. "
          "Every rejected summary denies the persistence, the transport, or the "
          "accumulation in fatty tissue."),
]
