#!/usr/bin/env python3
"""
Original Math content for Test 8 — all three modules, 66 questions.

Difficulty, per the request to raise Module 1 and Module 2 (Hard):

  MODULE_1     upper-medium. Two-to-three step setups, a rearrangement before
               the arithmetic, or a constant to solve for. Harder than Test 7's
               Module 1, but still the routing module: it has to separate
               students, so it stays below Module 2 (Hard).
  MODULE_2_EASY genuinely easy — the lower branch of the adaptive split.
  MODULE_2_HARD hard. Parameters rather than numbers, structural answers,
               composed functions, systems with a condition on a constant,
               and geometry needing two relationships at once.

House style follows Test 1/2 (see CLAUDE.md). LaTeX typed by hand.
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
 dict(n="A1-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("\\[5(x-3)-2(x+4)=13\\]What is the solution to the given equation?"),
      choices=["4", "8", "12", "18"], correct="C",
      check="5x-15-2x-8 = 3x-23 = 13, so 3x = 36 and x = 12."),

 dict(n="A1-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A shop sells notebooks at x dollars each and pens at y dollars each. Three notebooks "
            "and four pens cost $25 in total, and five notebooks cost $7 more than two pens. What "
            "is the cost, in dollars, of two notebooks and one pen?"),
      choices=["8", "10", "12", "14"], correct="B",
      check="3x+4y=25 and 5x-2y=7 give x = 3 and y = 4, so 2x + y = 10."),

 dict(n="A1-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A line passes through \\((-2, 7)\\) and \\((4, -5)\\). At what value of x does the "
            "line cross the x-axis?"),
      choices=["\\(\\frac{3}{2}\\)", "2", "\\(\\frac{5}{2}\\)", "3"], correct="A",
      check="Slope -2, y = -2x + 3, so x-intercept at x = 3/2."),

 dict(n="A1-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A delivery van weighs 1,850 kilograms empty and may not exceed a total mass of "
            "3,200 kilograms. Each crate loaded onto the van has a mass of 45 kilograms. What is "
            "the greatest number of crates the van can carry?"),
      choices=["28", "29", "30", "31"], correct="C",
      check="45c <= 1350 gives c <= 30."),

 dict(n="A1-05", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A recipe is written twice on a card. The first version reads \\(ax+7y=21\\) and "
            "the second reads \\(6x+14y=42\\), where a is a constant, x is the mass of flour "
            "and y the mass of sugar. If the two versions place no different requirement on x "
            "and y at all, what is the value of a?"),
      choices=["2", "3", "6", "7"], correct="B",
      check="Halving the second gives 3x+7y=21, so a = 3."),

 dict(n="A1-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The function f is linear. If \\(f(3)=8\\) and \\(f(7)=20\\), what is the value of "
            "\\(f(0)\\)?"),
      choices=["-4", "-1", "2", "5"], correct="B",
      check="Slope 3; f(0) = 8 - 3(3) = -1."),

 dict(n="A1-07", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A cyclist rides for 2 hours at one constant speed and then for 3 hours at a speed "
            "8 kilometres per hour slower. The total distance is 156 kilometres. What was the "
            "faster speed, in kilometres per hour?"),
      choices=["30", "34", "36", "40"], correct="C",
      check="2s + 3(s-8) = 156 gives 5s = 180 and s = 36."),

 dict(n="A1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A large square has side \\(3x-2\\) units and a small square has side "
            "\\(x+5\\) units. Which expression gives how much greater the area of the large "
            "square is than that of the small square?"),
      choices=["\\(8x^{2}-22x-21\\)", "\\(8x^{2}-2x-21\\)", "\\(10x^{2}-22x+29\\)",
               "\\(8x^{2}-22x+29\\)"], correct="A",
      check="(3x-2)^2 - (x+5)^2 = 8x^2 - 22x - 21."),

 dict(n="A1-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A farmer's yield, in tonnes, from applying x units of fertiliser is modelled by "
            "\\(Y(x)=-2x^{2}+16x-27\\). What is the greatest yield the model predicts?"),
      choices=["4", "5", "8", "27"], correct="B",
      check="Vertex at x = 4; Y(4) = -32 + 64 - 27 = 5."),

 dict(n="A1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A file is compressed so that its size is \\(4^{2x-1}\\) kilobytes. The compressed "
            "file is 64 kilobytes. What is the value of x?"),
      choices=["1", "2", "\\(\\frac{5}{2}\\)", "3"], correct="B",
      check="64 = 4^3, so 2x-1 = 3 and x = 2."),

 dict(n="A1-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The solutions to \\(2x^{2}-9x-5=0\\) are p and q, with \\(p>q\\). What is the value "
            "of \\(p-q\\)?"),
      choices=["\\(\\frac{9}{2}\\)", "5", "\\(\\frac{11}{2}\\)", "\\(\\frac{21}{4}\\)"], correct="C",
      check="Roots 5 and -1/2, so p - q = 11/2."),

 dict(n="A1-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A rectangle has an area of \\(x^{2}-x-12\\) square units and a width of "
            "\\(x+3\\) units. Which expression represents its length, in units, for "
            "\\(x>4\\)?"),
      choices=["\\(x-4\\)", "\\(x+4\\)", "\\(x-3\\)", "\\(x-12\\)"], correct="A",
      check="(x^2-x-12)/(x+3) = (x-4)(x+3)/(x+3) = x-4."),

 dict(n="A1-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A projectile is launched so that its height, in metres, after t seconds is "
            "\\(h(t)=-4.9t^{2}+29.4t\\). For how many seconds is the projectile in the air "
            "before it returns to the ground?"),
      choices=["3", "4.9", "6", "29.4"], correct="C",
      check="-4.9t(t-6) = 0 gives t = 0 or t = 6."),

 dict(n="A1-14", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A sample of a radioactive isotope halves in mass every 12 years. A laboratory "
            "records a mass of 40 grams today. Which function gives the mass, \\(M(y)\\), in "
            "grams, y years from today?"),
      choices=["\\(M(y)=40\\left(\\frac{1}{2}\\right)^{12y}\\)",
               "\\(M(y)=40\\left(\\frac{1}{2}\\right)^{\\frac{y}{12}}\\)",
               "\\(M(y)=40\\left(\\frac{1}{12}\\right)^{\\frac{y}{2}}\\)",
               "\\(M(y)=40-\\frac{y}{12}\\)"], correct="B",
      check="Halving every 12 years puts y/12 in the exponent."),

 dict(n="A1-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A map is drawn to a scale of 1 centimetre to 2.5 kilometres. Two towns are 17.4 "
            "centimetres apart on the map. A road between them is 12 kilometres longer than the "
            "straight-line distance. How long, in kilometres, is the road?"),
      choices=["43.5", "51.0", "55.5", "58.5"], correct="C",
      check="17.4 * 2.5 = 43.5, plus 12 gives 55.5."),

 dict(n="A1-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("After a 12% increase, the price of a season ticket is $728. What was the price, in "
            "dollars, before the increase?"),
      choices=["$616", "$640", "$650", "$684"], correct="C",
      check="728 / 1.12 = 650."),

 dict(n="A1-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table shows the distribution of scores on a 10-point quiz taken by 25 students."
            + table(["Score", "Number of students"],
                    [["6", "3"], ["7", "5"], ["8", "9"], ["9", "6"], ["10", "2"]])
            + "What is the mean score, to the nearest hundredth?"),
      choices=["7.96", "8.00", "8.16", "8.24"], correct="A",
      check="(18+35+72+54+20)/25 = 199/25 = 7.96."),

 dict(n="A1-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A jar holds 9 white counters and 6 black counters. Two counters are drawn at random "
            "without replacement. What is the probability that both are black?"),
      choices=["\\(\\frac{1}{7}\\)", "\\(\\frac{2}{15}\\)", "\\(\\frac{4}{25}\\)",
               "\\(\\frac{3}{14}\\)"], correct="A",
      check="(6/15)(5/14) = 30/210 = 1/7."),

 dict(n="A1-19", domain="GT", skill="GT-LA", type="MC",
      stem=("Two similar triangles have areas of 45 and 125 square centimetres. The shortest "
            "side of the smaller triangle is 6 centimetres. What is the length, in centimetres, "
            "of the shortest side of the larger triangle?"),
      choices=["8", "10", "12", "15"], correct="B",
      check="Area ratio 45:125 = 9:25, so side ratio 3:5 and 6(5/3) = 10."),

 dict(n="A1-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A cone and a cylinder have the same radius and the same height. The volume of the "
            "cylinder is 96 cubic centimetres. What is the volume, in cubic centimetres, of the "
            "cone?"),
      answers=["32"],
      check="A cone is one third of the cylinder: 96/3 = 32."),

 dict(n="A1-21", domain="ADV", skill="ADV-NE", type="FR",
      stem=("\\[x^{2}+kx+36=0\\]In the given equation, k is a negative constant. If the equation "
            "has exactly one real solution, what is the value of \\(|k|\\)?"),
      answers=["12"],
      check="Discriminant k^2 - 144 = 0 gives k = -12, so |k| = 12."),

 dict(n="A1-22", domain="GT", skill="GT-TR", type="FR",
      stem=("A ladder leans against a wall so that its foot is 7 metres from the base of the "
            "wall and its top touches the wall 24 metres above the ground. How many metres long "
            "is the ladder?"),
      answers=["25"],
      check="sqrt(49+576) = sqrt(625) = 25."),
]


# ------------------------------------------------------------ Module 2 Easy
MODULE_2_EASY = [
 dict(n="A2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A theatre had some people seated. After 9 more people arrived, there were 23 people "
            "seated. How many people were seated before the 9 arrived?"),
      choices=["12", "14", "23", "32"], correct="B", check="x + 9 = 23 gives x = 14."),

 dict(n="A2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("Six identical crates have a combined mass of 54 kilograms. What is the mass, in "
            "kilograms, of one crate?"),
      choices=["6", "8", "9", "48"], correct="C", check="54/6 = 9."),

 dict(n="A2E-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A shop sells pens for $3 each. Which equation gives the total cost C, in dollars, "
            "of p pens?"),
      choices=["\\(C=3+p\\)", "\\(C=3p\\)", "\\(C=p-3\\)", "\\(C=\\frac{p}{3}\\)"], correct="B",
      check="Three dollars per pen."),

 dict(n="A2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A plumber charges a $5 call-out fee plus $2 for each minute on site. What is the "
            "total charge, in dollars, for a 4-minute visit?"),
      choices=["9", "11", "13", "14"], correct="C", check="5 + 2(4) = 13."),

 dict(n="A2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem="Which value of x satisfies \\(x+4<9\\)?",
      choices=["4", "5", "9", "13"], correct="A", check="x < 5, and only 4 qualifies."),

 dict(n="A2E-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A rope 48 centimetres long is cut into 6 equal pieces. How long, in centimetres, is "
            "each piece?"),
      choices=["6", "8", "12", "42"], correct="B", check="48/6 = 8."),

 dict(n="A2E-07", domain="ALG", skill="ALG-LF", type="MC",
      stem="What is the slope of the line \\(y=7x-2\\)?",
      choices=["-2", "2", "5", "7"], correct="D", check="Slope is the coefficient of x."),

 dict(n="A2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A square tile has a side length of \\(x+3\\) centimetres. What is the perimeter "
            "of the tile, in centimetres?"),
      choices=["\\(4x+3\\)", "\\(4x+7\\)", "\\(4x+12\\)", "\\(x+12\\)"], correct="C",
      check="4(x+3) = 4x + 12."),

 dict(n="A2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A storage box has a square base of side \\(x^{2}\\) units and a height of "
            "\\(x^{3}\\) units. Which expression gives its volume, in cubic units, for "
            "\\(x>0\\)?"),
      choices=["\\(x^{7}\\)", "\\(x^{12}\\)", "\\(2x^{7}\\)", "\\(x^{5}\\)"], correct="A",
      check="x^2 * x^2 * x^3 = x^7."),

 dict(n="A2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A gardener models the number of blooms on a shrub as \\(B(w)=w^{2}-6\\), where w "
            "is the number of weeks since planting. How many blooms does the model predict after "
            "5 weeks?"),
      choices=["4", "16", "19", "25"], correct="C", check="25 - 6 = 19."),

 dict(n="A2E-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A square patio has an area of 49 square metres. What is the length, in metres, of "
            "one side?"),
      choices=["6", "7", "24.5", "98"], correct="B", check="sqrt(49) = 7."),

 dict(n="A2E-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("Two square rugs have areas of 81 and 16 square metres. What is the combined length, "
            "in metres, of one side of each rug?"),
      choices=["11", "13", "97", "25"], correct="B", check="9 + 4 = 13."),

 dict(n="A2E-13", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A rectangular sheet has an area of \\(10x^{4}\\) square units and a width of "
            "\\(2x\\) units. What is its length, in units, for \\(x>0\\)?"),
      choices=["\\(5x^{3}\\)", "\\(5x^{4}\\)", "\\(8x^{3}\\)", "\\(20x^{3}\\)"], correct="A",
      check="10x^4 / 2x = 5x^3."),

 dict(n="A2E-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem="What is 30% of 260?",
      choices=["68", "72", "78", "86"], correct="C", check="0.30 * 260 = 78."),

 dict(n="A2E-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A car uses 6 litres of fuel to travel 90 kilometres. At the same rate, how many "
            "litres are needed to travel 240 kilometres?"),
      choices=["12", "14", "16", "18"], correct="C", check="240/90 * 6 = 16."),

 dict(n="A2E-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem="What is the mean of 12, 15, 18, 19 and 26?",
      choices=["17", "18", "19", "20"], correct="B", check="90/5 = 18."),

 dict(n="A2E-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table shows the number of visitors to a museum on three days."
            + table(["Day", "Visitors"], [["Friday", "220"], ["Saturday", "410"], ["Sunday", "365"]])
            + "How many more visitors came on Saturday than on Friday?"),
      choices=["145", "165", "190", "215"], correct="C", check="410 - 220 = 190."),

 dict(n="A2E-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A bag holds 4 red and 6 yellow tokens. One token is drawn at random. What is the "
            "probability that it is red?"),
      choices=["\\(\\frac{2}{5}\\)", "\\(\\frac{3}{5}\\)", "\\(\\frac{2}{3}\\)",
               "\\(\\frac{1}{4}\\)"], correct="A", check="4/10 = 2/5."),

 dict(n="A2E-19", domain="GT", skill="GT-LA", type="MC",
      stem=("A triangular sail has two corners measuring 55&deg; and 65&deg;. What is the "
            "measure, in degrees, of the third corner?"),
      choices=["50", "60", "70", "120"], correct="B", check="180 - 120 = 60."),

 dict(n="A2E-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A rectangle has a length of 14 centimetres and a width of 9 centimetres. What is "
            "its area, in square centimetres?"),
      answers=["126"], check="14 * 9 = 126."),

 dict(n="A2E-21", domain="GT", skill="GT-AV", type="FR",
      stem="A circle has a radius of 7 units. What is its circumference, in terms of \\(\\pi\\)? "
           "(Enter the coefficient of \\(\\pi\\).)",
      answers=["14"], check="C = 2 pi r = 14 pi."),

 dict(n="A2E-22", domain="GT", skill="GT-TR", type="FR",
      stem=("In right triangle JKL, angle L is a right angle, \\(JL=6\\) and \\(KL=8\\). What is "
            "the length of JK?"),
      answers=["10"], check="sqrt(36+64) = 10."),
]


# ------------------------------------------------------------ Module 2 Hard
MODULE_2_HARD = [
 dict(n="A2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("\\[px+qy=14\\]\\[3x+2y=7\\]In the given system, p and q are constants. If the system "
            "has no solution, which of the following must be true?"),
      choices=["\\(2p=3q\\)", "\\(2p-3q=0\\) and \\(p\\ne 6\\)", "\\(p=6\\) and \\(q=4\\)",
               "\\(3p=2q\\)"], correct="B",
      check="Parallel needs p/3 = q/2, i.e. 2p = 3q; p = 6 would also match the constants and give infinitely many solutions, so p != 6."),

 dict(n="A2H-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("Line m has equation \\(4x-3y=12\\). Line n is perpendicular to m and passes through "
            "the point \\((8, -1)\\). What is the y-intercept of line n?"),
      choices=["-7", "3", "5", "9"], correct="C",
      check="m has slope 4/3, so n has slope -3/4; -1 = -3/4(8) + b gives b = 5."),

 dict(n="A2H-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A worker earns $16 per hour for the first 38 hours in a week and $24 per hour for "
            "each additional hour. In a week when the worker earned at least $704, what is the "
            "least number of hours worked?"),
      choices=["40", "42", "44", "46"], correct="B",
      check="16(38) = 608, and 608 + 24e >= 704 needs e >= 4, so 38 + 4 = 42 hours."),

 dict(n="A2H-04", domain="ADV", skill="ADV-NE", type="MC",
      stem=("\\[3x^{2}+bx+12=0\\]In the given equation, b is a constant. For how many values of b "
            "does the equation have exactly one real solution?"),
      choices=["Zero", "Exactly one", "Exactly two", "Infinitely many"], correct="C",
      check="b^2 = 144 gives b = 12 and b = -12, so exactly two."),

 dict(n="A2H-05", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A parabola has its vertex at \\((4, 7)\\) and passes through \\((2, 19)\\). "
            "What is the y-coordinate of the point on the parabola whose x-coordinate is 8?"),
      choices=["31", "43", "55", "67"], correct="C",
      check="y = a(x-4)^2 + 7 with 4a + 7 = 19 gives a = 3, so y = 3(16) + 7 = 55."),

 dict(n="A2H-06", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("The table gives values of the function f."
            + table(["x", "1", "2", "3", "4"], [["f(x)", "5", "8", "11", "14"]])
            + "The function g is defined by \\(g(x)=x^{2}+2\\). What is the value of "
              "\\(g(f(3))\\)?"),
      choices=["26", "38", "64", "123"], correct="D",
      check="f(3) = 11 from the table, and g(11) = 121 + 2 = 123."),

 dict(n="A2H-07", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A support wire of length \\(x+1\\) metres is replaced by one of length "
            "\\(\\sqrt{3x+13}\\) metres, and the two lengths turn out to be equal. Given "
            "that the length is positive, what is the value of x?"),
      choices=["-4", "-1", "3", "4"], correct="D",
      check="3x+13 = (x+1)^2 gives x^2-x-12 = 0, roots 4 and -3; only 4 keeps the length positive."),

 dict(n="A2H-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A cube has a volume of \\(\\frac{8x^{9}}{27}\\) cubic units, where "
            "\\(x>0\\). What is the area, in square units, of one of its faces?"),
      choices=["\\(\\frac{4x^{6}}{9}\\)", "\\(\\frac{4x^{6}}{27}\\)",
               "\\(\\frac{16x^{6}}{9}\\)", "\\(\\frac{4x^{27}}{9}\\)"], correct="A",
      check="Side = (8x^9/27)^(1/3) = 2x^3/3, and its square is 4x^6/9."),

 dict(n="A2H-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A biologist models a population as \\(P(t)=k\\left(\\frac{3}{2}\\right)^{t}\\), "
            "where t is measured in years and k is a constant. The population two years from now "
            "will exceed today's population by 25. What is the value of k?"),
      choices=["16", "20", "25", "36"], correct="B",
      check="k(9/4 - 1) = 5k/4 = 25 gives k = 20."),

 dict(n="A2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A circular running track is described in the xy-plane by "
            "\\[x^{2}+y^{2}-10x+8y=-16\\]with distances measured in metres. How many metres "
            "apart are the two points of the track that are farthest from each other?"),
      choices=["5", "8", "10", "\\(2\\sqrt{41}\\)"], correct="C",
      check="(x-5)^2+(y+4)^2 = 25, so r = 5 and the greatest separation is the diameter, 10."),

 dict(n="A2H-11", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A chemist mixes a 15% saline solution with a 40% saline solution to obtain 20 litres "
            "of a 24% solution. How many litres of the 40% solution are used?"),
      choices=["6.4", "7.2", "8.0", "12.8"], correct="B",
      check="0.15(20-v) + 0.40v = 0.24(20) gives 3 + 0.25v = 4.8, v = 7.2."),

 dict(n="A2H-12", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A data set of 12 values has a mean of 31. Two values, 18 and 24, are removed. What "
            "is the mean of the remaining 10 values?"),
      choices=["32.0", "33.0", "34.0", "35.0"], correct="B",
      check="(372 - 42)/10 = 330/10 = 33."),

 dict(n="A2H-13", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A survey of 480 commuters is summarised below."
            + table(["", "Drives", "Takes transit", "Total"],
                    [["Under 30", "84", "156", "240"],
                     ["30 or over", "138", "102", "240"],
                     ["Total", "222", "258", "480"]])
            + "A commuter who takes transit is selected at random. What is the probability that "
              "the commuter is under 30?"),
      choices=["\\(\\frac{13}{40}\\)", "\\(\\frac{26}{43}\\)", "\\(\\frac{13}{20}\\)",
               "\\(\\frac{17}{43}\\)"], correct="B",
      check="156/258 = 26/43."),

 dict(n="A2H-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A solution's concentration falls by 15% in the first hour and by a further 20% in "
            "the second hour. By what percent has the concentration fallen overall?"),
      choices=["31%", "32%", "35%", "37%"], correct="B",
      check="0.85 * 0.80 = 0.68, a fall of 32%."),

 dict(n="A2H-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("A researcher reports the mean of 25 measurements as 14.8. A 26th measurement is then "
            "added, and the mean of all 26 becomes 15.0. What is the 26th measurement?"),
      choices=["18.0", "19.0", "20.0", "21.0"], correct="C",
      check="26(15.0) - 25(14.8) = 390 - 370 = 20."),

 dict(n="A2H-16", domain="GT", skill="GT-LA", type="MC",
      stem=("In triangle PQR, \\(PQ=15\\), \\(PR=20\\) and the measure of angle P is 90&deg;. "
            "Point S lies on QR so that PS is perpendicular to QR. What is the length of PS?"),
      choices=["10", "12", "\\(\\frac{60}{7}\\)", "16"], correct="B",
      check="QR = 25; area = (15*20)/2 = 150 = (25*PS)/2, so PS = 12."),

 dict(n="A2H-17", domain="GT", skill="GT-AV", type="MC",
      stem=("A sphere has the same volume as a cylinder of radius 4 and height 18. What is the "
            "radius of the sphere?"),
      choices=["4", "5", "6", "9"], correct="C",
      check="Cylinder is 288pi; (4/3)pi r^3 = 288pi gives r^3 = 216 and r = 6."),

 dict(n="A2H-18", domain="GT", skill="GT-TR", type="MC",
      stem=("In a right triangle, \\(\\cos x^{\\circ}=\\frac{8}{17}\\). What is the value of "
            "\\(\\sin x^{\\circ}\\)?"),
      choices=["\\(\\frac{15}{17}\\)", "\\(\\frac{8}{15}\\)", "\\(\\frac{15}{8}\\)",
               "\\(\\frac{17}{15}\\)"], correct="A",
      check="Opposite = sqrt(289-64) = 15, so sin = 15/17."),

 dict(n="A2H-19", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The function f is linear and satisfies \\(f(x+4)-f(x)=18\\) for all x. If "
            "\\(f(1)=5\\), what is the value of \\(f(9)\\)?"),
      choices=["23", "36", "41", "45"], correct="C",
      check="Slope = 18/4 = 4.5; f(9) = 5 + 4.5(8) = 41."),

 dict(n="A2H-20", domain="ADV", skill="ADV-NE", type="FR",
      stem=("A rectangle's length and width, in centimetres, are the two solutions of "
            "\\(3x^{2}-14x+8=0\\). What is the area of the rectangle, in square centimetres? "
            "(Express your answer as a fraction or a decimal.)"),
      answers=["8/3"],
      check="Area is the product of the roots, c/a = 8/3."),

 dict(n="A2H-21", domain="ALG", skill="ALG-LE", type="FR",
      stem=("At a fundraiser, tickets cost $12 for adults and $7 for children. A total of 260 "
            "tickets were sold for $2,470. How many child tickets were sold?"),
      answers=["130"],
      check="12a + 7(260-a) = 2470 gives 5a + 1820 = 2470, a = 130, so children = 130."),

 dict(n="A2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A conical paper cup has a radius of 6 centimetres and holds \\(96\\pi\\) cubic "
            "centimetres of water when full. How deep, in centimetres, is the cup?"),
      answers=["8"],
      check="(1/3)pi(36)h = 96pi gives 12h = 96 and h = 8."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
