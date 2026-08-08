#!/usr/bin/env python3
"""
Original Math content for Test 16 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students and per the
user's explicit instruction that Test 16's Module 1 be much harder than a
stock Module 1:

  MODULE_1      upper-medium and deliberately hard. Almost every item makes a
                constant, a rate, a unit price or an unknown be recovered
                first and only then used — two or three steps throughout.
                Clearly harder than Module 2 (Easy), clearly below Module 2
                (Hard).
  MODULE_2_EASY genuinely one-step — one operation, no recovery step. This is
                the lower branch of the adaptive split.
  MODULE_2_HARD hard: parameters instead of numbers, structural and symbolic
                answer choices, a composed function, systems conditioned on a
                constant, inequality chains, and geometry that needs two
                relationships chained together.

Every setting sits inside Test 16's assigned thematic territory — maritime
shipping and harbour pilotage, textile weaving and dyeing, beekeeping,
printing presses, glass and bottle works, lighthouse keeping, salt pans, rope
walks, sailmaking, tide mills, cargo manifests, ferry timetables, indigo vats
and loom warping — and every stem was written to a different template from
anything banked in production.

House style follows Test 1/2 (see CLAUDE.md): stems are bare HTML, simple
inline math stays plain text, data tables are real <table> markup, and all
LaTeX is typed by hand. No bulk conversion step was used anywhere in this
file.
"""

TABLE = '<table style="border-collapse:collapse;margin:0.75rem 0;">{head}{body}</table>'
TH = '<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;">{}</th>'
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">{}</td>'


def table(headers, rows):
    head = "<tr>" + "".join(TH.format(h) for h in headers) + "</tr>"
    body = "".join("<tr>" + "".join(TD.format(c) for c in r) + "</tr>" for r in rows)
    return TABLE.format(head=head, body=body)


