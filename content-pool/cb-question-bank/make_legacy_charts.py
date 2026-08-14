# -*- coding: utf-8 -*-
"""Rebuild the two line charts missing from legacy Tests 3-5 R&W questions.

Both questions say "uses data from the graph" but their passages carry no
figure at all -- the chart was lost when the EliteXSAT paper was transcribed.

Every value below was measured by pixel analysis of the ORIGINAL chart bitmap
pulled out of the source PDF with `pdfimages` (not off a page render, which
clips the slide), against the detected gridline rows:

  * March 2023 EliteXSAT p.7  -> imgs7/m-007-000.png, gridlines y=370(10) ..
    y=780(0), 41 px per unit.  Marker outlines give a top and a bottom edge;
    the value is the midpoint.  Every one landed within 0.2 of an integer.
  * Nov 2023 EliteXSAT p.13 -> imgs13/n-013-000.png, gridlines y=162(300) ..
    y=376.5(50), 35.75 px per 50.  Open circles were located by their ring
    (dark-light-dark row pattern); filled triangles are base-heavy so their
    span, not their ink centroid, was used.

Palette + mark specs follow the `dataviz` skill and match this repo's existing
house chart style in make_charts9.py: categorical slots 1-4 (#2a78d6 blue,
#eb6834 orange, #1baf7a aqua, #eda100 yellow), validated with
scripts/validate_palette.js --mode light (ALL CHECKS PASS; worst adjacent CVD
delta-E 9.1).  The contrast WARN on aqua and yellow is relieved the documented
way -- every series carries a visible direct label as well as the legend, and
identity is composite (hue x marker shape), never colour alone.
"""
import base64
import io
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
INK, INK2, GRID = "#0b0b0b", "#52514e", "#D9DEE5"


def style(ax):
    ax.set_facecolor("white")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
        ax.spines[s].set_linewidth(1.0)
    ax.yaxis.grid(True, color=GRID, linewidth=0.9)
    ax.xaxis.grid(False)
    ax.set_axisbelow(True)
    ax.tick_params(colors=INK2, labelsize=9, length=0)


def render(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=160, facecolor="white",
                bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode("ascii")


# --------------------------------------------------------------- women judges
# Source: 2023 March EliteXSAT, "Women Judges and Magistrates on High Courts,
# 2009-2013".  Measured values (all integers):
#   Slovenia            4, 4, 5, 5, 5
#   Finland             7, 6, 6, 7, 7
#   Dominican Republic  5, 5, 8, 4, 4
def judges():
    years = [2009, 2010, 2011, 2012, 2013]
    slovenia = [4, 4, 5, 5, 5]
    finland = [7, 6, 6, 7, 7]
    dominican = [5, 5, 8, 4, 4]

    fig, ax = plt.subplots(figsize=(5.5, 3.05))
    style(ax)
    ax.plot(years, slovenia, color=BLUE, lw=2, marker="o", ms=6.5, mfc="white",
            mec=BLUE, mew=2, label="Slovenia", zorder=4, clip_on=False)
    ax.plot(years, finland, color=ORANGE, lw=2, marker="s", ms=6, mfc="white",
            mec=ORANGE, mew=2, label="Finland", zorder=3, clip_on=False)
    ax.plot(years, dominican, color=AQUA, lw=2, marker="^", ms=7, mfc="white",
            mec=AQUA, mew=2, label="Dominican Republic", zorder=3, clip_on=False)
    ax.set_ylim(0, 10)
    ax.set_yticks([0, 2, 4, 6, 8, 10])
    ax.set_xlim(2008.85, 2013.15)
    ax.set_xticks(years)
    ax.set_xlabel("Year", color=INK2, fontsize=9.5, labelpad=6)
    ax.set_ylabel("Number", color=INK2, fontsize=9.5, labelpad=6)
    for name, val, col, dy in (("Finland", 7, ORANGE, 1),
                               ("Slovenia", 5, BLUE, 8),
                               ("Dominican Republic", 4, AQUA, -8)):
        ax.annotate(name, (2013, val), xytext=(9, dy), textcoords="offset points",
                    color=col, fontsize=9.5, fontweight="bold", va="center")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.36), ncol=3,
              frameon=False, fontsize=9.5, handlelength=2.2,
              columnspacing=1.6, labelcolor=INK)
    fig.subplots_adjust(right=0.66)
    return render(fig)


# ------------------------------------------------------------ science fair
# Source: 2023 Nov EliteXSAT, "Total Science Research Submissions by Topic,
# 2016-2019".  Measured values:
#   cellular and molecular biology  200, 300, 280, 280
#   physics and space science        95,  90,  87, 100
#   medicine and health             220, 220, 224, 286
#   animal science                   50,  50,  50,  90
# Four series carry long names, so the direct labels sit inline on a white
# plate beside each line's least-crowded point rather than in a right margin,
# which at 2019 would collide (286 vs 280, and 100 vs 90).
def science_fair():
    years = [2016, 2017, 2018, 2019]
    cellular = [200, 300, 280, 280]
    physics = [95, 90, 87, 100]
    medicine = [220, 220, 224, 286]
    animal = [50, 50, 50, 90]

    fig, ax = plt.subplots(figsize=(5.6, 3.3))
    style(ax)
    ax.plot(years, cellular, color=BLUE, lw=2, marker="o", ms=6.5, mfc="white",
            mec=BLUE, mew=2, label="cellular and molecular biology",
            zorder=5, clip_on=False)
    ax.plot(years, physics, color=ORANGE, lw=2, marker="s", ms=6, mfc="white",
            mec=ORANGE, mew=2, label="physics and space science",
            zorder=4, clip_on=False)
    ax.plot(years, medicine, color=AQUA, lw=2, marker="^", ms=7, mfc="white",
            mec=AQUA, mew=2, label="medicine and health", zorder=4, clip_on=False)
    ax.plot(years, animal, color=YELLOW, lw=2, marker="D", ms=5.5, mfc="white",
            mec=YELLOW, mew=2, label="animal science", zorder=3, clip_on=False)
    ax.set_ylim(0, 350)
    ax.set_yticks([0, 50, 100, 150, 200, 250, 300, 350])
    ax.set_xlim(2015.9, 2019.1)
    ax.set_xticks(years)
    ax.set_xlabel("Year", color=INK2, fontsize=9.5, labelpad=6)
    ax.set_ylabel("Number of submissions", color=INK2, fontsize=9.5, labelpad=6)

    plate = dict(boxstyle="round,pad=0.18", fc="white", ec="none", alpha=0.92)
    for name, xy, col, off in (
            ("cellular and molecular biology", (2017, 300), BLUE, (-6, 13)),
            ("medicine and health", (2017, 220), AQUA, (-4, -14)),
            ("physics and space science", (2017, 90), ORANGE, (-4, 14)),
            ("animal science", (2017, 50), YELLOW, (-4, -14))):
        ax.annotate(name, xy, xytext=off, textcoords="offset points",
                    color=col, fontsize=8.5, fontweight="bold",
                    ha="center", va="center", bbox=plate, zorder=6)

    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.42), ncol=2,
              frameon=False, fontsize=9, handlelength=2.2,
              columnspacing=1.6, labelcolor=INK)
    return render(fig)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    out = {"judges": judges(), "science_fair": science_fair()}
    with open(os.path.join(here, "legacy_charts.json"), "w") as fh:
        json.dump(out, fh)
    for k, v in out.items():
        print(k, len(v), "chars")
