#!/usr/bin/env python3
"""
Original Math content for Test 11 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium. A constant or a rate has to be recovered before
                the question can be answered; two or three steps throughout.
                Deliberately harder than Module 2 (Easy) and below Module 2
                (Hard).
  MODULE_2_EASY genuinely one-step — the lower branch of the adaptive split.
  MODULE_2_HARD hard. Parameters instead of numbers, structural answers, a
                composed function, systems conditioned on a constant, and
                geometry that needs two relationships at once.

Every setting is concrete and deliberately unlike anything already banked in
production (bookbinding, glacier survey, cable barges, tern colonies, dye vats,
botanical gardens). House style follows Test 1/2 — see CLAUDE.md. All LaTeX is
typed by hand; no bulk conversion step was used anywhere in this file.
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
 dict(n="D1-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A puppet theatre sold 3 times as many child tickets as adult tickets one evening. "
            "A child ticket costs $7 and an adult ticket costs $18, and the evening's ticket "
            "sales came to $1,404. How many adult tickets were sold?"),
      choices=["36", "39", "78", "108"], correct="A",
      check="7(3a) + 18a = 39a = 1,404, so a = 36."),

 dict(n="D1-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A bookbinder charges one fixed price per volume for stitching and a different fixed "
            "price per volume for gilding. Stitching 4 volumes and gilding 3 volumes costs $141, "
            "while stitching 6 volumes and gilding 5 volumes costs $223. How many dollars does it "
            "cost to gild one volume?"),
      choices=["18", "23", "27", "31"], correct="B",
      check="4s+3g=141 and 6s+5g=223 give g = 23 and s = 18."),

 dict(n="D1-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The terminus of a glacier retreats from a fixed marker post at a constant rate. In "
            "2010 the terminus was 3,150 metres from the post, and in 2018 it was 3,614 metres "
            "from the post. In which year does this model place the terminus 4,020 metres from "
            "the post?"),
      choices=["2019", "2023", "2025", "2031"], correct="C",
      check="Rate = 464/8 = 58 m per year; 870/58 = 15 years after 2010."),

 dict(n="D1-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A robotics club has $840 to spend. It must first buy one controller board that costs "
            "$215, and it will then spend the rest on motor kits that cost $58 each. What is the "
            "greatest number of motor kits the club can buy?"),
      choices=["6", "8", "9", "10"], correct="D",
      check="215 + 58k <= 840 gives k <= 10.7, so 10 kits."),

 dict(n="D1-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A luthier prices a custom mandolin by the rule \\(P=380+rh\\), where h is the number "
            "of hours of work the instrument takes, r is a constant hourly rate in dollars, and P "
            "is the price in dollars. A mandolin that took 26 hours was priced at $1,290. What is "
            "the price of a mandolin that takes 41 hours?"),
      choices=["$1,815", "$1,940", "$2,015", "$2,215"], correct="A",
      check="380 + 26r = 1,290 gives r = 35, so P = 380 + 41(35) = 1,815."),

 dict(n="D1-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A barge pays cable out over its stern at a constant rate. After 12 minutes of paying "
            "out, 348 metres of cable remain on the drum; after 30 minutes, 186 metres remain. How "
            "many metres of cable were on the drum before the barge began paying out?"),
      choices=["438", "456", "474", "492"], correct="B",
      check="Rate = 162/18 = 9 m per minute, so the drum began with 348 + 12(9) = 456 m."),

 dict(n="D1-07", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A rainwater tank holds 220 litres at the moment a hose is turned on, and the hose "
            "adds water at a constant rate. Nine minutes later the tank holds 355 litres. The tank "
            "spills over once it holds 1,000 litres. How many minutes after the hose is turned on "
            "does the tank spill over?"),
      choices=["45", "48", "52", "60"], correct="C",
      check="Rate = 135/9 = 15 litres per minute; 780/15 = 52 minutes."),

 dict(n="D1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A sound engineer writes the total delay of a signal chain, in milliseconds, as "
            "\\(\\frac{10x^{2}+x-21}{2x+3}\\), where x is the number of processing units in the "
            "chain and \\(x>2\\). Which expression is equivalent to that delay?"),
      choices=["\\(2x-7\\)", "\\(5x+7\\)", "\\(5x-21\\)", "\\(5x-7\\)"], correct="D",
      check="10x^2+x-21 factors as (2x+3)(5x-7), so the quotient is 5x-7."),

 dict(n="D1-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A vineyard models the extra profit, in dollars, from planting n additional rows of "
            "vines as \\(P(n)=-15n^{2}+540n-1{,}200\\). How many additional rows give the greatest "
            "extra profit under this model?"),
      choices=["18", "24", "36", "54"], correct="A",
      check="The vertex is at n = 540/30 = 18."),

 dict(n="D1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A film archive digitises its reels so that the number still undigitised after w weeks "
            "is \\(N(w)=8{,}748\\left(\\frac{1}{3}\\right)^{w}\\). After how many weeks does this "
            "model give 108 undigitised reels?"),
      choices=["3", "4", "6", "9"], correct="B",
      check="8,748/108 = 81 = 3^4, so w = 4."),

 dict(n="D1-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The flight path of a ski jumper is modelled by \\(y=x^{2}-3x-10\\) and the landing "
            "slope by \\(y=2x-4\\), where x and y are measured in metres. The two graphs meet at "
            "two points. What is the sum of the x-coordinates of those two points?"),
      choices=["-6", "1", "5", "11"], correct="C",
      check="x^2-3x-10 = 2x-4 gives x^2-5x-6 = 0, whose roots -1 and 6 sum to 5."),

 dict(n="D1-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A weather station converts a raw sensor count m into a scaled reading R using "
            "\\(R=\\frac{2m+9}{4}\\). Which expression gives m in terms of R?"),
      choices=["\\(\\frac{4R-9}{2}\\)", "\\(\\frac{4R+9}{2}\\)", "\\(\\frac{R-9}{2}\\)",
               "\\(4R-9\\)"], correct="A",
      check="4R = 2m + 9, so m = (4R-9)/2."),

 dict(n="D1-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("An acoustics designer models the reverberation time of a concert hall as "
            "\\(T(v)=\\frac{v^{2}}{800}+1.5\\) seconds, where v is the width of the hall in "
            "metres. A hall built to this design has a reverberation time of 3.5 seconds. What is "
            "its width, in metres?"),
      choices=["20", "25", "32", "40"], correct="D",
      check="v^2/800 = 2 gives v^2 = 1,600 and v = 40."),

 dict(n="D1-14", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A vaccine held in cold storage loses 12% of its potency every month, so 88% of the "
            "potency at the start of a month remains at the end of it. A vial begins with 4,000 "
            "potency units. To the nearest whole unit, how many potency units does the vial hold "
            "after 4 months?"),
      choices=["2,080", "2,399", "2,560", "3,080"], correct="B",
      check="4,000(0.88)^4 = 2,398.78, which rounds to 2,399."),

 dict(n="D1-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A hand press stamps 45 medallions from every 2 kilograms of pewter, and pewter costs "
            "$19 per kilogram. What is the cost of the pewter needed to stamp 1,080 medallions?"),
      choices=["$456", "$722", "$912", "$1,026"], correct="C",
      check="1,080/45 = 24 batches, so 48 kg of pewter at $19 costs $912."),

 dict(n="D1-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A gallery raised the price of a print by 25%, and three months later lowered the new "
            "price by 12%. A collector who bought the print after both changes paid $264. What was "
            "the price of the print before either change?"),
      choices=["$198", "$220", "$228", "$240"], correct="D",
      check="(1.25)(0.88) = 1.10 and 264/1.10 = 240."),

 dict(n="D1-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of nesting pairs of terns counted on each of four islets "
            "during one breeding season."
            + table(["Islet", "Nesting pairs"],
                    [["Ardle", "84"], ["Brisay", "126"], ["Corran", "147"], ["Dunnet", "63"]])
            + "What percent of all the nesting pairs counted were on Corran?"),
      choices=["15%", "20%", "30%", "35%"], correct="D",
      check="Total 420 pairs; 147/420 = 35%."),

 dict(n="D1-18", domain="GT", skill="GT-LA", type="MC",
      stem=("In a triangular sail, the second angle measures twice the first, and the third angle "
            "measures 24&deg; less than the sum of the other two. What is the measure, in degrees, "
            "of the largest of the three angles?"),
      choices=["68", "78", "84", "102"], correct="B",
      check="a + 2a + (3a-24) = 180 gives a = 34, so the angles are 34, 68 and 78."),

 dict(n="D1-19", domain="GT", skill="GT-TR", type="MC",
      stem=("A ranger in a fire tower spots a smoke plume on level ground at an angle of "
            "depression of 30&deg;. The ranger's window is 45 metres above the ground. How far, in "
            "metres, is the plume from the foot of the tower?"),
      choices=["\\(15\\sqrt{3}\\)", "\\(45\\sqrt{3}\\)", "\\(90\\)", "\\(90\\sqrt{3}\\)"],
      correct="B",
      check="tan 30 = 45/d gives d = 45 sqrt(3)."),

 dict(n="D1-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A stonemason saws a cube of granite whose edges are 30 centimetres long into smaller "
            "cubes whose edges are 6 centimetres long, wasting none of the stone. How many smaller "
            "cubes does the mason obtain?"),
      answers=["125"],
      check="(30/6)^3 = 5^3 = 125."),

 dict(n="D1-21", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("The mean mass of the 11 pumpkins entered in a growers' contest was 84 kilograms. When "
            "a twelfth pumpkin was entered, the mean mass of all 12 pumpkins rose to 86 kilograms. "
            "What was the mass, in kilograms, of the twelfth pumpkin?"),
      answers=["108"],
      check="12(86) - 11(84) = 1,032 - 924 = 108."),

 dict(n="D1-22", domain="GT", skill="GT-LA", type="FR",
      stem=("Two similar triangular gable ends have corresponding bases of 9 metres and 15 metres. "
            "The smaller gable end has an area of 27 square metres. What is the area, in square "
            "metres, of the larger gable end?"),
      answers=["75"],
      check="The area ratio is (15/9)^2 = 25/9, and 27(25/9) = 75."),
]


# ------------------------------------------------------------ Module 2 Easy
MODULE_2_EASY = [
 dict(n="D2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A caretaker reglazes every window in a hall, fitting 7 panes in each window and using "
            "126 panes altogether. How many windows are in the hall?"),
      choices=["9", "12", "14", "18"], correct="D",
      check="126/7 = 18."),

 dict(n="D2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A tailor cuts a 27-metre bolt of cloth by first trimming off a 9-metre remnant and "
            "then dividing what is left into 4 equal pieces. How many metres long is each of those "
            "4 pieces?"),
      choices=["4.5", "6", "9", "18"], correct="A",
      check="(27-9)/4 = 4.5."),

 dict(n="D2E-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A phone repair shop charges a $35 inspection fee plus $22 for each hour of labour. "
            "What is the total charge, in dollars, for a repair that needs 4 hours of labour?"),
      choices=["101", "113", "123", "145"], correct="C",
      check="35 + 22(4) = 123."),

 dict(n="D2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A hedgehog rescue centre begins the winter with 150 kilograms of feed and uses 18 "
            "kilograms of it each week. Which expression gives the mass of feed, in kilograms, "
            "remaining after w weeks?"),
      choices=["\\(150-18w\\)", "\\(150w-18\\)", "\\(18w-150\\)", "\\(168w\\)"], correct="A",
      check="Start at 150 and subtract 18 for each week."),

 dict(n="D2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("An after-school club runs only when at least 12 children are enrolled. Which "
            "inequality gives all the possible numbers c of enrolled children for which the club "
            "runs?"),
      choices=["\\(c<12\\)", "\\(c\\le 12\\)", "\\(c\\ge 12\\)", "\\(c>12\\)"], correct="C",
      check="At least 12 means 12 or more."),

 dict(n="D2E-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("Three friends split the $96 cost of a gift equally, and one of them also pays a $9 "
            "delivery charge. How many dollars does that friend pay altogether?"),
      choices=["32", "35", "38", "41"], correct="D",
      check="96/3 = 32, and 32 + 9 = 41."),

 dict(n="D2E-07", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A public fountain is drained at a constant rate, and \\(L(m)=900-45m\\) gives the "
            "number of litres of water in the fountain m minutes after draining begins. What is "
            "the meaning of 900 in this model?"),
      choices=["The number of litres of water in the fountain when draining begins.",
               "The number of litres of water drained from the fountain each minute.",
               "The number of minutes the fountain takes to empty completely.",
               "The number of litres of water left in the fountain after 45 minutes."],
      correct="A",
      check="At m = 0 the model gives 900 litres."),

 dict(n="D2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A landscaper spends \\(6b+9\\) minutes planting the beds and \\(4b-2\\) minutes "
            "planting the borders, where b is the number of beds. Which expression gives the total "
            "planting time, in minutes?"),
      choices=["\\(2b+11\\)", "\\(10b+7\\)", "\\(10b+11\\)", "\\(24b-18\\)"], correct="B",
      check="(6b+9) + (4b-2) = 10b + 7."),

 dict(n="D2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A quilt panel has an area of \\(x^{2}+7x\\) square centimetres. Which expression is "
            "equivalent to that area?"),
      choices=["\\(7x^{2}\\)", "\\(x^{2}(1+7)\\)", "\\((x+7)(x+1)\\)", "\\(x(x+7)\\)"],
      correct="D",
      check="x is a common factor, so the area is x(x+7)."),

 dict(n="D2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("Oranges are stacked so that the number of oranges in the nth layer of a stack is "
            "\\(n^{2}+2\\). How many oranges are in the 5th layer?"),
      choices=["12", "17", "27", "52"], correct="C",
      check="5^2 + 2 = 27."),

 dict(n="D2E-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A pebble dropped from a bridge falls \\(5t^{2}\\) metres in the first t seconds of "
            "its fall. How many seconds does the pebble take to fall 45 metres?"),
      choices=["3", "5", "9", "20"], correct="A",
      check="5t^2 = 45 gives t^2 = 9 and t = 3."),

 dict(n="D2E-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A sluice gate releases water so that the flow speed, in centimetres per second, t "
            "seconds after the gate opens is \\(u(t)=\\frac{120}{t+2}\\). What is the flow speed "
            "4 seconds after the gate opens?"),
      choices=["15", "20", "24", "60"], correct="B",
      check="120/(4+2) = 20."),

 dict(n="D2E-13", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A crystallographer records a count as \\(\\left(a^{4}\\right)^{3}\\), where "
            "\\(a>1\\). Which expression is equivalent to that count?"),
      choices=["\\(a^{7}\\)", "\\(a^{12}\\)", "\\(a^{43}\\)", "\\(a^{64}\\)"], correct="B",
      check="Multiply the exponents: 4 times 3 is 12."),

 dict(n="D2E-14", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A rumour spreads through a village so that the number of people who have heard it h "
            "hours after it starts is \\(P(h)=5\\cdot 2^{h}\\). How many people have heard the "
            "rumour 4 hours after it starts?"),
      choices=["20", "40", "80", "160"], correct="C",
      check="5(2^4) = 5(16) = 80."),

 dict(n="D2E-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A trail mix is made with 2 parts almonds to 3 parts raisins by mass. One batch "
            "contains 480 grams of raisins. How many grams of almonds are in that batch?"),
      choices=["240", "288", "300", "320"], correct="D",
      check="(2/3)(480) = 320."),

 dict(n="D2E-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("The membership of a museum rose from 400 people to 460 people in one year. By what "
            "percent did the membership rise?"),
      choices=["12%", "13%", "15%", "60%"], correct="C",
      check="60/400 = 0.15, which is 15%."),

 dict(n="D2E-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of minutes a swimmer trained on each of four days."
            + table(["Day", "Minutes trained"],
                    [["Monday", "48"], ["Tuesday", "65"], ["Wednesday", "52"], ["Thursday", "61"]])
            + "How many more minutes did the swimmer train on Tuesday than on Monday?"),
      choices=["13", "17", "24", "113"], correct="B",
      check="65 - 48 = 17."),

 dict(n="D2E-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A hockey team scored 1, 3, 3, 4 and 9 goals in its five matches this month. What is "
            "the mean number of goals the team scored per match?"),
      choices=["3", "3.5", "4", "5"], correct="C",
      check="(1+3+3+4+9)/5 = 20/5 = 4."),

 dict(n="D2E-19", domain="GT", skill="GT-LA", type="MC",
      stem=("A surveyor stakes out a triangular plot in which two of the angles measure 48&deg; "
            "and 79&deg;. What is the measure, in degrees, of the third angle?"),
      choices=["45", "53", "63", "127"], correct="B",
      check="180 - 48 - 79 = 53."),

 dict(n="D2E-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A gardener marks out a flowerbed shaped like a triangle whose base measures 14 metres "
            "and whose height measures 6 metres. How many square metres of ground does the "
            "flowerbed cover?"),
      answers=["42"],
      check="(1/2)(14)(6) = 42."),

 dict(n="D2E-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A storage bin is a cube whose edges are each 7 feet long. What is the volume of the "
            "bin, in cubic feet?"),
      answers=["343"],
      check="7^3 = 343."),

 dict(n="D2E-22", domain="GT", skill="GT-TR", type="FR",
      stem=("A ladder 26 feet long leans against a vertical wall, with the foot of the ladder 10 "
            "feet from the base of the wall. How many feet up the wall does the top of the ladder "
            "reach?"),
      answers=["24"],
      check="sqrt(26^2 - 10^2) = sqrt(576) = 24."),
]


# ------------------------------------------------------------ Module 2 Hard
MODULE_2_HARD = [
 dict(n="D2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A shipping planner writes two loading constraints as \\(4x+3y=26\\) and "
            "\\(kx+9y=57\\), where x and y are the numbers of two kinds of container and k is a "
            "constant. No pair \\((x,y)\\) satisfies both constraints. What is the value of k?"),
      choices=["3", "6", "9", "12"], correct="D",
      check="Parallel lines need 4(9) = 3k, so k = 12; the constants then rule out a common line."),

 dict(n="D2H-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A pyrometer converts a raw count x into a temperature offset \\(f(x)\\), and f is a "
            "linear function. The instrument's calibration certificate records \\(f(2)=-5\\) and "
            "\\(f(8)=13\\). What is the value of \\(f(-3)\\)?"),
      choices=["-23", "-20", "-14", "-8"], correct="B",
      check="Slope 18/6 = 3 and f(x) = 3x - 11, so f(-3) = -20."),

 dict(n="D2H-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A community kitchen makes soup and stew. Each litre of soup needs 2 minutes of "
            "preparation and each litre of stew needs 5 minutes, and the kitchen has at most 240 "
            "minutes of preparation time. The kitchen must also make at least twice as many litres "
            "of soup as of stew. What is the greatest whole number of litres of stew the kitchen "
            "can make?"),
      choices=["24", "26", "30", "48"], correct="B",
      check="With soup at twice the stew, 4w + 5w = 9w <= 240 gives w <= 26.6, so 26 litres."),

 dict(n="D2H-04", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A rectangular reflecting pool measuring 12 metres by 8 metres is bordered on all four "
            "sides by a walkway of uniform width w metres. The walkway covers exactly as much "
            "ground as the pool itself. What is the value of w?"),
      choices=["2", "3", "4", "6"], correct="A",
      check="(12+2w)(8+2w) - 96 = 96 gives 4w^2 + 40w - 96 = 0, whose positive root is 2."),

 dict(n="D2H-05", domain="ADV", skill="ADV-NF", type="MC",
      stem=("Two stages of a water treatment plant are modelled by \\(g(x)=2x-5\\) and "
            "\\(f(x)=x^{2}+x\\), applied in that order so that the output of g becomes the input "
            "of f. Which expression is equivalent to \\(f(g(x))\\)?"),
      choices=["\\(2x^{2}+2x-5\\)", "\\(4x^{2}-20x+20\\)", "\\(4x^{2}-18x+30\\)",
               "\\(4x^{2}-18x+20\\)"], correct="D",
      check="(2x-5)^2 + (2x-5) = 4x^2 - 20x + 25 + 2x - 5 = 4x^2 - 18x + 20."),

 dict(n="D2H-06", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A ballistics report gives the height of a test round above a datum line, in metres, "
            "as \\(h(x)=2x^{2}-16x+35\\). Which form of the expression displays the least height "
            "the round reaches as a constant or coefficient?"),
      choices=["\\(2(x-4)^{2}+3\\)", "\\(2(x-4)^{2}-3\\)", "\\(2(x-8)^{2}+3\\)",
               "\\((2x-8)^{2}+3\\)"], correct="A",
      check="2(x-4)^2 + 3 expands to 2x^2 - 16x + 35, and the least height is the constant 3."),

 dict(n="D2H-07", domain="ADV", skill="ADV-NE", type="MC",
      stem=("Two pumps working together empty a flooded cellar in 4 hours. Working alone, the "
            "larger pump would take 6 hours less than the smaller pump would take alone. How many "
            "hours would the smaller pump take to empty the cellar alone?"),
      choices=["8", "10", "12", "18"], correct="C",
      check="1/s + 1/(s-6) = 1/4 gives s^2 - 14s + 24 = 0, and only s = 12 exceeds 6."),

 dict(n="D2H-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A materials engineer reduces the quantity "
            "\\(\\frac{\\left(8a^{9}\\right)^{\\frac{2}{3}}}{2a^{3}}\\), where \\(a>0\\). Which "
            "expression is equivalent to that quantity?"),
      choices=["\\(2a^{6}\\)", "\\(4a^{3}\\)", "\\(4a^{6}\\)", "\\(2a^{3}\\)"], correct="D",
      check="The numerator is 4a^6, and dividing by 2a^3 leaves 2a^3."),

 dict(n="D2H-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The cross-section of a skateboard bowl is the graph of \\(y=a(x-3)^{2}-8\\), where a "
            "is a constant and x and y are measured in feet. The lowest point of the bowl is at "
            "\\((3,-8)\\), and the rim of the bowl passes through \\((5,4)\\). What is the value "
            "of a?"),
      choices=["2", "3", "4", "6"], correct="B",
      check="4 = a(2)^2 - 8 gives 4a = 12 and a = 3."),

 dict(n="D2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A control loop is described as critically damped when the equation "
            "\\(3x^{2}+kx+12=0\\) has exactly one real solution, where k is a positive constant. "
            "What is the value of k?"),
      choices=["6", "9", "12", "24"], correct="C",
      check="The discriminant k^2 - 144 is zero when k = 12, taking the positive value."),

 dict(n="D2H-11", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A pharmacist mixes a 15% saline solution with a 40% saline solution to obtain 500 "
            "millilitres of a 24% saline solution. How many millilitres of the 40% solution does "
            "the pharmacist use?"),
      choices=["120", "150", "180", "320"], correct="C",
      check="0.15(500-y) + 0.40y = 120 gives 0.25y = 45 and y = 180."),

 dict(n="D2H-12", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A forester selected 200 oaks at random from a plantation of 4,000 oaks and found that "
            "38 of the selected oaks showed signs of a fungal blight. Which of the following is "
            "the most appropriate conclusion?"),
      choices=["Exactly 760 of the oaks in the plantation show signs of the blight.",
               "The blight will eventually reach every oak in the plantation.",
               "Nothing about the plantation as a whole can be concluded from a sample.",
               "It is reasonable to estimate that about 760 of the oaks in the plantation show "
               "signs of the blight."],
      correct="D",
      check="A random sample supports an estimate for the population, not an exact count."),

 dict(n="D2H-13", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A shop recorded the number of umbrellas it sold on each of 9 days, and the mean of "
            "the 9 figures was 14. The owner then found that one day's figure had been entered as "
            "8 when it should have been 26. What is the mean of the 9 corrected figures?"),
      choices=["15", "15.5", "16", "18"], correct="C",
      check="The total rises by 18, from 126 to 144, so the mean is 144/9 = 16."),

 dict(n="D2H-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A dye vat must be filled with 3,600 litres of liquid in which the ratio of water to "
            "concentrate is 11 to 1 by volume. Concentrate is sold only in 25-litre drums. What is "
            "the least number of drums of concentrate needed to fill the vat?"),
      choices=["10", "12", "15", "24"], correct="B",
      check="Concentrate is 3,600/12 = 300 litres, and 300/25 = 12 drums."),

 dict(n="D2H-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of visitors to a botanical garden in each season of one "
            "year, together with the mean amount each visitor spent in the garden's shop."
            + table(["Season", "Visitors", "Mean spend per visitor ($)"],
                    [["Spring", "8,400", "6.50"], ["Summer", "15,200", "9.25"],
                     ["Autumn", "7,600", "5.80"], ["Winter", "4,300", "4.20"]])
            + "By how many dollars did total summer spending exceed the combined total spending of "
              "the other three seasons?"),
      choices=["$16,320", "$23,860", "$25,340", "$31,200"], correct="B",
      check="Summer is $140,600; the other three total $116,740; the difference is $23,860."),

 dict(n="D2H-16", domain="GT", skill="GT-LA", type="MC",
      stem=("A steel truss plate has the shape of a right triangle. The perpendicular dropped from "
            "the right-angle vertex to the hypotenuse divides the hypotenuse into two segments, of "
            "lengths 4 centimetres and 9 centimetres. What is the length, in centimetres, of that "
            "perpendicular?"),
      choices=["5", "6", "6.5", "13"], correct="B",
      check="The perpendicular is the geometric mean of the segments: sqrt(4 times 9) = 6."),

 dict(n="D2H-17", domain="GT", skill="GT-AV", type="MC",
      stem=("A conical funnel has a radius of 6 centimetres and a height of 16 centimetres, with "
            "its apex at the bottom. Sand fills the funnel to half its height, measured upward "
            "from the apex. What volume of sand, in cubic centimetres, is in the funnel?"),
      choices=["\\(12\\pi\\)", "\\(18\\pi\\)", "\\(24\\pi\\)", "\\(48\\pi\\)"], correct="C",
      check="The sand forms a similar cone of radius 3 and height 8, of volume (1/3) pi (9)(8) = 24 pi."),

 dict(n="D2H-18", domain="GT", skill="GT-TR", type="MC",
      stem=("A surveyor's plot is a right triangle \\(ABC\\) with the right angle at C, and the "
            "surveyor's notes record \\(\\tan A=\\frac{5}{12}\\). What is the value of "
            "\\(\\sin A\\)?"),
      choices=["\\(\\frac{5}{13}\\)", "\\(\\frac{12}{13}\\)", "\\(\\frac{13}{5}\\)",
               "\\(\\frac{5}{12}\\)"], correct="A",
      check="Legs 5 and 12 give a hypotenuse of 13, so sin A = 5/13."),

 dict(n="D2H-19", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A workshop makes brackets on two machines. Machine P makes 4 brackets an hour and "
            "machine Q makes 7 brackets an hour. Machine Q may be run for at most 8 hours, and the "
            "workshop needs at least 88 brackets. What is the least whole number of hours for "
            "which machine P must be run?"),
      choices=["6", "8", "10", "12"], correct="B",
      check="With Q at its 8-hour limit, 4p + 56 >= 88 gives p >= 8."),

 dict(n="D2H-20", domain="ALG", skill="ALG-LF", type="FR",
      stem=("The price of a ski resort's season pass is a linear function of the number of lifts "
            "the pass covers. A pass covering 6 lifts costs $342, and a pass covering 10 lifts "
            "costs $510. How many dollars does a pass covering 15 lifts cost?"),
      answers=["720"],
      check="Slope 168/4 = 42 per lift and intercept 342 - 252 = 90, so 90 + 15(42) = 720."),

 dict(n="D2H-21", domain="ALG", skill="ALG-LE", type="FR",
      stem=("In a two-person relay, the first runner covers a certain distance at a constant 12 "
            "kilometres per hour, and the second runner covers twice that distance at a constant 8 "
            "kilometres per hour. The relay takes 4 hours in total. How many kilometres did the "
            "first runner cover?"),
      answers=["12"],
      check="d/12 + 2d/8 = 4 gives d/3 = 4 and d = 12."),

 dict(n="D2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A solid sphere of radius 6 centimetres is melted down and recast, with no loss of "
            "metal, into identical solid cylinders each of radius 2 centimetres and height 3 "
            "centimetres. How many such cylinders are made?"),
      answers=["24"],
      check="The sphere is 288 pi and each cylinder is 12 pi, so 288/12 = 24."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
