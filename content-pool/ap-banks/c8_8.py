# CALC 8.8 Volumes with Cross Sections: Triangles and Semicircles
# — 25 questions
# Equilateral triangle of side s: (sqrt(3)/4)s^2. Isosceles right triangle with
# a LEG in the base: s^2/2; with the HYPOTENUSE in the base: s^2/4. Semicircle
# of DIAMETER s: (pi/8)s^2. All volumes recomputed by sympy; see verify_c8_8.py.
TOPIC = ("8.8", "Volumes with Cross Sections: Triangles and Semicircles", 8)
QUESTIONS = [
 dict(q="What is the area of an equilateral triangle with side length s?", choices=[
   "(sqrt(3)/4)*s^2",
   "(sqrt(3)/2)*s^2",
   "s^2/2",
   "(1/2)*s^2*sqrt(2)"], ans=0,
   why="Its height is (sqrt(3)/2)s, so the area is (1/2)*s*(sqrt(3)/2)s."),
 dict(q="What is the area of a semicircle whose DIAMETER has length s?", choices=[
   "(pi/8)*s^2",
   "(pi/2)*s^2",
   "(pi/4)*s^2",
   "pi*s^2"], ans=0,
   why="The radius is s/2, so the area is (1/2)*pi*(s/2)^2 = pi*s^2/8."),
 dict(q="What is the area of an isosceles right triangle whose HYPOTENUSE has length s?", choices=[
   "s^2/4",
   "s^2/2",
   "s^2",
   "(sqrt(2)/4)*s^2"], ans=0,
   why="Each leg is s/sqrt(2), so the area is (1/2)(s/sqrt(2))^2 = s^2/4."),
 dict(q="What is the area of an isosceles right triangle whose LEGS have length s?", choices=[
   "s^2/2",
   "s^2/4",
   "s^2",
   "(sqrt(2)/2)*s^2"], ans=0,
   why="The two legs are the base and the height, giving area (1/2)s^2."),
 dict(q="The base of a solid is the region bounded by y = 2x, y = 0, and x = 3. Cross sections perpendicular to the x-axis are equilateral triangles. What is the volume?", choices=[
   "9*sqrt(3)",
   "3*sqrt(3)",
   "18*sqrt(3)",
   "36*sqrt(3)"], ans=0,
   why="The side is 2x, so the volume is (sqrt(3)/4) times the integral of 4x^2 from 0 to 3, which is 9*sqrt(3)."),
 dict(q="The base of a solid is the region between y = 1 - x^2 and the x-axis. Cross sections perpendicular to the x-axis are semicircles with diameter in the base. What is the volume?", choices=[
   "2*pi/15",
   "pi/15",
   "4*pi/15",
   "16*pi/15"], ans=0,
   why="The integral of (1 - x^2)^2 from -1 to 1 is 16/15, and (pi/8)(16/15) = 2pi/15."),
 dict(q="The base of a solid is the disk x^2 + y^2 = 9. Cross sections perpendicular to the x-axis are equilateral triangles. What is the volume?", choices=[
   "36*sqrt(3)",
   "18*sqrt(3)",
   "9*sqrt(3)",
   "72*sqrt(3)"], ans=0,
   why="The side is 2*sqrt(9 - x^2), so the volume is sqrt(3) times the integral of 9 - x^2 from -3 to 3, which is 36*sqrt(3)."),
 dict(q="The base of a solid is the region between y = 2 - x^2 and y = x^2. Cross sections perpendicular to the x-axis are semicircles with diameter in the base. What is the volume?", choices=[
   "8*pi/15",
   "4*pi/15",
   "2*pi/15",
   "16*pi/15"], ans=0,
   why="The diameter is 2 - 2x^2 on [-1, 1], whose square integrates to 64/15, and (pi/8)(64/15) = 8pi/15."),
 dict(q="The base of a solid is the region bounded by y = sqrt(x), y = 0, and x = 16. Cross sections perpendicular to the x-axis are isosceles right triangles with one LEG in the base. What is the volume?", choices=[
   "16",
   "32",
   "64",
   "128"], ans=2,
   why="The leg is sqrt(x), so the area is x/2 and the integral from 0 to 16 is 64."),
 dict(q="The base of a solid is the region bounded by y = x, y = 0, and x = 6. Cross sections perpendicular to the x-axis are isosceles right triangles with the HYPOTENUSE in the base. What is the volume?", choices=[
   "9",
   "18",
   "36",
   "72"], ans=1,
   why="The hypotenuse is x, so the area is x^2/4 and the integral from 0 to 6 is 18."),
 dict(q="The base of a solid is the triangle bounded by y = 2 - x and the two axes. Cross sections perpendicular to the x-axis are semicircles with diameter in the base. What is the volume?", choices=[
   "pi/3",
   "pi/6",
   "2*pi/3",
   "8*pi/3"], ans=0,
   why="The integral of (2 - x)^2 from 0 to 2 is 8/3, and (pi/8)(8/3) = pi/3."),
 dict(q="The base of a solid is the disk x^2 + y^2 = 1. Cross sections perpendicular to the x-axis are semicircles with diameter in the base. What is the volume?", choices=[
   "2*pi/3",
   "pi/3",
   "4*pi/3",
   "8*pi/3"], ans=0,
   why="The diameter is 2*sqrt(1 - x^2), so the area is (pi/2)(1 - x^2) and the integral gives 2pi/3."),
 dict(q="Which integral gives the volume of a solid whose base is the region between y = f(x) and the x-axis on [a, b], with semicircular cross sections having diameter in the base?", choices=[
   "(pi/8) * int from a to b of f(x)^2 dx",
   "(pi/2) * int from a to b of f(x)^2 dx",
   "pi * int from a to b of f(x)^2 dx",
   "(pi/4) * int from a to b of f(x) dx"], ans=0,
   why="The radius is f(x)/2, so the area of the semicircle is (1/2)pi(f(x)/2)^2 = (pi/8)f(x)^2."),
 dict(q="The base of a solid is the region between y = cos(x) and the x-axis for -pi/2 <= x <= pi/2. Cross sections perpendicular to the x-axis are equilateral triangles. What is the volume?", choices=[
   "sqrt(3)*pi/8",
   "sqrt(3)*pi/4",
   "sqrt(3)*pi/2",
   "sqrt(3)/8"], ans=0,
   why="The integral of cos^2(x) on that interval is pi/2, and (sqrt(3)/4)(pi/2) = sqrt(3)pi/8."),
 dict(q="The base of a solid is the region bounded by y = e^(2x), y = 0, x = 0, and x = 1. Cross sections perpendicular to the x-axis are semicircles with diameter in the base. What is the volume?", choices=[
   "pi*(e^4 - 1)/32",
   "pi*(e^4 - 1)/16",
   "pi*(e^4 - 1)/8",
   "pi*(e^2 - 1)/32"], ans=0,
   why="The integral of e^(4x) from 0 to 1 is (e^4 - 1)/4, and multiplying by pi/8 gives pi(e^4 - 1)/32."),
 dict(q="A student computes the volume of a solid with semicircular cross sections using (pi/2)*s^2, where s is the segment cut from the base. What is the error?", choices=[
   "s is the diameter, so the radius is s/2 and the area is (pi/8)s^2",
   "the area of a semicircle is pi*s^2",
   "the segment should be squared twice",
   "there is no error"], ans=0,
   why="Using s as the radius instead of the diameter inflates the area by a factor of 4."),
 dict(q="What is the area of a semicircle whose RADIUS is s?", choices=[
   "(pi/2)*s^2",
   "(pi/8)*s^2",
   "pi*s^2",
   "(pi/4)*s^2"], ans=0,
   why="Half of pi*s^2 is (pi/2)s^2; the pi/8 formula applies only when s is the diameter."),
 dict(q="The base of a solid is the region bounded by y = x^3, y = 0, and x = 1. Cross sections perpendicular to the x-axis are equilateral triangles. What is the volume?", choices=[
   "sqrt(3)/28",
   "sqrt(3)/14",
   "sqrt(3)/7",
   "sqrt(3)/4"], ans=0,
   why="The integral of x^6 from 0 to 1 is 1/7, and (sqrt(3)/4)(1/7) = sqrt(3)/28."),
 dict(q="The base of a solid is the region bounded by x = y^2 and x = 4. Cross sections perpendicular to the y-axis are isosceles right triangles with one LEG in the base. What is the volume?", choices=[
   "64/15",
   "128/15",
   "256/15",
   "512/15"], ans=2,
   why="The leg is 4 - y^2, and half the integral of its square from -2 to 2 is 256/15."),
 dict(q="The base of a solid is the region bounded by y = 1/x, y = 0, x = 1, and x = 4. Cross sections perpendicular to the x-axis are equilateral triangles. What is the volume?", choices=[
   "3*sqrt(3)/16",
   "3*sqrt(3)/4",
   "sqrt(3)/4",
   "15*sqrt(3)/16"], ans=0,
   why="The integral of 1/x^2 from 1 to 4 is 3/4, and (sqrt(3)/4)(3/4) = 3sqrt(3)/16."),
 dict(q="The base of a solid is the triangle bounded by y = 4 - x and the two axes. Cross sections perpendicular to the x-axis are semicircles with diameter in the base. What is the volume?", choices=[
   "8*pi/3",
   "4*pi/3",
   "16*pi/3",
   "32*pi/3"], ans=0,
   why="The integral of (4 - x)^2 from 0 to 4 is 64/3, and (pi/8)(64/3) = 8pi/3."),
 dict(q="Two solids share the same base. One has square cross sections and the other has semicircular cross sections with diameter in the base. How do their volumes compare?", choices=[
   "the semicircular solid has pi/8 of the volume of the square one, so it is smaller",
   "the semicircular solid has pi/2 of the volume, so it is larger",
   "the volumes are equal",
   "the semicircular solid has pi times the volume"], ans=0,
   why="The areas of the two cross sections differ by exactly the factor pi/8 at every slice, so the volumes differ by that factor."),
 dict(q="The base of a solid is the region between y = 3x and y = x^2. Cross sections perpendicular to the x-axis are equilateral triangles. What is the volume?", choices=[
   "81*sqrt(3)/40",
   "81*sqrt(3)/20",
   "81*sqrt(3)/10",
   "27*sqrt(3)/40"], ans=0,
   why="The integral of (3x - x^2)^2 from 0 to 3 is 81/10, and (sqrt(3)/4)(81/10) = 81sqrt(3)/40."),
 dict(q="The base of a solid is the region bounded by y = x, y = 0, and x = 3. Cross sections perpendicular to the x-axis are triangles whose height is twice the base. What is the volume?", choices=[
   "9",
   "27/2",
   "18",
   "27"], ans=0,
   why="The area is (1/2)(x)(2x) = x^2, and the integral from 0 to 3 is 9."),
 dict(q="For a solid with semicircular cross sections built on the region between y = f(x) and y = g(x), the radius of a cross section at x is", choices=[
   "(f(x) - g(x))/2",
   "f(x) - g(x)",
   "2*(f(x) - g(x))",
   "(f(x) + g(x))/2"], ans=0,
   why="The segment between the curves is the diameter, so the radius is half of it."),
]
