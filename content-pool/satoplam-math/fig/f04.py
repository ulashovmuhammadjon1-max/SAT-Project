import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from fh6_lib import emit

BLK = dict(color="black", lw=1.2)

# boxplot: min 85, Q1 97, median 114, Q3 124, max 138
lo, q1, med, q3, hi = 85, 97, 114, 124, 138
fig, ax = plt.subplots(figsize=(5.4, 1.9))
y, hh = 1.0, 0.30
ax.plot([q1, q3, q3, q1, q1], [y - hh, y - hh, y + hh, y + hh, y - hh], **BLK)
ax.plot([med, med], [y - hh, y + hh], **BLK)
ax.plot([lo, q1], [y, y], **BLK)
ax.plot([q3, hi], [y, y], **BLK)
ax.plot([lo, lo], [y - hh * 0.8, y + hh * 0.8], **BLK)
ax.plot([hi, hi], [y - hh * 0.8, y + hh * 0.8], **BLK)

ax.set_xlim(80, 140)
ax.set_ylim(0.3, 1.75)
ax.set_yticks([])
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(5))
ax.tick_params(axis="x", which="both", direction="out", top=False)
for side in ("top", "left", "right"):
    ax.spines[side].set_visible(False)
ax.spines["bottom"].set_position(("data", 0.42))
ax.spines["bottom"].set_linewidth(1.1)
fig.text(0.5, -0.02, "Number of units sold per day", ha="center",
         fontsize=11, fontweight="bold")

emit(fig, "satmath-ma2-mean-median-mode-range-14",
     "A boxplot drawn above a horizontal number line running from 80 to 140, "
     "captioned Number of units sold per day.")
