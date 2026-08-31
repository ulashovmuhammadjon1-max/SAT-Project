"""Structural gate for AP U.S. Government 5.3 Political Parties.

gov345_check plus the four usgov_anchor helpers, plus two content gates.

  _direction  EK 5.3.A.1's linkage institutions are "channels that allow
              INDIVIDUALS TO COMMUNICATE THEIR PREFERENCES TO POLICYMAKERS". The
              arrow is the definition. A paraphrase in which these institutions
              inform citizens, reach the public, or carry government's decisions
              outward has reversed it and is describing something else.

              MEDIA is where the reversal is most tempting, because carrying
              information outward is the obvious thing media does and EK 5.3.A.1
              lists it for the opposite reason. Items 2, 3 and 6 turn on the
              direction and the gate refuses any key that reverses it -- while
              allowing items 3 and 27, whose keys correctly NAME the reversal in
              order to refuse it.

  _functions  EK 5.3.B.1 names FIVE functions and the fifth is the one that
              disappears: THE COMMITTEE AND PARTY LEADERSHIP SYSTEMS IN
              LEGISLATURES. Losing it is not a small omission. LO 5.3.B says
              parties act ON THE ELECTORATE AND GOVERNMENT; functions i to iv
              are all directed at voters and candidates, so function v is the
              ENTIRE government half of the objective. A module that stopped at
              four would answer half the question while looking complete.

              The gate pins all five in the item that lists them, pins the fifth
              as the government-facing one, and refuses any key asserting that
              parties act only on the electorate. The activities table is built
              four rows against one to show the split, and q30 asserts the
              government row is present and nonzero.
"""
import gov345_check as gc
import usgov_anchor as ua
import v5_3

ANCHORS = {
 1: "Channels that allow individuals to communicate their preferences to policymakers",
 2: "From individuals to policymakers",
 3: "a linkage institution carries individuals' preferences to policymakers",
 4: "Political parties, interest groups, elections, and media",
 5: "individuals communicate a preference to those who will make policy",
 6: "Because it serves as a channel through which the preferences of individuals reach",
 7: "It introduces the category that the topics on parties, interest groups, and media",
 8: "It is a channel carrying individuals' preferences to policymakers",
 9: "The electorate and government",
 10: "and the committee and party leadership systems in legislatures",
 11: "The committee and party leadership systems in legislatures",
 12: "Fundraising and media strategy",
 13: "Candidate recruitment",
 14: "Mobilization and education of voters",
 15: "Party platforms, which EK 4.7.A.1 describes as generally aligning more closely",
 16: "The committee and party leadership systems in legislatures",
 17: "and with it the whole government half of LO 5.3.B",
 18: "the means by which the party carries individuals' preferences toward policymakers",
 19: "Parties recruit and run candidates for office under their own label",
 20: "Which of the four linkage institutions is most effective",
 21: "and the second asks how party functions produce effects",
 22: "A party operating as a linkage institution, and the party platform function",
 23: "and also something that has an effect on the electorate or on government",
 24: "and they act on both the electorate and government through five named functions",
 25: "interest groups are the only channel named most effective by a larger share",
 26: "list of four linkage institutions",
 27: "does not determine whether it meets the framework's definition",
 28: "and the electorate-directed activities together take most of the staff time",
 29: "five functions of political parties",
 30: "the government half of what LO 5.3.B asks about",
}
# Items 11 and 16 carry the same anchor string because both key on EK 5.3.B.1.v
# by name; usgov_anchor checks an anchor against its own question's five choices
# rather than across the module, so identical anchors on different items are
# fine, and here the framework's own wording is what each item is testing.

