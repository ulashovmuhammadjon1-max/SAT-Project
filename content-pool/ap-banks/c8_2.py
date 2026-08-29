# CALC 8.2 Connecting Position, Velocity, and Acceleration Using Integrals
# — 25 questions
# The distinction the AP exam tests hardest: DISPLACEMENT is the integral of v,
# TOTAL DISTANCE is the integral of |v|. Every value is recomputed by sympy in
# verify_c8_2.py, with the sign changes of v located by solving v = 0.
TOPIC = ("8.2", "Connecting Position, Velocity, and Acceleration Using Integrals", 8)
QUESTIONS = [
 dict(q="A particle moves with velocity v(t). What is its displacement over the time interval [a, b]?", choices=[
   "int from a to b of v(t) dt",
   "int from a to b of |v(t)| dt",
   "int from a to b of v'(t) dt",
   "|int from a to b of v(t) dt| divided by (b - a)"], ans=0,
   why="Displacement is the net change in position, which the Fundamental Theorem gives as the integral of the velocity."),
 dict(q="A particle moves with velocity v(t). What is the total distance it travels over [a, b]?", choices=[
   "int from a to b of |v(t)| dt",
   "int from a to b of v(t) dt",
   "|int from a to b of v(t) dt|",
   "int from a to b of a(t) dt"], ans=0,
   why="Total distance adds up motion in both directions, which requires integrating the speed |v(t)|."),
 dict(q="A particle has velocity v(t) = t - 3 for 0 <= t <= 5. What is its displacement?", choices=[
   "-2.5",
   "0",
   "2.5",
   "6.5"], ans=0,
   why="The integral of t - 3 from 0 to 5 is 12.5 - 15 = -2.5."),
 dict(q="A particle has velocity v(t) = t - 3 for 0 <= t <= 5. What is the total distance it travels?", choices=[
   "-2.5",
   "2.5",
   "5",
   "6.5"], ans=3,
   why="The velocity changes sign at t = 3, and the two pieces contribute 4.5 and 2, for a total of 6.5."),
 dict(q="A particle has velocity v(t) = t^2 - 4 for 0 <= t <= 3. What is its displacement?", choices=[
   "-3",
   "3",
   "23/3",
   "9"], ans=0,
   why="The integral of t^2 - 4 from 0 to 3 is 9 - 12 = -3."),
 dict(q="A particle has velocity v(t) = t^2 - 4 for 0 <= t <= 3. What is the total distance it travels?", choices=[
   "7/3",
   "3",
   "16/3",
   "23/3"], ans=3,
   why="The velocity changes sign at t = 2, contributing 16/3 on [0, 2] and 7/3 on [2, 3]."),
 dict(q="A particle has velocity v(t) = sin(t) for 0 <= t <= 2pi. What is its displacement?", choices=[
   "0",
   "2",
   "4",
   "2pi"], ans=0,
   why="The integral of sin over a full period is 0, so the particle ends where it started."),
 dict(q="A particle has velocity v(t) = sin(t) for 0 <= t <= 2pi. What is the total distance it travels?", choices=[
   "4",
   "0",
   "2",
   "2pi"], ans=0,
   why="The velocity changes sign at t = pi, and each half-period contributes 2 to the integral of |sin(t)|."),
 dict(q="A particle has velocity v(t) = 4 - 2t for 0 <= t <= 4. What is its displacement?", choices=[
   "-8",
   "0",
   "4",
   "8"], ans=1,
   why="The integral is 16 - 16 = 0, since the particle returns to its starting position."),
 dict(q="A particle has velocity v(t) = 4 - 2t for 0 <= t <= 4. What is the total distance it travels?", choices=[
   "0",
   "4",
   "8",
   "16"], ans=2,
   why="The velocity changes sign at t = 2, and each piece contributes 4 to the integral of |v|."),
 dict(q="A particle has velocity v(t) = t^2 - 5t + 6 for 0 <= t <= 4. What is its displacement?", choices=[
   "14/3",
   "16/3",
   "17/3",
   "6"], ans=1,
   why="An antiderivative is t^3/3 - 5t^2/2 + 6t, whose value at 4 is 16/3 and at 0 is 0."),
 dict(q="A particle has velocity v(t) = t^2 - 5t + 6 for 0 <= t <= 4. What is the total distance it travels?", choices=[
   "14/3",
   "16/3",
   "17/3",
   "19/3"], ans=2,
   why="The velocity changes sign at t = 2 and t = 3, and the three pieces contribute 14/3, 1/6, and 5/6."),
 dict(q="For a particle moving on a line, when is the total distance traveled equal to the magnitude of the displacement?", choices=[
   "when the velocity does not change sign on the interval",
   "always",
   "only when the velocity is positive",
   "only when the acceleration is zero"], ans=0,
   why="If the particle never reverses direction, all of the motion accumulates in one direction and the two quantities agree."),
 dict(q="A particle has velocity v(t) = 3t^2 and position s(0) = 2. What is s(2)?", choices=[
   "6",
   "8",
   "10",
   "12"], ans=2,
   why="Integrating gives s(t) = t^3 + 2, so s(2) = 8 + 2 = 10."),
 dict(q="A particle has acceleration a(t) = 6t and velocity v(0) = 1. What is v(t)?", choices=[
   "v(t) = 3t^2 + 1",
   "v(t) = 6t^2 + 1",
   "v(t) = 3t^2",
   "v(t) = 6 + t"], ans=0,
   why="Antidifferentiating 6t gives 3t^2 + C, and v(0) = C = 1."),
 dict(q="For a particle moving on a line, int from a to b of a(t) dt represents", choices=[
   "the change in velocity from time a to time b",
   "the change in position from time a to time b",
   "the total distance traveled",
   "the average acceleration"], ans=0,
   why="The Fundamental Theorem applied to the acceleration returns v(b) - v(a)."),
 dict(q="The speed of a particle at time t is", choices=[
   "|v(t)|",
   "v(t)",
   "a(t)",
   "v'(t)"], ans=0,
   why="Speed is the magnitude of velocity and is never negative."),
 dict(q="A particle moving on a horizontal line is moving to the left exactly when", choices=[
   "v(t) < 0",
   "a(t) < 0",
   "s(t) < 0",
   "|v(t)| < 0"], ans=0,
   why="The sign of the velocity gives the direction of motion."),
 dict(q="A particle's speed is increasing at time t exactly when", choices=[
   "v(t) and a(t) have the same sign",
   "a(t) > 0",
   "v(t) > 0",
   "v(t) and a(t) have opposite signs"], ans=0,
   why="Speed grows when the acceleration pushes in the direction the particle is already moving."),
 dict(q="A ball is thrown upward with a(t) = -32 feet per second squared and v(0) = 64 feet per second. At what time does it reach its greatest height?", choices=[
   "t = 2 seconds",
   "t = 4 seconds",
   "t = 32 seconds",
   "t = 1 second"], ans=0,
   why="Integrating gives v(t) = 64 - 32t, which is zero at t = 2, where the motion turns around."),
 dict(q="Which statement is the Net Change Theorem applied to motion?", choices=[
   "s(b) - s(a) = int from a to b of v(t) dt",
   "s(b) - s(a) = int from a to b of |v(t)| dt",
   "v(b) - v(a) = int from a to b of v(t) dt",
   "s(b) = int from a to b of v(t) dt"], ans=0,
   why="Integrating a rate of change over an interval gives the net change in the accumulated quantity."),
 dict(q="A particle has velocity v(t) = e^t - 1 for 0 <= t <= 2. What is the total distance it travels?", choices=[
   "e^2 - 3",
   "e^2 - 1",
   "e^2 + 1",
   "e^2 - 2"], ans=0,
   why="The velocity is nonnegative on this interval, so the distance equals the displacement e^2 - 1 - 2."),
 dict(q="A particle has velocity v(t) = 2t - 6 and position s(0) = 4. What is s(5)?", choices=[
   "-5",
   "-1",
   "1",
   "9"], ans=1,
   why="Integrating gives s(t) = t^2 - 6t + 4, so s(5) = 25 - 30 + 4 = -1."),
 dict(q="A particle has velocity v(t) = t - 3 for 0 <= t <= 5. What are its average velocity and its average speed on that interval?", choices=[
   "average velocity -0.5 and average speed 1.3",
   "average velocity 1.3 and average speed -0.5",
   "both are -0.5",
   "both are 1.3"], ans=0,
   why="Average velocity is the displacement -2.5 divided by 5, and average speed is the total distance 6.5 divided by 5."),
 dict(q="To find the total distance a particle travels on [0, 5] when v(t) = t - 3, a student computes int from 0 to 5 of (t - 3) dt and reports 2.5 after taking an absolute value at the end. What is the error?", choices=[
   "the absolute value must be applied to v(t) inside the integral, before integrating, since v changes sign at t = 3",
   "the antiderivative of t - 3 is wrong",
   "the limits of integration should be reversed",
   "there is no error"], ans=0,
   why="Taking the absolute value after integrating lets the negative and positive portions cancel, which is exactly what total distance must not do."),
]
