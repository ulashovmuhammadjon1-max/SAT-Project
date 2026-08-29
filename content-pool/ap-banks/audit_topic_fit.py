"""Find questions filed under the wrong CED topic.

The banks were written topic by topic, so a question can be perfectly correct
and still sit in the wrong place — a monopoly question in the perfect-competition
topic, an inflation question in the GDP topic. A student practising one topic
then meets material they have not studied, which is what this looks for.

The method is deliberately conservative. Each topic declares the vocabulary that
belongs to it and the vocabulary that belongs to OTHER topics; a question is
reported only when it carries foreign terms and none of its own. Reporting is
the point — every hit is read by a person before anything is moved, because a
keyword rule cannot tell a genuine misfile from a legitimate mention.

Word boundaries here use explicit lookarounds rather than \\b. This project has
produced the same bug four times: \\bpi never matched because a digit and a
letter are both \\w, a setting check matched the "fen" inside "fence", and
another matched "must" and the "moth" inside "months". A substring match in a
checker is worse than no check, because it trains you to ignore the output.
"""
import argparse
import importlib
import re
import sys

# Terms that mark a question as belonging to a particular topic. Only terms
# specific enough to discriminate are listed: "cost" appears everywhere in
# microeconomics and would flag nothing useful.
MICRO_MARKERS = {
    "1.3": ["production possibilities", "ppc", "frontier"],
    "1.4": ["comparative advantage", "absolute advantage", "terms of trade"],
    "2.3": ["price elasticity of demand", "elastic", "inelastic", "elasticity"],
    "2.6": ["consumer surplus", "producer surplus", "total surplus"],
    "2.8": ["price ceiling", "price floor", "deadweight loss", "excise tax"],
    "3.1": ["marginal product", "total product", "average product", "returns to scale",
            "diminishing marginal returns", "production function"],
    "3.2": ["fixed cost", "variable cost", "average total cost", "marginal cost",
            "average variable cost", "average fixed cost", "sunk cost"],
    "3.3": ["long-run average", "lrat", "economies of scale", "diseconomies",
            "minimum efficient scale"],
    "3.4": ["accounting profit", "economic profit", "implicit cost", "explicit cost",
            "normal profit"],
    "3.5": ["marginal revenue", "profit-maximizing", "shut down", "shutdown",
            "break-even", "mr = mc"],
    "3.6": ["entry", "exit", "long-run equilibrium", "constant-cost industry"],
    "3.7": ["perfect competition", "perfectly competitive", "price taker",
            "standardized product"],
    "4.1": ["market power", "barrier to entry", "barriers to entry", "market structure",
            "concentration"],
    "4.2": ["monopoly", "monopolist", "natural monopoly", "patent"],
    "4.3": ["price discrimination", "discriminating", "willingness to pay"],
    "4.4": ["monopolistic competition", "monopolistically competitive",
            "product differentiation", "excess capacity"],
    "4.5": ["oligopoly", "game theory", "nash", "dominant strategy", "cartel",
            "collusion", "payoff", "prisoner"],
    "5.1": ["marginal revenue product", "mrp", "derived demand", "factor market"],
    "5.3": ["marginal factor cost", "mfc"],
    "5.4": ["monopsony", "monopsonist"],
    "6.2": ["externality", "externalities", "spillover", "pigouvian", "corrective tax"],
    "6.3": ["public good", "private good", "common resource", "club good",
            "free rider", "free-rider", "non-rival", "nonrival", "excludable"],
    "6.5": ["gini", "lorenz", "inequality", "quintile", "poverty", "progressive tax",
            "regressive tax", "transfer payment"],
    "1.1": ["scarcity", "opportunity cost", "factors of production", "trade-off"],
    "1.2": ["economic system", "command economy", "market economy", "allocation"],
    "1.5": ["cost-benefit", "marginal benefit"],
    "1.6": ["marginal utility", "utility", "budget constraint", "consumer choice"],
    "2.1": ["law of demand", "demand curve", "substitute", "complement", "normal good",
            "inferior good", "shift"],
    "2.2": ["law of supply", "supply curve", "input price"],
    "2.4": ["price elasticity of supply"],
    "2.5": ["income elasticity", "cross-price elasticity"],
    "2.7": ["shortage", "surplus", "equilibrium"],
    "2.9": ["tariff", "quota", "import", "export", "world price"],
    "5.2": ["factor demand", "factor supply", "compensating"],
    "6.1": ["allocative efficiency", "productive efficiency", "socially efficient",
            "marginal social"],
    "6.4": ["antitrust", "regulation", "regulated", "fair-return", "price cap",
            "socially optimal pricing", "government intervention", "government failure"],
}

