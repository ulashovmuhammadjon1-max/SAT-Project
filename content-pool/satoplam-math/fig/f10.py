import numpy as np
import matplotlib.pyplot as plt
from fh6_lib import emit

GRID = dict(color="0.82", lw=0.6)

XS = [2, 4, 6, 7, 9]
YS = [265, 330, 420, 460, 525]
YB = 75.0          # the printed horizontal axis sits above y = 0
YTOP = 600.0

fig, ax = plt.subplots(figsize=(5.2, 3.8))
for gx in (2, 4, 6, 8, 10):
    ax.plot([gx, gx], [YB, 590], **GRID)
for gy in (225, 375, 525):
    ax.plot([0, 10.5], [gy, gy], **GRID)

x = np.array([0.0, 10.2])
ax.plot(x, 180 + 39.0 * x, color="black", lw=1.4)
ax.plot(XS, YS, "o", color="black", ms=5)

ax.annotate("", xy=(11.1, YB), xytext=(0, YB),
            arrowprops=dict(arrowstyle="-|>", color="black", lw=1.1))
ax.annotate("", xy=(0, YTOP + 25), xytext=(0, YB),
            arrowprops=dict(arrowstyle="-|>", color="black", lw=1.1))
for t in (2, 4, 6, 8, 10):
    ax.plot([t, t], [YB - 11, YB + 11], color="black", lw=1.0)
    ax.text(t, YB - 30, "$%d$" % t, ha="center", va="top", fontsize=12)
for t in (225, 375, 525):
    ax.plot([-0.13, 0.13], [t, t], color="black", lw=1.0)
    ax.text(-0.3, t, "$%d$" % t, ha="right", va="center", fontsize=12)

ax.text(0.35, 578, "Temperature ($^{\\circ}$F)", ha="left", va="top", fontsize=12)
ax.text(10.4, 120, "Time (hours)", ha="right", va="bottom", fontsize=12)

ax.set_xlim(-2.0, 11.6)
ax.set_ylim(YB - 105, YTOP + 55)
ax.axis("off")

emit(fig, "satmath-ma3-scatterplots-9",
     "A scatterplot with a line of best fit drawn through the points. The "
     "horizontal axis is labelled Time (hours) and the vertical axis is labelled "
     "Temperature in degrees Fahrenheit.",
     note="Drawn from the page. The printed vertical axis does not start at zero "
          "and is only labelled 225, 375 and 525, so it is reproduced that way. "
          "The page confirms the line of best fit rises by roughly 40 degrees F per "
          "hour, which is the value the book drops from choice C.")
