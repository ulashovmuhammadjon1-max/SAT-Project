# -*- coding: utf-8 -*-
"""Regenerate the two line charts whose questions turn on trend slope.

Values were measured from the 300-dpi renders of the College Board source pages
by pixel analysis (see markers2.py / raw2.py), never inferred from the flattened
prose string. Palette + mark specs follow the `dataviz` skill: categorical slots
1-3 (#2a78d6 blue, #eb6834 orange, #1baf7a aqua), validated with
scripts/validate_palette.js (all checks PASS; the aqua contrast WARN is relieved
by the mandatory direct labels). Composite encoding (hue x marker shape) keeps
the series apart in print and under CVD.
"""
import io, base64, os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BLUE, ORANGE, AQUA = '#2a78d6', '#eb6834', '#1baf7a'
INK, INK2, GRID = '#0b0b0b', '#52514e', '#D9DEE5'

def style(ax):
    ax.set_facecolor('white')
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    for s in ('left', 'bottom'):
        ax.spines[s].set_color(GRID)
        ax.spines[s].set_linewidth(1.0)
    ax.yaxis.grid(True, color=GRID, linewidth=0.9)
    ax.xaxis.grid(False)
    ax.set_axisbelow(True)
    ax.tick_params(colors=INK2, labelsize=9, length=0)

def render(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=160, facecolor='white',
                bbox_inches='tight', pad_inches=0.12)
    plt.close(fig)
    return 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode('ascii')

# ---------------------------------------------------------------- condors
def condors():
    years = [2014, 2015, 2016, 2017, 2018, 2019, 2020]
    wild = [228, 268, 276, 290, 312, 337, 329]
    captive = [193, 167, 170, 173, 176, 181, 175]
    fig, ax = plt.subplots(figsize=(5.1, 3.05))
    style(ax)
    ax.plot(years, wild, color=BLUE, lw=2, marker='o', ms=6.5,
            mfc='white', mec=BLUE, mew=2, label='wild', zorder=3, clip_on=False)
    ax.plot(years, captive, color=ORANGE, lw=2, marker='s', ms=6,
            mfc='white', mec=ORANGE, mew=2, label='captive', zorder=3, clip_on=False)
    ax.set_ylim(0, 400); ax.set_yticks([0, 100, 200, 300, 400])
    ax.set_xlim(2013.7, 2020.3); ax.set_xticks(years)
    ax.set_xlabel('Year', color=INK2, fontsize=9.5, labelpad=6)
    ax.set_ylabel('Number of condors', color=INK2, fontsize=9.5, labelpad=6)
    ax.annotate('wild', (2020, 329), xytext=(9, 5), textcoords='offset points',
                color=BLUE, fontsize=9.5, fontweight='bold', va='center')
    ax.annotate('captive', (2020, 175), xytext=(9, -2), textcoords='offset points',
                color=ORANGE, fontsize=9.5, fontweight='bold', va='center')
    leg = ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.34), ncol=2,
                    frameon=False, fontsize=9.5, handlelength=2.2,
                    columnspacing=2.0, labelcolor=INK)
    fig.subplots_adjust(right=0.86)
    return render(fig)

# ---------------------------------------------------------------- copper
def copper():
    labels = ['1889', '1902', '1909']
    x = [0, 1, 2]
    montana = [106, 267, 316]
    arizona = [32, 119, 291]
    michigan = [88, 170, 231]
    fig, ax = plt.subplots(figsize=(5.1, 3.05))
    style(ax)
    ax.plot(x, montana, color=BLUE, lw=2, marker='o', ms=6.5, mfc='white',
            mec=BLUE, mew=2, label='Montana', zorder=4, clip_on=False)
    ax.plot(x, arizona, color=ORANGE, lw=2, marker='s', ms=6, mfc='white',
            mec=ORANGE, mew=2, label='Arizona', zorder=3, clip_on=False)
    ax.plot(x, michigan, color=AQUA, lw=2, marker='^', ms=7, mfc='white',
            mec=AQUA, mew=2, label='Michigan', zorder=3, clip_on=False)
    ax.set_ylim(0, 400); ax.set_yticks([0, 100, 200, 300, 400])
    ax.set_xlim(-0.12, 2.12); ax.set_xticks(x); ax.set_xticklabels(labels)
    ax.set_xlabel('Year', color=INK2, fontsize=9.5, labelpad=6)
    ax.set_ylabel('Yearly copper production\n(in millions of pounds)',
                  color=INK2, fontsize=9.5, labelpad=6)
    for name, val, col, dy in (('Montana', 316, BLUE, 7),
                               ('Arizona', 291, ORANGE, -8),
                               ('Michigan', 231, AQUA, 0)):
        ax.annotate(name, (2, val), xytext=(9, dy), textcoords='offset points',
                    color=col, fontsize=9.5, fontweight='bold', va='center')
    ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.34), ncol=3,
              frameon=False, fontsize=9.5, handlelength=2.2,
              columnspacing=1.8, labelcolor=INK)
    fig.subplots_adjust(right=0.80)
    return render(fig)

if __name__ == '__main__':
    import json
    out = {'224428ac': condors(), '30c3aa98': copper()}
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'charts9_img.json'), 'w'))
    for k, v in out.items():
        print(k, len(v), 'chars')
