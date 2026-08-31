"""Structural gate for AP U.S. Government 5.6 Interest Groups Influencing
Policymaking.

gov345_check plus the four usgov_anchor helpers, plus three content gates.

  _across     EK 5.6.A.2's PREPOSITION is the content. Interest groups work
              WITHIN party coalitions, and iron triangles and issue networks
              help them exert influence ACROSS political party coalitions. The
              first clause already covers the within case, so ACROSS is the only
              thing the second half adds, and it is why the framework names
              these arrangements separately from ordinary coalition politics. A
              paraphrase putting iron triangles inside a party has dropped the
              reason the statement exists. The gate pins the preposition.

  _resources  EK 5.6.B.1 has a structure a summary flattens. Items i and ii name
              things a group HAS -- large memberships, the ability to mobilize
              them, large financial reserves, and more direct and more frequent
              access. Item iii names a PROBLEM groups face, free riding, and the
              SELECTIVE BENEFITS they use against it. Reading the third as a
              third kind of resource loses that structure, so the gate keeps
              both definitions intact and refuses calling free riding an
              advantage.

              The statement's own noun is INEQUALITY: it is the DIFFERENCES
              among groups, not resources in general, that the framework says
              affect influence, which is why LO 5.6.B asks about variation.

  _visual     Skill 3.F is unusually specific -- the limitations of the VISUAL
              REPRESENTATION of the data, not of the data. Those are different
              objects, and the wrong one is easy to answer: sample size, wording
              and causation are all real limitations that belong to skill 3.E.
              So the gate requires the chart items to name a property of the
              DRAWING (an axis, what a chart plots, what a slice aggregates) and
              refuses a key that answers with a property of the data instead.
              Item 22 makes the distinction itself the question.

              Every described chart is labelled hypothetical and attributed to
              no one, for the reason set out in the 4.8 header: this bank is
              text, a described chart is an honest stimulus, and an invented one
              credited to a real source would be a fabrication nothing
              downstream could catch.
"""
import re

import gov345_check as gc
import usgov_anchor as ua
import v5_6

ANCHORS = {
 1: "Very specific interests or more general ones",
 2: "Educating voters and office holders, conducting lobbying, drafting legislation",
 3: "Legislators and government agencies",
 4: "friend of the court to provide additional information for justices to consider",
 5: "That the filer is not a party to the case",
 6: "Drafting legislation",
 7: "Mobilizing membership to apply pressure on legislators",
 8: "Filing an amicus curiae brief",
 9: "Exert influence across political party coalitions",
 10: "arrangements that reach past party lines",
 11: "iron triangles helping interest groups exert influence across political party",
 12: "names the stable arrangements through which those dealings can cross party lines",
 13: "The inequality of interest group resources",
 14: "Large memberships, the ability to mobilize those members, and access to large financial",
 15: "a large membership that does not act supplies less influence than a smaller one that",
 16: "More direct and more frequent access to important people in the policy process",
 17: "benefits from the work of an interest group without providing financial support",
 18: "available only to members, offered to encourage more people to join",
 19: "while the third describes a problem groups face and a response to it",
 20: "the chart gives the viewer no way to see how many people each bar represents",
 21: "since the bars no longer show quantities in proportion",
 22: "hidden inside a single undifferentiated slice",
 23: "A limitation of the data rather than of its visual representation",
 24: "so that differences in rates between groups cannot be seen",
 25: "but the largest number of members acting",
 26: "large memberships, ability to mobilize members, and access to large financial reserves",
 27: "with no indication that one group has more than two thousand times another's membership",
 28: "the group offering members-only goods and services has far more dues-paying members",
 29: "free riders and the selective benefits groups use to encourage more people to join",
 30: "and with it the free riding that the comparison between the two columns reveals",
}

