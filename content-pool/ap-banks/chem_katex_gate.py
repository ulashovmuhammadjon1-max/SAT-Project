r"""Render every hand-written math span in the AP Chemistry banks through KaTeX.

    python3 chem_katex_gate.py            # every h*.py in this directory
    python3 chem_katex_gate.py h1_1 h1_2  # named modules only
    python3 chem_katex_gate.py --selftest # negative control

WHY THIS EXISTS SEPARATELY FROM ``chem_notation.py``. That module gates the
spans structurally -- balanced braces, an allow list of macros, placement. This
one actually renders them, and it renders at ``throwOnError: true``.

CLAUDE.md, from the Calculus/Statistics typesetting run: *"KaTeX must be checked
at throwOnError: true. Production renders at throwOnError: false, which shows a
broken span as red source text instead of failing, so a check that mirrors
production sees nothing. The checker has to be stricter than the site."* That is
exactly the situation here -- ``MathContent`` passes ``throwOnError: false``.

The node side is written to a temp file rather than kept in the repo, so there
is one place to read and no second copy to drift.
"""
import glob
import importlib
import json
import os
import re
import subprocess
import sys
import tempfile

_SPAN = re.compile(r"\\\((.*?)\\\)", re.S)

_NODE = r"""
const katex = require("katex");
const spans = JSON.parse(require("fs").readFileSync(process.argv[2], "utf8"));
const bad = [];
for (const s of spans) {
  try {
    katex.renderToString(s.tex, { throwOnError: true, output: "html" });
  } catch (e) {
    bad.push({ where: s.where, tex: s.tex, msg: String(e.message).slice(0, 160) });
  }
}
console.log(JSON.stringify({ n: spans.length, bad }));
"""


def collect(names):
    spans = []
    for name in names:
        mod = importlib.import_module(name)
        for i, item in enumerate(mod.QUESTIONS, 1):
            texts = [item["q"], item["why"]] + list(item["choices"])
            table = item.get("table")
            if table:
                texts += [str(h) for h in table["headers"]]
                texts += [str(c) for row in table["rows"] for c in row]
            for text in texts:
                for tex in _SPAN.findall(text):
                    spans.append({"where": f"{name} q{i}", "tex": tex})
    return spans


def render(spans):
    """Returns the list of spans KaTeX refused at throwOnError: true."""
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    with tempfile.TemporaryDirectory() as tmp:
        data = os.path.join(tmp, "spans.json")
        script = os.path.join(tmp, "gate.cjs")
        with open(data, "w") as fh:
            json.dump(spans, fh)
        with open(script, "w") as fh:
            fh.write(_NODE)
        # The script lives in a temp dir, so CommonJS resolution starts there
        # and never reaches the repo's node_modules. NODE_PATH points it back.
        env = dict(os.environ, NODE_PATH=os.path.join(root, "node_modules"))
        out = subprocess.run(["node", script, data], cwd=root, env=env,
                             capture_output=True, text=True)
    assert out.returncode == 0, f"node failed: {out.stderr[:400]}"
    return json.loads(out.stdout)


def main(names):
    spans = collect(names)
    if not spans:
        print("no math spans found -- nothing to render")
        return
    result = render(spans)
    for b in result["bad"]:
        print(f"FAIL {b['where']}: {b['tex']!r} -- {b['msg']}")
    assert not result["bad"], f"{len(result['bad'])} span(s) KaTeX will not render"
    print(f"OK  {result['n']} math span(s) across {len(names)} module(s) render at "
          "throwOnError: true.")


def _selftest():
    """A gate that cannot fail is worse than none. Prove this one fails."""
    good = [{"where": "control", "tex": r"6.022 \times 10^{23}"}]
    assert not render(good)["bad"], "a valid span was rejected"
    print("  control OK  a valid span renders")
    for tex in (r"\frac{1}{2", r"\nosuchmacro{x}", r"x^{"):
        bad = render([{"where": "control", "tex": tex}])["bad"]
        assert bad, f"CONTROL FAILED: KaTeX accepted {tex!r} at throwOnError true"
        print(f"  control OK  {tex!r} rejected: {bad[0]['msg'][:60]}")
    print("all chem_katex_gate controls behaved as required.")


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if "--selftest" in sys.argv:
        _selftest()
    else:
        mods = args or sorted(
            os.path.splitext(os.path.basename(p))[0]
            for p in glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                            "h[0-9]*.py")))
        main(mods)
