"""Structural gate for AP U.S. Government 5.7 Groups Influencing Policy Outcomes.

gov345_check plus the four usgov_anchor helpers, plus two content gates.

  _actors        EK 5.7.A.2's list CROSSES THE LINE between government and
                 society, and that is the thing to notice about it. Interest
                 groups, professional organizations and social movements are
                 outside government; THE MILITARY and BUREAUCRATIC AGENCIES are
                 inside it, and the framework calls all five COMPETING ACTORS in
                 one breath. So the topic is not "how outside groups pressure
                 government" -- it is how a set of actors, some of them parts of
                 the government itself, compete over policy. A module that
                 quietly dropped the two governmental actors would be answering
                 a different and easier question, so the gate pins all five and
                 refuses any key confining the list to actors outside
                 government.

                 It also pins the two qualifiers, AT KEY STAGES and TO VARYING
                 DEGREES, which say influence is uneven along two different
                 dimensions -- when it is exercised and how much of it there is.
                 Both are droppable and item 14 exists to keep them apart.

  _occasionally  EK 5.7.A.3 has one flat clause and one hedged one. Elections
                 and parties ARE RELATED TO major policy shifts; they only
                 OCCASIONALLY lead to realignments of voting constituencies.
                 Turning the hedge into a rule -- every consequential election
                 realigns the electorate -- is the error, and it is tempting
                 because the two halves sit in one sentence. The second table is
                 built with initiatives following all four elections and a
                 realignment following one, so item 30's correction rests on
                 arithmetic rather than on assertion.

The budget table gives bureaucratic agencies and the military their own columns
precisely so the governmental actors cannot be dropped in practice while
surviving in a definition, and it is built so the LEADING ACTOR CHANGES from
stage to stage, which is what AT KEY STAGES looks like as data.
"""
import gov345_check as gc
import usgov_anchor as ua
import v5_7

ANCHORS = {
 1: "Single-issue groups, ideological or social movements, and protest movements",
 2: "Affecting society and policymaking",
 3: "change how people think and behave as well as to change what government does",
 4: "organized around one question rather than a broad programme",
 5: "very specific interests correspond closely to EK 5.7.A.1's single-issue groups",
 6: "A protest movement, which the framework lists among groups forming to affect society",
 7: "Which of the three kinds of group is most effective",
 8: "Interest groups, professional organizations, social movements, the military, and",
 9: "It includes actors inside government, the military and bureaucratic agencies",
 10: "parts of the government compete over policy alongside outside groups",
 11: "The federal budget process",
 12: "At key stages and to varying degrees",
 13: "an actor may matter greatly at one point in the process and little at another",
 14: "not only in when they have it",
 15: "competing actors influencing policymaking",
 16: "Major policy shifts or initiatives",
 17: "Occasionally",
 18: "so evidence of a policy shift is not evidence of a realignment",
 19: "A change in which groups of voters support which party",
 20: "one as an occasional consequence of elections and the other as what defines a critical",
 21: "competition among distinct interests as a permanent feature of society",
 22: "Protest movements, which form with the goal of affecting society and policymaking",
 23: "with a professional organization and a bureaucratic agency both named on its list",
 24: "some inside government and some outside it",
 25: "so the leading actor changes across the process",
 26: "such as the federal budget process, at key stages and to varying degrees",
 27: "which is what the framework's phrase AT KEY STAGES describes",
 28: "while a realignment was observed after only one of the four",
 29: "occasionally leading to political realignments",
 30: "which is why the framework says elections lead to realignments only occasionally",
}

