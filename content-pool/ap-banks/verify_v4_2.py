"""Structural gate for AP U.S. Government 4.2 Political Socialization.

gov345_check plus the four usgov_anchor helpers, plus three content gates, one
for each of the three things this topic's two sentences contain that a summary
loses.

  _outputs        EK 4.2.A.1 says socialization develops political "beliefs,
                  values, opinions, AND BEHAVIORS". Four, and the fourth is the
                  one that goes. Dropping it turns the topic into an account of
                  what people think, when the framework's own list ends with
                  what they do -- which is what makes voting and joining an
                  organization outputs of socialization rather than separate
                  subjects. The gate pins all four in the defining key and
                  refuses any key that says the process produces attitudes only.

  _agents         EK 4.2.A.1 names FIVE contributors, and the fifth carries a
                  parenthesis: social environments, "including civic and
                  religious organizations". Lists in the wild stop at four, at
                  media, and the category that disappears is the one the
                  framework troubled to spell out. The gate pins all five and
                  the parenthesis, and refuses any key claiming there are four.

  _both_ways      EK 4.2.A.2 says U.S. political culture "has BOTH INFLUENCED
                  AND BEEN INFLUENCED BY the values of other countries". Half a
                  sentence is available in either direction, and which half a
                  reader keeps depends on what they already believed -- which is
                  exactly why a bank must keep both. The gate refuses any key
                  stating one direction while denying or omitting the other.

WHY NINE DATA ITEMS
-------------------
The suggested skill here is 3.A, DESCRIBE THE DATA PRESENTED: the most purely
quantitative skill in the course and the only topic in Unit 4 assigned it. So
three tables rather than the usual two, and each is built on one of the three
losses above -- the agents, the two directions of influence, and the four
outputs. The arithmetic checks below recompute every claim in all nine items,
including the two that exist to be corrected.
"""
import gov345_check as gc
import usgov_anchor as ua
import v4_2

ANCHORS = {
 1: "The process by which individuals develop political beliefs, values, opinions, and",
 2: "Beliefs, values, opinions, and behaviors",
 3: "an account of what people do politically",
 4: "Political behaviors, one of the four things the framework says socialization develops",
 5: "the more general commitments those positions draw on",
 6: "unfolds over time through repeated influence",
 7: "Family, schools, peers, media, and social environments",
 8: "Civic and religious organizations",
 9: "A social environment, which the framework's parenthesis says includes civic",
 10: "Family",
 11: "Schools, touching both beliefs and behaviors",
 12: "Peers",
 13: "A religious organization in which a person participates regularly",
 14: "Its democratic ideals, principles, and core values",
 15: "both influenced and been influenced by the values of other countries",
 16: "one half of a sentence that the framework writes in both directions",
 17: "As the two directions of influence the framework says globalization has produced",
 18: "describes the culture those attitudes are acquired within",
 19: "five contributors that operate throughout a person's life",
 20: "Socialization is the process through which attitudes develop, and ideology is shaped",
 21: "and the share naming it rises across the three groups",
 22: "Peers, falling from 16 percent to 5 percent",
 23: "so family leads there as well",
 24: "Two of the four practices spread outward from United States practice and two were",
 25: "both influenced and been influenced by the values of other countries",
 26: "The table records 8 instances of the United States adopting a practice from abroad",
 27: "changed for the largest share of respondents and values for the smallest",
 28: "list of what political socialization develops",
 29: "Every category changed for a substantial share of these adult respondents",
 30: "lists the contributors without ranking them against one another",
}
# Item 25 keys on the same sentence of EK 4.2.A.2 as item 15, so its anchor is
# written against its own choice text rather than reused; usgov_anchor checks
# an anchor against its own question's five choices, not across the module.
ANCHORS[25] = "That U.S. political culture has both influenced and been influenced"

