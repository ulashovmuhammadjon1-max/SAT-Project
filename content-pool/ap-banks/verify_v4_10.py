"""Structural gate for AP U.S. Government 4.10 Ideology and Social Policy.

gov345_check plus the four usgov_anchor helpers, plus three content gates.

  _three_positions  EK 4.10.A.1 and EK 4.10.A.2 are exact mirrors: the same two
                    variables -- national involvement and state responsibility
                    -- moved in opposite directions. They disagree about WHICH
                    LEVEL should act. EK 4.10.A.3 disagrees about WHETHER EITHER
                    should, restraining national and state government alike with
                    two named exceptions.

                    So the libertarian position is NOT the conservative one
                    taken further, and a student who lines the three up from
                    most government to least has the first two right and the
                    third wrong. The conservative position TRANSFERS
                    responsibility to states; the libertarian position removes
                    the state option that transfer relies on. This is the single
                    structural fact the topic turns on, it is invisible to any
                    check that only looks for the right words, and the gate
                    refuses any key that puts the third position on the axis of
                    the first two.

  _in_parties       EK 4.10.B.1 says policy trends reflect the success of
                    conservative or liberal perspectives IN POLITICAL PARTIES --
                    not in the public, not in the courts, and not their
                    correctness. The prepositional phrase is the mechanism and
                    is the first thing a paraphrase drops. The gate pins it, and
                    refuses any key that relocates the success to the public or
                    evaluates either perspective.

  _no_named_case    The CED lists three Supreme Court cases against this topic
                    and marks all three ILLUSTRATIVE EXAMPLES (NOT REQUIRED).
                    Each is also a live political controversy, which makes
                    naming one doubly wrong here: content the exam cannot ask
                    about, and a contested question dragged into a bank with no
                    business taking a position on it. The gate allows only the
                    CED's fourteen required cases anywhere in the module, and
                    item 24 makes the required-versus-illustrative distinction
                    the question instead.

The three required cases the CED does attach to 4.10.A -- Brown, Engel and Yoder
-- share the feature that makes them usable: each applies a national
constitutional rule against a state or local practice in education or religion,
which is exactly the axis EK 4.10.A.1 and EK 4.10.A.2 describe. They rest on
three different clauses, so item 18 asks for the axis rather than the provision.
"""
import re

import gov345_check as gc
import usgov_anchor as ua
import v4_10

ANCHORS = {
 1: "More national government involvement, with less responsibility left to state",
 2: "Less national government involvement, with more responsibility left to state",
 3: "except when government is protecting private property or individual liberty",
 4: "Which level of government should take primary responsibility",
 5: "so it disagrees about whether either should act rather than about which one should",
 6: "while the libertarian position restrains states too",
 7: "Education and public health",
 8: "When government is protecting private property or individual liberty",
 9: "a tendency within an ideology rather than a position every adherent holds",
 10: "The success of conservative or liberal perspectives in political parties",
 11: "in the parties that nominate and organize officeholders",
 12: "the direction of policy over a period rather than any single enactment",
 13: "so one policy change is weak evidence about the direction of policy",
 14: "Which of the two perspectives produces better social policy",
 15: "which is a shift on the national and state axis those statements describe",
 16: "constraining what state and local school authorities may do",
 17: "A limit on government involvement at the state level in the name of protecting",
 18: "whether a national rule displaces what a state or local authority had been doing",
 19: "accepts differing policies across states as a consequence",
 20: "which favors more national involvement with less responsibility left to states",
 21: "The libertarian position of EK 4.10.A.3",
 22: "reflect the success of conservative or liberal perspectives in political parties",
 23: "import a contested political question the framework does not settle",
 24: "and the second asks how ideologies affect the policy that results",
 25: "rose across the first three periods and then fell slightly in the fourth",
 26: "claim about policy trends concerning the level of government involvement",
 27: "so it cannot identify what produced the movement it shows",
 28: "leads on two of the four issues and primary state responsibility on the other two",
 29: "which describe the liberal, conservative and libertarian positions",
 30: "is a position the framework describes, not an absence of one",
}