GROUNDING = {
 1: "EK 5.7.A.1's three kinds of group. The distractors list EK 5.3.A.1's linkage institutions "
    "and three of EK 5.7.A.2's competing actors, which is a different statement.",
 2: "EK 5.7.A.1's phrase 'form with the goal of affecting society and policymaking'. Both "
    "objects are the framework's own.",
 3: "EK 5.7.A.1's two objects read apart: a group on this list may aim at conduct and belief "
    "as well as at what government does.",
 4: "EK 5.7.A.1's single-issue groups set against its broader movements, the same scope "
    "contrast EK 5.6.A.1 draws between very specific and more general interests.",
 5: "EK 5.6.A.1 against EK 5.7.A.1: overlapping territory approached from different starting "
    "points.",
 6: "EK 5.7.A.1's protest movements applied, with the framework's stated goal covering both "
    "drawing attention and pressing for a change in law.",
 7: "EK 5.7.A.1 read for what it omits: three kinds of group, one goal, no comparison.",
 8: "EK 5.7.A.2's five competing actors. The distractors list EK 5.3.A.1's linkage "
    "institutions and EK 5.7.A.1's three kinds of group.",
 9: "EK 5.7.A.2's list read for what it spans. Three actors are outside government and two "
    "are inside it, and the framework calls all five competing actors in one sentence.",
 10: "EK 5.7.A.2's inclusion of bureaucratic agencies among actors that INFLUENCE "
     "policymaking, a role beyond implementation. EK 5.6.A.2's iron triangles describe one "
     "arrangement in which an agency works with a committee and an interest group.",
 11: "EK 5.7.A.2's own example: policymaking 'such as the federal budget process'. Naming a "
     "process with stages is what makes AT KEY STAGES meaningful.",
 12: "EK 5.7.A.2's two qualifiers, verbatim: 'at key stages and to varying degrees'.",
 13: "EK 5.7.A.2's AT KEY STAGES: influence concentrated at points in a process rather than "
     "spread across it.",
 14: "EK 5.7.A.2's TO VARYING DEGREES against AT KEY STAGES -- how much against when. The "
     "framework states that the degrees vary without saying which actor has most.",
 15: "EK 5.7.A.2 applied to three of its five actors pressing in different directions, which "
     "is the framework's word COMPETING in a scenario.",
 16: "EK 5.7.A.3's flat clause: elections and political parties 'are related to major policy "
     "shifts or initiatives.'",
 17: "EK 5.7.A.3's hedge, verbatim: OCCASIONALLY leading to political realignments.",
 18: "EK 5.7.A.3's two clauses read against each other. One is unhedged and one is hedged, so "
     "the second is rarer than the first by the framework's own wording.",
 19: "EK 5.7.A.3's realignments of voting CONSTITUENCIES, read with EK 5.4.A.3.i's definition "
     "of a critical election as one with a realignment of party support among voters.",
 20: "EK 5.4.A.3.i against EK 5.7.A.3: the same phenomenon in two statements with different "
     "jobs, one defining a term and one naming an occasional consequence.",
 21: "Federalist No. 10 (required document), quoted verbatim; the CED attaches it to 5.7.A. "
     "Madison identifies distinct and durable interests, which is the background condition for "
     "the competition EK 5.7.A.2 describes.",
 22: "'Letter from a Birmingham Jail' (required document), quoted verbatim; the CED attaches "
     "the Letter to 5.7.A. Its argument that change follows demand is the premise of organized "
     "protest, and EK 5.7.A.1 names protest movements.",
 23: "EK 5.7.A.2 applied to two of its five named actors, one outside government and one "
     "inside it.",
 24: "LO 5.7.A's phrase VARIOUS POLITICAL ACTORS against EK 5.7.A.2's list, which spans "
     "government and society.",
 25: "Data item, CED skill 1.E. Every column and the leading actor at each stage are "
     "recomputed below.",
 26: "EK 5.7.A.2 located in the table: rows are stages of the framework's own named example "
     "and columns are four of the five actors it lists.",
 27: "EK 5.7.A.2's AT KEY STAGES against a claim of domination. The change of leader across "
     "rows is recomputed below.",
 28: "Data item, CED skill 1.E. Both columns are recomputed below.",
 29: "EK 5.7.A.3's two clauses located as the table's two data columns, with their different "
     "frequencies.",
 30: "EK 5.7.A.3's hedge against the inference from a policy shift to a realignment. The counts "
     "are recomputed below.",
}

