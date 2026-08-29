# CALC 4.4 Introduction to Related Rates — 25 questions
# Every differentiated relation and every numeric rate is recomputed in
# verify_c4_4.py with sympy, using sp.Function objects of t so the chain rule is
# applied by sympy rather than assumed. The translation items ("increasing at 10
# cubic centimeters per second" means dV/dt = 10) are conventions, not computations.
TOPIC = ("4.4", "Introduction to Related Rates", 4)
QUESTIONS = [
 dict(q="If x and y are both differentiable functions of t and x^2 + y^2 = 25, then differentiating both sides with respect to t gives",
   choices=[
     "2x(dx/dt) + 2y(dy/dt) = 0",
     "2x + 2y = 0",
     "2x(dx/dt) + 2y(dy/dt) = 25",
     "2x(dx/dt) + 2y(dy/dt) = 50t"], ans=0,
   why="Each term needs the chain rule, and the derivative of the constant 25 is 0."),

 dict(q="A circle's radius r is a function of time t, and its area is A = pi*r^2. Then dA/dt equals",
   choices=[
     "2pi*r(dr/dt)",
     "2pi*r",
     "pi*r^2(dr/dt)",
     "2pi(dr/dt)"], ans=0,
   why="Differentiating pi*r^2 with respect to t requires the chain rule factor dr/dt; omitting it gives the derivative with respect to r instead."),

 dict(q="A sphere's radius r is a function of time. For V = (4/3)pi*r^3, dV/dt equals",
   choices=[
     "4pi*r^2(dr/dt)",
     "4pi*r^2",
     "(4/3)pi*r^2(dr/dt)",
     "12pi*r^2(dr/dt)"], ans=0,
   why="d/dt[(4/3)pi*r^3] = (4/3)pi*3r^2*(dr/dt) = 4pi*r^2(dr/dt)."),

 dict(q="A cube's edge length s is a function of time and its volume is V = s^3. Then dV/dt equals",
   choices=[
     "3s^2(ds/dt)",
     "3s^2",
     "s^3(ds/dt)",
     "3s(ds/dt)"], ans=0,
   why="The chain rule gives 3s^2 times ds/dt, since s itself depends on t."),

 dict(q="A triangle has base b and height h, both changing with time, and area A = (1/2)bh. Then dA/dt equals",
   choices=[
     "(1/2)[b(dh/dt) + h(db/dt)]",
     "(1/2)(db/dt)(dh/dt)",
     "(1/2)b(dh/dt)",
     "(1/2)[b(dh/dt) - h(db/dt)]"], ans=0,
   why="Both factors vary, so the product rule applies and each term keeps its own time derivative."),

 dict(q="If x and y are differentiable functions of t with xy = 12, then",
   choices=[
     "x(dy/dt) + y(dx/dt) = 0",
     "(dx/dt)(dy/dt) = 0",
     "x(dy/dt) + y(dx/dt) = 12",
     "x(dy/dt) - y(dx/dt) = 0"], ans=0,
   why="The product rule applies on the left and the derivative of the constant 12 is 0."),

 dict(q="If r is a differentiable function of t, then d/dt(r^3) equals",
   choices=[
     "3r^2(dr/dt)",
     "3r^2",
     "r^3(dr/dt)",
     "3r^2 + dr/dt"], ans=0,
   why="This is the chain rule: differentiate the outer power, then multiply by the derivative of the inside function r with respect to t."),

 dict(q="A balloon is being inflated so that its volume increases at 10 cubic centimeters per second. In symbols this says",
   choices=[
     "dV/dt = 10",
     "V = 10t",
     "dV/dr = 10",
     "dr/dt = 10"], ans=0,
   why="A rate of change of volume with respect to time is exactly dV/dt, and it is given as the constant 10."),

 dict(q="The top of a ladder slides down a wall at 2 feet per second. If y is the height of the top of the ladder above the ground, this is written",
   choices=[
     "dy/dt = -2",
     "dy/dt = 2",
     "y = -2t",
     "dy/dx = -2"], ans=0,
   why="The height is decreasing, so the rate is negative; the magnitude 2 is the speed."),

 dict(q="In a related rates problem about a circle, why is it wrong to substitute r = 5 into A = pi*r^2 before differentiating with respect to t?",
   choices=[
     "Substituting first treats the radius as a constant, and the derivative of the constant 25pi is 0",
     "Substituting first gives dA/dt in the wrong units",
     "Substituting first makes the chain rule unnecessary but the answer doubles",
     "There is nothing wrong with it; the answer is the same either way"], ans=0,
   why="A value of a changing quantity may only be substituted after differentiating, or the variable is frozen and its rate disappears."),

 dict(q="A circle's radius grows at dr/dt = 2 centimeters per second. When r = 5 centimeters, dA/dt equals",
   choices=[
     "20pi square centimeters per second",
     "10pi square centimeters per second",
     "25pi square centimeters per second",
     "50pi square centimeters per second"], ans=0,
   why="dA/dt = 2pi*r(dr/dt) = 2pi(5)(2) = 20pi square centimeters per second."),

 dict(q="A cube's edge grows at 0.5 inch per second. When the edge is 4 inches, the volume is changing at",
   choices=[
     "24 cubic inches per second",
     "48 cubic inches per second",
     "8 cubic inches per second",
     "32 cubic inches per second"], ans=0,
   why="dV/dt = 3s^2(ds/dt) = 3(16)(0.5) = 24 cubic inches per second."),

 dict(q="Suppose x^2 + y^2 = 169 with x and y differentiable functions of t. At the instant when x = 5, y = 12, and dx/dt = 4, the value of dy/dt is",
   choices=[
     "-5/3",
     "5/3",
     "-3/5",
     "-24/5"], ans=0,
   why="From 2(5)(4) + 2(12)(dy/dt) = 0 we get dy/dt = -40/24 = -5/3."),

 dict(q="A square's side length increases at 3 centimeters per minute. Its perimeter P = 4s is then changing at",
   choices=[
     "12 centimeters per minute",
     "3 centimeters per minute",
     "4 centimeters per minute",
     "12s centimeters per minute"], ans=0,
   why="dP/dt = 4(ds/dt) = 4(3) = 12 centimeters per minute, independent of the current side length."),

 dict(q="A circle's radius increases at 0.5 meter per second. The circumference C = 2pi*r is changing at",
   choices=[
     "pi meters per second",
     "0.5pi meters per second",
     "2pi meters per second",
     "pi*r meters per second"], ans=0,
   why="dC/dt = 2pi(dr/dt) = 2pi(0.5) = pi meters per second, which does not depend on r."),

 dict(q="A cylinder has radius r and height h, both functions of time, and volume V = pi*r^2*h. Then dV/dt equals",
   choices=[
     "pi[2r*h(dr/dt) + r^2(dh/dt)]",
     "pi[2r(dr/dt) + (dh/dt)]",
     "2pi*r*h(dr/dt)",
     "pi*r^2(dh/dt)"], ans=0,
   why="The product rule on r^2 and h gives one term for each changing factor, each with its own time derivative."),

 dict(q="Water fills a cylindrical tank of fixed radius 3 feet, so only the depth h changes. For V = pi*r^2*h, dV/dt equals",
   choices=[
     "9pi(dh/dt)",
     "9pi*h(dh/dt)",
     "6pi(dh/dt)",
     "pi*h^2(dh/dt)"], ans=0,
   why="With r constant at 3, V = 9pi*h and the only time-varying factor is h."),

 dict(q="If x, y, and z are differentiable functions of t satisfying z^2 = x^2 + y^2, then",
   choices=[
     "2z(dz/dt) = 2x(dx/dt) + 2y(dy/dt)",
     "z(dz/dt) = x + y",
     "2z = 2x(dx/dt) + 2y(dy/dt)",
     "dz/dt = dx/dt + dy/dt"], ans=0,
   why="Every squared term needs the chain rule, so each contributes twice the variable times its own rate."),

 dict(q="If y = sqrt(x) and dx/dt = 6, then at the instant when x = 9 the value of dy/dt is",
   choices=[
     "1",
     "3",
     "6",
     "1/6"], ans=0,
   why="dy/dt = (1/(2sqrt(x)))(dx/dt) = (1/6)(6) = 1."),

 dict(q="If y = sin(x) and dx/dt = 3, then at the instant when x = pi/3 the value of dy/dt is",
   choices=[
     "3/2",
     "1/2",
     "(3sqrt(3))/2",
     "-3/2"], ans=0,
   why="dy/dt = cos(x)(dx/dt) = (1/2)(3) = 3/2; using sin instead of cos gives (3sqrt(3))/2."),

 dict(q="A conical tank has radius always equal to half its depth, so r = h/2. Written in terms of h alone, the volume V = (1/3)pi*r^2*h and its time derivative are",
   choices=[
     "V = pi*h^3/12 and dV/dt = (pi*h^2/4)(dh/dt)",
     "V = pi*h^3/3 and dV/dt = pi*h^2(dh/dt)",
     "V = pi*h^3/12 and dV/dt = (pi*h^3/12)(dh/dt)",
     "V = pi*h^2/12 and dV/dt = (pi*h/6)(dh/dt)"], ans=0,
   why="Substituting r = h/2 gives V = (1/3)pi(h^2/4)h = pi*h^3/12, whose time derivative is (3pi*h^2/12)(dh/dt) = (pi*h^2/4)(dh/dt)."),

 dict(q="If x and y are differentiable functions of t with x^2*y = 8, then",
   choices=[
     "2xy(dx/dt) + x^2(dy/dt) = 0",
     "2x(dx/dt) + (dy/dt) = 0",
     "2xy(dx/dt) + x^2(dy/dt) = 8",
     "x^2(dy/dt) = 2xy(dx/dt)"], ans=0,
   why="Apply the product rule to x^2 times y, chain rule inside each factor, and set the result equal to the derivative of the constant 8."),

 dict(q="Oil spreads in a circle whose area grows at a constant 12 square meters per second. When the radius is 3 meters, dr/dt equals",
   choices=[
     "2/pi meters per second",
     "6pi meters per second",
     "2pi meters per second",
     "1/(6pi) meters per second"], ans=0,
   why="From 12 = 2pi(3)(dr/dt) we get dr/dt = 12/(6pi) = 2/pi meters per second."),

 dict(q="A tank's volume V is measured in liters and time t in seconds. The units of dV/dt are",
   choices=[
     "liters per second",
     "liters",
     "seconds per liter",
     "liters per second per second"], ans=0,
   why="A time derivative of a volume carries volume units over time units."),

 dict(q="If y is a differentiable function of x and x is a differentiable function of t, then dy/dt equals",
   choices=[
     "(dy/dx)(dx/dt)",
     "(dy/dx) + (dx/dt)",
     "(dy/dx)/(dx/dt)",
     "(dx/dy)(dt/dx)"], ans=0,
   why="This is the chain rule, and it is the identity every related rates problem rests on."),
]
