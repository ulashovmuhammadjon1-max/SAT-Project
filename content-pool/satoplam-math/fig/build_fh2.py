#!/usr/bin/env python3
"""Build the missing figures for slice fh-2 (SAToplam Math ma2 book).

Every figure was checked against the printed page image under pages/ before
being drawn.  One JSON line is appended to fig/fh-2.jsonl per figure, flushed
immediately, so a crash loses at most the figure in flight.
"""
import base64, io, json, math, os, sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["DejaVu Serif"]
plt.rcParams["mathtext.fontset"] = "cm"

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "fh-2.jsonl")

LW = 1.8          # line weight for the geometry itself
FS = 13           # label font size
CAPFS = 11        # caption font size
NOTSCALE = "Note: Figure not drawn to scale"

done = set()
if os.path.exists(OUT):
    with open(OUT) as fh:
        for line in fh:
            line = line.strip()
            if line:
                done.add(json.loads(line)["id"])


def emit(qid, fig, alt, note=""):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=110, bbox_inches="tight",
                pad_inches=0.10, facecolor="white")
    plt.close(fig)
    raw = buf.getvalue()
    b64 = base64.b64encode(raw).decode("ascii")
    rec = {"id": qid, "imageUrl": "data:image/png;base64," + b64,
           "alt": alt, "note": note}
    with open(OUT, "a") as fh:
        fh.write(json.dumps(rec) + "\n")
        fh.flush()
        os.fsync(fh.fileno())
    print("  %-38s %6.1f KB  png" % (qid, len(raw) / 1024.0))


def newax(w=5.0, h=3.6):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def seg(ax, p, q, **kw):
    kw.setdefault("color", "black")
    kw.setdefault("lw", LW)
    kw.setdefault("solid_capstyle", "round")
    ax.plot([p[0], q[0]], [p[1], q[1]], **kw)


def txt(ax, p, s, **kw):
    kw.setdefault("fontsize", FS)
    kw.setdefault("ha", "center")
    kw.setdefault("va", "center")
    kw.setdefault("color", "black")
    ax.text(p[0], p[1], s, **kw)


def rightangle(ax, v, d1, d2, size):
    """Small square at vertex v, opening along unit dirs d1 and d2."""
    n1 = (d1[0] / math.hypot(*d1) * size, d1[1] / math.hypot(*d1) * size)
    n2 = (d2[0] / math.hypot(*d2) * size, d2[1] / math.hypot(*d2) * size)
    pts = [(v[0] + n1[0], v[1] + n1[1]),
           (v[0] + n1[0] + n2[0], v[1] + n1[1] + n2[1]),
           (v[0] + n2[0], v[1] + n2[1])]
    ax.plot([p[0] for p in pts], [p[1] for p in pts],
            color="black", lw=1.2, solid_joinstyle="miter")


def caption(ax, text, xmid, ybot):
    ax.text(xmid, ybot, text, fontsize=CAPFS, ha="center", va="top",
            color="black")


# ----------------------------------------------------------------- helpers
def two_parallels(ax, y_hi, y_lo, x0, x1, hi_label, lo_label, side="right"):
    seg(ax, (x0, y_hi), (x1, y_hi))
    seg(ax, (x0, y_lo), (x1, y_lo))
    if hi_label:
        txt(ax, (x1 + 0.18, y_hi), hi_label)
    if lo_label:
        txt(ax, (x1 + 0.18, y_lo), lo_label)


BUILDERS = {}


def builder(qid):
    def deco(fn):
        BUILDERS[qid] = fn
        return fn
    return deco


# =========================================================== lines & angles
@builder("satmath-ma2-lines-angles-12")
def _():
    fig, ax = newax(4.4, 4.0)
    # r and s are VERTICAL here; t rises to the right.
    seg(ax, (0, -1.6), (0, 1.6))
    seg(ax, (1.2, -1.6), (1.2, 1.6))
    seg(ax, (-0.85, -1.45), (2.05, 1.45))          # y = x - 0.6
    txt(ax, (0, 1.78), r"$r$")
    txt(ax, (1.2, 1.78), r"$s$")
    txt(ax, (2.18, 1.55), r"$t$")
    txt(ax, (-0.20, -0.92), r"$x^\circ$")          # left of r, below t
    txt(ax, (1.00, 0.86), r"$y^\circ$")            # left of s, above t
    ax.set_xlim(-1.15, 2.45)
    ax.set_ylim(-1.85, 2.00)
    return (fig,
            "Two parallel vertical lines r and s cut by a transversal t that "
            "rises to the right; one angle is marked at each intersection, "
            "labelled x degrees and y degrees.",
            "")


