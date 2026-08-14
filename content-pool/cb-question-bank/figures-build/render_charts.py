# -*- coding: utf-8 -*-
"""Render the rebuilt bar/line figures to base64 PNG data URIs.

Design follows the dataviz skill: validated categorical palette in fixed slot
order, recessive grid/axes, thin marks with a surface gap between adjacent
bars, >=8px markers and 2px lines, a legend whenever there are >=2 series and
none when there is one, and text in ink tokens rather than series colors.
No value labels are drawn -- the original charts had none, and adding them
would hand the reader precision the source figure did not give.
"""
import base64, io, os, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from charts import CHARTS, PALETTE

SURFACE = "#ffffff"
INK = "#0b0b0b"
INK2 = "#52514e"
GRID = "#e3e2de"
AXIS = "#c9c8c3"


def rounded_bar(ax, x0, w, h, color, yspan, rx_max):
    """Bar with rounded data-end (~4px), anchored square to the baseline."""
    if h <= 0:
        return
    rx = min(rx_max, w / 2)
    ry = min(yspan * 0.010, h / 2)
    x1 = x0 + w
    verts = [(x0, 0), (x0, h - ry), (x0, h), (x0 + rx, h),
             (x1 - rx, h), (x1, h), (x1, h - ry), (x1, 0), (x0, 0)]
    codes = [Path.MOVETO, Path.LINETO, Path.CURVE3, Path.CURVE3,
             Path.LINETO, Path.CURVE3, Path.CURVE3, Path.LINETO, Path.CLOSEPOLY]
    ax.add_patch(PathPatch(Path(verts, codes), facecolor=color, edgecolor="none",
                           linewidth=0, zorder=3))


def style_axes(ax, spec):
    ax.set_facecolor(SURFACE)
    ax.yaxis.grid(True, color=GRID, linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(AXIS)
        ax.spines[s].set_linewidth(0.8)
    yt = spec["yticks"]
    ax.set_yticks(yt)
    fmt = (lambda v: f"{v:,.0f}") if spec.get("comma") else (lambda v: f"{v:g}")
    ax.set_yticklabels([fmt(v) for v in yt])
    ax.set_ylim(min(yt), max(yt))
    ax.tick_params(axis="both", colors=INK2, labelsize=8.5, length=0)
    for lbl in ax.get_xticklabels() + ax.get_yticklabels():
        lbl.set_color(INK2)
    if spec.get("ylabel"):
        ax.set_ylabel(spec["ylabel"], color=INK2, fontsize=9)
    if spec.get("xlabel"):
        ax.set_xlabel(spec["xlabel"], color=INK2, fontsize=9, labelpad=8)


def render(qid, spec, outdir="png_out"):
    n_ser = len(spec["series"])
    n_cat = len(spec["cats"])
    width = max(6.2, min(9.5, 3.0 + 0.85 * n_cat + (0.25 * n_ser if spec["kind"] == "bar" else 0)))
    height = 4.3
    fig, ax = plt.subplots(figsize=(width, height), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    style_axes(ax, spec)

    xs = list(range(n_cat))
    if spec["kind"] == "bar":
        group = 0.78
        bw = group / n_ser
        gap = bw * 0.10 if n_ser > 1 else 0.0
        yspan = max(spec["yticks"]) - min(spec["yticks"])
        rx_max = 4.0 * (n_cat + 0.2) / (width * 150 * 0.78)
        for si, (name, vals) in enumerate(spec["series"]):
            color = PALETTE[si]
            for ci, v in enumerate(vals):
                x0 = ci - group / 2 + si * bw + (gap / 2 if n_ser > 1 else 0)
                rounded_bar(ax, x0, bw - gap, v, color, yspan, rx_max)
            if name:
                ax.plot([], [], marker="s", linestyle="none", markersize=7,
                        color=color, label=name)
        ax.set_xlim(-0.6, n_cat - 0.4)
    else:
        markers = ["o", "s", "^", "D"]
        dashes = [(None, None), (5, 2), (1.5, 1.6), (7, 2, 1.5, 2)]
        for si, (name, vals) in enumerate(spec["series"]):
            color = PALETTE[si]
            ln, = ax.plot(xs, vals, color=color, linewidth=2.0, zorder=3 + si,
                          marker=markers[si % 4], markersize=6.5,
                          markerfacecolor=color, markeredgecolor=SURFACE,
                          markeredgewidth=1.4, label=name)
            d = dashes[si % 4]
            if d[0] is not None:
                ln.set_dashes(list(d))
        ax.set_xlim(-0.35, n_cat - 0.65)

    ax.set_xticks(xs)
    rot = spec.get("rot", 0)
    ax.set_xticklabels(spec["cats"], rotation=rot,
                       ha="right" if rot else "center",
                       rotation_mode="anchor" if rot else None)

    ax.set_title(spec["title"], color=INK, fontsize=11, pad=12)

    if n_ser >= 2:
        mx = max(len(s[0]) for s in spec["series"])
        ncol = min(n_ser, 4) if mx <= 14 else (2 if mx <= 26 and n_ser > 2 else 1)
        off = -0.22 if rot == 0 else -0.34
        if spec.get("xlabel") and "\n" in spec["xlabel"]:
            off -= 0.07
        if any("\n" in c for c in spec["cats"]):
            off -= 0.07
        leg = ax.legend(loc="upper center", bbox_to_anchor=(0.5, off),
                        ncol=ncol, frameon=False, fontsize=9, handlelength=1.8,
                        columnspacing=1.6, borderpad=0)
        for t in leg.get_texts():
            t.set_color(INK2)

    fig.tight_layout()
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, qid + ".png")
    fig.savefig(path, facecolor=SURFACE, bbox_inches="tight", pad_inches=0.18)
    plt.close(fig)
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()


def render_all():
    out = {}
    for qid, spec in CHARTS.items():
        out[qid] = render(qid, spec)
    return out


if __name__ == "__main__":
    ids = sys.argv[1:] or list(CHARTS)
    for qid in ids:
        uri = render(qid, CHARTS[qid])
        print(qid, len(uri))
