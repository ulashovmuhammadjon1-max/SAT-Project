import math
import matplotlib.pyplot as plt
from fh6_lib import emit

BLK = dict(color="black", lw=1.1)


def right_angle(ax, vertex, d1, d2, size=0.055, scale=1.0):
    """small square at `vertex`, along unit directions d1, d2 (data coords)."""
    s = size * scale
    vx, vy = vertex
    p1 = (vx + d1[0] * s, vy + d1[1] * s)
    p2 = (vx + d1[0] * s + d2[0] * s, vy + d1[1] * s + d2[1] * s)
    p3 = (vx + d2[0] * s, vy + d2[1] * s)
    ax.plot([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], **BLK)


# ---------------------------------------------------------------- triangles-2
# C bottom-left, B bottom-right (right angle), A top-right.  Drawn to scale
# for AB = 29, AC = 47  ->  CB = sqrt(47^2 - 29^2) ~= 37.0
CB = math.sqrt(47 ** 2 - 29 ** 2) / 29.0   # in units where AB = 1
fig, ax = plt.subplots(figsize=(4.8, 3.2))
C, B, A = (0.0, 0.0), (CB, 0.0), (CB, 1.0)
ax.plot([C[0], B[0], A[0], C[0]], [C[1], B[1], A[1], C[1]], **BLK)
right_angle(ax, B, (-1, 0), (0, 1), size=0.075)
ax.text(C[0] - 0.06, C[1], "$C$", ha="right", va="center", fontsize=13)
ax.text(B[0], B[1] - 0.08, "$B$", ha="center", va="top", fontsize=13)
ax.text(A[0] + 0.05, A[1] + 0.05, "$A$", ha="left", va="bottom", fontsize=13)
ax.text(A[0] + 0.05, 0.5, "29", ha="left", va="center", fontsize=12)
ax.text(CB / 2 - 0.10, 0.55, "47", ha="right", va="center", fontsize=12)
ax.set_xlim(-0.28, CB + 0.30)
ax.set_ylim(-0.28, 1.28)
ax.set_aspect("equal")
ax.axis("off")
emit(fig, "satmath-ma3-triangles-2",
     "A right triangle with vertices labelled C at the lower left, B at the lower "
     "right where the right angle is marked, and A at the top right. The vertical "
     "leg and the hypotenuse each carry a length label.",
     note="The printed figure carries NO side lengths, so the question is "
          "unanswerable as printed; the labels 29 (leg AB) and 47 (hypotenuse AC) "
          "were restored because the four answer choices are consistent with no "
          "other assignment. Added labels, flagged per the brief.")

# ---------------------------------------------------------------- triangles-9
# right angle at bottom-left; vertical leg labelled a, base 12, hypotenuse 14.
# Book prints "Note: Figure not drawn to scale"; printed shape is base:height
# about 225:195, which is reproduced rather than the true 12:sqrt(52).
w, h = 1.15, 1.0
fig, ax = plt.subplots(figsize=(4.8, 3.4))
P0, P1, P2 = (0.0, 0.0), (w, 0.0), (0.0, h)
ax.plot([P0[0], P1[0], P2[0], P0[0]], [P0[1], P1[1], P2[1], P0[1]], **BLK)
right_angle(ax, P0, (1, 0), (0, 1), size=0.075)
ax.text(-0.06, h / 2, "$a$", ha="right", va="center", fontsize=13)
ax.text(w / 2, -0.08, "12", ha="center", va="top", fontsize=12)
ax.text(w / 2 + 0.10, h / 2 + 0.09, "14", ha="left", va="bottom", fontsize=12)
ax.set_xlim(-0.30, w + 0.22)
ax.set_ylim(-0.34, h + 0.16)
ax.set_aspect("equal")
ax.axis("off")
fig.text(0.5, 0.005, "Note: Figure not drawn to scale", ha="center", fontsize=10)
emit(fig, "satmath-ma3-triangles-9",
     "A right triangle with the right angle at the lower left. The vertical leg is "
     "labelled a and the horizontal leg and hypotenuse each carry a number.")

# --------------------------------------------------------------- triangles-10
# X top-left, Y bottom-left (right angle), Z bottom-right, 35 degrees at Z.
w, h = 1.05, 1.0
fig, ax = plt.subplots(figsize=(4.8, 3.4))
Y, Z, X = (0.0, 0.0), (w, 0.0), (0.0, h)
ax.plot([Y[0], Z[0], X[0], Y[0]], [Y[1], Z[1], X[1], Y[1]], **BLK)
right_angle(ax, Y, (1, 0), (0, 1), size=0.075)
ax.text(-0.05, -0.05, "$Y$", ha="right", va="top", fontsize=13)
ax.text(w + 0.05, -0.05, "$Z$", ha="left", va="top", fontsize=13)
ax.text(-0.02, h + 0.06, "$X$", ha="right", va="bottom", fontsize=13)
ax.text(w - 0.12, 0.09, r"$35^{\circ}$", ha="right", va="bottom", fontsize=12)
ax.set_xlim(-0.26, w + 0.26)
ax.set_ylim(-0.32, h + 0.22)
ax.set_aspect("equal")
ax.axis("off")
fig.text(0.5, 0.005, "Note: Figure not drawn to scale", ha="center", fontsize=10)
emit(fig, "satmath-ma3-triangles-10",
     "A right triangle with vertices X at the top left, Y at the lower left where "
     "the right angle is marked, and Z at the lower right; the angle at Z is "
     "labelled with its degree measure.")