STAGE = "Stage of the budget process"
ACTOR_COLS = ["Interest groups (%)", "Professional organizations (%)",
              "Bureaucratic agencies (%)", "The military (%)"]
INITIATIVES = "Major policy initiatives enacted in the next two years"
REALIGN = "Realignment of voting constituencies observed"


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def _num(t, header):
    return [gc.num(c) for c in _col(t, header)]


def _leaders(t):
    out = []
    for r in t["rows"]:
        vals = {h: gc.num(r[t["headers"].index(h)]) for h in ACTOR_COLS}
        out.append(max(vals, key=lambda k: vals[k]))
    return out


def q25(t):
    """Agencies lead the first two stages, interest groups the last two."""
    for r in t["rows"]:
        assert sum(gc.num(c) for c in r[1:]) == 100, f"row {r[0]!r} does not total 100"
    leaders = _leaders(t)
    assert leaders[0] == leaders[1] == "Bureaucratic agencies (%)", \
        f"agencies do not lead the first two stages: {leaders}"
    assert leaders[2] == leaders[3] == "Interest groups (%)", \
        f"interest groups do not lead the last two stages: {leaders}"
    mil = _num(t, "The military (%)")
    assert "The military (%)" not in leaders, "the military leads a stage, which the key denies"
    return (f"leaders by stage: {', '.join(l.split(' (')[0] for l in leaders)}; military peaks "
            f"at {max(mil):.0f} and leads nowhere")


def q26(t):
    """Rows are budget stages; columns are four of EK 5.7.A.2's five actors."""
    assert len(t["rows"]) == 4, f"{len(t['rows'])} stages, not four"
    for h in ACTOR_COLS:
        assert h in t["headers"], f"missing actor column {h!r}"
    assert "Bureaucratic agencies (%)" in t["headers"] and "The military (%)" in t["headers"], \
        "the two governmental actors are not both given their own columns"
    return "four budget stages against four named actors, including both governmental ones"


def q27(t):
    """The leader changes across the process, so no actor dominates."""
    leaders = _leaders(t)
    assert len(set(leaders)) > 1, f"one actor leads every stage: {leaders}"
    return f"the leading actor changes across the process: {', '.join(set(leaders))}"


def q28(t):
    """Initiatives after every election; realignment after exactly one."""
    init = _num(t, INITIATIVES)
    real = [x.strip().lower() == "yes" for x in _col(t, REALIGN)]
    assert all(x > 0 for x in init), f"an election produced no initiatives: {init}"
    assert sum(real) == 1, f"{sum(real)} realignments, not one"
    top = init.index(max(init))
    assert real[top], "the realignment did not follow the election with the most initiatives"
    assert init.index(min(init)) != real.index(True), \
        "the realignment followed the election with the fewest initiatives, which the key denies"
    return (f"initiatives {', '.join(f'{x:.0f}' for x in init)}, all above zero; "
            f"{sum(real)} realignment of {len(real)} elections")


def q29(t):
    """The two data columns are EK 5.7.A.3's two clauses."""
    heads = [h.lower() for h in t["headers"]]
    assert any("policy initiatives" in h for h in heads), f"no initiatives column: {heads}"
    assert any("realignment" in h for h in heads), f"no realignment column: {heads}"
    return "an initiatives column and a realignment column -- EK 5.7.A.3's two clauses"


def q30(t):
    """Three elections produced initiatives without a realignment."""
    init = _num(t, INITIATIVES)
    real = [x.strip().lower() == "yes" for x in _col(t, REALIGN)]
    without = sum(1 for i, r in zip(init, real) if i > 0 and not r)
    assert without >= 3, f"only {without} elections produced initiatives without a realignment"
    return (f"{without} of {len(init)} elections produced initiatives with no realignment -- "
            "the first does not imply the second")


# --- module-specific content gates -------------------------------------------

