"""Redraws every figure in the screenshot test from verified data (CLAUDE.md rule 3:
real figures, never a prose description). Run: python3 figures.py"""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

def save(fig, name):
    fig.savefig(f"figures/{name}.png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)

# Math M2 Hard Q7: right rectangular pyramid, l = 14, w = 7, height h.
def pyramid():
    fig, ax = plt.subplots(figsize=(3.6, 3.4))
    A, B, C, D = (0.0, 1.4), (1.8, 0.0), (4.0, 1.2), (2.2, 2.6)  # base corners (D hidden)
    O = ((A[0]+C[0])/2, (A[1]+C[1])/2)                            # base centre
    P = (O[0], 5.0)                                               # apex
    k = dict(color="black", lw=1.4)
    for s, e in [(A, B), (B, C), (P, A), (P, B), (P, C)]:
        ax.plot([s[0], e[0]], [s[1], e[1]], **k)
    for s, e in [(A, D), (D, C), (P, D), (P, O)]:
        ax.plot([s[0], e[0]], [s[1], e[1]], color="black", lw=1, ls=(0, (4, 3)))
    sq = 0.18
    ax.plot([O[0], O[0]+sq, O[0]+sq], [O[1]+sq, O[1]+sq, O[1]], color="black", lw=0.9)
    ax.text(0.75, 0.55, r"$w$", fontsize=13, ha="center")
    ax.text(3.05, 0.4, r"$\ell$", fontsize=13, ha="center")
    ax.text(O[0]+0.12, 3.3, r"$h$", fontsize=13)
    ax.set_aspect("equal"); ax.axis("off")
    save(fig, "m2h_q7_pyramid")

# Math M2 Hard Q8: graph of y = f(x) - 19 = -15/8 x - 15/2, points (-4, 0) and (0, -7.5).
def line_graph():
    fig, ax = plt.subplots(figsize=(3.6, 3.6))
    xs = [-5.0, 1.3]
    ax.plot(xs, [-15/8*x - 7.5 for x in xs], color="black", lw=1.8)
    ax.plot([-4, 0], [0, -7.5], "o", color="black", ms=4)
    ax.axhline(0, color="black", lw=0.9); ax.axvline(0, color="black", lw=0.9)
    ax.set_xlim(-6.5, 5); ax.set_ylim(-11, 3.5)
    ax.set_xticks([-6, -4, -2, 2, 4]); ax.set_yticks([2.5, -2.5, -5.0, -7.5, -10.0])
    ax.set_xticks(range(-6, 5), minor=True); ax.set_yticks([x/2 for x in range(-22, 7)], minor=True)
    ax.grid(which="both", color="#D9DEE5", lw=0.6)
    ax.set_xlabel("x"); ax.set_ylabel("y", rotation=0)
    ax.tick_params(labelsize=8)
    save(fig, "m2h_q8_line")

pyramid(); line_graph()
print("figures written")
