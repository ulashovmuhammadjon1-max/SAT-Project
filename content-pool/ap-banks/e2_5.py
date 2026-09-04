# AP ENVIRONMENTAL SCIENCE 2.5 Natural Disruptions to Ecosystems
# CED effective Fall 2026, Unit 2 The Living World: Biodiversity.
# Enduring understanding ERT-2: ecosystems have structure and diversity that change over
# time.
# Learning objective ERT-2.G: explain how natural disruptions, both short- and long-term,
# impact an ecosystem. Suggested skill 5.A, describe patterns or trends in data.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-2.G.1  Natural disruptions to ecosystems have environmental consequences that may,
#              for a given occurrence, be as great as, or greater than, many human-made
#              disruptions.
#   ERT-2.G.2  Earth system processes operate on a range of scales in terms of time.
#              Processes can be periodic, episodic, or random.
#   ERT-2.G.3  Earth's climate has changed over geological time for many reasons.
#   ERT-2.G.4  Sea level has varied significantly as a result of changes in the amount of
#              glacial ice on Earth over geological time.
#   ERT-2.G.5  Major environmental change or upheaval commonly results in large swathes of
#              habitat changes.
#   ERT-2.G.6  Wildlife engages in both short- and long-term migration for a variety of
#              reasons, including natural disruptions.
#
# THE HEDGES ARE LOAD-BEARING AND SEVERAL ITEMS TURN ON THEM. ERT-2.G.1 says MAY be as
# great as or greater than MANY human-made disruptions, and it says so FOR A GIVEN
# OCCURRENCE -- it is a comparison of single events, not a claim that natural disruption
# outweighs human activity in total. ERT-2.G.3 says climate changed FOR MANY REASONS and
# names none of them. ERT-2.G.5 says COMMONLY. ERT-2.G.6 says A VARIETY OF REASONS,
# INCLUDING natural disruptions, so a natural disruption is one reason among several. No
# key anywhere hardens one of these into a stronger claim.
#
# PERIODIC, EPISODIC AND RANDOM ARE NAMED BUT NOT DEFINED, so no item asks a student to
# tell an episodic process from a random one -- the framework supplies no way to draw that
# line. Item 5 asks only which words are on the list, and item 18 asks which tabulated
# process recurs at a CONSTANT interval, which is arithmetic on the table plus the ordinary
# meaning of the word periodic; the claim in verify_e2_5.py says exactly that.
#
# ERT-2.G.3 gives no cause of past climate change, so no key names one. ERT-2.G.4 gives
# exactly one cause of sea level variation, glacial ice, and no key adds another.
#
# BOUNDARY WITH 2.2 AND 2.6. Anthropogenic disruption of ecosystem services is ERT-2.C.1
# in topic 2.2 and appears here only as the other side of ERT-2.G.1's comparison. How
# populations respond to environmental change over generations is ERT-2.H in topic 2.6;
# nothing here is about natural selection.
#
# NO FIGURES. Every quantitative item carries a table=, recomputed in verify_e2_5.py from
# that table alone.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("2.5", "Natural Disruptions to Ecosystems", 2)

_T_DISRUPT = dict(
    headers=["Event recorded in one forested region", "Hectares of forest destroyed"],
    rows=[["A volcanic eruption, a natural event", "60000"],
          ["A wildfire started by lightning, a natural event", "41000"],
          ["A logging operation, a human made activity", "15000"],
          ["A road and pipeline corridor, a human made activity", "3500"]])

_T_SEALEVEL = dict(
    headers=["Interval of geological time",
             "Glacial ice on Earth (millions of cubic kilometres)",
             "Sea level relative to today (metres)"],
    rows=[["Interval 1", "12", "5"],
          ["Interval 2", "30", "-20"],
          ["Interval 3", "55", "-75"],
          ["Interval 4", "78", "-120"]])

_T_CLIMATE = dict(
    headers=["Interval of geological time",
             "Average global surface temperature (degrees Celsius)"],
    rows=[["Interval 1", "22"],
          ["Interval 2", "17"],
          ["Interval 3", "11"],
          ["Interval 4", "19"],
          ["Interval 5", "14"]])

