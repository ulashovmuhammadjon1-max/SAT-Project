import numpy as np
import matplotlib.pyplot as plt
from fh6_lib import emit

GRID = dict(color="0.80", lw=0.55)
CURVE = dict(color="black", lw=2.0, solid_capstyle="round")


def panel(ax, xlo, xhi, ylo, yhi, xticks, yticks):
    for gx in np.arange(np.ceil(xlo), xhi + 1e-9):
        ax.plot([gx, gx], [ylo, yhi], **GRID)
    for gy in np.arange(np.ceil(ylo), yhi + 1e-9):
        ax.plot([xlo, xhi], [gy, gy], **GRID)
    ax.annotate("", xy=(xhi + 0.55, 0), xytext=(xlo, 0),
                arrowprops=dict(arrowstyle="-|>", color="black", lw=1.0))
    ax.annotate("", xy=(0, yhi + 0.55), xytext=(0, ylo),
                arrowprops=dict(arrowstyle="-|>", color="black", lw=1.0))
    for t in xticks:
        ax.plot([t, t], [-0.13, 0.13], color="black", lw=1.0)
        ax.text(t, -0.35, "$%d$" % t, ha="center", va="top", fontsize=9)
    for t in yticks:
        ax.plot([-0.13, 0.13], [t, t], color="black", lw=1.0)
        ax.text(-0.28, t, "$%d$" % t, ha="right", va="center", fontsize=9)
    ax.text(xhi + 0.35, 0.45, "$x$", ha="center", va="bottom", fontsize=10)
    ax.text(0.42, yhi + 0.30, "$y$", ha="left", va="center", fontsize=10)
    ax.set_xlim(xlo - 0.9, xhi + 1.3)
    ax.set_ylim(ylo - 1.0, yhi + 1.2)
    ax.axis("off")


fig, axes = plt.subplots(2, 2, figsize=(7.0, 5.2))
(a1, a2), (a3, a4) = axes

# A) y = 2*sqrt(x)
panel(a1, 0, 10.4, 0, 6.4, [2, 4, 6, 8, 10], [2, 4, 6])
x = np.linspace(0, 10.4, 300)
a1.plot(x, 2 * np.sqrt(x), **CURVE)

# B) y = sqrt(2x)
panel(a2, 0, 10.4, 0, 6.4, [2, 4, 6, 8, 10], [2, 4, 6])
a2.plot(x, np.sqrt(2 * x), **CURVE)

# C) y = sqrt(x+1) - 1
panel(a3, -2.5, 9.4, -2.5, 4.4, [-2, 2, 4, 6, 8], [-2, 2, 4])
x2 = np.linspace(-1, 9.4, 300)
a3.plot(x2, np.sqrt(x2 + 1) - 1, **CURVE)

# D) y = 2*sqrt(x+1) - 2
panel(a4, -2.5, 9.4, -2.5, 4.4, [-2, 2, 4, 6, 8], [-2, 2, 4])
a4.plot(x2, 2 * np.sqrt(x2 + 1) - 2, **CURVE)

for ax, lab in zip((a1, a2, a3, a4), ("A)", "B)", "C)", "D)")):
    ax.text(0.0, 1.0, lab, transform=ax.transAxes, ha="left", va="top",
            fontsize=12)

fig.subplots_adjust(wspace=0.08, hspace=0.12)
emit(fig, "satmath-ma2-functions-function-notation-5",
     "Four coordinate grids labelled A) to D), each showing one increasing "
     "square-root-shaped curve plotted against an x-axis and a y-axis.",
     note="The four answer choices ARE these graphs, so all four are supplied as a "
          "single labelled image and the choice texts stay A/B/C/D. Two readings in "
          "the recorded spec are wrong against the page: choice C passes through the "
          "origin (it is y = sqrt(x+1) - 1, starting at (-1,-1)), not crossing the "
          "y-axis near y = 1; and choice D starts at (-1,-2), not at (0,-2) (it is "
          "y = 2*sqrt(x+1) - 2). A and B are as recorded: y = 2*sqrt(x) and "
          "y = sqrt(2x). Drawn from the page.")