GROUNDING = {
 1: "EK 5.3.A.1, verbatim: linkage institutions are 'channels that allow individuals to "
    "communicate their preferences to policymakers.' The direction is part of the definition.",
 2: "EK 5.3.A.1's arrow, read on its own. An institution carrying information outward from "
    "government to citizens is doing something the definition does not describe.",
 3: "EK 5.3.A.1 against the reversed paraphrase. Informing the public is something several of "
    "these institutions also do; it is not what makes them linkage institutions.",
 4: "EK 5.3.A.1's four items: political parties, interest groups, elections, media. The "
    "distractor listing families and schools is EK 4.2.A.1's contributors to socialization.",
 5: "EK 5.3.A.1's definition applied to elections, the most direct form of the communication "
    "it describes. State administration and constitutional requirement are true and are not "
    "what places elections on this list.",
 6: "EK 5.3.A.1's definition applied to media, which is listed for the same reason as the "
    "other three. The outward flow of information is the more obvious thing media does, which "
    "is why the item is worth asking.",
 7: "EK 5.3.A.1's list against the structure of Unit 5, which takes up parties, third parties, "
    "interest groups, elections and the media in later topics.",
 8: "EK 5.3.A.1's definition applied, CED skill 1.B. That the organization is private is what "
    "makes it a linkage institution rather than part of what it communicates with.",
 9: "LO 5.3.B and EK 5.3.B.1, both of which name the electorate AND government.",
 10: "EK 5.3.B.1's five functions in order. The four-item distractor is the standard omission "
     "and drops the government half of the objective.",
 11: "EK 5.3.B.1.v, the only listed function operating inside a legislature rather than among "
     "voters. It is what makes LO 5.3.B's phrase AND GOVERNMENT accurate.",
 12: "EK 5.3.B.1.iv, verbatim: 'campaign management, including fundraising and media "
     "strategy.'",
 13: "EK 5.3.B.1.iii applied. Finding people to run is distinct from campaign management, "
     "which supports a candidacy once it exists.",
 14: "EK 5.3.B.1.i applied, with both halves of the framework's phrase present and neither "
     "activity attached to a particular candidate.",
 15: "EK 5.3.B.1.ii against EK 4.7.A.1, which says each major party's platforms generally "
     "align more closely with a set of ideological positions. One document, two statements.",
 16: "EK 5.3.B.1.v applied to a legislative agenda coordinated through party leadership, with "
     "no voter or candidacy in the scenario.",
 17: "EK 5.3.B.1.v read against LO 5.3.B. The other four functions are all electorate-facing, "
     "so dropping the fifth answers half the objective while appearing complete.",
 18: "EK 5.3.A.1 and EK 5.3.B.1 read together: the functions are the activities through which "
     "the channel operates.",
 19: "EK 5.3.A.1 assigns both parties and interest groups the same channel role, so the "
     "difference comes from EK 5.3.B.1.iii and iv against EK 5.6.A.1's account of what "
     "interest groups do, which does not include running candidates under a label.",
 20: "EK 5.3.A.1 read for what it omits: a definition and a list of four, with no ranking.",
 21: "LO 5.3.A's verb DESCRIBE against LO 5.3.B's EXPLAIN, matched to the content behind each.",
 22: "EK 5.3.A.1's channel and EK 5.3.B.1.ii's platform function, describing one episode at "
     "two levels.",
 23: "EK 5.3.B.1's own phrase, 'the functions AND IMPACT of political parties on the electorate "
     "and government'. Each item is both an activity and a way the party bears on someone.",
 24: "EK 5.3.A.1 and EK 5.3.B.1 together. Each distractor drops one of the two statements or "
     "overstates it.",
 25: "Data item, CED skill 1.B. Both columns are recomputed below.",
 26: "EK 5.3.A.1's four institutions located as the table's rows, with the stem's wording "
     "matching the framework's definition.",
 27: "EK 5.3.A.1's definition against a ranking. Membership follows from being a channel, not "
     "from a rating; the figures are recomputed below.",
 28: "Data item, CED skill 1.B. The split and the staff time totals are recomputed below.",
 29: "EK 5.3.B.1's five functions located as the table's five rows, in order.",
 30: "EK 5.3.B.1.v present as a real row with a nonzero share, against a claim that parties act "
     "only on voters. Recomputed below.",
}

USED, EFFECTIVE = "Used it in the past year (%)", "Named it the most effective (%)"
CHANNEL = "Channel"
DIRECTED, TIME = "Directed mainly at", "Share of staff time (%)"
ACTIVITY = "Party activity"