# ---------------------------------------------------------------- Module 1
MODULE_1 = [
 dict(n="H1-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A ship chandler sells tarred hemp line and manila line, both by the coil. An order of "
            "7 coils of hemp line together with 4 coils of manila line came to $258, and an order "
            "of 3 coils of hemp line together with 8 coils of manila line came to $274. What does "
            "one coil of hemp line cost?"),
      choices=["$22", "$26", "$30", "$34"], correct="A",
      check="7h+4m=258 and 3h+8m=274 give h = 22 and m = 26, so a coil of hemp line is $22."),

 dict(n="H1-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A harbour pilot is paid a fixed fee for taking charge of a vessel plus a further "
            "constant amount for each hour spent on board. Taking charge of a vessel for 3 hours "
            "was billed at $410, and taking charge of a vessel for 7 hours was billed at $690. How "
            "much is billed for taking charge of a vessel for 5 hours?"),
      choices=["$410", "$480", "$520", "$550"], correct="D",
      check="The hourly amount is (690-410)/4 = 70 and the fixed fee is 410 - 3(70) = 200, so 5 "
            "hours costs 200 + 5(70) = 550."),

 dict(n="H1-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("Brine in a salt pan is left to evaporate, and its depth falls at a constant rate. The "
            "table records the depth at four moments during one day."
            + table(["Hours since measuring began", "Depth of brine (cm)"],
                    [["2", "96"], ["4", "88"], ["7", "76"], ["11", "60"]])
            + "If the depth keeps falling at this rate, how many hours after measuring began does "
              "the pan run dry?"),
      choices=["20", "22", "24", "26"], correct="D",
      check="The rate is (60-96)/(11-2) = -4 cm per hour, and 96 - 4(h-2) = 0 gives h = 26."),

 dict(n="H1-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A bottle works has 14 hours of furnace time left this week. A batch of green glass "
            "occupies the furnace for 50 minutes and a batch of flint glass occupies it for 35 "
            "minutes, and 6 batches of flint glass have already been promised to customers. How "
            "many batches of green glass can the works still make this week?"),
      choices=["10", "11", "12", "13"], correct="C",
      check="14 hours is 840 minutes; 50g + 35(6) <= 840 gives g <= 12.6, so 12 batches."),

 dict(n="H1-05", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A cargo manifest lists 46 pieces, each of them either a cask or a bale. Every cask "
            "weighs 38 kilograms and every bale weighs 22 kilograms, and the consignment weighs "
            "1,332 kilograms in all. How many casks are on the manifest?"),
      choices=["20", "24", "26", "30"], correct="A",
      check="With c casks and 46-c bales, 38c + 22(46-c) = 1,332 gives 16c = 320 and c = 20."),

 dict(n="H1-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A beekeeper keeps hives at a coastal site and at a moorland site. The number of hives "
            "at the coastal site is 4 fewer than twice the number at the moorland site. After the "
            "beekeeper carts 6 hives from the coastal site to the moorland site, the two sites hold "
            "equal numbers of hives. How many hives were at the moorland site to begin with?"),
      choices=["12", "16", "20", "28"], correct="B",
      check="With m at the moorland site the coastal site holds 2m-4, and (2m-4)-6 = m+6 gives "
            "m = 16."),

 dict(n="H1-07", domain="ALG", skill="ALG-LE", type="MC",
      stem=("The north quay and the south quay of an estuary lie 63 kilometres apart. A ferry "
            "leaves the north quay travelling toward the south quay at a steady 18 kilometres per "
            "hour, and at the same moment a faster ferry leaves the south quay travelling toward "
            "the north quay at a steady 24 kilometres per hour. How many kilometres from the north "
            "quay are the two ferries when they pass each other?"),
      choices=["18", "24", "27", "36"], correct="C",
      check="They close at 42 km per hour, so they meet after 63/42 = 1.5 hours, by which time the "
            "first ferry has covered 18(1.5) = 27 km."),

 dict(n="H1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A sail loft computes the area of a cut panel, in square feet, as "
            "\\(\\frac{9x^{2}-64}{3x+8}\\), where x is a measurement taken from the plan and "
            "\\(x>3\\). Which expression is equivalent to that area?"),
      choices=["\\(3x-8\\)", "\\(3x+8\\)", "\\(9x-8\\)", "\\(3x^{2}-8\\)"], correct="A",
      check="The numerator factors as (3x-8)(3x+8), so the quotient is 3x-8."),

 dict(n="H1-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The illumination a ship receives from a harbour beacon is modelled by "
            "\\(E=\\frac{k}{d^{2}}\\), where d is the distance from the beacon in kilometres, k is "
            "a constant, and E is the illumination in lux. At a distance of 3 kilometres the "
            "illumination is 40 lux. At what distance, in kilometres, does this model give an "
            "illumination of 10 lux?"),
      choices=["4", "5", "6", "12"], correct="C",
      check="k = 40(9) = 360, and 360/d^2 = 10 gives d^2 = 36 and d = 6."),

 dict(n="H1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A shipwright lofting a hull sets the curve and the batten so that the equation "
            "\\(2x^{2}+12x+k=0\\), where k is a constant, has exactly one real solution. What is "
            "the value of k?"),
      choices=["12", "18", "24", "36"], correct="B",
      check="One real solution means 12^2 - 4(2)k = 0, so 8k = 144 and k = 18."),

 dict(n="H1-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("An apiary's store of comb honey is drawn down by 20% of whatever remains in each month "
            "of winter. Three months into the winter the store holds 256 kilograms. How many "
            "kilograms did the store hold at the start of the winter?"),
      choices=["500", "512", "600", "640"], correct="A",
      check="The store keeps a factor of 0.8 each month, and 256/0.8^3 = 256/0.512 = 500."),

 dict(n="H1-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A glassworks converts a furnace pressure p, where \\(p>0\\), into a gauge reading g "
            "with \\(g=\\frac{p^{2}}{4}-9\\). Which expression gives p in terms of g?"),
      choices=["\\(\\sqrt{4g+9}\\)", "\\(2\\sqrt{g+9}\\)", "\\(2\\sqrt{g}+3\\)",
               "\\(\\frac{\\sqrt{g+9}}{2}\\)"], correct="B",
      check="p^2 = 4(g+9), so p = 2 times the square root of g+9."),

 dict(n="H1-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A bottle works records how many bottles it rejects each week and finds that the count "
            "fits \\(R(n)=an^{2}+c\\), where n is the number of the week and a and c are constants."
            + table(["Week n", "Bottles rejected"],
                    [["1", "14"], ["2", "26"], ["3", "46"], ["4", "74"]])
            + "How many rejected bottles does this model give for week 6?"),
      choices=["118", "130", "154", "190"], correct="C",
      check="a+c = 14 and 4a+c = 26 give a = 4 and c = 10, so R(6) = 4(36) + 10 = 154."),

 dict(n="H1-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("An indigo vat is charged with 3 kilograms of woad for every 40 litres of liquor it "
            "holds, and woad costs $7.50 a kilogram. What is the cost of the woad needed to charge "
            "a vat holding 320 litres of liquor?"),
      choices=["$150", "$180", "$210", "$240"], correct="B",
      check="320/40 = 8 lots of 3 kg is 24 kg, and 24($7.50) = $180."),

 dict(n="H1-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A bottle works raised the price of a case of jars by 15%. A merchant who buys 40 cases "
            "at a time now pays $69 more for those 40 cases than before the rise. What was the "
            "price of one case before the rise?"),
      choices=["$9.20", "$10.35", "$11.00", "$11.50"], correct="D",
      check="The rise per case is 0.15p, and 40(0.15p) = 69 gives 6p = 69 and p = 11.50."),

 dict(n="H1-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table lists the bottles a glassworks packed in one shift, by size."
            + table(["Size", "Bottles packed", "Capacity of one bottle (litres)"],
                    [["Half-pint", "400", "0.25"], ["Pint", "320", "0.50"],
                     ["Quart", "260", "1.00"], ["Magnum", "120", "1.50"]])
            + "What is the combined capacity, in litres, of all the bottles packed in the shift?"),
      choices=["620", "660", "700", "740"], correct="C",
      check="100 + 160 + 260 + 180 = 700 litres."),

 dict(n="H1-17", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("Across 9 sailings of a car ferry the mean number of vehicles carried was 46. Across "
            "the first 4 of those sailings the mean number of vehicles carried was 51. What was the "
            "mean number of vehicles carried across the other 5 sailings?"),
      answers=["42"],
      check="9(46) - 4(51) = 414 - 204 = 210 vehicles on 5 sailings, and 210/5 = 42."),

 dict(n="H1-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A bee inspector counted how many supers were standing on each hive in an apiary, and "
            "the table summarises the counts."
            + table(["Supers on the hive", "Number of hives"],
                    [["1", "4"], ["2", "7"], ["3", "9"], ["4", "5"]])
            + "What is the median number of supers per hive in this apiary?"),
      choices=["1.5", "2", "2.5", "3"], correct="D",
      check="There are 25 hives, so the median is the 13th value; 4 and 7 hives carry 1 or 2 "
            "supers, so the 13th value falls in the group carrying 3."),

 dict(n="H1-19", domain="GT", skill="GT-LA", type="MC",
      stem=("A lighthouse keeper's short ladder leans against the tower with its foot 2.8 metres "
            "from the wall and its top 9.6 metres up the wall. A long ladder leans against the same "
            "wall at the same angle, with its top 24 metres up the wall. How many metres from the "
            "wall is the foot of the long ladder?"),
      choices=["7", "8.4", "9.6", "11.2"], correct="A",
      check="The two right triangles are similar, and 24/9.6 = 2.5, so the foot is 2.5(2.8) = 7 m "
            "from the wall."),

 dict(n="H1-20", domain="GT", skill="GT-TR", type="MC",
      stem=("A hawser is made fast to a bollard on a level quay and runs straight up to a fitting "
            "on a mast, making an angle of 60&deg; with the quay. The bollard is 14 metres from the "
            "foot of the mast. How many metres of hawser run from the bollard to the fitting?"),
      choices=["24.2", "28", "32", "35"], correct="B",
      check="The bollard distance is the adjacent side, so the hawser is 14/cos 60 = 28 m."),

 dict(n="H1-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A rope walk's curing tank is a rectangular box measuring 3 metres by 1.2 metres by 0.8 "
            "metres. Tar is pumped into the empty tank at 96 litres per minute, and one cubic metre "
            "is 1,000 litres. How many minutes does the tank take to fill?"),
      answers=["30"],
      check="The tank holds 3(1.2)(0.8) = 2.88 cubic metres, which is 2,880 litres, and 2,880/96 "
            "= 30 minutes."),

 dict(n="H1-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A glassworks makes two funnels of the same shape, one a scaled copy of the other. The "
            "smaller funnel stands 12 centimetres tall and holds 96 cubic centimetres. The larger "
            "funnel stands 18 centimetres tall. How many cubic centimetres does the larger funnel "
            "hold?"),
      answers=["324"],
      check="The linear scale factor is 18/12 = 1.5, so volumes scale by 1.5^3 = 3.375, and "
            "96(3.375) = 324."),
]