_FIVE_ACTORS = ("interest groups", "professional organizations", "social movements",
                "the military", "bureaucratic agencies")
_OUTSIDE_ONLY = (
    "actors outside government", "only groups outside government",
    "all of them are private organizations", "none of them is part of the government",
    "outside groups pressure government",
)


def _actors(module):
    """EK 5.7.A.2's five actors stay five, governmental ones included."""
    bad = []
    q8 = module.QUESTIONS[7]
    k8 = q8["choices"][q8["ans"]].lower()
    for a in _FIVE_ACTORS:
        if a not in k8:
            bad.append(f"q8: the key has dropped {a!r}, one of EK 5.7.A.2's five competing "
                       "actors")
    q9 = module.QUESTIONS[8]
    k9 = q9["choices"][q9["ans"]].lower()
    if "inside government" not in k9:
        bad.append("q9: the key no longer records that EK 5.7.A.2's list includes actors "
                   "INSIDE government -- the military and bureaucratic agencies -- which is "
                   "what makes this topic about competition rather than outside pressure")
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        stem = item["q"].lower()
        refusing = "notable" in stem or "not state" in stem
        for o in _OUTSIDE_ONLY:
            if o in key and not refusing:
                bad.append(f"q{i} key: confines EK 5.7.A.2's list to {o!r}; the framework names "
                           "the military and bureaucratic agencies among the competing actors")
    q12 = module.QUESTIONS[11]
    k12 = q12["choices"][q12["ans"]].lower()
    if "key stages" not in k12 or "varying degrees" not in k12:
        bad.append("q12: the key no longer carries both of EK 5.7.A.2's qualifiers")
    q13 = module.QUESTIONS[12]
    if "one point in the process" not in q13["choices"][q13["ans"]].lower():
        bad.append("q13: the key no longer explains AT KEY STAGES as influence concentrated in "
                   "the process rather than spread across it")
    q14 = module.QUESTIONS[13]
    if "not only in when" not in q14["choices"][q14["ans"]].lower():
        bad.append("q14: the key no longer separates TO VARYING DEGREES (how much) from AT KEY "
                   "STAGES (when), which is the whole point of the item")
    if bad:
        print(f"FAIL {module.__name__} actors")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} actors: all five of EK 5.7.A.2's competing actors survive "
          "including the two inside government, both qualifiers stay, and no key reduces the "
          "topic to outside pressure on government")


_REALIGN_RULE = (
    "every election produces a realignment",
    "always leading to political realignments",
    "a realignment was observed after every election",
    "an election producing major policy initiatives has thereby produced a realignment",
    "realignments follow every major policy shift",
)


def _occasionally(module):
    """EK 5.7.A.3's hedge stays a hedge."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        stem = item["q"].lower()
        refusing = "correction" in stem or "not state" in stem
        for r in _REALIGN_RULE:
            if r in key and not refusing:
                bad.append(f"q{i} key: states {r!r}. EK 5.7.A.3 says elections and parties are "
                           "related to major policy shifts and only OCCASIONALLY lead to "
                           "realignments -- one clause flat, one hedged")
    q17 = module.QUESTIONS[16]
    if "occasionally" not in q17["choices"][q17["ans"]].lower():
        bad.append("q17: the key no longer carries EK 5.7.A.3's own word OCCASIONALLY")
    q18 = module.QUESTIONS[17]
    if "not evidence of a realignment" not in q18["choices"][q18["ans"]].lower():
        bad.append("q18: the key no longer records that a policy shift is not evidence of a "
                   "realignment, which is what the difference between the two clauses means")
    if bad:
        print(f"FAIL {module.__name__} occasionally")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} occasionally: EK 5.7.A.3's hedge survives, and no key turns "
          "an occasional realignment into a rule that follows from a policy shift")


ua.shape(v5_7)
ua.check(v5_7, ANCHORS, GROUNDING)
ua.notation(v5_7)
_actors(v5_7)
_occasionally(v5_7)
gc.check(v5_7, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