GROUNDING = {
 1: "EK 4.10.A.1, verbatim: liberal ideologies 'generally favor more national government "
    "involvement to address some social issues such as education and public health, with less "
    "responsibility for these issues left to state governments.'",
 2: "EK 4.10.A.2, whose structure mirrors EK 4.10.A.1 exactly: the same two variables moved "
    "in opposite directions.",
 3: "EK 4.10.A.3, verbatim, including both exceptions: 'little national or state government "
    "involvement except when national or state government is protecting private property or "
    "individual liberty.'",
 4: "EK 4.10.A.1 against EK 4.10.A.2. Both accept that government addresses social issues and "
    "differ over the balance between national involvement and state responsibility.",
 5: "EK 4.10.A.3 against the two before it. The third statement favors little of either level, "
    "which removes the state option EK 4.10.A.2 relies on.",
 6: "EK 4.10.A.2's TRANSFER of responsibility to states against EK 4.10.A.3's restraint of "
    "both levels. A transfer is not a reduction in total government action, which is why the "
    "third position is not the second taken further.",
 7: "EK 4.10.A.1 and EK 4.10.A.2's shared phrase, 'some social issues such as education and "
    "public health'. Using the same pair in both is what makes them directly comparable.",
 8: "EK 4.10.A.3's two exceptions, which sit inside the position and are why it is not a "
    "position of no government.",
 9: "The word GENERALLY in all three statements, which characterizes a tendency within an "
    "ideology rather than a position every adherent holds on every issue.",
 10: "EK 4.10.B.1, verbatim: 'Policy trends concerning the level of government involvement in "
     "social issues reflect the success of conservative or liberal perspectives in political "
     "parties.'",
 11: "EK 4.10.B.1's prepositional phrase IN POLITICAL PARTIES, which locates the mechanism in "
     "the organizations that nominate and organize officeholders rather than in the public.",
 12: "EK 4.10.B.1's subject, policy TRENDS -- a direction across time rather than any single "
     "enactment.",
 13: "EK 4.10.B.1's subject applied to a one-enactment inference, which is both a single "
     "observation and a backward inference to a cause the observation does not establish.",
 14: "EK 4.10.B.1 read for what it omits: a relationship described, neither perspective "
     "evaluated.",
 15: "Brown v. Board of Education (1954), required case, which the CED attaches to 4.10.A. CED "
     "holding: race-based school segregation violates the equal protection clause. Education "
     "is one of the two social issues EK 4.10.A.1 and EK 4.10.A.2 name.",
 16: "Engel v. Vitale (1962), required case, which the CED attaches to 4.10.A. CED holding: "
     "school sponsorship of religious activities violates the Establishment Clause. A school "
     "district is a state instrumentality, so the holding constrains state and local action.",
 17: "Wisconsin v. Yoder (1972), required case, which the CED attaches to 4.10.A. CED holding: "
     "compelling Amish students to attend school past the eighth grade violates the Free "
     "Exercise Clause. Compulsory attendance is STATE law, so the outcome limits state "
     "involvement on a liberty ground -- the shape EK 4.10.A.3 describes, though the case was "
     "decided on a constitutional clause rather than on any ideology.",
 18: "The three required cases the CED attaches to 4.10.A, which rest on three different "
     "clauses and share only the axis: a national rule applied against a state or local "
     "practice on a social question.",
 19: "CED skill 4.C on a described argument. EK 4.10.A.2 leaves more responsibility to state "
     "governments, and fifty responsible governments can reach different answers, so variation "
     "is a consequence the position accepts.",
 20: "CED skill 4.C. Uniform protection everywhere requires the national government to set the "
     "rule, which is the direction EK 4.10.A.1 describes.",
 21: "CED skill 4.C. The argument restrains government at every level and carves out property "
     "and freedom, which is EK 4.10.A.3's structure with both of its exceptions.",
 22: "CED skill 4.C. EK 4.10.B.1 locates the success that matters for policy trends inside "
     "political parties, which is what the argument asserts, and its implication is that "
     "policy can move without a corresponding movement in public opinion.",
 23: "The CED's distinction between required content and ILLUSTRATIVE EXAMPLES marked NOT "
     "REQUIRED. The examples listed for this topic are also live political disputes, so "
     "presenting one as course content would both misstate the exam and take a side.",
 24: "LO 4.10.A against LO 4.10.B: the positions themselves, described by EK 4.10.A.1 to 3, "
     "against how those positions become policy, which EK 4.10.B.1 routes through parties.",
 25: "Data item, CED skill 4.C. Both columns are recomputed below.",
 26: "EK 4.10.B.1's subject located in the table: how the level of government involvement in "
     "one social policy area changed over four periods.",
 27: "EK 4.10.B.1's mechanism against a table that contains no column measuring a party. A "
     "trend is consistent with the framework's explanation without being evidence for it.",
 28: "Data item, CED skill 4.C. Which column leads each issue is recomputed below.",
 29: "EK 4.10.A.1 to 3 located as the table's three response columns.",
 30: "EK 4.10.A.3 read against a reading of its column as indifference. The column's range is "
     "recomputed below.",
}