GROUNDING = {
 1: "EK 4.2.A.1, verbatim: 'Political socialization refers to the process by which individuals "
    "develop political beliefs, values, opinions, and behaviors.'",
 2: "EK 4.2.A.1's four outputs. The fourth, BEHAVIORS, is the one a summary drops.",
 3: "EK 4.2.A.1's fourth output read for what it adds: the process reaches conduct as well as "
    "attitude, which puts voting and joining an organization on the framework's own list.",
 4: "EK 4.2.A.1's fourth output applied to attendance at a public meeting, which is conduct. "
    "Nothing in the definition confines the process to attitudes or to an age group.",
 5: "EK 4.2.A.1 lists opinions and values as separate outputs, and EK 4.1.A.1 describes core "
    "values as things whose different interpretations produce different positions. A framework "
    "treating them as synonyms would not need both words.",
 6: "EK 4.2.A.1's noun PROCESS and its verb phrase CONTRIBUTE TO THE DEVELOPMENT, both of "
    "which describe something gradual rather than a single moment.",
 7: "EK 4.2.A.1's five contributors: 'Family, schools, peers, media, and social environments.'",
 8: "EK 4.2.A.1's parenthesis after social environments: 'including civic and religious "
    "organizations' -- course content rather than an example a reader supplies.",
 9: "EK 4.2.A.1's fifth contributor applied. A neighborhood association is a civic "
    "organization, and the framework names five contributors rather than four.",
 10: "EK 4.2.A.1's first named contributor, applied to the plainest case of its operation.",
 11: "EK 4.2.A.1's second contributor together with two of its four outputs: an understanding "
     "(belief) and an intention to act (behavior).",
 12: "EK 4.2.A.1's third contributor: people of similar age influencing one another outside a "
     "family or institutional setting.",
 13: "LO 4.2.A's phrase CULTURAL FACTORS, which attaches to EK 4.2.A.1's fifth contributor and "
     "its parenthesis. The distractors describe institutional rules rather than settings.",
 14: "EK 4.2.A.2, verbatim: 'U.S. political culture is defined by its democratic ideals, "
     "principles, and core values.' This is what links the topic to EK 4.1.A.1's four values.",
 15: "EK 4.2.A.2, verbatim: 'U.S. political culture has both influenced and been influenced by "
     "the values of other countries.' Both halves are the framework's own.",
 16: "EK 4.2.A.2 read against a one-way summary. The outward claim is not false; it is half of "
     "a sentence reported as though it were all of it.",
 17: "EK 4.2.A.2 applied to a scenario containing one instance of each direction.",
 18: "EK 4.2.A.1 and EK 4.2.A.2 read together: an individual-level process, and the culture it "
     "runs within together with how that culture has changed.",
 19: "EK 4.2.A.1's five contributors and its verb CONTRIBUTE TO THE DEVELOPMENT, against a "
     "fixed endpoint. EK 4.3.A.1's life cycle effects presuppose continued development.",
 20: "EK 4.2.A.1 against EK 4.4.A.1, which states that political socialization in turn "
     "influences political ideology. The framework orders the two rather than equating them.",
 21: "Data item, CED skill 3.A. Every column's largest entry and the direction of the family "
     "row are recomputed below.",
 22: "Data item, CED skill 3.A: the largest decline across age groups. Every row's change from "
     "youngest to oldest is recomputed below.",
 23: "Data item: reading the second largest entry in a column as the largest. Both figures are "
     "recomputed below.",
 24: "Data item, CED skill 3.A. The direction of movement for each of the four practices is "
     "recomputed below.",
 25: "EK 4.2.A.2's bidirectional claim shown as data, with nonzero entries in both columns.",
 26: "Data item: a one-way reading of a two-column table. The inward total is recomputed.",
 27: "Data item, CED skill 3.A. The largest and smallest change shares are recomputed below.",
 28: "EK 4.2.A.1's four outputs located as the table's rows, in the framework's own order.",
 29: "Data item: reading a study of adults as evidence that development stops in childhood. "
     "The smallest change share is recomputed below, and EK 4.3.A.1's life cycle effects "
     "describe experiences at different life stages.",
 30: "EK 4.2.A.1's list of contributors read for what it does NOT say. The framework supplies "
     "no weighting among family, schools, peers, media and social environments, so it "
     "predicts nothing about which prevails where two conflict. Order of mention in a list "
     "is not a claim about strength.",
}
GROUNDING[29] = (
    "Data item: reading a study of adults as evidence that development stops before adulthood. "
    "The smallest change share is recomputed below. EK 4.3.A.1's life cycle effects describe "
    "experiences a person encounters during different life stages, which presupposes that "
    "development continues.")

UNDER30, MID, OVER60 = "Under 30 (%)", "Ages 30 to 59 (%)", "Age 60 and older (%)"
INFLUENCE = "Influence named as most important"
OUT, IN = "Countries adopting it from U.S. practice", "Instances of U.S. adoption from abroad"
PRACTICE = "Political practice"
CHANGED, UNCHANGED = "Respondents showing a change (%)", "Respondents showing no change (%)"
MEASURED = "What was measured"


def _col(t, header):
    j = t["headers"].index(header)
    return [gc.num(r[j]) for r in t["rows"]]


def _labels(t):
    return [r[0] for r in t["rows"]]


def q21(t):
    """Family leads every column and rises; every column totals 100."""
    cols = {h: _col(t, h) for h in (UNDER30, MID, OVER60)}
    for h, c in cols.items():
        assert sum(c) == 100, f"column {h!r} totals {sum(c):.0f}, not 100"
    names = _labels(t)
    fam = names.index("Family")
    for h, c in cols.items():
        assert c[fam] == max(c), f"family does not lead column {h!r}: {c}"
    trend = [cols[h][fam] for h in (UNDER30, MID, OVER60)]
    assert trend == sorted(trend) and len(set(trend)) == 3, f"the family row is {trend}"
    return (f"family leads all three columns at {', '.join(f'{x:.0f}' for x in trend)}, "
            "rising; every column totals 100")


