import base64, io, json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fh-3.jsonl")
PREVIEW = "/tmp/claude-0/-home-user-SAT-Project/16335d00-5283-5db6-a7a3-023a1a5fae45/scratchpad/prev"
os.makedirs(PREVIEW, exist_ok=True)

matplotlib.rcParams.update({
    "font.family": "DejaVu Sans",
    "mathtext.fontset": "dejavusans",
    "axes.edgecolor": "black",
    "text.color": "black",
    "axes.labelcolor": "black",
    "xtick.color": "black",
    "ytick.color": "black",
    "savefig.facecolor": "white",
    "figure.facecolor": "white",
})


def emit(fig, qid, alt, note=""):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=110, bbox_inches="tight",
                pad_inches=0.12, facecolor="white")
    plt.close(fig)
    data = buf.getvalue()
    with open(os.path.join(PREVIEW, qid + ".png"), "wb") as f:
        f.write(data)
    kb = len(data) / 1024.0
    uri = "data:image/png;base64," + base64.b64encode(data).decode("ascii")
    rec = {"id": qid, "imageUrl": uri, "alt": alt, "note": note}
    with open(OUT, "a") as f:
        f.write(json.dumps(rec) + "\n")
    print("%-46s %6.1f KB" % (qid, kb))
    return kb


def already():
    if not os.path.exists(OUT):
        return set()
    return {json.loads(l)["id"] for l in open(OUT) if l.strip()}