@builder("satmath-ma2-lines-angles-14")
def _():
    fig, ax = newax(5.0, 3.0)
    two_parallels(ax, 1, 0, 0, 3.25, r"$r$", r"$s$")
    seg(ax, (0.2875, 1.45), (2.725, -0.5))         # slope -0.8
    txt(ax, (2.80, -0.62), r"$n$")
    txt(ax, (1.10, 1.15), r"$164^\circ$")          # above r, right of n
    txt(ax, (2.24, 0.16), r"$x^\circ$")            # above s, right of n
    ax.set_xlim(-0.25, 3.7)
    ax.set_ylim(-0.95, 1.75)
    return (fig,
            "Two parallel horizontal lines r and s cut by a transversal n; "
            "one angle at the upper intersection carries a degree measure and "
            "an angle at the lower intersection is labelled x degrees.",
            "")


@builder("satmath-ma2-lines-angles-16")
def _():
    fig, ax = newax(5.0, 3.0)
    two_parallels(ax, 1, 0, 0, 3.0, r"$r$", r"$s$")
    seg(ax, (0.6, -0.4), (2.5, 1.5))               # slope +1
    txt(ax, (1.70, 1.16), r"$138^\circ$")          # above r, left of n
    txt(ax, (0.70, 0.16), r"$x^\circ$")            # above s, left of n
    ax.set_xlim(-0.25, 3.5)
    ax.set_ylim(-0.7, 1.75)
    return (fig,
            "Two parallel horizontal lines r and s cut by a transversal that "
            "rises to the right; one angle at the upper intersection carries a "
            "degree measure and an angle at the lower intersection is labelled "
            "x degrees.",
            "The book leaves the transversal unlabelled in this figure even "
            "though the stem calls it line n; reproduced as printed.")


@builder("satmath-ma2-lines-angles-20")
def _():
    fig, ax = newax(5.0, 3.0)
    two_parallels(ax, 1, 0, 0, 3.0, r"$p$", r"$q$")
    seg(ax, (0.48, 1.35), (3.04, -0.45))           # slope -0.70
    txt(ax, (0.40, 1.50), r"$t$")
    txt(ax, (2.12, 0.16), r"$x^\circ$")            # above q, left of t
    txt(ax, (2.66, 0.16), r"$142^\circ$")          # above q, right of t
    ax.set_xlim(-0.25, 3.5)
    ax.set_ylim(-0.75, 1.75)
    return (fig,
            "Two parallel horizontal lines p and q cut by a transversal t; at "
            "the lower intersection one angle is labelled x degrees and the "
            "angle beside it carries a degree measure.",
            "")


@builder("satmath-ma2-lines-angles-21")
def _():
    fig, ax = newax(5.0, 3.2)
    two_parallels(ax, 1, 0, 0, 3.2, r"$m$", r"$n$")
    seg(ax, (0.75, 1.23), (2.35, -0.37))           # slope -1, m at .98, n at 1.98
    txt(ax, (0.68, 1.38), r"$k$")
    txt(ax, (0.70, 1.16), r"$q^\circ$")            # above m, left of k
    txt(ax, (1.20, 0.80), r"$r^\circ$")            # below m, right of k
    txt(ax, (2.22, 0.16), r"$s^\circ$")            # above n, right of k
    txt(ax, (1.58, -0.20), r"$135^\circ$")         # below n, left of k
    txt(ax, (2.34, -0.18), r"$t^\circ$")           # below n, right of k
    ax.set_xlim(-0.25, 3.7)
    ax.set_ylim(-0.60, 1.60)
    return (fig,
            "Two parallel horizontal lines m and n cut by a transversal k; "
            "four angles are labelled with letters and one with a degree "
            "measure.",
            "")


