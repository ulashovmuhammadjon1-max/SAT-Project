"""Helpers for building slice fh-4 figures: plain black-on-white SAT-book style."""
import base64, io, json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fh-4.jsonl")

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.linewidth": 1.0,
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
})


def new_fig(w=5.0, h=3.6, dpi=110):
    fig, ax = plt.subplots(figsize=(w, h), dpi=dpi)
    return fig, ax


def cross_axes(ax, xlim, ylim, xticks=None, yticks=None, grid=True,
               xlabel="x", ylabel="y", origin_label=True, gridstep=1,
               gridstepy=None, equal=True, xtick_labels=None, ytick_labels=None):
    """SAT-style xy-plane: axes through the origin with arrowheads."""
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    if equal:
        ax.set_aspect("equal", adjustable="box")
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    if grid:
        import numpy as np
        gx = np.arange(int(np.ceil(xlim[0] / gridstep)) * gridstep, xlim[1] + 1e-9, gridstep)
        gs2 = gridstepy or gridstep
        gy = np.arange(int(np.ceil(ylim[0] / gs2)) * gs2, ylim[1] + 1e-9, gs2)
        for v in gx:
            ax.plot([v, v], list(ylim), color="0.75", lw=0.5, zorder=0)
        for v in gy:
            ax.plot(list(xlim), [v, v], color="0.75", lw=0.5, zorder=0)
    ax.annotate("", xy=(xlim[1], 0), xytext=(xlim[0], 0),
                arrowprops=dict(arrowstyle="-|>,head_width=0.15,head_length=0.4",
                                color="black", lw=1.2), zorder=3)
    ax.annotate("", xy=(0, ylim[1]), xytext=(0, ylim[0]),
                arrowprops=dict(arrowstyle="-|>,head_width=0.15,head_length=0.4",
                                color="black", lw=1.2), zorder=3)
    if xticks:
        for t in xticks:
            ax.plot([t, t], [-0.09 * (ylim[1] - ylim[0]) / 10, 0.09 * (ylim[1] - ylim[0]) / 10],
                    color="black", lw=1.0, zorder=3)
            lab = (xtick_labels or {}).get(t, str(t))
            ax.text(t, -0.03 * (ylim[1] - ylim[0]), lab, ha="center", va="top", fontsize=8)
    if yticks:
        for t in yticks:
            ax.plot([-0.09 * (xlim[1] - xlim[0]) / 10, 0.09 * (xlim[1] - xlim[0]) / 10], [t, t],
                    color="black", lw=1.0, zorder=3)
            lab = (ytick_labels or {}).get(t, str(t))
            ax.text(-0.02 * (xlim[1] - xlim[0]), t, lab, ha="right", va="center", fontsize=8)
    if origin_label:
        ax.text(-0.015 * (xlim[1] - xlim[0]), -0.02 * (ylim[1] - ylim[0]), "O",
                ha="right", va="top", fontsize=9, style="italic")
    if xlabel:
        ax.text(xlim[1], 0.03 * (ylim[1] - ylim[0]), xlabel, ha="right", va="bottom",
                fontsize=10, style="italic")
    if ylabel:
        ax.text(0.02 * (xlim[1] - xlim[0]), ylim[1], ylabel, ha="left", va="top",
                fontsize=10, style="italic")


def quad_axes(ax, xlim, ylim, xlabel, ylabel, xticks=None, yticks=None, grid=True):
    """First-quadrant style plot with labelled axes along the left/bottom."""
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(1.1)
    ax.spines["bottom"].set_linewidth(1.1)
    if xticks is not None:
        ax.set_xticks(xticks)
    if yticks is not None:
        ax.set_yticks(yticks)
    ax.tick_params(direction="out", length=4, width=1.0, labelsize=8)
    if grid:
        ax.grid(True, color="0.75", lw=0.5)
        ax.set_axisbelow(True)
    ax.set_xlabel(xlabel, fontsize=9)
    ax.set_ylabel(ylabel, fontsize=9)


def to_data_uri(fig, pad=0.05):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", pad_inches=pad)
    plt.close(fig)
    raw = buf.getvalue()
    return "data:image/png;base64," + base64.b64encode(raw).decode("ascii"), len(raw)


def emit(qid, fig, alt, note=""):
    uri, nbytes = to_data_uri(fig)
    with open(OUT, "a") as f:
        f.write(json.dumps({"id": qid, "imageUrl": uri, "alt": alt, "note": note}) + "\n")
    print("wrote %s  png=%.1f KB  b64=%.1f KB" % (qid, nbytes / 1024, len(uri) / 1024))
