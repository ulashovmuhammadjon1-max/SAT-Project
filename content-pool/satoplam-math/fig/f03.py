import math
import matplotlib.pyplot as plt
from fh6_lib import emit

BLK = dict(color="black", lw=1.1)


def ra(ax, v, d1, d2, s=0.075):
    """right-angle square at vertex v along unit directions d1, d2"""
    ax.plot([v[0] + d1[0] * s, v[0] + (d1[0] + d2[0]) * s, v[0] + d2[0] * s],
            [v[1] + d1[1] * s, v[1] + (d1[1] + d2[1]) * s, v[1] + d2[1] * s], **BLK)


def angle_pt(w, h, d=0.32):
    """point inside the triangle, on the bisector of the bottom-right angle"""
    import math as _m
    u1 = (-1.0, 0.0)
    L = _m.hypot(w, h)
    u2 = (-w / L, h / L)
    bx, by = u1[0] + u2[0], u1[1] + u2[1]
    n = _m.hypot(bx, by)
    return (w + d * bx / n, d * by / n)


def tri(w, h, figsize=(4.8, 3.4)):
    """right triangle: apex top-left (0,h), right angle bottom-left (0,0),
    bottom-right (w,0)."""
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot([0, w, 0, 0], [0, 0, h, 0], **BLK)
    ra(ax, (0, 0), (1, 0), (0, 1))
    ax.set_xlim(-0.30, w + 0.30)
    ax.set_ylim(-0.34, h + 0.24)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


# ------------------------------------------------------------ trigonometry-1
# A top-left, B bottom-left (right angle), C bottom-right; AB = 23, AC = 43.
# Drawn to scale: BC = sqrt(43^2 - 23^2) ~= 36.33
h = 1.0
w = math.sqrt(43 ** 2 - 23 ** 2) / 23.0
fig, ax = tri(w, h)
ax.text(-0.02, h + 0.07, "$A$", ha="right", va="bottom", fontsize=13)
ax.text(-0.05, -0.05, "$B$", ha="right", va="top", fontsize=13)
ax.text(w + 0.05, -0.05, "$C$", ha="left", va="top", fontsize=13)
ax.text(-0.08, h / 2, "23", ha="right", va="center", fontsize=12)
ax.text(w / 2 - 0.06, h / 2 + 0.10, "43", ha="center", va="bottom", fontsize=12)
emit(fig, "satmath-ma3-trigonometry-1",
     "A right triangle with vertex A at the top left, B at the lower left where the "
     "right angle is marked, and C at the lower right. The vertical leg and the "
     "hypotenuse each carry a length label.")

# ------------------------------------------------------------ trigonometry-3
# J top-left, K bottom-left (right angle), L bottom-right; 55 is the hypotenuse
# JL, y degrees is the angle at L.  Printed proportions kept (book prints
# "Note: Figure not drawn to scale."); drawing to scale would leak KL.
w, h = 1.35, 1.0
fig, ax = tri(w, h)
ax.text(-0.02, h + 0.07, "$J$", ha="right", va="bottom", fontsize=13)
ax.text(-0.05, -0.05, "$K$", ha="left", va="top", fontsize=13)
ax.text(w + 0.05, -0.05, "$L$", ha="left", va="top", fontsize=13)
ax.text(w / 2 + 0.06, h / 2 + 0.10, "55", ha="center", va="bottom", fontsize=12)
_p = angle_pt(w, h); ax.text(_p[0], _p[1], r"$y^{\circ}$", ha="center", va="center", fontsize=12)
fig.text(0.5, 0.005, "Note: Figure not drawn to scale.", ha="center", fontsize=10)
emit(fig, "satmath-ma3-trigonometry-3",
     "A right triangle with vertex J at the top left, K at the lower left where the "
     "right angle is marked, and L at the lower right. The hypotenuse carries a "
     "length label and the angle at L is labelled y degrees.",
     note="On the page the length 55 is printed on top of the right-angle mark at "
          "K, overlapping it, rather than beside a side. Redrawn with 55 beside the "
          "hypotenuse JL, which is the only reading the arithmetic supports.")

