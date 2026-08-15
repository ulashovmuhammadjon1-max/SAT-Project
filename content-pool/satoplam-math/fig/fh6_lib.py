import base64, io, json, os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fh-6.jsonl")

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.edgecolor": "black",
    "axes.labelcolor": "black",
    "text.color": "black",
    "xtick.color": "black",
    "ytick.color": "black",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
})


def emit(fig, qid, alt, note="", dpi=110):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi, bbox_inches="tight",
                facecolor="white", pad_inches=0.12)
    plt.close(fig)
    raw = buf.getvalue()
    uri = "data:image/png;base64," + base64.b64encode(raw).decode("ascii")
    line = json.dumps({"id": qid, "imageUrl": uri, "alt": alt, "note": note})
    with open(OUT, "a") as f:
        f.write(line + "\n")
    print("wrote %-45s %6.1f KB" % (qid, len(raw) / 1024.0))
    if len(raw) > 120 * 1024:
        print("  !! OVER 120 KB")
