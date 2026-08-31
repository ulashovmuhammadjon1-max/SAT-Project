"""Structural gate for AP U.S. Government 4.9 Ideology and Economic Policy.

gov345_check plus the four usgov_anchor helpers, plus three content gates.
Two learning objectives here, which is unusual, and each brings its own way of
going wrong.

  _actors       EK 4.9.B.1 and EK 4.9.B.2 both define their policy by WHO TAKES
                THE ACTION -- Congress and the president for fiscal, the Federal
                Reserve for monetary -- before saying anything about instruments
                or effects. Reversing them is the classic error, and a student
                who has learned the pair as "taxes and spending" against
                "interest rates" has the right examples and no rule for a case
                the examples do not cover. The gate refuses any key that gives
                either policy the other's actor.

                It also pins the Fed's three properties, each separately
                droppable: INDEPENDENT agency, MAXIMUM EMPLOYMENT, and PRICE
                STABILITY. Two goals, not one. A summary that keeps only price
                stability describes a different institution from the one the
                framework describes, and the difference matters precisely when
                the two goals point different ways.

  _positions    EK 4.9.A.1's three positions are comparatives -- MORE, FEWER,
                LITTLE OR NO -- and the libertarian one carries two exceptions
                the framework states: protecting property rights and voluntary
                trade. Those exceptions are inside the position, not outside it,
                so "libertarians favor no government" is not what the CED says.
                The gate keeps conservative at FEWER, keeps the libertarian
                exceptions, and refuses any key that evaluates the three.

  _undefined_terms
                EK 4.9.B.1 NAMES Keynesian and supply-side positions and DEFINES
                NEITHER. Every textbook defines them, which is exactly the
                danger: supplying those definitions would put content the
                framework does not state beside content it does, with the same
                authority and nothing to tell a student which is which. It is
                the same refusal 3.13 makes about affirmative action outcomes
                and 3.12 about the separate but equal case. Item 17 makes the
                naming itself the question. The gate refuses any key that
                defines either term, and pins item 17's key to the fact that the
                framework stops at naming them.

                This one is FLAGGED, not hidden. A teacher may well want to add
                the definitions, and they should know the bank did not get them
                from the CED rather than discovering a silent gap.

SKILL 3.E SHAPES ALL NINE DATA ITEMS. The suggested skill is "explain possible
limitations of the data provided", which is about what data CANNOT show, so each
table is followed by a limitation question: the interest rate table cannot
establish the direction of causation, the action table cannot show whether an
action worked, and the cross-country table cannot separate regulation from
everything else four countries differ in. The cross-country table is also built
with NO consistent relationship between regulation and growth, which is what
lets item 29 ask what the data supports without the module taking a side on a
question EK 4.9.A.1 leaves as three positions.
"""
import gov345_check as gc
import usgov_anchor as ua
import v4_9

ANCHORS = {
 1: "More governmental regulation of the marketplace",
 2: "Fewer regulations of the marketplace",
 3: "Little or no regulation beyond the protection of property rights and voluntary trade",
 4: "while libertarian ideologies favor little or no regulation apart from two named",
 5: "are themselves government functions the position supports",
 6: "since it favors more governmental regulation of the marketplace",
 7: "defined relative to one another rather than by any particular amount",
 8: "Which of the three positions produces better economic outcomes",
 9: "Congress and the president",
 10: "The Federal Reserve",
 11: "since the framework defines each policy by its actor",
 12: "since it consists of actions taken by Congress and the president",
 13: "since it is an action taken by the Federal Reserve",
 14: "An independent agency",
 15: "Maximum employment and price stability",
 16: "so the Fed's task involves weighing them against each other",
 17: "It names them without defining either",
 18: "since the passage argues that self-interest rather than direction produces",
 19: "which is not the same as a claim that regulation is always harmful",
 20: "and the second asks how fiscal and monetary actions influence economic conditions",
 21: "so a table showing an association rarely establishes which variable affected which",
 22: "and in the fourth period both move in the opposite direction",
 23: "to influence interest rates which affect broader economic conditions",
 24: "or whether the central bank was responding to conditions rather than producing them",
 25: "and every action taken by the Federal Reserve as monetary",
 26: "and EK 4.9.B.2's assignment of monetary policy to the Federal Reserve",
 27: "but reports nothing about whether any action achieved what it was intended",
 28: "is neither the least nor the most regulated of the four",
 29: "since the table shows no consistent relationship",
 30: "so no effect of regulation can be separated out",
}

