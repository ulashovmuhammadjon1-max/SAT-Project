import matplotlib.pyplot as plt
from fh6_lib import emit

A = {4: 1, 5: 2, 6: 3, 7: 4, 8: 3, 9: 2, 10: 1}
B = {4: 2, 5: 3, 6: 4, 7: 3, 8: 2, 9: 1, 10: 1}

fig, axes = plt.subplots(1, 2, figsize=(6.2, 2.4))
for ax, counts, title in zip(axes, (A, B), ("Data Set A", "Data Set B")):
    ax.plot([3.6, 10.4], [0, 0], color="black", lw=1.6)
    for v, n in counts.items():
        for i in range(n):
            ax.plot([v], [0.35 + 0.42 * i], "o", color="black", ms=4.5)
    for v in range(4, 11):
        ax.text(v, -0.45, str(v), ha="center", va="top", fontsize=10)
    ax.set_title(title, fontsize=11, fontweight="bold", pad=8)
    ax.set_xlim(3.3, 10.7)
    ax.set_ylim(-1.3, 2.7)
    ax.set_aspect(0.9)
    ax.axis("off")

fig.subplots_adjust(wspace=0.15)
emit(fig, "satmath-ma3-mean-median-mode-range-1",
     "Two dot plots side by side, headed Data Set A and Data Set B. Each is a "
     "number line from 4 to 10 with a stack of dots above the values.")
