# CALC 6.1 Exploring Accumulations of Change — 25 questions
# Answers verified with sympy; see verify_c6_1.py.
# Questions 1, 2, 6, 12, 16, 20, 22, 25 are conceptual (units, interpretation,
# misconception) and carry no sympy computation; they are listed as CONCEPTUAL
# in the verifier and their reasoning was checked by hand.
TOPIC = ("6.1", "Exploring Accumulations of Change", 6)
QUESTIONS = [
 dict(q="Water flows into a tank at a rate of R(t) gallons per minute, where t is measured in minutes. What does int from 0 to 20 of R(t) dt represent?", choices=[
   "the flow rate at the instant t = 20",
   "the number of gallons that flow into the tank during the first 20 minutes",
   "the average flow rate over the first 20 minutes",
   "the change in the flow rate between t = 0 and t = 20"], ans=1,
   why="Integrating a rate of change over an interval accumulates the total change in the quantity, so the units are (gallons per minute)(minutes) = gallons."),
 dict(q="A population changes at a rate of P'(t) people per year, where t is in years. What are the units of int from 2 to 5 of P'(t) dt?", choices=[
   "people per year",
   "people",
   "people per year squared",
   "years"], ans=1,
   why="The integral multiplies a rate in people per year by a width in years, so the units of people per year cancel down to people."),
 dict(q="A pump moves water at the constant rate of 7 gallons per minute for 15 minutes. How much water does it move?", choices=[
   "2.14 gallons",
   "22 gallons",
   "105 gallons",
   "210 gallons"], ans=2,
   why="With a constant rate the accumulation is a rectangle of height 7 and width 15, so 7(15) = 105 gallons."),
 dict(q="A car starts from rest and its velocity is v(t) = 4t feet per second for 0 <= t <= 6. How far does it travel during these 6 seconds?", choices=[
   "24 feet",
   "72 feet",
   "144 feet",
   "216 feet"], ans=1,
   why="The region under v is a triangle with base 6 and height v(6) = 24, so the distance is (1/2)(6)(24) = 72 feet."),
 dict(q="A machine produces bolts at a rate of 6 bolts per minute for 0 <= t <= 4 and is shut off, producing nothing, for 4 < t <= 9. How many bolts are produced during the first 9 minutes?", choices=[
   "6 bolts",
   "24 bolts",
   "30 bolts",
   "54 bolts"], ans=1,
   why="Only the first 4 minutes contribute, giving 6(4) = 24 bolts; the rate is 0 afterward, so that stretch adds no area."),
 dict(q="The volume of liquid in a vat is decreasing at a constant rate of 3 liters per minute for 8 minutes. What is the change in the volume over those 8 minutes?", choices=[
   "-24 liters",
   "-11 liters",
   "11 liters",
   "24 liters"], ans=0,
   why="A decreasing quantity has a negative rate, so the accumulated change is (-3)(8) = -24 liters."),
 dict(q="A particle moves along a line with velocity v(t) = 12 - 3t meters per second. What is the particle's displacement from t = 0 to t = 4?", choices=[
   "0 meters",
   "12 meters",
   "24 meters",
   "48 meters"], ans=2,
   why="On [0, 4] the graph of v is a triangle with base 4 and height 12, and v >= 0 throughout, so the displacement is (1/2)(4)(12) = 24 meters."),
 dict(q="A particle has velocity v(t) = 12 - 3t meters per second. What is its displacement from t = 0 to t = 6?", choices=[
   "6 meters",
   "18 meters",
   "24 meters",
   "30 meters"], ans=1,
   why="The area above the axis on [0, 4] is 24 and the area below the axis on [4, 6] is 6, and displacement counts the second one as negative: 24 - 6 = 18 meters."),
 dict(q="An object moves with velocity v(t) = 2t - 8 feet per second. What total distance does it travel from t = 0 to t = 6?", choices=[
   "4 feet",
   "12 feet",
   "16 feet",
   "20 feet"], ans=3,
   why="Distance adds the areas without regard to sign: 16 units of area below the axis on [0, 4] plus 4 units above it on [4, 6] gives 20 feet."),
 dict(q="A chemical is produced at a rate that increases linearly from 2 grams per hour at t = 0 to 10 grams per hour at t = 4. How many grams are produced during these 4 hours?", choices=[
   "8 grams",
   "20 grams",
   "24 grams",
   "48 grams"], ans=2,
   why="The region under a linear rate is a trapezoid, with area ((2 + 10)/2)(4) = 24 grams."),
 dict(q="The depth of water in a well changes at a rate of h'(t) centimeters per hour, and int from 0 to 6 of h'(t) dt = -15. Which statement must be true?", choices=[
   "The depth after 6 hours is 15 centimeters.",
   "The depth decreased by a total of 15 centimeters over the 6 hours.",
   "The depth was decreasing at 15 centimeters per hour.",
   "The depth decreased by 15 centimeters during each of the 6 hours."], ans=1,
   why="The definite integral of a rate gives the net change, so the depth ended 15 centimeters lower than it started; nothing is claimed about the starting depth or the rate at any instant."),
 dict(q="A rate function f satisfies f(t) <= 0 for all t in [a, b], with a < b. What can be concluded about the accumulated change int from a to b of f(t) dt?", choices=[
   "It is positive.",
   "It is negative or zero.",
   "It is zero.",
   "Its sign cannot be determined."], ans=1,
   why="All of the area lies on or below the horizontal axis, so the signed area, and therefore the accumulated change, is at most zero."),
 dict(q="A quantity Q satisfies Q(0) = 50, and int from 0 to 4 of Q'(t) dt = 18. What is Q(4)?", choices=[
   "18",
   "32",
   "68",
   "72"], ans=2,
   why="The integral of the rate gives the change, so Q(4) = Q(0) + 18 = 50 + 18 = 68."),
 dict(q="A bacteria colony grows at a rate of 200 cells per hour during the first 3 hours and 500 cells per hour during the next 2 hours. By how many cells does the colony grow in these 5 hours?", choices=[
   "700 cells",
   "1000 cells",
   "1600 cells",
   "3500 cells"], ans=2,
   why="The accumulation is the sum of two rectangles, 200(3) + 500(2) = 600 + 1000 = 1600 cells."),
 dict(q="A car is driven at 50 miles per hour for 2 hours and then at 30 miles per hour for 1 hour. How far does it travel altogether?", choices=[
   "80 miles",
   "100 miles",
   "130 miles",
   "150 miles"], ans=2,
   why="Each constant stretch contributes a rectangle of area: 50(2) + 30(1) = 130 miles."),
 dict(q="Oil leaks from a tank at a rate of L(t) barrels per hour. Which expression gives the total number of barrels that leak out between t = 1 and t = 5?", choices=[
   "L(5) - L(1)",
   "int from 1 to 5 of L(t) dt",
   "L'(5) - L'(1)",
   "4 L(5)"], ans=1,
   why="L is already a rate, so the total leaked is the accumulation of that rate, the definite integral of L over [1, 5]."),
 dict(q="The temperature of a room changes at a constant rate of -2 degrees per hour for 4 hours. If the room began at 70 degrees, what is its temperature at the end?", choices=[
   "60 degrees",
   "62 degrees",
   "68 degrees",
   "78 degrees"], ans=1,
   why="The accumulated change is (-2)(4) = -8 degrees, so the final temperature is 70 - 8 = 62 degrees."),
 dict(q="A runner's velocity in meters per second increases linearly from 0 at t = 0 to 8 at t = 2, stays at 8 until t = 5, and then decreases linearly to 0 at t = 7. What total distance does the runner cover from t = 0 to t = 7?", choices=[
   "24 meters",
   "32 meters",
   "40 meters",
   "56 meters"], ans=2,
   why="The area is a triangle of area 8, a rectangle of area 24, and a triangle of area 8, and the velocity is never negative, so the distance is 40 meters."),
 dict(q="A tank holds 30 gallons of water. For the next 5 minutes water enters at 4 gallons per minute while water simultaneously leaves at 1.5 gallons per minute. How much water is in the tank at the end of the 5 minutes?", choices=[
   "17.5 gallons",
   "30 gallons",
   "42.5 gallons",
   "50 gallons"], ans=2,
   why="The net rate is 4 - 1.5 = 2.5 gallons per minute, so the tank gains 2.5(5) = 12.5 gallons, ending with 42.5."),
 dict(q="Asked for the total change in a quantity Q on [0, 5], a student answers Q'(5) - Q'(0). What is wrong with the student's reasoning?", choices=[
   "Nothing; that is the total change.",
   "The student subtracted values of the rate function instead of accumulating the rate over the interval.",
   "The student should have used Q'(0) - Q'(5).",
   "The student should have divided by 5."], ans=1,
   why="Total change is the accumulation of the rate, int from 0 to 5 of Q'(t) dt, which equals Q(5) - Q(0); subtracting two values of Q' compares rates, not amounts."),
 dict(q="Snow falls at a rate of 3 inches per hour for the first 2 hours of a storm and then at 1 inch per hour afterward. How many hours after the storm begins has 8 inches of snow accumulated?", choices=[
   "3 hours",
   "4 hours",
   "5 hours",
   "6 hours"], ans=1,
   why="The first 2 hours give 6 inches, and the remaining 2 inches take 2 more hours at 1 inch per hour, so the total is 4 hours."),
 dict(q="A particle's velocity is positive on [0, 3] and negative on [3, 5]. Which statement about the motion on [0, 5] is correct?", choices=[
   "The displacement and the total distance traveled are equal.",
   "The total distance traveled is greater than the displacement.",
   "The displacement is greater than the total distance traveled.",
   "The displacement must be zero."], ans=1,
   why="Displacement subtracts the area below the axis while distance adds it, so with a genuine sign change the distance exceeds the displacement."),
 dict(q="The volume of a balloon changes at a rate of 6 cubic centimeters per second for 0 <= t <= 5 and at a rate of -2 cubic centimeters per second for 5 < t <= 10. What is the net change in volume over [0, 10]?", choices=[
   "10 cubic centimeters",
   "20 cubic centimeters",
   "30 cubic centimeters",
   "40 cubic centimeters"], ans=1,
   why="The two accumulations are 6(5) = 30 and (-2)(5) = -10, and the net change adds them: 30 - 10 = 20 cubic centimeters."),
 dict(q="A quantity has rate of change R(t) kilograms per day, with int from 0 to 3 of R(t) dt = 12 and int from 0 to 7 of R(t) dt = 5. What happened between day 3 and day 7?", choices=[
   "The quantity increased by 5 kilograms.",
   "The quantity increased by 17 kilograms.",
   "The quantity decreased by 7 kilograms.",
   "The quantity decreased by 12 kilograms."], ans=2,
   why="The change on [3, 7] is 5 - 12 = -7, so the quantity fell by 7 kilograms over that stretch."),
 dict(q="For a differentiable position function s with velocity v, which of the following is NOT an accumulation of a rate of change?", choices=[
   "the total distance a car travels while its speedometer reading is recorded",
   "the slope of the tangent line to the graph of s at t = 3",
   "the total volume of water added to a pool from a hose with a known flow rate",
   "the net change in a bank balance given the rate of deposits and withdrawals"], ans=1,
   why="A slope is an instantaneous rate obtained by differentiating, the opposite operation; the other three sum a rate over an interval."),
]