GROUNDING = {
 1: "EK 4.9.A.1, verbatim: 'Liberal ideologies favor more governmental regulation of the "
    "marketplace.' MORE is a comparative, defined against the other two positions.",
 2: "EK 4.9.A.1: 'conservative ideologies favor fewer regulations.' FEWER is not an absence, "
    "which is the whole difference from the libertarian position in the same sentence.",
 3: "EK 4.9.A.1: 'libertarian ideologies favor little or no regulation of the marketplace "
    "beyond the protection of property rights and voluntary trade.' The exceptions are the "
    "framework's own.",
 4: "EK 4.9.A.1's two phrases set against each other: FEWER regulations against LITTLE OR NO "
    "regulation with two named exceptions.",
 5: "EK 4.9.A.1's word BEYOND, which places protecting property rights and voluntary trade "
    "inside the libertarian position rather than outside it. A market needs enforceable "
    "ownership and enforceable agreements, so favoring markets is not favoring no government.",
 6: "EK 4.9.A.1's arrangement applied: a new requirement on firms is more regulation, and the "
    "framework ranks the three positions by how much of it each favors.",
 7: "EK 4.9.A.1's comparatives MORE and FEWER, which need something to compare against and "
    "find it in the other positions named in the same sentence.",
 8: "EK 4.9.A.1 read for what it omits: three positions described, none evaluated.",
 9: "EK 4.9.B.1, verbatim: 'Fiscal policy consists of actions taken by Congress and the "
    "president to influence economic conditions.' Actor first.",
 10: "EK 4.9.B.2, verbatim: 'Monetary policy consists of actions taken by the Federal Reserve "
     "(the Fed) to influence interest rates which affect broader economic conditions.'",
 11: "EK 4.9.B.1 and EK 4.9.B.2 both beginning with the actor, which supplies a rule rather "
     "than a list of examples. Taxes against interest rates gives examples and no criterion.",
 12: "EK 4.9.B.1's actor applied. Aiming at economic conditions does not make an action "
     "monetary, because EK 4.9.B.2 assigns that category to a different institution.",
 13: "EK 4.9.B.2's actor applied to an action other than an interest rate change. The mention "
     "of interest rates describes what the Fed influences rather than all it may do.",
 14: "EK 4.9.B.2: 'The Fed is an independent agency.' Its independence is what distinguishes "
     "monetary from fiscal policy institutionally.",
 15: "EK 4.9.B.2: the Fed 'seeks to achieve maximum employment and price stability.' Two "
     "goals in one clause.",
 16: "EK 4.9.B.2's two goals, named without ranking. Two objectives can recommend different "
     "courses at once, and the framework's silence on priority is part of what it says.",
 17: "EK 4.9.B.1 read for where it stops: it names Keynesian and supply-side positions and "
     "defines neither, so any definition would come from outside the framework's statement.",
 18: "Adam Smith, 'The Wealth of Nations' (required document), quoted verbatim; the CED "
     "attaches it to 4.9.A and 4.9.B. The passage locates provision in participants' own "
     "interest rather than in direction of them.",
 19: "'The Wealth of Nations', quoted verbatim. The passage describes a mechanism and makes no "
     "claim about the effects of regulation, so the inference goes beyond it. EK 4.9.A.1 "
     "records three positions precisely because the question is contested.",
 20: "LO 4.9.A and LO 4.9.B compared: one about ideological positions on regulation, one about "
     "the mechanics of two kinds of policy action.",
 21: "CED skill 3.E for this topic. An association between two economic series is consistent "
     "with several explanations, including a third factor and reverse causation.",
 22: "Data item, CED skill 3.E. Every series and its direction is recomputed below.",
 23: "EK 4.9.B.2 located in the table: a target interest rate beside the broader economic "
     "conditions the framework says it affects.",
 24: "CED skill 3.E: the limitation is inference, not accuracy. A central bank lowering rates "
     "BECAUSE unemployment is rising produces exactly this pattern without having caused it.",
 25: "Data item, CED skill 3.E. The classification is checked against the institution column.",
 26: "EK 4.9.B.1 and EK 4.9.B.2's assignment of each policy to its actor, located in a table "
     "whose classification column follows its institution column exactly.",
 27: "CED skill 3.E: every column concerns the action and its author and none reports an "
     "outcome, so the table settles classification and leaves effectiveness untouched.",
 28: "Data item, CED skill 3.E. The regulation and growth series are recomputed below.",
 29: "EK 4.9.A.1's three positions against a table with no consistent pattern, which is what "
     "leaves all three intact. Recomputed below.",
 30: "CED skill 3.E: four countries in one year differ in population, resources, institutions "
     "and history, any of which could account for the differences shown.",
}