GROUNDING = {
 1: "EK 5.6.A.1's opening: interest groups 'may represent very specific or more general "
    "interests.' Breadth of interest is one of the variations LO 5.6.B asks about.",
 2: "EK 5.6.A.1's four activities. The distractors list EK 5.3.B.1's party functions and EK "
    "5.2.A.2's state election decisions.",
 3: "EK 5.6.A.1's phrase 'apply pressure on and work with legislators and government "
    "agencies'. Naming agencies is what connects this to EK 5.6.A.2's iron triangles.",
 4: "EK 5.6.A.1's parenthesis, verbatim: 'a written document submitted as a friend of the "
    "court to provide additional information for justices to consider when reviewing a case.'",
 5: "EK 5.6.A.1's phrase FRIEND OF THE COURT and its word ADDITIONAL, which together "
    "presuppose the filer is not the one whose case it is.",
 6: "EK 5.6.A.1's activity of drafting legislation, which the framework lists separately from "
    "lobbying.",
 7: "EK 5.6.A.1's mobilizing membership, distinguished from lobbying by who does the "
    "contacting.",
 8: "EK 5.6.A.1's amicus curiae brief as the one route on its list that reaches a court; the "
    "other four are aimed at voters, legislators and agencies.",
 9: "EK 5.6.A.2, verbatim: iron triangles and issue networks 'help interest groups exert "
    "influence ACROSS political party coalitions.'",
 10: "EK 5.6.A.2's contrast between working WITHIN party coalitions and exerting influence "
     "ACROSS them. The framework says groups do both, IN ADDITION TO one another.",
 11: "EK 5.6.A.2 applied. The three participants and the persistence across a change in party "
     "control are the ACROSS in the framework's sentence.",
 12: "EK 5.6.A.1's list of bodies against EK 5.6.A.2's structures: one gives the activity, the "
     "other the arrangement it can settle into.",
 13: "EK 5.6.B.1's own noun, INEQUALITY. It is the differences among groups that the framework "
     "says affect influence, which is why LO 5.6.B asks about variation.",
 14: "EK 5.6.B.1.i's three resources, with AARP as the framework's own named example -- which "
     "makes that organization course content here rather than an illustration.",
 15: "EK 5.6.B.1.i listing membership and the ability to mobilize as two things, and EK "
     "5.6.A.1 making mobilization an activity rather than a possession.",
 16: "EK 5.6.B.1.ii, verbatim: access that is both MORE DIRECT and MORE FREQUENT. An advantage "
     "independent of size, which is why it is listed separately.",
 17: "EK 5.6.B.1.iii's definition of a free rider, verbatim. Both halves matter: the person "
     "benefits, and the person does not pay.",
 18: "EK 5.6.B.1.iii's selective benefits, verbatim. The word ONLY is what makes them work: a "
     "benefit the public receives anyway gives no one a reason to pay.",
 19: "EK 5.6.B.1's structure. Items i and ii name what a group HAS; item iii names what a "
     "group SUFFERS and the response to it.",
 20: "CED skill 3.F on a described hypothetical chart. A chart of rates omits the denominator "
     "by construction, which is a property of the drawing rather than of the data.",
 21: "CED skill 3.F. A bar's length reads as a quantity, so a baseline above zero makes ratios "
     "between bars appear larger than they are.",
 22: "CED skill 3.F. An aggregated residual category conceals whatever structure lies inside "
     "it; the stem supplies the policy area, so that is not what is missing.",
 23: "CED skill 3.F against skill 3.E. Sample size is a property of the data, and the two are "
     "separate skills in the CED's own list.",
 24: "CED skill 3.F. A chart of totals hides rates by construction; the distractors describe "
     "how data was collected or worded.",
 25: "Data item, CED skill 3.F. Every rate and every mobilized count is recomputed below.",
 26: "EK 5.6.B.1.i's three resources located as the table's three data columns, in order.",
 27: "CED skill 3.F applied to this table: a chart of the rate column alone omits the "
     "membership figures. The ratio between the largest and smallest is recomputed below.",
 28: "Data item, CED skill 3.F. Both matched pairs are recomputed below.",
 29: "EK 5.6.B.1.iii located in the gap between beneficiaries and dues payers, with the fourth "
     "column recording the framework's own response to it.",
 30: "CED skill 3.F: free riding is visible only as a gap between two columns, so a chart of "
     "one of them cannot show it however accurately it is drawn.",
}

