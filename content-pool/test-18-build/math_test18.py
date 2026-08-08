#!/usr/bin/env python3
"""
Original Math content for Test 18 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium, deliberately harder than a stock Module 1.
                Almost every item makes a constant, a rate, a unit price or an
                unknown be recovered first and only then used; two or three
                steps throughout. Clearly harder than Module 2 (Easy) and
                clearly below Module 2 (Hard).
  MODULE_2_EASY genuinely one-step — the lower branch of the adaptive split.
                One operation, no recovery step.
  MODULE_2_HARD hard, and harder than a stock hard module. Parameters instead
                of numbers, structural and symbolic answer choices, a composed
                function, a system conditioned on a constant, an inequality
                chain, and geometry needing two relationships chained.

Every setting is drawn from Test 18's assigned thematic territory — aviation
and ballooning, brewing and malting, watchmaking and clock escapements,
quarrying and stonemasonry, orchards and cider pressing, wind pumps, bell
founding, blacksmithing, cooperage, hop drying, gliding and thermals, airship
mooring, sundials, marble cutting and grafting stock — and is deliberately
unlike anything already banked in production. House style follows Test 1/2 —
see CLAUDE.md. All LaTeX is typed by hand; no bulk conversion step was used
anywhere in this file.
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
      stem=("A cooperage buys oak staves and ash hoops, paying the same price for every stave and "
            "the same price for every hoop. An order of 8 staves and 3 hoops costs $131, and an "
            "order of 5 staves and 6 hoops costs $152. What is the cost, in dollars, of an order "
            "of 6 staves and 2 hoops?"),
      choices=["94", "104", "112", "122"], correct="A",
      check="8s+3h=131 and 5s+6h=152 give s = 10 and h = 17, so 6(10) + 2(17) = 94."),

 dict(n="H1-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The shadow cast by a sundial's gnomon shortens at a constant rate through the "
            "morning. The shadow was 96 centimetres long at 8:00 in the morning and 51 centimetres "
            "long at 11:00 that same morning. According to this model, how many hours after 8:00 "
            "is the shadow 21 centimetres long?"),
      choices=["4", "5", "6", "8"], correct="B",
      check="The shadow shortens by 45 cm in 3 hours, so 15 cm an hour, and 75/15 = 5."),

 dict(n="H1-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A balloon may lift off only if the total mass it carries is at most 480 kilograms. "
            "The pilot and the basket together have a mass of 195 kilograms, two passengers of "
            "mass 74 kilograms each are aboard, and each bag of ballast has a mass of 18 "
            "kilograms. What is the greatest number of ballast bags the balloon can carry at "
            "lift-off?"),
      choices=["5", "6", "7", "8"], correct="C",
      check="480 - 195 - 148 = 137 kilograms spare, and 137/18 is 7.6, so 7 bags."),

 dict(n="H1-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("Two rigs drill along a quarry face. The first rig has already drilled 340 metres and "
            "drills a further 25 metres in each shift; the second has already drilled 460 metres "
            "and drills a further 15 metres in each shift. How many metres will each rig have "
            "drilled when the two have drilled the same total length?"),
      choices=["300", "480", "600", "640"], correct="D",
      check="340 + 25s = 460 + 15s gives s = 12 shifts, and 340 + 25(12) = 640 metres."),

 dict(n="H1-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A wind pump feeds a reservoir that already holds 1,250 litres when the pump is "
            "started, and the pump adds 340 litres for every hour it runs. The reservoir has to be "
            "emptied as soon as it holds 12,450 litres. The pump runs for 9 hours on each day of a "
            "spell of steady wind. On which day of that spell does the reservoir first have to be "
            "emptied?"),
      choices=["4", "5", "6", "7"], correct="A",
      check="(12,450 - 1,250)/340 = 32.9 hours of pumping, and 32.9/9 falls in the fourth day."),

 dict(n="H1-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A blacksmith's store held 560 kilograms of coke at the start of a week, and every "
            "forging uses the same mass of coke. After 12 forgings 344 kilograms of coke were "
            "left. How many kilograms are left after 20 forgings?"),
      choices=["182", "200", "216", "224"], correct="B",
      check="216 kilograms over 12 forgings is 18 each, and 560 - 20(18) = 200."),

 dict(n="H1-07", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A quarry lorry made 34 trips in one week, each trip carrying either granite blocks or "
            "ballast and nothing else. Every granite trip carried 8 tonnes and every ballast trip "
            "carried 14 tonnes, and the lorry carried 386 tonnes in all that week. How many "
            "ballast trips did the lorry make?"),
      choices=["13", "15", "19", "21"], correct="C",
      check="g + b = 34 with 8g + 14b = 386 gives 6b = 114, so b = 19."),

 dict(n="H1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A cooper chamfers both ends of a stave. The oak taken off, in cubic centimetres, is "
            "modelled by \\((2w+5)(w-3)-\\left(w^{2}-4w\\right)\\), where w is the width of the "
            "stave in centimetres. Which expression is equivalent to that model?"),
      choices=["\\(w^{2}-5w-15\\)", "\\(3w^{2}-w-15\\)", "\\(w^{2}+3w+15\\)",
               "\\(w^{2}+3w-15\\)"], correct="D",
      check="(2w+5)(w-3) = 2w^2 - w - 15, and taking away w^2 - 4w leaves w^2 + 3w - 15."),

 dict(n="H1-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The moisture content of the hops in an oast house, in percent, h hours after the kiln "
            "is lit is modelled by \\(M(h)=\\frac{288}{h+4}\\). After how many hours does this "
            "model give a moisture content of 18 percent?"),
      choices=["12", "14", "18", "20"], correct="A",
      check="288/18 = 16, so h + 4 = 16 and h = 12."),

 dict(n="H1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("An airship's ballonet is bled so that the pressure inside it, in pascals, t hours "
            "after the valve is opened is modelled by "
            "\\(P(t)=1{,}600\\left(\\frac{1}{2}\\right)^{\\frac{t}{3}}\\). After how many hours "
            "does this model give a pressure of 100 pascals?"),
      choices=["8", "12", "16", "24"], correct="B",
      check="1,600/100 = 16 = 2^4, so t/3 = 4 and t = 12."),

 dict(n="H1-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The pitch of a bell, in hertz, varies inversely with the square of the diameter of "
            "its mouth, so that \\(f=\\frac{k}{d^{2}}\\) for some constant k, where d is that "
            "diameter in metres. A bell whose mouth is 1.2 metres across sounds at 500 hertz. What "
            "is the pitch, in hertz, of a bell from the same foundry whose mouth is 2 metres "
            "across?"),
      choices=["120", "144", "180", "300"], correct="C",
      check="k = 500(1.2)^2 = 720, and 720/2^2 = 180."),

 dict(n="H1-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A stonemason's estimating rule gives the number of blocks needed for a wall as "
            "\\(N=\\frac{3A}{2t}\\), where A is the area of the wall face and t is the thickness "
            "of one block. Which expression gives t in terms of N and A?"),
      choices=["\\(\\frac{2N}{3A}\\)", "\\(\\frac{3AN}{2}\\)", "\\(\\frac{2A}{3N}\\)",
               "\\(\\frac{3A}{2N}\\)"], correct="D",
      check="2tN = 3A, so t = 3A/(2N)."),

 dict(n="H1-13", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A slab of marble is cut so that its length is 4 centimetres more than 3 times its "
            "width, and the slab covers 644 square centimetres. What is the length of the slab, in "
            "centimetres?"),
      choices=["14", "42", "46", "52"], correct="C",
      check="w(3w+4) = 644 gives w = 14, so the length is 3(14) + 4 = 46."),

 dict(n="H1-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A cider press yields 7 litres of juice from every 11 kilograms of apples. An "
            "orchard's crop of 3,300 kilograms of apples is pressed, and the juice is run off into "
            "casks holding 15 litres each. How many casks are filled completely?"),
      choices=["140", "150", "210", "300"], correct="A",
      check="3,300/11 = 300 lots of 7 litres is 2,100 litres, and 2,100/15 = 140."),

 dict(n="H1-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A maltings held 4,800 kilograms of barley at the start of autumn. Its stock fell by "
            "25 percent during autumn and then rose by 12 percent during winter. How many "
            "kilograms of barley did the maltings hold at the end of winter?"),
      choices=["3,960", "4,032", "4,140", "4,224"], correct="B",
      check="4,800(0.75) = 3,600, and 3,600(1.12) = 4,032."),

 dict(n="H1-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of hours each of four wind pumps ran last month and the "
            "volume of water each pump raised in that time."
            + table(["Wind pump", "Hours run", "Water raised (litres)"],
                    [["Aldergate", "120", "90,000"], ["Chalk Down", "150", "108,000"],
                     ["Barrow Fen", "180", "148,500"], ["Denhill", "200", "156,000"]])
            + "Which pump raised the greatest volume of water for each hour that it ran?"),
      choices=["Aldergate", "Chalk Down", "Barrow Fen", "Denhill"], correct="C",
      check="The hourly volumes are 750, 720, 825 and 780 litres, and 825 is the greatest."),

 dict(n="H1-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the casks a cooperage repaired last quarter, classified by the kind "
            "of cask and by whether the repair called for a new head."
            + table(["Kind of cask", "Repair called for a new head",
                     "Repair did not call for a new head"],
                    [["Hogshead", "84", "116"], ["Butt", "56", "44"], ["Firkin", "60", "40"]])
            + "Of the casks whose repair called for a new head, what percent were hogsheads?"),
      choices=["21%", "28%", "30%", "42%"], correct="D",
      check="84 + 56 + 60 = 200 casks needed a new head, and 84/200 = 42 percent."),

 dict(n="H1-18", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("The mean mass of the 9 bells in a peal is 284 kilograms. When the tenor, the heaviest "
            "of the 9, is left out, the mean mass of the remaining 8 bells is 246 kilograms. What "
            "is the mass of the tenor, in kilograms?"),
      answers=["588"],
      check="9(284) - 8(246) = 2,556 - 1,968 = 588."),

 dict(n="H1-19", domain="GT", skill="GT-LA", type="MC",
      stem=("A straight quarry ramp runs from A to D, with the points B and C lying on it in that "
            "order, so that \\(AB=3x\\) metres, \\(BC=x+8\\) metres, \\(CD=2x-5\\) metres and "
            "\\(AD=63\\) metres. What is the length of \\(BC\\), in metres?"),
      choices=["18", "20", "24", "30"], correct="A",
      check="3x + (x+8) + (2x-5) = 63 gives x = 10, so BC = 10 + 8 = 18."),

 dict(n="H1-20", domain="GT", skill="GT-TR", type="MC",
      stem=("A ground crew runs a mooring cable in a straight line from the nose of a moored "
            "airship to an anchor on level ground. The cable makes an angle of 60&deg; with the "
            "ground, and the anchor lies 14 metres from the point on the ground directly below "
            "the nose. The crew started with 45 metres of cable wound on a drum. How many metres "
            "of cable are left on the drum once the cable reaches the anchor?"),
      choices=["11", "17", "21", "31"], correct="B",
      check="cos 60 = 14/L gives a cable of 28 metres, so 45 - 28 = 17 metres are left."),

 dict(n="H1-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A quarry cuts a rectangular block of granite measuring 1.2 metres by 0.8 metres by "
            "0.5 metres. This granite has a mass of 2,700 kilograms for each cubic metre. What is "
            "the mass of the block, in kilograms?"),
      answers=["1296"],
      check="1.2(0.8)(0.5) = 0.48 cubic metres, and 0.48(2,700) = 1,296."),

 dict(n="H1-22", domain="GT", skill="GT-AV", type="FR",
      stem=("Barley stands to a depth of 5 metres in a cylindrical silo whose base has a radius of "
            "2 metres. All of that barley is moved into a second cylindrical silo whose base has a "
            "radius of 5 metres. To what depth, in metres, does the barley stand in the second "
            "silo?"),
      answers=["0.8", "4/5"],
      check="The barley occupies 20 pi cubic metres, and 20 pi divided by 25 pi is 0.8."),
]


# ------------------------------------------------------------ Module 2 Easy
MODULE_2_EASY = [
 dict(n="H2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A blacksmith charges $9 for each horseshoe made. A farrier was charged $153 for "
            "horseshoes. How many horseshoes were made for that farrier?"),
      choices=["17", "18", "19", "21"], correct="A",
      check="153/9 = 17."),

 dict(n="H2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A bell founder adds x kilograms of tin to 340 kilograms of copper, and the bell metal "
            "that results has a mass of 425 kilograms. What is the value of x?"),
      choices=["75", "85", "95", "105"], correct="B",
      check="425 - 340 = 85."),

 dict(n="H2E-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A watchmaker has finished 15 movements so far and finishes 4 more in each week that "
            "follows. Which expression gives the number of movements the watchmaker has finished "
            "after w further weeks?"),
      choices=["\\(4w-15\\)", "\\(15w+4\\)", "\\(15+4w\\)", "\\(19w\\)"], correct="C",
      check="Start at 15 and add 4 for each further week."),

 dict(n="H2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A gliding club prices an aerotow launch by the rule \\(C(m)=38+0.60m\\), where m is "
            "the number of minutes the tug is airborne and \\(C(m)\\) is the charge in dollars. "
            "What is the best interpretation of 0.60 in this model?"),
      choices=["The charge, in dollars, that applies to every launch however long the tug is "
               "airborne.",
               "The number of minutes the tug is airborne when the charge is $38.",
               "The total charge, in dollars, for a launch with the tug airborne for 38 minutes.",
               "The charge, in dollars, for each further minute the tug is airborne."],
      correct="D",
      check="0.60 multiplies the minutes, so it is the charge added by each further minute."),

 dict(n="H2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A picking ladder in an orchard may carry a load of at most 130 kilograms. A picker "
            "whose mass is 78 kilograms climbs the ladder carrying a bag of apples of mass a "
            "kilograms. Which inequality gives every possible value of a?"),
      choices=["\\(a\\ge 52\\)", "\\(a\\le 130\\)", "\\(a\\le 208\\)", "\\(a\\le 52\\)"],
      correct="D",
      check="78 + a is at most 130, so a is at most 52."),

 dict(n="H2E-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A barrel holds 90 gallons of cider, and 7 gallons are drawn off each day. After how "
            "many days does the barrel hold 34 gallons?"),
      choices=["8", "9", "12", "14"], correct="A",
      check="90 - 7d = 34 gives 7d = 56 and d = 8."),

 dict(n="H2E-07", domain="ALG", skill="ALG-LF", type="MC",
      stem=("An airship has 84 metres of mooring cable let out at noon, and the ground crew lets "
            "out 6 more metres in each hour after noon. How many metres of cable are let out 5 "
            "hours after noon?"),
      choices=["90", "114", "120", "126"], correct="B",
      check="84 + 6(5) = 114."),

 dict(n="H2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A hop-drying schedule takes \\(3(2q-7)\\) hours, where q is the number of loads "
            "dried. Which expression is equivalent to \\(3(2q-7)\\)?"),
      choices=["\\(6q-7\\)", "\\(5q-21\\)", "\\(6q-21\\)", "\\(2q-21\\)"], correct="C",
      check="3(2q) = 6q and 3(-7) = -21."),

 dict(n="H2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A square quarry tile of side x centimetres has a square of side 7 centimetres cut out "
            "of it, so the area left, in square centimetres, is \\(x^{2}-49\\). Which expression "
            "is equivalent to \\(x^{2}-49\\)?"),
      choices=["\\((x-7)^{2}\\)", "\\((x+7)^{2}\\)", "\\(x(x-49)\\)", "\\((x-7)(x+7)\\)"],
      correct="D",
      check="A difference of two squares factors as (x-7)(x+7)."),

 dict(n="H2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A bell founder's costing rule gives the cost of a bell, in hundreds of dollars, as "
            "\\(C(d)=5d^{2}+40\\), where d is the diameter of the bell's mouth in feet. What is "
            "the value of \\(C(6)\\)?"),
      choices=["100", "130", "190", "220"], correct="D",
      check="5(36) + 40 = 220."),

 dict(n="H2E-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A watchmaker's gauge reading is computed as \\(\\sqrt{n+7}\\), where n is the number "
            "of jewels in a movement. The reading for one movement is 5. What is the value of n?"),
      choices=["18", "25", "32", "39"], correct="A",
      check="n + 7 = 25, so n = 18."),

 dict(n="H2E-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The sugar left in a fermenting wort, in grams per litre, is modelled by "
            "\\(S(d)=81\\left(\\frac{1}{3}\\right)^{d}\\), where d is the number of days since the "
            "yeast was pitched. How many grams per litre of sugar are left 2 days after pitching?"),
      choices=["3", "9", "27", "54"], correct="B",
      check="81(1/9) = 9."),

 dict(n="H2E-13", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A balloon designer's notes record an envelope index as "
            "\\(\\left(2x^{3}\\right)^{4}\\). Which expression is equivalent to "
            "\\(\\left(2x^{3}\\right)^{4}\\)?"),
      choices=["\\(8x^{12}\\)", "\\(2x^{12}\\)", "\\(16x^{12}\\)", "\\(16x^{7}\\)"], correct="C",
      check="2^4 = 16 and the exponent 3 is multiplied by 4."),

 dict(n="H2E-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Malt costs $1.35 for each kilogram. What is the cost of 40 kilograms of malt?"),
      choices=["$27", "$29.60", "$48.60", "$54"], correct="D",
      check="40(1.35) = 54."),

 dict(n="H2E-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A blacksmith drew 250 nails in a day and rejected 12 percent of them. How many of "
            "those nails did the blacksmith reject?"),
      choices=["30", "45", "88", "220"], correct="A",
      check="0.12(250) = 30."),

 dict(n="H2E-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of casks a cooperage made in each of four weeks."
            + table(["Week", "Casks made"],
                    [["1", "38"], ["2", "45"], ["3", "52"], ["4", "41"]])
            + "How many more casks did the cooperage make in week 3 than in week 1?"),
      choices=["7", "14", "17", "21"], correct="B",
      check="52 - 38 = 14."),

 dict(n="H2E-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of gliders a club launched by winch and by aerotow on each "
            "of four days."
            + table(["Day", "Winch launches", "Aerotow launches"],
                    [["Thursday", "14", "9"], ["Friday", "11", "16"],
                     ["Saturday", "23", "12"], ["Sunday", "19", "21"]])
            + "On which of these days were the most gliders launched by winch?"),
      choices=["Thursday", "Friday", "Saturday", "Sunday"], correct="C",
      check="The winch counts are 14, 11, 23 and 19, and 23 is the greatest."),

 dict(n="H2E-18", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("The masses, in kilograms, of the six anvils in a blacksmith's shop are 82, 95, 74, "
            "110, 88 and 91. What is the mean of these six masses, in kilograms?"),
      answers=["90"],
      check="The six masses total 540, and 540/6 = 90."),

 dict(n="H2E-19", domain="GT", skill="GT-LA", type="MC",
      stem=("A blacksmith scribes a straight line across the square corner of a plate, cutting "
            "that right angle into two smaller angles. One of the two measures 34&deg;. What is "
            "the measure, in degrees, of the other?"),
      choices=["56", "66", "124", "146"], correct="A",
      check="The two angles make up a right angle, so 90 - 34 = 56."),

 dict(n="H2E-20", domain="GT", skill="GT-AV", type="MC",
      stem=("A crate of dried hops is a rectangular box 8 feet long, 5 feet wide and 3 feet tall. "
            "A cooperage lines all six faces of the box with felt. How many square feet of felt "
            "does lining the box take?"),
      choices=["120", "158", "166", "240"], correct="B",
      check="2(8)(5) + 2(8)(3) + 2(5)(3) = 80 + 48 + 30 = 158."),

 dict(n="H2E-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A malting floor is L-shaped: a rectangle 12 metres by 5 metres joined along one edge "
            "to a rectangle 4 metres by 3 metres. What is the total area of the floor, in square "
            "metres?"),
      answers=["72"],
      check="12(5) = 60 and 4(3) = 12, and 60 + 12 = 72."),

 dict(n="H2E-22", domain="GT", skill="GT-TR", type="FR",
      stem=("A smith bends a bracket into a right triangle in which one of the acute angles "
            "measures 30&deg; and the hypotenuse measures 18 centimetres. How many centimetres "
            "long is the side opposite the 30&deg; angle?"),
      answers=["9"],
      check="The side opposite a 30 degree angle is half the hypotenuse."),
]


# ------------------------------------------------------------ Module 2 Hard
MODULE_2_HARD = [
 dict(n="H2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A maltings blends x tonnes of pale malt with y tonnes of crystal malt. The blend must "
            "satisfy both of the following conditions.<br/>\\(x+3y=17\\)<br/>\\(3x+y=23\\)<br/>By "
            "how many tonnes does the pale malt in the blend exceed the crystal malt?"),
      choices=["3", "5", "10", "13"], correct="A",
      check="Subtracting the first condition from the second gives 2x - 2y = 6, so x - y = 3."),

 dict(n="H2H-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A watch regulator's correction is a linear function f. In the xy-plane the graph of "
            "\\(y=f(x)\\) passes through the point \\((-2,13)\\) and has the same slope as the "
            "line \\(5x+2y=9\\). What is the value of \\(f(6)\\)?"),
      choices=["-27", "-7", "3", "33"], correct="B",
      check="5x+2y=9 has slope -5/2, and 13 - (5/2)(8) = -7."),

 dict(n="H2H-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A hop kiln's damper setting x must satisfy \\(-7<4-3x\\le 13\\). Which of the "
            "following gives every value of x that satisfies this condition?"),
      choices=["\\(x<\\frac{11}{3}\\)", "\\(-3<x\\le \\frac{11}{3}\\)",
               "\\(-3\\le x<\\frac{11}{3}\\)", "\\(x\\ge -3\\)"], correct="C",
      check="4 - 3x <= 13 gives x >= -3, and 4 - 3x > -7 gives x < 11/3."),

 dict(n="H2H-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A brewer has 60 litres of wort whose extract is 12 percent by mass. The brewer adds x "
            "litres of water, which carries no extract, so that the extract of the diluted wort is "
            "9 percent. What is the value of x?"),
      choices=["12", "15", "20", "24"], correct="C",
      check="The extract stays at 7.2 litres, and 7.2/(60+x) = 0.09 gives 60 + x = 80."),

 dict(n="H2H-05", domain="ALG", skill="ALG-LF", type="FR",
      stem=("A quarry's crushing plant charges a fixed setup fee plus a fixed amount for each "
            "tonne crushed. Crushing 140 tonnes costs $1,930, and crushing 260 tonnes costs "
            "$3,250. How many dollars does crushing 400 tonnes cost?"),
      answers=["4790"],
      check="1,320/120 = $11 a tonne, so the setup fee is 1,930 - 1,540 = $390, and "
            "390 + 400(11) = 4,790."),

 dict(n="H2H-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A cooperage makes only casks and firkins. Each cask takes m staves and each firkin "
            "takes n staves, and the cooperage makes 3 times as many firkins as casks. Making them "
            "all takes T staves. Which expression gives the number of casks the cooperage makes?"),
      choices=["\\(\\frac{T}{3(m+n)}\\)", "\\(\\frac{T}{m+n}\\)", "\\(\\frac{3T}{m+3n}\\)",
               "\\(\\frac{T}{m+3n}\\)"], correct="D",
      check="If c casks are made then cm + 3cn = T, so c = T/(m+3n)."),

 dict(n="H2H-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A cider maker will press a delivery of apples only if its mass m, in kilograms, "
            "satisfies both \\(m\\ge 4{,}000\\) and \\(0.62m\\le 3{,}410\\). What is the greatest "
            "possible value of m?"),
      choices=["5,500", "5,750", "6,000", "6,250"], correct="A",
      check="3,410/0.62 = 5,500, which is also at least 4,000."),

 dict(n="H2H-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A quarry's blast-vibration model is the function f defined by \\(f(x)=2x^{2}-5\\). "
            "For a positive value a the model gives \\(f(a)=45\\). What is the value of "
            "\\(f(a+1)\\)?"),
      choices=["45", "67", "72", "95"], correct="B",
      check="2a^2 - 5 = 45 gives a = 5, and f(6) = 2(36) - 5 = 67."),

 dict(n="H2H-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A stress index for a quarry drill is written as "
            "\\(\\frac{x^{2}-x-12}{x^{2}-16}\\), where \\(x>4\\). Which expression is equivalent "
            "to this index?"),
      choices=["\\(\\frac{x-3}{x-4}\\)", "\\(\\frac{x+3}{x-4}\\)", "\\(\\frac{x+3}{x+4}\\)",
               "\\(\\frac{x+4}{x+3}\\)"], correct="C",
      check="(x-4)(x+3) over (x-4)(x+4) cancels to (x+3)/(x+4)."),

 dict(n="H2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The equation \\(kx^{2}-24x+16=0\\), where k is a nonzero constant, models the profile "
            "of a bell mould and has exactly one real solution. What is the value of k?"),
      choices=["3", "4", "6", "9"], correct="D",
      check="24^2 = 4(16)k gives 576 = 64k, so k = 9."),

 dict(n="H2H-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A hop-kiln timing rule is scaled so that its setting x satisfies "
            "\\(9^{x+4}=27^{x}\\). What is the value of x?"),
      choices=["2", "4", "6", "8"], correct="D",
      check="Writing both sides in base 3 gives 2x + 8 = 3x, so x = 8."),

 dict(n="H2H-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("The specification for a balloon fabric puts its strength ratio at "
            "\\(\\left(\\frac{16x^{8}}{y^{4}}\\right)^{\\frac{3}{4}}\\), for positive values of x "
            "and y. Which expression is equivalent to that strength ratio?"),
      choices=["\\(\\frac{8x^{6}}{y^{3}}\\)", "\\(\\frac{12x^{6}}{y^{3}}\\)",
               "\\(\\frac{8x^{11}}{y^{7}}\\)", "\\(\\frac{64x^{6}}{y^{3}}\\)"], correct="A",
      check="16 raised to the three-quarter power is 8, and each exponent is multiplied by 3/4."),

 dict(n="H2H-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A parabolic arch over a quarry haulage tunnel is modelled by \\(y=a(x-8)(x-20)\\), "
            "where x and y are measured in metres and a is a constant. The arch reaches its "
            "greatest height, 12 metres, above the tunnel floor. What is the value of a?"),
      choices=["\\(-\\frac{1}{2}\\)", "\\(-\\frac{1}{3}\\)", "\\(\\frac{1}{3}\\)", "\\(-3\\)"],
      correct="B",
      check="The greatest height is at x = 14, where a(6)(-6) = -36a = 12, so a = -1/3."),

 dict(n="H2H-14", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The mean thickness of the 12 marble tiles in a crate is 18 millimetres. One tile, 16 "
            "millimetres thick, is taken out and a thicker tile is put in its place, and the mean "
            "thickness of the 12 tiles in the crate becomes 18.5 millimetres. What is the "
            "thickness, in millimetres, of the tile that was put in?"),
      choices=["18.5", "20", "21", "22"], correct="D",
      check="The total rises by 12(0.5) = 6 millimetres, so the new tile is 16 + 6 = 22."),

 dict(n="H2H-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of bells a foundry cast in each of five years."
            + table(["Year", "Bells cast"],
                    [["2018", "120"], ["2019", "138"], ["2020", "156"], ["2021", "195"],
                     ["2022", "234"]])
            + "For which of these years was the percent increase in bells cast over the previous "
              "year the greatest?"),
      choices=["2019", "2020", "2021", "2022"], correct="C",
      check="The increases are 15%, about 13%, 25% and 20%, so 2021 is the greatest."),

 dict(n="H2H-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A quarry manager selected 60 of the 1,500 stone blocks cut in one month at random and "
            "weighed each of them. The mean mass of the selected blocks was 412 kilograms, with an "
            "associated margin of error of 9 kilograms. Which conclusion is best supported by "
            "these results?"),
      choices=["It is plausible that the mean mass of all 1,500 blocks cut that month is between "
               "403 kilograms and 421 kilograms.",
               "Every one of the 1,500 blocks cut that month has a mass between 403 kilograms and "
               "421 kilograms.",
               "The mean mass of all 1,500 blocks cut that month is exactly 412 kilograms.",
               "It is plausible that the mean mass of every stone block cut at every quarry is "
               "between 403 kilograms and 421 kilograms."],
      correct="A",
      check="A margin of error gives a plausible range for the mean of the population sampled, "
            "which here is the 1,500 blocks cut that month."),

 dict(n="H2H-17", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A wind pump raises 3.5 litres of water each second when its wheel turns at 20 "
            "revolutions per minute, and the volume raised each second is directly proportional "
            "to the wheel's speed. How many litres does the pump raise in 15 minutes while its "
            "wheel turns at 32 revolutions per minute?"),
      choices=["3,150", "5,040", "5,600", "8,064"], correct="B",
      check="3.5(32/20) = 5.6 litres a second, and 5.6(900) = 5,040."),

 dict(n="H2H-18", domain="PSDA", skill="PSDA-RP", type="FR",
      stem=("A nursery finds that 7 of every 12 scions cut from a particular apple tree take when "
            "they are grafted onto new stock. At this rate, how many of 456 scions cut from that "
            "tree would be expected to take?"),
      answers=["266"],
      check="456 divided by 12 is 38, and 38(7) = 266."),

 dict(n="H2H-19", domain="GT", skill="GT-LA", type="MC",
      stem=("A diagonal brace crosses two parallel beams of a bell frame. Where the brace meets "
            "the upper beam one of the angles measures \\((3x+10)\\) degrees, and where the brace "
            "meets the lower beam the corresponding angle measures \\((5x-30)\\) degrees. What is "
            "the measure, in degrees, of the angle supplementary to the angle at the upper beam?"),
      choices=["70", "110", "130", "150"], correct="B",
      check="Corresponding angles are equal, so 3x + 10 = 5x - 30 gives x = 20 and an angle of "
            "70 degrees, whose supplement is 110 degrees."),

 dict(n="H2H-20", domain="GT", skill="GT-AV", type="MC",
      stem=("A bell founder casts an ingot of bell metal as a right circular cylinder whose height "
            "is twice its radius. The ingot's volume is \\(128\\pi\\) cubic centimetres. What is "
            "the radius of the ingot, in centimetres?"),
      choices=["2", "3", "4", "8"], correct="C",
      check="pi r^2 (2r) = 2 pi r^3 = 128 pi gives r^3 = 64, so r = 4."),

 dict(n="H2H-21", domain="GT", skill="GT-TR", type="MC",
      stem=("A forged bracket has the shape of a right triangle \\(RST\\), with its right angle at "
            "S. In this bracket \\(\\sin R=\\frac{5}{13}\\). What is the value of "
            "\\(\\tan R\\)?"),
      choices=["\\(\\frac{5}{12}\\)", "\\(\\frac{12}{13}\\)", "\\(\\frac{12}{5}\\)",
               "\\(\\frac{13}{5}\\)"], correct="A",
      check="A 5-12-13 right triangle gives an adjacent leg of 12, so tan R = 5/12."),

 dict(n="H2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A cooper's vat is a right circular cylinder that holds 400 litres. A second vat is "
            "also a right circular cylinder; the radius of its base is 50 percent greater than the "
            "first vat's and its height is 20 percent less than the first vat's. How many litres "
            "does the second vat hold?"),
      answers=["720"],
      check="The volume is multiplied by 1.5 squared and by 0.8, and 400(2.25)(0.8) = 720."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