NAT, STATE_LOCAL = "National government share (%)", "State and local share (%)"
NAT_R, STATE_R, LITTLE = ("Primarily the national government (%)", "Primarily state governments (%)",
                          "Little involvement at either level (%)")


def _col(t, header):
    j = t["headers"].index(header)
    return [gc.num(r[j]) for r in t["rows"]]


def q25(t):
    """National share rises three times then falls; the two columns are complements."""
    nat, sl = _col(t, NAT), _col(t, STATE_LOCAL)
    for n, s in zip(nat, sl):
        assert n + s == 100, f"a row totals {n + s:.0f}, not 100"
    assert nat[0] < nat[1] < nat[2], f"the national share does not rise three times: {nat}"
    assert nat[3] < nat[2], f"the national share does not fall in the fourth period: {nat}"
    assert nat != sorted(nat), "the national share rises throughout"
    return (f"national share {', '.join(f'{x:.0f}' for x in nat)}; state and local the "
            f"complement; rise of {nat[2] - nat[0]:.0f} then a fall of {nat[2] - nat[3]:.0f}")


def q26(t):
    """The table measures a level of government involvement over periods."""
    heads = [h.lower() for h in t["headers"]]
    assert any("national" in h for h in heads) and any("state" in h for h in heads), \
        f"the two levels are not both present: {heads}"
    assert len(t["rows"]) == 4, f"{len(t['rows'])} periods, not four"
    return f"{len(t['rows'])} periods of a national against state and local division"


def q27(t):
    """No column measures a party, which is the limitation the item names."""
    heads = [h.lower() for h in t["headers"]]
    for h in heads:
        for p in ("party", "parties", "democrat", "republican", "perspective"):
            assert p not in h, \
                f"column {h!r} measures {p!r}, which would weaken the stated limitation"
    assert len(_col(t, NAT)) >= 2, "too few periods to describe a trend at all"
    return f"columns are {', '.join(heads)} -- a trend, and nothing measuring a party"


def _leader(t, row):
    vals = {NAT_R: gc.num(row[1]), STATE_R: gc.num(row[2]), LITTLE: gc.num(row[3])}
    return max(vals, key=lambda k: vals[k])


def q28(t):
    """National leads two issues, state two, and the third column never leads."""
    leaders = [_leader(t, r) for r in t["rows"]]
    assert leaders.count(NAT_R) == 2, f"national leads {leaders.count(NAT_R)} issues"
    assert leaders.count(STATE_R) == 2, f"state leads {leaders.count(STATE_R)} issues"
    assert LITTLE not in leaders, "the third column leads an issue, which the key denies"
    for r in t["rows"]:
        assert sum(gc.num(c) for c in r[1:]) == 100, f"row {r[0]!r} does not total 100"
    return (f"leaders: {', '.join('national' if l == NAT_R else 'state' for l in leaders)}; "
            "rows total 100")


