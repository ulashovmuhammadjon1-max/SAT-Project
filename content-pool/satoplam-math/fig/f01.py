import matplotlib.pyplot as plt
from fh6_lib import emit

fig, ax = plt.subplots(figsize=(4.6, 3.6))

# two vertical lines r and s
for x in (1.0, 2.0):
    ax.plot([x, x], [0.02, 2.57], color="black", lw=1.1)

# transversal k, slope -1, through (1,1.8) and (2,0.8)
ax.plot([0.28, 2.55], [2.52, 0.25], color="black", lw=1.1)

ax.text(0.20, 2.72, "$k$", ha="center", va="center", fontsize=13, style="italic")
ax.text(1.00, 2.72, "$r$", ha="center", va="center", fontsize=13, style="italic")
ax.text(2.00, 2.72, "$s$", ha="center", va="center", fontsize=13, style="italic")

ax.text(1.09, 1.93, r"$w^{\circ}$", ha="left", va="center", fontsize=13)
ax.text(1.09, 1.42, r"$x^{\circ}$", ha="left", va="center", fontsize=13)
ax.text(2.09, 0.93, r"$y^{\circ}$", ha="left", va="center", fontsize=13)
ax.text(2.09, 0.42, r"$z^{\circ}$", ha="left", va="center", fontsize=13)

ax.set_xlim(0.0, 2.75)
ax.set_ylim(0.0, 2.95)
ax.set_aspect("equal")
ax.axis("off")
fig.text(0.5, 0.005, "Note: Figure not drawn to scale", ha="center", fontsize=10)

emit(fig, "satmath-ma3-lines-angles-18",
     "A transversal line k crossing two vertical lines r and s. Four angles are "
     "labelled with variables: w and x at the intersection with r, y and z at the "
     "intersection with s.")