MEMBERS, ACTED, RESERVES = ("Members (thousands)", "Members who acted when asked (%)",
                            "Financial reserves (millions of dollars)")
BENEFIT, DUES, SELECTIVE = ("People who benefit from its work (thousands)",
                            "Dues-paying members (thousands)",
                            "Offers members-only goods and services")


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def _num(t, header):
    return [gc.num(c) for c in _col(t, header)]


def q25(t):
    """Largest membership has the lowest rate and still mobilizes the most people."""
    mem, act = _num(t, MEMBERS), _num(t, ACTED)
    names = _col(t, "Interest group")
    big = mem.index(max(mem))
    small = mem.index(min(mem))
    assert act[big] == min(act), f"the largest group's rate {act[big]:.0f} is not the lowest"
    assert act[small] == max(act), f"the smallest group's rate {act[small]:.0f} is not the highest"
    mobilized = [m * a / 100 for m, a in zip(mem, act)]
    assert mobilized[big] == max(mobilized), "the largest group does not mobilize the most people"
    return (f"{names[big]} {mem[big]:.0f} thousand members at {act[big]:.0f} percent mobilizes "
            f"{mobilized[big]:.0f} thousand; {names[small]} {mem[small]:.0f} at "
            f"{act[small]:.0f} percent mobilizes {mobilized[small]:.0f}")


def q26(t):
    """The three data columns are EK 5.6.B.1.i's three resources."""
    heads = [h.lower() for h in t["headers"]]
    assert "members (thousands)" in heads, f"no membership column: {heads}"
    assert any("acted" in h for h in heads), f"no mobilization column: {heads}"
    assert any("reserves" in h for h in heads), f"no financial reserves column: {heads}"
    return "membership, mobilization and financial reserves -- EK 5.6.B.1.i's three resources"


def q27(t):
    """The membership range is enormous, which is what a rate-only chart would hide."""
    mem, act = _num(t, MEMBERS), _num(t, ACTED)
    ratio = max(mem) / min(mem)
    assert ratio > 2000, f"the largest membership is only {ratio:.0f} times the smallest"
    top_rate = act.index(max(act))
    assert mem[top_rate] == min(mem), \
        "the highest rate does not belong to the smallest group, so the chart would not mislead"
    return (f"largest membership {max(mem):.0f} thousand against smallest {min(mem):.0f}, a "
            f"ratio of {ratio:.0f}; the highest action rate belongs to the smallest group")


def _pairs(t):
    ben, dues = _num(t, BENEFIT), _num(t, DUES)
    sel = [s.strip().lower() == "yes" for s in _col(t, SELECTIVE)]
    out = {}
    for b, d, s in zip(ben, dues, sel):
        out.setdefault(b, {})[s] = d
    return out


def q28(t):
    """Within each matched pair, the selective-benefit group has more dues payers."""
    pairs = _pairs(t)
    assert len(pairs) == 2, f"{len(pairs)} beneficiary levels, not two matched pairs"
    for b, d in pairs.items():
        assert set(d) == {True, False}, f"beneficiary level {b:.0f} is not a matched pair"
        assert d[True] > d[False], \
            f"at {b:.0f} thousand beneficiaries, selective {d[True]:.0f} does not exceed "\
            f"{d[False]:.0f}"
    ben, dues = _num(t, BENEFIT), _num(t, DUES)
    assert all(b > d for b, d in zip(ben, dues)), "a row has more dues payers than beneficiaries"
    return "; ".join(f"{b:.0f} thousand beneficiaries: {d[False]:.0f} without selective "
                     f"benefits against {d[True]:.0f} with" for b, d in pairs.items())


