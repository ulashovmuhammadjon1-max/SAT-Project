import numpy as np
import matplotlib.pyplot as plt
from fh6_lib import emit

GRID = dict(color="0.85", lw=0.5)
BLK = dict(color="black", lw=1.3)

fig, ax = plt.subplots(figsize=(5.0, 3.9))

# light graph-paper grid over the plotted region
for gx in np.arange(0, 24.001, 1.0):
    ax.plot([gx, gx], [0, 350], **GRID)
for gy in np.arange(0, 350.001, 10.0):
    ax.plot([0, 24], [gy, gy], **GRID)

x = np.linspace(0, 24, 400)
y = 275.0 * (75.0 / 275.0) ** (x / 24.0)
ax.plot(x, y, **BLK)
ax.plot([0, 24], [275, 75], "o", color="black", ms=5)
ax.text(1.0, 288, "$(0, 275)$", ha="left", va="bottom", fontsize=11)
ax.text(24.6, 88, "$(24, 75)$", ha="right", va="bottom", fontsize=11)

# axes as arrows through the origin
ax.annotate("", xy=(25.6, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle="-|>", color="black", lw=1.1))
ax.annotate("", xy=(0, 372), xytext=(0, 0),
            arrowprops=dict(arrowstyle="-|>", color="black", lw=1.1))

ax.set_xticks(range(0, 25, 4))
ax.set_yticks(range(0, 351, 50))
ax.set_yticklabels(["$\\$\\,%d$" % v for v in range(0, 351, 50)])
ax.tick_params(axis="both", direction="out", length=4, top=False, right=False,
               labelsize=11)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.set_xlim(-0.6, 26.4)
ax.set_ylim(-14, 385)

emit(fig, "satmath-ma3-functions-function-notation-19",
     "A decreasing curve on a grid. The horizontal axis is the number of months "
     "since purchase, from 0 to 24, and the vertical axis is the estimated value in "
     "dollars. The endpoints of the curve are labelled with their coordinates.")
