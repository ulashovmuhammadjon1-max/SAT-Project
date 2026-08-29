# CALC 4.5 Solving Related Rates Problems — 25 questions
# Every geometric relationship is stated in words; no question depends on a figure.
# Every numeric rate below is recomputed in verify_c4_5.py with sympy, differentiating
# the governing equation with the variables declared as functions of t.
TOPIC = ("4.5", "Solving Related Rates Problems", 4)
QUESTIONS = [
 dict(q="A 13-foot ladder leans against a vertical wall with its base on level ground. The base is pulled away from the wall at 2 feet per second. When the base is 5 feet from the wall, the top of the ladder is sliding down the wall at",
   choices=[
     "5/6 foot per second",
     "6/5 feet per second",
     "24/5 feet per second",
     "2 feet per second"], ans=0,
   why="From x^2 + y^2 = 169 with x = 5, y = 12, and dx/dt = 2, we get dy/dt = -(5)(2)/12 = -5/6, so the top falls at 5/6 foot per second."),

 dict(q="For the same 13-foot ladder whose base moves away from the wall at 2 feet per second, let theta be the angle the ladder makes with the ground. When the base is 5 feet from the wall, theta is changing at",
   choices=[
     "-1/6 radian per second",
     "-2/13 radian per second",
     "1/6 radian per second",
     "-5/12 radian per second"], ans=0,
   why="From cos(theta) = x/13, -sin(theta)(d theta/dt) = (1/13)(dx/dt), and with sin(theta) = 12/13 this gives d theta/dt = -1/6 radian per second."),

 dict(q="For the same 13-foot ladder, consider the right triangle formed by the ladder, the wall, and the ground. When the base is 5 feet from the wall and moving away at 2 feet per second, the area of that triangle is changing at",
   choices=[
     "119/12 square feet per second",
     "-119/12 square feet per second",
     "12 square feet per second",
     "5/6 square foot per second"], ans=0,
   why="A = xy/2 gives dA/dt = (x(dy/dt) + y(dx/dt))/2 = (5(-5/6) + 12(2))/2 = 119/12 square feet per second."),

 dict(q="Air is pumped into a spherical balloon at 100 cubic centimeters per second. When the radius is 5 centimeters, the radius is increasing at",
   choices=[
     "1/pi centimeter per second",
     "pi centimeters per second",
     "4/pi centimeters per second",
     "1/(4pi) centimeter per second"], ans=0,
   why="dV/dt = 4pi*r^2(dr/dt) gives 100 = 4pi(25)(dr/dt) = 100pi(dr/dt), so dr/dt = 1/pi centimeter per second."),

 dict(q="For that same balloon, at the instant when the radius is 5 centimeters and increasing at 1/pi centimeter per second, the surface area S = 4pi*r^2 is increasing at",
   choices=[
     "40 square centimeters per second",
     "40pi square centimeters per second",
     "20 square centimeters per second",
     "100 square centimeters per second"], ans=0,
   why="dS/dt = 8pi*r(dr/dt) = 8pi(5)(1/pi) = 40 square centimeters per second, and the pi cancels."),

 dict(q="A spherical snowball melts so that its radius decreases at 0.1 centimeter per minute. When the radius is 8 centimeters, its volume is changing at about",
   choices=[
     "-80.4 cubic centimeters per minute",
     "-25.6 cubic centimeters per minute",
     "-10.1 cubic centimeters per minute",
     "80.4 cubic centimeters per minute"], ans=0,
   why="dV/dt = 4pi*r^2(dr/dt) = 4pi(64)(-0.1) = -25.6pi, which is about -80.4 cubic centimeters per minute."),

 dict(q="A stone dropped in a pond makes a circular ripple whose radius grows at 2 feet per second. When the radius is 10 feet, the area enclosed is growing at",
   choices=[
     "40pi square feet per second",
     "20pi square feet per second",
     "100pi square feet per second",
     "4pi square feet per second"], ans=0,
   why="dA/dt = 2pi*r(dr/dt) = 2pi(10)(2) = 40pi square feet per second."),

 dict(q="Water is poured into a cone-shaped tank, vertex down, whose top radius is 5 feet and whose depth is 10 feet, so the water's radius is always half its depth. If water enters at 9 cubic feet per minute, the depth is rising, when the water is 6 feet deep, at",
   choices=[
     "1/pi foot per minute",
     "9/pi feet per minute",
     "1/(4pi) foot per minute",
     "4/pi feet per minute"], ans=0,
   why="With r = h/2, V = pi*h^3/12 and dV/dt = (pi*h^2/4)(dh/dt), so 9 = 9pi(dh/dt) and dh/dt = 1/pi foot per minute."),

 dict(q="Sand falls onto a conical pile at 10 cubic feet per minute, and the pile always has diameter equal to its height. When the pile is 4 feet high, its height is increasing at",
   choices=[
     "5/(2pi) feet per minute",
     "5/(8pi) foot per minute",
     "10/pi feet per minute",
     "2/(5pi) foot per minute"], ans=0,
   why="Diameter equal to height means r = h/2, so V = pi*h^3/12 and 10 = (pi(16)/4)(dh/dt) = 4pi(dh/dt), giving dh/dt = 5/(2pi) feet per minute."),

 dict(q="A 6-foot-tall person walks away from a 15-foot-tall lamppost along level ground at 5 feet per second. The person's shadow is lengthening at",
   choices=[
     "10/3 feet per second",
     "5/3 feet per second",
     "25/3 feet per second",
     "2 feet per second"], ans=0,
   why="Similar triangles give 6/s = 15/(x + s), so s = 2x/3 and ds/dt = (2/3)(5) = 10/3 feet per second."),

 dict(q="For that same 6-foot person and 15-foot lamppost, the tip of the shadow is moving away from the lamppost at",
   choices=[
     "25/3 feet per second",
     "10/3 feet per second",
     "5 feet per second",
     "15/3 feet per second"], ans=0,
   why="The tip's distance from the post is x + s = x + 2x/3 = 5x/3, so its rate is (5/3)(5) = 25/3 feet per second, the walking rate plus the shadow's growth."),

 dict(q="Two cars leave the same intersection at the same time, one heading due north at 60 miles per hour and one heading due east at 80 miles per hour. One hour later, the distance between them is increasing at",
   choices=[
     "100 miles per hour",
     "140 miles per hour",
     "20 miles per hour",
     "70 miles per hour"], ans=0,
   why="With x = 80, y = 60, and z = 100, z(dz/dt) = x(dx/dt) + y(dy/dt) gives dz/dt = (80(80) + 60(60))/100 = 100 miles per hour."),

 dict(q="A car is 30 miles due north of an intersection driving north at 40 miles per hour, and a truck is 40 miles due east of the same intersection driving east at 30 miles per hour. The distance between them is changing at",
   choices=[
     "48 miles per hour",
     "70 miles per hour",
     "50 miles per hour",
     "35 miles per hour"], ans=0,
   why="With x = 40, dx/dt = 30, y = 30, dy/dt = 40, and z = 50, dz/dt = (40(30) + 30(40))/50 = 48 miles per hour."),

 dict(q="A kite stays at a constant height of 100 feet while the wind carries it horizontally away from the person holding it at 8 feet per second. When 260 feet of string are out, the string is being let out at",
   choices=[
     "96/13 feet per second",
     "8 feet per second",
     "13/96 foot per second",
     "5/13 foot per second"], ans=0,
   why="With z^2 = x^2 + 100^2 and z = 260 the horizontal distance is 240, so dz/dt = (240/260)(8) = 96/13 feet per second."),

 dict(q="A rectangular tank has a horizontal base 4 feet by 3 feet and vertical sides. Water flows in at 6 cubic feet per minute. The water level rises at",
   choices=[
     "0.5 foot per minute",
     "2 feet per minute",
     "6 feet per minute",
     "0.25 foot per minute"], ans=0,
   why="V = 12h so dV/dt = 12(dh/dt), and 6 = 12(dh/dt) gives dh/dt = 0.5 foot per minute, the same at every depth."),

 dict(q="A baseball diamond is a square 90 feet on a side. A runner leaves first base and runs toward second base at 25 feet per second. When the runner is 30 feet from first base, the distance from the runner to home plate is changing at about",
   choices=[
     "7.91 feet per second",
     "25 feet per second",
     "8.33 feet per second",
     "23.72 feet per second"], ans=0,
   why="With z^2 = 90^2 + x^2, x = 30 and z = 30sqrt(10), so dz/dt = x(dx/dt)/z = 750/(30sqrt(10)) = 25/sqrt(10), about 7.91 feet per second."),

 dict(q="A balloon rises vertically at 10 feet per second from a launch point on level ground 100 feet from an observer. When the balloon is 100 feet high, the observer's angle of elevation is increasing at",
   choices=[
     "0.05 radian per second",
     "0.1 radian per second",
     "0.2 radian per second",
     "0.025 radian per second"], ans=0,
   why="From tan(theta) = h/100, sec^2(theta)(d theta/dt) = (1/100)(dh/dt); at h = 100 the angle is pi/4 and sec^2 = 2, so d theta/dt = 0.1/2 = 0.05 radian per second."),

 dict(q="A gas is compressed at constant temperature so that its pressure P in pounds per square inch and volume V in cubic inches satisfy PV = 600. When V = 30 cubic inches and the volume is decreasing at 5 cubic inches per minute, the pressure is",
   choices=[
     "increasing at 10/3 pounds per square inch per minute",
     "decreasing at 10/3 pounds per square inch per minute",
     "increasing at 100 pounds per square inch per minute",
     "increasing at 5 pounds per square inch per minute"], ans=0,
   why="P = 20 there, and P(dV/dt) + V(dP/dt) = 0 gives 20(-5) + 30(dP/dt) = 0, so dP/dt = 10/3 and the pressure rises as the gas is squeezed."),

 dict(q="The side of a square grows at 2 centimeters per second. When the side is 10 centimeters, the area is growing at",
   choices=[
     "40 square centimeters per second",
     "20 square centimeters per second",
     "100 square centimeters per second",
     "4 square centimeters per second"], ans=0,
   why="dA/dt = 2s(ds/dt) = 2(10)(2) = 40 square centimeters per second."),

 dict(q="A cube's edge grows at 0.5 centimeter per second. When the edge is 4 centimeters, the total surface area S = 6s^2 is growing at",
   choices=[
     "24 square centimeters per second",
     "48 square centimeters per second",
     "96 square centimeters per second",
     "12 square centimeters per second"], ans=0,
   why="dS/dt = 12s(ds/dt) = 12(4)(0.5) = 24 square centimeters per second; 24 cubic centimeters per second would be the volume's rate, a different quantity."),

 dict(q="A trough 10 feet long has a cross-section that is an isosceles triangle 3 feet across the top and 1 foot deep, vertex down, so the surface width is always three times the water depth. Water enters at 12 cubic feet per minute. When the water is 0.5 foot deep, the depth is rising at",
   choices=[
     "0.8 foot per minute",
     "1.6 feet per minute",
     "0.4 foot per minute",
     "2.4 feet per minute"], ans=0,
   why="The cross-sectional area is (1/2)(3h)(h), so V = 15h^2 and dV/dt = 30h(dh/dt); 12 = 30(0.5)(dh/dt) gives dh/dt = 0.8 foot per minute."),

 dict(q="A person of height p walks away from a lamppost of height L at a constant rate. Which relationship correctly sets up the shadow-length problem, where x is the distance from the post to the person and s is the shadow length?",
   choices=[
     "p/s = L/(x + s)",
     "p/x = L/s",
     "p/s = L/x",
     "p*s = L(x + s)"], ans=0,
   why="The small triangle formed by the person and the shadow is similar to the large triangle formed by the post and the whole distance from post to shadow tip."),

 dict(q="In the sliding-ladder problem, the base moves away from the wall at a positive rate and the answer for dy/dt comes out negative. This is because",
   choices=[
     "y measures the height of the top of the ladder, which is decreasing as the base slides out",
     "the ladder's length is shrinking",
     "a sign error has been made; dy/dt must be positive",
     "the derivative of a square root is always negative"], ans=0,
   why="A negative rate simply reports a decreasing quantity, and the top of the ladder does drop as the base slides away."),

 dict(q="A car is 0.3 mile due north of an intersection moving south toward it at 60 miles per hour, while a truck is 0.4 mile due east of the intersection moving west toward it at 45 miles per hour. At that instant the distance between the two vehicles is",
   choices=[
     "decreasing at 72 miles per hour",
     "increasing at 72 miles per hour",
     "decreasing at 105 miles per hour",
     "decreasing at 36 miles per hour"], ans=0,
   why="With z = 0.5, dz/dt = (0.4(-45) + 0.3(-60))/0.5 = -72, so the gap closes at 72 miles per hour."),

 dict(q="A spherical balloon is inflated so that its volume increases at a constant 20 cubic centimeters per second. At the instant when the balloon's surface area is 100pi square centimeters, the radius is increasing at",
   choices=[
     "1/(5pi) centimeter per second",
     "1/pi centimeter per second",
     "5/pi centimeters per second",
     "1/(20pi) centimeter per second"], ans=0,
   why="Surface area 100pi means 4pi*r^2 = 100pi and r = 5, so 20 = 4pi(25)(dr/dt) gives dr/dt = 1/(5pi) centimeter per second."),
]