def q29(t):
    """Both the free-rider gap and the selective-benefit response are present."""
    ben, dues = _num(t, BENEFIT), _num(t, DUES)
    gaps = [b - d for b, d in zip(ben, dues)]
    assert all(g > 0 for g in gaps), f"a row shows no free-rider gap: {gaps}"
    sel = [s.strip().lower() for s in _col(t, SELECTIVE)]
    assert set(sel) == {"yes", "no"}, f"the selective benefits column is {sel}"
    return (f"free-rider gaps {', '.join(f'{g:.0f}' for g in gaps)} thousand, and the "
            "selective benefits column takes both values")


def q30(t):
    """Free riding is a gap between two columns, so one column cannot show it."""
    heads = [h.lower() for h in t["headers"]]
    assert any("benefit from its work" in h for h in heads), f"no beneficiary column: {heads}"
    assert any("dues-paying" in h for h in heads), f"no dues column: {heads}"
    ben, dues = _num(t, BENEFIT), _num(t, DUES)
    assert ben != dues, "the two columns are identical, so there would be no gap to hide"
    return "two columns whose difference is the free riding; either alone conceals it"


# --- module-specific content gates -------------------------------------------

def _across(module):
    """EK 5.6.A.2's iron triangles reach ACROSS party coalitions."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        at = key.find("iron triangle")
        if at < 0:
            at = key.find("issue network")
        if at < 0:
            continue
        seg = key[max(0, at - 80):at + 160]
        for wrong in ("within a single political party", "inside a party",
                      "within the party organization", "part of the party organization"):
            if wrong in seg:
                bad.append(f"q{i} key: places iron triangles or issue networks {wrong!r}; EK "
                           "5.6.A.2 says they help interest groups exert influence ACROSS "
                           "political party coalitions")
    q9 = module.QUESTIONS[8]
    if "across political party coalitions" not in q9["choices"][q9["ans"]].lower():
        bad.append("q9: the key no longer carries EK 5.6.A.2's preposition, ACROSS political "
                   "party coalitions, which is the only thing that half of the sentence adds")
    q10 = module.QUESTIONS[9]
    if "past party lines" not in q10["choices"][q10["ans"]].lower():
        bad.append("q10: the key no longer records why the contrast between WITHIN and ACROSS "
                   "matters")
    if bad:
        print(f"FAIL {module.__name__} across")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} across: EK 5.6.A.2's iron triangles and issue networks keep "
          "their reach ACROSS party coalitions in every key that describes them")


def _resources(module):
    """EK 5.6.B.1's structure survives: two advantages, one problem with a response."""
    bad = []
    q13 = module.QUESTIONS[12]
    if "inequality" not in q13["choices"][q13["ans"]].lower():
        bad.append("q13: the key no longer carries EK 5.6.B.1's own noun, INEQUALITY -- it is "
                   "the differences among groups the framework says affect influence")
    q14 = module.QUESTIONS[13]
    k14 = q14["choices"][q14["ans"]].lower()
    for r in ("membership", "mobilize", "financial reserves"):
        if r not in k14:
            bad.append(f"q14: the key has dropped {r!r}, one of EK 5.6.B.1.i's three resources")
    q17 = module.QUESTIONS[16]
    k17 = q17["choices"][q17["ans"]].lower()
    if "benefits from the work" not in k17 or "without providing financial support" not in k17:
        bad.append("q17: the key no longer carries both halves of EK 5.6.B.1.iii's free rider "
                   "definition -- benefiting, and not paying")
    q18 = module.QUESTIONS[17]
    k18 = q18["choices"][q18["ans"]].lower()
    if "only to members" not in k18:
        bad.append("q18: the key no longer carries the word ONLY in EK 5.6.B.1.iii's selective "
                   "benefits, which is what makes them work against free riding")
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for wrong in ("free riders are a resource", "free riding is an advantage",
                      "a third kind of resource"):
            if wrong in key:
                bad.append(f"q{i} key: treats free riding as an advantage ({wrong!r}); EK "
                           "5.6.B.1.iii names a problem groups face and the selective benefits "
                           "they use against it")
    if bad:
        print(f"FAIL {module.__name__} resources")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} resources: EK 5.6.B.1's INEQUALITY survives, its three "
          "resources and both definitions stay intact, and no key treats free riding as an "
          "advantage")