RATE, UNEMP, INFL = ("Target interest rate (%)", "Unemployment rate (%)", "Inflation rate (%)")
INSTITUTION, CLASSIFICATION = "Institution taking it", "Classification"
REGULATED, GROWTH, C_UNEMP = ("Economic activity subject to regulation (%)", "Growth rate (%)",
                              "Unemployment rate (%)")


def _col(t, header):
    j = t["headers"].index(header)
    return [gc.num(r[j]) for r in t["rows"]]


def _text(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def q22(t):
    """Rate falls and unemployment rises for three periods, then both reverse."""
    rate, un, inf = _col(t, RATE), _col(t, UNEMP), _col(t, INFL)
    assert rate[0] > rate[1] > rate[2], f"the rate does not fall across the first three: {rate}"
    assert un[0] < un[1] < un[2], f"unemployment does not rise across the first three: {un}"
    assert rate[3] > rate[2] and un[3] < un[2], f"the fourth period does not reverse both"
    assert not all(x < y for x, y in zip(inf, inf[1:])), \
        "inflation rises monotonically, which the key's last distractor denies"
    return (f"rate {', '.join(f'{x:.1f}' for x in rate)}; unemployment "
            f"{', '.join(f'{x:.1f}' for x in un)} -- opposite for three periods, both reverse "
            "in the fourth")


def q23(t):
    """The table carries an interest rate and broader conditions, and no fiscal actor."""
    heads = [h.lower() for h in t["headers"]]
    assert any("interest rate" in h for h in heads), f"no interest rate column: {heads}"
    assert any("unemployment" in h for h in heads) and any("inflation" in h for h in heads), \
        f"the broader conditions are missing: {heads}"
    for h in heads:
        assert "congress" not in h and "president" not in h, \
            f"column {h!r} names a fiscal actor, which this table does not measure"
    return "an interest rate beside unemployment and inflation -- EK 4.9.B.2's variables"


def q24(t):
    """Two series move together, which is consistent with influence either way."""
    rate, un = _col(t, RATE), _col(t, UNEMP)
    assert len(rate) == len(un) >= 4, "too few periods to describe an association"
    opposite = sum(1 for a, b, c, d in zip(rate, rate[1:], un, un[1:])
                   if (b - a) * (d - c) < 0)
    assert opposite >= 2, f"the two series move oppositely in only {opposite} transitions"
    assert len(t["headers"]) == 4, "the table no longer carries both conditions"
    return (f"the two series move oppositely in {opposite} of {len(rate) - 1} transitions -- an "
            "association, with no column identifying which moved first")


def q25(t):
    """Classification follows the institution exactly, two of each."""
    inst = [i.lower() for i in _text(t, INSTITUTION)]
    cls = [c.lower() for c in _text(t, CLASSIFICATION)]
    for i, c in zip(inst, cls):
        if "federal reserve" in i:
            assert c == "monetary", f"{i!r} classified {c!r}"
        else:
            assert "congress" in i and "president" in i, f"unexpected institution {i!r}"
            assert c == "fiscal", f"{i!r} classified {c!r}"
    assert cls.count("fiscal") == 2 and cls.count("monetary") == 2, f"classifications {cls}"
    return f"classification tracks the institution in all {len(cls)} rows: {', '.join(cls)}"


def q26(t):
    """Both actors appear, so the table exercises both framework statements."""
    inst = [i.lower() for i in _text(t, INSTITUTION)]
    assert any("federal reserve" in i for i in inst), "no monetary actor in the table"
    assert any("congress" in i for i in inst), "no fiscal actor in the table"
    return "both of the framework's actors appear, each with two actions"


def q27(t):
    """No column reports an outcome, which is the limitation the item names."""
    heads = [h.lower() for h in t["headers"]]
    for h in heads:
        for outcome in ("unemployment", "inflation", "growth", "achieved", "effect", "result"):
            assert outcome not in h, \
                f"column {h!r} reports an outcome, so the key's limitation does not hold"
    return f"columns are {', '.join(heads)} -- author and classification, no outcome"


def q28(t):
    """Highest growth belongs to neither extreme of the regulation range."""
    reg, gro = _col(t, REGULATED), _col(t, GROWTH)
    names = _text(t, "Country")
    assert reg == sorted(reg), f"the regulation column is not ordered: {reg}"
    top = gro.index(max(gro))
    assert top not in (0, len(gro) - 1), \
        f"the highest growth belongs to {names[top]!r}, an extreme of the regulation range"
    assert gro != sorted(gro) and gro != sorted(gro, reverse=True), \
        f"growth is monotonic in regulation: {gro}"
    return (f"regulation {', '.join(f'{x:.0f}' for x in reg)}; growth "
            f"{', '.join(f'{x:.1f}' for x in gro)} -- highest at {names[top]!r}, an interior row")


def q29(t):
    """No consistent relationship in either economic condition."""
    reg, gro, un = _col(t, REGULATED), _col(t, GROWTH), _col(t, C_UNEMP)
    for name, series in (("growth", gro), ("unemployment", un)):
        assert series != sorted(series) and series != sorted(series, reverse=True), \
            f"{name} moves monotonically with regulation, so the table would favour a position"
    return ("neither growth nor unemployment moves monotonically with the regulation share -- "
            "no row pattern supports any one position")


def q30(t):
    """One year, four countries, and nothing in the table holds anything else constant."""
    assert len(t["rows"]) == 4, f"{len(t['rows'])} countries, not four"
    heads = [h.lower() for h in t["headers"]]
    for h in heads:
        for confounder in ("population", "resources", "institutions", "history", "year",
                           "period"):
            assert confounder not in h, \
                f"column {h!r} controls for {confounder!r}, weakening the stated limitation"
    return (f"{len(t['rows'])} countries, one year, and no column holding anything else "
            "constant")


# --- module-specific content gates -------------------------------------------

_FISCAL_ACTOR = "congress and the president"
_MONETARY_ACTOR = "federal reserve"


def _actors(module):
    """Fiscal belongs to Congress and the president; monetary to the Fed."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        at = key.find("fiscal policy")
        if at >= 0 and _MONETARY_ACTOR in key[at:at + 120] and _FISCAL_ACTOR not in key:
            bad.append(f"q{i} key: attaches the Federal Reserve to fiscal policy; EK 4.9.B.1 "
                       "assigns fiscal policy to Congress and the president")
        at = key.find("monetary policy")
        if at >= 0 and _FISCAL_ACTOR in key[at:at + 120] and _MONETARY_ACTOR not in key:
            bad.append(f"q{i} key: attaches Congress and the president to monetary policy; EK "
                       "4.9.B.2 assigns monetary policy to the Federal Reserve")
    q9 = module.QUESTIONS[8]
    if _FISCAL_ACTOR not in q9["choices"][q9["ans"]].lower():
        bad.append("q9: the key no longer names EK 4.9.B.1's actor, Congress and the president")
    q10 = module.QUESTIONS[9]
    if _MONETARY_ACTOR not in q10["choices"][q10["ans"]].lower():
        bad.append("q10: the key no longer names EK 4.9.B.2's actor, the Federal Reserve")
    q14 = module.QUESTIONS[13]
    if "independent" not in q14["choices"][q14["ans"]].lower():
        bad.append("q14: the key no longer states that the Fed is an INDEPENDENT agency")
    q15 = module.QUESTIONS[14]
    k15 = q15["choices"][q15["ans"]].lower()
    for goal in ("maximum employment", "price stability"):
        if goal not in k15:
            bad.append(f"q15: the key has dropped {goal!r}; EK 4.9.B.2 names TWO goals, and a "
                       "summary keeping one describes a different institution")
    if bad:
        print(f"FAIL {module.__name__} actors")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} actors: fiscal policy keeps Congress and the president, "
          "monetary policy keeps the Federal Reserve, and the Fed keeps its independence and "
          "both of its goals")


def _positions(module):
    """EK 4.9.A.1's three positions keep their comparatives and the libertarian exceptions."""
    bad = []
    pins = {
        1: ("more governmental regulation", "liberal"),
        2: ("fewer regulations", "conservative"),
        3: ("little or no regulation", "libertarian"),
    }
    for n, (clause, who) in pins.items():
        key = module.QUESTIONS[n - 1]["choices"][module.QUESTIONS[n - 1]["ans"]].lower()
        if clause not in key:
            bad.append(f"q{n}: the {who} key no longer carries EK 4.9.A.1's own phrase "
                       f"{clause!r}")
    q3 = module.QUESTIONS[2]
    k3 = q3["choices"][q3["ans"]].lower()
    for exc in ("property rights", "voluntary trade"):
        if exc not in k3:
            bad.append(f"q3: the libertarian key has dropped {exc!r}; EK 4.9.A.1 places both "
                       "exceptions inside the position with the word BEYOND")
    verdicts = ("produces the best outcomes", "is the correct position",
                "is better for the economy", "has been shown to work")
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        stem = item["q"].lower()
        if "not state" in stem:
            continue
        for v in verdicts:
            if v in key:
                bad.append(f"q{i} key: evaluates one of EK 4.9.A.1's positions ({v!r}); the "
                           "framework describes three and evaluates none")
    if bad:
        print(f"FAIL {module.__name__} positions")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} positions: EK 4.9.A.1's three comparatives survive, the "
          "libertarian exceptions for property rights and voluntary trade with them, and no "
          "key evaluates any of the three")


