import numpy as np
import matplotlib.pyplot as plt
from fh6_lib import emit

GRID = dict(color="0.80", lw=0.55)
LINE = dict(color="black", lw=1.9, solid_capstyle="butt")

# ============================================================ linear-functions-52
# x-axis drawn along the top of the window, y-axis along the right.
fig, ax = plt.subplots(figsize=(5.0, 4.4))
XLO, XHI, YLO, YHI = -14.7, 0.45, -13.7, 0.45
for gx in range(-14, 0, 2):
    ax.plot([gx, gx], [YLO, YHI], **GRID)
for gy in range(-13, 0, 2):
    ax.plot([XLO, XHI], [gy, gy], **GRID)
ax.annotate("", xy=(XHI + 0.55, 0), xytext=(XLO, 0),
            arrowprops=dict(arrowstyle="-|>", color="black", lw=1.1))
ax.annotate("", xy=(0, YHI + 0.55), xytext=(0, YLO),
            arrowprops=dict(arrowstyle="-|>", color="black", lw=1.1))
for t in range(-14, 0, 2):
    ax.plot([t, t], [-0.16, 0.16], color="black", lw=1.0)
    ax.text(t, -0.36, "$-%d$" % abs(t), ha="center", va="top", fontsize=11)
for t in range(-13, 0, 2):
    ax.plot([-0.20, 0.20], [t, t], color="black", lw=1.0)
    ax.text(-0.38, t, "$-%d$" % abs(t), ha="right", va="center", fontsize=11)
ax.plot([-14, 0], [0, -13], **LINE)
ax.plot([-14, 0], [0, -13], "o", color="black", ms=6)
ax.set_xlim(XLO - 0.8, XHI + 1.2)
ax.set_ylim(YLO - 0.8, YHI + 1.2)
ax.axis("off")
emit(fig, "satmath-ma2-linear-functions-52",
     "A line segment drawn on a grid whose x-axis runs along the top of the window "
     "and whose y-axis runs down the right-hand side; both axes are labelled with "
     "negative values and the two endpoints of the segment are marked with solid "
     "dots.")


# ============================================================ linear-functions-16
def panel16(ax, slope, intercept):
    for gx in range(4, 21, 4):
        ax.plot([gx, gx], [0, 600], **GRID)
    for gy in range(100, 601, 100):
        ax.plot([0, 20], [gy, gy], **GRID)
    ax.annotate("", xy=(23.0, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="black", lw=1.4))
    ax.annotate("", xy=(0, 660), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="black", lw=1.4))
    for t in range(4, 21, 4):
        ax.plot([t, t], [-14, 14], color="black", lw=1.0)
        ax.text(t, -40, "$%d$" % t, ha="center", va="top", fontsize=9)
    for t in range(100, 601, 100):
        ax.plot([-0.35, 0.35], [t, t], color="black", lw=1.0)
        ax.text(-0.7, t, "$%d$" % t, ha="right", va="center", fontsize=9)
    ax.text(23.2, 45, "$x$", ha="center", va="bottom", fontsize=10)
    ax.text(0.7, 655, "$y$", ha="left", va="center", fontsize=10)
    x = np.linspace(0, 20, 50)
    ax.plot(x, intercept + slope * x, **LINE)
    ax.set_xlim(-5.5, 25.5)
    ax.set_ylim(-135, 730)
    ax.axis("off")


fig, axes = plt.subplots(2, 2, figsize=(7.0, 5.0))
(a1, a2), (a3, a4) = axes
panel16(a1, -5, 500)      # A  y = -5x + 500
panel16(a2, -25, 500)     # B  falls to 0 at x = 20
panel16(a3, 0, 500)       # C  horizontal at 500
panel16(a4, 5, 500)       # D  rises to 600 at x = 20
for ax, lab in zip((a1, a2, a3, a4), ("A)", "B)", "C)", "D)")):
    ax.text(0.0, 1.0, lab, transform=ax.transAxes, ha="left", va="top", fontsize=12)