def q29(t):
    """Three response columns, matching the framework's three positions."""
    heads = t["headers"][1:]
    assert len(heads) == 3, f"{len(heads)} response columns, not three"
    low = [h.lower() for h in heads]
    assert "national" in low[0] and "state" in low[1] and "either level" in low[2], \
        f"the three columns do not map onto the framework's three arrangements: {low}"
    return "three response columns: national, state, and little at either level"


def q30(t):
    """The third column is a consistent minority, not an empty one."""
    little = _col(t, LITTLE)
    assert all(x > 0 for x in little), f"the third column reports zero somewhere: {little}"
    assert max(little) - min(little) <= 3, f"the third column is not consistent: {little}"
    assert max(little) < 20, f"the third column reaches {max(little):.0f}, not a minority"
    for r in t["rows"]:
        assert gc.num(r[3]) < max(gc.num(r[1]), gc.num(r[2])), \
            f"the third column leads on {r[0]!r}"
    return (f"third column {', '.join(f'{x:.0f}' for x in little)} -- a consistent minority "
            f"between {min(little):.0f} and {max(little):.0f}, never zero and never leading")


# --- module-specific content gates -------------------------------------------

_ON_THE_AXIS = (
    "the conservative position taken further",
    "libertarian ideologies favor less national involvement and more state",
    "libertarian position favors more state responsibility",
    "just beyond conservative on the same line",
    "the libertarian position is identical to the conservative",
)


def _three_positions(module):
    """The libertarian position is not a further step on the liberal-conservative axis."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        for phrase in _ON_THE_AXIS:
            if phrase in key:
                bad.append(f"q{i} key: places EK 4.10.A.3 on the axis of EK 4.10.A.1 and "
                           f"4.10.A.2 ({phrase!r}). The conservative position TRANSFERS "
                           "responsibility to states; the libertarian position restrains "
                           "states too, which removes the option the transfer relies on")
    pins = {
        1: ("more national government involvement", "liberal"),
        2: ("less national government involvement", "conservative"),
        3: ("little national or state government involvement", "libertarian"),
    }
    for n, (clause, who) in pins.items():
        key = module.QUESTIONS[n - 1]["choices"][module.QUESTIONS[n - 1]["ans"]].lower()
        if clause not in key:
            bad.append(f"q{n}: the {who} key no longer carries the framework's own phrase "
                       f"{clause!r}")
    q3 = module.QUESTIONS[2]
    k3 = q3["choices"][q3["ans"]].lower()
    for exc in ("private property", "individual liberty"):
        if exc not in k3:
            bad.append(f"q3: the libertarian key has dropped {exc!r}; EK 4.10.A.3 names both "
                       "exceptions, and without them the position reads as no government")
    q5 = module.QUESTIONS[4]
    if "whether either should act" not in q5["choices"][q5["ans"]].lower():
        bad.append("q5: the key no longer states the structural difference -- that EK 4.10.A.3 "
                   "disagrees about WHETHER either level should act rather than about which")
    # Items 1 and 2 must be exact mirrors, or the pair has lost its point.
    k1 = module.QUESTIONS[0]["choices"][module.QUESTIONS[0]["ans"]].lower()
    k2 = module.QUESTIONS[1]["choices"][module.QUESTIONS[1]["ans"]].lower()
    if not (("more national" in k1 and "less responsibility" in k1)
            and ("less national" in k2 and "more responsibility" in k2)):
        bad.append("q1 and q2: the two keys are no longer exact mirrors on both variables; EK "
                   "4.10.A.1 and EK 4.10.A.2 move national involvement and state "
                   "responsibility in opposite directions, which is what makes them comparable")
    if bad:
        print(f"FAIL {module.__name__} three positions")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} three positions: EK 4.10.A.1 and 4.10.A.2 stay exact mirrors, "
          "EK 4.10.A.3 keeps both exceptions, and no key treats the libertarian position as "
          "the conservative one taken further")


_RELOCATED = (
    "perspectives in the general public", "success of a perspective with voters",
    "perspectives in the courts", "perspectives among independents",
)
_EVALUATIVE = (
    "produces better social policy", "is the correct perspective",
    "has been shown to be right", "is better for society",
)


def _in_parties(module):
    """EK 4.10.B.1's mechanism stays IN POLITICAL PARTIES, and neither side is judged."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        key = item["choices"][item["ans"]].lower()
        stem = item["q"].lower()
        withholds = "not state" in stem
        for r in _RELOCATED:
            if r in key:
                bad.append(f"q{i} key: relocates EK 4.10.B.1's mechanism to {r!r}; the "
                           "framework says perspectives succeed IN POLITICAL PARTIES")
        for v in _EVALUATIVE:
            if v in key and not withholds:
                bad.append(f"q{i} key: evaluates a perspective ({v!r}); EK 4.10.B.1 describes "
                           "a relationship between party politics and policy direction and "
                           "judges neither side")
    q10 = module.QUESTIONS[9]
    if "political parties" not in q10["choices"][q10["ans"]].lower():
        bad.append("q10: the key no longer carries EK 4.10.B.1's phrase IN POLITICAL PARTIES, "
                   "which is the mechanism the statement names")
    q12 = module.QUESTIONS[11]
    if "over a period" not in q12["choices"][q12["ans"]].lower():
        bad.append("q12: the key no longer records that EK 4.10.B.1's subject is TRENDS rather "
                   "than any single enactment")
    if bad:
        print(f"FAIL {module.__name__} in parties")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} in parties: EK 4.10.B.1's success stays success IN POLITICAL "
          "PARTIES, its subject stays trends, and no key judges either perspective")