MACRO_MARKERS = {
    "1.2": ["production possibilities", "ppc", "frontier"],
    "1.3": ["comparative advantage", "absolute advantage", "terms of trade"],
    "2.1": ["gross domestic product", "gdp", "circular flow", "expenditure approach",
            "intermediate good"],
    "2.3": ["unemployment", "labor force", "frictional", "structural", "cyclical",
            "discouraged worker", "natural rate"],
    "2.4": ["consumer price index", "cpi", "price index", "inflation rate",
            "market basket", "deflator"],
    "2.5": ["shoe-leather", "menu cost", "unanticipated inflation", "disinflation",
            "deflation"],
    "2.6": ["real gdp", "nominal gdp", "base year"],
    "2.7": ["business cycle", "recession", "expansion", "peak", "trough",
            "recessionary gap", "inflationary gap", "output gap"],
    "3.1": ["aggregate demand", "wealth effect", "real balances", "interest rate effect"],
    "3.2": ["multiplier", "marginal propensity", "mpc", "mps"],
    "3.3": ["short-run aggregate supply", "sras", "sticky wage", "supply shock"],
    "3.4": ["long-run aggregate supply", "lras", "full employment output",
            "potential output"],
    "3.8": ["fiscal policy", "government spending", "tax cut", "expansionary fiscal",
            "contractionary fiscal"],
    "3.9": ["automatic stabilizer", "progressive tax", "transfer payment"],
    "4.1": ["bond", "stock", "financial asset", "liquidity"],
    "4.2": ["nominal interest", "real interest", "fisher"],
    "4.3": ["medium of exchange", "store of value", "unit of account", "fiat money",
            "m1", "m2"],
    "4.4": ["reserve requirement", "required reserve", "excess reserve", "money multiplier",
            "fractional reserve", "t-account"],
    "4.5": ["money market", "money demand", "money supply"],
    "4.6": ["monetary policy", "open market operation", "discount rate", "central bank"],
    "4.7": ["loanable funds", "national saving"],
    "5.2": ["phillips curve", "phillips"],
    "5.3": ["quantity theory", "velocity", "monetary neutrality", "hyperinflation"],
    "5.4": ["deficit", "national debt", "debt-to-gdp"],
    "5.5": ["crowding out", "crowd out"],
    "5.6": ["economic growth", "rule of 70", "productivity growth"],
    "6.1": ["balance of payments", "current account", "financial account",
            "capital account"],
    "6.2": ["exchange rate", "appreciat", "depreciat"],
    "6.3": ["foreign exchange", "currency market"],
    "6.5": ["net export"],
    "6.6": ["capital flow", "capital inflow", "capital outflow"],
    "1.1": ["scarcity", "opportunity cost", "factors of production", "trade-off"],
    "1.4": ["law of demand", "demand curve", "substitute", "complement", "normal good",
            "inferior good"],
    "1.5": ["law of supply", "supply curve", "input price"],
    "1.6": ["shortage", "surplus", "equilibrium"],
    "2.2": ["limitation", "underground economy", "non-market", "per capita"],
    "3.5": ["equilibrium in the ad-as", "short-run equilibrium", "long-run equilibrium"],
    "3.6": ["stagflation", "shift in aggregate", "short run"],
    "3.7": ["self-adjust", "wage adjust", "long run"],
    "5.1": ["policy mix", "policy action"],
    "5.7": ["public policy", "infrastructure", "human capital", "research and development"],
    "6.4": ["intervention", "peg", "sterilization", "fixed exchange", "floating"],
}


def has_term(text: str, term: str) -> bool:
    """Whole-term match with explicit lookarounds.

    \\b is wrong here: it treats a digit as a word character, so "m1" inside
    "m1 and m2" behaves differently from what you would expect, and a term
    ending in a letter would match inside a longer word.
    """
    return re.search(rf"(?<![A-Za-z0-9]){re.escape(term)}(?![A-Za-z0-9])", text) is not None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("modules", nargs="+")
    ap.add_argument("--subject", choices=["MICRO", "MACRO"], required=True)
    args = ap.parse_args()

    markers = MICRO_MARKERS if args.subject == "MICRO" else MACRO_MARKERS
    findings = 0

    for mod_name in args.modules:
        m = importlib.import_module(mod_name)
        code, title, _unit = m.TOPIC
        own = markers.get(code)
        if own is None:
            continue

        for i, item in enumerate(m.QUESTIONS, 1):
            text = (item["q"] + " " + " ".join(item["choices"]) + " " + item["why"]).lower()

            # A question that carries its own topic's vocabulary is at home,
            # whatever else it mentions.
            if any(has_term(text, t) for t in own):
                continue

            foreign = sorted(
                {
                    other
                    for other, terms in markers.items()
                    if other != code and any(has_term(text, t) for t in terms)
                }
            )
            if not foreign:
                continue

            # Only the suspicious shape is reported: a question that speaks of
            # exactly ONE other topic and none of its own. Matching several
            # topics is the signature of a legitimate cross-cutting question,
            # and reporting those is the noise that trains you to ignore the
            # output entirely.
            if len(foreign) != 1:
                continue
            findings += 1
            print(f"[LIKELY] {args.subject} {code} q{i}: reads as {foreign[0]}")
            print(f"         {item['q'][:110]}")

    print(f"\n{findings} question(s) to read.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