def _col(t, header):
    j = t["headers"].index(header)
    return [r[j] for r in t["rows"]]


def _num(t, header):
    return [gc.num(c) for c in _col(t, header)]


def q25(t):
    """Elections lead both columns; interest groups alone gain from used to effective."""
    names, used, eff = _col(t, CHANNEL), _num(t, USED), _num(t, EFFECTIVE)
    top_u, top_e = names[used.index(max(used))], names[eff.index(max(eff))]
    assert top_u == top_e == "Elections", f"leaders are {top_u!r} and {top_e!r}"
    gains = [n for n, u, e in zip(names, used, eff) if e > u]
    assert gains == ["Interest groups"], f"the channels gaining are {gains}"
    assert sum(eff) == 100, f"the effectiveness column totals {sum(eff):.0f}, not 100"
    return (f"elections lead both columns at {max(used):.0f} and {max(eff):.0f}; only "
            f"{gains[0]!r} is named most effective more than it is used")


def q26(t):
    """The rows are EK 5.3.A.1's four linkage institutions."""
    names = [n.lower() for n in _col(t, CHANNEL)]
    assert names == ["political parties", "interest groups", "elections", "media"], \
        f"the rows are {names}, not EK 5.3.A.1's four in order"
    return "rows are EK 5.3.A.1's four linkage institutions: " + ", ".join(names)


def q27(t):
    """Media is present, is not the least used, and is not the most effective."""
    names, used, eff = _col(t, CHANNEL), _num(t, USED), _num(t, EFFECTIVE)
    i = names.index("Media")
    assert used[i] != min(used), f"media is the least used at {used[i]:.0f}"
    assert used[i] == sorted(used)[-2], "media is not the second most used"
    assert eff[i] != max(eff), "media is the most effective, which the correction denies"
    return (f"media used by {used[i]:.0f} percent, the second highest, and named most "
            f"effective by {eff[i]:.0f}")


def q28(t):
    """Four electorate rows against one government row, and the four take most of the time."""
    directed = [d.strip().lower() for d in _col(t, DIRECTED)]
    time = _num(t, TIME)
    assert directed.count("the electorate") == 4, f"{directed.count('the electorate')} electorate rows"
    assert directed.count("government") == 1, f"{directed.count('government')} government rows"
    assert sum(time) == 100, f"staff time totals {sum(time):.0f}, not 100"
    elec = sum(x for d, x in zip(directed, time) if d == "the electorate")
    gov = sum(x for d, x in zip(directed, time) if d == "government")
    assert elec > gov, f"electorate rows take {elec:.0f} against government {gov:.0f}"
    assert max(time) != gov, "the government row takes the largest share, which the key denies"
    return (f"four electorate rows totalling {elec:.0f} percent against one government row at "
            f"{gov:.0f}; largest single share {max(time):.0f}")


def q29(t):
    """The rows are EK 5.3.B.1's five functions, in order."""
    rows = [r.lower() for r in _col(t, ACTIVITY)]
    assert len(rows) == 5, f"{len(rows)} rows, not five"
    for want, got in zip(("mobilization", "platform", "recruitment", "campaign management",
                          "committee"), rows):
        assert want in got, f"expected {want!r} in row {got!r}"
    return "rows are EK 5.3.B.1's five functions in order"


def q30(t):
    """The government row exists, is nonzero, and is the one the correction names."""
    directed = [d.strip().lower() for d in _col(t, DIRECTED)]
    time, rows = _num(t, TIME), _col(t, ACTIVITY)
    gov = [(r, x) for r, d, x in zip(rows, directed, time) if d == "government"]
    assert len(gov) == 1, f"{len(gov)} government rows, not one"
    label, share = gov[0]
    assert share == 15, f"the government row is {share:.0f} percent, not the 15 keyed"
    assert share > 0, "the government row is zero, so the correction has no figure"
    assert "committee" in label.lower() and "legislature" in label.lower(), \
        f"the government row is {label!r}, not EK 5.3.B.1.v"
    return f"one government row, {label!r}, at {share:.0f} percent of staff time"