# ------------------------------------------------------------ trigonometry-5
# Q top-left, R bottom-left (right angle), S bottom-right; QR = 4, RS = 10,
# hypotenuse QS = c, y degrees at S. Printed proportions kept ("not to scale").
w, h = 1.35, 1.0
fig, ax = tri(w, h)
ax.text(-0.02, h + 0.07, "$Q$", ha="right", va="bottom", fontsize=13)
ax.text(-0.05, -0.05, "$R$", ha="left", va="top", fontsize=13)
ax.text(w + 0.05, -0.05, "$S$", ha="left", va="top", fontsize=13)
ax.text(-0.08, h / 2, "4", ha="right", va="center", fontsize=12)
ax.text(w / 2, -0.09, "10", ha="center", va="top", fontsize=12)
ax.text(w / 2 + 0.06, h / 2 + 0.10, "$c$", ha="center", va="bottom", fontsize=12)
_p = angle_pt(w, h); ax.text(_p[0], _p[1], r"$y^{\circ}$", ha="center", va="center", fontsize=12)
fig.text(0.5, 0.005, "Note: Figure not drawn to scale.", ha="center", fontsize=10)
emit(fig, "satmath-ma3-trigonometry-5",
     "A right triangle with vertex Q at the top left, R at the lower left where the "
     "right angle is marked, and S at the lower right. The two legs carry numbers, "
     "the hypotenuse is labelled c, and the angle at S is labelled y degrees.",
     note="On the page the hypotenuse label c is printed on top of the right-angle "
          "mark at R rather than beside the hypotenuse; redrawn beside QS, the only "
          "side it can belong to since both legs already carry numbers.")

# ------------------------------------------------------------ trigonometry-6
# Same triangle QRS; QR = 4, RS = 9, hypotenuse c, y at S. Drawn to scale.
h = 1.0
w = 9.0 / 4.0
fig, ax = tri(w, h, figsize=(5.0, 3.0))
ax.text(-0.02, h + 0.07, "$Q$", ha="right", va="bottom", fontsize=13)
ax.text(-0.05, -0.05, "$R$", ha="left", va="top", fontsize=13)
ax.text(w + 0.05, -0.05, "$S$", ha="left", va="top", fontsize=13)
ax.text(-0.08, h / 2, "4", ha="right", va="center", fontsize=12)
ax.text(w / 2, -0.09, "9", ha="center", va="top", fontsize=12)
ax.text(w / 2 + 0.10, h / 2 + 0.08, "$c$", ha="center", va="bottom", fontsize=12)
_p = angle_pt(w, h, 0.42); ax.text(_p[0], _p[1], "$y$", ha="center", va="center", fontsize=12)
emit(fig, "satmath-ma3-trigonometry-6",
     "A right triangle with vertex Q at the top left, R at the lower left where the "
     "right angle is marked, and S at the lower right. The two legs carry numbers, "
     "the hypotenuse is labelled c, and the angle at S is labelled y.",
     note="The printed labels are misplaced: 4 and 9 are both crowded at vertex R "
          "and c sits on top of the right-angle mark. Redrawn with 4 on leg QR, 9 "
          "on leg RS and c on the hypotenuse, which is the only assignment the "
          "answer choices allow.")

# ------------------------------------------------------------ trigonometry-7
# J top-left, K bottom-left (right angle), L bottom-right; 59 is hypotenuse JL,
# y at L. Printed proportions kept; drawing to scale would leak KL.
w, h = 1.35, 1.0
fig, ax = tri(w, h)
ax.text(-0.02, h + 0.07, "$J$", ha="right", va="bottom", fontsize=13)
ax.text(-0.05, -0.05, "$K$", ha="left", va="top", fontsize=13)
ax.text(w + 0.05, -0.05, "$L$", ha="left", va="top", fontsize=13)
ax.text(w / 2 + 0.06, h / 2 + 0.10, "59", ha="center", va="bottom", fontsize=12)
_p = angle_pt(w, h); ax.text(_p[0], _p[1], "$y$", ha="center", va="center", fontsize=12)
emit(fig, "satmath-ma3-trigonometry-7",
     "A right triangle with vertex J at the top left, K at the lower left where the "
     "right angle is marked, and L at the lower right. The hypotenuse carries a "
     "length label and the angle at L is labelled y.",
     note="On the page the length 59 is printed on top of the right-angle mark at "
          "K rather than beside a side. Redrawn with 59 beside the hypotenuse JL, "
          "the only reading the arithmetic supports. The figure is deliberately not "
          "drawn to scale, since a to-scale drawing would give away KL.")