_T_INTERVAL = dict(
    headers=["Natural process", "Years between the first and second occurrence",
             "Years between the second and third occurrence",
             "Years between the third and fourth occurrence"],
    rows=[["Process 1", "12", "12", "12"],
          ["Process 2", "3", "19", "41"],
          ["Process 3", "7", "30", "8"],
          ["Process 4", "55", "6", "23"]])

_T_SCALE = dict(
    headers=["Earth system process",
             "Typical time over which one occurrence plays out (years)"],
    rows=[["Process A", "1"],
          ["Process B", "70"],
          ["Process C", "5000"],
          ["Process D", "2000000"]])

_T_HABITAT = dict(
    headers=["Habitat type in one valley", "Area before the eruption (hectares)",
             "Area two years after the eruption (hectares)"],
    rows=[["Mature forest", "9000", "400"],
          ["Young scrub", "1200", "2100"],
          ["Bare ash and rock", "0", "8100"],
          ["Wetland", "800", "400"]])

_T_MIGRATION = dict(
    headers=["Migrating species", "Distance moved one way (kilometres)",
             "Months spent away from the breeding area"],
    rows=[["Species 1", "15", "1"],
          ["Species 2", "400", "3"],
          ["Species 3", "6000", "7"],
          ["Species 4", "90", "2"]])

_T_DROUGHT = dict(
    headers=["Stage of the drought", "Rainfall in the season (millimetres)",
             "Waterbirds counted on the wetland"],
    rows=[["The year before the drought", "480", "5200"],
          ["The second year of the drought", "90", "300"],
          ["The year after the rains returned", "510", "4700"]])

