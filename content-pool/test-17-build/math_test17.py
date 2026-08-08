#!/usr/bin/env python3
"""
Original Math content for Test 17 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium, deliberately harder than a stock Module 1. Almost
                every item makes a constant, a rate, a unit price or an unknown
                be recovered first and only then used; two or three steps
                throughout. Clearly above Module 2 (Easy), clearly below
                Module 2 (Hard).
  MODULE_2_EASY genuinely one-step — the lower branch of the adaptive split.
  MODULE_2_HARD hard, and harder than a stock hard module: parameters instead
                of numbers, structural and symbolic answer choices, a composed
                function, a system conditioned on a constant, an inequality
                chain, and geometry that needs two relationships chained.

Every setting is drawn from Test 17's assigned thematic territory — mountain
and land survey, dairying and cheesemaking, railway operation and signalling,
ceramics and kiln firing, forestry and timber yards, drystone walling, hill
farming, cable cars and funiculars, reservoir management, sheep shearing,
narrow-gauge haulage, seed drills, hedge laying and contour mapping — and is
deliberately unlike anything already banked in production.

House style follows Test 1/2 (see CLAUDE.md): bare HTML stems, simple inline
maths left as plain text, real <table> markup for every data table, &deg; as an
entity. All LaTeX is typed by hand; no bulk conversion step was used anywhere
in this file.
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
      stem=("A narrow-gauge line carries slate in two sizes of wagon, and each large wagon holds "
            "3 times as much slate as each small wagon. A train made up of 6 large wagons and 11 "
            "small wagons carries 87 tonnes of slate when every wagon is full. How many tonnes of "
            "slate does one full large wagon hold?"),
      choices=["3", "5", "6", "9"], correct="D",
      check="With s tonnes in a small wagon, 18s + 11s = 29s = 87, so s = 3 and a large wagon holds 9."),

 dict(n="H1-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A dairy presses two cheeses. Every truckle of Cheddar takes 11 litres of milk and "
            "every truckle of Caerphilly takes 7 litres. In one day the dairy pressed 40 truckles "
            "altogether and used 356 litres of milk. How many truckles of Caerphilly did it press "
            "that day?"),
      choices=["12", "16", "19", "21"], correct="D",
      check="11d + 7(40-d) = 356 gives d = 19 truckles of Cheddar, leaving 40 - 19 = 21 of Caerphilly."),

 dict(n="H1-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A hill path climbs so steadily that its height above sea level is a linear function of "
            "the distance walked along it. A survey found the path 412 metres above sea level at "
            "250 metres along, and 542 metres above sea level at 900 metres along. A summit cairn "
            "on the same path stands 620 metres above sea level. How many metres along the path is "
            "the cairn?"),
      choices=["1,040", "1,290", "1,350", "3,100"], correct="B",
      check="The path rises 130 m over 650 m, a gradient of 0.2; 208/0.2 = 1,040 m beyond the 250 m mark."),

 dict(n="H1-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A seed drill sows at a constant rate once it is set up, and setting it up at the gate "
            "of a field takes the same fixed time every time. Sowing a field of 3.5 hectares took "
            "91 minutes altogether, and sowing a field of 6 hectares took 151 minutes altogether. "
            "How many of those minutes are the set-up time?"),
      choices=["7", "12", "19", "26"], correct="A",
      check="60 extra minutes for 2.5 extra hectares is 24 minutes per hectare, so 91 - 3.5(24) = 7."),

 dict(n="H1-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A drystone waller may put no more than 260 kilograms in one barrow load. Each coping "
            "stone has a mass of 34 kilograms and each hearting stone has a mass of 9 kilograms, "
            "and the waller must take 6 coping stones in this load. What is the greatest number of "
            "hearting stones the waller can add to the same load?"),
      choices=["5", "6", "7", "9"], correct="B",
      check="204 kg of coping leaves 56 kg, and 56/9 is between 6 and 7, so 6 hearting stones."),

 dict(n="H1-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("The lever frame in a signal box holds 44 levers. The number of point levers is 4 fewer "
            "than twice the number of signal levers, and the remaining 6 levers are spares. How "
            "many signal levers does the frame hold?"),
      choices=["12", "14", "16", "18"], correct="B",
      check="v + (2v-4) + 6 = 44 gives 3v = 42 and v = 14, with 24 point levers and 6 spares."),

 dict(n="H1-07", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A cheesemaker judges a vat by its yield index Y, defined by \\(Y=\\frac{5m}{m+4}\\), "
            "where m is the mass of curd drawn from the vat in kilograms and \\(0 < Y < 5\\). Which "
            "expression gives m in terms of Y?"),
      choices=["\\(\\frac{4Y}{5-Y}\\)", "\\(\\frac{4Y}{Y-5}\\)", "\\(\\frac{5Y}{Y+4}\\)",
               "\\(\\frac{Y-4}{5}\\)"], correct="A",
      check="Y(m+4) = 5m gives 4Y = m(5-Y), so m = 4Y/(5-Y)."),

 dict(n="H1-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A timber yard finds that the daily profit, in dollars, from selling oak planks at a "
            "price of p dollars each is \\(R(p)=(150-5p)(p-8)\\). At what price, in dollars, is the "
            "daily profit greatest?"),
      choices=["8", "14", "19", "30"], correct="C",
      check="The profit is zero at p = 8 and p = 30, so the greatest value is midway, at p = 19."),

 dict(n="H1-09", domain="ADV", skill="ADV-NE", type="MC",
      stem=("After a check dam is built, the silt reaching a reservoir each year is modelled by "
            "\\(f(t)=v(0.6)^{t}\\) tonnes, where t is the number of years since the dam was built "
            "and v is a constant. In the third year after the dam was built, 1,296 tonnes of silt "
            "reached the reservoir. How many tonnes reached it in the year the dam was built?"),
      choices=["2,160", "3,600", "4,320", "6,000"], correct="D",
      check="v(0.6)^3 = 0.216v = 1,296 gives v = 6,000."),

 dict(n="H1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A mountaineering club estimates the time, in minutes, that a laden party takes to "
            "climb a slope as \\(T=9\\sqrt{r}+12\\), where r is the rise of the slope in metres. A "
            "climb estimated at 93 minutes has what rise, in metres?"),
      choices=["9", "27", "81", "121"], correct="C",
      check="9 sqrt(r) = 81 gives sqrt(r) = 9 and r = 81."),

 dict(n="H1-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The load a squared timber beam of a given span can carry is modelled by "
            "\\(L(b)=cb^{2}\\) kilograms, where b is the breadth of the beam in centimetres and c "
            "is a constant. A beam of breadth 6 centimetres carries 900 kilograms. What load, in "
            "kilograms, does a beam of breadth 10 centimetres carry under this model?"),
      choices=["1,500", "1,800", "2,100", "2,500"], correct="D",
      check="900 = c(36) gives c = 25, so L(10) = 25(100) = 2,500."),

 dict(n="H1-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A ceramicist writes the area of a rectangular kiln shelf, in square centimetres, both "
            "as \\((3x+m)(2x-5)\\) and as \\(6x^{2}-7x-20\\), where x is a length in centimetres "
            "and m is a constant. What is the value of m?"),
      choices=["2", "4", "5", "8"], correct="B",
      check="Expanding gives 6x^2 + (2m-15)x - 5m, so -5m = -20 and m = 4, which also makes 2m-15 = -7."),

 dict(n="H1-13", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A shearing gang works at a steady rate of 18 ewes every 25 minutes and shears for 6 "
            "hours a day. How many days does the gang need to shear a flock of 1,296 ewes?"),
      choices=["5", "6", "8", "10"], correct="A",
      check="1,296/18 = 72 lots of 25 minutes is 1,800 minutes, or 30 hours, which is 5 days of 6 hours."),

 dict(n="H1-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Green oak has a mass of 1.05 tonnes for every cubic metre, and it loses 28% of that "
            "mass while it is seasoned. A timber yard seasons 40 cubic metres of green oak. What is "
            "the mass, in tonnes, of the seasoned timber?"),
      choices=["25.2", "28.8", "29.4", "30.24"], correct="D",
      check="40(1.05) = 42 tonnes green, and 42(0.72) = 30.24 tonnes seasoned."),

 dict(n="H1-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("A contour map records the area of ground on one hill that lies above each of four "
            "heights."
            + table(["Height above sea level (m)", "Area of ground above that height (ha)"],
                    [["400", "80"], ["500", "52"], ["600", "30"], ["700", "12"]])
            + "Of the ground lying above 400 metres, what percent lies below 600 metres?"),
      choices=["37.5%", "50%", "62.5%", "75%"], correct="C",
      check="80 - 30 = 50 hectares of the 80 hectares above 400 m, and 50/80 = 62.5%."),

 dict(n="H1-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A dairy runs 300 litres of milk testing 4.2% butterfat into a vat together with 200 "
            "litres testing 3.7% butterfat. What percent butterfat does the mixture in the vat "
            "test?"),
      choices=["3.85%", "3.95%", "4.00%", "4.15%"], correct="C",
      check="300(4.2) + 200(3.7) = 2,000 units of butterfat over 500 litres, which is 4.00%."),

 dict(n="H1-17", domain="GT", skill="GT-TR", type="MC",
      stem=("A cable car runs in a straight line up a slope that makes an angle of 30&deg; with the "
            "horizontal, and its upper station stands 420 metres higher than its lower station. New "
            "haulage cable costs $18 for each metre. What is the cost of a length of cable equal to "
            "the straight run between the two stations?"),
      choices=["$7,560", "$12,600", "$15,120", "$30,240"], correct="C",
      check="The run is 420/sin 30 = 840 metres, and 840(18) = 15,120."),

 dict(n="H1-18", domain="GT", skill="GT-LA", type="MC",
      stem=("A drystone wall runs in a straight line across a fell, and two straight sheep tracks "
            "cross it. The two tracks are parallel to each other. Where the first track crosses the "
            "wall the acute angle measures \\((4x-10)\\)&deg;, and where the second track crosses "
            "the wall the obtuse angle on the same side of the wall measures \\((6x+40)\\)&deg;. "
            "What is the value of x?"),
      choices=["13", "15", "17", "25"], correct="B",
      check="The two marked angles are supplementary, so 10x + 30 = 180 and x = 15."),

 dict(n="H1-19", domain="GT", skill="GT-AV", type="MC",
      stem=("The firing chamber of a kiln is a rectangular box 90 centimetres long, 60 centimetres "
            "wide and 75 centimetres high. The shelves inside take up 12% of the chamber's volume, "
            "and each pot loaded into what is left takes up 1,800 cubic centimetres. How many pots "
            "can the chamber hold?"),
      choices=["176", "180", "198", "225"], correct="C",
      check="The chamber is 405,000 cubic cm, 88% of which is 356,400, and 356,400/1,800 = 198."),

 dict(n="H1-20", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("A forester measured the girths of 9 beeches in one compartment and found a mean girth of "
            "128 centimetres. One of the 9 measurements, recorded as 96 centimetres, was later "
            "found to belong to a tree outside the compartment and was struck out. What is the "
            "mean girth, in centimetres, of the 8 measurements that remain?"),
      answers=["132"],
      check="9(128) = 1,152, and (1,152 - 96)/8 = 1,056/8 = 132."),

 dict(n="H1-21", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A narrow-gauge locomotive hauls a loaded train at a steady 12 kilometres per hour on "
            "the level and at a steady 8 kilometres per hour on the incline. One journey covers 30 "
            "kilometres, of which 6 kilometres are on the incline and the rest on the level. How "
            "many minutes does the journey take?"),
      answers=["165"],
      check="24/12 = 2 hours on the level and 6/8 = 0.75 hours on the incline, a total of 2.75 hours."),

 dict(n="H1-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A drystone wall has the same cross-section along its whole length: a trapezium 1.2 "
            "metres wide at the base, 0.6 metres wide at the top and 1.5 metres high. The wall runs "
            "for 40 metres. How many cubic metres of stone does the wall contain?"),
      answers=["54"],
      check="The cross-section is (1.2+0.6)/2 times 1.5 = 1.35 square metres, and 1.35(40) = 54."),
]


# ------------------------------------------------------------ Module 2 Easy
MODULE_2_EASY = [
 dict(n="H2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A cheese press takes 8 truckles at a time. A dairy pressed 96 truckles in one day, "
            "filling the press completely each time it was used. How many times was the press "
            "used?"),
      choices=["8", "10", "12", "14"], correct="C",
      check="96/8 = 12."),

 dict(n="H2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A drystone waller dressed 340 stones. Of these, 85 went on the coping and the rest "
            "were shared equally between 5 sections of wall. How many of the dressed stones went "
            "into each section?"),
      choices=["45", "48", "51", "68"], correct="C",
      check="(340 - 85)/5 = 255/5 = 51."),

 dict(n="H2E-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A funicular charges a $6 platform fee plus $3 for each kilometre travelled. What is "
            "the total charge, in dollars, for a journey of 9 kilometres?"),
      choices=["24", "27", "30", "33"], correct="D",
      check="6 + 3(9) = 33."),

 dict(n="H2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A narrow-gauge line records the mass a wagon carries against the depth of slate loaded "
            "into it, and the record is a straight line in the xy-plane through the points "
            "\\((2,15)\\) and \\((6,39)\\). What is the slope of that line?"),
      choices=["6", "8", "12", "24"], correct="A",
      check="(39-15)/(6-2) = 24/4 = 6."),

 dict(n="H2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("No more than 6 people may stand in a signal box at one time. There are already 2 "
            "people in the box. What is the greatest number of further people who may enter?"),
      choices=["4", "6", "8", "10"], correct="A",
      check="6 - 2 = 4."),

 dict(n="H2E-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A kiln firing schedule sets the total firing time, in minutes, by the equation "
            "7t+16=709, where t is the number of minutes spent at each of 7 holding stages. What is "
            "the value of t?"),
      choices=["85", "91", "95", "99"], correct="D",
      check="7t = 693, so t = 99."),

 dict(n="H2E-07", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A kiln is loaded with \\(9p+14\\) pots, of which \\(4p+5\\) have been glazed. Which "
            "expression gives the number of pots in the kiln that have not been glazed?"),
      choices=["\\(5p-9\\)", "\\(5p+9\\)", "\\(5p+19\\)", "\\(13p+19\\)"], correct="B",
      check="(9p+14) - (4p+5) = 5p + 9."),

 dict(n="H2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A ceramicist records a shrinkage factor as \\(\\frac{c^{9}}{c^{4}}\\), where "
            "\\(c>1\\). Which expression is equivalent to that factor?"),
      choices=["\\(c^{\\frac{9}{4}}\\)", "\\(c^{13}\\)", "\\(c^{36}\\)", "\\(c^{5}\\)"],
      correct="D",
      check="Subtract the exponents: 9 - 4 = 5."),

 dict(n="H2E-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A drystone waller lays courses that narrow as the wall rises, so that the nth course "
            "takes \\(45-2n\\) stones. How many stones does the 8th course take?"),
      choices=["29", "31", "37", "45"], correct="A",
      check="45 - 2(8) = 29."),

 dict(n="H2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A funicular company's repair fund is modelled by \\(V(y)=2{,}000(1.5)^{y}\\) dollars, "
            "where y is the number of years since the fund was opened. How many dollars does the "
            "model give for the fund 2 years after it was opened?"),
      choices=["3,000", "4,500", "6,000", "6,750"], correct="B",
      check="2,000(1.5)^2 = 2,000(2.25) = 4,500."),

 dict(n="H2E-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A nursery bed's spruce seedlings triple in number every year, so that the bed holds "
            "\\(40\\cdot 3^{y}\\) seedlings after y years. After how many years does the bed hold "
            "1,080 seedlings?"),
      choices=["1", "2", "3", "27"], correct="C",
      check="1,080/40 = 27 = 3^3, so y = 3."),

 dict(n="H2E-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A survey office corrects a raw offset x with the function \\(f(x)=x^{2}-6x\\). What is "
            "the value of \\(f(-2)\\)?"),
      choices=["-8", "8", "16", "20"], correct="C",
      check="4 - (-12) = 4 + 12 = 16."),

 dict(n="H2E-13", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Each wagon on a narrow-gauge slate train carries 1.4 tonnes. How many tonnes does a "
            "train of 25 such wagons carry?"),
      choices=["3.5", "26.4", "33.6", "35"], correct="D",
      check="25(1.4) = 35."),

 dict(n="H2E-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Of the 250 lambs born on a hill farm one spring, 45 were twins. What percent of the "
            "lambs born that spring were twins?"),
      choices=["15%", "18%", "20%", "22.5%"], correct="B",
      check="45/250 = 0.18, which is 18%."),

 dict(n="H2E-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("A milk lorry called at four hill farms one morning. The table gives the number of "
            "churns it collected at each farm."
            + table(["Farm", "Churns collected"],
                    [["Fellgarth", "14"], ["Gill Head", "9"], ["Rowantree", "17"],
                     ["Sourmire", "12"]])
            + "How many churns did the lorry collect altogether?"),
      choices=["43", "48", "52", "56"], correct="C",
      check="14 + 9 + 17 + 12 = 52."),

 dict(n="H2E-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The fleeces taken from five ewes had masses, in kilograms, of 2.6, 3.1, 3.4, 3.4 and "
            "4.0. What is the median of these five masses, in kilograms?"),
      choices=["3.0", "3.1", "3.3", "3.4"], correct="D",
      check="The masses are already in order and the middle one is 3.4."),

 dict(n="H2E-17", domain="GT", skill="GT-LA", type="MC",
      stem=("Two straight fence lines cross each other on level ground. One of the four angles they "
            "make measures 118&deg;. What is the measure, in degrees, of an angle adjacent to it?"),
      choices=["28", "62", "72", "118"], correct="B",
      check="Adjacent angles on a straight line add to 180, and 180 - 118 = 62."),

 dict(n="H2E-18", domain="GT", skill="GT-AV", type="MC",
      stem=("A circular sheep fold has a radius of 9 metres. What is the circumference of the fold, "
            "in metres?"),
      choices=["\\(9\\pi\\)", "\\(18\\pi\\)", "\\(36\\pi\\)", "\\(81\\pi\\)"], correct="B",
      check="The circumference is 2 pi r = 18 pi."),

 dict(n="H2E-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A rectangular hay meadow measures 140 metres by 85 metres. How many metres of hedge "
            "are needed to enclose the meadow completely?"),
      choices=["225", "450", "900", "11,900"], correct="B",
      check="2(140 + 85) = 450."),

 dict(n="H2E-20", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("Five firings of a kiln used 38, 44, 41, 47 and 40 kilowatt-hours of electricity. What "
            "is the mean number of kilowatt-hours used per firing?"),
      answers=["42"],
      check="(38+44+41+47+40)/5 = 210/5 = 42."),

 dict(n="H2E-21", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A cable car makes 14 trips up the mountain each day and carries 32 passengers on every "
            "trip up. How many passengers does it carry up the mountain in one day?"),
      answers=["448"],
      check="14(32) = 448."),

 dict(n="H2E-22", domain="GT", skill="GT-TR", type="FR",
      stem=("A funicular track runs straight up a hillside for 250 metres and rises 150 metres "
            "vertically over that run. How many metres does the track advance horizontally over the "
            "same run?"),
      answers=["200"],
      check="The horizontal advance is sqrt(250^2 - 150^2) = sqrt(40,000) = 200."),
]


# ------------------------------------------------------------ Module 2 Hard
MODULE_2_HARD = [
 dict(n="H2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A survey office writes down two conditions on the same triangulation check:<br/>"
            "\\(6x-4y=14\\)<br/>\\(9x+cy=21\\)<br/>where c is a constant. Every pair "
            "\\((x,y)\\) that satisfies the first condition also satisfies the second. What is the "
            "value of c?"),
      choices=["-6", "-4", "4", "6"], correct="A",
      check="The second equation must be 3/2 times the first: 3/2 of 6 is 9 and of 14 is 21, so c = 3/2 of -4 = -6."),

 dict(n="H2H-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A cheesemaker's ripening model is a linear function f for which \\(f(3)=k\\) and "
            "\\(f(11)=k+52\\), where k is a constant. What is the value of \\(f(7)-f(5)\\)?"),
      choices=["6.5", "13", "26", "52"], correct="B",
      check="The slope is 52/8 = 6.5 whatever k is, and 7 - 5 = 2, so the difference is 13."),

 dict(n="H2H-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A hill farmer must spread at least 55 kilograms of lime on every hectare treated, and "
            "no more than 80 kilograms on every hectare treated. One full tank holds 1,320 "
            "kilograms of lime. Which inequality gives all the possible numbers h of hectares that "
            "one full tank can treat at an allowed rate?"),
      choices=["\\(16.5\\le h\\le 80\\)", "\\(24\\le h\\le 55\\)", "\\(55\\le h\\le 80\\)",
               "\\(16.5\\le h\\le 24\\)"], correct="D",
      check="The heaviest allowed rate treats 1,320/80 = 16.5 ha and the lightest treats 1,320/55 = 24 ha."),

 dict(n="H2H-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("Two survey parties leave the same cairn at the same moment and walk in opposite "
            "directions along a ridge, each at its own constant speed. One party walks 1.5 "
            "kilometres per hour faster than the other, and after 4 hours the parties are 26 "
            "kilometres apart. How many kilometres per hour does the faster party walk?"),
      choices=["2.5", "3.25", "4", "5.5"], correct="C",
      check="4(u + u + 1.5) = 26 gives 8u = 20 and u = 2.5, so the faster party walks 4."),

 dict(n="H2H-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("On a survey plan a drainage cut is drawn through the point \\((-3,7)\\) and "
            "perpendicular to the fence line \\(4x-6y=15\\). Which equation defines the drainage "
            "cut?"),
      choices=["\\(2x-3y=-27\\)", "\\(2x+3y=15\\)", "\\(3x+2y=-5\\)", "\\(3x+2y=5\\)"],
      correct="D",
      check="The fence line has slope 2/3, so the cut has slope -3/2; through (-3,7) that is 3x + 2y = 5."),

 dict(n="H2H-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A shearing contract pays $2.40 for every ewe shorn cleanly, while a ewe that is nicked "
            "earns nothing and costs the shearer a further $0.90 in penalty. After working "
            "through a flock of 320 ewes, a shearer was paid $715.20. How many of the ewes were "
            "nicked?"),
      choices=["12", "16", "22", "24"], correct="B",
      check="2.40(320-w) - 0.90w = 768 - 3.30w = 715.20 gives 3.30w = 52.80 and w = 16."),

 dict(n="H2H-07", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A timber-drying schedule applies \\(h(x)=3x+2\\) and then \\(k(x)=x^{2}-5x\\), so that "
            "the output of h becomes the input of k. Which expression is equivalent to "
            "\\(k(h(x))\\)?"),
      choices=["\\(9x^{2}+12x-6\\)", "\\(3x^{2}-15x+2\\)", "\\(9x^{2}-3x-6\\)",
               "\\(9x^{2}-3x+14\\)"], correct="C",
      check="(3x+2)^2 - 5(3x+2) = 9x^2 + 12x + 4 - 15x - 10 = 9x^2 - 3x - 6."),

 dict(n="H2H-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A forester writes the difference between two growth allowances as "
            "\\(\\frac{1}{x-3}-\\frac{2}{x+1}\\), where \\(x>3\\). Which expression is equivalent "
            "to that difference?"),
      choices=["\\(\\frac{x+7}{x^{2}-2x-3}\\)", "\\(\\frac{-1}{x^{2}-2x-3}\\)",
               "\\(\\frac{3x-5}{x^{2}-2x-3}\\)", "\\(\\frac{7-x}{x^{2}-2x-3}\\)"], correct="D",
      check="Over the common denominator (x-3)(x+1), the numerator is (x+1) - 2(x-3) = 7 - x."),

 dict(n="H2H-09", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A contour mapper finds that the curve \\(y=x^{2}-2x\\) and the straight line "
            "\\(x+y=8\\) meet at two points, where x and y are measured in kilometres. What is "
            "the sum of the y-coordinates of those two points?"),
      choices=["1", "8", "15", "16"], correct="C",
      check="x^2 - x - 8 = 0 gives x-coordinates summing to 1, and the y-coordinates sum to 16 - 1 = 15."),

 dict(n="H2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A levelling correction x satisfies \\(\\sqrt{3x+16}=x+2\\). What is the value of x?"),
      choices=["3", "4", "12", "16"], correct="A",
      check="Squaring gives x^2 + x - 12 = 0, whose roots are 3 and -4; only x = 3 keeps x+2 non-negative."),

 dict(n="H2H-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The number of viable seeds left in a seed drill's hopper t weeks after filling is "
            "modelled by \\(V(t)=u\\left(\\frac{3}{4}\\right)^{\\frac{t}{6}}\\), where u is a "
            "positive constant. What is the value of \\(\\frac{V(18)}{V(6)}\\)?"),
      choices=["\\(\\frac{9}{16}\\)", "\\(\\frac{3}{4}\\)", "\\(\\frac{27}{64}\\)",
               "\\(\\frac{4}{3}\\)"], correct="A",
      check="The ratio is (3/4)^3 divided by (3/4)^1, which is (3/4)^2 = 9/16, whatever u is."),

 dict(n="H2H-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A reservoir engineer rewrites \\(3x^{2}+24x+61\\) in the form \\(3(x+r)^{2}+w\\), "
            "where r and w are constants. What is the value of \\(r+w\\)?"),
      choices=["13", "17", "21", "25"], correct="B",
      check="3(x+4)^2 + 13 expands to 3x^2 + 24x + 61, so r = 4, w = 13 and r + w = 17."),

 dict(n="H2H-13", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A dairy weighed a random sample of 60 of the 900 cheeses maturing in one store and "
            "found a mean maturing loss of 118 grams, with an associated margin of error of 6 grams "
            "at the 95% confidence level. Which conclusion is most appropriate?"),
      choices=["Every cheese in the store has a maturing loss of between 112 grams and 124 grams.",
               "The mean maturing loss for all 900 cheeses in the store is certainly 118 grams.",
               "Nothing about the store as a whole can be concluded, because only 60 cheeses were "
               "weighed.",
               "It is plausible that the mean maturing loss for all 900 cheeses in the store is "
               "between 112 grams and 124 grams."],
      correct="D",
      check="A margin of error gives a plausible interval for the population mean, not a certainty or a rule for every cheese."),

 dict(n="H2H-14", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("A forest survey recorded the area felled at four coupes in one season and the mean "
            "volume of timber cut from each hectare of that coupe."
            + table(["Coupe", "Area felled (ha)", "Mean volume per hectare (cubic metres)"],
                    [["Ashfell", "12", "180"], ["Birkrigg", "8", "240"],
                     ["Crag Wood", "15", "160"], ["Dale Head", "5", "300"]])
            + "Taking the four coupes together, what was the mean volume of timber cut per hectare, "
              "in cubic metres?"),
      choices=["195", "199.5", "220", "245"], correct="B",
      check="Total volume 7,980 cubic metres over 40 hectares gives 199.5."),

 dict(n="H2H-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A survey plan is drawn to a scale of 1 to 2,500, so that a length on the ground is "
            "2,500 times the length that represents it on the plan. A reservoir drawn on the "
            "plan covers 48 square centimetres. What is the reservoir's actual area, in square "
            "metres?"),
      choices=["1,200", "12,000", "30,000", "300,000"], correct="C",
      check="Areas scale by 2,500 squared, so 48 sq cm becomes 300,000,000 sq cm, which is 30,000 sq m."),

 dict(n="H2H-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A creamery filled 12 vats one week, and the mean yield of the 12 vats was 65 "
            "kilograms. The 5 vats set with a new starter culture had a mean yield of 58 kilograms. "
            "What was the mean yield, in kilograms, of the other 7 vats?"),
      choices=["68", "69", "70", "72"], correct="C",
      check="12(65) - 5(58) = 780 - 290 = 490, and 490/7 = 70."),

 dict(n="H2H-17", domain="GT", skill="GT-TR", type="MC",
      stem=("A traverse leg forms a right triangle \\(ABC\\) with the right angle at C, and the "
            "field book records \\(\\cos A=\\frac{9}{41}\\). What is the value of \\(\\sin B\\)?"),
      choices=["\\(\\frac{9}{40}\\)", "\\(\\frac{40}{41}\\)", "\\(\\frac{9}{41}\\)",
               "\\(\\frac{41}{9}\\)"], correct="C",
      check="Angles A and B are complementary in a right triangle, so sin B = cos A = 9/41."),

 dict(n="H2H-18", domain="GT", skill="GT-AV", type="MC",
      stem=("A cheese vat is a cylinder whose height is equal to the diameter of its base, and the "
            "vat holds \\(2{,}000\\pi\\) cubic centimetres when full. What is the height of the "
            "vat, in centimetres?"),
      choices=["10", "20", "40", "100"], correct="B",
      check="With height 2r, the volume is 2 pi r^3 = 2,000 pi, so r = 10 and the height is 20."),

 dict(n="H2H-19", domain="GT", skill="GT-LA", type="MC",
      stem=("A hedge layer plans a triangular field corner \\(ABC\\). A new hedge \\(DE\\) is set "
            "with D on \\(AB\\) and E on \\(AC\\), parallel to \\(BC\\). The plan gives "
            "\\(AD=6\\) metres, \\(DB=9\\) metres and \\(DE=8\\) metres. What is the length of "
            "\\(BC\\), in metres?"),
      choices=["12", "14", "20", "24"], correct="C",
      check="Triangles ADE and ABC are similar with ratio 6 to 15, so BC = 8(15/6) = 20."),

 dict(n="H2H-20", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A haulage cable is spliced from two lengths whose ratio is 5 to 3. The longer length is "
            "96 metres longer than the shorter. How many metres long is the spliced cable?"),
      answers=["384"],
      check="5u - 3u = 2u = 96 gives u = 48, and the whole cable is 8u = 384."),

 dict(n="H2H-21", domain="PSDA", skill="PSDA-RP", type="FR",
      stem=("A timber yard's log store held 4,500 tonnes at the start of the month. Deliveries "
            "during the month raised the amount held by 20%, and sales then reduced the raised "
            "amount by 35%. How many tonnes does the store hold at the end of the month?"),
      answers=["3510"],
      check="4,500(1.20) = 5,400, and 5,400(0.65) = 3,510."),

 dict(n="H2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A drystone wall 1.4 metres high and 0.8 metres thick is to be built along 250 metres "
            "of a boundary. Stone is delivered in loads of 14 cubic metres. How many loads of stone "
            "does the wall take?"),
      answers=["20"],
      check="250(1.4)(0.8) = 280 cubic metres, and 280/14 = 20 loads."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