@builder("satmath-ma2-lines-angles-23")
def _():
    fig, ax = newax(5.0, 3.2)
    two_parallels(ax, 1, 0, 0, 3.2, r"$q$", r"$r$")
    seg(ax, (1.10, -0.44), (2.30, 1.44))           # r at 1.38, q at 2.02
    txt(ax, (2.38, 1.57), r"$s$")
    txt(ax, (2.32, 1.16), r"$61^\circ$")           # above q, right of s
    txt(ax, (1.12, 0.17), r"$y$")                  # above r, left of s
    ax.set_xlim(-0.25, 3.7)
    ax.set_ylim(-0.65, 1.80)
    return (fig,
            "Two parallel horizontal lines q and r cut by a transversal s that "
            "rises to the right; one angle at the upper intersection carries a "
            "degree measure and one at the lower intersection is labelled y.",
            "")


@builder("satmath-ma2-lines-angles-27")
def _():
    fig, ax = newax(3.6, 3.2)
    seg(ax, (-1, 1), (1, -1))
    seg(ax, (-1, -1), (1, 1))
    txt(ax, (0.02, 0.40), r"$w^\circ$")
    txt(ax, (0.03, -0.40), r"$z^\circ$")
    ax.set_xlim(-1.25, 1.25)
    ax.set_ylim(-1.25, 1.25)
    return (fig,
            "Two straight lines crossing at one point; the angle above the "
            "crossing is labelled w degrees and the angle below it is labelled "
            "z degrees.",
            "")


@builder("satmath-ma2-lines-angles-29")
def _():
    fig, ax = newax(5.0, 3.2)
    two_parallels(ax, 1, 0, 0, 3.2, r"$l$", r"$k$")
    seg(ax, (0.53, 1.55), (2.60, -0.28))           # l at .96, k at 2.24
    txt(ax, (0.44, 1.68), r"$t$")
    txt(ax, (1.22, 1.16), r"$x^\circ$")            # above l, right of t
    txt(ax, (1.94, 0.16), r"$y^\circ$")            # above k, left of t
    ax.set_xlim(-0.25, 3.7)
    ax.set_ylim(-0.55, 1.90)
    return (fig,
            "Two parallel horizontal lines l and k cut by a transversal t; one "
            "angle at each intersection is labelled, x degrees at the upper "
            "line and y degrees at the lower line.",
            "")


@builder("satmath-ma2-lines-angles-30")
def _():
    fig, ax = newax(5.0, 3.2)
    two_parallels(ax, 1, 0, 0, 3.2, r"$q$", r"$r$")
    seg(ax, (1.10, -0.44), (2.30, 1.44))
    txt(ax, (2.38, 1.57), r"$s$")
    txt(ax, (2.32, 1.16), r"$74^\circ$")
    txt(ax, (1.12, 0.17), r"$y$")
    ax.set_xlim(-0.25, 3.7)
    ax.set_ylim(-0.65, 1.80)
    return (fig,
            "Two parallel horizontal lines q and r cut by a transversal s that "
            "rises to the right; one angle at the upper intersection carries a "
            "degree measure and one at the lower intersection is labelled y.",
            "")


@builder("satmath-ma2-lines-angles-36")
def _():
    fig, ax = newax(5.0, 3.2)
    two_parallels(ax, 1, 0, 0, 3.2, r"$l$", r"$m$")
    seg(ax, (1.02, 1.22), (2.83, -0.41))           # l at 1.26, m at 2.37
    txt(ax, (2.92, -0.54), r"$k$")
    txt(ax, (1.50, 1.16), r"$x^\circ$")            # above l, right of k
    txt(ax, (2.02, -0.22), r"$111^\circ$")         # below m, left of k
    ax.set_xlim(-0.25, 3.7)
    ax.set_ylim(-0.75, 1.55)
    return (fig,
            "Two parallel horizontal lines l and m cut by a transversal k; an "
            "angle above the upper line is labelled x degrees and an angle "
            "below the lower line carries a degree measure.",
            "")