# ------------------------------------------------------------ Module 2 Easy
MODULE_2_EASY = [
 dict(n="H2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A bottle works packs 12 bottles into each crate and packed 336 bottles in one "
            "morning. How many crates did the works pack that morning?"),
      choices=["28", "32", "36", "48"], correct="A",
      check="336/12 = 28."),

 dict(n="H2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A printing house charges $19 to make up the plates for a poster and then $6 for each "
            "poster printed. An order came to $97 in all. How many posters were printed?"),
      choices=["12", "13", "15", "16"], correct="B",
      check="(97-19)/6 = 13."),

 dict(n="H2E-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A pilot boat charges a $30 call-out plus $45 for each hour it is at sea. What is the "
            "total charge, in dollars, for a job lasting 4 hours?"),
      choices=["165", "180", "210", "300"], correct="C",
      check="30 + 45(4) = 210."),

 dict(n="H2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A warp beam is wound with 1,200 metres of thread, and 15 metres are woven off it each "
            "hour the loom runs. Which expression gives the number of metres of thread left on the "
            "beam after the loom has run for h hours?"),
      choices=["\\(15h-1{,}200\\)", "\\(1{,}200h-15\\)", "\\(1{,}185h\\)", "\\(1{,}200-15h\\)"],
      correct="D",
      check="Start at 1,200 metres and take away 15 metres for each hour."),

 dict(n="H2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A bee inspector must visit at least 15 apiaries this month. Which inequality gives all "
            "the possible numbers a of apiaries the inspector may visit this month?"),
      choices=["\\(a<15\\)", "\\(a\\ge 15\\)", "\\(a\\le 15\\)", "\\(a>15\\)"], correct="B",
      check="At least 15 means 15 or more."),

 dict(n="H2E-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A sailmaker uses the equation 14p+35=203 to work out the number p of panels in a sail. "
            "What is the value of p?"),
      choices=["9", "10", "12", "14"], correct="C",
      check="14p = 168, so p = 12."),

 dict(n="H2E-07", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A dock gauge reports the height of the water as H=1.8+0.6t, where H is the height in "
            "metres and t is the number of hours after low water. What does 1.8 represent in this "
            "model?"),
      choices=["The number of hours after low water at which the reading is taken.",
               "The number of metres by which the height rises each hour.",
               "The greatest height, in metres, that the water reaches.",
               "The height of the water, in metres, at low water."],
      correct="D",
      check="1.8 is the value of H when t is 0, which is the moment of low water."),

 dict(n="H2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A press run uses \\(9k+40\\) sheets of paper, and \\(3k-8\\) of those sheets are "
            "spoiled. Which expression gives the number of sheets that are not spoiled?"),
      choices=["\\(6k+48\\)", "\\(6k+32\\)", "\\(12k+32\\)", "\\(6k-48\\)"], correct="A",
      check="(9k+40) - (3k-8) = 6k + 48."),

 dict(n="H2E-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A glassblower models the volume of a hollow float of radius r centimetres as "
            "\\(V(r)=2r^{3}\\) cubic centimetres. What volume does the model give for a float of "
            "radius 3 centimetres?"),
      choices=["18", "54", "72", "216"], correct="B",
      check="2(3^3) = 2(27) = 54."),

 dict(n="H2E-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A rigger solves \\(3x^{2}=75\\) and keeps only the positive solution. What is that "
            "solution?"),
      choices=["3", "4", "5", "25"], correct="C",
      check="x^2 = 25, so the positive solution is 5."),

 dict(n="H2E-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A printing house rates a press by \\(E(n)=\\frac{120}{n+2}\\), where n is the number "
            "of colours the press lays down. What is the rating when the press lays down 8 "
            "colours?"),
      choices=["8", "10", "11", "12"], correct="D",
      check="120/(8+2) = 120/10 = 12."),

 dict(n="H2E-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A glass batch is scaled up by the factor \\(27^{\\frac{2}{3}}\\). What is the value of "
            "that factor?"),
      choices=["9", "18", "27", "81"], correct="A",
      check="The cube root of 27 is 3, and 3 squared is 9."),

 dict(n="H2E-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The number of brood cells in a young hive is modelled by \\(C(d)=200(2)^{d}\\), where "
            "d is the number of days since the queen began laying. How many brood cells does the "
            "model give after 4 days?"),
      choices=["1,600", "3,200", "4,000", "6,400"], correct="B",
      check="200(2^4) = 200(16) = 3,200."),

 dict(n="H2E-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A ferry burns 38 litres of fuel for each nautical mile it steams. How many litres does "
            "it burn on a crossing of 24 nautical miles?"),
      choices=["684", "874", "912", "950"], correct="C",
      check="38(24) = 912."),

 dict(n="H2E-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A cargo of 750 crates was landed, and 12% of the crates were damaged. How many of the "
            "crates were damaged?"),
      choices=["90", "96", "105", "120"], correct="A",
      check="0.12(750) = 90."),

 dict(n="H2E-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of casks landed at a quay on each of four days."
            + table(["Day", "Casks landed"],
                    [["Monday", "48"], ["Tuesday", "63"], ["Wednesday", "51"], ["Thursday", "90"]])
            + "How many more casks were landed on Thursday than on Tuesday?"),
      choices=["21", "27", "39", "42"], correct="B",
      check="90 - 63 = 27."),

 dict(n="H2E-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("On six nights a lighthouse keeper logged 12, 9, 15, 9, 11 and 16 vessels passing the "
            "light. What is the mean of the six figures?"),
      choices=["9", "11.5", "12", "15"], correct="C",
      check="The six figures total 72, and 72/6 = 12."),

 dict(n="H2E-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A crate holds 40 bottles, 9 of which are flawed. One bottle is drawn from the crate at "
            "random. What is the probability that the bottle drawn is flawed?"),
      choices=["\\(\\frac{9}{40}\\)", "\\(\\frac{9}{31}\\)", "\\(\\frac{31}{40}\\)",
               "\\(\\frac{1}{9}\\)"], correct="A",
      check="9 flawed bottles out of 40 gives a probability of 9/40."),

 dict(n="H2E-19", domain="GT", skill="GT-LA", type="MC",
      stem=("A sailmaker cuts a four-sided storm cover whose first three corners measure 95&deg;, "
            "78&deg; and 120&deg;. What is the measure, in degrees, of the fourth corner?"),
      choices=["47", "57", "62", "67"], correct="D",
      check="The four angles of a quadrilateral total 360, and 360 - 95 - 78 - 120 = 67."),

 dict(n="H2E-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A salt pan is a rectangle measuring 32 metres by 18 metres. What is the area, in "
            "square metres, of the pan?"),
      answers=["576"],
      check="32(18) = 576."),

 dict(n="H2E-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A circular buoy has a waterline whose circumference is \\(14\\pi\\) metres. What is "
            "the radius, in metres, of that waterline?"),
      answers=["7"],
      check="The circumference is 2 pi r, so 2r = 14 and r = 7."),

 dict(n="H2E-22", domain="GT", skill="GT-LA", type="FR",
      stem=("A ferry's boarding ramp is 10 metres long and lifts cargo 6 metres from the quay up to "
            "the car deck. How many metres does the ramp reach out horizontally?"),
      answers=["8"],
      check="The ramp is the hypotenuse, so the horizontal reach is the square root of 10^2 - 6^2, "
            "which is 8."),
]


