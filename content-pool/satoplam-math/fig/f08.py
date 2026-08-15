import matplotlib.pyplot as plt
from fh6_lib import emit

BLK = dict(color="black", lw=1.2)


def dotplot(counts, lo, hi, ticks, figsize, caption=None, dot=6.0, step=0.62):
    fig, ax = plt.subplots(figsize=figsize)
    ax.annotate("", xy=(hi + 0.6, 0), xytext=(lo - 0.6, 0),
                arrowprops=dict(arrowstyle="-|>", color="black", lw=1.1))
    for t in ticks:
        ax.plot([t, t], [-0.16, 0.16], **BLK)
        ax.text(t, -0.45, str(t), ha="center", va="top", fontsize=11)
    for v, n in counts.items():
        for i in range(n):
            ax.plot([v], [0.55 + step * i], "o", color="black", ms=dot)
    ax.set_xlim(lo - 1.0, hi + 1.0)
    ax.set_ylim(-1.6, 0.55 + step * (max(counts.values()) - 1) + 0.7)
    ax.axis("off")
    if caption:
        fig.text(0.5, 0.0, caption, ha="center", va="top", fontsize=11,
                 fontweight="bold", linespacing=1.35)
    return fig


# ------------------------------------------------- mean-median-mode-range-2
c2 = {167: 1, 168: 3, 170: 1, 171: 3, 173: 4, 174: 1, 178: 2}
fig = dotplot(c2, 166.4, 178.6, [168, 170, 172, 174, 176, 178], (5.4, 3.0),
              caption="Estimated market value\n(in thousand of dollars)")
emit(fig, "satmath-ma2-mean-median-mode-range-2",
     "A dot plot on a horizontal number line with tick labels from 168 to 178, "
     "captioned Estimated market value in thousand of dollars.",
     note="The caption is reproduced exactly as printed, including the book's "
          "\"in thousand of dollars\".")

# ------------------------------------------------- mean-median-mode-range-3
c3 = {38: 2, 39: 1, 40: 3, 41: 2, 46: 1}
fig = dotplot(c3, 37.6, 46.4, list(range(38, 47)), (5.4, 2.3))
emit(fig, "satmath-ma2-mean-median-mode-range-3",
     "A dot plot on a horizontal number line with a tick at every whole number "
     "from 38 to 46.")