# ================================================================ triangles
@builder("satmath-ma2-triangles-11")
def _():
    fig, ax = newax(4.8, 3.2)
    A, C, B = (0, 0), (10, 0), (4.9, 6.0)
    F = (4.9, 0)
    seg(ax, A, C); seg(ax, A, B); seg(ax, B, C)
    ax.plot([B[0], F[0]], [B[1], F[1]], color="black", lw=1.3, ls=(0, (4, 3)))
    rightangle(ax, F, (1, 0), (0, 1), 0.45)
    txt(ax, (-0.55, -0.05), r"$A$")
    txt(ax, (10.55, -0.05), r"$C$")
    txt(ax, (4.9, 6.65), r"$B$")
    txt(ax, (5.55, 3.1), r"$h$")
    ax.annotate("", xy=(0, -1.15), xytext=(10, -1.15),
                arrowprops=dict(arrowstyle="<|-|>", color="black", lw=1.0,
                                mutation_scale=11,
                                shrinkA=0, shrinkB=0))
    txt(ax, (5.0, -1.95), "10 cm", fontsize=12)
    ax.set_xlim(-1.3, 11.3)
    ax.set_ylim(-2.7, 7.2)
    return (fig,
            "Triangle ABC with a horizontal base AC carrying a dimension "
            "arrow and its measurement, and a dashed altitude from vertex B "
            "down to the base labelled h, with a right-angle mark at its foot.",
            "")


@builder("satmath-ma2-triangles-23")
def _():
    fig, ax = newax(4.4, 3.2)
    P0, P1, P2 = (0, 0), (0, 0.75), (1.0, 0)
    seg(ax, P0, P1); seg(ax, P0, P2); seg(ax, P1, P2)
    rightangle(ax, P0, (1, 0), (0, 1), 0.075)
    txt(ax, (-0.10, 0.40), r"$x$")
    txt(ax, (0.50, -0.11), r"$66$")
    txt(ax, (0.80, 0.055), r"$30^\circ$", fontsize=12)
    ax.set_xlim(-0.22, 1.12)
    ax.set_ylim(-0.24, 0.90)
    return (fig,
            "A right triangle with the right angle at the lower-left vertex; "
            "the vertical leg is labelled x, the horizontal leg carries a "
            "length, and the lower-right angle carries a degree measure.",
            "")


@builder("satmath-ma2-triangles-34")
def _():
    fig, ax = newax(4.2, 3.4)
    P0, P1, P2 = (0, 0), (0, 1.0), (1.0, 0)
    seg(ax, P0, P1); seg(ax, P0, P2); seg(ax, P1, P2)
    rightangle(ax, P0, (1, 0), (0, 1), 0.075)
    txt(ax, (-0.11, 0.50), r"$37$")
    txt(ax, (0.50, -0.12), r"$37$")
    txt(ax, (0.58, 0.60), r"$x$")
    ax.set_xlim(-0.26, 1.12)
    ax.set_ylim(-0.26, 1.14)
    return (fig,
            "A right triangle with the right angle at the lower-left vertex; "
            "both legs carry lengths and the hypotenuse is labelled x.",
            "")


@builder("satmath-ma2-triangles-42")
def _():
    fig, ax = newax(5.4, 2.9)
    A, B, C = (0, 0), (1.0, 0), (0.5, -1.0)
    seg(ax, A, B); seg(ax, B, C); seg(ax, C, A)
    txt(ax, (-0.17, 0.03), r"$A$")
    txt(ax, (1.17, 0.03), r"$B$")
    txt(ax, (0.50, -1.22), r"$C$")
    txt(ax, (0.20, -0.16), r"$60^\circ$", fontsize=12)
    txt(ax, (0.10, -0.55), r"$d$")
    k = 1.55
    X = (1.95, 0.28)
    Y = (X[0] + 1.0 * k, X[1])
    Z = (X[0] + 0.5 * k, X[1] - 1.0 * k)
    seg(ax, X, Y); seg(ax, Y, Z); seg(ax, Z, X)
    txt(ax, (X[0] - 0.17, X[1] + 0.03), r"$X$")
    txt(ax, (Y[0] + 0.17, Y[1] + 0.03), r"$Y$")
    txt(ax, (Z[0], Z[1] - 0.22), r"$Z$")
    caption(ax, NOTSCALE, 1.75, -1.62)
    ax.set_xlim(-0.35, 3.72)
    ax.set_ylim(-2.15, 0.52)
    return (fig,
            "Two triangles side by side: a smaller triangle ABC with one "
            "angle marked in degrees and one side labelled d, and a larger "
            "triangle XYZ of the same shape with no labels on its sides or "
            "angles.",
            "")


