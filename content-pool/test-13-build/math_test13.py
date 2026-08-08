#!/usr/bin/env python3
"""
Original Math content for Test 13 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium. A constant, a rate or an unknown price has to be
                recovered before the question can be answered; two or three
                steps throughout. Deliberately harder than Module 2 (Easy) and
                below Module 2 (Hard).
  MODULE_2_EASY genuinely one-step — the lower branch of the adaptive split.
  MODULE_2_HARD hard. A system conditioned on a constant, structural answers, a
                composed function, a parameter recovered before a minimum can be
                read off, and geometry that needs two relationships at once.

Every setting is concrete and deliberately unlike anything already banked in
production (bell founding, canal reservoirs, drilling logs, madder dye, osprey
counts, seedling nurseries, salt cones, cable spools). House style follows
Test 1/2 — see CLAUDE.md. All LaTeX is typed by hand; no bulk conversion step
was used anywhere in this file.
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
 dict(n="F1-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A bell foundry casts handbells and tower bells from bronze. Casting 3 handbells and "
            "2 tower bells uses 96 kilograms of bronze, and casting 5 handbells and 4 tower bells "
            "uses 178 kilograms of bronze. How many kilograms of bronze does one tower bell use?"),
      choices=["14", "21", "24", "27"], correct="D",
      check="3h+2t=96 and 5h+4t=178 give h = 14 and t = 27."),

 dict(n="F1-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A chapel choir of 96 singers is split into three sections. The alto section has 6 more "
            "singers than the soprano section, and the tenor section has half as many singers as "
            "the soprano section. How many singers are in the tenor section?"),
      choices=["18", "24", "36", "42"], correct="A",
      check="s + (s+6) + s/2 = 96 gives s = 36, so the tenor section has 18."),

 dict(n="F1-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("During a drought the water level in a canal reservoir falls at a constant rate. On day "
            "5 of the drought the level was 412 centimetres, and on day 17 it was 328 centimetres. "
            "On which day of the drought does this model give a level of 300 centimetres?"),
      choices=["19", "21", "24", "28"], correct="B",
      check="Rate = -84/12 = -7 cm per day; 412 - 7(t-5) = 300 gives t = 21."),

 dict(n="F1-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A bicycle courier prices a delivery by the rule \\(C=45+rm\\), where m is the number "
            "of miles the delivery covers, r is a constant charge per mile in dollars, and C is the "
            "price in dollars. A delivery covering 24 miles was priced at $141. What is the price "
            "of a delivery covering 38 miles?"),
      choices=["$173", "$189", "$197", "$211"], correct="C",
      check="45 + 24r = 141 gives r = 4, so C = 45 + 38(4) = 197."),

 dict(n="F1-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A drilling rig bores a well at a constant rate, and the table gives the depth of the "
            "bore recorded at four times during one shift."
            + table(["Hours since drilling began", "Depth (metres)"],
                    [["2", "34"], ["5", "61"], ["9", "97"], ["12", "124"]])
            + "At this rate, what is the depth of the bore 20 hours after drilling began?"),
      choices=["169", "178", "187", "196"], correct="D",
      check="Rate = 90/10 = 9 m per hour, so depth = 34 + 9(18) = 196."),

 dict(n="F1-06", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A paintings conservator has 300 minutes of studio time left this week. Each canvas she "
            "cleans takes 26 minutes and each frame she repairs takes 14 minutes, and she must "
            "complete 8 frame repairs. What is the greatest number of canvases she can clean in the "
            "time that is left?"),
      choices=["6", "7", "8", "9"], correct="B",
      check="26c + 14(8) <= 300 gives c <= 7.2, so 7 canvases."),

 dict(n="F1-07", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A postal van drives for 3 hours on country roads at a constant speed and then for 2 "
            "hours on a motorway at a constant speed 6 kilometres per hour greater. The van covers "
            "152 kilometres in all. What was its speed, in kilometres per hour, on the country "
            "roads?"),
      choices=["24", "26", "28", "34"], correct="C",
      check="3v + 2(v+6) = 152 gives 5v = 140 and v = 28."),

 dict(n="F1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A mosaic workshop writes the number of tiles needed for a panel as "
            "\\(\\frac{6x^{2}+11x-35}{3x-5}\\), where x is the number of rows in the panel and "
            "\\(x>3\\). Which expression is equivalent to that number of tiles?"),
      choices=["\\(2x-7\\)", "\\(2x+7\\)", "\\(3x+7\\)", "\\(6x+7\\)"], correct="B",
      check="6x^2+11x-35 factors as (3x-5)(2x+7), so the quotient is 2x+7."),

 dict(n="F1-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A kelp farm models the yield of one raft, in kilograms, as "
            "\\(Y(n)=-8n^{2}+448n-500\\), where n is the number of seeded lines on the raft. How "
            "many seeded lines give the greatest yield under this model?"),
      choices=["12", "16", "24", "28"], correct="D",
      check="The vertex is at n = 448/16 = 28."),

 dict(n="F1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A hospital tracks a radioactive tracer so that the activity remaining after d days is "
            "\\(A(d)=6{,}250\\left(\\frac{1}{5}\\right)^{d}\\) becquerels. After how many days does "
            "this model give an activity of 50 becquerels?"),
      choices=["3", "4", "5", "6"], correct="A",
      check="6,250/50 = 125 = 5^3, so d = 3."),

 dict(n="F1-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A cartographer draws a parabolic depth contour \\(y=x^{2}+4x-12\\) across a straight "
            "survey line \\(y=3x+8\\), where x and y are measured in kilometres. The contour meets "
            "the line at two points. What is the product of the x-coordinates of those two points?"),
      choices=["-20", "-5", "-1", "20"], correct="A",
      check="x^2+4x-12 = 3x+8 gives x^2+x-20 = 0, whose roots 4 and -5 have product -20."),

 dict(n="F1-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A tannery converts the raw mass g of a hide into a finishing index w using "
            "\\(w=\\frac{5g-14}{3}\\). Which expression gives g in terms of w?"),
      choices=["\\(\\frac{3w+14}{5}\\)", "\\(\\frac{3w-14}{5}\\)", "\\(\\frac{5w+14}{3}\\)",
               "\\(3w+14\\)"], correct="A",
      check="3w = 5g - 14, so g = (3w+14)/5."),

 dict(n="F1-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The power a wind turbine generates is modelled by \\(P(v)=cv^{3}\\), where v is the "
            "wind speed in metres per second, c is a constant and P is the power in kilowatts. At a "
            "wind speed of 6 metres per second the turbine generates 108 kilowatts. How many "
            "kilowatts does it generate at a wind speed of 10 metres per second?"),
      choices=["180", "300", "500", "540"], correct="C",
      check="c(216) = 108 gives c = 0.5, so P = 0.5(1,000) = 500."),

 dict(n="F1-14", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A mat of invasive water hyacinth covers 2,000 square metres of a lagoon, and the area "
            "it covers grows by 15% each week. To the nearest square metre, how many square metres "
            "does the mat cover after 5 weeks?"),
      choices=["3,530", "4,023", "4,600", "5,000"], correct="B",
      check="2,000(1.15)^5 = 4,022.71, which rounds to 4,023."),

 dict(n="F1-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A dyer uses 7 grams of madder root for every 4 metres of cloth, and madder root costs "
            "$3 per gram. What is the cost of the madder root needed to dye 96 metres of cloth?"),
      choices=["$336", "$420", "$504", "$672"], correct="C",
      check="96/4 = 24 lots of 7 g is 168 g, and 168($3) = $504."),

 dict(n="F1-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A ferry operator cut the fare on one crossing by 20% in the spring and then raised the "
            "reduced fare by 35% in the autumn. A passenger travelling after both changes paid $54. "
            "What was the fare, in dollars, before either change?"),
      choices=["$40", "$45", "$48", "$50"], correct="D",
      check="(0.80)(1.35) = 1.08 and 54/1.08 = 50."),

 dict(n="F1-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of breeding pairs of ospreys counted at four lochs in 2015 "
            "and again in 2022."
            + table(["Loch", "Pairs in 2015", "Pairs in 2022"],
                    [["Dorrin", "40", "52"], ["Enard", "55", "70"],
                     ["Fionn", "35", "48"], ["Gruinard", "70", "80"]])
            + "By what percent did the total number of breeding pairs counted increase from 2015 "
              "to 2022?"),
      choices=["20%", "25%", "50%", "125%"], correct="B",
      check="Totals are 200 and 250, and 50/200 = 25%."),

 dict(n="F1-18", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("The 14 members of a rowing club have a mean mass of 78 kilograms. The 6 members of the "
            "lightweight squad within that club have a mean mass of 62 kilograms. What is the mean "
            "mass, in kilograms, of the other 8 members of the club?"),
      answers=["90"],
      check="14(78) - 6(62) = 1,092 - 372 = 720, and 720/8 = 90."),

 dict(n="F1-19", domain="GT", skill="GT-LA", type="MC",
      stem=("In a triangular roof truss, the largest angle measures 3 times the smallest angle, and "
            "the remaining angle measures 20&deg; more than the smallest angle. What is the "
            "measure, in degrees, of the largest angle?"),
      choices=["32", "52", "64", "96"], correct="D",
      check="a + 3a + (a+20) = 180 gives a = 32, so the largest angle is 96."),

 dict(n="F1-20", domain="GT", skill="GT-TR", type="MC",
      stem=("A conveyor belt carries gravel in a straight line from ground level to the top of a "
            "silo 15 metres high, and the belt makes an angle of 30&deg; with the horizontal. "
            "Gravel travels along the belt at 2 metres per second. How many seconds does a piece "
            "of gravel take to travel the whole length of the belt?"),
      choices=["7.5", "15", "30", "60"],
      correct="B",
      check="The belt is 15/sin 30 = 30 m long, and 30/2 = 15 seconds."),

 dict(n="F1-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A solid scale model of a granite monument is built at one-quarter of the monument's "
            "linear dimensions. The finished monument contains 448 cubic feet of granite. How many "
            "cubic feet of granite does the model contain?"),
      answers=["7"],
      check="Volumes scale by 4^3 = 64, and 448/64 = 7."),

 dict(n="F1-22", domain="GT", skill="GT-LA", type="FR",
      stem=("A vertical pole 2.4 metres tall casts a shadow 1.8 metres long on level ground. At the "
            "same moment a nearby spire casts a shadow 31.5 metres long. How many metres tall is "
            "the spire?"),
      answers=["42"],
      check="The triangles are similar, so the spire is (2.4/1.8)(31.5) = 42 m tall."),
]


# ------------------------------------------------------------ Module 2 Easy
MODULE_2_EASY = [
 dict(n="F2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A bindery sews 8 signatures into every book it makes and used 152 signatures "
            "altogether. How many books did the bindery make?"),
      choices=["17", "18", "19", "21"], correct="C",
      check="152/8 = 19."),

 dict(n="F2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A hiker's pack weighs 23 kilograms. She leaves 5 kilograms of supplies at a mountain "
            "hut and divides the rest of the load equally among 3 dry bags. How many kilograms does "
            "each dry bag hold?"),
      choices=["5", "6", "7.5", "9"], correct="B",
      check="(23-5)/3 = 6."),

 dict(n="F2E-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A kayak hire charges an $18 launch fee plus $13 for each hour on the water. What is "
            "the total charge, in dollars, for 5 hours on the water?"),
      choices=["65", "78", "83", "95"], correct="C",
      check="18 + 13(5) = 83."),

 dict(n="F2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A community compost bin holds 240 kilograms of material at the start of the season and "
            "loses 15 kilograms of it each week. Which expression gives the mass of material, in "
            "kilograms, in the bin after w weeks?"),
      choices=["\\(240-15w\\)", "\\(240w-15\\)", "\\(15w-240\\)", "\\(225w\\)"], correct="A",
      check="Start at 240 and subtract 15 for each week."),

 dict(n="F2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A service lift may carry no more than 8 passengers at a time. Which inequality gives "
            "all the possible numbers p of passengers the lift may carry at one time?"),
      choices=["\\(p<8\\)", "\\(p\\ge 8\\)", "\\(p\\le 8\\)", "\\(p>8\\)"], correct="C",
      check="No more than 8 means 8 or fewer."),

 dict(n="F2E-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A tram ticket costs $4. A traveller pays with a $50 note and receives $14 in change. "
            "How many tram tickets did the traveller buy?"),
      choices=["8", "9", "11", "12"], correct="B",
      check="(50-14)/4 = 9."),

 dict(n="F2E-07", domain="ALG", skill="ALG-LF", type="MC",
      stem=("On a long drive the function \\(D(t)=560-70t\\) gives the distance remaining, in "
            "kilometres, t hours after the drive begins. What is the meaning of 70 in this model?"),
      choices=["The total distance, in kilometres, of the drive.",
               "The number of hours the whole drive takes.",
               "The distance remaining, in kilometres, one hour after the drive begins.",
               "The number of kilometres by which the remaining distance decreases each hour."],
      correct="D",
      check="70 multiplies t, so it is the drop in the remaining distance per hour."),

 dict(n="F2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A signwriter uses \\(5m-8\\) grams of gold leaf on the letters of a sign and "
            "\\(3m+14\\) grams on the border, where m is the number of letters. Which expression "
            "gives the total mass of gold leaf, in grams, used on the sign?"),
      choices=["\\(8m+6\\)", "\\(8m-6\\)", "\\(2m+6\\)", "\\(8m+22\\)"], correct="A",
      check="(5m-8) + (3m+14) = 8m + 6."),

 dict(n="F2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A tiler lays \\(3(2x+5)\\) tiles along one wall of a bathroom. Which expression is "
            "equivalent to that number of tiles?"),
      choices=["\\(6x+5\\)", "\\(2x+15\\)", "\\(5x+6\\)", "\\(6x+15\\)"], correct="D",
      check="Distributing gives 6x + 15."),

 dict(n="F2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A tiling pattern grows so that the nth figure in the pattern uses \\(3n^{2}\\) tiles. "
            "How many tiles does the 4th figure use?"),
      choices=["24", "36", "48", "144"], correct="C",
      check="3(4^2) = 3(16) = 48."),

 dict(n="F2E-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A caterer's rule says that a square baking pan whose sides are x centimetres long "
            "serves \\(\\frac{x^{2}}{50}\\) people. One of the caterer's pans serves 8 people. How "
            "many centimetres long are the sides of that pan?"),
      choices=["16", "20", "25", "40"], correct="B",
      check="x^2/50 = 8 gives x^2 = 400 and x = 20."),

 dict(n="F2E-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A photographer's exposure index is given by \\(g(x)=\\frac{x+9}{x-1}\\), where x is "
            "the meter reading and \\(x>1\\). What is the exposure index when the meter reading is "
            "5?"),
      choices=["2.5", "3.5", "4", "7"], correct="B",
      check="(5+9)/(5-1) = 14/4 = 3.5."),

 dict(n="F2E-13", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A lens grinder enlarges every measurement on a drawing by the scale factor "
            "\\(16^{\\frac{3}{4}}\\). What is the value of that scale factor?"),
      choices=["8", "12", "48", "64"], correct="A",
      check="16^(3/4) is the cube of the fourth root of 16, which is 2^3 = 8."),

 dict(n="F2E-14", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A lily pond is stocked so that the number of lily pads h hours after stocking is "
            "\\(P(h)=3\\cdot 4^{h}\\). How many lily pads are there 3 hours after stocking?"),
      choices=["36", "48", "144", "192"], correct="D",
      check="3(4^3) = 3(64) = 192."),

 dict(n="F2E-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A decorator mixes paint using 3 parts white to 5 parts blue by volume. One batch uses "
            "45 litres of white paint. How many litres of blue paint does that batch use?"),
      choices=["27", "60", "75", "120"], correct="C",
      check="(5/3)(45) = 75."),

 dict(n="F2E-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("The number of passengers using a rural bus route fell from 250 a day to 200 a day. By "
            "what percent did the number of passengers fall?"),
      choices=["12.5%", "20%", "25%", "50%"], correct="B",
      check="50/250 = 0.20, which is 20%."),

 dict(n="F2E-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("A village bakery kept a record of its output over four days, given in the table."
            + table(["Day", "Loaves baked"],
                    [["Monday", "84"], ["Tuesday", "96"], ["Wednesday", "78"], ["Thursday", "102"]])
            + "Over these four days combined, how many loaves did the bakery bake?"),
      choices=["336", "348", "354", "360"], correct="D",
      check="84 + 96 + 78 + 102 = 360."),

 dict(n="F2E-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("On five mornings a birdwatcher counted 9, 4, 2, 7 and 6 herons on an estuary. What is "
            "the median of the five counts?"),
      choices=["4", "5.6", "6", "7"], correct="C",
      check="In order the counts are 2, 4, 6, 7, 9, so the median is 6."),

 dict(n="F2E-19", domain="GT", skill="GT-LA", type="MC",
      stem=("A carpenter cuts an isosceles bracket in the shape of a triangle in which two of the "
            "angles each measure 35&deg;. What is the measure, in degrees, of the third angle?"),
      choices=["55", "110", "115", "145"], correct="B",
      check="180 - 35 - 35 = 110."),

 dict(n="F2E-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A packing crate is a rectangular box measuring 6 feet by 4 feet by 3 feet. What is the "
            "volume of the crate, in cubic feet?"),
      answers=["72"],
      check="6(4)(3) = 72."),

 dict(n="F2E-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A square ceramic tile has an area of 169 square centimetres. What is the perimeter, in "
            "centimetres, of the tile?"),
      answers=["52"],
      check="The side is sqrt(169) = 13, so the perimeter is 4(13) = 52."),

 dict(n="F2E-22", domain="GT", skill="GT-TR", type="FR",
      stem=("A wheelchair ramp rises 5 metres while covering a horizontal distance of 12 metres. "
            "How many metres long is the sloping surface of the ramp?"),
      answers=["13"],
      check="sqrt(5^2 + 12^2) = sqrt(169) = 13."),
]


# ------------------------------------------------------------ Module 2 Hard
MODULE_2_HARD = [
 dict(n="F2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A metallurgist writes two blending constraints as \\(6x-4y=10\\) and "
            "\\(9x+cy=15\\), where x and y are the masses of two alloys in kilograms and c is a "
            "constant. Every pair \\((x,y)\\) that satisfies the first constraint also satisfies "
            "the second. What is the value of c?"),
      choices=["-9", "-6", "4", "6"], correct="B",
      check="Multiplying the first equation by 3/2 gives 9x - 6y = 15, so c = -6."),

 dict(n="F2H-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A barometric altimeter reports an offset \\(f(x)\\) for a raw pressure reading x, and "
            "f is a linear function. The instrument's log records \\(f(-4)=17\\) and "
            "\\(f(6)=-3\\). For what value of x does \\(f(x)=5\\)?"),
      choices=["-2", "1", "2", "7"], correct="C",
      check="Slope -20/10 = -2 and f(x) = -2x + 9, so f(x) = 5 at x = 2."),

 dict(n="F2H-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A delivery van carries parcels of two kinds. Each parcel of the first kind has a mass "
            "of 12 kilograms and each parcel of the second kind has a mass of 18 kilograms, and the "
            "van may carry a total parcel mass of at most 960 kilograms. The van must carry at "
            "least 30 parcels of the first kind. What is the greatest number of parcels of the "
            "second kind the van can carry?"),
      choices=["26", "30", "32", "33"], correct="D",
      check="12(30) + 18b <= 960 gives b <= 33.3, so 33 parcels."),

 dict(n="F2H-04", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A framer cuts a rectangular mounting card whose length is 3 centimetres greater than "
            "its width, and the card has an area of 154 square centimetres. What is the perimeter, "
            "in centimetres, of the card?"),
      choices=["44", "50", "56", "62"], correct="B",
      check="w(w+3) = 154 gives w = 11 and length 14, so the perimeter is 2(25) = 50."),

 dict(n="F2H-05", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A kiln controller turns a dial setting x into a firing temperature with "
            "\\(h(x)=5x-1\\), and the energy the kiln then draws at a firing temperature T is "
            "\\(f(T)=T^{2}+3\\). Which expression gives the energy the kiln draws in terms of the "
            "dial setting x?"),
      choices=["\\(25x^{2}-10x+4\\)", "\\(25x^{2}+3\\)", "\\(25x^{2}-10x+2\\)",
               "\\(5x^{2}+2\\)"], correct="A",
      check="(5x-1)^2 + 3 = 25x^2 - 10x + 1 + 3 = 25x^2 - 10x + 4."),

 dict(n="F2H-06", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("The clearance between a parabolic arch and the roadway beneath it, in feet, is given "
            "by \\(c(x)=3x^{2}+24x+50\\), where x is the horizontal distance in feet from a fixed "
            "marker. Which equivalent form of the expression displays the minimum clearance as a "
            "constant or coefficient?"),
      choices=["\\(3(x+8)^{2}+2\\)", "\\((3x+12)^{2}+2\\)", "\\(3(x+4)^{2}-2\\)",
               "\\(3(x+4)^{2}+2\\)"], correct="D",
      check="3(x+4)^2 + 2 expands to 3x^2 + 24x + 50, and the minimum clearance is 2."),

 dict(n="F2H-07", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A sheet of tinplate measuring 20 centimetres by 16 centimetres is made into an open "
            "tray by cutting a square of side x centimetres from each corner and folding the four "
            "flaps upward. The base of the finished tray has an area of 192 square centimetres. "
            "What is the value of x?"),
      choices=["2", "3", "4", "8"], correct="A",
      check="(20-2x)(16-2x) = 192 gives x^2 - 18x + 32 = 0, whose roots are 2 and 16; only 2 fits."),

 dict(n="F2H-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("The ratio of two cross-sectional areas in a ventilation duct is written as "
            "\\(\\frac{x^{2}-9}{x^{2}+7x+12}\\), where \\(x>3\\). Which expression is equivalent "
            "to that ratio?"),
      choices=["\\(\\frac{x+3}{x+4}\\)", "\\(\\frac{x-3}{x-4}\\)", "\\(\\frac{x-3}{x+4}\\)",
               "\\(\\frac{x-9}{7x+12}\\)"], correct="C",
      check="The numerator is (x-3)(x+3) and the denominator is (x+3)(x+4), so (x+3) cancels."),

 dict(n="F2H-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The floor of a dry valley is modelled by \\(y=k(x+2)(x-6)\\), where k is a constant "
            "and x and y are measured in hundreds of metres. The model passes through the point "
            "\\((0,-36)\\). What is the least value of y the model takes?"),
      choices=["-48", "-36", "-24", "12"], correct="A",
      check="k(2)(-6) = -36 gives k = 3; the vertex is at x = 2, where y = 3(4)(-4) = -48."),

 dict(n="F2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("While calibrating a pressure gauge a technician has to solve the equation "
            "\\(\\sqrt{2x+11}=x+4\\). What is the only value of x that satisfies this equation?"),
      choices=["-5", "-4", "-1", "5"], correct="C",
      check="Squaring gives x^2+6x+5 = 0 with roots -1 and -5; x = -5 makes the right side "
            "negative, so only x = -1 works."),

 dict(n="F2H-11", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A foundry melts an alloy that is 40% copper together with an alloy that is 70% copper "
            "to obtain 90 kilograms of an alloy that is 60% copper. How many kilograms of the 70% "
            "alloy does the foundry use?"),
      choices=["30", "45", "54", "60"], correct="D",
      check="0.40(90-y) + 0.70y = 54 gives 0.30y = 18 and y = 60."),

 dict(n="F2H-12", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A university selected 250 of its 6,000 first-year students at random and then randomly "
            "assigned each selected student to one of two study-skills programmes. Students who "
            "followed programme X went on to score significantly higher on a common end-of-term "
            "assessment than students who followed programme Y. Which of the following is the most "
            "appropriate conclusion?"),
      choices=["No conclusion about cause can be drawn, because the students were not assigned at "
               "random.",
               "Programme X will raise the assessment score of every first-year student at the "
               "university.",
               "First-year students at any university will score higher on the assessment if they "
               "follow programme X.",
               "Programme X is likely to cause higher assessment scores for first-year students at "
               "this university."],
      correct="D",
      check="Random selection plus random assignment supports a causal claim, limited to the "
            "population sampled."),

 dict(n="F2H-13", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The table gives the results of a germination trial on seedlings raised at two "
            "nurseries."
            + table(["Nursery", "Germinated", "Did not germinate"],
                    [["Alder Bank", "90", "30"], ["Bythorn", "120", "60"]])
            + "One of the seedlings that germinated is selected at random. What is the probability "
              "that the selected seedling was raised at Alder Bank?"),
      choices=["\\(\\frac{3}{10}\\)", "\\(\\frac{3}{7}\\)", "\\(\\frac{7}{10}\\)",
               "\\(\\frac{3}{4}\\)"], correct="B",
      check="210 seedlings germinated, 90 of them at Alder Bank, and 90/210 = 3/7."),

 dict(n="F2H-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A label press prints 45 sheets each minute, each sheet yields 16 labels, and finished "
            "labels are packed 500 to a box. How many boxes can be filled completely from the "
            "labels the press produces in 4 hours of continuous printing?"),
      choices=["172", "288", "345", "346"], correct="C",
      check="45(240) = 10,800 sheets give 172,800 labels, and 172,800/500 = 345.6."),

 dict(n="F2H-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives, for each of four workshops at a pottery, the number of bowls thrown "
            "in one week and the mean mass of one bowl."
            + table(["Workshop", "Bowls thrown", "Mean mass of one bowl (kg)"],
                    [["Ash", "40", "2.5"], ["Birch", "60", "4.0"],
                     ["Cedar", "50", "3.2"], ["Damson", "50", "5.0"]])
            + "What is the mean mass, in kilograms, of one bowl across all four workshops?"),
      choices=["3.55", "3.68", "3.75", "3.90"], correct="C",
      check="Total mass 750 kg over 200 bowls gives 3.75 kg."),

 dict(n="F2H-16", domain="GT", skill="GT-LA", type="MC",
      stem=("A gable bracket has the shape of triangle \\(RST\\), in which the side \\(RS\\) is "
            "the same length as the side \\(RT\\). When the side \\(ST\\) is extended beyond T, "
            "the angle it makes with the side \\(TR\\) measures 118&deg;. What is the measure, in "
            "degrees, of the angle at R?"),
      choices=["44", "56", "62", "68"], correct="B",
      check="The interior angle at T is 62, so the angle at S is 62 and R is 180 - 124 = 56."),

 dict(n="F2H-17", domain="GT", skill="GT-AV", type="MC",
      stem=("A grain hopper is a cylinder of radius 3 metres and height 5 metres with a cone of the "
            "same radius and height 4 metres joined to its base. What is the total volume of the "
            "hopper, in cubic metres?"),
      choices=["\\(51\\pi\\)", "\\(57\\pi\\)", "\\(63\\pi\\)", "\\(69\\pi\\)"], correct="B",
      check="The cylinder is 45 pi and the cone is 12 pi, so the total is 57 pi."),

 dict(n="F2H-18", domain="GT", skill="GT-TR", type="MC",
      stem=("A drawing office sets out a right triangle \\(JKL\\) in which the right angle is at L, "
            "so the angles at J and at K have measures that add to 90&deg;. The office records "
            "\\(\\tan J=\\frac{3}{4}\\). What is the value of \\(\\cos K\\)?"),
      choices=["\\(\\frac{3}{4}\\)", "\\(\\frac{4}{5}\\)", "\\(\\frac{3}{5}\\)",
               "\\(\\frac{5}{3}\\)"], correct="C",
      check="Legs 3 and 4 give a hypotenuse of 5, so sin J = 3/5, and cos K equals sin J."),

 dict(n="F2H-19", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A caterer packs portions into trays that hold 8 portions each and boxes that hold 5 "
            "portions each. She must pack at least 60 portions and may use at most 9 containers in "
            "all. If she uses exactly 4 boxes, how many trays must she use?"),
      choices=["4", "5", "6", "7"], correct="B",
      check="4 boxes hold 20, so 8t >= 40 gives t >= 5, while t + 4 <= 9 gives t <= 5."),

 dict(n="F2H-20", domain="ALG", skill="ALG-LF", type="FR",
      stem=("The mass of a spool of cable is a linear function of the length of cable wound on it. "
            "A spool holding 40 metres of cable has a mass of 27 kilograms, and a spool holding 100 "
            "metres of cable has a mass of 51 kilograms. What is the mass, in kilograms, of the "
            "empty spool?"),
      answers=["11"],
      check="Slope 24/60 = 0.4 kg per metre, so the empty spool is 27 - 16 = 11 kg."),

 dict(n="F2H-21", domain="ALG", skill="ALG-LE", type="FR",
      stem=("In a chemistry stockroom, 2 crates and 5 drums together weigh 197 kilograms, and 4 "
            "crates and 3 drums together weigh 219 kilograms. What is the combined weight, in "
            "kilograms, of one crate and one drum?"),
      answers=["61"],
      check="The system gives a drum 25 kg and a crate 36 kg, so together 61 kg."),

 dict(n="F2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A conical pile of road salt has a radius of 9 metres and a height of 4 metres. The "
            "salt is reshaped, with none lost, into a cylinder of radius 6 metres. What is the "
            "height, in metres, of the cylinder?"),
      answers=["3"],
      check="The cone holds 108 pi cubic metres, and 36 pi h = 108 pi gives h = 3."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
