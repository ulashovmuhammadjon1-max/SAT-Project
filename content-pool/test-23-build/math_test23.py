#!/usr/bin/env python3
"""
Original Math content for Test 23 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium. Almost every item makes a rate, a constant, a
                total or an unknown be recovered first and only then used;
                two or three steps throughout. Clearly above Module 2 (Easy),
                clearly below Module 2 (Hard).
  MODULE_2_EASY genuinely one-step — the lower branch of the adaptive split.
  MODULE_2_HARD hard: parameters in place of numbers, symbolic answer choices,
                a composed function, systems conditioned on a constant, an
                extraneous-root radical equation, similar solids, and a circle
                given in general form.

Every setting comes from Test 23's assigned territory — canal locks and
pounds, barge haulage, aqueducts, dredging, towpaths, wharves and quays and
canal toll keeping — and the territory is SPLIT across the adaptive branch,
because a student sees Module 1 and exactly one Module 2 module:

  Module 1          locks, lock gates and mitres, pounds and summit levels,
                    feeders and springs, aqueduct troughs, dredging and silt,
                    sluices and paddles, cuttings, reaches, lock keepers' logs
  Module 2 (both)   barges and barge horses, towpaths, wharves and quays,
                    warehouses, cargo (salt, grain, gravel), toll houses and
                    tolls, tally clerks, gauging and draught

verify_math_test23.py pass 4 enforces that split with a keyword check.

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
      stem=("The Barrowby flight has 16 locks and lifts a boat 72 metres in all. Each of the 4 "
            "locks at the head of the flight lifts a boat 2 metres more than each of the other 12 "
            "locks does. How many metres does each of the 4 locks at the head lift a boat?"),
      choices=["4", "4.5", "5", "6"], correct="D",
      check="12x + 4(x+2) = 72 gives 16x = 64 and x = 4, so a head lock lifts 4 + 2 = 6 metres."),

 dict(n="H1-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A steam dredger lifts 210 cubic metres of silt a day and a shovel gang lifts 90 cubic "
            "metres a day. The dredger started on a reach holding 4,500 cubic metres of silt and "
            "worked alone at first; the shovel gang then joined it, and the reach was clear at the "
            "end of the 18th day. On how many of those 18 days did the two work together?"),
      choices=["6", "8", "9", "12"], correct="B",
      check="The dredger lifted 18(210) = 3,780, leaving 720 for the shovel gang at 90 a day, so 8 days."),

 dict(n="H1-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A gauge on an aqueduct trough records the depth of water in the trough at four times "
            "after the sluice at its head is opened, and the depth rises at a constant rate."
            + table(["Minutes after the sluice was opened", "Depth of water (centimetres)"],
                    [["2", "31"], ["5", "43"], ["8", "55"], ["11", "67"]])
            + "What depth of water does this model give at the moment the sluice was opened?"),
      choices=["19", "21", "23", "27"], correct="C",
      check="The depth rises 12 cm every 3 minutes, so 4 cm a minute, and 31 - 2(4) = 23."),

 dict(n="H1-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A summit pound must be kept between 1.20 metres and 1.50 metres above the cill of its "
            "lower gates. Through a dry spell in which no boats are worked through, the depth above "
            "the cill, in metres, is 1.62 - 0.04t, where t is the number of hours since the spell "
            "began. The depth is within the required range for whole-number values of t from 3 up "
            "to some greatest value. What is that greatest value?"),
      choices=["10", "11", "12", "13"], correct="A",
      check="1.62 - 0.04t is at least 1.20 while t is at most 10.5, so the greatest whole number is 10."),

 dict(n="H1-05", domain="ALG", skill="ALG-LE", type="MC",
      stem=("Three reaches of a canal are to be dredged. The middle reach is 400 metres longer than "
            "the shortest reach, and the longest reach is twice the shortest. The three reaches "
            "measure 6,000 metres altogether. How many metres long is the longest reach?"),
      choices=["1,400", "1,800", "2,400", "2,800"], correct="D",
      check="x + (x+400) + 2x = 6,000 gives x = 1,400, so the longest is 2(1,400) = 2,800."),

 dict(n="H1-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A contractor's charge for dredging a reach is a fixed sum for bringing the plant to "
            "the site plus a fixed amount for each cubic metre of silt lifted. Lifting 900 cubic "
            "metres cost $6,150 and lifting 1,500 cubic metres cost $9,750. A third reach cost "
            "$10,950. How many cubic metres of silt were lifted from the third reach?"),
      choices=["1,600", "1,700", "1,825", "1,900"], correct="B",
      check="600 extra cubic metres cost $3,600, so $6 each and $750 fixed; (10,950 - 750)/6 = 1,700."),

 dict(n="H1-07", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The depth of water in a pound, in metres, is modelled by "
            "\\(d(t)=-0.05(t-14)^{2}+3.2\\), where t is the number of hours after midnight and "
            "\\(0 \\le t \\le 24\\). For how many hours of that day does the model give a depth of "
            "at least 3 metres?"),
      choices=["4", "5", "6", "8"], correct="A",
      check="d >= 3 needs (t-14)^2 <= 4, so t runs from 12 to 16, a span of 4 hours."),

 dict(n="H1-08", domain="ADV", skill="ADV-NE", type="MC",
      stem=("Silt stirred up by a passing boat settles out so that the mass still held in the "
            "water, in grams per cubic metre, is modelled by "
            "\\(s(t)=180\\left(\\frac{1}{2}\\right)^{\\frac{t}{9}}\\), where t is the number of "
            "minutes since the boat passed. After how many minutes does the model give 22.5 grams "
            "per cubic metre?"),
      choices=["18", "24", "27", "36"], correct="C",
      check="22.5 is 180 divided by 8, so t/9 = 3 and t = 27."),

 dict(n="H1-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("The speed v, in metres per second, at which water leaves a paddle under a head of h "
            "metres is modelled by \\(v=\\sqrt{2gh}\\), where g is a positive constant. Which "
            "expression gives h in terms of v and g?"),
      choices=["\\(\\frac{2v}{g}\\)", "\\(\\frac{v^{2}}{2g}\\)", "\\(\\frac{2g}{v^{2}}\\)",
               "\\(\\frac{v}{2g^{2}}\\)"], correct="B",
      check="Squaring gives v^2 = 2gh, so h = v^2/(2g)."),

 dict(n="H1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The number of boats waiting to pass a lock when the flight reopens after a stoppage "
            "of d days is modelled by \\(w(d)=d^{2}+6d\\). After how many days' stoppage does this "
            "model give 91 boats waiting?"),
      choices=["5", "7", "9", "13"], correct="B",
      check="d^2 + 6d - 91 = 0 factors as (d+13)(d-7), and only d = 7 is possible."),

 dict(n="H1-11", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Two feeder streams delivered a cubic metres and b cubic metres of water in an hour, "
            "where a - b = 7 and a + b = 13. What is the value of \\(a^{2}-b^{2}\\)?"),
      choices=["20", "49", "84", "91"], correct="D",
      check="a^2 - b^2 is (a+b)(a-b) = 13(7) = 91, without solving for either amount."),

 dict(n="H1-12", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A pound 2,400 metres long and 12 metres wide must be raised 15 centimetres before the "
            "deepest boats can pass along it. The feeder that supplies the pound delivers 480 cubic "
            "metres of water an hour. How many hours does raising the pound take?"),
      choices=["9", "10", "12", "15"], correct="A",
      check="2,400(12)(0.15) = 4,320 cubic metres, and 4,320/480 = 9 hours."),

 dict(n="H1-13", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A clerk added up the boats entered in 40 lock keepers' log books for one day and found "
            "a mean of 11.5 boats. Two of the books were then found to have been copied out "
            "wrongly: one had been entered as 4 boats when the book read 24, and the other as 1 "
            "boat when the book read 31. What is the corrected mean?"),
      choices=["12.25", "12.75", "13.25", "14"], correct="B",
      check="The total rises from 460 by 20 and by 30 to 510, and 510/40 = 12.75."),

 dict(n="H1-14", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the volume of silt lifted and the number of hours worked at each of "
            "four reaches during one season."
            + table(["Reach", "Silt lifted (cubic metres)", "Hours worked"],
                    [["Ashby Cut", "1,344", "28"], ["Brindle Reach", "1,530", "34"],
                     ["Croxall Reach", "2,014", "38"], ["Dunwater Cut", "1,196", "26"]])
            + "At which reach was the mean volume of silt lifted per hour greatest?"),
      choices=["Ashby Cut", "Brindle Reach", "Croxall Reach", "Dunwater Cut"], correct="C",
      check="The four rates are 48, 45, 53 and 46 cubic metres an hour, and 53 is the greatest."),

 dict(n="H1-15", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The table gives the boats worked through one lock in a day, by size and by whether "
            "they were loaded."
            + table(["", "Loaded", "Empty"],
                    [["Narrow boats", "84", "36"], ["Wide boats", "45", "15"]])
            + "Of the boats that were empty, what fraction were narrow boats?"),
      choices=["\\(\\frac{3}{10}\\)", "\\(\\frac{5}{17}\\)", "\\(\\frac{2}{3}\\)",
               "\\(\\frac{12}{17}\\)"], correct="D",
      check="36 of the 51 empty boats were narrow, and 36/51 = 12/17."),

 dict(n="H1-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of days in one 30-day month on which a lock was worked the "
            "stated number of times."
            + table(["Times the lock was worked", "Days"],
                    [["20", "5"], ["25", "12"], ["30", "9"], ["35", "4"]])
            + "What was the mean number of times a day that the lock was worked that month?"),
      choices=["25", "26.5", "27", "28.5"], correct="C",
      check="The month's total is 100 + 300 + 270 + 140 = 810 lockings, and 810/30 = 27."),

 dict(n="H1-17", domain="GT", skill="GT-LA", type="MC",
      stem=("The two leaves of a pair of lock gates each make an angle of 18&deg; with the straight "
            "line drawn across the chamber from one leaf's hinge to the other's, and the leaves "
            "meet at a point on the centre line of the chamber. That line and the two leaves form a "
            "triangle. What is the measure, in degrees, of the angle of that triangle at the point "
            "where the leaves meet?"),
      choices=["36", "72", "144", "162"], correct="C",
      check="The triangle's other two angles are 18 each, so the angle at the meeting point is 180 - 36 = 144."),

 dict(n="H1-18", domain="GT", skill="GT-AV", type="MC",
      stem=("A culvert that carries a stream under a canal embankment is a cylinder 2 metres in "
            "diameter and 45 metres long. How many cubic metres of water does the culvert contain "
            "when it is running full?"),
      choices=["\\(22.5\\pi\\)", "\\(45\\pi\\)", "\\(90\\pi\\)", "\\(180\\pi\\)"],
      correct="B",
      check="The radius is 1 metre, so the volume is pi(1)^2(45) = 45 pi cubic metres."),

 dict(n="H1-19", domain="GT", skill="GT-TR", type="MC",
      stem=("The bank of a cutting rises 4.2 metres for every 5.6 metres measured horizontally. A "
            "stone drain runs straight up the face of the bank from its foot to its top. What is "
            "the cosine of the angle the drain makes with the horizontal?"),
      choices=["0.6", "0.75", "0.8", "1.25"], correct="C",
      check="The face is the hypotenuse of a 4.2 by 5.6 right triangle, so 7 metres, and 5.6/7 = 0.8."),

 dict(n="H1-20", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A feeder stream and a spring both run into a summit pound. The feeder delivers 250 "
            "cubic metres of water an hour more than the spring does, and together they deliver 800 "
            "cubic metres an hour. How many cubic metres of water does the feeder deliver in an "
            "hour?"),
      answers=["525"],
      check="s + (s+250) = 800 gives s = 275, so the feeder delivers 525."),

 dict(n="H1-21", domain="ADV", skill="ADV-NE", type="FR",
      stem=("The volume of water, in cubic metres, held in a leaking pound t days after the leak "
            "began is modelled by \\(V(t)=5{,}400-2t^{2}-40t\\). After how many days does the model "
            "give a volume of 4,800 cubic metres?"),
      answers=["10"],
      check="2t^2 + 40t = 600 gives t^2 + 20t - 300 = 0, whose positive root is t = 10."),

 dict(n="H1-22", domain="GT", skill="GT-AV", type="FR",
      stem=("Water crosses an aqueduct along a trough 3.5 metres wide, standing 1.2 metres deep and "
            "moving at 0.5 metres per second. How many cubic metres of water cross the aqueduct in "
            "one minute?"),
      answers=["126"],
      check="3.5(1.2) = 4.2 square metres, times 0.5 gives 2.1 cubic metres a second, times 60 is 126."),
]

# ---------------------------------------------------------- Module 2 (Easy)
MODULE_2_EASY = [
 dict(n="H2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A wharf charges $45 for berthing a barge and a further $8 for each tonne unloaded from "
            "it. One barge's bill came to $165. How many tonnes were unloaded from that barge?"),
      choices=["15", "20", "21", "24"], correct="A",
      check="8t + 45 = 165 gives 8t = 120 and t = 15."),

 dict(n="H2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("At a wharf the number of loaded barges is 3 times the number of empty barges, and "
            "there are 48 barges in all. How many of them are empty?"),
      choices=["12", "16", "24", "36"], correct="A",
      check="e + 3e = 48 gives e = 12."),

 dict(n="H2E-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A barge horse walks along the towpath at a steady 4 kilometres an hour. Which equation "
            "gives the distance d, in kilometres, that the horse walks in h hours?"),
      choices=["d = 4 - h", "d = h + 4", "4d = h", "d = 4h"], correct="D",
      check="Distance is the steady speed times the time, so d = 4h."),

 dict(n="H2E-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A barge may carry no more than 26 tonnes of cargo, and 17 tonnes have already been "
            "loaded into it. Which inequality gives the possible numbers t of further tonnes that "
            "may be loaded?"),
      choices=["\\(t \\ge 9\\)", "\\(t \\le 26\\)", "\\(t \\le 9\\)", "\\(t \\le 43\\)"],
      correct="C",
      check="17 + t is at most 26, so t is at most 9."),

 dict(n="H2E-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The toll charged on a barge carrying t tonnes of cargo, in dollars, is given by "
            "C = 3t + 11. What is the toll on a barge that is carrying no cargo at all?"),
      choices=["3", "8", "11", "14"], correct="C",
      check="Setting t = 0 gives C = 11."),

 dict(n="H2E-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("The number b of barges that passed a toll house in one week satisfies 5b - 12 = 43. "
            "How many barges passed the toll house that week?"),
      choices=["8", "11", "12", "55"], correct="B",
      check="5b = 55, so b = 11."),

 dict(n="H2E-07", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("The toll on a barge carrying t tonnes of salt is 4(2t + 5) dollars, and the gauging "
            "fee on the same barge is 3t dollars. Which expression is equivalent to "
            "4(2t + 5) - 3t?"),
      choices=["5t + 20", "5t + 5", "8t + 20", "11t + 20"], correct="A",
      check="8t + 20 - 3t = 5t + 20."),

 dict(n="H2E-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The number of sacks left in a warehouse after n barges have been loaded from it is "
            "given by \\(w(n)=120-8n\\). How many sacks are left after 9 barges have been loaded?"),
      choices=["40", "48", "56", "112"], correct="B",
      check="120 - 8(9) = 120 - 72 = 48."),

 dict(n="H2E-09", domain="ADV", skill="ADV-NE", type="MC",
      stem=("Sacks of grain on a quay are stacked in a square, with the same number of sacks along "
            "each side of the square, and the stack holds 196 sacks in all. How many sacks are "
            "there along each side?"),
      choices=["14", "39", "49", "98"], correct="A",
      check="The side length is the square root of 196, which is 14."),

 dict(n="H2E-10", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A barge pays 6g dollars in toll on its gravel and 6h dollars in toll on its grain. "
            "Which expression is equivalent to 6g + 6h?"),
      choices=["6gh", "12(g + h)", "36gh", "6(g + h)"], correct="D",
      check="6 is a factor of both terms, so 6g + 6h = 6(g + h)."),

 dict(n="H2E-11", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A gang shares a load of 8t + 20 sacks equally between 4 barges. Which expression "
            "gives the number of sacks put into each barge?"),
      choices=["2t + 5", "2t + 20", "4t + 10", "8t + 5"], correct="A",
      check="(8t + 20)/4 = 2t + 5."),

 dict(n="H2E-12", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A barge is carrying 32 tonnes of cargo, and 25% of that cargo is salt. How many tonnes "
            "of salt is the barge carrying?"),
      choices=["6", "8", "12", "24"], correct="B",
      check="0.25(32) = 8."),

 dict(n="H2E-13", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The tolls collected at one toll house on the seven days of a week were, in dollars, "
            "34, 47, 12, 29, 41, 22, and 38. What is the range of these seven amounts, in dollars?"),
      choices=["29", "35", "41", "47"], correct="B",
      check="The greatest is 47 and the least is 12, so the range is 35."),

 dict(n="H2E-14", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the tolls collected at each of four toll houses in one week."
            + table(["Toll house", "Tolls collected (dollars)"],
                    [["Aldersley", "640"], ["Bratch", "815"], ["Compton", "470"],
                     ["Deepfields", "905"]])
            + "How many more dollars were collected at Bratch than at Compton?"),
      choices=["145", "235", "290", "345"], correct="D",
      check="815 - 470 = 345."),

 dict(n="H2E-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Three barges shared a cargo of 141 tonnes equally between them. How many tonnes did "
            "each barge carry?"),
      choices=["41", "47", "51", "423"], correct="B",
      check="141/3 = 47."),

 dict(n="H2E-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("Of the 60 barges tied up along a wharf, 24 are carrying grain. What fraction of those "
            "barges are carrying grain?"),
      choices=["\\(\\frac{2}{5}\\)", "\\(\\frac{5}{12}\\)", "\\(\\frac{3}{5}\\)",
               "\\(\\frac{2}{3}\\)"], correct="A",
      check="24/60 = 2/5."),

 dict(n="H2E-17", domain="GT", skill="GT-AV", type="MC",
      stem=("The hold of a barge is a rectangular box 18 metres long, 2 metres wide and 1.5 metres "
            "deep. How many cubic metres does the hold contain when it is filled level to the top?"),
      choices=["21.5", "27", "36", "54"], correct="D",
      check="18(2)(1.5) = 54."),

 dict(n="H2E-18", domain="GT", skill="GT-LA", type="MC",
      stem=("A triangular gusset plate on a barge has two sides of equal length, and the angle "
            "between those two sides measures 40&deg;. What is the measure, in degrees, of each of "
            "the plate's other two angles?"),
      choices=["40", "50", "70", "140"], correct="C",
      check="The two angles opposite the equal sides are equal, and (180 - 40)/2 = 70."),

 dict(n="H2E-19", domain="GT", skill="GT-TR", type="MC",
      stem=("A barge horse pulls on a towline that makes an angle of 20&deg; with the line of the "
            "canal, and the pull along the towline is 400 newtons. Taking "
            "\\(\\cos 20^{\\circ}=0.94\\), what is the part of that pull acting along the line of "
            "the canal, in newtons?"),
      choices=["136", "146", "376", "426"], correct="C",
      check="The component along the canal is 400 cos 20 degrees, which is 400(0.94) = 376."),

 dict(n="H2E-20", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A toll of $4 is charged for every tonne of cargo carried on a barge. The toll on one "
            "barge came to $92. How many tonnes of cargo was that barge carrying?"),
      answers=["23"],
      check="92/4 = 23."),

 dict(n="H2E-21", domain="ADV", skill="ADV-NE", type="FR",
      stem=("A chute delivers \\(4^{x}\\) sacks of grain into a barge in x minutes. After how many "
            "minutes has the chute delivered 64 sacks?"),
      answers=["3"],
      check="64 is 4 cubed, so x = 3."),

 dict(n="H2E-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A rectangular grain store on a quay measures 26 metres by 14 metres. A fence is to be "
            "built all the way round the outside of the store. How many metres of fencing does "
            "that take?"),
      answers=["80"],
      check="The perimeter is 2(26 + 14) = 80 metres."),
]

# ---------------------------------------------------------- Module 2 (Hard)
MODULE_2_HARD = [
 dict(n="H2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A toll house charges $3 a tonne on the first 20 tonnes a barge carries and $2 a tonne "
            "on every tonne it carries above 20. One barge paid $94 in toll. How many tonnes was "
            "that barge carrying?"),
      choices=["25", "31", "34", "37"], correct="D",
      check="The first 20 tonnes cost $60, and the remaining $34 buys 17 tonnes, so 20 + 17 = 37."),

 dict(n="H2H-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A tally clerk's two rules for a barge's papers give the system below.<br/>"
            "3x + 2y = 19<br/>5x - 4y = 17<br/>What is the value of x + y?"),
      choices=["3", "5", "7", "11"], correct="C",
      check="Doubling the first and adding gives 11x = 55, so x = 5, y = 2 and x + y = 7."),

 dict(n="H2H-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("Two haulage firms quote for towing the same barge. One charges $40 and a further $7 "
            "for each tonne carried; the other charges $96 and a further $3 for each tonne "
            "carried. For loads heavier than how many tonnes is the first firm's charge the "
            "greater of the two?"),
      choices=["12", "14", "18", "22"], correct="B",
      check="40 + 7t exceeds 96 + 3t when 4t > 56, that is for loads above 14 tonnes."),

 dict(n="H2H-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("What is the greatest integer value of x for which \\(5-2x \\ge 3(x-4)\\)?"),
      choices=["2", "3", "4", "17"], correct="B",
      check="5 - 2x >= 3x - 12 gives 17 >= 5x, so x is at most 3.4 and the greatest integer is 3."),

 dict(n="H2H-05", domain="ALG", skill="ALG-LE", type="MC",
      stem=("In the equation 3(2x - 5) + k = 6x + 7, k is a constant, and the equation is true for "
            "every value of x. What is the value of k?"),
      choices=["22", "27", "32", "37"], correct="A",
      check="6x - 15 + k = 6x + 7 for every x only when k - 15 = 7, so k = 22."),

 dict(n="H2H-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The draught of a barge rises steadily with the load it carries: an empty barge of one "
            "class draws 46 centimetres, and every 5 tonnes loaded into it adds a further 3 "
            "centimetres. Which expression gives the load, in tonnes, of a barge of that class "
            "drawing d centimetres?"),
      choices=["\\(\\frac{3(d-46)}{5}\\)", "\\(\\frac{5d-46}{3}\\)", "\\(\\frac{d-46}{15}\\)",
               "\\(\\frac{5(d-46)}{3}\\)"], correct="D",
      check="d = 46 + (3/5)L, so L = 5(d-46)/3."),

 dict(n="H2H-07", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The functions f and g are defined by \\(f(x)=\\frac{x+5}{2}\\) and g(x) = 4x - 3. "
            "Which expression is equivalent to f(g(x))?"),
      choices=["2x + 1", "2x - 1", "4x + 1", "\\(\\frac{4x+5}{2}\\)"], correct="A",
      check="f(4x-3) = (4x-3+5)/2 = (4x+2)/2 = 2x + 1."),

 dict(n="H2H-08", domain="ADV", skill="ADV-NE", type="MC",
      stem=("In a toll clerk's gauging rule the positive number x satisfies "
            "\\(x+\\frac{1}{x}=5\\). What is the value of \\(x^{2}+\\frac{1}{x^{2}}\\)?"),
      choices=["21", "23", "25", "27"], correct="B",
      check="Squaring gives x^2 + 2 + 1/x^2 = 25, so x^2 + 1/x^2 = 23."),

 dict(n="H2H-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A tender divides a total charge of \\(6x^{2}-x-15\\) dollars equally among 2x + 3 "
            "barges, where \\(2x+3 \\ne 0\\). Which expression gives the charge, in dollars, for "
            "each barge?"),
      choices=["2x - 5", "3x + 5", "3x - 5", "\\(3x^{2}-5\\)"], correct="C",
      check="6x^2 - x - 15 factors as (2x+3)(3x-5), so the quotient is 3x - 5."),

 dict(n="H2H-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The mass of grain left in a warehouse t weeks after a stoppage on the canal is "
            "modelled by \\(M(t)=M_{0}(0.85)^{t}\\), where \\(M_{0}\\) is the mass held when the "
            "stoppage began. By what percentage does this model say the mass falls over any period "
            "of 2 weeks?"),
      choices=["15", "27.75", "30", "32.5"], correct="B",
      check="0.85 squared is 0.7225, a fall of 0.2775, or 27.75%, whatever the starting mass."),

 dict(n="H2H-11", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to \\(\\frac{1}{u}-\\frac{1}{v}\\), where u and v are "
            "positive?"),
      choices=["\\(\\frac{u-v}{uv}\\)", "\\(\\frac{1}{u-v}\\)", "\\(\\frac{u+v}{uv}\\)",
               "\\(\\frac{v-u}{uv}\\)"], correct="D",
      check="Over the common denominator uv the numerators are v and u, giving (v-u)/(uv)."),

 dict(n="H2H-12", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A wharf clerk gauged a random sample of 80 of the 1,200 barges that used the wharf in "
            "one season and found 18 of them loaded above the permitted limit. Which of the "
            "following is the most appropriate estimate of the number of those 1,200 barges that "
            "were loaded above the limit?"),
      choices=["18", "108", "270", "480"], correct="C",
      check="18 of 80 is 0.225, and 0.225(1,200) = 270."),

 dict(n="H2H-13", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Working at the same steady rate as one another, 4 gangs unload 6 barges in 9 hours. At "
            "that rate, how many hours would 6 gangs take to unload 10 barges?"),
      choices=["6", "7.5", "9", "10"], correct="D",
      check="6 barges take 36 gang-hours, so 6 gang-hours each; 10 barges need 60, and 60/6 = 10 hours."),

 dict(n="H2H-14", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of barges gauged at two toll houses in one week, by the "
            "cargo each was carrying."
            + table(["Cargo", "Hatton toll house", "Napton toll house"],
                    [["Salt", "24", "16"], ["Grain", "45", "30"], ["Gravel", "31", "54"]])
            + "What percentage of the barges carrying grain were gauged at Hatton toll house?"),
      choices=["45", "60", "75", "80"], correct="B",
      check="45 of the 75 barges carrying grain were gauged at Hatton, and 45/75 = 0.60."),

 dict(n="H2H-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A barge's cargo is 40% salt by mass. After a further 6 tonnes of gravel are loaded "
            "into the same barge, the salt is 25% of the cargo by mass. What was the mass of the "
            "cargo, in tonnes, before the gravel was loaded?"),
      choices=["4", "8", "10", "15"], correct="C",
      check="0.40m = 0.25(m+6) gives 0.15m = 1.5 and m = 10."),

 dict(n="H2H-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The table gives the tonnage entered against each of the 20 barges gauged at a toll "
            "house in one day."
            + table(["Tonnage entered", "Barges"],
                    [["12", "4"], ["15", "7"], ["18", "6"], ["20", "3"]])
            + "What is the median of the 20 tonnages?"),
      choices=["15", "16.5", "18", "20"], correct="A",
      check="The 10th and 11th of the 20 values in order are both 15, so the median is 15."),

 dict(n="H2H-17", domain="GT", skill="GT-AV", type="MC",
      stem=("Two hoppers used for gravel at a wharf are similar in shape, and the larger hopper is "
            "1.5 times as tall as the smaller. The smaller hopper holds 96 cubic metres. How many "
            "cubic metres does the larger hopper hold?"),
      choices=["144", "216", "324", "432"], correct="C",
      check="Volumes of similar solids scale by 1.5 cubed = 3.375, and 96(3.375) = 324."),

 dict(n="H2H-18", domain="GT", skill="GT-LA", type="MC",
      stem=("A winding hole, the widened place in a canal where a barge is turned round, is a "
            "circle of area \\(400\\pi\\) square metres. By how many metres is the diameter of the "
            "winding hole greater than the length of a barge 21 metres long?"),
      choices=["9", "19", "29", "39"], correct="B",
      check="The radius is 20 metres, so the diameter is 40 and 40 - 21 = 19."),

 dict(n="H2H-19", domain="GT", skill="GT-TR", type="MC",
      stem=("In right triangle ABC the right angle is at B, and \\(\\sin A=\\frac{5}{13}\\). What "
            "is the value of \\(\\tan C\\)?"),
      choices=["\\(\\frac{5}{13}\\)", "\\(\\frac{5}{12}\\)", "\\(\\frac{13}{5}\\)",
               "\\(\\frac{12}{5}\\)"], correct="D",
      check="With BC = 5k and AC = 13k, AB = 12k, and tan C = AB/BC = 12/5."),

 dict(n="H2H-20", domain="ALG", skill="ALG-LE", type="FR",
      stem=("The toll, in dollars, on a barge carrying a load of L tonnes is given by "
            "\\(T=\\frac{5(L+8)}{4}\\). What load, in tonnes, is charged a toll of $60?"),
      answers=["40"],
      check="5(L+8) = 240 gives L + 8 = 48 and L = 40."),

 dict(n="H2H-21", domain="ADV", skill="ADV-NE", type="FR",
      stem=("In a gauging rule the positive numbers x and y satisfy \\(x^{2}+y^{2}=58\\) and "
            "xy = 21. What is the value of x + y?"),
      answers=["10"],
      check="(x+y)^2 = x^2 + y^2 + 2xy = 58 + 42 = 100, and x + y is positive, so it is 10."),

 dict(n="H2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("Two cylindrical hoppers on a wharf hold the same volume of gravel when full. The "
            "first has a base of radius 2 metres and a height of 9 metres, and the second has a "
            "base of radius 3 metres. What is the height of the second hopper, in metres?"),
      answers=["4"],
      check="pi(4)(9) = pi(9)h gives h = 4."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