fig.subplots_adjust(wspace=0.05, hspace=0.10)
emit(fig, "satmath-ma2-linear-functions-16",
     "Four coordinate grids labelled A) to D), each showing a single straight line. "
     "The horizontal axis is labelled x with ticks up to 20 and the vertical axis "
     "is labelled y with ticks up to 600.",
     note="The four answer choices ARE these graphs, so all four are supplied as a "
          "single labelled image and the choice texts stay A/B/C/D.")


# ============================================================ linear-functions-80
def panel80(ax, xhi, yhi, xstep, ystep, xgrid, ygrid, pts, x0=None):
    x0 = xstep if x0 is None else x0
    for gx in np.arange(x0, xhi + 1e-9, xgrid):
        ax.plot([gx, gx], [0, yhi], **GRID)
    for gy in np.arange(ygrid, yhi + 1e-9, ygrid):
        ax.plot([0, xhi], [gy, gy], **GRID)
    ax.annotate("", xy=(xhi * 1.14, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="black", lw=1.3))
    ax.annotate("", xy=(0, yhi * 1.10), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="black", lw=1.3))
    for t in np.arange(x0, xhi + 1e-9, xstep):
        ax.plot([t, t], [-yhi * 0.022, yhi * 0.022], color="black", lw=0.9)
        ax.text(t, -yhi * 0.06, "$%d$" % t, ha="center", va="top", fontsize=8)
    for t in np.arange(ystep, yhi + 1e-9, ystep):
        ax.plot([-xhi * 0.018, xhi * 0.018], [t, t], color="black", lw=0.9)
        ax.text(-xhi * 0.035, t, "$%d$" % t, ha="right", va="center", fontsize=8)
    ax.text(xhi * 1.16, yhi * 0.06, "$x$", ha="center", va="bottom", fontsize=9)
    ax.text(xhi * 0.035, yhi * 1.09, "$y$", ha="left", va="center", fontsize=9)
    ax.text(-xhi * 0.035, -yhi * 0.055, "$O$", ha="right", va="top", fontsize=10)
    ax.plot([p[0] for p in pts], [p[1] for p in pts], **LINE)
    ax.set_xlim(-xhi * 0.30, xhi * 1.26)
    ax.set_ylim(-yhi * 0.20, yhi * 1.20)
    ax.axis("off")
    ax.set_xlabel("Number of oak trees", fontsize=9, labelpad=2)


fig, axes = plt.subplots(2, 2, figsize=(7.4, 6.2))
(a1, a2), (a3, a4) = axes
panel80(a1, 40, 40, 5, 5, 5, 5, [(0, 15), (20, 0)])
panel80(a2, 40, 40, 5, 5, 5, 5, [(0, 20), (15, 0)])
panel80(a3, 19, 20, 4, 2, 4, 4, [(0, 15), (15, 0)], x0=2)
panel80(a4, 19, 20, 4, 2, 4, 4, [(0, 0), (15.75, 21.0)], x0=2)
for ax, lab in zip((a1, a2, a3, a4), ("A)", "B)", "C)", "D)")):
    ax.text(-0.02, 1.02, lab, transform=ax.transAxes, ha="left", va="top",
            fontsize=12)
    ax.text(0.55, -0.10, "Number of oak trees", transform=ax.transAxes,
            ha="center", va="top", fontsize=9)
    ax.text(-0.12, 0.55, "Number of pine trees", transform=ax.transAxes,
            ha="center", va="center", rotation=90, fontsize=9)
fig.subplots_adjust(wspace=0.28, hspace=0.32)
emit(fig, "satmath-ma2-linear-functions-80",
     "Four coordinate grids labelled A) to D), each showing a single straight line. "
     "On every grid the horizontal axis is labelled Number of oak trees and the "
     "vertical axis is labelled Number of pine trees.",
     note="The four answer choices ARE these graphs, so all four are supplied as a "
          "single labelled image and the choice texts stay A/B/C/D. Choice D's line "
          "runs off the top of its window in the book, and is drawn that way here.")