# Properties of a DRAWING, against properties of the DATA. Skill 3.F asks for
# the first; skill 3.E asks for the second, and answering the wrong one is the
# easy mistake, since sample size and wording are real limitations.
# A key answers skill 3.F either by naming a feature of the drawing (an axis, a
# bar, a slice, what the chart plots) or by naming what the drawing HIDES --
# item 30's key does the latter, saying the chart "would hide the beneficiary
# population entirely", and a feature-only list reported it. Concealment is the
# whole point of the skill, so the verbs belong in the vocabulary.
_DRAWING = ("axis", "bars", "bar", "slice", "chart", "plots", "plotting", "drawn",
            "visual representation", "proportion",
            "hide", "hides", "conceal", "conceals", "cannot show", "would not show")
_DATA_ONLY = ("sample", "survey reached", "question wording", "worded", "single year",
              "causation", "response rate")


def _visual(module):
    """Chart items must answer with a property of the drawing, not of the data."""
    bad = []
    chart_items = []
    for i, item in enumerate(module.QUESTIONS, 1):
        stem = item["q"]
        low = stem.lower()
        if "chart" not in low:
            continue
        chart_items.append(i)
        # A stem PRESENTS a chart when it describes one: "chart shows",
        # "chart plots". Item 23 mentions a chart while asking which skill a
        # student answered, and presents no image. The first draft of this
        # exemption keyed on the phrase "visual representation" appearing
        # anywhere in the stem, which is far too wide -- a negative control that
        # stripped the hypothetical label from a real chart item stayed SILENT,
        # because that item's own question ends "...of this visual
        # representation?". Presenting is a verb, so test for the verb.
        presenting = any(p in low for p in ("chart shows", "chart plots",
                                            "chart of this data plots"))
        if presenting and "hypothetical" not in low:
            bad.append(f"q{i}: describes a chart without labelling it hypothetical. This bank "
                       "is text, so a described chart is honest only if it is not presented "
                       "as a real one")
        if presenting and re.search(r"^\s*[—-]\s*\S", stem, re.MULTILINE):
            bad.append(f"q{i}: attributes a chart to a source. An invented chart credited to a "
                       "real publication is a fabrication nothing downstream could catch")
        key = item["choices"][item["ans"]].lower()
        # The key must name something about the drawing, unless the item is the
        # one whose whole point is that the answer given was about the data.
        if "rather than of" in key or "limitation of the data" in key:
            continue
        if not any(d in key for d in _DRAWING):
            bad.append(f"q{i} key: names no property of the drawing. Skill 3.F asks for the "
                       "limitations of the VISUAL REPRESENTATION, so the answer has to be "
                       "about how the data was drawn")
        if any(d in key for d in _DATA_ONLY):
            bad.append(f"q{i} key: answers with a property of the DATA, which is skill 3.E. "
                       "Skill 3.F asks what the drawing conceals")
    if len(chart_items) < 4:
        bad.append(f"only {len(chart_items)} items describe a chart; the suggested skill for "
                   "this topic is 3.F, which is about visual representations")
    if bad:
        print(f"FAIL {module.__name__} visual")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} visual: {len(chart_items)} chart items, every one labelled "
          "hypothetical and unattributed, and every key names a property of the drawing rather "
          "than of the data")


ua.shape(v5_6)
ua.check(v5_6, ANCHORS, GROUNDING)
ua.notation(v5_6)
_across(v5_6)
_resources(v5_6)
_visual(v5_6)
gc.check(v5_6, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