# --- module-specific content gates -------------------------------------------

_REVERSED = (
    "channels through which government informs citizens",
    "carry government's decisions to individuals",
    "way for government to keep the public informed",
    "carrying government's decisions outward",
    "communicate government's positions to individuals",
)


def _direction(module):
    """EK 5.3.A.1's arrow runs from individuals to policymakers."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        # An item may NAME the reversal in order to refuse it; items 3 and 27 do
        # exactly that, and a flat scan would report both correct keys.
        refusing = any(w in key for w in ("the other way", "does not determine", "rather than",
                                          "is not what", "reversed"))
        for r in _REVERSED:
            if r in key and not refusing:
                bad.append(f"q{i} key: reverses EK 5.3.A.1's arrow ({r!r}). Linkage "
                           "institutions are channels allowing INDIVIDUALS to communicate "
                           "their preferences TO POLICYMAKERS")
    q1 = module.QUESTIONS[0]
    k1 = q1["choices"][q1["ans"]].lower()
    if "individuals to communicate" not in k1 or "policymakers" not in k1:
        bad.append("q1: the key no longer carries EK 5.3.A.1's definition with its direction")
    q2 = module.QUESTIONS[1]
    if "from individuals to policymakers" not in q2["choices"][q2["ans"]].lower():
        bad.append("q2: the key no longer states the direction of the channel")
    q4 = module.QUESTIONS[3]
    k4 = q4["choices"][q4["ans"]].lower()
    for inst in ("political parties", "interest groups", "elections", "media"):
        if inst not in k4:
            bad.append(f"q4: the key has dropped {inst!r}, one of EK 5.3.A.1's four linkage "
                       "institutions")
    if bad:
        print(f"FAIL {module.__name__} direction")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} direction: no key reverses EK 5.3.A.1's arrow, the definition "
          "keeps its direction, and all four linkage institutions survive")


_FIVE = ("mobilization", "platform", "recruitment", "campaign management", "committee")
_ELECTORATE_ONLY = (
    "parties act only on voters", "parties act only on the electorate",
    "the electorate only", "parties have no role inside government",
)


def _functions(module):
    """EK 5.3.B.1's five functions stay five, and the fifth stays government-facing."""
    bad = []
    q10 = module.QUESTIONS[9]
    k10 = q10["choices"][q10["ans"]].lower()
    for f in _FIVE:
        if f not in k10:
            bad.append(f"q10: the key has dropped {f!r}, one of EK 5.3.B.1's five functions")
    for n in (11, 16):
        key = module.QUESTIONS[n - 1]["choices"][module.QUESTIONS[n - 1]["ans"]].lower()
        if "committee" not in key or "legislature" not in key:
            bad.append(f"q{n}: the key no longer names EK 5.3.B.1.v, the committee and party "
                       "leadership systems in legislatures -- the whole government half of "
                       "LO 5.3.B")
    q9 = module.QUESTIONS[8]
    k9 = q9["choices"][q9["ans"]].lower()
    if "electorate" not in k9 or "government" not in k9:
        bad.append("q9: the key no longer names both halves of LO 5.3.B, the electorate AND "
                   "government")
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        stem = item["q"].lower()
        refusing = "correction" in stem or "incomplete" in stem or "not state" in stem
        for e in _ELECTORATE_ONLY:
            if e in key and not refusing:
                bad.append(f"q{i} key: says {e!r}. EK 5.3.B.1.v places parties inside "
                           "legislatures, and LO 5.3.B names the electorate AND government")
    if bad:
        print(f"FAIL {module.__name__} functions")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} functions: all five of EK 5.3.B.1's functions survive, the "
          "committee and leadership systems stay named as the government-facing one, and no "
          "key confines parties to the electorate")


ua.shape(v5_3)
ua.check(v5_3, ANCHORS, GROUNDING)
ua.notation(v5_3)
_direction(v5_3)
_functions(v5_3)
gc.check(v5_3, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
