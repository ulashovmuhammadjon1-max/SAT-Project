# CALC 4.2 Straight-Line Motion: Connecting Position, Velocity, and Acceleration — 25 questions
# Every derivative, root, extreme value, and total-distance figure is verified in
# verify_c4_2.py with sympy. The definitional items (speed = |v|, speeding up when
# v and a share a sign, direction change requires a sign change in v) carry no
# computation and are checked by statement of the definition.
TOPIC = ("4.2", "Straight-Line Motion: Connecting Position, Velocity, and Acceleration", 4)
QUESTIONS = [
 dict(q="A particle moves along a line with position s(t). Its velocity at time t is",
   choices=[
     "s'(t)",
     "s''(t)",
     "|s(t)|",
     "s(t)/t"], ans=0,
   why="Velocity is the instantaneous rate of change of position, which is the first derivative of s."),

 dict(q="If a particle has velocity v(t), its speed at time t is",
   choices=[
     "|v(t)|",
     "v(t)",
     "v'(t)",
     "|v'(t)|"], ans=0,
   why="Speed is the magnitude of velocity, so it is |v(t)| and is never negative."),

 dict(q="A particle moving along a line is speeding up at time t exactly when",
   choices=[
     "v(t) and a(t) are both nonzero and have the same sign",
     "a(t) > 0",
     "v(t) > 0",
     "v(t) and a(t) have opposite signs"], ans=0,
   why="Speed is |v|, and |v| increases precisely when the acceleration pushes in the same direction the particle is already moving."),

 dict(q="At time t = 5 a particle on the x-axis has v(5) = -4 and a(5) = -2. At that instant the particle is",
   choices=[
     "moving in the negative direction and speeding up",
     "moving in the negative direction and slowing down",
     "moving in the positive direction and speeding up",
     "at rest"], ans=0,
   why="Negative velocity means motion in the negative direction, and because the acceleration has the same sign the speed |v| is increasing."),

 dict(q="At time t = 4 a particle has velocity -8 meters per second and acceleration 3 meters per second per second. At t = 4 the particle is",
   choices=[
     "slowing down, because the velocity and the acceleration have opposite signs",
     "speeding up, because the acceleration is positive",
     "speeding up, because the particle is moving backward",
     "momentarily at rest"], ans=0,
   why="A positive acceleration opposes motion that is in the negative direction, so the speed |v| = 8 is decreasing even though a > 0."),

 dict(q="A particle moves along the x-axis with position s(t) = t^3 - 6t^2 + 9t for t >= 0. Its velocity is",
   choices=[
     "v(t) = 3t^2 - 12t + 9",
     "v(t) = 3t^2 - 6t + 9",
     "v(t) = t^2 - 12t + 9",
     "v(t) = 6t - 12"], ans=0,
   why="Differentiating term by term gives 3t^2 - 12t + 9; 6t - 12 is the acceleration."),

 dict(q="For the particle with position s(t) = t^3 - 6t^2 + 9t, the particle is at rest at",
   choices=[
     "t = 1 and t = 3",
     "t = 2 only",
     "t = 0 and t = 2",
     "t = 3 only"], ans=0,
   why="Setting 3t^2 - 12t + 9 = 3(t - 1)(t - 3) equal to zero gives t = 1 and t = 3."),

 dict(q="For the particle with position s(t) = t^3 - 6t^2 + 9t and t >= 0, the particle moves in the negative direction on the interval",
   choices=[
     "1 < t < 3",
     "0 < t < 1",
     "t > 3",
     "0 < t < 2"], ans=0,
   why="v(t) = 3(t - 1)(t - 3) is negative exactly between its two roots."),

 dict(q="For the particle with position s(t) = t^3 - 6t^2 + 9t, describe the motion at t = 2.5.",
   choices=[
     "Moving in the negative direction and slowing down, since v(2.5) = -2.25 and a(2.5) = 3",
     "Moving in the negative direction and speeding up, since the acceleration is positive",
     "Moving in the positive direction and speeding up, since the acceleration is positive",
     "At rest, since the acceleration is changing sign"], ans=0,
   why="Velocity is negative and acceleration is positive, so they disagree in sign and the speed is decreasing even though a > 0."),

 dict(q="A particle has position s(t) = t^3 - 6t^2 + 9t. The total distance it travels for 0 <= t <= 4 is",
   choices=[
     "4",
     "8",
     "12",
     "16"], ans=2,
   why="The particle turns at t = 1 and t = 3, and |4 - 0| + |0 - 4| + |4 - 0| = 12, while 4 is only the net displacement."),

 dict(q="A particle has velocity v(t) = t^2 - 4t + 3 for t >= 0. The particle is speeding up on",
   choices=[
     "1 < t < 2 and t > 3",
     "0 < t < 1 and 2 < t < 3",
     "t > 2",
     "1 < t < 3"], ans=0,
   why="v is negative on (1, 3) and a(t) = 2t - 4 is negative on (0, 2), so v and a share a sign on (1, 2) and again on (3, infinity)."),

 dict(q="A ball is thrown upward so that its height above the ground, in feet, after t seconds is s(t) = -16t^2 + 64t + 80. The velocity of the ball at t = 1 second is, in feet per second,",
   choices=[
     "16",
     "32",
     "48",
     "128"], ans=1,
   why="v(t) = -32t + 64, so v(1) = 32 feet per second; 128 is the height s(1), not the velocity."),

 dict(q="For the ball with height s(t) = -16t^2 + 64t + 80 feet, the maximum height reached is, in feet,",
   choices=[
     "80",
     "128",
     "144",
     "160"], ans=2,
   why="The velocity -32t + 64 is zero at t = 2, and s(2) = 144 feet."),

 dict(q="The ball with height s(t) = -16t^2 + 64t + 80 feet strikes the ground. Its speed at that moment is, in feet per second,",
   choices=[
     "64",
     "80",
     "96",
     "160"], ans=2,
   why="The height is zero at t = 5, where v(5) = -96, and the speed is the magnitude |−96| = 96 feet per second."),

 dict(q="For the ball with height s(t) = -16t^2 + 64t + 80 feet, the acceleration at t = 3 seconds is, in feet per second per second,",
   choices=[
     "-32",
     "-16",
     "0",
     "64"], ans=0,
   why="a(t) = s''(t) = -32 for every t, a constant, since the height is a quadratic in t."),

 dict(q="A particle moves along the x-axis with position s(t) = 2 sin(t) for 0 <= t <= 2pi. At t = 3pi/4 the particle is",
   choices=[
     "moving in the negative direction and speeding up",
     "moving in the negative direction and slowing down",
     "moving in the positive direction and speeding up",
     "at rest"], ans=0,
   why="v = 2cos(3pi/4) = -sqrt(2) and a = -2sin(3pi/4) = -sqrt(2) are both negative, so the particle moves negatively with increasing speed."),

 dict(q="A particle moves along a line with position s(t) = t*e^(-t) for t >= 0. Its velocity is",
   choices=[
     "v(t) = (1 - t)e^(-t)",
     "v(t) = e^(-t)",
     "v(t) = -t*e^(-t)",
     "v(t) = (t - 1)e^(-t)"], ans=0,
   why="The product rule gives 1*e^(-t) + t*(-e^(-t)) = (1 - t)e^(-t); dropping the second term or losing the sign gives the other choices."),

 dict(q="For the particle with position s(t) = t*e^(-t), describe the motion at t = 1.5.",
   choices=[
     "Moving in the negative direction and speeding up, since v and a are both negative there",
     "Moving in the negative direction and slowing down, since the velocity is negative",
     "Moving in the positive direction and speeding up",
     "At rest, since t = 1.5 is past the turning point"], ans=0,
   why="v(1.5) = -0.5e^(-1.5) and a(1.5) = (1.5 - 2)e^(-1.5) = -0.5e^(-1.5) are both negative, so the speed is increasing."),

 dict(q="A particle moving along a line changes direction at time t = c only if",
   choices=[
     "v(c) = 0 and v changes sign at c",
     "v(c) = 0",
     "a(c) = 0",
     "s(c) = 0"], ans=0,
   why="A velocity that touches zero without changing sign, as with v(t) = (t - 2)^2, means the particle pauses but keeps going the same way."),

 dict(q="A particle has velocity v(t) = (t - 2)^2 for t >= 0. Which statement is true?",
   choices=[
     "The particle is momentarily at rest at t = 2 but never changes direction.",
     "The particle changes direction at t = 2.",
     "The particle moves in the negative direction for t < 2.",
     "The particle is at rest for all t."], ans=0,
   why="A square is never negative, so the velocity is zero only at t = 2 and positive on both sides of it."),

 dict(q="A particle has position s(t) = t^3 - 6t^2 + 9t. Its average velocity on the interval 0 <= t <= 4 is",
   choices=[
     "0",
     "1",
     "3",
     "12"], ans=1,
   why="Average velocity is (s(4) - s(0))/(4 - 0) = (4 - 0)/4 = 1, which is not the same as the total distance 12 divided by nothing."),

 dict(q="A particle has velocity v(t) = 4 - t^2 for t >= 0. On the interval 0 < t < 2 the particle's speed is",
   choices=[
     "decreasing, because the velocity is positive and the acceleration is negative",
     "increasing, because the velocity is positive",
     "increasing, because the acceleration is negative",
     "constant, because the velocity is a smooth function"], ans=0,
   why="v > 0 and a(t) = -2t < 0 on that interval, so velocity and acceleration disagree in sign and |v| falls."),

 dict(q="For the particle with velocity v(t) = 4 - t^2, the motion for t > 2 is best described as",
   choices=[
     "moving in the negative direction with increasing speed",
     "moving in the negative direction with decreasing speed",
     "moving in the positive direction with increasing speed",
     "at rest"], ans=0,
   why="For t > 2 both v = 4 - t^2 and a = -2t are negative, so the particle moves negatively and speeds up."),

 dict(q="A particle moves along the x-axis with position s(t) = 2t^3 - 21t^2 + 60t for t >= 0. At which time is the particle at rest and changing from moving in the positive direction to moving in the negative direction?",
   choices=[
     "t = 2",
     "t = 2.5",
     "t = 3.5",
     "t = 5"], ans=0,
   why="v(t) = 6(t - 2)(t - 5) is positive before t = 2 and negative just after, while at t = 5 the change is from negative to positive."),

 dict(q="For the particle with position s(t) = 2t^3 - 21t^2 + 60t, the particle is moving in the negative direction while speeding up on the interval",
   choices=[
     "2 < t < 3.5",
     "3.5 < t < 5",
     "0 < t < 2",
     "t > 5"], ans=0,
   why="v = 6(t - 2)(t - 5) is negative on (2, 5) and a(t) = 12t - 42 is negative for t < 3.5, so both are negative exactly on (2, 3.5)."),
]