def q22(t):
    """Peers fall further than any other row across the three age groups."""
    drops = {n: _col(t, UNDER30)[i] - _col(t, OVER60)[i] for i, n in enumerate(_labels(t))}
    biggest = max(drops, key=lambda k: drops[k])
    assert biggest == "Peers", f"the largest decline is on {biggest!r}, not peers"
    assert drops["Peers"] > drops["Schools"], \
        f"schools fall by {drops['Schools']:.0f}, at least as much as peers {drops['Peers']:.0f}"
    risers = [k for k, v in drops.items() if v < 0]
    assert set(risers) >= {"Family", "Media"}, f"family and media do not both rise: {risers}"
    return ("changes from youngest to oldest: "
            + ", ".join(f"{k.split(',')[0]} {-v:+.0f}" for k, v in drops.items()))


def q23(t):
    """In the youngest column family exceeds media."""
    young = dict(zip(_labels(t), _col(t, UNDER30)))
    assert young["Family"] == 38 and young["Media"] == 21, \
        f"the youngest column reads family {young['Family']:.0f}, media {young['Media']:.0f}"
    assert young["Family"] > young["Media"], "media leads family among the youngest"
    assert young["Media"] == sorted(young.values())[-2], \
        "media is not the second largest entry in the youngest column"
    return (f"youngest column: family {young['Family']:.0f} against media "
            f"{young['Media']:.0f}, which is the second largest entry")


def q24(t):
    """Two practices move outward only and two inward only."""
    out, inn = _col(t, OUT), _col(t, IN)
    outward = [n for n, o, i in zip(_labels(t), out, inn) if o > 0 and i <= 1]
    inward = [n for n, o, i in zip(_labels(t), out, inn) if o == 0 and i > 0]
    assert len(outward) == 2 and len(inward) == 2, \
        f"{len(outward)} outward and {len(inward)} inward, not two and two"
    assert len(t["rows"]) == 4, f"{len(t['rows'])} practices, not four"
    return (f"outward: {', '.join(n.split()[0] for n in outward)}; "
            f"inward: {', '.join(n.split()[0] for n in inward)}")


def q25(t):
    """Both columns carry nonzero entries, which is what makes the claim bidirectional."""
    out, inn = _col(t, OUT), _col(t, IN)
    assert sum(out) > 0 and sum(inn) > 0, f"a direction is empty: {sum(out)}, {sum(inn)}"
    return f"outward total {sum(out):.0f}, inward total {sum(inn):.0f} -- both nonzero"


def q26(t):
    """The inward column totals 8 across three of the four practices."""
    inn = _col(t, IN)
    assert sum(inn) == 8, f"the inward column totals {sum(inn):.0f}, not the 8 the key states"
    nonzero = sum(1 for x in inn if x > 0)
    assert nonzero == 3, f"{nonzero} practices show inward movement, not three"
    assert sum(_col(t, OUT)) > 0, "the outward column is empty, so the key's contrast fails"
    return (f"inward column {', '.join(f'{x:.0f}' for x in inn)} totalling {sum(inn):.0f} "
            f"across {nonzero} of {len(inn)} practices")


def q27(t):
    """Opinions change most, values least; behaviors are second."""
    ch = dict(zip(_labels(t), _col(t, CHANGED)))
    top = max(ch, key=lambda k: ch[k])
    low = min(ch, key=lambda k: ch[k])
    assert top.startswith("Political opinions"), f"the largest change is on {top!r}"
    assert low == "Political values", f"the smallest change is on {low!r}"
    ranked = sorted(ch, key=lambda k: -ch[k])
    assert ranked[1].startswith("Political behaviors"), \
        f"behaviors are not second: {ranked[1]!r}"
    for r in t["rows"]:
        assert gc.num(r[1]) + gc.num(r[2]) == 100, f"row {r[0]!r} does not total 100"
    return ("change shares " + ", ".join(f"{k.split()[1]} {v:.0f}" for k, v in ch.items())
            + f"; every row totals 100")


def q28(t):
    """The rows are EK 4.2.A.1's four outputs, in order."""
    names = [n.lower() for n in _labels(t)]
    for want, got in zip(("beliefs", "values", "opinions", "behaviors"), names):
        assert want in got, f"expected {want!r} in row {got!r}"
    assert len(names) == 4, f"{len(names)} rows, not four"
    return "rows are EK 4.2.A.1's four outputs in order: beliefs, values, opinions, behaviors"