# ------------------------------------------------------------ Module 2 Hard
MODULE_2_HARD = [
 dict(n="H2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A ferry company charges freight by the tonne, at one rate for salt and another rate "
            "for glass sand. Carrying 5 tonnes of salt together with 2 tonnes of glass sand costs "
            "$94, and carrying 2 tonnes of salt together with 5 tonnes of glass sand costs $109. "
            "What does it cost to carry 1 tonne of salt together with 1 tonne of glass sand?"),
      choices=["$29", "$34", "$47", "$58"], correct="A",
      check="Adding the two conditions gives 7x + 7y = 203, so x + y = 29 without either rate "
            "having to be found separately."),

 dict(n="H2H-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A harbour master applies a tide correction \\(f(x)\\) to a gauge reading x, and f is a "
            "linear function. The table gives two entries from the correction sheet."
            + table(["Reading x", "Correction \\(f(x)\\)"], [["3", "-2"], ["11", "14"]])
            + "What is the value of \\(f(0)\\)?"),
      choices=["-11", "-8", "-5", "2"], correct="B",
      check="The slope is (14+2)/(11-3) = 2, so f(x) = 2x - 8 and f(0) = -8."),

 dict(n="H2H-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A freight ferry may carry a total of at most 4,200 kilograms on its cargo deck. Each "
            "pallet of glass weighs 180 kilograms and each pallet of salt weighs 120 kilograms, and "
            "the operator requires at least twice as many salt pallets as glass pallets on every "
            "sailing. On a sailing carrying exactly 9 pallets of glass, what is the greatest number "
            "of pallets of salt the ferry can carry?"),
      choices=["18", "20", "21", "25"], correct="C",
      check="180(9) = 1,620 kg leaves 2,580 kg, and 2,580/120 = 21.5, so 21 pallets, which also "
            "meets the requirement of at least 18."),

 dict(n="H2H-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A stowage calculation uses the system<br/>3x+2y=17<br/>5x-4y=k<br/>where x and y are "
            "the numbers of tonnes of two cargoes and k is a constant. The solution of this system "
            "has y=4. What is the value of k?"),
      choices=["-11", "-7", "-4", "-1"], correct="D",
      check="y = 4 makes 3x + 8 = 17, so x = 3, and k = 5(3) - 4(4) = -1."),

 dict(n="H2H-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A ferry company sets the fare for a crossing of d nautical miles as F=a+bd dollars, "
            "where a and b are constants. A crossing of 12 nautical miles costs $39 and a crossing "
            "of 20 nautical miles costs $59. Which expression gives F in terms of d?"),
      choices=["\\(9+2.5d\\)", "\\(2.5+9d\\)", "\\(15+2d\\)", "\\(39+2.5d\\)"], correct="A",
      check="b = (59-39)/8 = 2.5 and a = 39 - 12(2.5) = 9."),

 dict(n="H2H-06", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A glassworks must turn out at least 500 bottles in a day. Its older machine turns out "
            "40 bottles an hour and its newer machine turns out 65 bottles an hour, and the two "
            "machines run independently of each other. If the older machine runs for a hours and "
            "the newer machine runs for b hours, which inequality must hold if the day's target is "
            "met?"),
      choices=["\\(40a+65b\\le 500\\)", "\\(40a+65b\\ge 500\\)", "\\(65a+40b\\ge 500\\)",
               "\\(105(a+b)\\ge 500\\)"], correct="B",
      check="Each machine's output is its rate times its running time, and the two outputs together "
            "must reach 500."),

 dict(n="H2H-07", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A printing house bought 3 reams of laid paper and 4 reams of wove paper for $131, and "
            "on another day bought 5 reams of laid paper and 2 reams of wove paper for $139. How "
            "many dollars more does one ream of laid paper cost than one ream of wove paper?"),
      answers=["4"],
      check="The system gives laid paper at $21 a ream and wove paper at $17 a ream, a difference "
            "of $4."),

 dict(n="H2H-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A dyeing line puts every skein through two stages. The first stage converts a raw "
            "reading x into \\(g(x)=\\frac{x}{2}+3\\), and the second stage converts a value u "
            "coming out of the first stage into \\(f(u)=u^{2}-4u\\). Which expression gives "
            "\\(f(g(x))\\)?"),
      choices=["\\(\\frac{x^{2}}{4}+3x-3\\)", "\\(\\frac{x^{2}}{2}+x-3\\)",
               "\\(\\frac{x^{2}}{4}+x-3\\)", "\\(\\frac{x^{2}}{4}-x+3\\)"], correct="C",
      check="Squaring x/2 + 3 gives x^2/4 + 3x + 9, and subtracting 4(x/2+3) = 2x + 12 leaves "
            "x^2/4 + x - 3."),

 dict(n="H2H-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A glassworks writes the difference of two cooling rates as "
            "\\(\\frac{2}{x-3}-\\frac{1}{x+2}\\), where \\(x>3\\). Which expression is equivalent "
            "to that difference?"),
      choices=["\\(\\frac{1}{(x-3)(x+2)}\\)", "\\(\\frac{x-7}{(x-3)(x+2)}\\)",
               "\\(\\frac{2x+7}{(x-3)(x+2)}\\)", "\\(\\frac{x+7}{(x-3)(x+2)}\\)"], correct="D",
      check="Over the common denominator the numerator is 2(x+2) - (x-3) = x + 7."),

 dict(n="H2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("Setting a press's feed reduces to the equation \\(\\frac{6}{x-2}=x+3\\), where "
            "\\(x\\ne 2\\). What is the sum of all the solutions of this equation?"),
      choices=["-1", "1", "3", "4"], correct="A",
      check="Multiplying out gives x^2 + x - 12 = 0, whose solutions 3 and -4 sum to -1."),

 dict(n="H2H-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A glass furnace's temperature deviation is modelled by \\(d(x)=a(x-6)^{2}-40\\), where "
            "x is the number of hours since firing began, a is a positive constant, and d is "
            "measured in degrees Celsius. The model gives \\(d(2)=8\\). What is the value of "
            "\\(d(9)\\)?"),
      choices=["-32", "-13", "-4", "23"], correct="B",
      check="a(16) - 40 = 8 gives a = 3, so d(9) = 3(9) - 40 = -13."),

 dict(n="H2H-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A bottle works records a mould-scaling factor as "
            "\\(\\frac{(4x^{3}y)^{2}}{8x^{4}y^{3}}\\), where x and y are positive. Which expression "
            "is equivalent to it?"),
      choices=["\\(\\frac{x^{2}}{2y}\\)", "\\(2x^{2}y\\)", "\\(\\frac{2x^{2}}{y}\\)",
               "\\(\\frac{2x^{2}}{y^{2}}\\)"], correct="C",
      check="The numerator is 16x^6y^2, and dividing by 8x^4y^3 leaves 2x^2/y."),

 dict(n="H2H-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("In the xy-plane, the lowest point of the parabola \\(y=3x^{2}-12x+7\\) is "
            "\\((h,k)\\). What is the value of h+k?"),
      choices=["-9", "-7", "-5", "-3"], correct="D",
      check="h = 12/6 = 2 and k = 3(4) - 24 + 7 = -5, so h + k = -3."),

 dict(n="H2H-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("At a rope walk, one tarring machine can coat a whole batch of rope in 6 hours and a "
            "second machine can coat the same batch in 12 hours. If both machines work on one batch "
            "at the same time, each at its own steady rate, how many hours does the batch take?"),
      choices=["4", "4.5", "6", "9"], correct="A",
      check="Together they coat 1/6 + 1/12 = 1/4 of a batch an hour, so a batch takes 4 hours."),

 dict(n="H2H-15", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A glassworks drew 200 bottles at random from one day's output of 15,000 bottles and "
            "found 6 of the 200 to be flawed. Based on this sample, which of the following is the "
            "best estimate of the number of flawed bottles in that day's output?"),
      choices=["300", "450", "600", "750"], correct="B",
      check="6/200 of 15,000 is 450."),

 dict(n="H2H-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the tonnage of each of four cargoes landed from one vessel, together "
            "with the price the merchant received for each tonne."
            + table(["Cargo", "Tonnes landed", "Price per tonne"],
                    [["Salt", "120", "$45"], ["Baled wool", "40", "$130"],
                     ["Glass sand", "90", "$62"], ["Coiled rope", "55", "$98"]])
            + "Which cargo earned the merchant the most money?"),
      choices=["Salt", "Baled wool", "Glass sand", "Coiled rope"], correct="C",
      check="The four cargoes earned $5,400, $5,200, $5,580 and $5,390, so glass sand earned the "
            "most."),

 dict(n="H2H-17", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("A quay holds 12 bales of raw wool whose mean mass is 84 kilograms. One bale is carted "
            "away, and the mean mass of the 11 bales left behind is 82 kilograms. What is the mass, "
            "in kilograms, of the bale that was carted away?"),
      answers=["106"],
      check="12(84) - 11(82) = 1,008 - 902 = 106."),

 dict(n="H2H-18", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A bottle works cut the number of bottles it rejects by 25% in one year and then cut "
            "the reduced number by a further 20% in the next year. It rejected 240 bottles in the "
            "second of those years. How many bottles did it reject in the year before either cut?"),
      choices=["288", "320", "360", "400"], correct="D",
      check="The two cuts leave a factor of 0.75(0.80) = 0.60, and 240/0.60 = 400."),

 dict(n="H2H-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A solid glass float in the shape of a sphere of radius 6 centimetres is melted down "
            "and recast, with none of the glass lost, as a solid cylinder 18 centimetres tall. What "
            "is the radius, in centimetres, of the cylinder?"),
      choices=["3", "4", "6", "8"], correct="B",
      check="The sphere holds 288 pi cubic centimetres, and 18 pi r^2 = 288 pi gives r^2 = 16 and "
            "r = 4."),

 dict(n="H2H-20", domain="GT", skill="GT-LA", type="MC",
      stem=("A sailmaker lofts a triangular staysail \\(ABC\\) in which the angle at A measures "
            "twice the angle at B. The side \\(AC\\) is extended beyond C, and the angle between "
            "that extension and the side \\(BC\\) measures 129&deg;. What is the measure, in "
            "degrees, of the angle at B?"),
      choices=["39", "41", "43", "51"], correct="C",
      check="That exterior angle equals the sum of the angles at A and B, so 2B + B = 129 and "
            "B = 43."),

 dict(n="H2H-21", domain="GT", skill="GT-TR", type="MC",
      stem=("A drawing office sets out a right triangle \\(PQR\\) with its right angle at Q, so "
            "\\(PR\\) is the longest side. The office records \\(\\sin R=\\frac{8}{17}\\) and "
            "\\(PR=51\\). What is the length of \\(QR\\)?"),
      choices=["45", "48", "51", "54"], correct="A",
      check="sin R = PQ/PR gives PQ = 24, and the square root of 51^2 - 24^2 is 45."),

 dict(n="H2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A tide mill's grain hopper is a rectangular box whose length is twice its width and "
            "whose height is 3 metres. The hopper holds 150 cubic metres. What is the width, in "
            "metres, of the hopper?"),
      answers=["5"],
      check="2w(w)(3) = 150 gives w^2 = 25 and w = 5."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