@builder("satmath-ma2-triangles-43")
def _():
    fig, ax = plt.subplots(figsize=(5.0, 4.7))
    ax.set_aspect("equal")
    ax.axis("off")
    g = dict(color="#c2c2cf", lw=0.7, zorder=0)
    for gx in range(-9, 10):
        ax.plot([gx, gx], [0, 16.6], **g)
    for gy in range(0, 17):
        ax.plot([-8.7, 8.7], [gy, gy], **g)
    ax.annotate("", xy=(9.1, 0), xytext=(-9.1, 0),
                arrowprops=dict(arrowstyle="-|>", color="black", lw=1.2,
                                mutation_scale=13, shrinkA=0, shrinkB=0),
                zorder=3)
    ax.annotate("", xy=(0, 17.1), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="black", lw=1.2,
                                mutation_scale=13, shrinkA=0, shrinkB=0),
                zorder=3)
    for tx in (-8, -6, -4, -2, 2, 4, 6, 8):
        ax.plot([tx, tx], [-0.28, 0.28], color="black", lw=1.1, zorder=3)
        ax.text(tx, -0.85, r"$%d$" % tx, fontsize=12, ha="center", va="top")
    for ty in range(2, 17, 2):
        ax.plot([-0.28, 0.28], [ty, ty], color="black", lw=1.1, zorder=3)
        ax.text(-0.45, ty, r"$%d$" % ty, fontsize=12, ha="right", va="center")
    ax.text(9.6, 0.45, r"$x$", fontsize=13, ha="left", va="center")
    ax.text(0.45, 17.6, r"$y$", fontsize=13, ha="center", va="bottom")
    ax.plot([-5, 4], [3, 9], color="black", lw=2.4, solid_capstyle="round",
            zorder=4)
    ax.plot([-5, 4], [3, 9], "o", color="black", ms=6.5, zorder=5)
    ax.set_xlim(-10.4, 10.4)
    ax.set_ylim(-2.3, 18.4)
    return (fig,
            "An xy-plane with a one-unit grid, the x-axis labelled every two "
            "units from negative eight to eight and the y-axis labelled every "
            "two units up to sixteen, showing a single line segment with a "
            "filled dot at each endpoint.",
            "")


@builder("satmath-ma2-triangles-45")
def _():
    fig, ax = newax(5.0, 2.9)
    A, C, B = (0, 0), (10, 0), (4.5, 3.3)
    F = (4.5, 0)
    seg(ax, A, C); seg(ax, A, B); seg(ax, B, C)
    ax.plot([B[0], F[0]], [B[1], F[1]], color="black", lw=1.3, ls=(0, (4, 3)))
    rightangle(ax, F, (1, 0), (0, 1), 0.42)
    txt(ax, (-0.55, -0.32), r"$A$")
    txt(ax, (10.55, -0.32), r"$C$")
    txt(ax, (4.5, 3.85), r"$B$")
    txt(ax, (5.15, 1.75), r"$h$")
    txt(ax, (4.85, -0.62), "10 cm", fontsize=12)
    caption(ax, NOTSCALE, 5.0, -1.35)
    ax.set_xlim(-1.3, 11.3)
    ax.set_ylim(-2.55, 4.45)
    return (fig,
            "Triangle ABC with a horizontal base AC carrying its measurement "
            "and a dashed altitude from vertex B down to the base labelled h, "
            "with a right-angle mark at its foot.",
            "")


@builder("satmath-ma2-triangles-46")
def _():
    fig, ax = newax(4.2, 3.2)
    P0, P1, P2 = (0, 0), (0, 1.0), (1.37, 0)
    seg(ax, P0, P1); seg(ax, P0, P2); seg(ax, P1, P2)
    rightangle(ax, P0, (1, 0), (0, 1), 0.085)
    txt(ax, (0.17, 0.84), r"$24^\circ$", fontsize=12)
    txt(ax, (1.12, 0.075), r"$a^\circ$", fontsize=12)
    caption(ax, NOTSCALE, 0.68, -0.20)
    ax.set_xlim(-0.18, 1.55)
    ax.set_ylim(-0.62, 1.16)
    return (fig,
            "A right triangle with the right angle marked at the lower-left "
            "vertex; the angle at the top vertex carries a degree measure and "
            "the angle at the lower-right vertex is labelled a degrees.",
            "")