def q29(t):
    """Every row shows change for a substantial share; the smallest is 19."""
    ch = _col(t, CHANGED)
    assert min(ch) == 19, f"the smallest change share is {min(ch):.0f}, not the 19 keyed"
    assert min(ch) > 0, "a category shows no change at all"
    assert not all(x > 50 for x in ch), \
        "every category exceeds half, which the key's fourth distractor needs to be false"
    return (f"change shares {', '.join(f'{x:.0f}' for x in ch)} -- smallest {min(ch):.0f}, "
            f"largest {max(ch):.0f}, none zero")


# --- module-specific content gates -------------------------------------------

_OUTPUTS = ("beliefs", "values", "opinions", "behaviors")
_AGENT_NAMES = ("family", "schools", "peers", "media", "social environments")


def _outputs(module):
    """EK 4.2.A.1's four outputs stay four, and BEHAVIORS survives."""
    bad = []
    for n in (1, 2):
        key = module.QUESTIONS[n - 1]["choices"][module.QUESTIONS[n - 1]["ans"]].lower()
        for o in _OUTPUTS:
            if o not in key:
                bad.append(f"q{n}: the key has dropped {o!r}, one of EK 4.2.A.1's four "
                           "outputs of political socialization")
    truncations = ("beliefs, values, and opinions only", "produces only attitudes",
                   "only what people think", "concerns only attitudes and not conduct")
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for t in truncations:
            if t in key:
                bad.append(f"q{i} key: truncates EK 4.2.A.1's outputs to attitudes ({t!r}); "
                           "the framework's list ends with BEHAVIORS")
    if bad:
        print(f"FAIL {module.__name__} outputs")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} outputs: EK 4.2.A.1's four outputs survive in the defining "
          "keys, BEHAVIORS included, and no key reduces the process to attitudes alone")


def _agents(module):
    """EK 4.2.A.1's five contributors stay five, and the parenthesis survives."""
    bad = []
    q7 = module.QUESTIONS[6]
    k7 = q7["choices"][q7["ans"]].lower()
    for a in _AGENT_NAMES:
        if a not in k7:
            bad.append(f"q7: the key has dropped {a!r}, one of EK 4.2.A.1's five contributors")
    q8 = module.QUESTIONS[7]
    k8 = q8["choices"][q8["ans"]].lower()
    if "civic" not in k8 or "religious" not in k8:
        bad.append("q8: the key no longer carries EK 4.2.A.1's parenthesis, 'including civic "
                   "and religious organizations'")
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for miscount in ("only four contributors", "names four contributors",
                         "three contributors", "family and schools only"):
            if miscount in key:
                bad.append(f"q{i} key: miscounts EK 4.2.A.1's contributors ({miscount!r}); "
                           "the framework names five, the fifth being social environments")
    if bad:
        print(f"FAIL {module.__name__} agents")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} agents: all five of EK 4.2.A.1's contributors survive, the "
          "civic and religious parenthesis with them, and no key miscounts them")


def _both_ways(module):
    """EK 4.2.A.2's globalization claim keeps both directions."""
    bad = []
    one_way = (
        "influenced other countries without being influenced",
        "been influenced by other countries without influencing",
        "has spread american values abroad without",
        "influence has run only outward",
        "influence has run only inward",
    )
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for phrase in one_way:
            if phrase in key:
                bad.append(f"q{i} key: states {phrase!r}. EK 4.2.A.2 says U.S. political "
                           "culture 'has BOTH influenced AND been influenced by the values of "
                           "other countries', and half a sentence is available in either "
                           "direction depending on the reader's priors")
    for n in (15, 25):
        key = module.QUESTIONS[n - 1]["choices"][module.QUESTIONS[n - 1]["ans"]].lower()
        if "influenced and been influenced" not in key:
            bad.append(f"q{n}: the key no longer carries both halves of EK 4.2.A.2's verb "
                       "phrase, INFLUENCED AND BEEN INFLUENCED")
    q14 = module.QUESTIONS[13]
    k14 = q14["choices"][q14["ans"]].lower()
    for part in ("democratic ideals", "principles", "core values"):
        if part not in k14:
            bad.append(f"q14: the key has dropped {part!r} from EK 4.2.A.2's definition of "
                       "U.S. political culture")
    if bad:
        print(f"FAIL {module.__name__} both ways")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} both ways: EK 4.2.A.2's globalization claim keeps both "
          "directions in every key that states it, and the definition of U.S. political "
          "culture keeps all three of its parts")


ua.shape(v4_2)
ua.check(v4_2, ANCHORS, GROUNDING)
ua.notation(v4_2)
_outputs(v4_2)
_agents(v4_2)
_both_ways(v4_2)
gc.check(v4_2, arith={21: q21, 22: q22, 23: q23, 24: q24, 25: q25, 26: q26,
                      27: q27, 28: q28, 29: q29})