_REQUIRED_PAIRS = {
    ("marbury", "madison"), ("mcculloch", "maryland"), ("schenck", "united"),
    ("brown", "board"), ("baker", "carr"), ("engel", "vitale"),
    ("gideon", "wainwright"), ("tinker", "des"), ("co", "united"), ("times", "united"),
    ("wisconsin", "yoder"), ("shaw", "reno"), ("states", "lopez"),
    ("mcdonald", "chicago"), ("united", "federal"), ("united", "fec"),
}
_VS = re.compile(r"([A-Za-z]+)\.?\s+v\.\s+([A-Za-z]+)")


def _no_named_case(module):
    """Only the CED's required cases; this topic's illustrative three are excluded."""
    bad = []
    for i, item in enumerate(module.QUESTIONS, 1):
        strings = [("stem", item["q"]), ("why", item["why"])]
        strings += [(f"choice {'ABCDE'[k]}", c) for k, c in enumerate(item["choices"])]
        for label, s in strings:
            for m in _VS.finditer(s):
                if (m.group(1).lower(), m.group(2).lower()) not in _REQUIRED_PAIRS:
                    bad.append(f"q{i} {label}: names {m.group(0)!r}. The CED marks every case "
                               "it lists for 4.10 an ILLUSTRATIVE EXAMPLE, NOT REQUIRED, and "
                               "each is also a live political controversy -- so naming one "
                               "would be content the exam cannot ask about AND a side taken "
                               "in a dispute the framework does not settle")
    if bad:
        print(f"FAIL {module.__name__} named case")
        for b in bad:
            print("  -", b)
        raise SystemExit(1)
    print(f"OK  {module.__name__} named case: every case named is one of the CED's fourteen "
          "required cases, and none of this topic's three illustrative examples appears")


ua.shape(v4_10)
ua.check(v4_10, ANCHORS, GROUNDING)
ua.notation(v4_10)
_three_positions(v4_10)
_in_parties(v4_10)
_no_named_case(v4_10)
gc.check(v4_10, arith={25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30})