@builder("satmath-ma2-triangles-47")
def _():
    fig, ax = newax(4.4, 3.0)
    L, K, J = (0, 0), (1.38, 0), (1.38, 1.0)
    seg(ax, L, K); seg(ax, K, J); seg(ax, J, L)
    rightangle(ax, K, (-1, 0), (0, 1), 0.085)
    txt(ax, (-0.15, -0.02), r"$L$")
    txt(ax, (1.53, -0.02), r"$K$")
    txt(ax, (1.50, 1.08), r"$J$")
    txt(ax, (0.62, 0.56), r"$90$")
    caption(ax, NOTSCALE, 0.69, -0.22)
    ax.set_xlim(-0.30, 1.70)
    ax.set_ylim(-0.62, 1.22)
    return (fig,
            "Right triangle JKL with the right angle marked at K; L is at the "
            "lower left, K at the lower right and J directly above K, and the "
            "hypotenuse carries a length.",
            "")


# ============================================================= trigonometry
@builder("satmath-ma2-trigonometry-1")
def _():
    fig, ax = newax(3.8, 3.6)
    F, D, E = (0, 0), (0, 4), (3, 0)
    seg(ax, F, D); seg(ax, F, E); seg(ax, D, E)
    rightangle(ax, F, (1, 0), (0, 1), 0.28)
    txt(ax, (0, 4.42), r"$D$")
    txt(ax, (-0.42, -0.30), r"$F$")
    txt(ax, (3.40, -0.20), r"$E$")
    txt(ax, (-0.32, 2.0), r"$4$")
    txt(ax, (1.5, -0.42), r"$3$")
    ax.set_xlim(-0.85, 3.75)
    ax.set_ylim(-0.95, 4.85)
    return (fig,
            "A right triangle DEF drawn with D directly above F and E to the "
            "right of F; both legs carry lengths.",
            "The book prints no right-angle mark at F, but the question is "
            "unanswerable unless angle F is known to be 90 degrees (the book "
            "leaves it to the drawing), so the right-angle square was added.")


def ramp(ax, W, H, theta_pos, height_text, length_rotated, arc):
    O, R, T = (0, 0), (W, 0), (W, H)
    seg(ax, O, R); seg(ax, R, T); seg(ax, T, O)
    rightangle(ax, R, (-1, 0), (0, 1), 0.07 * W)
    if arc:
        ax.add_patch(Arc(O, 0.42 * W, 0.42 * W, theta1=0,
                         theta2=math.degrees(math.atan2(H, W)),
                         color="black", lw=1.1))
    txt(ax, theta_pos, r"$\theta$")
    txt(ax, (W / 2.0, -0.13 * max(H, 0.6 * W)), r"$x$")
    txt(ax, (W + 0.08 * W, H / 2.0), height_text, ha="left", fontsize=12)
    if length_rotated:
        ang = math.degrees(math.atan2(H, W))
        txt(ax, (W * 0.42 - 0.10 * H, H * 0.42 + 0.16 * W),
            "length of the ramp", rotation=ang, fontsize=12,
            rotation_mode="anchor")
    else:
        txt(ax, (W * 0.45, H + 0.30 * W * 0.35), "length of the ramp",
            fontsize=12)


@builder("satmath-ma2-trigonometry-2")
def _():
    fig, ax = newax(5.4, 2.5)
    ramp(ax, 3.6, 1.0, (0.80, 0.12), "height\nof the\nramp",
         length_rotated=False, arc=False)
    ax.set_xlim(-0.25, 5.15)
    ax.set_ylim(-0.75, 1.95)
    return (fig,
            "A right triangle representing a ramp: the horizontal bottom side "
            "is labelled x, the vertical side on the right is labelled height "
            "of the ramp with a right-angle mark where the two meet, the "
            "hypotenuse is labelled length of the ramp, and the angle at the "
            "left-hand vertex is labelled theta.",
            "")


