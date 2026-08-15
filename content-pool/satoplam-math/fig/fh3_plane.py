"""Coordinate-plane helper matching the SATashkent books' look."""
import numpy as np

GRID = "#c4c4c4"


def plane(ax, xlim, ylim, gridx=1.0, gridy=1.0,
          xticks=None, yticks=None, xlabels=None, ylabels=None,
          axis_arrows=True, grid_dashed=False, label_fs=10,
          xname='x', yname='y', xtick_pos='below', ytick_pos='left',
          grid_range=None):
    """Draw gridlines, axes with arrowheads, and tick labels."""
    x0, x1 = xlim
    y0, y1 = ylim
    gx0, gx1, gy0, gy1 = grid_range if grid_range else (x0, x1, y0, y1)
    ls = (0, (5, 4)) if grid_dashed else '-'
    if gridx:
        v = np.arange(np.ceil(gx0 / gridx) * gridx, gx1 + 1e-9, gridx)
        for t in v:
            ax.plot([t, t], [gy0, gy1], color=GRID, lw=0.6, ls=ls, zorder=0)
    if gridy:
        h = np.arange(np.ceil(gy0 / gridy) * gridy, gy1 + 1e-9, gridy)
        for t in h:
            ax.plot([gx0, gx1], [t, t], color=GRID, lw=0.6, ls=ls, zorder=0)

    ap = dict(arrowstyle='-|>', color='black', lw=1.2,
              mutation_scale=9, shrinkA=0, shrinkB=0)
    if axis_arrows:
        ax.annotate('', xy=(x1, 0), xytext=(gx0, 0), arrowprops=ap, zorder=3)
        ax.annotate('', xy=(0, y1), xytext=(0, gy0), arrowprops=ap, zorder=3)
    else:
        ax.plot([gx0, x1], [0, 0], color='black', lw=1.2, zorder=3)
        ax.plot([0, 0], [gy0, y1], color='black', lw=1.2, zorder=3)

    tl = 0.10 * (gridy or 1)
    if xticks is not None:
        labs = xlabels if xlabels is not None else [
            ('%g' % t) for t in xticks]
        for t, s in zip(xticks, labs):
            ax.plot([t, t], [-tl, tl], color='black', lw=1.0, zorder=3)
            if xtick_pos == 'below':
                ax.text(t, -tl - 0.14 * (gridy or 1), s, ha='center',
                        va='top', fontsize=label_fs, zorder=4)
    tlx = 0.10 * (gridx or 1)
    if yticks is not None:
        labs = ylabels if ylabels is not None else [
            ('%g' % t) for t in yticks]
        for t, s in zip(yticks, labs):
            ax.plot([-tlx, tlx], [t, t], color='black', lw=1.0, zorder=3)
            if ytick_pos == 'left':
                ax.text(-tlx - 0.16 * (gridx or 1), t, s, ha='right',
                        va='center', fontsize=label_fs, zorder=4)

    if xname:
        ax.text(x1 - 0.02 * (x1 - x0), 0.10 * (y1 - y0), xname, ha='right',
                va='bottom', fontsize=label_fs + 2, style='italic')
    if yname:
        ax.text(0.03 * (x1 - x0), y1 - 0.02 * (y1 - y0), yname, ha='left',
                va='top', fontsize=label_fs + 2, style='italic')

    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
    ax.axis('off')