# Definitions the CED does not supply. EK 4.9.B.1 names Keynesian and
# supply-side and defines neither, so a key stating what either holds would be
# outside content wearing the framework's authority.
_DEFINITIONS = (
    "keynesian position holds", "supply-side position holds",
    "keynesian ideologies favor", "supply-side ideologies favor",
    "keynesians argue", "supply-side economists argue",
    "keynesian, meaning", "supply-side, meaning",
)


def _undefined_terms(module):
    """Neither Keynesian nor supply-side may be defined: the framework does not."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        for label, s in ([("key", item["choices"][item["ans"]]), ("why", item["why"])]
                         + [(f"choice {'ABCDE'[k]}", c)
                            for k, c in enumerate(item["choices"])]):
            low = s.lower()
            for d in _DEFINITIONS:
                if d in low:
                    bad.append(f"q{i} {label}: defines a term the framework only names ({d!r}). "
                               "EK 4.9.B.1 says fiscal policy 'includes Keynesian and "
                               "supply-side positions' and stops, so a definition here would "
                               "be outside content carrying the CED's authority")
    q17 = module.QUESTIONS[16]
    k17 = q17["choices"][q17["ans"]].lower()
    if "without defining" not in k17:
        bad.append("q17: the key no longer records that EK 4.9.B.1 names the two positions "
                   "without defining them, which is the honest answer for this item")
    if bad:
        print(f"FAIL {module.__name__} undefined terms")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} undefined terms: neither Keynesian nor supply-side is "
          "defined anywhere in the module, matching EK 4.9.B.1, which names both and defines "
          "neither -- flagged in the module header so a teacher knows it is a CED gap")


ua.shape(v4_9)
ua.check(v4_9, ANCHORS, GROUNDING)
ua.notation(v4_9)
_actors(v4_9)
_positions(v4_9)
_undefined_terms(v4_9)
gc.check(v4_9, arith={22: q22, 23: q23, 24: q24, 25: q25, 26: q26, 27: q27,
                      28: q28, 29: q29, 30: q30})