@builder("satmath-ma2-trigonometry-3")
def _():
    fig, ax = newax(4.8, 3.0)
    ramp(ax, 2.3, 1.47, (0.52, 0.17), "height of\nthe ramp",
         length_rotated=True, arc=True)
    ax.set_xlim(-0.20, 3.95)
    ax.set_ylim(-0.55, 1.95)
    return (fig,
            "A right triangle representing a ramp: the horizontal bottom side "
            "is labelled x, the vertical side on the right is labelled height "
            "of the ramp with a right-angle mark where the two meet, the "
            "hypotenuse is labelled length of the ramp, and the angle at the "
            "left-hand vertex is labelled theta.",
            "")


@builder("satmath-ma2-trigonometry-4")
def _():
    fig, ax = newax(4.6, 3.2)
    A, C, B = (0, 0), (1.9, 0), (1.9, 1.54)
    seg(ax, A, C); seg(ax, C, B); seg(ax, B, A)
    rightangle(ax, C, (-1, 0), (0, 1), 0.10)
    txt(ax, (-0.16, -0.03), r"$A$")
    txt(ax, (2.07, -0.03), r"$C$")
    txt(ax, (2.05, 1.62), r"$B$")
    txt(ax, (0.95, -0.16), r"$53$")
    txt(ax, (0.85, 0.86), r"$54$")
    caption(ax, "Note: Figure not drawn to a scale.", 0.95, -0.40)
    ax.set_xlim(-0.35, 2.30)
    ax.set_ylim(-0.90, 1.82)
    return (fig,
            "A right triangle with the right angle marked at C, A at the lower "
            "left and B directly above C; the horizontal side and the "
            "hypotenuse each carry a length.",
            "")


@builder("satmath-ma2-trigonometry-9")
def _():
    fig, ax = newax(4.6, 3.2)
    Z, X, Y = (0, 0), (0, 1.56), (2.0, 0)
    seg(ax, Z, X); seg(ax, Z, Y); seg(ax, X, Y)
    rightangle(ax, Z, (1, 0), (0, 1), 0.115)
    txt(ax, (0, 1.72), r"$X$")
    txt(ax, (-0.16, -0.16), r"$Z$")
    txt(ax, (2.12, -0.16), r"$Y$")
    txt(ax, (-0.17, 0.80), r"$29$")
    txt(ax, (1.0, -0.17), r"$37$")
    ax.set_xlim(-0.40, 2.32)
    ax.set_ylim(-0.42, 1.92)
    return (fig,
            "Right triangle XYZ with the right angle marked at Z, X directly "
            "above Z and Y to the right of Z; both legs carry lengths.",
            "")


@builder("satmath-ma2-trigonometry-10")
def _():
    fig, ax = newax(4.4, 3.0)
    T, S, R = (0, 0), (1.24, 0), (1.24, 1.0)
    seg(ax, T, S); seg(ax, S, R); seg(ax, R, T)
    rightangle(ax, S, (-1, 0), (0, 1), 0.085)
    txt(ax, (-0.15, -0.03), r"$T$")
    txt(ax, (1.39, -0.03), r"$S$")
    txt(ax, (1.24, 1.14), r"$R$")
    txt(ax, (0.55, 0.55), r"$79$")
    ax.set_xlim(-0.30, 1.58)
    ax.set_ylim(-0.24, 1.30)
    return (fig,
            "Right triangle RST with the right angle marked at S, T at the "
            "lower left and R directly above S; the hypotenuse carries a "
            "length.",
            "")


# ---------------------------------------------------------------- run them
def main():
    recs = json.load(open(os.path.join(HERE, "fh-2.slice.json")))
    missing = []
    for r in recs:
        qid = r["id"]
        if qid in done:
            print("  %-38s skipped (already built)" % qid)
            continue
        fn = BUILDERS.get(qid)
        if fn is None:
            missing.append(qid)
            continue
        fig, alt, note = fn()
        emit(qid, fig, alt, note)
    if missing:
        print("NO BUILDER FOR:", missing, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