QUESTIONS = [

 dict(q="What does the framework say about the environmental consequences of natural "
        "disruptions compared with human-made ones?",
      choices=[
        "For a given occurrence they may be as great as, or greater than, many human-made "
        "disruptions.",
        "They are always smaller than those of any human-made disruption.",
        "They are always greater than those of every human-made disruption.",
        "They cannot be compared with human-made disruptions at all.",
        "They are identical in size to those of human-made disruptions."],
      ans=0,
      why="ERT-2.G.1 states that natural disruptions have environmental consequences that "
          "may, for a given occurrence, be as great as, or greater than, many human-made "
          "disruptions. The statement allows the comparison and hedges it, so neither "
          "always claim is what it says."),

 dict(q="ERT-2.G.1 says MAY be as great as or greater than MANY human-made disruptions, "
        "FOR A GIVEN OCCURRENCE. What does that phrasing establish?",
      choices=[
        "That single events are being compared, and that some human-made disruptions are "
        "not being ranked below natural ones.",
        "That the total effect of all natural disruptions exceeds the total effect of all "
        "human activity.",
        "That every natural disruption exceeds every human-made one.",
        "That natural disruptions occur more often than human-made ones.",
        "That human-made disruptions have no environmental consequences of their own."],
      ans=0,
      why="ERT-2.G.1 compares occurrences rather than totals, uses may rather than does, "
          "and says many human-made disruptions rather than all of them. Every rejected "
          "option strengthens one of those three hedges."),

 dict(q="What does the framework say about the time scales on which Earth system processes "
        "operate?",
      choices=[
        "They operate on a range of scales in terms of time.",
        "They all operate on the same time scale.",
        "They all operate over intervals shorter than a human lifetime.",
        "They all operate over intervals longer than a million years.",
        "Their time scales cannot be described."],
      ans=0,
      why="ERT-2.G.2 states that Earth system processes operate on a range of scales in "
          "terms of time, so no single scale covers them and none is ruled out."),

 dict(q="Which three descriptions does the framework apply to Earth system processes?",
      choices=[
        "Periodic, episodic or random.",
        "Periodic, seasonal or reversible.",
        "Episodic, random or reversible.",
        "Periodic, gradual or catastrophic.",
        "Episodic, cyclical or permanent."],
      ans=0,
      why="ERT-2.G.2 states that processes can be periodic, episodic, or random. Each "
          "rejected set replaces at least one of those three with a word the statement does "
          "not use."),

 dict(q="A revision card lists four words and says all four are the framework's "
        "descriptions of Earth system processes. Which word is not?",
      choices=["Reversible", "Periodic", "Episodic", "Random",
               "All four are on the framework's list"],
      ans=0,
      why="ERT-2.G.2 gives three words: periodic, episodic, and random. Reversible is not "
          "among them, so a card carrying four words has one too many."),

 dict(q="What does the framework say about Earth's climate over geological time?",
      choices=[
        "It has changed over geological time for many reasons.",
        "It has been constant over geological time.",
        "It has changed over geological time for a single reason.",
        "It has changed only since human industry began.",
        "It has changed only in the past ten thousand years."],
      ans=0,
      why="ERT-2.G.3 states that Earth's climate has changed over geological time for many "
          "reasons. The statement asserts change, places it in geological time, and puts "
          "more than one reason behind it."),

 dict(q="ERT-2.G.3 says Earth's climate has changed FOR MANY REASONS. What follows from "
        "that wording?",
      choices=[
        "That the framework attributes past climate change to more than one cause and names "
        "none of them here.",
        "That the framework names the single cause of every past climate change.",
        "That past climate change had no identifiable cause at all.",
        "That every past climate change had exactly the same cause.",
        "That climate change before human industry is not part of the framework's claim."],
      ans=0,
      why="ERT-2.G.3 says many reasons, which is more than one, and the statement lists no "
          "reason of its own. So a single-cause answer and a no-cause answer both go beyond "
          "what is written."),

 dict(q="According to the framework, what has caused sea level to vary significantly over "
        "geological time?",
      choices=[
        "Changes in the amount of glacial ice on Earth.",
        "Changes in the number of rivers reaching the ocean.",
        "Changes in the salinity of the deep ocean.",
        "Changes in the area of coastal wetland.",
        "Changes in the rate at which rain falls on the ocean."],
      ans=0,
      why="ERT-2.G.4 states that sea level has varied significantly as a result of changes "
          "in the amount of glacial ice on Earth over geological time. That is the one "
          "cause the statement gives."),

 dict(q="What does the framework say commonly results from major environmental change or "
        "upheaval?",
      choices=[
        "Large swathes of habitat changes.",
        "The immediate extinction of every species present.",
        "A permanent rise in the number of species present.",
        "A return of the ecosystem to its previous state within a year.",
        "No change to habitat at any scale."],
      ans=0,
      why="ERT-2.G.5 states that major environmental change or upheaval commonly results in "
          "large swathes of habitat changes. The claim is about habitat over a large area, "
          "not about extinction, enrichment or immediate recovery."),

 dict(q="What does the framework say about migration in wildlife?",
      choices=[
        "Wildlife engages in both short-term and long-term migration, for a variety of "
        "reasons that include natural disruptions.",
        "Wildlife engages only in long-term migration, and only because of natural "
        "disruptions.",
        "Wildlife engages only in short-term migration, and only because of natural "
        "disruptions.",
        "Wildlife engages in migration only where humans have altered the habitat.",
        "Wildlife migration has no relationship to natural disruptions."],
      ans=0,
      why="ERT-2.G.6 states that wildlife engages in both short- and long-term migration for "
          "a variety of reasons, including natural disruptions. Both durations are named and "
          "natural disruptions are one reason among several."),

 dict(q="Does the framework treat natural disruption as the only reason wildlife migrates?",
      choices=[
        "No, it gives a variety of reasons and includes natural disruptions among them.",
        "Yes, it names natural disruption as the sole reason.",
        "Yes, but only for movements lasting less than one season.",
        "No, it says natural disruptions never cause migration.",
        "No, because it treats migration as unrelated to the environment."],
      ans=0,
      why="ERT-2.G.6 says a variety of reasons, INCLUDING natural disruptions, which places "
          "natural disruption inside a larger set rather than alone in it, and does not "
          "remove it from the set either."),

 dict(q="Four events destroyed forest in one region. What does the table establish about "
        "the two kinds of event?",
      table=_T_DISRUPT,
      choices=[
        "A single natural event destroyed more forest than either of the human made "
        "activities listed.",
        "Each human made activity destroyed more forest than either natural event.",
        "The two natural events together destroyed less forest than the logging operation.",
        "All four events destroyed the same area of forest.",
        "Only the human made activities destroyed any forest at all."],
      ans=0,
      why="The eruption destroyed 60,000 hectares and the wildfire 41,000, while the "
          "logging operation destroyed 15,000 and the corridor 3,500. ERT-2.G.1 states that "
          "the consequences of a natural disruption may, for a given occurrence, be as "
          "great as or greater than many human-made disruptions, which is what this record "
          "shows for these occurrences."),

 dict(q="In that same record, roughly how does the forest destroyed by the eruption compare "
        "with the forest destroyed by the logging operation?",
      table=_T_DISRUPT,
      choices=["About four times as much", "About twice as much",
               "About ten times as much", "About one quarter as much",
               "About the same amount"],
      ans=0,
      why="The eruption destroyed 60,000 hectares and the logging operation 15,000, and "
          "60,000 divided by 15,000 is 4. The comparison is arithmetic on two entries in one "
          "column."),

 dict(q="Four intervals of geological time were reconstructed for glacial ice and sea "
        "level. What does the table establish?",
      table=_T_SEALEVEL,
      choices=[
        "Sea level stood lower in the intervals when more glacial ice was present.",
        "Sea level stood higher in the intervals when more glacial ice was present.",
        "Sea level was the same in all four intervals.",
        "Glacial ice was the same in all four intervals.",
        "Sea level and glacial ice cannot be compared across intervals."],
      ans=0,
      why="Ordered by glacial ice the sea level readings run 5, then 20, 75 and 120 metres "
          "below today, falling as the ice grows. ERT-2.G.4 states that sea level has varied "
          "significantly as a result of changes in the amount of glacial ice on Earth."),

 dict(q="Across those four intervals, how far apart are the highest and the lowest sea "
        "level reading?",
      table=_T_SEALEVEL,
      choices=["125 metres", "115 metres", "120 metres", "75 metres", "12 metres"],
      ans=0,
      why="The highest reading is 5 metres above today and the lowest is 120 metres below, "
          "and the distance between them is 125 metres. ERT-2.G.4 describes the variation as "
          "significant, and this is the size of it in the record."),

 dict(q="Average global surface temperature was reconstructed for five intervals of "
        "geological time. What does the table establish?",
      table=_T_CLIMATE,
      choices=[
        "The average temperature differed from one interval to another.",
        "The average temperature was the same in every interval.",
        "The average temperature rose steadily from the first interval to the last.",
        "The average temperature fell steadily from the first interval to the last.",
        "The record gives no temperature for any interval."],
      ans=0,
      why="The five readings are 22, 17, 11, 19 and 14 degrees Celsius, which are neither "
          "all equal nor in order. ERT-2.G.3 states that Earth's climate has changed over "
          "geological time, and a record of unequal intervals is what that change looks "
          "like."),

 dict(q="How large is the difference between the warmest and the coolest of those five "
        "reconstructed intervals?",
      table=_T_CLIMATE,
      choices=["Eleven degrees Celsius", "Five degrees Celsius", "Eight degrees Celsius",
               "Twenty-two degrees Celsius", "Three degrees Celsius"],
      ans=0,
      why="The warmest interval averages 22 degrees Celsius and the coolest 11, and 22 less "
          "11 is 11. The difference is arithmetic on the two extreme entries of one column."),

 dict(q="Four natural processes were dated over four occurrences each. Which one recurs at "
        "a constant interval?",
      table=_T_INTERVAL,
      choices=["Process 1", "Process 2", "Process 3", "Process 4",
               "None of the four recurs at a constant interval"],
      ans=0,
      why="One row records the same gap three times over, at 12 years, while the other three "
          "rows record gaps that differ from one another. ERT-2.G.2 lists periodic among the "
          "descriptions Earth system processes can take, and a constant interval is what "
          "the ordinary meaning of that word describes."),

 dict(q="Which of those four processes shows the longest single gap between two successive "
        "occurrences?",
      table=_T_INTERVAL,
      choices=["Process 4", "Process 1", "Process 2", "Process 3",
               "Two processes share the longest gap"],
      ans=0,
      why="The longest single gap anywhere in the record is 55 years, and it belongs to the "
          "row whose other gaps are 6 and 23 years. The comparison is a search of every "
          "entry in the three gap columns."),

 dict(q="Four Earth system processes were timed. What does the record establish about their "
        "time scales?",
      table=_T_SCALE,
      choices=[
        "They span a range of scales, from about a year to hundreds of thousands of years.",
        "They all play out over about the same length of time.",
        "They all play out within a single year.",
        "They all take longer than a million years.",
        "Their durations were not recorded."],
      ans=0,
      why="The four durations are 1, 70, 5,000 and 2,000,000 years, so the longest exceeds "
          "the shortest by a factor of two million. ERT-2.G.2 states that Earth system "
          "processes operate on a range of scales in terms of time."),

 dict(q="A valley was surveyed for habitat before an eruption and two years after it. What "
        "does the table establish?",
      table=_T_HABITAT,
      choices=[
        "Most of the valley's area changed from one habitat type to another.",
        "The valley's habitats were unchanged by the eruption.",
        "Only a small corner of the valley changed habitat type.",
        "The valley lost all of its area to the sea.",
        "Every habitat type in the valley increased in area."],
      ans=0,
      why="Mature forest fell from 9,000 hectares to 400 while bare ash and rock rose from "
          "none to 8,100, and the valley's total area is unchanged at 11,000 hectares, so "
          "most of it is under a different habitat type than before. ERT-2.G.5 states that "
          "major environmental change or upheaval commonly results in large swathes of "
          "habitat changes."),

 dict(q="Which habitat type in that valley lost the most area over the two years?",
      table=_T_HABITAT,
      choices=["Mature forest", "Young scrub", "Bare ash and rock", "Wetland",
               "No habitat type lost area"],
      ans=0,
      why="Mature forest fell by 8,600 hectares while wetland fell by 400 and the other two "
          "types gained area. The comparison is a subtraction carried out on every row."),

 dict(q="Four migrating species were tracked for distance and for time away. What does the "
        "record establish?",
      table=_T_MIGRATION,
      choices=[
        "Migrations range from short movements lasting a month to long ones lasting most of "
        "a year.",
        "Every tracked species moved about the same distance.",
        "Every tracked species was away for the same number of months.",
        "None of the tracked species moved more than a hundred kilometres.",
        "None of the tracked species returned to its breeding area."],
      ans=0,
      why="The distances run from 15 to 6,000 kilometres and the absences from 1 to 7 "
          "months. ERT-2.G.6 states that wildlife engages in both short-term and long-term "
          "migration, which is the spread this record shows."),

 dict(q="Which of the four tracked species spends the longest time away from its breeding "
        "area?",
      table=_T_MIGRATION,
      choices=["Species 3", "Species 1", "Species 2", "Species 4",
               "Two species share the longest absence"],
      ans=0,
      why="The absences recorded are 1, 3, 7 and 2 months, and the longest belongs to the "
          "species that also travels furthest. The comparison is a direct reading of one "
          "column."),

 dict(q="A wetland was counted through a drought and after it. What does the record "
        "establish?",
      table=_T_DROUGHT,
      choices=[
        "The waterbirds left the wetland as the rainfall collapsed and most were counted "
        "there again once the rains returned.",
        "The waterbirds stayed on the wetland throughout the drought.",
        "The waterbirds left the wetland and did not return after the rains.",
        "The waterbird count rose during the drought and fell afterwards.",
        "Rainfall and the waterbird count moved in opposite directions."],
      ans=0,
      why="Rainfall runs 480, 90 and 510 millimetres while the bird count runs 5,200, 300 "
          "and 4,700, so both collapse together and both recover together. ERT-2.G.6 states "
          "that wildlife engages in migration for a variety of reasons including natural "
          "disruptions, and a drought is such a disruption."),

 dict(q="A researcher claims that one storm changed as much habitat in a bay as thirty "
        "years of building did. Which comparison would test the claim most directly?",
      choices=[
        "The area of habitat altered by the single storm set against the area altered by the "
        "building over those thirty years.",
        "The number of storms recorded in the bay over the same thirty years.",
        "The cost of repairing the buildings the storm damaged.",
        "The number of species living in the bay before the storm.",
        "The wind speed the storm reached at its peak."],
      ans=0,
      why="ERT-2.G.1 compares the environmental consequences of a given natural occurrence "
          "with those of human-made disruptions, so the test is a like-for-like measurement "
          "of altered area. A storm count, a repair bill, a species list and a wind speed "
          "each measure something else."),

 dict(q="Which of these would the framework count as a natural disruption rather than a "
        "human-made one?",
      choices=[
        "A hurricane crossing a stretch of coastal forest.",
        "A reservoir flooding a valley behind a new dam.",
        "A quarry removing a hillside for building stone.",
        "A canal cut between two river systems.",
        "A plantation replacing a native woodland."],
      ans=0,
      why="ERT-2.G.1 sets natural disruptions beside human-made ones, and a hurricane is an "
          "event of the Earth system rather than an act of construction. Each rejected "
          "option is something people built or planted."),

 dict(q="Which statement about the timing of Earth system processes stays within ERT-2.G.2?",
      choices=[
        "Different processes play out over very different lengths of time, and a process may "
        "be periodic, episodic or random.",
        "All processes play out over the same length of time, and each one is periodic.",
        "Different processes play out over different lengths of time, and every one of them "
        "is random.",
        "Different processes play out over different lengths of time, and none of them "
        "recurs.",
        "All processes are episodic, and time scale is not a useful description of them."],
      ans=0,
      why="ERT-2.G.2 makes two assertions: processes operate on a range of scales in terms "
          "of time, and processes can be periodic, episodic, or random. Each rejected "
          "statement collapses the range to one scale or the three descriptions to one."),

 dict(q="Which conclusion about past sea level does the framework support?",
      choices=[
        "Sea level has varied significantly, and the framework attributes that variation to "
        "changes in the amount of glacial ice.",
        "Sea level has varied significantly, and the framework attributes that variation to "
        "changes in ocean salinity.",
        "Sea level has been stable over geological time apart from short local changes.",
        "Sea level has varied significantly, but the framework gives no cause for it.",
        "Sea level has varied significantly, and the framework attributes that variation to "
        "the number of rivers reaching the sea."],
      ans=0,
      why="ERT-2.G.4 states that sea level has varied significantly as a result of changes "
          "in the amount of glacial ice on Earth over geological time. It asserts both the "
          "variation and that one cause, so an answer denying the variation, denying the "
          "cause, or substituting another cause departs from it."),

 dict(q="Which single sentence collects what this topic's six statements assert and nothing "
        "further?",
      choices=[
        "A single natural disruption may match or exceed many human-made ones; Earth system "
        "processes run on many time scales and may be periodic, episodic or random; climate "
        "has changed for many reasons; sea level has followed glacial ice; upheaval commonly "
        "changes habitat over large areas; and wildlife migrates over short and long terms "
        "for several reasons, natural disruption among them.",
        "Every natural disruption exceeds every human-made one; Earth system processes all "
        "run on one time scale; climate has changed for a single reason; sea level has "
        "followed ocean salinity; upheaval always changes habitat; and wildlife migrates "
        "only because of natural disruption.",
        "A single natural disruption may match or exceed many human-made ones; Earth system "
        "processes run on many time scales; climate has been constant; sea level has "
        "followed glacial ice; upheaval commonly changes habitat over large areas; and "
        "wildlife does not migrate.",
        "Natural disruptions have no environmental consequences; Earth system processes run "
        "on many time scales and may be periodic, episodic or random; climate has changed "
        "for many reasons; sea level has followed glacial ice; upheaval commonly changes "
        "habitat; and wildlife migrates for several reasons.",
        "A single natural disruption may match or exceed many human-made ones; Earth system "
        "processes are all random; climate has changed for many reasons; sea level has "
        "varied for no stated cause; upheaval rarely changes habitat; and wildlife migrates "
        "only over short terms."],
      ans=0,
      why="The keyed sentence carries ERT-2.G.1's hedged comparison, ERT-2.G.2's range of "
          "time scales and three descriptions, ERT-2.G.3's many reasons, ERT-2.G.4's glacial "
          "ice, ERT-2.G.5's large swathes of habitat change and ERT-2.G.6's two durations "
          "and several reasons. Each rejected summary hardens a hedge, denies a statement, "
          "or swaps a cause."),
]
